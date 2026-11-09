"""Genera la matriz prevista del T-13 desde el SD3, sin inventar ejecución.

La prioridad y el criterio pertenecen al catálogo SD3; cumplimiento y EDT al
T-12. Los identificadores /Pnn son casos previstos, no resultados aprobados.
Los conteos se derivan del catálogo de la referencia indicada y se guardan en
matriz_pruebas.json; no se fijan en el código.
Uso: python generar_matriz_pruebas.py [ref-SD3]
"""
from collections import Counter
from math import ceil
from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REF = sys.argv[1] if len(sys.argv) > 1 else "3d0eeea70c16ea3a6c5dfb3f539d8892fb865005"
BLOCK = 25
CASES_BY_PRIORITY = {"Crítica": 5, "Alta": 3, "Media": 2}
CONTRACTS, CASES_BY_CONTRACT = 15, 7
WORDS = dict(enumerate("cero una dos tres cuatro cinco seis siete ocho nueve".split()))


def source(path):
    return subprocess.check_output(
        ["git", "show", f"{REF}:{path}"], cwd=ROOT
    ).decode("utf-8")


def rows(text):
    for line in text.splitlines():
        if re.match(r"\s*(?:RF|RNF|RT)-\d", line):
            yield [c.strip() for c in line.strip().removesuffix(r"\\").split(" & ")]


# Hito de certificación al que aporta evidencia cada etapa (T-17, sección 4.2).
MILESTONE = {"E1": "H5", "E2": "H10", "E1 y E2": "H5 y H10", "E1; regresión E2": "H5 y H10"}


def break_id(value):
    return value.replace("-", r"-\allowbreak{}")


# Las tres descripciones de equipos más extensas se resumen por componente.
# Se conserva el texto íntegro del T-12 en el JSON y se cita la fila en el PDF.
COMPONENT_SUMMARIES = {
    "RNF-23.01": "Equipos de terreno y operación (T-11): B-01, B-02, kit B-03 a B-14 y SIM B-15; incluye accesorios y consumibles.",
    "RNF-23.02": "TC58e, MC9400 estándar y Cold Storage Freezer, ZQ620 Plus, termógrafo EYE SENSOR, balanza Dibal, ZT411, PAX A920 Pro y kit de frío B-03 a B-11.",
    "RT-08.11": "MC9400 estándar y Cold Storage Freezer, TC58e de reparto y preventa, ZQ620 Plus, PAX A920 Pro, baterías y cargadores, UPS B-13 y protección B-14.",
}

catalogue = {}
tables = {
    "rf_caso.tex": "3.A.1", "rf_btt.tex": "3.A.3", "rf_propios.tex": "3.A.3b",
    "rnf_caso.tex": "3.A.4", "rnf_btt.tex": "3.A.5", "rnf_propios.tex": "3.A.5b",
}
for filename, table in tables.items():
    for cells in rows(source("tablas_anexo/" + filename)):
        identifier = cells[0]
        if filename == "rf_btt.tex" and identifier in {f"RF-14.0{i}" for i in range(1, 6)}:
            identifier += "-BTT"
        match = next(
            re.search(r"(Crítica|Alta|Media)\s*/\s*(.*)", c)
            for c in cells if re.search(r"(Crítica|Alta|Media)\s*/", c)
        )
        assert len(cells) == (7 if filename.startswith("rf_") else 6), (filename, identifier)
        assert identifier not in catalogue, identifier
        assert cells[-1], (filename, identifier, "origen vacío")
        catalogue[identifier] = {
            "priority": match[1], "stage": match[2], "table": table, "source_id": cells[0],
            "origin": cells[-1],
            "criterion": cells[4] if filename.startswith("rf_") else cells[2],
            "verification": "Precondición y resultado esperado" if filename.startswith("rf_") else cells[3],
        }
assert catalogue, "catálogo SD3 vacío"

t12 = list(rows(source("LAFROX-Formulario-T-12.tex")))
t12_ids = {c[0] for c in t12}
assert len(t12) == len(t12_ids), "filas T-12 duplicadas"
assert set(catalogue) <= t12_ids, sorted(set(catalogue) - t12_ids)
data = []
aliases = []
for c in t12:
    identifier, state, component, work = c[0], c[2], c[3], c[4]
    if identifier in catalogue:
        item = catalogue[identifier]
        count = CASES_BY_PRIORITY[item["priority"]]
        data.append({"id": identifier, "state": state, "component": component, "edt": work,
                     **item, "cases": [f"{identifier}/P{i:02}" for i in range(1, count + 1)]})
    elif identifier.startswith("RT-"):
        count = 0 if state == "No cumple" else 1
        data.append({"id": identifier, "state": state, "component": component, "edt": work,
                     "priority": "RT", "stage": "Según T-12 y T-14", "table": "T12.2",
                     "origin": f"Bases Técnicas Transversales, {identifier}",
                     "criterion": c[1], "verification": "Verificación del requisito y del alcance ofertado",
                     "cases": [f"{identifier}/P01"] if count else []})
    else:
        aliases.append({"id": identifier, "component": component, "cases": []})

contracts = [{"id": f"INT-{i:02}", "stage": "E2" if i == 8 else "E1; regresión E2",
              "cases": [f"INT-{i:02}/P{n:02}" for n in range(1, CASES_BY_CONTRACT + 1)]}
             for i in range(1, CONTRACTS + 1)]
all_cases = [c for x in data + contracts for c in x["cases"]]
assert len(all_cases) == len(set(all_cases))

own = [x for x in data if not x["id"].startswith("RT-")]
rt = [x for x in data if x["id"].startswith("RT-")]
counts = {
    "t12_rows": len(t12), "requirements": len(data), "aliases": len(aliases),
    "own": len(own), "rt": len(rt), "contracts": len(contracts), "cases": len(all_cases),
    "priority": dict(Counter(x["priority"] for x in own)),
    "rt_state": dict(Counter(x["state"] for x in rt)),
    "rt_without_case": sum(1 for x in rt if not x["cases"]),
    "blocks": ceil(len(data) / BLOCK),
}

lines = [
    "% Generado por revision/generar_matriz_pruebas.py; no editar a mano.",
]
for index, item in enumerate(data):
    # xltabular mide la tabla completa: limitar cada bloque evita exceder maxdimen.
    if index % BLOCK == 0:
        lines += [
            r"\begin{tablasimple}{>{\hsize=0.82\hsize\linewidth=\hsize}Y >{\hsize=1.04\hsize\linewidth=\hsize}Y >{\hsize=0.65\hsize\linewidth=\hsize}Y >{\hsize=1.49\hsize\linewidth=\hsize}Y}",
            f"{{\\multicolumn{{4}}{{l}}{{\\textbf{{Matriz individual: bloque {index // BLOCK + 1} de {counts['blocks']}.}}}} \\\\",
            r"\cab{Requisito y origen} & \cab{Componente y EDT} & \cab{Prueba prevista y estado} & \cab{Criterio y fuente}}",
        ]
    identifier = item["id"]
    component = item["component"]
    if identifier in COMPONENT_SUMMARIES:
        component = COMPONENT_SUMMARIES[identifier] + rf"\newline \emph{{T-12, fila {break_id(identifier)}}}"
        item["component_display"] = component
    criterion_ref = (f"SD3, Tabla {item['table']}, fila {break_id(item['source_id'])}"
                     if not identifier.startswith("RT-") else f"T-12, Parte B, fila {break_id(identifier)}")
    cases = f"/P01 a /P{len(item['cases']):02}" if len(item["cases"]) > 1 else "/P01" if item["cases"] else "0; brecha visible"
    state = {"Cumple parcialmente": "Parcial", "No cumple": "No cumple"}.get(item["state"], item["state"])
    timing = f"; {item['stage']}; {MILESTONE[item['stage']]}" if item["stage"] in MILESTONE else ""
    lines.append(" & ".join([
        rf"\textbf{{{break_id(identifier)}}}\newline {item['origin']}",
        rf"{component}\newline \textbf{{EDT:}} {item['edt']}",
        rf"{cases}\newline {state}; {item['priority']}{timing}",
        rf"{item['criterion']}\newline \emph{{{criterion_ref}}}",
    ]) + r" \\")
    if index % BLOCK == BLOCK - 1 or index == len(data) - 1:
        lines += [r"\end{tablasimple}", ""]
lines += [
          f"Las {WORDS.get(len(aliases), len(aliases))} filas absorbidas o alias conservan su disposición en el T-12 y no añaden casos independientes:",
          r"\begin{tablasimple}{Y Y Y}",
          r"{\cab{Fila} & \cab{Disposición vigente del T-12} & \cab{Casos adicionales}}"]
for item in aliases:
    lines.append(f"{break_id(item['id'])} & {item['component']} & 0" + r" \\")
lines += [r"\end{tablasimple}", "",
          r"\begin{tablasimple}{Y Y Y}",
          r"{\cab{Contrato} & \cab{Casos previstos} & \cab{Etapa de aceptación / hito}}"]
for item in contracts:
    lines.append(f"{item['id']} & /P01 a /P{CASES_BY_CONTRACT:02} & {item['stage']}; {MILESTONE[item['stage']]}" + r" \\")
lines += [r"\end{tablasimple}", ""]
(ROOT / "T13/matriz_requisitos.tex").write_text("\n".join(lines), encoding="utf-8")
payload = {"source_ref": REF, "source_commit": subprocess.check_output(
    ["git", "rev-parse", REF], cwd=ROOT, text=True).strip(),
    "test_count": len(all_cases), "counts": counts,
    "requirements": data, "aliases": aliases, "contracts": contracts}
(ROOT / "revision/matriz_pruebas.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"OK ({REF}): {json.dumps(counts, ensure_ascii=False)}; ningún resultado ejecutado.")
