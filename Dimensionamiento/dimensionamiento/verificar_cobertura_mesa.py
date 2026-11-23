"""Reproduce cotas de espera y HH por calendario; no acredita turnos reales."""
import argparse
import calendar
from datetime import date
import json
import math
from pathlib import Path


def service_level(arrivals, agents):
    load = arrivals / 6
    if arrivals < 0 or agents <= load:
        return 0.0
    weights = [load ** k / math.factorial(k) for k in range(agents)]
    tail = load ** agents / math.factorial(agents) * agents / (agents - load)
    return 1 - tail / (sum(weights) + tail) * math.exp(-(6 * agents - arrivals) / 180)


def capacity(agents):
    low, high = 0.0, 6.0 * agents
    for _ in range(80):
        middle = (low + high) / 2
        if service_level(middle, agents) >= .8:
            low = middle
        else:
            high = middle
    return low


def audit():
    thresholds = {str(c): capacity(c) for c in (1, 2, 3, 7, 8)}
    for c in (1, 2, 3, 7, 8):
        limit = thresholds[str(c)]
        assert service_level(limit - .000001, c) >= .8
        assert service_level(limit + .000001, c) < .8
    safe = {c: math.floor(value * 100) / 100 for c, value in thresholds.items()}
    months = []
    for contract_month in range(21, 57):
        offset = 1 + contract_month - 1  # M1 = febrero de 2027.
        year, month = 2027 + offset // 12, offset % 12 + 1
        days = calendar.monthrange(year, month)[1]
        sundays = sum(date(year, month, d).weekday() == 6 for d in range(1, days + 1))
        ordinary_days = days - sundays
        peak = month in (9, 12)
        daytime = 52 if peak and contract_month >= 25 else 37
        base = ordinary_days * daytime
        if peak:
            base += ordinary_days * 6 + sundays * 24
        row = dict(contract_month=contract_month, year=year, month=month,
                   ordinary_days=ordinary_days, sundays=sundays, base_hours=base,
                   base_places=math.ceil(base / 128))
        if peak:
            # B/C necesitan tres agentes de valle también si se adelantan a M23.
            selective = ordinary_days * (52 + 6) + sundays * 48
            extended = selective + ordinary_days * 6
            row.update(selective_hours=selective, selective_places=math.ceil(selective / 128),
                       extended_hours=extended, extended_places=math.ceil(extended / 128),
                       extra_noc_hours=ordinary_days * 2)
        months.append(row)
    september = next(r for r in months if (r['year'], r['month']) == (2029, 9))
    assert tuple(september[k] for k in ('base_hours', 'selective_hours', 'extended_hours')) == (1570, 1690, 1840)
    assert tuple(september[k] for k in ('base_places', 'selective_places', 'extended_places')) == (13, 14, 15)
    assert sum(r['base_hours'] for r in months) == 38246  # T-15, 10.1.2.
    assert max(r['base_places'] for r in months) == 13
    assert max(r.get('selective_places', 0) for r in months) == 14
    assert max(r.get('extended_places', 0) for r in months) == 15
    valley = 2391 * .75 / (31000 / 1400) / 17
    assert service_level(valley, 2) < .8 <= service_level(valley, 3)
    # Un domingo al 40 % del valle no cabe en un único agente.
    assert service_level(valley * .4, 1) < .8 <= service_level(valley * .4, 2)
    # Una tasa nocturna igual al valle exige dos agentes, incluso en el escenario base.
    assert service_level(2000 * .75 / (31000 / 1400) / 17, 1) < .8
    return dict(proyecto='LafroX', nature='Calculo de diseno; sin registros ni cuadrante nominal acreditados',
                effective_monthly_hours=128, handling_minutes=10, target_fraction=.8,
                answer_seconds=20, exact_hourly_capacity=thresholds,
                conservative_hourly_capacity=safe, months=months,
                critical_error_budgets_continuous_minutes={str(d): d * 24 * 60 * .001 for d in (28, 29, 30, 31)},
                alternatives_approved=False, other_documents_modified=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = audit()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('LafroX: cotas de Erlang C, 36 meses y alternativas de 13/14/15 plazas verificados.')
