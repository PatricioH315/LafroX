import re,difflib
from pathlib import Path

def norm(s):
 s=s.lower().replace('\\ensuremath{\\times}','×').replace('\\ensuremath{\\leq}','≤').replace('\\ensuremath{\\div}','÷').replace('\\%','%')
 s=re.sub(r'\\(?:textbf|emph|allowbreak|texttt)\{([^{}]*)\}',r'\1',s)
 s=re.sub(r'\\[a-zA-Z]+\*?(?:\{[^{}]*\})?',' ',s)
 s=re.sub(r'[^\w\d]+',' ',s,flags=re.UNICODE)
 return ' '.join(s.split())
md={}
for n,s in enumerate(Path('tmp/edt-audit/LAFROX-Formulario-T-14.md').read_text(encoding='utf-8').splitlines(),1):
 m=re.match(r'^\s*\|\s*(\d+(?:\.\d+){2,3})\s*\|',s)
 if m:md[m.group(1)]=(n,[x.strip() for x in s.split('|')[1:-1]])
for p in Path('formulario-t14/tablas').glob('tab_*.tex'):
 for n,s in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
  m=re.match(r'^\s*(\d+(?:\.\d+){2,3})\s*&',s)
  if not m:continue
  code=m.group(1);cells=[x.strip().rstrip('\\').strip() for x in s.split('&')]
  mn,mc=md[code]
  if len(cells)!=len(mc):print('COLUMN_COUNT',code,p.name,n,len(cells),len(mc));continue
  for col,(a,b) in enumerate(zip(mc,cells),1):
   ratio=difflib.SequenceMatcher(None,norm(a),norm(b)).ratio()
   if ratio<0.9:
    print(f'{code}\t{p.name}:{n}\tMD:{mn}\tcol:{col}\t{ratio:.2f}\tMD={a[:125]}\tTEX={b[:125]}')
