---
name: pdf-handling
description: Conformar, compilar y exportar la propuesta final en PDF (LaTeX/pdflatex y otros). Use cuando haya que compilar el informe LaTeX, resolver errores de compilación, ajustar overfull, exportar diagramas a PDF o generar el PDF de entrega del proyecto TFEP-01/2026. Trigger: "pdf", "pdflatex", "compilar latex", "main.tex", "exportar pdf", "overfull".
---

# pdf-handling — PDF y compilación LaTeX

Compila y conforma los documentos PDF de la propuesta, y exporta diagramas a PDF.

## Compilación LaTeX (productos/Informe*/)

- Documento raíz: `main.tex` (compilar desde el directorio del informe).
- Instrucción: `pdflatex -halt-on-error -interaction=nonstopmode main.tex`, dos
  pasadas para referencias cruzadas/TOC (rerun si aparece "Label(s) may have changed").
- Paquetes ya usados: `longtable` (tablas largas de catálogos), `tabularx`,
  `inputenc[utf8]`.

### Errores frecuentes y solución

- **Unicode no soportado por inputenc:** escapar caracteres no-Latin-1/UTF-8 básico
  (`−`U+2212, `≤`, `≥`, `→`, `×`, `°`) → `$-$`, `$\le$`, `$\ge$`, `$\rightarrow$`,
  `$\times$`, `\ensuremath{^\circ}`.
- **`\input` no encuentra archivo:** en `\input{...}` la ruta es relativa al
  directorio de `main.tex`, no del capítulo. Usar prefijo de carpeta, p. ej.
  `\input{03_esquema_solucion_alcance/catalogos/cat_rf}`.
- **Overfull hbox:** revisar columnas `p{}` de tablas; un overfull idéntico en
  todas las tablas longtable suele ser una celda no particionable o ancho de columna.
- **`\headheight` fancyhdr:** advertencia cosmética; se puede solventar con
  `\setlength{\headheight}{22pt}`.

## Exportación de diagramas a PDF/imagen

- Mermaid: `mmdc -i archivo.mmd -o salida.svg/png/pdf` (fuente de diagramas = texto).
- PlantUML: `curl https://kroki.io/plantuml/png` hacia imagen; se guarda en `Diagramas/`.
- Regla: la fuente de los diagramas vive en `.md` (versionable); los PNG/SVG/PDF
  exportados se guardan en `Diagramas/`.

## Conformado de entrega

- Reunir sobres/documentos según Art. 43.3 y nomenclatura TFEP-01/2026.
- Verificar que no queden `\pendiente` si la entrega es formal (o marcarlos como borrador).
- Validar número de páginas, referencias resueltas y ausencia de errores/undefined.