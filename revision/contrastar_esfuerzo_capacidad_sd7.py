"""Contraste reproducible de esfuerzo y capacidad; no cambia las fuentes."""
from pathlib import Path
from collections import defaultdict
from decimal import Decimal as D
from fractions import Fraction as F
import contextlib, io, json, os, re, runpy, csv, calendar
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
T = ROOT / 'formulario-t15'
OUT = Path(os.environ['TEMP']) / 'lafrox-sd7-esfuerzo-capacidad'
OUT.mkdir(parents=True, exist_ok=True)
def rows(path):
    return [line.strip().removesuffix(r'\\').strip().split(' & ')
            for line in path.read_text(encoding='utf8').splitlines()
            if re.match(r'^  \d+\.',line)]
def es(s):
    return F(s.replace('.','').replace(',','.'))
base = {a[0]: a for a in rows(T/'tablas/tab_T15_2.tex')}
cont = {a[0]: a for a in rows(T/'tablas/tab_T15_10.tex')}
dated = {a[0]: a for a in rows(T/'tablas/tab_T15_paquetes.tex')}
assert len(base)==227 and len(cont)==59 and len(dated)==168
assert set(cont).isdisjoint(dated) and set(cont)|set(dated)==set(base)
K = {a['EDT']: a for a in csv.DictReader((ROOT/'revision/frente-b/K4_PAQUETES.csv').open(encoding='utf-8-sig'))}
src=(T/'contenido.tex').read_text(encoding='utf8')
mod=src.split('{tab:T15-tamano-escenario}',1)[1].split(r'\end{tablalafrox}',1)[0]
m={a[0]: tuple(map(int,a[3:6])) for l in mod.splitlines() if re.match(r'^  3\.[45]\.',l) for a in [l.strip().split(' & ')]}
assert len(m)==15
risk_modules={a[0]:F(a[2]) for l in mod.splitlines() if re.match(r'^  3\.[45]\.',l) for a in [l.strip().split(' & ')]}

rules={
 'G': (8,8,'revisión documental'),
 'E': (16,24,'ajuste de diseño y revisión'),
 'I': (16,32,'repetición de integración o conciliación'),
 'V': (8,24,'repetición de prueba y registro'),
 'T': (8,24,'repetición de instalación o instrucción'),
 'D': (16,32,'regresión y ajuste de integración')
}
triggers=(
    (r'cliente|proveedor|cadena|tercero|sindicato|transportista','coordinación externa',8),
    (r'erp|interfaces?|edi|pasarela|migraci[oó]n|datos|conciliaci[oó]n','repetición de datos o interfaz',8),
    (r'sin conexi[oó]n|corte|resilien|recuperaci[oó]n|seguridad ofensiva|temperatura|congel','repetición en contingencia',8),
)
eff=[]
for k,a in base.items():
    b=F(a[7])
    if k in m:
        o,mid,p=map(F,m[k]); why='Estimación por requisitos T-12 y repruebas de módulo'
    elif k in cont:
        assert es(cont[k][4])==b
        o=mid=p=b; why='Esfuerzo programado por cobertura, turno u ocurrencia'
    else:
        assert es(dated[k][3])==b
        saved,rework,why=rules[a[1]]
        desc=' '.join(K[k][x] for x in ['nombre','entregable','criterio']).lower()
        for pattern,reason,block in triggers:
            if re.search(pattern,desc):rework+=block;why+='; '+reason
        o,mid,p=b-saved,b,b+rework
    assert 0<=o<=mid<=p
    eff.append((k,a[1],b,o,mid,p,(o+4*mid+p)/6,why))
assert len(eff)==227 and sum(x[2] for x in eff)==220023-12536
def outnum(x): return f'{float(x):.2f}'
with (OUT/'pert_227.csv').open('w',encoding='utf-8-sig',newline='') as fp:
    w=csv.writer(fp);w.writerow(('EDT','Clase','HH base','O','M','P','E','Motivo'))
    for k,c,b,o,mid,p,e,why in eff:w.writerow((k,c,*map(outnum,(b,o,mid,p,e)),why))

with contextlib.redirect_stdout(io.StringIO()):
    x=runpy.run_path(str(ROOT/'revision/recalcular_cpm_texto_sd7.py'))
def month(d):return (d.year-2027)*12+d.month-1
def ym(m):return 2027+m//12, m%12+1
def group(f):return 'ARQ_DAT' if f in ('ARQ','DAT') else f
def hours_n1(m):
    y,k=ym(m);d=calendar.monthrange(y,k)[1]
    sun=sum(date(y,k,i).weekday()==6 for i in range(1,d+1))
    return (d-sun)*(41 if m<25 else 58)+((d-sun)*6+sun*24 if k in (9,12) else 0)

load=defaultdict(F)
for k,p in x['P'].items():
    a=x['EA']['S:'+k];b=x['EA']['F:'+k]
    assert a<b
    for i in range(a,b):
        load['entregable',group(p['role']),month(x['CAL'][i])]+=F(str(p['hh']))/(b-a)
# Coberturas segregadas: sus horas-posición no compiten con las familias de planta.
# Donde no hay distribución mensual aprobada, se contrasta el promedio de la ventana.
special={
 '4.2.1':[2464,2464,2464], '4.2.2':[2464,1312,544,544,544],
 '4.3.1':[2464,2464], '4.3.2':[F(2464*5,24),F(2464*19,24)]
}
coverage={'8.1.1':'NOC','8.1.2':'N1','8.1.5':'SOC'}
for k,a in cont.items():
    lo,hi=map(int,a[3].split('–'))
    h=es(a[4]); role=coverage.get(k,group(a[2]))
    if k in special: weights=list(map(F,special[k]))
    elif k in ('8.1.1','8.1.5'):weights=[F(24*calendar.monthrange(*ym(j))[1]) for j in range(lo,hi+1)]
    elif k=='8.1.2':weights=[F(hours_n1(j)) for j in range(lo,hi+1)]
    else:weights=[F(1) for j in range(lo,hi+1)]
    if k in coverage:assert sum(weights)==h,(k,sum(weights),h)
    for j,w in enumerate(weights,lo):load['continuo',role,j]+=h*w/sum(weights)
for j in range(16,21):
    load['adicional','NOC',j]+=24*calendar.monthrange(*ym(j))[1]
    load['adicional','N1',j]+=hours_n1(j)
for j in range(13,21):
    load['adicional','DES',j]+=256;load['adicional','CAL',j]+=128
for j in range(13,21):load['adicional','SRE',j]+=16
assert sum(load.values())==220023
roles=sorted({r for _,r,_ in load})
limits=x['caps_all'];summary={}
with (OUT/'capacidad_mensual.csv').open('w',encoding='utf-8-sig',newline='') as fp:
    w=csv.writer(fp);w.writerow(('Mes','Familia','Entregables HH','Continuas HH','Adicionales HH','Total HH','Equiv. a 128 HH','Umbral escenario HH'))
    for r in roles:
        monthly=[]
        for j in range(1,57):
            parts=[load[t,r,j] for t in ('entregable','continuo','adicional')]; h=sum(parts);monthly.append((h,j))
            w.writerow((j,r,*map(outnum,parts),outnum(h),outnum(h/128),limits[r]*128 if r in limits else ''))
        peak,j=max(monthly)
        summary[r]={'hh_pico':outnum(peak),'mes':j,'equivalentes':outnum(peak/128),'umbral':limits.get(r),
                    'meses_exceso':[j for h,j in monthly if r in limits and h>limits[r]*128]}
result={'conteos':{'modulos':15,'otros_entregables':153,'continuos':59},'esperado_paquetes':outnum(sum(x[6] for x in eff)),
        'esperado_mas_componentes_fijos':outnum(sum(x[6] for x in eff)+12536),
        'hh_capacidad':outnum(sum(load.values())),'capacidad':summary}
# Sensibilidad del esfuerzo esperado, sin cambiar la base ni inferir probabilidad.
total=sum(a[6] for a in eff)+12536
var_mod=sum(F(o+4*mid+pes,6)-240-risk_modules[k]/6 for k,(o,mid,pes) in m.items())
rework=sum((a[5]-a[4])/6 for a in eff if a[0] in dated and a[0] not in m)+sum(risk_modules.values())/6
result['sensibilidad_hh']={'modulos_variable_menos_20':outnum(total-var_mod/5),
    'central':outnum(total),'modulos_variable_mas_20':outnum(total+var_mod/5),
    'doble_reproceso':outnum(total+rework)}
# Prueba de capacidad diaria de las cuatro pruebas críticas; cifras en décimas.
cal=[d for d in x['CAL'] if date(2027,10,25)<=d<=date(2027,11,19)]
assert len(cal)==19 and sum(d<=date(2027,11,11) for d in cal)==13
qa=[]
for j,d in enumerate(cal):
    critical=j<13
    totals=[160,160,248 if j==0 else 246,248 if j==0 else 246] if critical else [187 if j<18 else 185]*2+[0,0]
    leads=[25 if j<18 else 30]*2+([37 if j<12 else 36]*2 if critical else [0,0])
    assert all(h<=n*64 for h,n in zip(totals,(3,3,4,4)))
    assert sum(leads)<=128 and sum(totals)-sum(leads)<=(11 if critical else 8)*64
    assert sum(totals)<=(13 if critical else 10)*64
    qa.append((d.isoformat(),*totals,sum(leads),sum(totals)-sum(leads),sum(totals)))
assert [sum(a[i] for a in qa) for i in range(1,8)]==[3200]*4+[1920,10880,12800]
with (OUT/'calidad_19_dias.csv').open('w',encoding='utf-8-sig',newline='') as fp:
    w=csv.writer(fp);w.writerow(('Fecha','3.8.2 HH','3.8.3 HH','3.8.4 HH','3.8.5 HH','Función 16 HH','Función 19 HH','Total HH'))
    for d,*h in qa:w.writerow((d,*[outnum(F(i,10)) for i in h]))
result['calidad_diaria']={'total_hh':'1280.00','dias':19,'dias_criticos':13,
    'hh_tramo_critico':outnum(F(sum(a[-1] for a in qa[:13]),10)),
    'maximo_diario':outnum(F(max(a[-1] for a in qa),10))}
(OUT/'resumen.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(result,ensure_ascii=False))
