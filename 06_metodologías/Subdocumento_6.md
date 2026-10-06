# Propuesta Técnica — Subdocumento 6: Metodologías

**Licitación:** TFEP-01/2026  
**Proyecto:** Plataforma Digital de Misión Crítica — Caso 02: Logística  
**Mandante:** Distribuidora Puelche S.A.  
**Proponente:** LafroX SpA — RUT 77.418.902-K  
**Representante legal:** Alex Aravena, Jefe de Proyecto y Apoderado  
**Fecha de emisión:** 05 de octubre de 2026  
**Formulario:** T-9 y T-10

## Índice

- [1. Metodologías del proyecto y software](#1-metodologías-del-proyecto-y-software)
  - [1.1 Metodología de gestión de proyecto](#11-metodología-de-gestión-de-proyecto)
    - [1.1.1 Gestión de interesados](#111-gestión-de-interesados)
    - [1.1.2 Gestión de comunicaciones](#112-gestión-de-comunicaciones)
    - [1.1.3 Gestión de adquisiciones](#113-gestión-de-adquisiciones)
    - [1.1.4 Gestión de integración](#114-gestión-de-integración)
  - [1.2 Metodología de desarrollo de software](#12-metodología-de-desarrollo-de-software)
    - [1.2.1 Arquitectura evolutiva, refactorización y deuda técnica](#121-arquitectura-evolutiva-refactorización-y-deuda-técnica)
    - [1.2.2 DevSecOps, integración y entrega continuas, infraestructura como código y pruebas automatizadas](#122-devsecops-integración-y-entrega-continuas-infraestructura-como-código-y-pruebas-automatizadas)
    - [1.2.3 Ceremonias, cadencias y decisiones del desarrollo](#123-ceremonias-cadencias-y-decisiones-del-desarrollo)

# 1. Metodologías del proyecto y software

Para que el desarrollo del producto final sea un éxito total, se debe por necesidad seguir metodologías asociadas a la gestión de proyecto y, a su vez, metodologías para el desarrollo de software. Estas metodologías serán las siguientes.

## 1.1 Metodología de gestión de proyecto

La gestión del proyecto se organizará mediante la planificación, el seguimiento y el control de las actividades necesarias para cumplir los objetivos acordados con Puelche. Para ello, se definirán los entregables, sus responsables, los recursos requeridos, los plazos y las dependencias entre actividades, considerando las restricciones de la operación. La planificación establecerá una línea base de alcance y cronograma, que servirá para medir el avance y evaluar las desviaciones.

El proyecto se ejecutará mediante entregas incrementales dentro de las dos etapas contractuales. La distribución propuesta prioriza primero la calidad y disponibilidad de la información operacional, y luego las capacidades que dependen de esos datos para optimizar y analizar la operación. En la Etapa 1 se implementarán las capacidades de la preventa, recepción, bodega, preparación y cross-docking; la trazabilidad de los lotes y cadenas de frío; además de la planificación de rutas basada en el conocimiento del planificador, acompañada del acuse de recibo de los conductores; y el manejo de efectivo más los retiros de los pedidos.

En la Etapa 2 se implementarán las capacidades de los portales y el intercambio electrónico con los clientes y, por último, la verificación de los costos de servir.

La planificación respetará el cronograma contractual: desarrollo de la Etapa 1 entre los meses 1 y 12, marcha blanca entre los meses 13 y 15 y paso a producción en el mes 16. El desarrollo de la Etapa 2 se realizará entre los meses 13 y 18, la marcha blanca en los meses 19 y 20 y el paso a producción en el mes 21. El trabajo de la Etapa 2 se coordinará con la marcha blanca y la estabilización de la Etapa 1, resguardando la continuidad operacional y la integridad de los datos compartidos.

El alcance y el cronograma aprobados servirán como referencia para evaluar el avance del proyecto. El jefe de proyecto revisará periódicamente el cumplimiento de los compromisos con el equipo y las contrapartes involucradas, registrará las desviaciones y coordinará las acciones correctivas. Si una modificación afecta el alcance, el plazo o los costos aprobados, se analizará su impacto y se solicitará la aprobación de Puelche antes de incorporarla al plan. Las decisiones y cambios aprobados quedarán registrados y se comunicarán a las personas afectadas.

Para gestionar el flujo de trabajo del equipo se utilizará un **tablero Kanban**. El tablero permitirá al equipo visualizar el trabajo pendiente, en ejecución, en revisión y terminado, junto con los responsables y bloqueos. Con esto, se establecerán límites de trabajo en curso. El tablero coordinará las tareas del equipo, pero no reemplazará el cronograma contractual ni la aceptación formal de los entregables. Cada tarea tendrá una definición de terminado y, cuando corresponda, evidencia asociada a los criterios de aceptación del entregable al que contribuye.

La gestión del proyecto se complementará con procesos para integrar las actividades, involucrar a los interesados, coordinar las comunicaciones y administrar las adquisiciones. Estos procesos se desarrollarán en los siguientes apartados.

### 1.1.1 Gestión de interesados

La gestión de interesados comprenderá la identificación de las personas, grupos y organizaciones que pueden influir en el proyecto o verse afectados por sus resultados. Para cada interesado se registrarán sus necesidades, expectativas, nivel de influencia, impacto potencial y disposición frente a los cambios. El análisis permitirá distinguir quiénes participan en decisiones, quiénes aportan conocimiento operacional, quiénes validan entregables y quiénes son afectados o ejercen supervisión externa.

El jefe de proyecto mantendrá actualizado el registro de interesados y planificará su involucramiento de acuerdo con el alcance de cada entrega. La participación podrá incluir levantamiento de necesidades, revisión de procesos, validación de criterios, pruebas y retroalimentación. Durante el proyecto se revisarán las expectativas y el nivel de participación requerido, especialmente cuando cambie el alcance o se incorporen nuevas capacidades. Las inquietudes, resistencias, acuerdos y compromisos relevantes se registrarán con su responsable y seguimiento; los conflictos que no puedan resolverse en la instancia de trabajo se elevarán a la autoridad correspondiente.

**Tabla 1.1. Interesados del proyecto — Fuente: elaboración propia**

| Interesado | Interés o preocupación | Contribución esperada |
|---|---|---|
| Gerencia general | Continuidad del negocio y relación con clientes | Aportar prioridades del negocio y resolver decisiones que requieran su intervención |
| Jefatura de calidad | Trazabilidad de lotes y control de temperatura | Definir y revisar reglas de control sanitario y evidencia de trazabilidad |
| Autoridades sanitarias | Disponibilidad y confiabilidad de la evidencia de trazabilidad | Informar exigencias aplicables y revisar antecedentes cuando corresponda |
| Planificador de rutas | Preservar el conocimiento operacional | Documentar restricciones y reglas de planificación, y participar en su validación |
| Gerencia comercial | Cumplimiento de la promesa de entrega e información confiable | Aportar y validar políticas comerciales, procesos de preventa y necesidades de servicio |
| Cadenas de supermercados | Recepción completa y oportuna de pedidos e intercambio electrónico | Participar en la definición y validación de los flujos de aviso de despacho y evidencia de entrega |
| Clientes del canal tradicional | Recepción correcta de pedidos, pagos y atención | Aportar retroalimentación sobre recepción, comprobantes y atención |
| Preventistas | Consulta de stock y crédito, y registro confiable de pedidos | Participar en el levantamiento y prueba de los flujos de preventa y cobranza |
| Sindicato de conductores | Condiciones de trabajo y uso de tecnologías | Canalizar inquietudes y aportar observaciones sobre los cambios que afecten a los conductores |
| Conductores propios | Registro de entregas, devoluciones y cobros | Participar en pruebas de ruta y validar la usabilidad de los dispositivos |
| Jefatura de bodega | Preparación, despacho y control de inventario | Aportar y validar procedimientos, excepciones y condiciones de operación |
| Preparadores de pedidos | Claridad de instrucciones y adecuación de los dispositivos | Participar en pruebas de los flujos de preparación de pedidos |
| Gerencia de operaciones | Continuidad del despacho y cumplimiento de entregas | Aportar prioridades operacionales y validar procedimientos y cambios que afecten la operación |
| Administración y finanzas | Control de cobros, conciliación y costos de servir | Definir y validar reglas de rendición, conciliación e indicadores financieros |
| Equipo de TI | Integración con sistemas existentes y mantenibilidad de la solución | Coordinar accesos e integraciones, y revisar documentación y transferencia de conocimiento |
| Conductores de transportistas externos | Acceso a la solución y registro de actividades de reparto | Participar en pruebas de los flujos que les correspondan y aportar observaciones de uso |
| Proveedores | Intercambio de información de productos, lotes y despacho | Coordinar formatos de intercambio y participar en pruebas de recepción y trazabilidad |

La tabla resume los principales grupos y roles identificados, sus intereses y la contribución esperada. La participación concreta se acordará según las responsabilidades de cada interesado y las actividades de cada entrega; la inclusión en la tabla no implica que todos participen en todas las decisiones ni que tengan atribuciones de aprobación.

### 1.1.2 Gestión de comunicaciones

La gestión de las comunicaciones buscará que los responsables de Puelche y los demás interesados se mantengan informados sobre los avances de las entregas que les competen. Asimismo, procurará mantener una comprensión común del estado del proyecto, facilitar la toma de decisiones y comunicar oportunamente las situaciones que puedan afectar los compromisos acordados.

Las reuniones se organizarán según los asuntos que deban tratarse y convocarán a las personas necesarias para analizarlos y resolverlos. Los acuerdos alcanzados se registrarán en actas que identifiquen las decisiones adoptadas, las actividades pendientes, sus responsables y los plazos comprometidos. Además, la documentación vigente se almacenará en un repositorio compartido, cuyo acceso se asignará de acuerdo con las responsabilidades de cada participante.

Cuando existan necesidades contrapuestas, se recogerán las posiciones de las áreas involucradas y se evaluarán sus efectos sobre la operación y los objetivos del proyecto. Los asuntos que no puedan resolverse en la instancia de trabajo se elevarán a la autoridad correspondiente. La resolución quedará registrada y se comunicará a las personas afectadas.

Antes de cada entrega incremental, se informará a los interesados pertinentes sobre los cambios previstos, las actividades de validación y el apoyo necesario para la puesta en funcionamiento. Las observaciones se registrarán y recibirán respuesta, distinguiendo aquellas que puedan atenderse dentro de lo acordado de aquellas que requieran una solicitud de cambio.

**Tabla 1.2. Comunicación del proyecto — Fuente: creación propia**

| Comunicación | Responsable de comunicar | Destinatarios | Frecuencia o momento |
|---|---|---|---|
| Seguimiento de actividades, compromisos y bloqueos | Jefe de proyecto | Equipo de proyecto y contrapartes involucradas | Semanal |
| Avance de entregables, desviaciones y riesgos | Jefe de proyecto | Comité de proyecto | Según frecuencia de seguimiento acordada |
| Cambios previstos, validaciones y apoyo | Jefe de proyecto | Interesados pertinentes | Antes de cada entrega |

### 1.1.3 Gestión de adquisiciones

Para la gestión de adquisiciones, debemos ser cuidadosos con la gestión y el control para desarrollar y administrar contratos, órdenes de compra, memorandos de acuerdo o acuerdos de nivel de servicio.

Para poder adquirir todos los productos y servicios necesarios para el desarrollo del proyecto, se requieren diversos contratos y órdenes de compra, que provienen del estudio de las necesidades de los diversos interesados y de la investigación propia del mercado para resolver los problemas existentes. A la vez, se realiza una revisión de los contratos administrativos y legales asociados al desarrollo del software para cumplir con los requerimientos de Puelche.

Todo lo relacionado con las órdenes de compra de insumos o herramientas físicas que utilizarán los trabajadores de Puelche se informará a la gerencia de Puelche, encargada de realizar esas compras. Por otro lado, LafroX investigará y contratará los servicios relacionados con la arquitectura lógica. Asimismo, adquirirá los insumos necesarios para implementar la arquitectura física.

Todas las adquisiciones se explicitan en la siguiente tabla.

**Tabla 1.3. Adquisiciones — Fuente: creación propia**

| Bien o servicio | Necesidad asociada | Tipo | Responsable de compra |
|---|---|---|---|
| Sensores de temperatura | Control de temperatura en bodegas y camiones | Insumos | Gerencia de Puelche |
| Pistola de código de barras | Registro de productos y lotes | Insumos | Gerencia de Puelche |
| Amazon Web Services (AWS) | Servidores y almacenamiento en la nube | Servicio | LafroX |

La tabla de adquisiciones busca identificar el bien o servicio, la necesidad asociada, el tipo correspondiente y el responsable de la compra.

### 1.1.4 Gestión de integración

La gestión de integración mantendrá alineados los distintos componentes del proyecto para que las decisiones sobre alcance, cronograma, costos, recursos, calidad, riesgos y adquisiciones se analicen de manera coordinada. El jefe de proyecto consolidará estos elementos en el plan para la dirección del proyecto, lo comunicará a los responsables y lo actualizará cuando se aprueben cambios. Este plan será la referencia común para organizar el trabajo y evaluar sus efectos sobre los compromisos asumidos con Puelche.

Durante la ejecución, el jefe de proyecto coordinará las actividades y sus dependencias, revisará el avance de los entregables y gestionará los impedimentos que afecten a más de un equipo o área. Cuando una decisión pueda repercutir en otros componentes del proyecto, se analizarán sus impactos antes de actuar. Las decisiones, acuerdos, riesgos transversales y asuntos que requieran escalamiento quedarán registrados con su responsable, resolución y fecha de seguimiento.

Toda solicitud de cambio que pueda afectar el alcance, los plazos, los costos o los criterios de aceptación se documentará y evaluará antes de su implementación. El análisis considerará sus efectos en el plan, los entregables relacionados, los riesgos y la operación. El jefe de proyecto elevará la solicitud a la autoridad correspondiente de Puelche y comunicará la decisión a las personas afectadas. Solo los cambios aprobados se incorporarán a la planificación vigente. Las acciones correctivas destinadas a cumplir los compromisos aprobados se registrarán y supervisarán; si modifican esos compromisos, deberán tramitarse además como solicitudes de cambio.

Al finalizar cada entrega, se comprobará que sus resultados satisfagan los criterios de aceptación y cuenten con la evidencia requerida. Las observaciones pendientes se registrarán con responsable y tratamiento acordado. También se documentarán las decisiones y lecciones aprendidas que puedan orientar el trabajo posterior. La coordinación entre entregas contemplará las actividades que se desarrollen en paralelo, de modo que no se comprometan la continuidad de la operación, la integridad de la información ni los hitos planificados.

## 1.2 Metodología de desarrollo de software

La metodología de desarrollo de software se coordinará con la gestión general del proyecto y con sus entregas incrementales. Para ello, se utilizará **Rational Unified Process (RUP)**, un proceso iterativo e incremental que organiza el desarrollo en cuatro fases y permite gestionar requisitos, arquitectura, implementación y pruebas de manera progresiva. Su elección se basa en que facilita la documentación del trabajo, la identificación temprana de riesgos y la reutilización de componentes cuando resulte pertinente.

RUP se organiza en las siguientes fases:

1. **Inicio:** se delimitarán el alcance y los objetivos de la solución, se identificarán los principales interesados y requisitos, y se elaborarán estimaciones iniciales de esfuerzo, costo y plazo. También se reconocerán los riesgos principales y se establecerá una visión inicial del producto.
2. **Elaboración:** se profundizarán los requisitos, incluidos los casos de uso, y se definirá la arquitectura de la solución. Se analizarán los riesgos prioritarios y se preparará el plan de desarrollo, de modo que las decisiones de diseño más relevantes se validen antes de avanzar a la construcción.
3. **Construcción:** se desarrollarán las capacidades priorizadas mediante iteraciones. En cada iteración se analizarán los requisitos correspondientes, se diseñará e implementará la solución y se realizarán pruebas. Los resultados se revisarán con los interesados pertinentes y se ajustarán cuando corresponda.
4. **Transición:** se preparará la solución para su uso, lo que comprenderá pruebas de aceptación, resolución de observaciones, preparación de usuarios, marcha blanca y despliegue conforme a los hitos aprobados.

Las iteraciones producirán resultados verificables, pero no necesariamente implicarán una puesta en producción o una marcha blanca. Las pruebas y revisiones de cada iteración permitirán comprobar el avance y corregir problemas durante el desarrollo; la marcha blanca y la aceptación formal se realizarán en los momentos definidos para cada etapa contractual. De este modo, RUP organizará el desarrollo del software, mientras que la metodología de gestión del proyecto coordinará las dependencias, los responsables, los hitos y las aprobaciones. Los casos de uso contribuirán a expresar y seguir los requisitos funcionales de la solución.

La secuencia de iteraciones se coordinará con las dos etapas contractuales. En la Etapa 1 se implementarán las capacidades de preventa, recepción, bodega, preparación y cross-docking; la trazabilidad de lotes y de la cadena de frío; la planificación inicial de rutas basada en la experiencia del planificador; la confirmación de recepción por parte de los conductores; y el manejo de efectivo y los retiros de pedidos. En la Etapa 2 se implementarán los portales y el intercambio electrónico con los clientes, y luego se verificará el costo de servir.

La transición se ajustará al cronograma acordado: para la primera etapa, la marcha blanca está prevista entre los meses 13 y 15 y el paso a producción en el mes 16; para la segunda, la marcha blanca se realizará entre los meses 19 y 20 y el paso a producción en el mes 21. La operación y el mantenimiento posteriores se gestionarán como actividades de soporte.

### 1.2.1 Arquitectura evolutiva, refactorización y deuda técnica

La arquitectura se establecerá inicialmente durante Elaboración y se validará progresivamente en las iteraciones de Construcción. Cuando los nuevos requisitos o los resultados de las pruebas justifiquen cambios, la arquitectura podrá ajustarse mediante decisiones documentadas y evaluadas según su impacto en las capacidades existentes, las integraciones y la operación.

Durante la construcción, el equipo podrá refactorizar el software para mejorar su estructura interna y facilitar su mantenimiento y evolución, procurando preservar su comportamiento funcional. Las limitaciones o compromisos técnicos que puedan dificultar cambios futuros se registrarán como deuda técnica, junto con su impacto y prioridad. Su tratamiento se planificará en las iteraciones correspondientes y se verificará mediante las pruebas definidas para ellas.

### 1.2.2 DevSecOps, integración y entrega continuas, infraestructura como código y pruebas automatizadas

Durante las iteraciones de Construcción, los cambios podrán integrarse con frecuencia y someterse a pruebas automatizadas y verificaciones de seguridad, con el propósito de detectar problemas tempranamente. La infraestructura de los ambientes podrá describirse mediante archivos versionados para facilitar su revisión y reproducción. Estas prácticas permitirán preparar entregas de manera repetible y controlada, sin que ello implique desplegar automáticamente en producción. La aceptación, la marcha blanca y el paso a producción se mantendrán sujetos a los hitos y aprobaciones definidos para cada etapa.

La integración continua permitirá ejecutar automáticamente la construcción y las pruebas definidas cada vez que se incorporen cambios. La entrega continua mantendrá versiones verificadas y listas para su despliegue en los ambientes correspondientes, sujeto a las aprobaciones previstas.

### 1.2.3 Ceremonias, cadencias y decisiones del desarrollo

El trabajo del equipo de desarrollo se organizará en torno a las iteraciones de Construcción de RUP. Al inicio de cada iteración, se revisarán los requisitos y prioridades definidos, se seleccionarán las tareas que puedan abordarse y se aclararán sus criterios de aceptación. Durante la iteración, el equipo dará seguimiento al avance mediante el tablero Kanban, identificando bloqueos, responsables y dependencias que requieran coordinación.

Al cierre de cada iteración, se revisarán los resultados verificables y se contrastarán con los criterios de aceptación correspondientes. Cuando sea pertinente, se presentarán a los interesados involucrados para recoger observaciones y determinar su tratamiento. El equipo también podrá revisar las dificultades y aprendizajes de la iteración, con el propósito de proponer ajustes a su forma de trabajo. Los acuerdos y acciones resultantes se registrarán con sus responsables y seguimiento.

La frecuencia de estas instancias se ajustará a la duración de las iteraciones y a las necesidades de coordinación del proyecto. Las revisiones con Puelche se organizarán de acuerdo con los entregables, las actividades de validación y los hitos contractuales, sin que cada iteración implique por sí misma una entrega formal o una puesta en producción.

Las decisiones técnicas necesarias para implementar los requisitos se tomarán dentro del equipo responsable y se documentarán cuando afecten la arquitectura, las integraciones, la seguridad o la operación de la solución. Si una decisión implica modificar el alcance, el plazo, los costos o los criterios de aceptación aprobados, se gestionará como una solicitud de cambio y deberá seguir el proceso de evaluación y aprobación definido para el proyecto antes de incorporarse a la planificación vigente.
