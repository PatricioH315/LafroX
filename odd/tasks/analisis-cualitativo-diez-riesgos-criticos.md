# Análisis focalizado de los diez riesgos cualitativamente más críticos

## Objetivo
Ampliar la subsección de análisis cualitativo en SD8 con una lectura focalizada de los diez riesgos de mayor exposición y una tabla que identifique los eventos/consecuencias junto con P, I, P×I y zona.

## Decisiones
- Mantener la selección y orden vigente de la Tabla 8.4: R-012, R-015, R-005, R-006, R-011, R-013, R-014, R-016, R-001 y R-003; exposición decimal descendente y, en empates, ID ascendente.
- Basarse estrictamente en las declaraciones actuales del T-16; no agregar consecuencias, causas, ubicaciones ni severidades inferidas.
- No confundir la exposición cualitativa qP×qI con p₀×HH cuantitativo.
- Incluir la tabla dentro de la sección cualitativa existente, con breves descripciones legibles y una interpretación de grupos de exposición/temas comunes.
- Mantener zonas registradas, no inventar umbrales universales.

## Alcance y resguardos
- Archivo de implementación: `08_plan_riesgos/contenido.tex`, subsección `Análisis cualitativo de riesgos` y Tabla 8.4.
- Preservar el resto de cambios locales previos en el archivo y el contenido de los otros documentos.
- Sin modificaciones a T-16 ni anexos, sin PDF de salida de proyecto, sin commit.

## Tareas
1. [done] Ampliar la Tabla 8.4 para identificar resumidamente cada uno de los diez riesgos, manteniendo P/I, producto y zona vigentes.
2. [done] Añadir una síntesis cualitativa que interprete los riesgos más expuestos y sus temas compartidos sin presentar respuestas propuestas como controles ya eficaces.
3. [done] Verificar datos/orden/cobertura, legibilidad estructural, `git diff --check` y preservar el resto de la subsección.

## Evidencia
- T-16, líneas 28, 30, 32–33, 38–43: eventos, consecuencias, ponderaciones y respuestas de los diez IDs.
- La Tabla 8.4 ahora contiene exactamente los diez IDs vigentes en orden, descripciones resumidas de evento/consecuencia, P/I decimales, producto y zona registrada; la síntesis interpreta los riesgos Críticos y Altos, sin describir mitigaciones como eficaces.
- Verificación independiente cotejó valores y zonas con T-16; el diff localizó solo esta subsección y `git diff --check` pasó. El cambio es documental, no aplica test funcional RED.
- No se compiló ni se generó PDF; la validación visual queda pendiente.
