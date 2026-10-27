# Decisiones y datos que deben quedar fijados antes del reparto por SD

## Propósito y alcance

Basado en `C:/Users/henri/.claude/plans/me-aburr-de-revisar-rosy-treehouse.md`, olas1–4, **sin1.1 ni olas0/5**. El objetivo es que cada responsable reciba decisiones y datos comunes ya fijados y edite sólo sus SD, sin esperar que otra IA produzca sus entradas.

No es una lista de decisiones ya tomadas ni una orden de corrección. Tampoco todas las preguntas corresponden a libre elección: las Bases limitan las respuestas, y algunos cierres requieren cálculos o evidencia, no una preferencia del usuario. Lo que ya esté respaldado se confirma y no se reabre.

## A. Decisiones/acuerdos que deben cerrarse

| ID | Pregunta que debe quedar respondida | Resultado concreto que se necesita antes del reparto | Origen / afectados |
|---|---|---|---|
| D01 | ¿Qué versión y qué documento mandan para cada familia de datos, y qué se hace cuando dos SD discrepan? | Tabla de autoridades con archivo/versión: requisitos, arquitectura, datos, metodología, calendario/dotación, riesgos, pruebas e innovaciones. La jerarquía normativa se respeta; no se autoriza contradecir Bases por preferencia de un SD. Un documento dueño no vuelve infalibles todos sus valores | Acuerdo habilitante inferido del orden dueño→citante de ola2; todos |
| D02 | ¿Se mantiene el refuerzo de hasta16evaluadores diarios? ¿Con qué modalidad, períodos, jornada y condición de disponibilidad? | Compromiso formal o retiro aprobado, con meses/personas/jornada y confirmación de asignación. Si se retira/cambia, recalcular capacidad antes de repartir, no enviar una cifra distinta a cada IA | 2.4; SD6,SD7/T15,SD9/T13 |
| D03 | ¿Cuál es la capacidad de desarrollo/SRE que se compromete al proyecto y cómo se demuestra disponibilidad y competencias? | Distinguir plantilla corporativa de personal asignable y simultáneo; roles, dedicaciones, períodos y competencias requeridas. Resolver40/48 sin asumir que distinto universo es contradicción. Si se necesita refuerzo, debe quedar definido, no supuesto | 4.11/RV012; SD1,SD6,SD7 |
| D04 | ¿Qué autoridad tiene el Comité de Calidad y Procesos y cómo se integra con el gobierno del proyecto? | Mantener o ajustar la autoridad interna, composición, veto, escalamiento y relación con comités existentes; no atribuir a las Bases una facultad no comprobada. SD1 ya lo describe: debe decidirse su articulación, no inventar un órgano nuevo por defecto | 4.4; SD1,SD6/T9,SD9 |
| D05 | ¿Se ratifican duplicación≤3% y acoplamiento≤20 como reglas internas bloqueantes, y qué mide exactamente cada una? | Definición de métrica, unidad/denominador, ámbito, herramienta, puerta y fuente oficial T10. No basta con ratificar dos números; deben ser medibles y significar lo mismo en todos los SD | 2.5; SD6/T10,SD9/anexos |
| D06 | ¿Qué método y escalas se adoptan para analizar riesgos y escoger sus respuestas? | Técnica efectiva (p.ej., FMEA adaptada), escalas, cálculo, criterio de priorización, tratamiento del residual y método de costo-beneficio. Distinguir puntuación ordinal de exposición esperada en HH. Recuperar una FMEA histórica no equivale a aprobarla vigente | 4.1–4.3; SD8/T16; efectos SD7/SD13 |
| D07 | ¿Cuáles P7-01…P7-11 se aceptan como supuestos de planificación y qué acción se adopta si no se cumplen? | Matriz de los once supuestos: validez, validación, disparador, riesgo/respuesta, responsable y consecuencia sobre trabajo/reserva. No basta afirmar que todos se evaluarán después | 2.1; SD7/Anexo7F,SD8/T16 |
| D08 | ¿La reserva de gestión de1600HH sigue siendo un compromiso vigente y autorizado, o se reemplaza/retira? ¿Qué relación tiene con contingencias por riesgo? | Regla aprobada de separación, autorización, uso y no doble conteo. El monto técnicamente necesario se calcula, no se elige para que coincidan los textos. Diferenciar presupuesto, exposición, capacidad y holgura | 2.1,4.3,4.11/RV020; SD8,SD7/T15,SD6 |
| D09 | ¿Qué respuestas se financiarán/programarán y cómo se distribuyen reservas y esfuerzo entre roles, paquetes y períodos? | Matriz final riesgo→respuesta→HH→rol→paquete→mes/hito, nivelada contra capacidad. Incluye riesgos nuevos de obsolescencia/bloqueo/escalabilidad y evita contar dos veces un control compartido. Requiere cálculo técnico previo y aprobación del compromiso, no pedir al usuario que invente HH | 2.1,4.1,4.3; SD8/T16,SD7/T14/T15,SD9 |
| D10 | ¿Cuál es el programa definitivo de pruebas reales de DR y cómo queda respaldado por recursos, paquetes y evidencias? | Pruebas y alcance antes deH5/H10 conformeC8, periodicidad aplicable, prerrequisitos, ambiente, evidencia, responsable y ventanas permitidas. No es opción conservar una programación que incumpla un compromiso obligatorio; se decide la solución compatible | 4.5; SD9/T13,SD8,SD7 |
| D11 | ¿Cuál es la conducta ofertada ante indisponibilidadDTE cuando cambia la carga o se requiere un documento nuevo? | Escenarios permitidos/prohibidos, procedimiento de contingencia, autoridad, evidencia y recuperación; coherente con solución técnica vigente y requisitos. No inferir que una guía preemitida cubre cualquier modificación | 4.11/RV018; SD4,SD6,SD7/T18; pruebas SD9 si cambian |
| D12 | ¿Cuál es la unidad exacta de retención/bloqueo térmico y cómo se relacionan lote ySSCC? | Regla por escenario, propagación del bloqueo, autoridad de liberación y relación entre datos y unidades físicas. Si la fuente obliga a una unidad, aplicarla; no elegir una granularidad incompatible por comodidad | 2.15; SD2,SD3/RNG04,SD5; pruebas SD9 afectadas |
| D13 | ¿Qué compromisoOTIF final se oferta y cómo se distingue la referencia del caso de la meta propia y sus tramos? | Desigualdad exacta, fórmula, universo, período y metas intermedias/finales; la misma condición enR18-04 eI-04A. Verificar si la referencia «sobre95%» es exigencia o referencia antes de tratar95% exacto como admisible | 4.7; SD3,SD13; aceptación SD9 si corresponde |
| D14 | ¿Cuál es el alcance real de telemetría ofertado para flota propia y de terceros? | Universo por tipo de vehículo, datos disponibles, integración existente/nueva y tratamiento de no disponibles. No inferir que número de conductores o tripulantes es número de camiones. Cerrar si los54de terceros requieren cobertura y con qué respaldo | 4.8/RF14.01; SD3/T12,SD4/T11,SD5; pruebas SD9 |
| D15 | ¿Cómo se delimita el universo de sitios que se usa para requisitos, operación y dimensionamiento? | Inventario clasificado (CD,cross-docking,oficinas,otros), servicios por sitio y distinción estado actual/crecimiento. Resolver cinco/seis según el universo, no imponer un número único a conceptos distintos | 4.8/S22; SD2,SD3,SD4; efectos datos/pruebas |
| D16 | ¿Qué catálogo se congela como base de trabajo y cuál es la regla para IDs coincidentes, alias y estados de cumplimiento? | VersiónSD3/T12; política de identificación/procedencia; clasificación de ofrecidos, parciales,no cumplidos y alias. Conteos y matriz se generan desde esa base. Las brechas se mantienen visibles; no se cambia estado para cuadrar totales | 4.8,4.10; SD3/T12,SD5,SD9/T13 |
| D17 | ¿Qué esquema de numeración de anexos y destinos de remisiones se fija para que nadie lo cambie por su cuenta? | Convención de anexosSD2/SD3 y estructura publicada deSD4, con equivalencias necesarias. La estructuraSD4 debe verificarse en salida antes de corregirla: usar comandosTeX distintos no demuestra por sí solo numeración incorrecta. No reabreC15 de formularios | 3.13,3.15,2.11 y parte2.12; SD2,SD3,SD4 y citantes |

### Qué preguntas desbloquean más trabajo

1. **D02–D11:** capacidad, gobierno, calidad, riesgos y programación; son las principales causas de esperas entre SD6/7/8/9.
2. **D12–D16:** alcance funcional y datos; evitan que SD3 cambie después de que SD5/SD9/SD13 hayan trabajado con otra definición.
3. **D01 yD17:** autoridad/versiones y estabilidad de destinos; evitan que cada IA resuelva contradicciones de modo diferente.

No hace falta que el usuario responda17preguntas a ciegas. Para cada una se presenta evidencia vigente, propuesta compatible y consecuencia. Si el archivo ya la resuelve, se registra como confirmada.

## B. Datos/verificaciones necesarios, pero que no se deben decidir por preferencia

| Verificación | Qué hay que obtener | Relación con decisiones |
|---|---|---|
| ConteosRF/RNF/RT y casos | Totales reproducibles por prioridad/estado, requisito único frente a fila/alias; matriz y batería recalculadas | Derivados deD16; no preguntar «qué total quieres» |
| Capacidad, reservas y holguras | Jornada/días/roles/meses, HH y reserva conciliada; encaje de revisiones y evidencia de marcha blanca bajo fechasC4 | Derivados deD02/D03/D07–D10; no seleccionar una holgura sin calcularla |
| RNF04.01 | Comprobar y trasladar el umbral medible ya respaldado; elT12actual declara«tiempo acotado» en requisito y<20minen respuesta | 4.8; no es una elección libre si la fuente ya fija el umbral |
| IDsRF14.01…05 | Comprobar procedencia y mapeo existente; elSD3consultado ya utiliza sufijo-BTT para distinguir colisiones | ParteD16; no rehacer un mapeo resuelto |
| EntidadesSD5 | Definición y conteo reproducible que explique139/121 si la diferencia persiste | 4.10; lógico/físico/tablas no son necesariamente el mismo conteo |
| Certificaciones | Vigencia/evidencia y plan de renovación real; SD1consultado ya contiene un plan. Verificar si cubre todos los casos del diagnóstico antes de volver a preguntarlo | 4.6; no pedir elegir fechas de certificados ni declarar renovación inexistente; SD12excluido |
| Revisiones humanas | Quién revisó qué, qué evidencia existe y qué falta realmente; SD8manual segúnC14 | 3.10,4.10; no se completa mediante aprobación genérica inventada |
| Remisiones | Destino por título/label/contenido y equivalencias cuando cambie numeración | D17; no elegir un número de sección por preferencia |

## C. No volver a preguntar

No reabrirC1–C15 de ola0: nombres,IDs de riesgo,mes1,dos actas,dotación de terreno,SOC,coberturas,RTO/RPO,congelamientos,terminología,roles,títulos,citas,escalaIA,numeración de formularios. Comprobar su aplicación es distinto de volver a decidirlos.

Tampoco requieren un acuerdo nuevo por defecto: corregir erratas, introducir listas/tablas, llamar figuras antes de mostrarlas, usar fuentes reales, restaurar campos oficiales o cumplir restricciones de tablas del cuerpo. Son correcciones contra una regla existente, no elecciones abiertas.

## D. Qué debe recibir cada responsable de SD

Antes del reparto, preparar una única tabla aprobada:

`ID de decisión | valor/regla final | fuente y versión | documento dueño | SD consumidores | evidencia/cálculo | estado`

Una cifra derivada no se considera congelada hasta tener cálculo; una decisión no se considera aprobada por estar redactada como propuesta. Si se cambian entradas después de arrancar, reaparece la dependencia: no prometer independencia absoluta sin controlar cambios.

El próximo reparto será porSDexclusivos usando esta tabla como entrada; este archivo no activa los repartos anteriores ni autoriza modificar entregables.
