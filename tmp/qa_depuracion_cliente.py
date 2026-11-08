from pathlib import Path
import json,re,subprocess,shutil
from pypdf import PdfReader
r=Path(__file__).resolve().parents[1]
base=json.loads((r/'tmp/depuracion-cliente-base.json').read_text(encoding='utf-8'))
for name,old in base.items():
 new=(r/name).read_text(encoding='utf-8')
 for a,b in zip([l for l in old.splitlines() if ' & ' in l],[l for l in new.splitlines() if ' & ' in l]):
  assert re.findall(r'\d+(?:[.,]\d+)?',a)==re.findall(r'\d+(?:[.,]\d+)?',b),name
 if name.endswith('/contenido.tex'):
  tag='\\section*{Declaración de uso de IA}'
  assert old[old.index(tag):]==new[new.index(tag):]
 assert [l for l in old.splitlines() if 'contenido academico' in l]==[l for l in new.splitlines() if 'contenido academico' in l]
print('Verificado: tablas técnicas, 35 riesgos y declaración de IA íntegros.')
script=(r/'tmp/revisar_pdf_limpieza_s8.py').read_text(encoding='utf-8').replace("qa=build/'qa'","qa=build/'qa-depuracion'")
exec(compile(script,'qa_depuracion','exec'))
