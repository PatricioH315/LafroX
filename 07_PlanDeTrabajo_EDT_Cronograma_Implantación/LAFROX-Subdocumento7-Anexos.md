# Anexos del Subdocumento 7

Estos anexos detallan los listados que el Subdocumento 7 resume. La EDT, el diccionario y la carta Gantt están en el Formulario T-14; el método de estimación y programación, la ruta crítica y los frentes de trabajo, en el Formulario T-15; y la implantación, en el Formulario T-18.

## Anexo 7.A — Meses contractuales y ventanas de congelamiento según la fecha de inicio

El Art. 17° de las Bases Administrativas fija los meses del contrato, no sus fechas. El mes 1 es el primer mes completo de ejecución (Bases Administrativas, Art. 10°, numeral 2). Si el contrato se inicia en el mes calendario $m$, el mes contractual $n$ cae en el mes calendario $m + (n - 1)$, contado en aritmética de doce meses.

El caso fija las ventanas del año: congelamiento total del 1 al 25 de septiembre y durante todo diciembre; congelamiento en los tres primeros días hábiles de cada mes (Caso 02, RT-10.05); y ningún paso a producción en septiembre ni en diciembre (sección 13.3, condición 2). El Capítulo 3, sección 3.1.2, deriva de esa regla los ocho meses de inicio que no ponen los meses 16 ni 21 en septiembre o diciembre (supuesto S-17). La Tabla «tab:7A1» aplica la misma fórmula a los meses de marcha blanca; los meses en negrita caen en una ventana de congelamiento.

**Meses calendario de los períodos contractuales según el mes de inicio. Fuente: elaboración propia a partir de las Bases Administrativas, Art. 17°, y del Caso 02, secciones 13.2 y 13.3.**

<a id="tab:7A1"></a>

| Inicio del contrato | Mes 13 (H6) | Meses 14 y 15 | Mes 16 (H7) | Mes 19 (H11) | Mes 20 | Mes 21 (H12) |
| --- | --- | --- | --- | --- | --- | --- |
| Diciembre de 2026 | **Diciembre de 2027** | Enero y febrero de 2028 | Marzo de 2028 | Junio de 2028 | Julio de 2028 | Agosto de 2028 |
| Febrero de 2027 | Febrero de 2028 | Marzo y abril de 2028 | Mayo de 2028 | Agosto de 2028 | **Septiembre de 2028** | Octubre de 2028 |
| Marzo de 2027 | Marzo de 2028 | Abril y mayo de 2028 | Junio de 2028 | **Septiembre de 2028** | Octubre de 2028 | Noviembre de 2028 |
| Mayo de 2027 | Mayo de 2028 | Junio y julio de 2028 | Agosto de 2028 | Noviembre de 2028 | **Diciembre de 2028** | Enero de 2029 |
| Julio de 2027 | Julio de 2028 | Agosto y **septiembre** de 2028 | Octubre de 2028 | Enero de 2029 | Febrero de 2029 | Marzo de 2029 |
| Agosto de 2027 | Agosto de 2028 | **Septiembre** y octubre de 2028 | Noviembre de 2028 | Febrero de 2029 | Marzo de 2029 | Abril de 2029 |
| Octubre de 2027 | Octubre de 2028 | Noviembre y **diciembre** de 2028 | Enero de 2029 | Abril de 2029 | Mayo de 2029 | Junio de 2029 |
| Noviembre de 2027 | Noviembre de 2028 | **Diciembre** de 2028 y enero de 2029 | Febrero de 2029 | Mayo de 2029 | Junio de 2029 | Julio de 2029 |

La tabla lleva a tres conclusiones. Primero, ningún inicio admisible deja las dos marchas blancas completas fuera de septiembre y diciembre: siempre hay al menos un mes de marcha blanca dentro de una ventana de congelamiento. Segundo, solo los inicios de diciembre de 2026, febrero de 2027 y marzo de 2027 ponen en producción la Etapa 2 antes de enero de 2029, fecha desde la que rigen las condiciones de la principal cadena de supermercados (Caso 02, sección 13.2; Capítulo 3, sección 3.1.2).

Tercero, entre esos tres inicios, febrero de 2027 es el único en que el congelamiento afecta solo el último mes de una marcha blanca (el mes 20, de la Etapa 2) y no un inicio de marcha blanca. Con diciembre de 2026, el H6 caería en diciembre; con marzo de 2027, el H11 caería en septiembre. Con febrero de 2027, las cuatro semanas de cierre de la marcha blanca de la Etapa 2 coinciden con el peak de Fiestas Patrias; por eso toda habilitación de la Etapa 2 ocurre en agosto de 2028 y el cierre se mide con el volumen del peak (Formulario T-18, sección 3.1). LafroX adopta febrero de 2027 como supuesto de calendario de la carta Gantt.

Durante un mes de congelamiento que cae dentro de una marcha blanca no se inicia ninguna ola ni se despliega ningún cambio. La marcha blanca continúa en convivencia con la forma actual de trabajar, se siguen midiendo los indicadores diarios y el volumen real de septiembre sirve como prueba de carga en operación. La fecha efectiva de inicio se confirma con la consulta V-12 (Capítulo 3, Anexo 3.H).

## Anexo 7.B — Dependencias entre paquetes de trabajo

La Tabla «tab:7B1» lista las dependencias que estructuran la red del cronograma. Son de tipo fin-comienzo (FC), salvo las marcadas como comienzo-comienzo (CC) y las de tipo «por interfaz», en que el sucesor espera los contratos del predecesor para construir y su entrega para integrar; cada una indica su fundamento. El Formulario T-15, sección 6.1, aplica estas dependencias actividad por actividad. Sobre esta red se identifica la ruta crítica del Subdocumento 7, sección 7.3.1, y se aplica el método de programación del Formulario T-15.

**Dependencias entre paquetes de trabajo. Fuente: elaboración propia a partir de los Formularios T-14 y T-18 y de los capítulos indicados.**

<a id="tab:7B1"></a>

| N.° | Predecesor | Sucesor | Tipo | Fundamento |
| --- | --- | --- | --- | --- |
| D-01 | 1.2.1 Línea base de alcance de la Etapa 1 (H1) | 2.1.1 Arquitectura lógica | FC | El diseño parte del alcance aprobado |
| D-02 | 1.2.3 Especificación de las interfaces sin documentación | 3.3.2 Integración con el ERP | FC | Interfaces sin documentación (Caso 02, sección 17.5) |
| D-03 | 1.2.2 Reglas de ruteo del planificador | 3.4.7 M4 Rutas | FC | Captura del conocimiento antes de la jubilación (Caso 02, cap. 18, resultado 16) |
| D-04 | 2.4.1 Aprobación de arquitectura, seguridad y datos (H2) | 3.4 Módulos de la Etapa 1 | FC | No se construye sin diseño aprobado (Capítulo 6, fase de Elaboración) |
| D-05 | 2.6.2 Prototipos y pruebas de usabilidad | 3.4 Módulos de la Etapa 1 | FC | Diseño con usuarios antes de construir (Bases Administrativas, Art. 26°); 2.6.2 cierra antes de que empiece 3.4 (Formulario T-15, Tabla 6.1) |
| D-06 | 2.2.1 Plan de seguridad | 3.3.1 Identidad y control de acceso | FC | La identidad aplica el plan de seguridad aprobado en el H2 |
| D-07 | 5.2.1 Contrato de los servicios de AWS | 3.2 Servicios de nube | FC | Servicios activos antes de configurar ambientes |
| D-08 | 3.2.1, 3.2.2, 3.2.4 y 3.2.5 Servicios de nube de aplicación, datos, respaldo y seguridad | 3.1.1 a 3.1.3 Ambientes en la nube (H3) | FC | Los ambientes usan los servicios configurados. La ingesta de IoT 3.2.3 precede a M12 (3.4.5) y la gestión de dispositivos 3.2.6 precede a la configuración de terminales (6.5.1); no condicionan los ambientes |
| D-09 | 2.3.1 y 2.3.2 Planos de sala y racks | 5.1.2 Especificación de compra de sala y racks | FC | Se especifica lo diseñado; planos en los meses 1 y 2 y especificación en los meses 2 y 3 |
| D-10 | 5.1.2 Especificación de compra | 6.1 Sala técnica de Talca | FC | Se instala el suministro recibido conforme a responsabilidades BTT/SD4/T-11; la compra de terreno del CLIENTE no transfiere toda provisión de sala/racks. 6.1 empieza en el mes 3, por lo que el CLIENTE compra dentro del mes siguiente a la aprobación de la especificación |
| D-11 | 6.1.5 Recepción técnica de la sala | 6.3.1 y 6.3.2 Racks R01 y R02 | FC | El acta de la sala habilita el montaje; 6.1.5 se firma después de 6.1.2 a 6.1.4 (Formulario T-15, Tabla 6.1) |
| D-12 | 6.3.1 a 6.3.3 Racks de Talca y gabinete de Concepción | 6.6 Configuración de los sitios | FC | El software de base se instala sobre el hardware montado. Los gabinetes de cross-docking (6.3.4) se montan junto con el equipamiento de campo de cada ola (6.5.1, CC) y no condicionan la configuración de los CD |
| D-13 | 6.6.3 Borde de los CD en servicio y validación inicial | H3 (mes 6); pruebas ampliadas antes de H5 | FC | Infraestructura híbrida del H3 (Formulario E-25) |
| D-14 | 3.1 Ambientes (H3) | Entrega y ejecución en QA de 3.4; no el inicio de desarrollo en DEV | FC | Los módulos se entregan en QA |
| D-15 | 3.3 Base compartida | 3.4 Módulos de la Etapa 1 | CC | La base compartida se construye primero (Capítulo 3, sección 3.4.3) |
| D-16 | 3.4.1 M1 Recepción y 3.4.2 M2 Inventario | 3.4.3 M5 Preparación y 3.4.4 M9 Calidad y trazabilidad | Por interfaz | Recepción e inventario alimentan preparación y retiro (Capítulo 3, sección 3.4.3). El sucesor construye después de que el predecesor fija sus contratos (actividad A02) e integra después de que el predecesor entrega en QA (A12) |
| D-17 | 3.4.2 M2 Inventario | 3.4.6 M3 Preventa | CC | La preventa necesita stock (Capítulo 3, sección 3.4.3) |
| D-18 | 3.4.3 M5 Preparación y 3.4.6 M3 Preventa | 3.4.7 M4 Rutas y 3.4.8 M6 Reparto | Por interfaz | Rutas y reparto requieren pedido confirmado y preparación (Capítulo 3, sección 3.4.3). El sucesor construye después de que el predecesor fija sus contratos (actividad A02) e integra después de que el predecesor entrega en QA (A12) |
| D-19 | 3.4.8 M6 Reparto | 3.4.10 M7 Cobranza y rendición | Por interfaz | La rendición requiere la entrega registrada (Capítulo 3, sección 3.4.3). El sucesor construye después de que el predecesor fija sus contratos (actividad A02) e integra después de que el predecesor entrega en QA (A12) |
| D-20 | 3.4 Módulos de la Etapa 1 | 3.8.1 Pruebas de integración (H4) | FC | Formulario E-25, H4 |
| D-21 | 3.8.1 Pruebas de integración | 3.8.2 Aceptación y 3.8.3 Operación sin conexión | FC | Bases Técnicas Transversales, numeral 20.1. Empiezan al terminar 3.8.1, en paralelo con la revisión del H4 por el CLIENTE |
| D-21b | 3.4 Módulos de la Etapa 1 entregados en QA | 3.8.4 Carga, 3.8.5 Recuperación, 3.8.6 Seguridad ofensiva y 3.8.8 Respaldo | FC | Pruebas no funcionales sobre la versión integrada en Preproducción; no dependen del resultado funcional de 3.8.1 |
| D-22 | 3.1.3 Ambiente de recuperación | 3.8.5 Prueba de recuperación ante desastres | FC | La prueba exige conmutación real |
| D-23 | 3.8.2 a 3.8.6 | 3.8.7 Certificación de la Etapa 1 (H5) | FC | Formulario E-25, H5 |
| D-24 | 3.7.1 a 3.7.4 Migración y ensayos | 3.7.5 Conciliación y corte | FC | Dos ensayos previos (numeral 20.1) |
| D-25 | 3.8.7 (H5), 3.7.5, 4.1.1 y 4.1.2 | 4.2.1 Marcha blanca de la Etapa 1 (H6) | FC | Formulario E-25, H6; RT-20.01 y RT-20.02 |
| D-26 | 6.5 Equipamiento de campo de cada ola | Ola correspondiente de 4.2.1 | FC | Equipamiento instalado antes de la ola |
| D-27 | 5.4.1 y 5.4.2 Acuerdos con transportistas y sindicato | Ola de reparto de 4.2.1 | FC | Capítulo 3, Anexo 3.I |
| D-28 | 4.2.1 y 7.3.1 Certificación de usuarios | 4.2.3 Paso a producción de la Etapa 1 (H7); luego 4.2.2 Estabilización (meses 16 a 20) | FC | Bases Administrativas, Art. 17.3 y 90.4. La estabilización 4.2.2 sigue al paso a producción y no lo condiciona |
| D-29 | 1.2.5 y 2.4.2 Línea base y diseño de la Etapa 2 (H8) | 3.5 Módulos de la Etapa 2 | FC | Formulario E-25, H8 |
| D-30 | 3.5 Módulos de la Etapa 2 | 3.9.1 Pruebas de integración (H9) | FC | Formulario E-25, H9 |
| D-31 | 3.9.1 a 3.9.5 | 3.9.6 Certificación de la Etapa 2 (H10) | FC | Formulario E-25, H10. Las pruebas 3.9.2 a 3.9.5 empiezan al terminar 3.9.1, en paralelo con la revisión del H9 |
| D-32 | 3.9.6 (H10), 3.6.5 y 4.1.3 | 4.3.1 Marcha blanca de la Etapa 2 (H11) | FC | Formulario E-25, H11 |
| D-33 | 4.3.1, 7.3.2, 7.1.4 y 4.3.4 | 4.3.3 Aceptación final (H12) | FC | Bases Administrativas, Art. 17.3 y 37.1 |
| D-34 | 4.3.3 Aceptación final (H12) | 8 Operación y 9.1 Cierre de la implementación | FC | Bases Administrativas, Art. 17.2, punto 4 |

Las dependencias D-02, D-04 y D-14 a D-25 forman la cadena que llega a la marcha blanca de la Etapa 1 y contienen la ruta crítica. Las dependencias D-07 a D-13 son las dos cadenas que convergen en el H3, y las D-29 a D-34 forman la secuencia de la Etapa 2.

## Anexo 7.C — Momento de los resultados de aceptación del caso

El Caso 02, capítulo 18, exige indicar en qué momento del cronograma se alcanza cada resultado y cómo se mide. La Tabla «tab:7C1» ubica en el cronograma las metas y métodos del Capítulo 3, Anexo 3.J.

**Momento de los dieciséis resultados de aceptación. Fuente: elaboración propia a partir del Caso 02, capítulo 18, y del Capítulo 3, Anexo 3.J.**

<a id="tab:7C1"></a>

| ID | Resultado | Meta | Momento | Paquetes |
| --- | --- | --- | --- | --- |
| R18-01 | Clientes afectados por lote en menos de 2 horas | Menos de 2 horas | Marcha blanca de la Etapa 1 (meses 13 a 15); se acepta en el H7 | 3.4.4 |
| R18-02 | Lote registrado en el 100 % de las recepciones que lo requieren | 100 % | Marcha blanca de la Etapa 1; H7 | 3.4.1 |
| R18-03 | Temperatura continua y auditable en cámaras y vehículos | 100 % con registro continuo | Marcha blanca de la Etapa 1; H7 | 3.4.4, 3.4.5, 6.5.3, 6.5.4 |
| R18-04 | OTIF medido de una sola forma | 90 % en el mes 15; 93 % en el mes 19; 95 % en el mes 32 | Medición diaria desde el mes 13; tramos en los meses 15, 19 y 32 | 3.4.11 |
| R18-05 | Stock y crédito visibles al tomar el pedido | 100 % de los pedidos | Marcha blanca de la Etapa 1; H7 | 3.4.6 |
| R18-06 | Ningún pedido perdido ni duplicado por falta de señal | 0 | Prueba de 14 horas antes del H5 y conciliación diaria en la marcha blanca de la Etapa 1 | 3.3.6, 3.8.3 |
| R18-07 | Ruta del día siguiente en menos de 20 minutos, corregible | Menos de 20 minutos | Marcha blanca de la Etapa 1; H7 | 3.4.7 |
| R18-08 | Prueba de entrega digital disponible el mismo día | 100 % | Marcha blanca de la Etapa 1; H7 | 3.4.8 |
| R18-09 | Cero guías extraviadas o ilegibles | 0 % | Marcha blanca de la Etapa 1; H7 | 3.3.2, 3.4.8 |
| R18-10 | Rendición cuadrada el mismo día | 100 % de diferencias con causal | Marcha blanca de la Etapa 1; H7 | 3.4.10 |
| R18-11 | Costo de servir por cliente y entrega | 100 % de las entregas | Marcha blanca de la Etapa 2 (meses 19 y 20); H12 | 3.5.4 |
| R18-12 | Pérdida anual de envases bajo la meta | Hasta 7 % del parque al año | Provisional al cierre de la marcha blanca de la Etapa 1 (H7); final tras 12 meses de operación | 3.4.9 |
| R18-13 | Pedidos de cadenas por vía electrónica y aviso de despacho | 100 % de las cadenas certificadas | Marcha blanca de la Etapa 2; cadenas certificadas antes del mes 21 | 3.5.1, 3.6.5, 3.6.6 |
| R18-14 | Ocupación mínima de cada camión y promedio superior | 60 % o más por salida; promedio sobre 68 % | Cuatro semanas de la ola de reparto en la marcha blanca de la Etapa 1 | 3.4.7 |
| R18-15 | Causa de cada faltante registrada al producirse | 100 % | Marcha blanca de la Etapa 1; H7 | 3.4.3 |
| R18-16 | El planificador puede jubilarse sin que la operación se resienta | OTIF sin caída respecto del período con el planificador | Dos semanas de planificación sin el planificador en la marcha blanca de la Etapa 1 | 1.2.2, 3.4.7 |

Los resultados R18-01 a R18-10 y R18-12/R18-14/R18-15/R18-16 tienen verificaciones en la marcha blanca de la Etapa 1 (14 resultados); R18-11 y R18-13 corresponden a E2. Uno de ellos, R18-06, se prueba además antes del H5, y R18-12 se acepta en esa marcha blanca solo de forma provisional. Por eso la certificación de usuarios y el volumen real de esa marcha blanca concentran el riesgo de aceptación del proyecto. Dos resultados se confirman en operación: el tramo de OTIF del mes 32 y la pérdida de envases tras 12 meses.

## Anexo 7.D — Innovaciones en la EDT y en el cronograma

Cada innovación declara sus paquetes de la EDT y sus meses del cronograma, como exige el Art. 29°, punto 4, de las Bases Administrativas. La Tabla «tab:7D1» los presenta con su código de innovación y sus meses.

**Paquetes y meses de las cinco innovaciones. Fuente: elaboración propia a partir del Formulario T-14.**

<a id="tab:7D1"></a>

| Innovación | Paquete de la cartera | Paquete de la EDT | Meses | Hito asociado |
| --- | --- | --- | --- | --- |
| 1 · Seguimiento de vencimiento posentrega en el local | INN-01.P1 | 3.10.1.1 | 7 a 9 | — |
|  | INN-01.P2 | 3.10.1.2 | 9 y 10 | H4 |
|  | INN-01.P3 | 3.10.1.3 | 9 y 10 | H4 |
|  | INN-01.P4 | 3.10.1.4 | 11 a 15 | H5 y marcha blanca E1 |
| 2 · Reproducción de incidentes de terreno | INN-02.P1 | 3.10.2.1 | 2 y 3 | — |
|  | INN-02.P2 | 3.10.2.2 | 3 a 5 | — |
|  | INN-02.P3 | 3.10.2.3 | 5 a 10 | H4 |
|  | INN-02.P4 | 3.10.2.4 y 8.3.1 | 11 a 15 (validación) y 21 a 56 (mantenimiento) | Marcha blanca E1 |
| 3 · Vida útil remanente por historia térmica del lote | INN-03.P1 | 3.10.3.1 | 3 a 5 | — |
|  | INN-03.P2 | 3.10.3.2 | 5 a 9 | — |
|  | INN-03.P3 | 3.10.3.3 | 9 y 10 | H4 |
|  | INN-03.P4 | 3.10.3.4 | 11 a 15 | H5 y marcha blanca E1 |
|  | INN-03.P5 | 8.3.2 | Cada seis meses, 21 a 56 | Operación |
| 4 · Tramo variable de la Operación ligado al costo de servir | INN-04.P1 | 5.4.3 | 17 a 20 | — |
|  | INN-04.P2 | 8.3.3 | 21 a 23 | — |
|  | INN-04.P3 | 8.3.4 | 24 a 56 | Hito mensual |
| 5 · Hoja de negocio del almacenero | INN-05.P1 | 3.10.4.1 | 13 y 14 | — |
|  | INN-05.P2 | 3.10.4.2 | 14 y 15 | — |
|  | INN-05.P3 | 3.10.4.3 | 15 a 17 | H9 |
|  | INN-05.P4 | 3.10.4.4 y 8.3.5 | 18 a 26 | H10 a H12 |
|  | INN-05.P5 | 8.3.6 | 24 a 27 | — |

Las innovaciones 1 a 3 concentran su construcción entre los meses 2 y 10 y se validan en la marcha blanca de la Etapa 1, por lo que su riesgo queda acotado antes del H7. La innovación 5 sigue el calendario de la Etapa 2 y se extiende a las rutas durante los primeros meses de operación, y la innovación 4 liquida desde el mes 24, después de su línea base y de tres liquidaciones en sombra.

## Anexo 7.E — Trazabilidad de módulos e interfaces a la EDT

La EDT contiene la arquitectura cuando cada módulo y cada interfaz del Capítulo 4 tienen al menos un paquete que los construye y prueba. La Tabla «tab:7E1» presenta esa correspondencia para los doce módulos, y la Tabla «tab:7E2», para las quince interfaces.

**Módulos de la solución y paquetes de la EDT. Fuente: elaboración propia a partir del Capítulo 3, Tabla 3.4, y del Formulario T-14.**

<a id="tab:7E1"></a>

| Módulo | Construcción | Pruebas | Etapa |
| --- | --- | --- | --- |
| M1 Recepción | 3.4.1 | 3.8.1 a 3.8.6 | 1 |
| M2 Inventario | 3.4.2 | 3.8.1 a 3.8.6 | 1 |
| M3 Preventa | 3.4.6 | 3.8.1 a 3.8.6 | 1 |
| M4 Rutas | 3.4.7 | 3.8.1 a 3.8.6 | 1 |
| M5 Preparación | 3.4.3 | 3.8.1 a 3.8.6 | 1 |
| M6 Reparto | 3.4.8 | 3.8.1 a 3.8.6 | 1 |
| M7 Cobranza y rendición | 3.4.10 | 3.8.1 a 3.8.6 | 1 |
| M8 Devoluciones y envases | 3.4.9 | 3.8.1 a 3.8.6 | 1 |
| M9 Calidad y trazabilidad | 3.4.4 | 3.8.1 a 3.8.6 | 1 |
| M10 Analítica | 3.4.11 (indicadores y OTIF) y 3.5.4 (costo de servir) | 3.8 y 3.9 | 1 y 2 |
| M11 Canal moderno | 3.5.1 | 3.9.1 a 3.9.5 | 2 |
| M12 Telemetría | 3.4.5 | 3.8.1 a 3.8.6 | 1 |

Once de los doce módulos se construyen en la cuenta 3.4 y se prueban en la 3.8; M10 Analítica es el único módulo con trabajo en ambas etapas, porque sus indicadores operacionales entran en la Etapa 1 y el costo de servir en la Etapa 2.

**Interfaces de la arquitectura y paquetes de la EDT. Fuente: elaboración propia a partir del Capítulo 4, Anexos 4.1-G y 4.1-H, y del Formulario T-14.**

<a id="tab:7E2"></a>

| Interfaz | Propósito | Paquetes |
| --- | --- | --- |
| INT-01 | Pedido de preventa y consulta | 3.4.6, 3.3.6 |
| INT-02 | Entrega, prueba de entrega y cobro | 3.4.8, 3.4.9, 3.4.10, 3.3.6 |
| INT-03 | Eventos de bodega a la nube | 3.4.2, 3.4.3, 3.3.6 |
| INT-04 | Detalle de cross-docking a Talca | 3.4.2, 6.3.4 |
| INT-05 | Eventos de temperatura | 3.4.4, 3.4.5, 6.5.3 |
| INT-06 | ERP de 2017 | 3.3.2 |
| INT-07 | Emisor de documentos tributarios del ERP | 3.3.2 |
| INT-08 | Cadenas del canal moderno | 3.6.5, 3.6.6 |
| INT-09 | Pasarela de pago | 3.6.2 |
| INT-10 | Mapas y geocodificación | 3.6.3 |
| INT-11 | Avisos al cliente | 3.6.4 |
| INT-12 | Réplica de cambios de datos del WMS | 3.3.3 |
| INT-13 | Identidad en el sitio | 3.3.1 |
| INT-14 | Métricas y trazas | 3.1.5 |
| INT-15 | Telemetría existente de la flota | 3.3.4 |

Las quince interfaces tienen un paquete que las construye, y las interfaces internas (INT-01 a INT-05 e INT-12 a INT-14) dependen de la base compartida o de los módulos que las usan. Además de estas interfaces, el paquete 3.6.1 construye el intercambio de lote y trazabilidad con los proveedores.

## Anexo 7.F — Supuestos y dependencias para preparar SD8

Esta matriz es entrada de planificación al SD8; no reemplaza T-16, una RBS ni la evaluación cuantitativa de riesgos. No se inventan probabilidades ni importes. Los códigos P7 sirven para trazabilidad interna y no renumeran T-12.

| ID | Riesgo / supuesto | EDT / hitos | Responsable de tratamiento | Disparador o control | Estado de preparación |
| --- | --- | --- | --- | --- | --- |
| P7-01 | Productividad y tamaños HH por clase no medidos | Los 222 paquetes; T-15 §4 | JP y líderes de frente | Sustituir tamaños por estimación de equipo trazable a T-12, cantidades y ensayos; recalcular si demanda supera capacidad | Modelo cuantificado, validación pendiente |
| P7-02 | Cronograma por actividad depende de tamaños y equipos supuestos | D-01–D-34; H2/H3/H4/H5/H9/H10 | JP/ARQ | T-15 §5–§6 programa 564 actividades con dependencias, revisión Art. 18.3 y nivelación; reservas de 3 a 35 días hábiles por hito. Reestimar con el equipo y repetir el cálculo; una reserva consumida a la mitad activa replanificación | Cronograma por actividad calculado; validación del equipo pendiente |
| P7-03 | Solapamientos compiten por especialistas | 4.2.1/4.2.2, 3.5, 4.3.1; meses 13–15/19–20 | Líder DES y CAL | Mantener 256 HH DES + 128 HH CAL/mes protegidas E1, sin préstamo a F4; asignar personas nominales | Capacidad modelada; contratación/turnos no acreditados |
| P7-04 | Fecha efectiva cambia congelamientos | 1.1.3, 4.1; V-12/H6/H11/H7/H12 | JP/CLIENTE | Confirmar fecha y transformar meses relativos en calendario; no iniciar corte en fechas prohibidas | Escenario febrero 2027, no fecha confirmada |
| P7-05 | Ola/cadena no lista antes de cuatro semanas de cierre | 4.2.1/4.3.1, 7.3, 3.6.5/6 | IMP/Comercial/Operaciones | Registro de todo el alcance, activación antes del tramo final, cero incidentes críticos/altos; no reemplazar alcance por muestra | Secuencia propuesta y aceptación definida |
| P7-06 | Reversión manual no soporta despacho o falla DTE | 4.1.2/3.3.2; H6/H11 | Operaciones/ARQ/SRE | Ensayo de 96 despachos, objetivo total 40 minutos, final antes de 05:30; contingencia ERP aprobada | Objetivo cuantificado; tiempo/volumen no medidos |
| P7-07 | Retiro temprano de acompañamiento o capacidad de mesa insuficiente | 4.2.2/4.3.2/8.1.1/8.1.2/8.1.5 | IMP/SRE | Decremento sólo con acta e indicadores sostenidos; mesa con las posiciones del SD4 y SOC 24×7 en T-15; medir abandono y resolución al primer contacto y calibrar Erlang A (T-15 §5.6) | Cobertura reconciliada con SD4; SLA no medidos |
| P7-08 | Compra/sala/borde incumple H3 | 5.1.2/6.1/6.3/6.6.3 | SRE/CLIENTE | Recepción de sala antes de racks y configuración; H3 exige borde mes 6, no mes 12 | Restricción corregida; fecha de compra pendiente |
| P7-09 | Reserva de stock/custodia duplica o confirma sin acuse | 3.3.6/3.4.2/3.4.6/3.8.1/3.8.3 | ARQ/DES/CAL | CD-05; AL-STOCK-01/AL-ACT-01 con concurrencia/corte/reintento; acuse durable y autoridad por época | Incluido en pruebas, no ejecutado |
| P7-10 | Tráfico adicional o recuperación excede diseño | 3.8.4/3.9.3; SD4 física/DR | ARQ/SRE | Verificar 4L de A31/A32 frente a 2N + 2L y retenciones múltiples; medir carga/drenaje y límite residual DR/RPO | Dependencia de arquitectura preservada |
| P7-11 | Control de conservación del precio pactado | 1.2.1/3.4.6; SD2 S-09, RF-03.11/12 y SD3 RNG-08 | Comercial/JP | Probar cambio de lista entre pedido y despacho y detectar diferencias ERP | Política documental alineada; prueba funcional exigida |
| P7-12 | Revisión humana y evidencia formal no disponibles | 1.5/1.8, A-6, todos los hitos | JP/CAL | Registrar quién revisó, qué verificó y cuándo; comprobar PDF final en su flujo correspondiente | No se acredita aprobación humana ni formal |

### Política de reservas que recibe SD8

El modelo protege 3.072 HH para correcciones E1 meses 13–20, además del trabajo base y cobertura. T-15 §5 deja reserva de calendario cero antes de H4/H5/H9/H10. La holgura local de convergencia no se suma como reserva adicional. Las últimas cuatro semanas de marcha blanca no son reserva. La reserva de gestión monetaria no está determinada: requiere escenarios de costo y autoridad de uso en el documento competente; SD7 no contiene precios.

### Condición para comenzar y condición para entregar

Puede comenzar la identificación, RBS, evaluación y respuesta de riesgos del SD8 usando los paquetes, supuestos y controles anteriores. Para entregar una oferta cerrada se requieren estimación validada, red detallada, personas y turnos asignados, fecha efectiva, conformidad de decisiones con el CLIENTE y evidencias de ensayo. La preparación no equivale a declarar cumplidas estas condiciones.

## Referencias

Bases Administrativas, Art. 17°/18° y Formularios T-14/T-15/T-18; Bases Técnicas Transversales, RT-20.02/05/06; Caso 02, §13.3/§17.6; Aclaraciones, Capítulos 7/8; SD3 §3.4.4; SD4 y anexos lógicos; SD6 §6.1/§6.2; formularios del SD7.

## Declaración de uso de IA

Se conserva la declaración histórica del cuerpo SD7. Codex apoyó la coherencia documental y la construcción del modelo de planificación y de este anexo el 6 de octubre de 2026 (nivel alto en texto; figuras sólo como descripción textual). Revisión humana no documentada. Los controles de consistencia no sustituyen la aprobación del equipo ni se atribuyen como revisión humana.

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
| --- | --- | --- | --- | --- | --- |
| Anexos 7.A a 7.E | Claude Code | Listados y cálculo del calendario | Alto | Ninguno | No documentada |
| Anexo 7.B y 7.F (7 de octubre de 2026) | Claude Code | Dependencias D-05/D-06/D-09–D-11/D-28 y supuestos P7-02/P7-07 | Alto | Ninguno | No documentada |
