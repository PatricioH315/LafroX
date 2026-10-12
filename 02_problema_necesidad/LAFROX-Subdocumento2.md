# Subdocumento 02 — Problema y necesidad

# Introducción al Problema y Necesidad

El presente subdocumento expone el diagnóstico integral, operacional y estratégico de Distribuidora Puelche S.A. en el marco del caso. Se analiza la estructura de su modelo logístico actual (*AS-IS*), caracterizado por una profunda fragmentación de datos, procesos manuales en terreno y desacoples entre la promesa comercial y la capacidad física de distribución.

Este capítulo establece la línea base conceptual y cuantitativa para el resto de la propuesta: fundamenta los requerimientos funcionales y el alcance técnico, define los requerimientos no funcionales y de resiliencia, y delimita las restricciones operativas que condicionan la planificación de la implantación. El catálogo pormenorizado de requerimientos del cliente, el registro extendido de supuestos y exclusiones, y el inventario nominal de actores y sistemas legados se presentan en los Anexos 2.1 a 2.3 de este subdocumento.

## 2.1 Resumen Ejecutivo del problema

Distribuidora Puelche S.A. enfrenta una crisis de eficiencia y competitividad operacional producto de la obsolescencia y desarticulación de su ecosistema informático. Su operación integra los centros de distribución de Talca y Concepción y tres plataformas de *cross-docking*. La flota considera 42 camiones propios y 54 de diez transportistas. En reparto trabajan 84 conductores y peonetas propios y cerca de 160 conductores de transportistas, y se atienden 14.200 puntos de entrega. La operación actual exhibe un índice de entrega a tiempo y completa (OTIF) de 82,4 %, frente a una referencia de 95 % (Distribuidora Puelche S.A., 2026c, cap. 7, tabla 7.1, p. 11). Por tanto, el 17,6 % de los despachos no llega completo y a tiempo. Esto deteriora la relación con el canal tradicional y pone en riesgo a la principal cadena de supermercados, que representa el 11 % de la venta y fija nuevas condiciones desde enero de 2029 (Distribuidora Puelche S.A., 2026c, cap. 1, p. 3).

La raíz del problema no reside en un único sistema defectuoso, sino en un tejido heterogéneo y desconectado: un ERP implantado en 2017 cuyos módulos satélites de preventa fueron abandonados por su proveedor, un WMS de 2013 con soporte discontinuado y procesos críticos gobernados mediante planillas de cálculo y papel. Esta desconexión tecnológica genera tres impactos críticos inmediatos:

1. **Vulnerabilidad sanitaria y regulatoria:** El retiro preventivo de marzo de 2026 demoró 9 días y alcanzó 4.800 kg del lote 24-0217, con una pérdida directa de dinero. El proveedor suspendió a Puelche por seis meses de su lista de distribuidores autorizados; ese proveedor representa el 6 % de las ventas. En el producto involucrado, el 41 % de las recepciones no registraba lote en el sistema.

2. **Fricción comercial y quiebre de preventa:** El 7,8 % de las líneas de pedido tomadas en terreno presenta quiebre de stock, pues los 62 preventistas operan a ciegas mediante una aplicación móvil obsoleta sin visibilidad de inventario ni crédito en tiempo real.

3. **Opacidad financiera y diferencias de rendición sin investigar:** La empresa subsidia entregas ineficientes bajo un prorrateo de costo de servir estático fijado en 2016. La rendición manual diferida del efectivo genera diferencias no conciliadas; además, el 1,1 % mensual de las guías de despacho se extravía o queda ilegible; ante un reclamo de entrega no recibida, encontrar la guía toma en promedio 12 días.

Estas brechas establecen la necesidad que debe abordar la oferta: recuperar trazabilidad de lote, hacer confiable la promesa de entrega, disminuir la pérdida de información en terreno y disponer de una base objetiva para gestionar el costo de servir. El Capítulo 3 define la solución y el alcance que responderán a estas necesidades.

## 2.2 Comprensión del problema y de la necesidad

Esta sección descompone el problema en tres dimensiones, lo sitúa en su contexto operacional, normativo y estacional, registra las tensiones entre áreas que la solución debe resolver y explica las prácticas de la industria que el caso pide investigar.

### 2.2.1 Los tres problemas entrelazados

El caso pide distinguir tres problemas entrelazados (Distribuidora Puelche S.A., 2026c, cap. 19, p. 35). La problemática de Puelche se descompone en esas tres dimensiones, que se retroalimentan:

1. **Habilitación sanitaria y comercial comprometida:** El cumplimiento del Reglamento Sanitario de los Alimentos (Decreto 977) exige el control riguroso de la cadena de frío (congelados a −18 °C o menos; la cámara de congelado de Talca opera a −22 °C) (Ministerio de Salud, 1996) y la trazabilidad bidireccional inmediata de lotes. En la actualidad, el registro de temperatura es discontinuo e instrumentalizado por el propio conductor, sin alarmas automáticas ante excursiones térmicas. Al recibir mercadería de los 180 proveedores, el personal revisa las fechas de vencimiento por muestreo y registra el lote de manera incompleta, en un campo de texto libre. La trazabilidad depende del papel de recepción y de la memoria de quienes despacharon, sin estar disponible de forma consultable en los sistemas. Esta carencia expone a Puelche a sanciones de la autoridad sanitaria, que ya observó la ausencia de registro continuo de temperatura en su última fiscalización. También le impide acreditar ante el proveedor de lácteos la capacidad de trazabilidad que este exige para restablecer la relación tras la suspensión, que vence en septiembre de 2026.

2. **Pérdida de competitividad del servicio:** El nivel de servicio actual (OTIF 82,4 % y *fill rate* 91,3 %) está lejos de las referencias de 95 % y 97 % que el caso asocia a esos indicadores. Además, la principal cadena exigirá desde enero de 2029 pedido electrónico, aviso de despacho, ventana de entrega de 30 minutos con penalización y prueba de entrega digital. Hoy Puelche entrega entre las 08:00 y las 18:00. Los clientes del canal tradicional (11.600 almacenes) y *food service* (2.100 puntos) enfrentan faltantes y retrasos. La falta de visibilidad en preventa y la rigidez de las rutas provocan reentregas equivalentes al 4,2 % de las entregas. Sobre la referencia de 1.400 entregas diarias, ello equivale a aproximadamente 59 reentregas al día (1.400 × 0,042 = 58,8).

3. **Desconocimiento estructural del costo de servir:** La fijación de precios y márgenes se calcula sobre un costo de transporte promedio estático que data de 2016. Puelche desconoce el costo real de atender a cada cliente, subsidiando rutas rurales remotas de baja densidad a expensas de clientes urbanos de alta rotación. La ocupación promedio de la flota es 68 % y cae a 41 % en días de baja utilización. La rotación anual de preparadores de pedidos alcanza 38 %, lo que incrementa el esfuerzo de capacitación e induce errores recurrentes en el armado de pedidos.

Los tres problemas no son independientes: comparten la causa descrita en la sección 2.1, un dato que no se registra donde ocurre el hecho. La cadena parte en la habilitación sanitaria: sin lote en la recepción no se puede saber qué cliente recibió qué producto. Sigue en el servicio: sin stock confiable en la preventa ni evidencia digital de la entrega, el OTIF no se puede medir de una sola forma ni mejorar. Y termina en el costo: si la entrega no deja registro de su tiempo, su carga y sus reentregas, el costo de servir solo puede seguir prorrateándose con el criterio de 2016. Por eso la captura del dato es la condición previa para medir el servicio y, después, para conocer el costo.

### 2.2.2 Contexto operacional, normativo y estacionalidad

La comprensión del negocio de Distribuidora Puelche S.A. exige interpretar sus restricciones regulatorias y sectoriales bajo el marco jurídico chileno vigente:

- **Reglamento Sanitario de los Alimentos (Decreto 977/1996 del Ministerio de Salud):** (Ministerio de Salud, 1996). Obliga a mantener registros inalterables de temperatura en alimentos congelados (temperatura ≤ −18 °C) y a ejecutar procedimientos de retiro de mercado (*recall*) en plazos expeditos ante sospecha de contaminación microbiológica o química.

- **Documentos Tributarios Electrónicos (DTE - SII):** (Servicio de Impuestos Internos, 2024). La Guía de Despacho Electrónica (GDE) rige el traslado legal de mercaderías. El acuse de recibo electrónico con constancia de entrega conforme o recepción con mermas es el instrumento probatorio que otorga mérito ejecutivo para la cobranza comercial y el cómputo del crédito fiscal IVA.

- **Normativa laboral de transportes:** El artículo 25 bis del Código del Trabajo regula la jornada y los descansos de los choferes de vehículos de carga terrestre interurbana. Estas condiciones deben considerarse al planificar las rutas a las que resulte aplicable esta regulación (Ministerio del Trabajo y Previsión Social, 2002, art. 25 bis).

- **Ley 21.719 de Protección de Datos Personales:** La entrada en vigencia de la ley está fijada para el 1 de diciembre de 2026 (Ley N.º 21.719, 2024, art. primero transitorio). Por ello, Puelche debe preparar el tratamiento de información comercial y comportamiento financiero de los almaceneros, y los controles telemáticos deben respetar la proporcionalidad laboral y la restricción del caso sobre cámaras y GPS.

- **Estándares sectoriales GS1 y EDI:** Las claves GS1 identifican de forma única los productos (GTIN), las ubicaciones, como los puntos de entrega (GLN), y las unidades logísticas (SSCC) (GS1 Chile, s. f.-b). Sobre esas claves se apoya el intercambio electrónico de datos (EDI) con el gran retail chileno, para órdenes de compra, avisos de despacho y facturas (GS1 Chile, s. f.-a).

A este marco se añade el impacto crítico de la **estacionalidad**, durante las tres primeras semanas de septiembre el volumen diario casi se duplica, de ≈ 1.400 a ≈ 2.600 entregas (Distribuidora Puelche S.A., 2026c, sección B.2, pp. 38–39). Este pico satura la ventana de preparación nocturna (22:00 a 06:00 hrs) y genera congestión severa en la ventana crítica de despacho matinal (05:30 a 07:00 hrs). Un dimensionamiento informático o de flota calculado para promedios mensuales colapsa inevitablemente en este período. Similar tensión ocurre en diciembre y durante los cierres mensuales, mientras que en invierno los caminos rurales empeoran y alargan los tramos sin señal, que en rutas de hasta 240 km ya llegan a dos horas.

### 2.2.3 Arbitraje de tensiones operacionales y comerciales

Las entrevistas de levantamiento del caso (Distribuidora Puelche S.A., 2026c, cap. 8, pp. 13–17) muestran contradicciones estructurales entre las distintas gerencias de Puelche. Estas tensiones no constituyen discrepancias accidentales, sino el reflejo de objetivos locales descoordinados que exigen una decisión antes de diseñar la solución. Para cada tensión se indica la decisión que la necesidad requiere:

1. **Promesa de entrega (Comercial contra Operaciones):** La Gerencia Comercial busca captar clientes prometiendo entregas en 24 horas a todo evento. La Gerencia de Operaciones afirma que tal promesa es materialmente imposible en la flota actual y genera frustración y reclamos. **Decisión que requiere la necesidad:** una promesa segmentada y viable: 24 horas para clientes urbanos con pedidos ingresados antes del corte de las 14:00, y 48 horas para clientes rurales, periféricos o abastecidos mediante *cross-docking*. El corte de las 14:00 sigue el día operativo del caso: la preventa trabaja de 09:00 a 18:00, pero las rutas del día siguiente se planifican de 15:00 a 18:30 y esa planificación depende de que los pedidos estén cerrados; después vienen la preparación de 22:00 a 06:00 y la salida de los camiones de 05:30 a 07:00 (Distribuidora Puelche S.A., 2026c, sección B.1, p. 38). Un pedido urbano que llega después del corte ya no alcanza ese ciclo. Cómo se informa la promesa al cliente se desarrolla en el Subdocumento 3.

2. **Control de cadena de frío (Calidad contra Operaciones):** La Jefa de Calidad exige que cualquier excursión térmica fuera de norma bloquee automáticamente el producto para entrega. Operaciones y los choferes argumentan que bloqueos ciegos obligan a retornar camiones cargados y provocan pérdidas catastróficas. **Decisión que requiere la necesidad:** un control térmico graduado: las excursiones menores y transitorias (apertura de puertas durante la descarga) justifican una advertencia, y solo las críticas y sostenidas (sobre el umbral del RSA) justifican retener el lote; la decisión final sobre el producto es de Calidad (Anexo 2.2, S-04). El mecanismo de alerta y retención se desarrolla en el Subdocumento 3.

3. **Gestión del efectivo (Finanzas contra Comercial):** Finanzas exige erradicar el efectivo y exigir transferencias o prepagos para evitar pérdidas. Comercial sostiene que exigir bancarización liquidará al canal tradicional. **Decisión que requiere la necesidad:** se respeta el pago en efectivo del canal tradicional, sin exigir al almacenero un dispositivo propio. La necesidad es que cada cobro quede asociado a su entrega y que la diferencia de rendición pueda rastrearse por entrega, en vez de detectarse al día siguiente. El mecanismo de registro, comprobante y cuadratura se desarrolla en el Subdocumento 3.

4. **Nube y cortes de enlace (Jefe de TI contra la operación):** El jefe de TI prefiere todo en la nube y él mismo explica por qué la operación no puede depender de ella: la fibra se corta cuatro veces al año, Concepción no tiene respaldo y las plataformas de cross-docking operan solo con red móvil. **Decisión que requiere la necesidad:** la preferencia por la nube es admisible solo si la operación no depende del enlace. Cada centro de distribución debe poder recibir, preparar y despachar durante al menos 24 horas sin enlace, y la preventa y el reparto deben operar un turno completo de 14 horas sin señal, sin pérdida ni duplicación de registros al reconectar (Distribuidora Puelche S.A., 2026c, cap. 10, restricciones 2 y 3, p. 19, y cap. 15, p. 26). Las Bases tampoco admiten una propuesta exclusivamente en nube: el modelo debe ser híbrido (Distribuidora Puelche S.A., 2026a, art. 16.1, p. 11). La solución que lo cumple se describe en el Subdocumento 3 y su arquitectura, en el Subdocumento 4.

5. **Planificación de rutas (Conocimiento tácito contra Algoritmo):** La empresa depende absolutamente del criterio mental de un único planificador con más de 20 años en la compañía, quien se jubilará en dos años. Operaciones teme que un software estándar genere rutas teóricas absurdas que los choferes rechacen. **Decisión que requiere la necesidad:** el conocimiento del planificador debe quedar explícito, documentado y validado por él antes de su jubilación, mediante una elicitación formal durante los primeros meses; cualquier ruta propuesta debe poder corregirse manualmente y respetar las restricciones de terreno que hoy solo él conoce (Anexo 2.2, S-16). El mecanismo se desarrolla en el Subdocumento 3.

### 2.2.4 Prácticas de la industria que el caso pide investigar

El caso enumera doce materias que el proponente debe investigar porque el documento no las explica (Distribuidora Puelche S.A., 2026c, sección 16.2, pp. 29–30). La sección 2.2.2 trata cuatro de ellas: los estándares GS1, los documentos tributarios electrónicos, el Reglamento Sanitario y la jornada del transporte. Esta sección cubre las ocho restantes. En cada una se resume lo que establece la norma o la literatura técnica y se contrasta con la situación de Puelche; cómo abordarlas corresponde al Subdocumento 3.

**Intercambio electrónico con el retail.** En el comercio minorista, el pedido, el aviso de despacho y la factura viajan como mensajes estructurados que el sistema del receptor lee sin digitación. GS1 define esos mensajes sobre sus claves globales y en un formato que no depende del software de cada empresa: órdenes de compra, facturas y avisos de despacho y de recepción (GS1 Chile, s. f.-a). En el estándar EANCOM corresponden a los mensajes ORDERS, DESADV e INVOIC (GS1, 2016). Los mensajes además necesitan un canal. En Chile, GS1 opera Comercionet, un servicio que transmite documentos electrónicos entre las empresas de su comunidad (GS1 Chile, s. f.-c); la alternativa es una conexión directa entre las partes, como la que define el protocolo AS2, que firma y cifra cada envío y devuelve un acuse de recepción (Moberg y Drummond, 2005). Puelche no recibe hoy ningún pedido por vía electrónica, y la cadena que concentra el 11 % de su venta exigirá desde 2029 pedido electrónico y aviso de despacho anticipado (Distribuidora Puelche S.A., 2026c, cap. 1, p. 3, y cap. 7, tabla 7.3, p. 12). Mientras no se sepa qué mensajes, qué versión y qué canal exige esa cadena, no se puede medir cuánto le falta a Puelche para cumplir.

**Cadena de frío.** El Reglamento Sanitario exige mantener los congelados a −18 °C y tolera, por períodos breves, que suban hasta −12 °C; para los demás alimentos refrigerados, remite a las recomendaciones técnicas del fabricante (Ministerio de Salud, 1996, arts. 71 y 192). Esa tolerancia muestra qué es una excursión térmica: no basta saber cuánto se alejó la temperatura, también importa cuánto duró. Medir la duración exige registrar tiempo y temperatura en cada etapa, desde la cámara hasta la entrega; así evalúan las cadenas de frío comerciales los estudios de campo que revisan Mercier et al. (2017). En Puelche la temperatura se anota dos veces por turno en las cámaras y tres veces por viaje en los camiones, y nadie ha escrito qué excursión invalida un producto (Distribuidora Puelche S.A., 2026c, sección 4.9, p. 9, y cap. 8, p. 15). Con esos registros no se puede probar que el frío se mantuvo, que fue justo lo que faltó cuando un cliente de *food service* rechazó un camión completo.

**Indicadores de servicio.** El OTIF cuenta los pedidos entregados completos y a tiempo, pero admite variantes, por lo que su definición debe acordarse; el pedido perfecto exige además que el pedido llegue sin daño y con la documentación correcta (Distribuidora Puelche S.A., 2026c, cap. C, pp. 39–40). El *fill rate* mide la fracción de la demanda que se atiende con stock, y no da lo mismo calcularlo por producto o por pedido. Un pedido al que le falta una sola línea cuenta como incumplido en la medición por pedido, pero casi no mueve la medición por producto (Chopra y Meindl, 2016). En Puelche el OTIF es 82,4 % y el *fill rate* 91,3 %, pero el caso no dice con qué base se calculan, y cuando una entrega falla la causa cambia según a quién se le pregunte (Distribuidora Puelche S.A., 2026c, cap. 8, p. 13). La definición de OTIF que adopta LafroX es el supuesto S-01 del Anexo 2.2.

**Costo de servir y costo por entrega.** El costo de servir asigna a cada cliente los costos de las actividades que consume su atención, como el transporte, la entrega, las devoluciones o la gestión del pedido; el costo por entrega reparte ese mismo costo entre las entregas del período. Guerreiro et al. (2008) lo aplicaron en una empresa brasileña de alimentos y concluyeron que da una visión de la rentabilidad de cada cliente más completa que el costeo tradicional. Puelche reparte el costo por zona con un criterio de 2016 y no mide el costo de cada viaje (Distribuidora Puelche S.A., 2026c, cap. 1, p. 3, y sección 4.4, p. 8). Ese prorrateo trata igual a dos almacenes de una misma zona aunque uno quede en una calle urbana y el otro al final de una ruta rural, y por eso Puelche no sabe si gana o pierde con un almacén pequeño de Empedrado que le compra cada dos semanas.

**Ruteo con capacidad y ventanas de tiempo.** Armar las rutas es un problema de ruteo de vehículos con capacidad y ventanas de tiempo (VRPTW): cada camión tiene un límite de carga, cada cliente un horario de recepción, y se busca cumplir ambos al menor costo. Los métodos exactos tienen límites de tamaño y de tiempo de cálculo, así que en la práctica se usan heurísticas, que entregan buenas soluciones sin garantizar la óptima (Toth y Vigo, 2014). La investigación reciente agrega a esa formulación cada vez más condiciones reales de la operación (Vidal et al., 2020), pero ningún método respeta una restricción que no se le haya entregado. En Puelche esas restricciones están en la cabeza del planificador: las ventanas horarias que conoce de memoria y los caminos que sabe que están malos (Distribuidora Puelche S.A., 2026c, sección 4.4, p. 8). Eso explica su desconfianza ante un software estándar, porque una ruta calculada sin esas reglas puede verse bien en el papel y no servir en la calle. Cuando él no está, el cumplimiento de entrega cae entre 6 y 9 puntos.

**Preparación de pedidos y ubicación en bodega.** La literatura distingue varias formas de organizar la preparación: por zonas, en que cada preparador cubre un sector; por lotes, en que se juntan varios pedidos en un mismo recorrido; y por olas, en que se liberan a la vez los pedidos con un mismo destino, por ejemplo los de un camión con hora fija de salida. La ubicación de los productos sigue una lógica parecida: el almacenamiento por clases agrupa los productos según su rotación y deja los de más movimiento más cerca de la salida (de Koster et al., 2007). En Talca cada preparador arma un pedido completo con una hoja impresa, y no existe una regla de ubicación por rotación, peso o compatibilidad: los productos de alta rotación siguen donde quedaron hace trece años, aunque la rotación cambió (Distribuidora Puelche S.A., 2026c, secciones 4.2 y 4.5, pp. 7–8). Con una rotación anual de 38 % entre los preparadores, la jefa de bodega dice que cada mes llega gente nueva que no sabe dónde está nada (Distribuidora Puelche S.A., 2026c, cap. 8, p. 14).

**Pronóstico de demanda.** En el comercio minorista, las promociones están entre los factores que más alteran la demanda: elevan la venta mientras duran y la deprimen después, sobre todo en productos que el cliente puede almacenar. Además, es común que el pronóstico se ajuste a mano durante una promoción, con resultados irregulares (Fildes et al., 2022). Del pronóstico dependen el stock de seguridad y el nivel de servicio que se puede sostener (Chopra y Meindl, 2016). Puelche repone con una planilla que considera la venta de las últimas ocho semanas y un ajuste manual por temporada; las promociones se agregan a mano cuando comercial avisa, y comercial no siempre avisa (Distribuidora Puelche S.A., 2026c, sección 4.1, p. 7). Ese método deja fuera las promociones y depende de un ajuste manual para septiembre, y es una causa posible del 7,8 % de líneas con quiebre de stock que se detecta en la preventa.

**Logística inversa.** La logística inversa gestiona el flujo de productos que vuelve desde el cliente, y una de sus decisiones centrales es el destino que se da a cada devolución (Agrawal et al., 2015). Elegir bien ese destino exige conocer la causa de la devolución. En Puelche las devoluciones equivalen al 2,9 % del volumen despachado; cada una puede volver a stock, venderse con descuento, devolverse al proveedor o destruirse, pero la decisión se toma producto por producto y no queda registrada de forma estructurada. La merma por vencimiento llega al 1,7 % del valor del inventario al año, y del parque estimado de 68.000 canastillos y 9.400 pallets se pierde el 14 % cada año, con los movimientos anotados en un cuaderno (Distribuidora Puelche S.A., 2026c, sección 4.8, p. 9).

**Modelos de atención al canal tradicional.** En la preventa, un vendedor toma el pedido y el camión lo entrega en un viaje posterior; en la autoventa, el camión lleva la mercadería y la venta y la entrega ocurren en la misma visita (Distribuidora Puelche S.A., 2026c, cap. C, p. 40). Boulaksil y Belkora (2017) compararon ambos modelos en la distribución a almacenes de barrio de Casablanca. La preventa necesita vendedores dedicados, pero el camión solo visita a quien hizo un pedido; la autoventa cobra y entrega en el acto, pero el camión recorre todos los locales, compren o no. Cuál conviene depende de la distancia entre los locales y de cuántas visitas terminan en pedido. La autoatención digital, en que el almacenero hace su propio pedido, también ahorra la visita, pero exige que el cliente tenga dispositivo y conexión. Puelche usa preventa, con 62 preventistas que visitan a cada cliente una vez por semana o cada quince días, mientras el competidor que llegó a Talca ofrece pedido autónomo y entrega en 24 horas (Distribuidora Puelche S.A., 2026c, cap. 1, p. 3, y sección 4.3, pp. 7–8). La autoatención no puede ser obligatoria, porque la mayoría de los almacenes no tiene internet y la restricción R-05 impide exigírselo.

Las ocho materias llevan a la misma conclusión que la sección 2.2.1: cada práctica de la industria depende de un dato que hoy Puelche no registra.

## 2.3 Dimensionamiento del problema

Esta sección cuantifica las brechas con las cifras del caso y analiza los seis procesos actuales donde se originan.

### 2.3.1 Cuantificación del impacto operacional y financiero

Para dimensionar la magnitud del desafío, la Tabla 2.1 reúne los indicadores de la situación actual (*AS-IS*) que el caso entrega para el ejercicio 2025, la referencia o meta asociada a cada uno y el efecto que producen en la operación.

**Tabla 2.1 — Brechas operacionales de Distribuidora Puelche S.A. Fuente: Distribuidora Puelche S.A. (2026c, cap. 7, tablas 7.1 a 7.3, pp. 11–12, y cap. 18, p. 34); las metas de merma y envases son propuestas por LafroX.**

| Indicador | Valor 2025 | Referencia o meta | Efecto en la operación |
| --- | ---: | --- | --- |
| OTIF | 82,4 % | sobre 95 % | 17,6 % de pedidos falla. |
| *Fill rate* | 91,3 % | sobre 97 % | Pedidos incompletos. |
| Quiebre de stock en preventa | 7,8 % de las líneas | bajo 2 % | Se promete producto agotado. |
| Reentregas | 4,2 % | bajo 1 % | Unas 59 reentregas diarias. |
| Guías extraviadas o ilegibles | 1,1 % mensual | cero | 12 días por reclamo. |
| Días para identificar un retiro | 9 días | menos de 2 horas | 6 meses de suspensión. |
| Recepciones sin lote (producto del retiro) | 41 % | 100 % con lote | Retiro reconstruido a mano. |
| Diferencias de rendición | $ 4,2 millones al mes | cuadra el mismo día | Diferencias sin investigar. |
| Diferencia de conteo cíclico | 2,3 % del valor contado | sin referencia | Descuadre contable y físico. |
| Merma por vencimiento | 1,7 % del inventario al año | hasta 1,0 % (LafroX) | Sin orden de vencimiento. |
| Pérdida de envases | 14 % al año | hasta 7 % (LafroX) | Sin control individual. |
| Ocupación del camión | 68 % | umbral por comprometer | Días de baja carga con 41 %. |

En la Tabla 2.1, la columna de referencia separa dos orígenes: los valores sin marca son referencias o resultados de aceptación que fija el caso, y los marcados «LafroX» son metas propias, porque el caso no las fija; el Subdocumento 3 las adopta como criterios de aceptación. La columna de efecto muestra que casi todas las brechas terminan en el servicio al cliente. Además, el caso cuantifica en dinero dos pérdidas por eventos: el retiro de marzo de 2026 y el rechazo de un camión completo por sospecha de ruptura de la cadena de frío. También registra diferencias de rendición mensuales, cuyas causas no se han investigado. Los dos eventos y las diferencias mensuales no corresponden al mismo período ni se suman. Las demás brechas se expresan como porcentajes sobre bases distintas:

- la merma, sobre el valor del inventario;

- el descuadre, sobre el valor contado;

- las reentregas, sobre las entregas;

- los envases, sobre el parque.

Por eso no se suman ni se comparan entre sí en dinero. Su efecto converge en la calidad del servicio, pero por vías distintas. Una reentrega o un faltante afectan el OTIF, porque el pedido no llega completo o dentro de la ventana. Una guía extraviada no afecta el OTIF si la entrega fue completa y a tiempo; afecta el pedido perfecto, que exige además documentación correcta (Anexo 2.2, S-01). Por esa razón, la brecha de servicio es la dimensión común del problema, medida con dos indicadores y no con una tasa única.

### 2.3.2 El enigma del cross-docking y los seis procesos AS-IS

Uno de los principales hallazgos del diagnóstico es el denominado **enigma del cross-docking**: la empresa invirtió en tres centros de transferencia con la promesa de reducir 24 horas del tiempo total de entrega, pero en la práctica solo logró una reducción neta de 8 horas. La brecha de 16 horas resulta de la diferencia entre ambos valores (24 − 8 = 16), pero las Bases señalan expresamente que su causa aún no se ha investigado.

La operación observada permite formular, sin anticipar una conclusión, la hipótesis de que la consolidación, la desconsolidación y la validación manual contribuyen a la brecha. Esta hipótesis debe validarse con mediciones de tiempos en Talca y en las tres plataformas antes de atribuir las 16 horas a un punto específico del proceso.

A continuación, se modelan y analizan los seis procesos críticos de la cadena logística actual (*AS-IS*) mediante diagramas de flujo que ilustran los puntos exactos de quiebre y pérdida de trazabilidad.

#### 2.3.2.1 Proceso 1: Preventa y Toma de Pedidos AS-IS

Como se aprecia en la Figura 2.1, el flujo comercial parte con el preventista visitando al cliente en terreno con una aplicación móvil desconectada que no posee visibilidad de stock ni del estado crediticio del comprador.

[Ver Figura 2.1](<figuras/figura 2.1.pdf>)

**Figura 2.1 Proceso de Preventa y Toma de Pedidos AS-IS. Fuente: elaboración a partir de Distribuidora Puelche S.A. (2026c, secciones 4.3 y 7.1, pp. 7–8 y 11).**

1. El preventista visita presencialmente al cliente; participan 62 preventistas.

2. Captura el pedido en una aplicación móvil desconectada, sin visibilidad de stock ni crédito.

3. Transmite el pedido cuando el dispositivo recupera cobertura; en zonas sin señal, el envío se retrasa hasta encontrarla. La ventana de 17:00 a 20:00 corresponde al regreso y sincronización de la flota, no a la preventa.

4. El proceso consulta si existe stock disponible y crédito aprobado.

5. Si la respuesta es afirmativa, el pedido ingresa formalmente a la cola de procesamiento del ERP.

6. Si la respuesta es negativa, se distinguen dos motivos que pueden coincidir: falta de stock, que produce pedidos incompletos o ventas perdidas y cuyo quiebre afecta al 7,8 % de las líneas; o bloqueo por crédito, que deja el pedido retenido en el ERP para revisión por Crédito y Cobranza al día siguiente.

La Figura 2.1 muestra que la falla no nace en el ERP, sino antes. El preventista promete sin ver stock ni crédito, y el error recién aparece cuando el pedido llega al sistema. El quiebre se detecta en la preventa, pero lo sufre el cliente en la entrega, porque recibe menos de lo pedido. Hoy no se registra cuántos pedidos quedan retenidos por crédito ni cuánto esperan; es un dato que habrá que medir.

#### 2.3.2.2 Proceso 2: Recepción de Mercadería y Control de Lotes AS-IS

En la Figura 2.2 se ilustra el registro de recepciones en los muelles de los centros de distribución al descargar los envíos de los 180 proveedores.

1. Arriba un camión al muelle del centro de distribución; la operación se relaciona con 180 proveedores.

2. Se descargan y cuentan físicamente los bultos en el andén.

3. La recepción se registra manualmente en una planilla física o guía en papel.

4. El proceso consulta si lote y vencimiento fueron digitados en el sistema.

5. Si la respuesta es afirmativa, la mercadería queda con lote registrado.

6. Si la respuesta es negativa, queda comprometida la trazabilidad sanitaria; 41 % de las recepciones del producto involucrado en el retiro no tenía lote registrado.

[Ver Figura 2.2](<figuras/figura 2.2.pdf>)

**Figura 2.2 Proceso de Recepción de Mercadería y Control de Lotes AS-IS. Fuente: elaboración a partir de Distribuidora Puelche S.A. (2026c, secciones 2.2 y 4.1, pp. 4 y 7).**

En la Figura 2.2 se ve que el lote se pierde en el paso 3, en el andén, y ningún paso posterior lo recupera: bodega, preparación y despacho mueven la mercadería sin saber de qué lote es. Por eso el retiro de marzo tomó 9 días: hubo que reconstruir con papeles y memoria lo que nunca se registró al recibir. El 41 % corresponde solo al producto del retiro; cuánto falta en las demás recepciones se desconoce (Anexo 2.2, SP-03) y es lo primero que conviene medir.

#### 2.3.2.3 Proceso 3: Preparación de Pedidos y Cross-Docking AS-IS

La operación de las tres plataformas de cross-docking (Curicó, Chillán y Los Ángeles) se detalla en la Figura 2.3, según la descripción del caso.

[Ver Figura 2.3](<figuras/figura 2.3.pdf>)

**Figura 2.3 Proceso de Preparación y Cross-Docking AS-IS. Fuente: elaboración a partir de Distribuidora Puelche S.A. (2026c, cap. 3, p. 6).**

1. En Talca se consolida la carga de cada plataforma en el camión de línea.

2. El camión de línea llega a la plataforma en la madrugada.

3. La carga se desconsolida en una ventana de operación de tres horas, sin almacenamiento y con personal reducido.

4. La carga se despacha en la mañana en los camiones de reparto.

Las plataformas operan con conectividad únicamente por red móvil y sin control de inventario (Distribuidora Puelche S.A., 2026c, cap. 6, pp. 10–11, y sección 4.2, p. 7).

La Figura 2.3 tiene cuatro tramos, pero ninguno deja hora registrada: no se sabe cuándo sale el camión de Talca, cuándo llega a la plataforma ni cuánto dura la desconsolidación. Sin esas marcas, las 16 horas no se pueden repartir entre consolidación, viaje, espera o descarga. La compañía sospecha de la consolidación en Talca, pero no hay datos que lo confirmen ni que lo desmientan, así que se trata como hipótesis (Anexo 2.2, SP-02) hasta medir cada tramo.

#### 2.3.2.4 Proceso 4: Planificación de Rutas AS-IS

El proceso de diagramación de despachos y asignación de vehículos se ilustra en la Figura 2.4.

1. Los pedidos confirmados quedan disponibles para planificación entre las 15:00 y las 18:30 horas.

2. Los datos se exportan manualmente a planillas Excel, sin interfaz directa.

3. Las rutas se diagraman manualmente con el conocimiento tácito del planificador.

4. Se imprimen las hojas de ruta y guías para la tripulación.

5. El despacho opera con rutas rígidas y subóptimas y alcanza 68 % de ocupación.

[Ver Figura 2.4](<figuras/figura 2.4.pdf>)

**Figura 2.4 Proceso de Planificación de Rutas AS-IS. Fuente: elaboración a partir de Distribuidora Puelche S.A. (2026c, secciones 4.4 y 4.6, p. 8).**

El cuello de botella de la Figura 2.4 es una persona. El planificador tarda 3,5 horas diarias en armar las rutas con una planilla de once hojas que solo él entiende, y cuando sale de vacaciones el cumplimiento de entrega cae entre seis y nueve puntos (Distribuidora Puelche S.A., 2026c, sección 4.4, p. 8). La ocupación de 68 %, que baja a 41 % en los días de menor carga, se explica porque el método manual no permite probar alternativas, no por falta de esfuerzo. Si se jubila sin dejar sus reglas por escrito, ese conocimiento se va con él.

#### 2.3.2.5 Proceso 5: Reparto y Entrega AS-IS

La interacción en la última milla entre los camiones de reparto y los puntos de destino se presenta en la Figura 2.5.

1. El camión sale a ruta durante la ventana de despacho de 05:30 a 07:00 horas.

2. Arriba al local comercial, ya sea almacén o cliente de food service.

3. El proceso consulta si el local está abierto y el cliente está conforme.

4. Si la respuesta es afirmativa, el cliente firma físicamente la guía de despacho.

5. Si el local está cerrado, el conductor decide si vuelve más tarde, deja el pedido con el negocio vecino o se lo lleva de vuelta; no existe una regla escrita. Si el cliente rechaza un producto, el conductor lo anota en la guía y se lo lleva de vuelta.

[Ver Figura 2.5](<figuras/figura 2.5.pdf>)

**Figura 2.5 Proceso de Reparto y Entrega AS-IS. Fuente: elaboración a partir de Distribuidora Puelche S.A. (2026c, sección 4.6, pp. 8–9).**

En la Figura 2.5, la entrega es donde se cierran o se rompen los procesos anteriores. Como no hay regla escrita para el local cerrado, cada conductor resuelve a su manera y la reentrega no queda registrada con su causa. El retorno de mercadería tampoco equivale siempre a una reentrega. La única prueba de entrega es la guía firmada en papel: si se pierde (1,1 % al mes), aclarar un reclamo toma en promedio 12 días.

La tasa de reentregas es del 4,2 % sobre el total de entregas (Distribuidora Puelche S.A., 2026c, cap. 7, tabla 7.1, p. 11). Aplicada a las aproximadamente 1.400 entregas de un día hábil normal, equivale a unas 59 reentregas diarias (1.400 × 0,042 = 58,8). Esta estimación está condicionada al supuesto SP-01 del Anexo 2.2, que requiere validar la aplicación de la tasa al volumen diario y la correspondencia de cada reentrega con una entrega. La cifra no representa la cantidad de retornos de mercancía al centro de distribución.

#### 2.3.2.6 Proceso 6: Rendición y Cobranza AS-IS

Por último, la liquidación de valores cobrados en efectivo se esquematiza en la Figura 2.6.

[Ver Figura 2.6](<figuras/figura 2.6.pdf>)

**Figura 2.6 Proceso de Rendición y Cobranza AS-IS. Fuente: elaboración a partir de Distribuidora Puelche S.A. (2026c, sección 4.7, p. 9).**

1. Se cobra en efectivo contra entrega; el 38 % de las ventas del canal tradicional se cobra así y el resto se factura a 30 días.

2. El conductor conserva el dinero hasta su regreso.

3. La rendición se realiza a la mañana siguiente en caja, contando el dinero contra el listado de entregas del día anterior.

4. La caja consulta si el dinero contado coincide con el listado de entregas al contado del día anterior.

5. Si coincide, se registra sin inconvenientes.

6. Si la respuesta es negativa, quedan diferencias no conciliadas y no es posible rastrear el descuadre por entrega.

La Figura 2.6 muestra un desfase: el descuadre ocurre en la calle, pero se descubre a la mañana siguiente en la caja, cuando ya no se sabe en qué entrega se produjo. Por eso los $ 4,2 millones mensuales de diferencia siguen sin investigar. El problema no es que falte control en la caja, sino que el cobro no queda unido a su entrega en el momento en que ocurre.

Leídos juntos, los seis procesos repiten un mismo patrón: el dato nace en terreno, se anota en papel o queda en la memoria de alguien, y se reconstruye después, cuando ya no se puede verificar. Así se pierden el lote en la recepción, la causa del faltante en la preventa, la evidencia en la guía y el origen del descuadre en la rendición. Cada pérdida afecta al proceso siguiente, y por eso los tres problemas de la sección 2.2.1 aparecen juntos.

## 2.4 Actores y Grupos de Interés

El éxito del proyecto depende de alinear a los 19 actores que conforman el ecosistema de Distribuidora Puelche S.A. Cada uno posee incentivos, niveles de poder y resistencias particulares frente a la automatización de procesos.

La Tabla 2.2 ubica a los 19 actores en una matriz de influencia e interés, con los niveles que les asigna el Anexo 2.3.

**Tabla 2.2 — Matriz de influencia e interés de los 19 actores. Fuente: elaboración a partir de Distribuidora Puelche S.A. (2026c, caps. 2 y 8, pp. 4–5 y 13–17) y del Anexo 2.3.**

| Influencia | Interés alto | Interés muy alto |
| --- | --- | --- |
| **Muy alta** | Canal tradicional, *food service* y canal moderno | Gerenta general, gerente comercial y gerente de finanzas |
| **Alta** | Preventistas, tripulación propia y peonetas, conductores externos, preparadores y sindicato de choferes | Gerente de operaciones, jefa de calidad, jefa de bodega, jefe de TI y planificador de rutas |
| **Media** | Empresas transportistas, proveedores y autoridad sanitaria | — |

La influencia indica cuánto puede cambiar un actor el resultado del proyecto. Es muy alta en quien decide las prioridades o la venta de la empresa, alta en quien hace el trabajo que el proyecto cambia y media en quien impone condiciones desde fuera, sin participar en la operación diaria. El interés indica cuánto cambia el proyecto el trabajo de cada actor: es muy alto en quien responde por un resultado que el proyecto modifica, y alto en quien ve cambiar su trabajo diario o su relación con Puelche. Ningún actor tiene interés bajo, porque el proyecto toca a los 19, y por eso la matriz no tiene esa columna.

Cada celda pide una gestión distinta. La dirección decide: arbitra las prioridades y aprueba el avance. Las jefaturas aportan las reglas que hoy no están escritas, como el criterio térmico, la ubicación en bodega o las rutas, y por eso participan desde el levantamiento. Los clientes no forman parte del proyecto, pero su reacción define la venta; se les informa lo que cambia en la entrega, sin exigirles nada nuevo. El personal de terreno se consulta y se capacita, porque sin su cooperación la operación no cambia aunque el sistema funcione. Con proveedores, transportistas y autoridad sanitaria bastan la información oportuna y los acuerdos formales. La celda vacía muestra que ningún actor externo depende del proyecto tanto como las jefaturas.

El mayor riesgo de resistencia está en el personal de terreno: el sindicato ya objetó las cámaras en cabina y el uso del GPS para controlar la jornada, y el planificador concentra un conocimiento que nadie más tiene. El catálogo nominal de los 19 actores, con su estrategia de participación, está en el Anexo 2.3, y el Subdocumento 3 desarrolla cómo se obtiene su apoyo.

## 2.5 Resumen de Requerimientos, Supuestos, Exclusiones y Restricciones

Esta sección resume lo que el CLIENTE requiere, los supuestos que formula LafroX y las exclusiones y restricciones del caso; el detalle está en los Anexos 2.1 a 2.3.

### 2.5.1 Resumen y análisis de requerimientos del cliente

A partir del análisis del problema y de las entrevistas del caso (Distribuidora Puelche S.A., 2026c, cap. 8, pp. 13–17), el cliente exige una solución que satisfaga un catálogo integral de requerimientos funcionales y no funcionales. Los principales ejes funcionales demandados abarcan:

- **Preventa y comercialización:** El preventista necesita conocer stock y crédito al tomar el pedido y seguir trabajando un turno completo sin señal, sin que ningún pedido se pierda ni se duplique.

- **Gestión de bodegas y trazabilidad de lotes:** Todo producto que lo requiera debe quedar con lote y vencimiento desde su recepción, salir en orden de vencimiento, también en la cámara a −22 °C, y permitir identificar a los clientes afectados por un lote en menos de 2 horas.

- **Despacho y última milla:** Rutas que respeten la promesa segmentada y las ventanas de servicio, evidencia de cada entrega disponible el mismo día y acuse de recibo válido de la Guía de Despacho Electrónica.

- **Conciliación financiera:** Cada cobro en efectivo debe quedar asociado a su entrega, y toda diferencia de rendición debe explicarse el mismo día con causal y responsable.

A estos ejes se suman condiciones no funcionales de las Bases Técnicas Transversales, como la disponibilidad mensual de 99,95 % por componente de infraestructura y de 99,9 % para la transacción de negocio de extremo a extremo (Distribuidora Puelche S.A., 2026b, cap. 7, sección 7.2, pp. 17–18). El catálogo completo y priorizado de requerimientos funcionales y no funcionales se detalla en el Anexo 2.1.

### 2.5.2 Supuestos de ingeniería formulados por LafroX

LafroX formula sus propios supuestos de ingeniería y los separa de las restricciones que imponen las Bases. El Anexo 2.2 reúne los que se refieren al problema: S-01 a S-16 y los tres supuestos del diagnóstico (SP-01 a SP-03), cada uno con su fundamento, su impacto y la forma de validarlo.

Los supuestos que dependen de la solución están en los subdocumentos que la desarrollan. El Anexo 3.C del Subdocumento 3 continúa la numeración con S-17 a S-44. Dos de ellos condicionan la integración: S-18 supone que las interfaces del ERP existen y pueden usarse sin modificarlo, y S-19, que se podrá acceder a los datos de telemetría del proveedor actual. Los supuestos de volumen, concurrencia y crecimiento (SV-01 a SV-07) están en el Anexo 4-W del Subdocumento 4; por ejemplo, que cada pedido genera una entrega y que septiembre es el mes de mayor exigencia.

### 2.5.3 Exclusiones y restricciones no negociables

Complementariamente, la Tabla 2.3 sintetiza cinco de las doce restricciones del caso, con los mismos códigos del Anexo 2.2. La inmutabilidad del canal tradicional y la prohibición de intervenir sistemas del 1 al 25 de septiembre, durante todo diciembre y en los tres primeros días hábiles de cada mes condicionan la propuesta de dos formas. Obligan a que la operación de terreno no dependa del sistema central. También obligan a programar despliegues y pasos a producción fuera de esos períodos (Distribuidora Puelche S.A., 2026c, cap. 10, pp. 19–20, y sección 13.3, p. 23). El inventario íntegro de exclusiones y restricciones se encuentra en el Anexo 2.2.

**Tabla 2.3 — Síntesis de restricciones no negociables del caso. Fuente: Distribuidora Puelche S.A. (2026c, cap. 10, pp. 19–20); detalle en el Anexo 2.2.**

| Código | Restricción | Condición que impone |
| --- | --- | --- |
| R-04 | ERP como registro contable único | El ERP no se sustituye y sigue siendo el único emisor de documentos tributarios. |
| R-05 | Canal tradicional sin cambios | A los 11.600 almacenes no se les exige internet, dispositivo propio ni pago electrónico. |
| R-08 | Ventanas de congelamiento | No se interviene del 1 al 25 de septiembre, en diciembre ni en los tres primeros días hábiles de cada mes. |
| R-10 | Privacidad laboral | El sindicato objetó las cámaras en cabina y el control de jornada por GPS. |
| R-12 | Validez de los documentos tributarios | La guía de despacho electrónica y su acuse tienen efectos legales que no se pueden comprometer. |

Las cinco restricciones de la Tabla 2.3 limitan la propuesta en tres planos. En terreno, R-05 y R-10 exigen generar la evidencia de entrega y cobro con recursos de Puelche y respetar los límites al uso de cámaras y GPS. En la integración, R-04 y R-12 mantienen al ERP como emisor de documentos tributarios. En el calendario, R-08 condiciona las intervenciones y los pasos a producción a las ventanas permitidas.

## Referencias

Las fuentes citadas en este documento se listan a continuación en formato APA 7.ª edición.

- Agrawal, S., Singh, R. K., y Murtaza, Q. (2015). A literature review and perspectives in reverse logistics. *Resources, Conservation and Recycling, 97*, 76–92. https://doi.org/10.1016/j.resconrec.2015.02.009

- Boulaksil, Y., y Belkora, M. J. (2017). Distribution strategies toward nanostores in emerging markets: The Valencia case. *Interfaces, 47*(6), 505–517. https://doi.org/10.1287/inte.2017.0914

- Chopra, S., y Meindl, P. (2016). *Supply chain management: Strategy, planning, and operation* (6.ª ed.). Pearson.

- Distribuidora Puelche S.A. (2026a). *Bases Administrativas de Licitación N° TFEP-01/2026: Contratación de Solución Integral de Software y Servicios de Operación*.

- Distribuidora Puelche S.A. (2026b). *Bases Técnicas Transversales de Licitación N° TFEP-01/2026*.

- Distribuidora Puelche S.A. (2026c). *Bases Técnicas – Logística: trazabilidad, promesa de entrega y costo de servir en una distribuidora de consumo masivo*.

- Fildes, R., Ma, S., y Kolassa, S. (2022). Retail forecasting: Research and practice. *International Journal of Forecasting, 38*(4), 1283–1318. https://doi.org/10.1016/j.ijforecast.2019.06.004

- GS1. (2016). *EANCOM® 2002 S4: Part I* (Edition 2016). https://gs1.org/sites/gs1/files/docs/eancom/ean02s4/part1/part1toc.htm

- GS1 Chile. (s. f.-a). *Comparte: transferencia de información crítica para el intercambio comercial*. Recuperado el 11 de octubre de 2026, de https://gs1chile.org/Estandares/comparte

- GS1 Chile. (s. f.-b). *Identifica: claves de identificación*. Recuperado el 11 de octubre de 2026, de https://gs1chile.org/Estandares/identifica

- GS1 Chile. (s. f.-c). *Servicios: comunicación para transacciones electrónicas (EDI – Comercionet)*. Recuperado el 11 de octubre de 2026, de https://gs1chile.org/Servicio/Detalle-de-Servicios

- Guerreiro, R., Bio, S. R., y Merschmann, E. V. V. (2008). Cost-to-serve measurement and customer profitability analysis. *The International Journal of Logistics Management, 19*(3), 389–407. https://doi.org/10.1108/09574090810919215

- de Koster, R., Le-Duc, T., y Roodbergen, K. J. (2007). Design and control of warehouse order picking: A literature review. *European Journal of Operational Research, 182*(2), 481–501. https://doi.org/10.1016/j.ejor.2006.07.009

- Ley N.º 21.719. (2024, 13 de diciembre). *Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales*. Diario Oficial de la República de Chile. https://www.bcn.cl/leychile/navegar?idNorma=1209272

- Mercier, S., Villeneuve, S., Mondor, M., y Uysal, I. (2017). Time–temperature management along the food cold chain: A review of recent developments. *Comprehensive Reviews in Food Science and Food Safety, 16*(4), 647–667. https://doi.org/10.1111/1541-4337.12269

- Ministerio de Salud. (1996). *Decreto Supremo N° 977: Aprueba Reglamento Sanitario de los Alimentos*. Diario Oficial de la República de Chile.

- Ministerio del Trabajo y Previsión Social. (2002). *Código del Trabajo de la República de Chile: Artículo 25 bis sobre jornada especial de transporte de carga*. Edición oficial.

- Moberg, D., y Drummond, R. (2005). *MIME-based secure peer-to-peer business data interchange using HTTP, Applicability Statement 2 (AS2)* (RFC 4130). Internet Engineering Task Force. https://www.rfc-editor.org/rfc/rfc4130

- Servicio de Impuestos Internos. (2024). *Manual de Procedimientos y Requisitos de Documentos Tributarios Electrónicos (DTE)*. SII Chile.

- Toth, P., y Vigo, D. (Eds.). (2014). *Vehicle routing: Problems, methods, and applications* (2.ª ed.). Society for Industrial and Applied Mathematics.

- Vidal, T., Laporte, G., y Matl, P. (2020). A concise guide to existing and emerging vehicle routing problem variants. *European Journal of Operational Research, 286*(2), 401–416. https://doi.org/10.1016/j.ejor.2019.10.010

## Declaración de uso de IA

La Tabla 2.4 declara el uso asistido de herramientas de inteligencia artificial en la elaboración del presente subdocumento y de sus anexos.

**Tabla 2.4 Declaración de uso de IA por sección del Subdocumento 2. Fuente: registro del equipo.**

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
| --- | --- | --- | --- | --- | --- |
| 2.1 Resumen Ejec. | Claude / Gemini | Síntesis ejecutiva y estilo formal | Alto | Medio | Alex Aravena: revisión del resumen y validación de la propuesta de valor. |
| 2.2 Comprensión | Claude / Gemini | Estructuración de los 3 problemas | Alto | Medio | Alex Aravena: revisión de los tres problemas frente al caso. |
| 2.3 Dimensionamiento | Claude / Gemini | Descripción estructurada de los 6 flujos AS-IS | Alto | Medio | Alex Aravena: revisión de los flujos y validación de los cálculos. |
| 2.4 Actores | Claude / Gemini | Disposición tabular de actores | Alto | Medio | Alex Aravena: validación de los actores frente al catálogo. |
| 2.5 Requerimientos | Claude / Gemini | Formato y redacción de supuestos | Alto | Medio | Alex Aravena: revisión de supuestos y restricciones. |
| Anexo 2.1 | Claude / Gemini | Maquetación del listado de requerimientos | Alto | Medio | Alex Aravena: validación del listado frente al catálogo. |
| Anexo 2.2 | Claude / Gemini / Codex | Consolidación de decisiones, exclusiones y restricciones; alineación de S-09 con el precio registrado y el control de diferencias con el ERP | Alto | Medio | Alex Aravena: revisión frente a los capítulos 10, 11 y 16.1 del caso y validación de S-09. |
| Anexo 2.3 | Claude / Gemini | Maquetación de actores y sistemas legados | Alto | Medio | Alex Aravena: revisión de actores, cifras y sistemas. |

La Tabla 2.4 muestra que la IA se usó con nivel alto en el texto y medio en los diagramas de todas las secciones, y que cada sección fue revisada por un integrante del equipo.
