# Propuesta Técnica — Subdocumento 6: Metodologías

**Licitación:** TFEP-01/2026  
**Proyecto:** Plataforma Digital de Misión Crítica — Caso 02: Logística  
**Mandante:** Distribuidora Puelche S.A.  
**Proponente:** LafroX SpA — RUT 77.418.902-K  
**Representante legal:** Alex Aravena, Jefe de Proyecto y Apoderado  
**Fecha de emisión:** 5 de octubre de 2026  
**Formularios:** T-9 y T-10

## Índice

- [Introducción a las Metodologías](#introducción-a-las-metodologías)
  - [6.1 Metodología de Gestión de Proyectos](#61-metodología-de-gestión-de-proyectos)
    - [6.1.1 Gestión de interesados](#611-gestión-de-interesados)
    - [6.1.2 Gestión de comunicaciones](#612-gestión-de-comunicaciones)
    - [6.1.3 Gestión de adquisiciones](#613-gestión-de-adquisiciones)
    - [6.1.4 Gestión de integración](#614-gestión-de-integración)
    - [6.1.5 Control del alcance, del cronograma y del valor ganado](#615-control-del-alcance-del-cronograma-y-del-valor-ganado)
    - [6.1.6 Mecanismos de decisión y cadencias de gobierno](#616-mecanismos-de-decisión-y-cadencias-de-gobierno)
  - [6.2 Metodología de Desarrollo Software](#62-metodología-de-desarrollo-software)
    - [6.2.1 Arquitectura evolutiva, refactorización y deuda técnica](#621-arquitectura-evolutiva-refactorización-y-deuda-técnica)
    - [6.2.2 DevSecOps, integración y entrega continuas, infraestructura como código y pruebas automatizadas](#622-devsecops-integración-y-entrega-continuas-infraestructura-como-código-y-pruebas-automatizadas)
    - [6.2.3 Ceremonias, cadencias y decisiones del desarrollo](#623-ceremonias-cadencias-y-decisiones-del-desarrollo)

# Introducción a las Metodologías

Este capítulo define cómo LafroX dirige el proyecto y cómo construye el software. La sección 6.1 adapta el PMBOK a un proyecto de 56 meses con dos etapas, solapamiento entre ellas y una operación que no puede detenerse; la sección 6.2 organiza el desarrollo con RUP iterativo y prácticas DevSecOps. Ambas metodologías se aplican en el plan de trabajo del SD7: la EDT del Formulario T-14 contiene los paquetes de gobierno, calidad y control que aquí se describen, y el Formulario T-15 programa sus cadencias. Las herramientas y compuertas de la cadena de entrega son las de la arquitectura del SD4, sección 4.2. Los Formularios T-9 y T-10 adjuntan, respectivamente, las secciones 6.1 y 6.2.

## 6.1 Metodología de Gestión de Proyectos

La gestión del proyecto aplica la Guía del PMBOK, sexta edición (PMI, 2017), adaptada a la complejidad del proyecto: se usan los procesos de integración, alcance, cronograma, calidad, recursos, comunicaciones, riesgos, adquisiciones e interesados, con la profundidad que exige cada uno. La adaptación tiene tres rasgos. Primero, el alcance y el cronograma tienen líneas base formales, porque los hitos del Formulario E-25 son fechas fijas y se aceptan por acta. Segundo, el avance se mide con valor ganado y no con porcentajes declarados (RT-19.07). Tercero, el flujo diario del equipo se gestiona con un tablero Kanban, un enfoque ágil que no reemplaza la línea base ni la aceptación formal de los entregables.

La planificación define los entregables, sus responsables, los recursos, los plazos y las dependencias entre actividades, considerando las restricciones de la operación. La línea base de alcance (paquete 1.2.1, H1) y la de cronograma (1.3.3) sirven para medir el avance y evaluar las desviaciones.

El proyecto se ejecuta mediante entregas incrementales dentro de las dos etapas contractuales. La distribución propuesta prioriza primero la calidad y disponibilidad de la información operacional, y luego las capacidades que dependen de esos datos para optimizar y analizar la operación. En la Etapa 1 se implementan las capacidades de preventa, recepción, bodega, preparación y cross-docking, incluida la reposición de compras. Se incorporan la trazabilidad de los lotes y de la cadena de frío, la planificación de rutas basada en el conocimiento del planificador, la captura de la evidencia de entrega y del acuse de recibo de la guía de despacho que registra el ERP, el manejo de efectivo y el retiro sanitario de lotes. En la Etapa 2 se implementan los portales y el intercambio electrónico con los clientes y, por último, el costo de servir.

La planificación respeta el cronograma contractual: desarrollo de la Etapa 1 entre los meses 1 y 12, marcha blanca entre los meses 13 y 15 y paso a producción en el mes 16. El desarrollo de la Etapa 2 ocupa los meses 13 a 18, la marcha blanca los meses 19 y 20 y el paso a producción el mes 21. El trabajo de la Etapa 2 se coordina con la marcha blanca y la estabilización de la Etapa 1, resguardando la continuidad operacional y la integridad de los datos compartidos.

El tablero Kanban muestra el trabajo pendiente, en ejecución, en revisión y terminado, con responsables y bloqueos, y fija límites de trabajo en curso. Cada tarea tiene una definición de terminado y, cuando corresponde, evidencia asociada a los criterios de aceptación del entregable al que contribuye. La gestión del proyecto se complementa con los procesos de los apartados siguientes.

### 6.1.1 Gestión de interesados

La gestión de interesados identifica a las personas, grupos y organizaciones que pueden influir en el proyecto o verse afectados por sus resultados. Para cada interesado se registran sus necesidades, expectativas, nivel de influencia, impacto potencial y disposición frente a los cambios. El análisis distingue quiénes participan en decisiones, quiénes aportan conocimiento operacional, quiénes validan entregables y quiénes son afectados o ejercen supervisión externa.

El jefe de proyecto mantiene actualizado el registro de interesados (paquete 1.4.1) y planifica su involucramiento de acuerdo con el alcance de cada entrega. La participación puede incluir levantamiento de necesidades, revisión de procesos, validación de criterios, pruebas y retroalimentación. Las inquietudes, resistencias, acuerdos y compromisos relevantes se registran con su responsable y seguimiento; los conflictos que no puedan resolverse en la instancia de trabajo se elevan a la autoridad correspondiente.

**Tabla 6.1. Interesados del proyecto — Fuente: elaboración propia**

| Interesado | Interés o preocupación | Contribución esperada |
|---|---|---|
| Gerencia general | Continuidad del negocio y relación con clientes | Aportar prioridades del negocio y resolver decisiones que requieran su intervención |
| Jefatura de calidad | Trazabilidad de lotes y control de temperatura | Definir y revisar reglas de control sanitario y evidencia de trazabilidad |
| Autoridades sanitarias | Disponibilidad y confiabilidad de la evidencia de trazabilidad | Informar exigencias aplicables y revisar antecedentes cuando corresponda |
| Planificador de rutas | Preservar el conocimiento operacional | Documentar restricciones y reglas de planificación, y participar en su validación |
| Gerencia comercial | Cumplimiento de la promesa de entrega e información confiable | Aportar y validar políticas comerciales, procesos de preventa y necesidades de servicio |
| Cadenas de supermercados | Recepción completa y oportuna de pedidos e intercambio electrónico | Participar en la definición y validación de los flujos de aviso de despacho y evidencia de entrega |
| Clientes del canal tradicional | Recepción correcta de pedidos, pagos y atención | Aportar retroalimentación sobre recepción, comprobantes y atención |
| Clientes de food service | Frescura, puntualidad y evidencia térmica de la entrega | Validar sus ventanas de entrega y la evidencia térmica del viaje |
| Preventistas | Consulta de stock y crédito, y registro confiable de pedidos | Participar en el levantamiento y prueba de los flujos de preventa y cobranza |
| Sindicato de conductores | Condiciones de trabajo y uso de tecnologías | Canalizar inquietudes y aportar observaciones sobre los cambios que afecten a los conductores |
| Conductores propios | Registro de entregas, devoluciones y cobros | Participar en pruebas de ruta y validar la usabilidad de los dispositivos |
| Jefatura de bodega | Preparación, despacho y control de inventario | Aportar y validar procedimientos, excepciones y condiciones de operación |
| Preparadores de pedidos | Claridad de instrucciones y adecuación de los dispositivos | Participar en pruebas de los flujos de preparación de pedidos |
| Gerencia de operaciones | Continuidad del despacho y cumplimiento de entregas | Aportar prioridades operacionales y validar procedimientos y cambios que afecten la operación |
| Administración y finanzas | Control de cobros, conciliación y costos de servir | Definir y validar reglas de rendición, conciliación e indicadores financieros |
| Equipo de TI | Integración con sistemas existentes y mantenibilidad de la solución | Coordinar accesos e integraciones, y revisar documentación y transferencia de conocimiento |
| Empresas transportistas | Asignación de conductores y vehículos, y uso de terminales | Firmar el acuerdo operacional y confirmar conductor y vehículo antes del despacho |
| Conductores de transportistas externos | Acceso a la solución y registro de actividades de reparto | Participar en pruebas de los flujos que les correspondan y aportar observaciones de uso |
| Proveedores | Intercambio de información de productos, lotes, despacho y órdenes de compra | Coordinar formatos de intercambio y participar en pruebas de recepción, trazabilidad y del portal de proveedores |

La tabla agrupa los diecinueve actores del Subdocumento 2, Anexo 2.3, con sus intereses y la contribución esperada; las gerencias y jefaturas se nombran por su área. La participación concreta se acuerda según las responsabilidades de cada interesado y las actividades de cada entrega; la inclusión en la tabla no implica que todos participen en todas las decisiones ni que tengan atribuciones de aprobación.

### 6.1.2 Gestión de comunicaciones

La gestión de las comunicaciones mantiene informados a los responsables de Puelche y a los demás interesados sobre los avances de las entregas que les competen, sostiene una comprensión común del estado del proyecto, facilita la toma de decisiones y comunica oportunamente las situaciones que puedan afectar los compromisos acordados.

Las reuniones convocan a las personas necesarias para analizar y resolver sus asuntos. Los acuerdos se registran en actas que identifican las decisiones, las actividades pendientes, sus responsables y los plazos; las actas de los comités se levantan dentro de los dos días hábiles siguientes (RT-19.09). La documentación vigente, los entregables, las actas y los registros de riesgos y de cambios se mantienen en el espacio colaborativo accesible al CLIENTE (RT-19.05).

Antes de cada entrega incremental se informa a los interesados pertinentes sobre los cambios previstos, las actividades de validación y el apoyo necesario para la puesta en funcionamiento. Las observaciones se registran y reciben respuesta, distinguiendo las que pueden atenderse dentro de lo acordado de las que requieren una solicitud de cambio.

**Tabla 6.2. Comunicación del proyecto — Fuente: elaboración propia**

| Comunicación | Responsable de comunicar | Destinatarios | Frecuencia o momento |
|---|---|---|---|
| Seguimiento de actividades, compromisos y bloqueos | Jefe de proyecto | Equipo de proyecto y contrapartes involucradas | Semanal |
| Avance de entregables, desviaciones y riesgos | Jefe de proyecto | Comité de Proyecto | Quincenal; registro de riesgos revisado en cada sesión |
| Informe mensual de avance con valor ganado (SPI y CPI) | Jefe de proyecto | Comité Ejecutivo y Contraparte Técnica | Mensual (RT-19.06 y RT-19.07) |
| Niveles de servicio, incidentes y capacidad en producción | Líder de Operación / SRE | Comité de Operación | Mensual, desde el mes 13 |
| Cambios previstos, validaciones y apoyo | Jefe de proyecto | Interesados pertinentes | Antes de cada entrega |

La Tabla 6.2 muestra que el Jefe de Proyecto concentra cuatro de las cinco comunicaciones y que la frecuencia crece hacia el equipo: semanal para el seguimiento, quincenal para el Comité de Proyecto y mensual para la dirección del CLIENTE. La única comunicación a cargo del Líder de Operación / SRE comienza en el mes 13, con la primera marcha blanca, porque desde entonces hay niveles de servicio que informar.

### 6.1.3 Gestión de adquisiciones

La gestión de adquisiciones planifica, contrata y controla los bienes y servicios que requiere la solución: contratos, órdenes de compra, acuerdos con terceros y acuerdos de nivel de servicio. Cada adquisición tiene un responsable, una fecha de necesidad derivada del cronograma, una dependencia con los paquetes que la usan y una evidencia de recepción.

El CLIENTE compra solo el equipamiento de terreno conforme a la especificación de LafroX (Caso 02, capítulo 11; SD3 E-09; paquete 5.1.1). LafroX provee, instala, integra y mantiene la sala técnica, los racks, los servidores, el almacenamiento, los firewalls, los switches, los servidores de Concepción, los mini-PC de borde y los gabinetes dentro del precio del contrato (Bases Administrativas, art. 14.2). Su especificación y compra corresponden al paquete 5.1.2 y su valorización se incluye en la Oferta Económica (art. 50.2). La obra civil de separación es de cargo del CLIENTE y LafroX la especifica y coordina (RT-06.06). El piso técnico, la energía, la climatización y los sistemas de incendio son provistos por LafroX. La recepción se acredita con las actas 5.1.3 y 6.1.5. Las licencias de terceros se constituyen a nombre del CLIENTE (5.2.3).

**Tabla 6.3. Adquisiciones — Fuente: elaboración propia a partir del Formulario T-14, fase 5, y del Formulario T-11**

| Bien o servicio | Necesidad asociada | Responsable del contrato / de LafroX | Fecha de necesidad | Paquetes que dependen y evidencia |
| --- | --- | --- | --- | --- |
| Equipamiento de terreno: terminales de preventa, reparto y bodega, impresoras, sensores de temperatura, termógrafos y gateways IoT | Operación de las aplicaciones y registro de frío | CLIENTE, según la especificación 5.1.1 / Arquitecto (especificación); SRE (recepción) | Antes de cada ola; sensores antes de 6.5 | 6.5, 4.2.1; Actas 5.1.3 |
| Sala técnica de Talca: UPS, generador, transferencia automática, climatización de precisión, detección y extinción | Recinto técnico del H3 | LafroX, especificación y compra 5.1.2 / Arquitecto (especificación); SRE (recepción) | Mes 3 | 6.1; Actas 5.1.3 y 6.1.5 |
| Servidores, almacenamiento, firewalls y switches de Talca y Concepción | Cómputo y red de los CD | LafroX, especificación y compra 5.1.2 / SRE | Mes 4 | 6.3, 6.6; Actas 5.1.3 |
| Racks R01/R02 y gabinete de borde de Concepción | Montaje del cómputo y las comunicaciones | LafroX, especificación y compra 5.1.2 / SRE | Racks: meses 4 y 5; gabinete de Concepción: mes 4 | 6.3.1 a 6.3.3; Actas 5.1.3 |
| Mini-PC y gabinetes de borde de cross-docking | Cómputo local de las plataformas | LafroX, especificación y compra 5.1.2 / SRE | Mes 9 | 6.3.4; Actas 5.1.3 |
| Obra civil de separación | Separación del recinto técnico | CLIENTE; LafroX la especifica y coordina (RT-06.06) / SRE | Mes 3 | 6.1.1; Acta 6.1.5 |
| Piso técnico, energía, climatización e incendio | Habilitación del recinto | LafroX, con instaladores especializados / SRE | Mes 3 | 6.1.1 a 6.1.4; Actas 5.1.3 y 6.1.5 |
| Servicios de AWS | Plataforma de nube y ambientes | LafroX (5.2.1) / SRE | Antes del mes 4 | 3.1, 3.2; Cuentas y servicios activos |
| Gestión de dispositivos y detección en endpoints | Enrolamiento y seguridad de los terminales | LafroX (5.2.2) / SRE | Antes del enrolamiento | 6.5, 7.1; Suscripciones activas |
| Licencias de software de terceros | Productos de la arquitectura | A nombre del CLIENTE (5.2.3) / Arquitecto | Antes de usar cada producto | 3.1 a 3.6; Registro de licencias |
| Fibra óptica de Talca y Concepción | Enlace principal | LafroX (5.3.1) / SRE | Antes del H3 | 6.6; Contrato y fecha de instalación |
| Planes LTE: dos proveedores; ocho planes | Respaldo de enlace: uno por CD y dos por plataforma de cross-docking | LafroX (5.3.2) / SRE | Antes del H3 | 6.6; Contratos |
| Starlink de los cinco sitios: Talca, Concepción y las tres plataformas | En los CD, tercer camino en espera caliente detrás de fibra y LTE; en cross-docking, enlace principal | LafroX (5.3.3) / SRE | Antes del H3 | 6.6; Contratos y equipos |
| Acuerdos con los diez transportistas | Uso de terminales y suplentes enrolados | LafroX con el CLIENTE (5.4.1) / Implantación | Antes del H6 | 4.2.1, ola de reparto; Diez acuerdos firmados |
| Acta con el sindicato | Terminales, GPS y cámaras | CLIENTE y sindicato (5.4.2) / Implantación | Antes del H6 | 4.2.1; Acta firmada |
| Custodia de fuentes | Continuidad ante insolvencia o incumplimiento | LafroX (5.4.4) / Jefe de proyecto | Antes del H4 | 9.2; Contrato y primer depósito |
| Evaluadores de pruebas subcontratados | Refuerzo de calidad durante las certificaciones, hasta 16 personas por día | LafroX / Líder de Calidad | Meses 9 a 12 y 16 a 18 | 3.8.2 a 3.8.8 y 3.9.2 a 3.9.7; Contrato con perfiles y disponibilidad por quincena |
| Servicio SOC 24×7, si se subcontrata | Monitoreo de seguridad desde el mes 13 | LafroX (8.1.5; RT-11.17) / Encargado de Seguridad | Mes 13 | 8.1.5; Contrato con cobertura y niveles de servicio |

Cada fila tiene en el registro de adquisiciones su estado, su proveedor y su fecha comprometida. Un atraso que amenace el H3 o una ola se escala al Comité Ejecutivo con su análisis de impacto.

### 6.1.4 Gestión de integración

La gestión de integración mantiene alineados los componentes del proyecto para que las decisiones sobre alcance, cronograma, costos, recursos, calidad, riesgos y adquisiciones se analicen de manera coordinada. El jefe de proyecto consolida estos elementos en el plan para la dirección del proyecto, lo comunica a los responsables y lo actualiza cuando se aprueban cambios.

Durante la ejecución, el jefe de proyecto coordina las actividades y sus dependencias, revisa el avance de los entregables y gestiona los impedimentos que afectan a más de un equipo o área. Las decisiones, acuerdos, riesgos transversales y asuntos que requieran escalamiento quedan registrados con su responsable, resolución y fecha de seguimiento.

Toda solicitud de cambio que pueda afectar el alcance, los plazos, los costos o los criterios de aceptación se documenta y evalúa antes de implementarla. El análisis considera sus efectos en el plan, los entregables relacionados, los riesgos y la operación. El jefe de proyecto eleva la solicitud a la autoridad correspondiente de Puelche y comunica la decisión a las personas afectadas. Solo los cambios aprobados se incorporan a la planificación vigente. Las acciones correctivas destinadas a cumplir los compromisos aprobados se registran y supervisan; si modifican esos compromisos, se tramitan además como solicitudes de cambio.

Al finalizar cada entrega se comprueba que sus resultados satisfagan los criterios de aceptación y cuenten con la evidencia requerida. Las observaciones pendientes se registran con responsable y tratamiento acordado, y se documentan las lecciones aprendidas.

### 6.1.5 Control del alcance, del cronograma y del valor ganado

El alcance se controla contra la línea base y la matriz de trazabilidad del Formulario T-12: un requerimiento sólo se da por cumplido cuando pasa la prueba asignada en el paquete que lo construye. El cronograma se controla contra la red del Formulario T-15, sección 5, que incluye los diez días hábiles de revisión del CLIENTE antes de cada hito (Art. 18.3).

El avance se mide con valor ganado (RT-19.07). El valor planificado de cada mes es la suma de las horas hombre programadas de los paquetes en curso según el Formulario T-15; el valor ganado acredita las horas de un paquete sólo en hitos de avance definidos de antemano (inicio, revisión interna y aceptación) y no por porcentaje declarado; el costo real son las horas registradas. Con ellos se calculan el índice de desempeño del cronograma (SPI) y el del costo (CPI). Un SPI o un CPI bajo 0,90, o una desviación mayor al 10 %, obligan a presentar un plan de recuperación dentro de cinco días hábiles (paquete 1.8.6).

La Tabla 6.4 aplica el cálculo al corte del H4 (mes 10). El valor planificado acumulado es la suma de las horas de los meses 1 a 10 de la curva del Formulario T-15, sección 4.4; el valor ganado y el costo real son un ejemplo de avance que ilustra cómo se lee el informe mensual.

**Tabla 6.4. Ejemplo de cálculo del valor ganado al corte del mes 10 — Fuente: elaboración propia a partir del Formulario T-15, sección 4.4**

| Indicador | Fórmula | Valor | Lectura |
| --- | --- | --- | --- |
| Valor planificado (PV) | Σ HH de los meses 1 a 10 (1.416 + 2.910 + 2.122 + 3.383 + 4.079 + 5.925 + 4.964 + 4.695 + 3.392 + 2.121) | 35.006 HH | Trabajo que el plan prevé terminado al mes 10 |
| Valor ganado (EV) | HH de los hitos de avance aceptados | 33.256 HH | Ejemplo: 95 % del trabajo planificado |
| Costo real (AC) | HH registradas | 34.300 HH | Ejemplo de horas efectivamente imputadas |
| SPI | EV / PV = 33.256 / 35.006 | 0,95 | Atraso del 5 %, sobre el umbral de 0,90 |
| CPI | EV / AC = 33.256 / 34.300 | 0,97 | Se usan 3 % más horas que las ganadas |

Con estos valores ningún índice cruza el umbral de 0,90, pero el SPI de 0,95 a un mes del H4 obliga a revisar en el Comité de Proyecto los paquetes que lo explican y su efecto sobre los 19 días hábiles de reserva del hito (Formulario T-15, Tabla 5.2). La amenaza se escala cuando la desviación proyectada supera la mitad de esa reserva.

Las reservas se controlan por separado: la capacidad protegida de la Etapa 1 y las necesidades de contingencia del SD8 sólo se usan con autorización registrada, y su consumo se informa en el mismo informe mensual.

### 6.1.6 Mecanismos de decisión y cadencias de gobierno

Los comités del Art. 71° de las Bases Administrativas tienen las cadencias de la Tabla 6.5.

**Tabla 6.5. Instancias de gobierno y cadencias — Fuente: elaboración propia a partir de las Bases Administrativas, Art. 71°, y del Formulario T-14, cuenta 1.8**

| Instancia | Frecuencia | Participantes | Decide o revisa | Paquete |
|---|---|---|---|---|
| Reunión de seguimiento | Semanal | Jefe de proyecto y líderes de frente | Avance, bloqueos y datos para los comités; no reemplaza a ningún comité | 1.3.5 |
| Comité de Proyecto | Quincenal | Jefe de proyecto, líderes y Contraparte Técnica | Avance de entregables y registro vivo de riesgos (RT-19.04) | 1.8.3 |
| Comité Ejecutivo | Mensual | Gerencias del CLIENTE y dirección de LafroX | Escalamientos, cambios de alcance o plazo y uso de reservas | 1.8.2 |
| Comité de Arquitectura | Mensual | Arquitecto de Solución, Seguridad y TI del CLIENTE | Decisiones de arquitectura y su registro | 1.8.4 |
| Comité de Operación | Mensual, desde el mes 13 hasta el mes 56 | Líder de Operación / SRE, mesa de servicio, Operaciones y TI del CLIENTE | Niveles de servicio, incidentes y problemas, capacidad de la mesa, pruebas de continuidad y plan de mejoras | 1.8.5 |

El Comité de Operación empieza con la primera marcha blanca, porque desde entonces la solución atiende operaciones reales. Revisa cada mes la disponibilidad de los servicios críticos, los incidentes críticos y altos y sus causas, la atención de la mesa (respuesta antes de 20 segundos, abandono y resolución al primer contacto), las pruebas de restauración y de continuidad y los cambios programados. Sus actas registran acuerdos, responsables y plazos (RT-19.09).

## 6.2 Metodología de Desarrollo Software

La metodología de desarrollo se coordina con la gestión del proyecto y con sus entregas incrementales. Se utiliza **Rational Unified Process (RUP)**, un proceso iterativo e incremental que organiza el desarrollo en cuatro fases y permite gestionar requisitos, arquitectura, implementación y pruebas de manera progresiva. Su elección se basa en que el proyecto tiene requisitos regulatorios y de continuidad que exigen una arquitectura validada temprano, documentación trazable y entregas formales por etapa, sin renunciar a iteraciones cortas que reduzcan el tiempo hasta disponer de software verificable.

RUP se organiza en las siguientes fases:

1. **Inicio:** se delimitan el alcance y los objetivos de la solución, se identifican los principales interesados y requisitos y se elaboran las estimaciones iniciales. También se reconocen los riesgos principales y se establece una visión inicial del producto.
2. **Elaboración:** se profundizan los requisitos, incluidos los casos de uso, y se define la arquitectura de la solución. Se analizan los riesgos prioritarios y se prepara el plan de desarrollo, de modo que las decisiones de diseño más relevantes se validen antes de construir. Los prototipos con usuarios terminan antes de construir cada módulo.
3. **Construcción:** se desarrollan las capacidades priorizadas mediante iteraciones. En cada iteración se analizan los requisitos correspondientes, se diseña e implementa la solución y se realizan pruebas. Los resultados se revisan con los interesados pertinentes y se ajustan cuando corresponde.
4. **Transición:** se prepara la solución para su uso: pruebas de aceptación, resolución de observaciones, preparación de usuarios, marcha blanca y despliegue conforme a los hitos aprobados.

Las iteraciones producen resultados verificables, pero no implican una puesta en producción o una marcha blanca. La marcha blanca y la aceptación formal se realizan en los momentos definidos para cada etapa contractual. Los casos de uso expresan y siguen los requisitos funcionales, y la matriz del Formulario T-12 los vincula con su prueba.

La secuencia de iteraciones se coordina con las dos etapas contractuales. La Etapa 1 comprende preventa, recepción, bodega, preparación y cross-docking, reposición de compras, trazabilidad de lotes y de la cadena de frío, planificación de rutas, captura de la evidencia de entrega y del acuse de recibo de la guía de despacho que registra el ERP, manejo de efectivo y retiro sanitario de lotes. En la Etapa 2 se implementan los portales y el intercambio electrónico con los clientes y, luego, el costo de servir. La transición sigue el cronograma: marcha blanca de la Etapa 1 entre los meses 13 y 15 y paso a producción en el mes 16; marcha blanca de la Etapa 2 en los meses 19 y 20 y paso a producción en el mes 21.

### 6.2.1 Arquitectura evolutiva, refactorización y deuda técnica

La arquitectura se establece durante Elaboración y se aprueba en el H2; se valida progresivamente en las iteraciones de Construcción. Cuando los nuevos requisitos o los resultados de las pruebas justifican cambios, la arquitectura se ajusta mediante una nueva versión de la decisión en el registro de decisiones de arquitectura del SD4, con su fecha, estado y acta del Comité de Arquitectura.

Durante la construcción, el equipo refactoriza el software para mejorar su estructura interna y facilitar su mantenimiento, preservando su comportamiento funcional; las pruebas automatizadas comprueban que el comportamiento no cambió. Las limitaciones o compromisos técnicos que puedan dificultar cambios futuros se registran como deuda técnica, con su impacto y prioridad. Una deuda clasificada como bloqueante por el análisis estático impide el despliegue; las demás se planifican en las iteraciones y se revisan en el Comité de Arquitectura.

### 6.2.2 DevSecOps, integración y entrega continuas, infraestructura como código y pruebas automatizadas

Cada cambio pasa por el pipeline de integración continua que define el SD4, sección 4.2: GitLab CI orquesta y AWS CodeBuild construye cada imagen de forma hermética, con procedencia SLSA nivel 3. El pipeline ejecuta la auditoría de dependencias con `composer audit`, las pruebas PHPUnit, el análisis estático con PHPStan y Larastan, el formato con Laravel Pint, las pruebas de contrato contra OpenAPI 3.1 y AsyncAPI 2.6, el escaneo de secretos y de imágenes de contenedor y la medición de cobertura.

Las compuertas son bloqueantes, no opcionales. El pipeline detiene la promoción ante:

- un hallazgo de seguridad crítico o alto en dependencias, código, secretos o imagen;
- un contrato público roto sin una nueva edición de la interfaz;
- una cobertura de la lógica de negocio inferior al 70 % (RT-04.11);
- una cobertura de pruebas unitarias inferior al 80 %, política corporativa de LafroX (Subdocumento 1, sección 1.3.1; paquete 1.5.2);
- una deuda técnica bloqueante o una prueba en falla.

La imagen aprobada se firma, se publica en Elastic Container Registry y se promueve por su digest, de modo que ningún ambiente recompila. La infraestructura de los cinco ambientes se describe como código: Terraform administra los recursos con estados separados por ambiente y Ansible configura los hosts; cada recurso tiene un único propietario de código. Las migraciones de base de datos siguen la estrategia de expandir y contraer y declaran su reversión.

La entrega continua mantiene versiones verificadas y listas para su despliegue en cada ambiente. El paso a Producción se ejecuta sólo dentro de las ventanas permitidas por el caso y, durante el desarrollo, sólo en los hitos aprobados: ningún cambio se despliega en septiembre, en diciembre ni en los tres primeros días hábiles de un mes.

### 6.2.3 Ceremonias, cadencias y decisiones del desarrollo

El trabajo del equipo de desarrollo se organiza en iteraciones de Construcción de dos semanas. Al inicio de cada iteración se revisan los requisitos y prioridades, se seleccionan las tareas que caben en la capacidad registrada y se aclaran sus criterios de aceptación. Durante la iteración, el equipo sigue el avance en el tablero Kanban, con bloqueos, responsables y dependencias.

Al cierre de cada iteración se demuestra el incremento verificable y se contrasta con sus criterios de aceptación; cuando es pertinente, se presenta a los interesados para recoger observaciones. El equipo revisa además las dificultades y aprendizajes de la iteración y registra las acciones de mejora con su responsable. Ninguna demostración constituye por sí misma una entrega formal o una puesta en producción.

Los artefactos del desarrollo son los casos de uso, la matriz de trazabilidad del Formulario T-12, el registro de decisiones de arquitectura, los contratos de interfaz, el registro de deuda técnica y los informes de pruebas de cada iteración.

Las decisiones técnicas necesarias para implementar los requisitos se toman dentro del equipo responsable y se documentan cuando afectan la arquitectura, las integraciones, la seguridad o la operación; las que cambian la arquitectura pasan por el Comité de Arquitectura. Si una decisión modifica el alcance, el plazo, los costos o los criterios de aceptación aprobados, se gestiona como una solicitud de cambio según la sección 6.1.4.

## Referencias

Las fuentes citadas en este documento se listan a continuación en formato APA 7.ª edición.

- Distribuidora Puelche S.A. (2026a). *Bases Administrativas de Licitación N.º TFEP-01/2026: Contratación de Solución Integral de Software y Servicios de Operación*.
- Distribuidora Puelche S.A. (2026b). *Bases Técnicas Transversales de Licitación N.º TFEP-01/2026*.
- Distribuidora Puelche S.A. (2026c). *Caso 02: Logística. Especificaciones del problema y operación de Distribuidora Puelche S.A.*
- Distribuidora Puelche S.A. (2026d). *Aclaraciones de la Licitación N.º TFEP-01/2026*.
- Kruchten, P. (2004). *The Rational Unified Process: An introduction* (3.ª ed.). Addison-Wesley.
- Project Management Institute. (2017). *La guía de los fundamentos para la dirección de proyectos (Guía del PMBOK®)* (6.ª ed.). Project Management Institute.

## Declaración de uso de IA

En cumplimiento de la sección 7.2 de las Aclaraciones de la licitación, la tabla siguiente declara el uso de herramientas de inteligencia artificial en este subdocumento, con la revisión humana de cada parte. La declaración se consolida en el Formulario A-6.

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
| --- | --- | --- | --- | --- | --- |
| Introducción | Claude Code | Redacción de la introducción y conexión con SD4 y SD7 | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 6.1 Metodología de Gestión de Proyectos | Codex; Claude Code | Responsabilidades de adquisición y cadencias; PMBOK adaptado, valor ganado, matriz de adquisiciones y Comité de Operación | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 6.2 Metodología de Desarrollo Software | Claude Code | Compuertas DevSecOps, herramientas del SD4, cadencia de iteraciones y artefactos | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| Formulario T-9 | Claude Code | Portada del formulario | Bajo | Ninguno | [[REVISIÓN HUMANA]] |
| Formulario T-10 | Claude Code | Portada del formulario | Bajo | Ninguno | [[REVISIÓN HUMANA]] |
