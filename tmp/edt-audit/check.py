import re,collections
from pathlib import Path

def rows_tex(folder):
 out=[]
 for p in Path(folder).glob('tab_*.tex'):
  for n,line in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
   m=re.match(r'\s*(\d+(?:\.\d+){2,3})\s*&',line)
   if m:out.append((m.group(1),str(p),n,line))
 return out

def rows_md(path):
 out=[]
 for n,line in enumerate(Path(path).read_text(encoding='utf-8').splitlines(),1):
  m=re.match(r'\s*\|\s*(\d+(?:\.\d+){2,3})\s*\|',line)
  if m:out.append((m.group(1),n,line))
 return out

tex=rows_tex('formulario-t14/tablas')
md=rows_md('tmp/edt-audit/LAFROX-Formulario-T-14.md')
tx=collections.defaultdict(list);mx=collections.defaultdict(list)
for code,path,n,line in tex:tx[code].append((path,n,line))
for code,n,line in md:mx[code].append((n,line))
print('T14 code rows tex',len(tex),'unique',len(tx),'MD rows',len(md),'unique',len(mx))
print('missing tex',sorted(mx.keys()-tx.keys()))
print('extra tex',sorted(tx.keys()-mx.keys()))
print('duplicate codes in tex',[(k,len(v)) for k,v in tx.items() if len(v)>1][:30])
print('T14 counts by phase',dict(sorted(collections.Counter(k[0] for k in tx).items())))
print('T14 empty essential cells',[(code,path,n) for code,path,n,line in tex if any(not x.strip() for x in line.split('&')[:6])][:30])
for code in sorted(mx.keys()&tx.keys()):
 a=mx[code][0][1].split('|')[1:-1]
 b=tx[code][0][2].rstrip('\\').split('&')
 if len(a)!=len(b):print('COLCOUNT',code,len(a),len(b))
 print('DIFF',code) if ('Seis pruebas' in b[2] and 'Siete pruebas' in a[2]) else None

for name in ('tab_T15_paquetes.tex','tab_T15_contingencia.tex'):
 p=Path('formulario-t15/tablas',name)
 if p.exists():
  lines=p.read_text(encoding='utf-8').splitlines()
  ids=[re.match(r'\s*(\d+(?:\.\d+){2,3})\s*&',s).group(1) for s in lines if re.match(r'\s*(\d+(?:\.\d+){2,3})\s*&',s)]
  print(name,'rows',len(ids),'unique',len(set(ids)))

for folder in ('subdocumento-07/tablas','subdocumento-07-anexos/tablas','formulario-t14/tablas','formulario-t15/tablas','formulario-t18/tablas'):
 print('\nTABLES',folder)
 for p in sorted(Path(folder).glob('tab_*.tex')):
  s=p.read_text(encoding='utf-8')
  m=re.search(r'\{\\cab\{[^\n]+',s)
  if not m:continue
  head=m.group(0)
  cols=head.count('\\cab{')
  print(p.name,cols,head[:170])
