# LafroX — Análisis vigente del Subdocumento 4 contra las Aclaraciones

## Dictamen y alcance

El SD4 tiene la estructura obligatoria y desarrolla la arquitectura de la solución con decisiones, figuras, correspondencias y cálculos. No corresponde declararlo plenamente conforme: persisten doce citas a Bases sin página, una condición de recuperación sin resolución contractual acreditada y un dimensionamiento incremental de innovaciones que todavía describe cómo obtener sus entradas, sin presentar resultados numéricos. La presentación final requiere comprobación sobre los PDF vigentes.

Revisión realizada el 12 de octubre de 2026 sobre el contenido local de `rama-md`, incluidos sus cambios sin commit. Se contrastaron cuerpo, anexos y T-11 con `Bases/aclaraciones-licitacion.md`. Se consultaron los registros anteriores para distinguir correcciones aplicadas de pendientes actuales. Se cotejaron también los títulos de 3.3/3.4 y los nombres M10/M11 del SD3. Las líneas citadas corresponden al estado revisado, no a la revisión del día anterior.

El Markdown es espejo de contenido; un enlace a una figura PDF existente no se clasifica por sí solo como defecto del entregable. No se recompiló ni se efectuó una nueva revisión visual del PDF. No se verificaron servicios comerciales, normas o legislación en fuentes externas, ni se certificó la ejecución de ensayos. Este informe no modifica los entregables.

## Contraste con las Aclaraciones

La siguiente matriz diferencia la evidencia textual actual de los controles que siguen abiertos.

| Exigencia | Evidencia vigente | Resultado |
| --- | --- | --- |
| §1: archivos y nomenclatura | Tres archivos separados: cuerpo, anexos y T-11; el capítulo cita sus complementos en la introducción. | Conforme en fuentes Markdown; verificar nombres PDF y ZIP final. |
| §§2 y 11: títulos obligatorios | Presentes el título del capítulo, 4.1, 4.1.1, 4.2, 4.2.1, 4.3, 4.3.1 y 4.3.2, con el texto obligatorio y en orden. | Conforme en el contenido examinado. |
| §§2 y 3: introducción y texto de caída | Introducción conecta SD3, arquitectura, anexos y T-11. No se detectaron títulos de desarrollo seguidos directamente de tabla, figura, lista u otro título, omitiendo blancos y anclas de navegación. | Conforme en la comprobación estructural. |
| §3: cuerpo analiza; anexos y formularios detallan | El cuerpo desarrolla responsabilidades, recorridos, elecciones y consecuencias. Catálogos y cálculos completos se concentran en anexos y T-11. | Organización adecuada. |
| §4: figuras propias e integradas | 29 figuras numeradas en el cuerpo, con activos locales existentes; vista general, capas, ambientes, red y recinto técnico. | Evidencia documental presente; tamaño impreso e integración efectiva se comprueban en PDF. |
| §5: tablas del cuerpo | 26 tablas técnicas, de 2–5 columnas y 2–11 filas de datos; la tabla 27 es la declaración de IA de seis columnas. | Dimensiones de síntesis adecuadas; una página, estilo y legibilidad requieren PDF. |
| §6: referencias | Bibliografías presentes, incluidas las cinco entradas AWS incorporadas a anexos. Persisten doce citas a Bases sin página. | Pendiente confirmado: A-01. |
| §7: uso de IA | 132 filas: 108 secciones numeradas, 23 anexos y T-11, con Álvaro Catalán como revisor. No se encontraron marcadores `[[...]]` en los tres archivos. | Cobertura documental presente; no acredita ensayos ni firma ni consolidación en A-6. |
| §8: innovaciones | Anexo 4-N describe los recorridos de las cinco innovaciones; 4.2.6 y 4-W.12 establecen aceptación de carga mixta. | Integración descrita; dimensionamiento incremental abierto: A-03. |
| §9: presentación | Los Markdown contienen navegación; no permiten medir puntos tipográficos, folios, firmas, orientación o tamaño de hoja. | No certificado en esta revisión. |
| §10: evaluación | Hay evidencia de ingeniería y pendientes identificables. | No se asigna puntaje ni se atribuye una decisión a la comisión. |
| §11: lógica → física y SD3 → lógica | Anexo 4-N contiene correspondencias por capacidad, doce módulos, inventario transversal y actores; M10/M11 coinciden con SD3. | Mapeo desarrollado; no constituye auditoría exhaustiva de todos los RF/RNF/RT. |

Los límites de cinco columnas y una página del §5 no se aplican a los catálogos de anexos ni al T-11. La declaración de IA conserva las seis columnas que exige específicamente el §7.2.

## A-01 — Doce citas a Bases sin folio

Este es un incumplimiento documental confirmado del §6: se exige documento, capítulo o artículo y página. Añadir la sección 16.5 mejora la precisión de dos citas, pero no reemplaza la página.

| Archivo | Línea | Cita sin página | Ocurrencias |
| --- | --- | --- | --- |
| Cuerpo | 785 | BTT, cap. 14; BA, art. 50.2 | 2 |
| Cuerpo | 795 | BTT, cap. 21 | 1 |
| Cuerpo | 1973 | BA, art. 50.2 | 2 |
| Cuerpo | 2248 | BTT, cap. 2; BA, art. 50.2 | 2 |
| Anexos | 369 | BTT, cap. 16, sección 16.5; BA, art. 50.2 | 2 |
| Anexos | 371 | BTT, cap. 16, sección 16.5 | 1 |
| T-11 | 12 | BA, art. 50.2 | 1 |
| T-11 | 57 | BTT, cap. 6 | 1 |

BA significa Bases Administrativas y BTT, Bases Técnicas Transversales. Las doce ocurrencias coinciden con el inventario previo, ahora localizadas en los Markdown actuales. Deben completarse contra los folios del PDF original; no corresponde deducirlos de la numeración del Markdown ni inventarlos. Esta comprobación no valida por sí sola las páginas que otras citas ya contienen.

## A-02 — La brecha de RPO sigue abierta

En 4.3.2.4, cuerpo, líneas 3315–3317, el diseño protege la extracción mediante fibra, LTE y satélite, pero reconoce que el aislamiento de los tres caminos seguido de destrucción del sitio puede dejar una copia externa con antigüedad mayor a quince minutos. Mantiene R8-05 y solicita tratamiento contractual; expresamente indica que registrar el riesgo no aprueba una excepción.

La exposición es honesta y técnicamente relevante. El pendiente consiste en resolver la compatibilidad entre el compromiso crítico de RPO ≤15 minutos y la cobertura de fallas declarada, conforme a la exigencia de continuidad, contingencias y cumplimiento de §§3 y 11. No se concluye que todos los escenarios del diseño incumplan ni que una aprobación del CLIENTE ya exista.

Para cerrar: precisar los escenarios cubiertos y el residual, comparar alternativas con criterio de selección, demostrar la cobertura mediante AL-DR-01 y obtener la decisión contractual requerida por las Bases. La prueba debe conservar el desfase observado y el punto recuperable; no puede convertir automáticamente un objetivo incumplido en una excepción aceptada.

## A-03 — Falta el resultado numérico de la carga incremental de SD13

El cuerpo, 4.2.6, líneas 2684 y 3049–3057, exige contrastar la carga base con las innovaciones. El Anexo 4-W.12, líneas 1843–1859, identifica qué medir para INN-01 a INN-05: cardinalidad, CPU, memoria, tamaño, retención, tráfico y concurrencia. Presenta el método y las pruebas, pero ese bloque no aporta una estimación numérica por innovación y recurso que permita comprobar la capacidad total.

Esto deja incompleta la fundamentación cuantitativa de la capacidad ampliada bajo §§3 y 11. No se reclama disponer de mediciones de producción antes de implantar: puede cerrarse inicialmente con supuestos explícitos y cálculos reproducibles, separando estimación y resultado de prueba. Las 10.920 muestras térmicas diarias ya incluidas en la base no cuantifican por sí solas el procesamiento derivado de INN-03 ni la carga de las otras cuatro innovaciones.

Para cerrar: agregar en la memoria un escenario por ventana y etapa, con demanda base, incremento estimado, demanda total, capacidad del recurso y acción ante exceso. El cuerpo debe resumir el efecto sobre la selección de capacidad. CPU, IOPS, almacenamiento, enlaces y trabajos de fondo necesitan cotas propias; no basta con suponer que los márgenes de TPS los absorben.

## A-04 — La cota máxima de API tiene margen mínimo en el modelo

En 4.2.6.9, cuerpo, líneas 2918–2937, se calcula una capacidad de 14 solicitudes/s por tarea y un techo de ocho tareas. La cota completa del portal y canal tradicional llega a 111,70 solicitudes/s. Aplicando el propio modelo:

- Capacidad al techo: 8 × 14 = 112 solicitudes/s.
- Diferencia: 112 − 111,70 = 0,30 solicitudes/s.
- Margen respecto de la demanda: 0,30 ÷ 111,70 × 100 ≈ 0,27 %.

No es una infracción automática de las Aclaraciones ni evidencia de saturación observada. Sí es una sensibilidad importante: la cota queda prácticamente en el límite calculado y depende de los 50 ms de CPU por solicitud, de la mezcla y del escalado oportuno. El propio texto reconoce que no permite aumentar la cuota y exige prueba.

Para cerrar: demostrar el escenario completo, incluyendo latencia de escalado y pérdida de una tarea si la disponibilidad comprometida exige sostener esa carga bajo falla. Definir la acción cuando se alcance el techo. La carga incremental de A-03 tampoco puede darse por absorbida por este margen.

Como mejora de precisión, sustituir «Cumple» en la conclusión de las primeras filas de la Tabla 19 por «Dentro de la capacidad calculada» o equivalente. Los párrafos ya distinguen modelo y ensayo, pero la celda aislada puede leerse como cumplimiento medido. No se atribuye aquí fabricación de resultados.

## Correcciones anteriores que siguen vigentes

La revisión del 11 de octubre es histórica y no debe reutilizarse como diagnóstico actual sin cotejo. En el estado examinado:

- No aparecen «Caso 02», el rótulo duplicado «Anexo Anexo 4-W» ni marcadores de revisión humana.
- La declaración cubre las 108 secciones numeradas; no falta ninguna fila en esa correspondencia.
- Las remisiones de capacidad usan las tablas 19 y 22, con destinos válidos; los antiguos números 28/29/30 no se mantienen como aquellos destinos.
- El Anexo 4-P tiene introducción bajo «Detalle de selección por capa».
- La bibliografía de anexos incluye las cinco referencias AWS j–n utilizadas en las notificaciones.
- Las Figuras 24–26 identifican una vista general y dos vistas específicas de red. El registro de cierre documenta dibujos independientes y rótulos de 10,58 puntos en el PDF revisado entonces; esa medida no se presenta como una nueva verificación visual.
- M10 BI Gerencia y M11 EDI Canal Moderno coinciden con SD3, tanto en los pasajes cotejados como en la matriz A.14.

## Evidencia, límites y prioridades

Los controles sobre los tres Markdown comprobaron 340 enlaces con fragmentos internos válidos, sin anclas explícitas duplicadas, y 210 enlaces a archivos locales existentes. Las 29 figuras pertenecen al cuerpo; hay 40 tablas en anexos y un catálogo de 93 filas en T-11. La comprobación estructural no detectó títulos de desarrollo sin texto de caída. Estos resultados prueban navegación y estructura, no legibilidad impresa ni exactitud de cada afirmación técnica.

La matriz A.14 contiene 22 filas de correspondencia y A.15 los doce módulos. Se localizaron las nueve subsecciones de 3.3/3.4 que esa correspondencia utiliza. La existencia de matrices no sustituye el cotejo bidireccional completo de capacidades, interfaces, decisiones, etapas y requerimientos; no se certifica el «100 %» con un porcentaje inventado.

Prioridad de cierre: resolver A-02 y cuantificar A-03; completar los folios de A-01; verificar la sensibilidad A-04; después comprobar los tres PDF vigentes, firmas, consolidación A-6 y ZIP. Los ensayos previstos son criterios de aceptación del proyecto, no resultados disponibles ni una exigencia de fabricar evidencia antes de la entrega de la oferta.

Fuentes de la revisión: las Aclaraciones; los tres archivos actuales de `04_arquitectura/`; SD3 para títulos y M10/M11; `Revision/revision_SD4_aclaraciones_2026-10-11.md`; `Revision/cierre_correcciones_SD4_aclaraciones_2026-10-11.md`; `Revision/citas_Bases_SD4_paginas_pendientes.md`; y el contexto de sesión. No se hicieron cambios técnicos, compilaciones, commit ni push.
