import math,json,pathlib,argparse,calendar
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

# Invertir la cola, en vez de atribuir la capacidad diurna al único puesto nocturno.
hourly_capacity = {}
for staffing in (1, 2, 3, 7, 8):
    left, right = 0.0, staffing * 6.0
    for _ in range(80):
        middle = (left + right) / 2
        if erlang(middle, staffing) >= .8:
            left = middle
        else:
            right = middle
    hourly_capacity[str(staffing)] = left
    assert erlang(left - .000001, staffing) >= .8 > erlang(left + .000001, staffing)
safe_capacity = {c: math.floor(value * 100) / 100 for c, value in hourly_capacity.items()}
assert [safe_capacity[str(c)] for c in (1, 2, 3)] == [1.23, 4.54, 8.55]
assert erlang(demand(2000)[1], 1) < .8

months = []
for contract_month in range(21, 57):
    calendar_index = 2027 * 12 + 1 + contract_month - 1
    year, zero_month = divmod(calendar_index, 12)
    month = zero_month + 1
    day_count = calendar.monthrange(year, month)[1]
    sundays_in_month = sum(date(year, month, d).weekday() == 6 for d in range(1, day_count + 1))
    workdays = day_count - sundays_in_month
    is_peak = month in (9, 12)
    daytime_hours = 52 if is_peak and contract_month >= 25 else 37
    base_hours = workdays * daytime_hours + (workdays * 6 + sundays_in_month * 24 if is_peak else 0)
    row = dict(contract_month=contract_month, year=year, month=month,
               ordinary_days=workdays, sundays=sundays_in_month, base_hours=base_hours,
               base_places=math.ceil(base_hours / 128))
    if is_peak:
        selective = workdays * 58 + sundays_in_month * 48
        extended = selective + workdays * 6
        row.update(selective_hours=selective, selective_places=math.ceil(selective / 128),
                   extended_hours=extended, extended_places=math.ceil(extended / 128),
                   extra_noc_hours=workdays * 2)
    months.append(row)
assert sum(row['base_hours'] for row in months) == 38246
assert [row['contract_month'] for row in months if row['month'] in (9, 12)] == [23, 32, 35, 44, 47, 56]
assert [max(row.get(field, 0) for row in months) for field in ('base_places', 'selective_places', 'extended_places')] == [13, 14, 15]
check_tex_table(annex, 'tab:sd10-alternativas-mesa', [
    ('A. Base: uno nocturno y dominical; dos en relevo NOC', '1.570', '13', '0'),
    ('B. Dos dominicales; uno nocturno; tres en relevo NOC', '1.690', '14', '50'),
    ('C. Dos nocturnos y dominicales; tres en relevo NOC', '1.840', '15', '50'),
])

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
    "exact_hourly_capacity": hourly_capacity,
    "conservative_hourly_capacity": safe_capacity,
    "coverage_calendar_months": months,
    "base_desk_hours_36months": sum(row['base_hours'] for row in months),
    "alternatives_approved": False,
    "proposed_internal_response_budgets": ola_results,
    "staffing_cross_check": {
        "bridge_hours": 9336,
        "dedicated_operation_hours": 86274.20,
        "operation_calendar_vs_e2_difference_hours": 631.12,
        "service_manager_difference_hours": 12,
    },
}
trace=out/"trazabilidad"
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--sd4-audit', type=pathlib.Path)
args = parser.parse_args()
if args.sd4_audit:
    comparison = json.loads(args.sd4_audit.read_text(encoding='utf-8'))
    assert comparison['months'] == months, 'Calendarios SD4/SD10 distintos'
    assert comparison['conservative_hourly_capacity'] == safe_capacity, 'Cotas SD4/SD10 distintas'
    for staffing, value in hourly_capacity.items():
        assert abs(value - comparison['exact_hourly_capacity'][staffing]) < 1e-10
    result['cross_document_numeric_check'] = 'passed'
trace.mkdir(exist_ok=True)
(trace/"calculos_sd10.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
print("LafroX SD10: controles y tablas de demanda, peak, SLA y acuerdos internos verificados.")
