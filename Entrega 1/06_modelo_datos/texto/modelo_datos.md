# Capítulo 5 · Modelo y Gestión de Datos (Subdoc. 5)


## 5.1 Visión General del Modelo de Datos

El modelo de datos de Puelche se organiza como persistencia políglota por dominio (ADR-04), que reconoce cuatro exigencias incompatibles entre sí y las reparte en motores especializados: el transaccional de preventa, reparto, bodega y cobranza exige consistencia y reconciliación determinista tras cortes; la ingesta IoT (sensores y termógrafos de cadena de frío) es escritura masiva de baja latencia con datos volátiles; la serie de tiempo consolidada de temperatura es analítica columnar con retención de 5 años; y la evidencia documental (POD, DTE) exige inmutabilidad legal durante 6 años. Un único motor no puede cumplir las cuatro posiciones CAP sin sacrificar desempeño (RT-05.02), y por eso el Cap. 15 del caso exige declarar motor y posición CAP por cada dominio.

El modelo de datos materializa el despliegue híbrido del Artículo 16°: el maestro de bodega vive on-premise (PostgreSQL + PostGIS por sitio, con autonomía 24 h sin enlace, RT-03.10) y se replica por CDC (WAL lógico) hacia Amazon Aurora PostgreSQL en sa-east-1, que concentra el OLTP de la nube (preventa, reparto, canal moderno, BI). El terreno opera offline de primera clase: las aplicaciones mantienen foto local de datos de lectura (stock, precios, crédito, rutas) y buffer de escrituras idempotente que se concilia al reconectar (RT-03.12), sin perder ni duplicar pedidos (Cap. 18, criterio 6).

La arquitectura de datos se describe conforme a ISO/IEC/IEEE 42010 y al diccionario por base lógica (RT-05.01), coherente con la arquitectura lógica v6.2 (Subdoc. 4.1) y con la arquitectura física (Subdoc. 4.2). La política de retención, archivado y eliminación se declara contra RT-16.10 (el caso la rotula RT-05.10; el código transversal correcto es RT-16.10, desajuste que se responde en el T-12 y se eleva como consulta al mandante por Art. 43.3) — ver S5.6.


## S5.1 Dominio de Información y Entornos de Datos — P6.1

El dominio de información de la solución cubre la totalidad de los datos que produce la operación de Puelche: preventa y pedidos, inventario y bodega (2 CD + 3 cross-docking), preparación, reparto y entregas, cobranza y cartera, trazabilidad sanitaria y cadena de frío, telemetría de flota, canal moderno EDI, documentos tributarios SII, analítica de gestión y datos maestros. Volumetría de referencia (Tabla 14.1 y Cap. 15 del caso): 14.200 clientes, 31.000 pedidos/mes (260.000 líneas, 2,4 M unidades), 180 proveedores, ~34.000 DTE/mes, 9.500 SKU proyectados a tres años, telemetría de 28 sensores + 18 termógrafos y ~1.400 entregas/día (peak de septiembre ≈ 2.600).


### Entornos de datos


> **Tabla 136** — Entornos de datos · 8 filas · ver planilla del subdocumento


### Bases/almacenes lógicos con nombre — 15 bases lógicas (no 15 servidores, S18)


> **Tabla 137** — Bases/almacenes lógicos con nombre — 15 bases lógicas (no 15 servidores, S18) · 16 filas · ver planilla del subdocumento

Multi-sitio por parametrización topológica (RF-02.02, RT-02.12): cada CD informa su stock al consolidado; un nuevo sitio se incorpora replicando la plantilla del clúster sin rediseño del modelo de datos.


## S5.2 Motor y Paradigma de Persistencia por Dominio (CAP) — P6.2

Justificación de paradigma y motor conforme a RT-05.02 (Obligatorio). Decisión: AP con consistencia eventual reconciliada — consistencia fuerte solo donde el negocio lo exige.


> **Tabla 138** — S5.2 Motor y Paradigma de Persistencia por Dominio (CAP) — P6.2 · 9 filas · ver planilla del subdocumento

Decisión de motor por dominio (decisión 16.1 #18): el volumen total es manejable en PostgreSQL con índices + PostGIS para georreferencia; DynamoDB absorbe el pico IoT; la serie consolidada vive en la capa OLAP (S3 Parquet → Redshift) y no se añade un motor de series dedicado (InfluxDB descartado: segundo motor a operar con un equipo TI de 4 personas — D2). El detalle de alternativas evaluadas y su fundamento está en ADR-04.


## S5.3 Migración, Saneamiento, Validación y Conciliación — P6.3


### Alcance y volúmenes por migrar (RT-05.11/05.15; valores del Cap. 15 del caso)


> **Tabla 139** — Alcance y volúmenes por migrar (RT-05.11/05.15; valores del Cap. 15 del caso) · 7 filas · ver planilla del subdocumento


### Metodología (RT-05.11 a RT-05.15)

Perfilado y saneamiento previo (RT-05.12): etapa de perfilado sobre los datos de origen (ERP 2017, WMS 2013, planillas) con informe de defectos detectados y decisión sobre cada uno (corregir / aceptar c/registro / excluir). Casos de saneamiento esperados y declarados: duplicados de cliente por RUT (maestro único resultante, MDM S5.6), campos de lote en texto libre o vacíos (el retiro de marzo mostró 41 % de recepciones sin lote), equivalencias de maestro entre cadenas (GTIN por cadena, RF-12.03) y saldos de envases (68.000 canastillos y 9.400 pallets sin control).

Reglas de transformación y carga verificada: carga de datos maestros con validación en el punto de captura y conciliación por recuentos; carga inicial transaccional por olas por sitio con estrategia azul-verde y plan de reversión.

Dos ensayos completos de migración sobre Preproducción (RT-05.13): con medición del tiempo total y del resultado de la conciliación; ensayo T + reensayo tras corrección.

Conciliación cuantitativa y verificable (RT-05.14): recuentos, sumas de control y muestreo dirigido; toda diferencia queda explicada y registrada en la bitácora de reconciliación (Art. 16.4). La reposición del conteo cíclico apuntala la exactitud del stock migrado (diferencia de 2,3 % → meta < 1 %).

Históricos no migrados (RT-05.15): quedan accesibles en repositorio de consulta solo lectura durante el período de retención del caso, sin depender del sistema legado; exportables bajo el régimen del Art. 85 (copia íntegra en formato interoperable con diccionario).

Coexistencia con el WMS 2013 (D10): el legado queda detrás de la misma ACL con tabla de «capacidad absorbida» (recepción GS1, slotting, misiones con HHT, conteo cíclico) que se vacía ola a ola por sitio, con estrategia azul-verde, plan de reversión y retiro al cierre de la Etapa 1.


## S5.4 Desempeño del Modelo de Datos: Indexación, Particionamiento y Caché — P6.4


### Indexación

Índices y claves en PostgreSQL/Aurora: FKs en todas las tablas transaccionales; índices por lote GS1 (GTIN + lote + vencimiento), SSCC y shipment_id (estructura que sostiene el retiro < 2 h), y PostGIS GiST para geometrías, rutas y geocercas (BD_RUTAS, BD_TELEMETRIA). Índices compuestos de trazabilidad forward/backward en BD_CALIDAD_TRAZABILIDAD.

Réplicas de solo lectura en Aurora para consultas de negocio sin competir con la escritura del maestro (2 lectores; RT-09.05).

Redshift: distribución por clave de negocio (ruta/lote) y compresión columnar sobre hechos (ventas, entregas, stock, costo de servir) y dimensiones (cliente, SKU, tiempo, ruta, canal).


### Particionamiento

Particionado mensual de transacciones de bodega (recepción, misiones, despacho) en PostgreSQL on-prem, primer remedio declarado ante el cuello de botella de escritura de la ventana 05:30–07:00 (RT-09.05; escala vertical → particionado + PgBouncer → réplica de lectura → 4.º nodo/sharding).

Orden garantizado por partición en mensajería (SQS FIFO con MessageGroupId = sitio/entidad) para reconciliación cross-sitio y eventos de trazabilidad (RT-02.07); el sync de terreno usa partición y reanudación (chunking) para cumplir ≤ 10 min de turno / ≤ 2 h de CD tras reconexión.

DynamoDB con TTL por partición (30 días) para telemetría raw; la serie consolidada se particiona en S3 Parquet por mes (5 años). El hub EDI particiona por cadena (perfiles de configuración, no desarrollo).


### Caché

Redis — Amazon ElastiCache (N-07): stock caliente, precios y sesiones SSO para latency de stock/crédito < 2 s en preventa (RT-09.01); patrón cache-aside con regeneración transparente < 15 min ante pérdida (el OLTP soporta la carga transicional).

Caché de turno precargada en el dispositivo (saldo, stock, tarifa; RT-17.03): foto local que sostiene el turno completo sin señal dentro de un consumo objetivo ≤ 8–12 MB/turno.

Caché local de identidad A-05 (Keycloak, TTL 8 h bodega / 14 h reparto) para autonomía sin red.

Caché de tableros (QuickSight, TTL) en las consolas locales de contingencia (RT-03.13); S3 Intelligent-Tiering para objetos de lectura fría.


### Optimización operacional

PgBouncer (pool de conexiones) y pre-generación nocturna de documentos de despacho y validaciones batch (crédito/stock) para descargar la ventana crítica.

Umbrales RT-09.01 cumplidos bajo carga de la ventana y verificados en marcha blanca: confirmación de línea de picking ≤ 1 s (lectura local PostgreSQL + HHT con misión descargada), registro de entrega ≤ 2 s, línea de preventa ≤ 1,5 s y consulta stock/crédito ≤ 2 s, en P95 frente al dimensionamiento de ~105 TPS base (~315 × 3× de crecimiento a tres años, RT-09.03).


## S5.5 Separación Transaccional / Analítica — P6.5

Cumplimiento de RT-05.05 (Obligatorio): el almacenamiento transaccional y el analítico están separados por diseño y ninguna consulta analítica puede degradar la operación.


> **Tabla 140** — S5.5 Separación Transaccional / Analítica — P6.5 · 7 filas · ver planilla del subdocumento

El cumplimiento de las latencias se mide con SLO en la Capa 8 (observabilidad única) y se verifica con pruebas de desempeño en la marcha blanca.


## S5.6 Calidad, Retención, Archivado y Eliminación Segura — P6.6 y P6.9


### Calidad de datos (RT-05.04, Obligatorio — marco ISO/IEC 25012, adoptado)


> **Tabla 141** — Calidad de datos (RT-05.04, Obligatorio — marco ISO/IEC 25012, adoptado) · 7 filas · ver planilla del subdocumento

Las reglas de calidad se declaran en el diccionario (RT-05.01) y se monitorean con controles automáticos (duplicados, saltos de secuencia, totales de conciliación) en la Capa 8; el incumplimiento genera tarea en el flujo de excepciones. Tablero de calidad disponible para el CLIENTE (RT-05.04).


### Retención, archivado y eliminación (RT-16.10, valores del Cap. 15 del caso)


> **Tabla 142** — Retención, archivado y eliminación (RT-16.10, valores del Cap. 15 del caso) · 8 filas · ver planilla del subdocumento

El caso rotula este requisito RT-05.10, pero el código transversal correcto es RT-16.10 (RT-05.10 es «catálogo de datos con linaje», Deseable). El desajuste se responde en el T-12 contra RT-16.10 y se declara como consulta al mandante (Art. 43.3), sin alterar los períodos.

Implementación de retención e inmutabilidad:


> **Tabla 143** — Retención, archivado y eliminación (RT-16.10, valores del Cap. 15 del caso) · 7 filas · ver planilla del subdocumento

Eliminación segura (RT-05.07, Obligatorio): procedimiento verificable de eliminación al vencimiento del plazo con registro inalterable (RT-16.07); borrado seguro de medios que salen de servicio y disposición final con gestor autorizado. Exportabilidad (RT-05.06, Obligatorio): la totalidad de la información del CLIENTE se exporta en formatos abiertos y documentados (CSV, JSON, Parquet con el diccionario), en cualquier momento del contrato, sin costo y sin intervención del proponente. Fin del contrato (Art. 85 BA / RT-05.08): entrega de copia íntegra en formato interoperable con diccionario y eliminación certificada de los datos del mandante, con directorio de tratamiento actualizado y auditoría.


## S5.7 Trazabilidad Sanitaria: Unidad de Trazabilidad y Retiro < 2 Horas — P6.7 y P6.8


### Unidad de trazabilidad sanitaria (decisión 16.1 #2; interrogante S16.3, núm. 2; D11)

La identidad primaria de la trazabilidad es el lote del proveedor en estándar GS1: GTIN + número de lote + fecha de vencimiento (con los rangos térmicos RF-09.01). La unidad logística (SSCC) se enlaza al lote en cada movimiento interno de Puelche (recepción → ubicación → picking → unidad de despacho). Se descartan caja y pallet como identidad primaria por la volumetría (~9.500 SKU, 2,4 M unidades/mes) y por el estado real de la captura (41 % de recepciones del producto del retiro sin lote): el problema es la captura, no el nivel de agregación; por eso la recepción exige lectura del lote del proveedor (RF-01), el 100 % de las recepciones registra el lote de los productos que lo requieren (Cap. 18, criterio 2) y la etiqueta SSCC se imprime al armar la unidad logística (RF-01.07).


### Modelo de trazabilidad

Evento a evento conforme a GS1 EPCIS (RT-05.23): cada movimiento genera un evento idempotente en la cadena (recibido, ubicado, preparado, despachado, entregado) con actor, equipo/dispositivo, timestamp y valores anteriores y posteriores (RT-05.03); los eventos se conservan como registros inmutables (RT-16.07).

Bidireccionalidad completa: forward — desde un lote del proveedor se responde con evidencia y no con estimación a qué clientes llegó, en qué fecha, en qué cantidad y con qué documento tributario; backward — desde una unidad en el local del cliente hasta la recepción que la originó (Cap. 9.5 del caso).

Drill-down hasta línea de pedido y lote en la analítica (RT-05.29).

Retiro sanitario < 2 horas (Cap. 18, criterio 1; situación actual: 9 días con resultado estimado): la consulta recorre BD_CALIDAD_TRAZABILIDAD con índices por lote/SSCC sobre la fuente de verdad consolidada (PostgreSQL + S3 Parquet), con SLO de respuesta y evidencia exportable ante la autoridad.

Registro continuo de temperatura en cámaras y vehículos (Cap. 18, criterio 3; hoy 3 lecturas manuales por viaje), con detección de excursión en el borde y regla escrita de bloqueo (decisión 16.1 #4).


### Gobernanza de trazabilidad

Los eventos se publican por la Capa 5 (orden por partición, deduplicación) y alimentan la lectura consolidada en el servidor; la bitácora de auditoría (RT-16.07) registra toda operación con quién, qué, cuándo, dispositivo y valores previos/posteriores, lo que sostiene la trazabilidad del dato de negocio (RT-05.03) además de la trazabilidad de lote. La matriz de trazabilidad del Cap. 17.1 conserva la relación origen → requerimiento → componente → prueba de cada dato.


## S5.8 Estándares GS1, EDI y Formato de la Autoridad Tributaria — P6.10

Cumplimiento de RT-05.23 (estándares sectoriales; llamada del caso en Cap. 16.2):


> **Tabla 144** — S5.8 Estándares GS1, EDI y Formato de la Autoridad Tributaria — P6.10 · 6 filas · ver planilla del subdocumento

La integración sigue el principio asíncrono por defecto, síncrono por excepción: lo síncrono queda restringido a los actos que lo exigen (DTE al SII, autorización de pago Transbank, lecturas críticas de stock/crédito), siempre con timeout explícito; todo lo demás circula por colas con DLQ y reintentos. El detalle de perfiles y contratos por contraparte (SII, ERP, cada cadena) se versiona y se prueba contra los bancos de prueba de cada contraparte.


## S5.9 Diccionario de Datos y Catálogo de Activos — P6.11

Cumplimiento de RT-05.01 (Obligatorio): diccionario de datos/catálogo documentado, por base lógica (S5.1), con formato estándar:


> **Tabla 145** — S5.9 Diccionario de Datos y Catálogo de Activos — P6.11 · 10 filas · ver planilla del subdocumento

El diccionario se publica en el catálogo de datos (activos de datos) con versionado; alimenta la matriz de trazabilidad del Cap. 17.1, habilita el linaje (RT-05.10, Deseable) sobre Redshift Serverless + S3, y acompaña la copia íntegra interoperable exigida por el Art. 85 al término del contrato. El numerador de cada atributo (nombre, tipo, dominio de valores, obligatoriedad, propietario y sensibilidad) queda cerrado en el entregable formal del diccionario previo a producción.


## S5.10 Evidencia de Entrega Digital y Acuse de Recibo Tributario — P6.12

Cumplimiento del criterio 8 del Cap. 18 (prueba de entrega digital disponible el mismo día; hoy guía en papel con 12 días para resolver un reclamo), de RT-16.14 (el receptor habitual es persona natural sin firma electrónica avanzada) y de la decisión de diseño 16.1 #15 (cómo se prueba la entrega cuando quien recibe no es el titular, no sabe firmar en pantalla o se niega):


> **Tabla 146** — S5.10 Evidencia de Entrega Digital y Acuse de Recibo Tributario — P6.12 · 5 filas · ver planilla del subdocumento

La evidencia capturada (firma, fotografías, QR) se conserva en S3 con Object Lock y retención de 6 años (inmutable, RT-16.07) y se articula con la guía de despacho electrónica (GDE) y su acuse de recibo conforme a la normativa tributaria vigente (SII) — el acuse de recibo de las mercaderías es el documento que da mérito ejecutivo a la factura, por lo que la solución no puede comprometer sus efectos legales. La firma se aplica conforme a la Ley 19.799 y RT-16.17/16.18 (verificación de validez del certificado al momento de la firma, sello de tiempo y evidencia de firma verificable después del vencimiento). La evidencia local se captura sin conexión; el documento se timbra al sincronizar con folio reservado por dispositivo (timbre diferido, RT-03.12) y el acuse se envía al cliente el mismo día (Cap. 18, criterio 8), con confirmación por mínimo tres canales (WhatsApp/SMS/push, correo, portal de consulta, RT-16.08). En el canal moderno, el acuse es digital por EDI (RF-12.13) dentro de la ventana acordada. El mecanismo completo de FID se actualiza en el mecanismo de consulta al mandante (Art. 43.3) y queda validado en la etapa de pruebas del Cap. 18.

Subdocumento 5 · Modelo y gestión de datos · Etapa preliminar · LafroX — Caso 02 Logística (Distribuidora Puelche S.A.). Fuentes: Lógica v6.2, ADR v02, Integración v01, Seguridad v01, Cloud v3.6, Dimensionamiento v05, Bases y Caso 02.

LAFROX

Propuesta de Solución — Distribuidora Puelche S.A.

Licitación N° TFEP-01/2026 — Caso 02 Logística

SUBDOCUMENTO 13

Innovaciones de la Propuesta

Informe 1
