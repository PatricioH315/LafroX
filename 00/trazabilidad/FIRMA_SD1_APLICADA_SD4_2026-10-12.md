# LafroX — Formato de firma del SD1 aplicado al SD4

Fecha: 12 de octubre de 2026. Petición explícita del usuario: analizar las otras ramas y traer el formato de firma del Subdocumento 1 LaTeX. Destino: checkout `subdoc-4`. Sin commit ni push.

## Fuente y alcance

Se actualizaron las referencias remotas y se compararon los bloques de firma del SD1, SD2, SD3 y SD13. Fuente principal: `LafroX-Subdoc1-LateX`, commit 05fe9c947e65080357daece0794675cbd9f2603c. SD2 y SD3 comparten el bloque de media firma; SD13 utiliza un bloque equivalente con una ruta propia.

Se importan exclusivamente el bloque de firma de portada, el pie de media firma y el recurso gráfico existente. Se preserva el resto de la plantilla SD4, incluida su información de portada. La imagen se copia sin modificación; no se dibuja ni genera otra firma.

SHA-256 de la imagen: `9110733598c0c51293c5c49e075c92e8eae38007db4cf6bd6e019d584c6b3208`.

## Aplicación

- Plantilla común `00/plantilla/formato-base/lafrox.cls`: media firma con imagen de 18 puntos de alto, línea de 3,4 cm, nombre y folio; opción `sinfirma` conserva solo el folio.
- Portada común `lafrox-portada.tex`: imagen de 3,4 cm de ancho, línea y datos del representante, siguiendo el bloque del SD1.
- Imagen en `00/plantilla/formato-base/logo/FIRMA_Alex_Aravena_transparente.png`; rutas explícitas en `main.tex`, `04/anexos_logica.tex` y `04/formulario_T11.tex`.
- Páginas horizontales: ajuste del pie del T-6 de SD1 adaptado a todos los entornos `landscape`; el interruptor cambia después de los saltos de entrada/salida, evitando mover el pie de la página vertical anterior. Firma y folio quedan en el extremo inferior derecho de la hoja orientada.

## Verificación

Los tres entregables compilaron con LuaLaTeX y tres pasadas: cuerpo 201 páginas, anexos 100 y T-11 48. Los conteos coinciden con el estado previo a importar la firma. Logs finales sin referencias indefinidas, cajas desbordadas, caracteres faltantes ni avisos de altura insuficiente del pie.

Se inspeccionaron nueve PNG: portadas, páginas 2 y páginas horizontales del cuerpo (13), anexos (82) y T-11 (5). Firma y folio visibles, sin superposición con el contenido. Se comprobó la presencia textual del rótulo de media firma en la página 2 de los tres PDF; el cotejo visual valida su colocación. Imágenes de QA en `04/revision/firma_20261012/`.

Se preservan los finales CRLF de las dos plantillas originales; el control de whitespace se ejecuta con `core.whitespace=cr-at-eol`, sin modificar la configuración persistente del repositorio. No se modifica el contenido técnico de `partes/`, `anexos/` ni `formularios/`.

La aplicación del recurso de firma solicitado no acredita una revisión humana nueva del contenido ni cambia los estados de aceptación técnica de la tabla de trazabilidad.

## Integracion remota y publicacion

Pull fast-forward de `subdoc-4` desde `7ba8608` a `5899782`, conservando la fecha y declaracion IA remotas. Firma integrada sin conflictos de contenido. Los otros cambios locales quedan respaldados en stash `b749d0a8575078bcadf2b41bdf3ed18e2d598f42` y se reaplican despues de publicar esta unidad de firma. Los tres PDF se recompilaron con tres pasadas y se comprobaron los logs y el rotulo de media firma.
