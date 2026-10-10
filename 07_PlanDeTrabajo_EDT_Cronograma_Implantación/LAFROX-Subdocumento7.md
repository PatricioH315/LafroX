# 7 Introducción al Plan de trabajo

Este capítulo presenta cómo LafroX ejecutará el proyecto de Distribuidora Puelche dentro del cronograma contractual obligatorio de 56 meses (Bases Administrativas, Art. 17°): qué trabajo se hace, en qué orden, con qué esfuerzo y cómo la solución entra en operación sin detener la venta, la bodega ni el reparto.

La sección 7.1 descompone el 100 % del alcance en una estructura de descomposición del trabajo (EDT) con paquetes estimables y asignables. La sección 7.2 secuencia ese trabajo y lo organiza en frentes paralelos, con especial atención a los meses 13 a 15 y 19 a 20, en que dos esfuerzos coexisten. La sección 7.3 presenta la ruta crítica, la carta Gantt con los hitos del Formulario E-25 y el plan de implantación y de marcha blanca de cada etapa.

El capítulo se apoya en otros tres capítulos de la oferta: el Capítulo 3 fija el alcance de cada etapa y los criterios de olas y estabilización; T-18 §6 concreta una propuesta de calendario, dotación y decisiones; el Capítulo 4 define los módulos M1 a M12 y las interfaces que la EDT construye; y el Capítulo 6 establece el proceso de desarrollo cuyas fases organizan la EDT y la gestión del proyecto que la controla. El detalle va en tres formularios y un archivo de anexos: el Formulario T-14 contiene la EDT completa, su diccionario y la carta Gantt; el Formulario T-15, el método de estimación y programación, la ruta crítica y los frentes de trabajo; el Formulario T-18, la implantación y la puesta en marcha controlada; y los Anexos 7.A a 7.F, los listados de apoyo y la preparación de riesgos.

## 7.1 EDT

La EDT es la base común del plan: el cronograma, la estimación y la asignación de responsables se construyen sobre sus paquetes, y su diccionario fija qué se entrega y cómo se acepta cada uno. Esta sección explica cómo se descompuso el trabajo, cómo queda la estructura, cómo cubre el alcance y cómo se asignan los responsables.

### 7.1.1 Criterio de descomposición

La EDT de Puelche se organiza en nueve fases. Las cuatro primeras son las fases del proceso de desarrollo del Capítulo 6 (Inicio, Elaboración, Construcción y Transición) y se recorren una vez por cada etapa del Art. 17°. El primer recorrido produce la Etapa 1, con la trazabilidad de recepción, la bodega, la cadena de frío, la preventa, las rutas, el reparto y la rendición, y termina con el paso a producción del mes 16. El segundo produce la Etapa 2, con el canal moderno, los portales y el costo de servir, y termina con el paso a producción del mes 21.

Las otras cinco fases agrupan el trabajo que no es desarrollo de software, pero sin el cual la solución no entra en operación: adquisiciones y contrataciones; infraestructura física y sitios; capacitación y gestión del cambio; operación y soporte durante 36 meses; y cierre.

La descomposición sigue la regla del 100 %: la suma del trabajo de los niveles inferiores reproduce el trabajo del nivel superior, sin omitir ni agregar alcance (Project Management Institute [PMI], 2017, p. 161). El segundo nivel son 49 cuentas de control, puntos de gestión donde se integran el alcance, el cronograma y el esfuerzo para medir el desempeño. El nivel inferior son 222 paquetes de trabajo, cada uno con un entregable verificable, un criterio de aceptación y un único responsable (PMI, 2017, pp. 161–162). En la cuenta de las innovaciones, cada innovación agrupa sus paquetes en un cuarto nivel.

El último nivel de la EDT es el paquete de trabajo, con su entregable, su responsable y su criterio de aceptación. Fuera de la EDT, cada paquete se descompone en actividades que cumplen la regla del 8/80, entre 8 y 80 horas hombre de esfuerzo, y la regla del período de reporte: ninguna actividad dura más de una quincena, el período con que informa el Comité de Proyecto (PMI, 2017, pp. 183–185). Los paquetes de producto se dividen con una plantilla por clase; por ejemplo, un módulo de 960 HH se divide en 12 actividades de 80 HH, desde el análisis de sus requerimientos hasta su entrega en QA. Los 163 paquetes con entregable se programan con fecha, personas y predecesoras; sus actividades se detallan hasta el H2 y, después, por planificación gradual antes de cada fase, cuando el equipo conoce el trabajo (PMI, 2017, p. 185). Así el cronograma no fija hoy el día de una actividad que ocurrirá en 2028, y cada fase se planifica como las iteraciones del proceso RUP del Capítulo 6. El Formulario T-15, Figura T15.3, muestra los puntos de replanificación (antes del H2, el H4, el H8 y el H9). Los 59 paquetes de esfuerzo continuo, como la cobertura del NOC, las reuniones periódicas o la mentoría posterior al H12, no se descomponen en actividades distintas: se programan por quincena u ocurrencia, en relevos de hasta 64 HH cada uno. La lista de actividades y las reglas de programación están en el Formulario T-15, sección 6.

Los paquetes de la fase de Operación son paquetes de esfuerzo continuo. Cada uno cubre un servicio durante los 36 meses y se controla con entregables periódicos, como los informes mensuales de servicio, los informes de pruebas y las actualizaciones anuales, que funcionan como sus puntos de verificación.

La Tabla 7.1 muestra el tamaño de cada fase y los hitos que produce.

<a id="tab:7-fases"></a>
**Tabla 7.1.** Cuentas de control y paquetes por fase. Fuente: elaboración propia a partir del Formulario T-14 y del Formulario E-25.

| Fase | CC | PT | Etapa | Hitos |
| --- | --- | --- | --- | --- |
| 1 Inicio | 9 | 35 | E1 y E2 | H1, H8 |
| 2 Elaboración | 6 | 18 | E1 y E2 | H2, H8 |
| 3 Construcción | 11 | 79 | E1 y E2 | H3, H4, H5, H9, H10 |
| 4 Transición | 3 | 10 | E1 y E2 | H6, H7, H11, H12 |
| 5 Adquisiciones y contrataciones | 4 | 13 | E1 y E2 | Habilita H3 |
| 6 Infraestructura física y sitios | 6 | 24 | E1 | Habilita H3 y H6 |
| 7 Capacitación y gestión del cambio | 3 | 13 | E1, E2 y Operación | Condición de H7 y H12 |
| 8 Operación y soporte (36 meses) | 5 | 26 | Operación | Hito mensual |
| 9 Cierre | 2 | 4 | Meses 21 y 56 | Después de H12 |
| **Total** | **49** | **222** |  |  |

La construcción concentra el 36 % de los paquetes (79 de 222), porque contiene los quince desarrollos de módulos, las integraciones, la migración, las pruebas de ambas etapas y las innovaciones. Las fases 5 a 7, que no producen software, suman 50 paquetes (23 %). Ese peso muestra que, en Puelche, la compra y la instalación del equipamiento de cinco sitios, los acuerdos con diez transportistas y con el sindicato y la capacitación de una operación que no puede detenerse son trabajo planificado y controlado, no supuestos.

La Figura 7.1 resume el primer nivel de la EDT: la raíz del proyecto y sus nueve fases.

<a id="fig:7-edt"></a>
![Figura 7.1: Vista del primer nivel de la EDT: raíz del proyecto y sus nueve fases. Fuente: elaboración propia a partir del Formulario T-14.](<imagenes/Imagenes de la edt/EDT nivel 2.drawio.png>)

**Figura 7.1.** Vista del primer nivel de la EDT: raíz del proyecto y sus nueve fases. Fuente: elaboración propia a partir del Formulario T-14.

Las fases de desarrollo (1 a 4) se recorren una vez por etapa; las fases 5 a 7 las habilitan en paralelo, y las fases 8 y 9 cubren la operación y el cierre. La figura muestra la estructura, no la secuencia temporal: el número de una fase no indica cuándo ocurre; sus fechas están en la carta Gantt de la sección 7.3.2.

### 7.1.2 Estructura general

Las láminas siguientes desglosan las cuentas de control y los paquetes por fase. Cada imagen se presenta inmediatamente después de su descripción; las divisiones «1 de 2», «2 de 2» y «1 de 3» identifican continuaciones de una misma fase.

#### 7.1.2.1 Fase 1. Inicio

La fase de Inicio define el proyecto, fija su alcance y planificación y establece cómo se gobierna y controla. Sus cuentas 1.1 a 1.5 abarcan el acta, la línea base, la planificación, los interesados y la calidad.

<a id="fig:7-edt-fase-1a"></a>
![Figura 7.2: Fase 1 — Inicio, primera parte: cuentas 1.1 a 1.5. Fuente: elaboración propia a partir del Formulario T-14.](<imagenes/Imagenes de la edt/EDT-Fase 1 (1 de 2).drawio.png>)

**Figura 7.2.** Fase 1 — Inicio, primera parte: cuentas 1.1 a 1.5. Fuente: elaboración propia a partir del Formulario T-14.

La segunda lámina completa Inicio con gestión de riesgos, reversibilidad, gobierno, control y cumplimiento normativo. Incluye los paquetes 1.2.2 y 1.2.3, que capturan las reglas de ruteo cuya fuente experta se jubila y las interfaces del sistema de gestión que el CLIENTE reconoce no tener documentadas; también incluye los comités del Art. 71°, el informe de valor ganado y el tablero (RT-19.06 a RT-19.09).

<a id="fig:7-edt-fase-1b"></a>
![Figura 7.3: Fase 1 — Inicio, segunda parte: cuentas 1.6 a 1.9, desde riesgos hasta cumplimiento contractual.](<imagenes/Imagenes de la edt/EDT-Fase 1 (2 de 2).drawio.png>)

**Figura 7.3.** Fase 1 — Inicio, segunda parte: cuentas 1.6 a 1.9, desde riesgos hasta cumplimiento contractual.

#### 7.1.2.2 Fase 2. Elaboración

Elaboración diseña la solución antes de programar: arquitectura lógica y física, datos trazables por lote, seguridad, sala técnica de Talca, continuidad y experiencia de usuario. La aprobación de arquitectura, seguridad y modelo de datos corresponde al H2 del mes 4. La primera lámina muestra las cuentas 2.1 a 2.3.

<a id="fig:7-edt-fase-2a"></a>
![Figura 7.4: Fase 2 — Elaboración, primera parte: arquitectura, seguridad y sala técnica, cuentas 2.1 a 2.3.](<imagenes/Imagenes de la edt/EDT-Fase 2 (1 de 2).drawio.png>)

**Figura 7.4.** Fase 2 — Elaboración, primera parte: arquitectura, seguridad y sala técnica, cuentas 2.1 a 2.3.

La continuación cubre la validación de diseños, continuidad del negocio y experiencia de usuario (cuentas 2.4 a 2.6), incluidos los procedimientos manuales y la recuperación ante desastres.

<a id="fig:7-edt-fase-2b"></a>
![Figura 7.5: Fase 2 — Elaboración, segunda parte: validación, continuidad y experiencia de usuario, cuentas 2.4 a 2.6.](<imagenes/Imagenes de la edt/EDT-Fase 2 (2 de 2).drawio.png>)

**Figura 7.5.** Fase 2 — Elaboración, segunda parte: validación, continuidad y experiencia de usuario, cuentas 2.4 a 2.6.

#### 7.1.2.3 Fase 3. Construcción

Construcción produce los ambientes y servicios de nube, la base compartida, los módulos de ambas etapas, las integraciones, la migración, las pruebas, las innovaciones y la documentación. La primera lámina reúne ambientes, nube, base compartida y módulos de la Etapa 1 (cuentas 3.1 a 3.4).

<a id="fig:7-edt-fase-3a"></a>
![Figura 7.6: Fase 3 — Construcción, primera parte: ambientes, nube, base compartida y módulos de la Etapa 1, cuentas 3.1 a 3.4.](<imagenes/Imagenes de la edt/EDT-Fase 3 (1 de 3).drawio.png>)

**Figura 7.6.** Fase 3 — Construcción, primera parte: ambientes, nube, base compartida y módulos de la Etapa 1, cuentas 3.1 a 3.4.

La segunda lámina presenta los módulos de la Etapa 2, las integraciones externas, la migración y las pruebas de la Etapa 1 (cuentas 3.5 a 3.8). La integración con el ERP conserva su función de emisor único de la guía de despacho.

<a id="fig:7-edt-fase-3b"></a>
![Figura 7.7: Fase 3 — Construcción, segunda parte: módulos de la Etapa 2, integraciones, migración y pruebas de la Etapa 1, cuentas 3.5 a 3.8.](<imagenes/Imagenes de la edt/EDT-Fase 3 (2 de 3).drawio.png>)

**Figura 7.7.** Fase 3 — Construcción, segunda parte: módulos de la Etapa 2, integraciones, migración y pruebas de la Etapa 1, cuentas 3.5 a 3.8.

La tercera lámina cierra Construcción con las pruebas de la Etapa 2, las innovaciones y la documentación técnica (cuentas 3.9 a 3.11). Por su formato vertical, se presenta rotada en una página propia para facilitar su consulta y ampliación digital.

<a id="fig:7-edt-fase-3c"></a>
![Figura 7.8: Fase 3 — Construcción, tercera parte: pruebas de la Etapa 2, innovaciones y documentación técnica, cuentas 3.9 a 3.11.](<imagenes/Imagenes de la edt/EDT-Fase 3 (3 de 3).drawio.png>)

**Figura 7.8.** Fase 3 — Construcción, tercera parte: pruebas de la Etapa 2, innovaciones y documentación técnica, cuentas 3.9 a 3.11.

#### 7.1.2.4 Fase 4. Transición

Transición convierte la solución probada en el registro oficial. Su plan contempla las olas y la reversión; luego coordina las marchas blancas, la estabilización y las actas de aceptación de ambas etapas (H7 y H12).

<a id="fig:7-edt-fase-4"></a>
![Figura 7.9: Fase 4 — Transición: plan de implantación y marchas blancas de las etapas 1 y 2, cuentas 4.1 a 4.3.](<imagenes/Imagenes de la edt/EDT-Fase 4.drawio.png>)

**Figura 7.9.** Fase 4 — Transición: plan de implantación y marchas blancas de las etapas 1 y 2, cuentas 4.1 a 4.3.

#### 7.1.2.5 Fase 5. Adquisiciones y contrataciones

Esta fase separa lo que compra el CLIENTE de lo que contrata LafroX: el CLIENTE compra hardware de terreno y de sala, que LafroX especifica y recibe; LafroX contrata nube, enlaces y licencias. También formaliza los acuerdos con transportistas y sindicato y la fórmula contractual de la innovación 4.

<a id="fig:7-edt-fase-5"></a>
![Figura 7.10: Fase 5 — Adquisiciones y contrataciones: hardware, servicios, enlaces y acuerdos con terceros, cuentas 5.1 a 5.4.](<imagenes/Imagenes de la edt/EDT-Fase 5.drawio.png>)

**Figura 7.10.** Fase 5 — Adquisiciones y contrataciones: hardware, servicios, enlaces y acuerdos con terceros, cuentas 5.1 a 5.4.

#### 7.1.2.6 Fase 6. Infraestructura física y sitios

La fase instala la sala técnica de Talca, con energía, climatización y extinción; el cableado, los racks y gabinetes de borde; y la infraestructura de los sitios. La primera lámina cubre la sala, el cableado y el montaje de racks (cuentas 6.1 a 6.3).

<a id="fig:7-edt-fase-6a"></a>
![Figura 7.11: Fase 6 — Infraestructura física y sitios, primera parte: sala técnica, cableado y racks, cuentas 6.1 a 6.3.](<imagenes/Imagenes de la edt/EDT-Fase 6 (1 de 2).drawio.png>)

**Figura 7.11.** Fase 6 — Infraestructura física y sitios, primera parte: sala técnica, cableado y racks, cuentas 6.1 a 6.3.

La segunda lámina incluye seguridad física, equipamiento de campo y configuración de la infraestructura distribuida en los sitios (cuentas 6.4 a 6.6), incluidos los termógrafos de los camiones con frío y la prueba de autonomía de 24 horas.

<a id="fig:7-edt-fase-6b"></a>
![Figura 7.12: Fase 6 — Infraestructura física y sitios, segunda parte: seguridad física, equipamiento de campo y configuración, cuentas 6.4 a 6.6.](<imagenes/Imagenes de la edt/EDT-Fase 6 (2 de 2).drawio.png>)

**Figura 7.12.** Fase 6 — Infraestructura física y sitios, segunda parte: seguridad física, equipamiento de campo y configuración, cuentas 6.4 a 6.6.

#### 7.1.2.7 Fase 7. Capacitación y gestión del cambio

La fase atiende la rotación del 38 % en preparación con capacitación continua del turno de noche; acompaña individualmente al personal con veinte o treinta años en la compañía; incorpora a los conductores externos en el andén; y transfiere conocimiento al equipo de TI del CLIENTE. La certificación de usuarios (cuenta 7.3) es una de las condiciones de cierre de cada marcha blanca.

<a id="fig:7-edt-fase-7"></a>
![Figura 7.13: Fase 7 — Capacitación y gestión del cambio: capacitación por roles, acompañamiento y certificaciones, cuentas 7.1 a 7.3.](<imagenes/Imagenes de la edt/EDT-Fase 7.drawio.png>)

**Figura 7.13.** Fase 7 — Capacitación y gestión del cambio: capacitación por roles, acompañamiento y certificaciones, cuentas 7.1 a 7.3.

#### 7.1.2.8 Fase 8. Operación y soporte

La fase presta servicios durante los meses 21 a 56: centro de operaciones, gestión de incidentes, continuidad, mantenimiento, innovaciones, informes y transferencia al equipo del CLIENTE.

<a id="fig:7-edt-fase-8"></a>
![Figura 7.14: Fase 8 — Operación y soporte durante 36 meses: servicios, mantenimiento, innovaciones, informes y transferencia, cuentas 8.1 a 8.5.](<imagenes/Imagenes de la edt/EDT-Fase 8.drawio.png>)

**Figura 7.14.** Fase 8 — Operación y soporte durante 36 meses: servicios, mantenimiento, innovaciones, informes y transferencia, cuentas 8.1 a 8.5.

#### 7.1.2.9 Fase 9. Cierre

Cierre comprende dos momentos: completar la implementación en el mes 21, con entrega de código, infraestructura como código y lecciones aprendidas; y ejecutar la salida al término del contrato, con el Plan de Reversibilidad y el tratamiento final de los datos.

<a id="fig:7-edt-fase-9"></a>
![Figura 7.15: Fase 9 — Cierre: cierre de implementación y salida al término del contrato, cuentas 9.1 y 9.2.](<imagenes/Imagenes de la edt/EDT-Fase 9.drawio.png>)

**Figura 7.15.** Fase 9 — Cierre: cierre de implementación y salida al término del contrato, cuentas 9.1 y 9.2.

### 7.1.3 Cobertura del alcance

Las Aclaraciones de la licitación exigen que la EDT contenga explícitamente las innovaciones y las actividades de seguridad, calidad, migración e implantación (sección 11, Capítulo 7), y el Caso 02 exige que contenga la arquitectura (capítulo 19). La Tabla 7.2 comprueba que cada uno de esos componentes tiene paquetes propios.

<a id="tab:7-cobertura"></a>
**Tabla 7.2.** Cobertura del alcance en la EDT. Fuente: elaboración propia a partir del Formulario T-14, del Capítulo 4 y de las Aclaraciones.

| Componente | Elementos | PT | Cuentas de control | Exigencia |
| --- | --- | --- | --- | --- |
| Módulos | M1–M12 y los portales de clientes y de transportistas; el portal de proveedores se construye con M11 Canal moderno (3.5.1) | 15 | 3.4, 3.5 | Caso 02, cap. 19 |
| Interfaces | INT-01 a INT-15 | 21 | 3.1, 3.3, 3.4, 3.6, 6.3, 6.5 | Caso 02, cap. 19 |
| Innovaciones | INN-01 a INN-05 | 23 | 3.10, 5.4, 8.3 | Aclaraciones; BA, Art. 29° |
| Seguridad | Diseño, construcción, pruebas y operación | 17 | 1.9, 2.2, 3.2, 3.3, 3.8, 3.9, 3.11, 6.4, 8.1, 8.2 | Aclaraciones |
| Calidad | Planes, puertas, pruebas y deuda técnica | 19 | 1.5, 3.8, 3.9, 3.11, 8.2 | Aclaraciones |
| Migración | Perfilamiento, carga, ensayos y conciliación | 6 | 3.3, 3.7 | Aclaraciones; BTT, numeral 20.1 |
| Implantación | Olas, marchas blancas, capacitación y cambio | 23 | 4.1 a 4.3, 7.1 a 7.3 | Aclaraciones; RT-20.01 a 20.08 |

La tabla muestra que ninguna exigencia descansa en un paquete genérico. La seguridad, por ejemplo, aparece en las cinco fases donde ocurre: el diseño de la Elaboración, la identidad y las pruebas de seguridad ofensiva de la Construcción, la seguridad física de la sala y el centro de operaciones de seguridad durante la Operación. Las pruebas de seguridad ofensiva 3.8.6 y 3.9.5 se cuentan en la fila de seguridad y en la de calidad, porque son a la vez control de seguridad y prueba de certificación. Las pruebas de la Etapa 2 repiten las de la Etapa 1 con una exigencia adicional: demostrar que la Etapa 1 en producción no se degrada.

La Figura 7.16 ubica esos paquetes por fase y muestra en qué parte de la EDT y, por lo tanto, del cronograma quedan las actividades de cada categoría.

<a id="fig:7-cobertura"></a>
![Figura 7.16: Ubicación en la EDT de las innovaciones y de la seguridad, la calidad, la migración y la implantación. Fuente: elaboración propia a partir del Formulario T-14 y de las Aclaraciones, sección 11.](<imagenes/Diagramas que faltaban/Fig_7-4_Cobertura_EDT.drawio.png>)

**Figura 7.16.** Ubicación en la EDT de las innovaciones y de la seguridad, la calidad, la migración y la implantación. Fuente: elaboración propia a partir del Formulario T-14 y de las Aclaraciones, sección 11.

La matriz confirma que las cinco categorías se distribuyen desde el diseño hasta la operación. Las innovaciones tienen paquetes en las fases donde se construyen, se contratan y se operan: INN-01, INN-02, INN-03 e INN-05 se construyen en la cuenta 3.10; la fórmula contractual de INN-04 se aprueba en la cuenta 5.4, porque es una innovación de modelo de contratación y no tiene paquete de construcción; e INN-02 a INN-05 tienen su parte de operación en la cuenta 8.3. Cada innovación tiene sus meses en el Anexo 7.D (Bases Administrativas, Art. 29°, punto 4).

Los anexos completan la cobertura. El Anexo 7.E relaciona los doce módulos y las quince interfaces del Capítulo 4 con el paquete que los construye y prueba, y el Anexo 7.C ubica los dieciséis resultados de aceptación del caso en su paquete y su momento. Los requerimientos del Formulario T-12 se trazan a los paquetes mediante la matriz de trazabilidad del paquete 1.2.4, que se aprueba con el H1.

### 7.1.4 Diccionario y asignación de responsables

El diccionario de la EDT, en el Formulario T-14, describe cada paquete con su entregable, su criterio de aceptación, su responsable y el período del cronograma en que se ejecuta, junto con el hito del Formulario E-25 que habilita. Todo entregable se recibe con el acta de la Contraparte Técnica, acompañada de su evidencia de verificación, su trazabilidad hacia los requerimientos y las observaciones resueltas (Bases Administrativas, Art. 18.1 y 18.2). Los criterios del diccionario se suman a esa regla común. Por ejemplo, el paquete 3.4.1 (M1 Recepción) se acepta solo si ningún producto con trazabilidad obligatoria se recibe sin lote, y el 4.1.2 (reversión de la Etapa 1) se acepta solo si su ensayo termina antes de las 05:30, sostiene 96 despachos sin interrupción con DTE válidos del ERP y no pierde ni duplica registros.

Los responsables son los ocho roles de la estructura para el proyecto del Capítulo 1, sección 1.5. La Tabla 7.3 muestra cómo se reparten los paquetes.

<a id="tab:7-responsables"></a>
**Tabla 7.3.** Paquetes por responsable. Fuente: elaboración propia a partir del Formulario T-14.

| Rol | PT | % | Fases con más paquetes |
| --- | --- | --- | --- |
| Líder de Operación / SRE | 58 | 26 % | 6 (21), 3 (13), 8 (12) |
| Líder de Implantación y Gestión del Cambio | 34 | 15 % | 7 (13), 4 (7) |
| Jefe de Proyecto | 33 | 15 % | 1 (22) |
| Líder de Desarrollo | 24 | 11 % | 3 (21) |
| Líder de Calidad | 19 | 9 % | 3 (15) |
| Arquitecto de Solución | 18 | 8 % | 2 (5), 3 (6) |
| Encargado de Seguridad de la Información | 18 | 8 % | 1 (4), 2 (4), 3 (4) |
| Líder de Datos | 18 | 8 % | 3 (16) |
| **Total** | **222** | **100 %** |  |

Todos los paquetes tienen un responsable único, de modo que son asignables. La distribución sigue la naturaleza del trabajo: el Jefe de Proyecto concentra la gestión y el gobierno; el Líder de Desarrollo, la construcción; y el Líder de Implantación, la capacitación y la transición. El Líder de Operación / SRE responde por un cuarto de los paquetes, porque reúne la nube, la infraestructura de los cinco sitios y la operación, y sus paquetes de las fases 3 y 6 ocurren a la vez. Responder por un paquete no significa ejecutarlo en persona: la sección 7.2.3 y el Formulario T-15 muestran qué frente ejecuta el trabajo bajo cada rol.

## 7.2 Plan de trabajo

El plan de trabajo aplica las metodologías del Capítulo 6. La gestión del proyecto se basa en el PMBOK: los alcances aprobados (H1 y H8) y el cronograma son las líneas base contra las que se mide el avance; el avance se mide con valor ganado en el informe mensual (RT-19.06 y RT-19.07); y todo cambio de alcance, plazo o criterio de aceptación se aprueba antes de incorporarse al plan, conforme al Art. 72° (paquete 1.4.3).

El desarrollo sigue las cuatro fases del proceso iterativo del Capítulo 6, que la EDT recorre una vez por etapa. Dentro de la Construcción, cada módulo avanza por iteraciones que producen resultados verificables, mientras que la marcha blanca y la aceptación formal ocurren solo en los meses que fija el Art. 17°. El tablero de flujo del equipo coordina las tareas diarias, pero no reemplaza el cronograma ni la aceptación formal de los entregables, como establece la metodología de gestión de proyectos del Capítulo 6.

### 7.2.1 Secuenciamiento y dependencias

El orden del trabajo sigue las dependencias de datos y de infraestructura de Puelche (Capítulo 3, sección 3.4.3). Primero se aprueban el alcance (H1, mes 2) y el diseño (H2, mes 4). En paralelo, se especifica y compra el equipamiento de la sala y de los sitios, y se contratan la nube y los enlaces, de modo que la infraestructura híbrida y los ambientes queden habilitados en el H3 del mes 6.

La construcción de la Etapa 1 parte por la base compartida, porque si falla, fallan todos los módulos. Sigue con recepción e inventario, que alimentan la preparación y el retiro sanitario, mientras la preventa avanza en paralelo porque necesita stock y crédito. Las rutas y el reparto se integran cuando existen el pedido confirmado y la preparación, y la rendición, cuando existe la entrega registrada. La Etapa 2 se diseña en los meses 13 y 14 (H8), reutiliza los pedidos, las guías y las evidencias ya probadas, y calcula el costo de servir con los hechos acumulados desde la marcha blanca de la Etapa 1.

La Figura 7.17 presenta esa red de precedencias entre cuentas de control. El Anexo 7.B lista las 34 dependencias entre paquetes con su fundamento.

<a id="fig:7-red"></a>
![Figura 7.17: Red de precedencias entre cuentas de control e hitos. Fuente: elaboración propia a partir del Anexo 7.B y del Formulario E-25.](<imagenes/Diagramas que faltaban/Fig_7-5_Red_Precedencias.drawio.png>)

**Figura 7.17.** Red de precedencias entre cuentas de control e hitos. Fuente: elaboración propia a partir del Anexo 7.B y del Formulario E-25.

La red muestra tres convergencias. En el H3 se juntan la cadena de la nube (5.2, 3.2 y 3.1) y la de la sala técnica (2.3, 5.1, 6.1, 6.3 y 6.6). En los hitos H4 y H5 se juntan los módulos, la base compartida, el diseño aprobado y la experiencia de usuario. Al cierre de la marcha blanca se juntan la solución certificada, la migración, el equipamiento de cada ola, la certificación de los usuarios y, en la ola de reparto, los acuerdos con los transportistas y el sindicato. Un atraso en cualquiera de esas ramas se propaga al hito aunque no sea de software. La ruta crítica corresponde al diseño, los módulos y la certificación de la Etapa 2, que la sección 7.3.1 analiza.

El secuenciamiento incorpora además las condiciones de la operación de Puelche que el caso exige ver en el plan (sección 17.5). Los congelamientos de septiembre y diciembre, y el cierre de los tres primeros días hábiles de cada mes, son restricciones de calendario para todo corte, despliegue e inicio de ola (paquete 1.3.1). La implantación en bodega y su acompañamiento se programan en el turno de noche, entre las 22:00 y las 06:00 (paquete 4.2.2), y la rotación del 38 % se atiende con capacitación continua y no con un evento único (paquete 7.1.2). Los 62 preventistas y los cerca de 200 conductores se capacitan en su ruta, sin detener la venta ni el reparto (paquetes 7.1.1 y 4.2.2).

Los acuerdos con los diez transportistas y con el sindicato preceden a la ola de reparto (paquetes 5.4.1 y 5.4.2), y la certificación del intercambio electrónico es un paquete por cadena y no una tarea única (paquetes 3.6.5 y 3.6.6). Las interfaces del sistema de gestión se levantan en el Inicio y se prueban temprano (paquetes 1.2.3 y 3.3.2). Las reglas de ruteo del planificador se capturan en los talleres de los meses 1 a 3 y se validan sin él durante la marcha blanca (paquete 1.2.2; resultado R18-16).

### 7.2.2 Estimación

El esfuerzo se estima por paquete con tres valores en horas hombre: optimista, más probable y pesimista (PMI, 2017, p. 201). La incertidumbre de cada estimación se representa con una distribución beta, una de las que el PMBOK admite para modelar la incertidumbre de duración y recursos (PMI, 2017, p. 432). Con ella, la técnica PERT da el esfuerzo esperado \(T_E = (O + 4M + P)/6\) y su desviación \(σ = (P - O)/6\) (Malcolm et al., 1959). El PMBOK presenta también la distribución triangular, \((O + M + P)/3\) (PMI, 2017, p. 201); se prefiere la beta porque da cuatro veces más peso al valor más probable, que el equipo funda en los requerimientos del Formulario T-12 y en las cantidades del Formulario T-11.

La base de cada estimación depende del tipo de paquete. Los módulos y las integraciones se estiman a partir de los requerimientos del Formulario T-12 asignados a cada paquete; la infraestructura, a partir de las cantidades del Formulario T-11; la implantación, a partir de las personas y rutas del caso; y la operación, a partir de los horarios de cobertura y de la periodicidad de los informes. Los paquetes de la fase 8 se estiman por mes y se multiplican por los 36 meses de operación. El Formulario T-15 detalla el método y las reglas de programación. La duración de cada paquete se obtiene de su esfuerzo esperado y de la dotación asignada, y la suma de las varianzas de los paquetes de la ruta crítica entrega la probabilidad de cumplir cada hito con la aproximación normal de PERT. Para programar y controlar, el esfuerzo de cada paquete se reparte entre sus actividades del Formulario T-15, sección 6, sin cambiar su total.

La Tabla 7.4 resume el resultado de la estimación por etapa contractual, con la reserva protegida separada del trabajo base.

<a id="tab_SD7_13"></a>
**Tabla 7.4.** Horas hombre programadas por etapa — Fuente: Formulario T-15, sección 4.3

| Etapa | Meses | HH base y cobertura | HH de reserva protegida | HH programadas |
| --- | --- | --- | --- | --- |
| Etapa 1 · Desarrollo | 1 a 12 | 37.981 | 0 | 37.981 |
| Etapa 1 · Marcha blanca | 13 a 15 | 11.147 | 1.152 | 12.299 |
| Etapa 2 · Desarrollo | 13 a 18 | 11.567 | 0 | 11.567 |
| Etapa 2 · Marcha blanca | 19 y 20 | 7.276 | 0 | 7.276 |
| Soporte puente de la Etapa 1 | 16 a 20 | 14.744 | 1.920 | 16.664 |
| Cierre y estabilización de la implementación | 21 y 22 | 2.775 | 0 | 2.775 |
| Operación | 21 a 56 | 128.374 | 0 | 128.374 |
| **Total** |  | **213.863** | **3.072** | **216.935** |

La operación concentra el 59 % de las horas programadas (128.374 de 216.935 HH), porque cubre 36 meses de servicio continuo del centro de operaciones, la mesa y el SOC; la mesa incluye desde el mes 25, cuando la demanda proyectada se acerca a su límite, un tercer agente en las franjas de menor demanda, con el que cubre sus niveles de servicio hasta 2.391 contactos al mes. Son puestos de turno 24×7 y de mesa, no personas dedicadas a otras tareas. La implementación propiamente tal, de los meses 1 a 22, suma 88.561 HH, y su tramo más denso son los meses 13 a 15, cuando la marcha blanca de la Etapa 1 y el desarrollo de la Etapa 2 suman 17.465 HH (4.485 + 4.889 + 8.090, según la curva del Formulario T-15, sección 4.4), con el máximo de 68 personas equivalentes en el mes 15. Las 3.072 HH de reserva se asignan sólo a la Etapa 1, de modo que una corrección en su marcha blanca no se financia con horas de la Etapa 2.

### 7.2.3 Frentes de trabajo y sincronización

El trabajo se organiza en ocho frentes. Cada frente es un equipo con un responsable que avanza en paralelo con los demás sobre un conjunto de cuentas de control. La Figura 7.18 presenta los frentes, su rol líder, sus cuentas de control y su ventana de actividad entre los meses 1 y 21; la correspondencia completa está en el Formulario T-15.

<a id="fig:7-frentes"></a>
![Figura 7.18: Frentes de trabajo de los meses 1 a 21. Fuente: elaboración propia a partir de los Formularios T-14 y T-15.](<imagenes/Diagramas que faltaban/Fig_7-6_T15-2_Frentes_Trabajo.drawio.png>)

**Figura 7.18.** Frentes de trabajo de los meses 1 a 21. Fuente: elaboración propia a partir de los Formularios T-14 y T-15.

La figura muestra que en ningún mes trabaja un solo frente: entre los meses 1 y 15 avanzan a la vez la dirección, la arquitectura, la construcción de la Etapa 1, la plataforma y la calidad, y desde el mes 9 se suma la implantación. Los frentes se sincronizan en tres instancias. La primera son los hitos del Formulario E-25, porque cada hito exige que varios frentes entreguen a la vez. La segunda son los comités del Art. 71°: el de Proyecto es quincenal y los de Arquitectura y Operación son mensuales, y sus actas registran los acuerdos entre frentes en dos días hábiles (RT-19.09). La tercera son las ventanas de calendario, que son comunes a todos los frentes.

### 7.2.4 Solapamientos de los meses 13 a 15 y 19 a 20

El Art. 17.2 obliga a dimensionar dotación y frentes para dos esfuerzos simultáneos. En los meses 13 a 15 trabajan a la vez el frente de implantación (F7), en la marcha blanca de la Etapa 1 con su acompañamiento; el de construcción de la Etapa 1 (F3), en las correcciones de esa marcha blanca; el de construcción de la Etapa 2 (F4), en su desarrollo, con el H8 en el mes 14; el de calidad (F6), en las pruebas de ambas etapas; y los frentes de dirección y de arquitectura (F1 y F2).

F3 y F4 dependen del mismo rol, el Líder de Desarrollo, pero son equipos distintos. Si el mismo equipo atendiera la marcha blanca y desarrollara la Etapa 2, cada incidente de la marcha blanca atrasaría la Etapa 2, que es precisamente la situación que el Art. 17.2 busca evitar. La Figura 7.18 lo hace visible: en la franja sombreada de los meses 13 a 15, las barras de F3 y F4 coexisten en carriles separados.

En los meses 19 y 20 la Etapa 1 está en producción y la Etapa 2 en marcha blanca. Trabajan F7, en la marcha blanca de la Etapa 2; F4, en sus correcciones; F6, en las pruebas; y el soporte de la Etapa 1 en producción. La dotación de cada frente en cada solapamiento se presenta en el Formulario T-15, de modo que los dos esfuerzos se sumen sin contar dos veces a las mismas personas.

## 7.3 Cronograma e implantación

El cronograma aplica el Art. 17° mes a mes y la implantación aplica las condiciones del Caso 02 (secciones 13.3 y 17.6). Esta sección presenta la ruta crítica, la carta Gantt, el plan de implantación, las marchas blancas, la estabilización y el momento en que se alcanza cada resultado comprometido. El detalle está en los Formularios T-14, T-15 y T-18.

### 7.3.1 Ruta crítica y holguras

La ruta crítica se calcula con el método de la ruta crítica sobre la red del Anexo 7.B (PMI, 2017, pp. 210–211). Una pasada hacia adelante da las fechas tempranas de cada paquete; una pasada hacia atrás, desde los meses fijos del Art. 17°, da las tardías; LS − ES es la holgura total; la libre se mide contra el ES de los sucesores. Como los hitos del Formulario E-25 son fechas fijas, un camino que no llega a su hito tiene holgura negativa y obliga a replanificar.

La ruta crítica corresponde a la Etapa 2: diseño (1.2.5, 2.1.4 y 2.4.2; H8, 4 días hábiles de reserva y 91,1 % de cumplimiento en la simulación con riesgos) → módulos (3.5) → prueba de integración (3.9.1; H9, 21 días hábiles) → certificación (3.9.2–3.9.7; H10, 25 días hábiles). La holgura total de cada camino es su reserva hasta la fecha límite del hito (Formulario T-15, Tabla 5.2). Son casi críticos la cadena de la Etapa 1 que nace en las interfaces sin documentación del ERP (1.2.3 → 3.3.2 → 3.4 → 3.8.1, H4 con 19 días; → 3.8.2–3.8.8, H5 con 35 días), la sala y los ambientes del H3 (2.3, 5.1.2, 6.1, 6.3, 6.6.3 y 3.1; 19 días), la captura de reglas del planificador (1.2.2 y 3.4.7), los acuerdos con transportistas y sindicato (5.4.1 y 5.4.2) y la certificación de las cadenas (3.6.5 y 3.6.6). El H1 tiene la menor reserva absoluta, 6 días, pero su desviación es mínima (σ 0,58; cumplimiento > 99,9 %). Las marchas blancas y los pasos a producción tienen fechas contractuales fijas. La Figura 7.19 sitúa la cadena de la Etapa 2 y los caminos casi críticos en los meses del contrato.

<a id="fig:7-ruta"></a>
![Figura 7.19: Ruta crítica identificada y caminos casi críticos de la implementación. Fuente: elaboración propia a partir del Anexo 7.B y de los períodos del Formulario T-14.](<imagenes/Diagramas que faltaban/Fig_7-7_T15-1_Ruta_Critica.drawio.png>)

**Figura 7.19.** Ruta crítica identificada y caminos casi críticos de la implementación. Fuente: elaboración propia a partir del Anexo 7.B y de los períodos del Formulario T-14.

La Figura 7.19 relaciona las cadenas de diseño, construcción y certificación con sus hitos y con las marchas blancas de ambas etapas. El Formulario T-15 programa los paquetes con entregable con sus dependencias, los diez días hábiles de revisión del Art. 18.3 antes de cada hito y un tope diario de dotación: hasta 40 de los 48 desarrolladores del SD1, escalonados entre junio y septiembre de 2027, y evaluadores subcontratados durante las certificaciones. Cada hito tiene una reserva entre su entrega y su fecha límite, de 4 a 35 días hábiles, dimensionada con la simulación de Monte Carlo del SD8, Anexo 8.C: con los riesgos del registro, cada hito se entrega a tiempo en al menos el 86,5 % de los escenarios (el menor es el H4, que exige todas las integraciones externas de la Etapa 1), y su fecha P80 queda antes de la fecha límite (Formulario T-15, Tabla 5.2). Las marchas blancas y sus cuatro semanas finales no aportan reserva utilizable.

La holgura se gestiona en las instancias de gobierno de la EDT. El avance de cada paquete de la ruta crítica y de los caminos casi críticos se revisa en la reunión semanal de seguimiento y en el Comité de Proyecto quincenal (paquetes 1.3.5 y 1.8.3). Toda amenaza a un hito se escala al Comité Ejecutivo cuando la desviación proyectada supera la mitad de su reserva, sin esperar a consumirla, con su análisis de impacto (paquetes 1.4.3 y 1.8.2). El informe mensual con valor ganado avisa toda desviación mayor al 10 % con su plan dentro de cinco días hábiles (paquete 1.8.6). H7 y H12 dependen además de la aceptación copulativa de la marcha blanca, que no tiene una probabilidad calculada.

### 7.3.2 Carta Gantt y calendario

La carta Gantt del Formulario T-14 cubre los 56 meses y muestra las marchas blancas, los pasos a producción y el inicio de la Operación. La Tabla 7.5 ubica los doce hitos del Formulario E-25 con el paquete que entrega cada uno.

<a id="tab:7-hitos"></a>
**Tabla 7.5.** Hitos del Formulario E-25 en el cronograma. Fuente: elaboración propia a partir del Formulario E-25 y del Formulario T-14.

| Hito | Mes | Entregable que lo gatilla | Paquetes |
| --- | --- | --- | --- |
| H1 | 2 | Línea base de alcance y matriz de trazabilidad | 1.2.1, 1.2.4 |
| H2 | 4 | Arquitectura, plan de seguridad y modelo de datos aprobados | 2.4.1 |
| H3 | 6 | Infraestructura híbrida y ambientes con observabilidad | 3.1.1, 3.1.2, 3.1.3, 3.1.5 |
| H4 | 10 | Software de la Etapa 1 con QA superado | 3.8.1 |
| H5 | 12 | Certificación de la Etapa 1 | 3.8.7 |
| H6 | 13 | Inicio de la marcha blanca de la Etapa 1 | 4.2.1 |
| H8 | 14 | Línea base y diseño de la Etapa 2 | 1.2.5, 2.4.2 |
| H7 | 16 | Paso a producción de la Etapa 1 | 4.2.3 |
| H9 | 17 | Software de la Etapa 2 con QA superado | 3.9.1 |
| H10 | 18 | Certificación de la Etapa 2 | 3.9.6 |
| H11 | 19 | Inicio de la marcha blanca de la Etapa 2 | 4.3.1 |
| H12 | 21 | Paso a producción de la Etapa 2 y aceptación final | 4.3.3, 4.3.4 |

La tabla está ordenada por mes y no por número de hito, porque el H8 (mes 14) ocurre antes que el H7 (mes 16). Ese cruce es la expresión concreta del solapamiento: la línea base de la Etapa 2 se aprueba mientras la Etapa 1 está en su marcha blanca.

Los meses contractuales caen en meses calendario distintos según la fecha de inicio del contrato, que aún no está definida (consulta V-12). La Tabla 7.6 aplica la regla a los tres inicios que el Capítulo 3, sección 3.1.2, considera compatibles con poner la Etapa 2 en producción antes de enero de 2029, fecha desde la que rigen las condiciones de la principal cadena de supermercados.

<a id="tab:7-inicio"></a>
**Tabla 7.6.** Meses contractuales según la fecha de inicio. Fuente: elaboración propia a partir de las Bases Administrativas, Art. 17°, y del Caso 02, secciones 13.2 y 13.3.

| Inicio | Mes 13 (H6) | Mes 16 (H7) | Meses 19 y 20 | Mes 21 (H12) |
| --- | --- | --- | --- | --- |
| Diciembre de 2026 | **Diciembre de 2027** | Marzo de 2028 | Junio y julio de 2028 | Agosto de 2028 |
| Febrero de 2027 | Febrero de 2028 | Mayo de 2028 | Agosto y **septiembre** de 2028 | Octubre de 2028 |
| Marzo de 2027 | Marzo de 2028 | Junio de 2028 | **Septiembre** y octubre de 2028 | Noviembre de 2028 |

Ningún inicio admisible deja las dos marchas blancas completas fuera de septiembre y diciembre; el Anexo 7.A extiende el análisis a los ocho meses de inicio admisibles. Con un inicio en diciembre de 2026, el inicio de la marcha blanca de la Etapa 1 cae en diciembre; con uno en marzo de 2027, el inicio de la marcha blanca de la Etapa 2 cae en septiembre. Con febrero de 2027, en cambio, el congelamiento afecta solo el segundo mes de la marcha blanca de la Etapa 2 y no un inicio, por lo que LafroX lo adopta como supuesto de calendario del cronograma. Su costo es que las semanas de cierre de esa marcha blanca coinciden con el peak de septiembre, que la sección 7.3.5 trata. Dentro de un mes de congelamiento no se inicia ninguna ola ni se despliega ningún cambio, y la marcha blanca continúa en convivencia, con medición diaria.

La Figura 7.20 presenta la carta Gantt resumida de los 56 meses con ese supuesto de inicio, por período contractual. La carta vigente por cuenta de control, generada desde las ventanas reconciliadas de los 222 paquetes, está en el Formulario T-14, sección 3.1.

<a id="fig:7-gantt"></a>
![Figura 7.20: Carta Gantt resumida de los 56 meses, con inicio en febrero de 2027. Fuente: elaboración propia a partir de las Bases Administrativas, Art. 17°, del Formulario E-25 y del Formulario T-14.](<imagenes/Diagramas que faltaban/Fig_7-8_T14-1_Gantt_56_meses.drawio.png>)

**Figura 7.20.** Carta Gantt resumida de los 56 meses, con inicio en febrero de 2027. Fuente: elaboración propia a partir de las Bases Administrativas, Art. 17°, del Formulario E-25 y del Formulario T-14.

La carta muestra que los periodos fijos del Art. 17° se respetan mes a mes y que ningún paso a producción cae en una columna de congelamiento: el mes 16 es mayo de 2028 y el mes 21, octubre de 2028. Las fases de desarrollo aparecen dos veces, una por etapa, y la capacitación continúa durante la operación por la rotación de la bodega. Las columnas rayadas del mes 20 y del mes 23 confirman lo que anticipa la Tabla 7.6: el cierre de la marcha blanca de la Etapa 2 ocurre en septiembre y el primer diciembre de operación llega dos meses después de la aceptación final.

Antes de cada paso a producción, el cronograma reserva las pruebas que exige el numeral 20.1 de las Bases Técnicas Transversales: carga y estrés a 1,5 veces el peak, resiliencia, recuperación ante desastres con conmutación real, seguridad ofensiva y accesibilidad. Además, programa dos ensayos de migración antes de la migración definitiva. En la Etapa 1 estas pruebas forman la cuenta 3.8, se ejecutan en los meses 9 y 10 y se entregan antes del H5 del mes 12; en la Etapa 2 forman la cuenta 3.9, se ejecutan en los meses 16 y 17 y se entregan antes del H10 del mes 18 (Formulario T-15, Tabla 5.2).

### 7.3.3 Plan de implantación y puesta en marcha

La implantación sigue el principio que impone el caso: nada entra en producción sin haber convivido con la forma actual de trabajar, y nada se despliega como un único evento (sección 13.3, condiciones 1 y 3). Técnicamente, cada capacidad se publica con un despliegue azul-verde y se habilita por sitio y por ola mediante indicadores de funcionalidad (feature flags), conforme al Capítulo 4, apartado 4.2.4.1.2. Así, cada ola puede revertirse sin reinstalar y cada operación tiene un único escritor autorizado (Capítulo 4, sección 4.1.8). Ningún despliegue ocurre en la ventana de despacho de 05:30 a 07:00, que no admite indisponibilidad, ni en fechas de congelamiento (Caso 02, RT-10.05).

La Etapa 1 entra en tres olas, en el orden de las dependencias de datos (Capítulo 3, sección 3.4.4). La Tabla 7.7 las presenta.

<a id="tab:7-olas"></a>
**Tabla 7.7.** Olas de implantación de la Etapa 1. Fuente: Capítulo 3, sección 3.4.4, y Formulario T-18.

| Ola | Procesos | Módulos | Avance | Registro oficial |
| --- | --- | --- | --- | --- |
| 1 | Datos maestros y recepción con lote | M1 | Por sitio | Recepciones y lotes |
| 2 | Inventario con FEFO y preparación nocturna | M2, M5 | Por sitio | Stock y preparación |
| 3 | Preventa, rutas, reparto, devoluciones y rendición | M3, M4, M6, M8, M7 | Por zona comercial | Pedidos, entregas y cobros |

Una ola avanza a la siguiente cuando cumple su criterio durante cuatro semanas consecutivas a volumen real: sin defectos críticos ni altos, con conciliación diaria sin diferencias no explicadas, con los indicadores de disponibilidad y tiempo de respuesta cumplidos, con los usuarios certificados y con el acta de la Contraparte Técnica (Capítulo 3, sección 3.4.4).

La programación de olas usa fechas reales y no una equivalencia de meses a 13 semanas: todos los grupos deben estar operativos antes del inicio de los 28 días finales de marcha blanca. T-18 §6.1 propone Talca/Concepción/plataformas/remanentes en semanas 5/6/7/8 para la ola de reparto, subordinadas a fechas permitidas y al límite F − 28 días. Se permite superposición por dominios sin intervenir simultáneamente el mismo proceso ni doble escritura.

<a id="fig:7-olas"></a>
[Ver figura 7.21 en PDF](<imagenes/Diagramas que faltaban/Fig_7-21.pdf>)

**Figura 7.21.** Secuencia de olas de la Etapa 1 durante la marcha blanca. Fuente: elaboración propia a partir del Capítulo 3, sección 3.4.4, y del Formulario T-18.

El avance de cada grupo exige su criterio y acompañamiento. Las cuatro semanas finales requieren todos los grupos y todo el volumen real, no una muestra. E2 habilita todas las cadenas del alcance, portales y costo de servir antes de F − 28 días y, en el ejemplo febrero 2027, antes de septiembre. La carga manual de pedidos mantiene contingencia auxiliar y no acredita intercambio electrónico ni permite excluir una cadena faltante.

La reversión tiene dos niveles, que la Tabla 7.8 distingue.

<a id="tab:7-reversion"></a>
**Tabla 7.8.** Niveles de reversión. Fuente: Capítulo 3, sección 3.4.4; Capítulo 4, apartados 4.2.4.1.2 (liberación y reversión) y 4.1.8 (único escritor); y Formulario T-18.

| Nivel | Qué hace | Quién decide | Plazo |
| --- | --- | --- | --- |
| Técnico | Devuelve el tráfico a la entrega previa por azul-verde/canario o desactiva el indicador de funcionalidad (feature flag) | Líder de Operación / SRE | Objetivo ≤10 minutos, medido en cada ensayo en Preproducción, fuera de la ventana de despacho |
| Operacional, Etapa 1 | Conserva/restaura versión operativa local probada, único escritor y DTE válidos; papel sólo de apoyo | Responsable de operaciones del CLIENTE | Completo antes de las 05:30 |
| Operacional, Etapa 2 | Desactiva la capacidad de la Etapa 2 que falla, sin tocar la Etapa 1 | Responsable de operaciones del CLIENTE | Fuera de la ventana de 05:30 a 07:00 |

La reversión operacional se dispara con señales observables: pedidos sin sincronizar al inicio de la carga, rutas del día no disponibles o un defecto crítico en la ventana de despacho. El plazo de las 05:30 protege la salida de los 96 camiones y no es el tiempo de recuperación ante desastres. La Figura 7.22 presenta el procedimiento por rol.

<a id="fig:7-reversion"></a>
[Ver figura 7.22 en PDF](<imagenes/Diagramas que faltaban/Fig_7-22.pdf>)

**Figura 7.22.** Procedimiento de reversión de la Etapa 1 en la ventana de despacho. Fuente: elaboración propia a partir del Formulario T-18.

La figura muestra que la decisión es del CLIENTE y se toma en el turno de noche, antes de que empiece el despacho. El ensayo debe comprobar que lo capturado permanece en cola y se concilia sin pérdida ni duplicación; no se presume por la descripción. Lo que se pierde es el avance de la ola, que reinicia su período de cuatro semanas (Caso 02, sección 17.6, punto 4). La reversión se ensaya en Preproducción antes de cada corte (paquete 4.1.2), y en ese ensayo se mide el tiempo de cada nivel.

### 7.3.4 Marcha blanca de la Etapa 1

La marcha blanca de la Etapa 1 son tres meses de operación supervisada con datos y usuarios reales, del mes 13 al 15. Convive con la operación vigente: en bodega, con la hoja de picking; en ruta, con la guía en papel; y en Talca, con el WMS de 2013 en solo lectura como respaldo de consulta. Cada día se concilian ambos registros, y toda diferencia se clasifica y explica antes del cierre del día (RT-20.03). La Tabla 7.9 presenta los indicadores que se miden y publican diariamente, con sus umbrales de cierre (RT-20.04).

<a id="tab:7-indicadores"></a>
**Tabla 7.9.** Indicadores diarios de la marcha blanca. Fuente: Bases Administrativas, Art. 17.3; Caso 02, RT-09.01 y RT-10.05; y Capítulo 3, Tabla 3.5.

| Indicador | Umbral | Condición Art. 17.3 |
| --- | --- | --- |
| Incidentes críticos y altos abiertos | 0 | 1 |
| Transacciones de la ola registradas en la solución | 100 % del volumen real durante las 4 últimas semanas | 2 |
| Indisponibilidad en la ventana de 05:30 a 07:00 | 0 minutos | 3 |
| Disponibilidad de la transacción crítica | 99,9 % o más | 3 |
| Tiempo de respuesta, percentil 95 | Línea de preparación hasta 1 s; entrega hasta 2 s; línea de preventa hasta 1,5 s; stock y crédito hasta 2 s | 3 |
| Diferencias de conciliación sin explicar | 0 | 4 |
| Usuarios de la ola certificados | 100 % | 5 |

Los indicadores reproducen las condiciones del Art. 17.3 con umbrales que se pueden medir cada día, de modo que el cierre no depende de un juicio al final del período. El volumen comprometido es la operación real completa de cada proceso y no una muestra; con las cifras del caso (sección 14.1), son cerca de 1.150 recepciones de proveedor y 260.000 líneas de preparación al mes, unos 31.000 pedidos al mes y alrededor de 1.400 entregas por día hábil, o 2.600 si las semanas de cierre coinciden con el peak de septiembre. El detalle por proceso está en el Formulario T-18, Tabla T-18.1.

La sexta condición del Art. 17.3 es el acta de la Contraparte Técnica, que en la Etapa 1 es el H7 del mes 16. Si una condición no se cumple al término del mes 15, la marcha blanca se extiende a costo de LafroX, sin mover las fechas siguientes (Art. 17.3). La Figura 7.23 resume el ciclo diario de control; las condiciones de cierre se enumeran debajo.

<a id="fig:7-ciclo"></a>
[Ver figura 7.23 en PDF](<imagenes/Diagramas que faltaban/Fig_7-23.pdf>)

**Figura 7.23.** Ciclo diario de la marcha blanca. Fuente: elaboración propia a partir de las Bases Administrativas, Art. 17.3, y del RT-20.04.

El ciclo de la Figura 7.23 se repite cada día: se miden los indicadores y se concilian los registros, se comparan los resultados con sus umbrales, se decide entre continuar, corregir o revertir y se publica el resultado diario. Si una incidencia amenaza de inmediato el despacho, se activa el procedimiento de reversión de la Figura 7.22 sin esperar la publicación diaria.

El cierre exige cumplir simultáneamente las seis condiciones del artículo 17.3 de las Bases Administrativas:

1. Cero incidentes críticos o altos abiertos.
2. Volumen real completo durante las últimas cuatro semanas.
3. Sin indisponibilidad en despacho; disponibilidad y respuesta dentro de umbral.
4. Sin diferencias inexplicadas ni pedidos perdidos o duplicados.
5. 100 % de usuarios capacitados y certificados.
6. Acta de aceptación de la Contraparte Técnica (H7).

Ninguna de estas condiciones compensa a otra.

La capacitación se hace en el puesto y en la ruta con las cuatro modalidades del Art. 90.2. Cada perfil se certifica antes del cierre, porque el Art. 17.3 exige que el personal del CLIENTE esté «capacitado y certificado conforme al plan de capacitación aprobado», y los usuarios administradores y el equipo técnico del CLIENTE se certifican además conforme al Art. 90.4. Los perfiles operativos, tomados del Capítulo 3, Anexo 3.I, son 120 preparadores, con un tutor por turno y un aprendizaje en el puesto de dos horas como máximo; 62 preventistas, en su propia ruta; 84 integrantes de la tripulación propia; y cerca de 160 conductores de transportistas, que se incorporan en el andén al asignarse a una ruta.

La adopción se mide por perfil y por ola, y si una ola no alcanza la meta, no avanza y se extiende el acompañamiento. La respuesta es distinta según el grupo: el personal con veinte o treinta años en la compañía recibe acompañamiento individual y reconocimiento formal de su conocimiento, y el personal rotativo de preparación cuenta con un tutor por turno (Formulario T-18, secciones 2.7 y 2.8).

### 7.3.5 Marcha blanca de la Etapa 2 y convivencia

La marcha blanca de la Etapa 2 dura los meses 19 y 20 y convive con la Etapa 1 en producción. La regla central del Art. 17.2 es que exista una única fuente de verdad para los datos compartidos: la Etapa 2 lee y extiende los pedidos, clientes, guías y entregas de la Etapa 1, sin copiarlos ni digitarlos de nuevo, y ningún despliegue de la Etapa 2 modifica las funciones estabilizadas de la Etapa 1 ni ocurre en la ventana de despacho.

Esta marcha blanca dura unas 8,7 semanas (2 × 52 / 12). Como el Art. 17.3 exige volumen real en las cuatro últimas, todas las cadenas certificadas, los portales y el costo de servir deben quedar habilitados en las primeras 4,7 semanas. Con el inicio supuesto de febrero de 2027, el mes 19 es agosto y el mes 20 es septiembre de 2028, de modo que toda habilitación ocurre en agosto, antes del congelamiento del 1 al 25 de septiembre. Las semanas de cierre se miden con el volumen del peak de Fiestas Patrias, cerca de 2.600 entregas diarias, en el primer septiembre de la Etapa 1 en producción. Durante el congelamiento se aplica continuidad previamente autorizada por el CLIENTE; T-18 §6.4 no presume que un cambio de configuración esté exento de las prohibiciones. La capacidad para ese peak se demuestra antes del H11 con la prueba de carga a 1,5 veces el peak, con ambas etapas activas (paquete 3.9.3; Formulario T-18, sección 3.1).

A los indicadores de la Tabla 7.9 se suman los propios del alcance de la Etapa 2: los pedidos de las cadenas certificadas recibidos por vía electrónica, los avisos de despacho dentro de dos minutos, las entregas con costo de servir calculado y la ausencia de degradación de los indicadores de la Etapa 1 (Formulario T-18, sección 3.3). La Figura 7.24 muestra cómo fluyen los datos entre ambas etapas.

<a id="fig:7-convivencia"></a>
[Ver figura 7.24 en PDF](<imagenes/Diagramas que faltaban/Fig_7-24.pdf>)

**Figura 7.24.** Convivencia de la Etapa 1 en producción con la Etapa 2 en marcha blanca. Fuente: elaboración propia a partir de la arquitectura lógica del Capítulo 4.

Se mantiene una sola fuente de verdad y un escritor autorizado por dato. La Etapa 2 no duplica datos ni modifica las funciones estabilizadas de la Etapa 1. Lee el registro único y lo extiende con sus propios datos, de modo que no existe una doble digitación que conciliar. El ERP se mantiene como registro contable y único emisor de la guía de despacho para ambas etapas. El paso a producción del mes 21 es la aceptación final de la implementación (H12) y el inicio de la Operación con ambos alcances (Art. 17.2, punto 4).

### 7.3.6 Estabilización y transferencia

Después de cada paso a producción hay una estabilización de cuatro semanas por ola, con atención reforzada y sin costo adicional (RT-20.06). La dotación se deriva de la operación del caso, como muestra la Tabla 7.10.

<a id="tab:7-estabilizacion"></a>
**Tabla 7.10.** Estabilización por ola. Fuente: Capítulo 3, sección 3.4.4.

| Frente | Personas | Cálculo |
| --- | --- | --- |
| Bodega, turno de noche | 2 | 1 por centro de distribución |
| Plataformas de cross-docking | 3 | 1 por plataforma |
| Calle | 7 | 158 rutas diarias / 24 días de lunes a sábado ≈ 6,6 |
| Coordinación | 1 | Líder de Implantación y Gestión del Cambio |

Las siete personas de calle permiten acompañar cada una de las 158 rutas diarias (96 camiones y 62 preventistas) al menos una vez en las cuatro semanas. Si la ola cubre una sola zona, la dotación se reduce en proporción a sus rutas, y la dotación decrece según la curva de adopción, como exige el RT-20.05.

La operación se transfiere al equipo de TI de cuatro personas del CLIENTE antes del mes 21, con procedimientos documentados y ensayados y con la base de conocimiento. Sigue una mentoría de seis meses (paquetes 7.1.4 y 8.5.2; RT-22.07). Quedan como servicio permanente de LafroX durante los 36 meses los que el Capítulo 3, sección 3.4.5, le asigna: el centro de operaciones, la mesa de servicio, la gestión de incidentes, la continuidad, la seguridad y el mantenimiento.

### 7.3.7 Momento de los resultados comprometidos

El Caso 02 exige indicar en qué momento del cronograma se alcanza cada resultado de aceptación (capítulo 18). La Tabla 7.11 agrupa los dieciséis resultados por momento; el detalle por resultado está en el Anexo 7.C.

<a id="tab:7-resultados"></a>
**Tabla 7.11.** Momento de los resultados de aceptación del caso. Fuente: Caso 02, capítulo 18; Capítulo 3, Anexo 3.J; y Anexo 7.C.

| Momento | Resultados | Cant. | Aceptación |
| --- | --- | --- | --- |
| Marcha blanca de la Etapa 1 (meses 13 a 15) | R18-01, 02, 03, 05, 06, 07, 08, 09, 10, 14, 15 y 16 | 12 | H7 (mes 16) |
| Marcha blanca de la Etapa 2 (meses 19 y 20) | R18-11 y 13 | 2 | H12 (mes 21) |
| Tramos durante el contrato | R18-04: OTIF de 90 % en el mes 15, 93 % en el mes 19 y 95 % en el mes 32 | 1 | Revisión mensual en comité |
| Provisional y final | R18-12: provisional en la marcha blanca de la Etapa 1 y final tras 12 meses de operación | 1 | H7 y operación |

Doce de los dieciséis resultados se aceptan en la marcha blanca de la Etapa 1. Otros dos también se verifican allí: R18-04, con su tramo del mes 15, y R18-12, de forma provisional. Son catorce resultados con verificaciones en ese período, conforme al Anexo 7.C y al Formulario T-18. Por eso el volumen real y la certificación de usuarios de ese período son la principal concentración de riesgo de aceptación del proyecto, y por eso el plan dedica a esa marcha blanca su mayor dotación de acompañamiento.

Las innovaciones también tienen su momento en el cronograma (Art. 29°, punto 4), como resume la Tabla 7.12.

<a id="tab:7-innovaciones"></a>
**Tabla 7.12.** Innovaciones en el cronograma. Fuente: Anexo 7.D.

| Innovación | Paquetes de la EDT | Meses | Hito |
| --- | --- | --- | --- |
| 1 · Seguimiento de vencimiento posentrega en el local | 3.10.1.1 a 3.10.1.4 | 7 a 15 | H4, H5 y marcha blanca E1 |
| 2 · Reproducción de incidentes de terreno | 3.10.2.1 a 3.10.2.4; 8.3.1 | 2 a 15; 21 a 56 | H4 y marcha blanca E1 |
| 3 · Vida útil remanente por historia térmica del lote | 3.10.3.1 a 3.10.3.4; 8.3.2 | 3 a 15; operación | H4, H5 y marcha blanca E1 |
| 4 · Tramo variable de la Operación ligado al costo de servir | 5.4.3; 8.3.3; 8.3.4 | 17 a 20; 21 a 23; 24 a 56 | Hito mensual |
| 5 · Hoja de negocio del almacenero | 3.10.4.1 a 3.10.4.4; 8.3.5; 8.3.6 | 13 a 27 | H9, H10 y H12 |

Tres innovaciones se validan en la marcha blanca de la Etapa 1. La innovación 5 sigue el calendario de la Etapa 2, y la innovación 4 empieza a liquidar recién desde el mes 24, después de una línea base y tres liquidaciones en sombra. Así, ninguna innovación agrega trabajo a la cadena casi crítica de la Etapa 1 después del H4.

### 7.3.8 Base de planificación y recursos

El Formulario T-15, sección 4, estima las horas de los 222 paquetes con tres valores (optimista, más probable y pesimista) por clase de tamaño, y separa las curvas mensuales de implementación, soporte puente de la Etapa 1 y Operación. La cobertura del centro de operaciones, la mesa de servicio y el SOC sigue las posiciones dimensionadas en el Capítulo 4, Anexo 4-W.7. Con esa base, el total programado es de 216.935 HH (204.527 HH de paquetes, 9.336 HH de soporte puente de la Etapa 1 y 3.072 HH de reserva del frente de construcción y de calidad) y el máximo mensual es de 68 personas equivalentes en el mes 15, cuando coinciden la marcha blanca de la Etapa 1 y el desarrollo de la Etapa 2. La sección 5 del mismo formulario calcula la red y el PERT sobre los paquetes nivelados y compara la curva con la dotación del Capítulo 1. Las capacidades protegidas de la Etapa 1 no se prestan al desarrollo de la Etapa 2.

La gestión del plan sigue el Capítulo 6: la sección 6.1 fija el PMBOK adaptado, el tablero Kanban, el valor ganado y el control de cambios, y la sección 6.2 fija el proceso RUP iterativo con DevSecOps. La Construcción avanza en las iteraciones definidas en la sección 6.2, con revisión semanal de avance y bloqueos y una demostración de incremento verificable al cierre de cada iteración; una demostración no implica un paso a producción. El Jefe de Proyecto registra la capacidad y los criterios de terminado antes de seleccionar el trabajo de cada iteración, y los cambios se aprueban según la sección 6.1.4.

El cronograma rector usa meses contractuales 1 a 56. El Anexo 7.A traduce esos meses a fechas con un inicio supuesto en febrero de 2027; cuando el CLIENTE confirme la fecha de inicio (consulta V-12), se recalculan los meses calendario y los congelamientos antes de aprobar cada corte. La revisión de parámetros de la Innovación 3 (paquete 8.3.2) se ejecuta en los meses 26, 32, 38, 44, 50 y 56.

El Formulario T-18, sección 6, define la cobertura por ola de M9, M12 y M10, propone Talca como sitio piloto, ordena las olas por sitio, por rutas y por certificación de cadenas, declara la estabilización de la Etapa 2 y el soporte de la Etapa 1 en los meses 16 a 20, y fija un objetivo de 40 minutos para el ensayo de reversión. El corte exige un ensayo con volumen real y la contingencia tributaria; el respaldo manual por sí solo no sustituye ese ensayo para los 96 despachos. El WMS queda en modo de solo lectura conforme al supuesto S-14.

El Anexo 7.F traslada al Capítulo 8 los supuestos, disparadores, responsables y paquetes de la planificación. La regla de precio es única en la oferta: el precio acordado al capturar el pedido (Capítulo 2, Anexo 2.2, S-09; RF-03.11 y RF-03.12). La coordinación de reserva y retención (SD4, apartado 4.1.4.4) está dimensionada en el Anexo 4-I, Tabla A.10, y el Anexo 4-W, Tablas A.32 y A.33. El máximo de cuatro mensajes por línea incluye una holgura porque la retención consumida no se libera. La proporción de líneas con más de una retención se mide con AL-STOCK-01 antes del H4 (R8-02), y la carga y el drenaje se verifican en 3.8.4 y 3.9.3, sin sumar la coordinación al drenaje tras un corte. El RPO ≤ 15 min se cumple con fibra, LTE y Starlink. La falla simultánea de los tres caminos seguida de la destrucción del sitio antes de reponer alguno es el riesgo residual declarado en SD4 4.3.2.4, gestionado en SD8 con R8-05 y verificado con AL-DR-01. Sus medidas son alarmas de retraso a 5 y 15 min, reposición del enlace, preemisión de guías y NAS WORM. La continuidad crítica y la capacidad nominal se verifican conforme al Anexo 8.E, con responsable y hito límite.

## 7.4 Referencias

Las Bases se citan con su documento y el artículo, capítulo, sección o código del requisito; las referencias internas a otros capítulos de esta oferta se indican por su número de capítulo y sección.

- Distribuidora Puelche S.A. (2026a). *Bases Administrativas de Licitación N.º TFEP-01/2026: Contratación de Solución Integral de Software y Servicios de Operación*.

- Distribuidora Puelche S.A. (2026b). *Bases Técnicas Transversales de Licitación N.º TFEP-01/2026*.

- Distribuidora Puelche S.A. (2026c). *Caso 02: Logística. Especificaciones del problema y operación de Distribuidora Puelche S.A.*

- Distribuidora Puelche S.A. (2026d). *Aclaraciones de la Licitación N.º TFEP-01/2026*.

- Malcolm, D. G., Roseboom, J. H., Clark, C. E., & Fazar, W. (1959). Application of a technique for research and development program evaluation. *Operations Research, 7*(5), 646–669.

- Project Management Institute. (2017). *La guía de los fundamentos para la dirección de proyectos (Guía del PMBOK®)* (6.ª ed.). Project Management Institute.

## 7.5 Declaración de uso de IA

En cumplimiento de la sección 7.2 de las Aclaraciones de la licitación, la tabla siguiente declara el uso de herramientas de inteligencia artificial en este subdocumento, con la revisión humana de cada parte. La declaración se consolida en el Formulario A-6.

<a id="tab:7-ia"></a>
**Tabla 7.13.** Declaración de uso de IA. Fuente: registro del equipo.

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
| --- | --- | --- | --- | --- | --- |
| Introducción | Claude Code | Redacción a partir de las Bases y de los capítulos de la oferta | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 7.1 EDT | Claude Code | Redacción, conteos desde la EDT del equipo y figuras de la EDT | Alto | Alto | [[REVISIÓN HUMANA]] |
| 7.2 Plan de trabajo | Claude Code | Redacción del secuenciamiento y de los frentes; red y carriles | Alto | Alto | [[REVISIÓN HUMANA]] |
| 7.3 Cronograma e implantación | Claude Code | Redacción, calendario por fecha de inicio, Gantt y flujos | Alto | Alto | [[REVISIÓN HUMANA]] |
| Anexos 7.A a 7.E | Claude Code | Listados y cálculo del calendario | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| Formulario T-14 | Claude Code | Diccionario a partir del diccionario de trabajo del equipo; Gantt por cuenta | Alto | Alto | [[REVISIÓN HUMANA]] |
| Formulario T-15 | Claude Code | Estructura, método y frentes | Alto | Alto | [[REVISIÓN HUMANA]] |
| Formulario T-18 | Claude Code | Redacción a partir del Capítulo 3 y del caso | Alto | Alto | [[REVISIÓN HUMANA]] |
| Ajustes de planificación SD7, T-14/T-15/T-18 y Anexo 7.F | Codex | Coherencia documental, supuestos de recursos y cálculo reproducible CPM/PERT, preparación de dependencias para SD8 | Alto | Descripciones textuales | [[REVISIÓN HUMANA]] |
| Cronograma por actividad, nivelación y PERT del T-15 §5–§6; criterio 8/80 de 7.1 | Claude Code | Descomposición de los paquetes en actividades según el PMBOK (Project Management Institute, 2017, cap. 6) | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| Correcciones interdocumentales SD7, Anexo 7.B, T-14 y T-15 | Claude Code | Ventanas y dependencias, revisión Art. 18.3, PERT, cobertura de mesa/SOC, carta Gantt vigente en Mermaid, salida y reversibilidad | Alto | Alto (carta Gantt Mermaid) | [[REVISIÓN HUMANA]] |
