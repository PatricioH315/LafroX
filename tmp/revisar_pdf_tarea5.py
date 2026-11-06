from pathlib import Path
from pypdf import PdfReader
from PIL import Image,ImageOps,ImageDraw
import subprocess,shutil,json
root=Path(__file__).resolve().parents[1]
build=root/'tmp/tarea5-build';qa=build/'qa-entrega';qa.mkdir(exist_ok=True)
report={}
for name in ['LAFROX-Subdocumento8','LAFROX-Subdocumento8-Anexos','LAFROX-Formulario-T-16']:
 pdf=build/(name+'.pdf');reader=PdfReader(pdf)
 texts=[p.extract_text() for p in reader.pages]
 report[name]={'pages':len(texts),'interesting':[]}
 for i,t in enumerate(texts):
  if any(s in t for s in ['Escalas previas','Banda de','PERT condicional (HH)','página 1 de 2','página 2 de 2','Fundamento del impacto','Respaldo de la valoración inicial','Dependencias y decisiones','Contrapartes, solicitudes','Dependencias del CLIENTE: compromisos','Trazabilidad con S4','Cruces verificados','Brechas de cobertura','Hipótesis de ocurrencia','Correspondencia de las omisiones']): report[name]['interesting'].append(i+1)
 subprocess.run([shutil.which('pdftoppm'),'-scale-to','650','-png',str(pdf),str(qa/name)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
 imgs=sorted(qa.glob(name+'-*.png'))
 # Exact name prefix prevents matching Annexes in the body list.
 imgs=[p for p in imgs if p.stem[len(name)+1:].isdigit()]
 for start in range(0,len(imgs),12):
  batch=imgs[start:start+12];sheet=Image.new('RGB',(1600,3*620),'#dddddd');draw=ImageDraw.Draw(sheet)
  for k,path in enumerate(batch):
   im=Image.open(path).convert('RGB');im.thumbnail((390,580));x=(k%4)*400+(400-im.width)//2;y=(k//4)*620+25
   sheet.paste(im,(x,y));draw.text(((k%4)*400+8,(k//4)*620+5),path.stem,fill='black')
  sheet.save(qa/(name+f'-contact-{start//12+1}.jpg'))
 print(name,len(texts),'pages; selected',report[name]['interesting'])
(qa/'report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
