# Cierre de correcciones locales del Subdocumento 7

Fecha: 5 de noviembre de 2026. Rama de trabajo: `LafroX-Subdoc7-LateX-CORRIGIENDO`.

Se aplicó el alcance local autorizado: cuerpo del S7, anexos y formularios T-14, T-15 y T-18, con sus figuras, fuentes y salidas. No se modificaron otras ramas. La mayor extensión responde a la prioridad de legibilidad acordada. Esta entrega no constituye el cierre de todas las observaciones del evaluador.

## Tareas y trazabilidad

Las páginas de revisión corresponden al PDF evaluador de 55 páginas. La columna «matriz» remite a la numeración de `revision/MATRIZ_TRAZABILIDAD_DEPENDENCIAS_SD7_2026-11-05.md`. Los métodos de implementación son decisiones propias; no se atribuyen al evaluador.

| Tarea local | Cambio realizado y evidencia | Relación con la revisión | Matriz | Estado y límite |
|---|---|---|---|---|
| T1. Mejorar legibilidad de figuras | Gantt vectoriales repartidos en láminas, nombres completos, fechas separadas y relaciones por ID. EDT detalladas y vista completa recompuestas sin cambiar su jerarquía. Tipografía mínima de las láminas recompuestas: 9,5 pt. Ejemplos: S7 pp. 23 y 64; T-14 desde p. 117. | Sí: legibilidad y claridad de Gantt/agrupaciones, pp. 29-30 y 32. La extensión a EDT ilegibles es una mejora propia de presentación. | 13; parte gráfica de 15 | Completada como presentación. No corrige la estructura por fases ni valida la lógica CPM. |
| T2. Corregir Figura 7.20 | Se eliminó del PDF y de su fuente editable la llamada inexistente al detalle de aceptación H12; se mantuvieron los 33 enlaces y los hitos. S7 p. 43. | Sí: anotación sin destino, p. 32. | 13 | Completada. No añade dependencias ni resuelve la aceptación de H12. |
| T3. Aclarar siglas y leyendas | Definiciones de SD, EDT, PT, HH, E1/E2, RC, PT/H, H1-H12, F1-F8, QA, SRE, NOC, SOC y DTE en los cinco cuerpos; leyendas en los gráficos. | Sí: siglas y comprensión, p. 32. | 15a | Completada dentro del ámbito local. |
| T4. Distinguir elaboración y aprobación | T-14, tabla 4, p. 48: 1.2.1 se elabora preliminarmente en mes 1 y se aprueba en H1/mes 2; 1.2.5 se elabora en mes 13 y se aprueba en H8/mes 14. | Sí para H1: inconsistencia editorial, p. 27. La aclaración equivalente de H8 es añadida del análisis propio. | 15a | Completada como aclaración; no se desplazaron hitos ni barras. |
| T5. Explicar los niveles de reversión | S7, tabla 7.8 y prosa, p. 105: objetivo técnico de hasta 10 minutos; preparación operacional de hasta 30 minutos en paralelo y verificación adicional de 10: máx(10,30)+10=40. Se conservan los límites 04:45, 05:25 y 05:30 y la remisión a T-18, sección 6.4. | Relación parcial con la preocupación por reversión operable, pp. 31 y 33. La distinción explícita 10/40 es aclaración propia. | 15a; contexto del 9 | Completada como explicación. Los plazos son objetivos a medir en Preproducción, no resultados de un ensayo ejecutado. |
| T6. Aligerar tablas | Se acortaron celdas de cobertura modular y de reversión, trasladando detalles a prosa inmediata. Se conservaron módulos, responsabilidades, disparadores y ventanas. S7 tabla 7.2 y tabla 7.8. | Sí: celdas extensas y presentación, pp. 31-32. | 14 | Completada en las tablas seleccionadas. |
| T7. Depurar repeticiones y redacción | Se condensó el cierre de S7, sección 7.3.8; el detalle técnico se remite a T-18, sección 6.5, p. 24, donde ya está disponible. Se corrigieron rótulos y expresiones de continuidad entre figuras. | Sí: duplicación y material técnico en planificación, pp. 31-33. | 14 | Parcial respecto de la observación amplia: no se trasladó contenido a otros subdocumentos ni se retiraron compromisos sin un destino existente. |
| T8. Verificar referencias internas | Sin referencias pendientes, etiquetas duplicadas ni marcadores «??» en los cinco PDF; se conservan números de figuras y etiquetas. Figura 7.20 sigue siendo 7.20 y los siete tramos Gantt siguen siendo 7.25-7.31. | Apoya la consistencia editorial, pp. 27 y 31-32; el control automatizado es adicional. | 15a-15b | Completada para referencias LaTeX internas. No certifica la vigencia de todas las referencias externas. |
| T9. Regenerar y verificar entregables | Se recompilaron los cinco PDF, se sincronizó `main.pdf` y se regeneraron los cinco Markdown desde los PDF finales. Se registraron hashes, invariantes, diagnósticos y revisión visual. | Control adicional de entrega, relacionado con la recomendación general de revisión final de p. 3. | 15b-15c | Completada. No se asignaron folios globales ni una nueva fecha/versión corporativa. |

## Validación y conservación de la base

Se conservaron por SHA-256 las cuatro tablas numéricas de T-15 y los tres archivos `.gan`. Se comprobaron 227 paquetes, 168 con programación fechada y 59 de esfuerzo continuo, 220.023 HH totales y un máximo de 64 personas. La comprobación de pertenencia cubre las 17 figuras detalladas de EDT y los 227 paquetes de la vista completa. La programación gráfica mantiene las 155 filas y 262 relaciones de la fuente correspondiente, sin recalcular fechas ni ruta crítica.

Los registros finales no contienen errores fatales, referencias sin resolver, glifos ausentes ni cajas desbordadas. Persisten avisos heredados de composición «Infinite glue shrinkage»: 4 en S7, 15 en anexos, 33 en T-14, 2 en T-15 y 3 en T-18. No se alteró la clase corporativa para suprimirlos. La inspección visual del asistente cubrió las 434 páginas mediante 39 hojas de contacto, con ampliaciones de EDT, Gantt, Figura 7.20, diccionario y reversión; no equivale a una aprobación humana del contenido técnico.

| Entregable | Páginas anteriores | Páginas finales |
|---|---:|---:|
| S7 | 66 | 117 |
| Anexos S7 | 25 | 26 |
| T-14 | 102 | 166 |
| T-15 | 99 | 100 |
| T-18 | 24 | 25 |
| Total | 316 | 434 |

`main.pdf` tiene las mismas 117 páginas y el mismo texto extraído que el PDF del S7. Los Markdown son extracciones de consulta: las figuras y su composición se revisan en los PDF.

## Pendientes que requieren coordinación

Permanecen pendientes la EDT por productos y su equivalencia de códigos; estimación por tamaño y escenarios PERT; cierre de dependencias y cálculo CPM; iteraciones y pruebas en el calendario; disponibilidad y nivelación de recursos; el déficit CAL de 217,60 HH; plazos de revisión/aceptación; tratamiento de defectos durante congelamientos; coordinación con cadenas y proveedor de lácteos; y conciliación de riesgos y reservas. No se presenta la mejora gráfica como solución de esos problemas.

Se preservaron las advertencias existentes sobre insuficiencias, los datos contractuales y las fechas comunes de la portada. La foliación integrada de la oferta y la ficha común de versión quedan para la consolidación transversal. No se editaron la declaración humana de IA, la plantilla ni los metadatos comunes.

## Evidencia y reproducción

`BASE_INICIAL.json` conserva la línea base; `GANTT_VECTOR.json` y `EDT_VECTOR.json` describen las fuentes y coberturas; `VERIFICACION.json` registra hashes finales, páginas, diagnósticos y evidencia visual. Las copias originales y los renders de comprobación están en `tmp/pdfs/local-20261105/` y no sustituyen los entregables finales de la raíz.

Los scripts `arreglos_locales_sd7.py`, `gantt_local_vector.py`, `edt_local_vector.py`, `compilar_local_sd7.ps1`, `validar_local_sd7.py` y `refresh_sd7_markdown.py` incluyen protección de rama. La compilación se valida antes de copiar los PDF a la raíz. La regeneración de Markdown se ejecuta después de esa copia. No se sobrescribieron registros históricos K4/K6 ni se realizó commit o push.

La interpretación de los tipos de relación de GanttProject se contrastó con su [enumeración oficial ConstraintType](https://raw.githubusercontent.com/bardsoftware/ganttproject/master/biz.ganttproject/core/src/main/java/biz/ganttproject/core/model/task/ConstraintType.java).
