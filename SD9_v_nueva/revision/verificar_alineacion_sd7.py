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
REF = sys.argv[1] if len(sys.argv) > 1 else "70aed659"


def source(path):
    return subprocess.check_output(
        ["git", "show", f"{REF}:{path}"], cwd=ROOT
    ).decode("utf-8")


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
            assert Decimal(r[5]) == Decimal(expected[3]), r[1]
        campaigns += 1
assert campaigns == 25, campaigns

acts = 0
for r in rows(t17):
    if len(r) == 5 and re.fullmatch(r"H\d+ \(\d+\)", r[0]):
        h = r[0].split()[0]
        assert r[1:] == milestones[h][1:5], (h, r[1:], milestones[h][1:5])
        acts += 1
assert acts == 10, acts

# Las 880 HH ya están dentro de T-15, no se agregan a 220.023.
cold = sum(Decimal(packages[p][3]) for p in ("2.4.3", "2.4.4", "4.1.4"))
assert cold == 880
conformity = annex[annex.index("Prevención & 1.2.4"):annex.index(r"\subsection*{9.C.2")]
totals = {"Prevención": Decimal(0), "Evaluación": Decimal(0)}
for r in rows(conformity):
    if r[0] in totals:
        totals[r[0]] += Decimal(r[-1].replace(".", "").replace(",", "."))
assert totals == {"Prevención": Decimal(4224), "Evaluación": Decimal(7792)}, totals
assert sum(totals.values()) == 12016
assert round(Decimal(12016) / Decimal(220023) * 100, 1) == Decimal("5.5")
for text in (body, annex, t13, t17):
    assert "217.543" not in text
    assert "11.136" not in text
    assert not re.search(r"T-15, secci(?:ón|ones) [456](?:\.|\b)", text)
assert "35,2" in body and "64,8" in body
assert "se toman del T-15 vigente" in t17
assert "cuya revisión humana fue confirmada por el usuario" in body
assert "revisión humana está pendiente" not in body
assert "revisión humana de esta actualización pendiente" not in body
print(f"OK: {campaigns} campañas, {acts} hitos; 12.016 HH = 4.224 + 7.792; referencia {REF}.")
print("La comprobación acredita sincronización documental, no nivelación ni aceptación del CLIENTE.")
