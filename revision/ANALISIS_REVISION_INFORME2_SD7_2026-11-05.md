# Análisis de la Primera Revisión del Informe 2, con énfasis en el Subdocumento 7

Fecha: 5 de noviembre de 2026.

Documento evaluador: `C:/Users/Leandro/Downloads/G02 - LAFROX - Primera Revisión Informe 2.pdf`, 55 páginas. Las páginas de revisión citadas abajo corresponden al folio del documento evaluador. Las páginas de S7, T-14, T-15 y T-18 corresponden al folio de cada entregable.

## 1. Diagnóstico

La evaluación reconoce una mejora grande respecto del Informe 1 y considera que la propuesta ya tiene contenido propio del caso. El problema transversal que identifica ahora es la falta de integración demostrable: metodología, EDT, programación, recursos, pruebas y riesgos se describen de manera compatible en muchos párrafos, pero no forman todavía un único plan ejecutable.

En el Subdocumento 7, las observaciones principales son de fondo. Cambiar redacción, diagramas o notas de cautela no resuelve una estimación sin derivación, una red incompleta ni un calendario con capacidad insuficiente. La implantación es uno de los puntos fuertes; la construcción y la fundamentación del cronograma son los puntos débiles.

**Revisión de mi conclusión anterior:** el estudio previo comprobó aritmética, trazabilidad de códigos y reproducción del modelo existente. Esos resultados siguen siendo ciertos, pero no justifican considerar suficiente el diseño del plan. La revisión externa muestra limitaciones estructurales que aquel informe no desarrolló: EDT por fases, estimaciones por clases, vínculos faltantes y falta de iteraciones programadas. Esta evaluación amplía y matiza ese diagnóstico anterior.

Las propuestas de corrección contenidas en el PDF se analizan como observaciones del evaluador. No se ejecutaron como instrucciones de edición: los entregables originales permanecen sin cambios.

## 2. Lectura global de la revisión

| Área | Qué reconoce la revisión | Qué queda por resolver | Relación con S7 |
|---|---|---|---|
| General, pp. 1–3 | Plantilla, firmas, índices, formularios y eliminación de errores de ensamblaje. | Volumen, legibilidad, foliación integrada, trazabilidad del Art. 46 y revisión humana sustantiva. | Presentación y cierre de los cinco entregables del capítulo. |
| S1, pp. 3–6 | Capacidad instalada y experiencia mejor documentadas. | Solidez financiera, una versión del SOC y capacidad disponible diferenciada de la planta total. | Sostener equipos, refuerzos y turnos del T-15; coordinar equipo nominado con capítulo 12. |
| S2, pp. 6–8 | Comprensión del problema, actores y procesos propios. | Separar problema de solución, completar restricciones y corregir fuentes. | Restricciones y actores que determinan calendario y adopción. |
| S3, pp. 8–13 | Etapas, criterios, catálogo y solución coherentes. | Trazabilidad completa hasta prueba/criterio, figuras, terminología y meta de OTIF. | Paquetes, tamaños y aceptación deben derivar de un alcance común. |
| S4, pp. 13–19 | Arquitectura, dimensionamiento, integración y continuidad mucho más sólidos. | Diagramas, sala acotada, cobertura de cámaras, residencia alternativa y provisión de frío. | Incorporar hitos y dependencias de esas decisiones; definir quién compra y cuándo. |
| S5, pp. 20–22 | Modelo, diccionario, migración y conciliación concretos. | Legibilidad, explicación y fundamento de algunos umbrales y volúmenes. | Migración necesita vínculos reales con modelo, interfaces, ensayos y corte. |
| S6, pp. 22–26 | DevSecOps y compuertas concretas. | Adaptación metodológica y cadencia sin reflejo en la Gantt, reglas de gestión incompletas. | Es el principal cruce que debe reconstruirse junto con S7. |
| S8, pp. 33–38 | Registro específico y cálculos de exposición consistentes. | Riesgos faltantes, residual, respuestas con plazo y costo-beneficio, técnica de análisis y reservas. | Cada respuesta y reserva debe encontrar paquete, rol y período en el plan. |
| S9, pp. 38–42 | Buen nivel técnico de calidad y pruebas propias del caso. | Pruebas por iteración, identidad sin enlace, usuarios nocturnos nuevos y aceptación. | Carga CAL, pruebas continuas, cierre formal y congelamientos. |
| S13, pp. 42–45 | Cartera estructurada y trazada. | Beneficios en unidades, naturaleza de INN-02 y doble uso de INN-03. | Completar dependencias y actualizar alcance, tamaños y pruebas si cambia la cartera. |

El S7 pesa **15 %**, la mayor ponderación individual de los ítems mostrados. La tabla final de las páginas 54–55 deja vacías las columnas de puntaje I2 y aporte: no hay una nota de Informe 2 que pueda deducirse de este PDF.

## 3. Qué conviene preservar en el Subdocumento 7

La revisión valida expresamente, en pp. 27–31:

- Cobertura de 227 paquetes, 49 cuentas y diccionario con entregables y aceptación propios del caso.
- Trazabilidad de los doce módulos, quince interfaces e innovaciones.
- Inclusión de adquisiciones, infraestructura, acuerdos con transportistas y sindicato, capacitación y cambio.
- Ocho frentes y separación del equipo que corrige E1 respecto del que construye E2.
- Aritmética de 220.023 HH y dimensionamiento de coberturas.
- Ubicación contractual de hitos, análisis del inicio y atención a congelamientos.
- Olas, volumen real, indicadores diarios, conciliación, certificación y estabilización.
- Reversión operacional ensayada para los 96 despachos y ERP como único emisor.

Estos contenidos son una base reutilizable. Reorganizar la EDT no significa eliminar sus entregables ni perder su diccionario. Reestimar puede cambiar HH, equipos y fechas: las 220.023 HH actuales deben conservarse como antecedente de comparación, no como un total que se fuerce a mantener.

## 4. Matriz de observaciones del S7 contrastadas con el estado local

### 4.1 Estructura, estimación y programación

| ID | Observación del evaluador | Contraste y estado actual | Qué demostraría el cierre |
|---|---|---|---|
| S7-01 | Primer nivel de EDT por fases RUP, p. 27. | Confirmada: Inicio, Elaboración, Construcción y Transición son las cuatro primeras ramas. La explicación actual justifica recorrerlas por etapa. | EDT agrupada por productos/resultados, con justificación de límites, cobertura y responsables. |
| S7-02 | Etapas utilizadas como ramas, p. 28. | Confirmada en 3.4/3.5, 3.8/3.9 y 4.2/4.3. | Etapa como atributo del paquete o incremento; correspondencia explícita con los entregables de cada aceptación. |
| S7-03 | Estimación por clases sin tamaño derivado del T-12, p. 28. | Confirmada en `tab_T15_clases.tex`: un módulo simple conserva el promedio de la clase y se promete ajustarlo después. | Tamaño por módulo, complejidad, productividad y esfuerzo verificables; separar desarrollo, integración, pruebas y acompañamiento. |
| S7-04 | O/P uniformes y probabilidades poco informativas, p. 28. | Confirmada la regla O=0,75M, P=1,25M. H7 y H12 calculan incertidumbre sobre siete días de su tramo final. | O/M/P propios y explicados; incertidumbre sobre caminos completos, con supuestos y límites claros. |
| S7-05 | 102 de 168 paquetes sin predecesora, p. 29. | Confirmé exactamente **102**, un 60,7 %. Incluye seis integraciones 3.6, cuatro tareas iniciales de migración y los dieciséis paquetes 3.10. | Una única red publicada y calculada, con vínculo o justificación para cada raíz y puertas de aceptación completas. |
| S7-06 | CPM construido desde fechas publicadas, pp. 29–30. | Confirmado en el código: cada inicio publicado se usa como fecha mínima y la duración toma el mayor entre ventana publicada y mínimo por HH/capacidad. | Programación por esfuerzo, capacidad, duraciones y vínculos; sólo restricciones externas justificadas fijan fechas de liberación. |
| S7-07 | Paralelismo de módulos sin nivelación demostrada, pp. 28–29. | Diez módulos E1 empiezan entre 10–18 junio de 2027; el undécimo, analítica, el 2 septiembre. La suma de máximos E1 es 132, pero no equivale a carga diaria real. | Calendario por actividad con equipos distintos, dedicación y capacidad compartida demostradas. |
| S7-08 | Iteraciones y ceremonias ausentes de Gantt, pp. 29–30. | El detalle de actividades cubre hasta H2; para construcción hay plantillas y planificación gradual. No se muestra la cadencia completa de incrementos. | Iteraciones de dos semanas con objetivo, incremento, revisión, demostración y pruebas, vinculadas a paquetes e hitos. |
| S7-09 | Pruebas ampliadas después de construcción, pp. 25, 30 y 40–41. | Confirmada la concentración de 3.8 y 3.9 en ventanas finales. El paquete continuo de puertas no permite leer el trabajo por incremento. | Pruebas de unidad, contrato, integración y regresión dentro de cada iteración, manteniendo certificación final. |

### 4.2 Factibilidad, aceptación y riesgos del calendario

| ID | Observación del evaluador | Contraste y estado actual | Qué demostraría el cierre |
|---|---|---|---|
| S7-10 | Cierre y producción incompatibles con revisión completa, p. 29. | Confirmada en T-15 p. 58. Entregas completas 2 mayo/2 octubre de 2028; producción 5 mayo/5 octubre. Sólo dos días de revisión anteriores al corte. | Procedimiento confirmado y calendario que incluya evidencia, revisión, acta y producción, sin aceptar evidencia futura. |
| S7-11 | CAL insuficiente, p. 28. | Reconfirmada: 1.049,60 HH mínimas contra 832 HH de diez personas; brecha 217,60 HH, 25 octubre–11 noviembre de 2027. | Refuerzo y asignación demostrados o redistribución viable. Trece es una cota mínima, no suficiencia acreditada. |
| S7-12 | IMP y JP sin provisión demostrada, pp. 28 y 30. | T-15 declara 27 IMP equivalentes en mes 19 y remite contratación; JP queda fuera de la tabla corporativa. | Fuente del equipo, competencias, disponibilidad, contratación y fechas de incorporación; coordinación con S1/cap. 12. |
| S7-13 | Reservas S7–S8 sin conciliación, pp. 36 y 53. | T-15 separa las 3.072 HH protegidas y deja otras reservas por reconciliar. La revisión habla de 1.100,60 HH de contingencia y 1.600 HH de gestión del S8 evaluado. | Matriz riesgo–respuesta–paquete–rol–HH–período–autorización, con solapamientos y doble conteo resueltos. |
| S7-14 | Defecto grave durante septiembre E2, p. 31. | Hay reglas de continuidad y de autorización, pero falta resolver el escenario de cierre ante un defecto abierto, su corrección y la nueva evidencia. | Árbol de decisión por fecha/severidad: contener, corregir cuando esté permitido, repetir pruebas y decidir sobre evidencia y acta. |
| S7-15 | Certificación de cadenas demasiado tardía, p. 31. | 3.6.5 comienza en febrero de 2028; 3.6.6 termina el 23 de agosto. El modelo no conecta 3.6.6 con un sucesor. | Contactos, contratos y sandbox tempranos; certificación por perfil/cadena con dependencias y puerta de habilitación antes de la evidencia final. |
| S7-16 | Evidencia temprana para proveedor de lácteos ausente, p. 31. | 1.1.3 pide acordarla, pero un acta para confirmar evidencia no define qué se entrega, a quién ni cuándo entre el inicio y H5. | Entregable temprano concreto, datos disponibles, responsable, destinatario y aceptación, separado del sistema definitivo. |
| S7-17 | Subsanación no cabe en H1/H7/H12, p. 41. | Sus holguras actuales son 5/2/3 días; restar una subsanación completa de diez produce −5/−8/−7. | Escenario de aceptación sin observaciones y escenario de subsanación modelados por separado, con tratamiento de impacto. |

### 4.3 Claridad, figuras y edición

| ID | Observación del evaluador | Contraste y estado actual | Qué demostraría el cierre |
|---|---|---|---|
| S7-18 | 1.2.1 dice mes 1 (H1), pero aceptación mes 2, p. 27. | Confirmada en `tab_T14_4.tex`. También 1.2.5 rotula mes 13 (H8), pero criterio exige aprobación en mes 14. | Separar elaboración preliminar y aprobación: mes de trabajo y mes del hito sin rótulos contradictorios. |
| S7-19 | Gantt pequeña, encabezados superpuestos, pp. 29–30. | La inspección de la p. 45 confirma rótulos densos y cabeceras superpuestas. No medí de forma independiente los 5–6 pt indicados por el evaluador. | Láminas legibles al 100 %, escala común y leyenda propia; revisión de todas las láminas finales. |
| S7-20 | Agrupaciones de barras ocultan detalle, p. 30. | Hay filas por conjuntos de códigos. Compartir fechas no demuestra que sean una actividad ni que compartan vínculos. | Resumen que permita rastrear cada paquete y sus dependencias; agrupaciones justificadas sin perder lógica. |
| S7-21 | Figura 7.20 anuncia detalle H12 inexistente, p. 32. | Confirmada visualmente en S7 p. 31: el rótulo remite hacia abajo sin ese detalle. La figura conecta ambas integraciones de cadenas, pero el código sólo impone 3.6.5 como preparación de marcha blanca. | Figura y red calculada reconciliadas; destino real del detalle o eliminación de la llamada. |
| S7-22 | Objetivos 10 y 40 minutos poco explicados en el cuerpo, p. 31. | T-18 sí aclara máximo(10,30)+10=40. La explicación del cuerpo está dispersa. | Una regla resumida: reversión técnica ≤10; contingencia operacional en paralelo ≤30; validación ≤10; total ≤40. |
| S7-23 | Tablas con párrafos y contenido ajeno al plan, pp. 31–33. | Confirmados texto extenso en reversión y bloque de precio, retención/mensajes y diseño DR en 7.3.8/T-18. | Tablas de síntesis y explicación en prosa; en S7 conservar sólo paquete, fecha, dependencia, prueba y responsable del control. |
| S7-24 | Volumen, siglas, folios y prosa defensiva, p. 32. | La entrega suma 316 páginas, incluidas portadas e índices. RC se explica en S7 y RC/PT/H en T-14; falta una leyenda autosuficiente en las figuras. Folios reinician por archivo. | Texto integrado y glosario breve; foliación de oferta completa al consolidar; límites agrupados en supuestos, sin sustituir decisiones por salvedades. |

Los puntos confirmados siguen presentes en el estado local: no hay evidencia de que hayan sido cerrados después de esta evaluación. Las fortalezas no deben contarse como correcciones pendientes.

## 5. Explicación de los cinco problemas de fondo

### 5.1 La EDT debe permitir controlar productos, no sólo recorrer un proceso

Para responder al criterio del evaluador, propongo estudiar una agrupación inicial como: plataforma base; capacidades de operación logística; integraciones y migración; infraestructura y equipamiento; solución implantada y usuarios habilitados; servicio de operación; gobierno y cierre. Es una propuesta de diseño, no una nueva EDT aprobada.

La etapa, fase metodológica, frente y módulo pueden ser atributos distintos. Un producto puede tener incrementos aceptables en E1 y E2, cada uno con alcance y aceptación propios, sin duplicar el producto completo por calendario. Tampoco basta renombrar «Construcción» como «Software»: debe revisarse qué trabajo contiene y cómo se demuestra la regla del 100 %.

Antes de recodificar, se necesita una tabla **código actual → producto → paquete futuro → etapa → requerimientos → prueba → criterio**. La numeración actual aparece en T-12, T-13, T-17, T-19, diagramas y scripts: una renumeración aislada rompería trazabilidad que el evaluador ya reconoce como correcta.

### 5.2 El modelo actual comprueba una propuesta de fechas; no genera toda la programación desde su fundamento

La implementación sí utiliza topología, pasadas hacia adelante y atrás y vínculos FC/CC; no es sólo una tabla dibujada. El límite está en sus entradas: fija como liberación mínima el inicio publicado de cada paquete y toma su ventana como duración mínima. Así, parte del calendario que debería justificarse ya entra como condición.

Además, los 102 vacíos no son equivalentes: algunas tareas iniciales pueden ser raíces legítimas y otras reciben relaciones especiales desde el código. Pero los casos importantes señalados por el evaluador efectivamente quedan sin causas previas o sin consecuencias posteriores suficientes.

Verifiqué ejemplos en el modelo ejecutado en memoria:

- 3.6.1 no tiene entrada lógica a su inicio, aunque sí bloquea 3.8.1.
- 3.7.1–3.7.4 no tienen entradas a sus inicios, aunque sí condicionan el cierre 3.7.5.
- 3.6.5 condiciona marcha blanca E2; **3.6.6 no tiene sucesor**.
- Los cuatro paquetes de INN-01 no tienen entradas externas a su inicio ni salidas de su fin hacia otros paquetes.

Por tanto, «sin predecesora no puede atrasar a nadie» no es literalmente cierto: puede atrasar sucesores que sí tenga. El problema real es que no hereda retrasos anteriores y, en algunos casos, ni siquiera transmite los propios a las puertas de aceptación. La solución es publicar y ejecutar una sola red completa, no rellenar celdas artificialmente.

### 5.3 Estimar por tamaño y evaluar incertidumbre son trabajos distintos

El problema de O=0,75M y P=1,25M no es una división mal hecha. Matemáticamente TE=M y sigma=M/12; la varianza es positiva. Lo débil es aplicar el mismo patrón sin fundamentar la incertidumbre específica de cada paquete.

También precisé el dato del evaluador sobre quince módulos iguales: la fuente actual tiene trece de 960 HH y dos, 3.4.4 y 3.4.5, de 1.440 HH por la ampliación de frío. Esa diferencia ya existe, pero sigue faltando una derivación de tamaños para cada módulo.

Una estimación defendible necesita requerimientos o casos de uso identificados, complejidad, transacciones/reglas/interfaces, factores y productividad explicados. Puede emplear Puntos de Casos de Uso u otra medida que corresponda al catálogo real. No corresponde inventar un conteo ni distribuir las mismas HH con ponderaciones elegidas para conservar el total.

El PERT actual de H7/H12 toma siete días como contribución variable y sigma≈0,5833. No incorpora como incertidumbre toda la construcción previa porque ésta queda detrás de liberaciones fijadas y restricciones del calendario. Eso explica por qué una probabilidad muy alta puede coexistir con dos días de margen y una capacidad no demostrada. La nueva evaluación debe hacerse después de completar red, estimación y recursos.

### 5.4 La nivelación debe mostrar personas y tiempo, no sólo equivalentes mensuales

El máximo mensual conjunto de 64 sigue siendo una suma aritmética válida, pero no prueba que especialistas concretos cubran cada día. Tampoco sumar 11 equipos máximos de 12 demuestra que se necesiten 132 simultáneos: cada paquete puede emplear menos personas en parte de su ventana.

Sí existe una imposibilidad necesaria en CAL bajo las ventanas actuales. Los paquetes 3.8.2 y 3.8.3 necesitan al menos 204,80 HH cada uno dentro del intervalo crítico; 3.8.4 y 3.8.5 necesitan 320 cada uno. Las diez personas declaradas dejan 217,60 HH sin capacidad. Esa brecha debe resolverse en la programación, con disponibilidad y apoyos reales, incluyendo las pruebas durante iteraciones.

Un contrato de refuerzo tampoco basta si no especifica perfiles, fechas, dedicaciones y supervisión. Implantación, SOC y dirección requieren el mismo tratamiento. Los equipos de E1 protegidos no deben contarse a la vez para construir E2.

### 5.5 Aceptación y septiembre son decisiones de planificación

La revisión no pide borrar la frase que reconoce el conflicto: pide resolverlo. Con evidencia terminada el 30 de abril/septiembre y entrega el primer hábil siguiente, el plazo completo de revisión termina el 16 de mayo/17 de octubre, después del corte propuesto. A esa secuencia todavía pueden agregarse observaciones, correcciones y segunda revisión.

Debe distinguirse el escenario nominal sin observaciones del escenario con subsanación. Restar diez días a la holgura no convierte automáticamente todos los plazos en incumplidos; sí muestra que no se ha protegido un ciclo completo de corrección en esos hitos. La revisión preliminar reduce errores, pero no elimina formalmente pasos sin una regla acordada.

Para septiembre E2, hace falta una decisión explícita ante un incidente grave detectado el día 5: cómo se contiene dentro de lo permitido, qué regla rige las correcciones, qué pruebas repiten y si la continuidad y evidencia siguen siendo aceptables. No debe asumirse una excepción de emergencia que contradiga S6/S9 ni que la corrección del defecto permita conservar automáticamente toda la evidencia. Tampoco debe imponerse un reinicio general de 28 días sin revisar qué criterio y dominio fueron afectados.

## 6. Observaciones del evaluador que conviene precisar

Estas precisiones mejoran la respuesta sin desconocer los problemas centrales:

1. **EDT por fases:** la revisión la rechaza para esta evaluación y pide productos. No hace falta convertir esa preferencia del criterio aplicado en una prohibición universal para justificar la corrección.
2. **Quince módulos iguales:** hay trece de 960 y dos de 1.440 HH; permanece la falta de tamaño individual.
3. **Once módulos arrancando juntos:** diez parten en junio; analítica parte en septiembre. Permanece la concentración y falta de nivelación.
4. **Sin predecesora:** puede tener sucesores y retrasarlos. Confirmé faltas tanto de entrada como de salida; 3.6.6 es especialmente importante.
5. **PERT degenerado:** no tiene varianza cero; su debilidad es empírica y de alcance del camino considerado.
6. **CPM inexistente:** sí hay un algoritmo y una red de 399 eventos y 581 relaciones. Falta sustentar y completar lo que modela.
7. **Códigos sin definición:** RC/PT/H tienen explicación parcial en el texto; una leyenda en cada lámina sigue siendo necesaria.
8. **Agrupación de cuentas distintas:** el ejemplo 3.11.3/3.11.4 pertenece a la misma cuenta 3.11. El reclamo de legibilidad y trazabilidad de vínculos sigue siendo pertinente.
9. **Indicios de IA:** p. 32 califica como sólido un pendiente literal, pero p. 54 afirma que no encontró indicios sólidos. Hay una inconsistencia interna de la revisión; no permite concluir por sí sola una sanción ni una nota cero. Conviene responder al problema técnico y conservar una declaración veraz de revisión.
10. **Volumen:** las 66 páginas del S7 incluyen portada, índices, referencias y declaración; no son 66 páginas netas de desarrollo. El volumen total y la necesidad de síntesis siguen siendo observaciones válidas.

## 7. Secuencia de corrección recomendada

| Orden | Trabajo | Resultado revisable | Coordinación necesaria |
|---|---|---|---|
| 1 | Fijar alcance, productos y criterios; resolver reglas de actas y congelamientos. | Decisiones documentadas y condiciones del calendario, sin cambios silenciosos de compromiso. | S3, S6, S9/T-17 y Contraparte Técnica. |
| 2 | Diseñar EDT por productos y tabla de equivalencias. | Cobertura completa con etapa y responsables como atributos; trazabilidad antes/después. | T-12, T-14, T-19 y arquitectura. |
| 3 | Estimar por tamaño y registrar O/M/P justificados. | Memoria de cálculo por módulo/interfaz; diferencias frente a la base anterior. | Alcance, desarrollo, calidad e infraestructura. |
| 4 | Completar dependencias e iteraciones. | Red única y Gantt con incrementos de dos semanas, pruebas, revisiones y demostraciones. | S6/T-10, S9/T-13 y responsables de frentes. |
| 5 | Nivelar recursos y recalcular fechas. | Calendario por rol/persona y capacidad; CAL, IMP y SOC resueltos; escenarios de aceptación. | S1, capítulo 12, contratación y turnos. |
| 6 | Conciliar respuestas y reservas de riesgos. | Riesgo–acción–paquete–HH–período–autoridad, sin doble conteo. | S8/T-16, S7 y Oferta Económica cuando corresponda. |
| 7 | Recalcular CPM y análisis de incertidumbre. | Caminos de construcción y aceptación, holguras, sensibilidad y límites del modelo. | Programación y riesgos. |
| 8 | Reescribir y maquetar los cinco entregables. | Cuerpo de síntesis, tablas breves, figuras legibles y referencias consistentes. | Responsables de documentos y consolidación. |

El diseño de iteraciones y la nivelación pueden requerir varias pasadas. No conviene empezar por rehacer todas las figuras: cambiarían otra vez cuando se cierre la red. Tampoco conviene llenar toda la operación de ceremonias de desarrollo: hay que distinguir construcción iterativa, instalación, campañas y servicios continuos.

Para considerar cerrado el S7 deben poder responderse, con evidencia, estas preguntas: ¿de dónde sale el tamaño?, ¿qué entrega cada incremento?, ¿qué lo habilita?, ¿quién lo ejecuta y con cuánta dedicación?, ¿qué prueba lo acepta?, ¿qué ocurre si falla?, ¿cómo afecta a producción y al hito contractual?

## 8. Alcance y evidencia de este análisis

Se extrajo el texto de las 55 páginas del PDF evaluador; se estudiaron las observaciones por capítulo y los cruces con S7. Se inspeccionaron visualmente las páginas 27–32 y 55, además de las páginas 31 y 45 del S7 actual. Se contrastaron las fuentes de EDT/diccionario, estimación, fechas, dependencias, actas, recursos y continuidad.

Se ejecutó el modelo CPM en memoria hasta antes de su escritura de archivos, comprobando 399 eventos, 581 relaciones, los 102 vacíos de la tabla, vínculos de ejemplos y los caminos PERT de H7/H12. No se alteraron sus resultados históricos. Los otros capítulos se analizan según lo que dice el PDF evaluador; no se afirma haber validado sus ramas actuales completas ni las Bases originales en esta revisión.

Archivos locales principales para reproducir el contraste:

- `formulario-t14/contenido.tex` y `formulario-t14/tablas/tab_T14_4.tex`.
- `formulario-t15/contenido.tex`, `tablas/tab_T15_clases.tex`, `tab_T15_paquetes.tex`, `tab_T15_actas.tex` y `tab_T15_8.tex`.
- `subdocumento-07/contenido.tex`, `tablas/tab_SD7_2.tex` y `tab_SD7_7.tex`.
- `subdocumento-07-anexos/tablas/tab_7B1.tex`.
- `formulario-t18/contenido.tex`.
- `revision/recalcular_cpm_20261025.py`.

Este archivo es un informe de análisis y una propuesta de trabajo. No presenta reestimaciones, acuerdos del CLIENTE, contrataciones ni correcciones como si ya estuvieran ejecutados.
