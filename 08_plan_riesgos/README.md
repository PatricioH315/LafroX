# Subdocumento 8 — Plan de riesgos

Las fuentes LaTeX reproducen el cuerpo, los Anexos 8.A–8.F y el T-16 vigentes.
Se conservan texto, cifras y los 18 campos pendientes de revisión humana.
La RBS se dibuja en TikZ y el modelo Python se mantiene literal con ajuste de líneas.

## Entradas independientes

Compilar desde la raíz del proyecto con LuaLaTeX:

~~~powershell
lualatex --interaction=nonstopmode --halt-on-error --jobname=LAFROX-Subdocumento8 08_plan_riesgos/LAFROX-Subdocumento8.tex
lualatex --interaction=nonstopmode --halt-on-error --jobname=LAFROX-Subdocumento8-Anexos 08_plan_riesgos/LAFROX-Subdocumento8-Anexos.tex
lualatex --interaction=nonstopmode --halt-on-error --jobname=LAFROX-Formulario-T-16 08_plan_riesgos/LAFROX-Formulario-T-16.tex
~~~

Repetir hasta estabilizar índices y referencias. main.tex monta sólo el cuerpo:
anexos y formulario son independientes. Se conservan la clase lafrox.cls,
la portada, los logotipos y la configuración común. Las tablas extensas de
anexos/formulario usan páginas horizontales con encabezado repetido; el cuerpo
permanece vertical. La fecha de entrega no se inventa y queda vacía.

## Actualizar desde Markdown

~~~powershell
python convertir_sd8.py --apply
~~~

Sin --apply, el conversor verifica párrafos, celdas y código sin escribir.
La presentación se valida compilando y revisando el PDF. Los marcadores de
revisión humana sólo se completan después de una revisión real.
