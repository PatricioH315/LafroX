# CONTEXTO DE SESIÓN

Este archivo define el protocolo de identidad y de control de sesión para el trabajo en este proyecto.

## Identidad del asistente en las respuestas

- Al iniciar **cada respuesta final** (todo mensaje de texto que el asistente entrega al usuario), el asistente debe comenzar con el encabezado:

  ```
  ## lafrox
  ```

  siempre al inicio, sin excepción.
- Este nombre (encabezado `## lafrox`) permite al usuario identificar de forma clara dónde termina una respuesta y dónde comienza una nueva sesión o mensaje del sistema, evitando ambigüedad entre bloques de contenido.

## Usuario

- El usuario se dirige a este proyecto como **lafrox**.
- En cualquier documento que requiera una firma, un nombre de usuario, una etiqueta de autoría o una identificación de la sesión, debe usarse `lafrox`.

## Regla de sesión

- El encabezado `## lafrox` debe estar presente al inicio de TODO mensaje de texto final del asistente, ya sea que responda una pregunta, inicie una tarea, reporte un avance o entregue un resultado.
- Los mensajes de herramientas (bash, edición de archivos, etc.) no llevan el encabezado; solo los mensajes de texto visibles para el usuario.
