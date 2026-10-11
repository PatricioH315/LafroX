# Pasar en limpio el registro de riesgos del T-16

## Objetivo
Reemplazar el marcador de tabla del Formulario T-16 con el punto 3 del CSV externo, manteniendo intactas las ediciones preexistentes y presentando el registro de forma legible en LaTeX.

## Alcance y decisiones
- Archivo destino confirmado: `Lafrox-Subdocumento-T-16.tex` (no existe el nombre `Lafrox-Subdocumento-1-16.tex`).
- Fuente: sección 3 de `Datos externos/Tablas_tiesgos/(Nueva)LafroX-Consolidado-Riesgos-SD8.xlsx - Riesgos LafroX.csv`.
- Se usan los 45 riesgos del CSV (`R-001`–`R-045`), con siete campos por riesgo, incluidas probabilidades e impactos fraccionarios. El texto introductorio declara que son ponderaciones cualitativas decimales y que la zona se determina por su producto.
- No se modificaron el CSV ni otros documentos. Se preservaron los cambios locales preexistentes ajenos a la tabla/afirmaciones de conteo del T-16.
- No crear commit sin solicitud explícita.

## Tareas
1. [x] Inspeccionar las filas del CSV y el contexto T-16.
2. [x] Incorporar el registro completo de la sección 3 en el marcador de T-16 y alinear la descripción a los datos fuente.
3. [x] Compilar/verificar el documento y revisar el diff para confirmar integridad, conteo y preservación de cambios preexistentes.

## Evidencia
- La sección 3 del CSV contiene 45 riesgos, columnas ID/RBS/enunciado/propietario/probabilidad/impacto/zona. La tabla final ocupa `Lafrox-Subdocumento-T-16.tex:29–74`.
- Un cotejo automatizado UTF-8 previo al último ajuste visual confirmó los 45 IDs, los siete campos y los valores correspondientes; luego se ajustaron únicamente los anchos de columnas.
- Compilación final autorizada con LuaLaTeX/latexmk en directorio temporal: exit 0; PDF de 15 páginas. Se ejecutó `git diff --check` sin errores de whitespace.
- Inspección visual de la página de tabla 6: apaisada, sin recortes; nombres de responsables y encabezado de Probabilidad ahora caben mejor. La tabla continúa en varias páginas.
- Persisten advertencias de paquetes ya observadas (`\\@parboxrestore` y orden de carga `fvextra`/`csquotes`); no impidieron compilar. Git mostró aviso de conversión LF→CRLF al tocar el archivo.
- No se creó commit. Los artefactos preexistentes no relacionados del árbol de trabajo se dejaron intactos.
