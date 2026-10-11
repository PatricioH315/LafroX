import re,difflib
from pathlib import Path

def norm(s):
 s=s.lower().replace('\\ensuremath{\\times}','×').replace('\\ensuremath{\\leq}','≤').replace('\\ensuremath{\\div}','÷').replace('\\%','%')
 s=re.sub(r'\\(?:textbf|emph|allowbreak|texttt)\{([^{}]*)\}',r'\1',s)
 s=re.sub(r'\\[a-zA-Z]+\*?(?:\{[^{}]*\})?',' ',s)
 s=re.sub(r'[^\w\d]+',' ',s,flags=re.UNICODE)
 return ' '.join(s.split())
md={}
for n,s in enumerate(Path('tmp/edt-audit/LAFROX-Formulario-T-15.md').read_text(encoding='utf-8').splitlines(),1):
 m=re.match(r'^\s*\|\s*(\d+(?:\.\d+){2,3})\s*\|',s)
 if m:md.setdefault(m.group(1),[]).append((n,[x.strip() for x in s.split('|')[1:-1]]))
for file in ('tab_T15_2.tex','tab_T15_paquetes.tex','tab_T15_10.tex'):
 p=Path('formulario-t15/tablas',file)
 print('\n',file)
 matches=0;missing=[];diff=[]
 for n,s in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
  m=re.match(r'^\s*(\d+(?:\.\d+){2,3})\s*&',s)
  if not m:continue
  code=m.group(1);cells=[x.strip().rstrip('\\').strip() for x in s.split('&')]
  cands=[(mn,mc) for mn,mc in md.get(code,[]) if len(mc)==len(cells)]
  if not cands:missing.append((code,n,len(cells)));continue
  mn,mc=max(cands,key=lambda x:sum(difflib.SequenceMatcher(None,norm(a),norm(b)).ratio() for a,b in zip(x[1],cells)))
  matches+=1
  for col,(a,b) in enumerate(zip(mc,cells),1):
   ratio=difflib.SequenceMatcher(None,norm(a),norm(b)).ratio()
   if ratio<0.9:diff.append((code,n,mn,col,round(ratio,2),a[:100],b[:100]))
 print('matched',matches,'missing',len(missing),'diff cells',len(diff))
 for x in missing[:15]:print('MISSING',x)
 for x in diff[:50]:print('DIFF',x)
