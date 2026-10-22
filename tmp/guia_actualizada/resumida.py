from pathlib import Path
from copy import deepcopy
from lxml import etree as E
import zipfile,json,hashlib

ROOT=Path(__file__).resolve().parents[2]
SOURCE=Path(r'C:\Users\henri\Downloads\Guia para el cliente SD9 y SD13 con guion tecnico.docx')
PPT=ROOT/'Presentaciones/Actualizada/LafroX - Informe 2 - plan de calidad resumido.pptx'
OUT=ROOT/'Presentaciones/Actualizada/Guia cliente SD9 y SD13 adaptada al plan resumido.docx'
NS={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
q=lambda n:'{'+NS['w']+'}'+n
pages=[
{'slide':33,'title':'Normas del plan de calidad','template':0,'rows':[
('ISO/IEC 25010','Organiza los criterios de calidad del producto. Cada criterio debe vincularse con una prueba y su resultado.'),
('ISO/IEC 25012','Permite evaluar que los datos estén completos, sean correctos y no se contradigan; las conciliaciones ayudan a comprobarlo.'),
('ISO/IEC/IEEE 29119','Ordena la planificación, ejecución y documentación de las pruebas, para saber qué se comprobó y con qué resultado.'),
('PMBOK','Guía cómo planificar, gestionar y controlar la calidad del proyecto. No es una certificación del software.'),
('WCAG 2.2 AA','Son criterios de accesibilidad. La evaluación combina herramientas automáticas y revisión manual.'),
('OWASP','Aporta referencias de seguridad para revisar el código y la aplicación funcionando. Ambos controles se complementan.'),
('Pruebas y conciliaciones','Son evidencia para comprobar el funcionamiento del producto y la consistencia de sus datos.'),
('Informes de revisión','Documentan los resultados de los controles de seguridad y accesibilidad, con herramientas y revisión de personas.'),
('Registros y acciones','Dejan constancia de revisiones, desviaciones y correcciones. La evidencia permite acreditar cumplimiento, no solo mencionar una norma.')],
'script':'El plan convierte las referencias en controles verificables. ISO 25010 organiza la calidad del producto; ISO 25012, la de los datos; ISO 29119, las pruebas. PMBOK guía la gestión; WCAG y OWASP apoyan accesibilidad y seguridad. Para Puelche, el cumplimiento se demuestra con pruebas, conciliaciones, informes y registros.',
'question':'¿Basta con citar la norma? No: debe existir un control aplicado y evidencia de su resultado.',
'source':'SD9, tabla 9.2, p. 8, y §9.1.4. Detalle complementario en las notas de la diapositiva 33.'},
{'slide':34,'title':'Calidad del producto','template':1,'rows':[
('Criterios de aceptación','Son las condiciones con las que se evaluará la entrega; no resultados que estemos declarando alcanzados.'),
('Funcionalidad','Cada requisito ofertado debe tener una prueba aprobada antes del hito que le corresponde.'),
('Desempeño','Se mide la respuesta de las transacciones críticas bajo la carga definida; un promedio favorable no basta.'),
('Compatibilidad','Se verifica el intercambio correcto de información y el funcionamiento de los procesos entre componentes y sistemas.'),
('Usabilidad','Se comprueban las tareas de cada perfil, las condiciones de trabajo y la accesibilidad WCAG 2.2 AA.'),
('Fiabilidad','Incluye continuidad y recuperación. La disponibilidad mensual no sustituye la protección de la ventana de despacho.'),
('Seguridad','No se acepta avanzar con hallazgos críticos o altos abiertos. No equivale a prometer riesgo nulo.'),
('Mantenibilidad','La revisión del código y la cobertura de pruebas ayudan a controlar los cambios; no garantizan ausencia de errores.'),
('Portabilidad','Se promueve el mismo artefacto validado entre ambientes, para no probar una versión y entregar otra.'),
('Resultados del negocio','Se verifican en operación y en el momento previsto para cada resultado; no todos se acreditan con una demostración técnica.')],
'script':'Comprobamos que los requisitos funcionen, que el despacho mantenga continuidad y que no queden hallazgos graves abiertos. También evaluamos respuesta, integración y facilidad de uso. A Producción pasa el mismo artefacto validado. Son criterios de aceptación, no resultados ya obtenidos; los resultados del negocio se comprueban en operación cuando corresponde.',
'question':'¿Dónde están los umbrales? En el plan, el protocolo y las notas. Siguen vigentes aunque no se enumeren al exponer.',
'source':'SD9, tablas 9.1, p. 6; 9.3, p. 10; 9.8, p. 18. T17, §5.'},
{'slide':35,'title':'Controles y aceptación','template':2,'rows':[
('A Revisar el cambio','Agrupa controles como revisión por pares, pruebas automáticas y seguridad del código antes de avanzar.'),
('B Validar antes de Producción','Comprueba las pruebas habilitantes, la certificación y la reversión ensayada antes de la entrada prevista.'),
('C Supervisar en operación','Observa el despliegue y sus indicadores, y permite revertir si se degrada el servicio.'),
('Condiciones conjuntas','La aceptación de marcha blanca exige cumplir todas las condiciones del protocolo. Una no compensa a otra.'),
('Incidentes atribuibles','No deben quedar incidentes críticos o altos abiertos atribuibles a la solución al cierre de marcha blanca.'),
('Volumen real','Debe registrarse todo el volumen real comprometido de la ola durante las últimas cuatro semanas, no una muestra.'),
('Continuidad y respuesta','Entre 05:30 y 07:00 no debe haber caída. También deben cumplirse los umbrales de disponibilidad y respuesta del protocolo.'),
('Conciliación','No deben quedar diferencias pendientes de explicación entre los datos conciliados.'),
('Usuarios de la ola','Quienes usarán la solución en esa ola deben estar capacitados y certificados.'),
('Acta de la Contraparte','La Contraparte Técnica firma la aceptación. Un acta no sustituye una prueba fallida ni levanta un bloqueo.'),
('Mejora continua','Se analiza la causa, se corrige y se verifica con el mismo criterio antes de cerrar con evidencia o escalar.')],
'script':'Los controles se agrupan en revisar el cambio, validar antes de Producción y supervisar la operación. Si algo falla, se corrige y se verifica. La aceptación de Puelche exige todas las condiciones del protocolo; iniciar la marcha blanca no equivale a aceptarla. La mejora continua analiza la causa y cierra las correcciones con evidencia.',
'question':'¿Se puede aceptar si falta una condición? No. Los grupos A, B y C resumen la exposición, pero no sustituyen las puertas del plan ni la aceptación contractual.',
'source':'SD9, §9.2.1, tabla 9.7, p. 16, y §9.2.6. T17, §4.3 y p. 12, Art. 17.3.'},
{'slide':36,'title':'Pruebas y evidencia','template':3,'rows':[
('Código e integración','Comprueba reglas, componentes y acuerdos de intercambio; la regresión revisa que un cambio no rompa lo que funcionaba.'),
('Seguridad y accesibilidad','Se revisa que la aplicación no mantenga hallazgos graves abiertos y que las personas puedan utilizarla.'),
('Antes de Producción','Se realizan aceptación de usuarios y ensayos de carga, fallas, recuperación, migración, despliegue y reversión.'),
('Terreno y operación','Se prueba el trabajo sin señal y la sincronización, el frío con guantes y el uso real. En marcha blanca se siguen indicadores.'),
('Requisito del ejemplo','Identificar clientes afectados por un lote en menos de dos horas. No significa retirar físicamente toda la mercadería en ese tiempo.'),
('Simulacro cronometrado','Comprueba el requisito mediante una prueba cuyo tiempo y resultado quedan registrados.'),
('Evidencia y acta','Relacionan el requisito con el resultado comprobado y con la aceptación de Puelche. El acta no reemplaza la prueba.'),
('Datos de prueba','Los datos reales usados en pruebas requieren anonimización. La evidencia debe conservar el caso, el ambiente y su resultado.')],
'script':'Probamos desde el código hasta condiciones de operación real: integración, carga, recuperación y trabajo sin señal. Cada resultado queda documentado. El ejemplo une requisito, simulacro cronometrado y aceptación de Puelche para comprobar la identificación de clientes afectados por un lote. Así mostramos evidencia del cumplimiento, no solo una lista de pruebas. Los datos reales de prueba requieren anonimización.',
'question':'¿Qué demuestra la trazabilidad? Que la necesidad del cliente tiene una prueba y un resultado vinculados con la entrega que acepta Puelche.',
'source':'SD9, tablas 9.8, p. 18, y 9.9, p. 20; §§9.2.4–9.2.5. T13, §§8.2–8.3. T17, §5, p. 12.'},
{'slide':37,'title':'Innovaciones con evaluación','template':5,'rows':[
('Seguimiento posentrega','Avisa al preventista de posibles vencimientos en el local. El riesgo se confirma y se aplican acciones autorizadas; se evalúan acierto y vencimiento.'),
('Reproducción de incidentes','Usa evidencia protegida para reconstruir una falla de terreno y comparar el tiempo hasta reproducir su causa en casos equivalentes.'),
('Vida útil por historia térmica','Usa temperatura y tiempo como apoyo a Calidad. Se valida por familia; nunca extiende la fecha impresa ni elimina bloqueos térmicos.'),
('Pago ligado al costo de servir','Propone un tramo variable condicionado a la mejora del costo comparable y al servicio. Finanzas debe poder reproducir el cálculo.'),
('OTIF','Significa entregas completas y a tiempo. Una reducción del costo no cuenta si empeora el servicio o distorsiona la comparación.'),
('Hoja del almacenero','Se muestra en el terminal del preventista o se entrega impresa a solicitud. No exige internet ni dispositivo al local; se evalúan comprensión y cobertura.'),
('Metas y resultados','Cada innovación tiene indicadores y momentos de verificación. Sus metas se mantienen en la oferta, pero no son beneficios ya demostrados.')],
'script':'Proponemos seguimiento posentrega, reproducción de incidentes y vida útil por historia térmica, sin ampliar la fecha impresa. El tramo variable del pago depende del costo comparable y del servicio. La hoja del almacenero se muestra en el terminal del preventista o se entrega impresa a solicitud. Cada innovación tiene indicadores; sus metas no son beneficios ya demostrados.',
'question':'¿De dónde sale el porcentaje de mejora? Es la meta de diseño ofertada, no una medición previa. Consultar indicador, línea base y momento de verificación en las notas.',
'source':'SD13, tablas 13.5, p. 15; 13.10, p. 23; 13.15, p. 32; 13.21, p. 40; 13.26, p. 47. T19, fichas 1–5.'}
]
with zipfile.ZipFile(SOURCE) as z:
    infos=z.infolist();data={i.filename:z.read(i.filename) for i in infos}
doc=E.fromstring(data['word/document.xml']);body=doc.find('w:body',NS)
pars=body.findall('w:p',NS);tables=body.findall('w:tbl',NS)
txt=lambda p:''.join(p.xpath('.//w:t/text()',namespaces=NS))
head=next(p for p in pars if txt(p)=='Diapositiva 34');sub=next(p for p in pars if txt(p)=='Normas y leyes')
normal=next(p for p in pars if txt(p).startswith('El plan de calidad'))
guion=next(p for p in pars if txt(p)=='Guion para exponer');sourcep=next(p for p in pars if txt(p).startswith('Base documental'))
section=deepcopy(body.find('w:sectPr',NS))
def prop(p):
    r=p.find('w:pPr',NS)
    if r is None:r=E.Element(q('pPr'));p.insert(0,r)
    return r
def paragraph(template,value,bold=None,size=None):
    p=deepcopy(template);rp=p.find('w:r/w:rPr',NS);rp=deepcopy(rp) if rp is not None else E.Element(q('rPr'))
    for n in ['color','strike','dstrike']:
        for el in rp.findall('w:'+n,NS):rp.remove(el)
    E.SubElement(rp,q('color'),{q('val'):'000000'})
    if bold is not None:
        for el in rp.findall('w:b',NS):rp.remove(el)
        E.SubElement(rp,q('b'),{q('val'):'1' if bold else '0'})
    if size:
        for n in ['sz','szCs']:
            for el in rp.findall('w:'+n,NS):rp.remove(el)
            E.SubElement(rp,q(n),{q('val'):str(round(size*2))})
    for el in list(p):
        if el.tag!=q('pPr'):p.remove(el)
    r=E.SubElement(p,q('r'));r.append(rp);E.SubElement(r,q('t')).text=value
    return p
def table(rows,template):
    t=deepcopy(template);old=t.findall('w:tr',NS);rowtemplate=deepcopy(old[1])
    for r in old[1:]:t.remove(r)
    for values in rows:
        row=deepcopy(rowtemplate)
        for cell,value in zip(row.findall('w:tc',NS),values):
            p=paragraph(cell.find('w:p',NS),value)
            for el in list(cell):
                if el.tag!=q('tcPr'):cell.remove(el)
            cell.append(p)
        t.append(row)
    return t
for el in list(body):body.remove(el)
for j,page in enumerate(pages):
    if j==0:
        p=paragraph(head,'Guía breve del plan de calidad e innovaciones',True,16)
        style=prop(p).find('w:pStyle',NS)
        if style is None:style=E.SubElement(prop(p),q('pStyle'))
        style.set(q('val'),'Title');body.append(p)
    p=paragraph(head,f'Diapositiva {page["slide"]}',True)
    if j:E.SubElement(prop(p),q('pageBreakBefore'))
    body.append(p);body.append(paragraph(sub,page['title'],True))
    if not j:body.append(paragraph(normal,'Posiciones reales 33–37 del PPT resumido. Para exponer, lee solo el guion. Las tablas y las respuestas son respaldo de consulta, no texto para leer completo.',False,10))
    body.append(table(page['rows'],tables[page['template']]))
    body.append(paragraph(guion,'Guion para exponer',True))
    body.append(paragraph(normal,page['script'],False))
    body.append(paragraph(guion,'Si el cliente pregunta',True))
    body.append(paragraph(normal,page['question'],False,10))
    body.append(paragraph(sourcep,'Base documental: '+page['source'],False))
body.append(section)
for el in doc.xpath('//w:strike|//w:dstrike',namespaces=NS):el.getparent().remove(el)
data['word/document.xml']=E.tostring(doc,xml_declaration=True,encoding='UTF-8',standalone=True)
with zipfile.ZipFile(OUT,'w') as z:
    for info in infos:z.writestr(info,data[info.filename])
with zipfile.ZipFile(SOURCE) as a,zipfile.ZipFile(OUT) as b:
    assert all(a.read(n)==b.read(n) for n in a.namelist() if n!='word/document.xml')
count={p['slide']:len(p['script'].split()) for p in pages};assert sum(count.values())<=300
report={'source':str(SOURCE),'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'ppt':str(PPT),'ppt_sha256':hashlib.sha256(PPT.read_bytes()).hexdigest(),'output':str(OUT),'script_words':count,'total_script_words':sum(count.values()),'slides':[p['slide'] for p in pages],'tables':5,'changed_parts':['word/document.xml']}
(ROOT/'tmp/guia_actualizada/resumida_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(report,ensure_ascii=False,indent=2))
