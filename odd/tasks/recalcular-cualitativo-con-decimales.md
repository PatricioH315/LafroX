# Recalcular el análisis cualitativo con ponderaciones decimales

## Objetivo
Actualizar el análisis cualitativo de SD8 y el Formulario T-16 para presentar probabilidad e impacto con los valores decimales cualitativos y calcular la exposición como P decimal × I decimal.

## Decisión autorizada
- El usuario eligió aplicar los valores decimales y las zonas de la Tabla 3 del CSV vigente para ambos documentos.
- Exposición = probabilidad decimal × impacto decimal.
- Prioridad/zona se toma del campo Zona de Tabla 3 (Baja/Media/Alta/Crítica), no de la matriz ordinal SD8 anterior.
- Mantener separados estos ponderadores cualitativos de p₀ y del análisis cuantitativo de HH.
- El archivo externo sirve como dato de trabajo; no presentarlo como fuente documental oficial en la redacción de SD8.

## Alcance y resguardos
- `08_plan_riesgos/contenido.tex`: escalas, matriz de prioridad y tabla/discusión del análisis cualitativo; reconciliar referencias que describan la exposición como ordinal.
- `Lafrox-Subdocumento-T-16.tex`: explicación y exposición/zona en las 45 filas; preservar textos y otros campos.
- Usar la tabla actualizada de 45 riesgos como base y cotejar cada fila por ID.
- Preservar todo cambio previo no relacionado. En particular, no restaurar ni reemplazar el PDF T-16 modificado sin nueva autorización.
- No cambiar otros anexos, no compilar a la raíz ni crear commit sin autorización explícita.

## Tareas
1. [done] Actualizar SD8: modelo de valoración, explicar zonas registradas por riesgo y revisar el resumen de los diez riesgos de mayor exposición.
2. [done] Actualizar T-16 para reflejar exposición decimal y zona de los 45 riesgos sin alterar el resto de campos.
3. [done] Verificar por ID todos los valores P, I, P×I y zona; revisar consistencia narrativa, estructura de filas y `git diff --check`.
4. [skipped] No compilar: una ejecución previa de MiKTeX ignoró la salida temporal y modificó el PDF rastreado; evitar repetir el riesgo sin resolver configuración segura.

## Contexto
- La Tabla 3 del CSV contiene los valores decimales cualitativos P, I y Zona para R-001–R-045.
- T-16 ya mostraba ordinal/decimal para P e I, pero mantenía Exposición ordinal.
- SD8 tenía una tabla top-10 con valores y bandas ordinales 1–25. La versión editada usa exposición decimal y conserva las zonas por riesgo sin inventar umbrales numéricos generales.
- Verificación delegada: los 45 IDs, P, I, productos y zonas coinciden; el top-10 quedó ordenado por producto descendente e ID ascendente; filas T-16 estructuralmente válidas con ocho columnas y mitigaciones no vacías; `git diff --check` pasó.
- No se compiló ni se inspeccionó visualmente el PDF por riesgo de sobrescribir el PDF T-16 preexistente modificado.
- El Anexo 8.A conserva una tabla/etiquetado de exposición y bandas ordinales antiguos, fuera del alcance autorizado; debe revisarse si se busca armonización integral de anexos.
- Hay cambios previos locales en SD8, T-16, PDF T-16 y otras tareas; tratarlos como preexistentes y conservarlos.
