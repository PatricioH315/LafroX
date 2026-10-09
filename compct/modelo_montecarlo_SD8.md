# Modelo de Monte Carlo del SD8 (nota de trabajo, no entregable)

Código usado para las Tablas B.2, C.3, C.4, C.6 y D.2 del SD8. Ejecutar: python -I modelo.py <carpeta LafroX> 5000 > salida.json. Requiere Python 3.12 y NumPy. Lee el T-15, compct/T15_actividades_internas.md (respaldo de la nivelación), el SD7, el Anexo 7.B y la Tabla B.1 del Anexo 8.B.

~~~python
import sys, re, json, hashlib, calendar, math, time
from pathlib import Path
from datetime import date, timedelta
import numpy as np
ROOT=Path(sys.argv[1]).resolve()
N=int(sys.argv[2]) if len(sys.argv)>2 else 5000
SEED=20261008
def file(prefix,name):
    return next(ROOT.glob(prefix+'*/'+name))
def read(p): return p.read_text(encoding='utf-8-sig')
T15=file('07_','LAFROX-Formulario-T-15.md')
T7=file('07_','LAFROX-Subdocumento7.md')
A7=file('07_','LAFROX-Subdocumento7-Anexos.md')
A8=file('08_','LAFROX-Subdocumento8-Anexos.md')
def rows(t):
    return [[s.strip() for s in l.strip().strip('|').split('|')]
            for l in t.splitlines() if l.startswith('|')]
t=read(T15)
pr=rows(t.split('### 4.2 Horas')[1].split('### 4.3')[0])
pkg={}
for c in pr:
    if re.fullmatch(r'\d+(?:\.\d+)+',c[0]):
        a,b=map(int,c[3].split('–'))
        pkg[c[0]]={'id':c[0],'class':c[1],'role':c[2],'a':a,'b':b,'hh':float(c[7])}
ar=rows(read(ROOT/'compct'/'T15_actividades_internas.md').split('### 6.1 Paquetes')[1].split('### 6.2')[0])
acts=[]
for c in ar:
    if re.fullmatch(r'\d+(?:\.\d+)+\.A\d+',c[0]):
        dep=[(m[0],bool(m[1])) for m in re.findall(r'(\d+(?:\.\d+)+(?:\.A\d+)?)(\s*\(CC\))?',c[8])]
        acts.append({'id':c[0],'pkg':c[0].split('.A')[0],'role':c[2],
                     'people':int(c[3]),'hh':float(c[4]),'start':c[5],
                     'end':c[6],'days':int(c[7]),'dep':dep})
assert len(pkg)==222 and len(acts)==564
assert abs(sum(p['hh'] for p in pkg.values())-204527)<1e-6
ap={a['pkg'] for a in acts}
assert len(ap)==163
for k in ap: assert abs(sum(a['hh'] for a in acts if a['pkg']==k)-pkg[k]['hh'])<1e-6
ROLES=['JP','ARQ','SEG','DAT','DES','CAL','SRE','IMP']
def monthdate(m):
    y=2027+(m)//12; mm=(m)%12+1
    return date(y,mm,1)
def parse(s): return date(*reversed(list(map(int,s.split('-')))))
START=date(2027,2,1)
DAYS=[START+timedelta(days=i) for i in range(365*7) if (START+timedelta(days=i)).weekday()<5]
DAYS=DAYS[:1800]; H=len(DAYS)
def di(d): return int(np.searchsorted(DAYS,d))
MONTH=np.array([(d.year-2027)*12+d.month-1 for d in DAYS])
def fmt(i): return DAYS[min(int(i),H-1)].strftime('%d-%m-%Y')
# HH por paquete y mes: las fechas de actividades gobiernan los productos.
pm={}
for k,p in pkg.items():
    v=np.zeros((56,8)); ri=ROLES.index(p['role'])
    if k in ap:
        for a in acts:
            if a['pkg']!=k: continue
            ix=np.arange(di(parse(a['start'])),di(parse(a['end']))+1)
            assert len(ix)==a['days'],a['id']
            for m in set(MONTH[ix]):
                v[m-1,ri]+=a['hh']*np.sum(MONTH[ix]==m)/len(ix)
    else:
        ms=list(range(p['a'],p['b']+1))
        weights=np.ones(len(ms))
        if k=='4.2.2': weights=np.array([2464,1312,544,544,544.])
        if k=='4.3.2': weights=np.array([2361.33,102.67])
        if k in ('8.1.1','8.1.5'):
            weights=np.array([calendar.monthrange(monthdate(m).year,monthdate(m).month)[1]*24 for m in ms])
        if k=='8.1.2':
            weights=[]
            for m in ms:
                d=monthdate(m); nd=calendar.monthrange(d.year,d.month)[1]
                ls=sum(date(d.year,d.month,j).weekday()<6 for j in range(1,nd+1))
                su=nd-ls; weights.append((ls*58 if m>=25 else ls*41)+(ls*6+su*24 if d.month in (9,12) else 0))
            weights=np.array(weights,float)
        for m,w in zip(ms,weights/np.sum(weights)):
            v[m-1,ri]+=p['hh']*w
    assert abs(v.sum()-p['hh'])<1e-5,k
    pm[k]=v
MAP=[
['3.3.2','4.1.2'],['3.3.6','3.4.2','3.4.6','3.8.1'],
['6.6.3','3.8.3','3.8.5'],['3.4.6','3.4.8','3.4.10','3.8.3'],
['3.8.5','3.9.4','8.2.7'],['3.8.4','3.9.3'],
['3.3.1','3.8.6','3.9.5','8.2.2'],['2.1','3.3','3.11','9.2'],
['8.2.2','8.2.3','8.2.4'],['1.2.3','3.3.2','3.3.5'],
sorted([k for k in ap if pkg[k]['b']<=21]),
['1.1.3','1.8','2.4','7.3'],['1.2.2','3.4.7'],['3.5','3.9'],
['3.5.1','3.6.5','3.6.6'],['3.7.1','3.7.2','3.7.3','3.7.4','3.7.5'],
['1.1.3','1.3.1','4.1.3'],['4.2.1','4.3.1','7.3','3.9.3'],
['5.1.2','6.1','6.3','6.6.3','6.5'],['7.1.2','7.2.1','7.3.1','7.3.2'],
['5.4.1','5.4.2','6.5'],['4.2.2','8.1.1','8.1.2'],
['3.4.5','6.5','3.8.3'],['3.10.2','3.3.1','3.8.6'],
['3.10.1','7.2.1'],['3.10.2','8.3.1'],['3.10.3','8.3.2'],
['5.4.3','8.3.3','8.3.4'],['3.10.4','8.3.5','8.3.6'],
['2.1','3.8.4','8.2.3'],
['3.8.2','3.8.3','3.9.2','3.9.3','3.9.4','3.9.5'],
['3.8.2','3.8.3','3.8.4','3.8.5','3.8.7','3.9.2','3.9.3','3.9.4','3.9.6']]
CONTROL=[
['4.1.2'],['3.8.1'],['6.6.3'],['3.8.3'],['3.8.5'],['3.8.4'],['3.8.6'],
['1.7.1','8.1.4','9.2.1'],['8.2.5'],['1.2.3'],['1.3.4'],['1.1.1'],
['1.2.2'],['1.3.4'],['2.1.4'],['3.7.1'],['1.1.3'],['4.1.1','7.3.1','7.3.2'],
['5.1.2','5.1.3'],['7.3.1','7.3.2'],['5.4.1','5.4.2'],[],
['6.5.3'],['3.8.6'],['3.10.1.4'],['3.10.2.4'],['3.10.3.4'],
['5.4.3'],['3.10.4.1','8.3.6'],['8.2.3'],['3.8.1','3.9.1'],['1.5.1']]
qrows=rows(read(A8).split('### B.1')[1].split('### B.2')[0])
evals={c[0]:(int(c[2]),int(c[3]),int(c[4])) for c in qrows if c[0].startswith('R8-')}
prob=np.array([{1:.05,2:.2,3:.4,4:.6,5:.8}[evals[f'R8-{i+1:02}'][0]] for i in range(32)])
frac=np.array([{1:0,2:.05,3:.1,4:.2,5:.3}[evals[f'R8-{i+1:02}'][1]] for i in range(32)])
expanded=[]; X=np.zeros((32,56,8))
for i,mp in enumerate(MAP):
    ks=sorted({k for k in pkg if any(k==p or k.startswith(p+'.') for p in mp)})
    expanded.append(ks)
    X[i]=sum((pm[k] for k in ks),np.zeros((56,8)))*frac[i]
X[17]=0; X[17,14,7]=2464; X[17,19,7]=2464
X[21]=0
for m in range(21,57):
    d=monthdate(m); nd=calendar.monthrange(d.year,d.month)[1]
    X[21,m-1,6]=4*sum(date(d.year,d.month,j).weekday()<6 for j in range(1,nd+1))
# Una correccion por paquete/perfil. Los dos grupos comparten efecto de capacidad o interfaz.
GROUPS=[[10,13,31],[9,14]]
def cost_expected(ps,correlated=False):
    out=X*ps[:,None,None]
    for group in GROUPS:
        out[group]=0
        outcomes=[]
        if correlated:
            edges=sorted({0.,1.,*ps[group]})
            for lo,hi in zip(edges,edges[1:]): outcomes.append((hi-lo,np.array([(lo+hi)/2<ps[g] for g in group])))
        else:
            for bits in range(1<<len(group)):
                on=np.array([bool(bits&(1<<j)) for j in range(len(group))])
                w=np.prod([ps[g] if z else 1-ps[g] for g,z in zip(group,on)])
                outcomes.append((w,on))
        for w,on in outcomes:
            if not any(on): continue
            stack=np.stack([X[g] if z else np.zeros((56,8)) for g,z in zip(group,on)])
            winner=stack.argmax(axis=0); maximum=stack.max(axis=0)
            for j,g in enumerate(group): out[g]+=w*np.where(winner==j,maximum,0)
    return out
EC=cost_expected(prob); ER=cost_expected(np.where(np.arange(32)==21,prob,np.maximum(prob-.2,0)))
CC=cost_expected(prob,True)
raw=(X*prob[:,None,None]).sum()
# Proteccion E1: solo trabajo de E1 en meses13-20 y perfiles DES/CAL.
eligible=np.zeros((56,8))
for i in (1,3): # R8-14 es exposicion E2, no correccion E1.
    eligible+=EC[i]
mask=np.zeros((56,8)); mask[12:20,4]=256; mask[12:20,5]=128
absorbed=np.minimum(eligible,mask).sum()
# Grupos de recurso corporativo: ARQ+DAT comparten 15; SOC separado.
RR=['JP','ARQ+DAT','SEG','DES','CAL','SRE','IMP']
ri=[0,1,2,1,3,4,5,6]
rmap=dict(zip(ROLES,ri))
CAP=np.tile(np.array([5.,15,7,40,10,44,30])[:,None],(1,H))
cert=((MONTH>=9)&(MONTH<=12))|((MONTH>=16)&(MONTH<=18))
CAP[4,cert]=16 # capacidad TOTAL durante certificacion, lectura conservadora de T-15.
BG=np.zeros_like(CAP)
for k,p in pkg.items():
    if k in ap or k=='8.1.5': continue
    for m in range(1,57):
        ix=np.flatnonzero(MONTH==m)
        if len(ix): BG[rmap[p['role']],ix]+=pm[k][m-1].sum()/(6.4*len(ix))
for m in range(16,21):
    ix=np.flatnonzero(MONTH==m); BG[5,ix]+=[1851,1786,1810,1851,2038][m-16]/(6.4*len(ix))
for m in range(13,21):
    ix=np.flatnonzero(MONTH==m); BG[3,ix]+=256/(6.4*len(ix)); BG[4,ix]+=128/(6.4*len(ix))
AV=CAP-BG
# Restricciones que afectan entregables/habilitaciones; desarrollo QA no es intervencion productiva.
ids={a['id']:j for j,a in enumerate(acts)}
# Desarrollo explicito de las dependencias del Anexo 7.B que afectan productos.
EDGES=[
(['1.2.1'],['2.1.1'],'FC'),(['1.2.3'],['3.3.2'],'FC'),
(['1.2.2'],['3.4.7'],'FC'),(['2.4.1'],['3.4'],'FC'),
(['2.6.2'],['3.4'],'FC'),(['2.2.1'],['3.3.1'],'FC'),
(['5.2.1'],['3.2'],'FC'),
(['3.2.1','3.2.2','3.2.4','3.2.5'],['3.1.1','3.1.2','3.1.3'],'FC'),
(['2.3.1','2.3.2'],['5.1.2'],'FC'),(['5.1.2'],['6.1'],'FC'),
(['6.1.5'],['6.3.1','6.3.2'],'FC'),
(['6.3.1','6.3.2','6.3.3'],['6.6'],'FC'),
(['3.3'],['3.4'],'CC'),(['3.4.2'],['3.4.6'],'CC'),
(['3.4'],['3.8.1'],'FC'),(['3.8.1'],['3.8.2','3.8.3'],'FC'),
(['3.4'],['3.8.4','3.8.5','3.8.6','3.8.8'],'FC'),
(['3.1.3'],['3.8.5'],'FC'),
(['3.8.2','3.8.3','3.8.4','3.8.5','3.8.6'],['3.8.7'],'FC'),
(['3.7.1','3.7.2'],['3.7.5'],'FC'),
(['1.2.5','2.4.2'],['3.5'],'FC'),(['3.5'],['3.9.1'],'FC'),
(['3.5'],['3.9.3','3.9.4','3.9.5'],'FC'),
(['3.9.1','3.9.2','3.9.3','3.9.4','3.9.5'],['3.9.6'],'FC')]
def pexpand(keys): return sorted(k for k in ap if any(k==p or k.startswith(p+'.') for p in keys))
def endpoint(k,first=False):
    aa=[a['id'] for a in acts if a['pkg']==k]
    return min(aa) if first else max(aa)
added_edges=[]
for pp,ss,kind in EDGES:
    for sk in pexpand(ss):
        dest=acts[ids[endpoint(sk,True)]]
        preds=pexpand(pp)
        if pp==['1.2.2']: preds=['1.2.2']
        for pk in preds:
            ref=(endpoint(pk,kind=='CC') if pk in ap else pk,kind=='CC')
            if ref not in dest['dep']:
                dest['dep'].append(ref); added_edges.append((dest['id'],ref[0],kind))
for pk in pexpand(['3.4']):
    dest=acts[ids[endpoint(pk)]]
    for ak in pexpand(['3.1']):
        ref=(endpoint(ak),False)
        if ref not in dest['dep']: dest['dep'].append(ref); added_edges.append((dest['id'],ref[0],'FC'))
for pp,ss in [(['3.4.1','3.4.2'],['3.4.3','3.4.4']),
              (['3.4.3','3.4.6'],['3.4.7','3.4.8']),(['3.4.8'],['3.4.10'])]:
    for sk in ss:
        for suffix,psuffix in [('A03','A02'),('A10','A12'),('A11','A12')]:
            dest=acts[ids[sk+'.'+suffix]]
            for pk in pp:
                ref=(pk+'.'+psuffix,False)
                if ref not in dest['dep']: dest['dep'].append(ref); added_edges.append((dest['id'],ref[0],'FC'))
# D-24: los ensayos 3.7.3 y 3.7.4 preceden al corte 3.7.5.A06; la preparacion de 3.7.5 avanza en paralelo.
for pk in ('3.7.3','3.7.4'):
    ref=(endpoint(pk),False)
    if ref not in acts[ids['3.7.5.A06']]['dep']: acts[ids['3.7.5.A06']]['dep'].append(ref); added_edges.append(('3.7.5.A06',ref[0],'FC'))
# D-31: la aceptacion 3.9.2 ejecuta (A02) al terminar 3.9.1; su preparacion A01 es paralela.
ref=('3.9.1.A02',False)
if ref not in acts[ids['3.9.2.A02']]['dep']: acts[ids['3.9.2.A02']]['dep'].append(ref); added_edges.append(('3.9.2.A02','3.9.1.A02','FC'))
missing=sorted({k for a in acts for k,cc in a['dep'] if k not in ids and k not in pkg})
dep=[[(ids[k],cc) for k,cc in a['dep'] if k in ids] for a in acts]
release=np.array([di(parse(a['start'])) for a in acts],int)
for j,a in enumerate(acts):
    for k,cc in a['dep']:
        if k in ids: continue
        p=pkg[k.split('.A')[0]]
        last=monthdate(p['b']); last=date(last.year,last.month,calendar.monthrange(last.year,last.month)[1])
        release[j]=max(release[j],di(monthdate(p['a'])) if cc else di(last)+int(last.weekday()<5))
baseline_end=np.array([di(parse(a['end'])) for a in acts],int)
risk_effect=np.zeros((32,len(acts)))
for i in range(32):
    if i in (17,21): continue
    for j,a in enumerate(acts):
        if a['pkg'] in expanded[i]: risk_effect[i,j]=frac[i]
psorted=sorted(ap); pidx={k:i for i,k in enumerate(psorted)}
pof=np.array([pidx[a['pkg']] for a in acts])
hpk={1:['1.2.1','1.2.4'],2:['2.4.1'],3:['3.1.1','3.1.2','3.1.3','3.1.5','6.6.3'],
     4:['3.8.1'],5:['3.8.7'],8:['1.2.5','2.4.2'],9:['3.9.1'],10:['3.9.6']}
hmonths={1:2,2:4,3:6,4:10,5:12,8:14,9:17,10:18}
hids={h:np.array([j for j,a in enumerate(acts) if a['pkg'] in ks]) for h,ks in hpk.items()}
limits={}
for h,m in {**hmonths,6:13,11:19}.items():
    md=monthdate(m); last=date(md.year,md.month,calendar.monthrange(md.year,md.month)[1])
    lim=di(last)-(last.weekday()>=5)-10
    limits[h]=lim
# Propagar prioridad de los hitos a los antecesores.
priority=np.full(len(acts),H-1,int)
for h,jx in hids.items(): priority[jx]=np.minimum(priority[jx],limits[h])
for repeat in range(len(acts)):
    change=False
    for j,ds in enumerate(dep):
        for k,cc in ds:
            if priority[k]>priority[j]: priority[k]=priority[j]; change=True
    if not change: break
order=[]; done=set()
while len(order)<len(acts):
    ready=[j for j in range(len(acts)) if j not in done and all(k in done for k,cc in dep[j])]
    assert ready,'Ciclo en predecesoras'
    j=min(ready,key=lambda j:(priority[j],release[j],acts[j]['id']))
    done.add(j); order.append(j)
source_errors=[(acts[j]['id'],acts[k]['id'],'CC' if cc else 'FC')
              for j in range(len(acts)) for k,cc in dep[j]
              if di(parse(acts[j]['start']))<(di(parse(acts[k]['start'])) if cc else baseline_end[k]+1)]
load=BG.copy()
for j,a in enumerate(acts): load[rmap[a['role']],release[j]:baseline_end[j]+1]+=a['people']
source_peak=(load-CAP).max(axis=1)
old_jp_cap=float(CAP[0,0])
CAP[0,:]=math.ceil(float(load[0].max()))
AV=CAP-BG
source_peak=(load-CAP).max(axis=1)
def permitted(d):
    first=monthdate((d.year-2027)*12+d.month-1)
    first3=[first+timedelta(days=z) for z in range(7) if (first+timedelta(days=z)).weekday()<5][:3]
    return not(d.month==12 or (d.month==9 and d.day<=25) or d in first3)
protected_ids={j for j,a in enumerate(acts) if a['pkg'] in {'6.5.1','6.5.2','6.5.3','6.5.4','6.5.5','6.5.6'} or a['id']=='3.7.5.A06'}
blocked=np.array([not permitted(d) for d in DAYS])
def schedule(factor,on):
    b=len(factor); starts=np.zeros((b,len(acts)),np.int32); ends=starts.copy()
    durfactor=on@risk_effect
    for group in GROUPS:
        vals=np.stack([on[:,g,None]*risk_effect[g] for g in group])
        durfactor-=vals.sum(axis=0); durfactor+=vals.max(axis=0)
    dd=np.ceil(np.array([a['hh']/a['people']/6.4 for a in acts])[None,:]
               *factor[:,pof]*(1+durfactor)-1e-12).astype(int)
    use=np.zeros((b,len(RR),H),np.float32); br=np.arange(b)
    for j in order:
        a=acts[j]; role=rmap[a['role']]; d=dd[:,j]
        s=np.full(b,release[j],int)
        for k,cc in dep[j]: s=np.maximum(s,starts[:,k] if cc else ends[:,k]+1)
        width=int(d.max()); off=np.arange(width)
        while True:
            ix=s[:,None]+off
            if ix.max()>=H: raise RuntimeError('Horizonte insuficiente')
            need=off[None,:]<d[:,None]
            clash=(use[br[:,None],role,ix]+a['people']>AV[role,ix]+1e-5)&need
            if j in protected_ids: clash|=blocked[ix]&need
            bad=clash.any(axis=1)
            if not bad.any(): break
            # Salto hasta despues del primer dia ocupado/prohibido.
            s[bad]+=clash[bad].argmax(axis=1)+1
        ix=s[:,None]+off; need=off[None,:]<d[:,None]
        use[br[:,None],role,ix]+=need*a['people']
        starts[:,j]=s; ends[:,j]=s+d-1
    for role in range(len(RR)):
        assert np.max(use[:,role]+BG[role]-CAP[role])<1e-4
    hh={h:ends[:,jx].max(axis=1) for h,jx in hids.items()}
    # Preparacion: todos los componentes, usuarios, acuerdos y equipos antes de evidencia.
    e1=[j for j,a in enumerate(acts) if a['pkg'].startswith(('3.4.','3.7.','3.8.','6.5.')) or a['pkg'] in ('4.1.1','4.1.2','5.4.1','5.4.2','7.3.1')]
    e2=[j for j,a in enumerate(acts) if a['pkg'].startswith(('3.5.','3.9.')) or a['pkg'] in ('3.6.5','3.6.6','4.1.3','7.3.2')]
    F1=date(2028,5,5); F2=date(2028,10,5)
    gates=[]
    for ix,F,mbend,m in [(e1,F1,date(2028,4,30),15),(e2,F2,date(2028,9,30),20)]:
        entry_pkg=(['3.8.7','3.7.5','4.1.1','4.1.2'] if m==15 else ['3.9.6','3.6.5','4.1.3'])
        entry_ix=[j for j,a in enumerate(acts) if a['pkg'] in entry_pkg]
        # H6/H11: prerrequisitos a tiempo para el acta del mes 13/19 (misma regla de entrega: acta - 10 habiles).
        gates.append(ends[:,entry_ix].max(axis=1)<=limits[6 if m==15 else 11])
        deadline=F-timedelta(days=28)
        ready=ends[:,ix].max(axis=1)<di(deadline)
        # Cota adversa R8-18: cuatro semanas adicionales, sin extender fecha contractual.
        gates.append(ready)
    return hh,gates,starts,ends
def stats(hh,gates):
    res={}
    for h,v in hh.items():
        good=v<=limits[h]; p=float(good.mean()); z=1.96; den=1+z*z/len(v)
        center=(p+z*z/(2*len(v)))/den
        half=z*math.sqrt(p*(1-p)/len(v)+z*z/(4*len(v)**2))/den
        res[str(h)]={'P50':fmt(np.quantile(v,.5,method='higher')),'P80':fmt(np.quantile(v,.8,method='higher')),
                     'p':p,'ci':[max(0,center-half),min(1,center+half)],'limit':fmt(limits[h])}
    allh=np.logical_and.reduce([v<=limits[h] for h,v in hh.items()])
    res['joint_delivery']=float(allh.mean())
    res['H6_ready']=float(gates[0].mean()); res['gate_E1']=float(gates[1].mean())
    res['H11_ready']=float(gates[2].mean()); res['gate_E2']=float(gates[3].mean())
    res['joint_readiness']=float((allh&np.logical_and.reduce(gates)).mean())
    res['readiness_ci']={}
    for key in ['H6_ready','gate_E1','H11_ready','gate_E2','joint_delivery','joint_readiness']:
        p=res[key]; z=1.96; den=1+z*z/len(v)
        center=(p+z*z/(2*len(v)))/den
        half=z*math.sqrt(p*(1-p)/len(v)+z*z/(4*len(v)**2))/den
        res['readiness_ci'][key]=[max(0,center-half),min(1,center+half)]
    return res
def run(corr=False,remove=None):
    rng=np.random.Generator(np.random.PCG64(SEED))
    factors=rng.beta(3,3,size=(N,len(psorted)))*.5+.75
    u=rng.random((N,32))
    if corr:
        for g in GROUPS: u[:,g]=u[:,g[0],None]
    on=u<prob
    if remove is not None: on[:,remove]=False
    hhout={h:[] for h in hids}; gout=[[],[],[],[]]
    for lo in range(0,N,250):
        hh,gg,_,_=schedule(factors[lo:lo+250],on[lo:lo+250])
        for h,v in hh.items(): hhout[h].append(v)
        for i,v in enumerate(gg): gout[i].append(v)
    return stats({h:np.concatenate(v) for h,v in hhout.items()},[np.concatenate(v) for v in gout])
st=time.time()
zero=schedule(np.ones((1,len(ap))),np.zeros((1,32),bool))
out={'n':N,'seed':SEED,'numpy':np.__version__,'hashes':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [T15,T7,A7]},
     'packages':pkg,'expanded':expanded,'map':MAP,'controls':CONTROL,'prob':prob.tolist(),'frac':frac.tolist(),
     'X':X.tolist(),'EC':EC.tolist(),'ER':ER.tolist(),'CC':CC.tolist(),
     'raw':raw,'portfolio':float(EC.sum()),'residual':float(ER.sum()),'correlated_cost':float(CC.sum()),
     'absorbed':float(absorbed),'additional':float(EC.sum()-absorbed),
     'base':stats(zero[0],zero[1]),'source_precedence_errors':source_errors,
     'source_peak_excess':dict(zip(RR,source_peak.tolist())),'jp_requested_capacity':float(CAP[0,0]),
     'missing_activity_references':missing,'added_dependency_edges':added_edges,
     'base_delayed_activities':int(np.sum(zero[2][0]>np.array([di(parse(a['start'])) for a in acts]))),
     'base_p80_dates':{str(h):fmt(v[0]) for h,v in zero[0].items()},
     'activity_count':len(acts),'product_packages':len(ap),'r11_count':len(expanded[10]),
     'r11_role_hh':{r:float(sum(pm[k][:,i].sum() for k in expanded[10])) for i,r in enumerate(ROLES)},
     'independent':run(),'adverse':run(True)}
print('BASE_AND_MAIN_READY '+json.dumps({k:out[k] for k in ['portfolio','raw','additional','base','independent','adverse','source_peak_excess','source_precedence_errors']},ensure_ascii=False),file=sys.stderr,flush=True)
out['sensitivity']={}
for i in [10,13,14,18,22,30,31,5]:
    out['sensitivity'][f'R8-{i+1:02}']=run(remove=i)
    print('SENSITIVITY_DONE R8-%02d'%(i+1),file=sys.stderr,flush=True)
out['elapsed']=time.time()-st
print(json.dumps(out,ensure_ascii=False))
~~~
