# Limpieza de notas visibles en las figuras lógicas — 26-10-2026

Solicitud del usuario: eliminar las notas de elaboración y los códigos internos D13/D15 visibles en las figuras, compilar el SD4 y no crear un commit todavía. El mensaje previsto para un commit posterior, solo cuando el usuario lo indique, es `correcciones menores`.

## Cambios

- Fuente editable: `04/figuras/fuentes/Arquitectura-logica-general-y-8-capas.drawio.xml`.
- Se vacían los ocho bloques de notas de las capas 1, 2, 3, 4, 5, 6 y 8, incluida la nota inferior de integración que remitía a «página 6». Se retiran frases como «Actores y canales del definitivo», «Destinos reproducidos del XML definitivo» y las explicaciones de conservación del dibujo recibido.
- Se eliminan `(D13)` y `(D15)` de los rótulos de Secrets Manager/SSM y MDM en la vista general y en la capa de seguridad. Se conserva N-13 como identificador del catálogo.
- Se actualizan los nueve PDF vectoriales insertados: ARQL-01 y ARQL-21 a ARQL-28. La edición de los operadores de texto de los PDF se realizó con pypdf, manteniendo las fuentes, las imágenes, las posiciones y las operaciones originales de dibujo. No se realizó una exportación nueva desde draw.io.
- El panel inferior vacío de integración se oculta con un rectángulo blanco vectorial; en el XML se dejan su relleno y borde sin color para que la siguiente exportación también lo suprima.
- No se cambian componentes, tecnologías, conexiones ni decisiones técnicas. No se corrigen en esta tarea otros pendientes de las figuras.

## Comprobación

Se compararon las operaciones de dibujo e imágenes de los nueve PDF contra las copias anteriores: se conservan todas. Solo se añade la operación de ocultar el panel vacío de integración. La comparación estructural del XML confirma que cambian únicamente doce atributos de texto y el estilo de ese panel; las coordenadas y conexiones permanecen iguales.

Se compila el cuerpo mediante `compilar.ps1 -SoloMain` (tres pasadas) y una pasada final de LuaLaTeX tras limpiar el panel vacío. El resultado es `entrega/LAFROX-Subdocumento4.pdf`, de 193 páginas. La extracción final verifica ausencia de las notas y de `(D13)`/`(D15)`, y presencia de N-13 y Secrets Manager. El registro final no contiene referencias indefinidas, caracteres faltantes ni desbordes Overfull. Se inspeccionan visualmente las nueve páginas afectadas del PDF compilado.

Los respaldos previos, el detalle de textos eliminados y la verificación quedan fuera del repositorio, en `../output/analisis_figuras_sd4_20261026/limpieza/`. Los anexos y el T-11 no requieren recompilación por esta limpieza de figuras del cuerpo.

La limpieza se dejó inicialmente sin preparar el índice, crear commit ni publicar cambios, conforme a la solicitud original. Posteriormente, el usuario autorizó el commit y su push con el mensaje acordado `correcciones menores`. El alcance de esa publicación comprende este registro, el XML, los nueve PDF de figuras y el cuerpo compilado. La compilación y esta limpieza no acreditan el cierre de otros pendientes de legibilidad o contenido del SD4.

Antes de publicar se integran por avance directo los tres commits remotos nuevos, hasta `479807ee`, conservando sus ajustes de frío en ruta, AS2 y referencias cruzadas. Se recompila el cuerpo con esa base y la limpieza de figuras para evitar reemplazar el PDF remoto por una versión anterior. Los archivos ajenos sin seguimiento se mantienen fuera del commit.
