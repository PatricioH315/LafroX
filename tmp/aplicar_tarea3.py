from pathlib import Path
import json,re,hashlib
root=Path(__file__).resolve().parents[1]
backup=root/'tmp/tarea3-baseline.json'
if backup.exists(): raise SystemExit('La tarea 3 ya fue aplicada; no repetir sobre los cambios actuales.')
body=root/'08_plan_riesgos/contenido.tex';ann=root/'LAFROX-Subdocumento8-Anexos.tex';form=root/'LAFROX-Formulario-T-16.tex'
original={p:p.read_text(encoding='utf-8') for p in [body,ann,form]}
# Contraparte que responde, apoyo, solicitud/evidencia, plazo y contingencia.
data={
1:('ARQ','Gerente Comercial; coordinación de TI con el responsable EDI de cada cadena.',
'Confirmar cadenas del alcance, contacto técnico, agenda y ambiente de certificación; entregar resultado firmado de intercambio de pedidos y avisos por cadena.',
'Solicitar agenda en mes 13 y confirmarla al cierre del mes 14. Certificación a D-5 de la ventana final de 28 días de evidencia de E2; D es el inicio de esa ventana.',
'Escalar al Gerente Comercial por CT. Reordenar pruebas independientes; conservar pendiente la cobertura EDI de la cadena. La carga manual no acredita E2 ni permite excluirla.',
'S3, Tabla 3.A.12, Canal Moderno; criterio R18-13.',
'Solicitar al Gerente Comercial, con TI y cada cadena, agenda EDI en mes 13, confirmada en mes 14, y certificación a D-5 del inicio de las cuatro semanas finales de evidencia de E2. Ante falta de respuesta, JP escala por CT; continuar pruebas independientes sin acreditar la cadena pendiente ni sustituir EDI por carga manual.'),
2:('DAT','Jefa de Calidad; Jefe de TI y Jefa de Bodega aportan fuentes ERP/WMS y antecedentes de lotes.',
'Entregar extractos y evidencia de origen de los vínculos sanitarios; Calidad debe decidir por escrito la disposición de conjuntos cuya historia no pueda reconstruirse y la política ante lote desconocido (V-07).',
'Solicitar fuentes en mes 1; política y resolución inicial al cierre del mes 2. Para cada carga, resolver las excepciones a D-5 de su validación; nunca después del corte.',
'Escalar a CT con los lotes y evidencia faltante; aislar el conjunto y trabajar sobre datos verificables. Mantener la aceptación pendiente; no inventar lotes ni reconstruir historia sin fuente.',
'S3, consulta V-07 y S-02; S2, Jefa de Calidad y Jefe de TI.',
'Solicitar a la Jefa de Calidad, con TI y Bodega, evidencia de origen y decisión sobre lotes no reconstruibles; política V-07 al cierre del mes 2 y excepciones a D-5 de validar cada carga. Si no responde, JP escala por CT, se aísla el conjunto y queda pendiente su aceptación; no se inventa historia sanitaria.'),
3:('DAT','Jefe de Abastecimiento; Jefe de TI entrega y explica los extractos del ERP.',
'Entregar tres años de ventas y pedidos, diccionario y cobertura temporal; validar el informe de perfilado V-09 y las excepciones identificadas.',
'Solicitar en mes 2; validación de V-09 al cierre del mes 3 y correcciones de cada extracto a D-5 de validar su carga.',
'Escalar por CT a Abastecimiento y TI; separar períodos incompletos y continuar perfilado de fuentes disponibles. No reducir unilateralmente los tres años exigidos ni dar por aceptado el historial faltante.',
'S3, V-09, S-25 y RF-10.01.',
'Solicitar al Jefe de Abastecimiento y a TI el historial de tres años y validación de V-09 al cierre del mes 3; corregir extractos a D-5 de validar la carga. Ante silencio, escalar por CT, separar períodos incompletos y continuar el perfilado disponible sin reducir la historia exigida.'),
4:('DAT','Jefa de Bodega; Gerente de Finanzas aprueba ajustes de saldo y Gerente de Operaciones coordina conteos.',
'Entregar conciliación entre inventario legado y conteo físico, causas de diferencias y ajustes autorizados; presentar acta de validación previa al corte.',
'Solicitar protocolo en mes 2 y validarlo en mes 3. En cada corte, responsables y conteo confirmados a D-5; conciliación y ajustes firmados antes de D.',
'Escalar por CT a Bodega y Finanzas; repetir conteo y conciliación del conjunto afectado. No ejecutar su corte sin acta; continuar trabajo independiente y evaluar recuperación sin mover hitos por silencio.',
'S3, S-14 y participación de Bodega; condiciones de aceptación de S8, 8.3.3.',
'Solicitar a Bodega, con Operaciones y Finanzas, protocolo de conciliación en mes 2, validado en mes 3. Confirmar conteo a D-5 del corte y cerrar acta y ajustes antes de D. Si no hay respuesta, escalar por CT, repetir conciliación y bloquear el corte afectado hasta contar con evidencia aprobada.'),
5:('DAT','Gerente de Operaciones; Gerente de Finanzas valida saldos y representantes de transportistas aportan antecedentes.',
'Entregar saldos de envases por cliente y transportista y sus respaldos; validar V-08. Si se requiere conteo inicial, autorizar su ejecución y firmar conciliación de M8.',
'Solicitar política de saldos en mes 2 (S-10). Para cada ola de reparto: respuesta a D-5 de validar la carga M8 y conciliación aprobada antes de habilitarla.',
'Escalar a Operaciones y Finanzas por CT; preparar conteo o reconstrucción documental autorizados. Mantener pendiente M8 en los saldos afectados; no asignar cero ni presumir aceptación.',
'S3, V-08, S-10 y RNG-07.',
'Solicitar al Gerente de Operaciones y a Finanzas respaldos y conciliación V-08 de saldos por cliente y transportista; política en mes 2 y respuesta a D-5 de validar la carga M8 de cada ola. Ante silencio, escalar por CT y mantener M8 pendiente para esos saldos; no presumir saldo cero.'),
6:('IMP','Gerentes Comercial y de Operaciones: horas de entrega; Gerente de Finanzas: montos esperados de rendición.',
'Entregar registros históricos verificables y aprobar fuente, período y confiabilidad de la línea base V-10; identificar limitaciones y resolver formalmente una alternativa que preserve los criterios de aceptación.',
'Solicitar en los primeros cinco días hábiles del mes 1; validar V-10 al cierre de ese mes. Cualquier alternativa debe resolverse antes de iniciar la comparación de aceptación.',
'Escalar a las tres gerencias por CT. Conservar por separado la captura futura y la historia comprobada; suspender la comparación afectada hasta resolver la referencia, sin fabricar antecedentes ni cambiar la meta.',
'S3, V-10 y S-01; S2, definición de OTIF.',
'Solicitar a Comercial y Operaciones las horas históricas y a Finanzas los montos de rendición, con validación de V-10 al cierre del mes 1. Si no responden, escalar por CT y mantener pendiente la referencia de aceptación; la captura futura no reconstruye la historia anterior.'),
7:('DAT','Gerente de Finanzas; Jefe de TI ejecuta la extracción del ERP y documenta su cobertura.',
'Entregar listado completo de deuda vigente y conciliación con el extracto provisional; autorizar la inclusión de documentos omitidos y registrar volumen y diferencias.',
'Solicitar universo y criterio de vigencia en mes 2; respuesta inicial al cierre del mes 3. Cada extracto completo y conciliado a D-5 de validar la migración de cartera.',
'Escalar por CT a Finanzas y TI; medir y preparar la extracción complementaria. Mantener pendiente la cartera incompleta; tramitar impactos por el gobierno del proyecto sin tratar la integridad obligatoria como ampliación opcional.',
'S3, alcance de migración y rol de Finanzas/TI; evento R-007 del T-16.',
'Solicitar a Finanzas y TI el universo de deuda vigente, con respuesta inicial al cierre del mes 3 y conciliación a D-5 de validar la migración. Ante silencio, escalar por CT y mantener la cartera incompleta pendiente; preparar extracción complementaria sin omitir deuda obligatoria.'),
11:('CAL','Jefa de Calidad, autoridad de aprobación sanitaria; Bodega y Operaciones validan aplicación en terreno.',
'Aprobar y versionar matriz de umbrales y duraciones por tipo de producto, fichas de almacenamiento y reglas de liberar, bloquear o rechazar; emitir aprobación de V-11.',
'Solicitar durante mes 1; matriz aprobada al cierre del mes 2, antes de certificar parametrización. Todo cambio posterior debe aprobarse antes de probarlo o usarlo.',
'Escalar inmediatamente por CT si amenaza certificación. Aplicar el tratamiento preventivo de V-11 a lecturas fuera de ficha y conservar el bloqueo; no cerrar marcha blanca sin matriz aprobada.',
'S3, V-11, S-04 y RNG-04.',
'Solicitar a la Jefa de Calidad la matriz térmica versionada V-11 durante mes 1 y su aprobación al cierre del mes 2, antes de certificar. Si no responde, escalar por CT y mantener el tratamiento preventivo de lecturas fuera de ficha; no cerrar marcha blanca ni aprobar parámetros por el CLIENTE.'),
12:('IMP','Jefe de TI, como coordinador técnico de adquisición; Gerente de Operaciones confirma disponibilidad por sitio y ola.',
'Confirmar orden y fecha de entrega del equipamiento comprado por el CLIENTE, inventario por ola y evidencia de recepción técnica conforme a la especificación de LafroX.',
'Solicitar calendario en mes 1. En cada instalación, entrega y acceso confirmados a D-5 y recepción técnica antes de D; D es el inicio de instalación o prueba que requiere el equipo.',
'Escalar por CT al Jefe de TI y a Operaciones; ejecutar sólo trabajo independiente. Bloquear instalación y pruebas sin equipo; evaluar recuperación sin sustituir la compra del CLIENTE por una obligación de LafroX.',
'S6, T-9, 1.3; S3, participación de TI y Operaciones.',
'Solicitar al Jefe de TI, con Operaciones, calendario de equipos en mes 1, entrega confirmada a D-5 y recepción técnica antes de la instalación o prueba D. Ante silencio o faltante, escalar por CT, continuar trabajo independiente y bloquear las actividades sin equipo.'),
13:('IMP','Gerente de Operaciones; representante autorizado de cada empresa transportista firma su acuerdo.',
'Obtener acuerdos operacionales por empresa con nómina y coordinación de conductores, vehículos, acceso y capacitación; registrar cobertura de las diez empresas sin presumir firma.',
'Solicitar acuerdos en mes 2. Para cada ola de reparto, firma y nómina a D-5 del inicio de incorporación de la empresa; verificar antes de habilitar a sus conductores.',
'Escalar por CT a Operaciones; incorporar sólo empresas con acuerdo y registrar cobertura pendiente. Una ola sin esa empresa no acredita cobertura completa ni elimina obligaciones de aceptación.',
'S3, Tabla 3.A.12, Empresas Transportistas y S-05.',
'Solicitar al Gerente de Operaciones y al representante de cada transportista el acuerdo y la nómina desde mes 2, firmados a D-5 de su incorporación a la ola. Ante silencio, escalar por CT y no habilitar a esa empresa; conservar su cobertura pendiente sin retirarla del alcance.'),
14:('IMP','Gerente de Operaciones gestiona acceso; propietario o representante autorizado del camión otorga permiso.',
'Entregar autorización de acceso e instalación de termógrafo por vehículo, agenda de visita y condiciones del propietario; documentar cualquier alternativa sometida a aprobación.',
'Solicitar con D-10 y recibir autorización a D-5 de cada visita de instalación. Comprobar permiso y vehículo antes de intervenir en D.',
'Escalar a Operaciones por CT; cancelar la intervención no autorizada y proponer otra visita o vehículo autorizado con trazabilidad equivalente. Mantener pendiente la evidencia térmica; no instalar ni sustituir controles sin aprobación.',
'S3, S-05 y participación de transportistas; evento R-014.',
'Solicitar a Operaciones y al propietario permiso de instalación por vehículo con D-10 de la visita y obtenerlo a D-5. Ante silencio, escalar por CT, suspender la intervención y proponer otra visita o vehículo autorizado; mantener pendiente la evidencia térmica.'),
15:('IMP','Gerentes Comercial y de Operaciones; Jefa de Bodega para el turno nocturno y supervisores de cada ola.',
'Confirmar supervisores, turnos y usuarios que registrarán transacciones oficiales; aprobar agenda de acompañamiento y revisar evidencia diaria de adopción por usuario y ola.',
'Convocar con D-10 y confirmar responsables y agenda a D-5 del inicio de cada ola. Revisar transacciones diariamente durante marcha blanca y resolver ausencias el mismo día.',
'Escalar por CT a la gerencia del turno o canal; focalizar acompañamiento y registrar brechas. No acreditar adopción con registros sólo en el proceso anterior ni cerrar la ola sin evidencia.',
'S3, Tabla 3.A.12, Operaciones, Bodega y personal de terreno; S8, art. 17.3.',
'Solicitar a Comercial y Operaciones, con Bodega por turno, responsables y agenda de acompañamiento a D-5 del inicio de cada ola, convocando a D-10. Si no responden o persiste el registro externo, escalar por CT, focalizar acompañamiento y mantener pendiente la evidencia de adopción.'),
16:('IMP','Gerente de Operaciones; Planificador de Rutas y su ayudante participan en transferencia y validación.',
'Confirmar fecha efectiva de retiro y disponibilidad (V-14), reservar talleres y entregar reglas y excepciones documentadas con prueba de transferencia al ayudante.',
'Solicitar disponibilidad en los primeros cinco días hábiles del mes 1 y confirmarla al cierre del mes 1. Ejecutar y validar transferencia en meses 1--3, antes de perder disponibilidad.',
'Escalar por CT a Operaciones; activar talleres con ayudante y antecedentes verificables. Mantener reglas no corroboradas como incertidumbre y obtener validación antes de usarlas en rutas aceptadas.',
'S3, V-14, S-16 y Tabla 3.A.12.',
'Solicitar al Gerente de Operaciones y al planificador confirmación de retiro y disponibilidad V-14 al cierre del mes 1; transferir y validar reglas con el ayudante en meses 1--3. Si no responde o se retira antes, escalar por CT y reconstruir con ayudante e historia verificable, sin dar por validadas reglas pendientes.'),
17:('IMP','Gerente de Operaciones y Jefa de Bodega para turnos; Gerente Comercial para preventistas; Jefe de TI para administradores.',
'Confirmar nómina por perfil, liberación horaria, suplentes y acceso a sesiones; entregar disponibilidad para formación y evaluación y revisar evidencia individual de certificación.',
'Convocar con D-10 de cada sesión y confirmar nómina y horarios a D-5. Completar evaluación antes de habilitar al usuario y, en todo caso, antes de cerrar la marcha blanca de su ola.',
'Escalar por CT a la jefatura responsable el mismo día del incumplimiento; reprogramar sesiones y disponer suplente sólo si está certificado. Mantener pendiente la certificación y el cierre de ola afectado.',
'S3, Tabla 3.A.12; condición de capacitación del art. 17.3 citada en S8.',
'Solicitar a Operaciones, Bodega, Comercial y TI, según perfil, nómina y liberación horaria a D-5 de cada sesión convocada a D-10. Ante silencio o ausencia, escalar por CT y reprogramar evaluación; usar sólo suplentes certificados y no acreditar preparación ni cierre de ola sin evidencia.'),
18:('JP','Contraparte Técnica, responsable de encauzar la decisión hacia Calidad, TI, Operaciones, Comercial o Finanzas según la materia.',
'Identificar en cada solicitud el área decisora, titular funcional y suplente, pregunta, antecedentes completos, tarea bloqueada y fecha límite; obtener respuesta o acta de decisión de la autoridad competente.',
'Registrar agenda y responsables al cierre del mes 1. Para insumos de coordinación, cursar a D-10 y recibir respuesta a D-5 de la tarea D; para recepción de entregables rigen los diez días hábiles del art. 18.3.',
'JP notifica a CT el vencimiento el mismo día, solicita encauzamiento en un día hábil y, si sigue sin resolución en dos días hábiles, pide instancia ejecutiva extraordinaria. Si amenaza seguridad, continuidad o hito, escala inmediatamente y mantiene bloqueada la tarea dependiente.',
'S6, 6.1.6 y T-9, 1.6; S8, arts. 18.1--18.3.',
'Solicitar a CT la identificación de área decisora y suplente, con agenda al cierre del mes 1. Cursar insumos a D-10 y pedir respuesta a D-5 de la tarea; las aceptaciones formales conservan diez días hábiles. Al vencer, aplicar escalamiento del Anexo 8.A.2 y mantener bloqueada la tarea dependiente; el silencio no autoriza cambios.'),
21:('ARQ','Contraparte Técnica; Jefe de TI coordina revisión técnica y la Gerenta General encauza autorización con la asesoría competente del CLIENTE.',
'Resolver por escrito regiones, residencia, transferencia y tratamiento de datos sobre el expediente de arquitectura y seguridad; identificar autoridad firmante y condiciones de habilitación.',
'Solicitar expediente y autoridad en mes 1, decisión inicial al cierre del mes 2 y siempre antes de habilitar entornos con datos sujetos a autorización; aplicar la fecha que venza primero.',
'Escalar por CT a la autoridad identificada y al Comité de Arquitectura; preparar alternativa con sus impactos. Mantener deshabilitada la transferencia no aprobada; no elegir unilateralmente otra región ni presumir autorización.',
'S6, T-9, Comité de Arquitectura; S8, evento R-021 y autoridad de aceptación.',
'Solicitar por CT, con TI y la autoridad del CLIENTE encauzada por Gerencia General, aprobación escrita de residencia y transferencia en mes 1, resuelta al cierre del mes 2 o antes de habilitar datos, lo que ocurra primero. Ante silencio, escalar y preparar alternativa de arquitectura; mantener deshabilitada la transferencia no aprobada.'),
22:('SEG','Contraparte Técnica; Gerente de Operaciones autoriza la intervención operacional y Jefe de TI valida su ejecución técnica.',
'Aprobar flujo de autorización urgente, contactos y suplentes; por incidente, decidir por escrito la intervención, ventana, alcance, reversión y responsable con el expediente de seguridad.',
'Flujo aprobado al cierre del mes 1. Cada intervención se solicita al detectar la necesidad; si no hay respuesta, reiterar y escalar en una hora o antes si el plazo de atención o continuidad exige actuar. Autorización siempre previa al cambio.',
'Aplicar contención permitida por el procedimiento, notificar inmediatamente a CT y Operaciones y convocar decisión ejecutiva urgente. Mantener estado seguro sin eludir congelamiento, alterar plazos contractuales ni interpretar silencio como permiso.',
'S6, T-9, comités de Arquitectura/Operación y cambios; S8, R-022.',
'Solicitar a CT, Operaciones y TI flujo y suplentes al cierre del mes 1; ante incidente, pedir autorización escrita antes del cambio. Sin respuesta, escalar en una hora o antes si lo exige el plazo de atención, manteniendo contención autorizada y estado seguro. El silencio no permite intervenir durante congelamiento.'),
31:('IMP','Gerente de Operaciones y representante de la empresa transportista; supervisor de andén verifica al conductor real.',
'Confirmar por despacho conductor, vehículo y viaje; acreditar identidad, autorización y certificación del reemplazo y registrar la vinculación auditada persona--vehículo--viaje.',
'Pedir nómina y suplentes a D-5 de incorporar la empresa. En cada despacho, confirmar conductor antes de salida; reemplazo no avisado se verifica y vincula en andén antes de habilitar uso.',
'Escalar de inmediato al supervisor de Operaciones y transportista por CT; solicitar conductor certificado y realizar formación extraordinaria del sustituto. No habilitar acceso no autorizado ni contabilizar pruebas incompletas como aceptadas.',
'S3, S-05 y Tabla 3.A.12, Conductores externos.',
'Solicitar a Operaciones y al transportista nómina y suplentes a D-5 de incorporar la empresa y confirmar conductor, vehículo y viaje antes de cada salida. Si falta respuesta o llega un sustituto, escalar, verificar en andén y solicitar conductor certificado; no habilitar uso no autorizado ni acreditar cobertura incompleta.'),
32:('JP','Contraparte Técnica; gerencia solicitante fundamenta la petición y Comité Ejecutivo decide los cambios dentro de sus atribuciones.',
'Entregar solicitud escrita con objetivo y criterio de aceptación; decidir alcance, esfuerzo y programación sobre el análisis de impacto antes de incorporar el cambio a la línea base.',
'Registrar y remitir a CT el mismo día hábil de recibirla; comunicar fecha de decisión necesaria antes de su primera actividad dependiente. No iniciar la implementación hasta aprobación formal.',
'Escalar al Comité Ejecutivo si la decisión amenaza un hito. Mantener la línea base vigente y continuar el trabajo independiente; el silencio no aprueba el cambio ni permite cargar desarrollo adicional.',
'S6, 6.1.4 y T-9, 1.4/1.6; evento R-032.',
'Solicitar por CT a la gerencia peticionaria solicitud escrita y decisión del cambio antes de su primera actividad dependiente; registrar y remitir el mismo día hábil. Ante silencio, mantener línea base y continuar trabajo independiente; si amenaza un hito, escalar al Comité Ejecutivo sin iniciar desarrollo no aprobado.'),
39:('JP','Gerente de Finanzas, con Gerente Comercial para canasta y malla; Contraparte Técnica canaliza conformidad y controversias.',
'Aprobar canasta, índices y regla estacional de 5.4.3, reproducir tres liquidaciones en sombra y conciliar evidencia de cada liquidación y de las diferencias del período.',
'Acordar reglas en meses 17--20, antes de cerrar mes 20. Validar tres liquidaciones en sombra en meses 21--23 antes del primer efecto de pago del mes 24; revisión posterior antes de cerrar cada liquidación.',
'Escalar por CT a Finanzas y al Comité Ejecutivo. Sin regla o reproducción válida no activar el tramo; ante disputa, suspender sólo el devengo del período según el mecanismo contractual y mantener servicio y acompañamiento fijo.',
'S13, 13.4.4--13.4.7, Tablas 13.19 y 13.21--13.22.',
'Solicitar a Finanzas, con Comercial y CT, reglas de 5.4.3 aprobadas al cierre del mes 20 y tres liquidaciones en sombra reproducidas en meses 21--23 antes del pago variable del mes 24. Ante silencio, no activar el tramo; una disputa se escala y suspende sólo el devengo correspondiente según contrato, manteniendo el servicio.'),
}
assert len(data)==20
backup.write_text(json.dumps({'original':{str(p.relative_to(root)):s for p,s in original.items()},'client_ids':[f'R-{n:03}' for n in data]},ensure_ascii=False,indent=2),encoding='utf-8')
b=original[body]
anchor='\\subsection{Escalas previas al análisis}'
govern=r'''\paragraph{Dependencias y decisiones del CLIENTE.}
Para los 20 riesgos que requieren un insumo o decisión del CLIENTE, la Tabla 8.A.2 identifica la contraparte funcional, la solicitud con evidencia, el plazo y la contingencia por falta de respuesta. El dueño LafroX conserva la gestión del riesgo; la contraparte entrega o decide dentro de su autoridad. La Contraparte Técnica (CT) recibe y encauza solicitudes y acepta entregables con acta; no sustituye la decisión sanitaria de Calidad ni la autorización del propietario de un vehículo. El Jefe de Proyecto registra en mes 1 el titular designado y suplente de cada cargo del CLIENTE, sin atribuirle una persona no identificada por este.

Los meses son relativos al inicio contractual. En la matriz, D es la fecha de la actividad o ventana indicada de la línea base vigente; D-10 y D-5 son diez y cinco días hábiles antes de D. LafroX cursa solicitudes completas a D-10 y pide respuesta a D-5, salvo plazo específico más temprano. Para compromisos de mes 1, las cursa en los primeros cinco días hábiles. Cada solicitud incluye ID, antecedentes, decisión o evidencia requerida, destinatario, fecha límite y actividad bloqueada. Las fechas D se registran al programar cada ola o actividad, sin cambiar el calendario contractual. Estos objetivos de coordinación se proponen para acordarlos en el arranque; no acreditan aceptación previa del CLIENTE ni sustituyen los diez días hábiles de revisión y diez de subsanación del art. 18.3 para recepción formal de entregables.

Al vencer una solicitud, el dueño informa a JP y CT el mismo día hábil con la evidencia faltante y efecto en la tarea. JP solicita a CT encauzar la decisión en un día hábil; si sigue sin resolución a los dos días hábiles del vencimiento, pide una instancia extraordinaria al Comité Ejecutivo con la gerencia competente. Una amenaza a seguridad, continuidad o hito se escala inmediatamente, sin esperar ese plazo ni la sesión mensual (S6, 6.1.6; T-9, 1.6). En urgencias rige además el plazo específico de R-022. El silencio activa la contingencia, conserva la tarea dependiente bloqueada y permite continuar sólo trabajo independiente; no aprueba datos, cambios, transferencia, aceptación o desplazamiento de hitos. Resolver la dependencia exige evidencia recibida y validación por la autoridad competente, registradas por JP.

'''
b=b.replace(anchor,govern+anchor,1)
# Local reference and response governance, without estimating response HH or residual risk.
b=b.replace('Las respuestas de la matriz del Anexo 8.A son propuestas de tratamiento derivadas del evento, los disparadores y los responsables consignados en T-16;', 'La Tabla 8.A.1 presenta las respuestas y la Tabla 8.A.2 concreta las 20 dependencias del CLIENTE con su contraparte, solicitud, plazo y contingencia. Las respuestas son propuestas de tratamiento derivadas del evento, los disparadores y los responsables consignados en T-16;')
t=original[form]
lines=[]
for line in t.splitlines():
 if re.match(r'R-\d{3} &',line):
  c=line.split(' & ');n=int(c[0][2:])
  if n in data: c[6]=data[n][6];line=' & '.join(c)
 lines.append(line)
t='\n'.join(lines)+'\n'
t=t.replace('el disparador observable se detalla en el Anexo 8.A.', 'el disparador observable se detalla en la Tabla 8.A.1. Para las 20 dependencias del CLIENTE se explicitan contraparte, solicitud, plazo y contingencia, con evidencia requerida en la Tabla 8.A.2. CT significa Contraparte Técnica; D es la fecha de la actividad indicada y D-10/D-5 son días hábiles anteriores a ella. El protocolo de solicitud y escalamiento se define en 8.1.2 del Subdocumento 8; los plazos de coordinación son propuestos y no alteran la recepción formal de entregables.')
a=original[ann]
old='La matriz presenta una respuesta propuesta para cada riesgo R-001--R-040 del registro vigente. Las descripciones de riesgo, disparadores y responsables se alinean con el Formulario T-16; las respuestas son propuestas de planificación y no acreditan por sí solas controles implementados, eficacia residual, plazo aprobado ni esfuerzo asignado. La estimación de HH de las acciones, su fecha/hito, evidencia de ejecución y contingencia específica deben ser acordadas con cada responsable y registradas en la línea base. La subcontratación no transfiere la obligación contractual final de LafroX.'
new='La Tabla 8.A.1 presenta una respuesta propuesta para cada riesgo R-001--R-040 del registro vigente, con descripciones, disparadores y responsables alineados con el T-16. La Tabla 8.A.2 especifica para las 20 dependencias del CLIENTE la contraparte, solicitud, evidencia, plazo y contingencia por falta de respuesta. Sus objetivos de coordinación se proponen para acuerdo en el arranque; no acreditan una aceptación previa ni la eficacia de las respuestas. La estimación del esfuerzo y la evaluación residual corresponden al desarrollo de los tratamientos. La subcontratación no transfiere la obligación contractual final de LafroX.'
assert old in a;a=a.replace(old,new)
alines=[]
for line in a.splitlines():
 if re.match(r'R-\d{3} &',line):
  c=line.split(' & ');n=int(c[0][2:])
  if n in data and len(c)==4:
   c[2]=data[n][6]+' Evidencia y detalle: Tabla 8.A.2.';line=' & '.join(c)
 alines.append(line)
a='\n'.join(alines)+'\n'
extra=r'''
\subsection*{Dependencias del CLIENTE: compromisos y contingencias}
\addcontentsline{toc}{subsection}{Dependencias del CLIENTE: compromisos y contingencias}

Esta matriz desarrolla los 20 riesgos R-001--R-007, R-011--R-018, R-021--R-022, R-031--R-032 y R-039. Los siete riesgos externos conservan su origen externo y las respuestas de la Tabla 8.A.1; no se atribuye al CLIENTE controlar al SII, un corte de suministro, un siniestro ni un cambio normativo. Los 13 riesgos internos conservan su tratamiento vigente hasta revisar su ubicación. La asignación funcional se apoya en S2, Tabla 2.A.7; S3, consultas de la Tabla 3.A.11 y participación de la Tabla 3.A.12; S6, T-9, 1.3 y 1.6; y S13, 13.4.4--13.4.7. Los plazos adicionales son objetivos de coordinación propuestos por LafroX, no respuestas ya recibidas ni cambios de obligaciones contractuales.

CT es la Contraparte Técnica. En ``ID / dueño'', JP, ARQ, DAT, CAL, IMP y SEG corresponden a las familias y responsables de la Tabla 8.1; desde mes 22 se aplica el relevo allí definido. D identifica la actividad o ventana indicada de la línea base; D-10 y D-5 son días hábiles anteriores. Salvo indicación específica, el dueño envía expediente completo a D-10 y solicita respuesta a D-5; si existe un plazo de mes más temprano, rige ese plazo. Para mes 1 solicita en sus primeros cinco días hábiles. Los plazos formales del art. 18.3 se conservan.

Si falta respuesta, el dueño informa a JP y CT el mismo día hábil del vencimiento. JP pide encauzamiento en un día hábil y, si no se resuelve en dos días hábiles del vencimiento, solicita instancia ejecutiva extraordinaria con la gerencia competente. Las amenazas a seguridad, continuidad o hitos se escalan de inmediato. La columna final añade la contingencia específica; no se espera la reunión mensual para actuar. Toda respuesta se cierra con evidencia validada, no con una promesa o el envío de la solicitud. Los titulares y suplentes por cargo se registran en mes 1 y se actualizan al cambiar su designación.

\begingroup
\renewcommand{\thetable}{8.A.2}
\begin{landscape}
\setlength{\textwidth}{\linewidth}
\begin{tablalafrox}{Contrapartes, solicitudes, plazos y contingencias de las 20 dependencias del CLIENTE. Fuente: asignaciones de S2/S3/S6/S13 y objetivos de coordinación propuestos en S8, 8.1.2.}{tab:sd8-dependencias-cliente}{G{0.07} F{0.17} Y F{0.21} F{0.23}}{\cab{ID / dueño} & \cab{Contraparte del CLIENTE / apoyo} & \cab{Solicitud y evidencia de resolución} & \cab{Plazo de solicitud y respuesta} & \cab{Escalamiento y contingencia por falta de respuesta}}
'''
for n,d in data.items():
 owner,client,req,deadline,fallback,source,summary=d
 extra+=f'R-{n:03} / {owner} & {client} & {req} & {deadline} & {fallback} \\\\\n'
extra+='\\end{tablalafrox}\n\\end{landscape}\n\\endgroup\n'
anchor='\\clearpage\n\\section{Anexo 8.B: Contingencia de esfuerzo por riesgo}'
assert anchor in a;a=a.replace(anchor,extra+'\n'+anchor,1)
for p,s in [(body,b),(ann,a),(form,t)]:p.write_text(s,encoding='utf-8')
note=['# Tarea 3: dependencias del CLIENTE','', 'Completada para los 20 riesgos dependientes del CLIENTE. No se modifican los demás subdocumentos, valoraciones, cuantificación, reservas ni riesgos residuales.','', '## Fuente y decisiones','', 'Contrapartes por cargo verificadas en PDFs vigentes de S2/S3; meses y consultas de S3, Tabla 3.A.11, pp. 162–166; comités y atribuciones de S6/T-9, pp. 7–8; R-039 de S13, pp. 38–41. No se inventan personas ni aprobaciones recibidas. TI coordina revisión de residencia, CT encauza a autoridad del CLIENTE y Gerencia General gestiona la autorización competente; no se atribuye a TI potestad legal propia.','', 'D-10/D-5 y escalamiento operativo en uno/dos días hábiles son propuestas de coordinación para acuerdo al arranque, no obligaciones aceptadas. Las recepciones formales conservan art. 18.3. Los meses son relativos al inicio contractual. R-022 se escala en una hora o antes si el plazo de atención lo exige; no autoriza intervención por silencio.','', '## Trazabilidad por ID','', '| ID | Cargo(s) del CLIENTE | Fuente |', '|---|---|---|']
for n,d in data.items():note.append(f'| R-{n:03} | {d[1]} | {d[5]} |')
note+=['','## Sincronización al terminar las tareas','', 'S6/T-9: incorporar el protocolo de solicitudes D-10/D-5 y los plazos de escalamiento, con sus límites y confirmación de titulares/suplentes. S3: conservar meses de V-07/V-09/V-10/V-11/V-14 y registrar el cierre con evidencia; completar la asignación de Finanzas/TI para cartera y de Bodega/Finanzas para inventario. S7: reflejar insumos previos por ola y solicitud de equipos sin cambiar hitos por silencio, pendiente de conciliación de la tarea 4 y planificación de la tarea 8. S13: conservar reglas de R-039 en meses 17–20 y sombra 21–23 antes del pago variable del mes 24; las valoraciones cambiadas en tarea 2 siguen pendientes de sincronizar.','', 'Para el prompt final: distinguir cargos de decisión de dueños LafroX, compromisos propuestos de acuerdos recibidos y coordinación de terceros de control sobre eventos externos. No se agregan ni eliminan riesgos.']
(root/'odd/tasks/tarea-3-dependencias-cliente.md').write_text('\n'.join(note)+'\n',encoding='utf-8')
print('Actualizadas 20 respuestas T-16, 20 respuestas 8.A.1, nueva matriz 8.A.2 y protocolo en 8.1.2.')
