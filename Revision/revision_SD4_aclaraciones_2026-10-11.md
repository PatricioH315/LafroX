# LafroX — Revisión del Subdocumento 4 conforme a las Aclaraciones

Estado posterior: el usuario autorizó corregir estos hallazgos y aclaró que Markdown sirve como espejo de contenido del LaTeX. La revisión siguiente conserva el diagnóstico anterior a los cambios. El estado vigente, incluida la designación de Álvaro Catalán como único revisor y la reclasificación de los enlaces a figuras, se documenta en [el cierre de correcciones](cierre_correcciones_SD4_aclaraciones_2026-10-11.md).

Fecha: 11 de octubre de 2026. Checkout: `LafroX-alvaro-md`, rama comprobada `rama-md`, HEAD `05f1d66708cbb1f524e1bbb294eeec2786fcec88`, con cambios locales previos conservados. Se revisó el contenido efectivo de los tres Markdown de `04_arquitectura/`, no sólo el commit. Las líneas indicadas corresponden a ese estado local.

La solicitud autoriza analizar y revisar el SD4, incluida la preferencia de llamar «caso» o «caso de logística» al caso sin enumerarlo. Este informe registra observaciones y recomendaciones; no modifica los entregables, sus figuras, las Bases ni otros subdocumentos. No se hizo commit ni push.

## Observaciones confirmadas

### O-01 — Persisten seis menciones de «Caso 02»

La denominación solicitada todavía no está aplicada en los tres entregables. Esta observación procede de la instrucción del usuario; las Aclaraciones no contienen una prohibición literal de «Caso 02».

| Archivo y línea | Texto localizado | Redacción recomendada |
| --- | --- | --- |
| Cuerpo, 167 | «y del caso 02 se desprenden ocho reglas de diseño» | «y del caso se desprenden ocho reglas de diseño» |
| Cuerpo, 2658 | «la volumetría del Caso 02» | «la volumetría del caso» |
| Cuerpo, 3383 | Referencia «Caso 02: Logística. Especificaciones…» | «Caso: Logística. Especificaciones…» |
| Anexos, 1869 | Referencia «Caso 02: Logística. Especificaciones…» | «Caso: Logística. Especificaciones…» |
| Anexos, 1877 | «Licitación TFEP-01/2026, Caso 02 — Logística» | «Licitación TFEP-01/2026, caso de logística» |
| T-11, 127 | Referencia «Caso 02: Logística. Especificaciones…» | «Caso: Logística. Especificaciones…» |

La búsqueda también contempló «caso 2» y separadores alternativos. No identificó otras coincidencias en estos tres archivos. No corresponde renombrar la Base original ni sus identificadores por esta observación. Las portadas PDF quedan fuera de esta comprobación.

### O-02 — La revisión humana sigue sin completar

Ubicación: cuerpo, líneas 3483–3538, Tabla 27. Las 56 filas contienen `[[REVISIÓN HUMANA]]`: 32 secciones, 23 anexos y T-11.

Las Aclaraciones §7.1 y §7.2 exigen elaboración, verificación y responsabilidad humana, y declarar quién revisó y qué verificó. La declaración existe y reconoce el uso de IA, pero los marcadores no acreditan revisión efectiva. Completar sólo con integrantes y comprobaciones reales; no borrar los marcadores para aparentar conformidad. El nivel «Alto» declarado no elimina esta exigencia.

### O-03 — Hay referencias a tablas inexistentes en el cuerpo

Ubicaciones: cuerpo, línea 2953 («Tabla 28») y línea 3041 («Tablas 29 y 30»). El cuerpo actual contiene tablas numeradas de 1 a 27, y la 27 es la declaración de IA. Estas remisiones conservan numeración anterior y no identifican evidencia disponible por su rótulo vigente.

Las Aclaraciones §5 exigen integración y referencias claras; §7.1 d incluye referencias a secciones o anexos inexistentes entre los indicios documentales. Corregir las remisiones según el tema y destino efectivo, preferentemente enlazando su ancla. La sensibilidad de portales se desarrolla en la Tabla 19; las otras remisiones deben cotejarse con el pasaje de capacidad y su ensayo antes de sustituir los números. No convertir mecánicamente «29 y 30» en nuevos números sin comprobar su significado.

### O-04 — Falta texto de caída en un subtítulo de anexos

Ubicación: anexos, línea 1099, «Detalle de selección por capa». El siguiente elemento es la lista que comienza por «Backend (12 módulos)», sin frase introductoria propia bajo el subtítulo.

Las Aclaraciones §3 prohíben título seguido directamente de lista sin frase introductoria. El párrafo que antecede al subtítulo pertenece al título superior y no resuelve este punto. Añadir una explicación breve del criterio de organización antes de la lista. En el desarrollo técnico del cuerpo no se localizaron títulos con esa misma deficiencia mediante la inspección estructural realizada; el índice se trató como navegación, no como contenido técnico.

### O-05 — Los anexos remiten a referencias bibliográficas de otro archivo

Ubicaciones: anexos, líneas 369 y 371. Se citan Amazon Web Services, s. f.-j, s. f.-k, s. f.-l, s. f.-m y s. f.-n y se añade «referencias del Subdocumento 4». La lista final de referencias de los anexos, desde la línea 1857, no contiene esas entradas.

Las fuentes existen en el cuerpo, pero la bibliografía del archivo de anexos no permite resolver por sí misma sus citas. Las Aclaraciones §6 exigen correspondencia entre las citas utilizadas y la lista final. Incorporar las entradas realmente utilizadas al archivo de anexos, conservando las letras consistentes con el cuerpo. Este hallazgo no afirma que esas fuentes sean inexistentes ni verifica la exactitud técnica de sus páginas web.

### O-06 — Hay citas a Bases sin página

Ejemplos comprobados: anexos, líneas 369 y 371, «Bases Técnicas Transversales, cap. 16», sin página para RT-16.24 y RT-16.23.

Las Aclaraciones §6 exigen documento, capítulo o artículo y página. Añadir el folio respaldado por la Base correspondiente. No inventar páginas ni considerar suficiente que el catálogo inicial cite un intervalo amplio para todos los RT. Estos ejemplos bastan para confirmar la observación; no constituyen un inventario exhaustivo de todas las citas incompletas.

### O-07 — El catálogo contiene un rótulo duplicado

Ubicación: anexos, línea 83, Tabla A.1: «4-W / Anexo Anexo 4-W — Memoria de cálculo del dimensionamiento».

La entrada debe decir «4-W / Anexo 4-W — Memoria de cálculo del dimensionamiento». El destino del enlace existe; el problema es editorial, no la ausencia del anexo. Corregir para mantener nomenclatura consistente conforme a las Aclaraciones §3.

## Observaciones condicionadas y verificaciones pendientes

### O-08 — Quince figuras aparecen como enlaces en el Markdown

El cuerpo tiene 27 figuras numeradas: 12 imágenes insertadas y 15 enlaces a PDF (Figuras 1–13, 17 y 24). Los rótulos, las fuentes y las explicaciones acompañan activos identificados; no son sólo leyendas sin objeto declarado.

Las Aclaraciones §4 y §7.1 a exigen figuras efectivamente integradas en el desarrollo. Si se entrega una exportación directa de estos Markdown, un enlace no reemplaza la figura visible. Si el entregable es el PDF ensamblado desde LaTeX, corresponde comprobar allí la inserción efectiva. No se afirma que el PDF carezca de esas figuras: no se inspeccionó ni recompiló en esta revisión.

### O-09 — La legibilidad de la Figura 24 conserva una observación previa

Ubicación del contenido: cuerpo, línea 2324, diagrama de red. El registro `Revision/ALINEACION_MD_LATEX_SD4_2026-10-11.md` informa rótulos cercanos a 5 puntos al imprimir la figura. Las Aclaraciones §4 exigen al menos 9 puntos y lectura sin ampliar.

Es evidencia de una revisión anterior, no una medición nueva del PDF actual. Verificar nuevamente el tamaño impreso y, si se confirma, reorganizar la vista general y preparar diagramas propios por partes. No usar recortes ampliados como figuras de detalle. La existencia de un PDF compilado sin desbordamientos no demuestra por sí sola legibilidad.

### O-10 — La declaración de IA agrupa subsecciones

La tabla contiene 32 entradas de secciones, pero el índice desarrolla niveles más finos, por ejemplo 4.1.3.1–4.1.3.8 y 4.2.6.1–4.2.6.13. Las Aclaraciones §7.2 piden una fila por sección. Verificar si la agrupación por sección madre satisface el nivel solicitado; la cobertura temática agrupada no equivale automáticamente a cobertura literal de cada subtítulo.

No se recomienda reducir la tabla a cinco columnas: sus seis columnas son las exigidas por §7.2. Tampoco se marca como infracción por sí solo que tenga 56 filas; primero debe preservarse la estructura específica de la declaración. La observación confirmada sobre esta tabla es la ausencia de revisión humana real registrada, descrita en O-02.

### O-11 — La presentación final y el mapeo del 100 % no quedan certificados

Los índices Markdown son navegables, pero no tienen folios. El índice del T-11 tampoco incluye su bloque final de Referencias, presentado en la línea 117 como texto en negrita. La revisión de una fuente Markdown no acredita índices paginados, letra del cuerpo ≥11 puntos, letra en figuras y tablas ≥9 puntos, formato carta u oficio, foliación inferior derecha, firmas, portadas, filas completas, encabezados repetidos o ZIP final. Comprobar estos aspectos en los entregables conforme a §§1, 4, 5 y 9.

La correspondencia SD3–lógica–física está desarrollada en 4.1, 4.2.2 y Anexo 4-N, con módulos, capacidades e integraciones identificados. Para afirmar el mapeo del 100 % exigido por el índice obligatorio se necesita cotejar todo el universo vigente de 3.3/3.4 con los componentes lógicos y físicos, no sólo verificar que exista una matriz. Esta revisión editorial no certifica ese porcentaje ni la coherencia integral con todos los otros subdocumentos. Los protocolos previstos tampoco se presentan como ensayos realizados.

## Comprobación por cada bloque de las Aclaraciones

| Bloque | Resultado observado |
| --- | --- |
| §1 Archivos y nomenclatura | Cuerpo, anexos y T-11 separados, con nombres coherentes; ZIP y nombres finales PDF no comprobados. |
| §2 Índice y orden | Títulos obligatorios presentes, introducción y cierre Referencias → Declaración de uso de IA en el cuerpo; paginación pendiente de comprobar en PDF. |
| §3 Redacción | Desarrollo narrativo y análisis presentes; caída faltante en anexos (O-04) y duplicación de rótulo (O-07). No se localizaron montos monetarios de oferta en los tres Markdown; menciones de costos o tarifas sin montos no constituyen por sí solas infracción. |
| §4 Figuras | 27 figuras del cuerpo con rótulos y activos identificados; integración en una exportación directa y legibilidad final sujetas a O-08/O-09. No se certificó visualmente que todos los detalles sean diagramas independientes sin recortes. |
| §5 Tablas | 26 tablas técnicas del cuerpo, de 2 a 5 columnas, con 2 a 11 filas de datos. No se localizaron tablas técnicas del tipo puro «Concepto / Descripción». Tabla IA de 6 columnas conforme a su formato específico. Una página, orientación, tipografía y estilo empresarial requieren verificación del PDF. Los límites de una página/cinco columnas no se trasladan a anexos ni T-11. |
| §6 Referencias | Lista final y numerosas citas contextualizadas presentes; referencias ausentes en bibliografía de anexos (O-05), citas sin página (O-06) y remisiones numéricas obsoletas (O-03). No se hizo validación exhaustiva de todas las fuentes externas. |
| §7 IA | Herramienta, finalidad, niveles y cobertura de 23 anexos/T-11 declarados. Las 56 revisiones humanas siguen sin acreditar (O-02); granularidad de secciones a revisar (O-10). |
| §8 Innovaciones | SD4 reconoce su integración con SD13 y carga incremental en 4.2.6/4-W.12. La evaluación de los siete elementos de cada innovación pertenece al SD13 y no se certifica aquí. |
| §9 Formalidad | Requiere control sobre los PDF finales y firmas; no inferir conformidad desde Markdown (O-11). |
| §10 Evaluación | Persisten defectos que deben resolverse antes de entregar. La aplicación de una sanción o de puntaje corresponde a la comisión; este informe no atribuye una decisión de evaluación ya tomada. |
| §11 Índice obligatorio del SD4 | Presentes 4.1, 4.1.1, 4.2, 4.2.1, 4.3, 4.3.1 y 4.3.2, con textos coincidentes. Desarrollo de lógica, integración, seguridad, emplazamiento, nube, cinco ambientes, continuidad, capacidad y centros de datos. Mapeo integral pendiente de certificar (O-11). |

## Resultado

La estructura obligatoria está presente, pero la versión revisada no permite declarar conformidad total. Priorizar revisión humana real, remisiones a tablas, denominación no enumerada del caso y referencias; después completar redacción y comprobar la presentación final. Los hallazgos antiguos no se copian automáticamente como actuales: por ejemplo, el T-11 ya distingue hardware de terreno adquirido por el CLIENTE e infraestructura on-premise provista por el adjudicatario.

Fuentes locales: `Bases/aclaraciones-licitacion.md`, los tres entregables vigentes de `04_arquitectura/`, `compct/CONTEXTO_SESION.md` y el registro previo de alineación. No se modificaron fuentes LaTeX ni se verificaron sitios web, certificaciones o resultados de pruebas reales.
