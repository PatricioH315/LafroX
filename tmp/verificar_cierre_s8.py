from pathlib import Path
from decimal import Decimal as D, ROUND_HALF_UP
from collections import Counter
import re,json,hashlib
r=Path(__file__).resolve().parents[1]
base=json.loads((r/'tmp/cierre-s8-base.json').read_text(encoding='utf-8'));data=json.loads((r/'tmp/cierre-s8-datos.json').read_text(encoding='utf-8'));mp=data['mapping'];risks=data['risks']
texts={p:(r/p).read_text(encoding='utf-8') for p in base['original']}
b=texts['08_plan_riesgos/contenido.tex'];rb=texts['08_plan_riesgos/figuras/rbs.tex'];a=texts['LAFROX-Subdocumento8-Anexos.tex'];f=texts['LAFROX-Formulario-T-16.tex']
parts={x:(r/f'08_plan_riesgos/anexo-{x}-{name}.tex').read_text(encoding='utf-8') for x,name in [('e','controles'),('f','respuestas'),('g','fmea'),('h','reservas'),('i','trazabilidad')]}
def sec(s,needle):
 p=s.index(needle);return s[p:s.index('\\end{tablalafrox}',p)]
def rows(s):return {l.split(' & ')[0]:l.split(' & ') for l in s.splitlines() if re.match(r'R-\d{3} &',l)}
reg=rows(sec(f,'\\begin{tablalafrox}{Registro cualitativo'))
assert list(reg)==[f'R-{i:03}' for i in range(1,36)]
oldreg=rows(base['original']['LAFROX-Formulario-T-16.tex']);q=rows(sec(a,'\\begin{tablalafrox}{Estimación acumulada'));oldq=rows(sec(base['original']['LAFROX-Subdocumento8-Anexos.tex'],'\\begin{tablalafrox}{Estimación acumulada'))
imp=rows(sec(a,'\\begin{tablalafrox}{Fundamento del impacto'));oldimp=rows(sec(base['original']['LAFROX-Subdocumento8-Anexos.tex'],'\\begin{tablalafrox}{Fundamento del impacto'))
ar=rows(sec(a,'\\begin{tablalafrox}{Matriz de respuestas'))
assert set(reg)==set(q)==set(imp)==set(ar)==set(risks)
for old,new in mp.items():
 assert reg[new][1:6]==oldreg[old][1:6],new
 assert q[new][1:]==oldq[old][1:],new
 assert imp[new][1:]==oldimp[old][1:],new
assert set(re.findall(r'\\RBSrisk\{(R-\d{3})\}',rb))==set(reg)
assert len(re.findall(r'^R-\d{3} / [A-Z]+ &',a,re.M))==28
assert sum(map(int,re.findall(r'\{\\small (\d+) riesgos\}',rb)))==35
num=lambda x:D(x.replace(',','.'))
rn=lambda x:x.quantize(D('.01'),rounding=ROUND_HALF_UP)
fmt=lambda x:f'{rn(D(x)):.2f}'.replace('.',',')
pl=lambda p:1 if p<=10 else 2 if p<=30 else 3 if p<=50 else 4 if p<=70 else 5
weights=list(map(D,['.1','.3','.5','.7','.9']))
zn=lambda e:'Baja' if e<D('.08') else 'Media' if e<D('.20') else 'Alta' if e<D('.40') else 'Crítica'
assert [pl(D(x)) for x in ['0','10','10.01','30','50','70','70.01','100']]==[1,1,2,2,3,4,5,5]
assert [zn(D(x)) for x in ['.0799','.08','.1999','.20','.3999','.40']]==['Baja','Media','Media','Alta','Alta','Crítica']
fr=rows(sec(parts['f'],'\\begin{tablalafrox}{Fichas ejecutables'));rr=rows(sec(parts['f'],'\\begin{tablalafrox}{Riesgo residual proyectado'));cb=rows(sec(parts['f'],'\\begin{tablalafrox}{Costo-beneficio'));fm=rows(sec(parts['g'],'\\begin{tablalafrox}{FMEA de'))
post=rows(sec(f,'\\begin{tablalafrox}{Resumen de valoración posterior'))
assert set(fr)==set(rr)==set(post)==set(reg)
high={k for k,x in risks.items() if x['high']};assert len(high)==15 and set(cb)==set(fm)==high
tot0=D(0);ca=D(0);ce=D(0);cr=D(0);ct=D(0);zones=Counter()
for k,x in risks.items():
 p,pr,H,A,C,R,er,et,ben,net=map(D,[x[t] for t in ['p','pr','h','A','C','R','er','et','benef','net']]);qi=D(x['qi']);ex=weights[pl(pr)-1]*qi
 assert D(0)<=pr<=p<=100 and D(0)<=C<=H and R==H-C
 assert er==pr/100*R and et==A+pr/100*C
 assert abs(ben-(p/100*H-er))<D('1e-20') and abs(net-(ben-et))<D('1e-20')
 assert abs((et+er)-(A+pr/100*H))<D('1e-20')
 assert D(x['E'])==ex and x['zone']==zn(ex)
 assert x['I']==int(reg[k][4].split(' / ')[0])
 assert rr[k][1].startswith(fmt(pr)+'\\% / '+str(pl(pr))) and x['zone'] in rr[k][2]
 assert post[k][1]==fmt(pr)+'\\%' and post[k][3]==fmt(ex)+' / '+x['zone']
 assert x['owner'] in fr[k][3] and 'A:' in fr[k][3] and 'C:' in fr[k][3]
 assert any(y in fr[k][2] for y in ['min','día','turno','D-5','antes','mes','hora'])
 if ex>=D('.20'):assert 'Plan adicional:' in fr[k][2]
 if k in high:
  initial=re.search(r'S=(\d); O=(\d); D=(\d); NPR=(\d+)',fm[k][1]);postfm=re.search(r'S1=(\d); O1=(\d); D1=(\d); NPR1=(\d+)',fm[k][4]);assert initial and postfm
  S,O,Dt,N=map(int,initial.groups());s1,o1,d1,n1=map(int,postfm.groups());assert S==s1==x['I'] and O==pl(p) and o1==pl(pr) and N==S*O*Dt and n1==s1*o1*d1
  assert 'B/T='+fmt(D(x['ratio'])) in cb[k][2] and 'Sin mejora' in cb[k][3]
  if D(x['ratio'])<1:assert 'menor que uno' in cb[k][4]
 ca+=A;ce+=pr/100*H;cr+=er;ct+=et;tot0+=num(q[k][7].rstrip('\\'));zones[x['zone']]+=1
assert tot0==D('1183.11') and ca==D('180') and rn(ce)==D('821.13') and rn(cr)==D('683.93') and rn(ct)==D('317.20')
assert dict(zones)==data['reszones']=={'Media':19,'Crítica':1,'Baja':11,'Alta':4}
# Ranking y orden iniciales preservados con equivalencia.
for needle in ['\\begin{tablalafrox}{Diez mayores valores esperados','\\begin{tablalafrox}{Diez riesgos de mayor exposición']:
 assert list(rows(sec(b,needle)))==[mp[k] for k in rows(sec(base['original']['08_plan_riesgos/contenido.tex'],needle))]
eq=sec(parts['i'],'\\begin{tablalafrox}{Equivalencias completas')
assert len(re.findall(r'^Histórico R-\d{3} &',eq,re.M))==51
for k,v in mp.items():assert f'Histórico {k} & {v} &' in eq
assert len(re.findall(r'^CI-\d{3} &',parts['e'],re.M))==16
for k in data['internal']:assert f'Histórico {k} & '+k.replace('R-','CI-')+' &' in eq
assert len(re.findall(r'^\d{2} &',sec(parts['i'],'\\begin{tablalafrox}{Trazabilidad observación'),re.M))==14
monthly=sec(parts['h'],'\\begin{tablalafrox}{Distribución mensual');ml=[l.split(' & ') for l in monthly.splitlines() if re.match(r'\d+ &',l)];assert len(ml)==56
printed_total=D(0)
for vals in ml:
 v=[num(z.rstrip('\\').strip()) for z in vals[1:]];assert abs(sum(v[:-1])-v[-1])<=D('.04');printed_total+=v[-1]
assert abs(printed_total-ce)<=D('.30')
assert '4 por 40=160' in parts['h'] and '1.152' in parts['h'] and '1.920' in parts['h'] and '216.951' in parts['h'] and '220.023' in parts['h']
# No ID antiguo ambiguo fuera de tabla histórica/cita expresamente rotulada.
for path,s in list(texts.items())+list(parts.items()):
 for l in s.splitlines():
  for m in re.finditer(r'(?<![\w-])R-(\d{3})',l):
   if int(m[1])>35:assert 'Histórico' in l or 'histórico' in l,path+': '+l
for p,s in texts.items():assert [l for l in s.splitlines() if 'contenido academico' in l]==[l for l in base['original'][p].splitlines() if 'contenido academico' in l]
for p,h in base['sources'].items():assert hashlib.sha256((r.parent/p).read_bytes()).hexdigest()==h,p
print('OK: 35 ID consecutivos; equivalencia de 51 anteriores y 16 CI; 28 coordinaciones; valores iniciales y citas protegidas intactos.')
print('OK: 35 fichas/residuales; 15 FMEA/costo-beneficio; cálculos, sensibilidad y planes adicionales coherentes.')
print('OK: A=180,00; contingencia=821,13; residual=683,93; tratamiento=317,20; total posterior=1.001,13 HH, sin duplicar C.')
print('OK: gestión propuesta 160 HH; protección E1 separada; distribución 56 meses; 14 observaciones y documentos externos intactos.')
