from pathlib import Path
from copy import deepcopy
import zipfile, hashlib, json, re
from lxml import etree as E

ROOT=Path(__file__).resolve().parents[2]
SOURCE=Path(r'C:\Users\henri\Downloads\Guia para el cliente SD9 y SD13 con guion tecnico.docx')
PPT=ROOT/'Presentaciones/Actualizada/LafroX - Informe 2 - calidad e innovaciones revisadas.pptx'
OUT=ROOT/'Presentaciones/Actualizada/Guia para el cliente SD9 y SD13 con guion tecnico actualizada.docx'
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
def q(n):return '{'+ns['w']+'}'+n

pages=[
{'slide':34,'title':'Normas y marco aplicable','rows':[
('ISO IEC 25010','Organiza la calidad del producto: funcionamiento, respuesta, seguridad y otras características. Cada criterio se comprueba mediante pruebas.'),
('ISO IEC 25012','Permite revisar que los datos estén completos, sean correctos y no se contradigan. La conciliación ayuda a detectar diferencias.'),
('ISO IEC IEEE 29119','Ordena cómo planificamos, ejecutamos y documentamos las pruebas. La evidencia permite revisar qué se comprobó y con qué resultado.'),
('PMBOK','Guía la planificación, la gestión y el control de la calidad del proyecto; no certifica por sí solo el software.'),
('WCAG 2.2 AA','Son criterios de accesibilidad. Combinamos herramientas automáticas y revisión manual para comprobar que las personas puedan utilizar la aplicación.'),
('OWASP','Aporta referencias de seguridad para revisar el código y probar la aplicación funcionando. El análisis estático y el dinámico se complementan.'),
('ISO 9001','Aporta el marco de gestión de calidad y auditoría de los registros. No equivale a garantizar que el programa nunca falle.'),
('CMMI DEV N3','Es una evaluación de madurez de procesos definidos y repetibles. No debe presentarse como una certificación ISO.'),
('Sanidad y documentos','Los controles de alimentos y la documentación tributaria se traducen en registros, validaciones y pruebas de los procesos correspondientes.'),
('Jornada y datos personales','Las rutas consideran restricciones de jornada; el acceso y el tratamiento de información personal requieren controles de protección.'),
('GS1 y EDI','GS1 permite identificar productos, lugares y unidades logísticas con códigos comunes. EDI permite intercambiar documentos entre empresas. No son leyes.'),
('Evidencia de cumplimiento','La referencia se acompaña con informes, conciliaciones, registros de ejecución o auditorías. Mencionar una norma no acredita su cumplimiento.')],
'script':[
'El plan de calidad convierte las referencias técnicas en controles que podamos demostrar. ISO 25010 organiza lo que evaluamos del producto e ISO 25012 nos ayuda a comprobar la calidad de los datos, por ejemplo su completitud y consistencia. ISO 29119 ordena cómo se preparan, ejecutan y documentan las pruebas. Para cada criterio vinculamos una medición y la evidencia de su resultado; no nos quedamos en una lista de normas.',
'Complementamos ese trabajo con seguridad basada en OWASP y accesibilidad WCAG, revisada tanto con herramientas como manualmente. ISO 9001 aporta el marco de gestión y auditoría, mientras CMMI se refiere a la madurez del proceso. Separamos estos referentes de las obligaciones sanitarias, tributarias, de jornada y de protección de datos. GS1 y EDI cumplen otra función: identificar e intercambiar información. Para Puelche, la evidencia serán informes y registros que permitan comprobar el cumplimiento antes de aceptar cada entrega.'],
'question':'Si preguntan por una exigencia legal concreta, hay que consultar la disposición aplicable y su trazabilidad en la oferta. No atribuir al SD9 todo el detalle legal de la lámina anterior.',
'source':'SD9, tabla 9.2, p. 8, y §9.1.4. Las obligaciones se presentan por ámbito; GS1 y EDI se separan del marco legal.'},
{'slide':35,'title':'Calidad del producto','rows':[
('Criterios de aceptación','Son las condiciones con las que se evaluará la entrega. No son resultados que estemos declarando alcanzados.'),
('Funcionalidad','Cada requisito ofertado debe tener una prueba aprobada antes de su hito. Desarrollarlo no basta para declararlo cumplido.'),
('Desempeño','Se mide la respuesta de las transacciones críticas bajo la carga definida. Un promedio favorable no basta para acreditar el criterio.'),
('Compatibilidad','Se verifica que las integraciones intercambien información correctamente y que los procesos completos funcionen entre componentes.'),
('Usabilidad','Se comprueba el uso por perfil y en condiciones de trabajo reales, junto con la accesibilidad WCAG 2.2 AA.'),
('Fiabilidad','Incluye continuidad y recuperación. La disponibilidad mensual y la protección de la ventana de despacho son criterios distintos.'),
('Seguridad','No se acepta avanzar con hallazgos críticos o altos abiertos. Esto no equivale a afirmar que el riesgo será siempre nulo.'),
('Mantenibilidad','La revisión del código y la cobertura de pruebas ayudan a controlar los cambios. La cobertura no garantiza que no existan errores.'),
('Portabilidad y artefacto','Se promueve la misma versión de software validada entre ambientes. Así no se prueba una versión y se entrega otra.'),
('Resultados del negocio','Se comprueban con medición en operación, en el momento previsto para cada resultado; una prueba técnica no los acredita todos.')],
'script':[
'La calidad del producto no se limita a que una función esté construida. Comprobamos que cada requisito tenga su prueba aprobada, que las transacciones críticas respondan bajo carga y que las integraciones permitan completar el proceso de negocio. En usabilidad revisamos la tarea de cada perfil y sus condiciones de trabajo, además de la accesibilidad. Estos son criterios de aceptación de la solución, no resultados que demos por obtenidos.',
'En fiabilidad distinguimos la disponibilidad mensual de la continuidad del despacho: un buen indicador mensual no compensa una interrupción en la ventana protegida. También ensayamos la recuperación. La seguridad se revisa para no avanzar con hallazgos graves abiertos; la mantenibilidad se apoya en revisión de código y cobertura de pruebas. A Producción se lleva el mismo artefacto validado. Finalmente, los resultados del negocio se verifican con operación real y en su momento de aceptación, no solo con una demostración técnica.'],
'question':'Si piden un umbral, consultar las notas de esta diapositiva y el protocolo. Las cifras siguen en la oferta: aquí se explica qué se controla, no se sustituyen las condiciones acordadas.',
'source':'SD9, tablas 9.1, p. 6; 9.3, p. 10; 9.8, p. 18. T17, §5, para la aceptación de resultados del caso.'},
{'slide':36,'title':'Controles y aceptación','rows':[
('Puertas y aceptación','Las puertas controlan el avance de un cambio. La aceptación contractual corresponde a Puelche y exige evidencia adicional de operación.'),
('G0 y G1','El cambio pasa por comprobaciones locales y revisión de otra persona antes de incorporarse al código compartido.'),
('G2 y G3','La integración continua revisa pruebas y calidad de código; antes de QA se controlan vulnerabilidades graves y regresiones de desempeño.'),
('G4','Antes de promover a preproducción se revisan regresión, seguridad de la aplicación y accesibilidad.'),
('G5 y G6','G5 habilita la entrada a Producción con pruebas, certificación y reversión. G6 supervisa el despliegue y revierte ante desviaciones.'),
('Incidentes atribuibles','No deben quedar incidentes críticos o altos abiertos atribuibles a la solución al cierre de la marcha blanca.'),
('Volumen real','Debe registrarse la totalidad del volumen real comprometido de la ola durante las últimas cuatro semanas, no solo una muestra.'),
('Continuidad y respuesta','Entre 05:30 y 07:00 no debe haber caída. También deben cumplirse la disponibilidad y los tiempos de respuesta del protocolo.'),
('Conciliación','No deben quedar diferencias pendientes de explicación. Una diferencia registrada sin resolver no equivale a conciliar.'),
('Usuarios de la ola','Quienes usarán la solución en esa ola deben estar capacitados y certificados. No se refiere indistintamente a toda la organización.'),
('Acta de la Contraparte','La aceptación requiere la firma de la Contraparte Técnica. Un acta no reemplaza una prueba fallida ni levanta un bloqueo.'),
('Condiciones conjuntas','Todas deben cumplirse; una no compensa a otra. Iniciar la marcha blanca en Producción no significa que ya esté aceptada.')],
'script':[
'Aquí distinguimos dos decisiones: permitir que un cambio avance y aceptar contractualmente una etapa. Las puertas revisan progresivamente el cambio. Primero se comprueban formato, pruebas y revisión por pares; después, la integración continua revisa el código y las pruebas. Antes de promover se controlan vulnerabilidades, regresión, seguridad y accesibilidad. Si falla un criterio bloqueante, corresponde corregir y volver a presentar evidencia, no reemplazar la prueba con una autorización.',
'La entrada a Producción permite iniciar la marcha blanca con la certificación y las pruebas habilitantes aprobadas, además de la reversión ensayada. La supervisión posterior permite detectar degradaciones y revertir el despliegue. Cerrar la marcha blanca exige además cumplir conjuntamente las condiciones del protocolo: incidentes atribuibles resueltos, volumen real comprometido, continuidad y respuesta, conciliación, usuarios de la ola certificados y acta firmada. Por eso nuestros controles internos no nos permiten declarar aceptada la etapa por cuenta propia.'],
'question':'Si preguntan si una condición puede compensar a otra: no. El T17 exige su cumplimiento conjunto. El detalle numérico de disponibilidad y respuesta está en sus notas y en el protocolo.',
'source':'SD9, §9.2.1 y tabla 9.7, p. 16. T17, §4.3 y p. 12, condiciones del Art. 17.3.'},
{'slide':37,'title':'Pruebas del código al terreno','rows':[
('Desarrollo','Las pruebas unitarias y de componente comprueban reglas y partes del programa antes de conectarlas con el conjunto.'),
('Contratos de API','Revisan los acuerdos entre componentes: información enviada, formato y respuesta esperada. Ayudan a detectar cambios incompatibles.'),
('QA y regresión','QA es el ambiente de pruebas. La integración comprueba conexiones; la regresión revisa que un cambio no rompa funciones existentes.'),
('Seguridad y accesibilidad','Se revisan vulnerabilidades y posibilidades de uso. DAST prueba seguridad con la aplicación funcionando, no solo leyendo su código.'),
('Aceptación de usuario','Las personas que realizarán el trabajo prueban tareas representativas. La validación se documenta con la Contraparte Técnica.'),
('Carga y estrés','Carga comprueba la demanda definida; estrés aumenta la exigencia para observar saturación y degradación controlada, sin perder transacciones.'),
('Fallas y conectividad','Se provocan fallas y cortes para comprobar continuidad y sincronización. El escenario de un sitio y el de un terminal no son iguales.'),
('Migración y reversión','Se comprueban el traslado y la conciliación de datos, además de la instalación y el retorno a una versión anterior si hace falta.'),
('Intrusión independiente','Un tercero autorizado evalúa la seguridad antes de la entrada a Producción prevista. No sustituye los controles diarios del desarrollo.'),
('Terreno','Se revisa el uso sin señal, con frío y guantes, lluvia, calor o una mano. Estas condiciones requieren pruebas físicas y operacionales.'),
('Operación y recuperación','La marcha blanca mide indicadores con operación real. Los ejercicios de recuperación comprueban el restablecimiento del servicio y de sus datos.'),
('Automatización y datos','Se automatizan comprobaciones repetibles y se conserva evidencia por caso y ambiente. Los datos reales usados en pruebas requieren anonimización verificada.')],
'script':[
'Las pruebas avanzan desde el código hacia escenarios cercanos a la operación real. En desarrollo comprobamos reglas y componentes, además de los contratos que permiten a las aplicaciones intercambiar información. En QA verificamos integraciones y ejecutamos regresión: después de un cambio, volvemos a comprobar que lo que funcionaba siga funcionando. La revisión de seguridad y accesibilidad combina herramientas con intervención humana.',
'En preproducción participan los usuarios y se ensayan carga, estrés, fallas de conectividad, migración y reversión. La carga no se escoge arbitrariamente: se deriva del dimensionamiento documentado. El trabajo sin señal, el frío con guantes y las demás condiciones de uso se prueban en terreno. Automatizamos lo repetible; las pruebas físicas o que requieren juicio humano se programan aparte. Cada caso deja evidencia de su ambiente y resultado. Los datos de prueba deben estar protegidos, y durante la marcha blanca los indicadores se miden con operación real.'],
'question':'Si preguntan por la duración de la regresión: la estimación nocturna de las notas corresponde al bloque automatizado bajo supuestos de planificación. No incluye toda la campaña manual ni de terreno.',
'source':'SD9, tabla 9.8, p. 18; tabla 9.9 y §9.2.4, p. 20. T13, §§8.2–8.3, pp. 19–20.'},
{'slide':38,'title':'Trazabilidad y mejora','rows':[
('Trazabilidad completa','Permite seguir una necesidad desde lo pedido por Puelche hasta el requisito, el trabajo, la prueba y la aceptación.'),
('Clientes afectados en menos de dos horas','El ejemplo exige identificar a los clientes afectados por un lote. No significa retirar físicamente toda la mercadería en ese tiempo.'),
('RF 09.01 y M9','RF-09.01 identifica el requisito de trazabilidad; M9 es el módulo de calidad y trazabilidad que participa en su cumplimiento.'),
('EDT y paquete 3.4.4','La EDT divide el proyecto en trabajos controlables. El paquete 3.4.4 ubica el trabajo de cadena de frío y retiro.'),
('Simulacro de retiro','Ensaya la identificación de afectados con un lote y deja evidencia del resultado y del tiempo medido.'),
('Código e identificador','La solicitud de fusión registra qué requisito atiende el cambio. Así se puede relacionar lo construido con la necesidad original.'),
('Digest e imagen firmada','El digest es la huella de la versión exacta del software; la firma permite comprobar su origen e integridad.'),
('Acta H7','Registra la aceptación del cierre de marcha blanca de la Etapa 1. No acepta anticipadamente resultados que se medirán después.'),
('PDCA','Planificar identifica causa y responsable; hacer aplica la corrección; verificar repite el criterio; actuar cierra o ajusta con evidencia.'),
('Control y causa raíz','Los diagramas de control muestran variaciones en el tiempo. Pareto ayuda a priorizar problemas; causa raíz busca por qué ocurren.'),
('Prevención','Es preparar procesos y controles para reducir la aparición de errores. Su programación no es una promesa de ausencia de fallas.'),
('Evaluación','Es revisar, probar y documentar el cumplimiento. El esfuerzo de prevención y evaluación no representa por sí solo el costo integral de calidad.')],
'script':[
'La trazabilidad permite demostrar que lo entregado responde a una necesidad de Puelche. En el ejemplo, identificar clientes afectados por un lote se vincula con el requisito RF-09.01, el módulo de calidad y trazabilidad, el paquete de trabajo y el simulacro que lo comprueba. Al incorporar el cambio de código registramos el identificador del requisito, y el digest de la imagen permite reconocer la versión exacta que se desplegó. Así relacionamos la prueba con lo que recibió el cliente.',
'Cuando una medición se desvía, aplicamos el ciclo de mejora: analizamos la causa y asignamos responsable, corregimos, repetimos la verificación con el mismo criterio y cerramos o ajustamos según la evidencia. Pareto ayuda a priorizar y los diagramas de control permiten observar variaciones del proceso. El esfuerzo de calidad incluye preparar controles para prevenir y ejecutar revisiones para evaluar. No se limita a probar al final, ni equivale a presupuestar como monto cerrado todas las fallas futuras.'],
'question':'Si preguntan por las horas retiradas de la lámina: corresponden a conformidad programada, obtenida de paquetes y roles de prevención y evaluación. No son el costo integral de calidad. Consultar notas y tabla 9.6.',
'source':'SD9, tabla 9.6, p. 14, y §§9.2.5–9.2.6, figuras 9.6–9.8. T17, §5, p. 12, para el alcance del ejemplo.'},
{'slide':50,'title':'Innovaciones con evaluación','rows':[
('Seguimiento posentrega','Agrega seguimiento al vencimiento en el local. El preventista recibe avisos, confirma el riesgo y aplica acciones autorizadas; se evalúan acierto y vencimiento frente a la base.'),
('Reproducción de incidentes','Reúne evidencia protegida para reconstruir una falla de terreno en pruebas. Se compara el tiempo hasta reproducir la causa en casos equivalentes.'),
('Vida útil por historia térmica','Usa temperatura y tiempo para apoyar a Calidad. La estimación se valida por familia y no amplía la fecha impresa ni elimina bloqueos térmicos.'),
('Pago ligado al costo de servir','Propone un tramo variable condicionado a la mejora del costo comparable y al servicio. Finanzas debe poder reproducir el cálculo.'),
('OTIF y comparación','OTIF mide entregas completas y a tiempo. Una reducción aparente del costo no cuenta si se degrada el servicio o cambia indebidamente la referencia.'),
('Hoja del almacenero','Devuelve información de sus compras en el terminal del preventista, sin exigir dispositivo ni internet al local. La copia solicitada se entrega por Reparto posteriormente.'),
('Cómo se evalúan','Se revisan acierto, diagnóstico, concordancia con Calidad, costo comparable y servicio, y comprensión y cobertura de la hoja. Cada indicador tiene condiciones y momento.'),
('Metas y resultados','Las metas se mantienen en la oferta, pero no son beneficios ya demostrados. La medición debe distinguir la habilitación de una innovación del ahorro posterior.')],
'script':[
'Las innovaciones agregan capacidades al alcance obligatorio y cada una tiene una forma de evaluación. El seguimiento posentrega avisa al preventista de productos que podrían vencer en el local, para confirmar el riesgo y aplicar una acción autorizada. La reproducción de incidentes reúne evidencia protegida para reconstruir la causa en pruebas y comparar el tiempo de diagnóstico en casos equivalentes. La historia térmica utiliza temperatura y tiempo para apoyar decisiones de Calidad; sus parámetros se validan por familia y no extienden la fecha impresa ni modifican los bloqueos.',
'En el modelo de negocio proponemos que un tramo variable del pago dependa del costo comparable por entrega, condicionado al nivel de servicio. El cálculo debe poder reproducirse con Finanzas: ahorrar empeorando las entregas no cuenta. La hoja del almacenero devuelve información útil en el terminal del preventista o mediante una copia solicitada, sin exigir conexión al local. Evaluamos comprensión, cobertura y uso. Las metas permanecen en la oferta con sus condiciones de medición; no las presentamos como ahorros ya observados.'],
'question':'Si preguntan de dónde sale un porcentaje: es la meta de diseño ofertada, no una medición previa. Consultar el indicador, su línea base y su momento de verificación en las notas; no inventar un cálculo que la justifique.',
'source':'SD13, tablas 13.5, p. 15; 13.10, p. 23; 13.15, p. 32; 13.21, p. 40; 13.26, p. 47. T19, fichas 1–5.'}
]

canonical={'ISO IEC 25010':'ISO/IEC 25010','ISO IEC 25012':'ISO/IEC 25012','ISO IEC IEEE 29119':'ISO/IEC/IEEE 29119','CMMI DEV N3':'CMMI-DEV N3','RF 09.01 y M9':'RF-09.01 y M9'}
for page in pages:page['rows']=[(canonical.get(a,a),b) for a,b in page['rows']]
with zipfile.ZipFile(SOURCE) as z:
    infos=z.infolist();data={i.filename:z.read(i.filename) for i in infos}
doc=E.fromstring(data['word/document.xml']);body=doc.find('w:body',ns)
pars=body.findall('w:p',ns);tables=body.findall('w:tbl',ns)
def contents(p):return ''.join(p.xpath('.//w:t/text()',namespaces=ns))
heading=next(p for p in pars if contents(p)=='Diapositiva 34')
sub=next(p for p in pars if contents(p)=='Normas y leyes')
intro=next(p for p in pars if contents(p).startswith('Numeración'))
guionh=next(p for p in pars if contents(p)=='Guion para exponer')
normal=next(p for p in pars if contents(p).startswith('El plan de calidad'))
sourcep=next(p for p in pars if contents(p).startswith('Base documental'))
section=deepcopy(body.find('w:sectPr',ns))
def ptext(template,value,bold=None,size=None):
    p=deepcopy(template)
    rp=p.find('w:r/w:rPr',ns);rp=deepcopy(rp) if rp is not None else E.Element(q('rPr'))
    for n in ['strike','dstrike','color']:
        for e in rp.findall('w:'+n,ns):rp.remove(e)
    E.SubElement(rp,q('color'),{q('val'):'000000'})
    if bold is not None:
        for e in rp.findall('w:b',ns):rp.remove(e)
        E.SubElement(rp,q('b'),{q('val'):'1' if bold else '0'})
    if size is not None:
        for n in ['sz','szCs']:
            for e in rp.findall('w:'+n,ns):rp.remove(e)
            E.SubElement(rp,q(n),{q('val'):str(round(size*2))})
    for child in list(p):
        if child.tag!=q('pPr'):p.remove(child)
    r=E.SubElement(p,q('r'));r.append(rp);E.SubElement(r,q('t')).text=value
    return p
def pp(p):
    prop=p.find('w:pPr',ns)
    if prop is None:prop=E.Element(q('pPr'));p.insert(0,prop)
    return prop
def table(rows,template):
    t=deepcopy(template);old=t.findall('w:tr',ns);rt=deepcopy(old[1])
    for r in old[1:]:t.remove(r)
    for values in rows:
        row=deepcopy(rt)
        for cell,value in zip(row.findall('w:tc',ns),values):
            p=cell.find('w:p',ns);new=ptext(p,value)
            for e in list(cell):
                if e.tag!=q('tcPr'):cell.remove(e)
            cell.append(new)
        trpr=row.find('w:trPr',ns)
        if trpr is None:trpr=E.Element(q('trPr'));row.insert(0,trpr)
        E.SubElement(trpr,q('cantSplit'))
        t.append(row)
    head=t.find('w:tr',ns);trpr=head.find('w:trPr',ns)
    if trpr is None:trpr=E.Element(q('trPr'));head.insert(0,trpr)
    E.SubElement(trpr,q('tblHeader'))
    return t
for el in list(body):body.remove(el)
for j,page in enumerate(pages):
    if j==0:
        p=ptext(heading,'Guía de exposición SD9 y SD13',True,16)
        style=pp(p).find('w:pStyle',ns)
        if style is None:style=E.SubElement(pp(p),q('pStyle'))
        style.set(q('val'),'Title');body.append(p)
    h=ptext(heading,f'Diapositiva {page["slide"]}',True)
    # One slide per page, preserving the six-page quick-reference structure.
    if j:E.SubElement(pp(h),q('pageBreakBefore'))
    body.append(h);body.append(ptext(sub,page['title'],True))
    if j==0:body.append(ptext(intro,'Guía actualizada para las posiciones reales 34–38 y 50. La tabla es para consultas; el guion es para exponer. Las cifras detalladas siguen en las notas del PPT.',False,10))
    body.append(table(page['rows'],tables[j]))
    body.append(ptext(guionh,'Guion para exponer',True))
    for value in page['script']:body.append(ptext(normal,value,False))
    body.append(ptext(guionh,'Si el cliente pregunta',True))
    body.append(ptext(normal,page['question'],False,10))
    body.append(ptext(sourcep,'Base documental: '+page['source'],False))
body.append(section)
for e in doc.xpath('//w:strike|//w:dstrike',namespaces=ns):e.getparent().remove(e)
data['word/document.xml']=E.tostring(doc,xml_declaration=True,encoding='UTF-8',standalone=True)
with zipfile.ZipFile(OUT,'w') as z:
    for info in infos:z.writestr(info,data[info.filename])
with zipfile.ZipFile(SOURCE) as a,zipfile.ZipFile(OUT) as b:
    assert all(a.read(n)==b.read(n) for n in a.namelist() if n!='word/document.xml')
assert not doc.xpath('//w:strike',namespaces=ns)
assert len(body.findall('w:tbl',ns))==6
report={'source':str(SOURCE),'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'ppt':str(PPT),'ppt_sha256':hashlib.sha256(PPT.read_bytes()).hexdigest(),'output':str(OUT),'slides':[p['slide'] for p in pages],'script_words':{p['slide']:len(' '.join(p['script']).split()) for p in pages},'changed_parts':['word/document.xml']}
(ROOT/'tmp/guia_actualizada/build_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(report,ensure_ascii=False,indent=2))
