"""Verificación documental de SD13; no mide beneficios ni sustituye revisión humana."""
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
SD7 = "68669befd04babce61e9fb4d8f5e6b29d28f46aa"
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
    assert all((m.get("start"), m.get("duration")) == ("2028-04-28", "0")
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
            "20-03-2028", "28-12-2027", "28-04-2028")
    assert [(h, milestones[h][1], rows[milestones[h][-1]][5])
            for h in ("H4", "H5", "H10")] == [
                ("H4", "20-10-2027", "22-10-2027"),
                ("H5", "24-11-2027", "01-12-2027"),
                ("H10", "27-06-2028", "28-06-2028"),
            ]
    print("17 paquetes, 7 enlaces y 3 marcadores sin duración; mes 15 y fechas H4/H5/H10 cotejados.")


def physical_examples():
    case = read(CASE, "Bases/Caso_02_Logistica.md")
    assert re.search(r"Unidades despachadas al mes.*2,4 millones", case)
    assert "2.600 visitas diarias" in case
    assert re.search(r"1\.400 a ≈2\.600 entregas", case)
    # Volúmenes del Caso; las tasas y los tiempos son supuestos, no observaciones.
    avoided = 100 * 25 // 100
    assert (avoided, avoided * (2_400_000 // 100) // 10_000) == (25, 60)
    minutes = 120 * 30 // 100
    assert (minutes, (minutes * 10) // 60) == (36, 6)
    assert (50 * (100 - 20) // 100, 50 - 40) == (40, 10)
    time_delta = 20 - 19
    assert divmod(time_delta * 1_000, 60) == (16, 40)
    assert (time_delta * 1_400 // 10, time_delta * 2_600 // 10) == (140, 260)
    assert (10 - 8) * (2_600 // 100) == 52
    assert (ceil(80 * 24 / 100), ceil(80 * 60 / 100)) == (20, 48)
    annex = (HERE.parent / "13_anexos/contenido.tex").read_text(encoding="utf-8")
    assert all(s in annex for s in ("25 unidades", "60 unidades", "36 minutos",
        "10 lotes", "16 horas y 40 minutos-persona", "140 minutos-persona",
        "260 en peak", "52 minutos", "20 de 24"))
    print("Cinco escenarios, extrapolaciones aritméticas y umbrales de muestra verificados.")


if __name__ == "__main__":
    dates_and_links()
    physical_examples()
