# Estado de las tablas de los anexos del subdocumento 3

Fecha de revisión: 1 de octubre de 2026.

## Alcance

Este reporte recoge el estado de las diez tablas revisadas de los anexos del subdocumento 3. Se excluyen las tablas de requerimientos funcionales y no funcionales y sus correspondencias.

La revisión considera el subdocumento 2 como referencia definitiva e inmutable, junto con las bases. Las aprobaciones se refieren a la coherencia del contenido documental, no a una certificación de cumplimiento de la solución implementada. No se modificaron las tablas durante esta revisión.

## Orden de completitud

Las tablas se presentan de mayor a menor completitud del contenido. Este orden no representa la dificultad de corregirlas ni su prioridad contractual.

| Orden | Tabla | Estado | Pendientes identificados |
|---|---|---|---|
| 1 | **3.A.7 — Exclusiones** | **Completa y aprobada** | Las nueve exclusiones son coherentes con el SD2 y las bases revisadas. Sin pendientes identificados en esta revisión. |
| 2 | **3.A.8 — Restricciones** | **Completa y aprobada** | Las doce restricciones son coherentes con las fuentes revisadas. Tiene el mismo nivel de completitud que exclusiones. |
| 3 | **3.A.14 — Glosario** | **Pendiente menor** | Precisar la definición de «RT» para distinguir los códigos de las bases transversales de los del caso, que tienen numeraciones diferentes. |
| 4 | **3.A.10 — Reglas de negocio** | **Con pendientes** | RNG-14 mantiene una excepción de ocupación pendiente de resolver. RNG-15 está alineada con el SD2, pero falta definir el tratamiento de pedidos urbanos posteriores a las 14:00, situación que el SD2 no resuelve. |
| 5 | **3.A.9 — Decisiones** | **Con observaciones** | D-04 generaliza la comprobación de los criterios en marcha blanca, aunque existen verificaciones posteriores. D-07 requiere concretar el mecanismo de reversión. |
| 6 | **3.A.12 — Participación de actores** | **Coherente, pero incompleta** | Los actores y dotaciones coinciden con el SD2. Faltan criterios verificables de cumplimiento y contingencias que aseguren la cobertura comprometida en algunas participaciones. |
| 7 | **3.A.6 — Supuestos** | **Con pendientes** | S-17 conserva el conflicto de calendario; S-27 mantiene excepciones de ocupación pendientes de resolver. Las contingencias de S-20, S-28 y S-40 no aseguran claramente el alcance ante falta de equipos, instrumentación o confirmación de instalaciones. |
| 8 | **3.A.11 — Consultas abiertas** | **Requiere ajustes** | Separar asuntos resueltos de consultas pendientes y precisar afirmaciones sin respaldo suficiente. Revisar V-03, V-04, V-05, V-07, V-08 y V-17 según el detalle siguiente. |
| 9 | **3.A.13 — Criterios de aceptación** | **Requiere ajustes** | Completar métodos de comprobación, resolver la excepción de ocupación de R18-14 y precisar el protocolo de medición anual de R18-12. |
| 10 | **3.A.15 — Declaración de IA** | **Incompleta** | Las once filas indican «Revisión humana: No documentada». Falta registrar quién revisó y qué verificó, utilizando antecedentes reales. |

## Detalle de los pendientes de consultas abiertas

- **V-03:** existe una solución adoptada en D-11; debe distinguirse de una consulta aún sin criterio definido.
- **V-04:** distinguir los documentos de origen de los códigos antes de establecer su correspondencia.
- **V-05:** la propia fila indica que no requiere respuesta; no corresponde mantenerla como consulta abierta sin aclarar su estado.
- **V-07:** explicar cómo se obtiene el lote cuando no está rotulado y tampoco existe documentación disponible. La captura manual no resuelve por sí sola la falta del dato.
- **V-08:** la falta de control de envases no demuestra necesariamente que no existan antecedentes del saldo inicial. La afirmación debe tratarse como un dato por verificar.
- **V-17:** permanece pendiente el conflicto de calendario identificado en la revisión previa.

## Detalle de los pendientes de aceptación

- **R18-03:** comprobar también el acceso del cliente a los registros térmicos.
- **R18-07:** verificar que la ruta sea corregible y que los cambios queden registrados, además del tiempo de generación.
- **R18-09:** verificar legibilidad y disponibilidad de las guías; la conciliación con acuse no demuestra ambos aspectos por sí sola.
- **R18-10:** comprobar la cuadratura y la explicación de todas las diferencias, además de realizar el cierre diario.
- **R18-12:** conservar el máximo de 7 % del parque al año fijado por el SD2. Definir el inicio del período y cómo se determina el parque utilizado como denominador.
- **R18-14:** resolver la excepción de ocupación pendiente.
- **R18-15:** comprobar que la causa se registra al producirse el faltante; contar faltantes con causa no verifica el momento del registro.

## Confirmaciones adicionales

- Las diez tablas mantienen el número de columnas esperado en sus filas.
- Las correcciones anteriores de coherencia con el SD2 se conservan.
- **S-41 está correctamente incorporado como supuesto**, con fundamento, impacto y validación mediante el inventario de TI del cliente en el mes 1. Los 184 computadores constituyen una cantidad propuesta pendiente de confirmar, no un dato informado por las bases.
- La validación pendiente de un supuesto no lo convierte automáticamente en una incoherencia: debe distinguirse de una discrepancia con el SD2 o las bases.

**Resultado de la revisión: dos tablas aprobadas y ocho con observaciones o pendientes.**
