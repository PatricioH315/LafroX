# LafroX — Anexos del Subdocumento 4

[Cuerpo](LAFROX-Subdocumento4.md) · [Anexos](LAFROX-Subdocumento4-Anexos.md) · [T-11](LAFROX-Formulario-T-11.md)

## Índice

- [Anexos del Subdocumento 4](#anexos-del-subdocumento-4)
- [Catálogo de anexos y trazabilidad](#catálogo-de-anexos-y-trazabilidad)
- [Anexo 4-A — Catálogo de eventos canónicos](#anexo-4-a-catálogo-de-eventos-canónicos)
- [Anexo 4-B — Gobierno de la integración](#anexo-4-b-gobierno-de-la-integración)
- [Anexo 4-C — Escenarios de carga masiva](#anexo-4-c-escenarios-de-carga-masiva)
- [Anexo 4-D — Matriz de los doce módulos](#anexo-4-d-matriz-de-los-doce-módulos)
- [Anexo 4-E — Trazabilidad funcional](#anexo-4-e-trazabilidad-funcional)
- [Anexo 4-F — Mapa de límites de contexto](#anexo-4-f-mapa-de-límites-de-contexto)
- [Anexo 4-G — Catálogo de interfaces internas](#anexo-4-g-catálogo-de-interfaces-internas)
- [Anexo 4-H — Catálogo de interfaces externas](#anexo-4-h-catálogo-de-interfaces-externas)
- [Anexo 4-I — Volumen de mensajes](#anexo-4-i-volumen-de-mensajes)
- [Anexo 4-J — Funciones sin conexión](#anexo-4-j-funciones-sin-conexión)
- [Anexo 4-K — Reglas de reconciliación](#anexo-4-k-reglas-de-reconciliación)
- [Anexo 4-L — Decisiones del numeral 16.1](#anexo-4-l-decisiones-del-numeral-161)
- [Anexo 4-M — Verificación de continuidad lógica](#anexo-4-m-verificación-de-continuidad-lógica)
- [Anexo 4-N — Correspondencia de componentes lógicos](#anexo-4-n-correspondencia-de-componentes-lógicos)
- [Anexo 4-O — Registro de decisiones de arquitectura](#anexo-4-o-registro-de-decisiones-de-arquitectura)
- [Anexo 4-P — Tecnologías, soporte y actualización](#anexo-4-p-tecnologías-soporte-y-actualización)
- [Anexo 4-Q — Modelado de amenazas lógicas](#anexo-4-q-modelado-de-amenazas-lógicas)
- [Anexo 4-R — Controles de seguridad y evidencia](#anexo-4-r-controles-de-seguridad-y-evidencia)
- [Anexo 4-S — Puntos de vista y correspondencias](#anexo-4-s-puntos-de-vista-y-correspondencias)
- [Anexo 4-T — Desempeño y aceptación lógica](#anexo-4-t-desempeño-y-aceptación-lógica)
- [Anexo 4-U — Prueba de entrega, guía y acuses](#anexo-4-u-prueba-de-entrega-guía-y-acuses)
- [Anexo 4-V — Protocolos de aceptación](#anexo-4-v-protocolos-de-aceptación)
- [Anexo 4-W — Memoria de cálculo del dimensionamiento](#anexo-4-w-memoria-de-cálculo-del-dimensionamiento)
- [4-W.1 Entradas, requisitos, parámetros y supuestos](#4-w1-entradas-requisitos-parámetros-y-supuestos)
- [4-W.2 Dimensiones 1–3: transacciones por segundo](#4-w2-dimensiones-13-transacciones-por-segundo)
- [4-W.3 Dimensiones 4–6: personas, concurrencia y dispositivos](#4-w3-dimensiones-46-personas-concurrencia-y-dispositivos)
- [4-W.4 Dimensiones 7–10: almacenamiento, retención y migración](#4-w4-dimensiones-710-almacenamiento-retención-y-migración)
- [4-W.5 Dimensiones 11–12: integraciones, mensajes y enlaces](#4-w5-dimensiones-1112-integraciones-mensajes-y-enlaces)
- [4-W.6 Dimensiones 13–14: terreno y sincronización](#4-w6-dimensiones-1314-terreno-y-sincronización)
- [4-W.7 Dimensiones 15–16: mesa de ayuda y operación](#4-w7-dimensiones-1516-mesa-de-ayuda-y-operación)
- [4-W.8 Capacidad on-premise por VM](#4-w8-capacidad-on-premise-por-vm)
- [4-W.9 Capacidad en nube](#4-w9-capacidad-en-nube)
- [4-W.10 Crecimiento, enlaces y ventana dominical](#4-w10-crecimiento-enlaces-y-ventana-dominical)
- [4-W.11 Umbrales de quiebre y cuello de botella](#4-w11-umbrales-de-quiebre-y-cuello-de-botella)
- [4-W.12 Pruebas de carga, estrés y operación](#4-w12-pruebas-de-carga-estrés-y-operación)
- [Referencias](#referencias)
- [Declaración de uso de IA](#declaración-de-uso-de-ia)

A.table

# Anexos del Subdocumento 4

Estos anexos reúnen los catálogos, las matrices, el registro de decisiones de arquitectura y la memoria de cálculo del dimensionamiento citados en los apartados 4.1, 4.2 y 4.3 del Subdocumento 4. El cuerpo del subdocumento conserva la explicación de las decisiones y sus consecuencias operativas; el detalle de cada equipo y servicio se entrega en el Formulario T-11.

## Catálogo de anexos y trazabilidad

Este catálogo reúne los 23 anexos del Subdocumento 4: los anexos 4-A a 4-V de la arquitectura lógica y el Anexo 4-W de la arquitectura física. La primera columna enlaza a su evidencia y identifica el anexo de inicio. El identificador se conserva aunque cambie la paginación. Las referencias desde el cuerpo deben usar la letra del anexo y, cuando corresponda, el identificador de contrato, módulo, decisión o ensayo.

<a id="tab:catalogo-anexos"></a>

**Tabla A.1 — Lista completa de anexos del Subdocumento 4**

| **Anexo / referencia** | **Evidencia** | **Requisito de referencia** |
| --- | --- | --- |
| [4-A / Anexo 4-A](LAFROX-Subdocumento4-Anexos.md#anx:A) | Catálogo de eventos canónicos | RT-02.07 |
| [4-B / Anexo 4-B](LAFROX-Subdocumento4-Anexos.md#anx:B) | Gobierno de la integración | RT-05.21; RT-10.07 |
| [4-C / Anexo 4-C](LAFROX-Subdocumento4-Anexos.md#anx:C) | Escenarios de carga masiva | RT-05.22 |
| [4-D / Anexo 4-D](LAFROX-Subdocumento4-Anexos.md#anx:D) | Matriz de los doce módulos | RT-02.02 |
| [4-E / Anexo 4-E](LAFROX-Subdocumento4-Anexos.md#anx:E) | Trazabilidad funcional | T-12 / capítulo 4 |
| [4-F / Anexo 4-F](LAFROX-Subdocumento4-Anexos.md#anx:F) | Mapa de límites de contexto | RT-02.02 |
| [4-G / Anexo 4-G](LAFROX-Subdocumento4-Anexos.md#anx:G) | Catálogo de interfaces internas | RT-05.21 |
| [4-H / Anexo 4-H](LAFROX-Subdocumento4-Anexos.md#anx:H) | Catálogo de interfaces externas | RT-05.21; RT-10.08 |
| [4-I / Anexo 4-I](LAFROX-Subdocumento4-Anexos.md#anx:I) | Volumen de mensajes | RT-09.01 |
| [4-J / Anexo 4-J](LAFROX-Subdocumento4-Anexos.md#anx:J) | Funciones sin conexión | RT-03.10/13 |
| [4-K / Anexo 4-K](LAFROX-Subdocumento4-Anexos.md#anx:K) | Reglas de reconciliación | RT-02.06; RT-03.12 |
| [4-L / Anexo 4-L](LAFROX-Subdocumento4-Anexos.md#anx:L) | Decisiones del numeral 16.1 | Caso, numeral 16.1 |
| [4-M / Anexo 4-M](LAFROX-Subdocumento4-Anexos.md#anx:M) | Verificación de continuidad lógica | RT-03.10; RT-07.04 |
| [4-N / Anexo 4-N](LAFROX-Subdocumento4-Anexos.md#anx:N) | Correspondencia de componentes lógicos | RT-02.02 |
| [4-O / Anexo 4-O](LAFROX-Subdocumento4-Anexos.md#anx:O) | Registro de decisiones de arquitectura | RT-02.04 |
| [4-P / Anexo 4-P](LAFROX-Subdocumento4-Anexos.md#anx:P) | Tecnologías, soporte y actualización | Bases, 1.6 |
| [4-Q / Anexo 4-Q](LAFROX-Subdocumento4-Anexos.md#anx:Q) | Modelado de amenazas lógicas | RT-11.02 |
| [4-R / Anexo 4-R](LAFROX-Subdocumento4-Anexos.md#anx:R) | Controles de seguridad y evidencia | RT-11.05/06 |
| [4-S / Anexo 4-S](LAFROX-Subdocumento4-Anexos.md#anx:S) | Puntos de vista y correspondencias | RT-02.03 |
| [4-T / Anexo 4-T](LAFROX-Subdocumento4-Anexos.md#anx:T) | Desempeño y aceptación lógica | RT-09.01–08 |
| [4-U / Anexo 4-U](LAFROX-Subdocumento4-Anexos.md#anx:U) | Prueba de entrega, guía y acuses | RT-16.14 |
| [4-V / Anexo 4-V](LAFROX-Subdocumento4-Anexos.md#anx:V) | Protocolos de aceptación | RT-07.04; RT-10.08 |
| [4-W / Anexo Anexo 4-W — Memoria de cálculo del dimensionamiento](LAFROX-Subdocumento4-Anexos.md#anx:42A) | Memoria de cálculo del dimensionamiento | RT-03.20; RT-09.01–09.06 |

Los RT del catálogo proceden de las Bases Técnicas Transversales (caps. 2–16, pp. 6–29), salvo RT-16.14, cuya aplicación a la guía y el acuse está precisada en el caso (Bases Técnicas del caso, cap. 15, p. 27). Para seguir una decisión de stock, consultar M2 en D, INT-01 en G, reconciliación en K y desempeño en T. Para seguir un despacho, consultar M5 en D, INT-07 en H, estados documentales en U y aceptación en V. N y S permiten cotejar esas responsabilidades con las capacidades del capítulo 3 y con su realización física en 4.2; el Anexo 4-W sustenta la capacidad de cada sitio y de la nube.

## Anexo 4-A — Catálogo de eventos canónicos

<a id="anx:A"></a>

La tabla identifica, para cada evento canónico, su productor, sus consumidores, la clave de partición y el hecho del caso o la decisión del numeral 16.1 que lo origina.

<a id="tab:eventos-canonicos"></a>

**Tabla A.2 — Eventos canónicos del dominio**

| **Evento** | **Productor** | **Consumidores** | **Clave de partición** | **Origen en el caso / Decisión** |
| --- | --- | --- | --- | --- |
| RecepcionConfirmada | M1 | M2, M9, ACL→ERP | site_id | Cap. 18, criterio 1: retiro sanitario < 2 h |
| StockReservado / ReservaLiberada | M2 | M3, M5 | sku_id | Decisión 16.1 N° 8: doble compromiso stock |
| PedidoConfirmado | M3 | M4, M5, M10, M11 | pedido_id | M11 consume el evento solo para responder a la cadena en pedidos de ese canal; M3 confirma el pedido |
| MisionPreparada | M5 | M6, ACL→ERP | pedido_id | Cierra ciclo bodega a andén |
| EntregaRegistrada | M6 | M7, M8, M10, ACL | entrega_id | Decisión 16.1 N° 1: entrega cumplida / OTIF |
| DevolucionRegistrada | M8 | M2, M7, M10 | entrega_id | Decisión 16.1 N° 12: efecto sobre DTE emitido |
| EnvaseMovido | M8 | M2, M10 | cliente_id | Decisión 16.1 N° 10: 68.000 canastillos, 9.400 pallets, 14% pérdida |
| ExcursionTermicaDetectada | M9 (borde) | M5 (bloqueo), M10, alertas | shipment_id | Decisión 16.1 N° 4: bloqueo local < 5 s |
| RendicionCerrada | M7 | M10, ACL→ERP | conductor_id | Control efectivo que circula en ruta |
| DesviacionDeRutaDetectada | M12 | M10, M9 | ruta_id | Costo de servir; no control de jornada. |

Fuente: elaboración propia a partir de las Bases Técnicas del caso (cap. 16, pp. 28–29) y de los flujos del apartado 4.1.

## Anexo 4-B — Gobierno de la integración

<a id="anx:B"></a>

La tabla asigna a cada mecanismo de gobierno de la integración su forma de operar, su responsable y el artefacto que deja evidencia.

<a id="tab:gobierno-integracion"></a>

**Tabla A.3 — Mecanismos de gobierno de la capa de integración**

| **Mecanismo** | **Cómo opera** | **Responsable / Artefacto** |
| --- | --- | --- |
| Catálogo único versionado | Toda integración: dueño, contrato, versión, estado, comportamiento ante falla. Lo que no está en el catálogo no se despliega. | Arquitecto Solución / Catálogo (portal API Gateway) |
| Comité Arquitectura | Aprueba altas y cambios `major`; cadencia declarada en plan gobierno. | Arq. Sol., Jefe Proy., Jefe TI Cliente / Actas |
| Pruebas contrato consumidor-proveedor | Pipeline: cambio que rompe consumidor registrado bloquea despliegue automáticamente. | Líder Desarrollo, Líder Calidad / Pipeline CI/CD |
| Pruebas falla por integración | Inyección fallas (RT-10.07) en marcha blanca; verifica comportamiento catálogo. | Líder Calidad, Líder Operación / Evidencia marcha blanca |
| Observabilidad por integración | Latencia, error, volumen, DLQ por integración, correlación `transaction_id` (Capa 8). | Líder Operación/SRE / tableros de CloudWatch |
| Bandeja excepciones negocio | EDI/DTE → bandeja operada por actor canónico (RF-12.05/12.06). | Jefe TI, Responsable Canal Moderno / Bandeja operativa |
| Traspaso equipo 4 personas | Catálogo, guías resolución, bandeja = artefactos operables sin proponente. | Líder Implantación/Gestión Cambio / Documentación traspaso |

Fuente: elaboración propia a partir de las Bases Técnicas Transversales (caps. 2 y 5, pp. 6–13).

## Anexo 4-C — Escenarios de carga masiva

<a id="anx:C"></a>

La tabla distingue los escenarios de carga y descarga masiva por su mecanismo y por el control que deja auditable cada lote.

<a id="tab:carga-masiva"></a>

**Tabla A.4 — Escenarios de carga y descarga masiva (RT-05.22)**

| **Escenario** | **Mecanismo** | **Control y auditoría** |
| --- | --- | --- |
| Carga inicial maestros/históricos (ERP, WMS) | ETL por lotes, inserción idempotente por UUID, ventana sin operación | Conteo previo/posterior por lote, conciliación totales, bitácora carga (quién, cuándo, lote, resultado); rechazados → cuarentena + reproceso |
| Descarga regulatoria (traza lote, temperaturas, DTE, geo) | Exportación asíncrona CSV/Parquet, firmada, checksum | Registro extracción (solicitante, filtro, resultado); control acceso datos sensibles (RT-16.09) |
| Sincronización masiva turno (terreno) | Sincronizadores con partición + reanudación + deduplicación; medios a S3 por objeto | Nivel servicio: turno completo ≤ 10 min; métricas sync en Capa 8 |
| Interfaces periódicas con terceros | Colas con `batch_id` + confirmación por lote | Monitoreo DLQ + acuse por lote en bandeja excepciones |

Fuente: elaboración propia a partir de RT-05.22 (Bases Técnicas Transversales, cap. 5, p. 13).

## Anexo 4-D — Matriz de los doce módulos

<a id="anx:D"></a>

La matriz asigna a cada módulo su requisito funcional, su responsabilidad, su interfaz principal, su actor y la etapa en que entra en producción.

<a id="tab:modulos-funcionales"></a>

**Tabla A.5 — Módulos, responsabilidades e interlocutores**

| **Módulo / RF** | **Responsabilidad** | **Interfaz principal** | **Actor principal** | **Etapa** |
| --- | --- | --- | --- | --- |
| M1 Recepción / RF-01 | Lote y recepción GS1. | Evento a M2; ACL con ERP. | Jefa de Bodega; Proveedor. | 1 |
| M2 Inventario / RF-02 | Movimientos por sitio, reserva central y FEFO. | Consulta de M3/M5. | Jefa de Bodega. | 1 |
| M3 Preventa / RF-03 | Pedido y precio pactado; autoatención por el canal de M11. | Reserva coordinada en M2; sincronización. | Preventista; clientes autorizados. | 1; autoatención en 2 |
| M4 Rutas / RF-04 | Secuencia y restricciones. | Ruta aprobada a M6. | Planificador de Rutas. | 1 |
| M5 Preparación / RF-05 | Misión y carga confirmada. | Guía nocturna vía `erp-sync` y ACL en VM-04. | Preparador; Jefa de Bodega. | 1 |
| M6 Reparto / RF-06 | Entrega y POD. | Evento a M7/M8. | Conductor propio; Conductor externo. | 1 |
| M7 Rendición / RF-07 | Cobro y descuadre. | ACL al ERP; evento a M10. | Conductores; Gerente de Finanzas. | 1 |
| M8 Devoluciones / RF-08 | Retorno y saldo de envases. | Evento a M2/M7. | Conductores; Jefa de Bodega. | 1 |
| M9 Calidad / RF-09 | Lote, frío y bloqueo. | Bloqueo a M5; alerta. | Jefa de Calidad. | 1 |
| M10 Analítica / RF-11 | OTIF operacional y costo de servir. | Consume eventos sin escribir. | Gerentes Comercial, de Finanzas y de Operaciones; Jefa de Calidad. | 1 OTIF; 2 costo |
| M11 Canal moderno / RF-12 | Pedido EDI y excepciones. | Contrato por cadena; M3. | Cliente del canal moderno; Gerente Comercial. | 2 |
| M12 Telemetría / RF-14 | Ruta real, desviación y datos para costo. | GPS a M4/M10. | Planificador de Rutas; Gerente de Operaciones. | 1; costo en 2 |

Fuente: elaboración propia a partir del catálogo de requerimientos y del alcance del capítulo 3.

## Anexo 4-E — Trazabilidad funcional

<a id="anx:E"></a>

La tabla sigue cada grupo de requisitos funcionales hasta el módulo responsable, las capas que lo realizan y la evidencia que permite verificarlo.

<a id="tab:traza-logica"></a>

**Tabla A.6 — Trazabilidad funcional de la arquitectura lógica**

| **Requisito** | **Responsable** | **Capas implicadas** | **Evidencia verificable** |
| --- | --- | --- | --- |
| RF-01 | M1 Recepción | 1, 4, 5 y 6 | Lote GS1 recibido y publicado. |
| RF-02 | M2 Inventario | 4, 5 y 6 | Reserva y FEFO por sitio. |
| RF-03 | M3 Preventa | 1, 3, 4 y 6 | Pedido único tras reconexión. |
| RF-04 | M4 Rutas | 1, 4 y 5 | Ruta revisada en menos de 20 min. |
| RF-05 | M5 Preparación | 1, 4, 5 y 6 | Lectura y carga por lote. |
| RF-06 | M6 Reparto | 1, 4, 5 y 6 | POD unido a entrega. |
| RF-07 | M7 Rendición | 1, 4 y 5 | Descuadre y aprobación segregados. |
| RF-08 | M8 Devoluciones | 1, 4, 5 y 6 | Saldo y causal conciliados. |
| RF-09 | M9 Calidad | 2, 4, 5 y 6 | Bloqueo y liberación por Calidad. |
| RF-11 | M10 Analítica | 4, 5 y 6 | OTIF y costo trazables al evento. |
| RF-12 | M11 Canal moderno | 3, 4 y 5 | Pedido EDI normalizado. |
| RF-14 | M12 Telemetría | 2, 4 y 5 | Ruta real correlacionada. |

Fuente: elaboración propia a partir del catálogo de requerimientos del capítulo 3 y de la Tabla [A.5](LAFROX-Subdocumento4-Anexos.md#tab:modulos-funcionales).

## Anexo 4-F — Mapa de límites de contexto

<a id="anx:F"></a>

El mapa indica, para cada módulo, el tipo de relación con sus interlocutores, el contrato que intercambian y el límite que impide invadir una decisión ajena.

<a id="tab:context-mapping"></a>

**Tabla A.7 — Mapa de límites de contexto**

| **Dueño** | **Relación** | **Interlocutor** | **Contrato** | **Límite** |
| --- | --- | --- | --- | --- |
| M1 Recepción | Traducción por ACL | ERP 2017 | Recepción validada. | ERP no escribe lote. |
| M2 Inventario | Servicio publicado | M3, M4 y M5 | Consulta y reserva. | Cada sitio decide movimientos; N-04/N-05 consolida. |
| M3 Preventa | Cliente de M2 | M2 y M7 | Pedido y sincronización. | No aprueba crédito local. |
| M4 Rutas | Adapta fuente | M3, M6 y GIS | Ruta aprobada. | GIS no decide ruta. |
| M5 Preparación | Proveedor de evento | M2, M6 y ACL | Misión preparada. | ERP emite guía por `erp-sync` local. |
| M6 Reparto | Proveedor de evento | M4, M7 y M8 | Entrega registrada. | No liquida cobro. |
| M7 Rendición | Traducción por ACL | M6 y ERP | Rendición aprobada. | ERP sigue tributario. |
| M8 Devoluciones | Lenguaje publicado | M2 y M7 | Devolución y envase. | No ajusta DTE. |
| M9 Calidad | Proveedor de bloqueo | M1, M5 y sensores | Lote bloqueado. | Calidad libera. |
| M10 Analítica | Consumidor de eventos | M1–M9 y M12 | Indicadores consolidados. | Solo lectura. |
| M11 Canal moderno | Traducción EDI | Cadena, M3 y ACL | Pedido normalizado. | M3 gobierna pedido. |
| M12 Telemetría | Adapta telemetría | GPS, M4 y M10 | Ruta observada. | No registra entrega. |

Fuente: elaboración propia a partir de las responsabilidades de M1–M12 del apartado 4.1.4.

## Anexo 4-G — Catálogo de interfaces internas

<a id="anx:G"></a>

El catálogo conserva los identificadores de las ocho interfaces internas. Las fichas que siguen completan el modo, volumen, ventana y conducta ante lentitud exigidos por RT-05.21. Los volúmenes son escenarios de diseño, no mediciones. Un mensaje de negocio puede atravesar varias interfaces: sus cifras no se suman como operaciones únicas.

<a id="tab:catalogo-internas"></a>

**Tabla A.8 — Integraciones internas: dueño, contrato y continuidad**

| **ID** | **Intercambio** | **Dueño** | **Contrato** | **Falla** |
| --- | --- | --- | --- | --- |
| INT-01 | Pedido preventa y consulta. | M3 | API negocio y sync. | Captura local sin confirmar. |
| INT-02 | Entrega, POD y cobro. | M6/M7/M8 | API sync por lote. | Cola en dispositivo. |
| INT-03 | Eventos bodega a nube. | M2/M5 | Eventos por sitio. | Broker local 24 h. |
| INT-04 | Detalle de cross-docking a la nube. | M2 | Evento de inventario. | Buffer y reconciliación. |
| INT-05 | Eventos de temperatura. | M9 | Evento de excursión. | Bloqueo local. |
| INT-12 | Cambios de datos a réplica. | M2 | CDC de bodega. | Desfase medido; reanudar. |
| INT-13 | Identidad a sitio. | Seguridad | Políticas firmadas. | Asignaciones vigentes. |
| INT-14 | Métricas y trazas. | Operación | OTLP. | Buffer local. |

Fuente: elaboración propia a partir de RT-02.06 y RT-03.12 (Bases Técnicas Transversales, cap. 2, p. 7, y cap. 3, pp. 8–9).

**Parámetros comunes del catálogo**

Los contratos distinguirán aceptación durable de procesamiento concluido. Como valores iniciales de diseño, las consultas interactivas tendrán espera máxima de 5 segundos y las transferencias de lotes, 30 segundos; un timeout produce estado incierto, nunca aprobación. Los reintentos conservan UUID, aplican espera exponencial con dispersión y máximo de 5 minutos entre intentos. Los errores de validación pasan a excepción sin reintento automático. El agotamiento del presupuesto de intentos deriva a una cola de errores con alerta; no elimina la operación. Estos parámetros se ajustarán con la prueba de carga sin relajar los tiempos de negocio exigidos.

##### INT-01. Preventa y consultas — M3

Modo mixto: consultas síncronas y captura/sincronización asíncrona. Volumen de pedidos: 1.400/2.600 por día; las consultas de lectura se estiman en cuatro por pedido (5.600/10.400 llamadas/día) y se miden por separado. Contraparte: API central, ventana requerida 24×7; la app conserva 14 horas de trabajo. Dentro de 2 segundos, si no hay respuesta vigente, muestra la copia fechada; no confirma reserva ni crédito. Lotes de sincronización esperan hasta 30 segundos y se reenvían con la misma clave. La confirmación final corresponde a M2/M3 y al control de crédito.

##### INT-02. Reparto, POD y rendición — M6/M7/M8

Modo asíncrono para evidencia y rendición; consulta de resultado síncrona. Base mínima: 1.400/2.600 entregas diarias (caso, cap. 14). Se consideran cinco operaciones por entrega: 7.000/13.000 operaciones/día; los eventos no aplicables no se emiten. Fotografías y firmas viajan como objetos con hash, separados del mensaje. Contraparte: API y almacenamiento central, requeridos 24×7. Timeout de lote: 30 segundos. La cola cifrada del dispositivo conserva el turno de 14 horas; solo elimina el evento local después de confirmar mensaje y objetos completos. No registra pago autorizado por ausencia de respuesta del POS.

##### INT-03. Eventos de bodega a nube — M1/M2/M5/M9

Modo asíncrono mediante outbox, RabbitMQ y consumidor canónico. Sobre de diseño: 260.000 ÷ 22,14 × 5 ≈ 58.710 eventos/día; peak: 109.032, con factor 1,857. Es el total de trazabilidad de los sitios, no una carga adicional por sitio. Contraparte: ingesta central, requerida 24×7. Sin acuse en 30 segundos, el productor retiene y reintenta; el acuse del broker no sustituye el acuse transaccional del dominio. Se conserva al menos 24 horas de actividad local y se mide la edad del evento local más antiguo. El consumidor deduplica por sitio y UUID antes de actualizar el dominio.

##### INT-04. Detalle de cross-docking a la nube — M2

Modo asíncrono. Volumen de diseño: 5.600/10.400 eventos/día, derivado de cuatro operaciones por cada una de las 1.400/2.600 entregas; no se suma de nuevo al total de INT-03. Contraparte: consolidación N-04/N-05 en nube, requerida 24×7. Timeout de acuse de 30 segundos; cada sitio mantiene su operación, buffer de 24 horas y secuencia propia. Al reconectar se reconcilia inventario en tránsito y se aísla cualquier doble compromiso.

##### Coordinación de reserva y retención — desarrollo de INT-03/04, M2

Modo asíncrono con respuesta durable, requerida para confirmar el pedido. M2 central publica cada solicitud en una cola FIFO del sitio, que su shipper lee por conexión saliente. M2 local valida y retiene, y su outbox devuelve el acuse por INT-03/04. Contrapartes: M2 central y M2 del sitio que custodia el stock, requeridas durante la toma y confirmación de pedidos y la liberación de reservas. Un timeout de transporte de 30 segundos deja la operación pendiente o incierta y nunca la confirma. La latencia de negocio se mide contra el objetivo de confirmación de reserva del Anexo 4-T, que es distinto de ese timeout.

Cada sobre JSON versionado lleva UUID, correlación, sitio, época de autoridad, lote, ubicación, cantidad y tipo: retener, liberar o resultado. Cada cola tiene un consumidor exclusivo con rol IAM de mínimo privilegio, validación de esquema y auditoría. Una repetición devuelve el resultado ya persistido. Una época obsoleta o un esquema incompatible pasa a la bandeja de excepciones. Durante un corte, el sitio conserva sus retenciones y la nube no confirma ni libera sin acuse durable. Al reconectar se consulta por clave y se concilia el resultado antes de reintentar. Volumen de diseño: 46.968/87.228 mensajes/día, con cuatro mensajes por línea de pedido (Anexo 4-I).

##### INT-05. Temperatura — M9

Modo asíncrono para muestras y alarma local inmediata. Volumen: 10.920 lecturas/día en régimen y peak, por 21 puntos de cámara × 288 lecturas más 28 termógrafos × 174 lecturas entre 05:30 y 20:00 (6.048 + 4.872). La ventana va desde la carga en la cámara hasta el regreso del último camión, que ocurre a más tardar a las 20:00 (Bases Técnicas del caso, anexo B, p. 38). El termógrafo registra en forma continua mientras el camión lleva producto de frío. Si una ruta se extiende, la lectura adicional se transmite al sincronizar. Contraparte: IoT Core/ingesta central, requerida 24×7; el bloqueo M9–M5 permanece local y no espera a nube. Acuse remoto máximo de 30 segundos por lote. Gateway: retención de 24 horas; termógrafo: registro de toda la ruta, hasta 14,5 horas en el horario declarado y continuo si la ruta se extiende. Una pérdida de señal o lectura obsoleta genera una incidencia diferenciada de la excursión térmica.

##### INT-12. Réplica de lectura del WMS de Talca — M2/Datos

Modo asíncrono CDC. El volumen físico depende del WAL y no equivale al número de eventos EPCIS. Para la prueba se usa V_WAL=N_T× b_WAL, donde N_T son los cambios medidos en Talca y b_WAL, bytes medidos por cambio. Los 12.602/23.404 cambios diarios son una cota conservadora calculada con los movimientos de todos los sitios, no un conteo propio de Talca; se aplica como cota al WAL de Talca, estimado en 0,123 GB/día. Migraciones, índices y amplificación se miden aparte. Contraparte: réplica Aurora de solo lectura, requerida 24×7. Se alerta al superar 5 minutos de retraso y se escala antes de 15; si caen fibra y LTE, Starlink en espera caliente toma el tráfico prioritario de DMS/WAL y sostiene RPO ≤ 15 minutos; con los tres caminos caídos, el WAL se conserva localmente para reconciliación. AL-DR-01 verifica el escenario de pérdida de sitio.

##### INT-13. Identidad y manifiestos — Seguridad

Modo mixto: autenticación central síncrona y distribución asíncrona de manifiestos. Se estiman 764 eventos/día (382 dispositivos × 2), tanto en régimen como en peak. Contraparte: Keycloak, requerida 24×7. Timeout interactivo: 5 segundos. Sin enlace se usa el verificador local con manifiesto de 26 horas, caché de identidad de 24 horas y permisos de turno de 8/14 horas. No se habilitan nuevas altas ni privilegios. AL-OFF-01 prueba dos relevos y el rechazo de identidades no preinscritas.

##### INT-14. Métricas, logs y trazas — Operación

Modo asíncrono por OTLP. Presupuesto de diseño: 13.000 eventos/día en régimen y peak (13 nodos × 1.000 eventos: 6 VM de Talca, 4 de Concepción y 3 mini-PC); son unidades de observabilidad y no mensajes comerciales sumables. Contraparte: colectores y CloudWatch, requeridos 24×7. Exportación con timeout de 30 segundos y buffer en disco de 24 horas. El fallo de exportación no bloquea negocio; el sitio mantiene alarma local por ocupación. Auditoría de negocio y eventos de seguridad no se descartan para conservar trazas diagnósticas.

Fuente: elaboración propia a partir de las Bases Técnicas del caso (cap. 14, p. 24) y RT-05.21 (Bases Técnicas Transversales, cap. 5, p. 13). Las tasas de consultas son supuestos de ensayo explícitos; su calibración exige medición.

## Anexo 4-H — Catálogo de interfaces externas

<a id="anx:H"></a>

La tabla identifica, para cada integración con terceros, el dueño interno, el contrato y la respuesta ante falla; las fichas que siguen completan modo, volumen, ventana y tiempo de espera.

<a id="tab:catalogo-externas"></a>

**Tabla A.9 — Integraciones externas y respuesta ante falla**

| **ID** | **Tercero** | **Dueño interno** | **Contrato** | **Falla** |
| --- | --- | --- | --- | --- |
| INT-06 | ERP 2017 | ACL/M7 | Adaptador versionado. | Cola; sin escritura directa. |
| INT-07 | Emisor DTE del ERP y SII | ACL/M5 | Guía y estado tributario. | Bloquear nueva salida afectada. |
| INT-08 | Cadenas modernas | M11 | Perfil EDI por cadena. | Bandeja y aviso acordado. |
| INT-09 | Pasarela de pago | M7 | Autorización con clave única. | Efectivo o crédito aprobado. |
| INT-10 | Mapas y geocodificación | M4 | API proveedor. | Ruta precargada. |
| INT-11 | Avisos al cliente | Trabajador Laravel de notificaciones | SNS o API del proveedor de notificaciones. | Reintento por canal acordado. |
| INT-15 | Telemetría existente | M12 | API de solo lectura. | Ruta planificada sin posición. |

Fuente: elaboración propia a partir de las Bases Técnicas del caso (cap. 5, p. 10) y RT-05.21 (Bases Técnicas Transversales, cap. 5, p. 13).

**Condiciones de servicio de las contrapartes**

Las ventanas siguientes expresan la disponibilidad que requiere Puelche. El catálogo no atribuye un SLA no acreditado al ERP, SII, cadenas ni proveedores. Antes de habilitar cada integración se incorporarán al contrato su horario efectivo, mantenimientos, cuotas y escalamiento; una ventana inferior a la requerida exige ajuste contractual u operativo. Los timeouts son parámetros iniciales del adaptador, sujetos a ensayo y al contrato de contraparte.

##### INT-06. ERP 2017 — ACL/M7

Modo asíncrono para intercambio de negocio; consulta síncrona de estado cuando una escritura queda incierta. Volumen normal/peak: 2.025/3.762 mensajes/día, calculados con los flujos diarios y equivalentes de 22,14 días; peak con factor 1,857. Contraparte requerida 24×7, especialmente preparación 22:00–06:00 y despacho 05:30–07:00. Timeout de 10 segundos por llamada. Ante lentitud se abre cortacircuito, se conserva la solicitud y se prioriza despacho; ante respuesta perdida se consulta por clave externa antes de repetir. Un error funcional va a excepción. No se escribe directamente en tablas del ERP.

##### INT-07. Emisión y estados DTE — ACL/M5

Modo síncrono para conocer el resultado documental antes de liberar salida, con seguimiento asíncrono de estados. Volumen normal/peak: 3.071/5.703 mensajes/día, con factor de septiembre 1,857. Polling y reintentos se miden aparte. Contrapartes: emisor ERP y su canal SII; se requiere servicio durante preparación y disponibilidad sin interrupción para las 96 salidas de 05:30–07:00. Timeout de llamada: 10 segundos, sin equiparar timeout a rechazo o autorización. Resultado incierto obliga a consultar la misma solicitud. La cola no habilita salida sin documento; se aplica el control y el protocolo AL-DTE-01. El ERP sigue siendo el único emisor.

##### INT-08. Cadenas del canal moderno — M11

Modo asíncrono EDI; el MDN es acuse de transporte, separado de la respuesta comercial. Desde enero de 2029 opera todos los días: 616/1.144 mensajes/día (1.400 y 2.600 pedidos × 11 % × 4 intercambios); hoy el volumen es 0. Contraparte requerida 24×7, con cortes de recepción y ventanas de entrega específicos de cada cadena, que deben figurar en su acuerdo. Timeout inicial de transporte: 30 segundos; MDN asíncrono esperado en 15 minutos como umbral de alerta propuesto, no SLA de la cadena. OpenAS2 conserva identificador y evidencia; M11 deduplica, valida equivalencias y deriva rechazo funcional a bandeja. Una entrega técnica no confirma el pedido ni permite superar su hora de corte.

##### INT-09. Pasarela de pago — M7

Modo síncrono. Volumen normal/peak: 2.800/5.200 mensajes/día como cota: a lo más un pago electrónico por entrega (1.400/2.600) y dos mensajes por pago, solicitud y respuesta. Los 11.800 cobros mensuales del caso son en efectivo y no miden pagos con tarjeta. Contraparte requerida 24×7, cubriendo el turno de reparto de hasta 14 horas. Timeout de 10 segundos. Si el resultado es incierto, se consulta por la misma clave antes de volver a cobrar. Sin respuesta no se registra autorización; se ofrece efectivo o crédito previamente aprobado según política del CLIENTE. Se concilia el resultado tardío para evitar cobro duplicado.

##### INT-10. Mapas y geocodificación — M4

Modo síncrono para consultas y asíncrono para cálculos extensos. Volumen normal/peak: 96/96 llamadas/día, con el mismo volumen en ambos escenarios. Contraparte requerida 24×7, con planificación previa a la salida y apoyo en ruta. Timeout de 5 segundos para consulta; trabajos largos tienen identificador y consulta de avance sin bloquear la API. Se conserva la ruta aprobada y cartografía precargada. La falta de proveedor impide nuevo cálculo que lo requiera, no borra la ruta vigente; cuotas o error 429 aplican espera informada.

##### INT-11. Avisos al cliente — Notificaciones

Modo asíncrono mediante trabajos Laravel y SNS/API de canal. Dos avisos por entrega: 2.800/5.200 mensajes/día (1.400/2.600 entregas). Contraparte requerida 24×7; las franjas permitidas de contacto se parametrizan por canal y cliente. Timeout de 10 segundos; reintento con clave de aviso y vigencia. Un aviso de ETA vencido se descarta con registro, no se envía al día siguiente. El estado enviado se distingue de recibido y no condiciona el registro de entrega. Falla persistente produce aviso operacional y canal alternativo acordado.

##### INT-15. Telemetría de flota — M12

Modo asíncrono o extracción periódica de solo lectura según API existente. Volumen normal/peak: 60.480/60.480 posiciones/día, calculadas para 42 camiones × 120 posiciones/h × 12 h; el peak no aumenta esta fuente. Contraparte requerida 24×7 para conservar historial y cubrir turnos. Timeout de 10 segundos por consulta o 30 por lote; reanudación por cursor y deduplicación. Sin datos se muestra posición fechada y ruta prevista, nunca una posición presuntamente actual. La geolocalización no sustituye al POD.

Fuente: elaboración propia a partir de las Bases Técnicas del caso (cap. 14, p. 24) y RT-05.21 (Bases Técnicas Transversales, cap. 5, p. 13). Los SLA de terceros requieren respaldo contractual; los supuestos de dimensionamiento se distinguen de la volumetría del caso.

## Anexo 4-I — Volumen de mensajes

<a id="anx:I"></a>

Esta síntesis permite contrastar órdenes de magnitud. Los anexos 4-G y 4-H son el catálogo por interfaz e identifican ventana, modo, unidades y supuestos. Las cifras siguientes incluyen flujos encadenados: no se suman para obtener transacciones únicas ni dimensionan por sí solas bytes de evidencia, WAL o ancho de banda. El peak depende de la variable que crece, no de duplicar todas las fuentes.

<a id="tab:volumen-mensajes"></a>

**Tabla A.10 — Volumen de mensajes por integración (derivado volumetría caso)**

| **Integración** | **Volumen régimen** | **Peak septiembre** | **Derivación** |
| --- | --- | --- | --- |
| INT-01 Pedido preventa | 1.400 msg/día | 2.600 | Entregas diarias habituales y peak de septiembre |
| INT-02 Entrega, POD y cobro | 7.000 msg/día | 13.000 | Cinco operaciones por entrega |
| INT-03 Eventos bodega a nube | 58.710 msg/día | 109.032 | 260.000 líneas ÷ 22,14 × 5; peak × 1,857 |
| INT-04 Detalle de cross-docking a la nube | 5.600 msg/día | 10.400 | Cuatro operaciones por entrega |
| INT-03/04 Coordinación de reserva | 46.968 msg/día | 87.228 | 260.000 líneas ÷ 22,14 × 4; peak: 21.807 líneas × 4 |
| INT-05 Temperatura | 10.920 msg/día | 10.920 | 21 × 288 lecturas de cámara + 28 × 174 de termógrafo |
| INT-06 ERP 2017 | 2.025 msg/día | 3.762 | Flujos ERP sobre 22,14 días; peak × 1,857 |
| INT-07 DTE/SII | 3.071 msg/día | 5.703 | 34.000 documentos ÷ 22,14 × 2; peak × 1,857 |
| INT-08 EDI cadenas modernas | 616 msg/día | 1.144 | Escenario 2029 (hoy 0): 1.400 y 2.600 × 11 % × 4 |
| INT-09 Pasarela de pago | 2.800 msg/día | 5.200 | Cota: un pago electrónico por entrega × 2 mensajes |
| INT-10 Mapas y geocodificación | 96 llamadas/día | 96 | Volumen constante en ambos escenarios |
| INT-11 Avisos al cliente | 2.800 msg/día | 5.200 | Dos avisos por entrega |
| INT-12 Cambios a réplica | 12.602 cambios/día | 23.404 | Peak × 1,857; WAL estimado de 0,123 GB/día en Talca |
| INT-13 Identidad y manifiestos | 764 eventos/día | 764 | 382 dispositivos × 2 |
| INT-14 Métricas, logs y trazas | 13.000 eventos/día | 13.000 | 13 nodos × 1.000 eventos |
| INT-15 Telemetría de flota | 60.480 posiciones/día | 60.480 | 42 camiones × 120 posiciones/h × 12 h |
| **Total** | **228.852/día** | **351.933/día** | **15 integraciones** |

Fuente: elaboración propia a partir de las Bases Técnicas del caso (cap. 14, p. 24). Los cálculos se indican en la columna de derivación.

La coordinación de reserva supone una retención por línea de pedido. Cada retención usa como máximo cuatro mensajes: solicitud y resultado de la retención, y solicitud y resultado de una liberación. La cifra supone que toda retención se libera, lo que sobrestima el flujo porque una retención consumida por la preparación no genera liberación. Esa holgura cubre las líneas repartidas entre lotes o sitios, cuya proporción mide AL-STOCK-01. Este flujo no duplica los movimientos físicos de INT-03 ni las operaciones de INT-04.

## Anexo 4-J — Funciones sin conexión

<a id="anx:J"></a>

La tabla declara qué funciones siguen disponibles sin enlace, cómo continúan localmente y qué ocurre al reconectar, conforme a RT-03.13.

<a id="tab:funciones-offline"></a>

**Tabla A.11 — Funciones sin conexión y procedimiento de continuidad**

| **Función** | **Estado** | **Continuidad local** | **Al reconectar** |
| --- | --- | --- | --- |
| Pedido preventa | Captura 14 h | Precio y stock informativos; pedido sin confirmar. | M2 valida reserva y crédito. |
| Pedido de autoatención | Captura en el portal instalado | Catálogo y precios con fecha; pedido en cola con UUID. | M3 valida stock y crédito y responde al cliente. |
| Entrega y POD | Captura 14 h | Evidencia cifrada y cola persistente. | M6 confirma o abre excepción. |
| Recepción y preparación | Opera 24 h | Registro GS1 y bloqueo térmico local. | Eventos a nube y conciliación. |
| Cobro en efectivo | Captura 14 h | Comprobante y custodia según política. | M7 rinde y concilia. |
| Autorización POS | No disponible | Efectivo o crédito autorizado; sin cargo presunto. | Autorizar una sola vez. |
| Nueva guía electrónica | Talca: disponible por RabbitMQ local; otros sitios: preemitida. | `erp-sync` en VM-04 consume RabbitMQ de Talca sin WAN y, por salida, la cola FIFO de solicitudes al ERP de los demás sitios, que reciben la respuesta por su cola; fuera de Talca se requiere un camino del sitio y uno de Talca. | M5 libera solo la carga amparada por la guía vigente; un ajuste sin camino hasta el ERP pasa a la ruta siguiente. Una guía anulada no se reutiliza: esa salida espera un documento válido. |
| Ruteo y mapas en línea | No disponible | Usar secuencia y mapas precargados. | Recalcular cambios sin confirmar. |
| EDI de supermercados | No disponible | Registrar incidente y aviso acordado con cadena. | Cola y bandeja de excepciones. |
| Tablero central | No disponible | Alarmas y bitácora local sostienen despacho. | Reponer telemetría y estado. |

Fuente: elaboración propia a partir de RT-03.10 y RT-03.13 (Bases Técnicas Transversales, cap. 3, pp. 8–9).

## Anexo 4-K — Reglas de reconciliación

<a id="anx:K"></a>

La tabla fija, para cada conflicto de negocio, la regla que lo resuelve, el lugar donde se ejecuta y los datos que conserva la bitácora del Artículo 16.4.

<a id="tab:reglas-reconciliacion"></a>

**Tabla A.12 — Reglas de reconciliación y bitácora Art. 16.4**

| **Conflicto** | **Regla de resolución** | **Dónde se ejecuta** | **Bitácora Art. 16.4** | **Dec. / ADR** |
| --- | --- | --- | --- | --- |
| Doble reserva stock (preventa offline vs online) | M2 ordena por recepción central y correlativo de desempate, y confirma solo tras la retención local durable. La solicitud no cubierta queda en excepción con aviso. | Capa 4 (M2/M3) | Pedido, stock, regla, resultado y hora. | Decisión 16.1 N° 8; RT-03.12 |
| Pedido duplicado (reenvío offline) | M3 conserva el UUID y devuelve el resultado ya persistido, sin volver a reservar ni cobrar. | Capa 4 (M3) | transaction_id, event_id y resultado previo. | RT-02.06 |
| Entrega offline vs cancelación back-office | M6 aísla el conflicto: compara estado y evidencia; un supervisor resuelve antes de ajustar cobro o DTE. | Capa 4 (M6/M7) | Entrega, cancelación, POD y decisión motivada. | Decisión 16.1 N° 1 |
| Excursión térmica detectada offline | Ante una excursión crítica y sostenida, M9 bloquea localmente la salida; solo Calidad libera tras evaluación. | Capas 2 y 4 (M9/M5) | Sensor, umbral, lote, bloqueo y liberación. | Decisión 16.1 N° 4 |
| Rendición conductor offline vs ERP caído | M7 conserva la captura en el dispositivo hasta reconexión; el sitio retiene sus propios eventos en RabbitMQ; `erp-sync` en VM-04 consume RabbitMQ local y SQS por salida, y reintenta con cortacircuito | Capa 1 (dispositivo) + Capa 4 (M7) + Capa 5 + ACL | conductor_id, monto, causal descuadre, reintentos ERP | INT-06, RT-10.08 |
| Conflicto envases (conductor devuelve vs cliente niega) | Cuenta corriente por cliente (saldo, no unidad); registro EnvaseMovido con firma/QR conductor; disputa → bandeja excepciones | Capa 4 (M8) | cliente_id, tipo envase, firma/QR, decisión (saldo actualizado) | Decisión 16.1 N° 10 |
| Cambio de precio entre captura y confirmación | M3 conserva el precio pactado bajo condiciones autorizadas (RNG-08 del Subdocumento 3). Una lista posterior no lo cambia. Una propuesta offline fuera de esas condiciones queda en excepción | M3 + M7 | pedido_id, precio pactado, versión de condiciones y excepción | Decisión 16.1 N° 9 |
| Devolución tras guía emitida | M8 conserva cantidad, lote y causal; el ERP decide y emite el documento tributario posterior mediante ACL | M8 + ACL | entrega_id, guía original, devolución, documento resultante | Decisión 16.1 N° 12 |

Fuente: elaboración propia a partir de las Bases Técnicas del caso (cap. 16, pp. 28–29) y RT-03.12 (Bases Técnicas Transversales, cap. 3, pp. 8–9).

## Anexo 4-L — Decisiones del numeral 16.1

<a id="anx:L"></a>

La tabla conserva el número y la pregunta de cada decisión del numeral 16.1 del caso, la regla o componente propuesto y la validación que corresponde al CLIENTE.

<a id="tab:16-decisiones"></a>

**Tabla A.13 — Decisiones de diseño del numeral 16.1**

| **Nº** | **Pregunta del caso** | **Regla o componente propuesto** | **Validación** |
| --- | --- | --- | --- |
| 1 | Entrega parcial e indicador de servicio | M6 distingue entregado completo, parcial y no entregado; M10 calcula OTIF por pedido completo y ventana acordada. | Criterio comercial |
| 2 | Unidad de trazabilidad sanitaria | M9 traza GTIN y lote proveedor; M1/M5 vinculan cada movimiento a SSCC. | Unidad con Calidad |
| 3 | Local cerrado y responsable del reintento | M6 registra intento, causal y evidencia, y reagenda a la siguiente ventana. Si la ausencia persiste, retorna al CD y nunca entrega a terceros (RNG-05). | Plazo y autoridad |
| 4 | Excursión térmica, decisión y bloqueo | M9 aplica umbral y duración por producto: advertencia ante una excursión menor y transitoria, y retención en M2/M5 ante una crítica y sostenida. Calidad libera, bloquea o rechaza. | Umbrales con Calidad |
| 5 | Identidad y sustitución de conductor externo | Despacho registra en la Etapa 1 el vínculo empresa–conductor–vehículo–turno, y el portal lo habilita al representante en la Etapa 2. OTP inicial, revocación y autor de cada POD. | Procedimiento transportista |
| 6 | Efectivo y riesgo del dinero en ruta | M7 conserva cobro y rendición individual con causal de diferencia; Puelche define custodia y límite por turno. | Política de Tesorería |
| 7 | Costo de servir y clientes no rentables | M10 calcula costo por entrega con ruta, tiempo, devoluciones y envases; Comercial decide medidas, no el algoritmo. | Criterio comercial |
| 8 | Dos preventistas comprometen el mismo stock | M2 central confirma tras la retención local durable, por orden de recepción y correlativo. M3 deja sin confirmar el pedido offline y comunica el quiebre al sincronizar. | Desempate según RNG-01 |
| 9 | Precio cambia antes del despacho | M3 conserva el precio pactado y la versión de condiciones. Un cambio posterior de lista no altera lo acordado (RNG-08). | Política de precios |
| 10 | Control de envases retornables | M8 registra saldo por cliente, tipo y movimiento con evidencia; se concilia en la rendición. | Modalidad de cargo |
| 11 | Maestro de productos ante cambios del proveedor | M1 ingresa equivalencia GTIN/formato; el maestro autorizado se sincroniza mediante ACL con ERP y preserva historial. | Dueño del maestro |
| 12 | Devolución y DTE ya emitido | M8 registra devolución y causal; ACL solicita al ERP el documento tributario que corresponda, enlazado al original. | Regla tributaria |
| 13 | Objeción sindical a cámaras y geolocalización | M12 usa telemetría de flota para ruta y costo; excluye cámaras en cabina y control de jornada por GPS. | Gestión laboral |
| 14 | Destino del WMS 2013 | M1, M2 y M5 reemplazan sus capacidades en Etapa 1 por sitio y ola, con reversión controlada (ADR-08). | Corte por sitio |
| 15 | Receptor distinto, imposibilidad o negativa a firmar | M6 identifica receptor y causal; conserva QR, fotografía o constancia de negativa según política, sin equiparar automáticamente POD con acuse tributario. | Validez de evidencia |
| 16 | Conocimiento concentrado del planificador | M4 guarda restricciones, excepciones y decisiones del planificador; la transición incluye transferencia y prueba de rutas. | Aceptación Operaciones |

Fuente: elaboración propia a partir de las Bases Técnicas del caso (cap. 16, pp. 28–29).

## Anexo 4-M — Verificación de continuidad lógica

<a id="anx:M"></a>

Este anexo establece los protocolos de aceptación. Cada ejecución conserva configuración, datos de carga, relojes sincronizados, inyección de fallas, trazas, resultados observados y acta.

**AL-DTE-01. Emisión documental de 96 salidas**

Operaciones prepara las 96 cargas de la ventana 05:30–07:00 y registra origen, destino, versión de carga y guía requerida. La matriz de ensayo incluye y comprueba ambas rutas de emisión: en Talca, M5 publica en RabbitMQ local y `erp-sync` en VM-04 consume sin WAN; en Concepción y los cross-docking, RabbitMQ local entrega al shipper, este publica en la cola FIFO de solicitudes al ERP, `erp-sync` la consume por conexión saliente y la respuesta vuelve por la cola del sitio. Dos procesos `erp-sync` en VM-04 solicitan la guía al ERP mediante la ACL. Al cerrar cada carga nocturna queda preemitida la guía y el ERP conserva el intercambio con el SII por fibra, LTE o Starlink en espera caliente de Talca.

El ensayo inyecta caída de fibra y LTE, respuesta extraviada del ERP, reintento, indisponibilidad transitoria del SII y cambio de carga después de la preemisión en ambas rutas. Un cambio invalida la guía: el ERP la anula según su procedimiento y emite otra antes de liberar, usando cualquiera de los tres caminos de Talca; fuera de Talca se requiere además un camino del sitio. Se comprueba por origen la secuencia RabbitMQ–`erp-sync` o RabbitMQ–shipper–cola de solicitudes–`erp-sync`–cola de respuesta, folio, carga, documento local, acuse y ausencia de duplicados. También se cortan los caminos hasta el ERP: el camión sale solo con la carga amparada por su guía vigente y el ajuste pasa a la ruta siguiente. Una guía anulada no se reutiliza: esa salida espera un documento válido. La aceptación exige documento válido para cada una de las 96 salidas; ninguna salida se libera por una autorización genérica.

**AL-DR-01. Recuperación de sitio y región**

RT-07.04 fija RTO ≤ 4 horas y RPO ≤ 15 minutos para servicios críticos. Se mide RPO_observado=t_incidente-t_ultimo_punto_consistente con UUID, secuencia y la última transacción confirmada recuperable fuera del sitio.

El protocolo mantiene carga de negocio y corta fibra, LTE y satélite de uno en uno y en pares; verifica que el camino restante transporte DMS/WAL de Talca, broker, outbox e identidad con retraso inferior a 15 minutos. En cada CD se provoca luego pérdida de sala o servidor con al menos un camino de extracción activo. Para Talca se detiene DMS, se habilita su copia de Aurora para escritura y se levanta `wms_only` en ECS Fargate; terminales y periféricos acceden por VPN. Con la sala de Talca perdida se comprueba que salen las cargas con guía preemitida y que una carga nueva queda bloqueada hasta restituir el ERP. También se ensaya promoción de us-east-1 si sa-east-1 falla. Concepción se reconstruye desde eventos centrales y recupera su propia operación; no recibe la carga de Talca.

Se contrastan pedidos, stock por sitio, preparación, bloqueos sanitarios y evidencias con el oráculo de prueba y se miden RTO y RPO completos. Una prueba separada mantiene el sitio operativo sin los tres caminos durante 24 horas para verificar autonomía y alarmas; el límite residual de pérdida simultánea de los tres medios seguida de destrucción del sitio se justifica en 4.3.2.

El ensayo semestral mide RPO ≤ 15 minutos para transacciones en nube, WMS de Talca, mensajes críticos, evidencias y documentos tributarios en S3 y telemetría de temperatura; analítica y mensajes no críticos tienen objetivo ≤ 24 horas, y las posiciones de flota, ≤ 24 horas dentro de sa-east-1. En S3 se verifica Replication Time Control, su objetivo de 99,99% de objetos en 15 minutos, los objetos pendientes y el evento de umbral que dispara la recopia; en DynamoDB Global Tables se mide ReplicationLatency y se comprueba la alarma a 60 segundos.

La conmutación regional ensaya la decisión del CLIENTE con autorizador titular y suplente facultado: si el titular no responde en 15 minutos, decide el suplente, y el paso de autorización no supera 30 minutos. El acta registra los ocho pasos y su peor caso secuencial de 5 + 30 + 20 + 30 + 15 + 15 + 5 + 15 = 135 minutos, dentro del RTO de 4 horas; el último paso redirige los shippers y `erp-sync` a las colas equivalentes, creadas vacías en la región secundaria.

**AL-OFF-01. Autonomía de 24 horas con dos relevos**

El ensayo cubre Talca, Concepción y cada cross-docking con el mismo perfil `wms_only`. Se preinscriben usuarios, dispositivos, turnos y permisos. El corte de los tres caminos comienza justo antes de renovar el manifiesto firmado de 26 horas; la caché descriptiva dura 24 horas.

A las 8 y 16 horas, personas distintas se identifican con PIN personal en terminal enrolado. Se comprueban firma, vigencia, sitio, rol y turno; se rechazan manifiesto alterado, PIN incorrecto, dispositivo no autorizado y privilegio nuevo. Se reinicia un componente y se verifica persistencia de outbox, bitácora y permisos. Durante el corte se ejecutan recepción, retención local, preparación, bloqueo térmico y despacho con guía válida preemitida; al reconectar se drenan eventos repetidos y fuera de orden.

La aceptación exige dos relevos autorizados, operaciones confirmadas aplicadas una sola vez, conflictos conciliados y auditoría completa. Se registran ocupación, retraso de cola y tiempo de drenaje con carga de septiembre; AL-DTE-01 verifica por separado una nueva guía y la invalidación de una guía preemitida.

**AL-CLI-01. Pedido de autoatención sin señal**

El ensayo usa el Portal de Clientes instalado en un teléfono Android y en uno iOS de gama básica, con cuentas activadas por el procedimiento del preventista. Con el teléfono sin red se consulta el catálogo descargado, se arma un pedido nuevo y se repite uno anterior; luego se cierra la aplicación y se reinicia el teléfono.

Al recuperar cobertura se verifica que cada pedido se envía una sola vez, aunque se repita el envío con el mismo UUID, y que M3 responde confirmado o con diferencias de stock, crédito o precio. Se rechazan el pedido con sesión vencida y el pedido de una cuenta bloqueada. La aceptación exige que ningún pedido armado sin señal se pierda o se duplique y que la reserva de stock ocurra solo al recibirlo M3.

## Anexo 4-N — Correspondencia de componentes lógicos

<a id="anx:N"></a>

La matriz identifica los doce módulos y los servicios transversales para cotejarlos con el esquema y explicación de solución exigidos en 3.3–3.4 y con su realización física en 4.2. Las capacidades de 3.3 y 3.4 se corresponden con los módulos y contratos de 4.1; la tabla de correspondencia de 4.2.2 identifica su realización física.

<a id="tab:correspondencia-modulos"></a>

**Tabla A.14 — Correspondencia de módulos y realización física**

| **Módulo** | **Capacidad en 3.3/3.4** | **Contrato** | **Realización en 4.2.2** |
| --- | --- | --- | --- |
| M1 | Recepción | INT-03/06 | Perfil WMS local, base por sitio y ACL ERP. |
| M2 | Inventario | INT-03/04/12 | WMS por sitio, consolidación central y réplica de lectura de Talca. |
| M3 | Preventa | INT-01/06 | App Kotlin y API Laravel central. |
| M4 | Ruteo | INT-10 | Servicio de planificación y optimizador separado por contrato. |
| M5 | Picking y carga | INT-03/07 | HHT, puerta local y WMS con control de guía. |
| M6 | Entrega y POD | INT-02 | App de reparto, API y almacenamiento de evidencia. |
| M7 | Rendición y cartera | INT-02/06/09 | API, trabajadores Laravel y ACL de cobranza. |
| M8 | Devoluciones | INT-02/03/06 | Registro móvil/local y servicios de conciliación. |
| M9 | Trazabilidad y frío | INT-03/05 | Bloqueo local, ingesta IoT y consulta de lotes. |
| M10 | Analítica | Eventos canónicos | Ingesta a lago y servicios de consulta analítica. |
| M11 | Canal moderno | INT-08 | Reglas Laravel, OpenAS2 y conector por cadena. |
| M12 | Telemetría | INT-15 | Adaptador de solo lectura y consulta de ruta real. |

Fuente: elaboración propia.

La tabla verifica la correspondencia de los doce módulos con sus capacidades, contratos y realizaciones; la Tabla 8 del apartado 4.2.2 completa el enlace físico. Las capacidades transversales también se corresponden: presentación y borde con aplicaciones, CloudFront y acceso privado; puerta de enlace con API central y puerta local; eventos con RabbitMQ, shipper y SQS; datos con bases, réplica de lectura y objetos; identidad con Keycloak y verificador local; secretos y auditoría con sus servicios de custodia; observabilidad con OpenTelemetry/ADOT, alarma local y CloudWatch. Notificaciones se traza a INT-11; el motor de optimización de M4 conserva contrato separado y no se presume implementado en PHP por la elección del backend.

La correspondencia entre 3.3, 3.4, 4.1 y 4.2.2 se verifica en ambos sentidos mediante identificador, contrato, responsable y realización física.

**Inventario trazable de capacidades transversales**

Los siguientes 37 identificadores complementan los doce módulos: el inventario lógico tiene 49 unidades verificables. La última columna resume el criterio de correspondencia; la realización física de cada identificador está en la Tabla 8 del apartado 4.2.2.

<a id="tab:inventario-transversal"></a>

**Tabla A.15 — Inventario transversal y realización física**

| **ID** | **Componente** | **Capacidad** | **Contrato** | **Correspondencia 4.2.2** |
| --- | --- | --- | --- | --- |
| UI-MOV | Apps Kotlin / Room | preventa y entrega | INT-01/02 | M3/M6/M7/M8 |
| UI-HHT | Terminales de bodega | preparación | INT-03 / API local | M1/M2/M5 |
| UI-WEB | Portales Angular | Administración; portales | API autorizada | Roles por empresa |
| BOR-PUB | CloudFront / AWS WAF / AWS Shield Advanced | seguridad | HTTPS | Entrada pública única |
| BOR-B2B | Superficie AS2 | canal moderno | INT-08 | Contrapartes registradas |
| GW-CENT | REST API / authorizer | plataforma | API / sincronización | ADR-13 |
| GW-LOCAL | Puerta API de sitio | WMS | INT-03 | Validación sin WAN |
| AUTH-CENT | Keycloak | seguridad | INT-13 / OIDC | Autoridad de identidad |
| AUTH-LOCAL | Verificador de turnos | continuidad | Manifiesto firmado | PIN, turno y sitio |
| WMS-SITE | Perfil WMS local | WMS | INT-03 | Un escritor por sitio |
| INT-BROKER | RabbitMQ | integración | AMQP | Persistencia y DLQ |
| INT-SHIPPER | Shipper local a nube | integración | JSON / SQS | Acuse después de envío |
| INT-CONSUMER | Consumidor PHP | integración | AsyncAPI / JSON | Persistir antes de acuse |
| INT-JOBS | Trabajadores Laravel | notificaciones y EDI | Colas internas | Perfil de trabajos en N-04 (Fargate) |
| INT-SCHED | Planificador | administración | Tareas versionadas | Un líder por ambiente |
| INT-ACL | Adaptador ERP | ERP / DTE | INT-06/07 | ERP único emisor |
| INT-EDI | OpenAS2 / perfiles | canal moderno | INT-08 | MDN no es acuse comercial |
| INT-GIS | Adaptador de mapas | rutas | INT-10 | Tiempo máximo / precarga |
| INT-OPT | Optimizador M4 | rutas | Trabajo versionado | Restricciones de ruta |
| INT-GPS | Adaptador de flota | telemetría | INT-15 | Solo lectura |
| INT-NOTIF | Notificaciones | administración | INT-11 | Vigencia por canal |
| INT-IOT | Captura térmica local | frío | INT-05 | Bloqueo local |
| DAT-OLTP | PostgreSQL / PostGIS | inventario | Repositorios propios | Autoridad por sitio |
| DAT-CDC | Réplica de Talca | continuidad | INT-12 | Lectura, no doble escritor |
| DAT-OLAP | DynamoDB / Glue / S3 / Redshift | analítica | ETL / eventos | Separado de OLTP |
| DAT-OBJ | Objetos POD / DTE | entrega | Hash y objeto | Retención por dominio |
| DAT-CACHE | Redis central | plataforma | Lecturas autorizadas | No reserva stock |
| DAT-LOCAL | Room / cola cifrada | movilidad | UUID / sincronización | Separar fotos y registros sin confirmar |
| SEC-SECRETS | Custodia de claves | seguridad | Identidad de servicio | Rotación segregada |
| SEC-AUDIT | Auditoría inalterable | administración | Evento de decisión | Sujeto, regla y resultado |
| SEC-SIEM | Detección y correlación | seguridad | Alertas | Casos Q/R |
| OBS-COLLECT | OpenTelemetry / ADOT | observabilidad | INT-14 / OTLP | Buffer de 24 horas |
| OBS-LOCAL | Alarmas del sitio | continuidad | Alerta local | No depende de WAN |
| OBS-CENT | CloudWatch | observabilidad | INT-14 | Plataforma única |
| DEV-PIPE | CI/CD y SBOM | plataforma | Artefacto firmado | Promoción por contrato |
| DEV-IAC | Terraform / Ansible | infraestructura | Estado y configuración | Propietario único |
| DEV-MDM | Gestión de terminales | seguridad | Enrolamiento | Política y borrado |

**Correspondencia de actores y permisos del sistema**

La Tabla [A.16](LAFROX-Subdocumento4-Anexos.md#tab:actores-permisos) realiza el catálogo de quince actores del apartado 3.4.2.1 del Subdocumento 3. Cada acción se autoriza por separado sobre el ámbito indicado. Ni el cargo ni el acceso a una consola conceden todos los permisos de un módulo.

<a id="tab:actores-permisos"></a>

**Tabla A.16 — Actores del sistema, interfaces y permisos**

| **Actor** | **Interfaz y módulos** | **Acciones** | **Ámbito y límite** | **Etapa** |
| --- | --- | --- | --- | --- |
| Preventista | App de preventa; M3, lectura M2/M7 | Consultar stock y crédito, capturar y sincronizar pedidos | Su cartera; no reserva offline | 1 |
| Conductor propio | App de reparto; M6/M7/M8 | Entrega, POD, cobro, retorno y envases | Su ruta y turno; no aprueba su descuadre | 1 |
| Conductor externo | App de reparto; M6/M7/M8 | Entrega y rendición propias | Identidad personal ligada a empresa y turno | 1 |
| Preparador | Terminal de bodega; M5, M1/M2 con permiso | Lecturas, faltantes y movimientos autorizados | Sitio, misión y turno; no libera lotes | 1 |
| Cliente del canal tradicional | Portal opcional; M3/M6/M7 | Armar pedidos; ver entregas, documentos y saldo | Solo sus datos; compra asistida sin cuenta | 2 |
| Cliente del canal moderno | Portal y conector EDI; M11/M3 | Pedidos, consultas y mensajes EDI | Su cadena; sesión humana y técnica separadas | 2 |
| Empresa transportista | Portal por representante; M4/M6/M12 | Ver rutas y documentos; confirmar conductor y vehículo | Su empresa; no firma POD | 2; registro por despacho en 1 |
| Proveedor | Portal por representante; M1 | Consultar órdenes y recepciones | Su organización; solo lectura | 2 |
| Jefa de Calidad | Consola de Calidad; M9, acciones M2/M5 | Fijar umbral y duración; liberar, bloquear o retirar | Lote e instalación; decisión exclusiva | 1 |
| Gerente Comercial | Consola comercial; M3/M7/M10/M11 | Reglas, excepciones e indicadores | Política y canal, con historial | 1; canal moderno en 2 |
| Gerente de Finanzas | Consola financiera; M7/M10 | Supervisar rendición y reglas financieras | Tesorería nominada; quien registra no aprueba | 1; costo en 2 |
| Planificador de Rutas | Consola de rutas; M4/M12 | Generar, corregir y aprobar rutas | Motivo auditado; no altera cobros | 1 |
| Jefe de TI | Consola de administración | Identidad, configuración, integraciones y monitoreo | Privilegio temporal con MFA; sin permisos de negocio | 1 |
| Gerente de Operaciones | Consola operacional; M2/M4/M5/M6 | Supervisar despacho y excepciones | Sitio; no omite guía ni Calidad | 1 |
| Jefa de Bodega | Consola de bodega; M1/M2/M5/M8 | Recepción, inventario, FEFO, preparación y retornos | Sitio; ajustes justificados | 1 |

Fuente: elaboración propia a partir del apartado 3.4.2.1 y del Anexo 3.I del Subdocumento 3.

Recepción, despacho, catálogo y Tesorería son funciones asignadas a personas nominadas dentro de estos perfiles. AL-ACT-01 del Anexo 4-V verifica cada fila con una operación permitida y una denegada.

## Anexo 4-O — Registro de decisiones de arquitectura

<a id="anx:O"></a>

El registro reúne las decisiones de arquitectura lógica y física conforme a RT-02.04 (Bases Técnicas Transversales, cap. 2, p. 7). Cada ficha identifica la alternativa descartada, el criterio de selección y la evidencia necesaria para verificar su realización. Los RT de las fichas remiten a las Bases Técnicas Transversales (caps. 2–16, pp. 6–29), salvo RT-10.05 y RT-16.14, precisados por el caso (Bases Técnicas del caso, cap. 15, p. 27).

La Tabla [A.17](LAFROX-Subdocumento4-Anexos.md#tab:adr-estado) fecha cada decisión, como exige RT-02.04. La fecha es la de registro en la versión de la oferta. Todas las decisiones las propone Bastián Trejo, Arquitecto de Solución, y las aprueban el Comité de Arquitectura y la Contraparte Técnica en el hito H2 del Formulario E-25. Ninguna se presenta como aprobada por el CLIENTE. Cada cambio posterior abre una nueva versión de la ficha, con su fecha, su estado (propuesta, aprobada o reemplazada) y el acta del Comité de Arquitectura que la resolvió.

<a id="tab:adr-estado"></a>

**Tabla A.17 — Fecha y estado de las decisiones de arquitectura**

| **ADR** | **Decisión** | **Fecha de registro** | **Estado** |
| --- | --- | --- | --- |
| ADR-01 | Estilo arquitectónico | 5 de octubre de 2026 | Propuesta en la oferta |
| ADR-02 | Conectividad WAN (tres caminos) | 5 de octubre de 2026 | Propuesta en la oferta |
| ADR-03 | Modelo híbrido y topología de sitios | 5 de octubre de 2026 | Propuesta en la oferta |
| ADR-04 | Persistencia políglota | 5 de octubre de 2026 | Propuesta en la oferta |
| ADR-05 | Mensajería asíncrona | 5 de octubre de 2026 | Propuesta en la oferta |
| ADR-06 | Identidad híbrida | 5 de octubre de 2026 | Propuesta en la oferta |
| ADR-07 | Movilidad de terreno | 5 de octubre de 2026 | Propuesta en la oferta |
| ADR-08 | Destino del WMS 2013 | 5 de octubre de 2026 | Propuesta en la oferta |
| ADR-09 | Estrategia de recuperación ante desastres | 5 de octubre de 2026 | Propuesta en la oferta |
| ADR-10 | Plataforma on-premise: virtualización y almacenamiento | 5 de octubre de 2026 | Propuesta en la oferta |
| ADR-11 | Integración B2B/EDI | 5 de octubre de 2026 | Propuesta en la oferta |
| ADR-12 | Capacidad y peak | 5 de octubre de 2026 | Propuesta en la oferta |
| ADR-13 | Puerta de enlace de servicios | 5 de octubre de 2026 | Propuesta en la oferta |
| ADR-14 | Observabilidad | 5 de octubre de 2026 | Propuesta en la oferta |
| ADR-15 | Gestión de secretos | 5 de octubre de 2026 | Propuesta en la oferta |
| ADR-16 | Acceso de personas internas y remotas | 5 de octubre de 2026 | Propuesta en la oferta |
| ADR-17 | Emisión de guías y liberación documental | 5 de octubre de 2026 | Propuesta en la oferta |
| ADR-18 | Protección de datos fuera del sitio | 5 de octubre de 2026 | Propuesta en la oferta |
| ADR-19 | Residencia de datos y regiones | 5 de octubre de 2026 | Propuesta en la oferta |
| ADR-20 | Frontend web | 5 de octubre de 2026 | Propuesta en la oferta |
| ADR-21 | Infraestructura como código y cadena de entrega | 5 de octubre de 2026 | Propuesta en la oferta |
| ADR-22 | Cadena de frío en el borde | 5 de octubre de 2026 | Propuesta en la oferta |

Fuente: elaboración propia a partir de RT-02.04 (Bases Técnicas Transversales, cap. 2, p. 7) y del Formulario E-25 de las Bases Administrativas.

**ADR-01. Estilo arquitectónico**

<a id="sub:adr-01"></a>
**Decisión adoptada.** Laravel 13/PHP 8.5 organiza M1–M12 en un monolito modular con perfiles de ejecución separados.

**Alternativas evaluadas.** Microservicios por módulo multiplican despliegues y operación; un monolito sin límites permite dependencias cruzadas.

**Criterio de selección.** Límites de dominio comprobables con el equipo de operación disponible.

**Consecuencias.** Los módulos comparten artefacto y publican contratos; API, WMS por sitio, erp-sync, shipper, consumidor y trabajadores tienen procesos y permisos propios, y cada uno se despliega y revierte por separado. Los servicios de negocio no conservan estado de sesión en sus procesos.

**Evidencia exigida.** Prueba de dependencias, contratos y promoción de un trabajador sin interrumpir el WMS.

**Requisitos que la sustentan.** RT-02.02, RT-02.04, RT-02.05; Caso, equipo TI.

**ADR-02. Conectividad WAN (tres caminos)**

<a id="sub:adr-02"></a>
**Decisión adoptada.** Talca y Concepción usan fibra y LTE con Starlink fijo como tercer camino en espera caliente: el terminal permanece encendido, el túnel IPsec establecido y BGP con menor preferencia, y solo toma tráfico si fallan ambos caminos terrestres. En los cross-docking Starlink es el camino principal, con LTE de dos proveedores como respaldo.

**Alternativas evaluadas.** Fibra y LTE solos comparten amenazas terrestres; apagar el terminal satelital obliga a adquirir satélites durante varios minutos y a negociar el túnel en plena falla.

**Criterio de selección.** Extracción continua y separación de dominios de falla con conmutación automática.

**Consecuencias.** Al fallar fibra y LTE, el satélite de los CD prioriza DMS/WAL de Talca, salida del broker y outbox, guías hacia el ERP y el SII, identidad y telemetría crítica; la oficina cede capacidad. Talca lo alimenta con UPS y generador y Concepción con UPS. La tarifa plana no aumenta por mantener encendido el terminal.

**Evidencia exigida.** Inyección de fallas por camino y medición de retraso, conmutación y RPO en AL-DR-01.

**Requisitos que la sustentan.** RT-03.10, RT-07.04; Caso, continuidad de sitios.

**ADR-03. Modelo híbrido y topología de sitios**

<a id="sub:adr-03"></a>
**Decisión adoptada.** Cada sitio conserva autoridad sobre sus movimientos con el mismo perfil `wms_only`; N-04/N-05 consolidan stock y reservas en la nube.

**Alternativas evaluadas.** Una autoridad única en Talca crea dependencia WAN; un perfil reducido en cross-docking fragmenta reglas y despliegue.

**Criterio de selección.** Autonomía de 24 horas y una regla de bodega común.

**Consecuencias.** Las transferencias se registran como despacho y recepción, conciliadas por eventos idempotentes en nube.

**Evidencia exigida.** Corte de Talca y de WAN por sitio con operación local y conciliación de transferencias.

**Requisitos que la sustentan.** RT-02.12, RT-03.10; Caso, cinco sitios operativos.

**ADR-04. Persistencia políglota**

<a id="sub:adr-04"></a>
**Decisión adoptada.** PostgreSQL/PostGIS conserva transacciones y geografía; DynamoDB recibe telemetría y S3/Redshift soportan analítica.

**Alternativas evaluadas.** Un almacén único hace competir analítica y despacho; un motor adicional de series aumenta operación.

**Criterio de selección.** Propiedad transaccional por dominio y consultas analíticas desacopladas.

**Consecuencias.** Los contratos de eventos alimentan vistas sin doble escritura de stock; el estado de sesión y de proceso reside en almacenes externos de alta disponibilidad.

**Evidencia exigida.** Consultas espaciales, trazabilidad de propietarios y ensayo de carga sin consultas BI al OLTP.

**Requisitos que la sustentan.** RT-02.05, RT-09.06; Caso, rutas y cadena de frío.

**ADR-05. Mensajería asíncrona**

<a id="sub:adr-05"></a>
**Decisión adoptada.** Outbox y RabbitMQ local publican sobres JSON versionados en SQS FIFO; los trabajos Laravel usan colas separadas.

**Alternativas evaluadas.** Broker solo en nube interrumpe el sitio; Kafka local añade administración desproporcionada.

**Criterio de selección.** Persistencia de 24 horas, orden por grupo e idempotencia de negocio.

**Consecuencias.** Los sitios inician conexiones salientes; solo DMS inicia desde nube hacia VM-02 por IPsec, con regla nominada y auditoría.

**Evidencia exigida.** Ensayo de corte, duplicado, desorden y acuse tras persistir; inspección de reglas de red.

**Requisitos que la sustentan.** RT-02.06, RT-02.07 y RT-03.10.

**ADR-06. Identidad híbrida**

<a id="sub:adr-06"></a>
**Decisión adoptada.** Keycloak es autoridad central y cada sitio verifica manifiestos firmados y PIN local para relevos sin WAN.

**Alternativas evaluadas.** IdP solo nube impide nuevos relevos; directorio maestro local duplica autoridad.

**Criterio de selección.** Acceso personal durante 24 horas sin crear un segundo emisor de identidades.

**Consecuencias.** La caché local es de solo lectura; la revocación remota se aplica al reconectar y los permisos expiran por turno.

**Evidencia exigida.** AL-OFF-01 ensaya dos relevos, dispositivo, vencimiento, reinicio y reconexión.

**Requisitos que la sustentan.** RT-03.10, RT-12.01 y RT-12.11.

**ADR-07. Movilidad de terreno**

<a id="sub:adr-07"></a>
**Decisión adoptada.** Kotlin Android nativo con Room y periféricos Zebra conserva capturas cifradas durante el turno.

**Alternativas evaluadas.** PWA no garantiza integración industrial y offline completo; Flutter añade una capa de validación de periféricos.

**Criterio de selección.** Escaneo, impresión y captura fiables en frío y sin señal.

**Consecuencias.** Se mantiene un artefacto para preventa, reparto y picking con perfiles de permiso; inventario, configuración, actualizaciones y bloqueo de dispositivos se administran remotamente.

**Evidencia exigida.** Ensayo de 14 horas sin señal, sincronización, periféricos y operación a -22 ^°C.

**Requisitos que la sustentan.** RT-03.10, RT-03.18; Caso, parque móvil.

**ADR-08. Destino del WMS 2013**

<a id="sub:adr-08"></a>
**Decisión adoptada.** M1/M2/M5 reemplazan el WMS 2013 por olas y un único escritor por operación.

**Alternativas evaluadas.** Mantener el legado prolonga falta de soporte; cambio simultáneo de todos los sitios eleva el riesgo de corte.

**Criterio de selección.** Funciones FEFO, GS1 y continuidad con reversión controlada.

**Consecuencias.** Cada ola reconcilia operaciones sin confirmar y verifica compatibilidad de esquema antes de cambiar el escritor.

**Evidencia exigida.** Prueba de stock, lote y preparación antes y después de la reversión.

**Requisitos que la sustentan.** Caso, WMS 2013 y continuidad de las bodegas.

**ADR-09. Estrategia de recuperación ante desastres**

<a id="sub:adr-09"></a>
**Decisión adoptada.** Aurora Global Database protege la región; el WMS de Talca se recupera en ECS Fargate sobre su copia en Aurora. ECR replica las imágenes entre regiones y la infraestructura como código crea en la secundaria las colas SQS FIFO, SQS y SNS equivalentes, inicialmente vacías.

**Alternativas evaluadas.** Concepción como DR de Talca consume su capacidad y mantiene amenaza terrestre; restauración fría no alcanza cuatro horas.

**Criterio de selección.** RTO ≤ 4 horas y RPO ≤ 15 minutos con dominios de falla separados.

**Consecuencias.** Talca habilita la copia para escritura al detener DMS; terminales acceden por VPN y el retorno invierte la réplica tras reconstruir VM-02. La conmutación redirige los shippers y `erp-sync` a las colas de la región secundaria sin depender de la primaria.

**Evidencia exigida.** AL-DR-01 recupera Talca en nube y ensaya promoción regional, escritura y retorno.

**Requisitos que la sustentan.** RT-07.04; Caso, continuidad.

**ADR-10. Plataforma on-premise: virtualización y almacenamiento**

<a id="sub:adr-10"></a>
**Decisión adoptada.** Talca usa tres nodos Proxmox de 16 núcleos y 64 GB cada uno, arranque M.2 en RAID 1, dos NVMe Ceph por nodo sin RAID y doble fuente; Ceph usa réplica `size`=3, `min_size`=2 y tres monitores. El NAS tiene doble fuente, RAID 6 y WORM.

**Alternativas evaluadas.** Ceph sobre RAID 10 duplica protección y reduce capacidad; un almacenamiento sin quórum pierde tolerancia a nodo.

**Criterio de selección.** Capacidad y quórum N+1 con demanda del Anexo 4-W.

**Consecuencias.** Se reservan recursos de OSD y monitor; seis OSD ofrecen cerca de 1,92 TB útiles y unos 1,5 TB al 80% de llenado. Frente a RT-03.14, el nivel declarado es Ceph sin RAID por hardware con réplica de tres copias, que tolera la falla de un disco y de un nodo. Concepción usa RAID 10 y doble fuente. E-01 usa dos SSD en RAID 1 por software, que tolera la falla de un disco con holgura para los 50 GB requeridos; RAID 5 o RAID 10 exigirían tres o cuatro discos que el mini-PC industrial no aloja. E-01 y sus switches tienen alimentación redundante.

**Evidencia exigida.** Prueba de pérdida de nodo, reconstrucción, latencia y carga de cientos de IOPS a 3× frente a decenas de miles de IOPS de NVMe.

**Requisitos que la sustentan.** RT-07.04, RT-08.03, RT-08.04; Anexo 4-W.

**ADR-11. Integración B2B/EDI**

<a id="sub:adr-11"></a>
**Decisión adoptada.** M11 traduce EANCOM/GS1 XML y EPCIS por cadena; OpenAS2 gestiona firma, cifrado y MDN; ERP se alcanza por ACL.

**Alternativas evaluadas.** Punto a punto por cadena duplica adaptadores; delegar EDI al ERP expone su frontera.

**Criterio de selección.** Contratos GS1 y aislamiento del emisor tributario.

**Consecuencias.** Los perfiles de cadena se versionan y las excepciones quedan trazables.

**Evidencia exigida.** Interoperabilidad por cadena con TLS 1.3, certificados, MDN y rechazo comercial.

**Requisitos que la sustentan.** RT-11.08, RF-12.03, RF-12.06; Caso, canal moderno.

**ADR-12. Capacidad y peak**

<a id="sub:adr-12"></a>
**Decisión adoptada.** Aurora mantiene capacidad fija, sin escalado automático, dimensionada para la cota extrema de la API más la cuota del canal tradicional, 111,70 solicitudes/s. Fargate escala la API de 2 a 4 tareas en los casos base y a 7 en la sensibilidad de 91,70 solicitudes/s, bajo el techo de 8, que también cubre esa cuota. El consumidor y los trabajos de notificaciones y EDI escalan de 2 a 4 tareas por perfil.

**Alternativas evaluadas.** Cambiar la clase de Aurora en septiembre introduce intervención en congelamiento; un proceso único comparte saturación entre perfiles.

**Criterio de selección.** Capacidad probada antes del peak y mamparos de concurrencia.

**Consecuencias.** Los perfiles tienen colas, conexiones y cuotas separadas; no se interviene del 1 al 25 de septiembre.

**Evidencia exigida.** Carga de 3× y sensibilidad de 91,70 solicitudes/s con medición de PHP-FPM, tareas API, conexiones, bloqueo de base y edad de colas.

**Requisitos que la sustentan.** RT-09.03, RT-09.06; Caso, peak de septiembre.

**ADR-13. Puerta de enlace de servicios**

<a id="sub:adr-13"></a>
**Decisión adoptada.** API Gateway REST publica entradas pública y privada con autorizador JWT Keycloak y VPC Link hacia ALB. La puerta de API local A-01 de cada sitio valida esquema, tasa, UUID y permisos, y registra auditoría sin WAN.

**Alternativas evaluadas.** Gateway propio agrega operación; HTTP API no cubre la validación y entrada privada requeridas.

**Criterio de selección.** Identidad y validación en puerta, con autorización de recurso en Laravel.

**Consecuencias.** El origen público directo y la API privada fuera del endpoint autorizado se deniegan; la puerta local conserva los controles de entrada durante el aislamiento.

**Evidencia exigida.** Prueba de JWT, cuota, esquema, origen y endpoint privado, más validación local de tasa, UUID, permisos y auditoría durante un corte WAN.

**Requisitos que la sustentan.** RT-11.07 y RT-11.11.

**ADR-14. Observabilidad**

<a id="sub:adr-14"></a>
**Decisión adoptada.** OpenTelemetry y ADOT exportan métricas, registros y trazas a CloudWatch con buffer local de 24 horas.

**Alternativas evaluadas.** Dos plataformas aumentan soporte; tablero solo remoto deja sin alarma al sitio aislado.

**Criterio de selección.** Correlación de extremo a extremo y una plataforma operable por el equipo.

**Consecuencias.** Las alarmas locales actúan durante el corte y el UUID se conserva al reenviar telemetría.

**Evidencia exigida.** Reconstrucción de una transacción tras corte y prueba de capacidad del buffer.

**Requisitos que la sustentan.** RT-03.16; Art. 16.4.

**ADR-15. Gestión de secretos**

<a id="sub:adr-15"></a>
**Decisión adoptada.** Secrets Manager custodia credenciales y certificados rotables; Parameter Store conserva configuración no sensible.

**Alternativas evaluadas.** Vault autoadministrado añade desellado y operación; archivos locales carecen de custodia central.

**Criterio de selección.** Rotación auditable con separación de funciones.

**Consecuencias.** KMS cifra secretos y una cuenta de emergencia queda bajo doble custodia fuera de línea.

**Evidencia exigida.** Prueba de rotación, denegación de acceso y uso auditado de contingencia.

**Requisitos que la sustentan.** RT-04.09, RT-11.09 y RT-12.13.

**ADR-16. Acceso de personas internas y remotas**

<a id="sub:adr-16"></a>
**Decisión adoptada.** Verified Access protege consolas con Keycloak MFA y postura del dispositivo.

**Alternativas evaluadas.** Client VPN concede acceso de red más amplio; VPN de sitio no cubre personas remotas.

**Criterio de selección.** Acceso por aplicación condicionado a identidad y postura.

**Consecuencias.** La consola y la API privada permanecen fuera de internet público.

**Evidencia exigida.** Prueba desde oficina y remoto con postura válida e inválida.

**Requisitos que la sustentan.** RT-03.22, RT-11.01, RT-12.03.

**ADR-17. Emisión de guías y liberación documental**

<a id="sub:adr-17"></a>
**Decisión adoptada.** Dos procesos `erp-sync` en VM-04 junto a la ACL consumen RabbitMQ de Talca y, por salida, la cola FIFO de solicitudes al ERP; las respuestas vuelven a cada sitio por su cola FIFO; el ERP emite ante SII por tres caminos.

**Alternativas evaluadas.** Trabajador solo en nube pierde la solicitud local sin WAN; emisión sustituta en Laravel duplica autoridad tributaria.

**Criterio de selección.** Guía válida antes de liberar cada camión sin conexión entrante desde nube.

**Consecuencias.** La guía se preemite al cerrar carga nocturna; cambiar carga invalida la guía y exige nueva emisión, que requiere un camino de Talca y, fuera de Talca, también uno del sitio. Si no hay camino hasta el ERP, el camión sale solo con la carga amparada por su guía vigente y el ajuste pasa a la ruta siguiente. Una guía ya anulada no se reutiliza.

**Evidencia exigida.** AL-DTE-01 ensaya 96 salidas, caída de fibra y LTE, cambio de carga, folio y acuse.

**Requisitos que la sustentan.** RT-10.05 y RT-16.14 del caso (Bases Técnicas del caso, cap. 15, p. 27); RF-05.06; Caso, 96 camiones.

**ADR-18. Protección de datos fuera del sitio**

<a id="sub:adr-18"></a>
**Decisión adoptada.** La extracción continua de DMS/WAL y outbox por fibra, LTE y satélite sostiene RPO ≤ 15 minutos en los CD.

**Alternativas evaluadas.** Retención solo en WAL o RabbitMQ local no protege la pérdida del sitio; dos caminos terrestres comparten falla.

**Criterio de selección.** Tres medios con dominios de falla distintos y confirmación durable externa.

**Consecuencias.** Se alerta a los 5 y 15 minutos; la autonomía local permanece y el límite residual se justifica en 4.3.2.

**Evidencia exigida.** AL-DR-01 mide puntos consistentes y recupera el WMS de Talca en nube con los tres caminos ensayados.

**Requisitos que la sustentan.** RT-07.04 y RT-03.10.

**ADR-19. Residencia de datos y regiones**

<a id="sub:adr-19"></a>
**Decisión adoptada.** La región primaria es sa-east-1 y la secundaria us-east-1, ambas transferencias internacionales sujetas a aprobación del CLIENTE.

**Alternativas evaluadas.** Restringir la propuesta a una sola región impide recuperación regional; replicar todas las categorías excede minimización.

**Criterio de selección.** Continuidad con base de licitud, minimización y control contractual.

**Consecuencias.** AWS actúa como encargado bajo contrato con cláusulas tipo para la Ley N.° 21.719 (Ley N.° 21.719, 2024); el CLIENTE administra KMS, cifra datos en reposo y tránsito, audita accesos, excluye la geolocalización de personas de la réplica secundaria y copia la analítica en forma diferida sin las posiciones de flota. La declaración de ambas regiones, la base de licitud y los resguardos se someten a la aprobación del CLIENTE como hito de la Etapa 1. us-east-1 ofrece todos los servicios de recuperación del diseño.

**Evidencia exigida.** Contrato de encargo, registro de tratamiento, aprobación de residencia y prueba de exclusiones y recuperación.

**Requisitos que la sustentan.** Art. 23 de las Bases Administrativas (art. 23, p. 17); Ley N.° 21.719; RT-07.04.

**ADR-20. Frontend web**

<a id="sub:adr-20"></a>
**Decisión adoptada.** Angular con TypeScript y Tailwind sirve portales y consolas con contratos publicados. El Portal de Clientes se publica además como aplicación web progresiva instalable, que es el perfil de autoatención con operación desconectada exigido por el caso.

**Alternativas evaluadas.** React ofrece composición flexible pero exige elegir más piezas de estado y navegación; Vue exige otra cadena de componentes y soporte. Un cuarto perfil del cliente en la aplicación Kotlin exigiría enrolar teléfonos de clientes en el MDM corporativo y mezclar su identidad con la de los turnos de trabajadores.

**Criterio de selección.** Uniformidad de componentes, contratos y mantenimiento del equipo, con separación entre las herramientas de trabajadores y de clientes.

**Consecuencias.** El portal usa OIDC y autorización por recurso; se actualizan dependencias durante el contrato. Sin señal, el portal instalado solo consulta lo descargado y arma el pedido; la confirmación espera la recepción en M3. El canal es opcional y no altera la atención por preventista.

**Evidencia exigida.** Prueba de accesibilidad, contratos, autenticación y promoción del mismo artefacto, más AL-CLI-01 del Anexo 4-M.

**Requisitos que la sustentan.** RT-16.30 y RT-17.01 del caso (Bases Técnicas del caso, cap. 15, p. 27); restricción 5 del caso.

**ADR-21. Infraestructura como código y cadena de entrega**

<a id="sub:adr-21"></a>
**Decisión adoptada.** Terraform y Ansible administran infraestructura y hosts; GitLab CI y CodeBuild construyen y promueven artefactos firmados.

**Alternativas evaluadas.** CloudFormation/CDK exige otra cadena para los hosts locales y aumenta el esfuerzo de portabilidad; CodePipeline/GitHub Actions dispersa las puertas del repositorio GitLab.

**Criterio de selección.** Propiedad única de recursos, construcción reproducible y trazabilidad de aprobación.

**Consecuencias.** Estados por ambiente, revisión de planes y puertas de seguridad preceden la promoción.

**Evidencia exigida.** Recreación de ambiente, plan sin deriva, SBOM, firma y reversión de despliegue.

**Requisitos que la sustentan.** RT-04.03–04.05.

**ADR-22. Cadena de frío en el borde**

<a id="sub:adr-22"></a>
**Decisión adoptada.** Greengrass en gateways industriales lee Modbus, bloquea localmente el despacho ante una excursión crítica y sostenida y conserva lecturas durante 24 horas.

**Alternativas evaluadas.** Lectura directa a nube depende de WAN; lectura en PLC mezcla control industrial con reglas de despacho y dificulta auditoría.

**Criterio de selección.** Bloqueo en menos de cinco segundos y evidencia durante aislamiento.

**Consecuencias.** Dos gateways cubren cámaras de Talca y uno Concepción; el módulo M9 mantiene la decisión de liberación.

**Evidencia exigida.** Inyección de excursión térmica, corte WAN, reinicio y reconciliación de lecturas.

**Requisitos que la sustentan.** RT-03.10; Caso, cadena de frío.

## Anexo 4-P — Tecnologías, soporte y actualización

<a id="anx:P"></a>

El inventario distingue versión de referencia de una imagen exacta de producción. Cada liberación fija parches, hashes y compatibilidad en los archivos de bloqueo y SBOM; las versiones futuras se aprueban mediante pruebas antes de promoverse. La hoja de ruta cubre los 56 meses mediante actualizaciones, no suponiendo soporte de una misma versión durante todo el contrato (Bases Técnicas Transversales, numeral 1.6, pp. 4–5).

<a id="tab:soporte-logico"></a>

**Tabla A.18 — Ciclo de soporte del núcleo lógico**

| **Producto** | **Referencia** | **Fin de soporte publicado** | **Plan de actualización** |
| --- | --- | --- | --- |
| Laravel | 13.x | Seguridad: 17-03-2028. | Evaluación anual; migrar al menos 6 meses antes del fin. |
| PHP | 8.5.x | Seguridad: 31-12-2029. | Actualización compatible antes del fin; ensayo de APIs y colas. |
| PostgreSQL | 16.x | 09-11-2028. | Ensayo de migración mayor y reversión 6 meses antes. |
| Angular | 22.x | LTS: junio de 2028, fecha orientativa del fabricante. | Revisión semestral y actualización anual por compatibilidad. |
| TypeScript | 6.0.x | Sin fecha contractual independiente. | Versión compatible con Angular; archivo de bloqueo y pruebas. |
| RabbitMQ | 4.3.x | Comunidad: 31-01-2027. | Actualizar antes de esa fecha a rama soportada; no se presume licencia comercial. |

Fuente: Laravel (2026), PHP (2026), PostgreSQL (2026), Angular (2026a, 2026b) y RabbitMQ (2026). Fechas consultadas el 30-09-2026; la de RabbitMQ, el 07-10-2026.

Laravel, PHP, PostgreSQL y Angular tienen horizontes inferiores al contrato: el responsable de Desarrollo registra cada trimestre su soporte y planifica la sustitución antes de vencimiento. RabbitMQ requiere una actualización temprana antes del fin comunitario de la rama de referencia, aun durante desarrollo. No se atribuye al CLIENTE un contrato de soporte comercial no contratado.

<a id="tab:inventario-software"></a>

**Tabla A.19 — Inventario complementario y control de vigencia**

| **Componente** | **Línea base lógica** | **Control durante 56 meses** |
| --- | --- | --- |
| PostGIS | 3.x compatible con PostgreSQL 16. | Compatibilidad y fin de soporte de la distribución registrados antes de liberar. |
| Kotlin/Android | Rama estable compatible con parque Zebra. | Matriz OS, SDK y periféricos por modelo; MDM impide OS fuera de soporte. |
| Room/SQLite | Versión estable de AndroidX Room y SQLite incorporada. | Parches fijados por Gradle; migración de cola sin perder registros sin confirmar. |
| Keycloak | 26.x, parche soportado al liberar. | Revisión trimestral del ciclo oficial; migrar junto al adaptador OIDC. |
| Tailwind/Node/RxJS | Versiones compatibles con Angular y su toolchain. | Archivo de bloqueo y matriz de compatibilidad; Node solo construye el cliente. |
| Composer/PHPUnit/PHPStan/Pint | Versiones compatibles con PHP 8.5 y Laravel 13. | Composer lock, análisis de licencia, audit y regresión; no entran herramientas de prueba al runtime. |
| php-amqplib/AWS SDK/swagger-php | Bibliotecas mantenidas compatibles con PHP 8.5. | Contrato AMQP, sobre JSON y generación OpenAPI bloquean cambios incompatibles. |
| OpenAS2/JVM | Rama soportada compatible con perfiles de las cadenas. | Certificados, licencia, runtime Java y pruebas MDN registrados antes de habilitar INT-08. |
| OpenTelemetry/ADOT | Versiones estables de SDK y colector. | Ensayo de recepción OTLP, correlación, buffer y exportación tras corte. |
| Terraform/Ansible | Versiones estables y providers fijados. | Terraform gobierna recursos; Ansible configura hosts. AWS CDK no gobierna los mismos recursos. |
| Servicios AWS | API/engine gestionados declarados por servicio. | Avisos de retiro trimestrales; prueba de adaptación. Aurora conserva versión de engine y fecha de soporte del proveedor. |
| MDM/Android Enterprise | Servicio y plan compatibles con el parque. | Contrato de soporte y actualización de dispositivos durante todo el período. |

Fuente: decisiones de arquitectura lógica y política de configuración de la propuesta.

El fin de soporte no publicado se registra como *no publicado*, con responsable y frecuencia de revisión; no significa soporte indefinido. Antes de aprobar una dependencia se verifica licencia, mantenimiento, vulnerabilidades y alternativa de sustitución (RT-11.26). La ficha de liberación identifica versión exacta, EOL conocido o política aplicable, prueba, rollback y responsable. La aceptación rechaza una imagen fuera de soporte.

Las alternativas se evalúan por operación offline, integración industrial, transacciones, geografía, carga del equipo y reversibilidad. PostgreSQL/PostGIS se selecciona frente a MariaDB por el dominio espacial; Angular se conserva frente a cambiar la plataforma web por sus contratos y componentes existentes; Kotlin se selecciona frente a una capa móvil adicional por validación del parque; Keycloak mantiene identidad propia frente a delegar el dominio de autorizaciones a un IdP propietario. Las herramientas de construcción no cambian esos contratos. Los criterios concretos se verifican en ADR-04/06/07/20/21 y el Anexo 4-T.

**Implementación compatible del backend**

La tabla relaciona cada capacidad del backend con su implementación en Laravel/PHP y con la comprobación que acredita su equivalencia.

<a id="tab:mapeo-laravel"></a>

**Tabla A.20 — Implementación lógica del backend Laravel**

| **Capacidad** | **Implementación Laravel/PHP** | **Comprobación** |
| --- | --- | --- |
| APIs y módulos | Rutas y controladores Laravel; servicios por contexto PSR-4. | Contratos OpenAPI y límites de módulo. |
| Persistencia y geografía | PDO/Query Builder y SQL PostGIS parametrizado; migraciones Laravel basales. | Datos, índices y consultas espaciales equivalentes. |
| Tareas y planificación | Consumidor PHP de JSON en SQS FIFO; trabajos Laravel en colas separadas y planificador único. | Orden por grupo, reintentos y tareas únicas. |
| Cola local y shipper | Adaptador AMQP con `php-amqplib` y sobre JSON. | Corte de 24 h, confirmación y drenaje sin pérdida. |
| Identidad y administración | Guard OIDC, políticas por recurso y portal Angular. | Permisos, baja y relevos de turno. |
| Contratos, pruebas y trazas | `swagger-php`, AsyncAPI, PHPUnit y OpenTelemetry PHP. | Paridad de API, eventos y correlación. |

## Anexo 4-Q — Modelado de amenazas lógicas

<a id="anx:Q"></a>

STRIDE se aplica por módulo, componente transversal e integración externa (RT-11.02). S representa suplantación; T, alteración; R, repudio; I, divulgación; D, denegación; E, elevación de privilegios. Cada escenario tiene una prueba negativa y un dueño; el registro se reevalúa al cambiar un contrato o límite de confianza. Esta matriz registra amenazas de diseño, no resultados de pentesting.

<a id="tab:amenazas-modulos"></a>

**Tabla A.21 — Amenazas de los doce módulos**

| **Elemento** | **Amenaza** | **Control y prueba** | **Dueño** |
| --- | --- | --- | --- |
| M1 | T: lote o recepción falsa. | GS1, cuarentena y evidencia; rechazar lote sin origen. | Recepción/Calidad |
| M2 | T/D: reserva duplicada. | Escritor único, UUID y bloqueo por agregado; doble compromiso. | Inventario |
| M3 | S/T: pedido con identidad ajena. | Turno, dispositivo y firma; token inválido y reenvío. | Comercial/Seguridad |
| M4 | T: ruta con restricción omitida. | Restricción versionada, aprobación y motivo; ruta incompatible. | Operaciones |
| M5 | E: liberar carga retenida. | Política por recurso y documento vigente; supervisor sin permiso. | Bodega/Calidad |
| M6 | R/T: POD alterado. | Hash, autor, hora y vínculo guía; objeto con hash distinto. | Reparto |
| M7 | E/R: aprobar cobro propio. | Segregación y conciliación; mismo autor registrador/aprobador. | Tesorería |
| M8 | T: devolución o saldo ficticio. | Causal, lote, evidencia y disputa; devolución repetida. | Bodega/Tesorería |
| M9 | T/E: ocultar excursión. | Alarma local y liberación exclusiva de Calidad; muestra alterada. | Calidad |
| M10 | I: exponer crédito por tablero. | Modelo autorizado, filtros y auditoría; consulta de otro cliente. | Datos/Seguridad |
| M11 | T/D: EDI repetido o inválido. | Firma, equivalencia y UUID; repetición/rechazo sin crear pedido. | Canal moderno |
| M12 | I: uso de GPS fuera de finalidad. | Rol, ruta, retención y consulta auditada; usuario sin asignación. | Flota/Seguridad |

Fuente: elaboración propia sobre límites de M1–M12 y RT-11.02.

<a id="tab:amenazas-fronteras"></a>

**Tabla A.22 — Amenazas en fronteras y terceros**

| **Elemento** | **Amenaza** | **Control y evidencia de aceptación** |
| --- | --- | --- |
| INT-06/07, ACL y ERP | T/R: documento duplicado o incierto. | Clave por carga, consulta antes de reintento y estado explícito; AL-DTE-01. |
| INT-08/OpenAS2 | S/T: contraparte falsa o mensaje cambiado. | Certificado registrado, firma y MDN; certificados desconocidos y hash alterado. |
| INT-09/POS | T/R: doble cobro por timeout. | Clave de cargo, consulta y conciliación; respuesta tardía después de alternativa. |
| INT-10/GIS/optimizador | D/T: cuotas o ruta manipulada. | Timeout, límites, ruta aprobada y comprobación de restricciones. |
| INT-11/avisos | I/T: revelar pedido o avisar tarde. | Consentimiento/canal, mínimo dato y vigencia; aviso vencido. |
| INT-15/GPS | I/T: posición falsa o histórica. | Cursor, fecha y acceso de solo lectura; muestra fuera de secuencia. |
| UI-MOV/UI-HHT/DAT-LOCAL | I/S: pérdida o préstamo de terminal. | MDM, cifrado, PIN y turno; pérdida y dispositivo no enrolado. |
| BOR-PUB/GW-CENT/AUTH-CENT | S/D: abuso o token ajeno. | WAF, cuota, JWT y política; firma/audiencia inválida y ráfaga. |
| GW-LOCAL/AUTH-LOCAL/WMS-SITE | E/T: manifiesto alterado o reloj movido. | Firma, reloj controlado y permisos; AL-OFF-01. |
| INT-BROKER/SHIPPER/CONSUMER/JOBS | T/D: evento repetido o tóxico. | Sobre versionado, outbox, DLQ y deduplicación; corte en cada acuse. |
| INT-SCHED/INT-IOT | D/T: tarea duplicada o sensor perdido. | Autoridad única y frescura de lectura; doble líder y ausencia de sensor. |
| DAT-OLTP/CDC/OLAP/OBJ/CACHE | I/T: lectura o escritura no autorizada. | Dueño, cifrado, cuenta mínima y hash; consulta directa y objeto cambiado. |
| SEC-SECRETS/AUDIT/SIEM | I/R: clave expuesta o evidencia borrada. | Custodia separada, Object Lock y alertas; administración sin descifrado. |
| OBS-COLLECT/LOCAL/CENT | D/R: buffer lleno o traza faltante. | Cuota, alarma y prioridad de auditoría; corte con saturación. |
| DEV-PIPE/IAC/MDM/UI-WEB/BOR-B2B | S/E: artefacto o acceso de gestión ajeno. | Firma, SBOM, aprobación y MFA; imagen sin procedencia y rol excesivo. |

Fuente: catálogo INT-01–15, inventario del Anexo 4-N y RT-11.02. Seguridad mantiene el registro; cada dueño ejecuta su escenario con Calidad.

Las integraciones internas heredan los controles de productor y consumidor: INT-01/02, identidad y UUID; INT-03/04, sitio y secuencia; INT-05, sensor y frescura; INT-12, cuenta CDC de lectura; INT-13, manifiesto firmado; INT-14, integridad y capacidad del buffer. Toda excepción conserva escenario, consecuencia, responsable, tratamiento y criterio de cierre.

## Anexo 4-R — Controles de seguridad y evidencia

<a id="anx:R"></a>

Esta matriz vincula controles de ISO/IEC 27001:2022, Anexo A, y su guía ISO/IEC 27002:2022 con la implementación lógica y la evidencia prevista por RT-11.05 (Bases Técnicas Transversales, cap. 11, p. 23). La numeración es un identificador de control, no una declaración de certificación. El sistema de gestión conserva además evaluación de riesgos y declaración de aplicabilidad. La política Zero Trust se fundamenta en NIST SP 800-207 (NIST, 2020).

<a id="tab:controles-seguridad"></a>

**Tabla A.23 — Controles aplicados a la vista lógica**

| **Control** | **Requisito** | **Implementación concreta** | **Evidencia** |
| --- | --- | --- | --- |
| 5.9 | RT-11.23 | Inventario de componentes y SBOM CycloneDX/SPDX por liberación. | SBOM y hashes del artefacto. |
| 5.12/5.13 | RT-11.03 | Clasificación aplicada a API, evento, objeto y copia local. | Matriz y pruebas de exportación. |
| 5.15/5.18 | RT-12.05/09/10 | Roles y atributos por recurso; altas y bajas trazadas. | Permisos y pruebas negativas. |
| 5.16/5.17 | RT-12.01/11 | Keycloak, PIN personal y credencial de turno firmada. | AL-OFF-01 y baja conectada. |
| 5.19/5.20 | RT-05.21 | SLA, ventanas, datos y respuesta de cada contraparte. | Fichas G/H y acuerdos. |
| 5.23 | RT-11.06 | Matriz de responsabilidad compartida por servicio (ISO/IEC 27017); datos personales cifrados con claves KMS del CLIENTE y registro de tratamiento (ISO/IEC 27018). | Matriz aprobada por servicio y registro de tratamiento. |
| 5.24/5.26 | RT-11.15/18/19 | Clasificación, correlación y comunicación de incidentes. | Ejercicio y bitácora; aviso crítico 2 h, incidente 24 h. |
| 5.30 | RT-10.03/04 | Funciones offline, dependencia y recuperación consistente. | Anexo 4-M y pruebas de recuperación de 4.3.2. |
| 5.34 | RT-05.07/16.09 | Retención y consulta de GPS/crédito registradas. | Consulta autorizada y eliminación. |
| 8.2 | RT-12.05/06 | Elevación temporal y segregación de Tesorería/Calidad. | Sesión y aprobación nominadas. |
| 8.5 | RT-12.03/07/08 | MFA, token corto, refresh rotatorio y expiración. | Pruebas de firma y sesión. |
| 8.7/8.8 | RT-11.04/16 | EDR y gestión de vulnerabilidades en runtime y terminal. | Escaneo y remediación 7/15/30 días. |
| 8.9 | RT-04.04/08 | Configuración por ambiente y cambios trazados. | Diferencia de configuración y reversión. |
| 8.10/8.11 | RT-05.07/11.25 | Eliminación verificable y anonimización fuera de producción. | Borrado y conjunto de prueba. |
| 8.13/8.14 | RT-07.04 | Estado durable y protección externa por dominio de falla. | AL-DR-01; no basta cola local. |
| 8.15/8.16 | RT-11.14/15 | Auditoría inalterable y detección específica del negocio. | UUID enlazado con regla SIEM. |
| 8.20/8.22 | RT-11.07/13 | Borde, superficie B2B separada y puerta local privada. | Intento directo al origen denegado. |
| 8.24 | RT-11.08/09/10 | Cifrado de reposo, campo y tránsito; claves separadas. | Admin sin texto claro y rotación. |
| 8.25/8.28 | RT-11.22/24 | SAST/SCA/DAST, firma y procedencia SLSA 3. | Pipeline bloqueado por hallazgo. |
| 8.29/8.31/8.32 | RT-04.02–04.05; RT-11.27 | Pruebas, ambientes segregados y promoción aprobada. | Commit, ensayo y despliegue correlacionados. |

Fuente: elaboración propia a partir de ISO (2022b, 2022c), RT de los capítulos 4, 5, 7, 10, 11, 12 y 16 (Bases Técnicas Transversales, caps. 4–16, pp. 10–29), y contratos lógicos. Seguridad verifica aplicabilidad con el responsable del sistema de gestión.

La arquitectura impone HSTS en los portales HTTPS, TLS 1.3 en interfaces compatibles y rechazo de TLS 1.0/1.1. Un tercero con limitación de protocolo exige excepción documentada y tratamiento, no una reducción silenciosa del control. Entre sistemas se utiliza mTLS u OAuth con credenciales de cliente; nunca una clave estática en la URL. El catálogo público no muestra precios, conforme al caso. OWASP ASVS nivel 2 y API Security Top 10 orientan las pruebas de aplicación. La superficie exacta y la implantación de EDR/SIEM se realizan en la vista física; los permisos, eventos y pruebas permanecen definidos aquí.

## Anexo 4-S — Puntos de vista y correspondencias

<a id="anx:S"></a>

La entidad de interés es la plataforma logística Puelche y sus fronteras con ERP, personas y servicios de terceros. La descripción cubre toma de pedido, reserva, preparación, salida, entrega, rendición, trazabilidad y análisis; su horizonte incluye dos etapas y 36 meses de operación. Cada punto de vista fija preocupación, interesados, modelos y comprobación, conforme a RT-02.03 e ISO/IEC/IEEE 42010:2022 (ISO, 2022a).

<a id="tab:puntos-vista"></a>

**Tabla A.24 — Interesados y modelos de las cinco vistas**

| **Vista** | **Interesados** | **Preocupación** | **Modelos y evidencia** |
| --- | --- | --- | --- |
| Lógica | TI y responsables de módulo. | Dueños, límites e interfaces sin dependencia de tablas ajenas. | Vista general, capas y anexos 4-D, F, G, H y N. |
| Procesos | Operaciones, conductores y Tesorería. | Una captura avanza a confirmación, salida y rendición con estados claros. | Secuencias del pedido con y sin conexión (apartado 4.1.3.5); anexos 4-A y 4-U. |
| Despliegue | TI, Infraestructura y Operaciones. | Cada función dispone de realización y contingencia por sitio. | Anexo 4-N y correspondencia con 4.2–4.3. |
| Datos | Calidad, Datos y Comercial. | Lote, reservas, acuses y evidencias tienen dueño y retención. | Modelo conceptual (apartado 4.1.5) y Anexo 4-K. |
| Seguridad | Seguridad, Calidad y CLIENTE. | Nadie libera, cobra o consulta sin permiso y evidencia. | Límites de confianza, anexos 4-Q y 4-R y prueba AL-OFF-01. |

Fuente: elaboración propia a partir de RT-02.03 (Bases Técnicas Transversales, cap. 2, p. 7) y de ISO (2022a).

CR-01 exige que cada capacidad del esquema y explicación de solución tenga uno o más componentes N con nombre idéntico y que todo componente tenga capacidad de origen. CR-02 exige productor único, consumidores registrados y contrato por evento; una arista sin contrato se rechaza. CR-03 exige que cada escritura tenga dueño de datos, clave idempotente y auditoría. CR-04 exige para cada función desconectada persistencia, permisos, límite de autonomía y reconciliación. CR-05 vincula componente lógico a realización física exacta; no se cuenta una referencia genérica. CR-06 exige que cada amenaza tenga control y prueba, y que cada decisión ADR tenga consecuencia verificable.

Arquitectura mantiene un registro de diferencias con componente, regla infringida, requisito, dueño, decisión y evidencia de cierre. La comprobación se ejecuta al cambiar un módulo, contrato, tecnología o etapa. La Tabla 8 del apartado 4.2.2 verifica CR-01/05; pruebas de contrato, CR-02/03; AL-OFF-01, CR-04; y la revisión de Q/R/O, CR-06.

## Anexo 4-T — Desempeño y aceptación lógica

<a id="anx:T"></a>

Los umbrales se miden sobre la operación percibida y confirmada, no sobre una llamada aislada. La copia de consulta puede responder inmediatamente como información fechada; no confirma stock o crédito. El timeout del adaptador es un límite de protección independiente del tiempo visible al usuario (Bases Técnicas del caso, cap. 15, p. 26; Bases Técnicas Transversales, cap. 9, pp. 21–22).

<a id="tab:aceptacion-desempeno"></a>

**Tabla A.25 — Objetivos y escenarios de desempeño**

| **Operación** | **Objetivo** | **Carga y comprobación** |
| --- | --- | --- |
| Confirmar línea picking | p95 ≤ 1 s. | Terminal, puerta local, M5/M2 y base; 186 terminales concurrentes del turno nocturno. |
| Registrar entrega | p95 ≤ 2 s. | Persistencia local durable, POD y UUID; el envío de foto no bloquea la captura. |
| Registrar línea preventa | p95 ≤ 1,5 s. | Captura cifrada, persistencia y estado; no exige reserva central offline. |
| Confirmar reserva con enlace | p95 ≤ 10 s. | Viaje nube–sitio–nube por la cola de coordinación; AL-STOCK-01. |
| Consultar stock/crédito | p95 ≤ 2 s. | API con enlace; copia fechada inmediata durante degradación. |
| Reconciliar reparto | ≤ 10 min por turno. | 14 h de captura, mensajes y objetos; sin pérdidas ni duplicados. |
| Reconciliar CD | ≤ 2 h tras corte. | 24 h locales, relevos y cargas por sitio; ocupación máxima y drenaje. |
| Planificar ruta | < 20 min. | Flota, destinos, capacidad, frío y ventanas; restricciones verificadas. |
| Liberar despachos | 96 salidas 05:30–07:00. | Guías por destino/carga y cambios tardíos; AL-DTE-01. |

Fuente: elaboración propia a partir de las Bases Técnicas del caso (caps. 14–15, pp. 24–28, y cap. 18, p. 34). Las pruebas son compromisos de ejecución, no resultados obtenidos.

La prueba RT-09.06 usa una carga total de 1,5 × 14,66 = 21,99 TPS, distribuida por perfil horario y sitio; las tasas por integración se detallan en el Anexo 4-W del Subdocumento 4. El crecimiento de RT-09.03 ensaya tres veces la volumetría inicial sin rediseñar contratos ni identificadores.

Las reservas se serializan por agregado para evitar doble compromiso; los perfiles ERP, reconciliación, EDI y reportes tienen mamparos de concurrencia y colas independientes. Bajo sobrecarga, lectura degrada a copia fechada, escritura permanece sin confirmar y objetos se transfieren por reanudación. El usuario recibe estado y causal; nunca se descarta una operación confirmada para recuperar velocidad.

AL-PERF-01 incrementa carga en escalones hasta saturación y mide p50/p95/p99, errores, bloqueos de base, edad de cola, WAL, buffer y tiempo de recuperación. El ensayo detiene consumidores no críticos y comprueba que despacho conserva su capacidad reservada. Si el ERP limita primero, se mejora continuidad y presupuesto de emisión, no se presume que más Laravel lo corrige. El informe conserva versión, datos, distribución horaria, curvas, punto de quiebre y operaciones sin confirmar. Los umbrales de autoscaling y límites de infraestructura se trazan al componente físico; su costo permanece en la oferta económica.

## Anexo 4-U — Prueba de entrega, guía y acuses

<a id="anx:U"></a>

La solución propone tres registros separados: documento tributario emitido por ERP, evidencia operacional capturada por M6 y acuse recibido por el canal del destinatario. El SII exige portar la representación gráfica o impresa del DTE durante traslado; su acuse técnico no acredita por sí solo recepción de mercaderías (Servicio de Impuestos Internos [SII], s. f.-a). La evidencia móvil tampoco se transforma automáticamente en el recibo legal del destinatario.

**Mecanismo de recepción propuesto**

M5 solicita la guía al cerrar la carga nocturna mediante `erp-sync` en VM-04 y guarda folio, tipo, emisor, destinatario, versión de carga, documento y hash antes de liberar; el conductor dispone de representación gráfica o impresa conforme al procedimiento tributario (SII, s. f.-a). Talca entrega la solicitud por RabbitMQ local; Concepción y los cross-docking la entregan por RabbitMQ local, shipper y la cola FIFO de solicitudes al ERP, que `erp-sync` consume por salida, y reciben folio y documento por la cola de respuesta del sitio. Si un cambio de carga invalida la guía y no hay camino disponible hasta el ERP de Talca, el camión solo sale con la carga amparada por su guía vigente y el ajuste pasa a la ruta siguiente. Una guía anulada no se reutiliza: esa salida espera un documento válido. En el local, M6 registra nombre del receptor, identificación según política validada, lugar, hora, cantidades aceptadas/rechazadas y firma manuscrita capturada o alternativa operacional QR/fotografía. La cola cifrada conserva el objeto y su hash; la sincronización vincula la evidencia a entrega y guía.

Para un receptor electrónico habilitado se propone recibir su acuse por el mecanismo tributario del ERP o el canal EDI acordado, conservar el XML y su validación e identificar al firmante o emisor autorizado. Para el receptor al que corresponde constancia en representación impresa, se obtiene esa constancia y se conserva copia digital vinculada; no se obliga a una persona natural a poseer firma electrónica avanzada. La diferencia se fundamenta en la interpretación publicada por el SII sobre receptores electrónicos y no obligados (SII, 2018) y en su formato de recibo electrónico (SII, s. f.-b). Tributación valida el perfil aplicable de cada cliente antes de habilitarlo.

<a id="tab:estados-documentales"></a>

**Tabla A.26 — Estados de evidencia y consecuencias**

| **Hecho** | **Evidencia conservada** | **Consecuencia lógica** |
| --- | --- | --- |
| Guía disponible | Folio, documento y hash del ERP. | M5 comprueba correspondencia con carga vigente. |
| Salida liberada | Usuario, carga, guía y hora. | M6 recibe el viaje; no modifica el documento. |
| Recepción completa | Cantidades y POD íntegro. | M7 concilia; acuse tributario sigue su propio estado. |
| Recepción parcial | Líneas rechazadas, lotes y causal. | M8 registra devolución; ERP decide ajuste documental. |
| Negativa a firmar | Nombre si disponible, causal y constancia alternativa. | Entrega en excepción; no marcar acuse legal obtenido. |
| Acuse tributario recibido | Origen, XML/constancia, fecha y validación. | Vincular al DTE sin reemplazar el POD. |
| Resultado incierto | Clave original y último estado conocido. | Consultar antes de reenviar o solicitar otro documento. |

Fuente: diseño lógico M5–M8, RT-16.14 del caso (Bases Técnicas del caso, cap. 15, p. 27) y publicaciones del SII citadas.

AL-POD-01 ensaya recepción completa, parcial, persona sustituta, negativa a firmar, falta de señal y objeto alterado. Se acepta cuando cada hecho conserva autor y origen, la guía precede a la salida, un cambio de carga invalida la guía y exige una nueva, el documento no cambia por reenvío y una evidencia operacional insuficiente no se declara acuse tributario. La FAQ del SII sobre contingencia es orientativa y no equivale a autorización para este contribuyente (SII, s. f.-c); el procedimiento de emisión bajo falla se cierra por AL-DTE-01.

## Anexo 4-V — Protocolos de aceptación

<a id="anx:V"></a>

Las pruebas siguientes se ejecutan en Preproducción y antes de la ola aplicable. Cada acta identifica carga, inyección de falla, resultados observados y responsables; el Anexo 4-M desarrolla AL-DTE-01, AL-DR-01, AL-OFF-01 y AL-CLI-01. La Tabla [A.27](LAFROX-Subdocumento4-Anexos.md#tab:condiciones-aceptacion) resume sus protocolos.

<a id="tab:condiciones-aceptacion"></a>

**Tabla A.27 — Protocolos de aceptación de la arquitectura lógica**

| **ID** | **Ejecución** | **Criterio de aceptación** | **Evidencia** |
| --- | --- | --- | --- |
| AL-DTE-01 | Ensayar 96 guías por las rutas de Talca y de los demás sitios, con fallas y cambio de carga. | Cada camión sale con guía válida del ERP; sin los tres caminos, solo lleva la carga amparada; una guía anulada no se reutiliza. | Origen, ruta, folio, carga, acuse y acta. |
| AL-POD-01 | Ensayar entrega total, parcial y receptor sustituto sin señal. | El POD conserva autor, objeto y acuse aplicable. | Firma, hash y trazas. |
| AL-SLA-01 | Simular ventanas y cuotas de ERP, SII y contrapartes. | Reintentos y escalamiento respetan cada contrato. | Contratos, logs y tiempos. |
| AL-OFF-01 | Aislar cada sitio 24 horas con dos relevos y despachar con guía preemitida. | Operación local y conciliación sin duplicados; solo sale carga amparada. | Bitácora, guías, colas y acta. |
| AL-CLI-01 | Armar pedidos sin señal en el Portal de Clientes instalado y reconectar. | Ningún pedido se pierde ni se duplica; M3 reserva solo al recibirlo. | UUID, respuesta de M3 y acta. |
| AL-DR-01 | Cortar caminos y recuperar Talca en nube. | RTO ≤ 4 horas y RPO ≤ 15 minutos. | Marcas de agua y acta. |
| AL-PERF-01 | Aplicar carga de 3× con mamparos por perfil. | Latencias y colas cumplen el Anexo 4-T. | Métricas y reporte. |
| AL-STOCK-01 | Pedir la última unidad desde preventa, portal y EDI, con cortes y acuses perdidos. | Una sola reserva confirmada con retención durable; nunca stock negativo. | Estado central y local, p95 y acta. |
| AL-ACT-01 | Probar cada actor del Anexo 4-N con una operación permitida y una denegada. | Autorización por acción y recurso, con auditoría personal. | Política, etapa, registros y acta. |

Fuente: elaboración propia.

AL-DTE-01 comprueba ambas rutas de las 96 guías, la preemisión nocturna, la invalidación por cambio de carga y la nueva emisión del ERP ante el SII por fibra, LTE o Starlink en espera caliente. AL-OFF-01 comprueba por separado el despacho con guía válida preemitida. AL-DR-01 mide la extracción continua y la recuperación del WMS de Talca en ECS Fargate; el límite residual se desarrolla en 4.3.2. Los resultados de todas las pruebas se vinculan a los requisitos y al registro ADR del Anexo 4-O.

**AL-STOCK-01. Confirmación central con custodia local**

En Preproducción se pide la misma última unidad al mismo tiempo desde preventa, portal y EDI. Se corta el enlace antes y después del registro local, se pierde el acuse, se repite el UUID, se cancela durante un aislamiento y se presenta una época obsoleta. Solo se acepta una reserva confirmada con retención durable de igual identidad, época y cantidad. El disponible nunca queda negativo y un timeout nunca confirma. La preparación consume la retención y una cancelación tardía no libera lo consumido. La prueba mide el p95 de confirmación con la latencia entre la nube y el sitio, la edad de la cola y la recuperación. También mide la proporción de líneas que requieren más de una retención, para contrastar el volumen del Anexo 4-I. Los resultados se trazan a RNG-01, RF-03.03, RT-02.06 y RT-03.12.

**AL-ACT-01. Autorización de los quince actores**

Cada fila del Anexo 4-N se prueba con una operación permitida y una denegada. Se incluyen el cruce entre empresas o rutas, la credencial de un representante usada como conductor, un rol de TI que intenta una aprobación de negocio, la aprobación del descuadre propio, la baja y el relevo sin conexión. Se comprueba que cada portal se habilita solo en su etapa, que el cliente tradicional compra asistido sin cuenta y que el catálogo público no muestra precios. El resultado esperado es una autorización por acción y recurso, con auditoría personal y sin credenciales compartidas. La evidencia se registra por actor, requisito, versión de la política y etapa, y se traza a RT-12.05, RT-12.06 y RT-12.12.

# Anexo 4-W — Memoria de cálculo del dimensionamiento

<a id="anx:42A"></a>

La memoria avanza desde los datos del caso hasta la capacidad de cada sitio y de la nube, en doce secciones.

4-W.section
anexo42A.section

## 4-W.1 Entradas, requisitos, parámetros y supuestos

<a id="sec:anexo-4b-entradas"></a>

Este anexo sustenta el dimensionamiento del apartado 4.2.6 y entrega la memoria de cálculo que respalda el Formulario T-11. Su alcance comprende las dieciséis dimensiones, la capacidad por sitio, la nube, los enlaces, la migración, el crecimiento y las pruebas de aceptación. Los supuestos de volumen, concurrencia y crecimiento que exige el Formulario T-7 (SV-01 a SV-07) se declaran en este anexo; los que fijan las cantidades de implementos (S-28 y S-30 a S-41) se registran en el Subdocumento 3.

La Tabla [A.28](LAFROX-Subdocumento4-Anexos.md#tab:anexo-4b-hechos) concentra los hechos que alimentan las fórmulas y conserva su cita en la forma de la propuesta.

<a id="tab:anexo-4b-hechos"></a>

**Tabla A.28 — Hechos del caso utilizados**

| **Dato** | **Valor** | **Fuente** |
| --- | --- | --- |
| Volumetría comercial | 31.000 pedidos; 260.000 líneas; 2,4 millones de unidades mensuales | Bases Técnicas del caso, cap. 2, p. 4 |
| Entregas | ≈ 1.400 normales y ≈ 2.600 en septiembre | Bases Técnicas del caso, cap. 14, p. 24 |
| Documentos tributarios electrónicos (DTE) y transporte | ≈ 34.000 documentos tributarios electrónicos, ≈ 2.100 viajes de camión y ≈ 420.000 km recorridos al mes | Bases Técnicas del caso, cap. 14, p. 24 |
| Operación de terreno | 62 preventistas; 42 camiones propios; 54 de terceros; 184 personas de administración, comercial y soporte | Bases Técnicas del caso, cap. 2, p. 5 |
| Bodegas | 120 personas nocturnas en Talca; 18.000 m² y 9.000 m² | Bases Técnicas del caso, cap. 8, p. 14, entrevista; Bases Técnicas del caso, cap. 2, p. 5 |
| Ventanas | Preparación 22:00–06:00; despacho 05:30–07:00; sincronización 17:00–20:00 | Bases Técnicas del caso, anexo B, p. 38 |
| Ruta y frío | 34 clientes en una ruta máximo actualmente; 18 camiones propios y 10 de terceros con equipo de frío; Talca a -22 °C | Bases Técnicas del caso, cap. 8, p. 16, entrevista al conductor; Bases Técnicas del caso, cap. 2, p. 5 |

La Tabla [A.29](LAFROX-Subdocumento4-Anexos.md#tab:anexo-4b-parametros) fija los valores que impone la propuesta. Un valor de diseño se confirma mediante perfilado, QA o prueba de carga, pero no se presenta como un hecho del CLIENTE.

<a id="tab:anexo-4b-parametros"></a>

**Tabla A.29 — Parámetros de diseño**

| **Parámetro** | **Valor** | **Justificación y uso** | **Confirmación** |
| --- | --- | --- | --- |
| Operaciones de flujo | 2 por línea: lectura de ubicación o lote y confirmación; 5 por entrega: estado, evidencia, documento, cobro y cierre; 4 por cross-docking: recepción, escaneo, desconsolidación y despacho | Flujo del apartado 4.1 | Validar mediante RT-09.06 (Bases Técnicas Transversales, cap. 9, p. 21) |
| Preventa | 2 consultas por visita y 1 operación por línea | Stock, crédito y pedido | Contrato y carga |
| Concentración horaria | SV-04 = 2,0, sólo en la hora cargada | Frío, despacho, reparto y sincronización | Perfil de 24 h |
| Portal | 60 solicitudes por sesión de 10 minutos; sensibilidad de 120 por sesión | Cota de sesiones; las sesiones se reparten en la hora y 15 minutos sólo determinan concurrencia | Validar mediante RT-09.06 (Bases Técnicas Transversales, cap. 9, p. 21) |
| Registro y movimiento | 1 KB; 0,5 KB | Almacenamiento y base local; sensibilidad ±50 % | QA |
| Base local | 4 meses más maestros y lotes presentes | Ciclo de conteo y conciliación | Levantamiento WMS |
| Evidencia | 30 KB de firma; 200 KB de foto; una adicional en devolución | Compresión en App de reparto | QA |
| Plataforma | 50 ms de CPU por solicitud; 64 MB por proceso; 150 ms de permanencia | Capacidad de VM y nube; se perfila y verifica en la prueba de carga | Validar mediante RT-09.06 (Bases Técnicas Transversales, cap. 9, p. 21) |
| Observabilidad | 250 MB y 1.000 eventos por nodo/día | ADOT: registros, métricas y trazas | Operación |
| Servidor del ERP trasladado | 1.600 W de placa, igual que un nodo del clúster | Carga eléctrica, UPS y generador de la sala de Talca (apartado 4.3.1.4) | Medir el equipo en el levantamiento |
| Subida satelital D-06 | 2 Mbps de subida mínima supuesta | Parámetro conservador para Talca, Concepción y los cross-docking | Confirmar en la instalación |
| Actualizaciones | App ≤100 MB; sistema operativo 2 GB | Tandas dominicales sin bodega ni reparto | Bases Técnicas del caso, anexo B.2, p. 38 |

La Tabla [A.30](LAFROX-Subdocumento4-Anexos.md#tab:anexo-4b-supuestos) declara el fundamento, impacto y validación de cada supuesto. Ninguno reemplaza un dato literal del caso.

<a id="tab:anexo-4b-supuestos"></a>

**Tabla A.30 — Supuestos de volumen**

| **Código** | **Qué suponemos y por qué** | **Si resulta equivocado** | **Cómo y cuándo se valida** |
| --- | --- | --- | --- |
| SV-01 | Un pedido genera una entrega; 31.000/1.400 produce 22,14 días y concuerda con 2.100/96. | Cambian evidencia, mensajes y almacenamiento. | Conciliación ERP–guías–entregas en Etapa 1. |
| SV-02 | Septiembre escala los flujos de volumen y diciembre no supera su exigencia; el factor 1,857 es cálculo. | Falta capacidad en el nuevo peak. | Serie mensual antes del congelamiento. |
| SV-03 | Talca prepara 2/3 y Concepción 1/3 por superficies y función de abastecimiento adicional. | Faltan terminales, WMS o enlace en el centro subestimado. | Exportación WMS por centro. |
| SV-04 | La hora cargada duplica la media de su propia ventana, una sola vez. | El cuello se traslada a WMS, ERP, Wi-Fi o nube. | Perfil horario y RT-09.06 (Bases Técnicas Transversales, cap. 9, p. 21). |
| SV-05 | La cadena principal no supera 11 % de los pedidos en el escenario EDI, que opera todos los días desde enero de 2029; el caso informa que pesa 11 % de la venta, y como sus pedidos son mayores que el promedio, tomar 11 % de los pedidos es una cota holgada. | Aumentan colas EDI. | Contrato y certificación del intercambio. |
| SV-06 | 2,5 contactos por persona/mes, 10 minutos y 25 % en hora cargada. | Se requieren más personas. | Tickets y Erlang C mensual. |
| SV-07 | La API de telemetría de los camiones propios continúa disponible. | Posición automática se degrada a ruta planificada. | Prueba contractual y técnica. |

## 4-W.2 Dimensiones 1–3: transacciones por segundo

<a id="sec:anexo-4b-dimensiones-1-3"></a>

Se calcula el máximo horario de cada lugar para no sumar ventanas que no coinciden. Los días equivalentes son 31.000 ÷ 1.400 = 22,14 días (los cálculos usan el cociente sin redondear, 22,142857) y el control cruzado es 2.100 ÷ 96 = 21,88 días. El factor de septiembre es 2.600 ÷ 1.400 = 1,857.

Las operaciones de cada entrega en cross-docking se reparten en recepción, escaneo y desconsolidación de 03:00 a 05:00, y despacho de 05:00 a 06:00; SV-04 concentra sólo la hora cargada de cada tramo. La preparación normal de Talca se calcula como 11.742 líneas por noche × 2 operaciones × 2/3 ÷ 28.800 segundos = 0,54 TPS de media; la hora cargada de SV-04 alcanza 1,09 TPS. El despacho se distribuye entre Talca y Concepción según SV-03; a las 05:00 el WMS alcanza 1,46 TPS normal y 2,68 TPS en septiembre en Talca, y 0,73 y 1,34 TPS en Concepción.

La nube suma preventa, reparto, recepción, trazabilidad, guías, sincronización y el escenario EDI. Los aproximadamente 2.852 documentos/día peak son el total de DTE (34.000 ÷ 22,14 × 1,857), no sólo guías; tomarlos todos como guías a emitir antes de la salida es una cota conservadora. El portal queda separado: 2.600 ÷ 9 × 2 por SV-04 = 578 sesiones en la hora cargada; 578 × 60 ÷ 3.600 = 9,63 solicitudes/s y 578 × 10 ÷ 60 = 96,30 concurrentes. La cota extrema es 2.600 × 60 ÷ 3.600 = 43,33 solicitudes/s y 433,33 concurrentes. Las 2.600 sesiones diarias del portal son un parámetro de diseño: se toma una sesión por cada cliente de food service y de cadenas, 2.100 + 500 = 2.600 (Bases Técnicas del caso, cap. 2, p. 4). La cota cubre esos dos canales y no al canal tradicional, cuyo uso del portal es opcional y no tiene medición en el caso. Ese canal se admite con una cuota propia en la puerta de enlace: 20 solicitudes/s agregadas para los clientes tradicionales, que es la capacidad remanente bajo el techo de 8 tareas en la cota extrema (8 × 14,00 − 91,70 = 20,30 solicitudes/s). Si la adopción medida acerca el uso a esa cuota, se amplía la capacidad antes de subirla. La cuota no rechaza pedidos de preventa, que usan su propio perfil. No son las 2.600 visitas diarias de preventa (Bases Técnicas del caso, anexo B, p. 38); que las dos cifras coincidan es casualidad.

La dimensión 1 es **12,34 TPS a las 12:00** en régimen normal. La dimensión 2 es **3,76 TPS normal y 6,94 TPS peak**, máximos reales del perfil horario entre 05:00 y 06:00 para la ventana 05:30–07:00. La dimensión 3 es **14,66 TPS a las 12:00** en septiembre. RT-09.06 (Bases Técnicas Transversales, cap. 9, p. 21) es 1,5 × 14,66 = **21,99 TPS**.

La Tabla [A.31](LAFROX-Subdocumento4-Anexos.md#tab:anexo-4b-horario) conserva el perfil hora por hora que produce esos máximos.

<a id="tab:anexo-4b-horario"></a>

**Tabla A.31 — Perfil horario por lugar de proceso**

| **Hora** | **Talca N/P** | **Concepción N/P** | Cross-docking N/P | **Nube N/P** | **Portal N/P** | **Total N/P** |
| --- | --- | --- | --- | --- | --- | --- |
| 00:00 | 0,54 / 1,01 | 0,27 / 0,50 | 0,00 / 0,00 | 0,74 / 1,37 | 0,00 / 0,00 | 1,55 / 2,88 |
| 01:00 | 0,54 / 1,01 | 0,27 / 0,50 | 0,00 / 0,00 | 0,74 / 1,37 | 0,00 / 0,00 | 1,55 / 2,88 |
| 02:00 | 0,54 / 1,01 | 0,27 / 0,50 | 0,00 / 0,00 | 0,74 / 1,37 | 0,00 / 0,00 | 1,55 / 2,88 |
| 03:00 | 0,54 / 1,01 | 0,27 / 0,50 | 0,58 / 1,08 | 0,74 / 1,37 | 0,00 / 0,00 | 2,14 / 3,97 |
| 04:00 | 0,54 / 1,01 | 0,27 / 0,50 | 1,17 / 2,17 | 0,74 / 1,37 | 0,00 / 0,00 | 2,72 / 5,05 |
| 05:00 | 1,46 / 2,68 | 0,73 / 1,34 | 0,78 / 1,44 | 0,79 / 1,47 | 0,00 / 0,00 | 3,76 / 6,94 |
| 06:00 | 0,74 / 1,33 | 0,37 / 0,67 | 0,00 / 0,00 | 0,68 / 1,26 | 0,00 / 0,00 | 1,79 / 3,26 |
| 07:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,84 / 1,56 | 0,00 / 0,00 | 0,84 / 1,56 |
| 08:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,84 / 1,57 | 0,00 / 0,00 | 0,84 / 1,57 |
| 09:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 1,70 / 3,15 | 4,81 / 4,81 | 6,51 / 7,96 |
| 10:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 1,70 / 3,15 | 4,81 / 4,81 | 6,51 / 7,97 |
| 11:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 1,70 / 3,15 | 4,81 / 4,81 | 6,51 / 7,96 |
| 12:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 2,71 / 5,03 | 9,63 / 9,63 | 12,34 / 14,66 |
| 13:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 1,70 / 3,15 | 4,81 / 4,81 | 6,51 / 7,96 |
| 14:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 1,70 / 3,15 | 4,81 / 4,81 | 6,51 / 7,96 |
| 15:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 1,70 / 3,15 | 4,81 / 4,81 | 6,51 / 7,96 |
| 16:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 1,70 / 3,15 | 4,81 / 4,81 | 6,51 / 7,96 |
| 17:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 2,47 / 4,59 | 4,81 / 4,81 | 7,29 / 9,41 |
| 18:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 2,40 / 4,45 | 0,00 / 0,00 | 2,40 / 4,45 |
| 19:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 1,46 / 2,71 | 0,00 / 0,00 | 1,46 / 2,71 |
| 20:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,68 / 1,26 | 0,00 / 0,00 | 0,68 / 1,26 |
| 21:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,68 / 1,26 | 0,00 / 0,00 | 0,68 / 1,26 |
| 22:00 | 0,54 / 1,01 | 0,27 / 0,50 | 0,00 / 0,00 | 0,74 / 1,37 | 0,00 / 0,00 | 1,55 / 2,88 |
| 23:00 | 0,54 / 1,01 | 0,27 / 0,50 | 0,00 / 0,00 | 0,74 / 1,37 | 0,00 / 0,00 | 1,55 / 2,88 |

La fila de las 12:00 gobierna los TPS totales porque coincide la hora cargada de preventa, reparto y portal. La hora de preparación conserva la mayor carga local de WMS, pero no la mayor suma de lugares.

## 4-W.3 Dimensiones 4–6: personas, concurrencia y dispositivos

<a id="sec:anexo-4b-dimensiones-4-6"></a>

La dimensión 4 es (640 + 160) + 14.200 + 180 = **15.180 personas o entidades**. La dimensión 5 toma el mayor resultado entre ventanas: noche 120 + 60 (S-39) + 6 (S-35) = 186; despacho 96; día sin portal 62 + 96 + 184 = 342; portal en régimen 342 + 96,30 = **438,30**; portal extremo 342 + 433,33 = **775,33**. La dimensión 6 es 62 + 96 = **158 dispositivos de terreno en operación simultánea**.

El parque separado de la dimensión 6 se distribuye así:

- Bodega: 132 terminales en Talca, 22 de ellos para congelado, y 66 en Concepción.
 
- Terreno: 69 terminales de preventa, 106 de reparto, 106 impresoras y 106 terminales de pago.
 
- Cross-docking y frío: 7 terminales de cross-docking y 31 termógrafos.

Cada cantidad aplica los supuestos S-28 y S-30 a S-41, registrados en el Subdocumento 3, y la reserva del 10 % del parque de cada tipo, redondeada hacia arriba, conforme a la tabla de repuestos de las Bases Técnicas Transversales (cap. 8, p. 19):

- Equipos de reparto (S-30): 96 camiones + 10 de reserva = 106 de cada dispositivo. A tres años (S-31), los viajes crecen 2.400 ÷ 2.100 = 1,143, es decir, 14,3 %; la flota llega a 96 × 1,143 = 109,7, unos 110 camiones, y el parque a 110 + 11 = 121, es decir, 15 unidades más de cada dispositivo.
 
- Terminales de preventa (S-32): 62 + 7 = 69. A tres años, 70 preventistas, un 12,9 % más, y 70 + 7 = 77, es decir, 8 más.
 
- Terminales de bodega: se comparten entre turnos (RT-12.11; Bases Técnicas del caso, cap. 15, p. 27), sin personal de carga adicional (S-33), de modo que los fija el turno nocturno: 120 preparadores en Talca y 60 en Concepción (S-39). En Talca, 20 son de la cuadrilla de congelado (S-34): los productos de frío son 1.100 ÷ 8.400 = 13,1 % del surtido y el congelado ocupa 400 ÷ 1.300 = 30,8 % del área fría, de modo que el congelado es cerca de 13,1 % × 30,8 % = 4,0 % de las líneas; 120 personas × 8 h = 960 horas-persona, cuyo 4,0 % son 38,4 horas, concentradas en las últimas 2 horas del turno: 38,4 ÷ 2 = 19,2, unas 20 personas. Talca suma 20 + 2 de congelado y 100 + 10 estándar, Concepción 60 + 6, y los cross-docking 6 + 3, una unidad de reserva por plataforma (S-35): 207 en total. A tres años (S-32), la dotación de los centros de distribución crece 350 ÷ 310 = 12,9 %: Talca llega a 23 + 3 de congelado y 113 + 12 estándar, y Concepción a 68 + 7; con los 9 de los cross-docking, el parque llega a 235 terminales de bodega, 28 más que al inicio. Las licencias de gestión de dispositivos y las identidades de terminal se dimensionan con 207 equipos al inicio y 235 en el año 3.
 
- Termógrafos: 28 + 3 = 31, para los 18 camiones con frío propios y los 10 de transportistas (S-28), sin compra por crecimiento (S-38).

## 4-W.4 Dimensiones 7–10: almacenamiento, retención y migración

<a id="sec:anexo-4b-dimensiones-7-10"></a>

El almacenamiento transaccional se calcula con 1.300.000 eventos = 260.000 líneas × 5, 520.000 operaciones = 260.000 líneas × 2, 155.000 operaciones = 31.000 pedidos × 5 y 279.050 movimientos = 260.000 líneas + 14.500 pallets + 3.400 conteos + 1.150 recepciones. Por tanto, ((1.300.000 + 520.000 + 155.000) × 1 KB + 279.050 × 0,5 KB) × 2 × 12 = **50,75 GB/año** y seis años acumulan **304,49 GB** como cota de retención. La evidencia es 30 KB + 200 KB × (1 + 900 ÷ 31.000) = **235,81 KB por entrega** y genera **87,72 GB/año**; en el mes peak alcanza 13,58 GB.

La temperatura separa cámaras y camiones: 21 puntos instalados × 288 lecturas/día = 6.048 lecturas de cámara, con la cámara de Concepción estimada por S-37, y 28 termógrafos × 174 lecturas/día entre 05:30 y 20:00 = 4.872 lecturas de camión; el total es 10.920 mensajes/día. Con 145 bytes por lectura, son 0,58 GB/año crudos, 0,14 GB/año almacenados con factor 0,25 y 2,89 GB crudos en cinco años. La posición produce 42 camiones × 12 h × 120 eventos/h × 365 = 22.075.200 eventos/año; se cuentan los 365 días como cota, aunque el domingo no hay reparto; con 145 bytes son 3,20 GB crudos y 0,80 GB almacenados en 12 meses. Son filas separadas porque sus retenciones son distintas.

La dimensión 10 se estima por dominio:

- Maestros completos: 34.180 KB.
 
- Ventas y pedidos: 3 años y 10.476.000 KB.
 
- Inventario y movimientos: 2 años y 3.348.600 KB.
 
- Recepciones con campo de lote: 5 años y 1.380.000 KB.
 
- Cuentas por cobrar: 2 años y 816.000 KB.

La suma de 16.054.780 KB × 2 ÷ 1.000.000 = **32,11 GB**. Con 10 o 30 líneas por recepción, el intervalo es **30,73–33,49 GB**. No se multiplican eventos históricos de trazabilidad: el caso declara que no existe una forma consultable. El 41 % sin lote sólo orienta el saneamiento.

## 4-W.5 Dimensiones 11–12: integraciones, mensajes y enlaces

<a id="sec:anexo-4b-dimensiones-11-12"></a>

La dimensión 11 cuenta los quince contratos INT-01 a INT-15 del apartado 4.1. La Tabla [A.32](LAFROX-Subdocumento4-Anexos.md#tab:anexo-4b-integraciones) deja el volumen por integración; las solicitudes del portal y las llamadas internas no aparecen.

<a id="tab:anexo-4b-integraciones"></a>

**Tabla A.32 — Mensajes por integración**

| **Integración** | **Normal/día** | **Peak/día** | **Origen del volumen** |
| --- | --- | --- | --- |
| INT-01 Pedido preventa y consulta | 1.400 | 2.600 | 1.400 × 1; 2.600 × 1, por SV-01 |
| INT-02 Entrega, POD y cobro | 7.000 | 13.000 | 1.400 × 5; 2.600 × 5 |
| INT-03 Eventos de bodega a nube | 58.710 | 109.032 | 260.000 ÷ 22,14 × 5; peak × 1,857 |
| INT-04 Detalle cross-docking a la nube | 5.600 | 10.400 | 1.400 × 4; cota de una plataforma |
| INT-03/04 Coordinación de reserva | 46.968 | 87.228 | 260.000 ÷ 22,14 × 4; peak: 21.807 líneas × 4 |
| INT-05 Eventos de temperatura | 10.920 | 10.920 | 6.048 + 4.872 lecturas/día |
| INT-06 ERP 2017 | 2.025 | 3.762 | 1.400 + 1.150 ÷ 22,14 + 900 ÷ 22,14 + 11.800 ÷ 22,14; peak × 1,857 |
| INT-07 DTE/SII | 3.071 | 5.703 | 34.000 ÷ 22,14 × 2; peak × 1,857 |
| INT-08 Cadenas modernas EDI | 616 | 1.144 | Escenario 2029 (hoy 0): 1.400 × 11 % × 4; 2.600 × 11 % × 4 |
| INT-09 Pasarela de pago | 2.800 | 5.200 | Cota de un pago electrónico por entrega, solicitud y respuesta: 1.400 × 2; 2.600 × 2 |
| INT-10 Mapas y geocodificación | 96 | 96 | 96 camiones × 1 |
| INT-11 Avisos al cliente | 2.800 | 5.200 | 1.400 × 2; 2.600 × 2 |
| INT-12 Cambios de datos a réplica | 12.602 | 23.404 | Cota conservadora de movimientos de todos los sitios: 279.050 ÷ 22,14; peak × 1,857 |
| INT-13 Identidad a sitio | 764 | 764 | 382 dispositivos × 2 |
| INT-14 Métricas y trazas | 13.000 | 13.000 | 13 nodos × 1.000 |
| INT-15 Telemetría existente | 60.480 | 60.480 | 42 × 12 × 120 |
| **Total** | **228.852** | **351.933** | **15 integraciones** |

Para la dimensión 12, el drenaje se obtiene sumando los aportes acumulados en 24 horas y dividiendo por 2 horas:

- Aportes en Talca: los cambios de 0,041 GB/día viajan como WAL, que no se suma aparte: WAL = 3 × 0,041 = 0,123 GB/día; broker = 0,5 × 0,041 = 0,020 GB/día; telemetría = 10.920 × 145 ÷ 1.000.000.000 ÷ 2 = 0,001 GB/día; observabilidad = 6 × 0,25 = 1,50 GB/día; incremental de respaldo = 0,041 GB/día.
 
- Resultado por sitio: Talca acumula 1,68 GB/día y drena 1,87 Mbps; su hora cargada de oficina y retorno de flota suma 3,29 Mbps, por lo que el peor caso es 3,29 + 1,87 = **5,16 Mbps**. Concepción acumula 1,09 GB/día y drena 1,21 Mbps; cada cross-docking acumula 0,27 GB/día y drena 0,30 Mbps.
 
- Tráfico prioritario continuo: Talca 0,014 Mbps; Concepción 0,007 Mbps; cada cross-docking 0,002 Mbps, con WAL, broker/outbox, guías y SII, identidad y telemetría crítica.

<a id="tab:anexo-4b-enlaces"></a>

**Tabla A.33 — Capacidad y utilización de enlaces por camino**

| **Sitio** | **Camino** | **Subida** | **Carga** | **Uso** |
| --- | --- | --- | --- | --- |
| Talca | D-03 fibra | 20 Mbps | 5,16 Mbps, peor caso | 25,80 % |
| Talca | D-04 LTE | 5 Mbps | 1,87 Mbps, drenaje | 37,43 % |
| Talca | D-06 satélite | 2 Mbps | 1,87 Mbps, drenaje | 93,59 % |
| Concepción | D-03 fibra | 10 Mbps | 1,88 Mbps, peor caso | 18,82 % |
| Concepción | D-04 LTE | 3 Mbps | 1,21 Mbps, drenaje | 40,45 % |
| Concepción | D-06 satélite | 2 Mbps | 1,21 Mbps, drenaje | 60,68 % |
| Cada cross-docking | D-06 satélite | 2 Mbps | 0,35 Mbps, peor caso | 17,41 % |
| Cada cross-docking | D-04 LTE | 2 Mbps | 0,30 Mbps, drenaje | 14,92 % |

La coordinación de reserva no se suma al drenaje: durante un aislamiento la nube no confirma reservas remotas del sitio, por lo que sus solicitudes esperan en la cola de la nube y no en el sitio. Su tasa continua es de 87.228 × 1 KB ÷ 86.400 s, unos 0,008 Mbps sumando todos los sitios, y no cambia la utilización de la tabla. La tasa prioritaria suma WAL, broker y telemetría crítica a los mensajes de guía, respuesta del SII e identidad, con una cota de 1 KB por mensaje; se divide el volumen diario por 86.400 segundos. Los 12.602/23.404 cambios diarios de INT-12 son una cota conservadora basada en movimientos de todos los sitios, aplicada al dimensionamiento de Talca y no un conteo medido allí. La utilización de respaldo divide el drenaje por la capacidad de cada camino. En Talca y Concepción, D-06 permanece encendido en espera caliente, con túnel IPsec establecido y BGP de menor preferencia; solo toma tráfico si fallan fibra y LTE, cuando prioriza DMS/WAL de Talca, salida del broker y outbox, guías hacia ERP y SII, identidad y telemetría crítica. La tarifa plana no agrega costo por mantenerlo encendido. En los cross-docking Starlink es el camino principal y LTE de dos proveedores da respaldo. El tercer camino de los CD sostiene la salida continua de datos exigida por el RPO de 15 minutos; la oficina cede prioridad durante la recuperación.

La ventana dominical usa ocho horas sin operación de bodega ni reparto. Cada sitio actualiza sus terminales de bodega y los equipos de reparto de los camiones que estacionan en él, repartidos por SV-03: 71 de los 106 en Talca y 35 en Concepción. En Talca, el respaldo completo de 15,12 GB se transfiere a 20 Mbps en 1,68 horas y la aplicación de sus 203 equipos, 20,30 GB, en 2,26 horas; juntas requieren 3,94 horas. Una tanda de 18 sistemas operativos de 2 GB agrega 4,00 horas y ocupa 7,94 horas; una ronda completa ocupa 12 domingos. En Concepción, el respaldo completo de 7,76 GB y la aplicación de sus 101 equipos, 10,10 GB, requieren 3,97 horas; una tanda de 9 sistemas operativos ocupa 7,97 horas y la ronda completa, 12 domingos. Los 69 terminales de preventa no usan esta ventana: trabajan en la calle y el MDM los actualiza por la red móvil. En cada cross-docking, el respaldo de 1,89 GB y la aplicación de sus 2 terminales, 0,20 GB, requieren 2,33 horas sobre la capacidad supuesta de 2 Mbps; con los 2 sistemas operativos, la ventana ocupa 6,77 horas y la ronda requiere un domingo. La aplicación se actualiza en un domingo por sitio; el sistema operativo se distribuye en tandas dominicales con cadencia semestral, dentro de los aproximadamente 43 domingos disponibles al año tras los congelamientos de septiembre y diciembre.

## 4-W.6 Dimensiones 13–14: terreno y sincronización

<a id="sec:anexo-4b-dimensiones-13-14"></a>

La peor ruta produce 34 × 235,81 KB ÷ 1.024 + 2 MB = **9,83 MB**. La ruta promedio produce 5,36 MB normales y 8,24 MB en septiembre. Para diez minutos, el umbral es 9,83 MB × 8 ÷ 600 segundos = **0,13 Mbps efectivos**.

La dimensión 14 es un tiempo. Los 96 camiones regresan entre 17:00 y 20:00; con SV-04, 96 ÷ 3 × 2 = **64 camiones** llegan en la hora punta. Según SV-03, se reparten entre Talca y Concepción en una proporción de 2/3 y 1/3: requieren 0,93 y 0,47 Mbps, respectivamente, en la Wi-Fi y el enlace de cada centro (1,40 Mbps en total). La flota completa agrega 0,70 Mbps durante las tres horas y queda sincronizada aproximadamente diez minutos después del último camión.

## 4-W.7 Dimensiones 15–16: mesa de ayuda y operación

<a id="sec:anexo-4b-dimensiones-15-16"></a>

La mesa de ayuda se dimensiona en cuatro pasos:

- Demanda horaria: (640 + 160) × 2,5 = **2.000 contactos mensuales**. Con 22,14 días equivalentes, la hora cargada concentra 2.000 × 25 % ÷ 22,14 = 22,58 contactos/hora y cada una de las otras 17 horas recibe 2.000 × 75 % ÷ 22,14 ÷ 17 = 3,98 contactos/hora.
 
- Resultado Erlang C: con 10 minutos de atención media y 80 % de respuestas antes de 20 segundos, exige 7 agentes en la hora cargada y 2 en las demás. Erlang C supone que nadie abandona la espera, por lo que no verifica el abandono ≤5 % ni la resolución al primer contacto ≥70 % de RT-21.06 (Bases Técnicas Transversales, cap. 21, p. 36). Ambos se miden por contacto desde la marcha blanca, y la dotación se calibra con esa medición.
 
- Dotación simultánea: (7 + 17 × 2) × 6 = 246 horas-posición semanales; 246 ÷ 42 = 5,86, pero la dotación no puede ser menor que las 7 posiciones simultáneas, por lo que la mesa requiere **7 personas**.
 
- Capacidad máxima de la dotación: la franja que limita es la de dos agentes. Con A = λ/μ, μ = 6 contactos/hora, C = [Ac/c! × c/(c − A)] ÷ [Σ(k = 0…c − 1) Ak/k! + Ac/c! × c/(c − A)] y SL(20 s) = 1 − C × e−(cμ − λ) × 20/3.600, el límite es 2.283 contactos/mes: 2.283 × 75 % ÷ 22,14 ÷ 17 = 4,55 contactos/hora y SL = 80,0 % con dos agentes, mientras la hora cargada recibe 25,78 contactos/hora y SL = 83,5 % con siete. La hora cargada sola admitiría 2.391 contactos/mes, pero con esa demanda las otras franjas bajan a 78,3 %. El escenario base de 2.000 contactos cumple (90,6 % y 84,2 %), y el del año 3, 2.258 contactos, queda a 1,1 % del límite. Por eso, cuando la demanda medida supere 2.200 contactos/mes se agrega un tercer agente en las franjas valle, con lo que el límite pasa a 2.391 contactos/mes, fijado por la hora cargada.

La cobertura 24×7 de septiembre y diciembre requiere, además, al menos una posición de mesa en las horas 22:00–04:00 de lunes a sábado y durante los domingos: 6 × 6 + 24 = 60 horas-posición semanales; 60 ÷ 42 = 1,43, por lo que se agregan **2 personas** y la mesa peak queda en 9. Un NOC y un SOC de una posición cada uno requieren 2 × (168 ÷ 42) = **8 personas**; desde el 26-04-2028 requieren 2 × 5 = **10 personas**, porque 168 ÷ 40 = 4,2 se redondea hacia arriba a 5 personas por posición. A 42 horas semanales, la dotación total es **15 personas en operación normal y 17 en septiembre/diciembre**; desde el 26-04-2028, a 40 horas semanales, es **17 en operación normal y 19 en peak**. Las funciones NOC/SOC pueden ser subcontratadas conforme a RT-21.01 (Bases Técnicas Transversales, cap. 21, p. 35) y RT-11.17 (Bases Técnicas Transversales, cap. 11, p. 24).

## 4-W.8 Capacidad on-premise por VM

<a id="sec:anexo-4b-onpremise"></a>

La base local contiene maestros, stock, lotes presentes y movimientos del horizonte de cuatro meses. El tamaño usa 1 KB por registro, 0,5 KB por movimiento y factor 2 de índices y auditoría. La RAM de la base usa 4 GB más 25 % del tamaño a 3×.

<a id="tab:anexo-4b-vm"></a>

**Tabla A.34 — Requerimiento por VM real del diseño**

| **VM o equipo** | **Requerido actual** | **Requerido a 3×** | **Sitio** |
| --- | --- | --- | --- |
| VM-01 | 3 vCPU; 4 GB; 50 GB; 22 IOPS | 3 vCPU; 4 GB; 50 GB; 65 IOPS | Talca |
| VM-02 | 3 vCPU; 6 GB; 20 GB; 22 IOPS | 3 vCPU; 8 GB; 31 GB; 65 IOPS | Talca |
| VM-03 | 2 vCPU; 4 GB; 50 GB; 22 IOPS | 2 vCPU; 4 GB; 50 GB; 65 IOPS | Talca |
| VM-04 | 2 vCPU; 3 GB; 20 GB; 5 IOPS | 2 vCPU; 3 GB; 20 GB; 13 IOPS | Talca |
| VM-05 | 2 vCPU; 2 GB; 20 GB; 22 IOPS | 2 vCPU; 2 GB; 20 GB; 65 IOPS | Talca |
| VM-06 | 2 vCPU; 4 GB; 50 GB; 43 IOPS | 2 vCPU; 4 GB; 50 GB; 86 IOPS | Talca |
| VM-C01 | 3 vCPU; 4 GB; 50 GB; 11 IOPS | 3 vCPU; 4 GB; 50 GB; 33 IOPS | Concepción |
| VM-C02 | 3 vCPU; 5 GB; 20 GB; 11 IOPS | 3 vCPU; 6 GB; 20 GB; 33 IOPS | Concepción |
| VM-C03 | 2 vCPU; 2 GB; 20 GB; 11 IOPS | 2 vCPU; 2 GB; 20 GB; 33 IOPS | Concepción |
| VM-C04 | 2 vCPU; 4 GB; 50 GB; 22 IOPS | 2 vCPU; 4 GB; 50 GB; 43 IOPS | Concepción |
| Mini-PC | 3 vCPU; 5 GB; 50 GB; 52 IOPS | 3 vCPU; 5 GB; 50 GB; 156 IOPS | Cada cross-docking |

VM-04 incorpora dos procesos PHP CLI de `erp-sync` de 64 MB cada uno: la base de 2 GB sube a 3 GB tras redondear 2 + 2 × 64 ÷ 1.024. Las VMs de Talca suman 14 vCPU, 23 GB RAM, 210 GB y 136 IOPS actuales; a 3× suman 14 vCPU, 25 GB, 221 GB y 359 IOPS. El hipervisor agrega 15 % de vCPU y 2 GB RAM por nodo; Ceph agrega por nodo dos OSD de 1 vCPU y 4 GB cada uno y monitor/manager de 1 vCPU y 2 GB. El total de Talca es 26 vCPU, 59 GB RAM y 210 GB actuales; a 3×, 26 vCPU, 61 GB y 221 GB. Concepción requiere con hipervisor 12 vCPU, 17 GB RAM y 140 GB actuales; a 3×, 12 vCPU, 18 GB y 140 GB.

Cada nodo ofertado de Talca dispone de 32 hilos y 64 GB RAM. Sus seis NVMe de 960 GB sin RAID suman 5,76 TB brutos; Ceph con tres réplicas entrega 1,92 TB útiles; con un nodo caído conserva quórum y sirve los datos con dos réplicas hasta que el nodo vuelve. El umbral de llenado al 80 % es 1,54 TB frente a 221 GB requeridos a 3×. En N+1 quedan 64 vCPU, 128 GB RAM y 1,92 TB útiles: utilización de CPU/RAM/disco de 40,62 % / 46,09 % / 10,94 % actual y 40,62 % / 47,66 % / 11,51 % a 3×. El mínimo por nodo para N+1 y 3× es 13 vCPU, 31 GB RAM y 221 GB de OSD. Concepción dispone de 16 hilos, 32 GB RAM y 3,84 TB útiles de RAID 10; utiliza 75,00 % / 53,12 % / 3,65 % actual y 75,00 % / 56,25 % / 3,65 % a 3×.

La energía de los gabinetes de borde y de piso se calcula con el método de la carga de TI de Talca: los servidores cuentan la potencia de placa de sus dos fuentes y los demás equipos, su consumo máximo de ficha; se agrega un margen de crecimiento de 20 %, se convierte a potencia aparente con factor de potencia 0,95 y se exige que la UPS no supere el 80 % de uso. La ONT y el router LTE del operador quedan cubiertos por el margen, igual que en Talca.

<a id="tab:anexo-4b-ups-borde"></a>

**Tabla A.35 — Carga y UPS de los gabinetes de borde y de piso**

| **Gabinete** | **Equipos y potencia** | **Carga de diseño** | **UPS y uso** |
| --- | --- | --- | --- |
| Borde de Concepción | Servidor 2 × 500 W; 2 firewalls × 150 W; 2 switches de núcleo × 150 W; Starlink 100 W; gateway IoT 10 W; total 1.710 W | 2.052 W; 2,16 kVA | 3 kVA; 72 % |
| Piso de Talca y de Concepción | Switch de acceso con fuente de 600 W, que incluye 370 W de PoE para los puntos de acceso; impresora de andén 98 W; total 698 W | 838 W; 0,88 kVA | 1,5 kVA; 59 % |
| Borde de cross-docking | Mini-PC 45 W; 2 firewalls × 24 W; 2 switches × 18,96 W; 2 puntos de acceso PoE+ × 30 W; Starlink 100 W; total 291 W | 349 W; 0,37 kVA | 0,75 kVA; 49 % |

Fuente: elaboración propia; consumos según la ficha técnica de cada modelo de referencia del Formulario T-11.

En los tres casos la UPS requerida, que es la carga de diseño dividida por 0,8, queda bajo la capacidad ofertada: 2,70, 1,10 y 0,46 kVA. Cada UPS lleva baterías para 30 minutos a su carga de diseño. Los consumos declarados del servidor de Concepción y del mini-PC satisfacen RT-08.01 (Bases Técnicas Transversales, cap. 8, p. 18).

## 4-W.9 Capacidad en nube

<a id="sec:anexo-4b-nube"></a>

El perfil de API atiende aplicaciones y portales N-01 a N-03. Una tarea Fargate entrega 0,70 ÷ 0,05 = **14,00 solicitudes/s**. La tabla de carga es: régimen, 12,34 solicitudes/s de nube más portal y 2 tareas; peak, 14,66 y 2; RT-09.06 (Bases Técnicas Transversales, cap. 9, p. 21), 21,99 y 2; cota extrema, 5,03 + 43,33 = 48,37 y 4. La sensibilidad de 120 solicitudes por sesión conserva las sesiones repartidas en la hora: 2,71 + 19,26 = 21,97 y 2 tareas en régimen; 5,03 + 86,67 = 91,70 y 7 tareas en cota. Todos los casos quedan bajo el techo de 8 tareas.

Aurora se dimensiona con la misma cota que la API, para que la base no sea el límite de un escenario que la API admite. Como cota, cada solicitud consume en la base los mismos 50 ms de CPU que en la aplicación, sin descontar la parte que atiendan el lector o la caché. Así se cubre también la falla del lector, cuando el escritor recibe toda la carga. La carga de nube a 3×, 43,98 solicitudes/s, exige 43,98 × 0,05 ÷ 0,70 = 3,14 vCPU. La cota extrema con la cuota del canal tradicional, 91,70 + 20 = 111,70 solicitudes/s, exige 111,70 × 0,05 = 5,59 vCPU, que sobre 8 vCPU es un uso de 69,8 %, bajo el 70 %. Se adopta db.r6g.2xlarge, de 8 vCPU y 64 GiB, para el escritor y el lector de sa-east-1 y para la instancia de us-east-1, que hereda la carga al conmutar. El peak actual, 14,66 × 0,05 = 0,73 vCPU, cabría en una instancia menor, pero cambiar de clase exigiría intervenir en el congelamiento de septiembre (ADR-12). Por eso la capacidad queda fija desde el inicio y se verifica en la prueba RT-09.06 (Bases Técnicas Transversales, cap. 9, p. 21), midiendo la mezcla real de lecturas y escrituras.

## 4-W.10 Crecimiento, enlaces y ventana dominical

<a id="sec:anexo-4b-crecimiento"></a>

La proyección de año 3 del numeral 14.1 de las Bases Técnicas del caso (cap. 14, p. 24) es 36.000 pedidos, 305.000 líneas, 1.650 entregas normales, 3.100 entregas peak y 40.000 DTE mensuales. Cada componente usa una base distinta:

- WMS Talca = 2,68 × (305.000 ÷ 260.000) = 3,15 TPS.
 
- Nube más portal = 14,66 × (36.000 ÷ 31.000) = 17,03 solicitudes/s.
 
- Evidencia = 87,72 × (36.000 ÷ 31.000) = 101,87 GB/año.
 
- Enlace de Talca = 5,20 Mbps a año 3 y 5,64 Mbps a 3×.
 
- Terminales de bodega de Talca = (23 + 3) de congelado + (113 + 12) estándar = 151.
 
- Mesa = 2.000 × (350 ÷ 310) = 2.258 contactos/mes.

Por separado, RT-09.03 (Bases Técnicas Transversales, cap. 9, p. 21) exige 3×: 93.000 pedidos, 780.000 líneas, 4.200/7.800 entregas y 102.000 DTE mensuales.

<a id="tab:anexo-4b-plan"></a>

**Tabla A.36 — Plan de capacidad**

| **Componente** | **Año 1** | **Año 3** | **3×** | **Acción** |
| --- | --- | --- | --- | --- |
| WMS de Talca, TPS peak | 2,68 | 3,15 | 8,05 | Revisar CPU e IOPS trimestralmente |
| Cada cross-docking, TPS peak | 2,17 | 2,58 | 6,50 | Revisar CPU e IOPS trimestralmente |
| Nube, TPS peak / tareas | 14,66 / 2 | 17,03 / 2 | 43,98 / 4 | Escalamiento y prueba trimestral |
| Evidencia anual | 87,72 GB | 101,87 GB | 263,16 GB | Escalar S3 y retención |
| Enlace de Talca, peor caso | 5,16 Mbps | 5,20 Mbps | 5,64 Mbps | Ampliar D-03 si p95 supera la cota |
| Terminales de bodega de Talca | 132 | 151 | no aplica | Ajustar parque a la dotación |
| Mesa, contactos mensuales | 2.000 | 2.258 | 6.000 | Recalibrar Erlang C |

La prueba RT-09.06 (Bases Técnicas Transversales, cap. 9, p. 21) usa una sola multiplicación: 14,66 × 1,5 = 21,99 TPS. Las tareas, colas y almacenamiento en nube escalan por política; la reserva N+1, la Wi-Fi y los enlaces se amplían mediante revisión planificada.

## 4-W.11 Umbrales de quiebre y cuello de botella

<a id="sec:anexo-4b-umbrales"></a>

La sensibilidad de SV-04 antes de alcanzar la capacidad CPU calculada es Talca 333,73×, Concepción 166,87×, cada cross-docking 12,92× y nube más portal 7,64×. La peor ruta exige 0,13 Mbps efectivos y la hora punta de retorno exige 1,40 Mbps agregados.

La emisión tributaria es el primer candidato a cuello de botella: tratar los 2.852 DTE peak como guías admite 9,47 segundos cada una en la preparación completa, 4,42 segundos al final del turno y 1,89 segundos en la ventana actual. Se observan guías aún no emitidas frente a la salida, tiempo del ERP, cola, base WMS, IOPS, Wi-Fi y drenaje en percentil 95. La degradación controlada encola con clave idempotente, aplica límite de tasa y muestra un mensaje explícito; el ERP sigue siendo el único emisor.

## 4-W.12 Pruebas de carga, estrés y operación

<a id="sec:anexo-4b-pruebas"></a>

La carga RT-09.06 (Bases Técnicas Transversales, cap. 9, p. 21) se ejecuta a **21,99 TPS totales**, distribuidos por lugar según el perfil horario, sin multiplicar cada lugar por separado. El estrés que exige el mismo RT-09.06 (Bases Técnicas Transversales, cap. 9, p. 21) supera la cota extrema del portal y la volumetría 3×. La prueba de corte dura 24 horas y debe drenar en dos; la sincronización de la peor ruta debe completar en diez minutos. Se ejecutan dos ensayos de migración conforme a RT-05.13 (Bases Técnicas Transversales, cap. 5, p. 12) y una verificación de la ventana dominical para cada sitio.

Se conservan percentil 95, utilización, colas, errores, pérdida o duplicación, estado de conciliación y parámetros confirmados. El perfil horario, la migración y la operación dominical se cierran con evidencia de prueba, sin convertir el resultado medido en un hecho previo.

## Referencias

- Angular. (2026a). *Release policy*. <https://angular.dev/reference/releases>

- Angular. (2026b). *Version compatibility*. <https://angular.dev/reference/versions>

- International Organization for Standardization. (2022a). *ISO/IEC/IEEE 42010:2022: Software, systems and enterprise—Architecture description*. <https://www.iso.org/standard/74393.html>

- International Organization for Standardization. (2022b). *ISO/IEC 27001:2022*. <https://www.iso.org/standard/27001>

- International Organization for Standardization. (2022c). *ISO/IEC 27002:2022*. <https://www.iso.org/standard/75652.html>

- Laravel. (2026). *Release notes*. <https://laravel.com/framework/docs/releases>

- Ley N.° 21.719. (2024). *Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales*. Diario Oficial de la República de Chile.

- National Institute of Standards and Technology. (2020). *Zero trust architecture* (Special Publication 800-207). U.S. Department of Commerce. <https://doi.org/10.6028/NIST.SP.800-207>

- PHP. (2026). *Supported versions*. <https://www.php.net/supported-versions.php>

- Pontificia Universidad Católica de Valparaíso. (2026a). *Bases técnicas del caso 02—Logística: Distribuidora Puelche S.A.* (Licitación N.° TFEP-01/2026).

- Pontificia Universidad Católica de Valparaíso. (2026b). *Bases técnicas transversales* (Licitación N.° TFEP-01/2026).

- Pontificia Universidad Católica de Valparaíso. (2026c). *Bases administrativas* (Licitación N.° TFEP-01/2026).

- PostgreSQL. (2026). *Versioning policy*. <https://www.postgresql.org/support/versioning/>

- RabbitMQ. (2026). *Release information*. <https://www.rabbitmq.com/release-information>

- Servicio de Impuestos Internos. (2018). *Oficio 781: acuse de recibo*. <https://www.sii.cl/normativa_legislacion/jurisprudencia_administrativa/ley_impuesto_ventas/2018/ja781.htm>

- Servicio de Impuestos Internos. (s. f.-a). *Representación de guía de despacho electrónica*. <https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6599.htm>

- Servicio de Impuestos Internos. (s. f.-b). *Formato de recibos*. <https://www.sii.cl/factura_electronica/desc_19983.pdf>

- Servicio de Impuestos Internos. (s. f.-c). *Contingencia de emisión*. <https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6624.htm>

## Declaración de uso de IA

OpenAI Codex asistió la organización de los catálogos, redacción, cálculos de escenario y verificación de consistencia de estos anexos. La revisión humana final se realizará sobre el consolidado: las filas registran ese estado sin atribuir una aprobación inexistente. No se generaron nuevos diagramas dentro de estos anexos.

<a id="tab:uso-ia-anexos"></a>

**Tabla A.37 — Uso de IA en los anexos lógicos**

| **Anexo** | **Herramienta** | **Finalidad** | **Texto** | **Diagramas** | **Revisión humana** |
| --- | --- | --- | --- | --- | --- |
| A | Codex | Eventos canónicos. | Alto | Ninguno | No realizada. |
| B | Codex | Gobierno de integración. | Alto | Ninguno | No realizada. |
| C | Codex | Carga masiva. | Alto | Ninguno | No realizada. |
| D | Codex | Módulos y responsabilidades. | Alto | Ninguno | No realizada. |
| E | Codex | Trazabilidad funcional. | Alto | Ninguno | No realizada. |
| F | Codex | Límites de contexto. | Alto | Ninguno | No realizada. |
| G | Codex | Interfaces internas. | Alto | Ninguno | No realizada. |
| H | Codex | Interfaces externas. | Alto | Ninguno | No realizada. |
| I | Codex | Cálculos de volumen. | Alto | Ninguno | No realizada. |
| J | Codex | Funciones offline. | Alto | Ninguno | No realizada. |
| K | Codex | Reconciliación. | Alto | Ninguno | No realizada. |
| L | Codex | Decisiones del caso. | Alto | Ninguno | No realizada. |
| M | Codex | Protocolos de aceptación. | Alto | Ninguno | No realizada. |
| N | Codex | Correspondencia lógica. | Alto | Ninguno | No realizada. |
| O | Codex | Especificación y trazabilidad. | Alto | Ninguno | No realizada. |
| P | Codex | Especificación y trazabilidad. | Alto | Ninguno | No realizada. |
| Q | Codex | Especificación y trazabilidad. | Alto | Ninguno | No realizada. |
| R | Codex | Especificación y trazabilidad. | Alto | Ninguno | No realizada. |
| S | Codex | Especificación y trazabilidad. | Alto | Ninguno | No realizada. |
| T | Codex | Especificación y trazabilidad. | Alto | Ninguno | No realizada. |
| U | Codex | Especificación y trazabilidad. | Alto | Ninguno | No realizada. |
| V | Codex | Especificación y trazabilidad. | Alto | Ninguno | No realizada. |

Fuente: registro de elaboración asistida; debe consolidarse con la revisión humana y el Formulario A-6 antes de presentar la oferta.

**Detalle por apartado del cuerpo**

La herramienta es OpenAI Codex en todas las filas. La revisión humana corresponde al consolidado; no se asigna una firma o resultado inexistente.

<a id="tab:ia-apartados"></a>

**Tabla A.38 — Declaración por apartado lógico**

| **Apartado** | **Finalidad** | **Texto** | **Diagramas** | **Revisión** |
| --- | --- | --- | --- | --- |
| 4.1.1 | especificaciones tecnologias de software a utilizar | Alto | No aplica | No realizada. |
| 4.1.2 | principios de integracion | Alto | No aplica | No realizada. |
| 4.1.3 | capas de la arquitectura | Alto | Alto, con modelo del equipo | No realizada. |
| 4.1.4 | modulos funcionales y limites de contexto | Alto | No aplica | No realizada. |
| 4.1.5 | modelo de datos conceptual | Alto | No aplica | No realizada. |
| 4.1.6 | catalogo de interfaces | Alto | No aplica | No realizada. |
| 4.1.7 | detalle de tecnologias seleccionadas | Alto | No aplica | No realizada. |
| 4.1.8 | implantacion progresiva del backend laravel | Alto | No aplica | No realizada. |
| 4.1.9 | ambientes del ciclo de vida y promocion de componentes | Alto | No aplica | No realizada. |
| 4.1.10 | patrones de diseno y continuidad | Alto | No aplica | No realizada. |
| 4.1.11 | registro de decisiones de arquitectura | Alto | No aplica | No realizada. |
| 4.1.12 | puntos unicos de falla y riesgos residuales | Alto | No aplica | No realizada. |
| 4.1.13 | comparacion de alternativas arquitectonicas | Alto | No aplica | No realizada. |
| 4.1.14 | relacion entre las vistas de arquitectura | Alto | No aplica | No realizada. |
| 4.1.15 | funciones disponibles y no disponibles sin conexion | Alto | No aplica | No realizada. |
| 4.1.16 | reglas de reconciliacion | Alto | No aplica | No realizada. |
| 4.1.17 | articulacion entre prueba de entrega dte y acuse | Alto | No aplica | No realizada. |
| 4.1.18 | identidad y ciclo de vida de conductores externos | Alto | No aplica | No realizada. |
| 4.1.19 | primer cuello de botella bajo la carga de septiembre | Alto | No aplica | No realizada. |
| 4.1.20 | decisiones del numeral 16 1 del caso | Alto | No aplica | No realizada. |
| 4.1.21 | condiciones y supuestos de diseno | Alto | No aplica | No realizada. |
