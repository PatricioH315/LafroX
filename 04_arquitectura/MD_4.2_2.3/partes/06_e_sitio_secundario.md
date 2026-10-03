<a id="h-04-partes-4-3-centros-de-datos-06-e-sitio-secundario-tex-102"></a>

## 4.3.2 Especificaciones Data Center Secundario

<a id="sec-e-especificaciones-del-sitio-secundario-y-"></a>

El Data Center Secundario cubre dos dominios de recuperación. La región AWS us-east-1 restituye el dominio de nube ante la pérdida de sa-east-1. La plataforma de nube de la región activa restituye el WMS de Talca ante la pérdida de su sala técnica; si también se pierde sa-east-1, la región activa pasa a ser us-east-1 tras la promoción. Concepción y los cross-docking son sitios operacionales autónomos y no reciben la carga de Talca. Los objetivos para servicios críticos son RTO ≤ 4 h y RPO ≤ 15 min, con respaldo 3-2-1-1-0 y ensayos semestrales. El Formulario T-11 detalla los recursos de recuperación.

<a id="h-04-partes-4-3-centros-de-datos-06-e-sitio-secundario-tex-103"></a>

### 4.3.2.1 Modalidad del sitio secundario

La modalidad del dominio de nube es activo-pasiva en caliente. La región us-east-1 mantiene una réplica funcional de aplicación y datos con capacidad reducida; ante la declaración del incidente se promueve Aurora y se escala la aplicación. El dominio de Talca conserva en Aurora una copia continua de su WMS y la misma imagen `wms_only` lista para ejecutarse en ECS Fargate. ADR-09 (Anexo 4-O) registra la selección frente a activo-activo y a la restauración en frío. La primera alternativa exigiría coordinar escrituras simultáneas entre regiones; la segunda agrega la reconstrucción de la plataforma al tiempo de recuperación.

<a id="h-04-partes-4-3-centros-de-datos-06-e-sitio-secundario-tex-104"></a>

### 4.3.2.2 Región o sitio de recuperación

La Tabla [36](../../LAFROX-Subdocumento4.md#tab-4-3-3) compara los dos destinos de recuperación con sus distancias y amenazas comunes.

<a id="tab-4-3-3"></a>

**Tabla 36 — Destinos de recuperación: distancia y amenazas comunes**

| **Destino** | **Dominio** | **Distancia** | **Amenazas comunes** |
| --- | --- | --- | --- |
| AWS us-east-1 | Nube de sa-east-1 | ≈ 7.700 km desde sa-east-1 | No comparte sismicidad ni red eléctrica con Brasil. |
| Nube sa-east-1; us-east-1 en contingencia regional | WMS de Talca | ≈ 2.700 km de Talca a sa-east-1 | No comparte sismicidad ni suministro eléctrico con Talca. |

 Fuente: elaboración propia.

Las distancias de la tabla separan los dominios de falla. La región secundaria se sitúa en Virginia del Norte, Estados Unidos, y la primaria en São Paulo, Brasil. Ambas implican transferencia internacional de datos personales desde Chile. AWS actúa como encargado del tratamiento por cuenta del CLIENTE, responsable de los datos, mediante un contrato de encargo que incorpora las cláusulas contractuales tipo aprobadas para la Ley N° 21.719 (Ley N° 21.719, 2024). Los datos se cifran en reposo con claves KMS administradas por el CLIENTE y en tránsito; se registran las actividades de tratamiento y se controlan y auditan los accesos.

La réplica secundaria se limita a los datos necesarios para continuidad. La analítica opera en sa-east-1 y se copia de forma diferida a la región secundaria, porque conserva los cinco años de registros de temperatura y de trazabilidad de lote. Las posiciones de flota, que son geolocalización de personas trabajadoras, no salen de sa-east-1 y se protegen con copias inmutables en otra cuenta de esa región; ante la pérdida total de sa-east-1 se pierde su historial, que solo alimenta el costo de servir. La región secundaria no se utiliza para consultas de negocio durante la operación normal. El artículo 23 de las Bases Administrativas sujeta la residencia declarada a aprobación del CLIENTE (PUCV, 2026c, art. 23), hito contractual de la Etapa 1. Si el CLIENTE no aprueba Estados Unidos por estar fuera de Sudamérica, el parámetro de región secundaria de la infraestructura como código se cambia a otra región AWS aprobada por el CLIENTE que ofrezca Aurora Global Database, DynamoDB Global Tables, replicación de S3, ECS Fargate y AWS Backup; se conservan la arquitectura y los objetivos RTO y RPO. Si restringe una categoría no crítica a la región primaria, se excluye esa categoría de la réplica y se protege con copias inmutables en otra cuenta de la misma región. Las categorías críticas necesarias para recuperar el servicio se mantienen en una región secundaria aprobada.

<a id="h-04-partes-4-3-centros-de-datos-06-e-sitio-secundario-tex-105"></a>

### 4.3.2.3 Replicación

La replicación continua usa un mecanismo por dominio, resumido en la Tabla [37](../../LAFROX-Subdocumento4.md#tab-4-3-4).

<a id="tab-4-3-4"></a>

**Tabla 37 — Replicación y RPO por dominio de datos**

| **Dominio de datos** | **Mecanismo de replicación** | **RPO / retraso declarado** |
| --- | --- | --- |
| Transaccional en nube (crítico) | Aurora Global Database replica la base hacia la región secundaria. | El RPO objetivo es ≤ 15 min y se mide en cada ensayo. |
| WMS de Talca (crítico) | AWS DMS replica PostgreSQL VM-02 por la VPN sobre fibra, LTE o Starlink. | El RPO objetivo es ≤ 15 min y se mide en cada ensayo. |
| Mensajes críticos de cada sitio | El outbox local retiene los eventos y el shipper los reenvía a SQS FIFO de la región activa. | El RPO objetivo es ≤ 15 min y se mide en cada ensayo. |
| Evidencias y documentos tributarios (críticos) | S3 Replication Time Control replica los objetos entre regiones. | El RPO objetivo es ≤ 15 min para el 99,99 % de los objetos y se mide en cada ensayo. |
| Telemetría de temperatura (crítica) | DynamoDB Global Tables replica las lecturas entre regiones. | El RPO objetivo es ≤ 15 min y se mide en cada ensayo. |
| Analítica (no crítica) | Los respaldos se copian de forma diferida a la región secundaria aprobada. | El RPO es ≤ 24 h. |
| Posiciones de flota (no críticas) | Se conservan solo en sa-east-1, con copia inmutable en otra cuenta de esa región. | El RPO es ≤ 24 h dentro de sa-east-1. |
| Mensajes no críticos | El outbox local conserva los eventos para reenviarlos a la cola de la región activa. | El RPO es ≤ 24 h. |

 Fuente: elaboración propia.

La tabla separa la copia DMS del WMS de Talca, destinada a su recuperación, del estado central consolidado por eventos idempotentes de todos los sitios. AWS DMS lee VM-02 por el túnel IPsec; la única conexión iniciada desde la nube hacia un sitio termina en esa VM. Aurora Global Database, DynamoDB Global Tables y la replicación de S3 protegen el dominio de nube. S3 Replication Time Control ofrece que el 99,99 % de los objetos se replique en 15 min; se vigila la métrica de objetos pendientes y un evento de umbral superado dispara la recopia. DynamoDB Global Tables replica de forma asíncrona con retraso típico de segundos y una alarma de `ReplicationLatency` a los 60 s. La edad de las réplicas y las colas se mide continuamente y todos los RPO se verifican en los ensayos semestrales.

<a id="h-04-partes-4-3-centros-de-datos-06-e-sitio-secundario-tex-106"></a>

### 4.3.2.4 RPO y RTO

La Tabla [38](../../LAFROX-Subdocumento4.md#tab-4-3-5) fija los objetivos medidos en las pruebas de recuperación.

<a id="tab-4-3-5"></a>

**Tabla 38 — Objetivos de continuidad**

| **Activo** | **Objetivo** | **Valor declarado** |
| --- | --- | --- |
| Servicios críticos | Tiempo de recuperación (RTO) | ≤ 4 h |
| Servicios críticos | Punto de recuperación (RPO) | ≤ 15 min |
| Transacción crítica de extremo a extremo | Disponibilidad mensual | ≥ 99,9 % |
| Infraestructura por componente | Disponibilidad mensual | 99,95 % |

 Fuente: elaboración propia.

El RPO de la tabla se sustenta en la extracción continua de datos críticos por tres dominios de falla distintos en los CD: fibra terrestre D-03, red celular D-04 y satélite D-06. En Talca y Concepción, Starlink permanece encendido como tercer camino en espera caliente, con el túnel IPsec establecido y BGP con menor preferencia; toma el tráfico solo si fallan fibra y LTE. En esa situación, la calidad de servicio prioriza DMS y WAL de Talca, la salida del broker y el outbox, las guías hacia el ERP y el SII, la identidad y la telemetría crítica. El terminal encendido evita los minutos necesarios para adquirir satélites y negociar el túnel durante la falla, sin costo adicional por la tarifa plana. La caída simultánea de fibra y LTE, incluso ante un terremoto que afecte la infraestructura terrestre, permite mantener la réplica de Talca y la publicación de eventos dentro del RPO mediante Starlink. En los cross-docking, Starlink es el camino principal y LTE de dos proveedores constituye el respaldo. La bodega conserva 24 h de operación local aunque cambie el camino WAN.

Queda como riesgo residual la falla simultánea de los tres caminos seguida de la destrucción del sitio antes de reponer alguno: en esa secuencia, la última copia remota podría exceder 15 min. Se mitiga con alarmas de retraso de replicación a los 5 y 15 min, reposición del enlace por el proveedor, preemisión de guías al cerrar la carga y conservación local en el NAS WORM de Talca. La autonomía local de 24 h se mantiene durante la atención del incidente. El RTO se verifica levantando la misma imagen del WMS de Talca en Fargate de la región activa y conectando sus terminales por la VPN.

<a id="h-04-partes-4-3-centros-de-datos-06-e-sitio-secundario-tex-107"></a>

### 4.3.2.5 Procedimiento de conmutación

<a id="sub-conmutacion-regional"></a>

La pérdida regional se atiende con la secuencia de la Tabla [39](../../LAFROX-Subdocumento4.md#tab-4-3-6). La promoción de Aurora requiere autorización del CLIENTE; Route 53 cambia el tráfico solo después de restituir y validar los servicios.

<a id="tab-4-3-6"></a>

**Tabla 39 — Secuencia de conmutación de región**

| **Paso** | **Acción** | **Ejecución** | **Tiempo** |
| --- | --- | --- | --- |
| 1 | Detección por verificación de salud y alarmas | Route 53 y CloudWatch | < 5 min |
| 2 | Declaración del incidente y autorización de la promoción | CLIENTE, con aviso por SNS | ≤ 30 min |
| 3 | Promoción de Aurora en us-east-1 | Systems Manager Automation | 15–20 min |
| 4 | Escalado de la plataforma de aplicación a carga completa | Systems Manager Automation | ≤ 30 min |
| 5 | Restitución de Keycloak, API pública y privada y Verified Access | Systems Manager Automation | < 15 min |
| 6 | Validación funcional con escrituras de pedidos y sincronización de prueba | Operación | < 15 min |
| 7 | Cambio del tráfico a us-east-1 en Route 53, con TTL de 60 s preparado | Systems Manager Automation | < 5 min |
| 8 | Reconexión de túneles y brokers y redirección de shippers y `erp-sync` a las colas regionales | Systems Manager Automation | < 15 min |

 Fuente: elaboración propia.

El peor caso secuencial suma 5 + 30 + 20 + 30 + 15 + 15 + 5 + 15 = 135 min, equivalentes a 2 h 15 min y dentro del RTO de 4 h; el escalado del paso 4 puede ejecutarse en paralelo con la promoción del paso 3 sin reducir este presupuesto conservador. El plan de continuidad designa a un autorizador titular y a un suplente del CLIENTE con facultad delegada; si el titular no responde en 15 min, decide el suplente dentro del máximo de 30 min. La decisión se ensaya en los simulacros semestrales. Las imágenes de ECR se replican entre regiones y las colas SQS FIFO, SQS y SNS equivalentes existen vacías en la región secundaria por infraestructura como código, de modo que el paso 8 redirige allí los `shippers` y `erp-sync` sin depender de la región primaria. La preparación de los registros con TTL de 60 s antecede al incidente. No se conmuta automáticamente el tráfico por salud antes de promover la base; el retorno automático permanece deshabilitado. Cada paso queda registrado por Systems Manager y el personal del CLIENTE puede ejecutarlo tras la transferencia de conocimiento.

Cuando se pierde solo la sala de Talca, se detiene la tarea DMS, se habilita para escritura la copia del WMS de Talca en Aurora y se levanta el perfil `wms_only` de la misma imagen en ECS Fargate de la región activa. Los terminales y periféricos de Talca se conectan por VPN mediante fibra, LTE o Starlink. Si la región primaria tampoco está disponible, se promueve primero us-east-1 con la secuencia regional descrita y allí se levanta el perfil de Talca. Concepción continúa atendiendo exclusivamente su propia bodega.

<a id="h-04-partes-4-3-centros-de-datos-06-e-sitio-secundario-tex-108"></a>

### 4.3.2.6 Procedimiento de retorno

El retorno regional se realiza tras resincronizar las réplicas, conciliar las transacciones de la contingencia y transferir los eventos retenidos. La operación valida escrituras y consultas en la región primaria, cambia coordinadamente Route 53 y registra el tiempo real empleado. Cada ensayo semestral incluye el retorno.

Para devolver el WMS a Talca se reconstruye su clúster, se carga VM-02 desde Aurora y se invierte temporalmente el sentido de la replicación hasta igualar los datos. Se detienen las escrituras en nube, se verifica la igualdad, se habilita el escritor local y se reconectan los terminales al WMS del sitio. El corte de vuelta se realiza fuera de las ventanas protegidas.

<a id="h-04-partes-4-3-centros-de-datos-06-e-sitio-secundario-tex-109"></a>

### 4.3.2.7 Pruebas del plan de recuperación y respaldos

Dos veces al año se ensaya la pérdida regional con escrituras de pedidos y sincronización en us-east-1; con la misma frecuencia se simula la pérdida de la sala de Talca y se levanta su WMS en Fargate sobre la copia en Aurora. Se miden RTO y RPO en cada ensayo y se exige el cumplimiento del 100 % de ambos objetivos. La restauración mensual de respaldos y la inyección de fallas se describen en la sección [4.2.4.6](../../LAFROX-Subdocumento4.md#sub-6-verificacion-de-la-continuidad).
