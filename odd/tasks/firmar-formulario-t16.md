# Agregar firma al Formulario T-16 independiente

## Objetivo
Incorporar en el documento independiente `Lafrox-Subdocumento-T-16.tex` la misma firma de portada y de pie ya implementada para las dos salidas del SD8, sin cambiar la presentación ni el contenido del registro.

## Decisión de alcance
El usuario eligió el Formulario T-16 independiente. Se reutiliza el soporte existente `sd8-comun.tex`, dado que el formulario es una salida del Subdocumento 8. No se agrega un bloque nuevo dentro de las tablas ni se modifican los PDFs originales.

## Tareas
1. [done] Cargar el soporte de firma existente desde la raíz independiente del T-16 y usar su wrapper de portada.
2. [done] Compilar el T-16 en una copia temporal aislada e inspeccionar portada y página interior con pie.

## Resultado y verificación
- `Lafrox-Subdocumento-T-16.tex` carga `sd8-comun.tex` y usa `\LFXportadasd`; no se duplicó soporte ni se modificó la clase compartida.
- El PDF compiló en una copia temporal (28 páginas). Se inspeccionaron la portada (página 1) y una página de tabla en orientación horizontal (página 6): se ven la firma de portada y la firma de pie, sin solapamiento con la tabla.
- `git diff --check -- Lafrox-Subdocumento-T-16.tex` pasó. La compilación emitió avisos no fatales de `fvextra`/`lineno`.
- No se compiló ni sobrescribió el PDF del espacio original; no se creó commit por la restricción expresa del usuario.

## Resguardos
- Modificar solo `Lafrox-Subdocumento-T-16.tex` en el código fuente.
- Preservar los cambios preexistentes y los PDFs del proyecto; no compilar sobre el espacio original.
- No crear commits.
