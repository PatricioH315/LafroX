---
name: pdf-handling
description: Conformación y exportación de la propuesta final del proyecto LafroX en PDF: conversión de Markdown/Word a PDF, combinación de documentos, control de páginas y verificación del resultado. Usar cuando el usuario pida exportar, convertir, unir o generar PDF de la propuesta, informes o documentos del proyecto.
---

# PDF handling (propuesta final)

Conformación de la propuesta final de la licitación en PDF. El documento final
debe verse profesional, en español y con estructura de oferta.

## Herramientas típicas

- **Markdown → PDF**: `pandoc` (+ LaTeX o `weasyprint`), o herramientas tipo
  `md-to-pdf`. Tablas complejas conviene pasarlas por Excel/HTML antes de PDF.
- **Word → PDF**: LibreOffice headless (`soffice --headless --convert-to pdf`).
- **Unir PDFs**: `qpdf --empty --pages a.pdf b.pdf -- out.pdf` o `pdfunite`.
- **Verificar** siempre releyendo el PDF resultante (páginas, tablas, acentos,
  imágenes incrustadas).

## Contenidos que deben quedar en la propuesta

- Informes y subdocumentos conforme al T-22 (Informe 1: alcance y arquitectura;
  Informe 2/3: plan, riesgos y oferta según calendario).
- Diagramas exportados desde `Diagramas/` incrustados.
- Planillas (requerimientos, T-12, T-15, oferta económica) referenciadas o anexas.
- Cifras coherentes con el Cap. 15 y el cronograma de 56 meses.

## Reglas

- No exportar como PDF versiones intermedias sin avisar: el PDF final es un
  entregable oficial (sobre).
- Verificar que no existan referencias rotas a rutas del repo (las imágenes y
  tablas deben quedar embebidas).