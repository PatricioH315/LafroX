# Revisión de la Comisión — Informe 2 · Subdocumento 9 (v7, observaciones y verificación de la v6)

**LAFROX · GRUPO 2 · INFORME 2 · Caso 2 · Distribuidora Puelche S.A.**

**Archivos recibidos** (`09_plan_calidad/`): `LAFROX-Subdocumento9.md`, `LAFROX-Subdocumento9-Anexos.md`, `LAFROX-Formulario-T-13.md`, `LAFROX-Formulario-T-17.md`. Nomenclatura correcta, un formulario por archivo. Se cotejan con SD1, SD3, SD4, SD6, SD7, T-10, T-11, T-12, T-14, T-15, T-16 y con las Bases.

**Alcance de esta corrida.** Aplica `prompt_revision_comision_informe2.md` al estado actual del SD9 (después de aplicar la v6 y sus cinco pendientes). Verifica cada observación de la v6 y registra los defectos nuevos. Las referencias indican archivo y sección; las comprobaciones exclusivas del PDF (paginación, folio, firma, tamaño de letra, legibilidad de figuras) quedan pendientes. **El SD8 se está rehaciendo:** todo control que dependa de su registro de riesgos (códigos R8-nn, reservas, T-16) se marca *No verificable con el material recibido* (sección 4).

**Diagnóstico.** Puntaje actual **0/100** por la causal de indicios de IA (ACL §7.1 d): 16 celdas `[[REVISIÓN HUMANA]]` (SD9 10, Anexos 4, T-13 1, T-17 1). Contenido **sin esa causal: 40**. Pasa los nodos 1 a 6 del árbol (sin precios; formularios presentes; títulos del índice presentes; las contradicciones de diseño de la v6 están resueltas); queda en el nodo 7 porque las 10 figuras no están dibujadas como imagen y aún hay un vacío de trazabilidad en T-13 y una contradicción con el T-14. Con las observaciones N7-01 a N7-06 cerradas, el nodo 7 da 60.

Revisión sin el SD8: la cifra es provisional hasta verificar la sección 4.

---

## 0. Fuera del puntaje de contenido (igual dejan el ítem en 0)

- **Crítico — 16 celdas `[[REVISIÓN HUMANA]]`.** Sólo un integrante puede completarlas con la revisión que efectivamente hizo (plantilla en `Revision/plantilla_revision_humana_IA.md`).
- **Crítico condicionado — figuras.** Las 10 figuras del SD9 son bloques Mermaid sin imagen enlazada. AGENTS.md exige enlazar la imagen real; en `Diagramas/` sólo hay `.drawio`. Si el PDF no trae el dibujo aplica la ACL §7.1 a: «diagramas descritos en texto que no se dibujaron».

---

## 1. Verificación de la v6 (26 observaciones)

| Estado | Observaciones |
| --- | --- |
| **Corregido** (21) | N-01 (Tabla 9.5 y 9.2.1: G5 sólo H7/H12; correcciones por G0–G4 y G6), N-02 (regla de septiembre de 2028, SD9 9.3.2 y T-13 8.3), N-04 (instancias PRE-M/C/S/A, Tabla 9.11, SD4 4.2.4.1), N-05 (Tabla 9.13 con H1–H5, H8–H10; H8 en 0), N-06 (Tabla 9.12), N-07 (duplicación ≤ 3 %, G2), N-08 y N-09 (acoplamiento y cobertura de negocio en TypeScript), N-10 (CMMI-DEV v2.0 + OWASP SAMM), N-11, N-12 (99,95 %, 9A-17), N-13, N-14 (Tabla 9.7 y 29119-2), N-16 (10,41 TPS), N-17 (Playwright, Pact/Spectral, MobSF), N-18, N-19, N-20, N-21, N-22, N-23, N-24 |
| **Parcial** (4) | N-03 (restauración mensual desde el mes 13: ver N7-01), N-15 (matriz con escenario y CP-ID, pero 13 filas sin ambiente ni paquete: N7-11), N-25 (se retiró la autocita; 27 de 29 citas a las Bases siguen sin página: N7-10), N-26 (se corrigió la numeración; hay dos tablas nuevas de 6 columnas: N7-03) |
| **No corregido** (0) | — |
| **Sin comprobar** (1) | N-05 en su parte del SD8 (probabilidades de la Tabla 5.2 del T-15 con las reservas de H2 y H3 corregidas: N7-05) |

Hecho comprobado en esta corrida: el Anexo 9.C tenía cinco filas (`RF-14.01-BTT` a `RF-14.05-BTT`) sin escenario ni CP-ID; se completaron antes de esta revisión y la suma de casos vuelve a 547 + 302 + 354 = 1.203, más 105 de contrato = 1.308.

---

## Nivel 1 — Contradicción de diseño

**N7-01. La restauración mensual de los meses 13 a 20 no tiene paquete en el T-14.** El SD9 (9.3.2) dice: «la restauración de respaldos es mensual desde ese mes (RT-07.12) y no desde el mes 21: en la marcha blanca la ejecuta el SRE con el procedimiento del paquete 8.1.6». El T13.5 asigna esas ocho restauraciones al paquete 8.1.6. El T-14 define el 8.1.6 como «Mensual, meses 21 a 56», con «36 informes», y el T-15 lo programa en los meses 21–56. Los paquetes de la marcha blanca (4.2.1, meses 13–15; 4.3.1, meses 19–20) no incluyen restauraciones, y los meses 16–18 no tienen paquete de operación. El RT-07.12 exige la prueba «al menos mensual» desde que existen datos reales. *Se espera:* un paquete con meses 13 a 20, horas y responsable en T-14 y T-15 (o la extensión del 8.1.6 a los meses 13–56 con 44 informes), y la misma cifra en SD9 Tabla 9.14, T13.5 y Figura 9.9.

---

## Nivel 2 — Trazabilidad, capacidad y fundamento

**N7-02. El retiro sanitario en menos de 2 horas no tiene prueba en el T-13.** La trazabilidad del requisito crítico se corta en S9/T-13. El T-17 (R18-01) exige «Simulacro de retiro con un lote real, cronometrado (JD-07 en el ensayo previo)». El SD9 sólo menciona el simulacro en la Figura 9.7 (resultado R18-01). El T13.1 no tiene ese tipo de prueba, el T13.3 no tiene su criterio de salida y el T13.5 no tiene su fecha ni paquete. *Se espera:* un tipo de prueba «Simulacro de retiro», con criterio de entrada (JD-07), de salida (lista de clientes afectados en menos de 2 h), ambiente, paquete y fecha.

**N7-03. Dos tablas del cuerpo superan las cinco columnas.** La Tabla 9.12 (Etapa, Prueba, Ventana, Responsable, HH máximas, Financiamiento) y la Tabla 9.13 (Hito, Prueba o entregable, Entrega programada, Reserva, Subsanación, Holgura) tienen seis. El Paso 6 y la Aclaración §3 fijan un máximo de cinco en el cuerpo. *Se espera:* separar o fusionar columnas, o llevar el detalle a un anexo.

**N7-04. Las cuatro instancias de Preproducción no tienen capacidad declarada.** El SD4 dice que cada una se reconstruye con la misma topología, configuración y dimensionamiento que Producción, y que PRE-C, PRE-S, PRE-A y PRE-M coinciden en el tiempo (Tabla 9.11, 21-10 a 09-11-2027). Ni el SD4 ni el T-11 dicen cuántas instancias pueden existir a la vez ni cómo se dimensiona la carga a 1,5× en PRE-C junto con las demás. *Se espera:* tope de instancias simultáneas y la capacidad total declarada en SD4 y T-11 (en unidades, sin precios).

**N7-05. Las reservas corregidas de H2 y H3 no recalculan las probabilidades.** El T-15 (nota bajo la Tabla 5.2) dice que los límites pasan a 14-05-2027 (reserva 11) y 15-07-2027 (reserva 18), y que las probabilidades se recalculan «al confirmar el calendario». La Tabla 5.2 sigue con 97,4 % (H2) y 88,3 % (H3), calculadas con 12 y 19. El H8 queda con holgura 0, y su probabilidad (91,1 %) no incorpora la subsanación de 4 días. *Se espera:* la tabla recalculada con las reservas que declara el propio T-15 (depende del SD8, ver sección 4).

**N7-06. Los umbrales propuestos por LafroX no tienen fundamento.** Duplicación ≤ 3 % (Tabla 9.3), inestabilidad ≤ 0,5 (9A-25), utilización ≤ 70 % (9A-09) y regresión ≤ 10 % (9B-19) se declaran «supuesto», pero ninguno cita una fuente ni un cálculo. La Comisión puede preguntar por qué 3 % y no 5 % (Paso 1.2: lo que el grupo no podría explicar). *Se espera:* una frase por umbral con su origen: referencia publicada, práctica de LafroX con su fuente (SD1) o línea base medida.

**N7-07. La DR del mes 21 coincide con el cierre del H12 y no figura en él.** El T-14 8.1.3 y el SD9 Tabla 9.14 programan la primera recuperación ante desastres en el mes 21 (octubre de 2028). La ficha H12 del T-17 no la menciona entre sus criterios ni su evidencia, y ningún documento fija en qué día del mes cae respecto del acta. *Se espera:* decidir si la DR del mes 21 es parte de la evidencia del H12 o se programa después del acta, y reflejarlo en T-17 y T13.5.

---

## Nivel 3 — Forma y redacción

**N7-08. La Tabla 9.5 mezcla puerta y flujo.** La fila «G0–G4 y G6, con repetición de la prueba afectada» ocupa la columna «Puerta», y G6 aparece también en su fila propia. La Figura 9.3 no dibuja la ruta de las correcciones de marcha blanca. *Se espera:* una fila «Corrección de marcha blanca» con su momento y la figura actualizada.

**N7-09. Cita de sección incorrecta en la Tabla 9.12.** La reserva protegida de la Etapa 1 (128 HH de CAL por mes, meses 13–20) está en el T-15, sección 4.1, y la fuente de la tabla cita «sección 4.5». *Se espera:* citar 4.1 para la reserva protegida y 4.5 para la de contingencia.

**N7-10. Citas a las Bases sin página.** En el cuerpo del SD9, 27 de 29 citas «(Distribuidora Puelche S.A., 2026a…c, …)» no indican página (2 la traen). Es el Paso 6: «citas a las Bases con documento, capítulo o artículo y página». Sólo se resuelve con el PDF de las Bases.

**N7-11. Trece filas de la matriz 9.C no tienen paquete.** RT-23.01 a RT-23.10 y RT-25.01, RT-25.03 y RT-25.08 dicen «Documento de la oferta | Sin paquete de la EDT | Presentación de la oferta». «Presentación de la oferta» no es un hito del E-25 ni del Art. 18. *Se espera:* paquete o hito real, o declarar el criterio de verificación fuera de la matriz con su justificación.

**N7-12. Marcador literal «borrador».** El SD9 (9.3.2) escribe «su control es el borrador anticipado» y el T-15, sección 5.5, usa «borrador». La lista del Paso 1.2 incluye «borrador» entre los indicios. *Se espera:* «versión preliminar» en todos los documentos (SD9, T-15, T-16, T-17, SD8-Anexos).

**N7-13. Binarios desfasados.** `Diagramas/LafroX-Calculos-SD9.xlsx` (Calendario: 6 DR, 29 métricas, 23 reglas), `Fig_9-9.drawio` (DR sin el mes 21), `Fig_9-1.drawio` (umbrales y reglas) no reflejan el Markdown. La Figura 9.9 ya tiene 48 líneas Mermaid; en el PDF arriesga quedar bajo 9 pt.

---

## 4. Dependencia del SD8 (no verificable mientras se rehace)

El SD9 cita el registro del SD8 y el T-16 en estos puntos. Al terminar el SD8 hay que repetir la comprobación:

| Cita en el SD9 / T-13 / T-17 | Qué debe seguir siendo cierto |
| --- | --- |
| Intro SD9: R8-18, R8-31, R8-32 | Mismos códigos y títulos |
| Tabla 9.7 (R8-01 a R8-07, R8-16, R8-23, R8-27) | Códigos, títulos y plazos del T-16 |
| Tabla 9.12 (R8-18) y 9.3.2 («153,6 HH esperadas de R8-31») | Reservas, HH y la cifra 153,6 del Anexo 8.A |
| Tabla 9.13 y T-17 1.2 (R8-12: 5 días en H1, 4 en H8) | Texto de R8-12 y E8-11 |
| 9.3.2, regla de septiembre: «Anexo 8.A» y disparadores de H12 | Misma lógica de reservas |
| Referencia al T-16 en T-13 6 («disparador del riesgo correspondiente») | Riesgo y disparador existentes |

---

## Ruta a 60

1. **Cerrar N7-01 a N7-02.** Son la contradicción con el T-14 y el corte de trazabilidad del requisito crítico; con ellos abiertos el diagnóstico no pasa de 40.
2. **Cerrar N7-03 a N7-07.** Completan cálculo, capacidad y fundamento; dejan sólo faltas menores.
3. **Limpiar N7-08 a N7-13.** Forma y redacción.
4. **Fuera del puntaje, pero imprescindible:** las 16 celdas de revisión humana y la imagen de las 10 figuras.
5. **Re-verificar la sección 4** cuando el SD8 esté terminado.

| Ítem | Peso | Puntaje actual | Sin la causal (hoy) | Meta |
| --- | --- | --- | --- | --- |
| 9. Plan de calidad (T-13, T-17) | 8 % | 0 | 40 (provisional hasta verificar el SD8) | 60 |
