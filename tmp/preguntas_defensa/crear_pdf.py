from pathlib import Path
import re, json
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'output' / 'pdf'
OUT.mkdir(parents=True, exist_ok=True)
BUILD = ROOT / 'tmp' / 'pdfs' / 'preguntas_defensa'
BUILD.mkdir(parents=True, exist_ok=True)

DATA = [
{'sd':1,'title':'Empresa y equipo','slides':'2 y 30','source':'LAFROX-Subdocumento1.pdf','items':[
('2','El equipo','¿Por qué deberíamos elegir a LafroX para una operación como la nuestra?','Nuestra propuesta se apoya en experiencia declarada en logística, trazabilidad y operación con conectividad intermitente. Además, asignamos responsables para construcción, seguridad, calidad y operación. Esas capacidades deben acreditarse con los antecedentes y referencias de la oferta, no solamente con esta presentación.'),
('2','El equipo','Las bases piden diez roles y ustedes presentan ocho personas. ¿Faltan integrantes?','Cubrimos los diez roles con ocho responsables. Bastián Trejo asume Arquitectura e Integración y Patricio Henríquez, Funcional e Implantación. Esto no significa asignar dos jornadas completas a una persona. El plan contempla equipos de apoyo y separar Implantación si la carga lo requiere.'),
('2 y 30','Responsabilidad durante la operación','¿Quién responde cuando el sistema ya está funcionando y ocurre un problema?','Alex Aravena mantiene la responsabilidad de dirección e interlocución con Puelche. Guillermo Castillo lidera la operación y el escalamiento técnico. Calidad y Seguridad mantienen sus responsabilidades durante el contrato, por lo que la responsabilidad de LafroX continúa después de implementar.')
]},
{'sd':2,'title':'Problema y necesidad','slides':'3, 4 y 50','source':'LAFROX-Subdocumento2.pdf','items':[
('4','Problemática','¿Por qué aseguran que problemas sanitarios, comerciales y financieros tienen una misma causa?','Porque los tres dependen de hechos que hoy no quedan registrados oportunamente. Sin lote se pierde trazabilidad; sin información confiable de pedidos y entregas se deteriora el servicio; y sin tiempos, recorridos y devoluciones por entrega no podemos calcular correctamente el costo de servir.'),
('3 y 4','Diagnóstico del retiro','¿El 41 % significa que casi la mitad de todas nuestras recepciones no tenía lote?','No. Ese porcentaje corresponde al producto involucrado en el retiro, no al conjunto de recepciones de Puelche. Lo usamos como evidencia de esa brecha específica. La solución exige lote en los productos que lo requieren, sin generalizar incorrectamente el diagnóstico.'),
('3 y 50','De nueve días a menos de dos horas','¿Nos están prometiendo retirar físicamente todos los productos en menos de dos horas?','No. El compromiso es identificar a los clientes afectados por un lote en menos de dos horas. El retiro físico requiere coordinación logística posterior. La identificación se comprobará mediante un simulacro cronometrado y evidencia revisada por Puelche.')
]},
{'sd':3,'title':'Solución y alcance','slides':'5 y 6','source':'LAFROX-Subdocumento3.pdf','items':[
('5 y 6','Solución e integración','¿Van a reemplazar nuestro ERP?','No. El ERP se conserva como registro contable y único emisor tributario. LafroX incorpora la gestión logística y le entrega la información necesaria mediante una integración controlada. No tendremos dos sistemas emitiendo documentos tributarios para una misma operación.'),
('6','Mapa de módulos','¿Qué recibiremos en cada etapa?','La primera etapa cubre la operación fundamental: preventa, recepción, inventario, preparación, rutas, reparto, rendición y trazabilidad. La segunda incorpora el portal de clientes, el intercambio electrónico del canal moderno y el costo de servir. M10 entrega indicadores como OTIF desde la primera etapa y amplía su alcance después.'),
('5 y 6','Alcance para el almacenero','¿Nuestros clientes tendrán que comprar teléfonos, contratar internet o dejar de pagar en efectivo?','No. El canal tradicional puede seguir siendo atendido mediante el preventista y el repartidor. El portal es opcional para ese canal y el efectivo sigue contemplado. La captura digital se realiza con las herramientas de la operación, sin trasladar esa obligación al almacenero.'),
('6','Límites del alcance','Ya que integrarán a los transportistas, ¿también administrarán sus contratos y pagos?','No. Integramos su participación operacional, pero la administración contractual y sus pagos quedan fuera del alcance. También se excluyen la sustitución del ERP y la adquisición del hardware de terreno. Puelche compra ese equipamiento y LafroX especifica sus características y cantidades.')
], 'note':'Ojo para el ensayo: no repitan literalmente la nota que dice que “solo M11 espera a la Etapa 2”. El informe también ubica el portal de clientes y el costo de servir en esa etapa.'},
{'sd':4,'title':'Arquitectura','slides':'5, 7, 11 a 16','source':'LAFROX-Subdocumento4.pdf','items':[
('7 y 16','Arquitectura híbrida','¿Por qué necesitamos componentes locales si estamos contratando una solución en la nube?','Porque recepción, preparación y despacho deben continuar cuando se corta el enlace. Los componentes locales sostienen esas operaciones y conservan sus registros. La nube concentra las capacidades centrales y la consolidación, pero no constituye una dependencia obligatoria para cada transacción local.'),
('11','Lógica de negocio','¿Por qué eligieron un monolito modular y no microservicios?','Buscamos una complejidad operativa proporcionada al volumen y al equipo de Puelche. El monolito modular mantiene separados los dominios sin multiplicar servicios que administrar. Sincronización, EDI y telemetría cuentan con trabajadores y capacidad de escalamiento independientes cuando lo necesitan.'),
('12','Integración y eventos','¿Cómo evitan que un pedido o cobro se duplique cuando vuelve la conexión?','Cada operación conserva un identificador único durante sus reintentos. El receptor reconoce lo que ya procesó y evita repetir su efecto. Los conflictos se resuelven con reglas de negocio y auditoría, no simplemente aceptando el dato con la hora más reciente.'),
('5, 12 y 16','Trabajo sin conexión','¿Trabajar sin señal significa que todas las sedes tendrán información actualizada en tiempo real?','No. Podemos conservar y ejecutar las operaciones autorizadas localmente, pero la consolidación central queda pendiente hasta reconectar. Diferenciamos una operación confirmada en su sitio de una copia central actualizada. Tampoco prometemos conocer instantáneamente hechos que siguen aislados en un dispositivo sin comunicación.'),
('16','Continuidad','¿Qué diferencia hay entre RTO de cuatro horas y RPO de quince minutos?','RTO es el tiempo objetivo para recuperar los servicios críticos. RPO limita la antigüedad del punto de datos recuperable. Recuperar rápido no basta si se pierden demasiados datos, y conservar los datos tampoco basta si el servicio tarda demasiado en volver. Ambos objetivos requieren ensayos.'),
('14 y 15','Seguridad y observabilidad','Si alguien usa indebidamente una cuenta autorizada, ¿cómo lo detectarán?','La autorización limita las acciones posibles y la auditoría permite reconstruir quién hizo qué. La observabilidad correlaciona solicitudes y eventos para investigar comportamientos anómalos. Estos controles se complementan con supervisión de seguridad, pruebas y procedimientos de contención. Una cuenta válida no elimina el riesgo de abuso.')
]},
{'sd':5,'title':'Datos y migración','slides':'5, 6, 13 y 36 (transversal)','source':'LAFROX-Subdocumento5.pdf','intro':'Este subdocumento no tiene una diapositiva exclusiva en la versión actual. Sus preguntas se relacionan con el esquema, la arquitectura de datos y las pruebas.','items':[
('5 y 13','Trazabilidad de los datos','¿Cómo podrán saber qué cliente recibió un lote específico?','Vinculamos el lote recibido con sus movimientos, las asignaciones de preparación y las líneas efectivamente entregadas. Así podemos seguir cantidades y destinos, incluso cuando un pedido utiliza varios lotes. La trazabilidad depende de registrar esa cadena, no de guardar solamente el número de lote.'),
('13 y 36','Migración','¿Qué harán si los datos antiguos no tienen lote o contienen información contradictoria?','No inventaremos información para completar campos. Preservaremos el original, aplicaremos correcciones aprobadas cuando exista fundamento y aislaremos lo que requiera decisión de Puelche. Los registros no resueltos deben mantener su procedencia y no presentarse como información confiable ya saneada.'),
('13 y 36','Conciliación','¿Cómo demostrarán que la migración quedó bien?','Conciliamos el universo mediante recuentos, claves, importes, cantidades y saldos según corresponda. Cada diferencia necesita causa, evidencia y aprobación. El criterio es cero diferencias sin explicar. Un muestreo puede complementar esos controles, pero no reemplaza la conciliación completa.'),
('6 y 13','Indicadores','¿Cómo evitaremos que el OTIF mejore artificialmente cambiando las fechas prometidas?','Conservamos la promesa original y registramos las reprogramaciones como revisiones, con motivo y autorización. Así no se borra el compromiso inicial para mejorar el indicador. También distinguimos pedidos de intentos de entrega para no alterar el resultado contando visitas como pedidos distintos.')
]},
{'sd':6,'title':'Metodologías','slides':'17 y 18','source':'LAFROX-Subdocumento6.pdf','items':[
('17 y 18','PMBOK, RUP y DevSecOps','¿Por qué mezclan tantas metodologías? ¿No complicará la ejecución?','Cada una cumple una función distinta. PMBOK organiza compromisos y control del proyecto; RUP estructura el desarrollo iterativo; DevSecOps incorpora controles en cada cambio. Kanban hace visible el trabajo cotidiano. No utilizamos el tablero ni una demostración como sustitutos de la aceptación contractual.'),
('17','Seguimiento','¿Cómo sabremos que realmente avanzan y no que solo están consumiendo horas?','Medimos avance contra entregables y evidencia, mediante valor ganado. Comparamos lo logrado con lo planificado y con el esfuerzo consumido. Si SPI o CPI baja de 0,90, corresponde analizar la desviación y gestionar acciones, en lugar de seguir reportando porcentajes subjetivos.'),
('17 y 18','Cambios','Si durante el proyecto pedimos una nueva funcionalidad, ¿la incorporarán en la siguiente iteración?','Primero evaluaremos su impacto. Si modifica alcance, fechas o recursos aprobados, requiere el procedimiento formal de cambio. Las iteraciones permiten desarrollar y validar incrementos, pero no autorizan a modificar compromisos contractuales unilateralmente.')
]},
{'sd':7,'title':'Plan de trabajo, recursos e implantación','slides':'19 a 22, 26, 31 y 32','source':'LafroX-Subdocumento7.pdf; LafroX-Formulario-T-15.pdf (cálculo de esfuerzo)','items':[
('19 y 22','Organización del trabajo','¿Por qué presentan dos etapas, ocho frentes y nueve fases? ¿Cuál es la estructura real?','Son perspectivas complementarias. Las etapas ordenan las entregas contractuales. Los frentes distribuyen responsabilidades y trabajo paralelo. Las nueve fases de la EDT descomponen el alcance en cuentas de control y paquetes. No son tres cronogramas distintos ni corresponde sumar sus esfuerzos entre sí.'),
('20, 21 y 26','Implantación','¿Cómo cambiarán el sistema sin detener nuestra operación?','La implantación será progresiva por olas, con pruebas, capacitación, conciliación y reversión ensayada antes de habilitar cada perímetro. La marcha blanca utiliza operación real bajo supervisión. El avance depende de criterios de habilitación, no solamente de que llegue una fecha del calendario.'),
('20 y 21','Congelamientos','¿Qué pasa si el mes contractual de salida a producción coincide con septiembre o diciembre?','No podemos resolverlo moviendo unilateralmente un hito obligatorio ni ignorando el congelamiento. La fecha de inicio debe ser compatible con ambas restricciones. Si aparece una incompatibilidad, corresponde plantearla formalmente al mandante. Los meses calendario dibujados en el Gantt dependen del inicio supuesto.'),
('22 y 32','Esfuerzo total','¿De dónde salen las 217.543 horas? ¿Son solamente horas de programación?','No. Incluyen los paquetes de trabajo y componentes adicionales de restauraciones, soporte puente y reserva protegida. Cubren gestión, infraestructura, pruebas, capacitación y operación, además del desarrollo. El T-15 reconcilia esos componentes; no corresponde interpretar el total como programación.'),
('32','Máximo de recursos','¿Las 69 personas del mes 15 ya están disponibles y comprometidas?','La cifra representa personas equivalentes de demanda programada durante el solape de etapas. Por sí sola no demuestra disponibilidad nominal. Para acreditar capacidad debemos contrastar perfiles, dedicaciones, turnos y compromisos, sin presentar la curva de esfuerzo como si fuera una nómina contratada.'),
('20, 21 y 32','Viabilidad del calendario','¿Pueden demostrar que la ruta crítica sigue siendo válida con las horas actuales?','El propio informe advierte que las referencias históricas de ruta crítica y probabilidades requieren recálculo con la línea base actual. No las presentaríamos como una demostración vigente. Debemos actualizar dependencias, duraciones y recursos antes de acreditar la viabilidad del calendario.'),
('31','Cierre y reversibilidad','¿Qué ocurre si al terminar el contrato queremos cambiar de proveedor?','El plan contempla una salida ordenada y transferencia al término del contrato. La reversibilidad se prepara desde el inicio y se ejecuta en el cierre, con datos, documentación y procedimientos. No depende únicamente de que la tecnología utilizada sea abierta.')
]},
{'sd':8,'title':'Riesgos','slides':'38 a 48','source':'LafroX-Subdocumento8.pdf','items':[
('38 y 47','Prioridades','De los 45 riesgos, ¿cuáles atenderían primero y por qué?','Los dos críticos son la trazabilidad incompleta ante un retiro y la recuperación fuera de RTO/RPO. Ambos comprometen resultados esenciales de Puelche. Sus respuestas incluyen simulacros de retiro y recuperación. También controlamos riesgos habilitantes, como duplicación de eventos, energía y conectividad.'),
('47 y 48','Exposición','Si un riesgo tiene exposición 0,40, ¿significa que tiene un 40 % de probabilidad de ocurrir?','No. El 0,40 resulta del producto de ponderaciones cualitativas de probabilidad e impacto y sirve para priorizar. La estimación porcentual utilizada para calcular esfuerzo esperado es otra variable. Confundirlas produciría una interpretación incorrecta del riesgo y de las reservas.'),
('39 y 47','Reservas','¿Las 2.058,5 horas garantizan que cualquier problema quedará cubierto?','No. Son una estimación de contingencia basada en probabilidad por impacto condicional en horas de los riesgos identificados. No constituyen una garantía ni un monto monetario. Las 1.600 horas de gestión son un supuesto separado, con autorización y tratamiento propios.'),
('40 a 47','Mitigación','Si todos tienen una respuesta, ¿por qué siguen existiendo riesgos altos y críticos?','Porque definir una respuesta no demuestra que haya funcionado. La reducción del riesgo exige ejecutar el control y comprobar su eficacia. Hasta entonces, la valoración residual es un objetivo condicionado. Tampoco podemos aceptar un riesgo para dejar de cumplir un requisito obligatorio.')
]},
{'sd':9,'title':'Calidad, pruebas y aceptación','slides':'26 y 33 a 36','source':'LAFROX-Subdocumento9.pdf; LAFROX-Formulario-T-17.pdf (aceptación)','items':[
('33','Normas','¿Qué aportan concretamente esas normas? Nombrarlas no demuestra calidad.','Correcto. ISO 25010 organiza los criterios del producto; ISO 25012, los datos; e ISO 29119, las pruebas. WCAG y OWASP apoyan controles de accesibilidad y seguridad. Su aplicación debe dejar resultados verificables: pruebas, conciliaciones, evaluaciones e informes. La referencia por sí sola no acredita cumplimiento.'),
('34','Desempeño','¿Prometen que ninguna transacción tardará más de un segundo?','No. El umbral de un segundo corresponde al percentil 95 de preparación, bajo las condiciones de prueba establecidas. Otros flujos tienen umbrales diferentes. No es un máximo absoluto para todas las transacciones ni una cifra que podamos dar por lograda antes de medirla.'),
('35','Aceptación','Si el sistema funciona, ¿por qué no podemos aceptar inmediatamente la marcha blanca?','Porque la aceptación exige conjuntamente ausencia de incidentes críticos o altos atribuibles, volumen real comprometido, continuidad y desempeño, conciliación, usuarios certificados y acta de la contraparte. Una demostración funcional o una firma no compensan una condición incumplida.'),
('26 y 35','Producción y marcha blanca','¿Cómo puede haber datos reales en Producción desde el mes 13 si el paso a producción es en el mes 16?','Distinguimos la habilitación técnica del ambiente para operar la marcha blanca, mediante G5, de la aceptación contractual de su cierre. H6 y H11 habilitan operación supervisada; H7 y H12 corresponden al paso contractual y su aceptación. Son decisiones diferentes.'),
('35','Incumplimiento','¿Qué pasa si al finalizar la marcha blanca queda una condición pendiente?','No solicitaremos aceptarla como si estuviera cumplida. Según el protocolo, la marcha blanca se extiende a costo de LafroX sin desplazar las fechas siguientes. Debemos corregir, volver a verificar y presentar evidencia. Una condición satisfecha no compensa otra que falla.'),
('36','Pruebas','¿Cómo probarán situaciones reales como frío, guantes y pérdida de señal?','El plan incluye pruebas de terreno, operación a −22 °C con guantes, autonomía sin conexión y sincronización posterior. También contempla carga, recuperación y reversión. Una prueba de interfaz en oficina no sustituye esos escenarios, y cada ejecución debe conservar resultados y evidencia.'),
('36','Catálogo y automatización','¿Los 1.316 casos ya fueron ejecutados? ¿Todos se prueban automáticamente durante la noche?','No. Es un catálogo inicial estimado. El 80 % de automatización es un parámetro de diseño, no un resultado alcanzado. La ejecución automática nocturna no incluye toda la campaña manual, que requiere esfuerzo adicional. Tampoco una cobertura alta demuestra ausencia de errores.')
]},
{'sd':13,'title':'Innovaciones','slides':'37','source':'LAFROX-Subdocumento13.pdf','items':[
('37','Seguimiento posentrega','¿Cómo sabrán qué está por vencer en el almacén si no tienen acceso a sus ventas?','Utilizamos entregas, devoluciones e historial de reposición para estimar, y el preventista confirma la situación durante la visita. Reposición no equivale a venta al consumidor. Si faltan datos, mostramos la información disponible sin simular una predicción ni incorporarla al inventario oficial.'),
('37','Reproducción de incidentes','¿Pueden garantizar una reducción del 30 % en todos los incidentes?','No para cada incidente. La meta se refiere a una reducción relativa de la mediana del tiempo de diagnóstico en casos comparables. Debemos medirla con el diseño de comparación de la oferta. Todavía no corresponde presentarla como un beneficio demostrado.'),
('37','Vida útil por historia térmica','¿El sistema podría autorizar vender después del vencimiento impreso?','No. La estimación apoya a Calidad y no extiende la fecha impresa ni elimina bloqueos térmicos. Requiere validación por familia antes de habilitar su uso. Si no acredita el desempeño exigido, no debemos utilizarla como fundamento de decisiones de disposición.'),
('37','Pago ligado al costo de servir','¿Podrían reducir costos empeorando nuestras entregas y aun así cobrar el incentivo?','El tramo variable está condicionado al nivel de servicio. La propuesta exige contrastar el costo sobre una base comparable y mantener OTIF de al menos 95 %. Así buscamos evitar premiar un ahorro aparente obtenido deteriorando las entregas. La fórmula tampoco demuestra anticipadamente que el ahorro se logrará.'),
('37','Hoja del almacenero','¿Qué tiene de útil esta innovación si el almacenero no tiene internet?','La información se muestra en el terminal del preventista y puede solicitarse una copia para la siguiente entrega. No exige dispositivo propio ni conexión del local. Su utilidad debe comprobarse mediante comprensión, cobertura y uso; no prometemos automáticamente un aumento de compras.')
]}
]

for name, file in [('Arial','arial.ttf'),('Arial-Bold','arialbd.ttf'),('Arial-Italic','ariali.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(Path('C:/Windows/Fonts')/file)))
pdfmetrics.registerFontFamily('Arial',normal='Arial',bold='Arial-Bold',italic='Arial-Italic',boldItalic='Arial-Bold')
INK=colors.HexColor('#18232D'); MUTED=colors.HexColor('#526170'); ORANGE=colors.HexColor('#C75A24'); LINE=colors.HexColor('#D8DFE4')
ST={
 'title':ParagraphStyle('title',fontName='Arial-Bold',fontSize=30,leading=35,textColor=INK,spaceAfter=15),
 'deck':ParagraphStyle('deck',fontName='Arial',fontSize=12,leading=18,textColor=MUTED,spaceAfter=13),
 'h1':ParagraphStyle('h1',fontName='Arial-Bold',fontSize=19,leading=23,textColor=INK,spaceAfter=6),
 'h2':ParagraphStyle('h2',fontName='Arial-Bold',fontSize=13,leading=17,textColor=INK,spaceBefore=13,spaceAfter=8),
 'meta':ParagraphStyle('meta',fontName='Arial-Bold',fontSize=9,leading=11,textColor=ORANGE,spaceAfter=3),
 'q':ParagraphStyle('q',fontName='Arial-Bold',fontSize=10.5,leading=13.2,textColor=INK,spaceAfter=4),
 'a':ParagraphStyle('a',fontName='Arial',fontSize=10.3,leading=13,textColor=INK,spaceAfter=0),
 'body':ParagraphStyle('body',fontName='Arial',fontSize=10.3,leading=15,textColor=INK,spaceAfter=8),
 'small':ParagraphStyle('small',fontName='Arial',fontSize=8.2,leading=11,textColor=MUTED,spaceAfter=8),
 'note':ParagraphStyle('note',fontName='Arial-Italic',fontSize=9.3,leading=13,textColor=MUTED,spaceBefore=8,spaceAfter=8),
 'cell':ParagraphStyle('cell',fontName='Arial',fontSize=9.2,leading=13,textColor=INK),
}
def P(t, kind='body'): return Paragraph(escape(t),ST[kind])
W,H=A4
LM=RM=45; TM=53; BM=43
usable=W-LM-RM

class GuideDoc(SimpleDocTemplate):
    def afterFlowable(self, f):
        if hasattr(f,'section_id'):
            key=f'sd{f.section_id}'
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(f'Subdocumento {f.section_id}: {f.section_title}',key,0,False)
            self.section_pages[f.section_id]=self.page

def decor(c,doc):
    c.saveState()
    c.setStrokeColor(ORANGE);c.setLineWidth(1.5);c.line(LM,H-31,W-RM,H-31)
    c.setFont('Arial-Bold',8);c.setFillColor(INK);c.drawString(LM,H-24,'LafroX')
    c.setFont('Arial',8);c.setFillColor(MUTED);c.drawRightString(W-RM,H-24,'Informe 2 / Guía de defensa')
    c.setStrokeColor(LINE);c.setLineWidth(.5);c.line(LM,32,W-RM,32)
    c.setFont('Arial',7.7);c.setFillColor(MUTED);c.drawString(LM,20,'Juego de roles: LafroX ante Distribuidora Puelche S.A.')
    c.drawRightString(W-RM,20,f'{doc.page}')
    c.restoreState()

def front(pages):
    s=[Spacer(1,14),P('Preguntas para defender\nla propuesta'.replace('\n',' '),'title'),
       P('46 preguntas y respuestas modelo, organizadas por subdocumento y diapositiva.','deck'),
       P('Juego de roles: ustedes representan a LafroX y el profesor actúa como contraparte de Puelche. Las respuestas distinguen compromisos, estimaciones y resultados todavía no demostrados.'),
       P('Ruta rápida de consulta','h2')]
    rows=[[P('Subdocumento','meta'),P('Diapositivas relacionadas','meta'),P('Página','meta')]]
    for sec in DATA:
        rows.append([P(f"{sec['sd']}. {sec['title']}",'cell'),P(sec['slides'],'cell'),P(str(pages.get(sec['sd'],'-')),'cell')])
    t=Table(rows,colWidths=[287,176,42],hAlign='LEFT')
    t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),('LINEBELOW',(0,0),(-1,0),.6,LINE),('LINEBELOW',(0,1),(-1,-1),.3,LINE)]))
    s += [t,Spacer(1,13),P('Cómo responder en el juego de roles','h2'),P('Respuesta directa + mecanismo + evidencia + límite.','q'),
          P('“Sí, la bodega puede continuar sin enlace porque confirma las operaciones autorizadas localmente. Lo comprobaremos mediante un ensayo de corte y conciliación posterior. Eso no significa que la información central permanezca actualizada en tiempo real”.','note'),
          P('Eviten “lo pusimos porque lo pedían” o “eso lo hizo otro compañero”. Si deben derivar: “Nuestro responsable de Datos puede precisar la conciliación; como LafroX, el compromiso es no aceptar diferencias sin explicar”.'),
          P('Referencia: presentación actual de 50 diapositivas, “LafroX - Informe 2 - plan de calidad resumido.pptx”, y subdocumentos del Informe 2. Numeración por posición en el archivo. Preparado el 22 de octubre de 2026.','small')]
    return s

def make_story(pages):
    story=front(pages)
    num=0
    for sec in DATA:
        story.append(PageBreak())
        h=P(f"Subdocumento {sec['sd']}",'h1');h.section_id=sec['sd'];h.section_title=sec['title']
        story += [h,P(sec['title'],'deck')]
        if sec.get('intro'):story += [P(sec['intro'],'note')]
        for slide,topic,q,a in sec['items']:
            num+=1
            label='Diapositiva' if re.fullmatch(r'\d+',slide) else 'Diapositivas'
            pair=[P(f'{num:02d}  /  {label} {slide}  /  {topic}','meta'),P(q,'q'),P('Respuesta: '+a,'a'),Spacer(1,8)]
            story.append(KeepTogether(pair))
        if sec.get('note'):story.append(P(sec['note'],'note'))
        story += [Spacer(1,4),P('Respaldo: '+sec['source'],'small')]
    assert num==46
    return story

path=OUT/'LafroX_Preguntas_y_respuestas_defensa_Informe_2.pdf'
pages={}
for run in range(2):
    doc=GuideDoc(str(path),pagesize=A4,rightMargin=RM,leftMargin=LM,topMargin=TM,bottomMargin=BM,title='LafroX - Preguntas y respuestas para la defensa del Informe 2',author='LafroX',subject='46 preguntas por subdocumento y diapositiva para juego de roles',allowSplitting=1)
    doc.section_pages={}
    doc.build(make_story(pages),onFirstPage=decor,onLaterPages=decor)
    pages=doc.section_pages

(BUILD/'contenido.json').write_text(json.dumps(DATA,ensure_ascii=False,indent=2),encoding='utf-8')
(BUILD/'paginas_secciones.json').write_text(json.dumps(pages,indent=2),encoding='utf-8')
print(json.dumps({'pdf':str(path),'section_pages':pages,'questions':46},ensure_ascii=False))
