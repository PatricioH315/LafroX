<a id="anexo-seccion-1"></a>

# Anexos del Subdocumento 4.1

[Cuerpo del Subdocumento 4.1](LAFROX-Subdocumento4.1.md) · [Procedencia y conversión](MANIFIESTO.md)

## Índice

- [Catálogo de anexos y trazabilidad](#anexo-seccion-2)
- [Anexo 4.1-A — Catálogo de eventos canónicos](#anexo-seccion-3)
- [Anexo 4.1-B — Gobierno de la integración](#anexo-seccion-4)
- [Anexo 4.1-C — Escenarios de carga masiva](#anexo-seccion-5)
- [Anexo 4.1-D — Matriz de los doce módulos](#anexo-seccion-6)
- [Anexo 4.1-E — Trazabilidad funcional](#anexo-seccion-7)
- [Anexo 4.1-F — Mapa de límites de contexto](#anexo-seccion-8)
- [Anexo 4.1-G — Catálogo de interfaces internas](#anexo-seccion-9)
  - [Parámetros comunes del catálogo](#anexo-seccion-10)
- [Anexo 4.1-H — Catálogo de interfaces externas](#anexo-seccion-11)
  - [Condiciones de servicio de las contrapartes](#anexo-seccion-12)
- [Anexo 4.1-I — Volumen de mensajes](#anexo-seccion-13)
- [Anexo 4.1-J — Funciones sin conexión](#anexo-seccion-14)
- [Anexo 4.1-K — Reglas de reconciliación](#anexo-seccion-15)
- [Anexo 4.1-L — Decisiones del numeral 16.1](#anexo-seccion-16)
- [Anexo 4.1-M — Verificación de continuidad lógica](#anexo-seccion-17)
  - [AL-DTE-01. Salida de 96 camiones y falla del emisor](#anexo-seccion-18)
  - [AL-DR-01. Pérdida de sitio durante una caída WAN](#anexo-seccion-19)
  - [AL-OFF-01. Autonomía de 24 horas con dos relevos](#anexo-seccion-20)
- [Anexo 4.1-N — Correspondencia de componentes lógicos](#anexo-seccion-21)
  - [Inventario trazable de capacidades transversales](#anexo-seccion-22)
- [Anexo 4.1-O — Decisiones de arquitectura lógica](#anexo-seccion-23)
  - [ADR-01. Núcleo y límites de módulo](#anexo-seccion-24)
  - [ADR-04. Persistencia por responsabilidad](#anexo-seccion-25)
  - [ADR-05. Mensajes canónicos y trabajos internos](#anexo-seccion-26)
  - [ADR-06. Identidad y relevo local](#anexo-seccion-27)
  - [ADR-07. Movilidad](#anexo-seccion-28)
  - [ADR-08. Sustitución del WMS](#anexo-seccion-29)
  - [ADR-11. EDI y frontera ERP](#anexo-seccion-30)
  - [ADR-12. Aislamiento y capacidad](#anexo-seccion-31)
  - [ADR-13. Publicación y autorización](#anexo-seccion-32)
  - [ADR-14. Observabilidad](#anexo-seccion-33)
  - [ADR-L01. Liberación documental](#anexo-seccion-34)
  - [ADR-L02. Protección fuera del sitio](#anexo-seccion-35)
- [Anexo 4.1-P — Tecnologías, soporte y actualización](#anexo-seccion-36)
  - [Implementación compatible del backend](#anexo-seccion-37)
- [Anexo 4.1-Q — Modelado de amenazas lógicas](#anexo-seccion-38)
- [Anexo 4.1-R — Controles de seguridad y evidencia](#anexo-seccion-39)
- [Anexo 4.1-S — Puntos de vista y correspondencias](#anexo-seccion-40)
- [Anexo 4.1-T — Desempeño y aceptación lógica](#anexo-seccion-41)
- [Anexo 4.1-U — Prueba de entrega, guía y acuses](#anexo-seccion-42)
  - [Mecanismo de recepción propuesto](#anexo-seccion-43)
- [Anexo 4.1-V — Condiciones de aceptación y dependencias](#anexo-seccion-44)
- [Referencias](#anexo-seccion-45)
- [Declaración de uso de IA](#anexo-seccion-46)
  - [Detalle por apartado del cuerpo](#anexo-seccion-47)


Estos anexos reúnen los catálogos y matrices de detalle citados en el apartado 4.1. El cuerpo principal conserva la explicación de las decisiones y sus consecuencias operativas.

<a id="anexo-seccion-2"></a>

## Catálogo de anexos y trazabilidad

Este catálogo reúne los 22 anexos del apartado 4.1. La primera columna enlaza a su evidencia y lleva a su sección de inicio. El identificador se conserva aunque cambie el orden de presentación. Las referencias desde el cuerpo deben usar la letra del anexo y, cuando corresponda, el identificador de contrato, módulo, decisión o ensayo.

<a id="tab-catalogo-anexos"></a>

**Tabla A.1 — Lista completa de anexos de arquitectura lógica**

| **Anexo / enlace** | **Evidencia** | **Requisito de referencia** |
| --- | --- | --- |
| [A](#anx-a) | Catálogo de eventos canónicos | RT-02.06/07 |
| [B](#anx-b) | Gobierno de la integración | RT-05.16/17 |
| [C](#anx-c) | Escenarios de carga masiva | RT-05.22 |
| [D](#anx-d) | Matriz de los doce módulos | RT-02.02 |
| [E](#anx-e) | Trazabilidad funcional | T12 / capítulo 4 |
| [F](#anx-f) | Mapa de límites de contexto | RT-02.02/13 |
| [G](#anx-g) | Catálogo de interfaces internas | RT-05.21 |
| [H](#anx-h) | Catálogo de interfaces externas | RT-05.21; RT-10.08 |
| [I](#anx-i) | Volumen de mensajes | RT-09.01 |
| [J](#anx-j) | Funciones sin conexión | RT-03.10/13 |
| [K](#anx-k) | Reglas de reconciliación | RT-02.06; RT-03.12 |
| [L](#anx-l) | Decisiones del numeral 16.1 | Caso, numeral 16.1 |
| [M](#anx-m) | Verificación de continuidad lógica | RT-03.10; RT-07.04 |
| [N](#anx-n) | Correspondencia de componentes lógicos | Aclaraciones, capítulo 4 |
| [O](#anx-o) | Decisiones de arquitectura lógica | RT-02.04 |
| [P](#anx-p) | Tecnologías, soporte y actualización | Bases, 1.6 |
| [Q](#anx-q) | Modelado de amenazas lógicas | RT-11.02 |
| [R](#anx-r) | Controles de seguridad y evidencia | RT-11.05/06 |
| [S](#anx-s) | Puntos de vista y correspondencias | RT-02.03 |
| [T](#anx-t) | Desempeño y aceptación lógica | RT-09.01–08 |
| [U](#anx-u) | Prueba de entrega, guía y acuses | RT-16.14 |
| [V](#anx-v) | Condiciones de aceptación y dependencias | RT-07.04; RT-10.08 |

Para seguir una decisión de stock, consultar M2 en D, INT-01 en G, reconciliación en K y desempeño en T. Para seguir un despacho, consultar M5 en D, INT-07 en H, estados documentales en U y aceptación en V. N y S permiten cotejar esas responsabilidades con las capacidades del capítulo 3 y la realización física, sin atribuir a esta vista una integración todavía no validada.

<a id="anexo-seccion-3"></a>

## Anexo 4.1-A — Catálogo de eventos canónicos

<a id="anx-a"></a>

El detalle de catálogo de eventos canónicos se presenta a continuación.

<a id="tab-eventos-canonicos"></a>

**Tabla A.2 — Eventos canónicos del dominio**

| **Evento** | **Productor** | **Consumidores** | **Clave de partición** | **Origen en el caso / Decisión** |
| --- | --- | --- | --- | --- |
| RecepcionConfirmada | M1 | M2, M9, ACL→ERP | site_id | Cap. 9.5: retiro sanitario < 2 h |
| StockReservado / ReservaLiberada | M2 | M3, M5 | sku_id | Decisión 16.1 N° 8: doble compromiso stock |
| PedidoConfirmado | M3 | M4, M5, M7, M11 | pedido_id | M11 traduce la entrada EDI; M3 confirma el pedido |
| MisionPreparada | M5 | M6, ACL→ERP | pedido_id | Cierra ciclo bodega a andén |
| EntregaRegistrada | M6 | M7, M8, M10, ACL | entrega_id | Decisión 16.1 N° 1: entrega cumplida / OTIF |
| DevolucionRegistrada | M8 | M2, M7, M10 | entrega_id | Decisión 16.1 N° 12: efecto sobre DTE emitido |
| EnvaseMovido | M8 | M2, M10 | cliente_id | Decisión 16.1 N° 10: 68.000 canastillos, 9.400 pallets, 14% pérdida |
| ExcursionTermicaDetectada | M9 (borde) | M5 (bloqueo), M10, alertas | shipment_id | Decisión 16.1 N° 4: bloqueo local < 5 s |
| RendicionCerrada | M7 | M10, ACL→ERP | conductor_id | Control efectivo que circula en ruta |
| DesviacionDeRutaDetectada | M12 | M10, M9 | ruta_id | Costo de servir; no control de jornada. |

 Fuente: elaboración propia de LafroX a partir de Caso 02, flujos operativos y numeral 16.1.

<a id="anexo-seccion-4"></a>

## Anexo 4.1-B — Gobierno de la integración

<a id="anx-b"></a>

El detalle de gobierno de la integración se presenta a continuación.

<a id="tab-gobierno-integracion"></a>

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

 Fuente: elaboración propia de LafroX a partir de Bases Técnicas Transversales, RT-02 y RT-05.

<a id="anexo-seccion-5"></a>

## Anexo 4.1-C — Escenarios de carga masiva

<a id="anx-c"></a>

El detalle de escenarios de carga masiva se presenta a continuación.

<a id="tab-carga-masiva"></a>

**Tabla A.4 — Escenarios de carga y descarga masiva (RT-05.22)**

| **Escenario** | **Mecanismo** | **Control y auditoría** |
| --- | --- | --- |
| Carga inicial maestros/históricos (ERP, WMS) | ETL por lotes, inserción idempotente por UUID, ventana sin operación | Conteo previo/posterior por lote, conciliación totales, bitácora carga (quién, cuándo, lote, resultado); rechazados → cuarentena + reproceso |
| Descarga regulatoria (traza lote, temperaturas, DTE, geo) | Exportación asíncrona CSV/Parquet, firmada, checksum | Registro extracción (solicitante, filtro, resultado); control acceso datos sensibles (RT-16.09) |
| Sincronización masiva turno (terreno) | Sincronizadores con partición + reanudación + deduplicación; medios a S3 por objeto | Nivel servicio: turno completo ≤ 10 min; métricas sync en Capa 8 |
| Interfaces periódicas con terceros | Colas con `batch_id` + confirmación por lote | Monitoreo DLQ + acuse por lote en bandeja excepciones |

 Fuente: elaboración propia de LafroX a partir de Bases Técnicas Transversales, RT-05.22.

<a id="anexo-seccion-6"></a>

## Anexo 4.1-D — Matriz de los doce módulos

<a id="anx-d"></a>

El detalle de matriz de los doce módulos se presenta a continuación.

<a id="tab-modulos-funcionales"></a>

**Tabla A.5 — Módulos, responsabilidades e interlocutores**

| **Módulo / RF** | **Responsabilidad** | **Interfaz principal** | **Actor principal** | **Etapa** |
| --- | --- | --- | --- | --- |
| M1 Recepción / RF-01 | Lote y recepción GS1. | Evento a M2; ACL con ERP. | Recepcionista; proveedor. | 1 |
| M2 Inventario / RF-02 | Stock, reserva y FEFO. | Consulta de M3/M5. | Jefatura de bodega. | 1 |
| M3 Preventa / RF-03 | Pedido y precio informado. | Reserva en M2; sincronización. | Preventista. | 1 |
| M4 Rutas / RF-04 | Secuencia y restricciones. | Ruta aprobada a M6. | Planificador. | 1 |
| M5 Preparación / RF-05 | Misión y carga confirmada. | Evento a M6; guía vía ACL. | Preparador; jefatura. | 1 |
| M6 Reparto / RF-06 | Entrega y POD. | Evento a M7/M8. | Conductor propio o externo. | 1 |
| M7 Rendición / RF-07 | Cobro y descuadre. | ACL al ERP; evento a M10. | Conductor; Tesorería. | 1 |
| M8 Devoluciones / RF-08 | Retorno y saldo de envases. | Evento a M2/M7. | Conductor; bodega. | 1 |
| M9 Calidad / RF-09 | Lote, frío y bloqueo. | Bloqueo a M5; alerta. | Jefatura de Calidad. | 1 |
| M10 Analítica / RF-11 | OTIF y costo de servir. | Consume eventos sin escribir. | Gerencias. | 2 |
| M11 Canal moderno / RF-12 | Pedido EDI y excepciones. | Contrato por cadena; M3. | Cadena; equipo comercial. | 2 |
| M12 Flota / RF-14 | Ruta real y desviación. | GPS a M4/M10. | Planificador; flota. | 2 |

 Fuente: elaboración propia de LafroX a partir de Caso 02, requerimientos funcionales y alcance del capítulo 3.

<a id="anexo-seccion-7"></a>

## Anexo 4.1-E — Trazabilidad funcional

<a id="anx-e"></a>

El detalle de trazabilidad funcional se presenta a continuación.

<a id="tab-traza-logica"></a>

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
| RF-14 | M12 Flota | 2, 4 y 5 | Ruta real correlacionada. |

 Fuente: elaboración propia de LafroX a partir del catálogo funcional del caso y las responsabilidades definidas en la Tabla [A.5](#tab-modulos-funcionales).

<a id="anexo-seccion-8"></a>

## Anexo 4.1-F — Mapa de límites de contexto

<a id="anx-f"></a>

El detalle de mapa de límites de contexto se presenta a continuación.

<a id="tab-context-mapping"></a>

**Tabla A.7 — Mapa de límites de contexto**

| **Dueño** | **Relación** | **Interlocutor** | **Contrato** | **Límite** |
| --- | --- | --- | --- | --- |
| M1 Recepción | Traducción por ACL | ERP 2017 | Recepción validada. | ERP no escribe lote. |
| M2 Inventario | Servicio publicado | M3, M4 y M5 | Consulta y reserva. | M2 decide stock. |
| M3 Preventa | Cliente de M2 | M2 y M7 | Pedido y sincronización. | No aprueba crédito local. |
| M4 Rutas | Adapta fuente | M3, M6 y GIS | Ruta aprobada. | GIS no decide ruta. |
| M5 Preparación | Proveedor de evento | M2, M6 y ACL | Misión preparada. | No emite guía. |
| M6 Reparto | Proveedor de evento | M4, M7 y M8 | Entrega registrada. | No liquida cobro. |
| M7 Rendición | Traducción por ACL | M6 y ERP | Rendición aprobada. | ERP sigue tributario. |
| M8 Devoluciones | Lenguaje publicado | M2 y M7 | Devolución y envase. | No ajusta DTE. |
| M9 Calidad | Proveedor de bloqueo | M1, M5 y sensores | Lote bloqueado. | Calidad libera. |
| M10 Analítica | Consumidor de eventos | M1–M9 y M12 | Indicadores consolidados. | Solo lectura. |
| M11 Canal moderno | Traducción EDI | Cadena, M3 y ACL | Pedido normalizado. | M3 gobierna pedido. |
| M12 Flota | Adapta telemetría | GPS, M4 y M10 | Ruta observada. | No registra entrega. |

 Fuente: elaboración propia de LafroX a partir de Caso 02 y responsabilidades de M1–M12 definidas en esta sección.

<a id="anexo-seccion-9"></a>

## Anexo 4.1-G — Catálogo de interfaces internas

<a id="anx-g"></a>

El catálogo conserva los identificadores de las ocho interfaces internas. Las fichas que siguen completan el modo, volumen, ventana y conducta ante lentitud exigidos por RT-05.21. Los volúmenes son escenarios de diseño, no mediciones. Un mensaje de negocio puede atravesar varias interfaces: sus cifras no se suman como operaciones únicas.

<a id="tab-catalogo-internas"></a>

**Tabla A.8 — Integraciones internas: dueño, contrato y continuidad**

| **ID** | **Intercambio** | **Dueño** | **Contrato** | **Falla** |
| --- | --- | --- | --- | --- |
| INT-01 | Pedido preventa y consulta. | M3 | API negocio y sync. | Captura local pendiente. |
| INT-02 | Entrega, POD y cobro. | M6/M7/M8 | API sync por lote. | Cola en dispositivo. |
| INT-03 | Eventos bodega a nube. | M2/M5 | Eventos por sitio. | Broker local 24 h. |
| INT-04 | Detalle cross-dock a Talca. | M2 | Evento de inventario. | Buffer y reconciliación. |
| INT-05 | Eventos de temperatura. | M9 | Evento de excursión. | Bloqueo local. |
| INT-12 | Cambios de datos a réplica. | M2 | CDC de bodega. | Desfase medido; reanudar. |
| INT-13 | Identidad a sitio. | Seguridad | Políticas firmadas. | Asignaciones vigentes. |
| INT-14 | Métricas y trazas. | Operación | OTLP. | Buffer local. |

 Fuente: elaboración propia de LafroX a partir de Diseño lógico LafroX, con base en RT-02.06 y RT-03.12.

<a id="anexo-seccion-10"></a>

### Parámetros comunes del catálogo

Los contratos distinguirán aceptación durable de procesamiento concluido. Como valores iniciales de diseño, las consultas interactivas tendrán espera máxima de 5 segundos y las transferencias de lotes, 30 segundos; un timeout produce estado incierto, nunca aprobación. Los reintentos conservan UUID, aplican espera exponencial con dispersión y máximo de 5 minutos entre intentos. Los errores de validación pasan a excepción sin reintento automático. El agotamiento del presupuesto de intentos deriva a una cola de errores con alerta; no elimina la operación. Estos parámetros se ajustarán con la prueba de carga sin relajar los tiempos de negocio exigidos.

**INT-01. Preventa y consultas — M3.**

Modo mixto: consultas síncronas y captura/sincronización asíncrona. Base de escrituras: 31.000/25=1.240 pedidos/día; escenario peak de diseño: 2.480. Para lectura se supone inicialmente cuatro consultas por pedido: 4.960/9.920 llamadas/día; se mide por separado del pedido. Contraparte: API central, ventana requerida 24×7; la app conserva 14 horas de trabajo. Dentro de 2 segundos, si no hay respuesta vigente, muestra la copia fechada; no confirma reserva ni crédito. Lotes de sincronización esperan hasta 30 segundos y se reenvían con la misma clave. La confirmación final corresponde a M2/M3 y al control de crédito.

**INT-02. Reparto, POD y rendición — M6/M7/M8.**

Modo asíncrono para evidencia y rendición; consulta de resultado síncrona. Base mínima: 1.400/2.600 entregas diarias (caso, cap. 14). Se supone inicialmente un sobre POD, uno de cobro y uno de devolución/envases por entrega: hasta 4.200/7.800 sobres/día; los eventos no aplicables no se emiten. Fotografías y firmas viajan como objetos con hash, separados del mensaje. Contraparte: API y almacenamiento central, requeridos 24×7. Timeout de lote: 30 segundos. La cola cifrada del dispositivo conserva el turno de 14 horas; solo elimina el pendiente después de confirmar mensaje y objetos completos. No registra pago autorizado por ausencia de respuesta del POS.

**INT-03. Eventos de bodega a nube — M1/M2/M5/M9.**

Modo asíncrono mediante outbox, RabbitMQ y consumidor canónico. Sobre de diseño: 260.000/25\times5=52.000 eventos/día; peak conservador: 104.000. Es el total de trazabilidad de los sitios, no una carga adicional por sitio. Contraparte: ingesta central, requerida 24×7. Sin acuse en 30 segundos, el productor retiene y reintenta; el acuse del broker no sustituye el acuse transaccional del dominio. Se conserva al menos 24 horas de actividad local y se mide la edad del pendiente más antiguo. El consumidor deduplica por sitio y UUID antes de actualizar el dominio.

**INT-04. Cross-docking a Talca — M2.**

Modo asíncrono. Su volumen es la fracción de INT-03 originada en Curicó, Chillán y Los Ángeles: V_04=f_CD V_03, con 0≤ f_CD\leq1. Hasta medir la distribución por sitio se ensaya el límite conservador 52.000/104.000 eventos/día para el conjunto; no se suma de nuevo al total de INT-03. Contraparte: consolidación de Talca, requerida 24×7. Timeout de acuse de 30 segundos; cada sitio mantiene su operación, buffer de 24 horas y secuencia propia. Al reconectar se reconcilia inventario en tránsito y se aísla cualquier doble compromiso.

**INT-05. Temperatura — M9.**

Modo asíncrono para muestras y alarma local inmediata. Escenario conservador común: (28+28)\times288=16.128 muestras/día, igual en régimen y peak, para 56 fuentes cada cinco minutos durante 24 horas. La variante con termógrafos solo 05:30–19:00 produciría 28\times288+28\times162=12.600; no se intercambian ambas cifras sin declarar la ventana de medición. Contraparte: IoT Core/ingesta central, requerida 24×7; el bloqueo M9–M5 permanece local y no espera a nube. Acuse remoto máximo de 30 segundos por lote. Gateway: retención de 24 horas; termógrafo: registro de toda la ruta, hasta 14 horas. Una pérdida de señal o lectura obsoleta genera una incidencia diferenciada de la excursión térmica.

**INT-12. Réplica de lectura del WMS de Talca — M2/Datos.**

Modo asíncrono CDC. El volumen físico depende del WAL y no equivale al número de eventos EPCIS. Para la prueba se usa V_WAL=N_T× b_WAL, donde N_T son cambios de Talca y b_WAL, bytes medidos por cambio. Como envolvente inicial, N_T\leq52.000/104.000 eventos/día y un supuesto de 10 KiB/evento dan 0,50/0,99 GiB/día; migraciones, índices y amplificación se miden aparte. No se adopta ese supuesto como tamaño demostrado del buffer. Contraparte: réplica Aurora de solo lectura, requerida 24×7. Se alerta al superar 5 minutos de retraso y se escala antes de 15; con WAN caída se conserva WAL dentro de capacidad, sin prometer RPO remoto cumplido. AL-DR-01 verifica el escenario de pérdida de sitio.

**INT-13. Identidad y manifiestos — Seguridad.**

Modo mixto: autenticación central síncrona y distribución asíncrona de manifiestos. Cinco sitios operativos por 24 renovaciones horarias dan 120 manifiestos/día; no aumenta por duplicación de pedidos. Escenario de autenticaciones de diseño: 2×(310+62+200)=1.144 intentos/día, más accesos de portales a medir separadamente. Contraparte: Keycloak, requerida 24×7. Timeout interactivo: 5 segundos. Sin enlace se usa el verificador local con manifiesto de 26 horas, caché de identidad de 24 horas y permisos de turno de 8/14 horas. No se habilitan nuevas altas ni privilegios. AL-OFF-01 prueba dos relevos y el rechazo de identidades no preinscritas.

**INT-14. Métricas, logs y trazas — Operación.**

Modo asíncrono por OTLP. Presupuesto inicial para carga: cinco sitios, veinte señales por sitio cada minuto: 5\times20\times1.440=144.000 muestras/día; igual en peak para métricas periódicas. Trazas: muestreo inicial del 10% de INT-03, 5.200/10.400; logs: supuesto de dos registros por evento, 104.000/208.000. Son unidades diferentes, no mensajes comerciales sumables. Contraparte: colectores y CloudWatch, requeridos 24×7. Exportación con timeout de 30 segundos y buffer en disco de 24 horas. El fallo de exportación no bloquea negocio; el sitio mantiene alarma local por ocupación. Auditoría de negocio y eventos de seguridad no se descartan para conservar trazas diagnósticas.

 Fuente: elaboración propia; Caso 02, cap. 14, y RT-05.21. Las tasas de consultas, sobres, WAL y observabilidad son supuestos de ensayo explícitos; su calibración exige medición.

<a id="anexo-seccion-11"></a>

## Anexo 4.1-H — Catálogo de interfaces externas

<a id="anx-h"></a>

El detalle de catálogo de interfaces externas se presenta a continuación.

<a id="tab-catalogo-externas"></a>

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

 Fuente: elaboración propia de LafroX a partir de Caso 02 y Bases Técnicas Transversales, RT-05.

<a id="anexo-seccion-12"></a>

### Condiciones de servicio de las contrapartes

Las ventanas siguientes expresan la disponibilidad que requiere Puelche. El catálogo no atribuye un SLA no acreditado al ERP, SII, cadenas ni proveedores. Antes de habilitar cada integración se incorporarán al contrato su horario efectivo, mantenimientos, cuotas y escalamiento; una ventana inferior a la requerida se trata como brecha de aceptación. Los timeouts son parámetros iniciales del adaptador, sujetos a ensayo y al contrato de contraparte.

**INT-06. ERP 2017 — ACL/M7.**

Modo asíncrono para intercambio de negocio; consulta síncrona de estado cuando una escritura queda incierta. Volumen normal: 1.240+46+1.400+1.400+600=4.686 mensajes/día; peak de diseño: 9.372. Contraparte requerida 24×7, especialmente preparación 22:00–06:00 y despacho 05:30–07:00. Timeout de 10 segundos por llamada. Ante lentitud se abre cortacircuito, se conserva la solicitud y se prioriza despacho; ante respuesta perdida se consulta por clave externa antes de repetir. Un error funcional va a excepción. No se escribe directamente en tablas del ERP.

**INT-07. Emisión y estados DTE — ACL/M5.**

Modo síncrono para conocer el resultado documental antes de liberar salida, con seguimiento asíncrono de estados. Envolvente: 34.000/25\times2=2.720 mensajes/día incluyendo un acuse/estado por documento; peak de diseño: 5.440. Polling y reintentos se miden aparte. Contrapartes: emisor ERP y su canal SII; se requiere servicio durante preparación y disponibilidad sin interrupción para las 96 salidas de 05:30–07:00. Timeout de llamada: 10 segundos, sin equiparar timeout a rechazo o autorización. Resultado incierto obliga a consultar la misma solicitud. La cola no habilita salida sin documento; se aplica el control y el protocolo AL-DTE-01. El ERP sigue siendo el único emisor.

**INT-08. Cadenas del canal moderno — M11.**

Modo asíncrono EDI; el MDN es acuse de transporte, separado de la respuesta comercial. Supuesto: 136 pedidos/día por cuatro intercambios (pedido, confirmación, aviso y acuse): 544/1.088 mensajes/día. Contraparte requerida 24×7, con cortes de recepción y ventanas de entrega específicos de cada cadena, que deben figurar en su acuerdo. Timeout inicial de transporte: 30 segundos; MDN asíncrono esperado en 15 minutos como umbral de alerta propuesto, no SLA de la cadena. OpenAS2 conserva identificador y evidencia; M11 deduplica, valida equivalencias y deriva rechazo funcional a bandeja. Una entrega técnica no confirma el pedido ni permite superar su hora de corte.

**INT-09. Pasarela de pago — M7.**

Modo síncrono. Supuesto inicial: 500/1.000 autorizaciones/día; no es una cifra de adopción confirmada por el caso. Contraparte requerida 24×7, cubriendo el turno de reparto de hasta 14 horas. Timeout de 10 segundos. Si el resultado es incierto, se consulta por la misma clave antes de volver a cobrar. Sin respuesta no se registra autorización; se ofrece efectivo o crédito previamente aprobado según política del CLIENTE. Se concilia el resultado tardío para evitar cobro duplicado.

**INT-10. Mapas y geocodificación — M4.**

Modo síncrono para consultas y asíncrono para cálculos extensos. Supuesto: 200/400 llamadas/día, a calibrar por zonas, tamaño de matrices y recálculos. Contraparte requerida 24×7, con planificación previa a la salida y apoyo en ruta. Timeout de 5 segundos para consulta; trabajos largos tienen identificador y consulta de avance sin bloquear la API. Se conserva la ruta aprobada y cartografía precargada. La falta de proveedor impide nuevo cálculo que lo requiera, no borra la ruta vigente; cuotas o error 429 aplican espera informada.

**INT-11. Avisos al cliente — Notificaciones.**

Modo asíncrono mediante trabajos Laravel y SNS/API de canal. Dos avisos por entrega: 2.800/5.200 mensajes/día, a partir de 1.400/2.600 entregas. Contraparte requerida 24×7; las franjas permitidas de contacto se parametrizan por canal y cliente. Timeout de 10 segundos; reintento con clave de aviso y vigencia. Un aviso de ETA vencido se descarta con registro, no se envía al día siguiente. El estado enviado se distingue de recibido y no condiciona el registro de entrega. Falla persistente produce aviso operacional y canal alternativo acordado.

**INT-15. Telemetría de flota — M12.**

Modo asíncrono o extracción periódica de solo lectura según API existente. Base: 42\times120\times12=60.480 posiciones/día, una cada 30 segundos durante 12 horas; límite de prueba con 14 horas: 70.560. El aumento de pedidos no duplica por sí solo los 42 vehículos propios. Contraparte requerida 24×7 para conservar historial y cubrir turnos. Timeout de 10 segundos por consulta o 30 por lote; reanudación por cursor y deduplicación. Sin datos se muestra posición fechada y ruta prevista, nunca una posición presuntamente actual. La geolocalización no sustituye al POD.

 Fuente: elaboración propia; Caso 02, cap. 14, y RT-05.21. Los SLA de terceros requieren respaldo contractual; los supuestos de dimensionamiento se distinguen de la volumetría del caso.

<a id="anexo-seccion-13"></a>

## Anexo 4.1-I — Volumen de mensajes

<a id="anx-i"></a>

Esta síntesis permite contrastar órdenes de magnitud. Los anexos G y H son el catálogo por interfaz e identifican ventana, modo, unidades y supuestos. Las cifras siguientes incluyen flujos encadenados: no se suman para obtener transacciones únicas ni dimensionan por sí solas bytes de evidencia, WAL o ancho de banda. El peak depende de la variable que crece, no de duplicar todas las fuentes.

<a id="tab-volumen-mensajes"></a>

**Tabla A.10 — Volumen de mensajes por integración (derivado volumetría caso)**

| **Integración** | **Volumen régimen** | **Peak septiembre** | **Derivación** |
| --- | --- | --- | --- |
| Capa anticorrupción ERP (INT-06) | 4.686 msg/día | 9.372 | 1.240 + 46 + 1.400 + 1.400 + 600; peak de diseño por factor 2 |
| Documentos tributarios y acuse (INT-07) | 2.720 msg/día | 5.440 | 34.000 docs/mes por 2 intercambios, sobre 25 días |
| Eventos trazabilidad GS1 EPCIS | ≈ 52.000 eventos/día | ≈ 104.000 | 260.000 líneas/mes × 5 eventos ciclo, sobre 25 días |
| Telemetría cadena frío (INT-05) | 16.128 muestras/día | 16.128 | 56 fuentes por 288; envolvente de 24 h, no solo turno móvil |
| Telemetría flota (INT-15) | 60.480 posiciones/día | 70.560 | 42 camiones por 120 posiciones/h; turno de 12/14 h |
| Capturas terreno (INT-01/02) | Hasta 5.440 sobres/día | Hasta 10.280 | 1.240/2.480 pedidos más 3 sobres por 1.400/2.600 entregas; excluye picking local |
| EDI canal moderno (INT-08) | 544 msg/día | 1.088 | Supuesto de 136 pedidos por 4 intercambios; peak por factor 2 |
| Notificaciones (INT-11) | 2.800 msg/día | 5.200 | Dos avisos por 1.400/2.600 entregas |
| Autorización pago (POS móvil) | ≈ 500 msg/día | ≈ 1.000 | fracción canal tradicional que migra efectivo a electrónico |
| Servicio mapas y geocodificación | ≈ 200 llamadas/día | ≈ 400 | una corrida ruteo por zona + recálculos incidencia |

 Fuente: elaboración propia de LafroX a partir de Caso 02, numeral 14.1; cálculos indicados en la columna de derivación.

<a id="anexo-seccion-14"></a>

## Anexo 4.1-J — Funciones sin conexión

<a id="anx-j"></a>

El detalle de funciones sin conexión se presenta a continuación.

<a id="tab-funciones-offline"></a>

**Tabla A.11 — Funciones sin conexión y procedimiento de continuidad**

| **Función** | **Estado** | **Continuidad local** | **Al reconectar** |
| --- | --- | --- | --- |
| Pedido preventa | Captura 14 h | Precio y stock informativos; pedido pendiente. | M2 valida reserva y crédito. |
| Entrega y POD | Captura 14 h | Evidencia cifrada y cola persistente. | M6 confirma o abre excepción. |
| Recepción y preparación | Opera 24 h | Registro GS1 y bloqueo térmico local. | Eventos a nube y conciliación. |
| Cobro en efectivo | Captura 14 h | Comprobante y custodia según política. | M7 rinde y concilia. |
| Autorización POS | No disponible | Efectivo o crédito autorizado; sin cargo presunto. | Autorizar una sola vez. |
| Nueva guía electrónica | No disponible | M5 retiene la salida afectada; escalar. | ERP emite antes de liberar. |
| Ruteo y mapas en línea | No disponible | Usar secuencia y mapas precargados. | Recalcular cambios pendientes. |
| EDI de supermercados | No disponible | Registrar incidente y aviso acordado con cadena. | Cola y bandeja de excepciones. |
| Tablero central | No disponible | Alarmas y bitácora local sostienen despacho. | Reponer telemetría y estado. |

 Fuente: elaboración propia de LafroX a partir de Bases Técnicas Transversales, RT-03.10 y RT-03.13.

<a id="anexo-seccion-15"></a>

## Anexo 4.1-K — Reglas de reconciliación

<a id="anx-k"></a>

El detalle de reglas de reconciliación se presenta a continuación.

<a id="tab-reglas-reconciliacion"></a>

**Tabla A.12 — Reglas de reconciliación y bitácora Art. 16.4**

| **Conflicto** | **Regla de resolución** | **Dónde se ejecuta** | **Bitácora Art. 16.4** | **Dec. / ADR** |
| --- | --- | --- | --- | --- |
| Doble reserva stock (preventa offline vs online) | M2 confirma una sola reserva; la otra queda en excepción con aviso, sin resolver por la última marca de tiempo. | Capa 4 (M2/M3) | Pedido, stock, regla, resultado y hora. | Decisión 16.1 N° 8; RT-02.06 |
| Pedido duplicado (reenvío offline) | M3 conserva el UUID y devuelve el resultado ya persistido, sin volver a reservar ni cobrar. | Capa 4 (M3) | transaction_id, event_id y resultado anterior. | RT-02.06 |
| Entrega offline vs cancelación back-office | M6 aísla el conflicto: compara estado y evidencia; un supervisor resuelve antes de ajustar cobro o DTE. | Capa 4 (M6/M7) | Entrega, cancelación, POD y decisión motivada. | Decisión 16.1 N° 1 |
| Excursión térmica detectada offline | M9 bloquea localmente la salida; solo Calidad libera tras evaluación. | Capas 2 y 4 (M9/M5) | Sensor, umbral, lote, bloqueo y liberación. | Decisión 16.1 N° 4 |
| Rendición conductor offline vs ERP caído | M7 conserva la captura en el dispositivo hasta reconexión; el sitio retiene sus propios eventos en RabbitMQ; `erp-sync` reintenta con cortacircuito | Capa 1 (dispositivo) + Capa 4 (M7) + Capa 5 + ACL | conductor_id, monto, causal descuadre, reintentos ERP | INT-06, RT-10.08 |
| Conflicto envases (conductor devuelve vs cliente niega) | Cuenta corriente por cliente (saldo, no unidad); registro EnvaseMovido con firma/QR conductor; disputa → bandeja excepciones | Capa 4 (M8) | cliente_id, tipo envase, firma/QR, decisión (saldo actualizado) | Decisión 16.1 N° 10 |
| Cambio de precio entre captura y confirmación | M3 conserva la tarifa mostrada; si cambió antes de confirmar, solicita aceptación o autorización comercial, sin cambiar silenciosamente el pedido | M3 + M7 | pedido_id, tarifa inicial y vigente, respuesta del cliente | Decisión 16.1 N° 9 |
| Devolución tras guía emitida | M8 conserva cantidad, lote y causal; el ERP decide y emite el documento tributario posterior mediante ACL | M8 + ACL | entrega_id, guía original, devolución, documento resultante | Decisión 16.1 N° 12 |

 Fuente: elaboración propia de LafroX a partir de Caso 02, decisiones 16.1, y RT-03.12.

<a id="anexo-seccion-16"></a>

## Anexo 4.1-L — Decisiones del numeral 16.1

<a id="anx-l"></a>

El detalle de decisiones del numeral 16.1 se presenta a continuación.

<a id="tab-16-decisiones"></a>

**Tabla A.13 — Decisiones de diseño del numeral 16.1**

| **Nº** | **Pregunta del caso** | **Regla o componente propuesto** | **Validación** |
| --- | --- | --- | --- |
| 1 | Entrega parcial e indicador de servicio | M6 distingue entregado completo, parcial y no entregado; M10 calcula OTIF por pedido completo y ventana acordada. | Criterio comercial |
| 2 | Unidad de trazabilidad sanitaria | M9 traza GTIN y lote proveedor; M1/M5 vinculan cada movimiento a SSCC. | Unidad con Calidad |
| 3 | Local cerrado y responsable del reintento | M6 registra causal y evidencia; la regla de reintento se parametriza y supervisa por Operaciones. | Plazo y autoridad |
| 4 | Excursión térmica, decisión y bloqueo | M9 aplica umbral por producto; M5 bloquea localmente y Calidad autoriza liberar o descartar. | Umbrales con Calidad |
| 5 | Identidad y sustitución de conductor externo | Portal Transportistas registra vínculo empresa–conductor–turno; OTP inicial y revocación al cambio; M6 conserva autor de cada POD. | Procedimiento transportista |
| 6 | Efectivo y riesgo del dinero en ruta | M7 conserva cobro y rendición individual con causal de diferencia; Puelche define custodia y límite por turno. | Política de Tesorería |
| 7 | Costo de servir y clientes no rentables | M10 calcula costo por entrega con ruta, tiempo, devoluciones y envases; Comercial decide medidas, no el algoritmo. | Criterio comercial |
| 8 | Dos preventistas comprometen el mismo stock | M2 confirma reserva central; M3 deja pendiente el pedido sin conexión y comunica rechazo o sustitución al sincronizar. | Prioridad comercial |
| 9 | Precio cambia antes del despacho | M3 conserva precio informado y versión de tarifa; una diferencia genera revalidación y aviso antes de confirmar. | Política de precios |
| 10 | Control de envases retornables | M8 registra saldo por cliente, tipo y movimiento con evidencia; se concilia en la rendición. | Modalidad de cargo |
| 11 | Maestro de productos ante cambios del proveedor | M1 ingresa equivalencia GTIN/formato; el maestro autorizado se sincroniza mediante ACL con ERP y preserva historial. | Dueño del maestro |
| 12 | Devolución y DTE ya emitido | M8 registra devolución y causal; ACL solicita al ERP el documento tributario que corresponda, enlazado al original. | Regla tributaria |
| 13 | Objeción sindical a cámaras y geolocalización | M12 usa telemetría de flota para ruta y costo; excluye cámaras en cabina y control de jornada por GPS. | Gestión laboral |
| 14 | Destino del WMS 2013 | M1, M2 y M5 reemplazan sus capacidades en Etapa 1 por sitio y ola, con reversión controlada (ADR-08). | Corte por sitio |
| 15 | Receptor distinto, imposibilidad o negativa a firmar | M6 identifica receptor y causal; conserva QR, fotografía o constancia de negativa según política, sin equiparar automáticamente POD con acuse tributario. | Validez de evidencia |
| 16 | Conocimiento concentrado del planificador | M4 guarda restricciones, excepciones y decisiones del planificador; la transición incluye transferencia y prueba de rutas. | Aceptación Operaciones |

 Fuente: elaboración propia de LafroX a partir de Caso 02, numeral 16.1.

<a id="anexo-seccion-17"></a>

## Anexo 4.1-M — Verificación de continuidad lógica

<a id="anx-m"></a>

Este anexo especifica pruebas de aceptación, no resultados de ensayos. Cada ejecución debe conservar versión de software y configuración, datos de carga, relojes sincronizados, comandos de inyección de falla, logs con correlación, resultados esperados y observados, incidencias y acta. Sin estos artefactos no se acredita cumplimiento. Los responsables indicados son roles propuestos de ejecución y aprobación, no firmas ya obtenidas.

<a id="anexo-seccion-18"></a>

### AL-DTE-01. Salida de 96 camiones y falla del emisor

La prueba verifica el control de M5/ACL/ERP frente a la ventana de 05:30–07:00 (Caso 02, cap. 10 y cap. 14). Operaciones aporta el programa de 96 salidas, la relación de cargas y la cantidad real de guías por camión. No se supone una guía por camión: la carga de emisión se deriva de los destinos y documentos necesarios. Tributación del CLIENTE y el responsable del ERP deben identificar por escrito el procedimiento permitido, sus límites, autorizaciones, recuperación y documentos de respaldo.

Se ensayan cuatro escenarios: indisponibilidad del ERP antes de preparar la carga; guía emitida cuya respuesta se pierde; falla del canal tributario después de cerrar carga; y cambio de carga cuando ya existe guía. En cada uno se verifica que la misma clave no genere dos documentos, que no se libere una carga distinta de la documentada y que los camiones no afectados continúen. El procedimiento autorizado, si aplica, registra responsable, causal, hora, documento y conciliación posterior. La aplicación no crea un emisor sustituto ni habilita un botón genérico para saltar el control.

El criterio de aceptación conjunta es disponer de documentación válida para las 96 salidas programadas, sin interrupción atribuible a la solución dentro de la ventana y sin duplicados ni emisión retroactiva desde terreno. Si la única respuesta posible es retener camiones, el ensayo preserva el control tributario, pero falla el criterio de continuidad. La anticipación de guías debe probarse con cambios tardíos y no se acepta como única mitigación. El responsable de Arquitectura debe elevar el conflicto al CLIENTE con el resultado del ensayo y la alternativa de continuidad del ERP; el requisito de indisponibilidad cero permanece vigente.

<a id="anexo-seccion-19"></a>

### AL-DR-01. Pérdida de sitio durante una caída WAN

RT-07.04 mantiene RTO máximo de 4 horas y RPO máximo de 15 minutos para servicios críticos. El punto de recuperación se mide con la última transacción de negocio confirmada y recuperable, no con el último mensaje enviado ni con la existencia de un respaldo. Para cada flujo se registra la marca de agua de confirmación durable fuera del dominio de falla local. Se define RPO_observado=t_incidente-t_ultimo\_punto\_consistente, verificando además las operaciones efectivamente perdidas por UUID y secuencia.

El ensayo confirma primero el caso con enlace disponible. Después interrumpe todos los caminos WAN del sitio, mantiene carga local durante al menos 60 minutos y simula la pérdida completa del origen sin reutilizar sus discos, colas ni WAL. El equipo recupera desde el sitio secundario y compara pedidos, stock, preparación, bloqueos sanitarios y evidencias contra un oráculo de prueba externo. Se repite con una desconexión de 24 horas para comprobar el límite de la envolvente offline. Se cronometran RTO y RPO reales, no tiempos del proceso de copia por separado.

La protección requerida es una copia durable de transacciones y evidencias críticas fuera del dominio de falla, con un desfase no mayor de 15 minutos aun en el escenario acordado. Un segundo medio de comunicación solo sirve si permanece disponible ante la falla ensayada; dos enlaces que caen juntos no la proporcionan. DMS, WAL y RabbitMQ almacenados únicamente en el sitio perdido tampoco sirven. Con aislamiento total prolongado y sin extracción externa, el diseño descrito no puede demostrar ese RPO. Suspender escrituras al minuto 15 protegería la antigüedad de los datos, pero contradice la autonomía local de 24 horas y no se adopta como solución implícita.

La brecha AL-BR-01 queda identificada para decisión de Arquitectura, Infraestructura y CLIENTE: diseñar y presupuestar una protección externa independiente y probarla, o tramitar una resolución formal del mandante sobre el escenario. Su registro no equivale a elevar una consulta ya enviada ni a obtener dispensa. La aceptación no se cierra mientras persista un resultado superior a 15 minutos o no exista una resolución formal aplicable; este apartado no modifica el diseño físico ni rebaja el requisito.

<a id="anexo-seccion-20"></a>

### AL-OFF-01. Autonomía de 24 horas con dos relevos

La prueba cubre RT-03.10 y RT-03.13, con los perfiles reales de Talca, Concepción y un cross-dock; los otros sitios deben ejecutar el mismo protocolo antes de su ola. Se preinscriben usuarios, dispositivos, turnos y permisos. El corte comienza justo antes de la renovación horaria del manifiesto de 26 horas, con caché de identidad de 24 horas y reloj local controlado. Se bloquea tanto la WAN como el IdP durante 24 horas; no basta cerrar una sesión del navegador.

A las 8 y 16 horas, personas distintas inician turno con PIN personal en terminal enrolado. Se verifican firma, vigencia, rol, sitio y turno; se rechazan usuario no preinscrito, manifiesto alterado, PIN repetidamente erróneo, dispositivo no autorizado y privilegio administrativo nuevo. Se comprueba que expirar la caché descriptiva no renueve permisos ni invalide indebidamente una asignación firmada vigente; el verificador debe disponer en el manifiesto de los atributos mínimos para decidir. Se reinicia un componente local y se verifica persistencia de sesiones autorizadas, outbox y bitácora sin reutilizar claves personales.

Durante el corte se ejecutan recepción, reserva local, picking, bloqueos térmicos, despacho con documento disponible y captura de incidencias. Se incluye el intento de nueva salida sin guía: su aceptación depende de AL-DTE-01, no de aprobar el PIN. Tras reconectar se drenan colas con reenvíos, duplicados y eventos fuera de orden; se comparan stock, pedidos, POD, permisos y auditoría con el oráculo. Una revocación central desconocida durante el corte se aplica al reconectar y sus acciones del intervalo se revisan; no se declara revocación instantánea offline.

Se acepta cuando ambos relevos funcionan con personas identificadas, no hay autorización indebida, todas las operaciones confirmadas reaparecen una sola vez en el destino y cada conflicto conserva regla y responsable. El informe registra latencias, ocupación máxima, antigüedad de cola y tiempo de drenaje bajo carga de septiembre. Seguridad, Calidad y Operaciones firman los resultados. La autonomía de despacho no se declara completa si queda abierto AL-DTE-01.

<a id="anexo-seccion-21"></a>

## Anexo 4.1-N — Correspondencia de componentes lógicos

<a id="anx-n"></a>

La matriz identifica los doce módulos y los servicios transversales para cotejarlos con el esquema y explicación de solución exigidos en 3.3–3.4 y con su realización física en 4.2. El texto de trabajo disponible del capítulo 3 conserva otra numeración: 3.2.1 contiene alcance funcional de Etapa 1, 3.2.2 infraestructura y 3.3.1 Etapa 2. Estas localizaciones permiten verificar la capacidad existente, pero no sustituyen la adecuación formal de ese capítulo. La correspondencia física es una asignación lógica requerida; su aceptación exige el identificador y la evidencia del componente implantado en el 4.2 integrado.

<a id="tab-correspondencia-modulos"></a>

**Tabla A.14 — Cobertura de módulos y realización requerida**

| **Módulo** | **Capacidad en capítulo 3** | **Contrato** | **Realización requerida en 4.2** |
| --- | --- | --- | --- |
| M1 | 3.2.1 Recepción | INT-03/06 | Perfil WMS local, base por sitio y ACL ERP. |
| M2 | 3.2.1 Inventario | INT-03/04/12 | WMS por sitio, consolidación central y réplica de lectura de Talca. |
| M3 | 3.2.1 Preventa | INT-01/06 | App Kotlin y API Laravel central. |
| M4 | 3.2.1 y 3.3.1 Ruteo | INT-10 | Servicio de planificación y optimizador separado por contrato. |
| M5 | 3.2.1 Picking y carga | INT-03/07 | HHT, puerta local y WMS con control de guía. |
| M6 | 3.2.1 Entrega y POD | INT-02 | App de reparto, API y almacenamiento de evidencia. |
| M7 | 3.2.1 Rendición; 3.3.1 Cartera | INT-02/06/09 | API, trabajadores Laravel y ACL de cobranza. |
| M8 | 3.2.1 y 3.3.1 Devoluciones | INT-02/03/06 | Registro móvil/local y servicios de conciliación. |
| M9 | 3.2.1 Trazabilidad y frío | INT-03/05 | Bloqueo local, ingesta IoT y consulta de lotes. |
| M10 | 3.3.1 Analítica | Eventos canónicos | Ingesta a lago y servicios de consulta analítica. |
| M11 | 3.3.1 Canal moderno | INT-08 | Reglas Laravel, OpenAS2 y conector por cadena. |
| M12 | 3.3.1 Telemetría | INT-15 | Adaptador de solo lectura y consulta de ruta real. |

 Fuente: capítulo 3 de trabajo, capacidades citadas; catálogo lógico M1–M12 e INT-01–15.

La tabla cubre 12 de 12 módulos, no el 100% de los componentes del capítulo integrado. Para las capacidades transversales de 3.2.2 se exige correspondencia adicional: presentación y borde con aplicaciones, CloudFront y acceso privado; puerta de enlace con API central y puerta local; eventos con RabbitMQ, shipper y SQS; datos con bases, réplica de lectura y objetos; identidad con Keycloak y verificador local; secretos y auditoría con sus servicios de custodia; observabilidad con OpenTelemetry/ADOT, alarma local y CloudWatch. Notificaciones se traza a INT-11; el motor de optimización de M4 conserva contrato separado y no se presume implementado en PHP por la elección del backend.

El cierre AL-MAP-01 requiere inventariar cada caja de los diagramas 3.3 y 4.1, asignarle identificador estable, contrato, responsable y componente exacto de 4.2, y efectuar la comprobación inversa para detectar infraestructura sin función. La cobertura se calcula como componentes con ambos enlaces verificados dividido por el inventario completo; una referencia genérica a 4.2 no cuenta como enlace verificado. No se declara 100% hasta integrar las versiones aprobadas de los tres apartados.

<a id="anexo-seccion-22"></a>

### Inventario trazable de capacidades transversales

Los siguientes 37 identificadores complementan los doce módulos: el inventario lógico tiene 49 unidades verificables. La capacidad del capítulo 3 se cita según su localización disponible; la última columna especifica la obligación que debe realizar 4.2, no acredita su implantación. AL-MAP-01 exige completar el identificador físico exacto y verificar ambos sentidos antes del cierre integrado.

<a id="tab-inventario-transversal"></a>

**Tabla A.15 — Inventario transversal y correspondencia requerida**

| **ID** | **Componente** | **Capacidad** | **Contrato** | **Obligación en 4.2** |
| --- | --- | --- | --- | --- |
| UI-MOV | Apps Kotlin / Room | 3.2.1 preventa y entrega | INT-01/02 | M3/M6/M7/M8 |
| UI-HHT | Terminales de bodega | 3.2.1 preparación | INT-03 / API local | M1/M2/M5 |
| UI-WEB | Portales Angular | 3.2.2 administración; 3.3.1 portales | API autorizada | Roles por empresa |
| BOR-PUB | CloudFront / WAF / Shield | 3.2.2 seguridad | HTTPS | Entrada pública única |
| BOR-B2B | Superficie AS2 | 3.3.1 canal moderno | INT-08 | Contrapartes registradas |
| GW-CENT | REST API / authorizer | 3.2.2 plataforma | API / sincronización | ADR-13 |
| GW-LOCAL | Puerta API de sitio | 3.2.1 WMS | INT-03 | Validación sin WAN |
| AUTH-CENT | Keycloak | 3.2.2 seguridad | INT-13 / OIDC | Autoridad de identidad |
| AUTH-LOCAL | Verificador de turnos | 3.2.2 continuidad | Manifiesto firmado | PIN, turno y sitio |
| WMS-SITE | Perfil WMS local | 3.2.1 WMS | INT-03 | Un escritor por sitio |
| INT-BROKER | RabbitMQ | 3.2.2 integración | AMQP | Persistencia y DLQ |
| INT-SHIPPER | Shipper local a nube | 3.2.2 integración | JSON / SQS | Acuse después de envío |
| INT-CONSUMER | Consumidor PHP | 3.2.2 integración | AsyncAPI / JSON | Persistir antes de acuse |
| INT-JOBS | Trabajadores Laravel | 3.2.2 ERP | Colas internas | ERP-sync aislado |
| INT-SCHED | Planificador | 3.2.2 administración | Tareas versionadas | Un líder por ambiente |
| INT-ACL | Adaptador ERP | 3.2.2 ERP / DTE | INT-06/07 | ERP único emisor |
| INT-EDI | OpenAS2 / perfiles | 3.3.1 canal moderno | INT-08 | MDN no es acuse comercial |
| INT-GIS | Adaptador de mapas | 3.2.1 rutas | INT-10 | Tiempo máximo / precarga |
| INT-OPT | Optimizador M4 | 3.2.1 y 3.3.1 rutas | Trabajo versionado | Restricciones de ruta |
| INT-GPS | Adaptador de flota | 3.3.1 telemetría | INT-15 | Solo lectura |
| INT-NOTIF | Notificaciones | 3.2.2 administración | INT-11 | Vigencia por canal |
| INT-IOT | Captura térmica local | 3.2.1 frío | INT-05 | Bloqueo local |
| DAT-OLTP | PostgreSQL / PostGIS | 3.2.1 inventario | Repositorios propios | Autoridad por sitio |
| DAT-CDC | Réplica de Talca | 3.2.2 continuidad | INT-12 | Lectura, no doble escritor |
| DAT-OLAP | DynamoDB / Glue / S3 / Redshift | 3.3.1 analítica | ETL / eventos | Separado de OLTP |
| DAT-OBJ | Objetos POD / DTE | 3.2.1 entrega | Hash y objeto | Retención por dominio |
| DAT-CACHE | Redis central | 3.2.2 plataforma | Lecturas autorizadas | No reserva stock |
| DAT-LOCAL | Room / cola cifrada | 3.2.1 movilidad | UUID / sincronización | Separar foto y pendientes |
| SEC-SECRETS | Custodia de claves | 3.2.2 seguridad | Identidad de servicio | Rotación segregada |
| SEC-AUDIT | Auditoría inalterable | 3.2.2 administración | Evento de decisión | Sujeto, regla y resultado |
| SEC-SIEM | Detección y correlación | 3.2.2 seguridad | Alertas | Casos Q/R |
| OBS-COLLECT | OpenTelemetry / ADOT | 3.2.2 observabilidad | INT-14 / OTLP | Buffer de 24 horas |
| OBS-LOCAL | Alarmas del sitio | 3.2.2 continuidad | Alerta local | No depende de WAN |
| OBS-CENT | CloudWatch | 3.2.2 observabilidad | INT-14 | Plataforma única |
| DEV-PIPE | CI/CD y SBOM | 3.2.2 plataforma | Artefacto firmado | Promoción por contrato |
| DEV-IAC | Terraform / Ansible | 3.2.2 infraestructura | Estado y configuración | Propietario único |
| DEV-MDM | Gestión de terminales | 3.2.2 seguridad | Enrolamiento | Política y borrado |

<a id="anexo-seccion-23"></a>

## Anexo 4.1-O — Decisiones de arquitectura lógica

<a id="anx-o"></a>

Las fichas tienen fecha de decisión documental 30 de septiembre de 2026 y estado *adoptada en la propuesta*. Ese estado no acredita aprobación del CLIENTE ni ejecución de la prueba. Los identificadores existentes se conservan; las fichas ADR-01, 05, 06, 13 y 14 sustituyen para la vista lógica las formulaciones incompatibles del registro anterior. La realización física debe cotejar esos identificadores antes del cierre integrado (PUCV, 2026b, RT-02.04; Aclaraciones, capítulo 4).

<a id="anexo-seccion-24"></a>

### ADR-01. Núcleo y límites de módulo

La decisión es Laravel 13/PHP 8.5 con M1–M12, puertos de dominio y perfiles API, WMS local y trabajadores separados. Se descartan microservicios por módulo por su carga de administración para cuatro personas y un monolito sin fronteras por impedir aislamiento; Django es viable, pero conservar ambos runtimes duplicaría dependencias y operación. El criterio es poder desplegar los procesos críticos de forma independiente sin duplicar el dominio. Se exige prueba de dependencias entre módulos, contratos y promoción de un trabajador sin interrumpir WMS. Un proceso comparte artefacto, no permisos ni memoria durable.

<a id="anexo-seccion-25"></a>

### ADR-04. Persistencia por responsabilidad

Se selecciona PostgreSQL/PostGIS para transacciones y geografía, DynamoDB para ingesta raw y S3/Redshift para consolidación analítica. Se descartan un único almacén para operación y análisis por competencia con picking, y un motor adicional de series por mayor operación. El criterio es conservar autoridad transaccional por sitio y permitir consulta analítica sin escribir stock. La consecuencia es reconciliar por contratos, no por doble escritura. La prueba comprueba propietarios, consultas espaciales y que un tablero no acceda al OLTP.

<a id="anexo-seccion-26"></a>

### ADR-05. Mensajes canónicos y trabajos internos

Se seleccionan outbox y RabbitMQ local, shipper hacia SQS FIFO y consumidor PHP de JSON versionado. Los trabajos serializados de Laravel usan colas separadas; SNS difunde avisos. Se descartan broker solo en nube por perder continuidad del sitio y Kafka por complejidad no justificada. Cada partición tiene orden y cada consumidor deduplica por sitio y UUID. El acuse del broker no equivale a resultado de negocio. La prueba interrumpe publicación, persistencia y acuse y demuestra una sola consecuencia.

<a id="anexo-seccion-27"></a>

### ADR-06. Identidad y relevo local

Keycloak mantiene la autoridad central. La caché descriptiva local dura 24 horas; el manifiesto firmado cubre 26 horas y se renueva cada hora; la autorización personal dura 8 horas en bodega o 14 en terreno. El verificador local valida persona, PIN, dispositivo, sitio y turno. Se descartan cuentas compartidas, caché que emite identidades y dependencia exclusiva del IdP remoto. La prueba AL-OFF-01 incluye relevos a las 8 y 16 horas, reloj, revocación al reconectar y reinicio. El riesgo de revocación remota durante aislamiento se limita por expiración y bloqueo conocido localmente.

<a id="anexo-seccion-28"></a>

### ADR-07. Movilidad

Kotlin nativo con Room y periféricos Zebra conserva captura cifrada y evidencia. Se descartan PWA como único cliente de campo y una capa multiplataforma sin validación de periféricos. El criterio es escaneo con guantes, acceso a termógrafo/POS e interacción de una mano. La selección no atribuye inferioridad universal a Flutter; se verifica con el parque del caso y pruebas a -22 °C, lluvia y sin señal.

<a id="anexo-seccion-29"></a>

### ADR-08. Sustitución del WMS

M1/M2/M5 sustituyen el WMS 2013 en Etapa 1 mediante olas por sitio y capacidad. Mantener el legado indefinidamente arrastra falta de soporte; reemplazarlo simultáneamente eleva el riesgo de corte. La reversión requiere un único escritor, conciliación de pendientes y esquema compatible; no se promete volver a una base antigua con eventos nuevos sin transformar. La aceptación comprueba stock, lote y misiones antes y después de una reversión.

<a id="anexo-seccion-30"></a>

### ADR-11. EDI y frontera ERP

M11 traduce EANCOM/GS1 XML mediante perfiles por cadena; OpenAS2 conserva transporte, firma y MDN. El ERP se alcanza solo por ACL. Se descartan conectores directos de cada módulo al ERP y equivalencias dispersas por pantalla. El criterio es incorporar cadenas por configuración sin cambiar el pedido de M3. Se ensayan mensaje repetido, código desconocido, MDN perdido y rechazo comercial. M11 entra en Etapa 2.

<a id="anexo-seccion-31"></a>

### ADR-12. Aislamiento y capacidad

API, WMS local, reconciliación, ERP-sync, EDI y notificaciones tienen procesos, concurrencia, permisos y colas propios. Se descarta escalar un único proceso para absorber IoT y guías a la vez. Los mamparos reservan capacidad para despacho y limitan consumidores no críticos. El Anexo T define respuesta, carga de ensayo y recuperación; los límites cuantitativos de instancias y su emplazamiento se acreditan en 4.2. La prueba mide bloqueo de base y edad de cola además de CPU.

<a id="anexo-seccion-32"></a>

### ADR-13. Publicación y autorización

Se selecciona Amazon API Gateway REST API con authorizer REQUEST que verifica JWT de Keycloak; la integración privada utiliza VPC Link V2 hacia ALB. Se descarta tratar HTTP API y REST API como intercambiables sin verificar validación y cuotas, y un gateway propio por carga de operación. La validación básica de Gateway se complementa en Laravel con esquema completo y políticas por recurso. La decisión se sustenta en la documentación de AWS sobre validación, authorizers e integración privada (Amazon Web Services [AWS], s. f.-a, s. f.-b, s. f.-c). Se ensayan firma, emisor, audiencia, expiración, alcance, cuerpo no admitido y acceso directo al origen.

<a id="anexo-seccion-33"></a>

### ADR-14. Observabilidad

OpenTelemetry y ADOT exportan a una plataforma CloudWatch con correlación de transacción; alarmas locales y buffer de 24 horas sostienen el sitio. Se descarta una segunda plataforma editorial de tableros por instalación y una alarma que dependa de WAN para detener una carga. El criterio es una operación común, sin convertir el diagnóstico en dueño de negocio. Los destinos, muestreo, retención y permisos se versionan; auditoría de negocio nunca se descarta para conservar una traza. La prueba reconstruye el recorrido de un UUID después del corte.

<a id="anexo-seccion-34"></a>

### ADR-L01. Liberación documental

M5 solicita la guía al ERP con clave por despacho y versión de carga. Se descartan emisión sustituta en Laravel, reintento ciego y autorización genérica del supervisor. La evidencia válida se guarda localmente antes de liberar. Se propone continuidad del emisor ERP con su mecanismo de emisión y custodia existente o una contingencia autorizada y documentada; la ACL consulta ese mismo emisor, sin duplicarlo. La elección concreta requiere validación de Tributación y responsable del ERP. AL-DTE-01 verifica cambios tardíos y las 96 salidas; el Anexo V registra la decisión del CLIENTE requerida.

<a id="anexo-seccion-35"></a>

### ADR-L02. Protección fuera del sitio

Toda transacción crítica confirmada localmente conserva secuencia y marca de agua de protección externa. Se exige copia durable fuera del dominio de falla con retraso máximo de 15 minutos en el escenario cubierto; la selección de medios es física. Se descarta declarar RPO cumplido mediante WAL o RabbitMQ del mismo sitio. Si todos los caminos de extracción fallan y el origen se destruye, no existe solución de software que recupere datos nunca enviados. La continuidad local se mantiene y el riesgo se escala por AL-BR-01 sin suspender implícitamente escrituras ni rebajar RT-07.04. AL-DR-01 comprueba el escenario y la decisión formal aplicable.

<a id="anexo-seccion-36"></a>

## Anexo 4.1-P — Tecnologías, soporte y actualización

<a id="anx-p"></a>

El inventario distingue versión de referencia de una imagen exacta de producción. Cada liberación fija parches, hashes y compatibilidad en los archivos de bloqueo y SBOM; las versiones futuras se aprueban mediante pruebas antes de promoverse. La hoja de ruta cubre los 56 meses mediante actualizaciones, no suponiendo soporte de una misma versión durante todo el contrato (PUCV, 2026b, numeral 1.6).

<a id="tab-soporte-logico"></a>

**Tabla A.16 — Ciclo de soporte del núcleo lógico**

| **Producto** | **Referencia** | **Fin de soporte publicado** | **Plan de actualización** |
| --- | --- | --- | --- |
| Laravel | 13.x | Seguridad: 17-03-2028. | Evaluación anual; migrar al menos 6 meses antes del fin. |
| PHP | 8.5.x | Seguridad: 31-12-2029. | Actualización compatible antes del fin; ensayo de APIs y colas. |
| PostgreSQL | 16.x | 09-11-2028. | Ensayo de migración mayor y reversión 6 meses antes. |
| Angular | 22.x | LTS: junio de 2028, fecha orientativa del fabricante. | Revisión semestral y actualización anual por compatibilidad. |
| TypeScript | 6.0.x | Sin fecha contractual independiente. | Versión compatible con Angular; archivo de bloqueo y pruebas. |
| RabbitMQ | 4.3.x | Comunidad: 30-11-2026. | Actualizar antes de esa fecha a rama soportada; no se presume licencia comercial. |

 Fuente: Laravel (2026), PHP (2026), PostgreSQL (2026), Angular (2026a, 2026b) y RabbitMQ (2026). Fechas consultadas el 30-09-2026.

Laravel, PHP, PostgreSQL y Angular tienen horizontes inferiores al contrato: el responsable de Desarrollo registra cada trimestre su soporte y planifica la sustitución antes de vencimiento. RabbitMQ requiere una actualización temprana antes del fin comunitario de la rama de referencia, aun durante desarrollo. No se atribuye al CLIENTE un contrato de soporte comercial no contratado.

<a id="tab-inventario-software"></a>

**Tabla A.17 — Inventario complementario y control de vigencia**

| **Componente** | **Línea base lógica** | **Control durante 56 meses** |
| --- | --- | --- |
| PostGIS | 3.x compatible con PostgreSQL 16. | Compatibilidad y fin de soporte de la distribución registrados antes de liberar. |
| Kotlin/Android | Rama estable compatible con parque Zebra. | Matriz OS, SDK y periféricos por modelo; MDM impide OS fuera de soporte. |
| Room/SQLite | Versión estable de AndroidX Room y SQLite incorporada. | Parches fijados por Gradle; migración de cola sin perder pendientes. |
| Keycloak | 26.x, parche soportado al liberar. | Revisión trimestral del ciclo oficial; migrar junto al adaptador OIDC. |
| Tailwind/Node/RxJS | Versiones compatibles con Angular y su toolchain. | Archivo de bloqueo y matriz de compatibilidad; Node solo construye el cliente. |
| Composer/PHPUnit/PHPStan/Pint | Versiones compatibles con PHP 8.5 y Laravel 13. | Composer lock, análisis de licencia, audit y regresión; no entran herramientas de prueba al runtime. |
| php-amqplib/AWS SDK/swagger-php | Bibliotecas mantenidas compatibles con PHP 8.5. | Contrato AMQP, sobre JSON y generación OpenAPI bloquean cambios incompatibles. |
| OpenAS2/JVM | Rama soportada compatible con perfiles de las cadenas. | Certificados, licencia, runtime Java y pruebas MDN registrados antes de habilitar INT-08. |
| OpenTelemetry/ADOT | Versiones estables de SDK y colector. | Ensayo de recepción OTLP, correlación, buffer y exportación tras corte. |
| Terraform/Ansible | Versiones estables y providers fijados. | Terraform gobierna recursos; Ansible configura hosts. AWS CDK no gobierna los mismos recursos. |
| Servicios AWS | API/engine gestionados declarados por servicio. | Avisos de retiro trimestrales; prueba de adaptación. Aurora conserva versión de engine y fecha de soporte del proveedor. |
| MDM/Android Enterprise | Servicio y plan compatibles con el parque. | Contrato de soporte y actualización de dispositivos durante todo el período. |

 Fuente: decisiones de arquitectura lógica y política de configuración de la propuesta. No se inventan fechas que un proveedor no publica.

El fin de soporte no publicado se registra como *no publicado*, con responsable y frecuencia de revisión; no significa soporte indefinido. Antes de aprobar una dependencia se verifica licencia, mantenimiento, vulnerabilidades y alternativa de sustitución (RT-11.26). La ficha de liberación identifica versión exacta, EOL conocido o política aplicable, prueba, rollback y responsable. La aceptación rechaza una imagen fuera de soporte.

Las alternativas se evalúan por operación offline, integración industrial, transacciones, geografía, carga del equipo y reversibilidad. PostgreSQL/PostGIS se selecciona frente a MariaDB por el dominio espacial; Angular se conserva frente a cambiar la plataforma web por sus contratos y componentes existentes; Kotlin se selecciona frente a una capa móvil adicional por validación del parque; Keycloak mantiene identidad propia frente a delegar el dominio de autorizaciones a un IdP propietario. Las herramientas de construcción no cambian esos contratos. Los criterios concretos se verifican en ADR-01/04/06/07/13 y el Anexo T.

<a id="anexo-seccion-37"></a>

### Implementación compatible del backend

<a id="tab-mapeo-laravel"></a>

**Tabla A.18 — Implementación lógica del backend Laravel**

| **Capacidad** | **Implementación Laravel/PHP** | **Comprobación** |
| --- | --- | --- |
| APIs y módulos | Rutas y controladores Laravel; servicios por contexto PSR-4. | Contratos OpenAPI y límites de módulo. |
| Persistencia y geografía | PDO/Query Builder y SQL PostGIS parametrizado; migraciones Laravel basales. | Datos, índices y consultas espaciales equivalentes. |
| Tareas y planificación | Consumidor PHP de JSON en SQS FIFO; trabajos Laravel en colas separadas y planificador único. | Orden por grupo, reintentos y tareas únicas. |
| Cola local y shipper | Adaptador AMQP con `php-amqplib` y sobre JSON. | Corte de 24 h, confirmación y drenaje sin pérdida. |
| Identidad y administración | Guard OIDC, políticas por recurso y portal Angular. | Permisos, baja y relevos de turno. |
| Contratos, pruebas y trazas | `swagger-php`, AsyncAPI, PHPUnit y OpenTelemetry PHP. | Paridad de API, eventos y correlación. |

<a id="anexo-seccion-38"></a>

## Anexo 4.1-Q — Modelado de amenazas lógicas

<a id="anx-q"></a>

STRIDE se aplica por módulo, componente transversal e integración externa (RT-11.02). S representa suplantación; T, alteración; R, repudio; I, divulgación; D, denegación; E, elevación de privilegios. Cada escenario tiene una prueba negativa y un dueño; el registro se reevalúa al cambiar un contrato o límite de confianza. Esta matriz registra amenazas de diseño, no resultados de pentesting.

<a id="tab-amenazas-modulos"></a>

**Tabla A.19 — Amenazas de los doce módulos**

| **Elemento** | **Amenaza** | **Control y prueba** | **Dueño** |
| --- | --- | --- | --- |
| M1 | T: lote o recepción falsa. | GS1, cuarentena y evidencia; rechazar lote sin origen. | Recepción/ Calidad |
| M2 | T/ D: reserva duplicada. | Escritor único, UUID y bloqueo por agregado; doble compromiso. | Inventario |
| M3 | S/ T: pedido con identidad ajena. | Turno, dispositivo y firma; token inválido y reenvío. | Comercial/ Seguridad |
| M4 | T: ruta con restricción omitida. | Restricción versionada, aprobación y motivo; ruta incompatible. | Operaciones |
| M5 | E: liberar carga retenida. | Política por recurso y documento vigente; supervisor sin permiso. | Bodega/ Calidad |
| M6 | R/ T: POD alterado. | Hash, autor, hora y vínculo guía; objeto con hash distinto. | Reparto |
| M7 | E/ R: aprobar cobro propio. | Segregación y conciliación; mismo autor registrador/ aprobador. | Tesorería |
| M8 | T: devolución o saldo ficticio. | Causal, lote, evidencia y disputa; devolución repetida. | Bodega/ Tesorería |
| M9 | T/ E: ocultar excursión. | Alarma local y liberación exclusiva de Calidad; muestra alterada. | Calidad |
| M10 | I: exponer crédito por tablero. | Modelo autorizado, filtros y auditoría; consulta de otro cliente. | Datos/ Seguridad |
| M11 | T/ D: EDI repetido o inválido. | Firma, equivalencia y UUID; repetición/ rechazo sin crear pedido. | Canal moderno |
| M12 | I: uso de GPS fuera de finalidad. | Rol, ruta, retención y consulta auditada; usuario sin asignación. | Flota/ Seguridad |

 Fuente: elaboración propia sobre límites de M1–M12 y RT-11.02.

<a id="tab-amenazas-fronteras"></a>

**Tabla A.20 — Amenazas en fronteras y terceros**

| **Elemento** | **Amenaza** | **Control y evidencia de aceptación** |
| --- | --- | --- |
| INT-06/ 07, ACL y ERP | T/ R: documento duplicado o incierto. | Clave por carga, consulta antes de reintento y estado explícito; AL-DTE-01. |
| INT-08/ OpenAS2 | S/ T: contraparte falsa o mensaje cambiado. | Certificado registrado, firma y MDN; certificados desconocidos y hash alterado. |
| INT-09/ POS | T/ R: doble cobro por timeout. | Clave de cargo, consulta y conciliación; respuesta tardía después de alternativa. |
| INT-10/ GIS/ optimizador | D/ T: cuotas o ruta manipulada. | Timeout, límites, ruta aprobada y comprobación de restricciones. |
| INT-11/ avisos | I/ T: revelar pedido o avisar tarde. | Consentimiento/ canal, mínimo dato y vigencia; aviso vencido. |
| INT-15/ GPS | I/ T: posición falsa o histórica. | Cursor, fecha y acceso de solo lectura; muestra fuera de secuencia. |
| UI-MOV/ UI-HHT/ DAT-LOCAL | I/ S: pérdida o préstamo de terminal. | MDM, cifrado, PIN y turno; pérdida y dispositivo no enrolado. |
| BOR-PUB/ GW-CENT/ AUTH-CENT | S/ D: abuso o token ajeno. | WAF, cuota, JWT y política; firma/ audiencia inválida y ráfaga. |
| GW-LOCAL/ AUTH-LOCAL/ WMS-SITE | E/ T: manifiesto alterado o reloj movido. | Firma, reloj controlado y permisos; AL-OFF-01. |
| INT-BROKER/ SHIPPER/ CONSUMER/ JOBS | T/ D: evento repetido o tóxico. | Sobre versionado, outbox, DLQ y deduplicación; corte en cada acuse. |
| INT-SCHED/ INT-IOT | D/ T: tarea duplicada o sensor perdido. | Autoridad única y frescura de lectura; doble líder y ausencia de sensor. |
| DAT-OLTP/ CDC/ OLAP/ OBJ/ CACHE | I/ T: lectura o escritura no autorizada. | Dueño, cifrado, cuenta mínima y hash; consulta directa y objeto cambiado. |
| SEC-SECRETS/ AUDIT/ SIEM | I/ R: clave expuesta o evidencia borrada. | Custodia separada, Object Lock y alertas; administración sin descifrado. |
| OBS-COLLECT/ LOCAL/ CENT | D/ R: buffer lleno o traza faltante. | Cuota, alarma y prioridad de auditoría; corte con saturación. |
| DEV-PIPE/ IAC/ MDM/ UI-WEB/ BOR-B2B | S/ E: artefacto o acceso de gestión ajeno. | Firma, SBOM, aprobación y MFA; imagen sin procedencia y rol excesivo. |

 Fuente: catálogo INT-01–15, inventario del Anexo N y RT-11.02. Seguridad mantiene el registro; cada dueño ejecuta su escenario con Calidad.

Las integraciones internas heredan los controles de productor y consumidor: INT-01/ 02, identidad y UUID; INT-03/ 04, sitio y secuencia; INT-05, sensor y frescura; INT-12, cuenta CDC de lectura; INT-13, manifiesto firmado; INT-14, integridad y capacidad del buffer. Toda excepción conserva escenario, consecuencia, responsable, tratamiento y criterio de cierre.

<a id="anexo-seccion-39"></a>

## Anexo 4.1-R — Controles de seguridad y evidencia

<a id="anx-r"></a>

Esta matriz vincula controles de ISO/ IEC 27001:2022, Anexo A, y su guía ISO/ IEC 27002:2022 con la implementación lógica y la evidencia prevista (RT-11.05). La numeración es un identificador de control, no una declaración de certificación. El sistema de gestión conserva además evaluación de riesgos y declaración de aplicabilidad. La política Zero Trust se fundamenta en NIST SP 800-207 (NIST, 2020).

<a id="tab-controles-seguridad"></a>

**Tabla A.21 — Controles aplicados a la vista lógica**

| **Control** | **Requisito** | **Implementación concreta** | **Evidencia** |
| --- | --- | --- | --- |
| 5.9 | RT-11.23 | Inventario de componentes y SBOM CycloneDX/ SPDX por liberación. | SBOM y hashes del artefacto. |
| 5.12/ 5.13 | RT-11.03 | Clasificación aplicada a API, evento, objeto y copia local. | Matriz y pruebas de exportación. |
| 5.15/ 5.18 | RT-12.05/ 06 | Roles y atributos por recurso; altas y bajas trazadas. | Permisos y pruebas negativas. |
| 5.16/ 5.17 | RT-12.01/ 11 | Keycloak, PIN personal y credencial de turno firmada. | AL-OFF-01 y baja conectada. |
| 5.19/ 5.20 | RT-05.21 | SLA, ventanas, datos y respuesta de cada contraparte. | Fichas G/ H y acuerdos. |
| 5.23 | RT-11.06 | Responsabilidad compartida por servicio de nube. | Control ISO 27017/ 27018 aplicable y dueño. |
| 5.24/ 5.26 | RT-11.18/ 19 | Clasificación, correlación y comunicación de incidentes. | Ejercicio y bitácora; aviso crítico 2 h, brecha 24 h. |
| 5.30 | RT-10.03/ 04 | Funciones offline, dependencia y recuperación consistente. | Protocolos M y plan del capítulo 11. |
| 5.34 | RT-16.09 | Finalidad, retención y consulta de GPS/ crédito registradas. | Consulta autorizada y eliminación. |
| 8.2 | RT-12.09 | Elevación temporal y segregación de Tesorería/ Calidad. | Sesión y aprobación nominadas. |
| 8.5 | RT-12.07/ 08 | MFA, token corto, refresh rotatorio y expiración. | Pruebas de firma y sesión. |
| 8.7/ 8.8 | RT-11.04/ 16 | EDR y gestión de vulnerabilidades en runtime y terminal. | Escaneo y remediación 7/ 15/ 30 días. |
| 8.9 | RT-04.05 | Configuración versionada y cambios aprobados. | Diferencia de configuración y reversión. |
| 8.10/ 8.11 | RT-05.07/ 11.25 | Eliminación verificable y anonimización fuera de producción. | Borrado y conjunto de prueba. |
| 8.13/ 8.14 | RT-07.04 | Estado durable y protección externa por dominio de falla. | AL-DR-01; no basta cola local. |
| 8.15/ 8.16 | RT-11.14/ 15 | Auditoría inalterable y detección específica del negocio. | UUID enlazado con regla SIEM. |
| 8.20/ 8.22 | RT-11.07/ 13 | Borde, superficie B2B separada y puerta local privada. | Intento directo al origen denegado. |
| 8.24 | RT-11.08/ 09/ 10 | Cifrado de reposo, campo y tránsito; claves separadas. | Admin sin texto claro y rotación. |
| 8.25/ 8.28 | RT-11.22/ 24 | SAST/ SCA/ DAST, firma y procedencia SLSA 3. | Pipeline bloqueado por hallazgo. |
| 8.29/ 8.31/ 8.32 | RT-04.03/ 11.27 | Pruebas, ambientes segregados y promoción aprobada. | Commit, ensayo y despliegue correlacionados. |

 Fuente: elaboración propia a partir de ISO (2022b, 2022c), RT-11/ 12 y contratos lógicos. Seguridad verifica aplicabilidad con el responsable del sistema de gestión.

La arquitectura impone HSTS en los portales HTTPS, TLS 1.3 en interfaces compatibles y rechazo de TLS 1.0/ 1.1. Un tercero con limitación de protocolo exige excepción documentada y tratamiento, no una reducción silenciosa del control. Entre sistemas se utiliza mTLS u OAuth con credenciales de cliente; nunca una clave estática en la URL. El catálogo público no muestra precios, conforme al caso. OWASP ASVS nivel 2 y API Security Top 10 orientan las pruebas de aplicación. La superficie exacta y la implantación de EDR/ SIEM se realizan en la vista física; los permisos, eventos y pruebas permanecen definidos aquí.

<a id="anexo-seccion-40"></a>

## Anexo 4.1-S — Puntos de vista y correspondencias

<a id="anx-s"></a>

La entidad de interés es la plataforma logística Puelche y sus fronteras con ERP, personas y servicios de terceros. La descripción cubre toma de pedido, reserva, preparación, salida, entrega, rendición, trazabilidad y análisis; su horizonte incluye dos etapas y 36 meses de operación. Cada punto de vista fija preocupación, interesados, modelos y comprobación, conforme a RT-02.03 e ISO/IEC/IEEE 42010:2022 (ISO, 2022a).

<a id="tab-puntos-vista"></a>

**Tabla A.22 — Interesados y modelos de las cinco vistas**

| **Vista** | **Interesados** | **Preocupación** | **Modelos y evidencia** |
| --- | --- | --- | --- |
| Lógica | TI y responsables de módulo. | Dueños, límites e interfaces sin dependencia de tablas ajenas. | General, capas y catálogos D/F/G/H/N. |
| Procesos | Operaciones, conductores y Tesorería. | Una captura avanza a confirmación, salida y rendición con estados claros. | Secuencias ARQL-15/16; eventos A y documento U. |
| Despliegue | TI, Infraestructura y Operaciones. | Cada función dispone de realización y contingencia por sitio. | Inventario N y enlaces exactos a 4.2–4.3. |
| Datos | Calidad, Datos y Comercial. | Lote, reservas, acuses y evidencias tienen dueño y retención. | Modelo ARQL-18, reconciliación K y capítulo 5. |
| Seguridad | Seguridad, Calidad y CLIENTE. | Nadie libera, cobra o consulta sin permiso y evidencia. | Límites de confianza, Q/R y prueba AL-OFF-01. |

 Fuente: interesados del caso, RT-02.03 y organización de la descripción arquitectónica (ISO, 2022a).

CR-01 exige que cada capacidad del esquema y explicación de solución tenga uno o más componentes N con nombre idéntico y que todo componente tenga capacidad de origen. CR-02 exige productor único, consumidores registrados y contrato por evento; una arista sin contrato se rechaza. CR-03 exige que cada escritura tenga dueño de datos, clave idempotente y auditoría. CR-04 exige para cada función desconectada persistencia, permisos, límite de autonomía y reconciliación. CR-05 vincula componente lógico a realización física exacta; no se cuenta una referencia genérica. CR-06 exige que cada amenaza tenga control y prueba, y que cada decisión ADR tenga consecuencia verificable.

Arquitectura mantiene un registro de diferencias con componente, regla infringida, requisito, dueño, decisión y evidencia de cierre. La comprobación se ejecuta al cambiar un módulo, contrato, tecnología o etapa. AL-MAP-01 verifica CR-01/05; pruebas de contrato, CR-02/03; AL-OFF-01, CR-04; y la revisión de Q/R/O, CR-06. La conformidad de una vista no se atribuye a otra sin sus modelos.

<a id="anexo-seccion-41"></a>

## Anexo 4.1-T — Desempeño y aceptación lógica

<a id="anx-t"></a>

Los umbrales se miden sobre la operación percibida y confirmada, no sobre una llamada aislada. La copia de consulta puede responder inmediatamente como información fechada; no confirma stock o crédito. El timeout del adaptador es un límite de protección independiente del tiempo visible al usuario (PUCV, 2026a, cap. 15; PUCV, 2026b, RT-09.01–09.08).

<a id="tab-aceptacion-desempeno"></a>

**Tabla A.23 — Objetivos y escenarios de desempeño**

| **Operación** | **Objetivo** | **Carga y comprobación** |
| --- | --- | --- |
| Confirmar línea picking | p95 ≤ 1 s. | Terminal, puerta local, M5/M2 y base; 120 preparadores concurrentes. |
| Registrar entrega | p95 ≤ 2 s. | Persistencia local durable, POD y UUID; el envío de foto no bloquea la captura. |
| Registrar línea preventa | p95 ≤ 1,5 s. | Captura cifrada, persistencia y estado; no exige reserva central offline. |
| Consultar stock/crédito | p95 ≤ 2 s. | API con enlace; copia fechada inmediata durante degradación. |
| Reconciliar reparto | ≤ 10 min por turno. | 14 h de captura, mensajes y objetos; sin pérdidas ni duplicados. |
| Reconciliar CD | ≤ 2 h tras corte. | 24 h locales, relevos y cargas por sitio; ocupación máxima y drenaje. |
| Planificar ruta | < 20 min. | Flota, destinos, capacidad, frío y ventanas; restricciones verificadas. |
| Liberar despachos | 96 salidas 05:30–07:00. | Guías por destino/carga y cambios tardíos; AL-DTE-01. |

 Fuente: Caso 02, caps. 14–15 y 18; las pruebas son compromisos de ejecución, no resultados obtenidos.

La carga nominal usa 31.000 pedidos y 260.000 líneas mensuales. La envolvente peak de G/H duplica los eventos de pedido y bodega cuando no existe una distribución horaria medida. RT-09.06 exige además 1,5 veces ese peak: por ejemplo, 156.000 eventos de bodega por día de ensayo si el peak es 104.000, y 3.900 entregas por día si la referencia peak es 2.600. Esas cifras no trasladan todas las entregas a la ventana de salida de camiones. La prueba distribuye la carga por hora y sitio y registra los supuestos; el crecimiento de RT-09.03 ensaya tres veces la volumetría inicial sin rediseñar contratos ni identificadores.

Las reservas se serializan por agregado para evitar doble compromiso; los perfiles ERP, reconciliación, EDI y reportes tienen mamparos de concurrencia y colas independientes. Bajo sobrecarga, lectura degrada a copia fechada, escritura permanece pendiente y objetos se transfieren por reanudación. El usuario recibe estado y causal; nunca se descarta una operación confirmada para recuperar velocidad.

AL-PERF-01 incrementa carga en escalones hasta saturación y mide p50/p95/p99, errores, bloqueos de base, edad de cola, WAL, buffer y tiempo de recuperación. El ensayo detiene consumidores no críticos y comprueba que despacho conserva su capacidad reservada. Si el ERP limita primero, se mejora continuidad y presupuesto de emisión, no se presume que más Laravel lo corrige. El informe conserva versión, datos, distribución horaria, curvas, punto de quiebre y operaciones pendientes. Los umbrales de autoscaling y límites de infraestructura se trazan al componente físico; su costo permanece en la oferta económica.

<a id="anexo-seccion-42"></a>

## Anexo 4.1-U — Prueba de entrega, guía y acuses

<a id="anx-u"></a>

La solución propone tres registros separados: documento tributario emitido por ERP, evidencia operacional capturada por M6 y acuse recibido por el canal del destinatario. El SII exige portar la representación gráfica o impresa del DTE durante traslado; su acuse técnico no acredita por sí solo recepción de mercaderías (Servicio de Impuestos Internos [SII], s. f.-a). La evidencia móvil tampoco se transforma automáticamente en el recibo legal del destinatario.

<a id="anexo-seccion-43"></a>

### Mecanismo de recepción propuesto

M5 guarda folio, tipo, emisor, destinatario, versión de carga, documento y hash antes de liberar; el conductor dispone de representación gráfica o impresa conforme al procedimiento tributario. En el local, M6 registra nombre del receptor, identificación según política validada, lugar, hora, cantidades aceptadas/rechazadas y firma manuscrita capturada o alternativa operacional QR/fotografía. La cola cifrada conserva el objeto y su hash; la sincronización vincula la evidencia a entrega y guía.

Para un receptor electrónico habilitado se propone recibir su acuse por el mecanismo tributario del ERP o el canal EDI acordado, conservar el XML y su validación e identificar al firmante o emisor autorizado. Para el receptor al que corresponde constancia en representación impresa, se obtiene esa constancia y se conserva copia digital vinculada; no se obliga a una persona natural a poseer firma electrónica avanzada. La diferencia se fundamenta en la interpretación publicada por el SII sobre receptores electrónicos y no obligados (SII, 2018) y en su formato de recibo electrónico (SII, s. f.-b). Tributación valida el perfil aplicable de cada cliente antes de habilitarlo.

<a id="tab-estados-documentales"></a>

**Tabla A.24 — Estados de evidencia y consecuencias**

| **Hecho** | **Evidencia conservada** | **Consecuencia lógica** |
| --- | --- | --- |
| Guía disponible | Folio, documento y hash del ERP. | M5 comprueba correspondencia con carga vigente. |
| Salida liberada | Usuario, carga, guía y hora. | M6 recibe el viaje; no modifica el documento. |
| Recepción completa | Cantidades y POD íntegro. | M7 concilia; acuse tributario sigue su propio estado. |
| Recepción parcial | Líneas rechazadas, lotes y causal. | M8 registra devolución; ERP decide ajuste documental. |
| Negativa a firmar | Nombre si disponible, causal y constancia alternativa. | Entrega en excepción; no marcar acuse legal obtenido. |
| Acuse tributario recibido | Origen, XML/constancia, fecha y validación. | Vincular al DTE sin reemplazar el POD. |
| Resultado incierto | Clave original y último estado conocido. | Consultar antes de reenviar o solicitar otro documento. |

 Fuente: diseño lógico M5–M8, RT-16.14 y publicaciones del SII citadas.

AL-POD-01 ensaya recepción completa, parcial, persona sustituta, negativa a firmar, falta de señal y objeto alterado. Se acepta cuando cada hecho conserva autor y origen, la guía precede a la salida, el documento no cambia por reenvío y una evidencia operacional insuficiente no se declara acuse tributario. La FAQ del SII sobre contingencia es orientativa y no equivale a autorización para este contribuyente (SII, s. f.-c); el procedimiento de emisión bajo falla se cierra por AL-DTE-01.

<a id="anexo-seccion-44"></a>

## Anexo 4.1-V — Condiciones de aceptación y dependencias

<a id="anx-v"></a>

La propuesta conserva los requisitos obligatorios y distingue diseño, aprobación y ensayo. Las condiciones siguientes requieren evidencia del CLIENTE o cotejo integrado; su registro no afirma que exista aprobación ni consulta enviada. Las pruebas se ejecutan en Preproducción y antes de cada ola aplicable, con resultados observados y responsables identificados.

<a id="tab-condiciones-aceptacion"></a>

**Tabla A.25 — Decisiones necesarias para aceptación**

| **ID** | **Decisión o dependencia** | **Alternativa y evidencia requerida** | **Responsable** |
| --- | --- | --- | --- |
| AL-DTE-01 | Continuidad de guía en 96 salidas. | Emisor ERP disponible y evidencia local, o contingencia tributaria expresamente autorizada; ensayo con carga cambiada. | Operaciones, Tributación y ERP. |
| AL-BR-01 | Pérdida del sitio aislado. | Protección externa independiente con desfase ≤ 15 min, o resolución formal del escenario; AL-DR-01. | Arquitectura, Infraestructura y CLIENTE. |
| AL-MAP-01 | Correspondencia 3.3/3.4/4.1/4.2. | Inventario N cotejado con esquema, nombres y realizaciones exactas. | Arquitectura y dueños de capítulos. |
| AL-POD-01 | Perfil de receptor y validez de acuse. | Procedimiento por cliente y evidencia conforme al canal aplicable. | Tributación, Comercial y Seguridad. |
| AL-SLA-01 | Ventanas efectivas de terceros. | Acuerdos de contraparte, cuotas, mantenimiento y escalamiento en G/H. | Integración y CLIENTE. |
| AL-REV-01 | Revisión humana y A-6. | Identificar persona, sección, diagramas y qué verificó; acta y declaración consolidadas. | Equipo responsable del Subdocumento 4. |

 Fuente: requisitos y protocolos citados en 4.1; condiciones de aceptación de la propuesta.

La propuesta de continuidad del ERP mantiene un único emisor lógico y un solo registro de documentos: un mecanismo de alta disponibilidad o recuperación del proveedor debe conservar sus claves y folios. La ACL admite consultar resultados y descargar evidencia, sin cambiar el ERP ni emitir en nombre de otro sistema. Si el proveedor no puede cumplir y no existe contingencia aplicable, la salida afectada permanece bloqueada y el requisito de continuidad no se considera satisfecho.

La protección de datos críticos distingue enlace ordinario caído de aislamiento absoluto. Un camino independiente que sigue operativo permite sacar la copia durable; no debe compartir el dominio de falla del sitio. Si se pierden simultáneamente todos los medios y el origen, la brecha no desaparece al llamarla modo offline. El ensayo y la decisión formal mantienen el objetivo RPO de 15 minutos; la arquitectura física debe realizar la protección que se seleccione.

Las condiciones AL-OFF-01, AL-PERF-01 y AL-POD-01 tienen protocolo reproducible. Su ejecución se programa en la EDT y plan de calidad; la ausencia de resultados en una oferta previa a construir no se presenta como prueba ya aprobada. El equipo revisa el consolidado y asume el diseño antes de entregar; la herramienta no firma esa revisión.

<a id="anexo-seccion-45"></a>

## Referencias

International Organization for Standardization. (2022a). *ISO/IEC/IEEE 42010:2022: Software, systems and enterprise—Architecture description*. [https://www.iso.org/standard/74393.html](https://www.iso.org/standard/74393.html)

 International Organization for Standardization. (2019). *ISO 22301:2019: Security and resilience—Business continuity management systems—Requirements*. [https://www.iso.org/standard/75106.html](https://www.iso.org/standard/75106.html)

 International Organization for Standardization. (2025). *ISO/IEC 27031:2025: Cybersecurity—Information and communication technology readiness for business continuity*. [https://www.iso.org/standard/27031](https://www.iso.org/standard/27031)

National Institute of Standards and Technology. (2020). *Zero trust architecture* (Special Publication 800-207). U.S. Department of Commerce. [https://doi.org/10.6028/NIST.SP.800-207](https://doi.org/10.6028/NIST.SP.800-207)

Pontificia Universidad Católica de Valparaíso. (2026a). *Bases Técnicas del Caso 02—Logística* (TFEP-01/2026).

Pontificia Universidad Católica de Valparaíso. (2026b). *Bases Técnicas Transversales* (TFEP-01/2026).

 International Organization for Standardization. (2022b). *ISO/IEC 27001:2022*. [https://www.iso.org/standard/27001](https://www.iso.org/standard/27001)

 International Organization for Standardization. (2022c). *ISO/IEC 27002:2022*. [https://www.iso.org/standard/75652.html](https://www.iso.org/standard/75652.html)

 Laravel. (2026). *Release notes*. [https://laravel.com/framework/docs/releases](https://laravel.com/framework/docs/releases)

 PHP. (2026). *Supported versions*. [https://www.php.net/supported-versions.php](https://www.php.net/supported-versions.php)

 PostgreSQL. (2026). *Versioning policy*. [https://www.postgresql.org/support/versioning/](https://www.postgresql.org/support/versioning/)

 Angular. (2026a). *Release policy*. [https://angular.dev/reference/releases](https://angular.dev/reference/releases)

 Angular. (2026b). *Version compatibility*. [https://angular.dev/reference/versions](https://angular.dev/reference/versions)

 RabbitMQ. (2026). *Release information*. [https://www.rabbitmq.com/release-information](https://www.rabbitmq.com/release-information)

 Amazon Web Services. (s. f.-a). *Request validation for REST APIs*. [https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html)

 Amazon Web Services. (s. f.-b). *Lambda authorizers*. [https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html)

 Amazon Web Services. (s. f.-c). *Private integrations*. [https://docs.aws.amazon.com/apigateway/latest/developerguide/private-integration.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/private-integration.html)

 Servicio de Impuestos Internos. (2018). *Oficio 781: acuse de recibo*. [https://www.sii.cl/normativa_legislacion/jurisprudencia_administrativa/ley_impuesto_ventas/2018/ja781.htm](https://www.sii.cl/normativa_legislacion/jurisprudencia_administrativa/ley_impuesto_ventas/2018/ja781.htm)

 Servicio de Impuestos Internos. (s. f.-a). *Representación de guía de despacho electrónica*. [https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6599.htm](https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6599.htm)

 Servicio de Impuestos Internos. (s. f.-b). *Formato de recibos*. [https://www.sii.cl/factura_electronica/desc_19983.pdf](https://www.sii.cl/factura_electronica/desc_19983.pdf)

 Servicio de Impuestos Internos. (s. f.-c). *Contingencia de emisión*. [https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6624.htm](https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6624.htm)

Pontificia Universidad Católica de Valparaíso. (2026c). *Aclaraciones de licitación: índice obligatorio y consistencia de los subdocumentos*.

<a id="anexo-seccion-46"></a>

## Declaración de uso de IA

OpenAI Codex asistió la organización de los catálogos, redacción, cálculos de escenario y verificación de consistencia de estos anexos. La revisión humana final se realizará sobre el consolidado: las filas registran ese estado sin atribuir una aprobación inexistente. No se generaron nuevos diagramas dentro de estos anexos.

<a id="tab-uso-ia-anexos"></a>

**Tabla A.26 — Uso de IA en los anexos lógicos**

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

<a id="anexo-seccion-47"></a>

### Detalle por apartado del cuerpo

La herramienta es OpenAI Codex en todas las filas. La revisión humana corresponde al consolidado; no se asigna una firma o resultado inexistente.

<a id="tab-ia-apartados"></a>

**Tabla A.27 — Declaración por apartado lógico**

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
