# Capítulo 4 · Arquitectura Física y de Despliegue de la Solución (Parte 4.2) {-}


## Visión general de la arquitectura física

La solución se despliega en dos dominios que se reparten el trabajo según lo que cada uno hace mejor. La carga principal —el núcleo transaccional de preventa, reparto y canal moderno, la integración, la analítica y el almacenamiento consolidado— corre en nube pública, sobre una región primaria en Sudamérica y una región secundaria en otro continente que sostiene la recuperación ante desastres. Los componentes on-premise cargan con lo que no puede depender de un enlace: la recepción, la preparación y el despacho de los centros de distribución, y la operación de terreno en 14.200 puntos de entrega.

Ese reparto no es una preferencia de diseño, sino la respuesta a tres hechos del caso. La fibra de los centros se corta unas cuatro veces al año. Hay rutas rurales donde el conductor recupera cobertura recién al regresar. Y entre las 05:30 y las 07:00 salen 96 camiones sin que exista plan manual que los reemplace. De ahí los tres compromisos que gobiernan todo lo demás: el centro de distribución opera veinticuatro horas seguidas sin enlace, el terminal de terreno opera un turno completo de catorce horas sin señal, y la ventana de despacho no admite indisponibilidad.

La red de instalaciones es de seis sitios en cuatro regiones. Cinco alojan cómputo —el centro de distribución de Talca, que es la sala técnica principal; el de Concepción, con gabinete de borde; y las tres plataformas de cross-docking de Curicó, Chillán y Los Ángeles— y el sexto es la casa matriz, contigua al centro principal, que no procesa operación logística y consume la nube a través del portal y del back office. El capítulo 8 del caso menciona cinco instalaciones mientras que su tabla de volumetría y el requisito de traslado a sitios alejados declaran seis: la divergencia se eleva como consulta al mandante y no altera el dimensionamiento, que se calcula sobre los cinco sitios con cómputo. La proyección del caso a tres años incorpora un séptimo sitio, que se absorbe por parametrización y con el gabinete de crecimiento ya reservado en la sala, sin obras adicionales.

Cuatro decisiones estructurales se desprenden de ahí y se desarrollan en las secciones siguientes:

- La identidad tiene una autoridad única en la nube y cachés locales de solo lectura. No existe un segundo maestro on-premise que haya que promover, de modo que un corte prolongado nunca abre la posibilidad de dos verdades de identidad.
- Ningún nodo on-premise acepta conexiones entrantes. Todo el tráfico se inicia desde adentro hacia la nube, con dos excepciones controladas que viajan por el túnel cifrado.
- Cada sitio dispone de dos caminos de comunicación independientes, con conmutación automática en menos de treinta segundos. En los centros de distribución se combina fibra óptica y LTE, y en los cross-docking, Starlink y LTE.
- El respaldo es uno solo para los dos dominios: copia local de recuperación rápida, copia inmutable en la nube, réplica en la región secundaria y custodia física externa.

La arquitectura se describe conforme a la norma ISO/IEC/IEEE 42010 sobre el marco TOGAF, y es coherente con la arquitectura lógica de la parte 4.1: las mismas capas, los mismos módulos y el mismo conjunto de tecnologías. La correspondencia entre cada requisito de las Bases y el lugar preciso de este capítulo donde se resuelve consta en la planilla de trazabilidad normativa que acompaña a esta parte; el pronunciamiento formal sobre la totalidad de los requisitos se entrega en el Formulario T-12.


## Modelo de emplazamiento híbrido

La solución se despliega en dos dominios, la nube pública y el on-premise, conectados por túneles VPN cifrados. Cada dominio puede operar de forma independiente cuando el enlace no está disponible.


### Dominio nube (AWS sa-east-1)

La nube concentra la carga principal de la solución. Todos los servicios se despliegan en al menos dos zonas de disponibilidad dentro de la región sa-east-1, de modo que la caída de un centro de datos de AWS no interrumpe la operación. La aplicación Django corre en contenedores ECS Fargate y atiende los procesos de preventa, reparto, canal moderno y el portal de clientes. Aurora PostgreSQL almacena la base de datos transaccional maestra y recibe en tiempo real las transacciones que se originan en las bodegas a través del servicio de replicación DMS CDC.

Todo el tráfico externo ingresa por API Gateway, donde WAF v2 valida las solicitudes y Shield protege contra ataques de denegación de servicio, antes de que el tráfico alcance la aplicación. Cuando las bodegas reconectan tras un corte de enlace, las transacciones pendientes llegan a la cola SQS FIFO, que las procesa en el orden exacto en que ocurrieron y sin duplicados. Cuando la aplicación registra un hecho relevante —una entrega confirmada, una excursión térmica o un pedido del canal moderno—, Celery despacha las tareas derivadas: enviar la notificación al cliente, actualizar los tableros analíticos, emitir el documento tributario al SII y, en la etapa de cadenas de supermercados, transmitir el acuse por EDI.

La telemetría de cadena de frío llega desde los gateways Greengrass en las bodegas hasta IoT Core en la nube. La capa analítica se apoya en Redshift Serverless para consultas históricas de hasta 5 años, y QuickSight publica los tableros de gestión del CLIENTE. La observabilidad se consolida en CloudWatch, que recibe logs, métricas y trazas tanto de los servicios en nube como de los colectores on-premise cuando estos disponen de enlace, y expone los tableros de operación sin infraestructura adicional que mantener. La identidad la gobierna Keycloak, que corre como servicio maestro en Fargate y distribuye las credenciales hacia las cachés locales de cada sitio. Una réplica pasiva de la infraestructura crítica en us-east-1 sostiene la recuperación ante desastres.


### Dominio on-premise (5 sitios con cómputo)

Cada centro de distribución mantiene su propia pila local: la misma aplicación Django corre en modo WMS contra una base PostgreSQL 16 local, un broker RabbitMQ que encola las transacciones y una caché de Keycloak que sostiene la sesión de los operarios. En CD Talca, un clúster Proxmox VE de 3 nodos con almacenamiento Ceph aloja las VMs (VM-01 a VM-06); en CD Concepción, un servidor de borde replica la misma pila (VM-C01 a VM-C04). Los tres cross-docking (Curicó, Chillán y Los Ángeles) operan con un mini-PC industrial que corre el WMS en Docker. La capa anticorrupción del ERP (VM-04, Talca) es la única puerta hacia el sistema legado. Los gateways IoT Greengrass procesan la cadena de frío en el borde, con detección de excursión térmica y bloqueo de despacho 100 % local. Un NAS cifrado (D-05) guarda la pierna local de respaldo 3-2-1-1-0.


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
- **Reparto en calle:** los conductores usan terminales Zebra TC58e, también con SIM 4G/LTE empresarial. Se comunican directamente con API Gateway por la red celular durante los turnos de reparto (14 h) y, cuando pierden señal en zonas rurales, operan contra su almacén local y sincronizan al reconectar.
- **Termógrafos de camión:** los termógrafos Onset InTemp CX450, calibrados contra patrón NIST, registran la temperatura del compartimento refrigerado de forma independiente y sin conexión a red durante toda la ruta. Al regresar el camión al centro de distribución, los datos se descargan por Bluetooth al gateway local del sitio y desde ahí se envían a IoT Core en la nube.

Cuando el enlace WAN cae, cada dominio sigue operando con su pila local: la bodega contra PostgreSQL y RabbitMQ locales, el terreno de calle contra su almacén local, y el cross-docking contra su WMS local. Al reconectar, la sincronización es determinista y no genera duplicados. El detalle de la autonomía por ámbito se desarrolla en la sección de operación desconectada de este mismo capítulo.


### Emplazamiento componente por componente

Las tablas 21a, 21b y 21c justifican la decisión de emplazamiento de cada componente conforme a los seis criterios del Art. 16.2: latencia tolerada, criticidad operacional, volumen de datos, restricciones regulatorias, disponibilidad de conectividad y costo total de propiedad. El criterio dominante se indica al inicio de cada justificación. Estas tablas responden a la pregunta *dónde* vive cada componente y *por qué*; el equipamiento físico ofertado (marca, modelo y cantidad) se detalla en el capítulo de implementos, y la infraestructura de sala del CD Talca (energía, clima, seguridad física y cableado) en el capítulo del sitio principal.


> **Tabla 21a** — Emplazamiento: componentes de nube pura (servicios administrados AWS sa-east-1) · 14 filas · ver planilla del subdocumento

> **Tabla 21b** — Emplazamiento: componentes on-premise · 11 filas · ver planilla del subdocumento

> **Tabla 21c** — Emplazamiento: componentes híbridos · 7 filas · ver planilla del subdocumento


![Diagrama de arquitectura física de la solución](../Diagramas/ARQF-01_Modelo_emplazamiento_hibrido.png)

Figura 15. Diagrama de arquitectura física de la solución.


### Instalaciones de la red on-premise

La red on-premise se compone de seis instalaciones (Tabla 14.1 y RT-21.16):

- **CD Talca (sala técnica principal, sala blanca de 32 m²):** clúster WMS de 3 nodos, base transaccional on-premise (PostgreSQL 16, VM-02), broker local RabbitMQ (VM-03), capa anticorrupción del ERP (VM-04), caché de identidad (VM-05), telemetría (VM-06), respaldo NAS (D-05) y componentes de sala (UPS N+1, generador 12 kVA con estanque 24 h, clima N+1, seguridad física).

- **CD Concepción (9.000 m², gabinete de borde):** servidor de borde con el WMS (VM-C01), base local (VM-C02), caché de identidad (VM-C03), broker + telemetría (VM-C04) y Gateway IoT Greengrass (B-02); opera 24 h de forma autónoma e independiente de Talca.

- **Cross-docking de Curicó, Chillán y Los Ángeles:** nodo de cómputo industrial (E-01) con WMS y broker locales, enlace principal Starlink (D-06) y respaldo LTE dual (2 proveedores).

- **Casa matriz y oficinas centrales (Talca):** sin nodo de cómputo propio; acceso a la nube para administración, planificación y portal de clientes.

La proyección a 3 años incorpora una séptima instalación; el gabinete de crecimiento de la sala (R04) absorbe esa expansión sin obras adicionales en el sitio principal.


## Tecnologías de software ofertadas

Las tecnologías se eligen bajo los criterios de neutralidad tecnológica, soporte vigente por los 56 meses contractuales y preferencia por servicios administrados y componentes de código abierto con estándares abiertos, de modo que el CLIENTE conserve la reversibilidad de la solución:


> **Tabla 22** — Tecnologías de Software a Utilizar · 15 filas · ver planilla del subdocumento


### Integración con el ERP y documentos tributarios

El ERP de 2017 no se reemplaza ni se modifica (Cap. 10 del caso): permanece como única fuente de verdad tributaria. La solución entrega los datos de operación a través de la capa anticorrupción (ACL, VM-04) y el ERP emite los documentos tributarios (guía de despacho electrónica, factura, boleta y nota de crédito con folios SII), con acuse de recibo con efectos legales —una sola verdad, un solo emisor. El acceso desde la nube a este ERP ocurre únicamente vía la ACL (celery-erp-sync → ACL, nunca escritura directa).


## Implementos a proveer: hardware y software

El inventario ofertado se agrupa en infraestructura de cómputo y almacenamiento, red y seguridad, dispositivos de terreno y operación. Son especificaciones de equipamiento físico (marca, modelo y cantidad) que el CLIENTE adquiere y el adjudicatario instala, integra y mantiene. Las cantidades y justificaciones de cada fila se referencian al Formulario T-11. La decisión de emplazamiento de cada componente (dónde vive y por qué, según Art. 16.2) se declara en el capítulo de emplazamiento; los componentes de infraestructura de sala del CD Talca (UPS, generador, climatización, seguridad física y gabinetes) se declaran en el capítulo del sitio principal.


### Infraestructura de cómputo y almacenamiento


> **Tabla 23** — c.1 Infraestructura de cómputo y almacenamiento · 4 filas · ver planilla del subdocumento


### Red y seguridad


> **Tabla 24** — c.2 Red y seguridad · 11 filas · ver planilla del subdocumento


### Dispositivos de terreno y operación


> **Tabla 25** — c.3 Dispositivos de terreno y operación · 12 filas · ver planilla del subdocumento

Gateway IoT + Greengrass (B-02): 2 unidades (Talca y Concepción), ADAM-6000, con runtime AWS IoT Greengrass Core embebido para detección de excursión y buffer local de 14 h.


### Resumen del inventario ofertado


> **Tabla 26** — c.4 Resumen del inventario ofertado · 27 filas · ver planilla del subdocumento


## Especificaciones del sitio principal on-premise (CD Talca)

**Tipología declarada (numeral 6.1 de las Transversales): sala técnica principal.** El CD Talca aloja el núcleo del componente on-premise —moPtor WMS, base transaccional del maestro de bodega, broker de colas, capa anticorrupción del ERP, caché de identidad, telemetría y respaldo local—, es decir cómputo, almacenamiento y procesamiento sustantivos en instalaciones del CLIENTE. Por eso se le aplican íntegramente los requisitos RT-06.01 a RT-06.34, y no el régimen proporcional de una sala de sitio.

**Disponibilidad de infraestructura comprometida: 99,95 % mensual**, conforme al numeral 6.1 y a la tabla del numeral 7.2 de las Transversales, medida por componente: energía del recinto, climatización, red y comunicaciones, servidores y cómputo, y motor de base de datos. El compromiso se sostiene con redundancia N+1 en energía y climatización, doble acometida con transferencia automática, generación autónoma propia y monitoreo continuo con alertamiento; no se invoca ninguna clasificación de instalación de tercero, porque las Bases no exigen certificación de nivel sino el cumplimiento verificable de cada requisito técnico individual. Este valor es el nivel de la infraestructura del recinto y es distinto del compromiso contractual penalizable del Artículo 78°, que recae sobre la transacción de negocio de extremo a extremo (≥ 99,9 % mensual, RT-10.01).

El programa arquitectónico propuesto considera ≈ 173 m² y 14 recintos: sala blanca de 32 m², NOC de 14 m², sala de sistemas de alimentación ininterrumpida y baterías, sala de climatización, sala de extinción, distribuidor principal y acometidas, recinto de custodia de medios de 10 m², patio de generador y recintos de apoyo. La disposición interna, la separación de zonas y la elevación de gabinetes constan en los planos del recinto que acompañan a esta parte.

Energía: UPS doble conversión on-line 6 kVA con configuración N+1 y banco VRLA con autonomía ≥ 30 min a plena carga; grupo electrógeno de 12 kVA con estanque para 24 h y contrato de reabastecimiento; transferencia automática red↔generador con prueba mensual con carga real; PDU verticales A/B por gabinete con medidor; factor de potencia ≥ 0,95.

Climatización: 2 CRAC de precisión ≈ 12.000 BTU/h en N+1, con free cooling, pasillo frío confinado y rango ASHRAE TC 9.9 de 18–27 °C y 40–60 % HR medido a la toma de aire del equipo; PUE objetivo de diseño 1,7 (valor conservador para sala de servidores pequeña con climatización de precisión N+1) con medición continua en 2 puntos y reporte trimestral.

Incendios: detección temprana por aspiración AnaLASER; extinción con agente limpio FM-200 conforme NFPA 75/2001 con botón de aborto; extintores ABC y CO₂ por recinto.

Seguridad física: 4 capas de acceso con biometría facial y resguardo AFIS, esclusa antipassback y bitácora electrónica, una persona a la vez y acompañada; 12 puertas controladas y 7 cámaras IP con retención ≥ 30 días integradas al control de acceso; NOC de 14 m² contiguo a la sala con ventana interior («ver sin entrar»); sensores ambientales DCIM/BMS.

Custodia de medios: recinto de 10 m² en la segunda línea, sin luz UV (≤ 300 lux), 40–60 % HR, ventilación forzada y 18–27 °C; medio cifrado transportable rotado semanalmente a bóveda externa bajo custodia acreditada con cadena de custodia y bitácora; la pierna inmutable S3 es complementaria, no la reemplaza.

Cableado y comunicaciones: cableado estructurado Cat6A F/UTP + fibra OM4 certificado enlace por enlace sobre piso técnico de 40 cm, jerarquía ANSI/TIA-942 ENI→MDA→HDA→ZDA→EDA, con dos ductos de ingreso independientes; 4 racks 42U en gabinete de servidores y comunicaciones separados, con el cuarto (R04) reservado al crecimiento a 3 años.

Los componentes de infraestructura de sala del CD Talca (UPS, generador, transferencia automática, climatización, seguridad física, extinción, cableado y gabinetes) se detallan a continuación. El equipamiento de cómputo, red y comunicaciones que se aloja en estos gabinetes (servidores, switches, firewalls, WLAN, terminales) se declara en el capítulo de implementos.


> **Tabla 27** — Especificaciones del sitio principal on-premise (CD Talca) · 12 filas · ver planilla del subdocumento


## Especificaciones del sitio secundario

**Cómo se satisface el numeral 7.1.** Las Transversales exigen un sitio secundario en dependencias distintas del principal, en modalidad activo-activo o activo-pasivo, con replicación en línea del ambiente de producción y características tecnológicas equivalentes a las del sitio principal en lo que respecta a los servicios críticos. La solución lo satisface con dos sitios secundarios, uno por cada dominio del despliegue híbrido, porque la carga crítica vive en ambos:

- **Para el componente on-premise, el CD Concepción:** es una dependencia física distinta, a 340 km del extremo opuesto de la red y sin amenazas comunes con Talca, y opera el motor de almacenes con su propia base local y autonomía de 24 horas. No es un sitio en espera: opera de forma autónoma todos los días y asume la carga de bodega de Talca mediante promoción controlada.
- **Para la carga principal en nube, la región AWS us-east-1:** aloja la réplica pasiva promovible del núcleo transaccional, a ≈ 7.700 km de la región primaria y ≈ 8.500 km de Talca, sin amenazas comunes.

El mecanismo de recuperación ante desastres (modalidad activo-pasiva, RTO ≤ 4 h, RPO ≤ 15 min), el procedimiento de conmutación y retorno, las pruebas semestrales, la tabla de componentes de la réplica y el esquema de respaldos 3-2-1-1-0 se declaran en el capítulo de arquitectura de despliegue.

El gabinete de borde con que se habilitan el sitio secundario on-premise y las tres plataformas de cross-docking se muestra en la figura correspondiente.


## Operación desconectada


> **Tabla 29** — Operación desconectada · 4 filas · ver planilla del subdocumento


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

Los planos de mensajería y su emplazamiento físico se describen en la Tabla 35.


> **Tabla 35** — Mensajería: planos y emplazamiento físico · 4 filas · ver planilla del subdocumento


### Costuras híbridas: amarre con la arquitectura física

La vista de integración y la vista física describen los mismos puntos de contacto. La Tabla 36 amarra ambas: cada costura física se cruza con la integración lógica que la usa, su contrato y sus extremos.


> **Tabla 36** — Costuras híbridas: amarre con la arquitectura física · 12 filas · ver planilla del subdocumento


### Carga y descarga masiva de datos


> **Tabla 39** — Carga y descarga masiva de datos · 4 filas · ver planilla del subdocumento

Regla: ninguna carga masiva se ejecuta dentro de la ventana crítica 05:30–07:00, y toda carga queda registrada y es auditable.


## Arquitectura de seguridad

Arquitectura de seguridad de la solución: modelo Zero Trust, capa expuesta, identidad y accesos, cifrado y controles. El perímetro de esta solución no es un edificio corporativo sino un entorno distribuido con alta rotación de personal externo y dispositivos compartidos en terreno, por lo que el modelo es Zero Trust y la identidad es la pieza central.


### Principios rectores


> **Tabla 42** — 1. Principios rectores · 8 filas · ver planilla del subdocumento


### Modelo Zero Trust aplicado


#### Los siete principios de NIST SP 800-207 en Puelche


> **Tabla 43** — 2.1 Los siete principios de NIST SP 800-207 en Puelche · 7 filas · ver planilla del subdocumento


#### Zonas y flujos

En texto, las zonas y su flujo son: la zona pública (clientes del canal moderno, transportistas ≈160 conductores y 180 proveedores) ingresa únicamente por la DMZ en nube (CloudFront + AWS WAF v2 + Shield Advanced → Amazon API Gateway con OIDC, cuotas, esquema y validación de carga útil); la zona de aplicación (ECS Fargate M1–M12 + workers y Keycloak IdP maestro como autoridad única) sirve a las zonas de datos (Aurora PostgreSQL, DynamoDB y S3 con Object Lock, en subredes privadas sin salida); la zona on-premise (VLAN 10 MGT · 20 SRV · 30 OPS · 40 WKS · 50 IOT, firewall D-01 UTM en HA como Customer Gateway y caché Keycloak de solo lectura TTL 8 h) conecta con la nube por VPN/IPsec saliente; y la zona de terreno (apps Kotlin offline-first + MDM; HHT compartidos en cámara a −22 °C) no tiene perímetro.

Reglas de zona declaradas:

- La única exposición pública es la DMZ en nube (CloudFront → WAF → API Gateway). Las consolas internas no pasan por ahí: entran por intranet o VPN.
- La zona de datos no tiene salida a internet y se consume por VPC Endpoints/PrivateLink.
- Desde la zona on-premise no se acepta ninguna conexión entrante salvo las dos excepciones D-AL-05.
- La zona de terreno no tiene perímetro: se protege con identidad, cifrado local, MDM y borrado remoto.


### Capa expuesta


> **Tabla 44** — 3. Capa expuesta · 8 filas · ver planilla del subdocumento


#### Superficie de exposición completa


> **Tabla 45** — 3.1 Superficie de exposición completa · 8 filas · ver planilla del subdocumento

Regla declarada: ningún nodo on-premise abre puertos entrantes. Toda gestión remota entra por el agente SSM sobre HTTPS saliente o por la VPN, nunca por un puerto publicado.


### Identidad, acceso y sesiones


#### Modelo de identidad (Modelo B)

Autoridad única en nube, cachés locales de solo lectura. El Keycloak IdP maestro vive en ECS Fargate (sa-east-1, Multi-AZ, respaldo en Aurora) y concentra todas las escrituras: altas, bajas, cambios de rol, políticas y revocaciones. En VM-05 (Talca) y VM-C03 (Concepción) operan cachés locales de solo lectura con TTL de 8 h que validan la firma OIDC de forma local. No existe un maestro on-premise ni promoción local a escritura.

Esta decisión resuelve un problema real del caso: el centro de distribución debe autenticar durante 24 h sin enlace y el terreno durante 14 h sin señal, pero un segundo maestro on-premise habría creado dos fuentes de verdad de identidad y un procedimiento de conmutación con riesgo de divergencia. Con el Modelo B, el DRP de identidad es la misma autoridad en nube: no hay nada que promover.


> **Tabla 46** — 4.1 Modelo de identidad (Modelo B) · 3 filas · ver planilla del subdocumento

Sincronización sin conexiones entrantes: el maestro publica el Realm cifrado a S3 y las cachés lo importan (INT-13, saliente). Las altas, bajas y roles se propagan desde el maestro hacia las cachés, nunca a la inversa. Revocación: Δ ≤ 8 h por TTL y < 24 h por SCIM; para identidades de alta sensibilidad la baja se refuerza con el bloqueo del terminal por MDM.


#### Federación, SSO y factores

OpenID Connect y OAuth 2.1, con SAML 2.0 disponible si la integración con el CLIENTE lo requiere; integración con el directorio corporativo por LDAP.

Inicio de sesión único para todos los módulos y cierre de sesión propagado (back-channel logout).

MFA obligatoria para administradores, accesos privilegiados y todo acceso desde fuera de la red corporativa.

Factores resistentes a la suplantación: FIDO2/WebAuthn (claves de acceso) disponible y preferente para perfiles administradores, además de TOTP (se supera el mínimo exigido).

Acceso de conductores externos: OTP de un solo uso por operación, sin cuenta corporativa (RF-06.08). Es la respuesta al hecho de que ~160 conductores no son trabajadores de la compañía y rotan sin aviso.


#### Autorización: RBAC más ABAC


> **Tabla 47** — 4.3 Autorización: RBAC más ABAC · 4 filas · ver planilla del subdocumento

El control de acceso se resuelve en cuatro capas:

- **RBAC.** Roles derivados de los 11 actores canónicos del modelo lógico. Los permisos viven en Keycloak.
- **ABAC.** Atributos de contexto que acotan el rol: instalación asignada, horario de turno (el despacho solo es válido en su ventana), dispositivo provisto y enrolado por MDM. Las políticas se aplican en la Capa 4.
- **Segregación de funciones.** Conciliación ≠ aprobación (M10); detección de excursión térmica ≠ decisión de bloqueo (M9); rendición ≠ cierre contable (M7). Nadie que genera un control lo ejecuta. La matriz completa se declara en el registro de requerimientos (Cap. 17.1).
- **Aislamiento de externos.** Cada proveedor ve solo sus órdenes de compra y documentos; cada transportista solo sus rutas asignadas. No hay visibilidad cruzada.


#### Política de sesión


> **Tabla 48** — 4.4 Política de sesión · 11 filas · ver planilla del subdocumento

La política de sesión se declara en cinco términos:

- **Duración máxima.** La credencial de acceso dura 30 minutos, valor único de la propuesta que rige para todos los perfiles (D-AL-07); la credencial de identidad vive 1 hora. En operación desconectada la sesión no depende del IdP sino de la caché local (A-05): el token de turno cubre 8 horas en el centro de distribución y 14 horas en terreno, de modo que la ventana sin enlace nunca queda descubierta (ADR-06).
- **Caducidad por inactividad.** 30 minutos en consolas de bodega y back-office y 60 minutos en superficies de solo lectura; una pantalla de consulta no obliga a reautenticarse cada media hora.
- **Renovación de la credencial de sesión.** Por credencial de refresco rotatoria de 30 días: cada uso emite una nueva e invalida la anterior, y el reúso detectado invalida la familia completa y fuerza la reautenticación.
- **Revocación inmediata.** El cierre global de sesión desde el panel de administración corta una sesión ante la pérdida o el compromiso de un dispositivo, y la baja de una identidad revoca sus credenciales vigentes.
- **Control de sesiones concurrentes.** Una sola sesión activa por actor de terreno: se deniega el inicio simultáneo del mismo preventista o conductor en otro dispositivo, con opción de invalidar la anterior.

La elevación temporal de privilegios no excede las 2 horas y exige justificación, aprobación de un segundo perfil y registro auditado. Las credenciales están firmadas y son de vida breve, la credencial de refresco es rotatoria y ningún identificador de sesión viaja en la ruta de la dirección web; el token se envía siempre en la cabecera de la petición. El registro, la verificación de identidad y la recuperación de acceso autoservido de personas usuarias externas se cubren con el mecanismo declarado en la subsección de federación.


#### Autenticación en el perfil operacional de terreno

El caso fija condiciones que descartan la contraseña como mecanismo de terreno: guantes térmicos a −22 °C, uso a una mano durante la descarga, uso de pie y a la intemperie en la puerta del local, dispositivos compartidos entre turnos en bodega y 38 % de rotación anual en preparación. La respuesta declarada:

- El operador autentica con conexión al inicio de turno (PIN de 6 dígitos o biometría del dispositivo) y descarga un token cifrado de vida acotada al turno.
- Durante el turno el PIN desbloquea el token local; no autentica contra el IdP por transacción. No hay dependencia de red en la ruta.
- El dispositivo es un factor de posesión enrolado por MDM; el PIN es el segundo factor. Esto satisface la MFA del Art. 22 sin exigir un segundo dispositivo a alguien que trabaja con guantes.
- Los datos locales están cifrados y admiten borrado remoto selectivo (RF-03.16/06.12): se borra la aplicación y su caché, no la información personal del dispositivo.


#### Gestión de dispositivos


> **Tabla 49** — 4.6 Gestión de dispositivos (MDM) · 6 filas · ver planilla del subdocumento

La gestión de dispositivos se declara en seis capacidades:

- **Enrolamiento.** Alta del dispositivo contra el usuario antes del turno; perfil por rol (preventista, preparador, conductor).
- **Configuración.** Cifrado local obligatorio, PIN obligatorio, bloqueo de pantalla, modo quiosco (aplicación única), actualización de aplicación y de caché de turno.
- **Postura y monitoreo.** Estado de sincronización, batería, versión de aplicación; alertas por dispositivo perdido, almacenamiento bajo o fallo recurrente de sincronización.
- **Seguridad.** Borrado remoto selectivo con revocación de tokens.
- **Inventario.** Registro por IMEI/serie, asignación y estado.
- **Operación.** MDM como servicio gestionado (Android Enterprise o equivalente): el equipo de TI del CLIENTE es de 4 personas y no administra la plataforma localmente.


#### Ciclo de vida de la identidad

- Aprovisionamiento ≤ 24 h desde el alta en recursos humanos o en el proveedor: cuenta, permisos por rol canónico y dispositivo enrolado.
- Baja efectiva en ≤ 24 h desde la desvinculación: revocación de tokens, borrado remoto del dispositivo y revocación de accesos externos.
- Flujo desatendido y auditable, con aprobación del jefe de área, bitácora de aprovisionamiento y revisión semestral de accesos (certificación de identidades).
- Auditoría de identidad con no repudio: creación, modificación, elevación y baja de cuentas, con la retención declarada en la detección, respuesta y evidencia.


#### Accesos privilegiados y cuenta de emergencia

- **PAM con acceso a demanda:** sin acceso interactivo permanente a producción. La operación excepcional se hace just-in-time por AWS Systems Manager Session Manager, con MFA, aprobación y sesión grabada.
- **Cuenta de emergencia (break-glass):** fuera de banda, custodiada en bóveda física con doble firma, para contingencia de indisponibilidad del IdP. Su activación exige procedimiento escrito, notificación inmediata a TI y a la gerencia, registro en cadena de custodia y rotación de credenciales tras el uso. Se prueba dos veces al año junto con el simulacro de recuperación ante desastres.


### Cifrado y gestión de claves


#### En tránsito


> **Tabla 50** — 5.1 En tránsito · 5 filas · ver planilla del subdocumento

El cifrado en tránsito se declara por trayecto:

- **Superficies públicas y portales.** TLS 1.3 con HSTS y precarga; TLS 1.0/1.1 deshabilitados.
- **Servicio a servicio.** mTLS (microsegmentación; sin confianza implícita en la red interna).
- **On-premise ↔ nube.** IPsec/IKEv2 cifrado, BGP, MTU 1436, dos túneles.
- **Borde IoT → nube.** MQTTS 8883 con certificado X.509 por dispositivo.
- **Respaldos y replicación.** TLS 1.3 en tránsito.


#### En reposo


> **Tabla 51** — 5.2 En reposo · 6 filas · ver planilla del subdocumento

Rotación y custodia: claves de datos con rotación anual o ante revocación o compromiso; claves maestras según el calendario del proveedor; rotación en línea, sin degradación del servicio. Los respaldos conservan la versión de clave necesaria para una restauración auditable. Separación de funciones en la custodia de claves: quien administra la plataforma no administra las claves maestras.


#### Cifrado a nivel de campo

El caso lo declara exigible para cuatro conjuntos de datos. Aplicación declarada:


> **Tabla 52** — 5.3 Cifrado a nivel de campo · 4 filas · ver planilla del subdocumento

El cifrado a nivel de campo se declara por conjunto de datos:

- **Comportamiento de pago y antecedentes comerciales del cliente.** Cifrado a nivel de campo con clave en KMS; acceso restringido por rol y registro de consultas.
- **Datos de geolocalización de personas.** Cifrado a nivel de campo, retención 12 meses y registro de consultas. La visibilidad de flota es operativa y no se desliza a control de jornada (D1, objeción sindical L577).
- **Medios de pago electrónicos.** El PAN no se almacena: tokenización en la pasarela; el terminal POS es PCI PTS 7.x.
- **RUT de clientes en bases y registros.** Pseudonimización mediante cifrado a nivel de campo (pgcrypto con clave en KMS).

Gestión de secretos. Los secretos de integración (credenciales del ERP, certificados AS2/EDI, credenciales del SII y de Transbank) se administran en AWS Secrets Manager y SSM Parameter Store, con rotación automática y consumo desde los nodos on-premise por VPC Endpoint saliente, coherente con el principio 4. Prohibición absoluta de secretos embebidos en código, imágenes o archivos de configuración.

Gestor de secretos: servicio administrado, no componente autoalojado. La decisión está fundada en el ADR-15 y su emplazamiento es el componente N-12 de la tabla de emplazamiento. Se descartó un gestor autoalojado on-premise porque habría exigido una máquina virtual adicional en Talca con su alta disponibilidad, respaldo, procedimiento de sellado y licencia, sumando superficie de administración a un equipo de cuatro personas sin beneficio funcional frente al servicio administrado. Todo componente de seguridad de esta arquitectura tiene emplazamiento declarado.


### Clasificación de la información y controles por nivel


> **Tabla 53** — 6. Clasificación de la información y controles por nivel · 4 filas · ver planilla del subdocumento


### Detección, respuesta y evidencia


> **Tabla 54** — 7. Detección, respuesta y evidencia · 11 filas · ver planilla del subdocumento



### Datos personales, residencia y transferencia internacional


> **Tabla 57** — 10. Datos personales, residencia y transferencia internacional · 12 filas · ver planilla del subdocumento

Dos de los resguardos de esta tabla son decisiones de diseño y no solo cláusulas contractuales, y se propagan a la sección de arquitectura de despliegue de este documento y a la arquitectura lógica (Subdocumento 4.1): la minimización, por la que la región secundaria sostiene continuidad y no se explota analíticamente, y la exclusión de los datos de geolocalización de personas de la replicación transfronteriza. La decisión de no replicar la geolocalización de personas tiene además un fundamento del caso: la geolocalización de personas es el dato con la objeción sindical explícita (Restricción no negociable N° 10, Cap. 10 del caso) y con la retención más corta (12 meses); mantenerlo en una sola jurisdicción reduce la superficie legal sin afectar la continuidad, porque no es un dato necesario para reanudar la operación.


#### Derechos de los titulares, política de privacidad y EIPD

**Derechos ARCOP (Ley 21.719).** Acceso, rectificación, supresión, oposición, portabilidad y bloqueo temporal; canal único (correo dedicado + formulario web), plazo de 30 días prorrogable una vez (Art. 11); contraparte: Encargado de Seguridad (BA Art. 27°); bitácora de solicitudes auditada.

**Política de privacidad.** Aviso informativo a titulares (clientes y trabajadores) con: responsable (Distribuidora Puelche S.A.), datos tratados por categoría, finalidades, base de licitud por tratamiento, destinatarios y transferencias, retención por categoría y derechos. Versión preliminar anexada al Informe 1.

**EIPD (BA Art. 27°).** Evaluación de impacto obligatoria por tratamiento masivo (14.200 clientes) y monitoreo sistemático (GPS de ~260 trabajadores). Versión final antes de producción, revisión anual.

**Vigencia.** La Ley 21.719 rige desde el 01-dic-2026; un proyecto de ley (Boletín 18.623-07) postergaría la vigencia al 01-dic-2027. La propuesta es robusta a ambas fechas por diseño.

#### Base de licitud por tratamiento

Cada tratamiento declara su base de licitud conforme a los Art. 12 (consentimiento) y 13 (bases distintas) de la Ley 21.719:

> **Tabla 58** — Base de licitud por tratamiento (Ley 21.719, Art. 12 y 13) · 7 filas · ver planilla del subdocumento

Garantías transversales: RAT como entregable del proyecto (ISO 5.31/5.34); geolocalización y comportamiento de pago tratados como sensibles (cifrado de campo + registro de consultas); consentimiento expreso, informado y revocable donde aplique; eliminación certificada al término del contrato (Art. 85 BA).

### Seguridad física

Los controles de seguridad física (cuatro capas de acceso, biometría, CCTV ≥ 30 días, custodia de medios y control de acceso de terceros) se detallan en la sección del sitio principal de este subdocumento.

## Arquitectura de despliegue

Ambientes, redes, alta disponibilidad, recuperación ante desastres y respaldos. Es autocontenida: los valores que declara se sostienen en los componentes especificados en las secciones anteriores de este capítulo (modelo de emplazamiento, tecnologías ofertadas, implementos y sitios principal y secundario).


### Ambientes de despliegue

Los cinco ambientes obligatorios del numeral 4.1 de las Bases Técnicas Transversales están habilitados como condición del hito H3, aislados entre sí mediante cuentas AWS separadas bajo una organización centralizada de AWS Control Tower (aislamiento estricto + SCP):


> **Tabla 62** — 1. Ambientes de despliegue · 5 filas · ver planilla del subdocumento

Reglas que gobiernan el modelo de ambientes:

- **Paridad Pre-Producción = Producción.** topología, versiones de componentes y configuración equivalentes; las diferencias por costo se declaran y justifican una a una.
- **On-premise como producción.** el despliegue on-premise es producción con la imagen única wms_only; esa misma imagen recorre Dev→QA→PreProd en la nube antes del cutover en Talca (ventana de 24 h) y en Concepción. No se mantienen ambientes on-premise separados — la paridad la garantizan la imagen única y el IaC versionado.
- **Entrega continua.** el pipeline CI ejecuta compilación, pruebas unitarias, análisis estático, análisis de composición, escaneo de secretos y escaneo de imágenes de contenedor, con bloqueo automático del despliegue ante hallazgos críticos o altos.
- **Despliegue sin interrupción.** estrategia azul-verde con canario (despliegue gradual a un porcentaje pequeño de tráfico) en etapas, demostrada en PreProducción antes de cada paso a producción; reversión automatizada.
- **Configuración externalizada.** un mismo artefacto se promueve QA→PreProd→Prod sin recompilación; los secretos viven en gestor de secretos con rotación automática, sin credenciales embebidas.
- **Datos no productivos.** Dev, QA y PreProd usan datos sintéticos generados desde la volumetría del Cap. 14 del caso; las plantillas próximas a producción pasan por anonimización/seudonimización verificable (Amazon Macie).
- **Sin acceso interactivo a producción.** los despliegues son exclusivamente por pipeline; el acceso administrativo excepcional es just-in-time vía AWS Systems Manager Session Manager con MFA, aprobación y sesión grabada.
- **Reducción de ambientes no productivos fuera de horario.** Dev/QA/PreProd se apagan o reducen fuera del horario de uso, con el ahorro reflejado en la estructura de costos.
- **Portal web (N-01/N-02/N-03).** la SPA Angular se publica por ambiente en S3+CloudFront (bucket y distribución por cuenta AWS) y su backend es la misma imagen Django del ambiente; entra a producción con el hito de enero 2029.


### Redes (topología, segmentación y conectividad)


#### WAN — doble camino con conmutación automática

Cada instalación dispone de dos caminos físicamente independientes con conmutación automática en < 30 s: fibra óptica más LTE empresarial en los CDs (Talca y Concepción), y Starlink más LTE empresarial en los cross-docks (Curicó, Chillán y Los Ángeles). El requisito exige ≤ 5 min declarados; el diseño opera en < 30 s. Los anchos de banda por sitio, en régimen y en peak, se declaran en la sección de dimensionamiento (Tabla 81).

Los cross-docks salen directo por Starlink a SQS/IoT/SSM y sincronizan detalle a Talca por AMQPS entre brokers (C-13). La pérdida total del enlace se cubre con la autonomía local de 24 h (CD) / 14 h (terreno), por lo que la redundancia de conectividad reduce la frecuencia de desconexión pero no es condición para operar.


#### VPN Site-to-Site (costura C1)

Extremos: D-01 Firewall/UTM (HA activo-pasivo) → Customer Gateway en cada CD; extremo cloud VGW del VPC Hub.

Protocolo: IPsec/IKEv2 cifrado, BGP, MTU 1436; 2 túneles (activo + standby). Conmutación < 30 s entre los dos caminos del sitio.


#### Segmentación de red (sin solapamiento)


> **Tabla 64** — 2.3 Segmentación de red (sin solapamiento) · 5 filas · ver planilla del subdocumento

Modelo Hub-and-Spoke con VPC de tránsito central: la comunicación cross-VPC pasa por el Transit Gateway (inspección) y los servicios AWS (S3, SQS, DynamoDB, KMS, SSM) se consumen por VPC Endpoints/PrivateLink sin tráfico por internet.


#### Zero Trust — flujos permitidos

Todo el tráfico on-premise → nube es outbound (HTTPS/443, MQTTS/8883) sin conexiones entrantes salvo las dos excepciones controladas D-AL-05 sobre túnel IPsec autenticado:


> **Tabla 65** — 2.4 Zero Trust — flujos permitidos · 9 filas · ver planilla del subdocumento


#### Capa pública (DMZ) y DNS

Primera línea: CloudFront + AWS WAF v2 (OWASP Top 10 + reglas personalizadas) + Shield Advanced; autenticación API Gateway con Keycloak OIDC, cuotas por cliente y validación de esquema.

DNS: Route 53 con health checks activos; routing por latencia en operación normal y failover automático hacia us-east-1 en contingencia.


### Alta disponibilidad


#### Capa cloud (sa-east-1) — Multi-AZ


> **Tabla 66** — 3.1 Capa cloud (sa-east-1) — Multi-AZ · 7 filas · ver planilla del subdocumento

Nivel de servicio de extremo a extremo sobre la transacción crítica de negocio: ≥ 99,9 % mensual (menos de 8,76 h al año). Es el compromiso contractual penalizable del Artículo 78° y es distinto de la disponibilidad de la infraestructura del recinto (99,95 % por componente, numerales 6.1 y 7.2), que es un medio para alcanzarlo.


#### Capa on-premise


> **Tabla 67** — 3.2 Capa on-premise · 7 filas · ver planilla del subdocumento

VMs dimensionadas con headroom ×1,5 para tolerar 3.900 entregas/día en el peak de septiembre. SPOF declarados y mitigados: periféricos de andén (respaldo manual), clúster Talca sin SPOF estructural, Concepción nodo único (autonomía 24 h + DRP), cross-dock mini-PC único (ventana de 3 h + sincronización diferida).


### Recuperación ante desastres


#### DRP nube (sa-east-1 → us-east-1) — activo-pasivo warm standby (réplica pasiva lista para promover en minutos)

Mecanismo: Aurora Global Database (réplica us-east-1, lag < 1 s) · DynamoDB Global Tables · S3 CRR (RTC < 15 min) · AWS DMS CDC del PostgreSQL WMS on-premise (lee wal_level=logical; si la VPN cae, encola y reanuda sin pérdida).

Objetivos: RTO ≤ 4 h / RPO ≤ 15 min; RPO declarado de mensajes no críticos ≤ 24 h, reducido a ≤ 15 min para los críticos con patrón outbox dual-write (escritura simultánea en BD y cola para garantizar consistencia).

Modalidad justificada (RT-07.01): activo-pasivo; activo-activo duplicaría la infraestructura transaccional (~105 TPS peak) con reconciliación de doble escritura sin beneficio frente al RTO comprometido.

Procedimiento: decisión de failover manual con disparador declarado (health check de la región primaria < 5 min) y protección contra conmutación innecesaria (confirmación SNS + autorización); pasos 4–7 automatizados por AWS Systems Manager Automation (promoción Aurora 15–20 min, escalado ECS, actualización DNS 45–60 min). El RTO se cumple porque la réplica es legible y la región DR está "caliente" (escalable < 30 min a carga completa).

Retorno (failback): procedimiento documentado en 6 pasos — re-sincronización con catch-up verificado, reconciliación de transacciones de la contingencia contra la bitácora, transferencia de eventos pendientes, conmutación coordinada de DNS, validación funcional e informe con tiempo real.

Pruebas: conmutación real ≥ 2 veces/año con informe de RTO/RPO efectivos y plan de corrección de brechas.

Residencia y transferencia internacional de datos (Art. 23 · Ley 21.719): la replicación hacia us-east-1 constituye una transferencia internacional de datos personales y se rige por los resguardos declarados en la arquitectura de seguridad: cifrado con CMK gestionada por el CLIENTE, acuerdo de tratamiento con cláusulas de transferencia, minimización (la región secundaria no se explota analíticamente, solo sostiene continuidad), exclusión de los datos de geolocalización de personas de la replicación transfronteriza —permanecen solo en sa-east-1 con retención de 12 meses— y registro en el inventario de tratamientos. La residencia queda sujeta a aprobación expresa del CLIENTE; si no la aprueba, la alternativa declarada es la continuidad intrarregional dentro de sa-east-1 (tercera AZ ampliada + respaldo inmutable regional — no es un segundo sitio geográfico ni usa Talca/Concepción para la carga cloud; AWS no tiene región en Chile), que cubre falla de AZ y corrupción de datos pero degrada el RTO ante una caída de toda la región sa-east-1 (24–72 h desde el respaldo inmutable; alternativa D del ADR-09).


#### DRP local (Talca → Concepción)

Promoción controlada del WMS edge (VM-C01) mediante procedimiento de 5 pasos; Concepción ya opera autónoma (latencia ≤ 1 s de picking, RNF-05.01). RTO +1–2 h para la bodega.

Identidad sin conmutación local: el maestro Keycloak está en la nube y las cachés A-05/VM-C03 siguen validando firmas offline — el DRP de identidad es la misma autoridad en nube, sin promoción local a maestro (elimina una clase entera de riesgos de DR).


#### DRP de la identidad

El maestro vive en la nube (Multi-AZ) con réplica DR us-east-1; las cachés locales son de solo lectura. No existe maestro local a promover, por lo que la identidad no depende del switchover.


### Respaldos — esquema 3-2-1-1-0

Esquema único para toda la arquitectura híbrida (nube + on-premise):


> **Tabla 68** — 5. Respaldos — esquema 3-2-1-1-0 · 5 filas · ver planilla del subdocumento

D-05 (NAS local con WORM) es la copia local de recuperación rápida y NO cuenta como la pierna inmutable; permite restaurar el WMS en ≤ 4 h sin depender del enlace WAN. RPO ≤ 15 min por AWS DMS CDC del WAL lógico (registro de escritura anticipada que permite replicar cambios en tiempo real, wal_level=logical) hacia la nube antes de la copia local.

Custodia física: medio de respaldo transportable, cifrado y rotado semanal, trasladado bajo custodia acreditada a bóveda externa distinta del sitio primario; la pierna inmutable S3 es complementaria, no reemplaza la custodia física.

Plan AWS Backup:


> **Tabla 69** — 5. Respaldos — esquema 3-2-1-1-0 · 6 filas · ver planilla del subdocumento

Vault Lock con enfriamiento de 3 días y retención mínima de 1 año; una vez bloqueado, ni la cuenta raíz puede eliminar respaldos. Retención sanitaria: trazabilidad 5 años + vida útil (D.S. 977/96), consistente con el lago analítico S3 y el repositorio de datos históricos.

## Dimensionamiento y plan de capacidad

Volúmenes, concurrencia, crecimiento y umbrales de desempeño. Cierra las dieciséis dimensiones del numeral 14.2 del caso con su valor, su método y su supuesto.


### Criterios y método de dimensionamiento

El dimensionamiento se deriva de la volumetría real del Caso (Tabla 14.1 / Cap. 14 y 15), no de promedios genéricos, dado el perfil de carga no plano:


> **Tabla 72** — 1. Criterios y método de dimensionamiento · 5 filas · ver planilla del subdocumento

Reglas que gobiernan el dimensionamiento:

- **Carga de diseño.** peak de septiembre (2.600 entregas/día) × 1,5 = 3.900 entregas/día toleradas sin degradación.
- **Transacciones por segundo de diseño.** ráfaga de 3 veces el régimen, unas 105 transacciones por segundo, según se deriva más abajo en la concurrencia.
- **Crecimiento.** la solución soporta tres veces la volumetría inicial sin rediseño en tres años, con la misma topología, según detalla el plan de capacidad.
- **Umbrales.** percentil 95 en toda medición, con un umbral declarado por cada operación.
- **Sin capacidad ociosa financiada.** el cómputo elástico en nube escala automática (ADR-12); el on-premise se dimensiona al margen útil sin sobrecompra.
- **Coherencia interna.** los totales de esta parte concuerdan con la Tabla 14.1 (volumetría) y con el dimensionamiento on-premise y de nube de esta misma sección, y con los ADR (ADR-01, 04, 10, 12 y Decisiones N° 28 y N° 30 del registro de decisiones (Subdocumento 3)).


### Volumetría de referencia (Tabla 14.1 Caso 02)


#### Valores base de dimensionamiento


> **Tabla 73** — 2.1 Valores base de dimensionamiento · 13 filas · ver planilla del subdocumento

Nota de coherencia (instalaciones): la Tabla 14.1 y RT-21.16 reportan 6 instalaciones (7 a tres años); el despliegue físico ubica cómputo en los 5 sitios on-premise listados + borde en terreno (calle y 14.200 puntos). La divergencia entre cinco y seis instalaciones, que enfrenta la tabla de volumetría con el capítulo 8 del caso, está declarada en las consultas al mandante (Art. 43.3) y no altera el dimensionamiento: el cómputo se emplaza en los 5 sitios, la 6.ª instalación es de red/almacenamiento sin nodo de cómputo propio.


#### Proyección a 3 años (Caso 02)


> **Tabla 74** — 2.2 Proyección a 3 años (Caso 02) · 8 filas · ver planilla del subdocumento

Los recursos se dimensionan, además, para 3× la volumetría inicial sin rediseño: la proyección real del Caso a 3 años (+16–19 %) queda muy por debajo del límite de diseño, dejando margen ante crecimiento mayor al modelado.


#### Volumetría de sistema del numeral 14.2 — las dieciséis dimensiones

El numeral 14.2 del caso entrega dieciséis dimensiones a estimar y advierte que un dimensionamiento basado en el promedio diario estará equivocado. Las dieciséis se declaran a continuación con su valor, su método y el supuesto que las sostiene. Ninguna queda sin valor.

| Dimensión del numeral 14.2 | Valor declarado | Método y supuesto |
|---|---|---|
| Transacciones por segundo en régimen normal | ≈ 35 TPS | Suma de flujos concurrentes de la peor ventana: 20 TPS de confirmación de preparación, 8 TPS de preventa y 7 de movimientos y sincronización |
| Transacciones por segundo en el peak de la ventana de despacho 05:30–07:00 | ≈ 1,7 TPS en ráfaga | 1.400 confirmaciones de carga, 1.400 timbrados de guía, 96 vinculaciones conductor–camión y 96 cierres de ruta, concentrados en los primeros 20 minutos de la ventana. La ventana es crítica por indisponibilidad cero, no por volumen: el cuello de botella está en la preparación nocturna |
| Transacciones por segundo en el peak de septiembre | ≈ 105 TPS | 35 TPS × burst 3, que cubre el doble de volumen estacional más la ráfaga de sincronización de flota de 17:00 a 20:00 |
| Personas usuarias registradas, internas y externas | ≈ 620 internas · ≈ 14.400 externas | Internas: 62 preventistas, 42 conductores propios, ≈ 160 conductores de terceros, 310 personas de centro de distribución, ≈ 40 de administración y gerencia, 4 de TI. Externas al cierre de la Etapa 2: 14.200 clientes con autoatención, 180 proveedores y 10 transportistas |
| Personas usuarias concurrentes en peak | ≈ 510 | 62 preventistas + ≈ 200 conductores + 120 terminales de preparación + 110 estaciones de centro de distribución + ≈ 20 de supervisión y mesa, según la ventana de solapamiento |
| Dispositivos de terreno en operación simultánea | ≈ 270, hasta ≈ 300 en peak | Parque de terminales de preventa, reparto y cámara con un 20 % de reserva |
| Volumen anual de almacenamiento transaccional | ≈ 375 GB/año | Crecimiento del maestro de bodega y del transaccional de nube desde los 1.890 GB asignados hacia los 5,7 TB proyectados a cinco años |
| Volumen anual de almacenamiento de evidencia de entrega, firmas y fotografías | ≈ 100 GB/año | 420.000 entregas al año × ≈ 230 KB por entrega (una firma de ≈ 30 KB más una a dos fotografías comprimidas de ≈ 200 KB), más la evidencia de las ≈ 900 devoluciones mensuales. Con retención de 6 años y almacenamiento por niveles, ≈ 600 GB al término del contrato |
| Volumen anual de almacenamiento de series de temperatura y de posicionamiento | ≈ 3,3 GB/año en crudo · ≈ 0,8 GB/año consolidado | Temperatura: 46 fuentes × 1 muestra cada 5 min × 365 días. Posicionamiento: 42 camiones × 1 posición cada 30 s × 12 h × 300 días. El crudo vive 30 días con expiración automática y la serie consolidada se conserva en formato columnar comprimido: 5 años para temperatura y 12 meses para geolocalización de personas |
| Volumen total de datos históricos a migrar | ≈ 30 GB de datos estructurados | Maestros completos (14.200 clientes, 8.400 productos, 180 proveedores), ventas y pedidos de 3 años (≈ 9,4 millones de líneas × ≈ 1 KB), movimientos de inventario de 2 años (≈ 3,4 millones × ≈ 0,5 KB), trazabilidad sanitaria de 5 años y cuentas por cobrar vivas más 2 años. El histórico documental permanece en el sistema de gestión, que sigue siendo la fuente tributaria |
| Número de integraciones y volumen de mensajes por integración | 15 integraciones · ≈ 150.000 mensajes/día | El desglose por integración está en la arquitectura de integración, derivado de la volumetría del caso sobre 25 días hábiles |
| Ancho de banda requerido por sitio, en régimen y en peak | Talca 20→50 Mbps · Concepción 10→20 Mbps · cross-docking por enlace satelital | Dimensionado sobre el tráfico de sincronización, telemetría y respaldo por sitio, con conmutación automática en menos de 30 s |
| Volumen de datos generado por un dispositivo de reparto en un turno completo sin señal | ≈ 8–12 MB por turno | Ruta del día, maestro acotado de productos y precios, evidencia de entrega comprimida de ≈ 30 entregas y cola de escrituras pendientes |
| Tiempo de sincronización de la flota al regresar al centro de distribución | ≤ 10 min para el 100 % de la flota | ≈ 200 dispositivos × 10 MB sobre el enlace del sitio, con sincronización particionada y reanudable; la ventana real de retorno es de 17:00 a 20:00, muy por encima del objetivo |
| Contactos mensuales a la mesa de ayuda | ≈ 620/mes en régimen · ≈ 1.500/mes en marcha blanca | 620 personas usuarias internas × 1,0 contacto/mes en operación estabilizada, con factor 2,5 durante las oleadas de puesta en producción y +40 % en el peak de septiembre. Los clientes del canal tradicional no entran por esta mesa: se atienden por autoatención |
| Dotación de la mesa de ayuda y del equipo de operación | Mesa: 7 personas · Operación: NOC y confiabilidad como servicio gestionado | Erlang C sobre la hora punta: ≈ 5 contactos/h con tiempo medio de operación de 8 min dan una intensidad de 0,67 Erlang, y 2 agentes cumplen el objetivo de 80 % atendido en 20 s. A eso se suman la cobertura de la ventana 05:30–07:00 y del turno nocturno de bodega, el segundo nivel y la supervisión: 3 agentes diurnos, 1 nocturno, 1 supervisor y 2 especialistas de segundo nivel |

Dos lecturas se desprenden de la tabla y gobiernan el diseño. La primera: el volumen de mensajes está dominado por las dos series de tiempo —trazabilidad y telemetría, ≈ 112.000 de los ≈ 150.000 mensajes diarios— que por diseño no atraviesan la base transaccional. La segunda: la ventana crítica de despacho no es la de mayor carga, sino la de menor tolerancia a la indisponibilidad; el dimensionamiento del cómputo se rige por la preparación nocturna y el peak de septiembre, y el de la resiliencia por la ventana de despacho.


### Concurrencia y TPS de diseño


#### Usuarios y terminales concurrentes


> **Tabla 75** — 3.1 Usuarios y terminales concurrentes · 7 filas · ver planilla del subdocumento


#### TPS estimados (peor ventana)


> **Tabla 76** — 3.2 TPS estimados (peor ventana) · 4 filas · ver planilla del subdocumento

El burst ×3 absorbe el peak de septiembre y las ráfagas de la ventana de sincronización 17:00–20:00. Los ≈ 105 TPS son el valor único de diseño de esta parte, citado por el ADR-01 y el ADR-12, y sustenta el dimensionamiento de operaciones de entrada y salida de la base transaccional y el escalado del cómputo en nube.


### Dimensionamiento on-premise


#### Cómputo — CD Talca (clúster N+1, 3 nodos Proxmox/Ceph)


> **Tabla 77** — 4.1 Cómputo — CD Talca (clúster N+1, 3 nodos Proxmox/Ceph) · 3 filas · ver planilla del subdocumento

Máquinas virtuales del clúster de Talca, con las familias declaradas más arriba en este mismo apartado:


> **Tabla 78** — 4.1 Cómputo — CD Talca (clúster N+1, 3 nodos Proxmox/Ceph) · 6 filas · ver planilla del subdocumento


#### Cómputo — Concepción (edge) y cross-docking


> **Tabla 79** — 4.2 Cómputo — Concepción (edge) y cross-docking · 2 filas · ver planilla del subdocumento


#### Almacenamiento


> **Tabla 80** — 4.3 Almacenamiento · 4 filas · ver planilla del subdocumento


#### Ancho de banda WAN por sitio


> **Tabla 81** — 4.4 Ancho de banda WAN por sitio · 3 filas · ver planilla del subdocumento

Estos valores son los mismos que declara la arquitectura de despliegue al describir las redes, con red privada virtual doble por centro de distribución.


### Dimensionamiento nube


> **Tabla 82** — 5. Dimensionamiento nube · 9 filas · ver planilla del subdocumento

Escalado automático:

- **Predictivo + reactivo (ADR-12).** pre-warm en agosto de las tareas ECS, concurrencia reservada Lambda y EventBridge; reactivo con Target Tracking en < 2 min · aprovisionamiento en < 3 min · cooldown 60 s.
- **Serverless-first.** DynamoDB On-Demand, Lambda y EventBridge escalan sin configuración adicional; la capacidad se paga por uso (sin capacidad ociosa financiada).


### Plan de capacidad y crecimiento 3× sin rediseño

El crecimiento se absorbe con el mismo diseño (sin cambio de topología, VLAN, réplica ni nube):


> **Tabla 83** — 6. Plan de capacidad y crecimiento 3× sin rediseño · 5 filas · ver planilla del subdocumento

En nube, el 3× se absorbe por auto-scaling (Fargate 2→6, Celery 2→4, Lambda hasta 500, Aurora xlarge + readers), sin rediseño arquitectónico — misma decisión ADR-12 que fija el límite de elasticidad del peak.


### Umbrales de desempeño


> **Tabla 84** — 7. Umbrales de desempeño (percentil p95) · 7 filas · ver planilla del subdocumento

Los umbrales se verifican con monitoreo CloudWatch y se prueban en preproducción con las pruebas de carga y estrés.


### Primer cuello de botella

VM-02 (PostgreSQL — escritura transaccional del maestro de bodega) se satura primero a medida que crece la carga: todo el picking (22:00–06:00) y el despacho masivo (05:30–07:00) pasan por el único punto de escritura.


> **Tabla 85** — 8. Primer cuello de botella · 1 fila · ver planilla del subdocumento

En nube el equivalente es Aurora (writer + readers); EventBridge/SQS absorben el pico de sincronización 17:00–20:00 (ADR-05).


### Degradación controlada

Enlace WAN: QoS prioriza broker/WAL; colas diferidas fuera de la ventana; conmutación automática < 30 s entre los dos caminos del sitio.

Offline: buffers RabbitMQ de 24 h y buffers OTel de 24 h; reconciliación cronológica e idempotente al reconectar.

Nube: throttling en API Gateway, timeouts y reintentos con backoff en Celery, DLQ para tareas fallidas.


### Pruebas de carga y estrés


> **Tabla 86** — 10. Pruebas de carga y estrés · 3 filas · ver planilla del subdocumento

Herramientas: k6/Gatling + drivers a medida contra las APIs (svc-erp-integration, svc-broker). Cortes: Etapa 1 (mes 13), Etapa 2 (mes 19), re-ejecución trimestral. Calendario e hitos formales en el Formulario T-13.


### Actualización del plan de capacidad

Gestión de capacidad durante la Operación con proyección trimestral de crecimiento: consumo real vs. proyectado (vCPU/RAM/almacenamiento/enlace/colas/TPS), con alertas anticipadas de agotamiento al 70 % / 2 semanas y propuesta de ajuste de dimensionamiento y de costo.

Ventana de ampliación conforme al procedimiento de ampliación (adición de vCPU/OSD dentro del físico; contrato escalonado de enlaces; 4.º nodo al acercarse al margen). La revisión se apoya en el informe de carga como insumo del hito de producción (mes 16).

En nube, la revisión de costos del dimensionamiento elástico evalúa umbrales Target Tracking y concurrencia reservada con al menos 30 días antes del peak de septiembre.

## Registro de decisiones de arquitectura

Registro consolidado de las quince decisiones de arquitectura que condicionan esta propuesta. Es entregable contractual conforme a RT-02.04 y se mantiene actualizado durante toda la ejecución. Para cada decisión se indica la alternativa escogida, las alternativas descartadas con el motivo de rechazo, y el criterio de selección. Todas las decisiones fueron aprobadas entre el 05 y el 06 de septiembre de 2026.


### ADR-01 · Estilo arquitectónico

**Decisión adoptada.** Monolito modular Django 5.x LTS / Python 3.12, desplegado en ECS Fargate con apps por dominio y límites de contexto DDD. Módulos críticos (WMS offline, shipper, workers, portal) en procesos separados.

**Alternativas descartadas.** *Microservicios EKS*: 20+ servicios con mesh Istio; rechazada porque el volumen (~105 TPS, 31 K pedidos/mes) está dos órdenes de magnitud bajo el umbral que los justifica, y 4 personas no operan 9–13 componentes de plano de control. TCO +USD 40–70 K en 56 meses sin beneficio funcional. *Monolito clásico (WMS 2013)*: sin fronteras de módulo, proveedor desaparecido; viola RT-02.02.

**Criterio de selección.** Pertinencia al volumen real (BTT §2.3); operabilidad por 4 personas; TCO 56 meses; despliegue independiente de componentes críticos sin particionar el dominio. Trazabilidad: RT-02.01/02.02/02.03 · RT-09.05 · BA Art. 16 · RNF-19.01–04. Relacionada: D5, D8, D14 (Arq. Lógica).

### ADR-02 · Conectividad WAN

**Decisión adoptada.** Doble camino por sitio: fibra + LTE en los centros de distribución, Starlink + LTE en los cross-docking. Conmutación automática < 30 s.

**Alternativas descartadas.** *Fibra en cross-docks*: naves industriales sin cobertura de fibra; costo de obra desproporcionado. *VSAT GEO*: latencia 500–700 ms RTT; penaliza RNF-05.01 y costo superior. *Tri-camino (fibra + Starlink + LTE)*: tercer camino no aporta disponibilidad significativa dado que cada sitio opera autónomamente ante pérdida total de enlace (24 h CD, 14 h terreno).

**Criterio de selección.** Dos caminos de física distinta satisfacen RT-03.17 sin punto único de fallo; la autonomía local cubre la pérdida total de enlace, por lo que un tercer camino es innecesario; cero mantención de radio para 4 personas. Trazabilidad: RT-03.10/03.17 · RT-10.05 · RNF-13.01/13.07/13.08 · Caso Cap. 6.12/8. Relacionada: Decisión 16.1 N° 26.

### ADR-03 · Modelo de despliegue híbrido

**Decisión adoptada.** Borde operacional on-premise (WMS maestro Talca, edge Concepción, WMS en cross-docks) + carga principal en AWS (ECS, Aurora, IoT, analítica, respaldo). 11 componentes on-prem, 12 híbridos, 13 nube pura.

**Alternativas descartadas.** *Solo nube*: inadmisible (Art. 16); sin enlace la bodega muere en minutos; picking en cámara −22 °C inviable con RTT 40–80 ms. *Solo on-premise*: inadmisible (Art. 16); no cumple carga principal en nube.

**Criterio de selección.** Único modelo que satisface Art. 16 en sus 4 numerales; latencia ≤ 1 s en cámara resuelta localmente; autonomía 24 h CD / 14 h terreno; TCO contenido delegando a servicios administrados AWS. Trazabilidad: BA Art. 16.1–16.4 · RT-03.01/03.02/03.10/03.19 · RNF-02.01/05.01/05.02. Relacionada: D7 (Arq. Lógica) · Decisión 16.1 N° 17.

### ADR-04 · Persistencia políglota

**Decisión adoptada.** PostgreSQL+PostGIS (transaccional WMS, CP), Aurora (OLTP cloud + DRP), DynamoDB (IoT raw, AP, TTL 30 d), S3+Redshift Serverless (OLAP + series de temperatura), S3 Object Lock/Glacier (retención legal 5 años).

**Alternativas descartadas.** *Motor único relacional*: no escala la ingesta IoT sin degradar picking (RNF-11.02). *InfluxDB para series de tiempo*: segundo motor exótico a operar; la serie consolidada cabe en la capa OLAP. *DynamoDB para todo*: no ofrece ACID cross-tabla para reconciliación determinista.

**Criterio de selección.** Posición CAP declarada por dominio (RT-05.02); 3 motores administrados operables por 4 personas; retención sanitaria D.S. 977/96 con inmutabilidad; RPO ≤ 15 min por réplica Aurora. Trazabilidad: RT-05.01/05.02/05.11–15 · RNF-09.01/09.02/11.02 · D.S. 977/96. Relacionada: D2, D4 (Arq. Lógica) · Decisión 16.1 N° 18.

### ADR-05 · Mensajería asíncrona

**Decisión adoptada.** RabbitMQ local por sitio (buffer 24 h) + shipper idempotente → SQS FIFO (VPC Endpoint outbound) + EventBridge (eventos de negocio) + IoT Core MQTT (ingesta edge).

**Alternativas descartadas.** *REST síncrono*: no sobrevive corte a mitad de ventana; rompe la reconciliación. *Kafka/MSK*: aporta orden y durabilidad pero operar clústeres en 5 sitios es desproporcionado para 4 personas y 105 TPS.

**Criterio de selección.** Resiliencia offline (buffer local + reproducción idempotente al reconectar); reconciliación determinista RT-03.12; Zero Trust (todo outbound, sin puertos entrantes); TCO proporcional al volumen. Trazabilidad: RT-02.06/02.07 · RT-03.10/03.12 · RNF-07.01/13.01 · BA Art. 21. Relacionada: D4 (Arq. Lógica).

### ADR-06 · Identidad híbrida (Modelo B)

**Decisión adoptada.** Keycloak IdP maestro en AWS (ECS Fargate, 2 tareas Multi-AZ, backend Aurora) + caché local solo lectura (TTL 8 h) en Talca y Concepción. Tokens offline por perfil (8 h bodega, 14 h reparto). OTP para conductores externos.

**Alternativas descartadas.** *IdP solo nube (Cognito/Auth0)*: paraliza la bodega ante corte de enlace. *AD maestro local + réplica cloud*: duplica administración de identidad, crea maestro a promover en DR. *Keycloak maestro local*: la nube no puede autenticar si el enlace cae en sentido inverso.

**Criterio de selección.** Autonomía offline sin maestro local a promover; autoridad única en nube (DR de identidad = misma instancia); OTP sin correo para externos (RT-12.12); MFA Art. 22; operado por 4 personas sin directorio propietario. Trazabilidad: RT-12.10/12.11/12.12 · RT-03.10 · RNF-13.01 · BA Art. 22 · RF-15.01–05 · RF-06.08. Relacionada: D6 (Arq. Lógica) · Decisión 16.1 N° 34.

### ADR-07 · Movilidad de terreno

**Decisión adoptada.** App nativa Android Kotlin para preventa, reparto y picking. Persistencia local SQLite/Room, SDK Zebra DataWedge (GS1 + QR), impresión BT (ZQ620), POS PAX. Dispositivos Rugged: EC55, TC58e, MC9400 Cold Storage.

**Alternativas descartadas.** *PWA*: no controla SDK de escáner Zebra de forma fiable ni persiste un turno completo sin capa nativa. *Híbrida Flutter*: runtime intermedio degrada interacción con periféricos industriales (escáner, impresora, POS).

**Criterio de selección.** Control nativo de periféricos industriales (DataWedge intents); offline total 14 h con sincronización < 10 min; UI para guantes −22 °C, una mano, lluvia; curva de aprendizaje ≤ 2 h; un mismo artefacto cubre los 3 perfiles de terreno. Trazabilidad: RT-13.08 · RT-12.11 · RT-03.19 · RNF-05.02/05.03/06.01 · RF-06.11–13. Relacionada: Decisión de proyecto N° 19.

### ADR-08 · Destino del WMS legado 2013

**Decisión adoptada.** Reemplazo total en Etapa 1 por módulo WMS del monolito (ADR-01), desplegado en Talca (maestro), Concepción (edge) y cross-docks (sobre E-01). Migración por dominio, oleadas por sitio, plan de reversión azul-verde.

**Alternativas descartadas.** *Mantener e integrar*: proveedor desaparecido, sin soporte ni roadmap; no soporta multi-sitio, picking FEFO (primero en expirar, primero en salir), SSCC GS1 ni conteo cíclico ciego. *Extender a otros sitios*: arrastra riesgo de soporte inexistente en ventana crítica 05:30–07:00.

**Criterio de selección.** Requisitos funcionales (RF-02.x) que el WMS 2013 no contempla; riesgo operacional inaceptable de sistema sin soporte; TCO amortizado con reducción de conteo 2,3 %→~0,3 % y merma 1,7 %→<1 %; reversión garantizada por despliegue azul-verde. Trazabilidad: RT-05.11–15 · RT-03.10 · RNF-02.01/05.01 · Caso 16.1 N° 14. Relacionada: Decisión 16.1 N° 14 (delegada por el CLIENTE).

### ADR-09 · Estrategia DR

**Decisión adoptada.** Activo-pasivo warm standby multi-región: réplica continua DMS CDC + Aurora WAL hacia us-east-1; DRP local Talca→Concepción (RTO +1–2 h); pruebas reales 2×/año; respaldo 3-2-1-1-0 con S3 Object Lock.

**Alternativas descartadas.** *Activo-activo*: duplica infraestructura transaccional y exige reconciliación de doble escritura para ~105 TPS sin beneficio medible frente al RTO comprometido. *Backup + restore frío*: RTO 24–72 h, incumple RNF-20.06. *Solo intrarregional (sin us-east-1)*: mantiene RTO ≤ 4 h ante falla de AZ pero no ante caída de toda la región; se declara como postura mínima si el CLIENTE no aprueba Art. 23.

**Criterio de selección.** RTO ≤ 4 h / RPO ≤ 15 min; proporcionalidad al volumen (activo-pasivo); DR de identidad resuelto en nube (ADR-06); pruebas semestrales reales con informe. Trazabilidad: RT-07.01/07.07 · RNF-20.06/20.07 · BA Art. 20. Relacionada: Decisión 16.1 N° 27.

### ADR-10 · Almacenamiento on-premise y RAID

**Decisión adoptada.** RAID 10 NVMe para BD transaccional del WMS (VM-02); RAID 6 con hot-spare para evidencia POD, logs y rollups; hipervisor Ceph N+1 para redundancia de infraestructura.

**Alternativas descartadas.** *RAID 5*: en discos de 8–16 TB la probabilidad de URE durante rebuild no es despreciable; solo tolera 1 fallo. *RAID 1 puro para todo*: sobre-costo del 50 % aplicado a datos no críticos sin beneficio proporcional.

**Criterio de selección.** IOPS deterministas en ventana de despacho (>100 K IOPS vs. ~840 necesarios); tolerancia a fallo de disco (RNF-13.04) con justificación del nivel RAID (RNF-13.05); TCO contenido aplicando RAID 10 solo a lo transaccional. Trazabilidad: RT-03.14 · RNF-13.03/13.04/13.05. Relacionada: Decisión 16.1 N° 28.

### ADR-11 · Integración B2B/EDI canal moderno

**Decisión adoptada.** Hub EDI centralizado GS1 (EANCOM/GS1 XML + EPCIS) en nube, con conector configurable por cadena, tabla de equivalencias GTIN (RF-12.03), bandeja de excepciones (RF-12.06) y Capa Anticorrupción hacia ERP/GDE. Canal moderno operativo ≤ enero 2029.

**Alternativas descartadas.** *Conectores punto-a-punto por cadena*: multiplica adaptadores, duplica lógica de mapeo, dispara mantenimiento ante cada cambio de especificación de cadena. *EDI delegado al ERP*: expone frontera frágil del ERP que no se reemplaza; viola Zero Trust (escritura directa desde cadena).

**Criterio de selección.** Estandarización GS1 (Cap. 16.2); esfuerzo marginal por cadena nueva (configuración, no código); aislamiento del ERP por ACL (Zero Trust, BA Art. 21); plazo contractual enero 2029. Trazabilidad: RT-05.23 · RT-16.16/16.17 · RNF-12.01 · RF-12.03/12.06 · Caso Cap. 16.2. Relacionada: RF-12 · RF-01.10.

### ADR-12 · Absorción del peak de septiembre

**Decisión adoptada.** Cómputo elástico: Fargate 2→6, Celery 2→4, Lambda 100→500, Aurora large→xlarge +2 readers, DynamoDB on-demand. Escala predictiva por calendario + reactiva (CPU, cola, TPS). Base con Savings Plan, peak con cómputo efímero.

**Alternativas descartadas.** *Capacidad fija al peak*: paga 12 meses la capacidad de 3 semanas; sobredimensionar para el promedio es error declarado por el caso. *Solo escala reactiva*: el burst de septiembre es predecible; la escala reactiva sola introduce lag de minutos en la ventana crítica.

**Criterio de selección.** Perfil no plano calculado al peak ×1,5 (RNF-19.04); cuello de botella identificado (RT-09.05) en persistencia transaccional + ingesta de flota; FinOps (RT-03.06): base reservada + peak efímero; congelamiento de cambios 1–25 sept y diciembre (RT-10.05). Trazabilidad: RT-09.05 · RT-03.06/03.08/03.09 · RNF-19.01–04 · RT-10.05. Relacionada: Decisión 16.1 N° 30.

### ADR-13 · Puerta de enlace de servicios

**Decisión adoptada.** Amazon API Gateway como Capa 3 única: autorizador OIDC (Keycloak), validación de esquema OpenAPI, cuotas y límites de tasa por actor/ruta, versionado /v{major}, propagación de transaction_id a Capa 8.

**Alternativas descartadas.** *Kong Gateway autoadministrado*: agrega componente crítico a parchar y dimensionar en la ruta de la venta; riesgo en ventana 05:30–07:00 con 4 personas. *Desarrollo propio (middleware Django)*: sin cuotas/rate-limit nativos; viola Art. 21.2.

**Criterio de selección.** Cumplimiento literal del Art. 21.2 (autenticación, autorización, cuotas, validación de esquema, inspección de carga) sin desarrollo propio; servicio administrado para 4 personas; coherencia entre vistas (Art. 16.4); reversibilidad por contratos OpenAPI/AsyncAPI estándar. Trazabilidad: BA Art. 21.2 · RT-02.01/02.02 · RT-11.11 · RT-05.16/05.18 · Art. 16.3. Relacionada: D8 (Arq. Lógica).

### ADR-14 · Plataforma de observabilidad

**Decisión adoptada.** Plataforma única en nube: instrumentación OpenTelemetry, colectores ADOT on-premise con buffer 24 h en disco, logs en CloudWatch Logs (12+24 meses), métricas en CloudWatch Metrics (13 meses) y trazas en CloudWatch con retención declarada. Tableros nativos de CloudWatch para operación.

**Alternativas descartadas.** *Prometheus+Grafana+Loki autoadministrado local + plataforma cloud*: constituye dos plataformas (viola Art. 16.4 y RT-03.16 que exigen «la misma»); VM-06 no tiene capacidad para sostenerlo. *AMP + X-Ray + Grafana*: cuatro servicios de observabilidad para un equipo de 4 personas; complejidad operativa desproporcionada sin ganancia funcional sobre CloudWatch nativo.

**Criterio de selección.** Art. 16.4 y RT-03.16 piden una plataforma, no dos; buffer ADOT resuelve «sin puntos ciegos» durante corte; ninguna decisión de la ventana 05:30–07:00 depende de un tablero; CloudWatch es nativo de AWS y no requiere infraestructura adicional; 4 personas no operan servidores de observabilidad. Trazabilidad: BA Art. 16.4 · RT-03.16 · RT-14.01–09 · RT-09.01 · Art. 16.3. Relacionada: D14 (Arq. Lógica).

### ADR-15 · Gestión de secretos

**Decisión adoptada.** AWS Secrets Manager (secretos con rotación: ERP, SII, Transbank, certificados AS2/EDI) + SSM Parameter Store (config no sensible). Consumo outbound por VPC Endpoint. Cifrado con CMK KMS y separación de funciones. Cuenta de emergencia en sobre sellado offline.

**Alternativas descartadas.** *HashiCorp Vault autoadministrado*: modo sellado tras reinicio exige intervención humana de madrugada; agrega infraestructura a operar. *Sin gestor centralizado (secretos en variables/archivos)*: prohibido por Art. 21.4.

**Criterio de selección.** Componente debe existir en la vista física (estaba declarado pero no emplazado); servicio administrado para 4 personas sin desellado manual; Zero Trust intacto (consumo outbound); separación de funciones Art. 21.2 vía IAM/CloudTrail; contingencia offline independiente de la nube. Trazabilidad: BA Art. 21.4/21.2 · Art. 16.2/16.3 · RT-04.09 · RT-11.09. Relacionada: D13, SEC-01 (Arq. Lógica).


