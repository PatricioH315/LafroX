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
from textwrap import shorten

from generar_resumen_modulos import MODULE, MODULES

ROOT = Path(__file__).resolve().parents[1]
REF = sys.argv[1] if len(sys.argv) > 1 else "8b0a224fe6ba7f37e91a653268b0621a5f326d01"
BLOCK = 30
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


def component_summary(item):
    """Keep the visible description short and resolve the exact T-12 cell by ID."""
    if item["state"] == "No cumple":
        return "Brecha declarada"
    component = item["component"]
    modules = sorted({int(m) for m in MODULE.findall(component)})
    if modules:
        return ", ".join(f"M{m} {MODULES[m - 1]}" for m in modules)
    if not component or component.strip() in {"—", "--", "No aplica"}:
        return "Componente por confirmar"
    if len(component) <= 115:
        return component
    prefix = re.split(r"[;$\\{}]", component, maxsplit=1)[0].strip()
    if not prefix:
        return "Ver componente ofertado"
    return shorten(prefix, width=115, placeholder="…") + ("…" if prefix != component and len(prefix) <= 115 else "")


def origin_reference(item, filename, table):
    origin = item[-1]
    if not any(c.isalnum() for c in origin):
        return f"Origen por confirmar (SD3, Tabla {table}, fila {break_id(item[0])})"
    if filename == "rnf_caso.tex" and origin.startswith("Cap."):
        origin = "Caso, " + origin
    if origin.startswith("Propio LafroX"):
        return f"SD3, Tabla {table}, fila {break_id(item[0])}" + (
            "; " + origin.split("Fuente: ", 1)[1] if "Fuente: " in origin else ""
        )
    return origin


def planned_cases(item):
    if not item["cases"]:
        return "0; brecha visible"
    if item["id"].startswith("RT-"):
        if item["id"] == "RT-03.13":
            return "/P01 declaración y sincronización; AL-OFF-01"
        return "/P01 (evidencia de la exigencia ofertada)"
    labels = [
        "/P01 conforme", "/P02 no conforme", "/P03 límite",
        "/P04 falla", "/P05 integridad",
    ]
    if item["id"] == "RF-01.02":
        labels[:2] = ["/P01 ingreso con lote válido", "/P02 intento con lote vacío"]
    elif item["id"] == "RNF-03.02":
        labels[:2] = ["/P01 consulta de stock y crédito en peak", "/P02 respuesta que excede 2 s"]
    return "; ".join(labels[:len(item["cases"])])


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
            "origin": origin_reference(cells, filename, table),
            "criterion": cells[4] if filename.startswith("rf_") else cells[2],
            "verification": "Precondición y resultado esperado" if filename.startswith("rf_") else cells[3],
        }
assert catalogue, "catálogo SD3 vacío"

alias_sources = {}
for filename, table in (
    ("materias_funcionales_complementarias.tex", "3.A.3a"),
    ("condiciones_rectoras_rnf.tex", "3.A.5a"),
):
    for cells in rows(source("tablas_anexo/" + filename)):
        if cells[0] in catalogue:
            continue
        covered = re.search(r"(?:RT|RF|RNF)-\d+\.\d+(?:-BTT)?", cells[2])
        assert covered, cells[0]
        alias_sources[cells[0]] = (covered[0], table)

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
        chapter = int(identifier[3:5])
        origin = f"BTT, cap. {chapter}, {break_id(identifier)}"
        if re.search(r"Caso, cap\. 15", c[1], flags=re.IGNORECASE):
            origin += f"; Caso, cap. 15, {break_id(identifier)}"
        data.append({"id": identifier, "state": state, "component": component, "edt": work,
                      "origin": origin, "priority": "RT", "stage": "Según T-12 y T-14", "table": "T12.2",
                     "criterion": c[1], "verification": "Verificación del requisito y del alcance ofertado",
                     "cases": [f"{identifier}/P01"] if count else []})
    else:
        covered_by, alias_table = alias_sources[identifier]
        aliases.append({"id": identifier, "component": component, "covered_by": covered_by,
                        "source_table": alias_table, "cases": []})

by_id = {item["id"]: item for item in data}
assert {alias["id"] for alias in aliases} == set(alias_sources)
assert all(alias["covered_by"] in by_id for alias in aliases)

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
            r"\begin{tablasimple}{>{\hsize=1.14\hsize\linewidth=\hsize}Y >{\hsize=1.12\hsize\linewidth=\hsize}Y >{\hsize=0.92\hsize\linewidth=\hsize}Y >{\hsize=1.12\hsize\linewidth=\hsize}Y >{\hsize=0.70\hsize\linewidth=\hsize}Y}",
            f"{{\\multicolumn{{5}}{{l}}{{\\textbf{{Matriz individual: bloque {index // BLOCK + 1} de {counts['blocks']}.}}}} \\\\",
            r"\cab{Requisito y origen} & \cab{Componente y paquete EDT} & \cab{Pruebas previstas} & \cab{Criterio verificable} & \cab{Estado, etapa e hito}}",
        ]
    identifier = item["id"]
    source_row = f"T-12, Parte {'B' if identifier.startswith('RT-') else 'A'}, {break_id(identifier)}"
    if identifier.startswith("RT-"):
        criterion = f"{source_row}, descripción y alcance ofertado"
    else:
        field = "resultado esperado" if identifier.startswith("RF-") else "umbral y verificación"
        criterion = f"SD3, Tabla {item['table']}, {break_id(item['source_id'])}, {field}"
    state = {"Cumple parcialmente": "Parcial", "No cumple": "No cumple"}.get(item["state"], item["state"])
    component = component_summary(item)
    if identifier == "RF-01.02":
        criterion += r"\newline Lote válido registrado; sin lote se muestra «Lote requerido para este producto» y se impide avanzar."
    elif identifier == "RNF-03.02":
        criterion += r"\newline Consulta conectada en hasta 2 s."
    lines.append(" & ".join([
        break_id(identifier) + r"\newline " + item["origin"],
        component + r"\newline " + source_row + r"\newline EDT " + item["edt"],
        planned_cases(item),
        criterion,
        f"{state}; {item['priority']}; {item['stage']}" + (f"; {MILESTONE[item['stage']]}" if item['stage'] in MILESTONE else ""),
    ]) + r" \\")
    if index % BLOCK == BLOCK - 1 or index == len(data) - 1:
        lines += [r"\end{tablasimple}", ""]
lines += [
          f"Las {WORDS.get(len(aliases), len(aliases))} filas absorbidas o alias conservan su disposición en el T-12 y no añaden casos independientes:",
          r"\begin{tablasimple}{Y Y Y}",
          r"{\cab{Alias y origen} & \cab{Requisito que lo cubre} & \cab{Casos adicionales}}"]
for item in aliases:
    parent = by_id[item["covered_by"]]
    link = break_id(parent["id"])
    if not parent["cases"]:
        link += " (brecha visible)"
    lines.append(f"{break_id(item['id'])}; SD3, Tabla {item['source_table']} & {link} & 0" + r" \\")
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
