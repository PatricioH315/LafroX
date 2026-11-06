"""Verifica que el cuerpo, el anexo y la memoria usen el mismo perfil TPS."""

import math
import re
from pathlib import Path

import calculo


ROOT = Path(__file__).resolve().parents[2]
PLACES = ("Talca", "Concepción", "cross-docking", "nube", "portal")
NUMBER = r"\d+,\d{2}\b"


def check_hourly(text: str, pattern: str, expected: dict[int, list[str]]) -> None:
    rows = re.findall(pattern, text, re.MULTILINE)
    assert len(rows) == 24, f"Se esperaban 24 filas horarias; hay {len(rows)}"
    for hour, row in rows:
        assert re.findall(NUMBER, row) == expected[int(hour)], f"Diferencia en {hour}:00"
    assert {int(hour) for hour, _ in rows} == set(range(24)), "Horas ausentes o duplicadas"


def main() -> None:
    normal = calculo.hourly_profile(1.0, True)
    september = calculo.hourly_profile(
        calculo.ENTREGAS_PEAK_DIA / calculo.ENTREGAS_NORMAL_DIA, True
    )
    for profile in (normal, september):
        for row in profile:
            assert math.isclose(row["total"], sum(row[place] for place in PLACES))

    normal_peak = calculo.peak_row(normal)
    september_peak = calculo.peak_row(september)
    normal_dispatch = calculo.peak_row(normal[5:7])
    september_dispatch = calculo.peak_row(september[5:7])
    peaks = (normal_peak, normal_dispatch, september_dispatch, september_peak)
    assert tuple(row["hora"] for row in peaks) == (12, 5, 5, 12)
    totals = [calculo.fmt(row["total"]) for row in peaks]
    assert totals == ["12,34", "3,76", "6,94", "14,66"]
    rounded_subtotals = sum(round(september_dispatch[place], 2) for place in PLACES)
    assert calculo.fmt(rounded_subtotals) == "6,93"

    expected = {
        h: [calculo.fmt(profile[h][key]) for key in (*PLACES, "total")
            for profile in (normal, september)]
        for h in range(24)
    }
    annex = (ROOT / "04/anexos/fisica/16_anexo_4b_memoria_calculo.tex").read_text(encoding="utf-8")
    check_hourly(annex, r"^\s*(\d{2}):00 &(.+)$", expected)
    report = calculo.OUT.read_text(encoding="utf-8")
    check_hourly(report, r"^\| (\d{2}):00 \|(.+)$", expected)

    body = (ROOT / "04/partes/4.2_fisica/12_k_dimensionamiento.tex").read_text(encoding="utf-8")
    table = body.split(r"{tab:t76}", 1)[1].split(r"\end{tablalafrox}", 1)[0]
    rows = [line for line in table.splitlines() if line.endswith(r"\\")]
    assert len(rows) == 6, "Tabla 14: se esperaban cinco lugares y un máximo agregado"
    assert "Despacho normal" in table and "Despacho en septiembre" in table
    for place, row in zip(PLACES, rows[:-1], strict=True):
        values = (calculo.peak_row(normal, place)[place], normal_dispatch[place],
                  september_dispatch[place], calculo.peak_row(september, place)[place])
        assert re.findall(NUMBER, row) == list(map(calculo.fmt, values)), place
    assert "Máximo agregado coincidente" in rows[-1]
    assert re.findall(NUMBER, rows[-1]) == totals
    test_rates = [calculo.fmt(round(row["total"], 2) * calculo.REQ_PRUEBA_CARGA)
                  for row in (september_peak, september_dispatch)]
    assert test_rates == ["21,99", "10,41"]
    for text in (body, annex, report):
        assert all(f"{rate} TPS" in text for rate in test_rates), "Falta un objetivo de ensayo"
    print("OK: Tabla 14, 24 horas y 288 tasas por representación, máximos y ensayos.")


if __name__ == "__main__":
    main()
