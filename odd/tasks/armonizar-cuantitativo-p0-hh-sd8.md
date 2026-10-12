# Armonizar el análisis cuantitativo SD8 con p₀ × HH

## Objetivo
Reconciliar la cuantificación de riesgos de SD8 con el registro actual de 45 riesgos (R-001…R-045), aplicando la decisión del usuario de tomar la suma de p₀ × HH como reserva de contingencia expresada en HH.

## Decisiones y reglas
- Valor esperado por riesgo: `VE_i = p₀_i × HH_condicional_i`.
- Total de 2.058,480 HH, ya verificado contra el registro actual, se adopta por decisión explícita del usuario como reserva de contingencia en esfuerzo; no confundir con monto en CLP ni resultado Monte Carlo.
- Mantener p₀ cuantitativa separado de los valores cualitativos qP/qI de la Tabla 3.
- No convertir objetivos residuales en reserva disponible sin eficacia acreditada.
- CSV es insumo de trabajo, no fuente oficial para citar en el SD8.
- No existe crosswalk R8↔R-001…R-045; retirar afirmaciones y asignaciones R8 sin equivalencia comprobable en lugar de mapear por número.
- La distribución por perfil/período y el encaje en EDT/T-15 no se derivan solo del valor esperado; cualquier asignación de reserva mensual/persona debe quedar como pendiente si no tiene evidencia actual.
- La reserva de gestión de 1.600 HH es independiente del cálculo p₀×HH; conservarla separada y señalar su base/validación, salvo dato documentado que la invalide.

## Alcance
- `08_plan_riesgos/contenido.tex`: sección de análisis cuantitativo y texto de plan de respuesta/reservas que conserva totales, IDs y asignaciones R8 obsoletos; quitar referencias R8 no trazables pertinentes a esta cuantificación.
- `LafroX-Subdocumento-8-Anexos.tex`: asegurar que Anexo 8.B enuncie correctamente el VE y la reserva adoptada sin atribuir formalidad oficial al CSV; preservar el detalle de 45 filas.
- No modificar T-16, PDFs, otros subdocumentos ni anexos fuera de esta cuantificación; preservar cambios locales preexistentes.

## Tareas
1. [done] Reemplazar en SD8 las cifras/IDs R8 obsoletos de contingencia y valor esperado con el cálculo actual p₀×HH y explicitar el alcance de la reserva en HH.
2. [done] Retirar la distribución antigua por perfil/período no mapeable y documentar los límites de asignación mensual y de capacidad en T-15; mantener separada la reserva de gestión.
3. [done] Alinear el texto de Anexo 8.B y la narrativa de reservas con los 45 riesgos y la decisión adoptada, sin cambiar cálculos fuente verificados.
4. [done] Verificar conteo e integridad de datos por ID, consistencia de cifras/referencias, ausencia de referencias cuantitativas R8 obsoletas y `git diff --check`; no compilar porque existe antecedente de MiKTeX ignorando la salida temporal y alterando el PDF rastreado.

## Evidencia inicial
- Scout read-only: p₀, HH condicional, VE por ID y totales actuales coinciden; total condicional 5.585,6 HH y VE 2.058,480 HH.
- CSV Tablas 4–6 y 17–18 contiene p₀, HH condicional, VE, respuestas y objetivos residuales; no tiene crosswalk ni la distribución antigua por perfil de R8.
- Las 45 filas de Anexo 8.B se cotejaron por ID contra el CSV y se recalcularon con aritmética decimal: cada VE = p₀×HH; total condicional 5.585,6 HH y VE 2.058,480 HH. `git diff --check` pasó.
- SD8 ya no presenta cifras antiguas de reserva 20.198,98 HH, base 204.527 HH, asignaciones por perfil/período y R8-xx como cálculo vigente.
- No se compiló para evitar riesgo al PDF; no se reporta Monte Carlo, percentil o probabilidad de cumplimiento, pues faltan distribuciones y modelo de actividades.
- La distribución mensual/perfil y ajuste al T-15 quedan pendientes de un crosswalk y evidencia de capacidad actuales.
