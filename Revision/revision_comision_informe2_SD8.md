# LafroX — Revisión de la Comisión Evaluadora: Subdocumento 8

**Fecha:** 8 de octubre de 2026. **Rama comprobada:** `rama-md`. **Objeto:** nueva aplicación de `prompt_revision_comision_informe2.md` al SD8, sus Anexos 8.A–8.F y T-16, contrastados con los entregables vigentes de SD1–SD7 y SD13, las cuatro Bases, los catálogos y el material de método del ramo.

**Dictamen según el prompt: 0/100 en el ítem 8 del Informe 2, de peso 10 %, por las 15 celdas de revisión humana sin completar.** El contenido supera varios hallazgos de la revisión anterior, pero subsisten deficiencias graves en la demostración de reservas y del riesgo general del cronograma. Como diagnóstico del contenido, sin aplicar las causales de §7.1, corresponde **40/100**, por el paso 7 del árbol del prompt: registro desarrollado y cuantificación mostrada, con profundidad insuficiente en partes esenciales. Ese diagnóstico no constituye un puntaje admisible ni promete una futura evaluación.

Este informe **reemplaza íntegramente** la revisión SD8 anterior, incluida su nota de correcciones posteriores. La sección SD8 de la revisión general permanece como antecedente histórico; no representa el estado actual. No se modificaron los entregables, las Bases, el prompt ni la planilla de contradicciones. Esta revisión automática no acredita revisión humana.

## Alcance, fuentes y límites

Se aplicaron los pasos 0–7 del prompt para el ítem 8. Su inventario inicial de materiales es histórico: actualmente sí están presentes SD4–SD8 y SD13. Se leyeron completos los tres archivos del SD8 y se contrastaron las secciones pertinentes de los demás documentos; no se volvieron a puntuar esos otros ítems.

Precedencia: Bases Administrativas, Bases Técnicas Transversales y Caso 02; las Aclaraciones posteriores gobiernan estructura y presentación. PMBOK y clases orientan el método, sin sustituir requisitos ni crear cifras contractuales.

| Fuente | Evidencia contrastada |
| --- | --- |
| [Bases Administrativas](../Bases/Bases_Administrativas.md) | Arts. 17, 18, 50.2, 56 y 57; T-7, T-16, T-21 y T-22 |
| [Bases Técnicas Transversales](../Bases/Bases_Tecnicas_Transversales.md) | RT-02.11, RT-07.04/07, RT-19.04 y RT-21.06/07 |
| [Caso 02](../Bases/Caso_02_Logistica.md) | Caps. 10, 11, 13, 14, 17, 18 y 19 |
| [Aclaraciones](../Bases/aclaraciones-licitacion.md) | §§1–7 y §11, Capítulo 8 |
| [SD1](../01_presentacion_empresa/LAFROX-Subdocumento1.md) | Dotación y Tabla 1.3: nombres y permanencia de responsables |
| [SD2](../02_problema_necesidad/LAFROX-Subdocumento2.md) y anexos | Restricciones operacionales, sindicato, suspensión láctea y S-09 |
| [SD3](../03_esquema_solucion_alcance/LAFROX-Subdocumento3.md), anexos y [T-12](../03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md) | Alcance E1/E2, precio, cámaras, autonomía, trazabilidad y criterios |
| [SD4](../04_arquitectura/LAFROX-Subdocumento4.md), [anexos](../04_arquitectura/LAFROX-Subdocumento4-Anexos.md) y T-11 | INT-03/04; 4.3.2.4; 4-V; 4-W.5/7; enlaces y suministros |
| [SD5](../05_modelo_datos/LAFROX-Subdocumento5.md) y anexos | Trazabilidad, migración, recuperación y presupuesto de retiro |
| [SD6](../06_metodologías/LAFROX-Subdocumento6.md), T-9 y T-10 | 6.1.3, 6.1.6 y 6.2: adquisiciones, cadencias y refuerzo |
| [SD7](../07_PlanDeTrabajo_EDT_Cronograma_Implantación/LAFROX-Subdocumento7.md), anexos, T-14, [T-15](../07_PlanDeTrabajo_EDT_Cronograma_Implantación/LAFROX-Formulario-T-15.md) y T-18 | Paquetes, horas, reservas, fechas, dependencias y marchas blancas |
| [SD13](../13_innovaciones/LAFROX-Subdocumento13.md), anexos y T-19 | R8-24 a R8-29, indicadores y relevo a Operación |
| Requerimientos y clases + pmbok | Catálogos conservados como fuentes; PMBOK cap. 11, correlación y respuestas |

**No verificable con el material recibido:** paginación, índice paginado, folio, firma, tipografía, orientación, legibilidad, texto seleccionable, ZIP final y nomenclatura efectiva de PDF. Tampoco se recibió la revisión original del Informe 1 ni su matriz oficial completa de observación–respuesta. SD8 es nuevo del Informe 2; se compara con las revisiones locales anteriores, sin inventar observaciones del Informe 1. SD9/T-13/T-17 no se puntúan; no se acreditan sus resultados ni actas.

Se recalcularon expresiones deterministas y se examinó documentalmente la simulación publicada. **No se ejecutó nuevamente Monte Carlo ni se certificaron sus probabilidades.**

## Paso 0 — Archivos, estructura y hechos

[SD8](../08_plan_riesgos/LAFROX-Subdocumento8.md), [Anexos](../08_plan_riesgos/LAFROX-Subdocumento8-Anexos.md) y [T-16](../08_plan_riesgos/LAFROX-Formulario-T-16.md) están presentes y separados. Los nombres Markdown conservan el patrón exigido. T-16 está citado en la introducción y en 8.2.2; contiene los ocho campos de las Bases y 32 filas.

Están presentes, con el texto obligatorio y en orden, «Introducción a los Riesgos», «8.1 Plan de riesgos», «8.2 Identificación y Análisis de Riesgos» y «8.3 Plan de Acción a Riesgos». Los tres archivos terminan en «Referencias» y «Declaración de uso de IA», sin numeración. Hay prosa introductoria y conexión con anexos y formularios. **Observación menor:** el primer título «LafroX — Subdocumento 8: Plan de riesgos» va seguido directamente de «Introducción a los Riesgos»; si el primero se conserva como encabezado de contenido y no como portada, incumple la caída textual de Aclaraciones §3.

El cuerpo contiene seis tablas de dos a cinco columnas, una figura Mermaid y prosa explicativa; no es principalmente un catálogo. Las dimensiones físicas quedan pendientes del PDF. Tabla 8.1 «Rol | Ámbito de riesgos que vigila» se aproxima al formato «Concepto | Descripción» prohibido por §5: integrar los ámbitos en prosa o convertirla en una matriz de responsabilidad/autoridad.

Figura 8.1 **sí contiene ahora un diagrama**, con 32 identificadores, citado antes y explicado después. Se retira el hallazgo «RBS es una lista». Su inserción y legibilidad en PDF siguen pendientes; no se infiere que vaya a omitirse.

## Paso 1 — Causales duras

### H01 — Crítico: revisión humana pendiente en 15 filas

**Evidencia:** Declaración de uso de IA de los tres archivos: «[[REVISIÓN HUMANA]]». Conteo: **7 cuerpo + 7 anexos + 1 T-16 = 15**. El conteo anterior de 13 quedó desactualizado.

**Regla:** Aclaraciones §7.1 d incluye «cuadros de aprobación en blanco» y, desde Informe 2, establece 0 del subdocumento completo. §7.2 exige «Revisión humana (quién y qué verificó)». El primer paso del árbol del prompt fija 0 en S8.

El uso declarado de IA, incluso «Alto», no es por sí solo una causal. La observación es el marcador de revisión pendiente. Sólo un integrante puede registrar la revisión que efectivamente hizo; no corresponde inventarla ni rebajar niveles para aparentar cumplimiento.

La declaración del cuerpo agrupa «Anexos 8.A a 8.F» en una fila; §7.2 exige una por cada anexo asociado. En los anexos también se agrupan partes y se añaden filas de intervenciones. Reorganizar la cobertura por sección/anexo/formulario, preservando la verdad del uso. La fila 8.2 declara «Ninguno» en diagramas y otra declara «Medio (Figura 8.1 en Mermaid…)»: consolidar ambas para que el mismo contenido no quede con niveles aparentemente incompatibles.

### Otros controles duros

- **Sin precios de oferta detectados:** cero coincidencias de $, USD, CLP o UF en los tres archivos. HH y porcentajes no son precios. La remisión económica respeta Art. 50.2.
- **T-16 presente:** no se aplica causal de formulario ausente.
- **Meses contractuales:** H7 mes 16, H12 mes 21 y operación 21–56; no se identifica una propuesta expresa de plazos distintos del Art. 17.1.
- **RBS materializada en fuente:** no se aplica la antigua causal por figura que era sólo lista.
- **RPO:** alineación textual con SD4; suficiencia examinada abajo. No se presenta como ensayo aprobado.
- **Firma, folio y admisibilidad formal:** pendientes del PDF; no se sancionan como ausentes en estas fuentes.

## Paso 2 — Observaciones anteriores: estado verificado

El estado se funda en el texto actual, no en la nota posterior del informe antiguo.

| Observación anterior | Estado actual y evidencia |
| --- | --- |
| RBS en lista | Corregida en fuente: Mermaid, SD8 8.2.1 |
| Apetito no declarado | Corregida: «El apetito de riesgo del proyecto se fija por nivel de exposición», 8.1.3 |
| Concepción sin tratamiento | Corregida: R8-03, sitio, tres caminos y ensayo con todos cortados |
| Peak de septiembre sin ficha | Corregida: R8-18, septiembre 2028, habilitación en agosto y carga previa |
| Costo-beneficio genérico | Parcial: C.5 calcula 22 críticos; diez altos postergan cálculo |
| H9 ≥90 % | Corregida: 89,9 % en SD8 8.2.3/C.3, SD7 7.3.1 y T-15 Tabla 5.2 |
| H7 confundido con mes 21 | Corregida: R8-22/E8-07/T-16, H7 mes 16 y H12 mes 21 |
| Puente 9.336 frente a 16.664 HH | Aclarada: SD8 8.2.3 explica inclusión; SD7 conserva etiqueta amplia |
| Estimaciones sin procedencia | Mejorada: T-15 4.1/E8-01 remiten a T-12/T-11; productividad sigue siendo supuesto |
| CD-05/A31/A32 obsoletos | Corregida: INT-03/04, Anexo 4-I y 4-W |
| Cámaras en R8-21 | Corregida: «La solución no instala cámaras en cabina» |
| «13 puestos» en C-04 | Corregida: «Los 12 puestos simultáneos necesitan relevos» |
| Mitigación de R8-11 distinta en T-16 | Corregida: estimación por clase, dotación y seguimiento |
| Formato T-16 R8-31/32 | Corregida: plazo y remisión a ficha |
| Suspensión láctea sólo septiembre | Corregida: «de marzo a septiembre de 2026», 8.3.3/E8-08 |
| Voz de auditor y fichas comprimidas | Mejorada: retirados los descargos señalados; quedan abreviaturas menores |
| Citas sin correspondencia | Mejorada: fuentes bibliográficas citadas en los tres archivos |
| C.4 3.000 frente a C.3 5.000 iteraciones | No corregida; se explica, sin rehacer sensibilidad |
| Reserva de gestión sin magnitud | No corregida: Anexo 8.D no la expresa en HH |
| Revisión humana pendiente | No corregida; ahora 15 filas |

No se asigna porcentaje de corrección del Informe 1: falta la matriz oficial y SD8 no pertenecía a ese informe.

## Paso 3 — Revisión por título obligatorio

### 8.1 Plan de riesgos

**Desarrollado:** enfoque ISO 31000, ciclo, ocho responsables nominados, escalas P/I/D, calibración en HH, exposición/NPR, apetito, tolerancia, escalamiento y cierre con evidencia. RT-19.04 no se reduce a nombrar una norma. Los comités quincenales/mensuales y Operación desde mes 13 coinciden con SD6 6.1.6. La separación de problemas actuales en 8.E frente a eventos futuros debe conservarse.

**H02 — Grave: responsables de operación sin traspaso explícito.** SD8 Tabla 8.1 identifica DAT con Leandro Chamorro e IMP con Patricio Henríquez; 8.1.1 aplica el plan «durante los 56 meses». R8-27 asigna DAT y revisiones en meses 26, 32, 38, 44, 50 y 56; R8-29 asigna IMP y evaluación meses 24–27. SD1 Tabla 1.3 limita a ambos al mes 21. SD13 13.3.4/13.5.4 declara que las actividades posteriores pasan al frente de Operación de Guillermo Castillo, con aprobación de Calidad/Seguridad.

Las siglas de familia pueden mantenerse en EDT/T-15, pero una ficha necesita distinguir responsable efectivo del perfil que carga HH. SD8 deja la responsabilidad en nombres cuya dedicación terminó, sin explicar sucesión. Añadir regla temporal y reflejarla en R8-27/R8-29/T-16, sin renombrar automáticamente las familias.

**H03 — Media: horizonte de R8-11 incompatible con su respuesta.** Anexo 8.A R8-11: «Horizonte: hasta el H5»; su mitigación comprueba el peak mes 15 y las brechas SEG/IMP del T-15, incluida E2. H5 es mes 12. Extender el horizonte o separar E1/E2, recalibrando P si cambia la exposición.

### 8.2 Identificación y Análisis de Riesgos

**Desarrollado:** 32 amenazas en Solución 13 / Desarrollo 10 / Implantación 9; cinco categorías; obsolescencia, bloqueo, escalabilidad, ciberseguridad y contrapartes; FMEA, valor esperado, Monte Carlo y sensibilidad. Los siete asuntos del Caso cap. 19 están cubiertos: R8-13, R8-21 para sindicato y terceros, R8-20, R8-10, R8-03 y R8-18.

Las 32 fichas, B.1 y T-16 coinciden en P/I y exposición; fichas/FMEA coinciden en D. E=P×I y NPR=P×I×D son correctos en las 32 filas. Hay 22 críticos y diez altos. Mayores NPR: R8-01/07/27=80, R8-05=75, R8-02=60. El quinto empata con otros NPR 60: explicitar desempate por plazo, sin considerarlo error aritmético.

**H04 — Grave: Monte Carlo no demuestra factibilidad con recursos.** Anexo 8.C.3: «La simulación no nivela recursos en cada iteración: supone que el equipo asignado a un paquete se mantiene mientras se alarga». T-15 5.7 limita DES a «48 personas simultáneas» y ARQ/DAT a 15. Alargar un paquete puede ocupar especialistas cuando otro ya los necesita. Conservarlos en ambos sin volver a nivelar puede adelantar fechas artificialmente.

Coincidir con T-15 confirma consistencia documental, no capacidad realizable en cada escenario. Recalcular con calendarios/equipos compartidos/refuerzo autorizado, o presentar probabilidades condicionadas a capacidad adicional demostrada. P80 no prueba por sí solo cumplimiento del Art. 17.2.

**H05 — Grave: correlación y doble conteo no resueltos.** SD8 8.2.2: «Los mismos efectos o consumos no se contabilizan dos veces». C.3: «los efectos de varios riesgos sobre un mismo paquete se suman». No se muestran dependencias causales o estadísticas. R8-11/14/32 comparten capacidad y R8-10/15, interfaces/certificación.

Sumar impactos distintos puede ser válido; sumar dos representaciones del mismo efecto no. Falta mapa riesgo–paquete–impacto y regla para efectos comunes. PMBOK cap. 11, 11.4.2.2, indica modelar correlación ante causa común/dependencia lógica. No se declara tampoco si los eventos se sortean independientemente. La ausencia de doble conteo no queda demostrada.

**H06 — Grave: corrida sin evidencia suficiente para reproducir resultados.** C.3 muestra distribución, iteraciones, fechas de liberación y tablas; no semilla, configuración completa, asociación explícita de riesgos a la red, tratamiento de revisiones/feriados ni salida de ejecución. T-15 contiene 564 actividades y C.3 simula 163 paquetes: falta explicar cómo la agregación conserva precedencia por interfaz y simultaneidad interna.

Esto no demuestra que la simulación sea inventada. Impide verificar que se ejecutó sobre la red descrita. Entregar evidencia reproducible, incluso mediante anexo metodológico Markdown con parámetros, mapeos y resultados de control. Repetir la tabla no basta.

**H07 — Media: sensibilidad C.4 poco comparable.** C.4 usa 3.000 iteraciones, base H9=90,5 %; C.3 usa 5.000, H9=89,9 %. La nota explica el muestreo; no es contradicción de plazo. Quitar R8-19/R8-23 deja H9=89,9 %, por debajo de su propia base.

Con p=0,905 y n=3.000, error estándar binomial ≈0,54 puntos porcentuales; intervalo aproximado de 95 %: ±1,05 puntos. Una diferencia menor a un punto puede ser ruido, pero no queda probado automáticamente para todas las comparaciones. Rehacer con números aleatorios comunes/semilla controlada, mismo modelo y número de iteraciones, reportando incertidumbre. **5.000 no es una obligación contractual** ni elimina por sí solo el ruido.

**H08 — Grave: marchas blancas excluidas del riesgo general.** C.3 excluye R8-18/R8-22; SD8 8.2.3 excluye H6/H7/H11/H12 por su «mes fijo del Art. 17°». La exclusión es explícita y hay escenarios/reservas: ya no es hito olvidado. Pero la fecha fija es restricción, no ausencia de incertidumbre.

Los 28 días con seis condiciones copulativas y congelamientos pueden impedir el acta aun con H5/H10 a tiempo. Evaluar cierre dentro de la ventana fija, sin mover fechas. Probabilidades marginales de ocho hitos no equivalen a probabilidad conjunta de todo el contrato. Una reserva de HH no recupera automáticamente cuatro semanas de evidencia.

### 8.3 Plan de Acción a Riesgos

**Desarrollado:** las 32 fichas contienen estrategia, responsable, disparador, plazo, mitigación, contingencia, residual, secundario y evidencia. C.5 compara 22 críticos en HH y vincula controles con T-15. C-01/C-02 distinguen secuencia y paralelo; C-06 protege despacho y no confunde reversión de 40 minutos con RTO general.

**H09 — Grave: contingencia adicional fuera de la programación llamada línea base.** SD8 8.3.2 dice que «forma parte de la línea base» y fija **13.223 HH adicionales**. T-15 4.2–4.4 conserva **202.774 = 190.366 base + 9.336 puente + 3.072 protegidas**, sin curva de esas horas adicionales. Tabla 8.6 reparte valor esperado por períodos, pero no reserva perfiles, equipos o días disponibles para la parte adicional.

Incorporarla llevaría el total, con valores no redondeados, a **215.997,04 HH**. No se afirma que ese aumento esté autorizado ni que deba sumarse sin deduplicar consumos. Conciliar base y reserva por perfil/ventana/nivelación, o declarar inequívocamente cada línea base. La valorización puede ir en la económica; la capacidad debe demostrarse en la técnica.

**H10 — Grave: deducción de capacidad protegida sin ocurrencias elegibles.** La aritmética 15.076−1.853=13.223 es correcta; la elegibilidad no queda plenamente probada. R8-02 controla antes de H4 y R8-04 antes de H5; la capacidad protegida existe sólo meses 13–20. R8-04 llega además hasta mes 56. Se descuenta su valor esperado completo sin dividir impacto previo, durante o posterior a esa ventana.

Una pérdida antes del mes 13 no puede cargarse a capacidad posterior para demostrar cumplimiento del hito. Separar riesgos previos y correcciones de marcha blanca, por mes/perfil, descontando sólo parte absorbible. No sustituir 1.853 por otra cifra sin cálculo. R8-14 requiere justificar además cómo la capacidad de corrección E1 cubre su consecuencia sobre E2.

**H11 — Grave: horizontes largos cuantificados como un año sin fundamento.** B.2: «los paquetes recurrentes cuentan doce meses». R8-09/05/27 declaran 56 meses; R8-22 meses 13–56 pero usa doce meses de C-05. R8-09 toma **1.536 HH**, un año de 8.2.2/3/4; T-15 programa **4.608 HH** para esos paquetes en meses 21–56. R8-27 toma **1.056 = 960 construcción + 96 de un año**, frente a 288 recurrentes de 8.3.2 en operación.

Un evento único puede causar sólo un año de retrabajo: no hay que multiplicar mecánicamente por 36/56. Pero justificar ese límite y distinguir probabilidad de al menos una ocurrencia, número de ocurrencias y duración del impacto. Sin ello, el total y el remanente de sólo 51 HH después del mes 33 no acreditan cobertura completa.

**H12 — Media: reducción residual uniforme y “evitar” incompatible.** Salvo R8-22, las fichas bajan P un nivel tras verificar controles. Es hipótesis ex ante, no eficacia medida; controles distintos no garantizan igual reducción de 20 puntos de probabilidad. R8-14 dice «Evitar, porque separar los equipos elimina la causa», pero conserva P=3, 40 % y 672 HH residuales.

Si elimina la amenaza, precisar qué otra subsiste; si reduce probabilidad, denominar mitigar. Las 4.273 HH liberables dependen de esa hipótesis, no son ahorro demostrado.

**H13 — Grave: reserva de gestión sin dimensionamiento técnico.** Anexo 8.D: «Riesgos no identificados; no se expresa en HH en esta oferta técnica». 8.3.2 remite su monto a Oferta Económica. Se explica autoridad y exclusión de base, pero no capacidad ni efecto en calendario. T-7/Aclaraciones §11, 8.3 exigen contingencia **y gestión**, reflejadas en cronograma.

Art. 50.2 prohíbe precios, no HH, días o regla dimensionada de capacidad. Definir magnitud técnica justificada o mecanismo cuantificado con disponibilidad y autorización. La decisión previa de postergarlo no acredita cumplimiento.

**H14 — Media: costo-beneficio pendiente en diez altos.** R8-08/13/21/25/26/28/29/30/31/32: «su retorno se calcula si sube a nivel crítico». El índice no limita análisis a críticos. Puede priorizarse detalle, pero explicar elección frente a alternativas/aceptación.

C.5 sí analiza 22 críticos: retirar el antiguo hallazgo “ninguna ficha compara”. Costos compartidos de 1.3.4, 3.8.6 y 7.3.1 se agregan una vez en una cartera; los cocientes no son sumables. Un control obligatorio frente a cero cumplimiento tampoco representa alternativa conforme.

**H15 — Media: R8-22 sin escenario suficiente para demanda mayor.** C-05 usa 442 HH/mes y sube el límite de 2.283 a 2.391 contactos, coherente con SD4 4-W.7. No dimensiona demanda >2.391, otra concentración por intervalo o tiempos medios mayores. Su horizonte cubre operación, la reserva doce meses.

Definir siguiente umbral y capacidad escalable. Abandono/resolución al primer contacto se miden aparte; medir no autoriza a aceptar incumplimiento del SLA obligatorio. Es contingencia inicial, no cobertura de cualquier demanda.

## Paso 4 — Caso y matriz de decisiones cruzadas

Se contrastan decisiones actuales sin arrastrar contradicciones desaparecidas.

| Decisión | Evidencia cruzada | Resultado |
| --- | --- | --- |
| RTO ≤4 h / RPO ≤15 min | R8-05/E8-05; SD4 4.3.2.4; SD5 AL-DR-01 | Valores y residual coinciden; suficiencia condicionada |
| 99,95 % infraestructura / 99,9 % transacción | SD8 8.E; SD4 4.3; T-12 RNF-20.01 | Coherente; distinto de cero interrupción de despacho |
| Tres caminos en CD | R8-03/05; SD4 4.2.5.1; SD6 Tabla 6.3; T-14 5.3.3 | Fibra/LTE/Starlink; ya no se excluye Starlink |
| Sala técnica | R8-19/E8-02; SD6 6.1.3; T-15 5.2; T-14 | LafroX compra mes 2, instala mes 3, recepción mes 4; terreno CLIENTE |
| Cámaras en cabina | R8-21/T-16; SD3 3.4.6; SD6/T-14 5.4.2 | SD8 excluye; acta en SD6/T-14 aún dice «terminales, GPS y cámaras»: ambigüedad |
| Etapas | SD8 H7/H12; SD7 Tabla 7.5; T-18 | Producción E1 mes 16; E2 mes 21; operación 21–56 |
| H9 | SD8 Tabla 8.5/C.3; SD7 7.3.1; T-15 Tabla 5.2 | 89,9 % consistente |
| Dotación | R8-11/32; SD1; T-15 5.7; SD6 6.1.3 | Peak 69 y DES 48; refuerzo CAL hasta 16/día condicionado |
| Autonomía/TTL | R8-03/04; SD3; SD4 4-V; SD5 | CD 24 h, terreno 14 h; caché 24 h/manifiesto 26 h, sin confundir durabilidad |
| Arquitectura/ambientes | Riesgos SD8; SD4; SD6 6.2 | No se introduce otro stack, pipeline ni sexto ambiente |
| Guía de despacho | R8-01/C-06; SD3; SD4 AL-DTE-01; SD5 | ERP único emisor; papel no acredita continuidad crítica |
| Precio de pedido | SD8 8.E; SD2 S-09; SD3 RNG-08; T-12 RF-03.11/12 | Precio acordado al capturar |
| Reserva/retención | R8-02/06/E8-06; SD4 INT-03/04, 4-I/4-W.5 | Cuatro mensajes por línea como cota; multiplicidad a medir |
| Excursión térmica | R8-23/27; SD3 RNG-04; SD5; SD13 13.3 | Calidad decide; inferencia no amplía vencimiento ni rebaja bloqueo |
| Mesa | R8-22/C-05; SD4 4-W.7; T-15 5.6 | Horario 04:00–22:00 L–S y peak 24×7; capacidades consistentes |
| Innovaciones | SD8 8.F/R8-25–29; SD13/T-19 | Nombres y P/I coinciden; falta traspaso después de mes 21 |
| Contingencia | SD8 8.3.2/8.D frente a T-15 4.4 | Monto explicado, capacidad adicional sin curva |

La mención de cámaras en un acta puede referirse a prohibirlas o tratar la objeción. **No demuestra instalación**; se registra ambigüedad, sin convertirla en causal por decisión de diseño contradictoria probada.

**RPO residual:** SD4/SD8 reconocen tres caminos caídos y destrucción del sitio. Alarmas, preemisión y NAS local no crean una copia externa reciente después de esa secuencia. RT-02.11 exige declarar y justificar puntos de falla; **no deroga RT-07.04**. Se retira contradicción de redacción entre SD4/SD8, sin declarar demostrado ese RPO. Delimitar ensayo/frontera recuperable y tratamiento contractual de excepción; no considerar disponible un NAS destruido con el sitio. Es limitación arquitectónica compartida.

**C-07:** F=01-05-2028 y F=01-10-2028 son ejemplos F−28 pero anteriores a los tres primeros días hábiles permitidos. El texto manda aplicar la regla y T-15 4.1 usa H12 firmado el **5 de octubre de 2028**. Marcar los F como ejemplos aritméticos sin validez contractual o actualizar fechas/evidencia. No calificarlos automáticamente como oferta expresa de fechas inadmisibles.

## Paso 5 — Cálculos y trazabilidad

Se reconstruyeron las expresiones de B.2 y la tabla de 222 paquetes de T-15 4.2.

| Comprobación | Resultado |
| --- | --- |
| Base de 222 paquetes | 190.366 HH |
| Base + puente + protegida | 190.366+9.336+3.072=202.774 HH |
| R8-11 | 22.640×0,30×0,60=4.075,20 HH; base necesita selección trazable |
| R8-22 | 442×12×0,60=3.182,40 HH |
| R8-18 | (12×24×8+160)×0,60=1.478,40 HH |
| Total B.2 sin redondear | 15.075,84 HH →15.076 |
| Residual bajo hipótesis de bajar P | 10.802,56 HH →10.803 |
| Diferencia liberable bajo hipótesis | 4.273,28 HH →4.273 |
| Selección elegible actual | 460,80+384+1.008=1.852,80 HH →1.853 |
| Adicional declarada | 15.075,84−1.852,80=13.223,04 HH →13.223 |
| Top cinco | 10.204,80/15.075,84≈67,69 % →67,7 % |
| Reserva respecto a base | 15.075,84/190.366≈7,92 % |
| Suma de filas visibles Tabla 8.6 | 15.075 frente a total 15.076; nota de redondeo lo explica |
| Meses 7–33, filas visibles | 13.222/15.076≈87,70 % →88 % |
| C-05 | 17×26=442 HH; techo(442/128)=4 personas equivalentes |
| C-06 | máximo(10,30)+10=40 min; 04:45+40=05:25 |
| R8-09, base anual | (1.152+1.152+2.304)/36×12=1.536 HH |
| R8-27, un año recurrente | 960+288/36×12=1.056 HH |

Las diferencias de inicial/residual/ahorro en C.5 pueden ser redondeo separado. Ejemplo R8-05: 111−56 parece 55, pero ahorro sin redondear=55,68 →56. No se acusa error aritmético cuando ese cálculo lo explica.

**H16 — Media: base del riesgo de mayor exposición sin selección trazable.** R8-11 Fuente y EDT dice «222 paquetes,1.3.4»; B.2 usa 22.640 HH. Los 222 suman 190.366: 22.640 debe ser subconjunto/exposición distinta. Listar suma de paquetes y período, distinguiendo planificación total y esfuerzo afectado. El producto 4.075 es correcto; la base no se certifica por multiplicar bien.

**Cadena crítica de trazabilidad:** retiro y clientes en **menos de dos horas**, Caso cap. 18 → SD2 problema → T-12 RF-09.01/02, M9 y 3.4.4 → SD4 EPCIS/autoridades por sitio → SD5 5.1, presupuesto **85 minutos** y Anexo 5-J → SD7/T-18 resultados de marcha blanca → SD8 R8-16/23/27. Existe cadena documental. SD5 escribe «≤2 h»: conservar el límite estricto del Caso en la aceptación, aunque el presupuesto de 85 minutos queda por debajo. La acreditación se corta en resultados/aceptación de SD9/T-13/T-17 no recibidos. No confundir pruebas previstas con ejecutadas.

## Paso 6 — Forma y declaración

Citas y referencias APA mejoraron; ya no sostienen el hallazgo antiguo “sólo se citan cuatro fuentes”. Las Bases se verifican por documento/sección; páginas definitivas quedan reservadas al PDF.

El glosario de 8.A existe. Mejorar definición de AL-DR-01 y remisión desde el cuerpo, pero no tratar todos los códigos como indefinidos. «222 paquetes,1.3.4» y abreviaturas son defectos de edición; por sí solos no prueban generación íntegra por IA.

B.1 se cita como «Tabla B.1», sin leyenda numerada propia en el anexo; C.1 y otras tablas de anexos también carecen de título numerado. Numerar para evitar ambigüedad, sin declarar ausente una tabla existente. El límite de cinco columnas del cuerpo **no aplica** a anexos/formularios.

La RBS es única figura del cuerpo; no se inventa mínimo de figuras. Su recorrido explica ramas/categorías; necesidad de detalle depende de legibilidad final. La declaración debe representar el diagrama asistido y registrar revisión real.

## Paso 7 — Prioridades y cierre

Cada acción debe cerrarse con evidencia y conservar separadas las notas de revisión.

1. **Equipo humano:** revisar realmente las 15 filas; registrar nombre y verificaciones, reorganizando por sección/anexo/formulario. Es el bloqueo actual.
2. **JP/SRE/CAL:** conciliar adicional y T-15 por mes/perfil/nivelación; dimensionar gestión. Cierre: curva conciliada y autorización cuantificada.
3. **JP/DES/CAL:** separar ocurrencias absorbibles meses 13–20; justificar exposición recurrente. Cierre: riesgo–ventana–perfil–HH sin duplicación.
4. **JP/CAL:** modelo reproducible, correlación y recursos en escenarios; evaluar cierre de marchas blancas en calendario fijo. Cierre: parámetros/mapeos/resultados repetibles.
5. **JP/Operación:** relevo DAT/IMP y horizonte R8-11. Cierre: responsables compatibles con SD1/SD13.
6. **Líderes:** fundamentar residual, corregir “evitar” R8-14, analizar diez altos y escalamiento R8-22. Cierre: respuesta/reserva defendible por ficha.
7. **ARQ/SRE:** explicitar límite RPO, frontera y ensayo; no atribuir recuperación a copia local destruida.
8. **Edición final:** ejemplos F, leyenda B.1, Tabla 8.1/declaración y RBS en PDF. Comprobar paginación, firma y legibilidad con esa entrega.

SD8 contiene trabajo específico de Puelche y análisis desarrollado. No corresponde declararlo sin observaciones ni acreditar simulaciones, contratos o ensayos no recibidos. Las correcciones externas necesarias están identificadas; esta corrida no las aplica silenciosamente.

## Tabla final — Ítem 8 del Informe 2

| Ítem | Peso T-21 | Puntaje por prompt | Ponderado |
| --- | --- | --- | --- |
| 8. Plan de riesgos — T-16 | 10 % | **0/100** | **0,0 puntos** |

**Diagnóstico de contenido sin §7.1: 40/100**, por reservas sin capacidad demostrada y cuantificación insuficiente para factibilidad general. No se suma al puntaje. No se emite total del Informe 2: sólo se volvió a evaluar SD8.
