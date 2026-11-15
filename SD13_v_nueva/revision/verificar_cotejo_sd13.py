"""Verificación documental de SD13: fechas, red, sesiones del mes 15 y estimaciones base."""
from datetime import datetime, timedelta
from math import ceil
from pathlib import Path
import re
import shutil
import subprocess
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
WIN_GIT = Path(r"C:\Program Files\Git\cmd\git.exe")
GIT = str(WIN_GIT) if WIN_GIT.is_file() else shutil.which("git")
SD7 = "c088f82cc96b3f25d947858a4b0f055b9e0a3b9c"
CASE = "1a8340ebf525b455ee38225294edbf8a20357df4"
T15 = "formulario-t15/tablas/"


def read(ref, name):
    return subprocess.check_output([GIT, "show", f"{ref}:{name}"], cwd=HERE).decode("utf-8")


def table(name):
    return {r[0]: r for line in read(SD7, T15 + name).splitlines()
            if (r := line.strip().removesuffix(r"\\").strip().split(" & "))
            and len(r) > 1}


def date(text):
    return datetime.strptime(text, "%d-%m-%Y").date()


def dates_and_links():
    rows = table("tab_T15_paquetes.tex")
    cpm = table("tab_T15_cpm_detalle.tex")
    milestones = table("tab_T15_7.tex")
    gantt = ET.parse(HERE / "Gantt_Innovaciones_13B.gan")
    all_tasks = gantt.findall(".//task")
    tasks = {task.get("name").split()[0]: task for task in all_tasks if task.get("meeting") == "false"}
    markers = [task for task in all_tasks if task.get("meeting") == "true"]
    assert len(markers) == 3
    assert len({task.get("id") for task in all_tasks}) == len(all_tasks)
    assert {task.get("name").split(" · ")[1] for task in markers} == {
        f"3.10.{i}.4" for i in range(1, 4)}
    assert all((m.get("start"), m.get("duration")) == ("2028-04-03", "26")
               and m.get("name").startswith("EV-15-0")
               and not m.findall("depend") for m in markers)
    budget = table("tab_T15_2.tex")
    t15 = read(SD7, "formulario-t15/contenido.tex")
    assert "E se reparte uniformemente entre los meses inclusivos" in t15
    for i, role in ((1, "DAT"), (2, "CAL"), (3, "DAT")):
        assert budget[f"3.10.{i}.4"][1:4] == ["E", role, "11–15"]
    assert set(tasks) == {f"3.10.{i}.{j}" for i in range(1, 5) for j in range(1, 5)} | {"5.4.3"}
    assert not gantt.findall("./allocations/*")
    ids = {task.get("id"): code for code, task in tasks.items()}
    edges = set()
    expected = set()
    for code, task in tasks.items():
        start, end = map(date, rows[code][4:6])
        assert (task.get("start"), int(task.get("duration"))) == (start.isoformat(), (end - start).days + 1)
        for pred in re.findall(r"3\.10\.[1-4]\.[1-4]", rows[code][6]):
            if date(rows[pred][5]) < start:
                expected.add((pred, code))
        for link in task.findall("depend"):
            succ = ids[link.get("id")]
            assert link.get("type") == "2"
            gap = date(rows[succ][4]) - end - timedelta(days=1)
            assert int(link.get("difference")) == gap.days >= 0
            edges.add((code, succ))
    assert edges == expected and len(edges) == 7
    for i in range(1, 4):
        code = f"3.10.{i}.4"
        assert (rows[code][5], cpm[code][3], cpm[code][5]) == (
            "28-04-2028", "28-12-2027", "28-04-2028")
    assert [(h, milestones[h][1], rows[milestones[h][-1]][5])
            for h in ("H4", "H5", "H10")] == [
                ("H4", "20-10-2027", "22-10-2027"),
                ("H5", "24-11-2027", "01-12-2027"),
                ("H10", "27-06-2028", "28-06-2028"),
            ]
    print("17 paquetes, 7 enlaces y 3 sesiones del mes 15 (3 al 28 de abril de 2028); fechas H4/H5/H10 cotejadas.")


def physical_examples():
    case = read(CASE, "Bases/Caso_02_Logistica.md")
    assert re.search(r"Unidades despachadas al mes.*2,4 millones", case)
    for fig in ("31.000", "≈ 62.000", "14.200", "11.600"):
        assert fig in case, fig
    # Estimaciones base: volúmenes del Caso y supuestos del modelo financiero.
    assert 2_400_000 * 1 * 25 // (100 * 100) == 6_000
    assert 6_000 * (56 - 16 + 1) == 246_000
    assert 120 * 30 // 100 == 36
    per_month = 52 / 12
    assert round(per_month * 36) == 156 and round(per_month * 36 * 2) == 312
    lots = 1_150 * 1_100 / 8_400
    assert round(lots, 1) == 150.6 and round(lots * 0.05 * 0.20, 1) == 1.5
    assert round(lots * 0.05 * 0.20 * 41) == 62
    assert 31_000 * 20 * 5 // 100 == 31_000 and round(31_000 / 60) == 517
    assert divmod(1 * 1_000, 60) == (16, 40)
    decisions = 62_000 * 11_600 / 14_200
    assert round(decisions) == 50_648 and round(decisions * 10 * 0.20) == 101_296
    assert (ceil(80 * 24 / 100), ceil(80 * 60 / 100)) == (20, 48)
    annex = (HERE.parent / "13_anexos/contenido.tex").read_text(encoding="utf-8")
    assert all(s in annex for s in ("6.000 unidades", "156 minutos", "312 minutos-persona",
        "150,6 lotes", "1,5 lotes", "31.000 minutos-persona", "16 horas y 40 minutos",
        "101.296 minutos", "50.648 decisiones", "20 de 24"))
    print("Cinco estimaciones base y umbrales de muestra verificados.")


if __name__ == "__main__":
    dates_and_links()
    physical_examples()
