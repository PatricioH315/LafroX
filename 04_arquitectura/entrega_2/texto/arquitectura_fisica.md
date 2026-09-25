# Capítulo 4 · Arquitectura Física y de Despliegue de la Solución (Parte 4.2) {-}

*Parte 4.2 del subdocumento 4. La arquitectura lógica es la parte 4.1 y se entrega por separado; ambas comparten el registro de decisiones y la volumetría, y se leen juntas.*

## Visión general de la arquitectura física

La arquitectura física materializa el despliegue híbrido obligatorio del Artículo 16° de las Bases Administrativas. La carga principal corre en nube pública AWS, con la región primaria en sa-east-1 (São Paulo, Brasil) y la recuperación ante desastres en us-east-1 (Norte de Virginia, EE. UU.). Los componentes on-premise garantizan la continuidad de la operación de bodega, plataformas y terreno durante cortes del enlace.

La red de instalaciones de la solución son 5 instalaciones en cuatro regiones. La proyección del caso a tres años incorpora una sexta instalación, sin requerir cambios en desarrollo o en crecimiento de servidores en CD Talca.

Los principios que gobiernan el diseño son los siguientes:

- **Carga principal en nube:** El núcleo transaccional de preventa, reparto y canal moderno, la analítica, la integración y el almacenamiento consolidado se ejecutan en AWS sa-east-1, con escalado elástico para el peak de septiembre.
- **Autonomía total de la operación de bodega:** El picking, despacho, recepción y conteo corren siempre contra los servidores del centro de distribución, no contra la nube. La conexión a internet no interviene en la operación de bodega.


## Modelo de emplazamiento híbrido

La solución se despliega en dos dominios, la nube pública y el on-premise, conectados por túneles VPN cifrados. Cada dominio puede operar de forma independiente cuando el enlace no está disponible.

### Dominio nube (AWS sa-east-1)

La nube concentra la carga principal de la solución. Todos los servicios se despliegan en al menos dos zonas de disponibilidad dentro de la región sa-east-1, de modo que la caída de un centro de datos de AWS no interrumpe la operación. La aplicación Django corre en contenedores ECS Fargate y atiende los procesos de preventa, reparto, canal moderno y el portal de clientes. Aurora PostgreSQL almacena la base de datos transaccional maestra y recibe en tiempo real las transacciones que se originan en las bodegas a través del servicio de replicación DMS CDC.

Todo el tráfico externo ingresa por API Gateway, donde WAF v2 valida las solicitudes y Shield protege contra ataques de denegación de servicio, antes de que el tráfico alcance la aplicación. Cuando las bodegas reconectan tras un corte de enlace, las transacciones pendientes llegan a la cola SQS FIFO, que las procesa en el orden exacto en que ocurrieron y sin duplicados. Cuando la aplicación registra un hecho relevante una entrega confirmada, una excursión térmica o un pedido del canal moderno, Celery despacha las tareas derivadas: enviar la notificación al cliente, actualizar los tableros analíticos, emitir el documento tributario al SII y, en la etapa de cadenas de supermercados, transmitir el acuse por EDI.

La telemetría de cadena de frío llega desde los gateways Greengrass en las bodegas hasta IoT Core en la nube. La capa analítica se apoya en Redshift Serverless para consultas históricas de hasta 5 años, y QuickSight publica los tableros de gestión del CLIENTE. La observabilidad se consolida en CloudWatch, que recibe logs, métricas y trazas tanto de los servicios en nube como de los colectores on-premise cuando estos disponen de enlace, y expone los tableros de operación sin infraestructura adicional que mantener. La identidad la gobierna Keycloak, que corre como servicio maestro en Fargate y distribuye las credenciales hacia las cachés locales de cada sitio. Una réplica pasiva de la infraestructura crítica en us-east-1 sostiene la recuperación ante desastres.

### Dominio on-premise

Cada centro de distribución mantiene su propia pila local: la misma aplicación Django corre en modo WMS contra una base PostgreSQL 16 local, un broker RabbitMQ que encola las transacciones y una caché de Keycloak que sostiene la sesión de los operarios. En CD Talca, un clúster Proxmox VE de 3 nodos con almacenamiento Ceph aloja las VMs (VM-01 a VM-06); en CD Concepción, un servidor de borde replica la misma pila en formato reducido (VM-C01 a VM-C04). Los tres cross-docking (Curicó, Chillán y Los Ángeles) operan con un mini-PC industrial que corre el WMS en Docker. La capa anticorrupción del ERP (VM-04, Talca) es la única puerta hacia el sistema legado. Los gateways IoT Greengrass procesan la cadena de frío en el borde, con detección de excursión térmica y bloqueo de despacho 100 % local. Un NAS cifrado (D-05) guarda la pierna local de respaldo 3-2-1-1-0.

### Conexión entre dominios

Los dos dominios se conectan mediante túneles VPN IPsec Site-to-Site cifrados, terminados en firewalls de borde en el lado on-premise y en AWS VPN Gateway en el lado nube, con enrutamiento dinámico BGP que conmuta automáticamente entre enlaces en menos de 30 segundos. Los centros de distribución disponen de fibra óptica como enlace principal y LTE empresarial como respaldo; los cross-docking, que operan en naves industriales sin cobertura de fibra, usan Starlink como enlace principal y LTE como respaldo.

#### Flujos entre nube y on-premise

Por diseño Zero Trust, las conexiones entre los dos dominios fijos, la nube y el on-premise, se inician siempre desde el on-premise hacia la nube. Existen dos excepciones declaradas a esta regla. La primera es DMS, que lee el registro de escritura anticipada de PostgreSQL para replicar los cambios hacia Aurora. La segunda es celery-erp-sync, que consulta la capa anticorrupción del ERP. Ambas conexiones viajan por el mismo túnel IPsec autenticado y quedan auditadas. Los datos, en cambio, fluyen en ambos sentidos según lo requiere cada flujo:

- **Datos transaccionales:** la base PostgreSQL local replica continuamente sus cambios hacia Aurora en la nube a través de DMS CDC, con un objetivo de pérdida de datos de 15 minutos o menos.
- **Eventos de bodega:** las transacciones del WMS se encolan en RabbitMQ local y, al disponer de enlace, se vuelcan en orden cronológico a SQS FIFO en la nube para su reconciliación.
- **Telemetría de cadena de frío en bodega:** los sensores Ebyte ME31 instalados en las cámaras de frío del CD alimentan al gateway Greengrass en el borde, que procesa las alertas localmente y reenvía los registros a IoT Core en la nube por MQTTS.
- **Observabilidad:** los colectores ADOT locales almacenan métricas y trazas en disco durante un máximo de 24 horas y las envían a CloudWatch en la nube cuando el enlace está disponible.
- **Identidad:** Keycloak maestro en la nube exporta las credenciales de forma cifrada a través de S3, y las cachés locales de cada sitio las importan para sostener las sesiones de los operarios sin depender del enlace.


#### Flujos desde el terreno

El terreno agrupa los flujos que se originan físicamente fuera del centro de distribución y fuera de la nube. Son tres:

- **Preventa en calle:** los preventistas usan terminales Zebra EC55, equipos industriales con SIM 4G/LTE empresarial y lector GS1 integrado. Se comunican directamente con API Gateway en la nube a través de la red celular del operador, sin atravesar la red del centro de distribución. Cuando no hay señal, operan contra su almacén local de turno y sincronizan al reconectar de forma idempotente.
- **Reparto en calle:** los conductores usan terminales Zebra TC58e, también con SIM 4G/LTE empresarial. Se comunican directamente con API Gateway por la red celular durante los turnos de reparto y, cuando pierden señal en zonas rurales, operan contra su almacén local y sincronizan al reconectar.
- **Termógrafos de camión:** los termógrafos Onset InTemp CX450, calibrados contra patrón NIST, registran la temperatura del compartimento refrigerado de forma independiente y sin conexión a red durante toda la ruta. Al regresar el camión al centro de distribución, los datos se descargan por Bluetooth al gateway local del sitio y desde ahí se envían a IoT Core en la nube.


Cuando el enlace WAN cae, cada dominio sigue operando con su pila local: la bodega contra PostgreSQL y RabbitMQ locales, el terreno de calle contra su almacén local, y el cross-docking contra su WMS local. Al reconectar, la sincronización es determinista y no genera duplicados. El detalle de la autonomía por ámbito se desarrolla en la sección de operación desconectada de este mismo capítulo.

### Emplazamiento componente por componente

Las tablas 21a, 21b y 21c justifican la decisión de emplazamiento de cada componente conforme a los seis criterios del Art. 16.2: latencia tolerada, criticidad operacional, volumen de datos, restricciones regulatorias, disponibilidad de conectividad y costo total de propiedad. La columna Criterio indica cuál de ellos determina el emplazamiento, y la justificación explica qué hace el componente y por qué vive donde vive. Estas tablas responden a la pregunta *dónde* vive cada componente y *por qué*; el equipamiento físico ofertado (marca, modelo y cantidad) se detalla en el capítulo de implementos, y la infraestructura de sala del CD Talca (energía, clima, seguridad física y cableado) en el capítulo del sitio principal.

**Tabla 21a** — Emplazamiento: componentes de nube pura en AWS sa-east-1

| ID | Componente | Criterio | Justificación |
|---|---|---|---|
| N-01 | ECS Fargate | Costo | Ejecuta la aplicación en contenedores y escala de 2 a 6 tareas en el peak de septiembre, sin mantener servidores permanentes ni equipamiento propio. |
| N-02 | Aurora PostgreSQL | Criticidad | Es la base transaccional maestra: opera en varias zonas de disponibilidad, se replica a us-east-1 con RTO ≤ 4 h y RPO ≤ 15 min, y amplía su almacenamiento sin intervención. |
| N-03 | Amazon S3 | Volumen y regulación | Guarda las evidencias de entrega, los DTE, la trazabilidad y la copia inmutable del respaldo, que crecen sin límite; Object Lock asegura la retención legal. |
| N-04 | SQS FIFO | Costo | Recibe la reconciliación de las bodegas en orden por sitio y sin duplicados, sin un broker propio que operar. |
| N-05 | AWS DMS | Volumen | Replica en forma continua los cambios de la base on-premise hacia Aurora sin desarrollo propio y sostiene un RPO de 15 min o menos. |
| N-06 | API Gateway | Regulación | Es la única entrada a las API y cumple lo que exige el Art. 21.2: validación de esquema, autenticación, cuotas y control de tasa, sin desarrollo propio. |
| N-07 | WAF v2 y Shield | Regulación y costo | Aplica las reglas gestionadas contra ataques OWASP y de denegación de servicio que exige el Art. 21.2, sin equipo dedicado que administrar. |
| N-08 | IoT Core | Volumen | Recibe los 13.200 mensajes diarios de cadena de frío por MQTTS y escala en forma automática. |
| N-09 | Secrets Manager y Parameter Store | Regulación | Cumple RT-04.09: guarda los secretos con rotación automática y sin credenciales embebidas, y los nodos on-premise los consumen en forma saliente por VPC Endpoint. |
| N-10 | CloudWatch | Costo | Recibe los logs, métricas y trazas de la nube y de los colectores on-premise, y los correlaciona con los servicios AWS sin operar un clúster de monitoreo. |
| N-11 | Security Lake y Macie | Regulación | Centraliza la correlación de eventos de seguridad y detecta en forma automática los datos personales y de pago para la auditoría. |
| N-12 | Redshift Serverless y QuickSight | Volumen y costo | Mantiene 5 años de datos analíticos separados de la base transaccional y publica los tableros del CLIENTE sin licencias de BI. |
| N-13 | Android Enterprise y Zebra DNA | Conectividad y costo | Gestiona en forma remota más de 462 dispositivos de terreno sin infraestructura propia, y lo opera el equipo de TI de 4 personas. |

**Tabla 21b** — Emplazamiento: componentes on-premise

| ID | Componente | Criterio | Justificación |
|---|---|---|---|
| L-01 | Proxmox VE | Criticidad | Virtualiza los 3 nodos del clúster de Talca. El hipervisor de la bodega no depende de la nube y el clúster N+1 opera 24 h sin enlace. |
| L-02 | Ceph | Criticidad | Almacena las VMs y los datos del WMS en 12 OSD con réplica 2, de modo que la falla de un disco no detiene la bodega. |
| L-03 | PostgreSQL 16 | Latencia y criticidad | Es la base de la bodega en VM-02 de Talca y VM-C02 de Concepción. El picking en cámara a −22 °C exige respuesta local y la bodega opera 24 h sin enlace; los cambios se replican a Aurora por DMS. |
| L-04 | RabbitMQ | Conectividad | Es el broker local en VM-03, VM-C04 y E-01: guarda hasta 24 h de transacciones durante un corte y las entrega en orden y sin duplicados al reconectar. |
| L-05 | Capa anticorrupción del ERP | Criticidad | Corre en VM-04 junto al ERP de 2017, fuente única de la información contable y tributaria, que reside en la red local sin exposición externa; la capa es su única puerta de entrada. |
| L-06 | NAS de respaldo | Conectividad | El equipo D-05 guarda la copia local cifrada de la regla 3-2-1-1-0 y permite restaurar el WMS en ≤ 4 h sin depender del enlace. |
| L-07 | Docker Compose | Conectividad | Ejecuta el WMS en el nodo E-01 de cada cross-docking, que no tiene fibra: la ventana de 3 h opera 100 % local y la instalación y el parcheo no dependen de la red. |
| L-08 | Greengrass v2 | Latencia | Corre en el gateway B-02, detecta la excursión térmica y bloquea el despacho en menos de 5 s, 100 % en el borde, con un buffer de 14 h. |
| L-09 | Colector ADOT | Conectividad | Corre en VM-06 y VM-C04, guarda la telemetría hasta 24 h en disco y la envía a la nube al reconectar. |
| L-10 | Firewall UTM | Criticidad | Los equipos D-01 y C13 terminan la VPN, segmentan la red y conmutan entre enlaces; en Talca operan en alta disponibilidad activo/pasivo. |
| L-11 | WLAN Wi-Fi 6E industrial | Latencia | Da cobertura en bodega y cámara de frío a 150 terminales RF simultáneos con respuesta ≤ 1 s en picking, sin depender del enlace WAN. |

**Tabla 21c** — Emplazamiento: componentes híbridos, con presencia en nube y on-premise

| ID | Componente | Nube | On-premise | Criterio | Justificación |
|---|---|---|---|---|---|
| H-01 | Django | ECS Fargate: preventa, reparto, portal y canal moderno | VM-01, VM-C01 y E-01: WMS de bodega en modo wms_only | Criticidad | La bodega opera contra su base local; el resto de los procesos escala en la nube. |
| H-02 | Keycloak | Maestro en Fargate con OIDC, MFA y SSO | Cachés de solo lectura en VM-05 y VM-C03 | Conectividad | La sesión sobrevive a los cortes: 8 h en bodega y 14 h en terreno. |
| H-03 | Celery | Fargate: reconciliación, sincronización con el ERP y notificaciones | VM-01 y VM-C01: workers de bodega | Criticidad | Las tareas de bodega no dependen de la nube; solo la reconciliación la requiere. |
| H-04 | OpenTelemetry | CloudWatch | Colectores ADOT con buffer de 24 h | Conectividad | La telemetría se difiere sin pérdida y se consolida en CloudWatch al reconectar. |
| H-05 | EDR | Consola de gestión y correlación | Agentes en cada VM y estación | Regulación | Cumple RT-11.16: detecta amenazas en las cargas de nube y on-premise con una respuesta centralizada. |
| H-06 | VPN IPsec Site-to-Site | AWS VPN Gateway con 2 túneles por CD | Firewall de borde como Customer Gateway | Conectividad | Cifra el enlace entre dominios, enruta con BGP y conmuta en forma automática entre enlaces. |
| H-07 | Ansible y Terraform | Terraform/CDK: infraestructura AWS | Ansible: configuración, parches y CIS en los 5 sitios | Costo | La infraestructura queda declarada como código, sin licencia de una plataforma de gestión. |

![Diagrama de arquitectura física de la solución](../Diagramas/ARQF-01_Modelo_emplazamiento_hibrido.png)

Figura 15. Diagrama de arquitectura física de la solución.

### Instalaciones de la red on-premise

La red on-premise se compone de seis instalaciones (Tabla 14.1 y RT-21.16):

- **CD Talca (sala técnica principal, sala blanca de 32 m²):** clúster WMS de 3 nodos, base transaccional on-premise (PostgreSQL 16, VM-02), broker local RabbitMQ (VM-03), capa anticorrupción del ERP (VM-04), caché de identidad (VM-05), telemetría (VM-06), respaldo NAS (D-05) y componentes de sala (UPS N+1, generador 12 kVA con estanque 24 h, clima N+1, seguridad física).
- **CD Concepción (9.000 m², gabinete de borde):** servidor de borde con el WMS (VM-C01), base local (VM-C02), caché de identidad (VM-C03), broker + telemetría (VM-C04) y Gateway IoT Greengrass (B-02); opera 24 h de forma autónoma e independiente de Talca.
- **Cross-docking de Curicó, Chillán y Los Ángeles:** nodo de cómputo industrial (E-01) con WMS y broker locales, enlace principal Starlink (D-06) y respaldo LTE dual (2 proveedores).
- **Casa matriz y oficinas centrales (Talca):** sin nodo de cómputo propio; acceso a la nube para administración, planificación y portal de clientes (RT-03.22).


La proyección a 3 años (RT-02.12) incorpora una séptima instalación; el gabinete de crecimiento de la sala (R04) absorbe esa expansión sin obras adicionales en el sitio principal.

### Operación desconectada

El modelo híbrido garantiza que ningún proceso operacional se detenga por pérdida del enlace WAN. Cada ámbito mantiene autonomía local con su propia base de datos, broker de mensajería y caché de identidad; al reconectar, la sincronización es idempotente y determinista, sin pérdida ni duplicación de transacciones. La Tabla 29 resume la autonomía por ámbito:

**Tabla 29** — Operación desconectada

| Ámbito | Autonomía | Cobertura funcional |
|---|---|---|
| Centro de distribución (CD Talca y Concepción) | ≥ 24 h | Recepción, preparación, despacho, conteo cíclico y trazabilidad contra la BD local; reconciliación determinista al reconectar (RT-03.12). |
| Terreno (preventa y reparto) | 14 h (turno completo) | Toma de pedido, entrega, POD, devoluciones y cobros contra caché local y buffer idempotente (RNF-06.02, RT-03.10); sesión sostenida por caché de identidad A-05 (TTL 8 h bodega, 14 h reparto/preventa). |
| Cross-docking | 3 h 100 % local | Recepción, desconsolidación, validación de frío y re-despacho (RT-03.10/03.11). |
| Sincronización al reconectar | Flota ≤ 10 min; CDs ≤ 2 h | Vuelco en orden estricto, deduplicación idempotente y reconciliación determinista (RT-03.12, RT-03.13, RNF-07.01). |

## Tecnologías de software ofertadas

Las tecnologías se eligen bajo los criterios de neutralidad tecnológica, soporte vigente por los 56 meses contractuales y preferencia por servicios administrados y componentes de código abierto con estándares abiertos, de modo que el CLIENTE conserve la reversibilidad de la solución:

- **B1 — Aplicación.** Django monolito modular (Python) + Celery sobre AWS ECS Fargate (2–6 tareas con escala automática). La misma imagen se reutiliza en modo wms_only dentro del ambiente on-premise.
- **B2 — BD transaccional nube (maestro).** Amazon Aurora PostgreSQL en sa-east-1 (Multi-AZ), con réplica pasiva promueble en us-east-1 para recuperación ante desastres (RTO ≤ 4 h / RPO ≤ 15 min).
- **B3 — BD transaccional on-premise.** PostgreSQL 16 (VM-02 Talca / VM-C02 Concepción): sistema de verdad de la bodega durante cortes de enlace, con flujo continuo hacia la réplica en nube por AWS DMS CDC sobre el WAL lógico (registro de escritura anticipada que permite replicar cambios en tiempo real) (RPO ≤ 15 min).
- **B4 — Broker de mensajería.** RabbitMQ local (colas offline por sitio) + SQS FIFO en nube (reconciliación): cada sitio absorbe hasta 24 h de operación sin enlace con vuelco en orden estricto e idempotencia (D-AL-03). Las tareas derivadas de cada evento las despacha Celery desde el monolito.
- **B5 — Identidad (IdP maestro).** Keycloak en ECS/Fargate (OIDC/OAuth 2.1, MFA, SSO), autoridad única en sa-east-1 con cachés locales de solo lectura (ADR-06); el modelo completo se describe en la sección de seguridad.
- **B6 — Telemetría IoT.** AWS IoT Core + Greengrass v2 + sensores Ebyte ME31 (B-01/B-02): registro continuo de cadena de frío con decisión de bloqueo por excursión térmica 100 % en el borde.
- **B7 — Observabilidad.** Plataforma única: instrumentación OpenTelemetry con colectores ADOT on-premise (VM-06, VM-C04, cross-dock; buffer en disco 24 h) que emiten a CloudWatch (logs, métricas y trazas) en sa-east-1 (ADR-14); sin herramientas duplicadas por ambiente ni infraestructura de monitoreo que operar.
- **B8 — Virtualización on-premise.** Proxmox VE/KVM + Ceph (12 OSD, réplica 2, 3 monitores): tolera la pérdida de cualquier nodo con quórum real; respaldo único 3-2-1-1-0 con NAS D-05 y pierna inmutable en nube.
- **B9 — Orquestación de contenedores de borde.** Docker/Docker Compose + WMS en los 3 cross-docking (E-01) y en el borde de Concepción: instalación y parcheo sin dependencia de la red, con paridad de versiones.
- **B10 — Gestión y configuración.** Ansible (F-02, parches/CIS) + Terraform/CDK IaC (multi-zona): configuración declarada como código versionado en el repositorio del CLIENTE.
- **B11 — Gestión de dispositivos de terreno (MDM).** N-13 — Android Enterprise / Zebra DNA (servicio gestionado): enrolamiento por IMEI contra el usuario, política (cifrado local, PIN, modo quiosco), actualización Over-The-Air de la aplicación y de la caché de turno, inventario del parque y borrado remoto selectivo; sin infraestructura on-premise (equipo de TI de 4 personas).
- **B12 — Gestión de secretos.** AWS Secrets Manager + SSM Parameter Store (N-12): rotación automática, sin credenciales embebidas; consumo saliente por VPC Endpoint desde los nodos on-premise (ADR-15); credencial de emergencia en sobre sellado en el recinto de custodia.
- **B13 — Seguridad lógica.** WAF v2 + Shield + API Gateway + SIEM/Security Lake + EDR (F-03) + Macie: superficie expuesta mínima y detección concentrada en un solo registro, bajo política Zero Trust.
- **B14 — Analítica / BI.** Redshift Serverless (OLAP, 5 años) + QuickSight: separación OLTP/OLAP con latencia máxima de 4 h para los tableros del CLIENTE.
- **B15 — Licenciamiento.** Servicios AWS por servicio + OSS sin licencia (Keycloak, PostgreSQL, Proxmox VE, RabbitMQ): reversibilidad y ausencia de dependencia propietaria.


### Integración con el ERP y documentos tributarios

El ERP de 2017 no se reemplaza ni se modifica (Cap. 10 del caso): permanece como única fuente de verdad tributaria. La solución entrega los datos de operación a través de la capa anticorrupción (ACL, VM-04) y el ERP emite los documentos tributarios (guía de despacho electrónica, factura, boleta y nota de crédito con folios SII), con acuse de recibo con efectos legales —una sola verdad, un solo emisor. El acceso desde la nube a este ERP ocurre únicamente vía la ACL (celery-erp-sync → ACL, nunca escritura directa).

## Implementos a proveer: hardware y software

El inventario ofertado se agrupa en infraestructura de cómputo y almacenamiento, red y seguridad, dispositivos de terreno y operación. Son especificaciones de equipamiento físico (marca, modelo y cantidad) que el CLIENTE adquiere y el adjudicatario instala, integra y mantiene (Art. 14.2). Las cantidades y justificaciones de cada fila se referencian al Formulario T-11. La decisión de emplazamiento de cada componente (dónde vive y por qué, según Art. 16.2) se declara en el capítulo de emplazamiento; los componentes de infraestructura de sala del CD Talca (UPS, generador, climatización, seguridad física y gabinetes) se declaran en el capítulo del sitio principal.

### Infraestructura de cómputo y almacenamiento

La infraestructura de cómputo y almacenamiento ofertada se detalla en la Tabla 23:

**Tabla 23** — Infraestructura de cómputo y almacenamiento

| Componente | Producto ofertado | Ubicación | Cant. | Justificación |
|---|---|---|---|---|
| C1 — Servidor hipervisor (clúster) | Dell PowerEdge R6615 / HPE DL325 Gen11 — EPYC 9124 16c, 128 GB DDR5 ECC, RAID 1 SO + RAID 10 (4 × NVMe 1,92 TB + Hot-Spare), 2 × 10GbE, dual PSU 1+1 | CD Talca (Rack R01) | 3 | Cada nodo entrega el mismo cómputo y almacenamiento: N+1 según RT-08.03 y Ceph con discos NVMe en RAID 10 supera los IOPS del peak de septiembre. |
| C2 — NAS respaldo local | NAS/WORM local cifrado (LUKS/SED) — copia rápida 3-2-1-1-0 | CD Talca (Rack R01) | 1 | Copia local de recuperación rápida: restauración del WMS en ≤ 4 h sin depender del enlace (RNF-20.06). Complementa la pierna inmutable en nube, pero no la reemplaza. |
| C3 — Servidor de borde Concepción | Dell R250 / HPE DL20 Gen11 — Xeon E-2300 6c, 32 GB, RAID 10 (4 × NVMe 960 GB + Hot-Spare) | CD Concepción (gabinete) | 1 | Sostiene el WMS con 24 h de operación autónoma (12 vCPU y 24 GB dimensionados para el volumen de Concepción), con doble fuente. |
| C4 — Nodo de cómputo de cross-docking | Mini-PC industrial Advantech ARK-2250 / NUC Pro 12 — i5/i7 12ª gen, 16 GB, NVMe 512 GB, 4G Cat-12 LTE dual SIM | Curicó, Chillán, Los Ángeles | 3 | Opera en naves sin climatización certificada (supuesto conservador de hasta 50 °C en verano bajo techumbre de zinc) y sin fibra (RT-03.17); enlace principal Starlink por ethernet con respaldo LTE dual de dos proveedores y conmutación automática en menos de 30 s. |

### Red y seguridad

Los componentes de red y seguridad ofertados se detallan en la Tabla 24:

**Tabla 24** — Red y seguridad

| Componente | Producto ofertado | Ubicación | Cant. | Justificación |
|---|---|---|---|---|
| C5 — Firewall UTM / Customer Gateway | Clúster HA Activo/Pasivo — firewall UTM de grado empresarial o equivalente, con sincronización de sesiones (D-01) | CD Talca (Rack R02) | 2 | Sin equipos únicos de perímetro (RT-08.03): la pasiva asume direcciones y túneles en menos de 30 s, en circuitos eléctricos distintos (RT-08.04). Punto de terminación de la Site-to-Site VPN y del Direct Connect activable. |
| C6 — Switch core L3 | Stack/MLAG — Cisco Catalyst 9300-48P o equivalente (D-02), plano de distribución único | CD Talca (Rack R02) | 2 | Un único plano de distribución: la falla de un miembro no interrumpe el tráfico (RT-08.03). |
| C7 — Switch de gestión | 1 × L2 (VLAN MGT) + consola KVM | CD Talca (Rack R02) | 1 | Puertos de administración (IPMI/iDRAC) aislados en VLAN dedicada con MFA; operación y recuperación incluso con la red de producción caída. |
| C8 — Red de distribución horizontal (HDA) | Patch panels fibra OM4 + Cat6A certificado | CD Talca (Rack R03) | 1 | Cableado certificado enlace por enlace (RT-06.04) con dos ductos de ingreso independientes a la sala (RT-06.32). |
| C9 — WLAN industrial | AP Wi-Fi 6E industriales VLAN-Operaciones + estudio de cobertura en bodega y cámara | CD Talca + Concepción (bodegas) | 2 redes (6+3 AP) | 120 (Talca) y 30 (Concepción) terminales rugosos simultáneos; segmentación por tipo de dispositivo (RT-03.23) y verificación de cobertura dentro de las cámaras donde opera el picking (RT-03.24→RT-03.23). |
| C10 — Enlace primario | Fibra óptica simétrica — Talca 20→50 Mbps · Concepción 10→20 Mbps | CD Talca · CD Concepción | 2 | Dimensionado (RT-03.20) sobre evidencia, DTE y telemetría (≈ 1–2 Mbps; peak sept. ≈ 312 MB/h ≈ 0,7 Mbps), sincronización de flota en la ventana de retorno (≈ 2 GB/día; ≈ 4–5 Mbps a 3× de RT-09.03) y respaldo semanal a la nube (≈ 40 → 120 GB, ≈ 40 Mbps en ventana nocturna); valores escalados al crecimiento 3× sin rediseño que exige RT-09.03. Respaldo escalonado sin obra adicional. El camino satelital Starlink (D-06) actúa como respaldo preferente. |
| C11 — Enlace respaldo | LTE empresarial (SIM dedicada) — Talca 5→10 Mbps · Concepción 3→5 Mbps · Cross-docks 2→5 Mbps (dual, 2 proveedores) | CD Talca · CD Concepción · Curicó, Chillán, Los Ángeles | 5 | Continuidad sin un solo camino ni proveedor (RT-03.17) con conmutación automática en menos de 30 s; en los CDs queda como camino terciario tras fibra y Starlink; en los cross-docks es el respaldo automático del satelital. |
| C12 — VPN | AWS Site-to-Site VPN IPsec IKEv2 cifrado + BGP | Talca y Concepción → sa-east-1 | 2 túneles/CD | Túneles IPsec con cifrado de grado comercial y enrutamiento dinámico para replicar base, sincronizar broker y transmitir telemetría sin degradar la operación (RT-03.21); MTU de túnel 1.436 bytes. |
| C13 — Firewall de borde (CD Concepción) | Firewall de borde o equivalente — Customer Gateway + conmutación automática | CD Concepción (gabinete) | 1 | Customer Gateway del túnel hacia AWS y failover entre fibra y LTE en menos de 30 s (RT-08.03, RT-03.17). |
| C14 — Switch core de borde (CD Concepción) | Cisco Catalyst 9300 o equivalente — capa de distribución | CD Concepción (gabinete) | 1 | Sostiene localmente la red de bodega del sitio secundario durante 24 h de autonomía sin depender del sitio principal (RT-08.03). |
| C15 — Switch compacto cross-docking | Netgear GS308E o equivalente — 8 puertos Gigabit gestionable | Curicó, Chillán, Los Ángeles | 3 | Equipo compacto y pasivo para nave industrial sin sala técnica: interconecta mini-PC, router Starlink, escáneres DS2208 y terminales (RT-03.17). |

### Dispositivos de terreno y operación

Los dispositivos de terreno y operación ofertados se detallan en la Tabla 25:

**Tabla 25** — Dispositivos de terreno y operación

| Componente | Producto ofertado | Ubicación | Cant. | Justificación |
|---|---|---|---|---|
| C16 — Terminal preventa | Zebra EC55 (Android, IP67, guantes, lector 2D SE4100) | Preventistas (5 regiones) | 62 + 20 % reserva | Opera sin señal, resiste la jornada con una carga, funciona con guantes y su luminosidad es legible a pleno sol (RT-08.11). |
| C17 — Terminal reparto | Zebra TC58e (5G, SE55, batería 7.000 mAh, GPS L1/L5, IP65/68, −30 °C) | Conductores propios (42) + externos (≈ 160) | ≈ 200 + reserva | Un solo modelo para propios y externos: mismo repuesto, capacitación e integración (sección de Emplazamiento de este documento). |
| C18 — Impresora cabina | Zebra ZQ620 Plus (3", ZPL, IP54, Link-OS) | Portátil — 1 por conductor repartidor | ≈ 200 | Evidencia de entrega y comprobantes impresos en cabina, no en bodega; diseñada para vehículo con batería de reemplazo. |
| C19 — POS móvil | PAX A920 Pro (Android 14, PCI PTS 7.x, EMV L1/L2) | Portátil — 1 por conductor repartidor | ≈ 200 | Cobranza con tarjeta en el domicilio del cliente: acreditado PCI PTS y certificado EMV, integrado vía Bluetooth con la aplicación de reparto. |
| C20 — Terminal RF congelado | Zebra MC9400 Cold Storage Freezer (−30 °C, SE58 100 pies, batería freezer 5.000 mAh, Wi-Fi 6E) | Talca 144 (120+20 %) · Concepción 30 | 174 | Picking de la cámara a −22 °C con guantes gruesos: certificado para cámara frigorífica, lectura a distancia y batería con recambio en caliente (RT-08.11, RT-08.12 y RT-13.08). |
| C21 — Impresora térmica andén | Zebra ZT411 (203 dpi, 14 ips, Ethernet, ZPL) | Talca (4: 2 recepción + 2 despacho) · Concepción (2) | 6 | Etiquetas SSCC GS1-128 impresas en el andén al armar la unidad logística (RF-01.07), con resolución garantizada a lo largo de la cadena (RT-05.23). |
| C22 — Balanza recepción | Dibal BEV (plataforma ME + DMI-610 Inox, doble RS-232/Ethernet) | Talca (2) · Concepción (1) | 3 | Captura en línea del peso de recepción hacia el WMS (RF-01.01), sin digitación manual, con grado industrial y calibración certificada. |
| C23 — Escáner GS1 cross-dock | Zebra DS2208 (1D/2D + GS1 DataBar, garantía 60 meses) | Curicó, Chillán, Los Ángeles | 6 (2 × plataforma) | Lectura de códigos GS1 de última generación en desconsolidación y re-despacho; dos unidades por plataforma cubren dos muelles simultáneos. |
| C24 — Sensor IoT temperatura | Módulo Ebyte ME31-XDXX0400 (4 canales PT100, Modbus RTU/TCP, −40…+85 °C) + sondas 3 hilos — 28 puntos | Talca, Concepción, cámaras, camiones | 7 módulos | 28 puntos de medición alimentan el registro continuo de cadena de frío; exactitud ±1,1 °C a −22 °C (valor calculado a partir del rango del sensor) distingue excursión térmica real de fluctuación del instrumento. |
| C25 — Termógrafo de camión | Onset InTemp CX450 (BLE, −30…+70 °C ±0,5 °C, NIST 2 ptos) | Camiones con frío | 18 | Registrador independiente calibrado contra patrón NIST en dos puntos; el dato aterriza en el sistema por Bluetooth al volver al centro. |
| C26 — Estaciones de trabajo | PC i5/i7, 16 GB, SSD NVMe 512 cifrado + 2 × 24" (NCh 2527) | Talca (5) · Concepción (3) | 8 | Puestos de despacho, administración, planificación, calidad y TI (RNF-23.04): disco cifrado gestionado desde el EDR y doble monitor (RT-08.08). |
| C27 — Kit Starlink fijo (enlace satelital D-06) | Starlink Enterprise fijo (antena en techumbre + router) — 1 TB (CDs) / 500 GB (cross-docks), 56 meses | Curicó, Chillán, Los Ángeles (principal) | 3 | Enlace principal en los cross-docks, que operan en naves industriales sin cobertura de fibra; el respaldo es LTE empresarial con conmutación automática (RT-03.17, RT-08.13); reposición de hardware estimada en 15 % en 56 meses (supuesto conservador basado en la vida útil declarada por el fabricante). |

Gateway IoT + Greengrass (B-02): 2 unidades (Talca y Concepción), ADAM-6000, con runtime AWS IoT Greengrass Core embebido para detección de excursión y buffer local de 14 h.

### Resumen del inventario ofertado

El inventario ofertado se resume en la Tabla 26:

**Tabla 26** — Resumen del inventario ofertado

| Familia | Cantidad |
|---|---|
| Servidores hipervisor clúster (Talca) | 3 |
| NAS respaldo local (D-05) | 1 |
| Servidor de borde Concepción | 1 |
| Mini-PC industrial cross-docking | 3 |
| Kit Starlink fijo WAN satelital (D-06) | 3 |
| Estaciones de trabajo | 8 |
| Terminales preventa Zebra EC55 | 62 + 20 % |
| Terminales reparto Zebra TC58e | ≈ 200 + reserva |
| Impresoras cabina ZQ620 Plus | ≈ 200 |
| POS PAX A920 Pro | ≈ 200 |
| Terminales RF Zebra MC9400 Cold Storage | 174 |
| Impresoras térmicas andén ZT411 | 6 |
| Balanzas Dibal BEV | 3 |
| Escáneres GS1 DS2208 | 6 |
| Sensores IoT Ebyte ME31 | 28 puntos (≈ 7 módulos) |
| Termógrafos Onset CX450 | 18 |
| Firewalls UTM | 2 HA + 1 borde |
| Switch core L3 stack/MLAG | 2 + 1 core |
| AP Wi-Fi 6E industrial | 6 + 3 |
| Switch compacto cross-docking | 3 |
| Gateway IoT + Greengrass (B-02) | 2 |
| UPS 6 kVA N+1 | 1 |
| Generador 12 kVA estanque 24 h | 1 |
| CRAC de precisión N+1 | 2 |
| Cámaras IP ≥ 30 días | 7 |
| Racks 42U | 4 |
| Nube AWS (Aurora, ECS, S3, WAF, IoT, BI) | 1 solución, 2 regiones |

## Especificaciones del sitio principal on-premise (CD Talca)

**Tipología declarada (numeral 6.1 de las Transversales): sala técnica principal.** El CD Talca aloja el núcleo del componente on-premise, es decir cómputo, almacenamiento y procesamiento sustantivos en instalaciones del CLIENTE. Concentra el motor WMS, la base transaccional del maestro de bodega, el broker de colas, la capa anticorrupción del ERP, la caché de identidad, la telemetría y el respaldo local. Por eso se le aplican íntegramente los requisitos RT-06.01 a RT-06.34, y no el régimen proporcional de una sala de sitio.

**Disponibilidad de infraestructura comprometida: 99,95 % mensual**, conforme al numeral 6.1 y a la tabla del numeral 7.2 de las Transversales, medida por componente: energía del recinto, climatización, red y comunicaciones, servidores y cómputo, y motor de base de datos. El compromiso se sostiene con redundancia N+1 en energía y climatización, doble acometida con transferencia automática, generación autónoma propia y monitoreo continuo con alertamiento; no se invoca ninguna clasificación de instalación de tercero, porque las Bases no exigen certificación de nivel sino el cumplimiento verificable de cada requisito técnico individual. Este valor es el nivel de la infraestructura del recinto y es distinto del compromiso contractual penalizable del Artículo 78°, que recae sobre la transacción de negocio de extremo a extremo (≥ 99,9 % mensual, RT-10.01).

El programa arquitectónico propuesto considera ≈ 173 m² y 14 recintos: sala blanca de 32 m², NOC de 14 m², sala de sistemas de alimentación ininterrumpida y baterías, sala de climatización, sala de extinción, distribuidor principal y acometidas, recinto de custodia de medios de 10 m², patio de generador y recintos de apoyo. La disposición interna, la separación de zonas y la elevación de gabinetes constan en los planos del recinto que acompañan a esta parte.

![Plano de distribución interna del recinto técnico, con la separación de las zonas de generador, baterías, climatización, servidores, comunicaciones y custodia de medios](../Diagramas/RT-06_DataCenter/DC01a_Plano_Distribucion.png)

Figura 16. Plano de distribución interna del recinto técnico, con la separación de las zonas de generador, baterías, climatización, servidores, comunicaciones y custodia de medios.

Energía: UPS doble conversión on-line 6 kVA con configuración N+1 y banco VRLA con autonomía ≥ 30 min a plena carga; grupo electrógeno de 12 kVA con estanque para 24 h y contrato de reabastecimiento; transferencia automática red↔generador con prueba mensual con carga real; PDU verticales A/B por gabinete con medidor; factor de potencia ≥ 0,95.

![Cadena eléctrica del recinto: acometida, transferencia automática, generación autónoma, alimentación ininterrumpida y distribución A/B por gabinete](../Diagramas/RT-06_DataCenter/DC02_Cadena_Electrica.png)

Figura 17. Cadena eléctrica del recinto: acometida, transferencia automática, generación autónoma, alimentación ininterrumpida y distribución A/B por gabinete.

Climatización: 2 CRAC de precisión ≈ 12.000 BTU/h en N+1, con free cooling, pasillo frío confinado y rango ASHRAE TC 9.9 de 18–27 °C y 40–60 % HR medido a la toma de aire del equipo; PUE objetivo de diseño 1,7 (valor conservador para sala de servidores pequeña con climatización de precisión N+1) con medición continua en 2 puntos y reporte trimestral.

Incendios: detección temprana por aspiración AnaLASER; extinción con agente limpio FM-200 conforme NFPA 75/2001 con botón de aborto; extintores ABC y CO₂ por recinto.

Seguridad física: 4 capas de acceso con biometría facial y resguardo AFIS, esclusa antipassback y bitácora electrónica, una persona a la vez y acompañada; 12 puertas controladas y 7 cámaras IP con retención ≥ 30 días integradas al control de acceso; NOC de 14 m² contiguo a la sala con ventana interior («ver sin entrar»); sensores ambientales DCIM/BMS.

Custodia de medios: recinto de 10 m² en la segunda línea, sin luz UV (≤ 300 lux), 40–60 % HR, ventilación forzada y 18–27 °C; medio cifrado transportable rotado semanalmente a bóveda externa bajo custodia acreditada con cadena de custodia y bitácora; la pierna inmutable S3 es complementaria, no la reemplaza.

Cableado y comunicaciones: cableado estructurado Cat6A F/UTP + fibra OM4 certificado enlace por enlace sobre piso técnico de 40 cm, jerarquía ANSI/TIA-942 ENI→MDA→HDA→ZDA→EDA, con dos ductos de ingreso independientes; 4 racks 42U en gabinete de servidores y comunicaciones separados, con el cuarto (R04) reservado al crecimiento a 3 años.

![Elevación de los cuatro gabinetes, con la ocupación proyectada de cada uno y el margen de crecimiento reservado en R04](../Diagramas/RT-06_DataCenter/DC03b_Elevacion_Racks_RT0605.png)

Figura 18. Elevación de los cuatro gabinetes, con la ocupación proyectada de cada uno y el margen de crecimiento reservado en R04.

Los componentes de infraestructura de sala del CD Talca (UPS, generador, transferencia automática, climatización, seguridad física, extinción, cableado y gabinetes) se detallan en la Tabla 27. El equipamiento de cómputo, red y comunicaciones que se aloja en estos gabinetes (servidores, switches, firewalls, WLAN, terminales) se declara en el capítulo de implementos:

**Tabla 27** — Componentes de sala del sitio principal (CD Talca)

| Componente | Producto ofertado | Ubicación | Cant. | Justificación |
|---|---|---|---|---|
| D1 — UPS | Doble conversión on-line 6 kVA, N+1, banco VRLA ≥ 30 min | Sala de UPS/baterías (2ª línea) | 1 | Sin parpadeo entre la caída de red y la partida del generador; autonomía ≥ 30 min a plena carga (RT-06.07). |
| D2 — Generador | Grupo electrógeno 12 kVA, estanque 24 h + contratos de reabastecimiento | Patio generador (exterior) | 1 | Asume TI y clima en 8–15 s; el estanque garantiza 24 h (RT-06.08). |
| D3 — ATS/TTA + tablero | Transferencia automática red↔generador + protecciones selectivas | Acometida (accesible desde fuera) | 1 | Transferencia automática con prueba mensual con carga real y termografía periódica (RT-06.10). |
| D4 — Climatización | 2 CRAC de precisión ≈ 12.000 BTU/h, N+1, free cooling, 18–27 °C / 40–60 % HR | Sala de climatización | 2 | Rango ASHRAE en toma de aire del equipo (RT-06.13 y RT-06.14); redundancia N+1 y pasillo frío confinado. |
| D5 — PDU racks | 2 PDU verticales A/B por gabinete, con medidor | 4 racks sala | 4 × 2 | Dos caminos eléctricos independientes por gabinete (RT-08.04); el medidor es el denominador del PUE. |
| D6 — Detección de incendios | Detección por aspiración AnaLASER o equivalente | Sala blanca | 1 | Detección temprana antes de llama visible (RT-06.16). |
| D7 — Extinción | FM-200 o equivalente, NFPA 75/2001, botón de aborto | Sala blanca | 1 | Agente limpio sobre equipos energizados (RT-06.17) y extintores ABC/CO₂ por recinto (RT-06.18). |
| D8 — Seguridad física | Biometría facial + resguardo AFIS, esclusa, bitácora electrónica | Acceso a la sala (4 capas) | 1 | Doble factor con re-verificación biométrica y antipassback (RT-06.20, RT-06.21 y RT-06.23). |
| D9 — Videovigilancia | 7 cámaras IP, retención ≥ 30 días + respaldo auditable | Sala + perímetro | 7 | Cobertura de cada puerta controlada; «la puerta marca el video» (RT-06.24). |
| D10 — Recinto de custodia | Sala de custodia 10 m²: LED sin UV ≤ 300 lux, 40–60 % HR, ventilación forzada, 18–27 °C | Sala — 2ª línea | 1 | Medios de respaldo en condiciones que no degradan el soporte (RT-06.27), accesible sin cruzar la sala blanca (RT-06.26). |
| D11 — Gabinetes | 4 racks 42U (R01 servidores, R02 red, R03 HDA/respaldo, R04 crecimiento) | Sala blanca | 4 | Servidores y comunicaciones separados (RT-06.05); el rack R04 absorbe el crecimiento a 3 años sin obras. |
| D12 — Cableado estructurado | Cat 6A + fibra OM4 certificado por enlace; piso técnico 40 cm | Sala | 1 | Normativa por enlace (RT-06.04) y recorridos máximos/mínimos verificados para enlaces de 10 GbE. |

## Especificaciones del sitio secundario

**Cómo se satisface el numeral 7.1.** Las Transversales exigen un sitio secundario en dependencias distintas del principal, en modalidad activo-activo o activo-pasivo, con replicación en línea del ambiente de producción y características tecnológicas equivalentes a las del sitio principal en lo que respecta a los servicios críticos. La solución lo satisface con dos sitios secundarios, uno por cada dominio del despliegue híbrido, porque la carga crítica vive en ambos:

- **Para el componente on-premise, el CD Concepción:** es una dependencia física distinta, a 340 km del extremo opuesto de la red y sin amenazas comunes con Talca, y opera el motor de almacenes con su propia base local y autonomía de 24 horas. No es un sitio en espera: opera de forma autónoma todos los días y asume la carga de bodega de Talca mediante promoción controlada.
- **Para la carga principal en nube, la región AWS us-east-1:** aloja la réplica pasiva promovible del núcleo transaccional, a ≈ 7.700 km de la región primaria y ≈ 8.500 km de Talca, sin amenazas comunes.


El mecanismo de recuperación ante desastres (modalidad activo-pasiva, RTO ≤ 4 h, RPO ≤ 15 min), el procedimiento de conmutación y retorno, las pruebas semestrales, la tabla de componentes de la réplica y el esquema de respaldos 3-2-1-1-0 se declaran en el capítulo de arquitectura de despliegue.

El gabinete de borde con que se habilitan el sitio secundario on-premise y las tres plataformas de cross-docking es el siguiente:

![Gabinete de borde industrializado del CD Concepción y de las tres plataformas de cross-docking: alimentación protegida, control de acceso y monitoreo remoto dimensionados al sitio (numeral 6.1, tipología de borde operacional)](../Diagramas/RT-06_DataCenter/DC04_Gabinetes_Borde.png)

Figura 19. Gabinete de borde industrializado del CD Concepción y de las tres plataformas de cross-docking: alimentación protegida, control de acceso y monitoreo remoto dimensionados al sitio (numeral 6.1, tipología de borde operacional).

## Arquitectura de integración

Vista física de las integraciones: emplazamiento de las superficies, mensajería y costuras con la arquitectura lógica. El catálogo de integraciones, los principios, los contratos, los eventos canónicos, la capa anticorrupción y el versionado se declaran en la arquitectura lógica (Subdocumento 4.1). El volumen de mensajes por integración se declara en el capítulo de dimensionamiento (Tabla 33).

### Vista de integración

La vista de integración se organiza en cuatro dominios físicos:

- **Terreno (offline-first):** C-01 App Preventa (62 preventistas), C-02 App Reparto (≈200 conductores) y C-03 HHT bodega (120 concurrentes).
- **On-premise (5 sitios con cómputo):** A-01 Motor WMS (M1, M2 y M5 en modo wms_only), A-03 RabbitMQ (buffer 24 h), A-04 capa anticorrupción (frontera única del ERP), B-02 Greengrass (buffer 14 h) y E-01 WMS del cross-dock (ventana de 3 h).
- **Nube AWS sa-east-1:** Amazon API Gateway (Capa 3), Capa 4 con M1–M12 en Django + workers Celery, N-09 SQS FIFO, M11 Hub EDI GS1 (EANCOM, GS1 XML y EPCIS) y N-08 IoT Core.
- **Terceros:** ERP 2017 (sin documentación de interfaces), SII (DTE y guía electrónica), cadenas de supermercados (hito enero 2029), Transbank Webpay/POS, GIS/mapas y notificaciones.


Flujo del tráfico entre estos dominios: el terreno de calle llama directo a la puerta de enlace (API Gateway) por la red celular, sin pasar por el on-premise; los HHT de bodega se comunican por WLAN local con el WMS del sitio; el WMS publica al broker local (A-03) que reenvía a SQS FIFO en la nube; el cross-dock (E-01) publica sus eventos críticos directo a SQS FIFO y solo el detalle del WMS del cross-dock viaja a Talca, de modo que lo crítico no depende de Talca (D-AL-04); Greengrass envía por IoT Core; y la Capa 4 consume las colas y alcanza el ERP únicamente a través de la capa anticorrupción (A-04), con una sola puerta hacia el legado.

### Mensajería (ADR-05)

Los planos de mensajería y su emplazamiento físico se describen en la Tabla 35:

**Tabla 35** — Mensajería: planos y emplazamiento físico

| Plano | Tecnología | Emplazamiento | Rol |
|---|---|---|---|
| Buffer local de sitio | RabbitMQ (A-03) | VM-03 Talca (≈ 3 M mensajes) · VM-C04 Concepción · broker en E-01 | Sostiene la autonomía de 24 h del centro de distribución. Es lo que permite que la bodega reciba, prepare y despache con el enlace caído. |
| Trabajo y reconciliación | SQS FIFO (N-09) | Nube | Orden garantizado por partición (MessageGroupId = sitio) y deduplicación; alimenta a celery-reconciliation y celery-erp-sync. |
| Tareas derivadas de eventos | Celery workers (Fargate) | Nube | Cada evento de negocio despacha tareas asíncronas: notificaciones, actualización analítica, emisión de DTE y transmisión EDI. |
| Transporte hacia la nube | Shipper en VM-03 (modo wms_only) | On-premise → nube | HTTPS 443 sobre VPC Endpoint SQS/PrivateLink (D-AL-03). AMQPS 5671 queda reservado a broker con broker on-premise. |

### Costuras híbridas: amarre con la arquitectura física

La vista de integración y la vista física describen los mismos puntos de contacto. La Tabla 36 amarra ambas: cada costura física se cruza con la integración lógica que la usa, su contrato y sus extremos.

**Tabla 36** — Costuras híbridas: amarre con la arquitectura física

| Costura física | Integración lógica | Contrato | Extremos |
|---|---|---|---|
| C1 — VPN corporativa | portadora de INT-06 e INT-12 | IPsec/IKEv2, BGP, MTU 1436 | D-01 ↔ VGW |
| C2 — Réplica WMS → Aurora | INT-12 | WAL lógico / DMS CDC | VM-02 ↔ Aurora |
| C4 — Broker → SQS FIFO | INT-03 | AsyncAPI 2.6 | VM-03 ↔ N-09 |
| C5 — ERP por la ACL | INT-06 | OpenAPI 3.1 de Puelche | VM-04 ↔ celery-erp-sync |
| C6 — Identidad | INT-13 | Realm cifrado por S3 | Keycloak maestro ↔ A-05 / VM-C03 |
| C7 — IoT Greengrass | INT-05 | MQTTS 8883, X.509 | B-02 ↔ N-08 |
| C8 — Observabilidad | INT-14 | OTLP | F-01 ↔ CloudWatch |
| C10 — Apps de terreno | INT-01 / INT-02 | OpenAPI 3.1 | C-01 / C-02 ↔ Capa 3 |
| C13 — Cross-dock | INT-04 | AsyncAPI 2.6 / AMQPS | E-01 ↔ VM-03 y ↔ N-09 |
| C14 — Notificaciones y EDI | INT-08 / INT-11 | GS1 / API de notificaciones | Celery workers ↔ terceros |
| C15 — Portales de la DMZ | INT-01 (lectura de stock, crédito y cobranza) | OpenAPI 3.1 | N-01/N-02/N-03 ↔ Capa 3 |
| C16 — Pago Transbank | INT-09 | API de la pasarela | Módulo integraciones ↔ Webpay |

### Carga y descarga masiva de datos

- **Carga inicial de maestros e históricos (ERP y WMS):** proceso ETL por lotes con inserción idempotente por UUID, en ventana sin operación. Control: conteo previo y posterior por lote, conciliación de totales y bitácora de carga (quién, cuándo, lote, resultado); los rechazados van a cuarentena con reproceso.
- **Descarga regulatoria (traza de lote, temperaturas, DTE, geolocalización):** exportación asíncrona a CSV o Parquet, firmada y con suma de verificación. Control: registro de la extracción (solicitante, filtro, resultado) y control de acceso a datos sensibles (RT-16.09).
- **Sincronización masiva de turno (terreno):** sincronizadores con partición y reanudación más deduplicación; los medios van a S3 por objeto. Control: turno completo ≤ 10 min; métricas de sincronización en la Capa 8.
- **Interfaces periódicas con terceros:** colas con batch_id y confirmación por lote. Control: monitoreo de DLQ y acuse por lote en la bandeja de excepciones.


Regla: ninguna carga masiva se ejecuta dentro de la ventana crítica 05:30–07:00, y toda carga queda registrada y es auditable.

## Arquitectura de seguridad

Esta solución de seguridad se estructura sobre: Zero Trust, capa expuesta, identidad y accesos, cifrado y controles, esto debido a que el perímetro de esta solución no es un edificio corporativo sino un entorno distribuido con alta rotación de personal externo y dispositivos compartidos en terreno.

### Principios rectores

1. **Zero Trust conforme a NIST SP 800-207**. Verificación explícita de cada solicitud, privilegio mínimo y presunción de compromiso. La red interna no confiere confianza.
2. **Seguridad desde el diseño y por defecto**. Modelado de amenazas STRIDE documentado por cada componente y por cada integración externa, antes de implementar.
3. **La identidad es el perímetro**. Autoridad única de identidad mediante Keycloak y toda decisión de acceso se toma sobre el token, no sobre la dirección de red de origen.
4. **Sin conexiones entrantes al on-premise**. Todo tráfico desde on-premise hacia la nube es saliente. Las dos únicas excepciones son las conexiones entrantes de DMS hacia PostgreSQL y de celery-erp-sync hacia ACL, declaradas, acotadas al túnel IPsec autenticado y auditadas.
5. **Cifrado en tránsito y en reposo sin excepciones**. TLS 1.3 mínimo para el transito, cifrado en reposo del 100 % de los datos con claves gestionadas en KMS/HSM y separación de funciones en su custodia.
6. **La seguridad no puede detener la ventana crítica**. Ningún control de seguridad puede introducir una dependencia en línea dentro de 05:30 hasta las 07:00 ni en las 14 h de terreno sin señal. La autenticación de terreno se resuelve sin red por diseño.
7. **Operable por cuatro personas**. El CLIENTE tiene 4 personas de TI, por lo que se privilegian servicios administrados y un SOC contratado 24/7 por sobre plataformas que exijan operación local especializada.
8. **Evidencia inalterable**. Todo evento de seguridad y toda acción de negocio quedan en un registro inalterable y con retención declarada; ni un administrador puede modificarlo.


### Modelo Zero Trust aplicado

#### Zonas y flujos

En el texto las zonas y su flujo son la zona pública como los clientes del canal moderno, transportistas para los 160 conductores y 180 proveedores que ingresan únicamente por la DMZ en nube en CloudFront más AWS WAF v2 más Shield Advanced hacia el Amazon API Gateway con OIDC, cuotas, esquema y validación de carga útil, para la zona de aplicación se usa ECS Fargate más workers y Keycloak IdP maestro como autoridad única que sirve a las zonas de datos como Aurora PostgreSQL, DynamoDB y S3 con Object Lock, en subredes privadas sin salida, para la zona on-premise se usa VLAN 10 MGT, 20 SRV, 30 OPS, 40 WKS, 50 IOT, firewall D-01 UTM en HA como Customer Gateway y caché Keycloak de solo lectura TTL 8 h que se conecta con la nube por VPN/IPsec saliente, por último para la zona de terreno se usa apps Kotlin offline-first más MDM; HHT compartidos en cámara a −22 °C que no tiene perímetro.

Reglas de zona declaradas:

- La única exposición pública es la DMZ en nube ya sea CloudFront hacia el WAF y hacia el API Gateway. Las consolas internas no pasan por ahí, por lo que entran por intranet o VPN.
- La zona de datos no tiene salida a internet y se consume por VPC Endpoints o PrivateLink.
- Desde la zona on-premise no se acepta ninguna conexión entrante salvo las dos excepciones D-AL-05.
- La zona de terreno no tiene perímetro, por lo que se protege con identidad, cifrado local, MDM y borrado remoto.


### Capa expuesta

- **Publicación exclusiva por capa de borde**. CloudFront como único origen público ya que los orígenes están restringidos y no se alcanzan directamente.
- **WAF con reglas gestionadas y personalizadas**. se usará AWS WAF v2 que es un conjunto gestionado OWASP que contiene Top 10 más reglas propias por API.
- **Protección DDoS en capas 3, 4 y 7**. AWS Shield Advanced con respuesta gestionada.
- **Gestión automatizada de certificados**. Inventario centralizado, renovación automática y alerta anticipada a 30 días del vencimiento.
- **Puerta de enlace con controles completos**. API Gateway con autenticación OIDC, autorización por rol, cuotas y límites de tasa por cliente, validación de esquema e inspección de carga útil.
- **Protección contra bots y abuso automatizado**. Reto progresivo en los puntos de entrada públicos sin degradar la accesibilidad.
- **Superficie de exposición declarada**. Inventario completo de servicios, protocolos, puertos por sitio y por zona.


### Desarrollo seguro y cadena de suministro

- **Matriz de controles.** Matriz trazable con control, implementación concreta y evidencia.
- **Firma y procedencia.** Artefactos firmados y verificados.
- **Entornos de prueba.** Prohibido el uso de datos productivos reales sin anonimización.
- **Dependencias de terceros.** Proceso de aprobación con criterios de licencia, mantenimiento activo y ausencia de vulnerabilidades conocidas.


#### Superficie de exposición completa

**Tabla 45** — Superficie de exposición completa (RT-11.13)

| Zona / sitio | Servicios expuestos | Protocolos y puertos | ¿Alcanzable desde internet? |
|---|---|---|---|
| DMZ pública en nube | Portales N-01, N-02 y N-03 sobre Puelche | HTTPS (TLS 1.3) | Sí, por CloudFront con WAF y Shield |
| Zona de aplicación en nube | ECS Fargate y Keycloak maestro | Solo desde el ALB y la puerta de enlace | No |
| Zona de datos en nube | Aurora, DynamoDB y S3 | Solo por VPC Endpoint y PrivateLink | No |
| Talca (red interna) | Portal WMS, API WMS, PostgreSQL, broker AMQP y gestión SSM | HTTPS (TCL 1.3), TCP | No, solo por VPN Zero Trust |
| Talca (borde) | Clúster de firewall en HA | IPsec 500/4500 UDP | Solo terminación IPsec |
| Concepción (borde) | Greengrass hacia IoT Core (MQTT saliente) | MQTTS 8883 (X.509) | No; sin puertos entrantes |
| Concepción y cross-docking | Gabinete de borde (mini-PC) | IPsec 500/4500 UDP | Solo por VPN IPsec |
| Estaciones de trabajo | NA | MQTTS 8883 (X.509) por proxy | No |

Regla declarada: ningún nodo on-premise abre puertos entrantes. Toda gestión remota entra por el agente SSM sobre MQTTS 8883 (X.509) o por la VPN, nunca por un puerto publicado.

### Identidad, acceso y sesiones

#### Modelo de identidad

Como autoridad única en nube y cachés locales de solo lectura el Keycloak IdP maestro vive en ECS Fargate ubicado en sa-east-1 respaldado en Aurora y concentra todas las escrituras ya sean altas, bajas, cambios de rol, políticas y revocaciones. Para el VM-05 de Talca y el VM-C03 de Concepción operan cachés locales de solo lectura con TTL de 8 h que validan la firma OIDC de forma local. No existe un maestro on-premise ni promoción local a escritura.

- **Keycloak IdP maestro en la nube (autoridad única)** Integración mediante SCIM con el directorio corporativo del CLIENTE por VPN saliente.
- **Caché local para Talca y Concepción (solo lectura por 8 horas)** Validación local de firma y emisión de sesiones sin conexión.


#### Federación, SSO y factores

- **SSO con cierre propagado.** Inicio de sesión único para todos los módulos con cierre de sesión propagado a todos en tiempo real.
- **Factores.** MFA obligatoria para administradores, privilegios y todo acceso externo.
- **RBAC + ABAC.** Control por roles complementado con atributos donde el proceso lo exija.
- **Credenciales firmadas y de vida breve.** Sin identificadores de sesión en la URL.
- **Ciclo de vida auditado.** Creación, modificación, elevación, bloqueo y baja de cuentas.
- **Aprovisionamiento automatizado.** Alta/baja ligadas al ciclo laboral.
- **Perfil operacional.** Autenticación adecuada al caso: guantes térmicos, uso a una mano, dispositivos compartidos y sin correo electrónico.


#### Política de sesión

- **Duración.** La credencial de acceso dura 30 minutos y la credencial de identidad dura 1 hora.
- **Renovación.** Credencial de refresco rotatoria por 30 días.
- **Inactividad.** Caducidad por inactividad según perfil.
- **Revocación y concurrencia.** Revocación inmediata ante baja, compromiso o suspensión.
- **Operación desconectada.** Token de turno de 8 horas en bodega o 14 horas en terreno que qpreventa y reparto).


#### Autenticación en terreno

Las condiciones estipuladas son los guantes térmicos a −22 °C, operación a una mano durante la descarga, uso de pie y a la intemperie en la puerta del local, dispositivos compartidos entre turnos en bodega y 38 % de rotación anual en preparación.

- El operador autentica con conexión al inicio de turno ya sea con un PIN de 6 dígitos y descarga un token cifrado de vida acotada al turno.
- Durante el turno el PIN desbloquea el token local que no se autentica contra el IdP por transacción.
- El dispositivo es un factor de posesión enrolado por MDM y el PIN es el segundo factor.
- Los datos locales están cifrados y admiten borrado remoto selectivo por lo que se borra la aplicación y su caché.


### Cifrado y gestión de claves

#### En tránsito

El cifrado en tránsito se declara por trayecto:

- **TLS 1.3 mínimo y obligatorio.** Prohibición expresa de TLS 1.0 y 1.1, conjuntos de cifrado modernos y HSTS con precarga en las superficies web.
- **Tráfico interno cifrado.** Capa de aplicación hacia la base de datos, broker y caché, mediante mTLS o cifrado nativo del protocolo.
- **On-premise desde o hacia la nube.** IPsec/IKEv2 cifrado, BGP y MTU 1436.
- **Respaldos y replicación.** TLS 1.3 en tránsito, incluida la replicación hacia us-east-1.
- **Gestión de certificados.** Inventario centralizado, renovación automática y alerta anticipada a 30 días del vencimiento.


#### En reposo

**Tabla 51** — Cifrado en reposo por componente

| Elemento | Cifrado | Gestión de claves |
|---|---|---|
| Almacenamiento del clúster | LUKS con NVMe con autocifrado | CMK dedicada on-premise |
| NAS de respaldo | LUKS | CMK independiente de la de producción |
| PostgreSQL on-premise | Cifrado del sistema de archivos subyacente | CMK dedicada |
| Aurora, DynamoDB y S3 | KMS | AWS KMS con CMK |
| Estaciones de trabajo | LUKS | Servidor de claves corporativo |
| Terminales de terreno | Cifrado del dispositivo | MDM |

Las claves de datos se rotan anualmente y las claves maestras siguen el calendario del proveedor de KMS/HSM. La rotación es en línea y no degrada el servicio, y los respaldos conservan la versión de clave necesaria para permitir una restauración auditable.

#### Cifrado a nivel de campo

El cifrado a nivel de campo se declara por conjunto de datos:

- **Comportamiento de pago y antecedentes comerciales del cliente.** Cifrado a nivel de campo con clave en KMS.
- **Datos de geolocalización de personas.** Cifrado a nivel de campo, retención de 12 meses y registro de consultas.
- **RUT de clientes en bases y registros.** Pseudonimización mediante cifrado a nivel de campo.


### Clasificación de la información y controles por nivel

**Tabla 53** — Clasificación de la información y controles por nivel (RT-11.03)

| Nivel | Ejemplos en Puelche | Controles mínimos |
|---|---|---|
| Restringido | Claves KMS/HSM, credenciales de servicio y firma privada de DTE | Cifrado a nivel de campo, KMS/HSM, MFA, acceso nominativo con aprobación y registro de consultas |
| Confidencial | Base del WMS | Cifrado en reposo y a nivel de campo, RBAC/ABAC, registro de consultas, retención declarada |
| Interno | Registros de operación, métricas y configuraciones | Acceso por rol y segregación de funciones |
| Público | Catálogo público de productos sin precios | Sin controles de confidencialidad, integridad vía CI/CD |

### Detección, respuesta y evidencia

- **Registro centralizado e inalterable.** Todos los eventos de seguridad se centralizan con ingesta continua.
- **Retención de eventos de seguridad.** 12 meses en línea + 24 meses en archivo recuperable que corresponden a 36 meses en total.
- **Auditoría de negocio.** 7 años en CloudWatch Logs con exportación periódica a S3 Glacier.
- **SIEM con casos de uso del negocio.** Security Lake con 6 casos de uso propios de la operación logística que corresponde a la alerta nocturna fuera de patrón, acceso remoto anómalo, MFA en TI en la sombra, exfiltración de datos de stock, escalada de privilegios y respuesta a incidente reglamentario.
- **EDR en nube y on-premise.** Agentes en todos los nodos on-premise, estaciones y cargas en nube.
- **SOC 24/7.** Cobertura contractual de ambos dominios con dotación mínima declarada.
- **Gestión de vulnerabilidades.** Plazos contractuales con crítica de 7 días, alta de 15 días, media de 30 días.
- **Respuesta a incidentes.** Plan con clasificación, cadena de escalamiento, plazos y responsables.
- **Simulación de incidentes.** Ejercicios al menos una vez al año con participación del CLIENTE.
- **Pruebas de intrusión.** Anuales por un tercero independiente del adjudicatario y previas a cada paso a producción.


### Datos personales, residencia y transferencia internacional

- **Residencia primaria.** Toda la operación productiva reside en AWS sa-east-1. El dominio on-premise reside en las instalaciones del CLIENTE en Chile.
- **Región secundaria.** us-east-1 es exclusivamente como ambiente de recuperación ante desastres.
- **Transferencia internacional.** La replicación hacia us-east-1 constituye una transferencia internacional de datos personales en el sentido de la Ley 21.719.
- **Resguardos declarados.** Se cuenta con un cifrado en reposo con CMK gestionada por el CLIENTE y en tránsito extremo a extremo, luego un acuerdo de tratamiento de datos con el proveedor de nube con cláusulas de transferencia, luego la minimización que la región secundaria no se usa para explotación analítica ni para consultas de negocio, solo para continuidad, luego los datos de geolocalización de personas quedan excluidos de la replicación transfronteriza y se conservan solo en sa-east-1 con retención de 12 meses y por último el registro de la transferencia en el inventario de tratamientos.
- **Aprobación del CLIENTE.** Si el CLIENTE no aprueba la transferencia a us-east-1, la alternativa declarada es la continuidad intrarregional en sa-east-1 entendida como no salir de la región AWS sa-east-1.
- **Eliminación segura.** Procedimiento verificable de eliminación al vencimiento, con registro inalterable.
- **Exportabilidad.** Capacidad de exportar la totalidad de la información del CLIENTE en formatos abiertos y documentados, en cualquier momento del contrato y sin costo adicional.
- **Derechos de los titulares.** Acceso, rectificación, cancelación, oposición, portabilidad y bloqueo temporal.


Dos de los resguardos de esta tabla son decisiones de diseño y no solo cláusulas contractuales, y se propagan a la sección de arquitectura de despliegue de este capítulo y a la arquitectura lógica, por la que la región secundaria sostiene continuidad y no se explota analíticamente, y la exclusión de los datos de geolocalización de personas de la replicación transfronteriza.

#### Derechos de los titulares, política de privacidad y EIPD

**EIPD.** Evaluación de impacto obligatoria por tratamiento masivo con 14.200 clientes y con monitoreo sistemático. **Vigencia.** La Ley 21.719 rige desde el 01 de diciembre de 2026 y un proyecto de ley del Boletín 18.623-07 postergaría la vigencia al 01 de diciembre de 2027.

#### Base de licitud por tratamiento

**Tabla 58** — Base de licitud por tratamiento (Ley 21.719, Art. 12 y 13)

| Tratamiento | Base de licitud | Garantías clave |
|---|---|---|
| Geolocalización de trabajadores | Ejecución contrato más interés legítimo | finalidad operativa, sin control de jornada y cifrado de campo |
| Comportamiento de pago / crédito | Ejecución contrato más interés legítimo | Cifrado de campo con acceso restringido |
| Datos laborales | Obligación legal más ejecución contrato | acceso restringido a RRHH |
| Clientes como preventa, DTE y portal | Ejecución contrato más obligación legal | Sin marketing sin consentimiento |
| firma y foto | Ejecución contrato | Retención 6 años |
| Conductores externos | Consentimiento del titular | Datos mínimos más OTP |

## Arquitectura de despliegue

Arquitectura de despliegue de la solución: ambientes, redes y segmentación, alta disponibilidad, recuperación ante desastres y respaldos. Es autocontenida: los valores que declara se sostienen en los componentes especificados en las secciones anteriores de este capítulo.

### Ambientes de despliegue

Un cambio recorre tres ambientes antes de llegar a Producción: Desarrollo, QA y Preproducción. La marcha blanca de cada etapa ocurre ya en Producción, porque es operación supervisada con datos y usuarios reales en paralelo con la operación vigente. Un quinto ambiente, de Recuperación ante Desastres, sostiene la continuidad (RT-04.01): reside en us-east-1 para el dominio de nube, mientras que la recuperación del dominio on-premise la asume el CD Concepción, que forma parte de Producción. Los cinco ambientes están habilitados como condición del hito H3, aislados entre sí mediante cuentas AWS separadas bajo una organización centralizada de AWS Control Tower (aislamiento estricto + SCP), que se listan en la Tabla 62:

**Tabla 62** — Ambientes de despliegue

| Ambiente | Cuenta AWS | VPC | Región | Uso |
|---|---|---|---|---|
| Desarrollo | Cuenta 1 | 10.104.0.0/16 | sa-east-1 | Integración continua, pruebas unitarias automáticas |
| QA | Cuenta 2 | 10.103.0.0/16 | sa-east-1 | Pruebas funcionales, de integración y de regresión; análisis dinámico |
| Preproducción | Cuenta 3 | 10.102.0.0/16 | sa-east-1 | Aceptación, carga, resiliencia y ensayo del paso a producción |
| Producción | Cuenta 4 | 10.101.0.0/16 | sa-east-1 | Operación real (Multi-AZ), con los sitios on-premise; marcha blanca |
| Recuperación ante Desastres | Cuenta 5 | 10.201.0.0/16 | us-east-1 | Réplica en caliente del dominio de nube (RT-04.01) |

Reglas que gobiernan el modelo de ambientes:

- **Paridad Preproducción = Producción (RT-04.02).** versiones, configuración, dimensionamiento y topología de nube equivalentes. Diferencias declaradas: (1) se reduce o apaga fuera del horario de uso; (2) trabaja con datos sintéticos, con anonimización verificada con Amazon Macie (RT-11.25); (3) el sitio on-premise se emula en su propia VPC, con la misma imagen wms_only, el mismo broker y el mismo verificador local, sin túnel hacia las bodegas. Como la emulación no reproduce el hardware, la primera instalación de cada versión en los centros de distribución avanza sitio por sitio.
- **Desarrollo y QA.** aislados y reconstruibles desde código; Desarrollo con datos sintéticos o anonimizados y QA con datos de prueba controlados y versionados, restituidos a un estado conocido antes de cada ciclo de pruebas.
- **On-premise como producción.** el despliegue on-premise es producción con la imagen única wms_only; esa misma imagen recorre Desarrollo→QA→Preproducción en la nube antes del cutover en Talca (ventana de 24 h) y en Concepción. No se mantienen ambientes on-premise separados — la paridad la garantizan la imagen única y el IaC versionado.
- **Entrega continua.** el pipeline CI ejecuta compilación, pruebas unitarias, análisis estático, análisis de composición, escaneo de secretos y escaneo de imágenes de contenedor, con bloqueo automático del despliegue ante hallazgos críticos o altos.
- **Despliegue sin interrupción.** estrategia azul-verde con canario (despliegue gradual a un porcentaje pequeño de tráfico) en etapas, demostrada en Preproducción antes de cada paso a producción; reversión automatizada.
- **Configuración externalizada.** un mismo artefacto se promueve QA→Preproducción→Producción sin recompilación; los secretos viven en gestor de secretos con rotación automática, sin credenciales embebidas.
- **Datos no productivos.** Desarrollo, QA y Preproducción usan datos sintéticos generados desde la volumetría del Cap. 14 del caso; las plantillas próximas a producción pasan por anonimización/seudonimización verificable (Amazon Macie).
- **Sin acceso interactivo a producción.** los despliegues son exclusivamente por pipeline; el acceso administrativo excepcional es just-in-time vía AWS Systems Manager Session Manager con MFA, aprobación y sesión grabada.
- **Reducción de ambientes no productivos fuera de horario.** Desarrollo, QA y Preproducción se apagan o reducen fuera del horario de uso, con el ahorro reflejado en la estructura de costos (RT-15.02, RT-04.13).
- **Portal web (N-01/N-02/N-03).** la SPA Angular se publica por ambiente en S3+CloudFront (bucket y distribución por cuenta AWS) y su backend es la misma imagen Django del ambiente; entra a producción con el hito de enero 2029.


### Redes (topología, segmentación y conectividad)

#### WAN — doble camino con conmutación automática

Cada instalación dispone de dos caminos físicamente independientes con conmutación automática en < 30 s: fibra óptica más LTE empresarial en los CDs (Talca y Concepción), y Starlink más LTE empresarial en los cross-docks (Curicó, Chillán y Los Ángeles). El requisito exige ≤ 5 min declarados; el diseño opera en < 30 s. Los anchos de banda por sitio, en régimen y en peak, se declaran en la sección de dimensionamiento (Tabla 81).

Los cross-docks salen directo por Starlink a SQS/IoT/SSM y sincronizan detalle a Talca por AMQPS entre brokers (C-13). La pérdida total del enlace se cubre con la autonomía local de 24 h (CD) / 14 h (terreno), por lo que la redundancia de conectividad reduce la frecuencia de desconexión pero no es condición para operar.

#### VPN Site-to-Site (costura C1)

Extremos: D-01 Firewall/UTM (HA activo-pasivo) → Customer Gateway en cada CD; extremo cloud VGW del VPC Hub.

Protocolo: IPsec/IKEv2 cifrado, BGP, MTU 1436; 2 túneles (activo + standby). Conmutación < 30 s entre los dos caminos del sitio.

#### Segmentación de red (sin solapamiento)

La segmentación de red sin solapamiento se define en la Tabla 64:

**Tabla 64** — Segmentación de red (sin solapamiento)

| Dominio | Bloque | Segmentación |
|---|---|---|
| Talca | 10.1.x.x | VLAN 10 (MGT), 20 (SRV), 30 (OPS), 40 (WKS), 50 (IOT) |
| Concepción | 10.2.x.x | Misma segmentación VLAN |
| Cross-dockings | 10.3.x.x – 10.5.x.x | Red plana simplificada + salida SSM/IoT outbound |
| VPC Hub | 10.100.0.0/16 | Transit Gateway; adjuntos de VPN |
| VPC Producción | 10.101.0.0/16 | Multi-AZ: DMZ pública 10.101.1.0/24 (az1) y 10.101.2.0/24 (az2) — ALB/WAF/CloudFront origin/NAT GW y portales N-01/N-02/N-03 · subredes app y datos privadas |

Modelo Hub-and-Spoke con VPC de tránsito central: la comunicación cross-VPC pasa por el Transit Gateway (inspección) y los servicios AWS (S3, SQS, DynamoDB, KMS, SSM) se consumen por VPC Endpoints/PrivateLink sin tráfico por internet (RT-03.03).

#### Zero Trust — flujos permitidos

Todo el tráfico on-premise → nube es outbound (HTTPS/443, MQTTS/8883) sin conexiones entrantes salvo las dos excepciones controladas D-AL-05 sobre túnel IPsec autenticado; los flujos permitidos se listan en la Tabla 65:

**Tabla 65** — Zero Trust — flujos permitidos

| Flujo | Protocolo | Destino |
|---|---|---|
| Broker (shipper VM-03) → SQS FIFO | HTTPS 443 (VPC Endpoint SQS/PrivateLink) | AWS |
| Telemetría ADOT → CloudWatch | HTTPS 443 | AWS |
| Greengrass → IoT Core | MQTTS 8883 (X.509) | AWS |
| SSM Agent (todos los nodos) | HTTPS 443 saliente | SSM Endpoint regional |
| Sync WMS Concepción → Talca | TCP 8080 / 5432 | SRV-TALCA (on-prem) |
| Sync cross-dock → Talca (broker a broker) | AMQPS 5671 | SRV-TALCA (on-prem) |
| Caché Keycloak A-05/VM-C03 → S3 (import Realm) | HTTPS 443 (VPC Endpoint S3) | AWS (objeto cifrado) |
| Excepción: AWS DMS → PostgreSQL WMS (CDC) | TCP 5432 (over VPN) | VM-02 SRV-TALCA |
| Excepción: celery-erp-sync → ACL ERP | HTTPS 443 (over VPN) | VM-04 SRV-TALCA |

#### Capa pública (DMZ) y DNS

Primera línea: CloudFront + AWS WAF v2 (OWASP Top 10 + reglas personalizadas) + Shield Advanced; autenticación API Gateway con Keycloak OIDC, cuotas por cliente y validación de esquema.

DNS: Route 53 con health checks activos; routing por latencia en operación normal y failover automático hacia us-east-1 en contingencia.

### Alta disponibilidad

#### Capa cloud (sa-east-1) — Multi-AZ

La capa cloud y su estrategia Multi-AZ se resumen en la Tabla 66:

**Tabla 66** — Capa cloud (sa-east-1) — Multi-AZ

| Componente | AZ primaria | AZ secundaria | Failover automático |
|---|---|---|---|
| Aurora PostgreSQL | sa-east-1a (Writer) | sa-east-1b / sa-east-1c (2 Readers/Failover) | < 30 s |
| DynamoDB | Multi-AZ nativo | — | Transparente |
| ECS Fargate | sa-east-1a | sa-east-1b | Application Auto Scaling re-scheduling |
| ElastiCache Redis | sa-east-1a (Primary) | sa-east-1b (Replica) | < 60 s |
| ALB | sa-east-1a | sa-east-1b | Transparente |
| NAT Gateway | sa-east-1a | sa-east-1b (independiente) | Routing automático |

Nivel de servicio de extremo a extremo sobre la transacción crítica de negocio: ≥ 99,9 % mensual (menos de 8,76 h al año). Es el compromiso contractual penalizable y es distinto de la disponibilidad de la infraestructura del recinto (99,95 % por componente), que es un medio para alcanzarlo.

#### Capa on-premise

La capa on-premise y su diseño por capa se resumen en la Tabla 67:

**Tabla 67** — Capa on-premise

| Capa | Diseño | Sustento |
|---|---|---|
| Cómputo | Clúster virtualizado 3 nodos con replicación síncrona Ceph (factor 2, quórum propio) | La sección de dimensionamiento y plan de capacidad de este documento; elimina el SPOF de un par sin quórum |
| Almacenamiento | RAID 10 (BD transaccional NVMe, IOPS > 100 k) y RAID 6 con hot-spare (evidencia/logs) | ADR-10 · RT-03.14/RNF-13.04/13.05 |
| Red | Par de firewall UTM (HA A/P), 2 switches core + switch de gestión | RNF-13.03 |
| WAN | Doble camino fibra/Starlink + LTE | RT-03.17 |
| Energía | UPS doble conversión 6 kVA N+1 (≥ 30 min a plena carga, RT-06.07) + generador 12 kVA estanque 24 h (RT-06.08) + ATS | Sala de Servidores v02, sección de energía |
| Clima | Clima de precisión N+1 ASHRAE TC 9.9, PUE de diseño 1,7 | Sala de Servidores v02, sección de climatización |
| Recinto | Sala mediana, 4 gabinetes; disponibilidad de infraestructura de 99,95 % por componente | Numerales 6.1 y 7.2 de las Transversales; sección de sitio principal (CD Talca) |

VMs dimensionadas con headroom ×1,5 (RNF-19.04) para tolerar 3.900 entregas/día en el peak de septiembre. SPOF declarados y mitigados (RT-02.11): periféricos de andén (respaldo manual), clúster Talca sin SPOF estructural, Concepción nodo único (autonomía 24 h + DRP), cross-dock mini-PC único (ventana de 3 h + sincronización diferida).

### Recuperación ante desastres

#### DRP nube (sa-east-1 → us-east-1) — activo-pasivo warm standby (réplica pasiva lista para promover en minutos)

Mecanismo: Aurora Global Database (réplica us-east-1, lag < 1 s) · DynamoDB Global Tables · S3 CRR (RTC < 15 min) · AWS DMS CDC del PostgreSQL WMS on-premise (lee wal_level=logical; si la VPN cae, encola y reanuda sin pérdida).

Objetivos: RTO ≤ 4 h / RPO ≤ 15 min; RPO declarado de mensajes no críticos ≤ 24 h, reducido a ≤ 15 min para los críticos con patrón outbox dual-write (escritura simultánea en BD y cola para garantizar consistencia).

Modalidad justificada: activo-pasivo; activo-activo duplicaría la infraestructura transaccional (\~105 TPS peak) con reconciliación de doble escritura sin beneficio frente al RTO comprometido (ADR-09).

Procedimiento: decisión de failover manual con disparador declarado (health check de la región primaria < 5 min) y protección contra conmutación innecesaria (confirmación SNS + autorización); pasos 4–7 automatizados por AWS Systems Manager Automation (promoción Aurora 15–20 min, escalado ECS, actualización DNS 45–60 min). El RTO se cumple porque la réplica es legible y la región DR está "caliente" (escalable < 30 min a carga completa).

Retorno (failback): procedimiento documentado en 6 pasos — re-sincronización con catch-up verificado, reconciliación de transacciones de la contingencia contra la bitácora (RT-03.12), transferencia de eventos pendientes, conmutación coordinada de DNS, validación funcional e informe con tiempo real.

Pruebas: conmutación real ≥ 2 veces/año con informe de RTO/RPO efectivos y plan de corrección de brechas.

Residencia y transferencia internacional de datos: la replicación hacia us-east-1 constituye una transferencia internacional de datos personales y se rige por los resguardos declarados en la sección de arquitectura de seguridad de este documento, en la subsección de datos personales, residencia y transferencia internacional: cifrado con CMK gestionada por el CLIENTE, acuerdo de tratamiento con cláusulas de transferencia, minimización (la región secundaria no se explota analíticamente, solo sostiene continuidad), exclusión de los datos de geolocalización de personas de la replicación transfronteriza (permanecen solo en sa-east-1 con retención de 12 meses) y registro en el inventario de tratamientos. La residencia queda sujeta a aprobación expresa del CLIENTE. Si no la aprueba, la alternativa declarada es la continuidad intrarregional dentro de sa-east-1, que consiste en una tercera AZ ampliada más respaldo inmutable regional. Esta alternativa no es un segundo sitio geográfico ni usa Talca o Concepción para la carga cloud, ya que AWS no tiene región en Chile. Cubre falla de AZ y corrupción de datos, pero degrada el RTO ante una caída de toda la región sa-east-1 a 24–72 h desde el respaldo inmutable (alternativa D del ADR-09).

#### DRP local (Talca → Concepción)

Promoción controlada del WMS edge (VM-C01) mediante procedimiento de 5 pasos; Concepción ya opera autónoma (latencia ≤ 1 s de picking, RNF-05.01). RTO +1–2 h para la bodega.

Identidad sin conmutación local: el maestro Keycloak está en la nube y las cachés A-05/VM-C03 siguen validando firmas offline — el DRP de identidad es la misma autoridad en nube, sin promoción local a maestro (elimina una clase entera de riesgos de DR).

#### DRP de la identidad (ADR-06)

El maestro vive en la nube (Multi-AZ) con réplica DR us-east-1; las cachés locales son de solo lectura. No existe maestro local a promover, por lo que la identidad no depende del switchover.

### Respaldos — esquema 3-2-1-1-0

Esquema único para toda la arquitectura híbrida (nube + on-premise):

- **3 copias de los datos.** (1) Datos activos sa-east-1 + WMS activo Talca; (2) Snapshot automatizado Aurora + respaldo local on-premise (D-05); (3) Backup exportado a S3.
- **2 medios.** PostgreSQL/Aurora y S3 (almacenamiento de objetos).
- **1 copia fuera del sitio.** S3 Cross-Region Replication → bucket en us-east-1.
- **1 copia inmutable.** S3 Object Lock (WORM, Compliance Mode) + AWS Backup Vault Lock (ni el root puede eliminarla); s3-documents-legal y s3-audit-logs en Compliance, no Governance.
- **0 errores.** Restore testing automatizado mensual (Lambda) + verificación de restauración local + prueba DR semestral.


D-05 (NAS local con WORM) es la copia local de recuperación rápida y NO cuenta como la pierna inmutable; permite restaurar el WMS en ≤ 4 h sin depender del enlace WAN. RPO ≤ 15 min por AWS DMS CDC del WAL lógico (wal_level=logical) hacia la nube antes de la copia local.

Custodia física: medio de respaldo transportable, cifrado y rotado semanal, trasladado bajo custodia acreditada a bóveda externa distinta del sitio primario; la pierna inmutable S3 es complementaria, no reemplaza la custodia física.

El plan AWS Backup se detalla en la Tabla 69:

**Tabla 69** — Respaldos — esquema 3-2-1-1-0

| Recurso | Frecuencia | Retención | Destino |
|---|---|---|---|
| Aurora PostgreSQL | Diario + PITR (restauración a un instante específico) continuo | 35 días | Backup Vault (cifrado CMK) |
| DynamoDB | Diario (On-Demand) | 35 días | Backup Vault |
| EFS | Diario | 30 días | Backup Vault |
| EBS | Diario (snapshots) | 14 días | Backup Vault |
| S3 documentos legales | Continuo (versioning + Object Lock) | 6 años | S3 + réplica CRR |
| Logs de seguridad/auditoría | Continuo | 7 años (Object Lock) | S3 archivo |

Vault Lock con enfriamiento de 3 días y retención mínima de 1 año; una vez bloqueado, ni la cuenta raíz puede eliminar respaldos. Retención sanitaria: trazabilidad 5 años + vida útil, consistente con el lago analítico S3 y el repositorio de datos históricos.

## Dimensionamiento y plan de capacidad

Volúmenes, concurrencia, crecimiento y umbrales de desempeño. Cierra las dieciséis dimensiones del numeral 14.2 del caso con su valor, su método y su supuesto.

### Criterios y método de dimensionamiento

El dimensionamiento se deriva de la volumetría real del Caso (Tabla 14.1 / Cap. 14 y 15), no de promedios genéricos, dado el perfil de carga no plano:

- **Preventa:** 09:00–18:00 (62 preventistas con EC55).
- **Preparación (pick duro):** 22:00–06:00 (120 terminales RF, −22 °C).
- **Despacho:** 05:30–07:00 (\~96 camiones; 42 propios + 54 transportistas).
- **Sincronización de flota:** 17:00–20:00 (\~270 dispositivos remotos).
- **Peak de septiembre:** ≈ 2× el volumen regular durante tres semanas.


Reglas que gobiernan el dimensionamiento:

- **Carga de diseño.** peak de septiembre (2.600 entregas/día) × 1,5 = 3.900 entregas/día toleradas sin degradación.
- **TPS de diseño.** burst ×3 → \~105 TPS (ver la subsección de concurrencia y TPS de diseño).
- **Crecimiento obligatorio.** la solución soporta 3× la volumetría inicial en 3 años sin rediseño (misma topología). El margen físico resultante es exigencia normativa, no capacidad ociosa financiada.
- **Umbrales.** percentil p95 en toda medición (Tabla 15), con umbrales por operación.
- **Sin capacidad ociosa financiada.** el cómputo elástico en nube escala automática (ADR-12); el on-premise se dimensiona al margen útil sin sobrecompra.
- **Coherencia interna.** los totales de esta parte concuerdan con la Tabla 14.1 (volumetría), el dimensionamiento de esta sección y los ADR (ADR-01, 04, 10, 12).


### Volumetría de referencia (Tabla 14.1 Caso 02)

#### Valores base de dimensionamiento

Los valores base de dimensionamiento se consolidan en la Tabla 73:

**Tabla 73** — Valores base de dimensionamiento

| Magnitud | Valor base |
|---|---|
| Clientes activos / puntos de entrega | 14.200 |
| Pedidos | 31.000 / mes |
| Líneas de pedido | 260.000 / mes |
| Unidades despachadas | 2.400.000 / mes |
| SKU activos | 8.400 |
| Posiciones de almacén (Talca) | 11.400 (87 % ocupación) |
| Entregas / día (régimen normal) | 1.400 |
| Entregas / día (peak septiembre) | 2.600 |
| Kilometraje | ≈ 420.000 km / mes |
| Documentos tributarios | ≈ 34.000 / mes |
| Camiones con cadena de frío | 18 |
| Puntos de medición de temperatura | 28 (≈ 7 módulos Ebyte de 4 canales) |
| Sitios on-premise con cómputo | 5 (Talca, Concepción, Curicó, Chillán, Los Ángeles) — de las 6 instalaciones que declaran la Tabla 14.1 y RT-21.16; la 6.ª es la casa matriz de Talca, sin nodo propio |

Nota de coherencia (instalaciones): la Tabla 14.1 y RT-21.16 reportan 6 instalaciones (7 a tres años); el despliegue físico ubica cómputo en los 5 sitios on-premise listados + borde en terreno (calle y 14.200 puntos). La divergencia 5/6 (Tabla 14.1 frente a lo declarado en el caso) está declarada en las consultas al mandante (Art. 43.3) y no altera el dimensionamiento: el cómputo se emplaza en los 5 sitios, la 6.ª instalación es de red/almacenamiento sin nodo de cómputo propio.

#### Proyección a 3 años (Caso 02)

La proyección a 3 años por magnitud se presenta en la Tabla 74:

**Tabla 74** — Proyección a 3 años (Caso 02)

| Magnitud | Base (año 0) | Año 3 | Variación |
|---|---|---|---|
| Clientes | 14.200 | 15.500 | +9 % |
| Pedidos / mes | 31.000 | 36.000 | +16 % |
| Líneas / mes | 260.000 | 305.000 | +17 % |
| Entregas / día (normal) | 1.400 | 1.650 | +18 % |
| Entregas / día (peak) | 2.600 | 3.100 | +19 % |
| Kilometraje / mes | 420.000 km | 480.000 km | +14 % |
| DTE / mes | ≈ 34.000 | ≈ 40.000 | +18 % |
| Instalaciones | 6 (5 con cómputo) | 7 | — |

Los recursos se dimensionan, además, para 3× la volumetría inicial sin rediseño (RT-09.03): la proyección real del Caso a 3 años (+16–19 %) queda muy por debajo del límite de diseño, dejando margen ante crecimiento mayor al modelado (ADR-12).

#### Volumetría de sistema del numeral 14.2 — las dieciséis dimensiones

El numeral 14.2 del caso entrega dieciséis dimensiones a estimar y advierte que un dimensionamiento basado en el promedio diario estará equivocado. Las dieciséis se declaran en la Tabla 72 con su valor, su método y el supuesto que las sostiene. Ninguna queda sin valor.

**Tabla 72** — Volumetría de sistema del numeral 14.2: las dieciséis dimensiones con su método y su supuesto

| Dimensión del numeral 14.2 | Valor declarado | Método y supuesto |
|---|---|---|
| Transacciones por segundo en régimen normal | ≈ 35 TPS | Suma de flujos concurrentes de la peor ventana: 20 TPS de confirmación de preparación, 8 TPS de preventa y 7 TPS de movimientos y sincronización (subsección de TPS estimados) |
| Transacciones por segundo en el peak de la ventana de despacho 05:30–07:00 | ≈ 1,7 TPS en ráfaga | 1.400 confirmaciones de carga, 1.400 timbrados de guía, 96 vinculaciones conductor–camión y 96 cierres de ruta, concentrados en los primeros 20 minutos de la ventana. La ventana es crítica por indisponibilidad cero, no por volumen: el cuello de botella está en la preparación nocturna |
| Transacciones por segundo en el peak de septiembre | ≈ 105 TPS | 35 TPS × burst 3, que cubre el doble de volumen estacional más la ráfaga de sincronización de flota de 17:00 a 20:00 |
| Personas usuarias registradas, internas y externas | ≈ 620 internas · ≈ 14.400 externas | Internas: 62 preventistas, 42 conductores propios, ≈ 160 conductores de terceros, 310 personas de centro de distribución, ≈ 40 de administración y gerencia, 4 de TI. Externas al cierre de la Etapa 2: 14.200 clientes con autoatención, 180 proveedores y 10 transportistas |
| Personas usuarias concurrentes en peak | ≈ 510 | 62 preventistas + ≈ 200 conductores + 120 terminales de preparación + 110 estaciones de centro de distribución + ≈ 20 de supervisión y mesa, según la ventana de solapamiento (subsección de usuarios y terminales concurrentes) |
| Dispositivos de terreno en operación simultánea | ≈ 270, hasta ≈ 300 en peak | Parque de terminales de preventa, reparto y cámara con 20 % de reserva (subsección de usuarios y terminales concurrentes) |
| Volumen anual de almacenamiento transaccional | ≈ 375 GB/año | Crecimiento del maestro de bodega y del transaccional de nube desde los 1.890 GB asignados hacia los 5,7 TB proyectados a 5 años (subsección de almacenamiento) |
| Volumen anual de almacenamiento de evidencia de entrega, firmas y fotografías | ≈ 100 GB/año | 420.000 entregas al año × ≈ 230 KB por entrega (una firma de ≈ 30 KB más una a dos fotografías comprimidas de ≈ 200 KB), más la evidencia de las ≈ 900 devoluciones mensuales. Con retención de 6 años y almacenamiento por niveles, ≈ 600 GB al término del contrato |
| Volumen anual de almacenamiento de series de temperatura y de posicionamiento | ≈ 3,3 GB/año en crudo · ≈ 0,8 GB/año consolidado | Temperatura: 46 fuentes × 1 muestra cada 5 min × 365 días. Posicionamiento: 42 camiones × 1 posición cada 30 s × 12 h × 300 días. El crudo vive 30 días con expiración automática y la serie consolidada se conserva en formato columnar comprimido: 5 años para temperatura y 12 meses para geolocalización de personas |
| Volumen total de datos históricos a migrar | ≈ 30 GB de datos estructurados | Maestros completos (14.200 clientes, 8.400 productos, 180 proveedores), ventas y pedidos de 3 años (≈ 9,4 millones de líneas × ≈ 1 KB), movimientos de inventario de 2 años (≈ 3,4 millones × ≈ 0,5 KB), trazabilidad sanitaria de 5 años y cuentas por cobrar vivas más 2 años. El histórico documental permanece en el sistema de gestión, que sigue siendo la fuente tributaria |
| Número de integraciones y volumen de mensajes por integración | 15 integraciones · ≈ 150.000 mensajes/día | Desglose por integración en la Tabla 33 de esta parte, derivado de la volumetría del caso sobre 25 días hábiles |
| Ancho de banda requerido por sitio, en régimen y en peak | Talca 20→50 Mbps · Concepción 10→20 Mbps · cross-docking por enlace satelital | Dimensionado sobre la sincronización de flota en la ventana de retorno y el respaldo semanal a la nube, escalado al 3× de RT-09.03, con conmutación automática en menos de 30 s (subsección de ancho de banda WAN por sitio) |
| Volumen de datos generado por un dispositivo de reparto en un turno completo sin señal | ≈ 8–12 MB por turno | Ruta del día, maestro acotado de productos y precios, evidencia de entrega comprimida de ≈ 30 entregas y cola de escrituras pendientes |
| Tiempo de sincronización de la flota al regresar al centro de distribución | 100 % dentro de la ventana de retorno 17:00–20:00, por lotes de ≤ 10 min | ≈ 200 dispositivos × 10 MB (≈ 2 GB/día; ≈ 6 GB y ≈ 8 Mbps de punta en el 3× de RT-09.03), con sincronización particionada y reanudable por lotes |
| Contactos mensuales a la mesa de ayuda | ≈ 620/mes en régimen · ≈ 1.500/mes en marcha blanca | 620 personas usuarias internas × 1,0 contacto/mes en operación estabilizada, con factor 2,5 durante las oleadas de puesta en producción y +40 % en el peak de septiembre. Los clientes del canal tradicional no entran por esta mesa: se atienden por autoatención |
| Dotación de la mesa de ayuda y del equipo de operación | Mesa: 7 personas · Operación: NOC y confiabilidad como servicio gestionado | Erlang C sobre la hora punta (supuesto de diseño; los parámetros se calibrarán con datos de operación en el hito H5): ≈ 5 contactos/h con tiempo medio de operación de 8 min dan una intensidad de 0,67 Erlang, y 2 agentes cumplen el objetivo de 80 % atendido en 20 s. A eso se suman la cobertura de la ventana 05:30–07:00 y del turno nocturno de bodega, el segundo nivel y la supervisión: 3 agentes diurnos, 1 nocturno, 1 supervisor y 2 especialistas de segundo nivel |

Dos lecturas se desprenden de la tabla y gobiernan el diseño. La primera: el volumen de mensajes está dominado por las dos series de tiempo, la trazabilidad y la telemetría, que suman ≈ 112.000 de los ≈ 150.000 mensajes diarios y que por diseño no atraviesan la base transaccional. La segunda: la ventana crítica de despacho no es la de mayor carga, sino la de menor tolerancia a la indisponibilidad; el dimensionamiento del cómputo se rige por la preparación nocturna y el peak de septiembre, y el de la resiliencia por la ventana de despacho.

#### Volumen de mensajes por integración

El desglose por integración, derivado de la volumetría del caso sobre 25 días hábiles al mes con el peak de septiembre al doble, se presenta en la Tabla 33. Esta tabla sustenta el dimensionamiento de red, colas y almacenamiento de series de tiempo, y es referenciada por la vista de integración de este mismo subdocumento.

**Tabla 33** — Volumen de mensajes por integración, derivado de la volumetría del caso

| Integración | Volumen en régimen | Peak septiembre | Derivación |
|---|---|---|---|
| Capa anticorrupción del ERP (asíncrona) | ≈ 4.700 mensajes/día | ≈ 9.400 | 1.240 pedidos + 46 recepciones + 1.400 preparaciones + 1.400 evidencias de entrega + ≈ 600 recaudaciones |
| Documentos tributarios y acuse (SII, síncrona) | ≈ 2.700 mensajes/día | ≈ 5.400 | 34.000 documentos/mes más su acuse, sobre 25 días |
| Eventos de trazabilidad GS1 EPCIS | ≈ 52.000 eventos/día | ≈ 104.000 | 260.000 líneas/mes × 5 eventos de ciclo, sobre 25 días |
| Telemetría de cadena de frío (IoT Core) | ≈ 13.200 mensajes/día | sin variación | 46 fuentes (28 puntos de cámara + 18 termógrafos) × 1 muestra cada 5 min |
| Telemetría de flota | ≈ 60.500 mensajes/día | ≈ 72.000 | 42 camiones propios × 1 posición cada 30 s durante 12 h de ruta |
| Sincronización de terreno (colas de dispositivo) | ≈ 13.000 escrituras/día | ≈ 26.000 | 1.240 pedidos + 1.400 evidencias + 10.400 confirmaciones de preparación |
| Intercambio electrónico con el canal moderno (Etapa 2) | ≈ 550 mensajes/día | ≈ 1.100 | 136 pedidos/día × 4 mensajes (pedido, confirmación, aviso de despacho, acuse) |
| Notificaciones multicanal | ≈ 2.800 mensajes/día | ≈ 5.600 | hora estimada de llegada y acuse por entrega |
| Autorización de pago (POS móvil) | ≈ 500 mensajes/día | ≈ 1.000 | fracción del canal tradicional que migra de efectivo a pago electrónico |
| Servicio de mapas y geocodificación | ≈ 200 llamadas/día | ≈ 400 | una corrida de ruteo por zona más recálculos por incidencia |

El total en régimen es de ≈ 150.000 mensajes al día. Las cinco integraciones restantes del catálogo son de configuración y administración, con volumen despreciable frente a estas cifras.

### Concurrencia y TPS de diseño

#### Usuarios y terminales concurrentes

La concurrencia por rol y dispositivo se detalla en la Tabla 75:

**Tabla 75** — Usuarios y terminales concurrentes

| Rol | Concurrencia | Dispositivo |
|---|---|---|
| Preventistas | 62 simultáneos | Zebra EC55 (parque 62 + reserva 20 %) |
| Conductores (reparto) | \~200 simultáneos | Zebra TC58e (parque único 42 propios + \~160 externos + reserva) |
| Personal de centro de distribución | 310 (turno) | Estaciones y terminales fijas |
| Operarios de picking simultáneos (turno nocturno) | 120 | Zebra MC9400 Cold Storage (pool Talca 144 = 120 + 20 %; Concepción 30) |
| Terminales RF concurrentes | 120 (base de diseño) | Ídem |
| Call center / supervisión | \~20 | Estaciones |
| Dispositivos móviles registrados (MQTT/IoT Core) | \~270 (hasta \~300+ en peak) | EC55 + TC58e + terminales de cámara |

#### TPS estimados (peor ventana)

Los TPS estimados en la peor ventana se derivan en la Tabla 76:

**Tabla 76** — TPS estimados (peor ventana)

| Flujo | Cálculo | TPS |
|---|---|---|
| Confirmaciones de picking | 120 terminales × 1 confirmación / 6 s | \~20 TPS |
| Pedidos de preventa (09:00–13:00) | 62 preventistas × 1 línea / 8 s | \~8 TPS |
| Movimientos de inventario + sincronización | Suma de flujos (broker, WMS, IoT) | \~35 TPS |
| TPS de diseño (burst ×3) | 35 × 3 en peak de septiembre | \~105 TPS |

El burst ×3 absorbe el peak de septiembre y las ráfagas de la ventana de sincronización 17:00–20:00. Los ≈ 105 TPS son el valor único de diseño de esta parte, citado por ADR-01 y ADR-12, y sustenta el dimensionamiento de IOPS de VM-02 (subsección de almacenamiento) y del escalado ECS (ADR-12).

### Dimensionamiento on-premise (ADR-10)

#### Cómputo — CD Talca (clúster N+1, 3 nodos Proxmox/Ceph)

El cómputo del clúster y su utilización N+1 se resumen en la Tabla 77:

**Tabla 77** — Cómputo — CD Talca (clúster N+1, 3 nodos Proxmox/Ceph)

| Recurso | Asignado | Físico (clúster) | Utilización N+1 |
|---|---|---|---|
| vCPU | 30 | 96 threads (3 nodos × 32) | 30 / 64 = 47 % (2 supervivientes) |
| RAM | 68 GB | 384 GB (3 × 128) | 68 / 256 = 27 % |
| Almacenamiento (pool Ceph, réplica 2) | 1.890 GB | 5,76 TB útiles (12 OSDs, RAID 10 NVMe) | 32 % |

Las VMs del clúster Talca (familias declaradas en la subsección de dimensionamiento on-premise de esta sección) se especifican en la Tabla 78:

**Tabla 78** — VMs del clúster CD Talca (N+1, 3 nodos Proxmox/Ceph)

| VM | Rol | vCPU | RAM | Disco datos |
|---|---|---|---|---|
| VM-01 | WMS Core (picking FEFO, misiones RF, despacho, SSCC GS1) | 8 | 16 GB | 100 GB |
| VM-02 | PostgreSQL — BD transaccional del maestro de bodega | 8 (→12) | 32 GB (→64) | 1.500 GB |
| VM-03 | RabbitMQ — broker de colas offline (buffer 24 h) | 4 | 8 GB | 200 GB |
| VM-04 | ACL ERP — frontera única de integración | 4 | 4 GB | 20 GB |
| VM-05 | Keycloak Local Auth Cache / Offline Proxy (A-05, Modelo B) | 4 | 4 GB | 20 GB |
| VM-06 | OpenTelemetry Collector + SSM Agent (buffer 24 h) | 2 | 4 GB | 50 GB |

#### Cómputo — Concepción (edge) y cross-docking

- **CD Concepción (C3):** 12 vCPU / 24 GB / RAID 10 (4×NVMe 960 GB + hot-spare). Rol: WMS con 24 h de autonomía sin enlace (RNF-13.01).
- **Plataformas de cross-docking (E-01):** Mini-PC industrial (Advantech ARK-2250 / NUC Pro 12). Rol: WMS del cross-dock (E-01) + router Starlink (enlace principal) + LTE de respaldo.


#### Almacenamiento

El esquema de almacenamiento y su capacidad útil se detallan en la Tabla 80:

**Tabla 80** — Almacenamiento

| Capa | Esquema | Capacidad útil |
|---|---|---|
| BD transaccional + pool de datos | Ceph réplica 2 sobre RAID 10 NVMe (≈ 4× factor de compra) | 5,76 TB pool (margen 68 % a 5 años) |
| Crecimiento 5 años | 1.890 GB × 3 | ≈ 5,7 TB < 5,76 TB, cumple |
| Respaldo de recuperación rápida (D-05) | NAS 2U, RAID 6 (4 × 4 TB) + WORM local | 8 TB |
| IOPS VM-02 | 105 TPS × 8 E/S = 840 IOPS requeridas | NVMe RAID 10 > 100.000 IOPS, cumple |

#### Ancho de banda WAN por sitio

El ancho de banda por sitio se declara en la Tabla 81:

**Tabla 81** — Ancho de banda WAN por sitio

| Sitio | Régimen normal | Peak septiembre | Respaldo (autoconmutación < 30 s) |
|---|---|---|---|
| CD Talca (D-03/D-04) | 20 Mbps fibra | 50 Mbps | LTE 5→10 Mbps |
| CD Concepción | 10 Mbps fibra | 20 Mbps | LTE 3→5 Mbps |
| Cross-docking (×3) | Starlink 500 GB principal | Ídem | LTE 2→5 Mbps |

Cohesión con la vista de despliegue: estos valores son los mismos que declara la sección de arquitectura de despliegue (red privada virtual IPsec doble por centro de distribución).

Justificación: el régimen lo manda la sincronización de flota dentro de la ventana de retorno (≈ 2 GB/día; ≈ 4–5 Mbps a la carga 3× de RT-09.03) más la evidencia de entrega, los DTE y la telemetría (≈ 1–2 Mbps; peak sept. ≈ 312 MB/h ≈ 0,7 Mbps), con margen de diseño. El peak de 50 Mbps en Talca cubre el respaldo completo semanal a la nube (≈ 40 → 120 GB en ventana nocturna, ≈ 40 Mbps) simultáneo a la ráfaga de septiembre. Los valores están escalados al crecimiento 3× sin rediseño, no a la demanda promedio.

### Dimensionamiento nube (ADR-12)

El dimensionamiento en nube por componente se resume en la Tabla 82:

**Tabla 82** — Dimensionamiento nube (ADR-12)

| Componente | Base (normal) | Peak septiembre | Criterio de escalado |
|---|---|---|---|
| ECS Fargate Django (tareas 2 vCPU / 4 GB) | 2 | 6 (3×) | Target Tracking CPU > 70 % |
| ECS Fargate Celery workers (2 vCPU / 4 GB) | 2 | 4 (2×) | Cola (queue depth) / CPU |
| AWS Lambda (fn-iot-validator, fn-document-signer) | 100 concurrencias | 500 (reserva) | Eventos IoT Core / S3 |
| Aurora PostgreSQL (writer / reader) | db.r6g.large × 2 AZ | db.r6g.xlarge + 2 readers | CPU > 60 % / Conexiones > 80 % |
| ElastiCache Redis | cache.r6g.large | cache.r6g.xlarge | Memoria > 75 % (stock/crédito < 2 s) |
| DynamoDB (telemetría IoT cruda) | On-demand | On-demand | Sin gestión de capacidad |
| AWS IoT Core (MQTT) | \~270 dispositivos | \~300+ | Concurrencia de terreno |
| Keycloak IdP maestro (Fargate) | 1 tarea 1 vCPU / 2 GB | 2 tareas (Multi-AZ) | CPU > 60 % |

Escalado automático (RT-09.04):

- **Predictivo + reactivo (ADR-12).** pre-warm en agosto de las tareas ECS, concurrencia reservada Lambda; reactivo con Target Tracking en < 2 min · aprovisionamiento en < 3 min · cooldown 60 s.
- **Serverless-first.** DynamoDB On-Demand y Lambda escalan sin configuración adicional; la capacidad se paga por uso (sin capacidad ociosa, RT-15.01 — FinOps Cloud del Subdocumento 4.1).


### Plan de capacidad y crecimiento 3× sin rediseño

El crecimiento se absorbe con el mismo diseño (sin cambio de topología, VLAN, réplica ni nube), como se detalla en la Tabla 83:

**Tabla 83** — Plan de capacidad y crecimiento 3× sin rediseño

| Recurso | Diseño (3.900 entregas/día) | 3× (7.800 entregas/día) | Acción declarada |
|---|---|---|---|
| vCPU clúster Talca | 30 / 64 = 47 % (N+1) | \~90 asignadas | Ampliación RT-08.05; al acercarse al margen, inserción del 4.º servidor idéntico (rack R04 de crecimiento de la sala técnica principal) → 96 threads + N+1 real |
| RAM | 68 / 256 = 27 % | \~205 GB | Dentro de los 384 GB físicos, cumple |
| Pool Ceph | 32 % de 5,76 TB | ≤ 96 % | Ampliación por adición de OSD/NVMe, sin rediseño |
| Enlace Talca / Concepción | 20→50 / 10→20 Mbps | 50 / 100 Mbps | Contrato escalonado de enlaces |
| TPS VM-02 | \~105 | \~315 | Escala vertical 8→12 vCPU (32→64 GB) + particionado mensual |

En nube, el 3× se absorbe por auto-scaling (Fargate 2→6, Celery 2→4, Lambda hasta 500, Aurora xlarge + readers), sin rediseño arquitectónico — misma decisión ADR-12 que fija el límite de elasticidad del peak.

### Umbrales de desempeño (percentil p95)

Los umbrales de desempeño por operación se fijan en la Tabla 84:

**Tabla 84** — Umbrales de desempeño (percentil p95)

| Operación | Umbral (p95) |
|---|---|
| Confirmación de una línea de preparación de pedidos (picking) | ≤ 1 s |
| Registro de una entrega en el local del cliente | ≤ 2 s |
| Registro de una línea en toma de pedido de preventa | ≤ 1,5 s |
| Consulta de stock y crédito en preventa | ≤ 2 s |
| Transacción operacional crítica de terreno (e2e) | ≤ 3 s |
| Navegación entre vistas ya cargadas | ≤ 1 s |
| Búsqueda con criterios compuestos | ≤ 3 s |

Los umbrales se verifican con monitoreo CloudWatch y se prueban en Preproducción (subsección de pruebas de carga y estrés).

### Primer cuello de botella

VM-02 (PostgreSQL — escritura transaccional del maestro de bodega) se satura primero a medida que crece la carga: todo el picking (22:00–06:00) y el despacho masivo (05:30–07:00) pasan por el único punto de escritura.

**Detección:** p95 de escritura > 800 ms; commit ×3 sobre la base; IO wait > 15 %; cola Backend > 5–10. **Mitigación:** 1) escala vertical 8→12 vCPU / 32→64 GB (margen N+1); 2) particionado mensual + PgBouncer (pooler de conexiones); 3) réplica de solo lectura; 4) 4.º nodo / sharding al agotar margen.

En nube el equivalente es Aurora (writer + readers); SQS FIFO absorbe el pico de sincronización 17:00–20:00 (ADR-05).

### Degradación controlada

Enlace WAN: QoS prioriza broker/WAL; colas diferidas fuera de la ventana; conmutación automática < 30 s entre los dos caminos del sitio.

Offline: buffers RabbitMQ de 24 h y buffers OTel de 24 h; reconciliación cronológica e idempotente al reconectar.

Nube: throttling en API Gateway, timeouts y reintentos con backoff en Celery, DLQ para tareas fallidas.

### Pruebas de carga y estrés

Las pruebas de carga y estrés se definen en la Tabla 86:

**Tabla 86** — Pruebas de carga y estrés

| Prueba | Carga | Escenario |
|---|---|---|
| Carga (RNF-19.04) | 1,5 × la carga de diseño = 5.850 entregas/día ≈ 160 TPS sostenidos (carga de diseño = peak 2.600 × 1,5 = 3.900; la prueba la vuelve a multiplicar por 1,5) | Preproducción, perfiles horarios reales (pick nocturno, despacho, preventa) |
| Estrés | Incremento hasta el punto de quiebre ≥ 3× | Curva de tiempo de respuesta vs carga |
| Informe de carga (RT-09.07) | Curvas, saturación, recursos (CPU/RAM/IOPS/enlace/colas) | Insumo al hito de producción (mes 16) y a la actualización de capacidad (RT-09.09, subsección de actualización del plan de capacidad) |

Herramientas: k6/Gatling + drivers a medida contra las APIs (svc-erp-integration, svc-broker). Cortes: Etapa 1 (mes 13), Etapa 2 (mes 19), re-ejecución trimestral. Calendario e hitos formales en el Formulario T-13.

### Actualización del plan de capacidad

Gestión de capacidad durante la Operación con proyección trimestral de crecimiento: consumo real vs. proyectado (vCPU/RAM/almacenamiento/enlace/colas/TPS), con alertas anticipadas de agotamiento al 70 % / 2 semanas y propuesta de ajuste de dimensionamiento y de costo.

Ventana de ampliación: adición de vCPU/OSD dentro del físico, contrato escalonado de enlaces, 4.º nodo al acercarse al margen. La revisión se apoya en el informe de carga como insumo del hito de producción (mes 16).

Nube: revisión de costos de nube — evaluar umbrales Target Tracking y concurrencia reservada con al menos 30 días antes del peak de septiembre.

## Registro de decisiones de arquitectura

Registro consolidado de las quince decisiones de arquitectura que condicionan esta propuesta. Es entregable contractual conforme a RT-02.04 y se mantiene actualizado durante toda la ejecución. Para cada decisión se indica la alternativa escogida, las alternativas descartadas con el motivo de rechazo, y el criterio de selección. Todas las decisiones fueron aprobadas entre el 05 y el 06 de septiembre de 2026.

### ADR-01 · Estilo arquitectónico

**Decisión adoptada.** Monolito modular Django 5.x LTS / Python 3.12, desplegado en ECS Fargate con apps por dominio y límites de contexto DDD. Módulos críticos (WMS offline, shipper, workers, portal) en procesos separados.

**Alternativas descartadas.** *Microservicios EKS*: volumen (\~105 TPS) dos órdenes bajo el umbral que los justifica; 4 personas no operan 9–13 componentes de plano de control; TCO estimado en +USD 40–70 K / 56 m (estimación interna basada en la operación de EKS con el equipo del CLIENTE). *Monolito clásico WMS 2013*: sin fronteras de módulo, proveedor desaparecido; viola RT-02.02.

**Criterio de selección.** Pertinencia al volumen real (BTT §2.3); operabilidad por 4 personas; TCO 56 meses; despliegue independiente sin particionar el dominio. Normativa: RT-02.01/02.02/02.03, RT-09.05, BA Art. 16, RNF-19.01–04. Relacionada: D5, D8, D14 (Arq. Lógica).

### ADR-02 · Conectividad WAN

**Decisión adoptada.** Doble camino por sitio: fibra + LTE en los centros de distribución, Starlink + LTE en los cross-docking. Conmutación automática < 30 s.

**Alternativas descartadas.** *Fibra en cross-docks*: naves industriales sin cobertura de fibra; costo de obra desproporcionado. *VSAT GEO*: latencia 500–700 ms RTT; penaliza RNF-05.01 y costo superior. *Tri-camino (fibra + Starlink + LTE)*: tercer camino no aporta disponibilidad significativa dado que cada sitio opera autónomamente ante pérdida total de enlace (24 h CD, 14 h terreno).

**Criterio de selección.** Dos caminos de física distinta satisfacen RT-03.17 sin punto único de fallo; la autonomía local cubre la pérdida total de enlace, por lo que un tercer camino es innecesario; cero mantención de radio para el equipo de 4 personas del CLIENTE. Normativa: RT-03.10/03.17, RT-10.05, RNF-13.01/13.07/13.08. Relacionada: Decisión 16.1 N° 26.

### ADR-03 · Modelo de despliegue híbrido

**Decisión adoptada.** Borde operacional on-premise (WMS maestro Talca, edge Concepción, WMS en cross-docks) + carga principal en AWS. 11 componentes on-prem, 12 híbridos, 13 nube pura.

**Alternativas descartadas.** *Solo nube*: inadmisible (Art. 16); sin enlace la bodega muere en minutos; picking en cámara −22 °C inviable con RTT 40–80 ms. *Solo on-premise*: inadmisible (Art. 16).

**Criterio de selección.** Único modelo que satisface Art. 16 en sus 4 numerales; latencia ≤ 1 s en cámara resuelta localmente; autonomía 24 h CD / 14 h terreno; TCO contenido con servicios administrados AWS. Normativa: BA Art. 16.1–16.4, RT-03.01/03.02/03.10/03.19, RNF-02.01/05.01/05.02. Relacionada: D7, Decisión 16.1 N° 17.

### ADR-04 · Persistencia políglota

**Decisión adoptada.** PostgreSQL+PostGIS (transaccional WMS, CP), Aurora (OLTP cloud + DRP), DynamoDB (IoT raw, AP, TTL 30 d), S3+Redshift Serverless (OLAP + series de temperatura), S3 Object Lock/Glacier (retención legal 5 años).

**Alternativas descartadas.** *Motor único relacional*: no escala ingesta IoT sin degradar picking (RNF-11.02). *InfluxDB*: segundo motor exótico a operar; serie de tiempo cabe en capa OLAP. *DynamoDB para todo*: no ofrece ACID cross-tabla para reconciliación determinista.

**Criterio de selección.** Posición CAP declarada por dominio (RT-05.02); 3 motores administrados operables por el equipo de TI del CLIENTE; retención sanitaria D.S. 977/96 con inmutabilidad; RPO ≤ 15 min por réplica Aurora. Normativa: RT-05.01/05.02/05.11–15, RNF-09.01/09.02/11.02. Relacionada: D2, D4, Decisión 16.1 N° 18.

### ADR-05 · Mensajería asíncrona

**Decisión adoptada.** RabbitMQ local por sitio (buffer 24 h) + shipper idempotente → SQS FIFO (VPC Endpoint outbound) + Celery workers (tareas derivadas de eventos) + IoT Core MQTT (ingesta edge).

**Alternativas descartadas.** *REST síncrono*: no sobrevive corte a mitad de ventana; rompe reconciliación. *Kafka/MSK*: operar clústeres en 5 sitios es desproporcionado para el equipo disponible y 105 TPS.

**Criterio de selección.** Resiliencia offline (buffer local + reproducción idempotente); reconciliación determinista RT-03.12; Zero Trust (todo outbound); TCO proporcional al volumen. Normativa: RT-02.06/02.07, RT-03.10/03.12, RNF-07.01/13.01, BA Art. 21. Relacionada: D4.

### ADR-06 · Identidad híbrida (Modelo B)

**Decisión adoptada.** Keycloak IdP maestro en AWS (ECS Fargate, 2 tareas Multi-AZ, backend Aurora) + caché local solo lectura (TTL 8 h) en Talca y Concepción. Tokens offline por perfil (8 h bodega, 14 h reparto). OTP para conductores externos.

**Alternativas descartadas.** *IdP solo nube*: paraliza bodega ante corte. *AD maestro local*: duplica administración, crea maestro a promover en DR. *Keycloak maestro local*: nube no puede autenticar si el enlace cae.

**Criterio de selección.** Autonomía offline sin maestro local a promover; autoridad única en nube; OTP sin correo para externos (RT-12.12); MFA Art. 22; operado por el equipo reducido del CLIENTE sin directorio propietario. Normativa: RT-12.10/12.11/12.12, RT-03.10, RNF-13.01, BA Art. 22, RF-15.01–05, RF-06.08. Relacionada: D6, Decisión 16.1 N° 34.

### ADR-07 · Movilidad de terreno

**Decisión adoptada.** App nativa Android Kotlin para preventa, reparto y picking. SQLite/Room, SDK Zebra DataWedge (GS1 + QR), impresión BT (ZQ620), POS PAX. Dispositivos Rugged: EC55, TC58e, MC9400 Cold Storage.

**Alternativas descartadas.** *PWA*: no controla SDK Zebra de forma fiable ni persiste turno completo sin capa nativa. *Híbrida Flutter*: runtime intermedio degrada interacción con periféricos industriales.

**Criterio de selección.** Control nativo de periféricos (DataWedge intents); offline total 14 h con sincro < 10 min; UI para guantes −22 °C, una mano, lluvia; curva de aprendizaje ≤ 2 h; un artefacto para 3 perfiles. Normativa: RT-13.08, RT-12.11, RT-03.19, RNF-05.02/05.03/06.01, RF-06.11–13. Relacionada: Decisión de proyecto N° 19.

### ADR-08 · Destino del WMS legado 2013

**Decisión adoptada.** Reemplazo total en Etapa 1 por módulo WMS del monolito (ADR-01): Talca maestro, Concepción edge, cross-docks sobre E-01. Migración por dominio, oleadas por sitio, reversión azul-verde.

**Alternativas descartadas.** *Mantener e integrar*: proveedor desaparecido, sin soporte; no soporta multi-sitio, picking FEFO (primero en expirar, primero en salir), SSCC GS1 ni conteo cíclico ciego. *Extender a otros sitios*: arrastra riesgo de soporte inexistente en ventana crítica.

**Criterio de selección.** Requisitos RF-02.x que el WMS 2013 no contempla; riesgo operacional inaceptable; TCO amortizado con reducción conteo 2,3 %→\~0,3 % y merma 1,7 %→<1 %; reversión azul-verde garantizada. Normativa: RT-05.11–15, RT-03.10, RNF-02.01/05.01, Caso 16.1 N° 14. Relacionada: Decisión 16.1 N° 14 (delegada por el CLIENTE).

### ADR-09 · Estrategia DR

**Decisión adoptada.** Activo-pasivo warm standby multi-región: DMS CDC + Aurora WAL hacia us-east-1; DRP local Talca→Concepción (RTO +1–2 h); pruebas 2×/año; respaldo 3-2-1-1-0 con S3 Object Lock.

**Alternativas descartadas.** *Activo-activo*: duplica infraestructura y exige reconciliación de doble escritura sin beneficio medible. *Backup + restore frío*: RTO 24–72 h, incumple RNF-20.06. *Solo intrarregional*: postura mínima si CLIENTE no aprueba Art. 23; aceptando RTO 24–72 h ante caída de región.

**Criterio de selección.** RTO ≤ 4 h / RPO ≤ 15 min; proporcionalidad al volumen; DR de identidad resuelto en nube (ADR-06); pruebas semestrales reales. Normativa: RT-07.01/07.07, RNF-20.06/20.07, BA Art. 20. Relacionada: Decisión 16.1 N° 27.

### ADR-10 · Almacenamiento on-premise y RAID

**Decisión adoptada.** RAID 10 NVMe para BD transaccional del WMS (VM-02); RAID 6 con hot-spare para evidencia POD, logs y rollups; hipervisor Ceph N+1.

**Alternativas descartadas.** *RAID 5*: probabilidad de URE durante rebuild en discos 8–16 TB; solo tolera 1 fallo. *RAID 1 puro para todo*: sobre-costo 50 % aplicado a datos no críticos sin beneficio proporcional.

**Criterio de selección.** IOPS deterministas en ventana de despacho (>100 K vs. \~840 necesarios); tolerancia a fallo de disco (RNF-13.04) con justificación (RNF-13.05); TCO contenido con RAID 10 solo en lo transaccional. Normativa: RT-03.14, RNF-13.03/13.04/13.05. Relacionada: Decisión 16.1 N° 28.

### ADR-11 · Integración B2B/EDI canal moderno

**Decisión adoptada.** Hub EDI centralizado GS1 (EANCOM/GS1 XML + EPCIS) en nube, con conector configurable por cadena, equivalencias GTIN (RF-12.03), bandeja de excepciones (RF-12.06) y ACL hacia ERP/GDE. Canal moderno operativo ≤ enero 2029.

**Alternativas descartadas.** *Punto-a-punto por cadena*: multiplica adaptadores; mantenimiento desproporcionado ante cambios de cadena. *EDI delegado al ERP*: expone frontera frágil; viola Zero Trust (escritura directa desde cadena).

**Criterio de selección.** Estandarización GS1 (Cap. 16.2); esfuerzo marginal por cadena nueva; aislamiento ERP por ACL (Zero Trust); plazo enero 2029. Normativa: RT-05.23, RT-16.16/16.17, RNF-12.01, RF-12.03/12.06. Relacionada: RF-12, RF-01.10.

### ADR-12 · Absorción del peak de septiembre

**Decisión adoptada.** Cómputo elástico: Fargate 2→6, Celery 2→4, Lambda 100→500, Aurora large→xlarge +2 readers, DynamoDB on-demand. Escala predictiva + reactiva. Base con Savings Plan, peak con cómputo efímero.

**Alternativas descartadas.** *Capacidad fija al peak*: paga 12 meses la capacidad de 3 semanas. *Solo escala reactiva*: burst predecible de septiembre; la reactiva sola introduce lag en ventana crítica.

**Criterio de selección.** Perfil no plano al peak ×1,5 (RNF-19.04); cuello de botella identificado (RT-09.05); FinOps (RT-03.06): base reservada + peak efímero; congelamiento 1–25 sept y diciembre (RT-10.05). Normativa: RT-09.05, RT-03.06/03.08/03.09, RNF-19.01–04, RT-10.05. Relacionada: Decisión 16.1 N° 30.

### ADR-13 · Puerta de enlace de servicios

**Decisión adoptada.** Amazon API Gateway como Capa 3 única: autorizador OIDC (Keycloak), validación de esquema OpenAPI, cuotas y límites de tasa por actor/ruta, versionado /v{major}, propagación de transaction_id a Capa 8.

**Alternativas descartadas.** *Kong autoadministrado*: agrega componente crítico a parchar en ruta de la venta; riesgo en ventana 05:30–07:00 con el equipo disponible. *Desarrollo propio (middleware Django)*: sin cuotas/rate-limit nativos; viola Art. 21.2.

**Criterio de selección.** Cumplimiento literal Art. 21.2 sin desarrollo propio; servicio administrado para 4 personas; coherencia entre vistas (Art. 16.4); reversibilidad por contratos OpenAPI/AsyncAPI estándar. Normativa: BA Art. 21.2, RT-02.01/02.02, RT-11.11, RT-05.16/05.18, Art. 16.3. Relacionada: D8.

### ADR-14 · Plataforma de observabilidad

**Decisión adoptada.** Plataforma única en nube: instrumentación OTel, colectores ADOT on-premise con buffer 24 h, logs en CloudWatch Logs (12+24 m), métricas en CloudWatch Metrics (13 meses) y trazas en CloudWatch con retención declarada. Tableros nativos de CloudWatch para operación.

**Alternativas descartadas.** *Prometheus+Grafana+Loki local + cloud*: dos plataformas (viola Art. 16.4 y RT-03.16); VM-06 sin capacidad. *AMP + X-Ray + Grafana*: cuatro servicios de observabilidad para un equipo de 4 personas; complejidad operativa desproporcionada sin ganancia funcional sobre CloudWatch nativo.

**Criterio de selección.** Art. 16.4 y RT-03.16 piden una plataforma; buffer ADOT resuelve «sin puntos ciegos» durante corte; ninguna decisión 05:30–07:00 depende de tablero; CloudWatch es nativo de AWS y no requiere infraestructura adicional; el equipo del CLIENTE no opera servidores de observabilidad. Normativa: BA Art. 16.4, RT-03.16, RT-14.01–09, RT-09.01. Relacionada: D14.

### ADR-15 · Gestión de secretos

**Decisión adoptada.** AWS Secrets Manager (secretos con rotación: ERP, SII, Transbank, certificados AS2/EDI) + SSM Parameter Store (config no sensible). Consumo outbound por VPC Endpoint. Cifrado CMK KMS, separación de funciones. Cuenta de emergencia en sobre sellado offline.

**Alternativas descartadas.** *HashiCorp Vault autoadministrado*: modo sellado tras reinicio exige intervención humana de madrugada; agrega infraestructura. *Sin gestor centralizado*: prohibido por Art. 21.4.

**Criterio de selección.** Servicio administrado sin desellado manual; Zero Trust (consumo outbound); separación de funciones Art. 21.2 vía IAM/CloudTrail; contingencia offline independiente de la nube. Normativa: BA Art. 21.4/21.2, Art. 16.2/16.3, RT-04.09, RT-11.09. Relacionada: D13, SEC-01.
