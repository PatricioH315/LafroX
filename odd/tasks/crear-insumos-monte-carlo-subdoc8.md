# Preparar tablas de insumos para Monte Carlo en SD8

## Objetivo
Revisar el CSV vigente y agregar al anexo del Subdocumento 8 tablas trazables que preparen un análisis Monte Carlo sin presentar resultados de simulación no sustentados.

## Alcance y decisiones
- Fuente revisada íntegramente: `Datos externos/Tablas_tiesgos/(Nueva)LafroX-Riesgos-actualizadosr.xlsx - Riesgos LafroX.csv` (755 líneas).
- Separar la ponderación cualitativa de la Tabla 3 (que alimenta el porcentaje mostrado en T-16) de la probabilidad inicial de ocurrencia de la Tabla 4 (usada por las Tablas 6–7 para valor esperado). No tratarlas como el mismo dato.
- Para el anexo, la probabilidad inicial por riesgo se toma de la Tabla 4; el impacto condicional en HH, de las Tablas 5–6; el mes de ocurrencia, de la Tabla 8. Los objetivos residuales se identifican como escenario condicionado, no como entrada base mientras falte validación.
- No afirmar Monte Carlo de cronograma ni producir percentiles simulados: el CSV no contiene distribuciones de duración, vínculos a actividades/precedencias, ni estructura de dependencia/correlación. Registrar supuestos, límites y datos pendientes.
- Preservar los 45 riesgos actuales y los cambios locales; no sustituir PDF del proyecto. No crear commit sin autorización explícita.

## Tareas
1. [x] Revisar todas las secciones del CSV y reconciliar las fuentes/semántica de probabilidad, impacto HH, valor esperado, mes, respuesta y residual.
2. [x] Incorporar al anexo 8.B una matriz por riesgo con ponderación cualitativa vs probabilidad inicial QRA, objetivo residual, impacto HH, valor esperado y mes estimado; agregar tabla de disponibilidad/limitaciones del modelo. No se generaron resultados simulados.
3. [x] Verificar las 45 filas contra el CSV, estructura LaTeX, referencias, `git diff --check` y compilación a directorio temporal.

## Evidencia de exploración
- CSV: Tabla 3, líneas 69–118; Tabla 4, líneas 121–173; Tabla 5, 174–222; Tabla 6, 224–272; Tabla 8, 285–335; respuestas, Tablas 9–10, líneas 337–438; criterios de recálculo, líneas 609–622; método/validación, líneas 695–706.
- Tabla 6 usa probabilidad inicial de Tabla 4 (ej. R-001: 45 % × 152,0 HH = 68,400 HH), no la ponderación cualitativa 0,50 de Tabla 3.
- Totales fuente: impactos condicionales 5.585,6 HH; valores esperados 2.058,480 HH.
- Annex entrypoint actual: `LafroX-Subdocumento-8-Anexos.tex`; contiene 8.A y termina sin 8.B. La metadata ya anuncia 8.A–8.G.

## Evidencia de cierre
- 45 IDs únicos y consecutivos; siete celdas por fila. Las 405 verificaciones de valores contra Tablas 3–6 y 8 dieron cero diferencias; cada valor esperado coincide con probabilidad inicial de Tabla 4 × impacto HH dentro del redondeo mostrado.
- Totales coinciden con CSV Tabla 6: 5.585,6 HH de impacto condicional y 2.058,480 HH de valor esperado. Estos son valores analíticos de la fuente, no salidas simuladas.
- El prefijo del Anexo 8.A coincide con `git show HEAD:LafroX-Subdocumento-8-Anexos.tex`; el contenido nuevo comienza después de 8.A.
- `git diff --check` sin hallazgos. LuaLaTeX compila a `/tmp/lafrox-mc-annex-final2-20261011/`, PDF de 12 páginas; páginas 10–12 inspeccionadas, tabla de disponibilidad y conclusión legibles y sin página de continuación casi vacía.
- Advertencias restantes de paquetes: cambio de `\\@parboxrestore` y recomendación de orden `fvextra`/`csquotes`. Ningún PDF del proyecto fue reemplazado.
- Revisión nativa del candidato completada y aprobada; un hallazgo informativo no bloqueante señala límites de probabilidad en `08_plan_riesgos/contenido.tex:66–67`. La autoridad aprobada fue reconocida y quemada.
- Commit: no creado (requiere pedido explícito del usuario).
