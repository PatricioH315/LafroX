from pathlib import Path
from pypdf import PdfReader
import re,subprocess,shutil
r=Path(__file__).resolve().parents[1];b=r/'tmp/cierre-s8-build'
names=['LAFROX-Subdocumento8','LAFROX-Subdocumento8-Anexos','LAFROX-Formulario-T-16']
texts={n:[p.extract_text() for p in PdfReader(b/(n+'.pdf')).pages] for n in names}
expected={f'R-{i:03}' for i in range(1,36)}
f=texts[names[2]]
assert set(re.findall(r'R-\d{3}','\n'.join(f[5:17])))==expected
assert set(re.findall(r'R-\d{3}','\n'.join(f[17:20])))==expected
assert set(re.findall(r'R-\d{3}','\n'.join(texts[names[0]][10:12])))==expected
assert all('??' not in ''.join(v) for v in texts.values())
print('PDF: 35 ID iniciales, 35 posteriores y RBS completa; sin referencias ??')
print('Páginas:',{n:len(v) for n,v in texts.items()})
p=r/'odd/tasks/matriz-cierre-s8.md'
s=(r/'08_plan_riesgos/anexo-i-trazabilidad.tex').read_text(encoding='utf-8')
start=s.index('\\begin{tablalafrox}{Trazabilidad observación');end=s.index('\\end{tablalafrox}',start)
lines=[l.split(' & ') for l in s[start:end].splitlines() if len(l)>3 and l[:2].isdigit()]
s='# Matriz de observaciones de S8\n\nCopia de consulta de la Tabla 8.I.1. La ubicación y equivalencia oficiales están en el PDF de anexos. Los estados parciales o de integración externa no representan cumplimiento total.\n\n| Obs. | Pedido y fuente | Respuesta | Ubicación | Estado |\n|---|---|---|---|---|\n'+'\n'.join('| '+' | '.join(c.replace(chr(92)+chr(92),'').strip() for c in line)+' |' for line in lines)+'\n'
s=s.replace(chr(96)*2,chr(8220)).replace(chr(39)*2,chr(8221))
p.write_text(s,encoding='utf-8')
for i in [113,114]:
 subprocess.run([shutil.which('pdftoppm'),'-f',str(i),'-l',str(i),'-scale-to','1800','-png',str(b/(names[1]+'.pdf')),str(b/'qa-final'/'matriz-final')],check=True)
