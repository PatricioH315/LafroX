from pathlib import Path
from copy import deepcopy
import zipfile,json,hashlib
from lxml import etree as E

root=Path(__file__).resolve().parents[2]
source=root/'Presentaciones/Actualizada/Guia para el cliente SD9 y SD13 con guion tecnico actualizada.docx'
out=root/'Presentaciones/Actualizada/Guia para el cliente SD9 y SD13 con guion compacto.docx'
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
q=lambda n:'{'+ns['w']+'}'+n
scripts={
34:'Las normas se traducen en controles verificables: calidad del producto y de los datos, pruebas documentadas, seguridad y accesibilidad. ISO 9001 aporta gestión y auditoría; CMMI, madurez del proceso. Separamos estos referentes de las obligaciones legales y de los estándares GS1 y EDI. Para Puelche, el cumplimiento se demuestra con informes y registros, no solo nombrando normas.',
35:'Comprobamos requisitos, respuesta bajo carga, integraciones y facilidad de uso. También revisamos seguridad, recuperación y calidad del código. A Producción pasa el mismo artefacto validado. Son criterios de aceptación, no resultados ya obtenidos: la continuidad del despacho se controla aparte de la disponibilidad mensual, y los resultados del negocio se verifican en operación cuando corresponde.',
36:'Las puertas controlan si un cambio puede avanzar: revisión por pares, pruebas, seguridad y reversión. Si falla un criterio bloqueante, se corrige y se verifica nuevamente. Entrar a Producción inicia la marcha blanca; no equivale a aceptarla. Su cierre exige todas las condiciones del protocolo: incidentes atribuibles resueltos, volumen real, continuidad y respuesta, conciliación, usuarios certificados y acta de Puelche.',
37:'Probamos desde el código hasta el terreno: reglas, integraciones, regresión y aceptación de usuarios. En preproducción ensayamos carga, fallas, migración y reversión; en terreno, trabajo sin señal y condiciones físicas. La carga viene del dimensionamiento. Automatizamos lo repetible y programamos aparte las pruebas manuales. Cada caso deja evidencia y los datos reales usados en pruebas requieren anonimización verificada.',
38:'Seguimos cada necesidad hasta el requisito, el trabajo, la prueba y la aceptación. El identificador del requisito vincula el código y el digest identifica la versión desplegada. Si hay desviaciones, analizamos la causa, corregimos y verificamos con el mismo criterio. El esfuerzo de calidad incluye prevención y evaluación; no representa por sí solo el costo de todas las fallas.',
50:'Proponemos seguimiento del vencimiento posentrega, reproducción de incidentes y estimación de vida útil por historia térmica. Esta última se valida por familia y no amplía la fecha impresa. El tramo variable del pago depende del costo comparable y del servicio. La hoja del almacenero se muestra en el terminal del preventista o se entrega impresa a solicitud. Cada innovación tiene indicadores: sus metas siguen en la oferta, pero no son beneficios ya demostrados.'}
with zipfile.ZipFile(source) as z:
    infos=z.infolist();data={i.filename:z.read(i.filename) for i in infos}
doc=E.fromstring(data['word/document.xml']);body=doc.find('w:body',ns)
def text(p):return ''.join(p.xpath('.//w:t/text()',namespaces=ns))
before_tables=[E.tostring(t) for t in body.findall('w:tbl',ns)]
counts={};slide=None;inside=False;old=[]
for el in list(body):
    if el.tag!=q('p'):continue
    value=text(el)
    if value.startswith('Diapositiva '):slide=int(value.split()[-1])
    if value=='Guion para exponer':inside=True;old=[];continue
    if inside and value=='Si el cliente pregunta':
        counts[slide]={'before':len(' '.join(text(p) for p in old).split()),'after':len(scripts[slide].split())}
        p=old[0]
        props=p.find('w:r/w:rPr',ns);props=deepcopy(props) if props is not None else None
        for child in list(p):
            if child.tag!=q('pPr'):p.remove(child)
        r=E.SubElement(p,q('r'))
        if props is not None:r.append(props)
        E.SubElement(r,q('t')).text=scripts[slide]
        for p in old[1:]:body.remove(p)
        inside=False;continue
    if inside:old.append(el)
assert before_tables==[E.tostring(t) for t in body.findall('w:tbl',ns)]
assert sorted(counts)==[34,35,36,37,38,50]
data['word/document.xml']=E.tostring(doc,xml_declaration=True,encoding='UTF-8',standalone=True)
with zipfile.ZipFile(out,'w') as z:
    for info in infos:z.writestr(info,data[info.filename])
before=sum(v['before'] for v in counts.values());after=sum(v['after'] for v in counts.values())
report={'counts':counts,'before':before,'after':after,'reduction_percent':round((1-after/before)*100),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'output':str(out),'tables_unchanged':True}
(root/'tmp/guia_actualizada/compact_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(report,ensure_ascii=False,indent=2))
