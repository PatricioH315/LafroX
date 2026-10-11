# Revisión de la Comisión — Informe 2 · Subdocumento 9 (v4)

**LAFROX · GRUPO 2 · INFORME 2 · Caso 2 · Distribuidora Puelche S.A.**

**Archivos recibidos** (`09_plan_calidad/`): `LAFROX-Subdocumento9.md` (611 líneas), `LAFROX-Subdocumento9-Anexos.md` (881), `LAFROX-Formulario-T-13.md` (199), `LAFROX-Formulario-T-17.md` (256). Nomenclatura conforme (Aclaraciones §1); un formulario por archivo. Los `.drawio` de `Diagramas/` no son entregables por sí mismos.

**Documentos revisados:** Subdocumento 9 (10 figuras Mermaid, 9 tablas numeradas y 3 sin número), Anexos 9.A–9.D, T-13 y T-17, contrastados con SD1, SD4, SD5, SD8, T-14 y las Bases. Rutas: SD9 = cuerpo; AN9 = anexos; T13/T17 = formularios; T14 = `07_*/…T-14`.

**Alcance de esta edición.** Revisión de fuente Markdown. Paginación, índice paginado, folio, firma, tamaño tipográfico, legibilidad de figuras y texto seleccionable quedan **pendientes del PDF final**. SD1, SD4, SD5, SD8 y T-14 se usaron sólo para cotejar cifras y decisiones.

---

## 1. Puntaje

### 9. PLAN DE CALIDAD — Formularios T-13 y T-17 (8 %)

**Revisión: (Puntaje 0)**

**Veredicto.** El subdocumento se tiene por no presentado. Hay 16 celdas `[[REVISIÓN HUMANA]]` (SD9 10, AN9 4, T13 1, T17 1), y el cuerpo comenta esas marcas dentro del texto entregable. Desde el Informe 2 cualquier indicio de la letra d deja el ítem en 0 sin subsanación (ACL §7.1). Sin esa causal, el diagnóstico de contenido es **20**: el núcleo (umbrales bloqueantes numéricos y estrategia 29119 propia) existe, pero el SD9 contradice al T-14 en 11 de 12 pruebas semestrales y deja sin paquete, fecha ni HH las pruebas obligatorias previas a H7 y H12.

Ponderado: 0 × 8 % = **0,0**.

---

## 2. Hallazgos

### Críticos

**C1 — 16 celdas de revisión humana vacías (No corregido, v1–v3).** SD9:602–611 (10), AN9:878–881 (4), T13:199, T17:256. Todas declaran nivel «Alto» en texto. ACL §7.1 d y §7.2. Sólo un integrante puede completarlas.

**C2 — Notas de proceso dentro del texto entregable (nuevo; ACL §7.1 d).**
- SD9:391: «La inspección no acredita la ejecución de las pruebas descritas ni reemplaza la revisión y el acta del CLIENTE.»
- SD9:403: «Las marcas de revisión humana pendientes no se completan por esta inspección ni se presentan como conformidad.» El cuerpo habla de sus propias marcas pendientes.
- SD9:440 («no inventa una medición favorable») y SD9:522–524 («no presenta como ejecutadas ni cubiertas actividades sin evidencia») están escritos como cautelas del redactor, no como compromisos del proponente.
- SD9:102: «Esta guía […] no modifica sus atribuciones.» Es una aclaración de auditoría, no contenido del plan.

**C3 — Fechas semestrales contradicen al T-14 (nuevo respecto de v3; contradicción entre subdocumentos).** SD9 Tabla 9.9 (SD9:565–567), Figura 9.9 y T13:167–168 fijan recuperación ante desastres en los meses 24, 30, 36, 42, 48 y 54 y resiliencia en 23, 29, 35, 41, 47 y 53. El T-14 fija recuperación en «Meses 27, 33, 39, 45, 51 y 54» (T14:1661) y resiliencia en «26, 32, 38, 44, 50 y 55» (T14:1681). Coinciden en cantidad y en un solo mes (el 54 de la recuperación); las otras 11 fechas difieren. El T13:173 afirma que las cantidades «coinciden con los entregables» del T-14, y la coincidencia es sólo numérica. La nota de contexto del 10-10 ya lo reconoce como «pendiente de propagar»; mientras no se propague, el SD9 es el que contradice.

**C4 — Certificación de cierre de H7 y H12 sin paquete, fecha ni HH (Parcial respecto de v3-H04).** T13:157 hace obligatorias, antes de H7 y H12, la intrusión por tercero, la resiliencia y la carga sobre la versión de cierre, y SD9:522 añade DR real y accesibilidad. SD9:524 reconoce que la Figura 9.9 «no desglosa fechas ni HH de las repeticiones de cierre». La Tabla T13.5 (T13:137–155) no tiene una sola fila con fechas para H7 o H12. Una exigencia declarada obligatoria y a la vez no planificada es una brecha del plan, y el SD9 la confiesa en lugar de cerrarla.

### Altos

**A1 — Ambiente de la seguridad ofensiva y de la resiliencia, contradictorio (Parcial respecto de v3-H15).**

| Fuente | Ambiente de la prueba de intrusión |
| --- | --- |
| Figura 9.4 (SD9:282) | Producción («Pentest por tercero») |
| Tabla 9.6 (SD9:308) | PREPROD |
| T13 Tabla T13.2 (T13:70) | Producción («prueba de intrusión anual») |
| T13 Tabla T13.3 (T13:96) | «Versión congelada en Preproducción» |

La Figura 9.4 pone también la resiliencia en Producción (SD9:283) y la Tabla 9.6 en PREPROD. Una decisión de ambiente debe tener una sola versión en los cuatro puntos.

**A2 — Cinco campañas en un ambiente y 6 días hábiles (No corregido, v3-H08).** T13:141–144 (21-10 a 09-11-2027) y T13:150–153 (19 a 26-05-2028) programan seguridad ofensiva, carga con resiliencia, recuperación y despliegue sobre el mismo Preproducción al mismo tiempo. Para la Etapa 2 son 6 días hábiles. El T13:96 exige «versión congelada» para el pentest, y la resiliencia inyecta fallas en ese mismo ambiente. Según v3, el SD8 (R8-07) pide programar las pruebas ofensivas fuera de las ventanas de certificación (cita tomada de v3; no re-verificada aquí).

**A3 — Holgura de los hitos ignora la segunda revisión y los feriados (No corregido, v3-H07 y H18).** La Tabla 9.8 (SD9:530–537) repite exactamente las mismas cifras que v3 (6/−4, 19/9, 35/25, 4/−6, 21/11, 25/15). La Figura 9.10 incluye revisión, subsanación y segunda revisión (30 días hábiles), pero la holgura resta sólo los 10 de subsanación. H1 y H8 quedan en −4 y −6 con un remedio (revisión anticipada) que no suma días a la reserva.

**A4 — Diciembre: el texto prohíbe lo que el calendario programa.** SD9:559 dice que las pruebas se fijan «fuera del congelamiento […] de diciembre». La Tabla 9.9 programa resiliencia en los meses 23, 35 y 47 (diciembre de 2028, 2029 y 2030) y T13:148 el ensayo de reversión en diciembre de 2027. SD9:520 y T13:173 lo salvan con «en Preproducción», pero la frase general de 9.3.3 es falsa tal como está escrita.

**A5 — Alcance de G5 en Operación sin definir.** La Tabla 9.5 exige en G5 «Prueba de la Tabla 9.6 no aprobada» como bloqueo del paso a producción, y la Tabla 9.6 incluye DR con conmutación real y pentest. La Tabla 9.4 fija una cadencia quincenal de despliegue. El documento no dice si cada versión quincenal repite esas pruebas ni qué puerta, G5 o G6, rige para ellas.

### Medios

- **M1 — Tres tablas sin número ni título.** «Guía de control y evidencia» (SD9:93), la tabla de «Mejora continua» (SD9:432) y la de «Control documental» (SD9:393). La primera además sigue a su título sin frase introductoria (SD9:91). El resto de las tablas del cuerpo lleva «Tabla 9.n — … Fuente: …» (ACL §4).
- **M2 — Figura 9.1: «24 umbrales bloqueantes» (SD9:60).** La Tabla 9.3 define 7 métricas de código. El 24 corresponde a las reglas del Anexo 9.B (9B-01 a 9B-24), que incluyen secretos, vulnerabilidades y regresión de p95.
- **M3 — Figura 9.9: la barra de H1 no coincide con la entrega.** SD9:474 extiende «Matriz y plan de calidad (H1)» hasta el 31-03-2027; la Tabla 9.8 entrega la matriz 1.2.4 el 09-03-2027.
- **M4 — Diez figuras Mermaid sin imagen enlazada.** AGENTS.md exige que toda figura enlace su imagen real; los `.drawio` existen, pero no se enlazan ni se referencian. Verificar en el PDF si las figuras quedan como imágenes (ACL §7.1 a).
- **M5 — Referencias.** (i) Orden APA: «International Organization for Standardization. (2015)» debe ir antes de las entradas con coautor (SD9:583–585). (ii) «CMMI Institute (2023)… SCAMPI A Appraisal Report N° 58190» es un informe de evaluación de LafroX, no una fuente publicada; el SD1:204 lo emite en noviembre de 2023 y el SD9:108 declara que vence en noviembre de 2026. No verificable con el material recibido; citar un certificado como referencia bibliográfica es inusual.
- **M6 — «Terreno» como sexto ambiente.** T13.2 tiene seis filas; el SD4 habla de cinco ambientes (DEV, QA, PREPROD, PROD, DR). El documento lo trata como ambiente de prueba separado; conviene que 9.2.4 lo diga una vez.
- **M7 — Capacidad de evaluadores sin la base del T-15 (según nota de contexto del 10-10; no re-verificado).** SD9:520 usa 21 días hábiles; el T-15 usa 20 días y el mes 10 supera la capacidad. El SD9 reconoce que el techo de 2.150,4 HH «no es una disponibilidad demostrada».

---

## 3. Correcciones de la revisión v3

| Hallazgo v3 | Estado en v4 | Evidencia |
| --- | --- | --- |
| H01 celdas de revisión humana | **No corregido** | 16 celdas (antes 13) |
| H02 remisiones a «Capítulo 11» y «Figura 7.4» | Corregido | Ahora remite a SD7 Tabla 7.2/Fig. 7.16 y a T-14 8.2.4/8.4.1 (SD9:448, 571) |
| H03 matriz 9.C vs T-12 | Corregido | 645 = 614 con prueba + 31 sin ella; 22 No cumple (2 RNF + 20 RT) y 15 parciales coinciden con el T-12 vigente (608/15/22) |
| H04 paso a producción y pruebas previas | **Parcial** | H6/H11 ya no se llaman paso a producción; las pruebas previas a H7/H12 siguen sin fecha (C4) |
| H05 DR del primer año | Corregido en SD9/T-13 | Primera DR en el mes 24; **el T-14 no se propagó** (C3) |
| H06 Figura 9.9 vs Tabla 9.9 | Corregido dentro del SD9 | Meses 23/24… coinciden en figura, tabla y T-13; el T-14 sigue distinto |
| H07 plazos sin feriados | **No corregido** | Tabla 9.8 igual |
| H08 pentest vs R8-07 | **No corregido** | A2 |
| H09 calidad de datos ISO 25012 | Corregido | AN9:70 define completitud, exactitud y consistencia con umbral |
| H13 reparto del costo de calidad | Corregido | 240 + 720 + 960 + 2.304 = 4.224; 2.080 + 1.760 + 400 + 2.384 = 6.624; 10.848 |
| H15 carga en Producción | **Parcial** | La carga está en PREPROD (Tabla 9.6); pentest y resiliencia siguen en Producción en la Figura 9.4 |
| H16 autoridad sobre puertas | Corregido | G5: «Nadie; se corrige»; el acta es condición adicional |
| H18 holgura y segunda revisión | **No corregido** | A3 |
| H21 siglas sin glosario | Corregido | SD, R8-nn, G0–G6, DRE, DORA, M y INT definidos en su primer uso |
| H26 productividad 6,4 HH/día | Corregido | 16 × 21 × 6,4 = 2.150,4 HH |
| H14, H17, H19, H20, H22–H25, H27–H30 | No re-verificados en esta pasada | — |

**Recuento de los 14 verificados:** 8 corregidos, 2 parciales, 4 no corregidos. La tabla de trazabilidad general del T-22 es del conjunto de la propuesta, no del SD9, y no se evalúa aquí.

---

## 4. Verificación de cálculos y consistencia (OK)

- **OK — Estructura.** 9.1, 9.2 y 9.3 con el texto exacto del índice obligatorio; «Referencias» y «Declaración de uso de IA» al final y sin numerar; la tabla de IA lista cada sección, anexo y formulario.
- **OK — Sin precios.** Búsqueda de `USD`, `CLP`, `UF`, `$`, `/mes`, CAPEX, OPEX y TCO: cero coincidencias en los cuatro archivos. Los costos van en HH.
- **OK — Sin marcadores de IA clásicos** (`[INSERTAR…]`, `[cite]`, `TODO`, `borrador`, «Cambios v…», nombres de archivo como fuente, ruptura de ficción). Los únicos indicios son C1 y C2.
- **OK — Casos de prueba.** 56 × 5 + 161 × 3 + 43 × 2 = 849; 849 + 354 + 105 = 1.308; 0,8 × 1.308 = 1.046; 1.046 × 0,5 / 60 = 8,7 h y 4,36 h con dos ejecutores; 262 × 15 / 60 = 65,5 HH; 271 = 260 + 9 + 2.
- **OK — Carga.** 14,66 × 1,5 = 21,99 TPS; 775,33 × 1,5 = 1.163 usuarios; 158 × 1,5 = 237 dispositivos; 6,94 × 1,5 = 10,41 TPS; 3× = 43,98 TPS.
- **OK — Presupuesto de error.** (1 − 0,999) × 1.440 × 30 = 43,2 min; 28, 29 y 31 días dan 40,32, 41,76 y 44,64.
- **OK — HH de calidad.** Tabla 9.7: 240 + 720 + 2.080 + 1.760 + 960 + 400 + 4.688 = 10.848 HH (5,0 % de 216.935). Los riesgos R8-31, R8-32 y R8-18 (153,6, 204,8 y 2.956,8 HH) coinciden con el SD8.
- **OK — 32,11 GB** de migración coincide con SD4 y SD5.
- **OK — Hitos.** H6/H11 como condiciones de entrada y H7/H12 como pasos contractuales de producción (mes 16 y mes 21), consistentes con T-17 y con el Art. 17.
- **OK — Calendario de Operación.** Los meses 23–31 de la Figura 9.9 mapean bien a dic-2028 … ago-2029 con el mes 1 = febrero de 2027; las cantidades (6 + 6 + 3 + 3 + 36) coinciden con T-13.
- **OK — Figuras y tablas.** Las 10 figuras y las 9 tablas numeradas se citan antes y se explican después. Ningún título carece de introducción, salvo el de M1.
- **OK — Disciplina de umbrales.** Cobertura 70 % negocio y 80 % global, ciclomática ≤ 10, cognitiva ≤ 15, duplicación ≤ 3 %, deuda ≤ 5 %, deptrac = 0, con herramienta y puerta. Se declara qué es supuesto de LafroX.

---

## 5. Pendientes del PDF final

Nomenclatura efectiva, portada, firma y foliación; índice con número de página y enlaces; tamaño ≥ 9 pt en figuras y ≥ 11 pt en cuerpo; tablas de más de una página o de más de 5 columnas (Tabla T13.3 tiene celdas de párrafo largas); páginas de las citas a las Bases (varias solo traen artículo o capítulo); páginas en blanco.

## 6. Qué se espera en el Informe 3

1. Completar las 16 celdas de revisión humana con la revisión efectivamente realizada, y retirar de SD9:391, 403, 440 y 522–524 las frases que comentan el proceso.
2. Propagar al T-14 (8.1.3 y 8.2.2) los meses 23/29/35/41/47/53 y 24/30/36/42/48/54, o devolver el SD9 y el T-13 a los meses del T-14.
3. Crear paquete, fechas, HH y responsables para la certificación de cierre de H7 y H12 en el T-14/T-15 y en la Tabla T13.5.
4. Fijar un solo ambiente para la intrusión y la resiliencia (Figura 9.4, Tabla 9.6, T13.2 y T13.3) y escalonar las campañas de 3.8 y 3.9 para no compartir Preproducción.
5. Rehacer la Tabla 9.8 con feriados y con la segunda revisión de 10 días, o justificar por escrito por qué H1 y H8 quedan negativos.
6. Numerar y titular las tres tablas sin caption; definir el alcance de G5 frente a la cadencia quincenal.

## CONSIDERACIONES TRANSVERSALES

- **Consistencia técnica.** La contradicción con el T-14 (C3) es la única de fondo entre subdocumentos; las cifras de volumen, HH y casos cuadran.
- **Trazabilidad.** El requisito «retiro de lote < 2 h» se sigue de R18-01 hasta la acta del H7 (Figura 9.7); se corta en el paquete 3.4.4, que no figura en la Tabla 9.7, porque los paquetes de calidad se agrupan por cuenta.
- **Uso de IA.** Dos tipos de indicio (C1, C2). Consecuencia: 0 sin subsanación desde el Informe 2.
- **Compliance.** Sin precios, sin plazos fuera del Art. 17°, nomenclatura correcta. Folio y firma: pendientes del PDF.
- **Correcciones.** De los 14 hallazgos de v3 re-verificados, 8 corregidos, 2 parciales y 4 no corregidos.

| Ítem | Peso | Puntaje | Ponderado |
| --- | --- | --- | --- |
| 9. Plan de calidad (T-13, T-17) | 8 % | 0 | 0,0 |
