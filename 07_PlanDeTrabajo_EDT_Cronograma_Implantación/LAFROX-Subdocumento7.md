# Capítulo 7. Introducción al Plan de trabajo

Este capítulo presenta cómo LafroX ejecutará el proyecto de Distribuidora Puelche dentro del cronograma contractual obligatorio de 56 meses (Bases Administrativas, Art. 17°): qué trabajo se hace, en qué orden, con qué esfuerzo y cómo la solución entra en operación sin detener la venta, la bodega ni el reparto.

La sección 7.1 descompone el 100 % del alcance en una estructura de descomposición del trabajo (EDT) con paquetes estimables y asignables. La sección 7.2 secuencia ese trabajo y lo organiza en frentes paralelos, con especial atención a los meses 13 a 15 y 19 a 20, en que dos esfuerzos coexisten. La sección 7.3 presenta la ruta crítica, la carta Gantt con los hitos del Formulario E-25 y el plan de implantación y de marcha blanca de cada etapa.

El capítulo se apoya en otros tres capítulos de la oferta: el Capítulo 3 fija el alcance de cada etapa, la secuencia de olas y la dotación de estabilización; el Capítulo 4 define los módulos M1 a M12 y las interfaces que la EDT construye; y el Capítulo 6 establece el proceso de desarrollo cuyas fases organizan la EDT y la gestión del proyecto que la controla. El detalle va en tres formularios y un archivo de anexos: el Formulario T-14 contiene la EDT completa, su diccionario y la carta Gantt; el Formulario T-15, el método de estimación y programación, la ruta crítica y los frentes de trabajo; el Formulario T-18, la implantación y la puesta en marcha controlada; y los Anexos 7.A a 7.E, los listados de apoyo.

## 7.1 EDT

La EDT es la base común del plan: el cronograma, la estimación y la asignación de responsables se construyen sobre sus paquetes, y su diccionario fija qué se entrega y cómo se acepta cada uno. Esta sección explica cómo se descompuso el trabajo, cómo queda la estructura, cómo cubre el alcance y cómo se asignan los responsables.

### Criterio de descomposición

La EDT de Puelche se organiza en nueve fases. Las cuatro primeras son las fases del proceso de desarrollo del Capítulo 6 (Inicio, Elaboración, Construcción y Transición) y se recorren una vez por cada etapa del Art. 17°. El primer recorrido produce la Etapa 1, con la trazabilidad de recepción, la bodega, la cadena de frío, la preventa, las rutas, el reparto y la rendición, y termina con el paso a producción del mes 16. El segundo produce la Etapa 2, con el canal moderno, los portales y el costo de servir, y termina con el paso a producción del mes 21.

Las otras cinco fases agrupan el trabajo que no es desarrollo de software, pero sin el cual la solución no entra en operación: adquisiciones y contrataciones; infraestructura física y sitios; capacitación y gestión del cambio; operación y soporte durante 36 meses; y cierre.

La descomposición sigue la regla del 100 %: la suma del trabajo de los niveles inferiores reproduce el trabajo del nivel superior, sin omitir ni agregar alcance (Project Management Institute [PMI], 2017, p. 161). El segundo nivel son 49 cuentas de control, puntos de gestión donde se integran el alcance, el cronograma y el esfuerzo para medir el desempeño. El nivel inferior son 222 paquetes de trabajo, cada uno con un entregable verificable, un criterio de aceptación y un único responsable (PMI, 2017, pp. 161–162). En la cuenta de las innovaciones, cada innovación agrupa sus paquetes en un cuarto nivel.

Los paquetes de la fase de Operación son paquetes de esfuerzo continuo. Cada uno cubre un servicio durante los 36 meses y se controla con entregables periódicos, como los informes mensuales de servicio, los informes de pruebas y las actualizaciones anuales, que funcionan como sus puntos de verificación.

**Cuentas de control y paquetes por fase.** Fuente: elaboración propia a partir del Formulario T-14 y del Formulario E-25.

| Fase | CC | PT | Etapa | Hitos |
|---|---:|---:|---|---|
| 1 Inicio | 9 | 35 | E1 y E2 | H1, H8 |
| 2 Elaboración | 6 | 18 | E1 y E2 | H2, H8 |
| 3 Construcción | 11 | 79 | E1 y E2 | H3, H4, H5, H9, H10 |
| 4 Transición | 3 | 10 | E1 y E2 | H6, H7, H11, H12 |
| 5 Adquisiciones y contrataciones | 4 | 13 | E1 y E2 | Habilita H3 |
| 6 Infraestructura física y sitios | 6 | 24 | E1 | Habilita H3 y H6 |
| 7 Capacitación y gestión del cambio | 3 | 13 | E1, E2 y Operación | Condición de H7 y H12 |
| 8 Operación y soporte (36 meses) | 5 | 26 | Operación | Hito mensual |
| 9 Cierre | 2 | 4 | Meses 21 y 56 | Después de H12 |
| **Total** | **49** | **222** | | |

La construcción concentra el 36 % de los paquetes (79 de 222), porque contiene los quince desarrollos de módulos, las integraciones, la migración, las pruebas de ambas etapas y las innovaciones. Las fases 5 a 7, que no producen software, suman 50 paquetes (23 %). Ese peso muestra que, en Puelche, la compra y la instalación del equipamiento de cinco sitios, los acuerdos con diez transportistas y con el sindicato y la capacitación de una operación que no puede detenerse son trabajo planificado y controlado, no supuestos.

**Figura 7-edt — Vista general de la EDT y su relación con las etapas del Art. 17°.** La raíz “Plataforma logística de Distribuidora Puelche” contiene 49 cuentas de control y 222 paquetes. Las fases 1 a 4 forman el ciclo de desarrollo, que se repite por etapa; las fases 5 a 7 son soporte paralelo; las fases 8 y 9 son operación y cierre. La banda temporal representa Etapa 1 (H1–H7, hasta mes 16), Etapa 2 (H8–H12, meses 13–21) y operación con hito mensual (meses 21–56); fase 9 cierra en los meses 21 y 56. La EDT no expresa secuencia: el número de una fase no indica cuándo ocurre, y sus fechas están en la carta Gantt de la sección 7.3.2. Fuente: elaboración propia a partir de las Bases Administrativas, Art. 15° y 17°, y del Formulario T-14.

### Estructura general

Las figuras 7-edt-dev y 7-edt-sop presentan el segundo nivel de la EDT: las cuentas de control de cada fase, con la cantidad de paquetes de cada una y los hitos que producen.

**Figura 7-edt-dev — Cuentas de control de las fases de desarrollo 1 a 4.** Inicio (9 CC, 35 PT): 1.1 Definición inicial del proyecto (3); 1.2 Alcance del proyecto (5; H1, H8); 1.3 Planificación (5); 1.4 Interesados y comunicaciones (3); 1.5 Calidad (2); 1.6 Riesgos (2); 1.7 Plan de Reversibilidad (2); 1.8 Gobierno y control (8); 1.9 Cumplimiento normativo y contractual (5). Elaboración (6 CC, 18 PT): 2.1 Arquitectura (4); 2.2 Diseño de seguridad (4); 2.3 Diseño de sala y racks (3); 2.4 Validación de diseños (2; H2, H8); 2.5 Continuidad del negocio (2); 2.6 Experiencia de usuario (3). Construcción (11 CC, 79 PT): 3.1 Ambientes y cadena de desarrollo (5; H3); 3.2 Servicios de nube (6); 3.3 Base compartida (6); 3.4 Módulos E1 (11); 3.5 Módulos E2 (4); 3.6 Integraciones externas (6); 3.7 Migración (5); 3.8 Pruebas E1 (8; H4, H5); 3.9 Pruebas E2 (7; H9, H10); 3.10 Innovaciones (16; INN-01, 02, 03 y 05); 3.11 Documentación técnica (5). Transición (3 CC, 10 PT): 4.1 Plan de implantación (3); 4.2 Marcha blanca y producción E1 (3; H6, H7); 4.3 Marcha blanca y producción E2 (4; H11, H12). Las fases 1 a 4 se recorren dos veces: la primera termina en H7 (mes 16) y la segunda en H12 (mes 21). Fuente: elaboración propia a partir del Formulario T-14 y del Formulario E-25.

En la Figura 7-edt-dev, cada rombo marca la cuenta de control que entrega el hito. La fase de Inicio fija qué se construye y cómo se dirige el proyecto. Además del acta, la línea base y los planes, contiene dos paquetes que solo existen por la situación de Puelche: el 1.2.2, que captura las reglas de ruteo del planificador cuya jubilación tiene fecha dentro del contrato (Caso 02, capítulo 18, resultado 16), y el 1.2.3, que especifica las interfaces del sistema de gestión que el CLIENTE reconoce no tener documentadas (Caso 02, sección 17.5). También incluye el gobierno del proyecto, con los comités del Art. 71°, el informe mensual con valor ganado y el tablero (RT-19.06 a RT-19.09), y el cumplimiento normativo y contractual.

La fase de Elaboración diseña la solución antes de programar: la arquitectura lógica y física, el modelo de datos con trazabilidad por lote, el plan de seguridad, los planos de la sala técnica de Talca, que hoy no cumple el estándar exigido (Caso 02, capítulo 16), la continuidad del negocio y la experiencia de usuario, diseñada con preparadores que trabajan con guantes a −22 °C, preventistas sin señal y conductores externos. La aprobación de la arquitectura, la seguridad y el modelo de datos es el H2 del mes 4.

La fase de Construcción produce los cinco ambientes y los servicios de nube; la base compartida, con la identidad, la integración con el ERP como único emisor de la guía de despacho, la convivencia con el WMS de 2013 y la operación sin conexión; los once módulos de la Etapa 1 y los cuatro desarrollos de la Etapa 2; las integraciones externas y la migración de datos; las pruebas de certificación de ambas etapas, las innovaciones y la documentación técnica. La fase de Transición convierte la solución probada en el registro oficial mediante el plan de olas, la reversión, las dos marchas blancas y la estabilización.

**Figura 7-edt-sop — Cuentas de control de las fases 5 a 9.** Adquisiciones y contrataciones (4 CC, 13 PT): 5.1 Hardware e infraestructura (3), 5.2 Nube y licencias (3), 5.3 Enlaces (3), 5.4 Acuerdos con terceros (4; transportistas, sindicato y fórmula de INN-04). Infraestructura física y sitios (6 CC, 24 PT): 6.1 Sala técnica de Talca (5), 6.2 Cableado (3), 6.3 Racks y gabinetes (4), 6.4 Seguridad física (3), 6.5 Equipamiento de campo (6), 6.6 Configuración de infraestructura (3). Capacitación y gestión del cambio (3 CC, 13 PT): 7.1 Capacitación por roles (6), 7.2 Gestión del cambio (5), 7.3 Evaluaciones y certificaciones (2; condición de cierre de cada marcha blanca, Art. 17.3). Operación y soporte (5 CC, 26 PT): 8.1 Servicios de operación (6), 8.2 Mantenimiento (7), 8.3 Innovaciones en operación (6), 8.4 Informes y obligaciones periódicas (4), 8.5 Capacitación y transferencia (3), meses 21 a 56. Cierre (2 CC, 4 PT): 9.1 Cierre de implementación (2, mes 21), 9.2 Salida al término del contrato (2, mes 56). Fuente: elaboración propia a partir del Formulario T-14.

La Figura 7-edt-sop muestra que el trabajo que no es software tiene cuentas propias con responsable. La fase de Adquisiciones y contrataciones separa lo que compra el CLIENTE de lo que contrata LafroX: el CLIENTE compra el hardware de terreno y de la sala, que LafroX especifica y recibe, y LafroX contrata la nube, los enlaces y las licencias. Esta fase reúne también los acuerdos sin los cuales la solución no sale a la ruta, con las diez empresas transportistas y con el sindicato, y la fórmula contractual de la innovación 4.

La fase de Infraestructura física y sitios instala la sala de Talca, con energía, climatización y extinción; los racks y los gabinetes de borde de Concepción y de las tres plataformas de cross-docking; los terminales, los sensores de cámara y los termógrafos de los 28 camiones con frío; y los enlaces con su respaldo. Termina con la prueba de autonomía de 24 horas del centro de distribución.

La fase de Capacitación y gestión del cambio atiende la rotación del 38 % en preparación, con capacitación continua del turno de noche; al personal con veinte o treinta años en la compañía, con acompañamiento individual; la incorporación en el andén de los conductores externos; y el traspaso al equipo de TI de cuatro personas. La certificación de usuarios, destacada en la cuenta 7.3, es una de las seis condiciones de cierre de cada marcha blanca. La fase de Operación presta los servicios de los meses 21 a 56, y la de Cierre entrega el código al término de la implementación y ejecuta la salida al término del contrato.

### Cobertura del alcance

Las Aclaraciones de la licitación exigen que la EDT contenga explícitamente las innovaciones y las actividades de seguridad, calidad, migración e implantación (sección 11, Capítulo 7), y el Caso 02 exige que contenga la arquitectura (capítulo 19). La tabla comprueba que cada uno de esos componentes tiene paquetes propios.

**Cobertura del alcance en la EDT.** Fuente: elaboración propia a partir del Formulario T-14, del Capítulo 4 y de las Aclaraciones.

| Componente | Elementos | PT | Cuentas de control | Exigencia |
|---|---|---:|---|---|
| Módulos | M1 a M12 y dos portales | 15 | 3.4, 3.5 | Caso 02, cap. 19 |
| Interfaces | INT-01 a INT-15 | 21 | 3.1, 3.3, 3.4, 3.6, 6.3, 6.5 | Caso 02, cap. 19 |
| Innovaciones | INN-01 a INN-05 | 23 | 3.10, 5.4, 8.3 | Aclaraciones; BA, Art. 29° |
| Seguridad | Diseño, construcción, pruebas y operación | 17 | 1.9, 2.2, 3.2, 3.3, 3.8, 3.9, 3.11, 6.4, 8.1, 8.2 | Aclaraciones |
| Calidad | Planes, puertas, pruebas y deuda técnica | 19 | 1.5, 3.8, 3.9, 3.11, 8.2 | Aclaraciones |
| Migración | Perfilamiento, carga, ensayos y conciliación | 6 | 3.3, 3.7 | Aclaraciones; BTT, numeral 20.1 |
| Implantación | Olas, marchas blancas, capacitación y cambio | 23 | 4.1 a 4.3, 7.1 a 7.3 | Aclaraciones; RT-20.01 a 20.08 |

La tabla muestra que ninguna exigencia descansa en un paquete genérico. La seguridad, por ejemplo, aparece en las cinco fases donde ocurre: el diseño de la Elaboración, la identidad y las pruebas de seguridad ofensiva de la Construcción, la seguridad física de la sala y el centro de operaciones de seguridad durante la Operación. Las pruebas de seguridad ofensiva 3.8.6 y 3.9.5 se cuentan en la fila de seguridad y en la de calidad, porque son a la vez control de seguridad y prueba de certificación. Las pruebas de la Etapa 2 repiten las de la Etapa 1 con una exigencia adicional: demostrar que la Etapa 1 en producción no se degrada.

**Figura 7-cobertura — Distribución por fase de las categorías de alcance.** La matriz ubica innovaciones, seguridad, calidad, migración e implantación en las fases 1 a 9: innovaciones en 3 (INN-01, 02, 03 y 05), 5 (INN-04) y 8 (INN-02 a 05); seguridad en 1, 2, 3, 6 y 8; calidad en 1, 3 y 8; migración en 3; implantación en 4 y 7. Las celdas listan los paquetes: fase 1, seguridad 1.9.2–1.9.4 y calidad 1.5.1–1.5.2; fase 2, seguridad 2.2.1–2.2.4; fase 3, innovaciones 3.10.1–3.10.4, seguridad 3.2.5, 3.3.1, 3.8.6, 3.9.5, 3.11.4, calidad 3.8.1–3.8.8, 3.9.1–3.9.7, 3.11.3 y migración 3.3.3, 3.7.1–3.7.5; fase 4, implantación 4.1.1–4.1.3, 4.2.1–4.2.3 y 4.3.1–4.3.4; fase 5, INN-04 5.4.3; fase 6, seguridad 6.4.1–6.4.3; fase 7, implantación 7.1.1–7.1.6, 7.2.1–7.2.5, 7.3.1–7.3.2; fase 8, innovaciones 8.3.1–8.3.6, seguridad 8.1.5 y 8.2.2, calidad 8.2.4. Fuente: elaboración propia a partir del Formulario T-14 y de las Aclaraciones, sección 11.

La matriz confirma que las cinco categorías se distribuyen desde el diseño hasta la operación. Las innovaciones tienen paquetes en las fases donde se construyen, se contratan y se operan: INN-01, INN-02, INN-03 e INN-05 se construyen en la cuenta 3.10; la fórmula contractual de INN-04 se aprueba en la cuenta 5.4, porque es una innovación de modelo de contratación y no tiene paquete de construcción; e INN-02 a INN-05 tienen su parte de operación en la cuenta 8.3. Cada innovación tiene sus meses en el Anexo 7.D (Bases Administrativas, Art. 29°, punto 4).

Los anexos completan la cobertura. El Anexo 7.E relaciona los doce módulos y las quince interfaces del Capítulo 4 con el paquete que los construye y prueba, y el Anexo 7.C ubica los dieciséis resultados de aceptación del caso en su paquete y su momento. Los requerimientos del Formulario T-12 se trazan a los paquetes mediante la matriz de trazabilidad del paquete 1.2.4, que se aprueba con el H1.

### Diccionario y asignación de responsables

El diccionario de la EDT, en el Formulario T-14, describe cada paquete con su entregable, su criterio de aceptación, su responsable y el período del cronograma en que se ejecuta, junto con el hito del Formulario E-25 que habilita. Todo entregable se recibe con el acta de la Contraparte Técnica, acompañada de su evidencia de verificación, su trazabilidad hacia los requerimientos y las observaciones resueltas (Bases Administrativas, Art. 18.1 y 18.2). Los criterios del diccionario se suman a esa regla común. Por ejemplo, el paquete 3.4.1 (M1 Recepción) se acepta solo si ningún producto con trazabilidad obligatoria se recibe sin lote, y el 4.1.2 (reversión de la Etapa 1) se acepta solo si su ensayo en Preproducción termina antes de las 05:30 sin perder registros.

Los responsables son los ocho roles de la estructura para el proyecto del Capítulo 1, sección 1.5. La tabla muestra cómo se reparten los paquetes.

**Paquetes por responsable.** Fuente: elaboración propia a partir del Formulario T-14.

| Rol | PT | % | Fases con más paquetes |
|---|---:|---:|---|
| Líder de Operación / SRE | 58 | 26 % | 6 (21), 3 (13), 8 (12) |
| Líder de Implantación y Gestión del Cambio | 34 | 15 % | 7 (13), 4 (7) |
| Jefe de Proyecto | 33 | 15 % | 1 (22) |
| Líder de Desarrollo | 24 | 11 % | 3 (21) |
| Líder de Calidad | 19 | 9 % | 3 (15) |
| Arquitecto de Solución | 18 | 8 % | 2 (5), 3 (6) |
| Encargado de Seguridad de la Información | 18 | 8 % | 1 (4), 2 (4), 3 (4) |
| Líder de Datos | 18 | 8 % | 3 (16) |
| **Total** | **222** | **100 %** | |

Todos los paquetes tienen un responsable único, de modo que son asignables. La distribución sigue la naturaleza del trabajo: el Jefe de Proyecto concentra la gestión y el gobierno; el Líder de Desarrollo, la construcción; y el Líder de Implantación, la capacitación y la transición. El Líder de Operación / SRE responde por un cuarto de los paquetes, porque reúne la nube, la infraestructura de los cinco sitios y la operación, y sus paquetes de las fases 3 y 6 ocurren a la vez. Responder por un paquete no significa ejecutarlo en persona: la sección 7.2.3 y el Formulario T-15 muestran qué frente ejecuta el trabajo bajo cada rol.

## 7.2 Plan de trabajo

El plan de trabajo aplica las metodologías del Capítulo 6. La gestión del proyecto se basa en el PMBOK: los alcances aprobados (H1 y H8) y el cronograma son las líneas base contra las que se mide el avance; el avance se mide con valor ganado en el informe mensual (RT-19.06 y RT-19.07); y todo cambio de alcance, plazo o criterio de aceptación se aprueba antes de incorporarse al plan, conforme al Art. 72° (paquete 1.4.3).

El desarrollo sigue las cuatro fases del proceso iterativo del Capítulo 6, que la EDT recorre una vez por etapa. Dentro de la Construcción, cada módulo avanza por iteraciones que producen resultados verificables, mientras que la marcha blanca y la aceptación formal ocurren solo en los meses que fija el Art. 17°. El tablero de flujo del equipo coordina las tareas diarias, pero no reemplaza el cronograma ni la aceptación formal de los entregables, como establece la metodología de gestión de proyectos del Capítulo 6.

### Secuenciamiento y dependencias

El orden del trabajo sigue las dependencias de datos y de infraestructura de Puelche (Capítulo 3, sección 3.4.3). Primero se aprueban el alcance (H1, mes 2) y el diseño (H2, mes 4). En paralelo, se especifica y compra el equipamiento de la sala y de los sitios, y se contratan la nube y los enlaces, de modo que la infraestructura híbrida y los ambientes queden habilitados en el H3 del mes 6.

La construcción de la Etapa 1 parte por la base compartida, porque si falla, fallan todos los módulos. Sigue con recepción e inventario, que alimentan la preparación y el retiro sanitario, mientras la preventa avanza en paralelo porque necesita stock y crédito. Las rutas y el reparto se integran cuando existen el pedido confirmado y la preparación, y la rendición, cuando existe la entrega registrada. La Etapa 2 se diseña en los meses 13 y 14 (H8), reutiliza los pedidos, las guías y las evidencias ya probadas, y calcula el costo de servir con los hechos acumulados desde la marcha blanca de la Etapa 1.

La Figura 7-red presenta la red de precedencias entre cuentas de control. El Anexo 7.B lista las 34 dependencias entre paquetes con su fundamento.

**Figura 7-red — Red de precedencias entre cuentas de control e hitos.** La red separa la Etapa 1 (meses 1–16) y la Etapa 2 (meses 13–21); muestra la cadena crítica como enlaces rojos y los hitos E-25 como rombos. En la Etapa 1 conecta alcance 1.2, arquitectura 2.1 y validación 2.4 (H1, H2); seguridad 2.2, base compartida 3.3, módulos 3.4, pruebas 3.8 y marcha blanca/producción 4.2 (H4–H7); experiencia de usuario 2.6 precede a 3.4. Los caminos de infraestructura reúnen diseño 2.3, hardware 5.1, sala 6.1, racks 6.3 e infraestructura de sitios 6.6 para H3, y nube/licencias 5.2, nube 3.2 y ambientes 3.1 también convergen en H3. Las condiciones de marcha blanca —acuerdos 5.4, equipamiento 6.5, migración 3.7, plan 4.1 y certificación 7.3— convergen en 4.2. Para Etapa 2, H8 precede a módulos 3.5, pruebas 3.9 y transición 4.3 (H9–H12), seguidos por operación 8 y cierre 9.1; cadenas 3.6.5/3.6.6 y traspaso/certificación 7.1.4/7.3.2 alimentan 4.3. Las líneas distinguen precedencia fin-comienzo y comienzo-comienzo (CC). Fuente: elaboración propia a partir del Anexo 7.B y del Formulario E-25.

La red muestra tres convergencias. En el H3 se juntan la cadena de la nube (5.2, 3.2 y 3.1) y la de la sala técnica (2.3, 5.1, 6.1, 6.3 y 6.6). En los hitos H4 y H5 se juntan los módulos, la base compartida, el diseño aprobado y la experiencia de usuario. Al cierre de la marcha blanca se juntan la solución certificada, la migración, el equipamiento de cada ola, la certificación de los usuarios y, en la ola de reparto, los acuerdos con los transportistas y el sindicato. Un atraso en cualquiera de esas ramas se propaga al hito aunque no sea de software. La cadena marcada en rojo es la ruta crítica identificada, que la sección 7.3.1 analiza.

El secuenciamiento incorpora además las condiciones de la operación de Puelche que el caso exige ver en el plan (sección 17.5). Los congelamientos de septiembre y diciembre, y el cierre de los tres primeros días hábiles de cada mes, son restricciones de calendario para todo corte, despliegue e inicio de ola (paquete 1.3.1). La implantación en bodega y su acompañamiento se programan en el turno de noche, entre las 22:00 y las 06:00 (paquete 4.2.2), y la rotación del 38 % se atiende con capacitación continua y no con un evento único (paquete 7.1.2). Los 62 preventistas y los cerca de 200 conductores se capacitan en su ruta, sin detener la venta ni el reparto (paquetes 7.1.1 y 4.2.2).

Los acuerdos con los diez transportistas y con el sindicato preceden a la ola de reparto (paquetes 5.4.1 y 5.4.2), y la certificación del intercambio electrónico es un paquete por cadena y no una tarea única (paquetes 3.6.5 y 3.6.6). Las interfaces del sistema de gestión se levantan en el Inicio y se prueban temprano (paquetes 1.2.3 y 3.3.2). Las reglas de ruteo del planificador se capturan en los talleres de los meses 1 a 3 y se validan sin él durante la marcha blanca (paquete 1.2.2; resultado R18-16).

### Estimación

El esfuerzo se estima por paquete con tres valores en horas hombre: optimista, más probable y pesimista (PMI, 2017, p. 201). La incertidumbre de cada estimación se representa con una distribución beta, una de las que el PMBOK admite para modelar la incertidumbre de duración y recursos (PMI, 2017, p. 432). Con ella, la técnica PERT da el esfuerzo esperado \(T_E = (O + 4M + P)/6\) y su desviación \(\sigma = (P - O)/6\) (Malcolm et al., 1959). El PMBOK presenta también la distribución triangular, \((O + M + P)/3\) (PMI, 2017, p. 201); se prefiere la beta porque da cuatro veces más peso al valor más probable, que el equipo funda en los requerimientos del Formulario T-12 y en las cantidades del Formulario T-11.

La base de cada estimación depende del tipo de paquete. Los módulos y las integraciones se estiman a partir de los requerimientos del Formulario T-12 asignados a cada paquete; la infraestructura, a partir de las cantidades del Formulario T-11; la implantación, a partir de las personas y rutas del caso; y la operación, a partir de los horarios de cobertura y de la periodicidad de los informes. Los paquetes de la fase 8 se estiman por mes y se multiplican por los 36 meses de operación. El Formulario T-15 detalla el método y las reglas de programación. La duración de cada paquete se obtiene de su esfuerzo esperado y de la dotación asignada, y la suma de las varianzas de los paquetes de la ruta crítica entrega la probabilidad de cumplir cada hito con la aproximación normal de PERT.

### Frentes de trabajo y sincronización

El trabajo se organiza en ocho frentes. Cada frente es un equipo con un responsable que avanza en paralelo con los demás sobre un conjunto de cuentas de control. La Figura 7-frentes presenta los frentes, su rol líder, sus cuentas de control y su ventana de actividad entre los meses 1 y 21; la correspondencia completa está en el Formulario T-15.

**Figura 7-frentes — Frentes de trabajo, meses 1 a 21.** F1 Dirección y gobierno, Jefe de Proyecto: meses 1–21 y tareas continuas hasta el 56 (cuentas 1.1–1.4, 1.6–1.9, 5.4.1–5.4.3, 8.4, 9). F2 Arquitectura y datos, Arquitecto de Solución: meses 1–21 (2.1–2.6, 3.3, 3.7, 3.11). F3 Construcción E1, Líder de Desarrollo: meses 1–15 (3.4, 3.6.1–3.6.4, 3.10.1–3.10.3). F4 Construcción E2, Líder de Desarrollo: meses 13–20 (3.5, 3.6.5, 3.6.6, 3.10.4). F5 Plataforma, Líder de Operación / SRE: meses 1–15 (3.1, 3.2, 5.1–5.3, 6.1–6.6). F6 Calidad y pruebas, Líder de Calidad: meses 1–21 (1.5, 3.8, 3.9). F7 Implantación, Líder de Implantación: meses 9–21 (4.1–4.3, 7.1–7.3). F8 Operación, Líder de Operación / SRE: meses 21–56 (8.1–8.3, 8.5). Los hitos E-25 se señalan en los meses 2, 4, 6, 10, 12, 13, 14, 16, 17, 18, 19 y 21 (H1–H12, en el orden contractual, con H8 en el 14). Se sombrean los solapamientos de los meses 13–15 y 19–20. Fuente: elaboración propia a partir de los Formularios T-14 y T-15.

La figura muestra que en ningún mes trabaja un solo frente: entre los meses 1 y 15 avanzan a la vez la dirección, la arquitectura, la construcción de la Etapa 1, la plataforma y la calidad, y desde el mes 9 se suma la implantación. Los frentes se sincronizan en tres instancias. La primera son los hitos del Formulario E-25, porque cada hito exige que varios frentes entreguen a la vez. La segunda son los comités del Art. 71°: el de Proyecto es quincenal y los de Arquitectura y Operación son mensuales, y sus actas registran los acuerdos entre frentes en dos días hábiles (RT-19.09). La tercera son las ventanas de calendario, que son comunes a todos los frentes.

### Solapamientos de los meses 13 a 15 y 19 a 20

El Art. 17.2 obliga a dimensionar dotación y frentes para dos esfuerzos simultáneos. En los meses 13 a 15 trabajan a la vez el frente de implantación (F7), en la marcha blanca de la Etapa 1 con su acompañamiento; el de construcción de la Etapa 1 (F3), en las correcciones de esa marcha blanca; el de construcción de la Etapa 2 (F4), en su desarrollo, con el H8 en el mes 14; el de calidad (F6), en las pruebas de ambas etapas; y los frentes de dirección y de arquitectura (F1 y F2).

F3 y F4 dependen del mismo rol, el Líder de Desarrollo, pero son equipos distintos. Si el mismo equipo atendiera la marcha blanca y desarrollara la Etapa 2, cada incidente de la marcha blanca atrasaría la Etapa 2, que es precisamente la situación que el Art. 17.2 busca evitar. La Figura 7-frentes lo hace visible: en la franja sombreada de los meses 13 a 15, las barras de F3 y F4 coexisten en carriles separados.

En los meses 19 y 20 la Etapa 1 está en producción y la Etapa 2 en marcha blanca. Trabajan F7, en la marcha blanca de la Etapa 2; F4, en sus correcciones; F6, en las pruebas; y el soporte de la Etapa 1 en producción. La dotación de cada frente en cada solapamiento se presenta en el Formulario T-15, de modo que los dos esfuerzos se sumen sin contar dos veces a las mismas personas.

## 7.3 Cronograma e implantación

El cronograma aplica el Art. 17° mes a mes y la implantación aplica las condiciones del Caso 02 (secciones 13.3 y 17.6). Esta sección presenta la ruta crítica, la carta Gantt, el plan de implantación, las marchas blancas, la estabilización y el momento en que se alcanza cada resultado comprometido. El detalle está en los Formularios T-14, T-15 y T-18.

### Ruta crítica y holguras

La ruta crítica se calcula con el método de la ruta crítica sobre la red del Anexo 7.B (PMI, 2017, pp. 210–211). Una pasada hacia adelante da las fechas tempranas de cada paquete; una pasada hacia atrás, desde los meses fijos del Art. 17°, da las tardías; y su diferencia es la holgura. Como los hitos del Formulario E-25 son fechas fijas, un camino que no llega a su hito tiene holgura negativa y obliga a replanificar.

La cadena crítica nace en las interfaces sin documentación del sistema de gestión, que el caso señala expresamente (sección 17.5), y recorre la especificación de las interfaces (1.2.3), la integración con el ERP (3.3.2), los módulos de la Etapa 1 (3.4), las pruebas de integración (H4, mes 10), la certificación (H5, mes 12), la marcha blanca (H6, mes 13) y el paso a producción (H7, mes 16). La Figura 7-ruta ubica esa cadena y los caminos casi críticos sobre los meses del contrato.

**Figura 7-ruta — Ruta crítica y caminos casi críticos.** La cadena crítica representada enlaza: 1.2.3 Interfaces sin documentación (meses 1–4); 3.3.2 Integración con el ERP (meses 5–10, antes de H4); 3.4 Módulos de la Etapa 1 (meses 5–10, hasta H4); 3.8.1–3.8.7 Pruebas y certificación (meses 10–12, H4 a H5); 4.2.1 Marcha blanca E1 (meses 13–15); y 4.2.3 Paso a producción (H7, mes 16). La figura señala cuatro caminos casi críticos: sala técnica y sitios (diseño 2.3, hardware 5.1.2 y 6.1–6.6, terminan en H3); planificador (1.2.2, 3.4.7 M4 Rutas y R18-16); acuerdos con terceros (5.4.1 y 5.4.2, antes de ola 3); y cadenas del canal moderno (3.6.5 en meses 13–18 y 3.6.6 en 19–21). Las ventanas de marcha blanca están en los meses 13–15 y 19–20. Fuente: elaboración propia a partir del Anexo 7.B y de los períodos del Formulario T-14.

La figura muestra por qué la cadena es crítica: cada uno de sus tramos termina en el mismo mes del hito fijo que lo sigue. La especificación de las interfaces termina en el mes 4, junto con el H2; los módulos y la integración con el ERP terminan en el mes 10, junto con el H4; y las pruebas terminan en el mes 12, junto con el H5. A la resolución mensual del cronograma, la cadena no tiene holgura: un atraso en cualquiera de sus tramos traslada el riesgo a la marcha blanca, cuyas fechas no se mueven. Los caminos casi críticos son cuatro: la sala técnica, que debe estar recibida para el H3; la captura de las reglas del planificador, que alimenta el módulo de rutas; los acuerdos con los transportistas y el sindicato, que deben estar firmados antes de la ola de reparto; y la certificación de las cadenas, que debe terminar antes del mes 21.

La holgura se gestiona en las instancias de gobierno de la EDT. El avance de cada paquete de la ruta crítica y de los caminos casi críticos se revisa en la reunión semanal de seguimiento y en el Comité de Proyecto quincenal (paquetes 1.3.5 y 1.8.3). Toda desviación que comprometa un hito se escala al Comité Ejecutivo con su análisis de impacto (paquetes 1.4.3 y 1.8.2), y el informe mensual con valor ganado avisa toda desviación mayor al 10 % con su plan dentro de cinco días hábiles (paquete 1.8.6). Con las duraciones PERT de la sección 7.2.2 se calcula, además, la probabilidad de cumplir H5, H7, H10 y H12, conforme al método del Formulario T-15.

### Carta Gantt y calendario

La carta Gantt del Formulario T-14 cubre los 56 meses y muestra las marchas blancas, los pasos a producción y el inicio de la Operación. La tabla ubica los doce hitos del Formulario E-25 con el paquete que entrega cada uno.

**Hitos del Formulario E-25 en el cronograma.** Fuente: elaboración propia a partir del Formulario E-25 y del Formulario T-14.

| Hito | Mes | Entregable que lo gatilla | Paquetes |
|---|---:|---|---|
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

Los meses contractuales caen en meses calendario distintos según la fecha de inicio del contrato, que aún no está definida (consulta V-12). La tabla aplica la regla a los tres inicios que el Capítulo 3, sección 3.1.2, considera compatibles con poner la Etapa 2 en producción antes de enero de 2029, fecha desde la que rigen las condiciones de la principal cadena de supermercados.

**Meses contractuales según la fecha de inicio.** Fuente: elaboración propia a partir de las Bases Administrativas, Art. 17°, y del Caso 02, secciones 13.2 y 13.3.

| Inicio | Mes 13 (H6) | Mes 16 (H7) | Meses 19 y 20 | Mes 21 (H12) |
|---|---|---|---|---|
| Diciembre de 2026 | **Diciembre de 2027** | Marzo de 2028 | Junio y julio de 2028 | Agosto de 2028 |
| Febrero de 2027 | Febrero de 2028 | Mayo de 2028 | Agosto y **septiembre** de 2028 | Octubre de 2028 |
| Marzo de 2027 | Marzo de 2028 | Junio de 2028 | **Septiembre** y octubre de 2028 | Noviembre de 2028 |

Ningún inicio admisible deja las dos marchas blancas completas fuera de septiembre y diciembre; el Anexo 7.A extiende el análisis a los ocho meses de inicio admisibles. Con un inicio en diciembre de 2026, el inicio de la marcha blanca de la Etapa 1 cae en diciembre; con uno en marzo de 2027, el inicio de la marcha blanca de la Etapa 2 cae en septiembre. Con febrero de 2027, en cambio, el congelamiento afecta solo el segundo mes de la marcha blanca de la Etapa 2 y no un inicio, por lo que LafroX lo adopta como supuesto de calendario del cronograma. Su costo es que las semanas de cierre de esa marcha blanca coinciden con el peak de septiembre, que la sección 7.3.5 trata. Dentro de un mes de congelamiento no se inicia ninguna ola ni se despliega ningún cambio, y la marcha blanca continúa en convivencia, con medición diaria.

**Figura 7-gantt — Carta Gantt resumida de los 56 meses, con inicio en febrero de 2027.** El desarrollo E1 ocupa los meses 1–12; marcha blanca 13–15 (H6 en 13); producción 16–20 (H7 en 16). Desarrollo E2 ocupa 13–18 (H8 en 14, H9 en 17, H10 en 18); marcha blanca 19–20 (H11 en 19); producción y aceptación en el 21 (H12). Operación (36 meses) comienza en el 21 y continúa al 56 con hito mensual. La figura ubica también las fases de EDT: Inicio 1–2 y 13–14; Elaboración 2–4 y 13–14; Construcción 4–12 y 14–18; Transición 13–16 y 19–21; Adquisiciones 1–6 y continua/a demanda 7–20; Infraestructura 3–13; Capacitación 12–16, 17–21 y continua/a demanda 22–56; Operación 21–56; Cierre meses 21 y 56. Se sombrean septiembre y diciembre (meses contractuales 8, 11, 20, 23, 32, 35, 44, 47 y 56), sin pasos a producción en esos meses. Fuente: elaboración propia a partir de las Bases Administrativas, Art. 17°, del Formulario E-25 y del Formulario T-14.

La carta muestra que los periodos fijos del Art. 17° se respetan mes a mes y que ningún paso a producción cae en una columna de congelamiento: el mes 16 es mayo de 2028 y el mes 21, octubre de 2028. Las fases de desarrollo aparecen dos veces, una por etapa, y la capacitación continúa durante la operación por la rotación de la bodega. Las columnas rayadas del mes 20 y del mes 23 confirman lo que anticipa la tabla: el cierre de la marcha blanca de la Etapa 2 ocurre en septiembre y el primer diciembre de operación llega dos meses después de la aceptación final.

Antes de cada paso a producción, el cronograma reserva las pruebas que exige el numeral 20.1 de las Bases Técnicas Transversales: carga y estrés a 1,5 veces el peak, resiliencia, recuperación ante desastres con conmutación real, seguridad ofensiva y accesibilidad. Además, programa dos ensayos de migración antes de la migración definitiva. En la Etapa 1 estas pruebas forman la cuenta 3.8 y terminan en la certificación del mes 12; en la Etapa 2 forman la cuenta 3.9 y terminan en el mes 18.

### Plan de implantación y puesta en marcha

La implantación sigue el principio que impone el caso: nada entra en producción sin haber convivido con la forma actual de trabajar, y nada se despliega como un único evento (sección 13.3, condiciones 1 y 3). Técnicamente, cada capacidad se publica con un despliegue azul-verde y se habilita por sitio y por ola mediante interruptores de funcionalidad. Así, cada ola puede revertirse sin reinstalar y cada operación tiene un único escritor autorizado (Capítulo 4, sección 4.1.8). Ningún despliegue ocurre en la ventana de despacho de 05:30 a 07:00, que no admite indisponibilidad, ni en fechas de congelamiento (Caso 02, RT-10.05).

La Etapa 1 entra en tres olas, en el orden de las dependencias de datos (Capítulo 3, sección 3.4.4). La tabla las presenta.

**Olas de implantación de la Etapa 1.** Fuente: Capítulo 3, sección 3.4.4, y Formulario T-18.

| Ola | Procesos | Módulos | Avance | Registro oficial |
|---:|---|---|---|---|
| 1 | Datos maestros y recepción con lote | M1 | Por sitio | Recepciones y lotes |
| 2 | Inventario con FEFO y preparación nocturna | M2, M5 | Por sitio | Stock y preparación |
| 3 | Preventa, rutas, reparto, devoluciones y rendición | M3, M4, M6, M8, M7 | Por zona comercial | Pedidos, entregas y cobros |

Una ola avanza a la siguiente cuando cumple su criterio durante cuatro semanas consecutivas a volumen real: sin defectos críticos ni altos, con conciliación diaria sin diferencias no explicadas, con los indicadores de disponibilidad y tiempo de respuesta cumplidos, con los usuarios certificados y con el acta de la Contraparte Técnica (Capítulo 3, sección 3.4.4).

El calendario de las olas tiene una restricción que se deriva de las Bases. La marcha blanca dura unas 13 semanas (\(3 \times 52 / 12\)), y el Art. 17.3 exige que toda la Etapa 1 opere a volumen real en las últimas cuatro, las semanas 10 a 13. Si las olas fueran estrictamente secuenciales, la tercera empezaría en la semana 9 y debería entrar en todas sus zonas a la vez, lo que el caso prohíbe. Por eso la ola 3 empieza antes de que termine el período de criterio de la ola 2, adelantándose en lo que dure su avance por zonas y sin intervenir el mismo proceso que la ola 2 (Formulario T-18, sección 2.1). La Figura 7-olas muestra esa secuencia.

**Figura 7-olas — Secuencia de olas de la Etapa 1 durante la marcha blanca.** La escala comprende semanas 1–13, entre los meses 13, 14 y 15, con H6 al inicio y H7 en el mes 16. Ola 1 (M1, avance por sitio) cumple cuatro semanas de criterio en las primeras semanas y luego registra oficialmente en la solución, retirando el papel. Ola 2 (M2 y M5, avance por sitio) cumple cuatro semanas de criterio desde aproximadamente la semana 5 y luego pasa a registro oficial. Ola 3 (M3, M4, M6, M8 y M7, por zona) entra escalonadamente zona por zona antes de la semana 10; todas las zonas operan a volumen real durante las semanas 10–13, ventana exigida por Art. 17.3. Los rombos señalan las decisiones de avance según criterio. Fuente: elaboración propia a partir del Capítulo 3, sección 3.4.4, y del Formulario T-18.

La figura deja ver el margen real del calendario: la ola 1 y la ola 2 usan las primeras ocho semanas en cumplir su criterio, y la ola 3 entra zona por zona en la franja anterior a la semana 10, de modo que todas sus zonas operen a volumen real en las cuatro semanas de cierre. Cada rombo de avance es una decisión: si la ola no cumple su criterio, no avanza y se extiende el acompañamiento. La Etapa 2 se despliega por cadena y por grupo de usuarios; cada cadena entra al intercambio electrónico cuando su perfil está certificado y, hasta entonces, sus pedidos siguen con carga manual controlada, que no acredita el resultado comprometido (Formulario T-18, sección 3.1).

La reversión tiene dos niveles, que la tabla distingue.

**Niveles de reversión.** Fuente: Capítulo 3, sección 3.4.4; Capítulo 4, sección 4.1.8; y Formulario T-18.

| Nivel | Qué hace | Quién decide | Plazo |
|---|---|---|---|
| Técnico | Vuelve a la versión anterior por azul-verde o por interruptor de funcionalidad | Líder de Operación / SRE | Sin reinstalar, fuera de la ventana de despacho |
| Operacional, Etapa 1 | Vuelve a la hoja de picking y a la guía en papel | Responsable de operaciones del CLIENTE | Completo antes de las 05:30 |
| Operacional, Etapa 2 | Desactiva la capacidad de la Etapa 2 que falla, sin tocar la Etapa 1 | Responsable de operaciones del CLIENTE | Fuera de la ventana de 05:30 a 07:00 |

La reversión operacional se dispara con señales observables: pedidos sin sincronizar al inicio de la carga, rutas del día no disponibles o un defecto crítico en la ventana de despacho. El plazo de las 05:30 protege la salida de los 96 camiones y no es el tiempo de recuperación ante desastres. La Figura 7-reversion presenta el procedimiento por rol.

**Figura 7-reversion — Procedimiento de reversión E1 en ventana de despacho.** Durante el turno nocturno (22:00–05:30, antes del despacho 05:30–07:00), el Líder de Operación/SRE detecta la señal en monitoreo y el Líder de Implantación confirma el impacto. El responsable de operaciones del CLIENTE decide si amenaza el despacho. Si no, se corrige y la ola continúa. Si sí, se vuelve completamente al papel antes de 05:30: operacionalmente se usa hoja de picking y guía en papel; técnicamente se activa interruptor o versión anterior. Al retomar, se concilia lo que quedó en cola y la ola reinicia sus cuatro semanas. Fuente: elaboración propia a partir del Formulario T-18.

La figura muestra que la decisión es del CLIENTE y se toma en el turno de noche, antes de que empiece el despacho. No se pierde información: lo capturado queda en cola y se concilia al retomar. Lo que se pierde es el avance de la ola, que reinicia su período de cuatro semanas (Caso 02, sección 17.6, punto 4). La reversión se ensaya en Preproducción antes de cada corte (paquete 4.1.2), y en ese ensayo se mide el tiempo de cada nivel.

### Marcha blanca de la Etapa 1

La marcha blanca de la Etapa 1 son tres meses de operación supervisada con datos y usuarios reales, del mes 13 al 15. Convive con la operación vigente: en bodega, con la hoja de picking; en ruta, con la guía en papel; y en Talca, con el WMS de 2013 en solo lectura como respaldo de consulta. Cada día se concilian ambos registros, y toda diferencia se clasifica y explica antes del cierre del día (RT-20.03). La tabla presenta los indicadores que se miden y publican diariamente, con sus umbrales de cierre (RT-20.04).

**Indicadores diarios de la marcha blanca.** Fuente: Bases Administrativas, Art. 17.3; Caso 02, RT-09.01 y RT-10.05; y Capítulo 3, Tabla 3.5.

| Indicador | Umbral | Condición Art. 17.3 |
|---|---|---:|
| Incidentes críticos y altos abiertos | 0 | 1 |
| Transacciones de la ola registradas en la solución | 100 % del volumen real durante las 4 últimas semanas | 2 |
| Indisponibilidad en la ventana de 05:30 a 07:00 | 0 minutos | 3 |
| Disponibilidad de la transacción crítica | 99,9 % o más | 3 |
| Tiempo de respuesta, percentil 95 | Línea de preparación hasta 1 s; entrega hasta 2 s; línea de preventa hasta 1,5 s; stock y crédito hasta 2 s | 3 |
| Diferencias de conciliación sin explicar | 0 | 4 |
| Usuarios de la ola certificados | 100 % | 5 |

Los indicadores reproducen las condiciones del Art. 17.3 con umbrales que se pueden medir cada día, de modo que el cierre no depende de un juicio al final del período. El volumen comprometido es la operación real completa de cada proceso y no una muestra; con las cifras del caso (sección 14.1), son cerca de 1.150 recepciones de proveedor y 260.000 líneas de preparación al mes, unos 31.000 pedidos al mes y alrededor de 1.400 entregas por día hábil, o 2.600 si las semanas de cierre coinciden con el peak de septiembre. El detalle por proceso está en el Formulario T-18, Tabla T-18.1.

La sexta condición del Art. 17.3 es el acta de la Contraparte Técnica, que en la Etapa 1 es el H7 del mes 16. Si una condición no se cumple al término del mes 15, la marcha blanca se extiende a costo de LafroX, sin mover las fechas siguientes (Art. 17.3). La Figura 7-ciclo resume cómo opera cada día de marcha blanca y cuándo se cierra.

**Figura 7-ciclo — Ciclo diario y condiciones de cierre.** Cada día se repite el circuito: medición de indicadores → comparación con umbral → decisión de continuar, corregir o revertir → conciliación y publicación del día. El cierre requiere simultáneamente seis condiciones del Art. 17.3: cero incidentes críticos ni altos abiertos; volumen real durante las cuatro últimas semanas al 100 % del volumen comprometido; disponibilidad/desempeño (cero minutos de indisponibilidad en ventana, disponibilidad de 99,9 % o más); conciliación sin diferencias inexplicadas y cero pedidos perdidos; 100 % de usuarios de la ola capacitados y certificados; y acta de Contraparte Técnica (H7 en E1, H12 en E2). Ninguna condición compensa a otra. Fuente: elaboración propia a partir de las Bases Administrativas, Art. 17.3, y del RT-20.04.

El ciclo de la izquierda se repite cada día: se miden los indicadores, se comparan con su umbral y se decide entre continuar, corregir o revertir, antes de conciliar y publicar el resultado. La lista de la derecha muestra que el cierre exige las seis condiciones a la vez; ninguna compensa a otra.

La capacitación se hace en el puesto y en la ruta con las cuatro modalidades del Art. 90.2. Cada perfil se certifica antes del cierre, porque el Art. 17.3 exige que el personal del CLIENTE esté «capacitado y certificado conforme al plan de capacitación aprobado», y los usuarios administradores y el equipo técnico del CLIENTE se certifican además conforme al Art. 90.4. Los perfiles operativos, tomados del Capítulo 3, Anexo 3.I, son 120 preparadores, con un tutor por turno y un aprendizaje en el puesto de dos horas como máximo; 62 preventistas, en su propia ruta; 84 integrantes de la tripulación propia; y cerca de 160 conductores de transportistas, que se incorporan en el andén al asignarse a una ruta.

La adopción se mide por perfil y por ola, y si una ola no alcanza la meta, no avanza y se extiende el acompañamiento. La respuesta es distinta según el grupo: el personal con veinte o treinta años en la compañía recibe acompañamiento individual y reconocimiento formal de su conocimiento, y el personal rotativo de preparación cuenta con un tutor por turno (Formulario T-18, secciones 2.7 y 2.8).

### Marcha blanca de la Etapa 2 y convivencia

La marcha blanca de la Etapa 2 dura los meses 19 y 20 y convive con la Etapa 1 en producción. La regla central del Art. 17.2 es que exista una única fuente de verdad para los datos compartidos: la Etapa 2 lee y extiende los pedidos, clientes, guías y entregas de la Etapa 1, sin copiarlos ni digitarlos de nuevo, y ningún despliegue de la Etapa 2 modifica las funciones estabilizadas de la Etapa 1 ni ocurre en la ventana de despacho.

Esta marcha blanca dura unas 8,7 semanas (\(2 \times 52 / 12\)). Como el Art. 17.3 exige volumen real en las cuatro últimas, todas las cadenas certificadas, los portales y el costo de servir deben quedar habilitados en las primeras 4,7 semanas. Con el inicio supuesto de febrero de 2027, el mes 19 es agosto y el mes 20 es septiembre de 2028, de modo que toda habilitación ocurre en agosto, antes del congelamiento del 1 al 25 de septiembre. Las semanas de cierre se miden con el volumen del peak de Fiestas Patrias, cerca de 2.600 entregas diarias, en el primer septiembre de la Etapa 1 en producción. Durante el congelamiento, la única acción posible sobre la Etapa 2 es su reversión por interruptor de funcionalidad, sin instalar software. La capacidad para ese peak se demuestra antes del H11 con la prueba de carga a 1,5 veces el peak, con ambas etapas activas (paquete 3.9.3; Formulario T-18, sección 3.1).

A los indicadores de la tabla anterior se suman los propios del alcance de la Etapa 2: los pedidos de las cadenas certificadas recibidos por vía electrónica, los avisos de despacho dentro de dos minutos, las entregas con costo de servir calculado y la ausencia de degradación de los indicadores de la Etapa 1 (Formulario T-18, sección 3.3). La Figura 7-convivencia muestra cómo fluyen los datos entre ambas etapas.

**Figura 7-convivencia — Etapa 1 en producción y Etapa 2 en marcha blanca.** Los módulos E1 (M1 Recepción, M2 Inventario, M3 Preventa, M4 Rutas, M5 Preparación, M6 Reparto, M7 Cobranza y rendición, M8 Devoluciones y envases, M9 Calidad y trazabilidad, M10 Analítica [indicadores y OTIF], M12 Telemetría) escriben en el registro único de la plataforma: clientes, pedidos, guías de despacho, entregas, lotes y cobros, con un solo escritor por dato y sin copias. E2 (M11 Canal moderno, Portal de clientes, Portal de transportistas y M10 Analítica: costo de servir) lee ese registro y lo extiende. El ERP se conecta como registro contable y único emisor de la guía de despacho. Ningún despliegue de E2 modifica una función estabilizada de E1. Fuente: elaboración propia a partir de la arquitectura lógica del Capítulo 4.

La figura muestra que la Etapa 2 no tiene un segundo registro de los datos de la Etapa 1: lee el registro único y lo extiende con sus propios datos, de modo que no existe una doble digitación que conciliar. El ERP se mantiene como registro contable y único emisor de la guía de despacho para ambas etapas. El paso a producción del mes 21 es la aceptación final de la implementación (H12) y el inicio de la Operación con ambos alcances (Art. 17.2, punto 4).

### Estabilización y transferencia

Después de cada paso a producción hay una estabilización de cuatro semanas por ola, con atención reforzada y sin costo adicional (RT-20.06). La dotación se deriva de la operación del caso, como muestra la tabla.

**Estabilización por ola.** Fuente: Capítulo 3, sección 3.4.4.

| Frente | Personas | Cálculo |
|---|---:|---|
| Bodega, turno de noche | 2 | 1 por centro de distribución |
| Plataformas de cross-docking | 3 | 1 por plataforma |
| Calle | 7 | 158 rutas diarias / 24 días de lunes a sábado ≈ 6,6 |
| Coordinación | 1 | Líder de Implantación y Gestión del Cambio |

Las siete personas de calle permiten acompañar cada una de las 158 rutas diarias (96 camiones y 62 preventistas) al menos una vez en las cuatro semanas. Si la ola cubre una sola zona, la dotación se reduce en proporción a sus rutas, y la dotación decrece según la curva de adopción, como exige el RT-20.05.

La operación se transfiere al equipo de TI de cuatro personas del CLIENTE antes del mes 21, con procedimientos documentados y ensayados y con la base de conocimiento. Sigue una mentoría de seis meses (paquetes 7.1.4 y 8.5.2; RT-22.07). Quedan como servicio permanente de LafroX durante los 36 meses los que el Capítulo 3, sección 3.4.5, le asigna: el centro de operaciones, la mesa de servicio, la gestión de incidentes, la continuidad, la seguridad y el mantenimiento.

### Momento de los resultados comprometidos

El Caso 02 exige indicar en qué momento del cronograma se alcanza cada resultado de aceptación (capítulo 18). La tabla agrupa los dieciséis resultados por momento; el detalle por resultado está en el Anexo 7.C.

**Momento de los resultados de aceptación del caso.** Fuente: Caso 02, capítulo 18; Capítulo 3, Anexo 3.J; y Anexo 7.C.

| Momento | Resultados | Cant. | Aceptación |
|---|---|---:|---|
| Marcha blanca de la Etapa 1 (meses 13 a 15) | R18-01, 02, 03, 05, 06, 07, 08, 09, 10, 14, 15 y 16 | 12 | H7 (mes 16) |
| Marcha blanca de la Etapa 2 (meses 19 y 20) | R18-11 y 13 | 2 | H12 (mes 21) |
| Tramos durante el contrato | R18-04: OTIF de 90 % en el mes 15, 93 % en el mes 19 y 95 % en el mes 32 | 1 | Revisión mensual en comité |
| Provisional y final | R18-12: provisional en la marcha blanca de la Etapa 1 y final tras 12 meses de operación | 1 | H7 y operación |

Doce de los dieciséis resultados se verifican en la marcha blanca de la Etapa 1. Por eso el volumen real y la certificación de usuarios de ese período son la principal concentración de riesgo de aceptación del proyecto, y por eso el plan dedica a esa marcha blanca su mayor dotación de acompañamiento.

Las innovaciones también tienen su momento en el cronograma (Art. 29°, punto 4), como resume la tabla.

**Innovaciones en el cronograma.** Fuente: Anexo 7.D.

| Innovación | Paquetes de la EDT | Meses | Hito |
|---|---|---|---|
| 1 · Seguimiento de vencimiento posentrega | 3.10.1.1 a 3.10.1.4 | 7 a 15 | H4, H5 y marcha blanca E1 |
| 2 · Reproducción de incidentes de terreno | 3.10.2.1 a 3.10.2.4; 8.3.1 | 2 a 15; 21 a 56 | H4 y marcha blanca E1 |
| 3 · Vida útil remanente por historia térmica | 3.10.3.1 a 3.10.3.4; 8.3.2 | 3 a 15; operación | H4, H5 y marcha blanca E1 |
| 4 · Tramo variable ligado al costo de servir | 5.4.3; 8.3.3; 8.3.4 | 17 a 20; 21 a 23; 24 a 56 | Hito mensual |
| 5 · Hoja de negocio del almacenero | 3.10.4.1 a 3.10.4.4; 8.3.5; 8.3.6 | 13 a 27 | H9, H10 y H12 |

Tres innovaciones se validan en la marcha blanca de la Etapa 1. La innovación 5 sigue el calendario de la Etapa 2, y la innovación 4 empieza a liquidar recién desde el mes 24, después de una línea base y tres liquidaciones en sombra. Así, ninguna innovación agrega trabajo a la ruta crítica de la Etapa 1 después del H4.

### Referencias

Las Bases se citan con su documento y el artículo, capítulo, sección o código del requisito; las referencias internas a otros capítulos de esta oferta se indican por su número de capítulo y sección.

- Distribuidora Puelche S.A. (2026a). *Bases Administrativas de Licitación N.º TFEP-01/2026: Contratación de Solución Integral de Software y Servicios de Operación*.
- Distribuidora Puelche S.A. (2026b). *Bases Técnicas Transversales de Licitación N.º TFEP-01/2026*.
- Distribuidora Puelche S.A. (2026c). *Caso 02: Logística. Especificaciones del problema y operación de Distribuidora Puelche S.A.*
- Distribuidora Puelche S.A. (2026d). *Aclaraciones de la Licitación N.º TFEP-01/2026*.
- Malcolm, D. G., Roseboom, J. H., Clark, C. E., & Fazar, W. (1959). Application of a technique for research and development program evaluation. *Operations Research, 7*(5), 646–669.
- Project Management Institute. (2017). *La guía de los fundamentos para la dirección de proyectos (Guía del PMBOK®)* (6.ª ed.). Project Management Institute.

### Declaración de uso de IA

En cumplimiento de la sección 7.2 de las Aclaraciones de la licitación, la tabla declara el uso de herramientas de inteligencia artificial en este subdocumento, en sus anexos y en sus formularios. Esta declaración se consolida en el Formulario A-6.

**Declaración de uso de IA.** Fuente: registro del equipo.

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana |
|---|---|---|---|---|---|
| Introducción | Claude Code | Redacción a partir de las Bases y de los capítulos de la oferta | Alto | Ninguno | No documentada |
| 7.1 EDT | Claude Code | Redacción, conteos desde la EDT del equipo y figuras de la EDT | Alto | Alto | No documentada |
| 7.2 Plan de trabajo | Claude Code | Redacción del secuenciamiento y de los frentes; red y carriles | Alto | Alto | No documentada |
| 7.3 Cronograma e implantación | Claude Code | Redacción, calendario por fecha de inicio, Gantt y flujos | Alto | Alto | No documentada |
| Anexos 7.A a 7.E | Claude Code | Listados y cálculo del calendario | Alto | Ninguno | No documentada |
| Formulario T-14 | Claude Code | Diccionario a partir del diccionario de trabajo del equipo; Gantt por cuenta | Alto | Alto | No documentada |
| Formulario T-15 | Claude Code | Estructura, método y frentes | Alto | Alto | No documentada |
| Formulario T-18 | Claude Code | Redacción a partir del Capítulo 3 y del caso | Alto | Alto | No documentada |
