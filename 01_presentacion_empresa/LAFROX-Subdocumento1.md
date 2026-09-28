# Presentación de la empresa

El presente subdocumento expone las credenciales corporativas, organizacionales y técnicas de LafroX como proponente para la licitación del Caso 02 de Distribuidora Puelche S.A. Presenta la trayectoria, capacidad instalada y líneas de negocio de la empresa; después desarrolla su estructura organizacional, su gobierno interno y su experiencia verificable en el Formulario T-6. La organización del equipo específico se complementa en el Capítulo 12 y las alianzas del proyecto se desarrollan en la sección 12.3.

## Presentación de la empresa

Fundada en 2012 en Santiago de Chile, LafroX es una empresa de ingeniería de software e integración de sistemas dedicada a diseñar, implantar y operar soluciones tecnológicas de misión crítica en sectores logísticos, distribución comercial de consumo masivo y transporte de carga. Durante catorce años de actividad ininterrumpida, la compañía ha desarrollado proyectos en entornos operacionales complejos caracterizados por alta dispersión geográfica, baja conectividad y con una estricta regulación técnica detrás.

Entre los principales hitos de su trayectoria destacan la puesta en marcha de su primera plataforma de ruteo y telemetría en 2015, la acreditación como integrador certificado de hardware industrial para cadenas de frío en 2018, la certificación corporativa en normas de calidad y seguridad en 2021, y la consolidación de su arquitectura modular híbrida en 2024, sosteniendo a la fecha operaciones que superan las 50.000 transacciones diarias en terreno.

La oferta de LafroX cuenta con tres líneas de negocio especializadas:

1. **Ingeniería de software en el borde (Edge Computing):** Desarrollo de aplicaciones móviles y sistemas locales con arquitectura *offline-first*. Implementan almacenamiento local cifrado mediante bases de datos SQLite en terminales móviles, sincronización asíncrona bidireccional y resolución determinista de conflictos al restablecer el enlace de comunicaciones, eliminando el riesgo de pérdida transaccional en zonas rurales o almacenes sin cobertura de red.
2. **Trazabilidad y telemetría de frío industrial:** Integración de hardware especializado de terreno, tales como termógrafos vehiculares, sensores inalámbricos y capturadores robustos aptos para operar bajo frío extremo. Esta línea asegura el monitoreo térmico continuo y la captura de eventos de custodia y transporte, en cumplimiento con el Reglamento Sanitario de los Alimentos (RSA) y normativas de retiro de producto.
3. **Arquitecturas modulares híbridas de misión crítica:** Diseño, despliegue y soporte continuo de plataformas que combinan un núcleo transaccional en nube pública (monolito modular implementado en Python y Django sobre bases de datos relacionales PostgreSQL) con componentes de borde desplegados en centros de distribución físicos (*on-premise*), asegurando alta resiliencia y autonomía operativa ante cortes de conectividad externa.

Para soportar estas líneas, LafroX dispone de capacidad instalada distribuida y de un catálogo de productos y servicios que se describe a continuación.

- **Infraestructura y ambientes:** Plataforma de cómputo en nube pública y dos centros de datos (primario y secundario en configuración activo-pasivo) que soportan cinco ambientes segregados: Desarrollo (DEV), Aseguramiento de Calidad (QA), Preproducción (PREPROD), Producción (PROD) y Recuperación ante Desastres (DR). La capacitación utiliza datos ficticios en un espacio aislado del ambiente que corresponda; no constituye un sexto ambiente. El entorno DR es sometido a auditorías y simulacros semestrales, con objetivos de RTO ≤ 4 horas y RPO ≤ 15 minutos.
- **Centro de Operaciones y Mesa de Servicios:** Centro de Operaciones de Red (NOC) y Mesa de Servicios con niveles de escalamiento L1, L2 y L3. La capacidad de atención y el horario comprometido para Puelche se dimensionarán en el Capítulo 10 a partir de la demanda de la marcha blanca; esta capacidad corporativa no constituye un compromiso de volumen para el CLIENTE.

El catálogo de la empresa se organiza en productos de software, servicios profesionales y servicios de infraestructura y conectividad.

### Productos de Software

- **Aplicaciones móviles de terreno:** Soluciones *offline-first* para fuerzas de venta, reparto y captura de información en campo, con sincronización asíncrona y resolución determinista de conflictos ante intermitencia de red.
- **Plataformas de monitoreo y telemetría:** Sistemas de seguimiento para flotas de transporte y cadena de frío, con generación de alertas ante desviaciones operacionales o térmicas.
- **Núcleos transaccionales y de gestión:** Sistemas para administración de inventarios, facturación y planificación logística, desplegados en arquitecturas híbridas.

### Servicios Profesionales

- **Implementación e integración de sistemas:** Diseño, despliegue y puesta en marcha de soluciones integradas con sistemas existentes del cliente.
- **Operación y soporte continuo:** Monitoreo, atención de incidentes y mesa de ayuda bajo acuerdos de nivel de servicio.
- **Consultoría técnica y regulatoria:** Asesoría en procesos operacionales y cumplimiento normativo aplicable a los sectores atendidos.
- **Gestión del cambio y capacitación:** Acompañamiento en la adopción de nuevas tecnologías y formación de usuarios finales.

### Servicios de Infraestructura y Conectividad

- **Suministro de hardware especializado:** Provisión y soporte de equipamiento tecnológico para operaciones de terreno, mediante alianzas con proveedores certificados.
- **Conectividad y redundancia:** Soluciones de comunicación para asegurar continuidad operacional en ubicaciones remotas o con conectividad limitada.
- **Continuidad y recuperación ante desastres:** Servicios para sostener la disponibilidad de sistemas críticos ante contingencias.

## Estructura Organizacional

LafroX posee una estructura organizacional funcional y matricial diseñada para garantizar tanto la excelencia en la ejecución técnica de los proyectos como la continuidad operacional ininterrumpida de los servicios en producción. La dotación profesional de planta está compuesta por 124 especialistas contratados por la empresa.

La Figura 1.1 ilustra el organigrama corporativo de la compañía, donde se identifican las líneas jerárquicas y funcionales de reporte.

**Figura 1.1 — Estructura organizacional corporativa de LafroX**

- **Propósito:** representar las líneas jerárquicas y funcionales de la empresa.
- **Nivel superior:** Gerencia General, responsable de la dirección estratégica.
- **Control independiente:** el Oficial de Seguridad de la Información (CISO) reporta directamente a la Gerencia General mediante una relación funcional independiente.
- **Nivel de coordinación:** la Dirección de Operaciones gestiona la entrega y los servicios y depende de la Gerencia General.
- **Áreas dependientes de Operaciones:** División de Ingeniería (desarrollo, datos y arquitectura), División de Infraestructura (NOC 24×7, SRE y redes) y División de Calidad (QA, pruebas y procesos CMMI).
- **Relaciones:** la línea entre CISO y Gerencia General es funcional; las líneas hacia Operaciones y sus tres divisiones son jerárquicas.

*Fuente: elaboración propia. Transcripción textual de la figura original.*

Del análisis de la Figura 1.1 se desprenden dos decisiones fundamentales de gobierno corporativo:

1. **Independencia del control de seguridad y calidad:** El Oficial de Seguridad de la Información (CISO) mantiene una línea de dependencia funcional y reporte directo a la Gerencia General, garantizando que las decisiones de seguridad no se subordinen a los plazos operacionales de los proyectos. De igual forma, la División de Aseguramiento de Calidad (QA) actúa con potestad de veto sobre los pasos a producción.
2. **Especialización operativa y de ingeniería:** La Dirección de Operaciones coordina horizontalmente los recursos para asegurar que la ingeniería de desarrollo mantenga foco en la construcción de software, mientras que la infraestructura y el NOC garantizan de forma ininterrumpida los acuerdos de nivel de servicio (SLA).

Para sostener estos procesos, la dotación profesional de 124 ingenieros y especialistas se distribuye formalmente como se expone en la Tabla 1.1.

**Distribución de la dotación profesional de planta de LafroX. Fuente: Elaboración propia.**

| **División Organizacional** | **Área / Rol Principal** | **Ubicación de Trabajo** | **Cantidad** |
| --- | --- | --- | --- |
| División de Ingeniería | Desarrollo Software (Python, Django, Móvil) | Sede Central (Santiago) | 48 |
| División de Ingeniería | Arquitectura de Solución e Integración | Sede Central (Santiago) | 15 |
| División de Infraestructura | Centro de Operaciones de Red (NOC 24×7) | Centro de Operaciones | 32 |
| División de Infraestructura | Ingeniería de Confiabilidad (SRE) y Cloud | Centro de Operaciones | 12 |
| División de Calidad (QA) | Aseguramiento y Automatización de Pruebas | Sede Central (Santiago) | 10 |
| Oficialía de Seguridad | CISO y Especialistas en Ciberseguridad | Sede Central (Santiago) | 7 |
| **Total Dotación** |  |  | **124** |

A partir de los datos presentados en la Tabla 1.1, el Centro de Operaciones de Red concentra 32 profesionales para monitoreo y resolución de incidentes. Su programación de turnos y respaldos se ajusta en cada contrato de operación; para Puelche, la dotación y el horario comprometido se fundamentarán en el Capítulo 10.

## Gobierno interno Calidad, Seguridad y Conocimiento

El modelo de gobierno interno de LafroX se fundamenta en políticas explícitas, comités de gestión colegiados y procesos auditables y medibles mediante indicadores cuantitativos.

### Modelo de Gobierno de Calidad
La calidad de los procesos de LafroX se rige por un Sistema de Gestión de Calidad certificado conforme a ISO 9001:2015 y por prácticas evaluadas bajo CMMI-DEV Nivel 3.

- **Instancia colegiada:** El Comité de Calidad y Procesos, presidido mensualmente por el Jefe de QA y con participación de los líderes de proyecto, analiza la adherencia metodológica y métricas de defecto.
- **Políticas y controles de ingeniería:** Se implementan compuertas de calidad automáticas (*quality gates*) en los canales de integración continua (CI/CD). Es política corporativa estricta rechazar cualquier compilación con cobertura de pruebas unitarias inferior al 80% o con deuda técnica detectada por SonarQube categorizada como bloqueante.
- **Auditorías internas:** Se ejecutan auditorías internas trimestrales a cargo de auditores líderes certificados, orientadas a evaluar la trazabilidad entre requerimientos, código y matrices de prueba.

### Modelo de Gobierno de Seguridad de la Información
El marco de seguridad corporativo está alineado y certificado bajo la norma ISO/IEC 27001:2022, implementando un enfoque de confianza cero (*Zero Trust*) y gestión continua del riesgo.

- **Responsable e instancias:** El Oficial de Seguridad de la Información (CISO) lidera el Comité de Seguridad y Privacidad, sesionando con periodicidad mensual para revisar incidentes, vectores de ataque y evaluar la gestión de vulnerabilidades.
- **Procesos DevSecOps:** Se integran análisis estáticos de seguridad de código (SAST) y análisis de composición de software (SCA) en cada confirmación de código. Se realizan pruebas de penetración (*ethical hacking*) externas de forma semestral.
- **Continuidad operacional:** Se gestionan planes de continuidad de negocio (BCP) y de recuperación ante desastres (DRP), sometidos a simulacros semestrales con corte controlado para verificar los umbrales de RTO ≤ 4 horas y RPO ≤ 15 minutos.

### Modelo de Gobierno de Gestión del Conocimiento
Para mitigar el riesgo de dependencia del conocimiento tácito individual de ingenieros sénior y especialistas operacionales, LafroX cuenta con un proceso formal de Transferencia y Preservación del Conocimiento:

- **Repositorio corporativo institucional:** El Líder de Calidad administra una base centralizada de arquitectura, estándares de codificación, guías de despliegue y recuperación. Todo cierre de incidente crítico (P1 o P2) exige un informe post-mortem aprobado por el responsable técnico y publicado en la base.
- **Talleres de elicitación y traspaso:** Los líderes de dominio realizan sesiones trimestrales para transformar conocimiento no estructurado en manuales reproducibles. El Comité de Calidad revisa semestralmente su vigencia y asigna responsables de actualización.

## Experiencia y Certificaciones

La idoneidad técnica y metodológica de LafroX está validada por certificaciones institucionales vigentes otorgadas por casas certificadoras reconocidas internacionalmente:

- **ISO 9001:2015 (Sistema de Gestión de la Calidad):** Certificado N° BV-CH-94821 emitido por Bureau Veritas. Alcance: ``Diseño, desarrollo, implementación, integración y soporte de sistemas de software logístico y transaccional''. Vigente hasta noviembre de 2028.
- **ISO/IEC 27001:2022 (Sistema de Gestión de Seguridad de la Información):** Certificado N° SI-0312/2023 emitido por AENOR. Alcance: ``Operación de servicios cloud, centros de datos on-premise y procesos de ingeniería de software de misión crítica''. Vigente hasta enero de 2027.
- **CMMI-DEV Nivel 3 (Modelo de Madurez de Capacidades para Desarrollo):** Evaluación SCAMPI A N° 58190, emitida en 2022 por un evaluador acreditado ante el CMMI Institute. Valida la estandarización y madurez de los procesos organizacionales de ciclo de vida del software.
- **ISO/IEC 20000-1:2018 (Sistema de Gestión de Servicios de TI):** Certificado N° CL21/8190 emitido por SGS. Alcance: ``Provisión de servicios de TI, gestión de incidentes y mesa de ayuda 24×7 para infraestructuras logísticas críticas''. Vigente hasta mayo de 2027.

En concordancia con el Artículo 34° de las Bases Administrativas y la aclaración oficial de la licitación, LafroX presenta en el archivo independiente **[LAFROX-Formulario-T-6.md](LAFROX-Formulario-T-6.md)** el detalle de tres proyectos finalizados en los últimos cinco años y en operación continua, los cuales demuestran experiencia en complejidad técnica y volumétrica equivalente a la del Caso 02:

1. **Sistema Híbrido de Reparto y Gestión Logística (LogiNacional S.A.):** Ejecutado entre 2021 y 2022, integró un núcleo logístico modular, ERP y facturación electrónica sobre nube pública y servidores de borde en 14 centros de distribución. Soporta 420 camiones y 22.000 entregas diarias bajo SLA contractual de 99,5%.
2. **Plataforma de Telemetría y Cadena de Frío IoT (FarmaRed S.A.):** Ejecutada entre 2022 y 2023, monitorea cámaras a -22 °C y una flota refrigerada; procesa más de 12 millones de mediciones mensuales bajo SLA de 99,9%.
3. **Sistema Móvil de Preventa y Ruteo Desconectado (Comercializadora Lácteos del Sur S.A.):** Ejecutado entre 2023 y 2024, habilita a 280 preventistas y procesa 18.000 transacciones comerciales diarias mediante sincronización determinista en diferido y políticas de crédito locales.

### Cartera de Clientes

A lo largo de sus catorce años de operación ininterrumpida, LafroX ha consolidado una cartera de clientes concentrada en los sectores logístico, de distribución comercial de consumo masivo y de transporte de carga, ámbitos que constituyen el foco estratégico declarado de la compañía.

Entre los clientes activos y relaciones comerciales vigentes de LafroX, destacan:

- **LogiNacional S.A.** – Operador logístico y de distribución de carga terrestre, con cobertura nacional.
- **FarmaRed S.A.** – Cadena de distribución farmacéutica con exigencias de trazabilidad y cadena de frío.
- **Comercializadora Lácteos del Sur S.A.** – Empresa de consumo masivo con fuerza de preventa en terreno.
- **TransAndina Cargo S.A.** – Empresa de transporte de carga pesada interregional, con flota propia de más de 300 camiones.
- **Supermercados del Maipo S.A.** – Cadena de retail de consumo masivo con centros de distribución regionales.
- **NutriChile Alimentos S.A.** – Empresa de manufactura y distribución de alimentos refrigerados y congelados.
- **Congelados del Pacífico S.A.** – Empresa exportadora de productos del mar con cadena de frío en puertos y centros de acopio.
- **Distribuidora Andes Retail S.A.** – Distribuidora mayorista de productos de consumo masivo con operación multirregional y bodegas de tránsito.

Esta base de clientes evidencia la capacidad de LafroX para operar de manera simultánea en múltiples industrias con requerimientos técnicos, regulatorios y logísticos diferenciados, sosteniendo relaciones comerciales de largo plazo por sobre contratos puntuales de corta duración.

## Estructura para Proyecto

Para garantizar el cumplimiento de los 56 meses de contrato estipulados en el Artículo 17° de las Bases Administrativas, LafroX establece una estructura de gobernanza de proyecto dedicada, centralizada y con líneas de autoridad unívocas.

El proyecto será liderado de forma exclusiva y continua por el Jefe de Proyecto nominado, **Alex Aravena**, quien actuará como interlocutor único frente a la contraparte técnica y directiva del cliente. Reportando directamente al Jefe de Proyecto, se constituye un comité técnico compuesto por siete líderes de dominio especializados:

- **Arquitecto de Solución (Bastián Trejo):** Responsable del diseño técnico global, la consistencia entre capas lógicas y la articulación del modelo híbrido nube/on-premise.
- **Encargado de Seguridad de la Información (Álvaro Catalán):** Responsable del cumplimiento de la norma ISO/IEC 27001, la arquitectura Zero Trust y los controles de acceso.
- **Líder de Datos (Leandro Chamorro):** Responsable de la modelación relacional, la estrategia de migración y la reconciliación determinista de inventarios.
- **Líder de Desarrollo (Tomás Pérez):** Responsable del desarrollo del monolito modular en Python/Django, componentes móviles y canal de entrega continua.
- **Líder de Calidad (Maximiliano Miño):** Responsable del plan de pruebas, automatización y cumplimiento de los umbrales de aseguramiento de calidad ISO/IEC 25010.
- **Líder de Operación / SRE (Guillermo Castillo):** Responsable de la disponibilidad continua 24×7, observabilidad de infraestructura y gestión de niveles de servicio.
- **Líder de Implantación y Gestión del Cambio (Patricio Henríquez):** Responsable de la adopción en terreno, capacitación de preventistas y conductores, y marchas blancas.

El detalle curricular, la matriz de dedicación porcentual por mes de contrato y las cartas formales de compromiso del equipo nominado se presentan en el Capítulo 12 y en el Formulario T-8.

## Alianzas

Para viabilizar el despliegue del modelo híbrido obligatorio (Artículo 16° de las Bases Administrativas) y asegurar soporte de clase empresarial en los componentes físicos de terreno, LafroX mantiene alianzas tecnológicas estratégicas y vigentes:

- **Amazon Web Services (AWS Partner Network – Advanced Tier Services):** LafroX es socio tecnológico nivel Advanced, con competencias certificadas en DevOps y Migración. Esta alianza garantiza acceso a soporte empresarial de nivel 3 directo con ingenieros de la nube, créditos de prueba de conceptos y revisiones arquitectónicas formales bajo el marco Well-Architected. Vigente hasta marzo de 2027.
- **Zebra Technologies (Premier Solution Partner):** Alianza formal para el suministro, soporte de fábrica y mantenimiento de terminales móviles industriales, lectores de códigos de barra e impresoras térmicas portátiles con certificación de operación en ambientes hostiles y cámaras de congelación a -25 °C. Vigente hasta junio de 2027.
- **Fortinet / Cisco (Select Partner):** Alianza para el aprovisionamiento de equipamiento de conectividad de borde, switches industriales y firewalls de red SD-WAN requeridos para enlazar de manera segura los centros de distribución y salas técnicas on-premise. Vigente hasta septiembre de 2027.
- **Starlink Business (Authorized Enterprise Reseller):** Convenio para la provisión e integración de terminales satelitales de baja órbita con prioridad de tráfico corporativo, garantizando redundancia de comunicaciones ante caídas de enlace en cross-dockings y almacenes remotos. Vigente hasta diciembre de 2027.

Las especificaciones particulares de hardware e implementos que estas alianzas suministran al proyecto se detallan en el Formulario T-11 y en la sección 12.3.

## Referencias

- AENOR. (2023). *Certificado de Sistema de Gestión de Seguridad de la Información ISO/IEC 27001:2022 N° SI-0312/2023*. AENOR Internacional.
- Bureau Veritas. (2023). *Certificado de Sistema de Gestión de la Calidad ISO 9001:2015 N° BV-CH-94821*. Bureau Veritas Certification.
- CMMI Institute. (2022). *CMMI for Development, Version 2.0: Maturity Level 3 SCAMPI A Appraisal Report N° 58190*. CMMI Institute.
- Distribuidora Puelche S.A. (2026a). *Bases Administrativas de Licitación N° TFEP-01/2026: Contratación de Solución Integral de Software y Servicios de Operación*.
- Distribuidora Puelche S.A. (2026b). *Bases Técnicas Transversales de Licitación N° TFEP-01/2026*.
- Distribuidora Puelche S.A. (2026c). *Caso 02: Logística – Especificaciones del Problema y Operación de Distribuidora Puelche S.A.*
- Distribuidora Puelche S.A. (2026d). *Aclaraciones de la Licitación N° TFEP-01/2026*.
- SGS. (2024). *Certificado de Sistema de Gestión de Servicios de TI ISO/IEC 20000-1:2018 N° CL21/8190*. SGS United Kingdom Ltd.

## Declaración de uso de IA

En cumplimiento de la Sección 7.2 de las Aclaraciones de la Licitación, se declara el uso asistido de herramientas de inteligencia artificial en la elaboración del presente subdocumento.

**Declaración de uso de Inteligencia Artificial por sección del Subdocumento 1.**

| **Sección** | **Herramienta** | **Finalidad del uso** | **Texto** | **Diagrama** | **Revisión humana** |
| --- | --- | --- | --- | --- | --- |
| 1.1 Presentación | Claude / Gemini | Formato y redacción de capacidades | Bajo | Ninguno | Alex Aravena (JP): Coherencia con líneas de negocio |
| 1.2 Estructura Org. | Claude / Gemini | Síntesis de turnos NOC y TikZ | Bajo | Medio | Bastián Trejo (Arq): Validación de organigrama y turnos |
| 1.3 Gobierno interno | Claude / Gemini | Estructuración de políticas y comités | Bajo | Ninguno | Álvaro Catalán (Seg): Verificación normas 27001/CMMI |
| 1.4 Experiencia | Claude / Gemini | Redacción de proyectos equivalentes | Bajo | Ninguno | Alex Aravena (JP): Verificación de volumetrías |
| 1.5 Estructura Proy. | Claude / Gemini | Alineación de roles institucionales | Bajo | Ninguno | Patricio Henríquez (Gest): Trazabilidad con Cap. 12 |
| 1.6 Alianzas | Claude / Gemini | Redacción de convenios de hardware | Bajo | Ninguno | Bastián Trejo (Arq): Coherencia con diseño híbrido |
| Formulario T-6 | Claude / Gemini | Disposición tabular en LaTeX | Bajo | Ninguno | Alex Aravena (JP): Validación de los 11 campos exigidos y coherencia con la sección 1.4 |
