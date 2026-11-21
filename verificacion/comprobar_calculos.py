import math,json,pathlib
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
}
trace=out/"trazabilidad"
trace.mkdir(exist_ok=True)
(trace/"calculos_sd10.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
print("LafroX SD10: 11 controles correctos; Erlang C 90,6%/84,2%; DR135min; reduccion teorica64,3%.")
