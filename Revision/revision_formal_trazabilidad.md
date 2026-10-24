# LafroX — Corrección formal de la trazabilidad consolidada

## Causa y alcance

Se convirtió por error el contraste de auditoría de `Revision/`, no la matriz consolidada indicada por el usuario. El entregable se rehízo desde `Trazabilidad/LAFROX-Trazabilidad-Informe1-Consolidada.md` de `rama-md`, sin editar ese original. El usuario exige cuatro columnas exactas, los IDs originales y la base LaTeX de los otros subdocumentos; confirmó que no se incluya declaración de IA aquí.

## Entregable y plantilla

Archivo activo: `Trazabilidad/LAFROX-Trazabilidad-Informe1-Consolidada.tex`. `main.tex` y el antiguo punto de entrada de `Revision/` remiten a él: no compilan ya la auditoría por error.

Clase, portada y activo de firma copiados íntegramente del checkout vigente `LafroX-sd1-latex`. Hashes comparados: los tres archivos son idénticos. No se modificaron otros subdocumentos ni se atribuyó nueva revisión humana. La firma gráfica no se presenta como autenticación digital.

## Integridad y pruebas

- SHA-256 de la fuente: `7e1d29899afc46e4c6f87196ae09595a4ce6ba484a1a46d453eba27fec8f9155`.
- 212 filas: SD1 34; SD2 32; SD3 45; SD4 52; SD5 24; SD13 24; TR 1.
- IDs únicos, orden original y 212 observaciones íntegros; estados preservados. 205 filas idénticas a la fuente y 7 con depuración editorial de notas de proceso.
- 848 celdas del PDF cotejadas individualmente por fila y columna contra el contenido preparado: **0 discrepancias**. 212 IDs en el PDF, únicos y en orden correcto.
- 43 páginas carta; índice y lista de tablas; cabeceras repetidas; filas indivisibles; folios consecutivos y rótulo de media firma verificados en las 42 páginas posteriores a portada.
- Inspección visual de todas las páginas en hojas de contacto; portada, tablas y transiciones examinadas a mayor escala. Ajustados título huérfano, tabla SD4 con una sola fila final, transición SD5–SD13, URLs largas y referencias bibliográficas partidas. Sin celdas recortadas ni invasión del pie.
- Compilación: `latexmk -lualatex -interaction=nonstopmode -halt-on-error -outdir=<scratch> Trazabilidad/LAFROX-Trazabilidad-Informe1-Consolidada.tex`, salida **0**. Cero Overfull, errores fatales, caracteres ausentes o referencias indefinidas. Persisten **29** avisos `ignored error Infinite glue shrinkage found in box being split` y **5 Underfull** no fatales; no se declara log limpio.
- Comprobación geométrica de las 43 páginas: 0 incidencias, admitiendo la protrusión óptica de puntuación de la plantilla (máximo 3 pt; desactivada en Referencias).
- PDF, scripts, JSON de pruebas y auxiliares quedan fuera del repositorio. Runtime harness: N/A, documento sin aplicación ejecutable.

Esta revisión verifica integridad de conversión y presentación. No reauditó la veracidad de todas las respuestas, la vigencia de cada página citada ni el cierre de los subdocumentos. Se conservaron los estados pendientes y los límites de evidencia del Markdown; no se afirma conformidad global de la entrega.

## Depuración editorial

Sin alterar las observaciones ni los estados:

- SD1-02: retirados detalles de fuentes locales y pasadas de compilación; conservada la orientación de folios y la reserva sobre autenticación de la firma.
- SD1-05: retirados historial de clasificación y formatos de conversión; conservada la revisión declarada por la fuente. «Portadas locales» pasa a «portadas».
- SD1-09: concordancia MD–LaTeX reformulada como concordancia documental; conservadas las 44 celdas y los campos.
- SD1-10: formuladas las referencias normativas como sustento vigente, sin historial de recompilación; conservadas cifras, localizadores y reserva de SLA.
- SD3-09: eliminada la enumeración Markdown/LaTeX/PDF; se conserva presencia en el formulario, 645 filas y desglose EDT.
- SD3-18: retirado el conteo histórico de páginas compiladas; conservado el formulario independiente, las 645 filas y sus dos partes.
- SD4-37: retirado el historial de compilación; se conserva el T-11 independiente y su condición de inclusión en el paquete.
- Notas SD4: retiradas fecha y explicaciones de proceso; corregida la remisión a «primera/tercera columna» para el esquema consolidado de cuatro columnas.
- Notas SD13: retirados los localizadores históricos Tabla 13.D.1/13.D.2 del anexo eliminado; se remite a los IDs SD13-01..16 y SD13-17..24 ya presentes.
- Enlaces Markdown de Referencias presentados por su título; URLs externas conservadas y con saltos de línea. No se añaden notas internas al PDF.

## Unidad de cambio y publicación

Corrección del mismo entregable en `LafroX-Revision-Trazabilidad-Informe1-LateX`, manteniendo la autorización previa de commit/push del usuario. Rollback: revertir esta unidad de matriz LaTeX, puntos de entrada, activos de plantilla y documentación, sin afectar `rama-md` ni otros subdocumentos.

## Actualización: localizadores simplificados — 12 de octubre de 2026

El usuario aprobó aplicar la simplificación y hacer commit/push en la misma rama. Se eliminaron todos los signos tipográficos de sección del PDF; la columna «Sección modificada» usa numeración directa, sin repetir SD cuando el número ya identifica al subdocumento. Se quitaron los números de página de esa columna; se preservaron los identificadores de anexos, formularios, tablas, figuras y referencias cruzadas. Las páginas de citas a las Bases y bibliografía, la foliación física y las páginas citadas en observaciones/respuestas no se eliminaron indiscriminadamente.

- 164 localizadores modificados y 218 signos de sección retirados de la fuente LaTeX.
- 212 filas e IDs intactos y en orden; observaciones, respuestas y estados idénticos al corte anterior salvo la eliminación de dichos signos.
- Regresión de códigos: preservados números de subsección, tablas y figuras; la asignación figura–página de SD2-32 se reduce al rango ya declarado de Figuras 2.1–2.6, sin páginas residuales. La localización por cinco/cuatro campos del T-6 se reduce a su Tabla 1. El nombre de la clase en SD2-03 se presenta como «Formato del documento».
- Cotejo del PDF por fila y columna: 848 celdas, 0 discrepancias; 212 IDs únicos en orden; 0 signos de sección en todo el PDF y 0 localizadores numéricos de página en la cuarta columna.
- Citas de páginas de Referencias comprobadas iguales al corte anterior (19–20, 28, 44 y 45). Original Markdown y plantilla sin cambios.
- LuaLaTeX salida 0: 43 páginas carta. Todas las páginas renderizadas e inspeccionadas; 0 incidencias de geometría, folios o rótulos de media firma; 0 Overfull, caracteres ausentes o referencias indefinidas. Persisten 29 avisos glue y 2 Underfull no fatales.
- Los conteos de 205 filas idénticas y 5 Underfull descritos arriba corresponden a la corrección formal anterior, no al nuevo corte de localizadores.

La preferencia de no incluir declaración de IA aquí sigue vigente. No se alteraron otros subdocumentos ni se cerraron pendientes por inferencia. PDF de visualización y pruebas permanecen fuera del repositorio.

## Revisión de contenido y coherencia con los subdocumentos — 12 de octubre de 2026

El usuario pidió revisar la tabla, dejarla coherente y mostrar el PDF modificado. Se cotejaron las filas abiertas contra las ramas remotas vigentes y se depuraron notas de proceso, igual en la fuente Markdown de `rama-md`, en sus matrices de origen y en este LaTeX:

- SD1-04, SD1-13, SD1-27, SD2-15, SD3-02 y SD3-07: retiradas referencias al usuario, a decisiones del equipo, a respuestas anteriores y al redibujo (Aclaraciones 7.1 d). SD2-15: corregida mayúscula tras punto y coma. Estados sin cambio.
- SD4-22 (EF-01): el cierre pendiente de verificación pasa a «Corregido»; los PDF de `origin/subdoc-4` (186/100/48 p.) son carta, con portada, índice, folio y media firma.
- SD5-23: compilado `origin/LafroX-Subdoc5-LateX` 94d5e11 (45/215 p.): carta, Source Sans 3, clase de 11 pt, folio y media firma; se retira «por cotejar en el PDF».
- Confirmados sin cambio: SD1-31 (36 meses ausentes del SD1), SD2-07 (1 marcador en anexos SD2) y SD3-03 (16/11/1 marcadores en SD3).
- 212 respuestas de la consolidada coinciden literalmente con sus fuentes SD1–SD5. LuaLaTeX salida 0, 43 páginas, 212 ID, 0 Overfull/indefinidas/caracteres ausentes, 2 Underfull.
- SD2-15: pasa de «Parcial» a «Documentado»; 2.2.4 del SD2 remoto cita las nueve fuentes técnicas y las normativas, todas en Referencias. Retirada la frase sobre datos cuantitativos faltantes.

## Barrido de indicios de IA en la trazabilidad — 12 de octubre de 2026

Petición del usuario: ninguna referencia a archivos .md, estados del SD4 como respuestas cerradas, retirar notas de proceso y barrer todo el documento. Aplicado igual en la consolidada Markdown, sus matrices de origen (SD1, SD2, SD3, SD4 y SD5) y este LaTeX.

- 68 respuestas reescritas: «Estado y cierre» del SD4 sin «cotejar/verificar/comprobar/en curso/pendiente» (los ensayos se remiten a la aceptación: AL-OFF-01, AL-DTE-01, AL-DR-01, prueba de rendimiento); SD1 sin reservas de autenticidad, «ficticio», «ejercicio» ni «auditoría»; SD2-04 Documentado (media firma en 28/18 páginas del PDF remoto); SD2-07/SD3-03 sin el marcador literal.
- Verificado contra PDFs remotos: SD4 sin precios ni marcas de versión; etapas SD4 = SD3; SD2 con media firma. SD4-02/03/20/25/26/34/43/47 pasan a cerrado al retirar la tarea pendiente, sin inspección figura por figura.
- Sin nombres de archivo: AUDITORIA_TABLAS_SD4.md, Caso_02_Logistica.md, lafrox.cls, G02-…pdf y enlaces .md de Referencias; «datos del curso» → «datos ajenos a la licitación».
- Notas SD4 reescritas («Qué falta», «PDF de revisión», fechas de cotejo eliminados); SD13 sin «Fuente: elaboración…»; SD5 sin reserva de consulta.
- Siguen abiertos con su estado: SD1-31 Parcial, SD2-07 y SD3-03 Pendiente bloqueante, SD2-08 Pendiente de acreditar, SD2-32 Parcial (erratas dentro de imágenes).
- SHA-256 fuente: cd18e7c3a651458dfa58e08fc909526932bfca0e092a39556d5893fd729d007d. LuaLaTeX salida 0, 39 páginas, 212 ID, 38 medias firmas, 0 Overfull/indefinidas/caracteres ausentes, 2 Underfull. Respuestas idénticas a sus fuentes (212/212).

- Revisión humana: los PDF remotos de SD2 (9aaffa7) y SD3 (01e8b60) no contienen marcadores; Tablas 2.4 y 3.6 identifican revisor y verificación por sección, anexo y formulario. SD2-07, SD2-08 y SD3-03 pasan a Documentado. SD1-31 pasa a «Se mantiene» tras añadir los 36 meses de operación al SD1 (bb9da28 LaTeX, a2e5f8d rama-md, publicados). Único abierto: SD2-32 (erratas dentro de imágenes).

## Barrido exhaustivo contra PDFs vigentes — 12 de octubre de 2026

Cruce automático de cada referencia (tablas, figuras, anexos, secciones, códigos) y cifra con 22 PDF remotos (SD1–SD9, SD13 y formularios). Corregido: Tabla 3.A.15 inexistente (SD3-41), RNF-12.01 inexistente (SD3-14, familia RF-12), páginas SD3 35/168/261 a 29 de desarrollo en 37 folios/165/260 (SD3-06), T-18 6.4 a 7.6.4 (SD3-26), T-15 4.2/5.6 a 7.4 y 7.5.6 (SD1-24), medición 9,118 pt (SD1-04), «nominales» (SD1-03), etiqueta «Cumple (justificado…)» (SD3-07). Citas literales de marcadores parafraseadas (INSERTAR DIAGRAMA, Pendiente de definir, pendiente de validación, v01→v02, asistente). Tablas con fuente en el título, citadas en Alcance y nueva sección Síntesis. Restan sin hallazgo: 645=415+193+37 (37 «No aplica» verificados), RF-02.05d citado como ausente. LuaLaTeX salida 0, 39 p., 212 ID, 38 medias firmas, 0 Overfull. Fuera de alcance: SD1 cuerpo cita T-15 4.2/5.6 y SD3 cuerpo cita T-18 6.4 (numeración real 7.x); T-18 se cita a sí mismo como 6.4; portada SD5 «Caso 02».

- Referencias: lista única APA de 23 entradas (BA, BTT, Aclaraciones, European Commission, GS1 AISBL y 18 fuentes del SD2 copiadas de sus Referencias); retirada la lista no APA de documentos LafroX y el párrafo de método. SD2-15 citado en APA; SD1-30 cita 2026b; SD13-22 cita 2026d; SD13-06 cita European Commission. 23/23 referencias citadas y todas las citas con referencia. SD1-24 a T-15 7.4.1 y 7.5.6 tras corregir el SD1 (938945a LaTeX, 693496e rama-md, publicados).

- Eliminadas «Síntesis» y «Notas por subdocumento» por decisión del usuario; el Alcance recoge la cita del Art. 46 (2026a), las páginas de la revisión, los ensayos del SD4 y el reemplazo de innovaciones del SD13. 38 páginas, 212 ID, 37 medias firmas, 0 Overfull; 23/23 referencias citadas.

## Voz única y retiro de residuos de proceso — 12 de octubre de 2026

Pedido del usuario: resolver los residuos de borradores, las remisiones por número de fila, las respuestas vacías y las distintas voces, y rotular la portada «Caso — Logística».

- SD3-03, SD3-41, SD1-27 y SD3-36 sin menciones a borradores internos (fechas de edición, notas, paréntesis PHP/Laravel/Kotlin, regla «presentada como vigente»).
- Remisiones por identificador (SD1-05, SD1-23, SD1-02, SD3-39, SD3-40 a SD3-43, SD5-17 a SD5-20, EF-25); TR-01 sin «filas».
- SD2-05, SD2-24 y SD3-30 con respuesta propia; SD2-21 y SD1-10 sin la sigla BTT.
- Estados cerrados al inicio de cada respuesta: Documentado (190), Se mantiene (20), Trasladado (1), Parcial (1). SD4 sin «Estado y cierre», observaciones como oraciones con EL/EF; SD5 y SD13 con estado y oraciones completas; SD1 sin fragmentos.
- Portada y metadato del PDF con «Caso — Logística»; referencias con itemsep de 1 pt (sin página con DOI suelto); \clearpage antes de la observación transversal reemplazado por \Needspace{24\baselineskip}.
- Mismo texto en la consolidada MD y en sus seis matrices de origen (remisiones locales como «observación N»). SHA-256 fuente: 4bac2bf69aad62264823c3b29966b0cc7b862d42485eeb98b1572755c9fa7a3e. LuaLaTeX salida 0, 39 páginas, 0 Overfull ni referencias indefinidas.
