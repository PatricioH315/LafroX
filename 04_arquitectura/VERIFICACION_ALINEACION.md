# LafroX — Verificación de alineación

Fecha: 3 de octubre de 2026. Fuente `rama-latex`, `732a9d6688569bf981594c2e21c47a167b8f8ba7`.

## Resultados

```json
{
  "source_commit": "732a9d6688569bf981594c2e21c47a167b8f8ba7",
  "base_commit": "e377a58085c6f5c979a5bf176ecb710ce9239bbb",
  "fragments": 61,
  "tables": 77,
  "data_rows": 822,
  "cells_including_headers": 3828,
  "figures": 26,
  "tikz_figures": 4,
  "plain_paragraphs_checked": 258,
  "identifiers_checked": 187,
  "documents": {
    "LAFROX-Subdocumento4.md": {
      "tables": 40,
      "rows": 303
    },
    "LAFROX-Subdocumento4-Anexos.md": {
      "tables": 36,
      "rows": 429
    },
    "LAFROX-Formulario-T-11.md": {
      "tables": 1,
      "rows": 90
    }
  },
  "chapter_markdown_files_checked": 32,
  "local_links_checked": 579,
  "explicit_anchors_checked": 808,
  "tracked_changes_outside_chapter": 0
}
```

Se cotejó la representación de todas las celdas y la estructura de filas de las 77 tablas del ensamblado. Los conteos de filas incluyen las filas de agrupación del T-11, que usa celdas combinadas en el fuente; en Markdown se conserva su texto en la primera columna y se completan las demás columnas vacías.

Los 258 párrafos comprobados son bloques de texto sin comandos LaTeX cotejados mediante normalización. Los demás bloques fueron procesados por el conversor, que rechaza comandos desconocidos. Este control no equivale a una revisión humana exhaustiva de cada oración o a una auditoría de cumplimiento. Los 187 identificadores técnicos se verificaron presentes.

Se verificaron las referencias internas, ausencia de anclas duplicadas y comandos LaTeX residuales en documentos vigentes. Las 26 figuras externas se comprobaron como blobs existentes y se registraron sus SHA-256. Los cuatro diagramas TikZ conservan enlaces al fuente y rótulos, sin reconstrucción gráfica.

## Organización y preservación

- Cuerpo: 4.1–4.3, Referencias y Declaración de uso de IA; sin T-11, memoria ni antiguo capítulo 4.4.
- Anexos: 4-A–4-W; registro único ADR-01–ADR-22 en 4-O y memoria en W.
- T-11: documento separado, convertido de la versión publicada.
- Cambios limitados a Markdown bajo `04_arquitectura/`; sin modificaciones en los capítulos heredados, índice Git ni carpeta `md para drive/`.
- Rama de trabajo: `alvaro-md`; sin commit ni push.

Los valores de diseño, supuestos y revisión humana pendiente conservan el estado de la fuente. Consultar [Discrepancias de fuente](DISCREPANCIAS_FUENTE.md) antes de una entrega final.
