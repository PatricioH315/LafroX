# Cotejo individual de cadena y componentes

Este registro documenta comprobaciones concretas de SD3-04 y SD3-06. Una diferencia en el criterio resumido no demuestra que la prueba falle: indica qué debe verificarse en sus pasos y evidencia. El cotejo sigue abierto mientras no se haya revisado la totalidad de las filas y sus fuentes.

## Recepción: primer contraste de T-12, Anexo 3.A y T-13

Fuentes: T-12 y catálogo 3.A locales; T-13 del SD9 `0c57a4bb`; diccionario T-14 del SD7 `68669bef`. Las pruebas identificadas son previstas, no ejecutadas.

| ID | Componente y paquete | Hallazgo en el criterio resumido de T-13 | Estado de la cadena |
|---|---|---|---|
| RF-01.01 | M1 compara SKU y cantidades con la orden, alerta por discrepancia y permite cerrar; 3.4.1 identifica Recepción. | El criterio menciona el comparativo y la disponibilidad para Calidad, pero no explicita la alerta por cada discrepancia ni que no se bloquee el cierre. El catálogo local sí los incluye. | Pendiente cotejar los pasos de /P01 a /P03 y conciliar el criterio con T-13. |
| RF-01.02 | M1 captura AI 10 o ingreso manual y bloquea el lote vacío; 3.4.1 identifica Recepción con lote. | El criterio exige lote y bloqueo, pero no menciona las dos vías de captura exigidas. El catálogo local las incluye. | Pendiente cotejar los pasos de /P01 a /P05 y conciliar el criterio con T-13. |
| RF-01.03 | M1 vincula vencimiento, lote y ubicación, y captura la fecha en el formato requerido; 3.4.1 identifica Recepción con vencimiento. | El criterio menciona fecha, lote y bloqueo, pero no explicita el formato DD/MM/AAAA ni la asociación a ubicación para FEFO. El catálogo local los incluye. | Pendiente cotejar los pasos de /P01 a /P05 y conciliar el criterio con T-13. |
| RF-01.04 | M1 registra tipo, SKU, lote, cantidad y fotografía; 3.4.1 identifica Recepción. | El criterio exige los campos requeridos y fotografía descargable; no enumera los campos, por lo que debe contrastarse el detalle de los casos con la exigencia. | Pendiente verificar el alcance del paquete para no conformidades y los pasos de /P01 a /P03. |
| RF-01.05 | M1 registra y alerta; M2 pone la cantidad afectada en cuarentena; 3.4.1 y 3.4.2 identifican Recepción e Inventario. | El criterio registra el bloqueo y la notificación, pero no explicita la transición automática al estado de cuarentena para el SKU/lote afectado. | Pendiente cotejar los pasos de /P01 a /P05 y conciliar el paquete 3.4.2 y el criterio con T-13. |
| RF-01.06 | M1 interpreta AI 01, 10, 17 y 00, autocompleta y habilita ingreso manual; 3.4.1 identifica Recepción. | El criterio menciona autocompletado e ingreso manual para código no encontrado, pero no enumera los cuatro AI ni cubre expresamente el código inválido. El catálogo local los incluye. | Pendiente cotejar los pasos de /P01 a /P03 y conciliar el criterio con T-13. |

La identificación de M1 o M2 y la existencia de un paquete no demuestran por sí mismas el alcance de construcción de todas las funciones. Los orígenes individuales también requieren cotejo; en particular, la reserva de RF-01.01 consta en `COTEJO_ORIGENES_3A1.md`.

### RF-01.01: respuesta aceptada

Se confirmó que el criterio del Anexo 3.A, Tabla 3.A.1, ya incorpora la formulación acordada: «Por cada SKU se compara la cantidad recibida con la OC; cada discrepancia genera una alerta sin bloquear el cierre. El comparativo queda registrado y disponible en el módulo de calidad». El usuario aceptó esta respuesta. La conciliación del resumen de T-13 y el cotejo de los pasos de RF-01.01/P01 a P03 continúan pendientes; esta confirmación no declara ejecutada ni aprobada una prueba.

### RF-01.02: respuesta aceptada

Se confirmó que el criterio del Anexo 3.A, Tabla 3.A.1, ya incorpora la formulación acordada: «El 100 % de los ítems con trazabilidad obligatoria registran lote; campo vacío muestra “Lote requerido para este producto” e impide continuar. Se aceptan tanto la lectura del AI 10 como el ingreso manual del lote». El usuario aceptó esta respuesta. La conciliación del resumen de T-13 y el cotejo de los pasos de RF-01.02/P01 a P05 continúan pendientes; esta confirmación no declara ejecutada ni aprobada una prueba.

### RF-01.03: respuesta aceptada

El usuario aceptó el criterio del Anexo 3.A, Tabla 3.A.1: el 100 % de los productos con control de vencimiento habilitado tiene la fecha registrada en formato DD/MM/AAAA y asociada al lote y la ubicación para FEFO; un campo vacío bloquea el avance. La conciliación del resumen de T-13 y el cotejo de los pasos de RF-01.03/P01 a P05 continúan pendientes; esta confirmación no declara ejecutada ni aprobada una prueba.

### RF-01.04: respuesta aceptada

Se amplió el criterio del Anexo 3.A, Tabla 3.A.1, para enumerar el tipo de la lista, SKU, lote, cantidad y al menos una fotografía capturada desde el dispositivo, además de su descarga desde Calidad. La conciliación de T-13 y el cotejo de los pasos RF-01.04/P01 a P03 permanecen pendientes. No se declara ejecutada ni aprobada una prueba.

### RF-01.05: respuesta aceptada

Se precisó el criterio del Anexo 3.A, Tabla 3.A.1: al confirmar la no conformidad, la cantidad afectada del SKU y lote correspondiente pasa automáticamente a estado «Cuarentena» y queda bloqueada para picking; el perfil de Calidad recibe una alerta en la aplicación dentro de cinco minutos. La conciliación de T-13 y el cotejo de los pasos RF-01.05/P01 a P05 permanecen pendientes. No se declara ejecutada ni aprobada una prueba.

### RF-01.06: respuesta aceptada

El usuario aceptó el criterio ya incluido en el Anexo 3.A, Tabla 3.A.1: los AI 01, 10, 17 y 00 de códigos GS1 válidos autocompletan GTIN, lote, vencimiento y SSCC; ante código inválido o no registrado se habilita el ingreso manual y, para producto no encontrado, se muestra «Producto no encontrado». La conciliación de T-13 y el cotejo de los pasos RF-01.06/P01 a P03 permanecen pendientes; no se declara una prueba ejecutada o aprobada.

### RF-01.07: respuesta aceptada

Se precisó el criterio del Anexo 3.A, Tabla 3.A.1, para que la generación del SSCC sea automática al cerrar el pallet y se ordene imprimir la etiqueta GS1-128 en la impresora térmica del andén. Se conservan las asociaciones a GTIN, lote, vencimiento y recepción, y la distinción del AI 11. La conciliación de T-13 y el cotejo de RF-01.07/P01 y P02 permanecen pendientes; no se declara una prueba ejecutada o aprobada.

### RF-01.08: respuesta aceptada

El usuario aceptó el criterio ya incluido en el Anexo 3.A, Tabla 3.A.1: la asociación SSCC–ubicación queda registrada; se escanean ambas etiquetas y se comprueba la compatibilidad térmica antes de confirmar; una ubicación incompatible se bloquea con mensaje descriptivo. La conciliación de T-13 y el cotejo de RF-01.08/P01 y P02 permanecen pendientes; no se declara una prueba ejecutada o aprobada.
