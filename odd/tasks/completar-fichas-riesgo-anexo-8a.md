# Completar las fichas de riesgo del Anexo 8.A

## Objetivo
Reemplazar la tabla de puntuaciones actual del Anexo 8.A por fichas útiles para los 45 riesgos vigentes, con información de respuesta y brechas identificadas, y corregir el texto del cuerpo SD8 que actualmente atribuye al anexo campos que no contiene.

## Decisiones
- El usuario autorizó actualizar Anexo 8.A y el contenido del SD8 si hace falta.
- El usuario decidió marcar como pendientes por responsable los campos que no estén respaldados por el registro, no inventar contingencias, riesgos secundarios ni plazos.
- Para los campos respaldados: conservar causa–evento–consecuencia, categoría/owner, ponderaciones cualitativas P e I actuales (ordinal/decimal) y zona; añadir estrategia, responsable, disparador, plazo/hito respaldado, acción de mitigación y criterio de evidencia del registro vigente.
- La meta residual se presenta como objetivo hipotético condicionado, no residual validado ni reducción de reserva disponible.
- Contingencia y riesgo secundario se etiquetan “Pendiente de definición por responsable” si no hay dato documentado; plazo/fecha se marca así cuando no hay hito de respuesta con evidencia.
- CSV es insumo de trabajo, no fuente oficial para citar en SD8. Mantener p₀×HH cuantitativo separado de valoración cualitativa.
- No afirmar que controles/mitigaciones son eficaces antes de la evidencia de validación.

## Alcance y resguardos
- `LafroX-Subdocumento-8-Anexos.tex`: rehacer Anexo 8.A para los 45 IDs actuales, organizado por familias RBS o forma equivalente legible.
- `08_plan_riesgos/contenido.tex`: ajustar únicamente la referencia que promete que Anexo 8.A ya define todos los campos; reflejar los soportados y los pendientes.
- Preservar Anexo 8.B y el resto de cambios locales. No modificar T-16, CSV, otros anexos/subdocumentos ni PDFs. No crear commit.

## Tareas
1. [done] Construir la estructura editorial de las fichas del Anexo 8.A con campos y estados inequívocos: 45 fichas compactas por ID, con valoración, respuesta respaldada y campos pendientes señalados.
2. [done] Incorporar los datos respaldados de los 45 riesgos, agrupados por RBS, y marcar brechas por responsable sin inventar.
3. [done] Corregir la promesa del cuerpo SD8 para que refleje el contenido real del Anexo 8.A.
4. [done] Verificar cobertura R-001…R-045, campos, P/I/zona, owner/estrategia/disparador/validación/residual condicionado, referencias y `git diff --check`; compilar en copia temporal y revisar render si es seguro.

## Evidencia inicial
- Scout read-only: Anexo 8.A actual (`LafroX-Subdocumento-8-Anexos.tex:21–71`) solo presenta una tabla de puntuaciones y no fichas de respuesta.
- Tablas de trabajo vigentes: CSV Tabla 3 (enunciado/P/I/zona), Tabla 9 (estrategia, acción, dueño, disparador, validación/etapa), Tabla 8 (mes estimado), objetivo residual y Tabla 17 (costos/retornos). Se usarán como entradas reproducidas, no como citas oficiales.
- Las fichas de R-001…R-045 se reconstruyeron agrupadas por las familias RBS y se cotejaron con T-16: 45 IDs únicos; P/I/exposición/zona, enunciados, estrategia, dueño, disparador, acción y validación consistentes. Cada ficha incorpora los campos; plazo/hito, contingencia y riesgo secundario quedan pendientes por responsable (135 estados pendientes). Residual objetivo indicado como condicionado/no validado; costos pendientes.
- `08_plan_riesgos/contenido.tex` ahora describe fielmente los campos disponibles y pendientes, sin afirmar eficacia.
- `git diff --check` pasó. Compilación LuaLaTeX del documento de anexos en copia temporal terminó con éxito (28 páginas); visual inspeccionada en páginas 5, 14, 22–23 y 28, sin clipping. PDF original no tocado. Anexo 8.B quedó idéntico a HEAD.
- Los objetivos residuales están condicionados; la reserva actual sigue siendo 2.058,480 HH hasta validar eficacia.
- Cambios locales previos existen en `08_plan_riesgos/contenido.tex`; conservarlos.
