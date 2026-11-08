from pathlib import Path
from pypdf import PdfReader
import subprocess,shutil,hashlib,json
root=Path(__file__).resolve().parents[1];build=root/'tmp/limpieza-s8-build';qa=build/'qa'
for name,pages in [('LAFROX-Subdocumento8',[8,11,12]),('LAFROX-Subdocumento8-Anexos',[39,44,97]),('LAFROX-Formulario-T-16',[18])]:
 for page in pages:
  subprocess.run([shutil.which('pdftoppm'),'-f',str(page),'-l',str(page),'-scale-to','1500','-singlefile','-png',str(build/(name+'.pdf')),str(qa/(name+f'-detalle-{page}'))],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
print('Detalles visuales generados.')
