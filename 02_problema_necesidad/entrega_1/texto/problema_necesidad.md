# Capítulo 2 · Problema y Necesidad (Subdoc. 2)


## 2.1 Contextualización del Entorno

La Distribuidora Puelche S.A. (en adelante, "Puelche" o "la Distribuidora") es una empresa familiar que fue fundada en 1974; actualmente, tiene a cargo a su tercera generación de dirección. Su especialidad es la distribución mayorista de consumo masivo (alimentos, bebidas, aseo del hogar y cuidado personal) en cinco regiones del centro-sur de Chile, desde La Araucanía hasta O'Higgins. La empresa opera desde dos centros de distribución principalmente: el primero, en Talca, abarca 18.000 metros cuadrados, mientras que el segundo en Concepción, 9.000 metros cuadrados; por otro lado, tienen tres plataformas de cross-docking en Curicó, Chillán y Los Ángeles. Más importante aún, tienen de forma activa 14.200 clientes, distribuidos en su mayoría entre almacenes y minimarkets del canal tradicional (11.600 clientes), restaurantes y casinos del segmento food service (2.100) y cadenas de supermercados regionales, sumando hasta 500 puntos de entrega en este sector. Solo en 2025, la compañía procesó 31.000 pedidos mensuales, movilizó 2,4 millones de unidades y emitió cerca de 34.000 documentos tributarios, todo ello con ventas anuales de $148.000 millones. Su dotación propia alcanza las 640 personas, complementada por, aproximadamente, 160 conductores, los cuales pertenecen a 10 empresas transportistas externas.

El 3 de marzo de 2026, el gerente de aseguramiento de calidad de uno de los principales proveedores de lácteos del país notificó a la Distribuidora Puelche la necesidad de ejecutar un retiro preventivo por desviación detectada en un lote identificado como 24-0217 de queso fresco, conforme a los procedimientos de retiro de producto establecidos en el Reglamento Sanitario de los Alimentos (Ministerio de Salud, 1996). La respuesta esperada era identificar, en el menor tiempo posible, a cuáles clientes había llegado dicho lote, la cantidad y la documentación que traía. La jefa tardó nueve días en responder y, para peor, no fue exacta, sino una estimación, ni siquiera certera. Al prácticamente ser imposible saber los puntos de entrega afectados, la empresa debió retirar de forma total, sobre los 14.200 clientes, dicho producto. La pérdida financiera de esta medida fue fatal: $31.000.000 en pérdidas directas producto del retiro, 4.800 kilogramos de queso fresco, un sumario sanitario abierto por la autoridad y una suspensión como distribuidor autorizado por el proveedor por seis meses, equivalente al 6 % de las ventas totales. Este evento expuso, con datos empíricos, una realidad que se intuía pero que no habían cuantificado: no tienen trazabilidad. El registro de lote de un producto existente, en el mejor de los casos, solo lleva una planilla impresa archivada en una carpeta, y, según la distribuidora, alrededor del 41 % de los casos no existe en absoluto esta planilla. No tienen ningún sistema operativo que permita responder en tiempo real a dónde fue a parar un producto específico.

El retiro sanitario no fue el único problema al que se enfrentó el comité ejecutivo en el primer trimestre de 2026. De forma paralela, se crearon dos presiones externas que transformaron una crisis puntual en una amenaza estratégica de largo plazo.

La primera es la irrupción de un distribuidor nacional que abrió operación en Talca ocho meses antes. Este competidor ofrece entregas en 24 horas y dispone de una aplicación móvil donde el almacenero realiza su pedido de forma completamente autónoma, consulta el stock disponible en la distribuidora y sabe, de forma aproximada, la llegada del camión. Para contrastar, Puelche entrega entre 48 a 72 horas y toma el pedido mediante un preventista que visita al cliente una vez por semana. La principal diferencia es que ellos sí poseen la información disponible en el momento correcto.

La segunda es que el cliente más importante de la compañía, una cadena de supermercados que representa el 11 % de la venta, notificó sus condiciones comerciales para el período que comienza en enero de 2029:

Pedidos exclusivamente por vía electrónica estructurada.

Aviso de despacho anticipado.

Ventana de entrega de treinta minutos con penalización por incumplimiento.

Prueba de entrega digital obligatoria.

Hoy, la Distribuidora Puelche no cumple con ninguna de estas condiciones: la ventana de entrega actual es de 10 horas entre las 8:00 y 18:00 horas, los pedidos no se reciben por ninguna vía electrónica y la prueba de entrega es una guía de papel firmada a mano.

Estas tres presiones llevaron al comité ejecutivo a convocar una licitación para desarrollar e implementar una solución integral de gestión logística, donde las metas son:

Entregas completas y a tiempo de 82,4 % a tener más del 95 %.

Cumplimiento de lo pedido de 91,3 % a tener más del 97 %.

Plazos de entrega de 48–72 horas a 24 horas.

Ventana de entrega comprometida disminuida hasta 30 minutos para 2029.

Tiempo de respuesta para responder un retiro sanitario de horas, con evidencia exacta.

Registro continuo y automático de temperatura en cadena de frío.

Costo de servir por cliente calculado por entrega.

Pedidos recibidos mediante vía electrónica estructurada.


## 2.2 Marco Legal y Regulatorio

El diseño, la construcción y la operación de la plataforma digital de misión crítica para la Distribuidora Puelche S.A. se encuentran condicionados por un entramado normativo nacional e internacional cuyo cumplimiento no constituye una formalidad declarativa, sino un conjunto de restricciones técnicas que inciden directamente en la arquitectura de la solución, en sus controles de seguridad, en la estructura de datos y en los flujos de integración con sistemas externos (Ministerio del Interior y Seguridad Pública, 2017, 2023, 2024; Ministerio de Salud, 1996). A continuación, se detalla el impacto técnico de cada cuerpo normativo relevante y los estándares internacionales cuya adherencia resulta exigible.


### 2.2.1 Marco Legal Nacional

Ley N° 21.719 sobre Protección de Datos Personales y Ley N° 19.628. La operación de Puelche involucra el tratamiento de datos personales de 14.200 clientes (Ministerio del Interior y Seguridad Pública, 2024). —en su mayoría personas naturales del canal tradicional—, datos comerciales sensibles como el comportamiento de pago y el historial crediticio, así como datos de geolocalización continua de 62 preventistas y aproximadamente 200 conductores. La Ley N° 21.719 establece la institucionalidad de la Agencia de Protección de Datos Personales e impone obligaciones de base de licitud, proporcionalidad, minimización y seguridad en el tratamiento. Técnicamente, esto exige que la solución implemente un modelo de control de acceso basado en roles (RBAC) complementado con control basado en atributos (ABAC) para garantizar que cada perfil acceda exclusivamente a los datos que su función requiere —por ejemplo, un preventista no debe visualizar el comportamiento de pago agregado de la cartera, sino únicamente el crédito disponible del cliente que visita—. Adicionalmente, los datos de categoría sensible identificados en el caso (comportamiento de pago, antecedentes comerciales, geolocalización de personas) deberán cifrarse a nivel de campo con algoritmo AES-256, de modo que el acceso a la base de datos no revele su contenido en texto claro, conforme al requisito RT-11.10 de las Bases Técnicas Transversales. La solución deberá mantener un registro de actividades de tratamiento, implementar mecanismos de anonimización y seudonimización verificables para ambientes no productivos (RT-11.25) y garantizar la residencia de los datos conforme a lo que el CLIENTE apruebe, con salvaguardas documentadas para toda transferencia internacional.

Ley N° 21.663, Ley Marco de Ciberseguridad e Infraestructura Crítica de la Información. Si bien Puelche no ha sido catalogada como operador de importancia vital (Ministerio del Interior y Seguridad Pública, 2023), la naturaleza de su operación —distribución de alimentos perecibles con cadena de frío regulada sanitariamente— la sitúa en una posición donde un incidente de ciberseguridad podría comprometer la inocuidad alimentaria de cinco regiones. La Ley N° 21.663 y las instrucciones de la Agencia Nacional de Ciberseguridad establecen estándares mínimos de protección que, en el contexto de esta licitación, se materializan en la adopción del modelo Zero Trust (NIST SP 800-207), la implementación de un centro de operaciones de seguridad (SOC) con cobertura 24×7, y la obligación de notificar al CLIENTE toda brecha de seguridad dentro de las 24 horas de su detección. Arquitectónicamente, la solución deberá segmentar las redes por capas, impedir el acceso directo desde Internet a cualquier componente de datos y verificar explícitamente cada solicitud, sin presuponer la confiabilidad de ninguna red, dispositivo o identidad.

Ley N° 21.459 sobre Delitos Informáticos. Esta ley tipifica conductas como el acceso ilícito a sistemas, la interceptación de datos y el fraude informático, y establece la responsabilidad de los responsables del tratamiento cuando sus medidas de seguridad resulten insuficientes. Para la solución propuesta, su impacto técnico se traduce en la obligatoriedad de pistas de auditoría inalterables (requisito RT-16.07): todo registro de auditoría deberá almacenarse en formato inmodificable, sin que ningún perfil —incluido el administrador de la plataforma— pueda eliminarlo o alterarlo. El registro deberá capturar quién ejecutó cada operación, desde qué dispositivo, en qué fecha y hora con zona horaria, y con qué valores anteriores y posteriores (RT-16.06). Complementariamente, la capa de borde de la solución deberá incorporar un cortafuegos de aplicaciones web (WAF) con reglas gestionadas y personalizadas, protección contra denegación de servicio distribuida en capas 3, 4 y 7 (RT-11.07), y correlación de eventos de seguridad en una plataforma SIEM con casos de uso de detección específicos para el proceso logístico del caso, y no únicamente genéricos de infraestructura (RT-11.15).

Ley N° 19.799 sobre Documentos Electrónicos y Firma Electrónica. La prueba de entrega digital constituye uno de los ejes centrales de la solución y debe articularse con la guía de despacho electrónica y su acuse de recibo conforme a la normativa tributaria vigente. La Ley N° 19.799 otorga validez jurídica a los documentos firmados electrónicamente y establece las condiciones para su equivalencia funcional con los documentos en soporte papel. Para el caso de Puelche, donde el receptor habitual es una persona natural sin firma electrónica avanzada, la solución deberá investigar y proponer un mecanismo que combine la captura biométrica (firma en dispositivo), la fotografía georreferenciada con marca de tiempo y la generación del sello de tiempo correspondiente, conservando la evidencia de firma que permita verificar el documento con posterioridad, conforme al requisito RT-16.18 de las Bases Técnicas Transversales.

Ley N° 17.336 sobre Propiedad Intelectual. La solución objeto de esta licitación involucra la construcción de software aplicativo, la integración de componentes de terceros y el uso de bibliotecas de código abierto. La Ley N° 17.336 protege los derechos de autor sobre programas computacionales y bases de datos, lo cual exige que la propuesta declare un proceso formal de aprobación de nuevas dependencias de terceros (RT-11.26), mantenga un inventario actualizado de componentes de software (SBOM) en formato Cyclone DX o SPDX por cada versión liberada (RT-11.23), y garantice que todo licenciamiento de software de base, de plataforma y de terceros se encuentre a nombre del CLIENTE durante la totalidad del período contractual. La cadena de suministro de software deberá cumplir con SLSA nivel 3 o superior, con firma de artefactos y verificación de procedencia (RT-11.24), asegurando la integridad y la trazabilidad de cada componente incorporado a la solución.

Ley N° 20.393 sobre Responsabilidad Penal de las Personas Jurídicas y Ley N° 21.595 de Delitos Económicos. La relevancia de este cuerpo normativo es particularmente aguda en el caso de Puelche por el manejo de efectivo en ruta —38 % de las ventas del canal tradicional se cobra al contado, con diferencias de rendición que promedian $4,2 millones mensuales sin investigación de causa— y por los controles internos asociados a la aprobación de transacciones financieras. La solución deberá implementar un mecanismo de aprobación dual para transacciones de alto riesgo: todo cambio de parámetro con impacto operacional requerirá la autorización de un segundo perfil (RT-16.03), toda elevación de privilegios será temporal, aprobada y grabada (RT-12.06), y la rendición de efectivo deberá registrarse en el momento del cobro —no al día siguiente— con conciliación automatizada que identifique y clasifique las discrepancias en tiempo real. Este diseño contribuye directamente al modelo de prevención de delitos que la Ley N° 20.393 exige a las personas jurídicas.

Reglamento Sanitario de los Alimentos y Normativa de Trazabilidad. El sumario sanitario abierto en marzo de 2026 evidenció la ausencia estructural de trazabilidad en la operación de Puelche (Ministerio de Salud, 1996). El Reglamento Sanitario obliga a mantener condiciones de almacenamiento controladas, registro continuo de temperatura en la cadena de frío y capacidad de ejecutar un retiro de producto con identificación precisa de los lotes y los destinatarios afectados. Técnicamente, la solución deberá implementar un modelo de trazabilidad lote-a-lote desde la recepción hasta el punto de entrega, integrado con los estándares GS1 de identificación de productos (GTIN), unidades logísticas (SSCC) y ubicaciones (GLN) (GS1, 2020), y con captura automatizada de temperatura mediante sensores IoT en cámaras y vehículos, con transmisión continua y alerta ante excursiones fuera de rango.

Normativa Tributaria: Documentos Tributarios Electrónicos. La guía de despacho electrónica es obligatoria y su acuse de recibo tiene efectos legales que la solución no puede comprometer (Restricción no negociable N° 12) (Servicio de Impuestos Internos, 2024). La solución no emitirá documentos tributarios —esa función permanece en el sistema de gestión empresarial—, pero deberá integrarse bidireccionalmente con él para garantizar la consistencia entre la información operativa y la contable-tributaria, respetando el principio de que no habrá dos verdades contables (Restricción no negociable N° 4).


### 2.2.2 Estándares Internacionales y Marcos de Referencia

ISO/IEC 27001 e ISO/IEC 27002 — Seguridad de la Información. Constituyen el estándar exigido para el sistema de gestión de seguridad de la información del adjudicatario (International Organization for Standardization, 2022). La solución deberá mantener una matriz de controles de seguridad trazable a estos estándares, indicando el control, su implementación concreta en la solución y la evidencia que lo acredita (RT-11.05). La certificación ISO/IEC 27001 es obligatoria, vigente a la fecha de la oferta o con plan de certificación dentro de los primeros 12 meses del contrato.

ISO/IEC 27017 e ISO/IEC 27018 — Seguridad y Datos Personales en Nube. Dada la naturaleza híbrida obligatoria de la solución, estos estándares aplican a todos los componentes desplegados en nube pública, con controles específicos para la segregación de datos entre inquilinos, la transparencia sobre la ubicación del procesamiento y la protección de datos personales en entornos cloud (RT-11.06).

ISO/IEC 27005 — Gestión de Riesgos de Seguridad de la Información. Si bien este estándar no se encuentra listado de forma explícita en el Art. 4.3 de las Bases Administrativas, su aplicación resulta complementaria al requisito de ISO/IEC 27001 —que sí es exigido— y al modelado de amenazas documentado por componente y por integración que establecen las Bases Técnicas Transversales (RT-11.02). En el contexto de Puelche, donde la dispersión geográfica de la operación —seis instalaciones en cuatro regiones, 14.200 puntos de entrega, rutas rurales sin cobertura— amplía significativamente la superficie de ataque y los escenarios de amenaza, ISO/IEC 27005 provee el marco metodológico específico para la identificación, evaluación y tratamiento de los riesgos de seguridad de la información, articulando las exigencias de ISO 27001 con la gestión de riesgos general que exige ISO 31000 (RT-19.04).

ISO 22301 — Continuidad del Negocio e ISO/IEC 27031 — Continuidad TIC. La ventana crítica de despacho de 05:30 a 07:00 —donde 96 camiones salen simultáneamente y no existe forma de ejecutar la operación manualmente— impone un requisito de indisponibilidad cero durante ese tramo. Estos estándares gobiernan el plan de continuidad del negocio con análisis de impacto, escenarios de contingencia y procedimientos de respaldo, así como la estrategia de recuperación ante desastres con RTO máximo de 4 horas y RPO máximo de 15 minutos para servicios críticos (RT-07.04).

Disponibilidad de Infraestructura del 99,95 % (Capítulo 6, Bases Técnicas Transversales). La sala de servidores actual de Puelche —25 m² con aire acondicionado tipo split y UPS de 10 minutos— no cumple los estándares del Capítulo 6 de las Bases Técnicas Transversales, que exigen un nivel de disponibilidad de infraestructura del 99,95 % (RT-06.01). La solución deberá contemplar una sala técnica secundaria en el centro de distribución de Talca dimensionada para sostener recepción, preparación y despacho durante un corte, con sistema de alimentación ininterrumpida de al menos 30 minutos a plena carga (RT-06.07), generación autónoma de 24 horas (RT-06.08), climatización de precisión redundante N+1 (RT-06.13) y control de acceso biométrico (RT-06.20). Este nivel de disponibilidad se alinea con los principios de las instalaciones de categoría Tier III del Uptime Institute, aunque las bases no exigen dicha certificación de forma textual, sino el cumplimiento verificable de cada requisito técnico individual.

NIST Cybersecurity Framework 2.0 y NIST SP 800-207 (Zero Trust). El marco de ciberseguridad del NIST estructura las funciones de identificar, proteger, detectar, responder y recuperar (National Institute of Standards and Technology, 2024), mientras que el modelo Zero Trust establece que ninguna solicitud es confiable por defecto (National Institute of Standards and Technology, 2020). Ambos marcos son exigidos explícitamente por las Bases Administrativas (Art. 4.3) y las Bases Técnicas Transversales (RT-11.01) como fundamento de la arquitectura de seguridad de la solución.

OWASP ASVS 4.0, OWASP Top 10 y OWASP API Security Top 10. Los estándares de seguridad del software aplicativo, con nivel 2 como mínimo para el estándar de verificación, gobiernan la seguridad del código, de las interfaces de programación y del ciclo de desarrollo, complementados por CIS Benchmarks para el endurecimiento de todos los sistemas on-premise (RT-03.15).

ISO/IEC 20000-1 e ITIL 4 — Gestión de Servicios de TI. El Art. 4.3 de las Bases Administrativas exige la adherencia a ISO/IEC 20000-1 como estándar para el sistema de gestión de servicios de TI, complementado por las prácticas de ITIL 4. En el contexto de Puelche, donde el equipo de TI se compone de cuatro personas y la operación demanda soporte 24×7 durante la ventana crítica de despacho (05:30 a 07:00) y el turno nocturno de bodega (22:00 a 06:00), la correcta estructuración del catálogo de servicios, los acuerdos de nivel de servicio, la gestión de incidentes y la gestión de cambios resulta determinante para la sostenibilidad operacional de la solución.

ISO/IEC 25010 e ISO/IEC 25012 — Calidad del Producto de Software y Calidad de Datos. El Art. 4.3 de las Bases Administrativas establece estos estándares como referencia para la calidad del producto software y la calidad de los datos. ISO/IEC 25010 define las características de calidad (funcionalidad, rendimiento, compatibilidad, usabilidad, fiabilidad, seguridad, mantenibilidad y portabilidad) contra las cuales se evaluará la solución. ISO/IEC 25012 (RT-05.04) resulta especialmente relevante para Puelche, donde la calidad de los datos maestros —particularmente el maestro de productos, cuya codificación cambia cuando un proveedor reformula un producto sin aviso— condiciona la trazabilidad lote-a-lote y la interoperabilidad con el canal moderno.

WCAG 2.2 — Accesibilidad Web. El Art. 4.3 de las Bases Administrativas y la Ley N° 20.422 sobre igualdad de oportunidades e inclusión social de personas con discapacidad exigen que las interfaces de la solución cumplan con las pautas de accesibilidad para el contenido web en su nivel AA. Esta exigencia aplica a todos los componentes con interfaz de usuario, incluyendo los módulos web de gestión y los paneles de indicadores operacionales.

Estándares GS1 de Identificación e Interoperabilidad. Los estándares GS1 para identificación de productos (GTIN), unidades logísticas (SSCC), ubicaciones (GLN) y trazabilidad de eventos en la cadena de suministro constituyen el lenguaje de interoperabilidad con proveedores y con el canal moderno. Su adopción es obligatoria (RT-05.23) y resulta condición necesaria para cumplir las exigencias del canal moderno a partir de enero de 2029 y para satisfacer los requerimientos de trazabilidad sanitaria que motivaron la suspensión comercial del proveedor de lácteos.

En síntesis, el marco legal y regulatorio descrito no opera como un listado declarativo de cumplimiento, sino como un conjunto de restricciones de diseño que permean la totalidad de la arquitectura: desde el modelo de datos —que debe soportar cifrado a nivel de campo, auditoría inalterable y trazabilidad lote-a-lote— hasta la infraestructura on-premise —que debe garantizar continuidad ante cortes de enlace—, pasando por la seguridad del ciclo de desarrollo —con SBOM, firma de artefactos y análisis de composición—, la protección de datos personales —con RBAC/ABAC, seudonimización y registro de consultas— y la interoperabilidad tributaria y comercial —con integración al sistema de gestión y adherencia a estándares GS1—. Una propuesta que aborde estos requisitos como formalidades a mencionar, en lugar de como decisiones de ingeniería a resolver, no será competitiva.


## 2.3 Modelo Operativo Actual (Procesos "AS-IS")

El presente apartado describe, de forma narrativa y secuencial, el flujo operativo diario tal como se ejecuta actualmente en la Distribuidora Puelche S.A. El propósito de este mapeo no es prescriptivo sino diagnóstico: se busca documentar con precisión cada eslabón de la cadena operativa para identificar los puntos exactos donde la ausencia de digitalización, la duplicación de registros, el almacenamiento inseguro y los silos de información generan ineficiencias medibles y riesgos cuantificados. De esta cartografía del proceso actual se derivarán, en secciones posteriores, los requerimientos funcionales y no funcionales de la solución propuesta.


### 2.3.1 Abastecimiento y Recepción de Mercadería

El ciclo operativo diario de Puelche se inicia con el proceso de abastecimiento. El área de compras genera las órdenes de compra en el módulo correspondiente del sistema de gestión empresarial (ERP implantado en 2017), partiendo de una sugerencia de reposición que no produce el propio sistema, sino una planilla de cálculo mantenida por el jefe de abastecimiento. Esta planilla considera la venta de las últimas ocho semanas y un factor de ajuste manual por temporada; las promociones no ingresan al cálculo de forma automática, sino que se agregan manualmente cuando el área comercial comunica la novedad —comunicación que, según el propio personal operativo, no siempre ocurre—. La desconexión entre la planilla de reposición y el sistema de gestión constituye el primer silo de información del proceso: la lógica de compra reside en un artefacto local, no versionado, sin control de acceso ni respaldo automatizado.

Los proveedores confirman las órdenes por correo electrónico. Ninguno de los 180 proveedores activos lo hace por vía electrónica estructurada. Los avisos de despacho, cuando existen, llegan también por correo, en documento adjunto y en formatos heterogéneos que varían según el proveedor. La recepción física se realiza sin cita previa —salvo tres proveedores grandes que coordinan telefónicamente—, lo que genera filas de hasta cinco horas en temporada alta.

En el andén de recepción, el proceso de verificación es enteramente manual: el recepcionista cuenta la mercadería contra la guía de despacho en papel, revisa fechas de vencimiento por muestreo visual, anota el lote de los productos que lo requieren en un campo de texto libre del sistema —cuando el producto trae la información visible y cuando efectivamente se registra—, y firma la guía. Posteriormente, ingresa la recepción al ERP en una segunda digitación. Este punto constituye el primer quiebre crítico de trazabilidad: el registro del lote es discrecional, no estructurado y no validado. En el retiro sanitario de marzo de 2026, el 41 % de las recepciones del producto involucrado carecía de registro de lote.

[INSERTAR DIAGRAMA DE FLUJO 1: Proceso de Abastecimiento y Recepción AS-IS] — El diagrama deberá ilustrar el flujo desde la generación de la sugerencia de reposición en planilla, la emisión de la orden de compra en el ERP, la confirmación por correo electrónico del proveedor, la llegada física sin cita previa, la verificación manual en andén, la doble digitación (papel → ERP) y el punto exacto donde se pierde la trazabilidad de lote. Deberá marcarse con un símbolo de alerta cada nodo donde existe riesgo de error, pérdida de datos o duplicación de registro.


### 2.3.2 Almacenamiento e Inventario

Una vez recepcionada, la mercadería ingresa al centro de distribución de Talca (18.000 m²) donde opera un sistema de gestión de almacenes (WMS) instalado en 2013. Sin embargo, este sistema se utiliza exclusivamente en Talca; el centro de distribución de Concepción (9.000 m²) opera su control de inventario mediante planillas de cálculo locales, y las tres plataformas de cross-docking (Curicó, Chillán y Los Ángeles) carecen por completo de control de inventario sistematizado, bajo el supuesto —no siempre verificado— de que no almacenan mercadería.

La asignación de ubicaciones a productos dentro del almacén se realiza según el criterio personal del jefe de bodega, sin regla documentada de asignación por rotación, peso o compatibilidad. Las ubicaciones vigentes fueron definidas cuando se instaló el WMS hace trece años, y la rotación de los productos ha cambiado sustancialmente desde entonces —con productos de alta rotación ubicados en posiciones subóptimas—, pero nadie ha emprendido un reordenamiento porque implicaría detener la operación.

El conteo cíclico de inventario se ejecuta sobre 3.400 posiciones mensuales, en el turno de noche, utilizando planillas impresas como soporte de captura. El preparador recorre la bodega con la planilla, anota las cantidades con lápiz, y la hoja retorna a la oficina de bodega donde alguien transcribe los resultados al sistema. La diferencia promedio del conteo es de 2,3 % del valor contado —equivalente a una discrepancia significativa de inventario—, y los ajustes se ejecutan al cierre del mes sin investigación de causa raíz, salvo cuando superan un umbral que "todos conocen" pero que no está documentado formalmente. La ausencia de un mecanismo de captura digital en el punto de conteo —esto es, la dependencia del ciclo papel → transcripción manual → ajuste sin análisis— impide identificar si los faltantes se originan en errores de recepción, de preparación, de despacho o de hurto.

[INSERTAR DIAGRAMA DE FLUJO 2: Proceso de Almacenamiento y Control de Inventario AS-IS] — El diagrama deberá representar la bifurcación operativa entre Talca (con WMS), Concepción (con planillas locales) y las plataformas de cross-docking (sin control), evidenciando los silos de información que impiden una visión consolidada del inventario. Deberá incluir el ciclo de conteo manual (planilla impresa → conteo con lápiz → transcripción al sistema → ajuste sin causa) y marcar los puntos donde la desconexión entre sistemas genera divergencias de stock.


### 2.3.3 Preventa y Toma de Pedidos

La captura de la demanda comercial se ejecuta a través de 62 preventistas que recorren rutas fijas, visitando a cada cliente con frecuencia semanal o quincenal según su clasificación. El preventista opera en terreno —de pie, en la puerta del local del cliente, frecuentemente a la intemperie— con un dispositivo móvil que ejecuta una aplicación adquirida en 2016 a un proveedor que ya no existe: no tiene soporte técnico, no es compatible con los dispositivos actuales y no ha recibido actualizaciones en años.

La aplicación muestra el catálogo de productos y los precios, y permite registrar el pedido. No muestra, sin embargo, información que resulta esencial para una venta informada: el stock disponible en el centro de distribución, el crédito disponible del cliente, su deuda vencida ni su historial de compra. El preventista trabaja con esa información en la memoria o anotada en un cuaderno personal —un soporte no encriptado, sin logs de auditoría, sin control de acceso y sin respaldo de ningún tipo—. Esta condición genera un doble problema: por un lado, se venden productos que no existen en stock (el 7,8 % de las líneas de pedido presentan quiebre en el momento de la entrega); por otro, se toman pedidos a clientes cuyo crédito está bloqueado, y el pedido queda retenido sin que el preventista ni el cliente sean notificados —el cliente se entera cuando llama para reclamar—.

En las zonas rurales, donde la cobertura de red móvil es deficiente o inexistente —con tramos sin señal de hasta dos horas continuas—, la aplicación guarda los pedidos localmente. Sin embargo, su comportamiento al recuperar cobertura es impredecible: en ocasiones no envía los pedidos almacenados y en otras los envía duplicados. Nadie ha medido la frecuencia de cada fallo, pero el equipo comercial estima que "pasa todas las semanas". La sincronización carece de mecanismo de deduplicación, de resolución determinista de conflictos y de bitácora auditable de las decisiones aplicadas.

Adicionalmente, el preventista observa diariamente información valiosa en el punto de venta —producto vencido de Puelche en la góndola, exhibidores del competidor, riesgo de cierre del local— pero no dispone de ningún canal sistematizado para registrarla. Esta inteligencia comercial se pierde estructuralmente.

[INSERTAR DIAGRAMA DE FLUJO 3: Proceso de Preventa y Toma de Pedidos AS-IS] — El diagrama deberá ilustrar el flujo completo desde la visita del preventista al punto de venta, la toma del pedido en la aplicación obsoleta (sin visibilidad de stock, crédito ni historial), el almacenamiento local en modo offline, la sincronización deficiente al recuperar señal (con bifurcación: no envío / envío duplicado), la llegada del pedido al ERP, la validación de crédito y el bloqueo sin notificación. Deberá destacarse visualmente el cuello de botella principal: la operación "a ciegas" del preventista.


### 2.3.4 Planificación de Rutas

La asignación diaria de las aproximadamente 1.400 entregas a los 96 camiones disponibles (42 propios y 54 de transportistas externos) la realiza una única persona: Hugo Maldonado Sepúlveda, con 21 años de antigüedad en la empresa. El proceso consume entre 3,5 y 4 horas diarias (de 15:00 a 18:30) y se apoya en una planilla de cálculo de 11 hojas que el propio planificador desarrolló y que ningún otro integrante de la organización logra comprender ni replicar.

En esa planilla, y fundamentalmente en la memoria del planificador, reside conocimiento operacional de carácter crítico: restricciones de carga en puentes rurales, horarios de atención de clientes específicos, preferencias de conductor por cliente, detalle de caminos en mal estado y condiciones estacionales de las rutas. Este conocimiento no está documentado en ningún sistema, no dispone de respaldo, no es consultable por otros usuarios y no se integra con ninguna API del ecosistema de sistemas de la empresa. Cuando el planificador toma vacaciones, el cumplimiento de entrega cae entre 6 y 9 puntos porcentuales. Se jubila en dos años.

El resultado observable es una planificación subóptima y estructuralmente frágil: la ocupación promedio de los camiones en volumen es del 68 %, con días en que un camión sale con apenas el 41 % de su capacidad. Nadie mide el costo de esa ineficiencia porque nadie mide el costo del viaje —el prorrateo del costo logístico por zona geográfica data de 2016 y carece de vigencia técnica—.


### 2.3.5 Preparación de Pedidos y Carga

La preparación se ejecuta en el turno de noche (22:00 a 06:00) con aproximadamente 120 personas que presentan una rotación anual del 38 %. El preparador recibe una hoja de picking impresa, ordenada por ubicación de bodega, y recorre el almacén con un transpaleta armando cada pedido en pallets o canastillos. Marca con lápiz los productos que va extrayendo de las posiciones.

Los productos no encontrados o insuficientes quedan como faltantes y se anotan manualmente al pie de la hoja de picking. La hoja retorna a la oficina de bodega, donde un operario transcribe los faltantes al sistema para que la facturación se ajuste. Este es el segundo punto donde se pierde información: el faltante se registra cuantitativamente, pero no su causa (¿no había stock? ¿estaba mal ubicado? ¿fue tomado por otro pedido?). Sin la causa, no existe posibilidad de análisis de causa raíz ni de mejora continua del proceso.

Los productos refrigerados y congelados se preparan al final del turno para minimizar la exposición fuera de cámara. En la cámara de congelado (−22 °C), los preparadores trabajan con guantes térmicos en turnos de 30 minutos. Los dispositivos electrónicos convencionales no operan de forma confiable a esa temperatura y dentro de la cámara no existe cobertura de señal —ni de red móvil ni de la red inalámbrica de la bodega—. Esta condición ambiental extrema representa una restricción no negociable (N° 7) que cualquier solución de captura digital deberá resolver con hardware y conectividad especializados.

La carga en los camiones se realiza por orden de ruta invertido, de modo que la primera entrega quede accesible. La correcta ejecución de esta secuencia depende de que el cargador conozca el orden de la ruta del día —información que reside exclusivamente en la planilla personal del planificador—.

[INSERTAR DIAGRAMA DE FLUJO 4: Proceso de Preparación de Pedidos, Carga y Despacho AS-IS] — El diagrama deberá cubrir desde la generación de la hoja de picking impresa, el recorrido del preparador por la bodega, la anotación manual de faltantes (sin causa), la transcripción al sistema, la preparación diferida de productos de cadena de frío, la carga en orden inverso de ruta y la salida de los camiones entre 05:30 y 07:00. Deberán marcarse los puntos de reingreso de datos (hoja → sistema) y el cuello de botella de la dependencia con la planilla del planificador para la secuencia de carga.


### 2.3.6 Transporte, Entrega y Cobro

Los camiones salen entre las 05:30 y las 07:00 portando las guías de despacho impresas en papel. El conductor lleva consigo, además, un termógrafo manual que debe leer y anotar tres veces durante el viaje para los productos con cadena de frío. No existe registro continuo ni automático de temperatura en ningún punto del transporte.

En el local del cliente, el conductor y el peoneta descargan la mercadería, el cliente revisa visualmente el pedido y firma la guía de despacho en papel. Si el cliente rechaza algún producto —por daño, fecha de vencimiento próxima o error en el pedido—, el conductor lo anota manualmente en la guía y lo reincorpora al camión. Si el cliente paga al contado (38 % de las ventas del canal tradicional), el conductor recibe el efectivo, lo anota y lo guarda en la cabina —en rutas rurales, un conductor puede circular con más de un millón de pesos en efectivo—.

Cuando el local del cliente se encuentra cerrado, no existe protocolo escrito que defina la acción a seguir. Cada conductor decide según su criterio: regresa más tarde, deja el pedido con el negocio vecino o se lo lleva de vuelta al centro de distribución. Esta discrecionalidad es la causa principal del 4,2 % de reentregas sobre el total de entregas.

Al regresar al centro de distribución, el conductor entrega el fajo de guías firmadas en la oficina. Esas guías se archivan físicamente en carpetas. El 1,1 % mensual de las guías no llega: se mojan en ruta, se pierden o quedan ilegibles. Cuando un cliente reclama no haber recibido un pedido, encontrar su guía toma en promedio 12 días; si la guía no aparece, la empresa no tiene forma de demostrar la entrega. Las diferencias entre lo pedido, lo despachado y lo efectivamente recibido no quedan explicadas en el momento: se descubren semanas después, cuando el cliente reclama o cuando llega la factura.

La rendición del efectivo cobrado se realiza a la mañana siguiente en caja, con el conductor contando el dinero contra el listado de entregas del día anterior. Las diferencias promedian $4,2 millones mensuales en toda la flota y se resuelven —según el jefe de tesorería— "conversando", sin investigación formal de si la diferencia corresponde a un error de conteo, a un descuento otorgado discrecionalmente por el conductor, a un cobro no realizado o a una pérdida.

[INSERTAR DIAGRAMA DE FLUJO 5: Proceso de Transporte, Entrega, Cobro y Rendición AS-IS] — Este diagrama deberá representar el flujo completo desde la salida del camión, las lecturas manuales de temperatura, la entrega y firma en papel en el local del cliente, las bifurcaciones ante local cerrado (sin protocolo), el cobro en efectivo, el retorno al centro de distribución, la entrega de guías, el archivo físico, la rendición al día siguiente y la resolución informal de diferencias. Deberán destacarse los puntos de riesgo: pérdida de guías (1,1 %), seguridad del efectivo, ausencia de evidencia digital de entrega y tiempo de resolución de reclamos (12 días).


### 2.3.7 Devoluciones, Mermas y Activos Retornables

Las devoluciones (2,9 % del volumen despachado) retornan al centro de distribución en el mismo camión, se reciben en un andén distinto, se revisan y se decide su destino: reingreso a stock, venta con descuento, devolución al proveedor o destrucción. Esta decisión la toma el jefe de bodega producto por producto, sin que quede registrada de forma estructurada en ningún sistema. El parque de 68.000 canastillos plásticos y 9.400 pallets en circulación se controla —si puede llamarse control— mediante anotaciones de los conductores en cuadernos personales, con una pérdida anual estimada del 14 % del parque, sin mecanismo de imputación por cliente ni por conductor. La merma por vencimiento (1,7 % del valor del inventario anual) se detecta tardíamente: en el conteo cíclico, en la preparación de pedidos o, en el peor escenario, cuando el preventista encuentra producto vencido de Puelche en la góndola del cliente.


### 2.3.8 Síntesis de Ineficiencias Estructurales del Modelo AS-IS

El análisis secuencial del flujo operativo revela un patrón sistémico: cada eslabón de la cadena opera con información incompleta, capturada en soportes frágiles (papel, cuadernos personales, planillas locales), transcrita manualmente al menos una vez —y frecuentemente dos— antes de llegar a un sistema de registro, almacenada sin encriptación ni protección de acceso, y confinada en silos que no conversan entre sí ni se integran mediante APIs o mecanismos automatizados de intercambio. El resultado no es una suma de ineficiencias aisladas, sino un sistema donde las deficiencias se refuerzan mutuamente: la venta "a ciegas" del preventista produce quiebres de stock que la bodega no puede anticipar porque no tiene visibilidad sobre lo comprometido; la planificación artesanal de rutas subutiliza la flota porque carece de datos de volumen y peso por producto; la entrega sin evidencia digital impide resolver reclamos que generan reentregas que nadie puede costear porque el costo de servir es desconocido.

[INSERTAR DIAGRAMA DE FLUJO 6: Visión Integrada del Ciclo Completo del Pedido AS-IS — Desde la Preventa hasta la Rendición] — Este diagrama de síntesis deberá representar el ciclo completo del pedido en una vista integrada, conectando las siete fases descritas, identificando con un código de color los tres tipos de ineficiencia recurrente: (a) captura manual y reingreso duplicado de datos (en rojo), (b) silos de información desconectados (en amarillo), y (c) almacenamiento inseguro sin cifrado, auditoría ni respaldo (en naranja). Deberá incluir, junto a cada cuello de botella, el indicador cuantificado de su impacto (7,8 % de quiebre de stock, 4,2 % de reentregas, 2,3 % de discrepancia de inventario, 1,1 % de guías extraviadas, $4,2 M de diferencias de rendición, 12 días para resolver un reclamo, 9 días para un retiro sanitario).


## 2.4 Diagnóstico de Ineficiencias

Las operaciones en Puelche se sostienen sobre procesos mayoritariamente manuales, sistemas con más de una década de antigüedad sin soporte, y conocimiento crítico que reside en personas y no en sistemas. Las ineficiencias se distribuyen a lo largo de todo el ciclo del pedido, es decir, desde la toma de la orden hasta la cobranza, apoyándose mutuamente, logrando que el impacto total sea mayor que la suma de sus partes.


### 2.4.1 Preventas

Los 62 preventistas utilizan una aplicación adquirida en 2016 a un proveedor que ya no existe: no tiene soporte técnico, no es compatible con los dispositivos actuales y no ha recibido actualizaciones. Más allá de su obsolescencia técnica, la aplicación no tiene las funcionalidades básicas para una venta informada: no muestra el stock disponible, no muestra la deuda ni crédito del cliente, además de no mostrar el historial de compra. El preventista trabaja con esa información en la cabeza o anotada en un cuaderno personal.

En zonas rurales, donde la cobertura de red es prácticamente inexistente, la aplicación guarda los pedidos localmente, pero en ocasiones no los envía al recuperar señal, y en otras los envía duplicado. Nadie ha medido con qué frecuencia ocurre cada cosa, pero el equipo comercial estima que "pasa todas las semanas". El resultado es que el 7,8 % de las líneas de pedido presentan quiebre en el momento de la entrega porque se vendió algo que no había, y que los pedidos bloqueados por crédito quedan retenidos sin que nadie avise al preventista ni al cliente, que se entera cuando llama molesto. Además, el preventista observa todos los días información valiosa en la góndola del cliente, como producto vencido, exhibidores del competidor o riesgo de cierre del local, que no tiene dónde registrar.


### 2.4.2 Planificación de Rutas

La asignación diaria de las 1.400 entregas a los 96 camiones disponibles la realiza una sola persona: Hugo Maldonado Sepúlveda, con 21 años de antigüedad en la empresa. El proceso toma entre 3,5 y 4 horas diarias y se apoya en una planilla de cálculo de 11 hojas que el propio planificador desarrolló y que nadie más logra comprender. En esa planilla, y en su memoria, existe conocimiento operacional considerado como crítico: restricciones de carga en puentes rurales, horarios de atención de clientes específicos, preferencias de conductor por cliente y el detalle de caminos en mal estado. Este conocimiento no está documentado en ningún sistema. Cuando el planificador toma vacaciones, el cumplimiento de entrega cae entre 6 y 9 puntos porcentuales. Se jubila en dos años.

El resultado es una planificación subóptima y frágil: la ocupación promedio de los camiones en volumen es del 68 %, con días en que un camión sale con el 41 % de su capacidad. Nadie mide el costo de esa ineficiencia porque nadie mide el costo del viaje.


### 2.4.3 Registro del Pedido y Protocolos

El conductor sale entre las 05:30 y las 07:00 con las guías de despacho impresas en papel. La prueba de entrega es la firma del cliente en esa guía. Al regresar, entrega el fajo de guías a la oficina. El 1,1 % mensual no llega: se moja, se pierde en ruta o queda ilegible. Cuando un cliente reclama que no recibió un pedido, encontrar su guía toma en promedio 12 días; si la guía no aparece, la empresa no tiene cómo demostrar la entrega.

Cuando el local del cliente está cerrado, no existe ningún protocolo escrito. Cada conductor decide: vuelve más tarde, deja el pedido con el negocio de al lado, o se lo lleva de vuelta. Esta discrecionalidad es la causa principal del 4,2 % de reentregas sobre el total de entregas. Asimismo, las diferencias entre lo pedido, lo despachado y lo efectivamente recibido no quedan explicadas: se descubren semanas después, cuando el cliente reclama o cuando llega la factura.


### 2.4.4 Trazabilidad de Lote Inexistente

El lote de un producto se registra en recepción en un campo de texto libre, y eso, cuando en verdad se registra. No existe ninguna integración entre ese registro y los movimientos posteriores del producto, como la preparación del pedido, carga, despacho y entrega al cliente. La trazabilidad existe únicamente en papel de bodega y en la memoria de las personas que operaron cada etapa. En el retiro sanitario de marzo, el 41 % de las recepciones del producto involucrado no tenía registro de lote, lo que hizo imposible delimitar el universo afectado con precisión.


### 2.4.5 Monitoreo de la Cadena de Frío

Los 1.100 SKU refrigerados o congelados están sujetos a exigencias sanitarias estrictas de control de temperatura. Sin embargo, el monitoreo se realiza de forma manual: dos lecturas por turno en las cámaras del centro de distribución (anotadas en planilla) y tres lecturas por viaje en los camiones con equipo de frío (anotadas por el conductor en papel). No existe registro continuo ni automático en ningún punto de la cadena. La autoridad sanitaria observó formalmente esta ausencia en su última fiscalización. Durante 2025, un cliente de food service rechazó un camión completo por sospecha de ruptura de cadena de frío; Puelche no pudo demostrar que la temperatura se había mantenido dentro de rango y asumió una pérdida de $21 millones.

Por otro lado, no existe ninguna regla escrita que defina qué constituye una excursión de temperatura que invalida el producto, quién tiene autoridad para tomar esa decisión y si el sistema debe bloquear el despacho de forma automática. La ausencia de esta regla hace inoperable cualquier sistema de alertas.


### 2.4.6 Cobranza en Efectivo sin Control Real

El 38 % de las ventas del canal tradicional se cobra en efectivo contra entrega. Los conductores rinden al día siguiente en caja, contando el dinero contra el listado de sus entregas del día anterior. Las diferencias de rendición promedian $4,2 millones mensuales en toda la flota y se resuelven, en palabras del jefe de tesorería, «conversando». No se investiga si la diferencia corresponde a un error de conteo, a un descuento que el conductor otorgó por su cuenta, a un cobro no realizado o a una pérdida. En algunas rutas rurales, el conductor circula con más de un millón de pesos en efectivo en la cabina.


### 2.4.7 Activos Retornables y Mermas sin Control Estructurado

La empresa tiene en circulación un parque estimado de 68.000 canastillos plásticos y 9.400 pallets. La palabra "estimado" es literal: no existe control individual de cada unidad. Los conductores registran las devoluciones de canastillos en un cuaderno. La pérdida anual estimada del parque es del 14 %, sin que exista un mecanismo de imputación por cliente o por conductor. La merma por vencimiento equivale al 1,7 % del valor del inventario al año, y se detecta en el conteo cíclico, en la preparación de pedidos, y, en el peor de los casos, cuando el preventista encuentra producto vencido de Puelche en la góndola del cliente.


### 2.4.8 Costo Logístico Desconocido

La determinación del gasto logístico se fundamenta en un prorrateo por área geográfica definido en 2016, cuya vigencia técnica es nula. Actualmente, la organización desconoce el costo real de servir a puntos de venta específicos, como un almacén en Empedrado con compras de $45.000 quincenales; variables críticas como el kilometraje, tiempos de servicio en descarga, densificación de rutas o la incidencia del preventista son ignoradas. Esta opacidad financiera sugiere que la distribuidora podría estar operando con margen negativo en miles de cuentas, ejecutando políticas de descuentos y logísticas sobre una base teórica que dista de la ejecución operativa diaria.


## 2.5 Análisis de Impacto

Las ineficiencias descritas en la sección anterior no operan de forma aislada: se encadenan y amplifican mutuamente, produciendo un impacto acumulado que excede la suma de sus efectos individuales. A continuación se cuantifica el impacto financiero, operacional y regulatorio de cada eje de ineficiencia, tomando como referencia los datos declarados por la propia organización y los registros del incidente sanitario de marzo de 2026.


### 2.5.1 Impacto Financiero Directo


> **Tabla 2** — 2.5.1 Impacto Financiero Directo · 8 filas · ver planilla del subdocumento


### 2.5.2 Impacto Operacional


> **Tabla 3** — 2.5.2 Impacto Operacional · 7 filas · ver planilla del subdocumento


### 2.5.3 Impacto Regulatorio y Comercial


> **Tabla 4** — 2.5.3 Impacto Regulatorio y Comercial · 5 filas · ver planilla del subdocumento


## 2.6 Problemas por Área


### 2.6.1 Área 1: Trazabilidad y Calidad Sanitaria

Este eje aborda la falta estructural para registrar y auditar, mediante datos estructurados y en tiempo real, el flujo de un lote desde su ingreso al almacén hasta la recepción final. Asimismo, contempla la ausencia de una supervisión automatizada y permanente de la temperatura en la cadena de frío, afectando tanto a las cámaras de los centros de distribución como a las unidades de transporte especializado.

La consecuencia crítica de esta brecha recae en el riesgo sanitario y el impacto financiero frente a eventuales retiros de producto, además del incumplimiento de normativas vigentes y la potencial pérdida de proveedores estratégicos que exigen trazabilidad certificada. El alcance operativo impacta la recepción de mercadería, el almacenamiento refrigerado, el picking de productos sensibles y la logística de última milla con temperatura controlada.


### 2.6.2 Área 2: Preventa y Gestión Comercial en Terreno

Esta dimensión abarca la captura de pedidos en el punto de venta, la administración de límites de crédito, las gestiones de cobranza y el levantamiento de información competitiva en góndola. Lo principal es la operación a ciegas del preventista, quien no tiene visibilidad sobre el stock disponible, estados financieros del cliente o historiales de consumo, utilizando herramientas que resultan ineficaces ante las condiciones de conectividad del terreno.

El efecto directo es el deterioro del nivel de servicio por quiebres de stock no informados y la parálisis de pedidos sin previo aviso, sumado a la pérdida de competitividad frente a nuevos actores que ya implementan modelos de autoservicio digital. Los procesos críticos comprometidos incluyen la toma de órdenes, la validación de crédito in situ y la detección de alertas comerciales en el mercado.


### 2.6.3 Área 3: Planificación de Rutas y Operación de Reparto

La programación diaria de despachos, la optimización de secuencias, la ejecución de la entrega y el cierre administrativo de la ruta, culminando en la gestión de incidencias como locales cerrados o devoluciones inmediatas. La vulnerabilidad central reside en la dependencia absoluta del conocimiento empírico de un solo individuo y la inexistencia de certificados de entrega digitales.

El impacto se traduce en una fragilidad operativa ante la ausencia del planificador, una utilización ineficiente de la flota y la incapacidad de gestionar reclamos con evidencia oportuna, además de desajustes en las rendiciones de efectivo. Los hitos afectados van desde el despacho en bodega hasta la liquidación diaria de los transportistas.


### 2.6.4 Área 4: Gestión de Bodega e Inventario

Se enfoca en la gobernanza de ubicaciones y existencias, los procesos de picking nocturno, los inventarios rotativos y la administración de activos retornables. La debilidad principal es la ejecución basada en soportes físicos, lo que impide el análisis de causas raíz en faltantes y el control unívoco de los activos de la compañía.

Esto deriva en discrepancias de inventario significativas (2,3 % del valor total), mermas por caducidad detectadas tardíamente y el extravío anual del 14 % del parque de canastillos y pallets. Las operaciones impactadas incluyen el almacenamiento estratégico, el surtido de pedidos y la logística inversa de devoluciones y activos.


### 2.6.5 Área 5: Información de Gestión y Costo de Servir

Contempla la generación de indicadores de desempeño en tiempo real, la determinación del costo logístico exacto por entrega y la integración tecnológica con los requerimientos del canal moderno para el 2029. La carencia central es que la inteligencia de negocio actual se sustenta en prorrateos teóricos y cierres diferidos, sin captura de datos en el origen del evento.

El riesgo principal es la toma de decisiones estratégicas sobre premisas inexactas y la imposibilidad técnica de cumplir con los protocolos EDI exigidos por las grandes cadenas. Los procesos involucrados abarcan el control de gestión diario, el análisis de rentabilidad granular y los reportes de cumplimiento ante organismos fiscalizadores.


## 2.7 Actores Afectados

La solución debe estar enteramente diseñada revisando minuciosamente la realidad de todos los actores que van a interactuar con el sistema, tanto internos como externos.


> **Tabla 5** — 2.7 Actores Afectados · 12 filas · ver planilla del subdocumento


## 2.8 Registro de Supuestos del Caso

Los siguientes supuestos delimitan el marco dentro del cual debe diseñarse la solución. No son opcionales: son condiciones del entorno que la propuesta debe respetar íntegramente.


> **Tabla 6** — 2.8 Registro de Supuestos del Caso · 11 filas · ver planilla del subdocumento


## Referencias (APA 7.ª)

A continuación se listan, en formato APA 7.ª, las fuentes normativas y sectoriales que fundamentan el contexto del problema y el marco legal y regulatorio del Subdoc. 2. La referencia normativa chilena se estructura con el autor institucional (ente emisor), el año de la versión vigente aplicable y el título oficial del cuerpo legal.

- Biblioteca del Congreso Nacional de Chile. (1996). *Ley 19.628 sobre protección de la vida privada* [Decreto 977/96 del Ministerio de Salud: Reglamento Sanitario de los Alimentos]. https://www.bcn.cl/leychile/navegar?idNorma=71271 listo

- GS1. (2020). *GS1 General Specifications: The foundational GS1 standard that defines how identification keys, data attributes and barcodes must be used* (Issue 20.0). GS1 AISBL.

https://documents.gs1us.org/adobe/assets/deliver/urn:aaid:aem:afbf55ad-0151-4a0c-8454-d494c0dc9527/GS1-General-Specifications.pdf

- International Organization for Standardization. (2022). *ISO/IEC 27001:2022 — Information security management systems — Requirements*. ISO.

- Ministerio de Salud. (1996). *Decreto 977: APRUEBA REGLAMENTO SANITARIO DE LOS ALIMENTOS*. Diario Oficial.

https://www.bcn.cl/leychile/navegar?idNorma=71271

- Ministerio del Interior y Seguridad Pública. (2017). *Ley 21.045: Crea el Ministerio de las Culturas, las Artes y el Patrimonio* (normativa de datos personales: Ley 19.628). Biblioteca del Congreso Nacional.

https://www.bcn.cl/leychile/navegar?idNorma=1110097

- Ministerio del Interior y Seguridad Pública. (2023). *Ley 21.663: Marco de ciberseguridad* (crea la Agencia Nacional de Ciberseguridad). Biblioteca del Congreso Nacional.

https://www.bcn.cl/leychile/navegar?idNorma=1202434

- Ministerio del Interior y Seguridad Pública. (2024). *Ley 21.719: Protección de datos personales*. Biblioteca del Congreso Nacional.

https://www.bcn.cl/leychile/navegar?idNorma=1209272

- National Institute of Standards and Technology. (2020). *Zero Trust Architecture* (NIST SP 800-207). U.S. Department of Commerce. https://doi.org/10.6028/NIST.SP.800-207

- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). U.S. Department of Commerce. https://doi.org/10.6028/NIST.CSWP.29

- Servicio de Impuestos Internos. (2024). *Manual del contribuyente: Documentos Tributarios Electrónicos (DTE)*. Gobierno de Chile. https://www.sii.cl

LAFROX

Propuesta de Solución — Distribuidora Puelche S.A.

Licitación N° TFEP-01/2026 — Caso 02 Logística

SUBDOCUMENTO 3

Esquema de Solución y Alcance

Informe 1
