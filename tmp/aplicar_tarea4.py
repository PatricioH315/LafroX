from pathlib import Path
import re,json,hashlib
root=Path(__file__).resolve().parents[1]
bp=root/'tmp/tarea4-baseline.json'
if bp.exists(): raise SystemExit('Tarea 4 ya aplicada; no repetir.')
paths=['08_plan_riesgos/contenido.tex','LAFROX-Subdocumento8-Anexos.tex','LAFROX-Formulario-T-16.tex']
before={p:(root/p).read_text(encoding='utf-8') for p in paths}
sources=[('S4','Subdocumento_4/LAFROX-Subdocumento4.pdf'),('S7','Subdocumento_7/LAFROX-Subdocumento7.pdf'),('T14','Subdocumento_7/LAFROX-Formulario-T-14.pdf'),('T15','Subdocumento_7/LAFROX-Formulario-T-15.pdf'),('S13','Subdocumento_13/LAFROX-Subdocumento13.pdf')]
sourcebase=root.parent/'Informe propuesta tecnica/Informe_2_LafroX'
sourcehash={p:hashlib.sha256((sourcebase/p).read_bytes()).hexdigest() for _,p in sources}
bp.write_text(json.dumps({'original':before,'source_hashes':sourcehash},ensure_ascii=False,indent=2),encoding='utf-8')
b,a,t=[before[p] for p in paths]
newresponses={
'R-016': 'Solicitar al Gerente de Operaciones y al planificador confirmación de retiro y disponibilidad V-14 al cierre del mes 1; transferir y validar reglas con el ayudante en meses 1--3. Probar las rutas y excepciones sin el planificador en la marcha blanca de meses 13--15 (S7, 7.2.1). Si falta respuesta o se retira antes, escalar por CT y reconstruir con ayudante e historia verificable, sin dar por validadas reglas pendientes.',
'R-018': 'Solicitar a CT área decisora y suplente, con agenda al cierre del mes 1; cursar insumos a D-10 y pedir respuesta a D-5. Las aceptaciones formales conservan diez días hábiles. Para promover la región de contingencia, avisar al suplente a los 15 min sin respuesta del titular y obtener decisión dentro de 30 min (S4, 4.3.2.5); no esperar el plazo ordinario. Mantener bloqueada la acción sin autorización; el silencio no permite cambios.',
'R-019': 'Mantener y ensayar los enlaces ya ofertados: en Talca y Concepción, fibra y LTE con Starlink en espera caliente; en cross-docking, Starlink con LTE Entel/Claro y conmutación menor a 30 s. En Los Ángeles de madrugada, probar pérdida del camino Starlink restante y continuidad local de su ventana de 3 h. Coordinar restitución y conciliación sin duplicar el mismo corte como falla de SII, POS o mapas. Referencia: S4, 4.2.5.3.',
'R-034': 'Mitigar. El paquete 3.10.1.4 abarca meses 11--15: certificación H5 en 11--12 y piloto con locales reales en marcha blanca 13--15. IMP conduce la respuesta, DAT dirige la innovación y Comercial/Calidad validan el catálogo 3.10.1.1 (meses 7--9). Medir I-01A en mes 15: al menos 70\% de aciertos con al menos 100 avisos evaluables; mostrar confianza y confirmar saldo en visita. Sin cumplirlo, no liberar a las demás rutas y degradar a aviso por vida útil remanente. Sin catálogo, mantener aviso informativo y escalar a Comercial.'
}
# Update only response fields, not the risk events or their valuations.
tl=[]
for l in t.splitlines():
 if re.match(r'R-\d{3} &',l):
  c=l.split(' & ')
  if c[0] in newresponses:c[6]=newresponses[c[0]];l=' & '.join(c)
 tl.append(l)
t='\n'.join(tl)+'\n'
tl=[]
for l in a.splitlines():
 if re.match(r'R-\d{3} &',l):
  c=l.split(' & ')
  if len(c)==4 and c[0] in newresponses:
   rid=c[0];c[2]=newresponses[rid]+(' Evidencia y detalle: Tabla 8.A.2.' if rid in ['R-016','R-018'] else '')
   if rid=='R-034':c[1]='I-01A inferior a 70\% con al menos 100 avisos evaluables en mes 15, o catálogo de acciones no validado al activar.'
   if rid=='R-019':c[1]='Corte del enlace del sitio o del respaldo restante; en Los Ángeles de madrugada, pérdida del camino Starlink disponible.'
   l=' & '.join(c)
 tl.append(l)
a='\n'.join(tl)
# Complete the existing client-dependency entries with the matching test/urgent limits.
alines=[]
for l in a.splitlines():
 if l.startswith('R-016 / IMP &'):
  c=l.split(' & ');c[2]+=' La transferencia se comprueba con rutas y excepciones probadas sin el planificador durante la marcha blanca.'
  c[3]+=' Prueba sin el planificador en meses 13--15 (S7, 7.2.1).';l=' & '.join(c)
 if l.startswith('R-018 / JP &'):
  c=l.split(' & ');c[2]+=' Para promoción regional, identificar autorizador titular y suplente con facultad delegada.'
  c[3]+=' Excepción de S4, 4.3.2.5: avisar al suplente a los 15 min sin respuesta del titular y resolver dentro del máximo de 30 min.'
  c[4]=c[4].replace('Si amenaza seguridad, continuidad o hito,', 'En promoción regional, escalar al suplente a los 15 min y mantener sin autorizar la promoción si vence el máximo de 30 min; registrar el efecto sobre el RTO, sin promover por silencio. Si amenaza seguridad, continuidad o hito,');l=' & '.join(c)
 alines.append(l)
a='\n'.join(alines)

# The source documents remain read-only; the reviewed links live in SD8.
intro='El Formulario T-16 reúne el registro de riesgos'
b=b.replace(intro,'El Anexo 8.D documenta los cruces con S4, S7 y S13 y distingue las correspondencias verificadas de las brechas todavía no incorporadas al registro. '+intro,1)
b=b.replace('En urgencias rige además el plazo específico de R-022.', 'En urgencias rige además el plazo específico de R-022. La promoción regional sigue la excepción de S4, 4.3.2.5: si el titular no responde en 15 min decide el suplente dentro del máximo de 30 min; R-018 recoge este plazo y R-021 conserva la aprobación previa de residencia de datos.')
b=b.replace('Los riesgos R-034 a R-040 son los riesgos de adopción de las cinco innovaciones del Capítulo 13. Cada uno conserva el ID con que lo cita ese capítulo y la respuesta que desarrolla su sección de riesgo de adopción (Subdocumento 13, secciones 13.1 a 13.5).',
'Los riesgos R-034 a R-040 conservan los ID de adopción de las cinco innovaciones de S13. Para R-034, 3.10.1.4 comprende certificación H5 en meses 11--12 y piloto con locales reales en meses 13--15: la ventana 11--15 es la del paquete completo. IMP conduce la respuesta de adopción; DAT dirige la innovación y Comercial/Calidad validan su catálogo (S13, 13.1.3--13.1.7, pp. 12--17). Las valoraciones de S8 responden a las escalas revisadas; las referencias numéricas antiguas de S13 requieren sincronización, identificada en el Anexo 8.D. Este anexo también vincula los riesgos arquitectónicos y la rotación del turno nocturno, sin dar por cubierta una brecha por mera similitud temática.')
anchor='\\subsection{Análisis cualitativo de riesgos}'
b=b.replace(anchor,
'La matriz de trazabilidad del Anexo 8.D registra tres brechas de arquitectura (B-S4-01 a B-S4-03) y una de rotación nocturna (B-S7-01), con evento candidato, responsable y tratamiento relacionado. Son registros de brecha, no riesgos valorados del T-16: la incorporación y valoración se realizará en la tarea de riesgos omitidos. Por ello, los 40 riesgos y sus totales publicados conservan el mismo universo; no acreditan cobertura completa de las condiciones ya detectadas. R-017 conserva la inasistencia a formación; la rotación anual del 38\% genera otro evento y no se usa como probabilidad $p_0$.\n\n'+anchor,1)
old='En continuidad, la solución compromete un RTO de 4 horas'
st=b.index(old);en=b.index('\n\n',st)
b=b[:st]+r'''En continuidad se mantienen los objetivos RTO de 4 horas y RPO de 15 minutos para servicios críticos (Bases Técnicas Transversales, cap. 7, RT-07.04, p. 17). S4, 4.3.2.4--4.3.2.7 (pp. 181--184), distingue extracción multicanal, recuperación del WMS, restitución de accesos y recuperación del ERP del CLIENTE. Las alarmas a los 5 y 15 minutos y AL-DR-01 verifican brecha y punto recuperable; se ensayan antes de H5/H10 y semestralmente durante Operación. AL-OFF-01 comprueba 24 h sin WAN y relevos a las 8 y 16 h; el manifiesto de 26 h no sustituye la caché de 24 h ni renueva por sí solo credenciales. AL-DTE-01 comprueba las 96 salidas con guía válida, preemisión, cambio de carga y nueva emisión del ERP. Estas evidencias se complementan: aprobar una no demuestra las otras. La pérdida de la sala de Talca detiene nuevas guías hasta restituir el ERP; recuperar el WMS en nube no resuelve esa dependencia ni permite exceptuar el RTO requerido. Esa brecha se registra como B-S4-02, sin declarar demostrada la continuidad completa. Para el retiro sanitario durante pérdida regional, S4, 4.3.2.5 (p. 184), plantea hasta 15 min de habilitación y 60 de consulta y verificación: 75 min frente al máximo de dos horas, sujetos a prueba y cobertura de evidencia.''' +b[en:]

# Four-field traceability: exact source -> existing risk/response -> discrepancy -> action.
trace=[
('TR-01','S13, 13.1.3--13.1.7, pp. 12--17; Tabla 13.3. T-15, pp. 21 y 50, EDT 3.10.1.4.',
'R-034; respuesta 8.A.1 y T-16. Paquete 11--15; certificación 11--12; piloto real 13--15; I-01A en mes 15.',
'El anexo no explicitaba meses; T-16 sólo mencionaba el piloto 13--15. S13 llama piloto a 11--15, aunque su propio texto distingue las dos fases.',
'Corregido en S8/T-16/8.A.1. IMP conduce adopción; DAT dirige INN-01 y Comercial/Calidad validan catálogo 3.10.1.1 en 7--9. Habilitar tras I-01A de al menos 70\% con al menos 100 avisos evaluables en mes 15. En S13 sólo falta sustituir la expresión ambigua por ventana del paquete; no se edita aquí.'),
('TR-02','S13, secciones de riesgo 13.1.7--13.5.7; S8, escalas de 8.1.3 y Anexo 8.C.',
'R-034--R-040: mismas causas e ID; valoraciones de S8 revisadas en tarea 2.',
'S13 mantiene referencias numéricas anteriores para R-034, R-036, R-039 y R-040. La coincidencia del ID no acredita igualdad de impacto y zona.',
'Sincronización externa requerida: R-034 pasa a I=4, E=0,28 Alta; R-036 a I=4, E=0,20 Alta; R-039 a I=3, E=0,10 Media; R-040 a I=4, E=0,28 Alta. P permanece igual. R-035, R-037 y R-038 conservan sus valores. JP conserva este cambio para el prompt final; no se copian en S8 los valores antiguos.'),
('TR-03','S4, Tabla 4 y 4.1.12, p. 78; identidad local en pp. 26--27 y 46--47; AL-OFF-01 en p. 81.',
'B-S4-01: disponibilidad de identidad central y autorizaciones locales. R-023/R-027 tratan compromiso de credenciales, no indisponibilidad.',
'No hay riesgo específico de indisponibilidad de identidad. Manifiesto de 26 h, caché de 24 h y credenciales de 8/14 h tienen funciones distintas y no acreditan por sí solos relevo ni revocación.',
'Brecha registrada para tarea 5. ARQ coordina con SEG/SRE y TI del CLIENTE; CAL exige antes de H5/H10 AL-OFF-01 con corte 24 h, relevos a 8/16 h, expiración, denegación y reconciliación. Separar control de diseño de dependencia residual; no presentar al CLIENTE un defecto de autenticación sin resolver.'),
('TR-04','S4, Tabla 4, p. 78; 4.1.17.2, p. 84; 4.2.5.4, pp. 152--153; 4.3.2.5, p. 183.',
'B-S4-02: ERP como emisor único y restitución del ERP del CLIENTE ante pérdida de sala. R-008 sólo cubre falta de respuesta del SII.',
'El fallo del ERP puede impedir nuevas guías aunque SII y WMS estén disponibles. La pérdida de sala y la guía anulada no quedan cubiertas por colas ni por promover el WMS.',
'Brecha registrada para tarea 5. ARQ/SRE coordinan con Jefe de TI y Finanzas del CLIENTE el procedimiento de restitución del ERP antes de las pruebas H5/H10. CAL contrasta AL-DTE-01 y AL-DR-01: guía preemitida válida, cambio de carga, anulación y nueva guía; bloquear salida sin documento válido. No exceptuar el objetivo de recuperación requerido.'),
('TR-05','S4, Tabla 4, p. 78; 4.1.15--4.1.16, pp. 80--81; 4.3.2.5--4.3.2.6, pp. 183--184.',
'B-S4-03: indisponibilidad de consolidación/reserva central de stock. R-004 es conciliación previa al corte; R-019 es enlace del sitio.',
'Falta el evento de servicio central indisponible o de transferencia de autoridad incoherente, aun con enlace disponible. La copia fechada no confirma una reserva global.',
'Brecha registrada para tarea 5. ARQ/DAT, con SRE y Operaciones/Comercial del CLIENTE, verifican antes de H5/H10 conciliación por sitio, UUID y exclusión del escritor anterior. Conservar capturas como pendientes; no confirmar stock con copia vencida ni permitir dos escritores. CAL exige actas de AL-STOCK-01 y AL-DR-01.'),
('TR-06','S4, Tabla 4, p. 78; 4.2.5.4, p. 152; T-16, R-008/R-009.',
'R-008: SII sin confirmación; R-009: resultado POS incierto. Respuestas 8.A.1.',
'Existe cobertura por evento; no corresponde crear otro riesgo sólo por aparecer en la tabla de arquitectura. R-008 no equivale a caída del ERP ni R-009 a una venta confirmada.',
'Correspondencia verificada. SRE mantiene pendientes tributarios y ARQ concilia POS con la misma clave; TI/Finanzas aportan el resultado externo. Pruebas de integración deben conservar estado sin confirmar y evitar duplicación de cargos. Si el origen es WAN, asociar a R-019 y no imputar otra vez el mismo episodio.'),
('TR-07','S4, Tabla 4, p. 78; S7, 7.2.1, p. 32; S3, V-14 y S-16.',
'R-016; respuesta 8.A.1, dependencia 8.A.2 y T-16. Talleres meses 1--3.',
'La transferencia temprana estaba prevista, pero no la comprobación de reglas sin el planificador en la marcha blanca que exige S7.',
'Corregido en T-16/8.A.1/8.A.2: IMP coordina con Gerente de Operaciones, planificador y ayudante; confirmar retiro en mes 1, transferir en 1--3 y probar sin el planificador en 13--15, antes de su retiro. La fecha efectiva se confirma mediante V-14; no se inventa. No se crea otro riesgo del mismo conocimiento.'),
('TR-08','S4, 4.2.5.3, pp. 150--151; 4.3.2.4, pp. 181--182. S7, T-14, 6.6.2--6.6.3, p. 74.',
'R-019: interrupción WAN por sitio. Respuesta 8.A.1/T-16; pruebas 6.6.2 y AL-OFF-01.',
'La respuesta era genérica. Concepción tiene respaldo propuesto, aunque el caso describa enlace único inicial. En Los Ángeles de madrugada puede quedar sólo Starlink.',
'Corregida la respuesta: SRE ensaya fibra/LTE/Starlink caliente en CD, Starlink y LTE Entel/Claro en cross-docking y pérdida del único camino restante en Los Ángeles. Verificar conmutación menor a 30 s, ventana local de 3 h de cross-docking y autonomía exigida de 24 h. Son condiciones distintas; no rebajar autonomía a 3 h. Recepción antes de H3 y aceptación ampliada antes de H5 según T-14.'),
('TR-09','S4, 4.2.5.3, p. 151; diseño de sala y energía. T-16, R-020.',
'R-020: corte que supera la autonomía de respaldo. Respuesta 8.A.1 y responsable SRE.',
'El corte externo ya está identificado. La autonomía difiere entre sala de Talca, gabinetes y Concepción; no puede afirmarse un respaldo uniforme para todo componente.',
'Correspondencia verificada. SRE debe comprobar transferencia y autonomía por componente, con TI/Operaciones del CLIENTE y los procedimientos de recuperación. UPS de gabinete de 30 min no equivale al generador de Talca de 24 h. Las fallas de diseño de UPS/HA se verifican en arquitectura y calidad, no se añaden como duplicados de corte eléctrico.'),
('TR-10','S4, 4.3.2.5, pp. 182--183; aprobación de promoción regional y residencia.',
'R-018: decisión del CLIENTE requerida para promover. R-021: autorización previa de residencia/transferencia.',
'El plazo ordinario D-5 o escalamiento en días no sirve para una autorización de recuperación. La aprobación de residencia no equivale a autorización de cada promoción.',
'Corregido en 8.1.2, T-16 y 8.A.1/8.A.2: JP registra titular y suplente con facultad delegada; SRE/ARQ notifican el incidente, avisan al suplente tras 15 min sin respuesta del titular y requieren decisión dentro de 30 min. Ensayar semestralmente AL-DR-01. Si no se autoriza, escalar y medir impacto en RTO; no promover ni redirigir tráfico por silencio.'),
('TR-11','S4, 4.2.1.1, p. 92 (S-36), y 4.2.2, p. 97: cobertura en cámaras.',
'Sin riesgo específico de cobertura RF en T-16. R-019 es WAN del sitio; R-038 es asociación lote--sensor.',
'El número de AP es preliminar y depende del estudio de cobertura; la falta inicial de cobertura interior no acredita que el diseño propuesto ya funcione.',
'Verificación de arquitectura, ARQ/SRE con Jefa de Bodega y TI: estudio y prueba en cámaras reales, con terminales y puertas/ocupación representativos, antes de aceptar la instalación. CAL registra resultado y corrección del diseño. En tarea 5 evaluar sólo la incertidumbre residual documentada; no crear por defecto un riesgo externo ni duplicar R-019/R-038.'),
('TR-12','S4, 4.2.5.3--4.2.5.4, pp. 150--152: pares de firewall, nodos, discos, switches y cómputo de borde.',
'Controles de disponibilidad de S4 y pruebas de calidad; R-019/R-020 sólo para enlace y energía.',
'Enumerar un componente no justifica trasladar una falla de diseño al registro del CLIENTE. Quedan por demostrar conmutación, exclusión del escritor y recuperación completa.',
'ARQ/SRE y CAL conservan la verificación por componente y escenario, antes de recepción/aceptación; evidencia en pruebas de S4. Pérdida completa del sitio se contrasta con B-S4-02/B-S4-03 según su efecto; revisar naturaleza y ubicación en tareas 5--6 sin crear un riesgo por disco, switch o firewall.'),
('TR-13','S7, 7.1.2.7 y Figura 7.15, pp. 21--22; 7.2.1, p. 32. T-14, 7.1.2, pp. 74--75; T-15, pp. 25 y 95.',
'B-S7-01: rotación anual del 38\% en preparación nocturna. R-017: inasistencia de personas convocadas; R-015: adopción de quienes continúan con el proceso previo.',
'Falta un evento de nuevas incorporaciones que superan la capacidad de inducción o ingresan sin competencias verificadas. El 38\% es una tasa anual de rotación, no p0 ni proporción cierta de fallos.',
'Brecha registrada una sola vez para tarea 5. Aplicar el programa 7.1.2 en meses 13--56 (22:00--06:00): IMP hasta mes 21 y SRE desde 22, familia IMP; Jefa de Bodega y Gerente de Operaciones aportan altas, turnos y tutores. Verificar aprendizaje en un máximo de dos horas, tutor y evaluación antes de habilitar trabajo autónomo; usar cobertura certificada si falta preparación. No cargar otra vez las HH ordinarias del paquete.'),
('TR-14','S4, 4.1.10, p. 75; 4.1.15, p. 81; 4.3.2.4--4.3.2.7, pp. 181--184.',
'S8, 8.3.3: RTO/RPO y pruebas AL-OFF-01, AL-DTE-01 y AL-DR-01. Enlace con B-S4-01--03.',
'S8 atribuía las 96 salidas a una sola prueba de recuperación y usaba 85 min para retiro. S4 distingue pruebas y fija presupuesto sanitario regional de 15+60=75 min.',
'Corregido en 8.3.3. SRE ejecuta recuperación, ARQ verifica dependencias y CAL valida cobertura y tiempos antes de H5/H10 y en ensayos semestrales; Calidad del CLIENTE valida la consulta sanitaria. Conservar RTO 4 h/RPO 15 min y máximo sanitario 2 h; el presupuesto de 75 min es objetivo sujeto a prueba, no resultado logrado ni excepción del ERP.'),
]
breaches=[
('B-S4-01','Identidad central',
'Dado que altas, bajas y relevos dependen de identidad central y permisos locales vigentes, puede que la indisponibilidad del IdP o un manifiesto no válido impida habilitar al personal requerido o propagar una revocación, afectando la continuidad y seguridad del relevo.',
'ARQ coordina SEG/SRE; contraparte: Jefe de TI y Operaciones. Verificar AL-OFF-01, 24 h de corte y relevos 8/16 h antes de H5/H10; denegar accesos no válidos, conservar auditoría y resolver con personal previamente autorizado. Tarea 5 debe separar incertidumbre de operación de defecto de diseño; tarea 6 conserva controles en arquitectura/calidad.',
'TR-03; diferente de R-023/R-027, que tratan compromiso de cuentas.'),
('B-S4-02','ERP y nueva guía',
'Dado que el ERP del CLIENTE es el único emisor tributario y reside en Talca, puede que su indisponibilidad, incluida la pérdida de la sala, impida emitir la guía nueva requerida por una carga modificada o una guía anulada, bloqueando la salida hasta restituirlo.',
'ARQ/SRE con Jefe de TI y Finanzas del CLIENTE; acordar restitución y ensayar AL-DTE-01/AL-DR-01 antes de H5/H10. Mantener sólo salidas con guía preemitida aún válida y bloquear las que requieren nueva guía. En tarea 5 valorar la dependencia del CLIENTE y el impacto del servicio sin presumir que el WMS recuperado restaura el ERP.',
'TR-04; R-008 sólo cubre espera del SII. Una sola brecha integra indisponibilidad ERP y pérdida de sala como causa.'),
('B-S4-03','Consolidación y reserva central',
'Dado que la reserva global depende del estado central y de una única autoridad de escritura, puede que falle la consolidación o no pueda restituirse una autoridad consistente, dejando el stock central desactualizado y pedidos sin confirmación o con conflictos de reserva.',
'ARQ/DAT con SRE, Operaciones y Comercial; AL-STOCK-01/AL-DR-01 antes de H5/H10. Mantener operación local y capturas pendientes; conciliar por UUID y sitio y excluir al escritor anterior antes de promover otro. En tarea 5 valorar la dependencia residual sin duplicar la corrección obligatoria del diseño.',
'TR-05; no equivale a diferencias iniciales R-004 ni a interrupción WAN R-019.'),
('B-S7-01','Rotación de preparación nocturna',
'Dado que el equipo de preparación nocturna presenta rotación anual del 38\% y necesita inducción continua, puede que la incorporación de reemplazos supere la capacidad de tutoría y evaluación o que se asignen personas no preparadas al flujo, afectando calidad de preparación, seguridad y certificación de la ola.',
'IMP hasta mes 21 y SRE desde 22, con Jefa de Bodega y Operaciones del CLIENTE. Programa 7.1.2 en meses 13--56, turno 22:00--06:00, aprendizaje máximo dos horas y evaluación antes del trabajo autónomo; formar reemplazos y disponer tutor/cobertura certificada. Tarea 5 estima ocurrencia y esfuerzo extraordinario sin convertir 38\% en p0 ni repetir las HH programadas.',
'TR-13; distinta de R-017 (ausencia a sesiones) y R-015 (resistencia/adopción). Vincular altas no certificadas a esta brecha para no duplicarlas en R-017.'),
]

extra=r'''
\clearpage
\section{Anexo 8.D: Trazabilidad con S4, S7 y S13}

La revisión contrasta los PDF vigentes de ``Informe propuesta tecnica/Informe\_2\_LafroX'', no las copias históricas ni los fuentes alternativos de ``Entrega 2 fake''. Las páginas citadas son las páginas impresas verificadas del documento indicado. La Tabla 8.D.1 vincula condición de origen, riesgo o respuesta existente, discrepancia y corrección. ``Corregido'' se refiere sólo a S8 y sus entregables; ``sincronización externa requerida'' identifica lo que todavía debe ajustarse en otros subdocumentos. Estos no se modifican en esta revisión.

Las cuatro brechas B-S4-01, B-S4-02, B-S4-03 y B-S7-01 se registran con evento candidato y tratamiento relacionado en la Tabla 8.D.2. No son ID de riesgos nuevos ni sustituyen su incorporación y valoración en T-16, previstas para la tarea de riesgos omitidos. El universo valorado sigue siendo R-001--R-040 y el Anexo 8.B conserva sus cifras. Las condiciones de verificación de cobertura RF y disponibilidad de componentes se distinguen de los riesgos residuales: no se convierten automáticamente en riesgos trasladables al CLIENTE. JP mantiene la trazabilidad hasta su resolución, valoración o reubicación justificada.

\begingroup
\renewcommand{\thetable}{8.D.1}
\begin{landscape}
\setlength{\textwidth}{\linewidth}
\begin{tablalafrox}{Cruces verificados S4/S7/S13 y correcciones del registro. Fuente: documentos y páginas indicados en cada fila.}{tab:sd8-trazabilidad-cruces}{G{0.06} F{0.19} F{0.20} F{0.20} Y}{\cab{Cruce} & \cab{Referencia y condición de origen} & \cab{Riesgo o respuesta asociada} & \cab{Discrepancia / estado} & \cab{Corrección, responsable y evidencia}}
'''
for row in trace:extra+=' & '.join(row)+' \\\\\n'
extra+=r'''\end{tablalafrox}
\end{landscape}
\endgroup

\subsection*{Brechas registradas para incorporación y valoración}
\addcontentsline{toc}{subsection}{Brechas registradas para incorporación y valoración}

Cada código B identifica una única brecha, no un riesgo cuantificado. La tasa de rotación y los tiempos de autonomía no son probabilidades de ocurrencia. La valoración posterior debe justificar $p_0$, impacto, episodios y esfuerzo adicional con las escalas de 8.1.3, conservando las causas comunes para evitar doble conteo. Los tratamientos aquí citados son los ya previstos en la propuesta o condiciones de verificación, no acciones cuya eficacia se haya demostrado.

\begingroup
\renewcommand{\thetable}{8.D.2}
\begin{landscape}
\setlength{\textwidth}{\linewidth}
\begin{tablalafrox}{Brechas de cobertura detectadas, sin valoración ni incorporación anticipada al T-16. Fuente: cruces de la Tabla 8.D.1.}{tab:sd8-brechas-registro}{G{0.10} F{0.14} Y F{0.31} F{0.17}}{\cab{Brecha} & \cab{Condición} & \cab{Evento candidato: causa, evento y efecto} & \cab{Responsable, tratamiento relacionado y momento} & \cab{Vínculo y regla para no duplicar}}
'''
for row in breaches:extra+=' & '.join(row)+' \\\\\n'
extra+='\\end{tablalafrox}\n\\end{landscape}\n\\endgroup\n\n'
a=a.replace('Anexos 8.A--8.C','Anexos 8.A--8.D').replace('Anexos 8.A, 8.B y 8.C','Anexos 8.A, 8.B, 8.C y 8.D')
a=a.replace('\\section*{Referencias}',extra+'\\section*{Referencias}',1)
# Cross references in the form explicitly do not claim that the gaps are covered.
t=t.replace('El detalle de valores esperados está en el Anexo 8.B;', 'El Anexo 8.D registra la trazabilidad con S4/S7/S13 y cuatro brechas aún no incorporadas ni valoradas en estos 40 riesgos. El detalle de valores esperados está en el Anexo 8.B;')
for p,s in zip(paths,[b,a,t]):(root/p).write_text(s,encoding='utf-8')
note=['# Tarea 4: coherencia con S4, S7 y S13','', 'Revisión directa de PDF vigentes y correcciones exclusivamente en S8, Anexos y T-16. El usuario indicó registrar las brechas ahora y completar su incorporación/valoración en tarea 5.','', '## Resultado','', '14 cruces TR-01–TR-14 en Tabla 8.D.1; cuatro brechas B-S4-01/02/03 y B-S7-01 en Tabla 8.D.2, cada una con evento, dueño, contraparte y tratamiento relacionado. No se añaden riesgos valorados, no se amplía el universo de 40 ni se recalculan HH o reservas.','', 'R-034: paquete 3.10.1.4 meses 11–15, H5/certificación 11–12, piloto real 13–15 e I-01A en mes 15 (≥70 % con ≥100 avisos evaluables); respuesta de adopción IMP, innovación DAT. Se corrigen T-16 y 8.A.1. R-016 agrega prueba sin planificador durante 13–15. R-019 especifica los caminos propuestos y la singularidad de Los Ángeles. R-018 separa autorización de promoción regional (titular/suplente 15/30 min) de R-021 (residencia previa).','', '## Cambios externos para el prompt final','', 'S13 13.1.3 p.12: llamar a 11–15 ventana del paquete completo y reservar piloto real para 13–15, como ya explican el propio texto y la Tabla 13.3. Sincronizar impactos/exposiciones/zonas de R-034/R-036/R-039/R-040 según tarea 2; los otros tres riesgos de innovación conservan valores.','', 'S4: conservar los protocolos diferenciados AL-OFF-01/AL-DTE-01/AL-STOCK-01/AL-DR-01 y vincular sus dependencias residuales con los IDs que se creen en tarea 5. La restitución del ERP del CLIENTE y los accesos de piso siguen siendo necesarios: recuperar WMS en nube no acredita nuevas guías ni permite exceptuar el RTO. Cobertura en cámaras y redundancia de componentes requieren evidencia de diseño/calidad, no un nuevo riesgo por componente.','', 'S7/T14/T15: conservar 7.1.2 en meses 13–56 y turno 22:00–06:00; IMP hasta 21/SRE desde22 con familiaIMP. Vincular el futuro riesgo de rotación anual38 % a este programa sin duplicar R-017, sin convertir la tasa en p0 y sin sumar otra vez las2816HH programadas. No confundir la ventana local de3h del cross-docking con autonomía exigida de24h.','', 'S6/T9: sincronizar excepción de autorización regional15/30min añadida aR-018; el flujo de R-022 no sustituye esa autorización.','', '## Pendiente delimitado','', 'Tarea5 incorpora y valora las cuatro brechas detectadas junto con las demás omisiones del caso; tareas6–9 mantienen su alcance. No se declara cerrado el riesgo residual ni la cobertura total del registro.']
# Keep the handoff note readable (avoid accidental joined tokens in strings above).
replacements={'desde22':'desde 22','familiaIMP':'familia IMP','anual38':'anual 38','en p0':'en p0','las2816HH':'las 2.816 HH','de3h':'de 3 h','de24h':'de 24 h','regional15/30min':'regional 15/30 min','aR-018':'a R-018','Tarea5':'Tarea 5','tareas6–9':'tareas 6–9'}
n='\n'.join(note)+'\n'
for x,y in replacements.items():n=n.replace(x,y)
(root/'odd/tasks/tarea-4-trazabilidad-s4-s7-s13.md').write_text(n,encoding='utf-8')
print('14 cruces, 4 brechas, 4 respuestas sincronizadas. Universo y valoraciones conservados.')
