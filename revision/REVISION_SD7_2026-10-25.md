# Revisión del Subdocumento 7 — coherencia con las Bases y con los demás subdocumentos

Fecha: 25-10-2026 · Rama revisada: `LafroX-Subdoc7-LateX` (commit `240e7e02`)

## Alcance y fuentes

- **SD7 completo:** `subdocumento-07/contenido.tex` y sus tablas, Anexos 7.A–7.F, Formularios T-14, T-15 y T-18 (fuentes y PDF compilados del 25-10 18:58).
- **Bases vigentes:** Bases Administrativas (Art. 17, 18, 37, 71, 78–80, Subdocumento 7, Formularios T-14/T-15/T-18 y E-25), Bases Técnicas Transversales (cap. 19–22), Caso 02 Logística (cap. 2, 10, 13, 14, 15, 17, 18 y 19) y **Aclaraciones de la Licitación** (que forman parte de las Bases).
- **Otros subdocumentos, en su rama más reciente:** SD1 (`LafroX-Subdoc1-LateX`), SD3 (`LafroX-Subdoc3-LateX`, incluido el T-12), SD4 (`subdoc-4`), SD6 (`LafroX-Subdoc6-LateX`), SD8 (`Lafrox_Subdocumento_8_Latex_Nuevo`), SD9 (`LafroX-Subdoc9-LateX`, T-13 y T-17) y SD13 (`LafroX-Subdoc13-LateX`, T-19).

> **Por qué importa la severidad.** Las Aclaraciones, sección 7.1, establecen que, desde el Informe 2, un capítulo con (c) contradicciones con otro subdocumento o (d) referencias a secciones o anexos inexistentes deja **todo el subdocumento como no presentado, con puntaje 0 y sin subsanación**. Por eso las referencias colgantes, que parecen detalles menores, aparecen aquí como críticas.

## Estado de las correcciones (25-10-2026)

**C1, C4 y A1 ya están corregidos en el T-15, el T-14, el T-18 y el SD7.**

| Hallazgo | Cambio aplicado | Resultado |
|---|---|---|
| **C1** | 4.3.4 pasa al 13–25-09-2028 (mes 20); 4.3.3 pasa al 02–11-10-2028 | H12: acta calculada el **25-10-2028**, con **+3 días hábiles** de holgura |
| **A1** | 2.4.2 se adelanta al 17–28-02-2028; 3.5.1–3.5.4 van del 15-03 al 28-04-2028, con máximo 5 personas por módulo | H8: 14 días de holgura. Pico de dotación: **64 personas en el mes 16** (antes 70 en el mes 15) |
| **C4** | Se reescribe el texto | La Etapa 2 sigue operando sin interrupción desde el primer día del mes 21 |

- **Cambios asociados:** 9.1.2 se programa en los meses 21–22. La estabilización 4.3.2 va del 26-10 al 22-11-2028.
- **Totales:** se mantienen las 220.023 HH. La Etapa 2 · marcha blanca pasa a 7.387,91 HH y el cierre a 2.694,54 HH.
- **Scripts:** `revision/recalcular_cpm_20261025.py` (CPM) y `revision/reprogramar_h12_e2_20261025.py` (curvas).
- **Pendiente:** las figuras de la Gantt deben reflejar estas fechas.

**Segunda pasada (pendientes propios del SD7):**

| Hallazgo | Resolución |
|---|---|
| **A2** | Se eliminaron los textos del escenario anterior (SD7, Anexos 7.B y 7.F, T-14). D-34 ya no condiciona la Etapa 2 al H12 |
| **M1** | La franja de los meses 16–20 se llama «Etapa 1 · Producción y estabilización»; «soporte puente» queda reservado a NOC + mesa (9.336 HH) |
| **M7** | La implementación abarca los meses 1–21; las HH de los meses 21–22 son la estabilización posterior al H12 (RT-20.06) |
| **M2** | El piloto queda del 09-11 al 20-12-2027 (meses 10–11), igual que el cálculo; se declara que no interviene sistemas en diciembre |
| **Holguras de la Etapa 1** | 3.4.10 pasa a los meses 5–9 y 3.8.7 a los meses 10–11 (`revision/ajustar_ventanas_e1_20261025.py`). **Ningún paquete queda con holgura negativa**; H4 y H5 siguen con 16 y 20 días |
| **Personas por paquete** | Se corrigió el promedio en 6 paquetes donde no alcanzaba para sus HH y se definió la columna en el T-15 |
| **M5** | Los títulos de las referencias siguen los nombres del T-7. Se agregaron SD1, SD2 y SD4 Anexos, y páginas a las citas del Caso. Cada cita tiene su entrada en la lista y viceversa |
| **M6** | F3 se divide en los tres subfrentes del SD3 §3.4.3 |
| **B1–B3** | Corregidos. F7 trabaja desde el mes 2 (diagnóstico 7.2.3) |
| **B5** | No aplica: «Líder de Calidad» es el nombre del Formulario T-8 |

**Siguen fuera de alcance por decisión del equipo:** C2 (numeración de tablas y figuras), C3 y A5 (SD8), figuras y A4 (nomenclatura de archivos).

## Resumen

| Severidad | N.º | Tema dominante |
|---|---|---|
| Crítica | 4 | Brecha del H12 fuera del mes 21; referencias colgantes a tablas o figuras; riesgos y anexos del SD8 inexistentes; activación de la Etapa 2 condicionada al acta |
| Alta | 6 | Construcción de la Etapa 2 poco creíble; textos desactualizados frente al T-15 vigente; SOC (SD6); nomenclatura de archivos; SD8 desalineado; T-17 desalineado |
| Media | 8 | Rótulos de HH, piloto y congelamiento, figuras sin cita, referencias APA, frentes del SD3, entre otros |
| Baja | 6 | Redacción y consistencia menor |

Lo que está bien se resume al final: el cronograma por meses, los hitos del E-25, las olas, la reversión, la estabilización y las cifras del caso están alineados con las Bases, el SD3 y el SD4.

---

## Críticos

### C1. El propio plan declara que el H12 no se cumple en el mes 21, y la brecha es autoinfligida

- **Dónde:** SD7 `contenido.tex:348`, `:359` y `:365–367`; T-15 `contenido.tex:44`, `:48` y `:176`; T-15 Tabla 7.8 (`tab_T15_7`, fila H12 con −4 días).
- **Choca con:** BA Art. 17.1 («toda oferta que proponga plazos distintos será declarada inadmisible»), Art. 37.1 (la garantía es condición de la aceptación final **del mes 21**) y Caso cap. 19 («que la ruta crítica sea creíble»).
- **Evidencia:** en `tab_T15_paquetes.tex:122`, el paquete **4.3.4 (garantía) no tiene predecesoras** («—»). Está programado del 02-10 al 10-10-2028 solo por su ventana, y 4.3.3 espera a 4.3.4. La misma Tabla 7.7 (`tab_T15_cpm_detalle.tex:123–124`) muestra las fechas tardías que resolverían el problema: 4.3.4 del 13 al 25-09 y 4.3.3 del 26-09 al 04-10. La garantía es un instrumento financiero y no interviene sistemas, por lo que el congelamiento de septiembre no la impide.
- **Propuesta:** reprogramar 4.3.4 en septiembre (mes 20) y preparar 4.3.3 en paralelo con las últimas semanas de marcha blanca. El expediente se entregaría a más tardar el 16-10, considerando el feriado del 09-10 y el del 27-10 de 2028. Con 10 días hábiles de revisión, el acta queda en el mes 21. Después hay que volver a correr `revision/recalcular_cpm_20261025.py` y actualizar la Tabla 7.8, la Figura 7.1 del T-15, la Figura 7.22 y el texto del SD7. Presentar una brecha negativa como «decisión pendiente del Comité Ejecutivo» es honesto, pero ante el evaluador equivale a ofrecer un plazo distinto del contractual.

### C2. Referencias a tablas o figuras que no existen en los PDF compilados

Los formularios y anexos compilados numeran todo como «Tabla 7.x» y «Figura 7.x»; no existen etiquetas como «Tabla 5.2», «T15.x» ni «T-18.x».

| Texto citado | Dónde | Destino real |
|---|---|---|
| «Formulario T-15, Tabla 5.2» | SD7 `:391`; Anexos `:69`; `tab_7F1` P7-02; también SD8 | T-15 **Tabla 7.8** (CPM y PERT de hitos) |
| «Formulario T-15, Figura T15.3» | SD7 `:83` | T-15 **Figura 7.3** |
| «Formulario T-18, Tabla T-18.1» | SD7 `:439` | T-18 **Tabla 7.3** (volumen) |
| «Tabla T15.1» | Texto **dentro de la imagen** `Fig_7-6_T15-2_Frentes_Trabajo.pdf` (Figura 7.21 del SD7 y Figura 7.2 del T-15) | T-15 Tabla 7.1 |
| «SD1, Tabla 1.1» como dotación técnica | T-15 `:200`; `tab_T15_8.tex:9–10` | En el SD1, la Tabla 1.1 es *Equipamiento*; la dotación es la **Tabla 1.3** |

- **Además:** como el SD7, los anexos y los tres formularios usan todos «Tabla 7.x», una cita como «Tabla 7.4» resulta ambigua entre archivos. Conviene que cada formulario use su propio prefijo, por ejemplo con `\renewcommand{\thetable}{T15.\arabic{table}}` en el T-15. Así las citas «T15.x» quedarían correctas sin reescribirlas.

### C3. El SD7 cita riesgos y anexos del SD8 que ya no existen

El SD8 vigente tiene los riesgos **R-001 a R-045** y solo los **Anexos 8.A y 8.B**.

| Cita | Dónde |
|---|---|
| R8-02 | SD7 `:522` |
| R8-01 | T-18 `:227` |
| R8-18 | T-15 `tab_T15_8.tex:9` |
| R8-27, R8-29 | T-14 `:1043` |
| «Anexo 8.E» | SD7 `:522` |
| «SD8, Anexo 8.D» | T-15 `:140` |
| «SD8, anexos 8.C–8.D, pp. 14, 16» | `tab_7F1.tex:1` (fuente del Anexo 7.F) |
| «Monte Carlo y fechas P80 del modelo de riesgos del SD8» | T-15 `:178`; el SD8 dice expresamente que su contingencia **no** es resultado de Monte Carlo |

- **Propuesta:** mapear cada código antiguo a su R-0xx vigente. Por ejemplo, el R-015 ya se corrigió en el commit `246e63fe`; los demás deben buscarse por contenido en el T-16. Hay que eliminar las menciones a 8.C, 8.D, 8.E y a Monte Carlo, o pedir al SD8 que esos anexos existan.

### C4. La Etapa 2 «se activa en Producción sólo tras la firma de H12»

- **Dónde:** T-18 `:174` y SD7 `:389` («la activación productiva de E2 queda condicionada al H12»).
- **Choca con:** BA Art. 17.2, punto 4 («El inicio de la fase de Operación en el mes 21 es simultáneo al paso a producción de la Etapa 2 y comprende ambos alcances **desde el primer día**») y con el propio SD7 `:486`, que cita correctamente esa regla.
- **Propuesta:** declarar que la Etapa 2 sigue operando sin interrupción desde la marcha blanca y que el mes 21 la cubre en Operación desde el día 1. El H12 formaliza la aceptación, pero no enciende la Etapa 2. Esto se resuelve casi por completo al corregir C1.

---

## Altos

### A1. La construcción de la Etapa 2 depende de una «ráfaga» de tres semanas poco creíble

- **Dónde:** `tab_T15_paquetes.tex:71–74` y `tab_T15_4_personas` (meses 13 a 15).
- **Hecho:** los cuatro módulos de la Etapa 2 (3.5.1 a 3.5.4, de 960 HH cada uno) se construyen todos entre el 03-04 y el 26-04-2028, en 17 días hábiles, con 8,3 personas en promedio y hasta 12 por módulo. En cambio, DES tiene **3 personas** en los meses 13 y 14 y salta a **25** en el mes 15. En la Etapa 1, un módulo equivalente tomó entre 41 y 75 días con unas 3 o 4 personas.
- **Riesgo:** el evaluador lo verá como productividad inconsistente (ley de Brooks) y como un pico de 70 personas inflado artificialmente. Esto debilita lo que piden el BA 17.2.1 (dotación suficiente en el solapamiento) y el Caso cap. 19 (ruta crítica creíble).
- **Propuesta:** iniciar la construcción comienzo-comienzo con el diseño preliminar del H8 (meses 13 y 14) y repartirla hasta el mes 16 con 4 o 5 personas por módulo. Después hay que recalcular la curva y el pico.

### A2. Textos del SD7 que contradicen al T-15 vigente

- **SD7 `:514`:** dice que «la sección 5 conserva la red y el PERT del escenario nominal anterior… requieren recálculo». Sin embargo, el T-15 `:44` y `:144` y el propio SD7 `:348` dicen que la sección 5 **ya** se calculó sobre las 220.023 HH. Hay que eliminar o reescribir ese párrafo.
- **SD7 `:389`:** da el acta H12 el **19-10-2028**, pero `:348` la da el **07-11-2028** dentro del mismo capítulo. Hay que unificar; tras corregir C1, debería quedar una sola fecha.
- **Anexos `:27` (7.B):** «En el escenario nominal histórico…» y «la identificación definitiva… requiere recalcular la red».
- **Anexos `:69` (7.F):** muestra reservas históricas (H1 6, H2 12, H3 19, H4 19, H5 35…). Los valores vigentes de la Tabla 7.8 son H1 5, H2 11, H3 17, H4 16, H5 20, H8 4, H9 19, H10 13 y H12 −4. P7-02 repite «4 a 35 días».
- **T-14 `:1103`:** «cálculo histórico de ruta crítica, en la sección 5» y «Reemplazan… a las figuras anteriores». Esas figuras ya no están, así que la cita apunta a contenido inexistente.
- **Nota:** las palabras «histórico», «pendiente de conciliación» (caption de `tab_T15_contingencia`, hoy no incluida) y «requieren recálculo» son los indicios que enumera la Aclaración 7.1(d).

### A3. SD6 contradice al SD7, al SD1, al SD4 y al T-12 sobre el SOC

- **SD6 §6.1.3:** «El servicio SOC 24x7 es condicional a su subcontratación; RT-11.17 presenta cumplimiento parcial porque la ubicación del SOC no está declarada».
- **SD7, T-15 `:96`, `tab_T15_8`, SD1 y T-12 (RT-11.17 = Cumple):** SOC **propio** de LafroX en Valparaíso desde el mes 13.
- **Corrección:** se hace en el SD6, no en el SD7. Además, el SD6 declara «La actualización del 24-10-2026 no cuenta con revisión humana registrada», lo que es un riesgo propio del SD6.

### A4. La nomenclatura de los archivos entregables no es uniforme

- **SD7:** `LafroX-Subdocumento7.pdf` y `LafroX-Formulario-T-14.pdf`.
- **SD1–SD6, SD9 y SD13:** `LAFROX-Subdocumento1.pdf` y similares.
- **SD8:** `LafroX-Subdocumento-8-Anexos.pdf` y `Lafrox-Subdocumento-T-16.pdf`, que además no sigue el patrón `EMPRESA-Formulario-T-X`.
- **Regla:** las Aclaraciones §1 establecen que un archivo mal nominado se considera **no presentado**. El equipo debe elegir una sola forma de escribir el nombre de la empresa y aplicarla a todos los archivos.

### A5. El SD8 no recoge lo que el SD7 le traslada

- **SD7 / Anexo 7.F:** afirma que el Capítulo 8 evalúa los supuestos P7-01 a P7-11, los registra en el T-16 y les asigna contingencia.
- **SD8 vigente:** no menciona ningún P7. Su contingencia es de 2.058,48 HH y su reserva de gestión de 1.600 HH; ninguna de las dos aparece en el SD7 ni en el T-15. Las Bases exigen el «reflejo» de las reservas en el cronograma (Subdocumento 8).
- **Además:** el SD8 cita «reserva de cronograma 4 a 35 días (T-15, Tabla 5.2)», un valor histórico que choca con el −4 actual.
- **Propuesta:** acordar con el SD8 dónde se citan los P7 y en qué parte del T-15 se refleja la contingencia de 2.058 HH. Puede ir como línea separada, fuera de la línea base.

### A6. El T-17 (SD9) usa fechas antiguas del T-15

- **T-17 §4.1:** dice que «el T-15 mantiene un escenario nominal de lunes a viernes sin feriados», lo que ya es falso.
- **Holguras de entrega del T-17:** H5 34, H9 19 y H10 23, con entregas el 29-11-2027 y el 12-06-2028.
- **T-15 vigente:** entrega del H5 el 01-12-2027 con 20 días, y entrega del H10 el 28-06-2028 con 13 días.
- **Propuesta:** el SD9 debe recalcular su tabla con el T-15 vigente, o con el que resulte después de corregir C1 y A1.

---

## Medios

### M1. «Soporte puente» tiene dos significados
La Tabla 7.4 del SD7 (`tab_SD7_13`) y la Tabla 7.4 del T-15 rotulan como «Soporte puente de la Etapa 1» la franja de los meses 16 a 20, con **14.824,31 HH**. El SD7 `:514` y el T-15 `:101` llaman «soporte puente» al NOC más la mesa, con **9.336 HH**. Conviene renombrar la fila, por ejemplo como «Etapa 1 en producción y soporte (meses 16–20)».

### M2. Piloto de frío: meses inconsistentes y solapamiento con el congelamiento de diciembre
- **Inconsistencia de meses:** `tab_T15_1.tex:10` dice «piloto de frío en 9–10»; el Anexo 7.F y las fechas (08-11 al 17-12-2027, o 09-11 al 20-12 según el cálculo) corresponden a los **meses 10 y 11**.
- **Congelamiento:** el piloto opera camiones reales durante diciembre, y la instalación de kits 6.5.x se extiende hasta el 14-01-2028. El Caso, cap. 10, restricción 8, prohíbe intervenir sistemas en diciembre.
- **Propuesta:** cerrar el piloto el 30-11 o declarar expresamente que no interviene sistemas productivos y que en diciembre no se hacen cambios.

### M3. Figuras que no se citan antes de aparecer
Las 17 láminas de la EDT (`fig:7-edt-fase-*`) y la Figura 7.24 de las olas (`fig:7-olas`, `:408`) no tienen `\ref`. Las Aclaraciones §4 exigen que cada figura «se cite en el texto antes de aparecer». Hay que añadir «La Figura \ref{…}» en el párrafo previo.

### M4. Recorte y ampliación de figuras
- **Texto en riesgo:** `:163` dice que la quinta lámina «amplía la cuenta 3.10». Las Aclaraciones §4 no aceptan «la ampliación de una sección de una imagen mayor como figura de detalle».
- **Propuesta:** si la lámina 5 es un diagrama dibujado aparte, cambiar «amplía» por «detalla». Si es un zoom, rehacerla.
- **Por verificar:** que todos los `trim=…clip` solo quiten márgenes en blanco, y que la EDT completa del T-14 (`:610`, a `1.18\linewidth`) y la red de precedencias (`1.12\linewidth`) respeten 9 pt y los márgenes.

### M5. Referencias APA incompletas e inconsistentes
- **Citas sin entrada en la lista** (Aclaraciones §6): SD1 (Capítulo 1, sección 1.5), SD2 (Capítulo 2, Anexo 2.2, S-09) y SD4 Anexos (LafroX, 2026l: Anexos 4-I y 4-W). Estas citas aparecen en el texto pero no en la lista del SD7.
- **Citas sin página:** las de las Bases como «(sección 13.3, condiciones 1 y 3)», «(sección 17.5)», «(sección 14.1)», «(capítulo 19)» y los RT sueltos.
- **Títulos distintos de los oficiales:** la lista usa «T-14: Estructura de desglose del trabajo», «T-15: Cronograma y asignación de recursos», «T-18: Implantación de la solución», «SD6: Metodología de desarrollo» y «SD7: Plan de trabajo». El propio T-15 se titula «Nivelación de recursos». Las Aclaraciones §3 exigen terminología idéntica.

### M6. Los frentes del SD7 no coinciden con los del SD3
El SD3 §3.4.3 describe **tres frentes** de construcción en la Etapa 1: bodega y calidad (M1, M2, M5, M9, M12); preventa, rutas y reparto (M3, M4, M6, M8); y datos y rendición (M7, M10). El SD7 y el T-15 tienen un único F3. Conviene declarar que F3 se organiza en esos tres subfrentes, o alinear el SD3.

### M7. El rótulo «Implementación meses 1 a 22» choca con el Art. 17
- **Dónde:** SD7 `:320` y la fila «Cierre y estabilización de la implementación 21 y 22».
- **Problema:** el Art. 17 cierra la implementación con la aceptación final del mes 21.
- **Propuesta:** presentar las 2.774 HH como estabilización posterior al paso a producción exigida por el RT-20.06, no como implementación del mes 22.

### M8. Tabla de reversión con celdas de oración completa
La Tabla 7.8 del SD7 (`tab_SD7_7`, columna «Qué hace») tiene celdas de oración completa. Las Aclaraciones §5 indican que si una celda necesita más de una frase, ese contenido va en texto. Conviene acortar las celdas a frases nominales.

---

## Bajos

- **B1.** `:67` dice «otros tres capítulos», pero enumera el Cap. 3, el T-18 §6, el Cap. 4 y el Cap. 6.
- **B2.** `:330` dice que «desde el mes 9 se suma la implantación», pero F7 figura como activo en los meses **8** a 21 en la Tabla 7.1 del T-15.
- **B3.** `:320` dice que «el SOC desde la primera marcha blanca del mes 13» forma parte de Operación (128.854 HH, meses 21–56). Esas HH de los meses 13 a 20 están en otras filas.
- **B4.** La Tabla 7.8 del SD7 asigna la reversión técnica al Líder de Operación/SRE, pero el SD4 §4.2.4.1.2 la declara **automática** por p95 o por tasa de errores. Se resuelve con «automática; supervisa SRE».
- **B5.** Rol con nombre distinto: el SD1 dice «Líder de Calidad y Pruebas» y el SD7 dice «Líder de Calidad».
- **B6.** La declaración de IA marca nivel Alto en todas las secciones y atribuye a Leandro Chamorro la verificación de «hitos, duraciones y ruta crítica». Debe quedar coherente con las correcciones de C1 y A1 antes de consolidarla en el A-6.

---

## Contrastes que salen bien

- Los meses del Art. 17, los doce hitos del E-25 y sus meses, y el orden H8 antes que H7 están correctos (Tabla 7.5).
- El calendario supuesto de febrero de 2027 es coherente con el SD3 §3.1.2 y con el hito de enero de 2029. Los feriados del script CPM aplican bien las Leyes 19.668 y 20.299 (09-10 y 27-10-2028).
- Las cifras del caso son correctas: 96 camiones (42 + 54), 28 con frío (18 + 10), 62 preventistas, 84 integrantes de la tripulación propia, unos 160 conductores de terceros, 1.400 y 2.600 entregas, 31.000 pedidos, 260.000 líneas, 1.150 recepciones, 38 % de rotación y 4 personas de TI.
- Las HH cuadran: la Tabla 7.4 del SD7 suma exactamente 220.023,00 = 216.951 + 3.072, y 3.072 = 8 × 384.
- Las olas, la convivencia, la estabilización (2 + 3 + 7 + 1) y el criterio de cuatro semanas coinciden con el SD3 §3.4.4. La reversión (≤10 min técnica y 40 min operacional) coincide con el SD3 y el SD4.
- Los congelamientos (1–25 de septiembre, diciembre y los tres primeros días hábiles) y la ausencia de paso a producción en septiembre y diciembre coinciden con el Caso cap. 10 y 13.3, el SD3 y el SD4 §4.2.4.1.4.
- La mesa (7 + 2 agentes, 2.283 y 2.391 contactos) y el SOC con 4 y luego 5 analistas desde el 26-04-2028 coinciden con el SD4 Anexo 4-W.7 y el T-12.
- Las innovaciones (paquetes y meses) coinciden con el T-19. Hay solo diferencias de grano fino: INN-01 y INN-03 se materializan en el mes 16 según el T-19.
- Los comités del Art. 71 (Proyecto quincenal; Arquitectura y Operación mensuales) y los RT-19.06 a 19.09, RT-20.01 a 20.08, RT-21.06 y RT-22.07 están cubiertos.
- Las secciones 7.1, 7.2 y 7.3 respetan el índice obligatorio de las Aclaraciones §11, y las tablas del cuerpo tienen 5 columnas o menos.

## Orden sugerido de corrección

1. **C1 y C4:** reprogramar 4.3.4 y 4.3.3, volver a correr el CPM y unificar las fechas del H12 en el SD7 y el T-15.
2. **A1:** repartir la construcción de la Etapa 2 y recalcular las curvas y el pico.
3. **C2 y C3:** corregir las referencias colgantes y los códigos del SD8; considerar el prefijo de numeración por formulario.
4. **A2:** eliminar los textos «históricos» del SD7, los Anexos 7.B y 7.F y el T-14.
5. **A4:** acordar la nomenclatura de archivos con todo el equipo.
6. **A3, A5 y A6:** avisar a los responsables del SD6, SD8 y SD9.
7. Resolver los puntos medios y bajos.
