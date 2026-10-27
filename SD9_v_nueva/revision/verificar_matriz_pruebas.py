"""Comprueba la actualización interna del SD9 contra el catálogo fuente.

No ejecuta casos ni certifica cumplimiento: valida IDs, estados y aritmética.
"""
from collections import Counter
from decimal import Decimal
from pathlib import Path
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "revision/matriz_pruebas.json").read_text(encoding="utf-8"))
requirements, aliases, contracts = (data[k] for k in ("requirements", "aliases", "contracts"))
assert len(requirements) == 644 and len(aliases) == 9 and len(contracts) == 15
ids = [x["id"] for x in requirements + aliases]
assert len(set(ids)) == len(ids) == 653
source = subprocess.check_output(
    ["git", "show", data["source_commit"] + ":LAFROX-Formulario-T-12.tex"], cwd=ROOT
).decode("utf-8")
source_states = {}
for line in source.splitlines():
    if re.match(r"\s*(?:RF|RNF|RT)-\d", line):
        cells = [c.strip() for c in line.strip().removesuffix(r"\\").split(" & ")]
        source_states[cells[0]] = cells[2]
assert set(ids) == set(source_states)
assert all(x["state"] == source_states[x["id"]] for x in requirements)
own = [x for x in requirements if not x["id"].startswith("RT-")]
rt = [x for x in requirements if x["id"].startswith("RT-")]
assert len(own) == 270 and len(rt) == 374
assert Counter(x["priority"] for x in own) == {"Crítica": 64, "Alta": 163, "Media": 43}
assert Counter(x["state"] for x in rt) == {"Cumple": 324, "Cumple parcialmente": 28, "No cumple": 22}
assert all(not x["cases"] for x in rt if x["state"] == "No cumple")
cases = [case for x in requirements + contracts for case in x["cases"]]
assert len(cases) == len(set(cases)) == data["test_count"] == 1352
assert contracts[7]["id"] == "INT-08" and contracts[7]["stage"] == "E2"

body, annex, t13, t17 = [
    (ROOT / folder / "contenido.tex").read_text(encoding="utf-8")
    for folder in ("09_plan_calidad", "09_anexos", "T13", "T17")
]
for text in (body, annex, t13, t17):
    prose = re.sub(r"hsize=\d+(?:\.\d+)?", "", text)
    for stale in ("1.316", "1.053", "263 casos", "262 RF", "18 RT en estado", "SCAMPI"):
        assert stale not in prose, stale
    assert "SD6, sección 6.1.3" not in text
assert r"\input{T13/matriz_requisitos.tex}" in t13
assert "644" not in body or "374" in body
assert "líneas modificadas" in body and "líneas modificadas" in annex
assert "ninguna persona ni comité levanta una puerta fallida" in body
assert "AL-CLI-01" in t13 and "Integración E2 (3.9.1)" in t13
assert "15 de 15 interfaces sin error con el alcance de E2 integrado" in t17
assert "Benchmark" in body
manual = Decimal(270) * Decimal(15) / Decimal(60)
assert manual == Decimal("67.5")
assert manual + 8 + 16 + 4 == Decimal("95.5")
assert manual + 8 + 24 + 8 + 4 == Decimal("111.5")
assert Decimal(12016) + Decimal("95.5") + Decimal("111.5") == Decimal(12223)
assert "12.223" in annex and "67,5" in annex
matrix = (ROOT / "T13/matriz_requisitos.tex").read_text(encoding="utf-8")
assert matrix.count("0; brecha visible") == 22
assert "RF-\\allowbreak{}09.11" in matrix
assert matrix.count("Matriz individual: bloque") == 13
assert r"hsize=1.352" not in t13  # La cifra de casos no es un ancho de columna.
print("OK: 653 filas T-12 trazadas; 644 requisitos, 9 alias, 15 contratos y 1.352 casos previstos.")
print("OK: 1.082 automáticos + 270 manuales; 67,5 HH/ciclo y fallas 95,5/111,5 HH.")
