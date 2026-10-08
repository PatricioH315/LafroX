# Correcciones del subdocumento 3 frente al subdocumento 2

Fecha: 1 de octubre de 2026.

Se utilizó el subdocumento 2 vigente como referencia definitiva. No se modificó ningún archivo de su carpeta. Se conservaron las tablas de requerimientos funcionales y no funcionales, sus correspondencias y el Formulario T-12, excluidos del alcance de esta revisión.

## Cambios aplicados

| Materia | Referencia del SD2 | Corrección del SD3 |
|---|---|---|
| Local cerrado | Anexo 2.2, S-03 | S-03, RNG-05 y cuerpo: retorno trazable al centro de distribución cuando el cliente continúa ausente. |
| Efectivo | Anexo 2.2, S-06 | S-06 y cuerpo: alternativas voluntarias, conservación del pago en efectivo y diferencias con causal y responsable antes del cierre. |
| Validación de conciliación | Anexo 2.2, S-06 | Participación de Finanzas: conciliación en el mes 1; costo de servir antes del mes 13. |
| Clientes no rentables | Anexo 2.2, S-07 | S-07 y cuerpo: revisión de frecuencia y pedido mínimo, sin eliminación automática. |
| Maestro de productos | Anexo 2.2, S-11 | S-11 y RNG-11: historial de cambios de códigos, equivalencias y excepciones sin segunda verdad de producto. |
| Devoluciones | Anexo 2.2, S-12 | S-12, RNG-06 y cuerpo: transmisión del evento y evidencia; el ERP emite nota de crédito cuando corresponde. |
| Telemetría y sindicato | Anexo 2.2, S-13; Anexo 2.3 | S-13, participación del sindicato y cuerpo: acuerdo previo para GPS de jornada; telemetría operacional con controles de privacidad aun sin ese acuerdo. |
| Prueba de entrega | Anexo 2.2, S-15 | S-15: conservación de fecha, ubicación e identidad disponible y articulación con el acuse tributario. |
| Promesa de entrega | Arbitraje 1 | S-21, RNG-15 y cuerpo: 24 horas urbanas para pedidos antes de las 14:00 y 48 horas rurales, periféricas o de cross-docking; se retira la conversión a horas hábiles y el comienzo automático al día siguiente. |
| Referencia de instalaciones | Anexo 2.2, E-06 | S-22 remite al lugar donde el SD2 reconoce la discrepancia entre cinco y seis instalaciones. |
| Personas y equipos de reparto | Resumen ejecutivo y Anexo 2.3 | S-23 conserva 84 personas propias y aproximadamente 160 conductores externos; distingue la población de unas 244 personas de los equipos compartidos por camión de S-30. Se conserva la flota de 42 + 54 = 96 camiones. |
| Control de retornables | Anexo 2.2, S-10 | RNG-07 conserva cantidades, control por cliente y transportista, movimientos de cuenta corriente y alertas por excesos y pérdidas. |
| Pérdida anual de envases | Tabla 2.1 | S-26, R18-12, anexos y cuerpo conservan máximo 7 % del parque al año, frente al 14 % estimado. Se elimina el denominador de despachos y la recalculación automática de la meta. |
| OTIF | Anexo 2.2, S-01 | RNG-09 exige 100 % de ítems y unidades; conserva fecha y ventana; fill rate y perfect order se miden por separado. |
| Diferencias de inventario | Tabla 2.1 | S-29 y cuerpo: el 2,3 % queda como línea base; diferencias investigadas y ajustes justificados, sin tolerancia automática de migración. |
| Merma por vencimiento | Tabla 2.1 | Anexo 3.J incorpora el compromiso del SD2: máximo 1,0 % del valor del inventario al año, tras 12 meses de operación, sin aumentar quiebres de stock. |

## Cuestiones que el SD2 no permite cerrar por sí solo

1. **Pedidos urbanos posteriores a las 14:00.** El SD2 no fija la promesa ni el momento desde el que se cuenta para estos pedidos. Se retiró la regla adicional del SD3 que alteraba el plazo; falta definir esta situación comercial.
2. **Medición anual de envases y merma.** Se conservan las metas y denominadores del SD2. Este no precisa la fecha de inicio de los 12 meses ni si el parque y el valor del inventario se toman al inicio, al cierre o como promedio. Hace falta un protocolo de medición que no altere los compromisos.
3. **Equipamiento individual alternativo.** El SD2 fija personas y flota, pero no cuántos conductores propios hay dentro de las 84 personas ni quién necesita cada periférico. S-30 mantiene la asignación propuesta por camión; una alternativa por persona requiere inventario y simultaneidad de uso, sin equiparar 244 personas a 244 conductores.
4. **Conflictos anteriores sin una solución determinada por el SD2.** Permanecen pendientes el mecanismo concreto de reversión, la excepción de ocupación y las demás decisiones frente a las bases señaladas en la revisión anterior. Esta corrección no constituye su aprobación.
5. **Tablas excluidas y Formulario T-12.** No se certifica su alineación con los textos corregidos. Su revisión posterior deberá conservar los datos del SD2 bajo el mismo criterio de prevalencia indicado por el usuario.

## Verificación

- Comparación SHA-256 de todos los archivos de la carpeta del SD2 antes y después: sin cambios.
- Comparación SHA-256 de las fuentes del SD3: cambiaron únicamente contenido.tex, anexos.tex y las tablas de supuestos, reglas de negocio, participación de actores y criterios de aceptación.
- Se conservan los identificadores S-01 a S-41, RNG-01 a RNG-16 y R18-01 a R18-16, sin duplicados ni saltos; se verificó la estructura de columnas de los registros editados.
- Compilación de cuerpo y anexos con LuaLaTeX en dos pasadas: 26 y 144 páginas respectivamente. Persisten avisos de la clase de tablas y un desbordamiento menor en la correspondencia de familias excluida de la edición.
- Se revisaron visualmente las páginas de registros modificados y del cuerpo afectado, sin solapamientos ni recortes observados en las zonas revisadas. Esta comprobación no es una auditoría visual de las tablas de requerimientos excluidas.

Los PDF actualizados sustituyen los del subdocumento 3 y sus anexos. El Formulario T-12 se conserva sin cambios. Las copias anteriores de ambos PDF se guardan en tmp/sd3_coherencia_sd2_build/respaldo_pdf_anterior.
