# LafroX — Subdocumento 8: Plan de riesgos

# Introducción a los Riesgos

La solución de LafroX integra recepción y trazabilidad, inventario, frío, preventa, reparto y cobranza en E1, y canal moderno, portales y costo de servir en E2. Sus riesgos dependen de una operación que despacha 96 camiones entre 05:30 y 07:00, mantiene los CD 24 horas sin WAN y el terreno 14 horas sin señal, conserva ERP como único emisor tributario y despliega sin detener rutas. Este plan conecta las decisiones comerciales del SD2, alcance del SD3, contratos y dimensionamiento del SD4, gobierno del SD6 y programación del SD7.

El cuerpo establece método y decisiones; los Anexos 8.A–8.F contienen registro ampliado, FMEA, escenarios, reservas y condiciones de evidencia; el T-16 conserva el formato obligatorio separado. Las condiciones que deben cerrarse antes de cada hito, incluida la brecha residual de RPO declarada en el SD4 (sección 4.3.2.4), se registran en el Anexo 8.E con responsable y plazo.

## 8.1 Plan de riesgos

Esta sección define cómo se gestionan los riesgos durante los 56 meses: el ciclo y sus instancias, los roles y su autoridad, las escalas con que se analizan y las reglas de registro y cierre.

### 8.1.1 Enfoque y ciclo

El registro vivo sigue identificación, análisis, respuesta y seguimiento conforme a la norma ISO 31000 (International Organization for Standardization [ISO], 2018), que exige el RT-19.04 de las Bases Técnicas Transversales (Distribuidora Puelche S.A., 2026b). Cada entrada distingue causa, evento incierto y consecuencia, sin convertir una inconsistencia observada en riesgo futuro. El Anexo 8.E separa problemas y dependencias actuales.

JP mantiene el registro único. Los líderes identifican riesgos al revisar interfaces, pruebas, capacidad y despliegues; verifican disparadores semanalmente y ante cada cambio. El Comité de Proyecto quincenal revisa todos los riesgos abiertos, responsables, plazos y evidencia. Los comités Ejecutivo y de Arquitectura mensuales deciden escalamiento y cambios de sus ámbitos, y desde el mes 13 el Comité de Operación mensual revisa los riesgos de servicio: niveles de atención, incidentes, capacidad y continuidad (SD6, sección 6.1.6). Una amenaza a continuidad, seguridad o hito se escala inmediatamente. Marcha blanca exige seguimiento diario; operación mantiene vigilancia diaria de incidentes y colas y revisión en comités.

### 8.1.2 Roles y autoridad

La Tabla 8.1 asigna a cada líder del proyecto el ámbito de riesgos que vigila en el registro.

**Tabla 8.1. Ámbito de riesgos por rol — Fuente: elaboración propia a partir del Capítulo 1, Tabla 1.3, y del Formulario T-16**

| Rol | Ámbito de riesgos que vigila |
| --- | --- |
| JP — Alex Aravena | Registro, fechas, contraparte, recursos y escalamiento |
| ARQ — Bastián Trejo | Interfaces, portabilidad, continuidad y resolución propuesta de RPO residual |
| SEG — Álvaro Catalán | Seguridad, acceso, datos y respuesta a incidentes |
| DAT — Leandro Chamorro | Migración, conciliación, trazabilidad y modelos |
| DES — Tomás Pérez | Módulos, integración, idempotencia y equipos separados E1/E2 |
| CAL — Maximiliano Miño | Pruebas, criterios y evidencia de cierre |
| SRE — Guillermo Castillo | Capacidad, infraestructura, enlaces, continuidad y atención |
| IMP — Patricio Henríquez | Olas, usuarios, formación, acuerdos y adopción |

Dirigen equipos; no ejecutan solos todas las HH. La Contraparte Técnica del CLIENTE acepta entregables mediante actas; Operaciones autoriza cortes y continuidad de su ámbito; Calidad del CLIENTE valida decisiones sanitarias. No se presume disponibilidad ni aprobación de esas contrapartes. Los cambios físicos siguen el gobierno de arquitectura, sin modificar silenciosamente SD4/T-11.

### 8.1.3 Escalas previas al análisis

P/I/D se asignan como juicios ordinales iniciales sustentados en exposición y controles descritos, no como frecuencias medidas; para el análisis cuantitativo, P e I se calibran con los tramos de la segunda tabla de esta sección. Horizonte: hasta entregar el control de cada ficha y, para riesgos recurrentes, los 56 meses del contrato. Cambiar el horizonte exige reevaluación.

**Tabla 8.2. Escalas ordinales de probabilidad, impacto y detección — Fuente: elaboración propia a partir de ISO (2018) e IEC (2018)**

| Valor | Probabilidad ordinal P | Impacto I: mayor efecto aplicable | Detección D: mayor valor, peor detección |
| --- | --- | --- | --- |
| 1 | Excepcional, sin dependencia expuesta identificada | Corrección local sin afectar aceptación ni servicio | Control automático probado detecta antes de confirmar |
| 2 | Posible con exposición limitada | Retrabajo absorbible en capacidad asignada | Ensayo sistemático detecta antes de habilitar |
| 3 | Plausible por una dependencia expuesta | Consume contingencia o afecta servicio auxiliar | Requiere conciliación o ensayo específico |
| 4 | Exposición recurrente o varias dependencias sin control demostrado | Amenaza hito, SLA o alcance obligatorio | Se aprecia al afectar operación o en revisión tardía |
| 5 | Condiciones muy favorables al evento sin barrera eficaz | Detiene despacho crítico, compromete seguridad/datos/sanidad o impide aceptación | Sin evidencia de detección o reconocible después de pérdida |

Exposición E = P × I (1–25): baja 1–3, moderada 4–7, alta 8–14 y crítica 15–25. FMEA agrega NPR = P × I × D (1–125), para ordenar dentro del nivel; desempates por impacto y proximidad del plazo. I = 5 exige escalamiento aunque E no alcance 15. No se asigna D = 1 a un control por describirlo.

Para el análisis cuantitativo, cada valor de P se calibra con un tramo de probabilidad y cada valor de I con la fracción del esfuerzo de los paquetes afectados que el evento agregaría como retrabajo o trabajo adicional. Los paquetes afectados son los que cada ficha del Anexo 8.A nombra en «Fuente y EDT», con sus HH del Formulario T-15. La calibración es un juicio del equipo, no una frecuencia medida, y se revisa con los datos del proyecto.

**Tabla 8.3. Calibración cuantitativa de las escalas — Fuente: elaboración propia a partir del Formulario T-15**

| Valor | Probabilidad (tramo y valor usado) | Impacto (fracción del esfuerzo afectado) |
| --- | --- | --- |
| 1 | Menos de 10 %; 5 % | Sin esfuerzo adicional |
| 2 | 10 a 30 %; 20 % | 5 % |
| 3 | 30 a 50 %; 40 % | 10 % |
| 4 | 50 a 70 %; 60 % | 20 % |
| 5 | Más de 70 %; 80 % | 30 % |

El valor esperado de un riesgo es su probabilidad por su impacto en HH. Las horas sirven de unidad porque la oferta técnica no contiene montos (BA Art. 50.2); la Oferta Económica valoriza esas horas.

### 8.1.4 Registro y cierre

El responsable actualiza fuente, estado, disparador, tratamiento, consumo de HH y evidencia. Estados: identificado, en tratamiento, control verificado o materializado. Materializar el evento abre un problema y conserva su ID. CAL verifica cierre técnico; JP registra la decisión; la aceptación contractual corresponde al CLIENTE. La puntuación residual se estima después de comprobar controles, no por asignar una mitigación. Ninguna aceptación de riesgo exime requisitos obligatorios.

## 8.2 Identificación y Análisis de Riesgos

Esta sección identifica los riesgos con una RBS y los analiza en dos niveles: uno cualitativo con FMEA y otro cuantitativo con el valor esperado de cada riesgo en horas hombre y una simulación de Monte Carlo sobre el cronograma por actividad del SD7.

### 8.2.1 RBS y análisis separados

La estructura de desglose de riesgos (RBS) tiene raíz «Riesgos de la propuesta LafroX» y tres ramas, una por cada análisis que exige el Formulario T-22: riesgo de la solución, del desarrollo y de la implantación. Dentro de cada rama, los riesgos se agrupan en las categorías técnica, organizacional, de proyecto, de seguridad y de operación que les corresponden. Los ID son únicos aunque una causa afecte varias ramas. La Figura 8.1 presenta la estructura con los 32 riesgos del Anexo 8.A.

- Riesgos de la propuesta LafroX (32)
  - Solución (13)
    - Técnico: R8-02, R8-04, R8-06, R8-08, R8-09, R8-27, R8-30
    - Operación: R8-01, R8-03, R8-05, R8-23
    - Seguridad: R8-07, R8-24
  - Desarrollo (10)
    - Proyecto: R8-11, R8-14, R8-15, R8-31
    - Técnico: R8-10, R8-16, R8-26
    - Organizacional: R8-12, R8-13, R8-32
  - Implantación (9)
    - Organizacional: R8-20, R8-21, R8-25, R8-29
    - Proyecto: R8-17, R8-19, R8-28
    - Operación: R8-18, R8-22

**Figura 8.1 — Estructura de desglose de riesgos (RBS). Fuente: elaboración propia a partir del Anexo 8.A.**

La figura muestra que la solución concentra 13 de los 32 riesgos y 11 de los 22 de nivel crítico de la Tabla B.1, porque reúne la continuidad del despacho, la reserva de stock y la evidencia de frío. Los dos riesgos de seguridad (R8-07 y R8-24) pertenecen a la rama de la solución, porque sus fichas los originan en los portales, móviles, integraciones y trazas que la arquitectura expone. El desarrollo se concentra en la categoría de proyecto (dotación, capacidad protegida de la Etapa 1, certificación de cadenas y revisión del CLIENTE), y la implantación, en la organizacional (rotación, transportistas, sindicato y adopción de innovaciones).

Solución: integridad de stock/custodia, ERP/DTE, autonomía, capacidad, RPO, seguridad, obsolescencia y proveedores. Desarrollo: interfaces sin documentación, recursos, contrapartes, conocimiento de rutas, migración, certificación externa, certificación paralela a la revisión del CLIENTE y refuerzo subcontratado de calidad. Implantación: congelamientos, cuatro semanas completas, suministros, adopción, relevos y atención. Anexo 8.A desarrolla 32 amenazas; 8.F cubre las cinco innovaciones y una oportunidad de diagnóstico con INN-02. Las tres ramas permiten preparar los análisis separados exigidos por T-22.

### 8.2.2 Resultados cualitativos y FMEA

El análisis de modos de falla y sus efectos (FMEA) sigue la IEC 60812 (International Electrotechnical Commission [IEC], 2018): a la probabilidad y el impacto agrega la detección, y su producto da el número de prioridad del riesgo (NPR). Anexo 8.B presenta P/I/D, exposición y NPR. La prioridad inicial se concentra en continuidad, RPO, ERP/DTE, seguridad, capacidad y aceptación. T-16 compara exposición; NPR no reemplaza su columna Expos.

La Tabla 8.4 extrae del Anexo 8.B, Tabla B.1, los cinco riesgos con mayor número de prioridad (NPR); el registro completo de los 32 está en ese anexo.

**Tabla 8.4. Riesgos con mayor NPR — Fuente: Anexo 8.B, Tabla B.1**

| Riesgo | P | I | D | NPR = P × I × D |
| --- | --- | --- | --- | --- |
| R8-01 ERP indisponible o guía invalidada | 4 | 5 | 4 | 80 |
| R8-07 Ataque o exposición de datos críticos | 4 | 5 | 4 | 80 |
| R8-27 INN-03 estima vida remanente insegura | 4 | 5 | 4 | 80 |
| R8-05 Pérdida del sitio supera RPO | 3 | 5 | 5 | 75 |
| R8-02 Doble reserva o custodia CD-05 | 4 | 5 | 3 | 60 |

Los cinco pertenecen a la rama de la solución y todos tienen impacto 5. Lo que los separa es la detección: R8-05 tiene la probabilidad más baja, pero su D = 5 (sólo se aprecia al perder el sitio) lo deja en el cuarto lugar, por sobre riesgos más probables. Por eso sus respuestas privilegian controles que se prueban antes del corte (ensayo de caída del ERP, prueba de concurrencia y ejercicio de recuperación) en vez de controles que sólo reaccionan cuando el evento ocurre.

No se suman puntuaciones como probabilidad del proyecto. Las relaciones importan: ausencia de contraparte puede atrasar interfaces/cadenas y eliminar semanas de evidencia; migración deficiente puede invalidar trazabilidad y aceptación. Los mismos efectos o consumos no se contabilizan dos veces.

### 8.2.3 Análisis cuantitativo

El análisis cuantitativo tiene dos partes (PMI, 2017, pp. 433–434). La primera calcula el valor esperado de cada riesgo con la calibración de la sección 8.1.3. El registro suma 15.076 HH de valor esperado, cerca de 8 % de las 190.366 HH base del T-15. Cinco riesgos concentran 67,7 % del total: productividad o dotación inferior al modelo (R8-11), mesa que no alcanza los niveles de atención (R8-22), marcha blanca que no cumple las seis condiciones (R8-18), uso de la capacidad protegida de la Etapa 1 por la Etapa 2 (R8-14) y doble reserva de stock (R8-02). El Anexo 8.B, Tabla B.2, presenta el cálculo de cada riesgo y su porcentaje acumulado.

La segunda parte simula 5.000 veces el cronograma por actividad del Formulario T-15. En cada iteración, la duración de cada paquete varía con la distribución PERT de su tríada, cada riesgo ocurre con su probabilidad y, si ocurre, alarga sus paquetes afectados en la fracción de su impacto. La tabla informa, para cada hito, la fecha límite de entrega, las fechas que se alcanzan en la mitad (P50) y en el 80 % (P80) de las iteraciones y la probabilidad de entregar a tiempo. Los hitos H6, H7, H11 y H12 no se simulan: son el inicio de cada marcha blanca y cada paso a producción, con mes fijo del Art. 17°, y su riesgo se trata con R8-18 y la reserva de contingencia (Anexo 8.C, sección C.3).

**Tabla 8.5. Resultado de la simulación de Monte Carlo por hito — Fuente: elaboración propia a partir del Formulario T-15 y del Anexo 8.C**

| Hito | Fecha límite de entrega | P50 | P80 | P(entrega a tiempo) |
| --- | --- | --- | --- | --- |
| H1 | 17-03-2027 | 09-03-2027 | 10-03-2027 | > 99,9 % |
| H2 | 17-05-2027 | 06-04-2027 | 09-04-2027 | > 99,9 % |
| H3 | 16-07-2027 | 30-06-2027 | 09-07-2027 | 98,6 % |
| H4 | 16-11-2027 | 28-10-2027 | 03-11-2027 | > 99,9 % |
| H5 | 17-01-2028 | 27-12-2027 | 05-01-2028 | 97,7 % |
| H8 | 17-03-2028 | 06-03-2028 | 09-03-2028 | 99,3 % |
| H9 | 16-06-2028 | 06-06-2028 | 14-06-2028 | 89,9 % |
| H10 | 17-07-2028 | 30-06-2028 | 07-07-2028 | 97,7 % |

La fecha P80 de cada hito queda antes de su fecha límite: el plan se compromete al percentil 80 y se ejecuta sobre las fechas programadas, que están cerca del P50. Para lograrlo, el SD7 dimensionó las reservas de cada hito con esta simulación, adelantó la sala técnica, los ambientes y la integración de la Etapa 2, y refuerza la calidad con evaluadores subcontratados durante las certificaciones. El H9 es el hito más expuesto (90 %), y su probabilidad depende sobre todo de R8-14, R8-11 y R8-15 (Anexo 8.C, Tabla C.4).

T-15 programa 202.774 HH, con soporte puente de 9.336 HH y reserva E1 de 3.072 HH ya incluidos; la mesa y el SOC siguen las posiciones del SD4 y el calendario real. El máximo mensual es 69 personas equivalentes en el mes 15, y la construcción de la Etapa 1 ocupa a 48 personas de desarrollo a la vez; no demuestra contratación ni cobertura por subventana, y la dotación declarada en el SD1 no cubre SEG ni IMP sin contratación o subcontratación (T-15 §5.7). Horas de atención tampoco prueban SLA.

## 8.3 Plan de Acción a Riesgos

Esta sección fija las respuestas a los riesgos analizados, las reservas que las financian en horas y las condiciones que deben cumplirse antes de declarar factible la propuesta.

### 8.3.1 Respuestas y costo-beneficio técnico

Cada ficha 8.A fija responsable, disparador, plazo, mitigación, contingencia y evidencia. Evitar se aplica a cortes inseguros, facturación diferente del pedido y liberación sanitaria sin evidencia; reducir, a controles y pruebas; compartir responsabilidades, a acuerdos externos. Contratar un tercero no transfiere la obligación final de LafroX. La atención auxiliar en contingencia no acredita capacidades obligatorias desactivadas.

El costo-beneficio compara HH de prevención/verificación con retrabajo y afectación de servicio/hitos, según 8.C. Los 160/320 HH derivan de clases del T-15; son referencias supuestas, no ensayos ejecutados ni ampliaciones aprobadas. El cumplimiento obligatorio prevalece sobre el cociente de ahorro. Valorización, tarifas y reservas monetarias corresponden exclusivamente a la Oferta Económica (BA Art. 50.2).

### 8.3.2 Reservas y cronograma

La reserva de contingencia cubre los riesgos identificados y se dimensiona con la suma de sus valores esperados: 15.076 HH (PMI, 2017, p. 202; p. 443). De ellas, 1.853 HH corresponden a R8-02, R8-04 y R8-14 (461 + 384 + 1.008 HH, Tabla B.2), los riesgos de corrección de la Etapa 1 que la capacidad protegida de 3.072 HH de los meses 13 a 20, ya incluida en el T-15, puede absorber según la regla del Anexo 8.D. Esa capacidad no puede usarse antes del mes 13 ni para la Etapa 2, de modo que no cubre a los demás riesgos, y la contingencia adicional es de 15.076 − 1.853 = 13.223 HH. La tabla reparte la contingencia por período según los meses de los paquetes afectados por cada riesgo; ese reparto es el reflejo de la reserva en el flujo de caja, y su valorización está en la Oferta Económica (Art. 50.2).

**Tabla 8.6. Reparto de la reserva de contingencia por período — Fuente: elaboración propia a partir del Anexo 8.B, Tabla B.2**

| Período | Contingencia (HH) |
| --- | --- |
| Meses 1–6 | 1.802 |
| Meses 7–12 | 4.090 |
| Meses 13–15 | 2.359 |
| Meses 16–21 | 3.287 |
| Meses 22–33 | 3.486 |
| Meses 34–56 | 51 |
| **Total** | **15.076** |

Los valores de cada período se redondean a la hora; el total se calcula sin redondear. El 88 % de la reserva (13.222 de 15.076 HH) se concentra entre los meses 7 y 33, donde coinciden la construcción, las dos marchas blancas y el primer año de operación; después del mes 33 queda sólo el remanente de los riesgos de operación (51 HH).

La reserva de cronograma son las reservas de cada hito del T-15, Tabla 5.2, dimensionadas para que la fecha P80 quede antes de la fecha límite (sección 8.2.3). La reserva de gestión cubre riesgos no identificados: no forma parte de la línea base, la autoriza el Comité Ejecutivo y su monto se define en la Oferta Económica (BA Art. 50.2). JP solicita el uso de cualquier reserva con causa, perfiles, ventana e impacto; ninguna reserva se presta entre etapas.

Cada uso registra un cargo único por evento/mes/perfil y remanente. Riesgos correlacionados comparten consumo real; E1 no presta su reserva a E2. Los recursos adicionales requieren actualizar T-15 y calendario, sin ampliar automáticamente los 56 meses. Los meses 21 y 22 separan 2.774,54 HH de cierre y estabilización de implementación de la operación.

### 8.3.3 Factibilidad y aceptación

El Anexo 8.E registra las condiciones de evidencia: productividad/dotación, secuencias diarias y plazos de revisión/subsanación del Art.18.3, fecha contractual, continuidad de 96 despachos, RPO remoto, atención y evidencia láctea. El dimensionamiento físico del Capítulo 4 (A31 y A32) ya incluye la coordinación CD-05; su multiplicidad y su drenaje se verifican en la prueba de concurrencia previa al H4. El límite residual RPO requiere resolución, no aceptación como sustituto de cumplimiento.

No se autoriza corte sin continuidad medida ni aceptación sin las seis condiciones simultáneas del Art. 17.3 y acta según Art. 18. La suspensión láctea de septiembre de 2026 es antecedente ocurrido; V-13 debe precisar evidencia y restitución con CLIENTE/proveedor. El proyecto no demuestra una solución retroactiva. La propuesta queda sujeta a las condiciones de cierre del Anexo 8.E, cada una con responsable, hito límite y evidencia; ninguna se da por cumplida sin las decisiones, pruebas y actas que allí se indican.

## Referencias

Las fuentes citadas en este documento se listan a continuación en formato APA 7.ª edición.

- Distribuidora Puelche S.A. (2026a). *Bases Administrativas de Licitación N.º TFEP-01/2026*, artículos 17, 18 y 50.2, y Formularios T-16 y T-22.
- Distribuidora Puelche S.A. (2026b). *Bases Técnicas Transversales de Licitación N.º TFEP-01/2026*, RT-07.04, RT-07.07, RT-19.04, RT-21.06, RT-21.07 y RT-26.04.
- Distribuidora Puelche S.A. (2026c). *Caso 02: Logística*, capítulos 10 a 14 y requisitos específicos citados.
- Distribuidora Puelche S.A. (2026d). *Aclaraciones de la Licitación N.º TFEP-01/2026*, secciones 2, 4, 6, 7 y 11 (Capítulo 8).
- LafroX. (2026). Subdocumentos 1 a 4, 6 y 7, con los anexos y formularios citados.
- International Electrotechnical Commission. (2018). *IEC 60812:2018 Failure modes and effects analysis (FMEA and FMECA)*. IEC.
- International Organization for Standardization. (2018). *ISO 31000:2018 Risk management — Guidelines*. ISO.
- Project Management Institute. (2017). *La guía de los fundamentos para la dirección de proyectos (Guía del PMBOK®)* (6.ª ed.), capítulo 11. Project Management Institute.

## Declaración de uso de IA

En cumplimiento de la sección 7.2 de las Aclaraciones de la licitación, la tabla siguiente declara el uso de herramientas de inteligencia artificial en este subdocumento, con la revisión humana de cada parte. La declaración se consolida en el Formulario A-6.

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
| --- | --- | --- | --- | --- | --- |
| Introducción | Codex | Redacción a partir de SD2–SD4, SD6 y SD7 | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 8.1 Plan de riesgos | Codex; Claude Code | Método, roles y escalas; Comité de Operación y textos de sección | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 8.2 Identificación y Análisis de Riesgos | Codex; Claude Code | RBS textual, FMEA y escenarios; valor esperado en HH y simulación de Monte Carlo sobre el cronograma por actividad | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 8.3 Plan de Acción a Riesgos | Codex; Claude Code | Respuestas, reservas y factibilidad; reserva de contingencia por valor esperado y su reparto por período | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| Anexos 8.A a 8.F | Codex; Claude Code | Ver la declaración de los anexos | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| Formulario T-16 | Codex; Claude Code | Ver la declaración del formulario | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| Introducción, 8.1.1, 8.1.3, 8.2.1–8.2.3, 8.3.2 y 8.3.3: correcciones de coherencia | Claude Code | Figura 8.1 (RBS) desde las fichas 8.A, contingencia adicional elegible, hitos no simulados, citas y referencias | Medio | Medio (descripción textual de la RBS) | [[REVISIÓN HUMANA]] |
