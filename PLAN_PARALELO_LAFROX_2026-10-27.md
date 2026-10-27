# Plan paralelo LafroX — cierre de los subdocumentos existentes

> **Reparto A–E sustituido:** para ejecución por cadenas sin esperas entre IAs, usar `PLAN_FRENTES_POR_DEPENDENCIAS_2026-10-27.md`. Este documento se conserva como detalle histórico de tareas; sus contratos K y su división por SD no son el reparto vigente. Olas0/5 fuera de la reorganización actual.

**Sí es viable repartir el trabajo entre varias personas con sus IAs.** La división recomendada es por dueño de subdocumento, agrupando las tareas de las olas 1–4, con entregas intermedias de datos. No repartir una ola completa a cada IA: eso haría que varias editaran los mismos documentos y mantendría dependencias innecesariamente seriales.

Estado: **reparto aprobado por el usuario, ampliado con fichas de cambios; la ejecución de correcciones todavía no se ha iniciado desde este chat**. Fecha: 27-10-2026.

## 1. Alcance y decisiones de partida

- Fuente del reparto: `C:/Users/henri/.claude/plans/me-aburr-de-revisar-rosy-treehouse.md`. Este archivo nuevo no modifica ese plan ni `REVISION_INTEGRAL_2026-10-27.md`.
- **Omitir íntegramente 1.1 para esta entrega:** no crear SD10, SD11, SD12, SD14 ni el T-8 incluido en ese punto. No considerar su ausencia un bloqueo de este cierre. Las remisiones existentes a esos capítulos se registran en el informe de revisión, pero no habilitan redactarlos ni certificar su contenido.
- Claude conserva exclusivamente la **aplicación de la ola 0** que ya está ejecutando. Que C1–C15 estén decididas no demuestra que sus cambios estén aplicados y compilados en todas las ramas.
- Se conserva el canon C1–C15, sin reabrirlo desde cada IA. Cualquier decisión adicional requiere aprobación humana y comunicación a los frentes afectados.
- La Declaración de IA del SD8 sigue siendo tarea **manual del equipo**, según C14. Ninguna IA inventa revisores, firmas, certificaciones renovadas ni resultados de pruebas.
- Las observaciones del plan fuente son pendientes de **revalidación tras la ola 0**, no una orden de repetir cambios ya resueltos.
- No se ejecutan commits, push, merges, creación de ramas, limpieza ni cambios de entregables por el solo hecho de crear este plan.

## 2. Camino rápido para el equipo

1. Dejar terminar a Claude; pedir su entrega de ola 0 por rama: SHA del commit, archivos, compilación y pendientes. No basta con el mensaje «canon cerrado».
2. Elegir responsables A–E. Cada persona abre su IA en una copia aislada y recibe este plan, el canon y el plan fuente.
3. Fijar una fotografía de entrada: commit de cada SD, versión del canon y archivos de Bases utilizados. Si los commits de Claude no están publicados, recibirlos por el medio acordado; **no partir silenciosamente del remoto anterior**.
4. Revalidar los hallazgos de cada frente; marcar los resueltos por ola 0 y trabajar sólo los restantes.
5. Entregar primero los acuerdos de datos de la sección 5; luego cerrar el resto de cada documento.
6. Un coordinador verifica cruces sobre commits concretos; cada dueño corrige su propio documento. Sólo después se integra y empaqueta lo autorizado para esta entrega.

Mientras Claude trabaja se puede leer el canon, revisar Bases y preparar diagnósticos en copias de lectura. **No editar ramas ni worktrees que Claude está usando.** El desarrollo de un verificador en una copia independiente es posible, pero sus resultados finales deben correr sobre la fotografía posterior a la ola 0.

## 3. Reparto recomendado: cinco frentes de escritura

Los nombres A–E son roles de reparto, no personas impuestas. Una persona puede llevar más de un frente, pero cada SD tiene **un único escritor**.

| Frente | Propiedad exclusiva | Primera entrega que desbloquea a otros | Trabajo posterior |
|---|---|---|---|
| A · Riesgos e innovación | SD8, SD13 y sus anexos/formularios | Riesgos, IDs, P7 y reservas conciliadas; matriz hacia SD7 | Análisis de riesgos, FMEA, respuestas, coherencia de innovaciones |
| B · Cronograma e implantación | SD7, T-14, T-15 y T-18; cualquier T-17 que efectivamente viva en su rama | Paquetes/hitos/fechas y responsabilidad de sala técnica; capacidad y reservas tras A/C | Cierre de cronograma, formularios, figuras y aceptación |
| C · Metodología y calidad | SD6, SD9 y formularios/anexos de esas ramas | Política de evaluadores, T-10, gobierno de calidad y programa DR | Alinear SD9/T-13/T-17 con decisiones finales y catálogo de D |
| D · Requisitos y datos | SD3, SD5 y formularios/anexos de esas ramas | Catálogo RF/RNF/RT, prioridades, retención y meta OTIF | Alinear SD5, datos, trazabilidad y referencias |
| E · Organización, caso y arquitectura | SD1, SD2, SD4 y sus formularios/anexos | Diccionario SD4/T-11, reversión, dotación y plan de renovación en SD1 | Forma, referencias, índices y revisión de arquitectura |

**T-17 no se identifica sólo por su número:** registrar su ruta y rama exactas. Si existen versiones en SD7 y SD9, B y C acuerdan cuál se entrega y cuál debe alinearse; nunca editar una misma copia desde ambos frentes.

### Si son menos integrantes

- **Cuatro:** A, B y C separados; una persona reúne D+E, entregando primero catálogo y diccionario.
- **Tres:** reunir A+B, mantener C y reunir D+E. Reduce coordinación de reservas, pero concentra carga en el primer frente.
- Con más personas, separar SD3 de SD5 o SD1/SD2 de SD4. No aumentar escritores dentro de un mismo SD sin separar archivos y acordar quién integra.

No se promete una aceleración numérica: el beneficio depende de la carga real y de la ruta crítica. El cierre seguirá esperando catálogo, riesgos/reservas, decisiones de calidad y su propagación.

## 4. Cobertura de los pendientes del plan fuente

Los números siguientes conservan los IDs originales para que se pueda comprobar que nada quedó sin dueño. Una tarea compartida se resuelve con entrega de datos, **no con permiso de escritura cruzada**.

| Frente | IDs de las olas 1–4 que debe revisar/cerrar en sus documentos |
|---|---|
| A | 1.2; parte SD8 de 1.4 y 1.7; 1.6; 2.1 (evaluación P7 y reservas), 2.7, 2.12, 2.13 (SD13), 2.14; 3.2, 3.8, 3.9, 3.10 (SD8: sólo coordinar revisión manual), 3.12 (T-19), 3.14, 3.16; 4.1–4.3, 4.5 (riesgo), 4.7 (I-04A) |
| B | 1.3; parte SD7 de 1.4 y 1.7; 2.1 (T-15), 2.2–2.4 (efectos en T-14/T-15), 2.6–2.13 según alcance SD7; 3.11, 3.12 (T-15), 3.16; 4.11 (efectos en programación/reserva) |
| C | 1.7 (SD6); 2.2–2.6, 2.9, 2.11–2.12 según alcance SD6/SD9; 3.1, 3.3, 3.9, 3.11 (SD6), 3.14, 3.16; 4.4, 4.5 (programa de pruebas), 4.11 (RV-012/018/020) |
| D | 1.5; 1.7 (SD3); 2.6, 2.11–2.13, 2.15, 2.16; 3.6, 3.9, 3.10, 3.15 (SD3), 3.16; 4.7 (requisito fuente), 4.8, 4.10 |
| E | 1.7 (SD1/SD2: modo de entrega); 2.7 (fuente SD4), 2.8 (fuente SD2), 2.10 (fuente SD4), 2.11–2.12, 2.15 (contraste SD2); 3.4, 3.5, 3.7, 3.9, 3.10, 3.12 (T-6), 3.13, 3.15 (SD2), 3.16; 4.6 (sólo SD1, no crear SD12), 4.9, 4.11 (datos SD1) |

Reglas para aplicar la tabla:

- 1.1 queda excluido: no se traslada a ningún frente.
- 1.3, 1.4, 1.6 y varios puntos de ola 2 podrían estar cerrados por la ola 0: comprobar, registrar evidencia y no rehacerlos.
- 3.15 requiere un acuerdo común antes de renumerar SD2/SD3; D y E no eligen estilos distintos.
- 3.16 aplica a **todos los SD existentes del alcance**, incluido SD13. Cada dueño revisa sus tablas; no hace falta esperar una auditoría global para comenzar.
- 4.10 no permite inventar revisión humana ni alterar estados de cumplimiento para que «cuadren». Verificar fuentes y escalar lo que requiera evidencia del equipo.
- Los textos dudosos no se «solucionan» borrando compromisos ni cambiando un pendiente real por una afirmación de cumplimiento sin respaldo.

### 4.1. Cómo ejecutar las fichas detalladas

Las fichas A01–E10 traducen los IDs originales en cambios ejecutables. **No son una auditoría nueva de las ramas posteriores a la ola 0.** Las ubicaciones y valores en conflicto provienen del plan fuente: hay que buscarlos en el SHA recibido y registrar la ruta vigente antes de editar. No aplicar un reemplazo porque todavía coincida un número de línea antiguo.

Para cada ficha, el responsable registra: estado inicial, fragmento o cálculo que respalda el hallazgo, archivos que realmente cambiará, resultado y comprobación. Si ola 0 ya lo corrigió, marcar «resuelto en K0» con SHA y evidencia. Si la fuente no permite resolverlo, elevar una pregunta concreta; no completar con datos inventados.

**Orden dentro de cada frente:** (1) revalidar K0; (2) publicar los datos que desbloquean otros frentes; (3) resolver contenido sustantivo; (4) propagar internamente a anexos, formularios y figuras; (5) revisar forma y compilación. No esperar a terminar toda la corrección editorial para entregar un dato estable.

### 4.2. Frente A — SD8, SD13 y T-16/T-19

**Objetivo:** dejar un catálogo único de riesgos, una evaluación explícita de los supuestos de SD7 y una reserva trazable, con SD13 citando ese mismo catálogo.

**Entradas:** K0; K4 de B; K3 de C para DR; K1 de E para nombres y arquitectura; K2 de D para OTIF. **Salida temprana:** K5, antes de terminar la edición de SD13.

| Ficha / origen | Dónde revisar | Cambio que debe hacer A | Comprobación de cierre |
|---|---|---|---|
| A01 · 1.2, 1.7 | SD8 `contenido.tex`, pasajes identificados en el plan fuente en líneas 79, 117, 171 y 183–202; `figuras/rbs.tex`; fuente del T-16 | Reescribir notas como «versión previa», «supuesto heredado», «se deben vincular» o «Corresponde obtener…» como contenido final sólo cuando exista una solución respaldada. Sustituir fuentes genéricas por la fuente real o el cálculo identificado. Un cálculo pendiente se resuelve o se informa al equipo como bloqueo, no se disimula | Cada pasaje tiene una respuesta verificable; no quedan notas de trabajo en los entregables ni afirmaciones sin respaldo |
| A02 · 1.4, 3.2, 3.8, 3.14 | Entradas `.tex`, portada T-16, `latexmkrc`, RBS y tablas de SD8 | Verificar C1 en fuentes y PDF; título «Introducción a los Riesgos»; corregir «riegos, debemos de definir»; rediseñar RBS para carta/oficio sin volver ilegible el texto; quitar numeración de tablas manual duplicada, actualizando sus remisiones | Compilación produce nombres correctos; RBS legible en tamaño final; tablas con número único y referencias correctas |
| A03 · 1.6, 2.14 | Catálogo de riesgos SD8, T-16, fichas INN-01…05 y citas de SD13 | Validar el mapeo creado por ola 0. Cada riesgo de adopción debe existir con ID `R-0xx`, descripción, P×I y responsable entre los ocho roles de C11. Identificar el equivalente real de `O8-01`; no transformarlo arbitrariamente en un riesgo. Corregir todas las citas y nombres, no sólo las 48 coincidencias históricas | Tabla de equivalencias antiguo → vigente → ubicación. Cada cita de SD13 llega a una ficha existente; sin IDs duplicados ni `R8-xx` residuales en entregables |
| A04 · 2.1 | Anexo 7.F (lectura), P7-01…P7-11; SD8 y T-16 | Evaluar los once supuestos: contenido, condición de validez, qué ocurre si falla, riesgo asociado, respuesta y disparador. Si varios P7 corresponden al mismo riesgo, explicitar la relación en vez de duplicarlo. Documentar por qué algún supuesto no genera riesgo adicional | Matriz de once P7, todos con evaluación o justificación; B puede seguir cada uno desde el Anexo 7.F hasta SD8 |
| A05 · 2.1, 4.3 | Reservas de SD8, T-16 y base K4 del T-15 | Preparar conciliación por riesgo: método, probabilidad/impacto y unidades; respuesta preventiva, contingencia, reserva asignada, rol, paquete EDT y hito afectado. Distinguir HH de costo monetario y de días de holgura; no sumarlos ni convertirlos sin supuesto explícito. Detectar reservas ya incluidas en paquetes y evitar doble conteo. Entregar a B diferencias respecto de K4 | K5 incluye detalle reproducible, total por unidad y diferencias explicadas contra T-15; ninguna remisión circular deja el cálculo «a cargo del otro documento» |
| A06 · 4.1–4.3 | Catálogo SD8, análisis y T-16; FMEA histórica en referencia local de SD8 antiguo | Incorporar riesgos de obsolescencia, bloqueo por proveedor y escalabilidad si siguen ausentes; vincular causa, evento, efecto, respuesta, responsable y plazo. Recuperar la FMEA como insumo, revisar escalas y aplicabilidad antes de reutilizarla; declarar método y cálculo de priorización. Añadir costo-beneficio de respuestas con supuestos y plazo, sin ampliar al modelo económico excluido | El método produce resultados reproducibles; cada riesgo nuevo tiene respuesta y seguimiento; T-16 contiene plazo y vínculos EDT/hitos verificables |
| A07 · 2.7, 4.5 | Continuidad en SD8 y escenarios DR; K3 de C | Alinear RTO/RPO y medios de demostración a C8. Evaluar el riesgo de programar tarde la primera prueba real de DR contra el calendario vigente; si K3 ya adelanta la prueba, actualizar el riesgo residual y el disparador. No reintroducir la salvedad excluida por C8 ni presentar una prueba planificada como ejecutada | SD8 describe el mismo programa que SD9; la valoración residual y las reservas tienen sentido con ese programa |
| A08 · 2.12–2.13, 3.9, 3.12, 4.7 | SD13: Tabla 13.1, I-04A, T-19, B-08 y remisión «transferencia desde el mes 22» | Usar nombres de K1; título oficial «Cartera de innovaciones»; completar «sostenibilidad» en tipo 5 si corresponde al índice/fuente. Actualizar I-04A al criterio OTIF recibido en K2, distinguiendo umbrales intermedios y objetivo final. Verificar transferencia con K6, sin fijar mes por copia del plan antiguo. Resolver citas según C13 | T-19, indicadores y cuerpo coinciden; OTIF usa la misma desigualdad, período y alcance que SD3; cada remisión llega a contenido real |
| A09 · 3.10, 3.16, 5.2 | Declaración de IA SD8; tablas del cuerpo SD8/SD13; restos de plantilla SD13 | Aplicar ficha transversal 4.7 en ambos SD. Preparar para el equipo la lista exacta de filas de IA que requieren edición manual en SD8, sin firmarlas. Limpiar sólo archivos confirmados fuera de uso | Revisión manual SD8 efectuada por el equipo; informe de tablas y PDF revisado; ninguna evidencia necesaria se elimina |

**Entrega final de A:** SD8/SD13 y formularios consistentes; mapeo de IDs; evaluación P7; FMEA/método; conciliación de reservas; lista de cambios comunicados a B/C/D. Se puede entregar K5 sin esperar el cierre visual de la RBS o de T-19.

### 4.3. Frente B — SD7, cronograma y formularios

**Objetivo:** que calendario, dotación, reservas, entregables y aceptación describan un mismo plan ejecutable, sin cambiar políticas de otros dueños.

**Entradas:** K0, K1 y datos de dotación de E; K3 de C; K5 de A. **Salidas:** K4 con la base actual primero; K6 con la versión conciliada después.

| Ficha / origen | Dónde revisar | Cambio que debe hacer B | Comprobación de cierre |
|---|---|---|---|
| B01 · 1.3, C4 | `subdocumento-07/contenido.tex`, T-14, T-15, T-18 y protocolos de aceptación que vivan en SD7 | Validar dos actas por etapa: cierre de marcha blanca al final de mes 15/20 habilitando pasos del 05-05-2028/05-10-2028; aceptación H7/H12 el 29-05-2028/25-10-2028 en mes 16/21. Incorporar el acta de cierre como entregable de 4.2.1/4.3.1 si falta. Demostrar encaje de revisión/subsanación sin recortar la evidencia requerida. Resolver, no sólo borrar, «requiere reprogramar» y «La carta no demuestra…» | Una línea temporal por etapa identifica evidencia, entrega, revisión, firma, paso a producción y aceptación; C recibe las mismas fechas |
| B02 · K4, 2.1 | T-14/T-15, Anexo 7.F, hitos y tablas de reservas | Entregar primero base por paquete: HH, rol, meses, entregable, hito, reserva y unidad. Recibir P7/K5 de A, reflejar reserva y actividad de respuesta donde corresponda; recalcular carga mensual y holguras. Explicar diferencias entre reserva de gestión, contingencia y holgura si se emplean esas categorías | K4 y K6 identificables por SHA; reconciliación muestra valor anterior/nuevo, causa y riesgos cubiertos; sin doble conteo |
| B03 · 2.2–2.4, 4.11 | T-14 6.1.1; T-15 `contenido.tex` y `tab_T15_8`; RV-012/018/020 de SD6 (lectura) | Confirmar y comunicar responsabilidad CLIENTE/mes 3 de sala técnica contra fuente vigente, sin confundir obra civil con instalación. Alinear SOC con C6. Con K3, ajustar o retirar la atribución no respaldada de evaluadores; modelar personas, días, horas y períodos por separado. Reconciliar 40/48 desarrolladores y reserva de 1.600 HH con E/C/A, sin fijar un número por mayoría | C puede corregir adquisiciones usando K4; capacidad calculada con jornada/días explícitos; reserva y dotación consistentes entre fuentes |
| B04 · 2.6–2.9, 2.13 | T-14 1.5.2; T-18; SD7 pasajes de dotación/congelamiento/continuidad | Verificar las tres coberturas C7 con su alcance; C8 sin salvedades; congelamiento C9 sin prohibir todo septiembre; C5 distinguiendo preparadores, conductores y tripulación; «M12 Telemetría» y nombres K1. Propagar a tablas, diagramas y notas, no sólo a párrafos | Búsqueda contextual más comprobación cruzada contra canon; cada número conserva unidad, lugar y población a la que se refiere |
| B05 · 2.10 | `tab_SD7_7` y explicación del procedimiento de reversión | Separar mecanismo automático descrito en K1 de responsabilidad operativa del SRE: supervisión, escalamiento, validación o activación manual sólo si la fuente lo contempla. No presentar al SRE como ejecutor manual obligatorio de un paso automático | Flujo y tabla describen el mismo mecanismo que SD4, con rol humano inequívoco |
| B06 · 2.11–2.12, C15 | Remisiones SD7/T-14/T-15/T-18 a SD3/SD4/SD9 y referencias a secciones de formularios | Verificar destinos de SD4 4.1.4.4, 4.2.4.1.2, 4.3.2.4 y Anexo 4-W.7, y SD3 3.4.3–3.4.5/Anexo 3.I donde se citen. Sustituir números históricos por los destinos realmente encontrados. Mantener formularios desde sección 1; coordinar con C la sección real del T-13/T-17 | Inventario origen → destino → título/label → SHA; no basta con que el número exista: debe respaldar la afirmación |
| B07 · 3.11 | Diecisiete láminas EDT y lámina que amplía la 3.10; texto circundante | Añadir llamada previa `\ref` y explicación de lectura de cada figura; definir vista general y detalles sin duplicar numeración ni prometer ampliaciones inexistentes. Cambiar etiquetas sólo si hace falta y actualizar todos sus usos | Ninguna lámina aislada; referencias correctas y texto/figuras legibles en PDF |
| B08 · 1.4, 1.7, 3.12 | Entradas/portadas/configuración; T-15 `tab_T15_3`; T-14 y Anexo 7.B | Verificar nombres C1; añadir columna «N° de personas (peak)» en T-15 conservando plantilla oficial y calcular el peak desde dotación real, no desde HH acumuladas. Corregir fuentes genéricas y texto preliminar según evidencia. Evaluar `tab_T15_contingencia.tex`/`tab_T15_11`: identificar usos y preservar cálculos antes de retirar huérfanos | Nombres de PDF correctos; peak reproducible; cero inclusiones rotas por limpieza; formato del formulario verificado |
| B09 · 3.16, 5.3 | Todas las tablas del cuerpo, incluida `tab_SD7_7` (M8); metadatos | Aplicar 4.7; mover detalle excesivo al anexo/formulario manteniendo una síntesis útil y sus remisiones. Aplicar sólo la ficha común de metadatos aprobada por coordinación | Cuerpo revisado tabla por tabla; numeración, referencias, cronograma y figuras siguen coherentes tras los movimientos |

**Entrega final de B:** K6, cálculos de capacidad/reservas/holguras, tabla única de hitos y actas, documentos y figuras actualizados. Enviar a A/C la lista de valores o secciones que cambiaron desde K4.

### 4.4. Frente C — SD6, SD9, metodología y pruebas

**Objetivo:** que lo prometido en calidad tenga respaldo en metodología/T-10, capacidad y calendario, y que cada requisito tenga trazabilidad sin inventar resultados de ejecución.

**Entradas:** K0, K1, K2, K4 y finalmente K6. **Salida temprana:** K3 con decisiones respaldadas; las propuestas no aprobadas se identifican como tales fuera del entregable final.

| Ficha / origen | Dónde revisar | Cambio que debe hacer C | Comprobación de cierre |
|---|---|---|---|
| C01 · 2.2–2.3 | SD6 `tablas/adquisiciones.tex`, `contenido.tex`; T-9 y referencias a T-14 | Confirmar SOC propio C6, contratación antes de mes 13 y estado coherente de RT-11.17. Corregir sala técnica a partir de K4 y fuente: responsable, actividad y mes, distinguiendo habilitación/obra e instalación. No mantener una subcontratación del SOC por inercia del texto anterior | SD6 y T-15/T-14 no se contradicen en responsable, modalidad ni fecha |
| C02 · 2.4 | SD6 sección citada como 6.1.3; SD9 pasajes históricos 291/303/324; T-15 `tab_T15_8` (lectura) | Verificar respaldo de «hasta 16 evaluadores subcontratados por día». Preparar decisión para el equipo: incorporar compromiso justificado con rol, período, jornada y contratación, o corregir/eliminar la atribución no respaldada y recalcular capacidad con B. No elegir unilateralmente. Tras aprobación, alinear SD6, SD9 y anexos propios | K3 especifica personas/día, días, horas y meses o declara retiro aprobado; B dispone de insumos suficientes para reproducir capacidad |
| C03 · 2.5–2.6 | T-10; SD6; SD9 métricas y Anexo 9.A | Incorporar umbrales de duplicación ≤3 % y acoplamiento ≤20 si siguen siendo compromisos aprobados y faltan en T-10; definir qué se cuenta, ámbito, herramienta y puerta. Si la fuente no avala su semántica, elevar la precisión antes de publicar. Mantener las tres coberturas C7 diferenciadas; no confundir global con código modificado | Cada umbral de SD9 tiene fuente y método; T-10 y Anexo 9.A usan misma métrica, desigualdad, alcance y condición bloqueante |
| C04 · 4.4 | SD6/T-9, SD9 marco de gobierno y referencia al Art. 71 | Contrastar «Comité de Calidad y Procesos» y su veto con el gobierno ya aprobado. Proponer al equipo incorporación explícita de autoridad interna o ajuste del texto a roles/atribuciones existentes, sin atribuir a las Bases un poder que no se encuentre allí. Propagar la decisión en ambos SD | No queda un órgano con poder exclusivo en un solo documento; K3 identifica composición, función, escalamiento y fuente de autoridad aprobada |
| C05 · 4.5, C8 | SD9/T-13 calendario de DR, resiliencia y evidencias; SD6 estrategia; K4/K6 | Revalidar si persiste la primera prueba real en mes 21. Programar demostración coherente con C8 antes de H5/H10 y la periodicidad aplicable; precisar ambiente, alcance, prerrequisitos, RTO/RPO medidos, evidencia y criterio de salida. Comunicar a A riesgo residual y a B paquetes/capacidad requeridos. No fijar una fecha que choque con K6 o congelamientos | Programa de pruebas y cronograma coinciden; cada paso a producción tiene evidencia previa planificada; no se presenta una simulación como conmutación real |
| C06 · 2.9, 4.11 | T-10 congelamientos; SD6 RV-012/018/020; SD9 capacidad | Corregir congelamiento a C9. Revisar 40/48 desarrolladores con E; contingencia DTE con arquitectura K1; reserva de 1.600 HH con K5/K6. Explicar naturaleza, alcance y consumo de la reserva en vez de duplicarla como capacidad adicional | Los tres RV tienen respuesta documentada; números y mecanismo DTE coinciden con sus dueños; ninguna prueba programada vulnera ventanas aplicables |
| C07 · 2.11–2.12, K2 | T-13, matriz de requisitos, generadores y verificadores existentes de SD9; T-17 | Recibir K2 y regenerar/revisar el enlace requisito → caso → criterio → hito. Separar requisitos, filas/alias, estados ofrecidos y casos previstos; justificar exclusiones según estado sin borrar IDs. Verificar destinatarios de citas de SD3 a T-13 y de SD4 a T-13; publicar las secciones correctas a D/E. Alinear T-17 y calendario con K6 y C4/C15 | Conteos reproducibles desde K2; matriz sin huérfanos ni casos duplicados accidentalmente; evidencias «previstas» diferenciadas de resultados reales; aceptación coherente con B |
| C08 · 3.1, 3.3, 3.9, 3.14 | SD6 entrada de capítulo, cierre, referencias; T-9; Anexo 6.B | Título «Metodologías»; Referencias y Declaración de IA sin número y con texto de entrada/cierre pertinente. Resolver cita de Kruchten según fuente realmente utilizada y C13. Completar frase inconclusa del T-9; corregir numeración 6.A.2 dentro de 6.B y todas sus remisiones | Índice y PDF muestran estructura exigida; sin citas indefinidas, frases truncas ni tablas con prefijo de otro anexo |
| C09 · 1.7, 3.11, 3.16 | SD6 `anexos.tex`, `tablas/adquisiciones.tex`, `comunicaciones.tex`, `interesados.tex`; tablas/figuras de SD6/SD9 | Revisar fuentes genéricas; planificar e incorporar figuras metodológicas que expliquen procesos realmente descritos, según exigencia comprobada de las Aclaraciones, sin figuras decorativas. Añadir llamada previa, explicación y declaración IA veraz. Aplicar 4.7 en ambos SD | Figuras útiles y legibles; fuentes trazables; tablas y referencias coherentes tras edición; revisión humana no inventada |

**Entrega final de C:** K3 aprobado, SD6/T-9/T-10 consistentes, SD9/T-13/T-17/anexos alineados, matriz y conteos verificables, calendario de pruebas con evidencia prevista y capacidad respaldada. Entregar a D/E los nuevos destinos de las remisiones.

### 4.5. Frente D — SD3, SD5, requisitos y datos

**Objetivo:** estabilizar el catálogo que consumen las pruebas y corregir los compromisos de datos sin alterar IDs o estados para esconder brechas.

**Entradas:** K0, K1; dotación y fuentes de caso de E; secciones T-13 de C y T-18 de B. **Salida temprana:** K2, versionado antes de la regeneración de matriz de C.

| Ficha / origen | Dónde revisar | Cambio que debe hacer D | Comprobación de cierre |
|---|---|---|---|
| D01 · K2, 4.8, 4.10 | SD3, T-12, anexos y archivos de catálogo vigentes | Extraer inventario RF/RNF/RT con ID, prioridad, estado, fuente y ubicación. Separar requisito único de fila/alias; reconciliar totales del texto y tablas. No adoptar los 261/645 del plan SD9 antiguo ni los 36 parciales/22 no cumple del diagnóstico sin recontar el SHA actual | K2 incluye conteos por clase/prioridad/estado, duplicados y alias explicados; C puede reproducir los totales desde los archivos publicados |
| D02 · 2.15 | SD3 introducción, RNG-04 y pasajes de retención; SD2 S-04 (lectura) | Determinar granularidad de la retención según Caso/Bases y fuente SD2: lote, SSCC o relación entre ambos. Corregir definiciones y reglas donde se contradigan; si difieren por escenario, escribir alcance y vínculo explícitos en lugar de reemplazo global | Una regla de negocio inequívoca con fuente; el modelo SD5 y E/SD2 reciben el mismo criterio |
| D03 · 4.8 | RF-14.01…05, RNF-04.01, S-22 y sus matrices | Resolver alcance de flota propia/terceros con fuente exacta; no transformar cifras de vehículos en conductores/tripulantes. Sustituir «tiempo acotado» por condición medible respaldada o propuesta pendiente de aprobación; resolver cinco/seis sitios con definición del universo. Para colisión de IDs caso/Bases, distinguir origen y mapeo sin renumerar ciegamente | Cada conflicto tiene fuente, regla y actualización en T-12; no hay requisito con alcance ambiguo ni colisión ocultada; impactos enviados a C/A/E |
| D04 · 4.7 | Meta OTIF SD3, indicadores y remisión hacia I-04A | Verificar «sobre 95 %» frente a «95 %» con la fuente del Caso. Precisar desigualdad, fórmula, período y alcance; conservar hitos intermedios cuando apliquen, sin sustituir toda meta por un único valor. Enviar definición final a A | K2 permite evaluar pasa/no pasa sin ambigüedad; SD13 puede actualizar I-04A sin reinterpretación |
| D05 · 2.6, 2.13, 2.16 | SD3 inicio del contrato, coberturas, glosario; SD5 referencias tecnológicas y meses | Verificar C3 febrero 2027 y C7 completo en SD3; glosario según K1. En SD5 sustituir el nombre tecnológico obsoleto por el oficial y escribir «mes N» donde corresponda; evitar reemplazar IDs de módulos que también usan M | Fechas, alcances de cobertura y términos coinciden con canon; IDs técnicos quedan intactos |
| D06 · 1.5, 3.9 | SD5 `partes/referencias_ia.tex`, `contenido.tex`, `5_1_modelo.tex`; SD3 cita «Ministerio de Salud, 1996» | Recuperar del historial previo a `2f936555` sólo el contexto que permita reconstruir citas borradas; no revertir íntegramente mejoras posteriores. Reconstruir autor/año/título de fuentes reales y sus llamadas. Retirar referencias propias según C13, sustituyéndolas por remisiones válidas. Resolver la cita sanitaria según lo efectivamente consultado | No hay huecos como «Caso  y …», fuentes sin identificar ni citas huérfanas; cada entrada tiene uso justificado |
| D07 · 2.11–2.12 | SD5 sección 5.1.7 hacia M9; SD3 hacia T-13/T-18 y destinos internos | Usar K1 para ubicar M9, en vez de perpetuar «4.1.4.8»; recibir destinos efectivos de C/B para T-13/T-18. Revisar secciones 3.4.3–3.4.5/Anexo 3.I citadas por otros frentes y comunicar cambios de numeración | Todas las remisiones apuntan al contenido correcto sobre el SHA acordado; A/B/C/E reciben destinos estables |
| D08 · 4.10 | SD5 `revision/`, modelo y notas con 139/121 entidades; T-12 | Contar entidades con definición explícita (lógicas/físicas, tablas u otra); explicar o corregir diferencias. Revalidar hallazgos de revisión, estados parciales/no cumple y ampliaciones. Solicitar evidencia humana faltante; no declarar revisado algo sólo porque una IA corrigió el texto | Conteo reproducible y criterio documentado; estados reflejan alcance ofertado real; bloqueos humanos identificados fuera de la versión final |
| D09 · 1.7, 3.6, 3.10, 3.15–3.16 | SD3 `tablas/sint_epicas.tex`; títulos 3.3.2/3.3.3 en `minipage`; introducciones 3.1.1/3.4.1/3.4.5/3.4.6; anexos SD3 y tablas SD5 | Reubicar títulos para estructura e índice correctos; integrar párrafos de frío tras una introducción y con secuencia lógica. Fuentes concretas; C14 sin «No aplica». Acordar estilo de anexos con E antes de renumerar; actualizar labels/remisiones y aplicar 4.7 en ambos SD | Índice correcto; sin párrafos pegados fuera de contexto; anexos con estilo acordado; tablas y declaraciones revisadas en PDF |

**Entrega final de D:** K2 y su método de conteo, SD3/T-12/SD5 coherentes, definición de retención y OTIF, conciliación de entidades y lista de remisiones cambiadas. Un cambio posterior del catálogo debe notificarse como nueva versión a C, indicando el delta de IDs.

### 4.6. Frente E — SD1, SD2, SD4 y fuentes transversales

**Objetivo:** estabilizar vocabulario, arquitectura, dotación y organización que consumen los demás frentes, además de cerrar sus observaciones formales.

**Entradas:** K0; decisiones de C para evaluadores/gobierno; destinos de T-13 de C; criterio de retención de D. **Salida temprana:** K1 y ficha de dotación/organización; no esperar a corregir toda la redacción de SD4.

| Ficha / origen | Dónde revisar | Cambio que debe hacer E | Comprobación de cierre |
|---|---|---|---|
| E01 · 2.7, 2.10, 2.13 | SD4/T-11, catálogo de componentes, continuidad y pipeline | Publicar nombres oficiales de módulos/componentes (incluidos M12, B-08 y ElastiCache), destinos verificables y procedimiento de reversión. Precisar automatismo, condiciones, rol SRE y umbral existente; separar reversión técnica de otras reversiones si son métricas distintas. Verificar RTO/RPO y medios de C8 | K1 cita archivo/sección/label y SHA para cada dato; B/C/D/A no necesitan deducir nombres ni comportamiento de párrafos contradictorios |
| E02 · 2.8, 2.15 | SD2 S-39/S-04; SD1 organización; cifras enviadas a B y D | Verificar C5: 120 preparadores Talca y 60 Concepción; ≈200 conductores frente a ≈244 tripulación, con desglose y fuente. Distinguir cantidad de camiones de personas. Contrastar retención con D; corregir SD2 sólo si el contraste con fuente lo exige | Ficha con métrica, unidad, lugar y universo; B actualiza sus pasajes sin mezclar poblaciones; SD2/SD3 no se contradicen en retención |
| E03 · 4.6 | SD1 certificados, vigencias y compromisos de personal/organización | Revalidar CMMI nov-2026, ISO 27001 ene-2027 y AWS mar-2027 contra evidencias disponibles. Incorporar plan de renovación: objeto, responsable, fecha objetivo respecto al contrato, actividad, evidencia exigida y contingencia si no se obtiene a tiempo. Distinguir certificación de empresa/persona y no afirmar una renovación inexistente | Plan verificable en SD1, sin crear SD12; cada vigencia tiene fuente y revisión humana de respaldo |
| E04 · 4.11, C7 | SD1 dotación y política de calidad; T-6; SD6 RV-012 (lectura) | Aclarar si 40/48 desarrolladores corresponde a conceptos/períodos distintos o a error; publicar desglose aprobado para C/B. Completar/verificar las tres coberturas C7 en SD1. Recibir decisiones de C que afecten organización; no añadir evaluadores a la dotación como si ya estuvieran aprobados | Dotación explicada por rol y período; capacidad de B no usa universos incompatibles; política de calidad alineada |
| E05 · 3.7 | SD2 `contenido.tex` pasajes históricos 66–67, `anexos.tex` 163 | Reformular «Decisión que requiere la necesidad» y «Decisión del proponente» para distinguir problema/necesidad de solución. Conservar evidencia, restricciones y consecuencias del caso; remitir a la solución en su SD cuando proceda en vez de describirla como problema original | Capítulo 2 explica qué necesita el cliente y por qué, sin presentar decisiones ofertadas como hechos del caso |
| E06 · 3.4, 4.9 | SD4 partes `02_b`, `02_a`, `11_j`, `12_k`, `06_e`; sección 4.3.1 | Añadir frase de entrada pertinente a listas tras `\paragraph*`; sustituir «La tabla distingue…» cuando en realidad sea una lista. Aclarar por qué una sección de Data Center Primaria incluye sala secundaria Talca y delimitar ambos objetos sin cambiar arquitectura por una corrección editorial | Listas con contexto; ninguna llamada al tipo de objeto equivocado; ubicación y función de salas inequívocas |
| E07 · 3.13 | SD4 montaje, encabezados 4.1/4.2/4.3, `00/trazabilidad/PENDIENTES.md` | Corregir jerarquía de capítulo/secciones para un solo capítulo 4 coherente con índice obligatorio. Revisar contadores y todas las referencias impactadas. Antes de publicar K1 final, avisar si la corrección cambia números citados por otros SD | Índice y PDF no crean capítulos extra; labels estables cuando sea posible; tabla antiguo → nuevo enviada a consumidores |
| E08 · 2.11–2.12 | T-11 remisión histórica 4.1.3.5 para M9; SD4 `11_j` hacia T-13; destinos SD4 citados por TRZ | Corregir M9 usando la sección realmente localizada; recibir de C la sección de T-13 que respalda cada afirmación. Publicar destinos SD4 4.1.1, 4.3.2.4, 4.2.6 y 4.1.3.5 para verificación de TRZ, sin editar TRZ fuera de asignación | Origen y destino semánticamente alineados; coordinación puede verificar TRZ sin inventar equivalencias |
| E09 · 3.5, 3.9–3.10, 3.12, 3.15 | SD2 anexos entre tablas 2.A.1/2.A.2; declaraciones SD1/SD2; T-6 campos y citas | Introducir/analisar tablas consecutivas; completar cierre de declaración IA SD1; usar «Ninguno» para diagramas de secciones SD2 sin figuras y C14 en SD1. Restaurar rótulos oficiales del T-6 sin inventar experiencia. Resolver «2026c/2026d» por C13 o fuente real; acordar anexos con D | Campos contrastados con formulario oficial; declaraciones fieles; citas resueltas; estilo de anexos consistente y remisiones actualizadas |
| E10 · 1.7, 3.16, 5.2–5.3 | Modos de salida SD1/SD2, tablas SD1/SD2/SD4, restos SD4/SD1, metadatos y clases | Aplicar 4.7 y preparar propuesta común de fecha, versión, título/subtítulo y formato. Comparar diferencias de clase, especialmente SD3, sin sobreescribir adaptaciones locales a ciegas. Inventariar restos antes de retirar plantillas/PDF antiguos/PNG; preservar evidencia útil. No confundir opción técnica de compilación con nota de borrador en el contenido | Ficha común aprobada antes de propagación; revisión visual tras cambios; cero borrados que rompan inclusiones o eliminen evidencia |

**Entrega final de E:** K1, ficha de dotación, plan de renovación SD1, SD1/SD2/SD4 y formularios corregidos, mapa de renumeración si existe y propuesta de metadatos. E no impone unilateralmente la clase común a los demás frentes.

### 4.7. Ficha transversal obligatoria — repetir en cada SD de A–E

Esta ficha concreta 3.16 y el cierre formal sin generar un sexto escritor. Cada responsable la aplica a **todos sus SD**, incluidos anexos/formularios en lo que corresponda a las Bases.

1. **Inventariar tablas del cuerpo:** archivo, label, título, columnas, extensión en PDF, tipo de contenido, fuente, llamada previa y análisis posterior. Comprobar las restricciones descritas por el plan fuente contra la Aclaración aplicable antes de decidir el traslado.
2. **Rediseñar, no sólo encoger:** ante tablas «Concepto | Descripción», celdas extensas, exceso de columnas o de páginas, convertir explicación en prosa o mover detalle al anexo/formulario permitido y dejar síntesis en el cuerpo. No usar letra ilegible ni mover un formulario obligatorio de lugar para eludir su formato.
3. **Actualizar enlaces:** al mover tablas/figuras o renumerar, mantener labels o actualizar todos los usos. Toda tabla/figura tiene llamada previa, fuente verdadera y explicación de lo relevante; no reemplazar una fuente genérica por una cita inventada.
4. **Revisar índice y cierres:** títulos y orden contra el índice oficial; Referencias/Declaración sin numeración cuando corresponda; formularios desde sección 1; figuras y tablas con numeración única y tamaño final legible.
5. **Aplicar C13/C14 contextualizadamente:** referencias propias como remisiones y fuentes externas bien identificadas; niveles de IA veraces por sección. «Alto» no permite inventar quién revisó; SD8 conserva su revisión manual asignada al equipo.
6. **Buscar y clasificar marcadores:** `pendiente`, `borrador`, `heredado`, `versión previa`, `??`, `[cite`, `TODO`, entre otros del plan fuente. Distinguir texto inadmisible de usos legítimos (p. ej., un estado del flujo de defectos). Cada coincidencia se justifica o corrige; no exigir cero palabras a costa del sentido.
7. **Separar fuente de resultado:** recalcular cuando cambien entradas, regenerar figuras/tablas derivadas y compilar de nuevo. Entregar evidencia de compilación e inspección visual, no sólo existencia de PDF.

**Registro mínimo por tarea:** `Ficha | IDs fuente | SHA inicial | ruta y sección | cambio aplicado o resuelto en K0 | verificación | dato comunicado a otro frente | bloqueo`. Los informes auxiliares se guardan separados de los PDF de entrega; no insertar notas de coordinación en el contenido final.

## 5. Dependencias: qué se entrega antes de continuar

| Contrato | Productor → consumidores | Contenido mínimo / condición de aceptación |
|---|---|---|
| K0 · Base común | Claude/coordinador → todos | Canon, SHA por rama, cambios de ola 0 y estado de compilación; recepción confirmada |
| K1 · Diccionario técnico | E → B, C, D, A | Nombres SD4/T-11, destinos de remisiones, comportamiento de reversión y compromisos de continuidad; sección/label verificados |
| K2 · Catálogo de requisitos | D → C, A | IDs RF/RNF/RT, estados y prioridades con conteos reproducibles, criterio retención y OTIF; no reutilizar cifras del plan SD9 antiguo |
| K3 · Políticas de calidad | C → B, E | Evaluadores: decisión y respaldo; umbrales del T-10; comité/veto; programa DR consistente con C8; datos o decisiones pendientes separados de acuerdos aprobados |
| K4 · Base de programación | B → A, C | Paquetes EDT, hitos y reservas/capacidad actuales; sala técnica; dos actas de C4; evidencia y plazos de revisión |
| K5 · Riesgos/reservas | A → B, C | P7 evaluados, IDs y equivalencias, cálculo de reserva sin doble conteo, HH/unidades y efecto temporal; riesgos de DR según programa de C |
| K6 · Programación conciliada | B → A, C | T-15/T-14 ajustados con K3/K5, capacidad y holguras verificadas; actas, fechas y reservas identificadas |

### Cómo evitar ciclos y esperas innecesarias

1. E y D publican K1/K2 temprano; no esperan terminar toda su revisión formal.
2. B entrega **la base actual K4** sin esperar que A cierre reservas. A calcula K5 sobre esa base. B devuelve K6; A y C verifican su propagación. Esto corta la remisión circular SD8 ↔ T-15.
3. C entrega K3 antes de cerrar la presentación de SD6. Puede usar K4 para diseñar las pruebas, pero no fija su calendario final hasta K6.
4. En A, cerrar SD8 antes de propagar a SD13. Si la ola 0 ya entregó el mapeo de riesgos, usarlo, no renumerar de nuevo.
5. En D, cerrar cambios sustantivos del T-12 antes de regenerar la matriz de pruebas en C. Un cambio posterior obliga a repetir conteos y cruces afectados, no a reabrir todos los frentes.
6. Las dudas de política (evaluadores, gobierno, certificaciones, anexos) se elevan al coordinador humano con alternativas y evidencia; una IA no decide por todo el equipo.

Ruta crítica orientativa: **K0 → K3/K4 → K5 → K6 → cierre de SD9/aceptación → verificación global**. K2 también es condición para cerrar trazabilidad de pruebas. El trabajo de forma y referencias avanza en paralelo.

## 6. Aislamiento y coordinación entre equipos

- En computadores distintos: cada integrante usa su clon. En un mismo computador: checkout/worktree y carpeta de compilación distintos por responsable y rama; nunca dos IAs escribiendo en la carpeta activa de Claude.
- No cambiar la rama del checkout compartido para trabajar otro SD. No ejecutar reset, clean, stash, prune, borrados o merges generales sobre trabajo ajeno.
- No sincronizar una misma carpeta de escritura con OneDrive entre dos equipos activos: usar intercambio controlado de commits/archivos, no edición concurrente del directorio.
- Registrar por frente: responsable humano, SD, rama real, SHA inicial, copia de trabajo y archivos autorizados. Los nombres de ramas del plan fuente son referencia a verificar, no garantía de su vigencia.
- Una vez entregada K0, preparar ramas de trabajo propias desde los commits recibidos. Seguir los nombres de ramas que el equipo haya autorizado; si no hay convención aplicable, proponer prefijo `codex/`, sin renombrar las ramas oficiales existentes.
- Si Claude dejó commits locales sin push, el remoto no contiene esos cambios: el coordinador debe organizar su transferencia. La publicación exige autorización; no convertir este plan en permiso implícito de push.
- Cada IA sólo lee documentos ajenos. Si detecta un problema, envía hallazgo al dueño con archivo, sección/label, valor actual y valor propuesto.
- No modificar `lafrox.cls`, portadas compartidas, canon ni políticas globales desde un frente aislado. E prepara propuestas de 5.3 y el coordinador obtiene aprobación antes de propagarlas por dueño.
- El coordinador mantiene el tablero, pero no reescribe silenciosamente los documentos de los cinco frentes.

### Formato único de entrega de datos y hallazgos

```text
Frente / responsable:
SD, rama y SHA revisado:
IDs del plan fuente:
Dato o decisión y unidad:
Fuente exacta: archivo + sección/label (línea sólo como ayuda):
Consumidores y remisiones afectadas:
Estado: propuesto / aprobado / aplicado / verificado:
Evidencia de cálculo, compilación o revisión:
Bloqueos y decisión humana requerida:
```

Sólo se consume como definitivo lo aprobado y respaldado por una versión identificable. Un mensaje informal «ya lo cambié» no reemplaza la entrega.

## 7. Ola 5: parte distribuida y parte de integración

| ID | Responsabilidad y orden |
|---|---|
| 5.1 | Coordinador con E/A: preservar primero la FMEA y evidencias necesarias; inventariar ramas obsoletas. Archivar/eliminar sólo con autorización expresa. No hacer prune mientras se dependa de una referencia local antigua |
| 5.2 | Cada dueño limpia sólo archivos confirmados fuera de uso en su SD. Verificar referencias e historial; no borrar por nombre ni eliminar material aún necesario para revisión |
| 5.3 | E propone ficha común de fecha, versión y formato. Tras aprobación, cada dueño aplica y recompila. No unificar clases a ciegas ni alterar la fecha sin acuerdo |
| 5.4 | Coordinador asigna un único dueño de TRZ cuando identifique su ubicación vigente. Actualiza sólo trazabilidad aplicable a esta entrega, sin crear capítulos excluidos |
| 5.5 | Coordinador o revisor de sólo lectura desarrolla el verificador; cada dueño resuelve los errores de sus documentos. Ejecutar contra el manifiesto final, no ramas cambiando durante la corrida |

El verificador debe distinguir `\label`/`\ref` de remisiones textuales, IDs de requisitos, riesgos, paquetes e hitos. Un grep encuentra candidatos, pero **no prueba por sí solo** que el destino existe ni que dice lo citado. Los cruces semánticos requieren revisión humana o comprobación específica.

## 8. Criterio de cierre por frente y cierre global

Cada frente entrega:

- [ ] Lista de IDs: resuelto por ola 0 / corregido ahora / no aplica justificado / bloqueado con evidencia.
- [ ] Diff limitado a sus documentos; sin cambios de otros frentes ni auxiliares de compilación incorporados por accidente.
- [ ] Remisiones actualizadas sobre K1–K6 y SHA de los documentos consultados.
- [ ] Compilación de cuerpo, anexos y formularios con su configuración; sin referencias o citas indefinidas. Revisar el log actual, no un PDF antiguo que quedó en la carpeta.
- [ ] Inspección visual de los PDF: índice, títulos, tablas, figuras, tamaños, numeración de formularios y nombres de salida.
- [ ] Búsqueda de marcadores del plan fuente, con revisión de cada coincidencia; cero problemas sin resolver, no un reemplazo automático de palabras.
- [ ] Declaración de IA fiel a lo ocurrido y revisión humana pendiente donde corresponda; SD8 revisado manualmente por el equipo.
- [ ] Commits o paquete de cambios preparados según autorización, sin push automático.

El coordinador cierra cuando:

- [ ] Todos los SD existentes del alcance tienen dueño y versión final identificada; 1.1 sigue excluido.
- [ ] SD8/SD13 usan los mismos IDs; SD8/T-15 comparten reservas sin doble conteo; SD6/SD9/T-15 comparten política de evaluadores.
- [ ] SD3/T-12 y SD9/T-13 coinciden en catálogo y conteos; SD4/T-11 y citantes usan los mismos nombres y destinos.
- [ ] Las dos actas, hitos, DR y plazos de aceptación son coherentes entre SD7/SD9/SD13 y formularios pertinentes.
- [ ] Se ejecutó 5.5 contra las versiones finales, y se revisaron semánticamente las remisiones no automatizables.
- [ ] Una revisión cruzada de sólo lectura no encuentra regresiones del canon; cualquier ajuste vuelve al dueño del SD.
- [ ] El paquete contiene sólo los entregables aplicables a esta entrega, con nombres oficiales y revisión humana. No confundir este cierre parcial con certificar toda la Propuesta Final.

## 9. Mensajes para iniciar cada IA

**Instrucción común — pegar antes del mensaje específico y adjuntar la ficha detallada del frente (secciones 4.2–4.6), además de 4.1 y 4.7:**

> Trabaja conforme a PLAN_PARALELO_LAFROX_2026-10-27.md y al canon C1–C15, usando el plan de revisión integral como catálogo de IDs. Ejecuta las fichas detalladas de tu frente en 4.2–4.6 y la ficha transversal 4.7; informa el estado de cada ficha, no sólo un resumen general. El punto 1.1 está excluido íntegramente de esta entrega. Claude está aplicando ola 0: no interfieras y espera K0 antes de editar. Primero confirma tus ramas, SHAs y archivos permitidos; revalida qué resolvió ola 0. Edita sólo tus SD. Publica temprano tus contratos K y comunica hallazgos ajenos a su dueño, sin corregirlos tú. No inventes decisiones ni evidencias. No hagas push, cambios de canon o limpieza destructiva sin autorización. Este mensaje organiza el trabajo; confirma con el responsable humano qué ejecución y commits están autorizados.

### Frente A
> Eres dueño de SD8 y SD13, incluidos sus anexos/formularios. Revisa los IDs asignados a A en la sección 4. Prioriza P7, conciliación de reservas y mapeo de riesgos; recibe K4/K3 y entrega K5. SD13 consume el catálogo de SD8. Conserva la FMEA antes de cualquier limpieza. La Declaración de IA del SD8 se entrega al equipo para edición manual. No edites SD7 ni SD9.

### Frente B
> Eres dueño de SD7 y sus formularios/anexos. Revisa los IDs asignados a B. Entrega primero K4; recibe K3/K5 y devuelve K6. Verifica actas de marcha blanca frente a aceptación, reservas, capacidad, sala técnica y reversión. No decidas políticas por SD6 ni reservas por SD8. Identifica con C la ubicación exacta de cada T-17. No edites las copias de C.

### Frente C
> Eres dueño de SD6 y SD9, incluidos T-9/T-10/T-13/T-17 cuando correspondan a esas ramas. Revisa los IDs asignados a C. Publica temprano K3: evaluadores, métricas, gobierno y DR; eleva las decisiones no aprobadas. Recibe K2 antes de regenerar la matriz de pruebas y K6 antes de cerrar calendarios. No inventes pruebas ejecutadas ni edites T-15.

### Frente D
> Eres dueño de SD3 y SD5 con sus anexos/formularios. Revisa los IDs asignados a D. Prioriza K2: catálogo verificable, prioridades, retención y OTIF. Usa el diccionario K1. No heredes conteos del antiguo plan SD9 ni ajustes números sólo para igualar documentos. Comunica cambios de catálogo a C y de OTIF a A. No edites SD9 ni SD13.

### Frente E
> Eres dueño de SD1, SD2 y SD4 con sus anexos/formularios. Revisa los IDs asignados a E. Publica K1: diccionario, destinos y reversión. Revisa dotación, renovación de certificaciones en SD1 sin inventar acreditación, referencias y estructura de arquitectura. Coordina estilo de anexos con D. No crees SD12 ni los demás capítulos excluidos. Propón cambios comunes de formato; no los impongas en documentos ajenos.

### Coordinación / revisión final
> Mantén un manifiesto de ramas y SHAs de entrada/salida y un tablero de contratos K0–K6. No repartas un mismo SD a dos escritores. Resuelve autorizaciones y decisiones transversales con el equipo humano. Coordina 5.1–5.5 y revisión cruzada sobre versiones congeladas. Devuelve cada corrección al dueño. No publiques ni declares cerrados puntos con evidencia pendiente.

## 10. Próxima acción concreta

Pedir a Claude que, **sin interrumpir ni ampliar su ola 0**, entregue los commits por rama y pendientes al terminar. Después asignar nombres a A–E y confirmar el alcance de ejecución con cada integrante. Este documento ya permite preparar los repartos; todavía no se han iniciado los frentes.
