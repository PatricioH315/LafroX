# Comprensión del problema y de la necesidad

El presente subdocumento expone el diagnóstico integral, operacional y estratégico de Distribuidora Puelche S.A. en el marco del caso. Se analiza la estructura de su modelo logístico actual (*AS-IS*), caracterizado por una profunda fragmentación de datos, procesos manuales en terreno y desacoples entre la promesa comercial y la capacidad física de distribución.

Este capítulo establece la línea base conceptual y cuantitativa para el resto de la propuesta: fundamenta los requerimientos funcionales y el alcance técnico, define los requerimientos no funcionales y de resiliencia, y delimita las restricciones operativas que condicionan la planificación de la implantación. El catálogo pormenorizado de requerimientos del cliente, el registro extendido de supuestos y exclusiones, y el inventario nominal de actores y sistemas legados se presentan en el archivo adjunto independiente **[LAFROX-Subdocumento2-Anexos.md](LAFROX-Subdocumento2-Anexos.md)**.

## Resumen Ejecutivo del problema

Distribuidora Puelche S.A. enfrenta una crisis de eficiencia y competitividad operacional producto de la obsolescencia y desarticulación de su ecosistema informático. Su operación integra los centros de distribución de Talca y Concepción y tres plataformas de *cross-docking*; las Bases presentan una discrepancia entre cinco y seis instalaciones que deberá confirmarse con el CLIENTE. La flota considera 42 camiones propios y 54 de diez transportistas, con cerca de 200 conductores en total, y atiende 14.200 puntos de entrega. La operación actual exhibe un índice de entrega a tiempo y completa (OTIF) de 82,4%. Por tanto, el 17,6% de los despachos no llega completo y a tiempo, deteriorando la relación con el canal tradicional y arriesgando contratos con el canal moderno.

La raíz del problema no reside en un único sistema defectuoso, sino en un tejido heterogéneo y desconectado: un ERP implantado en 2017 cuyos módulos satélites de preventa fueron abandonados por su proveedor, un WMS de 2013 con soporte discontinuado y procesos críticos gobernados mediante planillas de cálculo y papel. Esta desconexión tecnológica genera tres impactos críticos inmediatos:

1. **Vulnerabilidad sanitaria y regulatoria:** El retiro preventivo de marzo de 2026 demoró 9 días y alcanzó 4.800 kg del lote 24-0217, con una pérdida directa de $31 millones. El proveedor suspendió a Puelche por seis meses de su lista de distribuidores autorizados; ese proveedor representa el 6% de las ventas. En el producto involucrado, el 41% de las recepciones no registraba lote en el sistema.
2. **Fricción comercial y quiebre de preventa:** El 7,8% de los pedidos tomados en terreno presenta quiebre de stock al sincronizarse con la bodega, pues los 62 preventistas operan a ciegas mediante una aplicación móvil obsoleta sin visibilidad de inventario ni crédito en tiempo real.
3. **Opacidad financiera y fuga de recursos:** La empresa subsidia entregas ineficientes bajo un prorrateo de costo de servir estático fijado en 2016. La rendición manual diferida del efectivo genera $4,2 millones mensuales en diferencias no conciliadas; además, el 1,1% de las guías de despacho se extravía y retrasa la cobranza hasta 12 días por reclamo.

Estas brechas establecen la necesidad que debe abordar la oferta: recuperar trazabilidad de lote, hacer confiable la promesa de entrega, disminuir la pérdida de información en terreno y disponer de una base objetiva para gestionar el costo de servir. El Capítulo 3 define la solución y el alcance que responderán a estas necesidades.

## Comprensión del problema y de la necesidad

### Los tres problemas entrelazados

En concordancia con el análisis prescrito en las Bases de Licitación, la problemática de Puelche debe descomponerse en tres dimensiones interconectadas que se retroalimentan mutuamente:

1. **Habilitación sanitaria y comercial comprometida:** El cumplimiento del Reglamento Sanitario de los Alimentos (Decreto 977) exige el control riguroso de la cadena de frío (-18 °C a -22 °C) y la trazabilidad bidireccional inmediata de lotes. En la actualidad, el registro de temperatura es discontinuo e instrumentalizado por el propio conductor, sin alarmas automáticas ante excursiones térmicas. Al recibir mercadería de los 180 proveedores, el personal ingresa cantidades globales sin registrar lote ni fecha de vencimiento en el sistema informático, dejando la asignación sujeta a la memoria física de los bodegueros. Esta carencia no solo expone a sanciones de la autoridad sanitaria, sino que imposibilita cumplir las exigencias de certificación comercial que el canal moderno demandará a contar de 2029 (representando el 11% de la facturación).
2. **Pérdida de competitividad del servicio:** El nivel de servicio actual (OTIF 82,4% y *Fill Rate* 91,3%) compromete la permanencia en el canal moderno, que exige OTIF de al menos 95% desde enero de 2029. Los clientes del canal tradicional (11.600 almacenes) y *food service* (2.100 puntos) enfrentan faltantes y retrasos. La falta de visibilidad en preventa y la rigidez de las rutas provocan reentregas equivalentes al 4,2% de las entregas. Sobre la referencia de 1.400 entregas diarias, ello equivale a aproximadamente 59 reentregas al día (1.400 × 0,042 = 58,8).
3. **Desconocimiento estructural del costo de servir:** La fijación de precios y márgenes se calcula sobre un costo de transporte promedio estático que data de 2016. Puelche desconoce el costo real de atender a cada cliente, subsidiando rutas rurales remotas de baja densidad a expensas de clientes urbanos de alta rotación. La ocupación promedio de la flota es 68% y cae a 41% en días de baja utilización. La rotación anual de preparadores de pedidos alcanza 38%, lo que incrementa el esfuerzo de capacitación e induce errores recurrentes en el armado de pedidos.

### Contexto operacional, normativo y estacionalidad

La comprensión del negocio de Distribuidora Puelche S.A. exige interpretar sus restricciones regulatorias y sectoriales bajo el marco jurídico chileno vigente:

- **Reglamento Sanitario de los Alimentos (Decreto 977/1996 del Ministerio de Salud):** Obliga a mantener registros inalterables de temperatura en alimentos congelados (temperatura ≤ -18 °C) y a ejecutar procedimientos de retiro de mercado (*recall*) en plazos expeditos ante sospecha de contaminación microbiológica o química.
- **Documentos Tributarios Electrónicos (DTE - SII):** La Guía de Despacho Electrónica (GDE) rige el traslado legal de mercaderías. El acuse de recibo electrónico con constancia de entrega conforme o recepción con mermas es el instrumento probatorio que otorga mérito ejecutivo para la cobranza comercial y el cómputo del crédito fiscal IVA.
- **Normativa laboral de transportes (Código del Trabajo, Art. 25 bis):** Regula la jornada laboral de conductores y peonetas, fijando descansos mínimos y límites de conducción continua que condicionan estrictamente la longitud y duración de las rutas de despacho.
- **Ley 21.719 de Protección de Datos Personales:** La entrada en vigencia de la ley está fijada para el 1 de diciembre de 2026. Por ello, Puelche debe preparar el tratamiento de información comercial y comportamiento financiero de los almaceneros, y los controles telemáticos deben respetar la proporcionalidad laboral y la restricción del caso sobre cámaras y GPS.
- **Estándares sectoriales GS1 y EDI:** Demanda la adopción de identificadores universales (GTIN para productos, GLN para puntos de entrega, GS1-128 para unidades logísticas de carga) e intercambio electrónico de datos (EDI) para órdenes de compra, avisos de despacho (DESADV) y facturación electrónica con el gran retail chileno.

A este marco se añade el impacto crítico de la **estacionalidad**: durante las tres primeras semanas de septiembre, la demanda de productos cárnicos, lácteos y bebidas experimenta un incremento cercano al 100% (aproximadamente el doble del volumen promedio anual). Este pico satura la ventana de preparación nocturna (22:00 a 06:00 hrs) y genera congestión severa en la ventana crítica de despacho matinal (05:30 a 07:00 hrs). Un dimensionamiento informático o de flota calculado para promedios mensuales colapsa inevitablemente en este período. Similar tensión ocurre en diciembre y durante los cierres mensuales, mientras que los inviernos en las zonas rurales del Maule y Biobío imponen cortes recurrentes de caminos y pérdidas prolongadas de señal móvil.

### Arbitraje de tensiones operacionales y comerciales

El levantamiento de información en terreno reveló contradicciones estructurales entre las distintas gerencias de Puelche. Estas tensiones no constituyen discrepancias accidentales, sino el reflejo de objetivos locales descoordinados que LafroX arbitra de la siguiente forma:

1. **Promesa de entrega (Comercial contra Operaciones):** La Gerencia Comercial busca captar clientes prometiendo entregas en 24 horas a todo evento. La Gerencia de Operaciones afirma que tal promesa es materialmente imposible en la flota actual y genera frustración y reclamos. **Arbitraje LafroX:** Se establece una promesa de entrega segmentada y viable: 24 horas garantizadas exclusivamente para clientes ubicados en radios urbanos consolidados, condicionado a pedidos ingresados antes de la hora de corte (14:00 hrs). Para clientes rurales, periféricos o abastecidos mediante *cross-docking*, la promesa contractual se fija en 48 horas, transparentando la ventana de servicio en la aplicación de preventa.
2. **Control de cadena de frío (Calidad contra Operaciones):** La Jefa de Calidad exige que cualquier excursión térmica fuera de norma bloquee automáticamente el producto para entrega. Operaciones y los choferes argumentan que bloqueos ciegos obligan a retornar camiones cargados y provocan pérdidas catastróficas. **Arbitraje LafroX:** Se implementa una política graduada de control térmico: excursiones menores y transitorias (apertura de puertas durante descarga en ruta) activan alertas preventivas en cabina; únicamente ante excursiones críticas y sostenidas en el tiempo (que superen el umbral de descongelamiento del RSA) el sistema bloquea preventivamente el lote en el dispositivo móvil y notifica a Calidad para inspección inmediata.
3. **Gestión del efectivo (Finanzas contra Comercial):** Finanzas exige erradicar el efectivo y exigir transferencias o prepagos para evitar pérdidas. Comercial sostiene que exigir bancarización liquidará al canal tradicional. **Arbitraje LafroX:** Se respeta la condición del canal tradicional: el almacenero continuará pagando en efectivo. La solución introduce una conciliación atómica y vinculante en el punto de entrega: el chofer registra el monto exacto cobrado, el cliente valida digitalmente la transacción y el sistema cuadra en tiempo real los valores a rendir, eliminando la opacidad en la rendición diferida al día siguiente.

4. **Nube y cortes de enlace (Jefe de TI contra la operación):** El jefe de TI prefiere todo en la nube y él mismo explica por qué la operación no puede depender de ella: la fibra se corta cuatro veces al año, Concepción no tiene respaldo y las plataformas de cross-docking operan solo con red móvil. **Arbitraje LafroX:** Deberemos contemplar un método en el cual no se dependa completamente de sevicios externos como la nube o la fibra para que el sistema no detenga su funcionamiento una vez ocurran estos inconvenientes.

5. **Planificación de rutas (Conocimiento tácito contra Algoritmo):** La empresa depende absolutamente del criterio mental de un único planificador con más de 20 años en la compañía, quien se jubilará en dos años. Operaciones teme que un software estándar genere rutas teóricas absurdas que los choferes rechacen. **Arbitraje LafroX:** Durante los primeros meses se ejecutará un proceso de elicitación formal de conocimiento para incorporar las reglas empíricas del planificador en el motor de optimización, asegurando una transición fluida y la preservación del activo intelectual de Puelche.

## Dimensionamiento del problema

### Cuantificación del impacto operacional y financiero

Para dimensionar objetivamente la magnitud del desafío, la Tabla 2.1 consolida las métricas e indicadores operativos de la situación actual (*AS-IS*), contrastándolos con las pérdidas económicas y de servicio que generan.

**Dimensionamiento cuantitativo de las brechas operacionales de Distribuidora Puelche S.A. Fuente: Elaboración propia a partir de las Bases Técnicas del Caso 02.**

| **Indicador Operacional** | **Línea Base Actual** | **Meta o condición** | **Impacto Económico y Operacional en Puelche** |
| --- | --- | --- | --- |
| Entregas a tiempo y completas (OTIF) | 82,4% | ≥ 95,0% | 17,6% pedidos fallidos; riesgo de pérdida de cartera en retail moderno (11% ventas 2029). |
| Demora en retiro de mercado (*recall*) | 9 días | < 2 horas | Retiro preventivo marzo 2026: suspensión de 6 meses del proveedor (6% ventas). |
| Recepciones sin registro de lote | 41,0% del producto involucrado | 100% en productos que lo requieren | Imposibilidad de trazar productos en bodega y despacho; ruptura del estándar de inocuidad. |
| Quiebre de stock en preventa | 7,8% | Meta a acordar con el CLIENTE | Ventas perdidas no recuperadas; preventista compromete productos físicamente agotados. |
| Reentregas operacionales | 4,2% | Meta a acordar con el CLIENTE | Sobre 1.400 entregas diarias, equivale a aproximadamente 59 reentregas por día. |
| Diferencias mensuales de efectivo | $4,2 M/mes | Meta a acordar con el CLIENTE | Fuga de recursos en rendición diferida D+1. |
| Diferencia en conteo cíclico | 2,3% del valor contado | Meta a acordar con el CLIENTE | Descuadre entre inventario contable y existencias físicas. |
| Merma por vencimiento en bodega | 1,7% del valor del inventario al año | Meta a acordar con el CLIENTE | Pérdida de productos perecibles por ausencia de despacho FEFO (*First Expired, First Out*). |
| Ocupación promedio de camiones | 68,0% | Umbral a comprometer | Capacidad ociosa de transporte; días valle registran 41% de utilización de tolva. |
| Pérdida de guías de despacho (GDE) | 1,1% emitidas | Meta a acordar con el CLIENTE | Retrasos en cobranza de hasta 12 días promedio por ciclo de reclamo y refacturación. |

Del análisis de la Tabla 2.1 se desprende que las mayores pérdidas financieras de Puelche se concentran en tres fuentes: la merma por vencimiento y los descuadres de inventario, que se miden sobre bases distintas y por ello no se suman; el sobrecosto de fletes inducido por reentregas; y el impacto de las sanciones sanitarias por falta de trazabilidad.

### El enigma del cross-docking y los seis procesos AS-IS

Uno de los principales hallazgos del diagnóstico es el denominado **enigma del cross-docking**: la empresa invirtió en tres centros de transferencia con la promesa de reducir 24 horas del tiempo total de entrega, pero en la práctica solo logró una reducción neta de 8 horas. La brecha de 16 horas resulta de la diferencia entre ambos valores (24 - 8 = 16), pero las Bases señalan expresamente que su causa aún no se ha investigado.

La operación observada permite formular, sin anticipar una conclusión, la hipótesis de que la consolidación, la desconsolidación y la validación manual contribuyen a la brecha. Esta hipótesis debe validarse con mediciones de tiempos en Talca y en las tres plataformas antes de atribuir las 16 horas a un punto específico del proceso.

A continuación, se modelan y analizan los seis procesos críticos de la cadena logística actual (*AS-IS*) mediante diagramas de flujo que ilustran los puntos exactos de quiebre y pérdida de trazabilidad.

#### Proceso 1: Preventa y Toma de Pedidos AS-IS
Como se aprecia en la Figura 2.1, el flujo comercial parte con el preventista visitando al cliente en terreno con una aplicación móvil desconectada que no posee visibilidad de stock ni del estado crediticio del comprador.

**Figura 2.1 — Proceso de Preventa y Toma de Pedidos AS-IS**

1. El preventista visita presencialmente al cliente; participan 62 preventistas.
2. Captura el pedido en una aplicación móvil desconectada, sin visibilidad de stock ni crédito.
3. Sincroniza al final de la jornada en el centro de distribución, desde las 18:00 horas.
4. El proceso consulta si existe stock disponible y crédito aprobado.
5. Si la respuesta es afirmativa, el pedido ingresa formalmente a la cola de procesamiento del ERP.
6. Si la respuesta es negativa, el quiebre de stock se detecta tarde; afecta 7,8 % y produce pedidos mutilados o ventas perdidas.

*Fuente: elaboración propia. Transcripción textual de la figura original.*

El análisis de la Figura 2.1 demuestra que el 7,8% de quiebre de stock se detecta de forma tardía tras el fin de la jornada comercial (18:00 hrs), cuando el pedido ingresa a la cola del ERP y se descubre que las unidades comprometidas ya habían sido asignadas a otros clientes, generando reclamos comerciales y ventas frustradas.

#### Proceso 2: Recepción de Mercadería y Control de Lotes AS-IS
En la Figura 2.2 se ilustra el registro de recepciones en los muelles de los centros de distribución al descargar los envíos de los 180 proveedores.

**Figura 2.2 — Proceso de Recepción de Mercadería y Control de Lotes AS-IS**

1. Arriba un camión al muelle del centro de distribución; la operación se relaciona con 180 proveedores.
2. Se descargan y cuentan físicamente los bultos en el andén.
3. La recepción se registra manualmente en una planilla física o guía en papel.
4. El proceso consulta si lote y vencimiento fueron digitados en el sistema.
5. Si la respuesta es afirmativa, la mercadería queda con lote registrado.
6. Si la respuesta es negativa, queda comprometida la trazabilidad sanitaria; 41 % de las recepciones del producto involucrado en el retiro no tenía lote registrado.

*Fuente: elaboración propia. Transcripción textual de la figura original.*

El análisis de la Figura 2.2 muestra que el registro de lote y vencimiento no es confiable. En el producto involucrado en el retiro sanitario, 41% de las recepciones no registró lote. Ese antecedente no permite extrapolar el porcentaje a todas las recepciones, pero sí fundamenta la necesidad de medir cobertura de captura y trazabilidad de extremo a extremo.

#### Proceso 3: Preparación de Pedidos y Cross-Docking AS-IS
La preparación de carga y el trasvasije en centros de transferencia se detallan en la Figura 2.3.

**Figura 2.3 — Proceso de Preparación y Cross-Docking AS-IS**

1. Arriba el camión troncal al centro de transferencia.
2. Se descargan completamente los pallets al patio, sin muelle directo.
3. Se despaletiza y se realiza un conteo visual contra hojas impresas.
4. Se repaletiza manualmente y se rearman las rutas en el andén.
5. La carga se transfiere al camión de reparto.

*Fuente: elaboración propia. Transcripción textual de la figura original.*

El diagrama de la Figura 2.3 representa las actividades que deben medirse durante el levantamiento. La operación manual puede contribuir a la brecha de 16 horas entre la reducción prometida y la observada, pero no se presenta como su causa probada.

#### Proceso 4: Planificación de Rutas AS-IS
El proceso de diagramación de despachos y asignación de vehículos se ilustra en la Figura 2.4.

**Figura 2.4 — Proceso de Planificación de Rutas AS-IS**

1. Los pedidos confirmados quedan disponibles para planificación entre las 15:00 y las 18:30 horas.
2. Los datos se exportan manualmente a planillas Excel, sin interfaz directa.
3. Las rutas se diagraman manualmente con el conocimiento tácito del planificador.
4. Se imprimen las hojas de ruta y guías para la tripulación.
5. El despacho opera con rutas rígidas y subóptimas y alcanza 68 % de ocupación.

*Fuente: elaboración propia. Transcripción textual de la figura original.*

Como revela la Figura 2.4, la planificación descansa exclusivamente en planillas de cálculo y en la memoria del planificador. Este procedimiento impide simular alternativas dinámicas ante congestión o picos estacionales, derivando en un promedio de ocupación de camiones de solo 68%.

#### Proceso 5: Reparto y Entrega AS-IS
La interacción en la última milla entre los camiones de reparto y los puntos de destino se presenta en la Figura 2.5.

**Figura 2.5 — Proceso de Reparto y Entrega AS-IS**

1. El camión sale a ruta durante la ventana de despacho de 05:30 a 07:00 horas.
2. Arriba al local comercial, ya sea almacén o cliente de food service.
3. El proceso consulta si el local está abierto y el cliente está conforme.
4. Si la respuesta es afirmativa, el cliente firma físicamente la guía de despacho.
5. Si la respuesta es negativa, la carga retorna al centro de distribución; la tasa informada es 4,2 %, equivalente aproximadamente a 59 reentregas diarias sin aviso bajo el supuesto indicado en el texto.

*Fuente: elaboración propia. Transcripción textual de la figura original.*

Del análisis de la Figura 2.5 se evidencia que cuando un conductor enfrenta un local cerrado o un rechazo parcial, no cuenta con un canal en tiempo real para reasignar la ruta ni con protocolos de aviso. El camión retorna con la carga al CD al finalizar el día. La estimación mensual de reentregas requiere confirmar la relación entre pedido y entrega física, declarada como supuesto en el Anexo 2.2.

#### Proceso 6: Rendición y Cobranza AS-IS
Por último, la liquidación de valores cobrados en efectivo se esquematiza en la Figura 2.6.

**Figura 2.6 — Proceso de Rendición y Cobranza AS-IS**

1. Se cobra en efectivo en el punto de entrega del canal tradicional.
2. El dinero queda bajo custodia en la cabina o en el domicilio del conductor.
3. La rendición física se realiza al día siguiente en el centro de distribución, mediante papel.
4. El proceso consulta si la cuadratura atómica está conforme.
5. Si la respuesta es afirmativa, se efectúan el depósito bancario y la conciliación contable en el ERP.
6. Si la respuesta es negativa, quedan diferencias no conciliadas por $4,2 millones mensuales y no es posible rastrear el descuadre por entrega.

*Fuente: elaboración propia. Transcripción textual de la figura original.*

La Figura 2.6 ilustra el mecanismo asociado a diferencias no conciliadas de $4,2 millones mensuales: el dinero recaudado se rinde al día siguiente mediante planillas físicas. Cuando surgen descuadres, resulta imposible rastrear en qué entrega ocurrió el error.

## Actores y Grupos de Interés

El éxito del proyecto depende de alinear a los 19 actores que conforman el ecosistema de Distribuidora Puelche S.A. Cada uno posee incentivos, niveles de poder y resistencias particulares frente a la automatización de procesos.

Para analizar de manera sintética su nivel de involucramiento y las estrategias de gestión del cambio correspondientes, la Tabla 2.2 presenta la matriz consolidada de grupos de interés del proyecto.

**Matriz de síntesis de actores, tensiones operacionales y estrategia de gestión**

| % L2.8cm Y C1.8cm C1.8cm L3.5cm% **Grupo / Estamento** | **Tensión / Desafío Principal** | **Influencia** | **Interés** | **Estrategia de Gestión** Dirección Estratégica <br> (Gerenta General, Comercial, Finanzas) | Discrepancia entre promesa comercial de 24 h y viabilidad operativa real; urgencia de retener canal moderno al 2029; opacidad en el costo de servir. | Muy Alta | Muy Alto | Arbitraje formal de promesa (24 h urbana / 48 h rural con corte a las 14:00); modelación analítica del costo de servir por canal. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Jefaturas Operacionales y Soporte <br> (Operaciones, Calidad, Bodega, TI, Planificador) | Brecha de 16 h no investigada entre reducción prometida y observada en cross-docking; riesgo de sumarios sanitarios por quiebre de lote; dependencia crítica de planificador único (jubilación en 2 años). | Alta | Muy Alto | Automatización de control térmico en cámaras (-22 °C); talleres de elicitación de heurísticas de ruteo; soporte externo 24×7 para mitigar dotación de TI (4 personas). |  |  |  |  |
| Personal Operativo de Terreno <br> (62 Preventistas, 84 conductores y peonetas propios, aprox. 160 externos, 120 Preparadores, Sindicato) | Uso de app obsoleta sin stock ni crédito (7,8% quiebre preventa); riesgo en transporte de efectivo ($4,2M/mes en diferencias); resistencia sindical a cámaras y GPS intrusivo. | Alta | Alto | Aplicación móvil *offline-first* ágil; prueba digital de entrega (POD); protocolo de conciliación atómica de dinero; enfoque de monitoreo centrado en activos y no en control laboral. |  |  |  |  |
| Clientes y Canales de Venta <br> (11.600 Tradicionales, 2.100 Food Service, 500 Modernos) | 17,6% de entregas fallidas o tardías (OTIF 82,4%); almaceneros sin internet ni dispositivo que pagan en efectivo; exigencia estricta de EDI/GDE en canal moderno hacia 2029. | Muy Alta | Alto | Preservación intacta de la compra tradicional sin imponer barreras tecnológicas; ventanas matinales (<10:00) para Food Service; cumplimiento de estándares GS1 y EDI para retail. |  |  |  |  |
| Proveedores, Transportistas y Autoridad <br> (180 Proveedores, 10 Transportistas, SEREMI de Salud) | En el producto involucrado en el retiro, 41% de recepciones sin registro de lote; rotación de choferes externos sin relación contractual directa; riesgo de sumario sanitario y clausura (Decreto 977 / RSA). | Media-Alta | Alto | Validación digital de lotes en muelle de descarga; acuerdos marco con transportistas; trazabilidad y auditoría de recall en menos de 2 horas ante requerimiento sanitario. |  |  |  |  |

El análisis de la Tabla 2.2 permite concluir que el principal foco de resistencia al cambio no se ubica en los clientes del canal tradicional (quienes acogen favorablemente cualquier mejora que no les altere su hábito de pago), sino en el personal operativo de terreno y sus organizaciones sindicales. La oposición histórica del sindicato a las cámaras en cabina y al rastreo satelital laboral demanda una estrategia de implantación basada en la transparencia: los sistemas telemáticos deben orientarse al aseguramiento de la carga y el activo vehicular, sin invadir la privacidad individual del conductor. De igual modo, la captura del conocimiento tácito del planificador de rutas exige una dinámica de reconocimiento formal de su experiencia profesional.

El catálogo extendido y nominal con el detalle de los 19 actores se encuentra disponible en el Anexo 2.3 de **[LAFROX-Subdocumento2-Anexos.md](LAFROX-Subdocumento2-Anexos.md)**.

## Resumen de Requerimientos, Supuestos, Exclusiones y Restricciones

### Resumen y análisis de requerimientos del cliente
A partir del análisis del problema y de las entrevistas a los actores clave, el cliente exige una solución que satisfaga un catálogo integral de requerimientos funcionales y no funcionales. Los principales ejes funcionales demandados abarcan:

- **Preventa y comercialización:** Captura de pedidos con validación de inventario y crédito en línea, soportando operación 100% desconectada con sincronización determinista sin pérdida transaccional.
- **Gestión de bodegas y trazabilidad de lotes:** Recepción con captura obligatoria de lote y vencimiento (GS1-128), gestión estricta FEFO en cámaras de frío (-22 °C) y capacidad de ejecutar recalls en menos de 2 horas.
- **Despacho y última milla:** Optimización de rutas urbanas y rurales con ventanas de servicio diferenciadas, prueba digital de entrega (POD) con captura de firma y fotografía, y acuse de recibo de Guía de Despacho Electrónica.
- **Conciliación financiera:** Registro atómico de cobranzas en efectivo y cuadratura vinculante en el punto de entrega.

El catálogo completo y priorizado de requerimientos funcionales y no funcionales se detalla en el Anexo 2.1 de **[LAFROX-Subdocumento2-Anexos.md](LAFROX-Subdocumento2-Anexos.md)**.

### Supuestos de ingeniería formulados por LafroX
Para diseñar una propuesta técnicamente sólida y exenta de contingencias imprevistas, LafroX formula un conjunto de supuestos propios de ingeniería, deslindándolos formalmente de las restricciones impuestas por las bases. El detalle, con fundamento, impacto y mecanismo de validación, se presenta en el Anexo 2.2 de **[LAFROX-Subdocumento2-Anexos.md](LAFROX-Subdocumento2-Anexos.md)**.

### Exclusiones y restricciones no negociables
Complementariamente, la Tabla tab:restricciones-caso sintetiza las restricciones del caso. La inmutabilidad de la operación del canal tradicional y la estricta prohibición de intervenir sistemas en períodos de *blackout* (como el mes de septiembre) condicionan la arquitectura del software: exigen desacoplar los módulos de terreno para operar con alta autonomía local y programar las marchas blancas fuera de los períodos de alta intensidad estacional. El inventario íntegro de exclusiones y restricciones se encuentra en el Anexo 2.2 de **[LAFROX-Subdocumento2-Anexos.md](LAFROX-Subdocumento2-Anexos.md)**.

**Síntesis de restricciones y exclusiones no negociables del caso**

| % C0.8cm L3.8cm Y L3.2cm% **N°** | **Restricción / Exclusión** | **Descripción Operativa / Legal** | **Origen / Cláusula** R1 | Inmutabilidad operativa del Canal Tradicional. | Los 11.600 almacenes pagan en efectivo y carecen de internet; la solución no puede obligarles a adquirir dispositivos ni modificar su proceso de compra. | Acta del Comité Ejecutivo; Restricción Cap. 10. |
| --- | --- | --- | --- | --- | --- | --- |
| R2 | ERP 2017 como verdad contable única. | El ERP no se sustituye. La plataforma captura y entrega datos transaccionales, pero el ERP emite los documentos tributarios legales. | Restricción no negociable N° 4 del Cap. 10. |  |  |  |
| R3 | Validez y efectos legales de DTEs y RSA. | Estricto cumplimiento del Decreto 977 (RSA), control de frío (-18 °C a -22 °C) y validez tributaria de Guías de Despacho Electrónicas. | Normativa sanitaria y tributaria chilena. |  |  |  |
| R4 | Resguardo de privacidad laboral y oposición sindical. | Prohibición de cámaras en cabina y monitoreo por GPS enfocado en productividad personal; el sindicato vetó la vigilancia intrusiva. | Restricción N° 10 Cap. 10; Dictámenes Dirección del Trabajo. |  |  |  |
| R5 | Ventanas de congelamiento de sistemas (Blackouts). | Prohibición absoluta de intervenciones, despliegues o cambios del 1 al 25 de septiembre, diciembre completo y primeros 3 días hábiles de cada mes. | Restricción N° 8 del Cap. 10. |  |  |  |

## Referencias

- Distribuidora Puelche S.A. (2026a). *Bases Administrativas de Licitación N° TFEP-01/2026: Contratación de Solución Integral de Software y Servicios de Operación*.
- Distribuidora Puelche S.A. (2026b). *Bases Técnicas Transversales de Licitación N° TFEP-01/2026*.
- Distribuidora Puelche S.A. (2026c). *Caso 02: Logística – Especificaciones del Problema y Operación de Distribuidora Puelche S.A.*
- Distribuidora Puelche S.A. (2026d). *Aclaraciones de la Licitación N° TFEP-01/2026*.
- GS1 Chile. (2020). *Estándares de Identificación y Trazabilidad Logística GS1: Guía de Aplicación para Consumo Masivo y Retail* (Versión 20.0). GS1.
- Ministerio de Salud. (1996). *Decreto Supremo N° 977: Aprueba Reglamento Sanitario de los Alimentos*. Diario Oficial de la República de Chile.
- Ministerio del Interior y Seguridad Pública. (2024). *Ley N° 21.719: Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales*. Biblioteca del Congreso Nacional de Chile.
- Ministerio del Trabajo y Previsión Social. (2002). *Código del Trabajo de la República de Chile: Artículo 25 bis sobre jornada especial de transporte de carga*. Edición oficial.
- Servicio de Impuestos Internos. (2024). *Manual de Procedimientos y Requisitos de Documentos Tributarios Electrónicos (DTE)*. SII Chile.

## Declaración de uso de IA

En cumplimiento de lo establecido en la Sección 7.2 de las Aclaraciones de la Licitación, se declara el uso asistido de herramientas de inteligencia artificial en la elaboración del presente subdocumento:

**Declaración de uso de Inteligencia Artificial por sección del Subdocumento 2.**

| **Sección** | **Herramienta** | **Finalidad del uso** | **Texto** | **Diag.** | **Revisión humana** |
| --- | --- | --- | --- | --- | --- |
| 2.1 Resumen Ejec. | Claude / Gemini | Síntesis ejecutiva y estilo formal | Bajo | Ninguno | Alex Aravena (JP): Validación del resumen y propuesta de valor |
| 2.2 Comprensión | Claude / Gemini | Estructuración de los 3 problemas | Bajo | Ninguno | Patricio Henríquez (Gest): Verificación de arbitraje de tensiones |
| 2.3 Dimensionamiento | Claude / Gemini | Asistencia en código TikZ de 6 flujos | Bajo | Medio | Tomás Pérez (Des): Verificación de flujos AS-IS y cálculos |
| 2.4 Actores | Claude / Gemini | Disposición tabular de actores | Bajo | Ninguno | Patricio Henríquez (Gest): Consistencia con catálogo de actores |
| 2.5 Requerimientos | Claude / Gemini | Formato y redacción de supuestos | Bajo | Ninguno | Bastián Trejo (Arq): Deslinde de supuestos vs restricciones |
| Anexo 2.1 | Claude / Gemini | Maquetación del listado de requerimientos | Bajo | Ninguno | Bastián Trejo (Arq): Coherencia con el catálogo canónico |
| Anexo 2.2 | Claude / Gemini | Consolidación de decisiones, exclusiones y restricciones | Bajo | Ninguno | Alex Aravena (JP): Cotejo con los capítulos 10, 11 y 16.1 del caso |
| Anexo 2.3 | Claude / Gemini | Maquetación de actores y sistemas legados | Bajo | Ninguno | Patricio Henríquez (Gest): Cotejo de actores, cifras y sistemas con el caso |
