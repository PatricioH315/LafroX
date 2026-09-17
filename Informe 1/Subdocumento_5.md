# **Capítulo 5 · Modelo y Gestión de Datos (Subdoc. 5\)**

## **5.1 Visión General del Modelo de Datos**

El modelo de datos de Puelche se organiza como **persistencia políglota por dominio** (ADR-04), que reconoce cuatro exigencias incompatibles entre sí y las reparte en motores especializados: el **transaccional** de preventa, reparto, bodega y cobranza exige **consistencia** y reconciliación determinista tras cortes; la **ingesta IoT** (sensores y termógrafos de cadena de frío) es **escritura masiva de baja latencia** con datos volátiles; la **serie de tiempo consolidada** de temperatura es **analítica columnar** con retención de 5 años; y la **evidencia documental** (POD, DTE) exige **inmutabilidad legal** durante 6 años. Un único motor no puede cumplir las cuatro posiciones CAP sin sacrificar desempeño (RT-05.02), y por eso el Cap. 15 del caso exige declarar motor y posición CAP por cada dominio.

El modelo de datos materializa el despliegue **híbrido** del Artículo 16°: el **maestro de bodega** vive **on-premise** (PostgreSQL \+ PostGIS por sitio, con autonomía 24 h sin enlace, RT-03.10) y se replica por CDC (WAL lógico) hacia **Amazon Aurora PostgreSQL** en sa-east-1, que concentra el OLTP de la nube (preventa, reparto, canal moderno, BI). El terreno opera **offline de primera clase**: las aplicaciones mantienen foto local de datos de lectura (stock, precios, crédito, rutas) y buffer de escrituras idempotente que se concilia al reconectar (RT-03.12), sin perder ni duplicar pedidos (Cap. 18, criterio 6).

La arquitectura de datos se describe conforme a ISO/IEC/IEEE 42010 y al diccionario por base lógica (RT-05.01), coherente con la arquitectura lógica v6.2 (Subdoc. 4.1) y con la arquitectura física (Subdoc. 4.2). La política de retención, archivado y eliminación se declara contra **RT-16.10** (el caso la rotula RT-05.10; el código transversal correcto es RT-16.10, desajuste que se responde en el T-12 y se eleva como consulta al mandante por Art. 43.3) — ver S5.6.

## **S5.1 Dominio de Información y Entornos de Datos — P6.1**

El **dominio de información** de la solución cubre la totalidad de los datos que produce la operación de Puelche: preventa y pedidos, inventario y bodega (2 CD \+ 3 cross-docking), preparación, reparto y entregas, cobranza y cartera, trazabilidad sanitaria y cadena de frío, telemetría de flota, canal moderno EDI, documentos tributarios SII, analítica de gestión y datos maestros. Volumetría de referencia (Tabla 14.1 y Cap. 15 del caso): **14.200 clientes**, **31.000 pedidos/mes** (260.000 líneas, 2,4 M unidades), **180 proveedores**, **\~34.000 DTE/mes**, **9.500 SKU** proyectados a tres años, telemetría de **28 sensores \+ 18 termógrafos** y **\~1.400 entregas/día** (peak de septiembre ≈ 2.600).

### Entornos de datos

| Entorno | Contenido | Tecnología |
| :---- | :---- | :---- |
| **On-premise por sitio (2 CD \+ 3 cross-dockings)** | Transaccional de bodega y operación local (recepción, inventario, preparación) — **maestro de bodega** (sucesor del WMS 2013\) con autonomía 24 h | **PostgreSQL \+ PostGIS** local por sitio, con réplica de continuidad |
| **Nube (OLTP cloud \+ réplica/DRP del maestro de bodega)** | Preventa, reparto, BI \+ réplica/DRP del maestro on-premise (CDC sobre WAL lógico) | **Amazon Aurora PostgreSQL** (réplica/DRP \+ OLTP cloud, no un segundo WMS) |
| **Ingesta IoT / telemetría en frío** | Lecturas de sensores y termógrafos (cadena de frío, −22 °C offline) | **Amazon DynamoDB** (raw, TTL 30 días) \+ AWS IoT Greengrass en borde |
| **Serie consolidada (OLAP)** | Telemetría de camiones, series de temperatura (consolidado 5 años) | **S3 Parquet ← AWS Glue ← DynamoDB raw (TTL 30 d)**; consulta **Redshift Serverless** (QuickSight) |
| **Cache / sesiones** | Stock caliente, precios, sesiones SSO, sync offline | **Redis — Amazon ElastiCache** (nube); la caché de turno vive en el dispositivo y la sesión sin conexión en el borde |
| **Documentos / adjuntos** | POD firmado, DTE, comprobantes, evidencia QR | **Amazon S3** (object storage/data lake, Object Lock) \+ caché local |
| **Analítica / BI (consolidada nube)** | OTIF, costo de servir, BI/gerencia, históricos | **Amazon Redshift Serverless** (OLAP), alimentado desde **S3 → Glue (ETL) — nunca directo a Aurora** (S19) |

### Bases/almacenes lógicos con nombre — 15 bases lógicas (no 15 servidores, S18)

| \# | BD | Dominio | Guarda |
| :---- | :---- | :---- | :---- |
| 1 | **BD\_INVENTARIO** | Almacén e inventario | Recepción, ubicaciones, stock por posición, slotting, conteo, lotes |
| 2 | **BD\_PREVENTA** | Venta y pedidos | Preventistas, pedidos offline (UUID), stock/crédito, promociones |
| 3 | **BD\_RUTAS** *(PostGIS)* | Planificación y geocercas | Rutas, secuenciación, ventanas, capacidad, geometrías/geocercas |
| 4 | **BD\_PREPARACION** | Bodega / picking | Misiones de picking, escaneo GS1, faltantes, secuenciación térmica |
| 5 | **BD\_REPARTO** | Despacho y entrega | Guías, POD, QR, firmas, estados, devoluciones en ruta |
| 6 | **BD\_COBRANZA\_FINANZAS** | Cobranza y cartera | Rendición, cartera de crédito, causales de descuadre, POS, costo de servir |
| 7 | **BD\_MAESTROS\_CONF** | Maestros y configuración | Catálogo de productos, clientes, bodegas, usuarios, parámetros |
| 8 | **BD\_GOBIERNO\_ACCESO** | Seguridad / IAM | Roles, permisos, sesiones, auditoría de acceso, OTP externos |
| 9 | **BD\_CALIDAD\_TRAZABILIDAD** | Calidad y trazabilidad | Lotes, sensor de frío, excursiones, trazabilidad forward-backward, control sanitario |
| 10 | **BD\_TELEMETRIA** *(OLAP: S3→Glue→Redshift)* | Flota / series de tiempo | Posición/velocidad GPS, eventos de ruta, series de temperatura |
| 11 | **BD\_EDI\_CANALMODERNO** | Canal moderno EDI | Pedidos EDI (AS2/API), excepciones, ASN, acuses, integración cadenas |
| 12 | **BD\_BI\_GERENCIA** *(analítica nube)* | Analítica / reportes | OTIF, costo de servir, ocupación de flota, segmentación, tableros |
| 13 | **BD\_MAILS\_NOTIF** | Notificaciones | Colas de avisos (SMS/WhatsApp/push), bitácora de envío |
| 14 | **REDIS\_SESIONES\_CACHE** *(Redis, solo nube)* | Cache / sesiones | Stock caliente, precios, sesiones SSO, sincronización offline |
| 15 | **S3\_DOCS** *(S3)* | Documentos / adjuntos | POD firmado, DTE, comprobantes, evidencia QR |

Multi-sitio por parametrización topológica (RF-02.02, RT-02.12): cada CD informa su stock al consolidado; un nuevo sitio se incorpora replicando la plantilla del clúster sin rediseño del modelo de datos.

## **S5.2 Motor y Paradigma de Persistencia por Dominio (CAP) — P6.2**

Justificación de paradigma y motor conforme a **RT-05.02** (Obligatorio). **Decisión: AP con consistencia eventual reconciliada — consistencia fuerte solo donde el negocio lo exige.**

| Clase de dato | Motor | Paradigma / garantías | Posición CAP | Justificación de negocio |
| :---- | :---- | :---- | :---- | :---- |
| **Stock / crédito (reserva y validación)** | PostgreSQL (on-prem) \+ Aurora (nube) | Relacional, ACID | **CP** (consistencia fuerte) en ruta síncrona por Gateway; offline el preventista usa **caché de turno** y la reserva se confirma en sync | Doble compromiso de stock es el riesgo \#1 (decisión 16.1 \#8); la regla se aplica en el servidor, no con timestamp ciego (S26) |
| **Pedidos / entregas / POD / cobros** | Aurora \+ PostgreSQL | Relacional, ACID \+ idempotencia (UUID) | **AP** con UUID \+ dedupe (RT-02.06/07): la escritura offline nunca se pierde, se reconcilia | Terreno sin señal hasta 14 h (RT-03.10); exigir consistencia fuerte en terreno \= dejar de operar |
| **Trazabilidad de lote / temperatura** | PostgreSQL \+ S3 Parquet/Redshift | Relacional \+ columnar (eventos) | **AP** con orden garantizado por partición (SQS FIFO/colas) \+ deduplicación | El registro continuo es evidencia; el orden por lote se preserva; la lectura consolidada ocurre en la fuente de verdad (servidor) |
| **Ingesta IoT / telemetría raw** | DynamoDB | No relacional, clave-valor, TTL | **AP** (eventual, TTL corto de 30 días) | Escritura masiva de baja latencia sin saturar el transaccional (RNF-11.02) |
| **Serie de tiempo consolidada** | S3 Parquet \+ Redshift Serverless | Columnar (OLAP) | **AP columnar** | Retención sanitaria 5 años, compresión y consulta por rango; **OLAP por diseño** (D2), sin segundo motor |
| **Configuración / parámetros (RF-02.02)** | PostgreSQL (BD\_MAESTROS\_CONF) | Relacional, ACID | **CP** (una versión vigente por topología, RT-02.12) | Un parámetro divergente corrompe inventario; versionado \+ aprobación |
| **Analítica (M10)** | Redshift Serverless | Columnar (modelo dimensional) | **Eventual** por diseño (separación transaccional/analítico) | Los tableros leen del almacén con latencias comprometidas, nunca del transaccional en vivo |
| **Notificaciones** | Colas (RabbitMQ/SQS) | Mensajería asíncrona | **AP** (colas) | Asíncrono por diseño; entrega diferida sin pérdida |

Decisión de motor por dominio (decisión 16.1 \#18): el volumen total es manejable en PostgreSQL con **índices \+ PostGIS** para georreferencia; DynamoDB absorbe el pico IoT; la serie consolidada vive en la capa OLAP (S3 Parquet → Redshift) y **no** se añade un motor de series dedicado (InfluxDB descartado: segundo motor a operar con un equipo TI de 4 personas — D2). El detalle de alternativas evaluadas y su fundamento está en ADR-04.

## **S5.3 Migración, Saneamiento, Validación y Conciliación — P6.3**

### Alcance y volúmenes por migrar (RT-05.11/05.15; valores del Cap. 15 del caso)

| Dato histórico | Volumen/alcance a migrar | Retención posterior a la migración |
| :---- | :---- | :---- |
| **Maestros** — clientes, productos y proveedores | **Completos** | Vigentes \+ consulta histórica |
| **Ventas y pedidos** | **3 años** | Consulta solo lectura durante el contrato |
| **Inventario y movimientos** | **2 años** | Ídem |
| **Trazabilidad sanitaria** | **5 años** | Ídem (piso RSA D.S. 977/96) |
| **Cuentas por cobrar** | **Saldos vivos más 2 años** | Ídem |
| **Bodega (SKU, ubicaciones, saldos)** — maestros del WMS 2013 | Completos | Migrados a la BD on-prem del maestro de bodega (S5.1); históricos ERP/WMS **consultables en modo solo lectura** durante todo el contrato |

### Metodología (RT-05.11 a RT-05.15)

1. **Perfilado y saneamiento previo (RT-05.12):** etapa de perfilado sobre los datos de origen (ERP 2017, WMS 2013, planillas) con **informe de defectos detectados y decisión sobre cada uno** (corregir / aceptar c/registro / excluir). Casos de saneamiento esperados y declarados: **duplicados de cliente por RUT** (maestro único resultante, MDM S5.6), **campos de lote en texto libre o vacíos** (el retiro de marzo mostró 41 % de recepciones sin lote), **equivalencias de maestro entre cadenas** (GTIN por cadena, RF-12.03) y **saldos de envases** (68.000 canastillos y 9.400 pallets sin control).  
2. **Reglas de transformación y carga verificada:** carga de datos maestros con **validación en el punto de captura** y conciliación por recuentos; carga inicial transaccional por olas por sitio con estrategia azul-verde y plan de reversión.  
3. **Dos ensayos completos de migración sobre Preproducción (RT-05.13):** con medición del tiempo total y del resultado de la conciliación; ensayo T \+ reensayo tras corrección.  
4. **Conciliación cuantitativa y verificable (RT-05.14):** **recuentos, sumas de control y muestreo dirigido**; toda diferencia queda **explicada** y registrada en la bitácora de reconciliación (Art. 16.4). La reposición del conteo cíclico apuntala la exactitud del stock migrado (diferencia de 2,3 % → meta \< 1 %).  
5. **Históricos no migrados (RT-05.15):** quedan **accesibles en repositorio de consulta solo lectura** durante el período de retención del caso, sin depender del sistema legado; exportables bajo el régimen del Art. 85 (copia íntegra en formato interoperable con diccionario).  
6. **Coexistencia con el WMS 2013 (D10):** el legado queda detrás de la misma ACL con tabla de «capacidad absorbida» (recepción GS1, slotting, misiones con HHT, conteo cíclico) que se **vacía ola a ola por sitio**, con estrategia azul-verde, plan de reversión y retiro al cierre de la Etapa 1\.

## **S5.4 Desempeño del Modelo de Datos: Indexación, Particionamiento y Caché — P6.4**

### Indexación

* **Índices y claves en PostgreSQL/Aurora:** FKs en todas las tablas transaccionales; índices por **lote GS1 (GTIN \+ lote \+ vencimiento)**, **SSCC** y shipment\_id (estructura que sostiene el retiro \< 2 h), y **PostGIS GiST** para geometrías, rutas y geocercas (BD\_RUTAS, BD\_TELEMETRIA). Índices compuestos de trazabilidad forward/backward en BD\_CALIDAD\_TRAZABILIDAD.  
* **Réplicas de solo lectura** en Aurora para consultas de negocio sin competir con la escritura del maestro (2 lectores; RT-09.05).  
* **Redshift**: distribución por clave de negocio (ruta/lote) y compresión columnar sobre hechos (ventas, entregas, stock, costo de servir) y dimensiones (cliente, SKU, tiempo, ruta, canal).

### Particionamiento

* **Particionado mensual de transacciones de bodega** (recepción, misiones, despacho) en PostgreSQL on-prem, primer remedio declarado ante el cuello de botella de escritura de la ventana 05:30–07:00 (RT-09.05; escala vertical → particionado \+ PgBouncer → réplica de lectura → 4.º nodo/sharding).  
* **Orden garantizado por partición** en mensajería (SQS FIFO con MessageGroupId \= sitio/entidad) para reconciliación cross-sitio y eventos de trazabilidad (RT-02.07); el sync de terreno usa **partición y reanudación (chunking)** para cumplir ≤ 10 min de turno / ≤ 2 h de CD tras reconexión.  
* **DynamoDB** con TTL por partición (30 días) para telemetría raw; la serie consolidada se particiona en S3 Parquet por mes (5 años). El hub EDI **particiona por cadena** (perfiles de configuración, no desarrollo).

### Caché

* **Redis — Amazon ElastiCache** (N-07): **stock caliente, precios y sesiones SSO** para latency de stock/crédito \< 2 s en preventa (RT-09.01); patrón cache-aside con regeneración transparente \< 15 min ante pérdida (el OLTP soporta la carga transicional).  
* **Caché de turno precargada en el dispositivo** (saldo, stock, tarifa; RT-17.03): foto local que sostiene el turno completo sin señal dentro de un consumo objetivo ≤ 8–12 MB/turno.  
* **Caché local de identidad A-05** (Keycloak, TTL 8 h bodega / 14 h reparto) para autonomía sin red.  
* **Caché de tableros** (QuickSight, TTL) en las consolas locales de contingencia (RT-03.13); **S3 Intelligent-Tiering** para objetos de lectura fría.

### Optimización operacional

* **PgBouncer** (pool de conexiones) y pre-generación nocturna de documentos de despacho y validaciones batch (crédito/stock) para descargar la ventana crítica.  
* Umbrales RT-09.01 cumplidos bajo carga de la ventana y verificados en marcha blanca: **confirmación de línea de picking ≤ 1 s** (lectura local PostgreSQL \+ HHT con misión descargada), **registro de entrega ≤ 2 s**, **línea de preventa ≤ 1,5 s** y **consulta stock/crédito ≤ 2 s**, en P95 frente al dimensionamiento de \~105 TPS base (\~315 × 3× de crecimiento a tres años, RT-09.03).

## **S5.5 Separación Transaccional / Analítica — P6.5**

Cumplimiento de **RT-05.05** (Obligatorio): el almacenamiento transaccional y el analítico están **separados por diseño** y **ninguna consulta analítica puede degradar la operación**.

| Exigencia | Cumplimiento |
| :---- | :---- |
| **RT-05.05 / separación** | La analítica **nunca** lee del transaccional (S19): el almacén (BD\_BI\_GERENCIA, S3 Parquet → Glue → Redshift Serverless) es la única vía de M10 (BI), alimentado por **eventos incrementales (Capa 5\)**; generadores de flujo procesan fuera de la ventana crítica (S19) |
| **RT-05.26 / modelo dimensional** | Hechos (ventas, entregas, stock, costo de servir) y dimensiones (cliente, SKU, tiempo, ruta, canal) en esquema estrella sobre Redshift Serverless |
| **RT-05.29 / latencia (valores del Cap. 15\)** | **Operación del día ≤ 5 min** (stream de eventos → tabla de agregados) · **cierre comercial ≤ 2 h** tras el retorno del último camión · **gestión ≤ 4 h**. De no fijar valores el capítulo, rige el tope transversal de 4 h |
| **RT-05.27 / autoservicio** | Self-service BI con **modelo semántico** en lenguaje de negocio (OTIF, fill rate, costo por entrega); usuarios \= Gerencia y Jefes, con aislamiento y auditoría de consultas |
| **RT-05.28 / informes y exportación** | Informes programables (diario/semanal/mensual) \+ **exportación asíncrona firmada con checksum** desde el portal; descarga regulatoria a CSV/Parquet con registro del solicitante |
| **RT-05.29 / drill-down** | Drill-down hasta **línea de pedido y lote** (resolución completa de trazabilidad sanitaria; retiro \< 2 h, Cap. 18\) |

El cumplimiento de las latencias se mide con **SLO en la Capa 8** (observabilidad única) y se verifica con pruebas de desempeño en la marcha blanca.

## **S5.6 Calidad, Retención, Archivado y Eliminación Segura — P6.6 y P6.9**

### Calidad de datos (RT-05.04, Obligatorio — marco ISO/IEC 25012, adoptado)

| Característica 25012 | Regla aplicada en Puelche | Dónde se verifica |
| :---- | :---- | :---- |
| Exactitud | Conteo cíclico: diferencia **de 2,3 % a \< 1 %**; conciliación de saldos por CD | M2/M5, proceso cíclico |
| Completitud | Todo pedido/entrega con UUID y estado; **cero pedidos perdidos/duplicados** (Cap. 18\) | Sync (Capa 3\) \+ dedupe |
| Consistencia | Reglas de negocio únicas (crédito, excursión, precio) aplicadas en el servidor; bitácora de reconciliación (Art. 16.4) | Capa 4 \+ Capa 8 |
| Puntualidad | Sync de turno ≤ 10 min; analítica día ≤ 5 min · cierre ≤ 2 h · gestión ≤ 4 h | SLO en Capa 8 |
| Integridad (referencial) | FKs y eventos canónicos (S8.6 de la lógica); validación en la ACL de integraciones | Hooks de integridad \+ pruebas de contrato |
| Trazabilidad | Toda escritura con actor/equipo/dispositivo y timestamp; lote GS1 completo (RT-05.03) | Registros inmutables (RT-16.07) |

Las reglas de calidad se declaran en el **diccionario** (RT-05.01) y se monitorean con **controles automáticos** (duplicados, saltos de secuencia, totales de conciliación) en la Capa 8; el incumplimiento genera tarea en el flujo de excepciones. **Tablero de calidad disponible para el CLIENTE** (RT-05.04).

### Retención, archivado y eliminación (RT-16.10, valores del Cap. 15 del caso)

| Clase de dato | Retención mínima |
| :---- | :---- |
| Documentos tributarios y su respaldo (DTE, guía de despacho electrónica) | **6 años** (plazo legal SII) |
| Registros sanitarios y trazabilidad de lote | **Vida útil del producto \+ 6 meses, con mínimo de 5 años** |
| Registros de temperatura | **5 años** |
| Evidencia de entrega (POD, firma, fotografía, QR) | **6 años** |
| Geolocalización de personas | **12 meses** (Ley 21.719, RT-11.10) — excluida de la replicación transfronteriza (S14) |
| Eventos de seguridad | 12 meses en línea \+ 24 en archivo |
| Auditoría de negocio | 7 años |

El caso rótula este requisito **RT-05.10**, pero el código transversal correcto es **RT-16.10** (RT-05.10 es «catálogo de datos con linaje», Deseable). El desajuste se responde en el T-12 contra RT-16.10 y se declara como **consulta al mandante (Art. 43.3)**, sin alterar los períodos.

**Implementación de retención e inmutabilidad:**

| Clase | Medio | Mecanismo |
| :---- | :---- | :---- |
| DTE / guías / facturas | S3 s3-documents-legal con **Object Lock (modo Compliance, 6 años \= 2.190 días)** → Glacier Deep Archive desde el año 2; metadatos (folio, fecha, estado, referencias) en Aurora | Sin posibilidad de eliminación prematura |
| Traza de lote y temperatura | BD\_CALIDAD\_TRAZABILIDAD (PostgreSQL) \+ **S3 Parquet inmutable (5 años)** \+ Redshift | Registros inmutables (RT-16.07) |
| POD / evidencia de entrega | S3 Object Lock (6 años) | Ídem |
| Telemetría raw | DynamoDB con **TTL 30 días** → consolida en S3 Parquet | TTL automático |
| Geolocalización de personas | Solo sa-east-1, **cifrado a nivel de campo** (RT-11.10) | Retención 12 meses; eliminación certificada al vencimiento |
| Respaldos | Aurora **PITR 35 días**; PostgreSQL on-prem respaldo diario \+ WAL; esquema **3-2-1-1-0** (NAS local \+ pierna inmutable nube \+ réplica us-east-1) | Pruebas semestrales (Art. 20 / RT-07.07) |

**Eliminación segura (RT-05.07, Obligatorio):** procedimiento verificable de eliminación al vencimiento del plazo con **registro inalterable** (RT-16.07); borrado seguro de medios que salen de servicio y disposición final con gestor autorizado. **Exportabilidad (RT-05.06, Obligatorio):** la totalidad de la información del CLIENTE se exporta en **formatos abiertos y documentados** (CSV, JSON, Parquet con el diccionario), en cualquier momento del contrato, **sin costo y sin intervención del proponente**. **Fin del contrato (Art. 85 BA / RT-05.08):** entrega de **copia íntegra en formato interoperable con diccionario** y **eliminación certificada** de los datos del mandante, con directorio de tratamiento actualizado y auditoría.

## **S5.7 Trazabilidad Sanitaria: Unidad de Trazabilidad y Retiro \< 2 Horas — P6.7 y P6.8**

### Unidad de trazabilidad sanitaria (decisión 16.1 \#2; interrogante S16.3, núm. 2; D11)

**La identidad primaria de la trazabilidad es el lote del proveedor en estándar GS1: GTIN \+ número de lote \+ fecha de vencimiento (con los rangos térmicos RF-09.01).** La **unidad logística (SSCC)** se enlaza al lote en **cada movimiento interno** de Puelche (recepción → ubicación → picking → unidad de despacho). Se descartan **caja y pallet como identidad primaria** por la volumetría (\~9.500 SKU, 2,4 M unidades/mes) y por el estado real de la captura (41 % de recepciones del producto del retiro sin lote): el problema es la **captura**, no el nivel de agregación; por eso la recepción exige **lectura del lote del proveedor (RF-01)**, el 100 % de las recepciones registra el lote de los productos que lo requieren (Cap. 18, criterio 2\) y la etiqueta SSCC se imprime al armar la unidad logística (RF-01.07).

### Modelo de trazabilidad

* **Evento a evento conforme a GS1 EPCIS** (RT-05.23): cada movimiento genera un evento idempotente en la cadena (recibido, ubicado, preparado, despachado, entregado) con actor, equipo/dispositivo, timestamp y **valores anteriores y posteriores** (RT-05.03); los eventos se conservan como registros inmutables (RT-16.07).  
* **Bidireccionalidad completa:** *forward* — desde un lote del proveedor se responde **con evidencia y no con estimación** a qué clientes llegó, en qué fecha, en qué cantidad y con qué documento tributario; *backward* — desde una unidad en el local del cliente hasta la **recepción que la originó** (Cap. 9.5 del caso).  
* **Drill-down hasta línea de pedido y lote** en la analítica (RT-05.29).  
* **Retiro sanitario \< 2 horas** (Cap. 18, criterio 1; situación actual: 9 días con resultado estimado): la consulta recorre BD\_CALIDAD\_TRAZABILIDAD con índices por lote/SSCC sobre la fuente de verdad consolidada (PostgreSQL \+ S3 Parquet), con SLO de respuesta y **evidencia exportable ante la autoridad**.  
* **Registro continuo de temperatura** en cámaras y vehículos (Cap. 18, criterio 3; hoy 3 lecturas manuales por viaje), con detección de excursión en el borde y regla escrita de bloqueo (decisión 16.1 \#4).

### Gobernanza de trazabilidad

Los eventos se publican por la Capa 5 (orden por partición, deduplicación) y alimentan la lectura consolidada en el servidor; la **bitácora de auditoría** (RT-16.07) registra toda operación con quién, qué, cuándo, dispositivo y valores previos/posteriores, lo que sostiene la trazabilidad del dato de negocio (RT-05.03) además de la trazabilidad de lote. La matriz de trazabilidad del Cap. 17.1 conserva la relación origen → requerimiento → componente → prueba de cada dato.

## **S5.8 Estándares GS1, EDI y Formato de la Autoridad Tributaria — P6.10**

Cumplimiento de **RT-05.23** (estándares sectoriales; llamada del caso en Cap. 16.2):

| Estándar / formato | Uso en la solución |
| :---- | :---- |
| **GS1 — identificación** | **GTIN** (producto/SKU, catálogo único \+ rangos térmicos), **SSCC** (unidad logística, etiqueta GS1-128 impresa en andén con AI 01/10/17/11), **GLN** (ubicaciones de la red de 6 instalaciones y puntos de entrega del canal moderno) |
| **GS1 — simbologías** | Códigos de barras 1D/2D con **GS1 DataBar** y GS1-128, leídos con terminales Zebra (DataWedge), escáneres DS2208 y lectores SE58/SE4100; resolución garantizada a lo largo de la cadena |
| **GS1 — trazabilidad de eventos** | **EPCIS** para los eventos de trazabilidad forward/backward (S5.7), intercambiados a través del hub EDI |
| **EDI con cadenas (canal moderno)** | **EANCOM D.01B / GS1 XML** (pedido, aviso de despacho, factura y acuse) vía **hub EDI centralizado con modelo canónico y capa anticorrupción** (ADR-11): una cadena nueva se incorpora por **configuración de perfil** y equivalencias GTIN (RF-12.03), no por desarrollo; ventana 30 min (RF-12.10); ASN antes del despacho; bandeja de excepciones operada por actor canónico (RF-12.06) |
| **Formato de la autoridad tributaria (SII)** | **DTE, guía de despacho electrónica y acuse de recibo** en el formato y firma que exige el SII (firma Ley 19.799, sello de tiempo y evidencia de firma verificable aun vencido el certificado, RT-16.18); **timbre diferido con folio reservado por dispositivo** cuando no hay conexión — la entrega no se detiene y no se emite guía de papel (RF-06.02) |

La integración sigue el principio **asíncrono por defecto, síncrono por excepción**: lo síncrono queda restringido a los actos que lo exigen (DTE al SII, autorización de pago Transbank, lecturas críticas de stock/crédito), siempre con timeout explícito; todo lo demás circula por colas con DLQ y reintentos. El detalle de perfiles y contratos por contraparte (SII, ERP, cada cadena) se versiona y se prueba contra los bancos de prueba de cada contraparte.

## **S5.9 Diccionario de Datos y Catálogo de Activos — P6.11**

Cumplimiento de **RT-05.01** (Obligatorio): diccionario de datos/catálogo documentado, **por base lógica** (S5.1), con formato estándar:

| Campo del diccionario | Contenido |
| :---- | :---- |
| Base lógica / objeto | BD\_\* (S5.1), tabla/vista, esquema |
| Definición de negocio | Significado en Puelche (trazable al RF) |
| Tipo / longitud / nulos / PK-FK | Perfil técnico |
| Linaje y origen | ¿Nace en transaccional (Mx), en integración (Capa 5\) o en analítica? (RT-05.10, Deseable) |
| **Dueño del dato** | Módulo dueño (trazable a la matriz del Cap. 17.1) |
| Reglas | Regla de negocio asociada (crédito, excursión, envases, FEFO) |
| **Retención** | Según S5.6 (5 años traza/temperatura, 6 años POD/DTE, 12 meses geolocalización) |
| Calidad | Regla y umbral de calidad (ISO/IEC 25012, RT-05.04) |
| **Sensibilidad** | ¿Dato personal? (Ley 19.628 / Ley 21.719, cifrado a nivel de campo RT-11.10) |

El diccionario se publica en el **catálogo de datos** (activos de datos) con **versionado**; alimenta la matriz de trazabilidad del Cap. 17.1, habilita el linaje (RT-05.10, Deseable) sobre Redshift Serverless \+ S3, y acompaña la **copia íntegra interoperable** exigida por el Art. 85 al término del contrato. El numerador de cada atributo (nombre, tipo, dominio de valores, obligatoriedad, propietario y sensibilidad) queda cerrado en el entregable formal del diccionario previo a producción.

## **S5.10 Evidencia de Entrega Digital y Acuse de Recibo Tributario — P6.12**

Cumplimiento del criterio 8 del Cap. 18 (prueba de entrega digital disponible el mismo día; hoy guía en papel con 12 días para resolver un reclamo), de **RT-16.14** (el receptor habitual es persona natural **sin firma electrónica avanzada**) y de la decisión de diseño 16.1 \#15 (cómo se prueba la entrega cuando quien recibe **no es el titular, no sabe firmar en pantalla o se niega**):

| Situación de recepción | Mecanismo de evidencia |
| :---- | :---- |
| **Receptor titular con firma** | **Firma en pantalla** (gesto) capturada offline en el dispositivo, vinculada a la entrega (RF-06.11) |
| **Quien recibe no es el titular** | Firma del receptor \+ **identificación registrada** (nombre, rol y RUT cuando corresponda) \+ fotografía de contexto |
| **No sabe firmar en pantalla** | **Fotografía de la recepción** \+ captura de identidad \+ QR de la entrega; no se condiciona la validez a la firma |
| **Se niega a firmar** | Registro de la negativa en el dispositivo \+ **fotografía y QR** \+ devolución/reintento conforme a la regla de local cerrado (decisión 16.1 \#3); la causal queda registrada al momento |

La evidencia capturada (firma, fotografías, QR) se conserva en **S3 con Object Lock y retención de 6 años** (inmutable, RT-16.07) y se **articula con la guía de despacho electrónica (GDE) y su acuse de recibo conforme a la normativa tributaria vigente (SII)** — el acuse de recibo de las mercaderías es el documento que da mérito ejecutivo a la factura, por lo que la solución **no puede comprometer sus efectos legales**. La firma se aplica conforme a la **Ley 19.799** y **RT-16.17/16.18** (verificación de validez del certificado al momento de la firma, sello de tiempo y evidencia de firma verificable después del vencimiento). La evidencia local se captura **sin conexión**; el documento se timbra al sincronizar con **folio reservado por dispositivo** (timbre diferido, RT-03.12) y el acuse se envía al cliente el mismo día (Cap. 18, criterio 8), con confirmación por mínimo tres canales (WhatsApp/SMS/push, correo, portal de consulta, RT-16.08). En el canal moderno, el acuse es **digital por EDI (RF-12.13)** dentro de la ventana acordada. El mecanismo completo de FID se actualiza en el mecanismo de consulta al mandante (Art. 43.3) y queda validado en la etapa de pruebas del Cap. 18\.

*Subdocumento 5 · Modelo y gestión de datos · Etapa preliminar · LafroX — Caso 02 Logística (Distribuidora Puelche S.A.). Fuentes: Lógica v6.2, ADR v02, Integración v01, Seguridad v01, Cloud v3.6, Dimensionamiento v05, Bases y Caso 02\.*

