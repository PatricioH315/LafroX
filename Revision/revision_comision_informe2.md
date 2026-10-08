# LAFROX · GRUPO 2 · INFORME 2 · Caso 2 · Distribuidora Puelche S.A.

**Revisión de la Comisión Evaluadora sobre fuentes Markdown.** Segunda corrida de `Revision/prompt_revision_comision_informe2.md` sobre la rama `rama-md`, con el estado del 8 de octubre de 2026, después de la auditoría de indicios de IA (`Revision/auditoria_indicios_IA.md`). Reemplaza la corrida del 7 de octubre, que sigue disponible en el historial de Git.

> **Alcance de esta corrida.** Se revisan sólo los subdocumentos presentes. El Subdocumento 9 y los Formularios T-13 y T-17 no se evalúan ni se penalizan como ausentes, por instrucción del usuario. Las comprobaciones exclusivas del PDF (nomenclatura efectiva, portada, firma, folio, índice paginado, tipografía, legibilidad y orientación) quedan pendientes de la compilación. Las referencias indican archivo y sección; no se citan páginas. El detalle de las contradicciones entre subdocumentos está en la planilla `Contradicciones_LafroX_Informe2.xlsx`, ubicada en la carpeta superior al repositorio, porque esta rama sólo admite archivos `.md`.

**Archivos recibidos:** `LAFROX-Subdocumento1` y `LAFROX-Formulario-T-6`; `LAFROX-Subdocumento2` y `-Anexos`; `LAFROX-Subdocumento3`, `-Anexos` y `LAFROX-Formulario-T-12`; `LAFROX-Subdocumento4`, `-Anexos` y `LAFROX-Formulario-T-11`; `LAFROX-Subdocumento5` y `-Anexos`; `LAFROX-Subdocumento6`, `LAFROX-Formulario-T-9` y `LAFROX-Formulario-T-10`; `LAFROX-Subdocumento7`, `-Anexos`, `LAFROX-Formulario-T-14`, `-T-15` y `-T-18`; `LAFROX-Subdocumento8`, `-Anexos` y `LAFROX-Formulario-T-16`; `LAFROX-Subdocumento13`, `-Anexos` y `LAFROX-Formulario-T-19`. Todos en `.md`; la nomenclatura del PDF queda pendiente. `13_innovaciones/innovaciones_corregidas.md` es un archivo de trabajo, no un entregable: no debe ir en el ZIP.

**Documentos revisados:** SD1 (315 líneas), SD2 (434 + 290), SD3 (432 + 757 + T-12 879), SD4 (2.853 + 1.697 + T-11 134), SD5 (629 + 1.782), SD6 (236 + T-9 + T-10), SD7 (697 + 232 + T-14 1.903 + T-15 1.180 + T-18 365), SD8 (206 + 760 + T-16 58), SD13 (700 + 130 + T-19 152).

---

## Causales duras (Paso 1)

- **Crítico — Marcadores sin completar en todas las declaraciones de IA (Aclaración §7.1 a).** Quedan 204 celdas `[[REVISIÓN HUMANA]]` en los 24 archivos entregables. Un cuadro de revisión en blanco es un marcador del tipo «[INSERTAR…]». Desde el Informe 2 deja el subdocumento completo en 0, sin subsanación. Lo afecta a todos: SD1 (Tabla 1.4, fila «1.5 Estructura Proy., Tabla 1.3») y SD2 (Anexos, fila «Correcciones de coherencia») tienen una sola fila pendiente cada uno; en los demás ninguna fila tiene revisor con nombre. Es la causal que hoy decide el puntaje. Se completa con `Revision/plantilla_revision_humana_IA.md`, sólo con revisiones que hayan ocurrido.
- **Crítico condicionado — Figuras que en la fuente son sólo descripción textual o lista (Aclaración §7.1 a, §4).** SD1 (Figura 1.1), SD2 (Figuras 2.1–2.6), SD3 (Figuras 3.1–3.4), SD7 (Figuras 7.1–7.12), SD8 (Figura 8.1, RBS) y SD13 (Figura 13.1) no enlazan ninguna imagen; la «figura» es un párrafo o una lista de viñetas. Si el PDF compilado desde LaTeX no trae el dibujo, la Comisión aplica la letra a): «diagramas descritos en texto que no se dibujaron». SD4 (26 enlaces) y SD5 (10 PNG) sí enlazan imágenes.
- **Precios (Art. 50.2): ninguno en la oferta.** OK - SD8 8.3.2 y SD13 13.x.5 expresan reservas e impacto en HH, rubros y meses; la valorización queda en la Oferta Económica. OK - El T-6 informa rangos de proyectos anteriores, campo propio del formulario.
- **Cronograma (Art. 17°): conforme en meses relativos** en SD3 Tabla 3.1, SD5 5.3.4, SD6 6.1, SD7 Tabla 7.5 y T-15. OK.
- **Formularios del ítem:** T-6, T-12, T-11, T-9, T-10, T-14, T-15, T-18, T-16 y T-19 están presentes. T-9 y T-10 siguen siendo tablas de remisión a secciones del SD6, sin contenido propio.

---

## CORRECCIONES DEL INFORME 1

**Tabla de trazabilidad (T-22; Art. 45):** parcial. Existen tablas de resolución por subdocumento en SD5 Anexo 5-K y SD13 Anexo 13.D. No existe la tabla general observación–respuesta–sección para General, S1, S2, S3, S4.1 y S4.2. La Comisión reconstruye esas correcciones desde el texto con la lista de control del prompt.

| Ítem | Corregido | Parcial | No corregido | No verificable |
|---|---:|---:|---:|---:|
| General | 2 | 3 | 0 | 2 |
| S1 | 6 | 1 | 0 | 1 |
| S2 | 9 | 2 | 0 | 0 |
| S3 | 9 | 2 | 0 | 1 |
| S4.1 | 7 | 1 | 0 | 0 |
| S4.2 | 10 | 1 | 0 | 0 |
| S5 | 4 | 1 | 0 | 0 |
| S13 | 4 | 2 | 0 | 0 |

**Cambios desde la corrida anterior:** se corrigieron la regla de precio (S-09, RNG-08, RF-03.11/12), el stack del SD1 (PHP/Laravel y Kotlin; SonarQube retirado), las notas de proceso señaladas («redactor», «sesión», «copia», «Base vigente de planificación», «versión anterior») y la ausencia de SD5 y SD13. **Regresión nueva:** ninguna.

---

## Transversal — Formalidad y contenido / Cumplimiento de instrucciones (3 %)

**Revisión: (No puntuado — forma pendiente del PDF)**

- Crítico: las 204 celdas `[[REVISIÓN HUMANA]]` (ver Paso 1).
- La introducción del SD3 no menciona sus anexos ni el T-12: «Responde a los tres problemas descritos en el Subdocumento 2 y se apoya en la estructura de proyecto del Subdocumento 1» (`LAFROX-Subdocumento3.md`, introducción). La Aclaración §11 exige conexión «con los demás capítulos, anexos y formularios». **No corregido (Informe 1).**
- T-9 y T-10 sólo remiten a secciones del SD6. El formulario «adjuntará … la información solicitada»; una tabla de punteros no la adjunta.
- SD4 marca 4.2 y 4.3 con `#` y 4.1 con `##`. Es un defecto de jerarquía que puede alterar el índice compilado.
- Leyendas «Fuente: elaboración propia.» sin fuente de datos: unas 50 en SD4 y varias en SD1, SD6, SD8 y SD13.

---

## 1. Presentación de la empresa — Formulario T-6 (3 %)

**Revisión: (Puntaje 0 — marcador IA) · Sin la causal: 20**

Veredicto: el subdocumento se tiene por no presentado por una sola celda: «1.5 Estructura Proy., Tabla 1.3 | Claude Code | … | Alto | Ninguno | [[REVISIÓN HUMANA]]». Corrigió el stack: «monolitos modulares en PHP y Laravel» y 48 desarrolladores «PHP/Laravel, móvil Kotlin» (Tabla 1.1). Sin la causal, queda en 20 por la contradicción de cobertura de pruebas con el SD6.

- OK - 1.1 a 1.6 presentes y en orden; T-6 con tres proyectos y la equivalencia cifra por cifra (Tabla 1.2).
- OK - Certificaciones con organismo, número, alcance y vigencia; alianzas coherentes con el híbrido.
- Contradicción (C-01 de la planilla): «rechazar cualquier compilación con cobertura de pruebas unitarias inferior al 80 %» (1.3.1) frente a 70 % de lógica de negocio y 80 % sólo del código modificado (SD6 6.2.2).
- La Figura 1.1 es una descripción textual sin imagen enlazada (ver Paso 1).
- CMMI-DEV vence en noviembre de 2026 e ISO/IEC 27001 en enero de 2027, ambos antes del inicio supuesto de febrero de 2027 (SD7 7.3.2). El documento declara la renovación, pero ningún riesgo del SD8 cubre su caducidad.
- 1.5 nombra al equipo nominado, que el índice asigna al Capítulo 12.

**Qué se espera en el Informe 3:** completar la revisión humana de la Tabla 1.3; un solo umbral de cobertura igual al del SD6; la figura del organigrama dibujada; evidencia del plan de renovación CMMI e ISO 27001.

---

## 2. Resumen ejecutivo, comprensión del problema y de la necesidad (6 %)

**Revisión: (Puntaje 0 — marcador IA) · Sin la causal: 60**

Veredicto: la única causal es una fila de los anexos: «Correcciones de coherencia | Codex | Alineación de S-09 … | Alto | Ninguno | [[REVISIÓN HUMANA]]». Corrigió la regla de precio: S-09 dice ahora «Rige el precio acordado al capturar el pedido», igual que SD3 y T-12. Es el subdocumento más limpio de la oferta.

- OK - 2.1 a 2.5 presentes; Tabla 2.1 con cálculos a la vista (1.400 × 0,042 = 58,8; 24 − 8 = 16); seis procesos AS-IS con análisis.
- OK - S-13 «No se instalan cámaras en cabina» es la versión correcta, y la siguen SD3 y SD4.
- Contradicción menor (C-20): la tensión 4 dice «La arquitectura que lo cumple se desarrolla en el Subdocumento 3». La arquitectura está en el SD4.
- Las seis figuras AS-IS son descripciones textuales (ver Paso 1).
- 2.4 no tiene matriz influencia–interés dibujada; 2.5.2 no resume ningún supuesto: sólo remite al Anexo 2.2. **No corregido (Informe 1).**

**Qué se espera en el Informe 3:** completar la revisión humana de la fila pendiente; corregir la referencia de la tensión 4; matriz de los 19 actores en figura; resumen de los supuestos críticos en 2.5.2.

---

## 3. Esquema de solución y alcance — Formulario T-12 (12 %)

**Revisión: (Puntaje 0 — marcador IA) · Sin la causal: 20**

Veredicto: las 19 filas de la declaración tienen `[[REVISIÓN HUMANA]]`, 18 de ellas en nivel «Alto». Desapareció la nota «redactor del Subdocumento 3». Sin la causal, el contenido queda en 20 por la contradicción de calendario con el SD7.

- OK - Regla de precio única (S-09, RNG-08, RF-03.11/12); promesa 24/48 h (RNG-15) idéntica en SD2, SD4 y SD5.
- OK - Estabilización calculada (158 / 24 ≈ 6,6) e idéntica en SD7 Tabla 7.10 y T-18.
- Contradicción (C-19): 3.1.2 declara que «los inicios en febrero, marzo, mayo, julio, agosto, octubre, noviembre y diciembre no generan conflicto» y admite diciembre de 2026. El SD7 (Tabla 7.6) muestra que con diciembre de 2026 el inicio de la marcha blanca E1 cae en diciembre, y que con febrero de 2027 el cierre de la marcha blanca E2 cae en el congelamiento de septiembre.
- La salida al conflicto sigue en V-17, «durante el período de consultas», que cerró el 01-09-2026 (T-20, N.º 4). Por el Art. 5.4, presentada la oferta rige la interpretación más exigente. **No corregido (Informe 1).**
- El T-12 sigue con cinco identificadores repetidos (RF-14.01 a RF-14.05): 181 filas RF y 176 identificaciones únicas.
- La introducción no conecta con los anexos ni con el T-12. Las Figuras 3.1–3.4 son descripciones textuales.
- La declaración llama «Regla provisoria» a RNG-04 y RNG-15.

**Qué se espera en el Informe 3:** revisión humana real por fila; un análisis de calendario idéntico al del SD7, que trate las marchas blancas además de los pasos a producción; reemplazar la dependencia de V-17 por una decisión propia; resolver las colisiones RF-14.xx.

---

## 4.1 Arquitectura lógica (7 %) · 4.2 Arquitectura física — Formulario T-11 (12 %)

**Revisión 4.1: (Puntaje 0 — marcador IA) · Sin la causal: 20**
**Revisión 4.2: (Puntaje 0 — marcador IA) · Sin la causal: 20**

Veredicto: las 29 filas de la Tabla 40 tienen `[[REVISIÓN HUMANA]]`. La declaración ya no contiene «Revisión final no realizada» ni «archivo de trabajo». Sin la causal, 4.1 queda en 20 porque los nombres de módulos no son idénticos a los del SD3, y 4.2 en 20 porque el SD8 declara insuficiente el tratamiento del RPO residual.

- OK - Monolito modular Laravel 13 / PHP 8.5 justificado para un equipo TI de 4; herramientas del pipeline idénticas a SD6 6.2.2; 16 dimensiones del 14.2 con memoria (Anexo 4-W); conmutación de 135 min (Tabla 39).
- OK - SD4 y SD5 coinciden en motores, retención (logs 12 + 24 meses, respaldos 35 días), manifiesto de 26 h, credenciales de 8/14 h, latencias ≤ 5 min / 2 h / 4 h y 10.920 mensajes térmicos diarios.
- Contradicción (C-11): la Tabla 3.4 del SD3 usa «M7 Cobranza y rendición», «M8 Devoluciones y envases» y «M9 Calidad y trazabilidad». El SD4 usa «M7 Rendición», «M8 Devoluciones» y «M9 Calidad» (Tabla 8 y Anexo 4-D, Tabla A.5), y «M4 Ruteo», «M5 Picking y carga», «M6 Entrega y POD» y «M9 Trazabilidad y frío» (Anexo 4-E, Tabla A.14). La Aclaración §11, 3.4, exige el mismo nombre en ambos capítulos.
- Contradicción (C-12): 4.3.2.4 deja como riesgo residual que la última copia remota supere 15 min y lo mitiga. SD8 8.3.3 y E8-05 dicen: «aceptar el riesgo no satisface Bases». RT-07.04 queda sin cumplimiento demostrado.
- Contradicción (C-13): el SD13 afirma que cada innovación se ubica en las capas y componentes del Capítulo 4 (RT-26.01). El SD4 no menciona ninguna innovación: cero coincidencias de «INN-» o «innovación» en cuerpo, anexos y T-11. Por ejemplo, el gateway B-02 no incluye el cálculo de vida útil de INN-03.

**Qué se espera en el Informe 3:** revisión humana documentada; nombres de módulos idénticos a la Tabla 3.4 en todas las tablas; cerrar el RPO residual en el diseño; incorporar las cinco innovaciones a 4.1 y 4.2.

---

## 5. Modelo y gestión de datos (6 %)

**Revisión: (Puntaje 0 — marcador IA) · Sin la causal: 40**

Veredicto: el SD5 se presenta y corrige la regresión de la corrida anterior, pero sus 34 filas de IA tienen `[[REVISIÓN HUMANA]]`. El contenido es técnicamente sólido y coherente con el SD4. Sin la causal queda en 40: la redacción es telegráfica y difícil de defender en una interrogación, y contiene una cifra calificada como contractual que las Bases no fijan.

- OK - 5.1 a 5.4 presentes; siete figuras PNG en el cuerpo y tres en el Anexo 5-M; diccionario atributo por atributo (5-A); EPCIS 2.0/CBV 2.0 con fuente.
- OK - ERP como único emisor, «no existe timbre diferido desde el móvil» (5.1.8). Volúmenes de migración con cálculo de tasas (5.3.4) y dos ensayos completos, en línea con SD7 7.3.2.
- Inconsistencia interna (indicio b): 5.2.6 dice «Umbral contractual ≤0,3 %», mientras 5.3.2 lo declara «meta de diseño». El 0,3 % no aparece en las Bases.
- Contradicción (C-08): ese «umbral contractual» no figura en los criterios de aceptación del SD3 (Anexo 3.J) ni en S-29, que sólo exige investigar y justificar las diferencias de inventario.
- Redacción: «E1 mantiene desarrollo M1–12, marcha blanca M13–15» usa «M» para meses, el mismo prefijo de los módulos M1–M12; abreviaturas S2, S3 y S4 sin glosario; frases como «Raw dura treinta días». El §7.1 trata igual el capítulo que el grupo no pueda explicar.
- Frases de auditor contra el propio diseño: «Se trata de procedimientos futuros, sin actas de ejecución acreditadas» (5.3.4).

**Qué se espera en el Informe 3:** revisión humana; una sola calificación del 0,3 % como meta de diseño; reescribir 5.1–5.4 en prosa completa, sin abreviaturas internas.

---

## 6. Metodologías — Formularios T-9 y T-10 (8 %)

**Revisión: (Puntaje 0 — marcador IA) · Sin la causal: 20**

Veredicto: las cinco filas de IA tienen `[[REVISIÓN HUMANA]]`. Es el subdocumento con más contradicciones hacia otros: cinco quedan registradas en su hoja (Starlink, cámaras, sala técnica, reserva de calendario y cobertura) y una más sobre interesados.

- OK - PMBOK con tres adaptaciones; valor ganado calculado con la curva del T-15 (Tabla 6.4: PV 35.006 HH, SPI 0,95, CPI 0,97); comités del Art. 71° con cadencias idénticas a SD7 y SD8.
- Contradicción (C-02): «Starlink de las tres plataformas» (Tabla 6.3) frente a Starlink en los cinco sitios del SD4.
- Contradicción (C-03): «Acta con el sindicato | Terminales, GPS y cámaras» (Tabla 6.3) frente a «No se instalan cámaras en cabina» (SD3 3.4.6; SD2 S-13).
- Contradicción (C-05): sala técnica de Talca «Mes 5» y obra civil «Meses 5 y 6» (Tabla 6.3) frente a los meses 3–4 del T-14, «desde el mes 4» del T-15 y «desde el mes 3» del SD8-A (R8-19).
- Contradicción (C-06): «el Formulario T-15 no deja reserva de calendario antes de ese hito [H4]» (6.1.5) frente a T-15 Tabla 5.2 (H4: 19 días hábiles) y SD7 7.3.1.
- Contradicción (C-09): la Tabla 6.1 registra 17 interesados sin influencia ni interés y con agrupaciones distintas de los 19 actores del SD2 (2.4 y Anexo 2.3).
- Texto de manual: 6.1.1 y 6.1.4 definen interesados e integración en abstracto; 6.2 enumera las fases de RUP como un libro. Cero figuras.

**Qué se espera en el Informe 3:** revisión humana; alinear la Tabla 6.3 con SD4, SD3 y T-14; borrar la frase sobre la reserva del H4; registro de interesados igual al del SD2; una figura del ciclo RUP con las puertas DevSecOps.

---

## 7. Plan de trabajo, EDT, cronograma e implantación — Formularios T-14, T-15 y T-18 (15 %)

**Revisión: (Puntaje 0 — marcador IA) · Sin la causal: 20**

Veredicto: las filas de IA del cuerpo, los anexos y los tres formularios tienen `[[REVISIÓN HUMANA]]`. La auditoría corrigió la numeración y las notas de versión. El plan es propio de Puelche y ahora tiene Monte Carlo y reservas por hito. Sin la causal queda en 20: contradice a SD4, SD3 y SD8, y declara estimaciones fundadas en el T-12 que su propio T-15 llama «tamaños supuestos».

- OK - 9 fases, 49 cuentas y 222 paquetes; 564 actividades con la regla del 8/80; hitos del E-25 en meses fijos; inicio en febrero de 2027 razonado (Tabla 7.6); indicadores de cierre mapeados al Art. 17.3 (Tabla 7.9).
- Contradicción (C-04): «Contrato de Starlink para las tres plataformas … en los tres sitios» (T-14 5.3.3) frente a los cinco sitios del SD4.
- Contradicción (C-07): «Acta de acuerdo con el sindicato sobre terminales, GPS y cámaras» (T-14 5.4.2) frente a S-13.
- Contradicción (C-10): «INT-04 | Detalle de cross-docking a Talca» (Anexo 7.E) frente a «Detalle de cross-docking a la nube» (SD4 Anexo 4-G, Tabla A.8).
- Contradicción (C-14): «cada hito se entrega a tiempo en al menos el 90 % de los escenarios» (7.3.1) frente a «H9 … 89,9 %» (SD8 Tabla 8.5; T-15 Tabla 5.2).
- Contradicción (C-15): «Soporte puente de la Etapa 1 | 16 a 20 | 14.744 | 1.920 | 16.664» (Tabla 7.4) frente a «soporte puente de 9.336 HH» (SD8 8.2.3; T-15 §4.1; el propio 7.3.8).
- Contradicción (C-16): 7.2.2 dice que el valor más probable «el equipo funda en los requerimientos del Formulario T-12». T-15 §4.1 dice «Son tamaños supuestos, a sustituir por estimaciones del equipo», y SD8 E8-01 lo repite. La tríada es ±25 % fijo (T-15 §5.3). **No corregido (Informe 1)** en sustancia: no hay estimación de tres valores ejecutada.
- Inconsistencias internas del SD7: 12 resultados en la marcha blanca E1 (Tabla 7.11) frente a 14 (T-18 §2 y Anexo 7.C); reservas de «6 a 35» días (7.3.1) frente a «3 a 35» (Anexo 7.F); «integración mes 16 (H9)» (T-14) con H9 en el mes 17; «88.561 HH» de implementación (7.2.2) frente a «190.366 HH de implementación» (7.3.8); «La estimación es provisional» (T-14, criterios vigentes).
- El cierre de la marcha blanca E2 sigue cayendo en el congelamiento y el peak de septiembre (7.3.5). Lo resuelve con «continuidad previamente autorizada por el CLIENTE», que no es una decisión propia.
- Las Figuras 7.1–7.12 son listas de viñetas sin imagen (ver Paso 1).

**Qué se espera en el Informe 3:** revisión humana; alinear Starlink, cámaras e INT-04; un solo valor de soporte puente y de probabilidad del H9; estimación de tres valores realmente fundada en T-12 y T-11, o declarar honestamente el método por analogía; resolver la marcha blanca E2 de septiembre.

---

## 8. Plan de riesgos — Formulario T-16 (10 %)

**Revisión: (Puntaje 0 — marcador IA) · Sin la causal: 20**

Veredicto: todas las filas de IA tienen `[[REVISIÓN HUMANA]]`. Desaparecieron «esta sesión», «esta copia» y «SD5 no consolidado». Hoy tiene 32 riesgos anclados en Puelche, FMEA, valor esperado de 15.076 HH y Monte Carlo de 5.000 iteraciones. Sin la causal queda en 20 por la contradicción con el SD4 sobre el RPO, que el propio SD8 hace explícita.

- OK - Escalas P/I/D definidas y calibradas (Tablas 8.2 y 8.3); RBS con tres ramas del T-22; contingencia 15.076 − 1.853 = 13.223 HH con reparto por período (Tabla 8.6); P de SD13 idénticas a T-16 y Anexo 8.B.
- Contradicción (C-17): «plazo: Antes H7/mes21» (T-16 R8-22; Anexo 8.A R8-22; E8-07). H7 es el mes 16 (SD7 Tabla 7.5).
- Contradicción (C-18): E8-11 dice que la subsanación «no tiene holgura: una observación atrasa el hito». El SD7 7.3.1 declara reservas de 6 a 35 días hábiles por hito.
- Contradicción menor (C-21): «La suspensión láctea de septiembre de 2026» (8.3.3; E8-08). Según el SD2, la suspensión empezó en marzo de 2026 y vence en septiembre.
- La Figura 8.1 (RBS) es una lista (ver Paso 1).
- El texto argumenta contra la propia oferta: «no demuestra contratación ni cobertura por subventana», «Horas de atención tampoco prueban SLA», «El proyecto no demuestra una solución retroactiva». Es la voz de un auditor, no la de un proponente (§7.1, dos voces).

**Qué se espera en el Informe 3:** revisión humana; corregir H7/mes 21; RBS dibujada; reescribir 8.2.3 y 8.3.3 como compromisos con disparador, no como confesiones.

---

## 9. Plan de calidad — Formularios T-13 y T-17 (8 %)

**No evaluado en esta corrida, por instrucción del usuario.**

---

## 13. Innovaciones — Formulario T-19 (10 %)

**Revisión: (Puntaje 0 — marcador IA) · Sin la causal: 40**

Veredicto: el SD13 se presenta, con los títulos 13.1–13.5 exactos, el tipo y el nombre en el primer párrafo y los siete elementos por innovación. La declaración de IA tiene `[[REVISIÓN HUMANA]]` en todas sus filas. Sin la causal queda en 40, con un riesgo de caer a 20 por el filtro del Art. 30° en la innovación 3.

- OK - Paquetes y meses idénticos a T-14 y Anexo 7.D; riesgos R8-25 a R8-29 con la escala del SD8; impacto económico por rubro y mes, sin montos; deslinde explícito con lo obligatorio (Tablas 13.2 y siguientes).
- Crítico potencial (C-22): la innovación 3 se presenta como «la forma en que LafroX … oferta» el RT-05.30 (13.3.2), y el T-12 la registra como cumplimiento de ese RT. El Art. 30° rechaza la innovación que coincide con un RT. Que el RT sea deseable no lo excluye del filtro.
- Contradicción (C-13, registrada en la hoja del SD4): el SD4 no recoge las innovaciones que el SD13 ubica en sus capas.
- La Figura 13.1 es una lista (ver Paso 1). Encabezado «Subdocumento 13 del T-7: Innovaciones» copiado de la Aclaración §11.

**Qué se espera en el Informe 3:** revisión humana; separar la innovación 3 del RT-05.30, o reemplazarla; reflejar las cinco en SD4 4.1/4.2; figura dibujada.

---

## CONSIDERACIONES TRANSVERSALES

- **Consistencia técnica.** La planilla registra 22 contradicciones entre subdocumentos: 8 altas, 9 medias y 5 bajas. Las que más pesan son Starlink (SD6, SD7 frente a SD4), cámaras (SD6, SD7 frente a SD2/SD3), nombres de módulos (SD4 frente a SD3), calendario admisible (SD3 frente a SD7), RPO residual (SD4 frente a SD8) e innovación 3 frente al RT-05.30 (SD13 frente a SD3). OK - RTO/RPO, 99,95/99,9 %, cinco ambientes, mesa 04:00–22:00 L–S con 24×7 en septiembre y diciembre, ERP emisor único, regla de precio, promesa 24/48 h, excursión térmica graduada, 202.774 HH, peak de 69 personas en el mes 15 y contingencia de 13.223 HH coinciden en todos los subdocumentos que las mencionan.
- **Trazabilidad (retiro de lote < 2 h).** SD2 Tabla 2.1 → T-12 RF-09.01/02 → SD4 M9/EPCIS → SD5 5.1.7 (presupuesto de 85 min) → SD7 Anexo 7.C (marcha blanca E1) → SD8 R8-16/R8-23. La cadena ya no se corta en el dato; se corta en la prueba y la aceptación (S9, no evaluado).
- **Coherencia plan ↔ equipo ↔ arquitectura.** La construcción ocupa a las 48 personas de la división de desarrollo a la vez (T-15 §5.7), aunque esas personas «atienden otros contratos». SEG (9 frente a 7) e IMP (26 sin división) requieren contratación. Está declarado, pero no es verosímil sin evidencia.
- **Uso de IA.** La causal ya no son notas de proceso: son los marcadores de revisión. Corregirlos es trabajo del equipo, no del asistente.
- **Compliance.** Sin precios ni plazos distintos del Art. 17°. Folio, firma y nomenclatura quedan pendientes del PDF.

## Tabla final

| Ítem | Peso | Puntaje actual | Puntaje sin la causal de marcadores | Ponderado sin la causal |
|---|---:|---:|---:|---:|
| Transversal | 3 % | N/E | N/E | — |
| 1 Presentación de la empresa | 3 % | 0 | 20 | 0,6 |
| 2 Problema y necesidad | 6 % | 0 | 60 | 3,6 |
| 3 Esquema de solución y alcance | 12 % | 0 | 20 | 2,4 |
| 4.1 Arquitectura lógica | 7 % | 0 | 20 | 1,4 |
| 4.2 Arquitectura física | 12 % | 0 | 20 | 2,4 |
| 5 Modelo y gestión de datos | 6 % | 0 | 40 | 2,4 |
| 6 Metodologías | 8 % | 0 | 20 | 1,6 |
| 7 Plan de trabajo, EDT, cronograma | 15 % | 0 | 20 | 3,0 |
| 8 Plan de riesgos | 10 % | 0 | 20 | 2,0 |
| 9 Plan de calidad | 8 % | N/E | N/E | — |
| 13 Innovaciones | 10 % | 0 | 40 | 4,0 |
| **Total (89 % evaluado)** | | **0** | | **23,4** |

**Referencia para el grupo (no forma parte del puntaje).** Con la revisión humana completa y las 22 contradicciones resueltas, el contenido se acercaría a S1 60, S2 60, S3 60, S4.1 60, S4.2 60, S5 60, S6 40, S7 40, S8 60 y S13 60, unos 48,8 puntos sobre el 89 % evaluado.

## Prioridades para el Informe 3

1. Completar las 204 celdas de revisión humana con revisiones reales (quién verificó qué). Es la única causal que hoy deja todo en 0.
2. Resolver las 8 contradicciones altas de la planilla, empezando por Starlink, cámaras, nombres de módulos y calendario.
3. Confirmar que el PDF trae dibujadas las figuras que en el Markdown son sólo texto (SD1, SD2, SD3, SD7, SD8, SD13).
4. Separar la innovación 3 del RT-05.30.
5. Reemplazar las frases que argumentan contra la propia oferta (SD8, SD5) por compromisos con disparador y responsable.
