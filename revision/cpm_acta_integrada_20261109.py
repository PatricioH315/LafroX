"""CPM por duraciones con acta integrada de H7/H12 (09-11-2026).

Deriva de recalcular_cpm_texto_sd7.py. Cambio de modelo: el expediente de H7/H12
se entrega el primer día hábil tras las cuatro semanas finales; la Contraparte
revisa diez días hábiles (BA, art. 18.3) y firma el acta del art. 17.3, que es
también el acta del hito (art. 18.1); el paso a producción ocurre después de la
firma y dentro del mes 16 o 21. No hay segunda revisión posterior a producción.
Escribe tab_T15_7 y tab_T15_cpm_detalle con los resultados.
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
    code,role,people,hh,start,end,preds=r; hh=hh.replace(',','.')
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
INTEGRADO={'H7':'4.2.3','H12':'4.3.3'}
for h,(m,codes) in M.items():
    node('ENT:'+h)
    for c in codes:
        if INTEGRADO.get(h)==c:
            # El expediente se consolida y entrega el primer día del paquete.
            edge('S:'+c,'ENT:'+h,1,'entrega del expediente integrado');continue
        edge(point(c,'S' if h in ['H6','H11'] else 'F'),'ENT:'+h,0,'entrega del hito')
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
# D-51: las demás cadenas se habilitan antes de las cuatro semanas finales de E2
# (20 días hábiles antes de la entrega del expediente del H12).
edge('F:3.6.6','ENT:H12',20,'D-51: cadenas antes de F-28')
# Acta integrada: producción después de la firma, fuera de los tres primeros
# días hábiles del mes; el paquete de aceptación registra el paso el mismo día.
for h,m,accept in [('H7',16,'4.2.3'),('H12',21,'4.3.3')]:
    prod='PROD:'+h
    node(prod,month(m)+3)
    edge('ACT:'+h,prod,0,'producción después del acta del art. 17.3')
    edge(prod,'F:'+accept,1,'registro del paso efectivo')
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
    if h in INTEGRADO:LS['PROD:'+h]=month(m,True)
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
    if h in INTEGRADO:slack=min(slack,month(m,True)-ES['PROD:'+h])
    pert_margin=deadline-ES['ENT:'+h]-(0 if start_hito else 10)
    probability=None
    packages=[]
    for a,b,w,why in chain:
        if b.startswith('F:') and b[2:] in P and b[2:] not in packages:packages.append(b[2:])
    results.append({'hito':h,'mes':m,'entrega':display(ES['ENT:'+h],not start_hito),
      'acta_temprana':display(ES['ACT:'+h],not start_hito),'limite_entrega':display(deadline-(0 if start_hito else 10),not start_hito),
      'limite_acta':display(deadline,not start_hito),'holgura_dias':slack,
      'produccion':display(ES['PROD:'+h]) if h in INTEGRADO else None,
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
BS2 = chr(92) * 2
def dmy(iso): y, m, d = iso.split('-'); return f'{d}-{m}-{y}'
def hold(es_map, h, m):
    if h in ('H6', 'H11'): return month(m) - es_map['ACT:' + h]
    s = month(m, True) + 1 - es_map['ACT:' + h]
    if h in INTEGRADO: s = min(s, month(m, True) - es_map['PROD:' + h])
    return s
ORDER = ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H8', 'H7', 'H9', 'H10', 'H11', 'H12']
res = {r['hito']: r for r in results}
lines = []
for h in ORDER:
    m = M[h][0]; r = res[h]; start = h in ('H6', 'H11')
    lim = display(month(m)) if start else display(month(m, True) + 1, True)
    prod = dmy(r['produccion']) if r['produccion'] else '—'
    ctrl = 'Inicio contractual fijo' if start else {'H7': '4.2.1 y 4.2.3', 'H12': '4.3.1 y 4.3.3'}.get(h, r['camino'][-1] if r['camino'] else '—')
    lines.append(f"  {h} & {dmy(r['entrega'])} & {dmy(r['acta_temprana'])} & {prod} & {dmy(lim)} & "
                 f"{hold(ES, h, m)} & {hold(EL, h, m)} & {ctrl} {BS2}")
T7 = ROOT / 'formulario-t15/tablas/tab_T15_7.tex'
head = (r"\begin{anexohorizontal}\setlength{\textwidth}{\linewidth}" "\n"
        r"\begin{tablalafrox}{Fechas y holguras de los hitos calculadas por duraciones y precedencias, con la línea base de 220.023 HH. Fuente: elaboración a partir de las secciones 4.2, 5.1 y 6.1, y del Anexo 7.B.}{tab_T15_7}" "\n"
        r"  {C{0.75cm} L{1.8cm} L{1.8cm} L{1.8cm} L{1.8cm} C{1.4cm} C{1.9cm} Y}" "\n"
        r"  {\cab{Hito} & \cab{Entrega} & \cab{Acta} & \cab{Paso a producción} & \cab{Límite contractual} & \cab{Holgura (días hábiles)} & \cab{Holgura con límite de capacidad} & \cab{Paquete controlante}}" "\n")
T7.write_text(head + '\n'.join(lines) + '\n' + r"\end{tablalafrox}" + '\n' + r"\end{anexohorizontal}" + '\n', encoding='utf-8')

def hh(x): return str(int(x)) if float(x).is_integer() else f'{x:.2f}'.replace('.', ',')
det = []
fuera = []
for d in detail:
    c = d['paquete']
    det.append(f"  {c} & {d['duracion_dias']} & {dmy(d['inicio'])} & {dmy(d['fin'])} & {dmy(d['inicio_tardio'])} & "
               f"{dmy(d['fin_tardio'])} & {d['holgura_hitos']} & {hh(d['hh'])} {BS2}")
    if d['inicio_publicado'] < d['inicio'] or d['fin_publicado'] > d['fin_tardio']:
        fuera.append((c, d['inicio_publicado'], d['inicio'], d['fin_publicado'], d['fin_tardio']))
TD = ROOT / 'formulario-t15/tablas/tab_T15_cpm_detalle.tex'
old = TD.read_text(encoding='utf-8').splitlines()
keep_head = [l for l in old if not re.match(r'^\s*\d+(\.\d+)+\s*&', l)]
idx = next(i for i, l in enumerate(keep_head) if l.strip().startswith(r'\end{tablalafrox}'))
TD.write_text('\n'.join(keep_head[:idx] + det + keep_head[idx:]) + '\n', encoding='utf-8')

out = {'metodo': 'CPM por duraciones con acta integrada H7/H12', 'nodos': len(base),
       'aristas': sum(map(len, adj.values())), 'hitos': results,
       'holgura_capacidad': {h: hold(EL, h, M[h][0]) for h in ORDER},
       'pico_reservado': {r: max(v for (k, t), v in booked.items() if k == r) for r in caps},
       'carta_fuera_de_ventana': fuera, 'paquetes_negativos': [d['paquete'] for d in detail if d['holgura_hitos'] < 0]}
OUT.mkdir(parents=True, exist_ok=True)
(OUT / 'resultado_acta_integrada.json').write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
for l in lines: print(l)
print('Nodos', out['nodos'], 'aristas', out['aristas'], 'pico', out['pico_reservado'])
print('Carta fuera de ventana CPM:', len(fuera), fuera[:12])
print('Paquetes con holgura negativa:', out['paquetes_negativos'])
