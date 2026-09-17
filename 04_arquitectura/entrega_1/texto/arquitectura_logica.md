# Capítulo 4 · Arquitectura Lógica de la Solución (Parte 4.1)


## 4.1  Visión General de la Arquitectura

La arquitectura lógica de la solución para la Distribuidora Puelche S.A. se organiza en un modelo de ocho capas de existencia obligatoria, conforme al numeral 2.1 de las Bases Técnicas Transversales (RT-02.01).

Los principios que gobiernan el diseño son los siguientes:

Operación sin conexión como requisito de primera clase: Preventa, reparto y bodega operan sin señal de red durante extensiones de hasta 14 horas en terreno y 24 horas en centro de distribución (RT-03.10). La sincronización es diferida, idempotente y con resolución determinista de conflictos por regla de negocio, nunca por marca de tiempo ciega.

El cliente del canal tradicional no cambia su forma de operar: Los 11.600 almacenes del canal tradicional no disponen de internet ni dispositivo; la solución se adapta a ellos mediante aviso por WhatsApp/SMS y confirmación con firma/QR del conductor, sin exigir instalación de aplicación alguna.

Despliegue híbrido obligatorio (Art. 16):  El núcleo transaccional se ejecuta por centro de distribución con autonomía local, y la analítica, integración y almacenamiento consolidado se trasladan a nube pública AWS. No se admiten propuestas exclusivamente en nube ni exclusivamente en on-premise.

Cronograma de 56 meses innegociable (Art. 17): La arquitectura contempla Etapa 1 (meses 1–15, producción mes 16) y Etapa 2 (meses 13–20, producción mes 21), con 36 meses de operación.

Zero Trust y multi-zona (NIST SP 800-207):  Identidad central en OIDC/MFA, microsegmentación con mTLS, infraestructura como código y sin confianza implícita en la red interna.

Cinco ambientes obligatorios incluyendo Recuperación ante Desastres (RT-04.01): El quinto ambiente es DRP en la región us-east-1 de AWS, con prueba semestral (Art. 20 / RT-07.07).

Equipo TI pequeño (4 personas): Todo componente debe ser administrable por el equipo de Puelche o por soporte del adjudicatario durante los 56 meses de contrato.

La arquitectura se describe conforme al marco TOGAF declarado, con descripción conforme a ISO/IEC/IEEE 42010. Las seis vistas exigidas están completas: lógica (este documento), de procesos, de datos, de seguridad, de integración y de despliegue/física. Las decisiones de diseño se registran como ADR fechados y fundados, conforme a RT-02.04.

La solución se apoya en un monolito modular Django (Python 3.12) que encapsula los 12 módulos de negocio, desplegado en Amazon ECS Fargate en nube y Docker/Docker Compose sobre el clúster Proxmox en los centros de distribución on-premise. Esta elección responde a una decisión de diseño explícita: un equipo de 4 personas, 14.200 clientes y aproximadamente 31.000 pedidos mensuales no justifican la complejidad operativa de microservicios, conforme a la recomendación del numeral 2.3 de las Bases Técnicas Transversales. La modularidad del monolito permite extraer componentes críticos (sincronización offline, EDI, telemetría) como workers independientes si el volumen lo exige, preservando la capacidad de escalado modular sin rediseño arquitectónico (RT-02.02).

La volumetría operativa que condiciona el dimensionamiento es la siguiente: 14.200 clientes activos, 8.400 SKU (que pasan a aproximadamente 9.500), 31.000 pedidos mensuales con 260.000 líneas y 2,4 millones de unidades, aproximadamente 1.400 entregas diarias habituales con peak de septiembre de 2.600 entregas (volumen casi duplicado durante tres semanas), 96 camiones en la ventana crítica de despacho (42 propios y 54 de transportistas externos), 62 preventistas, aproximadamente 200 conductores, 120 preparadores nocturnos y 310 personas de centro de distribución. El diseño se dimensiona contra el pico de septiembre en la ventana de 05:30 a 07:00, nunca contra el promedio, y declara explícitamente los puntos únicos de falla (SPOF) con su mitigación conforme a RT-02.11.


## 4.2  Capas de la Arquitectura

La solución se organiza en ocho capas conformes al numeral 2.1 de las Bases Técnicas Transversales. Cada capa tiene un rol preciso e interfaces definidas con las capas adyacentes. A continuación se describe cada una de ellas.


### 4.2.1  Capa de Presentación

La capa de presentación constituye la superficie de interacción de los 11 actores canónicos definidos en la arquitectura. Incluye dos tipos fundamentales de interfaces: las aplicaciones móviles de campo, diseñadas bajo el principio de offline-first, y los portales y consolas web, implementados como aplicaciones de página única (SPA) servidas desde la nube.

Las aplicaciones de campo (preventa y reparto) se construyen en Kotlin nativo para Android, decisión alineada con el ecosistema del parque de dispositivos Zebra (EC55, TC58e, MC9400) desplegado en los centros de distribución y con las condiciones de operación del terreno. La app de preventa mantiene una foto local de datos de lectura (stock, precios, crédito, promociones) y captura local de eventos (pedidos, identificadores únicos UUID); la app de reparto gestiona la entrega, la prueba de entrega digital (POD con firma, código QR y fotografía), la cobranza en ruta y el control de envases retornables. Ambas aplicaciones operan con datos locales cifrados y sincronizan de forma idempotente por medio del API Gateway cuando se recupera la conectividad.

Los terminales de bodega (HHT con escáner GS1) operan en condiciones extremas de temperatura (cámara de congelado a -22 °C sin señal) y descargan las misiones de picking al inicio del turno nocturno para una autonomía local de 24 horas.

Los portales web (Angular con Tailwind CSS) cubren las necesidades de los actores de back-office: portal de clientes (consulta de estado, documentos tributarios, autoservicio), portal de transportistas (rutas asignadas, documentación), portal de proveedores (órdenes de compra, recepciones), portal público (catálogo consultable sin autenticación) y portal de administración TI. Estos portales se accesan por intranet o VPN, con autenticación OIDC (Keycloak) y se sirven desde la nube por medio de la tarea `web` en ECS Fargate.

Las consolas de planificación de rutas, calidad, BI/gerencia y administración TI conforman el back-office web, cada una conectada a su base de datos correspondiente y accesible únicamente desde la red interna.


### 4.2.2  Capa de Borde y Exposición (Capa 2)

La capa de borde constituye el único punto de entrada público de la plataforma y, en el contexto de Puelche, también es el borde de terreno y bodega donde la conectividad es intermitente. Sus componentes principales son:

CDN (Amazon CloudFront): distribución de contenido estático de portales y catálogo público.

WAF gestionado (AWS WAF + Shield): filtrado de tráfico con reglas OWASP Top 10 y reglas personalizadas por API; protección contra denegación de servicio en capas 3, 4 y 7.

Balanceador de carga (ALB): terminación de TLS 1.3 y balanceo hacia el API Gateway en nube.

Ingreso on-premise por centro de distribución: firewall/UTM con IPS (D-01) como único punto de entrada local, en configuración activo-pasivo de alta disponibilidad.

AWS IoT Greengrass: borde IoT en terreno y almacenes para la recolección de datos de sensores de frío y telemetría de camiones, con buffer de reenvío y persistencia local durante cortes de conectividad.


### 4.2.3  Capa de Puerta de Enlace de Servicios (Capa 3)

La puerta de enlace de servicios se materializa en Amazon API Gateway, decisión fundamentada en la D8 (2026-09-05): es un servicio administrado que elimina la necesidad de operar nodos adicionales, se integra nativamente con WAF, Shield y ALB, y soporta autenticación OIDC con Keycloak, validación de esquema OpenAPI, limitación de tasa por cliente y endpoint, cuotas por tipo de tráfico, versionado de contratos y trazabilidad por transacción mediante la propagación de un identificador `transaction_id`.

La capa publica dos conjuntos de APIs: las de negocio (`/v1`) y las de sincronización offline (`/sync/v1`), estas últimas con escrituras idempotentes por UUID. La sincronización de dispositivos de preventa, reparto y misiones de picking constituye tráfico de API de primera clase que ingresa por el Gateway, valida esquema y aplica deduplicación en el servidor (RT-02.06).


### 4.2.4  Capa de Lógica de Negocio (Capa 4)

La capa de servicios de negocio encapsula los 12 módulos funcionales de la solución (M1–M12), implementados como un monolito modular Django con cada módulo separado por apps y contextos. Los módulos son stateless (RT-02.05): el estado de proceso reside en las bases de datos y colas de la capa de datos y de integración, nunca en memoria del proceso.

Los componentes críticos se empaquetan y escalan por separado como workers o procesos desacoplados: sincronización offline, EDI (AS2) y telemetría. Esta modularidad permite extraer estos workers del monolito si el volumen lo requiere, preservando la capacidad de escalado independiente de los servicios críticos (RT-02.02).

El escalado horizontal se ejecuta en nube mediante ECS Fargate con autoscaling por umbrales de CPU, rutas y colas, con límites superiores y costo declarados en la oferta. En on-premise, los contenedores se escalan por sitio con réplicas sobre el clúster Proxmox.


### 4.2.5  Capa de Integración y Eventos (Capa 5)

La capa de integración es de primera clase en la arquitectura, distinción relevante por cuanto el caso Puelche se resuelve principalmente en las integraciones: un ERP implantado en 2017 sin documentación de interfaces, un WMS de 2013, integración EDI con cadenas de retail desde enero 2029, facturación electrónica ante el SII, GPS/telemetría de flota y sensores de frío.

La mensajería asíncrona se distribuye entre RabbitMQ en cada sitio on-premise (integraciones locales: cobranzas a ERP, preparación a ERP, EDI, telemetría) y Amazon SQS FIFO con EventBridge en nube (reconciliación y eventos cross-sitio, con orden garantizado por partición). Toda cola incluye reintento con retroceso exponencial, cola de mensajes fallidos (DLQ) y deduplicación en el consumidor (RT-02.07).

Las conexiones con sistemas externos se clasifican en síncronas y asíncronas. Las síncronas (SII/facturación, Transbank/POS, GIS/mapas) pasan por el API Gateway (Capa 3) con timeout explícito obligatorio (RT-02.08). Las asíncronas (ERP, EDI AS2, telemetría, notificaciones) pasan por colas (Capa 5) con DLQ y reintento. Esta clasificación define el contrato y el comportamiento ante falla de cada integración.


### 4.2.6  Capa de Acceso a Datos (Capa 6)

La capa de datos es híbrida por diseño, coherente con la naturaleza de la operación y con el despliegue obligatorio en dos ambientes:

On-premise por sitio (2 centros de distribución + 3 plataformas de cross-docking): PostgreSQL con PostGIS como base transaccional de bodega y operación local, constituyendo el maestro de bodega con autonomía de 24 horas. Cada sitio mantiene una réplica y respaldo con WAL.

Nube: Amazon Aurora PostgreSQL como réplica/DRP del maestro de bodega y como OLTP de preventa y reparto; Amazon DynamoDB para ingesta IoT de sensores de frío (raw con TTL de 30 días); Amazon S3 y Redshift Serverless para la serie consolidada OLAP (S3 Parquet ← AWS Glue ← DynamoDB raw); Redis (Amazon ElastiCache) para cache de stock caliente, precios y sesiones SSO; y S3 como almacén de documentos (POD firmado, DTE, comprobantes, evidencia QR).

La separación transaccional/analítica es estricta: la analítica no lee del transaccional para evitar degradar la ventana crítica de despacho. Las latencias comprometidas son: operación del día ≤ 5 minutos, cierre comercial ≤ 2 horas, gestión ≤ 4 horas.


### 4.2.7  Capa de Seguridad Transversal (Capa 7)

La seguridad se aplica transversalmente a todas las capas, no como perímetro único. Sus dominios principales son:

Identidad y acceso: Keycloak como proveedor de identidad (IdP) maestro en ECS/Fargate con OIDC, SSO, MFA y perfiles por cada uno de los 11 actores canónicos. Caché local on-premise con TTL de 8 horas que sostiene la autonomía de 24 horas en centro de distribución y 14 horas en terreno.

Gestión de secretos: AWS Secrets Manager y SSM Parameter Store con rotación automática. Los nodos on-premise los consumen por VPC Endpoint saliente, sin abrir puertos entrantes (D13).

Cifrado: TLS 1.3 y mTLS en tránsito; AWS KMS en reposo.

Microsegmentación: mTLS entre servicios internos, sin confianza implícita en la red.

Auditoría: registros inmutables (RT-16.07) con trazabilidad de acciones por actor, almacenados en formato inmodificable.

Detección: Amazon GuardDuty, Security Hub y CloudTrail con correlación en la capa de observabilidad.

Modelado de amenazas: STRIDE por componente y por integración externa (Art. 21.1), con mitigación diseñada antes de la implementación.

La identidad y acceso se modela con RBAC por rol canónico complementado con ABAC por atributos de contexto (instalación, horario de turno, dispositivo), con segregación de funciones en aprobaciones y elevación temporal de privilegios (JIT) con justificación y registro auditado (RT-12.05–12.07).


### 4.2.8  Capa de Observabilidad Transversal (Capa 8)

La capa de observabilidad formaliza métricas, registros y trazas distribuidas con correlación en nube y on-premise, sobre una sola plataforma conforme a RT-03.16 y Art. 16.4.

La instrumentación se basa en OpenTelemetry (SDK en Django, apps Kotlin, API Gateway, RabbitMQ/SQS, Greengrass) con trazas y métricas nativas y spans correlacionados por `transaction_id` propagado desde la Capa 3.

En on-premise, los colectores ADOT (con buffer en disco de 24 horas) recolectan la telemetría local y la exportan a la plataforma centralizada en nube: Amazon Managed Service for Prometheus (AMP) compatible con PromQL para métricas, Amazon CloudWatch Logs para registros (12 meses en línea + 24 meses en archivo), AWS X-Ray para trazas distribuidas (30 días de retención) y Grafana OSS autoadministrado en sa-east-1 para tableros operacionales unificados.

Los tableros se estructuran en tres niveles: operacional (para el equipo de TI y SRE), gerencial (para la gerencia y jefes) y del mandante (para Puelche, solo lectura con auditoría de consultas, conforme a RT-14.02). Las alertas se formulan por síntomas de negocio, no por causas técnicas, con ventanas de evaluación para evitar falsos positivos y escalamiento por criticidad.

Durante un corte de enlace, los tableros centralizados no están disponibles, pero el buffer de 24 horas garantiza que no se pierde telemetría, las alarmas locales del equipamiento operan independientemente y las decisiones de la ventana crítica de despacho (05:30–07:00) no dependen de la observabilidad centralizada.


## 4.3  Módulos Funcionales

La capa de servicios de negocio se compone de 12 módulos funcionales (M1–M12), cada uno con un actor canónico responsable, un conjunto de requerimientos funcionales trazables y límites de contexto explícitos. A continuación se describen los seis módulos seleccionados como ejes centrales de la solución.


### 4.3.1  Módulo de Trazabilidad

El módulo de trazabilidad resuelve el problema central que motivó la licitación: la incapacidad de responder en tiempo real ante un retiro sanitario. En marzo de 2026, un retiro preventivo de queso fresco tomó 9 días en resolverse de forma inexacta, generando pérdidas de $31 millones, la apertura de un sumario sanitario y la suspensión como distribuidor autorizado por un proveedor clave por seis meses.

El módulo implementa la unidad de trazabilidad sanitaria definida como el lote del proveedor conforme al estándar GS1 (GTIN + lote + vencimiento FEFO + temperatura), decisión fundamentada en la decisión 16.1 #2 (v4). La identidad primaria se enlaza a la unidad logística SSCC en cada movimiento interno de Puelche. Se descartan caja y pallet como identidad primaria debido a la volumetría (aproximadamente 9.500 SKU, 2,4 millones de unidades mensuales) y por el estado real de la captura (41% de recepciones sin lote registrado): el problema no es el nivel de agregación, sino la captura; por eso la recepción exige lectura del lote del proveedor (RF-01).

La trazabilidad forward/backward se implementa evento a evento conforme al estándar GS1 EPCIS, permitiendo al sistema responder en menos de 2 horas ante un retiro sanitario (Cap. 18), con identificación precisa de los lotes y puntos de entrega afectados. Los registros de temperatura se capturan de forma continua por sensores IoT en cámaras y vehículos, con alerta automática ante excursiones fuera de rango (RF-09.03/05) y bloqueo del despacho cuando se detecta una excursión térmica (RF-09.07). El módulo integra sensores de frío (Greengrass, Capa 2), inventario (M2), preparación (M5) y la capa de observabilidad (Capa 8), con evidencia de cumplimiento exportable.


### 4.3.2  Módulo de Gestión de Inventario

El módulo de inventario gestiona el stock multi-sitio en la topología de 2 centros de distribución y 3 plataformas de cross-docking, con las siguientes capacidades:

Stock multi-sitio parametrizable (RF-02.02, RT-02.12): cada sitio informa su stock al consolidado; la venta con stock se ejecuta en tiempo real con conexión y con foto local sin ella. La topología es parametrizable para admitir la séptima instalación proyectada a 3 años y el eventual centro de distribución de Los Lagos hacia 2030.

Slotting y conteo ciego: asignación de ubicaciones por criterio documentado de rotación, peso y compatibilidad, con conteo cíclico de inventario mediado por terminales HHT con escáner GS1, reduciendo la discrepancia actual del 2,3% del valor contado a menos del 1%.

FEFO (First Expired, First Out): la preparación y el despacho respetan el principio de primer vencimiento, con secuenciación térmica para productos refrigerados y congelados.

Stock disponible: consulta de disponibilidad para preventa (online con conexión, offline con caché de turno) con reserva de stock mediante la regla de negocio definida en la decisión 16.1 #8 (doble compromiso de stock resuelto en el servidor, no con timestamp ciego).


### 4.3.3  Módulo de Preventa Móvil

El módulo de preventa resuelve una de las dolencias operativas más agudas: los 62 preventistas en terreno utilizan actualmente una aplicación obsoleta que no consulta stock ni crédito del cliente, se cae y duplica pedidos. El módulo implementa:

Toma de pedido offline (RF-03.02): el preventista toma el pedido sin señal de red. La aplicación mantiene una foto local de datos de lectura (stock, crédito del cliente, precios vigentes, promociones) que se descarga al inicio del turno cuando hay conectividad.

Identificador único y deduplicación (RF-03.16/17): cada evento generado offline lleva un UUID idempotente que se envía por el API Gateway con deduplicación en el servidor.

Validación de stock y crédito: la validación definitiva ocurre en la sincronización con la regla de negocio del servidor (reserva de stock, RF-03.03; crédito del cliente, RF-03.08/09). Sin conexión, el pedido queda como pendiente de validación y se resuelve en la sincronización posterior.

Sincronización diferida: al recuperar cobertura, el dispositivo envía las escrituras acumuladas por el API Gateway (Capa 3), que valida esquema y deduplica antes de entregar a la capa de negocio.

El diseño offline-first se sustenta en la constancia de que el preventista opera sin señal durante la jornada completa en terreno, y que la ventana de sincronización al recuperar cobertura no supera los 10 minutos para un dispositivo de reparto..


### 4.3.4  Módulo de Planificación de Rutas

El módulo de planificación de rutas automatiza un proceso que actualmente depende de una sola persona (21 años de conocimiento concentrado, con retiro programado en 2 años) que administra una planilla de 11 hojas. El módulo implementa:

Secuenciación automática: algoritmo de optimización determinístico (VRP con capacidad y ventanas de tiempo) ejecutado en menos de 20 minutos (Cap. 18), sin inteligencia artificial (RT-18), con explicabilidad completa para el planificador.

Ventanas horarias y capacidad: considera capacidad de vehículo, ventanas de entrega del cliente y cadena de frío.

Integración con GIS: consulta de direcciones, cálculo de ETA y geocercas por API externa, con caché de mapas por zona en dispositivos para degradación a ruta offline con secuencia cargada.

Costo de entrega: alimenta el cálculo del costo de servir por cliente, uno de los ejes de evaluación del caso.


### 4.3.5  Módulo de Rendición y Cobro

El módulo de rendición y cobro resuelve las diferencias de rendición que promedian $4,2 millones mensuales sin investigación de causa. Implementa:

Rendición digital individual (RF-07.02): cada conductor rinde sus cobros del turno de forma digital, con causales de descuadre clasificadas y trazables.

Cobranza en ruta (RF-07.06): el conductor cobra al cliente del canal tradicional con terminal POS móvil (Transbank), incluyendo doble captura offline cuando no hay señal y rendición posterior al reconectar.

Interfaz con ERP (RF-07.09): la rendición aprobada se envía al ERP por medio de colas asíncronas (Capa 5) con confirmación de llegada.

Costo de servir (RF-11): el módulo alimenta el tablero de BI con el costo real por entrega, incluyendo kilometraje real (telemetría M12), tiempo de servicio y deducciones por devoluciones.


### 4.3.6  Módulo de Dashboard de Costo de Servir

El módulo de inteligencia de negocio consolida la información operativa en tableros gerenciales de autoservicio (RT-05.27) con modelo semántico en el mismo lenguaje del negocio: OTIF, fill rate, costo por entrega, ocupación de flota y segmentación por canal/cliente.

Los tableros se alimentan del almacén analítico (Redshift Serverless) con latencias comprometidas: operación del día ≤ 5 minutos, cierre comercial ≤ 2 horas, gestión ≤ 4 horas (RT-05.29). El modelo dimensional se estructura en hechos (ventas, entregas, stock, costo de servir) y dimensiones (cliente, SKU, tiempo, ruta, canal), con drill-down hasta línea de pedido y lote para trazabilidad sanitaria completa.

La información es de solo lectura para la analítica, sin acceder al transaccional en vivo, conforme al principio de separación transaccional/analítico. Los informes se programan (diarios, semanales, mensuales) y se exportan de forma asíncrona con firma y checksum (RT-05.28).


## 4.4  Modelo de Datos Conceptual

El modelo de datos de la solución se fundamenta en un conjunto de entidades de negocio canónicas, sus relaciones y eventos, conforme a RT-02.13. Este modelo alimenta la matriz de trazabilidad del Capítulo 17.1 y los contratos de integración (OpenAPI 3.1 y AsyncAPI 2.6 por módulo).

Las entidades principales son:

Cliente: con RUT, razón social, canal (tradicional, food service, cadenas), crédito, georreferencia y estado de bloqueo. Eventos: creación, actualización y cambio de bloqueo.

Pedido: identificador UUID, preventista, cliente, líneas de detalle (SKU, cantidad, precio) y ciclo de vida (tomado → confirmado → preparado → despachado → entregado → rendido). Eventos: toma, confirmación, asignación de línea, despacho y evidencia de entrega.

SKU / Producto: con codificación GTIN/GS1, unidad, clasificación de temperatura, rangos térmicos (RF-09.01) y vida útil.

Lote: la unidad de trazabilidad sanitaria, vinculada al lote del proveedor (GS1: GTIN + lote + vencimiento) y enlazada a la unidad logística SSCC en cada movimiento interno. Eventos: recepción, bloqueo, inicio de retiro sanitario y enlace con unidad logística.

Misión de preparación: HHT, oleada, ubicación, unidades y ciclo de vida (descargada → ejecutada → cerrada).

Ruta / viaje: planificador, vehículo, conductor, ventanas, secuencia de entregas y geocercas.

Entrega: pedido, viaje, prueba de entrega (POD: firma, QR, fotografía), documentos DTE y efectivo. Eventos: evidencia, reintento y aprobación de rendición.

Documento tributario: factura, boleta, guía de despacho, folio del SII y acuse.

Envase retornable: canastillo o pallet, cliente, saldo y pérdida estimada del 14% anual (decisión 16.1 #10). Control por cuenta corriente por cliente, no por unidad identificada.

Sensor / registro térmico: dispositivo, lote o posición, temperatura y excursión térmica.

Los eventos usan verbos en pasado y son la base de los esquemas AsyncAPI. Toda escritura offline es idempotente por UUID (RT-02.06).

El almacenamiento se distribuye en quince bases de datos lógicas con nombre, separadas por dominio: BD_INVENTARIO, BD_PREVENTA, BD_RUTAS (PostGIS), BD_PREPARACION, BD_REPARTO, BD_COBRANZA_FINANZAS, BD_MAESTROS_CONF, BD_GOBIERNO_ACCESO, BD_CALIDAD_TRAZABILIDAD, BD_TELEMETRIA (OLAP: S3 Parquet → Glue → Redshift), BD_EDI_CANALMODERNO, BD_BI_GERENCIA (analítica nube), BD_MAILS_NOTIF, REDIS_SESIONES_CACHE y S3_DOCS. Las quince bases corresponden a una separación lógica por dominio, no a quince servidores físicos.


## 4.5  Tecnologías Seleccionadas

A continuación se resume la tecnología de cada capa y su justificación principal:

Backend (12 módulos): Django (Python 3.12) como monolito modular. GeoDjango/PostGIS de primer nivel para el caso GIS-fuerte, un solo lenguaje, administración integrada y LTS de 56 meses.

Frontend web (portales y consolas): Angular con Tailwind CSS. Framework corporativo con TypeScript, soporte OIDC directo con Keycloak y LTS de Google.

Apps de campo (preventa y reparto): Kotlin Android nativo. Nativo del parque Zebra/Android, escáner GS1 vía Zebra DataWedge, SQLite/Room offline, acceso nativo a GPS, POS y térmica.

Borde / CDN / WAF (Capa 2): CloudFront + WAF + Shield + ALB en nube; firewall/UTM con IPS en ingreso on-premise.

Puerta de enlace de servicios (Capa 3): Amazon API Gateway. Servicio administrado sin nodo a operar, integración nativa con WAF, throttling, cuotas y OIDC.

Base de datos transaccional: PostgreSQL + PostGIS on-premise por sitio (maestro de bodega, autonomía 24 horas).

Base de datos nube (OLTP + DRP): Amazon Aurora PostgreSQL. Compatible con PostgreSQL, multi-AZ, failover en menos de 30 segundos, PITR de 35 días.

Ingesta IoT / frío: Amazon DynamoDB con AWS IoT Greengrass en borde. Escrituras serverless con TTL nativo (raw 30 días).

Serie consolidada (OLAP): S3 Parquet + AWS Glue + Redshift Serverless. OLAP por diseño: DynamoDB raw → Glue → S3 Parquet → Redshift, sin motor de series adicional.

Cache / sesiones: Amazon ElastiCache (Redis). Sin instancia on-premise: la operación desconectada se sostiene con la caché de turno del dispositivo y la caché del IdP (TTL 8 horas).

Mensajería asíncrona (Capa 5): RabbitMQ en on-premise + SQS FIFO y EventBridge en nube.

Analítica / BI: S3 Data Lake + Redshift Serverless + Glue ETL. OLAP histórico sin degradar OLTP.

Objetos / documentos: Amazon S3 con Intelligent-Tiering y Object Lock.

IAM / Identidad (Capa 7): Keycloak (OIDC, SAML, SSO, MFA) como IdP maestro en ECS/Fargate con caché local on-premise.

Gestión de secretos (Capa 7): AWS Secrets Manager + SSM Parameter Store con rotación automática (D13).

Observabilidad (Capa 8): OpenTelemetry/ADOT (emisión on-premise, buffer 24 horas) + AMP + CloudWatch Logs + X-Ray + Grafana OSS (plataforma única en nube, D14).

Gestión de dispositivos (RT-03.18): MDM gestionado (Android Enterprise / Zebra DNA, SaaS) como componente con emplazamiento propio (N-13, D15).

Contenedores / orquestación: Docker + ECS Fargate en nube; Docker Compose sobre Proxmox en on-premise.

Infraestructura como Código: Terraform (multi-zona) + Ansible.

CI/CD: GitLab CI como orquestador + AWS CodeBuild para construcción hermética con procedencia SLSA 3.

Los servicios AWS consumidos incluyen: CloudFront, WAF+Shield, ALB, API Gateway, Aurora, ElastiCache, DynamoDB, S3, Redshift Serverless, ECS Fargate, Route 53, Secrets Manager/SSM, KMS, IAM+Organizations, CloudWatch/X-Ray/AMP, Transit Gateway/VPC Peering, SQS, AWS Backup, GuardDuty/Security Hub, CloudTrail, SES/SNS e IoT Core+Greengrass.

El núcleo de la plataforma se compone de software de código abierto (Django, Angular, PostgreSQL, Redis, RabbitMQ, Keycloak) portable y sin lock-in de proveedor, coherente con las exigencias de mantenibilidad por un equipo pequeño durante los 56 meses de contrato.


## 4.6  Patrones de Diseño y Buenas Prácticas

La arquitectura aplica un conjunto de patrones de diseño que responden a las restricciones específicas de la operación de Puelche:

Offline-first con sincronización idempotente. Toda escritura desde un dispositivo sin conexión lleva un UUID único y se envía por el API Gateway al reconectar. El servidor deduplica (RT-02.06) y resuelve los conflictos de stock por regla de negocio, no por marca de tiempo ciega (S26). Este patrón es la piedra angular del diseño: previene la pérdida de transacciones y la duplicación de pedidos, que eran fallas recurrentes en la operación actual.

Servicios stateless con estado en almacenes externos. Los módulos de negocio (Capa 4) no mantienen estado en memoria; las sesiones se almacenan en Keycloak/Cookie y Redis (ElastiCache), y en operación desconectada la sesión la sostiene la caché local del IdP con TTL de 8 horas (A-05). Este patrón habilita el escalado horizontal en ECS Fargate y la resiliencia ante fallos de un nodo individual.

Degradación elegante sin pérdida silenciosa. Cuando un componente no responde, la operación continúa en modo reducido informado a la persona usuaria ("modo offline"). Ninguna degradación produce pérdida de una transacción de venta o entrega: si una escritura no llega al servidor, queda en el buffer local del dispositivo, visible como pendiente y reconciliada en la sincronización posterior (RT-02.09). La clasificación de servicios (RT-10.02) distingue cuatro niveles de criticidad: crítico (despacho 05:30–07:00), alto (preventa, rutas, DTE), medio (EDI, notificaciones, BI) y bajo (reportes ad-hoc).

Resiliencia con cortacircuitos y colas. Toda llamada remota lleva timeout explícito obligatorio (RT-02.08), reintento con retroceso exponencial y jitter, y cortacircuitos sobre sistemas externos (ERP, Transbank, SII). Un fallo de ERP no degrada la preventa. Las colas con DLQ (Capa 5) absorben los picos de integración y garantizan la entrega al menos una vez con deduplicación.

Capa anticorrupción sobre legados. Frente al ERP 2017 (sin documentación de interfaces) y al WMS 2013 (sin soporte GS1/SSCC ni modo offline para cámara a -22 °C), la arquitectura implementa una capa anticorrupción (ACL) con adaptadores por contrato OpenAPI y estrategia de estrangulamiento por capacidades (RT-02.14). Las capacidades del ERP se absorben de a una en los módulos M1, M5, M7 y M11; el WMS 2013 se absorbe en M2 y M5 (decisión 16.1 #14, D10).

Trazabilidad end-to-end por correlación. Cada transacción lleva un `transaction_id` que se propaga desde la Capa 3 a través de todas las capas, habilitando correlación completa de métricas, trazas y registros en la capa de observabilidad. Este patrón es exigido por RT-03.16 y Art. 16.4, que demandan "la misma plataforma" para nube y on-premise, sin puntos ciegos.

Gobierno de contratos y versionado. Las APIs de negocio y de integración se documentan con OpenAPI 3.1 (síncrona) y AsyncAPI 2.6 (eventos), con semver estricto, propietario declarado por módulo, compatibilidad hacia atrás y aviso mínimo de 6 meses antes de deprecar una versión (RT-05.16/17).

Seguridad Zero Trust. Cada solicitud se verifica explícitamente, sin presuponer la confiabilidad de ninguna red, dispositivo o identidad (NIST SP 800-207). La segmentación se implementa por IaC (Terraform), los servicios se comunican por mTLS, los secretos se gestionan en servicios administrados con rotación automática, y los registros de auditoría son inmutables (RT-16.07).

Separación transaccional/analítica. La analítica (M10, BI) no accede al transaccional en vivo; el almacén analítico (Redshift Serverless) se alimenta por eventos incrementales de la Capa 5 con generadores de flujo que procesan fuera de la ventana crítica (S19). Este patrón protege el desempeño de la operación y respalda los compromisos de latencia: operación del día ≤ 5 minutos, cierre comercial ≤ 2 horas, gestión ≤ 4 horas.


## 4.7  Diagramas de la arquitectura lógica


### 4.7.1  Diagrama general de la arquitectura lógica


![4.7.1  Diagrama general de la arquitectura lógica](../Diagramas/ARQL-01_Vision_general.png)

Figura 1. Diagrama general de la arquitectura lógica.


### 4.7.2  Diagrama del preventista de la arquitectura lógica


![4.7.2  Diagrama del preventista de la arquitectura lógica](../Diagramas/ARQL-02_Preventista.png)

Figura 2. Diagrama del preventista de la arquitectura lógica.


### 4.7.3  Diagrama del conductor propio de la arquitectura lógica


![4.7.3  Diagrama del conductor propio de la arquitectura lógica](../Diagramas/ARQL-03_Conductor_propio.png)

Figura 3. Diagrama del conductor propio de la arquitectura lógica.


### 4.7.4  Diagrama del conductor externo de la arquitectura lógica


![4.7.4  Diagrama del conductor externo de la arquitectura lógica](../Diagramas/ARQL-04_Conductor_externo.png)

Figura 4. Diagrama del conductor externo de la arquitectura lógica.


### 4.7.5  Diagrama del cliente canal tradicional de la arquitectura lógica


![4.7.5  Diagrama del cliente canal tradicional de la arquitectura lógica](../Diagramas/ARQL-05_Cliente_canal_tradicional.png)

Figura 5. Diagrama del cliente canal tradicional de la arquitectura lógica.


### 4.7.6  Diagrama del cliente canal moderno de la arquitectura lógica


![4.7.6  Diagrama del cliente canal moderno de la arquitectura lógica](../Diagramas/ARQL-06_Cliente_canal_moderno.png)

Figura 6. Diagrama del cliente canal moderno de la arquitectura lógica.


### 4.7.7  Diagrama del transportista de la arquitectura lógica


![4.7.7  Diagrama del transportista de la arquitectura lógica](../Diagramas/ARQL-07_Transportista.png)

Figura 7. Diagrama del transportista de la arquitectura lógica.


### 4.7.8  Diagrama del proveedor de la arquitectura lógica


![4.7.8  Diagrama del proveedor de la arquitectura lógica](../Diagramas/ARQL-08_Proveedor.png)

Figura 8. Diagrama del proveedor de la arquitectura lógica.


### 4.7.9  Diagrama del preparador de la arquitectura lógica


![4.7.9  Diagrama del preparador de la arquitectura lógica](../Diagramas/ARQL-09_Preparador.png)

Figura 9. Diagrama del preparador de la arquitectura lógica.


### 4.7.10  Diagrama de jefa de calidad de la arquitectura lógica


![4.7.10  Diagrama de jefa de calidad de la arquitectura lógica](../Diagramas/ARQL-10_Jefa_de_calidad.png)

Figura 10. Diagrama de jefa de calidad de la arquitectura lógica.


### 4.7.11  Diagrama de gerente comercial de la arquitectura lógica


![4.7.11  Diagrama de gerente comercial de la arquitectura lógica](../Diagramas/ARQL-11_Gerente_comercial.png)

Figura 11. Diagrama de gerente comercial de la arquitectura lógica.


### 4.7.12  Diagrama de gerente finanzas de la arquitectura lógica


![4.7.12  Diagrama de gerente finanzas de la arquitectura lógica](../Diagramas/ARQL-12_Gerente_finanzas.png)

Figura 12. Diagrama de gerente finanzas de la arquitectura lógica.


### 4.7.13  Diagrama de planificador de rutas de la arquitectura lógica


![4.7.13  Diagrama de planificador de rutas de la arquitectura lógica](../Diagramas/ARQL-13_Planificador_de_rutas.png)

Figura 13. Diagrama de planificador de rutas de la arquitectura lógica.


### 4.7.14  Diagrama de gerente de TI de la arquitectura lógica


![4.7.14  Diagrama de gerente de TI de la arquitectura lógica](../Diagramas/ARQL-14_Gerente_TI.png)

Figura 14. Diagrama de gerente de TI de la arquitectura lógica.
