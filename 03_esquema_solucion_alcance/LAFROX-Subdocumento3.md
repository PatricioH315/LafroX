<a id="seccion-1"></a>

# 3 Introducción al Alcance de la Solución

## Índice

- [3.1 Resumen Ejecutivo de la Solución](#seccion-2)
  - [3.1.1 Capacidades de la solución](#seccion-3)
  - [3.1.2 Implementación, implantación y operación](#seccion-4)
- [3.2 Alcance](#seccion-5)
  - [3.2.1 Reparto entre etapas y dependencias](#seccion-6)
  - [3.2.2 Exclusiones, restricciones y supuestos](#seccion-7)
  - [3.2.3 Catálogo de requerimientos y correspondencia](#seccion-8)
  - [3.2.4 Reglas de negocio y discrepancias](#seccion-9)
  - [3.2.5 Criterios de aceptación](#seccion-10)
- [3.3 Esquema de solución](#seccion-11)
  - [3.3.1 Vista conceptual del ciclo logístico](#seccion-12)
  - [3.3.2 Trazabilidad y cadena de frío](#seccion-13)
  - [3.3.3 Continuidad e integración](#seccion-14)
- [3.4 Explicación de la Solución](#seccion-15)
  - [3.4.1 Aplicación en la jornada operacional](#seccion-16)
  - [3.4.2 Correspondencia con la arquitectura lógica](#seccion-17)
  - [3.4.3 Implementación](#seccion-18)
  - [3.4.4 Implantación](#seccion-19)
  - [3.4.5 Operación](#seccion-20)
  - [3.4.6 Participación de los grupos de interés](#seccion-21)
- [Referencias](#seccion-22)
- [Declaración de uso de IA](#seccion-23)


Este subdocumento desarrolla la respuesta de LafroX a las necesidades de Distribuidora Puelche S.A. identificadas en el Subdocumento 2. Utiliza las capacidades y responsabilidades descritas en el Subdocumento 1 como contexto de la propuesta, sin convertir la experiencia corporativa en una elección de tecnología para este proyecto. El alcance se explica desde los procesos de recepción, preparación, preventa, reparto y rendición, y desde los resultados que el CLIENTE exige obtener.

La sección 3.1 presenta la solución y su horizonte; la sección 3.2 delimita capacidades, etapas, restricciones y aceptación; la sección 3.3 representa los procesos mediante esquemas conceptuales; y la sección 3.4 explica su aplicación operacional y la participación de los actores. Los registros detallados se mantienen en **[LAFROX-Subdocumento3-Anexos.md](LAFROX-Subdocumento3-Anexos.md)**, anexos 3.A a 3.K. El archivo independiente **[LAFROX-Formulario-T-12.md](LAFROX-Formulario-T-12.md)** conserva los requisitos y permite distinguir el contenido respaldado de los campos todavía sin respuesta.

Esta versión contrasta las Bases, los subdocumentos 1 y 2 y las arquitecturas lógica y física disponibles del Subdocumento 4. Los compromisos de la oferta se distinguen de las pruebas que deberán ejecutarse durante la implantación y la marcha blanca.

<a id="seccion-2"></a>

## 3.1 Resumen Ejecutivo de la Solución

La propuesta aborda tres necesidades relacionadas: recuperar la trazabilidad sanitaria y comercial, mejorar la confiabilidad de las entregas y conocer el costo de servir. La primera exige capturar lote y temperatura donde se mueve el producto; la segunda necesita pedidos con información comercial y evidencia de entrega; y la tercera depende de que los hechos de cada entrega queden registrados. Es la relación problema–necesidad desarrollada en el Subdocumento 2, secciones 2.1 y 2.2, y en las Bases del caso, capítulos 7 y 9 (Distribuidora Puelche S.A., 2026c).

<a id="seccion-3"></a>

### 3.1.1 Capacidades de la solución

El alcance funcional consolidado comprende preventa desconectada con consulta de stock y crédito, recepción con lote y vencimiento, gestión de bodega con FEFO, preparación por olas, cross-docking, planificación de rutas, control de frío, entrega digital, articulación del acuse tributario con el ERP, conciliación de efectivo y retiro sanitario. El portal de clientes, la integración electrónica del canal moderno y el costo de servir completan el alcance de la segunda etapa (LafroX, 2026b, anexo 2.1).

El ERP se conserva como registro contable y emisor de documentos tributarios. La solución aporta los datos de la operación y debe convivir con los procesos excluidos del contrato. El almacenero no necesita adquirir un dispositivo, disponer de internet ni abandonar el efectivo. Estas condiciones son restricciones del CLIENTE, no opciones de diseño (Distribuidora Puelche S.A., 2026c, cap. 10, restricciones 4 y 5).

El despliegue será híbrido, con carga principal en nube pública y componentes on-premise, conforme al artículo 16 de las Bases Administrativas. El turno móvil sin cobertura y la continuidad del centro ante un corte del enlace forman parte del alcance desde su definición; no se agregan como contingencias al final del desarrollo.

La arquitectura lógica organiza estas capacidades en doce módulos de negocio: recepción, inventario, preventa, planificación de rutas, preparación, reparto, cobranza y rendición, devoluciones y envases, calidad y trazabilidad, analítica, canal moderno y telemetría. La carga principal se ejecuta en nube pública y el borde operacional del CD Talca sostiene recepción, preparación y despacho durante la pérdida de enlace. Esta distribución cumple el modelo híbrido sin trasladar al Subdocumento 3 el detalle de servicios, red o dimensionamiento del Subdocumento 4.

<a id="seccion-4"></a>

### 3.1.2 Implementación, implantación y operación

La Tabla [3.1](#tabla-3-1) sitúa el alcance en los meses relativos del contrato. Se conserva el calendario obligatorio sin asignar una fecha de inicio que no está consolidada.

<a id="tabla-3-1"></a>

**Tabla 3.1 — Marco contractual de las etapas. Fuente: Bases Administrativas, art. 17, pp. 12–13.**

| **Etapa** | **Desarrollo** | **Marcha blanca** | **Producción / operación** |
| --- | --- | --- | --- |
| Etapa 1 | Meses 1–12 | Meses 13–15 | Producción: mes 16. |
| Etapa 2 | Meses 13–18 | Meses 19–20 | Producción: mes 21. |
| Operación |  |  | Meses 21–56: 36 meses. |

La superposición entre desarrollo y marcha blanca obliga a considerar simultáneamente construcción y estabilización. La tabla fija los hitos, pero no acredita que exista una dotación o secuencia detallada capaz de cumplirlos. Los congelamientos de septiembre, diciembre y cierre mensual deben verificarse cuando se conozca la fecha efectiva de inicio (Distribuidora Puelche S.A., 2026a, art. 17; 2026c, secciones 13.2 y 13.3).

La fecha calendario se determinará al formalizar el inicio contractual. Mientras tanto, el plan se gobierna por meses relativos: durante los meses 16 a 20 el equipo mantiene estabilización de la Etapa 1 mientras construye y prepara la Etapa 2, sin desplazar los hitos obligatorios.

<a id="seccion-5"></a>

## 3.2 Alcance

El alcance se organiza por capacidades que responden a necesidades del CLIENTE. El catálogo resumido del Subdocumento 2 orienta el reparto funcional; las Bases fijan los límites y resultados mínimos. Los registros existentes del Subdocumento 3 se conservan como insumo de contraste, sin tratar sus decisiones adicionales como acuerdos aprobados.

<a id="seccion-6"></a>

### 3.2.1 Reparto entre etapas y dependencias

La Tabla [3.2](#tabla-3-2) resume la asignación ya expresada en el anexo 2.1. Agrupa requerimientos por proceso; no altera sus identificadores ni introduce una división arquitectónica.

<a id="tabla-3-2"></a>

**Tabla 3.2 — Alcance funcional por etapa. Fuente: LafroX (2026b), anexo 2.1.**

| **Capacidad** | **RF resumidos del SD2** | **Etapa** | **Dependencia principal** |
| --- | --- | --- | --- |
| Preventa, recepción y bodega | RF-01 a RF-05 | 1 | Datos comerciales, lotes e inventario. |
| Rutas, frío y entrega | RF-06 a RF-09 | 1 | Pedidos y movimientos registrados. |
| Efectivo y retiro sanitario | RF-10 y RF-11 | 1 | Entregas, cobros y lotes. |
| Portal e intercambio electrónico | RF-12 y RF-13 | 2 | Datos de pedidos y entregas disponibles. |
| Costo de servir | RF-14 | 2 | Hechos operacionales por entrega. |

La captura precede a la explotación de los datos. Sin registrar el lote en recepción, el retiro sanitario no puede reconstruir sus destinos. Sin vincular pedido, entrega y cobro, la conciliación conserva las discontinuidades actuales. La analítica necesita esos hechos antes de producir un costo individual confiable. Por ello, la Etapa 1 concentra captura y continuidad; la Etapa 2 utiliza esa base para nuevos canales y análisis.

La planificación de rutas permanece en la Etapa 1, tal como está consolidada en el RF-06 del Subdocumento 2. Su urgencia no se limita al ahorro: el caso advierte que el conocimiento operativo reside en una persona próxima a jubilarse. El supuesto consolidado prevé talleres en los meses 1 a 3 y cooperación durante los primeros cuatro meses (LafroX, 2026b, sección 2.5; Distribuidora Puelche S.A., 2026c, sección 13.1). El módulo de analítica entrega en la Etapa 1 la medición diaria de OTIF y los controles de operación; el costo de servir por cliente y entrega se habilita en la Etapa 2, cuando existe una base de hechos de entrega suficientemente completa.

La asignación detallada de cada RF y RNF se mantiene en el Anexo 3.A, Anexo 3.B y Formulario T-12. Las innovaciones se desarrollan en el Subdocumento 13; desde este alcance solo se consideran sus ideas centrales cuando refuercen trazabilidad, continuidad, eficiencia de proceso, sostenibilidad o experiencia de los actores, sin anticipar su evaluación económica.

<a id="seccion-7"></a>

### 3.2.2 Exclusiones, restricciones y supuestos

Las exclusiones del capítulo 11 del caso se conservan en el Anexo 3.D: sustitución del ERP, remuneraciones, punto de venta del cliente, comercio al consumidor final, administración contractual de transportistas, rediseño de la red logística, robotización, mantenimiento mecánico y adquisición del hardware de terreno. En este último punto, el CLIENTE compra y LafroX especifica cantidades y características. Integrar a los transportistas operacionalmente no supone gestionar sus contratos o pagos.

Las restricciones del Anexo 3.E mantienen el despacho de 05:30 a 07:00, la continuidad ante pérdida de enlace, el turno móvil sin señal, la captura en cámara a -22 °C, el canal tradicional, la incorporación de terceros y las ventanas de congelamiento. Estas condiciones impiden diseñar una solución que dependa de conexión permanente o que transfiera nuevas funciones especializadas al equipo de cuatro personas del CLIENTE (Distribuidora Puelche S.A., 2026c, cap. 10).

El reemplazo modular progresivo del WMS es una decisión de alcance ya declarada en el inventario de sistemas legados del Subdocumento 2. La arquitectura lo materializa en inventario y preparación, preservando al ERP como fuente contable y tributaria. La integración se realiza mediante contratos de servicio y mensajería; la disponibilidad y calidad de las interfaces heredadas se valida al inicio para definir la migración y la reconciliación (LafroX, 2026b, sección 2.5 y anexo 2.3).

El Anexo 3.C y las reglas de negocio documentan las decisiones operacionales propuestas: reserva al confirmar el pedido, precio vigente al despacho con excepciones configurables, reagendamiento frente a local cerrado, control de envases por saldo, devolución registrada en terreno y conciliación determinista al reconectar. La excursión térmica se registra y bloquea preventivamente el lote; Calidad autoriza su liberación o disposición, conservando la evidencia de la decisión.

<a id="seccion-8"></a>

### 3.2.3 Catálogo de requerimientos y correspondencia

El Anexo 3.A conserva los 174 identificadores RF del catálogo previo. De ellos, 31 tienen un desarrollo contrastado en esta revisión; los restantes conservan su materia, con descripción y compromiso vacíos. El Anexo 3.B conserva 90 identificadores RNF: 13 tienen un umbral respaldado y los demás requieren contraste. Estos conteos describen el estado del trabajo, no el número de requisitos aceptados por el CLIENTE.

La correspondencia del Anexo 3.A relaciona los RF-01 a RF-14 resumidos del Subdocumento 2 con identificadores detallados del Subdocumento 3. Un número coincidente no implica equivalencia: RF-01 en el documento 2 es preventa, mientras la familia RF-01.xx del documento 3 trata recepción. Se conservan ambas nomenclaturas indicando siempre su documento de origen.

Las prioridades Crítica, Alta y Media se mantienen donde provienen del catálogo consolidado o donde un resultado expreso del caso respalda la clasificación. Una prioridad Alta no implica que el requisito pueda omitirse. Los campos todavía vacíos evitan simular una priorización completa. El T-12 mantiene separadas la existencia del requisito y la demostración de su cumplimiento.

La traza hacia la arquitectura se desarrolla en la Sección 3.4. La EDT, los casos de prueba y sus responsables se definirán en los documentos de planificación y calidad; en el T-12 se registra la verificación prevista, sin declararla ejecutada antes de la marcha blanca.

<a id="seccion-9"></a>

### 3.2.4 Reglas de negocio y discrepancias

Consultar stock y crédito, preparar con FEFO y registrar el efectivo son capacidades respaldadas. Las reglas del Anexo 3.G completan su uso operacional: el stock se reserva al confirmar, la excepción de crédito queda registrada, el local cerrado se reagenda, las devoluciones afectan el ERP mediante el proceso tributario correspondiente y los envases se controlan por saldo del cliente. La regla de excursión térmica deja la detección y el bloqueo preventivo al sistema, y la disposición final a Calidad; así se preserva continuidad sin delegar una decisión sanitaria al conductor (Distribuidora Puelche S.A., 2026c, secciones 16.1 y 17.1).

El Anexo 3.H registra las discrepancias que deben cerrarse antes del diseño detallado. Entre ellas se encuentran los «14 CD» mencionados en el Subdocumento 2, las referencias cruzadas de códigos RT, las marcas de sistemas legados y la atribución de la rotación del 38% a conductores externos. El caso atribuye esta rotación a preparación de pedidos; esta versión no la utiliza para dimensionar conductores (Distribuidora Puelche S.A., 2026c, cap. 10, restricción 11).

**Nota de trabajo:** Los documentos 1 y 2 no se modifican en esta consolidación. Para completar la consistencia se requiere revisar las discrepancias registradas con el equipo y contrastar el universo de instalaciones con las Bases, que contienen a su vez una diferencia entre cinco y seis instalaciones.

<a id="seccion-10"></a>

### 3.2.5 Criterios de aceptación

El Anexo 3.J conserva los dieciséis resultados del capítulo 18 del caso. Entre los límites expresos están obtener la lista de clientes afectados por lote en menos de dos horas, registrar lote en el 100% de las recepciones que lo requieren, mantener registro térmico continuo, no perder ni duplicar pedidos por falta de señal y generar la ruta siguiente en menos de veinte minutos (Distribuidora Puelche S.A., 2026c, cap. 18, p. 35).

La Tabla [3.3](#tabla-3-3) relaciona tres problemas con resultados verificables. Distingue los límites fijados por el CLIENTE de las metas cuya definición corresponde al proponente.

<a id="tabla-3-3"></a>

**Tabla 3.3 — Síntesis de resultados de aceptación. Fuente: Bases del caso, cap. 18.**

| **Problema** | **Resultado exigido** | **Límite expreso** | **Registro** |
| --- | --- | --- | --- |
| Trazabilidad sanitaria | Clientes afectados por lote con evidencia. | Menos de 2 horas. | R18-01 |
| Confiabilidad del servicio | Pedidos sin pérdida ni duplicación por falta de señal. | Ninguno perdido o duplicado. | R18-06 |
| Costo desconocido | Costo por cliente y entrega desde los hechos. | Sin meta numérica propia fijada. | R18-11 |

La aceptación del alcance requiere demostrar resultados, no solo disponibilidad de pantallas. Obtener un reporte de lotes sin evidencia no satisface R18-01; registrar pedidos sin comprobar la reconciliación no acredita R18-06. Los protocolos y sus datos de prueba todavía deben documentarse.

El Anexo 3.J define para cada resultado el momento de verificación, datos, evidencia y responsable de aceptación. Las metas propias de OTIF, envases y ocupación se someterán a la línea base medida durante el levantamiento inicial; esta secuencia evita usar una estimación histórica como si fuera una medición comparable.

<a id="seccion-11"></a>

## 3.3 Esquema de solución

Los siguientes esquemas representan procesos y circulación de información. Sus bloques son capacidades de negocio, no módulos desplegados ni capas de una arquitectura. Cada figura utiliza únicamente las relaciones necesarias para explicar el alcance consolidado.

<a id="seccion-12"></a>

### 3.3.1 Vista conceptual del ciclo logístico

La Figura [3.1](#figura-3-1) conecta la captura comercial con la ejecución y el cierre. La recepción alimenta el inventario disponible para preparar; el pedido orienta la preparación y la ruta; y la entrega genera evidencia para rendición y análisis.

<a id="figura-3-1"></a>

**Figura 3.1 — Relación conceptual de capacidades. Fuente: elaboración propia a partir de SD2, anexo 2.1.**

Transcripción textual de la figura original.

Elementos:

- Preventa<br>Stock y crédito.
- Recepción y bodega<br>Lote, vencimiento y FEFO.
- Pedido y planificación<br>Ruta corregible.
- Preparación y carga<br>Olas y faltantes.
- Entrega digital<br>Evidencia y cobro.
- Rendición y análisis<br>Conciliación y costo.

Relaciones:

- Preventa<br>Stock y crédito → Pedido y planificación<br>Ruta corregible.
- Recepción y bodega<br>Lote, vencimiento y FEFO → Preparación y carga<br>Olas y faltantes.
- Pedido y planificación<br>Ruta corregible → Preparación y carga<br>Olas y faltantes.
- Preparación y carga<br>Olas y faltantes → Entrega digital<br>Evidencia y cobro.
- Entrega digital<br>Evidencia y cobro → Rendición y análisis<br>Conciliación y costo.

La figura muestra por qué la analítica depende de la captura en terreno: el costo de servir necesita hechos de entrega, no solamente totales contables. También distingue el pedido de la ejecución física, evitando que una confirmación comercial se interprete como una entrega realizada.

<a id="seccion-13"></a>

### 3.3.2 Trazabilidad y cadena de frío

La Figura [3.2](#figura-3-2) representa la continuidad del lote y del registro térmico. Su propósito es conservar el vínculo entre recepción, movimiento y destino para responder a un retiro sanitario.

<a id="figura-3-2"></a>

**Figura 3.2 — Información necesaria para trazabilidad sanitaria. Fuente: elaboración propia a partir de las Bases del caso, cap. 18, criterios 1–3.**

Transcripción textual de la figura original.

Elementos:

- Recepción<br>Lote y vencimiento.
- Bodega y preparación<br>Movimientos del lote.
- Consulta sanitaria<br>Origen y clientes afectados.
- Transporte y entrega<br>Destino y evidencia.
- Registro continuo de temperatura en cámaras y vehículos.

Relaciones:

- Recepción<br>Lote y vencimiento → Bodega y preparación<br>Movimientos del lote.
- Bodega y preparación<br>Movimientos del lote → Transporte y entrega<br>Destino y evidencia.
- Transporte y entrega<br>Destino y evidencia → Consulta sanitaria<br>Origen y clientes afectados.
- Recepción<br>Lote y vencimiento → Consulta sanitaria<br>Origen y clientes afectados.
- Registro continuo de temperatura en cámaras y vehículos → Transporte y entrega<br>Destino y evidencia.
- Registro continuo de temperatura en cámaras y vehículos → Consulta sanitaria<br>Origen y clientes afectados.

La consulta necesita relacionar movimientos y clientes; las lecturas térmicas aportan la evidencia del manejo del producto. Ante una excursión, el sistema retiene preventivamente el lote y notifica a Calidad, que registra la liberación, sustitución o disposición con su fundamento.

<a id="seccion-14"></a>

### 3.3.3 Continuidad e integración

La Figura [3.3](#figura-3-3) distingue los ámbitos cuya operación debe sostenerse ante pérdida de conectividad y su relación con la nube. El ERP conserva su responsabilidad contable y tributaria, sin asignarle un emplazamiento no verificado.

<a id="figura-3-3"></a>

**Figura 3.3 — Ámbitos de continuidad e intercambio, sin topología física. Fuente: elaboración propia; BA, art. 16; caso, cap. 10 y 15.**

Transcripción textual de la figura original.

Elementos:

- Preventa y reparto<br>Turno sin señal: 14 horas.
- Carga principal en nube<br>Intercambio de información.
- Centro de distribución<br>Autonomía: al menos 24 horas.
- ERP conservado<br>Registro contable y emisión.

Relaciones:

- Preventa y reparto<br>Turno sin señal: 14 horas ↔ Carga principal en nube<br>Intercambio de información; enlace discontinuo; reconexión.
- Centro de distribución<br>Autonomía: al menos 24 horas ↔ Carga principal en nube<br>Intercambio de información; enlace discontinuo.
- Carga principal en nube<br>Intercambio de información ↔ ERP conservado<br>Registro contable y emisión.

La autonomía evita que un corte detenga la captura; la sincronización posterior debe reconciliar los registros sin perder ni duplicar pedidos. El caso exige que el dispositivo sincronice tras el turno en no más de diez minutos y el centro tras un corte de 24 horas en no más de dos horas. Se usa el código RT-03.12 de las Bases Transversales para la materia de sincronización, dejando registrado el desajuste con el código citado en el caso (Distribuidora Puelche S.A., 2026b, RT-03.12; 2026c, cap. 15).

La plataforma conserva una cola local e idempotente de transacciones, por lo que la reconexión reconcilia cada registro con identificador único y deja una bitácora de conflictos. La reserva firme ocurre en el servicio central al confirmar; la consulta offline muestra la antigüedad del dato y no promete stock antes de esa confirmación. El detalle de protocolos y componentes se especifica en el Subdocumento 4.

<a id="seccion-15"></a>

## 3.4 Explicación de la Solución

La solución se interpreta a través de la jornada de Puelche y de los actores identificados en el Subdocumento 2. Su valor depende de que la información se capture donde ocurre la operación y pueda seguirse hasta los resultados del CLIENTE.

<a id="seccion-16"></a>

### 3.4.1 Aplicación en la jornada operacional

En recepción se captura lote y vencimiento antes de perder el vínculo con el producto. Bodega utiliza esa información para FEFO y preparación por olas; los faltantes registran su causa cuando se producen. La preparación nocturna y el despacho concentrado exigen que la captura local continúe durante un corte del enlace (Distribuidora Puelche S.A., 2026c, cap. 10 y 18; LafroX, 2026b, RF-02 a RF-05).

En la calle, el preventista consulta stock y crédito al registrar el pedido. El conductor registra la entrega y el efectivo con o sin señal. Al recuperar conectividad, los registros deben integrarse sin duplicación. El almacenero conserva su forma de compra y pago; la aplicación no presupone que tenga un teléfono o una conexión propia.

Al cerrar la operación, la rendición vincula cobros con entregas y explica las diferencias. Calidad puede reconstruir los destinos de un lote. En la segunda etapa, la información registrada permite desarrollar el costo de servir y alimentar los nuevos canales. La promesa comercial, los reintentos y el efecto tributario de una devolución requieren reglas explícitas antes de transformarse en automatismos.

<a id="seccion-17"></a>

### 3.4.2 Correspondencia con la arquitectura lógica

Este apartado vincula capacidades y módulos de negocio sin repetir las capas técnicas ni el inventario de servicios de la arquitectura.

<a id="tabla-3-4"></a>

**Tabla 3.4 — Correspondencia entre capacidades del alcance y módulos lógicos. Fuente: Arquitectura Lógica v6-2.**

| **Capacidad** | **Módulo** | **Resultado que habilita** | **Etapa** |
| --- | --- | --- | --- |
| Recepción, lote y vencimiento | M1 Recepción | Trazabilidad de ingreso y calidad de datos. | 1 |
| Inventario, FEFO y preparación | M2 Inventario; M5 Preparación | Stock confiable y despacho controlado. | 1 |
| Preventa y ruteo | M3 Preventa; M4 Rutas | Pedido confirmable y ruta corregible. | 1 |
| Entrega, cobro y retorno | M6 Reparto; M7 Rendición; M8 Devoluciones | POD, conciliación y control de envases. | 1 |
| Calidad, evidencia y flota | M9 Calidad; M12 Telemetría | Retiro sanitario y control de cadena de frío. | 1 |
| Gestión y nuevos canales | M10 Analítica; M11 Canal moderno | OTIF diario, costo de servir e intercambio estructurado. | 1 / 2 |

La tabla permite verificar que cada flujo de la Sección 3.3 tiene una responsabilidad lógica. M10 entrega los indicadores operacionales de la Etapa 1 y profundiza el costo de servir en la Etapa 2; M11 se incorpora con el canal moderno en la segunda etapa.

<a id="seccion-18"></a>

### 3.4.3 Implementación

La implementación construye primero una base compartida de identidad, integración, registro auditable, operación desconectada y observabilidad. Sobre ella se organizan tres frentes: bodega y calidad; preventa, rutas y reparto; y datos, rendición y canales. Cada incremento integra requisitos, configuración versionada, pruebas automatizadas y pruebas operacionales por perfil antes de promoverse entre ambientes. La Etapa 2 reutiliza esa base para canal moderno y costo de servir, sin alterar las funciones estabilizadas de la Etapa 1 durante la ventana de despacho.

<a id="seccion-19"></a>

### 3.4.4 Implantación

La implantación debe convivir con la forma actual de trabajar durante la marcha blanca, conciliar ambos registros y permitir volver atrás. Debe poder desplegarse por proceso, sitio o zona, considerar el turno nocturno y capacitar en terreno sin detener venta ni reparto. La incorporación de cada transportista requiere un acuerdo operacional propio (Distribuidora Puelche S.A., 2026c, sección 13.3, p. 23).

Estas condiciones impiden asumir que basta con instalar la aplicación. Bodega necesita acompañamiento en su horario real, y los conductores externos requieren un mecanismo de incorporación que sobreviva a la rotación. No se asigna una cantidad de acompañantes a partir de superficie de bodega ni se confunde número de camiones con personas.

La implantación comienza por datos maestros y trazabilidad de recepción, continúa por bodega y preparación, y culmina con preventa, reparto y rendición por zonas operacionales. Cada ola realiza carga, conciliación, capacitación por perfil y marcha blanca con volumen representativo. Un avance requiere ausencia de defectos críticos o altos, conciliación sin diferencias no explicadas, indicadores sostenidos, certificación de usuarios y acta de aceptación. La reversión la autoriza el responsable operativo del CLIENTE cuando un umbral acordado amenaza el despacho; los registros capturados permanecen en cola para su conciliación posterior.

<a id="seccion-20"></a>

### 3.4.5 Operación

La operación cubre los 36 meses contractuales y complementa al equipo de cuatro personas del CLIENTE con monitoreo, gestión de incidentes, continuidad, seguridad, datos y evolución controlada. Atiende de 04:00 a 22:00 de lunes a sábado, amplía a 24 por 7 en septiembre y diciembre y mantiene respuesta ante incidentes críticos durante la ventana de despacho. La atención incluye canal asistido para clientes tradicionales; la autoatención no se impone como condición para recibir soporte.

La continuidad debe verificarse mediante recuperación y sincronización, con RTO máximo de cuatro horas y RPO máximo de quince minutos para servicios críticos, y pruebas de recuperación al menos dos veces al año (Distribuidora Puelche S.A., 2026b, RT-07.04 y RT-07.07). El diseño de medición y la evidencia aún deben completarse.

Los servicios críticos de pedido, bodega, entrega, trazabilidad y rendición se supervisan con indicadores de disponibilidad, latencia, colas pendientes, sincronización y calidad de datos. Los procedimientos de escalamiento distinguen la mesa de servicio, especialistas de aplicación, infraestructura y decisión operacional del CLIENTE. La capacidad de la mesa se recalibrará con tickets observados durante la marcha blanca; este documento no declara un cálculo de demanda ya ejecutado.

<a id="seccion-21"></a>

### 3.4.6 Participación de los grupos de interés

Se mantienen los 19 actores nominales del anexo 2.3, sin reducirlos a un supuesto catálogo de dieciséis grupos. El Anexo 3.I los enumera individualmente y vincula cada uno con la participación ya sustentada en el documento 2.

La dirección y el comité ejecutivo revisan resultados y arbitran prioridades; operaciones y calidad resuelven las tensiones entre continuidad y tratamiento sanitario; el planificador transfiere conocimiento y corrige rutas; y bodega, preventistas, conductores y peonetas validan los flujos en sus condiciones reales de trabajo. El sindicato participa antes de activar telemetría que afecte al trabajo de terreno. Clientes, proveedores y autoridad reciben evidencias e intercambios acordes a su función, sin trasladarles obligaciones tecnológicas ajenas al caso (LafroX, 2026b, sección 2.4 y anexo 2.3).

El Anexo 3.I convierte esta participación en actividades verificables: levantamiento y validación de reglas durante el inicio, capacitación y certificación antes de cada ola, acompañamiento en marcha blanca y seguimiento de adopción durante operación. Cada actividad identifica responsable, momento, indicador y respuesta ante resistencia; no supone que exista aprobación previa de un actor.

<a id="seccion-22"></a>

## Referencias

Las fuentes utilizadas son las Bases y los dos subdocumentos consolidados. Las citas internas indican sección o registro para distinguir decisiones del equipo y exigencias del CLIENTE.

- Distribuidora Puelche S.A. (2026a). *Bases Administrativas de Licitación N.º TFEP-01/2026*.
- Distribuidora Puelche S.A. (2026b). *Bases Técnicas Transversales de Licitación N.º TFEP-01/2026*.
- Distribuidora Puelche S.A. (2026c). *Caso 02: Logística*.
- LafroX. (2026a). *Subdocumento 1: Presentación de la empresa*.
- LafroX. (2026b). *Subdocumento 2: Comprensión del problema y de la necesidad y anexos*.
- LafroX. (2026c). *Arquitectura lógica v6-2 y arquitectura física de la solución*.

Las referencias internas se localizan por artículo, capítulo, código o sección de la fuente. La paginación de los PDF se incorporará en la revisión formal de citas.

<a id="seccion-23"></a>

## Declaración de uso de IA

Se declara la intervención de Codex en esta consolidación. El nivel indicado corresponde a esta revisión, no sustituye el historial anterior. No se atribuye al equipo una revisión humana que no consta realizada.

La Tabla [3.5](#tabla-3-5) registra la asistencia utilizada en esta revisión.

<a id="tabla-3-5"></a>

**Tabla 3.5 — Declaración de uso de IA. Fuente: registro de esta revisión.**

| **Sección** | **Herramienta** | **Finalidad** | **Nivel texto** | **Nivel diagramas** | **Revisión humana** |
| --- | --- | --- | --- | --- | --- |
| 3.1 | Codex | Contraste y edición. | Alto | Ninguno | No documentada. |
| 3.2 | Codex | Contraste y edición. | Alto | Ninguno | No documentada. |
| 3.3 | Codex | Contraste y edición. | Alto | Alto | No documentada. |
| 3.4 | Codex | Contraste y edición. | Alto | Ninguno | No documentada. |
| 3.A | Codex | Contraste y edición. | Alto | Ninguno | No documentada. |
| 3.B | Codex | Contraste y edición. | Alto | Ninguno | No documentada. |
| 3.C | Codex | Contraste y edición. | Alto | Ninguno | No documentada. |
| 3.D | Codex | Contraste y edición. | Alto | Ninguno | No documentada. |
| 3.E | Codex | Contraste y edición. | Alto | Ninguno | No documentada. |
| 3.F | Codex | Contraste y edición. | Alto | Ninguno | No documentada. |
| 3.G | Codex | Contraste y edición. | Alto | Ninguno | No documentada. |
| 3.H | Codex | Contraste y edición. | Alto | Ninguno | No documentada. |
| 3.I | Codex | Contraste y edición. | Alto | Ninguno | No documentada. |
| 3.J | Codex | Contraste y edición. | Alto | Ninguno | No documentada. |
| 3.K | Codex | Contraste y edición. | Alto | Ninguno | No documentada. |
| T-12 | Codex | Contraste y edición. | Alto | Ninguno | No documentada. |

**Nota de trabajo:** Falta registrar quién revisó y qué verificó. Para completarlo se requiere revisión humana efectiva del contenido y su consolidación en el Formulario A-6.


> Nota de conversión: se conserva el contenido vigente, incluidos títulos, errores, notas de trabajo, campos vacíos y diferencias entre versiones. Las figuras están transcritas a texto. Las menciones de arquitectura y otros subdocumentos son referencias del original, no evidencia incorporada o verificada en esta conversión.
