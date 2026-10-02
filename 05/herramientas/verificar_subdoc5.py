"""Integridad documental, aritmética, referencias y QA de los dos PDFs."""
from pathlib import Path
import csv, hashlib, json, re, math
import pdfplumber, pypdfium2 as pdfium
from pypdf import PdfReader
from PIL import Image, ImageDraw
root=Path(__file__).resolve().parents[2];base=root/'05';errors=[]
def check(ok,msg):
    if not ok:errors.append(msg)
model=json.loads((base/'anexos/datos/fuentes/modelo.json').read_text(encoding='utf-8'))
calc=json.loads((base/'anexos/datos/fuentes/CALCULOS.json').read_text(encoding='utf-8'))
names=[e['nombre'] for e in model['entidades']]
check(len(names)==len(set(names)),'Entidades duplicadas')
for e in model['entidades']:
    keys=[a['nombre'] for a in e['atributos']]
    check(len(keys)==len(set(keys)),f"Atributos repetidos en {e['nombre']}")
    for a in e['atributos']:check(all(a.get(k) for k in ['nombre','tipo','valores','obligatorio','propietario','sensibilidad']),f"Atributo incompleto {e['nombre']}.{a.get('nombre')}")
for a,b,c,d,rule in model['relaciones']:check(a in names and b in names,f'Relación sin entidad {a}/{b}')
check(len(model['dominios'])==15,'Dominios distintos de arquitectura')
with (base/'formularios/trazabilidad/MATRIZ_RT05.csv').open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f))
check(len(rows)==30 and {r['requisito'] for r in rows}=={f'RT-05.{i:02}' for i in range(1,31)},'Cobertura RT-05')
for k,v in [('oltp_bytes_anual',50748600000),('pod_bytes_anual',87720000000),('migracion_bytes_destino',32109560000),('temperatura_curada_bytes_anual',140039550)]:check(math.isclose(calc[k],v),f'Cálculo {k}')
body='\n'.join(p.read_text(encoding='utf-8') for p in sorted((base/'partes').rglob('01_*.tex')))
sections=re.findall(r'\\section\{([^}]+)\}',body)
check(sections==['Modelo','Gestión de datos','Estrategia de migración','Estrategia de desempeño'],'Índice obligatorio')
for p in list(base.rglob('*.tex'))+[root/'main_subdocumento_5.tex',root/'contenido_subdocumento_5.tex']:
    s=p.read_text(encoding='utf-8')
    for inc in re.findall(r'\\input\{([^}]+)\}',s):check((root/inc).exists(),f'Include ausente {inc}')
    check(not re.search(r'\\n(?=\\)',s),f'Salto literal en {p.name}')
pdfs=[];qa=base/'salida/qa';qa.mkdir(parents=True,exist_ok=True)
for name in ['LAFROX-Subdocumento5','LAFROX-Subdocumento5-Anexos']:
    p=root/(name+'.pdf');check(p.exists(),f'PDF ausente {name}')
    if not p.exists():continue
    doc=pdfium.PdfDocument(p);texts=[page.extract_text() or '' for page in PdfReader(p).pages]
    check(all(t.strip() for t in texts),f'Página vacía {name}')
    check('??' not in '\n'.join(texts),f'Referencia no resuelta {name}')
    s=(base/'salida'/(name+'.log')).read_text(encoding='utf-8',errors='replace')
    warnings=re.findall(r'(?:Overfull[^\n]*|LaTeX Warning:[^\n]*|Missing character:[^\n]*)',s)
    check(not any('undefined' in w.lower() or 'Overfull' in w or 'Missing character' in w for w in warnings),f'Overflow/referencia/glifo en {name}')
    outside=[]
    with pdfplumber.open(p) as geometry:
        for i,page in enumerate(geometry.pages):
            for char in page.chars:
                if char['x0'] < -1 or char['top'] < -1 or char['x1']>page.width+1 or char['bottom']>page.height+1:outside.append(i+1)
    check(not outside,f'Texto fuera de página {name}')
    pdfs.append(dict(archivo=p.name,paginas=len(doc),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),advertencias=warnings,texto_fuera_pagina=outside))
    for start in range(0,len(doc),12):
        sheet=Image.new('RGB',(1800,1840),'#e6e6e6');draw=ImageDraw.Draw(sheet)
        for off in range(min(12,len(doc)-start)):
            im=doc[start+off].render(scale=.72).to_pil().convert('RGB');im.thumbnail((430,550))
            col=off%4;row=off//4;sheet.paste(im,(col*450+(450-im.width)//2,row*610+30));draw.text((col*450+12,row*610+8),str(start+off+1),fill='black')
        sheet.save(qa/f'{name}-contacto-{start//12+1:02}.png')
    selection={0,1,len(doc)-1}
    selection.update(i for i,t in enumerate(texts) if ('Figura 5.' in t or 'Tabla 5.' in t) if not name.endswith('-Anexos'))
    if name.endswith('-Anexos'):selection.update(i for i,t in enumerate(texts) if any(k in t for k in ['Anexo 5-B','Anexo 5-E','Anexo 5-H','dim_producto']))
    for i in sorted(selection):doc[i].render(scale=1.4).to_pil().save(qa/f'{name}-pagina-{i+1:03}.png')
report=dict(fecha='2026-10-02',rama='alvaro-modelo-y-gestion-de-datos',entidades=len(names),atributos=sum(len(e['atributos']) for e in model['entidades']),dominios=15,relaciones=len(model['relaciones']),requisitos=len(rows),estructura=sections,errores=errors,pdfs=pdfs,revision_visual='Por registrar tras inspección',ensayos_operacionales='No ejecutados; protocolos y criterios documentados')
(base/'formularios/trazabilidad/VERIFICACION.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2));raise SystemExit(bool(errors))
