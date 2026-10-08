
LafroX SpA

VERSIÓN FINAL PARA ENTREGA

LICITACIÓN PÚBLICA

# Licitación N.° TFEP-01/2026

Proyecto de Plataforma Digital de Misión Crítica

Caso 02 — Logística

Sobre N.° 2 --- Oferta Técnica

# Propuesta Técnica

## Subdocumento 02 — Problema y necesidad

Subdocumento 02 · Formulario T-7

| MANDANTE | REPRESENTANTE LEGAL |
| --- | --- |
| Distribuidora Puelche S.A. | Alex Aravena<br>Jefe de Proyecto y Apoderado<br>contacto@lafrox.cl<br>+56 32 250 4100 |

PROPONENTE

RUT 77.418.902-K

Av. Brasil 2241, Valparaíso

FECHA DE EMISIÓN

05 de octubre de 2026

FIRMA DEL REPRESENTANTE LEGAL

Alex Aravena

Jefe de Proyecto y Apoderado · LafroX SpA

## Índice general

| Contenido | Página |
| --- | --- |
| Índice general | 2 |
| Lista de tablas | 3 |
| Lista de figuras | 4 |
| 2 Introducción al Problema y Necesidad | 5 |
| 2.1 Resumen Ejecutivo del problema | 5 |
| 2.2 Comprensión del problema y de la necesidad | 6 |
| 2.2.1 Los tres problemas entrelazados | 6 |
| 2.2.2 Contexto operacional, normativo y estacionalidad | 7 |
| 2.2.3 Arbitraje de tensiones operacionales y comerciales | 8 |
| 2.3 Dimensionamiento del problema | 9 |
| 2.3.1 Cuantificación del impacto operacional y financiero | 9 |
| 2.3.2 El enigma del cross-docking y los seis procesos AS-IS | 12 |
| 2.3.2.1 Proceso 1: Preventa y Toma de Pedidos AS-IS | 12 |
| 2.3.2.2 Proceso 2: Recepción de Mercadería y Control de Lotes AS-IS | 13 |
| 2.3.2.3 Proceso 3: Preparación de Pedidos y Cross-Docking AS-IS | 14 |
| 2.3.2.4 Proceso 4: Planificación de Rutas AS-IS | 15 |
| 2.3.2.5 Proceso 5: Reparto y Entrega AS-IS | 16 |
| 2.3.2.6 Proceso 6: Rendición y Cobranza AS-IS | 17 |
| 2.4 Actores y Grupos de Interés | 18 |
| 2.5 Resumen de Requerimientos, Supuestos, Exclusiones y Restricciones | 20 |
| 2.5.1 Resumen y análisis de requerimientos del cliente | 20 |
| 2.5.2 Supuestos de ingeniería formulados por LafroX | 20 |
| 2.5.3 Exclusiones y restricciones no negociables | 21 |
| Referencias | 22 |
| Declaración de uso de IA | 22 |

## Lista de tablas

| Contenido | Página |
| --- | --- |
| Tabla 2.1 Dimensionamiento cuantitativo de las brechas operacionales de Distribuidora Puelche S.A. Fuente: Elaboración propia a partir de Distribuidora Puelche S.A. (2026c), tablas 7.1 a 7.3 y sección 4.8. | 9 |
| Tabla 2.2 Matriz de síntesis de actores, tensiones operacionales y estrategia de gestión. Fuente: elaboración propia a partir de Distribuidora Puelche S.A. (2026c), caps. 2, 4, 10 y 13. | 18 |
| Tabla 2.3 Síntesis de restricciones no negociables del caso. Fuente: Distribuidora Puelche S.A. (2026c), cap. 10 y sección 13.3. | 21 |
| Tabla 2.4 Declaración de uso de IA por sección del Subdocumento 2. Fuente: registro del equipo. | 22 |

## Lista de figuras

| Contenido | Página |
| --- | --- |
| Figura 2.1 Proceso de Preventa y Toma de Pedidos AS-IS. Fuente: elaboración propia a partir de Distribuidora Puelche S.A. (2026c), capítulos 4 y 8. | 13 |
| Figura 2.2 Proceso de Recepción de Mercadería y Control de Lotes AS-IS. Fuente: elaboración propia a partir de Distribuidora Puelche S.A. (2026c), capítulos 4 y 8. | 14 |
| Figura 2.3 Proceso de Preparación y Cross-Docking AS-IS. Fuente: elaboración propia a partir de Distribuidora Puelche S.A. (2026c), capítulos 4 y 8. | 15 |
| Figura 2.4 Proceso de Planificación de Rutas AS-IS. Fuente: elaboración propia a partir de Distribuidora Puelche S.A. (2026c), capítulos 4 y 8. | 16 |
| Figura 2.5 Proceso de Reparto y Entrega AS-IS. Fuente: elaboración propia a partir de Distribuidora Puelche S.A. (2026c), capítulos 4 y 8. | 16 |
| Figura 2.6 Proceso de Rendición y Cobranza AS-IS. Fuente: elaboración propia a partir de Distribuidora Puelche S.A. (2026c), capítulos 4 y 8. | 17 |

CAPÍTULO 2

# Introducción al Problema y Necesidad

El presente subdocumento expone el diagnóstico integral, operacional y estratégico de Distribuidora Puelche S.A. en el marco del caso. Se analiza la estructura de su modelo logístico actual (AS-IS), caracterizado por una profunda fragmentación de datos, procesos manuales en terreno y desacoples entre la promesa comercial y la capacidad física de distribución.

Este capítulo establece la línea base conceptual y cuantitativa para el resto de la propuesta: fundamenta los requerimientos funcionales y el alcance técnico, define los requerimientos no funcionales y de resiliencia, y delimita las restricciones operativas que condicionan la planificación de la implantación. El catálogo pormenorizado de requerimientos del cliente, el registro extendido de supuestos y exclusiones, y el inventario nominal de actores y sistemas legados se presentan en los Anexos 2.1 a 2.3 de este subdocumento.

## 2.1 Resumen Ejecutivo del problema

Distribuidora Puelche S.A. enfrenta una crisis de eficiencia y competitividad operacional producto de la obsolescencia y desarticulación de su ecosistema informático. Su operación integra los centros de distribución de Talca y Concepción y tres plataformas de cross-docking. La flota considera 42 camiones propios y 54 de diez transportistas. En reparto trabajan 84 conductores y peonetas propios y cerca de 160 conductores de transportistas, y se atienden 14.200 puntos de entrega. La operación actual exhibe un índice de entrega a tiempo y completa (OTIF) de 82,4 %, frente a una referencia de 95 % (2026c, tabla 7.1). Por tanto, el 17,6 % de los despachos no llega completo y a tiempo. Esto deteriora la relación con el canal tradicional y pone en riesgo a la principal cadena de supermercados, que representa el 11 % de la venta y fija nuevas condiciones desde enero de 2029 (2026c, cap. 1).

La raíz del problema no reside en un único sistema defectuoso, sino en un tejido heterogéneo y desconectado: un ERP implantado en 2017 cuyos módulos satélites de preventa fueron abandonados por su proveedor, un WMS de 2013 con soporte discontinuado y procesos críticos gobernados mediante planillas de cálculo y papel. Esta desconexión tecnológica genera tres impactos críticos inmediatos:

1. Vulnerabilidad sanitaria y regulatoria: El retiro preventivo de marzo de 2026 demoró 9 días y alcanzó 4.800 kg del lote 24-0217, con una pérdida directa de dinero. El proveedor suspendió a Puelche por seis meses de su lista de distribuidores autorizados; ese proveedor representa el 6 % de las ventas. En el producto involucrado, el 41 % de las recepciones no registraba lote en el sistema.

2. Fricción comercial y quiebre de preventa: El 7,8 % de las líneas de pedido tomadas en terreno presenta quiebre de stock, pues los 62 preventistas operan a ciegas mediante una aplicación móvil obsoleta sin visibilidad de inventario ni crédito en tiempo real.

3. Opacidad financiera y diferencias de rendición sin investigar: La empresa subsidia entregas ineficientes bajo un prorrateo de costo de servir estático fijado en 2016. La rendición manual diferida del efectivo genera diferencias no conciliadas; además, el 1,1 % mensual de las guías de despacho se extravía o queda ilegible; ante un reclamo de entrega no recibida, encontrar la guía toma en promedio 12 días.

Estas brechas establecen la necesidad que debe abordar la oferta: recuperar trazabilidad de lote, hacer confiable la promesa de entrega, disminuir la pérdida de información en terreno y disponer de una base objetiva para gestionar el costo de servir. El Capítulo 3 define la solución y el alcance que responderán a estas necesidades.

## 2.2 Comprensión del problema y de la necesidad

Esta sección descompone el problema en tres dimensiones, lo sitúa en su contexto operacional, normativo y estacional, y registra las tensiones entre áreas que la solución debe resolver.

### 2.2.1 Los tres problemas entrelazados

En concordancia con el análisis prescrito en las Bases de Licitación, la problemática de Puelche se descompone en tres dimensiones interconectadas que se retroalimentan mutuamente:

1. Habilitación sanitaria y comercial comprometida: El cumplimiento del Reglamento Sanitario de los Alimentos (Decreto 977) exige el control riguroso de la cadena de frío (congelados a −18 °C o menos; la cámara de congelado de Talca opera a −22 °C) (Ministerio de Salud, 1996) y la trazabilidad bidireccional inmediata de lotes. En la actualidad, el registro de temperatura es discontinuo e instrumentalizado por el propio conductor, sin alarmas automáticas ante excursiones térmicas. Al recibir mercadería de los 180 proveedores, el personal revisa las fechas de vencimiento por muestreo y registra el lote de manera incompleta, en un campo de texto libre. La trazabilidad depende del papel de recepción y de la memoria de quienes despacharon, sin estar disponible de forma consultable en los sistemas. Esta carencia expone a Puelche a sanciones de la autoridad sanitaria, que ya observó la ausencia de registro continuo de temperatura en su última fiscalización. También le impide acreditar ante el proveedor de lácteos la capacidad de trazabilidad que este exige para restablecer la relación tras la suspensión, que vence en septiembre de 2026.

2. Pérdida de competitividad del servicio: El nivel de servicio actual (OTIF 82,4 % y fill rate 91,3 %) está lejos de las referencias de 95 % y 97 % que el caso asocia a esos indicadores. Además, la principal cadena exigirá desde enero de 2029 pedido electrónico, aviso de despacho, ventana de entrega de 30 minutos con penalización y prueba de entrega digital.

Hoy Puelche entrega entre las 08:00 y las 18:00. Los clientes del canal tradicional (11.600 almacenes) y food service (2.100 puntos) enfrentan faltantes y retrasos. La falta de visibilidad en preventa y la rigidez de las rutas provocan reentregas equivalentes al 4,2 % de las entregas. Sobre la referencia de 1.400 entregas diarias, ello equivale a aproximadamente 59 reentregas al día (1.400 × 0,042 = 58,8).

3. Desconocimiento estructural del costo de servir: La fijación de precios y márgenes se calcula sobre un costo de transporte promedio estático que data de 2016. Puelche desconoce el costo real de atender a cada cliente, subsidiando rutas rurales remotas de baja densidad a expensas de clientes urbanos de alta rotación. La ocupación promedio de la flota es 68 % y cae a 41 % en días de baja utilización. La rotación anual de preparadores de pedidos alcanza 38 %, lo que incrementa el esfuerzo de capacitación e induce errores recurrentes en el armado de pedidos.

### 2.2.2 Contexto operacional, normativo y estacionalidad

La comprensión del negocio de Distribuidora Puelche S.A. exige interpretar sus restricciones regulatorias y sectoriales bajo el marco jurídico chileno vigente:

- Reglamento Sanitario de los Alimentos (Decreto 977/1996 del Ministerio de Salud): (Ministerio de Salud, 1996). Obliga a mantener registros inalterables de temperatura en alimentos congelados (temperatura ≤ -18 °C) y a ejecutar procedimientos de retiro de mercado (recall) en plazos expeditos ante sospecha de contaminación microbiológica o química.

- Documentos Tributarios Electrónicos (DTE - SII): (Servicio de Impuestos Internos, 2024). La Guía de Despacho Electrónica (GDE) rige el traslado legal de mercaderías. El acuse de recibo electrónico con constancia de entrega conforme o recepción con mermas es el instrumento probatorio que otorga mérito ejecutivo para la cobranza comercial y el cómputo del crédito fiscal IVA.

- Normativa laboral de transportes (Código del Trabajo, Art. 25 bis): (Ministerio del Trabajo y Previsión Social, 2002). Regula la jornada laboral de conductores y peonetas, fijando descansos mínimos y límites de conducción continua que condicionan estrictamente la longitud y duración de las rutas de despacho.

- Ley 21.719 de Protección de Datos Personales: (Ministerio del Interior y Seguridad Pública, 2024). La entrada en vigencia de la ley está fijada para el 1 de diciembre de 2026. Por ello, Puelche debe preparar el tratamiento de información comercial y comportamiento financiero de los almaceneros, y los controles telemáticos deben respetar la proporcionalidad laboral y la restricción del caso sobre cámaras y GPS.

- Estándares sectoriales GS1 y EDI: (GS1 Chile, 2020). Demanda la adopción de identificadores universales (GTIN para productos, GLN para puntos de entrega, GS1-128 para unidades logísticas de carga) e intercambio electrónico de datos (EDI) para órdenes de compra, avisos de despacho (DESADV) y facturación electrónica con el gran retail chileno.

A este marco se añade el impacto crítico de la estacionalidad, durante las tres primeras semanas de septiembre el volumen diario casi se duplica, de ≈ 1.400 a ≈ 2.600 entregas (2026c, anexo B.2). Este pico satura la ventana de preparación nocturna (22:00 a 06:00 hrs) y genera congestión severa en la ventana crítica de despacho matinal (05:30 a 07:00 hrs). Un dimensionamiento informático o de flota calculado para promedios mensuales colapsa inevitablemente en este período. Similar tensión ocurre en diciembre y durante los cierres mensuales, mientras que en invierno los caminos rurales empeoran y alargan los tramos sin señal, que en rutas de hasta 240 km ya llegan a dos horas.

### 2.2.3 Arbitraje de tensiones operacionales y comerciales

Las entrevistas de levantamiento del caso (Distribuidora Puelche S.A., 2026c, cap. 8) muestran contradicciones estructurales entre las distintas gerencias de Puelche. Estas tensiones no constituyen discrepancias accidentales, sino el reflejo de objetivos locales descoordinados que exigen una decisión antes de diseñar la solución. Para cada tensión se indica la decisión que la necesidad requiere:

1. Promesa de entrega (Comercial contra Operaciones): La Gerencia Comercial busca captar clientes prometiendo entregas en 24 horas a todo evento. La Gerencia de Operaciones afirma que tal promesa es materialmente imposible en la flota actual y genera frustración y reclamos. Decisión que requiere la necesidad: una promesa segmentada y viable: 24 horas para clientes urbanos con pedidos ingresados antes del corte de las 14:00, y 48 horas para clientes rurales, periféricos o abastecidos mediante cross-docking. Cómo se informa la promesa al cliente se desarrolla en el Subdocumento 3.

2. Control de cadena de frío (Calidad contra Operaciones): La Jefa de Calidad exige que cualquier excursión térmica fuera de norma bloquee automáticamente el producto para entrega. Operaciones y los choferes argumentan que bloqueos ciegos obligan a retornar camiones cargados y provocan pérdidas catastróficas. Decisión que requiere la necesidad: un control térmico graduado: las excursiones menores y transitorias (apertura de puertas durante la descarga) justifican una advertencia, y solo las críticas y sostenidas (sobre el umbral del RSA) justifican retener el lote; la decisión final sobre el producto es de Calidad (Anexo 2.2, S-04). El mecanismo de alerta y retención se desarrolla en el Subdocumento 3.

3. Gestión del efectivo (Finanzas contra Comercial): Finanzas exige erradicar el efectivo y exigir transferencias o prepagos para evitar pérdidas. Comercial sostiene que exigir bancarización liquidará al canal tradicional. Decisión que requiere la necesidad: se respeta el pago en efectivo del canal tradicional, sin exigir al almacenero un dispositivo propio (Distribuidora Puelche S.A., 2026c, cap. 10, restricción 5). La necesidad es que cada cobro quede asociado a su entrega y que la diferencia de rendición pueda rastrearse por entrega, en vez de detectarse al día siguiente. El mecanismo de registro, comprobante y cuadratura se desarrolla en el Subdocumento 3.

4. Nube y cortes de enlace (Jefe de TI contra la operación): El jefe de TI prefiere todo en la nube y él mismo explica por qué la operación no puede depender de ella: la fibra se corta cuatro veces al año, Concepción no tiene respaldo y las plataformas de cross-docking operan solo con red móvil. Decisión que requiere la necesidad: la preferencia por la nube es admisible solo si la operación no depende del enlace. Cada centro de distribución debe poder recibir, preparar y despachar durante al menos 24 horas sin enlace, y la preventa y el reparto deben operar un turno completo de 14 horas sin señal, sin pérdida ni duplicación de registros al reconectar (Distribuidora Puelche S.A., 2026c, cap. 10, restricciones 2 y 3, y cap. 15). La arquitectura que lo cumple se desarrolla en el Subdocumento 3.

5. Planificación de rutas (Conocimiento tácito contra Algoritmo): La empresa depende absolutamente del criterio mental de un único planificador con más de 20 años en la compañía, quien se jubilará en dos años. Operaciones teme que un software estándar genere rutas teóricas absurdas que los choferes rechacen. Decisión que requiere la necesidad: el conocimiento del planificador debe quedar explícito, documentado y validado por él antes de su jubilación, mediante una elicitación formal durante los primeros meses; cualquier ruta propuesta debe poder corregirse manualmente y respetar las restricciones de terreno que hoy solo él conoce (Anexo 2.2, S-16). El mecanismo se desarrolla en el Subdocumento 3.

## 2.3 Dimensionamiento del problema

Esta sección cuantifica las brechas con las cifras del caso y analiza los seis procesos actuales donde se originan.

### 2.3.1 Cuantificación del impacto operacional y financiero

Para dimensionar objetivamente la magnitud del desafío, la Tabla 2.1 consolida las métricas e indicadores operativos de la situación actual (AS-IS), contrastándolos con las pérdidas económicas y de servicio que generan.

Tabla 2.1 Dimensionamiento cuantitativo de las brechas operacionales de Distribuidora Puelche S.A. Fuente: Elaboración propia a partir de Distribuidora Puelche S.A. (2026c), tablas 7.1 a 7.3 y sección 4.8.

| Indicador Operacional | Línea Base Actual | Meta o condición | Impacto Económico y Operacional en Puelche |
| --- | --- | --- | --- |
| Entregas a tiempo y completas (OTIF) | 82,4 % | Referencia del caso: sobre 95 % | 17,6 % de pedidos fallidos; riesgo de perder a la principal cadena (11 % de la venta) ante sus condiciones de 2029. |
| Cumplimiento de lo pedido (fill rate) | 91,3 % | Referencia del caso: sobre 97 % | Pedidos entregados incompletos; afecta directamente el componente In-Full del OTIF. |
| Tiempo para identificar a los clientes afectados por un retiro sanitario | 9 días, con resultado estimado | Lista de clientes afectados por lote, con evidencia, en menos de 2 horas | Retiro preventivo marzo 2026: suspensión de 6 meses del proveedor (6 % ventas). |
| Recepciones sin registro de lote | 41,0 % del producto involucrado | El 100 % de las recepciones registra el lote de los productos que lo requieren. | Imposibilidad de trazar productos en bodega y despacho; ruptura del estándar de inocuidad. |
| Quiebre de stock en preventa | 7,8 % de las líneas | Referencia del caso: bajo 2 % | Ventas perdidas no recuperadas; preventista compromete productos físicamente agotados. |
| Reentregas operacionales | 4,2 % | Referencia del caso: bajo 1 % | Sobre 1.400 entregas diarias, equivale a aproximadamente 59 reentregas por día. |
| Diferencias mensuales de efectivo | $4,2 M/mes | Rendición cuadrada el mismo día; toda diferencia identificada y explicada. | Diferencias de rendición sin investigar; se rinden a la mañana siguiente. |
| Diferencia en conteo cíclico | 2,3 % del valor contado | Diferencias de inventario investigadas y ajustes debidamente justificados. | Descuadre entre inventario contable y existencias físicas. |
| Merma por vencimiento | 1,7 % del valor del inventario al año | Merma no superior al 1,0 % del valor del inventario al año, verificada tras 12 meses de operación, sin aumentar los quiebres de stock. | Pérdida de productos perecibles por ausencia de despacho FEFO (First Expired, First Out). |
| Pérdida de envases retornables | 14 % estimado del parque al año | Parque de envases controlado; pérdida anual no superior al 7 %, verificada tras 12 meses de operación. | 68.000 canastillos y 9.400 pallets sin control individual; se anotan en un cuaderno. |
| Ocupación promedio de camiones | 68,0 % | Umbral a comprometer | Capacidad ociosa de transporte; días valle registran 41 % de utilización de tolva. |
| Pérdida de guías de despacho (GDE) | 1,1 % emitidas | Referencia del caso: cero | Ante un reclamo de entrega no recibida, encontrar la guía toma en promedio 12 días. |

Del análisis de la Tabla 2.1 se desprende que el caso cuantifica en dinero dos pérdidas por eventos: el retiro de marzo de 2026 y el rechazo de un camión completo por sospecha de ruptura de la cadena de frío. Además, registra diferencias de rendición mensuales, cuyas causas no se han investigado. Los dos eventos y las diferencias mensuales no corresponden al mismo período ni se suman. Las demás brechas se expresan como porcentajes sobre bases distintas:

- la merma, sobre el valor del inventario;

- el descuadre, sobre el valor contado;

- las reentregas, sobre las entregas;

- los envases, sobre el parque.

Por eso no se suman ni se comparan entre sí en dinero. Su efecto converge en la calidad del servicio, pero por vías distintas. Una reentrega o un faltante afectan el OTIF, porque el pedido no llega completo o dentro de la ventana. Una guía extraviada no afecta el OTIF si la entrega fue completa y a tiempo; afecta el pedido perfecto, que exige además documentación correcta (Anexo 2.2, S-01). Por esa razón, la brecha de servicio es la dimensión común del problema, medida con dos indicadores y no con una tasa única.

### 2.3.2 El enigma del cross-docking y los seis procesos AS-IS

Uno de los principales hallazgos del diagnóstico es el denominado enigma del cross-docking: la empresa invirtió en tres centros de transferencia con la promesa de reducir 24 horas del tiempo total de entrega, pero en la práctica solo logró una reducción neta de 8 horas. La brecha de 16 horas resulta de la diferencia entre ambos valores (24 - 8 = 16), pero las Bases señalan expresamente que su causa aún no se ha investigado.

La operación observada permite formular, sin anticipar una conclusión, la hipótesis de que la consolidación, la desconsolidación y la validación manual contribuyen a la brecha. Esta hipótesis debe validarse con mediciones de tiempos en Talca y en las tres plataformas antes de atribuir las 16 horas a un punto específico del proceso.

A continuación, se modelan y analizan los seis procesos críticos de la cadena logística actual (AS-IS) mediante diagramas de flujo que ilustran los puntos exactos de quiebre y pérdida de trazabilidad.

#### 2.3.2.1 Proceso 1: Preventa y Toma de Pedidos AS-IS

Como se aprecia en la Figura 2.1, el flujo comercial parte con el preventista visitando al cliente en terreno con una aplicación móvil desconectada que no posee visibilidad de stock ni del estado crediticio del comprador.

1. El preventista visita presencialmente al cliente; participan 62 preventistas.

2. Captura el pedido en una aplicación móvil desconectada, sin visibilidad de stock ni crédito.

3. Transmite el pedido cuando el dispositivo recupera cobertura; en zonas sin señal, el envío se retrasa hasta encontrarla. La ventana de 17:00 a 20:00 corresponde al regreso y sincronización de la flota, no a la preventa.

4. El proceso consulta si existe stock disponible y crédito aprobado.

5. Si la respuesta es afirmativa, el pedido ingresa formalmente a la cola de procesamiento del ERP.

6. Si la respuesta es negativa, se distinguen dos motivos que pueden coincidir: falta de stock, que produce pedidos incompletos o ventas perdidas y cuyo quiebre afecta al 7,8 % de las líneas; o bloqueo por crédito, que deja el pedido retenido en el ERP para revisión por Crédito y Cobranza al día siguiente.

> **[Descripción de imagen — Figura 2.1]**
> Diagrama de flujo dispuesto de arriba hacia abajo. Los pasos son rectángulos de esquinas redondeadas, con relleno naranja claro y borde naranja o relleno gris claro y borde gris, unidos por flechas negras. Los tres primeros recuadros dicen «1. Visita presencial al cliente (62 preventistas)», «2. Captura pedido en App móvil offline sin stock ni crédito» y «3. Transmisión al recuperar cobertura (retraso en zonas sin señal)». Después aparece un rombo gris con la pregunta «¿Stock disponible y crédito aprobado?». La rama izquierda «Si» conduce a «4. Ingreso formal a cola de procesamiento enERP». La rama derecha «No» se divide en dos recuadros: «Falta de stock: pedido incompleto / venta perdida. 7,8% de las líneas con quiebre.» y «Bloqueo por crédito: pedido retenido en el ERP. Revisión por Crédito y Cobranza al día siguiente.». Sobre esta bifurcación figura la nota «*Los motivos pueden coincidir.».

**Figura 2.1 Proceso de Preventa y Toma de Pedidos AS-IS. Fuente: elaboración propia a partir de Distribuidora Puelche S.A. (2026c), capítulos 4 y 8.**

El análisis de la Figura 2.1 distingue dos problemas que el preventista no puede anticipar con la información de su aplicación: la falta de stock, cuyo quiebre afecta al 7,8 % de las líneas y puede producir pedidos incompletos o ventas perdidas, y el bloqueo por crédito, que deja el pedido retenido en el ERP para revisión por Crédito y Cobranza al día siguiente. El pedido se transmite al recuperar cobertura y el crédito se valida en el sistema de gestión.

#### 2.3.2.2 Proceso 2: Recepción de Mercadería y Control de Lotes AS-IS

En la Figura 2.2 se ilustra el registro de recepciones en los muelles de los centros de distribución al descargar los envíos de los 180 proveedores.

1. Arriba un camión al muelle del centro de distribución; la operación se relaciona con 180 proveedores.

2. Se descargan y cuentan físicamente los bultos en el andén.

3. La recepción se registra manualmente en una planilla física o guía en papel.

4. El proceso consulta si lote y vencimiento fueron digitados en el sistema.

5. Si la respuesta es afirmativa, la mercadería queda con lote registrado.

6. Si la respuesta es negativa, queda comprometida la trazabilidad sanitaria; 41 % de las recepciones del producto involucrado en el retiro no tenía lote registrado.

> **[Descripción de imagen — Figura 2.2]**
> Diagrama vertical con flechas negras, recuadros de esquinas redondeadas alternados en naranja claro y gris claro, y un rombo gris de decisión. Los primeros recuadros contienen «1. Arribo de camión a muelle CD (180 proveedores)», «2. Descarga y conteo físico de bultos en andén» y «3. Registro manual en planilla física / guía en papel». El rombo pregunta «¿Se digita lote y vencimiento en sistema?». La rama izquierda «Si» lleva a «4. Mercadería con lote registrado». La rama derecha «No» lleva al recuadro «Producto involucrado: 41% sin lote Riesgo para trazabilidad sanitaria».

**Figura 2.2 Proceso de Recepción de Mercadería y Control de Lotes AS-IS. Fuente: elaboración propia a partir de Distribuidora Puelche S.A. (2026c), capítulos 4 y 8.**

El análisis de la Figura 2.2 muestra que el registro de lote y vencimiento no es confiable.

En el producto involucrado en el retiro sanitario, 41 % de las recepciones no registró lote. Ese antecedente no permite extrapolar el porcentaje a todas las recepciones, pero sí fundamenta la necesidad de medir cobertura de captura y trazabilidad de extremo a extremo.

#### 2.3.2.3 Proceso 3: Preparación de Pedidos y Cross-Docking AS-IS

La operación de las tres plataformas de cross-docking (Curicó, Chillán y Los Ángeles) se detalla en la Figura 2.3, según la descripción del caso.

1. En Talca se consolida la carga de cada plataforma en el camión de línea.

2. El camión de línea llega a la plataforma en la madrugada.

3. La carga se desconsolida en una ventana de operación de tres horas, sin almacenamiento y con personal reducido.

4. La carga se despacha en la mañana en los camiones de reparto.

Las plataformas operan con conectividad únicamente por red móvil y sin control de inventario (Distribuidora Puelche S.A., 2026c, capítulo 6 y sección 4.2).

> **[Descripción de imagen — Figura 2.3]**
> Diagrama lineal vertical formado por cuatro rectángulos de esquinas redondeadas, unidos por flechas negras hacia abajo. El primero y el tercero tienen relleno naranja claro y borde naranja; el segundo y el cuarto, relleno gris claro y borde gris. Sus textos, en orden, son «1. Consolidación en Talca en camión de línea», «2. Llegada del camión de línea a la plataforma en la madrugada», «3. Desconsolidación en ventana de 3 horas, sin almacenamiento» y «4. Despacho matinal en camiones de reparto». No aparecen bifurcaciones ni rombos de decisión.

**Figura 2.3 Proceso de Preparación y Cross-Docking AS-IS. Fuente: elaboración propia a partir de Distribuidora Puelche S.A. (2026c), capítulos 4 y 8.**

El diagrama de la Figura 2.3 representa las actividades que deben medirse durante el levantamiento. La sospecha interna de la compañía es que el tiempo se pierde en la consolidación en Talca, pero el caso advierte que no hay datos que lo confirmen ni que lo desmientan; por eso se presenta como hipótesis (Anexo 2.2, SP-02) y no como causa probada de la brecha de 16 horas.

#### 2.3.2.4 Proceso 4: Planificación de Rutas AS-IS

El proceso de diagramación de despachos y asignación de vehículos se ilustra en la Figura 2.4.

1. Los pedidos confirmados quedan disponibles para planificación entre las 15:00 y las 18:30 horas.

2. Los datos se exportan manualmente a planillas Excel, sin interfaz directa.

3. Las rutas se diagraman manualmente con el conocimiento tácito del planificador.

4. Se imprimen las hojas de ruta y guías para la tripulación.

5. El despacho opera con rutas rígidas y subóptimas y alcanza 68 % de ocupación.

> **[Descripción de imagen — Figura 2.4]**
> Diagrama vertical de cinco recuadros de esquinas redondeadas, conectados consecutivamente mediante flechas negras hacia abajo. Los recuadros primero, tercero y quinto tienen relleno naranja claro y borde naranja; segundo y cuarto son grises. En orden, dicen «1. Pedidos confirmados disponibles para planificación (15:00–18:30 hrs)», «2. Exportación manual a planillas Excel sin interfaz directa», «3. Diagramación manual de rutas (conocimiento tácito del planificador)», «4. Impresión física de hojas de ruta y guías para tripulación» y «5. Despacho con rutas rígidas y subóptimas (68% ocupación)».

**Figura 2.4 Proceso de Planificación de Rutas AS-IS. Fuente: elaboración propia a partir de Distribuidora Puelche S.A. (2026c), capítulos 4 y 8.**

Como revela la Figura 2.4, la planificación descansa exclusivamente en planillas de cálculo y en la memoria del planificador. Este procedimiento impide simular alternativas dinámicas ante congestión o picos estacionales, derivando en un promedio de ocupación de camiones de solo 68 %.

#### 2.3.2.5 Proceso 5: Reparto y Entrega AS-IS

La interacción en la última milla entre los camiones de reparto y los puntos de destino se presenta en la Figura 2.5.

1. El camión sale a ruta durante la ventana de despacho de 05:30 a 07:00 horas.

2. Arriba al local comercial, ya sea almacén o cliente de food service.

3. El proceso consulta si el local está abierto y el cliente está conforme.

4. Si la respuesta es afirmativa, el cliente firma físicamente la guía de despacho.

5. Si el local está cerrado, el conductor decide si vuelve más tarde, deja el pedido con el negocio vecino o se lo lleva de vuelta; no existe una regla escrita. Si el cliente rechaza un producto, el conductor lo anota en la guía y se lo lleva de vuelta.

> **[Descripción de imagen — Figura 2.5]**
> Diagrama con dos pasos iniciales dispuestos verticalmente: un recuadro gris «1. Despacho matinal de camión a ruta (05:30 a 07:00 hrs)» y un recuadro naranja claro «2. Arribo a local comercial (Almacén o Food Service)», unidos por flechas negras. A continuación, un rombo gris pregunta «¿Local abierto y cliente conforme?». La rama izquierda «Si» lleva al recuadro naranja claro «3. Firma física de guía de despacho enpapel». La rama derecha «No» se divide en dos recuadros naranja claro. El primero dice «Local cerrado A criterio del conductor:» y enumera «• Volver más tarde», «• Dejar con el negocio vecino» y «• Retornar el pedido». El segundo dice «Producto rechazado Anotar en guía y retornar el producto rechazado». Las flechas muestran las tres salidas desde la decisión.

**Figura 2.5 Proceso de Reparto y Entrega AS-IS. Fuente: elaboración propia a partir de Distribuidora Puelche S.A. (2026c), capítulos 4 y 8.**

La Figura 2.5 distingue las situaciones de local cerrado y rechazo de productos. Ante un local cerrado, el conductor decide si vuelve más tarde, deja el pedido con el negocio vecino o se lo lleva de vuelta; no existe una regla escrita. Cuando el cliente rechaza un producto, el conductor lo anota en la guía y se lo lleva de vuelta. Por tanto, el retorno de mercancía no es el resultado obligatorio de toda visita a un local cerrado ni equivale por sí mismo a una reentrega.

La tasa de reentregas es del 4,2 % sobre el total de entregas (Distribuidora Puelche S.A., 2026c, sección 7.1). Aplicada a las aproximadamente 1.400 entregas de un día hábil normal, equivale a unas 59 reentregas diarias (1.400 × 0,042 = 58,8). Esta estimación está condicionada al supuesto SP-01 del Anexo 2.2, que requiere validar la aplicación de la tasa al volumen diario y la correspondencia de cada reentrega con una entrega. La cifra no representa la cantidad de retornos de mercancía al centro de distribución.

#### 2.3.2.6 Proceso 6: Rendición y Cobranza AS-IS

Por último, la liquidación de valores cobrados en efectivo se esquematiza en la Figura 2.6.

1. Se cobra en efectivo contra entrega; el 38 % de las ventas del canal tradicional se cobra así y el resto se factura a 30 días.

2. El conductor conserva el dinero hasta su regreso.

3. La rendición se realiza a la mañana siguiente en caja, contando el dinero contra el listado de entregas del día anterior.

4. La caja consulta si el dinero contado coincide con el listado de entregas al contado del día anterior.

5. Si coincide, se registra sin inconvenientes.

6. Si la respuesta es negativa, quedan diferencias no conciliadas y no es posible rastrear el descuadre por entrega.

> **[Descripción de imagen — Figura 2.6]**
> Diagrama vertical con tres pasos, un rombo de decisión y dos salidas. Los pasos, conectados por flechas negras, son «1. Cobro en efectivo en punto de entrega (Canal tradicional)», «2. El conductor conserva el dinero hasta su regreso» y «3. Rendición en caja a la mañana siguiente contra listado de entregas». El primero y el tercero son recuadros naranja claro; el segundo es gris claro. El rombo gris pregunta «¿Dinero coincide con el listado?». La rama izquierda «Si» termina en «Registro coincide»; la derecha «No» termina en «No Diferencias no conciliadas, descuadre no rastreable por entrega». Ambas salidas están en recuadros naranja claro.

**Figura 2.6 Proceso de Rendición y Cobranza AS-IS. Fuente: elaboración propia a partir de Distribuidora Puelche S.A. (2026c), capítulos 4 y 8.**

La Figura 2.6 muestra por qué las diferencias quedan sin conciliar: el dinero recaudado se rinde al día siguiente contra planillas físicas, de modo que, cuando surge un descuadre, no es posible rastrear en qué entrega ocurrió el error.

## 2.4 Actores y Grupos de Interés

El éxito del proyecto depende de alinear a los 19 actores que conforman el ecosistema de Distribuidora Puelche S.A. Cada uno posee incentivos, niveles de poder y resistencias particulares frente a la automatización de procesos.

Para analizar de manera sintética su nivel de involucramiento y las estrategias de gestión del cambio correspondientes, la Tabla 2.2 presenta la matriz consolidada de grupos de interés del proyecto.

Tabla 2.2 Matriz de síntesis de actores, tensiones operacionales y estrategia de gestión. Fuente: elaboración propia a partir de Distribuidora Puelche S.A. (2026c), caps. 2, 4, 10 y 13.

| Grupo / Estamento | Tensión / Desafío Principal | Influencia | Interés | Estrategia de Gestión |
| --- | --- | --- | --- | --- |
| Dirección Estratégica (Gerenta General, Comercial, Finanzas) | Discrepancia entre la promesa comercial de 24 h y la viabilidad operativa; condiciones 2029 de la principal cadena (11 % de la venta); opacidad en el costo de servir. | Muy Alta | Muy Alto | Participación en el comité que arbitra la promesa de entrega y el orden de prioridades, con decisiones registradas en acta. |
| Jefaturas Operacionales y Soporte (Operaciones, Calidad, Bodega, TI, Planificador) | Brecha de 16 h no investigada entre la reducción prometida y la observada en cross-docking; riesgo sanitario por falta de lote; dependencia de un planificador único que se jubila en dos años; equipo TI de 4 personas. | Alta | Muy Alto | Participación directa en el levantamiento: talleres con el planificador, validación de la regla térmica con Calidad y medición conjunta de tiempos en cross-docking. |
| Personal Operativo de Terreno (62 preventistas, 84 conductores y peonetas propios, aprox. 160 conductores de transportistas, 120 preparadores, sindicato) | Preventa sin stock ni crédito (7,8 % de las líneas con quiebre); riesgo en el transporte de efectivo; objeción sindical a cámaras y control de jornada por GPS. | Alta | Alto | Validación de cada cambio en sus condiciones reales de trabajo; acuerdo previo con el sindicato antes de utilizar GPS para control de jornada; controles de privacidad en el uso de telemetría operacional; capacitación sin detener la venta ni el reparto. |
| Clientes y Canales de Venta (11.600 tradicionales, 2.100 food service, 500 modernos) | 17,6 % de entregas fallidas o tardías (OTIF 82,4 %); almaceneros a los que no se puede exigir internet, dispositivo ni pago electrónico, con el 38 % de la venta del canal cobrada en efectivo contra entrega; condiciones 2029 de la principal cadena. | Muy Alta | Alto | Preservar la forma de compra y pago del canal tradicional; levantar con los clientes de food service sus exigencias de puntualidad y frescura, y con cada cadena sus condiciones. |
| Proveedores, Transportistas y Autoridad (180 proveedores, 10 transportistas, SEREMI de Salud) | En el producto del retiro, 41 % de recepciones sin lote; rotación sin aviso de conductores de terceros; observación de la autoridad por falta de registro continuo de temperatura. | Media-Alta | Alto | Aviso anticipado de los requisitos de rotulado; acuerdo operacional con cada transportista; canal formal con la autoridad sanitaria. |

El análisis de la Tabla 2.2 permite concluir que el principal foco de resistencia al cambio no se ubica en los clientes del canal tradicional (quienes acogen favorablemente cualquier mejora que no les altere su hábito de pago), sino en el personal operativo de terreno y sus organizaciones sindicales. La oposición histórica del sindicato a las cámaras en cabina y al rastreo satelital laboral demanda una estrategia de implantación basada en la transparencia: los sistemas telemáticos deben orientarse al aseguramiento de la carga y el activo vehicular, sin invadir la privacidad individual del conductor. De igual modo, la captura del conocimiento tácito del planificador de rutas exige una dinámica de reconocimiento formal de su experiencia profesional.

El catálogo extendido y nominal con el detalle de los 19 actores se encuentra disponible en el Anexo 2.3.

## 2.5 Resumen de Requerimientos, Supuestos, Exclusiones y Restricciones

Esta sección resume lo que el CLIENTE requiere, los supuestos que formula LafroX y las exclusiones y restricciones del caso; el detalle está en los Anexos 2.1 a 2.3.

### 2.5.1 Resumen y análisis de requerimientos del cliente

A partir del análisis del problema y de las entrevistas del caso (Distribuidora Puelche S.A., 2026c, cap. 8), el cliente exige una solución que satisfaga un catálogo integral de requerimientos funcionales y no funcionales. Los principales ejes funcionales demandados abarcan:

- Preventa y comercialización: El preventista necesita conocer stock y crédito al tomar el pedido y seguir trabajando un turno completo sin señal, sin que ningún pedido se pierda ni se duplique.

- Gestión de bodegas y trazabilidad de lotes: Todo producto que lo requiera debe quedar con lote y vencimiento desde su recepción, salir en orden de vencimiento, también en la cámara a −22 °C, y permitir identificar a los clientes afectados por un lote en menos de 2 horas.

- Despacho y última milla: Rutas que respeten la promesa segmentada y las ventanas de servicio, evidencia de cada entrega disponible el mismo día y acuse de recibo válido de la Guía de Despacho Electrónica.

- Conciliación financiera: Cada cobro en efectivo debe quedar asociado a su entrega, y toda diferencia de rendición debe explicarse el mismo día con causal y responsable.

El catálogo completo y priorizado de requerimientos funcionales y no funcionales se detalla en el Anexo 2.1.

### 2.5.2 Supuestos de ingeniería formulados por LafroX

Para diseñar una propuesta técnicamente sólida y exenta de contingencias imprevistas, LafroX formula un conjunto de supuestos propios de ingeniería, deslindándolos formalmente de las restricciones impuestas por las bases. El detalle, con fundamento, impacto y mecanismo de validación, se presenta en el Anexo 2.2.

### 2.5.3 Exclusiones y restricciones no negociables

Complementariamente, la Tabla 2.3 sintetiza cinco de las doce restricciones del caso, con los mismos códigos del Anexo 2.2. La inmutabilidad del canal tradicional y la prohibición de intervenir sistemas del 1 al 25 de septiembre, durante todo diciembre y en los tres primeros días hábiles de cada mes condicionan la propuesta de dos formas. Obligan a que la operación de terreno no dependa del sistema central. También obligan a programar despliegues y pasos a producción fuera de esos períodos (Distribuidora Puelche S.A., 2026c, cap. 10 y sección 13.3). El inventario íntegro de exclusiones y restricciones se encuentra en el Anexo 2.2.

**Tabla 2.3 Síntesis de restricciones no negociables del caso. Fuente: Distribuidora Puelche S.A. (2026c), cap. 10 y sección 13.3.**

| N° | Restricción | Descripción operativa o legal | Origen |
| --- | --- | --- | --- |
| R-05 | Inmutabilidad operativa del canal tradicional. | A los 11.600 almacenes no se les puede exigir internet, dispositivo propio ni pago electrónico; el 38 % de la venta del canal se cobra en efectivo contra entrega. | Caso, cap. 10, restricción 5, y sección 4.7. |
| R-04 | ERP 2017 como verdad contable única. | El ERP no se sustituye. La plataforma captura y entrega datos transaccionales, pero el ERP emite los documentos tributarios legales. | Caso, cap. 10, restricción 4. |
| R-12 | Validez legal de los documentos tributarios. | La guía de despacho electrónica y su acuse de recibo tienen efectos legales que la solución no puede comprometer; se suma el cumplimiento sanitario del Decreto 977 para los congelados. | Caso, cap. 10, restricción 12; Ministerio de Salud (1996). |
| R-10 | Privacidad laboral y objeción sindical. | El sindicato objetó formalmente las cámaras en cabina y el control de jornada por posicionamiento satelital. | Caso, cap. 10, restricción 10. |
| R-08 | Ventanas de congelamiento. | Prohibido intervenir sistemas del 1 al 25 de septiembre, durante todo diciembre y en los tres primeros días hábiles de cada mes; el paso a producción tampoco puede ocurrir en septiembre ni en diciembre. | Caso, cap. 10, restricción 8, y sección 13.3. |

Las cinco restricciones de la Tabla 2.3 limitan el diseño en tres planos. En terreno, R-05 y R-10 impiden apoyar la solución en el dispositivo del almacenero o en la vigilancia del conductor, por lo que la evidencia de entrega y de cobro debe generarse con los equipos de Puelche. En la integración, R-04 y R-12 dejan al ERP como único emisor tributario, de modo que la plataforma prepara los datos pero no emite documentos legales. En el calendario, R-08 elimina septiembre, diciembre y los primeros días hábiles de cada mes como ventanas de paso a producción, lo que fija las fechas de corte del Capítulo 7.

## Referencias

Las fuentes citadas en este documento se listan a continuación en formato APA 7.ª edición.

- Distribuidora Puelche S.A. (2026a). Bases Administrativas de Licitación N° TFEP-01/2026: Contratación de Solución Integral de Software y Servicios de Operación.

- Distribuidora Puelche S.A. (2026b). Bases Técnicas Transversales de Licitación N° TFEP-01/2026.

- Distribuidora Puelche S.A. (2026c). Caso 02: Logística – Especificaciones del Problema y Operación de Distribuidora Puelche S.A.

- GS1 Chile. (2020). Estándares de Identificación y Trazabilidad Logística GS1: Guía de Aplicación para Consumo Masivo y Retail (Versión 20.0). GS1.

- Ministerio de Salud. (1996). Decreto Supremo N° 977: Aprueba Reglamento Sanitario de los Alimentos. Diario Oficial de la República de Chile.

- Ministerio del Interior y Seguridad Pública. (2024). Ley N° 21.719: Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales. Biblioteca del Congreso Nacional de Chile.

- Ministerio del Trabajo y Previsión Social. (2002). Código del Trabajo de la República de Chile: Artículo 25 bis sobre jornada especial de transporte de carga. Edición oficial.

- Servicio de Impuestos Internos. (2024). Manual de Procedimientos y Requisitos de Documentos Tributarios Electrónicos (DTE). SII Chile.

## Declaración de uso de IA

En cumplimiento de la sección 7.2 de las Aclaraciones de la licitación, la tabla siguiente declara el uso de herramientas de inteligencia artificial en este subdocumento, con la revisión humana de cada parte. La declaración se consolida en el Formulario A-6.

**Tabla 2.4 Declaración de uso de IA por sección del Subdocumento 2. Fuente: registro del equipo.**

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
| --- | --- | --- | --- | --- | --- |
| 2.1 Resumen Ejec. | Claude / Gemini | Síntesis ejecutiva y estilo formal | Bajo | Ninguno | Alex Aravena (JP): Validación del resumen y propuesta de valor |
| 2.2 Comprensión | Claude / Gemini | Estructuración de los 3 problemas | Bajo | Ninguno | Patricio Henríquez (Gest): Verificación de arbitraje de tensiones |
| 2.3 Dimensionamiento | Claude / Gemini | Descripción estructurada de los 6 flujos AS-IS | Bajo | Medio | Tomás Pérez (Des): Verificación de flujos AS-IS y cálculos |
| 2.4 Actores | Claude / Gemini | Disposición tabular de actores | Bajo | Ninguno | Patricio Henríquez (Gest): Consistencia con catálogo de actores |
| 2.5 Requerimientos | Claude / Gemini | Formato y redacción de supuestos | Bajo | Ninguno | Bastián Trejo (Arq): Deslinde de supuestos vs restricciones |
| Anexo 2.1 | Claude / Gemini | Maquetación del listado de requerimientos | Bajo | Ninguno | Bastián Trejo (Arq): Coherencia con el catálogo canónico |
| Anexo 2.2 | Claude / Gemini | Consolidación de decisiones, exclusiones y restricciones | Bajo | Ninguno | Alex Aravena (JP): Cotejo con los capítulos 10, 11 y 16.1 del caso |
| Anexo 2.3 | Claude / Gemini | Maquetación de actores y sistemas legados | Bajo | Ninguno | Patricio Henríquez (Gest): Cotejo de actores, cifras y sistemas con el caso |
