# Informe 2 — Tabla de TPS del Subdocumento 4

| Observación | Respuesta | Sección modificada |
| --- | --- | --- |
| La fila total de la tabla de TPS no explica por qué no suma los máximos de cada lugar. | Se rotula como máximo agregado coincidente. La nota distingue los máximos locales de los agregados por bloque, explica el supuesto del tramo 05:30–06:00 y documenta que los totales se calculan antes de redondear. | 4.2.6, Tabla 14 y Anexo 4-W.2. |
| El despacho muestra dos totales con un solo desglose por lugar. | Se separan despacho normal y despacho en septiembre. Ambas columnas muestran las contribuciones del tramo que determina su máximo. Se conservan los valores declarados de 12,34; 3,76; 6,94 y 14,66 TPS. | 4.2.6, Tabla 14. |

## Coherencia con los usos de la cifra

- 4.1 y el Anexo 4-W distinguen máximos modelados, no medidos. SV-04 eleva la tasa de la hora cargada sin restarla del resto del día. El resumen de cálculo identifica la tasa de cross-docking como el agregado de las tres plataformas; usarla como cota de un equipo no la convierte en tres cargas simultáneas.
- 4.2.6, el Anexo 4-W y el T-11 tratan la carga de nube y portal como solicitudes equivalentes en la estimación de capacidad. La prueba distingue solicitudes HTTP, eventos y trabajo por perfil. No se cambian las cantidades de tareas ni se acredita capacidad operativa por cálculo.
- Las proyecciones del año 3 usan la precisión interna del modelo. El escenario global de 3× usa los 14,66 TPS declarados. Los objetivos de ensayo usan los valores declarados: 21,99 TPS con la mezcla de septiembre y, por separado, 10,41 TPS durante 90 minutos de despacho con cero minutos de indisponibilidad. El T-13 y el plan de calidad se cotejaron en la referencia local de seguimiento `origin/LafroX-Subdoc9-LateX` (`37c4eb75`); no se modificaron.

## Verificación repetible

1. Regenerar la memoria con `python -B Dimensionamiento/dimensionamiento/calculo.py`.
2. Ejecutar `python -B Dimensionamiento/dimensionamiento/verificar_tps.py`. Comprueba la Tabla 14, las 24 filas y 288 tasas por representación, las ventanas ganadoras, el caso de redondeo y los objetivos de ensayo.
3. Ejecutar `.\compilar.ps1` y revisar la tabla y sus notas en el cuerpo, el perfil horario y los objetivos en los anexos, y el alcance de la cota de capacidad en el T-11. La corrección no ejecuta los ensayos de Preproducción.
