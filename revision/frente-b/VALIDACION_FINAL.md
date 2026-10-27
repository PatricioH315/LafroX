# Validación final del frente B

Base: `93a5e884`. Rama: `LafroX-Subdoc7-LateX`. Sin commit ni publicación.

## Compilación y PDF

| Documento | Páginas | Errores fatales | Referencias sin resolver | Desbordes | Avisos glue de la clase |
|---|---:|---:|---:|---:|---:|
| LAFROX-Subdocumento7 | 66 | 0 | 0 | 0 | 4 |
| LAFROX-Subdocumento7-Anexos | 25 | 0 | 0 | 0 | 14 |
| LAFROX-Formulario-T-14 | 102 | 0 | 0 | 0 | 34 |
| LAFROX-Formulario-T-15 | 99 | 0 | 0 | 0 | 2 |
| LAFROX-Formulario-T-18 | 24 | 0 | 0 | 0 | 3 |

**316 páginas finales tras retirar la fila adicional de IA por solicitud del usuario.** LuaLaTeX finalizó correctamente. Para SD7 se conserva la salida ya compilada de `main.tex`, que incluye su entrada original con los metadatos comunes; `main.pdf` y el PDF entregable son idénticos. Los cinco Markdown se regeneraron desde los PDF; no conservan citas bibliográficas propias `LafroX 2026x`. Los hashes finales coinciden con `K6_QA_PDF.json`.

Los avisos `Infinite glue shrinkage found in box being split` corresponden al comportamiento heredado de la clase compartida con tablas multipágina; se registran sin modificar la clase. No hubo errores fatales, referencias/citas indefinidas, glifos ausentes ni solicitudes de nueva pasada. Se eliminó el aviso hypcap de T15 y el desborde del Anexo 7.A.

## Inspección visual

Se renderizaron todas las páginas y se inspeccionaron todas las hojas de contacto. Se repitió la revisión de las partes afectadas tras ajustar anchos de 49 tablas del diccionario T14, dotación T15, orientación de la declaración IA e inicio de la tabla de reversión. Se revisaron ampliadas la secuencia de actas (T15 p.58), resumen con peak (T15 p.30), aceptación (T14 p.60), reversión (SD7 p.54), nueva declaración IA (SD7 p.67) y programa DR (T18 p.19). No se detectaron recortes, superposiciones ni caracteres perdidos en estas inspecciones. Las tablas extensas repiten encabezados y conservan sus continuaciones. La inspección es del asistente; no se atribuye a un revisor humano.

Las 17 láminas EDT de detalle cubren los 227 paquetes. Los nodos adicionales 3.10.1–3.10.4 son agrupaciones, no paquetes nuevos. Cada lámina tiene llamada previa. Se reexportaron tres fuentes draw.io afectadas y la Gantt resumida con sus siete tramos. La comparación XML demuestra que las 155 tareas de la Gantt conservan atributos y dependencias; cambian nombres de actas y menciones en notas.

## Verificación numérica

`verificar_frente_b.py` comprueba 227 paquetes T14/T15, 168 con fechas y 59 continuos; 207.487 + 128 + 9.336 + 3.072 = 220.023 HH; sumas mensuales por etapa y personas por rol; peak 64 en mes 16; capacidad individual HH/ventana; coincidencia de los 168 paquetes CPM con fechas publicadas; hashes de las cuatro fuentes numéricas idénticos a K4. Las probabilidades PERT siguen siendo condicionales y no certifican aceptación ni recursos.

La prueba por intervalos detecta brecha CAL de 217,60 HH en 25-10–11-11-2027 y mínimo de 13 personas bajo los máximos publicados; las diez declaradas no bastan. Los cierres requieren acordar revisión: sólo dos días previos a producción en el escenario de entrega completa, frente a diez disponibles para CLIENTE. Ambos asuntos se registran conservando fechas.

## Estado de cierre

Implementación y validación local terminadas. K6 permanece condicionado a resolver actas y capacidad nominal/refuerzos, recibir K1/K3/K5 y conciliar reservas. No se inventan pruebas ejecutadas, contrataciones, revisores ni acuerdos del CLIENTE.

El control de permisos rechazó la última solicitud de recompilación para añadir una nota al pie. Se revirtió únicamente esa nota, conservando la fuente y el PDF T15 ya compilados y revisados. El alcance del peak está explicado en el texto anterior a la tabla. Para SD7 se reutilizó la salida previamente compilada de su envoltorio `main.tex`, sin ejecutar una nueva compilación.

Actualización posterior: fila adicional de IA retirada por instrucción del usuario; SD7 y main.tex recompilados correctamente, Markdown sincronizado, cierre de tabla inspeccionado en la página 66 y hash de SD7 actualizado. Las verificaciones históricas de la fila adicional corresponden al estado previo a su eliminación.
