# Plan de acción para la RBS de 33 riesgos
Documento de trabajo para rehacer el punto 8.3 del Subdocumento 8 y sincronizar sus anexos con los 33 riesgos y resultados vigentes de 8.2.
La propuesta distinguirá controles existentes, respuestas propuestas y condiciones que siguen pendientes de decisión o evidencia.

## Specs
S1 — “ahora realiza todo el 8.3 con todos los insumos que tengas mas los resultados de los puntos anteriores”
S2 — “la tabla que creaste (tabla 8.6) muevelo al latex de los anexos, en caso de que lo necesites, elimina los anexos o directamente hazlo desde 0, reemplazando el contenido de los anexos”

## Tasks
- T1 | S1 | Route: inline — rehacer respuestas para R-001--R-033, reservas HH/calendario y condiciones de aceptación del punto 8.3, sin presentar propuestas como controles aprobados. | Commit: 439c8f7
- T2 | S1 | Route: inline — cotejar cobertura de IDs, cifras, fuentes oficiales, límites de evidencia, resolver referencias de versión en la introducción, revisar salida visual y compilación; registrar el commit de cierre. | Commit: 439c8f7
- T3 | S2 | Route: inline — mover la matriz de respuestas desde el cuerpo a Anexo 8.A como Tabla 8.A.1; retirar la copia en el cuerpo y renumerar la tabla de reservas a 8.6. | Commit: pending
- T4 | S2 | Route: inline — reemplazar Anexo 8.B obsoleto por detalle HH de R-001--R-033 con O/M/P, PERT y VE; reconciliar el inventario y excluir valores monetarios. | Commit: pending
- T5 | S2 | Route: inline — actualizar referencias/cabeceras entre el cuerpo y los anexos, verificar IDs/cifras y compilar ambos LaTeX. | Commit: pending

## Log
L1 — ahora realiza todo el 8.3 con todos los insumos que tengas mas los resultados de los puntos anteriores
L2 — Reescritura de 8.3 aplicada: matriz de respuesta propuesta para los 33 riesgos, cifras de exposición de 8.2 y reservas/aceptación actualizadas; la compilación de main.tex pasó y la matriz contiene 33 IDs únicos. T1 está implementado; T2 continúa con revisión visual/documental y cierre.
L3 — La primera revisión del PDF mostró que la introducción y las referencias a los Anexos 8.A–8.B aún describían la versión de 45 riesgos; se actualizaron para dejarla como versión anterior sin crosswalk y evitar usarla como base para los 33 riesgos actuales. También se sustituyó en escalas la remisión a 8.B por el análisis cuantitativo de 8.2.3. La compilación final pasó y las tablas de respuesta y reservas se inspeccionaron visualmente.
L4 — Cierre verificado: 33 IDs únicos en la matriz, cifras actuales y versión histórica distinguidas, sin mención del CSV en 8.3; `latexmk -lualatex -halt-on-error main.tex` y `git diff --check` pasaron. Código y documento de riesgos quedan en el commit 439c8f7.
L5 — la tabla que creaste (tabla 8.6) muevelo al latex de los anexos, en caso de que lo necesites, elimina los anexos o directamente hazlo desde 0, reemplazando el contenido de los anexos
L6 — Inspección de alcance: `LafroX-Subdocumento-8-Anexos.tex` contiene fichas de una versión anterior de 45 riesgos y un Anexo 8.B con 45 registros/2.058,480 HH; la matriz actual de 33 está en el cuerpo como Tabla 8.6 y debe trasladarse al anexo. Mantener fuera la edición de cifras monetarias.
L7 — Reconciliación cuantitativa: el archivo auxiliar anuncia 34 riesgos en su encabezado, pero contiene 33 filas, exactamente R-001--R-033. Se recalcularon O/M/P acumulados por episodios, PERT y VE; la suma VE es 825,34 HH y reproduce los valores de la Tabla 8.5 de 8.2. No hay fila adicional que excluir.
L8 — La matriz propuesta se movió desde el cuerpo a Anexo 8.A como Tabla 8.A.1; se eliminó la copia del cuerpo y la tabla de reservas se renumeró a 8.6. La inspección visual confirma la continuación de la matriz y los 33 riesgos.
L9 — Anexo 8.B reconstruido con R-001--R-033: O/M/P acumulados por episodios, PERT = (O+4M+P)/6 y VE = p0×PERT; la suma es 825,34 HH y el top 10 coincide con 8.2.3. Se eliminaron cifras, tablas y referencias heredadas de la antigua versión de 45 riesgos.
L10 — Referencias del cuerpo y anexos sincronizadas; Tabla 8.B.1 compilada y ajustada a dos páginas en orientación horizontal. Las compilaciones de `LafroX-Subdocumento-8-Anexos.tex` y `main.tex`, el cotejo de 33 IDs/top 10/825,34 HH y `git diff --check` pasaron. La evaluación nativa ASSESS quedó `unassessable` porque detectó archivos sin seguimiento que requieren declaración explícita; el plan de ASSESS indica autoverificación del escritor y no añade verificador independiente al no haberse escalado un riesgo de Task Size alto.
