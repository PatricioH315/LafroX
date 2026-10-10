# Revisión de la Comisión — Informe 2 · Subdocumento 9 (v3)

LAFROX · GRUPO 2 · INFORME 2 · Caso 2 · Distribuidora Puelche S.A.

Revisión aplicada con `Revision/prompt_revision_comision_informe2.md` sobre las fuentes Markdown vigentes al 9 de octubre de 2026, después del cierre de los pendientes cruzados 1–9 registrado en `compct/CONTEXTO_SESION.md`. Conforme a la regla del repositorio, la evidencia se cita por archivo y línea; no se inventan páginas. Paginación, índice paginado, folio, firma, tamaño tipográfico, legibilidad de figuras y plantilla quedan pendientes de la compilación del PDF final. Las cifras se recalcularon con lectura directa de los archivos y, cuando se indica, con un conteo automatizado de la matriz del Anexo 9.C contra el T-12.

**Archivos recibidos:** `LAFROX-Subdocumento9.md`, `LAFROX-Subdocumento9-Anexos.md`, `LAFROX-Formulario-T-13.md`, `LAFROX-Formulario-T-17.md` (carpeta `09_plan_calidad/`). Nomenclatura conforme (Aclaraciones §1). Un formulario por archivo. Fuentes `.drawio` de las Figuras 9.1–9.10 en `09_plan_calidad/Diagramas/` (no entregables por sí mismas).

**Documentos revisados:** Subdocumento 9 (556 líneas, 10 figuras Mermaid, 9 tablas); Anexos (848 líneas, 645 filas de matriz); T-13 (172 líneas); T-17 (233 líneas). Contrastados contra las cuatro Bases y contra SD1, SD3 + Anexos + T-12, SD4 + Anexos + T-11, SD5 + Anexos, SD6 + T-9/T-10, SD7 + Anexos + T-14/T-15/T-18, SD8 + Anexos + T-16 y SD13.

**Abreviaturas de rutas usadas en esta revisión:** SD9 = `09_plan_calidad/LAFROX-Subdocumento9.md`; AN9 = `09_plan_calidad/LAFROX-Subdocumento9-Anexos.md`; T13 / T17 = formularios del SD9; BA, BTT, CASO, ACL = `Bases/Bases_Administrativas.md`, `Bases_Tecnicas_Transversales.md`, `Caso_02_Logistica.md`, `aclaraciones-licitacion.md`; T12, T14, T15 = formularios en sus carpetas; SD1, SD4, SD5, SD6, SD7, SD8A (Anexos del SD8), T9, T10 = archivos homónimos.

---

## 1. Puntaje

### 9. PLAN DE CALIDAD — Formularios T-13 y T-17 (8 %)

[9.1 Plan de Calidad · 9.2 Estrategia de Aseguramiento de Calidad · 9.3 Alineación con Plan de Trabajo]

**Revisión: (Puntaje 0)**

**Veredicto.** El subdocumento se tiene por no presentado. Persisten 13 celdas `[[REVISIÓN HUMANA]]` (cuadros de aprobación en blanco, ACL §7.1 d, ACL:129) y aparecen dos indicios nuevos de la misma letra: una remisión a un capítulo que no forma parte de la entrega («el Capítulo 11 desarrolla», SD9:520) y una remisión a una figura que no contiene lo que se le atribuye («matriz de cobertura del SD7, Figura 7.4», SD9:400, cuando la Figura 7.4 del SD7 es la Fase 2 de la EDT, SD7:81). Se suma un indicio de la letra c: el Anexo 9.C declara un estado distinto al del T-12 en 99 de 645 identificadores. Desde el Informe 2 cualquiera de ellos deja el ítem en 0 sin subsanación (ACL:131).

**Diagnóstico de contenido sin la causal §7.1 (no suma): 20.** El núcleo existe (umbrales bloqueantes numéricos y estrategia 29119 propia de Puelche), pero el árbol del prompt se detiene en el paso 6 por contradicciones con otros documentos en decisiones de etapa y de umbral: (i) el SD9 y el T-13 llaman «primer paso a Producción» al H6/H11, cuando el E-25 y el Art. 17.1 sitúan el paso a producción en el H7 (mes 16) y el H12 (mes 21), y las pruebas obligatorias previas a esos hitos quedan sin fecha, paquete ni HH; (ii) la frecuencia de recuperación ante desastres del primer año de Operación no alcanza el umbral del RT-07.07; (iii) la Figura 9.9 contradice la Tabla 9.9, el T-13 y el T-14 en cuatro de doce pruebas semestrales. Resueltos esos tres puntos, el contenido quedaría en 40 por las faltas de cálculo y de cobertura que se detallan en la sección 2.

| Ítem | Peso | Puntaje | Ponderado |
| --- | --- | --- | --- |
| 9. Plan de calidad — T-13 y T-17 | 8 % | 0 | 0,0 |
| Diagnóstico de contenido sin la causal §7.1 (no suma) | — | 20 | — |

Causales duras revisadas (Paso 1 del prompt): precios 0 apariciones de «$», «USD», «CLP» o «UF» en los cuatro archivos (BA Art. 50.2); formulario del ítem presente (T-13 y T-17); cronograma alineado al Art. 17° (SD9:432 y 436; T17:125, 137, 185, 197); folio y firma no verificables en Markdown; indicios de IA presentes (ver H01–H03).

---

## 2. Hallazgos por severidad

### Críticos

**H01 — Celdas de revisión humana vacías (No corregido, revisiones v1 y v2).** 13 celdas `[[REVISIÓN HUMANA]]`: SD9:550–556 (7), AN9:845–848 (4), T13:172 (1), T17:233 (1). Todas las filas declaran nivel «Alto» en texto. ACL §7.1 d (ACL:129) y §7.2 (ACL:155): un nivel «Alto» no autoriza un capítulo sin revisión humana.

**H02 — Remisiones a objetos inexistentes o equivocados (nuevo).**
- SD9:520: «el presupuesto de capacidad de la mantención, que el Capítulo 11 desarrolla». El Subdocumento 11 no se presenta en el Informe 2 y no figura en Referencias (SD9:537). ACL §7.1 d: «referencias a secciones o anexos inexistentes».
- SD9:400: «como muestra la matriz de cobertura del SD7, Figura 7.4». La Figura 7.4 del SD7 es «Fase 2 — Elaboración, primera parte: arquitectura, seguridad y sala técnica, cuentas 2.1 a 2.3» (SD7:81). La matriz de cobertura es la Tabla 7.2 (SD7:179) y su figura es la 7.16 (SD7:198, cuyo archivo se llama todavía `Fig_7-4_Cobertura_EDT`). La remisión quedó obsoleta tras la renumeración del SD7.

**H03 — Matriz 9.C desalineada con el T-12 (nuevo; ACL §7.1 c).** El conteo automatizado de AN9:140–784 contra T12 da 99 identificadores con «Cumple parcialmente» en el Anexo 9.C y «Cumple» en el T-12 (por ejemplo RF-02.06, AN9:156, frente a T12:27). La matriz reproduce los estados antiguos del T-12 (RF 136/44/1, RNF 64/24/2, RT 242/104/28); el T-12 vigente da RF 159/21/1, RNF 78/10/2 y RT 304/42/28. Los totales de casos no cambian (1.192 + 90 = 1.282, porque los 31 «No cumple» coinciden), pero la columna «Estado T-12» es falsa en el 15,3 % de las filas, y el expediente de aceptación del H12 promete «la matriz 9.C completa con el estado de prueba de los 645 identificadores» (T17:196).

### Altos

**H04 — El paso a producción de las Bases no es el del SD9, y las pruebas previas al H7 y al H12 no están planificadas (nuevo).**
- SD9:473 y T13:140 declaran que «el primer paso a Producción es el inicio de la marcha blanca (H6 y H11)». El E-25 define el H7 como «Paso a producción de la Etapa 1» (BA:1994) y el H12 como «Paso a producción de la Etapa 2» (BA:2005); el Art. 17.1 fija la producción en los meses 16 y 21 (BA:305, 308).
- Las pruebas que la BTT §20.1 exige «antes de cada paso a producción» (carga y estrés, resiliencia, seguridad ofensiva, accesibilidad; BTT:897–901), el RT-10.07 (BTT:557), el RT-11.20 (BTT:598) y el Art. 24 (BA:433–434) quedan como «repeticiones» sin fecha ni paquete: la Tabla T13.5 (T13:118–138) no tiene filas para ellas y la Tabla 9.7 (SD9:404–412) no les asigna HH.
- SD9:473 carga su costo «a la reserva de contingencia del riesgo R8-07». El T-15 establece que las reservas «no se programa[n] como trabajo» (T15:420), y la ficha de R8-07 (SD8A:146–163) trata un ataque o exposición de datos, con plazo «Antes H5/H10» (SD8A:155). Una prueba obligatoria no es la respuesta a un riesgo.
- El estrés y la accesibilidad, también exigidos antes de cada paso (BTT:897, 901), no figuran en la lista de repeticiones (SD9:473; T17:135, 195).

**H05 — Recuperación ante desastres por debajo de la frecuencia exigida en el primer año de Operación (nuevo).** El RT-07.07 exige «al menos dos veces al año» (BTT:423) y el Art. 20 «al menos semestral durante la fase de Operación» (BA:360). Las pruebas están en los meses 27, 33, 39, 45, 51 y 54 (SD9:514; T13:151; T14:1661). La Operación empieza en el mes 21 (BA:309). Recuento:
- semestre 1 de Operación (meses 21–26, oct-2028 a mar-2029): 0 pruebas;
- año 1 de Operación (meses 21–32): 1 prueba (mes 27);
- desde la última conmutación real previa (3.9.4, 19 al 26-05-2028, T15:662) hasta el mes 27 (abril de 2029) pasan unos 11 meses, contra la «separación máxima de seis meses» que el propio plan declara (SD9:514, 520).
El T-14 afirma «dos por año» (T14:1661), lo que es falso para el primer año.

**H06 — La Figura 9.9 contradice la Tabla 9.9, el T-13 y el T-14 (regresión respecto de la v2).** La Figura Mermaid muestra «Resiliencia oct-29», «Recuperación nov-29», «Resiliencia oct-30» y «Recuperación nov-30» (SD9:444–445, 450–451), es decir, los meses 33/34 y 45/46. La Tabla 9.9 fija resiliencia en 32 y 44 y recuperación en 33 y 45 (SD9:514–515), igual que T13:150–151 y T14:1661, 1681. La fuente `Diagramas/Fig_9-9_Calidad_Cronograma.drawio` tiene el mismo desfase: al mapear sus marcadores sobre la escala de meses se obtienen recuperación en 27, 34, 39, 46, 51 y 54, y resiliencia en 26, 33, 38, 45, 50 y 55. El texto que explica la figura (SD9:471, «ninguna prueba periódica de la Operación cae en un congelamiento») describe la figura, pero no la tabla, que pone dos resiliencias en septiembre (SD9:520).

**H07 — Plazos en días hábiles calculados sin feriados (nuevo).** El Art. 10.1 define los días hábiles «de lunes a viernes, excluidos los festivos» (BA:202). Las fechas límite y las reservas del T-15 (T15:492–499), copiadas en la Tabla 9.8 (SD9:481–486) y en las fichas del T-17 (T17:65, 77, 89, 101, 113, 149, 161, 173), se reproducen exactamente con lunes a viernes sin feriados. Recalculadas con los feriados legales de Chile:

| Hito | Fecha límite declarada | Fecha límite recalculada | Reserva declarada → recalculada | Holgura con observaciones |
| --- | --- | --- | --- | --- |
| H1 | 17-03-2027 | 16-03-2027 (Viernes Santo 26-03-2027) | 6 → 5 | −4 → −5 |
| H2 | 17-05-2027 | 14-05-2027 (21-05-2027) | 12 → 11 | 2 → 1 |
| H3 | 16-07-2027 (feriado de la Virgen del Carmen) | 15-07-2027 | 19 → 17 | 9 → 7 |
| H4 | 16-11-2027 | 16-11-2027 (1-11 en la reserva) | 19 → 18 | 9 → 8 |
| H5 | 17-01-2028 | 17-01-2028 (8-12 en la reserva) | 35 → 34 | 25 → 24 |
| H8 | 17-03-2028 | 17-03-2028 | 4 → 4 | −6 |
| H9 | 16-06-2028 | 14-06-2028 (20-06 y 26-06-2028) | 21 → 19 | 11 → 9 |
| H10 | 17-07-2028 | 17-07-2028 (15-08 fuera; 26-06 en la reserva) | 25 → 23 | 15 → 13 |

El equipo sí consideró el feriado del 1 de mayo para la fecha F1 del SD8 (registro de contexto), de modo que el criterio no es uniforme.

**H08 — La programación del pentest contradice el SD8 (nuevo).** El riesgo secundario de R8-07 establece que «las pruebas ofensivas sobre Preproducción pueden degradar un ambiente compartido; se programan fuera de las ventanas de certificación» (SD8A:161). El T-15 y el T-13 programan la seguridad ofensiva 3.8.6 del 21-10 al 09-11-2027 y la 3.9.5 del 19 al 26-05-2028, en paralelo con carga, resiliencia, recuperación ante desastres y despliegue en el mismo ambiente (T15:654–658, 661–665; T13:124–127, 133–136). Además, el T-13 exige «versión congelada en Preproducción» para el pentest (T13:79) mientras la resiliencia inyecta fallas en ese ambiente (T13:77).

**H09 — Calidad de datos ISO/IEC 25012 sin indicadores ni umbrales (nuevo).** SD9:89 afirma que «las siete dimensiones de ISO/IEC 25012 […] y sus 16 indicadores ya están definidos en el SD5, sección 5.2». El SD5 5.2.5 sólo enumera las dimensiones (SD5:370), y su lista de referencias aclara que la norma «no es fuente de umbrales numéricos» (SD5:592). Los 16 indicadores del SD5 (Anexo 5-H, Tabla A.18) son indicadores de negocio (OTIF, cobranza, costo por entrega), no de calidad de datos por dimensión. El Anexo 9.A no tiene ninguna métrica de datos (AN9:15–43). El Art. 23 exige calidad de datos conforme a 25012 «con […] indicadores de completitud y exactitud» (BA:419), y la sola mención de un estándar vale cero (ACL:57).

**H10 — Requisitos de terreno y de usabilidad sin prueba completa (nuevo).**
- El RT-13.08 del Caso exige operar «bajo lluvia y sobre 34 °C en verano, a una sola mano, con pantalla legible bajo sol directo» (CASO:745). El plan prueba sólo −22 °C con guantes (SD9:288; AN9:29; T13:75). No hay escenario de lluvia ni de calor. La matriz lo marca «Cumple parcialmente» (AN9:627) sin indicar qué queda fuera.
- El RT-13.04 pide tiempo máximo, número máximo de pasos, tasa de error y tiempo de aprendizaje «por perfil» (BTT:657). El T-12 lo declara «Cumple parcialmente […] umbrales a definir por el equipo» (T12:501). Aun así, el T-13 fija como criterio de salida «indicadores del RT-13.04 cumplidos» (T13:73), un criterio que no se puede verificar.

**H11 — Los dos ensayos de migración no tienen paquete ni fecha coherentes (nuevo).** La BTT exige «dos ensayos previos a la migración definitiva» (BTT:902). El SD9 promete «dos ensayos completos, 32,11 GB» (SD9:292) y el SD5, dos ensayos completos independientes (SD5:418, 473). Pero cada documento identifica otros paquetes:
- el T-13 programa un solo renglón, «Ensayos de migración en Preproducción», con el paquete 3.7.2 (T13:123);
- el T-14 define 3.7.2 como «Datos maestros cargados: 8.400 SKU, clientes e instalaciones» (T14:358);
- el T-15 llama «los dos ensayos» a 3.7.3 y 3.7.4 en diciembre de 2027 (T15:479), que el T-14 describe como los saldos de Talca y los de Concepción (T14:360, 362), es decir, dos cargas distintas y no dos ensayos completos.
El T-13 no programa 3.7.3, 3.7.4 ni el corte 3.7.5.

**H12 — HH de la Operación inverosímiles o ausentes (nuevo; prompt Paso 4 g).**
- El paquete 8.1.3 asigna 80 HH a seis conmutaciones regionales reales con medición de RTO/RPO e informe (T15:306, 896: «6 ocurrencias […] 13,3»), es decir, 13,3 HH por prueba. La prueba equivalente de certificación (3.8.5) tiene 320 HH (T15:212).
- La prueba anual de carga previa a septiembre (meses 31, 43 y 55) remite al «Paquete 8.2» (SD9:518), que es una cuenta. Ningún paquete del T-14 la contiene (T14:8.1.1–8.5.3), y la Tabla 9.7 no le asigna HH.
- Las resiliencias de la Operación están en 8.2.2, paquete del rol SEG (T14:1681), mientras el T-13 asigna su ejecución a CAL y SRE (T13:35).

### Medios

**H13 — El reparto del costo de la calidad no reproduce su descripción (nuevo).** SD9:184 incluye en prevención «la matriz de trazabilidad, el plan de calidad, las puertas automáticas» (1.2.4 + 1.5.1 + 1.5.2 = 240 HH), la usabilidad (720), la evidencia de INN-02 (960) y la deuda técnica (2.304). La suma da 4.224 HH, no 3.984. La cifra de 3.984 excluye las 240 HH de plan, matriz y puertas, que quedan dentro de las 6.864 de evaluación. El total de 10.848 HH es correcto (Tabla 9.7, SD9:406–412, contra T15:118–317).

**H14 — Fechas del T-13 distintas del T-15 (nuevo).** El T-13 afirma usar «las fechas de los paquetes del Formulario T-15, sección 6.1» (T13:110), pero programa 3.8.2 y 3.8.3 del 10 al 17-11-2027 (T13:128–129). El T-15 los programa del 21-10 al 17-11-2027 (T15:652–653) y explica que empiezan al terminar 3.8.1 (T15:476).

**H15 — Prueba de carga en Producción (nuevo).** La Figura 9.4 sitúa «Resiliencia y carga antes de cierre de etapa» dentro de Producción (SD9:265). El Art. 24 y el RT-09.06 exigen la carga «sobre Preproducción» (BA:433; BTT:539), y la Tabla 9.6 la ubica allí (SD9:285). La Tabla 9.9 no indica el ambiente de la carga anual (SD9:518).

**H16 — Autoridad sobre las puertas incoherente (nuevo).** La Tabla 9.5 permite que la Contraparte Técnica, «con acta», levante G5 cuando una prueba de la Tabla 9.6 no se aprueba o hay un defecto crítico o alto abierto (SD9:219). El texto dice, a renglón seguido, que «ningún hallazgo de seguridad crítico o alto admite excepción en ninguna puerta» (SD9:221), y el Art. 17.3 no admite incidentes críticos o altos abiertos (BA:320). Además, G6 no tiene fila en la Tabla 9.5, aunque el texto anuncia «lo que bloquea cada puerta» (SD9:209).

**H17 — La gobernanza de calidad no está en el SD1 ni en el SD6/T-9 (nuevo).** SD9:87 dice que el Comité de Calidad y Procesos «puede vetar una promoción (SD1, sección 1.3.1)». El SD1 sólo dice que el Comité «analiza la adherencia metodológica y métricas de defecto» (SD1:173). Los comités del proyecto en el T-9 son de Proyecto, Ejecutivo y de Operación (T9:66–68), además del de Arquitectura del T-10. El SD9 usa además un «Comité de Calidad» (SD9:109, 165, 392; T13:85) que no figura en esa gobernanza.

**H18 — La holgura ignora la segunda revisión del CLIENTE (nuevo).** La Figura 9.10 incluye una «Segunda revisión» después de la subsanación (SD9:497–499), pero la holgura resta sólo los 10 días de subsanación (SD9:488). Con revisión, subsanación y segunda revisión se necesitan 30 días hábiles. El H4 deja 9 (8 con feriados) para la segunda revisión, y el H1 y el H8 quedan negativos (BA Art. 18.3, BA:335).

**H19 — Momento de la aceptación provisional de R18-04 y R18-12 contradictorio (nuevo).** El T-17 registra la aceptación provisional de ambos en el acta del H12 (T17:225). El SD3 fija la de R18-12 «al cierre de la marcha blanca E1» (Anexos del SD3, línea 661), y el SD7 asigna R18-12 a «H7 y operación» y R18-04 a «revisión mensual en comité» (SD7, Tabla 7.11, líneas 491–494).

**H20 — Umbrales de desempeño incompletos (nuevo).** La Tabla 31 del SD4 fija 11 umbrales p95 (SD4:2907–2921). El Anexo 9.A cubre 7 (AN9:18–21). No tienen métrica ni prueba la navegación (1 s), la transacción crítica de terreno (3 s), la búsqueda compuesta (3 s; RF-17.11 ≤ 2 s) y el informe estándar (30 s), todos de la BTT §9.1.

**H21 — Códigos internos sin glosario en su primer uso (nuevo).** «SD3»/«SD4» (SD9:38, sin definir «SD»); «R8-18, R8-31 y R8-32» e «INN-02» (SD9:40, explicados recién en SD9:184 y 323); «H5 y el H10» (SD9:109, antes de vincular los hitos al E-25 en SD9:418); «G0–G6», «DRE» y «DORA» en la Figura 9.1 (SD9:61–64): G0–G6 se definen en SD9:192, DRE no se expande y DORA no aparece en el texto; «M1–M12 · INT-01–15» (SD9:359) no se expanden en el cuerpo. Es un indicio que el prompt asocia a la ACL §7.1 (códigos internos sin glosario).

**H22 — El T-12 no remite al SD9, al T-13 ni al T-17 (nuevo).** Ninguna fila del T-12 cita el SD9, el T-13 ni el T-17 en «Sección de la propuesta» (0 apariciones). Hay requisitos que el SD9 desarrolla y cuya sección apunta a otro documento: el RT-20.08 remite a «T-18 1» (T12:597), y el RT-04.11, el RT-09.06 y el RT-13.01 remiten al SD4, al SD6 o al T-14. Así se corta la trazabilidad requisito → sección que el SD9 afirma (SD9:369) y que exige el Caso 17.1 (CASO:823).

**H23 — Matriz 9.C genérica y sin criterio de aceptación (nuevo).** Los 175 RF con prueba propia tienen la misma prueba, «Sistema y aceptación de usuario» (AN9:140–284). La matriz no tiene columna de criterio de aceptación. Tampoco declara qué parte se verifica en los requisitos «Cumple parcialmente»: 73 según el T-12 y 172 según la propia matriz. El Caso 17.1 pide «prueba de verificación y criterio de aceptación» por requerimiento (CASO:823).

**H24 — Referencias sin correspondencia 1:1 (nuevo).** Faltan en la lista de referencias de los anexos (AN9:832–837) tres fuentes citadas: McCabe (AN9:66), «Martin» (AN9:69) y WCAG 2.2/W3C (AN9:28). La entrada «LafroX (2026) Subdocumentos 3, 4, 5, 6 y 9» (AN9:836) omite el SD1 (AN9:62), el T-12, el T-14 y el T-19, y el SD13 (INN-02, AN9:809). En el cuerpo, la entrada «Subdocumentos 1 a 8 y 13» (SD9:537) incluye el SD2, que no se cita, y deja fuera el Capítulo 11, que sí se cita (SD9:520). El T-13 cita ISO/IEC/IEEE 29119-3 (T13:3), que no está en ninguna lista. Norma infringida: ACL §6 (ACL:109–111).

**H25 — Determinismo de la reconciliación de stock sin criterio (nuevo).** El RT-03.13 del Caso exige que la sincronización del CD «resuelv[a] de forma determinista los conflictos de stock» (CASO:732). Los criterios de salida sólo miden tiempo, pérdidas y duplicados (T13:75; AN9:33).

### Bajos

**H26 — Capacidad de los evaluadores con otra productividad.** SD9:471 calcula 16 × 21 × 8 = 2.688 HH. El T-15 usa 6,4 HH efectivas por persona y día (T15:439), con lo que la capacidad sería 2.150,4 HH. La conclusión no cambia, pero las bases de cálculo deben ser las mismas.

**H27 — Herramientas fuera del inventario y regla no ejecutable.**
- eslint-plugin-sonarjs, `npm audit` y el SAST y Secret Detection de GitLab (SD9:158, 227; AN9:67, 74–75) no figuran en el SD4, el T-11 ni el Anexo 4-P.
- La regla 9B-09 asigna a PHPMD la complejidad cognitiva ≤ 15 (AN9:67), pero la configuración de PHPMD sólo define CyclomaticComplexity, NPathComplexity y ExcessiveMethodLength (AN9:96). Si la herramienta no mide esa métrica, el grupo no podrá explicar la regla (ACL:133).

**H28 — Severidad «alta» contraria al SD4.** SD9:392 define un defecto alto como el que «afecta un servicio de nivel alto sin alternativa». El SD4 define el nivel alto justamente porque «tiene una alternativa costosa» (SD4:2391).

**H29 — Formalidad pendiente o incompleta.**
- La declaración de IA del cuerpo agrupa los cuatro anexos en una fila (SD9:554); la ACL pide una fila por anexo (ACL:137).
- «## Referencias» de los anexos va seguida directamente de la lista, sin frase de introducción (AN9:830; ACL §3).
- Los anexos, el T-13 y el T-17 no tienen índice, y la ACL §9 lo exige «en cada documento» (ACL:178).
- 16 de 26 citas a las Bases del cuerpo no indican página (ACL:107). Queda pendiente del PDF.

**H30 — Imprecisiones menores.**
- La Figura 9.7 nombra el paquete «3.4.4 Cadena de frío y retiro sanitario» (SD9:360); en el T-14 es «Cadena de frío, retención de lotes y retiro sanitario» (T14:302).
- Las «cinco compuertas bloqueantes que define el SD6, sección 6.2.2» (SD9:209) están en el T-10 (T10:68–76).
- Los seis casos de contrato (SD9:300) omiten el caso «no responde» que el RT-10.08 distingue de error y lentitud (BTT:558).
- La ficha del H11 no fija tiempo para la reversión operativa (T17:183); la del H6 fija ≤ 40 min (T17:123).
- El informe de evaluación CMMI 2023 que cita el SD1 (SD1:299) no se distingue en las Referencias del SD9 (SD9:526), aunque SD9:95 se apoya en él.

---

## 3. Preguntas de la Comisión

| N.º | Pregunta | Respuesta / evidencia | Estado |
| --- | --- | --- | --- |
| 1 | ¿Aparecen exactos, en orden y con su texto, los títulos obligatorios del Capítulo 9? | Sí. «Introducción al Plan de calidad» (SD9:34), «9.1 Plan de Calidad» (SD9:42), «9.2 Estrategia de Aseguramiento de Calidad» (SD9:186), «9.3 Alineación con Plan de Trabajo» (SD9:394); cierre con «Referencias» (SD9:522) y «Declaración de uso de IA» (SD9:544). Coincide con ACL:320–332. | Respondida |
| 2 | ¿La introducción resume el capítulo y lo conecta con capítulos, anexos y formularios? | Sí, SD9:36–40 (SD3–SD8, SD13, Anexos 9.A–9.D, T-13 y T-17). | Respondida |
| 3 | ¿El T-13 y el T-17 se entregan como archivos propios y se citan donde se usan? | Sí. Se citan en SD9:9, 40, 277, 352 y 475. | Respondida |
| 4 | ¿Cada característica de ISO/IEC 25010 tiene una métrica y un umbral numérico de esta solución? | Sí: Tabla 9.2 (SD9:134–143) y 29 métricas en el Anexo 9.A (AN9:15–43). | Respondida |
| 5 | ¿Hay umbrales bloqueantes numéricos para cobertura, complejidad, acoplamiento y duplicación? | Sí: Tabla 9.3 (SD9:155–161) y 9B-01 a 9B-13 (AN9:59–71). | Respondida |
| 6 | ¿Con qué regla mide PHPMD la complejidad cognitiva ≤ 15? | La configuración sólo define ciclomática, NPath y longitud (AN9:96). No se explica cómo se mide (H27). | Sin respuesta |
| 7 | ¿El modelo de madurez está vigente al inicio del contrato y cómo se usa? | La evaluación CMMI vence en noviembre de 2026; se renueva con el H1 y, mientras tanto, rige ISO 9001 (SD9:95). TMMi se usa como autoevaluación en el H5 y el H10 (SD9:109). | Respondida |
| 8 | ¿La calidad de datos ISO/IEC 25012 tiene indicadores y umbrales verificables? | No. Se remite al SD5, que no los define (SD9:89; SD5:370, 592) (H09). | Sin respuesta |
| 9 | ¿Cada puerta dice qué bloquea y quién puede levantarla, incluida G6? | G6 no tiene fila, y G5 puede levantarla la Contraparte Técnica, contra SD9:221 (SD9:213–219) (H16). | Sin respuesta |
| 10 | ¿Las herramientas del pipeline son las mismas que en SD4, T-11, T-10 y Anexo 4-P? | Casi todas: SD4-Anexos:1048–1050; T10:58–61; T-11:112. Faltan eslint-plugin-sonarjs, `npm audit` y el SAST de GitLab por nombre (H27). | Respondida |
| 11 | ¿Las cargas de prueba se derivan del dimensionamiento? | Sí: 1,5 × 14,66 = 21,99 TPS; 1,5 × 775,33 = 1.163; 1,5 × 158 = 237; 3 × 14,66 = 43,98; 1,5 × 6,94 = 10,41 (SD9:294; SD4 Tabla 33, SD4:2958–2976). | Respondida |
| 12 | ¿Todas las pruebas de carga se ejecutan en Preproducción, como exige el Art. 24? | No consta. La Figura 9.4 pone carga en Producción (SD9:265), y la carga anual no declara ambiente (SD9:518) (H15). | Sin respuesta |
| 13 | ¿Con qué volumen almacenado (no diario) se carga la base de Preproducción en la prueba de carga? | Sólo se especifica el día de peak (AN9:802). No hay volumen de base de datos, aunque el SD4 proyecta 50,75 GB al año (SD4 Tabla 33). | Sin respuesta |
| 14 | ¿Los 11 umbrales p95 de la Tabla 31 del SD4 tienen métrica y prueba? | No: 7 de 11 (H20). | Sin respuesta |
| 15 | ¿Se prueba el RT-13.08 completo: lluvia, más de 34 °C y sol directo? | No; sólo −22 °C y guantes (H10). | Sin respuesta |
| 16 | ¿Los indicadores del RT-13.04 están definidos por perfil? | No. El T-12 dice «umbrales a definir por el equipo» (T12:501), y el T-13 igual los usa como criterio (T13:73). | Sin respuesta |
| 17 | ¿Cuáles son, y cuándo se ejecutan, los dos ensayos completos de migración? | T-13, T-14 y T-15 identifican paquetes distintos (H11). | Sin respuesta |
| 18 | ¿Los ambientes de prueba están libres de datos productivos sin anonimizar (Ley 21.719, Art. 21.4)? | Sí: SD9:306; AN9:790, 815–828; Macie y prueba de reidentificación; DR tratado como réplica productiva (T13:58). | Respondida |
| 19 | ¿La trazabilidad requisito–diseño–código–prueba–despliegue es coherente con el T-12? | La cadena existe (Figura 9.7, SD9:356–369), pero hay 99 estados desalineados (H03) y el T-12 no remite al SD9 (H22). | Sin respuesta |
| 20 | ¿Se reproducen los conteos 645 / 605 / 40 / 1.282 / 1.026 / 4,3 h / 64 HH? | Sí. El recuento automatizado da 645 filas, 1.192 casos (544 + 302 + 346) + 90 = 1.282; 56 × 5 + 160 × 3 + 43 × 2 = 846; 0,8 × 1.282 = 1.026; 1.026 × 0,5 / 60 = 8,55 h; 256 × 15 / 60 = 64 HH. Conciliación 259 + 9 + 3 = 271 (SD9:298). | Respondida |
| 21 | En los requisitos «Cumple parcialmente», ¿qué parte se verifica y se acepta? | No se declara en la matriz ni en el T-17 (H23). | Sin respuesta |
| 22 | ¿Las HH de calidad coinciden con el T-15 paquete por paquete? | Sí: 240 + 720 + 2.080 + 1.760 + 960 + 400 + 4.688 = 10.848; CAL = 4.656 (T15:118–317). | Respondida |
| 23 | ¿El reparto prevención / evaluación reproduce lo que describe el texto? | No: lo descrito suma 4.224 HH, no 3.984 (H13). | Sin respuesta |
| 24 | ¿Las pruebas obligatorias previas al H7 y al H12 tienen fecha, paquete, HH y ambiente? | No; se cargan a la reserva de R8-07 (H04). | Sin respuesta |
| 25 | ¿Qué hito es el «paso a producción»: el H6 o el H7? | El SD9 dice H6/H11 y el E-25, H7/H12 (H04). Requiere decisión. | Sin respuesta |
| 26 | ¿Los plazos en días hábiles excluyen los festivos (Art. 10.1)? | No (H07). | Sin respuesta |
| 27 | ¿La holgura de cada hito considera la segunda revisión del CLIENTE? | No (H18). | Sin respuesta |
| 28 | ¿La recuperación ante desastres cumple «dos veces al año» y «semestral» en todo el período de Operación? | No en el primer semestre ni en el primer año (H05). | Sin respuesta |
| 29 | ¿Alguna prueba que interviene Producción cae en un congelamiento? | La Tabla 9.9 y el T-13 ubican las resiliencias de septiembre entre el 26 y el 30 (SD9:520; T13:156), conforme al RT-10.05 del Caso (CASO:741). Pero el Caso 13.2 llama a septiembre «ventana de congelamiento total» (CASO:638), el SD4 cierra todo septiembre al despliegue (SD4:2318), y no se dice dónde se ejecutan las restauraciones mensuales de diciembre y de los tres primeros días hábiles (SD9:517; T13:154). | Sin respuesta |
| 30 | ¿La Figura 9.9 coincide con la Tabla 9.9 y con el T-14? | No, en cuatro pruebas (H06). | Sin respuesta |
| 31 | ¿La simultaneidad del pentest con la carga y la resiliencia en Preproducción es compatible con R8-07? | No (H08). | Sin respuesta |
| 32 | ¿Son verosímiles 13,3 HH por conmutación regional real en la Operación? | No se justifica (H12). | Sin respuesta |
| 33 | ¿La prueba anual de carga previa a septiembre tiene paquete y HH en el T-14 y el T-15? | No (H12). | Sin respuesta |
| 34 | ¿Los responsables nombrados coinciden con el SD1? | Sí: Miño, Líder de Calidad, meses 1–56 (SD1:255, 272); Henríquez, Líder Funcional (SD1:271); Aravena, JP (SD1:265). | Respondida |
| 35 | ¿La facultad de veto del Comité de Calidad tiene respaldo en el SD1 y el SD6/T-9? | No (H17). | Sin respuesta |
| 36 | ¿El momento de aceptación de los 16 resultados R18 coincide con el SD3 y el SD7? | 14 de 16 sí; R18-04 y R18-12 no (H19). | Sin respuesta |
| 37 | ¿Todos los códigos internos se definen en su primer uso? | No (H21). | Sin respuesta |
| 38 | ¿Hay correspondencia 1:1 entre citas y referencias en los cuatro archivos? | No (H24). | Sin respuesta |
| 39 | ¿Hay precios, tarifas o montos? | No: 0 apariciones de «$», «USD», «CLP» o «UF»; el costo de la calidad va en HH (SD9:184). | Respondida |
| 40 | ¿Hay indicios de la ACL §7.1 que dejen el subdocumento en 0? | Sí: H01, H02 y H03. | Respondida |
| 41 | ¿El cronograma respeta el Art. 17°? | Sí: marcha blanca E1 de febrero a abril de 2028 y E2 de agosto a septiembre de 2028 (SD9:432, 436); H6 en el mes 13, H7 en el 16, H11 en el 19 y H12 en el 21 (T17:125, 137, 185, 197). | Respondida |
| 42 | ¿El refuerzo de evaluadores es coherente con el SD6 y el T-15? | Sí en meses y tope (SD9:471; T15:480). La productividad usada difiere (H26). | Respondida |

**Balance: 16 preguntas respondidas y 26 sin respuesta.** Las 26 sin respuesta pasan al plan de correcciones.

---

## 4. Plan de correcciones

| ID | Origen | Archivo / sección | Acción concreta | ¿Decisión humana o del equipo? | Prioridad |
| --- | --- | --- | --- | --- | --- |
| PC-01 | H01, P40 | SD9 (Declaración); AN9 (Declaración); T-13; T-17 | Un integrante revisa cada sección y completa las 13 celdas con su nombre y lo que verificó; revisar si «Alto» refleja el uso real. | Sí (sólo integrantes) | P1 |
| PC-02 | H02 | SD9 9.3.3 (línea 520) | Quitar la remisión al Capítulo 11 o reemplazarla por el paquete del T-14 que contiene el presupuesto de capacidad (8.4.1). | No | P1 |
| PC-03 | H02 | SD9 9.3.1 (línea 400) | Cambiar «Figura 7.4» por «Tabla 7.2 y Figura 7.16 del SD7». | No | P1 |
| PC-04 | H03, P19 | AN9 9.C (Tabla 9.C.2) | Regenerar la columna «Estado T-12» desde el T-12 vigente (99 filas) y verificar que 9.C.1 y SD9 9.2.5 sigan cuadrando. | No | P1 |
| PC-05 | H04, P24, P25 | SD9 9.3.2; T-13 8.1; T-17 H7/H12; T-14/T-15 | Decidir si H7/H12 son los pasos a producción del E-25 (recomendado por BA:1994, 2005). Programar con fecha, paquete, HH y ambiente la carga y estrés, resiliencia, intrusión y accesibilidad previas al H7 y al H12, dentro de la línea base y no contra la reserva de R8-07. | Sí (definición y cambio del T-14/T-15) | P1 |
| PC-06 | H05, P28 | SD9 Tabla 9.9; T-13 T13.6; T-14 8.1.3; Fig. 9.9 | Rehacer el calendario de recuperación ante desastres para que haya al menos una prueba en cada semestre de Operación (meses 21–26 incluidos) y dos en cada año, sin chocar con resiliencia ni congelamientos. | Sí (elegir los meses) | P1 |
| PC-07 | H06, P30 | SD9 Figura 9.9 (Mermaid) y `Fig_9-9_Calidad_Cronograma.drawio` | Mover los marcadores a resiliencia sep-29/sep-30 (días 26–30) y recuperación oct-29/oct-30, o a los meses que fije PC-06; ajustar el texto de SD9:471. | No (salvo lo que fije PC-06) | P1 |
| PC-08 | H07, P26 | T-15 Tabla 5.2; SD9 Tabla 9.8; T-17 fichas | Recalcular fechas límite y reservas con los feriados legales (Art. 10.1), y propagar al SD7, SD8 y los resúmenes. | Sí (afecta la simulación del SD8) | P1 |
| PC-09 | H08, P31 | T-15 6.1; T-13 T13.5; SD8 R8-07 | Separar el pentest de las pruebas de carga y resiliencia en Preproducción, o reescribir el riesgo secundario de R8-07 con el control que se aplicará. | Sí | P1 |
| PC-10 | H09, P8 | SD9 9.1.1; AN9 9.A; SD5 5.2.5 | Definir métricas de calidad de datos por dimensión de 25012 (al menos completitud y exactitud), con umbral, punto de medición, prueba (migración y marcha blanca) y paquete; corregir la remisión al SD5. | Sí (umbrales) | P1 |
| PC-11 | H10, P15, P16 | AN9 9.A (9A-13, 9A-15); T-13 T13.3; SD9 Tabla 9.6; T-12 RT-13.04 y RT-13.08 | Agregar escenarios de lluvia, más de 34 °C y sol directo; definir los indicadores del RT-13.04 por perfil (tiempo, pasos, error, aprendizaje) y quitar «a definir por el equipo» del T-12. | Sí (umbrales por perfil) | P1 |
| PC-12 | H11, P17 | T-13 T13.5; T-14 3.7.x; T-15 5.2; SD9 Tabla 9.6 | Identificar los dos ensayos completos (paquete, fechas, ambiente, volumen) de forma única en T-13, T-14, T-15 y SD5, y programarlos en el T-13. | Sí | P1 |
| PC-13 | H12, P32, P33 | T-14 8.1.3, 8.2.x; T-15 4.3/6.1; SD9 Tablas 9.7 y 9.9 | Dimensionar las HH reales de cada conmutación de recuperación ante desastres en la Operación; crear o asignar el paquete de la carga anual con HH; ubicar las resiliencias de la Operación en un paquete SRE/CAL; recalcular la Tabla 9.7 y el costo de la calidad. | Sí (estimación) | P1 |
| PC-14 | H13, P23 | SD9 9.1.5 | Hacer que la descripción de prevención y evaluación coincida con 3.984 / 6.864, o recalcular ambas cifras (4.224 / 6.624) y el texto. | No | P2 |
| PC-15 | H14 | T-13 T13.5 | Corregir 3.8.2 y 3.8.3 a 21-10 → 17-11-2027 (T-15 6.1). | No | P2 |
| PC-16 | H15, P12 | SD9 Figura 9.4; Tabla 9.9 | Sacar la carga del bloque Producción de la Figura 9.4 y declarar el ambiente (Preproducción) de la carga anual. | No | P2 |
| PC-17 | H16 | SD9 Tabla 9.5 y Figura 9.3 | Agregar la fila G6; aclarar que el acta de la Contraparte Técnica es condición de G5 y no levanta fallas de prueba ni defectos críticos o altos. | No | P2 |
| PC-18 | H17, P35 | SD9 9.1.1; SD1 1.3.1; SD6 6.1.6 / T-9 | Decidir si existe un comité de calidad del proyecto con facultad de veto. Si existe, incluirlo en el SD1 y en la gobernanza del SD6/T-9; si no, corregir el SD9. | Sí | P2 |
| PC-19 | H18, P27 | SD9 9.3.2 y Tabla 9.8; T-15 5.5 | Explicar cómo se cubre la segunda revisión del CLIENTE o reconocer el riesgo con su control en el SD8. | Sí | P2 |
| PC-20 | H19, P36 | T-17 sección 3 | Alinear el acta de la aceptación provisional de R18-04 y R18-12 con el SD3 (Tabla 3.A.13) y el SD7 (Tabla 7.11), o corregir aquellos. | Sí (qué documento manda) | P2 |
| PC-21 | H20, P14 | AN9 9.A | Agregar métricas para navegación, transacción de terreno, búsqueda compuesta / RF-17.11 e informe estándar, con su prueba. | No | P2 |
| PC-22 | H21, P37 | SD9 (intro, 9.1.2, Figuras 9.1 y 9.7) | Definir en su primer uso SD, R8-xx, INN-02, H1–H12, G0–G6, DRE, DORA, M1–M12 e INT-01–15. | No | P2 |
| PC-23 | H22 | T-12, columna «Sección de la propuesta» | Agregar SD9, T-13 y T-17 en los RT de pruebas y aceptación (RT-04.04, 04.11, 07.07, 07.12, 09.06, 09.07, 10.07, 11.20, 13.01, 13.04, 20.08 y cap. 20). | No | P2 |
| PC-24 | H23, P21 | AN9 9.C; T-17 | Especificar la prueba por familia de RF (no una etiqueta única), agregar el criterio de aceptación o su remisión, e indicar el alcance verificado de cada «Cumple parcialmente». | Sí (alcance de los parciales) | P2 |
| PC-25 | H24, P38 | SD9, AN9 y T-13 (Referencias) | Agregar McCabe, Martin y W3C a los anexos; listar los subdocumentos y formularios efectivamente citados; agregar 29119-3 o quitar la cita. | No | P2 |
| PC-26 | H25 | T-13 T13.3; AN9 9A-19 | Agregar al criterio de salida la resolución determinista de conflictos de stock, con su caso de prueba. | No | P2 |
| PC-27 | P13 | SD9 9.2.3; AN9 9.D | Declarar el volumen de la base de Preproducción en la prueba de carga y su origen. | Sí | P2 |
| PC-28 | P29 | SD9 9.3.3; T-13 8.2 | Fundar la interpretación del 1–25 de septiembre frente al Caso 13.2 y al SD4 Tabla 14, o mover las pruebas; declarar el ambiente de las restauraciones de diciembre y de los primeros días hábiles. | Sí | P2 |
| PC-29 | P6, H27 | AN9 9.B; SD4 4.2.4.1 / Anexo 4-P; T-11 | Reemplazar PHPMD por una herramienta que mida la complejidad cognitiva en PHP, o quitar esa métrica para PHP; registrar sonarjs, `npm audit` y el SAST de GitLab en el SD4 y el T-11; confirmar la vigencia de PHPCPD. | Sí (herramientas) | P3 |
| PC-30 | H26, H28, H30 | SD9 9.3.2, 9.2.6, Figura 9.7, 9.2.1, 9.2.3; T-17 H11 | Usar 6,4 HH/día; alinear la severidad «alta» con el SD4 Tabla 16; nombre exacto de 3.4.4; citar el T-10 para las cinco compuertas; agregar el caso «no responde»; fijar el tiempo de la reversión operativa E2; citar CMMI (2023). | No | P3 |
| PC-31 | H29 | SD9 (Declaración); AN9 (Referencias, índice); T-13; T-17 | Separar una fila por anexo; agregar frase introductoria a las referencias de los anexos; agregar índice a los anexos y formularios; completar páginas de las citas en el PDF. | No (páginas: requiere el PDF) | P3 |
| PC-32 | P29 (SD1 1.3.2) | SD1 1.3.2; SD9 Tabla 9.9 | Decidir si la política corporativa de pentest semestral se aplica al contrato; si se aplica, el plan debe tener seis pruebas; si no, el SD1 debe decirlo. | Sí | P3 |

Prioridad: P1 = bloquea el puntaje o una causal; P2 = contradicción o brecha de requisito; P3 = forma o precisión.

---

## 5. Estado de los hallazgos de las revisiones anteriores

| Revisión | Hallazgo | Estado actual | Evidencia |
| --- | --- | --- | --- |
| v1 y v2 | 13 celdas `[[REVISIÓN HUMANA]]` | **No corregido** | SD9:550–556; AN9:845–848; T13:172; T17:233 |
| v1 y v2 | Citas a las Bases sin página | **Abierto** (16 de 26; pendiente del PDF) | SD9, citas «Distribuidora Puelche S.A., 2026a–c» |
| v1 | R18 sin glosario en las figuras | Resuelto | SD9:352 (R18-01 a R18-16); Fig. 9.6–9.7 |
| v1 | Tabla 9.4 con tres métricas DORA | Resuelto | SD9:176–179, 182 |
| v1 | «Seis de ocho» en 9.1.3 | Resuelto | SD9:145 |
| v1 | ISO/IEC 25012 e ISO 9001 sin referencia | Resuelto (pero ver H09: 25012 sin indicadores) | SD9:532–533 |
| v1 | G3 permitía levantar una vulnerabilidad alta | Resuelto (persiste la ambigüedad de G5, H16) | SD9:217, 221; AN9:49 |
| v1 | Fundamento de las pruebas antes de H7/H12 | **Parcial → reabierto como H04** | SD9:473; T13:140; BA:1994, 2005 |
| v1 | Siglas DES y otras en el T-13 | Resuelto | T13:20 |
| v1 | 26 días hábiles sin derivación | Resuelto | AN9:794 |
| v1 | Figuras Mermaid y `.drawio` distintas | **No corregido** (la 9.9 está desfasada en ambas versiones, H06) | SD9:444–451; Fig_9-9 |
| v1 | Pendientes cruzados 1–9 (SD1, SD3, T-12, T-14, SD6, T-15) | Resueltos, según la v2; se reconfirmaron SD1:185, 205 y T15:479 | — |
| v2 | Conciliación 261/259 y 10/9 | Resuelto | SD9:298 |
| v2 | Errata de puntuación en AN9:130 | Resuelto | AN9:130 |
| v2 | «R18» antes de definirse en la ficha H7 | Resuelto parcialmente: remite a la sección 3 | T17:134 |
| v2 | Resiliencias de septiembre (días 26–30) | Resuelto en texto y tablas; **regresión en la Figura 9.9** (H06) | SD9:520; T13:156 |
| v2 | Distinguir CMMI 2018 y la evaluación 2023 en Referencias | **No corregido** | SD9:526; SD1:299 |

Resumen: de 17 hallazgos previos, 10 están resueltos, 2 resueltos sólo en parte y 5 siguen abiertos o sin corregir (incluida una regresión). Esta revisión agrega 30 hallazgos (H02–H30; H01 es el arrastrado de las versiones anteriores), y el más grave entre ellos es la desalineación de la matriz 9.C con el T-12.

---

## CONSIDERACIONES TRANSVERSALES

- **Trazabilidad.** El retiro de lote en menos de 2 h se recorre completo: Caso cap. 18 → RF-09.01 (T12:96) → M9 → 3.4.4 (T14:302) → CP-RF-09.01-01 a -05 (AN9:225) → JD-07 (AN9:806) → R18-01 en el H7 (T17:208). La cadena se corta en el T-12, que no remite al SD9 (H22), y en el estado de 99 identificadores (H03).
- **Coherencia entre plan, equipo y arquitectura.** Las HH de calidad cuadran con el T-15 (10.848; CAL 4.656), pero la Operación tiene pruebas sin HH o con HH inverosímiles (H12). La gobernanza de calidad no está en el SD6/T-9 (H17).
- **Fundamentación ingenieril.** Las cargas, casos, presupuestos de error y costo total se reproducen. Fallan el reparto del costo (H13), los días hábiles (H07) y la frecuencia de recuperación ante desastres (H05).
- **Uso de IA.** Causal vigente: H01, H02 y H03. Además, varios pasajes son difíciles de defender en una interrogación (PHPMD cognitiva, 13,3 HH por conmutación, «primer paso a Producción» en el H6).
- **Cumplimiento.** No hay precios, plazos fuera del Art. 17° ni archivos mal nominados.
