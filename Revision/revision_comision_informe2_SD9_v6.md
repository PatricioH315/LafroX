# Revisión de la Comisión — Informe 2 · Subdocumento 9 (v6, sólo observaciones)

**LAFROX · GRUPO 2 · INFORME 2 · Caso 2 · Distribuidora Puelche S.A.**

**Archivos recibidos** (`09_plan_calidad/`): `LAFROX-Subdocumento9.md`, `LAFROX-Subdocumento9-Anexos.md`, `LAFROX-Formulario-T-13.md`, `LAFROX-Formulario-T-17.md`. Se cotejan con SD1, SD3, SD4, SD6, SD8, T-10, T-12, T-14 y T-15, y con las Bases.

**Alcance de esta corrida.** Sólo se registran defectos; se omiten los «OK». El objetivo es identificar lo que impide alcanzar **60/100 sin la causal de IA**. Las referencias indican archivo y sección; las comprobaciones exclusivas del PDF quedan pendientes.

**Diagnóstico de contenido sin la causal: 20.** El árbol del prompt lo fija en el paso 6 por contradicciones de diseño y un plan no ejecutable. Para llegar a 60 (paso 7) se necesita un núcleo completo, cero contradicciones y sólo faltas menores.

---

## 0. Fuera del puntaje de contenido (igual dejan el ítem en 0)

- **Crítico — 16 celdas `[[REVISIÓN HUMANA]]`:** SD9 10, Anexos 4, T-13 1 y T-17 1 (ACL §7.1). Sin subsanación.
- **Crítico condicionado — Figuras.** Las 10 figuras son bloques Mermaid sin imagen enlazada. Si el PDF no trae el dibujo, aplica la ACL §7.1 a: «diagramas descritos en texto que no se dibujaron». AGENTS.md exige enlazar la imagen real. Los `.drawio` de `Diagramas/` no se referencian.

---

## Nivel 1 — Lo que hoy deja el contenido en 20

**N-01. G5 tiene dos alcances en el mismo documento.** La sección 9.2.1 dice: «G5 rige los pasos H7 y H12». La 9.3.2 dice: «Cada corrección de marcha blanca pasa por las puertas G0 a G5». Si G5 exige la Tabla 9.6 completa y el acta de la Contraparte, cada corrección de marcha blanca requiere pentest y DR. Si no lo exige, la Tabla 9.5 está mal. *Se espera:* un único alcance de G5 y una puerta específica, con su contenido, para las correcciones de marcha blanca.

**N-02. Correcciones de la marcha blanca E2 en el congelamiento.** La sección 9.3.2 afirma que la marcha blanca E2 «no introduce cambios técnicos durante el congelamiento». El mismo apartado obliga a promover las correcciones por G0–G5. En septiembre de 2028 el grupo debe elegir entre desplegar en congelamiento (Caso, Cap. 13) o llegar al H12 (octubre) con defectos abiertos, que el Art. 17.3 no admite. El documento no resuelve el dilema. *Se espera:* una regla de correcciones para septiembre de 2028: qué se corrige, por qué vía de emergencia, quién lo autoriza y cómo se protege el H12.

**N-03. Producción sin pruebas periódicas en los meses 13 a 20.** La Tabla 9.9 y la T13.6 empiezan la restauración en el mes 21. Sin embargo, Producción opera con datos reales desde el H6, mes 13 («Producción | Marcha blanca | Datos reales», T13.2). El RT-07.12 exige una restauración «al menos mensual». La DR va del mes 17 (3.9.4) al mes 27 y la resiliencia del mes 17 al 26: entre 10 y 11 meses. Eso contradice la «separación máxima de seis meses» que el propio SD9 declara. Además, la Tabla 9.9 atribuye esa frase al RT-07.07, que dice «al menos dos veces al año». *Se espera:* restauraciones mensuales desde el mes 13, DR y resiliencia con una separación ≤ 6 meses desde el primer paso a producción, y la cita literal del RT.

**N-04. Preproducción saturada (v5 A2: no corregido y ahora también en la E1).** En la E1, la T13.5 programa 3.8.4, 3.8.5, 3.8.6 y 3.8.8 entre el 21-10 y el 09-11-2027, superpuestos con los ensayos de migración 3.7.2 (04-10 a 03-11-2027), todos en Preproducción. En la E2, la carga con resiliencia, la DR, el pentest y el despliegue caben en 6 días hábiles (19 a 26-05-2028). El pentest exige «Versión congelada en Preproducción» (T13.3) mientras la resiliencia inyecta fallas en ese mismo ambiente. La aceptación E2 (3.9.2), con cadenas, transportistas, Comercial y Finanzas (T-17, H10), dura 4 días hábiles (27 a 31-05-2028). *Se espera:* campañas escalonadas, o un segundo ambiente justificado, y duraciones de pentest y de aceptación fundadas.

**N-05. La Tabla 9.8 acepta atraso (v5 A3: no corregido).** Hay dos holguras negativas: H1 con −4 y H8 con −6. La «versión preliminar una semana antes» no cambia el plazo formal del Art. 18.3. El cálculo omite la segunda revisión de la Figura 9.10 y los feriados. La fecha límite del H2 (17-05-2027, T-17) no descuenta el 21-05, y la del H3 (16-07-2027) cae en feriado. La tabla excluye el H2 y el H3, aunque tienen fecha programada y el H3 incluye la prueba de las puertas. *Se espera:* holgura ≥ 0 en todos los hitos con entrega programada, calculada con feriados y con revisión, subsanación y segunda revisión.

**N-06. Re-certificaciones sin paquete, HH ni fecha (v5 C4: parcial).** La sección 9.3.2 y la T13.5 cargan la repetición de pruebas a la «reserva protegida de la Etapa 1 del Formulario T-15 (meses 13 a 20)». Las correcciones de la E2, que condicionan el H12 del mes 21, quedan fuera de esa reserva. *Se espera:* paquete, HH, ventana y responsable para la re-certificación de cada etapa.

---

## Nivel 2 — Núcleo 9.1/9.2 incompleto frente a la lista del prompt

**N-07. La duplicación no tiene umbral bloqueante.** La Tabla 9.3 dice «Medida y registrada; sin umbral bloqueante», igual que la 9B-23. El prompt S9 exige «métricas de código (cobertura, complejidad, acoplamiento, duplicación) con UMBRALES BLOQUEANTES numéricos».

**N-08. El acoplamiento no se mide como métrica, y el cuerpo contradice al anexo.** La Tabla 9.3 sólo tiene la regla deptrac (0 violaciones). La 9B-10 fija «Inestabilidad de los módulos núcleo ≤ 0,5» bloqueante en G2, pero no figura en la Tabla 9.3 ni en la Figura 9.1 («5 umbrales bloqueantes»). Kotlin y TypeScript no tienen control de acoplamiento.

**N-09. TypeScript no tiene cobertura de lógica de negocio.** La 9B-05 sólo mide la cobertura global en Angular, aunque la sección 9.1.4 fija los umbrales «en los tres lenguajes de la solución».

**N-10. El modelo de madurez no sostiene el plan.** CMMI-DEV vence en noviembre de 2026, y el propio texto dice: «Mientras no la acredite, el proyecto no invoca ese nivel como garantía» (9.1.2). ISO 9001 no es un modelo de madurez. No hay un modelo de madurez del proceso de pruebas, ni se explica cómo se usaría para mejorar el proceso durante el contrato. La referencia «SCAMPI A Appraisal Report N° 58190» no es una fuente publicada.

**N-11. Las métricas de proceso no cubren el desarrollo ni los defectos.** DORA, el MTTR y el presupuesto de error requieren Producción (mes 16 en adelante); para los meses 1 a 15 no hay ninguna métrica de proceso. La sección 9.1.1 dice que el Comité analiza «las métricas de defectos», pero la Tabla 9.4 no define ninguna: densidad, defectos escapados, reapertura o tasa de aprobación de pruebas.

**N-12. La fiabilidad omite el 99,95 % de la infraestructura.** «99,95» no aparece en el SD9, el T-13 ni el T-17, aunque está en BTT, SD1, SD3 y SD4 y en el Cap. 10 del Caso. La Tabla 9.2 y la 9A-16 sólo miden el 99,9 % de los servicios críticos.

**N-13. La automatización no es un compromiso, y sus cifras no se sostienen.** La sección 9.2.3 dice «Si el 80 % se automatiza…»: es una condición, no una meta. El medio minuto por caso automatizado, que incluye integración y Espresso, y los 15 minutos por caso manual no tienen fuente ni cálculo. Es el tipo de cifra que la Comisión puede preguntar en una interrogación (Paso 1, punto 2).

**N-14. Las pruebas no se basan en riesgos.** ISO/IEC/IEEE 29119 organiza la estrategia en torno al riesgo del producto. Aquí la intensidad sale de la prioridad del requisito (5/3/2 casos, Anexo 9.C.1) y no se vincula con los riesgos técnicos del SD8. El modelo de procesos de pruebas se atribuye a la parte 1 (ISO, IEC & IEEE, 2022); corresponde citar la parte 2.

**N-15. La matriz 9.C es genérica.** 218 de las 271 filas RF/RNF repiten «Sistema y aceptación de usuario | QA · PREPROD». Cada uno de los 354 RT recibe un solo caso, sin justificación. Trece filas dicen «Inspección del entregable de la oferta | — | —», sin paquete ni hito. Ninguna fila tiene el identificador «CP-ID requisito-nn» que promete la Figura 9.7.

**N-16. La ventana de 05:30 a 07:00 sólo está en prosa.** La prueba a 10,41 TPS (9.2.3) no figura en la Tabla 9.6, en los criterios de la T13.3 ni en la ficha H5 del T-17. Es la restricción operacional más dura del caso.

**N-17. Faltan herramientas y alcances de prueba.** No hay herramienta E2E para las consolas y los portales Angular: Jest es unitaria (T13.4). La prueba de contrato no nombra herramienta. La app Android no tiene pruebas de seguridad propias: el DAST cubre «Portales y API» (9B-16).

**N-18. Las puertas no tienen sostén en la Operación.** Los paquetes 1.5.1 y 1.5.2 abarcan los meses 6 a 20 (Tabla 9.7), y la barra «Puertas automáticas activas» de la Figura 9.9 termina el 30-09-2028. Sin embargo, la sección 9.2.1 hace pasar cada versión quincenal de los meses 21 a 56 por G0 a G4 y G6, sin paquete ni HH.

**N-19. El esfuerzo de calidad no tiene justificación.** Son 10.848 HH, el 5,0 % de 216.935. El rol CAL tiene 4.656 HH, unos 36 personas-mes en 56 meses. No hay analogía con los proyectos del T-6 ni una referencia que respalde la proporción.

---

## Nivel 3 — Inconsistencias internas y de los formularios

**N-20. Inconsistencias internas.**
- La sección 9.3.2 dice: «por eso las ejecuciones de diciembre no intervienen Producción». Las resiliencias en Preproducción caen en septiembre (meses 32 y 44); ninguna cae en diciembre.
- La sección 9.3.3 dice: «Cada resiliencia se ejecuta el mes anterior a la recuperación de su semestre». La última resiliencia (mes 55) es posterior a la última recuperación (mes 54).
- La regresión dura «≈ 4,3 h» en la T13.4 y 4,36 h en la sección 9.2.3.
- La 9A-28 marca su umbral como «(supuesto)», pero el texto del Anexo 9.A sólo identifica como propuestos los de 9A-09, 9A-25 y 9A-29.

**N-21. Defectos del T-17.** No tiene la sección «Referencias», aunque cita los Arts. 17.3 y 18 y el RT-20.08. El H3 entrega la «sala técnica de Talca» sin criterios eléctricos, térmicos ni de disponibilidad. El momento del R18-14, «Marcha blanca de la ola de reparto», no corresponde a ninguna etapa ni mes definidos.

---

## Nivel 4 — Forma y redacción citables (ACL §7.1 b/d, «dos voces»)

**N-22. Voz de auditor contra la propia oferta.** Las frases siguientes defienden al redactor y no comprometen al proponente:
- «Este plan no declara que la norma aporte umbrales por sí misma» (9.1.1).
- «Ningún umbral se presenta como una medición ya obtenida» (9.1.3).
- «pero no acredita que hayan sido probados» (9.1.4).
- «sin garantizar que toda variante del defecto quede detectada» (9.2.6).
- «Una acción ejecutada no equivale a una acción eficaz» (9.2.6).
- «no es una disponibilidad demostrada ni fija para cualquier mes» (9.3.2).
- «Mientras no la acredite, el proyecto no invoca ese nivel como garantía» (9.1.2).
- «como si la norma fijara cifras» (Anexo 9.A).

Es el mismo patrón que la revisión general observó en el SD8.

**N-23. La Tabla 9.6a parece una lista de control de esta misma oferta.** Incluye «Títulos de las Aclaraciones conservados» y «revisión humana identificada únicamente si fue realizada». Puede leerse como nota de proceso del redactor (ACL §7.1 d).

**N-24. Siglas sin glosario.** BTT, BA, CAL, DES, IMP, SEG, DAT, SRE, DORA, MTTR, SLSA, SAST, SCA, DAST, PCOV, p95, TPS, JD-nn, 9A-nn y R18-nn. El prompt trata los «códigos internos sin glosario» como indicio.

**N-25. Referencias.** «LafroX. (2026). Subdocumentos 1, 3 a 8 y 13…» cita la propia oferta como fuente bibliográfica. 20 de las 30 citas a las Bases no indican página. El informe SCAMPI no es localizable.

**N-26. Formato.** Las Tablas 9.6a y 9.6b usan sufijo en vez de numeración correlativa. La Tabla 9.1 tiene una columna titulada «Responsable existente». La Figura 9.9, un Gantt de unas 35 líneas, arriesga quedar bajo 9 pt en el PDF.

---

## Ruta a 60

1. **Resolver N-01 a N-06.** Mientras quede uno abierto, el diagnóstico sigue en 20 (paso 6: contradicción de diseño o plan no ejecutable).
2. **Cerrar N-07 a N-19.** Completan el núcleo que el prompt exige para el S9: umbrales bloqueantes de las cuatro métricas de código, madurez, métricas de proceso, 99,95 %, estrategia basada en riesgo y matriz específica. Con eso el ítem llega a 40 y, con pocas faltas, a 60.
3. **Limpiar N-20 a N-26,** para que lo pendiente sea «menor» y no queden indicios citables.
4. **Fuera del puntaje, pero imprescindible:** completar las 16 celdas de revisión humana con revisiones efectivas y enlazar la imagen de las 10 figuras.

| Ítem | Peso | Puntaje actual | Sin la causal (hoy) | Meta |
| --- | --- | --- | --- | --- |
| 9. Plan de calidad (T-13, T-17) | 8 % | 0 | 20 | 60 |
