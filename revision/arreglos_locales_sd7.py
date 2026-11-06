"""Correcciones locales reproducibles. No reestima ni reprograma el proyecto."""
from pathlib import Path
from datetime import date, timedelta
import hashlib, json, re, shutil, subprocess, sys, xml.etree.ElementTree as ET
from urllib.parse import unquote
from io import BytesIO

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'revision/local-20261105'
TMP = ROOT / 'tmp/pdfs/local-20261105'
ASSETS = ROOT / 'imagenes/Diagramas que faltaban/Revision-local'
EXPECTED = 'LafroX-Subdoc7-LateX-CORRIGIENDO'
DOCS = ['LAFROX-Subdocumento7', 'LAFROX-Subdocumento7-Anexos',
        'LAFROX-Formulario-T-14', 'LAFROX-Formulario-T-15', 'LAFROX-Formulario-T-18']
NUMERIC = ['formulario-t15/tablas/'+s+'.tex' for s in
           ['tab_T15_2','tab_T15_paquetes','tab_T15_4','tab_T15_4_personas']]
GANTT = ['Fig_7_Gantt_Resumen_Dependencias.gan','Fig_7_Gantt_56_Meses.gan','Fig_7_Gantt_Vista_Critica.gan']

def guard():
    branch=subprocess.check_output(['git','branch','--show-current'],cwd=ROOT,text=True).strip()
    if branch != EXPECTED: raise RuntimeError('Rama no autorizada: '+branch)

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def baseline():
    guard(); OUT.mkdir(parents=True,exist_ok=True); TMP.mkdir(parents=True,exist_ok=True)
    target=OUT/'BASE_INICIAL.json'
    if target.exists(): raise RuntimeError('La captura inicial ya existe; no sobrescribir.')
    from pypdf import PdfReader
    files=NUMERIC+['imagenes/Diagramas que faltaban/'+s for s in GANTT]
    info={'rama':EXPECTED,'head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
          'invariantes':{p:sha(ROOT/p) for p in files},'documentos':{}}
    for name in DOCS:
        p=ROOT/(name+'.pdf'); shutil.copy2(p,TMP/(name+'-antes.pdf'))
        info['documentos'][name]={'sha256':sha(p),'paginas':len(PdfReader(p).pages)}
    src=ROOT/'imagenes/Diagramas que faltaban/Fig_7-20_Red_Precedencias.pdf'
    shutil.copy2(src,TMP/'red-antes.pdf')
    target.write_text(json.dumps(info,ensure_ascii=False,indent=2),encoding='utf-8')
    print('Referencia inicial guardada; cinco PDF preservados.')

def replace(p,old,new):
    text=p.read_text(encoding='utf-8-sig')
    if new in text:return
    if old not in text:
        if new in text:return
        raise ValueError('Texto no encontrado: '+str(p)+' '+old[:70])
    p.write_text(text.replace(old,new),encoding='utf-8')

def text_edits():
    guard()
    p=ROOT/'formulario-t14/tablas/tab_T14_4.tex'
    replace(p,'& ARQ & Mes 1 (H1).', '& ARQ & Elaboración preliminar: mes 1. Aprobación: H1, mes 2.')
    replace(p,'& ARQ & Mes 13 (H8).', '& ARQ & Elaboración: mes 13. Aprobación: H8, mes 14.')
    folders=['subdocumento-07','subdocumento-07-anexos','formulario-t14','formulario-t15','formulario-t18']
    old='En este capítulo, BA, BTT y Caso designan las Bases Administrativas, las Bases Técnicas Transversales y las Bases Técnicas del caso.'
    glossary=' SD seguido de un número identifica el Subdocumento correspondiente. EDT significa estructura de descomposición del trabajo; PT, paquete de trabajo; HH, horas hombre; y E1/E2, Etapas 1 y 2. En las cartas Gantt, RC identifica los elementos marcados como ruta crítica en la fuente de programación y PT/H identifica los demás paquetes e hitos.'
    replace(ROOT/'subdocumento-07/contenido.tex',old,old+glossary)
    for folder in folders[1:]:
        p=ROOT/folder/'contenido.tex'
        lead='En estos anexos,' if folder=='subdocumento-07-anexos' else 'En este formulario,'
        old=lead+' BA, BTT y Caso designan las Bases Administrativas, las Bases Técnicas Transversales y las Bases Técnicas del caso.'
        replace(p,old,old+glossary)
    p=ROOT/'subdocumento-07/tablas/tab_SD7_2.tex'
    replace(p,'M1–M12 y los portales de clientes y de transportistas; el portal de proveedores se construye con M11 Canal moderno (3.5.1)','M1–M12 y portales de clientes y transportistas')
    p=ROOT/'subdocumento-07/contenido.tex'
    marker='\\parte{tablas/tab_SD7_2}'
    replace(p,marker,marker+'\n\nEl portal de proveedores se construye con M11 Canal moderno, en el paquete 3.5.1. Las categorías de cobertura se superponen: sus cantidades no se suman para obtener los 227 paquetes de la EDT.')
    p=ROOT/'subdocumento-07/tablas/tab_SD7_7.tex'
    text=p.read_text(encoding='utf-8')
    rows=[
      '  Técnico & Restitución automática de la entrega previa & Mecanismo automático; supervisión SRE & Objetivo: \\ensuremath{\\leq}10 minutos en Preproducción \\\\',
      '  Operacional, Etapa 1 & Versión local probada, escritor único y DTE válidos & Operaciones del CLIENTE & Antes de las 05:30 \\\\',
      '  Operacional, Etapa 2 & Desactivación de la capacidad afectada de E2 & Operaciones del CLIENTE & Fuera de 05:30–07:00 \\\\'
    ]
    lines=text.splitlines(); j=0
    for i,line in enumerate(lines):
        if re.match(r'\s*(Técnico|Operacional, Etapa [12]) &',line):lines[i]=rows[j];j+=1
    assert j==3
    p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    p=ROOT/'subdocumento-07/contenido.tex'
    marker='\\parte{tablas/tab_SD7_7}'
    explanation=('\n\nEl objetivo técnico de hasta 10 minutos es una parte del ensayo de reversión; el objetivo total es de 40 minutos. '
      'La preparación de la contingencia operacional dispone de hasta 30 minutos en paralelo con la reversión técnica; '
      'la verificación y autorización de despacho dispone de hasta 10 minutos adicionales. Por tanto, el total se calcula como '
      '\\(\\max(10,30)+10=40\\) minutos (Formulario T-18, sección 6.4). La decisión límite propuesta es a las 04:45 '
      'y la restauración operacional objetivo, a las 05:25, antes de las 05:30. El ensayo mide estos objetivos; '
      'el papel sólo apoya las tareas auxiliares y no sustituye el despacho crítico. En E2, la desactivación afecta '
      'únicamente a la capacidad que falla y conserva la Etapa 1. Los cambios de indicadores de funcionalidad siguen '
      'su procedimiento autorizado, distinto del disparo técnico automático.')
    replace(p,marker,marker+explanation)
    replace(p,'La quinta lámina amplía la cuenta 3.10 para que se lean sus paquetes de innovación:',
              'La quinta lámina detalla los paquetes de innovación agrupados en la cuenta 3.10:')
    replace(p,'Las láminas siguientes desglosan las cuentas de control y los paquetes por fase. Cada imagen se presenta inmediatamente después de su descripción. La fase 3 se divide en cinco láminas para facilitar la lectura: las dos primeras separan la base técnica de los módulos de la Etapa 1; las tres restantes muestran las cuentas 3.5 a 3.11, con una lámina adicional para ampliar los paquetes de innovación de la cuenta 3.10.',
              'Las láminas siguientes desglosan las cuentas de control y los paquetes por fase. Cada imagen se presenta después de su descripción. La fase 3 se divide en cinco láminas: base técnica, módulos de la Etapa 1, cuentas 3.5 a 3.8, cuentas 3.9 a 3.11 y detalle de los paquetes de innovación de la cuenta 3.10.')
    replace(ROOT/'formulario-t18/contenido.tex','\\subsection{Controles nuevos de coordinación y aceptación}',
            '\\subsection{Verificaciones programadas de coordinación y recuperación}')
    print('Correcciones textuales aplicadas.')

def polish():
    guard()
    short=(' H1–H12 son los hitos del Formulario E-25 y F1–F8, los frentes de trabajo. '
           'QA designa el ambiente de calidad; SRE, el equipo de operación e ingeniería de fiabilidad; '
           'NOC, el centro de operaciones; SOC, el centro de operaciones de seguridad; y DTE, los documentos tributarios electrónicos.')
    ending='PT/H identifica los demás paquetes e hitos.'
    for folder in ['subdocumento-07','subdocumento-07-anexos','formulario-t14','formulario-t15','formulario-t18']:
        p=ROOT/folder/'contenido.tex';s=p.read_text(encoding='utf-8')
        if short not in s:s=s.replace(ending,ending+short,1)
        p.write_text(s,encoding='utf-8')
    p=ROOT/'subdocumento-07/contenido.tex';s=p.read_text(encoding='utf-8')
    a=s.index('El Anexo 7.F traslada al Capítulo 8 los supuestos, disparadores, responsables y paquetes de la planificación.')
    b=s.index('\n\\clearpage',a)
    summary=('El Anexo 7.F traslada al Capítulo 8 los supuestos, disparadores, responsables y paquetes de la planificación. '
      'La prueba de precio verifica que se conserve el acordado al capturar el pedido (Subdocumento 2, Anexo 2.2, S-09; RF-03.11 y RF-03.12). '
      'La coordinación de reserva y retención se verifica antes del H4 con AL-STOCK-01 y AL-ACT-01; los paquetes 3.8.4 y 3.9.3 comprueban carga y drenaje.\n\n'
      'El Formulario T-18, sección 6.5, especifica las condiciones técnicas de estas verificaciones y sus referencias al Subdocumento 4. '
      'La recuperación se demuestra con AL-DR-01 antes del H5 y del H10 '
      'y, después, dos veces al año durante la Operación (Bases Técnicas Transversales, cap. 7, RT-07.07, p. 17). '
      'El calendario y la asignación del equipo de cada campaña se completan conforme al programa de pruebas, sin alterar sus criterios de aceptación.\n')
    s=s[:a]+summary+s[b:]
    needle='el papel sólo apoya las tareas auxiliares y no sustituye el despacho crítico.'
    s=s.replace(needle,'la medición se realiza en Preproducción y fuera de la ventana de despacho. El papel sólo apoya las tareas auxiliares y no sustituye el despacho crítico.',1)
    p.write_text(s,encoding='utf-8')
    print('Glosario completado y duplicación técnica resumida mediante remisión interna.')

def layout_text():
    guard()
    for folder in ['subdocumento-07','formulario-t14']:
        p=ROOT/folder/'contenido.tex';s=p.read_text(encoding='utf-8')
        s=s.replace('Fuente: elaboración en GanttProject a partir de',
                    'Fuente: elaboración gráfica a partir de la programación en GanttProject y de')
        s=s.replace('elaborada en GanttProject:', 'basada en la programación en GanttProject:')
        for word in ['primera','segunda','tercera','cuarta','quinta']:
            s=s.replace(word+' lámina',word+' figura')
        if folder=='subdocumento-07':
            s=s.replace('clip,width=1.12\\linewidth,height=0.90\\textheight','clip,width=0.97\\linewidth,height=0.90\\textheight')
            s=s.replace('Las láminas siguientes desglosan las cuentas de control y los paquetes por fase. Cada imagen se presenta después de su descripción. La fase 3 se divide en cinco láminas:',
                        'Las figuras siguientes desglosan las cuentas de control y los paquetes por fase. Cada figura está precedida por su descripción y puede continuar en varias láminas. La fase 3 se presenta en cinco figuras:')
        else:
            s=s.replace('La figura siguiente presenta la EDT completa en una sola vista panorámica. Por su densidad, se recomienda ampliarla en el PDF; el Subdocumento 7 contiene las láminas separadas por fase para consultar las cuentas de control y los paquetes con mayor legibilidad.',
                        'La Figura \\ref{fig:T14-edt-completa} presenta la EDT completa en láminas consecutivas por fase, con sus cuentas de control y paquetes legibles a tamaño impreso. La jerarquía y los códigos son los de la estructura anterior; el Subdocumento 7 organiza sus figuras de detalle por fase.')
        p.write_text(s,encoding='utf-8')
    print('Descripciones y fuentes adaptadas a las continuaciones gráficas.')

def network():
    guard()
    from pypdf import PdfReader,PdfWriter
    import pdfplumber
    from reportlab.pdfgen import canvas
    source=TMP/'red-antes.pdf'; ASSETS.mkdir(parents=True,exist_ok=True)
    reader=PdfReader(source); xml=unquote(str(reader.metadata['/Subject']))
    tree=ET.fromstring(xml); cells=tree.findall('.//mxCell')
    changed=0
    for cell in cells:
        value=cell.get('value','')
        if 'detalle de aceptación H12 abajo' in value:
            cell.set('value',value.replace(' · detalle de aceptación H12 abajo',''));changed+=1
    assert changed==1 and sum(c.get('edge')=='1' for c in cells)==33
    ET.ElementTree(tree).write(ASSETS/'Fig_7-20_Red_Precedencias.drawio',encoding='utf-8',xml_declaration=True)
    with pdfplumber.open(source) as doc:
        hits=doc.pages[0].search('D-29 a D-31c.*');assert len(hits)==1
        hit=hits[0]; width,height=doc.pages[0].width,doc.pages[0].height
    # Retirar el objeto de texto: la anotación obsoleta tampoco queda en la extracción.
    import pypdfium2 as pdfium
    doc=pdfium.PdfDocument(source); pg=doc[0]; textpage=pg.get_textpage()
    targets=[o for o in pg.get_objects(filter=[pdfium.raw.FPDF_PAGEOBJ_TEXT],textpage=textpage)
             if 'detalle de aceptación H12 abajo' in o.extract()]
    assert len(targets)==1
    small_labels=[o for o in pg.get_objects(filter=[pdfium.raw.FPDF_PAGEOBJ_TEXT],textpage=textpage) if o.extract().strip()=='D-20']
    textpage.close()
    for obj in targets: pg.remove_obj(obj);obj.close()
    for obj in small_labels:
        assert pdfium.raw.FPDFTextObj_SetFontSize(obj,37)
    pg.gen_content(); clean=TMP/'red-sin-rotulo.pdf';doc.save(clean);pg.close();doc.close()
    clean_reader=PdfReader(clean);page=clean_reader.pages[0]
    buf=BytesIO(); c=canvas.Canvas(buf,pagesize=(width,height))
    c.setFillColorRGB(.75,.20,.17);c.setFont('Helvetica-Bold',9)
    c.drawString(hit['x0'],height-hit['bottom']+1.4,'D-29 a D-31c');c.save();buf.seek(0)
    page.merge_page(PdfReader(buf).pages[0])
    writer=PdfWriter();writer.add_page(page)
    metadata={k:str(v) for k,v in reader.metadata.items()};metadata['/Subject']=ET.tostring(tree,encoding='unicode')
    writer.add_metadata(metadata)
    with (ASSETS/'Fig_7-20_Red_Precedencias.pdf').open('wb') as f:writer.write(f)
    assert 'detalle de aceptación H12 abajo' not in PdfReader(ASSETS/'Fig_7-20_Red_Precedencias.pdf').pages[0].extract_text()
    print('Red editable recuperada; 33 conectores conservados.')

if __name__=='__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    {'baseline':baseline,'texto':text_edits,'pulir':polish,'composicion':layout_text,'red':network}[sys.argv[1]]()
