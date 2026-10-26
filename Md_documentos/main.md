# Subdocumento 8: Plan de riesgos

## Introducción a la gestión de riesgos

Este plan organiza los 45 riesgos vigentes del proyecto (R-001–R-045) en siete categorías de la EDR, según su fuente predominante. Para cada riesgo conserva un ID y articula identificación, valoración, respuesta y seguimiento; la categoría no determina por sí sola la prioridad ni limita las áreas que pueden verse afectadas.

La valoración cualitativa utiliza los niveles ordinales y las ponderaciones decimales de probabilidad e impacto, con la zona registrada para cada riesgo. La cuantificación del esfuerzo se mantiene separada: el valor esperado se calcula como $p_0\times HH^{\mathrm{cond}}$. La suma de los 45 riesgos, **2.058,480 HH**, se adopta como contingencia en esfuerzo; no es un monto monetario ni un resultado de simulación. Los objetivos residuales siguen condicionados a validar la eficacia de las respuestas.

El Anexo 8.A reúne las fichas de respuesta de los 45 riesgos. Registra los datos disponibles y señala como pendientes de definición por responsable los plazos, las contingencias y los riesgos secundarios que no están sustentados; tampoco presume eficacia de las mitigaciones. El Anexo 8.B presenta el detalle de $p_0$, impactos condicionales y valores esperados. El Formulario T-16 conserva por separado su formato obligatorio (Distribuidora Puelche S.A., 2026d, sección 11).

## Plan de riesgos

Esta sección define cómo se gestionan los riesgos durante los 56 meses: el ciclo y sus instancias, los roles y su autoridad, las escalas con que se analizan y las reglas de registro y cierre.

### Enfoque y ciclo

El registro vivo sigue identificación, análisis, respuesta y seguimiento conforme a la norma ISO 31000 (International Organization for Standardization [ISO], 2018), que exige el RT-19.04 de las Bases Técnicas Transversales (Distribuidora Puelche S.A., 2026b). Cada entrada distingue causa, evento incierto y consecuencia, sin convertir una inconsistencia observada en riesgo futuro. El Anexo 8.E separa problemas y dependencias actuales.

JP mantiene el registro único. Los líderes identifican riesgos al revisar interfaces, pruebas, capacidad y despliegues; verifican disparadores semanalmente y ante cada cambio. El Comité de Proyecto quincenal revisa todos los riesgos abiertos, responsables, plazos y evidencia. Los comités Ejecutivo y de Arquitectura mensuales deciden escalamiento y cambios de sus ámbitos, y desde el mes 13 el Comité de Operación mensual revisa los riesgos de servicio: niveles de atención, incidentes, capacidad y continuidad (SD6, sección 6.1.6). Una amenaza a continuidad, seguridad o hito se escala inmediatamente. Marcha blanca exige seguimiento diario; operación mantiene vigilancia diaria de incidentes y colas y revisión en comités. En cada comité se compara la reserva restante con el riesgo remanente (análisis de reserva), y al cierre de cada etapa, en el H5 y el H10, una auditoría de riesgos comprueba que el proceso funciona (PMI, 2017, p. 456). El Comité Ejecutivo recibe cada mes un extracto con los diez riesgos de mayor exposición; el registro completo queda en el repositorio del proyecto.

### Roles y autoridad

La Tabla 8.1 distingue al responsable del riesgo, la familia de esfuerzo y su vigencia. Los responsables dirigen equipos; no ejecutan solos las HH. Las familias del T-15 se conservan al relevar liderazgo.

**Tabla 8.1. Responsabilidad y vigencia por familia.** Fuente: SD1 Tabla 1.3, SD13 y T-16.

| Familia | Hasta mes 21 | Meses 22–56 | Autoridad/aprobación |
|---|---|---|---|
| JP | Alex Aravena | Alex Aravena, dirección de contrato | Registro/escalamiento |
| ARQ | Bastián Trejo | Trejo, Comité Arquitectura | Diseño/frontera DR |
| SEG | Álvaro Catalán | Álvaro Catalán | Seguridad/privacidad |
| DAT | Leandro Chamorro | Guillermo Castillo; equipo DAT | Miño/Calidad: parámetros |
| DES | Tomás Pérez | Guillermo Castillo; equipo DES | CAL: verifica cambios |
| CAL | Maximiliano Miño | Maximiliano Miño | Evidencia/eficacia |
| SRE | Guillermo Castillo | Guillermo Castillo | Capacidad/continuidad |
| IMP | Patricio Henríquez | Guillermo Castillo; equipo IMP | CAL: usuarios; SEG: privacidad |

Las responsabilidades de DAT e IMP se transfieren al frente F8 de Operación, como establece el SD13. Para que no dependan de una sola persona, desde el mes 22 Bastián Trejo, que sigue en el Comité de Arquitectura, es suplente de Guillermo Castillo en DAT y DES, y Maximiliano Miño lo es en IMP; ambos continúan hasta el mes 56 (SD1, Tabla 1.3). Las decisiones sanitarias requieren aprobación de Calidad y las de privacidad, de Seguridad. La Contraparte Técnica acepta con acta; Operaciones autoriza cortes y Calidad del CLIENTE decide sobre los aspectos sanitarios. La agenda de decisiones se fija en mes 1 y se sigue en el registro. Los cambios físicos siguen el gobierno de arquitectura.

### Escalas previas al análisis

Para poder realizar un buen análisis de riegos, debemos de definir la probabilidad (P), el impacto (I) y la prioridad (P x I).

La probabilidad cualitativa (P) expresa el juicio ordinal sobre la posibilidad de ocurrencia del riesgo. Se asigna en una escala de **1 a 5** mediante las bandas de ponderación cualitativa $q$ de la tabla 8.2. Estas bandas no se aplican a $p_0$, la estimación inicial porcentual de ocurrencia que se presenta en el Anexo 8.B y se usa para el valor esperado en HH.

**Tabla 8.2. Escala cualitativa de probabilidad.** Fuente: elaboración propia basado en contenido academico.

| Valor | Banda cualitativa ($q$) | Descripción | Criterio cualitativo |
|---:|---|---|---|
| 1 | $1%\leq q\leq10%$ | Muy baja | Poco probable que ocurra; condiciones excepcionales |
| 2 | $11%\leq q\leq30%$ | Baja | Puede ocurrir en casos aislados |
| 3 | $31%\leq q\leq50%$ | Media | Podría ocurrir algunas veces durante el proyecto |
| 4 | $51%\leq q\leq70%$ | Alta | Ocurrirá con frecuencia si no se mitiga |
| 5 | $q\geq70%$ | Muy alta | Casi seguro de que ocurra |

Por otro lado, el impacto (I) representa el nivel de afectación que tendria el riesgo si llegara a materializarse. Se evalúa también en una escala de **1 a 5**, donde 1 representa un impacto insignificante y 5 un impacto muy alto.

**Tabla 8.3. Escala de impacto.** Fuente: elaboración propia basado en contenido academico.

| Valor | Descripción | Criterio cualitativo |
|---:|---|---|
| 1 | Insignificante | Impacto imperceptible en el proyecto |
| 2 | Menor | Afectación leve, fácil de controlar |
| 3 | Moderado | Impacto parcial en entregables o plazos |
| 4 | Alto | Afecta hitos principales o desempeño general |
| 5 | Muy alto | Compromete el éxito total del proyecto |

La ponderación decimal cualitativa de probabilidad e impacto produce la exposición $P\times I$.

**Escala de exposición.** Fuente: elaboración propia basado en contenido academico.

| Valor | Zona |
|---|---|
| $P\times I<0.08$ | Baja |
| $0.08\leq P\times I<0.20$ | Media |
| $0.20\leq P\times I<0.40$ | Alta |
| $P\times I>0.40$ | Crítica |

La zona de prioridad de cada riesgo es la zona registrada y adoptada del registro vigente; no se infiere a partir de umbrales sobre la exposición decimal. Los niveles ordinales de P e I se conservan junto con sus ponderaciones decimales. $p_0$ y las HH permanecen separados.

### Registro y cierre

El responsable actualiza fuente, estado, disparador, tratamiento, consumo de HH y evidencia. Estados: identificado, en tratamiento, control verificado o materializado. Materializar el evento abre un problema y conserva su ID. CAL verifica cierre técnico; JP registra la decisión; la aceptación contractual corresponde al CLIENTE. La puntuación residual efectiva exige eficacia comprobada; C.5 sólo compara hipótesis. Verificar un control no libera reserva automáticamente. Ninguna aceptación de riesgo exime requisitos obligatorios.

## Identificación y Análisis de Riesgos

Esta sección identifica los riesgos con una RBS y los analiza cualitativamente mediante la exposición decimal ($q_P\times q_I$), junto con los niveles ordinales de P e I y la zona registrada para cada riesgo, y cuantitativamente mediante el valor esperado de cada riesgo en horas-hombre. No se presentan resultados de simulación, percentiles ni probabilidades de cumplimiento.

### RBS y análisis separados

La estructura de desglose de riesgos (EDR o RBS, por sus siglas en inglés) organiza los 45 riesgos del registro vigente (R-001–R-045) en siete categorías, según su fuente predominante: Solución y tecnología (14), Integración y legado (7), Operación del cliente (8), Personas y adopción (7), Contrato y licitación (4), Regulatorio y externo (2) y Empresa proveedora (3). La Figura presenta esta clasificación. Cada riesgo conserva un ID y una categoría principal; la agrupación identifica su fuente predominante, pero no limita las áreas que pueden verse afectadas ni determina por sí sola su prioridad.

![Estructura de desglose de riesgos (EDR/RBS) del proyecto LafroX: siete ramas y 45 riesgos. Fuente: elaboración propia a partir del registro de riesgos actualizado.](../08_plan_riesgos/figuras/EDR_LafroX-Página-3.drawio.svg)

La rama **Solución y tecnología** reúne los riesgos del funcionamiento y la continuidad de la solución: calidad de datos, reconexión, autonomía móvil, operación en frío, trazabilidad sanitaria, capacidad, recuperación, seguridad y dependencias tecnológicas. Incluye, por ejemplo, los conflictos y duplicados tras reconexión (R-005), el retiro sanitario sin trazabilidad completa (R-012) y la recuperación y el retorno que exceden RTO/RPO (R-015). También incorpora las innovaciones de reproducción de incidentes (INN-02, R-037) y estimación de vida útil (INN-03, R-038). Es la rama con más riesgos; esa cantidad describe la distribución del registro y no determina por sí sola su prioridad.

**Integración y legado** agrupa las dependencias de interfaces del ERP, telemetría de terceros, convivencia del WMS, certificación EDI, avisos, pagos y datos de ruteo; entre ellas están las interfaces del ERP no utilizables (R-001) y la certificación EDI dependiente de las cadenas (R-030). **Operación del cliente** reúne las condiciones de conectividad, infraestructura, disponibilidad de contrapartes, ventanas de intervención, instalaciones y control de los flujos físicos y de efectivo. Ejemplos son la caída simultánea de enlaces de Concepción (R-006), las contrapartes que no validan a tiempo (R-022) y las devoluciones y envases que alteran saldo o custodia (R-044).

**Personas y adopción** aborda la objeción sindical y la privacidad de geolocalización (R-017), la incorporación de conductores rotativos por los transportistas (R-018), la rotación y el aprendizaje en bodega nocturna (R-019), la capacitación y la pérdida del conocimiento de rutas (R-021). En esta rama también se ubican el seguimiento de stock posentrega de INN-01 (R-036) y la comprensión y privacidad de la hoja del almacenero de INN-05 (R-040). Así, la EDR distingue las dependencias humanas de las condiciones técnicas y operativas que pueden afectar el mismo proceso.

**Contrato y licitación** concentra la aceptación y marcha blanca (R-026), los cambios de alcance, los incentivos de costo de servir de INN-04 y la transferencia y salida. **Regulatorio y externo** cubre la evidencia verificable del POD y la guía (R-029), junto con los cambios de retención o normativa aplicable (R-042). **Empresa proveedora** reúne la suficiencia de dotación compartida entre etapas (R-025), la capacidad de mesa, NOC y soporte de sitio (R-034), y la estimación de costos variables y caja del proveedor (R-035).

Los temas de riesgo señalados en el Caso 02 (Distribuidora Puelche S.A., 2026c, Cap. 19) se pueden recorrer con estos códigos: interfaces del ERP (R-001), enlaces de Concepción (R-006), objeción sindical (R-017), conductores de terceros (R-018), rotación en bodega (R-019), conocimiento de rutas (R-021) y capacidad ante el despacho crítico o el peak (R-013). Su distribución entre ramas permite reconocer las distintas fuentes de riesgo sin reunirlas artificialmente bajo una sola fase del proyecto.

Los análisis de **solución**, **desarrollo** e **implantación** exigidos por el Formulario T-22 se mantienen como perspectivas de evaluación, no como ramas de esta EDR. Solución examina el comportamiento, la integridad y la continuidad durante el uso; Desarrollo, la construcción, integración y certificación de los productos; e Implantación, la habilitación, aceptación y adopción del servicio en el CLIENTE. Un mismo riesgo puede afectar más de una perspectiva: la certificación EDI (R-030), por ejemplo, condiciona tanto el desarrollo de la integración como su habilitación. El análisis transversal conserva el ID sin duplicar riesgos.

La figura presenta la clasificación del registro actualizado de 45 riesgos, utilizada también en el Formulario T-16. Los análisis y anexos que conservan la codificación anterior R8 corresponden a una versión previa del registro; sus valoraciones y resultados no se atribuyen automáticamente a los códigos R-001 a R-045. La EDR permite localizar las fuentes de riesgo, mientras que el registro detalla sus causas, consecuencias, responsables y respuestas.

### Análisis cualitativo de riesgos

El análisis cualitativo del T-16 presenta los niveles ordinales de probabilidad e impacto en una escala de 1 a 5 junto con sus ponderaciones decimales. La exposición corresponde al producto decimal ($q_P\times q_I$), y la zona de cada riesgo es la registrada y adoptada del registro vigente, sin inferirla mediante umbrales sobre ese producto. La Tabla 8.4 presenta los diez riesgos con mayor exposición decimal, ordenados de mayor a menor producto y, en caso de empate, por ID ascendente.

**Tabla 8.4. Valoración cualitativa vigente de 10 riesgos más altos.** Fuente: T-16; zonas registradas.

| ID | P decimal | I decimal | Exposición decimal ($q_P\times q_I$) | Zona registrada |
|---|---:|---:|---:|---|
| R-012 | 0,50 | 0,80 | 0,40 | Crítica |
| R-015 | 0,50 | 0,80 | 0,40 | Crítica |
| R-005 | 0,30 | 0,80 | 0,24 | Alta |
| R-006 | 0,30 | 0,80 | 0,24 | Alta |
| R-011 | 0,30 | 0,80 | 0,24 | Alta |
| R-013 | 0,30 | 0,80 | 0,24 | Alta |
| R-014 | 0,30 | 0,80 | 0,24 | Alta |
| R-016 | 0,30 | 0,80 | 0,24 | Alta |
| R-001 | 0,50 | 0,40 | 0,20 | Alta |
| R-003 | 0,50 | 0,40 | 0,20 | Alta |

Entre los diez seleccionados, R-012 y R-015 tienen exposición decimal 0,40 y zona Crítica; les siguen seis riesgos con 0,24 y zona Alta. El corte en 0,20 deja varios riesgos empatados; para mantener exactamente diez filas se incluyen R-001 y R-003, los primeros por ID ascendente. La exposición ponderada no equivale al impacto estimado en horas-hombre.

### Análisis cuantitativo

El valor esperado cuantifica el esfuerzo condicional de cada riesgo ponderado por su probabilidad inicial estimada $p_0$. Para el riesgo $i$, se calcula como $VE_i=p_{0,i}\times H_i^{\mathrm{cond}}$, donde $p_{0,i}$ se expresa entre 0 y 1 y $H_i^{\mathrm{cond}}$ es el impacto de esfuerzo si el evento ocurre, medido en horas-hombre (HH).

La suma de los valores esperados de los 45 riesgos es **2.058,480 HH**. Por decisión adoptada, este total se utiliza como estimación de contingencia en HH calculada por $p_0\times HH$; no es dinero, esfuerzo cierto ni resultado de Monte Carlo. El detalle se presenta en el Anexo 8.B; son estimaciones de planificación pendientes de validación por los responsables.

$p_0$ cuantitativa se mantiene distinta de la exposición cualitativa $q_P\times q_I$, que se calcula por separado junto con los niveles ordinales y la zona registrada. No se presentan simulaciones, percentiles ni probabilidades de cumplimiento.

La Tabla 8.5 ordena los diez mayores valores esperados $VE=p_0\times HH^{\mathrm{cond}}$, no los riesgos por su exposición cualitativa $q_P\times q_I$. Los eventos y consecuencias se resumen estrictamente desde el T-16.

**Tabla 8.5. Diez mayores valores esperados de esfuerzo.** Fuente: T-16; cálculo sobre las estimaciones de planificación del Anexo 8.B.

| ID | Evento / consecuencia (resumen T-16) | $p_0$ | HH condicional | VE (HH) |
|---|---|---:|---:|---:|
| R-030 | Certificación de cadena no disponible a tiempo; integración no habilitada y pérdida de capacidad comercial | 50% | 232 | 116,000 |
| R-004 | Saneamiento de lotes excede lo previsto o carga datos inconsistentes; rechazo de migración y pérdida de trazabilidad | 45% | 224 | 100,800 |
| R-003 | Corte deja saldos divergentes o tareas sin dueño; reversión y convivencia extendida | 40% | 201,6 | 80,640 |
| R-026 | Observaciones, capacitación o indicadores abiertos al cierre; extensión a cargo de LafroX sin mover fases | 40% | 201,6 | 80,640 |
| R-012 | Cadena de custodia incompleta en sitio o retorno; identificación tardía de clientes y lote afectado | 35% | 201,6 | 70,560 |
| R-015 | Restauración o promoción pierde datos o supera límites; interrupción prolongada y conciliación extraordinaria | 35% | 201,6 | 70,560 |
| R-001 | Interfaz disponible no soporta contratos necesarios; retrabajo de ACL y atraso de integración | 45% | 152 | 68,400 |
| R-021 | Retiro antes de transferir y validar excepciones; rutas inseguras o promesas incumplidas | 45% | 152 | 68,400 |
| R-038 | Estimación inválida o excede uso permitido; decisión de disposición errónea | 45% | 152 | 68,400 |
| R-018 | Acuerdo o enrolamiento no cubre reemplazos de conductores; entregas sin evidencia y trabajo paralelo en papel | 45% | 150,4 | 67,680 |

Estos diez valores suman 792,080 HH, aproximadamente el 38,5% del total de 2.058,480 HH. Agrupan dependencias de integración y migración, transición y aceptación, trazabilidad y recuperación, además de continuidad del conocimiento y enrolamiento de conductores; esta agrupación describe temas, no eficacia de controles. Los $p_0$ son estimaciones de planificación y el VE representa esfuerzo esperado, no un resultado real ni de Monte Carlo. La tabla no determina zonas críticas cualitativas ni modifica las reservas ya establecidas.

## Plan de Acción a Riesgos

Esta sección fija las respuestas a los riesgos analizados, las reservas que las financian en horas y las condiciones que deben cumplirse antes de declarar factible la propuesta.

### Respuestas y costo-beneficio técnico

Las fichas del Anexo 8.A documentan los datos de respuesta respaldados por el registro vigente e identifican los campos aún pendientes de definición por responsable. Los objetivos residuales son condicionados y no se consideran eficaces ni disponibles para reducir la contingencia adoptada de 2.058,480 HH; la subcontratación no traslada la obligación final de LafroX.

La evaluación de alternativas de respuesta debe considerar su esfuerzo y evitar doble conteo cuando un control atiende varios riesgos. La cuantificación actual no permite atribuir paquetes de respuesta o costos agregados a los códigos vigentes sin un crosswalk verificable. Se descarta toda alternativa que incumpla sanidad, despacho, integridad de datos o una función obligatoria.

CAL comprueba resultados y JP solicita cambios con evidencia, remanente y ventana de uso. La eficacia de respuestas debe validarse antes de modificar probabilidades o liberar contingencia.

### Reservas y cronograma

La reserva de contingencia adoptada para los riesgos identificados es **2.058,480 HH**, la suma de $p_0\times HH$ condicional del registro vigente de 45 riesgos. Es una estimación de esfuerzo, no una asignación por mes, perfil o paquete. No existe crosswalk verificable entre los códigos R8 de los análisis anteriores y el registro vigente; por ello no se atribuyen concentraciones, actividades ni capacidad a riesgos individuales. Las asignaciones mensuales y por perfil, y su encaje con la dotación del T-15, quedan pendientes de evidencia y planificación actualizadas.

El T-15 deberá reflejar la capacidad cuando se disponga de una asignación sustentada. Con los antecedentes disponibles no puede afirmarse que toda la contingencia cabe en la dotación declarada ni que se requiera una capacidad adicional específica.

**Tabla 8.5 (numeración tal como figura en la fuente). Reservas de esfuerzo, HH.** Fuente: estimación adoptada y supuesto de gestión existente.

| Concepto | HH |
|---|---:|
| Contingencia adoptada ($p_0\times HH$) | 2.058,480 |
| Gestión (supuesto independiente existente) | 1.600 |

La reserva de gestión de 1.600 HH es un supuesto existente, independiente de la contingencia y no derivado del registro cuantitativo. Su fundamento y validación se mantienen separados; no forma parte de las 2.058,480 HH de contingencia. Para cada cargo futuro se deberá identificar evento, paquete, etapa, perfil, período, HH y evidencia, evitando doble consumo.

La reserva de gestión existente es de **1.600 HH**; se conserva como supuesto independiente, fuera de la línea base y separada de la contingencia. No se deriva del registro $p_0\times$HH ni forma parte de las 2.058,480 HH. Su fundamento y validación son independientes y deben mantenerse documentados. La autoriza el Comité Ejecutivo y obliga a actualizar la línea base; un riesgo identificado nunca se carga a esta reserva.

La reserva de cronograma son los días hábiles entre la entrega programada de cada hito y su fecha límite, de 4 a 35 (T-15, Tabla 5.2). Las cuatro semanas finales de cada marcha blanca son evidencia obligatoria y no aportan reserva. La valorización y el flujo monetario de las reservas corresponden a la Oferta Económica (BA Art. 50.2).

### Factibilidad y aceptación

El Anexo 8.E registra las condiciones de evidencia: productividad/dotación, secuencias diarias y plazos de revisión/subsanación del Art. 18.3, fecha contractual, continuidad de 96 despachos, RPO remoto, atención y evidencia láctea. La coordinación de reserva y retención de INT-03/04 (SD4, apartado 4.1.4.4 y Anexo 4-G) está dimensionada en el Anexo 4-I, Tabla A.10, y el Anexo 4-W, Tablas A.32 y A.33, con un máximo de cuatro mensajes por línea. La retención consumida no se libera y esa holgura cubre líneas repartidas entre lotes o sitios. AL-STOCK-01 mide la proporción de líneas con más de una retención antes del H4. Las pruebas 3.8.4 y 3.9.3 verifican la carga y el drenaje, sin sumar la coordinación al drenaje tras un corte. El compromiso RPO $\leq15$ min del SD4, sección 4.2.5.1, se verifica por escenario sobre fibra, LTE y Starlink. La falla simultánea de los tres caminos seguida de la destrucción del sitio antes de reponer alguno es el riesgo residual declarado en SD4 4.3.2.4 (RT-02.11). Los controles de replicación, reposición de enlaces, preemisión de guías y conservación local deben verificarse con evidencia y responsables en el registro vigente. AL-DR-01 mide RPO/RTO antes de H5/H10. Si el NAS se destruye con el sitio, sólo queda la última copia remota consistente: las medidas locales no demuestran por sí solas una pérdida de datos de 15 minutos o menos. Por eso E8-05 exige demostrar en AL-DR-01 qué copia remota sobrevive y en qué frontera se cumple el RPO de 15 minutos (RT-07.04), junto con el tratamiento del riesgo residual (RT-02.11).

El retiro sanitario debe identificar a los clientes afectados con evidencia en menos de dos horas; los 85 minutos de diseño del SD5 no constituyen un ensayo aprobado. E8-13 y E8-14 establecen las condiciones de calendario y capacidad. No se autoriza corte sin continuidad medida ni aceptación sin las seis condiciones simultáneas del Art. 17.3 y acta según Art. 18. La suspensión del proveedor de lácteos, de marzo a septiembre de 2026, es antecedente ocurrido. La consulta V-13 del SD3 (Anexo 3.H) precisa en el mes 1, con el CLIENTE y el proveedor, qué evidencia de trazabilidad restablece la relación, y la Etapa 1 prioriza esa trazabilidad; la restitución depende del proveedor. La propuesta queda sujeta a las condiciones de cierre del Anexo 8.E, cada una con responsable, hito límite y evidencia; ninguna se da por cumplida sin las decisiones, pruebas y actas que allí se indican.

## Referencias

Las fuentes citadas en este documento se listan en formato APA 7.ª edición. Las Bases se citan en el texto con su documento y el artículo, capítulo, sección o código del requisito.

- Distribuidora Puelche S.A. (2026a). *Bases Administrativas de Licitación N.º TFEP-01/2026: Contratación de Solución Integral de Software y Servicios de Operación*.
- Distribuidora Puelche S.A. (2026b). *Bases Técnicas Transversales de Licitación N.º TFEP-01/2026*.
- Distribuidora Puelche S.A. (2026c). *Caso Logística. Especificaciones del problema y operación de Distribuidora Puelche S.A.*
- Distribuidora Puelche S.A. (2026d). *Aclaraciones de la Licitación N.º TFEP-01/2026*.
- LafroX. (2026). Subdocumentos 1 a 9 y 13, con los anexos y formularios citados, incluidos los Formularios T-13 y T-17.
- International Electrotechnical Commission. (2018). *IEC 60812:2018 Failure modes and effects analysis (FMEA and FMECA)*. IEC.
- International Organization for Standardization. (2018). *ISO 31000:2018 Risk management — Guidelines*. ISO.
- Project Management Institute. (2017). *La guía de los fundamentos para la dirección de proyectos (Guía del PMBOK®)* (6.ª ed.), capítulo 11. Project Management Institute.

## Declaración de uso de IA

La tabla declara apoyo de IA conforme a las Aclaraciones §7.2. La revisión humana identifica quién efectivamente verificó cada parte y se consolida en el Formulario A-6.

**Tabla 8.IA.1. Declaración de uso de IA.**

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
|---|---|---|---|---|---|
| Introducción | Gentle-Shell mas ChatGpt | Conexión con operación, alcance y formularios | Alto | Ninguno | Maximiliano Miño: Lectura preliminar de introducción entregada. En caso de encontrar inconsistencias, arreglarlo |
| 8.1 Plan de riesgos | Gentle-Shell mas ChatGpt | Roles, escalas, ciclo y cierre | Alto | Ninguno | Maximiliano Miño: Lectura de contenido plasmado en documento, validación de contenido mediande consistencia entre otros documentos y visita a contenido academico |
| 8.2 Identificación y Análisis de Riesgos | Gentle-Shell mas ChatGpt | RBS, exposición cualitativa y valor esperado en HH | Alto | Medio | Maximiliano Miño: Se hace revisión de los riesgos antes de hacer RBS, luego de validación se revisa RBS, basado en riesgos se realiza análisis asistido por IA |
| 8.3 Plan de Acción a Riesgos | Gentle-Shell mas ChatGpt | Respuestas, contingencia y gestión | Alto | Ninguno | Maximiliano Miño: Se hace lectura de lo entregado, se valida con las tablas de anexos y formularios necesarios |
| Anexo 8.A | Gentle-Shell mas ChatGpt | Proponer respuestas y estrategias para los riesgos, junto con un responsable para cada uno | Alto | Ninguno | Maximiliano Miño:Análisis exahutivo de los riesgos, enfocandonos principalmente en en los puntos de Disparador hasta Costo |
| Anexo 8.B | Gentle-Shell mas ChatGpt | Proponer y validar los cálculos relacionados con la estimación de tres valores | Alto | Ninguno | Maximiliano Miño: Se realiza validación con tabla de formulario T-16 |
| Formulario T-16 | Gentle-Shell mas ChatGpt | Mejorar la redacción de las descripciones de riesgos y proponer valores de probabilidad e impacto, y estrategias o respuestas | Alto | Ninguno | Maximiliano Miño: Revisión de los riesgos, cercionandose de que este relacionado con el caso |
