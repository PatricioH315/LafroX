# Subdocumento 7 — Plan de trabajo

> Texto extraído del [PDF final](LafroX-Subdocumento7.pdf). Las figuras y la composición visual se consultan en el PDF.

LafroX SpA
VERSIÓN FINAL PARA ENTREGA
LICITACIÓN PÚBLICA
Licitación N.° TFEP-01/2026
Proyecto de Plataforma Digital de Misión Crítica
Caso — Logística
Sobre N.° 2 --- Oferta Técnica
Subdocumento 7
Plan de Trabajo, EDT, Cronograma e Implantación
Subdocumento 7 · Formulario T-14
MANDANTE
Distribuidora Puelche S.A.
PROPONENTE
LafroX SpA
RUT 77.418.902-K
Av. Brasil 2241, Valparaíso
REPRESENTANTE LEGAL
Alex Aravena
Jefe de Proyecto y Apoderado
contacto@lafrox.cl
+56 32 250 4100
FECHA DE EMISIÓN
12 de octubre de 2026
FIRMA DEL REPRESENTANTE LEGAL
Alex Aravena
Jefe de Proyecto y Apoderado · LafroX SpA
SOBRE2_LAFROX_OFERTA_TECNICA_20261012.ZIP 1


---

LafroX SpA
Índice general
Índice general 2
Lista de tablas 3
Lista de figuras 4
7 Introducción al Plan de trabajo 6
7.1 EDT 6
7.1.1 Criterio de descomposición 6
7.1.2 Estructura general 9
7.1.2.1 Fase 1. Inicio 9
7.1.2.2 Fase 2. Elaboración 11
7.1.2.3 Fase 3. Construcción 13
7.1.2.4 Fase 4. Transición 18
7.1.2.5 Fase 5. Adquisiciones y contrataciones 19
7.1.2.6 Fase 6. Infraestructura física y sitios 20
7.1.2.7 Fase 7. Capacitación y gestión del cambio 22
7.1.2.8 Fase 8. Operación y soporte 23
7.1.2.9 Fase 9. Cierre 25
7.1.3 Cobertura del alcance 26
7.1.4 Diccionario y asignación de responsables 29
7.2 Plan de trabajo 30
7.2.1 Secuenciamiento y dependencias 30
7.2.2 Estimación 34
7.2.3 Frentes de trabajo y sincronización 36
7.2.4 Solapamientos de los meses 13 a 15 y 19 a 20 38
7.3 Cronograma e implantación 38
7.3.1 Ruta crítica y holguras 38
7.3.2 Carta Gantt y calendario 41
7.3.3 Plan de implantación y puesta en marcha 45
7.3.4 Marcha blanca de la Etapa 1 49
7.3.5 Marcha blanca de la Etapa 2 y convivencia 52
7.3.6 Estabilización y transferencia 53
7.3.7 Momento de los resultados comprometidos 54
7.3.8 Base de planificación y recursos 56
Referencias 58
Declaración de uso de IA 58
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
2


---

LafroX SpA
Lista de tablas
Tabla 7.1 Cuentas de control y paquetes por fase. 8
Tabla 7.2 Cobertura del alcance en la EDT. 27
Tabla 7.3 Paquetes por responsable. 29
Tabla 7.4 Horas hombre programadas por etapa — 35
Tabla 7.5 Hitos del Formulario E-25 en el cronograma. 41
Tabla 7.6 Meses contractuales según la fecha de inicio. 43
Tabla 7.7 Olas de implantación de la Etapa 1. 45
Tabla 7.8 Niveles de reversión. 47
Tabla 7.9 Indicadores diarios de la marcha blanca. 50
Tabla 7.10 Estabilización por ola. 53
Tabla 7.11 Momento de los resultados de aceptación del caso. 54
Tabla 7.12 Innovaciones en el cronograma. 55
Tabla 7.13 Declaración de uso de IA. 59
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
3


---

LafroX SpA
Lista de figuras
Figura 7.1 Vista del primer nivel de la EDT: raíz del proyecto y sus nueve fases. 9
Figura 7.2 Fase 1 — Inicio, primera parte: cuentas 1.1 a 1.5. 10
Figura 7.3 Fase 1 — Inicio, segunda parte: cuentas 1.6 a 1.9, desde riesgos hasta cumpli-
miento contractual. 11
Figura 7.4 Fase 2 — Elaboración, primera parte: arquitectura, seguridad y sala técnica,
cuentas 2.1 a 2.3. 12
Figura 7.5 Fase 2 — Elaboración, segunda parte: validación, continuidad y experiencia
de usuario, cuentas 2.4 a 2.6. 13
Figura 7.6 Fase 3 — Construcción, primera parte: ambientes, servicios de nube y base
compartida, cuentas 3.1 a 3.3. 14
Figura 7.7 Fase 3 — Construcción, segunda parte: módulos de la Etapa 1, cuenta 3.4. 15
Figura 7.8 Fase 3 — Construcción, tercera parte: módulos de la Etapa 2, integraciones,
migración y pruebas de la Etapa 1, cuentas 3.5 a 3.8. 16
Figura 7.9 Fase 3 — Construcción, cuarta parte: pruebas de la Etapa 2, innovaciones y
documentación técnica, cuentas 3.9 a 3.11. 17
Figura 7.10 Fase 3 — Construcción, quinta parte: detalle de los paquetes de las innova-
ciones agrupadas en la cuenta 3.10. 18
Figura 7.11 Fase 4 — Transición: plan de implantación y marchas blancas de las etapas 1
y 2, cuentas 4.1 a 4.3. 19
Figura 7.12 Fase 5 — Adquisiciones y contrataciones: hardware, servicios, enlaces y
acuerdos con terceros, cuentas 5.1 a 5.4. 20
Figura 7.13 Fase 6 — Infraestructura física y sitios, primera parte: sala técnica, cableado
y racks, cuentas 6.1 a 6.3. 21
Figura 7.14 Fase 6 — Infraestructura física y sitios, segunda parte: seguridad física,
equipamiento de campo y configuración, cuentas 6.4 a 6.6. 22
Figura 7.15 Fase 7 — Capacitación y gestión del cambio: capacitación por roles, acompa-
ñamiento y certificaciones, cuentas 7.1 a 7.3. 23
Figura 7.16 Fase 8 — Operación y soporte, primera parte: servicios de operación y
mantenimiento, cuentas 8.1 y 8.2. 24
Figura 7.17 Fase 8 — Operación y soporte, segunda parte: innovaciones, obligaciones
periódicas, capacitación y transferencia, cuentas 8.3 a 8.5. 25
Figura 7.18 Fase 9 — Cierre: cierre de implementación y salida al término del contrato,
cuentas 9.1 y 9.2. 26
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
4


---

LafroX SpA
Figura 7.19 Ubicación en la EDT de las innovaciones y la seguridad, la calidad, la migra-
ción y la implantación. 28
Figura 7.20 Red de precedencias entre cuentas de control e hitos. 33
Figura 7.21 Frentes de trabajo de los meses 1 a 21. 37
Figura 7.22 Dependencias y caminos de menor holgura del escenario nominal histórico;
sujetos a recálculo. 40
Figura 7.23 Carta Gantt resumida de los 56 meses, con inicio en febrero de 2027. 44
Figura 7.24 Secuencia de olas de la Etapa 1 durante la marcha blanca. 47
Figura 7.25 Procedimiento de reversión de la Etapa 1 en la ventana de despacho. 49
Figura 7.26 Ciclo diario de la marcha blanca. 51
Figura 7.27 Convivencia de la Etapa 1 en producción con la Etapa 2 en marcha blanca. 53
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
5


---

CAPÍTULO 7
Introducción al Plan de trabajo
Este capítulo presenta cómo LafroX ejecutará el proyecto de Distribuidora Puelche dentro
del cronograma contractual obligatorio de 56 meses (BA, art. 17, pp. 12–13): qué trabajo se
hace, en qué orden, con qué esfuerzo y cómo la solución entra en operación sin detener la
venta, la bodega ni el reparto.
La sección 7.1 descompone el 100 % del alcance en una estructura de descomposición del
trabajo (EDT) con paquetes estimables y asignables. La sección 7.2 secuencia ese trabajo y
lo organiza en frentes paralelos, con especial atención a los meses 13 a 15 y 19 a 20, en que
dos esfuerzos coexisten. La sección 7.3 presenta la ruta crítica, la carta Gantt con los hitos del
Formulario E-25 y el plan de implantación y de marcha blanca de cada etapa.
El capítulo se apoya en otros tres capítulos de la oferta: el Capítulo 3 fija el alcance de cada
etapa y los criterios de olas y estabilización; la sección 6 del Formulario T-18 concreta una
propuesta de calendario, dotación y decisiones; el Capítulo 4 define los módulos M1 a M12
y las interfaces que la EDT construye; y el Capítulo 6 (LafroX, 2026o) establece el proceso de
desarrollo cuyas fases organizan la EDT y la gestión del proyecto que la controla. El detalle va
en tres formularios y un archivo de anexos: el Formulario T-14 contiene la EDT completa, su
diccionario y la carta Gantt; el Formulario T-15, el método de estimación y programación, la
ruta crítica y los frentes de trabajo; el Formulario T-18, la implantación y la puesta en marcha
controlada; y los Anexos 7.A a 7.F, los listados de apoyo y la preparación de riesgos.
En este capítulo, BA, BTT y Caso designan las Bases Administrativas (Distribuidora Puelche
S.A., 2026a), las Bases Técnicas Transversales (2026b) y las Bases Técnicas del Caso Logística
(2026c).
7.1 EDT
La EDT es la base común del plan: el cronograma, la estimación y la asignación de respon-
sables se construyen sobre sus paquetes, y su diccionario fija qué se entrega y cómo se acepta
cada uno. Esta sección explica cómo se descompuso el trabajo, cómo queda la estructura, cómo
cubre el alcance y cómo se asignan los responsables.
7.1.1 Criterio de descomposición
La EDT de Puelche se organiza en nueve fases. Las cuatro primeras son las fases del proceso
de desarrollo del Capítulo 6 (Inicio, Elaboración, Construcción y Transición) y se recorren una
vez por cada etapa del artículo 17 de las Bases Administrativas (pp. 12–13). El primer recorrido
produce la Etapa 1, con la trazabilidad de recepción, la bodega, la cadena de frío, la preventa,
las rutas, el reparto y la rendición, y termina con el paso a producción del mes 16. El segundo
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
6


---

LafroX SpA Introducción al Plan de trabajo
produce la Etapa 2, con el canal moderno, los portales y el costo de servir, y termina con el
paso a producción del mes 21.
Las otras cinco fases agrupan el trabajo que no es desarrollo de software, pero sin el cual la
solución no entra en operación: adquisiciones y contrataciones; infraestructura física y sitios;
capacitación y gestión del cambio; operación y soporte durante 36 meses; y cierre.
La descomposición sigue la regla del 100 %: la suma del trabajo de los niveles inferiores
reproduce el trabajo del nivel superior, sin omitir ni agregar alcance (Project Management
Institute [PMI], 2017, p. 161). El segundo nivel son 49 cuentas de control, puntos de gestión
donde se integran el alcance, el cronograma y el esfuerzo para medir el desempeño. El nivel
inferior son 222 paquetes de trabajo, cada uno con un entregable verificable, un criterio de
aceptación y un único responsable (PMI, 2017, pp. 161–162). En la cuenta de las innovaciones,
cada innovación agrupa sus paquetes en un cuarto nivel.
El último nivel de la EDT es el paquete de trabajo, con su entregable, su responsable y
su criterio de aceptación. Fuera de la EDT, cada paquete se descompone en actividades que
cumplen la regla del 8/80, entre 8 y 80 horas hombre de esfuerzo, y la regla del período de
reporte: ninguna actividad dura más de una quincena, el período con que informa el Comité
de Proyecto (PMI, 2017, pp. 183–185). Los paquetes de producto se dividen con una plantilla
por clase; por ejemplo, un módulo de 960 HH se divide en 12 actividades de 80 HH, desde
el análisis de sus requerimientos hasta su entrega en QA. Los 163 paquetes con entregable
se programan con fecha, personas y predecesoras; sus actividades se detallan hasta el H2 y,
después, por planificación gradual antes de cada fase, cuando el equipo conoce el trabajo (PMI,
2017, p. 185). Así el cronograma no fija hoy el día de una actividad que ocurrirá en 2028, y
cada fase se planifica como las iteraciones del proceso RUP del Capítulo 6. El Formulario T-15,
Figura T15.3, muestra los puntos de replanificación (antes del H2, el H4, el H8 y el H9). Los
59 paquetes de esfuerzo continuo, como la cobertura del NOC, las reuniones periódicas o la
mentoría posterior al H12, no se descomponen en actividades distintas: se programan por
quincena u ocurrencia, en relevos de hasta 64 HH cada uno. La lista de actividades y las reglas
de programación están en el Formulario T-15, sección 6.
Los paquetes de la fase de Operación son paquetes de esfuerzo continuo. Cada uno cubre
un servicio durante los 36 meses y se controla con entregables periódicos, como los informes
mensuales de servicio, los informes de pruebas y las actualizaciones anuales, que funcionan
como sus puntos de verificación.
La Tabla 7.1 muestra el tamaño de cada fase y los hitos que produce.
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
7


---

LafroX SpA Introducción al Plan de trabajo
Tabla 7.1 Cuentas de control y paquetes por fase. Fuente: elaboración a partir de LafroX (2026d, T-14) y el
Formulario E-25.
Fase CC PT Etapa Hitos
1 Inicio 9 35 E1 y E2 H1, H8
2 Elaboración 6 18 E1 y E2 H2, H8
3 Construcción 11 79 E1 y E2 H3, H4, H5, H9,
H10
4 Transición 3 10 E1 y E2 H6, H7, H11, H12
5 Adquisiciones y
contrataciones
4 13 E1 y E2 Habilita H3
6 Infraestructura
física y sitios
6 24 E1 Habilita H3 y H6
7 Capacitación y
gestión del cam-
bio
3 13 E1, E2 y Opera-
ción
Condición de H7 y
H12
8 Operación y
soporte (36 meses)
5 26 Operación Hito mensual
9 Cierre 2 4 Meses 21 y 56 Después de H12
Total 49 222
La construcción concentra el 36 % de los paquetes (79 de 222), porque contiene los quince
desarrollos de módulos, las integraciones, la migración, las pruebas de ambas etapas y las
innovaciones. Las fases 5 a 7, que no producen software, suman 50 paquetes (23 %). Ese peso
muestra que, en Puelche, la compra y la instalación del equipamiento de cinco sitios, los
acuerdos con diez transportistas y con el sindicato y la capacitación de una operación que no
puede detenerse son trabajo planificado y controlado, no supuestos.
La Figura 7.1 resume el primer nivel de la EDT: la raíz del proyecto y sus nueve fases.
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
8


---

LafroX SpA Introducción al Plan de trabajo
Plataforma logística de Distribuidora Puelche
1.
Inicio
2.
Elaboración
3.
Construcción
4.
Transición
5.
Adquisiciones
y
contrataciones
6.
Infraestructura
física y sitios
7.
Capacitación
y gestión del
cambio
8.
Operación y
soporte (36
meses)
9.
Cierre
Figura 7.1 Vista del primer nivel de la EDT: raíz del proyecto y sus nueve fases. Fuente: elaboración a partir de
LafroX (2026d, T-14).
Las fases de desarrollo (1 a 4) se recorren una vez por etapa; las fases 5 a 7 las habilitan en
paralelo, y las fases 8 y 9 cubren la operación y el cierre. La figura muestra la estructura, no la
secuencia temporal: el número de una fase no indica cuándo ocurre; sus fechas están en la
carta Gantt de la sección 7.3.2.
7.1.2 Estructura general
Las láminas siguientes desglosan las cuentas de control y los paquetes por fase. Cada
imagen se presenta inmediatamente después de su descripción. La fase 3 se divide en cinco
láminas para facilitar la lectura: las dos primeras separan la base técnica de los módulos de
la Etapa 1; las tres restantes muestran las cuentas 3.5 a 3.11, con una lámina adicional para
ampliar los paquetes de innovación de la cuenta 3.10.
7.1.2.1 Fase 1. Inicio
La fase de Inicio define el proyecto, fija su alcance y planificación y establece cómo se
gobierna y controla. Sus cuentas 1.1 a 1.5 abarcan el acta, la línea base, la planificación, los
interesados y la calidad.
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
9


---

LafroX SpA Introducción al Plan de trabajo
1. Inicio
1.1 Definición inicial del
proyecto
1.1.1 Acta de
constitución del
proyecto, firmada con
la Contraparte Técnica
1.1.2 Documento de
validación con el
CLIENTE de los
problemas y metas del
proyecto
1.1.3 Acta de
confirmación con el
CLIENTE de la fecha
de inicio, la evidencia
para el proveedor de
lácteos, las ventanas
de paso a producción
y el acuse tributario
1.2 Alcance del proyecto
1.2.1 Documento de
especificación de
requerimientos y línea
base de alcance de la
Etapa 1 (H1)
1.2.2 Documento de
reglas de ruteo
capturadas al
planificador de rutas
1.2.3 Documento de
especificación de las
interfaces sin
documentación del
ERP, del WMS de 2013
y de la telemetría del
tercero
1.2.4 Matriz de
trazabilidad:
requerimiento,
módulo, paquete y
prueba (H1)
1.2.5 Documento de
línea base de alcance
de la Etapa 2: canal
moderno y costo de
servir (H8)
1.3 Planificación del
proyecto
1.3.1 Plan para la
dirección del proyecto,
con el calendario de
congelamientos de
septiembre, diciembre
y el cierre mensual
1.3.2 EDT y diccionario
de la EDT (línea base
del alcance)
1.3.3 Carta Gantt de 56
meses con los hitos
H1 a H12 y la ruta
crítica
1.3.4 Documento de
nivelación de recursos
y frentes del
solapamiento de los
meses 13 a 15 y 19 a
20
1.3.5 Minuta reunión
semanal
1.4 Gestión de interesados
y comunicaciones
1.4.1 Registro de
interesados con su
influencia, interés y
estrategia
1.4.2 Plan de
comunicaciones con
calendario y canales
por grupo de interés
1.4.3 Registro de
solicitudes de cambio
con análisis de
impacto
1.5 Gestión de calidad
1.5.1 Plan de calidad y
plan de pruebas
1.5.2 Puertas de
calidad automáticas en
la cadena de
integración (cobertura
mínima del 80 %)
Figura 7.2 Fase 1 — Inicio, primera parte: cuentas 1.1 a 1.5. Fuente: elaboración a partir de LafroX (2026d, T-14).
La segunda lámina completa Inicio con gestión de riesgos, reversibilidad, gobierno, control
y cumplimiento normativo. Incluye los paquetes 1.2.2 y 1.2.3, que capturan las reglas de ruteo
cuya fuente experta se jubila y las interfaces del sistema de gestión que el CLIENTE reconoce no
tener documentadas; también incluye los comités del artículo 71 de las Bases Administrativas
(p. 37), el informe de valor ganado y el tablero (RT-19.06 a RT-19.09).
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
10


---

LafroX SpA Introducción al Plan de trabajo
1. Inicio
1.6 Gestión de riesgos
1.6.1 Plan de riesgos y
registro inicial de
riesgos según ISO
31000
1.6.2 Registro de
riesgos revisado en
cada Comité de
Proyecto
1.7 Plan de Reversibilidad
1.7.1 Plan de
Reversibilidad inicial
(primeros 90 días)
1.7.2 Actualizaciones
anuales del Plan de
Reversibilidad durante
la implementación
1.8 Gobierno y control del
proyecto
1.8.1 Oficina de gestión del
proyecto con metodología
basada en el PMBOK
1.8.2 Actas del Comité
Ejecutivo mensual, con la
aprobación de los cambios
de alcance
1.8.3 Actas del Comité de
Proyecto quincenal
1.8.4 Actas del Comité de
Arquitectura mensual
1.8.5 Actas del Comité de
Operación mensual, desde
el mes 13
1.8.6 Informe mensual de
avance con valor ganado
1.8.7 Tablero de estado del
proyecto disponible para el
CLIENTE
1.8.8 Espacio colaborativo
con la documentación, los
entregables, las actas, los
riesgos y los cambios
1.9 Cumplimiento
normativo y contractual
1.9.1 Matriz de cumplimiento
normativo por obligación
legal, con su control y su
evidencia
1.9.2 Acuerdo de
tratamiento de datos
personales con el CLIENTE
1.9.3 Registro de
actividades de tratamiento y
evaluación de impacto en
protección de datos
1.9.4 Certificación ISO/IEC
27001 vigente y entrega
anual de los informes de
certificación
1.9.5 Garantía de fiel
cumplimiento, seguros y
certificados laborales
vigentes durante el contrato
Figura 7.3 Fase 1 — Inicio, segunda parte: cuentas 1.6 a 1.9, desde riesgos hasta cumplimiento contractual.
Estas cuentas completan Inicio: identifican los riesgos y la reversibilidad, establecen el
gobierno y control del proyecto y cierran con el cumplimiento normativo y contractual.
7.1.2.2 Fase 2. Elaboración
Elaboración diseña la solución antes de programar: arquitectura lógica y física, datos
trazables por lote, seguridad, sala técnica de Talca, continuidad y experiencia de usuario. La
aprobación de arquitectura, seguridad y modelo de datos corresponde al H2 del mes 4. La
primera lámina muestra las cuentas 2.1 a 2.3.
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
11


---

LafroX SpA Introducción al Plan de trabajo
2. Elaboración
2.1 Arquitectura de la
solución
2.1.1 Documento de
arquitectura lógica:
capas, módulos M1 a
M12 e interfaces
2.1.2 Documento de
arquitectura física
híbrida: nube, centros
de distribución y
plataformas de cross-
docking
2.1.3 Modelo de datos
y diccionario de datos,
con la trazabilidad por
lote
2.1.4 Documento de
diseño detallado de
M11 y del intercambio
con las cadenas
2.2 Diseño de la seguridad
2.2.1 Plan de
seguridad de la
información
2.2.2 Modelado de
amenazas por
componente y por
integración externa,
actualizado ante cada
cambio
2.2.3 Plan de respuesta
a incidentes de
seguridad, con aviso al
CLIENTE en dos horas
2.2.4 Matriz de
clasificación de la
información y matriz
de controles
2.3 Diseño de la sala
técnica y de los racks
2.3.1 Plano de la sala
técnica de Talca, con
su cálculo eléctrico y
térmico
2.3.2 Plano de
distribución de los
racks R01 de
servidores y R02 de
comunicaciones
2.3.3 Plano de los
gabinetes de borde de
Concepción y de las
plataformas de cross-
docking
Figura 7.4 Fase 2 — Elaboración, primera parte: arquitectura, seguridad y sala técnica, cuentas 2.1 a 2.3.
La continuación cubre la validación de diseños, continuidad del negocio y experiencia
de usuario (cuentas 2.4 a 2.6), incluidos los procedimientos manuales y la recuperación ante
desastres.
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
12


---

LafroX SpA Introducción al Plan de trabajo
2. Elaboración
2.4 Validación de diseños
2.4.1 Acta de
aprobación de la
arquitectura, el plan de
seguridad y el modelo
de datos (H2)
2.4.2 Acta de
aprobación del diseño
detallado de la Etapa 2
(H8)
2.5 Continuidad del
negocio
2.5.1 Plan de
continuidad del
negocio según ISO
22301, con análisis de
impacto y
procedimientos
manuales
2.5.2 Plan de
continuidad TIC según
ISO/IEC 27031 y plan
de recuperación ante
desastres
2.6 Experiencia de usuario
2.6.1 Investigación con
preparadores,
preventistas,
conductores y
almaceneros
2.6.2 Prototipos y
pruebas de usabilidad
con participantes del
CLIENTE
2.6.3 Indicadores de
usabilidad
comprometidos por
transacción crítica
Figura 7.5 Fase 2 — Elaboración, segunda parte: validación, continuidad y experiencia de usuario, cuentas 2.4 a
2.6.
Con estas cuentas, los diseños quedan sometidos a validación y se completan los planes de
continuidad y experiencia de usuario que orientan la fase de Construcción.
7.1.2.3 Fase 3. Construcción
Construcción produce los ambientes y servicios de nube, la base compartida, los módulos de
ambas etapas, las integraciones, la migración, las pruebas, las innovaciones y la documentación.
La primera lámina reúne los ambientes de desarrollo, los servicios de nube y la base compartida
(cuentas 3.1 a 3.3).
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
13


---

LafroX SpA Introducción al Plan de trabajo
3. Construcción
3.1 Ambientes y cadena de
desarrollo
3.1.1 Ambientes de
Desarrollo y QA en la
nube (H3)
3.1.2 Ambientes de
Preproducción y
Producción en la nube
(H3)
3.1.3 Ambiente de
recuperación ante
desastres en la región
secundaria (H3)
3.1.4 Cadena de
integración y entrega
continua, e
infraestructura como
código
3.1.5 Observabilidad
de los doce módulos y
de los sitios, con
tableros para el
CLIENTE (H3)
3.2 Servicios de nube de
la plataforma
3.2.1 Servicio de nube
para la aplicación y los
portales
3.2.2 Servicio de nube
de base de datos,
caché y mensajería
3.2.3 Servicio de nube
de ingesta de IoT,
telemetría cruda y
plataforma analítica
3.2.4 Servicio de nube
de respaldo inmutable
y réplica entre
regiones
3.2.5 Servicio de nube
de seguridad y
gobierno, y detección
en endpoints
3.2.6 Servicio de
gestión de
dispositivos móviles
3.3 Base compartida
3.3.1 Identidad y control de
acceso, incluidos los
conductores externos que
rotan sin aviso
3.3.2 Integración con el
ERP como único emisor de
la guía de despacho (INT-
06 e INT-07)
3.3.3 Convivencia con el
WMS de 2013 durante el
reemplazo
3.3.4 Integración con la
telemetría de los 42
camiones propios (INT-15)
3.3.5 Registro auditable de
stock, lotes y cobros
3.3.6 Operación sin
conexión: 14 horas en
terreno y 24 horas en el CD
Figura 7.6 Fase 3 — Construcción, primera parte: ambientes, servicios de nube y base compartida, cuentas 3.1 a
3.3.
La segunda lámina desglosa los módulos de la Etapa 1 (cuenta 3.4), con los componentes
de recepción, inventario, preparación de pedidos, cadena de frío, aplicaciones y operación de
tiendas.
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
14


---

LafroX SpA Introducción al Plan de trabajo
3. Construcción
3.4 Módulos de la Etapa 1
3.4.1 Recepción de mercadería con captura de lote y vencimiento (M1 Recepción)
3.4.2 Inventario por ubicación y lote, con FEFO y conteo cíclico (M2 Inventario)
3.4.3 Preparación de pedidos en el turno de noche y en la cámara de congelado (M5
Preparación)
3.4.4 Cadena de frío, retención de lotes y retiro sanitario (M9 Calidad y trazabilidad)
3.4.5 Ingesta de temperatura y posición de la flota (M12 Telemetría)
3.4.6 Aplicación móvil de preventa sin conexión, con stock y crédito (M3 Preventa)
3.4.7 Planificación de rutas corregible por el planificador (M4 Rutas)
3.4.8 Aplicación móvil de reparto con prueba de entrega digital (M6 Reparto)
3.4.9 Devoluciones en terreno y control de envases (M8 Devoluciones y envases)
3.4.10 Cobro en ruta, rendición y conciliación (M7 Cobranza y rendición)
3.4.11 Indicadores operacionales y OTIF diario (M10 Analítica)
Figura 7.7 Fase 3 — Construcción, segunda parte: módulos de la Etapa 1, cuenta 3.4.
La tercera lámina presenta los módulos de la Etapa 2, las integraciones externas, la mi-
gración y las pruebas de la Etapa 1 (cuentas 3.5 a 3.8). La integración con el ERP conserva su
función de emisor único de la guía de despacho.
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
15


---

LafroX SpA Introducción al Plan de trabajo
3. Construcción
3.5 Módulos de la Etapa 2
3.5.1 Pedido
electrónico y aviso de
despacho para las
cadenas (M11 Canal
moderno)
3.5.2 Portal web de
clientes: cuenta, saldo,
entregas y
documentos
3.5.3 Portal web de
transportistas: rutas
asignadas del día
siguiente
3.5.4 Costo de servir
por cliente y por
entrega (M10 Analítica)
3.6 Integraciones externas
3.6.1 Intercambio de
lote y trazabilidad con
los proveedores
3.6.2 Integración con la
pasarela de pago para
el cobro con tarjeta
(INT-09)
3.6.3 Integración con el
servicio de mapas y
geocodificación (INT-
10)
3.6.4 Integración con el
servicio de avisos al
cliente (INT-11)
3.6.5 Intercambio
electrónico con la
principal cadena, con
sus pruebas
aprobadas (INT-08)
3.6.6 Incorporación de
las demás cadenas al
intercambio
electrónico (INT-08)
3.7 Migración de datos
3.7.1 Informe de
perfilamiento y datos
saneados
3.7.2 Datos maestros
cargados: 8.400 SKU,
clientes e
instalaciones
3.7.3 Saldos migrados
desde el WMS de Talca
3.7.4 Saldos cargados
en Concepción desde
el conteo físico
3.7.5 Acta de
conciliación y corte
fuera de las ventanas
de congelamiento
3.8 Pruebas de la Etapa 1
3.8.1 Pruebas de integración, regresión
e idempotencia en QA (H4)
3.8.2 Pruebas de aceptación y de
accesibilidad con preventistas,
conductores y bodega
3.8.3 Pruebas del perfil operacional: sin
señal, sin enlace y a −22 °C con
guantes
3.8.4 Pruebas de carga con el peak de
septiembre y de resiliencia
3.8.5 Prueba de recuperación ante
desastres con conmutación real
3.8.6 Prueba de seguridad ofensiva de
la Etapa 1, por un tercero independiente
3.8.7 Acta de certificación de la Etapa 1
(H5)
3.8.8 Demostración en Preproducción
del despliegue sin interrupción de la
Etapa 1
Figura 7.8 Fase 3 — Construcción, tercera parte: módulos de la Etapa 2, integraciones, migración y pruebas de la
Etapa 1, cuentas 3.5 a 3.8.
La cuarta lámina reúne las pruebas de la Etapa 2, las innovaciones y la documentación
técnica (cuentas 3.9 a 3.11).
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
16


---

LafroX SpA Introducción al Plan de trabajo
3. Construcción
3.9 Pruebas de la Etapa 2
3.9.1 Pruebas de integración y regresión
sin afectar la Etapa 1 en producción (H9)
3.9.2 Pruebas de aceptación y de
accesibilidad con cadenas,
transportistas, Comercial y Finanzas
3.9.3 Pruebas de carga con ambas etapas
activas y de resiliencia
3.9.4 Prueba de recuperación ante
desastres con ambas etapas
3.9.5 Prueba de seguridad ofensiva de la
Etapa 2, por un tercero independiente
3.9.6 Acta de certificación de la Etapa 2 y
cierre del desarrollo (H10)
3.9.7 Demostración en Preproducción del
despliegue sin interrupción de la Etapa 2
3.10 Innovaciones
3.10.1 Innovación 1:
seguimiento de
vencimiento
posentrega en el local
3.10.2 Innovación 2:
reproducción de
incidentes de terreno
3.10.3 Innovación 3:
vida útil remanente por
historia térmica del lote
3.10.4 Innovación 5:
hoja de negocio del
almacenero
3.11 Documentación técnica
3.11.1 Documentación técnica, funcional,
de arquitectura, de operación y de
seguridad
3.11.2 Base de conocimiento de
incidentes y decisiones de diseño
3.11.3 Estándares de codificación y
documentación de interfaces en OpenAPI
y AsyncAPI
3.11.4 Inventario de componentes
(SBOM) con sus licencias de código
abierto
3.11.5 Depósito del código fuente en el
repositorio del CLIENTE en cada
liberación
Figura 7.9 Fase 3 — Construcción, cuarta parte: pruebas de la Etapa 2, innovaciones y documentación técnica,
cuentas 3.9 a 3.11.
La quinta lámina amplía la cuenta 3.10 para que se lean sus paquetes de innovación: segui-
miento de vencimientos, reproducción de incidentes, vida útil remanente y hoja de negocio
del almacenero.
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
17


---

LafroX SpA Introducción al Plan de trabajo
3. Construcción
3.10 Innovaciones
3.10.1 Innovación 1:
seguimiento de
vencimiento posentrega
en el local
3.10.1.1 Documento de
catálogo de acciones y
protocolo del piloto
(INN-01.P1)
3.10.1.2 Estimador de
saldo y ritmo de
reposición (INN-01.P2)
3.10.1.3 Función de
lista sin conexión en la
aplicación de preventa
(INN-01.P3)
3.10.1.4 Informe del
piloto en marcha
blanca y habilitación
(INN-01.P4)
3.10.2 Innovación 2:
reproducción de
incidentes de terreno
3.10.2.1 Informe de
medición inicial y
contrato de evidencia
(INN-02.P1)
3.10.2.2 Circuito
mínimo de
reproducción en la
preventa (INN-02.P2)
3.10.2.3 Captura de
evidencia en las
aplicaciones de
preventa, preparación y
reparto (INN-02.P3)
3.10.2.4 Informe de
validación comparada
durante la
implementación (INN-
02.P4, primera parte)
3.10.3 Innovación 3: vida
útil remanente por historia
térmica del lote
3.10.3.1 Documento de
familias priorizadas y
parámetros aprobados
(INN-03.P1)
3.10.3.2 Asociación
lote–sensor en el borde
y en el camión (INN-
03.P2)
3.10.3.3 Vista en M9 y
orden de salida
sugerido (INN-03.P3)
3.10.3.4 Informe de
validación en marcha
blanca con Calidad
(INN-03.P4)
3.10.4 Innovación 5: hoja
de negocio del
almacenero
3.10.4.1 Prototipo e
informe de la prueba de
comprensión (INN-
05.P1)
3.10.4.2 Evaluación de
privacidad y diseño de
la impresión en cabina
(INN-05.P2)
3.10.4.3 Cálculo y
bloques 1 a 3 de la hoja
de negocio (INN-05.P3)
3.10.4.4 Hoja
certificada, en marcha
blanca y en producción
(INN-05.P4, primera
parte)
Figura 7.10 Fase 3 — Construcción, quinta parte: detalle de los paquetes de las innovaciones agrupadas en la
cuenta 3.10.
El detalle identifica los paquetes de INN-01, INN-02, INN-03 e INN-05 dentro de 3.10. INN-04
conserva su tratamiento distinto: su fórmula contractual se acuerda en la cuenta 5.4, como
muestra la fase de Adquisiciones y contrataciones.
7.1.2.4 Fase 4. Transición
Transición convierte la solución probada en el registro oficial. Su plan contempla las olas y
la reversión; luego coordina las marchas blancas, la estabilización y las actas de aceptación de
ambas etapas (H7 y H12).
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
18


---

LafroX SpA Introducción al Plan de trabajo
4. Transición
4.1 Plan de implantación
4.1.1 Plan de olas de la
Etapa 1 por sitio y
zona: Talca,
Concepción y
plataformas de cross-
docking
4.1.2 Procedimiento de
reversión de la Etapa 1
antes de las 05:30, con
hoja de picking y guía
en papel
4.1.3 Plan de
implantación y
reversión de la Etapa 2
fuera de la ventana de
05:30 a 07:00
4.2 Marcha blanca y
producción de la Etapa 1
4.2.1 Marcha blanca de
la Etapa 1 con
conciliación diaria (H6)
4.2.2 Estabilización de
la Etapa 1 en el turno
de noche y
acompañamiento en
ruta
4.2.3 Acta de paso a
producción y cierre de
la Etapa 1 (H7)
4.3 Marcha blanca y
producción de la Etapa 2
4.3.1 Marcha blanca de
la Etapa 2 en
convivencia con la
Etapa 1 y fuente única
de datos (H11)
4.3.2 Estabilización de
la Etapa 2 con
Comercial, Finanzas,
cadenas y
transportistas
4.3.3 Acta de paso a
producción y
aceptación final de la
implementación (H12)
4.3.4 Garantía de
correcto
funcionamiento
constituida, condición
de la aceptación final
(H12)
Figura 7.11 Fase 4 — Transición: plan de implantación y marchas blancas de las etapas 1 y 2, cuentas 4.1 a 4.3.
La cuenta 4.1 prepara las olas y la reversión; las cuentas 4.2 y 4.3 separan la marcha blanca
y producción de cada etapa, asociadas a los hitos H7 y H12.
7.1.2.5 Fase 5. Adquisiciones y contrataciones
Esta fase distingue el equipamiento de terreno, que el CLIENTE compra según la espe-
cificación de LafroX, de la infraestructura de la sala técnica, los racks, los servidores y los
gabinetes de borde, que LafroX especifica, compra y provee. LafroX incorpora el costo de esta
infraestructura en su Oferta Económica; el CLIENTE no la adquiere mediante una compra
separada. LafroX también contrata nube, enlaces y licencias. La fase formaliza, además, los
acuerdos con transportistas y sindicato y la fórmula contractual de la innovación 4.
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
19


---

LafroX SpA Introducción al Plan de trabajo
5. Adquisiciones y contrataciones
5.1 Hardware e
infraestructura
5.1.1 Especificación de
compra del
equipamiento de
terreno para el
CLIENTE
5.1.2 Especificación de
compra de la sala
técnica, los racks y los
gabinetes de borde
para el CLIENTE
5.1.3 Actas de
recepción técnica de
los equipos
comprados por el
CLIENTE
5.2 Servicios de nube y
licencias
5.2.1 Contrato de los
servicios de AWS
5.2.2 Suscripción del
servicio de gestión de
dispositivos y de
detección en
endpoints
5.2.3 Licencias de
software de terceros
constituidas a nombre
del CLIENTE
5.3 Enlaces de
comunicaciones
5.3.1 Contrato de fibra
óptica de los CD de
Talca y Concepción
5.3.2 Contrato de
planes LTE con dos
proveedores
5.3.3 Contrato de
Starlink para las tres
plataformas de cross-
docking
5.4 Acuerdos con terceros
5.4.1 Acuerdos
operacionales
firmados con los diez
transportistas
5.4.2 Acta de acuerdo
con el sindicato sobre
terminales, GPS y
cámaras
5.4.3 Fórmula
aprobada del tramo
variable: reglas de
atribución, canasta e
índices (INN-04.P1)
5.4.4 Contrato de
custodia de fuentes
con un tercero
independiente
Figura 7.12 Fase 5 — Adquisiciones y contrataciones: hardware, servicios, enlaces y acuerdos con terceros,
cuentas 5.1 a 5.4.
La cuenta 5.1 reúne las adquisiciones de hardware, manteniendo la distinción anterior:
el CLIENTE compra el equipamiento de terreno y LafroX compra y provee la infraestructura
de sala, incluida en su Oferta Económica. Las cuentas 5.2 a 5.4 organizan nube y licencias,
enlaces y acuerdos con terceros.
7.1.2.6 Fase 6. Infraestructura física y sitios
La fase instala la sala técnica de Talca, con energía, climatización y extinción; el cableado,
los racks y gabinetes de borde; y la infraestructura de los sitios. La primera lámina cubre la
sala, el cableado y el montaje de racks (cuentas 6.1 a 6.3).
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
20


---

LafroX SpA Introducción al Plan de trabajo
6. Infraestructura física y sitios
6.1 Adecuación de la sala
técnica de Talca
6.1.1 Obra civil y piso
técnico de la sala
6.1.2 Hardware de
energía instalado: UPS
modular N+1,
generador con 24
horas de autonomía,
transferencia
automática y PDU A/B
6.1.3 Hardware de
climatización de
precisión N+1
instalado
6.1.4 Hardware de
detección temprana de
incendio y extinción
por agente limpio
instalado
6.1.5 Acta de
recepción técnica de la
sala
6.2 Cableado estructurado
6.2.1 Cableado de
cobre Cat6A y fibra
OM4 tendido, con dos
ductos de ingreso
independientes
6.2.2 Certificación de
enlaces, etiquetado y
planos as-built
6.2.3 Gabinetes de
piso y switches de
acceso instalados en
las bodegas de Talca y
Concepción
6.3 Montaje de racks y
gabinetes
6.3.1 Rack R01 de
servidores montado:
clúster de tres nodos,
respaldo local y
consola KVM
6.3.2 Rack R02 de
comunicaciones
montado: firewalls,
switches de núcleo y
de gestión, y
distribución de fibra
6.3.3 Gabinete de
borde de Concepción
montado: servidor,
firewalls, switches,
UPS, climatización y
monitoreo
6.3.4 Gabinetes de
borde montados en
Curicó, Chillán y Los
Ángeles
Figura 7.13 Fase 6 — Infraestructura física y sitios, primera parte: sala técnica, cableado y racks, cuentas 6.1 a 6.3.
La segunda lámina incluye seguridad física, equipamiento de campo y configuración de la
infraestructura distribuida en los sitios (cuentas 6.4 a 6.6), incluidos los termógrafos de los
camiones con frío y la prueba de autonomía de 24 horas.
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
21


---

LafroX SpA Introducción al Plan de trabajo
6. Infraestructura física y sitios
6.4 Sistemas de seguridad
física
6.4.1 Hardware de
control de acceso
biométrico y esclusa
instalado
6.4.2 Hardware de
videovigilancia
instalado
6.4.3 Recinto de
custodia de respaldos
habilitado
6.5 Equipamiento de
campo
6.5.1 Terminales de
preventa, reparto y
bodega configurados y
enrolados
6.5.2 Terminales de
pago configurados,
uno por camión
6.5.3 Sensores de
cámara y gateways IoT
instalados en Talca y
Concepción
6.5.4 Termógrafos
instalados en los 28
camiones con frío
(propios y de
transportistas)
6.5.5 Impresoras de
cabina instaladas
6.5.6 Impresoras de
andén y balanzas de
recepción instaladas
6.6 Configuración de la
infraestructura de los
sitios
6.6.1 Software de base
instalado en los sitios:
virtualización,
contenedores,
PostgreSQL, RabbitMQ
y Keycloak
6.6.2 Enlaces de fibra,
LTE y Starlink
habilitados, con
conmutación al
respaldo
6.6.3 Borde de los CD
en servicio, con la
prueba de autonomía
de 24 horas aprobada
Figura 7.14 Fase 6 — Infraestructura física y sitios, segunda parte: seguridad física, equipamiento de campo y
configuración, cuentas 6.4 a 6.6.
Con seguridad física, equipamiento de campo y configuración de los sitios, estas cuentas
completan la infraestructura distribuida que habilita la operación en terreno.
7.1.2.7 Fase 7. Capacitación y gestión del cambio
La fase atiende la rotación del 38 % en preparación con capacitación continua del turno
de noche; acompaña individualmente al personal con veinte o treinta años en la compañía;
incorpora a los conductores externos en el andén; y transfiere conocimiento al equipo de TI
del CLIENTE. La certificación de usuarios (cuenta 7.3) es una de las condiciones de cierre de
cada marcha blanca.
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
22


---

LafroX SpA Introducción al Plan de trabajo
7. Capacitación y gestión del cambio
7.1 Capacitación por roles
7.1.1 Plan de capacitación
por perfil: usuarios finales,
avanzados, administradores,
equipo técnico y soporte
7.1.2 Programa de
capacitación continua del
turno de noche por la
rotación del 38 %
7.1.3 Procedimiento de
incorporación de los
conductores de los
transportistas en el andén
7.1.4 Traspaso al equipo de
TI de cuatro personas del
CLIENTE
7.1.5 Materiales de
capacitación: manuales por
perfil, guías rápidas,
preguntas frecuentes y
videos tutoriales
7.1.6 Plataforma de
autoformación en línea con
registro de avance
7.2 Gestión del cambio
7.2.1 Acompañamiento del
personal con 20 o 30 años en
la compañía
7.2.2 Gestión del cambio con
las cadenas y los
transportistas
7.2.3 Diagnóstico del impacto
organizacional por área y
perfil, con agentes de cambio
7.2.4 Procedimientos
operativos afectados,
rediseñados y documentados
7.2.5 Medición de la adopción
y plan de acción correctiva
7.3 Evaluaciones y
certificaciones
7.3.1 Certificación de
preventistas, conductores y
preparadores (Etapa 1)
7.3.2 Certificación de
Comercial y Finanzas en
costo de servir (Etapa 2)
Figura 7.15 Fase 7 — Capacitación y gestión del cambio: capacitación por roles, acompañamiento y
certificaciones, cuentas 7.1 a 7.3.
La lámina muestra que la adopción combina formación por perfil, acompañamiento del
personal y certificaciones antes de los cierres de marcha blanca.
7.1.2.8 Fase 8. Operación y soporte
La fase presta servicios durante los meses 21 a 56: centro de operaciones, gestión de
incidentes, continuidad, mantenimiento, innovaciones, informes y transferencia al equipo
del CLIENTE. La primera lámina presenta las cuentas 8.1 y 8.2, que reúnen los servicios de
operación y el mantenimiento de la solución.
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
23


---

LafroX SpA Introducción al Plan de trabajo
8. Operación y soporte (36 meses)
8.1 Servicios de operación
8.1.1 Servicio de centro de operaciones 24×7
y mesa de servicio durante los 36 meses de
operación (04:00 a 22:00; 24×7 en
septiembre y diciembre)
8.1.2 Servicio de gestión de incidentes,
problemas y niveles de servicio del Art. 78°
durante los 36 meses de operación
8.1.3 Servicio de continuidad y pruebas
semestrales de recuperación ante desastres
durante los 36 meses de operación
8.1.4 Actualizaciones anuales del Plan de
Reversibilidad durante los 36 meses de
operación
8.1.5 Servicio de centro de operaciones de
seguridad 24×7 con SIEM durante los 36
meses de operación
8.1.6 Pruebas mensuales de restauración de
respaldos durante los 36 meses de
operación
8.2 Mantenimiento
8.2.1 Mantenimiento correctivo y evolutivo
del software durante los 36 meses de
operación, con bolsa anual de horas y fuera
de las ventanas de congelamiento
8.2.2 Mantenimiento de ciberseguridad
durante los 36 meses de operación:
vulnerabilidades, intrusión anual e inyección
de fallas
8.2.3 Mantenimiento del hardware durante
los 36 meses de operación: sala técnica,
racks, gabinetes de borde y equipamiento de
terreno
8.2.4 Registro y reducción de la deuda
técnica durante los 36 meses de operación
8.2.5 Actualizaciones anuales de los
componentes de base durante los 36 meses
de operación
8.2.6 Revisiones semestrales de las
instalaciones eléctricas de la sala durante
los 36 meses de operación
8.2.7 Ciclo de vida del equipamiento durante
los 36 meses de operación: reposición y
disposición final
Figura 7.16 Fase 8 — Operación y soporte, primera parte: servicios de operación y mantenimiento, cuentas 8.1 y
8.2.
La primera parte concentra la continuidad del servicio y el mantenimiento del software,
la infraestructura y la ciberseguridad. Sus paquetes conservan las frecuencias, horarios y
ventanas que condicionan la operación durante los 36 meses.
La segunda lámina completa la fase con las cuentas 8.3 a 8.5: innovaciones en operación,
informes y obligaciones periódicas, y capacitación y transferencia. También distingue los
períodos particulares de las innovaciones y la mentoría al equipo del CLIENTE.
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
24


---

LafroX SpA Introducción al Plan de trabajo
8. Operación y soporte (36 meses)
8.3 Innovaciones en operación
8.3.1 Innovación 2:
mantenimiento de escenarios
de regresión (INN-02.P4,
segunda parte)
8.3.2 Innovación 3: revisión
semestral de parámetros
durante los 36 meses de
operación (INN-03.P5)
8.3.3 Innovación 4: línea base
y liquidaciones en sombra
(INN-04.P2)
8.3.4 Innovación 4:
liquidación mensual del
tramo variable, meses 24 a 56
(INN-04.P3)
8.3.5 Innovación 5:
despliegue gradual por rutas
(INN-05.P4, segunda parte)
8.3.6 Innovación 5: bloque 4
condicionado (INN-05.P5)
8.4 Informes y obligaciones
periódicas
8.4.1 Gestión de la capacidad
con proyección trimestral
durante los 36 meses de
operación
8.4.2 Informes mensuales de
consumo de nube (FinOps)
durante los 36 meses de
operación
8.4.3 Estimaciones anuales
de la huella de carbono de la
operación
8.4.4 Actualizaciones
semestrales del depósito de
custodia de fuentes durante
los 36 meses de operación
8.5 Capacitación y transferencia
en operación
8.5.1 Dos jornadas anuales de
actualización y capacitación
del personal nuevo durante
los 36 meses de operación
8.5.2 Mentoría al equipo
técnico del CLIENTE durante
los seis meses posteriores al
mes 21
8.5.3 Mantenimiento de la
base de conocimiento
durante los 36 meses de
operación, con métricas de
uso
Figura 7.17 Fase 8 — Operación y soporte, segunda parte: innovaciones, obligaciones periódicas, capacitación y
transferencia, cuentas 8.3 a 8.5.
Estas cuentas completan la operación con la continuidad de las innovaciones, los informes
recurrentes y la transferencia de conocimiento. La mentoría al equipo técnico del CLIENTE
se extiende durante los seis meses posteriores al mes 21, mientras que el tramo variable de
INN-04 se liquida entre los meses 24 y 56.
7.1.2.9 Fase 9. Cierre
Cierre comprende dos momentos: completar la implementación en el mes 21, con entrega
de código, infraestructura como código y lecciones aprendidas; y ejecutar la salida al término
del contrato, con el Plan de Reversibilidad y el tratamiento final de los datos.
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
25


---

LafroX SpA Introducción al Plan de trabajo
9. Cierre
9.1 Cierre de la
implementación
9.1.1 Entrega del
código fuente, la
infraestructura como
código y los
procedimientos de
despliegue
9.1.2 Informe de
lecciones aprendidas y
archivo de la
implementación
9.2 Salida al término del
contrato
9.2.1 Ejecución del
Plan de Reversibilidad
y acompañamiento de
90 días
9.2.2 Certificado de
devolución o
eliminación de datos
personales
Figura 7.18 Fase 9 — Cierre: cierre de implementación y salida al término del contrato, cuentas 9.1 y 9.2.
La EDT distingue así el cierre de implementación del mes 21 de la salida al término del
contrato, que incluye la ejecución del Plan de Reversibilidad y el tratamiento final de los datos.
7.1.3 Cobertura del alcance
Las Aclaraciones de la licitación exigen que la EDT contenga explícitamente las innovacio-
nes y las actividades de seguridad, calidad, migración e implantación (sección 11, Capítulo 7),
y el Caso logística exige que contenga la arquitectura (capítulo 19). La Tabla 7.2 comprueba
que cada uno de esos componentes tiene paquetes propios.
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
26


---

LafroX SpA Introducción al Plan de trabajo
Tabla 7.2 Cobertura del alcance en la EDT. Fuente: elaboración a partir de LafroX (2026d, T-14); LafroX (2026m,
SD4); y Distribuidora Puelche S.A. (2026d, Aclaraciones).
Componente Elementos PT Cuentas de control Exigencia
Módulos M1–M12 y los por-
tales de clientes
y de transportis-
tas; el portal de
proveedores se
construye con
M11 Canal mo-
derno (3.5.1)
15 3.4, 3.5 Caso logística, cap.
19
Interfaces INT-01 a INT-15 21 3.1, 3.3, 3.4, 3.6,
6.3, 6.5
Caso logística, cap.
19
Innovaciones INN-01 a INN-05 23 3.10, 5.4, 8.3 Aclaraciones; BA,
Art. 29°
Seguridad Diseño, construc-
ción, pruebas y
operación
17 1.9, 2.2, 3.2, 3.3,
3.8, 3.9, 3.11, 6.4,
8.1, 8.2
Aclaraciones
Calidad Planes, puertas,
pruebas y deuda
técnica
19 1.5, 3.8, 3.9, 3.11,
8.2
Aclaraciones
Migración Perfilamiento,
carga, ensayos y
conciliación
6 3.3, 3.7 Aclaraciones; BTT,
numeral 20.1
Implantación Olas, marchas
blancas, capacita-
ción y cambio
23 4.1 a 4.3, 7.1 a 7.3 Aclaraciones; RT-
20.01 a 20.08
La tabla muestra que ninguna exigencia descansa en un paquete genérico. La seguridad,
por ejemplo, aparece en las cinco fases donde ocurre: el diseño de la Elaboración, la identidad
y las pruebas de seguridad ofensiva de la Construcción, la seguridad física de la sala y el centro
de operaciones de seguridad durante la Operación. Las pruebas de seguridad ofensiva 3.8.6
y 3.9.5 se cuentan en la fila de seguridad y en la de calidad, porque son a la vez control de
seguridad y prueba de certificación. Las pruebas de la Etapa 2 repiten las de la Etapa 1 con una
exigencia adicional: demostrar que la Etapa 1 en producción no se degrada.
La Figura 7.19 ubica esos paquetes por fase y muestra en qué parte de la EDT y, por lo tanto,
del cronograma quedan las actividades de cada categoría.
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
27


---

LafroX
SpA
Introducción
al
Plan
de
trabajo
Fase de la EDT
Innovaciones
23 PaqueteTrabajo
Seguridad
17 PaqueteTrabajo
Calidad
19 PaqueteTrabajo
Migración
6 PaqueteTrabajo
Implantación
23 PaqueteTrabajo
1 Inicio —
1.9.2, 1.9.3,
1.9.4
1.5.1, 1.5.2 — —
2 Elaboración — 2.2.1–2.2.4 — — —
3 Construcción
3.10.1 INN-01
3.10.2 INN-02
3.10.3 INN-03
3.10.4 INN-05
3.2.5, 3.3.1
3.8.6, 3.9.5
3.11.4
3.8.1–3.8.8
3.9.1–3.9.7
3.11.3
3.3.3
3.7.1–3.7.5
—
4 Transición — — — —
4.1.1–4.1.3
4.2.1–4.2.3
4.3.1–4.3.4
5 Adquisiciones 5.4.3 INN-04 — — — —
6 Infraestructura — 6.4.1–6.4.3 — — —
7 Capacitación — — — —
7.1.1–7.1.6
7.2.1–7.2.5
7.3.1, 7.3.2
8 Operación
8.3.1–8.3.6
(INN-02 a INN-05)
8.1.5, 8.2.2 8.2.4 — —
9 Cierre — — — — —
Figura 7.19 Ubicación en la EDT de las innovaciones y la seguridad, la calidad, la migración y la implantación. Fuente: elaboración a partir de LafroX (2026d,
T-14) y Distribuidora Puelche S.A. (2026d, sec. 11).
LafroX
SpA
Subdocumento
7
Media
firma:
Alex
Aravena
28


---

LafroX SpA Introducción al Plan de trabajo
La matriz confirma que las cinco categorías se distribuyen desde el diseño hasta la operación.
Las innovaciones tienen paquetes en las fases donde se construyen, se contratan y se operan:
INN-01, INN-02, INN-03 e INN-05 se construyen en la cuenta 3.10; la fórmula contractual de
INN-04 se aprueba en la cuenta 5.4, porque es una innovación de modelo de contratación y no
tiene paquete de construcción; e INN-02 a INN-05 tienen su parte de operación en la cuenta
8.3. Cada innovación tiene sus meses en el Anexo 7.D (BA, art. 29, p. 19, punto 4).
Los anexos completan la cobertura. El Anexo 7.E relaciona los doce módulos y las quince
interfaces del Capítulo 4 con el paquete que los construye y prueba, y el Anexo 7.C ubica los
dieciséis resultados de aceptación del caso en su paquete y su momento. Los requerimientos
del Formulario T-12 se trazan a los paquetes mediante la matriz de trazabilidad del paquete
1.2.4, que se aprueba con el H1.
7.1.4 Diccionario y asignación de responsables
El diccionario de la EDT, en el Formulario T-14, describe cada paquete con su entregable, su
criterio de aceptación, su responsable y el período del cronograma en que se ejecuta, junto con
el hito del Formulario E-25 que habilita. Todo entregable se recibe con el acta de la Contraparte
Técnica, acompañada de su evidencia de verificación, su trazabilidad hacia los requerimientos
y las observaciones resueltas (BA, arts. 18.1 y 18.2, p. 13). Los criterios del diccionario se suman
a esa regla común. Por ejemplo, el paquete 3.4.1 (M1 Recepción) se acepta solo si ningún
producto con trazabilidad obligatoria se recibe sin lote, y el 4.1.2 (reversión de la Etapa 1) se
acepta solo si su ensayo termina antes de las 05:30, sostiene 96 despachos sin interrupción con
DTE válidos del ERP y no pierde ni duplica registros.
Los responsables son los ocho roles de la estructura para el proyecto del Capítulo 1, sección
1.5. La Tabla 7.3 muestra cómo se reparten los paquetes.
Tabla 7.3 Paquetes por responsable. Fuente: elaboración a partir de LafroX (2026d, T-14).
Rol PT % Fases con más paquetes
Líder de Operación /
SRE
58 26 % 6 (21), 3 (13), 8 (12)
Líder de Implantación y
Gestión del Cambio
34 15 % 7 (13), 4 (7)
Jefe de Proyecto 33 15 % 1 (22)
Líder de Desarrollo 24 11 % 3 (21)
Líder de Calidad 19 9 % 3 (15)
Arquitecto de Solución 18 8 % 2 (5), 3 (6)
continúa en la página siguiente
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
29


---

LafroX SpA Introducción al Plan de trabajo
Tabla 7.3 — continuación
Rol PT % Fases con más paquetes
Encargado de Seguridad
de la Información
18 8 % 1 (4), 2 (4), 3 (4)
Líder de Datos 18 8 % 3 (16)
Total 222 100 %
Todos los paquetes tienen un responsable único, de modo que son asignables. La distribu-
ción sigue la naturaleza del trabajo: el Jefe de Proyecto concentra la gestión y el gobierno; el
Líder de Desarrollo, la construcción; y el Líder de Implantación, la capacitación y la transición.
El Líder de Operación / SRE responde por un cuarto de los paquetes, porque reúne la nube,
la infraestructura de los cinco sitios y la operación, y sus paquetes de las fases 3 y 6 ocurren
a la vez. Responder por un paquete no significa ejecutarlo en persona: la sección 7.2.3 y el
Formulario T-15 muestran qué frente ejecuta el trabajo bajo cada rol.
7.2 Plan de trabajo
El plan de trabajo aplica las metodologías del Capítulo 6. La gestión del proyecto se basa en
el PMBOK: los alcances aprobados (H1 y H8) y el cronograma son las líneas base contra las
que se mide el avance; el avance se mide con valor ganado en el informe mensual (RT-19.06
y RT-19.07); y todo cambio de alcance, plazo o criterio de aceptación se aprueba antes de
incorporarse al plan, conforme al artículo 72 de las Bases Administrativas (p. 38) (paquete
1.4.3).
El desarrollo sigue las cuatro fases del proceso iterativo del Capítulo 6, que la EDT recorre
una vez por etapa. Dentro de la Construcción, cada módulo avanza por iteraciones que producen
resultados verificables, mientras que la marcha blanca y la aceptación formal ocurren solo en
los meses que fija el artículo 17 de las Bases Administrativas (pp. 12–13). El tablero de flujo del
equipo coordina las tareas diarias, pero no reemplaza el cronograma ni la aceptación formal
de los entregables, como establece la metodología de gestión de proyectos del Capítulo 6.
7.2.1 Secuenciamiento y dependencias
El orden del trabajo sigue las dependencias de datos y de infraestructura de Puelche (Ca-
pítulo 3, sección 3.4.3). Primero se aprueban el alcance (H1, mes 2) y el diseño (H2, mes 4).
En paralelo, se especifica y compra el equipamiento de la sala y de los sitios, y se contratan la
nube y los enlaces, de modo que la infraestructura híbrida y los ambientes queden habilitados
en el H3 del mes 6.
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
30


---

LafroX SpA Introducción al Plan de trabajo
La construcción de la Etapa 1 parte por la base compartida, porque si falla, fallan todos los
módulos. Sigue con recepción e inventario, que alimentan la preparación y el retiro sanitario,
mientras la preventa avanza en paralelo porque necesita stock y crédito. Las rutas y el reparto
se integran cuando existen el pedido confirmado y la preparación, y la rendición, cuando
existe la entrega registrada. La Etapa 2 se diseña en los meses 13 y 14 (H8), reutiliza los pedidos,
las guías y las evidencias ya probadas, y calcula el costo de servir con los hechos acumulados
desde la marcha blanca de la Etapa 1.
La Figura 7.20 presenta esa red de precedencias entre cuentas de control. El Anexo 7.B lista
las 34 dependencias entre paquetes con su fundamento.
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
31


---

LafroX
SpA
Introducción
al
Plan
de
trabajo
LafroX
SpA
Subdocumento
7
Media
firma:
Alex
Aravena
32


---

LafroX
SpA
Introducción
al
Plan
de
trabajo
ETAPA 1 · meses 1 a 16
ETAPA 2 · meses 13 a 21
Alcance y
diseño
Fases 1 y 2 ·
H1, H2
Construcción E1
Fase 3 · H4, H5
Sala técnica e
infraestructura
Fases 2, 5 y 6 ·
H3
Nube y
ambientes
Fases 5 y 3 · H3
Condiciones de
la marcha blanca
E1
1.2 Alcance
del proyecto
2.6
Experiencia
de usuario
2.1
Arquitectura
de la solución
2.2 Diseño de
la seguridad
2.4 Validación
de diseños
3.3 Base
compartida
3.4 Módulos
de la Etapa 1
3.8 Pruebas
de la Etapa 1
3.6.1–3.6.4
Integraciones
externas E1
2.3 Diseño de
sala y racks
5.1 Hardware
e
infraestructura
6.1 Sala
técnica de
Talca
6.3 Racks y
gabinetes
6.6
Infraestructura
de los sitios
5.2 Nube y
licencias
3.2 Servicios
de nube
3.1 Ambientes
3.7 Migración
de datos
6.5
Equipamiento
de campo
5.4 Acuerdos
con terceros
7.3
Certificación
de usuarios
4.1 Plan de
implantación
4.2 Marcha
blanca y
producción de
la Etapa 1
1.2.5 · 2.4.2
Línea base y
diseño E2
3.5 Módulos
de la Etapa 2
3.9 Pruebas
de la Etapa 2
3.6.5 · 3.6.6
Cadenas
7.1.4 · 7.3.2
Traspaso y
certificación E2
4.3 Marcha
blanca y
producción E2
8 Operación
9.1 Cierre de la
implementación
Ruta crítica del proyecto:
diseño E2 → módulos → pruebas (D-29 a D-31c)
H3
mes 6
◆ H1 ◆ H2
◆ H5
◆ H4
◆ H7
◆ H6
◆ H8 ◆ H10
◆ H9 ◆ H12
◆ H11
1.2.3 → 3.3.2 (interfaces ERP)
Ambientes
QA y DR
4.1.3
D-20
Figura 7.20 Red de precedencias entre cuentas de control e hitos. Fuente: elaboración a partir de LafroX (2026t, Anexo 7.B) y Distribuidora Puelche S.A. (2026a,
Formulario E-25).
LafroX
SpA
Subdocumento
7
Media
firma:
Alex
Aravena
33


---

LafroX SpA Introducción al Plan de trabajo
La red muestra tres convergencias. En el H3 se juntan la cadena de la nube (5.2, 3.2 y 3.1) y
la de la sala técnica (2.3, 5.1, 6.1, 6.3 y 6.6). En los hitos H4 y H5 se juntan los módulos, la base
compartida, el diseño aprobado y la experiencia de usuario. Al cierre de la marcha blanca se
juntan la solución certificada, la migración, el equipamiento de cada ola, la certificación de los
usuarios y, en la ola de reparto, los acuerdos con los transportistas y el sindicato. Un atraso en
cualquiera de esas ramas se propaga al hito aunque no sea de software. En el escenario nominal
anterior a la reestimación, el camino de menor holgura pasa por el diseño, los módulos y la
certificación de la Etapa 2; la sección 7.3.1 explica el alcance de ese resultado histórico.
El secuenciamiento incorpora además las condiciones de la operación de Puelche que
el caso exige ver en el plan (sección 17.5). Los congelamientos de septiembre y diciembre,
y el cierre de los tres primeros días hábiles de cada mes, son restricciones de calendario
para todo corte, despliegue e inicio de ola (paquete 1.3.1). La implantación en bodega y su
acompañamiento se programan en el turno de noche, entre las 22:00 y las 06:00 (paquete 4.2.2),
y la rotación del 38 % se atiende con capacitación continua y no con un evento único (paquete
7.1.2). Los 62 preventistas y los cerca de 200 conductores se capacitan en su ruta, sin detener la
venta ni el reparto (paquetes 7.1.1 y 4.2.2).
Los acuerdos con los diez transportistas y con el sindicato preceden a la ola de reparto
(paquetes 5.4.1 y 5.4.2), y la certificación del intercambio electrónico es un paquete por cadena
y no una tarea única (paquetes 3.6.5 y 3.6.6). Las interfaces del sistema de gestión se levantan
en el Inicio y se prueban temprano (paquetes 1.2.3 y 3.3.2). Las reglas de ruteo del planificador
se capturan en los talleres de los meses 1 a 3 y se validan sin él durante la marcha blanca
(paquete 1.2.2; resultado R18-16).
7.2.2 Estimación
El esfuerzo se estima por paquete con tres valores en horas hombre: optimista, más probable
y pesimista (PMI, 2017, p. 201). La incertidumbre de cada estimación se representa con una
distribución beta, una de las que el PMBOK admite para modelar la incertidumbre de duración y
recursos (PMI, 2017, p. 432). Con ella, la técnica PERT da el esfuerzo esperado 𝑇𝐸 = (𝑂+4𝑀+𝑃)/6
y su desviación 𝜎 = (𝑃 −𝑂)/6 (Malcolm et al., 1959). El PMBOK presenta también la distribución
triangular, (𝑂 + 𝑀 + 𝑃)/3 (PMI, 2017, p. 201); se prefiere la beta porque da cuatro veces más
peso al valor más probable, que el equipo funda en los requerimientos del Formulario T-12 y
en las cantidades del Formulario T-11.
La base de cada estimación depende del tipo de paquete. Los módulos y las integraciones
se estiman a partir de los requerimientos del Formulario T-12 asignados a cada paquete; la
infraestructura, a partir de las cantidades del Formulario T-11; la implantación, a partir de
las personas y rutas del caso; y la operación, a partir de los horarios de cobertura y de la
periodicidad de los informes. Los paquetes de la fase 8 se estiman por mes y se multiplican por
los 36 meses de operación. El Formulario T-15 detalla el método y las reglas de programación.
La duración de cada paquete se obtiene de su esfuerzo esperado y de la dotación asignada, y la
suma de las varianzas de los paquetes de la ruta crítica entrega la probabilidad de cumplir cada
hito con la aproximación normal de PERT. Para programar y controlar, el esfuerzo de cada
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
34


---

LafroX SpA Introducción al Plan de trabajo
paquete se reparte entre sus actividades del Formulario T-15, sección 6, sin cambiar su total.
La Tabla 7.4 resume el resultado de la estimación por etapa contractual, con la reserva
protegida separada del trabajo base.
Tabla 7.4 Horas hombre programadas por etapa — Fuente: elaboración a partir de LafroX (2026e, T-15), sección
4.3
Etapa Meses HH base y cobertu-
ra
HH de reserva
protegida
HH programadas
Etapa 1 · Desarro-
llo
1 a 12 38.141 0 38.141
Etapa 1 · Marcha
blanca
13 a 15 11.195 1.152 12.347
Etapa 2 · Desarro-
llo
13 a 18 11.407 0 11.407
Etapa 2 · Marcha
blanca
19 y 20 7.308 0 7.308
Soporte puente de
la Etapa 1
16 a 20 14.792 1.920 16.712
Cierre y estabi-
lización de la
implementación
21 y 22 2.775 0 2.775
Operación 21 a 56 128.854 0 128.854
Total 214.471 3.072 217.543
La operación concentra el 59 % de las horas programadas (128.854 de 217.543 HH), porque
cubre 36 meses de servicio continuo del centro de operaciones y la mesa, y el SOC desde
la primera marcha blanca del mes 13; la mesa incluye desde el mes 25, cuando la demanda
proyectada se acerca a su límite, un tercer agente en las franjas de menor demanda, con el
que cubre sus niveles de servicio hasta 2.391 contactos al mes. Son puestos de turno 24×7 y de
mesa, no personas dedicadas a otras tareas. La implementación propiamente tal, de los meses
1 a 22, suma 88.689 HH, y su tramo más denso son los meses 13 a 15, cuando la marcha blanca
de la Etapa 1 y el desarrollo de la Etapa 2 suman 17.513 HH (4.501,27 + 4.905,22 + 8.106,39,
según la curva del Formulario T-15, sección 4.4), con el máximo de 69 personas equivalentes
en el mes 15. Las 3.072 HH de reserva se asignan sólo a la Etapa 1, de modo que una corrección
en su marcha blanca no se financia con horas de la Etapa 2.
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
35


---

LafroX SpA Introducción al Plan de trabajo
7.2.3 Frentes de trabajo y sincronización
El trabajo se organiza en ocho frentes. Cada frente es un equipo con un responsable que
avanza en paralelo con los demás sobre un conjunto de cuentas de control. La Figura 7.21
presenta los frentes, su rol líder, sus cuentas de control y su ventana de actividad entre los
meses 1 y 21; la correspondencia completa está en el Formulario T-15.
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
36


---

LafroX
SpA
Introducción
al
Plan
de
trabajo
2027
1
feb
2
mar
3
abr
4
may
5
jun
6
jul
7
ago
8
sep
9
oct
10
nov
11
dic
2028
12
ene
13
feb
14
mar
15
abr
16
may
17
jun
18
jul
19
ago
20
sep
21
oct
Mes contractual →
Hitos del Formulario E-25
H1 H2 H3 H4
H6
H7
H8
H9
H10
H11
H12
F1 Dirección, gobierno y cumplimiento
Jefe de Proyecto · meses 1 a 56
→ hasta
el mes
56
F2 Arquitectura, seguridad y datos
Arquitecto de Solución · meses 1 a 21
F3 Construcción y correcciones E1
Líder de Desarrollo · meses 1 a 20 4.2.2 capacidad protegida
F4 Construcción de la Etapa 2
Líder de Desarrollo · meses 13 a 20
F5 Plataforma, infraestructura y soporte
puente 4.2.2 soporte puente
F6 Calidad y pruebas
Líder de Calidad · meses 1 a 21
F7 Implantación y gestión del cambio
Líder de Implantación y GC · meses 9 a 21
F8 Operación y soporte
Líder de Operación / SRE · meses 21 a 56
8.1–8.3,
8.5:
desde el
mes 21
hasta el
56
Solapamiento · meses 13 a 15 Solapamiento · meses 19 y 20
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
Leyenda Ventana del frente (Tabla T15.1) Cuentas de control activas (GanttPRO) Capacidad protegida / soporte puente 4.2.2
Solapamiento de etapas (Art. 17.2) Septiembre y diciembre (sin pasos a producción) Hito del Formulario E-25 (en su mes contractual)
H5
Líder de Operación / SRE · meses 1 a 20
Figura 7.21 Frentes de trabajo de los meses 1 a 21. Fuente: elaboración a partir de LafroX (2026d, T-14) y LafroX (2026e, T-15).
LafroX
SpA
Subdocumento
7
Media
firma:
Alex
Aravena
37


---

LafroX SpA Introducción al Plan de trabajo
La figura muestra que en ningún mes trabaja un solo frente: entre los meses 1 y 15 avanzan
a la vez la dirección, la arquitectura, la construcción de la Etapa 1, la plataforma y la calidad,
y desde el mes 9 se suma la implantación. Los frentes se sincronizan en tres instancias. La
primera son los hitos del Formulario E-25, porque cada hito exige que varios frentes entreguen
a la vez. La segunda son los comités del artículo 71 de las Bases Administrativas (p. 37): el de
Proyecto es quincenal y los de Arquitectura y Operación son mensuales, y sus actas registran los
acuerdos entre frentes en dos días hábiles (RT-19.09). La tercera son las ventanas de calendario,
que son comunes a todos los frentes.
7.2.4 Solapamientos de los meses 13 a 15 y 19 a 20
El artículo 17.2 de las Bases Administrativas (p. 13) obliga a dimensionar dotación y frentes
para dos esfuerzos simultáneos. En los meses 13 a 15 trabajan a la vez el frente de implantación
(F7), en la marcha blanca de la Etapa 1 con su acompañamiento; el de construcción de la Etapa
1 (F3), en las correcciones de esa marcha blanca; el de construcción de la Etapa 2 (F4), en su
desarrollo, con el H8 en el mes 14; el de calidad (F6), en las pruebas de ambas etapas; y los
frentes de dirección y de arquitectura (F1 y F2).
F3 y F4 dependen del mismo rol, el Líder de Desarrollo, pero son equipos distintos. Si
el mismo equipo atendiera la marcha blanca y desarrollara la Etapa 2, cada incidente de la
marcha blanca atrasaría la Etapa 2, que es precisamente la situación que el artículo 17.2 de las
Bases Administrativas (p. 13) busca evitar. La Figura 7.21 lo hace visible: en la franja sombreada
de los meses 13 a 15, las barras de F3 y F4 coexisten en carriles separados.
En los meses 19 y 20 la Etapa 1 está en producción y la Etapa 2 en marcha blanca. Trabajan
F7, en la marcha blanca de la Etapa 2; F4, en sus correcciones; F6, en las pruebas; y el soporte
de la Etapa 1 en producción. La dotación de cada frente en cada solapamiento se presenta en
el Formulario T-15, de modo que los dos esfuerzos se sumen sin contar dos veces a las mismas
personas.
7.3 Cronograma e implantación
El cronograma aplica el artículo 17 de las Bases Administrativas (pp. 12–13) mes a mes y la
implantación aplica las condiciones del Caso logística (secciones 13.3 y 17.6, pp. 23 y 33). Esta
sección presenta la ruta crítica, la carta Gantt, el plan de implantación, las marchas blancas, la
estabilización y el momento en que se alcanza cada resultado comprometido. El detalle está
en los Formularios T-14, T-15 y T-18.
7.3.1 Ruta crítica y holguras
La ruta crítica se calcula con el método de la ruta crítica sobre la red del Anexo 7.B (PMI,
2017, pp. 210–211). Una pasada hacia adelante da las fechas tempranas de cada paquete; una
pasada hacia atrás, desde los meses fijos del artículo 17 de las Bases Administrativas (pp. 12–13),
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
38


---

LafroX SpA Introducción al Plan de trabajo
da las tardías; LS − ES es la holgura total; la libre se mide contra el ES de los sucesores. Como
los hitos del Formulario E-25 son fechas fijas, un camino que no llega a su hito tiene holgura
negativa y obliga a replanificar.
En el escenario nominal anterior a la reestimación, la cadena de menor holgura correspon-
de a la Etapa 2: diseño (1.2.5, 2.1.4 y 2.4.2) → módulos (3.5) → integración (3.9.1) → certificación
(3.9.2–3.9.7). La Tabla 5.2 del Formulario T-15 conserva sus antiguas reservas y probabilidades
como referencia histórica; no están recalculadas con las 217.543 HH ni con asignaciones
nominales. También requieren comprobación las cadenas de la Etapa 1, la sala técnica, los
acuerdos de implantación y la certificación de cadenas. Las marchas blancas y los pasos a pro-
ducción mantienen sus fechas contractuales fijas. La Figura 7.22 representa las dependencias
del escenario nominal, sin acreditar la ruta crítica de la línea base actual.
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
39


---

LafroX SpA Introducción al Plan de trabajo
2027
1
feb
2
mar
3
abr
4
may
5
jun
6
jul
7
ago
8
sep
9
oct
10
nov
11
dic
2028
12
ene
13
feb
14
mar
15
abr
16
may
17
jun
18
jul
19
ago
20
sep
21
oct
Mes contractual
→
Hitos del Formulario
E-25
H1 H2 H3 H4 H5
H6
H7
H8 H9 H10
H11
H12
Ruta crítica · Etapa 2
1.2.5 · 2.1.4 Línea base y
diseño E2
H8: reserva 4 días hábiles · 91,1 % \
(simulación con riesgos\)
2.4.2 Acta de diseño E2 \(revisión del
CLIENTE\)
3.5 Módulos de la Etapa 2
3.9.1 Prueba de integración E2
3.9.2–3.9.7 Certificación
E2 H10: reserva 25 días
hábiles
Casi crítico · Etapa 1 \(interfaces del
ERP\)
1.2.3 Interfaces sin
documentación
3.3 Base compartida \(3.3.2 ERP\)
3.4 Módulos de la Etapa 1
3.8.1 Prueba de integración E1 H4: reserva 19 días hábiles
3.8.2–3.8.8 Certificación E1 H5: reserva 35 días hábiles
Casi crítico · sala técnica y
ambientes \(H3\)
2.3 Planos de sala y racks
5.1.2 Especificación y compra
6.1 Sala técnica de Talca
6.3.1–6.3.3 y 6.6.3 Racks y borde
de los CD
3.2 y 3.1 Servicios de nube y
ambientes
H3: reserva 19 días hábiles
Otros caminos casi críticos
1.2.2 Reglas de ruteo del
planificador
3.4.7 M4 Rutas \(usa las reglas
capturadas\)
5.4.1 · 5.4.2 Transportistas y
sindicato
3.6.5 · 3.6.6 Intercambio con las
cadenas
1.2.1 · 1.2.4 Alcance y
trazabilidad
H1: reserva 6 días hábiles (la menor; σ 0,58, > 99,9 %\)
Marcha blanca E1 Marcha blanca E2
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
Leyenda Ruta crítica \(D-29 a D-31c\)
Casi crítico E1 \(D-02, D-04, D-14 a
D-25\)
Casi crítico del H3 \(D-07 a D-13\)
Otros casi críticos \(D-03, D-27, D-
32\)
Reserva hasta la fecha límite del
hito
Marcha blanca \(Art. 17°\)
Septiembre y diciembre \(sin
pasos a producción\)
Hito del Formulario E-25 \(en su
mes contractual\)
H9: reserva 21 días hábiles · 100
% (simulación con riesgos\)
Figura 7.22 Dependencias y caminos de menor holgura del escenario nominal histórico; sujetos a recálculo.
Fuente: elaboración a partir de LafroX (2026t, Anexo 7.B) y LafroX (2026d, T-14, períodos contractuales).
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
40


---

LafroX SpA Introducción al Plan de trabajo
La Figura 7.22 relaciona las cadenas de diseño, construcción y certificación con sus hitos y con
las marchas blancas de ambas etapas. El escenario nominal del Formulario T-15 incluye las
dependencias, los diez días hábiles de revisión del artículo 18.3 de las Bases Administrativas (p.
13) y una hipótesis de hasta 40 desarrolladores simultáneos, todavía pendiente de asignación
nominal. Las reservas, probabilidades y fechas P80 de su Tabla 5.2 y del modelo de riesgos
previo corresponden a ese escenario histórico; no deben interpretarse como resultados de
la línea base de 217.543 HH. Las marchas blancas y sus cuatro semanas finales no aportan
reserva utilizable.
La holgura se gestiona en las instancias de gobierno de la EDT. El avance de cada paquete de la
ruta crítica y de los caminos casi críticos se revisa en la reunión semanal de seguimiento y en
el Comité de Proyecto quincenal (paquetes 1.3.5 y 1.8.3). Toda amenaza a un hito se escala al
Comité Ejecutivo cuando la desviación proyectada supera la mitad de su reserva, sin esperar a
consumirla, con su análisis de impacto (paquetes 1.4.3 y 1.8.2). El informe mensual con valor
ganado avisa toda desviación mayor al 10 % con su plan dentro de cinco días hábiles (paquete
1.8.6). H7 y H12 dependen además de la aceptación copulativa de la marcha blanca, que no
tiene una probabilidad calculada.
7.3.2 Carta Gantt y calendario
La carta Gantt del Formulario T-14 cubre los 56 meses y muestra las marchas blancas, los pasos
a producción y el inicio de la Operación. La Tabla 7.5 ubica los doce hitos del Formulario E-25
con el paquete que entrega cada uno.
Tabla 7.5 Hitos del Formulario E-25 en el cronograma. Fuente: elaboración a partir del Formulario E-25 y LafroX
(2026d, T-14).
Hito Mes Entregable que lo gatilla Paquetes
H1 2 Línea base de alcance y
matriz de trazabilidad
1.2.1, 1.2.4
H2 4 Arquitectura, plan de
seguridad y modelo de
datos aprobados
2.4.1
H3 6 Infraestructura híbri-
da y ambientes con
observabilidad
3.1.1, 3.1.2, 3.1.3, 3.1.5
H4 10 Software de la Etapa 1
con QA superado
3.8.1
continúa en la página siguiente
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
41


---

LafroX SpA Introducción al Plan de trabajo
Tabla 7.5 — continuación
Hito Mes Entregable que lo gatilla Paquetes
H5 12 Certificación de la Eta-
pa 1
3.8.7
H6 13 Inicio de la marcha
blanca de la Etapa 1
4.2.1
H8 14 Línea base y diseño de
la Etapa 2
1.2.5, 2.4.2
H7 16 Paso a producción de la
Etapa 1
4.2.3
H9 17 Software de la Etapa 2
con QA superado
3.9.1
H10 18 Certificación de la Eta-
pa 2
3.9.6
H11 19 Inicio de la marcha
blanca de la Etapa 2
4.3.1
H12 21 Paso a producción de
la Etapa 2 y aceptación
final
4.3.3, 4.3.4
La tabla está ordenada por mes y no por número de hito, porque el H8 (mes 14) ocurre antes
que el H7 (mes 16). Ese cruce es la expresión concreta del solapamiento: la línea base de la
Etapa 2 se aprueba mientras la Etapa 1 está en su marcha blanca.
Los meses contractuales caen en meses calendario distintos según la fecha de inicio del
contrato, que aún no está definida (consulta V-12). La Tabla 7.6 aplica la regla a los tres inicios
que el Capítulo 3, sección 3.1.2, considera compatibles con poner la Etapa 2 en producción
antes de enero de 2029, fecha desde la que rigen las condiciones de la principal cadena de
supermercados.
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
42


---

LafroX SpA Introducción al Plan de trabajo
Tabla 7.6 Meses contractuales según la fecha de inicio. Fuente: elaboración a partir de Distribuidora Puelche S.A.
(2026a, art. 17) y Distribuidora Puelche S.A. (2026c, secs. 13.2 y 13.3).
Inicio Mes 13 (H6) Mes 16 (H7) Meses 19 y 20 Mes 21 (H12)
Diciembre de 2026 Diciembre de
2027
Marzo de 2028 Junio y julio de
2028
Agosto de 2028
Febrero de 2027 Febrero de 2028 Mayo de 2028 Agosto y septiem-
bre de 2028
Octubre de 2028
Marzo de 2027 Marzo de 2028 Junio de 2028 Septiembre y
octubre de 2028
Noviembre de
2028
Ningún inicio admisible deja las dos marchas blancas completas fuera de septiembre y diciem-
bre; el Anexo 7.A extiende el análisis a los ocho meses de inicio admisibles. Con un inicio en
diciembre de 2026, el inicio de la marcha blanca de la Etapa 1 cae en diciembre; con uno en
marzo de 2027, el inicio de la marcha blanca de la Etapa 2 cae en septiembre. Con febrero de
2027, en cambio, el congelamiento afecta solo el segundo mes de la marcha blanca de la Etapa
2 y no un inicio, por lo que LafroX lo adopta como supuesto de calendario del cronograma. Su
costo es que las semanas de cierre de esa marcha blanca coinciden con el peak de septiembre,
que la sección 7.3.5 trata. Dentro de un mes de congelamiento no se inicia ninguna ola ni se
despliega ningún cambio, y la marcha blanca continúa en convivencia, con medición diaria.
La Figura 7.23 presenta la carta Gantt resumida de los 56 meses con ese supuesto de inicio,
por período contractual. La carta vigente por cuenta de control, generada desde las ventanas
reconciliadas de los 222 paquetes, está en el Formulario T-14, sección 3.1.
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
43


---

LafroX
SpA
Introducción
al
Plan
de
trabajo
2027 2028 2029 2030 2031
1 2 3 4 5 6 7 8 9 1011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556
Hitos del Formulario E-25 H1 H2 H3 H4 H5
H6
H8 H7H9
H10
H11
H12
Períodos obligatorios del Art. 17°
Etapa 1 · Desarrollo
Etapa 1 · Marcha blanca
Etapa 1 · Producción
Etapa 2 · Desarrollo
Etapa 2 · Marcha blanca
Etapa 2 · Producción y aceptación
Operación contractual · 36 meses
Fases de la EDT
F1 · Inicio, gobierno y control
F2 · Elaboración
F3 · Construcción
F4 · Transición
F5 · Adquisiciones
F6 · Infraestructura física
F7 · Capacitación y cambio
F7 · Capacitación continua
F8 · SOC previo a operación
F8 · Operación y soporte
F9 · Cierre
Gris: septiembre y diciembre; no se inician olas ni se despliegan cambios.
Mes 20: continúa la marcha blanca de E2 durante el congelamiento. SOC comienza en el 13; operación contractual en el 21.
Figura 7.23 Carta Gantt resumida de los 56 meses, con inicio en febrero de 2027. Fuente: elaboración a partir de Distribuidora Puelche S.A. (2026a, art. 17, pp.
12–13 y Formulario E-25) y LafroX (2026d, T-14).
LafroX
SpA
Subdocumento
7
Media
firma:
Alex
Aravena
44


---

LafroX SpA Introducción al Plan de trabajo
La carta muestra que los periodos fijos del artículo 17 de las Bases Administrativas (pp. 12–13)
se respetan mes a mes y que ningún paso a producción cae en una columna de congelamiento:
el mes 16 es mayo de 2028 y el mes 21, octubre de 2028. Las fases de desarrollo aparecen dos
veces, una por etapa, y la capacitación continúa durante la operación por la rotación de la
bodega. Las columnas rayadas del mes 20 y del mes 23 confirman lo que anticipa la Tabla 7.6:
el cierre de la marcha blanca de la Etapa 2 ocurre en septiembre y el primer diciembre de
operación llega dos meses después de la aceptación final.
Antes de cada paso a producción, el cronograma reserva las pruebas que exige el numeral
20.1 de las Bases Técnicas Transversales (p. 35): carga y estrés a 1,5 veces el peak, resiliencia,
recuperación ante desastres con conmutación real, seguridad ofensiva y accesibilidad. Además,
programa dos ensayos de migración antes de la migración definitiva. En la Etapa 1 estas pruebas
forman la cuenta 3.8, se ejecutan en los meses 9 y 10 y se entregan antes del H5 del mes 12; en
la Etapa 2 forman la cuenta 3.9, se ejecutan en los meses 16 y 17 y se entregan antes del H10
del mes 18 (Formulario T-15, Tabla 5.2).
7.3.3 Plan de implantación y puesta en marcha
La implantación sigue el principio que impone el caso: nada entra en producción sin haber
convivido con la forma actual de trabajar, y nada se despliega como un único evento (sección
13.3, condiciones 1 y 3). Técnicamente, cada capacidad se publica con un despliegue azul-verde
y se habilita por sitio y por ola mediante indicadores de funcionalidad (feature flags), conforme
al Capítulo 4, apartado 4.2.4.1.2. Así, cada ola puede revertirse sin reinstalar y cada operación
tiene un único escritor autorizado (Capítulo 4, sección 4.1.8). Ningún despliegue ocurre en
la ventana de despacho de 05:30 a 07:00, que no admite indisponibilidad, ni en fechas de
congelamiento (Caso, cap. 15, RT-10.05, p. 27).
La Etapa 1 entra en tres olas, en el orden de las dependencias de datos (Capítulo 3, sección
3.4.4). La Tabla 7.7 las presenta.
Tabla 7.7 Olas de implantación de la Etapa 1. Fuente: elaboración a partir de LafroX (2026k, SD3, sec. 3.4.4), y
LafroX (2026s, T-18).
Ola Procesos Módulos Avance Registro oficial
1 Datos maestros y
recepción con lote
M1 Por sitio Recepciones y
lotes
2 Inventario con FE-
FO y preparación
nocturna
M2, M5 Por sitio Stock y prepara-
ción
continúa en la página siguiente
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
45


---

LafroX SpA Introducción al Plan de trabajo
Tabla 7.7 — continuación
Ola Procesos Módulos Avance Registro oficial
3 Preventa, rutas,
reparto, devolucio-
nes y rendición
M3, M4, M6, M8,
M7
Por zona comer-
cial
Pedidos, entregas
y cobros
Una ola avanza a la siguiente cuando cumple su criterio durante cuatro semanas consecutivas a
volumen real: sin defectos críticos ni altos, con conciliación diaria sin diferencias no explicadas,
con los indicadores de disponibilidad y tiempo de respuesta cumplidos, con los usuarios
certificados y con el acta de la Contraparte Técnica (Capítulo 3, sección 3.4.4).
La programación de olas usa fechas reales y no una equivalencia de meses a 13 semanas: todos
los grupos deben estar operativos antes del inicio de los 28 días finales de marcha blanca.
La sección 6.1 del Formulario T-18 propone Talca/Concepción/plataformas/remanentes en
semanas 5/6/7/8 para la ola de reparto, subordinadas a fechas permitidas y al límite F − 28 días.
Se permite superposición por dominios sin intervenir simultáneamente el mismo proceso ni
doble escritura.
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
46


---

LafroX SpA Introducción al Plan de trabajo
Semana 5
Talca
Semana 6
Concepción
Semana 7
Plataformas
Semana 8
Remanentes
Antes de comenzar los últimos 28 días: todo el alcance activo, con
fechas sujetas a ventanas permitidas y sin doble escritura
Últimos 28 días de marcha blanca (referencia: semanas 10--13)
Volumen real completo en todas las zonas + criterios sostenidos
durante cuatro semanas consecutivas
Figura 7.24 Secuencia de olas de la Etapa 1 durante la marcha blanca. Fuente: elaboración a partir de LafroX
(2026k, SD3, sec. 3.4.4), y LafroX (2026s, T-18).
El avance de cada grupo exige su criterio y acompañamiento. Las cuatro semanas finales
requieren todos los grupos y todo el volumen real, no una muestra. E2 habilita todas las
cadenas del alcance, portales y costo de servir antes de F − 28 días y, en el ejemplo febrero
2027, antes de septiembre. La carga manual de pedidos mantiene contingencia auxiliar y no
acredita intercambio electrónico ni permite excluir una cadena faltante.
La reversión tiene dos niveles, que la Tabla 7.8 distingue.
Tabla 7.8 Niveles de reversión. Fuente: elaboración a partir de LafroX (2026k, SD3, sec. 3.4.4); LafroX (2026m,
SD4, apartados 4.2.4.1.2 y 4.1.8); y LafroX (2026s, T-18).
Nivel Qué hace Quién decide Plazo
Técnico Devuelve el tráfico a
la entrega previa por
azul-verde/canario o
desactiva el indicador
de funcionalidad (featu-
re flag)
Líder de Operación /
SRE
Objetivo ≤10 minutos,
medido en cada ensayo
en Preproducción,
fuera de la ventana de
despacho
Operacional, Etapa 1 Conserva/restaura
versión operativa local
probada, único escritor
y DTE válidos; papel
sólo de apoyo
Responsable de opera-
ciones del CLIENTE
Completo antes de las
05:30
continúa en la página siguiente
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
47


---

LafroX SpA Introducción al Plan de trabajo
Tabla 7.8 — continuación
Nivel Qué hace Quién decide Plazo
Operacional, Etapa 2 Desactiva la capacidad
de la Etapa 2 que falla,
sin tocar la Etapa 1
Responsable de opera-
ciones del CLIENTE
Fuera de la ventana de
05:30 a 07:00
La reversión operacional se dispara con señales observables: pedidos sin sincronizar al inicio
de la carga, rutas del día no disponibles o un defecto crítico en la ventana de despacho. El
plazo de las 05:30 protege la salida de los 96 camiones y no es el tiempo de recuperación ante
desastres. La Figura 7.25 presenta el procedimiento por rol.
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
48


---

LafroX SpA Introducción al Plan de trabajo
Operacional
Versión local y documentos ERP válidos antes de las
05:30
Sí
Responsable de Operaciones del CLIENTE
autoriza la reversión operacional
No
Corregir; la ola
continúa
¿Amenaza el
despacho?
Turno de noche
Se detecta una incidencia que
podría afectar el despacho.
Acompañante verifica el
impacto y lo informa a
Operaciones del CLIENTE
Técnica
Volver a versión anterior o desactivar el
interruptor
Al retomar, conciliar los registros que quedaron en
cola, sin pérdida ni duplicación
La ola afectada reinicia sus cuatro semanas de cumplimiento
Figura 7.25 Procedimiento de reversión de la Etapa 1 en la ventana de despacho. Fuente: elaboración a partir de
LafroX (2026s, T-18).
La figura muestra que la decisión es del CLIENTE y se toma en el turno de noche, antes de
que empiece el despacho. El ensayo debe comprobar que lo capturado permanece en cola y se
concilia sin pérdida ni duplicación; no se presume por la descripción. Lo que se pierde es el
avance de la ola, que reinicia su período de cuatro semanas (Caso, sección 17.6, punto 4, p. 33).
La reversión se ensaya en Preproducción antes de cada corte (paquete 4.1.2), y en ese ensayo
se mide el tiempo de cada nivel.
7.3.4 Marcha blanca de la Etapa 1
La marcha blanca de la Etapa 1 son tres meses de operación supervisada con datos y usuarios
reales, del mes 13 al 15. Convive con la operación vigente: en bodega, con la hoja de picking;
en ruta, con la guía en papel; y en Talca, con el WMS de 2013 en solo lectura como respaldo de
consulta. Cada día se concilian ambos registros, y toda diferencia se clasifica y explica antes
del cierre del día (RT-20.03). La Tabla 7.9 presenta los indicadores que se miden y publican
diariamente, con sus umbrales de cierre (RT-20.04).
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
49


---

LafroX SpA Introducción al Plan de trabajo
Tabla 7.9 Indicadores diarios de la marcha blanca. Fuente: elaboración a partir de Distribuidora Puelche S.A.
(2026a, art. 17.3); Distribuidora Puelche S.A. (2026c, RT-09.01 y RT-10.05); y LafroX (2026k, SD3, Tabla 3.5).
Indicador Umbral Condición Art. 17.3
Incidentes críticos y altos abier-
tos
0 1
Transacciones de la ola registra-
das en la solución
100 % del volumen real durante
las 4 últimas semanas
2
Indisponibilidad en la ventana
de 05:30 a 07:00
0 minutos 3
Disponibilidad de la transacción
crítica
99,9 % o más 3
Tiempo de respuesta, percentil
95
Línea de preparación hasta 1
s; entrega hasta 2 s; línea de
preventa hasta 1,5 s; stock y
crédito hasta 2 s
3
Diferencias de conciliación sin
explicar
0 4
Usuarios de la ola certificados 100 % 5
Los indicadores reproducen las condiciones del artículo 17.3 de las Bases Administrativas (p.
13) con umbrales que se pueden medir cada día, de modo que el cierre no depende de un
juicio al final del período. El volumen comprometido es la operación real completa de cada
proceso y no una muestra; con las cifras del caso (sección 14.1), son cerca de 1.150 recepciones
de proveedor y 260.000 líneas de preparación al mes, unos 31.000 pedidos al mes y alrededor
de 1.400 entregas por día hábil, o 2.600 si las semanas de cierre coinciden con el peak de
septiembre. El detalle por proceso está en el Formulario T-18, Tabla T-18.1.
La sexta condición del artículo 17.3 de las Bases Administrativas (p. 13) es el acta de la Contra-
parte Técnica, que en la Etapa 1 es el H7 del mes 16. Si una condición no se cumple al término
del mes 15, la marcha blanca se extiende a costo de LafroX, sin mover las fechas siguientes
(BA, art. 17.3, p. 13). La Figura 7.26 resume el ciclo diario de control; las condiciones de cierre
se enumeran debajo.
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
50


---

LafroX SpA Introducción al Plan de trabajo
Medir
indicadores y
conciliar
registros
Comparar
resultados con
los umbrales
Decidir:
continuar,
corregir o
revertir
Publicar el
resultado
diario
Figura 7.26 Ciclo diario de la marcha blanca. Fuente: elaboración a partir de Distribuidora Puelche S.A. (2026a,
art. 17.3, p. 13) y Distribuidora Puelche S.A. (2026b, RT-20.04, p. 35).
El ciclo de la Figura 7.26 se repite cada día: se miden los indicadores y se concilian los registros,
se comparan los resultados con sus umbrales, se decide entre continuar, corregir o revertir y
se publica el resultado diario. Si una incidencia amenaza de inmediato el despacho, se activa
el procedimiento de reversión de la Figura 7.25 sin esperar la publicación diaria.
El cierre exige cumplir simultáneamente las seis condiciones del artículo 17.3 de las Bases
Administrativas (p. 13):
1. Cero incidentes críticos o altos abiertos.
2. Volumen real completo durante las últimas cuatro semanas.
3. Sin indisponibilidad en despacho; disponibilidad y respuesta dentro de umbral.
4. Sin diferencias inexplicadas ni pedidos perdidos o duplicados.
5. 100 % de usuarios capacitados y certificados.
6. Acta de aceptación de la Contraparte Técnica (H7).
Ninguna de estas condiciones compensa a otra.
La capacitación se hace en el puesto y en la ruta con las cuatro modalidades del artículo 90.2
de las Bases Administrativas (p. 45). Cada perfil se certifica antes del cierre, porque el artículo
17.3 de las Bases Administrativas (p. 13) exige que el personal del CLIENTE esté «capacitado
y certificado conforme al plan de capacitación aprobado», y los usuarios administradores y
el equipo técnico del CLIENTE se certifican además conforme al artículo 90.4 de las Bases
Administrativas (p. 45). Los perfiles operativos, tomados del Capítulo 3, Anexo 3.I, son 120
preparadores, con un tutor por turno y un aprendizaje en el puesto de dos horas como máximo;
62 preventistas, en su propia ruta; 84 integrantes de la tripulación propia; y cerca de 160
conductores de transportistas, que se incorporan en el andén al asignarse a una ruta.
La adopción se mide por perfil y por ola, y si una ola no alcanza la meta, no avanza y se
extiende el acompañamiento. La respuesta es distinta según el grupo: el personal con veinte o
treinta años en la compañía recibe acompañamiento individual y reconocimiento formal de su
conocimiento, y el personal rotativo de preparación cuenta con un tutor por turno (Formulario
T-18, secciones 2.7 y 2.8).
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
51


---

LafroX SpA Introducción al Plan de trabajo
7.3.5 Marcha blanca de la Etapa 2 y convivencia
La marcha blanca de la Etapa 2 dura los meses 19 y 20 y convive con la Etapa 1 en producción.
La regla central del artículo 17.2 de las Bases Administrativas (p. 13) es que exista una única
fuente de verdad para los datos compartidos: la Etapa 2 lee y extiende los pedidos, clientes,
guías y entregas de la Etapa 1, sin copiarlos ni digitarlos de nuevo, y ningún despliegue de la
Etapa 2 modifica las funciones estabilizadas de la Etapa 1 ni ocurre en la ventana de despacho.
Esta marcha blanca dura unas 8,7 semanas (2 × 52 / 12). Como el artículo 17.3 de las Bases
Administrativas (p. 13) exige volumen real en las cuatro últimas, todas las cadenas certificadas,
los portales y el costo de servir deben quedar habilitados en las primeras 4,7 semanas. Con
el inicio supuesto de febrero de 2027, el mes 19 es agosto y el mes 20 es septiembre de 2028,
de modo que toda habilitación ocurre en agosto, antes del congelamiento del 1 al 25 de sep-
tiembre. Las semanas de cierre se miden con el volumen del peak de Fiestas Patrias, cerca
de 2.600 entregas diarias, en el primer septiembre de la Etapa 1 en producción. Durante el
congelamiento se aplica continuidad previamente autorizada por el CLIENTE; la sección 6.4 del
Formulario T-18 no presume que un cambio de configuración esté exento de las prohibiciones.
La capacidad para ese peak se demuestra antes del H11 con la prueba de carga a 1,5 veces el
peak, con ambas etapas activas (paquete 3.9.3; Formulario T-18, sección 3.1).
A los indicadores de la Tabla 7.9 se suman los propios del alcance de la Etapa 2: los pedidos
de las cadenas certificadas recibidos por vía electrónica, los avisos de despacho dentro de
dos minutos, las entregas con costo de servir calculado y la ausencia de degradación de los
indicadores de la Etapa 1 (Formulario T-18, sección 3.3). La Figura 7.27 muestra cómo fluyen
los datos entre ambas etapas.
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
52


---

LafroX SpA Introducción al Plan de trabajo
ERP
Registro con-
table y emisor
único de guías
Etapa 1
Producción
estable
Registro
compartido
Pedidos, clientes,
guías,
entregas, lotes y
cobros
Etapa 2 en marcha
blanca
Canal moderno (M11),
portales y costo de
servir (M10)
Extiende
los datos
Documentos
válidos
Opera y
escribe
Lee
Figura 7.27 Convivencia de la Etapa 1 en producción con la Etapa 2 en marcha blanca. Fuente: elaboración a
partir de LafroX (2026m, SD4, arquitectura lógica).
Se mantiene una sola fuente de verdad y un escritor autorizado por dato. La Etapa 2 no duplica
datos ni modifica las funciones estabilizadas de la Etapa 1. Lee el registro único y lo extiende
con sus propios datos, de modo que no existe una doble digitación que conciliar. El ERP se
mantiene como registro contable y único emisor de la guía de despacho para ambas etapas. El
paso a producción del mes 21 es la aceptación final de la implementación (H12) y el inicio de
la Operación con ambos alcances (BA, art. 17.2, punto 4, p. 13).
7.3.6 Estabilización y transferencia
Después de cada paso a producción hay una estabilización de cuatro semanas por ola, con
atención reforzada y sin costo adicional (RT-20.06). La dotación se deriva de la operación del
caso, como muestra la Tabla 7.10.
Tabla 7.10 Estabilización por ola. Fuente: elaboración a partir de LafroX (2026k, SD3, sec. 3.4.4).
Frente Personas Cálculo
Bodega, turno de noche 2 1 por centro de distribución
Plataformas de cross-docking 3 1 por plataforma
Calle 7 158 rutas diarias / 24 días de
lunes a sábado ≈ 6,6
continúa en la página siguiente
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
53


---

LafroX SpA Introducción al Plan de trabajo
Tabla 7.10 — continuación
Frente Personas Cálculo
Coordinación 1 Líder de Implantación y Gestión
del Cambio
Las siete personas de calle permiten acompañar cada una de las 158 rutas diarias (96 camiones
y 62 preventistas) al menos una vez en las cuatro semanas. Si la ola cubre una sola zona, la
dotación se reduce en proporción a sus rutas, y la dotación decrece según la curva de adopción,
como exige el RT-20.05.
La operación se transfiere al equipo de TI de cuatro personas del CLIENTE antes del mes 21,
con procedimientos documentados y ensayados y con la base de conocimiento. Sigue una
mentoría de seis meses (paquetes 7.1.4 y 8.5.2; RT-22.07). Quedan como servicio permanente
de LafroX durante los 36 meses los que el Capítulo 3, sección 3.4.5, le asigna: el centro de
operaciones, la mesa de servicio, la gestión de incidentes, la continuidad, la seguridad y el
mantenimiento.
7.3.7 Momento de los resultados comprometidos
El Caso logística exige indicar en qué momento del cronograma se alcanza cada resultado
de aceptación (cap. 18, p. 34). La Tabla 7.11 agrupa los dieciséis resultados por momento; el
detalle por resultado está en el Anexo 7.C.
Tabla 7.11 Momento de los resultados de aceptación del caso. Fuente: elaboración a partir de Distribuidora
Puelche S.A. (2026c, cap. 18); LafroX (2026j, Anexo 3.J); y LafroX (2026t, Anexo 7.C).
Momento Resultados Cant. Aceptación
Marcha blanca de la
Etapa 1 (meses 13 a 15)
R18-01, 02, 03, 05, 06,
07, 08, 09, 10, 14, 15 y 16
12 H7 (mes 16)
Marcha blanca de la
Etapa 2 (meses 19 y 20)
R18-11 y 13 2 H12 (mes 21)
Tramos durante el
contrato
R18-04: OTIF de 90 %
en el mes 15, 93 % en el
mes 19 y 95 % en el mes
32
1 Revisión mensual en
comité
continúa en la página siguiente
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
54


---

LafroX SpA Introducción al Plan de trabajo
Tabla 7.11 — continuación
Momento Resultados Cant. Aceptación
Provisional y final R18-12: provisional en
la marcha blanca de la
Etapa 1 y final tras 12
meses de operación
1 H7 y operación
Doce de los dieciséis resultados se aceptan en la marcha blanca de la Etapa 1. Otros dos también
se verifican allí: R18-04, con su tramo del mes 15, y R18-12, de forma provisional. Son catorce
resultados con verificaciones en ese período, conforme al Anexo 7.C y al Formulario T-18. Por
eso el volumen real y la certificación de usuarios de ese período son la principal concentración
de riesgo de aceptación del proyecto, y por eso el plan dedica a esa marcha blanca su mayor
dotación de acompañamiento.
Las innovaciones también tienen su momento en el cronograma (BA, art. 29, punto 4, p. 19),
como resume la Tabla 7.12.
Tabla 7.12 Innovaciones en el cronograma. Fuente: elaboración a partir de LafroX (2026t, Anexo 7.D).
Innovación Paquetes de la EDT Meses Hito
1 · Seguimiento de
vencimiento posentrega
en el local
3.10.1.1 a 3.10.1.4 7 a 15 H4, H5 y marcha blanca
E1
2 · Reproducción de
incidentes de terreno
3.10.2.1 a 3.10.2.4; 8.3.1 2 a 15; 21 a 56 H4 y marcha blanca E1
3 · Vida útil remanente
por historia térmica del
lote
3.10.3.1 a 3.10.3.4; 8.3.2 3 a 15; operación H4, H5 y marcha blanca
E1
4 · Tramo variable de
la Operación ligado al
costo de servir
5.4.3; 8.3.3; 8.3.4 17 a 20; 21 a 23; 24 a 56 Hito mensual
5 · Hoja de negocio del
almacenero
3.10.4.1 a 3.10.4.4; 8.3.5;
8.3.6
13 a 27 H9, H10 y H12
Tres innovaciones se validan en la marcha blanca de la Etapa 1. La innovación 5 sigue el
calendario de la Etapa 2, y la innovación 4 empieza a liquidar recién desde el mes 24, después
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
55


---

LafroX SpA Introducción al Plan de trabajo
de una línea base y tres liquidaciones en sombra. Así, ninguna innovación agrega trabajo a la
cadena casi crítica de la Etapa 1 después del H4.
7.3.8 Base de planificación y recursos
El Formulario T-15, sección 4, estima las horas de los 222 paquetes con tres valores (optimista,
más probable y pesimista) por clase de tamaño, y separa las curvas mensuales de implemen-
tación, soporte puente de la Etapa 1 y Operación. La cobertura del centro de operaciones, la
mesa de servicio y el SOC sigue las posiciones dimensionadas en el Capítulo 4, Anexo 4-W.7.
Con esa base, el total programado es de 217.543 HH (205.135 HH de paquetes y restauraciones
previas a Operación, 9.336 HH de soporte puente de la Etapa 1 y 3.072 HH de reserva del
frente de construcción y de calidad) y el máximo mensual es de 69 personas equivalentes en
el mes 15, cuando coinciden la marcha blanca de la Etapa 1 y el desarrollo de la Etapa 2. La
sección 5 del mismo formulario conserva la red y el PERT del escenario nominal anterior a
esta reestimación. Esos resultados requieren recálculo con asignaciones nominales, feriados y
esfuerzo vigente antes de confirmar la ruta crítica o las probabilidades; la curva de 69 personas
expresa demanda, no disponibilidad acreditada. Las capacidades protegidas de la Etapa 1 no
se prestan al desarrollo de la Etapa 2.
La gestión del plan sigue el Capítulo 6: la sección 6.1 fija el PMBOK adaptado, el tablero Kanban,
el valor ganado y el control de cambios, y la sección 6.2 fija el proceso RUP iterativo con
DevSecOps. La Construcción avanza en las iteraciones definidas en la sección 6.2, con revisión
semanal de avance y bloqueos y una demostración de incremento verificable al cierre de cada
iteración; una demostración no implica un paso a producción. El Jefe de Proyecto registra la
capacidad y los criterios de terminado antes de seleccionar el trabajo de cada iteración, y los
cambios se aprueban según la sección 6.1.4.
El cronograma rector usa meses contractuales 1 a 56. El Anexo 7.A traduce esos meses a fechas
con un inicio supuesto en febrero de 2027; cuando el CLIENTE confirme la fecha de inicio
(consulta V-12), se recalculan los meses calendario y los congelamientos antes de aprobar cada
corte. La revisión de parámetros de la Innovación 3 (paquete 8.3.2) se ejecuta en los meses 26,
32, 38, 44, 50 y 56.
El Formulario T-18, sección 6, define la cobertura por ola de M9, M12 y M10, propone Talca
como sitio piloto, ordena las olas por sitio, por rutas y por certificación de cadenas, declara la
estabilización de la Etapa 2 y el soporte de la Etapa 1 en los meses 16 a 20, y fija un objetivo
de 40 minutos para el ensayo de reversión. El corte exige un ensayo con volumen real y la
contingencia tributaria; el respaldo manual por sí solo no sustituye ese ensayo para los 96
despachos. El WMS queda en modo de solo lectura conforme al supuesto S-14.
El Anexo 7.F traslada al Capítulo 8 los supuestos, disparadores, responsables y paquetes de la
planificación. La regla de precio es única en la oferta: el precio acordado al capturar el pedido
(Capítulo 2, Anexo 2.2, S-09; RF-03.11 y RF-03.12). La coordinación de reserva y retención
(SD4, apartado 4.1.4.4) está dimensionada en el Anexo 4-I, Tabla A.10, y el Anexo 4-W, Tablas
A.32 y A.33. El máximo de cuatro mensajes por línea incluye una holgura porque la retención
consumida no se libera. La proporción de líneas con más de una retención se mide con AL-
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
56


---

LafroX SpA Introducción al Plan de trabajo
STOCK-01 antes del H4 (R8-02), y la carga y el drenaje se verifican en 3.8.4 y 3.9.3, sin sumar
la coordinación al drenaje tras un corte. El RPO ≤ 15 min se cumple con fibra, LTE y Starlink.
La falla simultánea de los tres caminos seguida de la destrucción del sitio antes de reponer
alguno es el riesgo residual declarado en SD4 4.3.2.4, gestionado en SD8 (LafroX, 2026r) con
R8-05 y verificado con AL-DR-01. Sus medidas son alarmas de retraso a 5 y 15 min, reposición
del enlace, preemisión de guías y NAS WORM. La continuidad crítica y la capacidad nominal
se verifican conforme al Anexo 8.E, con responsable y hito límite.
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
57


---

LafroX SpA Introducción al Plan de trabajo
## Referencias
Las fuentes citadas en este subdocumento se listan en formato APA 7.ª edición. Las Bases se
citan en el texto con su documento y el artículo, capítulo, sección o código del requisito.
• Distribuidora Puelche S.A. (2026a). Bases Administrativas, Licitación TFEP-01/2026.
• Distribuidora Puelche S.A. (2026b). Bases Técnicas Transversales, Licitación TFEP-01/2026.
• Distribuidora Puelche S.A. (2026c). Bases Técnicas del Caso Logística.
• Distribuidora Puelche S.A. (2026d). Aclaraciones de la Licitación TFEP-01/2026.
• LafroX. (2026d). Formulario T-14: Estructura de desglose del trabajo. Propuesta técnica, Licita-
ción TFEP-01/2026.
• LafroX. (2026e). Formulario T-15: Cronograma y asignación de recursos. Propuesta técnica,
Licitación TFEP-01/2026.
• LafroX. (2026j). Subdocumento 3: Anexos. Propuesta técnica, Licitación TFEP-01/2026.
• LafroX. (2026k). Subdocumento 3: Especificación de requerimientos. Propuesta técnica, Licita-
ción TFEP-01/2026.
• LafroX. (2026m). Subdocumento 4: Arquitectura de la solución. Propuesta técnica, Licitación
TFEP-01/2026.
• LafroX. (2026o). Subdocumento 6: Metodología de desarrollo. Propuesta técnica, Licitación
TFEP-01/2026.
• LafroX. (2026r). Subdocumento 8: Plan de riesgos. Propuesta técnica, Licitación TFEP-01/2026.
• LafroX. (2026s). Formulario T-18: Implantación de la solución. Propuesta técnica, Licitación
TFEP-01/2026.
• LafroX. (2026t). Subdocumento 7: Anexos. Propuesta técnica, Licitación TFEP-01/2026.
• Malcolm, D. G., Roseboom, J. H., Clark, C. E., & Fazar, W. (1959). Application of a technique
for research and development program evaluation. Operations Research, 7(5), 646–669.
• Project Management Institute. (2017). Guía de los fundamentos para la dirección de proyectos
(Guía del PMBOK) (6.ª ed.). Project Management Institute.
Declaración de uso de IA
La tabla siguiente prepara la declaración de uso de inteligencia artificial exigida por la sección
7.2 de las Aclaraciones de la licitación. Los niveles consignados deben confirmarse con el
historial real de elaboración. La última columna indica comprobaciones pendientes: el res-
ponsable incorporará su nombre, cargo y resultado una vez que las realice. La versión validada
se consolidará en el Formulario A-6.
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
58


---

LafroX SpA Introducción al Plan de trabajo
Tabla 7.13 Declaración de uso de IA. Fuente: elaboración a partir de registro del equipo.
Sección Herramienta Finalidad del
uso
Nivel en texto Nivel en diagra-
mas
Revisión huma-
na (quién y qué
verificó)
Introducción Claude Code Borrador de
síntesis de las
Bases y los
capítulos de la
oferta
Alto Ninguno [[REVISIÓN
HUMANA]]
7.1 EDT Claude Code;
Codex
Redacción,
conteos y ajus-
te de las figu-
ras de la EDT
Alto Alto [[REVISIÓN
HUMANA]]
7.2 Plan de
trabajo
Claude Code;
Codex
Secuencia-
miento, de-
pendencias
y frentes de
trabajo
Alto Alto [[REVISIÓN
HUMANA]]
7.3 Cronogra-
ma e implanta-
ción
Claude Code;
Codex
Calenda-
rio, Gantt,
CPM/PERT y
esquemas de
implantación
Alto Alto [[REVISIÓN
HUMANA]]
Anexo 7.A Claude Code;
Codex
Conversión de
meses contrac-
tuales a fechas
y congelamien-
tos
Alto Ninguno [[REVISIÓN
HUMANA]]
Anexo 7.B Claude Code;
Codex
Red de de-
pendencias
y revisiones
contractuales
Alto Ninguno [[REVISIÓN
HUMANA]]
Anexo 7.C Claude Code Relación de
resultados de
aceptación
con paquetes e
hitos
Alto Ninguno [[REVISIÓN
HUMANA]]
continúa en la página siguiente
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
59


---

LafroX SpA Introducción al Plan de trabajo
Tabla 7.13 — continuación
Sección Herramienta Finalidad del
uso
Nivel en texto Nivel en diagra-
mas
Revisión huma-
na (quién y qué
verificó)
Anexo 7.D Claude Code;
Codex
Ubicación de
las innovacio-
nes en la EDT
y el calendario
Alto Ninguno [[REVISIÓN
HUMANA]]
Anexo 7.E Claude Code Trazabilidad
de módulos e
interfaces a la
EDT
Alto Ninguno [[REVISIÓN
HUMANA]]
Anexo 7.F Claude Code;
Codex
Supuestos de
planificación y
dependencias
para riesgos
Alto Ninguno [[REVISIÓN
HUMANA]]
Formulario
T-14
Claude Code;
Codex
Diccionario
de la EDT,
ventanas y
cartas Gantt
Alto Alto [[REVISIÓN
HUMANA]]
Formulario
T-15
Claude Code;
Codex
HH, nivela-
ción, activida-
des de 8 a 80
horas, PERT y
frentes
Alto Alto [[REVISIÓN
HUMANA]]
Formulario
T-18
Claude Code;
Codex
Plan de olas,
marcha blanca,
estabilización
y reversión
Alto Alto [[REVISIÓN
HUMANA]]
LafroX SpA
Subdocumento 7
Media firma: Alex Aravena
60


---
