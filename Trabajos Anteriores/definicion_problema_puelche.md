# 2. Presentación del Problema
## Caso 02 — Logística · Distribuidora Puelche S.A.

> **Asignatura:** Taller de Formulación de Proyectos Informáticos — ICI-5444
> **Mandante:** Distribuidora Puelche S.A. (empresa ficticia)
> **Versión:** 1.0 — agosto de 2026

---

## 2.1 Descripción del Contexto y Dolor del Negocio

### Perfil institucional del mandante

Distribuidora Puelche S.A. es una empresa familiar fundada en 1974, actualmente en su tercera generación de dirección. Su giro es la distribución mayorista de consumo masivo —alimentos, bebidas, aseo del hogar y cuidado personal— en cinco regiones del centro-sur de Chile, desde O'Higgins hasta La Araucanía. La empresa opera desde dos centros de distribución principales —Talca (18.000 m²) y Concepción (9.000 m²)— y tres plataformas de cross-docking en Curicó, Chillán y Los Ángeles. Su cartera activa comprende 14.200 clientes, distribuidos entre almacenes y minimarkets del canal tradicional (11.600), restaurantes y casinos del segmento food service (2.100) y cadenas de supermercados regionales (500 puntos de entrega). En el ejercicio 2025, la compañía procesó 31.000 pedidos mensuales, movilizó 2,4 millones de unidades y emitió cerca de 34.000 documentos tributarios, todo ello con ventas anuales de $148.000 millones. Su dotación propia alcanza las 640 personas, complementada por aproximadamente 160 conductores pertenecientes a 10 empresas transportistas externas.

### El detonante: retiro sanitario de marzo de 2026

El 3 de marzo de 2026, el gerente de aseguramiento de calidad de uno de los principales proveedores de lácteos del país notificó a Distribuidora Puelche la necesidad de ejecutar un retiro preventivo por desviación detectada en el lote 24-0217 de queso fresco. La respuesta institucional esperada era identificar, en el menor tiempo posible, a qué clientes había llegado ese lote, en qué cantidad y con qué documentación. La jefa de calidad tardó **nueve días** en responder, y la respuesta fue una estimación, no una certeza. Al ser imposible delimitar con exactitud los puntos de entrega afectados, la empresa debió ejecutar el retiro de forma indiscriminada sobre la totalidad de sus 14.200 clientes, con las siguientes consecuencias:

| Impacto | Magnitud |
|---|---|
| Pérdida financiera directa del retiro | $31 millones |
| Kilos recuperados innecesariamente | 4.800 kg |
| Sumario sanitario abierto por la autoridad | Sí |
| Suspensión como distribuidor autorizado por el proveedor | 6 meses (equivalente al 6% de las ventas) |

Este evento expuso con datos concretos una realidad que el equipo directivo intuía pero no había cuantificado: la operación entera carece de trazabilidad. El registro del lote de un producto existe, en el mejor de los casos, en una planilla impresa archivada en carpeta, y en el 41% de los casos no existe en absoluto. No hay ningún sistema que permita responder en tiempo real a dónde fue a parar un producto específico.

### El contexto competitivo y las presiones externas

El retiro sanitario no fue el único problema que enfrentó el comité ejecutivo en el primer trimestre de 2026. De manera simultánea, se materializaron dos presiones externas que transformaron una crisis puntual en una amenaza estratégica de largo plazo.

La primera es la irrupción de un distribuidor nacional que abrió operación en Talca ocho meses antes. Este competidor ofrece entrega en 24 horas y dispone de una aplicación móvil donde el almacenero realiza su pedido de forma autónoma, consulta el stock disponible y sabe la hora estimada de llegada del camión. Puelche, en contraste, entrega en 48 a 72 horas y toma el pedido mediante un preventista que visita al cliente una vez por semana. La diferencia no radica en mejores camiones ni en mejores precios: radica en información disponible en el momento correcto.

La segunda presión proviene del cliente más importante de la compañía, una cadena de supermercados regional que representa el 11% de la venta. Esta cadena notificó sus condiciones comerciales para el período que comienza en enero de 2029: pedidos exclusivamente por vía electrónica estructurada, aviso de despacho anticipado, ventana de entrega de **treinta minutos** con penalización por incumplimiento, y prueba de entrega digital obligatoria. Hoy, Puelche no cumple ninguna de estas condiciones: la ventana de entrega actual es de 10 horas (de 08:00 a 18:00), los pedidos no se reciben por ninguna vía electrónica y la prueba de entrega es una guía de papel firmada a mano.

### Metas del negocio que justifican la inversión

La combinación de estas tres presiones —el retiro sanitario, el avance del competidor y la exigencia del canal moderno— llevó al comité ejecutivo a convocar una licitación para desarrollar e implementar una solución integral de gestión logística. Las metas de negocio que la solución debe alcanzar son:

| Indicador | Situación 2025 | Meta |
|---|---|---|
| OTIF (entregas completas y a tiempo) | 82,4% | >95% |
| Fill rate (cumplimiento de lo pedido) | 91,3% | >97% |
| Plazo de entrega desde el pedido | 48–72 horas | 24 horas |
| Ventana de entrega comprometida | 08:00–18:00 (10 horas) | 30 minutos (exigencia 2029) |
| Tiempo para responder un retiro sanitario | 9 días, resultado estimado | Horas, con evidencia exacta |
| Registro continuo de temperatura en cadena de frío | Inexistente | Continuo y automático |
| Costo de servir por cliente | Desconocido | Calculado por entrega |
| Pedidos recibidos por vía electrónica estructurada | 0 de 31.000/mes | 100% del canal moderno |

---

## 2.2 Diagnóstico de Ineficiencias Operativas

La operación de Puelche se sostiene sobre procesos mayoritariamente manuales, sistemas con más de una década de antigüedad sin soporte, y conocimiento crítico que reside en personas y no en sistemas. Las ineficiencias se distribuyen a lo largo de todo el ciclo del pedido —desde la toma de la orden hasta la cobranza— y se refuerzan mutuamente, haciendo que el impacto total sea mayor que la suma de sus partes.

### 2.2.1 Preventa sin información real

Los 62 preventistas utilizan una aplicación adquirida en 2016 a un proveedor que ya no existe: no tiene soporte técnico, no es compatible con los dispositivos actuales y no ha recibido actualizaciones. Más allá de su obsolescencia técnica, la aplicación carece de las funcionalidades básicas para una venta informada: **no muestra el stock disponible, no muestra la deuda ni el crédito del cliente, y no muestra el historial de compra**. El preventista trabaja con esa información en la cabeza o anotada en un cuaderno personal.

En zonas rurales, donde la cobertura de red es intermitente o inexistente, la aplicación guarda los pedidos localmente, pero en ocasiones no los envía al recuperar señal, y en otras los envía duplicado. Nadie ha medido con qué frecuencia ocurre cada cosa, pero el equipo comercial estima que «pasa todas las semanas». El resultado es que el 7,8% de las líneas de pedido presentan quiebre en el momento de la entrega —porque se vendió algo que no había— y que los pedidos bloqueados por crédito quedan retenidos sin que nadie avise al preventista ni al cliente, que se entera cuando llama enojado. Adicionalmente, el preventista observa todos los días información valiosa en la góndola del cliente —producto vencido, exhibidores del competidor, riesgo de cierre del local— que no tiene dónde registrar.

### 2.2.2 Planificación de rutas concentrada en una sola persona

La asignación diaria de las 1.400 entregas a los 96 camiones disponibles la realiza una sola persona: Hugo Maldonado Sepúlveda, con 21 años de antigüedad en la empresa. El proceso toma entre 3,5 y 4 horas diarias y se apoya en una planilla de cálculo de 11 hojas que el propio planificador desarrolló y que nadie más comprende. En esa planilla —y en su memoria— reside conocimiento operacional crítico: restricciones de carga en puentes rurales, horarios de atención de clientes específicos, preferencias de conductor por cliente y el detalle de caminos en mal estado. Este conocimiento no está documentado en ningún sistema. Cuando el planificador toma vacaciones, el cumplimiento de entrega cae entre **6 y 9 puntos porcentuales**. Se jubila en dos años.

El resultado es una planificación subóptima y frágil: la ocupación promedio de los camiones en volumen es del 68%, con días en que un camión sale con el 41% de su capacidad. Nadie mide el costo de esa ineficiencia porque nadie mide el costo del viaje.

### 2.2.3 Entrega sin registro digital ni protocolo

El conductor sale entre las 05:30 y las 07:00 con las guías de despacho impresas en papel. La prueba de entrega es la firma del cliente en esa guía. Al regresar, entrega el fajo de guías a la oficina. El **1,1% mensual no llega**: se moja, se pierde en ruta o queda ilegible. Cuando un cliente reclama que no recibió un pedido, encontrar su guía toma en promedio 12 días; si la guía no aparece, la empresa no tiene cómo demostrar la entrega.

Cuando el local del cliente está cerrado, no existe ningún protocolo escrito. Cada conductor decide: vuelve más tarde, deja el pedido con el negocio de al lado, o se lo lleva de vuelta. Esta discrecionalidad es la causa principal del 4,2% de reentregas sobre el total de entregas. Asimismo, las diferencias entre lo pedido, lo despachado y lo efectivamente recibido no quedan explicadas: se descubren semanas después, cuando el cliente reclama o cuando llega la factura.

### 2.2.4 Trazabilidad de lote inexistente

El lote de un producto se registra en recepción en un campo de texto libre, cuando se registra. No existe ninguna integración entre ese registro y los movimientos posteriores del producto —preparación de pedido, carga, despacho y entrega al cliente—. La trazabilidad existe únicamente en papel de bodega y en la memoria de las personas que operaron cada etapa. En el retiro sanitario de marzo, el **41% de las recepciones del producto involucrado no tenía registro de lote**, lo que hizo imposible delimitar el universo afectado con precisión.

### 2.2.5 Cadena de frío sin monitoreo continuo

Los 1.100 SKU refrigerados o congelados están sujetos a exigencias sanitarias estrictas de control de temperatura. Sin embargo, el monitoreo se realiza de forma manual: dos lecturas por turno en las cámaras del centro de distribución (anotadas en planilla) y tres lecturas por viaje en los camiones con equipo de frío (anotadas por el conductor en papel). No existe registro continuo ni automático en ningún punto de la cadena. La autoridad sanitaria observó formalmente esta ausencia en su última fiscalización. Durante 2025, un cliente de food service rechazó un camión completo por sospecha de ruptura de cadena de frío; Puelche no pudo demostrar que la temperatura se había mantenido dentro de rango y asumió una pérdida de **$21 millones**.

Adicionalmente, no existe ninguna regla escrita que defina qué constituye una excursión de temperatura que invalida el producto, quién tiene autoridad para tomar esa decisión y si el sistema debe bloquear el despacho de forma automática. La ausencia de esta regla hace inoperable cualquier sistema de alertas.

### 2.2.6 Cobranza en efectivo sin trazabilidad ni control

El 38% de las ventas del canal tradicional se cobra en efectivo contra entrega. Los conductores rinden al día siguiente en caja, contando el dinero contra el listado de sus entregas del día anterior. Las diferencias de rendición promedian **$4,2 millones mensuales** en toda la flota y se resuelven, en palabras del jefe de tesorería, «conversando». No se investiga si la diferencia corresponde a un error de conteo, a un descuento que el conductor otorgó por su cuenta, a un cobro no realizado o a una pérdida. En algunas rutas rurales, el conductor circula con más de un millón de pesos en efectivo en la cabina.

### 2.2.7 Activos retornables y mermas sin control estructurado

La empresa tiene en circulación un parque estimado de 68.000 canastillos plásticos y 9.400 pallets. La palabra «estimado» es literal: no existe control individual de cada unidad. Los conductores registran las devoluciones de canastillos en un cuaderno. La pérdida anual estimada del parque es del **14%**, sin que exista un mecanismo de imputación por cliente o por conductor. La merma por vencimiento equivale al **1,7% del valor del inventario al año**, y se detecta en el conteo cíclico, en la preparación de pedidos, o —en el peor de los casos— cuando el preventista encuentra producto vencido de Puelche en la góndola del cliente.

### 2.2.8 Costo de servir desconocido

El costo logístico se prorratea por zona geográfica con un criterio elaborado en 2016. Nadie en la empresa sabe cuánto cuesta atender a un almacén de Empedrado que compra $45.000 cada dos semanas: el kilómetro recorrido, el tiempo de descarga, el porcentaje de su ruta que representa, la frecuencia de visita del preventista. Es perfectamente posible que la compañía esté perdiendo dinero en miles de clientes y tomando decisiones comerciales —descuentos, frecuencias de visita, pedidos mínimos— sobre la base de un prorrateo que no refleja la realidad operacional.

---

## 2.3 Segmentación del Problema por Áreas

Las ineficiencias descritas en la sección anterior no son independientes entre sí, pero sí pueden agruparse en áreas funcionalmente delimitadas. Esta segmentación tiene como propósito alinear el diagnóstico con los módulos de la solución a proponer y establecer claramente los límites de cada componente.

### Área 1 — Trazabilidad y Calidad Sanitaria

Esta área comprende la incapacidad de la empresa de registrar y consultar, de forma estructurada y en tiempo real, el recorrido de un lote desde la recepción del proveedor hasta su entrega al cliente final. Incluye también la ausencia de monitoreo continuo y automático de temperatura en la cadena de frío, en cámaras del centro de distribución y en vehículos refrigerados.

El impacto principal de esta brecha es el riesgo sanitario y financiero ante un retiro de producto, el incumplimiento normativo frente a la autoridad, y la pérdida de proveedores estratégicos que exigen acreditación de trazabilidad como condición comercial. Los procesos afectados abarcan la recepción de proveedores, el almacenamiento en cámara, la preparación de pedidos de productos con temperatura controlada, el transporte refrigerado y la entrega al cliente.

### Área 2 — Preventa y Gestión Comercial en Terreno

Esta área comprende la toma de pedidos en el local del cliente por parte de los preventistas, la gestión de la información de crédito y de cobranza en terreno, y el registro de observaciones comerciales en góndola. La brecha central es que el preventista opera sin información real —de stock, de crédito, de historial— y con una herramienta que falla en las condiciones reales del campo.

El impacto principal es la erosión de la confianza del cliente ante quiebres de stock y pedidos bloqueados sin aviso, la pérdida de oportunidades comerciales por falta de visibilidad, y la incapacidad de competir con un distribuidor que ya ofrece autoservicio digital. Los procesos afectados son la toma de pedidos, la gestión de crédito en terreno, la cobranza por el preventista y la detección de oportunidades en el punto de venta.

### Área 3 — Planificación de Rutas y Operación de Reparto

Esta área comprende la asignación diaria de entregas a camiones, el secuenciamiento de rutas, la ejecución del reparto, el registro de la entrega al cliente —con gestión del local cerrado y de las devoluciones en terreno— y la rendición del efectivo cobrado. La brecha central es la concentración del conocimiento operacional en una sola persona y la ausencia de evidencia digital de la entrega.

El impacto principal es la fragilidad operacional ante la ausencia del planificador, la baja ocupación de la flota, la imposibilidad de responder reclamos de entrega de forma oportuna y las diferencias de rendición de efectivo no investigadas. Los procesos afectados son la planificación de rutas, la carga y despacho desde el centro de distribución, la entrega en el local del cliente, las devoluciones en ruta y la rendición diaria de efectivo.

### Área 4 — Gestión de Bodega e Inventario

Esta área comprende el control de ubicaciones y stock en las instalaciones, la preparación nocturna de pedidos (picking), el conteo cíclico de inventario y la gestión de envases retornables y devoluciones. La brecha central es que los procesos de bodega se ejecutan con papeles impresos, sin registro de causas de faltante y sin control individual de activos.

El impacto principal es la diferencia de inventario no investigada (2,3% del valor contado en el ciclo), la merma por vencimiento, los faltantes en preparación cuya causa es desconocida, y la pérdida del 14% anual del parque de envases retornables. Los procesos afectados son el almacenamiento y asignación de ubicaciones, la preparación de pedidos, el conteo cíclico, la gestión de devoluciones y el control de activos retornables.

### Área 5 — Información de Gestión y Costo de Servir

Esta área comprende la generación de indicadores operacionales en tiempo real, el cálculo del costo real de cada entrega por cliente, y la integración con los canales electrónicos que el mercado exigirá a partir de 2029. La brecha central es que todos los indicadores actuales se construyen desde prorrateos, estimaciones y cierres del día siguiente, sin datos capturados en el momento y el lugar del hecho.

El impacto principal es la incapacidad de tomar decisiones comerciales y logísticas con base en información real, y la imposibilidad de cumplir las condiciones del canal moderno en el plazo exigido. Los procesos afectados son el cierre diario de operaciones, el análisis de rentabilidad por cliente, la integración EDI con cadenas de supermercados y el reporte a la autoridad sanitaria.

---

## 2.4 Definición de Actores y Supuestos

### 2.4.1 Actores directamente afectados

La solución debe diseñarse considerando la realidad de todos los actores que interactúan con el sistema, tanto internos como externos. Sus condiciones de uso son, en muchos casos, más restrictivas que las de un entorno de oficina y deben tratarse como requisitos de diseño, no como excepciones.

| Actor | Rol en la operación | Ineficiencia específica que enfrenta |
|---|---|---|
| **Preventista** (62 personas, terreno) | Toma pedidos, gestiona cobranza y observa el punto de venta | Opera sin stock, sin crédito del cliente y con app obsoleta que falla en campo; no tiene dónde registrar observaciones comerciales |
| **Conductor repartidor propio** (42 personas) | Transporta, entrega y cobra en efectivo | Sin protocolo ante local cerrado, sin registro digital de entrega, riesgo de seguridad personal con efectivo en ruta |
| **Conductor de transportista externo** (~160 personas) | Realiza entregas con camiones de diez empresas distintas | No es trabajador de Puelche; rota sin aviso; su incorporación requiere acuerdo con cada transportista |
| **Preparador de pedidos** (~120 personas, turno nocturno) | Prepara el pedido físico en bodega con hoja impresa | Alta rotación (38% anual), faltantes sin causa registrada, condiciones extremas en cámara de congelado (−22 °C, sin señal) |
| **Planificador de rutas** (1 persona) | Asigna diariamente las entregas a los camiones | Todo el conocimiento crítico de rutas reside en él; se jubila en dos años; nadie más comprende su planilla |
| **Jefa de calidad** | Asegura trazabilidad sanitaria y cadena de frío | Sin sistema consultable de lotes, sin registro continuo de temperatura y sin regla escrita de excursión térmica |
| **Gerente comercial** | Define la promesa de entrega y gestiona el canal moderno | No puede comprometer plazos que la operación no puede cumplir; enfrenta la pérdida del 11% de ventas en 2029 |
| **Gerente de finanzas** | Controla el costo logístico y la rendición de efectivo | Sin costo de servir real; $4,2 M/mes de diferencias de rendición sin investigar |
| **Jefe de TI** (equipo de 4 personas) | Mantiene toda la infraestructura tecnológica de la empresa | Sin capacidad para administrar sistemas adicionales sin soporte externo incluido en el contrato |
| **Cliente del canal tradicional** (11.600 almacenes) | Recibe el pedido y paga en efectivo | No tiene internet ni dispositivo propio; no puede —ni debe— cambiar su forma de operar |
| **Cliente del canal moderno** (500 puntos de entrega) | Cadenas y supermercados con exigencias EDI | Requieren desde enero de 2029 condiciones de integración electrónica que Puelche hoy no cumple |

### 2.4.2 Supuestos normativos y de entorno

Los siguientes supuestos delimitan el marco dentro del cual debe diseñarse la solución. No son opcionales: son condiciones del entorno que la propuesta debe respetar íntegramente.

| N° | Supuesto | Fundamento |
|---|---|---|
| 1 | El cliente del canal tradicional no cambiará su forma de comprar: paga en efectivo, no dispone de conexión a internet ni de dispositivo propio. La solución debe funcionar con el cliente tal como es. | Condición explícita establecida por la Gerenta General en el acta del comité ejecutivo. Restricción no negociable N°5 del Capítulo 10. |
| 2 | El sistema de gestión empresarial (ERP, 2017) no se reemplaza ni se modifica. Es el registro contable y tributario único. La solución le entrega datos y no emite documentos tributarios por cuenta propia. No habrá dos verdades contables. | Restricción no negociable N°4 del Capítulo 10. |
| 3 | Los documentos tributarios electrónicos (guía de despacho electrónica, factura, nota de crédito y acuse de recibo) se rigen por la normativa de la autoridad tributaria. La guía de despacho electrónica tiene efectos legales que la solución no puede comprometer. | Normativa tributaria chilena vigente. |
| 4 | La solución debe cumplir el Reglamento Sanitario de los Alimentos en materia de condiciones de almacenamiento, control de temperatura, registro de lotes y capacidad de ejecución de retiro de producto. | Marco regulatorio que originó el sumario sanitario de marzo de 2026. |
| 5 | La Ley N°21.719 de protección de datos personales aplica al tratamiento de datos comerciales y de comportamiento de pago de los 14.200 clientes (muchos de ellos personas naturales) y a los datos de geolocalización del personal en terreno. | Marco normativo vigente aplicable al proyecto. |
| 6 | La jornada de los conductores se rige por el régimen especial de jornada de los trabajadores del transporte, el cual condiciona la planificación de rutas y el uso de datos de posicionamiento para control de horas de conducción y descanso. | Marco normativo laboral vigente. |
| 7 | El sindicato de conductores objetó formalmente la instalación de cámaras en cabina y el uso del posicionamiento satelital para control de jornada. Cualquier propuesta que involucre esas tecnologías debe contemplar un plan explícito de gestión del cambio y negociación sindical. | Restricción no negociable N°10 del Capítulo 10. |
| 8 | El área de TI cuenta con cuatro personas para toda la empresa. Cualquier función operacional o de soporte que requiera un especialista dedicado que la compañía no tiene debe ofrecerse como servicio externo y estar costeada en la propuesta. | Restricción no negociable N°9 del Capítulo 10. |
| 9 | Están prohibidas las intervenciones en sistemas del 1 al 25 de septiembre y durante todo el mes de diciembre (peaks operacionales), y durante los tres primeros días hábiles de cada mes (cierre comercial y contable). | Restricción no negociable N°8 del Capítulo 10. |
| 10 | Los estándares GS1 para identificación de productos (GTIN), unidades logísticas (SSCC) y ubicaciones (GLN), así como los estándares de trazabilidad de eventos en la cadena de suministro, son el marco de referencia para la interoperabilidad con proveedores y con el canal moderno. | Normativa sectorial y condiciones comerciales del canal moderno. |
