"""Verificación de coherencia del SD13 contra el T-15 (SD7) y el T-16 (SD8) vigentes.

Lee los archivos de trabajo de los worktrees hermanos (sd7-corrigiendo, sd8-revision),
no commits fijados. Uso: python revision/verificar_coherencia_sd13.py
Sale con código 1 si encuentra algún problema.
"""
from datetime import date
from pathlib import Path
import os
import re
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
WT = HERE.parents[2]
SD7 = Path(os.environ.get("SD7_DIR", WT / "sd7-corrigiendo"))
SD8 = Path(os.environ.get("SD8_DIR", WT / "sd8-revision"))
T15 = SD7 / "formulario-t15" / "tablas"
FILES = {
    "cuerpo": ROOT / "13_innovaciones" / "contenido.tex",
    "t19": ROOT / "T19" / "contenido.tex",
    "anexos": ROOT / "13_anexos" / "contenido.tex",
}
BS = chr(92)
problems = []


def fail(msg):
    problems.append(msg)


def text(name):
    return FILES[name].read_text(encoding="utf-8")


def lines(name):
    return text(name).splitlines()


def t15_rows(name):
    rows = {}
    for line in (T15 / name).read_text(encoding="utf-8").splitlines():
        parts = line.strip().removesuffix(BS * 2).strip().split(" & ")
        if len(parts) > 1:
            rows[parts[0].strip()] = [p.strip() for p in parts]
    return rows


# 1. Códigos antiguos de la EDT (antes de la renumeración por productos del SD7)
OLD = [
    (r"(?<![\d.])3\.10\.[1-4](?:\.[1-4x])?(?!\d)", "cuenta 3.10.x"),
    (r"(?<![\d.])8\.3\.[1-6](?!\d)", "paquete 8.3.x antiguo"),
    (r"(?<![\d.])5\.4\.3(?!\d)", "paquete 5.4.3 antiguo"),
    (r"(?<![\d.])8\.2\.1(?!\d)", "paquete 8.2.1 antiguo"),
    (r"paquete 4\.2\.2(?!\d)", "paquete 4.2.2 antiguo"),
]
for name in FILES:
    for n, line in enumerate(lines(name), 1):
        for pat, label in OLD:
            if re.search(pat, line):
                fail(f"{name}:{n} código antiguo ({label})")

# 2. Montos: la oferta técnica no puede traer precios (Art. 50.2)
MONEY = [r"\bUF\b", r"\bCLP\b", r"\bUSD\b", BS + r"\$ ?\d", r"\$ ?\d[\d.]* ?(millones|mil)\b"]
for name in FILES:
    for n, line in enumerate(lines(name), 1):
        for pat in MONEY:
            if re.search(pat, line):
                fail(f"{name}:{n} posible monto ({pat})")

# 3. Paquetes y meses contra el T-15 (tabla de asignación de partidas)
asig = {}
for line in (T15 / "tab_T15_asignacion_partidas.tex").read_text(encoding="utf-8").splitlines():
    m = re.match(r"\s*(7\.[1-5]\.[1-6]) & .*? & [A-Z]{2,4} & (\d+)–(\d+) & ", line)
    if m:
        asig[m.group(1)] = (int(m.group(2)), int(m.group(3)))
if len(asig) != 23:
    fail(f"T-15: se esperaban 23 paquetes de la cuenta 7 y hay {len(asig)}")
row_re = re.compile(r"^INN-0\d\.P\d & (7\.\d\.\d) & (\d+)(?: a | y )(\d+) &")
for name in ("cuerpo",):
    for n, line in enumerate(lines(name), 1):
        m = row_re.match(line)
        if m:
            code, a, b = m.group(1), int(m.group(2)), int(m.group(3))
            if code not in asig:
                fail(f"{name}:{n} paquete {code} no existe en el T-15")
            elif asig[code] != (a, b):
                fail(f"{name}:{n} {code} meses {a}-{b}; el T-15 dice {asig[code][0]}-{asig[code][1]}")
for name in FILES:
    for n, line in enumerate(lines(name), 1):
        for code in re.findall(r"(?<![\d.])7\.[1-5]\.[1-6](?!\d)", line):
            if code not in asig:
                fail(f"{name}:{n} paquete {code} no existe en el T-15")

# 4. Fechas: toda fecha dd-mm-aaaa debe salir del T-15
known = set()
for f in ("tab_T15_paquetes.tex", "tab_T15_cpm_detalle.tex", "tab_T15_7.tex", "tab_T15_5.tex"):
    known |= set(re.findall(r"\d{2}-\d{2}-\d{4}", (T15 / f).read_text(encoding="utf-8")))
for name in FILES:
    for n, line in enumerate(lines(name), 1):
        for d in re.findall(r"(?<!\d)\d{2}-\d{2}-\d{4}(?!\d)", line):
            if d not in known:
                fail(f"{name}:{n} fecha {d} no figura en el T-15")


def month_of(d):  # mes 1 = febrero de 2027
    dd, mm, yy = map(int, d.split("-"))
    return (yy - 2027) * 12 + mm - 1


for hito, d, esperado in (("H4", "20-10-2027", 9), ("H5", "24-11-2027", 10), ("H10", "27-06-2028", 17)):
    if month_of(d) != esperado:
        fail(f"{hito}: la entrega {d} cae en el mes {month_of(d)}, se esperaba {esperado}")
    if d not in known:
        fail(f"{hito}: fecha {d} ausente del T-15")

# 5. Riesgo R-027 contra el T-16
t16 = (SD8 / "LAFROX-Formulario-T-16.tex").read_text(encoding="utf-8")
r027 = next((l for l in t16.splitlines() if l.startswith("R-027 &") and "Dado que" in l), "")
if "3 / 0,50" not in r027 or "0,10 (Media)" not in r027:
    fail("T-16: R-027 ya no figura con p0 = 3 / 0,50 y exposición 0,10 (Media); revisar el SD13")
for name in FILES:
    for n, line in enumerate(lines(name), 1):
        if "R-027" in line and re.search(r"p_0\$ (?:de|=) 25", line):
            fail(f"{name}:{n} R-027 con p0 = 25 %: el valor inicial es 40 %, el 25 % es el residual")

# 6. Citas y referencias (APA 7): cada entrada se cita y cada cita tiene entrada
ITEM = BS + "item "
for name in FILES:
    t = text(name)
    i = t.find(BS + "section*{Referencias}")
    if i < 0:
        fail(f"{name}: sin sección Referencias")
        continue
    body, refs = t[:i], t[i:]
    entries = [l.strip()[len(ITEM):] for l in refs.splitlines() if l.strip().startswith(ITEM)]
    keys = []
    for e in entries:
        m = (re.match(r"(Distribuidora Puelche S\.A\.|DORA|European Commission|GS1 AISBL)\.? \((\d{4}[a-z]?)\)", e)
             or re.match(r"([^.(]+?)[,.] .*?\((\d{4}[a-z]?)\)", e)
             or re.match(r"(Ley [\d.]+) de (\d{4})", e))
        if not m:
            fail(f"{name}: entrada sin año reconocible: {e[:50]}")
            continue
        keys.append((m.group(1).strip(), m.group(2)))
    sorted_keys = sorted(keys, key=lambda k: k[0].lower().replace(" ", ""))
    if [k[0] for k in keys] != [k[0] for k in sorted_keys]:
        fail(f"{name}: la lista de referencias no está en orden alfabético")
    for author, year in keys:
        base = author.split(",")[0]
        if base not in body:
            fail(f"{name}: la referencia {author} ({year}) no se cita en el texto")
    cited = set(re.findall(r"Distribuidora Puelche S\.A\., (2026[a-z])", body))
    listed = {y for a, y in keys if a.startswith("Distribuidora")}
    for y in cited - listed:
        fail(f"{name}: se cita Distribuidora Puelche S.A. {y} y falta en la lista")

# 7. Texto que rompe la ficción de la licitación
for name in FILES:
    for n, line in enumerate(lines(name), 1):
        if re.search(r"\b(Informe [123]|TODO|FIXME|profesor|curso)\b|pendiente de revisión", line):
            fail(f"{name}:{n} texto de proceso interno o ajeno a la licitación")

print("Coherencia SD13:", "OK" if not problems else f"{len(problems)} problema(s)")
for p in problems:
    print(" -", p)
sys.exit(1 if problems else 0)
