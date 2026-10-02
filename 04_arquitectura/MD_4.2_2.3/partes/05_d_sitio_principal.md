<!-- Fuente: 04/partes/4.3_centros_de_datos/05_d_sitio_principal.tex — conversión fiel; editar el .tex y regenerar -->

<a id="cap:4-3-data-center"></a>
# 4.3 Data center

<a id="sec:d-especificaciones-del-sitio-principal-on-"></a>
## 4.3.1 Especificaciones Data Center Primaria

El Data Center Primario concentra la operación productiva de la solución en dos dominios que se exigen mutuamente por el carácter híbrido obligatorio del despliegue: la región primaria de la nube en sa-east-1, ubicada en São Paulo, Brasil, y la sala técnica secundaria on-premise del centro de distribución de Talca, tipología que fija el propio caso. Ambos dominios se especifican bajo el mismo criterio: un centro de datos comprende no solo los servidores, sino también las condiciones que sostienen la operación sin interrupción: energía acondicionada, clima controlado, conectividad, seguridad física y monitoreo permanente con procedimiento escrito.

Esta sección declara, para cada dominio, el proveedor, la región y las zonas de disponibilidad, los servicios contratados y el sitio on-premise. También fija los objetivos de continuidad verificables que los gobiernan: disponibilidad de infraestructura de 99,95 % mensual por componente y, para los servicios críticos, RTO ≤ 4 h y RPO ≤ 15 min. Sobre estos objetivos se sostiene el compromiso contractual penalizable de ≥ 99,9 % mensual de la transacción de negocio de extremo a extremo. El desglose servicio por servicio y componente por componente se entrega en el Formulario T-11.

### 4.3.1.1 Proveedor

Para la nube en Amazon Web Services todos los servicios se contratan en cuentas del CLIENTE, que son organizadas bajo AWS Control Tower con una cuenta por ambiente de modo que la propiedad de los datos y de la infraestructura es del CLIENTE desde el primer día. Los criterios con que se eligieron esos servicios se explican en el apartado [4.2.3](02_b_servicios_nube.md#sec:servicios-nube). AWS satisface el requisito de presencia de región o zona en Chile o en Sudamérica con la región primaria sa-east-1. El cumplimiento de los estándares y marcos de referencia del Artículo 4.3 de las Bases Administrativas (Art. 4.3, p. 5) entre ellos ISO/IEC 27017 (nube) e ISO/IEC 27018 (datos personales en nube) se acredita en la matriz de controles ISO/IEC 27001/27002 de la arquitectura de seguridad (apartado 4.1), y no se repite en esta sección.

En el dominio On-premise del CD de Talca, el caso exige cómputo, almacenamiento y procesamiento en las instalaciones del CLIENTE para sostener recepción, preparación y despacho durante un corte de enlace; ello obliga a la modalidad híbrida. Ese alcance requiere cómputo local para la continuidad de un sitio operacional sin albergar el núcleo. Por ello, el sitio adopta la tipología de **sala técnica secundaria o de sitio** del numeral 6.1 de las Bases Técnicas Transversales (Cap. 6, p. 14), con disponibilidad de infraestructura de 99,95 % y dimensionamiento proporcional al equipamiento real.

### 4.3.1.2 Región y zonas de disponibilidad

La región primaria de la nube es sa-east-1, ubicada en São Paulo, Brasil. Todo componente con requisito de alta disponibilidad se despliega en al menos dos zonas de disponibilidad; no se acepta un diseño en una sola zona. Aurora PostgreSQL tiene el escritor en sa-east-1a y un lector promovible en sa-east-1b. ECS Fargate, ElastiCache Redis, el balanceador de aplicación y el NAT Gateway operan entre esas mismas dos zonas con conmutación automática; DynamoDB opera Multi-AZ de forma nativa y transparente. El único componente con escritor único es la base de datos, que conmuta de forma automática entre las zonas. Este diseño sostiene el compromiso de extremo a extremo de ≥ 99,9 % mensual de la transacción crítica y la conmutación se verifica en las pruebas de resiliencia por inyección de fallas de la arquitectura de despliegue.

### 4.3.1.3 Servicios contratados en la región primaria

Los servicios contratados en la región primaria son los que agrupa por función la Tabla [5](#tab:servicios-nube) del apartado [4.2.3](02_b_servicios_nube.md#sec:servicios-nube). En esta región se concentran la operación productiva, la analítica y los servicios de detección, cumplimiento y gobierno; todos son servicios administrados, de modo que la solución no opera servidores en la nube.

### 4.3.1.4 Sitio on-premise: CD Talca (sala técnica secundaria)

El caso fija para el CD de Talca una sala técnica secundaria “dimensionada para sostener recepción, preparación y despacho durante un corte”, y advierte que la sala actual de 25 m<sup>2</sup> no cumple el Capítulo 6 de las Bases Técnicas Transversales (p. 14). Conforme a la tipología del numeral 6.1 de las Bases Técnicas Transversales (Cap. 6, p. 14), no se aplica íntegramente a este sitio el conjunto de exigencias de una sala técnica principal, sino el subconjunto dimensionado al sitio: energía, climatización, control de acceso, detección de incendio y monitoreo. El numeral 6.1 de las Bases Técnicas Transversales (Cap. 6, p. 14) exige declarar la tipología y justificar el dimensionamiento, y advierte que “sobredimensionar el recinto es tan penalizado como subdimensionarlo: ambos revelan que el cálculo de capacidad no se hizo”. El equipamiento real que la sala debe alojar y los cálculos eléctrico y térmico desarrollados a continuación determinan su superficie proyectada, que se fija en el plano de distribución interna (Figura [15](05_d_sitio_principal.md#fig:recinto-talca)).

La sala aloja el siguiente equipamiento:

- El núcleo del componente on-premise, con el motor WMS y el borde operacional del CD sobre un clúster virtualizado de tres nodos con redundancia N+1, que tolera la pérdida de cualquier nodo manteniendo quórum.
- Una NAS local con el respaldo de recuperación rápida.
- Los dos firewalls de la frontera del sitio.

El listado completo de componentes de sala (UPS, generador, climatización, seguridad física, extinción, cableado y gabinetes) y del equipamiento de cómputo y red que alojan los gabinetes se entrega en el Formulario T-11. La ocupación por rack y el margen de crecimiento se declaran en la Figura [14](05_d_sitio_principal.md#fig:racks-talca).

Para la disponibilidad y la redundancia la disponibilidad de infraestructura comprometida es del 99,95 % mensual por componente en energía del recinto, climatización, red y comunicaciones, servidores y cómputo, y motor de base de datos. Además se sostiene con redundancia N+1 en energía y climatización, con generación autónoma y con monitoreo continuo con alertamiento. No se invoca una clasificación de instalación de terceros (ejemplo un nivel TIER certificado), por lo que los niveles de disponibilidad de infraestructura del numeral 7.2 de las Bases Técnicas Transversales (Cap. 7, p. 17) son un medio, no un fin y el compromiso que se mide y se penaliza es el de la transacción de negocio de extremo a extremo.

La Figura [13](05_d_sitio_principal.md#fig:cd-talca) muestra cómo se conecta el equipamiento de la sala con la bodega, la cadena de frío y el ERP.

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

La Figura [14](05_d_sitio_principal.md#fig:racks-talca) muestra cómo se reparte el equipamiento de cómputo y red en los dos racks de la sala.

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

Los equipos de energía y climatización y los controles de acceso anteriores se ordenan físicamente como muestra la Figura [15](05_d_sitio_principal.md#fig:recinto-talca), que distribuye el recinto por zonas y líneas de acceso.

<a id="fig:recinto-talca"></a>
![](https://raw.githubusercontent.com/PatricioH315/LafroX/95ed2c9a1cc20aa7ad9f3ebbe03cafa0e1e1259c/04/figuras/centros_de_datos/Recinto_CD_Talca.png)

**Figura 15.** Distribución interna del recinto técnico del CD Talca por zonas y líneas de acceso

*Fuente: elaboración propia.*

El plano ordena el recinto en profundidad progresiva. En el exterior quedan el grupo electrógeno con su estanque, el empalme con la transferencia automática entre red y generador, las condensadoras de la climatización y la llegada de la fibra y el LTE por dos ductos independientes. La línea técnica reúne la sala de UPS y baterías, el tablero eléctrico independiente del recinto y la acometida de comunicaciones, junto con la zona de trabajo y la zona de respaldo. La línea restringida contiene solo la sala de servidores y comunicaciones, con los racks R01 y R02, la climatización de precisión y la detección y extinción. El ingreso sigue un único recorrido: acceso principal, pasillo de control con espacio de enrolamiento, esclusa que admite una persona a la vez con nueva verificación y, recién entonces, la sala; la estación de enrolamiento y los baños quedan fuera del recinto. Los puestos de trabajo y el área de respaldo quedan en la línea técnica, separados de la sala de equipos, de modo que las labores habituales de operación no exigen ingresar a la línea restringida. La separación física de generadores y baterías respecto del área de servidores evita que una falla de energía o de clima contamine el cómputo, y deja al proveedor de fibra y al de climatización sin cruzar la última línea del recinto.

El sitio monitorea en línea la temperatura, la humedad y la presencia de agua, con alertamiento integrado a la plataforma de observabilidad. El estado de los puntos controlados del recinto converge en la plataforma de monitoreo, con destinatario, canal, tiempo de respuesta y procedimiento escrito. La observabilidad reutiliza el mecanismo del sitio on-premise hacia la nube que define la arquitectura de despliegue del apartado [4.2.4](11_j_despliegue.md#sec:despliegue). La convergencia en un solo tablero constituye la plataforma de observabilidad del sitio. No se declara una plataforma DCIM/BMS de terceros porque las Bases no la exigen y el monitoreo ambiental y de alertas se satisface con el monitoreo en línea y su alertamiento integrado.

El cómputo almacenado onsite corre sobre un clúster virtualizado de tres nodos con redundancia N+1 y almacenamiento distribuido que tolera la pérdida de al menos un nodo con quórum real. El almacenamiento local combina un nivel para la base transaccional (RAID 10 NVMe) y otro para el respaldo local (NAS D-05, RAID 6), justificados frente a las alternativas en la sección [4.4.10](14_m_decisiones_adr.md#sub:adr-10). La instancia de escritura es el punto único declarado y se mitiga con reinicio en otro nodo del clúster.
