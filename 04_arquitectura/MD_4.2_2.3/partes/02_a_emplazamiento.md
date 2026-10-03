<a id="h-04-partes-4-2-fisica-02-a-emplazamiento-tex-50"></a>

## 4.2.2 Emplazamiento de cada componente

<a id="sec-emplazamiento"></a>

El emplazamiento de cada componente se decide con los seis criterios del Artículo 16.2 de las Bases Administrativas (PUCV, 2026c, art. 16.2, p. 11): latencia tolerada, criticidad operacional, volumen de datos, restricciones regulatorias, disponibilidad de conectividad y costo total de propiedad. En este caso la conectividad y la latencia pesan más que en una operación de oficina, porque el caso describe una red que se corta: la fibra de Talca tiene en promedio cuatro cortes al año de hasta seis horas, Concepción carece de respaldo en la situación de partida, los cross-docking dependen de red móvil en la situación de partida y en Los Ángeles la señal es intermitente justo en su ventana de madrugada, las cámaras no tienen cobertura en su interior y hay rutas sin señal durante dos horas o durante el turno completo, como describe el capítulo 6 del caso.

De esos hechos se desprende la regla que ordena todo el emplazamiento: lo que debe funcionar sin enlace vive en el sitio, y lo que escala, se comparte o está expuesto a Internet vive en la nube. Conforme a esa regla, registrada en ADR-03 (Anexo 4-O), los 36 componentes del catálogo se reparten en 13 de nube pura, 11 on-premise y 12 híbridos, que tienen una parte en cada dominio.

<a id="h-04-partes-4-2-fisica-02-a-emplazamiento-tex-51"></a>

### 4.2.2.1 Instalaciones y dominios

De las seis instalaciones que cubre la solución, cinco alojan cómputo on-premise. La tipología que fija el caso se aplica así:

-  El CD Talca es la sala técnica secundaria, con un clúster de tres nodos con Proxmox VE y almacenamiento Ceph que aloja las máquinas virtuales VM-01 a VM-06.

-  El CD Concepción opera en un gabinete de borde, con un servidor con Proxmox VE que replica la misma pila en las máquinas VM-C01 a VM-C04.

-  Las plataformas de cross-docking de Curicó, Chillán y Los Ángeles operan cada una en un gabinete de borde, con un mini-PC industrial que ejecuta el WMS en contenedores.

-  La sexta instalación, la casa matriz de Talca, está junto al centro de distribución, solo aloja oficinas y trabaja contra la nube, por lo que no requiere cómputo propio y el dimensionamiento se calcula sobre los otros cinco recintos.

Los dos centros de distribución tienen su recinto especificado en el apartado [4.3](../../LAFROX-Subdocumento4.md#cap-4-3-data-center); las plataformas de cross-docking no lo tienen, porque operan en un gabinete de borde dentro de la nave. La Figura [16](../../LAFROX-Subdocumento4.md#fig-crossdocking) muestra ese gabinete, que se repite igual en Curicó, Chillán y Los Ángeles.

![Figura original](https://raw.githubusercontent.com/PatricioH315/LafroX/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/fisica/Arquitectura_Fisica_Crossdocking.png)

**Figura 16 — Gabinete de borde de las plataformas de cross-docking**

<a id="fig-crossdocking"></a>

*Fuente: elaboración propia.*

Starlink es el enlace principal y el LTE de dos proveedores lo respalda; ambos llegan a un par de firewalls compactos en alta disponibilidad, que termina el túnel VPN hacia la nube y conmuta de enlace en menos de 30 s. Detrás de los firewalls, dos switches industriales conectan los dos puntos de acceso de la nave y las dos interfaces del mini-PC industrial, que ejecuta en contenedores Docker el WMS, PostgreSQL, RabbitMQ, la caché de Keycloak y el colector ADOT. Los dos terminales inalámbricos de cada plataforma leen los códigos GS1 y trabajan contra ese WMS local. El gabinete reúne en un solo equipo las funciones que Talca y Concepción reparten en varias máquinas virtuales, y con ello opera al 100 % en local la ventana de tres horas de recepción, desconsolidación y re-despacho. El mini-PC es un equipo único por sitio, con alimentación redundante y reposición desde Talca; su reconstrucción desde el estado central de la nube se trata en la sección [4.2.5](../../LAFROX-Subdocumento4.md#sec-conexiones).

La Figura [17](../../LAFROX-Subdocumento4.md#fig-cd-concepcion) presenta el gabinete de borde del CD Concepción como parte de su operación autónoma.

![Figura original](https://raw.githubusercontent.com/PatricioH315/LafroX/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/centros_de_datos/Arquitectura_Fisica_CD_Concepcion.png)

**Figura 17 — Gabinete de borde del CD Concepción**

<a id="fig-cd-concepcion"></a>

*Fuente: elaboración propia.*

La figura sitúa el WMS, PostgreSQL, RabbitMQ y la caché de identidad en cuatro VM del servidor Proxmox local. El par de firewalls y los dos switches de núcleo sostienen la red del sitio. Fibra D-03, LTE D-04 y Starlink D-06 proporcionan tres caminos hacia la nube; la UPS de 3 kVA del gabinete protege el servidor, los equipos de red y el terminal satelital durante 30 min y permite el apagado ordenado; su carga de diseño, 2,16 kVA, usa el 72 % de esa capacidad (Anexo 4-W). El servidor tiene fuentes redundantes. Si falla, se repone y se reconstruye su base a partir del estado central alimentado por los eventos del propio sitio. El detalle de cada equipo está en el Formulario T-11.

La séptima instalación que proyecta el caso a tres años se incorpora parametrizando la infraestructura como código, sobre el bloque de direccionamiento ya reservado en la Tabla [15](../../LAFROX-Subdocumento4.md#tab-t64), sin obras en la sala de Talca.

En la nube, la región primaria es sa-east-1 y cada servicio se despliega en al menos dos zonas de disponibilidad. La región us-east-1 solo aloja la recuperación ante desastres. La Figura [18](../../LAFROX-Subdocumento4.md#fig-emplazamiento-dominios) ubica cada componente en su sitio.

**Diagrama vectorial del fuente:** [consultar figura en LaTeX](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/partes/4.2_fisica/02_a_emplazamiento.tex). Representación textual de sus rótulos; no sustituye el diagrama.

- Nube AWS
- **sa-east-1**, dos zonas o más N-01 a N-03 Portales N-04 Plataforma de aplicación N-05 Base de datos en nube N-06 Telemetría cruda N-07 Caché N-08 Ingesta de IoT N-09 Mensajería N-10 Plataforma analítica N-12 Seguridad y gobierno N-13 Gestión de dispositivos Parte en nube de los híbridos
- **us-east-1**, recuperación N-11 Respaldo inmutable y réplica
- On-premise
- **CD Talca**, sala técnica secundaria Máquinas VM-01 a VM-06 con A-01 a A-05 y F-01 Red: D-01 en par, D-02 a D-06 Frío: B-01 y B-02 Bodega: C-03 a C-05 Gestión: F-02 y F-03
- **CD Concepción**, gabinete de borde Máquinas VM-C01 a VM-C04 con A-01 a A-03, A-05 y F-01 Red: D-01 a D-04 y D-06 Frío: B-01 y B-02 Bodega: C-03 a C-05 Gestión: F-03
- **Cross-docking**, tres sitios Mini-PC E-01 con A-01 a A-03 y caché de A-05 Red: D-01 compacto, D-02, D-04 y D-06 Gestión: F-01 y F-03
- **Casa matriz**, Talca Sin cómputo; usa la nube
- Terreno
- **Calle** C-01 App de preventa 62 terminales EC55 C-02 App de reparto 96 terminales TC58e
- **Camiones de frío** B-03 Termógrafos, 28
- **Locales de clientes** 14.200 puntos de entrega

**Figura 18 — Ubicación de los componentes por dominio y por sitio**

<a id="fig-emplazamiento-dominios"></a>

*Fuente: elaboración propia.*

La figura muestra que ninguna instalación depende de los sistemas de otra para operar, aunque Concepción siga recibiendo parte de su surtido desde Talca. Talca y Concepción tienen cada uno su WMS, su base, su broker y su caché de identidad; los cross-docking reúnen esas mismas funciones en un solo equipo; y el terreno lleva su propio almacén local en el dispositivo. La nube concentra lo que es común a todos los sitios: los portales, el transaccional compartido, la analítica y los servicios de seguridad. Los doce componentes híbridos aparecen en los dos dominios porque cada uno tiene una parte que debe seguir operando en el sitio y otra que consolida en la nube.

<a id="h-04-partes-4-2-fisica-02-a-emplazamiento-tex-52"></a>

### 4.2.2.2 Correspondencia con la arquitectura lógica

La Tabla [8](../../LAFROX-Subdocumento4.md#tab-mapeo-logica) asocia cada módulo y cada capa transversal de la arquitectura lógica del apartado 4.1 con el componente físico que lo ejecuta y con el lugar donde corre. Es la traza que permite seguir una responsabilidad lógica hasta su emplazamiento. Los componentes físicos se identifican con un catálogo único, agrupado por letra: A para el núcleo de bodega, B para la cadena de frío, C para los dispositivos de operación, D para la red, E para los cross-docking, F para la observabilidad y la seguridad de los nodos, y N para la nube.

<a id="tab-mapeo-logica"></a>

**Tabla 8 — Correspondencia entre la arquitectura lógica y la física**

| **Módulo o capa (4.1)** | **Componente físico (4.2)** | **Dónde se ejecuta** |
| --- | --- | --- |
| M1 Recepción | A-01 y A-02, con C-03 y C-05 | Sitio |
| M2 Inventario | A-01 y A-02 en el sitio; N-04 y N-05 para el consolidado | Sitio y nube |
| M3 Preventa | C-01 en el terminal; N-04, N-05 y N-07 | Terreno y nube |
| M4 Rutas | N-04 y N-05; motor de optimización en su propio contenedor | Nube |
| M5 Preparación | A-01 y A-02, con C-03 y C-04 | Sitio |
| M6 Reparto | C-02 en el terminal; N-04 y N-05, con la evidencia en S3 | Terreno y nube |
| M7 Rendición | C-02; N-04; A-04 hacia el ERP | Terreno, nube y VM-04 |
| M8 Devoluciones | C-02; N-04; A-01 para la recepción física de retornos mediante la puerta de API local | Terreno, nube y sitio |
| M9 Calidad | B-01, B-02 con la función local de bloqueo en el borde y B-03; N-06 y N-08 | Sitio, camiones y nube |
| M10 Analítica | N-10 | Nube |
| M11 Canal moderno | N-04 con el perfil EDI y el transporte AS2; A-04 | Nube y VM-04 |
| M12 Flota | N-04 y N-06, con la API del proveedor de telemetría | Nube |
| Capa 1, portales y consolas | N-01 a N-03 y frontend de consolas en N-04 | Nube |
| Capas 2 y 3, entrada y puerta de enlace | CloudFront, WAF y API Gateway (N-01 a N-03 y N-12); puerta de API local en A-01 | Nube y sitio |
| Capa 5, integración y eventos | A-03; N-09; A-04 | Sitio y nube |
| Capa 6, datos | A-02; N-05, N-06, N-07, N-10 y N-11 | Sitio y nube |
| Capa 7, seguridad e identidad | A-05 con el verificador local; F-03; N-12 | Nube y sitio |
| Capa 8, observabilidad | F-01 y CloudWatch (N-12) | Sitio y nube |

 Fuente: elaboración propia.

El perfil local cubre M1, M2, M5, la función de bloqueo de M9 y la recepción física de retornos de M8 a través de la puerta de API local. Los módulos compartidos corren en N-04 y el terreno captura en su terminal. Los perfiles de ejecución se especifican en la sección [4.2.4](../../LAFROX-Subdocumento4.md#sec-despliegue).

<a id="h-04-partes-4-2-fisica-02-a-emplazamiento-tex-53"></a>

### 4.2.2.3 Síntesis del emplazamiento por dominio y criterio

La Tabla [9](../../LAFROX-Subdocumento4.md#tab-t21) resume cómo se distribuyen los 36 componentes entre los tres dominios y los seis criterios del Artículo 16.2 (PUCV, 2026c, art. 16.2, p. 11) que deciden cada emplazamiento. A continuación se justifica, dominio por dominio, por qué cada componente vive donde vive; el producto, la cantidad y la ubicación exacta de cada elemento no son materia del emplazamiento y se especifican en el Formulario T-11.

<a id="tab-t21"></a>

**Tabla 9 — Distribución de los componentes por dominio y criterio de emplazamiento**

| **Criterio** | **Nube pura** | **On-premise** | **Híbridos** | **Total** |
| --- | --- | --- | --- | --- |
| Latencia tolerada | 1 | 4 | 1 | 6 |
| Criticidad operacional | 2 | 2 | 3 | 7 |
| Volumen de datos | 3* | — | — | 3 |
| Conectividad | — | 4 | 7 | 11 |
| Regulación | 5 | — | 1 | 6 |
| Costo total de propiedad | 3* | 1 | — | 4 |
| **Total de componentes** | **13** | **11** | **12** | **36** |

 Fuente: elaboración propia.

El emplazamiento responde a cuatro criterios decisivos del caso:

-  Conectividad: decide once componentes y domina los on-premise e híbridos, por los cortes de enlace y el terreno sin señal.

-  Regulación: decide seis y domina la nube pura, porque el Artículo 21 de las Bases Administrativas (PUCV, 2026c, p. 15) impide exponer los sitios a Internet y separa los públicos externos en la DMZ.

-  Costo y volumen: concentran en la nube lo que escala y se paga por uso.

-  Latencia y criticidad: dejan en el sitio lo que debe responder sin enlace.

La columna Total suma 37 en las filas de criterios porque la plataforma analítica (N-10) se contabiliza en los dos criterios que deciden su emplazamiento, volumen de datos y costo total de propiedad; la fila final suma los 36 componentes efectivos.

<a id="h-04-partes-4-2-fisica-02-a-emplazamiento-tex-54"></a>

### 4.2.2.4 Componentes de nube pura

Los trece componentes de nube pura viven solo en la nube. La justificación de cada uno y el criterio del Artículo 16.2 (PUCV, 2026c, art. 16.2, p. 11) que la determina son los siguientes:

-  **N-01 Portal de Clientes** (regulación): atiende el catálogo, el pedido de autoatención, el estado de entrega, los documentos y el saldo de los clientes desde Internet, también como aplicación instalable que arma el pedido sin señal; por eso se publica solo en la DMZ de la nube y ningún tráfico externo llega a los sitios del CLIENTE.

-  **N-02 Portal de Transportistas** (regulación): los conductores externos entran con una clave de un solo uso y sin cuenta corporativa, y ese acceso se resuelve en la DMZ de la nube.

-  **N-03 Portal de Proveedores** (regulación): los 180 proveedores consultan órdenes de compra, recepciones y devoluciones desde Internet, aislados de la red de bodega.

-  **N-04 Plataforma de aplicación** (costo): Laravel corre en ECS Fargate con perfiles de API, reconciliación, trabajos y planificación que escalan por separado. La plataforma aloja el frontend Angular de consolas y el transporte AS2 de M11 en dos tareas distribuidas entre dos zonas cada uno; el motor de rutas M4 ejecuta una tarea por corrida, que ECS relanza en otra zona ante una falla para repetirla dentro de la planificación de 15:00 a 18:30, con el plazo de 20 min por corrida medido en la prueba de aceptación. M11 usa contratos versionados (ADR-11, Anexo 4-O).

-  **N-05 Base de datos en nube** (criticidad): Aurora PostgreSQL guarda el transaccional de los módulos en nube y la réplica del WMS, conmuta entre zonas en menos de 30 s y se replica a us-east-1.

-  **N-06 Telemetría cruda** (volumen): DynamoDB recibe las lecturas de temperatura sin gestión de capacidad y las expira a los 30 días, cuando ya están consolidadas en la capa analítica.

-  **N-07 Caché** (latencia): ElastiCache mantiene en memoria el stock, el crédito y las sesiones para que la consulta de preventa responda en menos de 2 s.

-  **N-08 Ingesta de IoT** (volumen): IoT Core recibe los 10.584 mensajes diarios de cadena de frío por MQTTS y gestiona los gateways del borde; su motor de reglas escribe cada lectura en DynamoDB y publica en SNS las que superan el umbral.

-  **N-09 Mensajería** (criticidad): una cola SQS FIFO recibe la reconciliación de los sitios como sobres JSON versionados, en orden por grupo y sin duplicados; otra cola FIFO lleva las solicitudes al ERP hasta `erp-sync` y una cola FIFO por sitio devuelve sus respuestas; otras colas SQS, separadas de esas, transportan los trabajos internos de Laravel; y SNS difunde las alertas de excursión térmica.

-  **N-10 Plataforma analítica** (volumen y costo): S3, Glue, Redshift Serverless y QuickSight conservan 5 años de datos separados del transaccional. Los tableros y la autoría de QuickSight se integran en las consolas para usuarios registrados, con modelo semántico documentado, creación autónoma de informes, exportación y permisos separados de lectura y creación; los indicadores operacionales actuales se consultan en la API de negocio.

-  **N-11 Respaldo inmutable y réplica** (regulación): S3 Object Lock, AWS Backup y la réplica en us-east-1 guardan la copia que ni un administrador puede borrar y sostienen el RTO de 4 h y el RPO de 15 min.

-  **N-12 Seguridad y gobierno** (regulación): KMS, Secrets Manager, WAF, Shield Advanced, Verified Access, Security Lake y CloudWatch implementan en la nube los controles del Artículo 21 de las Bases Administrativas (PUCV, 2026c, p. 15) definidos en la arquitectura de seguridad (apartado 4.1), como servicios que un equipo de TI de cuatro personas puede operar.

-  **N-13 Gestión de dispositivos** (costo): Android Enterprise y Zebra DNA gestionan como servicio el parque de terminales de preventa, reparto y cámara, con borrado remoto selectivo y sin infraestructura en los sitios.

Ningún componente de nube pura participa en las transacciones que el caso exige resolver sin enlace: la confirmación de preparación, el despacho y el registro de entrega se ejecutan en el sitio o en el dispositivo. Lo que sube a la nube lo hace por tres razones. Los portales y la gestión de identidades externas lo hacen por regulación, porque el Artículo 21 de las Bases Administrativas (PUCV, 2026c, p. 15) impide exponer los sitios a Internet. La plataforma de aplicación, la analítica y la telemetría lo hacen por volumen y costo, porque su carga varía con la estación y se paga por uso. Y la seguridad y el respaldo lo hacen porque un equipo de TI de cuatro personas no puede operar esos controles en sus propios servidores.

<a id="h-04-partes-4-2-fisica-02-a-emplazamiento-tex-55"></a>

### 4.2.2.5 Componentes on-premise

Los once componentes on-premise viven solo en las instalaciones del CLIENTE. La justificación de cada uno y su criterio:

-  **B-01 Sensores de temperatura** (latencia): los 21 puntos de medición de las cámaras se leen por Modbus en el mismo sitio, porque dentro de la cámara no hay señal y la lectura no puede esperar al enlace.

-  **B-02 Gateway IoT** (latencia): los gateways de Talca y Concepción detectan la excursión térmica y bloquean el despacho en menos de 5 s, con un buffer de 24 h si cae el enlace, igual a la autonomía del centro de distribución.

-  **C-03 Terminales de bodega** (conectividad): los terminales MC9400 trabajan en la bodega y en las cámaras, incluido el congelado a -22 °C, sin señal móvil, contra el WMS del sitio por la red inalámbrica de la bodega.

-  **C-04 Impresoras de andén** (latencia): las seis impresoras ZT411 imprimen la etiqueta SSCC en el andén al armar la unidad logística, sin salir de la red local.

-  **C-05 Balanzas de recepción** (latencia): las tres balanzas envían el peso de recepción al WMS del sitio en línea, sin digitación y sin depender del enlace.

-  **D-02 Switching** (criticidad): los switches de cada sitio segmentan la red local por VLAN y la mantienen operativa aunque caiga la WAN.

-  **D-03 Enlace de fibra** (conectividad): es el camino principal de la VPN en Talca y Concepción, con 20 y 10 Mbps en régimen.

-  **D-04 Enlace LTE** (conectividad): respalda la fibra en los CD y, con dos proveedores, respalda a Starlink en los cross-docking, con conmutación en menos de 30 s.

-  **D-06 Enlace satelital** (conectividad): Starlink es el camino principal de los cross-docking, respaldado por LTE de dos proveedores, y el tercer camino en espera caliente de Talca y Concepción, con terminal encendido, túnel IPsec establecido y BGP de menor preferencia que solo toma tráfico si fallan fibra y LTE.

-  **E-01 WMS de cross-docking** (criticidad): el mini-PC de cada plataforma opera 100 % en local la ventana de 3 h de recepción, desconsolidación y re-despacho, con su propio broker y su propia base.

-  **F-02 Gestión de parches** (costo): Ansible aplica los parches y las líneas base CIS a los nodos de los cinco sitios por la red de gestión, sin licencia de plataforma.

En el on-premise dominan la latencia y la conectividad. Los sensores, las impresoras, las balanzas y los terminales de cámara son periféricos que trabajan donde está la mercadería, y ninguno puede depender de un enlace que el caso describe como intermitente. Los tres enlaces y el switching tampoco podrían emplazarse en otro lugar: son la infraestructura que conecta el sitio con la nube y sostiene su red interna cuando esa conexión falla.

<a id="h-04-partes-4-2-fisica-02-a-emplazamiento-tex-56"></a>

### 4.2.2.6 Componentes híbridos

Los doce componentes híbridos tienen una parte en cada dominio. Para cada uno, la justificación explica qué parte vive en el sitio, qué parte vive en la nube y por qué se reparten así:

-  **A-01 Motor WMS** (latencia): el perfil `wms_only` del artefacto Laravel, con su servidor web y PHP-FPM, corre en VM-01, VM-C01 y E-01 porque la confirmación de preparación debe responder en 1 s sin depender del enlace, y su réplica en Aurora sostiene la continuidad. El mismo motor expone la puerta de API local de la bodega, que durante un corte valida el esquema, la tasa, el UUID y la auditoría de las solicitudes de los terminales sin pasar por API Gateway.

-  **A-02 Base transaccional del WMS** (criticidad): PostgreSQL 16 en VM-02 y VM-C02 es el registro de cada bodega durante un corte. AWS DMS replica continuamente los cambios de VM-02 (Talca) a Aurora para continuidad y lectura por fibra, LTE o Starlink; VM-C02 (Concepción) entrega sus eventos por las colas de integración.

-  **A-03 Broker de colas** (conectividad): RabbitMQ en VM-03, VM-C04 y E-01 guarda hasta 24 h de eventos sin enlace, con mensajes persistentes y confirmación de publicación; el shipper, un proceso PHP con el adaptador AMQP `php-amqplib`, los publica como sobres JSON en SQS FIFO y solo los retira del broker cuando SQS confirma la recepción.

-  **A-04 Capa anticorrupción del ERP** (criticidad): corre en VM-04 junto al ERP de 2017, que no se modifica. En la misma VM, `erp-sync` consume la cola local de Talca y, mediante conexión saliente, la cola FIFO de solicitudes al ERP de los demás orígenes, cuyas respuestas devuelve por la cola de cada sitio; usa una clave idempotente por operación para que un reintento no emita un segundo documento tributario.

-  **A-05 Identidad** (conectividad): el IdP maestro Keycloak corre en Fargate y sus cachés de solo lectura en VM-05, VM-C03 y E-01 validan las sesiones de bodega y de cross-docking sin enlace; en el mismo nodo, un verificador local habilita cada relevo de turno durante un corte con el manifiesto de turno firmado y un segundo factor local, el PIN personal.

-  **B-03 Termógrafos de camión** (conectividad): los 28 termógrafos —18 en los camiones propios y 10 en los de los transportistas, instalados con el acuerdo de cada uno (S-28)— registran la temperatura durante toda la ruta sin señal y sincronizan por Bluetooth con el terminal del conductor, que alerta la excursión térmica en el momento y la reenvía a la nube cuando recupera cobertura; al volver el camión, el mismo terminal descarga el registro completo y lo envía a la nube para que IoT Core lo valide.

-  **C-01 App de preventa** (conectividad): toma pedidos contra el almacén local del terminal cuando no hay señal y sincroniza por CloudFront al reconectar, sin duplicar pedidos (sección [4.2.5](../../LAFROX-Subdocumento4.md#sec-conexiones)).

-  **C-02 App de reparto** (conectividad): registra entregas, evidencia y cobros durante 14 h sin señal y los sincroniza con la nube al recuperar cobertura.

-  **D-01 Firewall y Customer Gateway** (criticidad): el par de firewalls de cada uno de los cinco sitios termina los túneles IPsec hacia el Transit Gateway de AWS y conmutan de enlace en menos de 30 s.

-  **D-05 Respaldo local** (conectividad): el NAS WORM de Talca restaura el WMS en 4 h sin depender del enlace, y su complemento inmutable vive en S3 Object Lock.

-  **F-01 Telemetría de observabilidad** (conectividad): los colectores ADOT de VM-06, VM-C04 y E-01 guardan hasta 24 h de métricas y trazas en disco y las envían a CloudWatch al reconectar.

-  **F-03 Detección en endpoints** (regulación): los agentes EDR de cada nodo y estación reportan a una consola central, lo que da una sola respuesta ante incidentes en nube y on-premise.

Los componentes híbridos siguen todos el mismo patrón: la parte que atiende la operación queda en el sitio y la parte que consolida queda en la nube, unidas por un mecanismo que tolera el corte. En el núcleo de bodega, Talca replica su base por DMS y los demás sitios sincronizan eventos por colas; en el terreno, el almacén local del dispositivo; y en la observabilidad, el buffer en disco de los colectores. Por eso la conectividad es el criterio dominante en siete de los doce: cada uno existe en dos lugares precisamente porque el enlace entre ellos no es confiable.

<a id="h-04-partes-4-2-fisica-02-a-emplazamiento-tex-57"></a>

### 4.2.2.7 Autonomía de cada ámbito sin enlace

El emplazamiento descrito se verifica en lo que cada ámbito puede hacer cuando pierde el enlace. La Tabla [10](../../LAFROX-Subdocumento4.md#tab-t29) declara esa autonomía y el tiempo en que cada ámbito vuelve a quedar sincronizado.

<a id="tab-t29"></a>

**Tabla 10 — Autonomía por ámbito ante la pérdida del enlace**

| **Ámbito** | **Autonomía sin enlace** |
| --- | --- |
| Centros de distribución de Talca y Concepción | 24 h o más, con reconciliación determinista |
| Terreno | 14 h, un turno completo |
| Cross-docking | 24 h o más; la ventana de 3 h opera 100 % local |
| Sincronización al reconectar | CD en 2 h; flota en 10 min |

 Fuente: elaboración propia.

Durante la autonomía, cada ámbito mantiene su operación completa contra sus datos locales:

-  El centro de distribución sigue con recepción, preparación, despacho, conteo cíclico y trazabilidad contra la base local.

-  El terreno sigue con toma de pedido, entrega, evidencia, devoluciones y cobros contra el almacén local del dispositivo.

-  El cross-docking mantiene recepción, desconsolidación, validación de frío y re-despacho.

Al reconectar, el vuelco ocurre en orden estricto, sin duplicados y con reconciliación determinista.

La autonomía de cada ámbito cubre el corte más largo que describe el caso para ese lugar. Las seis horas del peor corte de fibra de Talca quedan dentro de las 24 horas del centro de distribución, y la ruta rural que recupera cobertura solo al regresar queda dentro del turno de 14 horas del terreno. Los tiempos de sincronización se sostienen con los enlaces dimensionados en la sección [4.2.6](../../LAFROX-Subdocumento4.md#sec-dimensionamiento), y lo que ocurre ante cada falla se desarrolla en la sección [4.2.5](../../LAFROX-Subdocumento4.md#sec-conexiones).
