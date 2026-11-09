"""Comprueba la actualización interna del SD9 contra el catálogo fuente.

No ejecuta casos ni certifica cumplimiento: valida IDs, estados y aritmética.
Los conteos esperados se recalculan desde matriz_pruebas.json y su commit
fuente; la prosa del SD9 y del T-13 debe publicar esas mismas cifras.
"""
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
from math import ceil
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
source_rows = {}
for line in source.splitlines():
    if re.match(r"\s*(?:RF|RNF|RT)-\d", line):
        cells = [c.strip() for c in line.strip().removesuffix(r"\\").split(" & ")]
        source_states[cells[0]] = cells[2]
        source_rows[cells[0]] = cells
assert set(ids) == set(source_states)
assert all(x["state"] == source_states[x["id"]] for x in requirements)
own = [x for x in requirements if not x["id"].startswith("RT-")]
rt = [x for x in requirements if x["id"].startswith("RT-")]
assert len(own) == counts["own"] and len(rt) == counts["rt"]
# Cotejo de origen y criterio con el catálogo original, no solo con los totales.
expected_catalogue = {}
for filename in ("rf_caso", "rf_btt", "rf_propios", "rnf_caso", "rnf_btt", "rnf_propios"):
    text = subprocess.check_output(
        ["git", "show", data["source_commit"] + f":tablas_anexo/{filename}.tex"], cwd=ROOT
    ).decode("utf-8")
    for line in text.splitlines():
        if not re.match(r"\s*(?:RF|RNF)-\d", line):
            continue
        cells = line.strip().removesuffix(r"\\").split(" & ")
        identifier = cells[0].strip()
        if filename == "rf_btt" and identifier in {f"RF-14.0{i}" for i in range(1, 6)}:
            identifier += "-BTT"
        assert identifier not in expected_catalogue, identifier
        criterion_col = 4 if filename.startswith("rf_") else 2
        expected_catalogue[identifier] = (cells[-1].strip(), cells[criterion_col].strip())
assert set(expected_catalogue) == {item["id"] for item in own}
for item in requirements:
    identifier = item["id"]
    t12 = source_rows[identifier]
    assert (item["component"], item["edt"]) == (t12[3], t12[4]), identifier
    expected = expected_catalogue.get(identifier, (f"Bases Técnicas Transversales, {identifier}", t12[1]))
    assert item["origin"] and item["criterion"] and (item["origin"], item["criterion"]) == expected, identifier
priority = Counter(x["priority"] for x in own)
rt_state = Counter(x["state"] for x in rt)
assert priority == counts["priority"] and rt_state == counts["rt_state"]
source_priorities = {}
for filename in ("rf_caso", "rf_btt", "rf_propios", "rnf_caso", "rnf_btt", "rnf_propios"):
    catalogue = subprocess.check_output(
        ["git", "show", f"{data['source_commit']}:tablas_anexo/{filename}.tex"], cwd=ROOT
    ).decode("utf-8")
    for line in catalogue.splitlines():
        row = re.match(r"\s*((?:RF|RNF)-[\d.]+(?:-BTT)?)\s+&", line)
        if not row:
            continue
        identifier = row[1]
        if filename == "rf_btt" and re.fullmatch(r"RF-14\.0[1-5]", identifier):
            identifier += "-BTT"
        match = re.search(r"&\s*(Crítica|Alta|Media)\s*/\s*([^&]+)&", line)
        assert match and identifier not in source_priorities, identifier
        source_priorities[identifier] = (match[1], match[2].strip())
assert {x["id"]: (x["priority"], x["stage"]) for x in own} == source_priorities
cases_by_priority = {"Crítica": 5, "Alta": 3, "Media": 2}
for item in own:
    assert len(item["cases"]) == cases_by_priority[item["priority"]], item["id"]
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
    for stale in ("1.316", "1.053", "263 casos", "262 RF", "18 RT en estado", "SCAMPI", "1.352", "0e0e0f39"):
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
# Dimensionamiento de la regresión y escenarios de falla a partir de la matriz.
automatic = int((Decimal(counts["cases"]) * Decimal("0.80")).quantize(Decimal(1), rounding=ROUND_HALF_UP))
manual_cases = counts["cases"] - automatic
automatic_hours = Decimal(automatic) * 30 / 3600
manual = Decimal(manual_cases) * 15 / 60
internal = manual + 8 + 16 + 4
external = manual + 8 + 24 + 8 + 4
event_sum = internal + external
baseline = 12016

def decimal_es(value, places=1):
    rounded = value.quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_UP)
    return f"{rounded:.{places}f}".replace(".", ",")

distribution = f"{num(automatic)} automáticos y {num(manual_cases)} manuales"
hours_one = decimal_es(automatic_hours, 2)
hours_two = decimal_es(automatic_hours / 2, 2)
manual_hours = decimal_es(manual)
cal_hours = decimal_es(manual + 8)
internal_hours, external_hours = decimal_es(internal), decimal_es(external)
for text in (body, t13):
    assert distribution in text and hours_one in text and hours_two in text
    assert f"{manual_hours} HH por ciclo" in text
assert f"{manual_cases} casos indivisibles" in t13
assert f"{ceil(manual_cases / 16)} tandas" in t13
assert f"{ceil(manual / Decimal('6.4'))} evaluadores-día" in t13
for phrase in (
    f"{manual_cases} casos a 15 minutos", f"{manual_hours} HH",
    f"Calidad (CAL) & {cal_hours} & {cal_hours}",
    f"{internal_hours} × nI + {external_hours} × nE",
    f"representa {num(int(event_sum))} HH",
    f"{num(baseline)} + {num(int(event_sum))} = {num(int(baseline + event_sum))} HH",
):
    assert phrase in annex, phrase
assert f"{internal_hours} HH por falla interna y {external_hours} HH por falla externa" in body
assert "V1–V21" in t13 and "Para RF-09.06" in t13
matrix = (ROOT / "T13/matriz_requisitos.tex").read_text(encoding="utf-8")
assert matrix.count("0; brecha visible") == counts["rt_without_case"] == rt_state["No cumple"]
assert "RF-\\allowbreak{}09.11" in matrix
assert matrix.count("Matriz individual: bloque") == counts["blocks"]
matrix_rows = [line for line in matrix.splitlines() if line.startswith(r"\textbf{") and r"\newline " in line]
assert len(matrix_rows) == counts["requirements"]
for row, item in zip(matrix_rows, requirements, strict=True):
    identifier = item["id"].replace("-", r"-\allowbreak{}")
    assert row.startswith(rf"\textbf{{{identifier}}}\newline {item['origin']} & "), item["id"]
    display = item.get('component_display', item['component'])
    if 'component_display' in item:
        assert rf'\emph{{T-12, fila {identifier}}}' in display, item['id']
    assert rf"{display}\newline \textbf{{EDT:}} {item['edt']} & " in row, item["id"]
    assert rf" & {item['criterion']}\newline \emph{{" in row, item["id"]
    if not item["id"].startswith("RT-"):
        assert re.search(r"; H(?:5|10|5 y H10) & ", row), item["id"]
assert rf"hsize={num(counts['cases'])}" not in t13  # La cifra de casos no es un ancho de columna.
print(f"OK ({data['source_commit'][:8]}): {counts['t12_rows']} filas T-12; {counts['requirements']} requisitos, "
      f"{counts['aliases']} alias, {counts['contracts']} contratos y {num(counts['cases'])} casos previstos.")
print(f"OK: {distribution}; {manual_hours} HH/ciclo y fallas {internal_hours}/{external_hours} HH.")
