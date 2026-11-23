"""Verificación de coherencia del SD13 contra los formularios y subdocumentos vigentes.

Lee los archivos de trabajo de los worktrees hermanos en modo solo lectura,
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
SD3 = Path(os.environ.get("SD3_DIR", WT / "sd3-corrigiendo"))
SD5 = Path(os.environ.get("SD5_DIR", WT / "sd5-corrigiendo"))
SD7 = Path(os.environ.get("SD7_DIR", WT / "sd7-corrigiendo"))
SD8 = Path(os.environ.get("SD8_DIR", WT / "sd8-revision"))
SD9 = Path(os.environ.get("SD9_DIR", WT / "sd9-corrigiendo"))
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
for f in ("tab_T15_paquetes.tex", "tab_T15_cpm_detalle.tex", "tab_T15_7.tex",
          "tab_T15_5.tex", "tab_T15_subsanacion.tex"):
    known |= set(re.findall(r"\d{2}-\d{2}-\d{4}", (T15 / f).read_text(encoding="utf-8")))
for name in FILES:
    for n, line in enumerate(lines(name), 1):
        for d in re.findall(r"(?<!\d)\d{2}-\d{2}-\d{4}(?!\d)", line):
            if d not in known:
                fail(f"{name}:{n} fecha {d} no figura en el T-15")


def month_of(d):  # mes 1 = febrero de 2027
    dd, mm, yy = map(int, d.split("-"))
    return (yy - 2027) * 12 + mm - 1


hitos = t15_rows("tab_T15_7.tex")
anexos = text("anexos")
for hito, mes_entrega, paquete in (("H4", 9, "6.1.1"), ("H5", 11, "6.7.1"), ("H10", 17, "6.7.2")):
    fila = hitos[hito]
    entrega = fila[1]
    if month_of(entrega) != mes_entrega or fila[-1] != paquete:
        fail(f"{hito}: revisar mes de entrega o paquete controlante en la tabla de hitos del T-15")
    fechas_anexo = re.findall(rf"\b{hito} el (\d{{2}}-\d{{2}}-\d{{4}})\b", anexos)
    if fechas_anexo != [entrega]:
        fail(f"anexos: entrega {hito} {fechas_anexo}; el T-15 indica {entrega}")

acta_h5 = hitos["H5"][2]
if f"la firma del acta es posterior, el {acta_h5}" not in anexos:
    fail(f"anexos: la firma de H5 debe figurar por separado el {acta_h5}")

# No confundir entrega, firma, corte ni ventana en caso de subsanación.
_, acta_h12, corte_h12, limite_h12 = hitos["H12"][1:5]
corte_subsanacion = t15_rows("tab_T15_subsanacion.tex")["H12"][2]
for name in ("cuerpo", "t19"):
    if acta_h12 not in text(name) or corte_h12 not in text(name):
        fail(f"{name}: faltan el acta ({acta_h12}) o el corte ({corte_h12}) nominales de H12")
if corte_subsanacion not in anexos or limite_h12 not in anexos:
    fail("anexos: la ventana con subsanación o el límite de H12 no coinciden con el T-15")

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

# 8. Restos de la numeración antigua y texto de proceso que no debe entregarse
FORBIDDEN = [
    (r"fase 5 de la EDT", "INN-04 ya no está en la fase 5"),
    (r"cuentas? 3\.8\b|3\.8\.[17]\b|3\.9\.6\b", "paquete controlante antiguo de un hito"),
    (r"carta editable|Pauta de revisión|versión final|se entregarán|que sigue pendiente", "texto de proceso interno"),
    (r"13\.x\b|13\.N\.7", "marcador sin resolver"),
    (r"desde el mes 22, frente de Operación|y desde el mes 22 el mantenimiento", "traspaso a Operación fuera del mes 21"),
    (r"Sandra Riffo, p\. 14|Katherine Ñanco, p\. 16", "página de entrevista del Caso incorrecta"),
    (r"precio máximo", "término no definido en las Bases"),
    (r"(?<![\w\\])\d+" + re.escape(BS) + "%", "porcentaje sin espacio antes de \\%"),
]
for name in FILES:
    for n, line in enumerate(lines(name), 1):
        for pat, label in FORBIDDEN:
            if re.search(pat, line):
                fail(f"{name}:{n} {label}")

# 9. Paquetes controlantes de H4, H5 y H10 en el Anexo 13.B (T-15, tab_T15_7)
for code in ("6.1.1", "6.7.1", "6.7.2"):
    if code not in text("anexos"):
        fail(f"anexos: falta el paquete controlante {code}")

# 10. Aritmética de los escenarios físicos y su presencia en el Anexo 13.B
assert 2_400_000 * 1 * 25 // (100 * 100) == 6_000 and 6_000 * (56 - 16 + 1) == 246_000
assert round(52 / 12 * 36) == 156 and round(52 / 12 * 36 * 2) == 312
lots = 1_150 * 1_100 / 8_400
assert round(lots, 1) == 150.6 and round(lots * 0.05 * 0.20, 1) == 1.5 and round(lots * 0.05 * 0.20 * 41) == 62
assert 420_000 * 5 // 100 == 21_000
assert round(62_000 * 11_600 / 14_200) == 50_648 and round(62_000 * 11_600 / 14_200 * 10 * 0.20) == 101_296
assert 2_400_000 * 15 // 10_000 * 25 // 100 == 900
assert (20 / 24, 19 / 24) == (0.8333333333333334, 0.7916666666666666)
for frag in ("6.000 unidades", "156 minutos", "312 minutos-persona", "150,6 recepciones", "1,5 lotes",
             "21.000 kilómetros", "101.296 minutos", "50.648 decisiones", "20 de 24"):
    if frag not in text("anexos"):
        fail(f"anexos: falta la cifra «{frag}» de los escenarios físicos")

# 11. No confundir evidencia de QA con ahorro en terreno ni contar dos veces RT-05.30.
t12 = (SD3 / "LAFROX-Formulario-T-12.tex").read_text(encoding="utf-8")
t13 = (SD9 / "SD9_v_nueva/T13/matriz_requisitos.tex").read_text(encoding="utf-8")
t12_early = next((l for l in t12.splitlines() if l.strip().startswith("RT-26.08 &")), "")
t13_early = next((l for l in t13.splitlines() if r"26.08}\newline" in l), "")
if any(not all(x in row for x in ("I-02A", "7.2.4")) for row in (t12_early, t13_early)):
    fail("RT-26.08: revisar el indicador temprano y su paquete contra T-12 y T-13")
for name in FILES:
    doc = text(name)
    if not any("I-02A" in l and "RT-26.08" in l for l in doc.splitlines()):
        fail(f"{name}: falta distinguir I-02A como evidencia temprana del RT-26.08")
    if "20 pares operativos acumulados" not in doc or "corte inicial" not in doc.lower():
        fail(f"{name}: no distingue el corte del mes 15 de la muestra acumulada de I-02E")
    if re.search(r"no se presenta como respuesta al RT-05\.30", doc):
        fail(f"{name}: contradice la respuesta ofertada en RT-05.30")

t12_model = next((l for l in t12.splitlines() if l.strip().startswith("RT-05.30 &")), "")
sd5_data = (SD5 / "05_modelo_datos/partes/5_1_modelo.tex").read_text(encoding="utf-8")
if not all(x in t12_model for x in ("determinista", "I-03B")) or "RT-05.30 se oferta" not in sd5_data:
    fail("RT-05.30: revisar el alcance del modelo determinista contra T-12 y SD5")
if "Se declara una sola vez como capacidad analítica" not in text("cuerpo"):
    fail("cuerpo: no separa el modelo RT-05.30 de su incorporación operacional")

# 12. El hito nominal y la ventana de valorización no son la misma fecha.
row_732 = t15_rows("tab_T15_paquetes.tex")["7.3.2"]
inn_03_p2 = next((l for l in lines("cuerpo") if l.startswith("INN-03.P2 &")), "")
if not all(d in inn_03_p2 for d in row_732[4:6]):
    fail("cuerpo: 7.3.2 no distingue ventana de asignación y fechas de la carta nivelada")
dic_75 = (SD7 / "formulario-t14/tablas/dic_7_5.tex").read_text(encoding="utf-8")
for name in FILES:
    rows = [l for l in lines(name) if "I-05A" in l and "dos visitas" in l]
    if not rows or "dentro de dos visitas" not in dic_75:
        fail(f"{name}: I-05A debe conservar las dos visitas del criterio 7.5.5")
fichas = re.split(r"\\section\*\{Ficha \d — Innovación \d\}", text("t19"))[1:]
if len(fichas) != 5 or any(re.findall(r"^(\d+)\. .+? &", f, flags=re.M) !=
                           [str(i) for i in range(1, 18)] for f in fichas):
    fail("t19: deben existir cinco fichas con los campos 1 a 17 en orden")

print("Coherencia SD13:", "OK" if not problems else f"{len(problems)} problema(s)")
for p in problems:
    print(" -", p)
sys.exit(1 if problems else 0)
