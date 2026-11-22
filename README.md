# LafroX — Subdocumento 10 (borrador revisado)

Servicios de operación y niveles de servicio, versión 0.5 del 21 de noviembre de 2026. Rama hija `LafroX-Subdoc10-LateX-corrigiendo`, creada desde `origin/LafroX-Subdoc10-LateX` en `3faaec7ac6ab05a2bb7c0b7187584ad59b0b81e4`.

## Entregables

- `LAFROX-Subdocumento10.pdf`: capítulo 10, servicios, dimensionamiento y niveles de servicio.
- `LAFROX-Subdocumento10-Anexos.pdf`: memoria de cálculo, indicadores, recuperación, brechas y matriz de requisitos.
- `trazabilidad/SD10_fuentes_y_brechas.md`: registro auxiliar de fuentes, versiones, localizaciones y decisiones. No sustituye un subdocumento LaTeX.
- `trazabilidad/fuentes_sd10.json`: versiones y huellas de las fuentes consultadas.
- `trazabilidad/calculos_sd10.json`: reproducción del modelo y resultados.

## Compilación y verificación

La revisión 0.5 alinea los sitios con el SD4 y amplía el dimensionamiento de soporte, los acuerdos propuestos y la medición. La trazabilidad conserva los cortes anteriores y los respaldos de la nueva revisión.

Se usa la clase corporativa heredada, sin modificaciones, y LuaLaTeX con sus fuentes y paquetes. Desde esta carpeta:

```powershell
python verificacion/comprobar_calculos.py
latexmk -lualatex -interaction=nonstopmode -halt-on-error -jobname=LAFROX-Subdocumento10 main.tex
latexmk -lualatex -interaction=nonstopmode -halt-on-error -jobname=LAFROX-Subdocumento10-Anexos anexos.tex
```

Después de compilar, ejecutar python verificacion/comprobar_entrega.py (requiere pypdf).

Revisar log, referencias, índices, folios, tablas y diagramas, y renderizar todas las páginas antes de publicar. Las bases y aclaraciones pueden consultarse en Markdown; las fuentes de subdocumentos y formularios usadas son LaTeX y sus PDF correspondientes.

## Alcance y limitaciones

La redacción reúne lo respaldado por las fuentes publicadas y reproduce las hipótesis de SD4 y T-15. El modelo no acredita abandono, resolución al primer contacto, turnos asignados ni ensayos realizados. Las brechas B-01 a B-11 requieren datos o conciliación documental; N/A indica falta de respaldo específico, no un valor cero. SD11 y SD12 son dependencias documentales del plan de operación y dotación. No se incluyen precios, firmas ni revisiones humanas no acreditadas. Este trabajo no modifica el modelo financiero ni otros subdocumentos.
