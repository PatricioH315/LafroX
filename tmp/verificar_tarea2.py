from pathlib import Path
from decimal import Decimal as D
from collections import Counter
import json,re
root=Path(__file__).resolve().parents[1]
snap=json.loads((root/'tmp/tarea2-baseline.json').read_text(encoding='utf-8'))
a=(root/'LAFROX-Subdocumento8-Anexos.tex').read_text(encoding='utf-8')
b=(root/'08_plan_riesgos/contenido.tex').read_text(encoding='utf-8')
t=(root/'LAFROX-Formulario-T-16.tex').read_text(encoding='utf-8')
r=(root/'08_plan_riesgos/figuras/rbs.tex').read_text(encoding='utf-8')
assert snap['quantitative_rows']==[l for l in a.splitlines() if re.match(r'R-\d{3} &',l) and r'\%' in l and len(l.split(' & '))==8]
for path,lines in snap['protected'].items():
 assert lines==[l for l in (root/path).read_text(encoding='utf-8').splitlines() if 'contenido academico' in l],path
def pn(p): return 1 if p<=10 else 2 if p<=30 else 3 if p<=50 else 4 if p<=70 else 5
def zn(e): return 'Baja' if e<D('.08') else 'Media' if e<D('.20') else 'Alta' if e<D('.40') else 'Crítica'
for x,y in [('0',1),('10',1),('10.01',2),('30',2),('30.01',3),('50',3),('50.01',4),('70',4),('70.01',5),('100',5)]: assert pn(D(x))==y
for x,y in [('.0799','Baja'),('.08','Media'),('.1999','Media'),('.20','Alta'),('.3999','Alta'),('.40','Crítica')]: assert zn(D(x))==y
num=lambda x:D(x.replace(',','.'))
ids=[];zones=Counter();evaluated={}
for line in t.splitlines():
 if not re.match(r'R-\d{3} &',line):continue
 c=line.split(' & ');rid=c[0];ids.append(rid)
 pl,q=c[3].split(' / ');il,qi=c[4].split(' / ')
 quant=next(l for l in snap['quantitative_rows'] if l.startswith(rid+' &')).split(' & ')
 assert int(pl)==pn(int(quant[1].split('\\')[0]))
 assert num(q)==[D('.1'),D('.3'),D('.5'),D('.7'),D('.9')][int(pl)-1]
 assert num(qi)==[D('.05'),D('.1'),D('.2'),D('.4'),D('.8')][int(il)-1]
 e,z=re.match(r'([\d,]+) \((.+)\)',c[5]).groups();assert num(e)==num(q)*num(qi);assert z==zn(num(e))
 assert re.search(r'\\RBSrisk\{'+rid+r'\}\{[^\n]+\}\{'+z+r'\}',r)
 support=[l for l in a.splitlines() if l.startswith(rid+' &')][-1].split(' & ')
 h,ih=support[1].split(' / ');dh,final=support[2].split(' / ')
 assert int(final)==int(il)==max(int(ih),int(dh));assert num(h)==num(quant[6]);assert num(support[3])==num(qi)
 hh=num(h);assert int(ih)==(1 if hh<=24 else 2 if hh<=80 else 3 if hh<=160 else 4 if hh<=320 else 5)
 zones[z]+=1;evaluated[rid]=num(e)
assert ids==[f'R-{i:03}' for i in range(1,41)]
section=b[b.index('\\begin{tablalafrox}{Diez riesgos'):b.index('\\subsection{Análisis cuantitativo}')]
top=re.findall(r'^(R-\d{3}) &',section,re.M)
assert top==sorted(evaluated,key=lambda k:(-evaluated[k],k))[:10]
for bad in ['se conserva sin reclasificar','no se infiere a partir de umbrales','Estas bandas no se aplican'] : assert bad not in b
print('OK: 40 registros, P/factores/impactos/exposición/zonas/RBS/respaldo, top 10 y límites.')
print('OK: filas cuantitativas y citas protegidas intactas. Zonas:',dict(zones))
