from pathlib import Path
from pypdf import PdfReader
from PIL import Image,ImageDraw
import subprocess,shutil,json,re
root=Path(__file__).resolve().parents[1]
build=root/'tmp/limpieza-s8-build';qa=build/'qa';qa.mkdir(exist_ok=True)
report={}
for name in ['LAFROX-Subdocumento8','LAFROX-Subdocumento8-Anexos','LAFROX-Formulario-T-16']:
 pdf=build/(name+'.pdf');reader=PdfReader(pdf)
 texts=[p.extract_text() for p in reader.pages]
 whole='\n'.join(texts)
 assert not re.search(r'CI-\d|8\.I\.[12]|411,82|1\.594,93|1\.600|Informe 2|renumer|sincronización externa|asuntos retirados',whole),name
 assert '??' not in whole,name
 report[name]={'pages':len(texts),'selected':[]}
 for i,t in enumerate(texts):
  if any(s in t for s in ['Dependencias operativas','Controles técnicos','Reservas, perfiles','8.D.1','8.E.1','8.H.1','T-16.2','página 1 de 2','página 2 de 2']):report[name]['selected'].append(i+1)
 subprocess.run([shutil.which('pdftoppm'),'-scale-to','650','-png',str(pdf),str(qa/name)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
 imgs=[p for p in sorted(qa.glob(name+'-*.png')) if p.stem[len(name)+1:].isdigit()]
 for start in range(0,len(imgs),12):
  sheet=Image.new('RGB',(1600,1860),'#dddddd');draw=ImageDraw.Draw(sheet)
  for k,path in enumerate(imgs[start:start+12]):
   im=Image.open(path).convert('RGB');im.thumbnail((390,580));x=k%4*400+(400-im.width)//2;y=k//4*620+25
   sheet.paste(im,(x,y));draw.text((k%4*400+8,k//4*620+5),path.stem,fill='black')
  sheet.save(qa/(name+f'-contact-{start//12+1}.jpg'))
 print(name,len(texts),'pages; selected',report[name]['selected'])
(qa/'report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
