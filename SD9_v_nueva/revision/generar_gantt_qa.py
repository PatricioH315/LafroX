"""Subdivide ventanas de QA publicadas sin modificar la línea base.
Uso: python revision/generar_gantt_qa.py [--check] [--ref COMMIT]
"""
import argparse
from datetime import date, timedelta
from pathlib import Path
import re
import shutil
import subprocess
import xml.etree.ElementTree as ET

REF = "68669befd04babce61e9fb4d8f5e6b29d28f46aa"
HERE = Path(__file__).resolve().parent
GIT_WIN = Path(r"C:\Program Files\Git\cmd\git.exe")
GIT = str(GIT_WIN) if GIT_WIN.is_file() else shutil.which("git")
ANNEX = HERE.parent / "09_anexos/contenido.tex"
OUTPUT = HERE / "Gantt_Calidad_9E.gan"
T15 = "formulario-t15/contenido.tex"
TEMPLATE = "imagenes/Diagramas que faltaban/Fig_7_Gantt_Resumen_Dependencias.gan"
SPLITS = {"3.4.7", "3.4.8", "3.5.1", "3.5.2", "3.5.3", "3.5.4"}
ROW = re.compile(r"^\s*(3\.[45]\.\d+) & (20\d\d) & (\d\d/[\d/ ,\-]+?)\s*\\\\\s*$", re.M)
DAY = timedelta(days=1)


def source(ref, path):
    return subprocess.check_output([GIT, "show", f"{ref}:{path}"], cwd=HERE).decode("utf-8")


def relief(day):
    """Backup role by month, per Anexo 9.E (roles with hours valued that month)."""
    return "Líder de Calidad y Pruebas" if (day.year, day.month) in {(2027, 8), (2027, 9), (2027, 10)} else "Analista QA Junior"


def windows(text):
    def as_date(s, y):
        d, m = map(int, s.split("/"))
        return date(int(y), m, d)
    return {
        code: [tuple(as_date(d, year) for d in span.split("--"))
               for span in spans.split(", ")]
        for code, year, spans in ROW.findall(text)
    }


def generate(ref):
    published = windows(source(ref, T15))
    assert published == windows(ANNEX.read_text(encoding="utf-8"))
    assert len(published) == 15 and sum(map(len, published.values())) == 77
    root = ET.fromstring(source(ref, TEMPLATE))
    root.set("name", "LafroX | Control de Calidad por ventanas (Anexo 9.E)")
    root.set("view-date", "2027-06-10")
    root.find("description").text = (
        f"Capa de QA propuesta sobre el T-15 ({ref[:8]}). Días corridos para visualizar. "
        "Sin asignación aprobada ni cambio de hitos, paquetes o fechas oficiales."
    )
    cal = root.find("calendars")
    for node in cal.findall("date"):
        cal.remove(node)
    week = cal.find("day-types/default-week")
    for key in ("sun", "mon", "tue", "wed", "thu", "fri", "sat"):
        week.set(key, "0")
    tasks = root.find("tasks")
    for node in tasks.findall("task"):
        tasks.remove(node)
    for key in ("resources", "allocations", "vacations", "previous"):
        root.find(key).clear()
    seen = set()
    count = 0
    for code, spans in published.items():
        refined = []
        for i, (start, end) in enumerate(spans):
            days = (end - start).days + 1
            if days > 14:
                assert i == len(spans) - 1 and code in SPLITS
                seen.add(code)
                pivot = start + DAY * (days // 2)
                refined.extend(((start, pivot - DAY), (pivot, end)))
            else:
                refined.append((start, end))
        assert refined[0][0] == spans[0][0] and refined[-1][1] == spans[-1][1]
        assert all(a[1] + DAY == b[0] for a, b in zip(refined, refined[1:]))
        assert all(any(a <= start <= end <= b for a, b in spans) for start, end in refined)
        for i, (start, end) in enumerate(refined, 1):
            days = (end - start).days + 1
            assert 1 <= days <= 14
            gate = ("Contrato y criterios" if i == 1 else "Entrega integrada en QA"
                    if i == len(refined) else "Demostración y regresión")
            task = ET.SubElement(tasks, "task", {
                "id": str(count), "name": f"{code} · {i}/{len(refined)} · {gate}",
                "color": "#2864a3", "meeting": "false", "start": str(start),
                "duration": str(days), "complete": "0", "expand": "true",
            })
            ET.SubElement(task, "notes").text = (
                f"Ventana de QA (ambos extremos incluidos): {start} a {end}. "
                f"Titular: Analista QA Senior; relevo: {relief(start)}; turno diurno hábil "
                "09:00-18:00 en QA (Anexo 9.E). El Líder de Calidad registra "
                "versión, casos, resultados y defectos; el Líder Funcional valida el "
                "incremento. No sustituye la certificación integral."
            )
            count += 1
    assert seen == SPLITS and count == 83
    ET.indent(root, space="    ")
    return ET.tostring(root, encoding="utf-8", xml_declaration=True) + b"\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--ref", default=REF)
    args = parser.parse_args()
    payload = generate(args.ref)
    if args.check:
        assert OUTPUT.read_text(encoding="utf-8") == payload.decode("utf-8"), "Gantt de QA desactualizada"
    else:
        OUTPUT.write_bytes(payload)
    print("15 paquetes, 83 ventanas (6 desdobladas), todas <= 14 días; extremos preservados.")


if __name__ == "__main__":
    main()
