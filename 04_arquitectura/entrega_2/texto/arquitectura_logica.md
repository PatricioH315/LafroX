# Capítulo 4 · Arquitectura Lógica de la Solución (Parte 4.1)

Versión de trabajo 0.2, basada en la revisión 67. Este subdocumento define responsabilidades, flujos e interfaces de la arquitectura lógica. Las referencias al despliegue expresan dependencias de esos servicios; no sustituyen ni modifican el subdocumento de arquitectura física.

## 4.1  Visión General de la Arquitectura

En Puelche, un pedido debe poder tomarse en una ruta sin cobertura, prepararse durante la noche y llegar al cliente con su lote y su evidencia de entrega identificados. La arquitectura parte de esa continuidad: cada operación se registra donde ocurre y se reconcilia cuando vuelve la conexión. Para ordenar las responsabilidades, la solución se organiza en las ocho capas exigidas por el numeral 2.1 de las Bases Técnicas Transversales (RT-02.01).

Los principios que gobiernan el diseño son los siguientes:

- **Continuidad sin conexión.** Preventa y reparto deben registrar un turno completo de 14 horas sin cobertura. El componente local debe mantener al menos 24 horas continuas de operación autónoma y degradada (RT-03.10). La sincronización posterior es idempotente: reenviar un evento no vuelve a ejecutar la operación. Los conflictos se resuelven con reglas de negocio documentadas, no dando prioridad automática al último registro recibido.

- **Atención adaptada al canal tradicional.** La solución no exige que los 11.600 almacenes instalen una aplicación ni dispongan de conexión propia. El conductor registra la entrega y su confirmación mediante firma o QR; los avisos por WhatsApp/SMS se utilizan cuando el canal está disponible.

- **Responsabilidades distribuidas entre bodega y nube.** Recepción, preparación y despacho mantienen su núcleo transaccional local. Preventa, reparto y canal moderno tienen sus servicios centrales en AWS, junto con la integración, la analítica y el almacenamiento consolidado. Las aplicaciones de terreno conservan la captura local aun cuando esos servicios no sean alcanzables. Esta separación responde al despliegue híbrido obligatorio del Art. 16.

- **Evolución durante 56 meses.** La Etapa 1 comprende los meses 1–15, con producción en el mes 16; la Etapa 2, los meses 13–20, con producción en el mes 21. Los 36 meses de operación se extienden del mes 21 al 56 (Art. 17).

- **Verificación explícita del acceso.** La identidad central utiliza OIDC y MFA. La comunicación interna aplica mTLS y segmentación, sin considerar confiable una solicitud solo por provenir de la red corporativa. La infraestructura se gestiona como código y los servicios críticos requieren distribución entre zonas de disponibilidad.

- **Recuperación con condiciones declaradas.** Se consideran cinco ambientes, incluido el de recuperación ante desastres (RT-04.01). La revisión 67 propone una región secundaria en us-east-1, con simulacros semestrales (Art. 20 / RT-07.07). La replicación de datos personales queda condicionada a la aprobación expresa del CLIENTE y a la revisión de los requisitos de transferencia aplicables. La alternativa intrarregional en sa-east-1 combina una tercera zona y respaldo inmutable, pero no equivale a recuperación ante la pérdida completa de la región: su cobertura y RTO deben aceptarse expresamente antes de adoptarla.

- **Operación sostenible para cuatro personas.** Las herramientas, los procedimientos y el soporte deben permitir que el equipo TI de Puelche administre la solución con el apoyo del adjudicatario durante todo el contrato.

La descripción sigue el marco TOGAF declarado y la organización de vistas de ISO/IEC/IEEE 42010. Este documento desarrolla la vista lógica y sus relaciones con procesos, datos, seguridad e integración. La vista de despliegue/física se mantiene en su documento específico; aquí no se declara su validación. Las decisiones se documentan mediante registros de decisión arquitectónica (ADR) fechados y fundamentados, conforme a RT-02.04.

El núcleo de negocio reúne 12 módulos en un monolito modular Django, con Python 3.12 como línea base de la propuesta. Esta organización mantiene separados los dominios sin imponer al equipo TI la operación de numerosos microservicios. Para 14.200 clientes y unos 31.000 pedidos mensuales, se privilegia esa simplicidad operativa, en línea con el numeral 2.3 de las Bases Técnicas Transversales. Los procesos de sincronización, EDI y telemetría pueden ejecutarse como trabajadores independientes cuando su carga lo requiera (RT-02.02). Se conserva la ejecución en contenedores: ECS Fargate en nube y Docker Compose sobre el entorno Proxmox local, sin desarrollar aquí su dimensionamiento físico.

La volumetría operativa que condiciona el dimensionamiento es la siguiente: 14.200 clientes activos, 8.400 SKU (que pasan a aproximadamente 9.500), 31.000 pedidos mensuales con 260.000 líneas y 2,4 millones de unidades, aproximadamente 1.400 entregas diarias habituales con peak de septiembre de 2.600 entregas (volumen casi duplicado durante tres semanas), 96 camiones en la ventana crítica de despacho (42 propios y 54 de transportistas externos), 62 preventistas, aproximadamente 200 conductores, 120 preparadores nocturnos y 310 personas de centro de distribución. El diseño se dimensiona contra el pico de septiembre en la ventana de 05:30 a 07:00, nunca contra el promedio, y declara explícitamente los puntos únicos de falla (SPOF) con su mitigación conforme a RT-02.11.

La revisión 67 distingue seis instalaciones: los CD de Talca y Concepción, las plataformas de cross-docking de Curicó, Chillán y Los Ángeles, y la casa matriz en Talca. Las primeras cinco requieren servicios locales de operación; la casa matriz utiliza los portales y el back office en nube. Esta distinción se conserva como supuesto de trabajo para aclarar la discrepancia entre cinco y seis instalaciones del caso, pendiente de respuesta del mandante. La identificación de sitio será parametrizable para admitir una séptima instalación proyectada a tres años y evaluar la futura operación en Los Lagos hacia 2030. No se presupone que sus recursos físicos estén ya aprobados.

## 4.2  Capas de la Arquitectura

Las ocho capas separan la interacción con las personas, las reglas de negocio y la persistencia. Seguridad y observabilidad atraviesan el conjunto. El siguiente mapa permite ubicar cada responsabilidad antes de revisar sus componentes.

| Capa | Nombre | Responsabilidad principal |
| --- | --- | --- |
| 1 | Presentación | Aplicaciones móviles, terminales de bodega, portales y consolas. |
| 2 | Borde y exposición | Protección del acceso, contenido estático y recepción segura de tráfico. |
| 3 | Puerta de enlace | Autenticación de APIs, contratos, cuotas y correlación. |
| 4 | Lógica de negocio | Reglas y procesos de los módulos M1–M12. |
| 5 | Integración y eventos | Colas, hub EDI y adaptadores de los sistemas externos. |
| 6 | Acceso a datos | Persistencia transaccional, analítica, documental y caché. |
| 7 | Seguridad transversal | Identidad, secretos, cifrado y auditoría. |
| 8 | Observabilidad transversal | Métricas, registros, trazas y alertas de operación. |

### 4.2.1  Capa de Presentación

La capa de presentación reúne las herramientas que utiliza cada persona para trabajar: aplicaciones móviles que pueden operar sin conexión y portales web servidos desde la nube. La revisión 67 declara 11 roles canónicos para el modelo de acceso. Las 13 vistas de perfiles heredadas se conservan en 4.7 como referencia; su correspondencia con esos roles debe quedar validada en la matriz de permisos, sin confundir una vista de interacción con un rol de autorización.

Las aplicaciones de campo (preventa y reparto) se construyen en Kotlin nativo para Android, decisión alineada con el ecosistema del parque de dispositivos Zebra (EC55, TC58e, MC9400) desplegado en los centros de distribución y con las condiciones de operación del terreno. La app de preventa mantiene una foto local de datos de lectura (stock, precios, crédito, promociones) y captura local de eventos (pedidos, identificadores únicos UUID); la app de reparto gestiona la entrega, la prueba de entrega digital (POD con firma, código QR y fotografía), la cobranza en ruta y el control de envases retornables. Ambas aplicaciones operan con datos locales cifrados y sincronizan de forma idempotente por medio del API Gateway cuando se recupera la conectividad.

Los terminales de bodega (HHT con escáner GS1) descargan las misiones de preparación al inicio del turno y registran su ejecución localmente, incluso en cámaras a -22 °C sin señal. La continuidad de 24 horas corresponde al servicio de bodega en su conjunto; debe verificarse con los cambios de turno y la vigencia de las credenciales, no deducirse de la sola descarga de misiones.

Los portales web, implementados en Angular con Tailwind CSS, permiten a clientes consultar pedidos y documentos, a transportistas revisar rutas y a proveedores consultar órdenes y recepciones. El catálogo público admite consulta sin autenticación; las funciones privadas requieren identidad OIDC mediante Keycloak y permisos por rol. La tarea `web` en ECS Fargate sirve las aplicaciones. El acceso administrativo se restringe a la red corporativa o a VPN con MFA.

Las consolas de rutas, calidad, BI y administración TI acceden a sus dominios mediante APIs autorizadas. Ningún navegador se conecta directamente a las bases de datos. Esta separación permite aplicar las mismas reglas de acceso y auditoría con independencia de la pantalla utilizada.

### 4.2.2  Capa de Borde y Exposición (Capa 2)

La capa de borde constituye el único punto de entrada público de la plataforma y, en el contexto de Puelche, también es el borde de terreno y bodega donde la conectividad es intermitente. Sus componentes principales son:

- **CDN (Amazon CloudFront).** Distribución de contenido estático de portales y catálogo público.

- **WAF gestionado (AWS WAF + Shield).** Filtrado de tráfico con reglas OWASP Top 10 y reglas personalizadas por API; protección contra denegación de servicio en capas 3, 4 y 7.

- **Balanceador de carga (ALB).** Distribuye hacia los servicios privados el tráfico que API Gateway entrega mediante su integración privada. El flujo de negocio se describe como cliente → API Gateway → integración privada/ALB → servicio, conservando la corrección del preliminar anterior.

- **Acceso local y continuidad del enlace.** Los servicios locales quedan detrás del control de acceso del sitio (D-01). La revisión 67 propone conectividad por fibra, Starlink y LTE dual, con conmutación SD-WAN objetivo inferior a 30 segundos. Para la arquitectura lógica, esto constituye una dependencia de conectividad: aunque falle la conmutación, las operaciones críticas deben continuar localmente. Su implementación, redundancia y dimensionamiento se remiten a arquitectura física.

- **AWS IoT Greengrass.** Borde IoT en terreno y almacenes para la recolección de datos de sensores de frío y telemetría de camiones, con buffer de reenvío y persistencia local durante cortes de conectividad.

### 4.2.3  Capa de Puerta de Enlace de Servicios (Capa 3)

Amazon API Gateway concentra la publicación de servicios, conforme a la decisión D8 citada por la revisión 67 (2026-09-05). El diseño requiere validar la identidad emitida por Keycloak, controlar esquema, cuotas y tasa de solicitudes, y propagar un `transaction_id`. La modalidad de API y su mecanismo de autorización deben concretarse al implementar; no se presupone que todas las modalidades ofrezcan las mismas capacidades de forma nativa. La integración privada entrega el tráfico al ALB y a los servicios en ECS Fargate.

La capa publica dos conjuntos de APIs: las de negocio (`/v1`) y las de sincronización offline (`/sync/v1`), estas últimas con escrituras idempotentes por UUID. La sincronización de dispositivos de preventa, reparto y misiones de picking constituye tráfico de API de primera clase que ingresa por el Gateway, valida esquema y aplica deduplicación en el servidor (RT-02.06).

### 4.2.4  Capa de Lógica de Negocio (Capa 4)

La capa de servicios de negocio encapsula los 12 módulos funcionales de la solución (M1–M12), implementados como un monolito modular Django con cada módulo separado por apps y contextos. Los módulos son stateless (RT-02.05): el estado de proceso reside en las bases de datos y colas de la capa de datos y de integración, nunca en memoria del proceso.

Los componentes críticos se empaquetan y escalan por separado como workers o procesos desacoplados: sincronización offline, EDI (AS2) y telemetría. Esta modularidad permite extraer estos workers del monolito si el volumen lo requiere, preservando la capacidad de escalado independiente de los servicios críticos (RT-02.02).

El escalado horizontal se ejecuta en nube mediante ECS Fargate con autoscaling por umbrales de CPU, rutas y colas, con límites superiores y costo declarados en la oferta. En on-premise, los contenedores se escalan por sitio con réplicas sobre el clúster Proxmox.

### 4.2.5  Capa de Integración y Eventos (Capa 5)

La capa de integración conecta la nueva operación con sistemas que Puelche ya utiliza. Sus límites son especialmente importantes ante el ERP de 2017 sin interfaces documentadas y el WMS de 2013. También concentra el intercambio con cadenas del canal moderno, los servicios de pago, los mapas y la telemetría, de modo que un cambio externo no obligue a modificar cada módulo de negocio.

RabbitMQ conserva las colas de integración local. En nube, EventBridge distribuye eventos y SQS FIFO ordena los mensajes que requieren secuencia dentro de cada grupo. El orden no se presume global ni se atribuye a toda la cadena de eventos. Los consumidores aplican deduplicación, reintentos con espera creciente y una cola de mensajes fallidos (DLQ), con intervención trazable cuando el procesamiento no puede completarse (RT-02.07).

Las APIs de la plataforma reciben solicitudes por la Capa 3. Los servicios de negocio invocan sus adaptadores de integración cuando necesitan consultar pagos o mapas, con tiempo máximo de espera explícito (RT-02.08). Los intercambios diferidos con ERP, EDI, telemetría y notificaciones utilizan colas y reintentos. La emisión tributaria se canaliza por el ERP mediante la ACL; no se crea un segundo emisor de documentos ante el SII.

El ERP de 2017 se conserva como única fuente de verdad tributaria y único emisor de DTE. La capa anticorrupción (ACL) traduce los contratos de la solución al formato del legado, sin reemplazarlo ni modificar su código. El flujo de rendición es: rendición aprobada → SQS → `celery-erp-sync` → ACL → ERP. Ningún módulo, portal o cadena escribe directamente en el ERP. La solución conserva el folio, estado y acuse que devuelve la integración para poder seguir cada documento hasta su operación de origen.

La integración con las cadenas del canal moderno se resuelve con un Hub EDI centralizado GS1 en nube (EANCOM, GS1 XML y EPCIS), con conector configurable por cadena, tabla de equivalencias GTIN (RF-12.03), bandeja de excepciones (RF-12.06) y Capa Anticorrupción hacia el ERP y la GDE. El hub mapea cada cadena contra un modelo canónico GS1, no contra el ERP; AS2 es uno de los transportes del hub. El canal moderno queda operativo ≤ enero 2029.

### 4.2.6  Capa de Acceso a Datos (Capa 6)

La capa de datos distingue quién conserva la información operativa, quién la consolida y quién la consulta para análisis. Esta separación evita que una caída del enlace detenga la bodega o que una consulta gerencial compita con el despacho. La revisión 67 diferencia los siguientes roles lógicos por sitio:

On-premise:
- **CD Talca:** PostgreSQL 16 con PostGIS como maestro de bodega para recepción, preparación y despacho, con autonomía mínima de 24 horas.
- **CD Concepción:** PostgreSQL y WMS de alcance reducido (`wms_only`), capaz de sostener 24 horas de operación local sin depender de Talca.
- **Cross-docking de Curicó, Chillán y Los Ángeles:** mini-WMS para registrar recepción, desconsolidación y despacho. El detalle se sincroniza con Talca y los eventos críticos se publican en SQS FIFO cuando existe conexión. Las tres horas indicadas en el caso son una ventana operativa, no una excepción a RT-03.10: el diseño lógico exige al menos 24 horas de continuidad local degradada, cuya suficiencia deberá demostrarse mediante pruebas.

En nube: Amazon Aurora PostgreSQL como réplica/DRP del maestro de bodega y como OLTP de preventa, reparto y canal moderno; Amazon DynamoDB para ingesta IoT de sensores de frío (raw con TTL de 30 días); Amazon S3 y Redshift Serverless para la serie consolidada OLAP (S3 Parquet ← AWS Glue ← DynamoDB raw); Redis (Amazon ElastiCache) para caché de stock caliente, precios y sesiones SSO; y S3 como almacén de documentos (POD firmado, DTE, comprobantes, evidencia QR).

No se incorpora Redis local. Al iniciar el turno con conexión, la aplicación solicita a las APIs una copia de stock, precios y demás datos autorizados; los servicios la obtienen de sus almacenes, incluido ElastiCache. El dispositivo conserva esa copia cifrada en SQLite/Room y consulta allí mientras está desconectado. Al reconectar, reconcilia primero las escrituras pendientes y actualiza los datos de lectura. Reemplazar la copia de lectura nunca debe borrar pedidos, cobros ni evidencias aún no confirmados por el servidor.

La vigencia de esos datos es independiente de la identidad. La revisión 67 establece credenciales de turno de 8 horas en CD y 14 horas en terreno, además de una caché local de identidad de solo lectura con TTL de 8 horas. Son controles distintos: una copia reciente de precios no renueva la sesión y una sesión válida no convierte el stock descargado en una reserva confirmada.

La separación transaccional/analítica es estricta: la analítica no lee del transaccional para evitar degradar la ventana crítica de despacho. Las latencias comprometidas son: operación del día ≤ 5 minutos, cierre comercial ≤ 2 horas, gestión ≤ 4 horas.

La revisión 67 plantea una política de respaldo 3-2-1-0 con cuatro funciones complementarias:

- **Recuperación local:** copia en NAS con control WORM y clave independiente, con objetivo de restauración del WMS de hasta 4 horas sin depender del enlace WAN. Esta copia no se contabiliza como la copia inmutable exigida.
- **Inmutabilidad en nube:** S3 Object Lock en modo Compliance y AWS Backup Vault Lock.
- **Recuperación regional:** Aurora Global Database y replicación de objetos S3 CRR con RTC, condicionadas a la aprobación del esquema de datos entre regiones y a pruebas de recuperación.
- **Custodia externa:** copia cifrada transportable, rotada semanalmente y con cadena de custodia. El respaldo en S3 no sustituye esta función.

Se propone un objetivo de punto de recuperación (RPO) de hasta 15 minutos mediante captura de cambios (CDC) desde el WAL lógico hacia nube con AWS DMS. Es un objetivo a probar con conectividad disponible, no una garantía durante un corte prolongado: en ese escenario los cambios permanecen en el sitio y el desfase remoto aumenta. La aceptación debe cubrir también la pérdida del sitio antes de sincronizar. Los procedimientos físicos de custodia y restauración corresponden a sus documentos específicos.

### 4.2.7  Capa de Seguridad Transversal (Capa 7)

La seguridad se aplica transversalmente a todas las capas, no como perímetro único. Sus dominios principales son:

- **Identidad y acceso.** Keycloak se mantiene como autoridad central en ECS Fargate, con OIDC, SSO y MFA. Los permisos se asignan a los 11 roles canónicos declarados, sujetos a la validación de su matriz de acceso. La caché local es de solo lectura y tiene TTL de 8 horas; las credenciales de turno duran 8 horas en CD y 14 horas en terreno. No se introduce un maestro local promocionable ni una credencial ordinaria de 24 horas. La recuperación de identidad debe conservar la misma autoridad y sus políticas.

La continuidad de 24 horas no queda demostrada solo por encadenar turnos de 8 horas. Antes de aprobar este diseño se debe especificar y probar cómo se habilita el siguiente turno cuando el IdP sigue inaccesible, qué sucede al vencer la caché y cómo se aplican las revocaciones pendientes. La cuenta de emergencia es una contingencia controlada y no reemplaza la autenticación normal de todos los operarios.

- **Gestión de secretos.** AWS Secrets Manager y SSM Parameter Store con rotación automática. Los nodos on-premise los consumen por VPC Endpoint saliente, sin abrir puertos entrantes, salvo las dos excepciones controladas D-AL-05 sobre túnel IPsec autenticado (D13). Cuenta de emergencia break-glass fuera de banda, custodiada en bóveda física con doble firma, para contingencia de indisponibilidad del IdP; su activación exige procedimiento escrito, notificación inmediata a TI y a la gerencia, registro en cadena de custodia y rotación de credenciales tras el uso. Se prueba dos veces al año junto con el simulacro de DRP. Prohibición absoluta de secretos embebidos en código, imágenes o archivos de configuración.

- **Cifrado y datos sensibles.** Se exige protección en tránsito mediante TLS y mTLS donde corresponda, y gestión de claves con KMS en nube. La revisión 67 propone cifrado por campo para antecedentes comerciales y comportamiento de pago, retención de 12 meses para geolocalización con registro de consultas, y seudonimización del RUT mediante mecanismos basados en pgcrypto. Estas políticas requieren aprobación y prueba de acceso y eliminación. El PAN de la tarjeta no se almacena; la integración utiliza tokenización de la pasarela. Las características y certificaciones del terminal POS se verifican en la adquisición, fuera del alcance de esta vista lógica.

- **Microsegmentación.** MTLS entre servicios internos, sin confianza implícita en la red.

- **Auditoría.** Registros inmutables (RT-16.07) con trazabilidad de acciones por actor, almacenados en formato inmodificable.

- **Detección.** Amazon GuardDuty, Security Hub y CloudTrail con correlación en la capa de observabilidad.

- **Modelado de amenazas.** STRIDE por componente y por integración externa (Art. 21.1), con mitigación diseñada antes de la implementación.

La identidad y acceso se modela con RBAC por rol canónico complementado con ABAC por atributos de contexto (instalación, horario de turno, dispositivo), con segregación de funciones en aprobaciones y elevación temporal de privilegios (JIT) con justificación y registro auditado (RT-12.05–12.07).

La revisión 67 distingue dos objetivos que deben medirse por separado: 99,95 % mensual para la infraestructura del recinto y al menos 99,9 % mensual para el servicio de negocio de extremo a extremo. El segundo se comprueba sobre la transacción crítica y no se deduce de la disponibilidad de cada componente. La cobertura, exclusiones y medición se contrastarán con los niveles de servicio contractuales; durante el despacho de 05:30 a 07:00 sigue vigente la exigencia de continuidad de la operación.

### 4.2.8  Capa de Observabilidad Transversal (Capa 8)

La observabilidad debe ayudar al equipo a responder preguntas operativas: qué pedido quedó pendiente, dónde se interrumpió una integración y qué entregas pueden verse afectadas. Para ello reúne métricas, registros y trazas de nube y sitios locales en una misma plataforma (RT-03.16 y Art. 16.4).

La instrumentación se basa en OpenTelemetry (SDK en Django, apps Kotlin, API Gateway, RabbitMQ/SQS, Greengrass) con trazas y métricas nativas y spans correlacionados por `transaction_id` propagado desde la Capa 3.

En on-premise, los colectores ADOT (con buffer en disco de 24 horas) recolectan la telemetría local y la exportan a la plataforma centralizada en nube: Amazon Managed Service for Prometheus (AMP) compatible con PromQL para métricas con retención de 13 meses, Amazon CloudWatch Logs para registros (12 meses en línea + 24 meses en archivo), AWS X-Ray para trazas distribuidas (30 días de retención) y Grafana OSS autoadministrado en sa-east-1 para tableros operacionales unificados.

Los tableros se estructuran en tres niveles: operacional (para el equipo de TI y SRE), gerencial (para la gerencia y jefes) y del mandante (para Puelche, solo lectura con auditoría de consultas, conforme a RT-14.02). Las alertas se formulan por síntomas de negocio, no por causas técnicas, con ventanas de evaluación para evitar falsos positivos y escalamiento por criticidad.

Durante un corte de enlace, el sitio no depende de los tableros centralizados para despachar. Las alarmas locales continúan y los colectores retienen la telemetría para enviarla al restablecer la conexión. La capacidad del buffer de 24 horas debe comprobarse con la carga de diseño; no se presume conservación ilimitada. La retención de métricas, registros técnicos y trazas no sustituye la política de auditoría de negocio exigida por RT-16.10.

## 4.3  Módulos Funcionales

Los 12 módulos M1–M12 separan responsabilidades de negocio y conservan su trazabilidad a los requerimientos funcionales. Los seis descritos a continuación permiten seguir el recorrido principal de la operación: conocer el lote, disponer de stock, tomar el pedido, organizar la ruta, rendir el cobro y medir el resultado.

### 4.3.1  Módulo de Trazabilidad

El módulo de trazabilidad resuelve el problema central que motivó la licitación: la incapacidad de responder en tiempo real ante un retiro sanitario. En marzo de 2026, un retiro preventivo de queso fresco tomó 9 días en resolverse de forma inexacta, generando pérdidas de $31 millones, la apertura de un sumario sanitario y la suspensión como distribuidor autorizado por un proveedor clave por seis meses.

El módulo implementa la unidad de trazabilidad sanitaria definida como el lote del proveedor conforme al estándar GS1 (GTIN + lote + vencimiento FEFO + temperatura), decisión fundamentada en la decisión 16.1 #2 (v4). La identidad primaria se enlaza a la unidad logística SSCC en cada movimiento interno de Puelche. Se descartan caja y pallet como identidad primaria debido a la volumetría (aproximadamente 9.500 SKU, 2,4 millones de unidades mensuales) y por el estado real de la captura (41% de recepciones sin lote registrado): el problema no es el nivel de agregación, sino la captura; por eso la recepción exige lectura del lote del proveedor (RF-01).

La trazabilidad forward/backward se implementa evento a evento conforme al estándar GS1 EPCIS, permitiendo al sistema responder en menos de 2 horas ante un retiro sanitario (Cap. 18), con identificación precisa de los lotes y puntos de entrega afectados. Los registros de temperatura se capturan de forma continua por sensores IoT en cámaras y vehículos, con alerta automática ante excursiones fuera de rango (RF-09.03/05) y bloqueo del despacho cuando se detecta una excursión térmica (RF-09.07). El módulo integra sensores de frío (Greengrass, Capa 2), inventario (M2), preparación (M5) y la capa de observabilidad (Capa 8), con evidencia de cumplimiento exportable.

### 4.3.2  Módulo de Gestión de Inventario

El módulo de inventario permite saber qué stock existe, dónde está y qué parte puede comprometerse. Mantiene la operación distribuida entre Talca, Concepción y los tres cross-docks; la casa matriz consulta la información consolidada. Sus capacidades son las siguientes:

- **Stock por sitio (RF-02.02, RT-02.12).** Cada instalación operativa informa sus movimientos al consolidado. Con conexión se consulta disponibilidad actual; sin ella se muestra la copia descargada, identificada como información pendiente de actualización. La parametrización admite nuevos sitios sin convertir a la casa matriz en una bodega ni asignarle stock operativo por defecto.

- **Slotting y conteo ciego.** Asignación de ubicaciones por criterio documentado de rotación, peso y compatibilidad, con conteo cíclico de inventario mediado por terminales HHT con escáner GS1, reduciendo la discrepancia actual del 2,3% del valor contado a menos del 1%.

- **FEFO (First Expired, First Out).** La preparación y el despacho respetan el principio de primer vencimiento, con secuenciación térmica para productos refrigerados y congelados.

- **Stock disponible.** Consulta de disponibilidad para preventa (online con conexión, offline con la foto de stock descargada desde ElastiCache al inicio del turno y almacenada localmente en SQLite/Room del dispositivo) con reserva de stock mediante la regla de negocio definida en la decisión 16.1 #8 (doble compromiso de stock resuelto en el servidor al sincronizar, no con timestamp ciego). Sin conexión, el pedido queda como pendiente de validación de stock hasta la sincronización posterior.

### 4.3.3  Módulo de Preventa Móvil

Para los 62 preventistas, tomar un pedido debe seguir siendo posible aun cuando la ruta no tenga cobertura. El módulo reemplaza una aplicación que no consulta stock ni crédito y presenta caídas y duplicación de pedidos. La nueva interacción distingue con claridad lo registrado en el dispositivo de lo confirmado por el servidor:

- **Toma de pedido offline (RF-03.02).** El preventista toma el pedido sin señal de red. La aplicación mantiene una foto local de datos de lectura (stock, crédito del cliente, precios vigentes, promociones) que se descarga al inicio del turno cuando hay conectividad.

- **Identificador único y deduplicación (RF-03.16/17).** Cada evento generado offline lleva un UUID idempotente que se envía por el API Gateway con deduplicación en el servidor.

- **Validación de stock y crédito.** La validación definitiva ocurre en la sincronización con la regla de negocio del servidor (reserva de stock, RF-03.03; crédito del cliente, RF-03.08/09). Sin conexión, el pedido queda como pendiente de validación y se resuelve en la sincronización posterior.

- **Sincronización diferida.** Al recuperar cobertura, el dispositivo envía las escrituras acumuladas por el API Gateway (Capa 3), que valida esquema y deduplica antes de entregar a la capa de negocio.

La prueba de aceptación de terreno considera un turno de 14 horas sin cobertura. El caso exige que un dispositivo de reparto sincronice esa jornada en un máximo de 10 minutos; para el CD, fija hasta 2 horas tras un corte de 24 horas. Estos límites se verifican con la volumetría correspondiente y reconciliación determinista (RT-03.12), sin extender automáticamente el umbral del repartidor a cualquier carga de preventa.

### 4.3.4  Módulo de Planificación de Rutas

El módulo de planificación de rutas automatiza un proceso que actualmente depende de una sola persona (21 años de conocimiento concentrado, con retiro programado en 2 años) que administra una planilla de 11 hojas. El módulo implementa:

- **Secuenciación automática.** Optimización determinista de rutas con capacidad y ventanas de tiempo (VRP), con objetivo de ejecución inferior a 20 minutos (Cap. 18). La solución propuesta no utiliza IA para esta función y debe permitir al planificador entender las restricciones y revisar el resultado; esa decisión de alcance no implica que RT-18 prohíba la IA.

- **Ventanas horarias y capacidad.** Considera capacidad de vehículo, ventanas de entrega del cliente y cadena de frío.

- **Integración con GIS.** Consulta de direcciones, cálculo de ETA y geocercas por API externa, con caché de mapas por zona en dispositivos para degradación a ruta offline con secuencia cargada.

- **Costo de entrega.** Alimenta el cálculo del costo de servir por cliente, uno de los ejes de evaluación del caso.

### 4.3.5  Módulo de Rendición y Cobro

El módulo de rendición y cobro resuelve las diferencias de rendición que promedian $4,2 millones mensuales sin investigación de causa. Implementa:

- **Rendición digital individual (RF-07.02).** Cada conductor rinde sus cobros del turno de forma digital, con causales de descuadre clasificadas y trazables.

- **Cobranza en ruta (RF-07.06).** El conductor registra el cobro y conserva su evidencia para la rendición. En pagos con POS móvil, la captura local de una operación no se presenta como autorización bancaria. El tratamiento sin cobertura depende de las capacidades y condiciones acordadas con la pasarela; se concilia al reconectar sin generar cargos duplicados.

- **Interfaz con ERP (RF-07.09).** La rendición aprobada se publica en SQS; el worker `celery-erp-sync` consume y entrega a la **capa anticorrupción (ACL)**; la ACL integra con el ERP. Nunca hay escritura directa al ERP. El ERP permanece como única fuente de verdad tributaria y único emisor de DTE.

- **Costo de servir (RF-11).** El módulo alimenta el tablero de BI con el costo real por entrega, incluyendo kilometraje real (telemetría M12), tiempo de servicio y deducciones por devoluciones.

### 4.3.6  Módulo de Dashboard de Costo de Servir

El módulo de inteligencia de negocio consolida la información operativa en tableros gerenciales de autoservicio (RT-05.27) con modelo semántico en el mismo lenguaje del negocio: OTIF, fill rate, costo por entrega, ocupación de flota y segmentación por canal/cliente.

Los tableros se alimentan del almacén analítico (Redshift Serverless) con latencias comprometidas: operación del día ≤ 5 minutos, cierre comercial ≤ 2 horas, gestión ≤ 4 horas (RT-05.29). El modelo dimensional se estructura en hechos (ventas, entregas, stock, costo de servir) y dimensiones (cliente, SKU, tiempo, ruta, canal), con drill-down hasta línea de pedido y lote para trazabilidad sanitaria completa.

La información es de solo lectura para la analítica, sin acceder al transaccional en vivo, conforme al principio de separación transaccional/analítico. Los informes se programan (diarios, semanales, mensuales) y se exportan de forma asíncrona con firma y checksum (RT-05.28).

La revisión 67 excluye IA y analítica predictiva del alcance propuesto. Se prioriza recuperar la calidad de la captura, dado que el caso informa un 41 % de recepciones sin lote registrado. El lago de datos columnar y el almacén analítico permiten evaluar esas capacidades más adelante, previa decisión del CLIENTE y sin darlas por incluidas. Esta delimitación debe mantenerse alineada con las innovaciones comprometidas en la propuesta.

## 4.4  Modelo de Datos Conceptual

El modelo de datos de la solución se fundamenta en un conjunto de entidades de negocio canónicas, sus relaciones y eventos, conforme a RT-02.13. Este modelo alimenta la matriz de trazabilidad del Capítulo 17.1 y los contratos de integración (OpenAPI 3.1 y AsyncAPI 2.6 por módulo).

Las entidades principales son:

- **Cliente.** Con RUT, razón social, canal (tradicional, food service, cadenas), crédito, georreferencia y estado de bloqueo. Eventos: creación, actualización y cambio de bloqueo.

- **Pedido.** Identificador UUID, preventista, cliente, líneas de detalle (SKU, cantidad, precio) y ciclo de vida (tomado → confirmado → preparado → despachado → entregado → rendido). Eventos: toma, confirmación, asignación de línea, despacho y evidencia de entrega.

- **SKU / Producto.** Con codificación GTIN/GS1, unidad, clasificación de temperatura, rangos térmicos (RF-09.01) y vida útil.

- **Lote.** La unidad de trazabilidad sanitaria, vinculada al lote del proveedor (GS1: GTIN + lote + vencimiento) y enlazada a la unidad logística SSCC en cada movimiento interno. Eventos: recepción, bloqueo, inicio de retiro sanitario y enlace con unidad logística.

- **Misión de preparación.** HHT, oleada, ubicación, unidades y ciclo de vida (descargada → ejecutada → cerrada).

- **Ruta / viaje.** Planificador, vehículo, conductor, ventanas, secuencia de entregas y geocercas.

- **Entrega.** Pedido, viaje, prueba de entrega (POD: firma, QR, fotografía), documentos DTE y efectivo. Eventos: evidencia, reintento y aprobación de rendición.

- **Documento tributario.** Factura, boleta, guía de despacho, folio del SII y acuse.

- **Envase retornable.** Canastillo o pallet, cliente, saldo y pérdida estimada del 14% anual (decisión 16.1 #10). Control por cuenta corriente por cliente, no por unidad identificada.

- **Sensor / registro térmico.** Dispositivo, lote o posición, temperatura y excursión térmica.

Los eventos usan verbos en pasado y son la base de los esquemas AsyncAPI. Toda escritura offline es idempotente por UUID (RT-02.06).

El almacenamiento se distribuye en quince dominios lógicos: BD_INVENTARIO, BD_PREVENTA, BD_RUTAS (PostGIS), BD_PREPARACION, BD_REPARTO, BD_COBRANZA_FINANZAS, BD_MAESTROS_CONF, BD_GOBIERNO_ACCESO, BD_CALIDAD_TRAZABILIDAD, BD_TELEMETRIA, BD_EDI_CANALMODERNO, BD_BI_GERENCIA, BD_MAILS_NOTIF, REDIS_SESIONES_CACHE y S3_DOCS. El dominio de telemetría conserva la ingesta raw en DynamoDB y su serie consolidada en S3 Parquet y Redshift, procesada con Glue. Esta separación incluye bases transaccionales, almacenes analíticos, caché y objetos; no representa quince servidores físicos ni quince motores de base de datos independientes.

## 4.5  Tecnologías Seleccionadas

A continuación se resume la tecnología de cada capa y su justificación principal:

- **Backend (12 módulos).** Django con Python 3.12 como línea base, organizado como monolito modular. GeoDjango y PostGIS cubren el trabajo geoespacial. El mantenimiento contempla actualizaciones a versiones soportadas durante los 56 meses; no supone soporte ininterrumpido de una única versión.

- **Frontend web.** Angular con Tailwind CSS y TypeScript. La integración con Keycloak se implementa mediante OIDC y se mantiene junto con las dependencias del cliente. Las versiones deben actualizarse durante el contrato conforme a sus ciclos de soporte.

- **Apps de campo (preventa y reparto).** Kotlin Android nativo. Nativo del parque Zebra/Android, escáner GS1 vía Zebra DataWedge, SQLite/Room offline, acceso nativo a GPS, POS y térmica.

- **Borde y continuidad del acceso (Capa 2).** CloudFront, WAF, Shield y ALB en nube, con control de acceso local. La conectividad por fibra, Starlink y LTE dual tiene un objetivo de conmutación inferior a 30 segundos, que debe probarse sin sustituir la autonomía del servicio local.

- **Puerta de enlace de servicios (Capa 3).** Amazon API Gateway. Servicio administrado sin nodo a operar, integración nativa con WAF, throttling, cuotas y OIDC.

- **Base de datos transaccional on-premise.** PostgreSQL + PostGIS por sitio con rol diferenciado — Talca maestro, Concepción edge `wms_only`, cross-docks mini-WMS con buffer acotado.

- **Base de datos nube (OLTP y recuperación).** Amazon Aurora PostgreSQL, con despliegue Multi-AZ y recuperación a un punto en el tiempo. La revisión propone una ventana de PITR de 35 días. Los tiempos de conmutación y restauración se miden en pruebas frente a los RTO/RPO comprometidos; no se da por garantizado un cambio de servicio en menos de 30 segundos.

- **Ingesta IoT / frío.** Amazon DynamoDB con AWS IoT Greengrass en borde. Escrituras serverless con TTL nativo (raw 30 días).

- **Serie consolidada (OLAP).** S3 Parquet + AWS Glue + Redshift Serverless. OLAP por diseño: DynamoDB raw → Glue → S3 Parquet → Redshift, sin motor de series adicional.

- **Caché y datos de turno.** Amazon ElastiCache en nube, sin instancia Redis local. Las APIs entregan una copia cifrada para SQLite/Room y conservan por separado la cola de escrituras pendientes. La identidad usa credenciales de 8 horas en CD y 14 horas en terreno, con las condiciones de continuidad descritas en 4.2.7.

- **Mensajería asíncrona (Capa 5).** RabbitMQ en on-premise + SQS FIFO y EventBridge en nube. **ERP integrado exclusivamente vía ACL; Hub EDI GS1 centralizado en nube (EANCOM, GS1 XML, EPCIS), AS2 como transporte.**

- **Analítica / BI.** S3 Data Lake, Redshift Serverless y Glue ETL. Consultas históricas sin degradar el procesamiento transaccional. No se incorpora IA ni analítica predictiva en el alcance propuesto por la revisión 67.

- **Objetos / documentos.** Amazon S3 con Intelligent-Tiering y Object Lock.

- **IAM / Identidad (Capa 7).** Keycloak (OIDC, SAML, SSO, MFA) como IdP maestro en ECS/Fargate con caché local on-premise de solo lectura.

- **Gestión de secretos (Capa 7).** AWS Secrets Manager + SSM Parameter Store con rotación automática (D13). **Cuenta de emergencia break-glass fuera de banda en bóveda física.**

- **Observabilidad (Capa 8).** OpenTelemetry/ADOT (emisión on-premise, buffer 24 horas) + AMP (**retención 13 meses**) + CloudWatch Logs + X-Ray + Grafana OSS (plataforma única en nube, D14).

- **Gestión de dispositivos (RT-03.18).** MDM gestionado (Android Enterprise / Zebra DNA, SaaS) como componente con emplazamiento propio (N-13, D15).

- **Contenedores / orquestación.** Docker + ECS Fargate en nube; Docker Compose sobre Proxmox en on-premise.

- **Infraestructura como Código.** Terraform (multi-zona) + Ansible.

- **CI/CD.** GitLab CI como orquestador + AWS CodeBuild para construcción hermética con procedencia SLSA 3.

Los servicios AWS consumidos incluyen: CloudFront, WAF+Shield, ALB, API Gateway, Aurora, ElastiCache, DynamoDB, S3, Redshift Serverless, ECS Fargate, Route 53, Secrets Manager/SSM, KMS, IAM+Organizations, CloudWatch/X-Ray/AMP, Transit Gateway/VPC Peering, SQS, AWS Backup, GuardDuty/Security Hub, CloudTrail, SES/SNS e IoT Core+Greengrass.

El núcleo utiliza tecnologías con alternativas de despliegue como Django, Angular, PostgreSQL, RabbitMQ y Keycloak. Eso facilita la portabilidad, pero no elimina la dependencia de los servicios administrados de AWS. La reversibilidad debe documentar contratos, exportación de datos y sustitución de adaptadores, junto con el esfuerzo de migración exigido por RT-03.07.

## 4.6  Patrones de Diseño y Buenas Prácticas

La arquitectura aplica un conjunto de patrones de diseño que responden a las restricciones específicas de la operación de Puelche:

**Registro local y sincronización idempotente.** Cada escritura recibe un UUID y permanece en una cola local hasta que el servidor confirma su procesamiento. Al volver la conexión se envía por API Gateway; el servicio de negocio deduplica y resuelve conflictos conforme a la regla S26 y RT-02.06. La copia de lectura en SQLite/Room se actualiza por separado. Así, renovar precios o stock no elimina un pedido pendiente y el trabajo de terreno no depende de una consulta a Redis en tiempo real.

**Servicios sin estado durable en memoria.** Las bases de datos y colas conservan el estado de negocio; las sesiones conectadas utilizan los mecanismos de identidad y caché definidos. Sustituir una instancia del servicio no debe perder el progreso de una operación. La identidad desconectada respeta las vigencias de 8 y 14 horas y la validación pendiente del cambio de turno, sin atribuir a una caché de solo lectura capacidad para emitir credenciales nuevas.

Degradación elegante sin pérdida silenciosa. Cuando un componente no responde, la operación continúa en modo reducido informado a la persona usuaria ("modo offline"). Ninguna degradación produce pérdida de una transacción de venta o entrega: si una escritura no llega al servidor, queda en el buffer local del dispositivo, visible como pendiente y reconciliada en la sincronización posterior (RT-02.09). La clasificación de servicios (RT-10.02) distingue cuatro niveles de criticidad: crítico (despacho 05:30–07:00), alto (preventa, rutas, DTE), medio (EDI, notificaciones, BI) y bajo (reportes ad-hoc).

Resiliencia con cortacircuitos y colas. Toda llamada remota lleva timeout explícito obligatorio (RT-02.08), reintento con retroceso exponencial y jitter, y cortacircuitos sobre sistemas externos (ERP, Transbank, SII). Un fallo de ERP no degrada la preventa. Las colas con DLQ (Capa 5) absorben los picos de integración y garantizan la entrega al menos una vez con deduplicación.

**Integración con legados mediante ACL.** Los módulos M1, M5, M7 y M11 intercambian información con el ERP a través de adaptadores; no absorben su responsabilidad tributaria ni modifican su código. Las capacidades del WMS 2013 se sustituyen gradualmente en M1, M2 y M5, conforme a las decisiones 16.1 #14, D10 y ADR-08 citadas por la revisión 67. La ACL mantiene separados el modelo de negocio nuevo y los formatos del legado, en coherencia con RT-02.14. No se permiten escrituras directas al ERP.

Trazabilidad end-to-end por correlación. Cada transacción lleva un `transaction_id` que se propaga desde la Capa 3 a través de todas las capas, habilitando correlación completa de métricas, trazas y registros en la capa de observabilidad. Este patrón es exigido por RT-03.16 y Art. 16.4, que demandan "la misma plataforma" para nube y on-premise, sin puntos ciegos.

Gobierno de contratos y versionado. Las APIs de negocio y de integración se documentan con OpenAPI 3.1 (síncrona) y AsyncAPI 2.6 (eventos), con semver estricto, propietario declarado por módulo, compatibilidad hacia atrás y aviso mínimo de 6 meses antes de deprecar una versión (RT-05.16/17).

Seguridad Zero Trust. Cada solicitud se verifica explícitamente, sin presuponer la confiabilidad de ninguna red, dispositivo o identidad (NIST SP 800-207). La segmentación se implementa por IaC (Terraform), los servicios se comunican por mTLS, los secretos se gestionan en servicios administrados con rotación automática, y los registros de auditoría son inmutables (RT-16.07). Sin puertos entrantes on-premise salvo las dos excepciones controladas D-AL-05 por túnel IPsec autenticado.

**Separación transaccional y analítica.** Los tableros consultan Redshift Serverless, no el transaccional en vivo. Los eventos incrementales permiten mantener las latencias de hasta 5 minutos para operación, 2 horas para cierre comercial y 4 horas para gestión. Las tareas pesadas se programan fuera de la ventana crítica, sin detener la actualización incremental necesaria para el tablero operacional. La revisión 67 no incluye IA ni analítica predictiva en este alcance.

## 4.7  Diagramas de la arquitectura lógica

Se conservan el diagrama general y las 13 vistas de perfiles de la biblioteca del proyecto. Son imágenes de la línea base, no diagramas redibujados para la revisión 67. Deben leerse junto con las responsabilidades y flujos actualizados en 4.1–4.6. Su concordancia con la ACL exclusiva del ERP, el hub EDI, los roles de sitio y el modelo de identidad queda pendiente de revisión gráfica; por ello, esta versión mantiene su carácter preliminar.

### 4.7.1  Diagrama general de la arquitectura lógica

![4.7.1  Diagrama general de la arquitectura lógica](../../../Diagramas/ARQL-01_Vision_general.png)

Figura 1. Diagrama general de la arquitectura lógica.

### 4.7.2  Diagrama del preventista de la arquitectura lógica

![4.7.2  Diagrama del preventista de la arquitectura lógica](../../../Diagramas/ARQL-02_Preventista.png)

Figura 2. Diagrama del preventista de la arquitectura lógica.

### 4.7.3  Diagrama del conductor propio de la arquitectura lógica

![4.7.3  Diagrama del conductor propio de la arquitectura lógica](../../../Diagramas/ARQL-03_Conductor_propio.png)

Figura 3. Diagrama del conductor propio de la arquitectura lógica.

### 4.7.4  Diagrama del conductor externo de la arquitectura lógica

![4.7.4  Diagrama del conductor externo de la arquitectura lógica](../../../Diagramas/ARQL-04_Conductor_externo.png)

Figura 4. Diagrama del conductor externo de la arquitectura lógica.

### 4.7.5  Diagrama del cliente canal tradicional de la arquitectura lógica

![4.7.5  Diagrama del cliente canal tradicional de la arquitectura lógica](../../../Diagramas/ARQL-05_Cliente_canal_tradicional.png)

Figura 5. Diagrama del cliente canal tradicional de la arquitectura lógica.

### 4.7.6  Diagrama del cliente canal moderno de la arquitectura lógica

![4.7.6  Diagrama del cliente canal moderno de la arquitectura lógica](../../../Diagramas/ARQL-06_Cliente_canal_moderno.png)

Figura 6. Diagrama del cliente canal moderno de la arquitectura lógica.

### 4.7.7  Diagrama del transportista de la arquitectura lógica

![4.7.7  Diagrama del transportista de la arquitectura lógica](../../../Diagramas/ARQL-07_Transportista.png)

Figura 7. Diagrama del transportista de la arquitectura lógica.

### 4.7.8  Diagrama del proveedor de la arquitectura lógica

![4.7.8  Diagrama del proveedor de la arquitectura lógica](../../../Diagramas/ARQL-08_Proveedor.png)

Figura 8. Diagrama del proveedor de la arquitectura lógica.

### 4.7.9  Diagrama del preparador de la arquitectura lógica

![4.7.9  Diagrama del preparador de la arquitectura lógica](../../../Diagramas/ARQL-09_Preparador.png)

Figura 9. Diagrama del preparador de la arquitectura lógica.

### 4.7.10  Diagrama de jefa de calidad de la arquitectura lógica

![4.7.10  Diagrama de jefa de calidad de la arquitectura lógica](../../../Diagramas/ARQL-10_Jefa_de_calidad.png)

Figura 10. Diagrama de jefa de calidad de la arquitectura lógica.

### 4.7.11  Diagrama de gerente comercial de la arquitectura lógica

![4.7.11  Diagrama de gerente comercial de la arquitectura lógica](../../../Diagramas/ARQL-11_Gerente_comercial.png)

Figura 11. Diagrama de gerente comercial de la arquitectura lógica.

### 4.7.12  Diagrama de gerente finanzas de la arquitectura lógica

![4.7.12  Diagrama de gerente finanzas de la arquitectura lógica](../../../Diagramas/ARQL-12_Gerente_finanzas.png)

Figura 12. Diagrama de gerente finanzas de la arquitectura lógica.

### 4.7.13  Diagrama de planificador de rutas de la arquitectura lógica

![4.7.13  Diagrama de planificador de rutas de la arquitectura lógica](../../../Diagramas/ARQL-13_Planificador_de_rutas.png)

Figura 13. Diagrama de planificador de rutas de la arquitectura lógica.

### 4.7.14  Diagrama de gerente de TI de la arquitectura lógica

![4.7.14  Diagrama de gerente de TI de la arquitectura lógica](../../../Diagramas/ARQL-14_Gerente_TI.png)

Figura 14. Diagrama de gerente de TI de la arquitectura lógica.
