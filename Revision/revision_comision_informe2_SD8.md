# LAFROX · GRUPO 2 · INFORME 2 · Caso 2 · Distribuidora Puelche S.A.

**Revisión de la Comisión Evaluadora sobre fuentes Markdown — sólo Subdocumento 8.** Corrida de `Revision/prompt_revision_comision_informe2.md` limitada al ítem 8 del T-21, sobre la rama `rama-md`, con el estado del 8 de octubre de 2026 posterior a la corrección de las contradicciones C-12, C-14 a C-18 y C-21. Complementa la sección 8 de `Revision/revision_comision_informe2.md`, que queda desactualizada en lo que aquí se indica. Las comprobaciones de páginas, folio, firma, tipografía y legibilidad quedan pendientes del PDF compilado; las referencias de evidencia indican archivo y sección.

**Archivos recibidos:** `LAFROX-Subdocumento8.md`, `LAFROX-Subdocumento8-Anexos.md` y `LAFROX-Formulario-T-16.md`. La nomenclatura cumple el patrón de la Aclaración §1; la del PDF queda pendiente.

**Documentos revisados:** Subdocumento 8 (206 líneas), Anexos 8.A–8.F (760 líneas), Formulario T-16 (58 líneas, 32 riesgos). Contrastados con SD2, SD4 (4.2.5.1, 4.3.2.4, Anexo 4-W.7), SD7 (7.2.2, 7.3.1, Tablas 7.4 y 7.5), T-15 (§4.1, §5.2, §5.5, Tabla 5.2), Caso 02 (Cap. 10, 13, 17.5 y 19) y Aclaraciones §2–§7 y §11.


> **Estado posterior (8 de octubre de 2026).** Después de esta revisión se corrigieron en el SD8 todas las observaciones salvo cuatro. Lo corregido: RBS como figura Mermaid; apetito de riesgo; riesgos del Caso 19 en R8-03 (Concepción) y R8-18 (peak de septiembre); costo-beneficio por riesgo en la Tabla C.5 y en cada ficha; voz de auditor; glosario de códigos; redacción telegráfica; citas 1:1; tablas citadas por número; «13 puestos» de C-04; T-16 R8-11, R8-31 y R8-32; cámaras en R8-21. También se reemplazaron «CD-05», «A31» y «A32», que ya no existen en el SD4, por la coordinación de reserva de INT-03/04, el Anexo 4-I y la sección 4-W.5. Quedan pendientes: las 13 celdas `[[REVISIÓN HUMANA]]`, que sólo puede completar un integrante; la Tabla C.4, que debe recalcularse con 5.000 iteraciones; la imagen de la Figura 8.1 para el PDF, y la magnitud de la reserva de gestión, que se deja para la entrega final por decisión del grupo.

---

## CORRECCIONES DEL INFORME 1

El SD8 es nuevo en el Informe 2: no tiene observaciones previas que verificar. Respecto de la corrida del 8 de octubre de `revision_comision_informe2.md`:

- Corregido: C-12 (RPO residual). El SD8 ya no afirma que «aceptar el riesgo no satisface Bases»; 8.3.3, R8-05, E8-05 y T-16 adoptan el tratamiento del SD4 4.3.2.4 con RT-02.11.
- Corregido: C-14 (H9 con 89,9 % en 8.2.3, Tabla 8.5, Tabla C.3 y SD7 7.3.1), C-15 (9.336 HH explicadas como parte de las 16.664 HH del SD7, Tabla 7.4), C-16 (E8-01 y R8-11 alineados con SD7 7.2.2), C-17 («antes del H7 (mes 16) y del H12 (mes 21)»), C-18 (E8-11 distingue H1 de H2–H10) y C-21 («de marzo a septiembre de 2026»).
- Parcial: la voz de auditor señalada en la corrida anterior. Se retiró «aceptar el riesgo no satisface Bases», pero siguen «no demuestra contratación ni cobertura por subventana», «Horas de atención tampoco prueban SLA» (8.2.3) y «El proyecto no demuestra una solución retroactiva» (8.3.3).
- No corregido: RBS dibujada y revisión humana.

**Regresión nueva:** una menor. El T-16, fila R8-11, conserva «Estimar con equipo/cantidades», mientras la ficha 8.A ya dice «Refinar con el equipo la estimación por clase, trazada al T-12 y a las cantidades del T-11».

---

## Causales duras (Paso 1)

- **Precios (Art. 50.2): ninguno.** OK - Cero coincidencias de «$», «USD», «CLP» o «UF» en los tres archivos. Las reservas se expresan en HH (Tabla 8.6; Anexo 8.D) y la reserva de gestión remite a la Oferta Económica (8.3.2).
- **Crítico — Indicio de IA, Aclaración §7.1 d (cuadros de aprobación en blanco).** 13 celdas `[[REVISIÓN HUMANA]]`: 7 en el cuerpo, 5 en los anexos y 1 en el T-16. Ninguna fila de la Declaración de uso de IA identifica a un integrante ni dice qué verificó. Además, 11 de las 13 filas declaran nivel «Alto» en texto.
- **Crítico — Indicio de IA, Aclaración §7.1 a y §4.** La «Figura 8.1 — Estructura de desglose de riesgos (RBS). Fuente: elaboración propia a partir del Anexo 8.A.» (8.2.1) es una lista de viñetas, no un diagrama. Es la única figura del capítulo. Si el PDF no la trae dibujada, es el caso literal de una leyenda «Fuente: elaboración propia» sin figura.
- **Códigos internos sin glosario en el cuerpo.** «V-13» (8.3.3), «A31 y A32», «CD-05» (8.3.3), «R18-16» (8.A R8-13), «AL-STOCK-01/AL-ACT-01», «2N+2L», «4L», «F−28 días» (anexos). El cuerpo no los define ni remite a un glosario.
- **Formulario del ítem:** OK - T-16 presente, citado en la introducción y en 8.2.2, con las ocho columnas del formato de las Bases Administrativas (ID, Riesgo, Categoría, Prob., Impacto, Expos., Mitigación, Responsable).
- **Cronograma Art. 17°:** OK - H7 en el mes 16, H12 en el mes 21, marchas blancas 13–15 y 19–20 y operación 21–56, coherentes con SD7 Tabla 7.5.

---

## 8. Plan de riesgos — Formulario T-16 (10 %)

*8.1 Plan de riesgos (enfoque, roles, escalas, ciclo) · 8.2 Identificación y Análisis de Riesgos (RBS y cuantificación técnicos, organizacionales, de proyecto, de seguridad y de operación; obsolescencia, bloqueo por proveedor, escalabilidad, ciberseguridad, contrapartes del CLIENTE; cualitativo y cuantitativo con FMEA, árbol de fallas o simulación) · 8.3 Plan de Acción a Riesgos (mitigación con costo-beneficio, responsable, plazo y disparador; reservas de contingencia y de gestión y su reflejo en el cronograma; valorización en la Oferta Económica). En todo el capítulo: riesgos de la solución propuesta, no un catálogo genérico.*

**Revisión: (Puntaje 0 — indicios de IA §7.1 a y d) · Sin la causal: 40**

Veredicto: el subdocumento queda en 0 por las 13 celdas `[[REVISIÓN HUMANA]]` y por una RBS que es una lista con leyenda de figura. Sin esas causales, el núcleo existe y es sólido: 32 riesgos anclados en Puelche, FMEA con NPR, valor esperado de 15.076 HH y una simulación de Monte Carlo de 5.000 iteraciones con P50 y P80 por hito. Con las siete contradicciones del SD8 ya resueltas sube de 20 a 40, no a 60. Faltan la RBS dibujada, dos riesgos que el Caso 19 nombra expresamente y un costo-beneficio por riesgo en lugar de una frase repetida 32 veces.

### Introducción a los Riesgos

- OK - Conecta con SD2, SD3, SD4, SD6 y SD7, describe anexos 8.A–8.F y el T-16, y cita el SD4 4.3.2.4 para el RPO residual (Aclaración §2).
- OK - Ancla el capítulo en cifras del caso: 96 camiones entre 05:30 y 07:00, CD 24 h sin WAN, terreno 14 h sin señal, ERP único emisor.

### 8.1 Plan de riesgos

- OK - Ciclo ISO 31000 con cadencias concretas: verificación semanal de disparadores, Comité de Proyecto quincenal, comités Ejecutivo y de Arquitectura mensuales, Comité de Operación mensual desde el mes 13, seguimiento diario en marcha blanca (8.1.1). Coincide con SD6 6.1.6.
- OK - Roles con nombre y ámbito (Tabla 8.1); los ocho nombres coinciden con el SD1.
- OK - Escalas P, I y D definidas en cinco niveles (Tabla 8.2), umbrales de exposición (baja 1–3, moderada 4–7, alta 8–14, crítica 15–25) y calibración cuantitativa de P en tramos de probabilidad y de I en fracción de esfuerzo (Tabla 8.3).
- El umbral de apetito no se declara como tal. Sólo existe la regla «I = 5 exige escalamiento aunque E no alcance 15» (8.1.3). Falta decir qué nivel de exposición residual acepta el Comité Ejecutivo y cuál exige tratamiento obligatorio.
- La Tabla 8.1 es del tipo «Rol | Ámbito», con frases en la segunda columna (Aclaración §5). Es admisible por su brevedad, pero bordea la regla «Concepto | Descripción».

### 8.2 Identificación y Análisis de Riesgos

- OK - Los cinco temas obligatorios tienen ficha: obsolescencia (R8-09), bloqueo por proveedor (R8-08), escalabilidad (R8-06, R8-30), ciberseguridad (R8-07, R8-24) y contrapartes del CLIENTE (R8-12).
- OK - Los tres análisis del T-22 son identificables: Solución (13), Desarrollo (10) e Implantación (9). La suma 13 + 10 + 9 = 32 coincide con el Anexo 8.A, y los 22 riesgos de nivel crítico de la Tabla B.1 se reparten 11 en la solución, como dice 8.2.1.
- OK - FMEA ejecutado: P, I, D, E y NPR para los 32 riesgos (Tabla B.1), con justificación individual de P y D en cada ficha. La Tabla 8.4 extrae los cinco mayores y el texto explica por qué R8-05, con P = 3, queda cuarto por su D = 5.
- OK - Cuantificación reproducible. Se recalcularon: 15.076 / 190.366 = 7,9 % («cerca de 8 %»); 4.075 + 3.182 + 1.478 + 1.008 + 461 = 10.204, es decir, 67,7 % del total; R8-11 = 22.640 × 30 % × 60 % = 4.075 HH; R8-22 = 442 × 12 × 60 % = 3.182 HH. Todo coincide.
- OK - Monte Carlo ejecutado y mostrado: distribución PERT beta(3,3), 5.000 iteraciones, P50, P80 y probabilidad por hito (Tabla 8.5 y C.3), y sensibilidad de tornado (Tabla C.4). Los valores coinciden con T-15 Tabla 5.2.
- OK - Riesgos propios del caso (Cap. 19): pérdida del conocimiento de rutas (R8-13), objeción sindical y rechazo de conductores de terceros (R8-21), rotación en bodega (R8-20) e interfaces sin documentación (R8-10).
- **Riesgo del Caso 19 ausente: «dependencia de un solo enlace en Concepción».** Ni el cuerpo, ni los anexos, ni el T-16 mencionan Concepción. El SD4 lo resuelve con tres caminos (fibra, LTE y Starlink D-06), pero el plan no registra el riesgo residual de ese sitio ni remite a la decisión.
- **Riesgo del Caso 19 sin ficha: «peak de septiembre coincidiendo con una fase del proyecto».** El Anexo 8.C, escenario C-07, reconoce que la evidencia de la Etapa 2 cae del «03–30 septiembre» con congelamiento del 01 al 25, pero ninguna de las 32 fichas trata ese solape. R8-17 cubre la fecha efectiva del contrato, no el peak.
- La Figura 8.1 no es un diagrama (ver causales). Un capítulo técnico cuya única figura es una lista no cumple la Aclaración §4.
- 8.2.3 dice que la simulación usa «el cronograma por actividad del Formulario T-15», y el Anexo C.3 dice «la red de los 163 paquetes con entregable». Ambos describen la misma red (564 actividades de 163 paquetes, T-15 §6), pero el texto debe usar una sola unidad.
- La Tabla C.4 tiene filas en que quitar un riesgo baja la probabilidad respecto de la base (por ejemplo, «Sin R8-19» deja el H9 en 89,9 % frente a 90,5 %). El texto lo atribuye al error de muestreo de 3.000 iteraciones. La explicación es correcta, pero una sensibilidad con más ruido que señal en el H9 debe correrse con las mismas 5.000 iteraciones.
- La voz de auditor persiste: «no demuestra contratación ni cobertura por subventana» y «Horas de atención tampoco prueban SLA» (8.2.3). Es la voz de un evaluador y no la de un proponente (§7.1, dos voces).

### 8.3 Plan de Acción a Riesgos

- OK - Cada ficha tiene responsable (rol del equipo nominado), disparador observable, plazo ligado a un hito, mitigación, contingencia y evidencia de cierre.
- OK - Reserva de contingencia por valor esperado (PMI, 2017), con la deducción de la capacidad protegida mostrada: 461 + 384 + 1.008 = 1.853 HH, y 15.076 − 1.853 = 13.223 HH. El reparto por período suma 15.076 HH (Tabla 8.6) y el 88 % se concentra en los meses 7–33 (13.222 HH).
- OK - Reflejo en el cronograma: la reserva de cronograma son las reservas de cada hito del T-15 Tabla 5.2 (6 a 35 días hábiles), y la fecha P80 de cada hito queda antes de su fecha límite.
- OK - RPO residual tratado como en el SD4, con medidas concretas (alarmas de 5 y 15 min, NAS WORM, preemisión de guías) y medición en conmutación real antes del H5 y del H10.
- **Costo-beneficio genérico.** Las 32 fichas repiten la misma frase: «Costo-beneficio técnico: asignar controles a los paquetes señalados, comparar HH de verificación y retrabajo según 8.C». El único cociente calculado es el ejemplo de C.2 (400/160 = 2,5), y el propio anexo dice que «Los valores específicos requieren estimación del equipo». El índice exige «estrategias de mitigación basadas en análisis costo-beneficio». Ninguna ficha compara su mitigación con su valor esperado de la Tabla B.2.
- La reserva de gestión no tiene magnitud técnica (ni HH ni días). Que el monto vaya a la Oferta Económica no impide expresar su tamaño en HH, como se hace con la de contingencia.
- El escenario C-04 afirma «13 puestos simultáneos necesitan relevos», pero su cálculo usa 12 puestos (12 × 24 × 8 + 160 = 2.464 HH). La cifra 13 no se deriva del cálculo mostrado (§7.1 b).
- 8.3.1 dice que «Los 160/320 HH derivan de clases del T-15; son referencias supuestas, no ensayos ejecutados ni ampliaciones aprobadas», y 8.3.3 que «El proyecto no demuestra una solución retroactiva». Son descargos y no compromisos con disparador.

### Consistencia

- OK - Ninguna contradicción abierta con otro subdocumento en la planilla de contradicciones tras las correcciones C-12, C-14 a C-18 y C-21.
- OK - Cifras transversales idénticas a las del resto de la propuesta: 202.774 HH, 190.366 HH base, 9.336 HH de soporte puente, 3.072 HH de reserva E1, peak de 69 personas en el mes 15, límite de mesa de 2.283 contactos/mes y demanda de 2.258 en el año 3 (SD4 Anexo 4-W.7), RTO 4 h y RPO 15 min.
- Inconsistencia interna menor: T-16 R8-11 («Estimar con equipo/cantidades») frente a 8.A R8-11 («Refinar con el equipo la estimación por clase…»).
- Precisión pendiente: R8-21 habla de «objeciones GPS/cámara», que es lo que registra el caso. No dice que la solución no instala cámaras en cabina (SD3 3.4.6; SD4 M12). Debe decirlo, para no reabrir la contradicción C-03/C-07.
- Formato del T-16: R8-31 y R8-32 no siguen el patrón «plazo: …; Disparador y contingencia: Anexo 8.A R8-NN» de las otras 30 filas.

### Forma e indicios de uso de IA

- **Crítico:** 13 celdas `[[REVISIÓN HUMANA]]` (§7.1 d) y una figura que es una lista con leyenda de fuente (§7.1 a). Ver causales.
- Las fichas 8.A usan una redacción telegráfica sin espacios que delata compresión automática: «Antes mes13; semanal hasta20», «meses1–3», «salida mes56», «enero2029», «resultado16», «BA17.2», «04–22 lunes–sábado y24×7». Un integrante difícilmente las defendería en una interrogación como texto propio (§7.1, último párrafo).
- Dos líneas idénticas cierran cada una de las 32 fichas («Costo-beneficio técnico…» y «Seguimiento semanal y en cada comité…»): 64 líneas de plantilla.
- Referencias (§6): el cuerpo lista ocho referencias, pero cita en formato APA sólo cuatro (ISO 2018, IEC 2018, PMI 2017 y Distribuidora Puelche 2026b). Las Bases Administrativas aparecen como «BA Art. 50.2» y no como (Distribuidora Puelche S.A., 2026a). 2026c, 2026d y LafroX (2026) no se citan. Los anexos citan sólo PMI 2017 de sus ocho referencias. El T-16 cita sólo ISO 2018 de sus siete.
- Las citas a las Bases no indican página (§6). Queda pendiente del PDF.
- Tablas: cuatro de las seis del cuerpo no se citan por su número antes de aparecer: la 8.2, la 8.3 («la segunda tabla de esta sección»), la 8.5 («La tabla informa») y la 8.6 («La tabla reparte»). El estilo de leyenda mezcla «Tabla 8.1.» en el cuerpo con «Tabla B.2 —» en los anexos (§5, formato único).
- OK - Todas las tablas del cuerpo tienen como máximo cinco columnas y análisis posterior. Ningún título va seguido directamente de una tabla, una figura u otro título.
- OK - Cierre con «Referencias» y «Declaración de uso de IA», sin numerar y en ese orden, en los tres archivos.

**Qué se espera en el Informe 3:**

- Completar la revisión humana de las 13 filas con nombre del integrante y qué verificó, y bajar el nivel declarado donde corresponda.
- Dibujar la RBS como figura propia (vista general y ramas), citarla antes y explicarla después.
- Registrar los dos riesgos del Caso 19 que faltan: enlace de Concepción (con la decisión del SD4) y peak de septiembre sobre la marcha blanca de la Etapa 2.
- Reemplazar la frase genérica de costo-beneficio por un cálculo por riesgo (HH de la mitigación frente al valor esperado de la Tabla B.2), al menos para los 22 riesgos críticos.
- Reescribir las fichas 8.A en prosa completa y con glosario de códigos. Convertir los descargos de 8.2.3, 8.3.1 y 8.3.3 en compromisos con disparador y responsable.
- Corregir la correspondencia 1:1 de referencias y citas, la sensibilidad C.4 con 5.000 iteraciones, el «13 puestos» de C-04 y la fila R8-11 del T-16.

---

## CONSIDERACIONES TRANSVERSALES (alcance SD8)

- **Consistencia técnica:** sin contradicciones abiertas con SD2, SD4 ni SD7 tras las correcciones de esta fecha. Queda la precisión de cámaras en R8-21.
- **Trazabilidad (retiro de lote < 2 h):** la cadena llega al SD8 por R8-16 (migración de lotes) y R8-23 (evidencia térmica), con evidencia de cierre definida. El tramo de pruebas y aceptación (S9, T-13, T-17) sigue sin evaluar.
- **Coherencia plan ↔ equipo ↔ arquitectura:** R8-11, R8-14 y R8-32 recogen el peak de 69 personas, las 48 simultáneas de desarrollo y las brechas de SEG e IMP del T-15 §5.7. Es la parte mejor anclada del capítulo.
- **Fundamentación ingenieril:** FMEA, valor esperado y Monte Carlo están ejecutados y cuadran con el T-15. La debilidad es el costo-beneficio y la falta de la figura.
- **Uso de IA:** las 13 celdas sin revisión humana, la RBS en lista y la redacción telegráfica dejan el subdocumento en 0.
- **Compliance:** sin precios ni plazos fuera del Art. 17°. Folio y firma pendientes del PDF.

## Tabla final (ítem 8)

| Ítem | Peso | Puntaje | Ponderado |
| --- | --- | --- | --- |
| 8. Plan de riesgos — T-16 | 10 % | 0 (sin la causal: 40) | 0,0 (sin la causal: 4,0) |
