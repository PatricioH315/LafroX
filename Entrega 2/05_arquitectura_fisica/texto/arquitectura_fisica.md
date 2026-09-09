# Capítulo 4 · Arquitectura Física y de Despliegue de la Solución (Parte 4.2)


## 4.1 Visión General de la Arquitectura Física

La arquitectura física materializa el despliegue híbrido obligatorio del Artículo 16° de las Bases Administrativas: la carga principal corre en nube pública AWS, con la región primaria en sa-east-1 (São Paulo, Brasil) y la recuperación ante desastres en us-east-1 (Norte de Virginia, EE. UU.); los componentes on-premise garantizan la continuidad de la operación de bodega, plataformas y terreno durante cortes del enlace.

La lectura única de la red de instalaciones es la del Artículo 16, la Tabla 14.1 y RT-21.16: seis instalaciones en cuatro regiones, de las cuales cinco alojan cómputo —el CD Talca (Sala Técnica Secundaria), el CD Concepción (gabinete de borde) y las tres plataformas de cross-docking de Curicó, Chillán y Los Ángeles— y la sexta es la casa matriz y oficinas centrales de Talca, contigua al CD principal, que no procesa operación logística y consume la nube a través del portal, el BI y el back office (RT-03.22). El §8 del caso menciona «cinco instalaciones»; prevalecen la Tabla 14.1 y RT-21.16, y la divergencia se eleva como consulta al mandante (Art. 43.3) sin alterar el dimensionamiento. La proyección del caso a tres años incorpora una séptima instalación (RT-02.12), absorbida por parametrización y por el gabinete de crecimiento de la sala (R04) sin obras adicionales.

Los principios que gobiernan el diseño son los siguientes:

Carga principal en nube (Art. 16.1): el núcleo transaccional de preventa, reparto y canal moderno, la analítica, la integración y el almacenamiento consolidado se ejecutan en AWS sa-east-1, con escalado elástico para el peak de septiembre.

Autonomía on-premise de primera clase: cada CD opera su WMS, su base PostgreSQL local y su broker de colas por 24 horas sin enlace (RT-03.10); el terreno de preventa y reparto opera la jornada completa (14 horas) sin señal, con la sesión de usuario sostenida por la caché local de identidad (RT-03.10, RNF-13.01).

Cero indisponibilidad en la ventana crítica de despacho (05:30–07:00): todas las decisiones de esa ventana son locales, sin dependencia de la observabilidad centralizada ni del enlace WAN.

Autoridad única de identidad (Modelo B, D6): Keycloak IdP maestro en ECS/Fargate (nube) y cachés locales de solo lectura con TTL de 8 horas en VM-05 (Talca) y VM-C03 (Concepción); no existe maestro on-premise ni promoción local a escritura.

Zero Trust end-to-end (NIST SP 800-207): sin conexiones entrantes a la red on-premise salvo dos excepciones controladas por la VPN (DMS→PostgreSQL y celery-erp-sync→ACL, D-AL-05); todo lo demás es tráfico iniciado desde adentro.

Caminos WAN redundantes en 3 tecnologías: fibra (D-03) + satelital Starlink (D-06) + LTE (D-04) por centro, con proveedores y medios distintos (RT-03.17/RT-03.21) y conmutación automática en menos de 30 segundos.

Respaldo único 3-2-1-1-0: datos activos + copia local de recuperación rápida (NAS D-05) + pierna inmutable en la nube (S3 Object Lock / Backup Vault Lock) + réplica en región secundaria + cero errores de restauración (pruebas semestrales, Art. 20 / RT-07.07).

La arquitectura se describe según el marco TOGAF declarado y la descripción conforme a ISO/IEC/IEEE 42010, coherente con la arquitectura lógica v6.2 (Subdoc. 4.1) y con la Tabla de Emplazamiento componente por componente (Art. 16.2). El detalle de cumplimiento por requerimiento se responde en el Formulario T-12 y el dimensionamiento explícito de la volumetría (numeral 14.2) en el Subdocumento 5.


## (a) Modelo de Emplazamiento Híbrido


> **Tabla 21** — (a) Modelo de Emplazamiento Híbrido · 7 filas · ver planilla del subdocumento

La justificación componente por componente conforme a los criterios del Art. 16.2 (latencia, criticidad operacional, volumen de datos, restricciones regulatorias, disponibilidad de conectividad y costo total de propiedad) se desarrolla en la Tabla de Emplazamiento v06 (§1.0): 36 componentes, 11 on-premise puros, 12 híbridos con pieza en ambos dominios y 13 servicios administrados de nube pura (serie N-01…N-13).


![(a) Modelo de Emplazamiento Híbrido](../Diagramas/ARQF-01_Modelo_emplazamiento_hibrido.png)

Figura 15. Modelo de Emplazamiento Híbrido.


### Instalaciones de la red on-premise

La red on-premise se compone de seis instalaciones (Tabla 14.1 y RT-21.16):

CD Talca (Sala Técnica Secundaria, sala blanca de 32 m²): clúster WMS de 3 nodos, base transaccional on-premise (PostgreSQL 16, VM-02), broker local RabbitMQ (VM-03), capa anticorrupción del ERP (VM-04), caché de identidad (VM-05), telemetría (VM-06), respaldo NAS (D-05) y componentes de sala (UPS N+1, generador 12 kVA con estanque 24 h, clima N+1, seguridad física).

CD Concepción (9.000 m², gabinete de borde): servidor de borde con el WMS en modo reducido (VM-C01), base local (VM-C02), caché de identidad (VM-C03), broker + telemetría (VM-C04) y Gateway IoT Greengrass (B-02); opera 24 h de forma autónoma e independiente de Talca.

Cross-docking de Curicó, Chillán y Los Ángeles: nodo de cómputo industrial (E-01) con mini-WMS y broker local, enlace principal Starlink (D-06) y respaldo LTE dual (2 proveedores).

Casa matriz y oficinas centrales (Talca): sin nodo de cómputo propio; acceso a la nube para administración, planificación y portal de clientes (RT-03.22).

La proyección a 3 años (RT-02.12) incorpora una séptima instalación; el gabinete de crecimiento de la sala (R04) absorbe esa expansión sin obras adicionales en el sitio principal.


## (b) Tecnologías de Software a Utilizar

Las tecnologías se eligen bajo los criterios de neutralidad tecnológica, soporte vigente por los 56 meses contractuales (RT-03.05) y preferencia por servicios administrados y componentes de código abierto con estándares abiertos (RT-03.07), de modo que el CLIENTE conserve la reversibilidad de la solución:


> **Tabla 22** — (b) Tecnologías de Software a Utilizar · 16 filas · ver planilla del subdocumento


### Integración con el ERP y documentos tributarios

El ERP de 2017 no se reemplaza ni se modifica (Cap. 10 del caso): permanece como única fuente de verdad tributaria. La solución entrega los datos de operación a través de la capa anticorrupción (ACL, VM-04) y el ERP emite los documentos tributarios (guía de despacho electrónica, factura, boleta y nota de crédito con folios SII), con acuse de recibo con efectos legales —una sola verdad, un solo emisor (P5.10). El acceso desde la nube a este ERP ocurre únicamente vía la ACL (celery-erp-sync → ACL, nunca escritura directa).


## (c) Implementos a Proveer (Hardware y Software)

El inventario ofertado se agrupa en infraestructura de cómputo y almacenamiento, red y seguridad, dispositivos de terreno y operación, y componentes de sala. Son especificaciones que el CLIENTE adquiere y el adjudicatario instala, integra y mantiene (Art. 14.2). Las cantidades y justificaciones de cada fila se referencian al Formulario T-11.


### c.1 Infraestructura de cómputo y almacenamiento


> **Tabla 23** — c.1 Infraestructura de cómputo y almacenamiento · 5 filas · ver planilla del subdocumento


### c.2 Red y seguridad


> **Tabla 24** — c.2 Red y seguridad · 12 filas · ver planilla del subdocumento


### c.3 Dispositivos de terreno y operación


> **Tabla 25** — c.3 Dispositivos de terreno y operación · 13 filas · ver planilla del subdocumento

Gateway IoT + Greengrass (B-02): 2 unidades (Talca y Concepción), ADAM-6000, con runtime AWS IoT Greengrass Core embebido para detección de excursión y buffer local de 14 h.


### c.4 Resumen del inventario ofertado


> **Tabla 26** — c.4 Resumen del inventario ofertado · 28 filas · ver planilla del subdocumento


## (d) Especificaciones Data Center Primaria (CD Talca)

El recinto técnico principal se habilita en las instalaciones del CLIENTE (CD Talca) como Sala Técnica Secundaria, con disponibilidad de infraestructura de nivel TIER II (99,741 %, ≈ 22,7 h/año de corte), redundancia N+1 en energía y climatización y generador propio. El programa considera ≈ 173 m² y 14 recintos (sala blanca de 32 m², NOC de 14 m², sala de UPS/baterías, sala de climatización, sala de extinción, MMR y acometidas, sala de custodia, patio de generador, entre otros), dando cumplimiento a RT-06.01 a RT-06.34 y RT-10.01:

El detalle de la disposición y de los 14 recintos está declarado en la sección de Arquitectura de Seguridad de este documento (§12, seguridad física del sitio primario).

Energía: UPS doble conversión on-line 6 kVA con configuración N+1 y banco VRLA con autonomía ≥ 30 min a plena carga (RT-06.07); grupo electrógeno de 12 kVA con estanque para 24 h y contrato de reabastecimiento (RT-06.08); transferencia automática red↔generador con prueba mensual con carga real (RT-06.10); PDU verticales A/B por gabinete con medidor (RT-08.04); factor de potencia ≥ 0,95 (RT-06.11).

Climatización: 2 CRAC de precisión ≈ 12.000 BTU/h en N+1, con free cooling, pasillo frío confinado y rango ASHRAE TC 9.9 de 18–27 °C y 40–60 % HR medido a la toma de aire del equipo (RT-06.13 y RT-06.14); PUE de diseño 1,7 con medición continua en 2 puntos y reporte trimestral.

Incendios: detección temprana por aspiración AnaLASER (RT-06.16); extinción con agente limpio FM-200 conforme NFPA 75/2001 con botón de aborto (RT-06.17); extintores ABC y CO₂ por recinto (RT-06.18).

Seguridad física: 4 capas de acceso con biometría facial y resguardo AFIS, esclusa antipassback y bitácora electrónica, una persona a la vez y acompañada (RT-06.20, RT-06.21 y RT-06.23); 12 puertas controladas y 7 cámaras IP con retención ≥ 30 días integradas al control de acceso (RT-06.24); NOC de 14 m² contiguo a la sala con ventana interior («ver sin entrar», RT-06.29/30); sensores ambientales DCIM/BMS (RT-06.14).

Custodia de medios (RT-06.26/27/28): recinto de 10 m² en la segunda línea, sin luz UV (≤ 300 lux), 40–60 % HR, ventilación forzada y 18–27 °C; medio cifrado transportable rotado semanalmente a bóveda externa bajo custodia acreditada con cadena de custodia y bitácora; la pierna inmutable S3 es complementaria, no la reemplaza.

Cableado y comunicaciones: cableado estructurado Cat6A F/UTP + fibra OM4 certificado enlace por enlace (RT-06.04) sobre piso técnico de 40 cm, jerarquía ANSI/TIA-942 ENI→MDA→HDA→ZDA→EDA, con dos ductos de ingreso independientes (RT-06.32); 4 racks 42U en gabinete de servidores y comunicaciones separados (RT-06.05), con el cuarto (R04) reservado al crecimiento a 3 años.

Los componentes de sala ofertados se detallan a continuación:


> **Tabla 27** — (d) Especificaciones Data Center Primaria (CD Talca) · 13 filas · ver planilla del subdocumento


## (e) Especificaciones Data Center Secundario y Recuperación ante Desastres

Se declara una modalidad activo/pasiva tibia (warm standby) con tres polos: CD Talca activo, CD Concepción activo autónomo y la réplica Aurora pasiva promueble en AWS us-east-1 (a ≈ 7.700 km de sa-east-1 y ≈ 8.500 km de Talca, sin amenazas comunes según RT-07.02). La región secundaria mantiene una réplica reducida pero funcional del stack, escalable en menos de 30 min:

RTO/RPO: RTO ≤ 4 h y RPO ≤ 15 min para los servicios críticos (RT-07.04); la réplica Aurora Global mantiene un retraso típico < 1 s, alarmado a los 5 y 15 min (RT-07.03) y la replicación S3 CRR con RTC cumple un RPO < 15 min.

Conmutación/retorno: failover en 8 pasos semiautomáticos (detección Route 53 < 5 min, promoción Aurora, escalado ECS Fargate, DNS, validación) con los pasos 4–7 automatizados mediante AWS Systems Manager Automation (RT-07.08); retorno (failback) en 6 pasos con reconciliación determinista de las transacciones generadas durante la contingencia (RT-07.05 y RT-07.06).

Pruebas: conmutación real dos veces al año (semestral, Art. 20 / RT-07.07) midiendo RTO y RPO efectivos con informe al CLIENTE, junto con la restauración mensual verificada con cero errores (3-2-1-1-0, RNF-20.07).

Respaldos 3-2-1-1-0 (esquema único nube + on-premise): la pierna «1 inmutable» vive en la nube (S3 Object Lock en modo Compliance + AWS Backup Vault Lock, RT-07.09 y RT-07.11); el NAS on-premise (D-05, WORM local + clave CMK independiente) es la copia local de recuperación rápida (RTO 4 h, RNF-20.06); la bóveda de custodia física externa completa la copia offsite (RT-06.26 y RT-06.28).

Los componentes del sitio secundario se detallan a continuación:


> **Tabla 28** — (e) Especificaciones Data Center Secundario y Recuperación ante Desastres · 6 filas · ver planilla del subdocumento


## Niveles de Servicio de Infraestructura

La infraestructura sostiene los niveles de disponibilidad del Capítulo 7 y el compromiso contractual del Artículo 78° (transacción de negocio crítica de extremo a extremo ≥ 99,9 %). La clasificación por servicio (RT-10.02) y su error budget son:

Crítico (≥ 99,9 %): transacción de terreno de extremo a extremo (pedido→entrega→POD) y WMS on-premise (picking/recepción), por detener preventa, reparto y facturación y por la ventana nocturna sin contingencia.

Alto (≥ 99 %): portal de clientes (stock, crédito, estado de cuenta) y telemetría IoT de cadena de frío en línea.

Medio: BI/analítica (reportes diferibles, latencia ≤ 4 h).

Bajo: notificaciones y comunicaciones (disponibles en colas).

La Sala Técnica Secundaria se dimensiona en TIER II (99,741 %) —clasificación de la infraestructura del recinto, no el SLO extremo a extremo— con cutover on-premise de 24 h (RT-03.10) y prueba de DR semestral, de modo que la cadena de disponibilidad nube→sala→borde→terreno queda declarada y medible para el CLIENTE, con compromiso contractual ≥ 99,9 % mensual de la transacción crítica de extremo a extremo (RT-10.01).


## Operación Desconectada (RT-03.10 a RT-03.13)


> **Tabla 29** — Operación Desconectada (RT-03.10 a RT-03.13) · 5 filas · ver planilla del subdocumento


## Arquitectura de Integración

Apartado 3 del Subdocumento 4 (T-22) — Arquitectura de integración: servicios, contratos, mensajería, versionado y gobierno. Marco: BA Art. 16.4 (bitácora de reconciliación) · Art. 19 (acoplamiento débil) · Art. 21 (Zero Trust) · Art. 23 (OpenAPI/AsyncAPI, versionado y obsolescencia) · BTT RT-02.06–02.09/02.14 · RT-03.11/03.12/03.13 · RT-05.16–05.23 · RT-10.08.

Por qué la integración es una capa de primera clase en Puelche. El caso no describe un sistema legado único que reemplazar: describe un tejido de sistemas —ERP de 2017 sin documentación de interfaces, WMS de 2013 con proveedor desaparecido, una preventa cuyo proveedor ya no existe, planillas y papel— más 14.200 puntos de entrega, 10 empresas transportistas y un hito externo contractual (enero de 2029, condiciones comerciales de la principal cadena de supermercados). El riesgo de este proyecto no está en construir módulos: está en las costuras.


### 1. Principios de integración


> **Tabla 30** — 1. Principios de integración · 9 filas · ver planilla del subdocumento


### 2. Vista de integración

En texto, la vista de integración se organiza en cuatro dominios con tráfico saliente desde el terreno y el on-premise hacia la nube:

Terreno (offline-first): C-01 App Preventa (62 preventistas), C-02 App Reparto (~200 conductores) y C-03 HHT bodega (120 concurrentes).

On-premise (5 sitios con cómputo): A-01 Motor WMS (M1, M2 y M5 en modo wms_only), A-03 RabbitMQ (buffer 24 h), A-04 capa anticorrupción (frontera única del ERP), B-02 Greengrass (buffer 14 h) y E-01 mini-WMS cross-dock (ventana de 3 h).

Nube AWS sa-east-1: Amazon API Gateway (Capa 3), Capa 4 con M1–M12 en Django + workers Celery, N-09 SQS FIFO, N-09 EventBridge, M11 Hub EDI GS1 (EANCOM · GS1 XML · EPCIS) y N-08 IoT Core.

Terceros: ERP 2017 (sin documentación de interfaces), SII (DTE y guía electrónica), cadenas de supermercados (hito enero 2029), Transbank Webpay/POS, GIS/mapas y notificaciones.

El flujo del tráfico: el terreno llama a la puerta de enlace (API Gateway); los HHT y el WMS publican al broker (A-03); el cross-dock (E-01) publica sus eventos críticos directo a SQS FIFO y solo el detalle del mini-WMS viaja a Talca — lo crítico no depende de Talca (D-AL-04); Greengrass envía por IoT Core; y la Capa 4 consume las colas y alcanza el ERP únicamente a través de la capa anticorrupción (A-04), con una sola puerta hacia el legado. Las flechas desde el dominio on-premise hacia la nube son todas salientes.


### 3. Catálogo de servicios de integración (RT-05.16 · RT-05.21)

El catálogo es el registro único de integraciones. Cada entrada tiene identificador estable, módulo dueño, contrato, versión y comportamiento ante falla. Vive versionado junto al código y se publica en el portal interno de desarrolladores servido por Amazon API Gateway (Capa 3).


### 3.1 Integraciones internas — superficies y plano híbrido


> **Tabla 31** — 3.1 Integraciones internas — superficies y plano híbrido · 9 filas · ver planilla del subdocumento


### 3.2 Integraciones externas — plataforma y terceros


> **Tabla 32** — 3.2 Integraciones externas — plataforma y terceros · 8 filas · ver planilla del subdocumento

Número de integraciones declarado: 15 (8 internas, 7 externas). El numeral 14.2 del caso exige declarar además el volumen de mensajes por integración. Los volúmenes de negocio están arriba; su traducción a mensajes por día es una de las celdas que debe cerrarse (hallazgo D1 de la auditoría de coherencia del Subdocumento 4).


### 4. Contratos (RT-05.16 · RT-05.18 · Art. 23)


> **Tabla 33** — 4. Contratos (RT-05.16 · RT-05.18 · Art. 23) · 6 filas · ver planilla del subdocumento


### 4.1 Eventos canónicos del dominio

Los eventos son el vocabulario del sistema. Se nombran en pasado, son inmutables y llevan event_id (UUID), occurred_at, site_id y transaction_id.


> **Tabla 34** — 4.1 Eventos canónicos del dominio · 11 filas · ver planilla del subdocumento


### 5. Mensajería (RT-02.06 · RT-02.07 · ADR-05)


> **Tabla 35** — 5. Mensajería (RT-02.06 · RT-02.07 · ADR-05) · 5 filas · ver planilla del subdocumento

Garantías declaradas:

Entrega al menos una vez, con deduplicación en el consumidor. No se promete entrega exactamente una vez: se promete idempotencia verificable.

Orden por partición, no orden global. La partición es el sitio o la entidad de negocio, según el evento.

DLQ por cola con retención declarada, monitoreada por el equipo de operación y con bandeja de excepciones cuando el mensaje afecta a un tercero (EDI, DTE).

Reintento con retroceso exponencial y variación aleatoria; cortacircuitos sobre ERP, SII y Transbank; mamparos por integración: un fallo del ERP no degrada la preventa.

Reconciliación determinista: al reconectar, el conflicto de stock se resuelve por la regla de reserva declarada, nunca por marca de tiempo, y la decisión queda en la bitácora del Art. 16.4.


### 6. Costuras híbridas — amarre con la arquitectura física

La vista de integración y la vista física describen los mismos puntos de contacto. Esta tabla es el amarre entre ambas y se lee junto a la sección Costuras híbridas (§6) de este mismo Subdocumento.


> **Tabla 36** — 6. Costuras híbridas — amarre con la arquitectura física · 13 filas · ver planilla del subdocumento


### 7. Capa anticorrupción y estrangulamiento del legado (RT-05.20 · RT-02.14 · ADR-08 · ADR-11)

Frontera única del ERP (A-04). El ERP de 2017 no tiene documentación de interfaces. En vez de descubrir su forma real dentro de cada módulo, se levanta una sola frontera: la ACL expone hacia adentro un contrato OpenAPI 3.1 propio de Puelche y absorbe hacia afuera la forma del ERP. Consecuencias:

El conocimiento del ERP queda concentrado y documentado en un solo componente, no disperso en doce módulos.

Ningún módulo, portal ni cadena de supermercados escribe al ERP: celery-erp-sync publica notificaciones por SQS y lee contratos por la ACL.

Cuando una capacidad del ERP se absorbe en la plataforma, se retira de la ACL sin tocar a los consumidores.

Estrangulamiento del WMS de 2013 (ADR-08). El WMS se reemplaza en la Etapa 1 por los módulos M1, M2 y M5 del monolito. Durante la coexistencia el legado queda detrás de la misma ACL, con una tabla de «capacidad absorbida» —recepción GS1, slotting, misiones de picking con HHT, conteo cíclico— que se vacía ola a ola por sitio, con estrategia azul-verde y plan de reversión.

Hub EDI GS1 (ADR-11). Una cadena nueva se incorpora por configuración de perfil (equivalencias GTIN por cadena, RF-12.03), no por desarrollo. El hub mapea cada cadena contra un modelo canónico GS1, no contra el ERP: es exactamente lo que evita construir una integración distinta por cada cadena (Cap. 17.4, punto 10 del caso).


### 8. Versionado y política de obsolescencia (RT-05.17 · Art. 23)


> **Tabla 37** — 8. Versionado y política de obsolescencia (RT-05.17 · Art. 23) · 8 filas · ver planilla del subdocumento


### 9. Gobierno de la capa de integración (Art. 19 · RT-05.16 · Cap. 14 BTT)


> **Tabla 38** — 9. Gobierno de la capa de integración (Art. 19 · RT-05.16 · Cap. 14 BTT) · 8 filas · ver planilla del subdocumento


### 10. Carga y descarga masiva de datos (RT-05.22)


> **Tabla 39** — 10. Carga y descarga masiva de datos (RT-05.22) · 5 filas · ver planilla del subdocumento

Regla: ninguna carga masiva se ejecuta dentro de la ventana crítica 05:30–07:00, y toda carga queda registrada y es auditable.


### 11. Funciones que no operan sin conexión (RT-03.13)

La declaración formal que exige RT-03.13 vive en la Tabla de Emplazamiento v06 (§1.1) y en la Arquitectura Lógica v6.2 (§9.5). Desde la vista de integración la regla es una sola:

Lo transaccional crítico de terreno y de bodega opera sin conexión (14 h en terreno, 24 h en el centro de distribución). Lo que depende de la nube o de un tercero degrada con procedimiento manual declarado y sin pérdida de datos.

Ninguna función de la ventana crítica de despacho (05:30–07:00) depende de una integración externa: el DTE se timbra de forma diferida con folio reservado, el cobro se captura como pendiente, la excursión térmica se detecta y bloquea localmente, y la ruta ya está cargada en el dispositivo.


### 12. Referencias cruzadas con las decisiones de arquitectura


> **Tabla 40** — 12. Referencias cruzadas con las decisiones de arquitectura · 7 filas · ver planilla del subdocumento


### 13. Trazabilidad normativa (resumen)


> **Tabla 41** — 13. Trazabilidad normativa (resumen) · 20 filas · ver planilla del subdocumento


## Arquitectura de Seguridad

Apartado 4 del Subdocumento 4 (T-22) — Arquitectura de seguridad: modelo Zero Trust, capa expuesta, identidad, cifrado y controles. Marco: BA Art. 21 (seguridad y ciberseguridad) · Art. 22 (identidad, acceso y sesiones) · Art. 23 (datos y residencia) · Art. 16.3/16.4 · BTT Cap. 11 (RT-11.01–11.28), Cap. 12 (RT-12.01–12.13), RT-03.15/03.18/03.22, RT-16.07/16.09 · NIST SP 800-207 · ISO/IEC 27001:2022 · STRIDE · Ley 21.719 · Ley 19.799.

Es además el documento de seguridad del subdocumento: es autocontenido y los valores aquí declarados no son nuevos salvo donde se indica expresamente (consolidan lo comprometido en este mismo Subdocumento 4.2).

Por qué la seguridad de Puelche no es la de una oficina. El perímetro de esta solución no es un edificio: son 62 preventistas de pie en la puerta de un almacén, ~200 conductores —de los cuales ~160 no son trabajadores de la compañía y rotan sin aviso—, dispositivos compartidos entre turnos en una cámara a −22 °C, un turno de preparación con 38 % de rotación anual y 14.200 puntos de entrega. Un modelo de seguridad basado en la red corporativa aquí no protege nada. Por eso el modelo es Zero Trust y por eso la identidad es la pieza central.


### 1. Principios rectores


> **Tabla 42** — 1. Principios rectores · 9 filas · ver planilla del subdocumento


### 2. Modelo Zero Trust aplicado (Art. 21.1 · NIST SP 800-207)


### 2.1 Los siete principios de NIST SP 800-207 en Puelche


> **Tabla 43** — 2.1 Los siete principios de NIST SP 800-207 en Puelche · 8 filas · ver planilla del subdocumento


### 2.2 Zonas y flujos

En texto, las zonas y su flujo son: la zona pública (clientes del canal moderno, transportistas ≈160 conductores y 180 proveedores) ingresa únicamente por la DMZ en nube (CloudFront + AWS WAF v2 + Shield Advanced → Amazon API Gateway con OIDC, cuotas, esquema y validación de carga útil); la zona de aplicación (ECS Fargate M1–M12 + workers y Keycloak IdP maestro como autoridad única) sirve a las zonas de datos (Aurora PostgreSQL, DynamoDB y S3 con Object Lock, en subredes privadas sin salida); la zona on-premise (VLAN 10 MGT · 20 SRV · 30 OPS · 40 WKS · 50 IOT, firewall D-01 UTM en HA como Customer Gateway y caché Keycloak de solo lectura TTL 8 h) conecta con la nube por VPN/IPsec saliente; y la zona de terreno (apps Kotlin offline-first + MDM; HHT compartidos en cámara a −22 °C) no tiene perímetro.

Reglas de zona declaradas:

La única exposición pública es la DMZ en nube (CloudFront → WAF → API Gateway). Las consolas internas no pasan por ahí: entran por intranet o VPN (RT-03.22).

La zona de datos no tiene salida a internet y se consume por VPC Endpoints/PrivateLink.

Desde la zona on-premise no se acepta ninguna conexión entrante salvo las dos excepciones D-AL-05.

La zona de terreno no tiene perímetro: se protege con identidad, cifrado local, MDM y borrado remoto.


### 3. Capa expuesta (Art. 21.2 · RT-11.11/11.13)


> **Tabla 44** — 3. Capa expuesta (Art. 21.2 · RT-11.11/11.13) · 9 filas · ver planilla del subdocumento


### 3.1 Superficie de exposición completa (RT-11.13)


> **Tabla 45** — 3.1 Superficie de exposición completa (RT-11.13) · 9 filas · ver planilla del subdocumento

Regla declarada: ningún nodo on-premise abre puertos entrantes. Toda gestión remota entra por el agente SSM sobre HTTPS saliente o por la VPN, nunca por un puerto publicado.


### 4. Identidad, acceso y sesiones (Art. 22 · BTT Cap. 12 · ADR-06)


### 4.1 Modelo de identidad (Modelo B)

Autoridad única en nube, cachés locales de solo lectura. El Keycloak IdP maestro vive en ECS Fargate (sa-east-1, Multi-AZ, respaldo en Aurora) y concentra todas las escrituras: altas, bajas, cambios de rol, políticas y revocaciones. En VM-05 (Talca) y VM-C03 (Concepción) operan cachés locales de solo lectura con TTL de 8 h que validan la firma OIDC de forma local. No existe un maestro on-premise ni promoción local a escritura.

Esta decisión resuelve un problema real del caso: el centro de distribución debe autenticar durante 24 h sin enlace y el terreno durante 14 h sin señal, pero un segundo maestro on-premise habría creado dos fuentes de verdad de identidad y un procedimiento de conmutación con riesgo de divergencia. Con el Modelo B, el DRP de identidad es la misma autoridad en nube: no hay nada que promover.


> **Tabla 46** — 4.1 Modelo de identidad (Modelo B) · 4 filas · ver planilla del subdocumento

Sincronización sin conexiones entrantes: el maestro publica el Realm cifrado a S3 y las cachés lo importan (INT-13, saliente). Las altas, bajas y roles se propagan desde el maestro hacia las cachés, nunca a la inversa. Revocación: Δ ≤ 8 h por TTL y < 24 h por SCIM; para identidades de alta sensibilidad la baja se refuerza con el bloqueo del terminal por MDM.


### 4.2 Federación, SSO y factores (Art. 22)

OpenID Connect y OAuth 2.1, con SAML 2.0 disponible si la integración con el CLIENTE lo requiere; integración con el directorio corporativo por LDAP.

Inicio de sesión único para todos los módulos y cierre de sesión propagado (back-channel logout).

MFA obligatoria para administradores, accesos privilegiados y todo acceso desde fuera de la red corporativa.

Factores resistentes a la suplantación: FIDO2/WebAuthn (claves de acceso) disponible y preferente para perfiles administradores, además de TOTP (RT-12.04, deseable, se supera el mínimo).

Acceso de conductores externos: OTP de un solo uso por operación, sin cuenta corporativa (RF-06.08). Es la respuesta al hecho de que ~160 conductores no son trabajadores de la compañía y rotan sin aviso.


### 4.3 Autorización: RBAC más ABAC (RT-12.05)


> **Tabla 47** — 4.3 Autorización: RBAC más ABAC (RT-12.05) · 5 filas · ver planilla del subdocumento


### 4.4 Política de sesión (Art. 22 · RT-12.07/12.12)


> **Tabla 48** — 4.4 Política de sesión (Art. 22 · RT-12.07/12.12) · 12 filas · ver planilla del subdocumento

Discrepancia resuelta (2026-09-06): se concilió el valor del access_token. Prevalece 30 min y es el valor único de la propuesta, declarado en la sección de Arquitectura de Seguridad de este documento (§4, ADR-06).


### 4.5 Autenticación en el perfil operacional de terreno (RT-12.11/12.10 — Según caso)

El caso fija condiciones que descartan la contraseña como mecanismo de terreno: guantes térmicos a −22 °C, uso a una mano durante la descarga, uso de pie y a la intemperie en la puerta del local, dispositivos compartidos entre turnos en bodega y 38 % de rotación anual en preparación. La respuesta declarada:

El operador autentica con conexión al inicio de turno (PIN de 6 dígitos o biometría del dispositivo) y descarga un token cifrado de vida acotada al turno.

Durante el turno el PIN desbloquea el token local; no autentica contra el IdP por transacción. No hay dependencia de red en la ruta.

El dispositivo es un factor de posesión enrolado por MDM; el PIN es el segundo factor. Esto satisface la MFA del Art. 22 sin exigir un segundo dispositivo a alguien que trabaja con guantes.

Los datos locales están cifrados y admiten borrado remoto selectivo (RF-03.16/06.12): se borra la aplicación y su caché, no la información personal del dispositivo.


### 4.6 Gestión de dispositivos (MDM — RT-03.18)


> **Tabla 49** — 4.6 Gestión de dispositivos (MDM — RT-03.18) · 7 filas · ver planilla del subdocumento


### 4.7 Ciclo de vida de la identidad (RT-12.09 · RT-15.05)

Aprovisionamiento ≤ 24 h desde el alta en recursos humanos o en el proveedor: cuenta, permisos por rol canónico y dispositivo enrolado.

Baja efectiva en ≤ 24 h desde la desvinculación (Art. 22): revocación de tokens, borrado remoto del dispositivo y revocación de accesos externos.

Flujo desatendido y auditable, con aprobación del jefe de área, bitácora de aprovisionamiento y revisión semestral de accesos (certificación de identidades).

Auditoría de identidad con no repudio: creación, modificación, elevación y baja de cuentas, con retención declarada (§7).


### 4.8 Accesos privilegiados y cuenta de emergencia (RT-12.06 · RT-12.13)

PAM con acceso a demanda: sin acceso interactivo permanente a producción. La operación excepcional se hace just-in-time por AWS Systems Manager Session Manager, con MFA, aprobación y sesión grabada (RT-11.27).

Cuenta de emergencia (break-glass): fuera de banda, custodiada en bóveda física con doble firma, para contingencia de indisponibilidad del IdP. Su activación exige procedimiento escrito, notificación inmediata a TI y a la gerencia, registro en cadena de custodia y rotación de credenciales tras el uso. Se prueba dos veces al año junto con el simulacro de recuperación ante desastres.


### 5. Cifrado y gestión de claves (Art. 21.2 · RT-11.08/11.09/11.10)


### 5.1 En tránsito


> **Tabla 50** — 5.1 En tránsito · 6 filas · ver planilla del subdocumento


### 5.2 En reposo


> **Tabla 51** — 5.2 En reposo · 7 filas · ver planilla del subdocumento

Rotación y custodia: claves de datos con rotación anual o ante revocación o compromiso; claves maestras según el calendario del proveedor; rotación en línea, sin degradación del servicio. Los respaldos conservan la versión de clave necesaria para una restauración auditable. Separación de funciones en la custodia de claves (Art. 21.2): quien administra la plataforma no administra las claves maestras.


### 5.3 Cifrado a nivel de campo (RT-11.10 — Según caso)

El caso lo declara exigible para cuatro conjuntos de datos. Aplicación declarada:


> **Tabla 52** — 5.3 Cifrado a nivel de campo (RT-11.10 — Según caso) · 5 filas · ver planilla del subdocumento

Gestión de secretos. Los secretos de integración (credenciales del ERP, certificados AS2/EDI, credenciales del SII y de Transbank) se administran en AWS Secrets Manager y SSM Parameter Store, con rotación automática y consumo desde los nodos on-premise por VPC Endpoint saliente, coherente con el principio 4. Prohibición absoluta de secretos embebidos en código, imágenes o archivos de configuración (Art. 21.4).

SEC-01 — resuelta y aplicada (2026-09-06). Se adoptó la alternativa (A): Secrets Manager + SSM Parameter Store, formalizada en ADR-15 y en la D13 de la arquitectura lógica (Subdoc. 4.1), y aplicada en este documento (sección de Arquitectura de Seguridad, §5.3; emplazamiento N-12). El texto original de la decisión se conserva a continuación como fundamento.

(Planteamiento original.) La arquitectura lógica declaraba HashiCorp Vault on-premise como gestor de secretos de la Capa 7, pero Vault no tiene emplazamiento físico en este Subdocumento: no figura en el dimensionamiento on-premise ni en el inventario físico. Alternativas evaluadas: (A) eliminar Vault y usar Secrets Manager/SSM con consumo saliente —menor superficie, servicio administrado (Art. 16.3), sin carga para un equipo de 4 personas, sin nueva máquina virtual ni licencia—; (B) incorporar una máquina virtual Vault en Talca con su alta disponibilidad, respaldo, sellado y costo, y declararla en el inventario y el dimensionamiento. Este documento adopta la alternativa (A) (ADR-15). Si se prefiere (B), debe incorporarse el componente a la arquitectura física y al dimensionamiento. No es admisible dejarlo como está: un componente de seguridad sin emplazamiento incumple el Art. 16.2.


### 6. Clasificación de la información y controles por nivel (RT-11.03)


> **Tabla 53** — 6. Clasificación de la información y controles por nivel (RT-11.03) · 5 filas · ver planilla del subdocumento


### 7. Detección, respuesta y evidencia (Art. 21.3 · RT-11.14 a RT-11.21)


> **Tabla 54** — 7. Detección, respuesta y evidencia (Art. 21.3 · RT-11.14 a RT-11.21) · 12 filas · ver planilla del subdocumento


### 8. Modelado de amenazas STRIDE (Art. 21.1 · RT-11.02)

Cada componente y cada integración externa modela sus amenazas antes de implementarse.


> **Tabla 55** — 8. Modelado de amenazas STRIDE (Art. 21.1 · RT-11.02) · 10 filas · ver planilla del subdocumento


### 9. Seguridad del ciclo de desarrollo (Art. 21.4 · RT-11.22 a RT-11.27)


> **Tabla 56** — 9. Seguridad del ciclo de desarrollo (Art. 21.4 · RT-11.22 a RT-11.27) · 7 filas · ver planilla del subdocumento


### 10. Datos personales, residencia y transferencia internacional (Art. 23 · Ley 21.719)


> **Tabla 57** — 10. Datos personales, residencia y transferencia internacional (Art. 23 · Ley 21.719) · 13 filas · ver planilla del subdocumento

Nota (2026-09-06). Este apartado cierra el hallazgo D2 de la auditoría: la arquitectura declaraba la región secundaria y su distancia, pero no la base de licitud ni los resguardos de la transferencia internacional que exige el Art. 23. Los resguardos (c) minimización y (d) exclusión de la geolocalización de personas de la replicación transfronteriza son decisiones de diseño adoptadas y ya propagadas a la sección de Arquitectura de Despliegue de este documento y a S14 de la arquitectura lógica v6.2. La decisión (d) tiene además un fundamento del caso: la geolocalización de personas es el dato con la objeción sindical explícita (L577) y con la retención más corta (12 meses); mantenerlo en una sola jurisdicción reduce la superficie legal sin afectar la continuidad, porque no es un dato necesario para reanudar la operación.


### 10.1 Protocolo ARCOP — derechos de los titulares (Ley 21.719)

Declaración de cumplimiento de los derechos de los titulares sobre los datos personales tratados por la solución:

Derechos cubiertos: acceso, rectificación, cancelación (supresión), oposición, portabilidad y bloqueo temporal. Instrumentación: acceso y portabilidad vía exportabilidad (§10, RT-05.06, formato abierto CSV/JSON con diccionario — lógica §10.8); rectificación y supresión vía ciclo de vida de datos (§10, RT-05.07/05.08) con trazabilidad de cada cambio; bloqueo temporal conforme a la ley en caso de impugnación del titular.

Canal único: correo dedicado y formulario web con acuse de recibo, publicados en la política de privacidad (§10.2). Ningún otro canal inicia el plazo de respuesta.

Plazo: respuesta en 30 días corridos, prorrogables una sola vez por 30 más, con aviso al titular (Art. 11 de la Ley 21.719).

Verificación de identidad: autenticación del titular o su representante (documento de identidad / poder), proporcional al riesgo del dato (reforzada para geolocalización y datos sensibles); registro de cada verificación.

Contraparte responsable (BA Art. 462): el Encargado de Seguridad de la Información coordina la recepción y respuesta de solicitudes y su registro; es la contraparte única e identificable ante los titulares y ante el CLIENTE.

Registro: bitácora de solicitudes ARCOP (qué derecho, quién, cuándo, resolución y plazo real), conservada conforme a la retención de auditoría (§10) y disponible para la Agencia de Protección de Datos Personales.


### 10.2 Política de Privacidad — versión preliminar (aviso al titular, Ley 21.719)

Documento de referencia del aviso informativo a titulares (clientes y trabajadores); versión preliminar anexable al Informe 1:

Responsable: Distribuidora Puelche S.A. (CLIENTE), con el proponente como encargado del tratamiento (cláusulas de tratamiento de datos, BA). Residencia primaria: Chile y AWS sa-east-1.

Datos tratados: identificación y contacto de clientes (14.200 puntos, mayoría personas naturales); comportamiento de pago e historial crediticio del canal tradicional; datos laborales de trabajadores; geolocalización de preventistas (62) y conductores (~200) con finalidad exclusivamente operativa (rutas, verificación de entrega, costo de servir) — sin control de jornada ni cámaras en cabina (decisión D1; objeción sindical L577).

Finalidades: operación comercial y logística (preventa, reparto, facturación), trazabilidad sanitaria obligatoria (D.S. 977/96), seguridad de la información y continuidad (DR/DRP), cumplimiento normativo.

Base de licitud: por tratamiento, según la tabla de §10.5 (Art. 12/13 de la Ley 21.719): geolocalización de trabajadores por ejecución del contrato de trabajo e interés legítimo del empleador (no consentimiento, por desequilibrio; test de proporcionalidad en §10.5); clientes por ejecución de contrato e interés legítimo; obligaciones legales (DTE, trazabilidad sanitaria) por obligación legal; conductores externos por consentimiento del titular. Donde aplique consentimiento, será expreso, informado, específico y revocable, con registro de la revocación.

Destinatarios y transferencias: AWS (encargado, ISO/IEC 27018) y subencargados declarados (BA 73.4); transferencia internacional a us-east-1 solo bajo los resguardos del Art. 23 (§10); geolocalización de personas excluida de la replicación transfronteriza.

Retención y eliminación: por categoría (§10): geolocalización 12 meses; trazabilidad sanitaria 5 años; documentos tributarios 6 años; eliminación certificada al término del contrato (Art. 85 BA).

Derechos del titular: acceso, rectificación, supresión, oposición, portabilidad y bloqueo temporal; cómo ejercerlos en §10.1 (canal dedicado, plazo 30 + 30 días).

Seguridad: medidas declaradas en este documento — cifrado a nivel de campo (RT-11.10), RBAC/ABAC, registro de consultas a datos sensibles (RT-16.09), Zero Trust (NIST SP 800-207).

Brechas: notificación al CLIENTE en ≤ 24 h (RT-11.19); el CLIENTE, como responsable, cumple la notificación ante la Agencia de Protección de Datos Personales y los titulares afectados.

Portales de canal moderno (N-01/N-02/N-03) y cookies: no se instrumentan cookies de terceros ni analítica de seguimiento; en caso de solicitarse, se implementará un banner de consentimiento de cookies conforme a la Ley 21.719 y un aviso específico del portal.


### 10.3 Evaluación de Impacto sobre Protección de Datos (EIPD) — alcance preliminar

Procedencia: BA Art. 462 (evaluación de impacto "cuando corresponda") y Ley 21.719 (tratamientos de alto riesgo). El caso la gatilla: tratamiento masivo de datos personales (14.200 clientes) y monitoreo sistemático de personas (GPS de ~260 trabajadores).

Alcance (criterios): finalidad, base de licitud, categorías (incluidas sensibles: geolocalización, comportamiento de pago), destinatarios, transferencias internacionales (us-east-1), retención por categoría, medidas de seguridad (§10) y riesgos para los titulares (vigilancia de trabajadores, acceso indebido a historial crediticio, exposición de geolocalización).

Tratamientos incluidos: preventa/reparto (geolocalización); gestión de crédito y cobranza (comportamiento de pago); trazabilidad sanitaria lote→cliente (D.S. 977/96); POD (firma/foto); analítica y observabilidad con datos personales.

Resultado comprometido: EIPD según metodología reconocida (p.ej. ISO/IEC 29134 / CNIL PIA): documento de riesgos y controles y veredicto de proporcionalidad; versión final antes de la entrada en producción y actualización ante cualquier cambio de tratamiento.

Entregable: documento formal del proyecto, con versión preliminar anexada al Informe 1 y revisión anual durante la operación.


### 10.4 Vigencia y seguimiento normativo

La Ley 21.719 entra en vigencia el 01-dic-2026 (Diario Oficial 13-dic-2024; vacancia de 2 años). El 31-ago-2026 el Gobierno ingresó el Boletín N° 18.623-07 (Mensaje N° 110-374, urgencia 01-sep-2026), que postergaría su entrada en vigencia al 01-dic-2027, aumenta a 5 los consejeros de la Agencia y amplía la primera amonestación a todos los responsables. Al cierre de esta versión es proyecto de ley, aún no publicado: mientras tanto rige el calendario 01-dic-2026. La propuesta es robusta a ambas fechas por diseño: se alinea contra el articulado completo ya publicado y la operación (contrato de 56 meses) cae dentro del régimen cualquiera sea la fecha; ninguno de los controles de este §10 depende de la fecha de vigencia.


### 10.5 Base de licitud por tratamiento (Ley 21.719, Art. 12 y 13)

Cierre de la decisión de base de licitud. La regla general de la ley es el consentimiento (Art. 12), salvo que concurra alguna de las bases distintas al consentimiento (Art. 13): ejecución de contrato, obligación legal, interés vital o interés legítimo del responsable. Cada tratamiento del caso declara su base, su fundamento y sus garantías:


> **Tabla 58** — 10.5 Base de licitud por tratamiento (Ley 21.719, Art. 12 y 13) · 8 filas · ver planilla del subdocumento

Garantías transversales de esta tabla:

RAT (registro de actividades de tratamiento): entregable del proyecto; cada fila se formaliza con finalidad, categorías, plazos, destinatarios y medidas (§10, control ISO 5.31/5.34).

Sensibilidad: geolocalización y comportamiento de pago se tratan como categorías sensibles que el caso identifica (RT-05.08/RT-11.10), con cifrado de campo y registro de consultas; la geolocalización se apoya en la excepción laboral/contractual de la ley, no en un consentimiento general.

Consentimiento donde aplique (uso no contractual de clientes, conductores externos): expreso, informado, específico y revocable, con registro de la revocación.

Menores de edad: la solución no trata datos de NNA; si un cliente resultara menor de 14 años, el consentimiento corresponderá a padres o representantes, y entre 14 y 18 al titular con asistencia, conforme la ley.

Ciclo de vida: eliminación certificada al término del contrato (Art. 85 BA) y retención por categoría (§10).


### 11. Matriz de controles ISO/IEC 27001:2022 (RT-11.05)

Referencia única de controles para toda la solución, nube y on-premise. El Dimensionamiento on-premise v05 §8.4 se apoya en esta matriz.


> **Tabla 59** — 11. Matriz de controles ISO/IEC 27001:2022 (RT-11.05) · 19 filas · ver planilla del subdocumento


### 12. Seguridad física (BTT Cap. 6)

La seguridad física del sitio primario se declara en la sección de Arquitectura de Seguridad de este documento (§12). Resumen de lo que sostiene esta arquitectura:

Cuatro capas de acceso hasta la sala blanca, con biometría facial (AFIS de respaldo) y esclusa con antipassback; acceso de a una persona con reverificación (RT-06.23).

CCTV IP con retención ≥ 30 días y respaldo en medio secundario auditable, cubriendo cada puerta controlada (RT-06.24).

Recinto de custodia de medios de 10 m² con condiciones ambientales declaradas, e inventario con rotación y registro de todo movimiento (RT-06.26 a RT-06.28).

Acceso de terceros (fabricantes, mantenedores, auditores) con acompañamiento obligatorio y registro (RT-06.25).

Control de dispositivos extraíbles en los nodos on-premise y borrado seguro verificable de los medios que salen de servicio.


### 13. Referencias cruzadas con las decisiones de arquitectura


> **Tabla 60** — 13. Referencias cruzadas con las decisiones de arquitectura · 9 filas · ver planilla del subdocumento


### 14. Trazabilidad normativa (resumen)


> **Tabla 61** — 14. Trazabilidad normativa (resumen) · 25 filas · ver planilla del subdocumento


## Arquitectura de Despliegue

Apartado 5 del Subdocumento 4 (T-22) — Arquitectura de despliegue: ambientes, redes, alta disponibilidad, recuperación ante desastres y respaldos. Marco: BA Art. 16 (híbrido) · Art. 20 (DR) · Art. 21–22 (seguridad) · BTT RT-03.xx / RT-04.xx / RT-07.07 / RT-10.01. Corresponde a la vista de despliegue (ISO/IEC/IEEE 42010, RT-02.03) de la arquitectura híbrida y es autocontenido: consolida los valores declarados en las secciones de este mismo Subdocumento 4.2.


### 1. Ambientes de despliegue (RT-04.01)

Los cinco ambientes obligatorios del numeral 4.1 de las Bases Técnicas Transversales están habilitados como condición del hito H3 (RT-04.01), aislados entre sí mediante cuentas AWS separadas bajo una organización centralizada de AWS Control Tower (aislamiento estricto + SCP):


> **Tabla 62** — 1. Ambientes de despliegue (RT-04.01) · 6 filas · ver planilla del subdocumento

Reglas que gobiernan el modelo de ambientes:

Paridad Pre-Producción = Producción (RT-04.02): topología, versiones de componentes y configuración equivalentes; las diferencias por costo se declaran y justifican una a una.

On-premise como producción (RT-04.01/RT-03.10): el despliegue on-premise es producción con la imagen única wms_only; esa misma imagen recorre Dev→QA→PreProd en la nube antes del cutover en Talca (ventana de 24 h) y en Concepción. No se mantienen ambientes on-premise separados — la paridad la garantizan la imagen única y el IaC versionado (RT-03.03).

Entrega continua (RT-04.05): el pipeline CI ejecuta compilación, pruebas unitarias, análisis estático, análisis de composición, escaneo de secretos y escaneo de imágenes de contenedor, con bloqueo automático del despliegue ante hallazgos críticos o altos (RT-11.22).

Despliegue sin interrupción (RT-04.07): estrategia azul-verde con canario en etapas, demostrada en PreProducción antes de cada paso a producción; reversión automatizada (RT-04.06).

Configuración externalizada (RT-04.08): un mismo artefacto se promueve QA→PreProd→Prod sin recompilación; los secretos viven en gestor de secretos con rotación automática (RT-04.09), sin credenciales embebidas.

Datos no productivos (RT-11.25): Dev, QA y PreProd usan datos sintéticos generados desde la volumetría del Cap. 14 del caso; las plantillas próximas a producción pasan por anonimización/seudonimización verificable (Amazon Macie).

Sin acceso interactivo a producción (RT-11.27): los despliegues son exclusivamente por pipeline; el acceso administrativo excepcional es just-in-time vía AWS Systems Manager Session Manager con MFA, aprobación y sesión grabada.

Reducción de ambientes no productivos fuera de horario (RT-04.13): Dev/QA/PreProd se apagan o reducen fuera del horario de uso, con el ahorro reflejado en la estructura de costos.

Portal web (N-01/N-02/N-03): la SPA Angular se publica por ambiente en S3+CloudFront (bucket y distribución por cuenta AWS) y su backend es la misma imagen Django del ambiente; entra a producción con el hito de enero 2029 (RNF-12.01).


### 2. Redes (topología, segmentación y conectividad)


### 2.1 WAN — tri-camino con SD-WAN (RT-03.17)

Cada instalación dispone de caminos físicamente independientes con conmutación automática en < 30 s (el requisito exige ≤ 5 min declarados; el diseño opera en < 30 s):


> **Tabla 63** — 2.1 WAN — tri-camino con SD-WAN (RT-03.17) · 5 filas · ver planilla del subdocumento

SD-WAN con políticas centralizadas y BGP; los cross-docks salen directo por Starlink a SQS/IoT/SSM (configuración crítica) y sincronizan detalle a Talca por AMQPS entre brokers (C-13). La pérdida total del enlace se cubre con la autonomía local 24 h (CD) / 14 h (terreno) — RT-03.10, RNF-13.01.


### 2.2 VPN Site-to-Site (costura C1)

Extremos: D-01 Firewall/UTM (HA activo-pasivo) → Customer Gateway en cada CD; extremo cloud VGW del VPC Hub.

Protocolo: IPsec/IKEv2, AES-256-GCM, BGP, MTU 1436; 2 túneles (activo + standby). Conmutación < 30 s sobre los tres caminos.


### 2.3 Segmentación de red (sin solapamiento)


> **Tabla 64** — 2.3 Segmentación de red (sin solapamiento) · 6 filas · ver planilla del subdocumento

Modelo Hub-and-Spoke con VPC de tránsito central: la comunicación cross-VPC pasa por el Transit Gateway (inspección) y los servicios AWS (S3, SQS, DynamoDB, KMS, SSM) se consumen por VPC Endpoints/PrivateLink sin tráfico por internet (RT-03.03).


### 2.4 Zero Trust — flujos permitidos (BA Art. 21)

Todo el tráfico on-premise → nube es outbound (HTTPS/443, MQTTS/8883) sin conexiones entrantes salvo las dos excepciones controladas D-AL-05 sobre túnel IPsec autenticado:


> **Tabla 65** — 2.4 Zero Trust — flujos permitidos (BA Art. 21) · 10 filas · ver planilla del subdocumento


### 2.5 Capa pública (DMZ) y DNS

Primera línea: CloudFront + AWS WAF v2 (OWASP Top 10 + reglas personalizadas) + Shield Advanced; autenticación API Gateway con Keycloak OIDC, cuotas por cliente y validación de esquema (RT-11.11).

DNS: Route 53 con health checks activos; routing por latencia en operación normal y failover automático hacia us-east-1 en contingencia.


### 3. Alta disponibilidad


### 3.1 Capa cloud (sa-east-1) — Multi-AZ


> **Tabla 66** — 3.1 Capa cloud (sa-east-1) — Multi-AZ · 8 filas · ver planilla del subdocumento

SLA de extremo a extremo sobre la transacción crítica de negocio ≥ 99,9 % mensual (RT-10.01, < 8,76 h/año), distinto de la clasificación TIER II del recinto (que es un medio, no el compromiso contractual).


### 3.2 Capa on-premise


> **Tabla 67** — 3.2 Capa on-premise · 8 filas · ver planilla del subdocumento

VMs dimensionadas con headroom ×1,5 (RNF-19.04) para tolerar 3.900 entregas/día en el peak de septiembre. SPOF declarados y mitigados (RT-02.11): periféricos de andén (respaldo manual), clúster Talca sin SPOF estructural, Concepción nodo único (autonomía 24 h + DRP), cross-dock mini-PC único (ventana de 3 h + sincronización diferida).


### 4. Recuperación ante desastres (BA Art. 20 · RT-07.07 · RNF-20.06)


### 4.1 DRP nube (sa-east-1 → us-east-1) — activo-pasivo warm standby

Mecanismo: Aurora Global Database (réplica us-east-1, lag < 1 s) · DynamoDB Global Tables · S3 CRR (RTC < 15 min) · AWS DMS CDC del PostgreSQL WMS on-premise (lee wal_level=logical; si la VPN cae, encola y reanuda sin pérdida).

Objetivos: RTO ≤ 4 h / RPO ≤ 15 min (RNF-20.06); RPO declarado de mensajes no críticos ≤ 24 h, reducido a ≤ 15 min para los críticos con patrón outbox dual-write.

Modalidad justificada (RT-07.01): activo-pasivo; activo-activo duplicaría la infraestructura transaccional (~105 TPS peak) con reconciliación de doble escritura sin beneficio frente al RTO comprometido.

Procedimiento: decisión de failover manual con disparador declarado (health check de la región primaria < 5 min) y protección contra conmutación innecesaria (confirmación SNS + autorización); pasos 4–7 automatizados por AWS Systems Manager Automation (promoción Aurora 15–20 min, escalado ECS, actualización DNS 45–60 min). El RTO se cumple porque la réplica es legible y la región DR está "caliente" (escalable < 30 min a carga completa).

Retorno (failback): procedimiento documentado en 6 pasos — re-sincronización con catch-up verificado, reconciliación de transacciones de la contingencia contra la bitácora (RT-03.12), transferencia de eventos pendientes, conmutación coordinada de DNS, validación funcional e informe con tiempo real.

Pruebas: conmutación real ≥ 2 veces/año con informe de RTO/RPO efectivos y plan de corrección de brechas (RT-07.07, Art. 20).

Residencia y transferencia internacional de datos (Art. 23 · Ley 21.719): la replicación hacia us-east-1 constituye una transferencia internacional de datos personales y se rige por los resguardos declarados en la sección de Arquitectura de Seguridad de este documento (§10): cifrado con CMK gestionada por el CLIENTE, acuerdo de tratamiento con cláusulas de transferencia, minimización (la región secundaria no se explota analíticamente, solo sostiene continuidad), exclusión de los datos de geolocalización de personas de la replicación transfronteriza —permanecen solo en sa-east-1 con retención de 12 meses— y registro en el inventario de tratamientos. La residencia queda sujeta a aprobación expresa del CLIENTE; si no la aprueba, la alternativa declarada es la continuidad intrarregional dentro de sa-east-1 (tercera AZ ampliada + respaldo inmutable regional — no es un segundo sitio geográfico ni usa Talca/Concepción para la carga cloud; AWS no tiene región en Chile), que cubre falla de AZ y corrupción de datos pero degrada el RTO ante una caída de toda la región sa-east-1 (24–72 h desde el respaldo inmutable; alternativa D del ADR-09).


### 4.2 DRP local (Talca → Concepción)

Promoción controlada del WMS edge (VM-C01) mediante procedimiento de 5 pasos; Concepción ya opera autónoma (latencia ≤ 1 s de picking, RNF-05.01). RTO +1–2 h para la bodega.

Identidad sin conmutación local: el maestro Keycloak está en la nube y las cachés A-05/VM-C03 siguen validando firmas offline — el DRP de identidad es la misma autoridad en nube, sin promoción local a maestro (elimina una clase entera de riesgos de DR).


### 4.3 DRP de la identidad (ADR-06)

El maestro vive en la nube (Multi-AZ) con réplica DR us-east-1; las cachés locales son de solo lectura. No existe maestro local a promover, por lo que la identidad no depende del switchover.


### 5. Respaldos — esquema 3-2-1-1-0 (RNF-20.07)

Esquema único para toda la arquitectura híbrida (nube + on-premise):


> **Tabla 68** — 5. Respaldos — esquema 3-2-1-1-0 (RNF-20.07) · 6 filas · ver planilla del subdocumento

D-05 (NAS local con WORM) es la copia local de recuperación rápida y NO cuenta como la pierna inmutable; permite restaurar el WMS en ≤ 4 h (RNF-20.06) sin depender del enlace WAN. RPO ≤ 15 min por AWS DMS CDC del WAL lógico (wal_level=logical) hacia la nube antes de la copia local.

Custodia física (RT-06.26/06.27/06.28): medio de respaldo transportable, cifrado y rotado semanal (RT-07.10), trasladado bajo custodia acreditada a bóveda externa distinta del sitio primario; la pierna inmutable S3 es complementaria, no reemplaza la custodia física.

Plan AWS Backup:


> **Tabla 69** — 5. Respaldos — esquema 3-2-1-1-0 (RNF-20.07) · 7 filas · ver planilla del subdocumento

Vault Lock con enfriamiento de 3 días y retención mínima de 1 año; una vez bloqueado, ni la cuenta raíz puede eliminar respaldos. Retención sanitaria: trazabilidad 5 años + vida útil (D.S. 977/96), consistente con el lago analítico S3 y el repositorio de datos históricos (RT-05.15).


### 6. Referencias cruzadas con las decisiones de arquitectura


> **Tabla 70** — 6. Referencias cruzadas con las decisiones de arquitectura · 6 filas · ver planilla del subdocumento


### 7. Trazabilidad normativa (resumen)


> **Tabla 71** — 7. Trazabilidad normativa (resumen) · 17 filas · ver planilla del subdocumento


## Dimensionamiento y Plan de Capacidad

Apartado 6 del Subdocumento 4 (T-22) — Dimensionamiento y plan de capacidad: volúmenes, concurrencia y crecimiento. Marco: BA Art. 16 (híbrido) · BTT RT-09.01…09.09 (capacidad y desempeño) · RT-03.20 (ancho de banda) · RNF-19.01–19.04 · T-13. Conforme al numeral 14.2 del Caso (dimensionamiento explícito con método y supuestos, sin celdas vacías): declara la carga de diseño, los supuestos de volumen y crecimiento y sus criterios, como sección autocontenida de este Subdocumento 4.2, con los ADR-01/04/10/12 como referencia interna.


### 1. Criterios y método de dimensionamiento (RT-09.01, RT-09.02)

El dimensionamiento se deriva de la volumetría real del Caso (Tabla 14.1 / Cap. 14 y 15), no de promedios genéricos, dado el perfil de carga no plano (RT-09.02):


> **Tabla 72** — 1. Criterios y método de dimensionamiento (RT-09.01, RT-09.02) · 6 filas · ver planilla del subdocumento

Reglas que gobiernan el dimensionamiento:

Carga de diseño (RNF-19.04): peak de septiembre (2.600 entregas/día) × 1,5 = 3.900 entregas/día toleradas sin degradación.

TPS de diseño: burst ×3 → ~105 TPS (ver §3).

Crecimiento (RT-09.03): la solución soporta 3× la volumetría inicial sin rediseño en 3 años (misma topología, §6).

Umbrales (RT-09.01): percentil p95 en toda medición (Tabla 15), con umbrales por operación (§7).

Sin capacidad ociosa financiada (RT-15.01): el cómputo elástico en nube escala automática (ADR-12); el on-premise se dimensiona al margen útil sin sobrecompra.

Coherencia interna: los totales de este documento concuerdan con la Tabla 14.1 (volumetría) y con las secciones de Dimensionamiento (§4 on-premise, §5 nube) y los ADR (ADR-01, 04, 10, 12 y decisiones 16.1 N° 28 y N° 30).


### 2. Volumetría de referencia (Tabla 14.1 Caso 02)


### 2.1 Valores base de dimensionamiento


> **Tabla 73** — 2.1 Valores base de dimensionamiento · 14 filas · ver planilla del subdocumento

Nota de coherencia (instalaciones): la Tabla 14.1 y RT-21.16 reportan 6 instalaciones (7 a tres años); el despliegue físico ubica cómputo en los 5 sitios on-premise listados + borde en terreno (calle y 14.200 puntos). La divergencia 5/6 (Tabla 14.1 vs §8 del Caso) está declarada en las consultas al mandante (Art. 43.3) y no altera el dimensionamiento: el cómputo se emplaza en los 5 sitios, la 6.ª instalación es de red/almacenamiento sin nodo de cómputo propio.


### 2.2 Proyección a 3 años (Caso 02)


> **Tabla 74** — 2.2 Proyección a 3 años (Caso 02) · 9 filas · ver planilla del subdocumento

Los recursos se dimensionan, además, para 3× la volumetría inicial sin rediseño (RT-09.03): la proyección real del Caso a 3 años (+16–19 %) queda muy por debajo del límite de diseño, dejando margen ante crecimiento mayor al modelado (ADR-12).


### 3. Concurrencia y TPS de diseño


### 3.1 Usuarios y terminales concurrentes


> **Tabla 75** — 3.1 Usuarios y terminales concurrentes · 8 filas · ver planilla del subdocumento


### 3.2 TPS estimados (peor ventana)


> **Tabla 76** — 3.2 TPS estimados (peor ventana) · 5 filas · ver planilla del subdocumento

El burst ×3 absorbe el peak de septiembre y las ráfagas de la ventana de sincronización 17:00–20:00. El ~105 TPS es el valor único de diseño de este documento, citado por ADR-01 y ADR-12, y sustenta el dimensionamiento de IOPS de VM-02 (§4.3) y del escalado ECS (ADR-12).


### 4. Dimensionamiento on-premise (ADR-10)


### 4.1 Cómputo — CD Talca (clúster N+1, 3 nodos Proxmox/Ceph)


> **Tabla 77** — 4.1 Cómputo — CD Talca (clúster N+1, 3 nodos Proxmox/Ceph) · 4 filas · ver planilla del subdocumento

VMs del clúster Talca (familias declaradas en la sección de Dimensionamiento on-premise de este documento, §4):


> **Tabla 78** — 4.1 Cómputo — CD Talca (clúster N+1, 3 nodos Proxmox/Ceph) · 7 filas · ver planilla del subdocumento


### 4.2 Cómputo — Concepción (edge) y cross-docking


> **Tabla 79** — 4.2 Cómputo — Concepción (edge) y cross-docking · 3 filas · ver planilla del subdocumento


### 4.3 Almacenamiento (ADR-10, RT-03.14)


> **Tabla 80** — 4.3 Almacenamiento (ADR-10, RT-03.14) · 5 filas · ver planilla del subdocumento


### 4.4 Ancho de banda WAN por sitio (RT-03.20 / RNF-13.08)


> **Tabla 81** — 4.4 Ancho de banda WAN por sitio (RT-03.20 / RNF-13.08) · 4 filas · ver planilla del subdocumento

Cohesión con el apartado 5 (despliegue): estos valores son los declarados en la sección de Arquitectura de Despliegue de este documento (§2, VPN IPsec dual por CD).


### 5. Dimensionamiento nube (ADR-12)


> **Tabla 82** — 5. Dimensionamiento nube (ADR-12) · 10 filas · ver planilla del subdocumento

Escalado automático (RT-09.04):

Predictivo + reactivo (ADR-12): pre-warm en agosto de las tareas ECS, concurrencia reservada Lambda y EventBridge; reactivo con Target Tracking en < 2 min · aprovisionamiento en < 3 min · cooldown 60 s.

Serverless-first: DynamoDB On-Demand, Lambda y EventBridge escalan sin configuración adicional; la capacidad se paga por uso (sin capacidad ociosa, RT-15.01 — FinOps Cloud §4.5).


### 6. Plan de capacidad y crecimiento 3× sin rediseño (RT-09.03)

El crecimiento se absorbe con el mismo diseño (sin cambio de topología, VLAN, réplica ni nube):


> **Tabla 83** — 6. Plan de capacidad y crecimiento 3× sin rediseño (RT-09.03) · 6 filas · ver planilla del subdocumento

En nube, el 3× se absorbe por auto-scaling (Fargate 2→6, Celery 2→4, Lambda hasta 500, Aurora xlarge + readers), sin rediseño arquitectónico — misma decisión ADR-12 que fija el límite de elasticidad del peak.


### 7. Umbrales de desempeño (RT-09.01 — Tabla 15, percentil p95)


> **Tabla 84** — 7. Umbrales de desempeño (RT-09.01 — Tabla 15, percentil p95) · 8 filas · ver planilla del subdocumento

Los umbrales se verifican con monitoreo OTel/Prometheus (CloudWatch) y se prueban en Pre-Producción (§10).


### 8. Primer cuello de botella (RT-09.05)

VM-02 (PostgreSQL — escritura transaccional del maestro de bodega) se satura primero a medida que crece la carga: todo el picking (22:00–06:00) y el despacho masivo (05:30–07:00) pasan por el único punto de escritura.


> **Tabla 85** — 8. Primer cuello de botella (RT-09.05) · 2 filas · ver planilla del subdocumento

En nube el equivalente es Aurora (writer + readers); EventBridge/SQS absorben el pico de sincronización 17:00–20:00 (ADR-05).


### 9. Degradación controlada (RT-09.08)

Enlace WAN: QoS prioriza broker/WAL; colas diferidas fuera de la ventana; conmutación SD-WAN < 30 s entre fibra/Starlink/LTE.

Offline: buffers RabbitMQ de 24 h (RNF-13.01) y buffers OTel de 24 h; reconciliación cronológica e idempotente al reconectar (RT-03.12).

Nube: throttling en API Gateway, timeouts y reintentos con backoff en Celery, DLQ para tareas fallidas.


### 10. Pruebas de carga y estrés (RT-09.06 / RT-09.07 — T-13)


> **Tabla 86** — 10. Pruebas de carga y estrés (RT-09.06 / RT-09.07 — T-13) · 4 filas · ver planilla del subdocumento

Herramientas: k6/Gatling + drivers a medida contra las APIs (svc-erp-integration, svc-broker). Cortes: Etapa 1 (mes 13), Etapa 2 (mes 19), re-ejecución trimestral. Calendario e hitos formales en el Formulario T-13.


### 11. Actualización del plan de capacidad (RT-09.09)

Gestión de capacidad durante la Operación con proyección trimestral de crecimiento (RT-09.09): consumo real vs. proyectado (vCPU/RAM/almacenamiento/enlace/colas/TPS), con alertas anticipadas de agotamiento al 70 % / 2 semanas y propuesta de ajuste de dimensionamiento y de costo.

Ventana de ampliación conforme al procedimiento RT-08.05 (adición de vCPU/OSD dentro del físico; contrato escalonado de enlaces; 4.º nodo al acercarse al margen). La revisión se apoya en el informe de carga (RT-09.07) como insumo del hito de producción (mes 16).

Nube: revisión FinOps (§4.5 Cloud) — evaluar umbrales Target Tracking y concurrencia reservada con al menos 30 días antes del peak de septiembre.


### 12. Referencias cruzadas con las decisiones de arquitectura


> **Tabla 87** — 12. Referencias cruzadas con las decisiones de arquitectura · 5 filas · ver planilla del subdocumento


### 13. Trazabilidad normativa (resumen)


> **Tabla 88** — 13. Trazabilidad normativa (resumen) · 11 filas · ver planilla del subdocumento


## Inteligencia de Negocios y Analítica Operacional (BI)

Apartado 7 del Subdocumento 4 (T-22) — Justificación del módulo de BI/Analítica. Justifica la existencia, alcance y diseño del módulo de Inteligencia de Negocios (BI) y Analítica Operacional: no es una capa optativa sino un componente obligatorio exigido por las Bases Técnicas Transversales (RT-05.25/05.26 — capa analítica con tableros operacionales y de gestión, filtros por período, unidad organizacional y drill-down; RT-14.02–14.04 — tableros, SLA/SLO sobre experiencia real p95 y alertamiento por síntomas de negocio; RT-16.28 — exportación) y por el Caso 02 (indicadores OTIF, Fill Rate y Costo de Servir). Marco adicional: BA Art. 5° (capacidad analítica como servicio horizontal), Cap. 5 (innovación obligatoria de análisis predictivo) y Art. 39° (acceso y exportación de datos). Fecha de emisión 04/09/2026 · revisión 1.0.


### 1. Objetivo

Este documento justifica la existencia, alcance y diseño del módulo de Inteligencia de Negocios (BI) y Analítica Operacional dentro de la arquitectura propuesta, demostrando que no se trata de una capa optativa sino de un componente obligatorio exigido tanto por las Bases Técnicas Transversales como por el Caso 02. Se presenta la trazabilidad completa desde las fuentes normativas hasta los componentes tecnológicos que lo materializan.


### 2. Fundamento normativo


### 2.1 Bases Técnicas Transversales (RT)


> **Tabla 89** — 2.1 Bases Técnicas Transversales (RT) · 6 filas · ver planilla del subdocumento

Las Bases Técnicas Transversales establecen que la capa analítica es un componente estructural de la plataforma, no una funcionalidad adicional. Su omisión o subdimensionamiento constituiría una observación grave conforme al Art. 10° de las Bases Administrativas.


### 2.2 Caso 02 — Distribuidora Puelche S.A.

El caso define tres indicadores estratégicos que requieren procesamiento analítico continuo:


> **Tabla 90** — 2.2 Caso 02 — Distribuidora Puelche S.A. · 4 filas · ver planilla del subdocumento

Citas textuales del caso que respaldan la exigencia:

"Mi indicador principal es el OTIF" — Nelson, Gerente Comercial (Cap. 7.1)

"El costo de servir es mi obsesión. Si no sabemos cuánto nos cuesta llegar a cada local, ¿cómo vamos a decidir a quién priorizar?" — Gerente de Finanzas (Cap. 7.2)

"Necesito saber el costo de servir por cliente y por entrega" — Gerente de Finanzas (Cap. 9.8)

Estos indicadores no pueden calcularse sin un componente de analítica que consolide datos transaccionales de múltiples módulos (preventa, transporte, cobranza, telemetría, bodega) y los presente de forma consumible por los gerentes.


### 3. Requerimientos funcionales del módulo


### 3.1 Requerimientos propios del módulo (Épica 11)


> **Tabla 91** — 3.1 Requerimientos propios del módulo (Épica 11) · 9 filas · ver planilla del subdocumento


### 3.2 Requerimientos no funcionales del módulo


> **Tabla 92** — 3.2 Requerimientos no funcionales del módulo · 3 filas · ver planilla del subdocumento


### 3.3 Requerimientos transversales vinculados al módulo


> **Tabla 93** — 3.3 Requerimientos transversales vinculados al módulo · 5 filas · ver planilla del subdocumento


### 3.4 Requerimientos de otras épicas con dependencia del módulo BI


> **Tabla 94** — 3.4 Requerimientos de otras épicas con dependencia del módulo BI · 12 filas · ver planilla del subdocumento


### 4. Mapeo de requerimientos a componentes de arquitectura


### 4.1 Componentes del módulo BI

El módulo de BI/Analítica se materializa en los siguientes componentes de la arquitectura:


> **Tabla 95** — 4.1 Componentes del módulo BI · 10 filas · ver planilla del subdocumento


### 4.2 Flujo de datos analíticos

En texto, el flujo de datos analíticos es: fuentes transaccionales (Preventa App, Bodega WMS, Transporte GPS y Cobranza App) → motor transaccional Aurora PostgreSQL (Preventa, Inventario, Transporte y Cobranza, cada dominio OLTP) → DMS CDC (extracción continua e incremental) → motor analítico Redshift Serverless (dimensiones Tiempo, Cliente, Ruta, Producto, Vehículo y Zona; hechos fact_entregas, fact_costos y fact_inventario; vistas materializadas mv_otif_diario, mv_costo_servir, mv_fill_rate, mv_ocupacion_flota y mv_rentabilidad_cliente) → dos salidas: Tablero Gerencial (Grafana/Angular — RF-11.06 operacional, RF-16.02 para el cliente, RF-16.03 alertas) y Distribución por correo (SES + Celery Beat — informes semanal y mensual, RF-11.01).


### 4.3 Justificación del desacople OLAP/OLTP (RNF-11.02)

El RNF-11.02 exige que las consultas analíticas no degraden los tiempos de respuesta transaccionales. Esto se resuelve mediante:

Motor separado: Redshift Serverless es un sistema OLAP independiente de Aurora PostgreSQL (OLTP). Las cargas analíticas corren en un clúster dedicado con recursos aislados.

Extracción asíncrona: DMS CDC copia cambios de Aurora → Redshift sin bloquear transacciones OLTP. La extracción es incremental y continua.

Vistas materializadas pre-calculadas: Los indicadores (OTIF, Fill Rate, Costo de Servir) se calculan como vistas materializadas en Redshift, que se refrescan periódicamente (cada 5–15 min según RNF-11.01). Las consultas de tablero leen de estas vistas, no de tablas crudas.

Caché Redis para tableros: Los resultados de consultas frecuentes se cachean en ElastiCache Redis, reduciendo aún más la carga sobre Redshift para dashboards de alta concurrencia.

Resultado: Picking en bodega mantiene latencia ≤ 1s y preventa ≤ 1.5s (RF de bodega/preventa) mientras los gerentes consultan tableros analíticos simultáneamente.


### 5. Componente de Costo de Servir

El cálculo del Costo de Servir (RF-11.02) es el requerimiento analítico más complejo del módulo, ya que consolida datos de 4 fuentes distintas:


> **Tabla 96** — 5. Componente de Costo de Servir · 9 filas · ver planilla del subdocumento

La fórmula de rentabilidad neta resultante (RF-11.08):

Margen neto = Ingreso por venta − Costo de mercadería − Costo de servir real

Donde el Costo de servir real = Σ(componentes anteriores) por cliente y por entrega.


### 6. Componente de Alertas de Negocio (RF-16.03)

Las alertas por síntomas de negocio se distinguen de las alertas de infraestructura en que miden impacto al negocio, no estado de servidores:


> **Tabla 97** — 6. Componente de Alertas de Negocio (RF-16.03) · 8 filas · ver planilla del subdocumento


### 7. Requerimientos de tableros (RT-05.25, RT-05.26)

Las Bases exigen tableros con las siguientes capacidades:


> **Tabla 98** — 7. Requerimientos de tableros (RT-05.25, RT-05.26) · 8 filas · ver planilla del subdocumento


### 7.1 Tablero operacional (RF-11.06)


> **Tabla 99** — 7.1 Tablero operacional (RF-11.06) · 6 filas · ver planilla del subdocumento


### 7.2 Tablero gerencial (RF-11.01)


> **Tabla 100** — 7.2 Tablero gerencial (RF-11.01) · 3 filas · ver planilla del subdocumento


### 8. Cumplimiento de Bases Administrativas


> **Tabla 101** — 8. Cumplimiento de Bases Administrativas · 4 filas · ver planilla del subdocumento


### 9. Resumen de cobertura


### 9.1 Conteo por origen


> **Tabla 102** — 9.1 Conteo por origen · 5 filas · ver planilla del subdocumento


### 9.2 Conteo por tipo de requerimiento


> **Tabla 103** — 9.2 Conteo por tipo de requerimiento · 4 filas · ver planilla del subdocumento


### 9.3 Conclusión

El módulo de BI/Analítica no es una funcionalidad agregada por iniciativa propia de la propuesta. Es un componente obligatorio exigido por:

Las Bases Técnicas Transversales (RT-05.25, RT-05.26, RT-14.02, RT-14.03, RT-14.04)

El Caso 02 de Logística (indicadores OTIF, Fill Rate, Costo de Servir)

25 requerimientos trazables a las fuentes normativas

Su omisión constituiría una inconsistencia grave con las Bases y haría imposible la medición de los 3 indicadores estratégicos del negocio (OTIF > 95%, Fill Rate > 97%, Costo de Servir conocido y gestionable).


## Decisiones de Arquitectura (ADR-01 … ADR-15)

Apartado 7 del Subdocumento 4 (T-22) — Decisiones de arquitectura (ADR). Registro ADR-01 … ADR-15 en formato MADR, versión v02, estado Aprobadas (2026-09-05 · actualizado 2026-09-06). Marco: TOGAF · ISO/IEC/IEEE 42010 (RT-02.03) · Arquitecturas limpias.

Cambios v01 → v02 (cierre de la auditoría del Subdocumento 4). (1) Se corrigen las cinco menciones a Kong en ADR-01, ADR-06 y ADR-11: la puerta de enlace decidida es Amazon API Gateway (D8, actualizada el 2026-09-05 para alinearse con la vista física). (2) Se incorporan ADR-13 (puerta de enlace de servicios), ADR-14 (plataforma de observabilidad) y ADR-15 (gestión de secretos), que existían como decisiones lógicas sin ADR propio, incumpliendo el apartado 7 del Subdocumento 4 y RT-02.04. (3) Se reapunta el documento de origen a la lógica vigente (Subdoc. 4.1). Empresa proponente: Pendiente de definir (nomenclatura Art. 43.3).

Finalidad. Cada ADR fundamenta y defiende una elección arquitectónica con el mismo rigor que un informe de ingeniería: contexto cuantificado desde el caso, alternativas reales de mercado evaluadas, criterio de selección técnico-económico (TCO, equipo de TI de 4 personas del CLIENTE, latencia, resiliencia), decisión precisa y sus trade-offs con mitigaciones. La trazabilidad normativa usa códigos exactos de las Bases Técnicas Transversales (RT-cc.nn), de las Bases Administrativas (BA Art. n°) y de los capítulos del Caso 02, y se enlaza con las decisiones de la Arquitectura Lógica v6.2 (Dn) y del registro de decisiones del caso (Decisión 16.1 N°).


### Índice de decisiones


> **Tabla 104** — Índice de decisiones · 16 filas · ver planilla del subdocumento


### ADR-01 — Estilo Arquitectónico: Monolito Modular vs. Microservicios

Estado: Aprobado

Fecha: 2026-09-05

Decisiones relacionadas: D5 (Arquitectura Lógica, 2026-09-03, confirmada 09-04); D8 (Amazon API Gateway, actualizada 2026-09-05 — ver ADR-13); D14 (observabilidad de plataforma única, 2026-09-06 — ver ADR-14).

Trazabilidad normativa: BTT RT-02.02 (arquitectura modular, fronteras explícitas, despliegue independiente de componentes críticos) · BTT §2.3 (la sofisticación no reemplaza la pertinencia: microservicios sin volumen que los justifique = error de ingeniería) · RT-02.01 (8 capas) · RT-02.03 (ISO/IEC/IEEE 42010) · RT-09.05 (cuello de botella) · BA Art. 16 (híbrido) · Caso 02 Cap. 14.2/15 (volumetría) · RNF-19.01–04 (capacidad, escalado, cuello de botella, pruebas 1,5×).


### 1. Contexto y Problema

La carga del caso es transaccional y concentrada, pero no plana: ~31.000 pedidos/mes y 260.000 líneas/mes sobre 14.200 clientes y 8.400 productos, con un peak de ~105 TPS en la ventana de despacho (dimensionamiento: ~20 TPS confirmación de picking con 120 terminales, ~8 TPS preventa, ~35 TPS movimientos + sincronización, burst ×3). Pérdidas operacionales traducibles a dinero: conteo cíclico con 2,3 % de diferencia, merma por vencimiento 1,7 % del inventario, OTIF 82,4 % contra meta 95 % y $4,2 millones/mes de descuadre de caja. El equipo de TI del CLIENTE tiene 4 personas para operar la solución completa durante 36 meses de Operación.


### 2. Alternativas Evaluadas


> **Tabla 105** — 2. Alternativas Evaluadas · 4 filas · ver planilla del subdocumento


### 3. Criterio de Selección y Justificación Técnica-Económica

Escala real (BTT §2.3): para 31.000 pedidos/mes y 105 TPS de diseño, el costo de coordinación de 20 servicios supera cualquier ganancia. El umbral donde los microservicios se justifican (típicamente >10³–10⁴ TPS, equipos de 5+ por dominio) está dos órdenes de magnitud por encima del caso.

Equipo de 4 personas (RT-02.02/RT-02.03): un monolito modular tiene 1 artefacto, 1 pipeline, 1 proceso: la reposición de personal y la mantención son lineales. EKS exige 9–13 componentes de plano de control (Kube-apiserver, etcd, Ingress, autoscaler, RBAC, CNI, mesh…) más 20 servicios; el costo fijo de operarlo supera al de la nube usada.

Despliegue independiente (RT-02.02): la modularidad del monolito se materializa en procesos y tareas separables —tarea portal (canal moderno, hito enero 2029), workers Celery (celery-reconciliation, celery-erp-sync), shipper de colas— que escalan y se despliegan de forma independiente sin particionar el dominio.

TCO (56 meses): A y B convergen en cómputo AWS, pero B agrega ~3 nodos EKS dedicados (≈ USD 1.200–1.600/mes) + SRE; A escala con Fargate (2→6 tareas) solo en septiembre (ADr-12). El diferencial B−A se estima en USD 40.000–70.000 en 56 meses por infraestructura y soporte, sin beneficio funcional neto.

Latencia/resiliencia: el monolito modular en nube + borde local (ADR-03) cumple RNF-05.01 (≤1 s) y RNF-02.01 (24 h) porque lo que corre local es el mismo kernel WMS; particionar en servicios no aporta resiliencia adicional y añade saltos de red.


### 4. Decisión Adoptada

Monolito modular en Django 5.x LTS sobre Python 3.12, con apps Django por dominio y límites de contexto explícitos (fundamentos de DDD y módulos de la Arquitectura Lógica v1), desplegado en ECS Fargate (tarea web + tarea portal + workers Celery), con Amazon API Gateway (D8 · ADR-13), observabilidad OpenTelemetry sobre plataforma única en nube (D14 · ADR-14) y borde local por sitio (ADR-03). Los módulos críticos (WMS offline, shipper de reconciliación, workers ERp-sync, tarea portal) se despliegan de forma independiente en procesos separados, satisfaciendo RT-02.02 sin adoptar microservicios.


### 5. Consecuencias, Trade-offs y Mitigaciones


> **Tabla 106** — 5. Consecuencias, Trade-offs y Mitigaciones · 5 filas · ver planilla del subdocumento


### ADR-02 — Conectividad y Redundancia WAN: Starlink LEO + SD-WAN

Estado: Aprobado

Fecha: 2026-09-05

Decisión relacionada: Decisión 16.1 N° 26 (redundancia de enlace de cada sitio).

Trazabilidad normativa: BTT RT-03.17 (enlace redundante con caminos y proveedores distintos, conmutación ≤ 5 min) · RT-03.10 (autonomía 24 h) · RT-03.19 (edge) · RNF-13.01 (autonomía 24 h CD / 14 h terreno) · RNF-13.07 (enlace redundante ≤ 5 min) · RNF-13.08 (ancho de banda dimensionado) · RT-10.05 (ventana crítica 05:30–07:00, indisponibilidad cero) · Caso 02 §6.12/§8 (cortes de fibra, Concepción sin respaldo, Los Ángeles sin señal en madrugada) · BA Art. 16.


### 1. Contexto y Problema

La operación depende del enlace de datos en horarios en que no existe plan manual (Restricción N° 1: indisponibilidad cero 05:30–07:00). Verificado en el caso:

Talca: fibra se corta 4 veces al año sin enlace de respaldo; la bodega debe aguantar 24 h sin enlace.

Concepción: no tiene respaldo alguno.

Cross-docks (Curicó, Chillán, Los Ángeles): conectividad exclusivamente por red móvil; Los Ángeles pierde señal intermitentemente entre las 03:00–05:00, exactamente su ventana de operación de 3 h.

Impacto económico: un día sin despacho de la mañana = operación caída (96 camiones).


### 2. Alternativas Evaluadas


> **Tabla 107** — 2. Alternativas Evaluadas · 4 filas · ver planilla del subdocumento


### 3. Criterio de Selección y Justificación Técnica-Económica

Riesgo funcional: el único escenario que B no resuelve —señal móvil intermitente en Los Ángeles 03:00–05:00— es el que el caso declara crítico. La alternativa A aporta un camino físicamente independiente de las torres 4G (constelación LEO) y de las trincheras de fibra.

RT-03.17/RNF-13.07: conmutación automática ≤ 5 min por diseño SD-WAN (detección de pérdida < 5 s, failover < 30 s según práctica de diseño del sitio); la redundancia de caminos es de física distinta (fibra → satelital → LTE), no solo de proveedor.

Ventana crítica (RT-10.05): el despacho 05:30–07:00 no depende de un único medio; el tri-camino convive con la autonomía local de 24 h (RNF-13.01) para el caso de pérdida total (RT-03.10).

TCO: la oferta Starlink (5 sitios, 56 meses) es USD ~58.236; frente a LTE puro que no cumple el requisito, el costo se justifica como prima de resiliencia del servicio crítico (costo de un día sin despacho >> costo del enlace). FinOps: CAPEX unitario bajo ($350.000 CLP/kit), reposición 15 % por ciclo de vida (RT-08.13).

Equipo de 4 TI: Starlink Enterprise gestionado (cero mantención de infraestructura de radio), SD-WAN con políticas centralizadas; sin ingeniería de redes satelitales in-house.


### 4. Decisión Adoptada

Tri-camino WAN por sitio con SD-WAN: (1) fibra (enlace principal en Talca y Concepción), (2) Starlink Enterprise LEO —principal en los 3 cross-docks (Curicó, Chillán, Los Ángeles) y respaldo automático en los 2 CD— y (3) LTE dual (2 proveedores) con módulo 4G Cat-12. Conmutación automática < 30 s entre caminos (sección de Arquitectura de Despliegue de este documento, §2) y con planes/precios declarados en la oferta (T-11 C27 · T-12 RT-08.13). Los cross-docks salen por Starlink directo a SQS/IoT/SSM (configuración crítica) y sincronizan detalle a Talca por AMQPS entre brokers (RT-03.11).


### 5. Consecuencias, Trade-offs y Mitigaciones


> **Tabla 108** — 5. Consecuencias, Trade-offs y Mitigaciones · 5 filas · ver planilla del subdocumento


### ADR-03 — Modelo de Despliegue Híbrido: Borde Operacional On-Premise vs. Nube AWS

Estado: Aprobado

Fecha: 2026-09-05

Decisiones relacionadas: D7 (AL v1: híbrido + multi-zona + IaC + Zero Trust); Decisión 16.1 N° 17 (asignación de componentes).

Trazabilidad normativa: BA Art. 16.1–16.4 (híbrido obligatorio, carga principal en nube, criterios 16.2, exigencias 16.3/16.4) · RT-03.01 (región primaria/secundaria) · RT-03.02 (multi-AZ) · RT-03.10 (autonomía) · RT-03.19 (edge) · RNF-02.01 (24 h) · RNF-05.01 (≤ 1 s en cámara) · RNF-05.02 (guantes −22 °C) · Caso 02 Cap. 6 (cámara sin cobertura) y Cap. 16.1.


### 1. Contexto y Problema

Tres hechos confluyen: (a) el Art. 16 exige carga principal en nube pública + componentes on-premise (inadmisible solo-nube o solo-on-prem); (b) la cámara de congelado a −22 °C no tiene cobertura de señal y el picking exige ≤ 1 s de confirmación (RNF-05.01), inviable con RTT de 40–80 ms hacia la nube más procesamiento remoto; (c) la bodega debe operar 24 h sin enlace (RNF-02.01/RT-03.10). El perfil de carga es nocturno (22:00–06:00) y de madrugada (05:30–07:00).


### 2. Alternativas Evaluadas


> **Tabla 109** — 2. Alternativas Evaluadas · 4 filas · ver planilla del subdocumento


### 3. Criterio de Selección y Justificación Técnica-Económica

Cumplimiento normativo: solo A satisface Art. 16 en sus cuatro numerales (16.1 híbrido, 16.2 justificación por componente, 16.3 exigencias de nube, 16.4 exigencias on-premise). La tabla maestra de emplazamiento es la sección (a) de este documento (36 componentes).

Latencia (RNF-05.01): el borde local ejecuta la confirmación de picking en el propio sitio; la alternativa nube añade ≥40–80 ms RTT y procesamiento remoto, por encima del umbral de 1 s en la cámara.

Autonomía (RNF-02.01/RT-03.10): el diseño del caso exige supervivencia sin enlace; el maestro local con réplica cloud (DMS CDC, RPO ≤ 15 min) da continuidad (ADR-09) sin depender de la WAN durante el corte.

TCO/equipo: el cómputo local se acota a lo imprescindible (23 componentes on-premise/híbrido), el resto se delega a servicios administrados AWS (ADR-12) — menor costo fijo que un DC propio y menor riesgo que una operación 100 % nube.

Carga principal en nube (Art. 16.1): canal moderno (portales), OLTP cloud, ingesta IoT, analítica/BI, respaldo inmutable y DRP viven en AWS (sa-east-1, DRP us-east-1 — RT-03.01).


### 4. Decisión Adoptada

Arquitectura híbrida obligatoria con borde operacional on-premise: WMS maestro + BD transaccional en Talca (VM-01/VM-02), edge autónomo en Concepción (VM-C01/VM-C02), mini-WMS en cross-docks (E-01), y máxima utilización de AWS administrado (ECS Fargate, Aurora, DynamoDB, IoT Core, S3, Redshift/QuickSight) para la carga principal. Detalle por componente en la sección (a) de este documento.


### 5. Consecuencias, Trade-offs y Mitigaciones


> **Tabla 110** — 5. Consecuencias, Trade-offs y Mitigaciones · 5 filas · ver planilla del subdocumento


### ADR-04 — Persistencia Políglota por Dominio

Estado: Aprobado

Fecha: 2026-09-05

Decisiones relacionadas: D2 (series de tiempo condicionadas al muestreo, consolidado en OLAP); D4 (nube AWS + PostgreSQL/Redis/Aurora/DynamoDB/S3+Redshift); Decisión 16.1 N° 18 (motor por dominio, RT-05.02).

Trazabilidad normativa: BTT RT-05.02 (paradigma, garantías transaccionales y posición CAP por dominio) · RT-05.01 (diccionario de datos) · RT-05.11–05.15 (migración/volúmenes) · RNF-09.01 (retiro < 2 h) · RNF-09.02 (retención 5 años) · RNF-11.02 (OLAP desacoplado del OLTP) · RSA D.S. 977/96 (retención legal de trazabilidad) · Caso 02 Cap. 16.1/16.2 y Cap. 4.9.


### 1. Contexto y Problema

Cada dominio tiene exigencias distintas de consistencia, volumen y retención: pedidos/inventario/trazabilidad demandan ACID y reconciliación determinista tras cortes; la ingesta de sensores y telemetría es escritura masiva de baja latencia; las series de tiempo (temperatura de cámara y camión) requieren compresión y consulta por rango; la analítica exige columnar separado para no degradar picking; y la retención sanitaria impone 5 años de trazabilidad (piso legal) con 6 meses adicionales por vida útil. Un único motor no puede cumplir las cuatro posiciones CAP sin sacrificar desempeño.


### 2. Alternativas Evaluadas


> **Tabla 111** — 2. Alternativas Evaluadas · 7 filas · ver planilla del subdocumento


### 3. Criterio de Selección y Justificación Técnica-Económica

RT-05.02 y CAP: la posición se declara por dominio: transaccional CP (consistencia inmediata; la operación offline y la reconciliación vuelta a línea lo exigen), IoT raw AP (eventual, TTL corto), series de tiempo AP columnar en la capa OLAP, analítica AP columnar. Declarar la posición evita el error de elegir un motor "para todo".

Volumen (RT-05.15): ~31.000 pedidos/mes, 260.000 líneas, 2,4 M unidades y telemetría de 28 sensores + 18 termógrafos → persistencia manejable en PostgreSQL (índices + PostGIS para georreferencia de rutas) con DynamoDB absorbiendo el pico de IoT sin saturar el transaccional (RNF-11.02).

Trazabilidad (RNF-09.01/09.02, D.S. 977/96): el registro de eventos por lote (EPCIS GS1, decisión 16.1 N° 35) se conserva en PostgreSQL (5 años) y su respaldo inmutable replica el piso legal; la réplica Aurora da RPO ≤15 min.

Equipo de 4 TI: tres motores administrados o de bajo mantenimiento (PostgreSQL/Aurora, DynamoDB, Redshift Serverless) — sin motores dedicados exóticos (InfluxDB descartado: segundo motor a operar, D2). La serie de tiempo consolidada no requiere un motor adicional: vive en la capa OLAP (S3 Parquet → Redshift).


### 4. Decisión Adoptada

Persistencia políglota por dominio: PostgreSQL+PostGIS (transaccional WMS on-premise, CP), Aurora PostgreSQL (OLTP cloud + réplica DRP, failover <30 s), DynamoDB (IoT raw, TTL 30 días, AP), S3 (lake analítico 5 años) con Redshift Serverless y QuickSight (OLAP, incluye la serie de tiempo consolidada de temperatura), y S3 Object Lock/Glacier + Backup Vault para retención legal inmutable (RSA D.S. 977/96). La matriz CAP está declarada y trazada a RT-05.02 en este documento (sección de Datos, ADR-04).


### 5. Consecuencias, Trade-offs y Mitigaciones


> **Tabla 112** — 5. Consecuencias, Trade-offs y Mitigaciones · 5 filas · ver planilla del subdocumento


### ADR-05 — Mensajería Asíncrona: Broker Local (RabbitMQ) + Colas Nube (SQS FIFO / EventBridge)

Estado: Aprobado

Fecha: 2026-09-05

Decisión relacionada: D4 (AL v1, capa de mensajería); shipper en VM-03 (D-AL-03).

Trazabilidad normativa: BTT RT-02.06 (idempotencia) · RT-02.07 (deduplicación) · RT-03.12 (sincronización/reconciliación tras reconexión) · RT-03.10 (autonomía) · RNF-07.01 (sincro < 10 min) · RNF-13.01 (24 h) · Zero Trust (BA Art. 21) · Caso 02 Cap. 16.1 (reglas de reintento/devolución).


### 1. Contexto y Problema

El caso exige orden estricto y sin pérdida en la cadena pedido→despacho→cobranza (una línea de preventa fuera de orden rompe la reconciliación determinista), pero la operación transcurre offline: bodega 24 h, terreno 14 h. Además, todo el tráfico debe ser outbound (Zero Trust: sin conexiones entrantes al on-premise). REST síncrono no sobrevive a un corte a mitad de ventana; Kafka aporta orden y durabilidad pero exige operación y no resuelve el broker local por sitio.


### 2. Alternativas Evaluadas


> **Tabla 113** — 2. Alternativas Evaluadas · 4 filas · ver planilla del subdocumento


### 3. Criterio de Selección y Justificación Técnica-Económica

Resiliencia (RT-03.10/RNF-13.01): el broker local retiene transacciones y telemetría durante el corte y las reproduce al reconectar; el shipper publica en orden cronológico e idempotente (idempotency keys, RT-02.06/02.07) a la cola FIFO.

Reconciliación determinista (RT-03.12): celery-reconciliation procesa la cola al recuperar el enlace; claves de idempotencia evitan duplicados (RT-02.07) y el orden de publicación por entidad garantiza consistencia en el maestro.

Zero Trust (BA Art. 21): SQS FIFO se consume via VPC Endpoint SQS/PrivateLink (HTTPS/443); AMQPS 5671 queda solo entre brokers on-premise (cross-dock → Talca). No se abren puertos entrantes.

TCO/equipo: RabbitMQ (este) + SQS/EventBridge (administrados) > Kafka (+MSK) para 105 TPS; el costo operativo de operar clústeres Kafka en 5 sitios es desproporcionado para 4 personas.


### 4. Decisión Adoptada

Capa de mensajería híbrida: RabbitMQ (A-03) como broker de colas offline en cada sitio (buffers 24 h), con shipper en VM-03 (modo wms_only) que publica el buffer hacia SQS FIFO (VPC Endpoint / HTTPS 443) con idempotencia; EventBridge como bus de eventos de negocio (eventos que disparan ERP-sync, alertas, auditoría) y AWS IoT Core (MQTT) para la ingesta edge (ADR-04/ADR-12). Workers celery-reconciliation y celery-erp-sync procesan en nube. Declarado en la sección de Arquitectura de Integración de este documento (§5, ADR-05).


### 5. Consecuencias, Trade-offs y Mitigaciones


> **Tabla 114** — 5. Consecuencias, Trade-offs y Mitigaciones · 5 filas · ver planilla del subdocumento


### ADR-06 — Identidad y Autenticación Híbrida (Modelo B): Keycloak IdP Maestro en Nube + Caché Local de Solo Lectura

Estado: Aprobado

Fecha: 2026-09-05

Decisiones relacionadas: D6 (AL v1, 2026-09-04: Keycloak IdP maestro, Modelo B); Decisión 16.1 N° 34 (credenciales de usuarios externos sin correo).

Trazabilidad normativa: BTT RT-12.10 (aprovisionamiento ≤ 24 h) · RT-12.11 (autenticación en perfil operacional: guantes, rotación 38 %, dispositivos compartidos) · RT-12.12 (credenciales de externos sin correo) · RT-03.10/RNF-13.01 (offline 24 h CD / 14 h terreno) · BA Art. 22 (MFA para acceso externo) · RF-15.01–15.05 (identidad centralizada) · RF-06.08 (OTP conductores externos ≤ 2 min) · Caso 02 Cap. 16.1 N° 34.


### 1. Contexto y Problema

La operación exige autenticación incluso sin enlace: la bodega trabaja 24 h y el terreno 14 h desconectados, con 62 preventistas y ~200 conductores (de 10 transportistas externos) sin correo corporativo, dispositivos compartidos entre turnos y rotación de personal de preparación de 38 % anual. Un IdP solo-nube paraliza la bodega ante un corte; un maestro local tradicional (AD) duplica la administración de identidad y crea un maestro a promover.


### 2. Alternativas Evaluadas


> **Tabla 115** — 2. Alternativas Evaluadas · 5 filas · ver planilla del subdocumento


### 3. Criterio de Selección y Justificación Técnica-Económica

Autonomía (RT-03.10/RNF-13.01): la caché local (A-05: VM-05 Talca, VM-C03 Concepción) valida localmente la firma OIDC y mantiene sesiones hasta 24 h CD / 14 h terreno; el token offline se renueva al inicio del turno en cobertura, de modo que la ventana offline siempre cubre la jornada (8 h bodega / 14 h reparto-preventa) sin autenticación en ruta.

Autoridad única (D6): todas las escrituras viven en el IdP maestro de la nube; los cambios de alta/baja/roles se propagan por export/import del Realm cifrado vía S3 (outbound) con Δ ≤ 8 h (TTL) y baja efectiva SCIM ≤ 24 h (RT-12.10). No existe maestro local a promover ⇒ DR de identidad = misma autoridad en nube (no depende de switchover).

Externos (RT-12.11/12.12): OTP de un solo uso para conductores (RF-06.08, ≤ 2 min, sin correo) y credencial inicial en sesión de dotación; MFA para todo acceso externo y privilegiado (Art. 22).

Equipo de 4 TI: Keycloak administrado (Fargate) + federación OIDC con Amazon API Gateway (ADR-13); sin sincronización de directorio propietario.


### 4. Decisión Adoptada

Modelo B de identidad (D6): Keycloak IdP maestro en AWS (ECS Fargate, 2 tareas Multi-AZ, backend Aurora) con caché local de solo lectura TTL 8 h en VM-05/VM-C03 y offline access tokens por perfil (8 h bodega, 14 h reparto/preventa). Sincronización del Realm cifrado por S3 (outbound, Zero Trust); MFA OIDC para externos; OTP para conductores externos. Declarado en la sección de Arquitectura de Seguridad de este documento (§4, ADR-06).


### 5. Consecuencias, Trade-offs y Mitigaciones


> **Tabla 116** — 5. Consecuencias, Trade-offs y Mitigaciones · 5 filas · ver planilla del subdocumento


### ADR-07 — Estrategia de Movilidad de Terreno: Aplicación Nativa Android (Kotlin)

Estado: Aprobado

Fecha: 2026-09-05

Decisión relacionada: Decisión de proyecto N° 19 (nativa vs. híbrida vs. PWA).

Trazabilidad normativa: BTT RT-12.11 (autenticación en perfil operacional) · RT-13.08 (interfaz de terreno: guantes térmicos, −22 °C, lluvia, 34 °C, una mano, turno sin conexión) · RT-03.19 (edge) · RNF-05.02 (guantes −22 °C) · RNF-05.03 (curva de aprendizaje ≤ 2 h) · RNF-06.01 (14 h sin señal) · RF-03.02 (stock offline) · RF-06.11/06.12/06.13 (QR/foto/impresora térmica) · Caso 02 Cap. 6 (cámara sin cobertura, turnos de 30 min).


### 1. Contexto y Problema

El terreno es el corazón de la operación: 62 preventistas, ~200 conductores y 120 terminales de bodega operando con guantes térmicos a −22 °C, a una mano durante la descarga, bajo lluvia, sol directo y 14 h sin señal. Requiere escáner GS1, impresora térmica Bluetooth y POS móvil (PAX), y curva de aprendizaje ≤ 2 h. Una PWA no controla el SDK de escáner Zebra de forma confiable ni persiste un turno completo sin capa nativa; una híbrida (Flutter) agrega un runtime intermedio que degrada la interacción con periféricos industriales.


### 2. Alternativas Evaluadas


> **Tabla 117** — 2. Alternativas Evaluadas · 4 filas · ver planilla del subdocumento


### 3. Criterio de Selección y Justificación Técnica-Económica

Periféricos (RT-13.08/RF-06.13): DataWedge (intents) entrega disparo de escáner GS1, CW (camera wedge) para QR (RF-06.11) y salidas a impresora BW Zebra — integraciones nativas estables que un runtime híbrido/PWA no garantiza.

Offline total (RNF-06.01/RT-03.19): SQLite/Room persiste el turno completo (pedidos, POD con foto/firma, cobros, devoluciones) y sincroniza con deduplicación e idempotencia al reconectar (< 10 min, RNF-07.01); STock indicativo con antigüedad visible (RF-02.05) y resolución cronológica de conflictos (RF-02.05e).

Condiciones extremas (RNF-05.02/RT-12.11): la UI nativa permite contraste alto, botones grandes, entrada por guantes (toque grueso), sin gestos complejos; dispositivos Rugged Zebra (EC55, TC58e, MC9400 Cold Storage) con Android 13+ y baterías de cámara/5G.

TCO: una misma app nativa cubre preventa, reparto y bodega (parque de terreno de la sección de Emplazamiento de este documento); el costo de mantención de la plataforma nativa se asume como trade-off frente a las exigencias RNF (documentado en este ADR-07).


### 4. Decisión Adoptada

Aplicación nativa Android (Kotlin) para preventa, reparto/cobranza y picking/recepción de bodega, con persistencia local SQLite/Room, SDK Zebra DataWedge (escáner GS1 + CW QR) y módulo de impresión Bluetooth (ZQ620) y POS (PAX). PWA (web) solo para la autoatención del canal moderno (portal, ADR-11). Dispositivos Rugged: EC55 (preventa), TC58e (reparto), MC9400 Cold Storage (cámara −22 °C), DS2208 (andén), penalizados por guantes/una mano (RNF-05.02).


### 5. Consecuencias, Trade-offs y Mitigaciones


> **Tabla 118** — 5. Consecuencias, Trade-offs y Mitigaciones · 5 filas · ver planilla del subdocumento


### ADR-08 — Destino del WMS Legado de 2013

Estado: Aprobado

Fecha: 2026-09-05

Decisión relacionada: Decisión 16.1 N° 14 (reemplazar el WMS de 2013).

Trazabilidad normativa: RT-05.11–RT-05.15 (plan de migración por dominio, volúmenes y reversión) · RT-03.10/RNF-02.01 (24 h) · RNF-05.01 (≤1 s) · Caso 02 Cap. 16.1 N° 14 (el CLIENTE delega expresamente la decisión) y Cap. 9 (dolores: conteo 2,3 %, merma 1,7 %, rasgos de WMS 2013) · estrategia azul-verde y reversión.


### 1. Contexto y Problema

El WMS de 2013 corre en Talca con proveedor desaparecido (sin soporte, sin roadmap), planillas impresas (conteo cíclico con 2,3 % de diferencia y ajustes sin investigación de causa), y no soporta multi-sitio ni operación de 24 h sin enlace. El CLIENTE delega expresamente en el proponente la decisión (Cap. 16.1 N° 14). Extenderlo arrastra el riesgo de fecha conocida: sin soporte, un incidente en la ventana crítica (05:30–07:00) no tendría plan B.


### 2. Alternativas Evaluadas


> **Tabla 119** — 2. Alternativas Evaluadas · 4 filas · ver planilla del subdocumento


### 3. Criterio de Selección y Justificación Técnica-Económica

Requisitos (RF-02.x): slotting ABC, conteo cíclico ciego, picking FEFO dirigido, SSCC GS1, trazabilidad por lote — el WMS 2013 no los contempla ni los puede incorporar sin proveedor.

Riesgo operacional: un sistema sin soporte expuesto a la ventana de indisponibilidad cero (RT-10.05) es un riesgo con fecha de impacto indefinido; el análisis de riesgos del caso lo califica como inaceptable frente al CAPEX del reemplazo.

Migración (RT-05.11–15): por dominio y en ventanas sin operación: maestros completos, ventas/pedidos 3 años, inventario 2 años, trazabilidad 5 años, CxC abierta; convivencia con el ERP/GDE (que no se reemplaza) vía capa anticorrupción (ADR-11).

Reversión y despliegue: estrategia azul-verde por ola y sitio, con umbrales de marcha blanca por oleada (RT-20.02/20.04) y plan de reversión para volver al WMS 2013 sin pérdida en caso de no superar los indicadores.

TCO 56 meses: el costo de reemplazo se paga en la Etapa 1 y se amortiza con la reducción de 2,3 %→~0,3 % de diferencia de conteo y 1,7 %→<1 % de merma (objetivos de RF/planilla del Cap. 18) y con OTIF 82,4 %→95 %.


### 4. Decisión Adoptada

Reemplazo total del WMS 2013 en la Etapa 1 por el módulo WMS del monolito modular (ADR-01) desplegado en Talca (maestro), Concepción (edge) y cross-docks (mini-WMS E-01), con migración por dominio (RT-05.11–15), oleadas por sitio y plan de reversión azul-verde documentado. El ERP administrativo/GDE no se reemplaza y se integra por la capa anticorrupción (ADR-11).


### 5. Consecuencias, Trade-offs y Mitigaciones


> **Tabla 120** — 5. Consecuencias, Trade-offs y Mitigaciones · 5 filas · ver planilla del subdocumento


### ADR-09 — Estrategia de Recuperación ante Desastres (DR): Warm Standby Activo-Pasivo Multi-Región

Estado: Aprobado

Fecha: 2026-09-05

Decisión relacionada: Decisión 16.1 N° 27 (modalidad activo-pasivo, RTO/RPO, cadencia de pruebas).

Trazabilidad normativa: RT-07.01 (declarar y justificar modalidad activo-activo vs. activo-pasivo) · RT-07.07 (pruebas reales ≥ 2 veces/año con informe y medición de RTO/RPO) · RNF-20.06 (RTO ≤ 4 h, RPO ≤ 15 min) · RNF-20.07 (3-2-1-1-0) · BA Art. 20 (continuidad y pruebas semestrales) · DRP local Talca→Concepción (RTO +1–2 h) · Caso 02 Cap. 16.1 N° 27.


### 1. Contexto y Problema

La ventana de despacho (05:30–07:00) no admite plan manual; una falla mayor del sitio primario debe recuperar el servicio con RTO ≤ 4 h y RPO ≤ 15 min (RNF-20.06) y probarse con conmutación real al menos 2 veces al año (RT-07.07/Art. 20). El sitio primario es Talca (WMS maestro on-premise); el respaldo secundario se apoya en la nube (replicación AWS) y en el borde autónomo de Concepción como DRP local.


### 2. Alternativas Evaluadas


> **Tabla 121** — 2. Alternativas Evaluadas · 5 filas · ver planilla del subdocumento


### 3. Criterio de Selección y Justificación Técnica-Económica

RTO/RPO (RNF-20.06): la réplica continua (DMS CDC) y la réplica de Aurora (WAL) mantienen RPO ≤ 15 min; el promote a la región DRP (us-east-1) más el DRP local Talca→Concepción (procedimiento documentado de 5 pasos, RTO +1–2 h) cumplen los cuatros horas.

RT-07.01: activo-activo duplicaría la infraestructura transaccional y exigiría reconciliación de doble escritura (~105 TPS peak) sin beneficio medible frente al RTO comprometido; la modalidad activo-pasiva es proporcional al volumen (CAP consistente, ADR-04).

Pruebas (RT-07.07/Art. 20): conmutación real semestral con informe de RTO/RPO efectivos y plan de corrección de brechas; consistente con la retención sanitaria y la operación continua.

Identidad (ADR-06): el DR de identidad no exige conmutación local (el maestro está en la nube y las cachés A-05 siguen validando firmas): se elimina una clase entera de riesgos de DR.

Respaldo 3-2-1-1-0 (RNF-20.07): copia primaria on-premise + réplica local (Concepción) + pierna cloud (S3 Object Lock/Backup Vault, inmutable) + offsite + prueba mensual de restauración y retención legal (ADR-04).

Falla de AZ vs. caída de región (alternativa D): si el CLIENTE no aprueba la transferencia a us-east-1 (Art. 23, sección de Arquitectura de Seguridad de este documento, §10), la postura mínima es la continuidad intrarregional en sa-east-1: uso de la tercera AZ (sa-east-1a/1b/1c) y respaldo inmutable regional, que mantiene RTO ≤ 4 h / RPO ≤ 15 min ante falla de una zona de disponibilidad o corrupción de datos — lo que el multi-AZ ya brinda —, pero no ante una caída de toda la región sa-east-1, escenario en que la reconstrucción desde el respaldo inmutable toma 24–72 h e incumple RNF-20.06. Esta alternativa no usa los sitios on-premise del CLIENTE para la carga cloud (Talca/Concepción alojan solo el dominio on-premise, con su DRP local RTO +1–2 h); y es precisamente esta degradación la que motiva solicitar la aprobación de us-east-1 con resguardos, conforme al Art. 23.


### 4. Decisión Adoptada

DR activo-pasivo warm standby multi-región: replicación continua del WMS (VM-02) hacia Aurora (ACM us-east-1 global replica) con DMS CDC, RPO ≤ 15 min y RTO ≤ 4 h; DRP local Talca→Concepción (VM-C01/VM-C02) con RTO +1–2 h para la bodega; pruebas reales 2×/año (RT-07.07) y respaldo 3-2-1-1-0 admitido por S3 Object Lock. Documentado en la sección de Arquitectura de Despliegue de este documento (§4, ADR-09). Si el CLIENTE no aprueba la transferencia internacional (Art. 23), rige la alternativa D (§2): continuidad intrarregional en sa-east-1 con tercera AZ y respaldo inmutable, aceptando el RTO de 24–72 h ante caída de toda la región, que es el impacto evaluado en §3.


### 5. Consecuencias, Trade-offs y Mitigaciones


> **Tabla 122** — 5. Consecuencias, Trade-offs y Mitigaciones · 5 filas · ver planilla del subdocumento


### ADR-10 — Almacenamiento On-Premise y Niveles RAID

Estado: Aprobado

Fecha: 2026-09-05

Decisión relacionada: Decisión 16.1 N° 28 (declarar y justificar nivel RAID frente a alternativas).

Trazabilidad normativa: BTT RT-03.14 (tolerancia a falla de disco y nivel RAID declarado) · RNF-13.03 (equipos críticos redundantes) · RNF-13.04 (tolerancia a falla de al menos 1 disco) · RNF-13.05 (justificación del nivel RAID) · Caso 02 Cap. 16.1 N° 28 y Cap. 10 (ventana crítica sin falla).


### 1. Contexto y Problema

La BD transaccional del WMS (VM-02) concentra ~105 TPS de diseño con escritura fuerte de sincronización y trazabilidad; la evidencia fotográfica del POD, los logs y el contenido de cámara suman datos de escritura secuencial menos críticos. Una falla de disco en la ventana de despacho (05:30–07:00) no puede detener la operación. El nivel RAID debe tolerar el fallo de al menos un disco (RNF-13.04) y justificarse (RNF-13.05/RT-03.14).


### 2. Alternativas Evaluadas


> **Tabla 123** — 2. Alternativas Evaluadas · 5 filas · ver planilla del subdocumento


### 3. Criterio de Selección y Justificación Técnica-Económica

Transaccional (RNF-13.04, RT-03.14): RAID 10 sobre NVMe Superdome/Kioxia (sección de Dimensionamiento de este documento, §4.3) entrega >100.000 IOPS frente a ~840 IOPS necesarias (105 TPS × 8 E/S), con latencia de escritura determinista y reparación acotada — crítico en la ventana de despacho.

Evidencia/logs: RAID 6 (doble paridad + hot-spare) para fotografías POD, logs y rollups; tolera el segundo fallo durante el rebuild, relevante en discos de alta capacidad y baja rotación de escritura.

Rechazo de RAID 5: en discos modernos de 8–16 TB, la probabilidad de URE (uncorrectable read error) durante un rebuild extenso no es despreciable; el caso exige tolerancia a fallo de al menos un disco en operación competitiva (RNF-13.04/05) y RAID 5 solo cubre uno.

Coherencia con Ceph (hipervisor): el pool Ceph N+1 de los nodos de cómputo complementa los niveles RAID de las VMs (redundancia de infraestructura, RNF-13.03); la pieza cross-dock usa contenedores con disco local del mini-PC recubierto por el respaldo nocturno (RNF-20.07).

TCO: el sobre-costo del 50 % de RAID 10 solo se aplica a la BD crítica; el grueso del almacenamiento (evidencia, logs, telemetría) usa RAID 6 con solo 2 de 8 discos de paridad, manteniendo el costo de almacenamiento total contenidamente respecto de RAID 1/0 puro.


### 4. Decisión Adoptada

RAID 10 para los servicios transaccionales del WMS (VM-02/VM-C02 y núcleo del maestro) con NVMe, y RAID 6 con hot-spare para evidencia fotográfica/POD, logs y rollups de cámara; RAID 5 descartado y justificado frente a alternativas (RNF-13.05/RT-03.14), con redundancia de equipos críticos por hipervisor Ceph N+1 (RNF-13.03). Registrado en la sección de Dimensionamiento de este documento (§4.3) y en el emplazamiento (ADR-10).


### 5. Consecuencias, Trade-offs y Mitigaciones


> **Tabla 124** — 5. Consecuencias, Trade-offs y Mitigaciones · 5 filas · ver planilla del subdocumento


### ADR-11 — Integración B2B/EDI con Supermercados: Hub GS1 Centralizado con Capa Anticorrupción

Estado: Aprobado

Fecha: 2026-09-05

Decisiones relacionadas: RF-12 (mensajería electrónica EDI); RF-01.10 (maestro interno de productos, tabla de equivalencias por cadena); A-04 (Capa Anticorrupción del ERP).

Trazabilidad normativa: BTT RT-05.23 (estándares sectoriales de intercambio — EDI) · RT-16.16 (documentos cifrados con integridad y retención) · RT-16.17 (firma electrónica Ley N° 19.799) · RNF-12.01 (canal moderno en producción antes de enero 2029) · RF-12.03 (equivalencias GTIN por cadena) · RF-12.06 (bandeja de excepciones) · RF-01.10 — estándares GS1 (EANCOM/GS1 XML, EPCIS) invocados por el Caso 02 Cap. 16.2 · Caso 02 Cap. 9 (cadenas del canal moderno).


### 1. Contexto y Problema

Los supermercados del canal moderno (p.ej. Walmart, Cencosud, SMU) exigen intercambio electrónico EDI dentro de sus ventanas de taking (pedidos, envío de guías/facturas, acuse de recibo). Hoy el caso lo resuelve por correo/telefono y con diferencias de maestro por cadena (decisión 16.1 N° 11). Conectores punto-a-punto por cadena multiplican los adaptadores, duplican la lógica de mapeo y disparan el mantenimiento ante cada cambio de especificación de la cadena; además, el ERP (que no se reemplaza) expone una frontera frágil.


### 2. Alternativas Evaluadas


> **Tabla 125** — 2. Alternativas Evaluadas · 4 filas · ver planilla del subdocumento


### 3. Criterio de Selección y Justificación Técnica-Económica

Estandarización (Cap. 16.2): el caso exige estándares GS1; el hub declara un modelo canónico (EANCOM D.01B/GS1 XML para pedidos/despachos/facturas, EPCIS para eventos de trazabilidad) y mapea cada cadena contra el modelo, no contra el ERP.

Esfuerzo marginal: una cadena nueva se agrega por configuración de perfil (equivalencias GTIN, RF-12.03) y pruebas de conexión, no por código; el hub centraliza la validación, el retry y la auditoría.

Aislamiento del ERP (ACL A-04): el ERP (que no se reemplaza, ADR-08) queda detrás de la capa anticorrupción: celery-erp-sync lee contratos OpenAPI del ERP y publica notificaciones por SQS; nunca hay escritura directa desde una cadena al ERP (Zero Trust, BA Art. 21).

Plazo contractual: el canal moderno (incluido EDI) entra en producción antes del hito enero 2029 (RNF-12.01), por lo que la Etapa 2 concentra portal y EDI detrás de la misma puerta de enlace (Amazon API Gateway, ADR-13) y del hub.

Equipo de 4 TI: el hub EDI se aloja como módulo del monolito (ADR-01) en la DMZ de AWS (N-01…N-03) con servicios administrados (API Gateway, SQS, EventBridge), sin adaptadores propietarios por cadena.


### 4. Decisión Adoptada

Hub EDI centralizado basado en GS1 (EANCOM/GS1 XML para textos, EPCIS para trazabilidad) en la nube (DMZ, modulo integraciones del monolito), con conector configurable por cadena, tabla de equivalencias GTIN/cadena (RF-12.03), bandeja de excepciones (RF-12.06) y Capa Anticorrupción (ACL, A-04) hacia el ERP/GDE. Canal moderno operativo ≤ enero 2029 (RNF-12.01). La evidencia POD se articula con la GDE y el acuse de recibo electrónico (RF-12.12/12.13, RT-16.17/16.18).


### 5. Consecuencias, Trade-offs y Mitigaciones


> **Tabla 126** — 5. Consecuencias, Trade-offs y Mitigaciones · 5 filas · ver planilla del subdocumento


### ADR-12 — Absorción del Peak de Septiembre y Perfil de Carga No Plano

Estado: Aprobado

Fecha: 2026-09-05

Decisión relacionada: Decisión 16.1 N° 30 (cuello de botella del peak de septiembre y estrategia).

Trazabilidad normativa: BTT RT-09.05 (identificar el cuello de botella y cómo se detecta/resuelve) · RT-03.06 (FinOps) · RT-03.08 (instancias reservadas/ahorro) · RT-03.09 (cómputo serverless para carga variable) · RNF-19.01–04 (capacidad, escalado horizontal automático, cuello de botella, pruebas 1,5×) · Caso 02 Cap. 14.2/15 (perfil no plano; congelamiento 1–25 sept) · RT-10.05 (congelamiento de cambios en septiembre/diciembre).


### 1. Contexto y Problema

El perfil de carga no es plano: preventa 09:00–18:00, preparación 22:00–06:00, despacho 05:30–07:00 (96 camiones), sincronización de flota 17:00–20:00, y septiembre casi duplica el volumen durante 3 semanas (1.400 → 2.600 entregas/día). Sobredimensionar para el promedio diario es un error declarado por el propio caso; sobredimensionar estático para el peak paga 12 meses la capacidad de 3 semanas.


### 2. Alternativas Evaluadas


> **Tabla 127** — 2. Alternativas Evaluadas · 4 filas · ver planilla del subdocumento


### 3. Criterio de Selección y Justificación Técnica-Económica

Perfil no plano (Cap. 14.2/15): la capacidad se calcula al peak ×1,5 (RNF-19.04) = 3.900 entregas/día, con ~105 TPS de diseño de despacho y pruebas de carga de 1,5×peak ≈ 160 TPS / 5.850 entregas (RNF-19.04). Fargate 2→6 tareas (Django), Celery 2→4 y Lambda 100→500 cubren la ratio de las 3 semanas sin pago residual.

Cuello de botella identificado (RT-09.05): confirmación/persistencia transaccional de pedidos e ingesta de telemetría de la flota. Se declara el punto de saturación y se vigila con métricas de negocio (OTIF, pedidos no preparados) y de infraestructura (cola SQS, CPU, TPS) — RNF-19.03.

FinOps (RT-03.06) y RT-03.08/03.09: la base reservada (RI/Savings Plan) cubre la capacidad de régimen; el crecimiento del peak se paga con cómputo efímero (Fargate/Lambda). Ampliar Aurora a xlarge + 2 readers y DynamoDB con autoscaling absorbe el pico sin compra fija.

Congelamiento (RT-10.05): del 1 al 25 de septiembre y en diciembre no se despliegan cambios; la escala predictiva se programa por calendario (calendario de eventos) y se valida en la marcha blanca de septiembre del año 1.

Equipo de 4 TI: la operación es declarativa (IaC, RT-03.03): el mismo despliegue escala y decrece sin intervención manual; las políticas de alerta de desviación de presupuesto (RT-03.06) sustituyen el control manual del costo.


### 4. Decisión Adoptada

Cómputo elástico con auto-escalado horizontal (Fargate Django 2→6, Celery 2→4, Lambda 100→500, Aurora db.r6g.large→xlarge +2 readers, DynamoDB on-demand) con escala predictiva por calendario (septiembre/diciembre) y reactiva (CPU, profundidad de cola, TPS); base de capacidad con Savings Plan/instancias reservadas de la carga de régimen (RT-03.08) y la diferencia del peak como cómputo efímero (RT-03.09). Monitoreo del cuello de botella declarado (RT-09.05/RNF-19.03) y pruebas 1,5×peak (RNF-19.04).


### 5. Consecuencias, Trade-offs y Mitigaciones


> **Tabla 128** — 5. Consecuencias, Trade-offs y Mitigaciones · 5 filas · ver planilla del subdocumento


### ADR-13 — Puerta de Enlace de Servicios: Amazon API Gateway

Estado: Aprobado

Fecha: 2026-09-05 (formalizado como ADR el 2026-09-06)

Decisión relacionada: D8 (Arquitectura Lógica v6.2, Capa 3).

Trazabilidad normativa: BA Art. 21.2 (puerta de enlace con autenticación, autorización, cuotas, límites de tasa, validación de esquema e inspección de carga útil) · RT-02.01 (capa 3 del modelo de referencia) · RT-11.11 · RT-05.16/05.18 (contratos y OAuth 2.1/mTLS) · RT-02.02 (contratos versionados retro-compatibles) · Art. 16.3 (preferencia por servicios administrados).


### 1. Contexto y Problema

La Capa 3 es el punto por donde entra todo: las APIs de negocio, la sincronización diferida de preventa y reparto —que es tráfico de primera clase, no un anexo— y los tres portales de la DMZ. El Art. 21.2 no pide «un gateway»: pide autenticación, autorización, cuotas, límites de tasa, validación de esquema e inspección de carga útil, todo en el borde. Y el CLIENTE opera con 4 personas de TI: cualquier componente que haya que parchar, dimensionar y sostener 24×7 compite con la operación.


### 2. Alternativas Evaluadas


> **Tabla 129** — 2. Alternativas Evaluadas · 4 filas · ver planilla del subdocumento


### 3. Criterio de Selección y Justificación Técnica-Económica

Cumplimiento literal del Art. 21.2 sin desarrollo propio: autenticación OIDC, autorización por rol, cuotas y límites de tasa por cliente, validación de esquema e inspección de carga útil son capacidades nativas.

Equipo de 4 personas (Cap. 2.4 del caso): la alternativa B agrega un componente crítico en la ruta de la venta que hay que dimensionar, parchar y recuperar. En la ventana de despacho 05:30–07:00, con indisponibilidad cero comprometida, ese es exactamente el riesgo que no conviene asumir.

Coherencia con la vista física: las secciones de Despliegue, Emplazamiento e Integración de este documento ya declaran Amazon API Gateway; mantener Kong en el registro de decisiones habría dejado una contradicción entre la arquitectura lógica, la física y el costo, que el Art. 16.4 in fine califica de incoherencia grave.

Reversibilidad (Art. 16.3): los contratos son OpenAPI 3.1 y AsyncAPI 2.6, estándares abiertos; la lógica de negocio vive en Django, no en el gateway. Migrar a Kong u otro gateway no exige reescribir servicios, solo reconfigurar rutas y autorizadores. La dependencia es de configuración, no de código, y así queda declarada en la matriz de reversibilidad.


### 4. Decisión Adoptada

Amazon API Gateway como Capa 3 única, con autorizador OIDC contra el Keycloak maestro, validación de esquema OpenAPI, cuotas y límites de tasa por actor y por ruta, versionado /v{major} y asignación de transaction_id propagado a la Capa 8. Kong Gateway queda declarado como alternativa open source evaluada y no adoptada.


### 5. Consecuencias, Trade-offs y Mitigaciones


> **Tabla 130** — 5. Consecuencias, Trade-offs y Mitigaciones · 4 filas · ver planilla del subdocumento


### ADR-14 — Plataforma de Observabilidad Única: OTel + AMP + CloudWatch + X-Ray

Estado: Aprobado

Fecha: 2026-09-06

Decisión relacionada: D14 (Arquitectura Lógica v6.2, Capa 8); reemplaza la parte de plataforma de D9.

Trazabilidad normativa: BA Art. 16.4 («monitoreo del componente on-premise integrado a la misma plataforma de observabilidad que la nube, sin puntos ciegos») · RT-03.16 (idéntica exigencia) · RT-14.01 a RT-14.09 · RT-09.01 (medición p95) · Art. 16.3 (servicios administrados).


### 1. Contexto y Problema

La observabilidad tiene que cubrir dos dominios muy distintos —una nube elástica y cinco sitios que pueden quedar 24 h sin enlace— y hacerlo sin puntos ciegos. La versión anterior de la arquitectura lógica declaraba un conjunto Prometheus + Grafana + Loki autoadministrado en cada centro de distribución, además de la plataforma en nube. Al contrastarlo con la vista física aparecieron dos problemas: ese conjunto no tenía máquina virtual dimensionada —VM-06 es de 2 vCPU, 4 GB y 50 GB, insuficiente para sostener Prometheus, Loki y Grafana con 13 meses de métricas— y, más de fondo, constituye una segunda plataforma de observabilidad, que es justamente lo que el Art. 16.4 y RT-03.16 prohíben al exigir «la misma».


### 2. Alternativas Evaluadas


> **Tabla 131** — 2. Alternativas Evaluadas · 4 filas · ver planilla del subdocumento


### 3. Criterio de Selección y Justificación Técnica-Económica

La norma pide una plataforma, no dos. Es el criterio decisivo: el Art. 16.4 y RT-03.16 usan la palabra «misma».

«Sin puntos ciegos» se resuelve con el buffer, no con una segunda plataforma. El colector ADOT retiene 24 h en disco —exactamente la autonomía comprometida del centro de distribución— de modo que un corte no produce un hueco en la serie: produce un retraso que se cierra al reconectar.

Ninguna decisión crítica depende de un tablero. El bloqueo de despacho por excursión térmica es local (decisión 16.1 N° 4), la alarma de cámara es acústica y luminosa, y los sensores de sala reportan al DCIM/BMS (RT-06.14). Lo que se pierde durante el corte es visibilidad agregada, no capacidad de operar.

Sin lock-in real: AMP es compatible con Prometheus y PromQL, de modo que las reglas de alerta y las consultas son portables; la instrumentación es OpenTelemetry, estándar neutral; y Grafana es OSS. Se conserva el ecosistema Prometheus/Grafana sin operar sus servidores.

Equipo de 4 personas: no se le entrega al CLIENTE una plataforma de observabilidad que mantener además del negocio.


### 4. Decisión Adoptada

Instrumentación OpenTelemetry en todos los componentes; colectores ADOT on-premise (F-01: VM-06 Talca, VM-C04 Concepción, contenedor en cross-docking) con buffer en disco de 24 h; plataforma única en nube: métricas en AMP (13 meses), registros en CloudWatch Logs (12 meses en línea + 24 en archivo), trazas en X-Ray (30 días), tableros en Grafana OSS autoadministrado en sa-east-1 y alertas por AMP/Alertmanager y CloudWatch hacia SNS y PagerDuty. Se declara expresamente qué no está disponible durante un corte (RT-03.13), y se declara que ninguna decisión de la ventana 05:30–07:00 depende de ello.


### 5. Consecuencias, Trade-offs y Mitigaciones


> **Tabla 132** — 5. Consecuencias, Trade-offs y Mitigaciones · 4 filas · ver planilla del subdocumento


### ADR-15 — Gestión de Secretos: Servicio Administrado en lugar de Gestor Autoalojado

Estado: Aprobado

Fecha: 2026-09-06

Decisión relacionada: D13 (Arquitectura Lógica v6.2, Capa 7); resolución SEC-01 de la sección de Arquitectura de Seguridad de este documento (§5.3).

Trazabilidad normativa: BA Art. 21.4 («prohibición absoluta de credenciales, claves o secretos embebidos… uso obligatorio de un gestor de secretos con rotación automática») · Art. 21.2 (gestión de claves con separación de funciones) · Art. 16.2 (justificación de emplazamiento componente por componente) · Art. 16.3 (servicios administrados) · Art. 21 (Zero Trust) · RT-04.09 · RT-11.09.


### 1. Contexto y Problema

La solución necesita custodiar secretos de peso: credenciales del ERP de 2017, certificados AS2 y EDI de cada cadena de supermercados, credenciales del SII y de Transbank, y las credenciales de servicio entre módulos. El Art. 21.4 exige un gestor con rotación automática. La arquitectura lógica declaraba HashiCorp Vault on-premise, pero al contrastarla con la vista física de este documento apareció el problema real: Vault no existía en ninguna vista física —no tenía máquina virtual en el dimensionamiento on-premise (§4), no figuraba en el inventario ni en el emplazamiento de este documento—. Un componente de seguridad sin emplazamiento justificado incumple el Art. 16.2 y, al no estar costeado, cae en la incoherencia grave del Art. 16.4 in fine.


### 2. Alternativas Evaluadas


> **Tabla 133** — 2. Alternativas Evaluadas · 4 filas · ver planilla del subdocumento


### 3. Criterio de Selección y Justificación Técnica-Económica

El componente debe existir en la vista física. Es la razón inmediata: lo declarado no estaba emplazado ni costeado. Cualquiera de las dos salidas corregía el defecto, pero solo una lo hacía sin agregar infraestructura.

Equipo de 4 personas (Cap. 2.4): el modo sellado de Vault tras un reinicio exige intervención humana con custodios. En una operación cuya ventana crítica es de 05:30 a 07:00 y cuyo turno de preparación es nocturno, introducir un componente que puede requerir desellado manual de madrugada es un riesgo operacional que no compra nada.

Zero Trust intacto: los nodos on-premise consumen secretos por VPC Endpoint saliente, coherente con la regla de que no se abren puertos entrantes salvo las dos excepciones D-AL-05.

La contingencia no depende de la nube. El secreto de la cuenta de emergencia queda deliberadamente fuera de línea, en sobre sellado con doble firma en el recinto de custodia de la sala (RT-06.26/06.27): es la única credencial que debe seguir siendo utilizable cuando no hay ni IdP ni enlace, y por eso no vive en ningún sistema.

Separación de funciones (Art. 21.2): quien administra la plataforma no administra las claves maestras; la política se expresa en IAM y queda auditada en CloudTrail.


### 4. Decisión Adoptada

AWS Secrets Manager para secretos con rotación (credenciales del ERP, SII, Transbank y certificados AS2/EDI) y SSM Parameter Store para parámetros de configuración no sensibles, con consumo saliente desde los nodos on-premise por VPC Endpoint, rotación automática, y cifrado con CMK de KMS bajo separación de funciones. HashiCorp Vault queda declarado como alternativa evaluada y no adoptada. La cuenta de emergencia se custodia fuera de línea.


### 5. Consecuencias, Trade-offs y Mitigaciones


> **Tabla 134** — 5. Consecuencias, Trade-offs y Mitigaciones · 4 filas · ver planilla del subdocumento


### Matriz de trazabilidad (ADR → normativa → decisión → documento)


> **Tabla 135** — Matriz de trazabilidad (ADR → normativa → decisión → documento) · 16 filas · ver planilla del subdocumento

LAFROX

Propuesta de Solución — Distribuidora Puelche S.A.

Licitación N° TFEP-01/2026 — Caso 02 Logística

SUBDOCUMENTO 5

Modelo y Gestión de Datos

Informe 1
