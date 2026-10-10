# Plan — Subdocumento 9 «Plan de calidad» (LafroX) + planilla de cálculos

## Contexto
El SD9 es el único subdocumento técnico que falta. Pesa 8 % en el T-21 y la Comisión dejó escrito que la trazabilidad «se corta en la prueba y la aceptación (S9)». Tiene que cubrir lo que piden las Aclaraciones cap. 9 (9.1, 9.2 y 9.3), BA Art. 24 y T-7, los formularios T-13 y T-17, BTT RT-04, 09, 10, 13 y 20.1, y Caso caps. 14, 15 y 18. Debe calzar con las cifras que ya están en SD1–SD8 y SD13.

Esta tarea entrega tres cosas: (1) el plan del SD9 (estructura, preguntas que responde cada sección y diagramas draw.io), (2) la lista de datos obligatorios y de cálculos, y (3) una planilla Excel con todos los cálculos. **El SD9, los .drawio y los formularios T-13 y T-17 no se redactan en esta tarea.**

Decisiones del usuario:
- **Cobertura**: puerta bloqueante con ≥70 % en la lógica de negocio (RT-04.11) **y** ≥80 % de cobertura unitaria **global**. Se mantiene lo que dicen SD1 y SD6; hay que corregir T-14 (1.5.2, «código modificado») y precisar SD4 L2158.
- **Pentest**: anual y antes de cada paso a producción (RT-11.20, T-14 8.2.2). Hay que corregir SD1 L180 y RNF-14.06 («semestral»).
- **Ubicación**: `LafroX/09_plan_calidad/Diagramas/`, igual que la carta Gantt del SD7.

## Entregables de esta tarea
1. `LafroX/09_plan_calidad/Diagramas/LafroX-Calculos-SD9.xlsx`, construida con openpyxl y fórmulas vivas. Antes de construirla se carga el skill `anthropic-skills:xlsx`.
2. `LafroX/compct/plan_SD9.md`: copia en Markdown de este plan, para que el grupo lo vea dentro del repo.
3. Una nota en `compct/CONTEXTO_SESION.md` (estado vigente), sin commit.

---

## A. Estructura del SD9 y preguntas que responde cada sección
Los títulos son obligatorios y textuales. Se pueden agregar subtítulos de nivel 3.

**Capítulo 9 · Introducción al Plan de calidad.** Texto de introducción. Responde cómo se conecta con SD3 (RNF y T-12), SD4 (umbrales p95, ambientes, pipeline), SD5 (ISO 25012 y migración), SD6 (puertas y DoD), SD7 (paquetes 1.5, 3.8, 3.9 y 8.x; hitos), SD8 (R8-18, 31 y 32), SD13 (INN-02) y con los formularios T-13 y T-17.

**9.1 Plan de Calidad**
- 9.1.1 Marco y gobierno:
  - ¿Qué norma rige cada objeto? ISO/IEC 25010 para el producto, 25012 para los datos, 29119 para las pruebas y PMBOK cap. 8 para el proceso.
  - ¿Quién decide? Líder de Calidad Maximiliano Miño, Comité de Calidad mensual con poder de veto (SD1 L138, L171).
- 9.1.2 Modelo de madurez:
  - ¿Qué nivel se declara y cómo se evidencia? CMMI-DEV N3 (SD1 L198).
  - ⚠ La certificación vence en **nov-2026**: hay que decir cómo se renueva, porque el contrato parte en feb-2027.
  - ¿Qué meta de madurez de pruebas se fija (TMMi) y cómo se mide?
- 9.1.3 Umbrales ISO/IEC 25010 por característica. Son las 8 del Art. 24: funcionalidad, desempeño, compatibilidad, usabilidad, fiabilidad, seguridad, mantenibilidad y portabilidad.
  - ¿Qué métrica, umbral, fuente y método de verificación tiene cada una? Los valores salen de SD4 Tabla 31, SD3 Tabla 3.5 y RNF.
- 9.1.4 Métricas de código con umbral bloqueante:
  - cobertura 70 % de negocio y 80 % global;
  - complejidad ciclomática y cognitiva;
  - acoplamiento entre los 12 módulos (deptrac, coherente con RT-02.02);
  - duplicación y deuda técnica (ratio).
  - ¿Con qué herramienta se mide en PHP, Kotlin y Angular?
- 9.1.5 Métricas de proceso y producto: densidad de defectos, eficiencia de remoción (DRE), escape a producción, las 4 métricas DORA (SD4 L2254) y el presupuesto de error de 43 min al mes.

**9.2 Estrategia de Aseguramiento de Calidad**
- 9.2.1 Puertas de calidad G0–G6 (commit → MR → CI → QA → PREPROD → PROD → operación):
  - ¿Qué bloquea cada puerta?
  - ¿Cómo calzan con las 5 puertas del SD6 L201–207?
- 9.2.2 Revisión por pares y análisis estático y dinámico:
  - reglas de MR;
  - SAST, SCA y escaneo de secretos e imágenes (RT-04.05);
  - DAST con herramienta nombrada (hoy no tiene ninguna);
  - PHPStan, Larastan y Pint;
  - detekt y ktlint (Kotlin);
  - ESLint (Angular).
- 9.2.3 Estrategia de pruebas según ISO/IEC/IEEE 29119:
  - niveles: unitaria, componente, integración/contrato, sistema/regresión, aceptación;
  - tipos: carga y estrés, resiliencia, DR, seguridad ofensiva, accesibilidad, usabilidad, migración, y las propias del caso (14 h sin señal, 24 h de corte del CD, −22 °C, ventana 05:30–07:00, sincronización ≤10 min);
  - en qué ambientes (DEV, QA, PREPROD, PROD, DR);
  - con qué datos: sintéticos y anonimizados según la Ley 21.719, verificados con Macie;
  - con qué automatización.
  - Llenar los vacíos de herramientas:
    - JUnit 5, Espresso y Kover/JaCoCo (Kotlin);
    - k6 (carga);
    - OWASP ZAP (DAST);
    - axe-core más pruebas manuales (WCAG 2.2 AA);
    - AWS FIS (inyección de fallas).
- 9.2.4 Verificación, validación y trazabilidad:
  - cadena requisito → componente → paquete EDT → caso de prueba → despliegue → criterio de aceptación (Caso 17.1);
  - cómo se recorre desde el T-12 (645 IDs) y RT-04.04;
  - gestión de defectos y severidades.

**9.3 Alineación con Plan de Trabajo**
- ¿Qué paquetes de la EDT son de calidad, con sus HH y meses? 1.2.4, 1.5.1–1.5.2, 2.6.x, 3.7.x, 3.8.1–3.8.8, 3.9.1–3.9.7, 3.10.2.x, 4.1.2, 7.3, 8.1.3, 8.1.6, 8.2.2 y 8.2.4.
- ¿Qué hito habilita cada prueba (H4, H5, H9, H10) y cómo se absorben los 10+10 días del Art. 18.3 dentro de las reservas del T-15?
- ¿Cómo encajan los congelamientos de septiembre y diciembre, el cierre de mes y la dotación CAL con el refuerzo de evaluadores?

**Anexos y formularios**
- `LAFROX-Subdocumento9-Anexos.md`:
  - 9.A umbrales ISO 25010 completos;
  - 9.B catálogo de reglas de análisis estático;
  - 9.C matriz de trazabilidad prueba ↔ RF/RNF/RT;
  - 9.D especificación de datos de prueba.
- `LAFROX-Formulario-T-13.md`: niveles, tipos, ambientes, datos, criterios de entrada y salida, automatización y calendario de carga, resiliencia, DR y seguridad ofensiva.
- `LAFROX-Formulario-T-17.md`: un protocolo por hito H1–H12 y uno para el producto final, con entregables, criterios objetivos, evidencia (Art. 18.2), plazos de 10+10, procedimiento de observaciones y acta.
- Cierre del cuerpo: Referencias (APA 7) y Declaración de uso de IA, con `[[REVISIÓN HUMANA]]` hasta que firme un integrante.

## B. Diagramas draw.io (`09_plan_calidad/Diagramas/`)
Se planifican aquí y se dibujan en la etapa de redacción. Formato: elaboración propia, texto ≥9 pt; los diagramas complejos llevan una vista general y luego sus partes.

| Fig. | Archivo | Contenido | Sección |
|---|---|---|---|
| 9.1 | Fig_9-1_Marco_Calidad.drawio | Vista general: normas → modelo → métricas → puertas → evidencia → aceptación | 9.1.1 |
| 9.2 | Fig_9-2_Modelo_ISO25010.drawio | Árbol de las 8 características con su métrica y umbral para Puelche | 9.1.3 |
| 9.3 | Fig_9-3_Puertas_Calidad.drawio | Pipeline GitLab CI/CodeBuild con puertas G0–G6 y sus criterios de bloqueo | 9.2.1 |
| 9.4 | Fig_9-4_Niveles_Ambientes.drawio | Matriz de niveles y tipos de prueba 29119 por ambiente DEV/QA/PREPROD/PROD/DR | 9.2.3 |
| 9.5 | Fig_9-5_Datos_Prueba.drawio | Flujo de datos de prueba: generación sintética y anonimización, sin datos productivos fuera de PROD | 9.2.3 |
| 9.6 | Fig_9-6_Modelo_V.drawio | Modelo en V: artefactos de diseño ↔ nivel de prueba ↔ hito E-25 | 9.2.4 |
| 9.7 | Fig_9-7_Cadena_Trazabilidad.drawio | Origen → RF/RNF/RT → M/INT → paquete EDT → caso → despliegue → criterio R18 | 9.2.4 |
| 9.8 | Fig_9-8_Ciclo_Defectos.drawio | Ciclo de vida del defecto con severidades y su relación con la puerta G5 y con la marcha blanca | 9.2.4 |
| 9.9 | Fig_9-9_Calidad_Cronograma.drawio | Línea de 56 meses con paquetes de calidad, H1–H12, congelamientos y pruebas periódicas | 9.3 |
| 9.10 | Fig_9-10_Flujo_Aceptacion.drawio | Flujo del T-17: entrega → 10 días hábiles → observaciones → 10 de subsanación → acta (Art. 18) | 9.3 / T-17 |

## C. Datos que tienen que estar (fuente y valor)
- **Bases**:
  - cobertura ≥70 % de negocio, bloqueante;
  - carga a 1,5× el peak en PREPROD;
  - resiliencia antes de cada paso y semestral;
  - DR 2 veces al año;
  - restauración mensual;
  - pentest anual y antes de cada paso;
  - WCAG 2.2 AA;
  - 2 ensayos de migración;
  - umbrales p95 de BTT 9.1 y Caso 15 RT-09.01 (picking 1 s, entrega 2 s, preventa 1,5 s, stock/crédito 2 s);
  - 99,9 % para servicios críticos;
  - RTO ≤4 h y RPO ≤15 min;
  - E-25 H1–H12 con sus meses;
  - Art. 17.3 (6 condiciones de cierre de marcha blanca);
  - Art. 18.2 y 18.3;
  - los 16 resultados del Caso cap. 18.
- **SD1**: ISO 9001, CMMI-DEV N3 (vence nov-2026), División QA de 10 personas, Miño como Líder de Calidad (meses 1–56), Henríquez a cargo de la aceptación.
- **SD3**: 261 requisitos (175 RF y 86 RNF); 56 críticos, 162 altos y 43 medios; T-12 con 645 IDs; Tabla 3.A.13 con R18-01 a R18-16; OTIF de 90, 93 y 95 % en los meses 15, 19 y 32; reversión de 40 min.
- **SD4**:
  - carga: 12,34 TPS en régimen, 14,66 TPS en el peak de septiembre y 21,99 TPS de prueba; 438,30 / 775,33 usuarios concurrentes; 158 dispositivos;
  - arquitectura: 12 módulos, 15 integraciones, 230.252 / 353.333 mensajes diarios;
  - pipeline y despliegue: 5 ambientes; reversión ≤10 min; métricas DORA; presupuesto de error de 43 min;
  - aceptación: protocolos AL-xx de la Tabla A.27.
- **SD5**: 7 dimensiones ISO 25012, 16 indicadores, 32,11 GB a migrar y 0 diferencias no explicadas.
- **SD6**: iteraciones de 2 semanas, 5 puertas, evaluadores (hasta 16 por día en los meses 9–12 y 16–18).
- **SD7, T-14 y T-15**:
  - paquetes CAL (4.656 HH);
  - paquetes de pruebas SEG/SRE (3.8.6: 160, 3.8.8: 320, 3.9.5: 320, 3.9.7: 160);
  - reserva protegida E1 CAL de 1.024 HH;
  - dotación CAL por mes;
  - reservas por hito (H1 6 … H10 25 días hábiles);
  - fechas de los hitos;
  - indicadores de marcha blanca (Tabla 7.9).
- **SD8**: R8-18 (valor esperado 2.956,80), R8-31 (153,60), R8-32 (204,80) y R8-26.
- **SD13**: indicadores de INN-02, I-02A a I-02D.

## D. Cálculos que debe mostrar el SD9 (todos en la planilla)
1. **Carga y estrés**:
   - 1,5 × 14,66 = 21,99 TPS;
   - usuarios de prueba: 1,5 × 775,33 ≈ 1.163, y 1,5 × 438,30;
   - dispositivos: 1,5 × 158 = 237;
   - escalones de estrés de 1×, 1,5×, 2× y 3× hasta el punto de quiebre (3× = 43,98 TPS, por RT-09.03);
   - mensajes de integración en peak × 1,5.
2. **Presupuesto de error**: (1 − 0,999) × 30 × 24 × 60 = 43,2 min al mes, por cada nivel de servicio de la Tabla 16.
3. **Estimación de casos de prueba**: requisitos por prioridad × casos por requisito (supuesto declarado, por ejemplo 5/3/2), más un caso por cada RT con estado Cumple o Parcial; tamaño y duración de la batería de regresión.
4. **HH de calidad**: suma por paquete y por mes contra la dotación CAL del T-15; capacidad de los evaluadores (16 × días hábiles) en los meses 9–12 y 16–18 contra las HH programadas; participación de las HH de calidad en las 216.935 HH.
5. **Calendario de pruebas periódicas en Operación**:
   - DR: 2 × 3 años = 6;
   - restauraciones: 36;
   - resiliencia: 6 semestrales + antes de cada paso;
   - pentest: 3 anuales + antes de H7 y H12;
   - verificación de que ninguna cae en congelamiento (1–25 sep, diciembre, 3 primeros días hábiles).
6. **Aceptación (T-17)**: por hito, entrega + 10 días de revisión + 10 de subsanación contra la reserva del T-15, para obtener la holgura restante.
7. **Costo de la calidad en HH (PMBOK cap. 8)**:
   - prevención: 1.5.x y 2.6.x;
   - evaluación: 3.8, 3.9 y 8.x;
   - fallas internas: R8-31;
   - fallas externas: R8-18;
   - con sus proporciones.
8. **Métricas objetivo**: DRE = defectos antes de producción / total ≥ meta; densidad de defectos por KLOC o por punto de caso; tasa de cambios fallidos ≤5 %.
9. **Umbrales de código**: tabla de valores con fórmula de cumplimiento (pasa/no pasa) para simular una medición.

## E. Planilla `LafroX-Calculos-SD9.xlsx` (hojas)
| Hoja | Contenido |
|---|---|
| Léeme | Propósito, convenciones (celdas de entrada en azul, fórmulas en negro), fuentes y fecha |
| Datos_Base | Cada dato del bloque C con valor, unidad y fuente (archivo y sección). Las demás hojas lo referencian |
| ISO25010 | Las 8 características: subcaracterística, métrica, umbral, fuente, método, ambiente y paquete EDT |
| Metricas_Codigo | Umbrales bloqueantes por lenguaje (PHP, Kotlin, Angular), herramienta, puerta y fórmula de cumplimiento |
| Carga_Estres | Cálculo 1 y escalones de estrés |
| Disponibilidad | Cálculo 2 por nivel de servicio |
| Casos_Prueba | Cálculo 3 con los supuestos editables |
| HH_Calidad | Paquetes × meses 1–56, totales, dotación CAL y capacidad de evaluadores (cálculo 4) |
| Calendario | Matriz de 56 meses × tipo de prueba, con formato condicional para congelamientos y conteos (cálculo 5) |
| Aceptacion_T17 | H1–H12: mes, fecha, entregable, 10+10, reserva y holgura (cálculo 6) |
| COQ | Cálculo 7 |
| Metricas_Proceso | Cálculos 8 y 9 |
| Inconsistencias | Las contradicciones detectadas, con su corrección propuesta (ver F) |
| Figuras | Lista de las 10 figuras draw.io con sección y estado |

## F. Inconsistencias que se registran (y se corrigen en la etapa de redacción, no ahora)
- Cobertura: T-14 1.5.2 y SD4 L2158 deben decir 70 % de negocio + 80 % global.
- Pentest semestral en SD1 L180 y RNF-14.06: pasa a anual y antes de cada paso.
- T-14 asigna 3.8.7, 3.9.1 y 3.9.6 a meses distintos de H5, H9 y H10.
- El refuerzo de evaluadores (meses 9–12 y 16–18) no coincide con la ejecución CAL (9–10 y 16–17).
- SD5 usa 12,30 TPS y SD4 12,34 TPS.
- SD7 indica 12 resultados R18 en E1 y el Anexo 7.C, 14.
- SD3 L107 dice que el T-12 trae prueba y criterio, pero el T-12 no tiene esa columna. La matriz 9.C la cubre.
- RNF-14.07 se verifica con un método incorrecto.
- CMMI vence en nov-2026.

## Verificación
- Abrir la planilla y recalcular (LibreOffice headless, si está disponible): cero errores `#REF!`, `#DIV/0!` o `#VALUE!`.
- Comprobar valores clave: 21,99 TPS; 43,2 min; 4.656 HH CAL; 6 pruebas DR; 36 restauraciones; 3 pentests.
- Confirmar que cada valor de Datos_Base cita un archivo y una sección que existen (grep).
- No tocar ningún entregable .md salvo `compct/plan_SD9.md` y `CONTEXTO_SESION.md`. Sin commit.
