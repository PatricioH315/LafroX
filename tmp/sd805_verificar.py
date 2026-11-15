from pathlib import Path
import json, re, xml.etree.ElementTree as ET
from decimal import Decimal as D, ROUND_HALF_UP
from collections import defaultdict, Counter

r=Path(__file__).resolve().parents[1]
read=lambda p:(r/p).read_text(encoding='utf-8')
def table(s,label):
    m=re.search(r'\\begin\{tablalafrox\}[^\n]*\{'+re.escape(label)+r'\}',s)
    return s[m.start():s.index('\\end{tablalafrox}',m.start())]
def rows(s,label):
    return {l.split(' & ')[0]:l.rstrip('\\ ').split(' & ') for l in table(s,label).splitlines() if re.match(r'R-\d{3}',l)}
num=lambda s:D(s.replace(',','.'))
fmt=lambda x:x.quantize(D('.01'),rounding=ROUND_HALF_UP)
base=json.loads(read('tmp/sd805-base.json'))
for p in ['LAFROX-Subdocumento8-Anexos.tex','LAFROX-Formulario-T-16.tex','08_plan_riesgos/anexo-f-respuestas.tex']:
    old=[l for l in base[p].splitlines() if re.match(r'R-\d{3}( /[^&]*)? &',l)]
    new=[l for l in read(p).splitlines() if re.match(r'R-\d{3}( /[^&]*)? &',l) and not l.startswith('R-036')]
    assert old==new, p
print('Filas de R-001 a R-035 intactas, incluidos cambios de SD8-04.')
a=read('LAFROX-Subdocumento8-Anexos.tex'); f=read('08_plan_riesgos/anexo-f-respuestas.tex'); t=read('LAFROX-Formulario-T-16.tex')
ids={f'R-{i:03}' for i in range(1,37)}
q=rows(a,'tab:sd8-anexo-b-pert'); residual=rows(f,'tab:cierre-residual'); fichas=rows(f,'tab:cierre-fichas')
for s,label in [(a,'tab:sd8-anexo-a-respuestas'),(a,'tab:sd8-anexo-b-pert'),(a,'tab:sd8-impactos-respaldo'),(f,'tab:cierre-fichas'),(f,'tab:cierre-residual'),(t,'tab:t16-residual')]:
    assert set(rows(s,label))==ids,label
assert len(rows(a,'tab:sd8-dependencias-cliente'))==29
assert len(rows(read('08_plan_riesgos/anexo-g-fmea.tex'),'tab:cierre-fmea'))==15
assert len([l for l in table(a,'tab:sd805-cobertura').splitlines() if 'Estado: cobertura documentada; eficacia pendiente.' in l])==10
assert set(q)==ids and set(residual)==ids
monthly=defaultdict(lambda:defaultdict(D))
initial=cont=remanente=response=prevent=D(0)
for rid,cell in q.items():
    p=num(cell[1].replace('\\%',''))/100
    o,m,pe=map(num,cell[3:6]); hh=(o+4*m+pe)/6
    assert fmt(hh)==num(cell[6]),rid
    assert fmt(p*hh)==num(cell[7]),rid
    pr=num(residual[rid][1].split('\\%')[0])/100
    detail=fichas[rid][3]
    profiles=re.match(r'(\w+) / (\w+); A: ([\d,]+)/([\d,]+); C: ([\d,]+)/([\d,]+) HH',detail)
    assert profiles,(rid,detail)
    groups=profiles.groups()
    owner,support=groups[:2]; aa=sum(map(num,groups[2:4])); cc=sum(map(num,groups[4:6]))
    assert cc<=hh,rid
    window=re.search(r'Ventana de programación (\d+)--(\d+)',fichas[rid][4]); first,last=map(int,window.groups())
    for month in range(first,last+1):
        for role,share in [(owner,D('.6')),(support,D('.4'))]: monthly[month][role]+=pr*hh*share/(last-first+1)
    initial+=p*hh;cont+=pr*hh;remanente+=pr*(hh-cc);response+=pr*cc;prevent+=aa
assert [fmt(v) for v in [initial,cont,remanente,response,prevent,prevent+cont]]==list(map(D,['1199.52','837.53','695.53','142.00','180.00','1017.53']))
h=read('08_plan_riesgos/anexo-h-reservas.tex')
block=table(h,'tab:cierre-mensual')
monthrows=[l for l in block.splitlines() if re.match(r'\d+ &',l)]
assert len(monthrows)==56
for line in monthrows:
    cells=line.rstrip('\\ ').split(' & '); month=int(cells[0])
    expected=[monthly[month][role] for role in ['JP','ARQ','DAT','CAL','SRE','IMP','SEG']]
    assert list(map(num,cells[1:]))==[fmt(x) for x in expected+[sum(expected)]],month
assert abs(sum(sum(x.values()) for x in monthly.values())-cont)<D('.00000001')
assert 'Total VE} & & 1199,52' in a
assert a.index('R-036 & 30\\%')<a.index('Total VE')
print('PERT, reservas y 56 meses/perfiles conciliados sin redondeo intermedio.')
tree=ET.parse(r/'08_plan_riesgos/figuras/LafroX_RBS_36_riesgos_S8_v4.drawio')
nodes=[c for c in tree.iter('mxCell') if re.match(r'n[1-6]\.\d+$',c.get('id',''))]
assert len(nodes)==36
assert {re.search(r'R-\d{3}',c.get('value'))[0] for c in nodes}==ids
assert Counter(c.get('id').split('.')[0] for c in nodes)==dict(n1=3,n2=6,n3=14,n4=8,n5=3,n6=2)
print('RBS: 36 riesgos únicos en seis ramas; cobertura de los diez temas completa en S8.')
