"""Comprueba SD9 contra las tablas publicadas del SD7, no certifica su CPM.

Uso desde cualquier carpeta: python verificar_alineacion_sd7.py [ref-SD7]
La referencia por defecto fija la versión usada en esta actualización.
"""
from decimal import Decimal
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REF = sys.argv[1] if len(sys.argv) > 1 else "d496da939ffd2b4a6e88d6281a7e35dd08c19f01"


def source(path):
    return subprocess.check_output(
        ["git", "show", f"{REF}:{path}"], cwd=ROOT
    ).decode("utf-8")


def num(text):
    return Decimal(text.replace(".", "").replace(",", "."))


def rows(text):
    for line in text.splitlines():
        if " & " in line and line.rstrip().endswith(r"\\"):
            yield [x.strip() for x in line.strip().removesuffix(r"\\").split(" & ")]


packages = {
    r[0]: r for r in rows(source("formulario-t15/tablas/tab_T15_paquetes.tex"))
    if re.fullmatch(r"\d+(?:\.\d+)+", r[0])
}
milestones = {
    r[0]: r for r in rows(source("formulario-t15/tablas/tab_T15_7.tex"))
    if re.fullmatch(r"H\d+", r[0])
}
body = (ROOT / "09_plan_calidad/contenido.tex").read_text(encoding="utf-8")
annex = (ROOT / "09_anexos/contenido.tex").read_text(encoding="utf-8")
t13 = (ROOT / "T13/contenido.tex").read_text(encoding="utf-8")
t17 = (ROOT / "T17/contenido.tex").read_text(encoding="utf-8")

campaigns = 0
for r in rows(t13):
    if len(r) == 6 and r[1] in packages and re.fullmatch(r"\d{2}-\d{2}-\d{4}", r[3]):
        expected = packages[r[1]]
        assert r[3:5] == expected[4:6], (r[1], r[3:5], expected[4:6])
        if r[5].isdigit():
            assert num(r[5]) == num(expected[3]), (r[1], r[5], expected[3])
        campaigns += 1
assert campaigns == 25, campaigns

acts = 0
for r in rows(t17):
    if len(r) == 5 and re.fullmatch(r"H\d+ \(\d+\)", r[0]):
        h = r[0].split()[0]
        m = milestones[h]
        # Columnas T-15: entrega, acta, paso a producción, límite, margen de firma, margen de corte.
        margen = m[5] if m[6] == "—" else f"{m[5]} firma / {m[6]} corte"
        assert r[1:] == [m[1], m[2], m[4], margen], (h, r[1:], m[1:7])
        acts += 1
assert acts == 10, acts

# El esfuerzo de frío (922,66 HH) forma parte de la línea base del T-15.
cold = sum(num(packages[p][3]) for p in ("2.7.1", "2.7.2", "2.7.3"))
assert cold == Decimal("922.66")
conformity = annex[annex.index(r"\subsection*{9.C.1 "):annex.index(r"\subsection*{9.C.2")]
totals = {"Prevención": Decimal(0), "Evaluación": Decimal(0)}
for r in rows(conformity):
    if r[0] in totals:
        totals[r[0]] += Decimal(r[-1].replace(".", "").replace(",", "."))
assert totals == {"Prevención": Decimal(4224), "Evaluación": Decimal("7834.66")}, totals
assert sum(totals.values()) == Decimal("12058.66")
linea_base = Decimal("203548.62")
proporcion = sum(totals.values()) / linea_base
assert round(proporcion, 4) == Decimal("0.0592")
assert round(proporcion * 100, 1) == Decimal("5.9")
assert len(packages) == 171
for documento in (body, annex):
    assert r"5,9 \%" in documento and "203.548,62" in documento
assert "203.548,62 HH y 230 paquetes" in t13
matriz = (ROOT / "T13/matriz_requisitos.tex").read_text(encoding="utf-8")
asignaciones = {
    "RF-17.02": "3.3.4",
    "RT-16.14": "3.3.4",
    "RF-17.08": "3.3.5",
    "RF-17.09": "3.3.6",
}
for identificador, paquete in asignaciones.items():
    assert paquete in packages
    marca = r"\textbf{" + identificador.replace("-", r"-\allowbreak{}") + "}"
    (fila,) = (linea for linea in matriz.splitlines() if linea.startswith(marca))
    assert rf"\textbf{{EDT:}} {paquete} & " in fila
    if identificador == "RF-17.09":
        assert "PDF, DOCX y XLSX" in fila and r"\newline Cumple; " in fila
for text in (body, annex, t13, t17):
    assert "217.543" not in text
    assert "11.136" not in text
    # C15 eliminó el prefijo de capítulo: las secciones 4/5/6 son válidas.
    assert not re.search(r"T-15, secci(?:ón|ones) 7\.[456](?:\.|\b)", text)
assert "35,0" in body and "65,0" in body
assert "fechas y holguras del escenario nominal del T-15" in t17
assert "reproduce las fechas del SD7" in t17
print(f"OK: {campaigns} campañas, {acts} hitos; 12.058,66 HH = 4.224 + 7.834,66; referencia {REF}.")
print("La comprobación acredita sincronización documental, no nivelación ni aceptación del CLIENTE.")
