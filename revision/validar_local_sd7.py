"""Valida la edición local sin sobrescribir las evidencias históricas K4/K6."""
from pathlib import Path
from collections import Counter
from decimal import Decimal
import hashlib,json,re,shutil,subprocess,sys
from pypdf import PdfReader
import pypdfium2 as pdfium
from PIL import Image,ImageDraw

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'revision/local-20261105'
TMP=ROOT/'tmp/pdfs/local-20261105'
DOCS=['LAFROX-Subdocumento7','LAFROX-Subdocumento7-Anexos','LAFROX-Formulario-T-14','LAFROX-Formulario-T-15','LAFROX-Formulario-T-18']

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def guard():
    branch=subprocess.check_output(['git','branch','--show-current'],cwd=ROOT,text=True).strip()
    assert branch=='LafroX-Subdoc7-LateX-CORRIGIENDO',branch
def rows(p):
    return [[c.strip() for c in l.strip().removesuffix('\\\\').split(' & ')]
            for l in p.read_text(encoding='utf-8').splitlines() if re.match(r'^\s*\d+(?:\.\d+)*\s*&',l)]

def checks():
    guard();base=json.loads((OUT/'BASE_INICIAL.json').read_text(encoding='utf-8'))
    unchanged={name:sha(ROOT/name)==digest for name,digest in base['invariantes'].items()}
    assert all(unchanged.values()),unchanged
    eff=rows(ROOT/'formulario-t15/tablas/tab_T15_2.tex');dates=rows(ROOT/'formulario-t15/tablas/tab_T15_paquetes.tex')
    hours=rows(ROOT/'formulario-t15/tablas/tab_T15_4.tex');people=rows(ROOT/'formulario-t15/tablas/tab_T15_4_personas.tex')
    codes=[]
    for p in (ROOT/'formulario-t14/tablas').glob('*.tex'):
        codes += [r[0] for r in rows(p) if len(r)==6 and re.fullmatch(r'\d+(?:\.\d+){2,3}',r[0])]
    assert len(codes)==len(eff)==227 and set(codes)=={r[0] for r in eff}
    assert len(dates)==168 and len(hours)==len(people)==56
    assert sum(Decimal(r[7]) for r in eff)==Decimal('207487')
    assert sum(Decimal(r[8]) for r in hours)==Decimal('220023')
    assert all(sum(map(Decimal,r[1:8]))==Decimal(r[8]) for r in hours)
    assert all(sum(map(int,r[1:9]))==int(r[9]) for r in people)
    assert max(int(r[9]) for r in people)==64
    edt=json.loads((OUT/'EDT_VECTOR.json').read_text(encoding='utf-8'))
    graphic_files=[]
    for diagram in edt['laminas']:
        text='\n'.join(pg.extract_text() or '' for i in range(1,diagram['paginas']+1)
                       for pg in PdfReader(ROOT/'imagenes/Diagramas que faltaban/Revision-local'/f'{diagram["salida"]}-{i}.pdf').pages)
        found=set(re.findall(r'(?<![\d.])\d+(?:\.\d+){1,3}(?![\d.])',text))
        assert set(diagram['codigos'])<=found,(diagram['salida'],set(diagram['codigos'])-found)
        graphic_files += [ROOT/'imagenes/Diagramas que faltaban/Revision-local'/f'{diagram["salida"]}-{i}.pdf' for i in range(1,diagram['paginas']+1)]
    full_files=[ROOT/'imagenes/Diagramas que faltaban/Revision-local'/f'EDT-completa-{i}.pdf' for i in range(1,edt['paginas_vista_completa']+1)]
    full_text='\n'.join(pg.extract_text() or '' for p in full_files for pg in PdfReader(p).pages)
    assert {r[0] for r in eff}<=set(re.findall(r'(?<![\d.])\d+(?:\.\d+){2,3}(?![\d.])',full_text))
    graphic_files+=full_files
    gantt=json.loads((OUT/'GANTT_VECTOR.json').read_text(encoding='utf-8'))
    for item in gantt['mapeo'].values():
        graphic_files += [ROOT/'imagenes/Diagramas que faltaban/Revision-local'/f'{item["stem"]}-{i}.pdf' for i in range(1,item['pages']+1)]
    import pdfplumber
    min_graphic=100
    for graphic in graphic_files:
        with pdfplumber.open(graphic) as doc:
            for page in doc.pages:
                chars=[c for c in page.chars if c['text'].strip()]
                if chars:min_graphic=min(min_graphic,min(c['size'] for c in chars))
                outside=[c['text'] for c in chars if c['x0']<-.6 or c['x1']>page.width+.6 or c['top']<-.6 or c['bottom']>page.height+.6]
                assert not outside,(graphic.name,'texto fuera de la lámina',outside[:10])
    assert min_graphic>=9.49,min_graphic
    result={'rama':base['rama'],'invariantes':unchanged,'paquetes':227,'con_fecha':168,'continuos':59,
            'HH':220023,'peak_personas':64,'EDT_laminas_verificadas':len(edt['laminas']),
            'graficos_recompuestos':len(graphic_files),'tipografia_minima_laminas_pt':round(min_graphic,3),'documentos':[]}
    sources=[p for folder in ['subdocumento-07','subdocumento-07-anexos','formulario-t14','formulario-t15','formulario-t18']
             for p in (ROOT/folder).rglob('*.tex')]
    result['fuentes_actuales']={str(p.relative_to(ROOT)).replace('\\','/'):sha(p) for p in sources}
    graphic_pages=[]
    for name in DOCS+['main']:
        p=TMP/(name+'.pdf');reader=PdfReader(p)
        log=(TMP/(name+'.log')).read_text(encoding='utf-8',errors='replace')
        diagnostics={
            'fatales':re.findall(r'^![^\n]*',log,re.M),
            'referencias_pendientes':re.findall(r'[^\n]*(?:undefined|Rerun to get|Label\(s\) may have changed|multiply defined)[^\n]*',log),
            'glifos_ausentes':re.findall(r'Missing character[^\n]*',log),
            'desbordes':re.findall(r'Overfull[^\n]*',log),
            'glue_heredado':log.count('Infinite glue shrinkage')}
        assert not diagnostics['fatales'] and not diagnostics['referencias_pendientes'] and not diagnostics['glifos_ausentes'],(name,diagnostics)
        assert not diagnostics['desbordes'],(name,diagnostics['desbordes'])
        texts=[p.extract_text() or '' for p in reader.pages]
        assert not any('??' in t for t in texts),(name,'marcador ??')
        assert not any('detalle de aceptación H12 abajo' in t for t in texts)
        aux=(TMP/(name+'.aux')).read_text(encoding='utf-8',errors='replace')
        labels=re.findall(r'\\newlabel\{([^}]+)\}',aux)
        assert len(labels)==len(set(labels)),(name,'etiquetas duplicadas')
        if name in DOCS:
            figures=[]
            for label in ['fig:7-gantt','fig:7-gantt-7','fig:7-red','fig:T14-gantt','fig:T14-gantt-7']:
                match=re.search(r'\\newlabel\{'+re.escape(label)+r'\}\{\{([^}]+)\}\{([^}]+)\}',aux)
                if match:figures.append({'etiqueta':label,'numero':match[1],'pagina':match[2]})
            details=[]
            terms=['Elaboración preliminar:','Aprobación: H8','objetivo total es de 40','Niveles de reversión',
                   '217,60','1.049,60','incompatibilidad','Verificaciones programadas','Dependencias · ID',
                   'Lámina 1 de','Hoja de barras 1 de']
            for i,t in enumerate(texts):
                if any(term in ' '.join(t.split()) for term in terms):details.append(i+1)
            result['documentos'].append({'documento':name,'paginas':len(reader.pages),
                'paginas_antes':base['documentos'][name]['paginas'],'sha256':sha(p),
                'diagnosticos':diagnostics,'etiquetas':figures,'paginas_detalle':details})
            if name=='LAFROX-Subdocumento7':graphic_pages=[i+1 for i,t in enumerate(texts) if 'Gantt de implementación' in t or 'Carta de los 56 meses' in t or 'Vista crítica conservada' in t]
    a=PdfReader(TMP/(DOCS[0]+'.pdf'));b=PdfReader(TMP/'main.pdf')
    assert len(a.pages)==len(b.pages)
    assert all((x.extract_text() or '')==(y.extract_text() or '') for x,y in zip(a.pages,b.pages))
    result['main_equivalente_texto_y_paginas']=True
    result['paginas_totales']=sum(d['paginas'] for d in result['documentos'])
    (OUT/'VERIFICACION.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'paginas':[(d['documento'],d['paginas']) for d in result['documentos']],
                      'HH':220023,'invariantes_conservadas':all(unchanged.values())},ensure_ascii=False))
    return result

def render():
    result=checks();qa=TMP/'qa';qa.mkdir(exist_ok=True)
    for item in result['documentos']:
        name=item['documento'];doc=pdfium.PdfDocument(TMP/(name+'.pdf'));sheets=[]
        for start in range(0,len(doc),12):
            sheet=Image.new('RGB',(1600,2200),'#dedede');draw=ImageDraw.Draw(sheet)
            for i in range(start,min(start+12,len(doc))):
                pic=doc[i].render(scale=.75).to_pil();pic.thumbnail((510,510))
                x=((i-start)%3)*533+(533-pic.width)//2;y=((i-start)//3)*550+25
                sheet.paste(pic,(x,y));draw.text((((i-start)%3)*533+8,((i-start)//3)*550+6),f'{i+1}',fill='black')
            path=qa/f'{name}-hoja-{start+1:03}.jpg';sheet.save(path,quality=90);sheets.append(str(path.relative_to(ROOT)))
        details=[]
        for number in item['paginas_detalle']:
            path=qa/f'{name}-detalle-{number:03}.png';doc[number-1].render(scale=1.5).to_pil().save(path);details.append(str(path.relative_to(ROOT)))
        item['hojas_contacto']=sheets;item['detalles_renderizados']=details
        doc.close();print(name,'renderizado',len(sheets),'hojas',flush=True)
    result['inspeccion_visual']='Pendiente de inspeccionar las imágenes generadas.'
    (OUT/'VERIFICACION.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')

def publish():
    guard();result=json.loads((OUT/'VERIFICACION.json').read_text(encoding='utf-8'))
    assert result.get('inspeccion_visual','').startswith('Completada'), 'Completar primero la inspección visual.'
    for d in result['documentos']:
        assert sha(TMP/(d['documento']+'.pdf'))==d['sha256'], 'PDF cambiado después de la inspección'
    for name,digest in result['fuentes_actuales'].items():assert sha(ROOT/name)==digest,name
    base=json.loads((OUT/'BASE_INICIAL.json').read_text(encoding='utf-8'))
    assert all(sha(ROOT/name)==digest for name,digest in base['invariantes'].items())
    for name in DOCS+['main']:shutil.copy2(TMP/(name+'.pdf'),ROOT/(name+'.pdf'))
    print('Cinco PDF finales y main.pdf sincronizados desde la compilación validada.')

if __name__=='__main__':
    sys.stdout.reconfigure(encoding='utf-8');{'comprobar':checks,'render':render,'publicar':publish}[sys.argv[1]]()
