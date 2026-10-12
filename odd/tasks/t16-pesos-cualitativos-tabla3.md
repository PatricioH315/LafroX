# Actualizar las ponderaciones de T-16 con la Tabla 3

## Objetivo
Actualizar el Formulario T-16 para mostrar, junto al nivel ordinal de Probabilidad e Impacto, los valores decimales cualitativos escritos exactamente como aparecen en la Tabla 3 del registro de riesgos, con coma decimal y sin convertirlos a porcentajes.

## Alcance y decisiones
- En las columnas existentes, usar `nivel ordinal / valor decimal de Tabla 3`: por ejemplo, Prob. `3 / 0,50` e Impacto `2 / 0,40`.
- Reproducir los valores `0,30`, `0,50`, `0,20`, `0,40` y `0,80` exactamente, sin signo `%` ni conversión a 30%, 50%, 20%, 40% u 80%.
- Preservar los niveles ordinales P/I y la Exposición P×I actuales; no recalcularlos a partir de esos valores decimales.
- Explicar que son ponderaciones cualitativas, no frecuencias observadas, estimaciones cuantitativas p₀ ni porcentajes de pérdida. No presentar el CSV externo como fuente oficial del Subdocumento 8.
- Mantener el punto 2/Monte Carlo del Subdocumento 8 en pausa. No tocar el cuerpo/anexos de SD8, no reemplazar PDFs del proyecto ni crear commits.

## Tareas
1. [done] Corregir la explicación introductoria y las 45 filas de T-16 para reproducir los valores decimales exactos de Tabla 3, sin `%`.
2. [in_progress] Verificar las 45 correspondencias exactas por ID, la preservación de P/I y Exposición, `git diff --check` y una compilación T-16 segura a temporal.

## Evidencia inicial
- Fuente de trabajo: `Datos externos/Tablas_tiesgos/(Nueva)LafroX-Riesgos-actualizadosr.xlsx - Riesgos LafroX.csv`, Tabla 3, columnas `Probabilidad` e `Impacto`.
- Muestra de la notación porcentual anterior, ahora supersedida: R-001 aparecía como `3 / 50%` y `2 / 40%`. La corrección solicitada es `3 / 0,50` y `2 / 0,40`, exactamente como en Tabla 3.
- Verificación independiente actualizada: 45 filas, ambos valores decimales exactos por ID; ordinales P/I y Expos. iguales a HEAD; introducción sin caracterizar los valores como porcentajes. `git diff --check` terminó con código 0.
- La primera compilación LuaLaTeX terminó reportando un PDF de 28 páginas, pero MiKTeX ignoró el destino temporal y escribió `Lafrox-Subdocumento-T-16.pdf`, `.log` y `.aux` en la raíz del proyecto. `git status` ahora muestra el PDF modificado, con mtime UTC `2026-10-12T00:34:23`. No se ejecutó la segunda pasada ni se restauró/limpió el PDF. Compilación segura a temporal pendiente de resolver la salida; pedir autorización antes de restaurar el PDF desde HEAD o conservar el generado.
- Implementación revisada en `Lafrox-Subdocumento-T-16.tex:19,28–72`: se muestran P/ponderación de probabilidad e I/ponderación de impacto; R-001 es `3 / 50\%` y `2 / 40\%`.
- Verificación independiente: 45 IDs coincidentes y únicos; porcentajes de Tabla 3 exactos; P, I y Expos. iguales a HEAD.
- `git diff --check -- Lafrox-Subdocumento-T-16.tex`: código 0.
- LuaLaTeX T-16 ejecutado dos veces en `/tmp/lafrox-t16-table3-verify-20261011/`; ambas ejecuciones código 0, PDF temporal de 28 páginas, sin referencias sin resolver ni advertencias bloqueantes. Advertencias no bloqueantes: `\\@parboxrestore` y orden de carga `fvextra`/`csquotes`.
- No se compiló SD8, no se reemplazó PDF del proyecto y no se creó commit.
- El usuario dejó en pausa el punto 2/Monte Carlo. El inspect nativo actual devolvió target `sha256:584cfcdf…`, con rutas rastreadas `08_plan_riesgos/contenido.tex`, `Lafrox-Subdocumento-T-16.pdf`, `Lafrox-Subdocumento-T-16.tex` y el task doc previo; también exige seleccionar el task doc nuevo untracked antes de START. No ejecuté START manualmente. El intento previo de selección arrojó `stale_target_identity` asociado a `review/start` (`lineage_created=false`); el estado actual volvió a ofrecer selección. No se ejecutó reviewer ni hay aprobación. La modificación local de `08_plan_riesgos/contenido.tex` se dejó intacta.
- Incidente de compilación: aunque se indicó un directorio temporal, MiKTeX reportó haber escrito `Lafrox-Subdocumento-T-16.pdf`, `.log` y `.aux` en la raíz. `git status` marca el PDF rastreado como modificado (mtime UTC `2026-10-12T00:34:23`). No hubo segunda compilación ni restauración/limpieza; esperar autorización para restaurar el PDF desde HEAD o conservarlo.
