# LafroX SpA


## LICITACIÓN PÚBLICA

# Licitación N.° TFEP-01/2026

**Proyecto de Plataforma Digital de Misión Crítica**
**Caso — Logística**

**Sobre N.° 2 --- Oferta Técnica**

# Propuesta Técnica

**Subdocumento 01 — Presentación de la empresa**
**Subdocumento 01 · Formulario T-7**

**MANDANTE**
Distribuidora Puelche S.A.

**PROPONENTE**
LafroX SpA
RUT 77.418.902-K
Av. Brasil 2241, Valparaíso

**REPRESENTANTE LEGAL**
Alex Aravena
Jefe de Proyecto y Apoderado
contacto@lafrox.cl
+56 32 250 4100

**FECHA DE EMISIÓN**

05 de octubre de 2026

**FIRMA DEL REPRESENTANTE LEGAL**

Alex Aravena
Jefe de Proyecto y Apoderado · LafroX SpA

---

# Índice general

- [1 Introducción](#1-introducción)
  - [1.1 Presentación de la empresa](#11-presentación-de-la-empresa)
    - [1.1.1 Productos de Software](#111-productos-de-software)
    - [1.1.2 Servicios Profesionales](#112-servicios-profesionales)
    - [1.1.3 Servicios de Infraestructura y Conectividad](#113-servicios-de-infraestructura-y-conectividad)
  - [1.2 Estructura Organizacional](#12-estructura-organizacional)
  - [1.3 Gobierno interno Calidad, Seguridad y Conocimiento](#13-gobierno-interno-calidad-seguridad-y-conocimiento)
    - [1.3.1 Modelo de Gobierno de Calidad](#131-modelo-de-gobierno-de-calidad)
    - [1.3.2 Modelo de Gobierno de Seguridad de la Información](#132-modelo-de-gobierno-de-seguridad-de-la-información)
    - [1.3.3 Modelo de Gobierno de Gestión del Conocimiento](#133-modelo-de-gobierno-de-gestión-del-conocimiento)
  - [1.4 Experiencia y Certificaciones](#14-experiencia-y-certificaciones)
    - [1.4.1 Cartera de Clientes](#141-cartera-de-clientes)
  - [1.5 Estructura para Proyecto](#15-estructura-para-proyecto)
  - [1.6 Alianzas](#16-alianzas)
  - [Referencias](#referencias)
  - [Declaración de uso de IA](#declaración-de-uso-de-ia)

# 1 Introducción

<a id="cap:empresa"></a>

Este capítulo presenta la trayectoria, los servicios y la organización de LafroX para el caso de Distribuidora Puelche S.A. Explica cómo se distribuyen las responsabilidades de calidad, seguridad y operación, y compara la experiencia de la empresa con las exigencias del caso. El Formulario T-6 acompaña el capítulo con el detalle de tres proyectos. La arquitectura y el plan de trabajo se desarrollan en los Subdocumentos 4 y 7; el equipo nominado y las alianzas específicas corresponden al Capítulo 12.

## 1.1 Presentación de la empresa

LafroX fue fundada en 2012 en Santiago de Chile. Se dedica al desarrollo, la integración y la operación de sistemas para logística, distribución de consumo masivo y transporte de carga. Su experiencia se concentra en operaciones con instalaciones dispersas, conectividad intermitente y exigencias de trazabilidad.

Entre los principales hitos de su trayectoria destacan la puesta en marcha de su primera plataforma de ruteo y telemetría en 2015, la acreditación como integrador certificado de hardware industrial para cadenas de frío en 2018, la primera certificación corporativa en normas de calidad y seguridad en 2021, mantenida desde entonces mediante auditorías de seguimiento y renovación, y la consolidación de su arquitectura modular híbrida en 2024, sosteniendo a la fecha dos operaciones diarias de gran volumen en terreno: 22.000 entregas diarias en el Proyecto 1 y 18.000 transacciones comerciales diarias en el Proyecto 3 del Formulario T-6. Son unidades distintas y no se suman.

LafroX mantiene un sitio web corporativo en <https://lafrox.github.io/>, publicado con certificado TLS válido, diseño responsivo y criterios WCAG 2.2 nivel AA. El sitio presenta el giro, la trayectoria, la misión, la visión y los valores de la empresa, su organigrama directivo, su Sede Central y su domicilio, el equipo, los casos de éxito del Formulario T-6, las certificaciones vigentes y las alianzas tecnológicas. Incluye además un centro de recursos con artículos técnicos, un recorrido guiado por la solución, el estado del servicio medido en vivo y una calculadora de ahorro para operaciones logísticas. LafroX mantiene el sitio activo y disponible durante todo el proceso de licitación, desde el registro del participante hasta la adjudicación (RT-23.01 a RT-23.10).

LafroX trabaja en tres líneas de negocio:

- **Ingeniería de software en el borde (Edge Computing):** Desarrollo de aplicaciones móviles y sistemas locales con arquitectura *offline-first*. Implementan almacenamiento local cifrado mediante bases de datos SQLite en terminales móviles, sincronización asíncrona bidireccional y resolución determinista de conflictos al restablecer el enlace de comunicaciones, para conservar las operaciones capturadas sin señal y sincronizarlas al recuperar la conexión.

- **Trazabilidad y telemetría de frío industrial:** Integración de hardware especializado de terreno, tales como termógrafos vehiculares, sensores inalámbricos y capturadores robustos aptos para operar bajo frío extremo. Esta línea registra temperaturas y eventos de custodia para apoyar los controles del Reglamento Sanitario de los Alimentos (RSA) y los procedimientos de retiro de productos.

- **Arquitecturas modulares híbridas de misión crítica:** Diseño, despliegue y soporte continuo de plataformas que combinan un núcleo transaccional en nube pública con componentes de borde desplegados en centros de distribución físicos (*on-premise*), con mecanismos de continuidad local ante cortes de conectividad externa. La línea trabaja habitualmente con monolitos modulares en PHP y Laravel sobre PostgreSQL, con aplicaciones móviles nativas en Kotlin, con límites de contexto explícitos, contratos de interfaz versionados y despliegue independiente de los componentes críticos. La arquitectura concreta para Puelche, con su justificación frente al Artículo 19° de las Bases Administrativas y al RT-02.02 de las Bases Técnicas Transversales, se presenta en la arquitectura de la oferta.

Estas líneas se apoyan en dos capacidades operativas:

- **Infraestructura y ambientes:** Plataforma de cómputo en nube pública y dos centros de datos (primario y secundario en configuración activo-pasivo) que soportan cinco ambientes segregados: Desarrollo (DEV), Aseguramiento de Calidad (QA), Preproducción (PREPROD), Producción (PROD) y Recuperación ante Desastres (DR). La capacitación utiliza datos ficticios en un espacio aislado del ambiente que corresponda; no constituye un sexto ambiente. El entorno DR es sometido a auditorías y simulacros semestrales, con objetivos de RTO ≤ 4 horas y RPO ≤ 15 minutos.

- **Centro de Operaciones y Mesa de Servicios:** Centro de Operaciones de Red (NOC), Centro de Operaciones de Seguridad (SOC) y Mesa de Servicios con niveles de escalamiento L1, L2 y L3, en el Centro de Operaciones de LafroX en Valparaíso (Av. Brasil 2241). Para Puelche, los incidentes de severidad crítica y alta se atienden 24×7×365, como exige el Artículo 78.2 de las Bases Administrativas; la mesa de servicio atiende al usuario de 04:00 a 22:00 de lunes a sábado, con cobertura 24×7 en septiembre y diciembre (Subdocumento 3, sección 3.4.5). Su capacidad se recalibra con los tickets observados en la marcha blanca; la capacidad corporativa no constituye un compromiso de volumen para el CLIENTE.

El catálogo de la empresa se organiza en productos de software, servicios profesionales y servicios de infraestructura y conectividad.

### 1.1.1 Productos de Software

Los productos cubren tres necesidades de la operación:

- **Aplicaciones móviles de terreno:** Soluciones *offline-first* para fuerzas de venta, reparto y captura de información en campo, con sincronización asíncrona y resolución determinista de conflictos ante intermitencia de red.

- **Plataformas de monitoreo y telemetría:** Sistemas de seguimiento para flotas de transporte y cadena de frío, con generación de alertas ante desviaciones operacionales o térmicas.

- **Núcleos transaccionales y de gestión:** Sistemas para administración de inventarios, facturación y planificación logística, desplegados en arquitecturas híbridas.

### 1.1.2 Servicios Profesionales

Los servicios profesionales acompañan la construcción y la adopción del sistema:

- **Implementación e integración de sistemas:** Diseño, despliegue y puesta en marcha de soluciones integradas con sistemas existentes del cliente.

- **Operación y soporte continuo:** Monitoreo, atención de incidentes y mesa de ayuda bajo acuerdos de nivel de servicio.

- **Consultoría técnica y regulatoria:** Asesoría en procesos operacionales y cumplimiento normativo aplicable a los sectores atendidos.

- **Gestión del cambio y capacitación:** Acompañamiento en la adopción de nuevas tecnologías y formación de usuarios finales.

### 1.1.3 Servicios de Infraestructura y Conectividad

La empresa también presta servicios para sostener la operación en terreno:

- **Suministro de hardware especializado:** Provisión y soporte de equipamiento tecnológico para operaciones de terreno, mediante alianzas con proveedores certificados.

- **Conectividad y redundancia:** Soluciones de comunicación para asegurar continuidad operacional en ubicaciones remotas o con conectividad limitada.

- **Continuidad y recuperación ante desastres:** Servicios para sostener la disponibilidad de sistemas críticos ante contingencias.

## 1.2 Estructura Organizacional

LafroX organiza su trabajo en las áreas de Ingeniería, Infraestructura, Calidad y Seguridad. La dotación técnica de planta asignable a proyectos es de 124 especialistas. La Figura [1.1](LAFROX-Subdocumento1.md#fig:organigrama) muestra cómo estas áreas se relacionan con la Gerencia General y la Dirección de Operaciones.

<a id="fig:organigrama"></a>

**Figura 1.1 — Estructura organizacional corporativa de LafroX. Fuente: Elaboración propia.**

![Organigrama corporativo de LafroX](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX-sd1-latex/figuras/Figura%201.1.pdf)

La Dirección de Operaciones coordina tres divisiones, cada una con una responsabilidad distinta:

- **Ingeniería:** desarrolla el software y reúne las especialidades de datos, arquitectura e integración.

- **Infraestructura:** sostiene la operación de los servicios mediante el NOC, los equipos de confiabilidad (SRE) y redes.

- **Calidad:** realiza las pruebas y revisa la aplicación de los procesos de ingeniería.

El CISO reporta directamente a la Gerencia General, por una línea independiente de la Dirección de Operaciones. Así, los asuntos de seguridad pueden escalarse sin pasar por los responsables de entrega. Calidad depende de Operaciones, pero ejerce su veto sobre los pasos a producción ante el Comité de Calidad y Procesos. Si hay desacuerdo, lo eleva a la Gerencia General; un plazo de entrega no permite levantar ese veto.

La Tabla [1.1](LAFROX-Subdocumento1.md#tab:dotacion) distribuye los 124 especialistas por área y sede e indica su antigüedad en LafroX. No incluye a la Gerencia General, la Dirección de Operaciones ni las funciones de gestión, comercial y administración, que no se asignan a proyectos.

<a id="tab:dotacion"></a>

**Tabla 1.1 — Dotación técnica por área, sede y antigüedad. Fuente: antecedentes corporativos declarados por LafroX.**

| **División** | **Área / rol principal** | **Sede** | **Personas** | **Antigüedad en LafroX** |
| --- | --- | --- | --- | --- |
| Ingeniería | Desarrollo de software (PHP/Laravel, móvil Kotlin) | Central (Santiago) | 48 | 1–8 años |
| Ingeniería | Arquitectura e integración | Central (Santiago) | 15 | 3–10 años |
| Infraestructura | NOC 24×7 | Operaciones (Valparaíso) | 32 | 1–7 años |
| Infraestructura | SRE y Cloud | Operaciones (Valparaíso) | 12 | 2–8 años |
| Calidad | Aseguramiento y automatización de pruebas | Central (Santiago) | 10 | 2–9 años |
| Seguridad | CISO y especialistas en ciberseguridad | Central (Santiago) | 7 | 2–8 años |
| **Total** | | | **124** | |

La dotación se concentra en dos frentes: Ingeniería reúne 48 + 15 = 63 especialistas e Infraestructura, 32 + 12 = 44. Calidad aporta 10 y Seguridad, 7; la suma es 63 + 44 + 10 + 7 = 124. Esta distribución distingue la construcción del software de su operación y de sus controles.

La antigüedad corresponde al tiempo de permanencia en LafroX, no a los años totales de experiencia profesional. Los rangos combinan personal estable con incorporaciones recientes; en Arquitectura e Integración, la permanencia de 3–10 años favorece la continuidad de las decisiones y el conocimiento de las interfaces.

Los 32 profesionales del NOC se organizan en cuatro equipos de siete y cuatro reemplazos comunes: 4×7+4=32. Cada equipo reúne un responsable de turno, cinco operadores y una persona habilitada para relevar puestos durante pausas y traspasos. La Tabla [1.2](LAFROX-Subdocumento1.md#tab:turnos_noc) resume esta distribución corporativa; los equipos rotan entre franjas y días de descanso, no trabajan todos los días ni quedan asignados permanentemente al turno nocturno.

<a id="tab:turnos_noc"></a>

**Tabla 1.2 — Distribución de los 32 profesionales del NOC. Fuente: esquema de operación declarado por LafroX.**

| **Asignación** | **Personas** |
| --- | --- |
| Cuatro equipos rotativos de siete integrantes | 28 |
| Reemplazos comunes habilitados para cubrir puestos | 4 |
| **Total NOC** | **32** |

Los turnos cubren las franjas 00:00–08:00, 08:00–16:00 y 16:00–24:00, hora local de Chile: 3×8=24 horas diarias. Se mantienen seis puestos activos, mientras el séptimo integrante del equipo y los cuatro reemplazos comunes permiten organizar relevos y ausencias. El dimensionamiento usa 40 horas semanales por persona: 32×40=1.280 horas de dotación frente a 6×24×7=1.008 horas de cobertura continua. Las 272 horas de diferencia se destinan a descansos dentro del turno, traspasos, formación y ausencias; son un margen bruto de planificación, no horas disponibles para otro contrato. El cuadrante mensual distribuye los turnos y los descansos de cada persona e incorpora los cambios de horario de Chile, sin depender de horas extraordinarias permanentes.

La continuidad se sostiene con tres reglas:

- **Relevo:** el turno saliente registra los incidentes abiertos, su prioridad, la siguiente acción y el responsable. El entrante confirma la recepción en el mismo registro; el cambio de turno no cierra ni reinicia los plazos del incidente.

- **Reemplazos:** vacaciones y formación se programan en el cuadrante. Ante una ausencia imprevista se activa un reemplazo habilitado para el puesto, incluido el de responsable de turno. Si el margen no alcanza, Operaciones incorpora un reemplazo adicional antes de dejar un puesto sin cobertura.

- **Escalamiento:** el responsable de turno coordina la atención y deriva a SRE o al especialista que corresponda. El relevo conserva la responsabilidad del incidente hasta que otro equipo acepta expresamente su atención.

Esta dotación atiende el NOC corporativo y no equivale a 32 personas dedicadas exclusivamente a Puelche. Para el CLIENTE, el monitoreo es 24×7; la mesa de ayuda conserva el horario de la sección 3.4.5 del Subdocumento 3. El SOC del proyecto se organiza por separado, con analistas bajo la dirección del Encargado de Seguridad. Los recursos del NOC no se cuentan como puestos de mesa ni de SOC.

## 1.3 Gobierno interno Calidad, Seguridad y Conocimiento

El gobierno interno define quién revisa la calidad, quién decide sobre seguridad y cómo se conserva el conocimiento técnico. Cada ámbito tiene responsables, actividades de seguimiento y reglas de escalamiento.

### 1.3.1 Modelo de Gobierno de Calidad

La calidad de los procesos de LafroX se rige por un Sistema de Gestión de Calidad certificado conforme a ISO 9001:2015 y por prácticas evaluadas bajo CMMI-DEV Nivel 3.

Los métodos de diseño, desarrollo, implementación, integración y soporte se ejecutan bajo los procesos de ese Sistema de Gestión de Calidad, cuyo alcance y vigencia se identifican en 1.4. En esta oferta se aplican mediante RUP y DevSecOps (LafroX, 2026, Subdocumento 6, sección 6.2); CMMI-DEV Nivel 3 acredita la madurez de procesos declarada, sin constituir una certificación independiente de esas metodologías (Distribuidora Puelche S.A., 2026b, RT-23.04).

- **Instancia colegiada:** El Comité de Calidad y Procesos, presidido mensualmente por el Jefe de QA y con participación de los líderes de proyecto, analiza la adherencia metodológica y métricas de defecto.

- **Políticas y controles de ingeniería:** Se implementan compuertas de calidad automáticas (*quality gates*) en los canales de integración continua (CI/CD). Es política corporativa rechazar cualquier compilación con cobertura unitaria global inferior al 80% o con hallazgos bloqueantes del análisis estático de código (PHPStan/Larastan y Pint). Esta política no reemplaza la cobertura mínima del 70% de la lógica de negocio exigida para este proyecto: ambos umbrales se verifican de forma independiente en el Formulario T-10.

- **Auditorías internas:** Se ejecutan auditorías internas trimestrales a cargo de auditores líderes certificados, orientadas a evaluar la trazabilidad entre requerimientos, código y matrices de prueba.

### 1.3.2 Modelo de Gobierno de Seguridad de la Información

El marco de seguridad corporativo está alineado y certificado bajo la norma ISO/IEC 27001:2022, implementando un enfoque de confianza cero (*Zero Trust*) y gestión continua del riesgo.

- **Responsable e instancias:** El Oficial de Seguridad de la Información (CISO) lidera el Comité de Seguridad y Privacidad, sesionando con periodicidad mensual para revisar incidentes, vectores de ataque y evaluar la gestión de vulnerabilidades.

- **Procesos DevSecOps:** Se integran análisis estáticos de seguridad de código (SAST) y análisis de composición de software (SCA) en cada confirmación de código. Se realizan pruebas de penetración (*ethical hacking*) externas de forma semestral. Esta cadencia es una política corporativa más exigente que el mínimo contractual, prueba de intrusión anual y antes de cada paso a producción (Distribuidora Puelche S.A., 2026b, RT-11.20), al que incluye y supera.

- **Continuidad operacional:** Se gestionan planes de continuidad de negocio (BCP) y de recuperación ante desastres (DRP), sometidos a simulacros semestrales con corte controlado para verificar los umbrales de RTO ≤ 4 horas y RPO ≤ 15 minutos.

Para Puelche, las pruebas de intrusión serán realizadas por un tercero independiente de LafroX, con periodicidad al menos anual durante la Operación y antes de cada paso a producción. LafroX entregará al CLIENTE cada informe íntegro y su plan de remediación con responsables y plazos (Distribuidora Puelche S.A., 2026b, RT-11.20).

### 1.3.3 Modelo de Gobierno de Gestión del Conocimiento

La gestión del conocimiento busca que la operación no dependa de una sola persona. LafroX conserva las decisiones y los procedimientos mediante dos prácticas:

- **Repositorio corporativo institucional:** El Jefe de QA administra una base centralizada de arquitectura, estándares de codificación, guías de despliegue y recuperación. Todo cierre de incidente crítico (P1 o P2) exige un informe post-mortem aprobado por el responsable técnico y publicado en la base.

- **Talleres de elicitación y traspaso:** Los líderes de dominio realizan sesiones trimestrales para transformar conocimiento no estructurado en manuales reproducibles. El Comité de Calidad revisa semestralmente su vigencia y asigna responsables de actualización.

## 1.4 Experiencia y Certificaciones

Los proyectos, volúmenes, números de certificado y alianzas de este capítulo son declarados por LafroX; su acreditación documental (certificados y cartas de referencia del Art. 34°) se entrega en el Sobre N° 1.

Los antecedentes institucionales declarados son los siguientes:

- **ISO 9001:2015 (Sistema de Gestión de la Calidad):** Certificado N° BV-CH-94821 emitido por Bureau Veritas en su renovación de noviembre de 2025 (Bureau Veritas, 2025). Alcance: ``Diseño, desarrollo, implementación, integración y soporte de sistemas de software logístico y transaccional''. Vigente hasta noviembre de 2028.

- **ISO/IEC 27001:2022 (Sistema de Gestión de Seguridad de la Información):** Certificado N° SI-0312/2023 emitido por AENOR (AENOR, 2023). Alcance: ``Operación de servicios cloud, centros de datos on-premise y procesos de ingeniería de software de misión crítica''. Vigente hasta enero de 2027.

- **CMMI-DEV Nivel 3 (Modelo de Madurez de Capacidades para Desarrollo):** Evaluación SCAMPI A N° 58190, emitida en noviembre de 2023 por un evaluador acreditado ante el CMMI Institute (CMMI Institute, 2023), con validez de tres años, hasta noviembre de 2026. Valida la estandarización y madurez de los procesos organizacionales de ciclo de vida del software.

- **ISO/IEC 20000-1:2018 (Sistema de Gestión de Servicios de TI):** Certificado N° CL21/8190 emitido por SGS (SGS, 2024). Alcance: ``Provisión de servicios de TI, gestión de incidentes y mesa de ayuda 24×7 para infraestructuras logísticas críticas''. Vigente hasta mayo de 2027.

Las certificaciones con vencimiento durante el contrato se renuevan mediante auditoría de recertificación ante el mismo organismo antes de su fecha de término: ISO/IEC 27001 antes de enero de 2027, ISO/IEC 20000-1 antes de mayo de 2027 e ISO 9001 antes de noviembre de 2028. La evaluación CMMI-DEV se renueva con una nueva evaluación SCAMPI A antes de noviembre de 2026, y su renovación se presenta ante la Contraparte Técnica junto con la línea base del H1. Mientras no se acredite, el proyecto no invoca ese nivel como garantía y se rige por los procesos auditados bajo ISO 9001. LafroX acredita la vigencia de cada certificado ante la Contraparte Técnica durante los 56 meses del contrato. Las Bases Técnicas Transversales admiten, para ISO/IEC 27001, un certificado vigente o un plan de certificación con hitos dentro de los primeros doce meses, y para ISO/IEC 20000-1 un certificado vigente o un plan declarado (Distribuidora Puelche S.A., 2026b, sección 15.2; 2026a, Art. 34°). LafroX supera ese mínimo: acredita ambos certificados vigentes a la fecha de la oferta, junto con ISO 9001.

En concordancia con el artículo 34 de las Bases Administrativas (Distribuidora Puelche S.A., 2026a) y con las reglas de entrega de formularios (Distribuidora Puelche S.A., 2026d, sección 1), LafroX presenta en el Formulario T-6 el detalle de tres proyectos finalizados en los últimos cinco años y en operación continua, los cuales demuestran experiencia en complejidad técnica y volumétrica equivalente a la del caso:

- **Sistema Híbrido de Reparto y Gestión Logística (LogiNacional S.A.):** Ejecutado entre 2021 y 2022, integró un núcleo logístico modular, ERP y facturación electrónica sobre nube pública y servidores de borde en 14 centros de distribución. Soporta 420 camiones y 22.000 entregas diarias bajo SLA contractual de 99,5%.

- **Plataforma de Telemetría y Cadena de Frío IoT (FarmaRed S.A.):** Ejecutada entre 2022 y 2023, monitorea cámaras a -22 °C y una flota refrigerada; procesa más de 12 millones de mediciones mensuales bajo SLA de 99,9%.

- **Sistema Móvil de Preventa y Ruteo Desconectado (Comercializadora Lácteos del Sur S.A.):** Ejecutado entre 2023 y 2024, habilita a 280 preventistas y procesa 18.000 transacciones comerciales diarias mediante sincronización determinista en diferido y políticas de crédito locales.

La Tabla [1.3](LAFROX-Subdocumento1.md#tab:equivalencia) compara la flota, los sitios, la preventa y la temperatura de trabajo de las referencias con Puelche. La disponibilidad se incluye para distinguir los SLA históricos de la exigencia de infraestructura del caso (Distribuidora Puelche S.A., 2026c, secciones 2.2 a 2.4 y cap. 10).

<a id="tab:equivalencia"></a>

**Tabla 1.3 — Equivalencia entre el caso y los proyectos del Formulario T-6. Fuente: elaboración propia a partir del caso y del Formulario T-6.**

| **Dimensión de Puelche** | **Valor del caso** | **Proyecto de referencia** | **Valor del proyecto** |
| --- | --- | --- | --- |
| Flota | 96 camiones, 28 con frío | 1 y 2 | 420 camiones; 180 vehículos refrigerados |
| Entregas diarias | ≈ 1.400; ≈ 2.600 en peak | 1 | 22.000 |
| Instalaciones con borde | 5 o 6 | 1 | 14 centros de distribución |
| Preventistas desconectados | 62 | 3 | 280 |
| Congelado | -22 °C | 2 | -22 °C |
| Disponibilidad | 99,95 % de infraestructura | 1 y 2 | 99,5 % y 99,9 % |

Las referencias aportan experiencia en operaciones de mayor escala: el Proyecto 1 combina 14 centros de distribución y 420 camiones; el Proyecto 2 trabaja con cadena de frío; y el Proyecto 3 cubre la preventa sin señal. Este último no es híbrido según el Artículo 16°, por lo que su aporte es la operación móvil desconectada, no la infraestructura local.

Los SLA de 99,5% y 99,9% del T-6 corresponden a servicios de esos proyectos; el 99,95% de Puelche corresponde a infraestructura. No son mediciones equivalentes ni una prueba de cumplimiento del nuevo contrato. La propuesta debe responder a esa exigencia mediante su diseño y sus pruebas de aceptación.

### 1.4.1 Cartera de Clientes

La cartera declarada reúne clientes de logística, distribución de consumo masivo y transporte. Esos sectores comparten con Puelche necesidades de coordinación entre centros, trazabilidad y trabajo en terreno.

Entre los clientes activos y relaciones comerciales vigentes de LafroX, destacan:

- **LogiNacional S.A.** – Operador logístico y de distribución de carga terrestre, con cobertura nacional.

- **FarmaRed S.A.** – Cadena de distribución farmacéutica con exigencias de trazabilidad y cadena de frío.

- **Comercializadora Lácteos del Sur S.A.** – Empresa de consumo masivo con fuerza de preventa en terreno.

- **TransAndina Cargo S.A.** – Empresa de transporte de carga pesada interregional, con flota propia de más de 300 camiones.

- **Supermercados del Maipo S.A.** – Cadena de retail de consumo masivo con centros de distribución regionales.

- **NutriChile Alimentos S.A.** – Empresa de manufactura y distribución de alimentos refrigerados y congelados.

- **Congelados del Pacífico S.A.** – Empresa exportadora de productos del mar con cadena de frío en puertos y centros de acopio.

- **Distribuidora Andes Retail S.A.** – Distribuidora mayorista de productos de consumo masivo con operación multirregional y bodegas de tránsito.

Los tres primeros clientes corresponden a los proyectos detallados en el T-6. Las demás referencias amplían la cartera declarada, pero no reemplazan los antecedentes de experiencia exigidos en ese formulario.

## 1.5 Estructura para Proyecto

La organización del proyecto mantiene una jefatura responsable durante los 56 meses del contrato y separa la dirección de las especialidades técnicas (Distribuidora Puelche S.A., 2026a, Art. 17°).

El proyecto será liderado de forma exclusiva y continua por el Jefe de Proyecto nominado, **Alex Aravena**, quien actuará como interlocutor único frente a la contraparte técnica y directiva del cliente. Reportando directamente al Jefe de Proyecto, se constituye un comité técnico compuesto por siete líderes de dominio especializados, que cubren los roles mínimos del numeral 19.2 de las Bases Técnicas Transversales según la Tabla [1.4](LAFROX-Subdocumento1.md#tab:roles_minimos):

- **Arquitecto de Solución (Bastián Trejo):** Responsable del diseño técnico global, la consistencia entre capas lógicas y la articulación del modelo híbrido nube/on-premise.

- **Encargado de Seguridad de la Información (Álvaro Catalán):** Responsable del cumplimiento de la norma ISO/IEC 27001, la arquitectura Zero Trust y los controles de acceso.

- **Líder de Datos (Leandro Chamorro):** Responsable de la modelación relacional, la estrategia de migración y la reconciliación determinista de inventarios.

- **Líder de Desarrollo (Tomás Pérez):** Responsable del desarrollo del monolito modular Laravel/PHP definido en el Subdocumento 4, con perfiles de ejecución y escalamiento de sus componentes críticos, de los componentes móviles y del canal de entrega continua.

- **Líder de Calidad (Maximiliano Miño):** Responsable del plan de pruebas, automatización y cumplimiento de los umbrales de aseguramiento de calidad ISO/IEC 25010.

- **Líder de Operación / SRE (Guillermo Castillo):** Responsable de la disponibilidad continua 24×7, observabilidad de infraestructura y gestión de niveles de servicio. Durante la Operación es, además, el gerente de servicio dedicado y la contraparte permanente del CLIENTE (Distribuidora Puelche S.A., 2026b, RT-21.02).

- **Líder de Implantación y Gestión del Cambio (Patricio Henríquez):** Responsable de la adopción en terreno, capacitación de preventistas y conductores, y marchas blancas.

La Tabla [1.4](LAFROX-Subdocumento1.md#tab:roles_minimos) resume la asignación y el período de participación de los diez roles del numeral 19.2 (Distribuidora Puelche S.A., 2026b). Las funciones se explican en el texto anterior; aquí se comparan responsables y dedicaciones, sin repetir su descripción.

<a id="tab:roles_minimos"></a>

**Tabla 1.4 — Asignación y dedicación de los roles del proyecto. Fuente: elaboración propia a partir de las Bases Técnicas Transversales, numeral 19.2.**

| **Rol** | **Responsable** | **Dedicación asignada** |
| --- | --- | --- |
| Jefe de Proyecto | Alex Aravena | 100% meses 1–21; dirección en Operación |
| Arquitecto de Solución | Bastián Trejo | 100% meses 1–21; Comité hasta mes 56 |
| Líder de Integración | Bastián Trejo | Incluido en el 100% de meses 1–21 |
| Encargado de Seguridad | Álvaro Catalán | Meses 1–56 |
| Líder de Datos | Leandro Chamorro | Meses 1–21 |
| Líder de Desarrollo | Tomás Pérez | 100% meses 1–21 |
| Líder Funcional | Patricio Henríquez | 100% meses 1–21 |
| Líder de Calidad y Pruebas | Maximiliano Miño | Meses 1–56 |
| Líder de Operación / SRE | Guillermo Castillo | Meses 1–56; 100% en Operación (21–56) |
| Líder de Implantación | Patricio Henríquez | Incluido en el 100% de meses 1–21 |

Los diez roles se distribuyen entre ocho personas: Trejo asume Arquitectura e Integración y Henríquez, el frente Funcional y la Implantación. Esa acumulación no suma dos dedicaciones de 100% para una misma persona. Trejo dirige el equipo de interfaces con ERP y terceros; Henríquez coordina el levantamiento, las reglas de negocio, los prototipos y las pruebas de aceptación con analistas funcionales y el equipo de implantación. Los recursos de apoyo se programan en el T-15, sección 5.7 del Subdocumento 7.

La participación de Operación desde el mes 1 cubre el mínimo de incorporación desde el mes 6; Implantación participa desde el mes 1 y cubre el mínimo del mes 8. Si la carga de las marchas blancas lo requiere, se nomina un Líder de Implantación separado sin reducir la dedicación del Líder Funcional. La experiencia y las cartas de compromiso se acreditan conforme a las Bases. Durante los meses 1–4, Desarrollo trabaja en diseño y prototipos, antes de la construcción.

Alex Aravena, Jefe de Proyecto y apoderado de LafroX, tendrá facultades para comprometer al ADJUDICATARIO en materias de ejecución durante toda la implementación, manteniendo la dedicación exclusiva declarada. Los cambios de alcance, plazo o costo se someterán a las instancias de aprobación previstas (Distribuidora Puelche S.A., 2026b, RT-19.02).

LafroX mantendrá vigentes las certificaciones del equipo asignado durante todo el contrato y, ante la salida de una persona certificada, propondrá un reemplazo de perfil igual o superior, con certificación vigente y dedicación equivalente. El reemplazo requerirá autorización previa y escrita del CLIENTE, acreditación documental y traslape mínimo de quince días hábiles, sin costo adicional (Distribuidora Puelche S.A., 2026b, RT-15.09; 2026a, Art. 76°).

## 1.6 Alianzas

Las alianzas corporativas cubren nube, equipos de terreno y comunicaciones. Su relación con el modelo híbrido exigido por el Artículo 16° se explica a continuación. Las alianzas que vencen durante el contrato se renuevan antes de su término y su vigencia se presenta a la Contraparte Técnica:

- **Amazon Web Services (AWS Partner Network – Advanced Tier Services):** LafroX es socio tecnológico nivel Advanced, con competencias certificadas en DevOps y Migración. El vínculo contempla soporte empresarial, pruebas de concepto y revisiones arquitectónicas bajo Well-Architected, según las condiciones del programa y del servicio contratado. Vigente hasta marzo de 2027.

- **Zebra Technologies (Premier Solution Partner):** Alianza formal para el suministro, soporte de fábrica y mantenimiento de terminales móviles industriales, lectores de códigos de barra e impresoras térmicas portátiles con certificación de operación en ambientes hostiles y cámaras de congelación a -25 °C. Vigente hasta junio de 2027.

- **Fortinet / Cisco (Select Partner):** Alianza para el aprovisionamiento de equipamiento de conectividad de borde, switches industriales y firewalls de red SD-WAN requeridos para enlazar de manera segura los centros de distribución y salas técnicas on-premise. Vigente hasta septiembre de 2027.

- **Starlink Business (Authorized Enterprise Reseller):** Convenio para la provisión e integración de terminales satelitales de baja órbita con prioridad de tráfico corporativo, como medio alternativo de comunicación ante caídas de enlace en centros de distribución, cross-dockings y almacenes remotos. Vigente hasta diciembre de 2027.

Estas alianzas cubren funciones distintas: AWS aporta servicios de nube; Zebra, equipos de captura; Fortinet/Cisco, redes de borde; y Starlink, un enlace alternativo. Ninguna sustituye la verificación de los equipos ni las pruebas de continuidad. Las especificaciones de los implementos se detallan en el Formulario T-11 del Subdocumento 4; la participación de socios en este proyecto corresponde a 12.3.

## Referencias

Las fuentes citadas en este documento se listan a continuación en formato APA 7.ª edición.

- AENOR. (2023). *Certificado de Sistema de Gestión de Seguridad de la Información ISO/IEC 27001:2022 N° SI-0312/2023*. AENOR Internacional.

- Bureau Veritas. (2025). *Certificado de Sistema de Gestión de la Calidad ISO 9001:2015 N° BV-CH-94821*. Bureau Veritas Certification.

- CMMI Institute. (2023). *CMMI for Development, Version 2.0: Maturity Level 3 SCAMPI A Appraisal Report N° 58190*. CMMI Institute.

- Distribuidora Puelche S.A. (2026a). *Bases Administrativas de Licitación N° TFEP-01/2026: Contratación de Solución Integral de Software y Servicios de Operación*.

- Distribuidora Puelche S.A. (2026b). *Bases Técnicas Transversales de Licitación N° TFEP-01/2026*.

- Distribuidora Puelche S.A. (2026c). *Caso: Logística – Especificaciones del Problema y Operación de Distribuidora Puelche S.A.*

- Distribuidora Puelche S.A. (2026d). *Aclaraciones de la Licitación N° TFEP-01/2026*.

- LafroX. (2026). *Subdocumento 6: Metodologías*.

- SGS. (2024). *Certificado de Sistema de Gestión de Servicios de TI ISO/IEC 20000-1:2018 N° CL21/8190*. SGS United Kingdom Ltd.

## Declaración de uso de IA

La Tabla [1.5](LAFROX-Subdocumento1.md#tab:declaracion_ia) identifica las herramientas y el alcance de la asistencia utilizada, conforme a la sección 7.2 de las Aclaraciones (Distribuidora Puelche S.A., 2026d). La declaración se consolida en el Formulario A-6.

<a id="tab:declaracion_ia"></a>

**Tabla 1.5 — Uso de IA por sección y formulario. Fuente: registro del equipo.**

| **Sección** | **Herramienta** | **Finalidad del uso** | **Nivel en texto** | **Nivel en diagramas** | **Revisión humana (quién y qué verificó)** |
| --- | --- | --- | --- | --- | --- |
| 1.1 | Claude / Gemini; OpenAI Codex | Redacción de trayectoria y servicios | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 1.2 | Claude / Gemini; OpenAI Codex | Organigrama, antigüedad, turnos y respaldos del NOC | Alto | Medio | [[REVISIÓN HUMANA]] |
| 1.3 | Claude / Gemini; OpenAI Codex | Redacción de gobierno y responsabilidades | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 1.4 | Claude / Gemini; OpenAI Codex | Comparación de experiencia y SLA | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 1.5 | Claude / Gemini; Claude Code; OpenAI Codex | Síntesis de roles y dedicaciones | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 1.6 | Claude / Gemini; OpenAI Codex | Redacción de alcance de alianzas | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| Anexos SD1 | OpenAI Codex | Reformulación y referencias | Bajo | Ninguno | [[REVISIÓN HUMANA]] |
| T-6 | Claude / Gemini; OpenAI Codex | Formato, introducción y referencias | Bajo | Ninguno | [[REVISIÓN HUMANA]] |

La asistencia en texto se concentra en la redacción y la síntesis del capítulo; el organigrama conserva el nivel de asistencia declarado para su elaboración. Las seis secciones requieren revisión humana de su versión actual. El T-6 requiere también la revisión de su presentación actual; los once campos de experiencia se mantienen sin cambios.
