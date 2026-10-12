# LafroX — Revisión del supuesto de 2.000 contactos mensuales

11 de octubre de 2026. Registro de revisión, no un dato nuevo aprobado para la oferta.

## Rectificación histórica — 12 de octubre de 2026

La revisión del 11 de octubre sólo evaluaba SV-06 vigente; omitió una versión anterior recuperada de Git. Ya existía separación entre régimen (620), oleadas (1.550) y peak supuesto (+40 %), reemplazada el 26 de septiembre en a5e6500. Ver [auditoría histórica](revision_historica_demanda_mesa_SD1_SD4.md). Las tasas son supuestos permitidos por Caso §14.2; la falta de historial real no las invalida automáticamente. El pendiente es justificar el escenario y conciliar calendario, población y cobertura, no inventar todo desde cero ni rebajar la cifra arbitrariamente. «La cifra es alta» en el corte anterior es valoración no acreditada por un benchmark: no se usa como prueba de sobredimensionamiento.

## Veredicto del corte anterior

**La cifra de 2.000 no proviene de las Bases ni de un registro de incidentes. Es un supuesto de diseño del Anexo 4-W.7. No está justificado presentarlo como la demanda mensual esperable de la mesa.**

El Caso, cap. 14.2, p. 25 impresa del PDF original, deja «Contactos mensuales a la mesa de ayuda» **a estimar y declarar como supuesto**. No prescribe 2.000. La fuente identificada para el cálculo es el Anexo 4-W.7 del SD4, que multiplica 640 trabajadores propios + aproximadamente 160 conductores externos por **2,5 contactos por persona y mes**, bajo el supuesto SV-06. Resultan 800 × 2,5 = 2.000. El factor 2,5 no está respaldado por historial, encuesta o dato del Caso.

## Interpretación y problemas

- Un **contacto** es una interacción con la mesa, no necesariamente una falla distinta, un ticket único ni una persona única. Puede tratarse de una consulta o seguimiento. Sin embargo, el modelo no desglosa estos motivos ni aporta sus frecuencias; esa posibilidad no valida 2.000.
- Implica **30 contactos anuales por cada una de las 800 personas consideradas**. En un mes con 26 días de atención de lunes a sábado serían aproximadamente 77 contactos diarios. La cifra es alta y exige justificación, especialmente si se presenta como demanda ordinaria y no como escenario de estrés.
- Los **22,14 días equivalentes** usados para repartir las llegadas salen de 31.000 pedidos ÷ 1.400 entregas diarias. Son una equivalencia de entregas; no demuestran cuántos días opera la mesa. Su uso para proyectar llamadas y la concentración del 25 % en una sola hora son otros dos supuestos sin evidencia independiente.
- La población de 800 excluye a 14.200 clientes y 180 proveedores citados en el dimensionamiento de usuarios. Hay que definir qué colectivos acceden realmente a la mesa y qué consultas se derivan a otros canales. No se deben sumar todos automáticamente, pero tampoco afirmar sin aclaración que 800 representan toda la demanda atendible.
- Los 2.283/2.391 contactos mensuales son **capacidades modeladas para esa distribución horaria y dotación**, no demanda observada ni prueba de que 2.000 contactos vayan a ocurrir. Si cambia el supuesto de demanda, deben revisarse conjuntamente distribución horaria, tiempo de atención, agentes y HH; no basta reemplazar un número aislado.

## Recomendación

1. Retirar la presentación de «2.000 contactos mensuales» como **demanda base validada**. Si se mantiene mientras se decide el redimensionamiento, etiquetarlo expresamente como **escenario hipotético alto SV-06**, no como incidencia histórica ni previsión acreditada.
2. Definir qué es contacto y qué población cubre la mesa: empleados, transportistas, clientes y proveedores; distinguir incidente, consulta, solicitud y seguimiento, para evitar conteos dobles.
3. Si existe historial de contactos, usar 3–6 meses con fecha/hora, canal, tipo, duración, usuario y ticket asociado. Si no existe porque el caso es ficticio, acordar una **hipótesis nueva y explícita**, con escenarios de sensibilidad, sin venderla como dato del CLIENTE. A modo de comparación aritmética, 0,25/0,5/1 contacto por persona-mes sobre la misma población de 800 darían 200/400/800; son ejemplos para decisión, **no cifras aprobadas**.
4. Recalcular y alinear SD1, SD4 cuerpo y Anexo 4-W.7, SD7 y T-15 sólo después de fijar la hipótesis. Revisar también el calendario de atención y sus HH. No cambiar el PDF del T-15 sin nueva autorización expresa del usuario.

## Estado

Este hallazgo **no modifica** las cifras de los entregables. La presente petición fue de revisión de plausibilidad, no una autorización para inventar una demanda sustitutiva ni para alterar paquetes de trabajo o alcance de otros subdocumentos. La corrección terminológica CMMI solicitada por separado sí se ejecuta en SD1 LaTeX y su espejo Markdown.
