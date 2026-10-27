"""Genera la matriz prevista del T-13 desde el SD3, sin inventar ejecución.

La prioridad y el criterio pertenecen al catálogo SD3; cumplimiento y EDT al
T-12. Los identificadores /Pnn son casos previstos, no resultados aprobados.
Uso: python generar_matriz_pruebas.py [ref-SD3]
"""
from collections import Counter
from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REF = sys.argv[1] if len(sys.argv) > 1 else "33508bb3"


def source(path):
    return subprocess.check_output(
        ["git", "show", f"{REF}:{path}"], cwd=ROOT
    ).decode("utf-8")


def rows(text):
    for line in text.splitlines():
        if re.match(r"\s*(?:RF|RNF|RT)-\d", line):
            yield [c.strip() for c in line.strip().removesuffix(r"\\").split(" & ")]


def break_id(value):
    return value.replace("-", r"-\allowbreak{}")


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
        assert identifier not in catalogue, identifier
        catalogue[identifier] = {
            "priority": match[1], "stage": match[2], "table": table, "source_id": cells[0],
            "criterion": cells[4] if filename.startswith("rf_") else cells[2],
            "verification": "Precondición y resultado esperado" if filename.startswith("rf_") else cells[3],
        }
assert len(catalogue) == 270
assert Counter(v["priority"] for v in catalogue.values()) == {"Crítica": 64, "Alta": 163, "Media": 43}

t12 = list(rows(source("LAFROX-Formulario-T-12.tex")))
assert len(t12) == 653 and len({c[0] for c in t12}) == 653
data = []
aliases = []
for c in t12:
    identifier, state, component, work = c[0], c[2], c[3], c[4]
    if identifier in catalogue:
        item = catalogue[identifier]
        count = {"Crítica": 5, "Alta": 3, "Media": 2}[item["priority"]]
        data.append({"id": identifier, "state": state, "component": component, "edt": work,
                     **item, "cases": [f"{identifier}/P{i:02}" for i in range(1, count + 1)]})
    elif identifier.startswith("RT-"):
        count = 0 if state == "No cumple" else 1
        data.append({"id": identifier, "state": state, "component": component, "edt": work,
                     "priority": "RT", "stage": "Según T-12 y T-14", "table": "T12.2",
                     "criterion": c[1], "verification": "Verificación del requisito y del alcance ofertado",
                     "cases": [f"{identifier}/P01"] if count else []})
    else:
        aliases.append({"id": identifier, "component": component, "cases": []})
assert len(data) == 644 and len(aliases) == 9
assert Counter(x["state"] for x in data if x["id"].startswith("RT-")) == {
    "Cumple": 324, "Cumple parcialmente": 28, "No cumple": 22,
}

contracts = [{"id": f"INT-{i:02}", "stage": "E2" if i == 8 else "E1; regresión E2",
              "cases": [f"INT-{i:02}/P{n:02}" for n in range(1, 8)]} for i in range(1, 16)]
assert sum(len(x["cases"]) for x in data + contracts) == 1352
all_cases = [c for x in data + contracts for c in x["cases"]]
assert len(all_cases) == len(set(all_cases))

lines = [
    "% Generado por revision/generar_matriz_pruebas.py; no editar a mano.",
]
for index, item in enumerate(data):
    # xltabular mide la tabla completa: limitar cada bloque evita exceder maxdimen.
    if index % 50 == 0:
        lines += [
            r"\begin{tablasimple}{Y Y Y Y Y}",
            f"{{\\multicolumn{{5}}{{l}}{{\\textbf{{Matriz individual: bloque {index // 50 + 1} de 13.}}}} \\\\",
            r"\cab{Requisito} & \cab{Criterio verificable en la fuente} & \cab{Casos previstos} & \cab{Paquete T-12} & \cab{Estado / prioridad / etapa}}",
        ]
    identifier = item["id"]
    criterion = (f"SD3, Tabla {item['table']}, fila {break_id(item['source_id'])}"
                 if not identifier.startswith("RT-") else f"T-12, Parte B, fila {break_id(identifier)}")
    cases = f"/P01 a /P{len(item['cases']):02}" if len(item["cases"]) > 1 else "/P01" if item["cases"] else "0; brecha visible"
    state = {"Cumple parcialmente": "Parcial", "No cumple": "No cumple"}.get(item["state"], item["state"])
    lines.append(" & ".join([break_id(identifier), criterion, cases, item["edt"],
                             f"{state}; {item['priority']}; {item['stage']}"]) + r" \\")
    if index % 50 == 49 or index == len(data) - 1:
        lines += [r"\end{tablasimple}", ""]
lines += [
          "Las nueve filas absorbidas o alias conservan su disposición en el T-12 y no añaden casos independientes:",
          r"\begin{tablasimple}{Y Y Y}",
          r"{\cab{Fila} & \cab{Disposición vigente del T-12} & \cab{Casos adicionales}}"]
for item in aliases:
    lines.append(f"{break_id(item['id'])} & {item['component']} & 0" + r" \\")
lines += [r"\end{tablasimple}", "",
          r"\begin{tablasimple}{Y Y Y}",
          r"{\cab{Contrato} & \cab{Casos previstos} & \cab{Etapa de aceptación}}"]
for item in contracts:
    lines.append(f"{item['id']} & /P01 a /P07 & {item['stage']}" + r" \\")
lines += [r"\end{tablasimple}", ""]
(ROOT / "T13/matriz_requisitos.tex").write_text("\n".join(lines), encoding="utf-8")
payload = {"source_ref": REF, "source_commit": subprocess.check_output(
    ["git", "rev-parse", REF], cwd=ROOT, text=True).strip(),
    "test_count": len(all_cases), "requirements": data, "aliases": aliases, "contracts": contracts}
(ROOT / "revision/matriz_pruebas.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
print("OK: 644 requisitos, 9 alias, 15 contratos y 1.352 casos previstos; ningún resultado ejecutado.")
