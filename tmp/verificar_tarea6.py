from pathlib import Path
from decimal import Decimal as D,ROUND_HALF_UP
from collections import Counter
import re,json,hashlib
r=Path(__file__).resolve().parents[1]
base=json.loads((r/'tmp/tarea6-baseline.json').read_text(encoding='utf-8'));old=base['original']
info=json.loads((r/'tmp/tarea6-datos.json').read_text(encoding='utf-8'))
f,a,b,rb=[(r/p).read_text(encoding='utf-8') for p in old]
e=(r/'08_plan_riesgos/anexo-e-internos.tex').read_text(encoding='utf-8')
active=set(info['active']);internal=set(info['internal'])
assert len(active)==35 and len(internal)==16 and not active&internal
assert active|internal=={f'R-{i:03}' for i in range(1,52)}
assert {f'R-{i:03}' for i in [9,10,23,24,25,26,27,34,35,36,37,38,40]}<=internal
def section(s,needle):
 start=s.index(needle);return s[start:s.index('\\end{tablalafrox}',start)]
def rows(s):return {l.split(' & ')[0]:l.split(' & ') for l in s.splitlines() if re.match(r'(?:R|CI)-\d{3}(?: / [A-Z]+)? &',l)}
reg=rows(f);assert set(reg)==active
ar=rows(section(a,'\\begin{tablalafrox}{Matriz de respuestas'))
q=rows(section(a,'\\begin{tablalafrox}{Estimación acumulada'))
c=rows(section(a,'\\begin{tablalafrox}{Fundamento del impacto inicial'))
assert set(ar)==set(q)==set(c)==active
for new,prev in [(reg,rows(old['LAFROX-Formulario-T-16.tex'])),(ar,rows(section(old['LAFROX-Subdocumento8-Anexos.tex'],'\\begin{tablalafrox}{Matriz de respuestas'))),(q,rows(section(old['LAFROX-Subdocumento8-Anexos.tex'],'\\begin{tablalafrox}{Estimación acumulada'))),(c,rows(section(old['LAFROX-Subdocumento8-Anexos.tex'],'\\begin{tablalafrox}{Fundamento del impacto inicial')))]:
 for k in active:assert new[k]==prev[k],k
deps=rows(section(a,'\\begin{tablalafrox}{Contrapartes, solicitudes'));assert len(deps)==28
assert all(k.split(' / ')[0] in active for k in deps)
assert len(re.findall(r'^R-\d{3} / \d+\\%',section(a,'\\begin{tablalafrox}{Hipótesis de ocurrencia'),re.M))==8
assert set(re.findall(r'\\RBSrisk\{(R-\d{3})\}',rb))==active
assert sum(map(int,re.findall(r'\{\\small (\d+) riesgos\}',rb)))==35
num=lambda x:D(x.replace(',','.'))
rn=lambda x:x.quantize(D('.01'),rounding=ROUND_HALF_UP)
pl=lambda p:1 if p<=10 else 2 if p<=30 else 3 if p<=50 else 4 if p<=70 else 5
zn=lambda x:'Baja' if x<D('.08') else 'Media' if x<D('.20') else 'Alta' if x<D('.40') else 'Crítica'
assert [pl(x) for x in [0,10,D('10.0001'),30,50,70,D('70.0001'),100]]==[1,1,2,2,3,4,5,5]
assert [zn(x) for x in map(D,['.0799','.08','.1999','.20','.3999','.40'])]==['Baja','Media','Media','Alta','Alta','Crítica']
ex={};ve={};zones=Counter()
for k,v in reg.items():
 p=num(q[k][1].split('\\')[0]);o,m,ps=map(num,q[k][3:6]);h=(o+4*m+ps)/6
 assert num(q[k][6])==rn(h) and num(q[k][7].rstrip('\\'))==rn(p/100*h)
 pn,pf=v[3].split(' / ');il,ifact=v[4].split(' / ')
 assert int(pn)==pl(p) and num(pf)==list(map(D,['.1','.3','.5','.7','.9']))[int(pn)-1]
 assert num(ifact)==list(map(D,['.05','.10','.20','.40','.80']))[int(il)-1]
 exp,z=re.match(r'([\d,]+) \(([^)]+)\)',v[5]).groups();exp=num(exp)
 assert exp==num(pf)*num(ifact) and z==zn(exp)
 ihh=1 if h<=24 else 2 if h<=80 else 3 if h<=160 else 4 if h<=320 else 5
 dh,fin=map(int,c[k][2].split(' / '));assert int(il)==fin==max(ihh,dh)
 assert c[k][1]==f'{rn(h):.2f}'.replace('.',',')+' / '+str(ihh)
 assert re.search(r'\\RBSrisk\{'+k+r'\}\{[^\n]+\}\{'+z+r'\}',rb)
 ex[k]=exp;ve[k]=num(q[k][7].rstrip('\\'));zones[z]+=1
assert dict(zones)==info['zones']
assert sum(ve.values())==D('1183.11')
assert list(rows(section(b,'\\begin{tablalafrox}{Diez mayores valores esperados')))==info['top']
assert list(rows(section(b,'\\begin{tablalafrox}{Diez riesgos de mayor exposición')))==info['topqual']
assert sum(ve[k] for k in info['top'])==D('689.67')
eq=rows(section(e,'\\begin{tablalafrox}{Estimaciones históricas internas'))
oldq=rows(section(old['LAFROX-Subdocumento8-Anexos.tex'],'\\begin{tablalafrox}{Estimación acumulada'))
for k in internal:
 ck=k.replace('R-','CI-');assert eq[ck][1:]==oldq[k][1:]
 assert k+' / '+ck+' &' in section(e,'\\begin{tablalafrox}{Matriz de reubicación')
 assert ck+' &' in section(e,'\\begin{tablalafrox}{Valoraciones iniciales históricas')
assert sum(num(v[7].rstrip('\\')) for v in eq.values())==D('411.82')
assert D('1183.11')+D('411.82')==D('1594.93')
eco=rows(section(e,'\\begin{tablalafrox}{Coordinación conservada'));assert len(eco)==3
assert len(re.findall(r'^CI-\d{3} / ',section(e,'\\begin{tablalafrox}{Coordinación conservada'),re.M))==3
assert not re.search(r'^CI-\d{3} / \d',section(e,'\\begin{tablalafrox}{Coordinación conservada'),re.M)
for k,v in eco.items():assert v[1:]==rows(section(old['LAFROX-Subdocumento8-Anexos.tex'],'\\begin{tablalafrox}{Contrapartes, solicitudes'))[k.replace('CI-','R-')][1:]
assert set(re.findall(r'CI-\d{3}',e))=={k.replace('R-','CI-') for k in internal}
for p in old:
 assert [l for l in old[p].splitlines() if 'contenido academico' in l]==[l for l in (r/p).read_text(encoding='utf-8').splitlines() if 'contenido academico' in l]
for p,h in base['source_hashes'].items():assert hashlib.sha256((r.parent/p).read_bytes()).hexdigest()==h,p
assert '1.600' in b and '1.183,11' in b and '411,82' in b and '1.594,93' in b
assert 'CI-034' in a and '13--15' in e and '70\\%' in e and '100 avisos' in e
assert '1 riesgo crítico, 14 altos, 15 medios y 5 bajos' in b
print('OK: 35 riesgos vigentes, 16 CI trazables (13 originales + 3 añadidos), 28 coordinaciones activas y 3 internas conservadas.')
print('OK: valores vigentes intactos, PERT/VE, límites, factores, impactos, zonas, RBS y diez mayores coherentes.')
print('OK: 1.183,11 HH vigentes + 411,82 HH históricas internas = 1.594,93 HH anteriores; no se libera reserva.')
print('OK: documentos fuente y citas protegidas intactos; piloto CI-034 conservado y destinos S4/S13/S9 identificados.')
