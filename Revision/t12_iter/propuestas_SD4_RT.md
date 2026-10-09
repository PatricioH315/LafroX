# LafroX — Decisiones SD4 para los RT restantes

Se aplicaron 14 de los 21 RT mediante frases en los componentes existentes; siete permanecen sin aplicar. La Tabla 1 registra la decisión y su fundamento. SD4 identifica `04_arquitectura/LAFROX-Subdocumento4.md`; SD4-Anexos, `04_arquitectura/LAFROX-Subdocumento4-Anexos.md`.

**Tabla 1 — Decisiones con mínimo arrastre**

| RT | Carácter | Decisión | Dónde quedó | Razón en una línea |
| --- | --- | --- | --- | --- |
| RT-05.24 | Deseable | No aplicado | Sin texto nuevo; T-12: No cumple | SD5 5.2.6 y 5.4.6 y Anexo 5-I lo excluyen expresamente; ofertarlo exige cambiar documentos prohibidos por la regla 1. |
| RT-06.15 | Deseable | No aplicado | Sin texto nuevo; T-12: No cumple | Dos racks y climatización N+1 no acreditan contención; cerrar un pasillo requiere definir elementos físicos adicionales. |
| RT-08.15 | Deseable | Aplicado | SD4 4.2.1.2 | Una unidad por tipo/variante para aceptación previa, luego incorporada al parque o reserva existentes. |
| RT-08.19 | Deseable | Aplicado | SD4 4.2.1.2 | Vida útil de 60 meses frente a 56: aplazamiento de renovación y sus residuos en 4 meses (7,1 %). |
| RT-09.10 | Deseable | Aplicado | SD4 4.2.4.1.1 | CI ejecuta carga de regresión en QA por versión candidata y semanalmente, dentro del horario de uso, y bloquea regresiones. |
| RT-11.28 | Deseable | Aplicado | SD4-Anexos 4-R | SAMM mide inicialmente y cada año los controles y prácticas ya previstos, con acciones de mejora. |
| RT-13.05 | Obligatorio | Aplicado | SD4 4.1.3.1 | Accesos de Angular/Kotlin en tres interacciones como máximo por función principal y perfil. |
| RT-13.09 | Obligatorio | Aplicado | SD4 4.1.3.1 | Sistema documentado con paleta, hasta dos familias, iconografía, retícula y componentes reutilizables. |
| RT-13.12 | Deseable | Aplicado | SD4 4.1.3.1 | Tema, texto y densidad por persona en su dispositivo; español, sin otros idiomas exigidos por el caso. |
| RT-14.09 | Deseable | Aplicado | SD4 4.1.3.8 | Detección de anomalías nativa de CloudWatch sobre la historia de cada métrica; alerta antes de los límites. |
| RT-15.05 | Deseable | No aplicado | Sin texto nuevo; T-12: No cumple | Falta comparación verificable de carbono regional y latencia; la residencia ya fijada no prueba menor intensidad. |
| RT-15.06 | Deseable | No aplicado | Sin texto nuevo; T-12: No cumple | El PUE y las potencias de diseño no permiten derivar una meta de reducción de consumo durante Operación. |
| RT-16.04 | Obligatorio | Aplicado | SD4 4.1.3.4 | Valores y perfiles implementados son configurables; algoritmos, reglas, estados y contratos nuevos requieren desarrollo. |
| RT-16.05 | Deseable | Aplicado | SD4 4.1.9 | QA compara el mismo juego de transacciones con parámetro vigente y propuesto antes de Producción. |
| RT-16.08 | Obligatorio | Aplicado | SD4 4.1.3.7 | Consola consulta/exporta gob_auditoria con los cuatro filtros y usa la exportación asíncrona de SD5 5.2.8. |
| RT-16.12 | Obligatorio | Aplicado | SD4 4.1.3.4 | Consola configura responsables, plazos y niveles mediante gob_asignacion y parámetros versionados. |
| RT-16.18 | Según caso | No aplicado | Sin texto nuevo; T-12: No cumple | POD/QR y acuse del ERP no acreditan sello de tiempo ni evidencia verificable tras vencer el certificado. |
| RT-16.19 | Obligatorio | Aplicado | SD4 4.1.6.2 | not_plantilla/cuerpo_ref permite plantillas CLIENTE y comprobantes transaccionales en HTML abierto. |
| RT-16.26 | Deseable | No aplicado | Sin texto nuevo; T-12: No cumple | INT-11 envía avisos; recibir respuestas y ejecutar acciones exige ampliar el canal e integración existentes. |
| RT-16.33 | Obligatorio | No aplicado | Sin texto nuevo; T-12: No cumple | 2.000 contactos de demanda y 2.283 de capacidad no estiman contactos evitados por autoatención. |
| RT-17.08 | Deseable | Aplicado | SD4 4.1.3.1 | Vista ligera del portal Angular en teléfonos económicos/anteriores con navegador y sistema compatibles. |

Fuente: Bases Técnicas Transversales, caps. 5–17; Caso 02, cap. 15; SD4, Anexo 4-W.7 y SD5 vigentes. El aplazamiento de RT-08.19 cuantifica tiempo de renovación, sin atribuir masa de residuos ni emisiones evitadas. Los textos son compromisos de oferta, no resultados de implementación o ensayos ejecutados.

## Datos o decisiones que faltan

Los siete RT no aplicados requieren resolver lo siguiente antes de ofertarlos:

- **RT-05.24:** autorizar el cambio de la exclusión expresa en `05_modelo_datos/LAFROX-Subdocumento5.md` 5.2.6/5.4.6 y `LAFROX-Subdocumento5-Anexos.md` 5-I; definir el espacio de documentación y credenciales de prueba autoservidas.
- **RT-06.15:** definir y autorizar una contención física concreta de pasillo frío o caliente, sus elementos y compatibilidad con los dos racks y la sala de SD4 4.3.1.4.
- **RT-15.05:** datos comparables de intensidad de carbono de sa-east-1/us-east-1 y alternativas, período y método, latencias medidas y decisión compatible con la residencia de datos de SD4 4.2.3.2/4.3.2.
- **RT-15.06:** línea base de consumo en kWh por período y ámbito y una medida con ahorro calculable que fundamente la meta; definir medición y reporte anual. 13,4 kW y PUE 1,5 son diseño, no línea base de Operación.
- **RT-16.18:** identificar los actos y certificados que requieren verificación de larga duración según Caso 15 (RT-16.14), la capacidad acreditada del ERP y una autoridad de sellado de tiempo con evidencia de validación conservable. V-18 del Anexo 4-V no acredita ese servicio.
- **RT-16.26:** autorizar recepción y ejecución de acciones por un canal conversacional, con capacidad bidireccional del proveedor y controles de identidad/confirmación; envío por WhatsApp no demuestra esa capacidad.
- **RT-16.33:** volumen comparable de atención asistida y proporción de motivos resolubles por autoatención con adopción estimada; de ahí derivar contactos evitados y comprometer la reducción y su indicador. (2.283 − 2.000) ÷ 2.283 = 12,4 % es holgura de capacidad, no reducción de atención.
