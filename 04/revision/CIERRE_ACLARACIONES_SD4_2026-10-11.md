# LafroX — Cierre de correcciones del SD4 conforme a las Aclaraciones

## Alcance y autorización

El usuario autorizó aplicar las propuestas de la revisión del SD4 en LaTeX y Markdown, como espejos de contenido. Confirmó revisión integral y pidió finalmente dejar únicamente a Álvaro Catalán en la columna de revisión humana. Los cambios se realizaron en los checkouts existentes `rama-md` y `subdoc-4`, preservando cambios locales anteriores. No se hizo commit ni push.

El Markdown es una representación para revisión del contenido de LaTeX. Sus enlaces a figuras no se tratan como defectos de presentación: el entregable visual es el PDF compilado.

## Resultado por observación

| Observación | Cambio y estado |
| --- | --- |
| O-01 Caso enumerado | Corregidas las seis menciones en cuerpo, anexos y T-11. Las tres portadas sobreescriben el metadato a «Caso — Logística» sin modificar la clase compartida ni las Bases originales. |
| O-02 Revisión humana | Las 132 filas identifican únicamente a Álvaro Catalán, conforme a la confirmación del usuario. Se registra revisión integral del contenido de cada sección, anexo o formulario, sin atribuirle ensayos ejecutados o mediciones. |
| O-03 Tablas 28/29/30 | Sustituidas por referencias automáticas a perfiles Fargate y ensayos de dimensionamiento. El Markdown enlaza las mismas tablas y usa la numeración compilada. |
| O-04 Texto de caída | Añadida la introducción bajo «Detalle de selección por capa» en Anexo 4-P. |
| O-05 Bibliografía AWS | Incorporadas las cinco entradas AWS utilizadas en anexos; se conservan las letras j–n del cuerpo y se eliminan remisiones a la bibliografía de otro archivo. |
| O-06 Citas sin página | Añadida la sección 16.5 a RT-16.23/24. Se inventariaron doce ocurrencias sin folio verificado: permanece pendiente el cotejo con PDF originales de Bases, ausentes en las fuentes locales consultadas. No se inventaron páginas. |
| O-07 Rótulo duplicado | Corregido «Anexo Anexo 4-W» y su origen en la conversión de etiquetas de anexos, para que no reaparezca al comparar formatos. |
| O-08 Figuras enlazadas en Markdown | Observación reclasificada: es una diferencia de representación admitida. Se comprueba el archivo real de cada figura y su correspondencia con la fuente LaTeX. |
| O-09 Red legible | Vista general y dos diagramas independientes de detalle, no recortes. Se conserva intacto el XML/PDF original y se integran las nuevas vistas en el cuerpo. Rótulos del diagrama medidos por encima de 10 puntos en el PDF ensamblado. |
| O-10 Granularidad de IA | Una fila por las 108 secciones numeradas del cuerpo, más 23 anexos y T-11: 132 filas. Se conserva el formato obligatorio de seis columnas, niveles reales e indicación de asistencia. |
| O-11 Formalidad y correspondencia | T-11 incorpora índice paginado, lista de tablas y Referencias navegables. Anexo 4-N amplía el mapeo con implementación, implantación, operación y participación de 3.4.3–3.4.6. Se cotejaron nueve subsecciones de 3.3/3.4, doce módulos y quince actores. Esto no constituye una certificación de cumplimiento de todos los RF/RNF/RT ni de ejecución de pruebas. |

## Conservación y límites

- La figura original de red conserva su SHA-256 `912bf7b551a9bd005b9e8f00b39d265faa7ff34221b6934f33cf4ee33b841aac`.
- Los datos, tecnologías, cantidades y decisiones técnicas anteriores se conservan; las cuatro nuevas filas de correspondencia vinculan contenido ya existente, sin crear módulos ni actores.
- La identidad del representante legal en las portadas permanece como antecedente corporativo: la instrucción del usuario cambió al revisor humano, no al apoderado ni a sus funciones.
- La firma real de la oferta y su consolidación administrativa en A-6 requieren su realización por el responsable. No se insertaron firmas ni se modificó A-6 u otros subdocumentos.
- La nueva numeración mueve Talca a Figura 27, racks a 28 y recinto a 29. Las remisiones externas del T-12 deben cotejarse por su responsable; no se editó SD3 en esta tarea.
- Las doce citas sin página se detallan en [el inventario pendiente](citas_Bases_SD4_paginas_pendientes.md). Se mantiene la distinción entre cálculo de diseño, revisión documental y resultados de ensayo.

## Verificación

Los controles de contenido verifican 132 filas IA con un único revisor, 108 secciones, 29 figuras con activos existentes, 340 enlaces internos válidos y ausencia de anclas explícitas duplicadas. Las nueve subsecciones de 3.3/3.4, los doce módulos y los quince actores tienen correspondencia documental.

La comparación normalizada secuencial coteja cuerpo, anexos y T-11; navegación y activos gráficos se comprueban aparte. Los resultados finales de compilación, extracción de texto y revisión visual se guardan en `LafroX-rama-latex/04/revision/aclaraciones_20261011/`. La falta de folios originales de Bases se mantiene como pendiente, no como conformidad ficticia.

Resultado final: cero diferencias en 1.647 bloques de cuerpo, 1.060 de anexos y 111 de T-11. Compilación LuaLaTeX de los tres documentos estabilizada en tres pasadas: 201, 100 y 48 páginas respectivamente. Sin referencias indefinidas, caracteres faltantes ni cajas desbordadas. La extracción integral de los tres PDF confirma ausencia del caso enumerado y de marcadores humanos, y ausencia de Alex Aravena en la declaración de revisión. La identidad corporativa de portada se verificó por separado.

Se inspeccionaron visualmente portadas, índices, las tres nuevas figuras de red, las 18 páginas de la declaración IA, el texto de caída del Anexo 4-P, la bibliografía AWS, la ampliación de la matriz en página 33 de anexos y las Referencias del T-11. La columna de emplazamiento de la Tabla A.14 se amplió sin alterar sus celdas. Los nuevos diagramas conservan 10,58 puntos en sus rótulos dentro del PDF compilado.
