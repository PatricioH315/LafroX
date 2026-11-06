from pathlib import Path
from decimal import Decimal as D,ROUND_HALF_UP
from collections import Counter
import re,json,hashlib
r=Path(__file__).resolve().parents[1]
baseline=json.loads((r/'tmp/tarea5-baseline.json').read_text(encoding='utf-8'))
old=baseline['original'];texts={p:(r/p).read_text(encoding='utf-8') for p in old}
f=texts['LAFROX-Formulario-T-16.tex'];a=texts['LAFROX-Subdocumento8-Anexos.tex'];b=texts['08_plan_riesgos/contenido.tex'];rb=texts['08_plan_riesgos/figuras/rbs.tex']
num=lambda x:D(x.replace(',','.'))
fmt=lambda x:f'{x:.2f}'.replace('.',',')
round2=lambda x:x.quantize(D('.01'),rounding=ROUND_HALF_UP)
def section(s,needle):
 start=s.index(needle);return s[start:s.index('\\end{tablalafrox}',start)]
def rows(s):return [l.split(' & ') for l in s.splitlines() if re.match(r'R-\d{3}(?: / [A-Z]+)? &',l)]
reg={c[0]:c for c in rows(f)}
assert list(reg)==[f'R-{i:03}' for i in range(1,52)]
orig={c[0]:c for c in rows(old['LAFROX-Formulario-T-16.tex'])}
for rid,c in orig.items():
 if rid not in {'R-016','R-019'}:assert c==reg[rid],rid
assert len(rows(section(a,'\\begin{tablalafrox}{Matriz de respuestas')))==51
responses={c[0]:c for c in rows(section(a,'\\begin{tablalafrox}{Matriz de respuestas'))}
deps=rows(section(a,'\\begin{tablalafrox}{Contrapartes, solicitudes'))
assert len(deps)==31 and len({c[0] for c in deps})==31
q={c[0]:c for c in rows(section(a,'\\begin{tablalafrox}{Estimación acumulada'))}
imp={c[0]:c for c in rows(section(a,'\\begin{tablalafrox}{Fundamento del impacto inicial'))}
assert set(q)==set(imp)==set(reg)
oldq={c[0]:c for c in rows(section(old['LAFROX-Subdocumento8-Anexos.tex'],'\\begin{tablalafrox}{Estimación acumulada'))}
for rid,c in oldq.items():
 if rid!='R-019':assert c==q[rid],rid
pf=[D('.1'),D('.3'),D('.5'),D('.7'),D('.9')];ifs=[D('.05'),D('.1'),D('.2'),D('.4'),D('.8')]
def plevel(p):return 1 if p<=10 else 2 if p<=30 else 3 if p<=50 else 4 if p<=70 else 5
def hlevel(h):return 1 if h<=24 else 2 if h<=80 else 3 if h<=160 else 4 if h<=320 else 5
def zn(e):return 'Baja' if e<D('.08') else 'Media' if e<D('.2') else 'Alta' if e<D('.4') else 'Crítica'
realh={};realve={};exp={};zones=Counter()
for rid,c in reg.items():
 p=int(q[rid][1].split('\\')[0]);o,m,ps=map(num,q[rid][3:6]);h=(o+4*m+ps)/6;v=D(p)/100*h;realh[rid]=h;realve[rid]=v
 assert 0<=p<=100 and o<=m<=ps and int(q[rid][2])>=1
 assert num(q[rid][6])==round2(h)
 assert num(q[rid][7].rstrip('\\'))==round2(v)
 pn,qp=c[3].split(' / ');il,qi=c[4].split(' / ')
 assert int(pn)==plevel(p) and num(qp)==pf[int(pn)-1] and num(qi)==ifs[int(il)-1]
 ihh=hlevel(h);hc,hn=imp[rid][1].split(' / ');dn,fin=imp[rid][2].split(' / ')
 assert num(hc)==round2(h) and int(hn)==ihh
 assert int(fin)==int(il)==max(ihh,int(dn)) and num(imp[rid][3])==num(qi)
 e,z=re.match(r'([\d,]+) \(([^)]+)\)',c[5]).groups();e=num(e)
 assert e==num(qp)*num(qi) and z==zn(e);exp[rid]=e;zones[z]+=1
 assert re.search(r'\\RBSrisk\{'+rid+r'\}\{[^\n]+\}\{'+z+r'\}',rb),rid
 if rid in {f'R-{i:03}' for i in range(41,52)}:
  assert responses[rid][2]==c[6]+' Evidencia y coordinación: Tabla 8.A.2.'
  assert responses[rid][3].rstrip('\\').strip()==c[7].rstrip('\\').strip()
  assert any(x[0].startswith(rid+' / ') for x in deps)
total=sum(map(round2,realve.values()),D(0));topq=sorted(realve,key=lambda k:(-realve[k],k))[:10];topqsum=sum((round2(realve[k]) for k in topq),D(0))
assert total==D('1594.93') and topqsum==D('739.40')
assert fmt(total) in section(a,'\\begin{tablalafrox}{Estimación acumulada')
assert [c[0] for c in rows(section(b,'\\begin{tablalafrox}{Diez mayores valores esperados'))]==topq
assert [c[0] for c in rows(section(b,'\\begin{tablalafrox}{Diez riesgos de mayor exposición'))]==sorted(exp,key=lambda k:(-exp[k],k))[:10]
assert dict(zones)=={'Alta':20,'Crítica':3,'Media':21,'Baja':7}
assert len(re.findall(r'\\RBSrisk\{R-\d{3}\}',rb))==51
assert sum(map(int,re.findall(r'\{\\small (\d+) riesgos\}',rb)))==51
ledger=section(a,'\\begin{tablalafrox}{Hipótesis de ocurrencia')
assert len(re.findall(r'^R-\d{3} / \d+\\% / \d+ &',ledger,re.M))==11
for p in old:
 assert [l for l in old[p].splitlines() if 'contenido academico' in l]==[l for l in texts[p].splitlines() if 'contenido academico' in l],p
for gap,rid in [('B-S4-01','R-048'),('B-S4-02','R-049'),('B-S4-03','R-050'),('B-S7-01','R-042')]:assert gap+' / '+rid+' &' in a
for bad in ['40 riesgos','40 eventos','40 registros','las 31 riesgos','cuatro brechas aún no incorporadas','sin valoración ni incorporación anticipada']:assert bad not in a+b+f,bad
assert '1.600' in b and '1.594,93' in b and '46,4' in b
for p,h in baseline['source_hashes'].items():assert hashlib.sha256((r.parent/'Informe propuesta tecnica/Informe_2_LafroX'/p).read_bytes()).hexdigest()==h,p
print('OK: 51 registros, respuestas, cuantificaciones, impactos y RBS; 31 coordinaciones completas; 11 hipótesis explícitas.')
print('OK: PERT/VE, bandas, factores, exposición, zonas y dos top 10; total 1.594,93 HH y top 739,40 HH (46,4 %).')
print('OK: cuatro brechas incorporadas, originales conservados salvo R-016/R-019; citas protegidas y documentos fuente intactos.')
