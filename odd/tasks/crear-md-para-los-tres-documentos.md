# Crear versiones Markdown de los tres documentos

## Objetivo
Crear un archivo Markdown por cada documento PDF vigente y guardarlos bajo `MD_documentos/`.

## Alcance y fuentes
- `MD_documentos/main.md` a partir del documento de cuerpo SD8 (`main.tex` y `08_plan_riesgos/contenido.tex`).
- `MD_documentos/LafroX-Subdocumento-8-Anexos.md` a partir de `LafroX-Subdocumento-8-Anexos.tex`.
- `MD_documentos/Lafrox-Subdocumento-T-16.md` a partir de `Lafrox-Subdocumento-T-16.tex`.

Usar las fuentes LaTeX como referencia canónica, preservar títulos, prosa, referencias, 45 riesgos y contenidos de las tablas/fichas. Markdown no reproduce paginación ni diseño PDF exactamente; estructurar tablas anchas para legibilidad sin omitir celdas.

## Tareas
1. [done] Convertir el cuerpo SD8 en `MD_documentos/main.md`.
2. [done] Convertir la apertura y los riesgos R-001–R-015 del Anexo 8.A.
3. [done] Completar todos los campos de los riesgos R-016–R-030 del Anexo 8.A.
4. [done] Completar todos los campos de los riesgos R-031–R-045 del Anexo 8.A.
5. [done] Convertir la tabla de valores esperados del Anexo 8.B para R-001–R-015.
6. [done] Añadir las filas R-016–R-030 de la tabla de valores esperados.
7. [done] Añadir las filas R-031–R-045 de la tabla de valores esperados.
8. [done] Convertir parámetros, contingencia, texto de cierre y referencias de anexos.
9. [done] Convertir la apertura y los riesgos R-001–R-015 del Formulario T-16.
10. [done] Añadir los riesgos R-016–R-030 del Formulario T-16.
11. [done] Añadir los riesgos R-031–R-045 y las tablas/declaraciones finales del T-16.
12. [done] Corregir escapes LaTeX y notas de alcance en Markdown.
13. [done] Revalidar cobertura completa, formato y referencias; preservar PDFs y fuentes.

## Verificación final
- Se generaron `MD_documentos/main.md`, `MD_documentos/LafroX-Subdocumento-8-Anexos.md` y `MD_documentos/Lafrox-Subdocumento-T-16.md`.
- Validación automatizada: Anexo 8.A tiene 45 fichas con los 12 campos; Anexo 8.B contiene 45 filas cuyos valores coinciden con la fuente LaTeX; T-16 tiene 45 filas cotejadas celda por celda, siete referencias y la declaración de IA. Las siete condiciones pendientes de cuantificación y los totales se conservaron.
- Los enlaces locales de `main.md` resuelven; no hay tabuladores, escapes `\\%` ni entornos TeX crudos; `git diff --check` pasó.
- No se compilaron PDFs como parte de la conversión ni se restauró ninguno. El estado actual de Git reporta `LafroX-Subdocumento-8-Anexos.pdf` y `Lafrox-Subdocumento-T-16.pdf` modificados frente a la versión registrada; el origen de esos cambios no pudo determinarse. Se dejaron intactos.
- No se modificaron fuentes LaTeX para esta tarea y no se creó commit.

## Corrección tras inspección
La validación estructural inicial solo contó IDs y detectó que R-016–R-045 del Anexo 8.A carecían de fichas completas. Se completaron en bloques y se verificaron los doce campos por riesgo. También se repararon operadores matemáticos, escapes de porcentaje, metadatos parciales y el encabezado de categoría erróneo. Los conteos de IDs no bastan: cada ficha debe conservar el contenido sustantivo del origen; la validación final lo comprueba.

## Ajuste de plan
La conversión inicial del Anexo 8.A no produjo un archivo. Se divide la generación de las dos tablas extensas y las fichas/filas de riesgo en tramos acotados para evitar truncamiento y facilitar la comprobación de cobertura.

## Resguardos
- No modificar los `.tex`, los PDFs ni el PNG externo.
- Mantener las cifras y estados pendientes como están en las fuentes; no inventar contenido.
- No crear commits.
