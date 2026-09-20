# Capítulo 4 · Arquitectura Física y de Despliegue de la Solución (Parte 4.2) {-}


## Visión general de la arquitectura física

La solución se despliega en dos dominios que se reparten el trabajo según lo que cada uno hace mejor. La carga principal —el núcleo transaccional de preventa, reparto y canal moderno, la integración, la analítica y el almacenamiento consolidado— corre en nube pública, sobre una región primaria en Sudamérica y una región secundaria en otro continente que sostiene la recuperación ante desastres. Los componentes on-premise cargan con lo que no puede depender de un enlace: la recepción, la preparación y el despacho de los centros de distribución, y la operación de terreno en 14.200 puntos de entrega.

Ese reparto no es una preferencia de diseño, sino la respuesta a tres hechos del caso. La fibra de los centros se corta unas cuatro veces al año. Hay rutas rurales donde el conductor recupera cobertura recién al regresar. Y entre las 05:30 y las 07:00 salen 96 camiones sin que exista plan manual que los reemplace. De ahí los tres compromisos que gobiernan todo lo demás: el centro de distribución opera veinticuatro horas seguidas sin enlace, el terminal de terreno opera un turno completo de catorce horas sin señal, y la ventana de despacho no admite indisponibilidad.

La red de instalaciones es de seis sitios en cuatro regiones. Cinco alojan cómputo —el centro de distribución de Talca, que es la sala técnica principal; el de Concepción, con gabinete de borde; y las tres plataformas de cross-docking de Curicó, Chillán y Los Ángeles— y el sexto es la casa matriz, contigua al centro principal, que no procesa operación logística y consume la nube a través del portal y del back office. El capítulo 8 del caso menciona cinco instalaciones mientras que su tabla de volumetría y el requisito de traslado a sitios alejados declaran seis: la divergencia se eleva como consulta al mandante y no altera el dimensionamiento, que se calcula sobre los cinco sitios con cómputo. La proyección del caso a tres años incorpora un séptimo sitio, que se absorbe por parametrización y con el gabinete de crecimiento ya reservado en la sala, sin obras adicionales.

Cuatro decisiones estructurales se desprenden de ahí y se desarrollan en las secciones siguientes:

- La identidad tiene una autoridad única en la nube y cachés locales de solo lectura. No existe un segundo maestro on-premise que haya que promover, de modo que un corte prolongado nunca abre la posibilidad de dos verdades de identidad.
- Ningún nodo on-premise acepta conexiones entrantes. Todo el tráfico se inicia desde adentro hacia la nube, con dos excepciones controladas que viajan por el túnel cifrado.
- Cada sitio dispone de tres caminos de comunicación de tecnologías y proveedores distintos —fibra, satelital y red móvil— con conmutación automática en menos de treinta segundos.
- El respaldo es uno solo para los dos dominios: copia local de recuperación rápida, copia inmutable en la nube, réplica en la región secundaria y custodia física externa.

La arquitectura se describe conforme a la norma ISO/IEC/IEEE 42010 sobre el marco TOGAF, y es coherente con la arquitectura lógica de la parte 4.1: las mismas capas, los mismos módulos y el mismo conjunto de tecnologías. La correspondencia entre cada requisito de las Bases y el lugar preciso de este capítulo donde se resuelve está en la última sección, Trazabilidad normativa; el pronunciamiento formal sobre la totalidad de los requisitos se entrega en el Formulario T-12.


## Modelo de emplazamiento híbrido


> **Tabla 21** — Modelo de Emplazamiento Híbrido · 6 filas · ver planilla del subdocumento

La justificación componente por componente conforme a los criterios del Art. 16.2 (latencia, criticidad operacional, volumen de datos, restricciones regulatorias, disponibilidad de conectividad y costo total de propiedad) se desarrolla en la tabla de emplazamiento componente por componente que acompaña a esta parte: 36 componentes, 11 on-premise puros, 12 híbridos con pieza en ambos dominios y 13 servicios administrados de nube pura (serie N-01…N-13).


![Modelo de Emplazamiento Híbrido](../Diagramas/ARQF-01_Modelo_emplazamiento_hibrido.png)

Figura 15. Modelo de Emplazamiento Híbrido.


### Instalaciones de la red on-premise

La red on-premise se compone de seis instalaciones (Tabla 14.1 y RT-21.16):

- **CD Talca (sala técnica principal, sala blanca de 32 m²).** clúster WMS de 3 nodos, base transaccional on-premise (PostgreSQL 16, VM-02), broker local RabbitMQ (VM-03), capa anticorrupción del ERP (VM-04), caché de identidad (VM-05), telemetría (VM-06), respaldo NAS (D-05) y componentes de sala (UPS N+1, generador 12 kVA con estanque 24 h, clima N+1, seguridad física).

- **CD Concepción (9.000 m², gabinete de borde).** servidor de borde con el WMS en modo reducido (VM-C01), base local (VM-C02), caché de identidad (VM-C03), broker + telemetría (VM-C04) y Gateway IoT Greengrass (B-02); opera 24 h de forma autónoma e independiente de Talca.

- **Cross-docking de Curicó, Chillán y Los Ángeles.** nodo de cómputo industrial (E-01) con mini-WMS y broker local, enlace principal Starlink (D-06) y respaldo LTE dual (2 proveedores).

- **Casa matriz y oficinas centrales (Talca).** sin nodo de cómputo propio; acceso a la nube para administración, planificación y portal de clientes (RT-03.22).

La proyección a 3 años (RT-02.12) incorpora una séptima instalación; el gabinete de crecimiento de la sala (R04) absorbe esa expansión sin obras adicionales en el sitio principal.


## Tecnologías de software ofertadas

Las tecnologías se eligen bajo los criterios de neutralidad tecnológica, soporte vigente por los 56 meses contractuales (RT-03.05) y preferencia por servicios administrados y componentes de código abierto con estándares abiertos (RT-03.07), de modo que el CLIENTE conserve la reversibilidad de la solución:


> **Tabla 22** — Tecnologías de Software a Utilizar · 15 filas · ver planilla del subdocumento


### Integración con el ERP y documentos tributarios

El ERP de 2017 no se reemplaza ni se modifica (Cap. 10 del caso): permanece como única fuente de verdad tributaria. La solución entrega los datos de operación a través de la capa anticorrupción (ACL, VM-04) y el ERP emite los documentos tributarios (guía de despacho electrónica, factura, boleta y nota de crédito con folios SII), con acuse de recibo con efectos legales —una sola verdad, un solo emisor. El acceso desde la nube a este ERP ocurre únicamente vía la ACL (celery-erp-sync → ACL, nunca escritura directa).


## Implementos a proveer: hardware y software

El inventario ofertado se agrupa en infraestructura de cómputo y almacenamiento, red y seguridad, dispositivos de terreno y operación, y componentes de sala. Son especificaciones que el CLIENTE adquiere y el adjudicatario instala, integra y mantiene (Art. 14.2). Las cantidades y justificaciones de cada fila se referencian al Formulario T-11.


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

**Tipología declarada (numeral 6.1 de las Transversales): sala técnica principal.** El CD Talca aloja el núcleo del componente on-premise —motor WMS, base transaccional del maestro de bodega, broker de colas, capa anticorrupción del ERP, caché de identidad, telemetría y respaldo local—, es decir cómputo, almacenamiento y procesamiento sustantivos en instalaciones del CLIENTE. Por eso se le aplican íntegramente los requisitos RT-06.01 a RT-06.34, y no el régimen proporcional de una sala de sitio.

**Disponibilidad de infraestructura comprometida: 99,95 % mensual**, conforme al numeral 6.1 y a la tabla del numeral 7.2 de las Transversales, medida por componente: energía del recinto, climatización, red y comunicaciones, servidores y cómputo, y motor de base de datos. El compromiso se sostiene con redundancia N+1 en energía y climatización, doble acometida con transferencia automática, generación autónoma propia y monitoreo continuo con alertamiento; no se invoca ninguna clasificación de instalación de tercero, porque las Bases no exigen certificación de nivel sino el cumplimiento verificable de cada requisito técnico individual. Este valor es el nivel de la infraestructura del recinto y es distinto del compromiso contractual penalizable del Artículo 78°, que recae sobre la transacción de negocio de extremo a extremo (≥ 99,9 % mensual, RT-10.01).

El programa arquitectónico considera ≈ 173 m² y 14 recintos: sala blanca de 32 m², NOC de 14 m², sala de sistemas de alimentación ininterrumpida y baterías, sala de climatización, sala de extinción, distribuidor principal y acometidas, recinto de custodia de medios de 10 m², patio de generador y recintos de apoyo. La disposición interna, la separación de zonas y la elevación de gabinetes constan en los planos del recinto que acompañan a esta parte (RT-06.03 y RT-06.05).

Energía: UPS doble conversión on-line 6 kVA con configuración N+1 y banco VRLA con autonomía ≥ 30 min a plena carga (RT-06.07); grupo electrógeno de 12 kVA con estanque para 24 h y contrato de reabastecimiento (RT-06.08); transferencia automática red↔generador con prueba mensual con carga real (RT-06.10); PDU verticales A/B por gabinete con medidor (RT-08.04); factor de potencia ≥ 0,95 (RT-06.11).

Climatización: 2 CRAC de precisión ≈ 12.000 BTU/h en N+1, con free cooling, pasillo frío confinado y rango ASHRAE TC 9.9 de 18–27 °C y 40–60 % HR medido a la toma de aire del equipo (RT-06.13 y RT-06.14); PUE de diseño 1,7 con medición continua en 2 puntos y reporte trimestral.

Incendios: detección temprana por aspiración AnaLASER (RT-06.16); extinción con agente limpio FM-200 conforme NFPA 75/2001 con botón de aborto (RT-06.17); extintores ABC y CO₂ por recinto (RT-06.18).

Seguridad física: 4 capas de acceso con biometría facial y resguardo AFIS, esclusa antipassback y bitácora electrónica, una persona a la vez y acompañada (RT-06.20, RT-06.21 y RT-06.23); 12 puertas controladas y 7 cámaras IP con retención ≥ 30 días integradas al control de acceso (RT-06.24); NOC de 14 m² contiguo a la sala con ventana interior («ver sin entrar», RT-06.29/30); sensores ambientales DCIM/BMS (RT-06.14).

Custodia de medios (RT-06.26/27/28): recinto de 10 m² en la segunda línea, sin luz UV (≤ 300 lux), 40–60 % HR, ventilación forzada y 18–27 °C; medio cifrado transportable rotado semanalmente a bóveda externa bajo custodia acreditada con cadena de custodia y bitácora; la pierna inmutable S3 es complementaria, no la reemplaza.

Cableado y comunicaciones: cableado estructurado Cat6A F/UTP + fibra OM4 certificado enlace por enlace (RT-06.04) sobre piso técnico de 40 cm, jerarquía ANSI/TIA-942 ENI→MDA→HDA→ZDA→EDA, con dos ductos de ingreso independientes (RT-06.32); 4 racks 42U en gabinete de servidores y comunicaciones separados (RT-06.05), con el cuarto (R04) reservado al crecimiento a 3 años.

Los componentes de sala ofertados se detallan a continuación:


> **Tabla 27** — Especificaciones del sitio principal on-premise (CD Talca) · 12 filas · ver planilla del subdocumento


## Especificaciones del sitio secundario y de la recuperación ante desastres

**Cómo se satisface el numeral 7.1.** Las Transversales exigen un sitio secundario en dependencias distintas del principal, en modalidad activo-activo o activo-pasivo, con replicación en línea del ambiente de producción y características tecnológicas equivalentes a las del sitio principal en lo que respecta a los servicios críticos. La solución lo satisface con dos sitios secundarios, uno por cada dominio del despliegue híbrido, porque la carga crítica vive en ambos:

- **Para el componente on-premise, el CD Concepción.** Es una dependencia física distinta, a 340 km del extremo opuesto de la red y sin amenazas comunes con Talca, y opera el motor de almacenes en modo reducido con su propia base local y autonomía de 24 horas. No es un sitio en espera: opera de forma autónoma todos los días y asume la carga de bodega de Talca mediante promoción controlada.
- **Para la carga principal en nube, la región AWS us-east-1.** Aloja la réplica pasiva promovible del núcleo transaccional, a ≈ 7.700 km de la región primaria y ≈ 8.500 km de Talca, sin amenazas comunes (RT-07.02).

**Modalidad declarada y justificada (RT-07.01): activo-pasiva en caliente.** La modalidad activo-activo duplicaría la infraestructura transaccional y obligaría a reconciliar escrituras concurrentes entre regiones, sin mejorar el objetivo de recuperación comprometido; el análisis completo está en el ADR-09. La región secundaria mantiene una réplica reducida pero funcional de la plataforma, escalable a carga completa en menos de 30 minutos:

- **RTO/RPO.** RTO ≤ 4 h y RPO ≤ 15 min para los servicios críticos (RT-07.04); la réplica Aurora Global mantiene un retraso típico < 1 s, alarmado a los 5 y 15 min (RT-07.03) y la replicación S3 CRR con RTC cumple un RPO < 15 min.

- **Conmutación/retorno.** failover en 8 pasos semiautomáticos (detección Route 53 < 5 min, promoción Aurora, escalado ECS Fargate, DNS, validación) con los pasos 4–7 automatizados mediante AWS Systems Manager Automation (RT-07.08); retorno (failback) en 6 pasos con reconciliación determinista de las transacciones generadas durante la contingencia (RT-07.05 y RT-07.06).

- **Pruebas.** conmutación real dos veces al año (semestral, Art. 20 / RT-07.07) midiendo RTO y RPO efectivos con informe al CLIENTE, junto con la restauración mensual verificada con cero errores (3-2-1-0, RNF-20.07).

- **Respaldos 3-2-1-0 (esquema único nube + on-premise).** la pierna «1 inmutable» vive en la nube (S3 Object Lock en modo Compliance + AWS Backup Vault Lock, RT-07.09 y RT-07.11); el NAS on-premise (D-05, WORM local + clave CMK independiente) es la copia local de recuperación rápida (RTO 4 h, RNF-20.06); la bóveda de custodia física externa completa la copia offsite (RT-06.26 y RT-06.28).

Los componentes del sitio secundario se detallan a continuación:


> **Tabla 28** — Especificaciones del sitio secundario y de la recuperación ante desastres · 5 filas · ver planilla del subdocumento


## Niveles de servicio de infraestructura

La infraestructura sostiene los niveles de disponibilidad del Capítulo 7 y el compromiso contractual del Artículo 78° (transacción de negocio crítica de extremo a extremo ≥ 99,9 %). La clasificación por servicio (RT-10.02) y su error budget son:

- **Crítico (≥ 99,9 %).** transacción de terreno de extremo a extremo (pedido→entrega→POD) y WMS on-premise (picking/recepción), por detener preventa, reparto y facturación y por la ventana nocturna sin contingencia.

- **Alto (≥ 99 %).** portal de clientes (stock, crédito, estado de cuenta) y telemetría IoT de cadena de frío en línea.

- **Medio.** BI/analítica (reportes diferibles, latencia ≤ 4 h).

- **Bajo.** notificaciones y comunicaciones (disponibles en colas).

La cadena de disponibilidad queda declarada y medible en sus cuatro tramos —nube, sala técnica, borde operacional y terreno—: la infraestructura del recinto se compromete en 99,95 % mensual por componente (numerales 6.1 y 7.2), la nube en la disponibilidad multizona del proveedor, el borde y el terreno en su autonomía declarada (24 h en el centro de distribución y 14 h en terreno, RT-03.10). Sobre esa cadena, el único compromiso que se mide y se penaliza es el del Artículo 78°: ≥ 99,9 % mensual de la transacción de negocio crítica de extremo a extremo (RT-10.01, menos de 8,76 h al año).


## Operación desconectada


> **Tabla 29** — Operación Desconectada (RT-03.10 a RT-03.13) · 4 filas · ver planilla del subdocumento


## Arquitectura de integración

Registro único de las integraciones de la solución: servicios, contratos, mensajería, versionado y gobierno. El marco normativo de este apartado se resume en la tabla de apertura de esta parte y se cita código por código en cada subsección.

Por qué la integración es una capa de primera clase en Puelche. El caso no describe un sistema legado único que reemplazar: describe un tejido de sistemas —ERP de 2017 sin documentación de interfaces, WMS de 2013 con proveedor desaparecido, una preventa cuyo proveedor ya no existe, planillas y papel— más 14.200 puntos de entrega, 10 empresas transportistas y un hito externo contractual (enero de 2029, condiciones comerciales de la principal cadena de supermercados). El riesgo de este proyecto no está en construir módulos: está en las costuras.


### Principios de integración


> **Tabla 30** — 1. Principios de integración · 8 filas · ver planilla del subdocumento


### Vista de integración

En texto, la vista de integración se organiza en cuatro dominios con tráfico saliente desde el terreno y el on-premise hacia la nube:

- **Terreno (offline-first).** C-01 App Preventa (62 preventistas), C-02 App Reparto (~200 conductores) y C-03 HHT bodega (120 concurrentes).
- **On-premise (5 sitios con cómputo).** A-01 Motor WMS (M1, M2 y M5 en modo wms_only), A-03 RabbitMQ (buffer 24 h), A-04 capa anticorrupción (frontera única del ERP), B-02 Greengrass (buffer 14 h) y E-01 mini-WMS cross-dock (ventana de 3 h).
- **Nube AWS sa-east-1.** Amazon API Gateway (Capa 3), Capa 4 con M1–M12 en Django + workers Celery, N-09 SQS FIFO, N-09 EventBridge, M11 Hub EDI GS1 (EANCOM · GS1 XML · EPCIS) y N-08 IoT Core.
- **Terceros.** ERP 2017 (sin documentación de interfaces), SII (DTE y guía electrónica), cadenas de supermercados (hito enero 2029), Transbank Webpay/POS, GIS/mapas y notificaciones.

El flujo del tráfico: el terreno llama a la puerta de enlace (API Gateway); los HHT y el WMS publican al broker (A-03); el cross-dock (E-01) publica sus eventos críticos directo a SQS FIFO y solo el detalle del mini-WMS viaja a Talca — lo crítico no depende de Talca (D-AL-04); Greengrass envía por IoT Core; y la Capa 4 consume las colas y alcanza el ERP únicamente a través de la capa anticorrupción (A-04), con una sola puerta hacia el legado. Las flechas desde el dominio on-premise hacia la nube son todas salientes.


### Catálogo de servicios de integración

El catálogo es el registro único de integraciones. Cada entrada tiene identificador estable, módulo dueño, contrato, versión y comportamiento ante falla. Vive versionado junto al código y se publica en el portal interno de desarrolladores servido por Amazon API Gateway (Capa 3).


#### Integraciones internas — superficies y plano híbrido


> **Tabla 31** — 3.1 Integraciones internas — superficies y plano híbrido · 8 filas · ver planilla del subdocumento


#### Integraciones externas — plataforma y terceros


> **Tabla 32** — 3.2 Integraciones externas — plataforma y terceros · 7 filas · ver planilla del subdocumento

**Número de integraciones y volumen de mensajes por integración (numeral 14.2).** Se declaran 15 integraciones: 8 internas y 7 externas. El volumen se deriva de la volumetría del caso sobre 25 días hábiles al mes, con el peak de septiembre al doble:

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

El total en régimen es de ≈ 150.000 mensajes al día, dominado por las dos series de tiempo —trazabilidad y telemetría— que por diseño no atraviesan la base transaccional: entran por el borde y se consolidan en la capa analítica (ADR-04). Las cinco integraciones restantes del catálogo son de configuración y administración, con volumen despreciable frente a estas cifras.


### Contratos


> **Tabla 33** — 4. Contratos (RT-05.16 · RT-05.18 · Art. 23) · 5 filas · ver planilla del subdocumento

Los contratos se declaran por dimensión:

- **API síncrona.** OpenAPI 3.1 por módulo, con ruta /v{major}/.... Metadatos obligatorios: x-owner (módulo dueño), x-version (semver), x-status (draft, stable, deprecated) y x-sunset (fecha de retiro).
- **Eventos.** AsyncAPI 2.6 con JSON Schema versionado por evento. Cada evento declara productor único, consumidores registrados, clave de partición y política de reintento.
- **Autenticación.** Superficies: OAuth 2.1 con PKCE. Servicio a servicio: mTLS. Máquina a máquina: credenciales de cliente con secreto de rotación automática. Todos los tokens los firma Keycloak (Capa 7).
- **Validación.** Validación de esquema e inspección de carga útil en la puerta de enlace (Art. 21.2), antes de alcanzar la Capa 4. Un mensaje que no valida no entra: se rechaza con causa y queda registrado.
- **Trazabilidad.** Todo llamado y todo evento propaga transaction_id (OpenTelemetry) desde la Capa 3 hasta la Capa 6. Es la clave con la que se reconstruye una operación de extremo a extremo, conforme al Art. 23: quién, qué, cuándo, desde dónde y con qué valores anteriores y posteriores.


#### Eventos canónicos del dominio

Los eventos son el vocabulario del sistema. Se nombran en pasado, son inmutables y llevan event_id (UUID), occurred_at, site_id y transaction_id.


> **Tabla 34** — 4.1 Eventos canónicos del dominio · 10 filas · ver planilla del subdocumento


### Mensajería


> **Tabla 35** — 5. Mensajería (RT-02.06 · RT-02.07 · ADR-05) · 4 filas · ver planilla del subdocumento

Garantías declaradas:

- **Entrega al menos una vez**, con deduplicación en el consumidor. No se promete entrega exactamente una vez: se promete idempotencia verificable.
- **Orden por partición, no orden global.** La partición es el sitio o la entidad de negocio, según el evento.
- **DLQ por cola** con retención declarada, monitoreada por el equipo de operación y con bandeja de excepciones cuando el mensaje afecta a un tercero (EDI, DTE).
- **Reintento con retroceso exponencial y variación aleatoria**; cortacircuitos sobre ERP, SII y Transbank; mamparos por integración: un fallo del ERP no degrada la preventa.
- **Reconciliación determinista:** al reconectar, el conflicto de stock se resuelve por la regla de reserva declarada, nunca por marca de tiempo, y la decisión queda en la bitácora del Art. 16.4.


### Costuras híbridas — amarre con la arquitectura física

La vista de integración y la vista física describen los mismos puntos de contacto. Esta tabla es el amarre entre ambas vistas: cada costura aparece aquí con su contraparte física.


> **Tabla 36** — 6. Costuras híbridas — amarre con la arquitectura física · 12 filas · ver planilla del subdocumento


### Capa anticorrupción y estrangulamiento del legado

Frontera única del ERP (A-04). El ERP de 2017 no tiene documentación de interfaces. En vez de descubrir su forma real dentro de cada módulo, se levanta una sola frontera: la ACL expone hacia adentro un contrato OpenAPI 3.1 propio de Puelche y absorbe hacia afuera la forma del ERP. Consecuencias:

- El conocimiento del ERP queda concentrado y documentado en un solo componente, no disperso en doce módulos.
- Ningún módulo, portal ni cadena de supermercados escribe al ERP: celery-erp-sync publica notificaciones por SQS y lee contratos por la ACL.
- Cuando una capacidad del ERP se absorbe en la plataforma, se retira de la ACL sin tocar a los consumidores.

Estrangulamiento del WMS de 2013 (ADR-08). El WMS se reemplaza en la Etapa 1 por los módulos M1, M2 y M5 del monolito. Durante la coexistencia el legado queda detrás de la misma ACL, con una tabla de «capacidad absorbida» —recepción GS1, slotting, misiones de picking con HHT, conteo cíclico— que se vacía ola a ola por sitio, con estrategia azul-verde y plan de reversión.

Hub EDI GS1 (ADR-11). Una cadena nueva se incorpora por configuración de perfil (equivalencias GTIN por cadena, RF-12.03), no por desarrollo. El hub mapea cada cadena contra un modelo canónico GS1, no contra el ERP: es exactamente lo que evita construir una integración distinta por cada cadena (Cap. 17.4, punto 10 del caso).


### Versionado y política de obsolescencia


> **Tabla 37** — 8. Versionado y política de obsolescencia (RT-05.17 · Art. 23) · 7 filas · ver planilla del subdocumento

La política de versionado y obsolescencia se declara en siete reglas:

- **Versionado semántico estricto.** major.minor.patch. major = cambio disruptivo; minor = aditivo y retro-compatible; patch = corrección.
- **Evolución aditiva primero.** Un campo se agrega, nunca cambia de significado. Un campo que deja de usarse se marca deprecated antes de retirarse.
- **Preaviso mínimo de 6 meses.** Ninguna versión se retira antes de seis meses de aviso formal (Art. 23 y RT-05.17). El registro de deprecaciones es visible para todo el equipo y para el CLIENTE.
- **Doble versión concurrente.** Durante la migración conviven v{n} y v{n+1}; el consumidor migra en su ventana, no en la del proveedor.
- **Aprobación de cambios disruptivos.** Un major requiere aprobación del Comité de Arquitectura y plan de migración con los consumidores identificados uno a uno.
- **Congelamientos del caso.** No se publica ni se retira ninguna versión en septiembre, en diciembre ni en los tres primeros días hábiles del mes (Cap. 13.2 del caso).
- **Contratos que no controla el proponente.** Las especificaciones de cada cadena de supermercados y del SII las fija la contraparte: se versionan como perfiles del hub y se prueban contra el banco de pruebas de cada contraparte antes de activarse.


### Gobierno de la capa de integración


> **Tabla 38** — 9. Gobierno de la capa de integración (Art. 19 · RT-05.16 · Cap. 14 BTT) · 7 filas · ver planilla del subdocumento


### Carga y descarga masiva de datos


> **Tabla 39** — 10. Carga y descarga masiva de datos (RT-05.22) · 4 filas · ver planilla del subdocumento

Regla: ninguna carga masiva se ejecuta dentro de la ventana crítica 05:30–07:00, y toda carga queda registrada y es auditable.


### Funciones que no operan sin conexión

La declaración formal de funciones no disponibles en modo desconectado que exige RT-03.13 se detalla por componente en la tabla de emplazamiento de esta parte y se resume en la arquitectura lógica (Subdocumento 4.1). Desde la vista de integración la regla es una sola:

- Lo transaccional crítico de terreno y de bodega opera sin conexión (14 h en terreno, 24 h en el centro de distribución). Lo que depende de la nube o de un tercero degrada con procedimiento manual declarado y sin pérdida de datos.
- Ninguna función de la ventana crítica de despacho (05:30–07:00) depende de una integración externa: el DTE se timbra de forma diferida con folio reservado, el cobro se captura como pendiente, la excursión térmica se detecta y bloquea localmente, y la ruta ya está cargada en el dispositivo.

## Arquitectura de seguridad

Arquitectura de seguridad de la solución: modelo Zero Trust, capa expuesta, identidad y accesos, cifrado y controles. Es autocontenida: los valores que declara se sostienen en los componentes especificados en las secciones anteriores de este capítulo (modelo de emplazamiento, tecnologías ofertadas, implementos y sitios principal y secundario).

Es además el documento de seguridad del subdocumento: es autocontenido y los valores aquí declarados no son nuevos salvo donde se indica expresamente (consolidan lo comprometido en este mismo Subdocumento 4.2).

Por qué la seguridad de Puelche no es la de una oficina. El perímetro de esta solución no es un edificio: son 62 preventistas de pie en la puerta de un almacén, ~200 conductores —de los cuales ~160 no son trabajadores de la compañía y rotan sin aviso—, dispositivos compartidos entre turnos en una cámara a −22 °C, un turno de preparación con 38 % de rotación anual y 14.200 puntos de entrega. Un modelo de seguridad basado en la red corporativa aquí no protege nada. Por eso el modelo es Zero Trust y por eso la identidad es la pieza central.


### Principios rectores


> **Tabla 42** — 1. Principios rectores · 8 filas · ver planilla del subdocumento


### Modelo Zero Trust aplicado


#### Los siete principios de NIST SP 800-207 en Puelche


> **Tabla 43** — 2.1 Los siete principios de NIST SP 800-207 en Puelche · 7 filas · ver planilla del subdocumento


#### Zonas y flujos

En texto, las zonas y su flujo son: la zona pública (clientes del canal moderno, transportistas ≈160 conductores y 180 proveedores) ingresa únicamente por la DMZ en nube (CloudFront + AWS WAF v2 + Shield Advanced → Amazon API Gateway con OIDC, cuotas, esquema y validación de carga útil); la zona de aplicación (ECS Fargate M1–M12 + workers y Keycloak IdP maestro como autoridad única) sirve a las zonas de datos (Aurora PostgreSQL, DynamoDB y S3 con Object Lock, en subredes privadas sin salida); la zona on-premise (VLAN 10 MGT · 20 SRV · 30 OPS · 40 WKS · 50 IOT, firewall D-01 UTM en HA como Customer Gateway y caché Keycloak de solo lectura TTL 8 h) conecta con la nube por VPN/IPsec saliente; y la zona de terreno (apps Kotlin offline-first + MDM; HHT compartidos en cámara a −22 °C) no tiene perímetro.

Reglas de zona declaradas:

- La única exposición pública es la DMZ en nube (CloudFront → WAF → API Gateway). Las consolas internas no pasan por ahí: entran por intranet o VPN (RT-03.22).
- La zona de datos no tiene salida a internet y se consume por VPC Endpoints/PrivateLink.
- Desde la zona on-premise no se acepta ninguna conexión entrante salvo las dos excepciones D-AL-05.
- La zona de terreno no tiene perímetro: se protege con identidad, cifrado local, MDM y borrado remoto.


### Capa expuesta


> **Tabla 44** — 3. Capa expuesta (Art. 21.2 · RT-11.11/11.13) · 8 filas · ver planilla del subdocumento


#### Superficie de exposición completa


> **Tabla 45** — 3.1 Superficie de exposición completa (RT-11.13) · 8 filas · ver planilla del subdocumento

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

Factores resistentes a la suplantación: FIDO2/WebAuthn (claves de acceso) disponible y preferente para perfiles administradores, además de TOTP (RT-12.04, deseable, se supera el mínimo).

Acceso de conductores externos: OTP de un solo uso por operación, sin cuenta corporativa (RF-06.08). Es la respuesta al hecho de que ~160 conductores no son trabajadores de la compañía y rotan sin aviso.


#### Autorización: RBAC más ABAC


> **Tabla 47** — 4.3 Autorización: RBAC más ABAC (RT-12.05) · 4 filas · ver planilla del subdocumento

El control de acceso se resuelve en cuatro capas:

- **RBAC.** Roles derivados de los 11 actores canónicos del modelo lógico. Los permisos viven en Keycloak.
- **ABAC.** Atributos de contexto que acotan el rol: instalación asignada, horario de turno (el despacho solo es válido en su ventana), dispositivo provisto y enrolado por MDM. Las políticas se aplican en la Capa 4.
- **Segregación de funciones (RT-12.06).** Conciliación ≠ aprobación (M10); detección de excursión térmica ≠ decisión de bloqueo (M9); rendición ≠ cierre contable (M7). Nadie que genera un control lo ejecuta. La matriz completa se declara en el registro de requerimientos (Cap. 17.1).
- **Aislamiento de externos (RT-12.11).** Cada proveedor ve solo sus órdenes de compra y documentos; cada transportista solo sus rutas asignadas. No hay visibilidad cruzada.


#### Política de sesión


> **Tabla 48** — 4.4 Política de sesión (Art. 22 · RT-12.07 · RT-12.08) · 11 filas · ver planilla del subdocumento

La política de sesión se declara en cinco términos conforme a RT-12.07:

- **Duración máxima.** La credencial de acceso dura 30 minutos, valor único de la propuesta que rige para todos los perfiles (D-AL-07); la credencial de identidad vive 1 hora. En operación desconectada la sesión no depende del IdP sino de la caché local (A-05): el token de turno cubre 8 horas en el centro de distribución (RNF-13.01) y 14 horas en terreno (RNF-06.02), de modo que la ventana sin enlace nunca queda descubierta (ADR-06).
- **Caducidad por inactividad.** 30 minutos en consolas de bodega y back-office y 60 minutos en superficies de solo lectura; una pantalla de consulta no obliga a reautenticarse cada media hora.
- **Renovación de la credencial de sesión.** Por credencial de refresco rotatoria de 30 días: cada uso emite una nueva e invalida la anterior, y el reúso detectado invalida la familia completa y fuerza la reautenticación.
- **Revocación inmediata.** El cierre global de sesión desde el panel de administración corta una sesión ante la pérdida o el compromiso de un dispositivo, y la baja de una identidad revoca sus credenciales vigentes.
- **Control de sesiones concurrentes.** Una sola sesión activa por actor de terreno: se deniega el inicio simultáneo del mismo preventista o conductor en otro dispositivo, con opción de invalidar la anterior.

La elevación temporal de privilegios no excede las 2 horas y exige justificación, aprobación de un segundo perfil y registro auditado. Conforme a RT-12.08, las credenciales están firmadas y son de vida breve, la credencial de refresco es rotatoria y ningún identificador de sesión viaja en la ruta de la dirección web; el token se envía siempre en la cabecera de la petición. El registro, la verificación de identidad y la recuperación de acceso autoservido de personas usuarias externas (RT-12.12) se cubren con el mecanismo declarado en la subsección de federación.


#### Autenticación en el perfil operacional de terreno

El caso fija condiciones que descartan la contraseña como mecanismo de terreno: guantes térmicos a −22 °C, uso a una mano durante la descarga, uso de pie y a la intemperie en la puerta del local, dispositivos compartidos entre turnos en bodega y 38 % de rotación anual en preparación. La respuesta declarada:

- El operador autentica con conexión al inicio de turno (PIN de 6 dígitos o biometría del dispositivo) y descarga un token cifrado de vida acotada al turno.
- Durante el turno el PIN desbloquea el token local; no autentica contra el IdP por transacción. No hay dependencia de red en la ruta.
- El dispositivo es un factor de posesión enrolado por MDM; el PIN es el segundo factor. Esto satisface la MFA del Art. 22 sin exigir un segundo dispositivo a alguien que trabaja con guantes.
- Los datos locales están cifrados y admiten borrado remoto selectivo (RF-03.16/06.12): se borra la aplicación y su caché, no la información personal del dispositivo.


#### Gestión de dispositivos


> **Tabla 49** — 4.6 Gestión de dispositivos (MDM — RT-03.18) · 6 filas · ver planilla del subdocumento

La gestión de dispositivos se declara en seis capacidades:

- **Enrolamiento.** Alta del dispositivo contra el usuario antes del turno; perfil por rol (preventista, preparador, conductor).
- **Configuración.** Cifrado local obligatorio, PIN obligatorio, bloqueo de pantalla, modo quiosco (aplicación única), actualización de aplicación y de caché de turno.
- **Postura y monitoreo.** Estado de sincronización, batería, versión de aplicación; alertas por dispositivo perdido, almacenamiento bajo o fallo recurrente de sincronización.
- **Seguridad.** Borrado remoto selectivo con revocación de tokens.
- **Inventario.** Registro por IMEI/serie, asignación y estado.
- **Operación.** MDM como servicio gestionado (Android Enterprise o equivalente): el equipo de TI del CLIENTE es de 4 personas y no administra la plataforma localmente.


#### Ciclo de vida de la identidad

- Aprovisionamiento ≤ 24 h desde el alta en recursos humanos o en el proveedor: cuenta, permisos por rol canónico y dispositivo enrolado.
- Baja efectiva en ≤ 24 h desde la desvinculación (Art. 22): revocación de tokens, borrado remoto del dispositivo y revocación de accesos externos.
- Flujo desatendido y auditable, con aprobación del jefe de área, bitácora de aprovisionamiento y revisión semestral de accesos (certificación de identidades).
- Auditoría de identidad con no repudio: creación, modificación, elevación y baja de cuentas, con la retención declarada en la detección, respuesta y evidencia.


#### Accesos privilegiados y cuenta de emergencia

- **PAM con acceso a demanda:** sin acceso interactivo permanente a producción. La operación excepcional se hace just-in-time por AWS Systems Manager Session Manager, con MFA, aprobación y sesión grabada (RT-11.27).
- **Cuenta de emergencia (break-glass):** fuera de banda, custodiada en bóveda física con doble firma, para contingencia de indisponibilidad del IdP. Su activación exige procedimiento escrito, notificación inmediata a TI y a la gerencia, registro en cadena de custodia y rotación de credenciales tras el uso. Se prueba dos veces al año junto con el simulacro de recuperación ante desastres.


### Cifrado y gestión de claves


#### En tránsito


> **Tabla 50** — 5.1 En tránsito · 5 filas · ver planilla del subdocumento

El cifrado en tránsito se declara por trayecto:

- **Superficies públicas y portales.** TLS 1.3 con HSTS y precarga; TLS 1.0/1.1 deshabilitados.
- **Servicio a servicio.** mTLS (microsegmentación; sin confianza implícita en la red interna).
- **On-premise ↔ nube.** IPsec/IKEv2 con AES-256-GCM, BGP, MTU 1436, dos túneles.
- **Borde IoT → nube.** MQTTS 8883 con certificado X.509 por dispositivo.
- **Respaldos y replicación.** TLS 1.3 en tránsito (RT-07.10).


#### En reposo


> **Tabla 51** — 5.2 En reposo · 6 filas · ver planilla del subdocumento

Rotación y custodia: claves de datos con rotación anual o ante revocación o compromiso; claves maestras según el calendario del proveedor; rotación en línea, sin degradación del servicio. Los respaldos conservan la versión de clave necesaria para una restauración auditable. Separación de funciones en la custodia de claves (Art. 21.2): quien administra la plataforma no administra las claves maestras.


#### Cifrado a nivel de campo

El caso lo declara exigible para cuatro conjuntos de datos. Aplicación declarada:


> **Tabla 52** — 5.3 Cifrado a nivel de campo (RT-11.10 — Según caso) · 4 filas · ver planilla del subdocumento

El cifrado a nivel de campo se declara por conjunto de datos:

- **Comportamiento de pago y antecedentes comerciales del cliente.** Cifrado a nivel de campo con clave en KMS; acceso restringido por rol y registro de consultas (RT-16.09).
- **Datos de geolocalización de personas.** Cifrado a nivel de campo, retención 12 meses y registro de consultas. La visibilidad de flota es operativa y no se desliza a control de jornada (D1, objeción sindical L577).
- **Medios de pago electrónicos.** El PAN no se almacena: tokenización en la pasarela; el terminal POS es PCI PTS 7.x.
- **RUT de clientes en bases y registros.** Pseudonimización mediante cifrado a nivel de campo (pgcrypto con clave en KMS).

Gestión de secretos. Los secretos de integración (credenciales del ERP, certificados AS2/EDI, credenciales del SII y de Transbank) se administran en AWS Secrets Manager y SSM Parameter Store, con rotación automática y consumo desde los nodos on-premise por VPC Endpoint saliente, coherente con el principio 4. Prohibición absoluta de secretos embebidos en código, imágenes o archivos de configuración (Art. 21.4).

Gestor de secretos: servicio administrado, no componente autoalojado. La decisión está fundada en el ADR-15 y su emplazamiento es el componente N-12 de la tabla de emplazamiento. Se descartó un gestor autoalojado on-premise porque habría exigido una máquina virtual adicional en Talca con su alta disponibilidad, respaldo, procedimiento de sellado y licencia, sumando superficie de administración a un equipo de cuatro personas sin beneficio funcional frente al servicio administrado (Art. 16.3). Todo componente de seguridad de esta arquitectura tiene emplazamiento declarado, como exige el Art. 16.2.


### Clasificación de la información y controles por nivel


> **Tabla 53** — 6. Clasificación de la información y controles por nivel (RT-11.03) · 4 filas · ver planilla del subdocumento


### Detección, respuesta y evidencia


> **Tabla 54** — 7. Detección, respuesta y evidencia (Art. 21.3 · RT-11.14 a RT-11.21) · 11 filas · ver planilla del subdocumento


### Modelado de amenazas STRIDE

Cada componente y cada integración externa modela sus amenazas antes de implementarse.


> **Tabla 55** — 8. Modelado de amenazas STRIDE (Art. 21.1 · RT-11.02) · 9 filas · ver planilla del subdocumento


### Seguridad del ciclo de desarrollo


> **Tabla 56** — 9. Seguridad del ciclo de desarrollo (Art. 21.4 · RT-11.22 a RT-11.27) · 6 filas · ver planilla del subdocumento


### Datos personales, residencia y transferencia internacional


> **Tabla 57** — 10. Datos personales, residencia y transferencia internacional (Art. 23 · Ley 21.719) · 12 filas · ver planilla del subdocumento

Dos de los resguardos de esta tabla son decisiones de diseño y no solo cláusulas contractuales, y se propagan a la sección de arquitectura de despliegue de este documento y a la arquitectura lógica (Subdocumento 4.1): la minimización, por la que la región secundaria sostiene continuidad y no se explota analíticamente, y la exclusión de los datos de geolocalización de personas de la replicación transfronteriza. La decisión de no replicar la geolocalización de personas tiene además un fundamento del caso: la geolocalización de personas es el dato con la objeción sindical explícita (Restricción no negociable N° 10, Cap. 10 del caso) y con la retención más corta (12 meses); mantenerlo en una sola jurisdicción reduce la superficie legal sin afectar la continuidad, porque no es un dato necesario para reanudar la operación.


#### Protocolo ARCOP — derechos de los titulares

Declaración de cumplimiento de los derechos de los titulares sobre los datos personales tratados por la solución:

- **Derechos cubiertos:** acceso, rectificación, cancelación (supresión), oposición, portabilidad y bloqueo temporal. Instrumentación: acceso y portabilidad por la vía de la exportabilidad (RT-05.06, en formato abierto CSV o JSON y con diccionario); rectificación y supresión por el ciclo de vida de datos (RT-05.07 y RT-05.08) con trazabilidad de cada cambio; bloqueo temporal conforme a la ley en caso de impugnación del titular.
- **Canal único:** correo dedicado y formulario web con acuse de recibo, publicados en la política de privacidad. Ningún otro canal inicia el plazo de respuesta.
- **Plazo:** respuesta en 30 días corridos, prorrogables una sola vez por 30 más, con aviso al titular (Art. 11 de la Ley 21.719).
- **Verificación de identidad:** autenticación del titular o su representante (documento de identidad / poder), proporcional al riesgo del dato (reforzada para geolocalización y datos sensibles); registro de cada verificación.
- **Contraparte responsable (BA Art. 27°):** el Encargado de Seguridad de la Información coordina la recepción y respuesta de solicitudes y su registro; es la contraparte única e identificable ante los titulares y ante el CLIENTE.
- **Registro:** bitácora de solicitudes ARCOP (qué derecho, quién, cuándo, resolución y plazo real), conservada conforme a la retención de auditoría y disponible para la Agencia de Protección de Datos Personales.


#### Política de Privacidad — versión preliminar

Documento de referencia del aviso informativo a titulares (clientes y trabajadores); versión preliminar anexable al Informe 1:

- **Responsable:** Distribuidora Puelche S.A. (CLIENTE), con el proponente como encargado del tratamiento (cláusulas de tratamiento de datos, BA). Residencia primaria: Chile y AWS sa-east-1.
- **Datos tratados:** identificación y contacto de clientes (14.200 puntos, mayoría personas naturales); comportamiento de pago e historial crediticio del canal tradicional; datos laborales de trabajadores; geolocalización de preventistas (62) y conductores (~200) con finalidad exclusivamente operativa (rutas, verificación de entrega, costo de servir) — sin control de jornada ni cámaras en cabina (Decisión N° 13 del registro; objeción sindical: Restricción no negociable N° 10 del Cap. 10 del caso).
- **Finalidades:** operación comercial y logística (preventa, reparto, facturación), trazabilidad sanitaria obligatoria (D.S. 977/96), seguridad de la información y continuidad (DR/DRP), cumplimiento normativo.
- **Base de licitud:** por tratamiento, según la tabla de bases de licitud de este mismo apartado (artículos 12 y 13 de la Ley N.° 21.719): geolocalización de trabajadores por ejecución del contrato de trabajo e interés legítimo del empleador (no consentimiento, por desequilibrio; test de proporcionalidad en la tabla de bases de licitud); clientes por ejecución de contrato e interés legítimo; obligaciones legales (DTE, trazabilidad sanitaria) por obligación legal; conductores externos por consentimiento del titular. Donde aplique consentimiento, será expreso, informado, específico y revocable, con registro de la revocación.
- **Destinatarios y transferencias:** AWS (encargado, ISO/IEC 27018) y subencargados declarados (BA 73.4); transferencia internacional a us-east-1 solo bajo los resguardos del Art. 23; la geolocalización de personas excluida de la replicación transfronteriza.
- **Retención y eliminación por categoría:** geolocalización 12 meses; trazabilidad sanitaria 5 años; documentos tributarios 6 años; eliminación certificada al término del contrato (Art. 85 BA).
- **Derechos del titular:** acceso, rectificación, supresión, oposición, portabilidad y bloqueo temporal; cómo ejercerlos, en el protocolo de derechos de los titulares (canal dedicado y plazo de 30 días, prorrogable una sola vez por otros 30).
- **Seguridad:** medidas declaradas en este documento — cifrado a nivel de campo (RT-11.10), RBAC/ABAC, registro de consultas a datos sensibles (RT-16.09), Zero Trust (NIST SP 800-207).
- **Brechas:** notificación al CLIENTE en ≤ 24 h (RT-11.19); el CLIENTE, como responsable, cumple la notificación ante la Agencia de Protección de Datos Personales y los titulares afectados.
- **Portales de canal moderno (N-01/N-02/N-03) y cookies:** no se instrumentan cookies de terceros ni analítica de seguimiento; en caso de solicitarse, se implementará un banner de consentimiento de cookies conforme a la Ley 21.719 y un aviso específico del portal.


#### Evaluación de Impacto sobre Protección de Datos (EIPD) — alcance preliminar

- **Procedencia:** BA Art. 27° (evaluación de impacto "cuando corresponda") y Ley 21.719 (tratamientos de alto riesgo). El caso la gatilla: tratamiento masivo de datos personales (14.200 clientes) y monitoreo sistemático de personas (GPS de ~260 trabajadores).
- **Alcance (criterios):** finalidad, base de licitud, categorías (incluidas sensibles: geolocalización, comportamiento de pago), destinatarios, transferencias internacionales (us-east-1), retención por categoría, medidas de seguridad y riesgos para los titulares (vigilancia de trabajadores, acceso indebido a historial crediticio, exposición de geolocalización).
- **Tratamientos incluidos:** preventa/reparto (geolocalización); gestión de crédito y cobranza (comportamiento de pago); trazabilidad sanitaria lote→cliente (D.S. 977/96); POD (firma/foto); analítica y observabilidad con datos personales.
- **Resultado comprometido:** EIPD según metodología reconocida (p.ej. ISO/IEC 29134 / CNIL PIA): documento de riesgos y controles y veredicto de proporcionalidad; versión final antes de la entrada en producción y actualización ante cualquier cambio de tratamiento.
- **Entregable:** documento formal del proyecto, con versión preliminar anexada al Informe 1 y revisión anual durante la operación.


#### Vigencia y seguimiento normativo

La Ley 21.719 entra en vigencia el 01-dic-2026 (Diario Oficial 13-dic-2024; vacancia de 2 años). El 31-ago-2026 el Gobierno ingresó el Boletín N° 18.623-07 (Mensaje N° 110-374, urgencia 01-sep-2026), que postergaría su entrada en vigencia al 01-dic-2027, aumenta a 5 los consejeros de la Agencia y amplía la primera amonestación a todos los responsables. Al cierre de esta versión es proyecto de ley, aún no publicado: mientras tanto rige el calendario 01-dic-2026. La propuesta es robusta a ambas fechas por diseño: se alinea contra el articulado completo ya publicado y la operación (contrato de 56 meses) cae dentro del régimen cualquiera sea la fecha; ninguno de los controles de este apartado depende de la fecha de vigencia.


#### Base de licitud por tratamiento

Cierre de la decisión de base de licitud. La regla general de la ley es el consentimiento (Art. 12), salvo que concurra alguna de las bases distintas al consentimiento (Art. 13): ejecución de contrato, obligación legal, interés vital o interés legítimo del responsable. Cada tratamiento del caso declara su base, su fundamento y sus garantías:


> **Tabla 58** — 10.5 Base de licitud por tratamiento (Ley 21.719, Art. 12 y 13) · 7 filas · ver planilla del subdocumento

Garantías transversales de esta tabla:

- **RAT (registro de actividades de tratamiento):** entregable del proyecto; cada fila se formaliza con finalidad, categorías, plazos, destinatarios y medidas (controles ISO 5.31 y 5.34).
- **Sensibilidad:** geolocalización y comportamiento de pago se tratan como categorías sensibles que el caso identifica (RT-05.08/RT-11.10), con cifrado de campo y registro de consultas; la geolocalización se apoya en la excepción laboral/contractual de la ley, no en un consentimiento general.
- **Consentimiento donde aplique (uso no contractual de clientes, conductores externos):** expreso, informado, específico y revocable, con registro de la revocación.
- **Menores de edad:** la solución no trata datos de NNA; si un cliente resultara menor de 14 años, el consentimiento corresponderá a padres o representantes, y entre 14 y 18 al titular con asistencia, conforme la ley.
- **Ciclo de vida:** eliminación certificada al término del contrato (Art. 85) y retención por categoría.


### Matriz de controles ISO/IEC 27001:2022

Referencia única de controles para toda la solución, nube y on-premise. El dimensionamiento on-premise se apoya en esta matriz.


> **Tabla 59** — 11. Matriz de controles ISO/IEC 27001:2022 (RT-11.05) · 18 filas · ver planilla del subdocumento


### Seguridad física

Seguridad física del sitio principal, en complemento de sus especificaciones de obra:

Cuatro capas de acceso hasta la sala blanca, con biometría facial (AFIS de respaldo) y esclusa con antipassback; acceso de a una persona con reverificación (RT-06.23).

CCTV IP con retención ≥ 30 días y respaldo en medio secundario auditable, cubriendo cada puerta controlada (RT-06.24).

Recinto de custodia de medios de 10 m² con condiciones ambientales declaradas, e inventario con rotación y registro de todo movimiento (RT-06.26 a RT-06.28).

Acceso de terceros (fabricantes, mantenedores, auditores) con acompañamiento obligatorio y registro (RT-06.25).

Control de dispositivos extraíbles en los nodos on-premise y borrado seguro verificable de los medios que salen de servicio.

## Arquitectura de despliegue

Arquitectura de seguridad de la solución: modelo Zero Trust, capa expuesta, identidad y accesos, cifrado y controles. Es autocontenida: los valores que declara se sostienen en los componentes especificados en las secciones anteriores de este capítulo (modelo de emplazamiento, tecnologías ofertadas, implementos y sitios principal y secundario).


### Ambientes de despliegue

Los cinco ambientes obligatorios del numeral 4.1 de las Bases Técnicas Transversales están habilitados como condición del hito H3 (RT-04.01), aislados entre sí mediante cuentas AWS separadas bajo una organización centralizada de AWS Control Tower (aislamiento estricto + SCP):


> **Tabla 62** — 1. Ambientes de despliegue (RT-04.01) · 5 filas · ver planilla del subdocumento

Reglas que gobiernan el modelo de ambientes:

- **Paridad Pre-Producción = Producción (RT-04.02).** topología, versiones de componentes y configuración equivalentes; las diferencias por costo se declaran y justifican una a una.
- **On-premise como producción (RT-04.01/RT-03.10).** el despliegue on-premise es producción con la imagen única wms_only; esa misma imagen recorre Dev→QA→PreProd en la nube antes del cutover en Talca (ventana de 24 h) y en Concepción. No se mantienen ambientes on-premise separados — la paridad la garantizan la imagen única y el IaC versionado (RT-03.03).
- **Entrega continua (RT-04.05).** el pipeline CI ejecuta compilación, pruebas unitarias, análisis estático, análisis de composición, escaneo de secretos y escaneo de imágenes de contenedor, con bloqueo automático del despliegue ante hallazgos críticos o altos (RT-11.22).
- **Despliegue sin interrupción (RT-04.07).** estrategia azul-verde con canario en etapas, demostrada en PreProducción antes de cada paso a producción; reversión automatizada (RT-04.06).
- **Configuración externalizada (RT-04.08).** un mismo artefacto se promueve QA→PreProd→Prod sin recompilación; los secretos viven en gestor de secretos con rotación automática (RT-04.09), sin credenciales embebidas.
- **Datos no productivos (RT-11.25).** Dev, QA y PreProd usan datos sintéticos generados desde la volumetría del Cap. 14 del caso; las plantillas próximas a producción pasan por anonimización/seudonimización verificable (Amazon Macie).
- **Sin acceso interactivo a producción (RT-11.27).** los despliegues son exclusivamente por pipeline; el acceso administrativo excepcional es just-in-time vía AWS Systems Manager Session Manager con MFA, aprobación y sesión grabada.
- **Reducción de ambientes no productivos fuera de horario (RT-04.13).** Dev/QA/PreProd se apagan o reducen fuera del horario de uso, con el ahorro reflejado en la estructura de costos.
- **Portal web (N-01/N-02/N-03).** la SPA Angular se publica por ambiente en S3+CloudFront (bucket y distribución por cuenta AWS) y su backend es la misma imagen Django del ambiente; entra a producción con el hito de enero 2029 (RNF-12.01).


### Redes (topología, segmentación y conectividad)


#### WAN — tri-camino con SD-WAN

Cada instalación dispone de caminos físicamente independientes con conmutación automática en < 30 s (el requisito exige ≤ 5 min declarados; el diseño opera en < 30 s):


> **Tabla 63** — 2.1 WAN — tri-camino con SD-WAN (RT-03.17) · 4 filas · ver planilla del subdocumento

SD-WAN con políticas centralizadas y BGP; los cross-docks salen directo por Starlink a SQS/IoT/SSM (configuración crítica) y sincronizan detalle a Talca por AMQPS entre brokers (C-13). La pérdida total del enlace se cubre con la autonomía local 24 h (CD) / 14 h (terreno) — RT-03.10, RNF-13.01.


#### VPN Site-to-Site (costura C1)

Extremos: D-01 Firewall/UTM (HA activo-pasivo) → Customer Gateway en cada CD; extremo cloud VGW del VPC Hub.

Protocolo: IPsec/IKEv2, AES-256-GCM, BGP, MTU 1436; 2 túneles (activo + standby). Conmutación < 30 s sobre los tres caminos.


#### Segmentación de red (sin solapamiento)


> **Tabla 64** — 2.3 Segmentación de red (sin solapamiento) · 5 filas · ver planilla del subdocumento

Modelo Hub-and-Spoke con VPC de tránsito central: la comunicación cross-VPC pasa por el Transit Gateway (inspección) y los servicios AWS (S3, SQS, DynamoDB, KMS, SSM) se consumen por VPC Endpoints/PrivateLink sin tráfico por internet (RT-03.03).


#### Zero Trust — flujos permitidos

Todo el tráfico on-premise → nube es outbound (HTTPS/443, MQTTS/8883) sin conexiones entrantes salvo las dos excepciones controladas D-AL-05 sobre túnel IPsec autenticado:


> **Tabla 65** — 2.4 Zero Trust — flujos permitidos (BA Art. 21) · 9 filas · ver planilla del subdocumento


#### Capa pública (DMZ) y DNS

Primera línea: CloudFront + AWS WAF v2 (OWASP Top 10 + reglas personalizadas) + Shield Advanced; autenticación API Gateway con Keycloak OIDC, cuotas por cliente y validación de esquema (RT-11.11).

DNS: Route 53 con health checks activos; routing por latencia en operación normal y failover automático hacia us-east-1 en contingencia.


### Alta disponibilidad


#### Capa cloud (sa-east-1) — Multi-AZ


> **Tabla 66** — 3.1 Capa cloud (sa-east-1) — Multi-AZ · 7 filas · ver planilla del subdocumento

Nivel de servicio de extremo a extremo sobre la transacción crítica de negocio: ≥ 99,9 % mensual (RT-10.01, menos de 8,76 h al año). Es el compromiso contractual penalizable del Artículo 78° y es distinto de la disponibilidad de la infraestructura del recinto (99,95 % por componente, numerales 6.1 y 7.2), que es un medio para alcanzarlo.


#### Capa on-premise


> **Tabla 67** — 3.2 Capa on-premise · 7 filas · ver planilla del subdocumento

VMs dimensionadas con headroom ×1,5 (RNF-19.04) para tolerar 3.900 entregas/día en el peak de septiembre. SPOF declarados y mitigados (RT-02.11): periféricos de andén (respaldo manual), clúster Talca sin SPOF estructural, Concepción nodo único (autonomía 24 h + DRP), cross-dock mini-PC único (ventana de 3 h + sincronización diferida).


### Recuperación ante desastres


#### DRP nube (sa-east-1 → us-east-1) — activo-pasivo warm standby

Mecanismo: Aurora Global Database (réplica us-east-1, lag < 1 s) · DynamoDB Global Tables · S3 CRR (RTC < 15 min) · AWS DMS CDC del PostgreSQL WMS on-premise (lee wal_level=logical; si la VPN cae, encola y reanuda sin pérdida).

Objetivos: RTO ≤ 4 h / RPO ≤ 15 min (RNF-20.06); RPO declarado de mensajes no críticos ≤ 24 h, reducido a ≤ 15 min para los críticos con patrón outbox dual-write.

Modalidad justificada (RT-07.01): activo-pasivo; activo-activo duplicaría la infraestructura transaccional (~105 TPS peak) con reconciliación de doble escritura sin beneficio frente al RTO comprometido.

Procedimiento: decisión de failover manual con disparador declarado (health check de la región primaria < 5 min) y protección contra conmutación innecesaria (confirmación SNS + autorización); pasos 4–7 automatizados por AWS Systems Manager Automation (promoción Aurora 15–20 min, escalado ECS, actualización DNS 45–60 min). El RTO se cumple porque la réplica es legible y la región DR está "caliente" (escalable < 30 min a carga completa).

Retorno (failback): procedimiento documentado en 6 pasos — re-sincronización con catch-up verificado, reconciliación de transacciones de la contingencia contra la bitácora (RT-03.12), transferencia de eventos pendientes, conmutación coordinada de DNS, validación funcional e informe con tiempo real.

Pruebas: conmutación real ≥ 2 veces/año con informe de RTO/RPO efectivos y plan de corrección de brechas (RT-07.07, Art. 20).

Residencia y transferencia internacional de datos (Art. 23 · Ley 21.719): la replicación hacia us-east-1 constituye una transferencia internacional de datos personales y se rige por los resguardos declarados en la arquitectura de seguridad: cifrado con CMK gestionada por el CLIENTE, acuerdo de tratamiento con cláusulas de transferencia, minimización (la región secundaria no se explota analíticamente, solo sostiene continuidad), exclusión de los datos de geolocalización de personas de la replicación transfronteriza —permanecen solo en sa-east-1 con retención de 12 meses— y registro en el inventario de tratamientos. La residencia queda sujeta a aprobación expresa del CLIENTE; si no la aprueba, la alternativa declarada es la continuidad intrarregional dentro de sa-east-1 (tercera AZ ampliada + respaldo inmutable regional — no es un segundo sitio geográfico ni usa Talca/Concepción para la carga cloud; AWS no tiene región en Chile), que cubre falla de AZ y corrupción de datos pero degrada el RTO ante una caída de toda la región sa-east-1 (24–72 h desde el respaldo inmutable; alternativa D del ADR-09).


#### DRP local (Talca → Concepción)

Promoción controlada del WMS edge (VM-C01) mediante procedimiento de 5 pasos; Concepción ya opera autónoma (latencia ≤ 1 s de picking, RNF-05.01). RTO +1–2 h para la bodega.

Identidad sin conmutación local: el maestro Keycloak está en la nube y las cachés A-05/VM-C03 siguen validando firmas offline — el DRP de identidad es la misma autoridad en nube, sin promoción local a maestro (elimina una clase entera de riesgos de DR).


#### DRP de la identidad

El maestro vive en la nube (Multi-AZ) con réplica DR us-east-1; las cachés locales son de solo lectura. No existe maestro local a promover, por lo que la identidad no depende del switchover.


### Respaldos — esquema 3-2-1-0

Esquema único para toda la arquitectura híbrida (nube + on-premise):


> **Tabla 68** — 5. Respaldos — esquema 3-2-1-0 (RNF-20.07) · 5 filas · ver planilla del subdocumento

D-05 (NAS local con WORM) es la copia local de recuperación rápida y NO cuenta como la pierna inmutable; permite restaurar el WMS en ≤ 4 h (RNF-20.06) sin depender del enlace WAN. RPO ≤ 15 min por AWS DMS CDC del WAL lógico (wal_level=logical) hacia la nube antes de la copia local.

Custodia física (RT-06.26/06.27/06.28): medio de respaldo transportable, cifrado y rotado semanal (RT-07.10), trasladado bajo custodia acreditada a bóveda externa distinta del sitio primario; la pierna inmutable S3 es complementaria, no reemplaza la custodia física.

Plan AWS Backup:


> **Tabla 69** — 5. Respaldos — esquema 3-2-1-0 (RNF-20.07) · 6 filas · ver planilla del subdocumento

Vault Lock con enfriamiento de 3 días y retención mínima de 1 año; una vez bloqueado, ni la cuenta raíz puede eliminar respaldos. Retención sanitaria: trazabilidad 5 años + vida útil (D.S. 977/96), consistente con el lago analítico S3 y el repositorio de datos históricos (RT-05.15).

## Dimensionamiento y plan de capacidad

Volúmenes, concurrencia, crecimiento y umbrales de desempeño. Cierra las dieciséis dimensiones del numeral 14.2 del caso con su valor, su método y su supuesto.


### Criterios y método de dimensionamiento

El dimensionamiento se deriva de la volumetría real del Caso (Tabla 14.1 / Cap. 14 y 15), no de promedios genéricos, dado el perfil de carga no plano (RT-09.02):


> **Tabla 72** — 1. Criterios y método de dimensionamiento (RT-09.01, RT-09.02) · 5 filas · ver planilla del subdocumento

Reglas que gobiernan el dimensionamiento:

- **Carga de diseño (RNF-19.04).** peak de septiembre (2.600 entregas/día) × 1,5 = 3.900 entregas/día toleradas sin degradación.
- **Transacciones por segundo de diseño.** ráfaga de 3 veces el régimen, unas 105 transacciones por segundo, según se deriva más abajo en la concurrencia.
- **Crecimiento (RT-09.03).** la solución soporta tres veces la volumetría inicial sin rediseño en tres años, con la misma topología, según detalla el plan de capacidad.
- **Umbrales (RT-09.01).** percentil 95 en toda medición, con un umbral declarado por cada operación.
- **Sin capacidad ociosa financiada (RT-15.01).** el cómputo elástico en nube escala automática (ADR-12); el on-premise se dimensiona al margen útil sin sobrecompra.
- **Coherencia interna.** los totales de esta parte concuerdan con la Tabla 14.1 (volumetría) y con el dimensionamiento on-premise y de nube de esta misma sección, y con los ADR (ADR-01, 04, 10, 12 y Decisiones N° 28 y N° 30 del registro de decisiones (Subdocumento 3)).


### Volumetría de referencia (Tabla 14.1 Caso 02)


#### Valores base de dimensionamiento


> **Tabla 73** — 2.1 Valores base de dimensionamiento · 13 filas · ver planilla del subdocumento

Nota de coherencia (instalaciones): la Tabla 14.1 y RT-21.16 reportan 6 instalaciones (7 a tres años); el despliegue físico ubica cómputo en los 5 sitios on-premise listados + borde en terreno (calle y 14.200 puntos). La divergencia entre cinco y seis instalaciones, que enfrenta la tabla de volumetría con el capítulo 8 del caso, está declarada en las consultas al mandante (Art. 43.3) y no altera el dimensionamiento: el cómputo se emplaza en los 5 sitios, la 6.ª instalación es de red/almacenamiento sin nodo de cómputo propio.


#### Proyección a 3 años (Caso 02)


> **Tabla 74** — 2.2 Proyección a 3 años (Caso 02) · 8 filas · ver planilla del subdocumento

Los recursos se dimensionan, además, para 3× la volumetría inicial sin rediseño (RT-09.03): la proyección real del Caso a 3 años (+16–19 %) queda muy por debajo del límite de diseño, dejando margen ante crecimiento mayor al modelado (ADR-12).


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


> **Tabla 80** — 4.3 Almacenamiento (ADR-10, RT-03.14) · 4 filas · ver planilla del subdocumento


#### Ancho de banda WAN por sitio


> **Tabla 81** — 4.4 Ancho de banda WAN por sitio (RT-03.20 / RNF-13.08) · 3 filas · ver planilla del subdocumento

Estos valores son los mismos que declara la arquitectura de despliegue al describir las redes, con red privada virtual doble por centro de distribución.


### Dimensionamiento nube


> **Tabla 82** — 5. Dimensionamiento nube (ADR-12) · 9 filas · ver planilla del subdocumento

Escalado automático (RT-09.04):

- **Predictivo + reactivo (ADR-12).** pre-warm en agosto de las tareas ECS, concurrencia reservada Lambda y EventBridge; reactivo con Target Tracking en < 2 min · aprovisionamiento en < 3 min · cooldown 60 s.
- **Serverless-first.** DynamoDB On-Demand, Lambda y EventBridge escalan sin configuración adicional; la capacidad se paga por uso (sin capacidad ociosa financiada, RT-15.01).


### Plan de capacidad y crecimiento 3× sin rediseño

El crecimiento se absorbe con el mismo diseño (sin cambio de topología, VLAN, réplica ni nube):


> **Tabla 83** — 6. Plan de capacidad y crecimiento 3× sin rediseño (RT-09.03) · 5 filas · ver planilla del subdocumento

En nube, el 3× se absorbe por auto-scaling (Fargate 2→6, Celery 2→4, Lambda hasta 500, Aurora xlarge + readers), sin rediseño arquitectónico — misma decisión ADR-12 que fija el límite de elasticidad del peak.


### Umbrales de desempeño


> **Tabla 84** — 7. Umbrales de desempeño (RT-09.01 — Tabla 15, percentil p95) · 7 filas · ver planilla del subdocumento

Los umbrales se verifican con monitoreo OTel/Prometheus (CloudWatch) y se verifican en preproducción con las pruebas de carga y estrés.


### Primer cuello de botella

VM-02 (PostgreSQL — escritura transaccional del maestro de bodega) se satura primero a medida que crece la carga: todo el picking (22:00–06:00) y el despacho masivo (05:30–07:00) pasan por el único punto de escritura.


> **Tabla 85** — 8. Primer cuello de botella (RT-09.05) · 1 fila · ver planilla del subdocumento

En nube el equivalente es Aurora (writer + readers); EventBridge/SQS absorben el pico de sincronización 17:00–20:00 (ADR-05).


### Degradación controlada

Enlace WAN: QoS prioriza broker/WAL; colas diferidas fuera de la ventana; conmutación SD-WAN < 30 s entre fibra/Starlink/LTE.

Offline: buffers RabbitMQ de 24 h (RNF-13.01) y buffers OTel de 24 h; reconciliación cronológica e idempotente al reconectar (RT-03.12).

Nube: throttling en API Gateway, timeouts y reintentos con backoff en Celery, DLQ para tareas fallidas.


### Pruebas de carga y estrés


> **Tabla 86** — 10. Pruebas de carga y estrés (RT-09.06 / RT-09.07 — T-13) · 3 filas · ver planilla del subdocumento

Herramientas: k6/Gatling + drivers a medida contra las APIs (svc-erp-integration, svc-broker). Cortes: Etapa 1 (mes 13), Etapa 2 (mes 19), re-ejecución trimestral. Calendario e hitos formales en el Formulario T-13.


### Actualización del plan de capacidad

Gestión de capacidad durante la Operación con proyección trimestral de crecimiento (RT-09.09): consumo real vs. proyectado (vCPU/RAM/almacenamiento/enlace/colas/TPS), con alertas anticipadas de agotamiento al 70 % / 2 semanas y propuesta de ajuste de dimensionamiento y de costo.

Ventana de ampliación conforme al procedimiento RT-08.05 (adición de vCPU/OSD dentro del físico; contrato escalonado de enlaces; 4.º nodo al acercarse al margen). La revisión se apoya en el informe de carga (RT-09.07) como insumo del hito de producción (mes 16).

En nube, la revisión de costos del dimensionamiento elástico evalúa umbrales Target Tracking y concurrencia reservada con al menos 30 días antes del peak de septiembre.

## Capa analítica: emplazamiento y dimensionamiento

Complemento del apartado 6 — Emplazamiento y dimensionamiento de la capa analítica. La capa analítica no es una funcionalidad añadida por iniciativa de la propuesta: es un componente exigido por el numeral 5.4 de las Transversales (RT-05.25 a RT-05.30: capa analítica separada de la transaccional, tableros operacionales y de gestión con filtros por período y unidad organizacional, desagregación hasta el hecho y latencia máxima declarada) y por el Capítulo 18 del caso, que fija OTIF, fill rate y costo de servir como criterios de aceptación. Este apartado declara con qué componentes se materializa, dónde se emplazan y cómo se garantiza que ninguna consulta analítica degrade la operación.

Alcance de lo que no se propone. Conforme a la decisión de diseño sobre analítica avanzada del registro de decisiones, la solución **no incorpora inteligencia artificial ni analítica predictiva** en el alcance contratado, y lo declara de forma fundada como permite el Capítulo 18 de las Transversales (RT-18.01). La capa analítica se entrega preparada —lago de datos en formato columnar y almacén analítico— para incorporarlas cuando el CLIENTE alcance la madurez de datos que hoy no tiene: el caso parte de un 41 % de recepciones sin registro de lote y un 2,3 % de diferencia de inventario, y predecir sobre esa base produce confianza injustificada. El ruteo se resuelve con optimización determinística, auditable y corregible por el planificador, que es lo que pide el criterio de aceptación N° 7 del caso.


### Fundamento normativo


#### Exigencias de las Bases Técnicas Transversales


> **Tabla 89** — 2.1 Bases Técnicas Transversales (RT) · 5 filas · ver planilla del subdocumento

El numeral 5.4 de las Transversales hace de la capa analítica un componente obligatorio y no una funcionalidad adicional: RT-05.25 a RT-05.28 son obligatorios y RT-05.29 fija la latencia máxima según el caso. La analítica predictiva de RT-05.30 es deseable y esta propuesta la declina de forma fundada, conforme a RT-18.01.


#### Exigencias del Caso 02

El caso define tres indicadores estratégicos que requieren procesamiento analítico continuo:


> **Tabla 90** — 2.2 Caso 02 — Distribuidora Puelche S.A. · 3 filas · ver planilla del subdocumento

Citas textuales del caso que respaldan la exigencia:

"Mi indicador principal es el OTIF" — Nelson, Gerente Comercial (Cap. 7.1)

"El costo de servir es mi obsesión. Si no sabemos cuánto nos cuesta llegar a cada local, ¿cómo vamos a decidir a quién priorizar?" — Gerente de Finanzas (Cap. 7.2)

"Necesito saber el costo de servir por cliente y por entrega" — Gerente de Finanzas (Cap. 9.8)

Estos indicadores no pueden calcularse sin un componente de analítica que consolide datos transaccionales de múltiples módulos (preventa, transporte, cobranza, telemetría, bodega) y los presente de forma consumible por los gerentes.


### Requerimientos que dependen de la capa analítica

Los requerimientos que esta capa satisface están fichados en el catálogo del subdocumento 3; aquí se listan agrupados por procedencia, para dejar constancia de que ninguno queda sin componente que lo sostenga.

**Propios del módulo (Épica 11).**


> **Tabla 91** — 3.1 Requerimientos propios del módulo (Épica 11) · 8 filas · ver planilla del subdocumento


**No funcionales del módulo.**


> **Tabla 92** — 3.2 Requerimientos no funcionales del módulo · 2 filas · ver planilla del subdocumento


**Requisitos transversales vinculados.**


> **Tabla 93** — 3.3 Requerimientos transversales vinculados al módulo · 4 filas · ver planilla del subdocumento


**De otras épicas, con dependencia de esta capa.**


> **Tabla 94** — 3.4 Requerimientos de otras épicas con dependencia del módulo BI · 11 filas · ver planilla del subdocumento


### Mapeo de requerimientos a componentes de arquitectura


#### Componentes de la capa analítica

El módulo de BI/Analítica se materializa en los siguientes componentes de la arquitectura:


> **Tabla 95** — 4.1 Componentes del módulo BI · 9 filas · ver planilla del subdocumento


#### Flujo de datos analíticos

En texto, el flujo de datos analíticos es: fuentes transaccionales (Preventa App, Bodega WMS, Transporte GPS y Cobranza App) → motor transaccional Aurora PostgreSQL (Preventa, Inventario, Transporte y Cobranza, cada dominio OLTP) → DMS CDC (extracción continua e incremental) → motor analítico Redshift Serverless (dimensiones Tiempo, Cliente, Ruta, Producto, Vehículo y Zona; hechos fact_entregas, fact_costos y fact_inventario; vistas materializadas mv_otif_diario, mv_costo_servir, mv_fill_rate, mv_ocupacion_flota y mv_rentabilidad_cliente) → dos salidas: Tablero Gerencial (Grafana/Angular — RF-11.06 operacional, RF-16.02 para el cliente, RF-16.03 alertas) y Distribución por correo (SES + Celery Beat — informes semanal y mensual, RF-11.01).


#### Justificación del desacople entre lo analítico y lo transaccional

El RNF-11.02 exige que las consultas analíticas no degraden los tiempos de respuesta transaccionales. Esto se resuelve mediante:

- **Motor separado.** Redshift Serverless es un sistema OLAP independiente de Aurora PostgreSQL (OLTP). Las cargas analíticas corren en un clúster dedicado con recursos aislados.
- **Extracción asíncrona.** DMS CDC copia cambios de Aurora → Redshift sin bloquear transacciones OLTP. La extracción es incremental y continua.
- **Vistas materializadas pre-calculadas.** Los indicadores (OTIF, Fill Rate, Costo de Servir) se calculan como vistas materializadas en Redshift, que se refrescan periódicamente (cada 5–15 min según RNF-11.01). Las consultas de tablero leen de estas vistas, no de tablas crudas.
- **Caché Redis para tableros.** Los resultados de consultas frecuentes se cachean en ElastiCache Redis, reduciendo aún más la carga sobre Redshift para dashboards de alta concurrencia.
- **Resultado.** Picking en bodega mantiene latencia ≤ 1s y preventa ≤ 1.5s (RF de bodega/preventa) mientras los gerentes consultan tableros analíticos simultáneamente.


### Componente de costo de servir

El cálculo del Costo de Servir (RF-11.02) es el requerimiento analítico más complejo del módulo, ya que consolida datos de 4 fuentes distintas:


> **Tabla 96** — 5. Componente de Costo de Servir · 8 filas · ver planilla del subdocumento

La fórmula de rentabilidad neta resultante (RF-11.08):

Margen neto = Ingreso por venta − Costo de mercadería − Costo de servir real

Donde el Costo de servir real = Σ(componentes anteriores) por cliente y por entrega.


### Componente de alertas de negocio

Las alertas por síntomas de negocio se distinguen de las alertas de infraestructura en que miden impacto al negocio, no estado de servidores:


> **Tabla 97** — 6. Componente de Alertas de Negocio (RF-16.03) · 7 filas · ver planilla del subdocumento


### Requerimientos de tableros

Las Bases exigen tableros con las siguientes capacidades:


> **Tabla 98** — 7. Requerimientos de tableros (RT-05.25, RT-05.26) · 7 filas · ver planilla del subdocumento


#### Tablero operacional


> **Tabla 99** — 7.1 Tablero operacional (RF-11.06) · 5 filas · ver planilla del subdocumento


#### Tablero gerencial


> **Tabla 100** — 7.2 Tablero gerencial (RF-11.01) · 2 filas · ver planilla del subdocumento


### Cumplimiento de Bases Administrativas


> **Tabla 101** — 8. Cumplimiento de Bases Administrativas · 3 filas · ver planilla del subdocumento


### Cobertura y cierre

**Conteo por origen normativo.**


> **Tabla 102** — 9.1 Conteo por origen · 4 filas · ver planilla del subdocumento


**Conteo por tipo de requerimiento.**


> **Tabla 103** — 9.2 Conteo por tipo de requerimiento · 3 filas · ver planilla del subdocumento


**Cierre.**

Veinticinco requerimientos de la propuesta dependen de esta capa y son trazables a su origen normativo. Sin ella no hay forma de medir los tres compromisos que el caso convierte en criterio de aceptación —OTIF por sobre 95 %, fill rate por sobre 97 % y costo de servir conocido y gestionable por cliente y por entrega—, y por eso su emplazamiento y su dimensionamiento forman parte de esta parte física y no de una fase posterior.



## Registro de decisiones de arquitectura

Registro consolidado de las quince decisiones de arquitectura que condicionan esta propuesta. Es entregable contractual conforme a RT-02.04 y se mantiene actualizado durante toda la ejecución. Para cada decisión se indica la alternativa escogida, las alternativas descartadas con el motivo de rechazo, y el criterio de selección. Todas las decisiones fueron aprobadas entre el 05 y el 06 de septiembre de 2026.


### ADR-01 · Estilo arquitectónico

**Decisión adoptada.** Monolito modular Django 5.x LTS / Python 3.12, desplegado en ECS Fargate con apps por dominio y límites de contexto DDD. Módulos críticos (WMS offline, shipper, workers, portal) en procesos separados.

**Alternativas descartadas.** *Microservicios EKS*: 20+ servicios con mesh Istio; rechazada porque el volumen (~105 TPS, 31 K pedidos/mes) está dos órdenes de magnitud bajo el umbral que los justifica, y 4 personas no operan 9–13 componentes de plano de control. TCO +USD 40–70 K en 56 meses sin beneficio funcional. *Monolito clásico (WMS 2013)*: sin fronteras de módulo, proveedor desaparecido; viola RT-02.02.

**Criterio de selección.** Pertinencia al volumen real (BTT §2.3); operabilidad por 4 personas; TCO 56 meses; despliegue independiente de componentes críticos sin particionar el dominio. Trazabilidad: RT-02.01/02.02/02.03 · RT-09.05 · BA Art. 16 · RNF-19.01–04. Relacionada: D5, D8, D14 (Arq. Lógica).

### ADR-02 · Conectividad WAN

**Decisión adoptada.** Tri-camino por sitio con SD-WAN: fibra + Starlink LEO + LTE dual (2 proveedores). Starlink principal en cross-docks, respaldo en CDs. Conmutación automática < 30 s.

**Alternativas descartadas.** *Fibra + LTE puro*: no resuelve Los Ángeles 03:00–05:00 (torre 4G falla en la ventana de operación) ni Concepción sin respaldo. *VSAT GEO*: latencia 500–700 ms RTT; penaliza RNF-05.01 y costo superior.

**Criterio de selección.** Cobertura de la ventana crítica 05:30–07:00 con caminos de física distinta; TCO USD ~58 K / 56 meses justificado como prima de resiliencia (costo de un día sin despacho >> costo del enlace); cero mantención de radio para 4 personas. Trazabilidad: RT-03.10/03.17 · RT-10.05 · RNF-13.01/13.07/13.08 · Caso Cap. 6.12/8. Relacionada: Decisión 16.1 N° 26.

### ADR-03 · Modelo de despliegue híbrido

**Decisión adoptada.** Borde operacional on-premise (WMS maestro Talca, edge Concepción, mini-WMS cross-docks) + carga principal en AWS (ECS, Aurora, IoT, analítica, respaldo). 11 componentes on-prem, 12 híbridos, 13 nube pura.

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

**Decisión adoptada.** Reemplazo total en Etapa 1 por módulo WMS del monolito (ADR-01), desplegado en Talca (maestro), Concepción (edge) y cross-docks (mini-WMS E-01). Migración por dominio, oleadas por sitio, plan de reversión azul-verde.

**Alternativas descartadas.** *Mantener e integrar*: proveedor desaparecido, sin soporte ni roadmap; no soporta multi-sitio, picking FEFO, SSCC GS1 ni conteo cíclico ciego. *Extender a otros sitios*: arrastra riesgo de soporte inexistente en ventana crítica 05:30–07:00.

**Criterio de selección.** Requisitos funcionales (RF-02.x) que el WMS 2013 no contempla; riesgo operacional inaceptable de sistema sin soporte; TCO amortizado con reducción de conteo 2,3 %→~0,3 % y merma 1,7 %→<1 %; reversión garantizada por despliegue azul-verde. Trazabilidad: RT-05.11–15 · RT-03.10 · RNF-02.01/05.01 · Caso 16.1 N° 14. Relacionada: Decisión 16.1 N° 14 (delegada por el CLIENTE).

### ADR-09 · Estrategia DR

**Decisión adoptada.** Activo-pasivo warm standby multi-región: réplica continua DMS CDC + Aurora WAL hacia us-east-1; DRP local Talca→Concepción (RTO +1–2 h); pruebas reales 2×/año; respaldo 3-2-1-0 con S3 Object Lock.

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

**Decisión adoptada.** Plataforma única en nube: instrumentación OpenTelemetry, colectores ADOT on-premise con buffer 24 h en disco, métricas en AMP (13 meses), logs en CloudWatch (12+24 meses), trazas en X-Ray (30 d), tableros Grafana OSS.

**Alternativas descartadas.** *Prometheus+Grafana+Loki autoadministrado local + plataforma cloud*: constituye dos plataformas (viola Art. 16.4 y RT-03.16 que exigen «la misma»); VM-06 no tiene capacidad para sostenerlo. *Solo CloudWatch nativo*: pierde compatibilidad PromQL/Grafana y portabilidad de reglas de alerta.

**Criterio de selección.** Art. 16.4 y RT-03.16 piden una plataforma, no dos; buffer ADOT resuelve «sin puntos ciegos» durante corte; ninguna decisión de la ventana 05:30–07:00 depende de un tablero; sin lock-in (OTel + AMP/PromQL + Grafana OSS portables); 4 personas no operan servidores de observabilidad. Trazabilidad: BA Art. 16.4 · RT-03.16 · RT-14.01–09 · RT-09.01 · Art. 16.3. Relacionada: D14 (Arq. Lógica).

### ADR-15 · Gestión de secretos

**Decisión adoptada.** AWS Secrets Manager (secretos con rotación: ERP, SII, Transbank, certificados AS2/EDI) + SSM Parameter Store (config no sensible). Consumo outbound por VPC Endpoint. Cifrado con CMK KMS y separación de funciones. Cuenta de emergencia en sobre sellado offline.

**Alternativas descartadas.** *HashiCorp Vault autoadministrado*: modo sellado tras reinicio exige intervención humana de madrugada; agrega infraestructura a operar. *Sin gestor centralizado (secretos en variables/archivos)*: prohibido por Art. 21.4.

**Criterio de selección.** Componente debe existir en la vista física (estaba declarado pero no emplazado); servicio administrado para 4 personas sin desellado manual; Zero Trust intacto (consumo outbound); separación de funciones Art. 21.2 vía IAM/CloudTrail; contingencia offline independiente de la nube. Trazabilidad: BA Art. 21.4/21.2 · Art. 16.2/16.3 · RT-04.09 · RT-11.09. Relacionada: D13, SEC-01 (Arq. Lógica).


