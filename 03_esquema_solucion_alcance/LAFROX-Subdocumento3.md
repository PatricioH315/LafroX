<!-- Conversión fiel a Markdown. Los bloques [Descripción de imagen] y los separadores de página son notas de conversión; el resto corresponde al contenido original. Se conservan las referencias y los cortes de página del PDF. -->

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

## Subdocumento 3 — Esquema de solución y alcance

Subdocumento 3 · Formulario T-7

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

LAFROX-Subdocumento3.pdf

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
| 3 Introducción al Alcance de la Solución | 5 |
| 3.1 Resumen Ejecutivo de la Solución | 5 |
| 3.1.1 Capacidades de la solución | 5 |
| 3.1.2 Implementación, implantación y operación | 6 |
| 3.2 Alcance | 8 |
| 3.2.1 Reparto entre etapas y dependencias | 8 |
| 3.2.2 Exclusiones, restricciones y supuestos | 9 |
| 3.2.3 Catálogo de requerimientos y correspondencia | 10 |
| 3.2.4 Reglas de negocio y consultas | 11 |
| 3.2.5 Criterios de aceptación | 12 |
| 3.3 Esquema de solución | 14 |
| 3.3.1 Vista conceptual del ciclo logístico | 14 |
| 3.3.2 Trazabilidad y cadena de frío | 14 |
| 3.3.3 Continuidad e integración | 16 |
| 3.4 Explicación de la Solución | 16 |
| 3.4.1 Aplicación en la jornada operacional | 17 |
| 3.4.2 Correspondencia con la arquitectura lógica | 18 |
| 3.4.3 Implementación | 18 |
| 3.4.4 Implantación | 19 |
| 3.4.5 Operación | 21 |
| 3.4.6 Participación de los grupos de interés | 23 |
| Referencias | 24 |
| Declaración de uso de IA | 24 |

LafroX SpA

Propuesta Técnica

2

---

<!-- Página 3 del PDF original -->

LafroX SpA

> **[Descripción de imagen — elementos gráficos de página]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», sobre una línea horizontal gris. En el pie aparece una franja negra con borde superior naranja inclinado.

## Lista de tablas

| Contenido | Página |
| --- | --- |
| Tabla 3.1 Marco contractual de las etapas. Fuente: Bases Administrativas, art. 17. | 6 |
| Tabla 3.2 Alcance funcional por etapa. Fuente: Subdocumento 2, Anexo 2.1; Anexo 3.A. | 8 |
| Tabla 3.3 Síntesis de resultados de aceptación. Fuente: caso, cap. 18; Anexo 3.J. | 12 |
| Tabla 3.4 Correspondencia entre capacidades del alcance y módulos lógicos. Fuente: elaboración propia. | 18 |
| Tabla 3.5 Objetivos de servicio. Fuente: BA, art. 78.2; BTT, secciones 7.2 y 10; caso, cap. 10 y 15. | 22 |
| Tabla 3.6 Declaración de uso de IA. Fuente: registro del equipo. | 24 |

LafroX SpA

Propuesta Técnica

3

---

<!-- Página 4 del PDF original -->

LafroX SpA

> **[Descripción de imagen — elementos gráficos de página]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», sobre una línea horizontal gris. En el pie aparece una franja negra con borde superior naranja inclinado.

## Lista de figuras

| Contenido | Página |
| --- | --- |
| Figura 3.1 Relación conceptual de capacidades y módulos. Fuente: elaboración propia a partir del Subdocumento 2, Anexo 2.1. | 15 |
| Figura 3.2 Información necesaria para trazabilidad sanitaria. Fuente: elaboración propia a partir del caso, cap. 18, criterios 1 a 3. | 15 |
| Figura 3.3 Ámbitos de continuidad e intercambio, sin topología física. Fuente: elaboración propia; BA, art. 16; caso, cap. 10 y 15. | 16 |

LafroX SpA

Propuesta Técnica

4

---

<!-- Página 5 del PDF original -->

> **[Descripción de imagen — elemento gráfico de página]**
> En el borde inferior aparece una franja negra con una línea naranja inclinada en su borde superior.

CAPÍTULO 3

# Introducción al Alcance de la Solución

Este capítulo define qué construye LafroX para Distribuidora Puelche S.A., en qué etapa, bajo qué condiciones y cómo se acepta. Responde a los tres problemas descritos en el Subdocumento 2 y se apoya en la estructura de proyecto del Subdocumento 1.

## 3.1 Resumen Ejecutivo de la Solución

La propuesta aborda tres necesidades relacionadas: recuperar la trazabilidad sanitaria y comercial, mejorar la confiabilidad de las entregas y conocer el costo de servir. La primera exige capturar lote y temperatura donde se mueve el producto; la segunda necesita pedidos con información comercial y evidencia de entrega; y la tercera depende de que los hechos de cada entrega queden registrados. Esta relación problema–necesidad se desarrolla en el Subdocumento 2, secciones «Resumen Ejecutivo del problema» y «Los tres problemas entrelazados».

### 3.1.1 Capacidades de la solución

El alcance funcional comprende preventa desconectada con consulta de stock y crédito, recepción con lote y vencimiento, gestión de bodega con FEFO, preparación por olas, cross-docking controlado, planificación de rutas, control de frío, entrega digital, acuse de recibo de la guía de despacho articulado con el ERP, conciliación de efectivo, reposición y retiro sanitario. El portal de clientes, la integración electrónica del canal moderno y el costo de servir completan el alcance de la segunda etapa. Estas capacidades corresponden a las familias F-01 a F-14 del Subdocumento 2, Anexo 2.1.

Estas capacidades se entienden mejor desde cada uno de los tres problemas del Subdocumento 2.

Trazabilidad sanitaria y comercial: Hoy el lote se anota en texto libre, cuando se anota, y en el producto del retiro de marzo de 2026 el 41 % de las recepciones no lo registraba; el retiro demoró 9 días (Subdocumento 2, sección 2.1). La solución ataca la causa en el punto donde se pierde el dato: la recepción no se cierra sin lote y vencimiento en los productos que lo requieren, el inventario los arrastra en cada movimiento y la entrega los asocia a la guía y al cliente. Con esa cadena, la lista de clientes afectados por un lote es una consulta y no una reconstrucción manual. El registro térmico continuo en cámaras y vehículos reemplaza las tres lecturas manuales por viaje y aporta la evidencia que la autoridad sanitaria observó como ausente.

Confiabilidad de la entrega: El OTIF de 82,4 % se explica por pedidos tomados sin ver stock ni crédito (7,8 % de las líneas con quiebre), rutas diagramadas a mano en 3,5 horas diarias y entregas sin evidencia inmediata (1,1 % mensual de guías extraviadas o ilegibles y 4,2 % de

LafroX SpA

Propuesta Técnica

5

---

<!-- Página 6 del PDF original -->

LafroX SpA

Introducción al Alcance de la Solución

> **[Descripción de imagen — elementos gráficos de página]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», sobre una línea horizontal gris. En el pie aparece una franja negra con borde superior naranja inclinado.

reentregas). La solución actúa en cada eslabón: el preventista ve stock y crédito y la promesa que corresponde al cliente; la ruta se genera en menos de 20 minutos y el planificador la corrige; el conductor registra la entrega, la evidencia y el cobro con o sin señal. Ninguna de estas mejoras exige al almacenero tecnología propia.

Costo de servir: El precio y el margen se calculan hoy con un costo de transporte promedio de 2016. El costo real de atender a cada cliente solo puede calcularse si cada entrega deja registro de su tiempo, su distancia, su carga, sus devoluciones y sus reentregas. Por eso la Etapa 1 captura esos hechos y la Etapa 2 los convierte en costo por cliente y por entrega. Sin la primera, la segunda repetiría el prorrateo actual con otra herramienta.

El ERP se conserva como registro contable y único emisor de documentos tributarios. La solución aporta los datos de la operación y convive con los procesos excluidos del contrato. El almacenero no necesita adquirir un dispositivo, disponer de internet ni abandonar el efectivo.

El despliegue es híbrido, con carga en nube y componentes on-premise. El turno móvil sin cobertura y la continuidad del centro de distribución ante un corte del enlace forman parte del alcance desde su definición; no se agregan como contingencias al final del desarrollo.

La solución organiza estas capacidades en doce módulos de negocio: M1 Recepción, M2 Inventario, M3 Preventa, M4 Rutas, M5 Preparación, M6 Reparto, M7 Cobranza y rendición, M8 Devoluciones y envases, M9 Calidad y trazabilidad, M10 Analítica, M11 Canal moderno y M12 Telemetría. Una base compartida provee identidad, integración, registro auditable, operación desconectada y observabilidad. La carga principal se ejecuta en nube pública y el borde operacional del CD sostiene recepción, preparación y despacho durante la pérdida de enlace. El detalle de servicios, red y dimensionamiento corresponde a la arquitectura de la oferta.

### 3.1.2 Implementación, implantación y operación

La Tabla 3.1 sitúa el alcance en los meses del contrato.

Tabla 3.1 Marco contractual de las etapas. Fuente: Bases Administrativas, art. 17.

| Etapa | Desarrollo | Marcha blanca | Producción / operación |
| --- | --- | --- | --- |
| Etapa 1 | Meses 1–12 | Meses 13–15 | Producción: mes 16 |
| Etapa 2 | Meses 13–18 | Meses 19–20 | Producción: mes 21 |
| Operación |  |  | Meses 21–56: 36 meses |

La superposición de los meses 13 a 20 obliga a sostener dos frentes: estabilizar la Etapa 1

LafroX SpA

Propuesta Técnica

6

---

<!-- Página 7 del PDF original -->

LafroX SpA

Introducción al Alcance de la Solución

> **[Descripción de imagen — elementos gráficos de página]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», sobre una línea horizontal gris. En el pie aparece una franja negra con borde superior naranja inclinado.

mientras se construye y prueba la Etapa 2. La implementación de la Etapa 2 no interviene las funciones estabilizadas de la Etapa 1 durante la ventana de despacho de 05:30 a 07:00.

La fecha de inicio del contrato no está definida (consulta V-12), pero el calendario puede analizarse de antemano. Si el mes 1 es el mes calendario m, el mes 16 cae en m + 3 y el mes 21 en m + 8, en aritmética de doce meses. Por lo tanto:

- un inicio en junio o septiembre ubica el paso a producción de la Etapa 1 en septiembre o diciembre;

- un inicio en enero o abril ubica el paso a producción de la Etapa 2 en septiembre o diciembre;

- los inicios en febrero, marzo, mayo, julio, agosto, octubre, noviembre y diciembre no generan conflicto.

El caso prohíbe el paso a producción en todo septiembre y en todo diciembre, además de los tres primeros días hábiles de cada mes. El congelamiento del 1 al 25 de septiembre (Anexo 3.E, R-08) no abre una ventana entre el 26 y el fin de mes para un paso a producción. El Art. 17° fija los meses 16 y 21, de modo que no es posible adelantarlos ni postergarlos sin alterar el cronograma obligatorio. Por eso LafroX supone que el contrato se inicia en uno de los ocho meses sin conflicto (Anexo 3.C, S-17). La eventual incompatibilidad entre los meses contractuales de paso a producción y las ventanas de prohibición del caso se plantea al mandante mediante V-17, por escrito, a través del canal oficial y durante el período de consultas de la licitación; su resolución requiere una respuesta formal (Anexo 3.H, V-17). En cualquier mes, el paso a producción evita los tres primeros días hábiles por el cierre contable.

El hito de enero de 2029 exige que el canal moderno esté en producción antes de esa fecha. Como el mes 21 no puede caer en diciembre, el inicio de contrato debe ser a más tardar en marzo de 2027, con lo que el mes 21 cae en noviembre de 2028. De los meses compatibles con S-17, diciembre de 2026 —si la contratación permite iniciar ese mes— y febrero o marzo de 2027 permiten comenzar después de los resultados de la licitación y poner la Etapa 2 en producción antes de enero de 2029. La fecha efectiva de inicio debe confirmarse mediante V-12.

La suspensión del proveedor de lácteos vence en septiembre de 2026, antes del mes 1 de cualquier inicio admisible. El vencimiento no restituye por sí solo la relación: el caso exige que la compañía acredite capacidad de trazabilidad para restablecerla. Por eso la trazabilidad de lote encabeza la secuencia de la Etapa 1 y la evidencia aceptable se consulta al proveedor (consulta V-13).

El comité ejecutivo prefiere primero trazabilidad y frío, luego preventa y entrega, y por último rutas y costo de servir. LafroX acoge los dos primeros grupos en la Etapa 1, pero adelanta las rutas a la Etapa 1. La observación de la gerenta general se considera fundada: el planificador se jubila en dos años y el cumplimiento cae entre 6 y 9 puntos cuando se ausenta. Si las rutas quedaran en la Etapa 2, su producción en el mes 21 llegaría cerca de su retiro, sin tiempo para capturar su conocimiento. El costo de servir sí se mantiene en la Etapa 2, porque necesita meses de hechos de entrega registrados en la Etapa 1.

LafroX SpA

Propuesta Técnica

7

---

<!-- Página 8 del PDF original -->

LafroX SpA

Introducción al Alcance de la Solución

> **[Descripción de imagen — elementos gráficos de página]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», sobre una línea horizontal gris. En el pie aparece una franja negra con borde superior naranja inclinado.

## 3.2 Alcance

El alcance se organiza por capacidades que responden a necesidades del CLIENTE. Las familias del Subdocumento 2, Anexo 2.1, orientan el reparto funcional; las Bases fijan los límites y resultados mínimos. Los subtítulos siguientes tratan las etapas, los límites del alcance, el catálogo, las reglas y la aceptación.

### 3.2.1 Reparto entre etapas y dependencias

La Tabla 3.2 resume la asignación de las familias F-01 a F-14 a las etapas. La correspondencia detallada con cada requerimiento está en el Anexo 3.A, Tabla 3.A.2.

Tabla 3.2 Alcance funcional por etapa. Fuente: Subdocumento 2, Anexo 2.1; Anexo 3.A.

| Capacidad | Familias SD2 | Etapa | Dependencia principal |
| --- | --- | --- | --- |
| Preventa, recepción, bodega y preparación | F-01 a F-05 | 1 | Datos comerciales, lotes e inventario. |
| Rutas, frío, entrega y acuse | F-06 a F-09 | 1 | Pedidos y movimientos registrados. |
| Efectivo y retiro sanitario | F-10 y F-11 | 1 | Entregas, cobros y lotes. |
| Portal e intercambio electrónico | F-12 y F-13 | 2 | Pedidos y entregas disponibles. |
| Costo de servir | F-14 | 2 | Hechos operacionales por entrega. |

La captura precede a la explotación de los datos. Sin registrar el lote en recepción, el retiro sanitario no puede reconstruir sus destinos. Sin vincular pedido, entrega y cobro, la conciliación conserva las discontinuidades actuales. La analítica necesita esos hechos antes de producir un costo individual confiable. Por ello, la Etapa 1 concentra captura y continuidad, y la Etapa 2 usa esa base para nuevos canales y análisis.

La justificación de cada grupo de familias es la siguiente:

- F-01 a F-05 (preventa, recepción, bodega, preparación y cross-docking), Etapa 1. Son la puerta de entrada de los datos. Sin lote en recepción no hay retiro sanitario; sin stock confiable la preventa sigue prometiendo productos agotados; y sin medir la transferencia en las plataformas la brecha de 16 horas del cross-docking sigue sin explicación.

- F-06 a F-09 (rutas, frío, entrega y acuse), Etapa 1. Las rutas se adelantan por la jubilación del planificador. El frío y la entrega sostienen dos resultados sanitarios y comerciales que el caso fija sin margen, y el acuse de la guía cierra el ciclo documental que hoy se pierde en el 1,1 % de los casos.

LafroX SpA

Propuesta Técnica

8

---

<!-- Página 9 del PDF original -->

LafroX SpA

Introducción al Alcance de la Solución

> **[Descripción de imagen — elementos gráficos de página]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», sobre una línea horizontal gris. En el pie aparece una franja negra con borde superior naranja inclinado.

- F-10 y F-11 (efectivo y retiro sanitario), Etapa 1. Dependen de que la entrega quede registrada: la rendición vincula cada cobro con su entrega, y el retiro recorre los destinos del lote. Ambos pueden probarse en la marcha blanca de la Etapa 1.

- F-12 y F-13 (portal e intercambio electrónico), Etapa 2. Necesitan pedidos, entregas y evidencias ya confiables para exponerlos a clientes y cadenas. La principal cadena exige el pedido electrónico y el aviso de despacho desde enero de 2029, fecha compatible con la producción del mes 21.

- F-14 (costo de servir), Etapa 2. Necesita meses de hechos de entrega registrados; el cálculo básico por entrega y el costo real se habilitan juntos en la Etapa 2, con una sola definición.

La planificación de rutas permanece en la Etapa 1, como indica F-06. El Subdocumento 2 prevé una elicitación formal del conocimiento del planificador durante los primeros meses (sección «Arbitraje de tensiones operacionales y comerciales», tensión 5) y su captura en la Etapa 1 antes de la jubilación (Anexo 2.2, S-16). LafroX concreta esa decisión con talleres en los meses 1 a 3 (Anexo 3.C, S-16). El módulo M10 entrega en la Etapa 1 la medición diaria de OTIF; el costo de servir por cliente y entrega se habilita en la Etapa 2.

La asignación de cada RF y RNF está en los Anexos 3.A y 3.B y en el Formulario T-12.

### 3.2.2 Exclusiones, restricciones y supuestos

Las exclusiones del caso se registran en el Anexo 3.D: sustitución del ERP, remuneraciones, punto de venta del cliente, comercio al consumidor final, administración contractual de transportistas, rediseño de la red logística, robotización, mantenimiento mecánico y adquisición del hardware de terreno. En este último punto, el CLIENTE compra y LafroX especifica cantidades y características. Integrar a los transportistas en la operación no supone gestionar sus contratos ni sus pagos.

Cada exclusión protege el alcance de un riesgo concreto. Sustituir el ERP multiplicaría el esfuerzo con un equipo de TI de cuatro personas y pondría en riesgo la emisión tributaria; conservarlo obliga, en cambio, a una integración desacoplada que no dependa de su disponibilidad en la ventana de despacho. Excluir la compra del hardware no reduce la responsabilidad de LafroX sobre él: la especificación de cantidades y características es parte de la oferta. Excluir el diseño de la red logística no impide medir el cross-docking; al contrario, la solución entrega los datos para que el CLIENTE decida sobre su red con evidencia.

El acuse de recibo de la guía de despacho respeta que el ERP sea el único emisor tributario. En terreno se captura la evidencia de recepción: firma en pantalla o, si no es posible, fotografía, nombre del receptor o confirmación QR. La solución la envía al ERP, que registra el acuse, y recibe de vuelta su estado para conciliarlo con cada guía el mismo día (Anexo 3.A, RF-06.14). Sin señal, la evidencia queda en cola y se envía al sincronizar. Así se resuelve en la Etapa 1 la necesidad F-09 del Subdocumento 2 sin crear un segundo emisor. Mediante V-18 se confirmarán el mecanismo de acuse tributario aceptado por el CLIENTE para receptores sin firma electrónica avanzada y cómo el ERP permite consultar y conciliar su estado.

Las restricciones del Anexo 3.E mantienen el despacho de 05:30 a 07:00, la continuidad ante

LafroX SpA

Propuesta Técnica

9

---

<!-- Página 10 del PDF original -->

LafroX SpA

Introducción al Alcance de la Solución

> **[Descripción de imagen — elementos gráficos de página]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», sobre una línea horizontal gris. En el pie aparece una franja negra con borde superior naranja inclinado.

pérdida de enlace, el turno móvil sin señal, la captura en cámara a −22 °C, el canal tradicional, la incorporación de terceros y las ventanas de congelamiento. Estas condiciones impiden diseñar una solución que dependa de conexión permanente o que transfiera funciones especializadas al equipo de cuatro personas del CLIENTE.

El reemplazo modular progresivo del WMS de 2013 es una decisión ya declarada en el Subdocumento 2, Anexo 2.2, S-14, y en el inventario de sistemas legados del Anexo 2.3. La solución lo materializa en los módulos M2 y M5, preservando al ERP como fuente contable y tributaria.

El Anexo 3.C registra 41 supuestos. Los dieciséis primeros provienen de las decisiones del Subdocumento 2, Anexo 2.2. Destacan la reserva de stock al confirmar el pedido, el precio acordado al tomar el pedido, que se conserva aunque cambie posteriormente la lista de precios, el reagendamiento ante local cerrado, el control de envases por saldo y la devolución registrada en terreno. La promesa de entrega sigue el arbitraje del Subdocumento 2: 24 horas para clientes urbanos con pedidos ingresados antes de las 14:00, y 48 horas para clientes rurales, periféricos o abastecidos por cross-docking (sección «Arbitraje de tensiones operacionales y comerciales», tensión 1). Esta promesa es distinta de la ventana de 30 minutos del canal moderno. Una excursión térmica menor y transitoria genera una alerta preventiva en cabina; ante una excursión crítica y sostenida, el sistema bloquea preventivamente el lote y notifica a Calidad, que decide su liberación, bloqueo o rechazo (Anexo 2.2, S-04).

### 3.2.3 Catálogo de requerimientos y correspondencia

El catálogo funcional ofertado suma 175 requerimientos: 134 del caso, 34 derivados de las Bases Técnicas Transversales y 7 requisitos propios de LafroX (Tabla 3.A.3b). Además, 6 materias funcionales no se ofertan como función independiente: una no se oferta con su fundamento y cinco las absorbe un requisito transversal (Tabla 3.A.3a). Por eso el Formulario T-12 tiene 181 filas RF. El catálogo no funcional ofertado suma 86 requerimientos: 24 del caso, 58 de las Bases y 4 propios de LafroX (Tabla 3.A.5b). A ellos se agregan 1 alias y 3 materias absorbidas por un requisito transversal (Tabla 3.A.5a), por lo que el T-12 tiene 90 filas RNF. Cada requerimiento funcional tiene actor, descripción, precondición, resultado esperado, prioridad, origen y etapa, como exige la sección 17.1 del caso. Cada requerimiento no funcional indica materia, umbral, verificación prevista, prioridad, etapa y origen.

La Tabla 3.A.2 relaciona las catorce familias del Subdocumento 2 con los requerimientos detallados (los indicadores de gestión de la Etapa 1 se agrupan aparte, porque el Subdocumento 2 no les asigna familia), y la Tabla 3.A.5a hace lo mismo con sus cinco condiciones rectoras. La numeración RF-xx.yy no coincide con la de las familias F-xx. Cinco identificadores coinciden en número con significado distinto (RF-14.01 a RF-14.05: telemetría en el caso y seguridad en las Bases).

La prioridad usa la escala Crítica, Alta y Media del Subdocumento 2, Anexo 2.1, con una regla explícita: un requerimiento funcional del caso no supera la prioridad de su familia en ese anexo, y «Crítica» se reserva a lo que sostiene un límite del capítulo 18, una restricción del capítulo 10, un hito externo de la sección 13.2 o una condición rectora del Subdocumento 2. El

LafroX SpA

Propuesta Técnica

10

---

<!-- Página 11 del PDF original -->

LafroX SpA

Introducción al Alcance de la Solución

> **[Descripción de imagen — elementos gráficos de página]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», sobre una línea horizontal gris. En el pie aparece una franja negra con borde superior naranja inclinado.

resultado es de 54 requerimientos críticos, 157 altos y 39 medios sobre los 250 del catálogo. Los once requisitos propios ofertados (7 funcionales de la Tabla 3.A.3b y 4 no funcionales de la Tabla 3.A.5b) siguen la misma regla: 2 críticos, 5 altos y 4 medios. El Formulario T-12 responde cada requerimiento con componente, sección, prueba prevista y criterio de aceptación. El paquete de trabajo de cada uno se asigna en el plan de trabajo de la oferta.

### 3.2.4 Reglas de negocio y consultas

Las reglas del Anexo 3.G fijan el uso operacional de las capacidades. El stock se reserva al confirmar en el servidor central y un pedido capturado sin señal toma su lugar al sincronizar. La excepción de crédito queda registrada con su autor. El local cerrado se reagenda; si el cliente continúa ausente, la mercadería retorna al centro de distribución con trazabilidad. Las devoluciones se transmiten al ERP, que emite la nota de crédito cuando corresponde. Los envases se controlan por saldo de cliente y transportista. La regla de excursión térmica gradúa la respuesta: alerta en cabina ante una excursión menor y bloqueo preventivo del sistema ante una crítica y sostenida; la disposición final es de Calidad; así se preserva la continuidad sin delegar una decisión sanitaria al conductor.

Cinco reglas concentran las decisiones más sensibles del caso, y cada una responde a un conflicto registrado en el Subdocumento 2:

- Reserva de stock (RNG-01). La reserva firme se realiza al confirmar el pedido en el servidor central, por orden de recepción y con correlativo de desempate. Un pedido capturado sin señal utiliza stock indicativo y entra en ese orden al sincronizar. Si dos preventistas solicitan el mismo producto y el stock no alcanza para ambos, se reserva según ese orden y se notifica el quiebre al preventista cuyo pedido no puede cubrirse.

- Excursión térmica (RNG-04). La respuesta se gradúa: advertencia ante una excursión menor y transitoria, y retención preventiva del lote ante una crítica y sostenida. La disposición final es siempre de Calidad. La regla evita tanto el bloqueo ciego que teme Operaciones como la liberación sin evidencia que teme Calidad.

- Corte y promesa (RNG-15). Un pedido urbano ingresado antes de las 14:00 se promete a 24 horas; uno rural, periférico o abastecido por cross-docking, a 48 horas. La regla reemplaza la promesa de 24 horas a todo evento que Operaciones considera imposible.

- Efectivo y rendición. Cada cobro queda asociado a su entrega en el momento en que ocurre, con comprobante para el cliente. La rendición no se cierra con diferencias sin causal ni responsable. La regla no elimina el efectivo del canal tradicional; elimina la imposibilidad de saber en qué entrega se produjo el descuadre.

- Local cerrado y reentrega (RNG-05). El conductor registra el intento y la entrega se reagenda a la siguiente ventana disponible; no se entrega a terceros. Si el cliente continúa ausente, la mercadería retorna al centro de distribución con trazabilidad del evento. La regla convierte cada reentrega en un evento con causa, que alimenta el OTIF y, en la Etapa 2, el costo de servir del cliente.

LafroX SpA

Propuesta Técnica

11

---

<!-- Página 12 del PDF original -->

LafroX SpA

Introducción al Alcance de la Solución

> **[Descripción de imagen — elementos gráficos de página]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», sobre una línea horizontal gris. En el pie aparece una franja negra con borde superior naranja inclinado.

El Anexo 3.H registra 18 consultas con su pregunta, efecto en el alcance, supuesto de oferta y responsable. Tres se dirigen al mandante porque tratan diferencias internas de las Bases: la suma del Formulario T-21, el número de ambientes y la compatibilización formal del calendario contractual del Art. 17° con las ventanas de prohibición de pasos a producción de la sección 13.3 del caso cuando la fecha de inicio ubica un paso a producción en septiembre o diciembre. LafroX adopta cinco ambientes (DEV, QA, PREPROD, PROD y DR), en coherencia con el Subdocumento 1, sección «Presentación de la empresa». El universo de instalaciones difiere entre las entrevistas (cinco) y la volumetría (seis) del caso; la solución se parametriza por sitio y se confirma en el mes 1.

### 3.2.5 Criterios de aceptación

El Anexo 3.J fija meta, momento y método para los dieciséis resultados del capítulo 18 del caso. Entre los límites expresos están obtener la lista de clientes afectados por lote en menos de dos horas, registrar lote en el 100 % de las recepciones que lo requieren, mantener registro térmico continuo, no perder ni duplicar pedidos por falta de señal y generar la ruta siguiente en menos de veinte minutos.

La Tabla 3.3 relaciona los tres problemas con resultados verificables. Distingue los límites fijados por el CLIENTE de las metas que corresponden al proponente.

Tabla 3.3 Síntesis de resultados de aceptación. Fuente: caso, cap. 18; Anexo 3.J.

| Problema | Resultado exigido | Meta | Registro |
| --- | --- | --- | --- |
| Trazabilidad sanitaria | Clientes afectados por lote con evidencia. | Menos de 2 horas (caso). | R18-01 |
| Confiabilidad del servicio | OTIF medido de una sola forma. | 90 % mes 15; 93 % mes 19; 95 % mes 32 (metas propias de LafroX; referencia del caso: sobre 95 %). | R18-04 |
| Costo desconocido | Costo por cliente y entrega desde los hechos. | 100 % de entregas costeadas (caso). | R18-11 |

La verificación de los resultados críticos se diseña para que la Contraparte Técnica firme sobre evidencia y no sobre declaraciones:

- Retiro sanitario (R18-01): Se ejecuta un simulacro con un lote real elegido por Calidad sin aviso previo. Se mide el tiempo desde la solicitud hasta la lista de clientes afectados con guía, fecha y cantidad, y se contrasta la lista con los registros de despacho. La evidencia es el archivo exportado y el acta del simulacro.

LafroX SpA

Propuesta Técnica

12

---

<!-- Página 13 del PDF original -->

LafroX SpA

Introducción al Alcance de la Solución

> **[Descripción de imagen — elementos gráficos de página]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», sobre una línea horizontal gris. En el pie aparece una franja negra con borde superior naranja inclinado.

- Lote en recepción (R18-02): Se comparan las recepciones del período con los productos que exigen lote. El resultado es un porcentaje con numerador y denominador trazables, no una muestra.

- Registro térmico (R18-03): Durante la marcha blanca se auditan las series térmicas de cámaras y vehículos con frío y se comprueba que el CLIENTE pueda consultarlas e identificar la cámara o vehículo, fecha y hora de cada lectura. Una brecha en la serie constituye incumplimiento, aunque las lecturas disponibles estén dentro del rango.

- Pedidos sin señal (R18-06): Se ejecuta una prueba de desconexión de 14 horas con dispositivos reales y se concilia pedido por pedido lo capturado con lo recibido en el servidor. El criterio es cero pérdidas y cero duplicados.

- Ruta del día siguiente (R18-07): Se mide diariamente el tiempo de generación y se registra cada corrección manual con su motivo. Las correcciones alimentan la parametrización de las reglas del planificador.

- Rendición (R18-10): Se verifica que cada diferencia del día tenga causal y responsable antes del cierre, y que la suma de los cobros por entrega cuadre con lo depositado.

La aceptación exige demostrar resultados, no solo disponibilidad de pantallas. Un reporte de lotes sin evidencia no satisface R18-01, y registrar pedidos sin comprobar la reconciliación no acredita R18-06. La meta de OTIF parte del 82,4 % actual (Subdocumento 2, Tabla 2.1) y alcanza el 95 % en el mes 32, como compromiso propio de LafroX. El caso señala como referencia un valor superior al 95 % y establece como criterio de aceptación alcanzar la meta comprometida por el proponente. Se fija un año después de la producción de la Etapa 2 (mes 21) porque requiere las dos etapas estabilizadas: rutas, preventa y entrega de la Etapa 1, y pedido electrónico y aviso de despacho de la Etapa 2, operando durante un ciclo anual completo que incluya los peaks de septiembre y diciembre. La ventana de 30 minutos que exigirá la principal cadena desde enero de 2029 no depende de este tramo: se mide con su propio indicador de llegada dentro de la ventana (Anexo 3.A, RF-12.10 y RF-12.11) desde la Etapa 2. Los tramos intermedios son propios de LafroX y siguen la entrada de las capacidades:

- 90 % al cierre de la marcha blanca de la Etapa 1 (mes 15), con preventa con stock y crédito visibles y rutas generadas por el sistema, todavía en convivencia con el papel.

- 93 % en el mes 19, tras tres meses de producción sin papel.

- 95 % en el mes 32, tras un ciclo anual completo con ambas etapas en producción.

La línea base de 82,4 % se mide hoy de forma distinta por cada área. Si la medición con la definición única de S-01 arroja otra cifra, los tramos se recalculan en el comité del mes 1 conservando la meta final (Anexo 3.C, S-01; Anexo 3.H, V-10).

El caso no fija la meta de pérdida de envases (R18-12) ni el umbral de ocupación (R18-14), y el CLIENTE no ha declarado un valor. LafroX formula ambos como supuestos de oferta, que se validan en el mes 2 (Anexo 3.C, S-26 y S-27):

- R18-12: pérdida anual de envases no superior al 7 % del parque, conforme al Subdocumento

LafroX SpA

Propuesta Técnica

13

---

<!-- Página 14 del PDF original -->

LafroX SpA

Introducción al Alcance de la Solución

> **[Descripción de imagen — elementos gráficos de página]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», sobre una línea horizontal gris. En el pie aparece una franja negra con borde superior naranja inclinado.

2, Tabla 2.1; la línea base es el 14 % estimado del parque al año. Una revisión de la línea

base no modifica esa meta.

- R18-14: cada camión sale a reparto con una ocupación mínima del 60 % de su capacidad volumétrica útil, incluidas las rutas rurales y sin excepciones. La ocupación promedio supera el 68 % actual, cumpliendo simultáneamente las restricciones de peso y condición térmica y la promesa de entrega de S-21. Cada resultado lo acepta la Contraparte Técnica en el acta de cierre de la marcha blanca. La pérdida anual de envases solo puede medirse sobre un año: R18-12 se acepta de forma provisional en ese cierre, con el saldo conciliado, y de forma definitiva tras 12 meses de operación. Lo mismo ocurre con el tramo final de OTIF, que se confirma en el mes 32 (Anexo 3.J).

## 3.3 Esquema de solución

Los siguientes esquemas representan el modelo conceptual de la solución: procesos, módulos y circulación de información. No representan capas técnicas ni emplazamiento físico. Cada figura se describe mediante sus elementos y relaciones, y se explica después.

### 3.3.1 Vista conceptual del ciclo logístico

La Figura 3.1 conecta la captura comercial con la ejecución y el cierre, e indica el módulo responsable de cada capacidad. Los pedidos confirmados alimentan la planificación; la asignación y secuencia de ruta orientan la preparación y la carga. El reparto puede salir directamente del centro de distribución o pasar por una plataforma de cross-docking. Las líneas continuas muestran relaciones operacionales y las discontinuas, intercambios con el ERP.

La figura muestra por qué la analítica depende de la captura en terreno: el costo de servir necesita hechos de entrega, no solamente totales contables. Los pedidos capturados sin señal ingresan a la planificación una vez confirmados; la reserva central se explica en la sección 3.3.3. La preparación envía al ERP cantidades y lotes para la emisión de la guía de despacho (RF-05.06); la entrega aporta la evidencia de recepción y recibe el estado del acuse. Las devoluciones aportan los datos para que el ERP emita la nota de crédito cuando corresponda. El ERP conserva la emisión tributaria.

### 3.3.2 Trazabilidad y cadena de frío

La Figura 3.2 representa la continuidad del lote y del registro térmico. Su propósito es conservar el vínculo entre recepción, movimiento y destino para responder a un retiro sanitario.

La consulta necesita relacionar movimientos y clientes; las lecturas térmicas aportan la evidencia del manejo del producto. Ante una excursión menor, el conductor recibe una alerta en cabina; ante una crítica y sostenida, el sistema retiene preventivamente el lote y notifica a Calidad, que registra la liberación, el bloqueo o el rechazo con su fundamento (Subdocumento 2, arbitraje, tensión 2).

LafroX SpA

Propuesta Técnica

14

---

<!-- Página 15 del PDF original -->

LafroX SpA

Introducción al Alcance de la Solución

> **[Descripción de imagen — elementos gráficos de página]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», sobre una línea horizontal gris. En el pie aparece una franja negra con borde superior naranja inclinado.



> **[Descripción de imagen — Figura 3.1; nota de conversión]**
> Diagrama en blanco y negro con once recuadros de esquinas redondeadas. En la parte superior aparecen preventa, canal moderno y portal, y recepción e inventario. Las dos primeras capacidades envían pedidos confirmados a planificación de rutas; recepción e inventario conduce a preparación y carga. Planificación envía la asignación y secuencia de carga a preparación. Desde preparación salen dos caminos hacia entrega digital: reparto directo y vía plataforma, pasando este último por cross-docking. Entrega se conecta con devoluciones y envases, rendición y análisis; rendición también conduce a análisis. Las flechas continuas representan relaciones operacionales. Las líneas discontinuas conectan preparación con ERP (A), entrega con ERP en ambos sentidos (B) y devoluciones con ERP mediante datos de devolución. Los cruces de líneas no representan una conexión. Bajo el diagrama aparece la explicación de esos intercambios.

- Preventa (M3) Stock y crédito; 24/48 h

- Canal moderno y portal (M11, E2)

- Recepción e inventario (M1, M2) Lote y FEFO

- Planificación de rutas (M4) Ruta corregible

- Preparación y carga (M5) Olas y faltantes

- Cross-docking (M2) Recepción desconsolidación y despacho

- Entrega digital (M6) POD, cobro y acuse

- ERP conservado Registro contable; único emisor tributario

- Devoluciones y envases (M8)

- Rendición (M7) Conciliación de efectivo

- Análisis (M10) OTIF E1; costo de servir E2

- Pedidos confirmados

- Pedidos confirmados

- Asignación y secuencia de carga

- Reparto directo

- Vía plataforma

- A

- B

- Datos de devolución

Intercambios con el ERP (líneas discontinuas): A: preparación → ERP, detalle preparado para emisión de GDE. B: entrega → ERP, evidencia de recepción; ERP → entrega, estado del acuse. Las líneas continuas muestran relaciones operacionales; los cruces de líneas no representan una conexión.

Figura 3.1 Relación conceptual de capacidades y módulos. Fuente: elaboración propia a partir del Subdocumento 2, Anexo 2.1.

> **[Descripción de imagen — Figura 3.2; nota de conversión]**
> Diagrama en blanco y negro con cinco recuadros rectangulares. Recepción, con lote y vencimiento, conduce a bodega y preparación, con movimientos del lote, y a consulta sanitaria, con origen y clientes afectados. Bodega y preparación conduce a transporte y entrega, con destino y evidencia; transporte y entrega conduce a consulta sanitaria. Un recuadro ancho inferior representa el registro continuo de temperatura en cámaras y vehículos y envía flechas a consulta sanitaria y a transporte y entrega.

- Recepción Lote y vencimiento

- Bodega y preparación Movimientos del lote

- Consulta sanitaria Origen y clientes afectados

- Transporte y entrega Destino y evidencia

- Registro continuo de temperatura en cámaras y vehículos

Figura 3.2 Información necesaria para trazabilidad sanitaria. Fuente: elaboración propia a partir del caso, cap. 18, criterios 1 a 3.

LafroX SpA

Propuesta Técnica

15

---

<!-- Página 16 del PDF original -->

LafroX SpA

Introducción al Alcance de la Solución

> **[Descripción de imagen — elementos gráficos de página]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», sobre una línea horizontal gris. En el pie aparece una franja negra con borde superior naranja inclinado.

### 3.3.3 Continuidad e integración

La Figura 3.3 distingue los ámbitos cuya operación debe sostenerse ante pérdida de conectividad y su relación con la nube. El ERP conserva su responsabilidad contable y tributaria.

> **[Descripción de imagen — Figura 3.3; nota de conversión]**
> Diagrama en blanco y negro con cuatro recuadros dispuestos en dos filas y dos columnas. Arriba se muestran preventa y reparto, con un turno sin señal de 14 horas, y carga principal en nube, con intercambio de información. Abajo aparecen el centro de distribución, con autonomía de al menos 24 horas, y el ERP conservado, con registro contable y emisión. Flechas discontinuas de doble sentido conectan la nube con preventa y reparto, bajo el rótulo «Reconexión», y con el centro de distribución. Una flecha continua de doble sentido conecta la nube con el ERP. La figura no representa una topología física.

- Preventa y reparto Turno sin señal: 14 horas

- Carga principal en nube Intercambio de información

- Centro de distribución Autonomía: al menos 24 horas

- ERP conservado Registro contable y emisión

- Reconexión

Figura 3.3 Ámbitos de continuidad e intercambio, sin topología física. Fuente: elaboración propia; BA, art. 16; caso, cap. 10 y 15.

La autonomía evita que un corte detenga la captura; la sincronización posterior reconcilia los registros sin perder ni duplicar pedidos. El caso exige que el dispositivo sincronice tras el turno en no más de diez minutos y el centro tras un corte de 24 horas en no más de dos horas. Se usa el código RT-03.12 de las Bases Técnicas Transversales para la sincronización y se registra el valor del caso.

La plataforma conserva una cola local e idempotente de transacciones, de modo que la reconexión reconcilia cada registro por su identificador único y deja una bitácora de conflictos. La reserva firme ocurre en el servicio central al confirmar; la consulta sin conexión muestra la antigüedad del dato y no promete stock antes de esa confirmación. Los protocolos y componentes se especifican en la arquitectura de la oferta.

Un corte de enlace de 24 horas en un centro de distribución recorre tres momentos. Durante el corte, el borde local sigue recibiendo, preparando y despachando, con el stock y las reglas vigentes al momento de la desconexión; las transacciones quedan en cola con su identificador único. Al volver el enlace, la cola se envía en orden y cada registro se reconcilia con la nube. Al restablecerse el enlace, los conflictos se reconcilian automáticamente conforme a la regla determinista documentada, sin sobrescritura silenciosa de conflictos de versión y con una bitácora auditable de las decisiones aplicadas. Después, los indicadores del día se recalculan con los datos completos. El mismo patrón rige para un turno de preventa o reparto de 14 horas sin señal. La fibra se corta cuatro veces al año y Concepción no tiene respaldo, de modo que este comportamiento no es una contingencia excepcional, sino una condición normal de operación que se prueba antes de cada paso a producción.

## 3.4 Explicación de la Solución

La solución se interpreta a través de la jornada de Puelche y de los actores identificados en el Subdocumento 2. Su valor depende de que la información se capture donde ocurre la operación y pueda seguirse hasta los resultados del CLIENTE.

LafroX SpA

Propuesta Técnica

16

---

<!-- Página 17 del PDF original -->

LafroX SpA

Introducción al Alcance de la Solución

> **[Descripción de imagen — elementos gráficos de página]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», sobre una línea horizontal gris. En el pie aparece una franja negra con borde superior naranja inclinado.

### 3.4.1 Aplicación en la jornada operacional

En recepción se captura lote y vencimiento antes de perder el vínculo con el producto. Bodega usa esa información para FEFO y preparación por olas; los faltantes registran su causa cuando se producen. La preparación nocturna y el despacho concentrado exigen que la captura local continúe durante un corte del enlace (Anexo 2.1, F-02 a F-05).

En la calle, el preventista consulta stock y crédito al registrar el pedido y ve la promesa de entrega que corresponde al cliente. El conductor registra la entrega, el cobro y el acuse con o sin señal. Al recuperar conectividad, los registros se integran sin duplicación. El almacenero conserva su forma de compra y pago; la aplicación no presupone que tenga un teléfono o una conexión propia.

Al cerrar la operación, la rendición vincula cobros con entregas y explica las diferencias con causal y responsable antes del cierre. Se mantiene la posibilidad de pagar en efectivo y su reducción se apoya en medios alternativos voluntarios. Calidad puede reconstruir los destinos de un lote. En la segunda etapa, la información registrada permite calcular el costo de servir y alimentar los nuevos canales. Los clientes no rentables se segmentan para revisar frecuencia y pedido mínimo; no se eliminan automáticamente (Subdocumento 2, Anexo 2.2, S-06 y S-07).

La jornada completa muestra cómo se encadenan las capacidades:

- 22:00 a 06:00, bodega. Los preparadores reciben las olas en su dispositivo y confirman cada línea por lectura. En la cámara a −22 °C trabajan con guantes, sin señal, con la sincronización diferida al salir. Un faltante se registra con su causa en el momento. Si el enlace de Talca o Concepción se corta, el borde del centro de distribución sostiene la preparación y la carga, y la reconciliación con la nube ocurre al volver el enlace.

- Madrugada, cross-docking. El camión de línea llega a cada plataforma y sus unidades se leen a la llegada y al cargarse en el reparto. Queda medido cuánto dura cada tramo y qué excepciones ocurren, que es la información que hoy falta para explicar la brecha de 16 horas.

- 05:30 a 07:00, despacho. Salen los 96 camiones. La ventana no admite indisponibilidad; por eso ningún cambio se despliega en ella y la operación local no depende del enlace.

- Durante el día, calle. El preventista toma pedidos con stock y crédito a la vista y la promesa que corresponde al cliente; sin señal, el pedido queda en cola y ocupa su lugar al sincronizar. El conductor registra entrega, evidencia, devoluciones, envases y cobro. Ante una excursión térmica menor y transitoria, el conductor recibe una advertencia; ante una crítica y sostenida, el sistema retiene preventivamente el lote y notifica a Calidad, que decide su liberación, bloqueo o rechazo.

- 15:00 a 18:30, planificación. Los pedidos confirmados quedan disponibles para la ruta del día siguiente, que se genera en minutos y el planificador corrige. Cada corrección queda registrada.

- Retorno, rendición y cierre. Al volver, el camión rinde contra sus cobros por entrega; toda diferencia tiene causal antes de cerrar. La evidencia de entrega ya está en el ERP, que registra el acuse de cada guía.

LafroX SpA

Propuesta Técnica

17

---

<!-- Página 18 del PDF original -->

LafroX SpA

Introducción al Alcance de la Solución

> **[Descripción de imagen — elementos gráficos de página]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», sobre una línea horizontal gris. En el pie aparece una franja negra con borde superior naranja inclinado.

Si en cualquier momento se detecta un lote sospechoso, Calidad obtiene los destinos con guía, fecha y cantidad, y el retiro se ejecuta sobre clientes identificados, no sobre estimaciones.

### 3.4.2 Correspondencia con la arquitectura lógica

La Tabla 3.4 vincula capacidades y módulos de negocio. Los nombres M1 a M12 son los que usa la arquitectura lógica de la oferta.

Tabla 3.4 Correspondencia entre capacidades del alcance y módulos lógicos. Fuente: elaboración propia.

| Capacidad | Módulo | Resultado que habilita | Etapa |
| --- | --- | --- | --- |
| Recepción, lote y vencimiento | M1 Recepción | Trazabilidad de ingreso y calidad de datos. | 1 |
| Inventario, FEFO, reposición, cross-docking y preparación | M2 Inventario; M5 Preparación | Stock confiable y despacho controlado. | 1 |
| Preventa y ruteo | M3 Preventa; M4 Rutas | Pedido confirmable y ruta corregible. | 1 |
| Entrega, acuse, cobro y retorno | M6 Reparto; M7 Cobranza y rendición; M8 Devoluciones y envases | POD, conciliación y control de envases. | 1 |
| Calidad, evidencia y flota | M9 Calidad y trazabilidad; M12 Telemetría | Retiro sanitario y control de cadena de frío. | 1 |
| Gestión y nuevos canales | M10 Analítica; M11 Canal moderno | OTIF diario, costo de servir e intercambio estructurado. | 1 / 2 |

La tabla permite verificar que cada flujo de la sección 3.3 tiene una responsabilidad lógica. M10 entrega los indicadores operacionales de la Etapa 1 y el costo de servir en la Etapa 2; M11 se incorpora con el canal moderno en la segunda etapa. Los requerimientos transversales de las Bases se asignan a la base compartida (Formulario T-12).

### 3.4.3 Implementación

La implementación construye primero la base compartida: identidad, integración con el ERP, registro auditable, operación desconectada y observabilidad. Sobre ella trabajan tres frentes en la Etapa 1: bodega y calidad (M1, M2, M5, M9, M12); preventa, rutas y reparto (M3, M4, M6, M8); y datos y rendición (M7, M10). La Etapa 2 agrega el frente de canal moderno y costo de servir (M11 y M10).

LafroX SpA

Propuesta Técnica

18

---

<!-- Página 19 del PDF original -->

LafroX SpA

Introducción al Alcance de la Solución

> **[Descripción de imagen — elementos gráficos de página]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», sobre una línea horizontal gris. En el pie aparece una franja negra con borde superior naranja inclinado.

Cada incremento recorre el mismo camino. Parte de un conjunto de requerimientos del Anexo 3.A con su criterio de aceptación. Se desarrolla en una rama versionada junto con su configuración y sus reglas parametrizables. Pasa por revisión de pares y por pruebas automatizadas en la cadena de integración continua, con un umbral bloqueante de 80 % de cobertura de pruebas unitarias (Subdocumento 1, sección «Gobierno interno Calidad, Seguridad y Conocimiento»), superior al 70 % mínimo de las Bases (RT-04.11). Luego se promueve por los ambientes DEV, QA y PREPROD. En PREPROD se ejecutan las pruebas del perfil operacional: desconexión de 14 horas para preventa y reparto, corte de 24 horas para el CD y uso con guantes a −22 °C.

Un incremento no se promueve a producción si tiene defectos críticos o altos abiertos, si la sincronización pierde o duplica registros, o si cae dentro de una ventana de congelamiento. Durante los meses 13 a 20, los cambios de la Etapa 2 se despliegan fuera de la ventana de despacho y sin modificar las funciones estabilizadas de la Etapa 1. La metodología completa y el plan de trabajo se detallan en los capítulos correspondientes de la oferta.

El orden de construcción sigue las dependencias de datos. Primero se estabilizan los datos maestros de productos, clientes e instalaciones, porque todo requerimiento posterior los usa. Luego se construyen recepción e inventario, que alimentan la preparación y el retiro sanitario; en paralelo avanza la preventa, que necesita stock y crédito. Rutas y reparto se integran cuando el pedido confirmado y la preparación existen, y la rendición cuando existe la entrega registrada. En la Etapa 2, el canal moderno reutiliza pedidos, guías y evidencias ya probadas, y el costo de servir usa los hechos acumulados desde la marcha blanca de la Etapa 1. Este orden permite probar cada incremento con datos reales de su predecesor, en lugar de simularlos.

### 3.4.4 Implantación

La implantación respeta las siete condiciones de la sección 13.3 del caso; la condición 2 (ningún paso a producción en septiembre, diciembre ni los tres primeros días hábiles) se resuelve en la sección 3.1.2. Cada proceso convive con la forma actual de trabajar durante la marcha blanca, con conciliación entre ambos registros y posibilidad de volver atrás. El despliegue se hace por proceso, sitio o zona, considera el turno nocturno y capacita en terreno sin detener venta ni reparto. La incorporación de cada transportista requiere un acuerdo operacional propio.

La secuencia comienza por datos maestros y trazabilidad de recepción, continúa por bodega y preparación, y culmina con preventa, reparto y rendición por zonas. En cada ola se define cuál es el registro oficial. Mientras dura la convivencia, la hoja de picking impresa y la guía en papel siguen siendo el respaldo; se retiran cuando la ola cumple su criterio de avance durante cuatro semanas consecutivas a volumen real.

El criterio de avance de una ola exige:

- Ausencia de defectos críticos o altos abiertos;

- Conciliación diaria sin diferencias no explicadas;

LafroX SpA

Propuesta Técnica

19

---

<!-- Página 20 del PDF original -->

LafroX SpA

Introducción al Alcance de la Solución

> **[Descripción de imagen — elementos gráficos de página]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», sobre una línea horizontal gris. En el pie aparece una franja negra con borde superior naranja inclinado.

- Volumen real de operación comprometido alcanzado e indicadores de disponibilidad y tiempo de respuesta cumplidos de forma sostenida durante al menos las cuatro últimas semanas;

- Criterios de aceptación correspondientes al alcance de la ola verificados según los métodos y períodos del Anexo 3.J, con aceptación provisional cuando corresponda y verificación definitiva al completar el período previsto;

- Usuarios certificados por perfil;

- Acta firmada por la Contraparte Técnica.

La reversión la autoriza el responsable operativo del CLIENTE cuando un indicador amenaza el despacho. Su disparador es observable: pedidos sin sincronizar al inicio de la carga, rutas del día no disponibles para cargar o un defecto crítico en la ventana de despacho. La vuelta al procedimiento anterior debe completarse antes de las 05:30. Por eso se decide en el turno de noche, con la hoja de picking y la guía en papel disponibles. Los registros capturados durante la ola permanecen en cola y se concilian al retomar; no se pierden. Este tiempo de vuelta no es el RTO de la sección 3.4.5: es el plazo para no afectar el despacho.

Después de cada paso a producción, la estabilización incluye presencia en bodega durante el turno de noche y acompañamiento en ruta a preventistas y conductores. Su duración es de cuatro semanas por ola, el mismo período que exige el criterio de avance. La dotación se deriva de la operación del caso:

- Bodega: la preparación es nocturna, de 22:00 a 06:00, en Talca y Concepción. Se asigna una persona de LafroX por centro de distribución en cada turno de noche de la ola, es decir, dos personas. Cada plataforma de cross-docking recibe una persona durante la recepción de madrugada y el despacho de la mañana en su ola, es decir, tres personas.

- Calle: cada día salen 96 camiones y trabajan 62 preventistas, lo que suma 158 rutas diarias. Para acompañar cada ruta al menos una vez en las cuatro semanas (24 días de lunes a sábado) se necesitan 158 / 24 ≈ 6,6 personas. Se asignan siete acompañantes en ruta durante las olas de preventa y reparto. Si la ola cubre solo una zona, la dotación se reduce en proporción a sus rutas.

- Coordinación: el Líder de Implantación coordina a este equipo y reporta el avance de cada ola al comité.

Los conductores externos se incorporan en el andén al asignarse a una ruta, con un mecanismo que sobrevive a la rotación sin aviso.

La adopción se mide por perfil y por ola con los indicadores del Anexo 3.I. La meta es que el 100 % de los usuarios de la ola esté certificado en su perfil y que el 100 % de las transacciones de la ola se registre en la solución al retirar el papel. Si una ola no alcanza esa meta, no avanza y se extiende el acompañamiento. El plan distingue dos grupos:

- Personal con 20 o 30 años en la compañía: acompañamiento individual en su puesto o ruta, y reconocimiento formal de su conocimiento. El caso advierte que un proyecto que pase por encima de estas personas fracasará.

LafroX SpA

Propuesta Técnica

20

---

<!-- Página 21 del PDF original -->

LafroX SpA

Introducción al Alcance de la Solución

> **[Descripción de imagen — elementos gráficos de página]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», sobre una línea horizontal gris. En el pie aparece una franja negra con borde superior naranja inclinado.

- Personal rotativo de preparación (38 % anual): aprendizaje en el puesto de dos horas como máximo (RNF-05.03) y un tutor por turno.

La migración de datos acompaña la secuencia de olas. El WMS de 2013 opera en Talca y Concepción usa planillas (Subdocumento 2, Anexo 2.3). En Talca se migran los saldos por SKU, ubicación y lote de sus 11.400 posiciones. En Concepción se cargan los saldos desde un conteo físico. En ambos casos el maestro cubre los 8.400 SKU activos, 1.100 de ellos refrigerados o congelados. Cada sitio sigue el mismo procedimiento:

- Carga inicial en PREPROD.

- Conciliación contra un conteo físico, separada por dominio: los documentos y los lotes deben coincidir sin diferencias; las diferencias de inventario se investigan y los ajustes se justifican antes del corte. El 2,3 % del valor contado es la línea base del problema descrito en el Subdocumento 2, Tabla 2.1, y no una tolerancia automática de migración (Anexo 3.C, S-29). Las diferencias se clasifican en conteo físico, saldo inicial, lote o error de migración y se presentan a la Contraparte Técnica con su explicación.

- Corte fuera de las ventanas de congelamiento.

El WMS se conserva en solo lectura hasta el cierre de la marcha blanca del sitio como respaldo de consulta (Anexo 3.C, S-14). La vía operacional de reversión es el procedimiento manual con hoja de picking y guía en papel descrito arriba; el CLIENTE conserva la autoridad sobre los datos, y las transacciones del período se concilian al retomar. La reversión se ensaya en PREPROD antes de cada corte.

### 3.4.5 Operación

La operación cubre los 36 meses contractuales y complementa al equipo de cuatro personas del CLIENTE con monitoreo, gestión de incidentes, continuidad, seguridad, datos y evolución controlada. Distingue dos servicios. El centro de operaciones de red monitorea la plataforma 24×7 (RNF-21.01). Los incidentes críticos y altos se atienden 24×7×365, con respuesta en 15 minutos y 1 hora, y resolución en 4 y 8 horas, respectivamente. La atención general de la mesa de servicio es de 04:00 a 22:00 de lunes a sábado, con cobertura 24×7 en septiembre y diciembre (RT-21.06). La atención incluye un canal asistido para clientes tradicionales; la autoatención no se impone como condición para recibir soporte.

La Tabla 3.5 resume los objetivos de servicio de la operación.

LafroX SpA

Propuesta Técnica

21

---

<!-- Página 22 del PDF original -->

LafroX SpA

Introducción al Alcance de la Solución

> **[Descripción de imagen — elementos gráficos de página]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», sobre una línea horizontal gris. En el pie aparece una franja negra con borde superior naranja inclinado.

Tabla 3.5 Objetivos de servicio. Fuente: BA, art. 78.2; BTT, secciones 7.2 y 10; caso, cap. 10 y 15.

| Servicio | Indicador | Objetivo | Medición |
| --- | --- | --- | --- |
| Infraestructura | Disponibilidad mensual | ≥ 99,95 % | Mensual, por componente. |
| Transacción crítica | Disponibilidad mensual | ≥ 99,9 % | Mensual, de extremo a extremo. |
| Despacho 05:30–07:00 | Indisponibilidad en la ventana | Cero | Diaria. |
| Recuperación | RTO / RPO de servicios críticos | ≤ 4 h / ≤ 15 min | Prueba semestral. |
| Incidentes críticos / altos | Respuesta y resolución, 24×7×365 | 15 min y 4 h / 1 h y 8 h | Por incidente; informe mensual. |

La tabla separa tres objetivos que no deben confundirse. El 99,95 % aplica a la infraestructura; el 99,9 % aplica a la transacción crítica completa; y la ventana de despacho no admite indisponibilidad, porque el caso la equipara a un día sin operación (Anexo 3.E, R-01). El RTO y el RPO rigen la recuperación ante desastres y se prueban al menos dos veces al año.

Los servicios de pedido, bodega, entrega, trazabilidad y rendición se supervisan con alertas por colas de sincronización pendientes, antigüedad de datos en dispositivos, latencia y calidad de datos. Una cola que crece fuera de lo normal antes de la carga genera una alerta al especialista de guardia. El escalamiento distingue la mesa de servicio, los especialistas de aplicación e infraestructura, y la decisión operacional del CLIENTE. La capacidad de la mesa se recalibra con los tickets observados en la marcha blanca. La transferencia de conocimiento al equipo TI del CLIENTE se hace con procedimientos de operación documentados y ensayados antes del mes 21.

La operación reconoce los peaks del caso. En las tres primeras semanas de septiembre el volumen diario pasa de cerca de 1.400 a cerca de 2.600 entregas, y diciembre y los cierres mensuales generan tensiones similares. Durante las ventanas definidas se mantiene el congelamiento de cambios. La atención general de la mesa opera de 04:00 a 22:00 de lunes a sábado y se amplía a 24×7 en septiembre y diciembre. Los incidentes críticos y altos mantienen atención 24×7×365. Durante esos períodos, la supervisión se concentra en las colas de sincronización y en la ventana de despacho. La capacidad de la plataforma se prueba antes de cada septiembre con carga superior a la del peak, y los resultados se informan al comité. Terminado cada peak, se revisan los incidentes y las alertas del período para ajustar umbrales y procedimientos antes del siguiente.

El equipo de cuatro personas del CLIENTE conserva la gestión de sus sistemas y la relación con los usuarios; LafroX aporta las especialidades permanentes que ese equipo no tiene:

LafroX SpA

Propuesta Técnica

22

---

<!-- Página 23 del PDF original -->

LafroX SpA

Introducción al Alcance de la Solución

> **[Descripción de imagen — elementos gráficos de página]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», sobre una línea horizontal gris. En el pie aparece una franja negra con borde superior naranja inclinado.

operación de nube, seguridad, datos y soporte de aplicación. Esta división evita transferir al CLIENTE funciones que el caso advierte que no puede absorber.

### 3.4.6 Participación de los grupos de interés

La estrategia de apoyo mantiene los 19 actores del Subdocumento 2, Anexo 2.3, con sus nombres. El Anexo 3.I asigna a cada uno actividad, momento, responsable LafroX, indicador y respuesta ante resistencia. Los responsables son los roles de la estructura de proyecto del Subdocumento 1, sección «Estructura para Proyecto».

El comité ejecutivo, presidido por la gerenta general, arbitra prioridades y aprueba estratégicamente el cierre de cada marcha blanca, sujeto al cumplimiento de las condiciones de aceptación y al acta firmada por la Contraparte Técnica. Operaciones y Calidad resuelven las tensiones entre continuidad y tratamiento sanitario. El planificador tiene influencia Alta e interés Muy Alto: participa desde el mes 1 en los talleres de reglas y valida las rutas propuestas. Bodega, preventistas, conductores y peonetas validan los flujos en sus condiciones reales de trabajo. El sindicato participa en la definición de finalidades y controles de privacidad de la telemetría operacional; su acuerdo previo se exige antes de utilizar GPS para control de jornada. Sin ese acuerdo se mantiene la telemetría de vehículo, ruta y carga con controles de privacidad y no se utiliza GPS para control de jornada. Clientes, proveedores y autoridad reciben evidencias e intercambios acordes a su función, sin obligaciones tecnológicas ajenas al caso (LafroX, 2026b, sección «Actores y Grupos de Interés» y Anexos 2.2 y 2.3).

La gerenta general advirtió que un proyecto que pase por encima de las personas será rechazado sin decirlo. Por eso la adopción se mide por perfil y por ola, y una ola no avanza si sus usuarios no están certificados.

La estrategia por grupo responde a las resistencias concretas que registra el caso:

- Planificador de rutas. Su conocimiento es el activo que la solución debe preservar. Los talleres de los meses 1 a 3 convierten sus reglas en parámetros que él valida, y la ruta propuesta se compara con la suya antes de reemplazarla. Se reconoce formalmente su aporte.

- Personal con 20 o 30 años en la compañía. El acompañamiento es individual y en su puesto. Sus observaciones sobre la ruta, la bodega o la caja se registran y se responden, porque el caso advierte que un proyecto que pase por encima de ellos será rechazado.

- Preparadores con rotación de 38 %. La interfaz se aprende en dos horas en el puesto, con un tutor por turno, de modo que la rotación no degrade la operación.

- Conductores de transportistas. No son trabajadores de la compañía y rotan sin aviso. Se incorporan en el andén con un mecanismo de identificación rápido, acordado con cada una de las diez empresas.

- Sindicato. No se instalan cámaras en cabina. El GPS para control de jornada requiere acuerdo previo con el sindicato. La telemetría operacional gestiona vehículo, ruta y carga con controles de privacidad, considerando que la ubicación del vehículo puede revelar la del conductor.

LafroX SpA

Propuesta Técnica

23

---

<!-- Página 24 del PDF original -->

LafroX SpA

Introducción al Alcance de la Solución

> **[Descripción de imagen — elementos gráficos de página]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», sobre una línea horizontal gris. En el pie aparece una franja negra con borde superior naranja inclinado.

- Clientes del canal tradicional. Conservan su forma de compra y pago; reciben comprobante y evidencia sin necesitar teléfono ni internet.

## Referencias

Las citas indican artículo, capítulo, sección o código de cada fuente.

- Distribuidora Puelche S.A. (2026a). Bases Administrativas de Licitación N.º TFEP-01/2026.

- Distribuidora Puelche S.A. (2026b). Bases Técnicas Transversales de Licitación N.º TFEP-01/2026.

- Distribuidora Puelche S.A. (2026c). Caso 02: Logística.

- Distribuidora Puelche S.A. (2026d). Aclaraciones de la Licitación N.º TFEP-01/2026.

- LafroX. (2026a). Subdocumento 1: Presentación de la empresa.

- LafroX. (2026b). Subdocumento 2: Comprensión del problema y de la necesidad, y sus anexos 2.1 a 2.3.

## Declaración de uso de IA

La Tabla 3.6 registra la asistencia de IA por sección, anexo y formulario. La revisión humana se registra cuando el equipo la realiza.

Tabla 3.6 Declaración de uso de IA. Fuente: registro del equipo.

| Sección | Herramienta | Finalidad | Nivel texto | Nivel diagramas | Revisión humana |
| --- | --- | --- | --- | --- | --- |
| 3.1 | Codex; Claude Code | Contraste con las Bases y redacción. | Alto | Ninguno | No documentada. |
| 3.2 | Codex; Claude Code | Contraste con las Bases y los Subdocumentos 1 y 2; redacción. | Alto | Ninguno | No documentada. |
| 3.3 | Codex; Claude Code | Descripción estructurada de las figuras. | Alto | Alto | No documentada. |
| 3.4 | Codex; Claude Code | Redacción de implementación, implantación y operación. | Alto | Ninguno | No documentada. |

continúa en la página siguiente

LafroX SpA

Propuesta Técnica

24

---

<!-- Página 25 del PDF original -->

LafroX SpA

Introducción al Alcance de la Solución

> **[Descripción de imagen — elementos gráficos de página]**
> En el encabezado aparece un pequeño contorno negro de cabeza de zorro junto a «LafroX SpA», sobre una línea horizontal gris. En el pie aparece una franja negra con borde superior naranja inclinado.

Tabla 3.6 — continuación

| Sección | Herramienta | Finalidad | Nivel texto | Nivel diagramas | Revisión humana |
| --- | --- | --- | --- | --- | --- |
| Anexo 3.A | Codex; Claude Code | Conversión del catálogo funcional. | Alto | Ninguno | No documentada. |
| Anexo 3.B | Codex; Claude Code | Conversión del catálogo no funcional. | Alto | Ninguno | No documentada. |
| Anexo 3.C | Codex; Claude Code | Redacción de supuestos. | Alto | Ninguno | No documentada. |
| Anexo 3.D | Codex; Claude Code | Redacción de registros. | Alto | Ninguno | No documentada. |
| Anexo 3.E | Codex; Claude Code | Redacción de registros. | Alto | Ninguno | No documentada. |
| Anexo 3.F | Codex; Claude Code | Redacción de registros. | Alto | Ninguno | No documentada. |
| Anexo 3.G | Codex; Claude Code | Redacción de reglas. | Alto | Ninguno | No documentada. |
| Anexo 3.H | Codex; Claude Code | Redacción de consultas. | Alto | Ninguno | No documentada. |
| Anexo 3.I | Codex; Claude Code | Redacción de la participación de actores. | Alto | Ninguno | No documentada. |
| Anexo 3.J | Codex; Claude Code | Redacción de criterios de aceptación. | Alto | Ninguno | No documentada. |
| Anexo 3.K | Codex; Claude Code | Glosario. | Medio | Ninguno | No documentada. |
| Formulario T-12 | Codex; Claude Code | Generación de la matriz de cumplimiento. | Alto | Ninguno | No documentada. |



LafroX SpA

Propuesta Técnica

25
