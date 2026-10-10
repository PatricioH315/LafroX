# Propuesta Técnica — Subdocumento 6: Metodologías

**Licitación:** TFEP-01/2026  
**Proyecto:** Plataforma Digital de Misión Crítica — Caso 02: Logística  
**Mandante:** Distribuidora Puelche S.A.  
**Proponente:** LafroX SpA — RUT 77.418.902-K  
**Representante legal:** Alex Aravena, Jefe de Proyecto y Apoderado  
**Fecha de emisión:** 7 de octubre de 2026  
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

Este subdocumento presenta y analiza los métodos de gestión del proyecto y de desarrollo de software. La gestión adapta el PMBOK mediante líneas base formales y control del avance con valor ganado; Kanban ordena el flujo diario, pero no sustituye la gobernanza ni la aceptación formal. El desarrollo combina RUP iterativo e incremental con prácticas DevSecOps, apoyadas por decisiones de arquitectura y compuertas de calidad. Los Formularios T-9 y T-10 contienen, respectivamente, el detalle de las metodologías de gestión y desarrollo. La arquitectura de referencia y la cadena de entrega se vinculan con el SD4.

## 6.1 Metodología de Gestión de Proyectos

La gestión adapta la Guía del PMBOK, sexta edición (PMI, 2017), a las características del proyecto. El alcance y el cronograma se controlan mediante líneas base formales, y el avance se mide con valor ganado, no con porcentajes declarados (RT-19.07). Kanban hace visible y ordena el flujo cotidiano del equipo, pero no sustituye esas líneas base ni la aceptación formal de los entregables.

La ejecución se organiza en entregas incrementales y fases coordinadas, de modo que las capacidades se incorporen progresivamente sin comprometer la continuidad operacional ni la integridad de los datos durante el solapamiento de etapas. El Formulario T-9 presenta el detalle de la planificación y de los mecanismos de gestión.

### 6.1.1 Gestión de interesados

La gestión de interesados identifica y clasifica a las personas, grupos y organizaciones que pueden verse afectados por el proyecto o influir en sus resultados, considerando sus necesidades, expectativas e influencia. El jefe de proyecto mantiene el registro detallado en el Formulario T-9 y realiza seguimiento a la participación y los compromisos de acuerdo con las actividades de cada entrega. Los conflictos que no puedan resolverse en la instancia de trabajo se escalan a la autoridad correspondiente. La identificación o participación de un interesado no le confiere por sí misma atribuciones universales de decisión o aprobación.

### 6.1.2 Gestión de comunicaciones

La gestión de las comunicaciones mantiene informados a los responsables de Puelche y a los demás interesados sobre los avances, facilita decisiones y da seguimiento a los compromisos. Los acuerdos, decisiones y acciones se documentan con responsables y plazos. Los cambios que puedan afectar los compromisos se comunican oportunamente; antes de cada entrega se informa a los interesados pertinentes sobre cambios previstos, validaciones y apoyos requeridos, y las observaciones se registran y atienden, canalizando por solicitud de cambio las que excedan lo acordado. El Formulario T-9 contiene los destinatarios, las cadencias, los registros y la matriz detallada de comunicaciones.

Cada informe mensual de avance incluirá estado del cronograma, avance físico y financiero, entregables del período, desviaciones, riesgos, incidencias y compromisos del período siguiente, con responsables y fechas (Distribuidora Puelche S.A., 2026b, RT-19.06). El avance y las desviaciones se sustentarán en las líneas base, el valor ganado y los registros de ejecución de 6.1.5.

### 6.1.3 Gestión de adquisiciones

La gestión de adquisiciones planifica y controla las compras y contrataciones según las necesidades, dependencias y cronograma. El CLIENTE compra el equipamiento de terreno conforme a las especificaciones de LafroX; para los equipos de la sala técnica, incluidos racks, servidores y equipos de borde, T-14 asigna a LafroX la orden de compra en el mes 2 y la instalación en el mes 3. La recepción técnica de los equipos y la recepción de la sala son hitos distintos: T-15 sitúa la recepción de la sala en el mes 4, sin que ello establezca aquí una fecha de recepción técnica ni de puesta en servicio/commissioning. El servicio SOC 24x7 es condicional a su subcontratación; RT-11.17 presenta cumplimiento parcial porque la ubicación del SOC no está declarada. Esta referencia no significa que el servicio ya esté contratado ni que exista cumplimiento completo. El refuerzo de evaluadores de prueba subcontratados, de hasta 16 por día, cubre los meses 9 a 12 y 16 a 18: en los meses 9, 10, 16 y 17 apoya la ejecución de las pruebas de etapa, y en los meses 11, 12 y 18 queda disponible para la subsanación de las observaciones del CLIENTE a los entregables de hito (LafroX, 2026, Subdocumento 9, sección 9.3.2). LafroX habilita el espacio proporcionado por el CLIENTE y configura los equipos; las evidencias y el registro completo de adquisiciones se detallan en T-9.

LafroX garantiza contractualmente que los datos del CLIENTE no serán utilizados para entrenar modelos de terceros, salvo autorización previa, expresa y escrita del CLIENTE. Esta obligación se exigirá también a los proveedores y subcontratistas que tengan acceso a dichos datos (Distribuidora Puelche S.A., 2026b, RT-18.02).

### 6.1.4 Gestión de integración

La integración coordina alcance, cronograma, costos, recursos, calidad, riesgos y adquisiciones. El jefe de proyecto mantiene las dependencias y los asuntos del proyecto; el detalle del proceso y las responsabilidades se presenta en el Formulario T-9.

Los cambios que afecten compromisos aprobados se documentan y evalúan, y requieren aprobación antes de incorporarse. Las acciones correctivas que mantienen esos compromisos no constituyen por sí mismas cambios formales; si los modifican, se tramitan como tales. Los entregables se comprueban frente a sus criterios de aceptación y la evidencia correspondiente.

### 6.1.5 Control del alcance, del cronograma y del valor ganado

El alcance y el cronograma se controlan contra sus líneas base aprobadas y la trazabilidad de requisitos del Formulario T-12 y del Formulario T-15. El avance se evalúa mediante indicadores de valor ganado, no mediante porcentajes autodeclarados. Las desviaciones y las acciones correctivas o de recuperación se registran y escalan conforme al proceso de gobierno. Las reservas se controlan por separado y sólo se utilizan con autorización registrada. El Formulario T-9 establece las reglas de cálculo, los umbrales, los plazos de recuperación y los detalles de reporte.

### 6.1.6 Mecanismos de decisión y cadencias de gobierno

La gobernanza combina seguimiento diferenciado y comités formales para revisar el avance, los riesgos, los cambios, la arquitectura y la operación del servicio. El seguimiento operativo semanal permite atender bloqueos y preparar información, pero no sustituye las instancias de comité. Las decisiones y acciones se registran con sus responsables y fechas de cumplimiento. El Formulario T-9 contiene la composición exacta, las cadencias, las atribuciones y las responsabilidades de cada instancia.

## 6.2 Metodología de Desarrollo Software

La metodología de desarrollo se coordina con la gestión del proyecto y sus entregas incrementales. RUP estructura el trabajo en cuatro fases —Inicio, Elaboración, Construcción y Transición— y permite avanzar de forma iterativa e incremental. Las iteraciones de construcción producen incrementos verificables, mientras que las etapas de entrega se coordinan con las fases contractuales para favorecer la continuidad operacional. Una iteración o demostración no constituye aceptación formal, marcha blanca ni puesta en producción. Los requisitos y sus pruebas se mantienen trazables mediante el Formulario T-12; el Formulario T-10 contiene el detalle de las fases, los procesos y los artefactos.

### 6.2.1 Arquitectura evolutiva, refactorización y deuda técnica

La arquitectura se establece y valida tempranamente, y evoluciona cuando los requisitos o resultados de pruebas justifican cambios, mediante decisiones trazables (véase SD4). La refactorización mejora la mantenibilidad y las pruebas preservan el comportamiento. La deuda técnica se registra con su impacto y prioridad, y se trata según la severidad acordada. El Formulario T-10 detalla los criterios y el proceso.

### 6.2.2 DevSecOps, integración y entrega continuas, infraestructura como código y pruebas automatizadas

El pipeline automatizado integra construcción, pruebas y controles de seguridad y calidad. Sus compuertas bloquean la promoción cuando fallan los controles aplicables, incluidos los requisitos de cobertura: al menos 70 % de cobertura de lógica de negocio según RT-04.11 y al menos 80 % de cobertura unitaria global según la política LafroX. Son requisitos distintos y no umbrales intercambiables. Los artefactos aprobados se promueven con trazabilidad entre ambientes, sin reconstruirlos. La infraestructura como código y las migraciones compatibles y reversibles permiten una entrega controlada. El Formulario T-10 detalla las herramientas, las reglas precisas de las compuertas, la infraestructura como código y los procedimientos de despliegue.

### 6.2.3 Ceremonias, cadencias y decisiones del desarrollo

El trabajo se organiza en iteraciones regulares, con trabajo priorizado y aceptado, seguimiento del avance y de los bloqueos, demostración de incrementos y revisión de aprendizajes para impulsar mejoras. Las demostraciones y los incrementos no constituyen por sí mismos una entrega formal ni una puesta en producción. Las decisiones técnicas se documentan; las que afectan la arquitectura siguen la gobernanza arquitectónica, y los cambios a compromisos aprobados se gestionan conforme a la sección 6.1.4. El Formulario T-10 detalla las cadencias, los artefactos, los roles y los procedimientos.

## Referencias

- Distribuidora Puelche S.A. (2026a). *Bases Administrativas de Licitación N.º TFEP-01/2026: Contratación de Solución Integral de Software y Servicios de Operación*.
- Distribuidora Puelche S.A. (2026b). *Bases Técnicas Transversales de Licitación N.º TFEP-01/2026*.
- Distribuidora Puelche S.A. (2026c). *Caso 02: Logística. Especificaciones del problema y operación de Distribuidora Puelche S.A.*
- Distribuidora Puelche S.A. (2026d). *Aclaraciones de la Licitación N.º TFEP-01/2026*.
- Kruchten, P. (2004). *The Rational Unified Process: An introduction* (3.ª ed.). Addison-Wesley.
- Project Management Institute. (2017). *La guía de los fundamentos para la dirección de proyectos (Guía del PMBOK®)* (6.ª ed.). Project Management Institute.

## Declaración de uso de IA

La tabla declara el uso de herramientas de inteligencia artificial en este subdocumento y en sus formularios; se consolida en el Formulario A-6.

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
|---|---|---|---|---|---|
| Introducción | Claude Code | Redacción de la introducción y conexión con SD4 y SD7 (7 de octubre de 2026) | Alto | Ninguno | No documentada |
| 6.1 Metodología de Gestión de Proyectos | Codex; Claude Code | Responsabilidades de adquisición y cadencias (6 de octubre de 2026); PMBOK adaptado, valor ganado, matriz de adquisiciones y Comité de Operación (7 de octubre de 2026); contenido del informe mensual y garantía sobre entrenamiento de modelos de terceros | Alto | Ninguno | No documentada |
| 6.2 Metodología de Desarrollo Software | Claude Code | Compuertas DevSecOps, herramientas del SD4, cadencia de iteraciones y artefactos (7 de octubre de 2026) | Alto | Ninguno | No documentada |
| Formulario T-9 | Claude Code | Portada y adaptación a Markdown del contenido metodológico detallado y sus tablas | Alto | Ninguno | No documentada |
| Formulario T-10 | Claude Code | Portada y adaptación a Markdown del contenido metodológico detallado y sus tablas | Alto | Ninguno | No documentada |
