# LafroX — Corrección formal de la trazabilidad consolidada

## Causa y alcance

Se convirtió por error el contraste de auditoría de `Revision/`, no la matriz consolidada indicada por el usuario. El entregable se rehízo desde `Trazabilidad/LAFROX-Trazabilidad-Informe1-Consolidada.md` de `rama-md`, sin editar ese original. El usuario exige cuatro columnas exactas, los IDs originales y la base LaTeX de los otros subdocumentos; confirmó que no se incluya declaración de IA aquí.

## Entregable y plantilla

Archivo activo: `Trazabilidad/LAFROX-Trazabilidad-Informe1-Consolidada.tex`. `main.tex` y el antiguo punto de entrada de `Revision/` remiten a él: no compilan ya la auditoría por error.

Clase, portada y activo de firma copiados íntegramente del checkout vigente `LafroX-sd1-latex`. Hashes comparados: los tres archivos son idénticos. No se modificaron otros subdocumentos ni se atribuyó nueva revisión humana. La firma gráfica no se presenta como autenticación digital.

## Integridad y pruebas

- SHA-256 de la fuente: `e7f57d66685da0bc234619b83ec459d5fa92798bac15b02580cfe194a0b484b5`.
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
