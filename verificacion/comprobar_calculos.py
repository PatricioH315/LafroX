import math,json,pathlib
from decimal import Decimal
from datetime import date
out=pathlib.Path(__file__).resolve().parents[1]
def erlang(lam,c,t=20):
    mu=6.0
    a=lam/mu
    if c<=a:
        return 0.0
    term=1.0
    subtotal=term
    for k in range(1,c):
        term*=a/k
        subtotal+=term
    tail=term*a/c*c/(c-a)
    wait=tail/(subtotal+tail)
    return 1-wait*math.exp(-(c*mu-lam)*t/3600)
MONTHLY_EQUIVALENT_DAYS = 31_000 / 1_400

def demand(n):
    return n*.25/MONTHLY_EQUIVALENT_DAYS,n*.75/MONTHLY_EQUIVALENT_DAYS/17
calc=[]
for n in (2000,2000*350/310,2283,2391,6000):
    peak,valley=demand(n)
    def agents(lam):
        return next(c for c in range(1,60) if erlang(lam,c)>=.8)
    calc.append(dict(contacts=n,peak=peak,valley=valley,sl7=erlang(peak,7),
                     sl2=erlang(valley,2),sl3=erlang(valley,3),
                     need_peak=agents(peak),need_valley=agents(valley)))
assert round(calc[0]["sl7"]*100,1)==90.6
assert round(calc[0]["sl2"]*100,1)==84.2
assert calc[2]["sl2"] >= .8 > erlang(demand(2284)[1], 2)
assert calc[3]["sl2"] < .8 <= calc[3]["sl3"]
assert calc[3]["sl7"] >= .8 > erlang(demand(2392)[0], 7)
assert (calc[-1]["need_peak"],calc[-1]["need_valley"])==(15,4)
dr=[5,30,20,30,15,15,15,5]
assert sum(dr)==135
assert round((1-60/168)*100,1)==64.3
assert math.ceil(26*37/128)==8
assert math.ceil((25*(52+6)+5*24)/128)==13
assert round(2304/109791.32*100,4)==2.0985
# Caso de 24 h: dos interrupciones solapadas cubren [100, 200).
# El mantenimiento aprobado cubre [120, 180), por lo que exceden 40 min.
calendar_minutes = 24 * 60
approved_minutes = 180 - 120
outage_minutes = 200 - 100 - approved_minutes
adjusted_minutes = calendar_minutes - approved_minutes
assert (outage_minutes, adjusted_minutes) == (40, 1380)
assert 100 * (1 - outage_minutes / adjusted_minutes) < 100 * (1 - outage_minutes / calendar_minutes)
assert sum((1851, 1786, 1810, 1851, 2038)) == 9336
assert sum(map(Decimal, ("38246", "21748.20", "26280"))) == Decimal("86274.20")
assert Decimal("109791.32") - Decimal("109160.20") == Decimal("631.12")
assert 36 * 128 - 4596 == 12

def check_tex_table(path, label, expected):
    """Compare the table cells against calculated quantities in display order."""
    content = (out / path).read_text(encoding="utf-8")
    table = content.split("{" + label + "}", 1)[1].split(r"\end{tablalafrox}", 1)[0]
    actual = [
        tuple(value.strip() for value in line.strip().removesuffix(r"\\").split("&"))
        for line in table.splitlines()[1:]
        if line.strip().endswith(r"\\")
    ]
    assert actual == expected, (label, actual, expected)


def spanish(value, digits=0):
    return f"{value:,.{digits}f}".translate(str.maketrans(".,", ",."))


def percent(fraction):
    return spanish(fraction * 100, 2) + r"\,\%"


external_profiles = [
    ("Clientes activos", 14200, Decimal("0.01")),
    ("Proveedores", 180, Decimal("0.25")),
    ("Representantes adicionales", 20, Decimal("0.50")),
]
external_contacts = sum(count * rate for _, count, rate in external_profiles)
profile_rows = [
    (name, spanish(count), spanish(rate, 2), spanish(count * rate))
    for name, count, rate in external_profiles
]
profile_rows.append((r"\textbf{Total adicional}", "", "", fr"\textbf{{{spanish(external_contacts)}}}"))
annex = "10_anexos/contenido.tex"
check_tex_table(annex, "tab:sd10-perfiles-demanda", profile_rows)

expanded = []
for multiplier in (1, 2):
    contacts = 2000 + int(external_contacts * multiplier)
    busy, valley = demand(contacts)
    peak_agents = next(c for c in range(1, 20) if erlang(busy, c) >= .8)
    valley_agents = next(c for c in range(1, 20) if erlang(valley, c) >= .8)
    expanded.append({
        "contacts": contacts,
        "agents_busy": peak_agents,
        "agents_valley": valley_agents,
        "sl_busy": erlang(busy, peak_agents),
        "sl_valley": erlang(valley, valley_agents),
    })
for scenario in expanded:
    source = (out / annex).read_text(encoding="utf-8")
    assert spanish(scenario["contacts"]) in source
    assert percent(scenario["sl_busy"]) in source
    assert percent(scenario["sl_valley"]) in source

peak_profiles = [
    ("Nocturna lunes a sábado", .25, 1, 1),
    ("Domingo", .40, 1, 2),
    ("Relevo NOC lunes a sábado", 1.00, 2, 3),
]
peak_table, peak_results = [], []
for name, fraction, base_staff, proposed_staff in peak_profiles:
    arrivals = demand(2391)[1] * fraction
    base_sl = erlang(arrivals, base_staff)
    proposed_sl = erlang(arrivals, proposed_staff)
    assert proposed_sl >= .8
    assert proposed_staff == base_staff or base_sl < .8
    peak_table.append((
        name, spanish(arrivals, 2),
        f"{base_staff} / {percent(base_sl)}",
        f"{proposed_staff} / {percent(proposed_sl)}",
    ))
    peak_results.append({
        "shift": name, "valley_fraction": fraction, "arrivals_per_hour": arrivals,
        "base_agents": base_staff, "proposed_agents": proposed_staff,
        "base_service_level": base_sl, "proposed_service_level": proposed_sl,
    })
check_tex_table(annex, "tab:sd10-peak-franjas", peak_table)

sundays = sum(date(2029, 9, day).weekday() == 6 for day in range(1, 31))
regular_days = 30 - sundays
peak_desk_reinforced = regular_days * (52 + 6) + sundays * 48
peak_noc_added = regular_days * 2
peak_desk_places = math.ceil(peak_desk_reinforced / 128)
assert (peak_desk_reinforced, peak_noc_added, peak_desk_places) == (1690, 50, 14)

ola_profiles = [
    ("Crítica", "min", 10, (20, 10, 150, 30), 15, 240),
    ("Alta", "min", 30, (45, 15, 300, 60), 60, 480),
    ("Media", "h", 2, (1, 1, 16, 4), 4, 24),
    ("Baja", "h", 4, (2, 2, 32, 8), 8, 48),
]
ola_table, ola_results = [], []
for label, unit, response, stages, maximum_response, maximum_resolution in ola_profiles:
    total = sum(stages)
    reserve = maximum_resolution - total
    assert response < maximum_response and reserve > 0
    sequence = " + ".join(map(str, stages))
    ola_table.append((label, f"{response} {unit}", f"{sequence} {unit}", f"{total} {unit}", f"{reserve} {unit}"))
    ola_results.append({"severity": label, "unit": unit, "response": response, "stages": stages, "resolution": total, "margin": reserve})
check_tex_table("10_anexos/partes/10_c_guias.tex", "tab:sd10-plazos-internos", ola_table)

result={
    "model":"Reproduccion de Erlang C de SD4 Anexo 4-W.7",
    "monthly_equivalent_days":MONTHLY_EQUIVALENT_DAYS,
    "average_handling_minutes":10,
    "busy_fraction":.25,
    "service_seconds":20,
    "scenarios":calc,
    "dr_sequence_minutes":dr,
    "dr_total_minutes":sum(dr),
    "dr_margin_minutes":240-sum(dr),
    "nonproduction_weekly_hours":60,
    "continuous_weekly_hours":168,
    "theoretical_reduction_percent":(1-60/168)*100,
    "ordinary_desk_hours_example":26*37,
    "peak_desk_hours_september_2029":25*(52+6)+5*24,
    "critical_downtime_budget_30days_minutes":30*24*60*.001,
    "availability_four_hours_outage_30days_percent":100*(1-4/(30*24)),
    "technical_debt_effort_percent":2304/109791.32*100,
    "approved_maintenance_example": {
        "calendar_minutes": calendar_minutes,
        "approved_minutes": approved_minutes,
        "unavailable_minutes": outage_minutes,
        "adjusted_denominator": adjusted_minutes,
        "availability_adjusted_percent": 100 * (1 - outage_minutes / adjusted_minutes),
        "availability_unadjusted_percent": 100 * (1 - outage_minutes / calendar_minutes),
    },
    "additional_contacts_sensitivity": expanded,
    "peak_shift_sensitivity": peak_results,
    "peak_desk_reinforced_september_2029": peak_desk_reinforced,
    "peak_desk_reinforced_places": peak_desk_places,
    "peak_noc_added_hours": peak_noc_added,
    "proposed_internal_response_budgets": ola_results,
    "staffing_cross_check": {
        "bridge_hours": 9336,
        "dedicated_operation_hours": 86274.20,
        "operation_calendar_vs_e2_difference_hours": 631.12,
        "service_manager_difference_hours": 12,
    },
}
trace=out/"trazabilidad"
trace.mkdir(exist_ok=True)
(trace/"calculos_sd10.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
print("LafroX SD10: controles y tablas de demanda, peak, SLA y acuerdos internos verificados.")
