<a id="h-04-partes-4-3-centros-de-datos-05-d-sitio-principal-tex-96"></a>

# 4.3 Data center

<a id="cap-4-3-data-center"></a>

La estrategia de centros de datos distribuye la operación productiva entre la región primaria AWS sa-east-1 y la sala técnica secundaria del CD Talca. El dominio de nube se recupera en us-east-1; ante la pérdida de la sala de Talca, su WMS se levanta en la plataforma de nube de la región activa sobre la copia en Aurora. Concepción y las tres plataformas de cross-docking son sitios operacionales autónomos y publican sus eventos para la consolidación central.

La arquitectura fija RTO ≤ 4 h, RPO ≤ 15 min y disponibilidad mensual de 99,95 % por componente de infraestructura, con un compromiso de ≥ 99,9 % para la transacción crítica de extremo a extremo. Esta sección concreta los emplazamientos, servicios y conexiones descritos en 4.2; el equipamiento y los servicios contratados se detallan en el Formulario T-11, entregado como archivo propio.

<a id="h-04-partes-4-3-centros-de-datos-05-d-sitio-principal-tex-97"></a>

## 4.3.1 Especificaciones Data Center Primaria

<a id="sec-d-especificaciones-del-sitio-principal-on-"></a>

El Data Center Primario concentra la operación productiva de la solución en dos dominios que se exigen mutuamente por el carácter híbrido obligatorio del despliegue: la región primaria de la nube en sa-east-1, ubicada en São Paulo, Brasil, y la sala técnica secundaria on-premise del centro de distribución de Talca, tipología que fija el propio caso. Ambos dominios se especifican bajo el mismo criterio: un centro de datos comprende no solo los servidores, sino también las condiciones que sostienen la operación sin interrupción: energía acondicionada, clima controlado, conectividad, seguridad física y monitoreo permanente con procedimiento escrito.

Esta sección declara, para cada dominio, el proveedor, la región y las zonas de disponibilidad, los servicios contratados y el sitio on-premise. También fija los objetivos de continuidad verificables que los gobiernan: disponibilidad de infraestructura de 99,95 % mensual por componente y, para los servicios críticos, RTO ≤ 4 h y RPO ≤ 15 min. Sobre estos objetivos se sostiene el compromiso contractual penalizable de ≥ 99,9 % mensual de la transacción de negocio de extremo a extremo. El desglose servicio por servicio y componente por componente se entrega en el Formulario T-11.

<a id="h-04-partes-4-3-centros-de-datos-05-d-sitio-principal-tex-98"></a>

### 4.3.1.1 Proveedor

Para la nube en Amazon Web Services todos los servicios se contratan en cuentas del CLIENTE, que son organizadas bajo AWS Control Tower con una cuenta por ambiente de modo que la propiedad de los datos y de la infraestructura es del CLIENTE desde el primer día. Los criterios con que se eligieron esos servicios se explican en el apartado [4.2.3](../../LAFROX-Subdocumento4.md#sec-servicios-nube). AWS satisface el requisito de presencia de región o zona en Chile o en Sudamérica con la región primaria sa-east-1. El cumplimiento de los estándares y marcos de referencia del Artículo 4.3 de las Bases Administrativas (PUCV, 2026c, art. 4.3, p. 5) entre ellos ISO/IEC 27017 (nube) e ISO/IEC 27018 (datos personales en nube) se acredita en la matriz de controles ISO/IEC 27001/27002 de la arquitectura de seguridad (apartado 4.1), y no se repite en esta sección.

En el dominio On-premise del CD de Talca, el caso exige cómputo, almacenamiento y procesamiento en las instalaciones del CLIENTE para sostener recepción, preparación y despacho durante un corte de enlace; ello obliga a la modalidad híbrida. Ese alcance requiere cómputo local para la continuidad de un sitio operacional sin albergar el núcleo. Por ello, el sitio adopta la tipología de **sala técnica secundaria o de sitio** del numeral 6.1 de las Bases Técnicas Transversales (PUCV, 2026b, cap. 6, p. 14), con disponibilidad de infraestructura de 99,95 % y dimensionamiento proporcional al equipamiento real.

<a id="h-04-partes-4-3-centros-de-datos-05-d-sitio-principal-tex-99"></a>

### 4.3.1.2 Región y zonas de disponibilidad

La región primaria de la nube es sa-east-1, ubicada en São Paulo, Brasil. Todo componente con requisito de alta disponibilidad se despliega en al menos dos zonas de disponibilidad; no se acepta un diseño en una sola zona. Aurora PostgreSQL tiene el escritor en sa-east-1a y un lector promovible en sa-east-1b. ECS Fargate, ElastiCache Redis, el balanceador de aplicación y el NAT Gateway operan entre esas mismas dos zonas con conmutación automática; DynamoDB opera Multi-AZ de forma nativa y transparente. El único componente con escritor único es la base de datos, que conmuta de forma automática entre las zonas. Este diseño sostiene el compromiso de extremo a extremo de ≥ 99,9 % mensual de la transacción crítica y la conmutación se verifica en las pruebas de resiliencia por inyección de fallas de la arquitectura de despliegue.

<a id="h-04-partes-4-3-centros-de-datos-05-d-sitio-principal-tex-100"></a>

### 4.3.1.3 Servicios contratados en la región primaria

Los servicios contratados en la región primaria son los que agrupa por función la Tabla [11](../../LAFROX-Subdocumento4.md#tab-servicios-nube) del apartado [4.2.3](../../LAFROX-Subdocumento4.md#sec-servicios-nube). En esta región se concentran la operación productiva, la analítica y los servicios de detección, cumplimiento y gobierno; todos son servicios administrados, de modo que la solución no opera servidores en la nube.

<a id="h-04-partes-4-3-centros-de-datos-05-d-sitio-principal-tex-101"></a>

### 4.3.1.4 Sitio on-premise: CD Talca (sala técnica secundaria)

El caso fija para el CD de Talca una sala técnica secundaria ``dimensionada para sostener recepción, preparación y despacho durante un corte'', y advierte que la sala actual de 25 m2 no cumple el Capítulo 6 de las Bases Técnicas Transversales (PUCV, 2026b, p. 14). Conforme a la tipología del numeral 6.1 de las Bases Técnicas Transversales (PUCV, 2026b, cap. 6, p. 14), no se aplica íntegramente a este sitio el conjunto de exigencias de una sala técnica principal, sino el subconjunto dimensionado al sitio: energía, climatización, control de acceso, detección de incendio y monitoreo. El numeral 6.1 de las Bases Técnicas Transversales (PUCV, 2026b, cap. 6, p. 14) exige declarar la tipología y justificar el dimensionamiento, y advierte que ``sobredimensionar el recinto es tan penalizado como subdimensionarlo: ambos revelan que el cálculo de capacidad no se hizo''. El equipamiento real que la sala debe alojar y los cálculos eléctrico y térmico desarrollados a continuación determinan su superficie proyectada, que se fija en el plano de distribución interna (Figura [30](../../LAFROX-Subdocumento4.md#fig-recinto-talca)).

La sala aloja el siguiente equipamiento:

-  El núcleo del componente on-premise, con el motor WMS y el borde operacional del CD sobre un clúster virtualizado de tres nodos con redundancia N+1, que tolera la pérdida de cualquier nodo manteniendo quórum.

-  Una NAS local con el respaldo de recuperación rápida.

-  Los dos firewalls de la frontera del sitio.

El listado completo de componentes de sala (UPS, generador, climatización, seguridad física, extinción, cableado y gabinetes) y del equipamiento de cómputo y red que alojan los gabinetes se entrega en el Formulario T-11. La ocupación por rack y el margen de crecimiento se declaran en la Figura [29](../../LAFROX-Subdocumento4.md#fig-racks-talca).

Para la disponibilidad y la redundancia la disponibilidad de infraestructura comprometida es del 99,95 % mensual por componente en energía del recinto, climatización, red y comunicaciones, servidores y cómputo, y motor de base de datos. Además se sostiene con redundancia N+1 en energía y climatización, con generación autónoma y con monitoreo continuo con alertamiento. No se invoca una clasificación de instalación de terceros (ejemplo un nivel TIER certificado), por lo que los niveles de disponibilidad de infraestructura del numeral 7.2 de las Bases Técnicas Transversales (PUCV, 2026b, cap. 7, p. 17) son un medio, no un fin y el compromiso que se mide y se penaliza es el de la transacción de negocio de extremo a extremo.

La Figura [28](../../LAFROX-Subdocumento4.md#fig-cd-talca) muestra cómo se conecta el equipamiento de la sala con la bodega, la cadena de frío y el ERP.

![Figura original](https://raw.githubusercontent.com/PatricioH315/LafroX/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/centros_de_datos/Arquitectura_Fisica_CD_Talca.png)

**Figura 28 — Arquitectura física del sitio on-premise del CD Talca**

<a id="fig-cd-talca"></a>

*Fuente: elaboración propia.*

La fibra D-03 es el enlace principal, LTE D-04 el segundo camino y Starlink D-06 el tercero en espera caliente; los tres llegan al par de firewalls, uno activo y otro pasivo. Starlink permanece encendido, con el túnel IPsec establecido y BGP con menor preferencia, y toma el tráfico solo si fallan fibra y LTE. En ese caso, la calidad de servicio prioriza DMS y WAL de Talca, la salida del broker y el outbox, las guías hacia el ERP y el SII, la identidad y la telemetría crítica. El terminal permanece encendido porque adquirir satélites y negociar el túnel durante una falla tardaría minutos; la tarifa plana no agrega costo por ello. Detrás, los dos switches de núcleo y el switch de gestión reparten la red hacia el clúster Proxmox VE con Ceph de tres nodos. El clúster aloja seis máquinas virtuales: VM-01 con el núcleo del WMS, VM-02 con PostgreSQL, VM-03 con RabbitMQ, VM-04 con la capa anticorrupción y los dos procesos de `erp-sync` que conversan con el ERP de 2017, VM-05 con la caché de Keycloak y VM-06 con el colector ADOT y el agente de Systems Manager. La línea punteada representa a AWS DMS, que lee los cambios de VM-02 por la VPN para replicarlos en Aurora. En la bodega, los terminales MC9400 y las impresoras de andén trabajan por Wi-Fi 6E contra el WMS; en la cadena de frío, los sensores entregan sus lecturas al gateway IoT, que las publica por MQTTS y bloquea el despacho ante una excursión térmica. El respaldo de recuperación rápida queda en la NAS WORM. La figura muestra que todo lo que la bodega necesita para recibir, preparar y despachar está dentro del sitio, y que la pérdida de un nodo no detiene la operación, porque sus máquinas virtuales se reinician en los otros dos.

La cadena eléctrica sigue esta secuencia: empalme → tablero general → transferencia automática → UPS → PDU del rack → fuente del equipo → servidor.

Esta cadena consta de UPS de doble conversión on-line en configuración N+1 con autonomía mínima de 30 minutos a plena carga y generación autónoma para un rango mínimo de 24 horas continuas, con estanque de combustible dimensionado y contrato de reabastecimiento declarado. La instalación eléctrica es independiente de la del resto del edificio y conforme a la normativa eléctrica chilena vigente, incluida la NCh Elec. 2777; se revisa y mide semestralmente, con informe entregable al CLIENTE, conforme a RT-06.10 (PUCV, 2026b, cap. 6, p. 15).

Para el cálculo de carga eléctrica se usa una cota conservadora por equipo, según la Tabla [34](../../LAFROX-Subdocumento4.md#tab-4-3-1): en los nodos, la suma de sus dos fuentes, y en los demás equipos, su potencia máxima de ficha. El Formulario T-11 declara los mismos valores por equipo.

<a id="tab-4-3-1"></a>

**Tabla 34 — Carga eléctrica de TI proyectada del recinto**

| **Equipo** | **Cantidad** | **Potencia de placa por unidad** | **Subtotal** |
| --- | --- | --- | --- |
| Nodo de cómputo del clúster (servidor rack 2U, un procesador) | 3 | 1.600 W (2 fuentes de 800 W) | 4.800 W |
| NAS local | 1 | 400 W | 400 W |
| Firewall del perímetro del sitio | 2 | 150 W | 300 W |
| Conmutador de núcleo (switch core) | 2 | 150 W | 300 W |
| Switch de gestión | 1 | 50 W | 50 W |
| **Carga TI base** |  |  | **5.850 W** |
| Consola KVM (cubierta por el margen) | 1 | 50 W | Incluida en el margen |
| Margen de crecimiento a tres años (20 %) |  |  | + 1.170 W |
| **Carga TI de diseño** |  |  | **7.020 W ≈ 7,0 kW** |

 Fuente: elaboración propia.

El cálculo eléctrico sigue estos pasos:

1.  Potencia aparente y UPS: con factor de potencia 0,95, 7,0 kW ÷ 0,95 ≈ 7,4 kVA; al 80 % de utilización, 7,4 kVA ÷ 0,8 ≈ 9,2 kVA. El UPS seleccionado es modular de 10 kVA, de doble conversión on-line, en configuración N+1 y con bypass de mantenimiento.

2.  PUE: la suma de 7,0 kW de carga TI, ≈ 2,1 kW de climatización de precisión, ≈ 0,4 kW de climatización de la sala de UPS, ≈ 0,6 kW de iluminación y apoyo y ≈ 0,61 kW de pérdidas del UPS es ≈ 10,7 kW; 10,7 ÷ 7,0 ≈ 1,5. Los gateways IoT y sus fuentes agregan ≈ 0,1 kW al consumo del sitio, hasta ≈ 10,8 kW, pero quedan fuera del PUE de la sala. El PUE estimado y la carga declarada satisfacen RT-06.11 (PUCV, 2026b, cap. 6, p. 15). El numerador se mide en el tablero del recinto y el denominador a la salida de las PDU, semestralmente y con informe entregable.

3.  Generador: la carga del sitio de ≈ 10,8 kW, con factor de potencia 0,8, requiere ≈ 10,8 ÷ 0,8 ≈ 13,5 kVA. Se especifica un grupo electrógeno de 20 kVA, que deja la carga de diseño bajo el 80 % de su capacidad, con estanque para 24 horas continuas y contrato de reabastecimiento.

La climatización de precisión para la operación continua es redundante en configuración N+1 y controla la temperatura y la humedad relativa dentro de los rangos que recomienda el fabricante del equipamiento.

Para calcular la carga térmica, se considera que cada kW eléctrico consumido por el equipamiento se disipa físicamente como aproximadamente 1 kW de calor sensible (≈ 3.412 BTU/h). Como el UPS está en su propia sala, la carga térmica de la sala de servidores corresponde a la carga TI de diseño, como resume la Tabla [35](../../LAFROX-Subdocumento4.md#tab-4-3-2):

<a id="tab-4-3-2"></a>

**Tabla 35 — Carga térmica sensible proyectada del recinto**

| **Origen del calor** | **Potencia equivalente** |
| --- | --- |
| Carga TI de diseño | 7.000 W |
| **Carga térmica sensible de diseño** | **≈ 7,0 kW** |

 Fuente: elaboración propia.

Sobre esa carga se instalan dos unidades de climatización de precisión de 10 kW cada una, en configuración N+1; una sola cubre los 7,0 kW de diseño con holgura. La temperatura y la humedad relativa se controlan dentro de los rangos del fabricante del equipamiento. La sala de UPS y baterías dispone de climatización de confort propia de 3,5 kW (≈ 12.000 BTU/h), que mantiene 20–25 °C, y de ventilación; disipa las pérdidas del UPS (≈ 0,61 kW) y el calor de carga de las baterías.

La consola KVM, con 50 W de potencia de placa, y los equipos terminales de acceso del operador (ONT de fibra, router LTE y terminal Starlink) quedan cubiertos por el margen de diseño del 20 % de la Tabla [34](../../LAFROX-Subdocumento4.md#tab-4-3-1), sin alterar el UPS de 10 kVA ni el generador de 20 kVA.

La protección contra incendios reúne estos elementos:

-  Detección temprana por aspiración de aire con tecnología láser, tipo AnaLASER.

-  Extinción automática con agente limpio tipo FM-200 con aprobación UL e instalación conforme a norma NFPA, con botón de aborto.

-  Sistema secundario de extintores portátiles habilitados con mantención y certificación vigentes.

El sistema de detección y extinción se integra al monitoreo en línea y notifica al NOC y a la contraparte del CLIENTE.

La Figura [29](../../LAFROX-Subdocumento4.md#fig-racks-talca) muestra cómo se reparte el equipamiento de cómputo y red en los dos racks de la sala.

![Figura original](https://raw.githubusercontent.com/PatricioH315/LafroX/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/centros_de_datos/Racks_CD_Talca.png)

**Figura 29 — Distribución de U y ocupación proyectada de los racks del CD Talca**

<a id="fig-racks-talca"></a>

*Fuente: elaboración propia.*

El rack R01 aloja los tres nodos del clúster, de 2U cada uno, la consola KVM y la NAS WORM; el rack R02 aloja el ODF, los paneles, los dos switches de núcleo, el switch de gestión, el par de firewalls y la bandeja del operador con la ONT de fibra, el router LTE y el terminal Starlink. Cada rack ocupa 12U de 42 (29 %). La carga de R01 es de 5,2 kW base y 6,2 kW de diseño, y la de R02, de 0,65 kW base y 0,8 kW de diseño; las cargas base suman los 5.850 W de la Tabla [34](../../LAFROX-Subdocumento4.md#tab-4-3-1), y las de diseño, los 7,0 kW que resultan al agregar el margen de 20 %. La figura dibuja comprimidos los bloques libres e indica la posición de cada equipo en U. Los racks de servidores son independientes de los racks de equipos de comunicación. La ocupación proyectada reserva margen de crecimiento a tres años, coherente con el 20 % de reserva de la carga eléctrica (Tabla [34](../../LAFROX-Subdocumento4.md#tab-4-3-1)), de modo que la ocupación declarada y su margen quedan fijados en la figura y en el Formulario T-11.

El control de acceso y la seguridad física del recinto comprenden:

-  Seguridad física y control de acceso biométrico basado principalmente en biometría facial con AFIS como respaldo.

-  Registro de todo ingreso y egreso en una bitácora auditable con identificación, fecha, hora y motivo.

-  Un espacio para atender a las personas en proceso de enrolamiento entre el acceso principal y el término del pasillo de la zona de control, además de una estación de enrolamiento fuera de las instalaciones del recinto técnico.

-  Un acceso al término del pasillo que impide el paso de más de una persona a la vez, con nueva verificación de identidad previa al ingreso.

-  Videovigilancia y monitoreo IP con imágenes en línea disponibles al menos los últimos 30 días y respaldo recuperable.

Las instalaciones sanitarias, las zonas de seguridad ante emergencia y las áreas exteriores existentes en el edificio del CLIENTE se utilizan, sin implementarlas nuevamente dentro del recinto. La bitácora auditable se conserva por un período de retención no inferior a cinco años, coherente con el piso que las Bases fijan para la retención de la auditoría del proyecto.

Los equipos de energía y climatización y los controles de acceso descritos se ordenan físicamente como muestra la Figura [30](../../LAFROX-Subdocumento4.md#fig-recinto-talca), que distribuye el recinto por zonas y líneas de acceso.

![Figura original](https://raw.githubusercontent.com/PatricioH315/LafroX/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/centros_de_datos/Recinto_CD_Talca.png)

**Figura 30 — Distribución interna del recinto técnico del CD Talca por zonas y líneas de acceso**

<a id="fig-recinto-talca"></a>

*Fuente: elaboración propia.*

El plano ordena el recinto en profundidad progresiva. En el exterior quedan el grupo electrógeno con su estanque, el empalme con la transferencia automática entre red y generador, las condensadoras de la climatización y la llegada independiente de fibra, LTE y Starlink. La fibra y LTE ingresan al edificio por puntos separados y siguen ductos independientes hasta la sala, conforme a RT-06.32 (PUCV, 2026b, cap. 6, p. 17); Starlink constituye el tercer camino. La línea técnica reúne la sala de UPS y baterías, el tablero eléctrico independiente del recinto y la acometida de comunicaciones, junto con la zona de trabajo y la zona de respaldo. La línea restringida contiene solo la sala de servidores y comunicaciones, con los racks R01 y R02, la climatización de precisión y la detección y extinción. El ingreso sigue un único recorrido: acceso principal, pasillo de control con espacio de enrolamiento, esclusa que admite una persona a la vez con nueva verificación y, recién entonces, la sala; la estación de enrolamiento y los baños quedan fuera del recinto. Los puestos de trabajo y el área de respaldo quedan en la línea técnica, separados de la sala de equipos, de modo que las labores habituales de operación no exigen ingresar a la línea restringida. La separación física de generadores y baterías respecto del área de servidores evita que una falla de energía o de clima contamine el cómputo, y deja al proveedor de fibra y al de climatización sin cruzar la última línea del recinto.

El sitio monitorea en línea la temperatura, la humedad y la presencia de agua, con alertamiento integrado a la plataforma de observabilidad. El estado de los puntos controlados del recinto converge en la plataforma de monitoreo, con destinatario, canal, tiempo de respuesta y procedimiento escrito. La observabilidad reutiliza el mecanismo del sitio on-premise hacia la nube que define la arquitectura de despliegue del apartado [4.2.4](../../LAFROX-Subdocumento4.md#sec-despliegue). La convergencia en un solo tablero constituye la plataforma de observabilidad del sitio. No se declara una plataforma DCIM/BMS de terceros porque las Bases no la exigen y el monitoreo ambiental y de alertas se satisface con el monitoreo en línea y su alertamiento integrado.

El cómputo local corre sobre un clúster virtualizado de tres nodos N+1 con quórum real. Ceph distribuye tres réplicas sobre NVMe sin RAID y tolera la pérdida de un nodo; el respaldo local reside en el NAS D-05 con RAID 6. La selección se justifica en ADR-10 (Anexo 4-O). La instancia de escritura VM-02 se reinicia en otro nodo ante una falla.
