"""Comprueba la actualización interna del SD9 contra el catálogo fuente.

No ejecuta casos ni certifica cumplimiento: valida IDs, estados y aritmética.
Los conteos esperados se recalculan desde matriz_pruebas.json y su commit
fuente; la prosa del SD9 y del T-13 debe publicar esas mismas cifras.
"""
from collections import Counter
from decimal import Decimal
from pathlib import Path
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "revision/matriz_pruebas.json").read_text(encoding="utf-8"))
requirements, aliases, contracts, counts = (data[k] for k in ("requirements", "aliases", "contracts", "counts"))
assert len(requirements) == counts["requirements"] and len(aliases) == counts["aliases"]
assert len(contracts) == counts["contracts"]
ids = [x["id"] for x in requirements + aliases]
assert len(set(ids)) == len(ids) == counts["t12_rows"]
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
assert len(own) == counts["own"] and len(rt) == counts["rt"]
priority = Counter(x["priority"] for x in own)
rt_state = Counter(x["state"] for x in rt)
assert priority == counts["priority"] and rt_state == counts["rt_state"]
assert all(not x["cases"] for x in rt if x["state"] == "No cumple")
cases = [case for x in requirements + contracts for case in x["cases"]]
assert len(cases) == len(set(cases)) == data["test_count"] == counts["cases"]
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


def num(value):
    return f"{value:,}".replace(",", ".")


published = {
    "SD9 9.2.4": (body, [
        f"{num(counts['own'])} RF/RNF: {priority['Crítica']} críticos, {priority['Alta']} altos y {priority['Media']} medios",
        f"{num(rt_state['Cumple'])} RT cumplidos, {rt_state['Cumple parcialmente']} parciales y {rt_state['No cumple']} no cumplidos",
        f"{num(rt_state['Cumple'] + rt_state['Cumple parcialmente'])} RT con casos previstos",
        f"{num(counts['cases'])} casos únicos",
    ]),
    "T-13 8.2": (t13, [
        f"Los {num(counts['own'])} RF y RNF con prioridad propia",
        f"Los {rt_state['No cumple']} RT en estado «No cumple»",
        f"Las {rt_state['Cumple parcialmente']} respuestas parciales",
        data["source_commit"][:8],
    ]),
}
for where, (text, phrases) in published.items():
    for phrase in phrases:
        assert phrase in text, f"{where}: falta «{phrase}»"
assert "líneas modificadas" in body and "líneas modificadas" in annex
assert "ninguna persona ni comité levanta una puerta fallida" in body
assert "AL-CLI-01" in t13 and "Integración E2 (3.9.1)" in t13
assert "15 de 15 interfaces sin error con el alcance de E2 integrado" in t17
assert "Benchmark" in body
# Reparto de planificación publicado en SD9 9.2.4: debe sumar el catálogo vigente.
assert 1082 + 270 == counts["cases"], "el reparto automático/manual no suma el catálogo"
manual = Decimal(270) * Decimal(15) / Decimal(60)
assert manual == Decimal("67.5")
assert manual + 8 + 16 + 4 == Decimal("95.5")
assert manual + 8 + 24 + 8 + 4 == Decimal("111.5")
assert Decimal(12016) + Decimal("95.5") + Decimal("111.5") == Decimal(12223)
assert "12.223" in annex and "67,5" in annex
matrix = (ROOT / "T13/matriz_requisitos.tex").read_text(encoding="utf-8")
assert matrix.count("0; brecha visible") == counts["rt_without_case"] == rt_state["No cumple"]
assert "RF-\\allowbreak{}09.11" in matrix
assert matrix.count("Matriz individual: bloque") == counts["blocks"]
assert all(row.rstrip().endswith((" H5 \\\\", " H10 \\\\", " H5 y H10 \\\\"))
           for row in matrix.splitlines()
           if re.match(r"(RF|RNF)-", row) and " & 0 \\" not in row), "fila sin hito"
assert r"hsize=1.352" not in t13  # La cifra de casos no es un ancho de columna.
print(f"OK ({data['source_commit'][:8]}): {counts['t12_rows']} filas T-12; {counts['requirements']} requisitos, "
      f"{counts['aliases']} alias, {counts['contracts']} contratos y {num(counts['cases'])} casos previstos.")
print("OK: 1.082 automáticos + 270 manuales; 67,5 HH/ciclo y fallas 95,5/111,5 HH.")
