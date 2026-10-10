# LafroX — Resumen del Formulario T-12: Cumplimiento y trazabilidad

[Índice de resúmenes](README.md) · [Formulario original](../03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md)

## Para qué sirve

Relaciona lo exigido con su estado de cumplimiento documental, el componente que lo satisface y la sección de la propuesta que lo desarrolla. Es la consulta principal cuando se pregunta «¿dónde se atiende este requisito?»; no es un registro de pruebas ejecutadas.

## Cómo leer sus dos partes

[La Parte A — Requerimientos funcionales y no funcionales del Subdocumento 3](../03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md#parte-a--requerimientos-funcionales-y-no-funcionales-del-subdocumento-3) responde **181 filas RF y 90 RNF** de los Anexos 3.A y 3.B: **271 filas**. RF significa funcional; RNF, condición de calidad u operación. No todas las filas agregan una función independiente.

Ambas partes usan exactamente **cinco columnas**: **ID requerimiento, Descripción, Cumple, Componente que lo satisface y Sección de la propuesta**. EDT, prueba, criterio y origen ya no son columnas independientes; la sección citada conduce al desarrollo y a la evidencia pertinente.

[La Parte B — Requisitos de las Bases Técnicas Transversales](../03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md#parte-b--requisitos-de-las-bases-t%C3%A9cnicas-transversales) responde **374 RT**. Cuando el Caso 02 fija alcance o valor para un código RT, lo incorpora en la descripción de esa misma fila. Las dos partes reúnen **645 requerimientos**.

## Qué significan las respuestas

- **Cumple:** la solución está desarrollada en la propuesta.
- **Cumple parcialmente:** existe cobertura incompleta; la fila identifica lo que falta.
- **No cumple:** no hay solución acreditada para la exigencia.

La columna «Cumple» expresa cobertura documental, no pruebas ya ejecutadas. La implantación y aceptación se comprueban en los hitos comprometidos; OTIF de **95 % en mes 32** y metas anuales requieren seguimiento posterior a la marcha blanca.

## Decisiones que conviene conservar

**RF-03.11 cumple** al conservar el precio acordado al capturar el pedido y transmitirlo al ERP. **RF-03.12 cumple parcialmente**: exige detectar diferencias, bloquear la confirmación y notificar a Comercial, pero falta el precio por línea recibido para facturación y la interfaz que lo entregue para compararlo. La regla de precio no acredita por sí sola ese bloqueo.

**RT-05.10 cumple parcialmente**: cubre la retención que fija el Caso 02, pero falta el catálogo de datos con linaje automatizado exigido como deseable por las Bases Transversales. **RT-05.24 no cumple** por falta del portal de desarrolladores. **RT-05.30 cumple** mediante el modelo cinético determinista de INN-03; el bloque RT-26 remite a SD13/T-19 para innovaciones.

Los códigos RF-14.01–05-BTT evitan confundir seguridad de Bases con telemetría del caso. Para seguir paquetes y pruebas hay que consultar las secciones citadas y T-14/T-15, no buscar columnas que la matriz vigente no contiene.

## Lectura relacionada

El [resumen de SD3](LAFROX-Subdocumento3-Resumen.md) explica alcance y reglas; [sus anexos](LAFROX-Subdocumento3-Anexos-Resumen.md) contienen los requisitos completos. T-14/T-15 programan la ejecución. La revisión humana pendiente y las verificaciones futuras conservan su estado.

---

**Fuente y actualización:** documento local vigente al 8 de octubre de 2026. Resumen elaborado con asistencia de Codex; no acredita aprobación del CLIENTE ni revisión humana adicional.
