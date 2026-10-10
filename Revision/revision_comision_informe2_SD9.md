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

**Veredicto actualizado tras las correcciones del 9 de octubre de 2026.** El subdocumento sigue formalmente en 0 por el §7.1 letra d: 13 celdas `[[REVISIÓN HUMANA]]` vacías en la declaración de IA. Son 7 en el cuerpo, 4 en los anexos, 1 en el T-13 y 1 en el T-17, y son cuadros de aprobación en blanco. Esa causal sólo la puede cerrar el equipo humano.

Sin esa causal, el diagnóstico de contenido sube a 70. El núcleo existe y es propio de Puelche: 29 métricas con umbral, 24 reglas bloqueantes, pruebas del caso calculadas desde la volumetría y una matriz de 645 identificadores. Las contradicciones principales detectadas en cobertura, bloqueo de vulnerabilidades, herramientas del pipeline, secuencia T-15 y pruebas antes de H7/H12 fueron corregidas en SD9 y propagadas a T-14, T-15, SD4, SD6, T-10, T-11, Anexo 4-P y el resumen del SD6. Siguen pendientes la revisión humana, las páginas de citas a las Bases y controles dependientes del PDF final; además, si se quiere demostrar la separación máxima semestral con precisión diaria, faltan fechas exactas de ejecución dentro de cada mes.

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
- Cerrado: la cobertura unitaria se alineó como global ≥ 80 % y la lógica de negocio como ≥ 70 % en SD9, T-14 1.5.2, SD6 6.2.2, T-10 y el resumen del SD6.
- Cerrado: la Tabla 9.4 incluye las cuatro métricas DORA, incluida la frecuencia de despliegue.
- Cerrado: 9.1.3 corrige el conteo y no trata la promoción del mismo artefacto como umbral propio de LafroX.
- Cerrado: ISO/IEC 25012 e ISO 9001:2015 tienen entrada en Referencias.

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
- Cerrado: G3 ya no permite levantar vulnerabilidades críticas o altas de imagen; sólo la regresión de desempeño 9B-22 admite excepción controlada sin incumplir p95 contractual.
- Cerrado: las herramientas de prueba y análisis fueron incorporadas a SD4 4.2.4.1, T-11, Anexo 4-P, SD6 6.2.2 y T-10: k6, OWASP ZAP, axe-core, AWS Fault Injection Service, Kover, JUnit 5, Espresso, Jest, PCOV, deptrac, PHPMD, PHPCPD, PhpMetrics, detekt, ktlint y ESLint.
- Cerrado: T-15 ahora programa 3.8.4, 3.8.5, 3.8.6 y 3.8.8 desde el 21-10-2027, con predecesora 3.8.1, y 3.9.3, 3.9.4, 3.9.5 y 3.9.7 desde el 19-05-2028, con predecesora 3.9.1. La aceptación 3.9.2 se ubica después de 3.9.1.
- Cerrado: SD9, T-13 y T-17 exigen repetir intrusión por tercero, resiliencia y carga aplicable antes de H7/H12; puede acotarse el alcance a componentes modificados, pero no sustituirse por una declaración de ausencia de cambios.
- Cerrado: Anexo 9.D deriva 26 días hábiles como 6 × 52 / 12.

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
| Cobertura unitaria | ≥ 80 % global | T-14 1.5.2, SD6, T-10 y resumen SD6 alineados a 80 % global | OK |
| Imagen con vulnerabilidad alta | No admite excepción | SD6 6.2.2 detiene la promoción | OK |
| Herramientas de prueba y análisis | 16 herramientas | SD4, T-11, Anexo 4-P, SD6 y T-10 las registran | OK |
| Pruebas de intrusión | Anuales, antes de cada paso y repetidas antes de H7/H12 | T-14 8.2.2 anual; SD1 pendiente de armonización si mantiene política semestral | Parcial |
| Inicio de las pruebas de Preproducción | Después de integración/regresión | T-15 alinea 3.8.4–3.8.8 con 3.8.1 y 3.9.3–3.9.7 con 3.9.1 | OK |
| RNF-06.02, 06.03, 11.03, 11.04 | Verificados con la fila que los absorbe (Anexo 9.C) | T-12: «Cumple» con componente propio; SD3 Tabla 3.A.5a: absorbidos o alias | Diferencia entre SD3 y T-12 |
| RTO, RPO, ambientes, despliegue, p95 | 4 h, 15 min, 5 ambientes, azul-verde con canario, Tabla 31 | SD4 | OK |
| Hitos y meses | E-25 y T-15 Tabla 5.2 | SD7, T-15 | OK |

### Forma e indicios de uso de IA

- Crítico: 13 celdas `[[REVISIÓN HUMANA]]` en las declaraciones de IA de los cuatro archivos (Aclaraciones §7.1 d, cuadros de aprobación en blanco). Desde el Informe 2, el subdocumento se tiene por no presentado.
- Cerrado: el código R18 quedó definido como R18-01 a R18-16 en el cuerpo y las figuras principales usan «16 resultados del Caso» o ejemplos concretos. La revisión visual final debe confirmar que la versión `.drawio` insertada en el PDF coincide con el Markdown.
- Las figuras del Markdown están en Mermaid y las fuentes `.drawio` difieren en detalle. La 9.4 agrega filas: DAST, corte de enlace y marcha blanca. La 9.7 trae un ejemplo concreto: RF-09.01, M9, 3.4.4. La 9.9 agrega las pruebas periódicas por mes. El texto que explica cada figura debe corresponder a la versión que se inserte en el PDF.
- Citas a las Bases: 18 de 27 no indican página (Aclaraciones §6). Se verifica en el PDF.
- Ningún título va seguido directamente de otra cosa que no sea texto: 0 casos en los cuatro archivos. Las 9 tablas del cuerpo tienen 5 columnas o menos y llevan análisis posterior. Las 10 figuras se citan antes y se explican después.
- Sin precios, tarifas ni montos: 0 apariciones de «$», «USD», «CLP» o «UF» (Art. 50.2).
- Sin marcadores, notas de proceso ni ruptura de la ficción.

### Qué se espera en el Informe 3

- Las 13 celdas de revisión humana firmadas por un integrante, con lo que efectivamente verificó.
- Confirmar en PDF que las figuras insertadas no reintroduzcan códigos sin glosario ni diferencias con el Markdown.
- Completar las páginas de las citas a las Bases cuando exista el PDF final paginado.
- Mantener la coherencia ya aplicada de cobertura, bloqueo de imágenes, herramientas del pipeline, predecesoras de certificación y repetición de intrusión/resiliencia/carga antes de H7/H12.
- Decidir si se acreditarán fechas exactas por día para demostrar la separación máxima de seis meses en las pruebas semestrales.

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
- **Coherencia entre plan, equipo y arquitectura.** Las HH de calidad del SD9 coinciden con el T-15. La dotación CAL del mes 16 (10 personas) y el refuerzo de evaluadores cubren las horas programadas. Las herramientas de prueba y análisis ya fueron incorporadas al SD4, al T-11, al Anexo 4-P, al SD6 y al T-10.
- **Fundamentación ingenieril.** Las cargas de prueba, el presupuesto de error de 43,2 minutos, el número de casos, la duración de la regresión, el costo de la calidad y las holguras de los hitos están calculados y se reproducen desde los datos citados.
- **Uso de IA.** La causal vigente son las celdas de revisión humana. El código R18 ya fue definido; queda pendiente la confirmación visual de las figuras finales.
- **Cumplimiento.** No hay precios, plazos fuera del Art. 17° ni archivos mal nominados.

| Ítem | Peso | Puntaje | Ponderado |
| --- | --- | --- | --- |
| 9. Plan de calidad — T-13 y T-17 | 8 % | 0 | 0,0 |
| Diagnóstico de contenido sin la causal §7.1 (no suma) | — | 70 | — |

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

### Seguimiento — correcciones cruzadas aplicadas

| N.° | Documento y sección | Estado vigente |
| --- | --- | --- |
| 1 | T-14, paquete 1.5.2 | Corregido: cobertura unitaria global ≥ 80 % y lógica de negocio ≥ 70 %, ambas bloqueantes. |
| 2 | SD4, sección 4.2.4.1 (pipeline) | Corregido: distingue cobertura de lógica de negocio y cobertura unitaria global, e incorpora el catálogo de herramientas del SD9. |
| 3 | SD4, T-11 y Anexo 4-P | Corregido: registran k6, OWASP ZAP, axe-core, AWS Fault Injection Service, JUnit 5, Espresso, Kover, Jest, PCOV, PHPMD, PHPCPD, PhpMetrics, deptrac, detekt, ktlint y ESLint con su función. |
| 4 | SD6, sección 6.2.2, y Formulario T-10 | Corregido: cobertura global ≥ 80 % e incorporación de las herramientas del pipeline. |
| 5 | T-15, sección 5.2 y Tabla 6.1 | Corregido: 3.8.4, 3.8.5, 3.8.6 y 3.8.8 dependen de 3.8.1; 3.9.3, 3.9.4, 3.9.5 y 3.9.7 dependen de 3.9.1. |
| 6 | T-14, paquetes 8.1.3 y 8.2.2 | Corregido: DR en meses 27, 33, 39, 45, 51 y 54; resiliencia en 26, 32, 38, 44, 50 y 55; intrusión anual en 28, 40 y 52. |
| 7 | Resumen del SD6 | Corregido: cobertura unitaria global ≥ 80 %. |

### Pendientes fuera de esta iteración

| N.° | Documento y sección | Pendiente |
| --- | --- | --- |
| 1 | SD1, sección 1.3.2 | Si mantiene pruebas de intrusión externas «semestrales», aclarar que es política corporativa y que este contrato exige anuales y antes de cada paso, o igualar la frecuencia. |
| 2 | SD3, sección 3.2, y Anexo 3.J | Remitir al Anexo 9.C (prueba) y al Formulario T-17 (criterio), porque el T-12 tiene cinco columnas. |
| 3 | T-12, filas RNF-06.02, RNF-06.03, RNF-11.03 y RNF-11.04 | Indicar la fila que los absorbe, como en el SD3, Tabla 3.A.5a. |
| 4 | SD3, sección 3.2 | Explicar la diferencia entre 261 requisitos del SD3 y 271 filas del T-12. |
| 5 | SD1, sección 1.4 | Declarar la renovación CMMI-DEV N3 o el régimen mientras se tramita, coherente con SD9, 9.1.2. |
| 6 | SD3, Anexo 3.B, RNF-14.07 | Reemplazar «ejercicio de recuperación» por verificación con puertas G2 y G4 (SAST y OWASP ZAP), como en el Anexo 9.C. |
| 7 | T-14, paquetes 3.8.7, 3.9.1 y 3.9.6 | Separar el mes de ejecución del mes del hito del E-25 si aún inducen confusión. |
| 8 | SD6, sección 6.1.3 | Precisar que los meses 11, 12 y 18 cubren la subsanación, como explica SD9, 9.3.2. |
| 9 | T-15, paquete 3.7.3 | Verificar si la carga de saldos migrados toca Producción durante el congelamiento de diciembre. |
