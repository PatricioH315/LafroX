# Plan de acción para la RBS de 33 riesgos
Documento de trabajo para rehacer el punto 8.3 del Subdocumento 8 con trazabilidad a los riesgos y a los resultados de 8.2.
La propuesta distinguirá controles existentes, respuestas propuestas y condiciones que siguen pendientes de decisión o evidencia.

## Specs
S1 — “ahora realiza todo el 8.3 con todos los insumos que tengas mas los resultados de los puntos anteriores”

## Tasks
- T1 | S1 | Route: inline — rehacer respuestas para R-001--R-033, reservas HH/calendario y condiciones de aceptación del punto 8.3, sin presentar propuestas como controles aprobados. | Commit: 439c8f7
- T2 | S1 | Route: inline — cotejar cobertura de IDs, cifras, fuentes oficiales, límites de evidencia, resolver referencias de versión en la introducción, revisar salida visual y compilación; registrar el commit de cierre. | Commit: 439c8f7

## Log
L1 — ahora realiza todo el 8.3 con todos los insumos que tengas mas los resultados de los puntos anteriores
L2 — Reescritura de 8.3 aplicada: matriz de respuesta propuesta para los 33 riesgos, cifras de exposición de 8.2 y reservas/aceptación actualizadas; la compilación de main.tex pasó y la matriz contiene 33 IDs únicos. T1 está implementado; T2 continúa con revisión visual/documental y cierre.
L3 — La primera revisión del PDF mostró que la introducción y las referencias a los Anexos 8.A–8.B aún describían la versión de 45 riesgos; se actualizaron para dejarla como versión anterior sin crosswalk y evitar usarla como base para los 33 riesgos actuales. También se sustituyó en escalas la remisión a 8.B por el análisis cuantitativo de 8.2.3. La compilación final pasó y las tablas de respuesta y reservas se inspeccionaron visualmente.
L4 — Cierre verificado: 33 IDs únicos en la matriz, cifras actuales y versión histórica distinguidas, sin mención del CSV en 8.3; `latexmk -lualatex -halt-on-error main.tex` y `git diff --check` pasaron. Código y documento de riesgos quedan en el commit 439c8f7.
