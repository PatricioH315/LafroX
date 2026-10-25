"""Recalcula el incremento de cadena de frío sobre las curvas publicadas del T-15.
Ejecutar desde cualquier carpeta con Python 3. Conserva la base de comparación,
calcula HH desde las filas vigentes y reserva refuerzo separado por rol.
"""
from pathlib import Path
from fractions import Fraction
from decimal import Decimal, ROUND_FLOOR, ROUND_HALF_UP
import json,re,math
ROOT=Path(__file__).resolve().parents[1]
BASE=json.loads(Path(__file__).with_name('cadena_frio_modelo_base.json').read_text(encoding='utf-8'))
ROLES=['JP','ARQ','SEG','DAT','DES','CAL','SRE','IMP']
def rows(s):return [l.strip().removesuffix('\\\\').strip().split(' & ') for l in s.splitlines() if re.match(r'^\s*\d+(?:\.\d+)*\s*&',l)]
def write_table(path,newrows):
 s=path.read_text(encoding='utf-8-sig');it=iter(newrows)
 ls=['  '+' & '.join(next(it))+r' \\' if re.match(r'^\s*\d+(?:\.\d+)*\s*&',l) else l for l in s.splitlines()]
 assert next(it,None) is None
 path.write_text('\n'.join(ls)+'\n',encoding='utf-8')
def allocation(row):
 a,b=map(int,row[3].split('–'));return {m:Fraction(row[7])/(b-a+1) for m in range(a,b+1)}
current={r[0]:r for r in rows((ROOT/'formulario-t15/tablas/tab_T15_2.tex').read_text(encoding='utf-8'))}
delta={(m,r):Fraction() for m in range(1,57) for r in ROLES}
changes=[]
for code,row in current.items():
 old=BASE['antes'].get(code)
 if old==row:continue
 changes.append(code)
 if old:
  for m,v in allocation(old).items():delta[m,old[2]]-=v
 for m,v in allocation(row).items():delta[m,row[2]]+=v
assert set(changes)=={'2.4.3','2.4.4','4.1.4','5.1.4','5.3.4','3.4.4','3.4.5','6.5.4','7.1.3','7.2.4'},changes
assert sum(delta.values())==2480
assert all(v>=0 for v in delta.values())
# La nueva carga queda en E1 desarrollo hasta 12, E1 MB 13–15, soporte 16–20.
values=[[Fraction(c) for c in r[1:8]] for r in BASE['curva_hh']]
for m in range(1,57):values[m-1][0 if m<=12 else 1 if m<=15 else 4 if m<=20 else 6]+=sum(delta[m,r] for r in ROLES)
# Mayor resto por etapa: la suma publicada de meses conserva las HH exactas.
rounded=[[0]*7 for _ in range(56)]
for col in range(7):
 raw=[values[m][col]*100 for m in range(56)];floors=[x.numerator//x.denominator for x in raw]
 total=sum(raw);target=int(Decimal(total.numerator)/Decimal(total.denominator)+Decimal('.5'))
 order=sorted(range(56),key=lambda m:raw[m]-floors[m],reverse=True)
 for m in order[:target-sum(floors)]:floors[m]+=1
 for m,v in enumerate(floors):rounded[m][col]=v
curves=[[str(m+1)]+[f'{v/100:.2f}' for v in r]+[f'{sum(r)/100:.2f}'] for m,r in enumerate(rounded)]
assert sum(sum(r) for r in rounded)==22002300
write_table(ROOT/'formulario-t15/tablas/tab_T15_4.tex',curves)
persons=[]
for row in BASE['curva_personas']:
 m=int(row[0]);nums=[int(row[j+1])+math.ceil(delta[m,r]/128) for j,r in enumerate(ROLES)]
 persons.append([str(m)]+list(map(str,nums))+[str(sum(nums))])
write_table(ROOT/'formulario-t15/tablas/tab_T15_4_personas.tex',persons)
# Resumen por etapa deriva de las columnas publicadas; reserva existente separada.
p=ROOT/'formulario-t15/tablas/tab_T15_3.tex';s=p.read_text(encoding='utf-8');ls=s.splitlines();idx=0
for n,l in enumerate(ls):
 if not re.match(r'^\s*(E1 |E2 |Operación|Cierre y)',l):continue
 c=l.strip().removesuffix('\\\\').strip().split(' & ');total=sum(r[idx] for r in rounded)/100
 c[1]=f'{total-float(c[2]):.2f}';c[3]=f'{total:.2f}';ls[n]='  '+' & '.join(c)+r' \\';idx+=1
assert idx==7
p.write_text('\n'.join(ls)+'\n',encoding='utf-8')
audit={'paquetes':len(current),'hh_paquetes':sum(float(r[7]) for r in current.values()),'incremento_hh':float(sum(delta.values())),'total_hh':220023,'peak_personas':max(int(r[-1]) for r in persons),'meses_peak':[int(r[0]) for r in persons if int(r[-1])==max(int(x[-1]) for x in persons)],'cambios':changes,'regla_refuerzo':BASE['regla_personas'],'delta_rol_mes':{f'{m}:{r}':float(v) for (m,r),v in delta.items() if v}}
Path(__file__).with_name('cadena_frio_recursos_verificacion.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in audit.items() if k!='delta_rol_mes'},ensure_ascii=False))
