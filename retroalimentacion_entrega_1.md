# Retroalimentación Subdocumento 3
**3. ESQUEMA DE SOLUCIÓN Y ALCANCE — Formulario T-12 (21 %)**

Revisión: (Puntaje 20)
Rehacer el documento completo. Son 138 páginas, de las cuales 120 (87 %) son tablas de listado: catálogos, supuestos, exclusiones, restricciones y un registro de 60 decisiones que ocupa 65 páginas. Si se retira lo que por instrucción del T-21 debía ir en el Formulario T-12 o en anexos, quedan unas seis páginas de texto (3.1 a 3.3), una tabla de grupos de interés y una de criterios. No hay esquema de la solución, y la implementación, la implantación y la operación no existen como secciones.

**a) Esquema de la solución**
* Crítico: no hay modelo conceptual. El documento no contiene ninguna figura, ni imagen ni dibujo, en 138 páginas.
* La solución se describe en dos páginas (3–4) y luego mediante tablas de capas y de emplazamiento. No se entiende qué se va a construir sin haber leído el Subdocumento 4.
* La matriz de trazabilidad (págs. 20–24) tiene unas 19 filas agregadas por bloque, sin columna de paquete de la EDT ni identificador de prueba. No permite seguir un requerimiento hasta su componente.
* OK - Trata por separado los tres problemas del caso y los conecta con las restricciones (págs. 3–4).

**b) Definición del alcance, etapas, exclusiones, supuestos y restricciones**
* Las exclusiones EX-01 a EX-09 son fieles al Cap. 11 del caso, y el apartado “Lo que no haremos” (pág. 8) es claro.
* No cita la objeción que la gerenta general dejó en el acta, no analiza dependencias entre épicas, y el hito de septiembre de 2026 (vencimiento de la suspensión del proveedor de lácteos) no figura en la tabla de hitos.
* Contradicción con el cronograma obligatorio (Art. 17°): la pág. 4 dice “Marcha blanca de la Etapa 2… Meses 13–20”; lo obligatorio es desarrollo 13–18 y marcha blanca 19–20.
* Las etapas no cuadran entre secciones: OTIF y fill rate se asignan a la Etapa 2 (págs. 8 y 82), pero los requerimientos RF-11.03 y RF-11.04 están en la Etapa 1; el EDI es de la Etapa 2 y las cadenas se habilitan en los “meses 10–16" (pág. 133).
* Exclusiones y restricciones infladas con relleno del proceso licitatorio (video de cinco minutos, web corporativa, garantías, "tres sobres"): EX-12 a EX-14 y R-14 a R-27 no son alcance de la solución.
* Los supuestos (15 páginas) no tienen identificador, fundamento ni instancia de validación, que el numeral 17.1 del caso exige. Aun así el texto cita un "Supuesto S-41" que no existe.
* No hay visión de arquitectura empresarial. Interoperabilidad, escalabilidad, seguridad y performance aparecen dispersas en filas del registro de decisiones (D30, D35, D41, D53…), no como análisis.

**Catálogo de requerimientos (debía ir en el Formulario T-12)**
* Crítico: el Formulario T-12 no fue entregado, pese a que la pág. 26 lo da por hecho ("Resuelto (Matriz T-12)").
* El catálogo funcional (90 requerimientos) tiene identificador, nombre, épica, etapa, prioridad y origen. Le faltan los campos que el numeral 17.1 exige: descripción verificable, actor, precondición y resultado esperado. Tal como está es una lista de nombres.
* La prioridad no discrimina: 80 de los 90 requerimientos son "Alta" o "Muy Alta".
* La numeración tiene saltos: parece el extracto de un catálogo mayor que no se adjunta.
* El catálogo no funcional (40) tiene umbral y origen, pero no el método de verificación.
* Se citan requerimientos que no existen en el catálogo: RF-02.05d/e (págs. 69–70), RF-15.05 (pág. 132).

**c) Implementación**
* No existe como sección. No hay metodología de desarrollo, descripción del pipeline, gestión de configuración ni estrategia de ramas y versiones.
* Sólo hay menciones sueltas dentro del registro de decisiones: trazabilidad requerimiento–commit–prueba (D54), aprobación de dependencias (D49), infraestructura como código (pág. 6), cobertura de pruebas de 70 % (R-43).

**d) Implantación**
* No existe como sección. Las oleadas (D36, pág. 97) y la migración (D32, D58, D60) son filas de una tabla.
* Se escribe "plan de reversión" sin describirlo. No hay tiempo de rollback para la ventana de despacho de 05:30 a 07:00.
* No hay convivencia con el papel (hoja de picking, guía de despacho) durante la marcha blanca, que el caso exige en los numerales 13.3 y 17.6.
* No hay dotación de acompañamiento en el turno de noche de bodega, ni mecanismo para incorporar a los conductores de las diez empresas transportistas.

**e) Operación**
* No existe como sección. "SRE" aparece una sola vez en 138 páginas (pág. 37). No hay objetivos de nivel de servicio, runbooks ni automatización operacional.
* La mesa de ayuda se propone de 08:00 a 20:00 (D33 y RNF-21.04); el caso exige de 04:00 a 22:00 de lunes a sábado (RT-21.06), porque el despacho es a las 05:30.
* OK - RTO ≤ 4 horas y RPO ≤ 15 minutos se mantienen coherentes en todo el documento (no así en el Subdocumento 1).

**Estrategia para los grupos de interés**
* OK - Una tabla con cuadrante, momento, responsable e indicador por actor (págs. 129–134).
* Faltan la gerenta general y el comité ejecutivo, el gerente comercial, los almaceneros, la autoridad sanitaria y los peonetas.
* El planificador de rutas queda en el cuadrante "C — Mantener informado" (pág. 131), cuando el criterio de aceptación N° 16 depende íntegramente de su cooperación.

**Criterios de aceptación y decisiones del caso**
* OK - Los 16 criterios de aceptación tienen línea base, meta, momento y forma de medición (págs. 135–138). El N° 16 no define cómo se verificará.
* OK - Las 16 decisiones del numeral 16.1 están tomadas y justificadas (D1 a D16), incluida la más costosa: el WMS de 2013 se reemplaza por estrangulamiento (D14). El registro de vacíos y consultas (págs. 25–27) detecta errores reales de las Bases. Este material es valioso, pero está enterrado en 65 páginas de tabla ilegible y nadie lo convirtió en un documento.
* Excursión térmica sin arbitrar y contradictoria: "El bloqueo del despacho NO es automático: lo habilita el sistema y lo decide el conductor" (D4, pág. 65, y RNG-04, pág. 127); "la adopta la autoridad de calidad" (D25, pág. 87). El conductor —que en 54 de los 96 camiones es de una empresa externa— no puede decidir la liberación sanitaria de un lote. El Subdocumento 4.1 dice, además, que el sistema bloquea el despacho.
* Precio entre pedido y despacho: el supuesto de la pág. 29 dice que se cobra el precio ofrecido por el preventista; D9 y RNG-08 dicen "precio vigente al despacho".
* La promesa de 24 horas se da por "verificable" (pág. 3) sin decisión, requerimiento ni criterio que la sostenga.
* Crítico: precio en la Oferta Técnica. D45 (pág. 107): "del orden de 113 mil dólares antes de reservas… se traslada a la oferta". Además contradice la exclusión EX-09, según la cual el hardware de terreno lo compra el CLIENTE.

**Indicios de uso de IA sin revisión**
* Catorce veces se cita como fuente el nombre de un archivo: "Capítulo 11, Caso_02_Logistica.md", "Bases_Tecnicas_Transversales.md" (págs. 43–53). Son los archivos que se le entregaron al asistente, no una fuente.
* Notas de corrección de una versión anterior que quedaron en el texto: "La decisión previa… contradice el por defecto del RF-03.11 y se reformula" (pág. 70); "tal como estaba declarado no tenía emplazamiento físico en ninguna vista" (pág. 103); "Es una exigencia literal del Artículo 23 que no estaba respondida" (pág. 108).
* Dos voces distintas: de D1 a D40 se parafrasean requerimientos; de D41 a D60 aparece otra prosa, con marcas comerciales y productos descartados.
* Se citan la "Decisión 20" y la "Decisión 29" en las págs. 5 y 8, setenta y cinco páginas antes de que existan; códigos sin glosario (BTC, BTT, R18, RNG, HHT); un párrafo de excursión térmica pegado dentro de la decisión sobre la cámara a −22 °C (pág. 87).

**Qué se espera en el Informe 2**
* Un documento de 25 a 35 páginas de análisis: esquema de la solución con su diagrama, alcance por etapa con sus criterios, y las secciones de implementación, implantación y operación desarrolladas.
* Catálogos, supuestos, restricciones y registro de decisiones en el Formulario T-12 y en anexos, con todos los campos del numeral 17.1 y en tablas legibles (hoja horizontal si hace falta).
* Matriz de trazabilidad requerimiento por requerimiento hasta el componente de la arquitectura.
* Resolver la excursión térmica con una regla escrita y un responsable que pueda decidir; arbitrar la promesa de entrega; alinear las etapas con el Art. 17°.
* Eliminar el precio de la pág. 107.
