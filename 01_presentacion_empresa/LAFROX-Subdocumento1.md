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

Este capítulo presenta la trayectoria, las capacidades instaladas, los servicios y la organización de LafroX. Describe su gobierno de calidad, seguridad y conocimiento, y analiza su experiencia en logística. La sección 1.5 explica la organización para el proyecto de Distribuidora Puelche S.A. El Formulario T-6 detalla tres proyectos de referencia. La arquitectura y el plan de trabajo se desarrollan en los Subdocumentos 4 y 7, y el equipo nominado en el Capítulo 12.

## 1.1 Presentación de la empresa

LafroX fue fundada en 2012 en Santiago de Chile, donde mantiene su Sede Central. Su Centro de Operaciones y domicilio declarado se encuentran en Av. Brasil 2241, Valparaíso. Se dedica al desarrollo, la integración y la operación de sistemas para logística, distribución de consumo masivo y transporte de carga. Su experiencia se concentra en operaciones con instalaciones dispersas, conectividad intermitente y exigencias de trazabilidad.

Entre los principales hitos de su trayectoria destacan la puesta en marcha de su primera plataforma de ruteo y telemetría en 2015, la acreditación como integrador certificado de hardware industrial para cadenas de frío en 2018, la primera certificación corporativa en normas de calidad y seguridad en 2021, mantenida mediante auditorías de seguimiento y renovación, y la consolidación de su arquitectura modular híbrida en 2024. Entre sus operaciones de referencia figuran las 22.000 entregas diarias del Proyecto 1 y las 18.000 transacciones comerciales diarias del Proyecto 3 del Formulario T-6.

El sitio web corporativo de LafroX, <https://lafrox.github.io/>, reúne la trayectoria, los servicios, la organización, las sedes, los proyectos de referencia, las certificaciones declaradas y las alianzas tecnológicas de la empresa.

LafroX trabaja en tres líneas de negocio:

- **Ingeniería de software en el borde (Edge Computing):** Desarrollo de aplicaciones móviles y sistemas locales que permiten trabajar sin conexión (*offline-first*), conservar los datos capturados y sincronizarlos cuando se restablece la comunicación.

- **Trazabilidad y telemetría de frío industrial:** Integración de termógrafos vehiculares, sensores y terminales de captura para registrar temperaturas y eventos de custodia en el transporte y almacenamiento de productos.

- **Arquitecturas modulares híbridas de misión crítica:** Diseño, despliegue y soporte de plataformas que combinan servicios en nube pública con componentes locales en centros de distribución. Esta combinación permite sostener funciones de terreno ante cortes de conectividad.

Estas líneas se apoyan en dos capacidades operativas:

- **Infraestructura y ambientes:** Plataforma de cómputo en nube pública y dos centros de datos, primario y secundario en configuración activo-pasivo. Soportan cinco ambientes segregados: Desarrollo (DEV), Aseguramiento de Calidad (QA), Preproducción (PREPROD), Producción (PROD) y Recuperación ante Desastres (DR). La capacitación utiliza datos ficticios en espacios aislados dentro de estos ambientes. Los ejercicios semestrales de recuperación verifican objetivos de tiempo de restitución (RTO) de hasta cuatro horas y pérdida de datos (RPO) de hasta quince minutos.

- **Centro de Operaciones y Mesa de Servicios:** Desde Valparaíso, LafroX mantiene el Centro de Operaciones de Red (NOC), que supervisa la infraestructura, el Centro de Operaciones de Seguridad (SOC), que vigila y analiza amenazas, y la Mesa de Servicios, que recibe consultas, solicitudes e incidentes de los usuarios. La mesa presta atención inicial y deriva los casos que requieren intervención especializada mediante niveles de escalamiento L1, L2 y L3. La cobertura de cada servicio se define en el acuerdo con su cliente.

La capacidad instalada combina equipos asignados a las especialidades y puestos compartidos del Centro de Operaciones. La Tabla [1.1](LAFROX-Subdocumento1.md#tab:equipamiento_corporativo) presenta el inventario corporativo de trabajo. El equipamiento que se suministra al cliente se detalla por separado en el Formulario T-11 del Subdocumento 4 (LafroX, 2026a).

<a id="tab:equipamiento_corporativo"></a>

**Tabla 1.1 — Equipamiento corporativo de trabajo y atención. Fuente: antecedentes corporativos declarados por LafroX.**

| **Equipamiento** | **Cantidad** | **Sede** | **Uso** |
| --- | --- | --- | --- |
| Equipos de Ingeniería, Calidad, Seguridad y SRE | 92 | Santiago: 80; Valparaíso: 12 | Desarrollo, pruebas, seguridad y administración de plataforma |
| Puestos compartidos del Centro de Operaciones | 16 | Valparaíso | Supervisión de infraestructura y atención de usuarios |
| Equipos de reemplazo | 4 | Dos en cada sede | Sustitución temporal de equipos de trabajo |
| **Total de equipos de cómputo** | **112** | | |

Los 92 equipos asignados corresponden a los especialistas de Ingeniería, Calidad, Seguridad y SRE: 48 + 15 + 10 + 7 + 12 = 92. De ellos, 80 trabajan en Santiago y 12 en Valparaíso. Los 32 profesionales del NOC comparten ocho puestos conforme a sus turnos. Cada puesto de atención incluye computador, monitor, auriculares y acceso a las herramientas del servicio. El inventario suma 92 equipos asignados, 16 puestos compartidos y cuatro equipos de reemplazo: 112 equipos de cómputo.

La Tabla [1.2](LAFROX-Subdocumento1.md#tab:puestos_operaciones) distingue los puestos de servicio de los puestos destinados a relevos y contingencias.

<a id="tab:puestos_operaciones"></a>

**Tabla 1.2 — Distribución de puestos del Centro de Operaciones. Fuente: antecedentes corporativos declarados por LafroX.**

| **Servicio** | **Puestos habilitados** | **Puestos de servicio simultáneos** | **Puestos de relevo o reserva** |
| --- | --- | --- | --- |
| NOC | 8 | 6 | 2 |
| Mesa de Servicios | 8 | Hasta 7 | 1 |

El NOC mantiene seis puestos activos de supervisión continua y dos habilitados para relevos o contingencias. La mesa dispone de siete puestos de atención y uno de reserva. Los agentes son las personas que atienden a los usuarios y utilizan esos puestos. Su dotación y sus turnos se dimensionan para cada servicio contratado. Los agentes de mesa y los analistas contratados del SOC se contabilizan por separado de los 124 especialistas de la Tabla [1.3](LAFROX-Subdocumento1.md#tab:dotacion). El dimensionamiento de la mesa para Puelche se detalla en el Subdocumento 4, Anexo 4-W.7, y el Formulario T-15, secciones 7.4.1 y 7.5.6.

El catálogo de la empresa se organiza en productos de software, servicios profesionales y servicios de infraestructura y conectividad.

### 1.1.1 Productos de Software

Los productos cubren tres necesidades de la operación:

- **Aplicaciones móviles de terreno:** Aplicaciones para fuerzas de venta, reparto y captura de información en campo. Permiten registrar operaciones sin conexión y sincronizarlas al recuperar la comunicación.

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

LafroX organiza su trabajo en las áreas de Ingeniería, Infraestructura, Calidad y Seguridad. La dotación técnica de planta asignable a proyectos es de 124 especialistas. La Gerencia General dirige la empresa. La Figura [1.1](LAFROX-Subdocumento1.md#fig:organigrama) muestra las dependencias de sus áreas y la línea de reporte de Seguridad.

<a id="fig:organigrama"></a>

**Figura 1.1 — Estructura organizacional corporativa de LafroX. Fuente: elaboración a partir de los antecedentes corporativos declarados por LafroX.**

![Organigrama corporativo de LafroX](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX-sd1-latex/figuras/Figura%201.1.pdf)

La Dirección de Operaciones coordina tres divisiones, cada una con una responsabilidad distinta:

- **Ingeniería:** desarrolla el software y reúne las especialidades de datos, arquitectura e integración.

- **Infraestructura:** sostiene la operación de los servicios mediante el NOC, los equipos de confiabilidad de servicios (SRE) y redes.

- **Calidad:** realiza las pruebas y revisa la aplicación de los procesos de ingeniería.

El Oficial de Seguridad de la Información, denominado CISO por la sigla inglesa de *Chief Information Security Officer*, dirige la función de seguridad. Reporta directamente a la Gerencia General y se sitúa fuera de la Dirección de Operaciones para evaluar riesgos con independencia de los responsables de entrega. La Dirección de Operaciones coordina Ingeniería, Infraestructura y Calidad. El Jefe de Calidad puede bloquear un paso a producción si no se cumplen los controles exigidos. El Comité de Calidad y Procesos revisa las observaciones y los desacuerdos se escalan a la Gerencia General.

La Tabla [1.3](LAFROX-Subdocumento1.md#tab:dotacion) distribuye los 124 especialistas por área y sede e indica su antigüedad en LafroX. Este total corresponde a la dotación técnica de planta. La Gerencia General, la Dirección de Operaciones, las funciones comerciales y administrativas, los agentes de mesa y los analistas contratados del SOC se contabilizan por separado.

<a id="tab:dotacion"></a>

**Tabla 1.3 — Dotación técnica por área, sede y antigüedad. Fuente: antecedentes corporativos declarados por LafroX.**

| **División** | **Área / rol principal** | **Sede** | **Personas** | **Antigüedad en LafroX** |
| --- | --- | --- | --- | --- |
| Ingeniería | Desarrollo de software | Central (Santiago) | 48 | 1–8 años |
| Ingeniería | Arquitectura e integración | Central (Santiago) | 15 | 3–10 años |
| Infraestructura | NOC 24×7 | Operaciones (Valparaíso) | 32 | 1–7 años |
| Infraestructura | SRE y nube | Operaciones (Valparaíso) | 12 | 2–8 años |
| Calidad | Aseguramiento y automatización de pruebas | Central (Santiago) | 10 | 2–9 años |
| Seguridad | CISO y especialistas en ciberseguridad | Central (Santiago) | 7 | 2–8 años |
| **Total** | | | **124** | |

La dotación se concentra en dos frentes: Ingeniería reúne 48 + 15 = 63 especialistas e Infraestructura, 32 + 12 = 44. Calidad aporta 10 y Seguridad, 7; la suma es 63 + 44 + 10 + 7 = 124. Esta distribución distingue la construcción del software de su operación y de sus controles.

La antigüedad indica el tiempo de permanencia en LafroX. Los rangos combinan personal estable con incorporaciones recientes y permiten reconocer la continuidad del equipo en cada especialidad.

Los 32 profesionales del NOC se organizan en cuatro equipos de siete y cuatro reemplazos comunes: 4×7+4=32. Cada equipo reúne un responsable de turno, cinco operadores y una persona habilitada para relevar puestos durante pausas y traspasos. La Tabla [1.4](LAFROX-Subdocumento1.md#tab:turnos_noc) resume esta distribución. Los equipos rotan entre las franjas de atención y sus días de descanso.

<a id="tab:turnos_noc"></a>

**Tabla 1.4 — Distribución de los 32 profesionales del NOC. Fuente: esquema de operación declarado por LafroX.**

| **Asignación** | **Personas** |
| --- | --- |
| Cuatro equipos rotativos de siete integrantes | 28 |
| Reemplazos comunes habilitados para cubrir puestos | 4 |
| **Total NOC** | **32** |

Los turnos cubren las franjas 00:00–08:00, 08:00–16:00 y 16:00–24:00, hora local de Chile. Se mantienen seis puestos activos, con relevos organizados entre el séptimo integrante del equipo y los cuatro reemplazos comunes. Para planificar la cobertura se consideran 40 horas semanales por persona: 32×40=1.280 horas de dotación frente a 6×24×7=1.008 horas de supervisión. La diferencia de 272 horas es el margen bruto para pausas, traspasos, formación y ausencias. El cuadrante mensual distribuye los turnos y los descansos e incorpora los cambios de horario de Chile.

La continuidad se sostiene con tres reglas:

- **Relevo:** el turno saliente registra los incidentes abiertos, su prioridad, la siguiente acción y el responsable. El entrante confirma la recepción en el mismo registro; el cambio de turno no cierra ni reinicia los plazos del incidente.

- **Reemplazos:** vacaciones y formación se programan en el cuadrante. Ante una ausencia imprevista se activa un reemplazo habilitado para el puesto, incluido el de responsable de turno. Si el margen no alcanza, Operaciones incorpora un reemplazo adicional antes de dejar un puesto sin cobertura.

- **Escalamiento:** el responsable de turno coordina la atención y deriva a SRE o al especialista que corresponda. El relevo conserva la responsabilidad del incidente hasta que otro equipo acepta expresamente su atención.

Esta dotación sostiene el NOC corporativo. La asignación a cada contrato se organiza dentro de esa división. La supervisión de infraestructura, la atención de usuarios y el análisis de seguridad son funciones distintas, con personal y turnos diferenciados.

## 1.3 Gobierno interno Calidad, Seguridad y Conocimiento

El gobierno interno define quién revisa la calidad, quién decide sobre seguridad y cómo se conserva el conocimiento técnico. Cada ámbito tiene responsables, actividades de seguimiento y reglas de escalamiento.

### 1.3.1 Modelo de Gobierno de Calidad

LafroX dispone de un Sistema de Gestión de Calidad certificado conforme a ISO 9001:2015 y de una evaluación de madurez de sus procesos de desarrollo bajo CMMI-DEV Nivel 3. Los antecedentes, el alcance y la vigencia declarados se identifican en 1.4.

El Sistema de Gestión de Calidad organiza el diseño, desarrollo, implementación, integración y soporte del software mediante procedimientos, responsables y registros de control. La evaluación CMMI se refiere a la madurez de esos procesos. La aplicación de RUP, proceso de desarrollo iterativo, y DevSecOps, integración de desarrollo, seguridad y operación, a este proyecto se detalla en el Subdocumento 6 (LafroX, 2026b, sección 6.2).

- **Instancia colegiada:** El Jefe de Aseguramiento de Calidad (QA) preside el Comité de Calidad y Procesos. El comité se reúne mensualmente con los líderes de proyecto para revisar el cumplimiento de los procedimientos, los defectos detectados y las acciones correctivas.

- **Políticas y controles de ingeniería:** El flujo de integración y entrega continua (CI/CD) incluye controles automáticos de calidad. La política corporativa exige cobertura unitaria global de al menos 80%, análisis estático sin hallazgos bloqueantes y conformidad con el estilo de código. El análisis estático detecta problemas sin ejecutar el programa y el control de estilo revisa su formato. Para este proyecto se verifica además, de forma independiente, una cobertura mínima del 70% de la lógica de negocio en el Formulario T-10.

- **Auditorías internas:** Se ejecutan auditorías internas trimestrales a cargo de auditores líderes certificados, orientadas a evaluar la trazabilidad entre requerimientos, código y matrices de prueba.

### 1.3.2 Modelo de Gobierno de Seguridad de la Información

LafroX gestiona la seguridad mediante su Sistema de Gestión de Seguridad de la Información, cuyo certificado ISO/IEC 27001:2022 se declara en 1.4. Sus controles verifican la identidad y los permisos de acceso, evalúan vulnerabilidades y mantienen planes de continuidad.

- **Responsable e instancias:** El CISO preside el Comité de Seguridad y Privacidad, que se reúne mensualmente para revisar incidentes, amenazas, vulnerabilidades y acciones de tratamiento. El comité coordina la función de seguridad y eleva los riesgos relevantes a la Gerencia General.

- **Procesos DevSecOps:** En cada incorporación de código se ejecutan análisis de seguridad del código fuente (SAST) y de sus dependencias de terceros (SCA). La política corporativa contempla también pruebas de intrusión externas semestrales.

- **Continuidad operacional:** Los planes de continuidad de negocio (BCP) y recuperación ante desastres (DRP) se prueban semestralmente mediante interrupciones controladas. Los ejercicios verifican los objetivos de restitución de hasta cuatro horas y pérdida de datos de hasta quince minutos.

En el proyecto de Puelche, las pruebas de intrusión previas a cada paso a producción complementan las revisiones periódicas. Un tercero independiente de LafroX las realizará, con frecuencia al menos anual durante la Operación y antes de cada paso a producción. Cada informe se entregará íntegro al CLIENTE junto con el plan de remediación, sus responsables y sus plazos (Distribuidora Puelche S.A., 2026b, RT-11.20, p. 24).

### 1.3.3 Modelo de Gobierno de Gestión del Conocimiento

La gestión del conocimiento busca que la operación no dependa de una sola persona. LafroX conserva las decisiones y los procedimientos mediante dos prácticas:

- **Repositorio corporativo institucional:** El Jefe de QA administra una base centralizada de arquitectura, estándares de codificación, guías de despliegue y recuperación. Todo cierre de incidente crítico (P1 o P2) exige un informe post-mortem aprobado por el responsable técnico y publicado en la base.

- **Talleres de elicitación y traspaso:** Los líderes de dominio realizan sesiones trimestrales para transformar conocimiento no estructurado en manuales reproducibles. El Comité de Calidad revisa semestralmente su vigencia y asigna responsables de actualización.

## 1.4 Experiencia y Certificaciones

Los proyectos, volúmenes, números de certificado y alianzas de este capítulo son declarados por LafroX; su acreditación documental (certificados y cartas de referencia del Art. 34°) se entrega en el Sobre N° 1.

Los antecedentes institucionales declarados son los siguientes:

- **ISO 9001:2015 (Sistema de Gestión de la Calidad):** Certificado N° BV-CH-94821 emitido por Bureau Veritas en su renovación de noviembre de 2025 (Bureau Veritas, 2025). Alcance: ``Diseño, desarrollo, implementación, integración y soporte de sistemas de software logístico y transaccional''. Vigente hasta noviembre de 2028.

- **ISO/IEC 27001:2022 (Sistema de Gestión de Seguridad de la Información):** Certificado N° SI-0312/2023 emitido por AENOR (AENOR, 2023). Alcance: ``Operación de servicios cloud, centros de datos on-premise y procesos de ingeniería de software de misión crítica''. Vigente hasta enero de 2027.

- **CMMI-DEV Nivel 3 (Modelo de Madurez de Capacidades para Desarrollo):** Evaluación Benchmark N° 58190, emitida en noviembre de 2023 por un evaluador acreditado ante el CMMI Institute (CMMI Institute, 2023), con validez de tres años, hasta noviembre de 2026. Valida la estandarización y madurez de los procesos organizacionales de ciclo de vida del software.

- **ISO/IEC 20000-1:2018 (Sistema de Gestión de Servicios de TI):** Certificado N° CL21/8190 emitido por SGS (SGS, 2024). Alcance: ``Provisión de servicios de TI, gestión de incidentes y mesa de ayuda 24×7 para infraestructuras logísticas críticas''. Vigente hasta mayo de 2027.

Las certificaciones con vencimiento durante el contrato se renuevan mediante auditoría de recertificación ante el mismo organismo antes de su fecha de término: ISO/IEC 27001 antes de enero de 2027, ISO/IEC 20000-1 antes de mayo de 2027 e ISO 9001 antes de noviembre de 2028. La evaluación CMMI-DEV se renueva con una nueva evaluación Benchmark antes de noviembre de 2026, y su renovación se presenta ante la Contraparte Técnica junto con la línea base del H1. Mientras no se acredite, el proyecto no invoca ese nivel como garantía y se rige por los procesos auditados bajo ISO 9001. LafroX acredita la vigencia de cada certificado ante la Contraparte Técnica durante los 56 meses del contrato. Las Bases Técnicas Transversales admiten, para ISO/IEC 27001, un certificado vigente o un plan de certificación con hitos dentro de los primeros doce meses, y para ISO/IEC 20000-1 un certificado vigente o un plan declarado (Distribuidora Puelche S.A., 2026b, sección 15.2; 2026a, Art. 34°). LafroX supera ese mínimo: acredita ambos certificados vigentes a la fecha de la oferta, junto con ISO 9001.

En concordancia con el artículo 34 de las Bases Administrativas (Distribuidora Puelche S.A., 2026a) y con las reglas de entrega de formularios (Distribuidora Puelche S.A., 2026d, sección 1), LafroX presenta en el Formulario T-6 el detalle de tres proyectos finalizados en los últimos cinco años y en operación continua, los cuales demuestran experiencia en complejidad técnica y volumétrica equivalente a la del caso:

- **Sistema Híbrido de Reparto y Gestión Logística (LogiNacional S.A.):** Ejecutado entre 2021 y 2022, integró un núcleo logístico modular, ERP y facturación electrónica sobre nube pública y servidores de borde en 14 centros de distribución. Soporta 420 camiones y 22.000 entregas diarias bajo SLA contractual de 99,5%.

- **Plataforma de Telemetría y Cadena de Frío IoT (FarmaRed S.A.):** Ejecutada entre 2022 y 2023, monitorea cámaras a -22 °C y una flota refrigerada; procesa más de 12 millones de mediciones mensuales bajo SLA de 99,9%.

- **Sistema Móvil de Preventa y Ruteo Desconectado (Comercializadora Lácteos del Sur S.A.):** Ejecutado entre 2023 y 2024, habilita a 280 preventistas y procesa 18.000 transacciones comerciales diarias mediante sincronización determinista en diferido y políticas de crédito locales.

La Tabla [1.5](LAFROX-Subdocumento1.md#tab:equivalencia) compara la flota, los sitios, la preventa y la temperatura de trabajo de las referencias con Puelche. Los valores operacionales del caso proceden de sus secciones 2.2 a 2.4 (Distribuidora Puelche S.A., 2026c, pp. 4–5). La disponibilidad se incluye para distinguir los SLA históricos de la exigencia de infraestructura de las Bases Técnicas Transversales (Distribuidora Puelche S.A., 2026b, sección 6.1, p. 14, y sección 7.2, pp. 17–18).

<a id="tab:equivalencia"></a>

**Tabla 1.5 — Equivalencia entre el caso y los proyectos del Formulario T-6. Fuente: elaboración a partir de Distribuidora Puelche S.A. (2026b y 2026c) y del Formulario T-6.**

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

La organización del proyecto mantiene una jefatura responsable durante los 56 meses del contrato, que incluyen los 36 meses de operación desde el mes 21, y separa la dirección de las especialidades técnicas (Distribuidora Puelche S.A., 2026a, Art. 17°).

El proyecto será liderado de forma exclusiva y continua por el Jefe de Proyecto nominado, **Alex Aravena**, quien actuará como interlocutor único frente a la contraparte técnica y directiva del cliente. Reportando directamente al Jefe de Proyecto, se constituye un comité técnico compuesto por siete líderes de dominio especializados, que cubren los roles mínimos del numeral 19.2 de las Bases Técnicas Transversales según la Tabla [1.6](LAFROX-Subdocumento1.md#tab:roles_minimos):

- **Arquitecto de Solución (Bastián Trejo):** Responsable del diseño técnico global, la consistencia entre capas lógicas y la articulación del modelo híbrido nube/on-premise.

- **Encargado de Seguridad de la Información (Álvaro Catalán):** Responsable del cumplimiento de la norma ISO/IEC 27001, la arquitectura Zero Trust y los controles de acceso.

- **Líder de Datos (Leandro Chamorro):** Responsable de la modelación relacional, la estrategia de migración y la reconciliación determinista de inventarios.

- **Líder de Desarrollo (Tomás Pérez):** Responsable del desarrollo del monolito modular Laravel/PHP definido en el Subdocumento 4, con perfiles de ejecución y escalamiento de sus componentes críticos, de los componentes móviles y del canal de entrega continua.

- **Líder de Calidad (Maximiliano Miño):** Responsable del plan de pruebas, automatización y cumplimiento de los umbrales de aseguramiento de calidad ISO/IEC 25010.

- **Líder de Operación / SRE (Guillermo Castillo):** Responsable de la disponibilidad continua 24×7, observabilidad de infraestructura y gestión de niveles de servicio. Durante la Operación es, además, el gerente de servicio dedicado y la contraparte permanente del CLIENTE (Distribuidora Puelche S.A., 2026b, RT-21.02).

- **Líder de Implantación y Gestión del Cambio (Patricio Henríquez):** Responsable de la adopción en terreno, capacitación de preventistas y conductores, y marchas blancas.

La Tabla [1.6](LAFROX-Subdocumento1.md#tab:roles_minimos) resume la asignación y el período de participación de los diez roles del numeral 19.2 (Distribuidora Puelche S.A., 2026b). Las funciones se explican en el texto anterior; aquí se comparan responsables y dedicaciones, sin repetir su descripción.

<a id="tab:roles_minimos"></a>

**Tabla 1.6 — Asignación y dedicación de los roles del proyecto. Fuente: elaboración a partir de Distribuidora Puelche S.A. (2026b, numeral 19.2).**

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

Los diez roles se distribuyen entre ocho personas: Trejo asume Arquitectura e Integración y Henríquez, el frente Funcional y la Implantación. Esa acumulación no suma dos dedicaciones de 100% para una misma persona. Trejo dirige el equipo de interfaces con ERP y terceros; Henríquez coordina el levantamiento, las reglas de negocio, los prototipos y las pruebas de aceptación con analistas funcionales y el equipo de implantación. Los recursos de apoyo se programan en el T-15, sección 7.5.7 del Subdocumento 7.

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

- CMMI Institute. (2023). *CMMI for Development, Version 2.0: Maturity Level 3 Benchmark Appraisal Report N° 58190*. CMMI Institute.

- Distribuidora Puelche S.A. (2026a). *Bases Administrativas de Licitación N° TFEP-01/2026: Contratación de Solución Integral de Software y Servicios de Operación*.

- Distribuidora Puelche S.A. (2026b). *Bases Técnicas Transversales de Licitación N° TFEP-01/2026*.

- Distribuidora Puelche S.A. (2026c). *Caso: Logística – Especificaciones del Problema y Operación de Distribuidora Puelche S.A.*

- Distribuidora Puelche S.A. (2026d). *Aclaraciones de la Licitación N° TFEP-01/2026*.

- LafroX. (2026a). *Subdocumento 4: Arquitectura de la solución*.

- LafroX. (2026b). *Subdocumento 6: Metodologías*.

- LafroX. (2026c). *Subdocumento 7: Plan de trabajo, EDT, cronograma e implantación. Formulario T-15: Nivelación de recursos*.

- SGS. (2024). *Certificado de Sistema de Gestión de Servicios de TI ISO/IEC 20000-1:2018 N° CL21/8190*. SGS United Kingdom Ltd.

## Declaración de uso de IA

La Tabla [1.7](LAFROX-Subdocumento1.md#tab:declaracion_ia) identifica las herramientas y el alcance de la asistencia utilizada, conforme a la sección 7.2 de las Aclaraciones (Distribuidora Puelche S.A., 2026d). La declaración se consolida en el Formulario A-6.

<a id="tab:declaracion_ia"></a>

**Tabla 1.7 — Uso de IA por sección y formulario. Fuente: registro del equipo.**

| **Sección** | **Herramienta** | **Finalidad del uso** | **Nivel en texto** | **Nivel en diagramas** | **Revisión humana (quién y qué verificó)** |
| --- | --- | --- | --- | --- | --- |
| 1.1 | Claude / Gemini; OpenAI Codex | Trayectoria, inventario y puestos corporativos de atención | Alto | No aplica | Alex Aravena: Se verificó el planteamiento y la visión de la empresa, junto con los productos y servicios ofrecidos. |
| 1.2 | Claude / Gemini; OpenAI Codex | Organigrama, antigüedad, turnos y respaldos del NOC | Alto | Alto | Alex Aravena: Se verificó el organigrama y sus áreas, además del equipo y la antigüedad. |
| 1.3 | Claude / Gemini; OpenAI Codex | Redacción de gobierno y responsabilidades | Alto | No aplica | Alex Aravena: Se validaron los modelos de gobierno planteados. |
| 1.4 | Claude / Gemini; OpenAI Codex | Comparación de experiencia y SLA | Alto | No aplica | Alex Aravena: Se validaron la experiencia y los proyectos realizados. |
| 1.5 | Claude / Gemini; Claude Code; OpenAI Codex | Síntesis de roles y dedicaciones | Alto | No aplica | Alex Aravena: Se validaron la estructura del proyecto y su jerarquía. |
| 1.6 | Claude / Gemini; OpenAI Codex | Redacción de alcance de alianzas | Alto | No aplica | Alex Aravena: Se validaron las alianzas establecidas. |
| T-6 | Claude / Gemini; OpenAI Codex | Formato, introducción y referencias | Alto | No aplica | Alex Aravena: Se verificaron los once campos de los tres proyectos y su coherencia con la sección 1.4. |
