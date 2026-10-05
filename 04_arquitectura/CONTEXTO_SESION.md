# LafroX — Contexto del Subdocumento 4

## Estado vigente — 5 de octubre de 2026

Aplicación autorizada del plan SD3–SD4 con catálogo de quince actores validado por el equipo. Se incorporó el SD3 actual de Descargas en Markdown y la definición de actores, interfaces, acciones y etapas. La lógica del SD4 y sus partes incorporan esa correspondencia, etapa E1 de OTIF/telemetría, portales E2, tratamiento térmico graduado, reglas de promesa/reentrega, reversión con legado en lectura y CD-05. Anexos G/I/N/V incorporan contrato, volumen adicional, permisos y AL-STOCK-01/AL-ACT-01. Los canónicos lógicos ya no son idénticos a `732a9d6`: ese commit conserva la procedencia inicial. Física, centros de datos, 4-W y T-11 conservan la versión original. Las dependencias y límites están en [Coherencia SD3–SD4](COHERENCIA_SD3_SD4_2026-10-05.md). No regenerar con el convertidor histórico porque eliminaría estos cambios de diseño. Se verifica igualdad entre partes y consolidados antes de commit y push.

## Estado vigente: 3 de octubre de 2026

El usuario autorizó ejecutar `PLAN_ALINEACION_SUBDOC4.md`. Se actualizó exclusivamente `04_arquitectura/` en `alvaro-md` desde el contenido ensamblado de `rama-latex`, commit `732a9d6688569bf981594c2e21c47a167b8f8ba7`. La base de destino era `e377a58085c6f5c979a5bf176ecb710ce9239bbb`. Las referencias se leyeron desde Git; no se fusionaron ramas.

Entregables: [cuerpo 4.1–4.3](LAFROX-Subdocumento4.md), [anexos 4-A–4-W](LAFROX-Subdocumento4-Anexos.md) y [T-11](LAFROX-Formulario-T-11.md). El registro ADR-01–ADR-22 es único en 4-O; la memoria es 4-W; ambos quedan fuera del cuerpo.

Las partes conservan sus rutas históricas. Los consolidados anteriores que podían inducir a usar una versión antigua son páginas de navegación. Se actualizaron figuras al commit vigente, reglas de mantenimiento y manifiestos, conservando la procedencia histórica.

Se procesaron 61 fragmentos, 77 tablas y 822 filas de datos; se comprobó la representación de 3.828 celdas incluidos los encabezados, 258 párrafos sin comandos y 187 identificadores técnicos. Los resultados y sus límites constan en [VERIFICACION_ALINEACION.md](VERIFICACION_ALINEACION.md). Las discrepancias de fuente se conservan en [DISCREPANCIAS_FUENTE.md](DISCREPANCIAS_FUENTE.md).

No se hicieron commit, push, carga a Drive ni compilación LaTeX. Los archivos heredados fuera del capítulo 04 y `md para drive/` se conservaron. No usar esa carpeta antigua de exportación como versión alineada.

## Mantenimiento siguiente

Usar el commit fuente fijado y el manifiesto al revisar cambios posteriores. Para resolver una discrepancia técnica, registrar la decisión y modificar los documentos afectados explícitamente; una conversión no acredita cumplimiento. Mantener las partes y los consolidados coherentes.

## Historia de incorporación

El siguiente registro corresponde a la importación inicial y no al estado vigente:

## Contexto de incorporación de arquitectura lógica

Fecha: 1 de octubre de 2026.

### Petición y alcance

El usuario solicitó copiar Alex-MD a una rama llamada `alvaro-md`, añadir una carpeta 04 con el formato de las carpetas anteriores, crear dentro `logica 4.1` y trasladar a Markdown todo el contenido lógico del Subdocumento 4.1.

La copia se ubica en `D:/Usuario/Documents/Proyecto_Lafrox/LafroX-alvaro-md`. La rama de origen `arquitectura-alvaro` permanece en su checkout original. Esta incorporación no incluye arquitectura física ni centros de datos y no publica cambios en GitHub.

### Fuentes

- Base Alex-MD: `09ace4cea5b96ca641368c56996367ff7f26ea50`.
- Fuente arquitectura-alvaro: `e55133c2f91806af03f393776256a2feea23faa7`.
- Ensamblador lógico: `04_arquitectura/entrega_2/latex/04_arquitectura_logica/contenido.tex`.
- Ensamblador de anexos: `04_arquitectura/entrega_2/latex/04_arquitectura_logica/anexos/contenido.tex`.

### Resultado documental

Se convierten los 24 fragmentos del cuerpo y los 26 fragmentos de anexos, incluidos los 22 anexos A–V, 33 tablas con 350 filas de datos y las referencias a 14 figuras. Se conservan referencias, declaración de uso de IA, decisiones, supuestos y pruebas pendientes. Los diagramas se referencian por commit sin crear copias binarias.

Las correcciones efectuadas son de conversión: numeración de las capas, referencias de figura sin duplicación y sustitución de páginas por enlaces. No se armoniza el diseño con física ni se declara cumplida una prueba pendiente.

### Mantenimiento

El contenido heredado de Alex-MD se conserva byte por byte; las nuevas instrucciones y el manifiesto quedan dentro del capítulo 04. El cotejo de referencias del capítulo 3, la incorporación de 4.2/4.3 y la publicación de esta rama requieren trabajo posterior solicitado por el usuario.

La incorporación se registra en un commit local de `alvaro-md`. Se comprobaron 151 enlaces internos, las 33 tablas y 350 filas, 199 párrafos sin comandos y 114 identificadores conservados. No se ejecuta push ni se cambia la rama del checkout original.

### Actualización: importación de Markdown físico

El 1 de octubre de 2026 el usuario autorizó importar la carpeta Markdown física publicada en `rama-latex`. Se incorporaron 15 archivos desde `MD_4.2_2.3`, commit `95ed2c9a1cc20aa7ad9f3ebbe03cafa0e1e1259c`, dentro de `04_arquitectura/MD_4.2_2.3`. Incluye 4.2, 4.3, ADR, referencias, T-11 y memoria de cálculo, en 13 partes y un documento reunido, más README. El documento reunido conserva el nombre de origen pero no incluye 4.1.

Se adaptaron 39 enlaces a figuras y fuentes fijándolos al commit de origen. No se importaron LaTeX ni binarios, no se editó la lógica y no se armonizaron decisiones técnicas. Las huellas se registran en `MANIFIESTO_IMPORTACION_FISICA.md`. El usuario solicitó registrar y publicar esta importación en `alvaro-md`; se verificaron los 15 documentos, los 39 enlaces externos y los 81 enlaces locales antes del commit. No se alteran los capítulos heredados de Alex-MD.

## Mejora coordinada del Subdocumento 5 — 2026-10-03

Al ejecutar el plan aprobado se añadió `COMPLEMENTO_COORDINACION_DATOS_SD5.md` (CD-05): reserva comercial M2 nube, retención/movimientos locales y solicitudes por colas consumidas mediante conexión saliente. Los canónicos y sus partes conservan la conversión histórica de 732a9d6; este complemento es un cambio de diseño posterior con capacidad y ensayos por comprobar. SD1 ajusta exclusivamente la responsabilidad del líder de desarrollo al stack Laravel/PHP vigente.
