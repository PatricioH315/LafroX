# K6 — Reconciliación local y condiciones de cierre

Implementación del plan de trece puntos aprobado por el usuario el 27-10-2026. Base `93a5e884`. Los resultados se reproducen con `verificar_frente_b.py` y `../recalcular_cpm_20261025.py` desde cualquier directorio.

## Resultado local

Se conservan los 227 paquetes (168 con fechas y 59 continuos), las 220.023 HH, las fechas de la tabla de paquetes y las curvas de horas/personas. El peak conjunto sigue en 64, mes 16. `K6_VERIFICACION.json` compara las cuatro fuentes numéricas con K4 y documenta los escenarios de cierre.

El CPM separa la duración global de ventana del trabajo interno mínimo de los módulos. Antes, la construcción absorbía toda la ventana menos contratos/integración; una espera por interfaz se propagaba de nuevo como trabajo obligatorio y desplazaba 3.4.10, H4 y el piloto. La corrección mantiene los vínculos, los equipos máximos y toda la ventana inicio–fin. Los 168 paquetes calculados coinciden con sus fechas publicadas. No constituye planificación detallada ni prueba de recursos reales disponibles.

Las holguras agregadas se mantienen: H1 5; H2 11; H3 17; H4 16; H5 20; H7 2; H8 14; H9 19; H10 13; H12 3 días hábiles. H6/H11 son inicios fijos. Son resultados condicionados; no resuelven por sí mismos la aceptación del cierre.

## Actas: conflicto que requiere decisión

Dos actas por etapa: cierre de marcha blanca (4.2.1/4.3.1), previo a producción; aceptación H7/H12 (4.2.3/4.3.3), posterior. Se corrigieron títulos y explicaciones de T14/T18 y las láminas editables de EDT afectadas.

El art. 18.3 consultado da al CLIENTE diez días hábiles para revisar cada entregable. No obliga a que tarde siempre diez, pero la programación no puede garantizar una respuesta en dos sin un procedimiento confirmado. El escenario conservador entrega el primer hábil después de completar la evidencia y revisa desde el siguiente:

| Evento | E1 | E2 |
|---|---|---|
| Últimos 28 días completos | 03–30 abril 2028 | 03–30 septiembre 2028 |
| Entrega completa, supuesto | 02 mayo | 02 octubre |
| Diez días hábiles de revisión | 03–16 mayo | 03–17 octubre |
| Producción objetivo conservada | 05 mayo | 05 octubre |
| Días de revisión anteriores a producción | 2 | 2 |
| Aceptación objetivo conservada | 29 mayo | 25 octubre |

El calendario es el supuesto interno heredado, pendiente de confirmación. Incluso sin subsanación, los diez días completos no caben antes de producción. Las cuatro semanas no se recortan ni se acepta evidencia futura. La preparación preliminar no reemplaza revisión formal ni garantiza subsanación. Hace falta acordar por escrito el procedimiento de cierre con CLIENTE/C; si exige reprogramación, presentar alternativas al usuario antes de cambiar fechas. K6 no se declara cerrado integralmente.

## Recursos y reservas

- Obra civil de separación: CLIENTE, RT-06.06; especificación/coordinación y piso técnico del alcance de LafroX. Necesidad en mes 3 y recepción mes 4 no equivalen a disponibilidad confirmada. Se añadió 6.1.1 a los criterios de recepción 6.1.5.
- SOC propio en Valparaíso, analistas contratados antes de mes 13 bajo SEG. Las horas de cobertura ya figuran en 8.1.5; confirmar turnos, relevos y separación del resto de seguridad.
- 48 DES son dotación de la división (SD1), no disponibilidad del contrato. Se retiró la afirmación no demostrada de máximo diario de 40.
- SD6 consultado no respalda «16 evaluadores/día». SD9 lo toma de T15: había dependencia circular. Se retiró la atribución a SD6 y se dejó explícita la condición de asignación/refuerzo pendiente.
- `K6_CAPACIDAD.csv` calcula dos escenarios de ventanas para entregables: demanda media uniforme y suma de máximos. Ninguno es demanda real diaria; no incluyen todo el servicio continuo ni acreditan nivelación. El escenario uniforme llega a DES 40,788, CAL 12,955, ARQ+DAT 14,331; señala necesidad de detallar asignación. La suma de máximos (DES 132, CAL 14, ARQ+DAT 22) es una cota, no un requerimiento de contratación.
- `K6_INTERVALOS_CAPACIDAD.csv` aporta una condición necesaria de factibilidad. Para CAL, entre 25-10 y 11-11-2027 hay 1.049,60 HH que no caben fuera del intervalo aun usando los máximos declarados; diez personas sólo ofrecen 832 HH en sus trece días hábiles. Brecha: 217,60 HH. Se requieren **al menos 13 CAL en algún momento**, sin contar servicios continuos. Es una cota inferior, no prueba de suficiencia de 13 ni orden de contratación. Resolver con C/E refuerzo o nivelación antes de aprobar recursos. Para las otras familias, no detectar violación de esta condición necesaria no demuestra factibilidad conjunta ni disponibilidad.
- 1.600 HH de gestión: SD8 las identifica como históricas, sin aprobación ni disponibilidad. No se suman. Otras 1.600 HH corresponden al esfuerzo de pruebas E2, cuenta 3.9; son otro concepto ya incluido en los paquetes.
- Reserva E1 3.072 HH = 8 × (256 DES + 128 CAL), ya incluida. Sin K5 aprobado no se crean reservas adicionales ni se asigna una reserva a riesgos por inferencia.
- La nueva columna de resumen identifica el peak **conjunto del período** a partir de la curva real publicada, no la dotación exclusiva de cada etapa. Los peaks exclusivos y la simultaneidad diaria siguen sujetos a planificación de actividades. El formulario oficial consultado exige personas, sin una tabla de columnas fijas; se conserva la tabla y se explica este alcance.

## Pruebas y operación

Se incorporaron las tres coberturas diferenciadas, el criterio de salida DR y los cuatro bloques de 80 HH dentro de cada campaña existente de 320 HH. Se mantienen las ventanas anteriores a H5/H10 y las siete campañas de operación (560 HH); no se inventan horas ni pruebas ejecutadas. Recursos SRE/SEG de apoyo y campañas semestrales exactas requieren el programa confirmado de C. El canario técnico revierte automáticamente; SRE supervisa y valida. Los cambios de indicadores de funcionalidad y la contingencia operacional conservan su autorización propia.

Se distinguió congelamiento total 1–25 septiembre de prohibición de paso a producción todo septiembre/diciembre. La política de despliegue de SD4 consultada también excluye todo septiembre: se conserva identificada como política adicional, sin convertirla en prohibición de toda actividad documental. No se cambian políticas de arquitectura unilateralmente.

## Referencias, tablas y archivos

Se añadieron llamadas previas a las 17 láminas EDT, se verifican sus códigos contra los 227 de T14 y se actualizan las láminas afectadas por cobertura/actas. Las referencias a «T15, Tabla 6.1» se sustituyen por sección 6.1 y título. Se localizó T17 en SD9; está fuera de esta rama y se conserva como documento del frente C. Sus secciones 1/2 contienen plazos, 4.1 calendario.

`K6_REFERENCIAS_EXTERNAS.csv` inventaría las remisiones y `FUENTES_CONSULTADAS.json` conserva SHA/blob de fuentes locales. Se contrastó la rama vigente local `origin/subdoc-4` en `b0606ac9`, indicada por el plan original, además de su antecedente de consistencia. Su índice PDF confirma 4.1.4.4 «Módulo M3 Preventa», 4.2.4.1.2 «Liberación y reversión» y 4.3.2.4 «RPO y RTO»; el texto fuente respalda la coordinación de reserva/retención, los disparos automáticos y los objetivos de recuperación. El Anexo 4-W.7 corresponde al dimensionamiento de mesa/operación. `DESTINOS_VERIFICADOS.csv` conserva los destinos principales; K1 debe confirmar versiones posteriores y los demás cruces antes del cierre integrado. No se añadieron capítulos excluidos.

`K6_TABLAS.csv` inventaría tablas y fuentes; `K6_VERIFICACION.json` lista seis archivos sin inclusión. Se conservan: cuatro declaraciones IA individuales cubiertas por la declaración principal, tabla de fechas agrupadas y escenario histórico de contingencia. Se preservan cálculos/evidencias y no se eliminan archivos por no estar incluidos. El escenario histórico no alimenta K6. La fecha/versión/nombre ZIP siguen la ficha común existente de 12-10-2026/v1.0; no se inventó una nueva versión coordinada. La nueva intervención IA se declara con revisión humana posterior pendiente, conservando las declaraciones históricas.

## Entrega y pendientes de coordinación

Los puntos locales se implementan y verifican; el cierre integral sigue condicionado a: procedimiento y fechas de cierre, disponibilidad nominal/refuerzos, K1 de referencias/arquitectura, K3 de pruebas y K5 de riesgos/reservas. Estos pendientes no se presentan como resultados aprobados. Los archivos de otras ramas se consultaron mediante Git, sin modificarlos ni enviar mensajes externos. La compilación y QA visual quedan registradas en `VALIDACION_FINAL.md`.

## Ajuste posterior solicitado por el usuario

Se retiró la fila adicional «Revisión del frente B, 27-10-2026» de la declaración de IA. Se conservaron las otras ocho filas, se recompiló SD7 y su entrada main.tex y se sincronizó el Markdown. El documento queda en 66 páginas; la declaración termina en la página 66.
