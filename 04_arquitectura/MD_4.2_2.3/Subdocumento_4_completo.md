<!-- Subdocumento 4 completo: unión en orden de contenido.tex de los archivos de partes/. Fuente: 04/partes/4.2_fisica, 04/partes/4.3_centros_de_datos, 04/formularios/T11 y 04/anexos/fisica -->

<a id="cap:4-2-arquitectura-fisica"></a>
# 4.2 Arquitectura física

La arquitectura física declara dónde vive cada componente de la solución, qué servicios se contratan en la nube, cómo se conectan los sitios entre sí y con la nube, qué ocurre cuando falla cada conexión y cuánta capacidad se provee.

Esa arquitectura materializa el despliegue híbrido obligatorio del Artículo 16° de las Bases Administrativas (Art. 16, p. 11). La carga principal corre en nube pública AWS, con la región primaria en sa-east-1 (São Paulo, Brasil) y la recuperación ante desastres en us-east-1 (Norte de Virginia, EE. UU.), y los componentes on-premise garantizan la continuidad de la operación de bodega, plataformas y terreno durante los cortes del enlace. La solución cubre las seis instalaciones de la compañía —los centros de distribución de Talca y de Concepción, las plataformas de cross-docking de Curicó, Chillán y Los Ángeles, y la casa matriz de Talca—, además de la calle y los 14.200 puntos de entrega. Cinco de esas instalaciones alojan cómputo; la casa matriz, contigua al centro de distribución de Talca, solo tiene oficinas y trabaja contra la nube. La séptima instalación, que el caso proyecta a tres años, se agrega por parametrización, sin cambios de desarrollo ni crecimiento de servidores en el CD Talca. Dos principios gobiernan el diseño:

- **Carga principal en nube:** el núcleo transaccional de preventa, reparto y canal moderno, la analítica, la integración y el almacenamiento consolidado se ejecutan en AWS sa-east-1, con escalado elástico para el peak de septiembre.
- **Autonomía total de la operación de bodega:** la preparación, el despacho, la recepción y el conteo corren siempre contra los servidores del centro de distribución, no contra la nube, de modo que la conexión a Internet no interviene en la operación de bodega.

La Figura [1](#fig:vista-general) presenta la vista general de la arquitectura física híbrida. Su recorrido por bloques permite situar los componentes y sus conexiones antes de examinar cada parte de la solución.

<a id="fig:vista-general"></a>
![](https://raw.githubusercontent.com/PatricioH315/LafroX/95ed2c9a1cc20aa7ad9f3ebbe03cafa0e1e1259c/04/figuras/fisica/Arquitectura_Fisica_General.png)

**Figura 1.** Vista general de la arquitectura física híbrida

*Fuente: elaboración propia.*

La Figura [1](#fig:vista-general) se lee de arriba hacia abajo en tres franjas. En la franja superior están quienes llegan desde fuera de la red del CLIENTE: clientes, proveedores y transportistas por los portales; preventistas y conductores con sus terminales EC55 y TC58e, que leen el termógrafo del camión por Bluetooth (BLE); la casa matriz y el teletrabajo; y las cadenas de supermercados. Cada grupo entra por una puerta distinta. Los portales y los terminales pasan por el borde global (Route 53, Shield Advanced, AWS WAF y CloudFront) hacia API Gateway; la casa matriz y el teletrabajo usan Verified Access; y las cadenas intercambian mensajes por el canal AS2 detrás del Network Load Balancer. Los recorridos y controles de entrada se detallan en la sección [4.2.5](#sec:conexiones).

En la franja central, la región primaria sa-east-1 reúne en la VPC de producción el balanceador privado de aplicación, la aplicación en ECS Fargate, Keycloak, ElastiCache, Aurora PostgreSQL y AWS DMS, que copia los cambios del PostgreSQL de Talca (VM-02) a un esquema de réplica de solo lectura en Aurora. Fuera de esa VPC quedan los servicios regionales DynamoDB, S3, SQS FIFO e IoT Core, que recibe la telemetría de cadena de frío por MQTTS, y la VPC Hub, donde Transit Gateway y la VPN Site-to-Site enlazan la nube con los sitios. La región us-east-1 recibe las réplicas de Aurora PostgreSQL, DynamoDB y S3 para la recuperación ante desastres. Esta franja se detalla en la Figura [4](#fig:nube) de la sección [4.2.3](#sec:servicios-nube), con la distribución por zona de disponibilidad, los servicios de operación y seguridad y la réplica reducida de aplicación en us-east-1.

En la franja inferior están las cinco instalaciones con cómputo, cada una con su par de firewalls y su switching, y conectada a la VPC Hub por su propio túnel VPN. El CD Talca aloja un clúster Proxmox VE con Ceph de tres nodos y seis máquinas virtuales, junto al ERP de 2017 y al respaldo NAS WORM; el CD Concepción, un servidor Proxmox de nodo único con cuatro máquinas virtuales; y cada una de las tres plataformas de cross-docking, un mini-PC industrial con Docker. En los dos centros de distribución, los terminales MC9400 trabajan por Wi-Fi 6E y el gateway IoT recoge los sensores de las cámaras; en los cross-docking, los terminales inalámbricos trabajan contra el mini-PC. Cada tipo de sitio tiene su propia figura de detalle: el cross-docking en la Figura [2](#fig:crossdocking) (sección [4.2.2](#sec:emplazamiento)), el CD Talca en la Figura [13](#fig:cd-talca) (sección [4.3.1](#sec:d-especificaciones-del-sitio-principal-on-)) y el CD Concepción en la Figura [16](#fig:cd-concepcion) (sección [4.3.2](#sec:e-especificaciones-del-sitio-secundario-y-)).

La figura muestra la regla que ordena el diseño: la bodega confirma sus operaciones contra el WMS del sitio, y la nube concentra los servicios comunes, la consolidación de datos y la recuperación. Talca replica los cambios de VM-02 a Aurora por DMS; Concepción y los cross-docking envían sus eventos por colas. Si cae el enlace, las bases y los brokers locales permiten seguir operando y entregan los eventos retenidos al reconectar.

Este apartado se ordena en seis partes:

- Sección [4.2.1](#sec:implementos): equipamiento y software provistos, resumidos y analizados; el detalle elemento por elemento figura en el Formulario T-11, que acompaña a este subdocumento como archivo propio (LAFROX-Formulario-T-11).
- Sección [4.2.2](#sec:emplazamiento): ubicación de cada componente en la nube o en las instalaciones según el Artículo 16.2 (Bases Administrativas, Art. 16.2, p. 11).
- Sección [4.2.3](#sec:servicios-nube): servicios contratados en la plataforma de nube.
- Sección [4.2.4](#sec:despliegue): puesta en marcha y operación, ambientes y ciclo de entrega, red de despliegue, alta disponibilidad, recuperación ante desastres, respaldos y verificación.
- Sección [4.2.5](#sec:conexiones): conexiones, puntos de falla y contingencia de cada uno.
- Sección [4.2.6](#sec:dimensionamiento): dimensionamiento y plan de capacidad derivados de la volumetría del caso.

Las especificaciones del data center primario y del secundario se desarrollan en el apartado [4.3](#cap:4-3-data-center), a continuación de este.


<a id="sec:implementos"></a>
## 4.2.1 Especificaciones Implementos a proveer (Hardware y Software)

Esta sección resume y analiza el equipamiento y el software que la solución requiere en las instalaciones del CLIENTE, en el terreno y en la plataforma de nube. El detalle de cada elemento, con su producto ofertado, su ubicación, su cantidad y su justificación, se entrega en el Formulario T-11. El equipamiento físico lo adquiere el CLIENTE, y el adjudicatario lo especifica, instala, integra y mantiene durante el contrato.

### 4.2.1.1 Síntesis del equipamiento por familia

La Tabla [1](#tab:t26) cruza cada familia de equipamiento con el sitio donde se instala. Las cifras son las unidades en operación; la reserva se analiza a continuación de la tabla.

<a id="tab:t26"></a>
**Tabla 1.** Equipamiento en operación por familia y por sitio
| Familia | Talca | Concepción | Cada cross-docking | Terreno |
| --- | --- | --- | --- | --- |
| Servidores y nodos de cómputo | 3 | 1 | 1 | – |
| Respaldo local (NAS WORM) | 1 | – | – | – |
| Firewalls | 2 | 2 | 2 | – |
| Switches de núcleo, de gestión y de sitio | 3 | 2 | 1 | – |
| Switches de acceso en las bodegas | 4 | 2 | – | – |
| Puntos de acceso Wi-Fi 6E | 39 | 20 | 2 | – |
| Terminales de bodega | 120 | 60 | 2 | – |
| Impresoras de andén | 4 | 2 | – | – |
| Balanzas de recepción | 2 | 1 | – | – |
| Puntos de temperatura en cámaras | 15 | 6 | – | – |
| Gateways IoT | 2 | 1 | – | – |
| Estaciones de trabajo | 5 | 3 | – | – |
| Terminales de preventa | – | – | – | 62 |
| Equipos de reparto por camión | – | – | – | 96 |
| Termógrafos de camión | – | – | – | 28 |

La tabla muestra que la operación se concentra en el terreno y en las bodegas, no en la sala técnica. Solo en la calle trabajan 62 terminales de preventa y 96 camiones equipados, cada uno con un terminal de conductor, una impresora de cabina y un terminal de pago; en las bodegas y en los cross-docking, 186 terminales y los puntos de acceso que los conectan. Frente a eso, el cómputo y el almacenamiento suman 8 equipos: 3 servidores en Talca, 1 en Concepción, 3 mini-PC y la NAS. Esa proporción refleja el caso, donde la operación ocurre en la calle, en la cámara y en el andén, y explica por qué la gestión de dispositivos (N-13) es un componente con emplazamiento propio y no un accesorio.

Los equipos de reparto se cuentan por camión y no por conductor, porque los conductores de los transportistas rotan sin aviso y el equipo queda en el vehículo (S-30). Los terminales de bodega se comparten entre turnos, como contempla el perfil operacional del caso (RT-12.11; Bases Técnicas del caso, Cap. 15, p. 27), por lo que su cantidad la fija el turno con más personas trabajando a la vez: los 120 preparadores nocturnos de Talca y los 60 de Concepción (S-39); la carga de los camiones la hace esa misma cuadrilla (S-33). Los puntos de acceso son una estimación preliminar por superficie, con mayor densidad dentro de las cámaras, que el estudio de cobertura confirma (S-36).

A las unidades en operación se suma la reserva del numeral 8.4 de las Bases Técnicas Transversales (Cap. 8, p. 19): el 10 % del parque de cada tipo de dispositivo y de componente crítico, redondeado hacia arriba. Con ella se cotizan 69 terminales de preventa, 106 de cada equipo de reparto, 205 terminales de bodega, 72 puntos de acceso, 7 impresoras de andén, 4 balanzas, 7 módulos y 24 sondas de temperatura, 31 termógrafos y 4 gateways IoT, además de una unidad de reserva por cada modelo de equipo de red y para el mini-PC: una para los firewalls de los centros de distribución, una para los de los cross-docking, una para los switches de núcleo, una para los de acceso, una para los de los cross-docking y una para el mini-PC. El switch de gestión no lleva reserva, porque su falla no detiene la operación. Los servidores no llevan una unidad entera de reserva: se cubren con repuestos por componente, como discos y fuentes. A tres años, el crecimiento de los viajes y de la dotación que proyecta el caso agrega 15 unidades de cada equipo de reparto, 8 terminales de preventa y 28 terminales de bodega (S-31, S-32); los termógrafos no crecen, porque el caso no proyecta más camiones con equipo de frío (S-38). El detalle elemento por elemento está en el Formulario T-11, el cálculo de cada cantidad en el Anexo 4.B y los supuestos en el registro del Subdocumento 3.

Se proveen ocho estaciones nuevas para despacho, administración, planificación, calidad y TI. Los equipos existentes de los usuarios de oficina se incorporan a la gestión central con CrowdStrike Falcon, cifrado de disco, parches y control de extraíbles como condición de acceso por Verified Access (sección [4.4.16](#sub:adr-16)).

### 4.2.1.2 Criterios de selección

Cada familia se especifica contra una condición del caso que el equipamiento de oficina no resiste:

- Los 22 terminales de la cuadrilla de congelado están certificados para trabajar a -30 °C con guantes gruesos y batería de recambio en caliente, porque la preparación de congelados ocurre a -22 °C. Los 183 restantes atienden la bodega seca, la cámara de refrigerado sobre 0 °C y los cross-docking, y son el modelo estándar, porque esas condiciones no exigen la versión para congelado (S-34).
- Los terminales de terreno operan un turno completo sin señal, a una mano y bajo sol directo.
- Los mini-PC de los cross-docking son de rango industrial, porque las naves no tienen climatización y el supuesto de diseño es de hasta 50 °C bajo la techumbre en verano.
- Los 28 termógrafos en operación cubren los 18 camiones propios y los 10 refrigerados de los transportistas que declara el caso, porque el instrumento viaja con la carga y su registro ampara la cadena de frío aun cuando el vehículo no sea del CLIENTE; en los camiones de terceros se instala con el acuerdo de cada transportista (S-28). Están calibrados contra un patrón NIST en dos puntos, porque su registro es la prueba de la cadena de frío ante un cliente o ante la autoridad sanitaria.

En la sala técnica se aplica redundancia sin sobrecompra:

- Talca: los tres servidores del clúster son idénticos, de modo que la pérdida de cualquiera deja capacidad para todas las máquinas virtuales; el crecimiento de 3 veces se absorbe agregando discos y memoria en los mismos nodos, dentro del margen de crecimiento de los racks, y los firewalls van en par.
- Concepción: el servidor se dimensiona a su propia bodega, sin sobrecompra, y sus switches de núcleo van en par porque es el sitio de recuperación on-premise.
- Los cinco sitios: los firewalls van en par activo/pasivo, porque RT-08.03 (Bases Técnicas Transversales, Cap. 8, p. 18) no admite cortafuegos en punto único de falla. El servidor de Concepción, y el mini-PC y el switch de cada cross-docking, quedan como puntos únicos de falla aceptados, cubiertos por la operación autónoma del sitio y por la unidad de reserva que viaja en el camión de línea nocturno desde Talca.

### 4.2.1.3 Software y licenciamiento

El software de base que opera el adjudicatario es de código abierto y se organiza así:

- PostgreSQL con PostGIS, RabbitMQ, Keycloak, Proxmox VE, Ceph y Docker sostienen la plataforma, junto con el motor de optimización de rutas.
- La aplicación está escrita en PHP 8.5 con Laravel 13 y sus dependencias fijadas por Composer. Las dependencias de PHP se revisan en cada construcción con `composer audit` y su licencia se verifica contra una lista de licencias admitidas antes de incorporarlas.
- Los portales usan Angular y TypeScript; las aplicaciones de terreno usan Kotlin.

Los únicos elementos con suscripción son los servicios de la plataforma de nube, descritos en la sección [4.2.3](#sec:servicios-nube), la gestión de dispositivos, los agentes de detección en endpoints y el orquestador de integración continua GitLab CI. Esta composición mantiene la reversibilidad de la solución y evita que el CLIENTE quede atado a un licenciamiento propietario.


<a id="sec:emplazamiento"></a>
## 4.2.2 Emplazamiento de cada componente

El emplazamiento de cada componente se decide con los seis criterios del Artículo 16.2 de las Bases Administrativas (Art. 16.2, p. 11): latencia tolerada, criticidad operacional, volumen de datos, restricciones regulatorias, disponibilidad de conectividad y costo total de propiedad. En este caso la conectividad y la latencia pesan más que en una operación de oficina, porque el caso describe una red que se corta: la fibra de Talca tiene en promedio cuatro cortes al año de hasta seis horas, Concepción no tiene respaldo, los cross-docking solo tienen red móvil y en Los Ángeles la señal es intermitente justo en su ventana de madrugada, las cámaras no tienen cobertura en su interior y hay rutas sin señal durante dos horas o durante el turno completo, como describe el capítulo 6 del caso.

De esos hechos se desprende la regla que ordena todo el emplazamiento: lo que debe funcionar sin enlace vive en el sitio, y lo que escala, se comparte o está expuesto a Internet vive en la nube. Conforme a esa regla, registrada en la decisión ADR-03, los 36 componentes del catálogo se reparten en 13 de nube pura, 11 on-premise y 12 híbridos, que tienen una parte en cada dominio.

### 4.2.2.1 Instalaciones y dominios

De las seis instalaciones que cubre la solución, cinco alojan cómputo on-premise. La tipología que fija el caso se aplica así:

- El CD Talca es la sala técnica secundaria, con un clúster de tres nodos con Proxmox VE y almacenamiento Ceph que aloja las máquinas virtuales VM-01 a VM-06.
- El CD Concepción opera en un gabinete de borde, con un servidor con Proxmox VE que replica la misma pila en las máquinas VM-C01 a VM-C04.
- Las plataformas de cross-docking de Curicó, Chillán y Los Ángeles operan cada una en un gabinete de borde, con un mini-PC industrial que ejecuta el WMS en contenedores.
- La sexta instalación, la casa matriz de Talca, está junto al centro de distribución, solo aloja oficinas y trabaja contra la nube, por lo que no requiere cómputo propio y el dimensionamiento se calcula sobre los otros cinco recintos.

Los dos centros de distribución tienen su recinto especificado en el apartado [4.3](#cap:4-3-data-center); las plataformas de cross-docking no lo tienen, porque operan en un gabinete de borde dentro de la nave. La Figura [2](#fig:crossdocking) muestra ese gabinete, que se repite igual en Curicó, Chillán y Los Ángeles.

<a id="fig:crossdocking"></a>
![](https://raw.githubusercontent.com/PatricioH315/LafroX/95ed2c9a1cc20aa7ad9f3ebbe03cafa0e1e1259c/04/figuras/fisica/Arquitectura_Fisica_Crossdocking.png)

**Figura 2.** Gabinete de borde de las plataformas de cross-docking

*Fuente: elaboración propia.*

Starlink es el enlace principal y el LTE de dos proveedores lo respalda; ambos llegan a un par de firewalls compactos en alta disponibilidad, que termina el túnel VPN hacia la nube y conmuta de enlace en menos de 30 s. Detrás de los firewalls, un switch compacto conecta los dos puntos de acceso de la nave y el mini-PC industrial, que ejecuta en contenedores Docker el WMS, PostgreSQL, RabbitMQ, la caché de Keycloak y el colector ADOT. Los dos terminales inalámbricos de cada plataforma leen los códigos GS1 y trabajan contra ese WMS local. El gabinete reúne en un solo equipo las funciones que Talca y Concepción reparten en varias máquinas virtuales, y con ello opera al 100 % en local la ventana de tres horas de recepción, desconsolidación y re-despacho. El switch y el mini-PC son puntos únicos de falla aceptados, con una unidad de reserva que llega desde Talca en el camión de línea nocturno; su contingencia se trata en la sección [4.2.5](#sec:conexiones).

La séptima instalación que proyecta el caso a tres años se incorpora parametrizando la infraestructura como código, sobre el bloque de direccionamiento ya reservado en la Tabla [9](#tab:t64), sin obras en la sala de Talca.

En la nube, la región primaria es sa-east-1 y cada servicio se despliega en al menos dos zonas de disponibilidad. La región us-east-1 solo aloja la recuperación ante desastres. La Figura [3](#fig:emplazamiento-dominios) ubica cada componente en su sitio.

<a id="fig:emplazamiento-dominios"></a>
**Figura 3.** Ubicación de los componentes por dominio y por sitio

> Figura compuesta en TikZ en el LaTeX; ver main.pdf, página 19.

- Nube AWS
- **sa-east-1**, dos zonas o más<br>N-01 a N-03 Portales<br>N-04 Plataforma de aplicación<br>N-05 Base de datos en nube<br>N-06 Telemetría cruda<br>N-07 Caché<br>N-08 Ingesta de IoT<br>N-09 Mensajería<br>N-10 Plataforma analítica<br>N-12 Seguridad y gobierno<br>N-13 Gestión de dispositivos<br>Parte en nube de los híbridos
- **us-east-1**, recuperación<br>N-11 Respaldo inmutable y réplica
- On-premise
- **CD Talca**, sala técnica secundaria<br>Máquinas VM-01 a VM-06<br>con A-01 a A-05 y F-01<br>Red: D-01 en par, D-02 a D-05<br>Frío: B-01 y B-02<br>Bodega: C-03 a C-05<br>Gestión: F-02 y F-03
- **CD Concepción**, gabinete de borde<br>Máquinas VM-C01 a VM-C04<br>con A-01 a A-03, A-05 y F-01<br>Red: D-01 a D-04<br>Frío: B-01 y B-02<br>Bodega: C-03 a C-05<br>Gestión: F-03
- **Cross-docking**, tres sitios<br>Mini-PC E-01<br>con A-01 a A-03 y caché de A-05<br>Red: D-01 compacto, D-02, D-04 y D-06<br>Gestión: F-01 y F-03
- **Casa matriz**, Talca<br>Sin cómputo; usa la nube
- Terreno
- **Calle**<br>C-01 App de preventa<br>62 terminales EC55<br>C-02 App de reparto<br>96 terminales TC58e
- **Camiones de frío**<br>B-03 Termógrafos, 28
- **Locales de clientes**<br>14.200 puntos de entrega

La figura muestra que ninguna instalación depende de los sistemas de otra para operar, aunque Concepción siga recibiendo parte de su surtido desde Talca. Talca y Concepción tienen cada uno su WMS, su base, su broker y su caché de identidad; los cross-docking reúnen esas mismas funciones en un solo equipo; y el terreno lleva su propio almacén local en el dispositivo. La nube concentra lo que es común a todos los sitios: los portales, el transaccional compartido, la analítica y los servicios de seguridad. Los doce componentes híbridos aparecen en los dos dominios porque cada uno tiene una parte que debe seguir operando en el sitio y otra que consolida en la nube.

### 4.2.2.2 Correspondencia con la arquitectura lógica

La Tabla [2](#tab:mapeo-logica) asocia cada módulo y cada capa transversal de la arquitectura lógica del apartado 4.1 con el componente físico que lo ejecuta y con el lugar donde corre. Es la traza que permite seguir una responsabilidad lógica hasta su emplazamiento. Los componentes físicos se identifican con un catálogo único, agrupado por letra: A para el núcleo de bodega, B para la cadena de frío, C para los dispositivos de operación, D para la red, E para los cross-docking, F para la observabilidad y la seguridad de los nodos, y N para la nube.

<a id="tab:mapeo-logica"></a>
**Tabla 2.** Correspondencia entre la arquitectura lógica y la física
| Módulo o capa (4.1) | Componente físico (4.2) | Dónde se ejecuta |
| --- | --- | --- |
| M1 Recepción | A-01 y A-02, con C-03 y C-05 | Sitio |
| M2 Inventario | A-01 y A-02 en el sitio; N-04 y N-05 para el consolidado | Sitio y nube |
| M3 Preventa | C-01 en el terminal; N-04, N-05 y N-07 | Terreno y nube |
| M4 Rutas | N-04 y N-05; motor de optimización en su propio contenedor | Nube |
| M5 Preparación | A-01 y A-02, con C-03 y C-04 | Sitio |
| M6 Reparto | C-02 en el terminal; N-04 y N-05, con la evidencia en S3 | Terreno y nube |
| M7 Rendición | C-02; N-04; A-04 hacia el ERP | Terreno, nube y VM-04 |
| M8 Devoluciones | C-02; N-04; A-01 en la recepción del retorno | Terreno, nube y sitio |
| M9 Calidad | B-01, B-02 con el bloqueo en el borde y B-03; N-06 y N-08 | Sitio, camiones y nube |
| M10 Analítica | N-10 | Nube |
| M11 Canal moderno | N-04 con el perfil EDI y el transporte AS2; A-04 | Nube y VM-04 |
| M12 Flota | N-04 y N-06, con la API del proveedor de telemetría | Nube |
| Capa 1, portales y consolas | N-01 a N-03 y frontend de consolas en N-04 | Nube |
| Capas 2 y 3, entrada y puerta de enlace | CloudFront, WAF y API Gateway (N-01 a N-03 y N-12); puerta de API local en A-01 | Nube y sitio |
| Capa 5, integración y eventos | A-03; N-09; A-04 | Sitio y nube |
| Capa 6, datos | A-02; N-05, N-06, N-07, N-10 y N-11 | Sitio y nube |
| Capa 7, seguridad e identidad | A-05 con el verificador local; F-03; N-12 | Nube y sitio |
| Capa 8, observabilidad | F-01 y CloudWatch (N-12) | Sitio y nube |

La tabla deja M1, M2, M5 y el bloqueo de M9 en el sitio; los módulos compartidos corren en N-04 y el terreno captura en su terminal. Los perfiles de ejecución se especifican en la sección [4.2.4](#sec:despliegue).

### 4.2.2.3 Síntesis del emplazamiento por dominio y criterio

La Tabla [3](#tab:t21) resume cómo se distribuyen los 36 componentes entre los tres dominios y los seis criterios del Artículo 16.2 (Bases Administrativas, Art. 16.2, p. 11) que deciden cada emplazamiento. A continuación se justifica, dominio por dominio, por qué cada componente vive donde vive; el producto, la cantidad y la ubicación exacta de cada elemento no son materia del emplazamiento y se especifican en el Formulario T-11.

<a id="tab:t21"></a>
**Tabla 3.** Distribución de los componentes por dominio y criterio de emplazamiento
| Criterio | Nube pura | On-premise | Híbridos | Total |
| --- | --- | --- | --- | --- |
| Latencia tolerada | 1 | 4 | 1 | 6 |
| Criticidad operacional | 2 | 2 | 3 | 7 |
| Volumen de datos | 3<sup>*</sup> | — | — | 3 |
| Conectividad | — | 4 | 7 | 11 |
| Regulación | 5 | — | 1 | 6 |
| Costo total de propiedad | 3<sup>*</sup> | 1 | — | 4 |
| **Total de componentes** | **13** | **11** | **12** | **36** |

El emplazamiento responde a cuatro criterios decisivos del caso:

- Conectividad: decide once componentes y domina los on-premise e híbridos, por los cortes de enlace y el terreno sin señal.
- Regulación: decide seis y domina la nube pura, porque el Artículo 21 de las Bases Administrativas (p. 15) impide exponer los sitios a Internet y separa los públicos externos en la DMZ.
- Costo y volumen: concentran en la nube lo que escala y se paga por uso.
- Latencia y criticidad: dejan en el sitio lo que debe responder sin enlace.

La columna Total suma 37 en las filas de criterios porque la plataforma analítica (N-10) se contabiliza en los dos criterios que deciden su emplazamiento, volumen de datos y costo total de propiedad; la fila final suma los 36 componentes efectivos.

### 4.2.2.4 Componentes de nube pura

Los trece componentes de nube pura viven solo en la nube. La justificación de cada uno y el criterio del Artículo 16.2 (Bases Administrativas, Art. 16.2, p. 11) que la determina son los siguientes:

- **N-01 Portal de Clientes** (regulación): atiende el catálogo, la autoatención y el pago de los clientes desde Internet, por lo que se publica solo en la DMZ de la nube y ningún tráfico externo llega a los sitios del CLIENTE.
- **N-02 Portal de Transportistas** (regulación): los conductores externos entran con una clave de un solo uso y sin cuenta corporativa, y ese acceso se resuelve en la DMZ de la nube.
- **N-03 Portal de Proveedores** (regulación): los 180 proveedores consultan órdenes de compra, recepciones y devoluciones desde Internet, aislados de la red de bodega.
- **N-04 Plataforma de aplicación** (costo): Laravel corre en ECS Fargate con perfiles de API, reconciliación, trabajos y planificación que escalan por separado. La plataforma aloja el frontend Angular de consolas, el motor de rutas M4 y el transporte AS2 de M11 en contenedores propios; los dos últimos usan contratos versionados (ADR-11, sección [4.4.11](#sub:adr-11)).
- **N-05 Base de datos en nube** (criticidad): Aurora PostgreSQL guarda el transaccional de los módulos en nube y la réplica del WMS, conmuta entre zonas en menos de 30 s y se replica a us-east-1.
- **N-06 Telemetría cruda** (volumen): DynamoDB recibe las lecturas de temperatura sin gestión de capacidad y las expira a los 30 días, cuando ya están consolidadas en la capa analítica.
- **N-07 Caché** (latencia): ElastiCache mantiene en memoria el stock, el crédito y las sesiones para que la consulta de preventa responda en menos de 2 s.
- **N-08 Ingesta de IoT** (volumen): IoT Core recibe los 10.584 mensajes diarios de cadena de frío por MQTTS y gestiona los gateways del borde; su motor de reglas escribe cada lectura en DynamoDB y publica en SNS las que superan el umbral.
- **N-09 Mensajería** (criticidad): una cola SQS FIFO recibe la reconciliación de los sitios como sobres JSON versionados, en orden por grupo y sin duplicados; otras colas SQS, separadas de esa, transportan los trabajos internos de Laravel; y SNS difunde las alertas de excursión térmica.
- **N-10 Plataforma analítica** (volumen y costo): S3, Glue, Redshift Serverless y QuickSight conservan 5 años de datos separados del transaccional. Los tableros y la autoría de QuickSight se integran en las consolas para usuarios registrados, con modelo semántico documentado, creación autónoma de informes, exportación y permisos separados de lectura y creación; los indicadores operacionales actuales se consultan en la API de negocio.
- **N-11 Respaldo inmutable y réplica** (regulación): S3 Object Lock, AWS Backup y la réplica en us-east-1 guardan la copia que ni un administrador puede borrar y sostienen el RTO de 4 h y el RPO de 15 min.
- **N-12 Seguridad y gobierno** (regulación): KMS, Secrets Manager, WAF, Shield Advanced, Verified Access, Security Lake y CloudWatch implementan en la nube los controles del Artículo 21 de las Bases Administrativas (p. 15) definidos en la arquitectura de seguridad (apartado 4.1), como servicios que un equipo de TI de cuatro personas puede operar.
- **N-13 Gestión de dispositivos** (costo): Android Enterprise y Zebra DNA gestionan como servicio el parque de terminales de preventa, reparto y cámara, con borrado remoto selectivo y sin infraestructura en los sitios.

Ningún componente de nube pura participa en las transacciones que el caso exige resolver sin enlace: la confirmación de preparación, el despacho y el registro de entrega se ejecutan en el sitio o en el dispositivo. Lo que sube a la nube lo hace por tres razones. Los portales y la gestión de identidades externas lo hacen por regulación, porque el Artículo 21 de las Bases Administrativas (p. 15) impide exponer los sitios a Internet. La plataforma de aplicación, la analítica y la telemetría lo hacen por volumen y costo, porque su carga varía con la estación y se paga por uso. Y la seguridad y el respaldo lo hacen porque un equipo de TI de cuatro personas no puede operar esos controles en sus propios servidores.

### 4.2.2.5 Componentes on-premise

Los once componentes on-premise viven solo en las instalaciones del CLIENTE. La justificación de cada uno y su criterio:

- **B-01 Sensores de temperatura** (latencia): los 21 puntos de medición de las cámaras se leen por Modbus en el mismo sitio, porque dentro de la cámara no hay señal y la lectura no puede esperar al enlace.
- **B-02 Gateway IoT** (latencia): los gateways de Talca y Concepción detectan la excursión térmica y bloquean el despacho en menos de 5 s, con un buffer de 24 h si cae el enlace, igual a la autonomía del centro de distribución.
- **C-03 Terminales de bodega** (conectividad): los terminales MC9400 trabajan en la bodega y en las cámaras, incluido el congelado a -22 °C, sin señal móvil, contra el WMS del sitio por la red inalámbrica de la bodega.
- **C-04 Impresoras de andén** (latencia): las seis impresoras ZT411 imprimen la etiqueta SSCC en el andén al armar la unidad logística, sin salir de la red local.
- **C-05 Balanzas de recepción** (latencia): las tres balanzas envían el peso de recepción al WMS del sitio en línea, sin digitación y sin depender del enlace.
- **D-02 Switching** (criticidad): los switches de cada sitio segmentan la red local por VLAN y la mantienen operativa aunque caiga la WAN.
- **D-03 Enlace de fibra** (conectividad): es el camino principal de la VPN en Talca y Concepción, con 20 y 10 Mbps en régimen.
- **D-04 Enlace LTE** (conectividad): respalda la fibra en los CD y, con dos proveedores, respalda a Starlink en los cross-docking, con conmutación en menos de 30 s.
- **D-06 Enlace satelital** (conectividad): Starlink es el camino principal de los cross-docking, que no tienen fibra y cuya red móvil falla en la madrugada de Los Ángeles.
- **E-01 WMS de cross-docking** (criticidad): el mini-PC de cada plataforma opera 100 % en local la ventana de 3 h de recepción, desconsolidación y re-despacho, con su propio broker y su propia base.
- **F-02 Gestión de parches** (costo): Ansible aplica los parches y las líneas base CIS a los nodos de los cinco sitios por la red de gestión, sin licencia de plataforma.

En el on-premise dominan la latencia y la conectividad. Los sensores, las impresoras, las balanzas y los terminales de cámara son periféricos que trabajan donde está la mercadería, y ninguno puede depender de un enlace que el caso describe como intermitente. Los tres enlaces y el switching tampoco podrían emplazarse en otro lugar: son la infraestructura que conecta el sitio con la nube y sostiene su red interna cuando esa conexión falla.

### 4.2.2.6 Componentes híbridos

Los doce componentes híbridos tienen una parte en cada dominio. Para cada uno, la justificación explica qué parte vive en el sitio, qué parte vive en la nube y por qué se reparten así:

- **A-01 Motor WMS** (latencia): el perfil `wms_only` del artefacto Laravel, con su servidor web y PHP-FPM, corre en VM-01, VM-C01 y E-01 porque la confirmación de preparación debe responder en 1 s sin depender del enlace, y su réplica en Aurora sostiene la continuidad. El mismo motor expone la puerta de API local de la bodega, que durante un corte valida el esquema, la tasa, el UUID y la auditoría de las solicitudes de los terminales sin pasar por API Gateway.
- **A-02 Base transaccional del WMS** (criticidad): PostgreSQL 16 en VM-02 y VM-C02 es el registro de cada bodega durante un corte. AWS DMS replica los cambios de VM-02 (Talca) a Aurora para continuidad y lectura, con un RPO de 15 min mientras hay enlace; VM-C02 (Concepción) sincroniza sus eventos por las colas de integración.
- **A-03 Broker de colas** (conectividad): RabbitMQ en VM-03, VM-C04 y E-01 guarda hasta 24 h de eventos sin enlace, con mensajes persistentes y confirmación de publicación; el shipper, un proceso PHP con el adaptador AMQP `php-amqplib`, los publica como sobres JSON en SQS FIFO y solo los retira del broker cuando SQS confirma la recepción.
- **A-04 Capa anticorrupción del ERP** (criticidad): corre en VM-04 junto al ERP de 2017, que no se modifica, y el trabajador Laravel `erp-sync` de la nube la consulta por la VPN como única puerta al legado, con una clave idempotente por operación para que un reintento no emita un segundo documento tributario.
- **A-05 Identidad** (conectividad): el IdP maestro Keycloak corre en Fargate y sus cachés de solo lectura en VM-05, VM-C03 y E-01 validan las sesiones de bodega y de cross-docking sin enlace; en el mismo nodo, un verificador local habilita cada relevo de turno durante un corte con el manifiesto de turno firmado y un segundo factor local, el PIN personal.
- **B-03 Termógrafos de camión** (conectividad): los 28 termógrafos —18 en los camiones propios y 10 en los de los transportistas, instalados con el acuerdo de cada uno (S-28)— registran la temperatura durante toda la ruta sin señal y sincronizan por Bluetooth con el terminal del conductor, que alerta la excursión térmica en el momento y la reenvía a la nube cuando recupera cobertura; al volver el camión, el mismo terminal descarga el registro completo y lo envía a la nube para que IoT Core lo valide.
- **C-01 App de preventa** (conectividad): toma pedidos contra el almacén local del terminal cuando no hay señal y sincroniza por CloudFront al reconectar, sin duplicar pedidos (sección [4.2.5](#sec:conexiones)).
- **C-02 App de reparto** (conectividad): registra entregas, evidencia y cobros durante 14 h sin señal y los sincroniza con la nube al recuperar cobertura.
- **D-01 Firewall y Customer Gateway** (criticidad): el par de firewalls de cada uno de los cinco sitios termina los túneles IPsec hacia el Transit Gateway de AWS y conmutan de enlace en menos de 30 s.
- **D-05 Respaldo local** (conectividad): el NAS WORM de Talca restaura el WMS en 4 h sin depender del enlace, y su complemento inmutable vive en S3 Object Lock.
- **F-01 Telemetría de observabilidad** (conectividad): los colectores ADOT de VM-06, VM-C04 y E-01 guardan hasta 24 h de métricas y trazas en disco y las envían a CloudWatch al reconectar.
- **F-03 Detección en endpoints** (regulación): los agentes EDR de cada nodo y estación reportan a una consola central, lo que da una sola respuesta ante incidentes en nube y on-premise.

Los componentes híbridos siguen todos el mismo patrón: la parte que atiende la operación queda en el sitio y la parte que consolida queda en la nube, unidas por un mecanismo que tolera el corte. En el núcleo de bodega, Talca replica su base por DMS y los demás sitios sincronizan eventos por colas; en el terreno, el almacén local del dispositivo; y en la observabilidad, el buffer en disco de los colectores. Por eso la conectividad es el criterio dominante en siete de los doce: cada uno existe en dos lugares precisamente porque el enlace entre ellos no es confiable.

### 4.2.2.7 Autonomía de cada ámbito sin enlace

El emplazamiento anterior se verifica en lo que cada ámbito puede hacer cuando pierde el enlace. La Tabla [4](#tab:t29) declara esa autonomía y el tiempo en que cada ámbito vuelve a quedar sincronizado.

<a id="tab:t29"></a>
**Tabla 4.** Autonomía por ámbito ante la pérdida del enlace
| Ámbito | Autonomía sin enlace |
| --- | --- |
| Centros de distribución de Talca y Concepción | 24 h o más, con reconciliación determinista |
| Terreno | 14 h, un turno completo |
| Cross-docking | 24 h o más; la ventana de 3 h opera 100 % local |
| Sincronización al reconectar | CD en 2 h; flota en 10 min |

Durante la autonomía, cada ámbito mantiene su operación completa contra sus datos locales:

- El centro de distribución sigue con recepción, preparación, despacho, conteo cíclico y trazabilidad contra la base local.
- El terreno sigue con toma de pedido, entrega, evidencia, devoluciones y cobros contra el almacén local del dispositivo.
- El cross-docking mantiene recepción, desconsolidación, validación de frío y re-despacho.

Al reconectar, el vuelco ocurre en orden estricto, sin duplicados y con reconciliación determinista.

La autonomía de cada ámbito cubre el corte más largo que describe el caso para ese lugar. Las seis horas del peor corte de fibra de Talca quedan dentro de las 24 horas del centro de distribución, y la ruta rural que recupera cobertura solo al regresar queda dentro del turno de 14 horas del terreno. Los tiempos de sincronización se sostienen con los enlaces dimensionados en la sección [4.2.6](#sec:dimensionamiento), y lo que ocurre ante cada falla se desarrolla en la sección [4.2.5](#sec:conexiones).


<a id="sec:servicios-nube"></a>
## 4.2.3 Servicios contratados en la plataforma de nube

La plataforma de nube es Amazon Web Services. Todos los servicios se contratan en cuentas del CLIENTE, organizadas bajo AWS Control Tower con una cuenta por ambiente, de modo que la propiedad de los datos y de la infraestructura es del CLIENTE desde el primer día. La selección sigue tres reglas:

- Preferir el servicio administrado cuando existe, porque el área de TI del CLIENTE es de cuatro personas.
- Preferir servicios compatibles con estándares abiertos, para acotar el esfuerzo de salir de la plataforma.
- Contratar en la región secundaria solo lo que la recuperación ante desastres necesita.

### 4.2.3.1 Servicios por función

La Tabla [5](#tab:servicios-nube) agrupa los servicios contratados por la función que cumplen en la arquitectura y los asocia a los componentes del catálogo que los usan. El listado servicio por servicio, con su justificación y su cantidad, se entrega en el Formulario T-11.

<a id="tab:servicios-nube"></a>
**Tabla 5.** Servicios contratados en la plataforma de nube, por función
| Función | Servicios contratados | Componentes | Región |
| --- | --- | --- | --- |
| Entrada pública | Route 53, CloudFront, AWS WAF, Shield Advanced, API Gateway pública | N-01 a N-03, N-12 | Global y sa-east-1 |
| Acceso interno | Verified Access, API Gateway privada y endpoint execute-api | N-04, N-12 | sa-east-1 y us-east-1 |
| Cómputo de aplicación | ECS Fargate, Application Load Balancer privado, Lambda autorizadora | N-04, A-05 | sa-east-1 y us-east-1 |
| Datos operacionales | Aurora PostgreSQL, Database Migration Service, DynamoDB, ElastiCache | N-05, A-02, N-06, N-07 | sa-east-1 y us-east-1 |
| Mensajería | SQS FIFO para la reconciliación, SQS para los trabajos de Laravel, SNS | N-09, A-03 | sa-east-1 |
| Integración B2B | Network Load Balancer y OpenAS2 en Fargate | N-04 (M11) | sa-east-1 |
| Internet de las cosas | IoT Core, IoT Greengrass | N-08, B-02, B-03 | sa-east-1 y borde |
| Analítica | S3, Glue, Redshift Serverless, QuickSight embebido | N-10 | sa-east-1 |
| Respaldo y recuperación | AWS Backup, S3 Object Lock, replicación de S3 entre regiones | N-11, D-05 | sa-east-1 y us-east-1 |
| Red y conectividad | VPC, Transit Gateway, Site-to-Site VPN, NAT Gateway, VPC Endpoints | D-01 | sa-east-1 y us-east-1 |
| Identidad, claves y secretos | KMS, Secrets Manager, Parameter Store, IAM Identity Center | A-05, N-12 | sa-east-1 y us-east-1 |
| Detección y cumplimiento | Security Lake, GuardDuty, Security Hub, Inspector, Macie, CloudTrail, Config | N-12, F-03 | sa-east-1; CloudTrail, GuardDuty y Config también en us-east-1 |
| Operación y gobierno | CloudWatch, Systems Manager, Control Tower, Organizations, Cost Explorer, Budgets | F-01, F-02, N-12 | sa-east-1 |
| Construcción y registro de imágenes | CodeBuild, Elastic Container Registry | N-04, A-01 | sa-east-1 |
| Servicios de terceros en nube | Android Enterprise y Zebra DNA; consola del EDR | N-13, F-03 | Servicio gestionado |

La tabla distingue los servicios de entrada, aplicación y datos. La aplicación corre en contenedores administrados; la única función Lambda autoriza las API REST. Los portales Angular se sirven desde S3 privado por CloudFront, y las consolas Angular desde Fargate. Las colas SQS de trabajos de Laravel están separadas de la cola FIFO de reconciliación; ElastiCache solo actúa como caché. El recorrido de acceso se precisa en la sección [4.2.5](#sec:conexiones).

### 4.2.3.2 Región secundaria y residencia de los datos

La región us-east-1 no es una segunda producción. Solo contiene recursos para la recuperación:

- Datos: réplica de Aurora mediante Aurora Global Database y de las tablas de temperatura de DynamoDB mediante Global Tables.
- Respaldos: copia de los buckets de S3 salvo el de geolocalización y copias de AWS Backup.
- Aplicación: réplica reducida de ECS que escala a carga completa en menos de 30 minutos durante una conmutación.

La analítica y los datos de geolocalización de personas quedan fuera de esa región por diseño, con los resguardos de residencia de la sección [4.3.2](#sec:e-especificaciones-del-sitio-secundario-y-).

### 4.2.3.3 Servicios que no se contratan

Los registros de decisión descartan de forma expresa los siguientes servicios y productos, que no aparecen en la arquitectura:

- No se instala Redis ni Laravel Horizon en los sitios, porque la continuidad local descansa en PostgreSQL y RabbitMQ, y un tercer motor por sitio agregaría operación sin beneficio.
- No se contrata un clúster de Kubernetes (EKS), porque el caso no exige desplegar ni escalar cada módulo por separado y el equipo de TI no operaría su plano de control.
- No se contrata Kafka administrado (MSK), porque RabbitMQ en cada sitio y SQS FIFO en la nube resuelven el orden y la durabilidad con menos operación.
- No se contratan servicios de trazas y métricas separados de CloudWatch, porque las Bases piden una sola plataforma de observabilidad para nube y on-premise.
- No se autoaloja un gestor de secretos, porque Secrets Manager rota las credenciales sin el desellado manual que exigiría uno propio.

### 4.2.3.4 Modelo de contratación

Los servicios se contratan por uso, con la capacidad base comprometida mediante Savings Plans y el peak de septiembre cubierto con capacidad efímera que se libera al terminar. Los ambientes de Desarrollo, QA y Preproducción se reducen o apagan fuera del horario de uso. La reversibilidad está asegurada por la elección de servicios: Aurora es compatible con PostgreSQL, los datos analíticos se guardan en formato Parquet, y Keycloak, Laravel, PostgreSQL y RabbitMQ son de código abierto, de modo que un traslado a otra plataforma conserva la aplicación y los datos y se concentra en sustituir los servicios administrados de AWS que la solución consume. Los montos de estos servicios se declaran en la Oferta Económica y no en este documento.

### 4.2.3.5 Topología de los servicios

La Figura [4](#fig:nube) ubica en la topología de AWS los servicios de la Tabla [5](#tab:servicios-nube) y los recursos de la región secundaria: el borde global, la región primaria sa-east-1 con sus dos zonas de disponibilidad y la región de recuperación us-east-1. Los servicios de gobierno de cuentas de la tabla (Control Tower, Organizations, Cost Explorer y Budgets) se aplican sobre las cuentas y no ocupan un lugar en la topología, por lo que no se dibujan.

<a id="fig:nube"></a>
![](https://raw.githubusercontent.com/PatricioH315/LafroX/95ed2c9a1cc20aa7ad9f3ebbe03cafa0e1e1259c/04/figuras/fisica/Arquitectura_Fisica_Nube.png)

**Figura 4.** Topología de los servicios en AWS: región primaria sa-east-1 y región de recuperación us-east-1

*Fuente: elaboración propia.*

La figura se recorre desde la entrada. En el borde global, Route 53 resuelve los nombres, y AWS WAF y Shield Advanced protegen a CloudFront, que sirve los portales desde S3 y reenvía las llamadas a la API Gateway pública. La Lambda autorizadora valida el token de las rutas protegidas de la API pública y de la API privada; los endpoints OIDC de autenticación pasan sin autorizador hacia Keycloak. La casa matriz y el teletrabajo entran por Verified Access al balanceador privado de aplicación, y las cadenas de supermercados llegan por el Network Load Balancer al transporte AS2.

Dentro de la VPC de producción, cada zona de disponibilidad tiene su propia copia de ECS Fargate, Keycloak y ElastiCache. Aurora PostgreSQL tiene el escritor en sa-east-1a y el lector promovible en sa-east-1b, y AWS DMS escribe en el escritor la réplica del PostgreSQL de Talca. Los VPC endpoints conectan Fargate con los servicios regionales sin salir a Internet. Esos servicios quedan fuera de las zonas porque AWS los opera en varias zonas de forma nativa: IoT Core escribe las lecturas de frío en DynamoDB, SQS FIFO recibe la reconciliación de los sitios, SNS difunde las alertas, ECR guarda las imágenes y AWS Backup custodia las copias; la analítica fluye de S3 a Glue, Redshift y QuickSight. El bloque de operación y seguridad (CloudWatch, CloudTrail, Config, GuardDuty, Security Hub, KMS, Secrets Manager, Systems Manager, IAM Identity Center e Inspector) es transversal a toda la región, y la VPC Hub recibe los túneles de los cinco sitios.

La región us-east-1 repite la cadena de entrada con capacidad reducida: API Gateway, la Lambda autorizadora, Verified Access y una VPC de recuperación con balanceador, Fargate, Keycloak y la réplica secundaria de Aurora, además de su propio Transit Gateway y su VPN para reconectar los sitios. La figura muestra así dos propiedades del diseño: ningún componente con estado depende de una sola zona de disponibilidad, y la recuperación regional no exige reconstruir la entrada, porque la réplica solo escala. Los tiempos de esa conmutación se fijan en el apartado [4.3](#cap:4-3-data-center).


<a id="sec:despliegue"></a>
## 4.2.4 Arquitectura de despliegue

La arquitectura física describe qué componentes existen, dónde viven y cómo se conectan. Esta sección describe cómo esa solución se pone en marcha y se mantiene en operación durante los 56 meses del contrato: por qué ambientes pasa un cambio antes de llegar a las bodegas y a la calle, sobre qué red se despliega, cómo sigue operando cuando algo falla y cómo se recupera cuando se pierde un sitio completo o se daña un dato. Los puntos de falla de cada conexión y de cada equipo, con su resolución inmediata, se declaran en la sección de conexiones y contingencia (Tablas [14](#tab:fallas-sitios) y [15](#tab:fallas-nube)); aquí se describen los mecanismos que sostienen esa continuidad y cómo se verifican.

Esos mecanismos son tres y no se sustituyen entre sí. La alta disponibilidad responde a la falla de un componente sin que la operación lo note. La recuperación ante desastres responde a la pérdida de un sitio o de una región completa. El respaldo responde al daño del dato, sea un borrado accidental, una corrupción o un cifrado malicioso, frente a los cuales las réplicas no protegen, porque replican el daño con la misma fidelidad que una escritura legítima.

<a id="sub:1-ambientes-de-despliegue-rt-04-01"></a>
### 4.2.4.1 Ambientes y ciclo de entrega

Un cambio recorre tres ambientes antes de llegar a Producción: Desarrollo, QA y Preproducción. Se construye y se prueba de forma unitaria en Desarrollo, se valida en QA con pruebas funcionales, de integración y de regresión automatizadas, y se ensaya en Preproducción, donde ocurren las pruebas de aceptación, de carga y de resiliencia y el ensayo del paso a producción. Solo entonces se promueve a Producción, sin recompilar, de modo que el artefacto que llega a producción es el mismo que se probó. La marcha blanca de cada etapa ocurre ya en Producción, porque es operación supervisada con datos y usuarios reales en paralelo con la operación vigente. Un quinto ambiente, de Recuperación ante Desastres, sostiene la continuidad: reside en la región us-east-1 para el dominio de nube, mientras que la recuperación del dominio on-premise la asume el CD Concepción, que forma parte de Producción, como se describe en la recuperación ante desastres de esta sección. La Tabla [6](#tab:t62) muestra cada ambiente con su bloque de direccionamiento, su región y su función.

<a id="tab:t62"></a>
**Tabla 6.** Ambientes de despliegue
| Ambiente | VPC | Región | Función |
| --- | --- | --- | --- |
| Desarrollo | 10.104.0.0/16 | sa-east-1 | Construcción y pruebas unitarias |
| QA | 10.103.0.0/16 | sa-east-1 | Pruebas funcionales, de integración y de regresión; análisis dinámico |
| Preproducción | 10.102.0.0/16 | sa-east-1 | Aceptación, carga, resiliencia y ensayo del paso a producción |
| Producción | 10.101.0.0/16 | sa-east-1 | Operación en varias zonas, con los sitios on-premise; marcha blanca |
| Recuperación ante Desastres | 10.201.0.0/16 | us-east-1 | Réplica en caliente del dominio de nube; el dominio on-premise se recupera en el CD Concepción |

Cada ambiente reside en una cuenta AWS propia, bajo una organización de AWS Control Tower cuyas políticas de control de servicio impiden que un error o un acceso indebido en un ambiente alcance a otro; la organización incorpora además sus cuentas de gestión, de archivo de registros y de auditoría. Los bloques de direccionamiento no se solapan entre sí ni con los de los sitios on-premise, y solo el ambiente de recuperación reside fuera de la región primaria. Los cinco ambientes quedan habilitados y operativos en el hito H3 del Formulario E-25, en el mes 6 del contrato, antes de la primera marcha blanca (RT-04.01; Bases Técnicas Transversales, Cap. 4, p. 10).

En la nube, en los cinco ambientes, la imagen de la aplicación corre en ECS Fargate, que es el cómputo de la plataforma de aplicación N-04 (Tabla [5](#tab:servicios-nube)); cada ambiente despliega la imagen en su propia cuenta, desde el mismo Elastic Container Registry de sa-east-1. Los ambientes se diferencian en su escala y en su conectividad, no en el servicio donde corre el código: Producción opera en dos zonas; Preproducción replica esa topología; Desarrollo, QA y Preproducción se reducen o apagan fuera del horario de uso; y Recuperación ante Desastres mantiene la réplica reducida de us-east-1.

Desarrollo y QA son aislados y se reconstruyen desde código. Desarrollo trabaja con datos sintéticos o anonimizados, y QA con un juego de datos de prueba controlado y versionado que se restituye a un estado conocido antes de cada ciclo de pruebas. Ningún ambiente no productivo recibe datos productivos sin anonimización o seudonimización verificable. Desarrollo, QA y Preproducción se reducen o apagan fuera del horario de uso, con el ahorro reflejado en la estructura de costos (RT-04.13; Bases Técnicas Transversales, Cap. 4, p. 11).

Las bodegas no tienen ambientes propios de prueba, y no los necesitan. El on-premise es producción: la imagen wms_only que corre en los centros de distribución y en los cross-docking es la misma que recorrió Desarrollo, QA y Preproducción en la nube, y la infraestructura de cada sitio se declara como código versionado. Lo que se ensayó en la nube es, por lo tanto, lo que se instala en Talca, en Concepción y en cada cross-docking, sitio por sitio. QA y Preproducción ensayan esa imagen con el verificador local de identidad y la puerta de API local del WMS, con adaptadores simulados del ERP, y reproducen el corte de enlace y el relevo de turno antes de cada paso a producción.

Preproducción es equivalente a Producción en versiones, configuración, dimensionamiento y topología de nube (RT-04.02; Bases Técnicas Transversales, Cap. 4, p. 10). Subsisten tres diferencias justificadas:

1. Preproducción se reduce o apaga fuera del horario de uso, por costo.
2. Preproducción trabaja con datos sintéticos generados desde la volumetría del caso, cuya anonimización se verifica con Amazon Macie, porque no se admiten datos productivos reales fuera de Producción sin anonimización verificable.
3. Preproducción emula el sitio on-premise dentro de su propia VPC, con la misma imagen wms_only, el mismo broker y el mismo verificador local, pero sin túnel hacia las bodegas, para que un ensayo no pueda alcanzar la operación real.

La emulación reproduce la topología del sitio y no su hardware; por eso la primera instalación de cada versión en los centros de distribución y los cross-docking avanza sitio por sitio, como se describe en la liberación. Durante las pruebas de carga y estrés de la Tabla [26](#tab:t86) opera con el dimensionamiento completo de Producción.

Las figuras siguientes muestran cada uno de los cinco ambientes. Desarrollo, QA y Preproducción residen solo en la nube. Producción y Recuperación ante Desastres son mixtos: Producción abarca la nube y los sitios on-premise, y Recuperación ante Desastres cubre la indisponibilidad de la región o del sitio primario (numeral 4.1 de las Bases Técnicas Transversales (Cap. 4, p. 10)) con un sitio por dominio, la región us-east-1 para la nube y el CD Concepción para el on-premise; Concepción es, a la vez, un sitio de Producción que opera todos los días. No existe un ambiente solo on-premise.

La Figura [5](#fig:amb-desarrollo) muestra la secuencia de despliegue de Desarrollo: la imagen que produce la cadena de entrega se despliega en ECS Fargate con la configuración y los secretos del ambiente, y los portales se publican en S3 privado, servidos por CloudFront.

<a id="fig:amb-desarrollo"></a>
![](https://raw.githubusercontent.com/PatricioH315/LafroX/95ed2c9a1cc20aa7ad9f3ebbe03cafa0e1e1259c/04/figuras/fisica/ambientes/amb_desarrollo.png)

**Figura 5.** Ambiente de Desarrollo

*Fuente: elaboración propia.*

QA sigue la misma secuencia en su propia cuenta y su propia VPC, con la misma imagen que recorrió Desarrollo (Figura [6](#fig:amb-qa)).

<a id="fig:amb-qa"></a>
![](https://raw.githubusercontent.com/PatricioH315/LafroX/95ed2c9a1cc20aa7ad9f3ebbe03cafa0e1e1259c/04/figuras/fisica/ambientes/amb_qa.png)

**Figura 6.** Ambiente de QA

*Fuente: elaboración propia.*

En Preproducción la secuencia se ensaya sobre la topología de Producción y el sitio on-premise emulado: las migraciones en Aurora y el despliegue azul-verde con canario se demuestran aquí antes de cada paso a producción (RT-04.07; Figura [7](#fig:amb-preproduccion); Bases Técnicas Transversales, Cap. 4, p. 11).

<a id="fig:amb-preproduccion"></a>
![](https://raw.githubusercontent.com/PatricioH315/LafroX/95ed2c9a1cc20aa7ad9f3ebbe03cafa0e1e1259c/04/figuras/fisica/ambientes/amb_preproduccion.png)

**Figura 7.** Ambiente de Preproducción

*Fuente: elaboración propia.*

En Producción la misma secuencia se ejecuta de forma automática y llega además a los sitios on-premise por el Transit Gateway y la Site-to-Site VPN de la VPC Hub, sitio por sitio (Figura [8](#fig:amb-produccion)).

<a id="fig:amb-produccion"></a>
![](https://raw.githubusercontent.com/PatricioH315/LafroX/95ed2c9a1cc20aa7ad9f3ebbe03cafa0e1e1259c/04/figuras/fisica/ambientes/amb_produccion.png)

**Figura 8.** Ambiente de Producción

*Fuente: elaboración propia.*

Recuperación ante Desastres tiene dos sitios, uno por dominio: en la región us-east-1, la réplica reducida recibe cada versión liberada en Producción; en el on-premise, el CD Concepción promueve su WMS con la misma imagen si se pierde Talca (Figura [9](#fig:amb-recuperacion)).

<a id="fig:amb-recuperacion"></a>
![](https://raw.githubusercontent.com/PatricioH315/LafroX/95ed2c9a1cc20aa7ad9f3ebbe03cafa0e1e1259c/04/figuras/fisica/ambientes/amb_recuperacion.png)

**Figura 9.** Ambiente de Recuperación ante Desastres

*Fuente: elaboración propia.*

El paso de un ambiente a otro lo controla el pipeline de integración continua: GitLab CI lo orquesta y AWS CodeBuild construye cada imagen de forma hermética, con procedencia SLSA nivel 3. Cada cambio instala las dependencias exactamente como las fija `composer.lock` y pasa por estos controles (RT-04.05; Bases Técnicas Transversales, Cap. 4, p. 10):

- Auditoría de dependencias con `composer audit` y pruebas PHPUnit.
- Análisis estático con PHPStan y Larastan, y formato con Laravel Pint.
- Pruebas de contrato contra OpenAPI 3.1 y AsyncAPI 2.6.
- Escaneo de secretos y de imágenes de contenedor, y medición de cobertura.

El pipeline bloquea el despliegue ante un hallazgo crítico o alto, ante un contrato público roto sin versión nueva o ante una cobertura de la lógica de negocio inferior al 70 % (RT-04.11; Bases Técnicas Transversales, Cap. 4, p. 11). Primero, la imagen aprobada se firma, se publica en Elastic Container Registry y se promueve por su digest, de modo que ningún ambiente recompila; el paso a Producción es automático una vez que la versión supera los controles del pipeline y el ensayo en Preproducción, dentro de las ventanas de la Tabla [8](#tab:jd02) (RT-04.06; Bases Técnicas Transversales, Cap. 4, p. 11). Segundo, la configuración no sensible se externaliza por ambiente en SSM Parameter Store y los secretos se gestionan en AWS Secrets Manager con rotación automática (sección [4.4.15](#sub:adr-15)); la imagen no contiene secretos ni el archivo de entorno (RT-04.08 y RT-04.09; Bases Técnicas Transversales, Cap. 4, p. 11). Tercero, las migraciones de base de datos son migraciones Laravel basales y aditivas, que siguen la estrategia de expandir y contraer: se ejecutan como un paso único del despliegue antes de cambiar el tráfico, cada versión solo agrega estructuras, de modo que la versión anterior y la nueva de la aplicación funcionan sobre el mismo esquema durante el despliegue, y las estructuras obsoletas se eliminan en una versión posterior. Cada migración declara además su reversión, de modo que el esquema puede volver a la versión anterior (RT-04.10; Bases Técnicas Transversales, Cap. 4, p. 11). Luego, el código reside en un repositorio con ramas protegidas, revisión obligatoria por pares y sin escritura directa sobre la rama principal (RT-04.03; Bases Técnicas Transversales, Cap. 4, p. 10); su gobierno y la trazabilidad se desarrollan en el plan de calidad (Subdocumento 9).

A Producción no se llega de otra forma: su acceso es restringido y auditado, y los desarrolladores no tienen acceso interactivo directo a ese ambiente (numeral 4.1 de las Bases Técnicas Transversales (Cap. 4, p. 10)). El acceso privilegiado excepcional reúne estos controles:

- IAM Identity Center federado con Keycloak por SAML 2.0 y SCIM, y MFA.
- Conjuntos de permisos temporales con aprobación previa y sesiones ECS Exec o Session Manager con registro de comandos y salida.
- SSH y el reenvío de puertos bloqueados.

La cuenta de último recurso (sección [4.4.15](#sub:adr-15)) se usa solo ante la indisponibilidad del IdP, con doble custodia, alerta inmediata, rotación de credenciales tras su uso y revisión posterior registrada.

Los portales de clientes, transportistas y proveedores siguen el mismo ciclo: su aplicación Angular se publica por ambiente en S3 privado y CloudFront, con la imagen de aplicación del mismo ambiente como backend. Las consolas Angular, en cambio, corren como contenedor en ECS Fargate tras el balanceador de aplicación privado (N-04).

#### 4.2.4.1.1 Artefacto y perfiles de ejecución

La aplicación se construye una sola vez por versión como una imagen PHP 8.5 con Laravel 13 que contiene el código, el `vendor` resuelto desde `composer.lock`, PHP-FPM, el intérprete de línea de comandos y las extensiones que la solución usa: `pdo_pgsql`, `mbstring`, `intl`, `openssl`, `opcache`, `curl` para el SDK de AWS, `sockets` para el adaptador AMQP `php-amqplib`, la extensión de OpenTelemetry y `pcntl`, que solo usan los procesos de línea de comandos para terminar de forma ordenada al recibir la señal de detención. Un servidor web liviano acompaña a PHP-FPM en los perfiles HTTP. La misma imagen corre en todos los ambientes y en todos los sitios; lo que cambia es el perfil con que arranca, como muestra la Tabla [7](#tab:perfiles).

<a id="tab:perfiles"></a>
**Tabla 7.** Perfiles de ejecución del artefacto Laravel
| Perfil | Proceso y función | Dónde corre | Escala por |
| --- | --- | --- | --- |
| API | Servidor web y PHP-FPM; APIs de M1–M12 para portales, preventa y reparto | N-04, ECS Fargate en 2 zonas | Procesos PHP-FPM ocupados sobre 70 %; 2 a 4 tareas, techo de 8 |
| `wms_only` | Servidor web y PHP-FPM; M1, M2, M5 y la recepción del retorno de M8, con la puerta de API local | VM-01, VM-C01 y E-01 | Fijo, dimensionado al sitio |
| Shipper | PHP CLI; lee RabbitMQ con `php-amqplib` y publica sobres JSON en SQS FIFO | VM-03, VM-C04 y E-01 | Uno por sitio |
| Consumidor de reconciliación | PHP CLI con el SDK de AWS; aplica los sobres al estado central | N-04, ECS Fargate | Edad del mensaje más antiguo; 2 a 4 tareas |
| Trabajos | PHP CLI con el trabajador de colas de Laravel; notificaciones, `erp-sync` y EDI en colas separadas | N-04, ECS Fargate | Profundidad de cada cola; 2 a 4 tareas, con `erp-sync` fijo en 2 procesos |
| Planificador | PHP CLI; tareas periódicas del ambiente | N-04, una sola tarea por ambiente | No escala |

Los perfiles comparten la revisión de código y la versión de esquema, pero cada uno tiene su propio rol de IAM o credencial local, con solo los permisos que su función necesita: el perfil de API no puede leer la cola de reconciliación, el consumidor no puede escribir en las colas de trabajos y el shipper solo puede enviar a su cola FIFO. El planificador corre como una sola tarea por ambiente, con despliegue que detiene la tarea anterior antes de iniciar la nueva, y cada tarea periódica toma además un bloqueo en la base de datos para impedir ejecuciones superpuestas; los sitios no ejecutan planificador, porque sus procesos permanentes son el servidor del WMS y el shipper. En los centros de distribución, el perfil `wms_only`, que es el Motor WMS A-01, corre como contenedor en VM-01 y VM-C01, y el shipper corre junto al broker de colas A-03, RabbitMQ, en VM-03 y VM-C04, todos sobre las máquinas virtuales de Proxmox. En cada cross-docking, el perfil `wms_only` y el shipper se orquestan con Docker Compose en E-01, junto a PostgreSQL, RabbitMQ y la caché de identidad. Los sitios descargan la imagen desde Elastic Container Registry por la VPN, a través de la VPC Hub, y los endpoints de interfaz de la VPC de Producción, en conexiones salientes y sin tráfico por Internet; Ansible (F-02), con el que se declara como código la configuración de los cinco sitios, actualiza sus contenedores sitio por sitio. La réplica reducida de us-east-1 recibe cada versión liberada en Producción desde el mismo Elastic Container Registry de sa-east-1, de modo que la plataforma que se promueve en una conmutación corre la misma versión que la región primaria. Fuera de la imagen Laravel quedan el frontend Angular de las consolas, el motor de rutas M4 y el transporte AS2 M11, los tres en contenedores propios sobre ECS Fargate (N-04) y construidos por el mismo pipeline; M4 y M11 operan además tras contratos versionados (sección [4.4.11](#sub:adr-11)).

Cada perfil cumple este ciclo de vida:

1. Arranque y compatibilidad de esquema: el contenedor verifica la versión esperada y no acepta tráfico ni mensajes si no coincide.
2. Comprobación de salud: los perfiles HTTP exponen una ruta de salud de proceso, que usa el balanceador, y otra de disponibilidad que comprueba la base y la cola; los procesos de línea de comandos informan su salud por un latido que vigila el orquestador.
3. Detención y drenaje: el balanceador deja de enviar solicitudes nuevas y espera 30 segundos a que terminen las vigentes; los trabajadores reciben la señal de detención, terminan el mensaje en curso sin tomar otro y salen antes de 120 segundos, plazo mayor que el tiempo máximo de un trabajo; el mensaje no confirmado vuelve a la cola al vencer su visibilidad.

Así, ningún reinicio, escalado o despliegue deja un trabajo a medias.

#### 4.2.4.1.2 Liberación y reversión

Cada versión se libera con estrategia azul-verde: la versión nueva se despliega junto a la vigente y recibe tráfico de forma gradual, en etapas de canario, después de haberse demostrado el mismo procedimiento en Preproducción (RT-04.07; Bases Técnicas Transversales, Cap. 4, p. 11). La puesta en producción avanza por proceso, por sitio o por zona comercial, nunca como un evento único que afecte a la vez a la bodega, la preventa, el reparto y la facturación. En la sustitución del WMS de 2013 por olas, cada capacidad se activa además por sitio mediante indicadores de funcionalidad (*feature flags*), de modo que revertir una ola es apagar su indicador, sin volver a desplegar.

Mientras dura el canario, la versión anterior permanece desplegada, por lo que revertir es devolverle el tráfico, sin recompilar ni volver a desplegar. La reversión es automática y se dispara cuando el percentil 95 de una transacción supera su umbral comprometido (Tabla [25](#tab:t84)) o cuando la versión nueva registra más errores que la estable en la misma ventana de observación. No se pierde ninguna transacción confirmada: las operaciones en curso quedan en los buffers locales, 24 horas por sitio en el broker y la caché de turno en los dispositivos, y se reprocesan de forma idempotente contra la versión restituida. El esquema no necesita revertirse durante el canario, porque la migración de la versión solo agregó estructuras; si hiciera falta, la reversión declarada de la migración lo devuelve a la versión anterior. Lo que se pierde es la versión, no la operación. El tiempo efectivo de reversión se mide en cada ensayo en Preproducción y no supera el tiempo de restauración de 4 horas del Artículo 78.3 de las Bases Administrativas (p. 40).

Si la falla de un despliegue se manifestara durante la ventana de despacho, la bodega y el reparto continuarían con su operación local (Tabla [4](#tab:t29)) mientras se revierte, sin detener la salida de los camiones.

Cada promoción ensaya además la compatibilidad de los mensajes pendientes. Un sitio puede volver de un corte de 24 horas con sobres publicados por la versión anterior, de modo que el consumidor de reconciliación acepta la versión vigente y la inmediatamente anterior del sobre JSON, y rechaza hacia la cola de mensajes fallidos cualquier versión que no reconozca, sin aplicarla. Preproducción reproduce ese caso —sitio emulado desconectado, promoción de la versión nueva y reconexión— antes de cada paso a producción.

#### 4.2.4.1.3 Transición al backend Laravel

La arquitectura lógica fija la implantación progresiva del backend (apartado 4.1). Su secuencia física es la siguiente:

1. Se registran los contratos OpenAPI y AsyncAPI, el sobre JSON y el esquema PostgreSQL de partida, que es la línea base de las migraciones Laravel.
2. Se construye el backend y se prueban las colas y la capa anticorrupción con fallas inducidas: corte de enlace, ERP caído, mensajes duplicados y fuera de orden.
3. Se habilita un sitio piloto, dimensionado por su capacidad real, con el WMS de 2013 disponible para la reversión; el tráfico se migra por olas con un único escritor autorizado para cada operación. Nunca escriben a la vez el sistema anterior y el nuevo sobre el stock, los cobros o los documentos tributarios.
4. Antes de cada corte se drenan los mensajes que el sistema nuevo no puede leer. Si algún ambiente conservara mensajes serializados por un framework anterior, se drenan o se transforman al sobre JSON antes del corte, porque Laravel no puede consumirlos.
5. Cada ola cierra verificando saldos de stock, cobros y folios contra el origen, y se revierte por sitio si falla un umbral acordado con el CLIENTE.
6. La reversión devuelve el tráfico al escritor anterior solo después de detener el nuevo, conciliar los pendientes y comprobar que el esquema sigue legible por la versión previa.

#### 4.2.4.1.4 Calendario y cadencia

El calendario de Puelche limita cuándo se puede intervenir la plataforma. El caso prohíbe intervenir los sistemas entre el 1 y el 25 de septiembre, en diciembre y durante el cierre contable de cada mes, prohíbe el paso a producción en todo septiembre y en diciembre, y exige indisponibilidad cero en la ventana de despacho (Bases Técnicas del caso, Cap. 10, restricción 8, p. 19, y Cap. 13, p. 23; RT-10.05 y RT-10.06; Bases Técnicas Transversales, Cap. 10, p. 22; Bases Técnicas del caso, Cap. 15, p. 27). La Tabla [8](#tab:jd02) cruza cada período con lo que admite.

<a id="tab:jd02"></a>
**Tabla 8.** Ventanas de despliegue
| Período | Despliegue | Indisponibilidad programada |
| --- | --- | --- |
| Todo septiembre; sin intervención alguna del 1 al 25 | No | No |
| Todo diciembre | No | No |
| Tres primeros días hábiles del mes | No | No |
| 05:30–07:00, lunes a sábado | No | No |
| 22:00–06:00, preparación de pedidos | Sí, sin interrupción | No |
| 08:00–18:00, recepción de proveedores | Sí, sin interrupción | No |
| Resto del calendario | Sí, sin interrupción | Excepcional, con aviso de 10 días hábiles |

El despliegue sin interrupción es, por lo tanto, la regla y no una capacidad opcional: solo fuera de las ventanas protegidas se admite una indisponibilidad programada, y únicamente por excepción. En la ventana nocturna, además, toda intervención en bodega considera el turno de preparación. Descontados los congelamientos, quedan unos diez meses desplegables al año, de los que se excluyen los tres primeros días hábiles de cada mes. Sobre ese margen se fija una cadencia quincenal de despliegue y un tiempo de hasta cinco días hábiles desde que se confirma un cambio de código hasta que llega a producción, compatible con el plazo de siete días corridos para remediar una vulnerabilidad crítica (Artículo 21.1 de las Bases Administrativas (Bases Administrativas, Art. 21.1, p. 15); RT-11.04; Bases Técnicas Transversales, Cap. 11, p. 23). La tasa de cambios fallidos no supera el 5 % de los despliegues del mes y el tiempo de restauración no supera 4 horas, conforme al Artículo 78.3 de las Bases Administrativas (p. 40); estas cuatro métricas se miden durante la Operación (RT-04.12; Bases Técnicas Transversales, Cap. 4, p. 11). Las correcciones de incidentes críticos usan el mismo pipeline, con prioridad y fuera de la cadencia quincenal, dentro del plazo de resolución de 4 horas. Cada servicio crítico tiene como presupuesto de error el complemento de su disponibilidad comprometida de 99,9 % mensual, unos 43 minutos al mes; si un servicio lo consume, se suspenden en él los despliegues que no sean correctivos hasta el mes siguiente (RT-10.09; Bases Técnicas Transversales, Cap. 10, p. 22).

<a id="sub:2-redes-topologia-segmentacion-y-conectivi"></a>
### 4.2.4.2 Red de despliegue

La sección de conexiones describe los caminos entre los sitios, el terreno y la nube, y su conmutación (Figura [10](#fig:conexiones) y Tabla [12](#tab:conexiones)). El despliegue agrega tres definiciones sobre esa red: dónde llegan los túneles, cómo se reparte el direccionamiento y cómo se dirige el tráfico entre regiones.

Los túneles de AWS Site-to-Site VPN de los cinco sitios llegan a la VPC Hub de sa-east-1, donde el Transit Gateway los enruta entre ellos y los une solo a la VPC de Producción; us-east-1 dispone de su propio Transit Gateway y de su VPN para reconectar los sitios durante una conmutación. La de Producción es la única VPC con enlace hacia los sitios, coherente con que el on-premise es producción: Desarrollo, QA y Preproducción no tienen conectividad con las bodegas, de modo que un error en un ambiente de prueba no puede alcanzarlas. El direccionamiento se asigna sin solapamiento, según la Tabla [9](#tab:t64).

<a id="tab:t64"></a>
**Tabla 9.** Direccionamiento y segmentación
| Dominio | Bloque | Segmentación |
| --- | --- | --- |
| Talca | 10.1.0.0/16 | VLAN de gestión, servidores, operación, estaciones e IoT |
| Concepción | 10.2.0.0/16 | Mismas VLAN que Talca |
| Cross-docking | 10.3.0.0/16 a 10.5.0.0/16 | VLAN de gestión y de operación tras el par de firewalls del sitio, por la VPN |
| Sitio adicional previsto | 10.6.0.0/16 | Reservado |
| VPC Producción, zona pública | 10.101.1.0/24 y 10.101.2.0/24 | NAT y Network Load Balancer del canal AS2 |
| VPC Producción, zona privada | Resto de 10.101.0.0/16 | ALB de aplicación y consolas, aplicación y datos; enlazada a los sitios por el Transit Gateway de la VPC Hub |

Cada sitio con cómputo dispone de un bloque propio, y el centro de distribución que Puelche evalúa abrir hacia 2030 en la Región de Los Lagos ya tiene el suyo reservado, de modo que su incorporación es una parametrización de la infraestructura como código (RT-02.12; Bases Técnicas Transversales, Cap. 2, p. 7; Bases Técnicas del caso, Cap. 15, p. 26). En la nube, los ALB de aplicación y consolas son privados; la subred pública solo aloja NAT y el Network Load Balancer del canal AS2. Los portales residen en S3 privado, servido únicamente por CloudFront. La VPC de Producción usa endpoints de interfaz execute-api, IoT Core, SQS, SSM y Elastic Container Registry, y endpoints de puerta de enlace para DynamoDB y S3. Como los de puerta de enlace no son alcanzables desde los sitios por la VPN, los sitios descargan la imagen por el endpoint de interfaz de Elastic Container Registry y por un endpoint de interfaz de S3, donde se almacenan las capas de las imágenes, sin salir a Internet.

El tráfico externo sigue las entradas de la sección [4.2.5.2](#sub:superficie). Route 53 conmuta el enrutamiento regional ante falla, pero la identidad, las API pública y privada y el acceso a las consolas por Verified Access deben restituirse antes de reabrir transacciones; la VPN hacia us-east-1 se activa durante la reconexión del broker (Tabla [4.3-6](#tab:4-3-6)).

La red también debe devolver a la normalidad a un sitio que operó desconectado. El compromiso es resincronizar la flota en hasta 10 minutos y un centro de distribución en hasta 2 horas después de un corte de 24 horas (Tabla [4](#tab:t29)). Un corte de 24 horas acumula los cambios de la base con su registro de escritura anticipada, el vaciado del broker, la telemetría, la observabilidad y el incremental de respaldo: unos 1,43 GB en Talca, 0,59 GB en Concepción y 0,27 GB en cada cross-docking, que se drenan en 2 horas con 1,59, 0,66 y 0,30 Mbps, respectivamente (Tabla [21](#tab:t81); Anexo 4.B). La evidencia de entrega no se suma, porque el terreno la envía por la red celular sin pasar por el centro de distribución. En el peor caso, que suma además la oficina y el retorno de la flota, la fibra de Talca queda al 26,51 % de su capacidad; y si el drenaje debe hacerse por el enlace de respaldo, ocupa el 31,88 % del LTE de Talca, el 21,93 % del de Concepción y el 14,92 % del de cada cross-docking, dentro del compromiso de 2 horas en todos los casos. Al reconectar, la calidad de servicio prioriza el broker y el registro de escritura anticipada sobre la telemetría.

<a id="sub:3-alta-disponibilidad"></a>
### 4.2.4.3 Alta disponibilidad

No todos los servicios necesitan el mismo nivel de continuidad. El Artículo 78 (Bases Administrativas, Art. 78.2, p. 40) fija cuatro niveles de servicio, y la solución asigna cada servicio a uno según el efecto de su indisponibilidad sobre la operación (RT-10.02; Bases Técnicas Transversales, Cap. 10, p. 22), como muestra la Tabla [10](#tab:jd05).

<a id="tab:jd05"></a>
**Tabla 10.** Clasificación de servicios por nivel de servicio
| Nivel | Disponibilidad | Resolución | Servicios |
| --- | --- | --- | --- |
| Crítico | 99,9 % | 4 h | Preparación y despacho en la ventana de 05:30 a 07:00, con el bloqueo por excursión térmica y la identidad de bodega que lo habilitan |
| Alto | 99,5 % | 8 h | Toma de pedido de preventa y consulta de stock y crédito, entrega y evidencia de entrega, planificación de rutas, documentos tributarios, integración con el ERP, cobranza y rendición, y registro de temperatura |
| Medio | 99,0 % | 24 h | Canal moderno (EDI), notificaciones, analítica y tableros, portales, consultas de geolocalización y registros de auditoría y seguridad |
| Bajo | 98,0 % | 48 h | Reportería e informes a pedido |

Las clases de servicio se distinguen por su alternativa operativa:

- Crítico: detiene un proceso sin alternativa; la ventana de despacho de 05:30 a 07:00 no admite ejecución manual, y el bloqueo por excursión térmica y la identidad de bodega condicionan la salida de la carga.
- Alto: tiene una alternativa costosa; la toma de pedido, la entrega y la consulta de stock y crédito siguen siendo transacciones críticas en desempeño (Tabla [25](#tab:t84)), pero el dispositivo las captura sin conexión durante un turno completo y las sincroniza al reconectar; la ruta puede planificarse a mano en 3,5 horas y las transacciones hacia el ERP se retienen en cola hasta 24 horas.
- Medio: dispone de una alternativa operativa.
- Bajo: no impide operar.

El compromiso penalizable del 99,9 % recae sobre la preparación y el despacho, que se ejecutan contra la base local del centro de distribución sin atravesar la WAN, y sobre la identidad, cuya autoridad reside en la nube y se sostiene con el despliegue en varias zonas de disponibilidad (apartado 4.3.1.2).

Esa es la razón por la que el 99,9 % de extremo a extremo no depende de multiplicar las disponibilidades de la infraestructura. El numeral 7.2 de las Bases Técnicas Transversales (Cap. 7, p. 17) fija un mínimo de 99,95 % mensual para la energía, la climatización, la red, el cómputo, la base de datos y los portales, pero esos valores son pisos por subsistema y su producto en serie quedaría por debajo del 99,9 %. El compromiso se sostiene en la redundancia interna de cada subsistema y en la ruta que sigue cada transacción. La confirmación de preparación, la más estricta, se ejecuta contra la base local del centro de distribución y no atraviesa la WAN ni la nube; descansa sobre energía y climatización en N+1, un par de firewall en alta disponibilidad, dos switches en stack, un clúster de tres nodos N+1 y almacenamiento Ceph sobre RAID 10, con un solo elemento en serie, la instancia de escritura VM-02, que se reinicia en otro nodo del clúster (Tabla [14](#tab:fallas-sitios)). La identidad, por su parte, se sostiene en la nube con Keycloak (A-05) en dos zonas y, en cada sitio, con la caché de solo lectura y el verificador local de relevo de turno.

En la nube, todos los servicios con requisito de alta disponibilidad operan en al menos dos zonas (RT-03.02; Bases Técnicas Transversales, Cap. 3, p. 8). Aurora PostgreSQL (N-05) escribe en sa-east-1a y mantiene un lector promovible en sa-east-1b, al que conmuta en menos de 30 segundos; ElastiCache mantiene primario y réplica entre esas zonas y conmuta en menos de 60 segundos; las tareas de ECS Fargate se distribuyen en ambas zonas y se reprograman solas ante la pérdida de una; y DynamoDB, el balanceador y los NAT Gateway son multizona por diseño. Estos tiempos corresponden a los que AWS declara como habituales para cada servicio y se tratan como objetivos que se miden en las pruebas de la sección [4.2.4.6](#sub:6-verificacion-de-la-continuidad). Ante el peak de septiembre, el escalamiento automático y la degradación controlada del apartado de dimensionamiento sostienen los umbrales de desempeño sin intervención.

<a id="sub:4-recuperacion-ante-desastres-ba-art-20-rt"></a>
### 4.2.4.4 Recuperación ante desastres

La recuperación ante desastres es activo-pasiva en caliente: la región us-east-1 mantiene una réplica reducida pero funcional de la plataforma, escalable a carga completa en menos de 30 minutos, que se promueve solo cuando se pierde la región primaria. Los objetivos son un RTO de hasta 4 horas y un RPO de hasta 15 minutos para los servicios críticos (RT-07.04; Bases Técnicas Transversales, Cap. 7, p. 17). Cada dominio de datos alcanza ese RPO con su propio mecanismo de replicación (Tabla [4.3-4](#tab:4-3-4)): Aurora Global Database mantiene en us-east-1 la réplica promovible de la base en nube, DynamoDB Global Tables la telemetría, y la replicación de S3 entre regiones lleva la evidencia, los documentos y las copias de AWS Backup (N-11).

Si Talca pierde sus dos caminos, la base local sigue siendo autoritativa y el slot de replicación lógica que lee AWS DMS retiene en VM-02 el registro de escritura anticipada hasta reconectar, de modo que los cambios se entregan sin pérdida al restablecer el enlace. Mientras dure el corte, en cambio, la réplica en nube queda desactualizada, hasta un máximo de 24 horas: el RPO remoto de 15 minutos rige solo con enlace y no se promete durante un corte que lo impide. El registro retenido se acota con un tope de 5 GB por slot, frente a los unos 0,123 GB diarios de registro de escritura anticipada que estima el dimensionamiento para Talca: cubre con amplio margen un corte de 24 horas y ocupa como máximo la cuarta parte de los 20 GB de disco de VM-02, sin arriesgarlo (Anexo 4.B). El retraso de replicación y el tamaño del registro retenido se miden de forma continua y generan alarma a los 5 y a los 15 minutos de retraso.

La réplica por DMS y la reconciliación por eventos cumplen funciones distintas y no se mezclan. DMS copia las tablas del WMS de Talca (VM-02) a un esquema de réplica de solo lectura en Aurora, que sirve a la continuidad y a las consultas. Concepción y los cross-docking no replican sus bases por DMS: publican sus eventos mediante los brokers y SQS FIFO. El consumidor de reconciliación aplica esos sobres JSON a las tablas de dominio del estado central —stock consolidado, trazabilidad de lotes, pedidos, entregas y cobros—, y en la misma transacción registra la clave de origen del evento, formada por el sitio y el identificador único que el evento trae desde su captura. Una restricción de unicidad sobre esa clave impide aplicar dos veces el mismo evento, aunque SQS lo entregue de nuevo o llegue después de la ventana de deduplicación de la cola. Ninguna tabla de dominio se alimenta de la réplica DMS, y ningún evento escribe en el esquema de réplica.

#### 4.2.4.4.1 Conmutación y retorno

La conmutación de región y el retorno siguen el procedimiento de la sección [4.3.2.5](#sub:conmutacion-regional) (Tabla [4.3-6](#tab:4-3-6)): el enrutamiento hacia us-east-1 conmuta de forma automática y su retorno se ejecuta de forma coordinada tras la reconciliación, mientras la promoción de la base exige la autorización del CLIENTE. Si la contingencia afecta solo a la bodega de Talca, el WMS de Concepción (VM-C01) asume su carga con un RTO adicional de 1 a 2 horas. Los sitios de recuperación y sus amenazas comunes se analizan en la Tabla [4.3-3](#tab:4-3-3).

#### 4.2.4.4.2 Operación durante una contingencia regional

Mientras la región primaria no está disponible, la bodega y el terreno siguen operando contra sus bases locales y sus dispositivos, y los servicios en nube vuelven con la promoción de la réplica. La analítica y las consultas de geolocalización de personas, excluidas de us-east-1 por diseño (sección [4.3.2](#sec:e-especificaciones-del-sitio-secundario-y-)), esperan el retorno; ninguna es un servicio crítico.

<a id="sub:5-respaldos-esquema-3-2-1-1-0-rnf-20-07"></a>
### 4.2.4.5 Respaldos

El respaldo protege contra lo que las réplicas replican: un dato borrado por error, corrompido o cifrado de forma maliciosa. La solución aplica un esquema 3-2-1-1-0 único para la nube y el on-premise, que cumple y supera el 3-2-1-0 exigido al tener a la vez una copia inmutable y una fuera de línea (RT-07.09; Bases Técnicas Transversales, Cap. 7, p. 18). Mantiene tres copias —los datos activos, las instantáneas de Aurora junto con la copia local D-05, y el respaldo exportado a S3— en dos medios, base de datos y almacenamiento de objetos. Una copia está fuera del sitio, replicada a us-east-1 por AWS Backup (N-11) y la replicación de S3, y otra es inmutable, en S3 Object Lock en modo Compliance con AWS Backup Vault Lock. El cero corresponde a los errores de verificación de restauración: cada mes se restaura una muestra rotativa que recorre todos los dominios de la Tabla [11](#tab:jd12), se mide el tiempo efectivo de restauración y todo error se corrige antes de la verificación siguiente (RT-07.12; Bases Técnicas Transversales, Cap. 7, p. 18).

La copia inmutable es el control frente a un ataque con credenciales administrativas comprometidas: en modo Compliance, ni un administrador ni la cuenta raíz pueden borrarla ni modificarla durante su retención, y el bloqueo de la bóveda, con 3 días de enfriamiento y un año de retención mínima, impide eliminar los respaldos una vez activado (RT-07.11; Bases Técnicas Transversales, Cap. 7, p. 18). La copia local D-05 cumple otra función: es la copia de recuperación rápida, cifrada con una clave independiente de la de producción, que permite restaurar el WMS en hasta 4 horas sin depender del enlace, y por eso no se cuenta como la copia inmutable. Un medio físico cifrado se rota además cada semana a una bóveda externa, y se conserva en el recinto de custodia declarado en el Formulario T-11 hasta su traslado.

La Tabla [11](#tab:jd12) muestra, para cada dominio de datos, con qué frecuencia se respalda, cuánto tiempo se retiene y en cuánto tiempo se restaura por completo (RT-07.13; Bases Técnicas Transversales, Cap. 7, p. 18).

<a id="tab:jd12"></a>
**Tabla 11.** Respaldo y restauración por dominio de datos
| Dominio | Frecuencia | Retención | Restauración |
| --- | --- | --- | --- |
| Transaccional de bodega | Continua; copia local D-05 en Talca; en Concepción y los cross-docking, reconstrucción desde el estado central | 35 días | ≤ 4 h |
| Transaccional en nube | Diaria y recuperación continua | 35 días | ≤ 4 h |
| Identidad | Diaria y recuperación continua | 35 días | ≤ 4 h |
| Trazabilidad sanitaria | Continua | Vida útil + 6 meses, mínimo 5 años | $<$ 2 h |
| Registros de temperatura | Diaria y continua | 5 años | ≤ 8 h |
| Evidencia de entrega | Continua con versionado | 6 años | ≤ 8 h |
| Respaldo de documentos tributarios | Continua con versionado | 6 años | ≤ 8 h |
| Geolocalización de personas | Continua | 12 meses | ≤ 24 h |
| Registros de seguridad y auditoría | Continua | 7 años | ≤ 24 h |

Cada tiempo de restauración corresponde al plazo de resolución que el Artículo 78.2 de las Bases Administrativas (p. 40) asigna al servicio más crítico que usa el dato: la base transaccional en nube se restaura en 4 horas porque sostiene también la identidad, que es crítica, porque Keycloak guarda en Aurora sus datos (sección [4.4.6](#sub:adr-06)). La trazabilidad sanitaria es la única excepción más exigente: se restaura en menos de 2 horas, porque ese es el plazo en que Puelche debe responder un retiro sanitario (Bases Técnicas del caso, Cap. 9, p. 18). Las retenciones cumplen o superan las del caso. La restauración, además, puede ser parcial: la recuperación de Aurora a un instante específico, sobre una instancia temporal, permite restituir un registro, una tabla, un módulo o el sistema completo sin intervenir el ambiente productivo (RT-07.14; Bases Técnicas Transversales, Cap. 7, p. 18).

AWS Backup aplica a Aurora y DynamoDB los respaldos y la recuperación a un instante específico, mientras S3 aporta versionado, Object Lock y réplica entre regiones para los documentos legales; Object Lock protege también los registros de seguridad y auditoría. Los plazos y las retenciones por dominio constan en la Tabla [11](#tab:jd12).

<a id="sub:6-verificacion-de-la-continuidad"></a>
### 4.2.4.6 Verificación de la continuidad

Los mecanismos anteriores se verifican con pruebas periódicas. Antes de cada paso a producción, y al menos una vez por semestre durante la Operación, se inyectan la caída de una instancia, de una zona o de una dependencia externa, la latencia elevada y la saturación de disco (RT-10.07; Bases Técnicas Transversales, Cap. 10, p. 22), y se comprueban las resoluciones de las Tablas [14](#tab:fallas-sitios) y [15](#tab:fallas-nube). La conmutación regional se ensaya dos veces al año con escrituras de pedidos y sincronización en us-east-1, y el RTO y el RPO medidos deben cumplirse en el 100 % de los ensayos (Bases Administrativas, Art. 78.3, p. 40); con la misma frecuencia se ensaya la pérdida completa del sitio de Talca, distinta del corte de enlace, mediante la promoción del WMS de Concepción; los respaldos se restauran mensualmente. Las pruebas se programan fuera de la ventana de despacho y producen un informe de resultados con el plan de corrección de las brechas detectadas (RT-07.07; Bases Técnicas Transversales, Cap. 7, p. 17). El plan de continuidad del negocio se elabora conforme a ISO 22301, y la continuidad TIC se estructura conforme a ISO/IEC 27031, articulada con el plan de recuperación ante desastres de esta sección (RT-10.03 y RT-10.04; Bases Técnicas Transversales, Cap. 10, p. 22).

La aplicación se instrumenta con OpenTelemetry para PHP y Laravel. Además de las métricas de infraestructura, cada perfil publica señales agrupadas por ámbito:

- Aplicación: procesos PHP-FPM ocupados, solicitudes en espera y reinicios de contenedor.
- Colas: profundidad y edad del mensaje más antiguo por cola y por grupo, y mensajes en las colas de fallidos.
- Integraciones: latencia de la capa anticorrupción y del ERP.
- Base de datos: latencia de escritura de VM-02.

El `transaction_id` viaja en las cabeceras HTTP, en las propiedades de los mensajes de RabbitMQ, en los atributos de los mensajes de SQS y en las llamadas a la capa anticorrupción, de modo que una misma traza une la entrega, su evidencia, la guía de despacho y el acuse del ERP. Estas señales disparan el escalado y las alarmas declaradas en el dimensionamiento.

La disponibilidad efectiva de cada servicio, las métricas del proceso de despliegue y el resultado de estas pruebas se miden sobre la plataforma de observabilidad y se entregan en el informe mensual de nivel de servicio (Bases Administrativas, Art. 79, p. 40). Es ahí donde el CLIENTE puede comprobar que lo que declara esta sección se cumple.


<a id="sec:conexiones"></a>
## 4.2.5 Conexiones, puntos de falla y contingencia

Esta sección describe cómo se conectan los sitios, el terreno y la nube, identifica cada punto donde esa conexión o su infraestructura puede fallar, y declara cómo se resuelve cada falla o, cuando no se resuelve de forma automática, cuál es la contingencia. Su punto de partida es el caso: la conectividad actual de Puelche se corta con frecuencia y en algunos lugares no existe, por lo que la solución no puede suponer un enlace disponible y debe decir, para cada conexión, qué pasa cuando no lo está.

### 4.2.5.1 Conexiones entre sitios, terreno y nube

Los dos dominios fijos, la nube y el on-premise, se conectan por túneles VPN IPsec que terminan en el par de firewalls de cada sitio (D-01) y en el Transit Gateway de AWS en sa-east-1, con enrutamiento dinámico BGP. El mismo Transit Gateway enruta entre los sitios, de modo que Concepción y los cross-docking alcanzan Talca sin exponerla a Internet. Los caminos de acceso se distribuyen así:

- Cada centro de distribución tiene dos caminos físicamente independientes: fibra y LTE.
- Cada cross-docking tiene dos caminos físicamente independientes: Starlink y LTE de dos proveedores.

Los terminales EC55 y TC58e acceden por red celular a CloudFront, cuyas rutas `/v1` y `/sync/v1` llegan a la API REST pública.

La Figura [10](#fig:conexiones) muestra estas conexiones.

<a id="fig:conexiones"></a>
**Figura 10.** Conexiones entre los sitios, el terreno y la nube

> Figura compuesta en TikZ en el LaTeX; ver main.pdf, página 57.

- Usuarios externos: clientes, transportistas y proveedores
- AWS sa-east-1
- Transit Gateway
- VPC Endpoints
- API REST pública
- CloudFront y WAF
- AWS us-east-1<br>recuperación<br>y réplica
- CD Talca<br> D-01 en par
- CD Concepción<br> D-01 de borde
- Cross-docking<br> E-01, tres sitios
- Terreno<br> C-01 y C-02
- Camiones<br> B-03

La figura distingue las entradas públicas, los túneles de sitio y las sincronizaciones locales en cuatro flujos:

- Sitios–Talca: Concepción y los cross-docking sincronizan con Talca por la VPN.
- Termógrafo–terminal: los termógrafos descargan por Bluetooth al terminal del conductor.
- Nube–VM: AWS DMS accede a VM-02 y `erp-sync` a VM-04 únicamente por el túnel IPsec autenticado.
- Cross-docking–SQS: los eventos críticos llegan a SQS FIFO sin depender de Talca.

Los 184 usuarios de administración, comercial y soporte de Talca y Concepción acceden a las consolas y a la administración de Keycloak solo por Verified Access. La consola Angular corre en Fargate tras un ALB privado y reenvía las llamadas a la API REST privada por el endpoint de interfaz execute-api. CloudFront publica únicamente los endpoints OIDC necesarios para autenticación y renovación de sesión por la API REST pública sin autorizador hacia Keycloak tras el ALB privado; el verificador local de relevos permanece en cada sitio. Las cadenas usan el canal AS2 descrito en la sección [4.4.11](#sub:adr-11).

La Tabla [12](#tab:conexiones) resume cada conexión con su medio, su camino alternativo y el tiempo de conmutación entre ambos.

<a id="tab:conexiones"></a>
**Tabla 12.** Conexiones de la solución y su camino alternativo
| Conexión | Medio y protocolo | Camino alternativo | Conmutación |
| --- | --- | --- | --- |
| CD Talca con la nube | Fibra D-03, túneles IPsec con BGP | LTE D-04 | Menos de 30 s |
| CD Concepción con la nube | Fibra D-03, túneles IPsec con BGP | LTE D-04 | Menos de 30 s |
| Cross-docking con la nube | Starlink D-06, túneles IPsec con BGP | LTE D-04 de dos proveedores | Menos de 30 s |
| Concepción con Talca | TCP 8080 y 5432 con TLS sobre la VPN | Operación autónoma | No aplica |
| Cross-docking con Talca | AMQPS 5671 entre brokers, por la VPN | Envío diferido | No aplica |
| Terreno con la nube | Red celular, CloudFront, API REST pública | Almacén local del dispositivo | No aplica |
| Termógrafos con el terminal del conductor | BLE con el terminal del conductor, en ruta y al regresar | Registro interno del termógrafo | No aplica |
| Usuarios externos con los portales | Internet, HTTPS por CloudFront | Ninguno: el autoservicio requiere conexión | No aplica |
| Oficinas y trabajo remoto con las consolas | Internet, HTTPS por Verified Access | Otra conexión a Internet | No aplica |
| Cadenas con el canal AS2 | Internet, TLS 1.3 al Network Load Balancer | Reenvío AS2 hasta el acuse MDN | No aplica |
| Región primaria con la secundaria | Replicación nativa de Aurora, DynamoDB y S3 | Respaldo inmutable | Promoción autorizada |

Los cinco sitios tienen un camino alternativo hacia la nube. Concepción también opera sin los sistemas de Talca, el terreno sin señal y los termógrafos con registro interno. El autoservicio de los portales requiere conexión.

<a id="sub:superficie"></a>
### 4.2.5.2 Superficie de exposición

La Tabla [13](#tab:superficie) delimita las únicas entradas desde redes externas. Cada entrada usa un subdominio propio del dominio del CLIENTE gestionado en Route 53.

<a id="tab:superficie"></a>
**Tabla 13.** Superficie de exposición
| Entrada | Servicio y puerto | Quién accede | Control |
| --- | --- | --- | --- |
| Portales y API | CloudFront, HTTPS 443 | Clientes, transportistas, proveedores y terminales de terreno | WAF, protección contra bots, Shield Advanced y autorizador |
| Identidad | OIDC de Keycloak por CloudFront, HTTPS 443 | Personas usuarias | WAF y límites de tasa |
| Consolas | Verified Access, HTTPS 443 | Oficina y trabajo remoto | Identidad, MFA y postura |
| Canal AS2 | Network Load Balancer, TCP 443 con TLS 1.3 | Cadenas registradas | Lista de IP, certificados, firma y MDN |
| Túneles de sitio | VPN del Transit Gateway, IPsec UDP 500 y 4500 | Firewalls D-01 de los cinco sitios | Autenticación IKE y cifrado IPsec |

La tabla excluye toda otra entrada desde fuera de la red del CLIENTE. En recuperación ante desastres se activan las mismas entradas en us-east-1. MDM, EDR, SII, Transbank, GIS, notificaciones y telemetría de flota son dependencias de salida, detalladas en el Formulario T-11.

### 4.2.5.3 Puntos de falla en los sitios y en los enlaces

Cada conexión se apoya en equipos del sitio que también pueden fallar. La Tabla [14](#tab:fallas-sitios) recorre esos puntos de falla, desde el enlace hasta la energía del recinto, e indica para cada uno el mecanismo que la resuelve y la contingencia si ese mecanismo no basta.

<a id="tab:fallas-sitios"></a>
**Tabla 14.** Puntos de falla en los sitios y en los enlaces
| Punto de falla | Resolución | Contingencia |
| --- | --- | --- |
| Fibra de un centro de distribución | BGP conmuta los túneles al LTE en menos de 30 s. | Si cae también el LTE, operación local 24 h. |
| Caída del enlace de Talca para la oficina | Verified Access admite otra conexión a Internet con los mismos controles. | Plan de rutas y manifiesto aprobados en el WMS antes de las 22:00; tableros y costo de servir esperan el retorno. |
| Starlink de un cross-docking | El LTE de dos proveedores toma el tráfico en menos de 30 s. | La ventana de 3 h opera 100 % local y sincroniza al reconectar. |
| Enlace de Los Ángeles en la madrugada | Starlink queda como camino único, porque la red móvil falla a esa hora. | La ventana de madrugada opera íntegramente local. |
| Firewall de Talca | La unidad pasiva asume las direcciones y los túneles en menos de 30 s. | Operación local 24 h sin enlace. |
| Firewall de Concepción | La unidad pasiva asume el túnel y la conmutación de enlace en menos de 30 s. | La unidad dañada se reemplaza con la de reserva de Talca. |
| Nodo del clúster de Talca | Las VM se reinician en los nodos restantes, con sus datos replicados por Ceph. | Ante un segundo nodo, el DRP local promueve el WMS de Concepción en 1 a 2 h. |
| Instancia de escritura VM-02 | Se reinicia en otro nodo del clúster. | D-05 restaura la base en hasta 4 h sin enlace. |
| Disco de un nodo de Talca | El RAID 10 reconstruye sobre el repuesto en caliente. | Ceph conserva una segunda copia en otro nodo. |
| Miembro del stack de switches de Talca o de Concepción | El otro miembro mantiene el tráfico. | Reposición sin corte con la unidad de reserva de Talca. |
| Servidor de borde de Concepción | El RAID 10 tolera la falla de un disco; el equipo tiene fuente única y, ante su falla, se repone. | La pila se reinstala con la misma imagen y la base local se reconstruye desde el estado central, que ya recibió los eventos del sitio por las colas. |
| Mini-PC de un cross-docking | Equipo único; se repone con la unidad de reserva, que viaja desde Talca en el camión de línea nocturno. | El nuevo equipo se resincroniza desde Talca y SQS FIFO. |
| Firewall de un cross-docking | La unidad pasiva del par asume el túnel en menos de 30 s. | La ventana de 3 h opera 100 % local y sincroniza al reconectar. |
| Periféricos de andén | Sin redundancia por equipo. | La etiqueta se emite en otra de las impresoras del centro de distribución. |
| Energía de la sala de Talca | UPS N+1 de 30 min y generador que toma carga en 8 a 15 s. | Estanque de 24 h y contrato de reabastecimiento. |
| Climatización de la sala de Talca | Segunda unidad de precisión en N+1. | Alerta del monitoreo de los sensores ambientales. |

La tabla muestra que los firewalls van en par en los cinco sitios, porque RT-08.03 (Bases Técnicas Transversales, Cap. 8, p. 18) no admite cortafuegos en punto único de falla, y que los puntos únicos de falla que permanecen son el servidor de Concepción y el mini-PC y el switch de cada cross-docking, donde la redundancia no compensa su costo: la pérdida de sus enlaces se cubre con la autonomía local, y la falla de sus propios equipos, con la reposición y la resincronización indicadas en la tabla. Por el mismo fundamento, ese servidor, el mini-PC y el switch de los cross-docking operan con fuente única, excepción declarada a la exigencia de fuente redundante. La liberación sanitaria y el despacho no dependen de la nube. En la ventana de Talca, VM-02 se reinicia en otro nodo y otra impresora emite la etiqueta si falla la del andén. Los mecanismos de alta disponibilidad se detallan en la sección [4.2.4.3](#sub:3-alta-disponibilidad).

### 4.2.5.4 Puntos de falla en la nube, el terreno y las integraciones

La Tabla [15](#tab:fallas-nube) completa el recorrido con los puntos de falla que están fuera de los sitios: la nube, el terreno y los sistemas de terceros.

<a id="tab:fallas-nube"></a>
**Tabla 15.** Puntos de falla en la nube, el terreno y las integraciones
| Punto de falla | Resolución | Contingencia |
| --- | --- | --- |
| Zona de disponibilidad de sa-east-1 | Aurora conmuta en menos de 30 s, ElastiCache en menos de 60 s y Fargate reprograma las tareas. | La operación continúa en las zonas restantes. |
| Región sa-east-1 completa | Route 53 redirige el tráfico y, con autorización del CLIENTE, se promueve la réplica en us-east-1. | RTO de 4 h y RPO de 15 min; la bodega y el terreno operan en local, y los terminales de bodega trabajan contra la puerta de API local del WMS. |
| Túnel VPN de Talca durante la replicación | VM-02 retiene los cambios en su registro de escritura mientras DMS no puede leerlos. | DMS reanuda la réplica al reconectar; la copia en Aurora queda desactualizada durante el corte. |
| IdP maestro o enlace de identidad | La caché de solo lectura, de 24 h, conserva los datos de identidad recibidos, y el verificador local habilita los relevos de turno con el manifiesto firmado y el PIN personal. | La credencial de turno dura hasta 8 h en bodega y 14 h en terreno; no hay revocación remota mientras dure el corte; cuenta de último recurso (sección [4.4.15](#sub:adr-15)). |
| Señal móvil en ruta | La aplicación opera contra el almacén local del dispositivo. | Sincroniza al reconectar dentro de los 10 min de la Tabla [4](#tab:t29). |
| ERP legado | El trabajador `erp-sync` retiene las operaciones en su cola SQS hasta 24 h y reintenta con la misma clave idempotente, de modo que un reintento no emite otro documento. | El camión no se libera sin guía confirmada o contingencia tributaria aprobada por el CLIENTE. |
| Perfil de API saturado | El balanceador reparte entre tareas y el escalado agrega tareas cuando los procesos PHP-FPM ocupados superan el 70 %. | Limitación de tasa en API Gateway con mensaje explícito al usuario. |
| Mensaje de reconciliación inválido o que falla | El consumidor rechaza el sobre de versión desconocida sin aplicarlo; tras cinco intentos pasa a la cola de mensajes fallidos. | Alarma inmediata y reproceso manual trazable; el grupo afectado no bloquea a los demás. |
| Excursión térmica sin enlace | El gateway bloquea el despacho en menos de 5 s en el borde. | Buffer de 24 h y alerta al reconectar. |
| SII, cadenas o notificaciones | Reintento con espera creciente y cola de mensajes fallidos. | Reproceso desde la cola al recuperarse el tercero. |
| Carga del peak de septiembre | Escalado automático e independiente de los perfiles de API y de trabajadores en Fargate, y de Aurora. | Limitación de tasa en API Gateway. |

Ninguna de estas fallas detiene la bodega ni el terreno. La peor de ellas, la pérdida de toda la región primaria, deja sin servicio a los portales y a la analítica hasta la promoción de la réplica, pero la preparación, el despacho y la entrega siguen operando contra sus bases locales y sus dispositivos, porque ninguna de esas transacciones depende de la nube para confirmarse.


<a id="sec:dimensionamiento"></a>
## 4.2.6 Dimensionamiento y plan de capacidad

El dimensionamiento traduce la volumetría del Caso 02 en capacidad para la operación normal, la ventana protegida de despacho y el peak de septiembre. Las citas nombran las Bases Técnicas del caso y las Bases Técnicas Transversales con su capítulo y página. La cadena es: hechos y requisitos, supuestos mínimos, dieciséis dimensiones del numeral 14.2 de las Bases Técnicas del caso (p. 25), capacidad por lugar de proceso y equipamiento. El Anexo 4.B conserva las sustituciones, el perfil horario, las sensibilidades y los umbrales; esta sección presenta la decisión de arquitectura y su consecuencia operativa.

<a id="sec:dimensionamiento-metodo"></a>
### 4.2.6.1 Método, fuentes y supuestos

Un hecho del caso se cita y no se registra como supuesto. Un requisito proviene de las Bases o del Capítulo 15. Un parámetro de diseño es una decisión que imponemos a la solución. Un supuesto completa una cifra que el caso calla y declara fundamento, impacto y validación. Un cálculo se deriva de las entradas anteriores. Los parámetros de plataforma son 50 ms de CPU por solicitud, 64 MB de memoria por proceso y 150 ms de permanencia del proceso en Fargate; son parámetros de diseño que se perfilan y se verifican en las pruebas de RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21). Los tiempos se evalúan en percentil 95 conforme a las Bases Técnicas Transversales, Cap. 9, p. 21.

La Figura [11](#fig:dimensionamiento-cadena) resume esta cadena. El resultado de cada etapa alimenta la siguiente: la volumetría determina las tasas, las tasas determinan capacidad y la capacidad determina los equipos.

<a id="fig:dimensionamiento-cadena"></a>
**Figura 11.** Cadena de cálculo del dimensionamiento.

> Figura compuesta en TikZ en el LaTeX; ver main.pdf, página 64.

- Volumetría<br>del caso
- Supuestos<br>mínimos
- 16 dimensiones<br>del numeral 14.2
- Capacidad por<br>lugar de proceso
- Equipos,<br>enlaces y nube

La cadena evita mezclar decisiones de diseño con hechos del CLIENTE. En particular, el factor SV-04 se aplica sólo a la hora cargada de cada ventana y no se usa para sumar procesos que ocurren en horas diferentes.

<a id="sec:dimensionamiento-regimenes"></a>
### 4.2.6.2 Perfil de carga y regímenes de diseño

El Bases Técnicas del caso, Anexo B, p. 38 distribuye la operación en estas ventanas:

- Preparación de 22:00 a 06:00.
- Cross-docking de 03:00 a 05:00.
- Despacho de 05:30 a 07:00.
- Reparto de 07:00 a 19:00.
- Recepción de proveedores de 08:00 a 18:00.
- Preventa de 09:00 a 18:00.
- Sincronización de 17:00 a 20:00.

El perfil de 24 horas de la Figura [12](#fig:dimensionamiento-perfil) muestra las tasas totales calculadas para esas superposiciones.

<a id="fig:dimensionamiento-perfil"></a>
**Figura 12.** Tasas totales por hora en régimen normal y en septiembre.

> Figura compuesta en TikZ en el LaTeX; ver main.pdf, página 65.

- TPS
- máximo a las 12:00: 12,30 y 14,66 TPS
- día normal
- peak de septiembre
- Etiquetas del eje vertical: 0, 5, 10, 15; eje vertical: TPS; etiquetas del eje horizontal: 00:00, 03:00, 06:00, 09:00, 12:00, 15:00, 18:00, 21:00, 24:00; máximo a las 12:00: 12,30 y 14,66 TPS; leyenda: día normal, peak de septiembre; ventanas: Preparación, Despacho, Preventa, Sincronización.

La hora más exigente es 12:00, con 12,30 TPS normales y 14,66 TPS en septiembre. Esa hora es una convención del cálculo: el factor SV-04 concentra la preventa y el portal en la hora central de su ventana, y el máximo sería el mismo en cualquier otra hora de esa ventana. En esa hora el portal aporta 9,63 TPS y la nube 2,67 TPS normales o 5,03 TPS en peak; Talca, Concepción y cada cross-docking están fuera de sus ventanas de mayor carga. El promedio diario engaña porque oculta la coincidencia de preventa, reparto y sesiones del portal.

La Tabla [16](#tab:dimensionamiento-calendario) resume los factores de calendario que se usan en la memoria.

<a id="tab:dimensionamiento-calendario"></a>
**Tabla 16.** Calendario y factores de diseño
| Dato | Valor | Uso | Fuente |
| --- | --- | --- | --- |
| Días equivalentes de despacho | 22,14 días | 31.000 ÷ 1.400; control 2.100 ÷ 96 = 21,88 | Bases Técnicas del caso, Cap. 14, p. 24 y Tabla 2.3; SV-01 |
| Factor de septiembre | 1,857 | 2.600 ÷ 1.400 | Bases Técnicas del caso, Cap. 14, p. 24; SV-02 |
| Período peak | 1 al 25 de septiembre | Define el régimen peak | Bases Técnicas del caso, Anexo B, p. 38 |
| Totales anuales | 12 × volumen mensual | Evita inventar días hábiles | Bases Técnicas del caso, Cap. 14, p. 24 |

Los 22,14 días son una equivalencia de cálculo, no una cantidad de días hábiles. El peak se obtiene por el cociente entre entregas de septiembre y entregas normales; diciembre no agrega un factor porque el caso identifica septiembre como la mayor exigencia.

<a id="sec:dimensionamiento-tps"></a>
### 4.2.6.3 Transacciones por segundo: dimensiones 1–3

La dimensión 1, «Transacciones por segundo en régimen normal», toma el máximo horario normal. La dimensión 2, «Transacciones por segundo en el peak de la ventana de despacho de 05:30 a 07:00», incluye la cota de emisión de guías. La dimensión 3, «Transacciones por segundo en el peak de septiembre», toma el máximo horario del perfil de septiembre.

La Tabla [17](#tab:t76) presenta los lugares de proceso y separa el portal de la nube. El despacho se muestra como una cota independiente porque el caso lo identifica como peak actual de emisión de documentos.

<a id="tab:t76"></a>
**Tabla 17.** Transacciones por segundo por lugar de proceso
| Lugar o flujo | Régimen normal | Ventana de despacho | Peak septiembre | Derivación |
| --- | --- | --- | --- | --- |
| WMS de Talca | 1,64 TPS | 1,11 TPS | 3,02 TPS | preparación y despacho según perfil horario |
| WMS de Concepción | 0,54 TPS | – | 1,01 TPS | 2/3 y 1/3 de las líneas; SV-03 |
| Cada cross-docking | 1,56 TPS | – | 2,89 TPS | 4 operaciones por entrega |
| Nube, sin portal | 2,67 TPS | 0,68 TPS | 5,03 TPS | preventa, reparto, recepción, trazabilidad, guías y sincronización |
| Portal | 9,63 TPS | – | 9,63 TPS | 2.600 ÷ 9 × 2 por SV-04 × 60 ÷ 3.600 |
| Total | 12,30 TPS | 1,68 / 3,05 TPS | 14,66 TPS | máximo horario; despacho con guías |

El flujo de preparación visible es 11.742 líneas por noche × 2 operaciones × 2/3 ÷ 28.800 segundos = 0,54 TPS de media de ventana para Talca. Al aplicar SV-04 sólo a la hora cargada, llega a 1,09 TPS; a las 05:00 se suma el despacho y el WMS de Talca alcanza 1,64 TPS normal. En septiembre llega a 3,02 TPS al incluir el factor de volumen. Las 2.600 sesiones habituales del portal pertenecen a food service y cadenas (Bases Técnicas del caso, Cap. 2, p. 4) y no son las 2.600 visitas diarias de preventa (Bases Técnicas del caso, Anexo B, p. 38); la coincidencia numérica no implica que sean el mismo flujo. La prueba RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21) es 1,5 × 14,66 = 21,99 TPS y no recibe un segundo multiplicador.

<a id="sec:dimensionamiento-usuarios"></a>
### 4.2.6.4 Personas usuarias, concurrencia y dispositivos: dimensiones 4–6

La dimensión 4, «Personas usuarias registradas, internas y externas», es 15.180 registros: 640 + 160 + 14.200 + 180. La dimensión 5, «Personas usuarias concurrentes en peak», toma el máximo de cada ventana sin sumar turnos que no coinciden. La Tabla [18](#tab:dimensionamiento-concurrencia) muestra la operación sin portal y la cota de sesiones.

<a id="tab:dimensionamiento-concurrencia"></a>
**Tabla 18.** Concurrencia por ventana
| Ventana | Operación sin portal | Portal | Máximo |
| --- | --- | --- | --- |
| Noche: preparación y cross-docking | 120 + 60 + 6 = 186 | – | 186 |
| Despacho | 96 equipos de reparto | – | 96 |
| Día | 62 + 96 + 184 = 342 | 96,30 en régimen | 438,30 |
| Sincronización | 62 + 96 = 158 | – | 158 |
| Cota extrema del portal | 342 | 433,33 | 775,33 |

La operación sin portal, que carga la Wi-Fi y los sitios, llega a 342 personas o equipos concurrentes durante el día. Los seis del cross-docking son personas con terminal inalámbrico, dos por plataforma (S-35). Los 96 equipos de reparto equivalen a 96 conductores en ruta; la dimensión 5 se expresa en personas o sesiones y no en camiones. La cota extrema del portal se conserva como prueba separada. La dimensión 6, «Dispositivos de terreno en operación simultánea», es 62 preventistas + 96 equipos de reparto = 158.

La cantidad a proveer se informa aparte, por ámbito:

- Bodega: 132 terminales en Talca, 22 de ellos para congelado, y 66 en Concepción.
- Terreno: 69 terminales de preventa, 106 terminales de reparto, 106 impresoras de cabina y 106 terminales de pago.
- Cross-docking y frío: 7 terminales de cross-docking y 31 termógrafos.

Cada cantidad incluye la reserva del 10 % del parque, redondeada hacia arriba, conforme a la tabla de repuestos de las Bases Técnicas Transversales (Cap. 8, p. 19). Solo los 22 terminales de la cuadrilla de congelado de Talca son aptos para {-}22 °C: el congelado representa cerca del 4 % de las líneas y se prepara al final del turno, de modo que la cuadrilla que entra a la cámara es de unas 20 personas (S-34). Concepción no tiene congelado.

<a id="sec:dimensionamiento-almacenamiento"></a>
### 4.2.6.5 Almacenamiento, retención y migración: dimensiones 7–10

La dimensión 7, «Volumen anual de almacenamiento transaccional», la dimensión 8, «Volumen anual de almacenamiento de evidencia de entrega, firmas y fotografías», la dimensión 9, «Volumen anual de almacenamiento de series de temperatura y de posicionamiento», y la dimensión 10, «Volumen total de datos históricos a migrar», se resumen en la Tabla [19](#tab:dimensionamiento-almacenamiento).

<a id="tab:dimensionamiento-almacenamiento"></a>
**Tabla 19.** Volumen, retención y destino de los datos
| Dominio | Volumen anual | Retención | Acumulado | Destino |
| --- | --- | --- | --- | --- |
| Datos transaccionales | 50,75 GB/año | 6 años como cota | 304,49 GB | Base local de 4 meses y nube |
| Evidencia de entrega | 87,72 GB/año | 6 años | 526,32 GB | S3 por niveles |
| Temperatura | 0,56 GB/año crudos | 5 años | 2,80 GB crudos | IoT y almacenamiento histórico |
| Posición | 3,20 GB/año crudos | 12 meses | 3,20 GB crudos | Telemetría y almacenamiento histórico |
| Migración histórica | 32,11 GB | Maestros; 36/24/60/24 meses | 30,73–33,49 GB de sensibilidad | Nube después del perfilado |

La migración no supone eventos históricos digitales de trazabilidad: el caso dice que no existe forma consultable y que el lote se anota en texto libre cuando se anota. Por eso la estimación usa 1.150 recepciones mensuales × 60 meses × 20 líneas por recepción, con sensibilidad de 10 a 30 líneas. El 41 % sin lote del retiro de marzo se usa sólo para saneamiento de calidad, conforme a Bases Técnicas del caso, Cap. 7, p. 12.

<a id="sec:dimensionamiento-enlaces"></a>
### 4.2.6.6 Integraciones y ancho de banda por sitio: dimensiones 11–12

La dimensión 11, «Número de integraciones y volumen de mensajes por integración», cuenta únicamente INT-01 a INT-15 del catálogo del apartado 4.1. Portal y llamadas internas a la API quedan fuera. La Tabla [20](#tab:dimensionamiento-integraciones) resume sus 175.661 mensajes diarios normales y 257.155 en peak.

<a id="tab:dimensionamiento-integraciones"></a>
**Tabla 20.** Mensajes de integración por grupo
| Integraciones | Normal | Peak | Origen |
| --- | --- | --- | --- |
| INT-01 a INT-04 | 72.710/día | 135.032/día | Pedidos, entregas, eventos y cota de cross-docking |
| INT-05 | 10.584/día | 10.584/día | 6.048 cámaras + 4.536 termógrafos |
| INT-06 a INT-10 | 5.725/día | 11.695/día | ERP, DTE, EDI, pagos y mapas |
| INT-11 a INT-15 | 86.642/día | 99.844/día | Avisos, réplica, identidad, ADOT y telemetría |
| **Total** | **175.661/día** | **257.155/día** | **15 integraciones** |

El EDI actual es cero y el escenario 2029 se limita a 11 % de los pedidos de la cadena principal, que pesa 11 % de la venta (SV-05). La Tabla [21](#tab:t81) compara la hora cargada, el drenaje y el peor caso con el enlace principal y el respaldo de cada sitio.

<a id="tab:t81"></a>
**Tabla 21.** Ancho de banda por sitio
| Sitio | Régimen cargado | Drenaje 24 h/2 h | Peor caso | Utilización principal / respaldo LTE (drenaje prioritario) |
| --- | --- | --- | --- | --- |
| Talca, D-03 / D-04 | 3,71 Mbps | 1,59 Mbps | 5,30 Mbps | 26,51 % / 31,88 % |
| Concepción, D-03 / D-04 | 0,11 Mbps | 0,66 Mbps | 0,77 Mbps | 7,68 % / 21,93 % |
| Cada cross-docking, D-06 / D-04 | 0,05 Mbps | 0,30 Mbps | 0,35 Mbps | 17,41 % / 14,92 % |

En esta comparación, D-03 es el enlace de fibra, D-04 el enlace LTE y D-06 el enlace satelital. El drenaje no incluye oficina: durante un corte no se encola ese tráfico. Sí incluye cambios con WAL, broker, telemetría, observabilidad e incremental de respaldo. Durante la recuperación por D-04, la sincronización tiene prioridad sobre la oficina conforme a RT-03.24 (Bases Técnicas Transversales, Cap. 3, p. 10). Talca agrega 1,40 Mbps en la hora punta de retorno de 64 camiones; el agregado de la ventana 17:00–20:00 es 0,70 Mbps. El respaldo completo semanal y la App de reparto caben en la ventana dominical; el sistema operativo se distribuye en tandas de 16 equipos en Talca, 10 en Concepción y 2 en cada cross-docking.

<a id="sec:dimensionamiento-terreno"></a>
### 4.2.6.7 Terreno: turno sin señal y sincronización de la flota: dimensiones 13–14

La dimensión 13, «Volumen de datos generado por un dispositivo de reparto en un turno completo sin señal», es 9,83 MB para la ruta de 34 clientes; una ruta promedio genera 5,36 MB normales y 8,24 MB en septiembre. La cifra incluye evidencia, una fotografía adicional cuando corresponde y 2 MB de datos locales.

La dimensión 14, «Tiempo de sincronización de la flota al regresar al centro de distribución», se expresa en tiempo: cada dispositivo sincroniza en diez minutos con al menos 0,13 Mbps efectivos. Los 64 camiones de la hora punta requieren 1,40 Mbps en la Wi-Fi y el enlace de Talca; la flota termina unos diez minutos después de la llegada del último camión. La cota de 34 clientes corresponde a la ruta rural más larga descrita en el caso (Bases Técnicas del caso, Cap. 8, p. 16, entrevista al conductor de la ruta Cauquenes); en el centro de distribución la sincronización ocurre por Wi-Fi.

<a id="sec:dimensionamiento-onpremise"></a>
### 4.2.6.8 Capacidad on-premise

La capacidad propuesta conserva maestros, stock, lotes presentes y movimientos de cuatro meses en cada sitio; el histórico vive en la nube. El horizonte cubre el ciclo de conteo de 11.400 ÷ 3.400 = 3,35 meses y la rotación media de 11,4 veces/año. Cada VM se calcula como base de sistema más carga; se agregan un 15 % de CPU y 2 GB de RAM por nodo para el hipervisor.

<a id="tab:t79"></a>
**Tabla 22.** Capacidad requerida por sitio
| Sitio | Base local | Requerido actual | Requerido a 3× |
| --- | --- | --- | --- |
| Talca, VM-01 a VM-06 | 5,04 GB; 7,78 GB RAM de trabajo | 17 vCPU; 24 GB RAM; 210 GB | 17 vCPU; 26 GB RAM; 221 GB |
| Concepción, VM-C01 a VM-C04 | 2,59 GB; 5,94 GB RAM de trabajo | 10 vCPU; 15 GB RAM; 140 GB | 10 vCPU; 16 GB RAM; 140 GB |
| Cada cross-docking, mini-PC | 0,63 GB; 4,47 GB RAM de trabajo | 3 vCPU; 5 GB RAM; 50 GB | 3 vCPU; 5 GB RAM; 50 GB |
| Configuración mínima por nodo | – | – | 9 vCPU; 13 GB RAM; 221 GB lógicos |

La configuración mínima N+1, con dos nodos sobrevivientes y réplica de almacenamiento, aplica sólo al clúster de Talca. Concepción y cada cross-docking se dimensionan con un nodo por sitio, como fija el apartado 4.2.2. En Talca el mínimo lo fija la redundancia, no la carga: la configuración cubre 3×, es decir, un margen de crecimiento de +200 % sobre la carga actual.

<a id="sec:dimensionamiento-nube"></a>
### 4.2.6.9 Capacidad en nube

La plataforma utiliza Fargate, Aurora, ElastiCache, SQS, IoT Core, DynamoDB y S3 como servicios administrados. Una tarea entrega 14 solicitudes por segundo al 70 % de uso con 50 ms de CPU. La Tabla [23](#tab:dimensionamiento-nube) separa el portal y compara cada perfil con el techo de ocho tareas.

<a id="tab:dimensionamiento-nube"></a>
**Tabla 23.** Procesos Fargate por perfil
| Perfil | Carga | Tareas | Techo | Conclusión |
| --- | --- | --- | --- | --- |
| Régimen normal | 12,30 solicitudes/s (nube + portal) | 2 | 8 | Cumple |
| Peak de septiembre | 14,66 solicitudes/s (nube + portal) | 2 | 8 | Cumple |
| Prueba RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21) | 21,99 solicitudes/s totales, distribuido por perfil horario | 2 | 8 | Una sola multiplicación |
| Cota extrema | 48,37 solicitudes/s (5,03 + 43,33) | 4 | 8 | Bajo el techo |
| Sensibilidad 120 solicitudes | 21,93 / 91,70 solicitudes/s; régimen / cota | 2 / 7 | 8 | Bajo el techo |

El portal en régimen usa 9,63 solicitudes/s y 96,30 sesiones concurrentes; su cota extrema usa 43,33 solicitudes/s y 433,33 sesiones concurrentes. Con 120 solicitudes por sesión, manteniendo las sesiones repartidas en la hora, el portal alcanza 19,27 solicitudes/s en régimen y 86,67 en la cota extrema; al sumar la nube resultan 21,93 y 91,70 solicitudes/s, que requieren 2 y 7 tareas. El parámetro se mantiene bajo el techo de ocho, pero se perfila en la prueba de carga.

<a id="sec:dimensionamiento-plan"></a>
### 4.2.6.10 Plan de capacidad

La Tabla [24](#tab:dimensionamiento-plan) mantiene separadas la proyección del año 3 y la exigencia técnica de 3×. Cada fila tiene una acción concreta de operación o ampliación.

<a id="tab:dimensionamiento-plan"></a>
**Tabla 24.** Proyección y crecimiento de capacidad
| Componente | Año 1 | Año 3 | 3× | Acción |
| --- | --- | --- | --- | --- |
| WMS de Talca, TPS peak | 3,02 | 3,02 × (305.000 ÷ 260.000) = 3,54 | 9,06 | Revisar CPU e IOPS trimestralmente |
| Nube, TPS peak / tareas | 14,66 / 2 | 14,66 × (36.000 ÷ 31.000) = 17,03 / 2 | 43,98 / 4 | Escalamiento automático y prueba trimestral |
| Evidencia anual | 87,72 GB | 87,72 × (36.000 ÷ 31.000) = 101,87 GB | 263,16 GB | Escalar S3 y revisar retención |
| Enlace de Talca, peor caso | 5,30 Mbps | 5,34 Mbps, con los flujos de volumen × 305.000 ÷ 260.000 | 8,71 Mbps | Ampliar D-03 si el percentil 95 supera la cota |
| Terminales de bodega de Talca | 132 | (23 + 3) de congelado + (113 + 12) estándar = 151 | no aplica | Ajustar parque a la dotación |
| Mesa de ayuda, contactos | 2.000/mes | 2.000 × (350 ÷ 310) = 2.258/mes | 6.000/mes | Recalibrar Erlang C trimestralmente |

La nube escala automáticamente dentro del techo declarado; nodos, almacenamiento local, Wi-Fi y enlaces requieren revisión planificada. La gestión trimestral compara la proyección observada con la cota de 3× y con la incorporación de nuevas unidades.

<a id="sec:dimensionamiento-cuello"></a>
### 4.2.6.11 Cuello de botella, umbrales y degradación controlada

El primer candidato es la emisión de guías del ERP. En el peak se emiten unos 2.852 documentos tributarios electrónicos (DTE) al día. El tiempo disponible por guía depende de la ventana:

- Entre 22:00 y 05:30: máximo de 9,47 segundos por guía.
- En las últimas 3,5 horas: máximo de 4,42 segundos por guía.
- En la ventana actual de despacho: máximo de 1,89 segundos por guía.

La solución emite la guía cuando confirma la carga, durante la noche. Se detectan guías aún no emitidas frente a la hora de salida de cada camión y se prioriza la cola, sin crear un segundo emisor: el ERP conserva la responsabilidad tributaria y la guía acompaña el traslado. Como el caso no documenta las interfaces del ERP y encarga levantarlas en los primeros meses (Bases Técnicas del caso, Cap. 5, p. 10), el tiempo real por guía se mide en ese levantamiento; si superara los 4,42 segundos, las cargas se cierran por camión en el orden de salida, para que la emisión empiece antes.

La Tabla [25](#tab:t84) fija los umbrales de respuesta que se observan en percentil 95.

<a id="tab:t84"></a>
**Tabla 25.** Umbrales de respuesta en percentil 95
| Operación | Umbral | Fuente |
| --- | --- | --- |
| Confirmación de línea de preparación | 1 s | Bases Técnicas del caso, Cap. 15, p. 26 |
| Registro de entrega | 2 s | Bases Técnicas del caso, Cap. 15, p. 26 |
| Línea de preventa | 1,5 s | Bases Técnicas del caso, Cap. 15, p. 26 |
| Consulta de stock y crédito | 2 s | Bases Técnicas del caso, Cap. 15, p. 26 |
| Transacción crítica de terreno | 3 s | Bases Técnicas Transversales, Cap. 9, p. 21 |
| Carga inicial del portal | 2 s | Bases Técnicas Transversales, Cap. 9, p. 21 |
| Navegación | 1 s | Bases Técnicas Transversales, Cap. 9, p. 21 |
| API de consulta | 500 ms | Bases Técnicas Transversales, Cap. 9, p. 21 |
| API de escritura | 800 ms | Bases Técnicas Transversales, Cap. 9, p. 21 |
| Búsqueda compuesta | 3 s | Bases Técnicas Transversales, Cap. 9, p. 21 |
| Informe estándar | 30 s | Bases Técnicas Transversales, Cap. 9, p. 21 |

Los otros candidatos son la base WMS, los IOPS, la Wi-Fi y el drenaje. Se detectan con percentil 95, longitud de colas, errores, retransmisiones y tiempo de sincronización. Si se supera una cota, se encola con clave idempotente, se limita la tasa y se muestra un mensaje explícito; no se pierden ni duplican pedidos.

<a id="sec:dimensionamiento-pruebas"></a>
### 4.2.6.12 Validación mediante pruebas de carga y estrés

La prueba RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21) carga una sola vez 1,5 × la dimensión 3, es decir, 21,99 TPS totales. La Tabla [26](#tab:t86) vincula cada ensayo con la decisión que debe cerrar.

<a id="tab:t86"></a>
**Tabla 26.** Pruebas que confirman el dimensionamiento
| Prueba | Carga | Qué confirma | Criterio |
| --- | --- | --- | --- |
| Carga RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21) | 21,99 TPS totales, distribuidos por lugar según el perfil horario | CPU, Fargate, portal, WMS, base e IOPS | Percentil 95 |
| Estrés RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21) | Sobre cota extrema portal y 3× | Umbral de quiebre y degradación | Sin pérdida ni duplicación |
| Corte de enlace | 24 h y drenaje en 2 h | WAL, broker, telemetría y observabilidad | Drenaje completo |
| Sincronización de dispositivo | Peor ruta en 10 min | 0,13 Mbps efectivos | Ruta reconciliada |
| Migración | Dos ensayos independientes | Volumen y calidad histórica | Conciliación de dominios |
| Ventana dominical | Respaldo y actualizaciones | Tandas por sitio y enlace | Cada tanda cabe |

La prueba de carga conserva tasas por lugar, percentil 95, utilización, colas, errores y comportamiento durante el drenaje; incluye la concurrencia de oficina y trabajo remoto por Verified Access, la API privada, el inicio de sesión y los tableros. Los parámetros confirmados se actualizan en la revisión trimestral de capacidad.

<a id="sec:dimensionamiento-sintesis"></a>
### 4.2.6.13 Síntesis de las dieciséis dimensiones del numeral 14.2

La Tabla [27](#tab:t72) reúne cada dimensión con el nombre literal del Caso 14.2, su valor normal o de ventana, su valor peak o declarado y la derivación correspondiente.

<a id="tab:t72"></a>
**Tabla 27.** Síntesis de las dieciséis dimensiones
| N.° | Dimensión | Valor en régimen normal o ventana | Valor en peak o declarado | Derivación |
| --- | --- | --- | --- | --- |
| 1 | Transacciones por segundo en régimen normal | 12,30 TPS a las 12:00 | – | Anexo 4.B, sección 4.B.2 |
| 2 | Transacciones por segundo en el peak de la ventana de despacho de 05:30 a 07:00 | 1,68 TPS | 3,05 TPS | Anexo 4.B, sección 4.B.2 |
| 3 | Transacciones por segundo en el peak de septiembre | – | 14,66 TPS a las 12:00 | Anexo 4.B, sección 4.B.2 |
| 4 | Personas usuarias registradas, internas y externas | 15.180 | – | Anexo 4.B, sección 4.B.3 |
| 5 | Personas usuarias concurrentes en peak | 438,30 en régimen; 342 sin portal | 775,33, cota extrema | Anexo 4.B, sección 4.B.3 |
| 6 | Dispositivos de terreno en operación simultánea | 158 | 158 | Anexo 4.B, sección 4.B.3 |
| 7 | Volumen anual de almacenamiento transaccional | 50,75 GB/año | 7,85 GB mes peak | Anexo 4.B, sección 4.B.4 |
| 8 | Volumen anual de almacenamiento de evidencia de entrega, firmas y fotografías | 87,72 GB/año | 13,58 GB mes peak | Anexo 4.B, sección 4.B.4 |
| 9 | Volumen anual de almacenamiento de series de temperatura y de posicionamiento | 0,56 + 3,20 GB/año crudos | 2,80 + 3,20 GB crudos retenidos | Anexo 4.B, sección 4.B.4 |
| 10 | Volumen total de datos históricos a migrar | 32,11 GB | 30,73–33,49 GB de sensibilidad | Anexo 4.B, sección 4.B.4 |
| 11 | Número de integraciones y volumen de mensajes por integración | 15; 175.661 mensajes/día | 257.155 mensajes/día | Anexo 4.B, sección 4.B.5 |
| 12 | Ancho de banda requerido por sitio, en régimen y en peak | 3,71 / 0,11 / 0,05 Mbps cargados | 5,30 / 0,77 / 0,35 Mbps peor caso | Anexo 4.B, sección 4.B.5 |
| 13 | Volumen de datos generado por un dispositivo de reparto en un turno completo sin señal | 5,36 MB promedio | 9,83 MB, ruta de 34 clientes | Anexo 4.B, sección 4.B.6 |
| 14 | Tiempo de sincronización de la flota al regresar al centro de distribución | 10 min por dispositivo | 10 min después del último camión | Anexo 4.B, sección 4.B.6 |
| 15 | Contactos mensuales a la mesa de ayuda | 2.000 contactos/mes | 2.000 contactos/mes en el escenario conservador; 7 agentes cubren hasta 2.391 | Anexo 4.B, sección 4.B.7 |
| 16 | Dotación de la mesa de ayuda y del equipo de operación | 7 + 8 = 15 personas a 42 h | 7 + 2 + 8 = 17 personas en peak | Anexo 4.B, sección 4.B.7 |

El diseño queda gobernado por tres condiciones operativas. La primera es la emisión de guías del ERP antes de la salida de cada camión, que es la única de las tres cuya capacidad no controla la solución y que por eso se mide primero. La segunda es el enlace de Talca durante el retorno de la flota, cuando la sincronización de los dispositivos se suma al tráfico de oficina. La tercera es el almacenamiento de la evidencia de entrega, que es el volumen que más crece y el que fija la política de niveles de S3. El resto de las dimensiones queda con holgura amplia frente a la capacidad propuesta, incluso con el crecimiento de 3×.


<a id="cap:4-3-data-center"></a>
# 4.3 Data center

<a id="sec:d-especificaciones-del-sitio-principal-on-"></a>
## 4.3.1 Especificaciones Data Center Primaria

El Data Center Primario concentra la operación productiva de la solución en dos dominios que se exigen mutuamente por el carácter híbrido obligatorio del despliegue: la región primaria de la nube en sa-east-1, ubicada en São Paulo, Brasil, y la sala técnica secundaria on-premise del centro de distribución de Talca, tipología que fija el propio caso. Ambos dominios se especifican bajo el mismo criterio: un centro de datos comprende no solo los servidores, sino también las condiciones que sostienen la operación sin interrupción: energía acondicionada, clima controlado, conectividad, seguridad física y monitoreo permanente con procedimiento escrito.

Esta sección declara, para cada dominio, el proveedor, la región y las zonas de disponibilidad, los servicios contratados y el sitio on-premise. También fija los objetivos de continuidad verificables que los gobiernan: disponibilidad de infraestructura de 99,95 % mensual por componente y, para los servicios críticos, RTO ≤ 4 h y RPO ≤ 15 min. Sobre estos objetivos se sostiene el compromiso contractual penalizable de ≥ 99,9 % mensual de la transacción de negocio de extremo a extremo. El desglose servicio por servicio y componente por componente se entrega en el Formulario T-11.

### 4.3.1.1 Proveedor

Para la nube en Amazon Web Services todos los servicios se contratan en cuentas del CLIENTE, que son organizadas bajo AWS Control Tower con una cuenta por ambiente de modo que la propiedad de los datos y de la infraestructura es del CLIENTE desde el primer día. Los criterios con que se eligieron esos servicios se explican en el apartado [4.2.3](#sec:servicios-nube). AWS satisface el requisito de presencia de región o zona en Chile o en Sudamérica con la región primaria sa-east-1. El cumplimiento de los estándares y marcos de referencia del Artículo 4.3 de las Bases Administrativas (Art. 4.3, p. 5) entre ellos ISO/IEC 27017 (nube) e ISO/IEC 27018 (datos personales en nube) se acredita en la matriz de controles ISO/IEC 27001/27002 de la arquitectura de seguridad (apartado 4.1), y no se repite en esta sección.

En el dominio On-premise del CD de Talca, el caso exige cómputo, almacenamiento y procesamiento en las instalaciones del CLIENTE para sostener recepción, preparación y despacho durante un corte de enlace; ello obliga a la modalidad híbrida. Ese alcance requiere cómputo local para la continuidad de un sitio operacional sin albergar el núcleo. Por ello, el sitio adopta la tipología de **sala técnica secundaria o de sitio** del numeral 6.1 de las Bases Técnicas Transversales (Cap. 6, p. 14), con disponibilidad de infraestructura de 99,95 % y dimensionamiento proporcional al equipamiento real.

### 4.3.1.2 Región y zonas de disponibilidad

La región primaria de la nube es sa-east-1, ubicada en São Paulo, Brasil. Todo componente con requisito de alta disponibilidad se despliega en al menos dos zonas de disponibilidad; no se acepta un diseño en una sola zona. Aurora PostgreSQL tiene el escritor en sa-east-1a y un lector promovible en sa-east-1b. ECS Fargate, ElastiCache Redis, el balanceador de aplicación y el NAT Gateway operan entre esas mismas dos zonas con conmutación automática; DynamoDB opera Multi-AZ de forma nativa y transparente. El único componente con escritor único es la base de datos, que conmuta de forma automática entre las zonas. Este diseño sostiene el compromiso de extremo a extremo de ≥ 99,9 % mensual de la transacción crítica y la conmutación se verifica en las pruebas de resiliencia por inyección de fallas de la arquitectura de despliegue.

### 4.3.1.3 Servicios contratados en la región primaria

Los servicios contratados en la región primaria son los que agrupa por función la Tabla [5](#tab:servicios-nube) del apartado [4.2.3](#sec:servicios-nube). En esta región se concentran la operación productiva, la analítica y los servicios de detección, cumplimiento y gobierno; todos son servicios administrados, de modo que la solución no opera servidores en la nube.

### 4.3.1.4 Sitio on-premise: CD Talca (sala técnica secundaria)

El caso fija para el CD de Talca una sala técnica secundaria “dimensionada para sostener recepción, preparación y despacho durante un corte”, y advierte que la sala actual de 25 m<sup>2</sup> no cumple el Capítulo 6 de las Bases Técnicas Transversales (p. 14). Conforme a la tipología del numeral 6.1 de las Bases Técnicas Transversales (Cap. 6, p. 14), no se aplica íntegramente a este sitio el conjunto de exigencias de una sala técnica principal, sino el subconjunto dimensionado al sitio: energía, climatización, control de acceso, detección de incendio y monitoreo. El numeral 6.1 de las Bases Técnicas Transversales (Cap. 6, p. 14) exige declarar la tipología y justificar el dimensionamiento, y advierte que “sobredimensionar el recinto es tan penalizado como subdimensionarlo: ambos revelan que el cálculo de capacidad no se hizo”. El equipamiento real que la sala debe alojar y los cálculos eléctrico y térmico desarrollados a continuación determinan su superficie proyectada, que se fija en el plano de distribución interna (Figura [15](#fig:recinto-talca)).

La sala aloja el siguiente equipamiento:

- El núcleo del componente on-premise, con el motor WMS y el borde operacional del CD sobre un clúster virtualizado de tres nodos con redundancia N+1, que tolera la pérdida de cualquier nodo manteniendo quórum.
- Una NAS local con el respaldo de recuperación rápida.
- Los dos firewalls de la frontera del sitio.

El listado completo de componentes de sala (UPS, generador, climatización, seguridad física, extinción, cableado y gabinetes) y del equipamiento de cómputo y red que alojan los gabinetes se entrega en el Formulario T-11. La ocupación por rack y el margen de crecimiento se declaran en la Figura [14](#fig:racks-talca).

Para la disponibilidad y la redundancia la disponibilidad de infraestructura comprometida es del 99,95 % mensual por componente en energía del recinto, climatización, red y comunicaciones, servidores y cómputo, y motor de base de datos. Además se sostiene con redundancia N+1 en energía y climatización, con generación autónoma y con monitoreo continuo con alertamiento. No se invoca una clasificación de instalación de terceros (ejemplo un nivel TIER certificado), por lo que los niveles de disponibilidad de infraestructura del numeral 7.2 de las Bases Técnicas Transversales (Cap. 7, p. 17) son un medio, no un fin y el compromiso que se mide y se penaliza es el de la transacción de negocio de extremo a extremo.

La Figura [13](#fig:cd-talca) muestra cómo se conecta el equipamiento de la sala con la bodega, la cadena de frío y el ERP.

<a id="fig:cd-talca"></a>
![](https://raw.githubusercontent.com/PatricioH315/LafroX/95ed2c9a1cc20aa7ad9f3ebbe03cafa0e1e1259c/04/figuras/centros_de_datos/Arquitectura_Fisica_CD_Talca.png)

**Figura 13.** Arquitectura física del sitio on-premise del CD Talca

*Fuente: elaboración propia.*

La fibra es el enlace principal y el LTE lo respalda; ambos llegan al par de firewalls, uno activo y otro pasivo. Detrás, los dos switches de núcleo y el switch de gestión reparten la red hacia el clúster Proxmox VE con Ceph de tres nodos. El clúster aloja seis máquinas virtuales: VM-01 con el núcleo del WMS, VM-02 con PostgreSQL, VM-03 con RabbitMQ, VM-04 con la capa anticorrupción que conversa con el ERP de 2017, VM-05 con la caché de Keycloak y VM-06 con el colector ADOT y el agente de Systems Manager. La línea punteada representa a AWS DMS, que lee los cambios de VM-02 por la VPN para replicarlos en Aurora. En la bodega, los terminales MC9400 y las impresoras de andén trabajan por Wi-Fi 6E contra el WMS; en la cadena de frío, los sensores entregan sus lecturas al gateway IoT, que las publica por MQTTS y bloquea el despacho ante una excursión térmica. El respaldo de recuperación rápida queda en la NAS WORM. La figura muestra que todo lo que la bodega necesita para recibir, preparar y despachar está dentro del sitio, y que la pérdida de un nodo no detiene la operación, porque sus máquinas virtuales se reinician en los otros dos.

La cadena eléctrica sigue esta secuencia: empalme → tablero general → transferencia automática → UPS → PDU del rack → fuente del equipo → servidor.

Esta cadena consta de UPS de doble conversión on-line en configuración N+1 con autonomía mínima de 30 minutos a plena carga y generación autónoma para un rango mínimo de 24 horas continuas, con estanque de combustible dimensionado y contrato de reabastecimiento declarado. La instalación eléctrica es independiente de la del resto del edificio y conforme a la normativa eléctrica chilena vigente, incluida la NCh Elec. 2777; se revisa y mide semestralmente, con informe entregable al CLIENTE.

Para el cálculo de carga eléctrica la carga se proyecta sobre los equipos que el Formulario T-11 declara para el recinto, usando su potencia de placa (suma de las fuentes del equipo, que es el valor con que se dimensiona el UPS), proyectada por equipo en la Tabla 4.3-1:

<a id="tab:4-3-1"></a>
**Tabla 4.3-1.** Carga eléctrica de TI proyectada del recinto
| Equipo | Cantidad | Potencia de placa por unidad | Subtotal |
| --- | --- | --- | --- |
| Nodo de cómputo del clúster (servidor rack 2U, doble procesador) | 3 | 1.600 W (2 fuentes de 800 W) | 4.800 W |
| NAS local | 1 | 400 W | 400 W |
| Firewall del perímetro del sitio | 2 | 150 W | 300 W |
| Conmutador de núcleo (switch core) | 2 | 150 W | 300 W |
| Switch de gestión | 1 | 50 W | 50 W |
| **Carga TI base** |  |  | **5.850 W** |
| Margen de crecimiento a tres años (20 %) |  |  | + 1.170 W |
| **Carga TI de diseño** |  |  | **7.020 W ≈ 7,0 kW** |

El cálculo eléctrico sigue estos pasos:

1. Potencia aparente y UPS: con factor de potencia 0,95, 7,0 kW $$ 0,95 ≈ 7,4 kVA; al 80 % de utilización, 7,4 kVA $$ 0,8 ≈ 9,2 kVA. El UPS seleccionado es modular de 10 kVA, de doble conversión on-line, en configuración N+1 y con bypass de mantenimiento.
2. PUE: la carga TI de 7,0 kW, la climatización de precisión de ≈ 2,3 kW, la iluminación y apoyo de ≈ 0,6 kW y las pérdidas de conversión del UPS de ≈ 0,55 kW suman ≈ 10,4 kW; 10,4 ÷ 7,0 ≈ 1,5. La PUE estimada de diseño es 1,5. El numerador se mide en el tablero general del recinto y el denominador a la salida de las PDU de los racks, semestralmente y con informe entregable. El PUE del recinto on-premise se declara junto con la intensidad de carbono de la región de nube.
3. Generador: la carga del sitio de ≈ 10,4 kW exige un grupo electrógeno de 15 kVA con estanque dimensionado a 24 horas continuas y contrato de reabastecimiento declarado.

La climatización de precisión para la operación continua es redundante en configuración N+1 y controla la temperatura y la humedad relativa dentro de los rangos que recomienda el fabricante del equipamiento.

Para calcular la carga térmica, se considera que cada kW eléctrico consumido por el equipamiento se disipa físicamente como aproximadamente 1 kW de calor sensible (≈ 3.412 BTU/h). Por ello, la carga térmica se dimensiona sobre la carga TI de diseño más las pérdidas de conversión del UPS, como resume la Tabla 4.3-2:

<a id="tab:4-3-2"></a>
**Tabla 4.3-2.** Carga térmica sensible proyectada del recinto
| Origen del calor | Potencia equivalente |
| --- | --- |
| Carga TI de diseño | 7.000 W |
| Pérdidas de conversión del UPS (eficiencia ≈ 0,92) | ≈ 610 W |
| **Carga térmica sensible de diseño** | **≈ 7,6 kW** |

Sobre esa carga se instalan dos unidades de climatización de precisión en configuración N+1, cada una con capacidad de enfriamiento de 10 kW (≈ 34.000 BTU/h) que cuenta con la pérdida de la unidad mayor, ya que la restante cubre la carga de diseño (7,6 kW $<$ 10 kW) con holgura y la temperatura y la humedad relativa se controlan dentro de los rangos del fabricante del equipamiento. No se declaran equipos ni potencias sin el cálculo que los respalde.La consola KVM y el equipo de acceso del operador (ONT de fibra y router LTE) suman en conjunto menos de 0,1 kW y quedan cubiertos por el margen de diseño del 20 % de la Tabla 4.3-1, sin alterar el dimensionamiento del UPS (10 kVA) ni del generador (15 kVA).

La protección contra incendios reúne estos elementos:

- Detección temprana por aspiración de aire con tecnología láser, tipo AnaLASER.
- Extinción automática con agente limpio tipo FM-200 con aprobación UL e instalación conforme a norma NFPA, con botón de aborto.
- Sistema secundario de extintores portátiles habilitados con mantención y certificación vigentes.

El sistema de detección y extinción se integra al monitoreo en línea y notifica al NOC y a la contraparte del CLIENTE. No se cita una edición específica de la norma NFPA, ya que el requisito de extinción se cumple por sí mismo y la norma externa no se invoca como fuente.

La Figura [14](#fig:racks-talca) muestra cómo se reparte el equipamiento de cómputo y red en los dos racks de la sala.

<a id="fig:racks-talca"></a>
![](https://raw.githubusercontent.com/PatricioH315/LafroX/95ed2c9a1cc20aa7ad9f3ebbe03cafa0e1e1259c/04/figuras/centros_de_datos/Racks_CD_Talca.png)

**Figura 14.** Distribución de U y ocupación proyectada de los racks del CD Talca

*Fuente: elaboración propia.*

El rack R01 aloja los tres nodos del clúster, de 2U cada uno, la consola KVM y la NAS WORM; el rack R02 aloja el ODF, los paneles, los dos switches de núcleo, el switch de gestión, el par de firewalls y la bandeja del operador con la ONT de fibra y el router LTE. Cada rack ocupa 12U de 42 (29 %). La carga de R01 es de 5,2 kW base y 6,2 kW de diseño, y la de R02, de 0,65 kW base y 0,8 kW de diseño; las cargas base suman los 5.850 W de la Tabla 4.3-1, y las de diseño, los 7,0 kW que resultan al agregar el margen de 20 %. La figura dibuja comprimidos los bloques libres e indica la posición de cada equipo en U. Los racks de servidores son independientes de los racks de equipos de comunicación. La ocupación proyectada reserva margen de crecimiento a tres años, coherente con el 20 % de reserva de la carga eléctrica (Tabla 4.3-1), de modo que la ocupación declarada y su margen quedan fijados en la figura y en el Formulario T-11.

El control de acceso y la seguridad física del recinto comprenden:

- Seguridad física y control de acceso biométrico basado principalmente en biometría facial con AFIS como respaldo.
- Registro de todo ingreso y egreso en una bitácora auditable con identificación, fecha, hora y motivo.
- Un espacio para atender a las personas en proceso de enrolamiento entre el acceso principal y el término del pasillo de la zona de control, además de una estación de enrolamiento fuera de las instalaciones del recinto técnico.
- Un acceso al término del pasillo que impide el paso de más de una persona a la vez, con nueva verificación de identidad previa al ingreso.
- Videovigilancia y monitoreo IP con imágenes en línea disponibles al menos los últimos 30 días y respaldo recuperable.

Las instalaciones sanitarias, las zonas de seguridad ante emergencia y las áreas exteriores existentes en el edificio del CLIENTE se utilizan, sin implementarlas nuevamente dentro del recinto. La bitácora auditable se conserva por un período de retención no inferior a cinco años, coherente con el piso que las Bases fijan para la retención de la auditoría del proyecto.

Los equipos de energía y climatización y los controles de acceso anteriores se ordenan físicamente como muestra la Figura [15](#fig:recinto-talca), que distribuye el recinto por zonas y líneas de acceso.

<a id="fig:recinto-talca"></a>
![](https://raw.githubusercontent.com/PatricioH315/LafroX/95ed2c9a1cc20aa7ad9f3ebbe03cafa0e1e1259c/04/figuras/centros_de_datos/Recinto_CD_Talca.png)

**Figura 15.** Distribución interna del recinto técnico del CD Talca por zonas y líneas de acceso

*Fuente: elaboración propia.*

El plano ordena el recinto en profundidad progresiva. En el exterior quedan el grupo electrógeno con su estanque, el empalme con la transferencia automática entre red y generador, las condensadoras de la climatización y la llegada de la fibra y el LTE por dos ductos independientes. La línea técnica reúne la sala de UPS y baterías, el tablero eléctrico independiente del recinto y la acometida de comunicaciones, junto con la zona de trabajo y la zona de respaldo. La línea restringida contiene solo la sala de servidores y comunicaciones, con los racks R01 y R02, la climatización de precisión y la detección y extinción. El ingreso sigue un único recorrido: acceso principal, pasillo de control con espacio de enrolamiento, esclusa que admite una persona a la vez con nueva verificación y, recién entonces, la sala; la estación de enrolamiento y los baños quedan fuera del recinto. Los puestos de trabajo y el área de respaldo quedan en la línea técnica, separados de la sala de equipos, de modo que las labores habituales de operación no exigen ingresar a la línea restringida. La separación física de generadores y baterías respecto del área de servidores evita que una falla de energía o de clima contamine el cómputo, y deja al proveedor de fibra y al de climatización sin cruzar la última línea del recinto.

El sitio monitorea en línea la temperatura, la humedad y la presencia de agua, con alertamiento integrado a la plataforma de observabilidad. El estado de los puntos controlados del recinto converge en la plataforma de monitoreo, con destinatario, canal, tiempo de respuesta y procedimiento escrito. La observabilidad reutiliza el mecanismo del sitio on-premise hacia la nube que define la arquitectura de despliegue del apartado [4.2.4](#sec:despliegue). La convergencia en un solo tablero constituye la plataforma de observabilidad del sitio. No se declara una plataforma DCIM/BMS de terceros porque las Bases no la exigen y el monitoreo ambiental y de alertas se satisface con el monitoreo en línea y su alertamiento integrado.

El cómputo almacenado onsite corre sobre un clúster virtualizado de tres nodos con redundancia N+1 y almacenamiento distribuido que tolera la pérdida de al menos un nodo con quórum real. El almacenamiento local combina un nivel para la base transaccional (RAID 10 NVMe) y otro para el respaldo local (NAS D-05, RAID 6), justificados frente a las alternativas en la sección [4.4.10](#sub:adr-10). La instancia de escritura es el punto único declarado y se mitiga con reinicio en otro nodo del clúster.


<a id="sec:e-especificaciones-del-sitio-secundario-y-"></a>
## 4.3.2 Especificaciones Data Center Secundario

El Data Center Secundario sostiene la continuidad cuando la operación primaria no está disponible y garantiza la recuperación de la plataforma y de los datos con objetivos declarados de tiempo y de pérdida. La modalidad activo-pasiva se declara y justifica primero; luego se materializa en sitios de recuperación, replicación, objetivos RPO/RTO y procedimientos de conmutación y retorno.

En coherencia con el carácter híbrido obligatorio de la solución, hay dos sitios de recuperación: la región AWS us-east-1 para el dominio en nube y el gabinete de borde del centro de distribución de Concepción para el dominio on-premise. En ambos se sostienen los objetivos de continuidad de los servicios críticos: RTO ≤ 4 horas y RPO ≤ 15 minutos, probados al menos dos veces al año con conmutación real y con respaldo 3-2-1-1-0. Sobre esos objetivos se sostiene el compromiso contractual penalizable de ≥ 99,9 % mensual de la transacción de negocio de extremo a extremo. El desglose componente por componente de la réplica y de la política de respaldo se entrega en el Formulario T-11.

### 4.3.2.1 Modalidad del sitio secundario

La modalidad declarada es activo-pasiva en caliente: la región de recuperación mantiene una réplica reducida pero funcional de la plataforma que es escalable a carga completa durante la conmutación y que se promueve sólo ante la indisponibilidad de la región primaria. La elección se justifica frente a las alternativas, como exigen las Bases:

- Frente al activo-activo: duplica la infraestructura y exige reconciliación de doble escritura entre sitios sin beneficio medible para el volumen transaccional del caso, por lo que su costo y su complejidad operacional no se justifican.
- Frente a la recuperación en frío desde respaldos: exige reconstruir la plataforma y restaurar los datos antes de volver a operar, lo que no es compatible con el objetivo de continuidad de los servicios críticos.

El costo de la modalidad se acota porque la región secundaria no es una segunda producción: contiene solo los recursos que exige la recuperación. Estos son la réplica pasiva promovible del núcleo transaccional, la réplica reducida de aplicación que escala durante la conmutación y las copias de respaldo. El propio caso expresa este criterio al exigir declarar la región primaria y la secundaria.

### 4.3.2.2 Región o sitio de recuperación

La solución tiene dos sitios de recuperación, uno por dominio en coherencia con el carácter híbrido obligatorio: la región AWS us-east-1 para el dominio en nube y el gabinete de borde del CD Concepción para el dominio on-premise. La Tabla 4.3-3 compara ambos sitios en distancia y amenazas comunes:

<a id="tab:4-3-3"></a>
**Tabla 4.3-3.** Sitios de recuperación: distancia y análisis de amenazas comunes
| Sitio de recuperación | Dominio que restituye | Distancia declarada | Análisis de amenazas comunes |
| --- | --- | --- | --- |
| Región AWS us-east-1 | Nube | ≈ 7.700 km de la región primaria sa-east-1 | Continente distinto y sin dependencia de la sismicidad ni de la malla eléctrica chilena y no comparte eventos de fuerza mayor con el sitio principal |
| CD Concepción (gabinete de borde) | On-premise | ≈ 200 km del CD Talca en línea recta, 250 km por carretera | Comparte con Talca la sismicidad de zona costera y el corte de la malla eléctrica nacional; esa exposición se mitiga con la independencia operacional de ambos sitios (operación autónoma 24 horas y alimentación protegida) y porque el dominio en nube no comparte esas amenazas |

La elección de la región us-east-1 como sitio de recuperación en nube y la habilitación de la recuperación ante desastres se declaran de forma incondicional. La transferencia internacional de datos personales que exige la continuidad se trata con los siguientes resguardos de la arquitectura de seguridad:

- Acuerdo de tratamiento con el proveedor de nube y cifrado en reposo y en tránsito extremo a extremo.
- Minimización: la región secundaria no se explota analíticamente ni se usa para consultas de negocio, solo para continuidad.
- Exclusión de los datos de geolocalización de personas de la replicación transfronteriza; permanecen solo en sa-east-1 y la exclusión se registra en el inventario de tratamientos.

En consecuencia, los objetivos de RTO y RPO no quedan supeditados a una aprobación futura.

La región secundaria contiene los recursos necesarios para la recuperación:

- La réplica de Aurora mediante Aurora Global Database y la réplica de DynamoDB mediante Global Tables.
- La copia de los buckets de S3 y las copias de AWS Backup.
- Una réplica reducida de la plataforma de aplicación que escala a carga completa durante una conmutación.

Dos capacidades quedan fuera de esa región por diseño: la analítica, porque la región secundaria no se explota analíticamente, y las consultas sobre datos de geolocalización de personas, que no se replican fuera de sa-east-1 conforme a los resguardos de residencia declarados.

Para la recuperación on-premise, el gabinete de borde del CD Concepción no está en espera: opera de forma autónoma todos los días con la tipología de borde operacional que fija el caso. Ante una contingencia que afecte solo a la bodega de Talca, asume la carga de esa bodega mediante la promoción controlada del motor de almacenes. El gabinete se dimensiona a su tipología mediante cuatro condiciones:

- Alimentación protegida con UPS y respaldo para la autonomía declarada.
- Climatización de precisión acorde al equipamiento del borde.
- Control de acceso.
- Monitoreo remoto integrado al NOC del sitio.

El listado componente por componente (cómputo, almacenamiento, enlace redundante y respaldo de alimentación) se entrega en el Formulario T-11. Los gabinetes de borde de los tres cross-docking no forman parte del sitio de recuperación; se especifican en el Formulario T-11 y su arquitectura se muestra en la Figura [2](#fig:crossdocking), sin repetir aquí la tipología.

La Figura [16](#fig:cd-concepcion) muestra el gabinete de borde de Concepción y el equipamiento con que opera todos los días.

<a id="fig:cd-concepcion"></a>
![](https://raw.githubusercontent.com/PatricioH315/LafroX/95ed2c9a1cc20aa7ad9f3ebbe03cafa0e1e1259c/04/figuras/centros_de_datos/Arquitectura_Fisica_CD_Concepcion.png)

**Figura 16.** Gabinete de borde del CD Concepción

*Fuente: elaboración propia.*

La fibra es el enlace principal y el LTE lo respalda; ambos llegan a un par de firewalls en alta disponibilidad que termina el túnel hacia la nube. Detrás, dos switches de núcleo en stack conectan el servidor Proxmox de nodo único, que aloja cuatro máquinas virtuales: VM-C01 con el WMS, VM-C02 con PostgreSQL, VM-C03 con la caché de Keycloak y VM-C04 con RabbitMQ, el shipper y el colector ADOT. En la bodega, los terminales MC9400 y las impresoras de andén trabajan por Wi-Fi 6E contra el WMS local; en la cadena de frío, los sensores entregan sus lecturas al gateway IoT, que las publica por MQTTS y bloquea el despacho ante una excursión térmica. La figura muestra que Concepción ejecuta la misma pila de Talca en una sola máquina. Por eso puede asumir la bodega de Talca con la promoción controlada del motor de almacenes, sin instalar software nuevo durante la contingencia. Como sitio de recuperación, Concepción lleva en par los firewalls y los switches de núcleo; el servidor queda como punto único de falla aceptado, cubierto por la operación autónoma de 24 horas ante la pérdida del enlace y, ante su falla, por su reposición y la reconstrucción de la base local desde el estado central, al que Concepción ya entregó sus eventos por las colas (sección [4.2.5](#sec:conexiones)).

### 4.3.2.3 Replicación

La replicación de datos es continua hacia el sitio de recuperación en nube con medición y alertamiento del retraso de replicación. Cada dominio de datos alcanza el objetivo de punto de recuperación con su propio mecanismo, como resume la Tabla 4.3-4:

<a id="tab:4-3-4"></a>
**Tabla 4.3-4.** Replicación y RPO por dominio de datos
| Dominio de datos | Mecanismo de replicación | RPO / retraso declarado |
| --- | --- | --- |
| Transaccional en nube (Aurora PostgreSQL) | Aurora Global Database hacia us-east-1 | $<$ 1 s |
| Telemetría (DynamoDB) | Global Tables | Continuo |
| Evidencia, documentos y respaldos (S3, AWS Backup) | Replicación de S3 entre regiones con control de tiempo | ≤ 15 min para el 99,99 % de los objetos |
| WMS on-premise (PostgreSQL de Talca) | AWS DMS por la VPN sobre el registro de escritura anticipada | ≤ 15 min con enlace |
| Mensajes críticos | Patrón outbox en base y cola | ≤ 15 min |
| Mensajes no críticos | Cola con reposición diferida | ≤ 24 h |

Todos los dominios críticos se replican de forma continua. El único dominio cuyo retraso de replicación depende de una condición externa es la réplica del WMS de Talca, ya que viaja por la WAN. Si Talca pierde simultáneamente sus dos caminos de enlace, el registro de escritura de VM-02 retiene los cambios que AWS DMS leerá al reconectar; la base local permanece autoritativa durante el corte y el retraso se mide de forma continua con alertas a los 5 y a los 15 minutos. Durante ese corte la copia remota del WMS queda desactualizada hasta un máximo de 24 horas, por lo que el RPO remoto de 15 minutos de esa réplica rige solo con enlace; el registro que el corte obliga a retener está dimensionado en la arquitectura de despliegue.

### 4.3.2.4 RPO y RTO

Los objetivos de continuidad de los servicios críticos son RTO ≤ 4 horas y RPO ≤ 15 minutos. La Tabla 4.3-5 resume los objetivos que gobiernan este sitio secundario y el compromiso sobre el que se miden.

<a id="tab:4-3-5"></a>
**Tabla 4.3-5.** Objetivos de continuidad
| Activo | Objetivo | Valor declarado |
| --- | --- | --- |
| Servicios críticos | Tiempo de recuperación (RTO) | ≤ 4 h |
| Servicios críticos | Punto de recuperación (RPO) | ≤ 15 min |
| Transacción de negocio crítica de extremo a extremo | Disponibilidad mensual | ≥ 99,9 % |
| Infraestructura por componente | Disponibilidad mensual | 99,95 % |

Estos objetivos no dependen de aprobaciones ni de otros eventos futuros del CLIENTE. Su alcance tiene una precisión, que corresponde a la réplica remota del WMS durante un corte de enlace: mientras el sitio está aislado su base local es la fuente autoritativa y no pierde información, pero la copia en la nube no puede actualizarse hasta que el enlace vuelve, como se indicó en la replicación. El RPO de la sección anterior se verifica en las pruebas de recuperación que miden el RTO y el RPO efectivamente alcanzados.

<a id="sub:conmutacion-regional"></a>
### 4.3.2.5 Procedimiento de conmutación

El procedimiento de conmutación está documentado, automatizado en la mayor medida posible y es ejecutable por el personal del CLIENTE tras la transferencia de conocimiento. La conmutación de región separa lo reversible de lo irreversible: el enrutamiento hacia us-east-1 se conmuta de forma automática, pero su retorno automático queda deshabilitado: una vez promovida la base, el tráfico vuelve a la región primaria solo mediante el procedimiento de retorno, después de reconciliar. En cambio, la promoción de la base de datos rompe la replicación y obliga a reconciliar al volver, por lo que exige confirmación y autorización del CLIENTE. La Tabla 4.3-6 muestra la secuencia completa.

<a id="tab:4-3-6"></a>
**Tabla 4.3-6.** Secuencia de conmutación de región
| Paso | Acción | Ejecución | Tiempo |
| --- | --- | --- | --- |
| 1 | Detección por verificación de salud de la región primaria | Route 53 | $<$ 5 min |
| 2 | Conmutación del enrutamiento hacia us-east-1 | Automática | — |
| 3 | Confirmación y autorización de la promoción | CLIENTE, con aviso por SNS | — |
| 4 | Promoción de Aurora en us-east-1 | Systems Manager Automation | 15–20 min |
| 5 | Escalado de la plataforma de aplicación a carga completa | Systems Manager Automation | $<$ 30 min |
| 6 | Restitución de Keycloak, API pública y privada y Verified Access | Systems Manager Automation | — |
| 7 | Actualización de DNS | Systems Manager Automation | 45–60 min |
| 8 | Reconexión del broker y sincronización del borde | Systems Manager Automation | — |
| 9 | Validación con escrituras de pedidos y sincronización | Operación | — |

Los pasos con tiempo declarado, ejecutados en serie y en el peor caso, suman cerca de 2 horas más el tiempo de la decisión, dentro del RTO de 4 horas. Solo el tercer paso requiere intervención humana; ahí reside la protección contra una conmutación innecesaria. Las transacciones se reabren solo tras la validación del noveno paso, porque el cambio de DNS no restituye por sí solo la identidad ni las API. Como los pasos cuarto a octavo están automatizados, el equipo de tecnologías de información del CLIENTE de cuatro personas puede ejecutar el procedimiento tras la transferencia de conocimiento, con el acompañamiento del servicio de operación del proyecto.

Cuando la contingencia afecta solo a la bodega de Talca, el plan de recuperación local promueve el motor de almacenes del CD Concepción, que opera de forma autónoma todos los días, con un RTO adicional de 1 a 2 horas dentro de la ventana de 4 horas. En esa contingencia local la identidad no requiere conmutación, porque su autoridad reside en la nube y las cachés locales son de solo lectura.

### 4.3.2.6 Procedimiento de retorno

Existe un procedimiento de retorno al sitio principal, documentado y probado, que incluye la reconciliación de los datos generados durante la contingencia. El retorno a la región primaria sigue seis pasos:

1. Resincronización con verificación de alcance.
2. Reconciliación de las transacciones de la contingencia contra la bitácora.
3. Transferencia de los eventos pendientes.
4. Conmutación coordinada del DNS.
5. Validación funcional.
6. Informe con el tiempo real empleado.

El procedimiento de retorno se prueba en cada ensayo de recuperación semestral, de modo que queda declarado y ejercitado.

### 4.3.2.7 Pruebas del plan de recuperación y respaldos

El procedimiento de conmutación y el de retorno se ensayan dos veces al año con conmutación real, incluidas escrituras de pedidos y sincronización en us-east-1; el RTO y el RPO medidos deben cumplirse en el 100 % de los ensayos. La inyección de fallas y la restauración mensual de respaldos se describen en la sección [4.2.4.6](#sub:6-verificacion-de-la-continuidad), y la política 3-2-1-1-0 con sus retenciones en la sección [4.2.4.5](#sub:5-respaldos-esquema-3-2-1-1-0-rnf-20-07).


<a id="sec:m-registro-de-decisiones-de-arquitectura"></a>
# 4.4 Registro de decisiones de arquitectura

Registro consolidado de las dieciséis decisiones de arquitectura que condicionan la solución. Para cada decisión se declara la elección, las alternativas descartadas y el criterio de selección; cuando corresponde, se exige evidencia verificable.

<a id="sub:adr-01"></a>
## 4.4.1 ADR-01 · Estilo arquitectónico

**Decisión adoptada.** Monolito modular en Laravel 13 sobre PHP 8.5, con los módulos M1–M12 separados por espacios de nombres PSR-4 y dependencias fijadas por `composer.lock`. Un solo artefacto, construido una vez por versión, se ejecuta en perfiles separados: API y `wms_only` con PHP-FPM, y shipper, consumidor de reconciliación, trabajos y planificador como procesos PHP de línea de comandos. El motor de optimización de rutas de M4 y el transporte AS2 de M11 quedan fuera del artefacto, tras un contrato versionado.

**Alternativas descartadas:**

- *Monolito modular en Django y Python 3.12*: técnicamente viable con los mismos contratos, pero la arquitectura lógica adopta Laravel y mantener ambos runtimes obligaría a operar dos cadenas de construcción, de dependencias y de parches.
- *Microservicios en EKS*: el caso no exige desplegar ni escalar cada módulo por separado, cuatro personas no operan un plano de control y el costo total de propiedad en 56 meses sube sin beneficio.
- *Monolito clásico del WMS de 2013*: sin fronteras de módulo y con el proveedor desaparecido, lo que impide desplegar los módulos por separado.
- *Traducir a PHP el ruteo y el AS2 sin prueba*: la equivalencia de un solver o de un conector no se deduce del cambio de lenguaje, por eso ambos se aíslan.

**Criterio de selección.** Coherencia con la arquitectura lógica (4.1); pertinencia al volumen real; operabilidad por cuatro personas; despliegue y escalado independiente por perfil sin particionar el dominio.

**Consecuencias.** La imagen incluye PHP-FPM, el intérprete de línea de comandos y las extensiones declaradas en la arquitectura de despliegue; el pipeline agrega `composer audit`, PHPUnit, PHPStan/Larastan y Pint; el dimensionamiento de los perfiles se recalcula para PHP en lugar de trasladar los valores anteriores. El motor de ruteo agrega una imagen propia al pipeline y una tarea de Fargate bajo demanda.

**Evidencia exigida.** Pruebas de paridad de contratos, datos y colas; prueba de carga por perfil; y, para el motor de ruteo, la generación de rutas de toda la operación en menos de 20 minutos, que es condición de aceptación del motor que se seleccione.

<a id="sub:adr-02"></a>
## 4.4.2 ADR-02 · Conectividad WAN

**Decisión adoptada.** Doble camino por sitio: fibra + LTE en los centros de distribución, Starlink + LTE en los cross-docking. Conmutación automática $<$ 30 s.

**Alternativas descartadas:**

- *Fibra en cross-docks*: naves industriales sin cobertura de fibra; costo de obra desproporcionado.
- *VSAT GEO*: latencia 500–700 ms RTT; penaliza el tiempo de respuesta y cuesta más.
- *Tri-camino (fibra + Starlink + LTE)*: tercer camino no aporta disponibilidad significativa dado que cada sitio opera autónomamente ante pérdida total de enlace (24 h CD, 14 h terreno).

**Criterio de selección.** Dos caminos de física distinta evitan el punto único de falla; la autonomía local cubre la pérdida total de enlace, por lo que un tercer camino es innecesario; cero mantención de radio para el equipo de 4 personas del CLIENTE.

<a id="sub:adr-03"></a>
## 4.4.3 ADR-03 · Modelo de despliegue híbrido

**Decisión adoptada.** Borde operacional on-premise (WMS maestro Talca, edge Concepción, WMS en cross-docks) + carga principal en AWS. 11 componentes on-prem, 12 híbridos, 13 nube pura.

**Alternativas descartadas:** *Solo nube*: inadmisible; sin enlace la bodega muere en minutos; picking en cámara -22 °C inviable con RTT 40–80 ms; *Solo on-premise*: inadmisible.

**Criterio de selección.** Único modelo que cumple el despliegue híbrido obligatorio; latencia ≤ 1 s en cámara resuelta localmente; autonomía 24 h CD / 14 h terreno; TCO contenido con servicios administrados AWS.

<a id="sub:adr-04"></a>
## 4.4.4 ADR-04 · Persistencia políglota

**Decisión adoptada.** PostgreSQL+PostGIS (transaccional WMS, CP), Aurora (OLTP cloud + DRP), DynamoDB (IoT raw, AP, TTL 30 d), S3+Redshift Serverless (OLAP + series de temperatura), S3 Object Lock/Glacier (retención legal por dominio de datos, de 5 a 7 años según la tabla de respaldos). La aplicación accede a PostgreSQL con PDO y el Query Builder de Laravel; las consultas geográficas de M4 usan SQL PostGIS parametrizado sobre índices espaciales GiST, y el esquema evoluciona con migraciones Laravel aditivas. La réplica DMS del WMS alimenta solo un esquema de réplica de lectura; el estado central se actualiza por los eventos de reconciliación, con una clave de origen única por evento.

**Alternativas descartadas:**

- *Motor único relacional*: no escala ingesta IoT sin degradar picking.
- *InfluxDB*: segundo motor exótico a operar; serie de tiempo cabe en capa OLAP.
- *DynamoDB para todo*: no ofrece ACID cross-tabla para reconciliación determinista.

**Criterio de selección.** Posición CAP declarada por dominio; 3 motores administrados operables por el equipo de TI del CLIENTE; retención sanitaria D.S. 977/96 con inmutabilidad; RPO ≤ 15 min por réplica Aurora.

<a id="sub:adr-05"></a>
## 4.4.5 ADR-05 · Mensajería asíncrona

**Decisión adoptada.** La cadena de eventos sigue cuatro pasos:

1. Publicación local: RabbitMQ opera por sitio con colas durables, mensajes persistentes y confirmación de publicación, como buffer de 24 h.
2. Envío del shipper: un proceso PHP con el adaptador AMQP `php-amqplib` publica cada evento como sobre JSON canónico y versionado en una cola SQS FIFO de reconciliación, por HTTPS hacia un VPC Endpoint, y solo retira el mensaje local cuando SQS confirma la recepción.
3. Consumo: un proceso PHP dedicado lee esa cola con el SDK de AWS y valida el esquema del sobre.
4. Confirmación: el consumidor aplica el sobre y confirma solo después de persistir el resultado.

Los trabajos internos de Laravel usan colas SQS distintas, de modo que ningún sobre externo llega al deserializador de trabajos del framework. IoT Core MQTT mantiene la ingesta del borde.

**Alternativas descartadas:**

- *REST síncrono*: no sobrevive un corte a mitad de ventana y rompe la reconciliación.
- *Kafka/MSK*: operar clústeres en cinco sitios es desproporcionado para el equipo disponible y para el volumen de mensajes del caso.
- *Una sola cola SQS para eventos y trabajos*: acopla el formato externo al serializador del framework e impide versionar el sobre.
- *Redis y Horizon en los sitios*: agregan un tercer motor local sin mejorar la durabilidad que ya dan PostgreSQL y RabbitMQ.
- *Workers Celery*: correspondían al backend Django y se retiran con él.

**Criterio de selección.** Resiliencia offline (buffer local y reproducción idempotente); reconciliación determinista; independencia del formato respecto del lenguaje; Zero Trust (todo saliente); costo total proporcional al volumen.

**Consecuencias.** La cola FIFO agrupa el orden por sitio y agregado de negocio, deduplica por el identificador del evento, usa una visibilidad de 60 s, cinco intentos antes de la cola de mensajes fallidos y una retención de 4 días; la base central guarda la clave de origen de cada evento aplicado para impedir su doble aplicación. El consumidor acepta la versión vigente del sobre y la anterior. Las alarmas vigilan la edad del mensaje más antiguo, la profundidad por grupo y los mensajes fallidos.

**Evidencia exigida.** Prueba de corte de 24 h por sitio con drenaje completo sin pérdida ni duplicados, dentro de las 2 h comprometidas; prueba de mensajes duplicados, fuera de orden y de versión desconocida.

<a id="sub:adr-06"></a>
## 4.4.6 ADR-06 · Identidad híbrida (Modelo B)

**Decisión adoptada.** Keycloak IdP maestro en AWS (ECS Fargate, 2 tareas Multi-AZ, backend Aurora) + caché local solo lectura (TTL 24 h, igual a la autonomía del CD) en Talca, Concepción y los cross-docking, con un verificador local en el mismo nodo que, en cada relevo de turno sin enlace, valida el manifiesto de turno firmado por Keycloak y un segundo factor local: el PIN personal sobre el terminal enrolado por MDM. Con enlace, Keycloak renueva el manifiesto al menos cada hora para una ventana de 26 h, de modo que un corte iniciado justo antes de una renovación conserva al menos 25 h de verificación local. La caché de 24 h y la credencial de turno cumplen propósitos distintos: la caché conserva los datos de identidad y de turno recibidos y no emite sesiones, mientras que la credencial de turno —hasta 8 h en bodega y 14 h en reparto— limita cuánto dura el acceso de una persona; así, un corte de 24 h cubre dos relevos en bodega, cada uno habilitado por el verificador. Durante el corte no se promete revocación remota inmediata. El backend Laravel valida los JWT OIDC de Keycloak —firma con las claves publicadas, emisor, audiencia, vencimiento y alcance— y aplica políticas por recurso, turno, ruta, sitio y empresa; no se incorpora Sanctum ni Passport como segundo emisor de identidades. OTP para conductores externos.

**Alternativas descartadas:**

- *IdP solo nube*: paraliza bodega ante corte.
- *AD maestro local*: duplica administración, crea maestro a promover en DR.
- *Keycloak maestro local*: nube no puede autenticar si el enlace cae.

**Criterio de selección.** Autonomía offline sin maestro local a promover; autoridad única en nube; OTP sin correo para externos; autenticación multifactor; operado por el equipo reducido del CLIENTE sin directorio propietario.

<a id="sub:adr-07"></a>
## 4.4.7 ADR-07 · Movilidad de terreno

**Decisión adoptada.** App nativa Android Kotlin para preventa, reparto y picking. SQLite/Room, SDK Zebra DataWedge (GS1 + QR), impresión BT (ZQ620), POS PAX. Dispositivos Rugged: EC55, TC58e, MC9400 Cold Storage.

**Alternativas descartadas:** *PWA*: no controla SDK Zebra de forma fiable ni persiste turno completo sin capa nativa; *Híbrida Flutter*: runtime intermedio degrada interacción con periféricos industriales.

**Criterio de selección.** Control nativo de periféricos (DataWedge intents); offline total 14 h con sincro $<$ 10 min; UI para guantes -22 °C, una mano, lluvia; curva de aprendizaje ≤ 2 h; un artefacto para 3 perfiles.

<a id="sub:adr-08"></a>
## 4.4.8 ADR-08 · Destino del WMS legado 2013

**Decisión adoptada.** Reemplazo total en Etapa 1 por módulo WMS del monolito: Talca maestro, Concepción edge, cross-docks sobre E-01. Migración por dominio, oleadas por sitio, reversión azul-verde. Durante la coexistencia cada operación tiene un único escritor autorizado, de modo que el WMS de 2013 y el nuevo nunca escriben a la vez stock, cobros o documentos tributarios; la reversión devuelve el tráfico al escritor anterior solo tras detener el nuevo y conciliar los pendientes.

**Alternativas descartadas:** *Mantener e integrar*: proveedor desaparecido, sin soporte; no soporta multi-sitio, picking FEFO (primero en expirar, primero en salir), SSCC GS1 ni conteo cíclico ciego; *Extender a otros sitios*: arrastra riesgo de soporte inexistente en ventana crítica.

**Criterio de selección.** Funciones de bodega que el WMS de 2013 no contempla; riesgo operacional inaceptable; TCO amortizado con reducción conteo 2,3 %→0,3 % y merma 1,7 %→$<$1 %; reversión azul-verde garantizada.

<a id="sub:adr-09"></a>
## 4.4.9 ADR-09 · Estrategia DR

**Decisión adoptada.** Activo-pasivo warm standby multi-región: DMS CDC desde VM-02 de Talca hacia Aurora y Aurora Global Database hacia us-east-1; los demás sitios sincronizan eventos por colas. DRP local Talca→Concepción (RTO +1–2 h); pruebas 2×/año; respaldo 3-2-1-1-0 con S3 Object Lock.

**Alternativas descartadas:**

- *Activo-activo*: duplica infraestructura y exige reconciliación de doble escritura sin beneficio medible.
- *Backup + restore frío*: exige reconstruir la plataforma y restaurar los datos antes de operar, lo que no es compatible con el RTO de 4 h.
- *Solo intrarregional*: degrada el objetivo de continuidad, porque ante la caída de la región la recuperación dependería de reconstruir la plataforma desde respaldos; se descarta y la recuperación en us-east-1 queda declarada de forma incondicional.

**Criterio de selección.** RTO ≤ 4 h / RPO ≤ 15 min; proporcionalidad al volumen; DR de identidad resuelto en nube; pruebas semestrales reales.

<a id="sub:adr-10"></a>
## 4.4.10 ADR-10 · Almacenamiento on-premise y RAID

**Decisión adoptada.** RAID 10 NVMe en los nodos del clúster de Talca y RAID 10 sobre las cuatro bahías del servidor de Concepción; RAID 6 en el NAS de respaldo local D-05; la evidencia de entrega vive en S3; clúster Proxmox VE con almacenamiento Ceph en N+1.

**Alternativas descartadas:** *RAID 5*: probabilidad de URE durante rebuild en discos 8–16 TB; solo tolera 1 fallo; *RAID 1 puro para todo*: sobre-costo 50 % aplicado a datos no críticos sin beneficio proporcional.

**Criterio de selección.** IOPS deterministas en ventana de despacho ($>$100 K vs. 840 necesarios); tolerancia a fallo de disco con justificación; TCO contenido con RAID 10 solo en lo transaccional.

<a id="sub:adr-11"></a>
## 4.4.11 ADR-11 · Integración B2B/EDI canal moderno

**Decisión adoptada.** Hub EDI centralizado GS1 (EANCOM/GS1 XML + EPCIS) en nube, con conector configurable por cadena, equivalencias GTIN, bandeja de excepciones y ACL hacia ERP/GDE; la transformación y las reglas corren en el perfil EDI de Laravel. Canal moderno operativo ≤ enero 2029. El transporte AS2 usa OpenAS2, de licencia BSD, corre en un contenedor propio de ECS Fargate tras un Network Load Balancer con paso TLS directo en TCP 443: TLS 1.3 termina en el contenedor. El grupo de seguridad admite solo las IP registradas de cada cadena; el transporte firma y cifra mensajes, administra certificados por cadena y acuses MDN, y entrega al perfil EDI por contrato versionado. Los certificados se guardan en Secrets Manager (sección [4.4.15](#sub:adr-15)).

**Alternativas descartadas:**

- *Punto a punto por cadena*: multiplica adaptadores y su mantenimiento.
- *EDI delegado al ERP*: expone una frontera frágil y permite escritura directa desde la cadena, contra Zero Trust.
- *AWS Transfer Family*: su servidor AS2 recibe por HTTP en TCP 5080 y no satisface TLS 1.3 en tránsito (RT-11.08; Bases Técnicas Transversales, Cap. 11, p. 23).
- *Biblioteca PHP para AS2*: carece de implementación validada con las cadenas.

**Criterio de selección.** Estandarización GS1, esfuerzo marginal por cadena nueva, aislamiento del ERP por la ACL, TLS 1.3 verificable y plazo de enero de 2029; el contenedor propio es la excepción a la preferencia por servicios administrados (RT-03.05; Bases Técnicas Transversales, Cap. 3, p. 8) necesaria para cumplir RT-11.08 (Bases Técnicas Transversales, Cap. 11, p. 23).

**Evidencia exigida.** Prueba de interoperabilidad por cadena con TLS 1.3, firma, cifrado, certificado y MDN antes de habilitarla.

<a id="sub:adr-12"></a>
## 4.4.12 ADR-12 · Absorción del peak de septiembre

**Decisión adoptada.** El cómputo elástico escala de forma independiente por perfil:

- API con PHP-FPM: de 2 a 4 tareas en el peak y techo de 8, por procesos ocupados sobre 70 %.
- Consumidor de reconciliación: de 2 a 4 tareas, por la edad del mensaje más antiguo.
- Trabajos: de 2 a 4 tareas, por la profundidad de cada cola, con `erp-sync` fijo en 2 procesos para no saturar el ERP.
- Planificador: una sola tarea.

Escala de forma predictiva y reactiva el cómputo elástico. Aurora pasa de large a xlarge (escritor en sa-east-1a y un lector promovible en sa-east-1b), y DynamoDB opera bajo demanda. La capacidad *Base* se contrata mediante Savings Plans y el peak se cubre con cómputo efímero.

**Alternativas descartadas:**

- *Capacidad fija al peak*: paga 12 meses la capacidad de 3 semanas.
- *Solo escala reactiva*: el peak de septiembre es predecible y la reactiva sola introduce retardo en la ventana crítica.
- *Trasladar las cifras del backend anterior (6 tareas de aplicación y 4 de workers Celery)*: eran supuestos de otro runtime y no valen para PHP-FPM.

**Criterio de selección.** Perfil no plano al peak ×1,5; cuello de botella identificado; FinOps: base reservada y peak efímero; congelamiento del 1 al 25 de septiembre y de diciembre.

**Consecuencias.** El número de tareas se deriva de dos supuestos declarados en el dimensionamiento —50 ms de CPU y 150 ms de residencia por solicitud— y no de una medición; las conexiones a PostgreSQL quedan acotadas por el número de procesos de cada perfil.

**Evidencia exigida.** Prueba de carga en Preproducción que mida el consumo real por solicitud y por sobre, la saturación de PHP-FPM, las conexiones, la edad de las colas y el rendimiento del ERP; si difieren de los supuestos, se recalculan tareas y procesos antes del paso a producción.

<a id="sub:adr-13"></a>
## 4.4.13 ADR-13 · Puerta de enlace de servicios

**Decisión adoptada.** Amazon API Gateway aloja dos API REST. La regional pública solo admite CloudFront: este agrega un encabezado de origen secreto exigido por el WAF regional y el endpoint predeterminado execute-api está deshabilitado. La privada solo admite el endpoint de interfaz execute-api de la VPC de Producción mediante política `aws:SourceVpce`. En las rutas protegidas, ambas usan la única función Lambda como autorizador de JWT de Keycloak (firma con claves publicadas, emisor, audiencia y vencimiento), modelos de validación de solicitud, planes de uso con cuotas y límites de tasa, inspección WAF e integración privada por VPC Link hacia el ALB privado. Laravel valida reglas de negocio y autorización por recurso; cada sitio mantiene la puerta de API local del WMS.

**Alternativas descartadas:**

- *Kong autoadministrado*: agrega un componente crítico que parchar en la ruta de la venta.
- *HTTP API con autorizador JWT nativo*: no ofrece API privada ni validación de modelos de solicitud.
- *Validación del token solo en Laravel*: la puerta no autentica e incumple RT-11.11 (Bases Técnicas Transversales, Cap. 11, p. 23).

**Criterio de selección.** Autenticación y validación en la puerta, separación de entradas pública y privada y acceso restringido al origen.

**Evidencia exigida.** Prueba de acceso directo denegado al origen público y a la API privada fuera del endpoint autorizado.

<a id="sub:adr-14"></a>
## 4.4.14 ADR-14 · Plataforma de observabilidad

**Decisión adoptada.** Plataforma única en nube: instrumentación con OpenTelemetry para PHP y Laravel y para las aplicaciones Kotlin, con el `transaction_id` propagado por HTTP, RabbitMQ, SQS y la capa anticorrupción; métricas propias por perfil (procesos PHP-FPM ocupados, reinicios, profundidad y edad de cola por grupo, mensajes fallidos, latencia del ERP y de escritura de VM-02); colectores ADOT on-premise con buffer 24 h, logs en CloudWatch Logs (12+24 m), métricas en CloudWatch Metrics (13 meses) y trazas en CloudWatch con retención declarada. Tableros nativos de CloudWatch para operación.

**Alternativas descartadas:** *Prometheus+Grafana+Loki local + cloud*: dos plataformas, cuando las Bases piden una sola; VM-06 sin capacidad; *AMP + X-Ray + Grafana*: cuatro servicios de observabilidad para un equipo de 4 personas; complejidad operativa desproporcionada sin ganancia funcional sobre CloudWatch nativo.

**Criterio de selección.** Las Bases piden una sola plataforma de observabilidad; buffer ADOT resuelve «sin puntos ciegos» durante corte; ninguna decisión 05:30–07:00 depende de tablero; CloudWatch es nativo de AWS y no requiere infraestructura adicional; el equipo del CLIENTE no opera servidores de observabilidad.

<a id="sub:adr-15"></a>
## 4.4.15 ADR-15 · Gestión de secretos

**Decisión adoptada.** AWS Secrets Manager (secretos con rotación: ERP, SII, Transbank, certificados AS2/EDI) + SSM Parameter Store (config no sensible). Consumo outbound por VPC Endpoint. Cifrado CMK KMS, separación de funciones. Cuenta de último recurso con credenciales en sobre sellado fuera de línea.

**Alternativas descartadas:** *HashiCorp Vault autoadministrado*: modo sellado tras reinicio exige intervención humana de madrugada; agrega infraestructura; *Sin gestor centralizado*: las Bases lo prohíben.

**Criterio de selección.** Servicio administrado sin desellado manual; Zero Trust (consumo outbound); separación de funciones vía IAM y CloudTrail; contingencia offline independiente de la nube.

<a id="sub:adr-16"></a>
## 4.4.16 ADR-16 · Acceso de personas internas y remotas

**Decisión adoptada.** AWS Verified Access protege por aplicación las consolas internas y la administración de Keycloak para oficina y trabajo remoto. Usa Keycloak con MFA como proveedor de confianza OIDC de usuario y CrowdStrike Falcon (F-03) como proveedor de postura de dispositivo; AWS WAF se asocia a la instancia. Su destino es el ALB privado del frontend Angular en Fargate, que reenvía llamadas a la API REST privada por el endpoint execute-api.

**Alternativas descartadas:** *Client VPN*: concede acceso de red y requiere un manejador de conexión adicional para verificar postura; *Solo VPN de sitio*: no cubre el trabajo remoto de RT-03.22 (Bases Técnicas Transversales, Cap. 3, p. 10) y confía en la ubicación de red.

**Criterio de selección.** Acceso por aplicación con identidad, MFA y postura para ambos orígenes, conforme a RT-03.22 (Bases Técnicas Transversales, Cap. 3, p. 10), RT-11.01 (Bases Técnicas Transversales, Cap. 11, p. 23) y RT-12.03 (Bases Técnicas Transversales, Cap. 12, p. 25).

**Evidencia exigida.** Pruebas de acceso con MFA y postura válida e inválida desde oficina y trabajo remoto.


# Referencias

Las fuentes citadas en este subdocumento son:

- *Bases administrativas* [Licitación N.° TFEP-01/2026]. (2026).
- *Bases técnicas del caso 02 — Logística: Distribuidora Puelche S.A.* (versión 1.0) [Licitación N.° TFEP-01/2026]. (2026).
- *Bases técnicas transversales* (versión 1.0) [Licitación N.° TFEP-01/2026]. (2026).


**Metadatos de portada**

- Documento: Propuesta Técnica
- Subtítulo: Formulario T-11 — Especificaciones técnicas ofertadas
- Alcance: Subdocumento 4 — Arquitectura lógica y física de la solución
- Formulario: Formulario T-11
- Fecha: 05 de octubre de 2026
- Versión: 2.0

# Formulario T-11: Especificaciones técnicas ofertadas

Este formulario detalla los componentes de infraestructura, plataforma, licenciamiento y hardware especificados para la solución, con su ubicación, su cantidad y su justificación, conforme al Formulario T-11 de las Bases Administrativas. Acompaña al Subdocumento 4 (Arquitectura lógica y física de la solución): su resumen y análisis están en el apartado 4.2.1 de ese subdocumento, y el emplazamiento de cada componente se justifica en su apartado 4.2.2. Cuando un elemento materializa un componente del catálogo de emplazamiento, la columna Componente lleva el mismo código y nombre del apartado 4.2.2 (por ejemplo, D-01 Firewall y Customer Gateway); los elementos de soporte que no son componentes de arquitectura, como la infraestructura de la sala técnica o el cableado, se identifican solo por su nombre. El equipamiento físico lo adquiere el CLIENTE, y el adjudicatario lo especifica, instala, integra y mantiene (Bases Administrativas, Art. 14.2, p. 10).

La Tabla [28](#tab:t11) reúne todos los elementos ofertados, agrupados por familia: infraestructura de cómputo y almacenamiento, red y seguridad, dispositivos de terreno y de operación, sala técnica de Talca, gabinetes de borde, plataforma de nube y software de base. Las cantidades de dispositivos de terreno y de componentes críticos incluyen una reserva del 10 % del parque de cada tipo, redondeada hacia arriba, conforme a la tabla de repuestos del numeral 8.4 de las Bases Técnicas Transversales (Cap. 8, p. 19); los supuestos que fijan cada cantidad (S-28 y S-30 a S-41) se registran en el Subdocumento 3, y el cálculo de cada cantidad está en el Anexo 4.B. El costo unitario estimado que pide RT-08.10 (Bases Técnicas Transversales, Cap. 8, p. 19) se declara en la Oferta Económica, porque la Oferta Técnica no admite precios (Bases Administrativas, Art. 50.2, p. 29).

<a id="tab:t11"></a>
**Tabla 1.** Formulario T-11: especificaciones técnicas ofertadas
| Componente | Producto / servicio ofertado | Ubicación / Lugar | Cantidad | Justificación |
| — | — | — | — | — |
| Infraestructura de cómputo y almacenamiento |  |  |  |  |
| Servidor del clúster | Servidor de rack de 2U y doble procesador, Dell PowerEdge R7625 o HPE DL385 Gen11: 2 EPYC 9124 de 16 núcleos, 128 GB DDR5 ECC ampliables, RAID 1 para el sistema y RAID 10 con 4 NVMe de 1,92 TB y repuesto en caliente, con bahías para duplicar los discos, 2 puertos de 10 GbE y 2 fuentes de 800 W | CD Talca, gabinete R01 | 3 | Tres nodos iguales dejan capacidad para todas las máquinas virtuales si falla uno (RT-03.14; Bases Técnicas Transversales, Cap. 3, p. 9), con doble fuente en circuitos distintos (RT-08.04; Bases Técnicas Transversales, Cap. 8, p. 18), y los discos NVMe en RAID 10 superan con holgura las operaciones de disco del peak de septiembre; el crecimiento de 3 veces se absorbe agregando discos y memoria en el mismo nodo. |
| D-05 — Respaldo local | NAS con bloqueo de escritura WORM y cifrado de disco | CD Talca, gabinete R01 | 1 | Es la copia local de recuperación rápida del esquema 3-2-1-1-0: restaura el WMS en hasta 4 h sin depender del enlace (RNF-20.06), y complementa la copia inmutable en nube sin reemplazarla. |
| Servidor de Concepción | Dell PowerEdge R250 con Xeon E-2300 de 8 núcleos y 16 hilos (por ejemplo, E-2378) o HPE ProLiant DL20 Gen11 con Xeon E-2400 de 8 núcleos y 16 hilos (por ejemplo, E-2478); 32 GB ampliables a 128 GB; RAID 10 sobre las 4 bahías con discos SSD de 1,92 TB (sin repuesto en caliente) | CD Concepción, gabinete de borde | 1 | Sostiene el WMS de Concepción con 24 h de operación autónoma y la promoción controlada de su motor de almacenes ante una contingencia de Talca (RNF-02.01, RT-07.02; Bases Técnicas Transversales, Cap. 7, p. 17), dimensionado a su propia bodega según la tabla de máquinas virtuales de Concepción del Subdocumento 4 (apartado 4.2.6). Fuente única declarada como punto único de falla aceptado (RT-02.11; Bases Técnicas Transversales, Cap. 2, p. 7). |
| E-01 — WMS de cross-docking (nodo) | Mini-PC industrial Advantech ARK-2250 o equivalente de rango industrial: Intel Core i5 o i7, 16 GB y NVMe de 512 GB | Curicó, Chillán y Los Ángeles; reserva en Talca | 3 + 1 de reserva = 4 | Opera en naves sin climatización, con un supuesto de diseño de hasta 50 °C en verano, y sin fibra, solo con red móvil (Bases Técnicas del caso, Cap. 6, p. 10); se conecta a la nube y a Talca a través del par de firewalls del sitio. Alimentación de entrada única: punto único de falla aceptado (RT-02.11; Bases Técnicas Transversales, Cap. 2, p. 7), cubierto por la operación local de la ventana; la unidad de reserva se guarda en Talca y viaja en el camión de línea nocturno (Bases Técnicas del caso, Cap. 3, p. 6). |
| Red y seguridad |  |  |  |  |
| D-01 — Firewall y Customer Gateway (Talca) | Clúster activo/pasivo de firewalls UTM de grado empresarial con sincronización de sesiones | CD Talca, gabinete R02; reserva en Talca | 2 + 1 de reserva = 3 | El sitio principal no admite un perímetro de equipo único (RT-08.03; Bases Técnicas Transversales, Cap. 8, p. 18): la unidad pasiva asume direcciones y túneles en menos de 30 s, en circuitos eléctricos distintos (RT-08.04; Bases Técnicas Transversales, Cap. 8, p. 18). Es el punto de terminación de la VPN Site-to-Site. La unidad de reserva cubre los firewalls de Talca y de Concepción, que son del mismo modelo. |
| D-02 — Switching (core de Talca) | Cisco Catalyst 9300-48P o equivalente en stack, con doble fuente | CD Talca, gabinete R02; reserva en Talca | 2 + 1 de reserva = 3 | Los dos equipos forman un único plano de distribución, de modo que la falla de uno no interrumpe el tráfico (RT-08.03; Bases Técnicas Transversales, Cap. 8, p. 18), y cada uno tiene doble fuente (RT-08.04; Bases Técnicas Transversales, Cap. 8, p. 18). La unidad de reserva cubre los switches de núcleo de Talca y de Concepción. |
| D-02 — Switching (gestión de Talca) | Switch de capa 2 para la VLAN de gestión | CD Talca, gabinete R02 | 1 | Aísla los puertos de administración de los servidores en una VLAN dedicada con MFA, y permite recuperar los equipos aunque la red de producción esté caída. |
| Consola KVM | Consola KVM de 1U | CD Talca, rack R01 (U24) | 1 | Da acceso local a la consola de los tres nodos y de la NAS del rack de servidores, sin conectar monitor y teclado a cada equipo. |
| Distribución horizontal | Paneles de fibra OM4 y cobre Cat6A certificado | CD Talca, racks R01 y R02 | 1 | Cableado certificado enlace por enlace (RT-06.04; Bases Técnicas Transversales, Cap. 6, p. 14), con dos ductos de ingreso independientes a la sala (RT-06.32; Bases Técnicas Transversales, Cap. 6, p. 17). |
| Red inalámbrica industrial | Puntos de acceso Wi-Fi 6E industriales en la VLAN de operaciones; los de la cámara de congelado, con rango de operación hasta -40 °C | Talca 39, Concepción 20 y cross-docking 6 (2 por plataforma) | 65 + 7 de reserva = 72 | Estimación preliminar por superficie, con mayor densidad dentro de las cámaras (S-36); la cantidad definitiva la fija el estudio de cobertura, con segmentación por tipo de dispositivo y cobertura verificada dentro de las cámaras (RT-03.23; Bases Técnicas Transversales, Cap. 3, p. 10). |
| D-03 — Enlace de fibra | Fibra óptica simétrica: Talca de 20 a 50 Mbps y Concepción de 10 a 20 Mbps | CD Talca y CD Concepción | 2 | Dimensionado sobre la replicación de la base, el vuelco de los brokers y la telemetría, de unos 0,2 Mbps en promedio, y sobre el respaldo semanal a la nube, de 40 a 120 GB en la ventana nocturna, unos 33 Mbps (RT-03.20; Bases Técnicas Transversales, Cap. 3, p. 9); los valores cubren el crecimiento de 3 veces sin rediseño (RT-09.03; Bases Técnicas Transversales, Cap. 9, p. 21). |
| D-04 — Enlace LTE | LTE empresarial con SIM dedicada: Talca de 5 a 10 Mbps, Concepción de 3 a 5 Mbps y cross-docking de 2 a 5 Mbps con dos proveedores | Talca 1, Concepción 1 y 2 por cross-docking | 8 planes | Evita depender de un solo camino o proveedor (RT-03.17; Bases Técnicas Transversales, Cap. 3, p. 9), con conmutación en menos de 30 s: en los centros de distribución respalda a la fibra y en los cross-docking respalda a Starlink con dos proveedores distintos. |
| D-01 — Firewall y Customer Gateway (túneles VPN) | AWS Site-to-Site VPN IPsec IKEv2 con BGP sobre Transit Gateway | Talca, Concepción y los tres cross-docking hacia sa-east-1, y hacia us-east-1 en la conmutación de región | 2 túneles por sitio | Replica la base, sincroniza los brokers y transmite telemetría cifrado y con enrutamiento dinámico (RT-03.21; Bases Técnicas Transversales, Cap. 3, p. 9), con una MTU de túnel de 1.436 bytes. |
| D-01 — Firewall y Customer Gateway (Concepción) | Par activo/pasivo de firewalls de borde de grado empresarial con sincronización de sesiones | CD Concepción, gabinete de borde | 2 (reserva compartida con Talca) | Concepción es el sitio de recuperación on-premise y RT-08.03 (Bases Técnicas Transversales, Cap. 8, p. 18) no admite cortafuegos en punto único de falla: la unidad pasiva asume el túnel hacia AWS y la conmutación entre fibra y LTE en menos de 30 s (RT-03.17; Bases Técnicas Transversales, Cap. 3, p. 9), con cada unidad en un circuito eléctrico distinto (RT-08.04; Bases Técnicas Transversales, Cap. 8, p. 18). |
| D-02 — Switching (núcleo de Concepción) | Cisco Catalyst 9300 o equivalente en stack, con doble fuente | CD Concepción, gabinete de borde | 2 (reserva compartida con Talca) | Los dos equipos forman un único plano de distribución, de modo que la falla de uno no detiene la red de bodega del sitio de recuperación (RT-08.03; Bases Técnicas Transversales, Cap. 8, p. 18), y cada uno tiene doble fuente (RT-08.04; Bases Técnicas Transversales, Cap. 8, p. 18). |
| D-02 — Switching de acceso (bodegas) | Cisco Catalyst 9200-24P o equivalente, con PoE+ y enlace de fibra al núcleo | Gabinetes de piso de las bodegas: Talca 4 y Concepción 2; reserva en Talca | 6 + 1 de reserva = 7 | El cableado de cobre no supera 100 m: los puntos de acceso, impresoras y balanzas alejados de la sala se conectan a un gabinete de piso cercano, que sube por fibra al núcleo del sitio; su cantidad sigue a la de puntos de acceso (S-36). |
| D-02 — Switching (cross-docking) | Netgear GS308E o equivalente, de 8 puertos Gigabit gestionables | Curicó, Chillán y Los Ángeles; reserva en Talca | 3 + 1 de reserva = 4 | Equipo compacto para una nave sin sala técnica: conecta el mini-PC, los dos firewalls y los puntos de acceso. Fuente externa única: punto único de falla aceptado (RT-02.11; Bases Técnicas Transversales, Cap. 2, p. 7), con la unidad de reserva en Talca, que viaja en el camión de línea nocturno (Bases Técnicas del caso, Cap. 3, p. 6). |
| D-01 — Firewall y Customer Gateway (cross-docking) | Par de firewalls compactos de grado empresarial en alta disponibilidad, con IPsec IKEv2, BGP y módem LTE Cat-12 de doble SIM | Curicó, Chillán y Los Ángeles, 2 por plataforma; reserva en Talca | 6 + 1 de reserva = 7 | Es el Customer Gateway del sitio: termina Starlink como enlace principal y LTE de dos proveedores como respaldo, conmuta en menos de 30 s (RT-03.17; Bases Técnicas Transversales, Cap. 3, p. 9) y evita exponer el sitio o Talca a Internet (Bases Administrativas, Art. 21, p. 15). Se instala en par porque RT-08.03 (Bases Técnicas Transversales, Cap. 8, p. 18) no admite cortafuegos en punto único de falla. |
| Dispositivos de terreno y de operación |  |  |  |  |
| C-01 — App de preventa (terminal) | Zebra EC55: Android, IP67, uso con guantes y lector 2D SE4100; accesorios: cargador y funda con correa de mano | Uno por preventista | 62 + 7 de reserva = 69 | Opera sin señal, dura la jornada con una carga, funciona con guantes y su pantalla se lee a pleno sol (RT-08.11; Bases Técnicas Transversales, Cap. 8, p. 19); la reserva es el 10 % del parque. |
| C-02 — App de reparto (terminal) | Zebra TC58e: 5G, lector SE55, batería de 7.000 mAh, GPS L1/L5, IP65/68 y -30 °C; accesorios: soporte y cargador de vehículo | Uno por camión: 42 propios y 54 de transportistas | 96 + 10 de reserva = 106 | Se asigna al camión y no al conductor, porque los conductores de terceros rotan sin aviso (S-30); un solo modelo para conductores propios y externos: mismo repuesto, misma capacitación y misma integración. |
| Impresora de cabina | Zebra ZQ620 Plus: 3 pulgadas, ZPL, IP54 y Link-OS; accesorios: batería de reemplazo y soporte de vehículo; consumible: rollo térmico | Una por camión | 96 + 10 de reserva = 106 | Imprime la evidencia de entrega y los comprobantes en la cabina; se asigna al camión (S-30). |
| Terminal de pago | PAX A920 Pro: Android 14, PCI PTS 7.x y EMV L1/L2; accesorio: base de carga | Uno por camión | 96 + 10 de reserva = 106 | Cobra con tarjeta en el local del cliente con certificación PCI PTS y EMV, integrado por Bluetooth con la aplicación de reparto; se asigna al camión (S-30). |
| C-03 — Terminales de bodega (congelado) | Zebra MC9400 Cold Storage Freezer: -30 °C, lector SE58 de 100 pies, batería de 5.000 mAh y Wi-Fi 6E; accesorios: batería de repuesto por equipo y cargador de baterías | CD Talca, cuadrilla de congelado | 20 + 2 de reserva = 22 | Prepara pedidos en la cámara a -22 °C con guantes gruesos, lee a distancia y recambia la batería en caliente (RT-08.11, Bases Técnicas Transversales, Cap. 8, p. 19; RT-08.12, Bases Técnicas Transversales, Cap. 8, p. 19; RT-13.08, Bases Técnicas del caso, Cap. 15, p. 27); lo usa solo la cuadrilla que entra al congelado, cuyo tamaño sigue a la participación del congelado en las líneas (S-34). |
| C-03 — Terminales de bodega (estándar) | Zebra MC9400 estándar: lector SE58, batería de 5.000 mAh y Wi-Fi 6E; accesorio: cuna de carga de cinco posiciones | Talca 100, Concepción 60 y cross-docking 6 (2 por plataforma) | 166 + 17 de reserva = 183 | Atiende la bodega seca, la cámara de refrigerado sobre 0 °C y la desconsolidación de los cross-docking; se comparte entre turnos (RT-12.11; Bases Técnicas del caso, Cap. 15, p. 27), por lo que lo dimensiona el turno con más personas a la vez: 120 preparadores en Talca, 60 en Concepción (S-39) y 2 por cross-docking (S-35), sin personal de carga adicional (S-33). |
| C-04 — Impresoras de andén | Zebra ZT411: 203 dpi, 14 ips, Ethernet y ZPL; consumibles: etiquetas de 4 × 6 pulgadas y cinta de transferencia térmica | Talca 4 y Concepción 2; reserva en Talca | 6 + 1 de reserva = 7 | Imprime la etiqueta SSCC GS1-128 al armar la unidad logística (RF-01.07), legible a lo largo de toda la cadena (RT-05.23; Bases Técnicas Transversales, Cap. 5, p. 13; Bases Técnicas del caso, Cap. 15, p. 26). |
| C-05 — Balanzas de recepción | Dibal BEV con plataforma ME e indicador DMI-610 inoxidable, RS-232 y Ethernet; accesorio: rampa de acceso para transpaleta | Talca 2 y Concepción 1; reserva en Talca | 3 + 1 de reserva = 4 | Captura el peso de recepción en línea hacia el WMS (RF-01.01), sin digitación, con calibración certificada. |
| B-01 — Sensores de temperatura | Módulo Ebyte ME31-XDXX0400: 4 canales PT100, Modbus RTU/TCP, de -40 a +85 °C, con sondas de 3 hilos; accesorios: fuente de 24 VDC y caja IP65 | Cámaras de Talca (15 puntos) y Concepción (6 puntos) | 6 + 1 de reserva = 7 módulos; 21 + 3 de reserva = 24 sondas | Alimenta el registro continuo de la cadena de frío, con una exactitud de ±1,1 °C a -22 °C que distingue una excursión real de la variación del instrumento; los puntos se distribuyen por superficie de cámara y junto a cada puerta, y la cámara de Concepción se estima en unos 450 m² (S-37). |
| B-03 — Termógrafos de camión | Onset InTemp CX450: Bluetooth, de -30 a +70 °C con ±0,5 °C y calibración NIST en dos puntos; accesorio: soporte de montaje en la caja de frío; consumible: batería reemplazable | Camiones con equipo de frío: 18 propios y 10 de transportistas | 28 + 3 de reserva = 31 | Registra la temperatura del transporte de forma independiente y sin conexión durante toda la ruta; alerta la excursión térmica en el terminal del conductor y, al volver, descarga el registro completo por Bluetooth a ese terminal, que lo envía a la nube. Los 10 camiones refrigerados de los transportistas se instrumentan con el mismo equipo, con el acuerdo de cada transportista (S-28); la flota con frío no crece en el horizonte de cotización (S-38). |
| Estación de trabajo | Ocho PC nuevas; equipos existentes de oficina con CrowdStrike Falcon, cifrado de disco, parches y control de extraíbles | Talca 5 y Concepción 3; oficinas de Talca y Concepción | 8 nuevas; 184 existentes gestionadas (S-41) | Puestos de despacho, administración, planificación, calidad y TI, con dos monitores de 24 pulgadas, ergonomía NCh 2527 y certificación de eficiencia energética; la postura gestionada habilita Verified Access (RT-08.07–08.09; Bases Técnicas Transversales, Cap. 8, p. 19). |
| D-06 — Enlace satelital | Starlink Enterprise fijo, antena en techumbre y router, plan de 500 GB al mes durante los 56 meses del contrato | Curicó, Chillán y Los Ángeles | 3 | Es el enlace principal de los cross-docking, que no tienen fibra, con LTE como respaldo automático (RT-03.17, Bases Técnicas Transversales, Cap. 3, p. 9; RT-08.13, Bases Técnicas Transversales, Cap. 8, p. 19); reposición de hardware estimada en 15 % durante el contrato. |
| B-02 — Gateway IoT | Gateway industrial con Linux, Moxa UC-8200 (Moxa Industrial Linux 3, Debian 11) o equivalente listado en el AWS Partner Device Catalog, con AWS IoT Greengrass V2, 2 puertos Gigabit Ethernet, 2 puertos serie RS-232/422/485, doble entrada de alimentación redundante de 12 a 48 VDC y operación de -40 a 85 °C; accesorios: dos fuentes de 24 VDC y montaje en riel DIN | Talca 2 y Concepción 1; reserva en Talca | 3 + 1 de reserva = 4 | Lee los módulos de temperatura por Modbus, detecta la excursión térmica y bloquea el despacho en el borde, con un buffer local de 24 h si cae el enlace. En Talca los dos gateways leen ambas cámaras por Modbus TCP, de modo que la falla de uno no detiene el bloqueo de despacho (RT-03.14; Bases Técnicas Transversales, Cap. 3, p. 9). |
| Infraestructura de la sala técnica de Talca |  |  |  |  |
| UPS | Modular de 10 kVA, doble conversión en línea, en N+1 y con bypass de mantenimiento | Zona de UPS y baterías (plano RT-06.03; Bases Técnicas Transversales, Cap. 6, p. 14) | 1 | Dimensionado sobre la carga TI de diseño de 7,0 kW y ≈ 7,4 kVA aparentes (factor de potencia 0,95), al 80 % de utilización, ≈ 9,2 kVA (RT-06.11; Bases Técnicas Transversales, Cap. 6, p. 15); autonomía de 30 min o más a plena carga (RT-06.07; Bases Técnicas Transversales, Cap. 6, p. 15). |
| Generador | Grupo electrógeno de 15 kVA con estanque para 24 h continuas y contrato de reabastecimiento declarado | Exterior, junto a la acometida (zona de generadores del plano RT-06.03; Bases Técnicas Transversales, Cap. 6, p. 14) | 1 | Sostiene la carga total del sitio, ≈ 10,4 kW entre TI, climatización y apoyo, durante 24 h o más (RT-06.08; Bases Técnicas Transversales, Cap. 6, p. 15). |
| Transferencia automática | Transferencia red-generador con tablero de protecciones | Acometida, accesible desde el exterior | 1 | Encadena empalme, tablero, transferencia, UPS, PDU y equipo sin interrupción (RT-06.07; Bases Técnicas Transversales, Cap. 6, p. 15); se prueba cada mes con carga real y admite termografía (RT-06.10; Bases Técnicas Transversales, Cap. 6, p. 15). |
| Climatización | 2 unidades de precisión de 10 kW (≈ 34.000 BTU/h) en N+1 | Zona de climatización, contigua a la sala de servidores y comunicaciones | 2 | Cubren la carga térmica sensible de diseño, ≈ 7,6 kW, aun con la pérdida de una unidad, dentro de los rangos del fabricante (RT-06.13, RT-06.11; Bases Técnicas Transversales, Cap. 6, p. 15). |
| Distribución eléctrica | 2 PDU verticales A/B por gabinete, con medidor | Racks R01 y R02 | 4 | Dos caminos eléctricos por gabinete (RT-08.04; Bases Técnicas Transversales, Cap. 8, p. 18); el medidor es el denominador de la PUE (RT-06.10, Bases Técnicas Transversales, Cap. 6, p. 15; RT-15.04, Bases Técnicas Transversales, Cap. 15, p. 27). |
| Detección de incendio | Detección temprana por aspiración con tecnología láser, tipo AnaLASER o equivalente | Sala de servidores y comunicaciones | 1 | Detecta antes de que exista llama visible (RT-06.16; Bases Técnicas Transversales, Cap. 6, p. 15) e integra el monitoreo en línea (RT-06.19; Bases Técnicas Transversales, Cap. 6, p. 16). |
| Extinción | Agente limpio tipo FM-200 o equivalente, con aprobación UL, botón de aborto y extintores portátiles habilitados | Sala de servidores y comunicaciones | 1 | Extinción automática sobre equipos energizados (RT-06.17; Bases Técnicas Transversales, Cap. 6, p. 15) y extintores con mantención vigente (RT-06.18; Bases Técnicas Transversales, Cap. 6, p. 15). |
| Control de acceso | Biometría facial con AFIS como respaldo, esclusa antipassback con nueva verificación, bitácora electrónica y estación de enrolamiento interna y externa | Acceso del recinto técnico | 1 | RT-06.20 (Bases Técnicas Transversales, Cap. 6, p. 16) a RT-06.23 (Bases Técnicas Transversales, Cap. 6, p. 16); bitácora auditable conservada 5 años o más (RT-06.21, Bases Técnicas Transversales, Cap. 6, p. 16; RT-16.10, Bases Técnicas Transversales, Cap. 16, p. 29). |
| Videovigilancia | Cámaras IP con imágenes en línea de 30 días o más y respaldo recuperable | Acceso principal, pasillo de control, esclusa, sala de servidores y comunicaciones, zona de UPS y baterías, y exterior | 6 | Cubre cada zona del plano del recinto y su perímetro, integrada al monitoreo (RT-06.24; Bases Técnicas Transversales, Cap. 6, p. 16). |
| Recinto de custodia | Recinto con iluminación sin UV de hasta 300 lux, 40 a 60 % HR, ventilación forzada y 18 a 27 °C | Área de respaldo del recinto (plano RT-06.03; Bases Técnicas Transversales, Cap. 6, p. 14) | 1 | Conserva los medios de respaldo sin degradarlos (RT-06.26, RT-06.27; Bases Técnicas Transversales, Cap. 6, p. 16). |
| Gabinetes | R01 servidores (3 nodos 2U en U18–U23, NAS 2U en U1–U2, KVM 1U en U24, paneles OM4/Cat6A en U40–U42) y R02 comunicaciones (bandeja del operador con ONT de fibra y router LTE, 2U en U31–U32; 2 firewalls 1U en U33–U34; switch de gestión 1U en U35; organizadores 1U en U36 y U39; 2 conmutadores de núcleo 1U en U37–U38; ODF y paneles en U40–U42), 42U | Sala de servidores y comunicaciones | 2 | Racks de servidores independientes de los racks de comunicaciones (RT-06.05; Bases Técnicas Transversales, Cap. 6, p. 15); ocupación proyectada R01 y R02 de 12U/42U (29 %) cada uno, con 30U libres por rack para el margen de crecimiento a tres años, coherente con la reserva eléctrica del 20 % de la Tabla 4.3-1. |
| Piso técnico y cableado | Cableado Cat6A y fibra OM4 certificados por enlace, sobre piso técnico | Sala | 1 | Cumple la norma por enlace (RT-06.04; Bases Técnicas Transversales, Cap. 6, p. 14) con recorridos verificados para 10 GbE. |
| Gabinetes de borde |  |  |  |  |
| Gabinete de borde de Concepción | Gabinete industrializado con alimentación protegida (UPS y respaldo) para la autonomía declarada | CD Concepción | 1 | Sitio de recuperación del dominio on-premise, a ≈ 200 km de Talca en línea recta y 250 km por carretera (RT-07.02; Bases Técnicas Transversales, Cap. 7, p. 17); opera de forma autónoma todos los días (RT-06.01 del caso; numeral 6.1 de las Bases Técnicas Transversales (Cap. 6, p. 14); Bases Técnicas del caso, Cap. 15, p. 26). |
| Climatización del borde | Climatización de precisión acorde al equipamiento del borde | CD Concepción, gabinete de borde | 1 | Dimensionada al equipamiento real del borde, conforme a la tipología del numeral 6.1 de las Bases Técnicas Transversales (Cap. 6, p. 14). |
| Control de acceso y monitoreo del borde | Acceso controlado y monitoreo remoto integrado al NOC | CD Concepción, gabinete de borde | 1 | Aplica la tipología de borde operacional del numeral 6.1 de las Bases Técnicas Transversales (Cap. 6, p. 14) con supervisión remota del sitio. |
| Gabinete de borde de cross-docking | Gabinete de 12U con UPS interna de 30 min o más, cerradura biométrica con registro, sensores de temperatura, humedad y apertura enviados al NOC, y ventilación forzada | Curicó, Chillán y Los Ángeles | 3 | Cumple en cada plataforma los requisitos del gabinete de borde del numeral 6.1 de las Bases Técnicas Transversales (Cap. 6, p. 14): protección eléctrica, control de acceso físico, monitoreo remoto y condiciones ambientales del equipo. |
| Plataforma de nube y servicios gestionados |  |  |  |  |
| N-01 a N-03 — Portales | S3 privado, CloudFront, AWS WAF y API REST pública | sa-east-1, borde público | 1 aplicación para 3 portales | Publica los portales de clientes, transportistas y proveedores sin exponer los sitios del CLIENTE (RT-03.04; Bases Técnicas Transversales, Cap. 3, p. 8). |
| API Gateway | Dos API REST, regional pública y privada, endpoint de interfaz execute-api y autorizador Lambda | Borde y VPC de Producción | 2 API REST; 1 función Lambda | WAF, modelos, cuotas, límites de tasa y VPC Link al ALB privado; acceso público solo por CloudFront (ADR-13). |
| AWS Verified Access | Confianza OIDC Keycloak y postura CrowdStrike Falcon; AWS WAF de instancia | Acceso de oficina y remoto | 1 instancia | Controla por aplicación las consolas y la administración de Keycloak con MFA y postura (ADR-16). |
| N-04 — Plataforma de aplicación | ECS Fargate, Application Load Balancer, Elastic Container Registry y CodeBuild | sa-east-1 en 2 zonas; réplica reducida en us-east-1 | API: 2 a 4 tareas, techo 8; consumidor: 2 a 4; trabajos: 2 a 4; planificador: 1 | Ejecuta los perfiles del monolito Laravel en tareas de 1 vCPU y 2 GB, cada uno con su escalado, su rol de IAM y sus métricas; el número de tareas es una estimación que confirma la prueba de carga (ADR-01, ADR-12). |
| N-04 — Frontend de consolas | Angular en ECS Fargate tras ALB privado | VPC de Producción | 1 frontend | Sirve las consolas y reenvía sus llamadas a la API REST privada por execute-api (ADR-16). |
| N-04 — Motor de optimización de rutas | Contenedor propio en ECS Fargate, tras un contrato versionado con M4 | sa-east-1 | 1 tarea por corrida, bajo demanda | Calcula la secuencia de rutas de M4 fuera del artefacto PHP; el motor se selecciona por la prueba de rutas en menos de 20 minutos, que es condición de aceptación (ADR-01). |
| N-04 — Transporte AS2 | OpenAS2 BSD en ECS Fargate tras Network Load Balancer con paso TLS directo | sa-east-1 | 1 transporte AS2; 1 acuerdo por cadena | TLS 1.3 en el contenedor, IP registradas, firma, cifrado, certificados por cadena y MDN; prueba de interoperabilidad por cadena (ADR-11). |
| N-05 — Base de datos en nube | Aurora PostgreSQL con Aurora Global Database y AWS DMS | sa-east-1 y us-east-1 | 1 clúster | Transaccional de los módulos en nube y réplica de lectura del WMS, separada del estado central que actualizan los eventos; conmuta entre zonas en menos de 30 s, con RPO de 15 min, que para la réplica del WMS rige mientras hay enlace (ADR-04, ADR-09). |
| N-06 — Telemetría cruda | DynamoDB bajo demanda; Global Tables solo para temperatura, y la tabla de posiciones de flota solo en sa-east-1 | sa-east-1 y us-east-1 | 1 tabla por serie | Recibe las lecturas de IoT sin gestión de capacidad y las expira a los 30 días (ADR-04). |
| N-07 — Caché | ElastiCache for Redis con primario y réplica | sa-east-1 en 2 zonas | 1 clúster | Responde la consulta de stock y crédito de preventa en menos de 2 s. |
| N-08 — Ingesta de IoT | IoT Core con su motor de reglas e IoT Greengrass | sa-east-1 y gateways de borde | 3 gateways y 28 termógrafos | Recibe, valida y alerta la telemetría de cadena de frío, y gestiona la flota de gateways. |
| N-09 — Mensajería | SQS FIFO de reconciliación con su cola de mensajes fallidos; colas SQS de trabajos de Laravel; SNS | sa-east-1 | 1 cola FIFO con grupos por sitio y agregado; 3 colas de trabajos (notificaciones, `erp-sync` y EDI), cada una con su cola de fallidos | Reconcilia los sobres JSON de los sitios en orden por grupo y sin duplicados, separa los trabajos internos del formato externo y difunde las alertas de frío (ADR-05). |
| N-10 — Plataforma analítica | S3, Glue, Redshift Serverless y QuickSight embebido | sa-east-1 | 1 lago de 5 años | Lectura y autoría con permisos separados en consolas; los indicadores actuales usan la API de negocio. |
| N-11 — Respaldo inmutable y réplica | AWS Backup con Vault Lock, S3 Object Lock y replicación de S3 entre regiones | sa-east-1 y us-east-1 | 1 política | Mantiene la copia inmutable del esquema 3-2-1-1-0 y la réplica de recuperación (ADR-09). La frecuencia, la retención y el tiempo de restauración por dominio de datos (RT-07.13; Bases Técnicas Transversales, Cap. 7, p. 18) son los de la tabla de respaldo y restauración por dominio de datos del Subdocumento 4 (apartado 4.2.4). |
| N-12 — Seguridad y gobierno | KMS, Secrets Manager, Parameter Store, IAM Identity Center, Shield Advanced, GuardDuty, Security Hub, Inspector, Macie, Security Lake, CloudTrail, Config, CloudWatch, Systems Manager, Control Tower, Organizations, Cost Explorer y Budgets | sa-east-1; claves, secretos, CloudTrail, GuardDuty y Config también en us-east-1 | 8 cuentas: 5 ambientes, gestión, archivo de registros y auditoría | Implementa en la nube los controles del Artículo 21 de las Bases Administrativas (p. 15) definidos en la arquitectura de seguridad (apartado 4.1) y el gobierno de costos, como servicios administrados (ADR-14, ADR-15). |
| D-01 — Firewall y Customer Gateway (parte en nube) | VPC, Transit Gateway, Site-to-Site VPN, NAT Gateway, VPC Endpoints y Route 53 | sa-east-1 y us-east-1 | 2 túneles por sitio | Conecta los sitios con la nube por túneles cifrados, sin exponer el tráfico en claro en Internet (RT-03.03, RT-03.04; Bases Técnicas Transversales, Cap. 3, p. 8). |
| N-13 — Gestión de dispositivos | Android Enterprise y Zebra DNA como servicio gestionado | Servicio en nube y agente en el dispositivo | 380 equipos: 69 EC55, 106 TC58e y 205 MC9400, incluida la reserva, que se deja configurada de antemano (Bases Técnicas Transversales, Cap. 8, p. 19) | Enrola, configura, actualiza y borra de forma selectiva el parque de terreno y de bodega (RT-03.18; Bases Técnicas Transversales, Cap. 3, p. 9). |
| F-03 — Detección en endpoints | CrowdStrike Falcon, consola EDR y agente de postura | Servicio en nube; agente en los 7 equipos físicos (3 nodos de Talca, servidor de Concepción y 3 mini-PC), las 10 máquinas virtuales y las estaciones | 17 servidores + 8 estaciones nuevas + 184 existentes (S-41) = 209 | Detecta y responde; verifica la postura de los equipos que acceden por Verified Access (RT-11.16; Bases Técnicas Transversales, Cap. 11, p. 24). |
| Dependencias de salida | MDM, EDR, SII, Transbank, GIS, notificaciones y telemetría de flota | Conexiones salientes de la solución | 7 dependencias | Integraciones externas sin entrada a la VPC de Producción (superficie de exposición, apartado 4.2.5). |
| Software de base y licenciamiento |  |  |  |  |
| Aplicación | Monolito modular en Laravel 13 sobre PHP 8.5, con PHP-FPM y PHP CLI, dependencias fijadas por `composer.lock` y las extensiones `pdo_pgsql`, `mbstring`, `intl`, `openssl`, `opcache`, `curl`, `sockets`, `pcntl` y OpenTelemetry; código abierto | Nube, VM-01, VM-C01, VM-03, VM-C04 y E-01 | 1 imagen firmada | Una sola base de código y de esquema para nube y sitios, ejecutada en perfiles de API, `wms_only`, shipper, consumidor, trabajos y planificador (ADR-01). |
| Aplicación de terreno | Aplicación nativa Android en Kotlin, con SQLite y Zebra DataWedge | EC55, TC58e y MC9400 | 1 artefacto para 3 perfiles | Controla los periféricos industriales y opera un turno completo sin señal (ADR-07). |
| Portales web y consolas | Angular con TypeScript y Tailwind CSS, código abierto | Portales en S3 y CloudFront; consolas en Fargate | 3 portales y consolas | Comparte componentes y contratos TypeScript; las consolas se sirven tras ALB privado. |
| A-02 — Base transaccional del WMS | PostgreSQL 16 con PostGIS, código abierto | VM-02, VM-C02 y los tres E-01 | 5 instancias | Registro local de cada bodega durante los cortes. Solo VM-02 (Talca) se replica a Aurora por DMS; Concepción y los cross-docking sincronizan eventos por los flujos de integración de 4.2.5. |
| A-03 — Broker de colas | RabbitMQ, código abierto, con el adaptador AMQP `php-amqplib` | VM-03, VM-C04 y los tres E-01 | 5 instancias | Buffer de 24 h por sitio con mensajes persistentes y confirmación de publicación; el shipper vacía el buffer hacia SQS FIFO como sobres JSON (ADR-05). |
| A-05 — Identidad | Keycloak, código abierto, con verificador local de relevo de turno | Fargate, VM-05, VM-C03 y los tres E-01 | 1 maestro, 5 cachés y 5 verificadores | Autoridad única en nube con cachés de solo lectura; el verificador local valida el manifiesto de turno firmado y el segundo factor local, el PIN personal, en los relevos sin enlace (ADR-06). |
| Virtualización | Proxmox VE con Ceph, código abierto | Clúster de Talca y servidor de Concepción | 1 clúster de 3 nodos y 1 nodo | Tolera la pérdida de un nodo sin detener la bodega. |
| Contenedores en los sitios | Docker y Docker Compose, código abierto | Máquinas virtuales de Talca y Concepción y los tres cross-docking | 5 sitios | Ejecutan la misma imagen de la aplicación que la nube; en los cross-docking orquestan además la base, el broker y la caché de identidad, con instalación y parcheo sin dependencia de la red. |
| F-01 — Telemetría de observabilidad | AWS Distro for OpenTelemetry y agente SSM | VM-06, VM-C04 y los tres E-01 | 5 colectores | Reciben las trazas y métricas de OpenTelemetry para PHP y las guardan hasta 24 h antes de enviarlas a CloudWatch al reconectar (ADR-14). |
| Configuración | Ansible y Terraform con CDK, código abierto | Repositorio del CLIENTE | 1 repositorio | Infraestructura y configuración declaradas como código versionado. |
| Integración y entrega continuas | GitLab CI como orquestador y AWS CodeBuild para la construcción | Pipeline del repositorio del CLIENTE; construcción en sa-east-1 | 1 pipeline | Instala las dependencias desde `composer.lock`, ejecuta `composer audit`, PHPUnit, PHPStan/Larastan, Pint y las pruebas de contrato OpenAPI y AsyncAPI, escanea con bloqueo automático (RT-04.05; Bases Técnicas Transversales, Cap. 4, p. 10) y construye y firma cada imagen de forma hermética, con procedencia SLSA nivel 3. |

La tabla vincula el equipamiento de sitio con los servicios de nube y los controles de acceso del catálogo de emplazamiento.


**Metadatos de portada**

- Documento: Propuesta Técnica
- Subtítulo: Anexo 4.B — Memoria de cálculo del dimensionamiento
- Alcance: Subdocumento 4 — Anexos
- Formulario: Anexo 4.B
- Fecha: 05 de octubre de 2026
- Versión: 2.0

# Anexo 4.B. Memoria de cálculo del dimensionamiento

<a id="sec:anexo-4b-entradas"></a>
## 4.B.1 Entradas, requisitos, parámetros y supuestos

Este anexo sustenta el dimensionamiento del apartado 4.2.6 y entrega la memoria de cálculo que respalda el Formulario T-11. Su alcance comprende las dieciséis dimensiones, la capacidad por sitio, la nube, los enlaces, la migración, el crecimiento y las pruebas de aceptación. Los supuestos de volumen, concurrencia y crecimiento que exige el Formulario T-7 (SV-01 a SV-07) se declaran en este anexo; los que fijan las cantidades de implementos (S-28 y S-30 a S-41) se registran en el Subdocumento 3.

La Tabla [29](#tab:anexo-4b-hechos) concentra los hechos que alimentan las fórmulas y conserva su cita en la forma de la propuesta.

<a id="tab:anexo-4b-hechos"></a>
**Tabla 29.** Hechos del caso utilizados
| Dato | Valor | Fuente |
| — | — | — |
| Volumetría comercial | 31.000 pedidos; 260.000 líneas; 2,4 millones de unidades mensuales | Bases Técnicas del caso, Cap. 2, p. 4 |
| Entregas | ≈ 1.400 normales y ≈ 2.600 en septiembre | Bases Técnicas del caso, Cap. 14, p. 24 |
| Documentos tributarios electrónicos (DTE) y transporte | ≈ 34.000 documentos tributarios electrónicos, ≈ 2.100 viajes de camión y ≈ 420.000 km recorridos al mes | Bases Técnicas del caso, Cap. 14, p. 24 |
| Operación de terreno | 62 preventistas; 42 camiones propios; 54 de terceros; 184 personas de administración, comercial y soporte | Bases Técnicas del caso, Cap. 2, p. 5 |
| Bodegas | 120 personas nocturnas en Talca; 18.000 m² y 9.000 m² | Bases Técnicas del caso, Cap. 8, p. 14, entrevista; Bases Técnicas del caso, Cap. 2, p. 5 |
| Ventanas | Preparación 22:00–06:00; despacho 05:30–07:00; sincronización 17:00–20:00 | Bases Técnicas del caso, Anexo B, p. 38 |
| Ruta y frío | 34 clientes en una ruta máximo actualmente; 18 camiones propios y 10 de terceros con equipo de frío; Talca a {-}22 °C | Bases Técnicas del caso, Cap. 8, p. 16, entrevista al conductor; Bases Técnicas del caso, Cap. 2, p. 5 |

La Tabla [30](#tab:anexo-4b-parametros) fija los valores que impone la propuesta. Un valor de diseño se confirma mediante perfilado, QA o prueba de carga, pero no se presenta como un hecho del CLIENTE.

<a id="tab:anexo-4b-parametros"></a>
**Tabla 30.** Parámetros de diseño
| Parámetro | Valor | Justificación y uso | Confirmación |
| — | — | — | — |
| Operaciones de flujo | 2 por línea: lectura de ubicación o lote y confirmación; 5 por entrega: estado, evidencia, documento, cobro y cierre; 4 por cross-docking: recepción, escaneo, desconsolidación y despacho | Flujo del apartado 4.1 | RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21) |
| Preventa | 2 consultas por visita y 1 operación por línea | Stock, crédito y pedido | Contrato y carga |
| Concentración horaria | SV-04 = 2,0, sólo en la hora cargada | Frío, despacho, reparto y sincronización | Perfil de 24 h |
| Portal | 60 solicitudes por sesión de 10 minutos; sensibilidad de 120 por sesión | Cota de sesiones; las sesiones se reparten en la hora y 15 minutos sólo determinan concurrencia | RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21) |
| Registro y movimiento | 1 KB; 0,5 KB | Almacenamiento y base local; sensibilidad ±50 % | QA |
| Base local | 4 meses más maestros y lotes presentes | Ciclo de conteo y conciliación | Levantamiento WMS |
| Evidencia | 30 KB de firma; 200 KB de foto; una adicional en devolución | Compresión en App de reparto | QA |
| Plataforma | 50 ms de CPU por solicitud; 64 MB por proceso; 150 ms de permanencia | Capacidad de VM y nube; se perfila y verifica en la prueba de carga | RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21) y Bases Técnicas Transversales, Cap. 9, p. 21 |
| Observabilidad | 250 MB y 1.000 eventos por nodo/día | ADOT: registros, métricas y trazas | Operación |
| Actualizaciones | App ≤100 MB; sistema operativo 2 GB | Tandas dominicales sin bodega ni reparto | Anexo B.2 |

La Tabla [31](#tab:anexo-4b-supuestos) declara el fundamento, impacto y validación de cada supuesto. Ninguno reemplaza un dato literal del caso.

<a id="tab:anexo-4b-supuestos"></a>
**Tabla 31.** Supuestos de volumen
| Código | Qué suponemos y por qué | Si resulta equivocado | Cómo y cuándo se valida |
| — | — | — | — |
| SV-01 | Un pedido genera una entrega; 31.000/1.400 produce 22,14 días y concuerda con 2.100/96. | Cambian evidencia, mensajes y almacenamiento. | Conciliación ERP–guías–entregas en Etapa 1. |
| SV-02 | Septiembre escala los flujos de volumen y diciembre no supera su exigencia; el factor 1,857 es cálculo. | Falta capacidad en el nuevo peak. | Serie mensual antes del congelamiento. |
| SV-03 | Talca prepara 2/3 y Concepción 1/3 por superficies y función de abastecimiento adicional. | Faltan terminales, WMS o enlace en el centro subestimado. | Exportación WMS por centro. |
| SV-04 | La hora cargada duplica la media de su propia ventana, una sola vez. | El cuello se traslada a WMS, ERP, Wi-Fi o nube. | Perfil horario y RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21). |
| SV-05 | La cadena principal no supera 11 % de los pedidos en el escenario EDI 2029; el caso informa que pesa 11 % de la venta, y como sus pedidos son mayores que el promedio, tomar 11 % de los pedidos es una cota holgada. | Aumentan colas EDI. | Contrato y certificación del intercambio. |
| SV-06 | 2,5 contactos por persona/mes, 10 minutos y 25 % en hora cargada. | Se requieren más personas. | Tickets y Erlang C mensual. |
| SV-07 | La API de telemetría de los camiones propios continúa disponible. | Posición automática se degrada a ruta planificada. | Prueba contractual y técnica. |

<a id="sec:anexo-4b-dimensiones-1-3"></a>
## 4.B.2 Dimensiones 1–3: transacciones por segundo

Se calcula el máximo horario de cada lugar para no sumar ventanas que no coinciden. Los días equivalentes son 31.000 ÷ 1.400 = 22,14 días y el control cruzado es 2.100 ÷ 96 = 21,88 días. El factor de septiembre es 2.600 ÷ 1.400 = 1,857.

La preparación normal de Talca se calcula como 11.742 líneas por noche × 2 operaciones × 2/3 ÷ 28.800 segundos = 0,54 TPS de media; la hora cargada de SV-04 alcanza 1,09 TPS. A las 05:00 el despacho local agrega su flujo y el máximo horario del WMS de Talca es 1,64 TPS normal y 3,02 TPS en septiembre.

La nube suma preventa, reparto, recepción, trazabilidad, guías, sincronización y el escenario EDI. El portal queda separado: 2.600 ÷ 9 × 2 por SV-04 = 578 sesiones en la hora cargada; 578 × 60 ÷ 3.600 = 9,63 solicitudes/s y 578 × 10 ÷ 60 = 96,30 concurrentes. La cota extrema es 2.600 × 60 ÷ 3.600 = 43,33 solicitudes/s y 433,33 concurrentes. Las 2.600 sesiones diarias del portal son un parámetro de diseño: se toma una sesión por cada cliente de food service y de cadenas, 2.100 + 500 = 2.600 (Bases Técnicas del caso, Cap. 2, p. 4). No son las 2.600 visitas diarias de preventa (Bases Técnicas del caso, Anexo B, p. 38); que las dos cifras coincidan es casualidad.

La dimensión 1 es **12,30 TPS a las 12:00** en régimen normal. La dimensión 2 es **1,68 TPS normal y 3,05 TPS peak** en la cota de despacho con guías. La dimensión 3 es **14,66 TPS a las 12:00** en septiembre. RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21) es 1,5 × 14,66 = **21,99 TPS**.

La Tabla [32](#tab:anexo-4b-horario) conserva el perfil hora por hora que produce esos máximos.

<a id="tab:anexo-4b-horario"></a>
**Tabla 32.** Perfil horario por lugar de proceso
| Hora | Talca N/P | Concepción N/P |  | Nube N/P | Portal N/P | Total N/P |
| — | — | — | — | — | — | — |
| 00:00 | 0,54 / 1,01 | 0,27 / 0,50 | 0,00 / 0,00 | 0,74 / 1,37 | 0,00 / 0,00 | 1,55 / 2,88 |
| 01:00 | 0,54 / 1,01 | 0,27 / 0,50 | 0,00 / 0,00 | 0,74 / 1,37 | 0,00 / 0,00 | 1,55 / 2,88 |
| 02:00 | 0,54 / 1,01 | 0,27 / 0,50 | 0,00 / 0,00 | 0,74 / 1,37 | 0,00 / 0,00 | 1,55 / 2,88 |
| 03:00 | 0,54 / 1,01 | 0,27 / 0,50 | 0,78 / 1,44 | 0,74 / 1,37 | 0,00 / 0,00 | 2,33 / 4,33 |
| 04:00 | 0,54 / 1,01 | 0,27 / 0,50 | 1,56 / 2,89 | 0,74 / 1,37 | 0,00 / 0,00 | 3,11 / 5,77 |
| 05:00 | 1,64 / 3,02 | 0,54 / 1,01 | 0,00 / 0,00 | 0,79 / 1,47 | 0,00 / 0,00 | 2,98 / 5,50 |
| 06:00 | 1,11 / 2,00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,68 / 1,26 | 0,00 / 0,00 | 1,79 / 3,26 |
| 07:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,84 / 1,56 | 0,00 / 0,00 | 0,84 / 1,56 |
| 08:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,84 / 1,57 | 0,00 / 0,00 | 0,84 / 1,57 |
| 09:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 1,68 / 3,15 | 4,81 / 4,81 | 6,49 / 7,96 |
| 10:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 1,68 / 3,15 | 4,81 / 4,81 | 6,49 / 7,97 |
| 11:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 1,68 / 3,15 | 4,81 / 4,81 | 6,49 / 7,96 |
| 12:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 2,67 / 5,03 | 9,63 / 9,63 | 12,30 / 14,66 |
| 13:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 1,68 / 3,15 | 4,81 / 4,81 | 6,49 / 7,96 |
| 14:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 1,68 / 3,15 | 4,81 / 4,81 | 6,49 / 7,96 |
| 15:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 1,68 / 3,15 | 4,81 / 4,81 | 6,49 / 7,96 |
| 16:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 1,68 / 3,15 | 4,81 / 4,81 | 6,49 / 7,96 |
| 17:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 2,45 / 4,59 | 4,81 / 4,81 | 7,27 / 9,41 |
| 18:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 2,40 / 4,45 | 0,00 / 0,00 | 2,40 / 4,45 |
| 19:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 1,46 / 2,71 | 0,00 / 0,00 | 1,46 / 2,71 |
| 20:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,68 / 1,26 | 0,00 / 0,00 | 0,68 / 1,26 |
| 21:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,68 / 1,26 | 0,00 / 0,00 | 0,68 / 1,26 |
| 22:00 | 0,54 / 1,01 | 0,27 / 0,50 | 0,00 / 0,00 | 0,74 / 1,37 | 0,00 / 0,00 | 1,55 / 2,88 |
| 23:00 | 0,54 / 1,01 | 0,27 / 0,50 | 0,00 / 0,00 | 0,74 / 1,37 | 0,00 / 0,00 | 1,55 / 2,88 |

La fila de las 12:00 gobierna los TPS totales porque coincide la hora cargada de preventa, reparto y portal. La hora de preparación conserva la mayor carga local de WMS, pero no la mayor suma de lugares.

<a id="sec:anexo-4b-dimensiones-4-6"></a>
## 4.B.3 Dimensiones 4–6: personas, concurrencia y dispositivos

La dimensión 4 es (640 + 160) + 14.200 + 180 = **15.180 personas o entidades**. La dimensión 5 toma el mayor resultado entre ventanas: noche 120 + 60 (S-39) + 6 (S-35) = 186; despacho 96; día sin portal 62 + 96 + 184 = 342; portal en régimen 342 + 96,30 = **438,30**; portal extremo 342 + 433,33 = **775,33**. La dimensión 6 es 62 + 96 = **158 dispositivos de terreno en operación simultánea**.

El parque separado de la dimensión 6 se distribuye así:

- Bodega: 132 terminales en Talca, 22 de ellos para congelado, y 66 en Concepción.
- Terreno: 69 terminales de preventa, 106 de reparto, 106 impresoras y 106 terminales de pago.
- Cross-docking y frío: 7 terminales de cross-docking y 31 termógrafos.

Cada cantidad aplica los supuestos S-28 y S-30 a S-41, registrados en el Subdocumento 3, y la reserva del 10 % del parque de cada tipo, redondeada hacia arriba, conforme a la tabla de repuestos de las Bases Técnicas Transversales (Cap. 8, p. 19):

- Equipos de reparto (S-30): 96 camiones + 10 de reserva = 106 de cada dispositivo. A tres años (S-31), los viajes crecen 2.400 ÷ 2.100 = 1,143, es decir, 14,3 %; la flota llega a 96 × 1,143 = 109,7, unos 110 camiones, y el parque a 110 + 11 = 121, es decir, 15 unidades más de cada dispositivo.
- Terminales de preventa (S-32): 62 + 7 = 69. A tres años, 70 preventistas, un 12,9 % más, y 70 + 7 = 77, es decir, 8 más.
- Terminales de bodega: se comparten entre turnos (RT-12.11; Bases Técnicas del caso, Cap. 15, p. 27), sin personal de carga adicional (S-33), de modo que los fija el turno nocturno: 120 preparadores en Talca y 60 en Concepción (S-39). En Talca, 20 son de la cuadrilla de congelado (S-34): los productos de frío son 1.100 ÷ 8.400 = 13,1 % del surtido y el congelado ocupa 400 ÷ 1.300 = 30,8 % del área fría, de modo que el congelado es cerca de 13,1 % × 30,8 % = 4,0 % de las líneas; 120 personas × 8 h = 960 horas-persona, cuyo 4,0 % son 38,4 horas, concentradas en las últimas 2 horas del turno: 38,4 ÷ 2 = 19,2, unas 20 personas. Talca suma 20 + 2 de congelado y 100 + 10 estándar, Concepción 60 + 6, y los cross-docking 6 + 1 (S-35): 205 en total. A tres años (S-32), la dotación de los centros de distribución crece 350 ÷ 310 = 12,9 %: Talca llega a 23 + 3 de congelado y 113 + 12 estándar, y Concepción a 68 + 7; con los 7 de los cross-docking, el parque llega a 233, es decir, 28 más.
- Termógrafos: 28 + 3 = 31, para los 18 camiones con frío propios y los 10 de transportistas (S-28), sin compra por crecimiento (S-38).

<a id="sec:anexo-4b-dimensiones-7-10"></a>
## 4.B.4 Dimensiones 7–10: almacenamiento, retención y migración

El almacenamiento transaccional se calcula con 1.300.000 eventos = 260.000 líneas × 5, 520.000 operaciones = 260.000 líneas × 2, 155.000 operaciones = 31.000 pedidos × 5 y 279.050 movimientos = 260.000 líneas + 14.500 pallets + 3.400 conteos + 1.150 recepciones. Por tanto, ((1.300.000 + 520.000 + 155.000) × 1 KB + 279.050 × 0,5 KB) × 2 × 12 = **50,75 GB/año** y seis años acumulan **304,49 GB** como cota de retención. La evidencia es 30 KB + 200 KB × (1 + 900 ÷ 31.000) = **235,81 KB por entrega** y genera **87,72 GB/año**; en el mes peak alcanza 13,58 GB.

La temperatura separa cámaras y camiones: 21 puntos instalados × 288 lecturas/día = 6.048 lecturas de cámara, con la cámara de Concepción estimada por S-37, y 28 termógrafos × 162 lecturas/día entre 05:30 y 19:00 = 4.536 lecturas de camión; el total es 10.584 mensajes/día. Con 145 bytes por lectura, son 0,56 GB/año crudos, 0,14 GB/año almacenados con factor 0,25 y 2,80 GB crudos en cinco años. La posición produce 42 camiones × 12 h × 120 eventos/h × 365 = 22.075.200 eventos/año; se cuentan los 365 días como cota, aunque el domingo no hay reparto; con 145 bytes son 3,20 GB crudos y 0,80 GB almacenados en 12 meses. Son filas separadas porque sus retenciones son distintas.

La dimensión 10 se estima por dominio:

- Maestros completos: 34.180 KB.
- Ventas y pedidos: 3 años y 10.476.000 KB.
- Inventario y movimientos: 2 años y 3.348.600 KB.
- Recepciones con campo de lote: 5 años y 1.380.000 KB.
- Cuentas por cobrar: 2 años y 816.000 KB.

La suma de 16.054.780 KB × 2 ÷ 1.000.000 = **32,11 GB**. Con 10 o 30 líneas por recepción, el intervalo es **30,73–33,49 GB**. No se multiplican eventos históricos de trazabilidad: el caso declara que no existe una forma consultable. El 41 % sin lote sólo orienta el saneamiento.

<a id="sec:anexo-4b-dimensiones-11-12"></a>
## 4.B.5 Dimensiones 11–12: integraciones, mensajes y enlaces

La dimensión 11 cuenta los quince contratos INT-01 a INT-15 del apartado 4.1. La Tabla [33](#tab:anexo-4b-integraciones) deja el volumen por integración; las solicitudes del portal y las llamadas internas no aparecen.

<a id="tab:anexo-4b-integraciones"></a>
**Tabla 33.** Mensajes por integración
| Integración | Normal/día | Peak/día | Origen del volumen |
| — | — | — | — |
| INT-01 Pedido preventa y consulta | 1.400 | 2.600 | 1.400 × 1; 2.600 × 1, por SV-01 |
| INT-02 Entrega, POD y cobro | 7.000 | 13.000 | 1.400 × 5; 2.600 × 5 |
| INT-03 Eventos de bodega a nube | 58.710 | 109.032 | 260.000 ÷ 22,14 × 5; peak × 1,857 |
| INT-04 Detalle cross-docking a Talca | 5.600 | 10.400 | 1.400 × 4; cota de una plataforma |
| INT-05 Eventos de temperatura | 10.584 | 10.584 | 6.048 + 4.536 lecturas/día |
| INT-06 ERP 2017 | 2.025 | 3.762 | 1.400 + 1.150 ÷ 22,14 + 900 ÷ 22,14 + 11.800 ÷ 22,14; peak × 1,857 |
| INT-07 DTE/SII | 3.071 | 5.703 | 34.000 ÷ 22,14 × 2; peak × 1,857 |
| INT-08 Cadenas modernas EDI | 0 | 1.144 | 0 actual; 2.600 × 11 % × 4 |
| INT-09 Pasarela de pago | 533 | 990 | 11.800 ÷ 22,14; peak × 1,857 |
| INT-10 Mapas y geocodificación | 96 | 96 | 96 camiones × 1 |
| INT-11 Avisos al cliente | 2.800 | 5.200 | 1.400 × 2; 2.600 × 2 |
| INT-12 Cambios de datos a réplica | 12.602 | 23.404 | 279.050 ÷ 22,14; peak × 1,857 |
| INT-13 Identidad a sitio | 760 | 760 | 380 dispositivos × 2 |
| INT-14 Métricas y trazas | 10.000 | 10.000 | 10 nodos × 1.000 |
| INT-15 Telemetría existente | 60.480 | 60.480 | 42 × 12 × 120 |
| **Total** | **175.661** | **257.155** | **15 integraciones** |

Para la dimensión 12, el drenaje se obtiene sumando los aportes acumulados en 24 horas y dividiendo por 2 horas:

- Aportes en Talca: los cambios de 0,041 GB/día viajan como WAL, que no se suma aparte: WAL = 3 × 0,041 = 0,123 GB/día; broker = 0,5 × 0,041 = 0,020 GB/día; telemetría = 10.584 × 145 ÷ 1.000.000.000 ÷ 2 = 0,001 GB/día; observabilidad = 5 × 0,25 = 1,25 GB/día; incremental de respaldo = 0,041 GB/día.
- Resultado por sitio: Talca suma 1,43 GB/día y drena 1,59 Mbps; la hora cargada de oficina y retorno de flota suma 3,71 Mbps, por lo que el peor caso es 3,71 + 1,59 = **5,30 Mbps**. Concepción acumula 0,59 GB/día y drena 0,66 Mbps; cada cross-docking acumula 0,27 GB/día y drena 0,30 Mbps.
- Utilización de enlaces: Talca, 26,51 % de D-03 y 31,88 % de D-04; Concepción, 7,68 % y 21,93 %; cada cross-docking, 17,41 % de D-06 y 14,92 % de D-04.

La utilización de respaldo divide sólo el drenaje por D-04, porque la sincronización tiene prioridad sobre la oficina durante la recuperación.

La ventana dominical usa ocho horas sin operación de bodega ni reparto. En Talca, el respaldo completo de 15,12 GB se convierte en 1,68 horas sobre 20 Mbps y la App de reparto, 23,80 GB, en 2,64 horas; juntas requieren 4,32 horas. Una tanda de 16 sistemas operativos de 2 GB agrega 3,56 horas y ocupa 7,88 horas, por lo que cabe una tanda por domingo y se necesitan 15 domingos para 238 equipos. En Concepción, respaldo de 7,76 GB y aplicación de 6,60 GB requieren 3,19 horas; una tanda de 10 sistemas operativos ocupa 7,64 horas y se necesitan 7 domingos. En cada cross-docking, el respaldo de 1,89 GB y la aplicación de sus 2 terminales, 0,20 GB, requieren 2,33 horas sobre 2 Mbps; con los 2 sistemas operativos la ventana ocupa 6,77 horas y basta un domingo. En cada sitio, el tamaño de la aplicación es ≤100 MB por equipo y preventa usa la red móvil; las actualizaciones se escalonan trimestralmente.

<a id="sec:anexo-4b-dimensiones-13-14"></a>
## 4.B.6 Dimensiones 13–14: terreno y sincronización

La peor ruta produce 34 × 235,81 KB ÷ 1.024 + 2 MB = **9,83 MB**. La ruta promedio produce 5,36 MB normales y 8,24 MB en septiembre. Para diez minutos, el umbral es 9,83 MB × 8 ÷ 600 segundos = **0,13 Mbps efectivos**.

La dimensión 14 es un tiempo. Los 96 camiones regresan entre 17:00 y 20:00; con SV-04, 96 ÷ 3 × 2 = **64 camiones** llegan en la hora punta. Su carga es 64 × 9,83 MB × 8 ÷ 3.600 segundos = **1,40 Mbps** en Wi-Fi y enlace. La flota completa agrega 0,70 Mbps durante las tres horas y queda sincronizada aproximadamente diez minutos después del último camión.

<a id="sec:anexo-4b-dimensiones-15-16"></a>
## 4.B.7 Dimensiones 15–16: mesa de ayuda y operación

La mesa de ayuda se dimensiona en cuatro pasos:

1. Demanda horaria: (640 + 160) × 2,5 = **2.000 contactos mensuales**. Con 22,14 días equivalentes, la hora cargada concentra 2.000 × 25 % ÷ 22,14 = 22,58 contactos/hora y cada una de las otras 17 horas recibe 2.000 × 75 % ÷ 22,14 ÷ 17 = 3,98 contactos/hora.
2. Resultado Erlang C: con 10 minutos de atención media, 80 % de respuestas antes de 20 segundos y abandono ≤5 %, exige 7 agentes en la hora cargada y 2 en las demás.
3. Dotación simultánea: (7 + 17 × 2) × 6 = 246 horas-posición semanales; 246 ÷ 42 = 5,86, pero la dotación no puede ser menor que las 7 posiciones simultáneas, por lo que la mesa requiere **7 personas**.
4. Capacidad máxima de siete agentes: Al resolver el mismo cálculo, el límite es 2.391 contactos/mes; 2.391 × 25 % ÷ 22,14 = 27,00 contactos/hora cargada y 2.391 × 75 % ÷ 22,14 ÷ 17 = 4,99 contactos/hora en las demás franjas.

La cobertura 24×7 de septiembre y diciembre requiere, además, al menos una posición de mesa en las horas 22:00–04:00 de lunes a sábado y durante los domingos: 6 × 6 + 24 = 60 horas-posición semanales; 60 ÷ 42 = 1,43, por lo que se agregan **2 personas** y la mesa peak queda en 9. Un NOC y un SOC de una posición cada uno requieren 2 × (168 ÷ 42) = **8 personas**; desde el 26-04-2028 requieren 2 × (168 ÷ 40) = **10 personas**. La dotación total es 15 personas en operación normal y 17 en septiembre/diciembre a 42 horas; con 40 horas, 17 y 19. Las funciones NOC/SOC pueden ser subcontratadas conforme a RT-21.01 (Bases Técnicas Transversales, Cap. 21, p. 35) y RT-11.17 (Bases Técnicas Transversales, Cap. 11, p. 24).

<a id="sec:anexo-4b-onpremise"></a>
## 4.B.8 Capacidad on-premise por VM

La base local contiene maestros, stock, lotes presentes y movimientos del horizonte de cuatro meses. El tamaño usa 1 KB por registro, 0,5 KB por movimiento y factor 2 de índices y auditoría. La RAM de la base usa 4 GB más 25 % del tamaño a 3×.

<a id="tab:anexo-4b-vm"></a>
**Tabla 34.** Requerimiento por VM real del diseño
| VM o equipo | Requerido actual | Requerido a 3× | Sitio |
| — | — | — | — |
| VM-01 | 3 vCPU; 4 GB; 50 GB; 25 IOPS | 3 vCPU; 4 GB; 50 GB; 73 IOPS | Talca |
| VM-02 | 3 vCPU; 6 GB; 20 GB; 25 IOPS | 3 vCPU; 8 GB; 31 GB; 73 IOPS | Talca |
| VM-03 | 2 vCPU; 4 GB; 50 GB; 25 IOPS | 2 vCPU; 4 GB; 50 GB; 73 IOPS | Talca |
| VM-04 | 2 vCPU; 2 GB; 20 GB; 5 IOPS | 2 vCPU; 2 GB; 20 GB; 13 IOPS | Talca |
| VM-05 | 2 vCPU; 2 GB; 20 GB; 25 IOPS | 2 vCPU; 2 GB; 20 GB; 73 IOPS | Talca |
| VM-06 | 2 vCPU; 4 GB; 50 GB; 49 IOPS | 2 vCPU; 4 GB; 50 GB; 97 IOPS | Talca |
| VM-C01 | 3 vCPU; 4 GB; 50 GB; 9 IOPS | 3 vCPU; 4 GB; 50 GB; 25 IOPS | Concepción |
| VM-C02 | 3 vCPU; 5 GB; 20 GB; 9 IOPS | 3 vCPU; 6 GB; 20 GB; 25 IOPS | Concepción |
| VM-C03 | 2 vCPU; 2 GB; 20 GB; 9 IOPS | 2 vCPU; 2 GB; 20 GB; 25 IOPS | Concepción |
| VM-C04 | 2 vCPU; 4 GB; 50 GB; 17 IOPS | 2 vCPU; 4 GB; 50 GB; 33 IOPS | Concepción |
| Mini-PC | 3 vCPU; 5 GB; 50 GB; 70 IOPS | 3 vCPU; 5 GB; 50 GB; 208 IOPS | Cada cross-docking |

Talca requiere 17 vCPU, 24 GB RAM y 210 GB actuales; a 3×, 17 vCPU, 26 GB y 221 GB. Con un nodo caído, el T-11 deja 128 vCPU, 256 GB RAM y 3.840 GB lógicos: la utilización es 13,28 % / 9,38 % / 5,47 % actual y 13,28 % / 10,16 % / 5,76 % a 3× para CPU, RAM y disco. La configuración mínima sin marca que cumple N+1 y 3× es 9 vCPU, 13 GB RAM y 221 GB lógicos por nodo.

<a id="sec:anexo-4b-nube"></a>
## 4.B.9 Capacidad en nube

El perfil de API atiende aplicaciones y portales N-01 a N-03. Una tarea Fargate entrega 0,70 ÷ 0,05 = **14,00 solicitudes/s**. La tabla de carga es: régimen, 12,30 solicitudes/s de nube más portal y 2 tareas; peak, 14,66 y 2; RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21), 21,99 y 2; cota extrema, 5,03 + 43,33 = 48,37 y 4. La sensibilidad de 120 solicitudes por sesión conserva las sesiones repartidas en la hora: 2,67 + 19,27 = 21,93 y 2 tareas en régimen; 5,03 + 86,67 = 91,70 y 7 tareas en cota. Todos los casos quedan bajo el techo de 8 tareas.

<a id="sec:anexo-4b-crecimiento"></a>
## 4.B.10 Crecimiento, enlaces y ventana dominical

La proyección de año 3 de la Tabla 14.1 es 36.000 pedidos, 305.000 líneas, 1.650 entregas normales, 3.100 entregas peak y 40.000 DTE mensuales. Cada componente usa una base distinta:

- WMS Talca = 3,02 × (305.000 ÷ 260.000) = 3,54 TPS.
- Nube más portal = 14,66 × (36.000 ÷ 31.000) = 17,03 solicitudes/s.
- Evidencia = 87,72 × (36.000 ÷ 31.000) = 101,87 GB/año.
- Enlace de Talca = 5,34 Mbps por el nuevo flujo de cambios.
- Terminales de bodega de Talca = (23 + 3) de congelado + (113 + 12) estándar = 151.
- Mesa = 2.000 × (350 ÷ 310) = 2.258 contactos/mes.

Por separado, RT-09.03 (Bases Técnicas Transversales, Cap. 9, p. 21) exige 3×: 93.000 pedidos, 780.000 líneas, 4.200/7.800 entregas y 102.000 DTE mensuales.

<a id="tab:anexo-4b-plan"></a>
**Tabla 35.** Plan de capacidad
| Componente | Año 1 | Año 3 | 3× | Acción |
| — | — | — | — | — |
| WMS de Talca, TPS peak | 3,02 | 3,54 | 9,06 | Revisar CPU e IOPS trimestralmente |
| Nube, TPS peak / tareas | 14,66 / 2 | 17,03 / 2 | 43,98 / 4 | Escalamiento y prueba trimestral |
| Evidencia anual | 87,72 GB | 101,87 GB | 263,16 GB | Escalar S3 y retención |
| Enlace de Talca, peor caso | 5,30 Mbps | 5,34 Mbps | 8,71 Mbps | Ampliar D-03 si p95 supera la cota |
| Terminales de bodega de Talca | 132 | 151 | no aplica | Ajustar parque a la dotación |
| Mesa, contactos mensuales | 2.000 | 2.258 | 6.000 | Recalibrar Erlang C |

La prueba RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21) usa una sola multiplicación: 14,66 × 1,5 = 21,99 TPS. Las tareas, colas y almacenamiento en nube escalan por política; la reserva N+1, la Wi-Fi y los enlaces se amplían mediante revisión planificada.

<a id="sec:anexo-4b-umbrales"></a>
## 4.B.11 Umbrales de quiebre y cuello de botella

La sensibilidad de SV-04 antes de alcanzar la capacidad CPU calculada es Talca 593,84×, Concepción 221,88×, cada cross-docking 9,69× y nube más portal 7,64×. La peor ruta exige 0,13 Mbps efectivos y la hora punta de retorno exige 1,40 Mbps agregados.

La emisión de guías es el primer candidato a cuello de botella: 2.852 guías admiten 9,47 segundos cada una en la preparación completa, 4,42 segundos al final del turno y 1,89 segundos en la ventana actual. Se observan guías aún no emitidas frente a la salida, tiempo del ERP, cola, base WMS, IOPS, Wi-Fi y drenaje en percentil 95. La degradación controlada encola con clave idempotente, aplica límite de tasa y muestra un mensaje explícito; el ERP sigue siendo el único emisor.

<a id="sec:anexo-4b-pruebas"></a>
## 4.B.12 Pruebas de carga, estrés y operación

La carga RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21) se ejecuta a **21,99 TPS totales**, distribuidos por lugar según el perfil horario, sin multiplicar cada lugar por separado. El estrés que exige el mismo RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21) supera la cota extrema del portal y la volumetría 3×. La prueba de corte dura 24 horas y debe drenar en dos; la sincronización de la peor ruta debe completar en diez minutos. Se ejecutan dos ensayos de migración conforme a RT-05.13 (Bases Técnicas Transversales, Cap. 5, p. 12) y una verificación de la ventana dominical para cada sitio.

Se conservan percentil 95, utilización, colas, errores, pérdida o duplicación, estado de conciliación y parámetros confirmados. El perfil horario, la migración y la operación dominical se cierran con evidencia de prueba, sin convertir el resultado medido en un hecho previo.
