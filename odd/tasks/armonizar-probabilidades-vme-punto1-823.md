# Armonizar probabilidades y cuantificar HH — punto 1 de 8.2.3

## Objetivo
Implementar solamente el primer punto acordado: armonizar T-16 con las probabilidades iniciales de ocurrencia del registro vigente y reemplazar el análisis heredado de 8.2.3 por el valor esperado de impactos en HH. Dejar Monte Carlo de exposición, Monte Carlo de cronograma, FMEA y FTA para puntos posteriores, que requieren una nueva orden del usuario.

## Alcance y decisiones
- Usar el registro de riesgos actualizado como fuente de trabajo; no citar en el texto oficial del Subdocumento 8 nombres de CSV, rutas externas ni numeración de tablas de archivos de consulta.
- En T-16, mostrar el nivel ordinal cualitativo P y, por separado, la probabilidad inicial cuantitativa p₀, separados por `/`. No recalcular el P ordinal con p₀: son dos insumos distintos. Las bandas no solapadas de la escala cualitativa (`0% ≤ q < 20%`→1; `20% ≤ q < 40%`→2; `40% ≤ q < 60%`→3; `60% ≤ q < 80%`→4; `80% ≤ q ≤ 100%`→5) se aplican a la ponderación cualitativa q, no a p₀. Impacto y exposición permanecen ordinales; exposición = nivel P × nivel I.
- Valor esperado por riesgo: `VE_i = p_i × impacto condicional_i (HH)`. La suma actual de los valores esperados es 2.058,480 HH; esto no es una reserva, un percentil de Monte Carlo ni un resultado de cronograma.
- Rehacer solamente la subsección 8.2.3 para presentar valor esperado; no desarrollar todavía los siguientes puntos. Limpiar en T-16 y Anexo 8.B las alusiones a archivos/tablas externos como fuentes oficiales. Referir el Anexo 8.B por nombre, no con `\\ref` entre documentos compilados por separado. Alinear la introducción general y la declaración de uso de IA con el contenido efectivamente incluido, sin afirmar FMEA/escenarios como completados. Indicar que la simulación de cronograma sigue pendiente. Al retirar la antigua Tabla 8.5, renumerar la tabla posterior 8.6→8.5 solo para cerrar la secuencia, sin alterar su contenido.
- Preservar cambios ajenos, no tocar el MD/PDF externo añadido por el usuario, no sustituir PDFs del proyecto y no crear commit sin autorización explícita.
- Rama actual: `Lafrox_Subdocumento_8_Latex_Nuevo`, un commit detrás de origin por cambios a RBS/EDR. No integrar ni cambiar de rama en esta tarea.

## Tareas
1. [done] Armonizar las bandas cualitativas y los 45 porcentajes p₀ de T-16, preservando P ordinal y exposiciones.
2. [done] Sustituir 8.2.3 por valor esperado HH, hacer autosuficiente Anexo 8.B y alinear las afirmaciones generales/IA; reparar referencias/numeración sin desarrollar el siguiente punto.
3. [done] Verificar datos, referencias, `git diff --check` y compilar T-16/SD8 en rutas temporales. La comparación independiente previa pasó; una segunda invocación Python autorizada falló por un regex del verificador (`None.group`), no por una aserción de datos.
4. [in_progress] Resolver la revisión nativa del candidato; el lineage `review-28d2b6de4050193f` sigue en `reviewing` con un slot de captura y los intentos de binding exacto fueron rechazados sin ejecutar reviewer.

## Evidencia de origen
- Fuente de trabajo: `Datos externos/Tablas_tiesgos/(Nueva)LafroX-Riesgos-actualizadosr.xlsx - Riesgos LafroX.csv`.
- Las probabilidades iniciales de ocurrencia se distinguen de las ponderaciones cualitativas previas; el valor esperado vigente total es 2.058,480 HH para 45 riesgos.
- Riesgos de implementación: `Lafrox-Subdocumento-T-16.tex`, `08_plan_riesgos/contenido.tex`, `LafroX-Subdocumento-8-Anexos.tex`.

## Evidencia de cierre
- `git diff --check`: terminó con código 0.
- Una verificación independiente previa cotejó 45 IDs, ordinales cualitativos, p₀, exposiciones, impactos condicionales y valores esperados; informó 5.585,6 HH condicionales y 2.058,480 HH esperados, sin discrepancias. Las filas numéricas no cambiaron después de esa comparación. La re-ejecución autorizada con `python -c` terminó con `AttributeError: 'NoneType' object has no attribute 'group'` dentro del verificador antes de las aserciones; no se interpreta como diferencia de datos.
- LuaLaTeX T-16: código 0, PDF temporal de 28 páginas en `/tmp/lafrox-point1-final-verify-20261011/t16/`. SD8 completo: código 0, PDF temporal de 17 páginas en `/tmp/lafrox-point1-final-verify-20261011/sd8/`; no quedaron referencias sin resolver tras las re-ejecuciones.
- Advertencias no bloqueantes: `\\@parboxrestore`, orden `fvextra`/`csquotes`; en SD8, PDF 1.7 del diagrama RBS excede el límite configurado 1.5.
- No corresponde prueba unitaria para este cambio documental. No se sustituyeron PDFs del proyecto ni se creó commit.
- La revisión nativa sigue abierta: lineage `review-28d2b6de4050193f`, transición `collect` (`reviewer_results_required`), lente `review-reliability`. Los intentos de captura rechazaron el binding con `mutation_performed:false`; no se ejecutó ni admitió resultado de reviewer. No se afirma aprobación.

Punto 2 de la propuesta queda detenido hasta nueva instrucción explícita del usuario. Antes de avanzar debe resolverse la captura nativa pendiente. Rama local no sincronizada: un commit detrás de origin por cambios RBS/EDR; no se integró.
