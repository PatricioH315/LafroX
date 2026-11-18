# Propuesta: EDT por entregables y corrección de los paquetes de trabajo (SD7, T-14, T-15, T-18)

Fecha: 17-11-2026. Base: rama `LafroX-Subdoc7-LateX-CORRIGIENDO` (commit 5e78b998), revisión del Informe 2 y tabla de trazabilidad Informe 2 → 3.

## 1. Qué resuelve y qué no cambia

Resuelve las observaciones del SD7 que nacen de cómo están armados los paquetes de trabajo: SD7-01, 02, 06, 08, 09, 10 (matiz), 11, 12, 14, 17, 25 y 26, más tres problemas que la revisión no nombró pero que salen de la misma raíz (P11 a P13).

Restricciones que la propuesta respeta:

- **No cambia el alcance ni el esfuerzo.** Siguen los 227 paquetes, con sus mismos entregables, criterios de aceptación, responsables y HH (202.108,62 HH en total). Ningún paquete se crea ni se elimina: sólo se reagrupan, cambian de código y algunos cambian de fecha.
- **No cambian los hitos ni los meses contractuales.** H1 a H12, marchas blancas (H6 01-02-2028 y H11 01-08-2028), producción el 17-05-2028 y el 18-10-2028, congelamientos.
- **Las figuras de la EDT y de la Gantt se rehacen al final**, una vez fijada la estructura.

Lo que sí cambia y hay que revisar aguas abajo: la distribución mensual de HH en junio–septiembre de 2027 (sección 6) y, por eso, el flujo del E2/Excel en esos meses.

## 2. Problemas y soluciones

| N.º | Problema (observación) | Evidencia hoy | Solución propuesta |
|---|---|---|---|
| P1 | Primer nivel de la EDT por fases RUP y no por entregables (SD7-01) | Fases 1 Inicio, 2 Elaboración, 3 Construcción, 4 Transición…; el índice por productos del T-14 es sólo una lectura encima | Nuevo nivel 1 de **10 productos** (sección 3). Las fases RUP pasan a ser lo que son: el ciclo de ejecución, descrito en el SD6 y visible en la Gantt, no la estructura del alcance |
| P2 | Etapa 1 y Etapa 2 como ramas (SD7-02) | Cuentas 3.4/3.5 «Módulos de la Etapa N», 3.8/3.9 «Pruebas de la Etapa N», 4.2/4.3 «Marcha blanca de la Etapa N» | Cada cuenta es un producto y contiene los incrementos de ambas etapas. La etapa queda como **atributo** del paquete (columna «Etapa» en el diccionario). Ejemplo: «6.3 Pruebas de carga y resiliencia» contiene 6.3.1 (E1) y 6.3.2 (E2) |
| P3 | Mismo producto partido por calendario | M10 Analítica en 3.4.11 (E1) y 3.5.4 (E2); carga 3.8.4/3.9.3; DR 3.8.5/3.9.4; seguridad ofensiva 3.8.6/3.9.5; despliegue 3.8.8/3.9.7; marcha blanca 4.2.1/4.3.1; estabilización 4.2.2/4.3.2; certificación de usuarios 7.3.1/7.3.2 | Cada par queda bajo una sola cuenta de producto (Anexo A). Los paquetes siguen separados porque tienen fechas, actas e hitos distintos (H5/H10, H7/H12), pero ya no en ramas distintas |
| P4 | Once módulos de la Etapa 1 parten la misma semana (SD7-08) | 3.4.1 a 3.4.10 empiezan entre el 10 y el 18-06-2027 | Construcción en **tres olas** según las dependencias que el propio SD7 describe (sección 4). Mismo fin que hoy (01-10-2027) |
| P5 | Máximo de 12 personas por módulo; 10 módulos en paralelo suman 120 (SD7-06) | Tabla de programación del T-15: «12,0 / 12», «10,3 / 12»… y el CPM calcula la duración con ese máximo | Equipos de 3 a 6 personas por módulo. Máximo simultáneo de **30**, dentro de las 31 plazas de construcción del T-15 sección 5.7. El CPM usa ese equipo real |
| P6 | Red incompleta: 77 de 168 paquetes con entregable sin predecesora (SD7-09) | Incluye 3.3.3–3.3.6, 3.10.x.1, casi toda la fase 5 y 6, 7.1.1, 9.1.1… | Predecesora para los 77 (Anexo B). Sólo el primer paquete depende de la firma del contrato. Regla: ningún paquete con entregable sin predecesora |
| P7 | CPM restringido por ventanas publicadas (matiz de SD7-10) | T-15 sección 5.1: «Cada paquete inicia cuando se cumplen sus precedencias, sin adelantarse al comienzo de su ventana» | Las fechas salen de duraciones y predecesoras. Sólo se mantienen como restricciones fijas: H6, H11, congelamientos, plazos del proveedor (8 semanas de homologación, 6 de piloto) y la obra civil del CLIENTE |
| P8 | Dos rutas críticas distintas (SD7-25) | La vista crítica de la Gantt (GanttProject, prefijo RC) muestra 3.2.x, 3.4.9, 3.5.x, migración; la Tabla 7 del T-15 dice que controlan 3.1.5, 3.8.1, 3.8.7, 3.9.1, 3.9.6 | Una sola fuente: el CPM del T-15 marca la ruta crítica y la Gantt toma de ahí la marca RC. La figura de ruta crítica muestra la cadena completa de la Etapa 1 (diseño → plataforma → módulos → certificación → H5 → marcha blanca → H7) y la de la Etapa 2 |
| P9 | Iteraciones de dos semanas invisibles en la Gantt (SD7-11) y pruebas concentradas al final (SD7-12) | La Gantt de construcción está a nivel de paquete; las 83 ventanas de QA viven en el SD9 y en una tabla del T-15 | En la Gantt, la barra de cada módulo se divide en sus iteraciones de 14 días con un rombo de demostración al cierre, sin agregar filas. Cada iteración incluye su actividad de pruebas del incremento (plantilla D del T-15). Las cuentas 6.x quedan como certificación final |
| P10 | Filas agrupadas que mezclan cuentas distintas (SD7-14) | «2 elementos: 3.11.3, 3.11.4» en la Figura 7.26 | Una fila por paquete, agrupadas bajo la barra resumen de su producto (nivel 1) y su cuenta |
| P11 | La EDI con la principal cadena parte en el mes 13, sin margen ante agosto de 2028 (SD7-17) | 3.6.5: 01-02-2028 → 04-07-2028; 3.6.6: 01-06-2028 → 23-08-2028 (termina después de H11) | Separar la habilitación de la cadena del desarrollo de M11 (sección 5): la principal cadena parte el 01-10-2027 y cierra el 31-05-2028; las demás, del 02-05 al 14-07-2028. Margen: dos meses y medio la principal; dos semanas y media las demás antes de H11 |
| P12 | Actividades detalladas sólo hasta el H2 (SD7-26) | 119 actividades de 60 paquetes; el resto «por planificación gradual» | Detallar en el T-15 todos los paquetes hasta el H5 (construcción completa de la Etapa 1, donde está la ruta crítica), en formato compacto: una fila por paquete con sus actividades, HH y quincena, generadas desde las plantillas por clase. La planificación gradual queda para la Etapa 2 y la Operación |
| P13 | Numeración de innovaciones desalineada | 3.10.4.x es INN-05; INN-04 está repartida en 5.4.3, 8.3.3 y 8.3.4; INN-02, 03 y 05 tienen parte en la cuenta 8.3 | Una cuenta por innovación, con el mismo número: 7.1 INN-01 … 7.5 INN-05, cada una con sus paquetes de implementación y de operación. Desaparece el cuarto nivel de la EDT |
| P14 | Paquetes de gestión y de operación sueltos de su producto | 8.1.4 (actualizaciones del Plan de Reversibilidad) separado de 1.7.x; 9.1.1 (entrega del código) separado de 3.11.5 y 5.4.4 (custodia) | Se agrupan con su producto: Plan de Reversibilidad (1.6); Documentación técnica, código y custodia (6.8) |

## 3. Nueva estructura: nivel 1 por entregables

| Nivel 1 | Producto que se acepta | Cuentas | Paquetes | Proviene de |
|---|---|---|---|---|
| 1 | Gestión del proyecto | 8 | 32 | 1.1, 1.3–1.9; 8.1.4; 9.1.2 |
| 2 | Requisitos y diseño aprobados | 8 | 26 | 1.2; 2.x; 4.1.4 |
| 3 | Plataforma base | 3 | 14 | 3.1, 3.2, 3.3 (identidad, registro auditable, sin conexión) |
| 4 | Software operativo | 5 | 15 | 3.4, 3.5 |
| 5 | Integraciones y datos migrados | 4 | 14 | 3.3 (ERP, WMS, flota), 3.6, 3.7 |
| 6 | Solución certificada y documentada | 8 | 22 | 3.8, 3.9, 3.11, 9.1.1, 5.4.4 |
| 7 | Innovaciones verificadas | 5 | 23 | 3.10; 5.4.3; 8.3 |
| 8 | Infraestructura, equipamiento y servicios habilitados | 7 | 35 | 5.1–5.3; 6.x |
| 9 | Implantación y usuarios habilitados | 7 | 25 | 4.1–4.3; 7.x; 5.4.1–5.4.2 |
| 10 | Servicio de operación y salida | 5 | 21 | 8.1, 8.2, 8.4, 8.5; 9.2 |
| | **Total** | **60** | **227** | |

Por qué esta agrupación (texto para el 7.1 del SD7):

- Cada elemento de nivel 1 termina en algo que la Contraparte recibe y acepta. Requisitos y diseños con acta (H1, H2, H8), una plataforma en servicio (H3), módulos aceptados en QA, integraciones probadas, una solución certificada (H5, H10), usuarios habilitados (H6, H7, H11, H12) y un servicio operando. El control del alcance se hace contra esos productos.
- La etapa no es una rama: cada paquete declara si habilita la Etapa 1, la Etapa 2, ambas o la Operación. Así, un mismo producto se controla de punta a punta (por ejemplo, la analítica M10 o las pruebas de carga) aunque se entregue en dos incrementos.
- El ciclo RUP (Inicio, Elaboración, Construcción, Transición) sigue gobernando cuándo se hace cada cosa. Se ve en la Gantt y en el SD6, y deja de condicionar cómo se agrupa el alcance.
- Se mantiene la regla del 100 %: los 227 paquetes del T-14 vigente aparecen una sola vez (Anexo A).

## 4. Construcción de los módulos de la Etapa 1 en tres olas

Orden de dependencias que ya describe el SD7 (sección 7.2.1): base compartida → recepción e inventario → preparación, frío y preventa → rutas y reparto → rendición. Inicio de cada ola: al quedar aprobados los contratos A01/A02 (diez días hábiles) del módulo del que depende, o al terminar ese módulo.

| Ola | Módulo (código nuevo / actual) | Personas | Días hábiles | Inicio | Fin | Depende de |
|---|---|---|---|---|---|---|
| A | M1 Recepción (4.1.1 / 3.4.1) | 4 | 35 | 10-06-2027 | 02-08-2027 | Plataforma (3.x) |
| A | M2 Inventario (4.1.2 / 3.4.2) | 5 | 32 | 10-06-2027 | 28-07-2027 | Plataforma |
| A | M3 Preventa (4.3.1 / 3.4.6) | 6 | 35 | 10-06-2027 | 02-08-2027 | Plataforma |
| B | M5 Preparación (4.1.3 / 3.4.3) | 5 | 31 | 25-06-2027 | 10-08-2027 | Contratos de M2 |
| B | M9 Cadena de frío (4.2.1 / 3.4.4) | 6 | 42 | 25-06-2027 | 25-08-2027 | Contratos de M2; banco y mapeo térmico |
| B | Ingesta M9/M12 (4.2.2 / 3.4.5) | 4 | 36 | 25-06-2027 | 17-08-2027 | Contratos de M2; nube IoT |
| C | M8 Devoluciones (4.3.4 / 3.4.9) | 3 | 31 | 29-07-2027 | 09-09-2027 | Fin de M2 |
| C | M4 Rutas (4.3.2 / 3.4.7) | 4 | 37 | 03-08-2027 | 23-09-2027 | Fin de M1; reglas de ruteo |
| C | M6 Reparto (4.3.3 / 3.4.8) | 6 | 42 | 03-08-2027 | 30-09-2027 | Fin de M3 |
| C | M7 Cobranza (4.3.5 / 3.4.10) | 6 | 33 | 17-08-2027 | 01-10-2027 | Contratos de M6 |
| C | M10 Analítica E1 (4.5.1 / 3.4.11) | 6 | 22 | 26-08-2027 | 27-09-2027 | Fin de M9 |

- Máximo simultáneo: **30 personas** (25-06-2027), frente a las 31 plazas de construcción del T-15 sección 5.7. Hoy la tabla del T-15 permite hasta 120.
- Último módulo: 01-10-2027. Hoy es el 04-10-2027 (3.4.10). La integración 3.8.1 (H4) conserva su inicio del 05-10-2027.
- Duración = ⌈HH / (6,4 × personas)⌉ días hábiles, la misma fórmula del T-15. Feriados considerados: 21-06, 28-06, 16-07 y 17-09-2027.
- Efecto mensual (HH de los once módulos, repartidas en sus días): hoy junio 2.188, julio 4.291, agosto 3.312, septiembre 2.057; con las olas, junio 1.508, julio 3.942, agosto 3.580, septiembre 2.810. Unas 1.030 HH pasan de junio–julio a agosto–septiembre. El total no cambia.

## 5. Intercambio electrónico con las cadenas

- **5.3.1 (actual 3.6.5), principal cadena: 01-10-2027 → 31-05-2028.** Primero la habilitación con la cadena: perfil de intercambio (de 1.2.3), registro como proveedor, conectividad AS2 de prueba y certificación de mensajes con datos de prueba. Después, la prueba de punta a punta con M11 cuando 4.4.1 (actual 3.5.1) esté en QA (28-04-2028). Predecesoras: 2.1.5 (actual 1.2.3), ambiente de Producción 3.1.2 (CC), y 4.4.1 para la prueba final. Mismas 516 HH, repartidas en más meses (menos de una plaza adicional de Arquitectura e Integración por mes).
- **5.3.2 (actual 3.6.6), demás cadenas: 02-05-2028 → 14-07-2028.** Predecesora: 5.3.1. Termina antes de H11 (01-08-2028); hoy termina el 23-08-2028, ya dentro de la marcha blanca.
- **Margen:** la principal queda lista dos meses antes de agosto de 2028. Si una cadena tarda en certificar, hay hasta el 31-07-2028 sin tocar H11.

## 6. Efectos que hay que absorber

| Efecto | Dónde | Qué hacer |
|---|---|---|
| Fechas de casi todos los paquetes con entregable cambian al recalcular el CPM sin ventanas fijas (P6, P7) | T-15 (programación, CPM, holguras, Tabla 7), T-14 (períodos del diccionario), SD7 (7.3), T-18 | Recalcular con el script de CPM ya existente (`revision/recalcular_cpm_*.py`) y revisar la holgura de cada hito. Ojo con H1: hoy tiene 5 días y las nuevas predecesoras de 1.1.x/1.2.x la pueden reducir |
| Distribución mensual de HH en junio–septiembre de 2027 y meses 9–12 (EDI) | T-15 secciones 4.4 y 5.7 (curva de plazas), E2/Excel (costos mensuales y Curva S) | Regenerar la curva desde la programación nueva. El total sigue en 202.108,62 HH. Avisar al equipo del Excel para mover las HH entre meses |
| Ventanas de QA del SD9 | SD9, Anexo 9.E.1 (83 ventanas) y registro de control de QA del T-15 | Regenerar las ventanas desde las iteraciones nuevas de cada módulo |
| Cambio de códigos | Citas de paquetes: SD7 y formularios (~1.020), T-12 en la rama del SD3 (columna «Paquete EDT» de 279 filas), SD9 (~700), SD4 (~180), SD13 (~130), SD8 (~40), SD5 y SD6 (~20 cada uno) | Reemplazo con script desde una sola tabla de equivalencias (`mapa.json`). Se reemplaza sólo en contexto de paquete (columnas de paquete, «paquete X», «(X)»), nunca en números de sección propios de cada subdocumento (por ejemplo, la sección 3.4.4 del SD3). Después del reemplazo, un control automático: ningún código actual queda vivo y cada código nuevo existe en el T-14 |
| Figuras | EDT (7.1–7.18), cobertura (7.19), red (7.20), ruta crítica, Gantt (7.24–7.31) | Al final, cuando la estructura y el CPM estén cerrados |
| Tabla de trazabilidad Informe 2 → 3 | Rama de anexos | SD7-01, 02, 06, 08, 09, 11, 14, 17, 25 y 26 pasan a Corregida; SD7-12 según cómo quede el SD9 |

## 7. Orden de trabajo propuesto

1. Fijar la tabla de equivalencias (Anexo A) y las predecesoras (Anexo B). Es la única decisión de fondo; lo demás se deriva.
2. T-14: nueva estructura (nivel 1, 60 cuentas, columna Etapa), diccionario con los códigos nuevos, textos de cada cuenta. Se elimina el párrafo «Estructura de alcance por productos», porque la EDT ya es por productos.
3. T-15: programación con olas, equipos reales y predecesoras completas; CPM sin ventanas fijas; actividades hasta H5; curva mensual; ventanas de iteración.
4. SD7: 7.1 (criterio de descomposición, tabla de fases → tabla de productos, cobertura), 7.2 (secuenciamiento, frentes, olas) y 7.3 (ruta crítica única, hitos, Gantt).
5. T-18 y anexos del SD7 (Anexo 7.B de dependencias con los códigos nuevos).
6. Otros subdocumentos: reemplazo de códigos con script en SD3/T-12, SD4, SD5, SD6, SD8, SD9 y SD13, rama por rama, con control de que no quede ningún código viejo.
7. SD9: ventanas de QA regeneradas.
8. Avisar del cambio mensual de HH para el E2/Excel.
9. Figuras de EDT, red y Gantt.
10. Tabla de trazabilidad y recompilación de todos los PDF.

## 8. Decisiones que necesito de ti

1. ¿Apruebas los 10 elementos de nivel 1 y la agrupación del Anexo A? En particular: el piloto de frío (actual 4.1.4) dentro de «Sistema de cadena de frío validado» en Diseño, y los acuerdos con transportistas y el sindicato dentro de Implantación.
2. ¿Aceptas mover unas 1.030 HH de junio–julio a agosto–septiembre de 2027 (y el reparto nuevo de la EDI), con el E2/Excel ajustándose a eso? La alternativa es fijar las HH por mes y ajustar los equipos, pero entonces el escalonamiento queda más débil.
3. ¿Hago yo el reemplazo de códigos en las ramas de los otros subdocumentos (SD3, SD4, SD5, SD6, SD8, SD9, SD13), o lo coordinas con cada responsable usando la tabla de equivalencias?

## Anexo A. Equivalencias: código nuevo ↔ código actual

La etapa se calcula desde las fechas del T-15 y el nombre del paquete. «Transversal» = gestión o documentación de ambas etapas.

**1 Gestión del proyecto**

| Nuevo | Actual | Paquete | Etapa |
|---|---|---|---|
| **1.1** | | **Constitución y confirmaciones contractuales** | |
| 1.1.1 | 1.1.1 | Acta de constitución del proyecto, firmada con la Contraparte Técnica | Transversal |
| 1.1.2 | 1.1.2 | Documento de validación con el CLIENTE de los problemas y metas del proyecto | Transversal |
| 1.1.3 | 1.1.3 | Acta de confirmación con el CLIENTE de la fecha de inicio, la evidencia para el proveedor de lá | Transversal |
| **1.2** | | **Planificación y líneas base** | |
| 1.2.1 | 1.3.1 | Plan para la dirección del proyecto, con el calendario de congelamientos de septiembre, diciemb | Transversal |
| 1.2.2 | 1.3.2 | EDT y diccionario de la EDT (línea base del alcance) | Transversal |
| 1.2.3 | 1.3.3 | Carta Gantt de 56 meses con los hitos H1 a H12 y la ruta crítica | Transversal |
| 1.2.4 | 1.3.4 | Documento de nivelación de recursos y frentes del solapamiento de los meses 13 a 15 y 19 a 20 | Transversal |
| 1.2.5 | 1.3.5 | Reunión semanal de seguimiento con su informe semanal | Transversal |
| **1.3** | | **Interesados y comunicaciones** | |
| 1.3.1 | 1.4.1 | Registro de interesados con su influencia, interés y estrategia | Transversal |
| 1.3.2 | 1.4.2 | Plan de comunicaciones con calendario y canales por grupo de interés | Transversal |
| 1.3.3 | 1.4.3 | Registro de solicitudes de cambio con análisis de impacto | Transversal |
| **1.4** | | **Gestión de la calidad** | |
| 1.4.1 | 1.5.1 | Plan de calidad y plan de pruebas | Transversal |
| 1.4.2 | 1.5.2 | Puertas de calidad automáticas: cobertura de lógica de negocio del 70 %, global del 80 % y del  | Transversal |
| **1.5** | | **Gestión de riesgos** | |
| 1.5.1 | 1.6.1 | Plan de riesgos y registro inicial de riesgos según ISO 31000 | Transversal |
| 1.5.2 | 1.6.2 | Registro de riesgos revisado en cada Comité de Proyecto | Transversal |
| **1.6** | | **Plan de Reversibilidad** | |
| 1.6.1 | 1.7.1 | Plan de Reversibilidad inicial (primeros 90 días) | Transversal |
| 1.6.2 | 1.7.2 | Primera actualización anual del Plan de Reversibilidad durante la implementación | Transversal |
| 1.6.3 | 8.1.4 | Actualizaciones anuales del Plan de Reversibilidad durante los 36 meses de operación | Operación |
| **1.7** | | **Gobierno, control y cierre** | |
| 1.7.1 | 1.8.1 | Oficina de gestión del proyecto con metodología basada en el PMBOK | Transversal |
| 1.7.2 | 1.8.2 | Actas del Comité Ejecutivo mensual, con la aprobación de los cambios de alcance | Transversal |
| 1.7.3 | 1.8.3 | Actas del Comité de Proyecto quincenal | Transversal |
| 1.7.4 | 1.8.4 | Actas del Comité de Arquitectura mensual | Transversal |
| 1.7.5 | 1.8.5 | Actas del Comité de Operación mensual, desde el mes 13 | Transversal |
| 1.7.6 | 1.8.6 | Informe mensual de avance con valor ganado | Transversal |
| 1.7.7 | 1.8.7 | Tablero de estado del proyecto disponible para el CLIENTE | Transversal |
| 1.7.8 | 1.8.8 | Espacio colaborativo con la documentación, los entregables, las actas, los riesgos y los cambio | Transversal |
| 1.7.9 | 9.1.2 | Informe de lecciones aprendidas y archivo de la implementación | Transversal |
| **1.8** | | **Cumplimiento normativo y contractual** | |
| 1.8.1 | 1.9.1 | Matriz de cumplimiento normativo por obligación legal, con su control y su evidencia | Transversal |
| 1.8.2 | 1.9.2 | Acuerdo de tratamiento de datos personales con el CLIENTE | Transversal |
| 1.8.3 | 1.9.3 | Registro de actividades de tratamiento y evaluación de impacto en protección de datos | Transversal |
| 1.8.4 | 1.9.4 | Certificación ISO/IEC 27001 vigente y entrega anual de los informes de certificación | Transversal |
| 1.8.5 | 1.9.5 | Garantía de fiel cumplimiento, seguros y certificados laborales vigentes durante el contrato | Transversal |

**2 Requisitos y diseño aprobados**

| Nuevo | Actual | Paquete | Etapa |
|---|---|---|---|
| **2.1** | | **Requisitos y líneas base de alcance** | |
| 2.1.1 | 1.2.1 | Documento de especificación de requerimientos y línea base de alcance de la Etapa 1 (H1) | Transversal |
| 2.1.2 | 1.2.5 | Documento de línea base de alcance de la Etapa 2: canal moderno y costo de servir (H8) | E2 |
| 2.1.3 | 1.2.4 | Matriz de trazabilidad: requerimiento, módulo, paquete y prueba (H1) | Transversal |
| 2.1.4 | 1.2.2 | Documento de reglas de ruteo capturadas al planificador de rutas | Transversal |
| 2.1.5 | 1.2.3 | Documento de especificación de las interfaces sin documentación del ERP, del WMS de 2013 y de l | Transversal |
| **2.2** | | **Arquitectura de la solución** | |
| 2.2.1 | 2.1.1 | Documento de arquitectura lógica: capas, módulos M1 a M12 e interfaces | E1 |
| 2.2.2 | 2.1.2 | Documento de arquitectura física híbrida: nube, centros de distribución y plataformas de cross- | E1 |
| 2.2.3 | 2.1.3 | Modelo de datos y diccionario de datos, con la trazabilidad por lote | E1 |
| 2.2.4 | 2.1.4 | Documento de diseño detallado de M11 y del intercambio con las cadenas | E2 |
| **2.3** | | **Diseño de la seguridad** | |
| 2.3.1 | 2.2.1 | Plan de seguridad de la información | E1 |
| 2.3.2 | 2.2.2 | Modelado de amenazas por componente y por integración externa, actualizado ante cada cambio | Transversal |
| 2.3.3 | 2.2.3 | Plan de respuesta a incidentes de seguridad, con aviso al CLIENTE en dos horas | E1 |
| 2.3.4 | 2.2.4 | Matriz de clasificación de la información y matriz de controles | E1 |
| **2.4** | | **Diseño de la sala técnica y de los sitios** | |
| 2.4.1 | 2.3.1 | Plano de la sala técnica de Talca, con su cálculo eléctrico y térmico | E1 |
| 2.4.2 | 2.3.2 | Plano de distribución de los racks R01 de servidores y R02 de comunicaciones | E1 |
| 2.4.3 | 2.3.3 | Plano de los gabinetes de borde de Concepción y de las plataformas de cross-docking | E1 |
| **2.5** | | **Continuidad del negocio** | |
| 2.5.1 | 2.5.1 | Plan de continuidad del negocio según ISO 22301, con análisis de impacto y procedimientos manua | E1 |
| 2.5.2 | 2.5.2 | Plan de continuidad TIC según ISO/IEC 27031 y plan de recuperación ante desastres | E1 |
| **2.6** | | **Experiencia de usuario** | |
| 2.6.1 | 2.6.1 | Investigación con preparadores, preventistas, conductores y almaceneros | E1 |
| 2.6.2 | 2.6.2 | Prototipos y pruebas de usabilidad con participantes del CLIENTE | E1 |
| 2.6.3 | 2.6.3 | Indicadores de usabilidad comprometidos por transacción crítica | E1 |
| **2.7** | | **Sistema de cadena de frío validado** | |
| 2.7.1 | 2.4.3 | Validación del diseño del kit en banco de pruebas | E1 |
| 2.7.2 | 2.4.4 | Mapeo térmico por tipo de carrocería | E1 |
| 2.7.3 | 4.1.4 | Piloto de cadena de frío en cuatro camiones | E1 |
| **2.8** | | **Aprobación de los diseños** | |
| 2.8.1 | 2.4.1 | Acta de aprobación de la arquitectura, el plan de seguridad y el modelo de datos (H2) | E1 |
| 2.8.2 | 2.4.2 | Acta de aprobación del diseño detallado de la Etapa 2 (H8) | E2 |

**3 Plataforma base**

| Nuevo | Actual | Paquete | Etapa |
|---|---|---|---|
| **3.1** | | **Ambientes y entrega continua** | |
| 3.1.1 | 3.1.1 | Ambientes de Desarrollo y QA en la nube (H3) | E1 |
| 3.1.2 | 3.1.2 | Ambientes de Preproducción y Producción en la nube (H3) | E1 |
| 3.1.3 | 3.1.3 | Ambiente de recuperación ante desastres en la región secundaria (H3) | E1 |
| 3.1.4 | 3.1.4 | Cadena de integración y entrega continua, e infraestructura como código | E1 |
| 3.1.5 | 3.1.5 | Observabilidad de los doce módulos y de los sitios, con tableros para el CLIENTE (H3) | E1 |
| **3.2** | | **Servicios de nube de la plataforma** | |
| 3.2.1 | 3.2.1 | Servicio de nube para la aplicación y los portales | E1 |
| 3.2.2 | 3.2.2 | Servicio de nube de base de datos, caché y mensajería | E1 |
| 3.2.3 | 3.2.3 | Servicio de nube de ingesta de IoT, telemetría cruda y plataforma analítica | E1 |
| 3.2.4 | 3.2.4 | Servicio de nube de respaldo inmutable y réplica entre regiones | E1 |
| 3.2.5 | 3.2.5 | Servicio de nube de seguridad y gobierno, y detección en endpoints | E1 |
| 3.2.6 | 3.2.6 | Servicio de gestión de dispositivos móviles | E1 |
| **3.3** | | **Servicios comunes** | |
| 3.3.1 | 3.3.1 | Identidad y control de acceso, incluidos los conductores externos que rotan sin aviso | E1 |
| 3.3.2 | 3.3.5 | Registro auditable de stock, lotes y cobros | E1 |
| 3.3.3 | 3.3.6 | Operación sin conexión: 14 horas en terreno y 24 horas en el CD | E1 |

**4 Software operativo**

| Nuevo | Actual | Paquete | Etapa |
|---|---|---|---|
| **4.1** | | **Bodega: recepción, inventario y preparación** | |
| 4.1.1 | 3.4.1 | Recepción de mercadería con captura de lote y vencimiento (M1 Recepción) | E1 |
| 4.1.2 | 3.4.2 | Inventario por ubicación y lote, con FEFO y conteo cíclico (M2 Inventario) | E1 |
| 4.1.3 | 3.4.3 | Preparación de pedidos en el turno de noche y en la cámara de congelado (M5 Preparación) | E1 |
| **4.2** | | **Calidad y cadena de frío** | |
| 4.2.1 | 3.4.4 | Cadena de frío, retención por SSCC y retiro sanitario (M9 Calidad y trazabilidad) | E1 |
| 4.2.2 | 3.4.5 | Ingesta de temperatura (M9) y posición de flota (M12) | E1 |
| **4.3** | | **Venta y reparto** | |
| 4.3.1 | 3.4.6 | Aplicación móvil de preventa sin conexión, con stock y crédito (M3 Preventa) | E1 |
| 4.3.2 | 3.4.7 | Planificación de rutas corregible por el planificador (M4 Rutas) | E1 |
| 4.3.3 | 3.4.8 | Aplicación móvil de reparto con prueba de entrega digital (M6 Reparto) | E1 |
| 4.3.4 | 3.4.9 | Devoluciones en terreno y control de envases (M8 Devoluciones y envases) | E1 |
| 4.3.5 | 3.4.10 | Cobro en ruta, rendición y conciliación (M7 Cobranza y rendición) | E1 |
| **4.4** | | **Canal moderno y portales** | |
| 4.4.1 | 3.5.1 | Pedido electrónico y aviso de despacho para las cadenas, y portal de proveedores (M11 Canal mod | E2 |
| 4.4.2 | 3.5.2 | Portal web de clientes: cuenta, saldo, entregas y documentos | E2 |
| 4.4.3 | 3.5.3 | Portal web de transportistas: rutas asignadas del día siguiente | E2 |
| **4.5** | | **Analítica (M10)** | |
| 4.5.1 | 3.4.11 | Indicadores operacionales y OTIF diario (M10 Analítica) | E1 |
| 4.5.2 | 3.5.4 | Costo de servir por cliente y por entrega (M10 Analítica) | E2 |

**5 Integraciones y datos migrados**

| Nuevo | Actual | Paquete | Etapa |
|---|---|---|---|
| **5.1** | | **Integraciones con el ERP, el WMS y la flota** | |
| 5.1.1 | 3.3.2 | Integración con el ERP como único emisor de la guía de despacho (INT-06 e INT-07) | E1 |
| 5.1.2 | 3.3.3 | Convivencia con el WMS de 2013 durante el reemplazo | E1 |
| 5.1.3 | 3.3.4 | Integración con la telemetría de los 42 camiones propios (INT-15) | E1 |
| **5.2** | | **Integraciones con servicios externos** | |
| 5.2.1 | 3.6.1 | Intercambio de lote y trazabilidad con los proveedores | E1 |
| 5.2.2 | 3.6.2 | Integración con la pasarela de pago para el cobro con tarjeta (INT-09) | E1 |
| 5.2.3 | 3.6.3 | Integración con el servicio de mapas y geocodificación (INT-10) | E1 |
| 5.2.4 | 3.6.4 | Integración con el servicio de avisos al cliente (INT-11) | E1 |
| **5.3** | | **Intercambio electrónico con las cadenas** | |
| 5.3.1 | 3.6.5 | Intercambio electrónico con la principal cadena, con sus pruebas aprobadas (INT-08) | E2 |
| 5.3.2 | 3.6.6 | Incorporación de las demás cadenas al intercambio electrónico (INT-08) | E2 |
| **5.4** | | **Migración de datos** | |
| 5.4.1 | 3.7.1 | Informe de perfilamiento y datos saneados | E1 |
| 5.4.2 | 3.7.2 | Datos maestros cargados: 8.400 SKU, clientes e instalaciones | E1 |
| 5.4.3 | 3.7.3 | Saldos migrados desde el WMS de Talca | E1 |
| 5.4.4 | 3.7.4 | Saldos cargados en Concepción desde el conteo físico | E1 |
| 5.4.5 | 3.7.5 | Acta de conciliación y corte fuera de las ventanas de congelamiento | E1 |

**6 Solución certificada y documentada**

| Nuevo | Actual | Paquete | Etapa |
|---|---|---|---|
| **6.1** | | **Pruebas de integración y regresión** | |
| 6.1.1 | 3.8.1 | Pruebas de integración, regresión e idempotencia en QA (H4) | E1 |
| 6.1.2 | 3.9.1 | Pruebas de integración y regresión sin afectar la Etapa 1 en producción (H9) | E2 |
| **6.2** | | **Pruebas de aceptación, accesibilidad y condiciones físicas** | |
| 6.2.1 | 3.8.2 | Pruebas de aceptación y de accesibilidad con preventistas, conductores y bodega | E1 |
| 6.2.2 | 3.8.3 | Cinco condiciones físicas: −22 °C con guantes, lluvia, calor superior a 34 °C, sol directo y us | E1 |
| 6.2.3 | 3.9.2 | Pruebas de aceptación y de accesibilidad con cadenas, transportistas, Comercial y Finanzas | E2 |
| **6.3** | | **Pruebas de carga y resiliencia** | |
| 6.3.1 | 3.8.4 | Pruebas de carga con el peak de septiembre y de resiliencia | E1 |
| 6.3.2 | 3.9.3 | Pruebas de carga con ambas etapas activas y de resiliencia | E2 |
| **6.4** | | **Pruebas de recuperación ante desastres** | |
| 6.4.1 | 3.8.5 | Prueba de recuperación ante desastres con conmutación real | E1 |
| 6.4.2 | 3.9.4 | Prueba de recuperación ante desastres con ambas etapas | E2 |
| **6.5** | | **Pruebas de seguridad ofensiva** | |
| 6.5.1 | 3.8.6 | Prueba de seguridad ofensiva de la Etapa 1, por un tercero independiente | E1 |
| 6.5.2 | 3.9.5 | Prueba de seguridad ofensiva de la Etapa 2, por un tercero independiente | E2 |
| **6.6** | | **Despliegue sin interrupción demostrado** | |
| 6.6.1 | 3.8.8 | Demostración en Preproducción del despliegue sin interrupción de la Etapa 1 | E1 |
| 6.6.2 | 3.9.7 | Demostración en Preproducción del despliegue sin interrupción de la Etapa 2 | E2 |
| **6.7** | | **Actas de certificación** | |
| 6.7.1 | 3.8.7 | Acta de certificación de la Etapa 1 (H5) | E1 |
| 6.7.2 | 3.9.6 | Acta de certificación de la Etapa 2 y cierre del desarrollo (H10) | E2 |
| **6.8** | | **Documentación técnica, código y custodia** | |
| 6.8.1 | 3.11.1 | Documentación técnica, funcional, de arquitectura, de operación y de seguridad | Transversal |
| 6.8.2 | 3.11.2 | Base de conocimiento de incidentes y decisiones de diseño | Transversal |
| 6.8.3 | 3.11.3 | Estándares de codificación y documentación de interfaces en OpenAPI y AsyncAPI | Transversal |
| 6.8.4 | 3.11.4 | Inventario de componentes (SBOM) con sus licencias de código abierto | Transversal |
| 6.8.5 | 3.11.5 | Depósito del código fuente en el repositorio del CLIENTE en cada liberación | Transversal |
| 6.8.6 | 9.1.1 | Entrega del código fuente, la infraestructura como código y los procedimientos de despliegue | E2 |
| 6.8.7 | 5.4.4 | Contrato de custodia de fuentes con un tercero independiente | E1 |

**7 Innovaciones verificadas**

| Nuevo | Actual | Paquete | Etapa |
|---|---|---|---|
| **7.1** | | **INN-01** | |
| 7.1.1 | 3.10.1.1 | Innovación 1: documento de catálogo de acciones y protocolo del piloto (INN-01.P1) | E1 |
| 7.1.2 | 3.10.1.2 | Innovación 1: estimador de saldo y ritmo de reposición (INN-01.P2) | E1 |
| 7.1.3 | 3.10.1.3 | Innovación 1: función de lista sin conexión en la aplicación de preventa (INN-01.P3) | E1 |
| 7.1.4 | 3.10.1.4 | Innovación 1: informe del piloto en marcha blanca y habilitación (INN-01.P4) | E1 |
| **7.2** | | **INN-02** | |
| 7.2.1 | 3.10.2.1 | Innovación 2: informe de medición inicial y contrato de evidencia (INN-02.P1) | E1 |
| 7.2.2 | 3.10.2.2 | Innovación 2: circuito mínimo de reproducción en la preventa (INN-02.P2) | E1 |
| 7.2.3 | 3.10.2.3 | Innovación 2: captura de evidencia en las aplicaciones de preventa, preparación y reparto (INN- | E1 |
| 7.2.4 | 3.10.2.4 | Innovación 2: informe de validación comparada durante la implementación (INN-02.P4, primera par | E1 |
| 7.2.5 | 8.3.1 | Innovación 2: mantenimiento de escenarios de regresión (INN-02.P4, segunda parte) | Operación |
| **7.3** | | **INN-03** | |
| 7.3.1 | 3.10.3.1 | Innovación 3: documento de familias priorizadas y parámetros aprobados (INN-03.P1) | E1 |
| 7.3.2 | 3.10.3.2 | Innovación 3: asociación lote–sensor en el borde y en el camión (INN-03.P2) | E1 |
| 7.3.3 | 3.10.3.3 | Innovación 3: vista en M9 y orden de salida sugerido (INN-03.P3) | E1 |
| 7.3.4 | 3.10.3.4 | Innovación 3: informe de validación en marcha blanca con Calidad (INN-03.P4) | E1 |
| 7.3.5 | 8.3.2 | Innovación 3: revisión periódica de parámetros durante la Operación (INN-03.P5) | Operación |
| **7.4** | | **INN-04** | |
| 7.4.1 | 5.4.3 | Fórmula aprobada del tramo variable: reglas de atribución, canasta e índices (INN-04.P1) | E2 |
| 7.4.2 | 8.3.3 | Innovación 4: línea base y liquidaciones en sombra (INN-04.P2) | Operación |
| 7.4.3 | 8.3.4 | Innovación 4: liquidación mensual del tramo variable, meses 24 a 56 (INN-04.P3) | Operación |
| **7.5** | | **INN-05** | |
| 7.5.1 | 3.10.4.1 | Innovación 5: prototipo e informe de la prueba de comprensión (INN-05.P1) | E2 |
| 7.5.2 | 3.10.4.2 | Innovación 5: evaluación de privacidad y diseño de la impresión en cabina (INN-05.P2) | E2 |
| 7.5.3 | 3.10.4.3 | Innovación 5: cálculo y bloques 1 a 3 de la hoja de negocio (INN-05.P3) | E2 |
| 7.5.4 | 3.10.4.4 | Innovación 5: hoja certificada, en marcha blanca y en producción (INN-05.P4, primera parte) | E2 |
| 7.5.5 | 8.3.5 | Innovación 5: despliegue gradual por rutas (INN-05.P4, segunda parte) | Operación |
| 7.5.6 | 8.3.6 | Innovación 5: bloque 4 condicionado (INN-05.P5) | Operación |

**8 Infraestructura, equipamiento y servicios habilitados**

| Nuevo | Actual | Paquete | Etapa |
|---|---|---|---|
| **8.1** | | **Compras de hardware y especificaciones** | |
| 8.1.1 | 5.1.1 | Especificación de compra de equipos de uso para el CLIENTE | E1 |
| 8.1.2 | 5.1.2 | Especificación y compra de la sala técnica, los racks, los servidores y los gabinetes de borde | E1 |
| 8.1.3 | 5.1.3 | Actas de recepción técnica del equipamiento de terreno comprado por el CLIENTE y de la infraest | E1 |
| 8.1.4 | 5.1.4 | Especificación y compra del sistema de cadena de frío | E1 |
| **8.2** | | **Servicios de nube, licencias y enlaces contratados** | |
| 8.2.1 | 5.2.1 | Contrato de los servicios de AWS | E1 |
| 8.2.2 | 5.2.2 | Suscripción del servicio de gestión de dispositivos y de detección en endpoints | E1 |
| 8.2.3 | 5.2.3 | Licencias de software de terceros constituidas a nombre del CLIENTE | E1 |
| 8.2.4 | 5.3.1 | Contrato de fibra óptica de los CD de Talca y Concepción | E1 |
| 8.2.5 | 5.3.2 | Contrato de planes LTE con dos proveedores (ocho planes) | E1 |
| 8.2.6 | 5.3.3 | Contrato de Starlink para los cinco sitios: Talca, Concepción y las tres plataformas de cross-d | E1 |
| 8.2.7 | 5.3.4 | Contrato de SIM M2M y servicio satelital de los camiones con frío | E1 |
| **8.3** | | **Sala técnica de Talca habilitada** | |
| 8.3.1 | 6.1.1 | Coordinación de la obra civil de separación, a cargo del CLIENTE (RT-06.06), y piso técnico de  | E1 |
| 8.3.2 | 6.1.2 | Hardware de energía instalado: UPS modular N+1, generador con 24 horas de autonomía, transferen | E1 |
| 8.3.3 | 6.1.3 | Hardware de climatización de precisión N+1 instalado | E1 |
| 8.3.4 | 6.1.4 | Hardware de detección temprana de incendio y extinción por agente limpio instalado | E1 |
| 8.3.5 | 6.1.5 | Acta de recepción técnica de la sala | E1 |
| **8.4** | | **Cableado, racks y gabinetes** | |
| 8.4.1 | 6.2.1 | Cableado de cobre Cat6A y fibra OM4 tendido, con dos ductos de ingreso independientes | E1 |
| 8.4.2 | 6.2.2 | Certificación de enlaces, etiquetado y planos as-built | E1 |
| 8.4.3 | 6.2.3 | Gabinetes de piso y switches de acceso instalados en las bodegas de Talca y Concepción | E1 |
| 8.4.4 | 6.3.1 | Rack R01 de servidores montado: clúster de tres nodos, respaldo local, consola KVM y traslado d | E1 |
| 8.4.5 | 6.3.2 | Rack R02 de comunicaciones montado: firewalls, switches de núcleo y de gestión, y distribución  | E1 |
| 8.4.6 | 6.3.3 | Gabinete de borde de Concepción montado: servidores activo y en espera, firewalls, switches, UP | E1 |
| 8.4.7 | 6.3.4 | Gabinetes de borde montados en Curicó, Chillán y Los Ángeles, con dos mini-PC (activo y en espe | E1 |
| **8.5** | | **Seguridad física** | |
| 8.5.1 | 6.4.1 | Hardware de control de acceso biométrico y esclusa instalado | E1 |
| 8.5.2 | 6.4.2 | Hardware de videovigilancia instalado | E1 |
| 8.5.3 | 6.4.3 | Recinto de custodia de respaldos habilitado | E1 |
| **8.6** | | **Equipamiento de campo** | |
| 8.6.1 | 6.5.1 | Terminales de preventa, reparto y bodega configurados y enrolados | E1 |
| 8.6.2 | 6.5.2 | Terminales de pago configurados, uno por camión | E1 |
| 8.6.3 | 6.5.3 | Sensores de cámara y gateways IoT instalados en Talca y Concepción | E1 |
| 8.6.4 | 6.5.4 | Kit de cadena de frío instalado y recibido en los 28 camiones con frío | E1 |
| 8.6.5 | 6.5.5 | Impresoras de cabina instaladas | E1 |
| 8.6.6 | 6.5.6 | Impresoras de andén y balanzas de recepción instaladas | E1 |
| **8.7** | | **Configuración de los sitios** | |
| 8.7.1 | 6.6.1 | Software de base instalado en los sitios: virtualización, contenedores, PostgreSQL, RabbitMQ y  | E1 |
| 8.7.2 | 6.6.2 | Enlaces de fibra, LTE y Starlink habilitados, con conmutación al respaldo | E1 |
| 8.7.3 | 6.6.3 | Borde de los CD en servicio, con la prueba de autonomía de 24 horas aprobada | E1 |

**9 Implantación y usuarios habilitados**

| Nuevo | Actual | Paquete | Etapa |
|---|---|---|---|
| **9.1** | | **Planes de implantación y reversión** | |
| 9.1.1 | 4.1.1 | Plan de olas de la Etapa 1 por sitio y zona: Talca, Concepción y plataformas de cross-docking | E1 |
| 9.1.2 | 4.1.2 | Procedimiento de reversión de la Etapa 1 antes de las 05:30, con versión operativa local y DTE  | E1 |
| 9.1.3 | 4.1.3 | Plan de implantación y reversión de la Etapa 2 fuera de la ventana de 05:30 a 07:00 | E2 |
| **9.2** | | **Marcha blanca** | |
| 9.2.1 | 4.2.1 | Marcha blanca de la Etapa 1 con conciliación diaria (H6) | E1 |
| 9.2.2 | 4.3.1 | Marcha blanca de la Etapa 2 en convivencia con la Etapa 1 y fuente única de datos (H11) | E2 |
| **9.3** | | **Estabilización** | |
| 9.3.1 | 4.2.2 | Estabilización de la Etapa 1, acompañamiento en ruta y restauraciones de soporte puente | E1 |
| 9.3.2 | 4.3.2 | Estabilización de la Etapa 2 con Comercial, Finanzas, cadenas y transportistas | E2 |
| **9.4** | | **Aceptación y paso a producción** | |
| 9.4.1 | 4.2.3 | Expediente de H7 | E1 |
| 9.4.2 | 4.3.3 | Expediente de H12 | E2 |
| 9.4.3 | 4.3.4 | Garantía de correcto funcionamiento constituida, condición de la aceptación final (H12) | E2 |
| **9.5** | | **Capacitación y certificación de usuarios** | |
| 9.5.1 | 7.1.1 | Plan de capacitación por perfil: usuarios finales, avanzados, administradores, equipo técnico y | Transversal |
| 9.5.2 | 7.1.2 | Programa de capacitación continua del turno de noche por la rotación del 38 % | E1 |
| 9.5.3 | 7.1.3 | Incorporación de conductores de transportistas, escaneos y lectura del rojo | E1 |
| 9.5.4 | 7.1.4 | Traspaso al equipo de TI de cuatro personas del CLIENTE | Transversal |
| 9.5.5 | 7.1.5 | Materiales de capacitación: manuales por perfil, guías rápidas, preguntas frecuentes y videos t | Transversal |
| 9.5.6 | 7.1.6 | Plataforma de autoformación en línea con registro de avance | Transversal |
| 9.5.7 | 7.3.1 | Certificación de preventistas, conductores y preparadores (Etapa 1) | E1 |
| 9.5.8 | 7.3.2 | Certificación de Comercial y Finanzas en costo de servir (Etapa 2) | E2 |
| **9.6** | | **Gestión del cambio** | |
| 9.6.1 | 7.2.1 | Acompañamiento del personal con 20 o 30 años en la compañía | Transversal |
| 9.6.2 | 7.2.2 | Gestión del cambio con las cadenas y los transportistas | E2 |
| 9.6.3 | 7.2.3 | Diagnóstico del impacto organizacional por área y perfil, con agentes de cambio | Transversal |
| 9.6.4 | 7.2.4 | Procedimientos operativos rediseñados, contingencia de frío y ruptura confirmada | Transversal |
| 9.6.5 | 7.2.5 | Medición de la adopción y plan de acción correctiva | Transversal |
| **9.7** | | **Acuerdos con terceros** | |
| 9.7.1 | 5.4.1 | Acuerdos operacionales firmados con los diez transportistas | E1 |
| 9.7.2 | 5.4.2 | Acta de acuerdo con el sindicato sobre terminales, GPS y cámaras | E1 |

**10 Servicio de operación y salida**

| Nuevo | Actual | Paquete | Etapa |
|---|---|---|---|
| **10.1** | | **Servicios de operación** | |
| 10.1.1 | 8.1.1 | Servicio de centro de operaciones 247 y mesa de servicio durante los 36 meses de operación (04: | Operación |
| 10.1.2 | 8.1.2 | Servicio de gestión de incidentes, problemas y niveles de servicio del Art. 78° durante los 36  | Operación |
| 10.1.3 | 8.1.3 | Servicio de continuidad y pruebas semestrales de recuperación ante desastres durante los 36 mes | Operación |
| 10.1.4 | 8.1.5 | Servicio de centro de operaciones de seguridad 247 con SIEM desde la primera marcha blanca (mes | Operación |
| 10.1.5 | 8.1.6 | Pruebas mensuales de restauración de respaldos durante los 36 meses de operación | Operación |
| **10.2** | | **Mantenimiento** | |
| 10.2.1 | 8.2.1 | Mantenimiento correctivo y evolutivo del software durante los 36 meses de operación, con bolsa  | Operación |
| 10.2.2 | 8.2.2 | Mantenimiento de ciberseguridad durante los 36 meses de operación: vulnerabilidades, intrusión  | Operación |
| 10.2.3 | 8.2.3 | Mantenimiento del hardware durante los 36 meses de operación: sala técnica, racks, gabinetes de | Operación |
| 10.2.4 | 8.2.4 | Registro y reducción de la deuda técnica durante los 36 meses de operación | Operación |
| 10.2.5 | 8.2.5 | Actualizaciones anuales de los componentes de base durante los 36 meses de operación | Operación |
| 10.2.6 | 8.2.6 | Revisiones semestrales de las instalaciones eléctricas de la sala durante los 36 meses de opera | Operación |
| 10.2.7 | 8.2.7 | Ciclo de vida del equipamiento durante los 36 meses de operación: reposición y disposición fina | Operación |
| **10.3** | | **Informes y obligaciones periódicas** | |
| 10.3.1 | 8.4.1 | Gestión de la capacidad con proyección trimestral durante los 36 meses de operación | Operación |
| 10.3.2 | 8.4.2 | Informes mensuales de consumo de nube (FinOps) durante los 36 meses de operación | Operación |
| 10.3.3 | 8.4.3 | Estimaciones anuales de la huella de carbono de la operación | Operación |
| 10.3.4 | 8.4.4 | Actualizaciones semestrales del depósito de custodia de fuentes durante los 36 meses de operaci | Operación |
| **10.4** | | **Capacitación y transferencia en operación** | |
| 10.4.1 | 8.5.1 | Dos jornadas anuales de actualización y capacitación del personal nuevo durante los 36 meses de | Operación |
| 10.4.2 | 8.5.2 | Mentoría al equipo técnico del CLIENTE durante los seis meses posteriores al mes 21 | Operación |
| 10.4.3 | 8.5.3 | Mantenimiento de la base de conocimiento durante los 36 meses de operación, con métricas de uso | Operación |
| **10.5** | | **Salida al término del contrato** | |
| 10.5.1 | 9.2.1 | Ejecución del Plan de Reversibilidad y acompañamiento de 90 días | Operación |
| 10.5.2 | 9.2.2 | Certificado de devolución o eliminación de datos personales | Operación |

## Anexo B. Predecesoras para los 77 paquetes que hoy no tienen

FC salvo que se indique CC (comienzo–comienzo). Los códigos están en la numeración nueva.

| Nuevo | Actual | Predecesora propuesta (código nuevo) | Motivo |
|---|---|---|---|
| 1.1.1 | 1.1.1 | Firma del contrato | Primer paquete: arranca con la firma del contrato |
| 1.1.2 | 1.1.2 | 1.1.1 | Valida problemas y metas una vez constituido el proyecto |
| 1.1.3 | 1.1.3 | 1.1.1 | Las confirmaciones se tratan en la primera sesión con la Contraparte |
| 2.1.1 | 1.2.1 | 1.1.2 | La especificación parte de los problemas y metas validados |
| 2.1.5 | 1.2.3 | 1.1.1 | Requiere acceso a ERP, WMS y bitácoras del CLIENTE |
| 2.1.3 | 1.2.4 | 2.1.1; 1.2.2 | Traza requisitos aprobados contra paquetes de la EDT |
| 2.1.2 | 1.2.5 | 6.7.1 (H5); 2.8.2 CC | La línea base de la Etapa 2 se fija con la Etapa 1 certificada |
| 1.2.1 | 1.3.1 | 1.1.1 | Plan de dirección tras la constitución |
| 1.2.2 | 1.3.2 | 2.1.1 | La EDT se fija sobre el alcance especificado |
| 1.2.3 | 1.3.3 | 1.2.2 | La carta se construye sobre la EDT |
| 1.2.4 | 1.3.4 | 1.2.3 | La nivelación usa la carta |
| 1.3.1 | 1.4.1 | 1.1.1 | Registro de interesados tras la constitución |
| 1.3.2 | 1.4.2 | 1.3.1 | Las comunicaciones dependen del registro de interesados |
| 1.4.1 | 1.5.1 | 2.1.1 | El plan de pruebas parte de los requisitos |
| 1.5.1 | 1.6.1 | 1.2.1 | Los riesgos se registran sobre el plan de dirección |
| 1.6.1 | 1.7.1 | 2.2.2 | La reversibilidad necesita la arquitectura física |
| 1.6.2 | 1.7.2 | 1.6.1 (FC + 12 meses) | Actualización anual del plan inicial |
| 1.8.1 | 1.9.1 | 1.1.1 | Matriz normativa al inicio |
| 1.8.2 | 1.9.2 | 1.1.1 | Acuerdo de datos al inicio |
| 1.8.3 | 1.9.3 | 1.8.2 | El registro de tratamiento sigue al acuerdo de datos |
| 2.2.2 | 2.1.2 | 2.1.1; 2.4.1 CC | Arquitectura física sobre el alcance y en paralelo con la sala |
| 2.2.3 | 2.1.3 | 2.1.1 | El modelo de datos parte de los requisitos |
| 2.2.4 | 2.1.4 | 2.1.2 | El diseño de M11 sigue a la línea base de la Etapa 2 |
| 2.3.1 | 2.2.1 | 1.8.1; 2.2.1 CC | Seguridad sobre las obligaciones normativas y la arquitectura |
| 2.3.3 | 2.2.3 | 2.3.1 | La respuesta a incidentes deriva del plan de seguridad |
| 2.3.4 | 2.2.4 | 1.8.1 | La clasificación deriva de la matriz normativa |
| 2.4.1 | 2.3.1 | Firma del contrato | Ruta crítica de la sala técnica (H3) |
| 2.4.2 | 2.3.2 | 2.4.1 CC | Racks se diseñan junto con la sala |
| 2.4.3 | 2.3.3 | 2.4.1 | Gabinetes de borde con el mismo criterio de la sala |
| 2.5.1 | 2.5.1 | 2.2.2 | El análisis de impacto usa la arquitectura física |
| 2.5.2 | 2.5.2 | 2.2.2; 2.5.1 CC | Continuidad TIC sobre la arquitectura física |
| 2.6.1 | 2.6.1 | 1.3.1 | La investigación usa el registro de interesados |
| 2.6.2 | 2.6.2 | 2.6.1 | Prototipos a partir de la investigación |
| 2.6.3 | 2.6.3 | 2.6.2 | Indicadores a partir de las pruebas de usabilidad |
| 3.1.4 | 3.1.4 | 3.2.1; 2.8.1 | Cadena de entrega sobre la nube contratada y la arquitectura aprobada |
| 3.1.5 | 3.1.5 | 3.1.1–3.1.3 CC | Observabilidad junto con los ambientes |
| 5.1.2 | 3.3.3 | 2.1.5; 2.8.1 | Convivencia con el WMS según las interfaces levantadas |
| 5.1.3 | 3.3.4 | 2.1.5; 3.2.3 | Telemetría sobre la ingesta de IoT |
| 3.3.2 | 3.3.5 | 2.2.3; 2.8.1 | Registro auditable sobre el modelo de datos aprobado |
| 3.3.3 | 3.3.6 | 2.8.1; 3.3.1 CC | Operación sin conexión sobre la identidad |
| 7.1.1 | 3.10.1.1 | 2.8.1 | INN-01 parte con la arquitectura aprobada |
| 7.2.1 | 3.10.2.1 | 2.1.1 | INN-02 mide sobre los requisitos aprobados |
| 7.3.1 | 3.10.3.1 | 2.1.1; 2.2.3 CC | INN-03 fija parámetros con el modelo de datos |
| 7.5.1 | 3.10.4.1 | 4.3.3; 2.1.2 CC | INN-05 usa la aplicación de reparto (M6) |
| 9.4.3 | 4.3.4 | 6.7.2 (H10) | La garantía se constituye con la Etapa 2 certificada |
| 8.1.1 | 5.1.1 | 2.1.1 | Equipos de uso según los requisitos |
| 8.1.3 | 5.1.3 | 8.1.1; 8.1.2 | Recepción de lo especificado y comprado |
| 8.2.1 | 5.2.1 | 2.2.2 | Contrato de nube según la arquitectura física |
| 8.2.2 | 5.2.2 | 8.2.1 | Suscripciones sobre la cuenta de nube |
| 8.2.3 | 5.2.3 | 2.8.1 | Licencias según la arquitectura aprobada |
| 8.2.4 | 5.3.1 | 2.2.2 | Enlaces según la arquitectura física |
| 8.2.5 | 5.3.2 | 2.2.2 | Planes LTE según la arquitectura física |
| 8.2.6 | 5.3.3 | 2.4.3 | Starlink según el diseño de sitios |
| 9.7.1 | 5.4.1 | 1.3.2; 9.6.3 | Acuerdos con transportistas con el plan de comunicaciones y el diagnóstico |
| 9.7.2 | 5.4.2 | 9.6.3 | Acuerdo sindical sobre el diagnóstico organizacional |
| 7.4.1 | 5.4.3 | 4.5.2 | La fórmula de INN-04 usa el costo de servir |
| 6.8.7 | 5.4.4 | 3.1.4 | Custodia sobre el repositorio y la cadena de entrega |
| 8.4.1 | 6.2.1 | 8.3.1; 2.4.2 | Cableado tras la obra civil, según el plano de racks |
| 8.4.2 | 6.2.2 | 8.4.1 | Certificación del cableado tendido |
| 8.4.3 | 6.2.3 | 8.4.2; 2.4.3 | Gabinetes de piso tras certificar el cableado |
| 8.4.6 | 6.3.3 | 2.4.3; 8.1.2 | Gabinete de borde diseñado y comprado |
| 8.4.7 | 6.3.4 | 8.4.6 | Plataformas replican el gabinete de Concepción |
| 8.5.1 | 6.4.1 | 8.3.5 | Seguridad física en la sala recibida |
| 8.5.2 | 6.4.2 | 8.3.5 | Videovigilancia en la sala recibida |
| 8.5.3 | 6.4.3 | 8.5.1 | Custodia con el acceso controlado |
| 8.6.2 | 6.5.2 | 8.1.3; 5.2.2 | Terminales de pago recibidos e integrados |
| 8.6.3 | 6.5.3 | 8.1.3; 8.4.3 | Sensores recibidos, con red de bodega |
| 8.6.5 | 6.5.5 | 8.1.3 | Impresoras recibidas |
| 8.6.6 | 6.5.6 | 8.1.3; 8.4.3 | Impresoras y balanzas recibidas, con red de bodega |
| 9.5.1 | 7.1.1 | 2.6.3; 9.1.1 CC | Plan de capacitación con los indicadores de uso y las olas |
| 9.5.6 | 7.1.6 | 9.5.1 CC | Plataforma junto con el plan |
| 9.6.2 | 7.2.2 | 9.1.3; 5.3.1 | Cambio con cadenas y transportistas según el plan de la Etapa 2 |
| 9.6.3 | 7.2.3 | 1.3.1 | Diagnóstico organizacional sobre el registro de interesados |
| 9.5.7 | 7.3.1 | 9.5.1; 9.2.1 CC | Certificación de usuarios durante la marcha blanca de la Etapa 1 |
| 9.5.8 | 7.3.2 | 4.5.2; 6.2.3 | Certificación en costo de servir con el módulo aceptado |
| 6.8.6 | 9.1.1 | 6.7.2 (H10) | Entrega del código con el desarrollo cerrado |
| 10.5.2 | 9.2.2 | 10.5.1 | Certificado al término de la ejecución de la reversibilidad |
