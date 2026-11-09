"""Escenarios CPM por duración y disponibilidad de DES/CAL (sin modificar fuentes).

Unidades: HH y capacidades de T-15, con el calendario nominal del escenario base.
Las coberturas y hitos contractuales se modelan como condiciones de calendario,
no como trabajo productivo ficticio. No se certifica personal nominal disponible.
"""
from pathlib import Path
from datetime import date, timedelta
from decimal import Decimal
from collections import defaultdict, deque
from bisect import bisect_left
from heapq import heappop, heappush
import calendar, json, math, re, hashlib

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__import__('os').environ['TEMP']) / 'lafrox-sd7-cpm-texto'

def rows(relative):
    text = (ROOT / relative).read_text(encoding='utf-8')
    result = []
    for line in text.splitlines():
        if re.match(r'^\s*\d+(?:\.\d+)*\s*&', line):
            result.append([c.strip() for c in line.strip().removesuffix('\\\\').split(' & ')])
    return result

def easter(y):
    a=y%19; b=y//100; c=y%100; d=b//4; e=b%4; f=(b+8)//25
    g=(b-f+1)//3; h=(19*a+b-d-g+15)%30; i=c//4; k=c%4
    l=(32+2*e+2*i-h-k)%7; m=(a+11*h+22*l)//451
    n=h+l-7*m+114
    return date(y,n//31,n%31+1)

def holidays(y):
    result={date(y,m,d) for m,d in [(1,1),(5,1),(5,21),(7,16),(8,15),(9,18),(9,19),(11,1),(12,8),(12,25)]}
    result |= {easter(y)-timedelta(days=2), easter(y)-timedelta(days=1)}
    # Ley 19.668: martes a jueves al lunes anterior; viernes al siguiente.
    for m,d in [(6,29),(10,12)]:
        x=date(y,m,d)
        if x.weekday() in (1,2,3): x-=timedelta(days=x.weekday())
        elif x.weekday()==4: x+=timedelta(days=3)
        result.add(x)
    # Ley 20.299: martes al viernes anterior; miércoles al viernes siguiente.
    x=date(y,10,31)
    if x.weekday()==1:x-=timedelta(days=4)
    elif x.weekday()==2:x+=timedelta(days=2)
    result.add(x)
    if date(y,9,18).weekday()==1:result.add(date(y,9,17))
    if date(y,9,18).weekday()==2:result.add(date(y,9,20))
    if date(y,9,18).weekday()==5:result.add(date(y,9,17))
    if date(y,1,1).weekday()==6:result.add(date(y,1,2))
    solstice={2027:21,2028:20,2029:20,2030:21,2031:21,2032:20}
    result.add(date(y,6,solstice[y]))
    return result

HOLIDAYS=set().union(*(holidays(y) for y in range(2027,2033)))
all_days=[date(2027,1,1)+timedelta(days=n) for n in range((date(2032,12,31)-date(2027,1,1)).days+1)]
CAL=[d for d in all_days if d.weekday()<5 and d not in HOLIDAYS]
def ix(d):return bisect_left(CAL,d)
def parse(s):return date(*map(int,s.split('-')[::-1]))
def month(m,last=False):
    y=2027+(m+0)//12; mm=(m+0)%12+1
    d=date(y,mm,calendar.monthrange(y,mm)[1] if last else 1)
    return ix(d+timedelta(days=1))-1 if last else ix(d)
def display(n,finish=False):return CAL[n-1 if finish else n].isoformat()
def clean(s):return s.replace(r'\allowbreak{}','')

EFF={r[0]:r for r in rows('formulario-t15/tablas/tab_T15_2.tex')}
P={}
for r in rows('formulario-t15/tablas/tab_T15_paquetes.tex'):
    code,role,people,hh,start,end,preds=r
    peak=float(people.split('/')[-1].strip().replace(',','.'))
    a,b=parse(start),parse(end)
    duration=math.ceil(float(hh)/(6.4*peak))
    if EFF[code][1]=='D' and code.startswith(('3.4.','3.5.')):
        duration=3*math.ceil(80/(6.4*peak))+math.ceil((float(hh)-240)/(6.4*peak))
    P[code]={'role':role,'hh':float(hh),'peak':peak,'release':month(int(EFF[code][3].split('–')[0])),'duration':duration,
             'published_start':a.isoformat(),'published_finish':b.isoformat(),
             'preds':clean(preds),'class':EFF[code][1]}
assert len(P)==168 and len(EFF)==227

base={}; adj=defaultdict(list); rev=defaultdict(list); indeg=defaultdict(int)
def node(n,release=0):base[n]=max(base.get(n,0),release);indeg[n]+=0
def edge(a,b,w=0,why=''):
    node(a);node(b)
    if (b,w,why) not in adj[a]:
        adj[a].append((b,w,why));rev[b].append((a,w,why));indeg[b]+=1
def leaves(code):
    if code in P:return [code]
    return sorted([c for c in P if c.startswith(code+'.')],key=lambda x:tuple(map(int,x.split('.'))))

for c,p in P.items():
    node('S:'+c,p['release']);node('F:'+c)
    edge('S:'+c,'F:'+c,p['duration'],'duración por capacidad')
    if p['class']=='D' and c.startswith(('3.4.','3.5.')):
        contracts=2*math.ceil(80/(6.4*p['peak']))
        integration=math.ceil(80/(6.4*p['peak']))
        # La ventana S->F contiene también margen y esperas. Atribuir todo ese
        # tiempo a construcción propaga de nuevo una espera por interfaz y
        # desplaza artificialmente 3.4.10, H4 y el piloto. Las puertas internas
        # usan el mínimo de trabajo efectivo; S->F conserva la ventana completa.
        construction=math.ceil((p['hh']-240)/(6.4*p['peak']))
        assert contracts + construction + integration <= p['duration']
        node('C:'+c);node('I:'+c)
        edge('S:'+c,'C:'+c,contracts,'trabajo:'+c)
        edge('C:'+c,'I:'+c,construction,'trabajo:'+c)
        edge('I:'+c,'F:'+c,integration,'trabajo:'+c)

# Paquetes continuos con entregable de cierre: conservan la duración completa
# de la marcha blanca y propagan cualquier inicio tardío a la aceptación.
for c in ['4.2.1','4.3.1']:
    mm=list(map(int,EFF[c][3].split('–')))
    start=month(mm[0]);finish=month(mm[-1],True)+1
    node('S:'+c,start);node('F:'+c)
    edge('S:'+c,'F:'+c,finish-start,'marcha blanca contractual, calendario fijo')

def point(code,which='F'):
    if code in P:return which+':'+code
    if code in EFF and not leaves(code):
        months=list(map(int,EFF[code][3].split('–')))
        n=which+':'+code
        node(n, month(months[0]) if which=='S' else month(months[-1],True)+1)
        return n
    raise ValueError(('Punto no resuelto',code,which))

def expand(text):
    result=[]
    text=clean(text)
    for token in re.findall(r'\d+(?:\.\d+)+(?:[––-]\d+(?:\.\d+)+)?',text):
        if '–' in token:
            lo,hi=token.split('–');a=lo.split('.');b=hi.split('.')
            assert a[:-1]==b[:-1],token
            codes=['.'.join(a[:-1]+[str(n)]) for n in range(int(a[-1]),int(b[-1])+1)]
        else:codes=[token]
        for c in codes:
            result.extend(leaves(c) or [c])
    return list(dict.fromkeys(result))

for c,p in P.items():
    text=p['preds'].split(';')[0]
    if text.startswith(('—','Especificación')):continue
    for chunk in re.split(r',\s*(?![^()]*\))',text):
        preds=expand(chunk)
        for pred in preds:
            if pred==c:continue
            if c=='2.1.1' and pred=='1.2.1':
                edge(point(pred),'F:'+c,0,'D-01: borrador/acta antes del cierre');continue
            if c=='3.7.5':
                tail=math.ceil(80/(6.4*p['peak']))
                edge(point(pred),'F:'+c,tail,'D-24: corte final A06');continue
            if any(x in chunk for x in ('protocolo inicial','contrato de evidencia','circuito mínimo','parámetros aprobados','prototipo inicial','diseño validado')):
                edge(point(pred,'S'),'S:'+c,0,'preparación concurrente');edge(point(pred),'F:'+c,0,'entregable para cierre');continue
            if '(QA)' in chunk:
                edge(point(pred),'F:'+c,0,'D-14: entrega en QA');continue
            if re.search(r'\bCC\b',chunk):
                edge(point(pred,'S'),'S:'+c,0,'CC');continue
            if '(interfaz)' in chunk:
                # Contratos A02 y entrega A12 se mantienen como puertas internas.
                # El último incremento del sucesor debe integrar la entrega precedente.
                tail=math.ceil(80/(6.4*p['peak']))
                edge(point(pred),'F:'+c,tail,'interfaz: integración tras entrega')
                edge('C:'+pred,'C:'+c,0,'interfaz: contratos A02 antes de construir')
                edge(point(pred),'I:'+c,0,'interfaz: entrega precedente antes de integrar');continue
            edge(point(pred),'S:'+c,0,'FC publicada')

# Cuatro actas parciales; no se bloquea el piloto con la recepción de los 28 kits.
node('KITS4',ix(date(2027,9,30))+1)
edge('S:6.5.4','KITS4',0,'recepción parcial')
edge('KITS4','S:4.1.4',0,'D-37')
# Duraciones mínimas de calendario, sin atribuirlas a HH de trabajo continuo.
node('PILOTO_FIN_CAL',ix(date(2027,12,17))+1)
edge('PILOTO_FIN_CAL','F:4.1.4',0,'seis semanas mínimas del piloto')

M={'H1':(2,['1.2.1','1.2.4']), 'H2':(4,['2.4.1']),
   'H3':(6,['3.1.1','3.1.2','3.1.3','3.1.5','6.6.3']),
   'H4':(10,['3.8.1']), 'H5':(12,['3.8.7']),
   'H8':(14,['1.2.5','2.4.2']), 'H7':(16,['4.2.3']),
   'H9':(17,['3.9.1']), 'H10':(18,['3.9.6']), 'H12':(21,['4.3.3','4.3.4'])}
M['H6']=(13,['4.2.1'])
M['H11']=(19,['4.3.1'])
for h,(m,codes) in M.items():
    node('ENT:'+h)
    for c in codes:edge(point(c,'S' if h in ['H6','H11'] else 'F'),'ENT:'+h,0,'entrega del hito')
    node('ACT:'+h,month(m)+(0 if h in ['H6','H11'] else 1))
    edge('ENT:'+h,'ACT:'+h,0 if h in ['H6','H11'] else 10,'revisión CLIENTE Art.18.3')

# Las aprobaciones formales que bloquean construcción o piloto son eventos separados.
for c in leaves('3.4'):edge('ACT:H2','S:'+c,0,'D-04: arquitectura aprobada')
edge('ACT:H1','F:2.1.1',0,'D-01: aprobación de alcance antes del cierre')
for c in leaves('3.5'):edge('ACT:H8','S:'+c,0,'D-29: diseño aprobado')
edge('ACT:H4','S:4.1.4',0,'D-37: piloto con H4 aprobado')
edge('ACT:H12','S:9.1.2',0,'D-34: cierre formal posterior al acta H12')
for c in ['3.7.5','4.1.1','4.1.2']:
    edge(point(c),'S:4.2.1',0,'D-25: preparación antes de marcha blanca')
edge('ACT:H5','S:4.2.1',0,'D-25: certificación E1 aprobada')
for c in ['3.6.5','4.1.3']:
    edge(point(c),'S:4.3.1',0,'D-32: preparación antes de marcha blanca')
edge('ACT:H10','S:4.3.1',0,'D-32: certificación E2 aprobada')
# Se usa el mes contractual de cada marcha blanca como fecha mínima de evidencia.
for e,m,c,accept in [(1,15,'4.2.1','4.2.3'),(2,20,'4.3.1','4.3.3')]:
    ent=f'CIERRE-ENT:{e}'; act=f'CIERRE-ACTA:{e}'; prod=f'PROD:{e}'
    node(ent,month(m,True)+2)
    edge(point(c),ent,1,'entrega después del cierre del período')
    edge(ent,act,10,'revisión de cierre')
    node(prod,month(m+1)+3)
    edge(act,prod,0,'producción después de acta')
    edge(prod,'S:'+accept,0,'aceptación posterior a producción')
node('OLA3',ix(date(2028,2,29)))
for c in ['4.1.4','6.5.4']:
    edge(point(c),'OLA3',0,'D-38: piloto y 28 kits antes de la ola 3')
for c in ['5.4.1','5.4.2']:
    edge(point(c),'OLA3',0,'D-27: acuerdos antes del reparto')

# Topología: ningún vínculo se omite por incumplir la propuesta diaria anterior.
q=deque(sorted(n for n in base if indeg[n]==0));order=[];counts=dict(indeg)
while q:
    n=q.popleft();order.append(n)
    for v,w,why in adj[n]:
        counts[v]-=1
        if counts[v]==0:q.append(v)
assert len(order)==len(base),('Ciclo', [n for n in base if n not in order])
caps={'DES':40,'CAL':13}
priority={n:10**9 for n in base}
for h,(m,_) in M.items():priority['ACT:'+h]=month(m) if h in ('H6','H11') else month(m,True)+1
for n in reversed(order):
    for v,w,_ in adj[n]:priority[n]=min(priority[n],priority[v]-w)
heap=[]; remaining=dict(indeg); prioritized=[]
for n in base:
    if remaining[n]==0:heappush(heap,(priority[n],base[n],n))
while heap:
    _,_,n=heappop(heap);prioritized.append(n)
    for v,w,_ in adj[n]:
        remaining[v]-=1
        if remaining[v]==0:heappush(heap,(priority[v],base[v],v))
assert len(prioritized)==len(order)
def forward(caps, groups=None, sequence=None):
    groups=groups or {}
    es=dict(base); crit={}; booked=defaultdict(float)
    for n in sequence or order:
        if n.startswith('S:') and n[2:] in P:
            p=P[n[2:]]; role=groups.get(p['role'],p['role'])
            if role in caps:
                days=p['duration']; ppl=p['peak']
                if ppl>caps[role]:raise ValueError((n,role,ppl,caps[role]))
                while any(booked[role,t]+ppl>caps[role] for t in range(es[n],es[n]+days)):
                    es[n]+=1
                for t in range(es[n],es[n]+days):booked[role,t]+=ppl
        for v,w,why in adj[n]:
            if es[n]+w>es[v]:es[v]=es[n]+w;crit[v]=(n,w,why)
    return es,crit,booked
ES,critical,_=forward({})
EL,_,booked=forward(caps)
# Límites de contraste de paquetes con entregable, no disponibilidad acreditada.
caps_all={'DES':40,'CAL':13,'ARQ_DAT':15,'SRE':12,'SEG':7,'IMP':27,'JP':5}
EA,_,booked_all=forward(caps_all,{'ARQ':'ARQ_DAT','DAT':'ARQ_DAT'},prioritized)

def path_to(n):
    path=[]
    while n in critical:
        p,w,why=critical[n];path.append((p,n,w,why));n=p
    return list(reversed(path))

results=[];all_ls={n:10**9 for n in base}
for h,(m,codes) in M.items():
    start_hito=h in ['H6','H11']
    deadline=month(m) if start_hito else month(m,True)+1
    LS={n:10**9 for n in base};LS['ACT:'+h]=deadline
    for n in reversed(order):
        for v,w,_ in adj[n]:
            if LS[v]<10**9:LS[n]=min(LS[n],LS[v]-w)
    for n in base:all_ls[n]=min(all_ls[n],LS[n])
    chain=path_to('ENT:'+h)
    # La dispersión se aplica a la duración de trabajo, no al tiempo fijo de revisión.
    contributions=defaultdict(float)
    for a,b,w,why in chain:
        if why=='duración por capacidad':contributions[b[2:]]+=w
        elif why.startswith('trabajo:'):contributions[why.split(':',1)[1]]+=w
        elif why in ['interfaz: integración tras entrega','D-24: corte final A06']:
            contributions[b[2:]]+=w
    durations=list(contributions.values())
    sigma=None
    slack=deadline-ES['ACT:'+h]
    pert_margin=deadline-ES['ENT:'+h]-(0 if start_hito else 10)
    probability=None
    packages=[]
    for a,b,w,why in chain:
        if b.startswith('F:') and b[2:] in P and b[2:] not in packages:packages.append(b[2:])
    results.append({'hito':h,'mes':m,'entrega':display(ES['ENT:'+h],not start_hito),
      'acta_temprana':display(ES['ACT:'+h],not start_hito),'limite_entrega':display(deadline-(0 if start_hito else 10),not start_hito),
      'limite_acta':display(deadline,not start_hito),'holgura_dias':slack,
      'camino':packages,'sigma_dias':sigma,'probabilidad_pert':None,
      'duraciones_camino':durations,'eventos_camino':chain})

# Las ventanas por paquete también son restricciones: no se inventa un hito
# contractual para los entregables administrativos sin enlace directo a E-25.
for c in P:
    mm=list(map(int,EFF[c][3].split('–')))
    all_ls['F:'+c]=min(all_ls['F:'+c],month(mm[-1],True)+1)
for n in reversed(order):
    for v,w,_ in adj[n]:
        if all_ls[v]<10**9:all_ls[n]=min(all_ls[n],all_ls[v]-w)
detail=[]
for c,p in P.items():
    tf=min(all_ls['S:'+c]-ES['S:'+c],all_ls['F:'+c]-ES['F:'+c])
    detail.append({'paquete':c,'hh':p['hh'],'duracion_dias':p['duration'],
      'inicio':display(ES['S:'+c]),'fin':display(ES['F:'+c],True),
      'inicio_tardio':display(all_ls['S:'+c]),'fin_tardio':display(all_ls['F:'+c],True),
      'holgura_hitos':tf,'inicio_publicado':p['published_start'],'fin_publicado':p['published_finish']})

violations=[]
for a in adj:
    for b,w,why in adj[a]:
        if ES[b]<ES[a]+w:violations.append((a,b,w))
assert not violations
out={'metodo':'CPM por duración de trabajo, con restricciones mensuales y escenario de capacidad',
     'supuestos':['Inicio nominal febrero2027; calendario interno heredado pendiente de confirmación del CLIENTE',
                  'Duraciones por techo de HH/(6.4*personas máximas); liberaciones mensuales',
                  'Puertas internas y esperas por dependencias; las fechas diarias base solo se muestran para contraste',
                  'No se acredita asignación nominal ni nivelación fina de recursos por actividad',
                  'H7/H12 incluyen revisión del cierre, producción posterior y revisión de aceptación',
                  'Sin probabilidades PERT; el límite de recursos solo se aplica a paquetes con entregable de DES y CAL'],
     'nodos':len(base),'aristas':sum(map(len,adj.values())),'paquetes_entregables':len(P),
     'paquetes_totales':len(EFF),'hh_paquetes':sum(float(r[7]) for r in EFF.values()),
     'hh_programadas':220023,'feriados':[d.isoformat() for d in sorted(HOLIDAYS)],
     'hitos':results,'paquetes':detail,'violaciones_precedencia':violations}
out['limitado']={h: {'entrega':display(EL['ENT:'+h],h not in ('H6','H11')), 'acta':display(EL['ACT:'+h],h not in ('H6','H11')), 'holgura':month(m,True)+1-EL['ACT:'+h] if h not in ('H6','H11') else month(m)-EL['ACT:'+h]} for h,(m,_) in M.items()}
out['modulos_limitado']={c:[display(EL['S:'+c]),display(EL['F:'+c],True)] for c in P if c.startswith(('3.4.','3.5.'))}
out['limites']=caps
out['contraste_todas_familias']={h:{'acta':display(EA['ACT:'+h],h not in ('H6','H11')),'holgura':(month(m) if h in ('H6','H11') else month(m,True)+1)-EA['ACT:'+h]} for h,(m,_) in M.items()}
out['limites_todas_familias']=caps_all
out['picos_todas_familias']={r:max(v for (k,t),v in booked_all.items() if k==r) for r in caps_all}
out['pico_reservado']={r:max(v for (k,t),v in booked.items() if k==r) for r in caps}
out['cierre']={k:display(v) for k,v in ES.items() if k.startswith(('PROD:','CIERRE-'))}
# Alternativa de expediente integrado. La preparación se adelanta; la revisión
# formal comienza una vez entregada la evidencia completa. No se presume acuerdo.
out['expediente_integrado']={}
for h, m, package in [('H7',16,'4.2.3'),('H12',21,'4.3.3')]:
    entrega=month(m)
    revision_inicio=entrega+1
    revision_fin=revision_inicio+9
    produccion=max(revision_fin+1,month(m)+3)
    dias=math.ceil(P[package]['hh']/(6.4*P[package]['peak']))
    assert dias==7 and P[package]['hh']==80
    assert produccion<=month(m,True)
    out['expediente_integrado'][h]={
       'preparacion':[display(entrega-dias+1),display(entrega-1)],
       'entrega':display(entrega),
       'revision':[display(revision_inicio),display(revision_fin)],
       'produccion':display(produccion),
       'holgura_habil':month(m,True)-produccion,
       'condicion':'Confirmación escrita del procedimiento, firma antes del corte y ausencia de observaciones'}

OUT.mkdir(parents=True,exist_ok=True)
(OUT/'resultado_cpm_pert.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
for h in results:print(h['hito'],h['entrega'],h['acta_temprana'],h['holgura_dias'],h['camino'],h['sigma_dias'])
print('Nodos',len(base),'aristas',out['aristas'],'; HH',out['hh_paquetes'])

print('limitado',out['limitado'],out['pico_reservado'])
