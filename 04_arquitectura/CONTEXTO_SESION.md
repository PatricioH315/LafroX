# Contexto de incorporación de arquitectura lógica

Fecha: 1 de octubre de 2026.

## Petición y alcance

El usuario solicitó copiar Alex-MD a una rama llamada `alvaro-md`, añadir una carpeta 04 con el formato de las carpetas anteriores, crear dentro `logica 4.1` y trasladar a Markdown todo el contenido lógico del Subdocumento 4.1.

La copia se ubica en `D:/Usuario/Documents/Proyecto_Lafrox/LafroX-alvaro-md`. La rama de origen `arquitectura-alvaro` permanece en su checkout original. Esta incorporación no incluye arquitectura física ni centros de datos y no publica cambios en GitHub.

## Fuentes

- Base Alex-MD: `09ace4cea5b96ca641368c56996367ff7f26ea50`.
- Fuente arquitectura-alvaro: `e55133c2f91806af03f393776256a2feea23faa7`.
- Ensamblador lógico: `04_arquitectura/entrega_2/latex/04_arquitectura_logica/contenido.tex`.
- Ensamblador de anexos: `04_arquitectura/entrega_2/latex/04_arquitectura_logica/anexos/contenido.tex`.

## Resultado documental

Se convierten los 24 fragmentos del cuerpo y los 26 fragmentos de anexos, incluidos los 22 anexos A–V, 33 tablas con 350 filas de datos y las referencias a 14 figuras. Se conservan referencias, declaración de uso de IA, decisiones, supuestos y pruebas pendientes. Los diagramas se referencian por commit sin crear copias binarias.

Las correcciones efectuadas son de conversión: numeración de las capas, referencias de figura sin duplicación y sustitución de páginas por enlaces. No se armoniza el diseño con física ni se declara cumplida una prueba pendiente.

## Mantenimiento

El contenido heredado de Alex-MD se conserva byte por byte; las nuevas instrucciones y el manifiesto quedan dentro del capítulo 04. El cotejo de referencias del capítulo 3, la incorporación de 4.2/4.3 y la publicación de esta rama requieren trabajo posterior solicitado por el usuario.

La incorporación se registra en un commit local de `alvaro-md`. Se comprobaron 151 enlaces internos, las 33 tablas y 350 filas, 199 párrafos sin comandos y 114 identificadores conservados. No se ejecuta push ni se cambia la rama del checkout original.

## Actualización: importación de Markdown físico

El 1 de octubre de 2026 el usuario autorizó importar la carpeta Markdown física publicada en `rama-latex`. Se incorporaron 15 archivos desde `MD_4.2_2.3`, commit `95ed2c9a1cc20aa7ad9f3ebbe03cafa0e1e1259c`, dentro de `04_arquitectura/MD_4.2_2.3`. Incluye 4.2, 4.3, ADR, referencias, T-11 y memoria de cálculo, en 13 partes y un documento reunido, más README. El documento reunido conserva el nombre de origen pero no incluye 4.1.

Se adaptaron 39 enlaces a figuras y fuentes fijándolos al commit de origen. No se importaron LaTeX ni binarios, no se editó la lógica y no se armonizaron decisiones técnicas. Las huellas se registran en `MANIFIESTO_IMPORTACION_FISICA.md`. El usuario solicitó registrar y publicar esta importación en `alvaro-md`; se verificaron los 15 documentos, los 39 enlaces externos y los 81 enlaces locales antes del commit. No se alteran los capítulos heredados de Alex-MD.
