# REC-012
## Subdocumento 4\LAFROX-Subdocumento4.pdf p.72
LafroX SpA Arquitectura lógica
implementan el contrato. Las pruebas de contrato verifican sustitución, segregación de
interfaces e inversión de dependencias.
4.1.11 Registro de decisiones de arquitectura
Las 22 decisiones de arquitectura se resumen en la Tabla A.18 del Anexo 4-O. Ese anexo
contiene para cada ADR la decisión, alternativas, criterio, consecuencias, evidencia y requisitos
que la sustentan.
La evidencia asociada a cada ficha permite verificar límites de módulo, continuidad por
sitio, protección de datos, desempeño bajo el peak y recuperación del WMS de Talca en la
nube. En ADR-12, la API utiliza de 2 a 4 tareas en el caso base, 7 en la sensibilidad de 91,70
solicitudes/s y las 8 del techo en la cota completa de 111,70 solicitudes/s, incluida la cuota de
20 solicitudes/s del canal tradicional. Esta última cota no deja margen para aumentar la cuota
sin revisar capacidad y latencia.
4.1.12 Puntos únicos de falla y riesgos residuales
RT-02.11 exige identificar las dependencias singulares que subsisten y justificar el riesgo
residual. La Tabla 3 distingue su efecto, la continuidad prevista y la condición de aceptación.
Una réplica o una cola reduce el impacto, pero no elimina por declaración la dependencia.
Tabla 3 Dependencias singulares y riesgo residual
Dependencia Efecto si falla Continuidad prevista Aceptación
Identidad central No hay altas ni
revocación remota.
Asignaciones vigentes y
servicio local.
Prueba de relevo 24 h.
ERP y emisión DTE Se retrasa una nueva
guía, perder la sala de
Talca la detiene hasta
restituir el ERP .
Preemisión nocturna y
ERP por tres caminos. La
salida sin guía válida se
bloquea.
AL-DTE-01 con 96
salidas.
Consolidación
central de stock
La reserva central queda
fechada.
Cada sitio opera
localmente y preventa
captura pedidos sujetos a
validación.
Conciliación de eventos
por sitio.
SII y pasarela de
pago
No hay respuesta en
línea.
Reintento y cobro
alternativo aprobado.
Sin confirmar no
equivale a aprobado.
Planificador
experto
Faltan decisiones ante
excepciones.
Reglas de M4 y suplente
capacitado.
Prueba antes de su retiro.
LafroX SpA
Propuesta Técnica
Media firma: Alex Aravena
72

## Subdocumento 4\LAFROX-Subdocumento4.pdf p.144
LafroX SpA Arquitectura física
• Región sa-east-1 completa. Resolución:Tras autorización del CLIENTE se promueve Aurora,
se restituyen identidad y API y se valida. Entonces Route 53 dirige el tráfico a us-east-1,
Contingencia: RTO de 4 h y RPO de 15 min. Bodega y terreno operan localmente durante la
conmutación.
• Túnel VPN de Talca durante la replicación. Resolución:BGP conmuta entre fibra D-03, LTE
D-04 y Starlink D-06 para que DMS siga leyendo VM-02. Contingencia: La autonomía local
conserva la operación mientras se restituye cualquier camino.
• IdP maestro o enlace de identidad. Resolución: La caché de solo lectura, de 24 h, conserva
los datos de identidad recibidos, y el verificador local habilita los relevos de turno con el
manifiesto firmado y el PIN personal. Contingencia: La credencial de turno dura hasta 8 h
en bodega y 14 h en terreno, sin revocación remota durante el corte, y queda disponible la
cuenta de último recurso (ADR-06, Anexo 4-O).
• Señal móvil en ruta. Resolución: La aplicación opera contra el almacén local del dispositivo.
Contingencia: Sincroniza al reconectar dentro de los 10 min del listado de autonomía por
ámbito.
• ERP legado. Resolución: El trabajador erp-sync en VM-04 retiene las solicitudes en la cola
local o en SQS y reintenta con la misma clave idempotente, Contingencia: Ningún camión
sale sin documento tributario válido emitido por el ERP .
• Perfil de API saturado. Resolución:El balanceador reparte entre tareas y el escalado agrega
tareas cuando los procesos PHP-FPM ocupados superan el 70 %, Contingencia: Limitación
de tasa en API Gateway con mensaje explícito al usuario.
• Mensaje de reconciliación inválido o que falla. Resolución: El consumidor rechaza el
sobre de edición desconocida sin aplicarlo, tras cinco intentos pasa a la cola de mensajes
fallidos, Contingencia: Alarma inmediata y reproceso manual trazable, el grupo afectado
no bloquea a los demás.
• Excursión térmica crítica sin enlace. Resolución:El gateway bloquea el despacho en menos
de 5 s en el borde, Contingencia: Buffer de 24 h y alerta al reconectar.
• SII, cadenas o notificaciones. Resolución: Reintento con espera creciente y cola de mensa-
jes fallidos, Contingencia: Reproceso desde la cola al recuperarse el tercero.
• Carga del peak de septiembre. Resolución: Fargate escala automáticamente por perfil y
Aurora ya está dimensionada para 3× sin cambio de instancia, Contingencia: Limitación de
tasa en API Gateway.
Fuente: elaboración a partir de PUCV (2026b, secciones 14.1–14.2 y 16.1, pp. 24–25 y 28–29), para volumetría y
decisiones abiertas, y LafroX (2026d, diseño de este apartado, pp. 138–145).
Las fallas de nube o enlace no detienen la preparación ni la entrega, que se confirman
localmente. La pérdida de la región primaria deja sin servicio a los portales y a la analítica
hasta promover la réplica. El despacho conserva la guía preemitida al cerrar la carga nocturna.
Si la carga cambia entre las 05:30 y las 07:00, la guía queda inválida y el ERP de Talca emite otra
por cualquiera de sus tres caminos, a los que Concepción y los cross-docking llegan por los
suyos. Si no hay camino hasta el ERP , el camión sale solo con la carga amparada por su guía
LafroX SpA
Propuesta Técnica
Media firma: Alex Aravena
144

## Subdocumento 7\LafroX-Formulario-T-14.pdf p.87
LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 7.45 Diccionario de la cuenta 8.1. Fuente: elaboración a partir de Distribuidora Puelche S.A. (2026a, arts.
17.2–17.6 y Formulario T-14, p. 63); Distribuidora Puelche S.A. (2026b, secs. 17.2–17.6, pp. 32–34).
Código Paquete de
trabajo
Entregable Criterio de
aceptación
Resp. Período
8.1.1 Servicio de
centro de ope-
raciones 24×7
y mesa de
servicio du-
rante los 36
meses de ope-
ración (04:00 a
22:00; 24×7 en
septiembre y
diciembre)
El servicio
prestado du-
rante los 36
meses, con
un informe
mensual de
servicio y un
informe anual
por cada año
de operación.
Se cumplen
los horarios de
cobertura en
cada uno de
los 36 meses.
SRE Meses 21 a 56.
Se paga en el
hito mensual.
8.1.2 Servicio de
gestión de
incidentes,
problemas y
niveles de ser-
vicio del Art.
78° durante los
36 meses de
operación
El servicio
prestado du-
rante los 36
meses, con un
informe men-
sual de niveles
de servicio, los
informes de
causa raíz y un
informe anual.
Se cumplen
los tiempos, y
cada incidente
crítico tiene
su informe a
tiempo.
SRE Meses 21 a 56.
Las multas se
descuentan del
hito mensual.
8.1.3 Servicio de
continuidad
y pruebas
semestrales de
recuperación
ante desastres
durante los
36 meses de
operación
Siete pruebas
de conmuta-
ción en los 36
meses (una
al inicio de la
Operación y
luego dos por
año, la última
en el mes 54),
cada una con
su informe.
Cada prue-
ba alcanza el
RTO y el RPO
comprome-
tidos en una
conmutación
real, progra-
mada fuera de
los congela-
mientos y con
separación má-
xima de seis
meses.
SRE Meses 21, 27,
33, 39, 45, 51 y
54.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
87

# REC-014
## Subdocumento 4\LAFROX-Subdocumento4.pdf p.144
LafroX SpA Arquitectura física
• Región sa-east-1 completa. Resolución:Tras autorización del CLIENTE se promueve Aurora,
se restituyen identidad y API y se valida. Entonces Route 53 dirige el tráfico a us-east-1,
Contingencia: RTO de 4 h y RPO de 15 min. Bodega y terreno operan localmente durante la
conmutación.
• Túnel VPN de Talca durante la replicación. Resolución:BGP conmuta entre fibra D-03, LTE
D-04 y Starlink D-06 para que DMS siga leyendo VM-02. Contingencia: La autonomía local
conserva la operación mientras se restituye cualquier camino.
• IdP maestro o enlace de identidad. Resolución: La caché de solo lectura, de 24 h, conserva
los datos de identidad recibidos, y el verificador local habilita los relevos de turno con el
manifiesto firmado y el PIN personal. Contingencia: La credencial de turno dura hasta 8 h
en bodega y 14 h en terreno, sin revocación remota durante el corte, y queda disponible la
cuenta de último recurso (ADR-06, Anexo 4-O).
• Señal móvil en ruta. Resolución: La aplicación opera contra el almacén local del dispositivo.
Contingencia: Sincroniza al reconectar dentro de los 10 min del listado de autonomía por
ámbito.
• ERP legado. Resolución: El trabajador erp-sync en VM-04 retiene las solicitudes en la cola
local o en SQS y reintenta con la misma clave idempotente, Contingencia: Ningún camión
sale sin documento tributario válido emitido por el ERP .
• Perfil de API saturado. Resolución:El balanceador reparte entre tareas y el escalado agrega
tareas cuando los procesos PHP-FPM ocupados superan el 70 %, Contingencia: Limitación
de tasa en API Gateway con mensaje explícito al usuario.
• Mensaje de reconciliación inválido o que falla. Resolución: El consumidor rechaza el
sobre de edición desconocida sin aplicarlo, tras cinco intentos pasa a la cola de mensajes
fallidos, Contingencia: Alarma inmediata y reproceso manual trazable, el grupo afectado
no bloquea a los demás.
• Excursión térmica crítica sin enlace. Resolución:El gateway bloquea el despacho en menos
de 5 s en el borde, Contingencia: Buffer de 24 h y alerta al reconectar.
• SII, cadenas o notificaciones. Resolución: Reintento con espera creciente y cola de mensa-
jes fallidos, Contingencia: Reproceso desde la cola al recuperarse el tercero.
• Carga del peak de septiembre. Resolución: Fargate escala automáticamente por perfil y
Aurora ya está dimensionada para 3× sin cambio de instancia, Contingencia: Limitación de
tasa en API Gateway.
Fuente: elaboración a partir de PUCV (2026b, secciones 14.1–14.2 y 16.1, pp. 24–25 y 28–29), para volumetría y
decisiones abiertas, y LafroX (2026d, diseño de este apartado, pp. 138–145).
Las fallas de nube o enlace no detienen la preparación ni la entrega, que se confirman
localmente. La pérdida de la región primaria deja sin servicio a los portales y a la analítica
hasta promover la réplica. El despacho conserva la guía preemitida al cerrar la carga nocturna.
Si la carga cambia entre las 05:30 y las 07:00, la guía queda inválida y el ERP de Talca emite otra
por cualquiera de sus tres caminos, a los que Concepción y los cross-docking llegan por los
suyos. Si no hay camino hasta el ERP , el camión sale solo con la carga amparada por su guía
LafroX SpA
Propuesta Técnica
Media firma: Alex Aravena
144

## Subdocumento 5\LAFROX-Subdocumento5.pdf p.19
LafroX SpA Introducción al Modelo y gestión de datos
La identidad fiscal usa tipo/emisor/folio/versión, hash verifica contenido y las referencias
tipadas comprueban la entidad de negocio. POD admite varias evidencias por entrega/intento,
el móvil puede cerrar localmente bajo autorización con evidencia durable, conservando estado
de verificación central posterior.
Un timeout de POS mantiene pago incierto: consulta, conciliación y eventual cancela-
ción/compensación dependen del contrato del tercero. Un pago alternativo necesita autoriza-
ción financiera y vínculo al primero; agotar reintentos no prueba rechazo ni evita por sí mismo
doble cargo. Autoriza un actor con rol financiero distinto del ejecutor. ajuste_redondeo expresa
importe registrado menos importe externo comprobado solo para tarjeta; efectivo/crédito no
fabrican autorización externa. Las cuentas de envases son saldos por cliente/tipo. S4, Anexo
4-M, define AL-DTE-01 y AL-DR-01, su aceptación requiere ensayo.
La cobranza distingue REPARTO, PREVENTA y PORTAL. El preventista registra efectivo
de facturas vencidas del cliente sin entrega ni vehículo, emite recibo provisional digital con
folio único e incorpora el cobro a su rendición diaria en caja, cob_aplicacion vincula pago y
facturas sin duplicar documento_id en el cobro. Una factura ERP puede carecer de carga y
conserva vencimiento, guía de despacho mantiene carga obligatoria. Cartera conserva deuda
por documento, ejecutivo, gestiones, compromisos y recontactos. Mora mayor a treinta días o
cupo excedido bloquea crédito, contado/cobro mantienen permisos. La cartola deriva tramos
del vencimiento y corte, disponible al cliente autenticado en E2 (RF-07.04/ .05/ .07/ .11).
En E2, el pago PORTAL queda EN_REVISION con su comprobante y sin efecto financie-
ro hasta que Tesorería lo aprueba; 5-C define su registro y envío al ERP (RF-07.08; LafroX
SpA., 2026a, 4.1.4.6). Para envases, el umbral versionado por cliente/tipo dispara un aviso al
preventista dentro de 24 h; 5-C precisa la correlación (RF-08.04, caso).
5.1.9 Intercambio electrónico, notificaciones y gobierno del acceso
RT-16.20 de las Bases Técnicas Transversales exige al menos tres canales: correo, notifi-
cación en la aplicación y mensajería instantánea o SMS. El modelo representa correo, aviso
persistente en el portal, WhatsApp y SMS. RT-16.08 corresponde a consulta y exportación de
auditoría, no a canales; sus filtros por persona, período, entidad y operación se conservan en
el dominio de gobierno (RT-16.08 y RT-16.20).
Plantillas, preferencias e intentos comparten CORREO, SMS, WHATSAPP y A VISO_EN_POR-
TAL. La preferencia vigente se identifica por cliente, finalidad, categoría y canal; la planti-
lla/versionado de referencia acredita la elección inicial, sin limitar la baja a esa edición. Antes
de emitir o reintentar se comprueba la baja comercial, que persiste hasta nueva decisión
expresa. Los avisos operacionales obligatorios se distinguen de los comerciales. Los atributos,
nulabilidad y restricciones vigentes se especifican en 5-A–5-C; las vistas gráficas resumen sus
relaciones.
El envío se desacopla mediante outbox y trabajador asíncrono, con reintento por polí-
tica versionada y claves de aviso/intento contra duplicados internos (RF-18.03 / RT-16.23).
not_intento distingue entrega, apertura y error; not_evento conserva evidencia e identidad
del emisor para deduplicar callbacks y reconstruir historia. apertura_estado es INFORMADA,
LafroX SpA
Propuesta Técnica
Media firma: Alex Aravena
19

## Subdocumento 5\LAFROX-Subdocumento5.pdf p.20
LafroX SpA Introducción al Modelo y gestión de datos
NO_INFORMADA o NO_SOPORTADA; solo INFORMADA lleva fecha y evento comprobables.
Acceder explícitamente al aviso del portal bajo sesión autorizada puede acreditar apertura de
ese aviso con origen PORTAL, sin acreditar lectura del SMS. Sin señal no se inventa fecha ni
se concluye «no leído». 5-B/5-C precisan correlación, incertidumbre externa y transiciones;
5-D/5-F, conservación e índices.
La Figura 5.9 desarrolla perfil de cadena, mensajes/ASN, avisos, asignación de roles y
auditoría; las equivalencias y excepciones se especifican en 5-A/5-C. El perfil establece esquema
y campos admitidos; se conserva mensaje original, hash, identidad externa y correlación. Un
reintento devuelve resultado previo sin duplicar efecto. Un código de cadena se traduce a
identidad canónica; no crea cliente/producto por defecto.
La auditoría registra actor, dispositivo, instante, operación, resultado y valores anterio-
res/posteriores mínimos. La excepción conserva contexto histórico, regla y versión; su iden-
tidad es (correlacion_id, clave), no hora de llegada. Los mensajes/notificaciones usan solo
integraciones habilitadas en S4 y su estado de envío no sustituye recepción de mercadería ni
acuse fiscal.
5.1.10 Telemetría, caché y objetos
La Figura 5.10 distingue ingesta térmica cruda en DynamoDB, archivo detallado S3 Par-
quet/Glue, serie/analítica Redshift, posición personal y objetos. Raw dura treinta días; el perfil
detallado y las versiones que lo interpretan permanecen cinco años. El agregado no permite
reconstruir una lectura perdida, por lo que no sustituye el detalle.
S4, Anexo 4-W .4, fija 21 puntos térmicos×288 y 28 termógrafos ×174 =10.920 muestras/día.
Operan tres gateways: dos en Talca y uno en Concepción; las reservas de T-11 no agregan
ingesta ordinaria. El sensor referencia su gateway, sin crear otra autoridad de maestros.
GPS permanece en sa-east-1, raw treinta días y plazo personal total doce meses, sin réplica
internacional. La posición no se confunde con geocerca de configuración. S3_DOCS conserva
originales por clase; Redis contiene lectura reconstruible y Room/SQLite conserva además
hechos/evidencias durables. Las claves, vigencias y purgas están en 5-G.
5.1.11 Modelo lógico del dominio analítico
La Figura 5.7 define hechos y dimensiones para analizar servicio, inventario, cobro y
frío. El grano e identidad de origen evitan duplicados de carga: pedido para compromiso,
entrega/intento para ejecución y línea/asignación para cantidades; la entrega por pedido no
cuenta cada visita como pedido independiente.
LafroX SpA
Propuesta Técnica
Media firma: Alex Aravena
20

# REC-015
## Subdocumento 4\LAFROX-Subdocumento4-Anexos.pdf p.65
LafroX SpA
Tabla A.23 — continuación
Elemen-
to
Amenaza Control y prueba Dueño
M11 T/D: EDI repetido o
inválido.
Firma, equivalencia y UUID,
repetición/rechazo sin crear
pedido.
Canal moderno
M12 I: uso de GPS fuera de
finalidad.
Rol, ruta, retención y consulta
auditada, usuario sin asignación.
Flota/Seguridad
Fuente: elaboración a partir de la especificación de LafroX sobre límites de M1–M12 y RT-11.02. Diseño propuesto:
LafroX (2026e, diseño de este apartado, pp. 64–66).
Tabla A.24 Amenazas en fronteras y terceros
Elemento Amenaza Control y evidencia de aceptación
INT-06/07, ACL y
ERP
T/R: documento
duplicado o incierto.
Clave por carga, consulta antes de reintento y estado
explícito, AL-DTE-01.
INT-08/OpenAS2 S/T: contraparte falsa o
mensaje cambiado.
Certificado registrado, firma y MDN, certificados
desconocidos y hash alterado.
INT-09/POS T/R: doble cobro por
timeout.
Clave de cargo, consulta y conciliación, respuesta tardía
después de alternativa.
INT-10/GIS/
optimizador
D/T: cuotas o ruta
manipulada.
Timeout, límites, ruta aprobada y comprobación de
restricciones.
INT-11/avisos I/T: revelar pedido o
avisar tarde.
Consentimiento/canal, mínimo dato y vigencia, aviso
vencido.
INT-15/GPS I/T: posición falsa o
histórica.
Cursor, fecha y acceso de solo lectura, muestra fuera de
secuencia.
UI-MOV/UI-HHT/
DAT-LOCAL
I/S: pérdida o
préstamo de terminal.
MDM, cifrado, PIN y turno, pérdida y dispositivo no
enrolado.
BOR-PUB/GW-CENT/
AUTH-CENT
S/D: abuso o token
ajeno.
W AF, cuota, JWT y política, firma/audiencia inválida y
ráfaga.
continúa en la página siguiente
LafroX SpA
Propuesta Técnica
Media firma: Alex Aravena
65

## Subdocumento 7\LafroX-Formulario-T-14.pdf p.87
LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 7.45 Diccionario de la cuenta 8.1. Fuente: elaboración a partir de Distribuidora Puelche S.A. (2026a, arts.
17.2–17.6 y Formulario T-14, p. 63); Distribuidora Puelche S.A. (2026b, secs. 17.2–17.6, pp. 32–34).
Código Paquete de
trabajo
Entregable Criterio de
aceptación
Resp. Período
8.1.1 Servicio de
centro de ope-
raciones 24×7
y mesa de
servicio du-
rante los 36
meses de ope-
ración (04:00 a
22:00; 24×7 en
septiembre y
diciembre)
El servicio
prestado du-
rante los 36
meses, con
un informe
mensual de
servicio y un
informe anual
por cada año
de operación.
Se cumplen
los horarios de
cobertura en
cada uno de
los 36 meses.
SRE Meses 21 a 56.
Se paga en el
hito mensual.
8.1.2 Servicio de
gestión de
incidentes,
problemas y
niveles de ser-
vicio del Art.
78° durante los
36 meses de
operación
El servicio
prestado du-
rante los 36
meses, con un
informe men-
sual de niveles
de servicio, los
informes de
causa raíz y un
informe anual.
Se cumplen
los tiempos, y
cada incidente
crítico tiene
su informe a
tiempo.
SRE Meses 21 a 56.
Las multas se
descuentan del
hito mensual.
8.1.3 Servicio de
continuidad
y pruebas
semestrales de
recuperación
ante desastres
durante los
36 meses de
operación
Siete pruebas
de conmuta-
ción en los 36
meses (una
al inicio de la
Operación y
luego dos por
año, la última
en el mes 54),
cada una con
su informe.
Cada prue-
ba alcanza el
RTO y el RPO
comprome-
tidos en una
conmutación
real, progra-
mada fuera de
los congela-
mientos y con
separación má-
xima de seis
meses.
SRE Meses 21, 27,
33, 39, 45, 51 y
54.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
87

# REC-035
## Subdocumento 3\LAFROX-Subdocumento3-Anexos.pdf p.153
LafroX SpA
Tabla 3.A.12 — continuación
Actor Actividad y momento Responsable
LafroX
Indicador Respuesta ante
resistencia
Planifi-
cador de
Rutas
Talleres de reglas (meses 1 a 3) y
validación de rutas propuestas en
marcha blanca.
Líder de Im-
plantación
Reglas documen-
tadas y prueba
de reemplazo
(R18-16).
Sesiones indivi-
duales y recono-
cimiento formal
de su aporte;
ante retiro antici-
pado, validación
con su ayudante
y datos histó-
ricos (LafroX,
2026a, Anexo 2.2,
S-16).
Preven-
tistas (62
personas)
Prueba de captura sin señal en su
ruta y capacitación antes de la ola.
Líder de Im-
plantación
Pedidos captu-
rados en la app
sobre el total.
Acompañamien-
to en ruta.
Tripu-
lación
propia y
peoneta
(84 perso-
nas)
Prueba de entrega digital y rendi-
ción antes de la ola.
Líder de Im-
plantación
Entregas con
POD digital sobre
el total.
Acompañamien-
to en ruta.
Conduc-
tores ex-
ternos
(aprox.
160 perso-
nas)
Confirmación de conductor y
vehículo antes del despacho; au-
tenticación del conductor real al
iniciar la ruta y vinculación au-
ditada persona–vehículo–viaje
(S-05).
Líder de Im-
plantación
Conductores
asignados con
autenticación
válida y vincula-
ción auditada al
vehículo y viaje.
Sin confirmación
previa, vincula-
ción en el andén
(S-05); guía im-
presa y apoyo en
andén.
Empresas
Transp.
(10 empre-
sas)
Firma de acuerdo operacional
(S-05) antes de la ola de reparto.
Jefe de Pro-
yecto
Acuerdos firma-
dos sobre 10.
Ola sin esa em-
presa hasta el
acuerdo.
continúa en la página siguiente
LafroX SpA
Propuesta Técnica
Media firma: Alex Aravena
153

## Subdocumento 7\LafroX-Formulario-T-18.pdf p.13
LafroX SpA Formulario T-18: Propuesta de implantación y puesta en marcha controlada
Tabla 7.6 Perfiles operativos y modalidad de capacitación. Fuente: elaboración a partir de LafroX (2026j, Anexo
3.I) y Distribuidora Puelche S.A. (2026c).
Perfil Personas Cómo se capacita sin detener la operación
Preparadores Talca 120 Aprendizaje en el puesto de 2 horas como máximo
(RNF-05.03) y un tutor por turno; capacitación
continua por la rotación del 38 %
Preparadores Concep-
ción
Por confirmar. Según
supuesto S-39 hasta 60
Aprendizaje en el puesto de hasta 2 horas (RNF-
05.03), tutor por turno y certificación antes del
cierre de la ola. Confirmar nómina, turnos y cober-
tura con el levantamiento del mes 1.
Preventistas 62 Prueba de captura sin señal en su propia ruta y
acompañamiento en ruta
Tripulación propia y
peonetas
84 Prueba de entrega digital y rendición antes de la ola,
y acompañamiento en ruta
Conductores de trans-
portistas
≈ 160 Incorporación en el andén al asignarse a una ruta,
con autenticación y vinculación persona–vehícu-
lo–viaje (S-05)
Los conductores de transportistas no son trabajadores de la compañía. Su incorporación
requiere el acuerdo operacional firmado con cada una de las diez empresas (paquete 5.4.1), y
una ola de reparto no incluye a una empresa transportista hasta que su acuerdo esté firmado
(Capítulo 3, Anexo 3.I; Caso, sección 13.3, p. 23, condición 6). El uso del GPS para control de
jornada requiere el acuerdo previo con el sindicato (paquete 5.4.2; S-13).
7.2.8 Medición de la adopción
La adopción se mide por perfil y por ola con los indicadores del Capítulo 3, Anexo 3.I:
pedidos capturados en la aplicación sobre el total, entregas con prueba digital, preparadores
certificados por turno y conductores con autenticación válida. La meta es que el 100 % de
los usuarios de la ola esté certificado y que el 100 % de las transacciones de la ola se registre
en la solución al retirar el papel. Si una ola no alcanza la meta, no avanza y se extiende el
acompañamiento (paquete 7.2.5).
La respuesta es distinta según el grupo (Caso, sección 17.6, punto 7, p. 33). El personal con
20 o 30 años en la compañía recibe acompañamiento individual en su puesto o ruta y reco-
nocimiento formal de su conocimiento (paquete 7.2.1), y el personal rotativo de preparación
cuenta con un tutor por turno y certificación en el puesto (paquete 7.1.2).
LafroX SpA
Formulario T-18
Media firma: Alex Aravena
13

## Subdocumento 7\LafroX-Formulario-T-18.pdf p.14
LafroX SpA Formulario T-18: Propuesta de implantación y puesta en marcha controlada
7.2.9 Cierre de la marcha blanca y paso a producción
La marcha blanca de la Etapa 1 cierra cuando se cumplen a la vez las seis condiciones del
artículo 17.3 de las Bases Administrativas (p. 13). El paso a producción ocurre en el mes 16,
fuera de las fechas prohibidas, y se formaliza con el acta del H7 (paquete 4.2.3). Si al término del
mes 15 no se cumplen las condiciones, la marcha blanca se extiende a costo del adjudicatario,
sin mover las fechas de las fases siguientes (BA, art. 17.3, p. 13).
7.3 Etapa 2: marcha blanca de los meses 19 y 20 y producción desde el
mes 21
La Etapa 2 se implanta sobre la plataforma ya estabilizada de la Etapa 1, con una marcha
blanca más corta y en convivencia con la Etapa 1 en producción.
7.3.1 Alcance y despliegue
La Etapa 2 pone en producción el intercambio electrónico de pedidos y avisos de despacho
con las cadenas (M11 Canal moderno), el portal de clientes, el portal de transportistas y el
costo de servir por cliente y por entrega (M10). Corresponde a los paquetes 3.5.1 a 3.5.4, 3.6.5
y 3.6.6 del Formulario T-14 y se despliega sobre la plataforma de la Etapa 1, sin rehacer su
arquitectura (BA, art. 15.1, p. 11).
El despliegue avanza por cadena y por grupo de usuarios. Cada cadena se incorpora al
intercambio electrónico cuando su perfil está certificado (paquetes 3.6.5 y 3.6.6) y, hasta
entonces, sus pedidos siguen con carga manual controlada, que no acredita el resultado R18-13.
Los portales se habilitan por grupo de clientes y por transportista, y el costo de servir se habilita
para Comercial y Finanzas con los hechos acumulados desde la marcha blanca de la Etapa 1.
La marcha blanca E2 ocupa meses 19–20. Todo el alcance requerido de cadenas, portales
y costo de servir debe activarse antes de F − 28 días; una cadena todavía no certificada no
se excluye del denominador de aceptación. La operación registra el 100 % de sus pedidos
y entregas reales, con los perfiles certificados y la conciliación requerida. La conversión
promedio de dos meses a 8,7 semanas no determina una fecha límite contractual.
En el escenario ilustrativo de inicio en febrero de 2027 (Anexo 7.A del Subdocumento 7), el
mes 19 cae en agosto de 2028 y el mes 20 en septiembre, lo que tiene tres consecuencias. La
primera es que toda habilitación de la Etapa 2 ocurre en agosto, porque el congelamiento total
va del 1 al 25 de septiembre (Caso, cap. 15, RT-10.05, p. 27), además de respetar F − 28 días y
los primeros tres días hábiles de agosto. La segunda es que la evidencia de cierre atraviesa
septiembre: incluye el volumen real de cada día y el peak cuando ocurre, con pruebas previas
a 1,5 veces la carga peak. Este sería el primer septiembre de E1 en producción, por lo que la
preparación de continuidad de ambas etapas es crítica. La tercera es que entre el 1 y el 25 de
septiembre no se despliega ningún cambio sobre ninguna de las dos etapas: ante un defecto
de la Etapa 2, se aplica la contingencia aprobada conforme a la sección 6.4, sin presumir que
LafroX SpA
Formulario T-18
Media firma: Alex Aravena
14

## Subdocumento 6\LAFROX-Subdocumento6-Anexos.pdf p.7
LafroX SpA
Tabla 6.A.2 — continuación
Bien o servicio Necesidad asociada Responsable de compra o contrato;
responsable LafroX, fecha, paquetes y
evidencia
Gestión de dispositivos
y detección en end-
points
Enrolamiento y seguridad de los
terminales
LafroX (5.2.2). SRE. Antes del enrola-
miento. Paquetes 6.5, 7.1. Suscripcio-
nes activas
Licencias de software
de terceros
Productos de la arquitectura A nombre del CLIENTE (5.2.3). Arqui-
tecto. Antes de usar cada producto.
Paquetes 3.1 a 3.6. Registro de licen-
cias
Fibra óptica de Talca y
Concepción
Enlace principal LafroX (5.3.1). SRE. Antes del H3.
Paquete 6.6. Contrato y fecha de
instalación
Planes LTE de dos pro-
veedores
Respaldo de enlace LafroX (5.3.2). SRE. Antes del H3.
Paquete 6.6. Contratos
Starlink de las tres
plataformas
Enlace de los cross-docking LafroX (5.3.3). SRE. Antes del H3.
Paquete 6.6. Contratos y equipos
Acuerdos con los diez
transportistas
Uso de terminales y suplentes enrola-
dos
LafroX con el CLIENTE (5.4.1). Im-
plantación. Antes del H6. Paquetes
4.2.1, ola de reparto. Diez acuerdos
firmados
Acta con el sindicato Terminales, GPS y cámaras CLIENTE y sindicato (5.4.2). Implan-
tación. Antes del H6. Paquete 4.2.1.
Acta firmada
Custodia de fuentes Continuidad ante insolvencia o in-
cumplimiento
LafroX (5.4.4). Jefe de proyecto. An-
tes del H4. Paquete 9.2. Contrato y
primer depósito
Servicio SOC 24×7, si se
subcontrata
Monitoreo de seguridad desde el mes
13
LafroX (8.1.5; RT-11.17). Encargado
de Seguridad. Mes 13. Paquete 8.1.5.
Contrato con cobertura y niveles de
servicio
La tabla refleja que las adquisiciones tienen responsables y momentos de necesidad distin-
tos: algunas corresponden al CLIENTE y otras a LafroX, y varias deben coordinarse con hitos o
paquetes específicos. Por ello, el seguimiento de fechas y evidencias de recepción o contrata-
ción es clave para anticipar atrasos que puedan afectar la implementación y la continuidad de
LafroX SpA
Propuesta Técnica
Media firma: Alex Aravena
7

# REC-036
## Subdocumento 3\LAFROX-Subdocumento3-Anexos.pdf p.126
LafroX SpA
Tabla 3.A.6 — continuación
ID Supuesto adoptado Fundamento Impacto si resulta
falso
Validación Origen
S-28 Las empresas transpor-
tistas aceptan que se
instale un termógrafo
en sus 10 camiones
con equipo de frío, y
el termógrafo queda
funcionando antes de
que esas rutas partan
con el nuevo proceso
de reparto. El CLIENTE
compra el equipo y
LafroX lo especifica e
integra.
Distribuidora Puel-
che no controla los
vehículos de terce-
ros; el alcance exige
registro continuo de
temperatura en los
vehículos con frío.
Esos 10 camio-
nes quedan sin
registro propio y
habría que exigir
el dato por contra-
to al transportista.
Gerencia
de Opera-
ciones y
transpor-
tistas, mes
6.
Caso, cap.
2.3, p. 5
(flota de
terceros),
y cap. 9, p.
18 (registro
térmico
continuo).
S-29 La discrepancia del
conteo cíclico actual
es de 2,3 % del valor
contado. Conforme al
SD2, las diferencias de
inventario se investigan
y los ajustes se justifi-
can; ese porcentaje es
línea base del proble-
ma y no una tolerancia
automática de migra-
ción. Documentos y
lotes deben coincidir
sin diferencias.
La diferencia entre
inventario contable
y existencias físicas
evidencia la nece-
sidad de conciliar
los datos antes de
migrarlos. El SD2
exige investigar las
diferencias y justi-
ficar los ajustes; la
discrepancia his-
tórica no autoriza
aceptar errores en
la migración (La-
froX, 2026c, Tabla
2.1).
Si el conteo arroja
otra discrepan-
cia, se actualiza
el diagnóstico y
se revisa el sanea-
miento; se mantie-
ne la investigación
y justificación de
cada diferencia.
Contrapar-
te Técnica,
antes de
cada corte.
SD2, Tabla
2.1
continúa en la página siguiente
LafroX SpA
Propuesta Técnica
Media firma: Alex Aravena
126

## Subdocumento 6\LAFROX-Subdocumento6-Anexos.pdf p.6
LafroX SpA
Anexo 6.B --- Adquisiciones asociadas al proyecto
Este anexo reúne los bienes y servicios necesarios para implementar y operar la solución,
e identifica para cada adquisición la necesidad que atiende, quién es responsable de su com-
pra o contratación, cuándo se requiere y qué evidencia permitirá verificar su cumplimiento.
Esta información facilita la coordinación de las adquisiciones con el cronograma y con las
actividades del proyecto.
Tabla 6.A.2 Adquisiciones – Fuente: elaboración propia a partir del Formulario T-14, fase 5, y del Formulario T-11
Bien o servicio Necesidad asociada Responsable de compra o contrato;
responsable LafroX, fecha, paquetes y
evidencia
Equipamiento de te-
rreno: terminales de
preventa, reparto y
bodega, impresoras,
sensores de tempera-
tura, termógrafos y
gateways IoT
Operación de las aplicaciones y
registro de frío
CLIENTE, según la especificación
5.1.1. Arquitecto (especificación);
SRE (recepción). Antes de cada ola;
sensores antes de 6.5. Paquetes 6.5,
4.2.1. Actas 5.1.3
Sala técnica de Talca:
UPS, generador, clima-
tización de precisión,
detección y extinción,
racks y gabinetes de
borde
Recinto técnico del H3 LafroX, según la especificación 5.1.2.
Arquitecto (especificación); SRE
(recepción). Mes 5. Paquetes 6.1, 6.3,
6.6. Actas 5.1.3 y 6.1.5
Servidores, almace-
namiento, firewalls,
switches y mini-PC de
borde
Cómputo y red de los sitios LafroX, según la especificación 5.1.2.
SRE. Mes 5. Paquetes 6.3, 6.6. Actas
5.1.3
Obra civil, piso técnico
e instalación de ener-
gía, climatización e
incendio
Habilitación del recinto LafroX, con instaladores especializa-
dos. SRE. Meses 5 y 6. Paquetes 6.1.1
a 6.1.4. Acta 6.1.5
Servicios de A WS Plataforma de nube y ambientes LafroX (5.2.1). SRE. Antes del mes 4.
Paquetes 3.1, 3.2. Cuentas y servicios
activos
continúa en la página siguiente
LafroX SpA
Propuesta Técnica
Media firma: Alex Aravena
6

# REC-042
## Subdocumento 7\LafroX-Formulario-T-18.pdf p.11
LafroX SpA Formulario T-18: Propuesta de implantación y puesta en marcha controlada
Tabla 7.5 — continuación
Frente de acompañamiento Dotación Cálculo
Coordinación 1 persona Líder de Implantación y Gestión del Cambio
Si la ola cubre solo una zona, la dotación de calle se reduce en proporción a sus rutas, y la
dotación decrece según la curva de adopción, como exige el RT-20.05.
7.2.7 Capacitación y certificación
Cada preparador nuevo, sin experiencia previa con el sistema, completará una misión de
al menos 20 líneas con una tasa de error máxima del 5 % después de un máximo de dos horas
de entrenamiento asistido en su puesto dentro de la bodega. No se exigirán sesiones fuera
del recinto de bodega ni materiales impresos de más de dos páginas (Capítulo 3, Anexo 3.B,
RNF-05.03).
La capacitación se programará por turnos y en horarios acordados con el CLIENTE, sin
interrumpir el despacho de mañana ni la preparación nocturna. El calendario considerará los
peaks de septiembre y diciembre y utilizará las modalidades de acompañamiento y autofor-
mación previstas para mantener la operación (BTT, cap. 22, RT-22.04, p. 38; Caso, cap. 15, pp.
26–27).
La capacitación se hace en el puesto y en la ruta, sin detener la venta ni el reparto (Caso,
sección 13.3, condición 5, p. 23). Usa las cuatro modalidades del artículo 90.2 de las Bases
Administrativas (p. 45): presencial en cada sitio, en línea sincrónica, autoformación en línea y
acompañamiento en el puesto durante la marcha blanca. Cada perfil se certifica antes de cerrar
la marcha blanca, porque el artículo 17.3 de las Bases Administrativas (p. 13) exige personal
«capacitado y certificado conforme al plan de capacitación aprobado» (paquetes 7.1.1 a 7.1.6
y 7.3.1). Los usuarios administradores y el equipo técnico del CLIENTE se certifican además
conforme al artículo 90.4 de las Bases Administrativas (p. 45). La Tabla 7.6 presenta los perfiles
operativos.
LafroX SpA
Formulario T-18
Media firma: Alex Aravena
11

## Subdocumento 7\LafroX-Formulario-T-18.pdf p.13
LafroX SpA Formulario T-18: Propuesta de implantación y puesta en marcha controlada
Tabla 7.6 Perfiles operativos y modalidad de capacitación. Fuente: elaboración a partir de LafroX (2026j, Anexo
3.I) y Distribuidora Puelche S.A. (2026c).
Perfil Personas Cómo se capacita sin detener la operación
Preparadores Talca 120 Aprendizaje en el puesto de 2 horas como máximo
(RNF-05.03) y un tutor por turno; capacitación
continua por la rotación del 38 %
Preparadores Concep-
ción
Por confirmar. Según
supuesto S-39 hasta 60
Aprendizaje en el puesto de hasta 2 horas (RNF-
05.03), tutor por turno y certificación antes del
cierre de la ola. Confirmar nómina, turnos y cober-
tura con el levantamiento del mes 1.
Preventistas 62 Prueba de captura sin señal en su propia ruta y
acompañamiento en ruta
Tripulación propia y
peonetas
84 Prueba de entrega digital y rendición antes de la ola,
y acompañamiento en ruta
Conductores de trans-
portistas
≈ 160 Incorporación en el andén al asignarse a una ruta,
con autenticación y vinculación persona–vehícu-
lo–viaje (S-05)
Los conductores de transportistas no son trabajadores de la compañía. Su incorporación
requiere el acuerdo operacional firmado con cada una de las diez empresas (paquete 5.4.1), y
una ola de reparto no incluye a una empresa transportista hasta que su acuerdo esté firmado
(Capítulo 3, Anexo 3.I; Caso, sección 13.3, p. 23, condición 6). El uso del GPS para control de
jornada requiere el acuerdo previo con el sindicato (paquete 5.4.2; S-13).
7.2.8 Medición de la adopción
La adopción se mide por perfil y por ola con los indicadores del Capítulo 3, Anexo 3.I:
pedidos capturados en la aplicación sobre el total, entregas con prueba digital, preparadores
certificados por turno y conductores con autenticación válida. La meta es que el 100 % de
los usuarios de la ola esté certificado y que el 100 % de las transacciones de la ola se registre
en la solución al retirar el papel. Si una ola no alcanza la meta, no avanza y se extiende el
acompañamiento (paquete 7.2.5).
La respuesta es distinta según el grupo (Caso, sección 17.6, punto 7, p. 33). El personal con
20 o 30 años en la compañía recibe acompañamiento individual en su puesto o ruta y reco-
nocimiento formal de su conocimiento (paquete 7.2.1), y el personal rotativo de preparación
cuenta con un tutor por turno y certificación en el puesto (paquete 7.1.2).
LafroX SpA
Formulario T-18
Media firma: Alex Aravena
13

## Subdocumento 7\LafroX-Formulario-T-14.pdf p.81
LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 7.41 — continuación
Código Paquete de
trabajo
Entregable Criterio de
aceptación
Resp. Período
6.6.3 Borde de los
CD en servicio,
con la prueba
de autonomía
de 24 horas
aprobada
Informe de
la prueba de
autonomía por
sitio.
Cada CD ope-
ra 24 horas
sin enlace y
concilia sin
pérdidas ni
duplicados.
SRE Mes 5, antes
del H3; prue-
bas de acepta-
ción ampliadas
antes del H5.
7.2.7 Fase 7. Capacitación y gestión del cambio
La fase 7 reúne 3 cuentas de control y 13 paquetes de trabajo.
7.2.7.1 Cuenta 7.1 — Capacitación por roles
Esta cuenta de control reúne la capacitación de cada grupo según su rol y su situación.
Todo el material de capacitación de 7.1.5, incluidos manuales por perfil, guías rápidas,
preguntas frecuentes y videos tutoriales, y la base de conocimiento consultable de 3.11.2 y
8.5.3 se entregarán en español, en formato editable y serán de propiedad del CLIENTE (BTT,
cap. 22, RT-22.03, p. 38).
El plan de 7.1.1 acordará con el CLIENTE un calendario para todos los perfiles, por turno
y horario, sin afectar la preparación nocturna, el despacho de 05:30 a 07:00 ni las labores en
calle de lunes a sábado, y considerando los peaks de septiembre y diciembre. La capacitación
de conductores externos se acordará con cada transportista mediante 5.4.1, y la inducción
continua de preparadores de 7.1.2 atenderá la rotación anual del 38 % sin detener la operación
(BTT, cap. 22, RT-22.04, p. 38; Caso, cap. 15, pp. 26–27).
La Tabla 7.42 presenta sus paquetes.
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
81

# REC-049
## Subdocumento 4\LAFROX-Subdocumento4.pdf p.143
LafroX SpA Arquitectura física
presencial (4.2.4.3). Cada equipo tiene dos fuentes, dos SSD en RAID 1 y una interfaz a cada
switch. Contingencia: Reposición del equipo dañado desde la reserva de Talca, si fallan
ambos, reconstrucción desde el estado central y SQS FIFO.
• Firewall de un cross-docking. Resolución:La unidad pasiva del par asume el túnel en menos
de 30 s. Contingencia: La ventana de 3 h opera 100 % local y sincroniza al reconectar.
• Periféricos de andén. Resolución: Sin redundancia por equipo. Contingencia: La etiqueta
se emite en otra de las impresoras del centro de distribución.
• Energía de la sala de Talca. Resolución: UPS N+1 de 30 min y generador que toma carga en
8 a 15 s, Contingencia: Estanque de 24 h y contrato de reabastecimiento.
• Corte de energía en la bodega. Resolución: Las UPS de los gabinetes de piso sostienen
switches PoE, AP e impresoras durante 30 min,Contingencia: Registro de frío con generador
en Talca y UPS de 30 min en Concepción.
• Climatización de la sala de Talca. Resolución: Segunda unidad de precisión en N+1, Con-
tingencia: Alerta del monitoreo de los sensores ambientales.
Fuente: elaboración a partir de PUCV (2026b, secciones 14.1–14.2 y 16.1, pp. 24–25 y 28–29), para volumetría y
decisiones abiertas, y LafroX (2026d, diseño de este apartado, pp. 138–145).
En Concepción, el RAID 10 tolera la falla de un disco y las fuentes redundantes sostienen
cada servidor ante la pérdida de un circuito. Si falla el servidor activo, el de espera toma su
lugar con la base al día, y solo la pérdida de ambos obliga a reconstruirla desde el estado
central alimentado por sus eventos. En Talca, el tablero respaldado por generador mantiene el
registro de frío, y en Concepción la UPS del gabinete permite el apagado ordenado. La tabla
muestra además que los firewalls van en par en los cinco sitios conforme a RT-08.03 (Bases
Técnicas Transversales, cap. 8, p. 18). Concepción y cada cross-docking tienen su cómputo en
un par de equipos activo y en espera (RT-03.14, Bases Técnicas Transversales, cap. 3, p. 9). Cada
cross-docking tiene además dos switches industriales, y cada equipo, alimentación redundante
y discos en RAID 1. El bloqueo sanitario permanece local y el despacho con guía preemitida
puede continuar cuando la carga conserva su autorización sanitaria. Una nueva liberación
corresponde solo a Calidad, conforme a 4.1.3.5 y 4.1.3.7. La consola central requiere conexión y
el perfil Kotlin autorizado usa la puerta local de A-01 con evaluación y auditoría persistentes. Si
el expediente local está incompleto o el permiso no está vigente, el lote permanece bloqueado.
En la ventana de Talca, VM-02 se reinicia en otro nodo y otra impresora emite la etiqueta si
falla la del andén. Los mecanismos de alta disponibilidad se detallan en la sección 4.2.4.3.
4.2.5.4 Puntos de falla en la nube, el terreno y las integraciones
El listado de fallas en nube, terreno e integraciones completa el recorrido con los puntos
de falla que están fuera de los sitios: la nube, el terreno y los sistemas de terceros.
• Zona de disponibilidad de sa-east-1. Resolución: Aurora conmuta en menos de 30 s, Elas-
tiCache en menos de 60 s y Fargate reprograma las tareas, Contingencia: La operación
continúa en las zonas restantes.
LafroX SpA
Propuesta Técnica
Media firma: Alex Aravena
143

## Subdocumento 7\LafroX-Formulario-T-14.pdf p.90
LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 7.46 — continuación
Código Paquete de
trabajo
Entregable Criterio de
aceptación
Resp. Período
8.2.2 Mantenimien-
to de ciberse-
guridad duran-
te los 36 meses
de operación:
vulnerabilida-
des, intrusión
anual e inyec-
ción de fallas
En los 36 me-
ses, los infor-
mes periódi-
cos de vulnera-
bilidades, tres
informes de
intrusión (uno
por año) y seis
de resiliencia
(dos por año).
Se cumplen
los plazos de
corrección; la
prueba anual
termina sin
hallazgos crí-
ticos ni altos
abiertos; hay
dos pruebas de
resiliencia por
año, con sepa-
ración máxima
de seis meses.
SEG Intrusión en
meses 28, 40 y
52; resiliencia
en meses 26,
32, 38, 44, 50 y
55.
8.2.3 Mantenimien-
to del hard-
ware durante
los 36 meses
de operación:
sala técnica,
racks, gabine-
tes de borde y
equipamiento
de terreno
Registro de
mantenimien-
tos de los 36
meses y un
informe anual
por cada año
de operación.
Se cumplen
los manteni-
mientos pro-
gramados, y
ningún equipo
crítico queda
sin repuesto.
SRE Meses 21 a 56.
8.2.4 Registro y re-
ducción de la
deuda técnica
durante los
36 meses de
operación
Registro de
deuda técnica
e informe
trimestral de
su reducción.
El registro está
cuantificado
y se cumple
la fracción
de capacidad
declarada.
DES Meses 21 a 56.
continúa en la página siguiente
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
90

# REC-057
## Subdocumento 4\LAFROX-Subdocumento4-Anexos.pdf p.54
LafroX SpA
ADR-18. Protección de datos fuera del sitio
Decisión adoptada. La extracción continua de DMS/W AL y outbox por fibra, LTE y satélite
sostiene RPO ≤ 15 minutos en los CD.
Alternativas evaluadas. Retención solo en W AL o RabbitMQ local no protege la pérdida del
sitio. Dos caminos terrestres comparten falla.
Criterio de selección. Tres medios con dominios de falla distintos y confirmación durable
externa.
Consecuencias. Se alerta a los 5 y 15 minutos y se mantiene la autonomía local. El aisla-
miento de los tres medios seguido de destrucción puede exceder el RPO. El registro R8-05 no
constituye aceptación del mandante. El escenario, su pérdida potencial y las alternativas de
comunicación requieren resolución contractual explícita.
Evidencia exigida. AL-DR-01 mide puntos consistentes y recupera el WMS de Talca en nube
con los tres caminos ensayados.
Requisitos que la sustentan. RT-07.04 y RT-03.10.
ADR-19. Residencia de datos y regiones
Decisión adoptada. La región primaria es sa-east-1 y la secundaria us-east-1, ambas trans-
ferencias internacionales sujetas a aprobación del CLIENTE.
Alternativas evaluadas. Restringir la propuesta a una sola región impide recuperación
regional, replicar todas las categorías excede minimización.
Criterio de selección. Continuidad con base de licitud, minimización y control contractual.
Consecuencias. A WS actúa como encargado bajo contrato con cláusulas tipo para la Ley
N.° 21.719 (Ley N.° 21.719, 2024). El CLIENTE administra KMS, cifra datos en reposo y tránsito,
audita accesos, excluye la geolocalización de personas de la réplica secundaria y copia la
analítica en forma diferida sin las posiciones de flota. La declaración de ambas regiones, la
base de licitud y los resguardos se someten a la aprobación del CLIENTE como hito de la Etapa
1. us-east-1 ofrece todos los servicios de recuperación del diseño.
Evidencia exigida. Contrato de encargo, registro de tratamiento, aprobación de residencia
y prueba de exclusiones y recuperación.
Requisitos que la sustentan. Art. 23 de las Bases Administrativas (art. 23, p. 17), Ley N.°
21.719, RT-07.04.
ADR-20. Frontend web
Decisión adoptada. Angular con TypeScript y Tailwind sirve portales y consolas con con-
tratos publicados. El Portal de Clientes se publica además como aplicación web progresiva
instalable, que es el perfil de autoatención con operación desconectada exigido por el caso.
Alternativas evaluadas. React ofrece composición flexible pero exige elegir más piezas de
estado y navegación, Vue exige otra cadena de componentes y soporte. Un cuarto perfil del
LafroX SpA
Propuesta Técnica
Media firma: Alex Aravena
54

## Subdocumento 4\LAFROX-Subdocumento4.pdf p.104
LafroX SpA Arquitectura física
desde S3. GuardDuty agrega el agente como sidecar a las tareas nuevas y analiza actividad
de procesos, archivos y red. Las tareas que ya estén ejecutándose se reinician o redespliegan
para que queden cubiertas. Los hallazgos se consolidan en Security Hub, que los entrega al
flujo de respuesta de seguridad para su triage y contención (Amazon Web Services, s. f.-d,
s. f.-e). La cobertura corresponde a ECS sobre Fargate. EKS sobre Fargate no forma parte de la
arquitectura.
Todos los recursos llevan etiquetas obligatorias de ambiente, módulo y centro de costo,
aplicadas desde la infraestructura como código y verificadas antes del despliegue. Con ellas
se entrega al CLIENTE el desglose mensual de consumo en Cost Explorer y se configuran las
alertas de A WS Budgets (RT-03.06, Bases Técnicas Transversales, cap. 3, p. 8).
4.2.3.2 Región secundaria y residencia de los datos
La región us-east-1 no es una segunda producción. Solo contiene recursos para la recupera-
ción:
• Datos: réplica de Aurora mediante Aurora Global Database y de las tablas de temperatura
de DynamoDB mediante Global Tables.
• Respaldos: copia de los buckets de S3 salvo el de geolocalización y copias de A WS Backup.
• Aplicación: réplica reducida de ECS que escala a carga completa en menos de 30 minutos
durante una conmutación.
• Imágenes: réplica de las imágenes de Elastic Container Registry, que recibe cada entrega
liberada en Producción.
• Mensajería: colas SQS FIFO y SQS, y temas SNS equivalentes, creados vacíos por infraes-
tructura como código para la conmutación.
La región primaria sa-east-1 está en São Paulo, Brasil, y la secundaria us-east-1 en Virginia
del Norte, Estados Unidos. Ambas suponen transferencia internacional de datos desde Chile.
Los datos de geolocalización de personas quedan fuera de la región secundaria. La analítica
se copia a ella en forma diferida, sin las posiciones de flota, porque conserva los registros de
temperatura y de trazabilidad de lote que el caso exige retener cinco años (Bases Técnicas
del caso, cap. 15, p. 26). La base de licitud, los resguardos de tratamiento y la garantía de
continuidad ante las decisiones de residencia del CLIENTE se desarrollan en la sección 4.3.2.
4.2.3.3 Servicios que no se contratan
Los registros de decisión descartan de forma expresa los siguientes servicios y productos,
que no aparecen en la arquitectura:
• No se instala Redis ni Laravel Horizon en los sitios, porque la continuidad local descansa
en PostgreSQL y RabbitMQ, y un tercer motor por sitio agregaría operación sin beneficio.
• No se contrata un clúster de Kubernetes (EKS). El monolito modular se despliega en pocos
LafroX SpA
Propuesta Técnica
Media firma: Alex Aravena
104

# REC-061
## Subdocumento 4\LAFROX-Subdocumento4-Anexos.pdf p.64
LafroX SpA
Anexo 4-Q --- Modelado de amenazas lógicas
STRIDE se aplica por módulo, componente transversal e integración externa (RT-11.02). S
representa suplantación; T, alteración; R, repudio; I, divulgación; D, denegación; E, elevación
de privilegios. Cada escenario tiene una prueba negativa y un dueño. El registro se reevalúa
al cambiar un contrato o límite de confianza. Esta matriz registra amenazas de diseño, no
resultados de pentesting.
Tabla A.23 Amenazas de los doce módulos
Elemen-
to
Amenaza Control y prueba Dueño
M1 T: lote o recepción
falsa.
GS1, cuarentena y evidencia,
rechazar lote sin origen.
Recepción/Calidad
M2 T/D: reserva duplicada. Escritor único, UUID y bloqueo
por agregado, doble compromiso.
Inventario
M3 S/T: pedido con
identidad ajena.
Turno, dispositivo y firma, token
inválido y reenvío.
Comercial/Seguridad
M4 T: ruta con restricción
omitida.
Restricción versionada,
aprobación y motivo, ruta
incompatible.
Operaciones
M5 E: liberar carga
retenida.
Política por recurso y documento
vigente, supervisor sin permiso.
Bodega/Calidad
M6 R/T: POD alterado. Hash, autor, hora y vínculo guía,
objeto con hash distinto.
Reparto
M7 E/R: aprobar cobro
propio.
Segregación y conciliación,
mismo autor registrador/
aprobador.
Tesorería
M8 T: devolución o saldo
ficticio.
Causal, lote, evidencia y disputa,
devolución repetida.
Bodega/Tesorería
M9 T/E: ocultar excursión. Alarma local y liberación
exclusiva de Calidad, muestra
alterada.
Calidad
M10 I: exponer crédito por
tablero.
Modelo autorizado, filtros y
auditoría, consulta de otro
cliente.
Datos/Seguridad
continúa en la página siguiente
LafroX SpA
Propuesta Técnica
Media firma: Alex Aravena
64

## Subdocumento 4\LAFROX-Subdocumento4-Anexos.pdf p.65
LafroX SpA
Tabla A.23 — continuación
Elemen-
to
Amenaza Control y prueba Dueño
M11 T/D: EDI repetido o
inválido.
Firma, equivalencia y UUID,
repetición/rechazo sin crear
pedido.
Canal moderno
M12 I: uso de GPS fuera de
finalidad.
Rol, ruta, retención y consulta
auditada, usuario sin asignación.
Flota/Seguridad
Fuente: elaboración a partir de la especificación de LafroX sobre límites de M1–M12 y RT-11.02. Diseño propuesto:
LafroX (2026e, diseño de este apartado, pp. 64–66).
Tabla A.24 Amenazas en fronteras y terceros
Elemento Amenaza Control y evidencia de aceptación
INT-06/07, ACL y
ERP
T/R: documento
duplicado o incierto.
Clave por carga, consulta antes de reintento y estado
explícito, AL-DTE-01.
INT-08/OpenAS2 S/T: contraparte falsa o
mensaje cambiado.
Certificado registrado, firma y MDN, certificados
desconocidos y hash alterado.
INT-09/POS T/R: doble cobro por
timeout.
Clave de cargo, consulta y conciliación, respuesta tardía
después de alternativa.
INT-10/GIS/
optimizador
D/T: cuotas o ruta
manipulada.
Timeout, límites, ruta aprobada y comprobación de
restricciones.
INT-11/avisos I/T: revelar pedido o
avisar tarde.
Consentimiento/canal, mínimo dato y vigencia, aviso
vencido.
INT-15/GPS I/T: posición falsa o
histórica.
Cursor, fecha y acceso de solo lectura, muestra fuera de
secuencia.
UI-MOV/UI-HHT/
DAT-LOCAL
I/S: pérdida o
préstamo de terminal.
MDM, cifrado, PIN y turno, pérdida y dispositivo no
enrolado.
BOR-PUB/GW-CENT/
AUTH-CENT
S/D: abuso o token
ajeno.
W AF, cuota, JWT y política, firma/audiencia inválida y
ráfaga.
continúa en la página siguiente
LafroX SpA
Propuesta Técnica
Media firma: Alex Aravena
65

## Subdocumento 7\LafroX-Formulario-T-14.pdf p.88
LafroX SpA Formulario T-14: Plan de trabajo, EDT y carta Gantt
Tabla 7.45 — continuación
Código Paquete de
trabajo
Entregable Criterio de
aceptación
Resp. Período
8.1.4 Actualizacio-
nes anuales
del Plan de
Reversibilidad
durante los
36 meses de
operación
Tres actuali-
zaciones del
plan, una por
año de opera-
ción.
En cada ac-
tualización,
el inventario,
las claves y la
exportación
están vigentes.
JP Meses 27, 39 y
51, continuan-
do la serie
anual que ini-
cia 1.7.2 (Art.
77.2).
8.1.5 Servicio de
centro de ope-
raciones de
seguridad 24×7
con SIEM des-
de la primera
marcha blanca
(mes 13) hasta
el mes 56
El servicio
prestado desde
el mes 13 hasta
el mes 56, con
un informe
mensual de
seguridad.
Cobertura
24×7 todos
los meses,
cada incidente
crítico avisado
dentro de
dos horas y
cada brecha
notificada
dentro de 24
horas.
SEG Meses 13 a 56.
8.1.6 Pruebas men-
suales de res-
tauración de
respaldos du-
rante los 36
meses de ope-
ración
36 informes de
restauración,
uno por mes.
Cada mes la
restauración
funciona sin
errores, con
su tiempo
medido.
SRE Mensual, me-
ses 21 a 56.
7.2.8.2 Cuenta 8.2 — Mantenimiento
Esta cuenta de control reúne el trabajo que mantiene la solución sana y actualizada, sepa-
rado por tipo: software, ciberseguridad y hardware.
LafroX destinará las 2.304 HH DES de 8.2.4 a reducir la deuda técnica durante los 36 meses
de Operación, equivalentes al 1,7948 % de las 128.373,67 HH de esa etapa: 2.304 ÷ 128.373,67
× 100 = 1,7948 %. Esa capacidad equivale a 2.304 ÷ 36 = 64 HH mensuales y 64 × 12 = 768
HH anuales, con seguimiento en el registro cuantificado y el informe trimestral existentes;
la fracción corresponde al total del período (BTT, cap. 21, RT-21.21, p. 38; Formulario T-15,
secciones 4.2, 4.3 y 6.2).
El paquete 8.2.1 reparte sus 4.608 HH DES, es decir 4.608 ÷ 3 = 1.536 HH por año de
LafroX SpA
Formulario T-14
Media firma: Alex Aravena
88

# REC-062
## Subdocumento 4\LAFROX-Subdocumento4-Anexos.pdf p.65
LafroX SpA
Tabla A.23 — continuación
Elemen-
to
Amenaza Control y prueba Dueño
M11 T/D: EDI repetido o
inválido.
Firma, equivalencia y UUID,
repetición/rechazo sin crear
pedido.
Canal moderno
M12 I: uso de GPS fuera de
finalidad.
Rol, ruta, retención y consulta
auditada, usuario sin asignación.
Flota/Seguridad
Fuente: elaboración a partir de la especificación de LafroX sobre límites de M1–M12 y RT-11.02. Diseño propuesto:
LafroX (2026e, diseño de este apartado, pp. 64–66).
Tabla A.24 Amenazas en fronteras y terceros
Elemento Amenaza Control y evidencia de aceptación
INT-06/07, ACL y
ERP
T/R: documento
duplicado o incierto.
Clave por carga, consulta antes de reintento y estado
explícito, AL-DTE-01.
INT-08/OpenAS2 S/T: contraparte falsa o
mensaje cambiado.
Certificado registrado, firma y MDN, certificados
desconocidos y hash alterado.
INT-09/POS T/R: doble cobro por
timeout.
Clave de cargo, consulta y conciliación, respuesta tardía
después de alternativa.
INT-10/GIS/
optimizador
D/T: cuotas o ruta
manipulada.
Timeout, límites, ruta aprobada y comprobación de
restricciones.
INT-11/avisos I/T: revelar pedido o
avisar tarde.
Consentimiento/canal, mínimo dato y vigencia, aviso
vencido.
INT-15/GPS I/T: posición falsa o
histórica.
Cursor, fecha y acceso de solo lectura, muestra fuera de
secuencia.
UI-MOV/UI-HHT/
DAT-LOCAL
I/S: pérdida o
préstamo de terminal.
MDM, cifrado, PIN y turno, pérdida y dispositivo no
enrolado.
BOR-PUB/GW-CENT/
AUTH-CENT
S/D: abuso o token
ajeno.
W AF, cuota, JWT y política, firma/audiencia inválida y
ráfaga.
continúa en la página siguiente
LafroX SpA
Propuesta Técnica
Media firma: Alex Aravena
65

## Subdocumento 4\LAFROX-Subdocumento4.pdf p.47
LafroX SpA Arquitectura lógica
bajo contrato con cláusulas tipo. El CLIENTE administra KMS y la geolocalización de personas
se excluye de la réplica secundaria, conforme se desarrolla en 4.3.2 (Bases Técnicas del caso,
cap. 15, pp. 26–30; Bases Técnicas Transversales, cap. 11, pp. 23–24; RT-11.08–11.10 y RT-16.09).
El CLIENTE consulta y exporta la auditoría desde la consola Angular mediante la API
Laravel, con filtros combinables por persona, período, entidad y tipo de operación, sin acceso
a la base de datos. La consulta reutiliza los campos del registro de auditoría y exporta el
resultado filtrado en CSV UTF-8 o JSON bajo los permisos del perfil. Para volúmenes extensos
emplea el trabajo asíncrono, seguimiento y descarga protegida de 5.2.8 (LafroX, 2026a, sección
5.2.8; LafroX, 2026b, Anexo 5-A; RT-16.08, Bases Técnicas Transversales, cap. 16, p. 29).
Amenazas, controles y evidencia. El modelado STRIDE toma cada módulo y cada integración
externa como unidad de revisión, identifica su límite de confianza, abuso posible, mitigación,
responsable y prueba.
• Para M3, el abuso es reutilizar una credencial o reenviar un pedido: se comprueban enrola-
miento, vigencia e idempotencia.
• Para M5, la elevación indebida de privilegios no debe liberar una carga bloqueada por M9:
se prueba la separación de autorizaciones.
• Para M11 y la ACL, un mensaje EDI repetido o manipulado se rechaza o aísla sin escribir
dos veces en el ERP . El Anexo 4-Q registra las amenazas por módulo y frontera. El Anexo
4-R vincula controles ISO/IEC 27001/27002 con responsable y prueba. Son especificaciones
de aceptación, no resultados de ensayos ni certificación (ISO, 2022b, 2022c) (RT-11.02 y
RT-11.05, Bases Técnicas Transversales, cap. 11, p. 23).
Cada decisión de acceso y cada acción crítica conserva sujeto, empresa si aplica, recurso,
operación, resultado, hora, identificador de transacción y regla aplicada. Los eventos de
seguridad se envían a una bitácora inalterable y al SIEM. Durante un corte se conservan
localmente y se remiten con el mismo identificador al reconectar. Las reglas de detección
incluyen acceso privilegiado fuera de turno, intentos reiterados de uso de una credencial
de conductor revocada, consulta masiva de datos comerciales, alteración de evidencia de
temperatura y desvío anómalo de mensajes EDI. Los registros técnicos en CloudWatch se
conservan 12 meses en línea y 24 meses adicionales en archivo. Los registros de seguridad y
auditoría se conservan 7 años bajo Object Lock. La retención de documentos tributarios y POD
se gobierna separadamente por su dominio de datos. La plataforma que opera estos controles
se describe en 4.2, y la dotación del SOC, en el Anexo 4-W (RT-11.14–11.19, Bases Técnicas
Transversales, cap. 11, p. 24).
La aceptación de esta vista requiere
• una prueba de acceso denegado por rol y atributo,
• una de cifrado de campo con lectura administrativa sin texto claro,
• una de continuidad y relevo offline,
• una de revocación al reconectar y
LafroX SpA
Propuesta Técnica
Media firma: Alex Aravena
47

# REC-063
## Subdocumento 4\LAFROX-Subdocumento4-Anexos.pdf p.65
LafroX SpA
Tabla A.23 — continuación
Elemen-
to
Amenaza Control y prueba Dueño
M11 T/D: EDI repetido o
inválido.
Firma, equivalencia y UUID,
repetición/rechazo sin crear
pedido.
Canal moderno
M12 I: uso de GPS fuera de
finalidad.
Rol, ruta, retención y consulta
auditada, usuario sin asignación.
Flota/Seguridad
Fuente: elaboración a partir de la especificación de LafroX sobre límites de M1–M12 y RT-11.02. Diseño propuesto:
LafroX (2026e, diseño de este apartado, pp. 64–66).
Tabla A.24 Amenazas en fronteras y terceros
Elemento Amenaza Control y evidencia de aceptación
INT-06/07, ACL y
ERP
T/R: documento
duplicado o incierto.
Clave por carga, consulta antes de reintento y estado
explícito, AL-DTE-01.
INT-08/OpenAS2 S/T: contraparte falsa o
mensaje cambiado.
Certificado registrado, firma y MDN, certificados
desconocidos y hash alterado.
INT-09/POS T/R: doble cobro por
timeout.
Clave de cargo, consulta y conciliación, respuesta tardía
después de alternativa.
INT-10/GIS/
optimizador
D/T: cuotas o ruta
manipulada.
Timeout, límites, ruta aprobada y comprobación de
restricciones.
INT-11/avisos I/T: revelar pedido o
avisar tarde.
Consentimiento/canal, mínimo dato y vigencia, aviso
vencido.
INT-15/GPS I/T: posición falsa o
histórica.
Cursor, fecha y acceso de solo lectura, muestra fuera de
secuencia.
UI-MOV/UI-HHT/
DAT-LOCAL
I/S: pérdida o
préstamo de terminal.
MDM, cifrado, PIN y turno, pérdida y dispositivo no
enrolado.
BOR-PUB/GW-CENT/
AUTH-CENT
S/D: abuso o token
ajeno.
W AF, cuota, JWT y política, firma/audiencia inválida y
ráfaga.
continúa en la página siguiente
LafroX SpA
Propuesta Técnica
Media firma: Alex Aravena
65

## Subdocumento 3\LAFROX-Subdocumento3-Anexos.pdf p.122
LafroX SpA
Tabla 3.A.6 — continuación
ID Supuesto adoptado Fundamento Impacto si resulta
falso
Validación Origen
S-19 El CLIENTE puede ac-
ceder a los datos de
telemetría del provee-
dor actual.
Existe un servicio
de telemetría pa-
ra la flota propia.
Su integración re-
quiere acceso a
los datos, cuyas
condiciones deben
confirmarse con el
proveedor.
LafroX propone
un mecanismo
alternativo con
igual cobertura de
posición, veloci-
dad y kilometraje
de los 42 camiones
propios, sujeto a
autorización del
CLIENTE; la cober-
tura de RF-14.01
no se reduce.
Jefe de TI y
proveedor
de teleme-
tría, mes
2.
S-20 El hardware de terreno
lo compra el CLIENTE
con la especificación
de LafroX, antes de
cada ola.
La compra del hard-
ware corresponde
al CLIENTE y su
disponibilidad con-
diciona cada ola.
La especificación
de LafroX permite
coordinar la ad-
quisición con el
despliegue.
La ola afectada
se posterga den-
tro de la holgura
disponible y se
aplica un plan de
recuperación para
mantener los hitos
contractuales. Si
la demora supera
esa holgura, se
registra y escala
el impacto con
medidas de miti-
gación, sin asumir
una modificación
automática de los
hitos.
Gerencia
de Ope-
raciones,
según ca-
lendario
de olas.
)
continúa en la página siguiente
LafroX SpA
Propuesta Técnica
Media firma: Alex Aravena
122
