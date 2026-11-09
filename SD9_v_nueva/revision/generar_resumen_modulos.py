"""Resume el catálogo previsto sin modificar su matriz caso por caso."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
MODULES = (
    "Recepción", "Inventario", "Preventa", "Rutas", "Preparación", "Reparto",
    "Cobranza y rendición", "Devoluciones y envases", "Calidad y trazabilidad",
    "Analítica", "Canal moderno", "Telemetría",
)
MODULE = re.compile(r"(?<![\w-])M(1[0-2]|[1-9])(?![\w-])")

def render(data):
    items, cases = Counter(), Counter()
    for item in data["requirements"]:
        if item["id"].startswith("RT-"):
            key = "RT"
        else:
            modules = set(MODULE.findall(item["component"]))
            key = next(iter(modules)) if len(modules) == 1 else "Varios" if modules else "Sin módulo"
        items[key] += 1
        cases[key] += len(item["cases"])
    items["Integraciones"] = len(data["contracts"])
    cases["Integraciones"] = sum(len(x["cases"]) for x in data["contracts"])
    assert sum(items.values()) == len(data["requirements"]) + len(data["contracts"])
    assert sum(cases.values()) == data["test_count"]
    groups = [(str(i), f"M{i} {name}") for i, name in enumerate(MODULES, 1)] + [
        ("Varios", "RF/RNF con varios módulos mencionados"),
        ("Sin módulo", "RF/RNF sin módulo explícito"),
        ("RT", "Requisitos técnicos del T-12 (incluye brechas sin caso)"),
        ("Integraciones", "Contratos de integración"),
    ]
    lines = [
        "% Generado por revision/generar_resumen_modulos.py; no editar a mano.",
        r"\begin{tablasimple}{>{\hsize=1.9\hsize\linewidth=\hsize}Y >{\hsize=0.55\hsize\linewidth=\hsize}Y >{\hsize=0.55\hsize\linewidth=\hsize}Y}",
        r"  {\cab{Módulo o grupo} & \cab{Filas} & \cab{Casos previstos}}",
    ]
    lines += [f"{name} & {items[key]} & {cases[key]}" + r" \\" for key, name in groups]
    lines += [rf"\textbf{{Total}} & \textbf{{{sum(items.values())}}} & \textbf{{{sum(cases.values()):,}}} \\".replace(",", "."),
              r"\end{tablasimple}",
              r"\fuentesd{Fuente: matriz individual y catálogo de contratos de esta sección; componente ofertado de cada requisito en la versión del T-12 registrada en la matriz.}",
              ""]
    return "\n".join(lines)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = json.loads((ROOT / "revision/matriz_pruebas.json").read_text(encoding="utf-8"))
    result = render(data)
    output = ROOT / "T13/resumen_modulos.tex"
    if args.check:
        if output.read_text(encoding="utf-8") != result:
            raise SystemExit("Resumen por módulo desactualizado.")
        print("Resumen por módulo cotejado con la matriz.")
    else:
        output.write_text(result, encoding="utf-8")
