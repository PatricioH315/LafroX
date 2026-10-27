"""Renderiza todas las páginas para QA y registra diagnósticos de compilación.

Las imágenes de inspección se guardan en TEMP. No modifica los PDF.
"""
from pathlib import Path
import hashlib, json, os, re
import pypdfium2 as pdfium
from pypdf import PdfReader
from PIL import Image, ImageDraw

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
TEMP=Path(os.environ['TEMP'])/'lafrox-frenteB-qa'
TEMP.mkdir(exist_ok=True)
names=['LAFROX-Subdocumento7','LAFROX-Subdocumento7-Anexos','LAFROX-Formulario-T-14',
       'LAFROX-Formulario-T-15','LAFROX-Formulario-T-18']
results=[]
for name in names:
    p=ROOT/(name+'.pdf');reader=PdfReader(p);doc=pdfium.PdfDocument(str(p))
    log=(ROOT/(name+'.log')).read_text(encoding='utf-8',errors='replace')
    assert 'Output written on' in log
    undefined=re.findall(r'[^\n]*(?:undefined|Missing character|Rerun to get|Label\(s\) may have changed)[^\n]*',log)
    assert not undefined, (name,undefined)
    fatal=re.findall(r'^![^\n]*',log,re.M)
    assert not fatal,(name,fatal)
    overfull=re.findall(r'Overfull[^\n]*',log)
    assert not overfull,(name,overfull)
    sheets=[];detail=[]
    keywords = ['Secuencia de cierre, producción y aceptación','Resumen T-15',
       '1.049,60','Niveles de reversión','Puertas de calidad automáticas',
       'Diccionario de la cuenta 4.2','Diccionario de la cuenta 4.3',
       'Secuencia de demostración de recuperación','Revisión del frente B',
       'Etapa 1 (H7)','implementación (H12)']
    for start in range(0,len(doc),24):
        sheet=Image.new('RGB',(1000,6*350),'#d0d0d0');draw=ImageDraw.Draw(sheet)
        for i in range(start,min(start+24,len(doc))):
            page=doc[i];pic=page.render(scale=.5).to_pil();pic.thumbnail((240,325))
            x=((i-start)%4)*250+(250-pic.width)//2;y=((i-start)//4)*350+20
            sheet.paste(pic,(x,y));draw.text((x,y-17),f'{i+1}',fill='black')
        dest=TEMP/f'{name}-sheet-{start+1:03}.jpg';sheet.save(dest,quality=88);sheets.append(str(dest))
    for i,page in enumerate(reader.pages):
        text=page.extract_text() or ''
        if i==0 or any(k in text for k in keywords):
            dest=TEMP/f'{name}-detail-{i+1:03}.png'
            doc[i].render(scale=1.45).to_pil().save(dest);detail.append({'pagina':i+1,'imagen':str(dest)})
    results.append({'documento':name,'paginas':len(reader.pages),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
      'errores_fatales':fatal,'referencias_pendientes':undefined,'overfull':overfull,
      'advertencias':[s for s in re.findall(r'(?:LaTeX Warning:|Package [^\n]* Warning:)[^\n]*',log)],
      'avisos_heredados_glue':log.count('Infinite glue shrinkage'),'hojas_inspeccion':sheets,'detalles':detail})
    doc.close()

# Los 17 detalles de fase, por sí solos, cubren los 227 paquetes de T14.
all_codes=set();diagrams=[]
for p in (ROOT/'imagenes/Imagenes de la edt').glob('EDT-Fase*.pdf'):
    text='\n'.join(page.extract_text() or '' for page in PdfReader(p).pages)
    codes=set(re.findall(r'(?<![\d.])\d+(?:\.\d+){2,3}(?![\d.])',text));all_codes |= codes
    diagrams.append({'archivo':str(p.relative_to(ROOT)),'codigos':len(codes)})
expected=set(re.findall(r'^\s*(\d+(?:\.\d+)+)\s*&',(ROOT/'formulario-t15/tablas/tab_T15_2.tex').read_text(encoding='utf-8'),re.M))
assert len(diagrams)==17 and not expected-all_codes,(len(diagrams),sorted(expected-all_codes))
sd7=(ROOT/'subdocumento-07/contenido.tex').read_text(encoding='utf-8')
labels=re.findall(r'\{(fig:7-edt-fase-[^}]+)\}',sd7)
assert len(set(labels))==17
assert all(sd7.find('\\ref{'+lab+'}') < sd7.find('{'+lab+'}',sd7.find('\\figuraEDT',sd7.find('\\ref{'+lab+'}'))) for lab in set(labels))
out={'documentos':results,'paginas_totales':sum(r['paginas'] for r in results),
     'laminas_EDT':diagrams,'paquetes_EDT_cubiertos':len(expected),'paquetes_EDT_ausentes':sorted(expected-all_codes),
     'inspeccion_visual':'Imágenes generadas; registrar inspección humana/asistente en VALIDACION_FINAL.md'}
(OUT/'K6_QA_PDF.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'paginas':out['paginas_totales'],'documentos':[{k:r[k] for k in ['documento','paginas','avisos_heredados_glue','advertencias']} for r in results],
                  'EDT':len(diagrams),'paquetes_EDT':len(expected),'carpeta_QA':str(TEMP)},ensure_ascii=False,indent=2))
