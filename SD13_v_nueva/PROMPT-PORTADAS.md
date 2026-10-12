# Prompt reutilizable para las portadas

## Prompt

Adapta únicamente las portadas del Subdocumento 13 y sus derivados (cuerpo, anexos y Formulario T-19) al estilo de la imagen de referencia. La imagen pertenece a otro subdocumento: úsala como guía visual, nunca como fuente de los datos de esta entrega.

Conserva el tamaño carta vertical y la composición editorial limpia: fondo blanco, márgenes amplios, alineación izquierda y cabecera negra a sangre cuyo borde inferior asciende hacia la derecha. En la cabecera, coloca el isotipo naranja de LafroX y «LafroX SpA» en blanco a la izquierda, y el estado documental pequeño en gris a la derecha. Acompaña la diagonal con una franja naranja intensa y un segundo filo naranja claro, separados por blanco. Usa la tipografía sans serif existente y filetes grises finos; no conviertas la portada completa en una imagen.

Ordena los bloques como en la referencia:

1. «Licitación pública», identificador de la licitación, objeto del proyecto y «Caso — Logística». No escribir «Caso 02» ni «Caso 2».
2. Sello negro con el sobre de la oferta en blanco.
3. «Propuesta Técnica» como título principal; debajo, «Subdocumento 13 — Innovaciones» como subtítulo destacado. En una línea secundaria, «Informe 2 · [pieza]», donde [pieza] sea «Cuerpo del subdocumento», «Anexos 13.A a 13.D» o «Formulario T-19», según corresponda.
4. Datos del mandante y proponente a la izquierda; representante legal y contacto a la derecha.
5. Fecha de emisión propia del documento, sin sustituirla por la fecha del ejemplo ni por la fecha del sistema.
6. Firma existente sobre fondo blanco, línea de firma, nombre y cargo. Nomenclatura real del PDF abajo a la izquierda y folio abajo a la derecha.

Conserva los datos institucionales existentes, el número 13, el tema Innovaciones, el formulario T-19 y la nomenclatura individual de cada archivo. No copiar «Subdocumento 02», «Problema y necesidad», «Formulario T-7» ni el nombre del PDF del ejemplo. No inventar firmas, fechas ni datos. No modificar capítulos, tablas, diagramas, cifras, referencias ni otras ramas o subdocumentos. Reutiliza la plantilla compartida del paquete y recompila los tres PDF; verifica visualmente las tres portadas y que el contenido posterior no haya cambiado.

## Aplicación local

- `lafrox-portada.tex`: muestra el alcance como subtítulo destacado y el informe/pieza como línea secundaria; conserva la composición y paleta existentes, que ya coinciden con la referencia.
- `sd13-comun.tex`: centraliza «Caso — Logística» y «Subdocumento 13 — Innovaciones» para los tres documentos.
- La fecha de emisión se conserva en 05 de octubre de 2026. La imagen de referencia muestra otra fecha; no se adopta automáticamente.
