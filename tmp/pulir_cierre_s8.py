from pathlib import Path
r=Path(__file__).resolve().parents[1]
p=r/'08_plan_riesgos/anexo-i-trazabilidad.tex';lines=p.read_text(encoding='utf-8').splitlines()
for i,l in enumerate(lines):
 if l[:2].isdigit() and ' & ' in l:
  cells=l.split(' & ')
  if cells[1].startswith('``') and "''" not in cells[1]:cells[1]=cells[1].replace(' (p.',"'' (p.",1)
  lines[i]=' & '.join(cells)
p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
p=r/'08_plan_riesgos/contenido.tex';s=p.read_text(encoding='utf-8').replace('\\paragraph{Análisis de modos de falla.}','\\paragraph{Análisis de modos de falla}');p.write_text(s,encoding='utf-8')
