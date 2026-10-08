# Subdocumento 3 — Consolidación de trabajo

Fuentes: Bases y subdocumentos 1 y 2. No se asume revisada la documentación posterior.

- `LAFROX-Subdocumento3.tex`: cuerpo (`contenido.tex`), 3.1–3.4, tres figuras conceptuales y cierre de referencias/IA.
- `LAFROX-Subdocumento3-Anexos.tex`: anexos 3.A–3.K, campos vacíos y notas visibles.
- `LAFROX-Formulario-T-12.tex`: archivo independiente; no declara cumplimiento ni trazabilidad completos.

## Datos y regeneración

`tablas/generador/consolidado.json` es el registro activo: 174 identificadores RF (31 desarrollados), 90 RNF (13 con umbral), decisiones y correspondencias. Lo no respaldado queda vacío. `datos_rt.py` lee los 374 códigos directamente de las Bases, sin consultar arquitectura.

Ejecutar `python -B tablas/generador/gen.py` desde esta carpeta. Editar los datos activos antes de regenerar, no las tablas resultantes. El generador no asigna módulos, EDT, pruebas ni «Cumple» por defecto. La declaración IA se mantiene en sus fragmentos dedicados.

`latexmk` compila los tres documentos con LuaLaTeX. La opción de clase `final` controla la presentación, no acredita cierre: esta versión contiene notas de trabajo autorizadas, incompatibles con una entrega formal hasta resolverlas.

Los fragmentos anteriores que no están incluidos por los documentos activos no son fuente de la consolidación. Los documentos 1 y 2 permanecen sin cambios. Las discrepancias se registran en el Anexo 3.H y en la bitácora de observaciones. No se reutilizan `main.pdf` ni otros PDF anteriores como salida vigente.
