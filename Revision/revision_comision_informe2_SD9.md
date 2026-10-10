# Revisión de la Comisión — Informe 2 · Subdocumento 9

LAFROX · GRUPO 2 · INFORME 2 · Caso 2 · Distribuidora Puelche S.A.

Revisión aplicada con `Revision/prompt_revision_comision_informe2.md` sobre las fuentes Markdown del 9 de octubre de 2026. Conforme a la regla de este repositorio, la evidencia se cita por archivo y sección. Quedan pendientes del PDF final la paginación, el índice paginado, el folio, la firma, el tamaño de letra, la legibilidad de las figuras y la plantilla.

**Archivos recibidos:**

- `09_plan_calidad/LAFROX-Subdocumento9.md`, `LAFROX-Subdocumento9-Anexos.md`, `LAFROX-Formulario-T-13.md` y `LAFROX-Formulario-T-17.md`. Nomenclatura conforme (Aclaraciones §1).
- En `09_plan_calidad/Diagramas/`: 10 fuentes `.drawio` (Figuras 9.1 a 9.10) y una planilla de cálculo de trabajo. La planilla no es entregable.

**Documentos revisados:**

| Documento | Extensión | Figuras | Tablas |
| --- | --- | --- | --- |
| Subdocumento 9 | 525 líneas, unas 8.800 palabras | 10 | 9 |
| Anexos | 848 líneas | 0 | 6 (una de 645 filas) |
| Formulario T-13 | 172 líneas | 0 | 6 |
| Formulario T-17 | 233 líneas | 0 | 14 |

Se contrastaron contra las cuatro Bases, SD1, SD3, SD4, SD6, SD7, T-12, T-14, T-15, SD8, T-16 y SD13.

## CORRECCIONES DEL INFORME 1

No aplica. El SD9 no se presentó en el Informe 1 ni en la revisión anterior del Informe 2 (`Revision/revision_comision_informe2.md`), así que no hay observaciones previas que verificar.

## 9. PLAN DE CALIDAD — Formularios T-13 y T-17 (8 %)

[Índice obligatorio:

- 9.1 Plan de Calidad: ISO/IEC 25010 y modelos de madurez; métricas de código, cobertura, complejidad y acoplamiento con umbrales bloqueantes.
- 9.2 Estrategia de Aseguramiento de Calidad: puertas, revisión por pares, análisis estático y dinámico; pruebas ISO/IEC/IEEE 29119 (niveles, tipos, ambientes, datos, automatización); verificación, validación y trazabilidad.
- 9.3 Alineación con Plan de Trabajo.]

**Revisión: (Puntaje 0)**

**Veredicto.** El subdocumento se tiene por no presentado por un indicio del §7.1 letra d: 13 celdas `[[REVISIÓN HUMANA]]` vacías en la declaración de IA. Son 7 en el cuerpo, 4 en los anexos, 1 en el T-13 y 1 en el T-17, y son cuadros de aprobación en blanco. A eso se suma un código interno sin glosario en tres figuras del cuerpo («R18»).

Sin esa causal, el diagnóstico de contenido es 20. El núcleo existe y es propio de Puelche: 29 métricas con umbral, 24 reglas bloqueantes, pruebas del caso calculadas desde la volumetría y una matriz de 645 identificadores. Pero contradice a otros subdocumentos en un umbral de calidad (cobertura, T-14 1.5.2), en la regla de bloqueo de imágenes vulnerables (SD6, sección 6.2.2) y en el conjunto de herramientas: 16 herramientas de prueba y análisis que no figuran en el SD4, sección 4.1.1, ni en el SD6, sección 6.2. Si se corrigen las contradicciones y se firma la revisión humana, el contenido justificaría 60 a 80.

### Introducción al Plan de calidad

- OK: el texto de introducción va inmediatamente bajo el título del capítulo. Conecta con SD3, SD4, SD5, SD6, SD7, SD8 y SD13, con los Anexos 9.A–9.D y con los Formularios T-13 y T-17 (Aclaraciones §2).
- OK: abre con exigencias propias del caso: picking en 1 s, 14 h sin señal, 96 camiones entre 05:30 y 07:00, retiro en menos de 2 h.

### 9.1 Plan de Calidad

- OK: las ocho características del Art. 24 tienen métrica y umbral propios. Son 29 métricas en el Anexo 9.A y 8 umbrales principales en la Tabla 9.2, con origen en las Bases, el Caso o el SD4. No es la lista de características de la norma.
- OK: hay modelo de madurez declarado y usado. CMMI-DEV N3 se cruza con tres áreas de práctica y TMMi N3 se mapea en la Tabla 9.1. El documento no se atribuye una certificación TMMi; declara una autoevaluación en el H5 y el H10.
- OK: SD9, 9.1.2 reconoce que la evaluación SCAMPI A vence en noviembre de 2026 y condiciona su invocación a la renovación. Eso evita una certificación que nadie pudo obtener (§7.1 b).
- OK: los umbrales de código son numéricos y bloqueantes (Tabla 9.3): cobertura ≥ 70 % y ≥ 80 %, complejidad ciclomática ≤ 10 y cognitiva ≤ 15, 0 dependencias prohibidas, duplicación ≤ 3 %, deuda ≤ 5 %. El acoplamiento se controla con deptrac sobre los 12 módulos (RT-02.02).
- OK: el costo de la calidad está calculado en HH y se reproduce:
  - prevención 3.984 + evaluación 6.864 = 10.848 HH;
  - fallas internas 358,4 HH (R8-31 + R8-32) y externas 2.956,8 HH (R8-18);
  - la razón entre conformidad y no conformidad es 3,3;
  - lo de conformidad equivale al 5,0 % de 216.935 HH.

  No hay montos (Art. 50.2).
- Contradicción con otro subdocumento (§7.1 c). SD9, 9.1.4 exige «≥ 80 %» de cobertura unitaria sobre «todo el código». El Formulario T-14, paquete 1.5.2, bloquea la versión «si la cobertura de líneas por pruebas unitarias del código modificado es inferior al 80 %». Global y código modificado son métricas distintas. El paquete que implementa la puerta mide otra cosa que la que el plan declara.
- SD9, 9.1.5 afirma: «Las cuatro métricas de entrega son las de Forsgren, Humble y Kim (2018)». La Tabla 9.4 muestra tres: tasa de cambios fallidos, tiempo del commit a producción y tiempo de restauración. Falta la frecuencia de despliegue, aunque el SD4, sección 4.2.4.1.4, la compromete (cadencia quincenal) y el RT-04.12 la exige.
- SD9, 9.1.3 afirma que «seis de los ocho umbrales vienen fijados por las Bases o por el caso. Los dos restantes, cobertura global y promoción del mismo artefacto, son compromisos de LafroX». La promoción del mismo artefacto es el RT-04.08 de las Bases, y la propia Tabla 9.2 lo cita como origen. El conteo es incorrecto.
- Las normas ISO/IEC 25012 (tres menciones) e ISO 9001:2015 (dos menciones) se citan en el texto sin entrada en Referencias. Eso incumple la correspondencia 1:1 entre citas y lista (Aclaraciones §6).

### 9.2 Estrategia de Aseguramiento de Calidad

- OK: las puertas G0–G6 están ubicadas en la cadena del SD4 y el SD6 (Figura 9.3, Tabla 9.5). Indican qué bloquea cada una y quién puede levantarla, y el texto explica cómo calzan con las cinco compuertas del SD6.
- OK: la revisión por pares tiene regla concreta: un par distinto del autor, más el arquitecto en módulos críticos y Seguridad en datos personales (RT-04.03).
- OK: hay análisis estático y dinámico con herramienta por lenguaje. Los cinco mínimos del RT-04.05 están cubiertos.
- OK: la estrategia sigue 29119, con los tres niveles de proceso y técnicas de la parte 4 asignadas por tipo de regla.
- OK: las pruebas propias del caso están, con cifras derivadas y verificables:
  - 21,99 TPS = 1,5 × 14,66;
  - 1.163 usuarios = 1,5 × 775,33;
  - 237 dispositivos = 1,5 × 158;
  - 43,98 TPS a 3×;
  - 10,41 TPS en la ventana de 05:30 a 07:00;
  - 14 h sin señal, 24 h sin enlace, −22 °C con guantes, sincronización en 10 min y 2 h, recuperación ante desastres y dos ensayos de migración (Tabla 9.6).
- OK: los cinco ambientes del SD4, Tabla 12, más terreno (Figura 9.4). Los datos de prueba son sintéticos y anonimizados, con Macie y la Ley 21.719 (Figura 9.5, Anexo 9.D).
- OK: la trazabilidad es de extremo a extremo y coherente con el T-12. La matriz de 645 identificadores (Anexo 9.C) cuadra: 605 con prueba propia, 31 «No cumple» y 9 absorbidos, 1.192 casos más 90 de contrato, 1.282 en total, con 1.026 casos de regresión automatizada en 4,3 h.
- Contradicción con otro subdocumento (§7.1 c) e interna. La Tabla 9.5 permite que el Líder de Calidad levante G3 ante una «Imagen con vulnerabilidad alta» con registro de deuda. Choca con tres cosas:
  - el SD6, sección 6.2.2, que detiene la promoción ante «un hallazgo de seguridad crítico o alto en dependencias, código, secretos o imagen»;
  - el RT-04.05, que exige «criterios de bloqueo automático»;
  - la frase siguiente del propio SD9: «ninguna puerta automática se levanta por decisión de una persona».
- Herramientas que no aparecen en la arquitectura ni en la metodología (Paso 5, S6; Paso 7). Ninguna de estas 16 herramientas figura en el SD4 ni en el SD6, T-10 incluido:
  - k6, OWASP ZAP, axe-core y AWS Fault Injection Service;
  - Kover, JUnit 5, Espresso, Jest y PCOV;
  - deptrac, PHPMD, PHPCPD y PhpMetrics;
  - detekt, ktlint y ESLint.

  La única coincidencia es Amazon Inspector. La Comisión lee esto como texto generado por separado. El SD4, sección 4.1.1, debe registrarlas con su alternativa y criterio, y el SD6, sección 6.2.2, debe incorporarlas al pipeline.
- Incoherencia entre el plan y el cronograma. El T-13, Tabla T13.3, exige para la prueba de intrusión una «Versión congelada en Preproducción». La puerta G4 exige la regresión completa antes de promover a Preproducción. Pero el T-15 programa 3.8.4, 3.8.5, 3.8.6 y 3.8.8 desde el 01-10-2027, con predecesora 3.4, mientras la integración y regresión 3.8.1 termina el 20-10-2027. En la Etapa 2 pasa lo mismo: 3.9.3–3.9.5 empiezan el 01-05-2028, igual que 3.9.1. Con la regla del propio plan, las pruebas de Preproducción no pueden empezar antes de cerrar 3.8.1 y 3.9.1.
- «Antes de cada paso a producción» (BTT §20.1; RT-11.20; RT-10.07). La seguridad ofensiva y la resiliencia de la Etapa 1 se ejecutan en octubre y noviembre de 2027. El paso a producción del H7 es en mayo de 2028, después de tres meses de correcciones de marcha blanca. El documento no explica por qué la versión que pasa en el H7 no requiere repetir esas pruebas. El T-13, sección 8.1, sólo afirma que la marcha blanca es «el primer paso a Producción».
- El Anexo 9.D y el T-13 dividen los volúmenes mensuales por «26 días hábiles» sin mostrar la derivación: 6 días por semana × 52 semanas / 12 = 26 (§7.1 b; Aclaraciones §3).

### 9.3 Alineación con Plan de Trabajo

- OK: la Tabla 9.7 agrupa los paquetes de calidad por cuenta, con meses y HH que suman 10.848 HH, y coincide paquete por paquete con el T-15.
- OK: la Tabla 9.8 compara la reserva de cada hito con la subsanación de 10 días hábiles. Reconoce la holgura negativa del H1 (−4) y del H8 (−6) y la resuelve con la revisión anticipada que fijan el T-15, sección 5.5, y el R8-12.
- OK: el calendario de la Operación evita septiembre, diciembre y los tres primeros días hábiles. Los conteos cuadran con el T-14: 6 pruebas de recuperación, 6 de resiliencia, 3 de intrusión y 36 restauraciones.
- OK: el refuerzo de evaluadores está cuantificado: 16 × 21 días hábiles × 8 h = 2.688 HH al mes. Se explica su uso en los meses 11, 12 y 18 para la subsanación.
- El texto atribuye a la Etapa 1 «las de la Etapa 1 terminan en noviembre de 2027, antes de diciembre». Es correcto para 3.8. Pero el T-15 programa 3.7.3, saldos migrados del WMS de Talca, entre el 01-12 y el 31-12-2027, en pleno congelamiento. No es una prueba del SD9; queda registrado porque la Figura 9.9 no muestra la migración.

### Formularios T-13 y T-17

- OK: el T-13 contiene todo lo que exige su formulario:
  - niveles, tipos, ambientes y datos;
  - criterios de entrada y salida para 14 tipos;
  - suspensión, automatización y roles;
  - calendario de carga, resiliencia, recuperación y seguridad ofensiva con fechas del T-15 y meses calendario de la Operación.
- OK: el T-17 cubre el Art. 18.2 (expediente de cuatro elementos), los plazos 10 + 10 del Art. 18.3 y el procedimiento de observaciones con atraso imputable. Trae una ficha por hito, H1 a H12, coherente con el E-25, el contenido del acta y los 16 resultados del Caso con su momento y evidencia.
- El T-13 usa las siglas DES, CAL, IMP, SRE, SEG y DAT en la Tabla T13.1 sin definirlas en el formulario. La sección 9 describe cinco de ellas, pero no DES.

### Consistencia

| Decisión | SD9 | Otro documento | Estado |
| --- | --- | --- | --- |
| Cobertura unitaria | ≥ 80 % global | T-14 1.5.2: 80 % del código modificado | Contradicción |
| Imagen con vulnerabilidad alta | G3 levantable por el Líder de Calidad | SD6 6.2.2: detiene la promoción | Contradicción |
| Herramientas de prueba y análisis | 16 herramientas | SD4 4.1.1 y SD6 6.2.2: no figuran | Contradicción |
| Pruebas de intrusión | Anuales y antes de cada paso | SD1 1.3.2: «de forma semestral» (política corporativa); RNF-14.06 y T-14 8.2.2: anuales | Diferencia que debe explicarse en el SD1 |
| Inicio de las pruebas de Preproducción | Después de G4 (regresión completa) | T-15: 3.8.4–3.8.8 desde el 01-10-2027, en paralelo con 3.8.1 | Incoherencia |
| RNF-06.02, 06.03, 11.03, 11.04 | Verificados con la fila que los absorbe (Anexo 9.C) | T-12: «Cumple» con componente propio; SD3 Tabla 3.A.5a: absorbidos o alias | Diferencia entre SD3 y T-12 |
| RTO, RPO, ambientes, despliegue, p95 | 4 h, 15 min, 5 ambientes, azul-verde con canario, Tabla 31 | SD4 | OK |
| Hitos y meses | E-25 y T-15 Tabla 5.2 | SD7, T-15 | OK |

### Forma e indicios de uso de IA

- Crítico: 13 celdas `[[REVISIÓN HUMANA]]` en las declaraciones de IA de los cuatro archivos (Aclaraciones §7.1 d, cuadros de aprobación en blanco). Desde el Informe 2, el subdocumento se tiene por no presentado.
- Crítico: «R18» aparece en tres figuras del cuerpo sin definición en el texto: Figura 9.6, «Necesidad y resultados R18» y «Marcha blanca y R18»; Figura 9.7, «acta T-17 · R18». El prompt lo lista como código interno sin glosario. El cuerpo sí dice «los 16 resultados del Caso, capítulo 18», pero no los asocia al código.
- Las figuras del Markdown están en Mermaid y las fuentes `.drawio` difieren en detalle. La 9.4 agrega filas: DAST, corte de enlace y marcha blanca. La 9.7 trae un ejemplo concreto: RF-09.01, M9, 3.4.4. La 9.9 agrega las pruebas periódicas por mes. El texto que explica cada figura debe corresponder a la versión que se inserte en el PDF.
- Citas a las Bases: 18 de 27 no indican página (Aclaraciones §6). Se verifica en el PDF.
- Ningún título va seguido directamente de otra cosa que no sea texto: 0 casos en los cuatro archivos. Las 9 tablas del cuerpo tienen 5 columnas o menos y llevan análisis posterior. Las 10 figuras se citan antes y se explican después.
- Sin precios, tarifas ni montos: 0 apariciones de «$», «USD», «CLP» o «UF» (Art. 50.2).
- Sin marcadores, notas de proceso ni ruptura de la ficción.

### Qué se espera en el Informe 3

- Las 13 celdas de revisión humana firmadas por un integrante, con lo que efectivamente verificó.
- Una sola regla de cobertura en SD1, SD6, T-14 1.5.2, SD4 4.2.4.1 y SD9.
- Una sola regla de bloqueo de imágenes en SD6 y SD9, y la frase de la Tabla 9.5 coherente con ella.
- Las 16 herramientas registradas en el SD4, sección 4.1.1, con su alternativa y criterio, e incorporadas al pipeline del SD6, sección 6.2.2.
- Las predecesoras de 3.8.4–3.8.8 y 3.9.3–3.9.7 en el T-15 alineadas con la puerta G4, o una justificación de por qué esas pruebas pueden empezar antes. Además, una regla explícita para repetir la intrusión y la resiliencia antes del H7 y del H12, o el fundamento para no hacerlo.
- La Tabla 9.4 con las cuatro métricas DORA, el conteo de 9.1.3 corregido, ISO/IEC 25012 e ISO 9001 en Referencias, «R18» definido y DES definido en el T-13.

## CONSIDERACIONES TRANSVERSALES

- **Trazabilidad.** El requisito «lista de clientes afectados por lote en menos de dos horas» se recorre completo:
  1. Caso, capítulo 18, resultado 1.
  2. RF-09.01 (T-12).
  3. M9 Calidad y trazabilidad (SD4).
  4. Paquete 3.4.4 (T-14).
  5. Casos CP-RF-09.01-01 a -05 en 3.8.1 y 3.8.2 (Anexo 9.C).
  6. Juego JD-07 para el simulacro (Anexo 9.D).
  7. Resultado R18-01 en el cierre de la marcha blanca E1 (T-17, Tabla T17.2).

  La cadena que la revisión anterior daba por cortada en el S9 queda cerrada en estos archivos.
- **Coherencia entre plan, equipo y arquitectura.** Las HH de calidad del SD9 coinciden con el T-15. La dotación CAL del mes 16 (10 personas) y el refuerzo de evaluadores cubren las horas programadas. Las herramientas, en cambio, no están en la arquitectura.
- **Fundamentación ingenieril.** Las cargas de prueba, el presupuesto de error de 43,2 minutos, el número de casos, la duración de la regresión, el costo de la calidad y las holguras de los hitos están calculados y se reproducen desde los datos citados.
- **Uso de IA.** Las causales son las celdas de revisión humana y el código «R18» sin glosario. No hay otros marcadores.
- **Cumplimiento.** No hay precios, plazos fuera del Art. 17° ni archivos mal nominados.

| Ítem | Peso | Puntaje | Ponderado |
| --- | --- | --- | --- |
| 9. Plan de calidad — T-13 y T-17 | 8 % | 0 | 0,0 |
| Diagnóstico de contenido sin la causal §7.1 (no suma) | — | 20 | — |

## Seguimiento — correcciones aplicadas en el SD9 (9 de octubre de 2026)

Se corrigieron en `09_plan_calidad/` los hallazgos que dependen sólo del SD9, sus anexos, sus formularios y sus figuras:

| Hallazgo | Corrección | Archivo |
| --- | --- | --- |
| «R18» sin glosario en las Figuras 9.6 y 9.7 | Las figuras usan «16 resultados del Caso»; 9.2.5 define R18-01 a R18-16 antes de la Figura 9.7 | Subdocumento 9 y Fig_9-7 |
| Tabla 9.4 con tres métricas DORA | Se agregó la frecuencia de despliegue (cadencia quincenal) y el texto nombra las cuatro | Subdocumento 9, 9.1.5 |
| Conteo «seis de ocho» en 9.1.3 | Siete de ocho umbrales vienen de las Bases o del Caso; el de mantenibilidad combina el 70 % del Art. 24 con el 80 % de LafroX | Subdocumento 9, 9.1.3 |
| ISO/IEC 25012 e ISO 9001 sin referencia | Citas (ISO & IEC, 2008) e (ISO, 2015) en el texto y entradas en Referencias | Subdocumento 9 |
| G3 permitía levantar una vulnerabilidad alta de imagen | G3 y G4 sin excepción para hallazgos de seguridad; sólo la regresión de desempeño (9B-22) admite excepción del Líder de Calidad | Subdocumento 9, Tabla 9.5; Anexo 9.B |
| Pruebas «antes de cada paso a producción» sin fundamento para el H7 y el H12 | Se fundamenta el H6 y el H11 como primer paso; se repiten la intrusión acotada y la resiliencia antes del H7 y del H12 si cambió la superficie expuesta, con cargo a R8-07 | Subdocumento 9, 9.3.2; T-13, 8.1 |
| DES y demás siglas sin definir en el T-13 | Se definen DES, CAL, IMP, SRE, SEG y DAT | T-13, sección 2 |
| 26 días hábiles sin derivación | 6 × 52 / 12 = 26 (lunes a sábado) | Anexo 9.D |
| Figuras Mermaid y `.drawio` con contenido distinto | La 9.7 Mermaid incluye el ejemplo de RF-09.01; la 9.9 Mermaid incluye las pruebas periódicas y los congelamientos de la Operación | Subdocumento 9 |

Siguen abiertos dentro del SD9:
- Las 13 celdas `[[REVISIÓN HUMANA]]`. Sólo puede cerrarlas un integrante que haya hecho la revisión.
- La página de las 18 citas a las Bases que no la indican. Se agrega al compilar el PDF, para no inventar páginas.

### Correcciones pendientes en otros subdocumentos (no aplicadas)

| N.° | Documento y sección | Qué dice hoy | Qué debe decir para ser coherente con el SD9 |
| --- | --- | --- | --- |
| 1 | T-14, paquete 1.5.2 | Bloqueo si la cobertura del «código modificado» es inferior al 80 % | Cobertura unitaria global ≥ 80 % y de lógica de negocio ≥ 70 %, ambas bloqueantes |
| 2 | SD4, sección 4.2.4.1 (pipeline) | Mide «cobertura» sin distinguir las dos métricas | Las dos métricas de cobertura con sus umbrales |
| 3 | SD4, sección 4.1.1 | No registra las herramientas de prueba y análisis | Registrar k6, OWASP ZAP, axe-core, AWS Fault Injection Service, JUnit 5, Espresso, Kover, Jest, PCOV, PHPMD, PHPCPD, PhpMetrics, deptrac, detekt, ktlint y ESLint, con alternativa y criterio |
| 4 | SD6, sección 6.2.2, y Formulario T-10 | El pipeline lista PHPUnit, PHPStan, Larastan, Pint, auditoría, contratos y escaneos | Incorporar las mismas herramientas y las puertas G0–G6 del SD9 |
| 5 | T-15, sección 6.1 (predecesoras) | 3.8.4, 3.8.5, 3.8.6 y 3.8.8 empiezan el 01-10-2027 con predecesora 3.4; 3.9.3–3.9.5 y 3.9.7 empiezan el 01-05-2028 con 3.5 | Predecesora 3.8.1 y 3.9.1 (o su regresión), coherente con la puerta G4. Recalcular fechas y reservas del H5 y del H10 en la Tabla 5.2, y propagar a SD7, SD8 y la planilla del Gantt |
| 6 | SD1, sección 1.3.2 | Pruebas de intrusión externas «de forma semestral» | Aclarar que es la política corporativa y que en este contrato son anuales y antes de cada paso (RT-11.20), o igualar la frecuencia |
| 7 | SD3, sección 3.2, y Anexo 3.J | El T-12 trae «prueba prevista y criterio de aceptación»; los protocolos van «en el plan de calidad de la oferta» | Remitir al Anexo 9.C (prueba) y al Formulario T-17 (criterio), porque el T-12 tiene cinco columnas |
| 8 | T-12, filas RNF-06.02, RNF-06.03, RNF-11.03 y RNF-11.04 | «Cumple» con componente propio | Indicar la fila que los absorbe, como en el SD3, Tabla 3.A.5a |
| 9 | SD3, sección 3.2 | 261 requisitos (175 RF y 86 RNF) | Explicar la diferencia con las 271 filas del T-12 (filas absorbidas, alias y no ofertadas) |
| 10 | SD1, sección 1.4 | CMMI-DEV N3 válido hasta noviembre de 2026 | Declarar la renovación o el régimen mientras se tramita, coherente con el SD9, 9.1.2 |
| 11 | SD3, Anexo 3.B, RNF-14.07 | SAST/DAST verificado con «ejercicio de recuperación» | Verificación con las puertas G2 y G4 (SAST y OWASP ZAP), como en el Anexo 9.C |
| 12 | T-14, paquetes 3.8.7, 3.9.1 y 3.9.6 | «Mes 10 (H5)», «Mes 16 (H9)», «Meses 16 y 17 (H10)» | Separar el mes de ejecución del mes del hito del E-25 (H5 mes 12, H9 mes 17, H10 mes 18) |
| 13 | SD6, sección 6.1.3 | Refuerzo de evaluadores en los meses 9–12 y 16–18 | Precisar que los meses 11, 12 y 18 cubren la subsanación, como explica el SD9, 9.3.2 |
| 14 | T-15, paquete 3.7.3 | Saldos migrados del WMS de Talca entre el 01-12 y el 31-12-2027 | Verificar si la carga toca Producción durante el congelamiento de diciembre |
