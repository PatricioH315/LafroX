<!-- Conversión fiel a Markdown. Los bloques [Descripción de imagen] y los separadores de página son notas de conversión; el resto corresponde al contenido original. Se conservan las referencias a páginas y los cortes de página del PDF. -->

---

<!-- Página 1 del PDF original -->

LafroX SpA

VERSIÓN FINAL PARA ENTREGA

> **[Descripción de imagen — logotipo y diseño de portada]**
> En la franja negra superior aparece el contorno naranja de una cabeza de zorro junto a «LafroX SpA» en blanco. A la derecha se lee «VERSIÓN FINAL PARA ENTREGA» en gris. El borde inferior de la franja es inclinado y tiene dos líneas naranjas separadas por una franja blanca. El resto de la portada tiene fondo blanco, títulos negros, líneas horizontales grises y un rótulo negro con texto blanco para «Sobre N.° 2 --- Oferta Técnica». Los datos del mandante y proponente se sitúan a la izquierda y los del representante legal a la derecha. En la zona de firma aparece una línea horizontal sin firma manuscrita visible.

LICITACIÓN PÚBLICA

# Licitación N.° TFEP-01/2026

Proyecto de Plataforma Digital de Misión Crítica

Caso 02 — Logística

Sobre N.° 2 --- Oferta Técnica

# Propuesta Técnica

## Anexos del Subdocumento 02

Anexos del Subdocumento 02 · Formulario T-7

| MANDANTE | REPRESENTANTE LEGAL |
| --- | --- |
| Distribuidora Puelche S.A. | Alex Aravena<br>Jefe de Proyecto y Apoderado<br>contacto@lafrox.cl<br>+56 32 250 4100 |

PROPONENTE

LafroX SpA

RUT 77.418.902-K

Av. Brasil 2241, Valparaíso

FECHA DE EMISIÓN

05 de octubre de 2026

FIRMA DEL REPRESENTANTE LEGAL

Alex Aravena

Jefe de Proyecto y Apoderado · LafroX SpA

LAFROX-Subdocumento2-Anexos.pdf

1

---

<!-- Página 2 del PDF original -->

LafroX SpA

> **[Descripción de imagen — elementos gráficos de página]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», sobre una línea horizontal gris. En el pie aparece una franja negra con borde superior naranja inclinado.

## Índice general

| Contenido | Página |
| --- | --- |
| Índice general | 2 |
| Lista de tablas | 3 |
| Lista de figuras | 4 |
| 2 Anexos del Subdocumento 2: Comprensión del problema y de la necesidad | 5 |
| Anexo 2.1: Listado de Requerimientos del Cliente | 5 |
| Anexo 2.2: Listado de Supuestos, Exclusiones y Restricciones | 7 |
| Anexo 2.3: Otros Listados (Actores del Ecosistema y Sistemas Legados) | 14 |

LafroX SpA

Propuesta Técnica

2

---

<!-- Página 3 del PDF original -->

LafroX SpA

## Lista de tablas

| Contenido | Página |
| --- | --- |
| Tabla 2.A.1 Catálogo consolidado de Requerimientos Funcionales del Caso 02. Fuente: Distribuidora Puelche S.A. (2026c); BTT. | 5 |
| Tabla 2.A.2 Requerimientos No Funcionales rectores del proyecto. Fuente: caso, cap. 10 y 15; BTT. | 7 |
| Tabla 2.A.3 Supuestos de formulación derivados de las decisiones abiertas del caso. Fuente: caso, sección 16.1. | 8 |
| Tabla 2.A.4 Supuestos propios del diagnóstico. Fuente: elaboración propia. | 11 |
| Tabla 2.A.5 Exclusiones explícitas del alcance del proyecto. Fuente: caso, cap. 11. | 12 |
| Tabla 2.A.6 Restricciones no negociables del Caso 02. Fuente: caso, cap. 10. | 13 |
| Tabla 2.A.7 Catálogo nominal extendido de los 19 actores del ecosistema Puelche. Fuente: caso, caps. 2, 4, 8 y 13. | 15 |
| Tabla 2.A.8 Inventario de sistemas legados de Distribuidora Puelche S.A. Fuente: caso, cap. 5. | 18 |

LafroX SpA

Propuesta Técnica

3

---

<!-- Página 4 del PDF original -->

LafroX SpA

> **[Descripción de imagen — elementos gráficos de página]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», sobre una línea horizontal gris. En el pie aparece una franja negra con borde superior naranja inclinado.

## Lista de figuras

LafroX SpA Propuesta Técnica 4

---

<!-- Página 5 del PDF original -->

CAPÍTULO 2

> **[Descripción de imagen — elemento gráfico de página]**
> En el borde inferior aparece una franja negra con una línea naranja inclinada en su borde superior.

# Anexos del Subdocumento 2: Comprensión del problema y de la necesidad

El presente documento recopila los listados detallados que sustentan el análisis del problema y de la necesidad presentado en el cuerpo del Subdocumento 2.

## Anexo 2.1: Listado de Requerimientos del Cliente

A partir de la narrativa del Caso 02, las entrevistas a los actores clave y las Bases Técnicas Transversales, se identifican catorce familias funcionales prioritarias y cinco condiciones no funcionales rectoras. Los códigos F-01 a F-14 identifican familias de síntesis de este anexo; el catálogo atómico y sus códigos RF/RNF se desarrollan en el Subdocumento 3 y en el Formulario T-12.

Tabla 2.A.1 Catálogo consolidado de Requerimientos Funcionales del Caso 02. Fuente: Distribuidora Puelche S.A. (2026c); BTT.

| Familia | Nombre del Requerimiento | Descripción Operativa y Criterio de Verificación | Prioridad | Etapa |
| --- | --- | --- | --- | --- |
| F-01 | Preventa Móvil Desconectada | Toma de pedidos en terreno durante un turno completo sin señal, con stock y crédito visibles y sin pérdida ni duplicación de pedidos al recuperar la conexión. | Crítica | Etapa 1 |
| F-02 | Recepción y Control de Lotes | Captura obligatoria de identificadores GS1, lote y fecha de vencimiento en la recepción de cada instalación antes de autorizar el ingreso físico. | Crítica | Etapa 1 |

continúa en la página siguiente

LafroX SpA Propuesta Técnica 5

---

<!-- Página 6 del PDF original -->

LafroX SpA Anexos del Subdocumento 2: Comprensión del problema y de la necesidad

> **[Descripción de imagen — elementos gráficos de página]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», sobre una línea horizontal gris. En el pie aparece una franja negra con borde superior naranja inclinado.

Tabla 2.A.1 — continuación

| Familia | Nombre del Requerimiento | Descripción Operativa y Criterio de Verificación | Prioridad | Etapa |
| --- | --- | --- | --- | --- |
| F-03 | Gestión de Bodega y FEFO | Control de existencias físicas y asignación de despachos bajo lógica estricta First Expired, First Out en cámaras de frío (-22 °C) y secos. | Alta | Etapa 1 |
| F-04 | Picking por Olas en Almacén | Generación y consolidación de hojas de preparación digitales por zonas de almacenamiento, reduciendo traslados y tiempos de armado nocturno. | Alta | Etapa 1 |
| F-05 | Cross-Docking Controlado | Registro y control de la transferencia entre recepción y despacho mediante lectura de unidades logísticas, con medición del tiempo real del proceso y de sus excepciones. | Alta | Etapa 1 |
| F-06 | Planificación Dinámica de Rutas | Propuesta y secuenciación de rutas según capacidad, zonas, ventanas horarias y restricciones de terreno, conservando la corrección manual y capturando las heurísticas del planificador. | Alta | Etapa 1 |
| F-07 | Telemetría y Control de Frío | Monitoreo continuo de temperatura vehicular y en cámaras fijas con registro inmutable y alertas automáticas graduadas ante excursión térmica. | Crítica | Etapa 1 |
| F-08 | Entrega Digital y POD | Captura en terreno de la prueba de entrega con firma en pantalla o evidencia alternativa, georreferenciación y registro estructurado de devoluciones o rechazos. | Crítica | Etapa 1 |

continúa en la página siguiente

LafroX SpA Propuesta Técnica 6

---

<!-- Página 7 del PDF original -->

LafroX SpA Anexos del Subdocumento 2: Comprensión del problema y de la necesidad

> **[Descripción de imagen — elementos gráficos de página]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», sobre una línea horizontal gris. En el pie aparece una franja negra con borde superior naranja inclinado.

Tabla 2.A.1 — continuación

| Familia | Nombre del Requerimiento | Descripción Operativa y Criterio de Verificación | Prioridad | Etapa |
| --- | --- | --- | --- | --- |
| F-09 | Acuse de Recibo Legal de GDE | Integración bidireccional con ERP para certificar el acuse de recibo de la Guía de Despacho Electrónica ante el SII con mérito ejecutivo. | Alta | Etapa 1 |
| F-10 | Conciliación de Efectivo | Registro del cobro en el local y cuadratura de la recaudación al retorno, con causales tipificadas y responsable identificado para toda diferencia. | Alta | Etapa 1 |
| F-11 | Trazabilidad y Retiro Sanitario | Identificación de la trayectoria completa de un lote, desde el proveedor hasta el cliente, con la lista de clientes afectados en menos de 2 horas. | Crítica | Etapa 1 |
| F-12 | Autoatención de Clientes | Canal de consulta para los clientes que dispongan de conectividad, sin exigir internet, dispositivo propio ni pago electrónico al canal tradicional. | Media | Etapa 2 |
| F-13 | Integración EDI Canal Moderno | Intercambio electrónico estándar GS1/EDI de órdenes de compra y avisos de despacho que la principal cadena exigirá desde enero de 2029. | Alta | Etapa 2 |
| F-14 | Analítica de Costo de Servir | Modelación granular del costo real de distribución por cliente, canal, ruta y tipología de carga, superando el prorrateo estático de 2016. | Media | Etapa 2 |

LafroX SpA Propuesta Técnica 7

---

<!-- Página 8 del PDF original -->

LafroX SpA Anexos del Subdocumento 2: Comprensión del problema y de la necesidad

Tabla 2.A.2 Requerimientos No Funcionales rectores del proyecto. Fuente: caso, cap. 10 y 15; BTT.

| Código | Dimensión de Calidad | Criterio y Métrica de Aceptación | Estándar / Base |
| --- | --- | --- | --- |
| RNF-DISP | Disponibilidad del Servicio | Disponibilidad mensual ≥ 99,95 % para los componentes de infraestructura y ≥ 99,9 % para la transacción crítica de extremo a extremo. | BTT, §7.2; Art. 78° BA |
| RNF-REND | Sincronización tras reconexión | Sincronización móvil completa en un máximo de 10 minutos tras 14 horas sin señal y sincronización de un centro de distribución en un máximo de 2 horas tras 24 horas desconectado. | Caso, Cap. 15; BTT, RT-03.12 |
| RNF-RESIL | Autonomía Desconectada | Capacidad de operación autónoma en terminales móviles de 14 horas de turno y en centros de distribución de ≥ 24 horas sin enlace WAN. | Caso, Cap. 10; BTT, RT-03.10 |
| RNF-SEG | Ciberseguridad y Privacidad | Cifrado de datos locales y en tránsito, autenticación multifactor y preparación para el cumplimiento de Ley 21.719 desde su entrada en vigencia. | ISO/IEC 27001; Ley 21.719 |
| RNF-DR | Continuidad y Recuperación | Centro de datos secundario con RTO ≤ 4 horas y RPO ≤ 15 minutos, validado mediante simulacros semestrales obligatorios. | BTT, RT-07.04 y RT-07.07 |

## Anexo 2.2: Listado de Supuestos, Exclusiones y Restricciones

La Tabla 2.A.3 registra como supuestos de formulación las dieciséis decisiones que el numeral 16.1 del caso deja abiertas y que LafroX resuelve; el supuesto S-N responde a la decisión N (Distribuidora Puelche S.A., 2026c, sección 16.1). Cada fila explicita la conducta adoptada, la consecuencia que asume el diseño, el efecto si el supuesto resulta falso y la instancia del CLIENTE que lo valida. La trazabilidad a requisitos detallados se desarrolla en el Subdocumento 3, Anexo 3.C.

LafroX SpA Propuesta Técnica 8

---

<!-- Página 9 del PDF original -->

LafroX SpA Anexos del Subdocumento 2: Comprensión del problema y de la necesidad

Tabla 2.A.3 Supuestos de formulación derivados de las decisiones abiertas del caso. Fuente: caso, sección 16.1.

| ID | Supuesto adoptado | Consecuencia asumida | Si resulta falso | Validación |
| --- | --- | --- | --- | --- |
| S-01 | OTIF considera cumplida solo la entrega del 100 % de ítems y unidades dentro de la fecha y ventana pactadas. | Toda entrega parcial o tardía se registra como incumplida, con causal; fill rate y perfect order se miden por separado. | Cambia la fórmula de OTIF y su línea base; se recalculan las metas. | Gerencia Comercial y de Operaciones, mes 1. |
| S-02 | La unidad de trazabilidad sanitaria es el lote del proveedor; el SSCC identifica la unidad logística asociada. | La recepción captura lote y vencimiento, y el retiro sanitario se consulta hacia atrás y hacia adelante por lote. | Se redefinen la captura en recepción y la consulta de retiro. | Jefa de Calidad, mes 1. |
| S-03 | Ante local cerrado, el conductor registra el intento y el sistema reagenda a la próxima ventana disponible; no se entrega a terceros. | Si el cliente continúa ausente, la mercadería retorna al centro de distribución con trazabilidad del evento. | Cambia el flujo de reentrega. | Gerencia de Operaciones, levantamiento de reglas. |
| S-04 | La excursión térmica se parametriza por tipo de producto. Una excursión menor y transitoria genera una alerta preventiva; una crítica y sostenida hace que el sistema bloquee preventivamente el lote. Calidad decide liberar, bloquear o rechazar. | El sistema no invalida automáticamente el producto y el conductor no decide su destino sanitario. | Si la autoridad exige invalidación automática, cambia el tratamiento en ruta. | Jefa de Calidad, mes 2. |
| S-05 | Cada transportista confirma conductor y vehículo antes del despacho; el conductor real se autentica al iniciar la ruta. | La rotación sin aviso queda resuelta mediante la vinculación auditada entre persona, vehículo y viaje. | Sin confirmación previa, la vinculación se hace en el andén. | Acuerdo con cada una de las 10 empresas transportistas. |

continúa en la página siguiente

LafroX SpA Propuesta Técnica 9

---

<!-- Página 10 del PDF original -->

LafroX SpA Anexos del Subdocumento 2: Comprensión del problema y de la necesidad

> **[Descripción de imagen — elementos gráficos de página]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», sobre una línea horizontal gris. En el pie aparece una franja negra con borde superior naranja inclinado.

Tabla 2.A.3 — continuación

| ID | Supuesto adoptado | Consecuencia asumida | Si resulta falso | Validación |
| --- | --- | --- | --- | --- |
| S-06 | Se mantiene el efectivo y se reduce mediante medios alternativos; cada camión realiza rendición digital individual. | Toda diferencia exige causal tipificada y responsable identificado antes del cierre. | Si el CLIENTE reduce el uso de efectivo mediante medios alternativos voluntarios, la conciliación se conserva con menor volumen de operaciones; el canal tradicional mantiene la posibilidad de pagar en efectivo. | Gerente de Finanzas, mes 1. |
| S-07 | El costo de servir se calcula por actividad, entrega y cliente, usando distancia, tiempos, volumen, devoluciones y activos retornables. | Los clientes no rentables se segmentan para revisar frecuencia y pedido mínimo; no se eliminan automáticamente. | Otra metodología cambia los datos que deben capturarse desde la Etapa 1. | Gerente de Finanzas, antes del mes 13. |
| S-08 | El stock se reserva al confirmar el pedido en el servidor central, por orden cronológico. | En modo desconectado el stock es indicativo; los conflictos se resuelven al sincronizar y se notifica el quiebre. | Una reserva local cambia la resolución de conflictos. | Gerencia Comercial, levantamiento de reglas. |
| S-09 | Rige el precio acordado al capturar el pedido y registrado conforme a las condiciones comerciales autorizadas. | Una actualización posterior de la lista no modifica el importe pactado; el ERP recibe y conserva el precio del pedido. | Una diferencia de integración se bloquea y concilia antes de facturar; no se aplica automáticamente la lista del despacho. | Gerencia Comercial, mes 2. |
| S-10 | Los 68.000 canastillos y 9.400 pallets se controlan por saldo de cliente y transportista, sin serialización unitaria. | Entregas y devoluciones actualizan la cuenta corriente; los excesos y pérdidas generan alertas e informes. | La serialización exige otra captura y otro hardware. | Gerencia de Operaciones, mes 2. |

continúa en la página siguiente

LafroX SpA Propuesta Técnica 10

---

<!-- Página 11 del PDF original -->

LafroX SpA Anexos del Subdocumento 2: Comprensión del problema y de la necesidad

Tabla 2.A.3 — continuación

| ID | Supuesto adoptado | Consecuencia asumida | Si resulta falso | Validación |
| --- | --- | --- | --- | --- |
| S-11 | El maestro interno de Puelche prevalece y conserva equivalencias e historial de cambios de códigos externos. | Los códigos sin equivalencia quedan en una bandeja de excepciones y no crean una segunda verdad de producto. | Otro maestro rector cambia las equivalencias. | Jefe de TI y Gerencia Comercial, mes 2. |
| S-12 | La devolución se registra en la entrega con SKU, cantidad y motivo; el ERP emite la nota de crédito cuando corresponde. | La solución transmite el evento y la evidencia, sin transformarse en un segundo emisor tributario. | El ERP se mantiene como único emisor en cualquier alternativa. | Gerente de Finanzas, mes 2. |
| S-13 | No se instalan cámaras en cabina. Se integra la telemetría existente para fines operacionales, con controles de privacidad. El uso del GPS para control de jornada queda sujeto a acuerdo previo con el sindicato. | La telemetría operacional se utiliza para gestionar vehículo, ruta y carga, sin destinar sus datos al control de jornada mientras no exista el acuerdo. Los controles de privacidad consideran que la ubicación del vehículo puede revelar la del conductor. | Si no se alcanza el acuerdo, se mantiene la telemetría operacional con controles de privacidad y no se utiliza GPS para control de jornada. | Jefe de TI y Gerencia de Operaciones, durante el levantamiento, para definir finalidades y controles de privacidad; sindicato, antes de habilitar el uso del GPS para control de jornada. |
| S-14 | El WMS de 2013 se reemplaza por la solución común para las instalaciones, con migración y reversión. | Se elimina la fragmentación entre WMS y planillas, asumiendo el esfuerzo de migrar y reconciliar datos. | Si se conserva, se agrega una integración y cambia la migración. | Jefa de Bodega y Jefe de TI, mes 3. |
| S-15 | La prueba principal es la firma en pantalla; si no es posible, se captura fotografía, nombre del receptor o confirmación QR vinculada a la GDE. | La alternativa conserva fecha, ubicación e identidad disponible y se articula con el acuse tributario. | Otra evidencia cambia la captura en la entrega. | Gerente de Finanzas, mes 2. |

continúa en la página siguiente

LafroX SpA Propuesta Técnica 11

---

<!-- Página 12 del PDF original -->

LafroX SpA Anexos del Subdocumento 2: Comprensión del problema y de la necesidad

Tabla 2.A.3 — continuación

| ID | Supuesto adoptado | Consecuencia asumida | Si resulta falso | Validación |
| --- | --- | --- | --- | --- |
| S-16 | El conocimiento del planificador se captura en la Etapa 1 y se parametriza en el motor de rutas antes de su jubilación. | El sistema propone rutas y conserva corrección manual; cada regla transferida queda documentada y probada en terreno. | Si el planificador se retira antes, las rutas se validan con su ayudante y con datos históricos. | Gerencia de Operaciones y planificador, mes 1. |

Además de las decisiones del caso, LafroX formula tres supuestos propios sobre el diagnóstico. Sostienen cifras e hipótesis del cuerpo de este subdocumento que el caso no permite confirmar.

Tabla 2.A.4 Supuestos propios del diagnóstico. Fuente: elaboración propia.

| ID | Supuesto | Fundamento | Si resulta falso | Validación |
| --- | --- | --- | --- | --- |
| SP-01 | La tasa de reentregas de 4,2 % se aplica sobre las ≈ 1.400 entregas diarias de un día hábil normal, y cada reentrega corresponde a una entrega. | Caso, secciones 2.2 y 7.1. | Cambia la estimación de ≈ 59 reentregas diarias. | Gerencia de Operaciones, con los registros de reentrega, mes 1. |
| SP-02 | La brecha de 16 horas entre la reducción prometida y la lograda en cross-docking se origina, al menos en parte, en la consolidación, la desconsolidación y la validación manual. | Sospecha interna registrada en el caso: el tiempo se perdería en la consolidación en Talca, sin datos que lo confirmen (cap. 3); descripción de las plataformas (sección 2.3) y tabla 7.2. | La mejora del control de cross-docking no reduce la brecha y la causa debe buscarse en el transporte troncal o en las esperas. | Medición de tiempos en Talca y en las tres plataformas, meses 1 a 3. |

continúa en la página siguiente

LafroX SpA Propuesta Técnica 12

---

<!-- Página 13 del PDF original -->

LafroX SpA Anexos del Subdocumento 2: Comprensión del problema y de la necesidad

> **[Descripción de imagen — elementos gráficos de página]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», sobre una línea horizontal gris. En el pie aparece una franja negra con borde superior naranja inclinado.

Tabla 2.A.4 — continuación

| ID | Supuesto | Fundamento | Si resulta falso | Validación |
| --- | --- | --- | --- | --- |
| SP-03 | La falta de registro de lote no se limita al producto del retiro de marzo, aunque su magnitud general se desconoce. | El lote se anota «en un campo de texto libre, cuando se anota» (caso, sección 4.1). | La brecha de captura es menor y la meta de 100 % se alcanza antes. | Jefa de Calidad, con la medición de cobertura de lote en las recepciones del mes 1. |

La Tabla 2.A.5 detalla las exclusiones explícitas de alcance que delimitan la responsabilidad contractual del proponente, garantizando la viabilidad del proyecto.

Tabla 2.A.5 Exclusiones explícitas del alcance del proyecto. Fuente: caso, cap. 11.

| N° | Exclusión de Alcance | Justificación Técnica y Contractual | Manejo / Mitigación |
| --- | --- | --- | --- |
| E-01 | Reemplazo o modificación del sistema de gestión empresarial. | El ERP de 2017 sigue siendo el registro contable y tributario y conserva sus módulos. | Integración desacoplada y una sola fuente oficial. |
| E-02 | Administración de remuneraciones y recursos humanos. | Estas funciones residen en el sistema de gestión empresarial. | Solo se integran identidades o datos mínimos cuando un proceso lo requiera. |
| E-03 | Punto de venta para el local del cliente. | El caso no solicita operar la venta interna del almacenero. | Se ofrece autoatención sin convertir la solución en POS del cliente. |
| E-04 | Comercio electrónico al consumidor final. | El alcance atiende la relación B2B de Puelche con sus clientes. | Los canales digitales se limitan al catálogo, pedido y seguimiento B2B. |
| E-05 | Administración contractual o pago de transportistas. | El contrato exige integración operacional, no liquidar contratos de transporte. | Se intercambian asignaciones, eventos y evidencias del viaje. |

continúa en la página siguiente

LafroX SpA Propuesta Técnica 13

---

<!-- Página 14 del PDF original -->

LafroX SpA Anexos del Subdocumento 2: Comprensión del problema y de la necesidad

Tabla 2.A.5 — continuación

| N° | Exclusión de Alcance | Justificación Técnica y Contractual | Manejo / Mitigación |
| --- | --- | --- | --- |
| E-06 | Diseño de la red logística. | La ubicación de centros de distribución y plataformas no está en discusión. | El despliegue se adapta a las instalaciones que se confirmen con el CLIENTE: cinco según las entrevistas y seis según la volumetría del caso. |
| E-07 | Automatización robotizada de bodega. | No se solicitan robots ni transportadores. | Se digitalizan recepción, ubicación, preparación y despacho con apoyo móvil. |
| E-08 | Gestión mecánica de la flota. | Mantenciones, repuestos y condición mecánica permanecen fuera del alcance. | Se integra la telemetría existente para fines operacionales. |
| E-09 | Compra del hardware de terreno por el proponente. | El CLIENTE adquiere dispositivos, lectores, impresoras y sensores. | El proponente especifica cantidades y características en la especificación de implementos de la oferta. |

La Tabla 2.A.6 reproduce las doce restricciones no negociables que condicionan la solución. No son supuestos ni exclusiones: su cumplimiento es obligatorio y debe demostrarse en arquitectura, plan de trabajo y pruebas.

Tabla 2.A.6 Restricciones no negociables del Caso 02. Fuente: caso, cap. 10.

| N° | Restricción | Implicación para la propuesta |
| --- | --- | --- |
| R-01 | Entre 05:30 y 07:00 salen 96 camiones y el despacho no puede detenerse. | Continuidad y cambios fuera de la ventana crítica. |
| R-02 | El centro de distribución debe recibir, preparar y despachar durante un corte del enlace. | Operación local autónoma durante al menos 24 horas. |
| R-03 | Preventa y reparto deben funcionar un turno completo sin señal. | Persistencia local por 14 horas y sincronización posterior controlada. |
| R-04 | El ERP no se reemplaza ni modifica y sigue emitiendo los documentos tributarios. | Integración desacoplada sin segundo registro contable ni tributario. |

continúa en la página siguiente

LafroX SpA Propuesta Técnica 14

---

<!-- Página 15 del PDF original -->

LafroX SpA Anexos del Subdocumento 2: Comprensión del problema y de la necesidad

Tabla 2.A.6 — continuación

| N° | Restricción | Implicación para la propuesta |
| --- | --- | --- |
| R-05 | No se exige internet, dispositivo propio ni pago electrónico al canal tradicional. | La operación se completa con recursos de Puelche y admite efectivo. |
| R-06 | La solución opera con 54 camiones de diez transportistas y conductores que rotan sin aviso. | Identificación rápida y acuerdo operacional con cada transportista. |
| R-07 | Los dispositivos de cámara operan a -22 °C y sin señal. | Equipos aptos para frío, guantes y trabajo desconectado. |
| R-08 | No se interviene del 1 al 25 de septiembre, durante diciembre ni los tres primeros días hábiles de cada mes. | Despliegues, pruebas y reversión se programan fuera de esos períodos. |
| R-09 | TI dispone de cuatro personas. | Toda especialidad permanente que no exista en el CLIENTE se presta como servicio. |
| R-10 | El sindicato objetó cámaras en cabina y control de jornada por GPS. | La propuesta excluye cámaras en cabina y condiciona el uso del GPS para control de jornada a un acuerdo previo con el sindicato. La telemetría operacional incorpora controles de privacidad. |
| R-11 | Preparación rota 38 % anual y trabaja en turno nocturno. | La interfaz y capacitación deben admitir aprendizaje breve y recambio frecuente. |
| R-12 | La emisión y el acuse de documentos tributarios electrónicos deben respetar la normativa vigente. | El diseño conserva validez legal, evidencia y trazabilidad con el ERP. |

## Anexo 2.3: Otros Listados (Actores del Ecosistema y Sistemas Legados)

La Tabla 2.A.7 presenta el catálogo nominal y extendido de los 19 actores que componen el ecosistema humano y operacional de Distribuidora Puelche S.A.

LafroX SpA Propuesta Técnica 15

---

<!-- Página 16 del PDF original -->

LafroX SpA Anexos del Subdocumento 2: Comprensión del problema y de la necesidad

> **[Descripción de imagen — elementos gráficos de página]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», sobre una línea horizontal gris. En el pie aparece una franja negra con borde superior naranja inclinado.

Tabla 2.A.7 Catálogo nominal extendido de los 19 actores del ecosistema Puelche. Fuente: caso, caps. 2, 4, 8 y 13.

| Actor / Cargo | Rol en el Ecosistema | Ineficiencia que enfrenta en la situación actual | Influencia | Interés | Estrategia de participación |
| --- | --- | --- | --- | --- | --- |
| Gerenta General | Patrocinadora y Alta Dirección | Retiro de 9 días con suspensión del proveedor de lácteos; una operación que sigue dependiendo de «una libreta»; advierte por la jubilación del planificador. | Muy Alta | Muy Alto | Preside el comité que arbitra prioridades y valida el cierre de cada etapa. |
| Gerente Comercial | Conducción de Ventas | Competidor con entrega en 24 horas y pedido autónomo; preventistas sin stock; condiciones 2029 de la principal cadena. | Muy Alta | Muy Alto | Valida la promesa de entrega y las reglas comerciales en el levantamiento. |
| Gerente de Operaciones | Ejecución Logística | Brecha no investigada entre la reducción prometida (24 h) y la observada (8 h) en cross-docking; promesa de 24 h que considera imposible. | Alta | Muy Alto | Participa en la medición de tiempos y aprueba cada cambio operacional antes de aplicarlo. |
| Gerente de Finanzas | Control Financiero | Diferencias de rendición de $4,2 millones al mes sin investigar; costo de servir prorrateado con un criterio de 2016. | Muy Alta | Muy Alto | Define las causales de diferencia y la metodología de costo de servir. |
| Jefa de Calidad | Aseguramiento Sanitario | Sin registro continuo de temperatura, observado por la autoridad; lote en texto libre; retiro de 9 días. | Alta | Muy Alto | Define la regla térmica y conduce el simulacro de retiro. |
| Jefa de Bodega | Custodia de Inventarios | Conteo cíclico con 2,3 % de diferencia y merma de 1,7 %; preparación nocturna con planillas impresas. | Alta | Muy Alto | Valida los flujos de bodega en el turno de noche. |
| Jefe de TI | Operación Tecnológica | Equipo de 4 personas; la fibra se corta cuatro veces al año; interfaces del ERP y del WMS sin documentación. | Alta | Muy Alto | Valida interfaces y recibe la transferencia de operación. |

continúa en la página siguiente

LafroX SpA Propuesta Técnica 16

---

<!-- Página 17 del PDF original -->

LafroX SpA Anexos del Subdocumento 2: Comprensión del problema y de la necesidad

Tabla 2.A.7 — continuación

| Actor / Cargo | Rol en el Ecosistema | Ineficiencia que enfrenta en la situación actual | Influencia | Interés | Estrategia de participación |
| --- | --- | --- | --- | --- | --- |
| Planificador de Rutas | Diagramación Logística | Planilla de once hojas que solo él entiende; 3,5 horas diarias; jubilación en dos años. | Alta | Muy Alto | Participa en talleres de reglas con reconocimiento formal de su conocimiento. |
| Preventistas (62 personas) | Captura de Pedidos | Aplicación de 2016 sin stock, crédito ni historial; 7,8 % de las líneas con quiebre de stock. | Alta | Alto | Prueban los cambios en su propia ruta antes de adoptarlos. |
| Tripulación propia y peoneta (84 personas) | Despacho y Cobranza | Rendición en caja a la mañana siguiente; guías en papel (1,1 % extraviadas); termógrafo manual con tres lecturas por viaje. | Alta | Alto | Validan el registro de entrega y la rendición antes de su adopción. |
| Conductores externos (aprox. 160 personas) | Flota Tercerizada | No son trabajadores de la compañía; rotan sin aviso; sus camiones no tienen telemetría. | Alta | Alto | Incorporación acordada con cada transportista. |
| Empresas Transp. (10 empresas) | Proveedores de Flete | 54 camiones, 10 con frío, que la compañía no controla. | Media-alta | Alto | Acuerdo operacional con cada empresa. |
| Preparadores (120 personas) | Picking en Almacén | Turno de noche de 22:00 a 06:00; rotación de 38 %; cámara a −22 °C sin señal. | Alta | Alto | Aprendizaje en el puesto, compatible con la rotación. |
| Sindicato de Choferes | Representación Laboral | Objeción formal a las cámaras en cabina y al control de jornada por posicionamiento satelital. | Alta | Alto | Participación en la definición de finalidades y controles de privacidad de la telemetría; acuerdo previo antes de utilizar GPS para control de jornada. |

continúa en la página siguiente

LafroX SpA Propuesta Técnica 17

---

<!-- Página 18 del PDF original -->

LafroX SpA Anexos del Subdocumento 2: Comprensión del problema y de la necesidad

Tabla 2.A.7 — continuación

| Actor / Cargo | Rol en el Ecosistema | Ineficiencia que enfrenta en la situación actual | Influencia | Interés | Estrategia de participación |
| --- | --- | --- | --- | --- | --- |
| Canal Tradicional (11.600 clientes) | Clientes Almaceneros | No se les puede exigir internet, dispositivo ni pago electrónico; el 38 % de la venta del canal se cobra en efectivo; el competidor les ofrece pedido autónomo. | Muy alta | Alto | Se preserva su forma de compra y pago. |
| Food Service (2.100 clientes) | Hoteles y Restaurantes | Sensibles a la frescura y a la puntualidad; el año pasado un cliente rechazó un camión completo por sospecha de ruptura de la cadena de frío. | Muy alta | Alto | Levantamiento de sus ventanas de entrega y exigencias de evidencia. |
| Canal Moderno (500 puntos) | Cadenas de Retail | La principal cadena (11 % de la venta) exige desde enero de 2029 pedido electrónico, aviso de despacho, ventana de 30 minutos con penalización y prueba de entrega digital. | Muy alta | Alto | Levantamiento de condiciones por cadena. |
| Proveedores (180 empresas) | Suministro de Carga | Lote anotado en texto libre, cuando se anota; el proveedor de lácteos suspendió a Puelche por seis meses. | Media-alta | Alto | Aviso anticipado de requisitos de rotulado. |
| Autoridad Sanitaria | Fiscalización SEREMI | Observó en su última fiscalización la ausencia de registro continuo de temperatura. | Media-alta | Alto | Canal formal para entregar evidencia de trazabilidad y temperatura. |

La Tabla 2.A.8 resume los ocho sistemas y registros que operan actualmente en Distribuidora Puelche S.A., con el destino que el caso les asigna (Distribuidora Puelche S.A., 2026c, cap. 5).

LafroX SpA Propuesta Técnica 18

---

<!-- Página 19 del PDF original -->

LafroX SpA Anexos del Subdocumento 2: Comprensión del problema y de la necesidad

> **[Descripción de imagen — logotipo del encabezado]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», a la izquierda del título «Anexos del Subdocumento 2: Comprensión del problema y de la necesidad», sobre una línea horizontal gris.

Tabla 2.A.8 Inventario de sistemas legados de Distribuidora Puelche S.A. Fuente: caso, cap. 5.

| Sistema / Aplicación | Tipo | Año de inicio | Estado operacional y deficiencias | Destino según el caso |
| --- | --- | --- | --- | --- |
| ERP principal | Sistema de gestión empresarial | 2017 | Ventas, facturación, cobranza, contabilidad, compras, inventario valorizado y remuneraciones; interfaces no documentadas. | Se mantiene como registro contable y tributario; se integra sin modificarlo. |
| Facturación electrónica | Documentos tributarios electrónicos | No informado | Emite facturas, guías de despacho y notas de crédito, integrada al ERP. | Se mantiene integrada al ERP; la solución no emite documentos tributarios. |
| WMS de bodega | Sistema de gestión de almacén | 2013 | Solo en Talca; Concepción usa planillas y las plataformas no controlan inventario. | Decisión del proponente: reemplazo progresivo con migración y reversión (Anexo 2.2, S-14). |
| Aplicación de preventa | Desarrollo a medida | 2016 | Proveedor desaparecido; sin soporte; sin stock, crédito ni historial. | Se reemplaza. |
| Planilla de rutas | Planilla de cálculo | No informado | Depende de un usuario único que se jubila en dos años. | Se reemplaza. |
| Planilla de reposición | Planilla de cálculo | No informado | Sugerencia de compra con ajuste manual por temporada. | Se reemplaza. |
| Telemetría de flota | Plataforma de un tercero | No informado | Posición y velocidad de los 42 camiones propios; los 54 de transportistas no están cubiertos; condiciones de acceso a los datos no claras. | Se mantiene como fuente y debe integrarse. |
| Planillas y cuadernos | Registros manuales | No informado | Lotes, conteo, faltantes, devoluciones, envases, temperatura, rendición de efectivo y costo por zona. | Deben desaparecer como sistema de registro. |

LafroX SpA Propuesta Técnica 19


## Referencias

Bases Administrativas TFEP-01/2026; Bases Técnicas Transversales; Caso 02 — Logística; Aclaraciones de licitación; SD3 y SD7 para las correspondencias de alcance y gobierno.

## Declaración de uso de IA

Actualización del 6 de octubre de 2026: Codex apoyó Alineación de S-09 con conservación del precio capturado y control de diferencias ERP. Participación alta en el texto ajustado, sin imágenes nuevas. No consta revisión humana de esta actualización; las comprobaciones documentales no acreditan aprobación del CLIENTE.
