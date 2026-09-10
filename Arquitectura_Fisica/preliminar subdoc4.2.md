# **Capítulo 4 · Arquitectura de la Solución — Subdocumento 4.2 (Unificado)**

> **Documento único del Subdocumento 4.2 (Formulario T-22).** Integra, como apartados de este mismo subdocumento: la **arquitectura física** (apartados (a)–(e), niveles de servicio y operación desconectada), la **arquitectura de integración** (apartado 3), la **arquitectura de seguridad** (apartado 4), la **arquitectura de despliegue** (apartado 5), el **dimensionamiento y plan de capacidad** con el módulo de **BI/analítica** (apartado 6) y las **decisiones de arquitectura** (ADR-01…ADR-15, apartado 7). Es un documento **autocontenido**: se sustenta en los documentos rectores (Bases y Caso 02) y en los catálogos de requerimientos funcionales y no funcionales (RF/RNF) del proyecto, sin citar archivos de trabajo internos. Documento unificado el **2026-09-06**.

## **4.1  Visión General de la Arquitectura Física**

La arquitectura física materializa el despliegue **híbrido obligatorio** del Artículo 16° de las Bases Administrativas: la **carga principal corre en nube pública AWS**, con la región primaria en `sa-east-1` (São Paulo, Brasil) y la recuperación ante desastres en `us-east-1` (Norte de Virginia, EE. UU.); los componentes *on-premise* garantizan la continuidad de la operación de bodega, plataformas y terreno durante cortes del enlace.

La lectura única de la red de instalaciones es la del Artículo 16, la Tabla 14.1 y RT-21.16: **seis instalaciones en cuatro regiones**, de las cuales **cinco alojan cómputo** —el CD Talca (Sala Técnica Secundaria), el CD Concepción (gabinete de borde) y las tres plataformas de cross-docking de Curicó, Chillán y Los Ángeles— y la **sexta es la casa matriz y oficinas centrales de Talca**, contigua al CD principal, que **no procesa operación logística** y consume la nube a través del portal, el BI y el *back office* (RT-03.22). El §8 del caso menciona «cinco instalaciones»; prevalecen la Tabla 14.1 y RT-21.16, y la divergencia se eleva como consulta al mandante (Art. 43.3) sin alterar el dimensionamiento. La proyección del caso a tres años incorpora una **séptima instalación** (RT-02.12), absorbida por parametrización y por el gabinete de crecimiento de la sala (R04) sin obras adicionales.

Los principios que gobiernan el diseño son los siguientes:

1. **Carga principal en nube (Art. 16.1):** el núcleo transaccional de preventa, reparto y canal moderno, la analítica, la integración y el almacenamiento consolidado se ejecutan en AWS `sa-east-1`, con escalado elástico para el *peak* de septiembre.  
2. **Autonomía *on-premise* de primera clase:** cada CD opera su WMS, su base PostgreSQL local y su broker de colas por 24 horas sin enlace (RT-03.10); el terreno de preventa y reparto opera la jornada completa (14 horas) sin señal, con la sesión de usuario sostenida por la caché local de identidad (RT-03.10, RNF-13.01).  
3. **Cero indisponibilidad en la ventana crítica de despacho (05:30–07:00):** todas las decisiones de esa ventana son locales, sin dependencia de la observabilidad centralizada ni del enlace WAN.  
4. **Autoridad única de identidad (Modelo B, D6):** Keycloak IdP maestro en ECS/Fargate (nube) y cachés locales de solo lectura con TTL de 8 horas en VM-05 (Talca) y VM-C03 (Concepción); no existe maestro *on-premise* ni promoción local a escritura.  
5. **Zero Trust end-to-end (NIST SP 800-207):** sin conexiones entrantes a la red *on-premise* salvo dos excepciones controladas por la VPN (DMS→PostgreSQL y `celery-erp-sync`→ACL, D-AL-05); todo lo demás es tráfico iniciado desde adentro.  
6. **Caminos WAN redundantes en 3 tecnologías:** fibra (D-03) + satelital Starlink (D-06) + LTE (D-04) por centro, con proveedores y medios distintos (RT-03.17/RT-03.21) y conmutación automática en menos de 30 segundos.  
7. **Respaldo único 3-2-1-1-0:** datos activos + copia local de recuperación rápida (NAS D-05) + pierna inmutable en la nube (S3 Object Lock / Backup Vault Lock) + réplica en región secundaria + cero errores de restauración (pruebas semestrales, Art. 20 / RT-07.07).

La arquitectura se describe según el marco TOGAF declarado y la descripción conforme a ISO/IEC/IEEE 42010, coherente con la arquitectura lógica v6.2 (Subdoc. 4.1) y con la Tabla de Emplazamiento componente por componente (Art. 16.2). El detalle de cumplimiento por requerimiento se responde en el Formulario T-12 y el dimensionamiento explícito de la volumetría (numeral 14.2) en el Subdocumento 5.

## **(a) Modelo de Emplazamiento Híbrido**

| Componente | Emplazamiento | Justificación |
|---|---|---|
| **A1 — Topología híbrida** | Nube AWS `sa-east-1` (carga principal) + CD Talca (Sala Técnica Secundaria) | Art. 16 y RT-03.01 exigen despliegue híbrido: la nube concentra la carga principal y el centro *on-premise* sostiene la bodega, operando 24 h sin enlace y el terreno hasta 14 h (RT-03.10), con cero indisponibilidad en la ventana crítica de despacho (05:30–07:00). |
| **A2 — Clúster WMS *on-premise*** | CD Talca, Sala Técnica Secundaria (sala blanca de 32 m²) — 3 nodos | Clúster HA N+1 de 3 nodos Proxmox VE/KVM + Ceph (12 OSD, réplica 2, 3 monitores): la caída o el mantenimiento de un nodo no detiene las cargas de trabajo (RT-08.03), se elimina el riesgo de *split-brain* de un par y se toleran fallas de disco (RT-03.14). |
| **A3 — Servidor de borde (CD Concepción)** | CD Concepción (gabinete de borde) — 1 | Ejecuta el WMS en modo reducido (copia local) con caché de identidad de 8 h; Concepción opera autónoma 24 h si se pierde el enlace con Talca, sin crear autoridades de identidad dispersas en terreno (autoridad única en nube). |
| **A4 — Nodo de cómputo de *cross-docking*** | Curicó, Chillán y Los Ángeles — 3 | Mini-PC industrial con mini-WMS local: sin fibra disponible (Cap. 6 del caso), el nodo procesa recepción, desconsolidación y re-despacho en forma local con enlace principal satelital Starlink y respaldo automático por red móvil dual LTE de dos proveedores (RT-03.17), con conmutación en menos de 30 s y ventana de operación de 3 h 100 % local (RT-03.10/RT-03.11); elimina el SPOF de red móvil de Los Ángeles entre 03:00–05:00. |
| **A5 — Conectividad WAN** | CD Talca y CD Concepción — 2 | VPN IPsec IKEv2 AWS Site-to-Site + SD-WAN multi-WAN: 3 caminos por centro (fibra, satelital Starlink, LTE) con proveedores y medios distintos (RT-03.21 y RT-03.17) y conmutación automática en menos de 30 s. Con Direct Connect disponible como complemento dedicado activable por el CLIENTE. |
| **A6 — Autonomía de terreno** | 14.200 puntos de entrega y rutas rurales — 200+ terminales | Terminales móviles con operación sin señal (buffer local) y sesión de usuario válida de 8 h (bodega) o 14 h (reparto/preventa): ningún pedido ni entrega se pierde por falta de cobertura (RT-03.10 y RT-03.11), y la sincronización al reconectar es deduplicada e idempotente en menos de 10 minutos (RT-03.12, RNF-07.01). |

La justificación componente por componente conforme a los criterios del Art. 16.2 (latencia, criticidad operacional, volumen de datos, restricciones regulatorias, disponibilidad de conectividad y costo total de propiedad) se desarrolla en la Tabla de Emplazamiento v06 (§1.0): 36 componentes, 11 *on-premise* puros, 12 híbridos con pieza en ambos dominios y 13 servicios administrados de nube pura (serie N-01…N-13).

### Instalaciones de la red on-premise

La red *on-premise* se compone de **seis instalaciones** (Tabla 14.1 y RT-21.16):

- **CD Talca** (Sala Técnica Secundaria, sala blanca de 32 m²): clúster WMS de 3 nodos, base transaccional *on-premise* (PostgreSQL 16, VM-02), broker local RabbitMQ (VM-03), capa anticorrupción del ERP (VM-04), caché de identidad (VM-05), telemetría (VM-06), respaldo NAS (D-05) y componentes de sala (UPS N+1, generador 12 kVA con estanque 24 h, clima N+1, seguridad física).  
- **CD Concepción** (9.000 m², gabinete de borde): servidor de borde con el WMS en modo reducido (VM-C01), base local (VM-C02), caché de identidad (VM-C03), broker + telemetría (VM-C04) y Gateway IoT Greengrass (B-02); opera 24 h de forma autónoma e independiente de Talca.  
- **Cross-docking de Curicó, Chillán y Los Ángeles**: nodo de cómputo industrial (E-01) con mini-WMS y broker local, enlace principal Starlink (D-06) y respaldo LTE dual (2 proveedores).  
- **Casa matriz y oficinas centrales (Talca)**: sin nodo de cómputo propio; acceso a la nube para administración, planificación y portal de clientes (RT-03.22).

La proyección a 3 años (RT-02.12) incorpora una séptima instalación; el gabinete de crecimiento de la sala (R04) absorbe esa expansión sin obras adicionales en el sitio principal.

## **(b) Tecnologías de Software a Utilizar**

Las tecnologías se eligen bajo los criterios de neutralidad tecnológica, soporte vigente por los 56 meses contractuales (RT-03.05) y preferencia por servicios administrados y componentes de código abierto con estándares abiertos (RT-03.07), de modo que el CLIENTE conserve la reversibilidad de la solución:

| Componente | Tecnología ofertada |
|---|---|
| **B1 — Aplicación** | **Django monolito modular (Python) + Celery** sobre AWS ECS Fargate (2–6 tareas con escala automática). La misma imagen se reutiliza en modo `wms_only` dentro del ambiente *on-premise* (RT-02.02). |
| **B2 — BD transaccional nube (maestro)** | **Amazon Aurora PostgreSQL** en `sa-east-1` (Multi-AZ), con réplica pasiva promueble en `us-east-1` para recuperación ante desastres (RT-07.02, RTO ≤ 4 h / RPO ≤ 15 min). |
| **B3 — BD transaccional *on-premise*** | PostgreSQL 16 (VM-02 Talca / VM-C02 Concepción): sistema de verdad de la bodega durante cortes de enlace, con flujo continuo hacia la réplica en nube por AWS DMS CDC sobre el WAL lógico (RPO ≤ 15 min, RT-07.03 y RT-07.04). |
| **B4 — Broker de mensajería** | RabbitMQ local (colas *offline* por sitio) + SQS FIFO en nube (reconciliación) + EventBridge (eventos): cada sitio absorbe hasta 24 h de operación sin enlace (RT-02.07) con vuelco en orden estricto e idempotencia (D-AL-03). |
| **B5 — Identidad (IdP maestro)** | **Keycloak** en ECS/Fargate (OIDC/OAuth 2.1, MFA, SSO), autoridad única de identidad en `sa-east-1` (RT-12.01); las cachés locales *on-premise* (A-05, VM-05/VM-C03) son de solo lectura con TTL de 8 h, sin autoridades de identidad dispersas (Modelo B, D6). |
| **B6 — Telemetría IoT** | AWS IoT Core + Greengrass v2 + sensores Ebyte ME31 (B-01/B-02): registro continuo de cadena de frío (RT-03.18 y RT-03.19) con decisión de bloqueo por excursión térmica 100 % en el borde. |
| **B7 — Observabilidad** | Plataforma única (Art. 16.4 / RT-03.16): instrumentación OpenTelemetry con colectores ADOT *on-premise* (VM-06, VM-C04, cross-dock; buffer en disco 24 h) que emiten a AMP (Prometheus), CloudWatch Logs, X-Ray y tableros Grafana OSS en `sa-east-1` (ADR-14); sin herramientas duplicadas por ambiente (RT-14.01 y RT-14.02). |
| **B8 — Virtualización *on-premise*** | Proxmox VE/KVM + Ceph (12 OSD, réplica 2, 3 monitores): tolera la pérdida de cualquier nodo con quórum real (RT-03.14); respaldo único 3-2-1-1-0 con NAS D-05 y pierna inmutable en nube. |
| **B9 — Orquestación de contenedores de borde** | Docker/Docker Compose + WMS en modo reducido (mini-WMS) en los 3 *cross-docking* (E-01) y en el borde de Concepción: instalación y parcheo sin dependencia de la red, con paridad de versiones (RT-03.19). |
| **B10 — Gestión y configuración** | Ansible (F-02, parches/CIS) + Terraform/CDK IaC (multi-zona): configuración declarada como código versionado en el repositorio del CLIENTE (RT-03.03 y RT-03.15). |
| **B11 — Gestión de dispositivos de terreno (MDM)** | **N-13 — Android Enterprise / Zebra DNA (servicio gestionado)**: enrolamiento por IMEI contra el usuario, política (cifrado local, PIN, modo quiosco), actualización Over-The-Air de la aplicación y de la caché de turno, inventario del parque y **borrado remoto selectivo** (RT-03.18 y RT-08.14); sin infraestructura *on-premise* (equipo de TI de 4 personas). |
| **B12 — Gestión de secretos** | **AWS Secrets Manager + SSM Parameter Store** (N-12): rotación automática (Art. 21.4), sin credenciales embebidas; consumo saliente por VPC Endpoint desde los nodos *on-premise* (ADR-15); credencial de emergencia en sobre sellado en el recinto de custodia. |
| **B13 — Seguridad lógica** | WAF v2 + Shield + API Gateway + SIEM/Security Lake + EDR (F-03) + Macie: superficie expuesta mínima y detección concentrada en un solo registro (RT-11.07 a RT-11.16), bajo política Zero Trust (RT-11.01). |
| **B14 — Analítica / BI** | Redshift Serverless (OLAP, 5 años) + QuickSight: separación OLTP/OLAP (RT-05.05) con latencia máxima de 4 h para los tableros del CLIENTE. |
| **B15 — Licenciamiento** | Servicios AWS por servicio + OSS sin licencia (Keycloak, PostgreSQL, Proxmox VE, RabbitMQ): reversibilidad y ausencia de dependencia propietaria (RT-03.07). |

### Integración con el ERP y documentos tributarios

El ERP de 2017 **no se reemplaza ni se modifica** (Cap. 10 del caso): permanece como única fuente de verdad tributaria. La solución entrega los datos de operación a través de la capa anticorrupción (ACL, VM-04) y el ERP **emite los documentos tributarios** (guía de despacho electrónica, factura, boleta y nota de crédito con folios SII), con acuse de recibo con efectos legales —una sola verdad, un solo emisor (P5.10). El acceso desde la nube a este ERP ocurre únicamente vía la ACL (`celery-erp-sync` → ACL, nunca escritura directa).

## **(c) Implementos a Proveer (Hardware y Software)**

El inventario ofertado se agrupa en infraestructura de cómputo y almacenamiento, red y seguridad, dispositivos de terreno y operación, y componentes de sala. Son especificaciones que el CLIENTE **adquiere** y el adjudicatario instala, integra y mantiene (Art. 14.2). Las cantidades y justificaciones de cada fila se referencian al Formulario T-11.

### c.1  Infraestructura de cómputo y almacenamiento

| Componente | Producto ofertado | Ubicación | Cant. | Justificación |
|---|---|---|---|---|
| **C1 — Servidor hipervisor (clúster)** | Dell PowerEdge R6615 / HPE DL325 Gen11 — EPYC 9124 16c, 128 GB DDR5 ECC, RAID 1 SO + RAID 10 (4 × NVMe 1,92 TB + Hot-Spare), 2 × 10GbE, dual PSU 1+1 | CD Talca (Rack R01) | 3 | Cada nodo entrega el mismo cómputo y almacenamiento: N+1 según RT-08.03 y Ceph con discos NVMe en RAID 10 supera los IOPS del *peak* de septiembre. |
| **C2 — NAS respaldo local** | NAS/WORM local cifrado (LUKS/SED) — copia rápida 3-2-1-1-0 | CD Talca (Rack R01) | 1 | Copia local de recuperación rápida: restauración del WMS en ≤ 4 h sin depender del enlace (RNF-20.06), complementando —sin reemplazar— la pierna inmutable en nube. |
| **C3 — Servidor de borde Concepción** | Dell R250 / HPE DL20 Gen11 — Xeon E-2300 6c, 32 GB, RAID 10 (4 × NVMe 960 GB + Hot-Spare) | CD Concepción (gabinete) | 1 | Sostiene el WMS en modo reducido 24 h de operación autónoma (12 vCPU y 24 GB dimensionados para el volumen de Concepción), con doble fuente. |
| **C4 — Nodo de cómputo de *cross-docking*** | Mini-PC industrial Advantech ARK-2250 / NUC Pro 12 — i5/i7 12ª gen, 16 GB, NVMe 512 GB, 4G Cat-12 LTE dual SIM | Curicó, Chillán, Los Ángeles | 3 | Opera en naves sin climatización certificada (hasta 60 °C en verano) y sin fibra (RT-03.17); enlace principal Starlink por ethernet con respaldo LTE dual de dos proveedores y conmutación automática en menos de 30 s. |

### c.2  Red y seguridad

| Componente | Producto ofertado | Ubicación | Cant. | Justificación |
|---|---|---|---|---|
| **C5 — Firewall UTM / Customer Gateway** | Clúster HA Activo/Passivo — FortiGate 60F o Palo Alto PA-220, con sincronización de sesiones (D-01) | CD Talca (Rack R02) | 2 | Sin equipos únicos de perímetro (RT-08.03): la pasiva asume direcciones y túneles en menos de 30 s, en circuitos eléctricos distintos (RT-08.04). Punto de terminación de la Site-to-Site VPN y del Direct Connect activable. |
| **C6 — Switch core L3** | Stack/MLAG — Cisco Catalyst 9300-48P o equivalente (D-02), plano de distribución único | CD Talca (Rack R02) | 2 | Un único plano de distribución: la falla de un miembro no interrumpe el tráfico (RT-08.03). |
| **C7 — Switch de gestión** | 1 × L2 (VLAN MGT) + consola KVM | CD Talca (Rack R02) | 1 | Puertos de administración (IPMI/iDRAC) aislados en VLAN dedicada con MFA; operación y recuperación incluso con la red de producción caída. |
| **C8 — Red de distribución horizontal (HDA)** | Patch panels fibra OM4 + Cat6A certificado | CD Talca (Rack R03) | 1 | Cableado certificado enlace por enlace (RT-06.04) con dos ductos de ingreso independientes a la sala (RT-06.32). |
| **C9 — WLAN industrial** | AP Wi-Fi 6E industriales VLAN-Operaciones + estudio de cobertura en bodega y cámara | CD Talca + Concepción (bodegas) | 2 redes (6+3 AP) | 120 (Talca) y 30 (Concepción) terminales rugosos simultáneos; segmentación por tipo de dispositivo (RT-03.23) y verificación de cobertura dentro de las cámaras donde opera el picking (RT-03.24→RT-03.23). |
| **C10 — Enlace primario** | Fibra óptica simétrica — Talca 20→50 Mbps · Concepción 10→20 Mbps | CD Talca · CD Concepción | 2 | Dimensionado sobre el volumen real (≈ 1.400 entregas/día) y el *peak* de septiembre (≈ 2.600, 312 MB/h); respaldo escalonado sin obra adicional (RT-03.20). El camino satelital Starlink (D-06) actúa como respaldo preferente. |
| **C11 — Enlace respaldo** | LTE empresarial (SIM dedicada) — Talca 5→10 Mbps · Concepción 3→5 Mbps · *Cross-docks* 2→5 Mbps (dual, 2 proveedores) | CD Talca · CD Concepción · Curicó, Chillán, Los Ángeles | 5 | Continuidad sin un solo camino ni proveedor (RT-03.17) con conmutación automática en menos de 30 s; en los CDs queda como camino terciario tras fibra y Starlink; en los cross-docks es el respaldo automático del satelital. |
| **C12 — VPN** | AWS Site-to-Site VPN IPsec IKEv2 AES-256-GCM + BGP | Talca y Concepción → `sa-east-1` | 2 túneles/CD | Túneles IPsec con cifrado de grado comercial y enrutamiento dinámico para replicar base, sincronizar broker y transmitir telemetría sin degradar la operación (RT-03.21); MTU de túnel 1.436 bytes. |
| **C13 — Firewall de borde (CD Concepción)** | FortiGate 40F o equivalente — Customer Gateway + SD-WAN | CD Concepción (gabinete) | 1 | Customer Gateway del túnel hacia AWS y failover entre fibra, Starlink y LTE en menos de 30 s (RT-08.03, RT-03.17). |
| **C14 — Switch core de borde (CD Concepción)** | Cisco Catalyst 9300 o equivalente — capa de distribución | CD Concepción (gabinete) | 1 | Sostiene localmente la red de bodega del sitio secundario durante 24 h de autonomía sin depender del sitio principal (RT-08.03). |
| **C15 — Switch compacto *cross-docking*** | Netgear GS308E o equivalente — 8 puertos Gigabit gestionable | Curicó, Chillán, Los Ángeles | 3 | Equipo compacto y pasivo para nave industrial sin sala técnica: interconecta mini-PC, router Starlink, escáneres DS2208 y terminales (RT-03.17). |

### c.3  Dispositivos de terreno y operación

| Componente | Producto ofertado | Ubicación | Cant. | Justificación |
|---|---|---|---|---|
| **C16 — Terminal preventa** | Zebra EC55 (Android, IP67, guantes, lector 2D SE4100) | Preventistas (5 regiones) | 62 + 20 % reserva | Opera sin señal, resiste la jornada con una carga, funciona con guantes y su luminosidad es legible a pleno sol (RT-08.11). |
| **C17 — Terminal reparto** | Zebra TC58e (5G, SE55, batería 7.000 mAh, GPS L1/L5, IP65/68, −30 °C) | Conductores propios (42) + externos (≈ 160) | ≈ 200 + reserva | Un solo modelo para propios y externos: mismo repuesto, capacitación e integración (sección de Emplazamiento de este documento). |
| **C18 — Impresora cabina** | Zebra ZQ620 Plus (3", ZPL, IP54, Link-OS) | Portátil — 1 por conductor repartidor | ≈ 200 | Evidencia de entrega y comprobantes impresos en cabina, no en bodega; diseñada para vehículo con batería de reemplazo. |
| **C19 — POS móvil** | PAX A920 Pro (Android 14, PCI PTS 7.x, EMV L1/L2) | Portátil — 1 por conductor repartidor | ≈ 200 | Cobranza con tarjeta en el domicilio del cliente: acreditado PCI PTS y certificado EMV, integrado vía Bluetooth con la aplicación de reparto. |
| **C20 — Terminal RF congelado** | Zebra MC9400 Cold Storage Freezer (−30 °C, SE58 100 pies, batería *freezer* 5.000 mAh, Wi-Fi 6E) | Talca 144 (120+20 %) · Concepción 30 | 174 | Picking de la cámara a −22 °C con guantes gruesos: certificado para cámara frigorífica, lectura a distancia y batería con recambio en caliente (RT-08.11, RT-08.12 y RT-13.08). |
| **C21 — Impresora térmica andén** | Zebra ZT411 (203 dpi, 14 ips, Ethernet, ZPL) | Talca (4: 2 recepción + 2 despacho) · Concepción (2) | 6 | Etiquetas SSCC GS1-128 impresas en el andén al armar la unidad logística (RF-01.07), con resolución garantizada a lo largo de la cadena (RT-05.23). |
| **C22 — Balanza recepción** | Dibal BEV (plataforma ME + DMI-610 Inox, doble RS-232/Ethernet) | Talca (2) · Concepción (1) | 3 | Captura en línea del peso de recepción hacia el WMS (RF-01.01), sin digitación manual, con grado industrial y calibración certificada. |
| **C23 — Escáner GS1 *cross-dock*** | Zebra DS2208 (1D/2D + GS1 DataBar, garantía 60 meses) | Curicó, Chillán, Los Ángeles | 6 (2 × plataforma) | Lectura de códigos GS1 de última generación en desconsolidación y re-despacho; dos unidades por plataforma cubren dos muelles simultáneos. |
| **C24 — Sensor IoT temperatura** | Módulo Ebyte ME31-XDXX0400 (4 canales PT100, Modbus RTU/TCP, −40…+85 °C) + sondas 3 hilos — 28 puntos | Talca, Concepción, cámaras, camiones | 7 módulos | 28 puntos de medición alimentan el registro continuo de cadena de frío; exactitud ±1,1 °C a −22 °C distingue excursión térmica real de fluctuación del sensor. |
| **C25 — Termógrafo de camión** | Onset InTemp CX450 (BLE, −30…+70 °C ±0,5 °C, NIST 2 ptos) | Camiones con frío | 18 | Registrador independiente calibrado contra patrón NIST en dos puntos; el dato aterriza en el sistema por Bluetooth al volver al centro. |
| **C26 — Estaciones de trabajo** | PC i5/i7, 16 GB, SSD NVMe 512 cifrado + 2 × 24" (NCh 2527) | Talca (5) · Concepción (3) | 8 | Puestos de despacho, administración, planificación, calidad y TI (RNF-23.04): disco cifrado gestionado desde el EDR y doble monitor (RT-08.08). |
| **C27 — Kit Starlink fijo (enlace satelital D-06)** | Starlink Enterprise fijo (antena en techumbre + router) — 1 TB (CDs) / 500 GB (*cross-docks*), 56 meses | CD Talca (respaldo) · CD Concepción (respaldo) · Curicó, Chillán, Los Ángeles (principal) | 5 | Tercer camino WAN en los CDs (fibra → satelital → LTE) cerrando la brecha de Concepción (RNF-13.07); enlace principal en los *cross-docks* para la ventana de 3 h, eliminando la dependencia exclusiva de red móvil (RT-08.13, RT-06.32); reposición de hardware 15 % en 56 meses. |

> **Gateway IoT + Greengrass (B-02):** 2 unidades (Talca y Concepción), ADAM-6000, con runtime AWS IoT Greengrass Core embebido para detección de excursión y buffer local de 14 h.

### c.4  Resumen del inventario ofertado

| Familia | Cantidad |
|---|---|
| Servidores hipervisor clúster (Talca) | 3 |
| NAS respaldo local (D-05) | 1 |
| Servidor de borde Concepción | 1 |
| Mini-PC industrial *cross-docking* | 3 |
| Kit Starlink fijo WAN satelital (D-06) | 5 |
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
| Switch compacto *cross-docking* | 3 |
| Gateway IoT + Greengrass (B-02) | 2 |
| UPS 6 kVA N+1 | 1 |
| Generador 12 kVA estanque 24 h | 1 |
| CRAC de precisión N+1 | 2 |
| Cámaras IP ≥ 30 días | 7 |
| Racks 42U | 4 |
| Nube AWS (Aurora, ECS, S3, WAF, IoT, BI) | 1 solución, 2 regiones |

## **(d) Especificaciones Data Center Primaria (CD Talca)**

El recinto técnico principal se habilita en las instalaciones del CLIENTE (CD Talca) como **Sala Técnica Secundaria**, con disponibilidad de infraestructura de nivel **TIER II (99,741 %**, ≈ 22,7 h/año de corte), redundancia N+1 en energía y climatización y generador propio. El programa considera ≈ **173 m²** y **14 recintos** (sala blanca de 32 m², NOC de 14 m², sala de UPS/baterías, sala de climatización, sala de extinción, MMR y acometidas, sala de custodia, patio de generador, entre otros), dando cumplimiento a RT-06.01 a RT-06.34 y RT-10.01:

El detalle de la disposición y de los 14 recintos está declarado en la sección de Arquitectura de Seguridad de este documento (§12, seguridad física del sitio primario).


- **Energía:** UPS doble conversión *on-line* 6 kVA con configuración N+1 y banco VRLA con autonomía ≥ 30 min a plena carga (RT-06.07); grupo electrógeno de 12 kVA con estanque para 24 h y contrato de reabastecimiento (RT-06.08); transferencia automática red↔generador con prueba mensual con carga real (RT-06.10); PDU verticales A/B por gabinete con medidor (RT-08.04); factor de potencia ≥ 0,95 (RT-06.11).  
- **Climatización:** 2 CRAC de precisión ≈ 12.000 BTU/h en N+1, con *free cooling*, pasillo frío confinado y rango ASHRAE TC 9.9 de 18–27 °C y 40–60 % HR medido a la toma de aire del equipo (RT-06.13 y RT-06.14); PUE de diseño 1,7 con medición continua en 2 puntos y reporte trimestral.  
- **Incendios:** detección temprana por aspiración AnaLASER (RT-06.16); extinción con agente limpio FM-200 conforme NFPA 75/2001 con botón de aborto (RT-06.17); extintores ABC y CO₂ por recinto (RT-06.18).  
- **Seguridad física:** 4 capas de acceso con biometría facial y resguardo AFIS, esclusa antipassback y bitácora electrónica, una persona a la vez y acompañada (RT-06.20, RT-06.21 y RT-06.23); 12 puertas controladas y 7 cámaras IP con retención ≥ 30 días integradas al control de acceso (RT-06.24); NOC de 14 m² contiguo a la sala con ventana interior («ver sin entrar», RT-06.29/30); sensores ambientales DCIM/BMS (RT-06.14).  
- **Custodia de medios (RT-06.26/27/28):** recinto de 10 m² en la segunda línea, sin luz UV (≤ 300 lux), 40–60 % HR, ventilación forzada y 18–27 °C; medio cifrado transportable rotado semanalmente a bóveda externa bajo custodia acreditada con cadena de custodia y bitácora; la pierna inmutable S3 es complementaria, no la reemplaza.  
- **Cableado y comunicaciones:** cableado estructurado Cat6A F/UTP + fibra OM4 certificado enlace por enlace (RT-06.04) sobre piso técnico de 40 cm, jerarquía ANSI/TIA-942 ENI→MDA→HDA→ZDA→EDA, con dos ductos de ingreso independientes (RT-06.32); 4 racks 42U en gabinete de servidores y comunicaciones separados (RT-06.05), con el cuarto (R04) reservado al crecimiento a 3 años.

Los componentes de sala ofertados se detallan a continuación:

| Componente | Producto ofertado | Ubicación | Cant. | Justificación |
|---|---|---|---|---|
| **D1 — UPS** | Doble conversión *on-line* 6 kVA, N+1, banco VRLA ≥ 30 min | Sala de UPS/baterías (2ª línea) | 1 | Sin parpadeo entre la caída de red y la partida del generador; autonomía ≥ 30 min a plena carga (RT-06.07). |
| **D2 — Generador** | Grupo electrógeno 12 kVA, estanque 24 h + contratos de reabastecimiento | Patio generador (exterior) | 1 | Asume TI y clima en 8–15 s; el estanque garantiza 24 h (RT-06.08). |
| **D3 — ATS/TTA + tablero** | Transferencia automática red↔generador + protecciones selectivas | Acometida (accesible desde fuera) | 1 | Transferencia automática con prueba mensual con carga real y termografía periódica (RT-06.10). |
| **D4 — Climatización** | 2 CRAC de precisión ≈ 12.000 BTU/h, N+1, *free cooling*, 18–27 °C / 40–60 % HR | Sala de climatización | 2 | Rango ASHRAE en toma de aire del equipo (RT-06.13 y RT-06.14); redundancia N+1 y pasillo frío confinado. |
| **D5 — PDU racks** | 2 PDU verticales A/B por gabinete, con medidor | 4 racks sala | 4 × 2 | Dos caminos eléctricos independientes por gabinete (RT-08.04); el medidor es el denominador del PUE. |
| **D6 — Detección de incendios** | Detección por aspiración AnaLASER o equivalente | Sala blanca | 1 | Detección temprana antes de llama visible (RT-06.16). |
| **D7 — Extinción** | FM-200 o equivalente, NFPA 75/2001, botón de aborto | Sala blanca | 1 | Agente limpio sobre equipos energizados (RT-06.17) y extintores ABC/CO₂ por recinto (RT-06.18). |
| **D8 — Seguridad física** | Biometría facial + resguardo AFIS, esclusa, bitácora electrónica | Acceso a la sala (4 capas) | 1 | Doble factor con re-verificación biométrica y antipassback (RT-06.20, RT-06.21 y RT-06.23). |
| **D9 — Videovigilancia** | 7 cámaras IP, retención ≥ 30 días + respaldo auditable | Sala + perímetro | 7 | Cobertura de cada puerta controlada; «la puerta marca el video» (RT-06.24). |
| **D10 — Recinto de custodia** | Sala de custodia 10 m²: LED sin UV ≤ 300 lux, 40–60 % HR, ventilación forzada, 18–27 °C | Sala — 2ª línea | 1 | Medios de respaldo en condiciones que no degradan el soporte (RT-06.27), accesible sin cruzar la sala blanca (RT-06.26). |
| **D11 — Gabinetes** | 4 racks 42U (R01 servidores, R02 red, R03 HDA/respaldo, R04 crecimiento) | Sala blanca | 4 | Servidores y comunicaciones separados (RT-06.05); el rack R04 absorbe el crecimiento a 3 años sin obras. |
| **D12 — Cableado estructurado** | Cat 6A + fibra OM4 certificado por enlace; piso técnico 40 cm | Sala | 1 | Normativa por enlace (RT-06.04) y recorridos máximos/mínimos verificados para enlaces de 10 GbE. |

## **(e) Especificaciones Data Center Secundario y Recuperación ante Desastres**

Se declara una modalidad **activo/pasiva tibia (*warm standby*)** con tres polos: CD Talca activo, CD Concepción activo autónomo y la **réplica Aurora pasiva promueble en AWS `us-east-1`** (a ≈ 7.700 km de `sa-east-1` y ≈ 8.500 km de Talca, sin amenazas comunes según RT-07.02). La región secundaria mantiene una réplica reducida pero funcional del stack, escalable en menos de 30 min:

- **RTO/RPO:** RTO ≤ 4 h y RPO ≤ 15 min para los servicios críticos (RT-07.04); la réplica Aurora Global mantiene un retraso típico < 1 s, alarmado a los 5 y 15 min (RT-07.03) y la replicación S3 CRR con RTC cumple un RPO < 15 min.  
- **Conmutación/retorno:** *failover* en 8 pasos semiautomáticos (detección Route 53 < 5 min, promoción Aurora, escalado ECS Fargate, DNS, validación) con los pasos 4–7 automatizados mediante AWS Systems Manager Automation (RT-07.08); retorno (*failback*) en 6 pasos con reconciliación determinista de las transacciones generadas durante la contingencia (RT-07.05 y RT-07.06).  
- **Pruebas:** conmutación real dos veces al año (semestral, Art. 20 / RT-07.07) midiendo RTO y RPO efectivos con informe al CLIENTE, junto con la restauración mensual verificada con cero errores (3-2-1-1-0, RNF-20.07).  
- **Respaldos 3-2-1-1-0 (esquema único nube + *on-premise*):** la pierna **«1 inmutable»** vive en la nube (**S3 Object Lock** en modo Compliance + **AWS Backup Vault Lock**, RT-07.09 y RT-07.11); el NAS *on-premise* (D-05, WORM local + clave CMK independiente) es la **copia local de recuperación rápida** (RTO 4 h, RNF-20.06); la bóveda de custodia física externa completa la copia *offsite* (RT-06.26 y RT-06.28).  



Los componentes del sitio secundario se detallan a continuación:

| Componente | Producto ofertado | Ubicación | Cant. | Justificación |
|---|---|---|---|---|
| **E1 — Réplica DRP Aurora** | Aurora PostgreSQL pasiva promueble + AWS DMS CDC (WAL lógico, `wal_level=logical`) | AWS `us-east-1` | 1 | Réplica al día con retraso monitoreado y alarmado a los 5 y 15 min (RT-07.02 y RT-07.03). |
| **E2 — Respaldos inmutables** | S3 Object Lock + Backup Vault Lock (pierna «1 inmutable» 3-2-1-1-0) | AWS `sa-east-1` + `us-east-1` | 1 política | Copia que ni el administrador puede borrar ni modificar (RT-07.09 y RT-07.11), sobrevive incluso a incidentes con acceso privilegiado. |
| **E3 — Bóveda externa física** | Servicio de custodia/transporte acreditado + medio físico cifrado con rotación semanal | Lugar geográfico distinto de Talca | 1 contrato | Custodia física exigida (RT-06.26): medio cifrado rotado semanalmente con cadena de custodia y bitácora (RT-06.28); complementa la copia S3, no la reemplaza. |
| **E4 — Copia local de recuperación rápida** | NAS D-05 (WORM local + cifrado CMK independiente) | CD Talca (Sala) | 1 | Restauración del WMS en ≤ 4 h sin depender del enlace (RNF-20.06), verificada mensualmente con cero errores (RNF-20.07). |
| **E5 — Conmutación/retorno** | Runbook de conmutación en 6 pasos (semiautomático), *failback* con ventanilla única + reconciliación determinista | Talca / AWS | 1 procedimiento | Procedimiento documentado y ensayado dos veces al año (RT-07.05 a RT-07.07), con medición de RTO y RPO e informe al CLIENTE. |

## Niveles de Servicio de Infraestructura

La infraestructura sostiene los niveles de disponibilidad del Capítulo 7 y el compromiso contractual del Artículo 78° (transacción de negocio crítica de extremo a extremo ≥ 99,9 %). La clasificación por servicio (RT-10.02) y su *error budget* son:

- **Crítico** (≥ 99,9 %): transacción de terreno de extremo a extremo (pedido→entrega→POD) y WMS *on-premise* (picking/recepción), por detener preventa, reparto y facturación y por la ventana nocturna sin contingencia.  
- **Alto** (≥ 99 %): portal de clientes (stock, crédito, estado de cuenta) y telemetría IoT de cadena de frío en línea.  
- **Medio**: BI/analítica (reportes diferibles, latencia ≤ 4 h).  
- **Bajo**: notificaciones y comunicaciones (disponibles en colas).

La Sala Técnica Secundaria se dimensiona en **TIER II (99,741 %)** —clasificación de la infraestructura del recinto, no el SLO extremo a extremo— con *cutover* *on-premise* de 24 h (RT-03.10) y prueba de DR semestral, de modo que la cadena de disponibilidad nube→sala→borde→terreno queda declarada y medible para el CLIENTE, con compromiso contractual **≥ 99,9 % mensual de la transacción crítica de extremo a extremo (RT-10.01)**.

## Operación Desconectada (RT-03.10 a RT-03.13)

| Ámbito | Autonomía | Cobertura |
|---|---|---|
| Centro de distribución (CD Talca y Concepción) | **≥ 24 h** | Recepción, preparación, despacho, conteo cíclico y trazabilidad contra la BD local; reconciliación determinista al reconectar (RT-03.12). |
| Terreno (preventa y reparto) | **14 h** (turno completo) | Toma de pedido, entrega, POD, devoluciones y cobros contra caché local y buffer idempotente (RNF-06.02, RT-03.10); sesión sostenida por caché de identidad A-05 (TTL 8 h para bodega, 14 h para reparto/preventa). |
| *Cross-docking* | Ventana de 3 h 100 % local | Recepción, desconsolidación, validación de frío y re-despacho (RT-03.10/03.11). |
| Sincronización al reconectar | Flota ≤ 10 min · CDs ≤ 2 h | Vuelco en orden estricto, deduplicación idempotente y reconciliación determinista (RT-03.12, RT-03.13, RNF-07.01). |

---

## Arquitectura de Integración

> **Apartado 3 del Subdocumento 4 (T-22) — Arquitectura de integración: servicios, contratos, mensajería, versionado y gobierno.** Marco: BA Art. 16.4 (bitácora de reconciliación) · Art. 19 (acoplamiento débil) · Art. 21 (Zero Trust) · Art. 23 (OpenAPI/AsyncAPI, versionado y obsolescencia) · BTT RT-02.06–02.09/02.14 · RT-03.11/03.12/03.13 · RT-05.16–05.23 · RT-10.08.
>
> **Por qué la integración es una capa de primera clase en Puelche.** El caso no describe un sistema legado único que reemplazar: describe un **tejido** de sistemas —ERP de 2017 sin documentación de interfaces, WMS de 2013 con proveedor desaparecido, una preventa cuyo proveedor ya no existe, planillas y papel— más 14.200 puntos de entrega, 10 empresas transportistas y un hito externo contractual (**enero de 2029**, condiciones comerciales de la principal cadena de supermercados). El riesgo de este proyecto no está en construir módulos: está en las **costuras**.

### 1. Principios de integración

| # | Principio | Declaración | Base |
|---|---|---|---|
| 1 | **Contrato antes que conexión** | Ninguna integración existe sin contrato publicado (OpenAPI 3.1 o AsyncAPI 2.6), dueño declarado y versión semántica. Una integración sin contrato no entra al catálogo y no se despliega. | Art. 23 · RT-05.16 |
| 2 | **Asíncrono por defecto, síncrono por excepción** | Toda dependencia entre módulos se modela como **evento** por la Capa 5. Solo las lecturas críticas de la venta (disponibilidad de stock, crédito del cliente) y los actos de fe pública (DTE al SII, autorización de pago) son síncronas, y siempre con **timeout explícito**. | Art. 19 · RT-02.07/02.08 |
| 3 | **Idempotencia universal** | Toda escritura originada en terreno o en bodega lleva **UUID de cliente** y ventana de deduplicación documentada. El servidor es la fuente de verdad y resuelve conflictos por **regla de negocio**, nunca por marca de tiempo ciega. | RT-02.06 · S26 |
| 4 | **Bitácora de reconciliación auditable** | Toda decisión de reconciliación registra qué transacción, qué conflicto, qué regla se aplicó, quién la aplicó y cuándo. Es un entregable auditable ante el mandante, no un registro técnico. | **Art. 16.4** · RT-03.12 |
| 5 | **El legado nunca se escribe directo** | El ERP de 2017 se toca **solo** a través de la capa anticorrupción A-04. Ninguna cadena de supermercados, ningún portal y ningún módulo escribe al ERP. | RT-05.20 · ADR-11 |
| 6 | **Zero Trust también en la integración** | Todo tráfico on-premise → nube es **saliente** (HTTPS/443, MQTTS/8883). Las dos únicas excepciones entrantes están declaradas y acotadas (D-AL-05). | Art. 21 · D-AL-05 |
| 7 | **Toda integración declara cómo falla** | Cada entrada del catálogo declara su comportamiento ante falla —reintentar, degradar, diferir o suplir con procedimiento manual— y se verifica con inyección de fallas. | **RT-10.08** · RT-09.08 |
| 8 | **Ninguna integración interrumpe la ventana crítica** | Cargas masivas, reprocesos y despliegues de conectores se ejecutan **fuera de 05:30–07:00** de lunes a sábado. | RT-10.05 (caso) |

### 2. Vista de integración

En texto, la vista de integración se organiza en cuatro dominios con tráfico **saliente** desde el terreno y el on-premise hacia la nube:

- **Terreno (offline-first):** C-01 App Preventa (62 preventistas), C-02 App Reparto (~200 conductores) y C-03 HHT bodega (120 concurrentes).
- **On-premise (5 sitios con cómputo):** A-01 Motor WMS (M1, M2 y M5 en modo `wms_only`), A-03 RabbitMQ (buffer 24 h), A-04 capa anticorrupción (frontera única del ERP), B-02 Greengrass (buffer 14 h) y E-01 mini-WMS cross-dock (ventana de 3 h).
- **Nube AWS sa-east-1:** Amazon API Gateway (Capa 3), Capa 4 con M1–M12 en Django + workers Celery, N-09 SQS FIFO, N-09 EventBridge, M11 Hub EDI GS1 (EANCOM · GS1 XML · EPCIS) y N-08 IoT Core.
- **Terceros:** ERP 2017 (sin documentación de interfaces), SII (DTE y guía electrónica), cadenas de supermercados (hito enero 2029), Transbank Webpay/POS, GIS/mapas y notificaciones.

El flujo del tráfico: el terreno llama a la puerta de enlace (API Gateway); los HHT y el WMS publican al broker (A-03); el cross-dock (E-01) publica sus eventos críticos **directo** a SQS FIFO y solo el detalle del mini-WMS viaja a Talca — lo crítico no depende de Talca (D-AL-04); Greengrass envía por IoT Core; y la Capa 4 consume las colas y alcanza el ERP **únicamente** a través de la capa anticorrupción (A-04), con una sola puerta hacia el legado. Las flechas desde el dominio on-premise hacia la nube son **todas salientes**.

### 3. Catálogo de servicios de integración (RT-05.16 · RT-05.21)

El catálogo es el **registro único** de integraciones. Cada entrada tiene identificador estable, módulo dueño, contrato, versión y comportamiento ante falla. Vive versionado junto al código y se publica en el portal interno de desarrolladores servido por **Amazon API Gateway** (Capa 3).

#### 3.1 Integraciones internas — superficies y plano híbrido

| ID | Integración | Modo | Contrato | Módulo dueño | Ventana crítica | Comportamiento ante falla (RT-10.08) |
|---|---|---|---|---|---|---|
| **INT-01** | App Preventa ↔ plataforma (pedidos, stock, crédito, promociones, precios) | Síncrono para lectura + **sincronización diferida idempotente** para escritura | OpenAPI 3.1 `/v1/preventa` y `/v1/sync` | M3 | 09:00–18:00 | Caché de turno (saldo, stock, tarifa; TTL 8 h); el pedido se toma sin conexión y se confirma en la sincronización; **no se pierde** |
| **INT-02** | App Reparto ↔ plataforma (POD, entregas, devoluciones, cobranza, envases) | Sincronización diferida idempotente por lotes | OpenAPI 3.1 `/v1/reparto` y `/v1/sync` | M6, M7, M8 | 05:30–07:00 y 17:00–20:00 | Turno completo de 14 h sin señal; sincronización **≤ 10 min** al reconectar (RT-03.12); acuse por lote (RF-06.07) |
| **INT-03** | Broker on-premise → nube (reconciliación del WMS) | Asíncrono | AsyncAPI 2.6 · SQS FIFO, `MessageGroupId` = sitio | M2, M5 | 22:00–06:00 | Buffer RabbitMQ **24 h**; publicación cronológica al reconectar; el CD queda sincronizado **≤ 2 h** tras un corte de 24 h |
| **INT-04** | Cross-dock → Talca (detalle del mini-WMS) | Asíncrono broker a broker | AsyncAPI 2.6 · AMQPS 5671 | M2 | 03:00–06:00 | Ventana de 3 h 100 % local; los eventos críticos van directo a SQS y **no dependen de Talca** (D-AL-04) |
| **INT-05** | Borde IoT → nube (cadena de frío) | Asíncrono, al menos una vez | AsyncAPI 2.6 · MQTTS 8883 con X.509 por dispositivo | M9, M12 | 24×7 | Buffer Greengrass **14 h**; la detección de excursión y el **bloqueo de despacho son 100 % locales** y no dependen de la nube |
| **INT-12** | Réplica WMS → Aurora (continuidad) | Asíncrono CDC | WAL lógico (`wal_level=logical`) por AWS DMS | M2 | continua | Excepción entrante declarada (D-AL-05); si la VPN cae, DMS encola en origen y reanuda sin pérdida — RPO ≤ 15 min |
| **INT-13** | Identidad: maestro → cachés locales | Asíncrono (importación del Realm cifrado por S3, saliente) | Exportación/importación de Realm Keycloak | Capa 7 | 24×7 | Δ ≤ 8 h por TTL y ≤ 24 h por SCIM; **sin conexiones entrantes** hacia Keycloak |
| **INT-14** | Observabilidad on-premise → plataforma | Asíncrono (OTLP) | OpenTelemetry | Capa 8 | 24×7 | Buffer en disco 24 h; el envío diferido cierra el hueco al reconectar |

#### 3.2 Integraciones externas — plataforma y terceros

| ID | Sistema | Modo | Contrato / estándar | Volumen declarado | Ventana crítica | Comportamiento ante falla (RT-10.08) |
|---|---|---|---|---|---|---|
| **INT-06** | **ERP 2017** (catálogo, stock valorizado, cobranzas, contabilidad) | Asíncrono por colas + síncrono **solo lecturas** | OpenAPI 3.1 **de Puelche** expuesto por la ACL (A-04); el ERP no publica contrato propio | ≈ 34.000 DTE/mes; cobranzas por turno | Cierre contable diario y primeros tres días hábiles del mes | **Cortacircuito**: preventa y reparto no se degradan; las colas retienen hasta 24 h; el desajuste se declara en la bitácora del Art. 16.4 |
| **INT-07** | **SII** — DTE, guía de despacho electrónica y acuse de recibo | Síncrono por la puerta de enlace | Formato de la autoridad tributaria (RT-05.23); firma conforme a la Ley 19.799 | ≈ 34.000 documentos/mes; pico en 05:30–07:00 | Emisión por turno | **La entrega no se detiene**: evidencia local (firma, QR, fotografía) y **timbre diferido** con folio reservado por dispositivo; reintento con retroceso exponencial — **cero guías de papel** (RF-06.02) |
| **INT-08** | **Cadenas de supermercados** — canal moderno | Asíncrono (AS2) + API síncrona selectiva | **EANCOM D.01B / GS1 XML** (pedido, aviso de despacho, factura) y **EPCIS** para eventos de trazabilidad | 500 puntos de entrega del canal moderno | **Ventana de 30 min** (RF-12.10); hito **enero de 2029** (RNF-12.01) | DLQ y **bandeja de excepciones** operada por un actor canónico (RF-12.05/12.06); alternativa manual declarada por acuerdo con cada cadena |
| **INT-09** | **Transbank Webpay y POS móvil** | Síncrono por la puerta de enlace | API de la pasarela; idempotencia por `transaction_id` | ≈ 1.400 entregas/día (≈ 2.600 en el peak); ≈ 11.800 cobros en efectivo/mes | 05:30–07:00 | **Doble captura sin conexión**: el POS registra la transacción como pendiente para autorización diferida; si no procede, efectivo o giro a crédito con firma. **El cobro nunca se pierde** |
| **INT-10** | **GIS, mapas, ETA y geocercas** | Síncrono por la puerta de enlace | API del proveedor GIS | Planificación diaria de ≈ 96 camiones | Planificación previa al despacho | **Caché de mapas por zona** en el dispositivo; degradación a ruta sin conexión con la secuencia ya cargada (M4); la entrega no se pierde |
| **INT-11** | **Notificaciones** — correo, aplicación, mensajería instantánea y SMS | Asíncrono por colas | API del proveedor de notificaciones | Avisos de despacho y de llegada por turno | Previo a la entrega | Cola local con entrega diferida; el canal se elige **por cliente**, porque buena parte del canal tradicional no usa correo (RT-16.21) |
| **INT-15** | **Telemetría de flota existente** (camiones propios) | Asíncrono, solo lectura | API de la fuente existente (RT-17.06) | 42 vehículos propios; ≈ 420.000 km/mes | Operación diurna | Degrada a ruta planificada sin posición real; **no se usa para control de jornada** (D1, objeción sindical L577) |

> **Número de integraciones declarado: 15** (8 internas, 7 externas). El numeral 14.2 del caso exige declarar además el **volumen de mensajes por integración**. Los volúmenes de negocio están arriba; su traducción a mensajes por día es una de las celdas que debe cerrarse (hallazgo D1 de la auditoría de coherencia del Subdocumento 4).

### 4. Contratos (RT-05.16 · RT-05.18 · Art. 23)

| Dimensión | Definición |
|---|---|
| **API síncrona** | **OpenAPI 3.1** por módulo, con ruta `/v{major}/...`. Metadatos obligatorios: `x-owner` (módulo dueño), `x-version` (semver), `x-status` (`draft`, `stable`, `deprecated`) y `x-sunset` (fecha de retiro). |
| **Eventos** | **AsyncAPI 2.6** con **JSON Schema** versionado por evento. Cada evento declara productor único, consumidores registrados, clave de partición y política de reintento. |
| **Autenticación** | Superficies: **OAuth 2.1 con PKCE**. Servicio a servicio: **mTLS**. Máquina a máquina: credenciales de cliente con secreto de rotación automática. Todos los tokens los firma Keycloak (Capa 7). |
| **Validación** | Validación de esquema e inspección de carga útil **en la puerta de enlace** (Art. 21.2), antes de alcanzar la Capa 4. Un mensaje que no valida no entra: se rechaza con causa y queda registrado. |
| **Trazabilidad** | Todo llamado y todo evento propaga `transaction_id` (OpenTelemetry) desde la Capa 3 hasta la Capa 6. Es la clave con la que se reconstruye una operación de extremo a extremo, conforme al Art. 23: quién, qué, cuándo, desde dónde y con qué valores anteriores y posteriores. |

#### 4.1 Eventos canónicos del dominio

Los eventos son el vocabulario del sistema. Se nombran en pasado, son inmutables y llevan `event_id` (UUID), `occurred_at`, `site_id` y `transaction_id`.

| Evento | Productor | Consumidores | Clave de partición | Por qué existe (origen en el caso) |
|---|---|---|---|---|
| `RecepcionConfirmada` | M1 | M2, M9, ACL → ERP | `site_id` | Origen de la trazabilidad de lote (Cap. 9.5: retiro sanitario en menos de 2 h) |
| `StockReservado` / `ReservaLiberada` | M2 | M3, M5 | `sku_id` | Resuelve el doble compromiso de stock (decisión 16.1 N° 8) |
| `PedidoConfirmado` | M3, M11 | M4, M5, M7 | `pedido_id` | Une preventa y canal moderno en un único flujo |
| `MisionPreparada` | M5 | M6, ACL → ERP | `pedido_id` | Cierra el ciclo de bodega a andén |
| `EntregaRegistrada` | M6 | M7, M8, M10, SII | `entrega_id` | Define «entrega cumplida» y alimenta el OTIF (decisión 16.1 N° 1) |
| `DevolucionRegistrada` | M8 | M2, M7, M10 | `entrega_id` | Efecto sobre el documento tributario ya emitido (decisión 16.1 N° 12) |
| `EnvaseMovido` | M8 | M2, M10 | `cliente_id` | 68.000 canastillos y 9.400 pallets con 14 % de pérdida anual (decisión 16.1 N° 10) |
| `ExcursionTermicaDetectada` | M9 (borde) | M5 (bloqueo), M10, alertas | `shipment_id` | Alerta en menos de 5 s; el bloqueo de despacho es **local** (decisión 16.1 N° 4) |
| `RendicionCerrada` | M7 | M10, ACL → ERP | `conductor_id` | Control del efectivo que hoy circula en ruta |
| `DesviacionDeRutaDetectada` | M12 | M10, M9 | `ruta_id` | Costo de servir; **no** control de jornada (D1) |

### 5. Mensajería (RT-02.06 · RT-02.07 · ADR-05)

| Plano | Tecnología | Emplazamiento | Rol |
|---|---|---|---|
| **Buffer local de sitio** | **RabbitMQ** (A-03) | VM-03 Talca (≈ 3 M mensajes) · VM-C04 Concepción · broker en E-01 | Sostiene la **autonomía de 24 h** del centro de distribución. Es lo que permite que la bodega reciba, prepare y despache con el enlace caído. |
| **Trabajo y reconciliación** | **SQS FIFO** (N-09) | Nube | Orden garantizado **por partición** (`MessageGroupId` = sitio) y deduplicación; alimenta a `celery-reconciliation` y `celery-erp-sync`. |
| **Bus de eventos de negocio** | **EventBridge** (N-09) | Nube | Coreografía entre módulos y disparo de alertas y notificaciones. Un módulo publica; los interesados se suscriben. |
| **Transporte hacia la nube** | *Shipper* en VM-03 (modo `wms_only`) | On-premise → nube | **HTTPS 443 sobre VPC Endpoint SQS/PrivateLink** (D-AL-03). AMQPS 5671 queda reservado a broker con broker on-premise. |

**Garantías declaradas:**

- **Entrega al menos una vez, con deduplicación en el consumidor.** No se promete entrega exactamente una vez: se promete **idempotencia verificable**.
- **Orden por partición**, no orden global. La partición es el sitio o la entidad de negocio, según el evento.
- **DLQ por cola** con retención declarada, monitoreada por el equipo de operación y con bandeja de excepciones cuando el mensaje afecta a un tercero (EDI, DTE).
- **Reintento con retroceso exponencial y variación aleatoria**; **cortacircuitos** sobre ERP, SII y Transbank; **mamparos** por integración: un fallo del ERP no degrada la preventa.
- **Reconciliación determinista:** al reconectar, el conflicto de stock se resuelve por la **regla de reserva** declarada, nunca por marca de tiempo, y la decisión queda en la bitácora del Art. 16.4.

### 6. Costuras híbridas — amarre con la arquitectura física

La vista de integración y la vista física describen los mismos puntos de contacto. Esta tabla es el amarre entre ambas y se lee junto a la sección **Costuras híbridas** (§6) de este mismo Subdocumento.

| Costura física | Integración lógica | Contrato | Extremos |
|---|---|---|---|
| C1 — VPN corporativa | portadora de INT-06 e INT-12 | IPsec/IKEv2, BGP, MTU 1436 | D-01 ↔ VGW |
| C2 — Réplica WMS → Aurora | **INT-12** | WAL lógico / DMS CDC | VM-02 ↔ Aurora |
| C4 — Broker → SQS FIFO | **INT-03** | AsyncAPI 2.6 | VM-03 ↔ N-09 |
| C5 — ERP por la ACL | **INT-06** | OpenAPI 3.1 de Puelche | VM-04 ↔ `celery-erp-sync` |
| C6 — Identidad | **INT-13** | Realm cifrado por S3 | Keycloak maestro ↔ A-05 / VM-C03 |
| C7 — IoT Greengrass | **INT-05** | MQTTS 8883, X.509 | B-02 ↔ N-08 |
| C8 — Observabilidad | **INT-14** | OTLP | F-01 ↔ CloudWatch / X-Ray / AMP |
| C10 — Apps de terreno | **INT-01 / INT-02** | OpenAPI 3.1 | C-01 / C-02 ↔ Capa 3 |
| C13 — Cross-dock | **INT-04** | AsyncAPI 2.6 / AMQPS | E-01 ↔ VM-03 y ↔ N-09 |
| C14 — Notificaciones y EDI | **INT-08 / INT-11** | GS1 / API de notificaciones | EventBridge ↔ terceros |
| C15 — Portales de la DMZ | INT-01 (lectura de stock, crédito y cobranza) | OpenAPI 3.1 | N-01/N-02/N-03 ↔ Capa 3 |
| C16 — Pago Transbank | **INT-09** | API de la pasarela | Módulo `integraciones` ↔ Webpay |

### 7. Capa anticorrupción y estrangulamiento del legado (RT-05.20 · RT-02.14 · ADR-08 · ADR-11)

**Frontera única del ERP (A-04).** El ERP de 2017 no tiene documentación de interfaces. En vez de descubrir su forma real dentro de cada módulo, se levanta **una sola frontera**: la ACL expone hacia adentro un contrato **OpenAPI 3.1 propio de Puelche** y absorbe hacia afuera la forma del ERP. Consecuencias:

- El conocimiento del ERP queda **concentrado y documentado en un solo componente**, no disperso en doce módulos.
- Ningún módulo, portal ni cadena de supermercados escribe al ERP: `celery-erp-sync` publica notificaciones por SQS y **lee** contratos por la ACL.
- Cuando una capacidad del ERP se absorbe en la plataforma, se retira de la ACL sin tocar a los consumidores.

**Estrangulamiento del WMS de 2013 (ADR-08).** El WMS se reemplaza en la Etapa 1 por los módulos M1, M2 y M5 del monolito. Durante la coexistencia el legado queda **detrás de la misma ACL**, con una tabla de «capacidad absorbida» —recepción GS1, *slotting*, misiones de picking con HHT, conteo cíclico— que se vacía ola a ola por sitio, con estrategia azul-verde y plan de reversión.

**Hub EDI GS1 (ADR-11).** Una cadena nueva se incorpora por **configuración de perfil** (equivalencias GTIN por cadena, RF-12.03), no por desarrollo. El hub mapea cada cadena contra un **modelo canónico GS1**, no contra el ERP: es exactamente lo que evita construir una integración distinta por cada cadena (Cap. 17.4, punto 10 del caso).

### 8. Versionado y política de obsolescencia (RT-05.17 · Art. 23)

| Regla | Definición |
|---|---|
| **Versionado semántico estricto** | `major.minor.patch`. `major` = cambio disruptivo; `minor` = aditivo y retro-compatible; `patch` = corrección. |
| **Evolución aditiva primero** | Un campo se agrega, nunca cambia de significado. Un campo que deja de usarse se marca `deprecated` antes de retirarse. |
| **Preaviso mínimo de 6 meses** | Ninguna versión se retira antes de seis meses de aviso formal (Art. 23 y RT-05.17). El registro de deprecaciones es visible para todo el equipo y para el CLIENTE. |
| **Doble versión concurrente** | Durante la migración conviven `v{n}` y `v{n+1}`; el consumidor migra en su ventana, no en la del proveedor. |
| **Aprobación de cambios disruptivos** | Un `major` requiere aprobación del **Comité de Arquitectura** y plan de migración con los consumidores identificados uno a uno. |
| **Congelamientos del caso** | No se publica ni se retira ninguna versión en **septiembre**, en **diciembre** ni en los **tres primeros días hábiles del mes** (Cap. 13.2 del caso). |
| **Contratos que no controla el proponente** | Las especificaciones de cada cadena de supermercados y del SII las fija la contraparte: se versionan como **perfiles del hub** y se prueban contra el banco de pruebas de cada contraparte antes de activarse. |

### 9. Gobierno de la capa de integración (Art. 19 · RT-05.16 · Cap. 14 BTT)

| Mecanismo | Cómo opera | Responsable |
|---|---|---|
| **Catálogo único versionado** | Toda integración vive en el catálogo con dueño, contrato, versión, estado y comportamiento ante falla. Lo que no está en el catálogo no se despliega. | Arquitecto de Solución |
| **Comité de Arquitectura** | Aprueba altas de integración y cambios `major`, con cadencia declarada en el plan de gobierno del proyecto. | Arquitecto de Solución, Jefe de Proyecto y Jefe de TI del CLIENTE |
| **Pruebas de contrato consumidor-proveedor** | Cada integración tiene pruebas de contrato en el pipeline; un cambio que rompe a un consumidor registrado **bloquea el despliegue** de forma automática. | Líder de Desarrollo y Líder de Calidad |
| **Pruebas de falla por integración** | Inyección de fallas (RT-10.07) por integración durante la marcha blanca: se verifica que el comportamiento declarado en el catálogo sea el comportamiento real. | Líder de Calidad y Líder de Operación |
| **Observabilidad por integración** | Latencia, tasa de error, volumen y profundidad de DLQ por integración, correlacionados por `transaction_id` (Capa 8). Toda DLQ tiene dueño y alerta. | Líder de Operación / SRE |
| **Bandeja de excepciones de negocio** | Lo que falla y afecta a un tercero (EDI, DTE) no muere en una cola técnica: aparece en una bandeja operada por un actor canónico con responsabilidad declarada (RF-12.05/12.06). | Jefe de TI y responsable del canal moderno |
| **Traspaso al equipo de cuatro personas** | El CLIENTE opera con **4 personas de TI**. El catálogo, las guías de resolución y la bandeja de excepciones son los artefactos que hacen operable esta capa sin el proponente. | Líder de Implantación y Gestión del Cambio |

### 10. Carga y descarga masiva de datos (RT-05.22)

| Escenario | Mecanismo | Control y auditoría |
|---|---|---|
| Carga inicial de maestros e históricos (ERP y WMS) | Proceso ETL por lotes con inserción **idempotente por UUID**, en ventana sin operación | Conteo previo y posterior por lote, conciliación de totales y bitácora de carga (quién, cuándo, lote, resultado); los rechazados van a cuarentena con reproceso |
| Descarga regulatoria (traza de lote, temperaturas, DTE, geolocalización) | Exportación **asíncrona** a CSV o Parquet, firmada y con suma de verificación | Registro de la extracción (solicitante, filtro, resultado) y control de acceso a datos sensibles (RT-16.09) |
| Sincronización masiva de turno (terreno) | Sincronizadores con **partición y reanudación** más deduplicación; los medios van a S3 por objeto | Nivel de servicio comprometido: **turno completo ≤ 10 min**; métricas de sincronización en la Capa 8 |
| Interfaces periódicas con terceros | Colas con `batch_id` y confirmación por lote | Monitoreo de DLQ y **acuse por lote** en la bandeja de excepciones |

> **Regla:** ninguna carga masiva se ejecuta dentro de la ventana crítica **05:30–07:00**, y toda carga queda registrada y es auditable.

### 11. Funciones que no operan sin conexión (RT-03.13)

La declaración formal que exige RT-03.13 vive en la Tabla de Emplazamiento v06 (§1.1) y en la Arquitectura Lógica v6.2 (§9.5). Desde la vista de integración la regla es una sola:

> **Lo transaccional crítico de terreno y de bodega opera sin conexión (14 h en terreno, 24 h en el centro de distribución). Lo que depende de la nube o de un tercero degrada con procedimiento manual declarado y sin pérdida de datos.**

Ninguna función de la ventana crítica de despacho (05:30–07:00) depende de una integración externa: el DTE se timbra de forma diferida con folio reservado, el cobro se captura como pendiente, la excursión térmica se detecta y bloquea localmente, y la ruta ya está cargada en el dispositivo.

### 12. Referencias cruzadas con las decisiones de arquitectura

| ADR | Aporte a la vista de integración |
|---|---|
| ADR-01 | Monolito modular: los módulos se comunican por eventos internos; EDI, telemetría y sincronización son *workers* extraíbles |
| ADR-05 | Mensajería asíncrona: RabbitMQ local con buffer de 24 h más SQS FIFO y EventBridge en nube |
| ADR-06 | Identidad: el maestro publica hacia las cachés (INT-13), nunca a la inversa |
| ADR-08 | WMS de 2013: absorción por estrangulamiento detrás de la ACL, con reversión azul-verde |
| ADR-11 | Hub EDI GS1 centralizado con capa anticorrupción; una cadena nueva se agrega por configuración |
| ADR-12 | El peak de septiembre se absorbe con elasticidad de los consumidores de cola, no con más integraciones |

### 13. Trazabilidad normativa (resumen)

| Requisito | Cómo se cumple |
|---|---|
| BA Art. 16.4 | Bitácora de reconciliación auditable de cada decisión de conflicto (§1, §5) |
| BA Art. 19 | Acoplamiento débil por eventos; dependencias síncronas acotadas y con timeout (§1, §3) |
| BA Art. 21 | Zero Trust: tráfico saliente; validación de esquema e inspección de carga útil en la puerta de enlace (§1, §4) |
| BA Art. 23 | OpenAPI 3.1 y AsyncAPI con versionado semántico y obsolescencia con preaviso de seis meses (§4, §8) |
| RT-02.06 | Idempotencia con UUID y ventana de deduplicación documentada (§1, §5) |
| RT-02.07 | Entrega al menos una vez, deduplicación y orden por partición (§5) |
| RT-02.08 / RT-02.09 | Reintento con retroceso, cortacircuitos, mamparos, timeout obligatorio y degradación elegante (§5) |
| RT-02.14 | Capa anticorrupción y estrangulamiento del legado (§7) |
| RT-03.11 / RT-03.12 | Registro local íntegro y reconciliación determinista con bitácora (§5, §11) |
| RT-03.13 | Declaración de funciones no disponibles sin conexión y procedimiento manual (§11) |
| RT-05.16 | Contratos formales OpenAPI 3.1 y AsyncAPI 2.6 con dueño y estado (§4) |
| RT-05.17 | Obsolescencia con seis meses de preaviso y doble versión concurrente (§8) |
| RT-05.18 | OAuth 2.1 con PKCE en superficies y mTLS entre servicios (§4) |
| RT-05.20 | Capa anticorrupción frente al ERP de 2017 y al WMS de 2013 (§7) |
| RT-05.21 | Matriz de integraciones con modo, volumen y ventana (§3) |
| RT-05.22 | Carga y descarga masiva con volumen, frecuencia y control de calidad (§10) |
| RT-05.23 | Estándares sectoriales: GS1 (EANCOM, GS1 XML, EPCIS) y formato de la autoridad tributaria (§3.2) |
| RT-10.08 | Comportamiento ante falla declarado por integración y verificado con inyección de fallas (§3, §9) |
| Caso Cap. 17.4, puntos 5, 6, 8 y 10 | Integración con el ERP y con los documentos tributarios (§3.2, §7); destino del WMS de 2013 (§7); evidencia de entrega articulada con la guía electrónica (INT-07); canal moderno sin una integración por cadena (§7) |

---

## Arquitectura de Seguridad

> **Apartado 4 del Subdocumento 4 (T-22) — Arquitectura de seguridad: modelo Zero Trust, capa expuesta, identidad, cifrado y controles.** Marco: BA Art. 21 (seguridad y ciberseguridad) · Art. 22 (identidad, acceso y sesiones) · Art. 23 (datos y residencia) · Art. 16.3/16.4 · BTT Cap. 11 (RT-11.01–11.28), Cap. 12 (RT-12.01–12.13), RT-03.15/03.18/03.22, RT-16.07/16.09 · NIST SP 800-207 · ISO/IEC 27001:2022 · STRIDE · Ley 21.719 · Ley 19.799.
>
> Es además el **documento de seguridad del subdocumento**: es autocontenido y los valores aquí declarados no son nuevos salvo donde se indica expresamente (consolidan lo comprometido en este mismo Subdocumento 4.2).
>
> **Por qué la seguridad de Puelche no es la de una oficina.** El perímetro de esta solución no es un edificio: son 62 preventistas de pie en la puerta de un almacén, ~200 conductores —de los cuales ~160 **no son trabajadores de la compañía y rotan sin aviso**—, dispositivos compartidos entre turnos en una cámara a −22 °C, un turno de preparación con 38 % de rotación anual y 14.200 puntos de entrega. Un modelo de seguridad basado en la red corporativa aquí no protege nada. Por eso el modelo es Zero Trust y por eso la identidad es la pieza central.

### 1. Principios rectores

| # | Principio | Declaración | Base |
|---|---|---|---|
| 1 | **Zero Trust conforme a NIST SP 800-207** | Verificación explícita de cada solicitud, privilegio mínimo y presunción de compromiso. La red interna **no** confiere confianza. | Art. 21.1 |
| 2 | **Seguridad desde el diseño y por defecto** | Modelado de amenazas **STRIDE** documentado por cada componente y por cada integración externa, antes de implementar. | Art. 21.1 · RT-11.02 |
| 3 | **La identidad es el perímetro** | Autoridad única de identidad (Keycloak, Modelo B); toda decisión de acceso se toma sobre el token, no sobre la dirección de red de origen. | Art. 22 · RT-12.01 · ADR-06 |
| 4 | **Sin conexiones entrantes al on-premise** | Todo tráfico on-premise → nube es saliente. Las dos únicas excepciones (DMS → PostgreSQL y `celery-erp-sync` → ACL) están declaradas, acotadas al túnel IPsec autenticado y auditadas. | Art. 21 · D-AL-05 · RT-11.13 |
| 5 | **Cifrado en tránsito y en reposo sin excepciones** | TLS 1.3 mínimo con HSTS; cifrado en reposo del 100 % de los datos con claves gestionadas en KMS/HSM y separación de funciones en su custodia. | Art. 21.2 · RT-11.08/11.09 |
| 6 | **La seguridad no puede detener la ventana crítica** | Ningún control de seguridad puede introducir una dependencia en línea dentro de 05:30–07:00 ni en las 14 h de terreno sin señal. La autenticación de terreno se resuelve **sin red** por diseño. | RT-10.05 (caso) · RT-03.10 |
| 7 | **Operable por cuatro personas** | El CLIENTE tiene 4 personas de TI. Se privilegian servicios administrados y un SOC contratado 24×7 por sobre plataformas que exijan operación local especializada. | Art. 16.3 · Cap. 2.4 del caso |
| 8 | **Evidencia inalterable** | Todo evento de seguridad y toda acción de negocio quedan en un registro **inalterable** y con retención declarada; ni un administrador puede modificarlo. | Art. 21.3 · RT-11.14 · RT-16.07 |

### 2. Modelo Zero Trust aplicado (Art. 21.1 · NIST SP 800-207)

#### 2.1 Los siete principios de NIST SP 800-207 en Puelche

| Principio NIST | Aplicación concreta en esta solución |
|---|---|
| Todo recurso de datos y servicio de cómputo es un recurso a proteger | Los 12 módulos, las 15 integraciones del catálogo, las bases on-premise y en nube, el borde IoT y los HHT de bodega están inventariados como recursos con dueño y clasificación |
| Toda comunicación se asegura sin importar la ubicación de red | TLS 1.3 entre superficies y borde; **mTLS servicio a servicio**; IPsec/IKEv2 con AES-256-GCM en la VPN; MQTTS con X.509 por dispositivo en el borde IoT |
| El acceso se concede por sesión | Tokens de vida breve firmados por Keycloak; el token de terreno se emite por **turno**, no de forma permanente |
| El acceso lo determina una política dinámica | **RBAC** por los 11 actores canónicos más **ABAC** por atributos de contexto: instalación asignada, horario de turno y dispositivo provisto (verificado por MDM) |
| Se vigila la integridad y postura de todos los activos | EDR en todos los nodos on-premise y estaciones (F-03); MDM con postura y estado de sincronización en los dispositivos de terreno (§4.6); escaneo semanal de vulnerabilidades |
| La autenticación y autorización son dinámicas y estrictamente aplicadas antes de conceder acceso | Autenticación en la puerta de enlace (OIDC), autorización en la Capa 4; elevación temporal de privilegios con aprobación y grabación |
| Se recolecta el máximo de información para mejorar la postura | SIEM (Security Lake) con **casos de uso del proceso logístico**, no solo de infraestructura; correlación por `transaction_id` en la Capa 8 |

#### 2.2 Zonas y flujos

En texto, las zonas y su flujo son: la **zona pública** (clientes del canal moderno, transportistas ≈160 conductores y 180 proveedores) ingresa únicamente por la **DMZ en nube** (CloudFront + AWS WAF v2 + Shield Advanced → Amazon API Gateway con OIDC, cuotas, esquema y validación de carga útil); la **zona de aplicación** (ECS Fargate M1–M12 + workers y Keycloak IdP maestro como autoridad única) sirve a las **zonas de datos** (Aurora PostgreSQL, DynamoDB y S3 con Object Lock, en subredes privadas sin salida); la **zona on-premise** (VLAN 10 MGT · 20 SRV · 30 OPS · 40 WKS · 50 IOT, firewall D-01 UTM en HA como Customer Gateway y caché Keycloak de solo lectura TTL 8 h) conecta con la nube por VPN/IPsec saliente; y la **zona de terreno** (apps Kotlin offline-first + MDM; HHT compartidos en cámara a −22 °C) no tiene perímetro.

**Reglas de zona declaradas:**

- La **única** exposición pública es la DMZ en nube (CloudFront → WAF → API Gateway). Las consolas internas **no** pasan por ahí: entran por intranet o VPN (RT-03.22).
- La zona de datos **no tiene salida a internet** y se consume por VPC Endpoints/PrivateLink.
- Desde la zona on-premise no se acepta ninguna conexión entrante salvo las dos excepciones D-AL-05.
- La zona de terreno **no tiene perímetro**: se protege con identidad, cifrado local, MDM y borrado remoto.

### 3. Capa expuesta (Art. 21.2 · RT-11.11/11.13)

| Control | Implementación | Exigencia |
|---|---|---|
| **Publicación exclusiva por capa de borde** | CloudFront (CDN) como único origen público; los orígenes están restringidos y no se alcanzan directamente | Art. 21.2 |
| **WAF con reglas gestionadas y personalizadas** | AWS WAF v2: conjunto gestionado OWASP Top 10 más reglas propias por API (límites de tamaño, patrones de la operación logística) | Art. 21.2 |
| **Protección DDoS en capas 3, 4 y 7** | AWS Shield Advanced con respuesta gestionada | Art. 21.2 |
| **TLS 1.3 y prohibición de TLS 1.0/1.1** | TLS 1.3 mínimo, conjuntos de cifrado modernos con AEAD, **HSTS con precarga**; deshabilitados RC4 y CBC sin AEAD | Art. 21.2 · RT-11.08 |
| **Gestión automatizada de certificados** | Inventario centralizado, renovación automática y **alerta anticipada a 30 días** del vencimiento; revisión de cadenas en la prueba semestral | RT-11.08 |
| **Puerta de enlace con controles completos** | API Gateway con autenticación OIDC, autorización por rol, **cuotas y límites de tasa por cliente**, validación de esquema e **inspección de carga útil** | Art. 21.2 · RT-11.11 |
| **Protección contra bots y abuso automatizado** | Reto progresivo en los puntos de entrada públicos (catálogo público y portales), sin degradar la accesibilidad | Art. 21.2 |
| **Superficie de exposición declarada** | Inventario completo de servicios, protocolos y puertos por sitio y por zona (§3.1) | **RT-11.13** |

#### 3.1 Superficie de exposición completa (RT-11.13)

| Zona / sitio | Servicios expuestos | Protocolos y puertos | ¿Alcanzable desde internet? |
|---|---|---|---|
| DMZ pública en nube | Portales N-01, N-02 y N-03 sobre `*.puelche.cl`; catálogo público | 443/TCP (HTTPS, TLS 1.3) | **Sí**, por CloudFront con WAF y Shield |
| Zona de aplicación en nube | ECS Fargate, Keycloak maestro | Solo desde el ALB y la puerta de enlace; sin dirección pública | No |
| Zona de datos en nube | Aurora, DynamoDB, S3 | Solo por VPC Endpoint/PrivateLink | No |
| Talca — red interna | Portal WMS, API WMS, PostgreSQL, caché LDAPS, broker AMQP, gestión SSH | 443, 8080, 5432, 636, 5671–5672, 22 (VLAN MGT con MFA) | **No** — solo por VPN Zero Trust |
| Talca — borde | Clúster de firewall en HA (Customer Gateway) | IPsec 500/4500 UDP | Solo terminación IPsec; ningún otro servicio |
| Talca / Concepción — IoT | Greengrass hacia IoT Core | MQTTS 8883 **saliente** | No; sin puertos entrantes |
| Concepción y cross-docking | Gabinete de borde (mini-PC) | IPsec 500/4500 UDP; SSM 443 saliente | Solo por VPN IPsec / SSM |
| Estaciones de trabajo | — | 443 saliente por proxy | No |

> **Regla declarada:** ningún nodo on-premise abre puertos entrantes. Toda gestión remota entra por el agente SSM sobre HTTPS saliente o por la VPN, nunca por un puerto publicado.

### 4. Identidad, acceso y sesiones (Art. 22 · BTT Cap. 12 · ADR-06)

#### 4.1 Modelo de identidad (Modelo B)

**Autoridad única en nube, cachés locales de solo lectura.** El **Keycloak IdP maestro** vive en ECS Fargate (sa-east-1, Multi-AZ, respaldo en Aurora) y concentra **todas** las escrituras: altas, bajas, cambios de rol, políticas y revocaciones. En VM-05 (Talca) y VM-C03 (Concepción) operan **cachés locales de solo lectura con TTL de 8 h** que validan la firma OIDC de forma local. **No existe un maestro on-premise ni promoción local a escritura.**

Esta decisión resuelve un problema real del caso: el centro de distribución debe autenticar durante 24 h sin enlace y el terreno durante 14 h sin señal, pero un segundo maestro on-premise habría creado dos fuentes de verdad de identidad y un procedimiento de conmutación con riesgo de divergencia. Con el Modelo B, el **DRP de identidad es la misma autoridad en nube**: no hay nada que promover.

| Instancia | Rol | Comportamiento |
|---|---|---|
| Keycloak IdP maestro (nube) | Autoridad única, todas las escrituras | Integración LDAP/SCIM con el directorio corporativo del CLIENTE por VPN saliente; MFA para todo acceso externo |
| Caché local Talca (A-05, VM-05) | Solo lectura, TTL 8 h | Validación local de firma y emisión de sesiones sin conexión; sostiene 24 h de centro de distribución y 14 h de terreno |
| Caché local Concepción (VM-C03) | Solo lectura, TTL 8 h | Ídem para el centro de distribución de borde |

**Sincronización sin conexiones entrantes:** el maestro publica el Realm cifrado a S3 y las cachés lo importan (INT-13, saliente). Las altas, bajas y roles se propagan **desde el maestro hacia las cachés, nunca a la inversa**. Revocación: Δ ≤ 8 h por TTL y < 24 h por SCIM; para identidades de alta sensibilidad la baja se refuerza con el bloqueo del terminal por MDM.

#### 4.2 Federación, SSO y factores (Art. 22)

- **OpenID Connect y OAuth 2.1**, con SAML 2.0 disponible si la integración con el CLIENTE lo requiere; integración con el directorio corporativo por LDAP.
- **Inicio de sesión único** para todos los módulos y **cierre de sesión propagado** (*back-channel logout*).
- **MFA obligatoria** para administradores, accesos privilegiados y **todo acceso desde fuera de la red corporativa**.
- **Factores resistentes a la suplantación:** **FIDO2/WebAuthn (claves de acceso)** disponible y preferente para perfiles administradores, además de TOTP (RT-12.04, deseable, se supera el mínimo).
- **Acceso de conductores externos:** **OTP de un solo uso por operación**, sin cuenta corporativa (RF-06.08). Es la respuesta al hecho de que ~160 conductores no son trabajadores de la compañía y rotan sin aviso.

#### 4.3 Autorización: RBAC más ABAC (RT-12.05)

| Capa de control | Definición |
|---|---|
| **RBAC** | Roles derivados de los **11 actores canónicos** del modelo lógico. Los permisos viven en Keycloak. |
| **ABAC** | Atributos de contexto que acotan el rol: **instalación asignada**, **horario de turno** (el despacho solo es válido en su ventana), **dispositivo provisto** y enrolado por MDM. Las políticas se aplican en la Capa 4. |
| **Segregación de funciones (RT-12.06)** | Conciliación ≠ aprobación (M10); detección de excursión térmica ≠ decisión de bloqueo (M9); rendición ≠ cierre contable (M7). **Nadie que genera un control lo ejecuta.** La matriz completa se declara en el registro de requerimientos (Cap. 17.1). |
| **Aislamiento de externos (RT-12.11)** | Cada proveedor ve solo sus órdenes de compra y documentos; cada transportista solo sus rutas asignadas. No hay visibilidad cruzada. |

#### 4.4 Política de sesión (Art. 22 · RT-12.07/12.12)

| Parámetro | Valor declarado |
|---|---|
| `id_token` | 1 h |
| `access_token` | **30 min** (valor prevalente, D-AL-07) |
| `refresh_token` | 30 días, **rotativo con familia y detección de reúso**: cada uso emite uno nuevo e invalida el anterior; un reúso detectado fuerza reautenticación |
| **Token sin conexión — bodega** | TTL **8 h** (turno nocturno de preparación, RNF-13.01) |
| **Token sin conexión — terreno** | TTL **14 h** (turno completo de reparto y jornada de preventa, RNF-06.02) |
| Renovación del token sin conexión | Al inicio de turno **con cobertura**, o contra la caché local A-05 en el centro de distribución. La ventana sin conexión cubre siempre el turno completo aunque el dispositivo no vuelva a ver señal |
| Caducidad por inactividad | 30 min en consolas de bodega y back-office; 60 min en superficies de solo lectura (BI) |
| Sesiones concurrentes | **Una sesión activa por actor de terreno**; se deniega el inicio concurrente del mismo preventista o conductor en otro dispositivo, con opción de invalidar la anterior |
| Identificador de sesión en la URL | **Prohibido** (Art. 22): el token viaja en cabecera, nunca en la ruta |
| Cierre global de sesión | Botón de administración para contingencia de dispositivo perdido o comprometido |
| Elevación temporal (JIT) | Máximo 2 h, con justificación, aprobación de un segundo perfil y **registro auditado** |

> **Discrepancia resuelta (2026-09-06):** se concilió el valor del `access_token`. Prevalece **30 min** y es el valor único de la propuesta, declarado en la sección de Arquitectura de Seguridad de este documento (§4, ADR-06).

#### 4.5 Autenticación en el perfil operacional de terreno (RT-12.11/12.10 — Según caso)

El caso fija condiciones que descartan la contraseña como mecanismo de terreno: **guantes térmicos a −22 °C**, uso **a una mano** durante la descarga, uso **de pie y a la intemperie** en la puerta del local, **dispositivos compartidos entre turnos** en bodega y **38 % de rotación anual** en preparación. La respuesta declarada:

- El operador autentica **con conexión al inicio de turno** (PIN de 6 dígitos o biometría del dispositivo) y descarga un token cifrado de vida acotada al turno.
- Durante el turno el **PIN desbloquea el token local**; no autentica contra el IdP por transacción. No hay dependencia de red en la ruta.
- El dispositivo es un **factor de posesión** enrolado por MDM; el PIN es el segundo factor. Esto satisface la MFA del Art. 22 sin exigir un segundo dispositivo a alguien que trabaja con guantes.
- Los datos locales están cifrados y admiten **borrado remoto selectivo** (RF-03.16/06.12): se borra la aplicación y su caché, no la información personal del dispositivo.

#### 4.6 Gestión de dispositivos (MDM — RT-03.18)

| Capacidad | Alcance |
|---|---|
| Enrolamiento | Alta del dispositivo contra el usuario antes del turno; perfil por rol (preventista, preparador, conductor) |
| Configuración | Cifrado local obligatorio, PIN obligatorio, bloqueo de pantalla, modo quiosco (aplicación única), actualización de aplicación y de caché de turno |
| Postura y monitoreo | Estado de sincronización, batería, versión de aplicación; alertas por dispositivo perdido, almacenamiento bajo o fallo recurrente de sincronización |
| Seguridad | Borrado remoto selectivo con revocación de tokens |
| Inventario | Registro por IMEI/serie, asignación y estado |
| Operación | MDM **como servicio gestionado** (Android Enterprise o equivalente): el equipo de TI del CLIENTE es de 4 personas y no administra la plataforma localmente |

#### 4.7 Ciclo de vida de la identidad (RT-12.09 · RT-15.05)

- **Aprovisionamiento ≤ 24 h** desde el alta en recursos humanos o en el proveedor: cuenta, permisos por rol canónico y dispositivo enrolado.
- **Baja efectiva en ≤ 24 h** desde la desvinculación (Art. 22): revocación de tokens, borrado remoto del dispositivo y revocación de accesos externos.
- Flujo **desatendido y auditable**, con aprobación del jefe de área, bitácora de aprovisionamiento y **revisión semestral de accesos** (certificación de identidades).
- **Auditoría de identidad** con no repudio: creación, modificación, elevación y baja de cuentas, con retención declarada (§7).

#### 4.8 Accesos privilegiados y cuenta de emergencia (RT-12.06 · RT-12.13)

- **PAM con acceso a demanda:** sin acceso interactivo permanente a producción. La operación excepcional se hace *just-in-time* por AWS Systems Manager Session Manager, con MFA, aprobación y **sesión grabada** (RT-11.27).
- **Cuenta de emergencia (*break-glass*):** fuera de banda, custodiada en bóveda física con doble firma, para contingencia de indisponibilidad del IdP. Su activación exige procedimiento escrito, **notificación inmediata a TI y a la gerencia**, registro en cadena de custodia y **rotación de credenciales tras el uso**. Se prueba **dos veces al año** junto con el simulacro de recuperación ante desastres.

### 5. Cifrado y gestión de claves (Art. 21.2 · RT-11.08/11.09/11.10)

#### 5.1 En tránsito

| Trayecto | Protección |
|---|---|
| Superficies públicas y portales | TLS 1.3 con HSTS y precarga; TLS 1.0/1.1 deshabilitados |
| Servicio a servicio | **mTLS** (microsegmentación; sin confianza implícita en la red interna) |
| On-premise ↔ nube | **IPsec/IKEv2 con AES-256-GCM**, BGP, MTU 1436, dos túneles |
| Borde IoT → nube | **MQTTS 8883** con certificado **X.509 por dispositivo** |
| Respaldos y replicación | TLS 1.3 en tránsito (RT-07.10) |

#### 5.2 En reposo

| Elemento | Cifrado | Gestión de claves |
|---|---|---|
| Almacenamiento del clúster (OSD Ceph / RAID 10) | LUKS/dm-crypt o NVMe con autocifrado | CMK dedicada on-premise (o HSM de borde), custodiada y respaldada |
| NAS de respaldo D-05 | LUKS/SED | CMK **independiente** de la de producción (RT-07.10) |
| PostgreSQL on-premise | Cifrado del sistema de archivos subyacente | CMK dedicada |
| Aurora, DynamoDB, S3 | SSE-KMS | AWS KMS con CMK y rotación anual |
| Estaciones de trabajo | BitLocker/LUKS gestionado | Servidor de claves corporativo |
| Terminales de terreno | Cifrado del dispositivo (Android FBE) y aplicación en entorno aislado | MDM (§4.6) |

**Rotación y custodia:** claves de datos con rotación anual o ante revocación o compromiso; claves maestras según el calendario del proveedor; rotación en línea, **sin degradación del servicio**. Los respaldos conservan la versión de clave necesaria para una restauración auditable. **Separación de funciones en la custodia de claves** (Art. 21.2): quien administra la plataforma no administra las claves maestras.

#### 5.3 Cifrado a nivel de campo (RT-11.10 — Según caso)

El caso lo declara exigible para cuatro conjuntos de datos. Aplicación declarada:

| Dato sensible | Tratamiento |
|---|---|
| **Comportamiento de pago y antecedentes comerciales del cliente** | Cifrado a nivel de campo con clave en KMS; acceso restringido por rol y **registro de consultas** (RT-16.09) |
| **Datos de geolocalización de personas** | Cifrado a nivel de campo, retención **12 meses** y registro de consultas. La visibilidad de flota es operativa y **no se desliza a control de jornada** (D1, objeción sindical L577) |
| **Medios de pago electrónicos** | El PAN **no se almacena**: tokenización en la pasarela; el terminal POS es PCI PTS 7.x |
| **RUT de clientes en bases y registros** | Pseudonimización mediante cifrado a nivel de campo (`pgcrypto` con clave en KMS) |

**Gestión de secretos.** Los secretos de integración (credenciales del ERP, certificados AS2/EDI, credenciales del SII y de Transbank) se administran en **AWS Secrets Manager y SSM Parameter Store**, con **rotación automática** y consumo desde los nodos on-premise por VPC Endpoint **saliente**, coherente con el principio 4. Prohibición absoluta de secretos embebidos en código, imágenes o archivos de configuración (Art. 21.4).

> **SEC-01 — resuelta y aplicada (2026-09-06).** Se adoptó la alternativa (A): **Secrets Manager + SSM Parameter Store**, formalizada en **ADR-15** y en la **D13** de la arquitectura lógica (Subdoc. 4.1), y aplicada en este documento (sección de Arquitectura de Seguridad, §5.3; emplazamiento N-12). El texto original de la decisión se conserva a continuación como fundamento.
>
> *(Planteamiento original.)* La arquitectura lógica declaraba **HashiCorp Vault on-premise** como gestor de secretos de la Capa 7, pero Vault **no tiene emplazamiento físico** en este Subdocumento: no figura en el dimensionamiento on-premise ni en el inventario físico. Alternativas evaluadas: **(A)** eliminar Vault y usar Secrets Manager/SSM con consumo saliente —menor superficie, servicio administrado (Art. 16.3), sin carga para un equipo de 4 personas, sin nueva máquina virtual ni licencia—; **(B)** incorporar una máquina virtual Vault en Talca con su alta disponibilidad, respaldo, sellado y costo, y declararla en el inventario y el dimensionamiento. **Este documento adopta la alternativa (A)** (ADR-15). Si se prefiere (B), debe incorporarse el componente a la arquitectura física y al dimensionamiento. **No es admisible dejarlo como está**: un componente de seguridad sin emplazamiento incumple el Art. 16.2.

### 6. Clasificación de la información y controles por nivel (RT-11.03)

| Nivel | Ejemplos en Puelche | Controles mínimos |
|---|---|---|
| **Restringido** | Claves KMS/HSM, credenciales de servicio, firma privada de DTE, claves de respaldo | PAM (§4.8), *break-glass* (§4.8), KMS/HSM, cifrado a nivel de campo |
| **Confidencial** | Base del WMS (inventario, clientes, trazabilidad de lote), evidencia de entrega, tokens, auditoría, antecedentes comerciales, geolocalización de personas | Cifrado en reposo, TLS 1.3, RBAC más ABAC, registro de consultas (RT-16.09) |
| **Interno** | Registros de operación, métricas, configuraciones | Acceso por rol y retención declarada |
| **Público** | Catálogo público de productos sin precios (RT-16.30) | Sin controles de confidencialidad; sí integridad y disponibilidad |

### 7. Detección, respuesta y evidencia (Art. 21.3 · RT-11.14 a RT-11.21)

| Control | Implementación |
|---|---|
| **Registro centralizado e inalterable** | Todos los eventos de seguridad (autenticación, cambios de configuración, accesos, EDR, firewall, DCIM) se centralizan con ingesta continua. Inalterabilidad por sellado en modo solo-anexado y S3 Object Lock: **ni un administrador modifica un evento sellado** |
| **Retención de eventos de seguridad** | **12 meses en línea + 24 meses en archivo recuperable** (36 meses en total), por sobre el mínimo del Art. 21.3 y de RT-11.14 |
| **Auditoría de negocio** | 7 años en `audit_log` (eventos de EventBridge), con no repudio |
| **SIEM con casos de uso del negocio** | Security Lake con **6 casos de uso propios de la operación logística**: alerta nocturna fuera de patrón, acceso remoto anómalo, MFA en TI en la sombra, exfiltración de datos de stock, escalada de privilegios y respuesta a incidente reglamentario. No son casos genéricos de infraestructura (Art. 21.3) |
| **EDR en nube y on-premise** | Agentes en todos los nodos on-premise, estaciones y cargas en nube, con consola centralizada integrada al SIEM |
| **SOC 24×7** | Cobertura contractual de ambos dominios con dotación mínima declarada (un analista de primer nivel por turno más segundo nivel de guardia) y catálogo de procedimientos |
| **Gestión de vulnerabilidades** | Plazos contractuales: **crítica 7 días** (CVSS ≥ 9,0 o explotación activa), **alta 15 días** (7,0–8,9), **media 30 días** (4,0–6,9). Escaneo automatizado semanal, escaneo externo trimestral y **verificación de corrección** por reexploración; trazabilidad reportada trimestralmente al CLIENTE |
| **Respuesta a incidentes** | Plan con fases, roles, clasificación y escalamiento; **comunicación al CLIENTE en ≤ 2 h** desde la detección de un incidente de severidad crítica |
| **Notificación de brechas** | Notificación al CLIENTE en **≤ 24 h** desde la detección con informe preliminar, y análisis de causa raíz dentro de los **5 días hábiles** siguientes |
| **Pruebas de intrusión** | **Anuales por un tercero independiente** del adjudicatario y **previas a cada paso a producción**, con entrega íntegra del informe y plan de remediación con plazos |
| **Simulacros con el CLIENTE** | Ejercicios de incidente conjuntos, coordinados con el simulacro semestral de recuperación ante desastres (Art. 20) |

### 8. Modelado de amenazas STRIDE (Art. 21.1 · RT-11.02)

Cada componente y cada integración externa modela sus amenazas antes de implementarse.

| Componente o integración | Amenazas STRIDE relevantes | Mitigación diseñada | Verificación |
|---|---|---|---|
| Apps de terreno (Kotlin, sin conexión) | Suplantación de usuario o dispositivo · alteración de datos locales · repudio de operaciones · denegación por buffer sin control | PIN o biometría más MDM (§4.6); cifrado local y buffer de escrituras inmutable; buffer acotado con monitoreo | Pruebas de seguridad de aplicación y revisión semestral |
| Puerta de enlace (API Gateway) | Suplantación de llamadas · denegación de servicio | OIDC con PKCE, límites de tasa, WAF y CDN en el borde, limitación exponencial | Pruebas de carga y abuso en marcha blanca |
| API de negocio (Django, M1–M12) | Suplantación · alteración · divulgación · elevación de privilegios | OAuth 2.1 y mTLS, ORM con validación de entrada, RBAC más ABAC, cifrado de datos sensibles | SAST y DAST en el pipeline |
| Colas y eventos (RabbitMQ, SQS, EventBridge) | Alteración de mensajes · repudio | mTLS, firma de eventos, bitácora de reconciliación (Art. 16.4) | Pruebas de contrato y auditoría |
| Bases de datos (PostgreSQL, Aurora, Redshift, S3) | Divulgación · alteración | KMS y cifrado en reposo, política de retención y eliminación, auditoría de acceso (RT-16.09) | Control de accesos y revisión de cifrado |
| ERP 2017, SII, Transbank, EDI/AS2 | Suplantación · alteración de datos intercambiados · repudio de transacciones | mTLS con certificados gestionados, capa anticorrupción, firmas y sumas de verificación en mensajes y exportaciones | Pruebas de falla por integración |
| Telemetría e IoT (Greengrass → DynamoDB) | Suplantación de sensores · alteración de lecturas | Certificado X.509 por dispositivo, borde autenticado, series inmutables | Rol de dispositivo y revisión periódica |
| Portales de la DMZ (N-01, N-02, N-03) | Suplantación de cliente externo · abuso automatizado · divulgación entre entidades | OIDC por rol, MFA y OTP, WAF con reglas propias, protección de bots, aislamiento estricto por entidad | Pentest previo a producción |
| Sala técnica y acceso físico | Acceso físico no autorizado · sustracción de medios | Cuatro capas de acceso, biometría facial, esclusa con antipassback, CCTV ≥ 30 días, custodia de medios | Auditoría física y bitácora |

### 9. Seguridad del ciclo de desarrollo (Art. 21.4 · RT-11.22 a RT-11.27)

| Control | Implementación |
|---|---|
| Análisis en el pipeline | SAST, análisis de composición de software, DAST y escaneo de imágenes de contenedor, con **bloqueo automático del despliegue** ante hallazgos críticos o altos |
| **SBOM por versión** | Inventario de componentes en **CycloneDX**, generado en el pipeline y **entregado al CLIENTE** junto con cada versión liberada |
| **Firma de artefactos y procedencia** | Imágenes OCI y SBOM firmados con Sigstore/cosign; construcción hermética con procedencia **SLSA nivel 3**, verificada antes de cada despliegue |
| Secretos | Prohibición absoluta de credenciales embebidas; gestor de secretos con rotación automática (§5.3) |
| Datos no productivos | Desarrollo, calidad y preproducción operan con **datos sintéticos** derivados de la volumetría del Cap. 14; las plantillas cercanas a producción pasan por anonimización o seudonimización verificable |
| Acceso a producción | **Sin acceso interactivo**: los despliegues son exclusivamente por pipeline; la excepción es *just-in-time* con MFA, aprobación y grabación de sesión |

### 10. Datos personales, residencia y transferencia internacional (Art. 23 · Ley 21.719)

| Materia | Declaración |
|---|---|
| **Residencia primaria** | Toda la operación productiva reside en **AWS sa-east-1 (São Paulo)**. El dominio on-premise reside en las instalaciones del CLIENTE en Chile |
| **Región secundaria** | **us-east-1 (Norte de Virginia, EE. UU.)**, exclusivamente como ambiente de recuperación ante desastres (quinto ambiente, RT-04.01) |
| **Transferencia internacional** | La replicación hacia us-east-1 (Aurora Global Database, DynamoDB Global Tables y S3 Cross-Region Replication) constituye una **transferencia internacional de datos personales** en el sentido de la Ley 21.719 y debe contar con base de licitud y resguardos, conforme exige el Art. 23 |
| **Resguardos declarados** | (a) Cifrado en reposo con **CMK gestionada por el CLIENTE** y en tránsito extremo a extremo; (b) acuerdo de tratamiento de datos con el proveedor de nube con cláusulas de transferencia; (c) **minimización**: la región secundaria no se usa para explotación analítica ni para consultas de negocio, solo para continuidad; (d) los datos de **geolocalización de personas** quedan **excluidos** de la replicación transfronteriza y se conservan solo en sa-east-1 con retención de 12 meses; (e) registro de la transferencia en el inventario de tratamientos |
| **Aprobación del CLIENTE** | La residencia y la transferencia quedan **sujetas a aprobación expresa del CLIENTE** (Art. 23). Si el CLIENTE no aprueba la transferencia a us-east-1, la alternativa declarada es la **continuidad intrarregional en sa-east-1** —entendida como **no salir de la región AWS sa-east-1 (São Paulo, Brasil)**, la única con los servicios requeridos; **AWS no posee región dentro de Chile**, por lo que esta alternativa **no es un segundo sitio geográfico ni usa los sitios on-premise del CLIENTE** (Talca/Concepción solo sostienen el dominio on-premise y su DRP local con RTO +1–2 h, ADR-09 §4)—: ampliación a la **tercera zona de disponibilidad** (sa-east-1a/1b/1c) más **respaldo inmutable regional** (S3 Object Lock / Backup Vault, esquema 3-2-1-1-0). Cubre **falla de zona de disponibilidad y corrupción de datos** (RTO ≤ 4 h / RPO ≤ 15 min), que es lo que ya provee el multi-AZ, pero **no una caída de toda la región sa-east-1**: en ese escenario la reconstrucción desde el respaldo inmutable toma **24–72 h**, incumpliendo RNF-20.06. Esta degradación es el impacto sobre el objetivo de recuperación, cuantificado en la **alternativa D del ADR-09** — y es la razón por la que el plan base solicita la aprobación del CLIENTE para us-east-1 con los resguardos del Art. 23 |
| **Retención por categoría** | Documentos tributarios y su respaldo: 6 años · trazabilidad sanitaria de lote: vida útil del producto más 6 meses, con mínimo de 5 años · registros de temperatura: 5 años · evidencia de entrega: 6 años · **geolocalización de personas: 12 meses** · eventos de seguridad: 12 meses en línea más 24 en archivo · auditoría de negocio: 7 años |
| **Eliminación segura** | Procedimiento verificable de eliminación al vencimiento, con registro inalterable; borrado seguro de medios que salen de servicio y disposición final con gestor autorizado |
| **Exportabilidad** | Capacidad de exportar la totalidad de la información del CLIENTE en formatos abiertos y documentados, en cualquier momento del contrato y sin costo adicional |
| **Derechos de los titulares (ARCOP)** | Acceso, rectificación, cancelación/supresión, oposición, portabilidad y bloqueo temporal; respuesta en **30 días corridos prorrogables 30**; canal único, verificación de identidad y registro de cada solicitud (§10.1) |
| **Base de licitud** | Resuelta por tratamiento en **§10.5** (Ley 21.719, Art. 12/13): geolocalización de trabajadores y POD por **ejecución del contrato de trabajo + interés legítimo del empleador** (no consentimiento, por desequilibrio; test de proporcionalidad documentado); clientes y crédito por **ejecución de contrato + interés legítimo**; DTE/RSA por **obligación legal**; conductores externos por **consentimiento del titular**; CCTV por **interés legítimo (seguridad)**; formalizada en el RAT (entregable) |
| **Política de privacidad / aviso al titular** | Aviso informativo para clientes y trabajadores (qué se trata, con qué fin, base de licitud, derechos y cómo ejercerlos); versión preliminar anexable al Informe 1 (§10.2) |
| **Evaluación de Impacto (EIPD)** | Obligatoria por tratamientos de alto riesgo (monitoreo sistemático de personas); entregable del proyecto con alcance preliminar (§10.3) y versión final antes de producción |

> **Nota (2026-09-06).** Este apartado **cierra el hallazgo D2 de la auditoría**: la arquitectura declaraba la región secundaria y su distancia, pero no la base de licitud ni los resguardos de la transferencia internacional que exige el Art. 23. Los resguardos **(c) minimización** y **(d) exclusión de la geolocalización de personas de la replicación transfronteriza** son decisiones de diseño adoptadas y **ya propagadas** a la sección de Arquitectura de Despliegue de este documento y a S14 de la arquitectura lógica v6.2. La decisión (d) tiene además un fundamento del caso: la geolocalización de personas es el dato con la objeción sindical explícita (L577) y con la retención más corta (12 meses); mantenerlo en una sola jurisdicción reduce la superficie legal sin afectar la continuidad, porque no es un dato necesario para reanudar la operación.

#### 10.1 Protocolo ARCOP — derechos de los titulares (Ley 21.719)

Declaración de cumplimiento de los derechos de los titulares sobre los datos personales tratados por la solución:

- **Derechos cubiertos:** acceso, rectificación, cancelación (supresión), oposición, portabilidad y bloqueo temporal. Instrumentación: acceso y portabilidad vía exportabilidad (§10, RT-05.06, formato abierto CSV/JSON con diccionario — lógica §10.8); rectificación y supresión vía ciclo de vida de datos (§10, RT-05.07/05.08) con trazabilidad de cada cambio; bloqueo temporal conforme a la ley en caso de impugnación del titular.
- **Canal único:** correo dedicado y formulario web con acuse de recibo, publicados en la política de privacidad (§10.2). Ningún otro canal inicia el plazo de respuesta.
- **Plazo:** respuesta en **30 días corridos, prorrogables una sola vez por 30 más**, con aviso al titular (Art. 11 de la Ley 21.719).
- **Verificación de identidad:** autenticación del titular o su representante (documento de identidad / poder), proporcional al riesgo del dato (reforzada para geolocalización y datos sensibles); registro de cada verificación.
- **Contraparte responsable (BA Art. 462):** el **Encargado de Seguridad de la Información** coordina la recepción y respuesta de solicitudes y su registro; es la contraparte única e identificable ante los titulares y ante el CLIENTE.
- **Registro:** bitácora de solicitudes ARCOP (qué derecho, quién, cuándo, resolución y plazo real), conservada conforme a la retención de auditoría (§10) y disponible para la Agencia de Protección de Datos Personales.

#### 10.2 Política de Privacidad — versión preliminar (aviso al titular, Ley 21.719)

Documento de referencia del aviso informativo a titulares (clientes y trabajadores); **versión preliminar anexable al Informe 1**:

1. **Responsable:** Distribuidora Puelche S.A. (CLIENTE), con el proponente como **encargado del tratamiento** (cláusulas de tratamiento de datos, BA). Residencia primaria: Chile y AWS sa-east-1.
2. **Datos tratados:** identificación y contacto de clientes (14.200 puntos, mayoría personas naturales); comportamiento de pago e historial crediticio del canal tradicional; datos laborales de trabajadores; **geolocalización** de preventistas (62) y conductores (~200) con **finalidad exclusivamente operativa** (rutas, verificación de entrega, costo de servir) — **sin control de jornada ni cámaras en cabina** (decisión D1; objeción sindical L577).
3. **Finalidades:** operación comercial y logística (preventa, reparto, facturación), trazabilidad sanitaria obligatoria (D.S. 977/96), seguridad de la información y continuidad (DR/DRP), cumplimiento normativo.
4. **Base de licitud:** por tratamiento, según la tabla de **§10.5** (Art. 12/13 de la Ley 21.719): geolocalización de trabajadores por **ejecución del contrato de trabajo e interés legítimo del empleador** (no consentimiento, por desequilibrio; test de proporcionalidad en §10.5); clientes por **ejecución de contrato e interés legítimo**; obligaciones legales (DTE, trazabilidad sanitaria) por **obligación legal**; conductores externos por **consentimiento del titular**. Donde aplique consentimiento, será expreso, informado, específico y **revocable**, con registro de la revocación.
5. **Destinatarios y transferencias:** AWS (encargado, ISO/IEC 27018) y subencargados declarados (BA 73.4); transferencia internacional a us-east-1 solo bajo los resguardos del Art. 23 (§10); **geolocalización de personas excluida de la replicación transfronteriza**.
6. **Retención y eliminación:** por categoría (§10): geolocalización 12 meses; trazabilidad sanitaria 5 años; documentos tributarios 6 años; eliminación certificada al término del contrato (Art. 85 BA).
7. **Derechos del titular:** acceso, rectificación, supresión, oposición, portabilidad y bloqueo temporal; cómo ejercerlos en §10.1 (canal dedicado, plazo 30 + 30 días).
8. **Seguridad:** medidas declaradas en este documento — cifrado a nivel de campo (RT-11.10), RBAC/ABAC, registro de consultas a datos sensibles (RT-16.09), Zero Trust (NIST SP 800-207).
9. **Brechas:** notificación al CLIENTE en **≤ 24 h** (RT-11.19); el CLIENTE, como responsable, cumple la notificación ante la Agencia de Protección de Datos Personales y los titulares afectados.
10. **Portales de canal moderno (N-01/N-02/N-03) y cookies:** no se instrumentan cookies de terceros ni analítica de seguimiento; en caso de solicitarse, se implementará un **banner de consentimiento de cookies** conforme a la Ley 21.719 y un aviso específico del portal.

#### 10.3 Evaluación de Impacto sobre Protección de Datos (EIPD) — alcance preliminar

- **Procedencia:** BA Art. 462 (evaluación de impacto "cuando corresponda") y Ley 21.719 (tratamientos de alto riesgo). El caso la gatilla: **tratamiento masivo de datos personales** (14.200 clientes) y **monitoreo sistemático de personas** (GPS de ~260 trabajadores).
- **Alcance (criterios):** finalidad, base de licitud, categorías (incluidas sensibles: geolocalización, comportamiento de pago), destinatarios, transferencias internacionales (us-east-1), retención por categoría, medidas de seguridad (§10) y riesgos para los titulares (vigilancia de trabajadores, acceso indebido a historial crediticio, exposición de geolocalización).
- **Tratamientos incluidos:** preventa/reparto (geolocalización); gestión de crédito y cobranza (comportamiento de pago); trazabilidad sanitaria lote→cliente (D.S. 977/96); POD (firma/foto); analítica y observabilidad con datos personales.
- **Resultado comprometido:** EIPD según metodología reconocida (p.ej. ISO/IEC 29134 / CNIL PIA): documento de riesgos y controles y veredicto de proporcionalidad; **versión final antes de la entrada en producción** y actualización ante cualquier cambio de tratamiento.
- **Entregable:** documento formal del proyecto, con **versión preliminar anexada al Informe 1** y revisión anual durante la operación.

#### 10.4 Vigencia y seguimiento normativo

La Ley 21.719 entra en vigencia el **01-dic-2026** (Diario Oficial 13-dic-2024; vacancia de 2 años). El 31-ago-2026 el Gobierno ingresó el **Boletín N° 18.623-07** (Mensaje N° 110-374, urgencia 01-sep-2026), que **postergaría su entrada en vigencia al 01-dic-2027**, aumenta a 5 los consejeros de la Agencia y amplía la primera amonestación a todos los responsables. Al cierre de esta versión **es proyecto de ley, aún no publicado**: mientras tanto rige el calendario 01-dic-2026. La propuesta es **robusta a ambas fechas** por diseño: se alinea contra el articulado completo ya publicado y la operación (contrato de 56 meses) cae dentro del régimen cualquiera sea la fecha; ninguno de los controles de este §10 depende de la fecha de vigencia.

#### 10.5 Base de licitud por tratamiento (Ley 21.719, Art. 12 y 13)

Cierre de la decisión de base de licitud. La regla general de la ley es el consentimiento (Art. 12), salvo que concurra alguna de las bases distintas al consentimiento (Art. 13): ejecución de contrato, obligación legal, interés vital o interés legítimo del responsable. Cada tratamiento del caso declara su base, su fundamento y sus garantías:

| Tratamiento | Datos | Base de licitud | Fundamento y garantías |
|---|---|---|---|
| Geolocalización de trabajadores (62 preventistas + ~200 conductores) | geolocalización (tratada como sensible por RT-11.10) | **Ejecución del contrato de trabajo + interés legítimo del empleador** (Art. 13) | No se usa consentimiento por desequilibrio empleador–trabajador. Minimización (D1): finalidad exclusivamente operativa, **sin control de jornada ni cámaras en cabina** (objeción sindical L577), retención 12 meses, cifrado a nivel de campo (RT-11.10), registro de consultas (RT-16.09), **excluida de la réplica transfronteriza** (§10). Test de proporcionalidad documentado e información previa a los trabajadores (aviso §10.2) |
| Comportamiento de pago e historial crediticio (canal tradicional) | financieros/comerciales | **Ejecución de contrato (venta a crédito) + interés legítimo (gestión de riesgo crediticio)** (Art. 13) | Datos derivados de la relación comercial (Decisión 16.1 N° 8/9); no requieren consentimiento para la operación de crédito; cifrado a nivel de campo y acceso restringido a crédito/cobranza (RBAC/ABAC) |
| Datos laborales de trabajadores (RUT, cuenta, perfil) | recursos humanos | **Cumplimiento de obligación legal + ejecución del contrato de trabajo** | Cláusula de protección de datos en contratos de trabajo (Art. 154 bis Código del Trabajo); acceso restringido a RRHH; retención según la ley |
| Clientes — identificación y contacto (preventa, DTE, portal canal moderno) | básicos de identificación | **Ejecución de contrato + cumplimiento de obligación legal** (DTE/SII) | Necesarios a la preventa, facturación y autoservicio; no se usan para marketing sin consentimiento del titular |
| POD — firma/foto de entrega | imagen/firma | **Ejecución de contrato (evidencia de entrega)** (Art. 13) | Retención 6 años; acceso acotado a operación y reclamos; minimización (un solo fin) |
| Conductores externos (~160, personal de terceros) | identificación, OTP, geolocalización si aplica | **Consentimiento del titular** vinculado a la relación contractual con la empresa de transporte (Art. 12) | Personal que **no es trabajador del CLIENTE**; datos mínimos y OTP sin cuenta corporativa (RF-06.08); los terminales TC58e son del parque único; borrado al término de la operación (Art. 85 BA) |
| Videovigilancia on-premise (CCTV, §12 y Sala §4.3) | imágenes | **Interés legítimo (seguridad de las instalaciones) + obligación de seguridad física RT-06.24** | Aviso de videovigilancia a personal y visitantes en el sitio; retención ≥ 30 días; acceso restringido y auditado |

Garantías transversales de esta tabla:
- **RAT (registro de actividades de tratamiento):** entregable del proyecto; cada fila se formaliza con finalidad, categorías, plazos, destinatarios y medidas (§10, control ISO 5.31/5.34).
- **Sensibilidad:** geolocalización y comportamiento de pago se tratan como categorías sensibles que el caso identifica (RT-05.08/RT-11.10), con cifrado de campo y registro de consultas; la geolocalización se apoya en la **excepción laboral/contractual** de la ley, no en un consentimiento general.
- **Consentimiento donde aplique** (uso no contractual de clientes, conductores externos): expreso, informado, específico y **revocable**, con registro de la revocación.
- **Menores de edad:** la solución no trata datos de NNA; si un cliente resultara menor de 14 años, el consentimiento corresponderá a padres o representantes, y entre 14 y 18 al titular con asistencia, conforme la ley.
- **Ciclo de vida:** eliminación certificada al término del contrato (Art. 85 BA) y retención por categoría (§10).

### 11. Matriz de controles ISO/IEC 27001:2022 (RT-11.05)

Referencia única de controles para toda la solución, nube y on-premise. El Dimensionamiento on-premise v05 §8.4 se apoya en esta matriz.

| Control (Anexo A) | Aplicación en Puelche | Evidencia |
|---|---|---|
| 5.7 Inteligencia de amenazas | Casos de uso del SIEM alimentados con contexto del sector logístico | Catálogo de detecciones |
| 5.15 Control de acceso | RBAC más ABAC sobre los 11 actores canónicos (§4.3) | Políticas de Keycloak y de la Capa 4 |
| 5.16 Gestión de acceso privilegiado | PAM *just-in-time* y *break-glass* (§4.8) | Procedimiento escrito y sesiones grabadas |
| 5.17 / 5.18 Autenticación y gestión de identidades | OIDC, OAuth 2.1, MFA, aprovisionamiento y baja ≤ 24 h (§4.7) | Keycloak y MDM |
| 5.19 / 5.20 Relaciones con proveedores | OTP para conductores externos, aislamiento por proveedor (§4.3) | Contratos y mecanismo OTP |
| 5.23 / 5.24 Seguridad en la nube y gestión de incidentes | Multi-AZ, GuardDuty, WAF, IAM, KMS, IaC; plan de respuesta (§7) | Configuración de cuentas y plan de incidentes |
| 5.31 / 5.34 Cumplimiento legal y privacidad | Ley 21.719, Ley 19.799, residencia y transferencia (§10) | Inventario de tratamientos, protocolo ARCOP y política de privacidad (§10.1–10.2) |
| 6.8 Notificación de eventos de seguridad | Canal declarado y plazos de 2 h y 24 h (§7) | Registro de notificaciones |
| 7.10 / 7.11 Respaldo y capacidad | Aurora con PITR de 35 días, WAL on-premise, CDC; RPO 15 min y RTO 4 h | Simulacro semestral (Art. 20) |
| 7.12 / 8.8 Redes y vulnerabilidades | Microsegmentación con mTLS, parches por Ansible, escaneo semanal (§7) | Plan de parches e informes de escaneo |
| 8.5 Autenticación segura | MFA, FIDO2 para administradores, PIN más posesión en terreno (§4.2, §4.5) | Configuración del IdP |
| 8.10 Eliminación de la información | Retención y eliminación certificada por categoría (§10) | Registro inalterable |
| 8.11 Enmascaramiento de datos | Cifrado a nivel de campo de geolocalización y antecedentes comerciales (§5.3) | Inventario de campos cifrados |
| 8.15 / 8.16 Registro, monitoreo y SIEM | Registros inalterables y alertas por síntomas de negocio (§7) | Capa 8 y correlación por `transaction_id` |
| 8.17 Sincronización de relojes | NTP en borde, on-premise y nube | Configuración y verificación |
| 8.23 Auditoría de registros | Revisión periódica por el Encargado de Seguridad (RT-16.09) | Procedimiento de auditoría |
| 8.25 / 8.28 Desarrollo seguro y codificación segura | SAST, DAST, SCA, SBOM, SLSA 3 (§9) | Pipeline y repositorio |
| 8.31 Separación de ambientes | Cinco cuentas AWS aisladas con SCP (RT-04.01) | Organización de cuentas |

### 12. Seguridad física (BTT Cap. 6)

La seguridad física del sitio primario se declara en la sección de Arquitectura de Seguridad de este documento (§12). Resumen de lo que sostiene esta arquitectura:

- **Cuatro capas de acceso** hasta la sala blanca, con biometría facial (AFIS de respaldo) y esclusa con antipassback; acceso **de a una persona** con reverificación (RT-06.23).
- **CCTV IP con retención ≥ 30 días** y respaldo en medio secundario auditable, cubriendo cada puerta controlada (RT-06.24).
- **Recinto de custodia de medios** de 10 m² con condiciones ambientales declaradas, e inventario con rotación y registro de todo movimiento (RT-06.26 a RT-06.28).
- **Acceso de terceros** (fabricantes, mantenedores, auditores) con acompañamiento obligatorio y registro (RT-06.25).
- **Control de dispositivos extraíbles** en los nodos on-premise y **borrado seguro verificable** de los medios que salen de servicio.

### 13. Referencias cruzadas con las decisiones de arquitectura

| ADR | Aporte a la vista de seguridad |
|---|---|
| ADR-03 | Modelo híbrido: define qué queda expuesto y qué no; el on-premise no publica servicios |
| ADR-06 | Identidad híbrida Modelo B: autoridad única en nube y cachés de solo lectura; el DRP de identidad no requiere conmutación |
| ADR-07 | Movilidad nativa Android: habilita cifrado local, MDM y borrado remoto selectivo en el parque de terreno |
| ADR-09 | Recuperación ante desastres multi-región: origina la materia de transferencia internacional del §10 |
| ADR-11 | Hub EDI con capa anticorrupción: ninguna cadena externa alcanza el ERP |
| **ADR-13** | Puerta de enlace Amazon API Gateway: concentra autenticación OIDC, cuotas, límites de tasa, validación de esquema e inspección de carga útil (Art. 21.2) en un único punto administrado |
| **ADR-14** | Observabilidad de plataforma única: sostiene la detección y la evidencia del §7 sin operar una segunda plataforma on-premise |
| **ADR-15** | Gestión de secretos en servicio administrado (SEC-01, §5.3) — **adoptada y propagada** el 2026-09-06 |

### 14. Trazabilidad normativa (resumen)

| Requisito | Cómo se cumple |
|---|---|
| BA Art. 21.1 | Zero Trust NIST SP 800-207 (§2); STRIDE por componente e integración (§8); clasificación de la información (§6); plazos de remediación 7/15/30 días (§7) |
| BA Art. 21.2 | Capa expuesta con CDN, WAF y Shield; TLS 1.3 con HSTS; cifrado en reposo con KMS y separación de funciones; puerta de enlace con cuotas, esquema y carga útil; protección de bots (§3, §5) |
| BA Art. 21.3 | Registro centralizado e inalterable con 12 + 24 meses; SIEM con casos de uso del negocio; EDR en ambos dominios; respuesta en 2 h; brechas en 24 h; pentest anual y previo a producción (§7) |
| BA Art. 21.4 | SAST, DAST, SCA y escaneo de imágenes con bloqueo; SBOM CycloneDX; SLSA 3; sin secretos embebidos; sin datos productivos en ambientes no productivos (§9) |
| BA Art. 22 | Identidad centralizada con OIDC/OAuth 2.1 y LDAP; SSO con cierre propagado; MFA; FIDO2; RBAC y ABAC con segregación de funciones; PAM; política de sesión completa; auditoría de identidad; baja ≤ 24 h; perfil operacional de terreno (§4) |
| BA Art. 23 | Residencia declarada, transferencia internacional con base de licitud y resguardos, retención por categoría, eliminación segura y exportabilidad (§10) |
| RT-11.02 | Modelado STRIDE por componente e integración (§8) |
| RT-11.03 | Clasificación en cuatro niveles con controles diferenciados (§6) |
| RT-11.04 | Programa de vulnerabilidades con plazos y verificación de corrección (§7) |
| RT-11.05 | Matriz de controles ISO/IEC 27001:2022 (§11) |
| RT-11.08 / RT-11.09 | TLS 1.3 con gestión de certificados; cifrado en reposo con KMS y rotación (§5) |
| RT-11.10 | Cifrado a nivel de campo para los cuatro conjuntos que fija el Cap. 15 del caso (§5.3) |
| RT-11.11 | Puerta de enlace con autenticación, cuotas, límites, esquema e inspección de carga útil (§3) |
| RT-11.13 | Superficie de exposición completa por zona y sitio (§3.1) |
| RT-11.14 / RT-11.15 / RT-11.17 | Eventos inalterables con retención; SIEM; SOC 24×7 (§7) |
| RT-11.18 / RT-11.19 / RT-11.20 / RT-11.21 | Plan de respuesta, notificación de brechas, pentest independiente y simulacros con el CLIENTE (§7) |
| RT-11.22 a RT-11.27 | Seguridad del ciclo de desarrollo (§9) |
| RT-12.01 a RT-12.13 | Identidad, acceso y sesiones completos (§4) |
| RT-03.15 | Endurecimiento CIS con gestión centralizada de parches (§7, F-02) |
| RT-03.18 | MDM de dispositivos de borde y terreno (§4.6) |
| RT-03.22 | Acceso remoto con confianza cero y verificación de postura; sin servicios internos expuestos (§2.2, §3.1) |
| RT-16.07 / RT-16.09 | Registro inalterable y registro de consultas a información sensible (§5.3, §7) |
| Caso Cap. 15 (RT-11.10, RT-12.11, RT-12.12, RT-16.09) | Cifrado a nivel de campo (§5.3); autenticación con guantes, a una mano y en dispositivos compartidos (§4.5); usuarios externos (§4.2, §4.3); registro de consultas (§5.3) |
| Caso Cap. 17.4, puntos 3 y 9 | Operación de un turno completo sin señal con autenticación local (§4.1, §4.5); incorporación de conductores de terceros con OTP y sin cuenta corporativa (§4.2) |

---

## Arquitectura de Despliegue

> **Apartado 5 del Subdocumento 4 (T-22) — Arquitectura de despliegue: ambientes, redes, alta disponibilidad, recuperación ante desastres y respaldos.** Marco: BA Art. 16 (híbrido) · Art. 20 (DR) · Art. 21–22 (seguridad) · BTT RT-03.xx / RT-04.xx / RT-07.07 / RT-10.01. Corresponde a la vista de despliegue (ISO/IEC/IEEE 42010, RT-02.03) de la arquitectura híbrida y es autocontenido: consolida los valores declarados en las secciones de este mismo Subdocumento 4.2.

### 1. Ambientes de despliegue (RT-04.01)

Los cinco ambientes obligatorios del numeral 4.1 de las Bases Técnicas Transversales están habilitados como **condición del hito H3** (RT-04.01), aislados entre sí mediante **cuentas AWS separadas** bajo una organización centralizada de AWS Control Tower (aislamiento estricto + SCP):

| Ambiente | Cuenta AWS | VPC | Región | Uso |
|---|---|---|---|---|
| Desarrollo | Cuenta 1 | `10.104.0.0/16` | sa-east-1 | Integración continua, pruebas unitarias automáticas |
| Calidad (QA) | Cuenta 2 | `10.103.0.0/16` | sa-east-1 | Pruebas funcionales, estáticas, DAST/SAST |
| Pre-Producción | Cuenta 3 | `10.102.0.0/16` | sa-east-1 | Marcha blanca, pruebas de aceptación y de carga |
| Producción | Cuenta 4 | `10.101.0.0/16` | sa-east-1 | Operación real (Multi-AZ) |
| Recuperación ante Desastres | Cuenta 5 | `10.201.0.0/16` | us-east-1 | 5.º ambiente obligatorio (RT-04.01) |

Reglas que gobiernan el modelo de ambientes:

- **Paridad Pre-Producción = Producción (RT-04.02):** topología, versiones de componentes y configuración equivalentes; las diferencias por costo se declaran y justifican una a una.
- **On-premise como producción (RT-04.01/RT-03.10):** el despliegue on-premise es **producción** con la imagen única `wms_only`; esa misma imagen recorre Dev→QA→PreProd en la nube antes del cutover en Talca (ventana de 24 h) y en Concepción. **No se mantienen ambientes on-premise separados** — la paridad la garantizan la imagen única y el IaC versionado (RT-03.03).
- **Entrega continua (RT-04.05):** el pipeline CI ejecuta compilación, pruebas unitarias, análisis estático, análisis de composición, escaneo de secretos y escaneo de imágenes de contenedor, con **bloqueo automático del despliegue** ante hallazgos críticos o altos (RT-11.22).
- **Despliegue sin interrupción (RT-04.07):** estrategia **azul-verde** con canario en etapas, demostrada en PreProducción antes de cada paso a producción; reversión automatizada (RT-04.06).
- **Configuración externalizada (RT-04.08):** un mismo artefacto se promueve QA→PreProd→Prod sin recompilación; los secretos viven en gestor de secretos con rotación automática (RT-04.09), sin credenciales embebidas.
- **Datos no productivos (RT-11.25):** Dev, QA y PreProd usan **datos sintéticos** generados desde la volumetría del Cap. 14 del caso; las plantillas próximas a producción pasan por anonimización/seudonimización verificable (Amazon Macie).
- **Sin acceso interactivo a producción (RT-11.27):** los despliegues son exclusivamente por pipeline; el acceso administrativo excepcional es **just-in-time** vía AWS Systems Manager Session Manager con MFA, aprobación y sesión grabada.
- **Reducción de ambientes no productivos fuera de horario (RT-04.13):** Dev/QA/PreProd se apagan o reducen fuera del horario de uso, con el ahorro reflejado en la estructura de costos.
- **Portal web (N-01/N-02/N-03):** la SPA Angular se publica **por ambiente** en S3+CloudFront (bucket y distribución por cuenta AWS) y su backend es la misma imagen Django del ambiente; entra a producción con el **hito de enero 2029** (RNF-12.01).

### 2. Redes (topología, segmentación y conectividad)

#### 2.1 WAN — tri-camino con SD-WAN (RT-03.17)

Cada instalación dispone de **caminos físicamente independientes** con **conmutación automática en < 30 s** (el requisito exige ≤ 5 min declarados; el diseño opera en < 30 s):

| Camino | Sitios | Rol |
|---|---|---|
| Fibra (D-03) | Talca, Concepción | Enlace principal en los 2 CD |
| Starlink Enterprise LEO (D-06) | 3 cross-docks (Curicó, Chillán, Los Ángeles) + respaldo en los 2 CD | Principal en cross-docks (cubre Los Ángeles 03:00–05:00 sin torres 4G); respaldo automático en CDs |
| LTE dual 4G Cat-12 (D-04) | Todos | 2 proveedores móviles distintos; tercer camino independiente |
| **AWS Direct Connect** (complemento activable, D-AL-20) | Talca | **Camino dedicado opcional**, terminado en el par de firewall D-01 mediante un VIF dedicado o alojado sobre la fibra D-03, **sin hardware adicional**. **No reemplaza** los tres caminos SD-WAN: aporta capacidad dedicada para la réplica DMS CDC, la telemetría y los sincronismos por lote. Mientras el CLIENTE no lo contrate, **la VPN IPsec sostiene por sí sola** el RPO ≤ 15 min, el RTO ≤ 4 h y el SLA ≥ 99,9 % |

SD-WAN con políticas centralizadas y BGP; los cross-docks salen **directo por Starlink a SQS/IoT/SSM** (configuración crítica) y sincronizan detalle a Talca por AMQPS entre brokers (C-13). La pérdida total del enlace se cubre con la **autonomía local 24 h** (CD) / **14 h** (terreno) — RT-03.10, RNF-13.01.

#### 2.2 VPN Site-to-Site (costura C1)

- Extremos: **D-01 Firewall/UTM (HA activo-pasivo) → Customer Gateway** en cada CD; extremo cloud **VGW** del VPC Hub.
- Protocolo: **IPsec/IKEv2, AES-256-GCM, BGP, MTU 1436**; 2 túneles (activo + standby). Conmutación < 30 s sobre los tres caminos.

#### 2.3 Segmentación de red (sin solapamiento)

| Dominio | Bloque | Segmentación |
|---|---|---|
| Talca | `10.1.x.x` | VLAN 10 (MGT), 20 (SRV), 30 (OPS), 40 (WKS), 50 (IOT) |
| Concepción | `10.2.x.x` | Misma segmentación VLAN |
| Cross-dockings | `10.3.x.x – 10.5.x.x` | Red plana simplificada + salida SSM/IoT outbound |
| VPC Hub | `10.100.0.0/16` | Transit Gateway; adjuntos de VPN |
| VPC Producción | `10.101.0.0/16` | Multi-AZ: DMZ pública `10.101.1.0/24` (az1) y `10.101.2.0/24` (az2) — ALB/WAF/CloudFront origin/NAT GW y portales N-01/N-02/N-03 · subredes app y datos privadas |

Modelo **Hub-and-Spoke** con VPC de tránsito central: la comunicación cross-VPC pasa por el Transit Gateway (inspección) y los servicios AWS (S3, SQS, DynamoDB, KMS, SSM) se consumen por **VPC Endpoints/PrivateLink sin tráfico por internet** (RT-03.03).

#### 2.4 Zero Trust — flujos permitidos (BA Art. 21)

Todo el tráfico on-premise → nube es **outbound** (HTTPS/443, MQTTS/8883) sin conexiones entrantes salvo las dos excepciones controladas D-AL-05 sobre túnel IPsec autenticado:

| Flujo | Protocolo | Destino |
|---|---|---|
| Broker (shipper VM-03) → SQS FIFO | HTTPS 443 (VPC Endpoint SQS/PrivateLink) | AWS |
| Telemetría ADOT → CloudWatch/AMP | HTTPS 443 | AWS |
| Greengrass → IoT Core | MQTTS 8883 (X.509) | AWS |
| SSM Agent (todos los nodos) | HTTPS 443 saliente | SSM Endpoint regional |
| Sync WMS Concepción → Talca | TCP 8080 / 5432 | SRV-TALCA (on-prem) |
| Sync cross-dock → Talca (broker a broker) | AMQPS 5671 | SRV-TALCA (on-prem) |
| Caché Keycloak A-05/VM-C03 → S3 (import Realm) | HTTPS 443 (VPC Endpoint S3) | AWS (objeto cifrado) |
| *Excepción*: AWS DMS → PostgreSQL WMS (CDC) | TCP 5432 (over VPN) | VM-02 SRV-TALCA |
| *Excepción*: `celery-erp-sync` → ACL ERP | HTTPS 443 (over VPN) | VM-04 SRV-TALCA |

#### 2.5 Capa pública (DMZ) y DNS

- **Primera línea:** CloudFront + AWS WAF v2 (OWASP Top 10 + reglas personalizadas) + Shield Advanced; autenticación API Gateway con Keycloak OIDC, cuotas por cliente y validación de esquema (RT-11.11).
- **DNS:** Route 53 con health checks activos; routing por latencia en operación normal y **failover automático hacia us-east-1** en contingencia.

### 3. Alta disponibilidad

#### 3.1 Capa cloud (sa-east-1) — Multi-AZ

| Componente | AZ primaria | AZ secundaria | Failover automático |
|---|---|---|---|
| Aurora PostgreSQL | sa-east-1a (Writer) | sa-east-1b / sa-east-1c (2 Readers/Failover) | < 30 s |
| DynamoDB | Multi-AZ nativo | — | Transparente |
| EventBridge | 3 brokers en 3 AZ | — | Reelección de líder |
| ECS Fargate | sa-east-1a | sa-east-1b | Application Auto Scaling re-scheduling |
| ElastiCache Redis | sa-east-1a (Primary) | sa-east-1b (Replica) | < 60 s |
| ALB | sa-east-1a | sa-east-1b | Transparente |
| NAT Gateway | sa-east-1a | sa-east-1b (independiente) | Routing automático |

SLA de extremo a extremo sobre la **transacción crítica de negocio ≥ 99,9 % mensual** (RT-10.01, < 8,76 h/año), distinto de la clasificación TIER II del recinto (que es un medio, no el compromiso contractual).

#### 3.2 Capa on-premise

| Capa | Diseño | Sustento |
|---|---|---|
| Cómputo | Clúster virtualizado **3 nodos** con replicación síncrona Ceph (factor 2, quórum propio) | Sección de Dimensionamiento de este documento (§4); elimina el SPOF de un par sin quórum |
| Almacenamiento | **RAID 10** (BD transaccional NVMe, IOPS > 100 k) y **RAID 6 con hot-spare** (evidencia/logs) | ADR-10 · RT-03.14/RNF-13.04/13.05 |
| Red | Par de firewall UTM (HA A/P), 2 switches core + switch de gestión | RNF-13.03 |
| WAN | Tri-camino fibra + Starlink + LTE (SD-WAN) | RT-03.17 |
| Energía | UPS doble conversión **6 kVA N+1** (≥ 30 min a plena carga, RT-06.07) + generador **12 kVA** estanque 24 h (RT-06.08) + ATS | Sala de Servidores v02 §5 |
| Clima | Clima de precisión **N+1** ASHRAE TC 9.9, PUE de diseño 1,7 | Sala de Servidores v02 §5.3 |
| Recinto | Sala mediana, 4 gabinetes, TIER II objetivo (99,741 %) | Sala de Servidores v02 §1 |

VMs dimensionadas con headroom ×1,5 (RNF-19.04) para tolerar **3.900 entregas/día** en el peak de septiembre. SPOF declarados y mitigados (RT-02.11): periféricos de andén (respaldo manual), clúster Talca sin SPOF estructural, Concepción nodo único (autonomía 24 h + DRP), cross-dock mini-PC único (ventana de 3 h + sincronización diferida).

### 4. Recuperación ante desastres (BA Art. 20 · RT-07.07 · RNF-20.06)

#### 4.1 DRP nube (sa-east-1 → us-east-1) — activo-pasivo warm standby

- **Mecanismo:** Aurora Global Database (réplica us-east-1, lag < 1 s) · DynamoDB Global Tables · **S3 CRR** (RTC < 15 min) · **AWS DMS CDC** del PostgreSQL WMS on-premise (lee `wal_level=logical`; si la VPN cae, encola y reanuda sin pérdida).
- **Objetivos:** **RTO ≤ 4 h / RPO ≤ 15 min** (RNF-20.06); RPO declarado de mensajes no críticos ≤ 24 h, reducido a ≤ 15 min para los críticos con patrón **outbox dual-write**.
- **Modalidad justificada (RT-07.01):** activo-pasivo; activo-activo duplicaría la infraestructura transaccional (~105 TPS peak) con reconciliación de doble escritura sin beneficio frente al RTO comprometido.
- **Procedimiento:** decisión de failover **manual con disparador declarado** (health check de la región primaria < 5 min) y protección contra conmutación innecesaria (confirmación SNS + autorización); pasos 4–7 **automatizados por AWS Systems Manager Automation** (promoción Aurora 15–20 min, escalado ECS, actualización DNS 45–60 min). El RTO se cumple porque la réplica es legible y la región DR está "caliente" (escalable < 30 min a carga completa).
- **Retorno (failback):** procedimiento documentado en 6 pasos — re-sincronización con catch-up verificado, reconciliación de transacciones de la contingencia contra la bitácora (RT-03.12), transferencia de eventos pendientes, conmutación coordinada de DNS, validación funcional e informe con tiempo real.
- **Pruebas:** conmutación real **≥ 2 veces/año** con informe de RTO/RPO efectivos y plan de corrección de brechas (RT-07.07, Art. 20).
- **Residencia y transferencia internacional de datos (Art. 23 · Ley 21.719):** la replicación hacia us-east-1 constituye una **transferencia internacional de datos personales** y se rige por los resguardos declarados en la sección de **Arquitectura de Seguridad de este documento** (§10): cifrado con CMK gestionada por el CLIENTE, acuerdo de tratamiento con cláusulas de transferencia, **minimización** (la región secundaria no se explota analíticamente, solo sostiene continuidad), **exclusión de los datos de geolocalización de personas de la replicación transfronteriza** —permanecen solo en sa-east-1 con retención de 12 meses— y registro en el inventario de tratamientos. La residencia queda **sujeta a aprobación expresa del CLIENTE**; si no la aprueba, la alternativa declarada es la **continuidad intrarregional dentro de sa-east-1** (tercera AZ ampliada + respaldo inmutable regional — no es un segundo sitio geográfico ni usa Talca/Concepción para la carga cloud; AWS no tiene región en Chile), que cubre falla de AZ y corrupción de datos pero **degrada el RTO ante una caída de toda la región sa-east-1** (24–72 h desde el respaldo inmutable; **alternativa D del ADR-09**).

#### 4.2 DRP local (Talca → Concepción)

- Promoción controlada del WMS edge (VM-C01) mediante **procedimiento de 5 pasos**; Concepción ya opera autónoma (latencia ≤ 1 s de picking, RNF-05.01). **RTO +1–2 h** para la bodega.
- **Identidad sin conmutación local:** el maestro Keycloak está en la nube y las cachés A-05/VM-C03 siguen validando firmas offline — el DRP de identidad es la misma autoridad en nube, sin promoción local a maestro (elimina una clase entera de riesgos de DR).

#### 4.3 DRP de la identidad (ADR-06)

El maestro vive en la nube (Multi-AZ) con réplica DR us-east-1; las cachés locales son de solo lectura. No existe maestro local a promover, por lo que la identidad **no depende del switchover**.

### 5. Respaldos — esquema 3-2-1-1-0 (RNF-20.07)

**Esquema único** para toda la arquitectura híbrida (nube + on-premise):

| Pierna | Implementación |
|---|---|
| **3 copias** de los datos | (1) Datos activos sa-east-1 + WMS activo Talca; (2) Snapshot automatizado Aurora + respaldo local on-premise (D-05); (3) Backup exportado a S3 |
| **2 medios** | PostgreSQL/Aurora y S3 (almacenamiento de objetos) |
| **1 copia fuera del sitio** | S3 Cross-Region Replication → bucket en us-east-1 |
| **1 copia inmutable** | **S3 Object Lock (WORM, Compliance Mode) + AWS Backup Vault Lock** (ni el root puede eliminarla); `s3-documents-legal` y `s3-audit-logs` en Compliance, no Governance |
| **0 errores** | Restore testing automatizado mensual (Lambda) + verificación de restauración local + prueba DR semestral |

- **D-05 (NAS local con WORM) es la copia local de recuperación rápida** y **NO cuenta como la pierna inmutable**; permite restaurar el WMS en ≤ 4 h (RNF-20.06) sin depender del enlace WAN. RPO ≤ 15 min por AWS DMS CDC del WAL lógico (wal_level=logical) hacia la nube antes de la copia local.
- **Custodia física (RT-06.26/06.27/06.28):** medio de respaldo transportable, cifrado y rotado semanal (RT-07.10), trasladado bajo custodia acreditada a bóveda externa distinta del sitio primario; la pierna inmutable S3 es complementaria, no reemplaza la custodia física.

**Plan AWS Backup:**

| Recurso | Frecuencia | Retención | Destino |
|---|---|---|---|
| Aurora PostgreSQL | Diario + PITR continuo | 35 días | Backup Vault (cifrado CMK) |
| DynamoDB | Diario (On-Demand) | 35 días | Backup Vault |
| EFS | Diario | 30 días | Backup Vault |
| EBS | Diario (snapshots) | 14 días | Backup Vault |
| S3 documentos legales | Continuo (versioning + Object Lock) | 6 años | S3 + réplica CRR |
| Logs de seguridad/auditoría | Continuo | 7 años (Object Lock) | S3 archivo |

Vault Lock con enfriamiento de 3 días y retención mínima de 1 año; una vez bloqueado, ni la cuenta raíz puede eliminar respaldos. Retención sanitaria: **trazabilidad 5 años + vida útil** (D.S. 977/96), consistente con el lago analítico S3 y el repositorio de datos históricos (RT-05.15).

### 6. Referencias cruzadas con las decisiones de arquitectura

| ADR | Aporte a la vista de despliegue |
|---|---|
| ADR-03 | Modelo híbrido: borde operacional on-premise + carga principal en nube (justificación Art. 16) |
| ADR-05 | Capa de mensajería RabbitMQ local + SQS/EventBridge (buffer offline, Zero Trust outbound) |
| ADR-09 | DR warm standby activo-pasivo multi-región (RTO/RPO, pruebas 2×/año) |
| ADR-10 | Almacenamiento on-premise y niveles RAID (RAID 10 / RAID 6, RT-03.14) |
| ADR-12 | Cómputo elástico y absorción del peak de septiembre (escala predictiva + reactiva) |

### 7. Trazabilidad normativa (resumen)

| Requisito | Cómo se cumple |
|---|---|
| RT-04.01 | 5 ambientes habilitados (hito H3) |
| RT-04.02 | PreProd = Prod en topología, versiones y configuración |
| RT-04.05/04.06 | CI con gates de seguridad y despliegue automatizado con reversión |
| RT-04.07 | Azul-verde/canario demostrado en PreProd |
| RT-04.08/04.09 | Configuración por ambiente y secretos con rotación |
| RT-03.01/03.02 | AWS sa-east-1 primaria/us-east-1 DRP; Multi-AZ en componentes críticos |
| RT-03.03 | IaC 100 % versionado en el repositorio del CLIENTE |
| RT-03.10 | Autonomía 24 h / 14 h sin enlace |
| RT-03.12 | Sincronización automática y reconciliación determinista al reconectar |
| RT-03.14 | RAID declarado y justificado frente a alternativas |
| RT-03.17 | Enlace redundante, caminos/proveedores distintos, conmutación < 30 s |
| RT-07.07 / Art. 20 | Pruebas de DR reales ≥ 2 veces/año con medición de RTO/RPO |
| RT-10.01 | Disponibilidad e2e ≥ 99,9 % mensual sobre la transacción crítica |
| RNF-20.06 / 20.07 | RTO ≤ 4 h / RPO ≤ 15 min · respaldo 3-2-1-1-0 |
| Art. 21 | Zero Trust: solo outbound, sin conexiones entrantes (salvo D-AL-05) |
| **Art. 23 / Ley 21.719** | Residencia declarada, base de licitud y resguardos de la transferencia internacional a us-east-1, con exclusión de la geolocalización de personas (§4.1; detalle en la sección de **Arquitectura de Seguridad de este documento**, §10) |

---

## Dimensionamiento y Plan de Capacidad

> **Apartado 6 del Subdocumento 4 (T-22) — Dimensionamiento y plan de capacidad: volúmenes, concurrencia y crecimiento.** Marco: BA Art. 16 (híbrido) · BTT RT-09.01…09.09 (capacidad y desempeño) · RT-03.20 (ancho de banda) · RNF-19.01–19.04 · T-13. Conforme al numeral 14.2 del Caso (dimensionamiento explícito con método y supuestos, sin celdas vacías): declara la carga de diseño, los supuestos de volumen y crecimiento y sus criterios, como sección autocontenida de este Subdocumento 4.2, con los ADR-01/04/10/12 como referencia interna.

### 1. Criterios y método de dimensionamiento (RT-09.01, RT-09.02)

El dimensionamiento se deriva de la **volumetría real del Caso (Tabla 14.1 / Cap. 14 y 15)**, no de promedios genéricos, dado el **perfil de carga no plano** (RT-09.02):

| Ventana | Perfil |
|---|---|
| Preventa | 09:00–18:00 (62 preventistas con EC55) |
| Preparación (pick duro) | 22:00–06:00 (120 terminales RF, −22 °C) |
| Despacho | 05:30–07:00 (~96 camiones; 42 propios + 54 transportistas) |
| Sincronización de flota | 17:00–20:00 (~270 dispositivos remotos) |
| Peak de septiembre | ≈ 2× el volumen regular durante tres semanas |

**Reglas que gobiernan el dimensionamiento:**

- **Carga de diseño (RNF-19.04):** peak de septiembre (2.600 entregas/día) × **1,5 = 3.900 entregas/día** toleradas sin degradación.
- **TPS de diseño:** burst ×3 → **~105 TPS** (ver §3).
- **Crecimiento (RT-09.03):** la solución soporta **3× la volumetría inicial sin rediseño en 3 años** (misma topología, §6).
- **Umbrales (RT-09.01):** percentil **p95** en toda medición (Tabla 15), con umbrales por operación (§7).
- **Sin capacidad ociosa financiada (RT-15.01):** el cómputo elástico en nube escala automática (ADR-12); el on-premise se dimensiona al margen útil sin sobrecompra.
- **Coherencia interna:** los totales de este documento concuerdan con la Tabla 14.1 (volumetría) y con las secciones de Dimensionamiento (§4 on-premise, §5 nube) y los ADR (ADR-01, 04, 10, 12 y decisiones 16.1 N° 28 y N° 30).

### 2. Volumetría de referencia (Tabla 14.1 Caso 02)

#### 2.1 Valores base de dimensionamiento

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
| Sitios on-premise con cómputo | **5** (Talca, Concepción, Curicó, Chillán, Los Ángeles) — de las **6 instalaciones** que declaran la Tabla 14.1 y RT-21.16; la 6.ª es la casa matriz de Talca, sin nodo propio |

> **Nota de coherencia (instalaciones):** la Tabla 14.1 y RT-21.16 reportan **6 instalaciones** (7 a tres años); el despliegue físico ubica cómputo en los **5 sitios on-premise** listados + borde en terreno (calle y 14.200 puntos). La divergencia 5/6 (Tabla 14.1 vs §8 del Caso) está declarada en las consultas al mandante (Art. 43.3) y no altera el dimensionamiento: el cómputo se emplaza en los 5 sitios, la 6.ª instalación es de red/almacenamiento sin nodo de cómputo propio.

#### 2.2 Proyección a 3 años (Caso 02)

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

Los recursos se dimensionan, además, para **3× la volumetría inicial sin rediseño (RT-09.03)**: la proyección real del Caso a 3 años (+16–19 %) queda muy por debajo del límite de diseño, dejando margen ante crecimiento mayor al modelado (ADR-12).

### 3. Concurrencia y TPS de diseño

#### 3.1 Usuarios y terminales concurrentes

| Rol | Concurrencia | Dispositivo |
|---|---|---|
| Preventistas | 62 simultáneos | Zebra EC55 (parque 62 + reserva 20 %) |
| Conductores (reparto) | ~200 simultáneos | Zebra TC58e (parque único 42 propios + ~160 externos + reserva) |
| Personal de centro de distribución | 310 (turno) | Estaciones y terminales fijas |
| Operarios de picking simultáneos (turno nocturno) | 120 | Zebra MC9400 Cold Storage (pool Talca 144 = 120 + 20 %; Concepción 30) |
| Terminales RF concurrentes | 120 (base de diseño) | Ídem |
| Call center / supervisión | ~20 | Estaciones |
| **Dispositivos móviles registrados (MQTT/IoT Core)** | **~270** (hasta ~300+ en peak) | EC55 + TC58e + terminales de cámara |

#### 3.2 TPS estimados (peor ventana)

| Flujo | Cálculo | TPS |
|---|---|---|
| Confirmaciones de picking | 120 terminales × 1 confirmación / 6 s | ~20 TPS |
| Pedidos de preventa (09:00–13:00) | 62 preventistas × 1 línea / 8 s | ~8 TPS |
| Movimientos de inventario + sincronización | Suma de flujos (broker, WMS, IoT) | ~35 TPS |
| **TPS de diseño (burst ×3)** | 35 × 3 en peak de septiembre | **~105 TPS** |

> El burst ×3 absorbe el peak de septiembre y las ráfagas de la ventana de sincronización 17:00–20:00. El **~105 TPS** es el valor único de diseño de este documento, citado por ADR-01 y ADR-12, y sustenta el dimensionamiento de IOPS de VM-02 (§4.3) y del escalado ECS (ADR-12).

### 4. Dimensionamiento on-premise (ADR-10)

#### 4.1 Cómputo — CD Talca (clúster N+1, 3 nodos Proxmox/Ceph)

| Recurso | Asignado | Físico (clúster) | Utilización bajo N+1 |
|---|---|---|---|
| vCPU | 30 | 96 threads (3 nodos × 32) | 30 / 64 = **47 %** (2 supervivientes) |
| RAM | 68 GB | 384 GB (3 × 128) | 68 / 256 = **27 %** |
| Almacenamiento (pool Ceph, réplica 2) | 1.890 GB | **5,76 TB útiles** (12 OSDs, RAID 10 NVMe) | **32 %** |

**VMs del clúster Talca (familias declaradas en la sección de Dimensionamiento on-premise de este documento, §4):**

| VM | Rol | vCPU | RAM | Disco datos |
|---|---|---|---|---|
| VM-01 | WMS Core (picking FEFO, misiones RF, despacho, SSCC GS1) | 8 | 16 GB | 100 GB |
| VM-02 | PostgreSQL — BD transaccional del maestro de bodega | 8 (→12) | 32 GB (→64) | 1.500 GB |
| VM-03 | RabbitMQ — broker de colas offline (buffer 24 h) | 4 | 8 GB | 200 GB |
| VM-04 | ACL ERP — frontera única de integración | 4 | 4 GB | 20 GB |
| VM-05 | Keycloak Local Auth Cache / Offline Proxy (A-05, Modelo B) | 4 | 4 GB | 20 GB |
| VM-06 | OpenTelemetry Collector + SSM Agent (buffer 24 h) | 2 | 4 GB | 50 GB |

#### 4.2 Cómputo — Concepción (edge) y cross-docking

| Sitio | Capacidad | Rol |
|---|---|---|
| CD Concepción (C3) | 12 vCPU / 24 GB / RAID 10 (4×NVMe 960 GB + hot-spare) | WMS en modo reducido 24 h sin enlace (RNF-13.01) |
| Plataformas de cross-docking (E-01) | Mini-PC industrial (Advantech ARK-2250 / NUC Pro 12) | Mini-WMS E-01 + router Starlink (enlace principal) + LTE dual de respaldo |

#### 4.3 Almacenamiento (ADR-10, RT-03.14)

| Capa | Esquema | Capacidad útil |
|---|---|---|
| BD transaccional + pool de datos | Ceph réplica 2 sobre RAID 10 NVMe (≈ 4× factor de compra) | 5,76 TB pool (margen 68 % a 5 años) |
| Crecimiento 5 años | 1.890 GB × 3 | ≈ 5,7 TB < 5,76 TB ✓ |
| Respaldo de recuperación rápida (D-05) | NAS 2U, RAID 6 (4 × 4 TB) + WORM local | 8 TB |
| IOPS VM-02 | 105 TPS × 8 E/S = 840 IOPS requeridas | NVMe RAID 10 > 100.000 IOPS ✓ |

#### 4.4 Ancho de banda WAN por sitio (RT-03.20 / RNF-13.08)

| Sitio | Régimen normal | Peak septiembre | Respaldo (autoconmutación < 30 s) |
|---|---|---|---|
| CD Talca (D-03/D-06/D-04) | 20 Mbps fibra | 50 Mbps | Starlink 1 TB (50–100 Mbps) · LTE 5→10 Mbps |
| CD Concepción | 10 Mbps fibra | 20 Mbps | Starlink 1 TB · LTE 3→5 Mbps |
| Cross-docking (×3) | Starlink 500 GB principal | Ídem | LTE dual 2→5 Mbps (2 proveedores) |

> **Cohesión con el apartado 5 (despliegue):** estos valores son los declarados en la sección de **Arquitectura de Despliegue de este documento** (§2, VPN IPsec dual por CD).

### 5. Dimensionamiento nube (ADR-12)

| Componente | Base (normal) | Peak septiembre | Criterio de escalado |
|---|---|---|---|
| ECS Fargate Django (tareas `2 vCPU / 4 GB`) | 2 | 6 (3×) | Target Tracking CPU > 70 % |
| ECS Fargate Celery workers (`2 vCPU / 4 GB`) | 2 | 4 (2×) | Cola (queue depth) / CPU |
| AWS Lambda (`fn-iot-validator`, `fn-document-signer`) | 100 concurrencias | 500 (reserva) | Eventos IoT Core / S3 |
| Aurora PostgreSQL (writer \| reader) | `db.r6g.large` × 2 AZ | `db.r6g.xlarge` + 2 readers | CPU > 60 % / Conexiones > 80 % |
| ElastiCache Redis | `cache.r6g.large` | `cache.r6g.xlarge` | Memoria > 75 % (stock/crédito < 2 s) |
| DynamoDB (telemetría IoT cruda) | On-demand | On-demand | Sin gestión de capacidad |
| Amazon EventBridge | Serverless | Serverless | Escala con el evento |
| AWS IoT Core (MQTT) | ~270 dispositivos | ~300+ | Concurrencia de terreno |
| Keycloak IdP maestro (Fargate) | 1 tarea `1 vCPU / 2 GB` | 2 tareas (Multi-AZ) | CPU > 60 % |

**Escalado automático (RT-09.04):**
- **Predictivo + reactivo (ADR-12):** pre-warm en agosto de las tareas ECS, concurrencia reservada Lambda y EventBridge; reactivo con Target Tracking en < 2 min · aprovisionamiento en < 3 min · cooldown 60 s.
- **Serverless-first:** DynamoDB On-Demand, Lambda y EventBridge escalan sin configuración adicional; la capacidad se paga por uso (sin capacidad ociosa, RT-15.01 — FinOps Cloud §4.5).

### 6. Plan de capacidad y crecimiento 3× sin rediseño (RT-09.03)

El crecimiento se absorbe **con el mismo diseño** (sin cambio de topología, VLAN, réplica ni nube):

| Recurso | Diseño (3.900 entregas/día) | 3× (7.800 entregas/día) | Acción declarada |
|---|---|---|---|
| vCPU clúster Talca | 30 / 64 = 47 % (N+1) | ~90 asignadas | Ampliación RT-08.05; al acercarse al margen, inserción del **4.º servidor idéntico** (rack R04 de crecimiento, Sala §6.2) → 96 threads + N+1 real |
| RAM | 68 / 256 = 27 % | ~205 GB | Dentro de los 384 GB físicos ✓ |
| Pool Ceph | 32 % de 5,76 TB | ≤ 96 % | Ampliación por adición de OSD/NVMe, sin rediseño |
| Enlace Talca / Concepción | 20→50 / 10→20 Mbps | 50 / 100 Mbps | Contrato escalonado de enlaces (§3.7) |
| TPS VM-02 | ~105 | ~315 | Escala vertical 8→12 vCPU (32→64 GB) + particionado mensual |

En nube, el 3× se absorbe por **auto-scaling** (Fargate 2→6, Celery 2→4, Lambda hasta 500, Aurora `xlarge` + readers), sin rediseño arquitectónico — misma decisión ADR-12 que fija el límite de elasticidad del peak.

### 7. Umbrales de desempeño (RT-09.01 — Tabla 15, percentil p95)

| Operación | Umbral (p95) |
|---|---|
| Confirmación de una línea de preparación de pedidos (picking) | ≤ 1 s |
| Registro de una entrega en el local del cliente | ≤ 2 s |
| Registro de una línea en toma de pedido de preventa | ≤ 1,5 s |
| Consulta de stock y crédito en preventa | ≤ 2 s |
| Transacción operacional crítica de terreno (e2e) | ≤ 3 s |
| Navegación entre vistas ya cargadas | ≤ 1 s |
| Búsqueda con criterios compuestos | ≤ 3 s |

Los umbrales se verifican con monitoreo OTel/Prometheus (CloudWatch) y se prueban en Pre-Producción (§10).

### 8. Primer cuello de botella (RT-09.05)

**VM-02 (PostgreSQL — escritura transaccional del maestro de bodega)** se satura primero a medida que crece la carga: todo el picking (22:00–06:00) y el despacho masivo (05:30–07:00) pasan por el único punto de escritura.

| Detección | Mitigación |
|---|---|
| p95 de escritura > 800 ms; commit ×3 sobre la base; IO wait > 15 %; cola Backend > 5–10 | 1) Escala vertical 8→12 vCPU / 32→64 GB (margen N+1) · 2) particionado mensual + PgBouncer · 3) réplica de solo lectura · 4) 4.º nodo / sharding al agotar margen |

En nube el equivalente es Aurora (writer + readers); EventBridge/SQS absorben el pico de sincronización 17:00–20:00 (ADR-05).

### 9. Degradación controlada (RT-09.08)

- **Enlace WAN:** QoS prioriza broker/WAL; colas diferidas fuera de la ventana; conmutación SD-WAN < 30 s entre fibra/Starlink/LTE.
- **Offline:** buffers RabbitMQ de 24 h (RNF-13.01) y buffers OTel de 24 h; reconciliación cronológica e idempotente al reconectar (RT-03.12).
- **Nube:** throttling en API Gateway, timeouts y reintentos con backoff en Celery, DLQ para tareas fallidas.

### 10. Pruebas de carga y estrés (RT-09.06 / RT-09.07 — T-13)

| Prueba | Carga | Escenario |
|---|---|---|
| Carga (RNF-19.04) | **1,5 × la carga de diseño = 5.850 entregas/día ≈ 160 TPS sostenidos** (carga de diseño = peak 2.600 × 1,5 = 3.900; la prueba la vuelve a multiplicar por 1,5) | Pre-Producción, perfiles horarios reales (pick nocturno, despacho, preventa) |
| Estrés | Incremento hasta el **punto de quiebre ≥ 3×** | Curva de tiempo de respuesta vs carga |
| Informe de carga (RT-09.07) | Curvas, saturación, recursos (CPU/RAM/IOPS/enlace/colas) | Insumo al hito de producción (mes 16) y a la actualización de capacidad (RT-09.09, §11) |

Herramientas: **k6/Gatling** + drivers a medida contra las APIs (svc-erp-integration, svc-broker). Cortes: Etapa 1 (mes 13), Etapa 2 (mes 19), re-ejecución trimestral. **Calendario e hitos formales en el Formulario T-13.**

### 11. Actualización del plan de capacidad (RT-09.09)

- **Gestión de capacidad durante la Operación con proyección trimestral de crecimiento** (RT-09.09): consumo real vs. proyectado (vCPU/RAM/almacenamiento/enlace/colas/TPS), con **alertas anticipadas de agotamiento al 70 % / 2 semanas** y propuesta de ajuste de dimensionamiento y de costo.
- **Ventana de ampliación** conforme al procedimiento RT-08.05 (adición de vCPU/OSD dentro del físico; contrato escalonado de enlaces; 4.º nodo al acercarse al margen). La revisión se apoya en el informe de carga (RT-09.07) como insumo del hito de producción (mes 16).
- **Nube:** revisión FinOps (§4.5 Cloud) — evaluar umbrales Target Tracking y concurrencia reservada con al menos 30 días antes del peak de septiembre.

### 12. Referencias cruzadas con las decisiones de arquitectura

| ADR | Aporte a la vista de capacidad |
|---|---|
| ADR-01 | Monolito modular: el peak se absorbe con réplicas de la misma imagen (2→6 Fargate) |
| ADR-04 | Persistencia políglota: DynamoDB On-Demand (IoT) + Aurora (OLTP) + OLAP S3/Redshift (series consolidadas) |
| ADR-10 | Almacenamiento on-premise: RAID 10 NVMe > 100.000 IOPS, pool Ceph 5,76 TB |
| ADR-12 | Absorción del peak de septiembre con cómputo elástico (escala predictiva + reactiva) |

### 13. Trazabilidad normativa (resumen)

| Requisito | Cómo se cumple |
|---|---|
| RT-09.01 | Cálculo de capacidad con supuestos (§2–§3); umbrales p95 (§7) y Tabla 15 |
| RT-09.02 | Perfil de carga no plano como base del diseño (§1) |
| RT-09.03 | 3× en 3 años sin rediseño (§6) |
| RT-09.04 | Escalado horizontal automático con umbrales y límites (§5) |
| RT-09.05 | Primer cuello de botella declarado y mitigado (§8) |
| RT-09.06 / 09.07 | Pruebas de carga/estrés 1,5× peak en PreProd + informe de carga (§10, T-13) |
| RT-09.08 | Degradación controlada por servicio (§9) |
| RT-09.09 | Gestión trimestral de capacidad con alertas anticipadas y propuesta de ajuste (§11) |
| RT-15.01 | Sin capacidad ociosa financiada (auto-scaling + escala vertical dentro del margen) |
| RNF-19.04 | Pruebas 1,5× peak (§10) y carga de diseño 3.900 entregas/día (§3) |

---

## Inteligencia de Negocios y Analítica Operacional (BI)

> **Apartado 7 del Subdocumento 4 (T-22) — Justificación del módulo de BI/Analítica.** Justifica la existencia, alcance y diseño del módulo de Inteligencia de Negocios (BI) y Analítica Operacional: no es una capa optativa sino un componente **obligatorio** exigido por las Bases Técnicas Transversales (**RT-05.25/05.26** — capa analítica con tableros operacionales y de gestión, filtros por período, unidad organizacional y drill-down; **RT-14.02–14.04** — tableros, SLA/SLO sobre experiencia real p95 y alertamiento por síntomas de negocio; **RT-16.28** — exportación) y por el Caso 02 (indicadores **OTIF**, **Fill Rate** y **Costo de Servir**). Marco adicional: **BA Art. 5°** (capacidad analítica como servicio horizontal), **Cap. 5** (innovación obligatoria de análisis predictivo) y **Art. 39°** (acceso y exportación de datos). Fecha de emisión 04/09/2026 · revisión 1.0.

### 1. Objetivo

Este documento justifica la existencia, alcance y diseño del módulo de Inteligencia de Negocios (BI) y Analítica Operacional dentro de la arquitectura propuesta, demostrando que no se trata de una capa optativa sino de un componente **obligatorio** exigido tanto por las Bases Técnicas Transversales como por el Caso 02. Se presenta la trazabilidad completa desde las fuentes normativas hasta los componentes tecnológicos que lo materializan.

### 2. Fundamento normativo

#### 2.1 Bases Técnicas Transversales (RT)

| ID RT | Requerimiento | Tipo | Naturaleza |
|-------|--------------|------|------------|
| RT-05.25 | Capa analítica con tableros operacionales y de gestión | Obligatorio | Estructura de plataforma |
| RT-05.26 | Tableros con filtros por período, unidad organizacional y drill-down | Obligatorio | Estructura de plataforma |
| RT-14.02 | Acceso propio y permanente a tableros operacionales y de negocio | Obligatorio | Observabilidad |
| RT-14.03 | SLA/SLO medidos sobre experiencia real del usuario (P95) | Obligatorio | Observabilidad |
| RT-14.04 | Alertamiento basado en síntomas de negocio | Obligatorio | Observabilidad |

Las Bases Técnicas Transversales establecen que la capa analítica es un **componente estructural** de la plataforma, no una funcionalidad adicional. Su omisión o subdimensionamiento constituiría una observación grave conforme al Art. 10° de las Bases Administrativas.

#### 2.2 Caso 02 — Distribuidora Puelche S.A.

El caso define tres indicadores estratégicos que requieren procesamiento analítico continuo:

| Indicador | Estado actual | Meta | Fuente en Caso |
|-----------|--------------|------|----------------|
| OTIF (On-Time In-Full) | 82.4% | > 95% | Cap. 4.1, 7.1 |
| Fill Rate | 91.3% | > 97% | Cap. 4.1 |
| Costo de Servir por cliente | Desconocido | Calcular y gestionar | Cap. 7.2, 9.8 |

Citas textuales del caso que respaldan la exigencia:

- *"Mi indicador principal es el OTIF"* — Nelson, Gerente Comercial (Cap. 7.1)
- *"El costo de servir es mi obsesión. Si no sabemos cuánto nos cuesta llegar a cada local, ¿cómo vamos a decidir a quién priorizar?"* — Gerente de Finanzas (Cap. 7.2)
- *"Necesito saber el costo de servir por cliente y por entrega"* — Gerente de Finanzas (Cap. 9.8)

Estos indicadores no pueden calcularse sin un componente de analítica que consolide datos transaccionales de múltiples módulos (preventa, transporte, cobranza, telemetría, bodega) y los presente de forma consumible por los gerentes.

### 3. Requerimientos funcionales del módulo

#### 3.1 Requerimientos propios del módulo (Épica 11)

| ID RF | Nombre | Actor(es) principal(es) | Descripción | Origen |
|-------|--------|------------------------|-------------|--------|
| RF-11.01 | Distribución Automática de Reportes Ejecutivos | Gerente de Finanzas, Gerente Comercial, Jefa de Calidad | Programar y distribuir vía correo reportes ejecutivos consolidados (PDF/XLSX) con periodicidad semanal y mensual, desglosando OTIF, Fill Rate, Merma por vencimiento y Costo de Servir por zona y canal | Cap. 7.1, 7.2, 9.8 |
| RF-11.02 | Cálculo del Costo de Servir por Entrega y Cliente | Gerente de Finanzas, Gerente Comercial | Calcular Costo de Servir real por entrega y cliente, imputando costos directos de transporte (combustible, peajes, tiempo de conducción/descarga) e indirectos prorrateados (bodega, administración) | Cap. 4.4, 7.2, 9.8 |
| RF-11.03 | Cálculo Diario Unificado del Indicador OTIF | Gerente Comercial, Jefa de Calidad, Conductores | Calcular diariamente OTIF por cliente, ruta, zona y total consolidado. On-Time = cumplimiento de fecha/ventana horaria. In-Full = 100% de ítems y unidades pedidas. Obligar registro de causal tipificada ante desvíos | Cap. 7.1, 9.1 |
| RF-11.04 | Medición de Fill Rate y Perfect Order con POD Móvil | Gerente Comercial, Conductores | Calcular automáticamente Fill Rate (unidades entregadas vs pedidas) e índice de Perfect Order contrastando orden original contra datos de entrega física confirmados en dispositivo móvil | Cap. 7.1, 9.4 |
| RF-11.05 | Monitoreo y Alerta de Ocupación de Flota | Planificador de rutas, Gerente Comercial | Calcular diariamente utilización de capacidad volumétrica (m³) y peso (kg) por viaje, alertando camiones con ocupación inferior al umbral configurable (< 65%) | Cap. 4.4, 7.2 |
| RF-11.06 | Tablero de Control Operacional en Tiempo Real | Gerente Comercial, Gerente de Finanzas, Jefa de Calidad | Tablero de Control que consolide avance de rutas de despacho, % entregas cumplidas, devoluciones en tránsito, alertas de cadena de frío y monto recaudado en efectivo | RT-05.29, Cap. 9.1, 9.6 |
| RF-11.07 | Liquidación y Cierre Comercial por Camión | Cajero Liquidador, Conductores, Gerente de Finanzas | Procesar automáticamente la liquidación y cierre comercial por camión al retornar a base, consolidando documentos tributarios, devoluciones, cobranzas y balance de envases retornables | RT-05.29 |
| RF-11.08 | Segmentación de Clientes por Rentabilidad Neta | Gerente Comercial, Preventista, Gerente de Finanzas | Segmentar mensualmente la cartera en matrices de rentabilidad neta (margen comercial vs costo de servir real), sugiriendo ajustes de frecuencia o umbrales mínimos de compra para clientes no rentables | Cap. 7.2, 9.8 |

#### 3.2 Requerimientos no funcionales del módulo

| ID RNF | Nombre | Descripción | Prioridad |
|--------|--------|-------------|-----------|
| RNF-11.01 | Latencia de despliegue de indicadores operacionales | Desplegar indicadores del día con latencia ≤ 5 min desde recepción en backend central | Muy Alta |
| RNF-11.02 | Desacople OLAP/BI vs OLTP | Desacoplar procesamiento analítico del motor transaccional, garantizando cero degradación en tiempos de respuesta de bodega (picking ≤ 1s) y preventa (≤ 1.5s) | Alta |

#### 3.3 Requerimientos transversales vinculados al módulo

| ID RF | Nombre | Actor(es) | Descripción | RT de origen |
|-------|--------|-----------|-------------|--------------|
| RF-16.02 | Acceso del CLIENTE a tableros operacionales y de negocio | Cliente | Acceso propio y permanente a tableros operacionales y de negocio con datos en tiempo real y capacidad de exportación | RT-14.02 |
| RF-16.03 | Alertamiento basado en síntomas de negocio | Equipo de operaciones | Alertas por síntomas de negocio (OTIF bajo, pedidos no preparados), no solo umbrales de infraestructura. Con supresión de ruido, agrupación, escalamiento y turnos de disponibilidad | RT-14.04 |
| RF-17.12 | Listados ordenables, filtrables, paginados y exportables | Persona usuaria interna | Listados ordenables, filtrables, paginados y exportables en formatos abiertos, con filtro aplicado reflejado en exportación | RT-16.28 |
| RNF-16.01 | SLA/SLO medidos sobre experiencia real del usuario | Equipo de operaciones | Indicadores de nivel de servicio medidos sobre experiencia real (P95), no sobre pruebas sintéticas | RT-14.03 |

#### 3.4 Requerimientos de otras épicas con dependencia del módulo BI

| ID RF | Épica | Nombre | Dependencia con BI |
|-------|-------|--------|-------------------|
| RF-04.08 | Planificación de Rutas | Cálculo integral del costo de entrega realizada | Alimenta RF-11.02 (costo de servir) con costo calculado por ruta |
| RF-06.07 | Transporte/POD | Sincronización de registros de turno (reporte de cierre) | Alimenta RF-11.07 (liquidación por camión) con datos de cierre |
| RF-07.02 | Cobranza | Rendición Digital Individual de Efectivo | Alimenta RF-11.07 con cuadratura de cobranza |
| RF-07.07 | Cobranza | Consulta de Estado de Cuenta en Portal | Consumida por RF-16.02 (tableros para clientes) |
| RF-08.06 | Logística Inversa | Reporte de Pérdida de Envases Retornables | Alimenta RF-11.02 (costo de servir) con costo de envases perdidos |
| RF-08.07 | Logística Inversa | Integración de Devoluciones y Mermas al Costo de Servir | Alimenta RF-11.02 con componente de devoluciones/mermas |
| RF-09.05 | Trazabilidad | Alerta de excursiones térmicas | Consumida por RF-11.06 (tablero operacional) y RF-16.03 (alertas) |
| RF-14.06 | Telemetría | Integración de telemetría con costo de servir | Alimenta RF-11.02 con km reales y tiempo de viaje por entrega |
| RF-14.09 | Telemetría | Reportes de kilometraje y consumo | Consumida por RF-11.01 (reportes ejecutivos) y RF-11.02 (costo de servir) |
| RF-02.07 | Almacén | Consulta de nivel de ocupación por zona | Consumida por RF-11.06 (tablero operacional) |
| RF-03.08 | Preventa | Alerta por superación del límite de crédito | Consumida por RF-16.03 (alertas de negocio) |

### 4. Mapeo de requerimientos a componentes de arquitectura

#### 4.1 Componentes del módulo BI

El módulo de BI/Analítica se materializa en los siguientes componentes de la arquitectura:

| Componente | Ubicación | Tecnología | Responsabilidad |
|------------|-----------|------------|-----------------|
| **Motor OLAP / Warehouse** | Cloud (AWS) | Amazon Redshift Serverless | Almacenamiento analítico desacoplado de OLTP. Consolida datos de Aurora PostgreSQL vía DMS CDC. Alimenta RF-11.01–RF-11.08 |
| **Motor transaccional fuente** | Cloud (AWS) | Amazon Aurora PostgreSQL (PostGIS) | Base OLTP de donde se extraen los datos hacia Redshift. Contiene datos de preventa, reparto, cobranza, bodega |
| **Motor transaccional fuente (on-prem)** | On-Premise (Talca) | PostgreSQL + PostGIS (local) | WMS de bodega. Sincroniza con Aurora vía DMS CDC (RPO ≤ 15 min) |
| **Capa de procesamiento analítico** | Cloud (AWS) | Celery workers (Django) + Redshift SQL | Cálculo de OTIF (RF-11.03), Fill Rate (RF-11.04), Costo de Servir (RF-11.02), Ocupación de Flota (RF-11.05), Segmentación (RF-11.08) |
| **Distribución de reportes** | Cloud (AWS) | Celery Beat + SES (correo) + S3 (almacenamiento PDF/XLSX) | RF-11.01: reportes automáticos semanales/mensuales |
| **Tablero operacional** | Cloud (AWS) | Grafana (autoservicio) o Angular SPA | RF-11.06: tablero de control en tiempo real. RF-16.02: acceso del cliente. RF-16.03: alertas de negocio |
| **Sistema de alertas** | Cloud (AWS) | CloudWatch + SNS + Celery | RF-16.03: alertamiento por síntomas de negocio. RF-11.05: alertas de ocupación |
| **Portal de autoatención cliente** | Cloud (AWS) | Angular SPA + API Gateway | RF-16.02: tableros para clientes con datos en tiempo real y exportación |
| **Caché de indicadores** | Cloud (AWS) | Amazon ElastiCache (Redis) | RNF-11.01: latencia ≤ 5 min para despliegue de indicadores |

#### 4.2 Flujo de datos analíticos

En texto, el flujo de datos analíticos es: **fuentes transaccionales** (Preventa App, Bodega WMS, Transporte GPS y Cobranza App) → **motor transaccional** Aurora PostgreSQL (`Preventa`, `Inventario`, `Transporte` y `Cobranza`, cada dominio OLTP) → **DMS CDC** (extracción continua e incremental) → **motor analítico** Redshift Serverless (dimensiones Tiempo, Cliente, Ruta, Producto, Vehículo y Zona; hechos `fact_entregas`, `fact_costos` y `fact_inventario`; vistas materializadas `mv_otif_diario`, `mv_costo_servir`, `mv_fill_rate`, `mv_ocupacion_flota` y `mv_rentabilidad_cliente`) → dos salidas: **Tablero Gerencial** (Grafana/Angular — RF-11.06 operacional, RF-16.02 para el cliente, RF-16.03 alertas) y **Distribución por correo** (SES + Celery Beat — informes semanal y mensual, RF-11.01).

#### 4.3 Justificación del desacople OLAP/OLTP (RNF-11.02)

El RNF-11.02 exige que las consultas analíticas **no degraden** los tiempos de respuesta transaccionales. Esto se resuelve mediante:

1. **Motor separado:** Redshift Serverless es un sistema OLAP independiente de Aurora PostgreSQL (OLTP). Las cargas analíticas corren en un clúster dedicado con recursos aislados.

2. **Extracción asíncrona:** DMS CDC copia cambios de Aurora → Redshift sin bloquear transacciones OLTP. La extracción es incremental y continua.

3. **Vistas materializadas pre-calculadas:** Los indicadores (OTIF, Fill Rate, Costo de Servir) se calculan como vistas materializadas en Redshift, que se refrescan periódicamente (cada 5–15 min según RNF-11.01). Las consultas de tablero leen de estas vistas, no de tablas crudas.

4. **Caché Redis para tableros:** Los resultados de consultas frecuentes se cachean en ElastiCache Redis, reduciendo aún más la carga sobre Redshift para dashboards de alta concurrencia.

**Resultado:** Picking en bodega mantiene latencia ≤ 1s y preventa ≤ 1.5s (RF de bodega/preventa) mientras los gerentes consultan tableros analíticos simultáneamente.

### 5. Componente de Costo de Servir

El cálculo del Costo de Servir (RF-11.02) es el requerimiento analítico más complejo del módulo, ya que consolida datos de 4 fuentes distintas:

| Componente de costo | Fuente de datos | Módulo productor | Fórmula simplificada |
|---------------------|----------------|------------------|----------------------|
| Combustible devengado | Telemetría GPS (litros/km) | Telemetría (Épica 14) | km recorridos × precio litro × rendimiento vehicular |
| Peajes | Registro de viaje | Transporte (Épica 6) | Monto real de peajes por viaje |
| Tiempo de conducción | Telemetría GPS (horas) | Telemetría (Épica 14) | Horas de conducción × costo hora conductor |
| Tiempo de descarga | App móvil de reparto | Transporte (Épica 6) | Minutos de descarga × costo hora |
| Costo de bodega (prorrateo) | WMS | Almacén (Épica 2) | Costo total bodega ÷ volumen almacenado × volumen cliente |
| Costo administrativo (prorrateo) | Facturación ERP | Administración | Costo fijo administrativo ÷ N pedidos × pedidos cliente |
| Costo de devoluciones/mermas | Logística inversa | Logística Inversa (Épica 8) | Costo de envases perdidos + productos dañados |
| Costo de mermas por vencimiento | Inventario | Almacén (Épica 2) | Valor de producto vencido imputado al cliente |

La fórmula de rentabilidad neta resultante (RF-11.08):

**Margen neto = Ingreso por venta − Costo de mercadería − Costo de servir real**

Donde el Costo de servir real = Σ(componentes anteriores) por cliente y por entrega.

### 6. Componente de Alertas de Negocio (RF-16.03)

Las alertas por síntomas de negocio se distinguen de las alertas de infraestructura en que miden **impacto al negocio**, no estado de servidores:

| Síntoma de negocio | Umbral configurable | Fuente de datos | Acción |
|--------------------|--------------------|--------------------|--------|
| OTIF diario < meta | < 95% (configurable) | Redshift (mv_otif_diario) | Notificación gerente comercial + calidad |
| Fill Rate mensual < meta | < 97% (configurable) | Redshift (mv_fill_rate) | Alerta gerente comercial |
| Costo de servir > umbral | > $X por entrega (configurable) | Redshift (mv_costo_servir) | Alerta gerente finanzas |
| Ocupación de flota < umbral | < 65% (configurable) | Redshift (mv_ocupacion_flota) | Alerta planificador de rutas |
| Excursión térmica en tránsito | > umbral por tipo producto | IoT/DynamoDB + SNS (Lambda validador) | Alerta conductor + calidad |
| Crédito de cliente excedido | Deuda + pedido > cupo | Aurora PostgreSQL (OLTP) | Bloqueo en app de preventa |
| Envases retornables excedidos | Saldo > umbral configurable | Aurora PostgreSQL (OLTP) | Alerta preventista |

### 7. Requerimientos de tableros (RT-05.25, RT-05.26)

Las Bases exigen tableros con las siguientes capacidades:

| Capacidad exigida | RT | Implementación |
|-------------------|----|--------------------|
| Tableros operacionales y de gestión | RT-05.25 | Dashboards separados: operacional (tiempo real, RF-11.06) y estratégico (periódico, RF-11.01) |
| Filtros por período | RT-05.26 | Filtros de rango de fechas en Grafana/Angular (hoy, semana, mes, trimestre, año) |
| Filtros por unidad organizacional | RT-05.26 | Filtros por zona, ruta, sucursal, cliente, canal de comercialización |
| Drill-down | RT-05.26 | Navegación de resumen → detalle: total → zona → ruta → cliente → entrega individual |
| Datos en tiempo real | RT-14.02 | Actualización cada ≤ 5 min (RNF-11.01) vía Redis cache + Redshift refresh |
| Acceso del cliente | RT-14.02 | Portal web Angular con autenticación Keycloak, RF-16.02 |
| Exportación | RT-16.28 | Descarga en PDF, XLSX, CSV con filtros aplicados, RF-17.12 |

#### 7.1 Tablero operacional (RF-11.06)

| Panel | Indicadores mostrados | Fuente | Frecuencia actualización |
|-------|----------------------|--------|-------------------------|
| Avance de rutas | Pedidos completados / total, % avance por ruta | Aurora PostgreSQL (OLTP) | Tiempo real (< 1 min) |
| Entregas cumplidas | % OTIF del día, entregas a tiempo vs atrasadas | Redshift (mv_otif_diario) | ≤ 5 min |
| Devoluciones en tránsito | Cantidad de devoluciones, productos devueltos | Aurora PostgreSQL (OLTP) | Tiempo real |
| Alertas cadena de frío | Excursiones térmicas activas, historial 24h | DynamoDB (IoT) + SNS (Lambda validador) | Tiempo real |
| Recaudación del día | Monto recaudado en efectivo, cheques, transferencias | Aurora PostgreSQL (cobranza) | Tiempo real |

#### 7.2 Tablero gerencial (RF-11.01)

| Reporte | Periodicidad | Indicadores | Destinatarios |
|---------|-------------|-------------|---------------|
| Reporte semanal ejecutivo | Cada lunes 06:00 AM | OTIF semanal, Fill Rate, Costo de Servir por zona, devoluciones | Gerente Comercial, Jefa de Calidad |
| Reporte mensual ejecutivo | Día 2 de cada mes | OTIF mensual, Fill Rate, Merma por vencimiento, Costo de Servir por zona y canal, rentabilidad por cliente | Gerente Comercial, Gerente de Finanzas, Jefa de Calidad |

### 8. Cumplimiento de Bases Administrativas

| Artículo Bases Admin. | Exigencia | Cumplimiento del módulo BI |
|----------------------|-----------|---------------------------|
| Art. 5° Capacidad Analítica | Proponer BI/OI como servicio horizontal | Módulo de BI como servicio horizontal sobre Redshift, consumido por todas las épicas |
| Cap. 5° Innovación | 1 innovación obligatoria (análisis predictivo) | Análisis predictivo de demanda (consumo de Redshift ML o SageMaker) usando histórico OTIF, Fill Rate y patrones de compra |
| Art. 39° Acceso a datos | Garantizar acceso y exportación de datos | Tableros con exportación PDF/XLSX/CSV (RF-17.12), portal de autoatención para clientes (RF-16.02) |

### 9. Resumen de cobertura

#### 9.1 Conteo por origen

| Fuente | Cantidad de RF/RNF que alimentan al módulo BI |
|--------|-----------------------------------------------|
| Épica 11 (propios) | 8 RF + 2 RNF = 10 |
| Transversales (Bases) | 3 RF + 1 RNF = 4 |
| Otras épicas (dependencias) | 11 RF |
| **Total** | **25 requerimientos** |

#### 9.2 Conteo por tipo de requerimiento

| Tipo | Cantidad |
|------|----------|
| Requerimientos funcionales (RF) | 22 |
| Requerimientos no funcionales (RNF) | 3 |
| **Total** | **25** |

#### 9.3 Conclusión

El módulo de BI/Analítica no es una funcionalidad agregada por iniciativa propia de la propuesta. Es un componente **obligatorio** exigido por:

- Las Bases Técnicas Transversales (RT-05.25, RT-05.26, RT-14.02, RT-14.03, RT-14.04)
- El Caso 02 de Logística (indicadores OTIF, Fill Rate, Costo de Servir)
- 25 requerimientos trazables a las fuentes normativas

Su omisión constituiría una inconsistencia grave con las Bases y haría imposible la medición de los 3 indicadores estratégicos del negocio (OTIF > 95%, Fill Rate > 97%, Costo de Servir conocido y gestionable).

---

## Decisiones de Arquitectura (ADR-01 … ADR-15)

> **Apartado 7 del Subdocumento 4 (T-22) — Decisiones de arquitectura (ADR).** Registro **ADR-01 … ADR-15** en formato **MADR**, versión **v02**, estado **Aprobadas** (2026-09-05 · actualizado 2026-09-06). Marco: TOGAF · ISO/IEC/IEEE 42010 (RT-02.03) · Arquitecturas limpias.
>
> **Cambios v01 → v02 (cierre de la auditoría del Subdocumento 4).** (1) Se corrigen las cinco menciones a **Kong** en ADR-01, ADR-06 y ADR-11: la puerta de enlace decidida es **Amazon API Gateway** (D8, actualizada el 2026-09-05 para alinearse con la vista física). (2) Se incorporan **ADR-13** (puerta de enlace de servicios), **ADR-14** (plataforma de observabilidad) y **ADR-15** (gestión de secretos), que existían como decisiones lógicas sin ADR propio, incumpliendo el apartado 7 del Subdocumento 4 y RT-02.04. (3) Se reapunta el documento de origen a la lógica vigente (Subdoc. 4.1). Empresa proponente: *Pendiente de definir (nomenclatura Art. 43.3)*.
>
> **Finalidad.** Cada ADR fundamenta y defiende una elección arquitectónica con el mismo rigor que un informe de ingeniería: contexto cuantificado desde el caso, alternativas reales de mercado evaluadas, criterio de selección técnico-económico (TCO, equipo de TI de 4 personas del CLIENTE, latencia, resiliencia), decisión precisa y sus trade-offs con mitigaciones. La **trazabilidad normativa** usa códigos exactos de las Bases Técnicas Transversales (RT-cc.nn), de las Bases Administrativas (BA Art. n°) y de los capítulos del Caso 02, y se enlaza con las decisiones de la Arquitectura Lógica v6.2 (Dn) y del registro de decisiones del caso (Decisión 16.1 N°).

### Índice de decisiones

| ADR | Título | Estado | Decisión relacionada |
|---|---|---|---|
| [ADR-01](#adr-01--estilo-arquitectónico-monolito-modular-vs-microservicios) | Estilo arquitectónico: monolito modular (Django 5.x LTS / Python 3.12) | Aprobado | D5 (AL v1) |
| [ADR-02](#adr-02--conectividad-y-redundancia-wan-starlink-leo--sd-wan) | Conectividad y redundancia WAN: Starlink LEO + SD-WAN | Aprobado | Decisión 16.1 N° 26 |
| [ADR-03](#adr-03--modelo-de-despliegue-híbrido-borde-operacional-on-premise--nube-aws) | Modelo de despliegue híbrido (Art. 16) | Aprobado | D7 (AL v1) · Decisión 16.1 N° 17 |
| [ADR-04](#adr-04--persistencia-políglota-por-dominio) | Persistencia políglota por dominio (CAP) | Aprobado | D2/D4 (AL v1) · Decisión 16.1 N° 18 |
| [ADR-05](#adr-05--mensajería-asíncrona-broker-local--colas-nube) | Mensajería asíncrona: RabbitMQ local + SQS FIFO/EventBridge | Aprobado | D4 (AL v1) |
| [ADR-06](#adr-06--identidad-y-autenticación-híbrida-modelo-b) | Identidad híbrida (Modelo B): Keycloak | Aprobado | D6 (AL v1) · Decisión 16.1 N° 34 |
| [ADR-07](#adr-07--estrategia-de-movilidad-de-terreno-nativa-android) | Movilidad de terreno: nativa Android (Kotlin) | Aprobado | Decisión de proyecto N° 19 |
| [ADR-08](#adr-08--destino-del-wms-legado-de-2013) | Destino del WMS legado de 2013 | Aprobado | Decisión 16.1 N° 14 |
| [ADR-09](#adr-09--estrategia-de-recuperación-ante-desastres-dr) | DR: activo-pasivo warm standby multi-región | Aprobado | Decisión 16.1 N° 27 |
| [ADR-10](#adr-10--almacenamiento-on-premise-y-niveles-raid) | Almacenamiento on-premise y niveles RAID | Aprobado | Decisión 16.1 N° 28 |
| [ADR-11](#adr-11--integración-b2b--edi-con-supermercados) | Integración B2B/EDI: hub GS1 con capa anticorrupción | Aprobado | RF-12 · RF-01.10 |
| [ADR-12](#adr-12--absorción-del-peak-de-septiembre-y-perfil-no-plano) | Absorción del peak de septiembre (cómputo elástico) | Aprobado | Decisión 16.1 N° 30 |
| [ADR-13](#adr-13--puerta-de-enlace-de-servicios-amazon-api-gateway) | Puerta de enlace de servicios: Amazon API Gateway | Aprobado | D8 (AL v6.2) |
| [ADR-14](#adr-14--plataforma-de-observabilidad-única-otel--amp--cloudwatch--x-ray) | Observabilidad: plataforma única con emisión on-premise | Aprobado | D14 (AL v6.2) |
| [ADR-15](#adr-15--gestión-de-secretos-servicio-administrado-en-lugar-de-gestor-autoalojado) | Gestión de secretos: servicio administrado | Aprobado | D13 (AL v6.2) · SEC-01 |

### ADR-01 — Estilo Arquitectónico: Monolito Modular vs. Microservicios

- **Estado:** Aprobado
- **Fecha:** 2026-09-05
- **Decisiones relacionadas:** D5 (Arquitectura Lógica, 2026-09-03, confirmada 09-04); **D8 (Amazon API Gateway, actualizada 2026-09-05 — ver ADR-13)**; **D14 (observabilidad de plataforma única, 2026-09-06 — ver ADR-14)**.
- **Trazabilidad normativa:** BTT **RT-02.02** (arquitectura modular, fronteras explícitas, despliegue independiente de componentes críticos) · BTT **§2.3** (la **sofisticación no reemplaza la pertinencia**: microservicios sin volumen que los justifique = error de ingeniería) · **RT-02.01** (8 capas) · **RT-02.03** (ISO/IEC/IEEE 42010) · **RT-09.05** (cuello de botella) · **BA Art. 16** (híbrido) · Caso 02 Cap. 14.2/15 (volumetría) · **RNF-19.01–04** (capacidad, escalado, cuello de botella, pruebas 1,5×).

#### 1. Contexto y Problema
La carga del caso es transaccional y concentrada, pero **no plana**: ~31.000 pedidos/mes y 260.000 líneas/mes sobre 14.200 clientes y 8.400 productos, con un **peak de ~105 TPS** en la ventana de despacho (dimensionamiento: ~20 TPS confirmación de picking con 120 terminales, ~8 TPS preventa, ~35 TPS movimientos + sincronización, burst ×3). Pérdidas operacionales traducibles a dinero: conteo cíclico con 2,3 % de diferencia, merma por vencimiento 1,7 % del inventario, OTIF 82,4 % contra meta 95 % y $4,2 millones/mes de descuadre de caja. El equipo de TI del CLIENTE tiene **4 personas** para operar la solución completa durante 36 meses de Operación.

#### 2. Alternativas Evaluadas
| Alternativa | Descripción | Soporte a escala (~105 TPS) | Equipo de 4 TI | Complejidad de operación | Rechazo/Aceptación |
|---|---|---|---|---|---|
| **A. Monolito modular (Django 5.x LTS, Python 3.12)** | Único despliegue de proceso con módulos internos (apps Django por dominio: WMS, preventa, distribución, trazabilidad, portal), **Amazon API Gateway** en la frontera (ADR-13), workers Celery para asincronía | Suficiente: 6 tareas Fargate en peak absorben 105 TPS con headroom ×1,5 | 1 framework, 1 lenguaje, 1 artefacto CI/CD; curva de reposición corta | Baja: un despliegue por ambiente, rollback simple, observabilidad OTel única | **Ganadora** |
| **B. Microservicios en Kubernetes (EKS)** | 20+ servicios acoplados a lo operacional (bodega, reparto, preventa, telemetría, facturación), mesh Istio, 3+ nodos por AZ | Sobra capacidad operativa para 105 TPS | Inviable: cluster operado por 4 personas (9–13 planos de control, versionado de contratos, backing services por dominio) | Alta: 2-3 SRE dedicados, curva de despliegue semanal, lock-in de operadores | Rechazada (BTT §2.3: volumen no la justifica) |
| **C. Monolito "clásico" sin límites de módulos (refactor del WMS 2013)** | Continuidad sobre el monolito actual sin fronteras de contexto ni despliegue independiente | Cumple hoy, no escala a multi-sitio | N/D (proveedor desaparecido, sin soporte) | Alta (deuda estructural) | Rechazada (viola RT-02.02) |

#### 3. Criterio de Selección y Justificación Técnica-Económica
- **Escala real (BTT §2.3):** para 31.000 pedidos/mes y **105 TPS de diseño**, el costo de coordinación de 20 servicios supera cualquier ganancia. El umbral donde los microservicios se justifican (típicamente >10³–10⁴ TPS, equipos de 5+ por dominio) está **dos órdenes de magnitud** por encima del caso.
- **Equipo de 4 personas (RT-02.02/RT-02.03):** un monolito modular tiene **1 artefacto, 1 pipeline, 1 proceso**: la reposición de personal y la mantención son lineales. EKS exige 9–13 componentes de plano de control (Kube-apiserver, etcd, Ingress, autoscaler, RBAC, CNI, mesh…) más 20 servicios; el costo fijo de operarlo supera al de la nube usada.
- **Despliegue independiente (RT-02.02):** la modularidad del monolito se materializa en **procesos y tareas separables** —tarea `portal` (canal moderno, hito enero 2029), workers Celery (`celery-reconciliation`, `celery-erp-sync`), shipper de colas— que escalan y se despliegan de forma independiente sin particionar el dominio.
- **TCO (56 meses):** A y B convergen en cómputo AWS, pero B agrega ~3 nodos EKS dedicados (≈ USD 1.200–1.600/mes) + SRE; A escala con Fargate (2→6 tareas) solo en septiembre (ADr-12). El diferencial B−A se estima en **USD 40.000–70.000 en 56 meses** por infraestructura y soporte, sin beneficio funcional neto.
- **Latencia/resiliencia:** el monolito modular en nube + borde local (ADR-03) cumple RNF-05.01 (≤1 s) y RNF-02.01 (24 h) porque lo que corre local es el mismo kernel WMS; particionar en servicios no aporta resiliencia adicional y añade saltos de red.

#### 4. Decisión Adoptada
**Monolito modular en Django 5.x LTS** sobre **Python 3.12**, con apps Django por dominio y límites de contexto explícitos (fundamentos de DDD y módulos de la Arquitectura Lógica v1), desplegado en **ECS Fargate** (tarea `web` + tarea `portal` + workers Celery), con **Amazon API Gateway** (D8 · ADR-13), observabilidad **OpenTelemetry sobre plataforma única en nube** (D14 · ADR-14) y borde local por sitio (ADR-03). Los módulos **críticos** (WMS offline, shipper de reconciliación, workers ERp-sync, tarea portal) se despliegan **de forma independiente** en procesos separados, satisfaciendo RT-02.02 sin adoptar microservicios.

#### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| Riesgo de acoplamiento entre apps si no se respetan los límites | Deuda estructural intrínseca al monolito | Architecture Fitness Functions (ArchUnit/Django: contratos de módulo) en CI; revisión por módulo (RT-02.01) |
| Un fallo de proceso puede amplificarse a todo el despliegue | Golpe de blast radius mayor que en microservicios | Separación en tareas/workers; health checks ALB; retry/backoff; observabilidad por `transaction_id` (D9) |
| Escalado vertical limitado del monolito | El peak se absorbe con más réplicas de la misma imagen | Auto-scaling predictivo+reactivo del peak de septiembre (ADR-12, 2→6 tareas) |
| Menor "trendiness" frente a la evaluación técnica | La BTT §2.3 **penaliza** microservicios injustificados | Documentación explícita del análisis de escala/TCO (este ADR) como evidencia de pertinencia |

### ADR-02 — Conectividad y Redundancia WAN: Starlink LEO + SD-WAN

- **Estado:** Aprobado
- **Fecha:** 2026-09-05
- **Decisión relacionada:** Decisión 16.1 N° 26 (redundancia de enlace de cada sitio).
- **Trazabilidad normativa:** BTT **RT-03.17** (enlace redundante con caminos y proveedores distintos, conmutación ≤ 5 min) · **RT-03.10** (autonomía 24 h) · **RT-03.19** (edge) · **RNF-13.01** (autonomía 24 h CD / 14 h terreno) · **RNF-13.07** (enlace redundante ≤ 5 min) · **RNF-13.08** (ancho de banda dimensionado) · **RT-10.05** (ventana crítica 05:30–07:00, indisponibilidad cero) · Caso 02 §6.12/§8 (cortes de fibra, Concepción sin respaldo, Los Ángeles sin señal en madrugada) · BA Art. 16.

#### 1. Contexto y Problema
La operación depende del enlace de datos en horarios en que no existe plan manual (Restricción N° 1: **indisponibilidad cero 05:30–07:00**). Verificado en el caso:
- **Talca:** fibra se corta **4 veces al año** sin enlace de respaldo; la bodega debe aguantar 24 h sin enlace.
- **Concepción:** no tiene respaldo alguno.
- **Cross-docks (Curicó, Chillán, Los Ángeles):** conectividad exclusivamente por red móvil; **Los Ángeles pierde señal intermitentemente entre las 03:00–05:00**, exactamente su ventana de operación de 3 h.
- Impacto económico: un día sin despacho de la mañana = operación caída (96 camiones).

#### 2. Alternativas Evaluadas
| Alternativa | Descripción | Cobertura Los Ángeles 03:00–05:00 | Cumple RT-03.17 (≤5 min, caminos distintos) | Costo 56 meses (referencial) | Rechazo/Aceptación |
|---|---|---|---|---|---|
| **A. Fibra + LTE + Starlink LEO con SD-WAN (tri-camino)** | Starlink como principal en cross-docks y respaldo en CDs; LTE dual (2 proveedores); SD-WAN con conmutación automática y BGP | Cobertura confirmada por constelación LEO (independiente de torres 4G) | Sí: 3 caminos, 2 proveedores LTE distintos + satelital | CAPEX $2.012.500 CLP + OPEX $50.400.000 CLP (56 m) = **$52.412.500 CLP (~USD 58.236)** (cotización 5 sitios) | **Ganadora** |
| **B. Fibra + LTE 4G puro** | Redundancia solo terrestre (fibra + 4G/Cat-12 femto backhaul) | No: en Los Ángeles la torre 4G falla justo en la ventana | Parcial: dos caminos pero el radio comparte tecnología física de torres | Sin CAPEX satelital; LTE puro ~USD 20–30 K en 56 m | Rechazada (no cierra el caso Los Ángeles ni el "sin red de respaldo" de Concepción) |
| **C. Satélite GEO tradicional (VSAT)** | Enlace de órbita geoestacionaria | Latencia 500–700 ms de ida y vuelta; débil en lluvia | Sí en camino, pero RTT penaliza RT-03.11/RNF-05.01 | Superior a LEO (equipos terminales GEO) | Rechazada (latencia y costo) |

#### 3. Criterio de Selección y Justificación Técnica-Económica
- **Riesgo funcional:** el único escenario que B no resuelve —señal móvil intermitente en Los Ángeles 03:00–05:00— es el que el caso declara crítico. La alternativa A aporta un **camino físicamente independiente de las torres 4G** (constelación LEO) y de las trincheras de fibra.
- **RT-03.17/RNF-13.07:** conmutación automática ≤ 5 min por diseño SD-WAN (detección de pérdida < 5 s, failover < 30 s según práctica de diseño del sitio); la redundancia de caminos es de física distinta (fibra → satelital → LTE), no solo de proveedor.
- **Ventana crítica (RT-10.05):** el despacho 05:30–07:00 no depende de un único medio; el tri-camino convive con la autonomía local de 24 h (RNF-13.01) para el caso de pérdida total (RT-03.10).
- **TCO:** la oferta Starlink (5 sitios, 56 meses) es **USD ~58.236**; frente a LTE puro que **no cumple el requisito**, el costo se justifica como prima de resiliencia del servicio crítico (costo de un día sin despacho >> costo del enlace). FinOps: CAPEX unitario bajo ($350.000 CLP/kit), reposición 15 % por ciclo de vida (RT-08.13).
- **Equipo de 4 TI:** Starlink Enterprise gestionado (cero mantención de infraestructura de radio), SD-WAN con políticas centralizadas; sin ingeniería de redes satelitales in-house.

#### 4. Decisión Adoptada
**Tri-camino WAN por sitio con SD-WAN:** (1) fibra (enlace principal en Talca y Concepción), (2) **Starlink Enterprise LEO** —principal en los 3 cross-docks (Curicó, Chillán, Los Ángeles) y respaldo automático en los 2 CD— y (3) **LTE dual** (2 proveedores) con módulo 4G Cat-12. Conmutación automática < 30 s entre caminos (sección de Arquitectura de Despliegue de este documento, §2) y con planes/precios **declarados en la oferta** (T-11 C27 · T-12 RT-08.13). Los cross-docks salen por Starlink directo a SQS/IoT/SSM (configuración crítica) y sincronizan detalle a Talca por AMQPS entre brokers (RT-03.11).

#### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| Costo recurrente de planes Starlink | La prima de conectividad satelital es el mayor gasto de red | Planes tier por sitio (1 TB CDs / 500 GB cross-docks); revisión trimestral FinOps (RT-03.06) |
| Skyline/interferencia puntual en cielos despejados (lluvia fuerte) | Degradación momentánea de throughput | SD-WAN con conmutación por política; LTE como tercer camino independiente |
| Dependencia de tarifas/dólar en 56 meses (TCM USD 900 CLP) | Variación cambiaria en OPEX | Cotización con supuesto de reposición y cláusula de revisión de tarifas; registro en supuestos |
| Sostenimiento de 5 kits (RT-08.13) | Gestión de repuestos | 15 % de reposición cotizado; ciclo de vida declarado en la sección de Emplazamiento e inventario de este documento |

### ADR-03 — Modelo de Despliegue Híbrido: Borde Operacional On-Premise vs. Nube AWS

- **Estado:** Aprobado
- **Fecha:** 2026-09-05
- **Decisiones relacionadas:** D7 (AL v1: híbrido + multi-zona + IaC + Zero Trust); Decisión 16.1 N° 17 (asignación de componentes).
- **Trazabilidad normativa:** **BA Art. 16.1–16.4** (híbrido obligatorio, carga principal en nube, criterios 16.2, exigencias 16.3/16.4) · **RT-03.01** (región primaria/secundaria) · **RT-03.02** (multi-AZ) · **RT-03.10** (autonomía) · **RT-03.19** (edge) · **RNF-02.01** (24 h) · **RNF-05.01** (≤ 1 s en cámara) · **RNF-05.02** (guantes −22 °C) · Caso 02 Cap. 6 (cámara sin cobertura) y Cap. 16.1.

#### 1. Contexto y Problema
Tres hechos confluyen: (a) el Art. 16 exige **carga principal en nube pública + componentes on-premise** (inadmisible solo-nube o solo-on-prem); (b) la cámara de congelado a **−22 °C no tiene cobertura de señal** y el picking exige **≤ 1 s** de confirmación (RNF-05.01), inviable con RTT de 40–80 ms hacia la nube más procesamiento remoto; (c) la bodega debe operar **24 h sin enlace** (RNF-02.01/RT-03.10). El perfil de carga es nocturno (22:00–06:00) y de madrugada (05:30–07:00).

#### 2. Alternativas Evaluadas
| Alternativa | Descripción | RT-03.10 (24 h) | RNF-05.01 (≤1 s) | Art. 16.1 (carga en nube) | Rechazo/Aceptación |
|---|---|---|---|---|---|
| **A. Híbrido: WMS maestro on-prem + borde por sitio + nube AWS (carga principal)** | WMS y BD transaccional en Talca (maestro), borde edge en Concepción y cross-docks, nube para OLTP cloud, canal moderno, analítica, IoT, respaldo inmutable | Sí (autonomía local 24 h CD / 14 h terreno) | Sí (confirmación en el dispositivo local) | Sí | **Ganadora** |
| **B. Solo nube (WMS en AWS)** | Toda la operación en la nube | No: sin enlace, bodega muere en minutos | No: RTT + procesamiento no sostiene ≤1 s en cámara | No (no es híbrida) | **Inadmisible** (BA Art. 16) |
| **C. Solo on-premise (WMS maestro + todo local)** | Centro de datos propio con todo el cómputo | Sí | Sí | No (no es híbrida) | **Inadmisible** (BA Art. 16) |

#### 3. Criterio de Selección y Justificación Técnica-Económica
- **Cumplimiento normativo:** solo A satisface Art. 16 en sus cuatro numerales (16.1 híbrido, 16.2 justificación por componente, 16.3 exigencias de nube, 16.4 exigencias on-premise). La tabla maestra de emplazamiento es la **sección (a) de este documento** (36 componentes).
- **Latencia (RNF-05.01):** el borde local ejecuta la confirmación de picking en el propio sitio; la alternativa nube añade ≥40–80 ms RTT y procesamiento remoto, por encima del umbral de 1 s en la cámara.
- **Autonomía (RNF-02.01/RT-03.10):** el diseño del caso exige supervivencia sin enlace; el maestro local con réplica cloud (DMS CDC, RPO ≤ 15 min) da continuidad (ADR-09) sin depender de la WAN durante el corte.
- **TCO/equipo:** el cómputo local se acota a lo imprescindible (23 componentes on-premise/híbrido), el resto se delega a servicios administrados AWS (ADR-12) — menor costo fijo que un DC propio y menor riesgo que una operación 100 % nube.
- **Carga principal en nube (Art. 16.1):** canal moderno (portales), OLTP cloud, ingesta IoT, analítica/BI, respaldo inmutable y DRP viven en AWS (sa-east-1, DRP us-east-1 — RT-03.01).

#### 4. Decisión Adoptada
**Arquitectura híbrida obligatoria con borde operacional on-premise:** WMS maestro + BD transaccional en Talca (VM-01/VM-02), edge autónomo en Concepción (VM-C01/VM-C02), mini-WMS en cross-docks (E-01), y máxima utilización de AWS administrado (ECS Fargate, Aurora, DynamoDB, IoT Core, S3, Redshift/QuickSight) para la carga principal. Detalle por componente en la **sección (a) de este documento**.

#### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| Dos dominios operativos que mantener (on-prem + nube) | Mayor superficie que la nube pura | IaC total (RT-03.03), SSM Agent (gestión sin puertos entrantes), Zero Trust (D7) |
| El maestro local exige administración de BD/hardware | Costo de operación on-premise | Dimensionamiento con headroom ×1,5 y RAID 10 (ADR-10); NOC 24×7 (RNF-21.01) |
| La identidad debe sobrevivir offline | Despliegue de caché local de solo lectura | Modelo B (ADR-06), sin maestro local a promover |
| La réplica cloud aumenta costos de AWS | DRP por réplica continua | Aurora replicada solo para lo crítico (A-01/A-02); respaldos 3-2-1-1-0 (ADR-09) |

### ADR-04 — Persistencia Políglota por Dominio

- **Estado:** Aprobado
- **Fecha:** 2026-09-05
- **Decisiones relacionadas:** D2 (series de tiempo condicionadas al muestreo, consolidado en OLAP); D4 (nube AWS + PostgreSQL/Redis/Aurora/DynamoDB/S3+Redshift); Decisión 16.1 N° 18 (motor por dominio, RT-05.02).
- **Trazabilidad normativa:** BTT **RT-05.02** (paradigma, garantías transaccionales y posición CAP por dominio) · **RT-05.01** (diccionario de datos) · **RT-05.11–05.15** (migración/volúmenes) · **RNF-09.01** (retiro < 2 h) · **RNF-09.02** (retención 5 años) · **RNF-11.02** (OLAP desacoplado del OLTP) · RSA **D.S. 977/96** (retención legal de trazabilidad) · Caso 02 Cap. 16.1/16.2 y Cap. 4.9.

#### 1. Contexto y Problema
Cada dominio tiene exigencias distintas de consistencia, volumen y retención: pedidos/inventario/trazabilidad demandan **ACID** y reconciliación determinista tras cortes; la ingesta de sensores y telemetría es **escritura masiva de baja latencia**; las series de tiempo (temperatura de cámara y camión) requieren compresión y consulta por rango; la analítica exige columnar separado para no degradar picking; y la retención sanitaria impone **5 años de trazabilidad** (piso legal) con 6 meses adicionales por vida útil. Un único motor no puede cumplir las cuatro posiciones CAP sin sacrificar desempeño.

#### 2. Alternativas Evaluadas
| Dominio | Alternativa A | Alternativa B | Alternativa C | Ganador |
|---|---|---|---|---|
| Transaccional (pedidos, inventario, trazabilidad, facturación) | PostgreSQL ACID (CP) | MySQL | MongoDB (AP) | **A — PostgreSQL** (CP: consistencia inmediata exigida por operación offline y reconciliación) |
| OLTP cloud + réplica DRP WMS | Aurora PostgreSQL | RDS MySQL | DocumentDB | **Aurora** (administrado, failover <30 s, PITR 35 días, réplica WAL) |
| IoT raw (senores, telemetría) | DynamoDB (AP) | PostgreSQL puro | Kafka+Elasticsearch | **DynamoDB** (escritura serverless <10 ms p99, TTL 30 días) |
| Series de tiempo (frío) | **Capa OLAP: S3 Parquet + Redshift Serverless (columna)** | InfluxDB | Particionado manual | **OLAP (S3+Redshift)** (adoptado según muestreo — D2; sin segundo motor; consolidado 5 años) |
| Analítica / BI / lake 5 años | S3 + Redshift Serverless + QuickSight | Snowflake | Athena sobre S3 puro | **S3+Redshift+QuickSight** (columnar desacoplado, RNF-11.02) |
| Retención legal / respaldo inmutable | S3 Object Lock / Glacier + Backup Vault | Cinta/tape local | NAS local puro | **S3 Object Lock/Glacier** (inmutabilidad WORM, custodia RT-06.26+27) |

#### 3. Criterio de Selección y Justificación Técnica-Económica
- **RT-05.02 y CAP:** la posición se declara por dominio: transaccional **CP** (consistencia inmediata; la operación offline y la reconciliación vuelta a línea lo exigen), IoT raw **AP** (eventual, TTL corto), series de tiempo **AP columnar en la capa OLAP**, analítica **AP columnar**. Declarar la posición evita el error de elegir un motor "para todo".
- **Volumen (RT-05.15):** ~31.000 pedidos/mes, 260.000 líneas, 2,4 M unidades y telemetría de 28 sensores + 18 termógrafos → persistencia manejable en PostgreSQL (índices + PostGIS para georreferencia de rutas) con DynamoDB absorbiendo el pico de IoT sin saturar el transaccional (RNF-11.02).
- **Trazabilidad (RNF-09.01/09.02, D.S. 977/96):** el registro de eventos por lote (EPCIS GS1, decisión 16.1 N° 35) se conserva en PostgreSQL (5 años) y su respaldo inmutable replica el piso legal; la réplica Aurora da RPO ≤15 min.
- **Equipo de 4 TI:** tres motores administrados o de bajo mantenimiento (PostgreSQL/Aurora, DynamoDB, Redshift Serverless) — sin motores dedicados exóticos (InfluxDB descartado: segundo motor a operar, D2). La serie de tiempo consolidada no requiere un motor adicional: vive en la capa OLAP (S3 Parquet → Redshift).

#### 4. Decisión Adoptada
**Persistencia políglota por dominio:** PostgreSQL+PostGIS (transaccional WMS on-premise, CP), Aurora PostgreSQL (OLTP cloud + réplica DRP, failover <30 s), DynamoDB (IoT raw, TTL 30 días, AP), S3 (lake analítico 5 años) con Redshift Serverless y QuickSight (OLAP, incluye la serie de tiempo consolidada de temperatura), y S3 Object Lock/Glacier + Backup Vault para retención legal inmutable (RSA D.S. 977/96). La matriz CAP está declarada y trazada a RT-05.02 en este documento (sección de Datos, ADR-04).

#### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| Consistencia fuerte en el transaccional limita escalado horizontal de escritura | El volumen (~105 TPS) no lo justifica | Réplicas de lectura (2 Aurora readers) y partición lógica por instalación (RF-02.01/02.02) |
| DynamoDB eventual abre ventanas de lectura inconsistente cortas | Telemetría no es crítico de negocio | TTL 30 días + consolidado en la capa OLAP (S3 Parquet/Redshift, 5 años) con validación de rango |
| Amazonas de datos (S3) requiere gobierno | Costo y gobernanza del lake | Glue + catálogo y QuickSight con modelos aprobados; FinOps (RT-03.06) |
| Integración entre motores exige ETL | Latencia de analítica != OLTP | Batch nocturno y distribución de datos por dominio (RT-05.01) |

### ADR-05 — Mensajería Asíncrona: Broker Local (RabbitMQ) + Colas Nube (SQS FIFO / EventBridge)

- **Estado:** Aprobado
- **Fecha:** 2026-09-05
- **Decisión relacionada:** D4 (AL v1, capa de mensajería); shipper en VM-03 (D-AL-03).
- **Trazabilidad normativa:** BTT **RT-02.06** (idempotencia) · **RT-02.07** (deduplicación) · **RT-03.12** (sincronización/reconciliación tras reconexión) · **RT-03.10** (autonomía) · **RNF-07.01** (sincro < 10 min) · **RNF-13.01** (24 h) · Zero Trust (BA Art. 21) · Caso 02 Cap. 16.1 (reglas de reintento/devolución).

#### 1. Contexto y Problema
El caso exige **orden estricto y sin pérdida** en la cadena pedido→despacho→cobranza (una línea de preventa fuera de orden rompe la reconciliación determinista), pero la operación transcurre **offline**: bodega 24 h, terreno 14 h. Además, todo el tráfico debe ser **outbound** (Zero Trust: sin conexiones entrantes al on-premise). REST síncrono no sobrevive a un corte a mitad de ventana; Kafka aporta orden y durabilidad pero exige operación y no resuelve el broker local por sitio.

#### 2. Alternativas Evaluadas
| Alternativa | Orden estricto | Buffer offline 24 h | Zero Trust (outbound) | Equipo de 4 TI | Rechazo/Aceptación |
|---|---|---|---|---|---|
| **A. RabbitMQ local + SQS FIFO/EventBridge (nube), shipper** | SQS FIFO por `group_id` (pedido/entidad) garantiza orden | RabbitMQ 24 h (~3 M mensajes) en cada sitio | Shippper VM-03 publica por HTTPS/443 (VPC Endpoint SQS), sin entrantes | RabbitMQ es maduro y liviano; SQS/EventBridge administrados | **Ganadora** |
| **B. Kafka (clúster local + MSK nube)** | Orden por partición | Posible local, pero requiere clúster mínimo 3 brokers por sitio | Requiere conectividad zookeeper/plano de control | Elevada: 3+ brokers por sitio + MSK; operación de retención y rebalances | Rechazada (escala y operación no la justifican) |
| **C. REST síncrono puro** | N/D | No: cae con la WAN | Parcial | Baja | Rechazada (viola RT-03.10/RNF-13.01) |

#### 3. Criterio de Selección y Justificación Técnica-Económica
- **Resiliencia (RT-03.10/RNF-13.01):** el broker local retiene transacciones y telemetría durante el corte y las reproduce al reconectar; el shipper publica en **orden cronológico e idempotente** (idempotency keys, RT-02.06/02.07) a la cola FIFO.
- **Reconciliación determinista (RT-03.12):** `celery-reconciliation` procesa la cola al recuperar el enlace; claves de idempotencia evitan duplicados (RT-02.07) y el orden de publicación por entidad garantiza consistencia en el maestro.
- **Zero Trust (BA Art. 21):** SQS FIFO se consume via VPC Endpoint SQS/PrivateLink (HTTPS/443); AMQPS 5671 queda solo entre brokers on-premise (cross-dock → Talca). No se abren puertos entrantes.
- **TCO/equipo:** RabbitMQ (este) + SQS/EventBridge (administrados) > Kafka (+MSK) para 105 TPS; el costo operativo de operar clústeres Kafka en 5 sitios es desproporcionado para 4 personas.

#### 4. Decisión Adoptada
**Capa de mensajería híbrida:** RabbitMQ (A-03) como broker de colas offline en cada sitio (buffers 24 h), con **shipper en VM-03 (modo `wms_only`)** que publica el buffer hacia **SQS FIFO** (VPC Endpoint / HTTPS 443) con idempotencia; **EventBridge** como bus de eventos de negocio (eventos que disparan ERP-sync, alertas, auditoría) y **AWS IoT Core (MQTT)** para la ingesta edge (ADR-04/ADR-12). Workers `celery-reconciliation` y `celery-erp-sync` procesan en nube. Declarado en la sección de Arquitectura de Integración de este documento (§5, ADR-05).

#### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| Dos brokers (local/nube) con estrategias distintas | Más superficie que un solo bus | Contratos de eventos versionados (AsyncAPI, RT-05.16/17); matriz de integración (sección de Integración de este documento, §6) |
| Posible duplicado en el flujo local→nube | Garantías "at-least-once" | Idempotency keys + procesamiento deduplicado (RT-02.06/07); buffer con ACK solo tras commit exitoso |
| Volume de mensajes en septiembre (2×) | Crecimiento de cola | SQS y broker dimensionados; auto-escalado de workers (ADR-12) |
| Kafka descartado | Menor capacidad de reprocesamiento histórico | S3 como foso de eventos (reproceso por replays controlados, ADR-04) |

### ADR-06 — Identidad y Autenticación Híbrida (Modelo B): Keycloak IdP Maestro en Nube + Caché Local de Solo Lectura

- **Estado:** Aprobado
- **Fecha:** 2026-09-05
- **Decisiones relacionadas:** D6 (AL v1, 2026-09-04: Keycloak IdP maestro, Modelo B); Decisión 16.1 N° 34 (credenciales de usuarios externos sin correo).
- **Trazabilidad normativa:** BTT **RT-12.10** (aprovisionamiento ≤ 24 h) · **RT-12.11** (autenticación en perfil operacional: guantes, rotación 38 %, dispositivos compartidos) · **RT-12.12** (credenciales de externos sin correo) · **RT-03.10**/RNF-13.01 (offline 24 h CD / 14 h terreno) · **BA Art. 22** (MFA para acceso externo) · **RF-15.01–15.05** (identidad centralizada) · **RF-06.08** (OTP conductores externos ≤ 2 min) · Caso 02 Cap. 16.1 N° 34.

#### 1. Contexto y Problema
La operación exige autenticación **incluso sin enlace**: la bodega trabaja 24 h y el terreno 14 h desconectados, con 62 preventistas y ~200 conductores (de 10 transportistas externos) **sin correo corporativo**, dispositivos compartidos entre turnos y rotación de personal de preparación de 38 % anual. Un IdP solo-nube paraliza la bodega ante un corte; un maestro local tradicional (AD) duplica la administración de identidad y crea un maestro a promover.

#### 2. Alternativas Evaluadas
| Alternativa | Offline 24 h/14 h | Externos sin correo (OTP) | Un solo maestro (sin promoción) | Rechazo/Aceptación |
|---|---|---|---|---|
| **A. Keycloak IdP maestro en nube (ECS Fargate) + caché local de solo lectura TTL 8 h + offline tokens (8 h/14 h)** | Sí (validación local de firma OIDC) | Sí (OTP emitido por jefe de flota, RF-06.08) | Sí (Modelo B, D6) | **Ganadora** |
| **B. IdP nube puro (ej. Cognito-only)** | No: sin red, sin autenticación | Parcial (depende de conectividad) | Sí | Rechazada (paraliza CD/terreno, RT-03.10) |
| **C. Active Directory tradicional on-premise** | Sí | Parcial (sin flujo OTP para externos sin dominio) | No: maestro local a promover en DR | Rechazada (complejidad de federación + DR de identidad) |
| **D. Cognito como dependencia** | No | Parcial | — | Rechazada (D6: Cognito solo alternativa; descendencia de dependencia) |

#### 3. Criterio de Selección y Justificación Técnica-Económica
- **Autonomía (RT-03.10/RNF-13.01):** la caché local (A-05: VM-05 Talca, VM-C03 Concepción) valida localmente la **firma OIDC** y mantiene sesiones hasta 24 h CD / 14 h terreno; el token offline se renueva al inicio del turno en cobertura, de modo que la ventana offline siempre cubre la jornada (8 h bodega / 14 h reparto-preventa) **sin autenticación en ruta**.
- **Autoridad única (D6):** todas las escrituras viven en el IdP maestro de la nube; los cambios de alta/baja/roles se propagan por **export/import del Realm cifrado vía S3 (outbound)** con Δ ≤ 8 h (TTL) y baja efectiva SCIM ≤ 24 h (RT-12.10). No existe maestro local a promover ⇒ **DR de identidad = misma autoridad en nube** (no depende de switchover).
- **Externos (RT-12.11/12.12):** OTP de un solo uso para conductores (RF-06.08, ≤ 2 min, sin correo) y credencial inicial en sesión de dotación; MFA para todo acceso externo y privilegiado (Art. 22).
- **Equipo de 4 TI:** Keycloak administrado (Fargate) + federación OIDC con **Amazon API Gateway** (ADR-13); sin sincronización de directorio propietario.

#### 4. Decisión Adoptada
**Modelo B de identidad (D6):** **Keycloak IdP maestro en AWS (ECS Fargate, 2 tareas Multi-AZ, backend Aurora)** con **caché local de solo lectura TTL 8 h** en VM-05/VM-C03 y **offline access tokens por perfil** (8 h bodega, 14 h reparto/preventa). Sincronización del Realm cifrado por S3 (outbound, Zero Trust); MFA OIDC para externos; OTP para conductores externos. Declarado en la sección de Arquitectura de Seguridad de este documento (§4, ADR-06).

#### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| Revocación no es inmediata en el borde (Δ ≤ 8 h TTL) | Ventana de revocación por TTL | SCIM ≤ 24 h; baja reforzada por matrícula de activos y MDM (bloqueo de terminal) |
| El Realm viaja por S3 (outbound) | Exposición del cifrado durante el traslado | Cifrado KMS del objeto; solo lectura de cachés; sin claves privadas locales |
| OTP para externos depende del jefe de flota | Fricción en cambio sin aviso | Emisión previa a la ventana; listado de contingencia; rotación diaria (RF-12.21) |
| Falla del IdP maestro deja sin altas/bajas | Degradación administrativa | Identidad en nube multi-AZ + us-east-1 DRP (ADR-09); las evaluaciones locales siguen operando |

### ADR-07 — Estrategia de Movilidad de Terreno: Aplicación Nativa Android (Kotlin)

- **Estado:** Aprobado
- **Fecha:** 2026-09-05
- **Decisión relacionada:** Decisión de proyecto N° 19 (nativa vs. híbrida vs. PWA).
- **Trazabilidad normativa:** BTT **RT-12.11** (autenticación en perfil operacional) · **RT-13.08** (interfaz de terreno: guantes térmicos, −22 °C, lluvia, 34 °C, una mano, turno sin conexión) · **RT-03.19** (edge) · **RNF-05.02** (guantes −22 °C) · **RNF-05.03** (curva de aprendizaje ≤ 2 h) · **RNF-06.01** (14 h sin señal) · **RF-03.02** (stock offline) · **RF-06.11/06.12/06.13** (QR/foto/impresora térmica) · Caso 02 Cap. 6 (cámara sin cobertura, turnos de 30 min).

#### 1. Contexto y Problema
El terreno es el corazón de la operación: 62 preventistas, ~200 conductores y 120 terminales de bodega operando con **guantes térmicos a −22 °C**, **a una mano durante la descarga**, bajo lluvia, sol directo y **14 h sin señal**. Requiere escáner GS1, impresora térmica Bluetooth y POS móvil (PAX), y curva de aprendizaje ≤ 2 h. Una PWA no controla el SDK de escáner Zebra de forma confiable ni persiste un turno completo sin capa nativa; una híbrida (Flutter) agrega un runtime intermedio que degrada la interacción con periféricos industriales.

#### 2. Alternativas Evaluadas
| Alternativa | Periféricos Zebra (DataWedge)/BT | Offline 14 h | UX guantes/1 mano/−22 °C | Curva ≤ 2 h | Rechazo/Aceptación |
|---|---|---|---|---|---|
| **A. Nativa Android (Kotlin), SQLite/Room + SDK Zebra DataWedge + scanner API** | Total (intent `com.symbol.datawedge`) | SQLite con sync deduplicada (RF-03.17) | Full control de la UI (botones grandes, táctil frente a guantes) | SÍ (flujos guiados) | **Ganadora** |
| **B. PWA (canal web)** | Limitado (Web Bluetooth parcial, sin DataWedge nativo) | Solo Service Worker con cuotas y poca fiabilidad para cámara/escáner | Media | Parcial | Rechazada para terreno; **adoptada para autoatención** del cliente (portal) |
| **C. Híbrida Flutter/React Native** | Puentes parciales, mantención de capa nativa | Posible pero con runtime intermedio | Media | Media | Rechazada (complejidad y rendimiento de periféricos) |

#### 3. Criterio de Selección y Justificación Técnica-Económica
- **Periféricos (RT-13.08/RF-06.13):** DataWedge (intents) entrega disparo de escáner GS1, CW (camera wedge) para QR (RF-06.11) y salidas a impresora BW Zebra — integraciones nativas estables que un runtime híbrido/PWA no garantiza.
- **Offline total (RNF-06.01/RT-03.19):** SQLite/Room persiste el turno completo (pedidos, POD con foto/firma, cobros, devoluciones) y sincroniza con deduplicación e idempotencia al reconectar (< 10 min, RNF-07.01); STock indicativo con antigüedad visible (RF-02.05) y resolución cronológica de conflictos (RF-02.05e).
- **Condiciones extremas (RNF-05.02/RT-12.11):** la UI nativa permite contraste alto, botones grandes, entrada por guantes (toque grueso), sin gestos complejos; dispositivos Rugged Zebra (EC55, TC58e, MC9400 Cold Storage) con Android 13+ y baterías de cámara/5G.
- **TCO:** una misma app nativa cubre preventa, reparto y bodega (parque de terreno de la sección de Emplazamiento de este documento); el costo de mantención de la plataforma nativa se asume como trade-off frente a las exigencias RNF (documentado en este ADR-07).

#### 4. Decisión Adoptada
**Aplicación nativa Android (Kotlin)** para preventa, reparto/cobranza y picking/recepción de bodega, con persistencia local **SQLite/Room**, SDK **Zebra DataWedge** (escáner GS1 + CW QR) y módulo de impresión Bluetooth (ZQ620) y POS (PAX). PWA (web) solo para la **autoatención del canal moderno** (portal, ADR-11). Dispositivos Rugged: EC55 (preventa), TC58e (reparto), MC9400 Cold Storage (cámara −22 °C), DS2208 (andén), penalizados por guantes/una mano (RNF-05.02).

#### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| Dos stacks de UI (nativa Android + portal web) | Mayor mantención que una sola tecnología | Automatización de CI/tests (Appium), contratos API compartidos; la web cubre el canal sin offline |
| Versionado de app en parque de ~270 dispositivos (62 EC55 preventa + ~200 TC58e reparto + reservas; 174 MC9400 bodega) | Coordinación de despliegues de terreno | MDM (Gestión de Endpoints, F-03) con controles de distribución; actualizaciones en ventana sin operación |
| SQLite frente a sincronización concurrente | Conflictos de stock | Claves de idempotencia + reconciliación cronológica (ADR-05) |
| Dependencia de kits Android fabricantes (Zebra) | Ciclo de vida OS | Dispositivos con Android 13→18 Garage/Zebra; política de intercambio RT-08.13 |

### ADR-08 — Destino del WMS Legado de 2013

- **Estado:** Aprobado
- **Fecha:** 2026-09-05
- **Decisión relacionada:** Decisión 16.1 N° 14 (reemplazar el WMS de 2013).
- **Trazabilidad normativa:** **RT-05.11–RT-05.15** (plan de migración por dominio, volúmenes y reversión) · **RT-03.10**/RNF-02.01 (24 h) · **RNF-05.01** (≤1 s) · Caso 02 Cap. 16.1 N° 14 (el CLIENTE delega expresamente la decisión) y Cap. 9 (dolores: conteo 2,3 %, merma 1,7 %, rasgos de WMS 2013) · estrategia azul-verde y reversión.

#### 1. Contexto y Problema
El WMS de 2013 corre en Talca con **proveedor desaparecido** (sin soporte, sin roadmap), planillas impresas (conteo cíclico con 2,3 % de diferencia y ajustes sin investigación de causa), y no soporta multi-sitio ni operación de 24 h sin enlace. El CLIENTE **delega expresamente** en el proponente la decisión (Cap. 16.1 N° 14). Extenderlo arrastra el riesgo de fecha conocida: sin soporte, un incidente en la ventana crítica (05:30–07:00) no tendría plan B.

#### 2. Alternativas Evaluadas
| Alternativa | Multi-sitio (RF-02.01/02.02) | Offline 24 h | Soporte y riesgo | Costo | Rechazo/Aceptación |
|---|---|---|---|---|---|
| **A. Reemplazo total en la Etapa 1** | Sí (topología configurable, consolidación multi-nodo) | Sí (RNF-02.01) | Proveedor nuevo con soporte contractual; conversión controlada | Mayor CAPEX, menor riesgo de operación | **Ganadora** |
| **B. Mantener/extender el WMS 2013** | No (arquitectura monocliente sin multi-sitio) | No | Proveedor desaparecido: sin parches ni soporte, un fallo = cero plan B en ventana crítica | Bajo CAPEX, riesgo operacional alto e ilimitado | Rechazada |
| **C. Coexistencia temporal (WMS 2013 + nuevo en un sitio)** | Parcial (solo mientras dure el puente) | — | Migración en olas reduce el riesgo | Medio | Complemento de la estrategia de despliegue (azul-verde), no fin último |

#### 3. Criterio de Selección y Justificación Técnica-Económica
- **Requisitos (RF-02.x):** slotting ABC, conteo cíclico ciego, picking FEFO dirigido, SSCC GS1, trazabilidad por lote — el WMS 2013 no los contempla ni los puede incorporar sin proveedor.
- **Riesgo operacional:** un sistema sin soporte expuesto a la ventana de indisponibilidad cero (RT-10.05) es un riesgo con fecha de impacto indefinido; el análisis de riesgos del caso lo califica como inaceptable frente al CAPEX del reemplazo.
- **Migración (RT-05.11–15):** por dominio y en ventanas sin operación: maestros completos, ventas/pedidos 3 años, inventario 2 años, trazabilidad 5 años, CxC abierta; convivencia con el ERP/GDE (que no se reemplaza) vía capa anticorrupción (ADR-11).
- **Reversión y despliegue:** estrategia **azul-verde** por ola y sitio, con umbrales de marcha blanca por oleada (RT-20.02/20.04) y plan de reversión para volver al WMS 2013 sin pérdida en caso de no superar los indicadores.
- **TCO 56 meses:** el costo de reemplazo se paga en la Etapa 1 y se amortiza con la reducción de 2,3 %→~0,3 % de diferencia de conteo y 1,7 %→<1 % de merma (objetivos de RF/planilla del Cap. 18) y con OTIF 82,4 %→95 %.

#### 4. Decisión Adoptada
**Reemplazo total del WMS 2013 en la Etapa 1** por el **módulo WMS del monolito modular (ADR-01)** desplegado en Talca (maestro), Concepción (edge) y cross-docks (mini-WMS E-01), con migración por dominio (RT-05.11–15), oleadas por sitio y plan de reversión azul-verde documentado. El ERP administrativo/GDE **no se reemplaza** y se integra por la capa anticorrupción (ADR-11).

#### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| Conversión de datos en ventanas sin operación | Ventana de corte por dominio | Migración nocturna por dominio con verificación de conciliación (RT-05.12/05.14) |
| Curva de aprendizaje del personal de bodega | Riesgo operacional en cutover | Marcha blanca por ola con certificación (RT-20.02/20.04); curva ≤ 2 h (RNF-05.03) |
| El ERP sigue existiendo | Dualidad de maestros durante la cohabitación | Capa anticorrupción (ADR-11) y catálogo de equivalencias (RF-12.03) |
| Costo de migración y reversiones | CAPEX de transición | Plan de reversión por ola; pruebas de restauración mensuales (RNF-20.07) |

### ADR-09 — Estrategia de Recuperación ante Desastres (DR): Warm Standby Activo-Pasivo Multi-Región

- **Estado:** Aprobado
- **Fecha:** 2026-09-05
- **Decisión relacionada:** Decisión 16.1 N° 27 (modalidad activo-pasivo, RTO/RPO, cadencia de pruebas).
- **Trazabilidad normativa:** **RT-07.01** (declarar y justificar modalidad activo-activo vs. activo-pasivo) · **RT-07.07** (pruebas reales ≥ 2 veces/año con informe y medición de RTO/RPO) · **RNF-20.06** (RTO ≤ 4 h, RPO ≤ 15 min) · **RNF-20.07** (3-2-1-1-0) · **BA Art. 20** (continuidad y pruebas semestrales) · DRP local Talca→Concepción (RTO +1–2 h) · Caso 02 Cap. 16.1 N° 27.

#### 1. Contexto y Problema
La ventana de despacho (05:30–07:00) no admite plan manual; una falla mayor del sitio primario debe recuperar el servicio con **RTO ≤ 4 h y RPO ≤ 15 min** (RNF-20.06) y probarse con conmutación real **al menos 2 veces al año** (RT-07.07/Art. 20). El sitio primario es Talca (WMS maestro on-premise); el respaldo secundario se apoya en la nube (replicación AWS) y en el borde autónomo de Concepción como DRP local.

#### 2. Alternativas Evaluadas
| Alternativa | RTO/RPO | Complejidad operativa | Costo | Cumple RT-07.01 (justificación) | Rechazo/Aceptación |
|---|---|---|---|---|---|
| **A. Activo-pasivo warm standby multi-región (Aurora réplica DRP + DMS CDC)** | RTO ≤ 4 h / RPO ≤ 15 min | Media: promote documentado, pruebas semestrales | Réplica + DRP regional (us-east-1) | Sí | **Ganadora** |
| **B. Activo-activo (multi-maestro)** | RPO ~0 | Alta: conflictos de escritura y reconciliación continua entre nodos | 2× infraestructura transaccional + reconciliación | Justificable pero no necesario al volumen | Rechazada (costo/complejidad desproporcionados, RT-07.01) |
| **C. Backup en frío (bajo demanda)** | RTO > 24 h (restauración completa) | Baja | Baja | No cumple RTO ≤ 4 h | Rechazada |
| **D. Continuidad intrarregional en sa-east-1 (sin us-east-1)** | Falla de AZ o corrupción: RTO ≤ 4 h / RPO ≤ 15 min (multi-AZ + CDC) · **caída de toda la región sa-east-1: RTO 24–72 h** desde respaldo inmutable (S3 Object Lock/Backup Vault) | Media: restauración y rehidratación; cada 6–12 meses requiere prueba real | Réplica y respaldo solo dentro de sa-east-1; menor costo de salida que A | No cumple RTO ≤ 4 h ante falla regional (RNF-20.06) | **Contingencia condicionada**: solo si el CLIENTE rechaza la transferencia internacional (Art. 23) — no sustituye a A como plan base |

#### 3. Criterio de Selección y Justificación Técnica-Económica
- **RTO/RPO (RNF-20.06):** la réplica continua (DMS CDC) y la réplica de Aurora (WAL) mantienen RPO ≤ 15 min; el promote a la región DRP (us-east-1) más el DRP local Talca→Concepción (procedimiento documentado de 5 pasos, RTO +1–2 h) cumplen los cuatros horas.
- **RT-07.01:** activo-activo duplicaría la infraestructura transaccional y exigiría reconciliación de doble escritura (~105 TPS peak) sin beneficio medible frente al RTO comprometido; la modalidad activo-pasiva es proporcional al volumen (CAP consistente, ADR-04).
- **Pruebas (RT-07.07/Art. 20):** conmutación real semestral con informe de RTO/RPO efectivos y plan de corrección de brechas; consistente con la retención sanitaria y la operación continua.
- **Identidad (ADR-06):** el DR de identidad no exige conmutación local (el maestro está en la nube y las cachés A-05 siguen validando firmas): se elimina una clase entera de riesgos de DR.
- **Respaldo 3-2-1-1-0 (RNF-20.07):** copia primaria on-premise + réplica local (Concepción) + pierna cloud (S3 Object Lock/Backup Vault, inmutable) + offsite + prueba mensual de restauración y retención legal (ADR-04).
- **Falla de AZ vs. caída de región (alternativa D):** si el CLIENTE no aprueba la transferencia a us-east-1 (Art. 23, sección de **Arquitectura de Seguridad de este documento**, §10), la postura mínima es la continuidad intrarregional en sa-east-1: uso de la tercera AZ (sa-east-1a/1b/1c) y respaldo inmutable regional, que mantiene RTO ≤ 4 h / RPO ≤ 15 min ante **falla de una zona de disponibilidad o corrupción de datos** — lo que el multi-AZ ya brinda —, pero **no ante una caída de toda la región sa-east-1**, escenario en que la reconstrucción desde el respaldo inmutable toma **24–72 h** e incumple RNF-20.06. Esta alternativa **no usa los sitios on-premise del CLIENTE** para la carga cloud (Talca/Concepción alojan solo el dominio on-premise, con su DRP local RTO +1–2 h); y es precisamente esta degradación la que motiva solicitar la aprobación de us-east-1 con resguardos, conforme al Art. 23.

#### 4. Decisión Adoptada
**DR activo-pasivo warm standby multi-región:** replicación continua del WMS (VM-02) hacia **Aurora (ACM us-east-1 global replica)** con DMS CDC, RPO ≤ 15 min y RTO ≤ 4 h; **DRP local** Talca→Concepción (VM-C01/VM-C02) con RTO +1–2 h para la bodega; pruebas reales **2×/año** (RT-07.07) y respaldo **3-2-1-1-0** admitido por S3 Object Lock. Documentado en la sección de Arquitectura de Despliegue de este documento (§4, ADR-09). **Si el CLIENTE no aprueba la transferencia internacional (Art. 23), rige la alternativa D** (§2): continuidad intrarregional en sa-east-1 con tercera AZ y respaldo inmutable, aceptando el RTO de 24–72 h ante caída de toda la región, que es el impacto evaluado en §3.

#### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| Capacidad de cómputo ociosa en la región DRP | Costo de la réplica caliente | Aurora multi-AZ compartida con OLTP cloud; DRP us-east-1 solo componentes críticos |
| Ventana de pérdida ≤ 15 min | No cero-datos | RPO ≤ 15 min aceptado (RNF-20.06); reconciliación de vuelta (RT-03.12) |
| Pruebas de conmutación real | Riesgo de fallo durante la prueba | Ventanas de prueba con plan de reversión; indicadores medidos y corrección de brechas (RT-07.07) |
| Replicación CDC sobre enlaces WAN | Costo de ancho de banda | WAL/DMS comprimido; ventana de replicación nocturna junto a sync batch |

### ADR-10 — Almacenamiento On-Premise y Niveles RAID

- **Estado:** Aprobado
- **Fecha:** 2026-09-05
- **Decisión relacionada:** Decisión 16.1 N° 28 (declarar y justificar nivel RAID frente a alternativas).
- **Trazabilidad normativa:** BTT **RT-03.14** (tolerancia a falla de disco y nivel RAID declarado) · **RNF-13.03** (equipos críticos redundantes) · **RNF-13.04** (tolerancia a falla de al menos 1 disco) · **RNF-13.05** (justificación del nivel RAID) · Caso 02 Cap. 16.1 N° 28 y Cap. 10 (ventana crítica sin falla).

#### 1. Contexto y Problema
La BD transaccional del WMS (VM-02) concentra ~105 TPS de diseño con escritura fuerte de sincronización y trazabilidad; la evidencia fotográfica del POD, los logs y el contenido de cámara suman datos de escritura secuencial menos críticos. Una falla de disco en la ventana de despacho (05:30–07:00) no puede detener la operación. El nivel RAID debe tolerar el fallo de al menos un disco (RNF-13.04) y justificarse (RNF-13.05/RT-03.14).

#### 2. Alternativas Evaluadas
| Nivel | Tolerancia | Reescritura/desempeño | Rebuild frente a URE | Costo (utilizable) | Aplicación | Rechazo/Aceptación |
|---|---|---|---|---|---|---|
| **RAID 10** | N-1 discos por espejo (≥ 1, hasta N/2) | Excelente para IOPS de escritura | Rápido y acotado | 50 % (4–8 NVMe) | BD transaccional y réplica (VM-02, VM-C02, PMe VM-01) | **Ganadora (transaccional)** |
| **RAID 6 (doble paridad + hot-spare)** | Hasta 2 discos simultáneos | Bueno para secuencial | Rebuild más largo, pero seguro ante segundo fallo | 2/N (p.ej. 2 de 8) | Evidencia POD (fotos/firmas), logs, rollups de cámara y mini-WMS de cross-dock | **Ganadora (datos/evidencia)** |
| **RAID 5** | 1 disco | Medio | Riesgo USB de URE en rebuild a gran capacidad + sin doble redundancia | 1/N (económico) | No aplica | Rechazada (no cumple RNF-13.04 robustamente en discos grandes y rebuild) |
| **JBOD/Sin RAID** | 0 | N/D | N/D | — | — | Inadmisible (viola RNF-13.04) |

#### 3. Criterio de Selección y Justificación Técnica-Económica
- **Transaccional (RNF-13.04, RT-03.14):** RAID 10 sobre NVMe Superdome/Kioxia (sección de Dimensionamiento de este documento, §4.3) entrega >100.000 IOPS frente a ~840 IOPS necesarias (105 TPS × 8 E/S), con latencia de escritura determinista y reparación acotada — crítico en la ventana de despacho.
- **Evidencia/logs:** RAID 6 (doble paridad + hot-spare) para fotografías POD, logs y rollups; tolera el segundo fallo durante el rebuild, relevante en discos de alta capacidad y baja rotación de escritura.
- **Rechazo de RAID 5:** en discos modernos de 8–16 TB, la probabilidad de URE (uncorrectable read error) durante un rebuild extenso no es despreciable; el caso exige tolerancia a fallo de al menos un disco en operación competitiva (RNF-13.04/05) y RAID 5 solo cubre uno.
- **Coherencia con Ceph (hipervisor):** el pool Ceph N+1 de los nodos de cómputo complementa los niveles RAID de las VMs (redundancia de infraestructura, RNF-13.03); la pieza cross-dock usa contenedores con disco local del mini-PC recubierto por el respaldo nocturno (RNF-20.07).
- **TCO:** el sobre-costo del 50 % de RAID 10 solo se aplica a la BD crítica; el grueso del almacenamiento (evidencia, logs, telemetría) usa RAID 6 con solo 2 de 8 discos de paridad, manteniendo el costo de almacenamiento total contenidamente respecto de RAID 1/0 puro.

#### 4. Decisión Adoptada
**RAID 10** para los servicios transaccionales del WMS (VM-02/VM-C02 y núcleo del maestro) con NVMe, y **RAID 6 con hot-spare** para evidencia fotográfica/POD, logs y rollups de cámara; **RAID 5 descartado** y justificado frente a alternativas (RNF-13.05/RT-03.14), con redundancia de equipos críticos por hipervisor Ceph N+1 (RNF-13.03). Registrado en la sección de Dimensionamiento de este documento (§4.3) y en el emplazamiento (ADR-10).

#### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| 50 % de pérdida útil en la BD | Mayor costo de almacenamiento crítico | Solo en la capa transaccional; resto en RAID 6 |
| Rebuild de RAID 6 durante fallas | Ventana de vulnerabilidad al segundo fallo | Hot-spare + alertas NOC 24×7 (RNF-21.01) y monitoreo SMART |
| Complejidad de niveles mixtos | Operación de dos políticas | Política única de respaldo 3-2-1-1-0 (RNF-20.07) sobre ambas capas |
| Dependencia del proveedor de hardware | Reposición de discos | SLA de reemplazo ≤ 4 h para componente crítico (sección de Emplazamiento de este documento); stock ≥ 10 % parque |

### ADR-11 — Integración B2B/EDI con Supermercados: Hub GS1 Centralizado con Capa Anticorrupción

- **Estado:** Aprobado
- **Fecha:** 2026-09-05
- **Decisiones relacionadas:** RF-12 (mensajería electrónica EDI); RF-01.10 (maestro interno de productos, tabla de equivalencias por cadena); A-04 (Capa Anticorrupción del ERP).
- **Trazabilidad normativa:** BTT **RT-05.23** (estándares sectoriales de intercambio — EDI) · **RT-16.16** (documentos cifrados con integridad y retención) · **RT-16.17** (firma electrónica Ley N° 19.799) · **RNF-12.01** (canal moderno en producción antes de enero 2029) · **RF-12.03** (equivalencias GTIN por cadena) · **RF-12.06** (bandeja de excepciones) · **RF-01.10** — estándares GS1 (EANCOM/GS1 XML, EPCIS) invocados por el Caso 02 Cap. 16.2 · Caso 02 Cap. 9 (cadenas del canal moderno).

#### 1. Contexto y Problema
Los supermercados del canal moderno (p.ej. Walmart, Cencosud, SMU) exigen intercambio electrónico EDI dentro de sus ventanas de taking (pedidos, envío de guías/facturas, acuse de recibo). Hoy el caso lo resuelve por correo/telefono y con diferencias de maestro por cadena (decisión 16.1 N° 11). Conectores punto-a-punto por cadena multiplican los adaptadores, duplican la lógica de mapeo y disparan el mantenimiento ante cada cambio de especificación de la cadena; además, el ERP (que no se reemplaza) expone una frontera frágil.

#### 2. Alternativas Evaluadas
| Alternativa | Estandarización GS1 | Esfuerzo por cadena nueva | Aislamiento del ERP | Madurez del ecosistema | Rechazo/Aceptación |
|---|---|---|---|---|---|
| **A. Hub EDI centralizado (GS1) + Capa Anticorrupción (ACL)** | Mapeo único a GS1 EANCOM/GS1 XML; EPCIS para trazabilidad | Conector configurado (perfiles por cadena), sin desarrollo a medida | El ERP solo habla con la ACL (nunca escritura directa) | Estándar de la industria; validación de esquemas | **Ganadora** |
| **B. Conectores punto-a-punto por cadena** | Modelado ad-hoc por cadena | Desarrollo y pruebas por cada cadena | Frontera expuesta directamente al ERP | Baja | Rechazada (esfuerzo × cadenas y acoplamiento) |
| **C. Portal manual de documentos** | No es EDI | Descarga/upload manual | N/D | Baja | Solo complemento (bandeja e impresos de respaldo) |

#### 3. Criterio de Selección y Justificación Técnica-Económica
- **Estandarización (Cap. 16.2):** el caso exige estándares GS1; el hub declara un modelo canónico (EANCOM D.01B/GS1 XML para pedidos/despachos/facturas, EPCIS para eventos de trazabilidad) y mapea cada cadena contra el modelo, no contra el ERP.
- **Esfuerzo marginal:** una cadena nueva se agrega por **configuración de perfil** (equivalencias GTIN, RF-12.03) y pruebas de conexión, no por código; el hub centraliza la validación, el retry y la auditoría.
- **Aislamiento del ERP (ACL A-04):** el ERP (que no se reemplaza, ADR-08) queda detrás de la capa anticorrupción: `celery-erp-sync` lee contratos OpenAPI del ERP y publica notificaciones por SQS; **nunca hay escritura directa** desde una cadena al ERP (Zero Trust, BA Art. 21).
- **Plazo contractual:** el canal moderno (incluido EDI) entra en producción antes del **hito enero 2029** (RNF-12.01), por lo que la Etapa 2 concentra portal y EDI detrás de la misma puerta de enlace (**Amazon API Gateway**, ADR-13) y del hub.
- **Equipo de 4 TI:** el hub EDI se aloja como módulo del monolito (ADR-01) en la DMZ de AWS (N-01…N-03) con servicios administrados (API Gateway, SQS, EventBridge), sin adaptadores propietarios por cadena.

#### 4. Decisión Adoptada
**Hub EDI centralizado basado en GS1** (EANCOM/GS1 XML para textos, EPCIS para trazabilidad) en la nube (DMZ, `modulo integraciones` del monolito), con **conector configurable por cadena**, **tabla de equivalencias GTIN/cadena** (RF-12.03), **bandeja de excepciones** (RF-12.06) y **Capa Anticorrupción (ACL, A-04)** hacia el ERP/GDE. Canal moderno operativo ≤ enero 2029 (RNF-12.01). La evidencia POD se articula con la GDE y el acuse de recibo electrónico (RF-12.12/12.13, RT-16.17/16.18).

#### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| Dependencia de especificaciones por cadena | Cambios en el perfil de cada cadena | Versionado de contratos (AsyncAPI, RT-05.16/17) y pruebas de integración contínua contra los bancos de pruebas de cada cadena |
| El ERP sigue siendo el emisor tributario | Latencia de la GDE/factura | Acuse dentro de los 30 min de la descarga (RF-12.13); la ACL abstrae el ERP |
| Equivocaciones de GTIN por cadena | Diferencias de maestro | Equivalencias por cadena (RF-12.03) + bandeja de excepciones visible (RF-12.06) |
| Costo de la infraestructura DMZ H2 | Recursos del hub | Servicios administrados y FinOps (RT-03.06); el hub comparte la tarea `portal` (ADR-01) |

### ADR-12 — Absorción del Peak de Septiembre y Perfil de Carga No Plano

- **Estado:** Aprobado
- **Fecha:** 2026-09-05
- **Decisión relacionada:** Decisión 16.1 N° 30 (cuello de botella del peak de septiembre y estrategia).
- **Trazabilidad normativa:** BTT **RT-09.05** (identificar el cuello de botella y cómo se detecta/resuelve) · **RT-03.06** (FinOps) · **RT-03.08** (instancias reservadas/ahorro) · **RT-03.09** (cómputo serverless para carga variable) · **RNF-19.01–04** (capacidad, escalado horizontal automático, cuello de botella, pruebas 1,5×) · Caso 02 Cap. 14.2/15 (perfil no plano; congelamiento 1–25 sept) · **RT-10.05** (congelamiento de cambios en septiembre/diciembre).

#### 1. Contexto y Problema
El perfil de carga no es plano: preventa 09:00–18:00, preparación 22:00–06:00, despacho 05:30–07:00 (96 camiones), sincronización de flota 17:00–20:00, y **septiembre casi duplica el volumen durante 3 semanas** (1.400 → 2.600 entregas/día). Sobredimensionar para el promedio diario es un error declarado por el propio caso; sobredimensionar estático para el peak paga 12 meses la capacidad de 3 semanas.

#### 2. Alternativas Evaluadas
| Alternativa | Costo en régimen | Comportamiento en peak | Detección de cuello de botella | Rechazo/Aceptación |
|---|---|---|---|---|
| **A. Cómputo elástico serverless/contenedores (Fargate 2→6, Celery 2→4, Lambda, Aurora escalada)** | Pago por uso; escala solo cuando sube la carga | Auto-escalado predictivo (calendario sept/diciembre) + reactivo (CPU/cola) | Amazon CloudWatch / Prometheus; umbrales de cola y TPS visibles (RT-09.05) | **Ganadora** |
| **B. Sobredimensionamiento estático (12×2 vCPU fijo + Aurora 2×)** | Pago fijo del 100 % los 56 meses | Nunca degrada, pero se paga todo el año | Requiere monitoreo manual | Rechazada (costo: ~40–60 % más OPEX por el peak inactivo, contra FinOps RT-03.06) |
| **C. Overprovision moderado + colas más largas (sin escala automática)** | Intermedio | Los workers cuelan y la reconciliación se desplaza a horario no crítico | Parcial | Complementa a A para cargas cola (reconciliación) |

#### 3. Criterio de Selección y Justificación Técnica-Económica
- **Perfil no plano (Cap. 14.2/15):** la capacidad se calcula al **peak ×1,5** (RNF-19.04) = **3.900 entregas/día**, con ~105 TPS de diseño de despacho y pruebas de carga de **1,5×peak ≈ 160 TPS / 5.850 entregas** (RNF-19.04). Fargate 2→6 tareas (Django), Celery 2→4 y Lambda 100→500 cubren la ratio de las 3 semanas sin pago residual.
- **Cuello de botella identificado (RT-09.05):** confirmación/persistencia transaccional de pedidos e ingesta de telemetría de la flota. Se declara el punto de saturación y se vigila con métricas de negocio (OTIF, pedidos no preparados) y de infraestructura (cola SQS, CPU, TPS) — RNF-19.03.
- **FinOps (RT-03.06) y RT-03.08/03.09:** la base reservada (RI/Savings Plan) cubre la capacidad de régimen; el crecimiento del peak se paga con cómputo efímero (Fargate/Lambda). Ampliar Aurora a `xlarge` + 2 readers y DynamoDB con autoscaling absorbe el pico sin compra fija.
- **Congelamiento (RT-10.05):** del 1 al 25 de septiembre y en diciembre no se despliegan cambios; la escala predictiva se programa por calendario (calendario de eventos) y se valida en la marcha blanca de septiembre del año 1.
- **Equipo de 4 TI:** la operación es declarativa (IaC, RT-03.03): el mismo despliegue escala y decrece sin intervención manual; las políticas de alerta de desviación de presupuesto (RT-03.06) sustituyen el control manual del costo.

#### 4. Decisión Adoptada
**Cómputo elástico con auto-escalado horizontal** (Fargate Django 2→6, Celery 2→4, Lambda 100→500, Aurora `db.r6g.large→xlarge` +2 readers, DynamoDB on-demand) con **escala predictiva por calendario** (septiembre/diciembre) y **reactiva** (CPU, profundidad de cola, TPS); base de capacidad con Savings Plan/instancias reservadas de la carga de régimen (RT-03.08) y la diferencia del peak como cómputo efímero (RT-03.09). Monitoreo del cuello de botella declarado (RT-09.05/RNF-19.03) y pruebas 1,5×peak (RNF-19.04).

#### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| Costo de proveer la parte efímera | Dependencia del autoscaler | 0 riesgo de pay-what-you-use: presupuestos y alarmas (RT-03.06); base RI para régimen |
| La cola puede crecer en el burst | Latencia de reconciliación | Vúmenes dimensionados (SQS × 24 h buffer); workers autoescalados; congelamiento de cambios (RT-10.05) |
| Complejidad del autoscaler predictivo | Configuración de calendario | Configuración IaC por evento (EventBridge); ensayo en marcha blanca de sept; aumentos conservadores ×1,5 |
| Surgimiento de cuello de botella nuevo tras el peak | Identificación tardía | Monitoreo de síntomas de negocio (RF-16.03) + pruebas de estrés al punto de quiebre (RNF-19.04) |

### ADR-13 — Puerta de Enlace de Servicios: Amazon API Gateway

- **Estado:** Aprobado
- **Fecha:** 2026-09-05 (formalizado como ADR el 2026-09-06)
- **Decisión relacionada:** D8 (Arquitectura Lógica v6.2, Capa 3).
- **Trazabilidad normativa:** **BA Art. 21.2** (puerta de enlace con autenticación, autorización, cuotas, límites de tasa, validación de esquema e inspección de carga útil) · **RT-02.01** (capa 3 del modelo de referencia) · **RT-11.11** · **RT-05.16/05.18** (contratos y OAuth 2.1/mTLS) · **RT-02.02** (contratos versionados retro-compatibles) · Art. 16.3 (preferencia por servicios administrados).

#### 1. Contexto y Problema
La Capa 3 es el punto por donde entra **todo**: las APIs de negocio, la sincronización diferida de preventa y reparto —que es tráfico de primera clase, no un anexo— y los tres portales de la DMZ. El Art. 21.2 no pide «un gateway»: pide autenticación, autorización, cuotas, límites de tasa, validación de esquema e inspección de carga útil, todo en el borde. Y el CLIENTE opera con **4 personas de TI**: cualquier componente que haya que parchar, dimensionar y sostener 24×7 compite con la operación.

#### 2. Alternativas Evaluadas
| Alternativa | Operación | Integración con el borde | Cuotas y esquema | Costo para un equipo de 4 | Veredicto |
|---|---|---|---|---|---|
| **A. Amazon API Gateway (administrado)** | Cero nodos que operar; escala con la carga | Nativa con CloudFront, WAF, Shield y ALB; autorizador OIDC contra Keycloak | Validación de esquema OpenAPI, cuotas y límites por cliente y por ruta, trazabilidad por transacción | Nulo en operación; costo por invocación declarado en FinOps | **Ganadora** |
| **B. Kong Gateway (open source, autoalojado)** | Nodos propios con alta disponibilidad, parches y versiones a cargo del equipo | Requiere integrar manualmente con WAF/ALB | Equivalente vía plugins | Alto: un componente crítico más en la ruta de la venta, operado por 4 personas | Rechazada |
| **C. Sin puerta de enlace, exponiendo el ALB directo a los módulos** | Mínima | — | No cumple Art. 21.2 (sin cuotas ni validación de esquema en el borde) | — | Rechazada (incumplimiento normativo) |

#### 3. Criterio de Selección y Justificación Técnica-Económica
- **Cumplimiento literal del Art. 21.2** sin desarrollo propio: autenticación OIDC, autorización por rol, cuotas y límites de tasa por cliente, validación de esquema e inspección de carga útil son capacidades nativas.
- **Equipo de 4 personas (Cap. 2.4 del caso):** la alternativa B agrega un componente crítico en la ruta de la venta que hay que dimensionar, parchar y recuperar. En la ventana de despacho 05:30–07:00, con indisponibilidad cero comprometida, ese es exactamente el riesgo que no conviene asumir.
- **Coherencia con la vista física:** las secciones de Despliegue, Emplazamiento e Integración de este documento ya declaran Amazon API Gateway; mantener Kong en el registro de decisiones habría dejado una contradicción entre la arquitectura lógica, la física y el costo, que el **Art. 16.4 in fine** califica de incoherencia grave.
- **Reversibilidad (Art. 16.3):** los contratos son **OpenAPI 3.1 y AsyncAPI 2.6**, estándares abiertos; la lógica de negocio vive en Django, no en el gateway. Migrar a Kong u otro gateway no exige reescribir servicios, solo reconfigurar rutas y autorizadores. La dependencia es de configuración, no de código, y así queda declarada en la matriz de reversibilidad.

#### 4. Decisión Adoptada
**Amazon API Gateway** como Capa 3 única, con autorizador OIDC contra el Keycloak maestro, validación de esquema OpenAPI, cuotas y límites de tasa por actor y por ruta, versionado `/v{major}` y asignación de `transaction_id` propagado a la Capa 8. **Kong Gateway queda declarado como alternativa open source evaluada y no adoptada.**

#### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| Dependencia de un servicio del proveedor de nube | Menor portabilidad del borde | Contratos en estándares abiertos; la lógica no vive en el gateway (§4.6 de reversibilidad) |
| Costo por invocación en el peak de septiembre | Gasto variable | Cuotas por actor y límites declarados; modelado en FinOps con el peak de 105 TPS |
| Los portales entran en enero de 2029 | La configuración crece en la Etapa 2 | Mismo gateway, rutas nuevas por configuración; sin componente adicional |

### ADR-14 — Plataforma de Observabilidad Única: OTel + AMP + CloudWatch + X-Ray

- **Estado:** Aprobado
- **Fecha:** 2026-09-06
- **Decisión relacionada:** D14 (Arquitectura Lógica v6.2, Capa 8); reemplaza la parte de plataforma de D9.
- **Trazabilidad normativa:** **BA Art. 16.4** («monitoreo del componente on-premise integrado a la misma plataforma de observabilidad que la nube, sin puntos ciegos») · **RT-03.16** (idéntica exigencia) · **RT-14.01 a RT-14.09** · **RT-09.01** (medición p95) · Art. 16.3 (servicios administrados).

#### 1. Contexto y Problema
La observabilidad tiene que cubrir dos dominios muy distintos —una nube elástica y cinco sitios que pueden quedar 24 h sin enlace— y hacerlo **sin puntos ciegos**. La versión anterior de la arquitectura lógica declaraba un conjunto **Prometheus + Grafana + Loki autoadministrado en cada centro de distribución**, además de la plataforma en nube. Al contrastarlo con la vista física aparecieron dos problemas: ese conjunto **no tenía máquina virtual dimensionada** —VM-06 es de 2 vCPU, 4 GB y 50 GB, insuficiente para sostener Prometheus, Loki y Grafana con 13 meses de métricas— y, más de fondo, **constituye una segunda plataforma de observabilidad**, que es justamente lo que el Art. 16.4 y RT-03.16 prohíben al exigir «la misma».

#### 2. Alternativas Evaluadas
| Alternativa | ¿Una sola plataforma? | Qué se ve durante un corte de 24 h | Operación | Veredicto |
|---|---|---|---|---|
| **A. Emisión on-premise (ADOT, buffer 24 h) → plataforma única en nube (AMP, CloudWatch, X-Ray, Grafana OSS)** | **Sí** | Sin tableros centralizados; alarmas locales del equipamiento y bloqueo de frío 100 % local; **cero pérdida de telemetría** gracias al buffer | Nula on-premise | **Ganadora** |
| **B. Prometheus + Grafana + Loki autoalojado por sitio, además de la nube** | No: dos plataformas | Tableros locales completos | Dos plataformas que parchar, dimensionar y correlacionar, sobre un equipo de 4; requiere VM adicional no dimensionada | Rechazada (incumple RT-03.16 y Art. 16.4; sin emplazamiento) |
| **C. Datadog o New Relic** | Sí | Depende del enlace igual que A | Menor, pero con lock-in y costo por host y por volumen | Rechazada (lock-in y costo) |

#### 3. Criterio de Selección y Justificación Técnica-Económica
- **La norma pide una plataforma, no dos.** Es el criterio decisivo: el Art. 16.4 y RT-03.16 usan la palabra «misma».
- **«Sin puntos ciegos» se resuelve con el buffer, no con una segunda plataforma.** El colector ADOT retiene 24 h en disco —exactamente la autonomía comprometida del centro de distribución— de modo que un corte no produce un hueco en la serie: produce un retraso que se cierra al reconectar.
- **Ninguna decisión crítica depende de un tablero.** El bloqueo de despacho por excursión térmica es local (decisión 16.1 N° 4), la alarma de cámara es acústica y luminosa, y los sensores de sala reportan al DCIM/BMS (RT-06.14). Lo que se pierde durante el corte es visibilidad agregada, no capacidad de operar.
- **Sin lock-in real:** **AMP es compatible con Prometheus y PromQL**, de modo que las reglas de alerta y las consultas son portables; la instrumentación es **OpenTelemetry**, estándar neutral; y Grafana es **OSS**. Se conserva el ecosistema Prometheus/Grafana sin operar sus servidores.
- **Equipo de 4 personas:** no se le entrega al CLIENTE una plataforma de observabilidad que mantener además del negocio.

#### 4. Decisión Adoptada
**Instrumentación OpenTelemetry** en todos los componentes; **colectores ADOT on-premise (F-01: VM-06 Talca, VM-C04 Concepción, contenedor en cross-docking) con buffer en disco de 24 h**; **plataforma única en nube**: métricas en **AMP** (13 meses), registros en **CloudWatch Logs** (12 meses en línea + 24 en archivo), trazas en **X-Ray** (30 días), tableros en **Grafana OSS** autoadministrado en sa-east-1 y alertas por AMP/Alertmanager y CloudWatch hacia SNS y PagerDuty. **Se declara expresamente qué no está disponible durante un corte** (RT-03.13), y se declara que ninguna decisión de la ventana 05:30–07:00 depende de ello.

#### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| Sin tableros centralizados durante un corte de enlace | Menor visibilidad agregada en contingencia | Buffer de 24 h sin pérdida; alarmas locales del equipamiento; bloqueo de frío local; declaración formal en la matriz RT-03.13 |
| Dependencia de servicios del proveedor de nube | Portabilidad | AMP compatible con Prometheus/PromQL, OTel como instrumentación y Grafana OSS: el ecosistema es portable |
| El buffer de 24 h consume disco en VM-06 y VM-C04 | Capacidad local | Dimensionado en el plan de capacidad; el corte de referencia es de 24 h (RT-03.10) |

### ADR-15 — Gestión de Secretos: Servicio Administrado en lugar de Gestor Autoalojado

- **Estado:** Aprobado
- **Fecha:** 2026-09-06
- **Decisión relacionada:** D13 (Arquitectura Lógica v6.2, Capa 7); resolución **SEC-01** de la sección de **Arquitectura de Seguridad de este documento** (§5.3).
- **Trazabilidad normativa:** **BA Art. 21.4** («prohibición absoluta de credenciales, claves o secretos embebidos… uso obligatorio de un gestor de secretos con rotación automática») · **Art. 21.2** (gestión de claves con separación de funciones) · **Art. 16.2** (justificación de emplazamiento componente por componente) · **Art. 16.3** (servicios administrados) · **Art. 21** (Zero Trust) · RT-04.09 · RT-11.09.

#### 1. Contexto y Problema
La solución necesita custodiar secretos de peso: credenciales del ERP de 2017, certificados AS2 y EDI de cada cadena de supermercados, credenciales del SII y de Transbank, y las credenciales de servicio entre módulos. El Art. 21.4 exige un gestor con rotación automática. La arquitectura lógica declaraba **HashiCorp Vault on-premise**, pero al contrastarla con la vista física de este documento apareció el problema real: **Vault no existía en ninguna vista física** —no tenía máquina virtual en el dimensionamiento on-premise (§4), no figuraba en el inventario ni en el emplazamiento de este documento—. Un componente de seguridad sin emplazamiento justificado **incumple el Art. 16.2** y, al no estar costeado, cae en la incoherencia grave del Art. 16.4 in fine.

#### 2. Alternativas Evaluadas
| Alternativa | Emplazamiento y costo | Operación para 4 personas | Zero Trust | Rotación automática | Veredicto |
|---|---|---|---|---|---|
| **A. AWS Secrets Manager + SSM Parameter Store** | Servicio administrado, sin VM ni licencia; costo por secreto declarable en FinOps | Nula: no se parcha ni se sella | Consumo **saliente** desde on-premise por VPC Endpoint; ningún puerto entrante | Nativa | **Ganadora** |
| **B. HashiCorp Vault autoalojado en Talca** | VM adicional con alta disponibilidad, respaldo, procedimiento de sellado y desellado, y licencia empresarial si se requiere alta disponibilidad | Alta: el desellado tras un reinicio es un procedimiento manual crítico que puede caer a las 3 de la mañana | Equivalente | Sí, con configuración propia | Rechazada |
| **C. Secretos en variables de entorno o en la configuración del despliegue** | — | — | — | — | Rechazada: **prohibición absoluta** del Art. 21.4 |

#### 3. Criterio de Selección y Justificación Técnica-Económica
- **El componente debe existir en la vista física.** Es la razón inmediata: lo declarado no estaba emplazado ni costeado. Cualquiera de las dos salidas corregía el defecto, pero solo una lo hacía sin agregar infraestructura.
- **Equipo de 4 personas (Cap. 2.4):** el modo sellado de Vault tras un reinicio exige intervención humana con custodios. En una operación cuya ventana crítica es de 05:30 a 07:00 y cuyo turno de preparación es nocturno, introducir un componente que puede requerir desellado manual de madrugada es un riesgo operacional que no compra nada.
- **Zero Trust intacto:** los nodos on-premise consumen secretos por **VPC Endpoint saliente**, coherente con la regla de que no se abren puertos entrantes salvo las dos excepciones D-AL-05.
- **La contingencia no depende de la nube.** El secreto de la **cuenta de emergencia** queda deliberadamente **fuera de línea**, en sobre sellado con doble firma en el recinto de custodia de la sala (RT-06.26/06.27): es la única credencial que debe seguir siendo utilizable cuando no hay ni IdP ni enlace, y por eso no vive en ningún sistema.
- **Separación de funciones (Art. 21.2):** quien administra la plataforma no administra las claves maestras; la política se expresa en IAM y queda auditada en CloudTrail.

#### 4. Decisión Adoptada
**AWS Secrets Manager** para secretos con rotación (credenciales del ERP, SII, Transbank y certificados AS2/EDI) y **SSM Parameter Store** para parámetros de configuración no sensibles, con consumo **saliente** desde los nodos on-premise por VPC Endpoint, rotación automática, y **cifrado con CMK de KMS bajo separación de funciones**. **HashiCorp Vault queda declarado como alternativa evaluada y no adoptada.** La cuenta de emergencia se custodia fuera de línea.

#### 5. Consecuencias, Trade-offs y Mitigaciones
| Consecuencia | Trade-off | Mitigación |
|---|---|---|
| Los nodos on-premise requieren enlace para obtener un secreto nuevo | Dependencia de la nube para la rotación | Los secretos en uso se cachean en memoria por el proceso durante la autonomía de 24 h; ninguna rotación se programa dentro de la ventana crítica ni de un corte |
| Dependencia de un servicio del proveedor de nube | Portabilidad | Los secretos son datos, no lógica; la exportación está cubierta por la declaración de reversibilidad (Art. 16.3) |
| Costo por secreto y por rotación | Gasto variable | Volumen acotado (integraciones del catálogo, 15 entradas) y declarado en FinOps |

### Matriz de trazabilidad (ADR → normativa → decisión → documento)

| ADR | RT / RNF clave | BA / Caso | Decisión relacionada | Documento que la materializa |
|---|---|---|---|---|
| ADR-01 | RT-02.02 · §2.3 · RT-09.05 · RNF-19.01–04 | Art. 16 | D5 | Arquitectura de Integración de este documento (§2.3) · Dimensionamiento (§3) |
| ADR-02 | RT-03.17 · RT-03.10 · RNF-13.01/13.07/13.08 · RT-10.05 | §6.12/§8 (caso) | Decisión 16.1 N° 26 | Arquitectura de Despliegue de este documento (§2) · Emplazamiento (§c) |
| ADR-03 | Art. 16.1–16.4 · RT-03.01/03.02/03.10 · RNF-02.01/05.01/05.02 | Art. 16 BA | D7 · Decisión 16.1 N° 17 | Emplazamiento de este documento (§a) · Despliegue (§1) |
| ADR-04 | RT-05.02 · RT-05.15 · RNF-09.01/09.02/11.02 | Cap. 16.1 N° 18/35 · D.S. 977/96 | D2/D4 | Persistencia de este documento (ADR-04) · BI (§4.2) |
| ADR-05 | RT-02.06/02.07 · RT-03.10/03.12 · RNF-07.01/13.01 | Art. 21 (Zero Trust) | D4 · D-AL-03 | Arquitectura de Integración de este documento (§5) |
| ADR-06 | RT-12.10/12.11/12.12 · RT-03.10 · RNF-13.01 | Art. 22 (MFA) | D6 · Decisión 16.1 N° 34 | Arquitectura de Seguridad de este documento (§4) |
| ADR-07 | RT-13.08 · RT-12.11 · RT-03.19 · RNF-05.02/05.03/06.01 | Cap. 6/13.8 (caso) | Decisión de proyecto N° 19 | Emplazamiento de este documento (§c.3) · RNF-05.02/05.03/06.01 |
| ADR-08 | RT-05.11–05.15 · RT-03.10 · RNF-02.01 | Cap. 16.1 N° 14 | Decisión 16.1 N° 14 | Arquitectura de Integración de este documento (§7) · Emplazamiento (§b) |
| ADR-09 | RT-07.01/07.07 · RNF-20.06/20.07 | Art. 20 BA | Decisión 16.1 N° 27 | Arquitectura de Despliegue de este documento (§4 · §5) |
| ADR-10 | RT-03.14 · RNF-13.03/13.04/13.05 | Cap. 16.1 N° 28 | Decisión 16.1 N° 28 | Dimensionamiento de este documento (§4) · Emplazamiento (A-02) |
| ADR-11 | RT-05.23 · RT-16.16/16.17 · RNF-12.01 · RF-12.03/12.06/12.13 | Cap. 16.2 GS1 | RF-12 · RF-01.10 | Arquitectura de Integración de este documento (§7) · RF-12.03/12.06/12.13 |
| ADR-12 | RT-09.05 · RT-03.06/03.08/03.09 · RNF-19.01–04 | Cap. 14.2/15 · RT-10.05 | Decisión 16.1 N° 30 | Dimensionamiento de este documento (§3 · §5 · §6) |
| **ADR-13** | RT-02.01 · RT-11.11 · RT-05.16/05.18 · RT-02.02 | Art. 21.2 · Art. 16.3 | D8 | Arquitectura de Integración de este documento (§4) · Seguridad (§3) |
| **ADR-14** | RT-03.16 · RT-14.01–14.09 · RT-09.01 | **Art. 16.4** · Art. 16.3 | D14 (reemplaza D9) | Arquitectura de Seguridad de este documento (§7) · RF-16.01 |
| **ADR-15** | RT-04.09 · RT-11.09 · RT-03.15 | **Art. 21.4** · Art. 21.2 · **Art. 16.2** · Art. 16.3 | D13 · SEC-01 | Arquitectura de Seguridad de este documento (§5.3) |

---

## Referencias

El presente Subdocumento 4.2 es un documento **autocontenido**: se sustenta únicamente en los documentos rectores y en los catálogos de requerimientos del proyecto. No cita archivos de trabajo internos.

| Documento | Rol |
|---|---|
| Bases Administrativas (BA) | Documento rector — precedencia (Art. 5°) |
| Bases Técnicas Transversales (BTT) | Documento rector — requerimientos RT-cc.nn |
| Caso 02 — Logística (Distribuidora Puelche S.A.) | Documento rector — Cap. 15 (valores y volumetría) |
| Catálogo de requerimientos funcionales (RF) | `Requerimientos/Requerimientos LOGISTICA - Consolidado de Requerimientos Funcionales.csv` |
| Catálogo de requerimientos no funcionales (RNF) | `Requerimientos/Requerimientos LOGISTICA - Consolidado de Requerimientos NO Funcionales.csv` |

*Subdocumento 4.2 · Arquitectura de la Solución · LafroX — Caso 02 Logística (Distribuidora Puelche S.A.).*