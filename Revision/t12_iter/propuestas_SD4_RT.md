# LafroX — Decisiones SD4 para los RT restantes

Se aplicaron 18 de los 21 RT mediante frases en los componentes existentes y los supuestos S-42/S-43; tres permanecen sin aplicar por decisión del usuario. La Tabla 1 registra la decisión y su fundamento. SD4 identifica `04_arquitectura/LAFROX-Subdocumento4.md`; SD4-Anexos, `04_arquitectura/LAFROX-Subdocumento4-Anexos.md`.

**Tabla 1 — Decisiones con mínimo arrastre**

| RT | Carácter | Decisión | Dónde quedó | Razón en una línea |
| --- | --- | --- | --- | --- |
| RT-05.24 | Deseable | No aplicado | Sin texto nuevo; T-12: No cumple | Por decisión del usuario; SD5 5.2.6 y 5.4.6 y Anexo 5-I lo excluyen expresamente. |
| RT-06.15 | Deseable | Aplicado | SD4 4.3.1.4 | Paneles ciegos, sellado de cable y orientación frente-frío / trasera-caliente reducen mezcla y recirculación, mejorando eficiencia y PUE estimado. |
| RT-08.15 | Deseable | Aplicado | SD4 4.2.1.2 | Una unidad por tipo/variante para aceptación previa, luego incorporada al parque o reserva existentes. |
| RT-08.19 | Deseable | Aplicado | SD4 4.2.1.2 | Equipos reparables en servicio al menos 60 meses desde su recepción, sin renovación general al cierre. |
| RT-09.10 | Deseable | Aplicado | SD4 4.2.4.1.1 | CI ejecuta carga de regresión en QA por versión candidata y semanalmente, dentro del horario de uso, y bloquea regresiones. |
| RT-11.28 | Deseable | Aplicado | SD4-Anexos 4-R | SAMM mide inicialmente y cada año los controles y prácticas ya previstos, con acciones de mejora. |
| RT-13.05 | Obligatorio | Aplicado | SD4 4.1.3.1 | Accesos de Angular/Kotlin en tres interacciones como máximo por función principal y perfil. |
| RT-13.09 | Obligatorio | Aplicado | SD4 4.1.3.1 | Sistema documentado con paleta, hasta dos familias, iconografía, retícula y componentes reutilizables. |
| RT-13.12 | Deseable | Aplicado | SD4 4.1.3.1 | Tema, texto y densidad por persona en su dispositivo; español, sin otros idiomas exigidos por el caso. |
| RT-14.09 | Deseable | Aplicado | SD4 4.1.3.8 | Trabajo programado con reglas estadísticas deterministas (sin IA, por D-09) sobre la historia de CloudWatch; alerta antes de los límites. |
| RT-15.05 | Deseable | No aplicado | Sin texto nuevo; T-12: No cumple | Por decisión del usuario; falta comparación verificable de carbono regional y latencia. |
| RT-15.06 | Deseable | Aplicado | SD4 4.2.3.4; SD3-Anexos 3.C, S-43 | Meta de al menos 60 % menos horas de cómputo no productivo, horario 60/168 h (64,3 % potencial), medición mensual y reporte anual con T-14 8.4.3. |
| RT-16.04 | Obligatorio | Aplicado | SD4 4.1.3.4 | Valores y perfiles implementados son configurables; algoritmos, reglas, estados y contratos nuevos requieren desarrollo. |
| RT-16.05 | Deseable | Aplicado | SD4 4.1.9 | QA compara el mismo juego de transacciones con parámetro vigente y propuesto antes de Producción. |
| RT-16.08 | Obligatorio | Aplicado | SD4 4.1.3.7 | Consola consulta/exporta gob_auditoria con los cuatro filtros y usa la exportación asíncrona de SD5 5.2.8. |
| RT-16.12 | Obligatorio | Aplicado | SD4 4.1.3.4 | Consola configura responsables, plazos y niveles mediante gob_asignacion y parámetros versionados. |
| RT-16.18 | Según caso | Aplicado | SD4 4.1.17; Tabla 17; SD4-Anexos 4-U | XML firmado por ERP, acuse SII y POD con hash, marca de tiempo y cadena disponible en S3 Object Lock por seis años; Cumple por decisión del usuario. |
| RT-16.19 | Obligatorio | Aplicado | SD4 4.1.6.2 | not_plantilla/cuerpo_ref permite plantillas CLIENTE y comprobantes transaccionales en HTML abierto. |
| RT-16.26 | Deseable | No aplicado | Sin texto nuevo; T-12: No cumple | Por decisión del usuario; recibir respuestas y ejecutar acciones exige ampliar INT-11. |
| RT-16.33 | Obligatorio | Aplicado | SD4 4.1.3.1; SD3-Anexos 3.C, S-42 | Meta de al menos 15 % menos consultas asistidas por cliente activo al cierre del primer año, línea base en marcha blanca y reporte mensual. |
| RT-17.08 | Deseable | Aplicado | SD4 4.1.3.1 | Vista ligera del portal Angular en teléfonos económicos/anteriores con navegador y sistema compatibles. |

Fuente: Bases Técnicas Transversales, caps. 5–17; Caso 02, cap. 15; SD4, Anexo 4-W.7 y SD5 vigentes. El aplazamiento de RT-08.19 cuantifica tiempo de renovación, sin atribuir masa de residuos ni emisiones evitadas. Los textos son compromisos de oferta, no resultados de implementación o ensayos ejecutados.

## Datos o decisiones que faltan

Los tres RT no aplicados se mantienen fuera de la oferta por decisión del usuario. Reconsiderarlos requeriría resolver lo siguiente:

- **RT-05.24:** autorizar el cambio de la exclusión expresa en `05_modelo_datos/LAFROX-Subdocumento5.md` 5.2.6/5.4.6 y `LAFROX-Subdocumento5-Anexos.md` 5-I; definir el espacio de documentación y credenciales de prueba autoservidas.
- **RT-15.05:** datos comparables de intensidad de carbono de sa-east-1/us-east-1 y alternativas, período y método, latencias medidas y decisión compatible con la residencia de datos de SD4 4.2.3.2/4.3.2.
- **RT-16.26:** autorizar recepción y ejecución de acciones por un canal conversacional, con capacidad bidireccional del proveedor y controles de identidad/confirmación; envío por WhatsApp no demuestra esa capacidad.
