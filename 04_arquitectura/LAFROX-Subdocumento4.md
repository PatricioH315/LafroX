# LafroX — Subdocumento 4

[Cuerpo](LAFROX-Subdocumento4.md) · [Anexos](LAFROX-Subdocumento4-Anexos.md) · [T-11](LAFROX-Formulario-T-11.md)

## Índice

- [4 Introducción a la Arquitectura lógica y física de la solución](#4-introducción-a-la-arquitectura-lógica-y-física-de-la-solución)
- [4.1 Arquitectura lógica](#41-arquitectura-lógica)
- [4.1.1 Especificaciones Tecnologías de Software a utilizar](#411-especificaciones-tecnologías-de-software-a-utilizar)
- [4.1.2 Principios de integración](#412-principios-de-integración)
- [4.1.3 Capas de la arquitectura](#413-capas-de-la-arquitectura)
- [4.1.3.1 Capa de presentación (Capa 1)](#4131-capa-de-presentación-capa-1)
- [4.1.3.2 Capa de borde y exposición (Capa 2)](#4132-capa-de-borde-y-exposición-capa-2)
- [4.1.3.3 Capa de puerta de enlace de servicios (Capa 3)](#4133-capa-de-puerta-de-enlace-de-servicios-capa-3)
- [4.1.3.4 Capa de lógica de negocio (Capa 4)](#4134-capa-de-lógica-de-negocio-capa-4)
- [4.1.3.5 Capa de integración y eventos (Capa 5)](#4135-capa-de-integración-y-eventos-capa-5)
- [4.1.3.6 Capa de acceso a datos (Capa 6)](#4136-capa-de-acceso-a-datos-capa-6)
- [4.1.3.7 Capa de seguridad transversal (Capa 7)](#4137-capa-de-seguridad-transversal-capa-7)
- [4.1.3.8 Capa de observabilidad transversal (Capa 8)](#4138-capa-de-observabilidad-transversal-capa-8)
- [4.1.4 Módulos funcionales y límites de contexto](#414-módulos-funcionales-y-límites-de-contexto)
- [4.1.4.1 Mapa de límites de contexto](#4141-mapa-de-límites-de-contexto)
- [4.1.4.2 Módulo de calidad y trazabilidad (M9)](#4142-módulo-de-calidad-y-trazabilidad-m9)
- [4.1.4.3 Módulo de inventario (M2)](#4143-módulo-de-inventario-m2)
- [4.1.4.4 Módulo de preventa móvil (M3)](#4144-módulo-de-preventa-móvil-m3)
- [4.1.4.5 Módulo de planificación de rutas (M4)](#4145-módulo-de-planificación-de-rutas-m4)
- [4.1.4.6 Módulo de rendición y cobro (M7)](#4146-módulo-de-rendición-y-cobro-m7)
- [4.1.4.7 Módulo de analítica y costo de servir (M10)](#4147-módulo-de-analítica-y-costo-de-servir-m10)
- [4.1.4.8 Recepción, preparación, reparto y servicios asociados](#4148-recepción-preparación-reparto-y-servicios-asociados)
- [4.1.5 Modelo de datos conceptual](#415-modelo-de-datos-conceptual)
- [4.1.6 Catálogo de interfaces](#416-catálogo-de-interfaces)
- [4.1.6.1 Integraciones internas](#4161-integraciones-internas)
- [4.1.6.2 Integraciones externas](#4162-integraciones-externas)
- [4.1.7 Detalle de tecnologías seleccionadas](#417-detalle-de-tecnologías-seleccionadas)
- [4.1.8 Implantación progresiva del backend Laravel](#418-implantación-progresiva-del-backend-laravel)
- [4.1.9 Ambientes del ciclo de vida y promoción de componentes](#419-ambientes-del-ciclo-de-vida-y-promoción-de-componentes)
- [4.1.10 Patrones de diseño y continuidad](#4110-patrones-de-diseño-y-continuidad)
- [4.1.10.1 SOLID aplicado a los contratos de negocio](#41101-solid-aplicado-a-los-contratos-de-negocio)
- [4.1.11 Registro de decisiones de arquitectura](#4111-registro-de-decisiones-de-arquitectura)
- [4.1.12 Puntos únicos de falla y riesgos residuales](#4112-puntos-únicos-de-falla-y-riesgos-residuales)
- [4.1.13 Comparación de alternativas arquitectónicas](#4113-comparación-de-alternativas-arquitectónicas)
- [4.1.14 Relación entre las vistas de arquitectura](#4114-relación-entre-las-vistas-de-arquitectura)
- [4.1.15 Funciones disponibles y no disponibles sin conexión](#4115-funciones-disponibles-y-no-disponibles-sin-conexión)
- [4.1.16 Reglas de reconciliación](#4116-reglas-de-reconciliación)
- [4.1.17 Articulación entre prueba de entrega, DTE y acuse](#4117-articulación-entre-prueba-de-entrega-dte-y-acuse)
- [4.1.17.1 Secuencia y excepciones](#41171-secuencia-y-excepciones)
- [4.1.17.2 Control de liberación en la ventana crítica](#41172-control-de-liberación-en-la-ventana-crítica)
- [4.1.18 Identidad y ciclo de vida de conductores externos](#4118-identidad-y-ciclo-de-vida-de-conductores-externos)
- [4.1.19 Primer cuello de botella bajo la carga de septiembre](#4119-primer-cuello-de-botella-bajo-la-carga-de-septiembre)
- [4.1.20 Decisiones del numeral 16.1 del caso](#4120-decisiones-del-numeral-161-del-caso)
- [4.1.21 Condiciones y supuestos de diseño](#4121-condiciones-y-supuestos-de-diseño)
- [4.2 Arquitectura física](#42-arquitectura-física)
- [4.2.1 Especificaciones Implementos a proveer (Hardware y Software)](#421-especificaciones-implementos-a-proveer-hardware-y-software)
- [4.2.1.1 Síntesis del equipamiento por familia](#4211-síntesis-del-equipamiento-por-familia)
- [4.2.1.2 Criterios de selección](#4212-criterios-de-selección)
- [4.2.1.3 Software y licenciamiento](#4213-software-y-licenciamiento)
- [4.2.2 Emplazamiento de cada componente](#422-emplazamiento-de-cada-componente)
- [4.2.2.1 Instalaciones y dominios](#4221-instalaciones-y-dominios)
- [4.2.2.2 Correspondencia con la arquitectura lógica](#4222-correspondencia-con-la-arquitectura-lógica)
- [4.2.2.3 Síntesis del emplazamiento por dominio y criterio](#4223-síntesis-del-emplazamiento-por-dominio-y-criterio)
- [4.2.2.4 Componentes de nube pura](#4224-componentes-de-nube-pura)
- [4.2.2.5 Componentes on-premise](#4225-componentes-on-premise)
- [4.2.2.6 Componentes híbridos](#4226-componentes-híbridos)
- [4.2.2.7 Autonomía de cada ámbito sin enlace](#4227-autonomía-de-cada-ámbito-sin-enlace)
- [4.2.3 Servicios contratados en la plataforma de nube](#423-servicios-contratados-en-la-plataforma-de-nube)
- [4.2.3.1 Servicios por función](#4231-servicios-por-función)
- [4.2.3.2 Región secundaria y residencia de los datos](#4232-región-secundaria-y-residencia-de-los-datos)
- [4.2.3.3 Servicios que no se contratan](#4233-servicios-que-no-se-contratan)
- [4.2.3.4 Modelo de contratación](#4234-modelo-de-contratación)
- [4.2.3.5 Topología de los servicios](#4235-topología-de-los-servicios)
- [4.2.4 Arquitectura de despliegue](#424-arquitectura-de-despliegue)
- [4.2.4.1 Ambientes y ciclo de entrega](#4241-ambientes-y-ciclo-de-entrega)
- [4.2.4.1.1 Artefacto y perfiles de ejecución](#42411-artefacto-y-perfiles-de-ejecución)
- [4.2.4.1.2 Liberación y reversión](#42412-liberación-y-reversión)
- [4.2.4.1.3 Transición al backend Laravel](#42413-transición-al-backend-laravel)
- [4.2.4.1.4 Calendario y cadencia](#42414-calendario-y-cadencia)
- [4.2.4.2 Red de despliegue](#4242-red-de-despliegue)
- [4.2.4.3 Alta disponibilidad](#4243-alta-disponibilidad)
- [4.2.4.4 Recuperación ante desastres](#4244-recuperación-ante-desastres)
- [4.2.4.4.1 Conmutación y retorno](#42441-conmutación-y-retorno)
- [4.2.4.4.2 Operación durante una contingencia regional](#42442-operación-durante-una-contingencia-regional)
- [4.2.4.5 Respaldos](#4245-respaldos)
- [4.2.4.6 Verificación de la continuidad](#4246-verificación-de-la-continuidad)
- [4.2.5 Conexiones, puntos de falla y contingencia](#425-conexiones-puntos-de-falla-y-contingencia)
- [4.2.5.1 Conexiones entre sitios, terreno y nube](#4251-conexiones-entre-sitios-terreno-y-nube)
- [4.2.5.2 Superficie de exposición](#4252-superficie-de-exposición)
- [4.2.5.3 Puntos de falla en los sitios y en los enlaces](#4253-puntos-de-falla-en-los-sitios-y-en-los-enlaces)
- [4.2.5.4 Puntos de falla en la nube, el terreno y las integraciones](#4254-puntos-de-falla-en-la-nube-el-terreno-y-las-integraciones)
- [4.2.6 Dimensionamiento y plan de capacidad](#426-dimensionamiento-y-plan-de-capacidad)
- [4.2.6.1 Método, fuentes y supuestos](#4261-método-fuentes-y-supuestos)
- [4.2.6.2 Perfil de carga y regímenes de diseño](#4262-perfil-de-carga-y-regímenes-de-diseño)
- [4.2.6.3 Transacciones por segundo: dimensiones 1–3](#4263-transacciones-por-segundo-dimensiones-13)
- [4.2.6.4 Personas usuarias, concurrencia y dispositivos: dimensiones 4–6](#4264-personas-usuarias-concurrencia-y-dispositivos-dimensiones-46)
- [4.2.6.5 Almacenamiento, retención y migración: dimensiones 7–10](#4265-almacenamiento-retención-y-migración-dimensiones-710)
- [4.2.6.6 Integraciones y ancho de banda por sitio: dimensiones 11–12](#4266-integraciones-y-ancho-de-banda-por-sitio-dimensiones-1112)
- [4.2.6.7 Terreno: turno sin señal y sincronización de la flota: dimensiones 13–14](#4267-terreno-turno-sin-señal-y-sincronización-de-la-flota-dimensiones-1314)
- [4.2.6.8 Capacidad on-premise](#4268-capacidad-on-premise)
- [4.2.6.9 Capacidad en nube](#4269-capacidad-en-nube)
- [4.2.6.10 Plan de capacidad](#42610-plan-de-capacidad)
- [4.2.6.11 Cuello de botella, umbrales y degradación controlada](#42611-cuello-de-botella-umbrales-y-degradación-controlada)
- [4.2.6.12 Validación mediante pruebas de carga y estrés](#42612-validación-mediante-pruebas-de-carga-y-estrés)
- [4.2.6.13 Síntesis de las dieciséis dimensiones del numeral 14.2](#42613-síntesis-de-las-dieciséis-dimensiones-del-numeral-142)
- [4.3 Data center](#43-data-center)
- [4.3.1 Especificaciones Data Center Primaria](#431-especificaciones-data-center-primaria)
- [4.3.1.1 Proveedor](#4311-proveedor)
- [4.3.1.2 Región y zonas de disponibilidad](#4312-región-y-zonas-de-disponibilidad)
- [4.3.1.3 Servicios contratados en la región primaria](#4313-servicios-contratados-en-la-región-primaria)
- [4.3.1.4 Sitio on-premise: CD Talca (sala técnica secundaria)](#4314-sitio-on-premise-cd-talca-sala-técnica-secundaria)
- [4.3.2 Especificaciones Data Center Secundario](#432-especificaciones-data-center-secundario)
- [4.3.2.1 Modalidad del sitio secundario](#4321-modalidad-del-sitio-secundario)
- [4.3.2.2 Región o sitio de recuperación](#4322-región-o-sitio-de-recuperación)
- [4.3.2.3 Replicación](#4323-replicación)
- [4.3.2.4 RPO y RTO](#4324-rpo-y-rto)
- [4.3.2.5 Procedimiento de conmutación](#4325-procedimiento-de-conmutación)
- [4.3.2.6 Procedimiento de retorno](#4326-procedimiento-de-retorno)
- [4.3.2.7 Pruebas del plan de recuperación y respaldos](#4327-pruebas-del-plan-de-recuperación-y-respaldos)
- [Referencias](#referencias)
- [Declaración de uso de IA](#declaración-de-uso-de-ia)

# 4 Introducción a la Arquitectura lógica y física de la solución

<a id="cap:arquitectura-logica"></a>

El capítulo 4 explica cómo la solución sostiene la operación distribuida de Puelche. La arquitectura lógica define las responsabilidades, los datos y los contratos que permiten ejecutar las capacidades del capítulo 3; la arquitectura física acredita su emplazamiento y continuidad, y la estrategia de centros de datos completa su recuperación. Los catálogos, el registro de decisiones de arquitectura (Anexo 4-O) y la memoria de cálculo del dimensionamiento (Anexo 4-W) se entregan en el archivo LAFROX-Subdocumento4-Anexos, y el detalle del equipamiento, en el Formulario T-11, entregado como archivo propio.

## 4.1 Arquitectura lógica

<a id="sec:arquitectura-logica"></a>

Los anexos 4-A a 4-N detallan eventos, módulos, interfaces, reglas y correspondencias. El Anexo 4-O reúne el registro único ADR-01 a ADR-22; el 4-P presenta las tecnologías y su actualización; los 4-Q y 4-R, amenazas y controles; el 4-S, los puntos de vista y sus reglas de correspondencia; el 4-T, el desempeño; el 4-U, la evidencia documental; y el 4-V, los protocolos de aceptación. Los anexos comienzan con un catálogo navegable: cada entrada identifica la sección que la utiliza y el requisito que respalda.

Este apartado desarrolla las responsabilidades y los contratos de la solución y su correspondencia con el esquema y la explicación de 3.3 y 3.4. La correspondencia se establece por capacidad: recepción e inventario (M1–M2), preventa y planificación (M3–M4), preparación y reparto (M5–M6), rendición y devoluciones (M7–M8), calidad y analítica (M9–M10), canal moderno y flota (M11–M12). El emplazamiento, las conexiones y su capacidad corresponden a 4.2; los centros de datos, a 4.3. Los catálogos extensos se entregan en los anexos 4-A a 4-V. El Anexo 4-N verifica las capacidades y contratos; la Tabla [8](LAFROX-Subdocumento4.md#tab:mapeo-logica) de 4.2.2 identifica su realización física.

En Puelche, un pedido debe poder tomarse en una ruta sin cobertura, prepararse durante la noche y llegar al cliente con su lote y su evidencia de entrega identificados. La arquitectura parte de esa continuidad: cada operación se registra donde ocurre y se reconcilia cuando vuelve la conexión. Para ordenar las responsabilidades, la solución se organiza en las ocho capas exigidas por el numeral 2.1 de las Bases Técnicas Transversales (cap. 2, p. 6; RT-02.01).

### 4.1.1 Especificaciones Tecnologías de Software a utilizar

<a id="subsec:tecnologias-software"></a>

El núcleo de negocio se implementa como monolito modular en Laravel 13 y PHP 8.5. Frente a microservicios por dominio, esta elección conserva una sola base de código y un despliegue comprensible para el equipo TI de cuatro personas; sincronización, mensajería EDI y telemetría se ejecutan como procesos separables cuando su carga lo exija. Laravel proporciona rutas, validación, políticas, contenedor de dependencias y trabajos en cola; las reglas de negocio permanecen en módulos propios, sin depender de esas interfaces. Se seleccionan PostgreSQL/PostGIS para transacciones y geografía, RabbitMQ local para conservar trabajo durante un corte y SQS FIFO para ordenar su entrega por partición al reconectar. Ni el framework ni la cola reemplazan la deduplicación y la conciliación de los consumidores.

Angular y TypeScript sirven los portales; Kotlin nativo en Android permite escaneo, captura de evidencia y almacenamiento cifrado en el parque móvil Zebra. Keycloak emite la identidad central mediante OIDC; las decisiones de autorización siguen siendo de cada servicio. La comparación con microservicios, aplicaciones híbridas y otros productos se resume en la sección de alternativas y en los ADR. Los servicios gestionados de AWS apoyan la ejecución y la integración; su ubicación y redundancia corresponden a 4.2. Estas elecciones deben sostenerse durante el contrato mediante actualización de versiones soportadas, sin prometer que una versión inicial durará 56 meses.

Los principios que gobiernan el diseño son los siguientes:

- **Continuidad sin conexión.** Preventa y reparto deben registrar un turno completo de 14 horas sin cobertura. El componente local debe mantener al menos 24 horas continuas de operación autónoma y degradada (RT-03.10; Bases Técnicas Transversales, cap. 3, p. 9). La sincronización posterior es idempotente: reenviar un evento no vuelve a ejecutar la operación. Los conflictos se resuelven con reglas de negocio documentadas, no dando prioridad automática al último registro recibido.

- **Atención adaptada al canal tradicional.** La solución no exige que los 11.600 almacenes instalen una aplicación ni dispongan de conexión propia. El conductor registra la entrega y su confirmación mediante firma o QR; los avisos por WhatsApp/SMS se utilizan cuando el canal está disponible. El almacenero que tiene teléfono puede, además, instalar el Portal de Clientes y armar su pedido sin señal; es un canal opcional que convive con el preventista.

- **Responsabilidades distribuidas.** Recepción, preparación y despacho conservan su núcleo transaccional disponible en cada sitio. Preventa, reparto y canal moderno disponen de servicios centrales, mientras las aplicaciones de terreno conservan la captura local cuando no pueden alcanzarlos. La ubicación, la capacidad y la redundancia de esos servicios se justifican en 4.2, conforme al Art. 16.

- **Evolución durante 56 meses.** La Etapa 1 comprende los meses 1–15, con producción en el mes 16; la Etapa 2, los meses 13–20, con producción en el mes 21. Los 36 meses de operación se extienden del mes 21 al 56 (Art. 17).

- **Verificación explícita del acceso.** La identidad central utiliza OIDC y MFA. Cada servicio verifica autorización, alcance y contexto; una solicitud no se considera confiable solo por provenir de la red corporativa. El cifrado y la auditoría acompañan cada intercambio.

- **Recuperación y reconciliación.** RT-07.04 exige RTO ≤ 4 horas y RPO ≤ 15 minutos para los servicios críticos. La extracción continua por fibra, LTE y satélite en los CD sostiene el RPO exigido aun ante la caída de los dos medios terrestres. El Anexo 4-M define AL-DR-01; el límite residual se justifica en 4.3.2. Los ambientes, medios de respaldo y conectividad redundante corresponden a 4.2.

- **Operación sostenible para cuatro personas.** Las herramientas, los procedimientos y el soporte deben permitir que el equipo TI de Puelche administre la solución con el apoyo del adjudicatario durante todo el contrato.

La descripción sigue la organización de vistas de ISO/IEC/IEEE 42010:2022 (International Organization for Standardization [ISO], 2022a). La vista lógica define las responsabilidades de los componentes y sus relaciones con los procesos, los datos, la seguridad y las integraciones. Cada decisión arquitectónica debe conservar su justificación, las alternativas consideradas y los requisitos que la sustentan (Bases Técnicas Transversales, cap. 2, p. 7; RT-02.04).

Las decisiones tecnológicas se registran con alternativas y criterios en el Anexo 4-O; el soporte y la actualización durante el contrato se especifican en el Anexo 4-P.

### 4.1.2 Principios de integración

<a id="subsec:principios-integracion"></a>

La integración no es un apéndice: es el tejido que sostiene la operación distribuida de Puelche. El riesgo principal del caso está en las costuras entre sistemas legados sin documentación de interfaces, no en los módulos nuevos. De las Bases Técnicas Transversales (RT-02.06 a RT-02.08 y RT-05.16; Bases Técnicas Transversales, cap. 2, p. 7, y cap. 5, p. 12) y del caso 02 se desprenden ocho reglas de diseño:

- **Contrato antes que conexión.** Cada interfaz tiene dueño, contrato OpenAPI o AsyncAPI, versión y comportamiento ante falla antes de entrar en operación.

- **Asincronía con excepciones justificadas.** Los eventos desacoplan procesos; disponibilidad, crédito, autorización de pago y actos tributarios que exigen respuesta se consultan con tiempo máximo de espera y estado explícito.

- **Idempotencia.** Una escritura conserva su UUID en todos los reintentos; el consumidor deduplica y resuelve conflictos por regla de negocio, no por la última marca de tiempo.

- **Reconciliación auditable.** Cada conflicto conserva operación, regla, resultado, autor y momento, conforme a la bitácora del Artículo 16.4 (Bases Administrativas, art. 16.4, p. 12).

- **Frontera única del legado.** La capa anticorrupción traduce hacia el ERP; ningún módulo o portal escribe directamente en él.

- **Confianza explícita.** Cada mensaje y llamada se autentica, autoriza y correlaciona; las excepciones de conectividad hacia el sitio son privadas, acotadas y auditadas.

- **Falla declarada.** Las quince entradas del catálogo indican si reintentan, se difieren, degradan o requieren procedimiento manual.

- **Ventana de despacho protegida.** Las cargas masivas, reprocesos y despliegues de conectores no interrumpen la operación de 05:30 a 07:00.

Estas reglas se verifican en los contratos, el catálogo de interfaces y las pruebas de falla de cada consumidor.

Estos principios se materializan en la capa de integración, los eventos canónicos, la capa anticorrupción, el catálogo de interfaces y las reglas de reconciliación descritas en este apartado.

El núcleo reúne M1–M12 en Laravel 13 sobre PHP 8.5, con dependencias fijadas por `composer.lock`. Cada módulo tiene espacio de nombres, servicios de aplicación, reglas de dominio y adaptadores propios. Esta organización evita que una pantalla o un cambio de proveedor invada otra capacidad. Para 14.200 clientes y unos 31.000 pedidos mensuales, se conserva la sencillez operativa del monolito modular, en línea con el numeral 2.3 de las Bases Técnicas Transversales. Sincronización, EDI y telemetría tienen trabajadores y capacidad de escalado independientes desde el inicio (RT-02.02; Bases Técnicas Transversales, cap. 2, p. 6); su emplazamiento se detalla en 4.2.

La volumetría operativa que condiciona el dimensionamiento es la siguiente: 14.200 clientes activos, 8.400 SKU (que pasan a aproximadamente 9.500), 31.000 pedidos mensuales con 260.000 líneas y 2,4 millones de unidades, aproximadamente 1.400 entregas diarias habituales con un pico de septiembre de 2.600 entregas (volumen casi duplicado durante tres semanas), 96 camiones en la ventana crítica de despacho (42 propios y 54 de transportistas externos), 62 preventistas, unos 160 conductores de transportistas y 310 personas de centro de distribución (Bases Técnicas del caso, cap. 14, pp. 24–25), además de 84 conductores propios y peonetas (Bases Técnicas del caso, cap. 2, p. 5). De esas 310 personas, 120 preparan pedidos en el turno nocturno de Talca (Bases Técnicas del caso, cap. 8, p. 14). El máximo horario global de septiembre alcanza 14,66 TPS a las 12:00, incluida la preventa y el portal; dentro de la ventana de despacho de 05:30 a 07:00, el máximo es 6,94 TPS. El diseño considera ambos picos según el proceso que dimensiona, nunca el promedio, y declara explícitamente los puntos únicos de falla (SPOF) con su mitigación conforme a RT-02.11.

El modelo distingue seis instalaciones: los CD de Talca y Concepción, las plataformas de cross-docking de Curicó, Chillán y Los Ángeles, y la casa matriz de Talca, contigua al CD principal (Bases Técnicas del caso, cap. 2, p. 5). Las primeras cinco ejecutan el mismo perfil `wms_only`, conservan autoridad sobre los movimientos de su bodega y publican eventos idempotentes para consolidar stock y reservas en N-04/N-05; la casa matriz no aloja cómputo propio y utiliza los portales y las consolas en nube. Los identificadores de sitio serán parametrizables para incorporar una séptima instalación proyectada a tres años y evaluar la futura operación en Los Lagos hacia 2030.

### 4.1.3 Capas de la arquitectura

Las ocho capas separan la interacción con las personas, las reglas de negocio y la persistencia. Seguridad y observabilidad atraviesan el conjunto. La vista general permite ubicar cada responsabilidad antes de revisar sus componentes; el inventario trazable se reúne en el Anexo 4-N.

Presentación reúne las superficies de trabajo; borde protege su entrada; puerta de enlace valida solicitudes; negocio decide por módulo; integración intercambia contratos; acceso a datos persiste por propietario. Seguridad y observabilidad atraviesan esas seis responsabilidades.

Las capas 7 y 8 atraviesan las demás; no duplican reglas de negocio.

La arquitectura se presenta primero mediante su vista general completa (Figura [1](LAFROX-Subdocumento4.md#fig:arql-general-completa)) y después mediante una síntesis de sus ocho capas (Figura [2](LAFROX-Subdocumento4.md#fig:arql-1)). Ambas vistas se complementan para relacionar las funciones de negocio con los componentes que las sostienen.

 **Figura 1 — Vista general completa de la arquitectura lógica**

![Vista general completa de la arquitectura lógica](https://raw.githubusercontent.com/PatricioH315/LafroX/d397c30ff8ad232ec4e3ea02caf5f3cb6800a547/04/figuras/logica/ARQL-01_Vision_general_9pt.pdf)

<a id="fig:arql-general-completa"></a>

Fuente: elaboración propia.

La vista general muestra cómo cada actor accede a la solución desde su aplicación, portal o consola y se relaciona con los módulos M1–M12. Se lee desde las personas hacia las reglas de negocio, las integraciones y los datos, distinguiendo los componentes de nube y los del sitio. Las conexiones representan intercambios sujetos a autorización, no acceso directo a las bases de datos. Seguridad y observabilidad acompañan todo el recorrido; sus controles y las condiciones de operación sin conexión se desarrollan en los apartados siguientes.

 **Figura 2 — Vista resumida de las ocho capas lógicas**

![Vista resumida de las ocho capas lógicas](https://raw.githubusercontent.com/PatricioH315/LafroX/d397c30ff8ad232ec4e3ea02caf5f3cb6800a547/04/figuras/logica/ARQL-19_Vista_general_legible.pdf)

<a id="fig:arql-1"></a>

Fuente: elaboración propia.

La vista resumida destaca la responsabilidad de cada capa: presentación captura y muestra información; borde protege la entrada; las puertas de servicio validan las solicitudes; el negocio aplica las reglas en Laravel; integración conserva y distribuye eventos; y acceso a datos administra la persistencia. Seguridad y observabilidad son transversales, no pasos finales del procesamiento. La puerta local permite que la bodega siga operando sin WAN, mientras las colas conservan el trabajo sin confirmar para reconciliarlo al recuperar la conexión.

#### 4.1.3.1 Capa de presentación (Capa 1)

La Figura [3](LAFROX-Subdocumento4.md#fig:arql-capa-1) presenta las responsabilidades de esta capa.

**Figura 3 — Presentación: aplicaciones y superficies de trabajo**

![Presentación: aplicaciones y superficies de trabajo](https://raw.githubusercontent.com/PatricioH315/LafroX/d397c30ff8ad232ec4e3ea02caf5f3cb6800a547/04/figuras/logica/capas_recortes/ARQL-21_Recorte_Presentacion.png)

<a id="fig:arql-capa-1"></a>
 Las aplicaciones móviles conservan las capturas sin confirmar; los portales y consolas consultan sus dominios mediante APIs autorizadas. El dispositivo y la pantalla no reemplazan la identidad ni los permisos de la persona.

La capa de presentación reúne las herramientas que utiliza cada persona para trabajar: aplicaciones móviles que pueden operar sin conexión y portales web servidos desde la nube. Preventistas, conductores y preparadores capturan hechos operativos; los clientes piden en autoatención y consultan sus datos, y transportistas y proveedores consultan únicamente sus datos autorizados; Calidad, gerencias, planificación y TI toman decisiones desde consolas especializadas. Los permisos se asignan mediante una matriz de roles y atributos: un perfil de interacción no implica por sí solo acceso a todas las funciones del módulo.

Las aplicaciones de los trabajadores (preventa, reparto y bodega) se construyen como una sola aplicación Kotlin nativa para Android, con un perfil para cada una, decisión alineada con el parque Zebra (EC55 en preventa, TC58e en reparto y MC9400 en las bodegas y los cross-docking) y con las condiciones de operación del terreno. La app de preventa mantiene una foto local de datos de lectura (stock, precios, crédito, promociones) y captura local de eventos (pedidos, identificadores únicos UUID); la app de reparto gestiona la entrega, la prueba de entrega digital (POD con firma, código QR y fotografía), la cobranza en ruta y el control de envases retornables. Ambas aplicaciones operan con datos locales cifrados y sincronizan de forma idempotente por medio del API Gateway cuando se recupera la conectividad.

Los terminales de bodega (HHT con escáner GS1) descargan las misiones de preparación al inicio del turno y registran su ejecución localmente, incluso en cámaras a -22 °C sin señal. La autonomía mínima de 24 horas comprende el servicio de bodega completo: registro de operaciones, conservación de datos, cambios de turno y control de acceso.

Los portales web, implementados en Angular con Tailwind CSS, permiten a transportistas revisar rutas y a proveedores consultar órdenes y recepciones. El Portal de Clientes permite pedir en autoservicio y consultar el estado de entrega, los documentos y el saldo (RT-16.30 del caso; Bases Técnicas del caso, cap. 15, p. 27). Se publica además como aplicación web progresiva, instalable desde el navegador en el teléfono del almacenero, y constituye el perfil de autoatención con operación desconectada de RT-17.01 del caso (Bases Técnicas del caso, cap. 15, p. 27). Sin señal, muestra el catálogo y los precios descargados con su fecha y permite armar el pedido, que queda en cola con su UUID y se envía por `/sync/v1` al recuperar cobertura. El pedido existe para la compañía solo cuando M3 lo recibe; la confirmación de stock, crédito y fecha de entrega espera esa recepción. La cuenta se activa en la visita del preventista con un código enviado por SMS al teléfono registrado, y nadie queda obligado a usarla. El catálogo público admite consulta sin autenticación; las funciones privadas requieren identidad OIDC mediante Keycloak y permisos por rol. El acceso administrativo exige MFA y una ruta autorizada, definida físicamente en 4.2.

Las consolas de rutas, calidad, BI y administración TI acceden a sus dominios mediante APIs autorizadas. Ningún navegador se conecta directamente a las bases de datos. Esta separación permite aplicar las mismas reglas de acceso y auditoría con independencia de la pantalla utilizada.

##### Actores del sistema, interfaces y autorización

El apartado 3.4.2.1 y el Anexo 3.I del Subdocumento 3 fijan quince actores del sistema: Preventista, Conductor propio, Conductor externo, Preparador, Cliente del canal tradicional, Cliente del canal moderno, Empresa transportista, Proveedor, Jefa de Calidad, Gerente Comercial, Gerente de Finanzas, Planificador de Rutas, Jefe de TI, Gerente de Operaciones y Jefa de Bodega. El Anexo 4-N relaciona cada actor con su interfaz, sus acciones, su ámbito de datos y su etapa. Una relación gráfica entre un actor y un módulo no concede acceso a todas sus funciones.

Empresa transportista y Proveedor acceden mediante personas representantes, identificadas y autorizadas por su organización. Conductor externo usa una identidad personal distinta, limitada a su turno y su ruta. Cliente del canal moderno tiene acceso humano al portal. El conector EDI de su cadena usa credenciales técnicas separadas. El canal tradicional mantiene la compra asistida y el pago en efectivo sin cuenta obligatoria. Su autoatención opcional y los portales externos se habilitan en la Etapa 2.

Los diecinueve interesados del negocio conservan su participación definida en los Subdocumentos 2 y 3. La Gerenta General recibe información de gobierno. El Sindicato de Choferes participa en los acuerdos de privacidad. La Autoridad Sanitaria recibe exportaciones auditadas de Calidad. Ninguno de ellos tiene cuenta directa en el sistema. El peoneta no comparte la sesión del conductor. Food service conserva su segmento comercial y usa el perfil de cliente del canal acordado. Recepción, despacho, catálogo y Tesorería son funciones autorizadas dentro de estos perfiles. Cada ejecutor tiene identidad personal y no existen cuentas genéricas por cargo.

El servicio verifica acción, recurso, empresa, sitio, ruta y turno antes de cada operación. Se separan registrar y aprobar una diferencia de caja, solicitar y autorizar una liberación sanitaria, y consultar y modificar reglas. La función de Tesorería se asigna a personas nominadas, distintas de quien registra. TI administra la plataforma con elevación controlada y no adquiere facultades de cobro ni de liberación sanitaria. Altas, cambios y bajas conservan el historial de permisos y la autoría de cada decisión.

#### 4.1.3.2 Capa de borde y exposición (Capa 2)

La Figura [4](LAFROX-Subdocumento4.md#fig:arql-capa-2) presenta las responsabilidades de esta capa.

**Figura 4 — Borde: entradas públicas, privadas y locales**

![Borde: entradas públicas, privadas y locales](https://raw.githubusercontent.com/PatricioH315/LafroX/d397c30ff8ad232ec4e3ea02caf5f3cb6800a547/04/figuras/logica/capas_recortes/ARQL-22_Recorte_Borde.png)

<a id="fig:arql-capa-2"></a>
 La entrada pública protege las APIs y rechaza el acceso directo a su origen. El acceso local sostiene la bodega sin WAN; Greengrass procesa los sensores de cámara, mientras AS2 conserva una superficie B2B distinta.

La capa de borde delimita la entrada pública y la entrada de dispositivos de terreno y bodega, donde la conectividad es intermitente. Define las siguientes responsabilidades; su despliegue se especifica en 4.2:

- **CDN (Amazon CloudFront).** Entrada pública de portales externos y APIs de negocio: distribuye contenido estático y encamina las rutas `/v1` y `/sync/v1` al API Gateway. El acceso directo al origen de esas APIs debe rechazarse y probarse. Las consolas internas usan acceso privado verificado; el transporte AS2 tiene una superficie separada, restringida a contrapartes registradas.

- **WAF gestionado (AWS WAF y AWS Shield Advanced).** Filtrado de tráfico con reglas OWASP Top 10 y reglas personalizadas por API; protección contra denegación de servicio en capas 3, 4 y 7.

- **Balanceador de carga (ALB).** Distribuye hacia los servicios privados el tráfico que API Gateway entrega mediante su integración privada. El flujo de acceso público es cliente → CloudFront/WAF → API Gateway → integración privada/ALB → servicio.

- **Acceso local y continuidad.** Los servicios del sitio aplican control de acceso propio y preservan la operación crítica aun cuando todos los enlaces externos estén indisponibles. En Talca y Concepción, Starlink fijo es el tercer camino en espera caliente tras fibra y LTE; en los cross-docking es el principal, con LTE de dos proveedores como respaldo y conmutación automática en menos de 30 segundos (ADR-02).

- **AWS IoT Greengrass.** Corre en tres gateways IoT industriales (Moxa UC-8200 o equivalente): dos en el CD Talca, que leen ambas cámaras por Modbus TCP para evitar un punto único de falla, y uno en el CD Concepción. Leen los sensores de cámara por Modbus y aplican la regla térmica local. Ante una excursión crítica y sostenida, bloquean el despacho en menos de 5 segundos desde su detección. Además, conservan 24 horas de datos sin enlace. No se instala en camiones: la posición de la flota llega por la API del tercero (INT-15). Los termógrafos registran toda la ruta en su memoria interna, avisan por BLE al terminal del conductor aun sin señal y este reenvía el aviso a la nube al recuperar cobertura; al volver el camión, el terminal descarga y envía el registro completo.

En los CD, Starlink permanece encendido con el túnel IPsec establecido y BGP de menor preferencia, por lo que toma tráfico solo cuando fallan fibra y LTE. En esa condición, la calidad de servicio prioriza DMS/WAL de Talca, la salida del broker y outbox, las guías hacia el ERP y el SII, la identidad y la telemetría crítica. Mantener el terminal encendido evita esperar la adquisición de satélites y la negociación del túnel durante la falla; la tarifa plana no añade costo por esa permanencia.

#### 4.1.3.3 Capa de puerta de enlace de servicios (Capa 3)

La Figura [5](LAFROX-Subdocumento4.md#fig:arql-capa-3) presenta las responsabilidades de esta capa.

**Figura 5 — Puertas de servicio: recorrido central y local**

![Puertas de servicio: recorrido central y local](https://raw.githubusercontent.com/PatricioH315/LafroX/d397c30ff8ad232ec4e3ea02caf5f3cb6800a547/04/figuras/logica/capas_recortes/ARQL-23_Recorte_Puertas.png)

<a id="fig:arql-capa-3"></a>
 El recorrido central valida la identidad y entrega solicitudes a servicios privados. La puerta local atiende al HHT dentro del sitio, sin invocar el Gateway remoto durante un corte; ambos recorridos conservan validación, idempotencia y auditoría.

Amazon API Gateway concentra la publicación de servicios detrás de la entrada pública de CloudFront. El diseño requiere validar la identidad emitida por Keycloak, controlar esquema, cuotas y tasa de solicitudes, y propagar un `transaction_id`. Se selecciona REST API con authorizer REQUEST que verifica firma, emisor, audiencia, expiración y alcance del JWT de Keycloak. Las operaciones sensibles no reutilizan autorizaciones almacenadas; el módulo verifica además recurso y revocación conocida. La integración privada usa VPC Link V2 hacia ALB; la validación básica de Gateway se complementa con el esquema completo en Laravel (Amazon Web Services [AWS], s. f.-a, s. f.-b, s. f.-c; Anexo 4-O, ADR-13). El recorrido físico y el bloqueo efectivo del acceso directo al origen se deben comprobar en 4.2.

La capa publica dos conjuntos de APIs: las de negocio (`/v1`) y las de sincronización offline (`/sync/v1`). El Gateway aplica los controles de entrada y enruta las solicitudes. El servicio de negocio valida el contenido y garantiza la idempotencia de cada escritura mediante su UUID, una ventana de deduplicación documentada y el registro persistente del resultado (RT-02.06; Bases Técnicas Transversales, cap. 2, p. 7).

El ingreso por API Gateway corresponde a los servicios en nube. Durante una interrupción del enlace, la bodega utiliza los servicios de su sitio sin depender del Gateway remoto. Los terminales sin cobertura conservan sus eventos y los entregan al servicio local cuando recuperan comunicación; la reconciliación con la nube ocurre al restablecerse el enlace externo. Los contratos y las reglas de validación se mantienen en ambos recorridos.

La bodega dispone además de una puerta de API *local* como función del motor WMS A-01, en VM-01, VM-C01 y E-01, acotada a la red del sitio y a M1, M2, M5, la recepción física de retornos de M8 y la función local de bloqueo de M9. Los terminales de bodega no llaman a Amazon API Gateway durante un corte: el verificador local valida la autorización de turno y esta función aplica esquema, límites de tasa, tamaño de carga, UUID y registro de auditoría antes de entregar una orden al módulo correspondiente. Este control no publica una segunda entrada en internet ni emite identidades nuevas. La Figura [6](LAFROX-Subdocumento4.md#fig:arql-17) separa los dos recorridos y muestra cómo se conserva el trabajo hasta la reconexión.

 **Figura 6 — Identidad y puerta de API local durante un corte de 24 horas**

![Identidad y puerta de API local durante un corte de 24 horas](https://raw.githubusercontent.com/PatricioH315/LafroX/d397c30ff8ad232ec4e3ea02caf5f3cb6800a547/04/figuras/logica/ARQL-17_Acceso_local_24h.png)

<a id="fig:arql-17"></a>

Fuente: elaboración propia.

El manifiesto de turno firmado por Keycloak llega antes del corte; en cada relevo el verificador local, alojado junto a la caché, valida el manifiesto y un segundo factor local: el PIN personal sobre el terminal enrolado por MDM. El permiso queda limitado a funciones de bodega, mientras los eventos y la bitácora se envían después con su identificador original. La prueba debe iniciar el corte antes de dos relevos sucesivos y medir vencimiento, denegación, reintentos y recuperación; la caché de identidad de 24 horas no emite sesiones y el relevo lo habilita el verificador local.

#### 4.1.3.4 Capa de lógica de negocio (Capa 4)

La Figura [7](LAFROX-Subdocumento4.md#fig:arql-capa-4) presenta las responsabilidades de esta capa.

**Figura 7 — Negocio: monolito modular Laravel y sus doce módulos**

![Negocio: monolito modular Laravel y sus doce módulos](https://raw.githubusercontent.com/PatricioH315/LafroX/d397c30ff8ad232ec4e3ea02caf5f3cb6800a547/04/figuras/logica/capas_recortes/ARQL-24_Recorte_Negocio.png)

<a id="fig:arql-capa-4"></a>
 La figura reúne los doce módulos de negocio y sus funciones principales, junto con las tecnologías del backend y los sistemas externos con los que se relacionan. Los límites e intercambios de cada contexto se desarrollan en los apartados siguientes.

La capa de servicios de negocio reúne M1–M12 en un monolito modular Laravel. Cada contexto separa `Domain`, `Application`, `Infrastructure` y `Http` bajo un espacio de nombres PSR-4. Los controladores reciben y validan solicitudes; los servicios de aplicación coordinan casos de uso; el dominio decide reservas, bloqueos y rendiciones; los adaptadores traducen persistencia e integraciones. Los módulos se llaman mediante interfaces públicas o eventos versionados: no acceden a las tablas privadas de otro contexto ni importan sus modelos de persistencia. Los proveedores de servicios registran esas interfaces en el contenedor y una prueba de dependencias impide invertir las fronteras. Así, compartir proceso no confunde la propiedad de cada decisión (RT-02.02; Bases Técnicas Transversales, cap. 2, p. 6).

La misma versión del artefacto Laravel ejecuta perfiles separados: API central, WMS local limitado a M1/M2/M5, recepción física de retornos de M8 y bloqueo M9, consumidores de SQS, adaptador AMQP y reglas comerciales EDI de M11. El transporte OpenAS2 es un componente independiente: verifica certificados, firma, cifrado y acuses MDN antes de entregar el mensaje a M11; no ejecuta reglas comerciales ni escribe en el ERP. Cada perfil dispone de cola, concurrencia, permisos y métricas propios. El planificador de tareas tiene una sola autoridad por ambiente. Esta separación permite escalar y reiniciar sincronización, EDI y telemetría sin multiplicar el monolito completo. Los componentes críticos se despliegan y revierten de forma independiente (RT-02.02; Bases Técnicas Transversales, cap. 2, p. 6): el perfil `wms_only` se actualiza sitio por sitio sin tocar la API central, y `erp-sync` con la ACL, el shipper de cada sitio, el consumidor de reconciliación, el motor de rutas, el transporte AS2 y las consolas tienen su propio servicio, su versión desplegada y su reversión. Un sitio puede operar con la entrega previa mientras la nube ya opera la nueva, porque los contratos aceptan la edición vigente y la anterior. Además, cada capacidad se habilita por sitio con indicadores de funcionalidad.

Los módulos evitan estado durable en memoria y pueden crecer por réplicas o por trabajadores independientes, según la demanda. Los umbrales, límites de capacidad, emplazamiento y costos se especifican en 4.2 y en la oferta económica.

#### 4.1.3.5 Capa de integración y eventos (Capa 5)

La Figura [8](LAFROX-Subdocumento4.md#fig:arql-capa-5) presenta las responsabilidades de esta capa.

**Figura 8 — Integración: continuidad local y contratos con terceros**

![Integración: continuidad local y contratos con terceros](https://raw.githubusercontent.com/PatricioH315/LafroX/d397c30ff8ad232ec4e3ea02caf5f3cb6800a547/04/figuras/logica/capas_recortes/ARQL-25_Recorte_Integracion.png)

<a id="fig:arql-capa-5"></a>
 El sitio conserva los eventos hasta confirmar su publicación y el consumidor confirma después de persistir. La ACL concentra el acceso al ERP, único emisor tributario; el hub EDI traduce contratos comerciales y las excepciones permanecen trazables.

La capa de integración conecta la nueva operación con sistemas que Puelche ya utiliza. Sus límites son especialmente importantes ante el ERP de 2017 sin interfaces documentadas y el WMS de 2013. También concentra el intercambio con cadenas del canal moderno, los servicios de pago, los mapas y la telemetría, de modo que un cambio externo no obligue a modificar cada módulo de negocio.

RabbitMQ conserva las colas de integración local. En nube, SQS FIFO ordena los mensajes de reconciliación dentro de cada grupo y SNS difunde eventos y alertas. Los avisos al cliente se entregan mediante SNS o la API del proveedor de notificaciones (INT-11). El orden no se presume global ni se atribuye a toda la cadena de eventos. Los consumidores aplican deduplicación, reintentos con espera creciente y una cola de mensajes fallidos (DLQ), con intervención trazable cuando el procesamiento no puede completarse (RT-02.07; Bases Técnicas Transversales, cap. 2, p. 7).

El shipper publica en la cola SQS FIFO de reconciliación un sobre JSON independiente de PHP con versión, identidad, clave de orden y carga. Un consumidor PHP dedicado lee ese sobre mediante el SDK de AWS, valida su esquema, invoca el caso de uso Laravel y reconoce el mensaje solo después de persistir el resultado. Las solicitudes al ERP viajan por otra cola, la cola FIFO de solicitudes al ERP, que solo lee `erp-sync` en VM-04 de Talca; cada respuesta vuelve a su sitio por una cola FIFO de respuesta propia, que el shipper del sitio lee por conexión saliente y entrega a RabbitMQ local. Los trabajos derivados propios de Laravel usan su conector SQS en colas distintas y declaran grupo y clave de deduplicación cuando requieren orden FIFO. Esta separación evita entregar mensajes externos al deserializador de trabajos del framework. RabbitMQ local se conecta mediante un adaptador AMQP probado con `php-amqplib`; el shipper confirma la publicación en SQS antes de reconocer el mensaje local. No se introduce Redis ni Horizon en los sitios, donde la continuidad depende de PostgreSQL y RabbitMQ.

Las APIs de la plataforma reciben solicitudes por la Capa 3. Los servicios de negocio invocan sus adaptadores de integración cuando necesitan consultar pagos o mapas, con tiempo máximo de espera explícito (RT-02.08; Bases Técnicas Transversales, cap. 2, p. 7). Los intercambios diferidos con ERP, EDI, telemetría y notificaciones utilizan colas y reintentos. La emisión tributaria se canaliza por el ERP mediante la ACL; no se crea un segundo emisor de documentos ante el SII.

El ERP de 2017 se conserva como única fuente de verdad tributaria y único emisor de DTE. La capa anticorrupción (ACL) traduce los contratos de la solución al formato del legado, sin reemplazarlo ni modificar su código. El flujo de rendición es: rendición aprobada → cola FIFO de solicitudes al ERP → `erp-sync` en VM-04 de Talca → ACL local → ERP. Dos procesos de `erp-sync` consumen además RabbitMQ local para las solicitudes del WMS de Talca; acceden a la cola de solicitudes mediante conexión saliente. Ningún módulo, portal o cadena escribe directamente en el ERP. El trabajador usa una clave idempotente por operación y conserva folio, estado y acuse para seguir cada documento hasta su origen; reintentar un trabajo no solicita un segundo documento. M5 solicita la guía al cerrar la carga nocturna; cualquier cambio de carga invalida la guía y exige una nueva. El ERP sigue como único emisor ante el SII por fibra, LTE o satélite.

La integración con las cadenas del canal moderno se resuelve con un hub EDI centralizado en nube. Utiliza mensajes comerciales EANCOM y GS1 XML, y eventos EPCIS para trazabilidad. Cada cadena dispone de un conector configurable, una tabla de equivalencias GTIN (RF-12.03) y una bandeja de excepciones (RF-12.06). El hub transforma los mensajes al modelo canónico y entrega al ERP, exclusivamente mediante la ACL, la información necesaria para sus documentos, incluida la guía de despacho electrónica (GDE). AS2 es uno de los transportes del hub. El canal moderno debe quedar operativo a más tardar en enero de 2029.

##### Eventos canónicos del dominio

<a id="subsubsec:eventos-canonicos"></a>

Los eventos son el vocabulario del sistema. Se nombran en pasado, son inmutables y llevan `event_id` (UUID), `occurred_at`, `site_id` y `transaction_id`. El catálogo de eventos canónicos del dominio se presenta en el Anexo 4-A. Cada evento declara productor único, consumidores registrados, clave de partición y política de reintento, y su origen se traza a un requisito del caso o a una decisión del numeral 16.1.

Los esquemas AsyncAPI 2.6 versionados por evento se gobiernan desde el Catálogo de interfaces (§ [4.1.6](LAFROX-Subdocumento4.md#sec:catalogo-interfaces)); `transaction_id` conserva la correlación entre los módulos consumidores.

##### Orquestación y coreografía

M3 solicita a M2 la reserva de cada pedido y lo deja pendiente hasta que M2 central persiste el acuse de la retención en el sitio. La respuesta llega de forma asíncrona y queda visible para el preventista como confirmación o quiebre. Cuando el pedido queda confirmado, publica `PedidoConfirmado`; M4, M5 y M10 reaccionan a ese hecho; M11 también lo consume solo para pedidos de cadenas, a fin de responder a la cadena mediante su propio consumidor. Esa coreografía evita que M3 conozca el horario de preparación o el esquema analítico. La publicación se registra junto con el cambio de estado mediante una bandeja transaccional de salida (*outbox*); el consumidor confirma su progreso solo después de persistir su resultado. Si falla un consumidor, la cola reintenta y termina en una bandeja de excepción, sin deshacer a ciegas el pedido ya confirmado.

El despacho tiene una coordinación distinta: M5 no libera la carga hasta recibir el resultado de M9 sobre el lote y la guía emitida por el ERP a través de la ACL. Una excursión crítica y sostenida bloquea localmente la salida aun con el enlace caído; solo Calidad puede liberar el lote tras evaluación registrada. El conductor informa la incidencia y conserva la carga, pero no aprueba su liberación sanitaria. Las Figuras [9](LAFROX-Subdocumento4.md#fig:arql-15) y [10](LAFROX-Subdocumento4.md#fig:arql-16) recorren el pedido con y sin conexión y hacen visible dónde cambia una captura sin confirmar a una operación confirmada.

 **Figura 9 — Secuencia lógica del pedido con conexión**

![Secuencia lógica del pedido con conexión](https://raw.githubusercontent.com/PatricioH315/LafroX/d397c30ff8ad232ec4e3ea02caf5f3cb6800a547/04/figuras/logica/ARQL-15_Pedido_con_conexion.png)

<a id="fig:arql-15"></a>

Fuente: elaboración propia.

Con conexión, M2 devuelve una reserva explícita y M5 no comienza a preparar un pedido rechazado. La carga preparada sigue retenida si M9 informa un bloqueo o si el ERP no devuelve la guía electrónica. El flujo dibuja esos dos retornos porque un pedido confirmado no autoriza por sí mismo la salida física.

 **Figura 10 — Secuencia lógica del pedido capturado sin conexión**

![Secuencia lógica del pedido capturado sin conexión](https://raw.githubusercontent.com/PatricioH315/LafroX/d397c30ff8ad232ec4e3ea02caf5f3cb6800a547/04/figuras/logica/ARQL-16_Pedido_sin_conexion.png)

<a id="fig:arql-16"></a>

Fuente: elaboración propia.

Sin conexión, la aplicación conserva la intención de compra, no una reserva firme. El mismo UUID viaja en todos los reintentos; M3 y M2 producen un resultado durable con la regla y la causal de excepción. Si se pierde el acuse de respuesta, el dispositivo conserva el evento y pregunta por ese UUID antes de eliminarlo. Solo un pedido confirmado alimenta M5, lo que permite explicar al cliente un faltante sin duplicar la venta.

##### Contratos de integración

<a id="subsubsec:contratos-integracion"></a>

Las APIs síncronas se describen en OpenAPI 3.1 por módulo y versión mayor. Cada operación declara dueño, esquema de solicitud y respuesta, identidad requerida, errores de negocio, límites de tasa y fecha de retirada. El Gateway valida la entrada, pero la decisión de negocio y la idempotencia pertenecen al servicio. Las interfaces de sincronización `/sync/v1` reciben lotes con UUID por operación y devuelven un resultado individual, de modo que un error de una entrega no obligue a repetir todas las demás.

Los eventos se describen en AsyncAPI 2.6 con productor único, consumidores, clave de partición, versión, política de reintento y cola de fallidos. Los mensajes viajan al menos una vez: cada consumidor deduplica por `event_id` y preserva orden dentro del agregado que lo exige. OAuth con PKCE protege clientes interactivos; mTLS y credenciales rotadas protegen servicios. `transaction_id` enlaza llamada, evento, resultado y evidencia de auditoría.

##### Capa anticorrupción y sustitución del WMS

<a id="subsubsec:acl-estrangulamiento"></a>

**Frontera única del ERP (A-04).** El ERP de 2017 no tiene documentación de interfaces. En vez de descubrir su forma real dentro de cada módulo, se levanta una sola frontera: la ACL expone hacia adentro un contrato OpenAPI 3.1 propio de Puelche y absorbe hacia afuera la forma del ERP. Consecuencias:

- El conocimiento del ERP queda concentrado y documentado en un solo componente, no disperso en doce módulos.

- Ningún módulo, portal ni cadena de supermercados escribe al ERP: el trabajador `erp-sync` en VM-04 consume RabbitMQ local y, por salida, la cola FIFO de solicitudes al ERP, y llama a la ACL del mismo sitio mediante su contrato versionado.

- Cuando una capacidad del ERP se absorbe en la plataforma, se retira de la ACL sin tocar a los consumidores.

**Estrangulamiento del WMS de 2013 (ADR-08, Decisión 16.1 N° 14).** El WMS se reemplaza en la Etapa 1 por los módulos M1, M2 y M5 del monolito. Cada ola quita al legado la escritura de esa capacidad, y al cerrar la marcha blanca de Talca el WMS de 2013 se apaga y se retira. La Tabla [1](LAFROX-Subdocumento4.md#tab:capacidad-wms) indica qué capacidad se absorbe en cada ola y cómo se revierte por sitio.

<a id="tab:capacidad-wms"></a>

**Tabla 1 — Capacidad absorbida del WMS 2013 por ola**

| **Capacidad WMS 2013** | **Módulo** | **Ola** | **Estrategia / Reversión** |
| --- | --- | --- | --- |
| Recepción GS1 | M1 | 1 | Azul-verde por sitio; reversión a la entrega previa |
| Slotting / ubicaciones | M2 | 1–2 | Azul-verde por sitio; reversión a la entrega previa |
| Misiones picking HHT | M5 | 2 | Azul-verde por sitio; reversión a la entrega previa |
| Conteo cíclico | M2 | 2–3 | Azul-verde por sitio; reversión a la entrega previa |

Fuente: Anexo 4-O, ADR-08, y las Bases Técnicas del caso (cap. 16, p. 29), decisión 14.

La sustitución por olas permite comprobar cada capacidad antes de retirar la precedente.

No se mantiene el WMS 2013 como sistema operativo en producción tras la Etapa 1. La ACL garantiza que ningún módulo, portal ni cadena escribe al ERP/WMS legado directamente.

**Hub EDI GS1 (ADR-11).** Una cadena nueva se incorpora por configuración de perfil (equivalencias GTIN por cadena, RF-12.03), no por desarrollo. El hub mapea cada cadena contra un modelo canónico GS1, no contra el ERP; así evita construir una integración diferente en los doce módulos de negocio.

##### Versionado y gobierno de integración

<a id="subsubsec:versionado-gobierno"></a>

Los contratos siguen versiones `major.minor.patch`. Un cambio aditivo conserva compatibilidad; retirar un campo exige marcarlo como obsoleto y anunciar la fecha de salida con al menos seis meses de anticipación. Dos versiones pueden convivir mientras migran los consumidores identificados. Un cambio incompatible requiere aprobación del Comité de Arquitectura, pruebas de contrato y plan de reversión. Los perfiles de cadenas se versionan sin alterar el vocabulario común del hub; los cambios de interfaces tributarias se gestionan en la ACL, no como perfiles EDI. El Anexo 4-B asigna dueño y evidencia a cada mecanismo de gobierno.

El catálogo y las pruebas hacen visible quién responde cuando un contrato cambia o falla.

##### Carga y descarga masiva de datos

<a id="subsubsec:carga-masiva"></a>

Las importaciones históricas y las extracciones regulatorias utilizan contratos distintos de la operación diaria. El Anexo 4-C compara su mecanismo, la prueba de integridad y el tratamiento de rechazos; ninguna carga masiva desplaza la preparación durante la ventana crítica de despacho.

El procesamiento por lotes conserva totales y rechazos sin bloquear la operación diaria.

**Regla transversal:** ninguna carga masiva se ejecuta dentro de la ventana crítica 05:30–07:00, y toda carga queda registrada y es auditable.

#### 4.1.3.6 Capa de acceso a datos (Capa 6)

La Figura [11](LAFROX-Subdocumento4.md#fig:arql-capa-6) presenta las responsabilidades de esta capa.

**Figura 11 — Datos: propiedad y persistencia híbrida**

![Datos: propiedad y persistencia híbrida](https://raw.githubusercontent.com/PatricioH315/LafroX/d397c30ff8ad232ec4e3ea02caf5f3cb6800a547/04/figuras/logica/capas_recortes/ARQL-26_Recorte_Datos.png)

<a id="fig:arql-capa-6"></a>
 El sitio conserva la autoridad de bodega y el dispositivo mantiene sus capturas hasta recibir confirmación durable. Los servicios centrales separan transacciones, caché, documentos y analítica; ninguna consulta de BI debe competir con el despacho.

La capa de datos distingue quién conserva la información operativa, quién la consolida y quién la consulta para análisis. Esta separación permite que la bodega siga trabajando sin enlace externo y que las consultas gerenciales no compitan con el despacho. Los dominios de información asumen las siguientes responsabilidades:

En la operación local:

- **CD Talca:** PostgreSQL 16 con PostGIS y perfil `wms_only` como autoridad de los movimientos físicos de Talca, con autonomía mínima de 24 horas.

- **CD Concepción:** PostgreSQL y el mismo perfil `wms_only`, capaz de sostener 24 horas de operación local sin depender de Talca, en un par de servidores activo y en espera (RT-03.14; Bases Técnicas Transversales, cap. 3, p. 9).

- **Cross-docking de Curicó, Chillán y Los Ángeles:** el mismo perfil `wms_only` en un par de equipos E-01, uno activo y otro en espera, para recepción, desconsolidación y despacho. Cada sitio publica su detalle por SQS FIFO hacia la consolidación en nube. Las tres horas indicadas en el caso son una ventana operativa, no una excepción a RT-03.10: el diseño lógico exige al menos 24 horas de continuidad local degradada, cuya suficiencia deberá demostrarse mediante pruebas.

En los servicios centrales, N-04/N-05 consolidan stock por sitio y la reserva de preventa mediante eventos idempotentes; PostgreSQL conserva las transacciones de preventa, reparto y canal moderno; el flujo de telemetría ingresa en DynamoDB y se consolida para análisis en S3 y Redshift mediante Glue; Redis acelera lecturas autorizadas de stock, precios y sesiones; S3 conserva documentos y evidencias. La función de cada almacén, y no su ubicación física, determina qué módulo puede escribir en él. La topología de replicación y recuperación se especifica en 4.2.

No se incorpora Redis local. Al iniciar el turno con conexión, la aplicación solicita a las APIs una copia de stock, precios y demás datos autorizados; los servicios la obtienen de sus almacenes, incluido ElastiCache. El dispositivo conserva esa copia cifrada en SQLite/Room y consulta allí mientras está desconectado. Al reconectar, reconcilia primero las escrituras sin confirmar y actualiza los datos de lectura. Reemplazar la copia de lectura nunca debe borrar pedidos, cobros ni evidencias aún no confirmados por el servidor.

La vigencia de los datos de lectura es independiente de la identidad. Las credenciales de turno duran 8 horas en bodega y 14 horas en terreno; la caché local de identidad es de solo lectura y tiene TTL de 24 horas en VM-05 (Talca), VM-C03 (Concepción) y E-01 de cada cross-docking. Una copia reciente de precios no renueva la sesión y una sesión válida no convierte el stock descargado en una reserva confirmada. El relevo de turno sin IdP lo habilita el verificador local del mismo nodo, conforme a la capa de seguridad de este apartado.

La separación transaccional/analítica es estricta: la analítica no lee del transaccional para evitar degradar la ventana crítica de despacho. Las latencias comprometidas son: operación del día ≤ 5 minutos, cierre comercial ≤ 2 horas, gestión ≤ 4 horas.

Cada evento conserva identidad, estado y resultado hasta recibir confirmación durable. DMS replica el WMS de Talca hacia un esquema de lectura; no escribe en las tablas de negocio centrales. Los consumidores de eventos actualizan estas últimas con deduplicación transaccional por sitio y UUID. Concepción y los cross-docking sincronizan sus eventos sin presumir un flujo DMS propio. Durante un corte cada sitio retiene sus cambios dentro de una capacidad comprobada para 24 horas. La extracción continua de DMS/WAL de Talca y de outbox por fibra, LTE y satélite sostiene RPO ≤ 15 minutos; AL-DR-01 del Anexo 4-M verifica la protección externa y 4.3.2 justifica el límite residual. El esquema 3-2-1-1-0, los medios de respaldo y la restauración se desarrollan en 4.2.

#### 4.1.3.7 Capa de seguridad transversal (Capa 7)

La Figura [12](LAFROX-Subdocumento4.md#fig:arql-capa-7) presenta las responsabilidades de esta capa.

**Figura 12 — Seguridad: identidad y autorización transversal**

![Seguridad: identidad y autorización transversal](https://raw.githubusercontent.com/PatricioH315/LafroX/d397c30ff8ad232ec4e3ea02caf5f3cb6800a547/04/figuras/logica/capas_recortes/ARQL-27_Recorte_Seguridad.png)

<a id="fig:arql-capa-7"></a>
 Keycloak emite la identidad y cada módulo decide la autorización sobre su recurso. Sin enlace, el verificador usa permisos de turno previamente firmados; el cifrado y la auditoría protegen los datos y decisiones a lo largo de todas las capas.

La seguridad atraviesa las ocho capas. Su unidad de decisión no es la red desde la que llega una solicitud, sino el sujeto, el recurso, la acción y el contexto del turno. Keycloak conserva la autoridad de identidad; el servicio dueño del recurso conserva la decisión de autorización. Esta separación evita que un token válido permita, por sí solo, liberar una carga, consultar crédito o modificar una regla de calidad (Bases Técnicas Transversales, caps. 11–12, pp. 23–26; RT-11.01 y RT-12.05; National Institute of Standards and Technology [NIST], 2020).

##### Límites de confianza y capa expuesta

La Figura [1](LAFROX-Subdocumento4.md#fig:arql-general-completa) distingue personas, dispositivos, sitio, servicios centrales y terceros. CloudFront protege los portales externos y sus APIs; el origen de esas APIs rechaza el acceso público directo. Las consolas internas usan acceso verificado por identidad y postura del dispositivo hacia servicios privados. OpenAS2 expone un canal B2B distinto, limitado a contrapartes registradas y con validación criptográfica y MDN; no es una API pública de negocio. Los almacenes de datos no son superficies públicas. El inventario de dominios, puertos y rutas de 4.2 debe representar las tres superficies por separado (RT-11.07 y RT-11.13; Bases Técnicas Transversales, cap. 11, p. 23).

API Gateway verifica la identidad, el alcance, las cuotas, los límites de tasa, el esquema y la carga útil antes de entregar una solicitud; M1–M12 repiten la autorización de negocio sobre el recurso concreto. Los puntos públicos incorporan detección de bots y reto progresivo sin bloquear a una persona legítima. La comunicación entre servicios se autentica mutuamente y se cifra; un evento asíncrono también conserva productor, destinatario, versión, identificador y permisos necesarios. Así se aplica el mismo límite de confianza a REST y a mensajería (RT-11.11–11.12; Bases Técnicas Transversales, cap. 11, p. 23).

La política lógica prohíbe el ingreso público directo a los sitios. Las excepciones de integración a través de un túnel privado no son exposición a internet: se autorizan de forma nominativa, por origen, destino y propósito, y se registran. La única conexión iniciada desde nube hacia un sitio es DMS hacia VM-02 de Talca, nominada y auditada por IPsec; las demás conexiones de los sitios se inician hacia nube. Las reglas de red se especifican en 4.2; una excepción no amplía el permiso de los módulos para escribir directamente en el ERP.

##### Identidad, autorización y sesiones

La identidad central utiliza OIDC, SSO y MFA. El rol se complementa con atributos de instalación, turno, ruta, dispositivo y empresa transportista. El proveedor solo consulta sus órdenes; el representante del transportista declara sus conductores y consulta sus rutas asignadas; el conductor actúa sobre su entrega y rendición; Calidad decide sobre un lote bloqueado; y Tesorería aprueba la conciliación, sin que quien registró el cobro pueda aprobar su propia diferencia. Los administradores elevan privilegios por tiempo limitado, con aprobación y registro de sesión. El alta, cambio de rol y baja quedan vinculados al ciclo de vida laboral o contractual, con baja efectiva antes de 24 horas desde la desvinculación, y los administradores usan además claves de acceso FIDO2; las personas externas disponen de registro, verificación y recuperación de acceso sin requerir correo corporativo (RT-12.01–12.06 y RT-12.09–12.12; Bases Técnicas Transversales, cap. 12, pp. 25–26).

En las APIs Laravel, un guard OIDC comprueba firma con las claves publicadas por Keycloak, emisor, audiencia, vencimiento y alcance. Las políticas del módulo dueño verifican además recurso, turno y atributos; se prueban tanto rutas HTTP como trabajos asíncronos para que una cola no eluda la autorización. El acceso local usa exclusivamente el verificador de manifiestos descrito abajo. Laravel no emite otra identidad de usuario mediante Sanctum o Passport: Keycloak sigue siendo el único IdP y la administración de personas se realiza en el portal Angular autorizado.

En conexión, el token de acceso dura como máximo 30 minutos; la inactividad cierra la sesión administrativa a los 15 minutos y las demás a los 30. La credencial de refresco es rotatoria, se invalida ante baja o sospecha de compromiso y no supera 24 horas para acceso ordinario ni 8 horas para privilegios. El cierre de sesión se propaga a los servicios conectados y se impide la concurrencia no autorizada para cuentas compartibles por riesgo. Ninguna credencial se transporta en la URL. Estas duraciones no renuevan ni alargan una autorización offline; responden a los controles de RT-12.07–12.08.

La credencial de turno dura hasta 8 horas en bodega y hasta 14 horas en terreno. Mientras existe enlace, Keycloak renueva al menos cada hora un manifiesto firmado con los turnos y permisos preinscritos para una ventana de 26 horas; así, incluso si el corte comienza justo antes de la renovación siguiente, quedan al menos 25 horas de verificación local. La caché de identidad, de solo lectura y TTL de 24 horas, conserva datos recibidos en VM-05 (Talca), VM-C03 (Concepción) y E-01 de cada cross-docking, pero no emite sesiones. Al relevarse un turno sin enlace, el verificador del mismo nodo comprueba la firma y vigencia del manifiesto y un segundo factor local: el PIN personal sobre el terminal enrolado por MDM; limita el acceso a M1, M2, M5, a la recepción física de retornos de M8 y a las acciones autorizadas de M9, bloquea intentos repetidos y registra cada decisión. El dispositivo compartido identifica el contexto, pero no sustituye la identidad personal del operario. Los detalles de claves y alojamiento pertenecen a 4.2 (ADR-06).

La revocación es inmediata en los servicios conectados. Durante una desconexión no se promete revocación remota instantánea: el permiso local expira al terminar su turno, no se amplía sin enlace y la incidencia se marca para revisar operaciones al reconectar. Una baja conocida localmente bloquea de inmediato la credencial en ese sitio; el verificador sincroniza las revocaciones y auditorías al restablecerse el enlace. Se ensayan dos relevos dentro de 24 horas, vencimiento, pérdida de dispositivo y recuperación del enlace. La cuenta de emergencia exige doble autorización, alcance acotado, custodia fuera de banda, registro y rotación posterior; no reemplaza la autenticación ordinaria de todos los operarios (RT-03.10 y RT-12.13; Bases Técnicas Transversales, cap. 3, p. 9, y cap. 12, p. 26).

##### Clasificación, cifrado y custodia

La Tabla [2](LAFROX-Subdocumento4.md#tab:seguridad-clasificacion) resume cómo cambia el control según el dato. La clasificación se aplica al evento, su copia local, las APIs y las exportaciones, no solo a la base de datos central.

<a id="tab:seguridad-clasificacion"></a>

**Tabla 2 — Clasificación lógica y protección de la información**

| **Nivel** | **Ejemplo del caso** | **Regla de acceso** | **Protección adicional** |
| --- | --- | --- | --- |
| Restringido | Credenciales, claves y factores. | Solo custodios nominados. | Claves separadas y auditoría. |
| Confidencial | Crédito, conducta de pago, geolocalización y POD. | Rol, finalidad y registro de consulta. | Cifrado por campo sensible. |
| Interno | Pedidos, movimientos y telemetría operativa. | Módulo dueño y perfiles autorizados. | Cifrado y trazabilidad. |
| Público | Catálogo sin precios. | Lectura anónima controlada. | Integridad y protección antiabuso. |

Fuente: elaboración propia a partir de RT-11.03, RT-11.09 y RT-11.10 (Bases Técnicas Transversales, cap. 11, p. 23; Bases Técnicas del caso, cap. 15, p. 27).

La categoría confidencial exige separar quién puede usar el dato de quién administra su almacenamiento: el acceso a la base no revela por sí solo comportamiento de pago ni geolocalización. Todo dato en reposo se cifra; los campos sensibles del caso reciben además cifrado por campo. En tránsito se exige TLS 1.3 para las interfaces compatibles, se prohíben TLS 1.0 y 1.1, se automatiza la gestión de certificados y se emplea mTLS entre servicios. La custodia y rotación de claves mantienen separación de funciones. El PAN de tarjetas no se almacena; se usa la tokenización de la pasarela. El RUT requiere una técnica de seudonimización con acceso a la clave separado y una finalidad documentada, sin confundir cifrado reversible con anonimización. La geolocalización de personas conserva la retención de 12 meses del caso y un registro de consultas; la región primaria sa-east-1 y la secundaria us-east-1 implican transferencias internacionales sujetas a aprobación del CLIENTE. AWS actúa como encargado bajo contrato con cláusulas tipo; el CLIENTE administra KMS y la geolocalización de personas se excluye de la réplica secundaria, conforme se desarrolla en 4.3.2 (Bases Técnicas del caso, cap. 15, pp. 26–30; Bases Técnicas Transversales, cap. 11, pp. 23–24; RT-11.08–11.10 y RT-16.09).

##### Amenazas, controles y evidencia

El modelado STRIDE toma cada módulo y cada integración externa como unidad de revisión, identifica su límite de confianza, abuso posible, mitigación, responsable y prueba. Para M3, el abuso es reutilizar una credencial o reenviar un pedido: se comprueban enrolamiento, vigencia e idempotencia. Para M5, la elevación indebida de privilegios no debe liberar una carga bloqueada por M9: se prueba la separación de autorizaciones. Para M11 y la ACL, un mensaje EDI repetido o manipulado se rechaza o aísla sin escribir dos veces en el ERP. El Anexo 4-Q registra las amenazas por módulo y frontera; el Anexo 4-R vincula controles ISO/IEC 27001/27002 con responsable y prueba. Son especificaciones de aceptación, no resultados de ensayos ni certificación (ISO, 2022b, 2022c) (RT-11.02 y RT-11.05; Bases Técnicas Transversales, cap. 11, p. 23).

Cada decisión de acceso y cada acción crítica conserva sujeto, empresa si aplica, recurso, operación, resultado, hora, identificador de transacción y regla aplicada. Los eventos de seguridad se envían a una bitácora inalterable y al SIEM; durante un corte se conservan localmente y se remiten con el mismo identificador al reconectar. Las reglas de detección incluyen acceso privilegiado fuera de turno, intentos reiterados de uso de una credencial de conductor revocada, consulta masiva de datos comerciales, alteración de evidencia de temperatura y desvío anómalo de mensajes EDI. Los registros técnicos en CloudWatch se conservan 12 meses en línea y 24 meses adicionales en archivo; los registros de seguridad y auditoría se conservan 7 años bajo Object Lock. La retención de documentos tributarios y POD se gobierna separadamente por su dominio de datos. La plataforma que opera estos controles se describe en 4.2, y la dotación del SOC, en el Anexo 4-W (RT-11.14–11.19; Bases Técnicas Transversales, cap. 11, p. 24).

La aceptación de esta vista requiere una prueba de acceso denegado por rol y atributo, una de cifrado de campo con lectura administrativa sin texto claro, una de continuidad y relevo offline, una de revocación al reconectar y una de correlación de un evento de negocio con su alerta de seguridad. Se distinguen dos objetivos de disponibilidad: 99,95 % mensual para la infraestructura del recinto y al menos 99,9 % mensual para el servicio de negocio de extremo a extremo. Ninguno elimina la exigencia de continuidad durante el despacho de 05:30 a 07:00.

#### 4.1.3.8 Capa de observabilidad transversal (Capa 8)

La Figura [13](LAFROX-Subdocumento4.md#fig:arql-capa-8) presenta las responsabilidades de esta capa.

**Figura 13 — Observabilidad: correlación de nube y sitios**

![Observabilidad: correlación de nube y sitios](https://raw.githubusercontent.com/PatricioH315/LafroX/d397c30ff8ad232ec4e3ea02caf5f3cb6800a547/04/figuras/logica/capas_recortes/ARQL-28_Recorte_Observabilidad.png)

<a id="fig:arql-capa-8"></a>
 La correlación permite seguir una operación entre APIs, módulos y consumidores. Durante el corte, el sitio conserva telemetría y mantiene sus alarmas; CloudWatch reúne registros, métricas y trazas para los tableros y la atención de incidentes.

La observabilidad debe ayudar al equipo a responder preguntas operativas: qué pedido quedó sin confirmar, dónde se interrumpió una integración y qué entregas pueden verse afectadas. Para ello reúne métricas, registros y trazas de nube y sitios locales en una misma plataforma (RT-03.16; Bases Técnicas Transversales, cap. 3, p. 9; Bases Administrativas, art. 16.4, p. 12).

La instrumentación utiliza OpenTelemetry para PHP/Laravel y las aplicaciones Kotlin, junto con los registros y métricas disponibles de API Gateway, RabbitMQ, SQS y Greengrass. El identificador `transaction_id` acompaña las solicitudes y los mensajes; los trabajadores extraen el contexto de traza del sobre de evento para correlacionar la operación de negocio, incluidos los procesos asíncronos.

En on-premise, los colectores ADOT, con buffer en disco de 24 horas, recolectan la telemetría local y la exportan a la plataforma única en Amazon CloudWatch: Logs conserva los registros técnicos 12 meses en línea y 24 meses en archivo; Metrics conserva las métricas 13 meses; las trazas y los tableros operacionales también se alojan en CloudWatch (ADR-14).

Los tableros se estructuran en tres niveles: operacional (para el equipo de TI y SRE), gerencial (para la gerencia y jefes) y del mandante (para Puelche, solo lectura con auditoría de consultas, conforme a RT-14.02; Bases Técnicas Transversales, cap. 14, p. 27). Las alertas se formulan por síntomas de negocio, no por causas técnicas, con ventanas de evaluación para evitar falsos positivos y escalamiento por criticidad.

Durante un corte de enlace, el sitio no depende de los tableros centralizados para despachar. Las alarmas locales continúan y los colectores retienen la telemetría para enviarla al restablecer la conexión. La capacidad del buffer de 24 horas debe comprobarse con la carga de diseño; no se presume conservación ilimitada. La retención de métricas, registros técnicos y trazas no sustituye la política de auditoría de negocio exigida por RT-16.10.

### 4.1.4 Módulos funcionales y límites de contexto

<a id="sec:modulos-funcionales"></a>

Los doce módulos M1–M12 separan decisiones de negocio y conservan su trazabilidad a los requerimientos. El Anexo 4-D identifica responsabilidad, intercambio, actor principal y etapa. Un actor puede participar en varios módulos sin convertirse en propietario de sus datos. El detalle de los módulos críticos se desarrolla inmediatamente después.

Cada módulo tiene un dueño de negocio y una vía explícita para colaborar con los demás.

La correspondencia con los identificadores físicos se detalla en la tabla de correspondencia del apartado 4.2.2 y en el Formulario T-11: N-04 ejecuta los módulos M1–M12 en nube; A-01 ejecuta M1, M2 y M5 como WMS local, además de la recepción física de retornos de M8, sobre A-02 (base transaccional), con A-03 (RabbitMQ), A-04 (ACL del ERP) y A-05 (identidad local) como apoyos. M9 utiliza B-02 (gateways de frío) y N-08 (ingesta IoT); M10 utiliza N-10 (analítica). N-09 proporciona SQS FIFO y SNS a los flujos asíncronos; N-01 a N-03 publican los portales y N-13 gestiona los terminales de bodega y terreno. Estos códigos identifican componentes de despliegue, no módulos de negocio adicionales.

El reparto evita que M6 emita DTE o que M10 escriba pedidos. M1 y M5 entregan datos al ERP únicamente por la capa anticorrupción. M11 entra en la Etapa 2 sin cambiar el dueño de la reserva de stock, que sigue siendo M2. Los límites y dependencias se precisan en el mapa siguiente.

El Anexo 4-E hace visible el paso del requerimiento al componente y a la capa que lo realiza. Es una síntesis de los dominios, no una sustitución del catálogo requisito por requisito del Formulario T-12; allí se debe conservar también origen, etapa, prueba y criterio de aceptación de cada RF y RNF.

La trazabilidad transversal se prueba sobre esos mismos recorridos: RT-03.10 para 24 horas en sitio y 14 horas en terreno, RT-03.12 para reconciliación determinista y RT-03.13 para funciones no disponibles sin conexión y plazos de sincronización del caso en M1, M3, M5 y M6; RT-02.06 mediante UUID y resultado persistente en M2/M3/M6; RT-02.13 mediante el modelo de dominio; y RT-11/12 mediante autorización y auditoría en cada cruce. El entorno de prueba y el caso de aceptación deben reproducir la falla, no limitarse a una marca de cumplimiento.

M3 conserva el precio acordado por el preventista al tomar el pedido y la versión de condiciones comerciales aplicada, conforme a RNG-08 del Subdocumento 3. Un cambio posterior de la lista de precios no altera ese importe. Una propuesta offline fuera de las condiciones autorizadas queda en excepción y el precio no se sustituye en silencio. La condición aplicada viaja en el pedido y en el intercambio con el ERP, para comprobar que la facturación respeta el importe acordado.

La promesa de RNG-15 es de 24 horas para pedidos urbanos ingresados antes de las 14:00 y de 48 horas para clientes rurales, periféricos o abastecidos por cross-docking. M3 conserva la fecha de ingreso, la regla y la ventana prometida, y M4 y M6 usan esa misma ventana. Ante un local cerrado, M6 registra el intento, la causal y la evidencia, y reagenda a la siguiente ventana disponible. Si la ausencia persiste, la mercadería retorna al CD con trazabilidad y nunca se entrega a terceros (RNG-05).

M10 entrega OTIF e indicadores operacionales en la Etapa 1 y el costo de servir en la Etapa 2. M12 captura y consulta la telemetría operacional desde la Etapa 1, y su uso para costo de servir se agrega en la Etapa 2. M11 habilita los portales y el canal moderno en la Etapa 2, y M3 sigue siendo dueño del pedido en todos los canales. En la Etapa 1, despacho registra la asignación nominada conductor–vehículo–turno mediante su función operacional, sin depender del portal de transportistas.

#### 4.1.4.1 Mapa de límites de contexto

<a id="subsec:limites-contexto"></a>

El modelo de dominios se organiza mediante límites de contexto explícitos. El Anexo 4-F indica qué módulo entrega información, qué módulo la recibe y dónde se traduce un modelo ajeno. El uso de un vocabulario publicado o de una capa anticorrupción evita que un cambio en el ERP o en una cadena comercial reescriba las reglas de stock y pedido.

El mapa expone dependencias que deben permanecer bajo contratos versionados.

El mapa asigna a cada relación un dueño de contrato y una superficie de intercambio. El catálogo de interfaces (§ [4.1.6](LAFROX-Subdocumento4.md#sec:catalogo-interfaces)) añade la versión y la conducta ante falla; una relación del Anexo 4-F no equivale por sí sola a un contrato ejecutable.

#### 4.1.4.2 Módulo de calidad y trazabilidad (M9)

El módulo de trazabilidad resuelve el problema central que motivó la licitación: la incapacidad de responder en tiempo real ante un retiro sanitario. En marzo de 2026, un retiro preventivo de queso fresco tomó 9 días en resolverse de forma inexacta, con la apertura de un sumario sanitario y la suspensión como distribuidor autorizado por un proveedor clave por seis meses.

La unidad de trazabilidad sanitaria es el lote del proveedor, identificado por el producto (GTIN) y el número de lote. El vencimiento y los registros de temperatura se conservan como atributos asociados; FEFO es la regla de rotación por vencimiento, no parte del identificador. Cada movimiento vincula el lote con la unidad logística identificada mediante SSCC. Esta organización permite seguir el producto aunque cambie de caja o pallet. Como el 41% de las recepciones carece de lote registrado, la captura en recepción es obligatoria para sostener la trazabilidad (RF-01).

La trazabilidad forward/backward se implementa evento a evento conforme al estándar GS1 EPCIS, permitiendo al sistema responder en menos de 2 horas ante un retiro sanitario (Bases Técnicas del caso, cap. 18, p. 34), con identificación precisa de los lotes y puntos de entrega afectados. Los registros de temperatura se capturan de forma continua en 21 puntos de temperatura en cámaras (15 en Talca y 6 en Concepción) y 28 termógrafos: 18 en camiones propios y 10 en camiones refrigerados de transportistas. Una excursión menor y transitoria genera una advertencia. Una excursión crítica y sostenida, según el umbral y la duración parametrizados por producto, genera retención preventiva automática en M2 y M5, también sin enlace (RNG-04 y RF-09.05/06/07 del Subdocumento 3). Mientras Calidad no apruebe los parámetros de un tipo de producto, toda lectura fuera del rango de almacenamiento de la ficha del SKU se trata como crítica. El sistema registra la versión de la regla, el umbral, la duración, el sensor y el lote. La jefatura de Calidad evalúa la excursión y es la única que autoriza una liberación trazada o dispone rechazo. El conductor no puede levantar el bloqueo. M9 integra los sensores de cámara mediante los tres gateways con Greengrass (Capa 2), los termógrafos mediante el terminal del conductor, inventario (M2), preparación (M5) y observabilidad (Capa 8), con evidencia exportable de la decisión.

#### 4.1.4.3 Módulo de inventario (M2)

El módulo de inventario permite saber qué stock existe, dónde está y qué parte puede comprometerse. Mantiene la operación distribuida entre Talca, Concepción y los tres cross-docks; la casa matriz consulta la información consolidada. Sus capacidades son las siguientes:

- **Stock por sitio (RF-02.02; RT-02.12; Bases Técnicas Transversales, cap. 2, p. 7).** Cada instalación operativa informa sus movimientos al consolidado. Con conexión se consulta disponibilidad actual; sin ella se muestra la copia descargada, identificada como información con fecha de actualización. La parametrización admite nuevos sitios sin convertir a la casa matriz en una bodega ni asignarle stock operativo por defecto.

- **Slotting y conteo ciego.** Asignación de ubicaciones por criterio documentado de rotación, peso y compatibilidad, con conteo cíclico de inventario mediado por terminales HHT con escáner GS1, reduciendo la discrepancia actual del 2,3% del valor contado a menos del 1%.

- **FEFO (First Expired, First Out).** La preparación y el despacho respetan el principio de primer vencimiento, con secuenciación térmica para productos refrigerados y congelados.

- **Stock disponible.** Con conexión se consulta la disponibilidad mediante APIs. Sin conexión se utiliza la copia autorizada descargada al inicio del turno y almacenada en SQLite/Room. La reserva comercial se confirma en M2 central después del acuse durable de la retención en M2 del sitio. Los pedidos capturados sin señal permanecen a la espera de validación. Los conflictos se resuelven con reglas documentadas de asignación y prioridad, no mediante la sola comparación de marcas de tiempo.

#### 4.1.4.4 Módulo de preventa móvil (M3)

Para los 62 preventistas, tomar un pedido debe seguir siendo posible aun cuando la ruta no tenga cobertura. El módulo reemplaza una aplicación que no consulta stock ni crédito y presenta caídas y duplicación de pedidos. La nueva interacción distingue con claridad lo registrado en el dispositivo de lo confirmado por el servidor:

- **Toma de pedido offline (RF-03.02).** El preventista toma el pedido sin señal de red. La aplicación mantiene una foto local de datos de lectura (stock, crédito del cliente, precios vigentes, promociones) que se descarga al inicio del turno cuando hay conectividad.

- **Identificador único y deduplicación (RF-03.16).** Cada evento recibe un UUID que se conserva en todos sus reintentos. El servicio de negocio registra su procesamiento y evita ejecutar dos veces la misma operación.

- **Validación de stock y crédito.** La validación definitiva ocurre en la sincronización con la regla de negocio del servidor (reserva de stock, RF-03.03; crédito del cliente, RF-03.08/09). Sin conexión, el pedido queda como a la espera de validación y se resuelve en la sincronización posterior.

- **Sincronización diferida.** Al recuperar cobertura, el dispositivo envía las escrituras acumuladas por API Gateway. El Gateway aplica los controles de entrada; el servicio de negocio valida, deduplica, procesa y confirma cada evento. El dispositivo conserva los eventos que aún no tienen confirmación.

- **Pedido de autoatención (RT-16.30 y RT-17.01 del caso; Bases Técnicas del caso, cap. 15, p. 27).** M3 recibe también el pedido que el cliente arma en el Portal de Clientes, incluido el armado sin señal en su modo instalable, con la misma deduplicación por UUID y la misma validación de stock y crédito. M3 es el único dueño del pedido en sus tres canales: preventista, autoatención y canal moderno (M11).

La prueba de aceptación de terreno considera un turno de 14 horas sin cobertura. El caso exige que un dispositivo de reparto sincronice esa jornada en un máximo de 10 minutos; para el CD, fija hasta 2 horas tras un corte de 24 horas (RT-03.13 del caso; Bases Técnicas del caso, cap. 15, p. 26). Estos límites se verifican con la volumetría correspondiente y reconciliación determinista (RT-03.12; Bases Técnicas Transversales, cap. 3, p. 9), sin extender automáticamente el umbral del repartidor a cualquier carga de preventa.

##### Reserva comercial y retención física por sitio

M2 central es dueño de la reserva comercial. M2 de cada sitio conserva la existencia, los movimientos y la retención física. M3 confirma un pedido solo después de que M2 central persiste el acuse de una retención local durable. El consolidado y la réplica DMS son proyecciones de lectura y no autorizan una reserva. Las solicitudes se ordenan por recepción central con correlativo de desempate (RNG-01 del Subdocumento 3). El pedido offline entra en ese orden al sincronizar.

M2 central persiste la solicitud pendiente con UUID, correlación, sitio, época de autoridad, lote, ubicación, cantidad y versión. El shipper del sitio lee, por conexión saliente, una cola FIFO de coordinación propia y entrega la solicitud al broker local. M2 local bloquea el agregado, valida la existencia y el estado de Calidad, y persiste la retención, la auditoría y el outbox. INT-03/04 devuelve el resultado, y M2 central persiste el acuse antes de que M3 confirme. Un reenvío recupera el resultado de la misma clave sin descontar otra vez.

La cancelación o la expiración central inicia una liberación pendiente. El stock sigue retenido hasta el acuse durable del sitio. Una retención ya consumida por la preparación no vuelve a quedar disponible. Si se pierde el acuse, la operación queda en estado incierto y la retención se mantiene. Durante un aislamiento no se confirma una reserva remota nueva, y el sitio continúa sus movimientos y misiones. Un cambio de autoridad exige conciliación y la revocación de la época anterior, y no se hace durante una partición.

La coordinación usa colas e identidades por sitio, separadas de las del ERP, de la reconciliación de eventos y de los trabajos de Laravel. La nube publica las solicitudes y cada shipper inicia su conexión. La única conexión iniciada desde la nube hacia un sitio sigue siendo DMS de Talca. El Anexo 4-G detalla este contrato dentro de INT-03/04, el Anexo 4-I cuantifica sus mensajes y AL-STOCK-01 del Anexo 4-V lo verifica. Su emplazamiento físico se describe en 4.2.

#### 4.1.4.5 Módulo de planificación de rutas (M4)

El módulo de planificación de rutas automatiza un proceso que actualmente depende de una sola persona (21 años de conocimiento concentrado, con retiro programado en 2 años) que administra una planilla de 11 hojas. El módulo implementa:

- **Secuenciación automática.** Optimización determinista de rutas con capacidad y ventanas de tiempo (VRP), con objetivo de ejecución inferior a 20 minutos (Bases Técnicas del caso, cap. 18, p. 34). El planificador puede conocer las restricciones utilizadas y revisar el resultado.

- **Ventanas horarias y capacidad.** Considera capacidad de vehículo, ventanas de entrega del cliente y cadena de frío.

- **Integración con GIS.** Consulta de direcciones, cálculo de ETA y geocercas por API externa, con caché de mapas por zona en dispositivos para degradación a ruta offline con secuencia cargada.

- **Costo de entrega.** Alimenta el cálculo del costo de servir por cliente, uno de los ejes de evaluación del caso.

La propuesta automática no convierte las excepciones del planificador en reglas opacas: M4 conserva restricción, motivo de ajuste y autor de la ruta aprobada para transferir conocimiento y comprobar el criterio de aceptación.

#### 4.1.4.6 Módulo de rendición y cobro (M7)

El módulo de rendición y cobro permite investigar las causas de las diferencias de rendición que hoy quedan sin explicación. Implementa:

- **Rendición digital individual (RF-07.02).** Cada conductor rinde sus cobros del turno de forma digital, con causales de descuadre clasificadas y trazables.

- **Cobranza en ruta (RF-07.05 y RF-07.09).** El conductor registra el cobro y conserva su evidencia para la rendición. En pagos con POS móvil, la captura local de una operación no se presenta como autorización bancaria. El tratamiento sin cobertura depende de las capacidades y condiciones acordadas con la pasarela; se concilia al reconectar sin generar cargos duplicados.

- **Interfaz con ERP (RF-07.02 e INT-06).** La rendición aprobada se publica en la cola FIFO de solicitudes al ERP; dos procesos `erp-sync` en VM-04 de Talca consumen esa cola por conexión saliente y la cola RabbitMQ local, y entregan a la **capa anticorrupción (ACL)** de la misma VM; la ACL integra con el ERP. Nunca hay escritura directa al ERP. El ERP permanece como única fuente de verdad tributaria y único emisor de DTE.

- **Costo de servir (RF-11).** El módulo alimenta el tablero de BI con el costo real por entrega, incluyendo kilometraje real (telemetría M12), tiempo de servicio y deducciones por devoluciones.

#### 4.1.4.7 Módulo de analítica y costo de servir (M10)

El módulo de inteligencia de negocio consolida la información operativa en tableros gerenciales de autoservicio (RT-05.27; Bases Técnicas Transversales, cap. 5, p. 13) con modelo semántico en el mismo lenguaje del negocio: OTIF, fill rate, costo por entrega, ocupación de flota y segmentación por canal/cliente.

Los tableros se alimentan del almacén analítico (Redshift Serverless) con latencias comprometidas: operación del día ≤ 5 minutos, cierre comercial ≤ 2 horas, gestión ≤ 4 horas (RT-05.29; Bases Técnicas Transversales, cap. 5, p. 13). El modelo dimensional se estructura en hechos (ventas, entregas, stock, costo de servir) y dimensiones (cliente, SKU, tiempo, ruta, canal), con drill-down hasta línea de pedido y lote para trazabilidad sanitaria completa.

La información es de solo lectura para la analítica, sin acceder al transaccional en vivo, conforme al principio de separación transaccional/analítico. Los informes se programan (diarios, semanales, mensuales) y se exportan de forma asíncrona con firma y checksum (RT-05.28; Bases Técnicas Transversales, cap. 5, p. 13).

El módulo prioriza la calidad de la captura y la disponibilidad de indicadores verificables, dado que el caso informa un 41 % de recepciones sin lote registrado.

Comercial y Finanzas consultan indicadores sobre el mismo modelo semántico, pero solo Tesorería, del área de Finanzas, aprueba las diferencias de rendición; M10 no recibe permiso para modificar cobros.

#### 4.1.4.8 Recepción, preparación, reparto y servicios asociados

**M1 Recepción** compara lo recibido con la orden de compra, identifica GTIN, lote, vencimiento y SSCC, y registra cuarentena cuando falta evidencia o hay una diferencia. Publica `RecepcionConfirmada` para que M2 ubique el stock; no lo reserva para venta. La información del ERP entra y sale exclusivamente por la capa anticorrupción.

El proveedor consulta el estado de su orden y de la recepción; no accede a las reglas internas de inventario ni confirma unilateralmente un lote.

**M5 Preparación** toma pedidos confirmados y ubicaciones de M2, aplica FEFO y genera misiones verificables con lectura GS1. Conserva localmente cada lectura y la causal de faltante. Una carga no se libera por el mero hecho de estar preparada: la guía se solicita al ERP por `erp-sync` y la ACL al cerrar la carga nocturna. Un cambio de carga invalida la guía, exige una nueva y mantiene bloqueada la salida hasta disponer del documento válido.

El preparador confirma cada lectura en el servicio local; la pérdida del enlace externo no borra la misión ni convierte una carga preparada en una salida autorizada.

**M6 Reparto y entrega** recibe de M4 la ruta y de M5 la carga liberada. El conductor registra receptor, cantidad recibida, rechazos y POD en el dispositivo aun sin señal. M6 no liquida cobros ni emite documentos tributarios; publica el resultado para M7 y M8 y mantiene visible el estado de sincronización por confirmar.

El conductor propio y el externo utilizan el mismo contrato de entrega con identidades personales distintas. La evidencia queda ligada al turno y al receptor, sin exigir que el almacén instale una aplicación.

**M8 Devoluciones y envases** separa la mercadería que regresa de los activos retornables. Cada devolución conserva cantidad, lote, causal y vínculo con la entrega; el ajuste tributario se solicita al ERP por la ACL. Los canastillos y pallets se controlan por saldo de cliente y movimientos firmados, sujetos a conciliación en la rendición.

**M11 Canal moderno** recibe pedidos mediante contratos EDI configurados por cadena, traduce códigos a un vocabulario común y envía el pedido normalizado a M3. Las diferencias de formato y equivalencias van a una bandeja de excepciones; M11 no se convierte en un segundo dueño del pedido ni del inventario.

La cadena intercambia pedidos por el hub EDI; desde la Etapa 2, el representante del transportista consulta sus rutas y confirma conductor y vehículo en su portal. Ninguno de esos canales reemplaza el registro personal del conductor que ejecuta M6.

**M12 Telemetría** consume la fuente de posicionamiento existente de los vehículos propios, compara ruta planificada con recorrido y entrega kilómetros a M10 para costo de servir. No incorpora cámaras de cabina ni usa la posición para controlar la jornada laboral. Su falla degrada la visibilidad de ruta, no la captura de entregas de M6.

### 4.1.5 Modelo de datos conceptual

El modelo de datos de la solución se fundamenta en un conjunto de entidades de negocio canónicas, sus relaciones y eventos, conforme a RT-02.13. Este modelo alimenta la matriz de trazabilidad que exige el numeral 17.1 de las Bases Técnicas del caso (cap. 17, p. 31), entregada en el Formulario T-12, y los contratos de integración (OpenAPI 3.1 y AsyncAPI 2.6 por módulo).

Las entidades principales son:

- **Cliente.** Con RUT, razón social, canal (tradicional, food service, cadenas), crédito, georreferencia y estado de bloqueo. Eventos: creación, actualización y cambio de bloqueo.

- **Pedido.** Identificador UUID, preventista, cliente, líneas de detalle (SKU, cantidad, precio) y ciclo de vida (tomado → confirmado → preparado → despachado → entregado → rendido). Eventos: toma, confirmación, asignación de línea, despacho y evidencia de entrega.

- **SKU / Producto.** Con codificación GTIN/GS1, unidad, clasificación de temperatura, rangos térmicos (RF-09.01) y vida útil.

- **Lote.** Unidad de trazabilidad sanitaria identificada por GTIN y número de lote del proveedor, con vencimiento como atributo asociado. Cada movimiento interno la vincula con su unidad logística SSCC. Eventos: recepción, bloqueo, inicio de retiro sanitario y enlace con unidad logística.

- **Misión de preparación.** HHT, oleada, ubicación, unidades y ciclo de vida (descargada → ejecutada → cerrada).

- **Ruta / viaje.** Planificador, vehículo, conductor, ventanas, secuencia de entregas y geocercas.

- **Entrega.** Pedido, viaje, prueba de entrega (POD: firma, QR, fotografía), documentos DTE y efectivo. Eventos: evidencia, reintento y aprobación de rendición.

- **Documento tributario.** Factura, boleta, guía de despacho, folio del SII y acuse.

- **Envase retornable.** Canastillo o pallet, cliente, saldo y pérdida estimada del 14% anual (Decisión 16.1 N° 10). Control por cuenta corriente por cliente, no por unidad identificada.

- **Sensor / registro térmico.** Dispositivo, lote o posición, temperatura y excursión térmica.

Los eventos usan verbos en pasado y son la base de los esquemas AsyncAPI. Toda escritura offline es idempotente por UUID (RT-02.06; Bases Técnicas Transversales, cap. 2, p. 7).

El almacenamiento se distribuye en quince dominios lógicos: BD_INVENTARIO, BD_PREVENTA, BD_RUTAS (PostGIS), BD_PREPARACION, BD_REPARTO, BD_COBRANZA_FINANZAS, BD_MAESTROS_CONF, BD_GOBIERNO_ACCESO, BD_CALIDAD_TRAZABILIDAD, BD_TELEMETRIA, BD_EDI_CANALMODERNO, BD_BI_GERENCIA, BD_MAILS_NOTIF, REDIS_SESIONES_CACHE y S3_DOCS. El dominio de telemetría conserva la ingesta raw en DynamoDB y su serie consolidada en S3 Parquet y Redshift, procesada con Glue. Esta separación incluye bases transaccionales, almacenes analíticos, caché y objetos; no representa quince servidores físicos ni quince motores de base de datos independientes.

La Figura [14](LAFROX-Subdocumento4.md#fig:arql-18) dibuja las relaciones mínimas necesarias para responder dos preguntas del caso: de qué lote provino una unidad entregada y a qué clientes llegó un lote que debe retirarse.

 **Figura 14 — Modelo conceptual del pedido, el lote y la entrega**

![Modelo conceptual del pedido, el lote y la entrega](https://raw.githubusercontent.com/PatricioH315/LafroX/d397c30ff8ad232ec4e3ea02caf5f3cb6800a547/04/figuras/logica/ARQL-18_Dominio_trazabilidad.png)

<a id="fig:arql-18"></a>

Fuente: elaboración propia de LafroX.

La línea de pedido se asigna a un lote identificado por GTIN y lote del proveedor; los movimientos con SSCC conservan la cadena de custodia hasta la entrega. La entrega vincula la evidencia de recepción y el folio de la guía que el ERP emitió antes del traslado. Un pedido aún puede no tener entrega, y una entrega puede registrar más de una evidencia o un rechazo parcial: esas cardinalidades y estados conservan el identificador de origen.

### 4.1.6 Catálogo de interfaces

<a id="sec:catalogo-interfaces"></a>

El catálogo identifica quince integraciones por número estable, dueño y superficie contractual. Los anexos 4-G y 4-H reúnen para cada una el modo, volumen esperado, ventana requerida de la contraparte y conducta ante lentitud o error (RT-05.21; Bases Técnicas Transversales, cap. 5, p. 13). Se distingue una ventana requerida por el diseño de un SLA efectivamente acordado con un tercero. El contrato ejecutable OpenAPI o AsyncAPI debe fijar operación o evento, esquema, versión, autenticación, errores y plazo de retirada. La publicación de una ruta genérica por sí sola no equivale a entregar ese contrato.

#### 4.1.6.1 Integraciones internas

Las ocho interfaces internas intercambian pedidos, entregas, inventario, identidad y telemetría entre dispositivos, sitios y nube. El Anexo 4-G permite reconocer qué módulo acepta cada mensaje y cómo se conserva cuando falla el enlace.

Las interfaces críticas conservan datos durante el corte y confirman cada operación al reconectar.

INT-01 y INT-02 conservan el UUID de cada operación hasta obtener acuse durable; INT-03 y INT-04 ordenan eventos por sitio o agregado. INT-12 replica únicamente el WMS de Talca a un esquema de lectura separado de las tablas escritas por los consumidores de eventos. La extracción continua por fibra, LTE y satélite sostiene un desfase menor de 15 minutos; AL-DR-01 del Anexo 4-M verifica la pérdida del sitio y 4.3.2 justifica el límite residual.

#### 4.1.6.2 Integraciones externas

Las siete interfaces con terceros se encapsulan para que un cambio de proveedor no altere doce módulos a la vez. El Anexo 4-H separa el tercero, el dueño interno del contrato y la conducta ante falla.

La ACL aísla el ERP; ninguna falla de tercero convierte un estado sin confirmar en aprobado.

La integración tributaria INT-07 pasa por el ERP, único emisor de DTE; M5 no llama al SII. La falla de INT-09 impide afirmar que un cargo quedó aprobado. Para INT-08 se preservan el mensaje original, su equivalencia y la respuesta enviada a cada cadena.

**Volumen de mensajes por integración.** Los anexos 4-G y 4-H declaran las quince interfaces; el Anexo 4-I resume órdenes de magnitud y cálculos. No se usa la suma de eventos, consultas, muestras y reenvíos como número de transacciones únicas: una misma operación cruza varias interfaces. La prueba mide además tamaño de mensajes, objetos y WAL. La telemetría se ingiere y consolida por su flujo específico sin competir con las escrituras críticas de despacho (ADR-04).

### 4.1.7 Detalle de tecnologías seleccionadas

A continuación se resume la tecnología de cada capa y su justificación principal:

- **Backend (12 módulos).** Laravel 13 sobre PHP 8.5, con Composer y `composer.lock`, organizado en contextos M1–M12. PostgreSQL/PostGIS conserva los datos geográficos; M4 usa repositorios espaciales con SQL parametrizado vía PDO/Query Builder y pruebas de consultas. Laravel 13 requiere PHP 8.3 o superior y admite PHP 8.5 (Laravel, 2026); ambos componentes se actualizarán a versiones con soporte durante los 56 meses.

- **Frontend web.** Angular 22 con Tailwind CSS y TypeScript 6.0 compatible con su matriz oficial. La integración con Keycloak se implementa mediante OIDC y se mantiene junto con las dependencias del cliente. Las versiones deben actualizarse durante el contrato conforme a sus ciclos de soporte.

- **Apps de campo (preventa y reparto).** Kotlin Android nativo. Nativo del parque Zebra/Android, escáner GS1 vía Zebra DataWedge, SQLite/Room offline, acceso nativo a GPS, POS y térmica.

- **Borde y continuidad del acceso (Capa 2).** CloudFront, AWS WAF, AWS Shield Advanced y ALB en nube, con control de acceso local. En los CD, Starlink fijo permanece encendido con IPsec establecido y BGP de menor preferencia tras fibra y LTE; en los cross-docking es el camino principal, con LTE de dos proveedores como respaldo y conmutación automática en menos de 30 segundos (ADR-02), sin sustituir la autonomía del servicio local.

- **Puerta de enlace de servicios (Capa 3).** Amazon API Gateway para publicar las APIs y aplicar controles de entrada. La configuración debe cubrir la validación de identidad de Keycloak, las cuotas y los límites de solicitudes, conforme a la modalidad de API seleccionada y al flujo descrito en la capa de puerta de enlace de este apartado.

- **Base de datos transaccional on-premise.** PostgreSQL + PostGIS por sitio con el mismo perfil `wms_only`; cada sitio es autoridad de sus movimientos y N-04/N-05 consolida stock y reservas en nube.

- **Base de datos nube (OLTP y recuperación).** Amazon Aurora PostgreSQL, con despliegue Multi-AZ y una ventana propuesta de recuperación a un punto en el tiempo (PITR) de 35 días. Los tiempos de conmutación y restauración se verifican mediante pruebas frente a los objetivos RTO/RPO establecidos.

- **Ingesta IoT / frío.** Amazon DynamoDB e IoT Core reciben las lecturas; Greengrass corre en tres gateways Moxa UC-8200 o equivalentes: dos en Talca, que leen ambas cámaras por Modbus TCP para evitar un punto único de falla, y uno en Concepción; leen sensores por Modbus, bloquean el despacho ante una excursión crítica y sostenida en menos de 5 segundos y conservan 24 horas sin enlace. Los termógrafos de los camiones registran toda la ruta en memoria interna y alertan por BLE al terminal, que reenvía el aviso al recuperar cobertura y descarga el registro completo al volver. Escrituras serverless con TTL nativo (raw 30 días).

- **Serie consolidada (OLAP).** S3 Parquet + AWS Glue + Redshift Serverless. OLAP por diseño: DynamoDB raw → Glue → S3 Parquet → Redshift, sin motor de series adicional.

- **Caché y datos de turno.** Redis acelera las lecturas centrales; no se exige Redis en cada sitio. Las APIs entregan una copia cifrada para SQLite/Room y conservan por separado la cola de escrituras sin confirmar. La identidad usa credenciales de 8 horas en bodega y 14 horas en terreno; su caché local de solo lectura tiene TTL de 24 horas en VM-05, VM-C03 y cada E-01, junto al verificador local de relevos (ADR-06).

- **Mensajería asíncrona (Capa 5).** RabbitMQ en on-premise mediante adaptador AMQP `php-amqplib`; SQS FIFO con sobre JSON y consumidor PHP para reconciliación, colas SQS separadas para trabajos Laravel, y SNS para difusión y alertas en nube. Un único planificador Laravel programa las tareas periódicas. Dos procesos `erp-sync` en VM-04 consumen RabbitMQ local y, por salida, la cola FIFO de solicitudes al ERP; ERP integrado exclusivamente vía ACL; Hub EDI GS1 centralizado en nube (EANCOM, GS1 XML, EPCIS), AS2 como transporte.

- **Analítica / BI.** S3 Data Lake, Redshift Serverless y Glue ETL. Consultas históricas sin degradar el procesamiento transaccional.

- **Objetos / documentos.** Amazon S3 con Intelligent-Tiering y Object Lock.

- **IAM / Identidad (Capa 7).** Keycloak (OIDC, SAML, SSO, MFA) como IdP maestro en nube, con caché local de solo lectura de TTL 24 horas y verificador local con manifiesto firmado y PIN personal en VM-05, VM-C03 y cada E-01.

- **Gestión de secretos (Capa 7).** AWS Secrets Manager y SSM Parameter Store con rotación automática. Cuenta de emergencia fuera de banda, con doble autorización, registro de uso y rotación posterior de credenciales.

- **Observabilidad (Capa 8).** OpenTelemetry para PHP/Laravel y colectores ADOT on-premise con buffer en disco de 24 horas; plataforma única Amazon CloudWatch para logs (12 meses en línea + 24 en archivo), métricas (13 meses), trazas y tableros (ADR-14).

- **Gestión de dispositivos (RT-03.18; Bases Técnicas Transversales, cap. 3, p. 9).** Gestión centralizada mediante MDM (Android Enterprise / Zebra DNA, SaaS), con inventario, configuración, actualización de firmware y aplicaciones, bloqueo y borrado remoto del parque móvil.

- **Contenedores / orquestación.** Imagen PHP 8.5 con servidor HTTP/PHP-FPM para APIs y procesos PHP CLI separados para colas y programación. ECS Fargate aloja los perfiles centrales; Talca y Concepción ejecutan el perfil `wms_only` sobre máquinas virtuales Proxmox, y Docker Compose ejecuta el mismo perfil `wms_only` en los equipos E-01 de los cross-docking. El código y las migraciones de esquema proceden del mismo artefacto versionado.

- **Infraestructura como Código.** Terraform administra recursos mediante proveedores y estados separados por ambiente; Ansible configura hosts. CDK no administra los mismos recursos: cada activo tiene un único propietario de infraestructura como código.

- **CI/CD.** GitLab CI como orquestador + AWS CodeBuild para construcción hermética con procedencia SLSA 3; `composer audit`, PHPUnit, PHPStan/Larastan y Laravel Pint verifican dependencias, comportamiento, análisis estático y formato. `swagger-php` genera OpenAPI 3.1 desde atributos PHP; los esquemas AsyncAPI 2.6 se validan y publican en la misma puerta de calidad.

Los servicios AWS consumidos incluyen: CloudFront, AWS WAF, AWS Shield Advanced, ALB, Network Load Balancer, API Gateway, Verified Access, Aurora, ElastiCache, DynamoDB, S3, Redshift Serverless, ECS Fargate, Lambda (solo como autorizador), Route 53, Secrets Manager, Systems Manager, KMS, IAM, Organizations, IAM Identity Center, CloudWatch, Transit Gateway, NAT Gateway, VPC Endpoints, Site-to-Site VPN, SQS, SNS, AWS Backup, GuardDuty, Security Hub, Security Lake, Macie, Inspector, Config, Database Migration Service, Glue, QuickSight, Elastic Container Registry, CodeBuild, Control Tower, CloudTrail e IoT Core+Greengrass.

Laravel conserva una superficie de APIs, políticas y colas coherente para los doce módulos; Django también permitiría el monolito, pero mantener su runtime junto al nuevo obligaría a operar dos cadenas de dependencias y dos familias de trabajadores. La equivalencia se acepta por contratos y pruebas, no por parecido de bibliotecas. PostgreSQL/PostGIS se prefiere a MariaDB por la combinación de transacciones y consultas geográficas del dominio de rutas y sitios; la prueba cubre consultas espaciales y migración. Keycloak se prefiere a un proveedor de identidad exclusivamente en nube porque permite administrar personal propio y externo sin trasladar la autorización de negocio fuera de M1–M12; el relevo local requiere la prueba de 24 horas. API Gateway reduce administración frente a un gateway propio, sujeto a prueba de cuotas y costo bajo el pico. RabbitMQ local más SQS FIFO conserva el trabajo del sitio sin enlace; la deduplicación y el orden por partición se prueban en los consumidores. Angular se conserva por sus componentes y contratos TypeScript. Los costos, el emplazamiento y la redundancia se comprueban en 4.2 y en el registro ADR.

El núcleo utiliza tecnologías con alternativas de despliegue como Laravel, Angular, PostgreSQL, RabbitMQ y Keycloak. Eso facilita la portabilidad, pero no elimina la dependencia de los servicios administrados de AWS. La reversibilidad documenta contratos, exportación de datos y sustitución de adaptadores, junto con el esfuerzo de migración exigido por RT-03.07, que 4.2 acota por servicio.

El Anexo 4-P reúne versiones de referencia, soporte y criterios de actualización. Las versiones menores se fijan en archivos de bloqueo y SBOM y se promueven mediante pruebas de contrato; no se congela una versión sin soporte por los 56 meses. Laravel, PHP, PostgreSQL, Angular y RabbitMQ se revisan conforme a sus políticas oficiales (Laravel, 2026; PHP, 2026; PostgreSQL, 2026; Angular, 2026a, 2026b; RabbitMQ, 2026).

### 4.1.8 Implantación progresiva del backend Laravel

<a id="sec:transicion-laravel"></a>

La implantación conserva los identificadores M1–M12, sus dueños de datos, las rutas y versiones públicas, los eventos JSON, la identidad Keycloak y las reglas offline. El Anexo 4-P muestra cómo se implementan las capacidades del backend; PostgreSQL/PostGIS, RabbitMQ, SQS y los clientes mantienen sus contratos.

La implementación conserva rutas y contratos, repositorios PostgreSQL/PostGIS y eventos JSON. Sustituye el runtime por Laravel/PHP, separa consumidor de integración y trabajos internos, y prueba identidad, trazas y reversión antes de habilitar cada ola.

La implantación comienza por fijar contratos, dueños de datos y un extracto conciliado del WMS de 2013 en Talca. Concepción inicia sus saldos con un conteo físico, porque hoy controla su stock por planilla. El esquema PostgreSQL de destino lo define el modelo de datos de la solución, sin suponer el motor del sistema antiguo. Las migraciones Laravel son aditivas y compatibles con los lectores de la ola previa. M1/M2/M5 se ensayan primero en un sitio piloto y después se habilitan los demás sitios, módulos y trabajadores. El WMS antiguo deja de escribir en cuanto se habilita cada ola y se retira al cerrar la marcha blanca de Talca, con sus datos ya migrados y conciliados. En coexistencia, cada operación tiene un único escritor autorizado y no hay doble escritura de stock, cobros o DTE. Una reversión de software vuelve a la versión compatible anterior del nuevo servicio, con el mismo estado y el mismo escritor. No reactiva el WMS antiguo como escritor de stock. La contingencia manual del Subdocumento 3 conserva el picking y la evidencia, pero no permite ejecutar a mano los 96 despachos de 05:30 a 07:00. Por eso la decisión de revertir se toma antes de esa ventana, con guías válidas emitidas por el ERP, conciliación previa y autorización del CLIENTE. Todo evento entre versiones usa JSON versionado. Cada ola se acepta con pruebas de 14 horas en terreno, 24 horas por sitio con dos relevos, guía previa al despacho, 96 salidas en la ventana crítica y reconciliación sin pedidos duplicados.

### 4.1.9 Ambientes del ciclo de vida y promoción de componentes

Los cinco ambientes del RT-04.01 cumplen propósitos distintos. En **Desarrollo**, el equipo construye los módulos Laravel y las aplicaciones Kotlin, los contratos y las migraciones con datos sintéticos o anonimizados; las pruebas unitarias no necesitan conectarse al ERP real. En **QA**, se despliegan M1–M12, el verificador local y los adaptadores simulados para ensayar integración, regresión, idempotencia y fallas de enlace con datos controlados. En **Preproducción**, el mismo artefacto y las mismas versiones de contratos se ensayan con topología equivalente a producción y volumen representativo de septiembre; se prueban los 186 terminales de bodega, el relevo de turnos, la emisión de guía por el ERP y la reconciliación. Toda diferencia de escala o configuración se declara antes de aceptar el ensayo, conforme a RT-04.02.

En **Producción**, los módulos sirven datos reales con acceso restringido y auditado; los desarrolladores no corrigen transacciones directamente. El ambiente de **Recuperación ante desastres** conserva la versión compatible de los componentes y permite ensayar conmutación y retorno al menos dos veces al año, sin presumir que una réplica remota contiene eventos aún no enviados desde un sitio aislado. Los cinco deben estar operativos en el hito H3; su emplazamiento, capacidad y segregación de redes se demuestran en 4.2, no mediante el simple nombre del ambiente.

La promoción conserva la identidad del artefacto PHP, `composer.lock` y la versión de esquema desde QA hasta producción. La revisión por pares, pruebas de contrato OpenAPI/AsyncAPI, PHPUnit, PHPStan/Larastan, `composer audit`, análisis de secretos e imágenes bloquean un despliegue defectuoso (RT-04.03–04.05; Bases Técnicas Transversales, cap. 4, p. 10). Cada cambio registra requisito, commit, prueba, aprobación y despliegue; una migración incompatible con eventos sin confirmar se detiene o conserva un lector de la versión precedente. La recuperación ante desastres verifica además la lectura de datos y mensajes generados durante la contingencia antes del retorno al primario.

### 4.1.10 Patrones de diseño y continuidad

<a id="sec:continuidad-logica"></a>

La continuidad se articula con ISO 22301 para la gestión de continuidad del negocio y con ISO/IEC 27031 para la preparación de las TIC que la sostiene, conforme a RT-10.03 y RT-10.04 (ISO, 2019, 2025). En esta vista, su aplicación se concreta en las dependencias entre módulos, las funciones que pueden continuar desconectadas, los estados sin confirmar y las condiciones para volver a una operación consistente. Esta correspondencia de diseño no constituye una certificación ni acredita por sí sola el cumplimiento integral de las normas.

Ante pérdida de conectividad, M1, M2 y M5 conservan la operación local y M9 mantiene el bloqueo sanitario; M3 y M6 conservan la captura de terreno durante las autonomías definidas. Las confirmaciones que dependen de crédito, stock central o documentos del ERP permanecen explícitamente sin confirmar o bloqueadas según su regla. La continuidad protege la evidencia y la seguridad de la operación: no habilita una salida sin autorización tributaria ni permite levantar un bloqueo sanitario para recuperar velocidad.

La recuperación lógica exige restablecer identidad y autorización, disponer del estado transaccional y de los eventos sin confirmar, y habilitar después el procesamiento y la reconciliación. Cada consumidor confirma solo operaciones persistidas, deduplica los reenvíos y deriva los conflictos a su responsable. Antes de cerrar la contingencia se cotejan pedidos, reservas, lotes, entregas y rendiciones con sus identificadores de origen; las operaciones sin confirmar y las excepciones quedan visibles y auditadas. El orden concreto de restauración y la capacidad de respaldo se documentan en 4.2 y 4.3.

La evidencia de aceptación vincula cada servicio con su requisito, módulo, dependencia, objetivo de recuperación y prueba. Se ensayan pérdida de WAN durante 24 horas en el sitio, captura móvil durante 14 horas, indisponibilidad del ERP, relevo sin IdP y recuperación con mensajes repetidos. Se mide la conservación de operaciones confirmadas, el respeto de los bloqueos, la ausencia de duplicados y el tiempo hasta recuperar un estado conciliado. Una pérdida completa del sitio requiere una prueba de restauración distinta del corte WAN, contrastada con RTO ≤ 4 horas y RPO ≤ 15 minutos para los servicios críticos. La extracción continua por fibra, LTE y satélite sostiene el RPO, verificado con AL-DR-01; 4.3.2 justifica el límite residual.

La arquitectura aplica un conjunto de patrones de diseño que responden a las restricciones específicas de la operación de Puelche:

**Registro local y sincronización idempotente.** Cada escritura recibe un UUID declarado por el cliente que se conserva al reintentar. El evento permanece en la cola local hasta que el servicio de negocio confirma su procesamiento. Ese servicio deduplica dentro de una ventana documentada (RT-02.06; Bases Técnicas Transversales, cap. 2, p. 7) y resuelve conflictos con reglas deterministas y bitácora auditable (RT-03.12; Bases Técnicas Transversales, cap. 3, p. 9). La copia de lectura en SQLite/Room se actualiza por separado. Así, renovar precios o stock no elimina un pedido sin confirmar y el trabajo de terreno no depende de una consulta a Redis en tiempo real.

**Servicios sin estado durable en memoria.** Las bases de datos y las colas conservan el estado de negocio; las sesiones utilizan los mecanismos de identidad definidos. Sustituir una instancia no debe perder el progreso de una operación. El acceso desconectado respeta las vigencias de las credenciales y las restricciones explicadas en la capa de seguridad.

**Degradación controlada sin pérdida silenciosa.** Cuando un componente no responde, la operación continúa en modo reducido informado a la persona usuaria ("modo offline"). Ninguna degradación produce pérdida de una transacción de venta o entrega: si una escritura no llega al servidor, queda en el buffer local del dispositivo, visible como no confirmada y reconciliada en la sincronización posterior (RT-02.09; Bases Técnicas Transversales, cap. 2, p. 7). La clasificación de servicios (RT-10.02; Bases Técnicas Transversales, cap. 10, p. 22) distingue cuatro niveles, conforme a la Tabla [16](LAFROX-Subdocumento4.md#tab:jd05): crítico, preparación, despacho y emisión de la guía durante la ventana 05:30–07:00, con el bloqueo por excursión térmica y la identidad de bodega que lo habilitan; alto, toma de pedido y consulta de stock y crédito, entrega y evidencia, planificación de rutas, los demás DTE, integración con el ERP, cobranza y rendición, registro de temperatura; medio, canal moderno (EDI), notificaciones, analítica y tableros, portales, consultas de geolocalización, registros de auditoría y seguridad; bajo, reportería e informes a pedido.

**Resiliencia con cortacircuitos y colas.** Las llamadas remotas tienen un tiempo máximo de espera explícito (RT-02.08; Bases Técnicas Transversales, cap. 2, p. 7). Las operaciones reintentables utilizan espera creciente con variación aleatoria y un cortacircuitos que suspende temporalmente las llamadas a un servicio que falla. Si el ERP no está disponible, la preventa conserva la captura de pedidos, mientras las confirmaciones dependientes del legado permanecen sin confirmar. Las colas y sus DLQ permiten recuperar el procesamiento; los consumidores deben deduplicar porque un mensaje puede entregarse más de una vez.

**Integración con legados mediante ACL.** Los módulos M1, M5, M7, M8 y M11 intercambian información con el ERP a través de adaptadores; no absorben su responsabilidad tributaria ni modifican su código. Las capacidades del WMS 2013 se reemplazan gradualmente en M1, M2 y M5. La ACL mantiene separados el modelo de negocio de la solución y los formatos del legado, en coherencia con RT-02.14. No se permiten escrituras directas al ERP.

**Correlación de extremo a extremo.** Cada transacción lleva un `transaction_id` que acompaña las solicitudes y los eventos, incluidos los capturados sin conexión. Al sincronizar, ese identificador permite relacionar métricas, trazas y registros en la plataforma común de observabilidad de nube y sitios locales (RT-03.16; Bases Técnicas Transversales, cap. 3, p. 9; Bases Administrativas, art. 16.4, p. 12).

**Gobierno de contratos y versionado.** Las APIs de negocio y de integración se documentan desde el código, con actualización automática de OpenAPI 3.1 (síncrona) y AsyncAPI 2.6 (eventos), semver estricto, propietario declarado por módulo, compatibilidad hacia atrás y aviso mínimo de 6 meses antes de deprecar una versión (RT-05.16/17; Bases Técnicas Transversales, cap. 5, p. 12).

**Seguridad Zero Trust.** Cada solicitud se verifica explícitamente, sin presuponer la confiabilidad de ninguna red, dispositivo o identidad (NIST, 2020, SP 800-207). Los servicios utilizan mTLS (RT-05.18; Bases Técnicas Transversales, cap. 5, p. 12), los secretos tienen rotación automática (RT-04.09; Bases Técnicas Transversales, cap. 4, p. 11) y los registros de auditoría son inmutables (RT-16.07; Bases Técnicas Transversales, cap. 16, p. 29). La segmentación y las conexiones entrantes al sitio local se especifican en 4.2.

**Separación transaccional y analítica.** Los tableros consultan Redshift Serverless, no el transaccional en vivo. Los eventos incrementales permiten mantener las latencias de hasta 5 minutos para operación, 2 horas para cierre comercial y 4 horas para gestión. Las tareas pesadas se programan fuera de la ventana crítica, sin detener la actualización incremental necesaria para el tablero operacional.

#### 4.1.10.1 SOLID aplicado a los contratos de negocio

La responsabilidad única se comprueba en el flujo de un pedido: M3 captura y confirma el pedido, M2 decide si reserva stock, M5 ejecuta la preparación y la ACL traduce hacia el ERP. Ninguno de esos componentes puede asumir la decisión del otro por compartir un proceso Laravel. Para extender el canal moderno, M11 incorpora un adaptador por cadena bajo un contrato publicado; M3 no se modifica para aprender un nuevo formato EDI. Esa es la aplicación concreta del principio abierto/cerrado.

Un adaptador nuevo sustituye a uno previo solo si conserva las respuestas, errores e idempotencia exigidos por el contrato versionado: las pruebas de contrato verifican esa sustitución. Las interfaces se separan por capacidad y autorización —consulta de stock, reserva, recepción de POD y liberación sanitaria— para que un cliente de lectura no reciba por accidente una operación de escritura. Finalmente, M3, M5 y M7 dependen de puertos de negocio para inventario, documentos y mensajería, no de llamadas directas al SDK de una nube o a tablas del ERP. En QA se reemplazan esos puertos por dobles de prueba; en producción los adaptadores implementan el contrato. Las pruebas de contrato verifican sustitución, segregación de interfaces e inversión de dependencias.

### 4.1.11 Registro de decisiones de arquitectura

<a id="sec:adr"></a>

Las 22 decisiones de arquitectura se resumen en la Tabla [3](LAFROX-Subdocumento4.md#tab:resumen-adr). El Anexo 4-O contiene para cada ADR la decisión, alternativas, criterio, consecuencias, evidencia y requisitos que la sustentan.

<a id="tab:resumen-adr"></a>

**Tabla 3 — Resumen del registro de decisiones de arquitectura**

| **ID** | **Decisión** | **Alternativa principal descartada** | **Criterio decisivo** |
| --- | --- | --- | --- |
| ADR-01 | Monolito modular Laravel con perfiles separados. | Microservicios por módulo. | Operación sostenible y límites verificables. |
| ADR-02 | Fibra, LTE y satélite en espera caliente en los CD. | Solo fibra y LTE. | Extracción continua aun si fallan los medios terrestres. |
| ADR-03 | Sitios autónomos y consolidación en nube. | Autoridad única de Talca. | Autonomía local con vista global. |
| ADR-04 | Persistencia según dominio de datos. | Almacén único. | Separación de despacho y analítica. |
| ADR-05 | RabbitMQ local y SQS FIFO. | Broker solo en nube. | Persistencia e idempotencia tras un corte. |
| ADR-06 | Keycloak con verificación local de turnos. | IdP solo en nube. | Relevo personal durante 24 horas. |
| ADR-07 | Aplicaciones Kotlin nativas. | PWA como cliente único. | Periféricos y captura sin señal. |
| ADR-08 | Reemplazo del WMS 2013 por olas. | Mantención indefinida del legado. | Funciones de bodega y reversión controlada. |
| ADR-09 | Talca recupera su WMS en nube. | Concepción como DR de Talca. | RTO de cuatro horas con falla separada. |
| ADR-10 | Proxmox y Ceph sobre NVMe sin RAID. | Ceph sobre RAID 10. | Quórum y capacidad útil. |
| ADR-11 | Hub GS1 y OpenAS2 con ACL. | Conexiones EDI directas al ERP. | Contratos y aislamiento tributario. |
| ADR-12 | Aurora fija a 3× y Fargate por perfil. | Cambio de instancia en septiembre. | Peak probado sin intervención. |
| ADR-13 | API Gateway REST en nube y puerta de API local A-01. | Gateway solo en nube. | Validación local de esquema, tasa, UUID, permisos y auditoría sin WAN. |
| ADR-14 | CloudWatch con OpenTelemetry y ADOT. | Dos plataformas de observabilidad. | Correlación con buffer local. |
| ADR-15 | Secrets Manager y Parameter Store. | Vault autoadministrado. | Rotación y custodia auditables. |
| ADR-16 | Verified Access para consolas. | Client VPN. | Acceso por aplicación y postura. |
| ADR-17 | `erp-sync` en VM-04 con doble cola. | Trabajador solo en nube. | Guía local válida sin WAN. |
| ADR-18 | Extracción por tres caminos con RPO de 15 min. | Retención solo en el sitio. | Copia durable fuera del sitio. |
| ADR-19 | Regiones declaradas y aprobación del CLIENTE. | Una sola región. | Continuidad y licitud de transferencia. |
| ADR-20 | Angular con TypeScript y Portal de Clientes instalable. | Perfil del cliente en la aplicación Kotlin. | Separación entre clientes y trabajadores. |
| ADR-21 | Terraform, Ansible, GitLab CI y CodeBuild. | CloudFormation/CDK y otra cadena CI. | Propiedad única y promoción trazable. |
| ADR-22 | Greengrass en gateways industriales. | Nube directa o PLC. | Bloqueo térmico local en cinco segundos. |

Fuente: elaboración propia a partir del Anexo 4-O.

La evidencia asociada a cada ficha permite verificar límites de módulo, continuidad por sitio, protección de datos, desempeño bajo el peak y recuperación del WMS de Talca en la nube. En ADR-12, la API utiliza de 2 a 4 tareas en el caso base y 7 en la sensibilidad de 91,70 solicitudes/s, siempre bajo el techo de 8 tareas.

### 4.1.12 Puntos únicos de falla y riesgos residuales

<a id="sec:spof"></a>

RT-02.11 exige identificar las dependencias singulares que subsisten y justificar el riesgo residual. La Tabla [4](LAFROX-Subdocumento4.md#tab:spof) distingue su efecto, la continuidad prevista y la condición de aceptación. Una réplica o una cola reduce el impacto, pero no elimina por declaración la dependencia.

<a id="tab:spof"></a>

**Tabla 4 — Dependencias singulares y riesgo residual**

| **Dependencia** | **Efecto si falla** | **Continuidad prevista** | **Aceptación** |
| --- | --- | --- | --- |
| Identidad central | No hay altas ni revocación remota. | Asignaciones vigentes y servicio local. | Prueba de relevo 24 h. |
| ERP y emisión DTE | Se retrasa una nueva guía; perder la sala de Talca la detiene hasta restituir el ERP. | Preemisión nocturna y ERP por tres caminos; la salida sin guía válida se bloquea. | AL-DTE-01 con 96 salidas. |
| Consolidación central de stock | La reserva central queda fechada. | Cada sitio opera localmente y preventa captura pedidos sujetos a validación. | Conciliación de eventos por sitio. |
| SII y pasarela de pago | No hay respuesta en línea. | Reintento y cobro alternativo aprobado. | Sin confirmar no equivale a aprobado. |
| Planificador experto | Faltan decisiones ante excepciones. | Reglas de M4 y suplente capacitado. | Prueba antes de su retiro. |

Fuente: elaboración propia a partir de RT-02.11 (Bases Técnicas Transversales, cap. 2, p. 7).

Las dependencias externas conservan riesgo residual que exige prueba o contingencia aprobada.

El ERP permanece como único emisor ante el SII mediante fibra, LTE y satélite de Talca; un cambio de carga invalida la guía preemitida y exige una nueva. El riesgo de identidad local tampoco se declara cerrado antes de probar cada relevo de turno durante un corte de 24 horas. El emplazamiento y la redundancia física se verifican en 4.2.

### 4.1.13 Comparación de alternativas arquitectónicas

<a id="sec:alternativas-arquitectonicas"></a>

La comparación considera la carga real, la continuidad desconectada, la reversión y la dotación que deberá operar la solución. La Tabla [5](LAFROX-Subdocumento4.md#tab:alternativas) resume las elecciones lógicas; los ADR explicitan su criterio y consecuencia operativa. La evaluación económica pertenece a los apartados de costos.

<a id="tab:alternativas"></a>

**Tabla 5 — Alternativas lógicas y criterio de selección**

| **Decisión** | **Seleccionada** | **Alternativa viable** | **Criterio decisivo** |
| --- | --- | --- | --- |
| Estilo del núcleo | Monolito modular M1–M12 con perfiles separados. | Servicios por dominio. | Menor carga operativa con 31.000 pedidos/mes. |
| Framework backend | Laravel 13/PHP 8.5 con límites PSR-4. | Django/Python con los mismos contratos. | Un runtime PHP y pruebas de paridad de contratos, datos y colas. |
| Aplicación terreno | Kotlin nativo. | Desarrollo multiplataforma. | Integración Zebra y persistencia local. |
| Mensajería | Broker local y cola de nube. | Broker solo en nube. | Conservación del trabajo con enlace caído. |
| WMS 2013 | Reemplazo por olas M1/M2/M5. | Sustitución simultánea. | Reversión por sitio y capacidad. |

Fuente: elaboración propia a partir del Anexo 4-O y de las Bases Técnicas del caso (cap. 14, p. 24).

El WMS y el broker de cada sitio sostienen recepción y despacho sin WAN; el monolito modular acota el número de procesos a operar.

El Artículo 16 de las Bases Administrativas exige el despliegue híbrido. Su distribución concreta corresponde a 4.2.

### 4.1.14 Relación entre las vistas de arquitectura

<a id="sec:iso42010"></a>

RT-02.03 exige cinco vistas de la arquitectura: lógica, procesos, despliegue, datos y seguridad. El Anexo 4-S define sus interesados, preocupaciones, modelos y reglas de correspondencia, siguiendo la organización de descripciones de ISO/IEC/IEEE 42010:2022 (ISO, 2022a). La integración atraviesa esas vistas; no se presenta como una sexta vista exigida por la Base.

Operaciones necesita comprobar que un pedido puede avanzar sin perder su lote ni saltarse una autorización; Calidad necesita seguir un lote hasta su receptor; Seguridad necesita distinguir quién puede liberar una carga; y TI necesita aislar una falla y recuperar el estado. Las vistas responden a esas preocupaciones con los mismos identificadores M1–M12, INT-01–15 y los componentes transversales del Anexo 4-N. Así se puede pasar de una secuencia a su dueño de datos, contrato y control sin cambiar de vocabulario.

Las correspondencias se comprueban en ambos sentidos: todo evento tiene productor y consumidores; toda escritura tiene dueño; toda función desconectada tiene persistencia y autorización locales; y todo componente desplegado debe realizar una responsabilidad inventariada. Una diferencia se registra con requisito afectado y ADR responsable. La cobertura lógica del inventario no se confunde con el cotejo de emplazamientos y centros de datos.

La vista lógica desarrolla aquí las responsabilidades y sus relaciones. El despliegue y los centros de datos se acreditan en 4.2–4.3.

### 4.1.15 Funciones disponibles y no disponibles sin conexión

<a id="sec:funciones-offline"></a>

Conforme a RT-03.10, la captura del turno de 14 horas en terreno y la operación local de 24 horas en los centros de distribución conservan sus eventos hasta recibir confirmación. RT-03.13 de las Bases Transversales exige nombrar también lo que no funciona sin red y el procedimiento que lo suple; el caso fija bajo ese mismo identificador los plazos de sincronización tras la reconexión. El Anexo 4-J distingue ambos casos; una operación sin confirmar nunca equivale a aprobación de un tercero.

La operación local conserva la captura; las autorizaciones externas esperan conexión o procedimiento aprobado. AL-OFF-01, en el Anexo 4-M, exige un corte de 24 horas con relevos a las 8 y 16 horas, verificación de permisos, reinicio de componentes y reconciliación. La prueba incluye recepción, preparación y despacho con guía válida preemitida al cerrar la carga nocturna. AL-DTE-01 ensaya el cambio de carga que invalida esa guía y exige otra mediante `erp-sync` en VM-04, el ERP y cualquiera de los tres caminos de Talca. Aprobar la captura o el relevo de identidad no basta para acreditar la continuidad completa del despacho.

La copia de stock, crédito y precios lleva fecha de actualización; al superar su vigencia se presenta como referencia, no como aprobación de la venta. El conductor tampoco presenta una captura POS como pago autorizado. El Portal de Clientes instalado conserva el catálogo, los precios con su fecha y el pedido armado sin señal; no reserva stock ni confirma precio o fecha de entrega hasta que M3 recibe el pedido, como verifica AL-CLI-01 del Anexo 4-M. Para el relevo de turno en bodega, la validación local de identidad debe probarse durante 24 horas antes de acreditar la autonomía completa.

### 4.1.16 Reglas de reconciliación

<a id="sec:reglas-reconciliacion"></a>

Toda reconciliación se resuelve por regla de negocio declarada, nunca por la sola marca de tiempo. La clave UUID generada por el cliente se conserva en todos los reintentos y el resultado se retiene para deduplicación durante 30 días; un lote más antiguo se aísla para revisión antes de admitir una nueva escritura. El resultado incluye identificador, versión, regla aplicada, actor y fecha. El Anexo 4-K muestra los conflictos de negocio principales.

Los conflictos de negocio dejan rastro de regla y resultado para revisión posterior.

La replicación es un flujo de continuidad, no una regla para resolver conflictos. INT-12 usa DMS desde Talca hacia una réplica de lectura; los demás sitios sincronizan eventos mediante INT-03 e INT-04. Durante un corte, la base de cada sitio conserva autoridad sobre su operación y retiene cambios hasta el acuse durable, dentro de la capacidad dimensionada. La extracción continua por fibra, LTE y satélite en los CD conserva una copia durable fuera del sitio y sostiene RPO ≤ 15 minutos. AL-DR-01 del Anexo 4-M mide el punto recuperable; el límite residual se justifica en 4.3.2.

### 4.1.17 Articulación entre prueba de entrega, DTE y acuse

<a id="sec:pod-dte-acuse"></a>

La guía de despacho electrónica debe estar vinculada a la salida de mercadería antes de iniciar el traslado. La aplicación no la emite: M5 entrega los datos de despacho a `erp-sync` en VM-04 y por la capa anticorrupción al ERP, que conserva la responsabilidad tributaria y devuelve folio, estado y documento. M6 captura después la recepción efectiva, incluidos bultos rechazados, identidad del receptor y evidencia. El acuse técnico de recepción o procesamiento ante el SII y el acuse de recepción de mercaderías del destinatario son hechos distintos; cada uno conserva su origen, fecha y estado.

#### 4.1.17.1 Secuencia y excepciones

La secuencia lógica es: preparación confirmada en M5; solicitud nocturna de guía al ERP mediante `erp-sync` y ACL de VM-04; autorización de salida con el documento disponible; captura de POD y diferencias en M6; conciliación de la entrega en M7/M8; y, si corresponde, solicitud al ERP de factura, nota de crédito o tratamiento tributario de la devolución. Un mismo `transaction_id` relaciona pedido, guía, entrega, evidencia, acuses y documentos posteriores. El acuse del destinatario se obtiene por el mecanismo que acuerde el CLIENTE conforme a la normativa aplicable; una fotografía o un QR no se presume equivalente por sí solo.

Si el ERP o su canal tributario no confirma la guía antes de la salida, M5 muestra el despacho como bloqueado y lo deriva al responsable de Operaciones y Tributación para aplicar únicamente la contingencia autorizada por el CLIENTE. La captura offline del POD permite registrar una entrega ya despachada; no autoriza emitir retroactivamente una guía desde el teléfono. Esta separación protege la continuidad de la evidencia sin atribuir a la aplicación facultades tributarias que permanecen en el ERP.

#### 4.1.17.2 Control de liberación en la ventana crítica

M5 conserva los estados carga confirmada, guía solicitada, resultado incierto, guía disponible y salida liberada. La solicitud lleva una clave estable por despacho y versión de carga. Ante un timeout se consulta el resultado de esa misma solicitud antes de repetirla; no se genera otra guía a ciegas. Solo se libera cuando la guía corresponde a la carga vigente y su evidencia está disponible localmente. Una modificación efectiva de carga invalida la guía y exige que el ERP anule el documento según su procedimiento y emita uno nuevo antes de la salida; si no hay conectividad para emitirlo, el cambio propuesto no se ejecuta y solo sale la carga original si su guía sigue vigente. Una guía ya anulada o invalidada no se reutiliza, aunque se reponga la carga anterior. El acuse técnico del SII, el documento emitido y la autorización de traslado no se representan con un único booleano.

Al cerrar la carga nocturna se solicita la guía por adelantado, sin confundir anticipación con contingencia. Antes de las 05:30, Operaciones revisa las salidas programadas y las guías disponibles. Durante 05:30–07:00 se prioriza INT-07 sobre reportes y cargas masivas; una incidencia identifica los camiones afectados, hora prevista, responsable y estado documental. Los despachos con documentación válida siguen su curso; ante un cambio de carga, la nueva guía la emite el ERP de Talca por cualquiera de sus tres caminos y, para Concepción y los cross-docking, requiere además un camino disponible del sitio. Ningún perfil de supervisor puede omitir ese control con una autorización genérica.

La preemisión nocturna permite liberar cada camión con la carga amparada por su guía vigente sin depender de Internet durante la ventana; si se propone cambiar la carga y no hay camino hasta el ERP, el cambio se pospone a la ruta siguiente y sale solo la carga original con su guía vigente. Si el cambio ya se ejecutó o la guía se anuló, la salida queda bloqueada hasta disponer de un documento válido. Ningún camión sale sin guía válida. AL-DTE-01 ensaya las 96 salidas con fallas inyectadas, preemisión nocturna, cambio de carga y emisión del ERP ante el SII por fibra, LTE y Starlink en espera caliente de Talca. La prueba registra folio, anulación, nueva guía y estado de cada salida.

El Anexo 4-U distingue emisión tributaria, constancia operativa y acuse del receptor. La firma, fotografía o QR del POD no se equiparan automáticamente al recibo exigible: el mecanismo se selecciona según el receptor y se canaliza por el ERP o el perfil EDI aprobado (SII, 2018, s. f.-a, s. f.-b).

### 4.1.18 Identidad y ciclo de vida de conductores externos

<a id="sec:conductores-externos"></a>

Los conductores de transportistas externos (≈ 160, de 10 empresas) no pertenecen a la dotación de Puelche. Antes de entregar una ruta, la empresa transportista declara la identidad del conductor y su vínculo con ella. En la Etapa 1, despacho registra esa declaración en su función operacional. Desde la Etapa 2, el representante de la empresa puede confirmarla en el portal de transportistas. El responsable de despacho aprueba la asignación conductor–vehículo–turno; el alta inicial requiere conexión para verificar un OTP de un solo uso. El identificador del conductor y el del transportista acompañan cada `EntregaRegistrada`. La autorización se limita a la ruta asignada y a M6, M7 y M8 mediante rol y atributos de turno, sitio y dispositivo.

La aplicación conserva localmente una asignación firmada para el turno de hasta 14 horas y permite capturar eventos mientras no exista red. La caché local de identidad, de solo lectura y TTL de 24 horas, no acorta por sí sola la vigencia de esa asignación de terreno; tampoco la renueva. Una persona reemplazante que no fue dada de alta no obtiene una nueva identidad sin conexión. En ese caso Operaciones reasigna el turno a un conductor ya habilitado y registra la excepción; la rotación no autoriza compartir el OTP ni la cuenta del conductor previo. Para que esa reasignación sea posible durante un corte de 24 horas, el acuerdo operacional con cada transportista le exige mantener enrolados, antes de cada turno, conductores suplentes suficientes para cubrir sus rutas del día siguiente. El manifiesto firmado que Keycloak renueva al menos cada hora los incluye. Si aun así no hay un suplente habilitado, la ruta no sale con una persona no identificada: Operaciones la reasigna a un camión con conductor habilitado o la reprograma. Este caso se ensaya en la prueba de corte de 24 horas antes del hito H5 del Formulario E-25.

Al finalizar el turno expiran la asignación y sus permisos. Si se denuncia pérdida de dispositivo o baja anticipada, Keycloak revoca el acceso conectado y el equipo borra los datos al recuperar conexión. La revocación inmediata de RT-12.07 (Bases Técnicas Transversales, cap. 12, p. 25) se cumple en todo lo que depende de la solución. Al recibir la denuncia, Keycloak revoca la sesión y las credenciales, la API rechaza toda operación posterior del dispositivo y la sincronización rechaza los eventos firmados después de la hora de revocación, que quedan en cuarentena para revisión. Un equipo sin señal no puede borrarse antes de que se conecte. Para ese intervalo, la aplicación exige el PIN personal en cada sesión, cifra los datos locales y bloquea la rendición y el cobro hasta validar la evidencia. La exposición queda acotada a los datos ya presentes en el equipo y a un máximo de 14 horas.

### 4.1.19 Primer cuello de botella bajo la carga de septiembre

<a id="sec:cuello-botella-septiembre"></a>

Septiembre eleva las entregas diarias de aproximadamente 1.400 a 2.600 durante tres semanas. Las 2.600 entregas ocurren a lo largo de la jornada; la ventana 05:30–07:00 concentra la salida de 96 camiones, no todas las firmas de entrega. En esa ventana, el primer cuello de botella probable es la confirmación de guías del ERP mediante la ACL: es una dependencia singular y aumentar réplicas Laravel no acelera al emisor legado. La base transaccional de Talca, la WAN al reconectar y la transferencia de evidencias son candidatos adicionales, no recursos cuya saturación ya se haya medido. La Tabla [6](LAFROX-Subdocumento4.md#tab:cuello-botella) muestra cómo contrastar la hipótesis; RT-09.05 exige sustentar el primer límite con una prueba reproducible.

<a id="tab:cuello-botella"></a>

**Tabla 6 — Detección del primer cuello de botella**

| **Recurso** | **Señal de saturación** | **Respuesta lógica** | **Prueba** |
| --- | --- | --- | --- |
| ERP por ACL | Aumentan guías sin confirmar y latencia p95 de emisión. | Preemitir al cerrar la carga nocturna; invalidar y reemitir si cambia. | 96 camiones en ventana. |
| VM-02, base transaccional de Talca | Crecen la latencia de confirmación y la espera de escritura. | Medir y aliviar contención de escrituras del WMS local. | Carga de preparación y despacho de Talca. |
| Cola de integración | Crecen edad del mensaje y DLQ. | Priorizar guías; diferir reportes. | Corte y reconexión. |
| M2 en bodega | Crecen espera de reserva y bloqueos de stock. | Serializar por SKU y aislar consultas. | Doble compromiso en peak. |

Fuente: elaboración propia a partir de las Bases Técnicas del caso (cap. 14, p. 24, y anexo B, p. 38).

La emisión de guías debe medirse antes de atribuir el límite al cómputo escalable.

Al cerrar la carga nocturna, `erp-sync` en VM-04 solicita la guía al ERP mediante la ACL local; el ERP dispone de fibra, LTE y satélite para comunicarse con el SII. Cualquier cambio de carga invalida la guía y exige otra antes de liberar. Se mide el número de guías sin confirmar antes de cada salida y se alerta al responsable de despacho; el camión afectado no se marca como liberado mientras falte el documento o una contingencia autorizada. La prueba de carga debe confirmar si el ERP es efectivamente el primer límite y ajustar esta hipótesis con medición, como exige RT-09.05.

El Anexo 4-T especifica percentiles, ventanas de ensayo, carga de 1,5 veces el peak y escenario de crecimiento de tres veces, con colas y procesos aislados. Los resultados se deben medir; los cálculos de escenario no son evidencia de capacidad ejecutada.

### 4.1.20 Decisiones del numeral 16.1 del caso

<a id="sec:16-decisiones-caso"></a>

El Anexo 4-L conserva el número y la pregunta de cada una de las dieciséis decisiones del caso. Distingue una regla de diseño de una validación que todavía requiere al CLIENTE: una fila marcada para validación no equivale a una aprobación suya. El registro de supuestos del capítulo 3 debe conservar el fundamento, impacto e instancia de validación de cada decisión.

Las validaciones se identifican por su número de origen para consulta al CLIENTE.

La matriz permite comprobar qué decisión implementa cada módulo. En particular, la identidad externa corresponde al número 5 y el destino del WMS al 14; ninguna de ellas debe desplazarse para llenar una tabla de cumplimiento.

### 4.1.21 Condiciones y supuestos de diseño

<a id="sec:contradicciones"></a>

La lógica adopta seis instalaciones en total, de las cuales cinco son sitios logísticos con servicio local y la sexta es la casa matriz de Talca, contigua al CD principal y sin cómputo propio (Bases Técnicas del caso, cap. 2, p. 5). La parametrización de sitios evita codificar el número en cada módulo.

Los cortes frecuentes de dos horas descritos en la operación son el escenario ordinario. Los límites de diseño son más exigentes: un turno de 14 horas en terreno y 24 horas en cada centro de distribución. No se reduce la autonomía porque el incidente más común sea más corto.

El relevo de turnos sin IdP, la autorización tributaria de salida y la pérdida de sitio se verifican con AL-OFF-01, AL-DTE-01 y AL-DR-01 del Anexo 4-M. Los objetivos exigidos siguen siendo RTO ≤ 4 horas y RPO ≤ 15 minutos para servicios críticos. La extracción continua por fibra, LTE y satélite de los CD sostiene el RPO ante la caída de dos caminos; AL-DR-01 verifica el punto recuperable y la recuperación del WMS de Talca en la nube. El límite residual se justifica en 4.3.2.

El Anexo 4-V reúne los protocolos de aceptación AL-DTE-01, AL-POD-01, AL-SLA-01, AL-OFF-01, AL-CLI-01, AL-DR-01, AL-PERF-01, AL-STOCK-01 y AL-ACT-01. Las actas registran configuración, fallas inyectadas, puntos de recuperación, salidas documentadas y resultados observados; 4.3.2 justifica el límite residual de continuidad.

fisica.chapter

4.chapter

[block]
 25pt28ptlafroxFuerte
 0.45em

# 4.2 Arquitectura física

<a id="cap:4-2-arquitectura-fisica"></a>

La arquitectura física declara dónde vive cada componente de la solución, qué servicios se contratan en la nube, cómo se conecta cada sitio con la nube, qué ocurre cuando falla cada conexión y cuánta capacidad se provee.

Esa arquitectura materializa el despliegue híbrido obligatorio del Artículo 16° de las Bases Administrativas (art. 16, p. 11). La carga principal corre en nube pública AWS, con la región primaria en sa-east-1 (São Paulo, Brasil) y la recuperación ante desastres en us-east-1 (Norte de Virginia, EE. UU.), y los componentes on-premise garantizan la continuidad de la operación de bodega, plataformas y terreno durante los cortes del enlace. La solución cubre las seis instalaciones de la compañía —los centros de distribución de Talca y de Concepción, las plataformas de cross-docking de Curicó, Chillán y Los Ángeles, y la casa matriz de Talca—, además de la calle y los 14.200 puntos de entrega. Cinco de esas instalaciones alojan cómputo; la casa matriz, contigua al centro de distribución de Talca, solo tiene oficinas y trabaja contra la nube. La séptima instalación, que el caso proyecta a tres años, se agrega por parametrización, sin cambios de desarrollo ni crecimiento de servidores en el CD Talca. Dos principios gobiernan el diseño:

- **Carga principal en nube:** el núcleo transaccional de preventa, reparto y canal moderno, la analítica, la integración y el almacenamiento consolidado se ejecutan en AWS sa-east-1, con escalado elástico para el peak de septiembre.

- **Autonomía total de la operación de bodega:** la preparación, el despacho, la recepción y el conteo corren contra los servidores del centro de distribución sin depender de Internet. La guía de despacho se preemite al cerrar la carga nocturna, en Talca desde su cola local y en los demás sitios por sus caminos de enlace. Si cambia la carga entre las 05:30 y las 07:00, se invalida la guía y el ERP de Talca emite otra por cualquiera de sus tres caminos, a los que Concepción y los cross-docking llegan por los suyos; si no hay camino hasta el ERP, el camión sale solo con la carga amparada por su guía vigente y el ajuste pasa a la ruta siguiente. Una guía ya anulada no se reutiliza: esa salida espera un documento válido.

La Figura [15](LAFROX-Subdocumento4.md#fig:vista-general) presenta la vista general de la arquitectura física híbrida. Su recorrido por bloques permite situar los componentes y sus conexiones antes de examinar cada parte de la solución.

**Figura 15 — Vista general de la arquitectura física híbrida**

![Vista general de la arquitectura física híbrida](https://raw.githubusercontent.com/PatricioH315/LafroX/d397c30ff8ad232ec4e3ea02caf5f3cb6800a547/04/figuras/fisica/Arquitectura_Fisica_General.png)

Fuente: elaboración propia.

<a id="fig:vista-general"></a>

La Figura [15](LAFROX-Subdocumento4.md#fig:vista-general) se lee de arriba hacia abajo en tres franjas. En la franja superior están quienes llegan desde fuera de la red del CLIENTE: clientes, proveedores y transportistas por los portales; preventistas y conductores con sus terminales EC55 y TC58e, que leen el termógrafo del camión por Bluetooth (BLE); la casa matriz y el teletrabajo; y las cadenas de supermercados. Cada grupo entra por una puerta distinta. Los portales y los terminales pasan por el borde global (Route 53, Shield Advanced, AWS WAF y CloudFront) hacia API Gateway; la casa matriz y el teletrabajo usan Verified Access; y las cadenas intercambian mensajes por el canal AS2 detrás del Network Load Balancer. Los recorridos y controles de entrada se detallan en la sección [4.2.5](LAFROX-Subdocumento4.md#sec:conexiones).

En la franja central, la región primaria sa-east-1 reúne en la VPC de producción el balanceador privado de aplicación, la aplicación en ECS Fargate, Keycloak, ElastiCache, Aurora PostgreSQL y AWS DMS, que copia los cambios del PostgreSQL de Talca (VM-02) a un esquema de réplica de solo lectura en Aurora. Fuera de esa VPC quedan los servicios regionales DynamoDB, S3, SQS FIFO e IoT Core, que recibe la telemetría de cadena de frío por MQTTS, y la VPC Hub, donde Transit Gateway y la VPN Site-to-Site enlazan la nube con los sitios. La región us-east-1 recibe las réplicas de Aurora PostgreSQL, DynamoDB y S3 para la recuperación ante desastres. Esta franja se detalla en la Figura [19](LAFROX-Subdocumento4.md#fig:nube) de la sección [4.2.3](LAFROX-Subdocumento4.md#sec:servicios-nube), con la distribución por zona de disponibilidad, los servicios de operación y seguridad y la réplica reducida de aplicación en us-east-1.

En la franja inferior están las cinco instalaciones con cómputo, cada una con su par de firewalls y su switching, y conectada a la VPC Hub por su propio túnel VPN. El CD Talca aloja un clúster Proxmox VE con Ceph de tres nodos y seis máquinas virtuales, el servidor del ERP de 2017, trasladado desde la sala actual, y el respaldo NAS WORM; el CD Concepción es un sitio operacional autónomo con dos servidores Proxmox, uno activo con cuatro máquinas virtuales y otro en espera con sus copias; y cada una de las tres plataformas de cross-docking opera autónomamente con dos mini-PC industriales con Docker, uno activo y otro en espera. En los dos centros de distribución, los terminales MC9400 trabajan por Wi-Fi 6E y los gateways IoT, dos en Talca y uno en Concepción, recogen los sensores de las cámaras; en los cross-docking, los terminales inalámbricos trabajan contra el mini-PC activo. Cada tipo de sitio tiene su propia figura de detalle: el cross-docking en la Figura [16](LAFROX-Subdocumento4.md#fig:crossdocking) (sección [4.2.2](LAFROX-Subdocumento4.md#sec:emplazamiento)), el CD Talca en la Figura [25](LAFROX-Subdocumento4.md#fig:cd-talca) (sección [4.3.1](LAFROX-Subdocumento4.md#sec:d-especificaciones-del-sitio-principal-on-)) y el CD Concepción en la Figura [17](LAFROX-Subdocumento4.md#fig:cd-concepcion) (sección [4.2.2](LAFROX-Subdocumento4.md#sec:emplazamiento)).

La figura muestra la regla que ordena el diseño: cada bodega confirma sus operaciones contra su propio WMS, y la nube concentra los servicios comunes, la consolidación de datos y la recuperación del WMS de Talca. Talca replica los cambios de VM-02 a Aurora por DMS; Concepción y los cross-docking envían sus eventos a SQS FIFO. Si cae el enlace, las bases y los brokers locales permiten seguir operando y entregan los eventos retenidos al reconectar.

Este apartado se ordena en seis partes:

- Sección [4.2.1](LAFROX-Subdocumento4.md#sec:implementos): equipamiento y software provistos, resumidos y analizados; el detalle elemento por elemento figura en el Formulario T-11, que acompaña a este subdocumento como archivo propio (LAFROX-Formulario-T-11).

- Sección [4.2.2](LAFROX-Subdocumento4.md#sec:emplazamiento): ubicación de cada componente en la nube o en las instalaciones según el Artículo 16.2 (Bases Administrativas, art. 16.2, p. 11).

- Sección [4.2.3](LAFROX-Subdocumento4.md#sec:servicios-nube): servicios contratados en la plataforma de nube.

- Sección [4.2.4](LAFROX-Subdocumento4.md#sec:despliegue): puesta en marcha y operación, ambientes y ciclo de entrega, red de despliegue, alta disponibilidad, recuperación ante desastres, respaldos y verificación.

- Sección [4.2.5](LAFROX-Subdocumento4.md#sec:conexiones): conexiones, puntos de falla y contingencia de cada uno.

- Sección [4.2.6](LAFROX-Subdocumento4.md#sec:dimensionamiento): dimensionamiento y plan de capacidad derivados de la volumetría del caso.

Las especificaciones del data center primario y del secundario se desarrollan en el apartado [4.3](LAFROX-Subdocumento4.md#cap:4-3-data-center), a continuación de este.

## 4.2.1 Especificaciones Implementos a proveer (Hardware y Software)

<a id="sec:implementos"></a>

Esta sección resume y analiza el equipamiento y el software que la solución requiere en las instalaciones del CLIENTE, en el terreno y en la plataforma de nube. El detalle de cada elemento, con su producto ofertado, su ubicación, su cantidad y su justificación, se entrega en el Formulario T-11. El hardware de terreno —terminales, lectores, impresoras portátiles y sensores— lo adquiere el CLIENTE, y el adjudicatario lo especifica (Bases Técnicas del caso, cap. 11, p. 20). La infraestructura on-premise la provee el adjudicatario dentro del contrato (Bases Administrativas, art. 14.2, p. 10). Todo el equipamiento lo instala, integra y mantiene el adjudicatario.

### 4.2.1.1 Síntesis del equipamiento por familia

La Tabla [7](LAFROX-Subdocumento4.md#tab:t26) cruza cada familia de equipamiento con el sitio donde se instala. Las cifras son las unidades en operación; la reserva se analiza a continuación de la tabla.

<a id="tab:t26"></a>

**Tabla 7 — Equipamiento en operación por familia y por sitio**

| **Familia** | **Talca** | **Concepción** | **Cada cross-docking** | **Terreno** |
| --- | --- | --- | --- | --- |
| Servidores y nodos de cómputo | 3 | 2 | 2 | – |
| Respaldo local (NAS WORM) | 1 | – | – | – |
| Firewalls | 2 | 2 | 2 | – |
| Switches de núcleo, de gestión y de sitio | 3 | 2 | 2 | – |
| Switches de acceso en las bodegas | 4 | 2 | – | – |
| UPS de gabinetes de piso | 4 | 2 | – | – |
| UPS de gabinetes de borde | – | 1 | 1 | – |
| Enlaces satelitales D-06 | 1 | 1 | 1 | – |
| Puntos de acceso Wi-Fi 6E | 39 | 20 | 2 | – |
| Terminales de bodega | 120 | 60 | 2 | – |
| Impresoras de andén | 4 | 2 | – | – |
| Balanzas de recepción | 2 | 1 | – | – |
| Puntos de temperatura en cámaras | 15 | 6 | – | – |
| Gateways IoT | 2 | 1 | – | – |
| Estaciones de trabajo | 5 | 3 | – | – |
| Terminales de preventa | – | – | – | 62 |
| Equipos de reparto por camión | – | – | – | 96 |
| Termógrafos de camión | – | – | – | 28 |

Fuente: elaboración propia.

La tabla incluye cinco enlaces satelitales: uno en Talca, uno en Concepción y uno por cada cross-docking.

La tabla muestra que la operación se concentra en el terreno y en las bodegas, no en la sala técnica. Solo en la calle trabajan 62 terminales de preventa y 96 camiones equipados, cada uno con un terminal de conductor, una impresora de cabina y un terminal de pago; en las bodegas y en los cross-docking, 186 terminales y los puntos de acceso que los conectan. Frente a eso, el cómputo y el almacenamiento suman 12 equipos: 3 servidores en Talca, 2 en Concepción, 6 mini-PC y la NAS. A ellos se suma el servidor del ERP del CLIENTE, que se traslada a la sala de Talca y no forma parte de la oferta. Esa proporción refleja el caso, donde la operación ocurre en la calle, en la cámara y en el andén, y explica por qué la gestión de dispositivos (N-13) es un componente con emplazamiento propio y no un accesorio.

Los equipos de reparto se cuentan por camión y no por conductor, porque los conductores de los transportistas rotan sin aviso y el equipo queda en el vehículo (S-30). Los terminales de bodega se comparten entre turnos, como contempla el perfil operacional del caso (RT-12.11; Bases Técnicas del caso, cap. 15, p. 27), por lo que su cantidad la fija el turno con más personas trabajando a la vez: los 120 preparadores nocturnos de Talca y los 60 de Concepción (S-39); la carga de los camiones la hace esa misma cuadrilla (S-33). Los puntos de acceso son una estimación preliminar por superficie, con mayor densidad dentro de las cámaras, que el estudio de cobertura confirma (S-36).

A las unidades en operación se suma la reserva del numeral 8.4 de las Bases Técnicas Transversales (cap. 8, p. 19): el 10 % del parque de cada tipo de dispositivo y componente crítico, redondeado hacia arriba. El T-11 distingue las unidades iniciales de la compra del año 3. Para el año 3, cada equipo de reparto pasa de 96 unidades instaladas más 10 de reserva a 110 instaladas más 11 de reserva (121 por fila, 15 más que la cantidad inicial); preventa pasa de 62 + 7 a 70 + 7 (77 en total, 8 más). En bodega, el cálculo del Anexo 4-W lleva el total de 207 a 235 terminales, incluidos los repuestos de esa proyección. Cada cross-docking mantiene desde el inicio una unidad de reserva precargada, además de las reservas asignadas a Talca y Concepción. Los demás equipos mantienen las reservas del 10 % o por componente declaradas en el T-11. El switch de gestión no lleva reserva, porque su falla no detiene la operación; los servidores se cubren con repuestos por componente, como discos y fuentes. Los termógrafos no crecen, porque el caso no proyecta más camiones con equipo de frío (S-38). El detalle elemento por elemento está en el Formulario T-11, el cálculo de cada cantidad en el Anexo 4-W y los supuestos en el registro del Subdocumento 3.

Se proveen ocho estaciones nuevas para despacho, administración, planificación, calidad y TI. Los equipos existentes de los usuarios de oficina se incorporan a la gestión central con CrowdStrike Falcon, cifrado de disco, parches y control de extraíbles como condición de acceso por Verified Access conforme a ADR-16 (Anexo 4-O).

### 4.2.1.2 Criterios de selección

Cada familia se especifica contra una condición del caso que el equipamiento de oficina no resiste:

- Los 22 terminales de la cuadrilla de congelado están certificados para trabajar a -30 °C con guantes gruesos y batería de recambio en caliente, porque la preparación de congelados ocurre a -22 °C. Los 185 restantes atienden la bodega seca, la cámara de refrigerado sobre 0 °C y los cross-docking, y son el modelo estándar, porque esas condiciones no exigen la versión para congelado (S-34).

- Los terminales de terreno operan un turno completo sin señal, a una mano y bajo sol directo.

- Los mini-PC de los cross-docking son de rango industrial, porque las naves no tienen climatización y el supuesto de diseño es de hasta 50 °C bajo la techumbre en verano.

- Los 28 termógrafos en operación cubren los 18 camiones propios y los 10 refrigerados de los transportistas que declara el caso, porque el instrumento viaja con la carga y su registro ampara la cadena de frío aun cuando el vehículo no sea del CLIENTE; en los camiones de terceros se instala con el acuerdo de cada transportista (S-28). Están calibrados contra un patrón NIST en dos puntos, porque su registro es la prueba de la cadena de frío ante un cliente o ante la autoridad sanitaria.

En la sala técnica se aplica redundancia sin sobrecompra:

- Talca: los tres nodos idénticos disponen cada uno de 32 hilos, 64 GB RAM y dos NVMe de 960 GB para Ceph sin RAID. Ceph mantiene tres réplicas y quórum con dos nodos; la configuración cubre la carga a 3× con un nodo caído, según el Anexo 4-W. Conforme a RT-03.14 y al Art. 16.4, el nivel declarado es Ceph sin RAID por hardware, con réplica de tres copias: tolera la falla de un disco y de un nodo. RAID 10 bajo Ceph se descarta porque duplica la protección y reduce la capacidad útil (ADR-10; Bases Técnicas Transversales, cap. 3, p. 9; Bases Administrativas, art. 16.4, p. 12).

- Concepción: dos servidores idénticos, uno activo y otro en espera, cada uno dimensionado para la bodega completa y con la base replicada en forma sincrónica (RT-03.14; Bases Técnicas Transversales, cap. 3, p. 9). Los switches de núcleo operan en par conforme a RT-08.03 (Bases Técnicas Transversales, cap. 8, p. 18).

- Los cinco sitios: los firewalls van en par activo/pasivo. Cada cross-docking dispone además de dos switches industriales y de dos mini-PC, uno activo y otro en espera. La reposición de un mini-PC dañado se apoya en la unidad de reserva conservada en Talca.

Los equipos de infraestructura cumplen RT-08.04 (Bases Técnicas Transversales, cap. 8, p. 18) con doble fuente y conexión a circuitos distintos. Los terminales móviles tienen batería, los puntos de acceso reciben PoE de switches con doble fuente, y las impresoras, balanzas y estaciones de trabajo se cubren mediante unidades alternativas y circuitos protegidos.

Todo el equipamiento es nuevo, sin uso previo y con garantía de fábrica vigente desde la recepción conforme (RT-08.06; Bases Técnicas Transversales, cap. 8, p. 18). Su vida útil esperada es de cinco años, mayor que los 56 meses del contrato. Los repuestos provienen de la reserva del 10 % y de la garantía del fabricante. Cada unidad dada de baja se repone desde esa reserva (RT-08.13; Bases Técnicas Transversales, cap. 8, p. 19).

### 4.2.1.3 Software y licenciamiento

El software de base que opera el adjudicatario es de código abierto y se organiza así:

- PostgreSQL con PostGIS, RabbitMQ, Keycloak, Proxmox VE, Ceph con tres réplicas y Docker sostienen la plataforma, junto con el motor de optimización de rutas.

- La aplicación está escrita en PHP 8.5 con Laravel 13 y sus dependencias fijadas por Composer. Las dependencias de PHP se revisan en cada construcción con `composer audit` y su licencia se verifica contra una lista de licencias admitidas antes de incorporarlas.

- Los portales usan Angular y TypeScript; las aplicaciones de terreno usan Kotlin.

Los únicos elementos con suscripción son los servicios de la plataforma de nube, descritos en la sección [4.2.3](LAFROX-Subdocumento4.md#sec:servicios-nube), la gestión de dispositivos, los agentes de detección en endpoints y el orquestador de integración continua GitLab CI. Esta composición mantiene la reversibilidad de la solución y evita que el CLIENTE quede atado a un licenciamiento propietario.

## 4.2.2 Emplazamiento de cada componente

<a id="sec:emplazamiento"></a>

El emplazamiento de cada componente se decide con los seis criterios del Artículo 16.2 de las Bases Administrativas (art. 16.2, p. 11): latencia tolerada, criticidad operacional, volumen de datos, restricciones regulatorias, disponibilidad de conectividad y costo total de propiedad. En este caso la conectividad y la latencia pesan más que en una operación de oficina, porque el caso describe una red que se corta: la fibra de Talca tiene en promedio cuatro cortes al año de hasta seis horas, Concepción carece de respaldo en la situación de partida, los cross-docking dependen de red móvil en la situación de partida y en Los Ángeles la señal es intermitente justo en su ventana de madrugada, las cámaras no tienen cobertura en su interior y hay rutas sin señal durante dos horas o durante el turno completo, como describe el capítulo 6 del caso.

De esos hechos se desprende la regla que ordena todo el emplazamiento: lo que debe funcionar sin enlace vive en el sitio, y lo que escala, se comparte o está expuesto a Internet vive en la nube. Conforme a esa regla, registrada en ADR-03 (Anexo 4-O), los 36 componentes del catálogo se reparten en 13 de nube pura, 11 on-premise y 12 híbridos, que tienen una parte en cada dominio.

### 4.2.2.1 Instalaciones y dominios

De las seis instalaciones que cubre la solución, cinco alojan cómputo on-premise. La tipología que fija el caso se aplica así:

- El CD Talca es la sala técnica secundaria, con un clúster de tres nodos con Proxmox VE y almacenamiento Ceph que aloja las máquinas virtuales VM-01 a VM-06.

- El CD Concepción opera en un gabinete de borde, con dos servidores con Proxmox VE: el activo replica la misma pila en las máquinas VM-C01 a VM-C04 y el otro mantiene sus copias en espera.

- Las plataformas de cross-docking de Curicó, Chillán y Los Ángeles operan cada una en un gabinete de borde, con dos mini-PC industriales, uno activo y otro en espera, que ejecutan el WMS en contenedores.

- La sexta instalación, la casa matriz de Talca, está junto al centro de distribución, solo aloja oficinas y trabaja contra la nube, por lo que no requiere cómputo propio y el dimensionamiento se calcula sobre los otros cinco recintos.

Los dos centros de distribución tienen su recinto especificado en el apartado [4.3](LAFROX-Subdocumento4.md#cap:4-3-data-center); las plataformas de cross-docking no lo tienen, porque operan en un gabinete de borde dentro de la nave. La Figura [16](LAFROX-Subdocumento4.md#fig:crossdocking) muestra ese gabinete, que se repite igual en Curicó, Chillán y Los Ángeles.

**Figura 16 — Gabinete de borde de las plataformas de cross-docking**

![Gabinete de borde de las plataformas de cross-docking](https://raw.githubusercontent.com/PatricioH315/LafroX/d397c30ff8ad232ec4e3ea02caf5f3cb6800a547/04/figuras/fisica/Arquitectura_Fisica_Crossdocking.png)

Fuente: elaboración propia.

<a id="fig:crossdocking"></a>

Starlink es el enlace principal y el LTE de dos proveedores lo respalda; ambos llegan a un par de firewalls compactos en alta disponibilidad, que termina el túnel VPN hacia la nube y conmuta de enlace en menos de 30 s. Detrás de los firewalls, dos switches industriales conectan los dos puntos de acceso de la nave y las dos interfaces de cada uno de los dos mini-PC industriales, que ejecutan en contenedores Docker el WMS, PostgreSQL, RabbitMQ, la caché de Keycloak y el colector ADOT. Los dos terminales inalámbricos de cada plataforma leen los códigos GS1 y trabajan contra el WMS local del mini-PC activo. El gabinete reúne en un par de equipos las funciones que Talca y Concepción reparten en varias máquinas virtuales, y con ello opera al 100 % en local la ventana de tres horas de recepción, desconsolidación y re-despacho. El mini-PC activo replica cada transacción en forma sincrónica al que está en espera, que toma su lugar si falla (RT-03.14; Bases Técnicas Transversales, cap. 3, p. 9; sección [4.2.4.3](LAFROX-Subdocumento4.md#sub:3-alta-disponibilidad)). Cada equipo tiene además alimentación redundante y dos SSD en RAID 1, y la reserva en Talca repone el equipo dañado. La reconstrucción desde el estado central de la nube, si fallan ambos, se trata en la sección [4.2.5](LAFROX-Subdocumento4.md#sec:conexiones).

La Figura [17](LAFROX-Subdocumento4.md#fig:cd-concepcion) presenta el gabinete de borde del CD Concepción como parte de su operación autónoma.

**Figura 17 — Gabinete de borde del CD Concepción**

![Gabinete de borde del CD Concepción](https://raw.githubusercontent.com/PatricioH315/LafroX/d397c30ff8ad232ec4e3ea02caf5f3cb6800a547/04/figuras/centros_de_datos/Arquitectura_Fisica_CD_Concepcion.png)

Fuente: elaboración propia.

<a id="fig:cd-concepcion"></a>

La figura sitúa el WMS, PostgreSQL, RabbitMQ y la caché de identidad en cuatro VM de un servidor Proxmox local. Un segundo servidor idéntico mantiene sus copias en espera, con la base replicada en forma sincrónica, y toma su lugar si falla (RT-03.14; Bases Técnicas Transversales, cap. 3, p. 9; sección [4.2.4.3](LAFROX-Subdocumento4.md#sub:3-alta-disponibilidad)). El par de firewalls y los dos switches de núcleo sostienen la red del sitio. Fibra D-03, LTE D-04 y Starlink D-06 proporcionan tres caminos hacia la nube. La UPS de 5 kVA del gabinete protege los dos servidores, los equipos de red y el terminal satelital durante 30 min y permite el apagado ordenado; su carga de diseño, 3,42 kVA, usa el 68 % de esa capacidad (Anexo 4-W). Cada servidor tiene fuentes redundantes. Solo si fallan ambos se repone el equipo y se reconstruye la base a partir del estado central alimentado por los eventos del propio sitio. El detalle de cada equipo está en el Formulario T-11.

La séptima instalación que proyecta el caso a tres años se incorpora parametrizando la infraestructura como código, sobre uno de los bloques de direccionamiento ya reservados en la Tabla [15](LAFROX-Subdocumento4.md#tab:t64), sin obras en la sala de Talca.

En la nube, la región primaria es sa-east-1 y cada servicio se despliega en al menos dos zonas de disponibilidad. La región us-east-1 solo aloja la recuperación ante desastres. La Figura [18](LAFROX-Subdocumento4.md#fig:emplazamiento-dominios) ubica cada componente en su sitio.

**Figura 18 — Ubicación de los componentes por dominio y por sitio**

Fuente: elaboración propia.

<a id="fig:emplazamiento-dominios"></a>

La figura muestra que ninguna instalación depende de los sistemas de otra para operar, aunque Concepción siga recibiendo parte de su surtido desde Talca. Talca y Concepción tienen cada uno su WMS, su base, su broker y su caché de identidad; los cross-docking reúnen esas mismas funciones en un par de mini-PC, uno activo y otro en espera; y el terreno lleva su propio almacén local en el dispositivo. La nube concentra lo que es común a todos los sitios: los portales, el transaccional compartido, la analítica y los servicios de seguridad. Los doce componentes híbridos aparecen en los dos dominios porque cada uno tiene una parte que debe seguir operando en el sitio y otra que consolida en la nube.

### 4.2.2.2 Correspondencia con la arquitectura lógica

La Tabla [8](LAFROX-Subdocumento4.md#tab:mapeo-logica) asocia cada módulo y cada capa transversal de la arquitectura lógica del apartado 4.1 con el componente físico que lo ejecuta y con el lugar donde corre. Es la traza que permite seguir una responsabilidad lógica hasta su emplazamiento. Los componentes físicos se identifican con un catálogo único, agrupado por letra: A para el núcleo de bodega, B para la cadena de frío, C para los dispositivos de operación, D para la red, E para los cross-docking, F para la observabilidad y la seguridad de los nodos, y N para la nube.

<a id="tab:mapeo-logica"></a>

**Tabla 8 — Correspondencia entre la arquitectura lógica y la física**

| **Módulo o capa (4.1)** | **Componente físico (4.2)** | **Dónde se ejecuta** |
| --- | --- | --- |
| M1 Recepción | A-01 y A-02, con C-03 y C-05 | Sitio |
| M2 Inventario | A-01 y A-02 en el sitio; N-04 y N-05 para el consolidado | Sitio y nube |
| M3 Preventa | C-01 en el terminal; N-04, N-05 y N-07 | Terreno y nube |
| M4 Rutas | N-04 y N-05; motor de optimización en su propio contenedor | Nube |
| M5 Preparación | A-01 y A-02, con C-03 y C-04 | Sitio |
| M6 Reparto | C-02 en el terminal; N-04 y N-05, con la evidencia en S3 | Terreno y nube |
| M7 Rendición | C-02; N-04; A-04 hacia el ERP | Terreno, nube y VM-04 |
| M8 Devoluciones | C-02; N-04; A-01 para la recepción física de retornos mediante la puerta de API local | Terreno, nube y sitio |
| M9 Calidad | B-01, B-02 con la función local de bloqueo en el borde y B-03; N-06 y N-08 | Sitio, camiones y nube |
| M10 Analítica | N-10 | Nube |
| M11 Canal moderno | N-04 con el perfil EDI y el transporte AS2; A-04 | Nube y VM-04 |
| M12 Telemetría | N-04 y N-06, con la API del proveedor de telemetría | Nube |
| Capa 1, portales y consolas | N-01 a N-03 y frontend de consolas en N-04 | Nube |
| Capas 2 y 3, entrada y puerta de enlace | CloudFront, WAF y API Gateway (N-01 a N-03 y N-12); puerta de API local en A-01 | Nube y sitio |
| Capa 5, integración y eventos | A-03; N-09; A-04 | Sitio y nube |
| Capa 6, datos | A-02; N-05, N-06, N-07, N-10 y N-11 | Sitio y nube |
| Capa 7, seguridad e identidad | A-05 con el verificador local; F-03; N-12 | Nube y sitio |
| Capa 8, observabilidad | F-01 y CloudWatch (N-12) | Sitio y nube |

Fuente: elaboración propia.

El perfil local cubre M1, M2, M5, la función de bloqueo de M9 y la recepción física de retornos de M8 a través de la puerta de API local. Los módulos compartidos corren en N-04 y el terreno captura en su terminal. Los perfiles de ejecución se especifican en la sección [4.2.4](LAFROX-Subdocumento4.md#sec:despliegue).

### 4.2.2.3 Síntesis del emplazamiento por dominio y criterio

La Tabla [9](LAFROX-Subdocumento4.md#tab:t21) resume cómo se distribuyen los 36 componentes entre los tres dominios y los seis criterios del Artículo 16.2 (Bases Administrativas, art. 16.2, p. 11) que deciden cada emplazamiento. A continuación se justifica, dominio por dominio, por qué cada componente vive donde vive; el producto, la cantidad y la ubicación exacta de cada elemento no son materia del emplazamiento y se especifican en el Formulario T-11.

<a id="tab:t21"></a>

**Tabla 9 — Distribución de los componentes por dominio y criterio de emplazamiento**

| **Criterio** | **Nube pura** | **On-premise** | **Híbridos** | **Total** |
| --- | --- | --- | --- | --- |
| Latencia tolerada | 1 | 4 | 1 | 6 |
| Criticidad operacional | 2 | 2 | 3 | 7 |
| Volumen de datos | 3* | — | — | 3 |
| Conectividad | — | 4 | 7 | 11 |
| Regulación | 5 | — | 1 | 6 |
| Costo total de propiedad | 3* | 1 | — | 4 |
| **Total de componentes** | **13** | **11** | **12** | **36** |

Fuente: elaboración propia.

El emplazamiento responde a cuatro criterios decisivos del caso:

- Conectividad: decide once componentes y domina los on-premise e híbridos, por los cortes de enlace y el terreno sin señal.

- Regulación: decide seis y domina la nube pura, porque RT-03.22 no admite exponer servicios internos a Internet (Bases Técnicas Transversales, cap. 3, p. 10) y el Artículo 21.2 exige publicar solo por una capa de borde (Bases Administrativas, art. 21.2, p. 15).

- Costo y volumen: concentran en la nube lo que escala y se paga por uso.

- Latencia y criticidad: dejan en el sitio lo que debe responder sin enlace.

La columna Total suma 37 en las filas de criterios porque la plataforma analítica (N-10) se contabiliza en los dos criterios que deciden su emplazamiento, volumen de datos y costo total de propiedad; la fila final suma los 36 componentes efectivos.

### 4.2.2.4 Componentes de nube pura

Los trece componentes de nube pura viven solo en la nube. La justificación de cada uno y el criterio del Artículo 16.2 (Bases Administrativas, art. 16.2, p. 11) que la determina son los siguientes:

- **N-01 Portal de Clientes** (regulación): atiende el catálogo, el pedido de autoatención, el estado de entrega, los documentos y el saldo de los clientes desde Internet, también como aplicación instalable que arma el pedido sin señal; por eso se publica solo en la DMZ de la nube y ningún tráfico externo llega a los sitios del CLIENTE.

- **N-02 Portal de Transportistas** (regulación): desde la Etapa 2, los representantes de cada empresa transportista consultan rutas y documentos y confirman conductor y vehículo desde Internet, y ese acceso se resuelve en la DMZ de la nube. Los conductores externos no usan el portal: trabajan en la app de reparto con su identidad personal.

- **N-03 Portal de Proveedores** (regulación): los 180 proveedores consultan órdenes de compra, recepciones y devoluciones desde Internet, aislados de la red de bodega.

- **N-04 Plataforma de aplicación** (costo): Laravel corre en ECS Fargate con perfiles de API, reconciliación, trabajos y planificación que escalan por separado. La plataforma aloja el frontend Angular de consolas y el transporte AS2 de M11 en dos tareas distribuidas entre dos zonas cada uno; el motor de rutas M4 ejecuta una tarea por corrida, que ECS relanza en otra zona ante una falla para repetirla dentro de la planificación de 15:00 a 18:30, con el plazo de 20 min por corrida medido en la prueba de aceptación. M11 usa contratos versionados (ADR-11, Anexo 4-O).

- **N-05 Base de datos en nube** (criticidad): Aurora PostgreSQL guarda el transaccional de los módulos en nube y la réplica del WMS, conmuta entre zonas en menos de 30 s y se replica a us-east-1.

- **N-06 Telemetría cruda** (volumen): DynamoDB recibe las lecturas de temperatura sin gestión de capacidad y las expira a los 30 días, cuando ya están consolidadas en la capa analítica.

- **N-07 Caché** (latencia): ElastiCache mantiene en memoria el stock, el crédito y las sesiones para que la consulta de preventa responda en menos de 2 s.

- **N-08 Ingesta de IoT** (volumen): IoT Core recibe los 10.920 mensajes diarios de cadena de frío por MQTTS y gestiona los gateways del borde; su motor de reglas escribe cada lectura en DynamoDB y publica en SNS las que superan el umbral.

- **N-09 Mensajería** (criticidad): una cola SQS FIFO recibe la reconciliación de los sitios como sobres JSON versionados, en orden por grupo y sin duplicados; otra cola FIFO lleva las solicitudes al ERP hasta `erp-sync` y una cola FIFO de respuesta para Concepción y para cada cross-docking devuelve sus respuestas, porque Talca las recibe por RabbitMQ local; una cola FIFO de coordinación por cada uno de los cinco sitios lleva las solicitudes de retención y liberación de stock que su shipper lee por conexión saliente; otras colas SQS, separadas de esas, transportan los trabajos internos de Laravel; y SNS difunde las alertas de excursión térmica.

- **N-10 Plataforma analítica** (volumen y costo): S3, Glue, Redshift Serverless y QuickSight conservan 5 años de datos separados del transaccional. Los tableros y la autoría de QuickSight se integran en las consolas para usuarios registrados, con modelo semántico documentado, creación autónoma de informes, exportación y permisos separados de lectura y creación; los indicadores operacionales actuales se consultan en la API de negocio.

- **N-11 Respaldo inmutable y réplica** (regulación): S3 Object Lock, AWS Backup y la réplica en us-east-1 guardan la copia que ni un administrador puede borrar y sostienen el RTO de 4 h y el RPO de 15 min.

- **N-12 Seguridad y gobierno** (regulación): KMS, Secrets Manager, WAF, Shield Advanced, Verified Access, Security Lake y CloudWatch implementan en la nube los controles del Artículo 21 de las Bases Administrativas (art. 21, p. 15) definidos en la arquitectura de seguridad (apartado 4.1), como servicios que un equipo de TI de cuatro personas puede operar.

- **N-13 Gestión de dispositivos** (costo): Android Enterprise y Zebra DNA gestionan como servicio el parque de terminales de preventa, reparto y cámara, con borrado remoto selectivo y sin infraestructura en los sitios.

Ningún componente de nube pura participa en las transacciones que el caso exige resolver sin enlace: la confirmación de preparación, el despacho y el registro de entrega se ejecutan en el sitio o en el dispositivo. Lo que sube a la nube lo hace por tres razones. Los portales y la gestión de identidades externas lo hacen por regulación, porque RT-03.22 no admite exponer servicios internos a Internet (Bases Técnicas Transversales, cap. 3, p. 10). La plataforma de aplicación, la analítica y la telemetría lo hacen por volumen y costo, porque su carga varía con la estación y se paga por uso. Y la seguridad y el respaldo lo hacen porque un equipo de TI de cuatro personas no puede operar esos controles en sus propios servidores.

### 4.2.2.5 Componentes on-premise

Los once componentes on-premise viven solo en las instalaciones del CLIENTE. La justificación de cada uno y su criterio:

- **B-01 Sensores de temperatura** (latencia): los 21 puntos de medición de las cámaras se leen por Modbus en el mismo sitio, porque dentro de la cámara no hay señal y la lectura no puede esperar al enlace.

- **B-02 Gateway IoT** (latencia): los gateways de Talca y Concepción detectan la excursión crítica y sostenida y bloquean el despacho en menos de 5 s, con un buffer de 24 h si cae el enlace, igual a la autonomía del centro de distribución.

- **C-03 Terminales de bodega** (conectividad): los terminales MC9400 trabajan en la bodega y en las cámaras, incluido el congelado a -22 °C, sin señal móvil, contra el WMS del sitio por la red inalámbrica de la bodega.

- **C-04 Impresoras de andén** (latencia): las seis impresoras ZT411 imprimen la etiqueta SSCC en el andén al armar la unidad logística, sin salir de la red local.

- **C-05 Balanzas de recepción** (latencia): las tres balanzas envían el peso de recepción al WMS del sitio en línea, sin digitación y sin depender del enlace.

- **D-02 Switching** (criticidad): los switches de cada sitio segmentan la red local por VLAN y la mantienen operativa aunque caiga la WAN.

- **D-03 Enlace de fibra** (conectividad): es el camino principal de la VPN en Talca y Concepción, con 20 y 10 Mbps en régimen.

- **D-04 Enlace LTE** (conectividad): respalda la fibra en los CD y, con dos proveedores, respalda a Starlink en los cross-docking, con conmutación en menos de 30 s.

- **D-06 Enlace satelital** (conectividad): Starlink es el camino principal de los cross-docking, respaldado por LTE de dos proveedores, y el tercer camino en espera caliente de Talca y Concepción, con terminal encendido, túnel IPsec establecido y BGP de menor preferencia que solo toma tráfico si fallan fibra y LTE.

- **E-01 WMS de cross-docking** (criticidad): el par de mini-PC de cada plataforma, uno activo y otro en espera, opera 100 % en local la ventana de 3 h de recepción, desconsolidación y re-despacho, con su propio broker y su propia base, replicada al equipo en espera.

- **F-02 Gestión de parches** (costo): Ansible aplica los parches y las líneas base CIS a los nodos de los cinco sitios por la red de gestión, sin licencia de plataforma.

En el on-premise dominan la latencia y la conectividad. Los sensores, las impresoras, las balanzas y los terminales de cámara son periféricos que trabajan donde está la mercadería, y ninguno puede depender de un enlace que el caso describe como intermitente. Los tres enlaces y el switching tampoco podrían emplazarse en otro lugar: son la infraestructura que conecta el sitio con la nube y sostiene su red interna cuando esa conexión falla.

### 4.2.2.6 Componentes híbridos

Los doce componentes híbridos tienen una parte en cada dominio. Para cada uno, la justificación explica qué parte vive en el sitio, qué parte vive en la nube y por qué se reparten así:

- **A-01 Motor WMS** (latencia): el perfil `wms_only` del artefacto Laravel, con su servidor web y PHP-FPM, corre en VM-01, VM-C01 y E-01 porque la confirmación de preparación debe responder en 1 s sin depender del enlace, y su réplica en Aurora sostiene la continuidad. El mismo motor expone la puerta de API local de la bodega, que durante un corte valida el esquema, la tasa, el UUID y la auditoría de las solicitudes de los terminales sin pasar por API Gateway.

- **A-02 Base transaccional del WMS** (criticidad): PostgreSQL 16 en VM-02 y VM-C02 es el registro de cada bodega durante un corte. AWS DMS replica continuamente los cambios de VM-02 (Talca) a Aurora para continuidad y lectura por fibra, LTE o Starlink; VM-C02 (Concepción) entrega sus eventos por las colas de integración. En Concepción y en cada cross-docking, la base activa se replica en forma sincrónica al equipo en espera.

- **A-03 Broker de colas** (conectividad): RabbitMQ en VM-03, VM-C04 y E-01 guarda hasta 24 h de eventos sin enlace, con mensajes persistentes y confirmación de publicación; el shipper, un proceso PHP con el adaptador AMQP `php-amqplib`, los publica como sobres JSON en SQS FIFO y solo los retira del broker cuando SQS confirma la recepción. El outbox conserva 24 h de eventos ya enviados para reenviarlos tras una conmutación.

- **A-04 Capa anticorrupción del ERP** (criticidad): corre en VM-04, en la misma sala que el ERP de 2017, que no se modifica. En la misma VM, `erp-sync` consume la cola local de Talca y, mediante conexión saliente, la cola FIFO de solicitudes al ERP de los demás orígenes, cuyas respuestas devuelve por la cola de cada sitio; usa una clave idempotente por operación para que un reintento no emita un segundo documento tributario.

- **A-05 Identidad** (conectividad): el IdP maestro Keycloak corre en Fargate y sus cachés de solo lectura en VM-05, VM-C03 y E-01 validan las sesiones de bodega y de cross-docking sin enlace; en el mismo nodo, un verificador local habilita cada relevo de turno durante un corte con el manifiesto de turno firmado y un segundo factor local, el PIN personal.

- **B-03 Termógrafos de camión** (conectividad): los 28 termógrafos —18 en los camiones propios y 10 en los de los transportistas, instalados con el acuerdo de cada uno (S-28)— registran la temperatura durante toda la ruta sin señal y sincronizan por Bluetooth con el terminal del conductor, que alerta la excursión térmica en el momento y la reenvía a la nube cuando recupera cobertura; al volver el camión, el mismo terminal descarga el registro completo y lo envía a la nube para que IoT Core lo valide.

- **C-01 App de preventa** (conectividad): toma pedidos contra el almacén local del terminal cuando no hay señal y sincroniza por CloudFront al reconectar, sin duplicar pedidos (sección [4.2.5](LAFROX-Subdocumento4.md#sec:conexiones)).

- **C-02 App de reparto** (conectividad): registra entregas, evidencia y cobros durante 14 h sin señal y los sincroniza con la nube al recuperar cobertura.

- **D-01 Firewall y Customer Gateway** (criticidad): el par de firewalls de cada uno de los cinco sitios termina los túneles IPsec hacia el Transit Gateway de AWS y conmutan de enlace en menos de 30 s.

- **D-05 Respaldo local** (conectividad): el NAS WORM de Talca restaura el WMS en 4 h sin depender del enlace, y su complemento inmutable vive en S3 Object Lock.

- **F-01 Telemetría de observabilidad** (conectividad): los colectores ADOT de VM-06, VM-C04 y E-01 guardan hasta 24 h de métricas y trazas en disco y las envían a CloudWatch al reconectar.

- **F-03 Detección en endpoints** (regulación): los agentes EDR de cada nodo y estación reportan a una consola central, lo que da una sola respuesta ante incidentes en nube y on-premise. El servidor del ERP del CLIENTE no lleva agente, porque se traslada sin cambios de software. El firewall de Talca solo le permite el tráfico de la ACL en VM-04 y la administración del CLIENTE.

Los componentes híbridos siguen todos el mismo patrón: la parte que atiende la operación queda en el sitio y la parte que consolida queda en la nube, unidas por un mecanismo que tolera el corte. En el núcleo de bodega, Talca replica su base por DMS y los demás sitios sincronizan eventos por colas; en el terreno, el almacén local del dispositivo; y en la observabilidad, el buffer en disco de los colectores. Por eso la conectividad es el criterio dominante en siete de los doce: cada uno existe en dos lugares precisamente porque el enlace entre ellos no es confiable.

### 4.2.2.7 Autonomía de cada ámbito sin enlace

El emplazamiento descrito se verifica en lo que cada ámbito puede hacer cuando pierde el enlace. La Tabla [10](LAFROX-Subdocumento4.md#tab:t29) declara esa autonomía y el tiempo en que cada ámbito vuelve a quedar sincronizado.

<a id="tab:t29"></a>

**Tabla 10 — Autonomía por ámbito ante la pérdida del enlace**

| **Ámbito** | **Autonomía sin enlace** |
| --- | --- |
| Centros de distribución de Talca y Concepción | 24 h o más, con reconciliación determinista |
| Terreno | 14 h, un turno completo |
| Cross-docking | 24 h o más; la ventana de 3 h opera 100 % local |
| Sincronización al reconectar | CD en 2 h; flota en 10 min |

Fuente: elaboración propia.

Durante la autonomía, cada ámbito mantiene su operación completa contra sus datos locales:

- El centro de distribución sigue con recepción, preparación, despacho, conteo cíclico y trazabilidad contra la base local.

- El terreno sigue con toma de pedido, entrega, evidencia, devoluciones y cobros contra el almacén local del dispositivo.

- El cross-docking mantiene recepción, desconsolidación, lectura del termógrafo en la recepción y re-despacho.

Al reconectar, el vuelco ocurre en orden estricto, sin duplicados y con reconciliación determinista.

La autonomía de cada ámbito cubre el corte más largo que describe el caso para ese lugar. Las seis horas del peor corte de fibra de Talca quedan dentro de las 24 horas del centro de distribución, y la ruta rural que recupera cobertura solo al regresar queda dentro del turno de 14 horas del terreno. Los tiempos de sincronización se sostienen con los enlaces dimensionados en la sección [4.2.6](LAFROX-Subdocumento4.md#sec:dimensionamiento), y lo que ocurre ante cada falla se desarrolla en la sección [4.2.5](LAFROX-Subdocumento4.md#sec:conexiones).

## 4.2.3 Servicios contratados en la plataforma de nube

<a id="sec:servicios-nube"></a>

La plataforma de nube es Amazon Web Services. Todos los servicios se contratan en cuentas del CLIENTE, organizadas bajo AWS Control Tower con una cuenta por ambiente, de modo que la propiedad de los datos y de la infraestructura es del CLIENTE desde el primer día. La selección sigue tres reglas:

- Preferir el servicio administrado cuando existe, porque el área de TI del CLIENTE es de cuatro personas.

- Preferir servicios compatibles con estándares abiertos, para acotar el esfuerzo de salir de la plataforma.

- Contratar en la región secundaria solo lo que la recuperación ante desastres necesita.

### 4.2.3.1 Servicios por función

La Tabla [11](LAFROX-Subdocumento4.md#tab:servicios-nube) agrupa los servicios contratados por la función que cumplen en la arquitectura y los asocia a los componentes del catálogo que los usan. El listado servicio por servicio, con su justificación y su cantidad, se entrega en el Formulario T-11.

<a id="tab:servicios-nube"></a>

**Tabla 11 — Servicios contratados en la plataforma de nube, por función**

| **Función** | **Servicios contratados** | **Componentes** | **Región** |
| --- | --- | --- | --- |
| Entrada pública | Route 53, CloudFront, AWS WAF, Shield Advanced, API Gateway pública | N-01 a N-03, N-12 | Global y sa-east-1 |
| Acceso interno | Verified Access, API Gateway privada y endpoint execute-api | N-04, N-12 | sa-east-1 y us-east-1 |
| Cómputo de aplicación | ECS Fargate, Application Load Balancer privado, Lambda autorizadora | N-04, A-05 | sa-east-1 y us-east-1 |
| Datos operacionales | Aurora PostgreSQL, Database Migration Service, DynamoDB, ElastiCache | N-05, A-02, N-06, N-07 | sa-east-1 y us-east-1 |
| Mensajería | SQS FIFO para la reconciliación, para las solicitudes al ERP y sus respuestas, y para la coordinación de reservas por sitio, SQS para los trabajos de Laravel y SNS, con equivalentes vacíos creados por infraestructura como código en us-east-1 | N-09, A-03 | sa-east-1 y us-east-1 |
| Integración B2B | Network Load Balancer y OpenAS2 en Fargate | N-04 (M11) | sa-east-1 |
| Internet de las cosas | IoT Core, IoT Greengrass | N-08, B-02, B-03 | sa-east-1 y borde |
| Analítica | S3, Glue, Redshift Serverless, QuickSight embebido | N-10 | sa-east-1 |
| Respaldo y recuperación | AWS Backup, S3 Object Lock, replicación de S3 entre regiones | N-11, D-05 | sa-east-1 y us-east-1 |
| Red y conectividad | VPC, Transit Gateway, Site-to-Site VPN, NAT Gateway, VPC Endpoints | D-01 | sa-east-1 y us-east-1 |
| Identidad, claves y secretos | KMS, Secrets Manager, Parameter Store, IAM Identity Center | A-05, N-12 | sa-east-1 y us-east-1 |
| Detección y cumplimiento | GuardDuty Runtime Monitoring para tareas ECS Fargate, Security Lake, Security Hub, Inspector, Macie, CloudTrail y Config | N-12, F-03 | sa-east-1 y us-east-1 |
| Operación y gobierno | CloudWatch, Systems Manager, Control Tower, Organizations, Cost Explorer, Budgets | F-01, F-02, N-12 | sa-east-1 |
| Construcción y registro de imágenes | CodeBuild y Elastic Container Registry con replicación de imágenes entre regiones | N-04, A-01 | sa-east-1 y us-east-1 |
| Servicios de terceros en nube | Android Enterprise y Zebra DNA; consola del EDR | N-13, F-03 | Servicio gestionado |

Fuente: elaboración propia.

La tabla distingue los servicios de entrada, aplicación y datos. La aplicación corre en contenedores administrados; la única función Lambda autoriza las API REST. Los portales Angular se sirven desde S3 privado por CloudFront, mientras el frontend de consolas y el transporte AS2 mantienen dos tareas Fargate en dos zonas cada uno; el motor de rutas ejecuta una tarea por corrida. Las colas SQS de trabajos de Laravel están separadas de la cola FIFO de reconciliación; ElastiCache solo actúa como caché. El recorrido de acceso se precisa en la sección [4.2.5](LAFROX-Subdocumento4.md#sec:conexiones).

Para cumplir RT-11.16, GuardDuty Runtime Monitoring observa las tareas Amazon ECS ejecutadas en Fargate en las cuentas de ambiente de sa-east-1 y en la región de recuperación us-east-1. Se fija Linux Fargate plataforma 1.4 o posterior y un rol de ejecución que permite obtener el agente administrado; la VPC permite descargar su imagen desde ECR y sus capas desde S3. GuardDuty agrega el agente como sidecar a las tareas nuevas y analiza actividad de procesos, archivos y red; las tareas que ya estén ejecutándose se reinician o redespliegan para que queden cubiertas. Los hallazgos se consolidan en Security Hub, que los entrega al flujo de respuesta de seguridad para su triage y contención (Amazon Web Services, s. f.-d, s. f.-e). La cobertura corresponde a ECS sobre Fargate; EKS sobre Fargate no forma parte de la arquitectura.

### 4.2.3.2 Región secundaria y residencia de los datos

La región us-east-1 no es una segunda producción. Solo contiene recursos para la recuperación:

- Datos: réplica de Aurora mediante Aurora Global Database y de las tablas de temperatura de DynamoDB mediante Global Tables.

- Respaldos: copia de los buckets de S3 salvo el de geolocalización y copias de AWS Backup.

- Aplicación: réplica reducida de ECS que escala a carga completa en menos de 30 minutos durante una conmutación.

- Imágenes: réplica de las imágenes de Elastic Container Registry, que recibe cada entrega liberada en Producción.

- Mensajería: colas SQS FIFO y SQS, y temas SNS equivalentes, creados vacíos por infraestructura como código para la conmutación.

La región primaria sa-east-1 está en São Paulo, Brasil, y la secundaria us-east-1 en Virginia del Norte, Estados Unidos; ambas suponen transferencia internacional de datos desde Chile. Los datos de geolocalización de personas quedan fuera de la región secundaria; la analítica se copia a ella en forma diferida, sin las posiciones de flota, porque conserva los registros de temperatura y de trazabilidad de lote que el caso exige retener cinco años (Bases Técnicas del caso, cap. 15, p. 26). La base de licitud, los resguardos de tratamiento y la garantía de continuidad ante las decisiones de residencia del CLIENTE se desarrollan en la sección [4.3.2](LAFROX-Subdocumento4.md#sec:e-especificaciones-del-sitio-secundario-y-).

### 4.2.3.3 Servicios que no se contratan

Los registros de decisión descartan de forma expresa los siguientes servicios y productos, que no aparecen en la arquitectura:

- No se instala Redis ni Laravel Horizon en los sitios, porque la continuidad local descansa en PostgreSQL y RabbitMQ, y un tercer motor por sitio agregaría operación sin beneficio.

- No se contrata un clúster de Kubernetes (EKS). El monolito modular se despliega en pocos perfiles independientes (API, consumidor, trabajos, consolas, AS2 y motor de rutas), que ECS Fargate ya despliega y revierte por separado (RT-02.02; Bases Técnicas Transversales, cap. 2, p. 6). Kubernetes se justifica con decenas de servicios, y el equipo de TI de cuatro personas no operaría su plano de control.

- No se contrata Kafka administrado (MSK), porque RabbitMQ en cada sitio y SQS FIFO en la nube resuelven el orden y la durabilidad con menos operación.

- No se contratan servicios de trazas y métricas separados de CloudWatch, porque las Bases piden una sola plataforma de observabilidad para nube y on-premise.

- No se autoaloja un gestor de secretos, porque Secrets Manager rota las credenciales sin el desellado manual que exigiría uno propio.

### 4.2.3.4 Modelo de contratación

Los servicios se contratan por uso, con la capacidad base comprometida mediante Savings Plans y el peak de septiembre cubierto con capacidad efímera que se libera al terminar. Los ambientes de Desarrollo, QA y Preproducción se reducen o apagan fuera del horario de uso. La reversibilidad está asegurada por la elección de servicios: Aurora es compatible con PostgreSQL, los datos analíticos se guardan en formato Parquet, y Keycloak, Laravel, PostgreSQL y RabbitMQ son de código abierto, de modo que un traslado a otra plataforma conserva la aplicación y los datos y se concentra en sustituir los servicios administrados de AWS que la solución consume. Ese esfuerzo se acota en tres grupos: Aurora, ElastiCache, S3 y ECS Fargate se reemplazan por PostgreSQL, Redis, almacenamiento compatible con S3 y contenedores, solo con cambios de configuración; SQS, SNS, Secrets Manager y CloudWatch se reemplazan cambiando el adaptador que ya los aísla detrás de un puerto de la aplicación; e IoT Core con Greengrass, DynamoDB, Redshift con Glue y QuickSight, API Gateway con su autorizador y Verified Access no son portables y exigen rediseñar la ingesta de frío, la analítica y la entrada. Una salida cambia así la configuración de cuatro servicios y los adaptadores de otros cuatro, y rediseña cinco componentes (RT-03.07; Bases Técnicas Transversales, cap. 3, p. 8). Los montos de estos servicios se declaran en la Oferta Económica y no en este documento.

### 4.2.3.5 Topología de los servicios

La Figura [19](LAFROX-Subdocumento4.md#fig:nube) ubica en la topología de AWS los servicios de la Tabla [11](LAFROX-Subdocumento4.md#tab:servicios-nube) y los recursos de la región secundaria: el borde global, la región primaria sa-east-1 con sus dos zonas de disponibilidad y la región de recuperación us-east-1. Los servicios de gobierno de cuentas de la tabla (Control Tower, Organizations, Cost Explorer y Budgets) se aplican sobre las cuentas y no ocupan un lugar en la topología, por lo que no se dibujan.

**Figura 19 — Topología de los servicios en AWS: región primaria sa-east-1 y región de recuperación us-east-1**

![Topología de los servicios en AWS: región primaria sa-east-1 y región de recuperación us-east-1](https://raw.githubusercontent.com/PatricioH315/LafroX/d397c30ff8ad232ec4e3ea02caf5f3cb6800a547/04/figuras/fisica/Arquitectura_Fisica_Nube.png)

Fuente: elaboración propia.

<a id="fig:nube"></a>

La figura se recorre desde la entrada. En el borde global, Route 53 resuelve los nombres, y AWS WAF y Shield Advanced protegen a CloudFront, que sirve los portales desde S3 y reenvía las llamadas a la API Gateway pública. La Lambda autorizadora valida el token de las rutas protegidas de la API pública y de la API privada; los endpoints OIDC de autenticación pasan sin autorizador hacia Keycloak. La casa matriz y el teletrabajo entran por Verified Access al balanceador privado de aplicación, y las cadenas de supermercados llegan por el Network Load Balancer al transporte AS2.

Dentro de la VPC de producción, cada zona de disponibilidad tiene su propia copia de ECS Fargate, Keycloak y ElastiCache. Aurora PostgreSQL tiene el escritor en sa-east-1a y el lector promovible en sa-east-1b, y AWS DMS escribe en el escritor la réplica del PostgreSQL de Talca. Los VPC endpoints conectan Fargate con los servicios regionales sin salir a Internet. Esos servicios quedan fuera de las zonas porque AWS los opera en varias zonas de forma nativa: IoT Core escribe las lecturas de frío en DynamoDB, SQS FIFO recibe la reconciliación de los sitios, SNS difunde las alertas, ECR guarda las imágenes y AWS Backup custodia las copias; la analítica fluye de S3 a Glue, Redshift y QuickSight. El bloque de operación y seguridad (CloudWatch, CloudTrail, Config, GuardDuty, Security Hub, KMS, Secrets Manager, Systems Manager, IAM Identity Center e Inspector) es transversal a toda la región, y la VPC Hub recibe los túneles de los cinco sitios.

La región us-east-1 repite la cadena de entrada con capacidad reducida: API Gateway, la Lambda autorizadora, Verified Access y una VPC de recuperación con balanceador, Fargate, Keycloak y la réplica secundaria de Aurora, además de su propio Transit Gateway y su VPN para reconectar los sitios. Abajo quedan DynamoDB, la réplica de S3 y AWS Backup, junto con ECR, que ya tiene las imágenes replicadas, y las colas SQS FIFO y los temas SNS, que existen vacíos. La figura muestra así dos propiedades del diseño: ningún componente con estado depende de una sola zona de disponibilidad, y la recuperación regional no exige reconstruir la entrada, porque la réplica solo escala. Los tiempos de esa conmutación se fijan en el apartado [4.3](LAFROX-Subdocumento4.md#cap:4-3-data-center).

[1]8pt
#12pt

## 4.2.4 Arquitectura de despliegue

<a id="sec:despliegue"></a>

La arquitectura física describe qué componentes existen, dónde viven y cómo se conectan. Esta sección describe cómo esa solución se pone en marcha y se mantiene en operación durante los 56 meses del contrato: por qué ambientes pasa un cambio antes de llegar a las bodegas y a la calle, sobre qué red se despliega, cómo sigue operando cuando algo falla y cómo se recupera cuando se pierde un sitio completo o se daña un dato. Los puntos de falla de cada conexión y de cada equipo, con su resolución inmediata, se declaran en la sección de conexiones y contingencia (Tablas [20](LAFROX-Subdocumento4.md#tab:fallas-sitios) y [21](LAFROX-Subdocumento4.md#tab:fallas-nube)). Aquí se describen los mecanismos que sostienen esa continuidad y cómo se verifican.

Esos mecanismos son tres y no se sustituyen entre sí. La alta disponibilidad responde a la falla de un componente sin que la operación lo note. La recuperación ante desastres responde a la pérdida de un sitio o de una región completa. El respaldo responde al daño del dato, sea un borrado accidental, una corrupción o un cifrado malicioso, frente a los cuales las réplicas no protegen, porque replican el daño con la misma fidelidad que una escritura legítima.

### 4.2.4.1 Ambientes y ciclo de entrega

<a id="sub:1-ambientes-de-despliegue-rt-04-01"></a>

Un cambio recorre tres ambientes antes de llegar a Producción: Desarrollo, QA y Preproducción. Se construye y se prueba de forma unitaria en Desarrollo, se valida en QA con pruebas funcionales, de integración y de regresión automatizadas, y se ensaya en Preproducción, donde ocurren las pruebas de aceptación, de carga y de resiliencia y el ensayo del paso a producción. Solo entonces se promueve a Producción, sin recompilar, de modo que el artefacto que llega a producción es el mismo que se probó. La marcha blanca de cada etapa ocurre ya en Producción, porque es operación supervisada con datos y usuarios reales en paralelo con la operación vigente. Un quinto ambiente, de Recuperación ante Desastres, sostiene la continuidad: reside en la región us-east-1 para el dominio de nube, mientras que el WMS de Talca se recupera en la plataforma de nube, como se describe en la recuperación ante desastres de esta sección. La Tabla [12](LAFROX-Subdocumento4.md#tab:t62) muestra cada ambiente con su bloque de direccionamiento, su región y su función.

<a id="tab:t62"></a>

**Tabla 12 — Ambientes de despliegue**

| **Ambiente** | **VPC** | **Región** | **Función** |
| --- | --- | --- | --- |
| Desarrollo | 10.104.0.0/16 | sa-east-1 | Construcción y pruebas unitarias |
| QA | 10.103.0.0/16 | sa-east-1 | Pruebas funcionales, de integración y de regresión, y análisis dinámico |
| Preproducción | 10.102.0.0/16 | sa-east-1 | Aceptación, carga, resiliencia y ensayo del paso a producción |
| Producción | 10.101.0.0/16 | sa-east-1 | Operación en varias zonas, con los sitios on-premise, y marcha blanca |
| Recuperación ante Desastres | 10.201.0.0/16 | us-east-1 | Réplica en caliente del dominio de nube y recuperación del WMS de Talca en la nube |

Fuente: elaboración propia.

Cada ambiente reside en una cuenta AWS propia, bajo una organización de AWS Control Tower cuyas políticas de control de servicio impiden que un error o un acceso indebido en un ambiente alcance a otro. La organización incorpora además sus cuentas de gestión, de archivo de registros y de auditoría. Los bloques de direccionamiento no se solapan entre sí ni con los de los sitios on-premise, y solo el ambiente de recuperación reside fuera de la región primaria. Los cinco ambientes quedan habilitados y operativos en el hito H3 del Formulario E-25, en el mes 6 del contrato, antes de la primera marcha blanca (RT-04.01; Bases Técnicas Transversales, cap. 4, p. 10).

En la nube, en los cinco ambientes, la imagen de la aplicación corre en ECS Fargate, que es el cómputo de la plataforma de aplicación N-04 (Tabla [11](LAFROX-Subdocumento4.md#tab:servicios-nube)). Cada ambiente despliega la imagen en su propia cuenta, desde el mismo Elastic Container Registry de sa-east-1, que replica cada imagen en us-east-1 para que la región de recuperación no dependa de la primaria. Los ambientes se diferencian en su escala y en su conectividad, no en el servicio donde corre el código:

- Producción opera en dos zonas.

- Preproducción replica esa topología.

- Desarrollo, QA y Preproducción se reducen o apagan fuera del horario de uso.

- Recuperación ante Desastres mantiene la réplica reducida de us-east-1.

Desarrollo y QA son aislados y se reconstruyen desde código. Desarrollo trabaja con datos sintéticos o anonimizados, y QA con un juego de datos de prueba controlado y versionado que se restituye a un estado conocido antes de cada ciclo de pruebas. Ningún ambiente no productivo recibe datos productivos sin anonimización o seudonimización verificable. Desarrollo, QA y Preproducción se reducen o apagan fuera del horario de uso, con el ahorro reflejado en la estructura de costos (RT-04.13; Bases Técnicas Transversales, cap. 4, p. 11).

Las bodegas no tienen ambientes propios de prueba, y no los necesitan. El on-premise es producción: la imagen wms_only que corre en los centros de distribución y en los cross-docking es la misma que recorrió Desarrollo, QA y Preproducción en la nube, y la infraestructura de cada sitio se declara como código versionado. Lo que se ensayó en la nube es, por lo tanto, lo que se instala en Talca, en Concepción y en cada cross-docking, sitio por sitio. QA y Preproducción ensayan esa imagen con el verificador local de identidad y la puerta de API local del WMS, con adaptadores simulados del ERP, y reproducen el corte de enlace y el relevo de turno antes de cada paso a producción.

Preproducción es equivalente a Producción en versiones, configuración, dimensionamiento y topología de nube (RT-04.02; Bases Técnicas Transversales, cap. 4, p. 10). Subsisten tres diferencias justificadas:

- Preproducción se reduce o apaga fuera del horario de uso, por costo.

- Preproducción trabaja con datos sintéticos generados desde la volumetría del caso, cuya anonimización se verifica con Amazon Macie, porque no se admiten datos productivos reales fuera de Producción sin anonimización verificable.

- Preproducción emula el sitio on-premise dentro de su propia VPC, con la misma imagen wms_only, el mismo broker y el mismo verificador local, pero sin túnel hacia las bodegas, para que un ensayo no pueda alcanzar la operación real.

La emulación reproduce la topología del sitio y no su hardware. Por eso, la primera instalación de cada entrega en los centros de distribución y los cross-docking avanza sitio por sitio, como se describe en la liberación. Durante las pruebas de carga y estrés de la Tabla [32](LAFROX-Subdocumento4.md#tab:t86) opera con el dimensionamiento completo de Producción.

Las figuras siguientes muestran cada uno de los cinco ambientes. Desarrollo, QA y Preproducción residen solo en la nube. Producción abarca la nube y los sitios on-premise. Recuperación ante Desastres cubre la pérdida de la región primaria mediante us-east-1 y la pérdida de la sala de Talca mediante el WMS levantado en la plataforma de nube (numeral 4.1 de las Bases Técnicas Transversales; Bases Técnicas Transversales, cap. 4, p. 10). Concepción opera su propia bodega en Producción.

**Desarrollo**

La Figura [20](LAFROX-Subdocumento4.md#fig:amb-desarrollo) muestra cómo llega una entrega a Desarrollo. Sus pasos numerados se leen de izquierda a derecha.

**Figura 20 — Ambiente de Desarrollo**

![Ambiente de Desarrollo](https://raw.githubusercontent.com/PatricioH315/LafroX/d397c30ff8ad232ec4e3ea02caf5f3cb6800a547/04/figuras/fisica/ambientes/amb_desarrollo.png)

Fuente: elaboración propia.

<a id="fig:amb-desarrollo"></a>

Los pasos de la figura son los siguientes:

- GitLab CI toma el cambio aprobado en la rama protegida y ejecuta los controles del pipeline, que se detallan más adelante en esta sección.

- AWS CodeBuild construye la imagen de la aplicación una sola vez, de forma hermética y con procedencia SLSA nivel 3.

- Elastic Container Registry (ECR) guarda la imagen firmada. Desde aquí se promueve por su digest a los demás ambientes, sin recompilar.

- ECS Fargate despliega la imagen en la VPC 10.104.0.0/16 de la cuenta de Desarrollo, con la configuración de SSM Parameter Store y los secretos de AWS Secrets Manager propios del ambiente.

- El pipeline publica los portales Angular de clientes, transportistas y proveedores (N-01 a N-03) en un bucket S3 privado, que CloudFront sirve.

Desarrollo no tiene enlace con los sitios.

**QA**

QA repite la secuencia de Desarrollo en su propia cuenta y su propia VPC (Figura [21](LAFROX-Subdocumento4.md#fig:amb-qa)). No construye una imagen nueva: usa la misma que recorrió Desarrollo, de modo que una falla detectada aquí corresponde al artefacto y no a una recompilación.

**Figura 21 — Ambiente de QA**

![Ambiente de QA](https://raw.githubusercontent.com/PatricioH315/LafroX/d397c30ff8ad232ec4e3ea02caf5f3cb6800a547/04/figuras/fisica/ambientes/amb_qa.png)

Fuente: elaboración propia.

<a id="fig:amb-qa"></a>

Los pasos de la figura son los siguientes:

- GitLab CI promueve a QA la entrega que superó Desarrollo.

- CodeBuild no vuelve a construir: la imagen es la que construyó para Desarrollo.

- ECR entrega esa imagen firmada, identificada por su digest.

- ECS Fargate la despliega en la VPC 10.103.0.0/16 de la cuenta de QA, donde corren las pruebas funcionales, de integración y de regresión.

- Los portales se publican en el bucket S3 privado de QA, que CloudFront sirve.

**Preproducción**

En Preproducción la secuencia se ensaya sobre la topología de Producción y sobre un sitio on-premise emulado (Figura [22](LAFROX-Subdocumento4.md#fig:amb-preproduccion)). Aquí se demuestran las migraciones y el despliegue azul-verde con canario antes de cada paso a producción (RT-04.07; Bases Técnicas Transversales, cap. 4, p. 11).

**Figura 22 — Ambiente de Preproducción**

![Ambiente de Preproducción](https://raw.githubusercontent.com/PatricioH315/LafroX/d397c30ff8ad232ec4e3ea02caf5f3cb6800a547/04/figuras/fisica/ambientes/amb_preproduccion.png)

Fuente: elaboración propia.

<a id="fig:amb-preproduccion"></a>

Los pasos de la figura son los siguientes:

- GitLab CI promueve a Preproducción la entrega que superó QA.

- CodeBuild no vuelve a construir: la imagen es la misma de Desarrollo y QA.

- ECR entrega la imagen firmada por su digest.

- Las migraciones aditivas se aplican sobre el escritor de Aurora PostgreSQL (N-05), como un paso único antes de cambiar el tráfico.

- La entrega nueva se despliega al mismo tiempo en dos lugares, por lo que la figura asigna el número 5 a ambos:

- En la VPC 10.102.0.0/16 se ensaya el despliegue azul-verde con canario. La entrega vigente («azul») sigue atendiendo mientras ECS Fargate levanta la nueva («verde») a su lado. El balanceador privado, en dos zonas, le pasa primero a la nueva una parte pequeña del tráfico, llamada canario, y la aumenta por etapas mientras no aparezcan errores. Si aparecen, el tráfico vuelve completo a la entrega vigente.

- En la VPC del sitio emulado, su base local recibe las mismas migraciones aditivas y la imagen `wms_only` recibe la misma entrega mientras el sitio está desconectado. Al reconectarlo, se comprueba que la reconciliación acepta los sobres que dejó la entrega previa.

- Los portales se publican en el bucket S3 privado de Preproducción, que CloudFront sirve.

La VPC del sitio emulado no tiene túnel hacia las bodegas, de modo que ningún ensayo alcanza la operación real.

**Producción**

En Producción la secuencia se ejecuta de forma automática y llega además a los sitios on-premise (Figura [23](LAFROX-Subdocumento4.md#fig:amb-produccion)).

**Figura 23 — Ambiente de Producción**

![Ambiente de Producción](https://raw.githubusercontent.com/PatricioH315/LafroX/d397c30ff8ad232ec4e3ea02caf5f3cb6800a547/04/figuras/fisica/ambientes/amb_produccion.png)

Fuente: elaboración propia.

<a id="fig:amb-produccion"></a>

Los pasos de la figura son los siguientes:

- GitLab CI inicia el paso a producción cuando la entrega superó los controles del pipeline y el ensayo en Preproducción, dentro de las ventanas de la Tabla [14](LAFROX-Subdocumento4.md#tab:jd02).

- CodeBuild no vuelve a construir: la imagen es la misma que se ensayó.

- ECR entrega la imagen firmada por su digest.

- Las migraciones aditivas se aplican sobre el escritor de Aurora PostgreSQL (N-05).

- ECS Fargate aplica en la VPC 10.101.0.0/16, en dos zonas, el mismo despliegue azul-verde con canario que se ensayó en Preproducción: la entrega nueva recibe el tráfico por etapas y, si falla, el tráfico vuelve a la vigente.

- Los portales se publican en el bucket S3 privado de Producción, que CloudFront sirve.

- La entrega llega a los sitios mediante dos acciones que ocurren juntas, por lo que la figura asigna el número 7 a ambas:

- Los sitios descargan la misma imagen desde ECR por la VPN, la VPC Hub y los endpoints de interfaz de la VPC de Producción, en conexiones salientes y sin pasar por Internet.

- Ansible (F-02), desde CD Talca, aplica sitio por sitio las migraciones aditivas a la base PostgreSQL activa: VM-02, VM-C02 y la del E-01 activo. En Concepción y los cross-docking, la réplica sincrónica las lleva al equipo en espera. Luego actualiza los contenedores: VM-01, VM-03 y VM-04 en Talca, VM-C01 y VM-C04 en los dos servidores de Concepción y los dos E-01 de cada cross-docking, primero el equipo en espera y luego el activo.

El paso 7 distingue a Producción de los demás ambientes: es el único que llega a las bodegas.

**Recuperación ante Desastres**

La Figura [24](LAFROX-Subdocumento4.md#fig:amb-recuperacion) muestra las dos rutas de recuperación: ante la pérdida de la región primaria y ante la pérdida de la sala de Talca.

**Figura 24 — Ambiente de Recuperación ante Desastres**

![Ambiente de Recuperación ante Desastres](https://raw.githubusercontent.com/PatricioH315/LafroX/d397c30ff8ad232ec4e3ea02caf5f3cb6800a547/04/figuras/fisica/ambientes/amb_recuperacion.png)

Fuente: elaboración propia.

<a id="fig:amb-recuperacion"></a>

Los pasos de la figura son los siguientes:

- GitLab CI libera la entrega en Producción.

- CodeBuild no vuelve a construir: la imagen es la misma que se liberó en Producción.

- ECR guarda la imagen firmada en sa-east-1.

- ECR replica cada entrega liberada en Producción a us-east-1, y la réplica reducida de ECS Fargate la despliega en la VPC 10.201.0.0/16. Si se pierde la región primaria, esa réplica escala a carga completa en menos de 30 minutos.

- Si se pierde la sala de Talca, el perfil `wms_only` de Talca se levanta en ECS Fargate de la VPC de Producción, sobre la copia del WMS de Talca que AWS DMS mantiene en Aurora PostgreSQL (N-05). El WMS recuperado conserva la identidad de Talca y atiende a los terminales de la bodega por la VPN.

Concepción no depende de esta recuperación: sigue operando su propia bodega.

Las cinco figuras comparten la misma cadena de entrega y la misma imagen firmada, y difieren en la cuenta, el bloque de direccionamiento y el alcance hacia los sitios. Solo Producción llega a las bodegas por la VPC Hub, y Recuperación ante Desastres conserva preparada la réplica reducida de us-east-1 y la recuperación del WMS de Talca en la nube.

El paso de un ambiente a otro lo controla el pipeline de integración continua: GitLab CI lo orquesta y AWS CodeBuild construye cada imagen de forma hermética, con procedencia SLSA nivel 3. Cada cambio instala las dependencias exactamente como las fija `composer.lock` y pasa por estos controles (RT-04.05; Bases Técnicas Transversales, cap. 4, p. 10):

- Auditoría de dependencias con `composer audit` y pruebas PHPUnit.

- Análisis estático con PHPStan y Larastan, y formato con Laravel Pint.

- Pruebas de contrato contra OpenAPI 3.1 y AsyncAPI 2.6.

- Escaneo de secretos y de imágenes de contenedor, y medición de cobertura.

El pipeline bloquea el despliegue ante un hallazgo crítico o alto, ante un contrato público roto sin nueva edición o ante una cobertura de la lógica de negocio inferior al 70 % (RT-04.11; Bases Técnicas Transversales, cap. 4, p. 11). Además aplica la política corporativa de LafroX del Subdocumento 1 (sección 1.3.1): bloquea toda versión con cobertura de pruebas unitarias inferior al 80 %. Son dos métricas distintas, medidas en la misma ejecución del pipeline, y una versión debe superar ambas. Primero, la imagen aprobada se firma, se publica en Elastic Container Registry y se promueve por su digest, de modo que ningún ambiente recompila. El paso a Producción es automático una vez que la imagen supera los controles del pipeline y el ensayo en Preproducción, dentro de las ventanas de la Tabla [14](LAFROX-Subdocumento4.md#tab:jd02) (RT-04.06; Bases Técnicas Transversales, cap. 4, p. 11). Segundo, la configuración no sensible se externaliza por ambiente en SSM Parameter Store y los secretos se gestionan en AWS Secrets Manager con rotación automática (ADR-15, Anexo 4-O). La imagen no contiene secretos ni el archivo de entorno (RT-04.08 y RT-04.09; Bases Técnicas Transversales, cap. 4, p. 11). Tercero, las migraciones de base de datos son migraciones Laravel basales y aditivas, que siguen la estrategia de expandir y contraer: se ejecutan como un paso único del despliegue antes de cambiar el tráfico, cada entrega solo agrega estructuras, de modo que la entrega previa y la nueva de la aplicación funcionan sobre el mismo esquema durante el despliegue, y las estructuras obsoletas se eliminan en una entrega posterior. Cada migración declara además su reversión, de modo que el esquema puede volver a la entrega previa (RT-04.10; Bases Técnicas Transversales, cap. 4, p. 11). Luego, el código reside en un repositorio con ramas protegidas, revisión obligatoria por pares y sin escritura directa sobre la rama principal (RT-04.03; Bases Técnicas Transversales, cap. 4, p. 10).

A Producción no se llega de otra forma: su acceso es restringido y auditado, y los desarrolladores no tienen acceso interactivo directo a ese ambiente (numeral 4.1 de las Bases Técnicas Transversales; Bases Técnicas Transversales, cap. 4, p. 10). El acceso privilegiado excepcional reúne estos controles:

- IAM Identity Center federado con Keycloak por SAML 2.0 y SCIM, y MFA.

- Conjuntos de permisos temporales con aprobación previa y sesiones ECS Exec o Session Manager con registro de comandos y salida.

- SSH y el reenvío de puertos bloqueados.

La cuenta de último recurso (ADR-06, Anexo 4-O) se usa solo ante la indisponibilidad del IdP, con doble custodia, alerta inmediata, rotación de credenciales tras su uso y revisión posterior registrada.

Los portales de clientes, transportistas y proveedores siguen el mismo ciclo: su aplicación Angular se publica por ambiente en S3 privado y CloudFront, con la imagen de aplicación del mismo ambiente como backend. Las consolas Angular, en cambio, corren como contenedor en ECS Fargate tras el balanceador de aplicación privado (N-04).

#### 4.2.4.1.1 Artefacto y perfiles de ejecución

La aplicación se construye una sola vez por entrega como una imagen PHP 8.5 con Laravel 13 que contiene el código, el `vendor` resuelto desde `composer.lock`, PHP-FPM, el intérprete de línea de comandos y las extensiones que la solución usa: `pdo_pgsql`, `mbstring`, `intl`, `openssl`, `opcache`, `curl` para el SDK de AWS, `sockets` para el adaptador AMQP `php-amqplib`, la extensión de OpenTelemetry y `pcntl`, que solo usan los procesos de línea de comandos para terminar de forma ordenada al recibir la señal de detención. Un servidor web liviano acompaña a PHP-FPM en los perfiles HTTP. La misma imagen corre en todos los ambientes y en todos los sitios, y lo que cambia es el perfil con que arranca, como muestra la Tabla [13](LAFROX-Subdocumento4.md#tab:perfiles). Cada perfil se despliega y revierte por separado, por lo que un componente crítico cambia de entrega sin detener a los demás (RT-02.02; Bases Técnicas Transversales, cap. 2, p. 6).

<a id="tab:perfiles"></a>

**Tabla 13 — Perfiles de ejecución del artefacto Laravel**

| **Perfil** | **Proceso y función** | **Dónde corre** | **Escala por** |
| --- | --- | --- | --- |
| API | Servidor web y PHP-FPM con las APIs de M1–M12 para portales, preventa y reparto | N-04, ECS Fargate en 2 zonas | Procesos PHP-FPM ocupados sobre 70 %, de 2 a 4 tareas y techo de 8 |
| `wms_only` | Servidor web y PHP-FPM con M1, M2, M5, la función local de bloqueo de M9 y la recepción física de retornos de M8, con la puerta de API local | VM-01, VM-C01 y E-01 | Fijo, dimensionado al sitio |
| Shipper | PHP CLI que lee RabbitMQ con `php-amqplib`, publica sobres JSON en las colas FIFO de reconciliación y de solicitudes al ERP, fuera de Talca, recibe las respuestas de su sitio y lee la cola de coordinación de reservas de su sitio | VM-03, VM-C04 y E-01 | Uno activo por sitio |
| Consumidor de reconciliación | PHP CLI con el SDK de AWS que aplica los sobres al estado central | N-04, ECS Fargate | Edad del mensaje más antiguo, de 2 a 4 tareas |
| Trabajos | PHP CLI con el trabajador de colas de Laravel, con notificaciones y EDI en colas separadas | N-04, ECS Fargate | Profundidad de cada cola, de 2 a 4 tareas |
| `erp-sync` | PHP CLI que consume RabbitMQ local y, por conexión saliente, la cola FIFO de solicitudes al ERP, y emite mediante A-04 | VM-04, Talca | Dos procesos fijos |
| Planificador | PHP CLI para las tareas periódicas del ambiente | N-04, una sola tarea por ambiente | No escala |

Fuente: elaboración propia.

Los perfiles comparten la revisión de código y el esquema de datos, pero cada uno tiene su propio rol de IAM o credencial local, con solo los permisos que su función necesita: el perfil de API no puede leer la cola de reconciliación, el consumidor no puede escribir en las colas de trabajos, el shipper solo puede enviar a las colas de reconciliación y de solicitudes al ERP y leer la respuesta y la coordinación de reservas de su sitio, y `erp-sync` es el único lector de las solicitudes al ERP. El planificador corre como una sola tarea por ambiente, con despliegue que detiene la tarea en ejecución antes de iniciar la nueva, y cada tarea periódica toma además un bloqueo en la base de datos para impedir ejecuciones superpuestas. Los sitios no ejecutan planificador: sus procesos permanentes son el servidor del WMS y el shipper, además de `erp-sync` en VM-04 de Talca. En los centros de distribución, el perfil `wms_only`, que es el Motor WMS A-01, corre como contenedor en VM-01 y VM-C01, y el shipper corre junto al broker de colas A-03, RabbitMQ, en VM-03 y VM-C04, todos sobre las máquinas virtuales de Proxmox. En cada cross-docking, el perfil `wms_only` y el shipper se orquestan con Docker Compose en E-01, junto a PostgreSQL, RabbitMQ y la caché de identidad. En Concepción y en cada cross-docking, el equipo en espera mantiene detenidos el WMS y el shipper; solo ejecuta la réplica de PostgreSQL, la caché de identidad y el colector de observabilidad hasta que toma el control. Los sitios descargan la imagen desde Elastic Container Registry por la VPN, a través de la VPC Hub, y los endpoints de interfaz de la VPC de Producción, en conexiones salientes y sin tráfico por Internet. Ansible (F-02), con el que se declara como código la configuración de los cinco sitios, actualiza sus contenedores sitio por sitio. Elastic Container Registry replica cada imagen liberada de sa-east-1 a us-east-1 mediante replicación entre regiones, de modo que la réplica reducida y la plataforma promovida en una conmutación usan el mismo digest sin depender del registro primario. En us-east-1, la infraestructura como código deja creadas y vacías las colas SQS FIFO y SQS, y los temas SNS equivalentes, a las que se redirigen los shippers y `erp-sync` durante la conmutación. Fuera de la imagen Laravel quedan el frontend Angular de las consolas, el motor de rutas M4 y el transporte AS2 M11, los tres en contenedores propios sobre ECS Fargate (N-04) y construidos por el mismo pipeline. M11 opera tras contratos versionados (ADR-11, Anexo 4-O).

El transporte AS2 y el frontend de consolas mantienen dos tareas cada uno, distribuidas entre dos zonas de disponibilidad (RT-03.02; Bases Técnicas Transversales, cap. 3, p. 8). El motor de rutas ejecuta una tarea por corrida. Si falla, ECS la relanza en otra zona y repite la corrida dentro de la planificación de 15:00 a 18:30, y la prueba de aceptación mide el plazo de 20 min por corrida.

Cada perfil cumple este ciclo de vida:

- Arranque y compatibilidad de esquema: el contenedor verifica la edición esperada y no acepta tráfico ni mensajes si no coincide.

- Comprobación de salud: los perfiles HTTP exponen una ruta de salud de proceso, que usa el balanceador, y otra de disponibilidad que comprueba la base y la cola. Los procesos de línea de comandos informan su salud por un latido que vigila el orquestador.

- Detención y drenaje: el balanceador deja de enviar solicitudes nuevas y espera 30 segundos a que terminen las vigentes. Los trabajadores reciben la señal de detención, terminan el mensaje en curso sin tomar otro y salen antes de 120 segundos, plazo mayor que el tiempo máximo de un trabajo. El mensaje no confirmado vuelve a la cola al vencer su visibilidad.

Así, ningún reinicio, escalado o despliegue deja un trabajo a medias.

#### 4.2.4.1.2 Liberación y reversión

Cada entrega se libera con estrategia azul-verde: la entrega nueva se despliega junto a la vigente y recibe tráfico de forma gradual, en etapas de canario, después de haberse demostrado el mismo procedimiento en Preproducción (RT-04.07; Bases Técnicas Transversales, cap. 4, p. 11). La puesta en producción avanza por proceso, por sitio o por zona comercial, nunca como un evento único que afecte a la vez a la bodega, la preventa, el reparto y la facturación. En la sustitución del WMS de 2013 por olas, cada capacidad se activa además por sitio mediante indicadores de funcionalidad (*feature flags*), sin volver a desplegar. Revertir una ola devuelve el tráfico a la entrega previa del nuevo servicio. El WMS de 2013 ya no escribe stock y se retira al cerrar la marcha blanca de Talca.

Mientras dura el canario, la entrega previa permanece desplegada, por lo que revertir es devolverle el tráfico, sin recompilar ni volver a desplegar. La reversión es automática y se dispara cuando el percentil 95 de una transacción supera su umbral comprometido (Tabla [31](LAFROX-Subdocumento4.md#tab:t84)) o cuando la entrega nueva registra más errores que la estable en la misma ventana de observación. No se pierde ninguna transacción confirmada: las operaciones en curso quedan en los buffers locales, 24 horas por sitio en el broker y la caché de turno en los dispositivos, y se reprocesan de forma idempotente contra la entrega restituida. El esquema no necesita revertirse durante el canario, porque la migración de la entrega solo agregó estructuras. Si hiciera falta, la reversión declarada de la migración lo devuelve a la entrega previa. La reversión cambia la imagen en servicio sin perder operaciones. El tiempo efectivo de reversión se mide en cada ensayo en Preproducción y tiene como objetivo 4 horas, el mismo valor del tiempo medio de restauración de incidentes críticos que el Artículo 78.3 mide cada mes (Bases Administrativas, art. 78.3, p. 40).

Si la falla de un despliegue se manifestara durante la ventana de despacho, la bodega y el reparto continuarían con su operación local (Tabla [10](LAFROX-Subdocumento4.md#tab:t29)) mientras se revierte, sin detener la salida de los camiones.

Cada promoción ensaya además la compatibilidad de los mensajes retenidos. Un sitio puede volver de un corte de 24 horas con sobres publicados por la entrega previa, de modo que el consumidor de reconciliación acepta la edición vigente y la inmediatamente previa del sobre JSON, y rechaza hacia la cola de mensajes fallidos cualquier edición que no reconozca, sin aplicarla. Preproducción reproduce ese caso —sitio emulado desconectado, promoción de la entrega nueva y reconexión— antes de cada paso a producción.

#### 4.2.4.1.3 Transición al backend Laravel

La arquitectura lógica fija la implantación progresiva del backend (apartado 4.1). Su secuencia física es la siguiente:

- Se registran los contratos OpenAPI y AsyncAPI, el sobre JSON, el esquema PostgreSQL de destino definido por el modelo de datos de la solución, que es la línea base de las migraciones Laravel, y el extracto conciliado del WMS de 2013 de Talca.

- Se construye el backend y se prueban las colas y la capa anticorrupción con fallas inducidas: corte de enlace, ERP caído, mensajes duplicados y fuera de orden.

- Se habilita un sitio piloto, dimensionado por su capacidad real, y el WMS de 2013 deja de escribir cada capacidad que se migra. El tráfico se migra por olas con un único escritor autorizado para cada operación. Nunca escriben a la vez el sistema de origen y el nuevo sobre el stock, los cobros o los documentos tributarios.

- Antes de cada corte se drenan los mensajes que el sistema nuevo no puede leer. Si algún ambiente conservara mensajes serializados por un framework de origen, se drenan o se transforman al sobre JSON antes del corte, porque Laravel no puede consumirlos.

- Cada ola cierra verificando saldos de stock, cobros y folios contra el extracto del origen, y se revierte por sitio si falla un umbral acordado con el CLIENTE.

- La reversión devuelve el tráfico a la entrega previa del nuevo servicio solo después de detener la nueva, conciliar los mensajes retenidos y comprobar que el esquema sigue legible por la entrega previa. No reactiva el WMS de 2013 como escritor.

#### 4.2.4.1.4 Calendario y cadencia

El calendario de Puelche limita cuándo se puede intervenir la plataforma. El caso prohíbe intervenir los sistemas entre el 1 y el 25 de septiembre, en diciembre y durante el cierre contable de cada mes, prohíbe el paso a producción en todo septiembre y en diciembre, y exige indisponibilidad cero en la ventana de despacho (Bases Técnicas del caso, cap. 10, restricción 8, p. 19, y Cap. 13, p. 23; RT-10.05 y RT-10.06; Bases Técnicas Transversales, cap. 10, p. 22; Bases Técnicas del caso, cap. 15, p. 27). La Tabla [14](LAFROX-Subdocumento4.md#tab:jd02) cruza cada período con lo que admite.

<a id="tab:jd02"></a>

**Tabla 14 — Ventanas de despliegue**

| **Período** | **Despliegue** | **Indisponibilidad programada** |
| --- | --- | --- |
| Todo septiembre, sin intervención alguna del 1 al 25 | No | No |
| Todo diciembre | No | No |
| Tres primeros días hábiles del mes | No | No |
| 05:30–07:00, lunes a sábado | No | No |
| 22:00–06:00, preparación de pedidos | Sí, sin interrupción | No |
| 08:00–18:00, recepción de proveedores | Sí, sin interrupción | No |
| Resto del calendario | Sí, sin interrupción | Excepcional, con aviso de 10 días hábiles |

Fuente: elaboración propia a partir de las Bases Técnicas del caso (cap. 10, p. 19).

El despliegue sin interrupción es, por lo tanto, la regla y no una capacidad opcional: solo fuera de las ventanas protegidas se admite una indisponibilidad programada, y únicamente por excepción. En la ventana nocturna, además, toda intervención en bodega considera el turno de preparación. Descontados los congelamientos, quedan unos diez meses desplegables al año, de los que se excluyen los tres primeros días hábiles de cada mes. Sobre ese margen se fija una cadencia quincenal de despliegue y un tiempo de hasta cinco días hábiles desde que se confirma un cambio de código hasta que llega a producción, compatible con el plazo de siete días corridos para remediar una vulnerabilidad crítica (Artículo 21.1 de las Bases Administrativas (art. 21.1, p. 15); RT-11.04; Bases Técnicas Transversales, cap. 11, p. 23). La tasa de cambios fallidos no supera el 5 % de los despliegues del mes y el tiempo de restauración no supera 4 horas, conforme al Artículo 78.3 de las Bases Administrativas (art. 78.3, p. 40). Estas cuatro métricas se miden durante la Operación (RT-04.12; Bases Técnicas Transversales, cap. 4, p. 11). Las correcciones de incidentes críticos usan el mismo pipeline, con prioridad y fuera de la cadencia quincenal, dentro del plazo de resolución de 4 horas. Cada servicio crítico tiene como presupuesto de error el complemento de su disponibilidad comprometida de 99,9 % mensual, unos 43 minutos al mes. Si un servicio lo consume, se suspenden en él los despliegues que no sean correctivos hasta el mes siguiente (RT-10.09; Bases Técnicas Transversales, cap. 10, p. 22).

### 4.2.4.2 Red de despliegue

<a id="sub:2-redes-topologia-segmentacion-y-conectivi"></a>

La sección de conexiones describe los caminos entre los sitios, el terreno y la nube, y su conmutación (Tabla [18](LAFROX-Subdocumento4.md#tab:conexiones)). El despliegue agrega tres definiciones sobre esa red: dónde llegan los túneles, cómo se reparte el direccionamiento y cómo se dirige el tráfico entre regiones.

Los túneles de AWS Site-to-Site VPN de los cinco sitios llegan a la VPC Hub de sa-east-1, donde el Transit Gateway los une solo a la VPC de Producción. La región us-east-1 dispone de su propio Transit Gateway y de su VPN para reconectar los sitios durante una conmutación. La de Producción es la única VPC con enlace hacia los sitios, coherente con que el on-premise es producción: Desarrollo, QA y Preproducción no tienen conectividad con las bodegas, de modo que un error en un ambiente de prueba no puede alcanzarlas. El direccionamiento se asigna sin solapamiento, según la Tabla [15](LAFROX-Subdocumento4.md#tab:t64), y el bloque de recuperación 10.201.0.0/16 corresponde al ambiente de Recuperación ante Desastres de la Tabla [12](LAFROX-Subdocumento4.md#tab:t62).

<a id="tab:t64"></a>

**Tabla 15 — Direccionamiento y segmentación**

| **Dominio** | **Bloque** | **Segmentación** |
| --- | --- | --- |
| Talca | 10.1.0.0/16 | VLAN de gestión, servidores, operación, estaciones e IoT |
| Concepción | 10.2.0.0/16 | Mismas VLAN que Talca |
| Cross-docking | 10.3.0.0/16 a 10.5.0.0/16 | VLAN de gestión y de operación tras el par de firewalls del sitio, por la VPN |
| Sitios adicionales previstos | 10.6.0.0/16 y 10.7.0.0/16 | Reservados |
| VPC Hub de conectividad, sa-east-1 | 10.100.0.0/16 | Transit Gateway y terminación VPN de los cinco sitios |
| VPC Producción, zona pública | 10.101.1.0/24 y 10.101.2.0/24 | NAT y Network Load Balancer del canal AS2 |
| VPC Producción, zona privada | Resto de 10.101.0.0/16 | ALB de aplicación y consolas, aplicación y datos, enlazada a los sitios por el Transit Gateway de la VPC Hub |

Fuente: elaboración propia.

Cada sitio con cómputo dispone de un bloque propio. La séptima instalación que el caso proyecta a tres años y el centro de distribución que Puelche evalúa abrir hacia 2030 en la Región de Los Lagos tienen reservados 10.6.0.0/16 y 10.7.0.0/16, de modo que su incorporación es una parametrización de la infraestructura como código (RT-02.12; Bases Técnicas Transversales, cap. 2, p. 7; Bases Técnicas del caso, cap. 15, p. 26). En la nube, los ALB de aplicación y consolas son privados, y la subred pública solo aloja NAT y el Network Load Balancer del canal AS2. Los portales residen en S3 privado, servido únicamente por CloudFront. La VPC de Producción usa endpoints de interfaz execute-api, IoT Core, SQS, SSM y Elastic Container Registry, y endpoints de puerta de enlace para DynamoDB y S3. Como los de puerta de enlace no son alcanzables desde los sitios por la VPN, los sitios descargan la imagen por el endpoint de interfaz de Elastic Container Registry y por un endpoint de interfaz de S3, donde se almacenan las capas de las imágenes, sin salir a Internet.

El tráfico externo sigue las entradas de la sección [4.2.5.2](LAFROX-Subdocumento4.md#sub:superficie). Route 53 cambia el tráfico regional después de la autorización del CLIENTE, la promoción de Aurora, la restitución de la identidad, las API pública y privada y Verified Access, y la validación funcional. Luego se reconectan la VPN y los brokers (Tabla [39](LAFROX-Subdocumento4.md#tab:4-3-6)).

La red también debe devolver a la normalidad a un sitio que operó desconectado. El compromiso es resincronizar la flota en hasta 10 minutos y un centro de distribución en hasta 2 horas después de un corte de 24 horas (Tabla [10](LAFROX-Subdocumento4.md#tab:t29)). Un corte de 24 horas acumula los cambios de la base con su registro de escritura anticipada, el vaciado del broker, la telemetría, la observabilidad y el incremental de respaldo: unos 1,68 GB en Talca, 1,29 GB en Concepción y 0,32 GB en cada cross-docking, que se drenan en 2 horas con 1,87, 1,44 y 0,35 Mbps, respectivamente (Tabla [27](LAFROX-Subdocumento4.md#tab:t81); Anexo 4-W). La evidencia de entrega no se suma al drenaje, porque durante el corte del centro de distribución el terminal la envía por la red celular. Las reservas de capacidad y la prioridad de cada camino se detallan en la Tabla de ancho de banda de 4.2.6. La operación de bodega conserva su autonomía mientras se drenan los mensajes. Al reconectar, la calidad de servicio prioriza el broker y el registro de escritura anticipada sobre la telemetría.

### 4.2.4.3 Alta disponibilidad

<a id="sub:3-alta-disponibilidad"></a>

No todos los servicios necesitan el mismo nivel de continuidad. El Artículo 78 (Bases Administrativas, art. 78.2, p. 40) fija cuatro niveles de servicio, y la solución asigna cada servicio a uno según el efecto de su indisponibilidad sobre la operación (RT-10.02; Bases Técnicas Transversales, cap. 10, p. 22), como muestra la Tabla [16](LAFROX-Subdocumento4.md#tab:jd05).

<a id="tab:jd05"></a>

**Tabla 16 — Clasificación de servicios por nivel de servicio**

| **Nivel** | **Disponibilidad** | **Resolución** | **Servicios** |
| --- | --- | --- | --- |
| Crítico | 99,9 % | 4 h | Preparación y despacho con emisión de la guía requerida por un cambio de carga en la ventana de 05:30 a 07:00, con el bloqueo por excursión térmica y la identidad de bodega que lo habilitan |
| Alto | 99,5 % | 8 h | Toma de pedido de preventa y consulta de stock y crédito, entrega y evidencia de entrega, planificación de rutas, otros documentos tributarios, integración con el ERP, cobranza y rendición, y registro de temperatura |
| Medio | 99,0 % | 24 h | Canal moderno (EDI), notificaciones, analítica y tableros, portales, consultas de geolocalización y registros de auditoría y seguridad |
| Bajo | 98,0 % | 48 h | Reportería e informes a pedido |

Fuente: elaboración propia a partir de las Bases Administrativas (art. 78.2, p. 40).

El plazo de 4 h de la guía nueva supone el ERP disponible. Si se pierde la sala de Talca, la guía nueva espera que el CLIENTE restituya el servidor del ERP. Mientras tanto, solo sale la carga amparada por su guía preemitida (sección [4.3.2.5](LAFROX-Subdocumento4.md#sub:conmutacion-regional)).

Las clases de servicio se distinguen por su alternativa operativa:

- Crítico: detiene un proceso sin alternativa. La ventana de despacho de 05:30 a 07:00 no admite ejecución manual, la nueva guía por un cambio de carga se emite antes de salir y el bloqueo por excursión térmica y la identidad de bodega condicionan la salida.

- Alto: tiene una alternativa costosa. La toma de pedido, la entrega y la consulta de stock y crédito siguen siendo transacciones críticas en desempeño (Tabla [31](LAFROX-Subdocumento4.md#tab:t84)), pero el dispositivo las captura sin conexión durante un turno completo y las sincroniza al reconectar. La ruta puede planificarse a mano en 3,5 horas y las transacciones hacia el ERP distintas de la guía de la ventana de despacho se retienen en cola hasta 24 horas.

- Medio: dispone de una alternativa operativa.

- Bajo: no impide operar.

El compromiso penalizable del 99,9 % recae sobre la preparación y el despacho, que se ejecutan contra la base local del centro de distribución sin atravesar la WAN, y sobre la identidad, cuya autoridad reside en la nube y se sostiene con el despliegue en varias zonas de disponibilidad (apartado 4.3.1.2).

Esa es la razón por la que el 99,9 % de extremo a extremo no depende de multiplicar las disponibilidades de la infraestructura. El numeral 7.2 de las Bases Técnicas Transversales (cap. 7, p. 17) fija un mínimo de 99,95 % mensual para la energía, la climatización, la red, el cómputo, la base de datos y los portales, pero esos valores son pisos por subsistema y su producto en serie quedaría por debajo del 99,9 %. El compromiso se sostiene en la redundancia interna de cada subsistema y en la ruta que sigue cada transacción. La confirmación de preparación, la más estricta, se ejecuta contra la base local del centro de distribución y no atraviesa la WAN ni la nube. Descansa sobre energía y climatización en N+1, un par de firewall en alta disponibilidad, dos switches en stack, un clúster de tres nodos N+1 y almacenamiento Ceph con tres réplicas en NVMe sin RAID, con un solo elemento en serie, la instancia de escritura VM-02, que se reinicia en otro nodo del clúster (Tabla [20](LAFROX-Subdocumento4.md#tab:fallas-sitios)). La identidad, por su parte, se sostiene en la nube con Keycloak (A-05) en dos zonas y, en cada sitio, con la caché de solo lectura y el verificador local de relevo de turno.

En Concepción y en cada cross-docking, la misma confirmación se ejecuta en un par de equipos idénticos, uno activo y otro en espera, conforme a RT-03.14 (Bases Técnicas Transversales, cap. 3, p. 9). Concepción usa dos servidores Proxmox independientes: el activo ejecuta VM-C01 a VM-C04 y el otro, sus copias. Cada cross-docking usa dos mini-PC E-01. El mecanismo es el mismo en los cuatro sitios:

- PostgreSQL del equipo activo replica cada transacción en forma sincrónica al de espera, de modo que una transacción confirmada existe en los dos equipos.

- Si el activo falla, el de espera promueve su base y toma la dirección virtual del sitio con keepalived (VRRP). Los terminales siguen trabajando contra la misma dirección y el sitio vuelve a operar en menos de un minuto.

- Para que no haya dos equipos activos, el de espera se promueve solo si deja de ver al activo por sus dos interfaces, conectadas a switches distintos.

- Al tomar el control, el equipo vuelve a publicar desde el outbox replicado los eventos de las últimas 24 horas, y la nube descarta por UUID los que ya recibió.

- Si falla el equipo en espera, la replicación pasa a asíncrona y se genera una alerta, para que el activo no se detenga. El equipo dañado se repone y se resincroniza desde el activo.

Solo la pérdida simultánea de los dos equipos obliga a reconstruir la base del sitio desde el estado central (Tabla [20](LAFROX-Subdocumento4.md#tab:fallas-sitios)).

En la nube, todos los servicios con requisito de alta disponibilidad operan en al menos dos zonas (RT-03.02; Bases Técnicas Transversales, cap. 3, p. 8):

- Aurora PostgreSQL (N-05) escribe en sa-east-1a y mantiene un lector promovible en sa-east-1b, al que conmuta en menos de 30 segundos.

- ElastiCache mantiene primario y réplica entre esas zonas y conmuta en menos de 60 segundos.

- Las tareas de ECS Fargate se distribuyen en ambas zonas y se reprograman solas ante la pérdida de una.

- DynamoDB, el balanceador y los NAT Gateway son multizona por diseño.

Estos tiempos corresponden a los que AWS declara como habituales para cada servicio y se tratan como objetivos que se miden en las pruebas de la sección [4.2.4.6](LAFROX-Subdocumento4.md#sub:6-verificacion-de-la-continuidad). Ante el peak de septiembre, el escalamiento automático y la degradación controlada del apartado de dimensionamiento sostienen los umbrales de desempeño sin intervención.

### 4.2.4.4 Recuperación ante desastres

<a id="sub:4-recuperacion-ante-desastres-ba-art-20-rt"></a>

La recuperación ante desastres es activo-pasiva en caliente: la región us-east-1 mantiene una réplica reducida pero funcional de la plataforma, escalable a carga completa en menos de 30 minutos, que se promueve solo cuando se pierde la región primaria. Los objetivos son un RTO de hasta 4 horas y un RPO de hasta 15 minutos para los servicios críticos (RT-07.04; Bases Técnicas Transversales, cap. 7, p. 17). Cada dominio de datos alcanza ese RPO con su propio mecanismo de replicación (Tabla [37](LAFROX-Subdocumento4.md#tab:4-3-4)): Aurora Global Database mantiene en us-east-1 la réplica promovible de la base en nube, DynamoDB Global Tables la telemetría, y la replicación de S3 entre regiones lleva la evidencia, los documentos y las copias de AWS Backup (N-11).

Si Talca pierde fibra y LTE, Starlink D-06, mantenido en espera caliente con el túnel IPsec establecido y BGP de menor preferencia, sostiene la lectura continua de AWS DMS sobre VM-02 y el envío de eventos críticos. La operación local conserva al menos 24 horas de autonomía. El límite residual del RPO y sus mitigaciones se exponen en 4.3.2, bajo «RPO y RTO». El registro retenido se acota con un tope de 5 GB por slot, frente a los unos 0,123 GB diarios de registro de escritura anticipada que estima el dimensionamiento para Talca: cubre con amplio margen un corte de 24 horas y ocupa como máximo la cuarta parte de los 20 GB actuales de VM-02, que crecen a 31 GB a 3×, sin arriesgarlo (Anexo 4-W). El retraso de replicación y el tamaño del registro retenido se miden de forma continua y generan alarma a los 5 y a los 15 minutos de retraso.

La réplica por DMS y la reconciliación por eventos cumplen funciones distintas y no se mezclan. DMS copia las tablas del WMS de Talca (VM-02) a un esquema de réplica de solo lectura en Aurora, que sirve a la continuidad y a las consultas. Concepción y los cross-docking no replican sus bases por DMS: publican sus eventos mediante los brokers y SQS FIFO. El consumidor de reconciliación aplica esos sobres JSON a las tablas de dominio del estado central —stock consolidado, trazabilidad de lotes, pedidos, entregas y cobros—, y en la misma transacción registra la clave de origen del evento, formada por el sitio y el identificador único que el evento trae desde su captura. Una restricción de unicidad sobre esa clave impide aplicar dos veces el mismo evento, aunque SQS lo entregue de nuevo o llegue después de la ventana de deduplicación de la cola. Ninguna tabla de dominio se alimenta de la réplica DMS, y ningún evento escribe en el esquema de réplica.

#### 4.2.4.4.1 Conmutación y retorno

La conmutación de región y el retorno siguen el procedimiento de la sección [4.3.2.5](LAFROX-Subdocumento4.md#sub:conmutacion-regional) (Tabla [39](LAFROX-Subdocumento4.md#tab:4-3-6)): la promoción de la base exige la autorización del CLIENTE y el enrutamiento hacia us-east-1 cambia después de la validación funcional. El retorno se ejecuta de forma coordinada tras la reconciliación. Si la contingencia afecta solo a la sala de Talca, su WMS se levanta en Fargate sobre su copia en Aurora de la región activa. Los dominios de recuperación y sus amenazas comunes se analizan en la Tabla [36](LAFROX-Subdocumento4.md#tab:4-3-3).

#### 4.2.4.4.2 Operación durante una contingencia regional

Mientras la región primaria no está disponible, la bodega y el terreno siguen operando contra sus bases locales y sus dispositivos. Tras la autorización del CLIENTE, la plataforma se promueve en us-east-1 y recupera las transacciones en nube. La analítica se recupera después desde su copia diferida, y las consultas de geolocalización de personas, excluidas de us-east-1 por diseño (sección [4.3.2](LAFROX-Subdocumento4.md#sec:e-especificaciones-del-sitio-secundario-y-)), esperan el retorno. Ninguna es un servicio crítico.

### 4.2.4.5 Respaldos

<a id="sub:5-respaldos-esquema-3-2-1-1-0-rnf-20-07"></a>

El respaldo protege contra lo que las réplicas replican: un dato borrado por error, corrompido o cifrado de forma maliciosa. La solución aplica el esquema 3-2-1-1-0 exigido para la nube y el on-premise, con una copia inmutable (RT-07.09; Bases Técnicas Transversales, cap. 7, p. 18). Mantiene tres copias en dos medios, base de datos y almacenamiento de objetos:

- Los datos activos.

- Una segunda copia, formada por las instantáneas de Aurora y, para el WMS de Talca, por la copia local D-05.

- El respaldo exportado a S3.

Una copia está fuera del sitio, replicada a us-east-1 por AWS Backup (N-11) y la replicación de S3, y otra es inmutable, en S3 Object Lock en modo Compliance con AWS Backup Vault Lock. El cero corresponde a los errores de verificación de restauración: cada mes se restaura una muestra rotativa que recorre todos los dominios de la Tabla [17](LAFROX-Subdocumento4.md#tab:jd12), se mide el tiempo efectivo de restauración y todo error se corrige antes de la verificación siguiente (RT-07.12; Bases Técnicas Transversales, cap. 7, p. 18).

La copia inmutable es el control frente a un ataque con credenciales administrativas comprometidas: en modo Compliance, ni un administrador ni la cuenta raíz pueden borrarla ni modificarla durante su retención, y el bloqueo de la bóveda, con 3 días de enfriamiento y una retención mínima de 35 días, igual a la menor retención de la Tabla [17](LAFROX-Subdocumento4.md#tab:jd12), impide eliminar los respaldos una vez activado (RT-07.11; Bases Técnicas Transversales, cap. 7, p. 18). La copia local D-05 cumple otra función: es la copia de recuperación rápida, cifrada con una clave independiente de la de producción, que permite restaurar el WMS en hasta 4 horas sin depender del enlace, y por eso no se cuenta como la copia inmutable. Un medio físico cifrado se rota además cada semana a una bóveda externa, y se conserva en el recinto de custodia declarado en el Formulario T-11 hasta su traslado.

La Tabla [17](LAFROX-Subdocumento4.md#tab:jd12) muestra, para cada dominio de datos, con qué frecuencia se respalda, cuánto tiempo se retiene y en cuánto tiempo se restaura por completo (RT-07.13; Bases Técnicas Transversales, cap. 7, p. 18).

<a id="tab:jd12"></a>

**Tabla 17 — Respaldo y restauración por dominio de datos**

| **Dominio** | **Frecuencia** | **Retención** | **Restauración** |
| --- | --- | --- | --- |
| Transaccional de bodega | Continua, con copia local D-05 en Talca y, en Concepción y los cross-docking, reconstrucción desde el estado central | 35 días | ≤ 4 h |
| Transaccional en nube | Diaria y recuperación continua | 35 días | ≤ 4 h |
| Identidad | Diaria y recuperación continua | 35 días | ≤ 4 h |
| Trazabilidad sanitaria | Continua | Vida útil + 6 meses, mínimo 5 años | < 2 h |
| Registros de temperatura | Diaria y continua | 5 años | ≤ 8 h |
| Evidencia de entrega | Continua con versionado | 6 años | ≤ 8 h |
| Respaldo de documentos tributarios | Continua con versionado | 6 años | ≤ 8 h |
| Geolocalización de personas | Continua | 12 meses | ≤ 24 h |
| Registros de seguridad y auditoría | Continua | 7 años | ≤ 24 h |

Fuente: elaboración propia.

Cada tiempo de restauración corresponde al plazo de resolución que el Artículo 78.2 de las Bases Administrativas (art. 78.2, p. 40) asigna al servicio más crítico que usa el dato: la base transaccional en nube se restaura en 4 horas porque sostiene también la identidad, que es crítica, porque Keycloak guarda en Aurora sus datos (ADR-06, Anexo 4-O). La trazabilidad sanitaria es la única excepción más exigente: se restaura en menos de 2 horas, porque ese es el plazo en que Puelche debe responder un retiro sanitario (Bases Técnicas del caso, cap. 18, p. 34). Las retenciones cumplen o superan las del caso. La restauración, además, puede ser parcial: la recuperación de Aurora a un instante específico, sobre una instancia temporal, permite restituir un registro, una tabla, un módulo o el sistema completo sin intervenir el ambiente productivo (RT-07.14; Bases Técnicas Transversales, cap. 7, p. 18).

AWS Backup aplica a Aurora y DynamoDB los respaldos y la recuperación a un instante específico, mientras S3 aporta versionado, Object Lock y réplica entre regiones para los documentos legales. Object Lock protege también los registros de seguridad y auditoría. Los plazos y las retenciones por dominio constan en la Tabla [17](LAFROX-Subdocumento4.md#tab:jd12).

### 4.2.4.6 Verificación de la continuidad

<a id="sub:6-verificacion-de-la-continuidad"></a>

Los mecanismos descritos se verifican con pruebas periódicas. Antes de cada paso a producción, y al menos una vez por semestre durante la Operación, se inyectan la caída de una instancia, de una zona, del equipo activo de Concepción o de un cross-docking, o de una dependencia externa, la latencia elevada y la saturación de disco (RT-10.07; Bases Técnicas Transversales, cap. 10, p. 22), y se comprueban las resoluciones de las Tablas [20](LAFROX-Subdocumento4.md#tab:fallas-sitios) y [21](LAFROX-Subdocumento4.md#tab:fallas-nube). La conmutación regional se ensaya dos veces al año con escrituras de pedidos y sincronización en us-east-1, y el RTO y el RPO medidos deben cumplirse en el 100 % de los ensayos (Bases Administrativas, art. 78.3, p. 40). Con la misma frecuencia se ensaya la pérdida completa de la sala de Talca, distinta del corte de enlace, levantando su WMS en la nube sobre la copia en Aurora, y los respaldos se restauran mensualmente. Las pruebas se programan fuera de la ventana de despacho y producen un informe de resultados con el plan de corrección de las brechas detectadas (RT-07.07; Bases Técnicas Transversales, cap. 7, p. 17). El plan de continuidad del negocio se elabora conforme a ISO 22301, y la continuidad TIC se estructura conforme a ISO/IEC 27031, articulada con el plan de recuperación ante desastres de esta sección (RT-10.03 y RT-10.04; Bases Técnicas Transversales, cap. 10, p. 22).

La aplicación se instrumenta con OpenTelemetry para PHP y Laravel. Además de las métricas de infraestructura, cada perfil publica señales agrupadas por ámbito:

- Aplicación: procesos PHP-FPM ocupados, solicitudes en espera y reinicios de contenedor.

- Colas: profundidad y edad del mensaje más antiguo por cola y por grupo, y mensajes en las colas de fallidos.

- Integraciones: latencia de la capa anticorrupción y del ERP.

- Base de datos: latencia de escritura de VM-02.

El `transaction_id` viaja en las cabeceras HTTP, en las propiedades de los mensajes de RabbitMQ, en los atributos de los mensajes de SQS y en las llamadas a la capa anticorrupción, de modo que una misma traza une la entrega, su evidencia, la guía de despacho y el acuse del ERP. Estas señales disparan el escalado y las alarmas declaradas en el dimensionamiento.

La disponibilidad efectiva de cada servicio, las métricas del proceso de despliegue y el resultado de estas pruebas se miden sobre la plataforma de observabilidad y se entregan en el informe mensual de nivel de servicio (Bases Administrativas, art. 79, p. 40). Es ahí donde el CLIENTE puede comprobar que lo que declara esta sección se cumple.

## 4.2.5 Conexiones, puntos de falla y contingencia

<a id="sec:conexiones"></a>

Esta sección describe cómo se conectan los sitios, el terreno y la nube, identifica cada punto donde esa conexión o su infraestructura puede fallar, y declara cómo se resuelve cada falla o, cuando no se resuelve de forma automática, cuál es la contingencia. Su punto de partida es el caso: la conectividad actual de Puelche se corta con frecuencia y en algunos lugares no existe, por lo que la solución no puede suponer un enlace disponible y debe decir, para cada conexión, qué pasa cuando no lo está.

### 4.2.5.1 Conexiones entre sitios, terreno y nube

Los dos dominios fijos, la nube y el on-premise, se conectan por túneles VPN IPsec que terminan en el par de firewalls de cada sitio (D-01) y en el Transit Gateway de AWS en sa-east-1, con enrutamiento dinámico BGP. Cada sitio publica sus eventos directamente a la nube y opera sin conexión con los sistemas de otra instalación. Los caminos de acceso se distribuyen así:

- Cada centro de distribución tiene tres caminos independientes: fibra D-03, LTE D-04 y Starlink D-06. Starlink permanece en espera caliente, con el terminal encendido, el túnel IPsec establecido y BGP de menor preferencia; solo toma el tráfico cuando fallan fibra y LTE y entonces prioriza DMS/WAL de Talca, broker y outbox, guías hacia ERP y SII, identidad y telemetría crítica.

- Cada cross-docking usa Starlink como camino principal y LTE de dos proveedores como respaldo.

El terminal satelital de los centros permanece encendido porque adquirir satélites y negociar el túnel durante una falla tardaría minutos; el plan de tarifa plana no agrega costo por mantenerlo encendido.

Los terminales EC55 y TC58e acceden por red celular a CloudFront, cuyas rutas `/v1` y `/sync/v1` llegan a la API REST pública.

Los flujos principales son las entradas HTTPS de usuarios externos por CloudFront, los túneles IPsec de los sitios hacia el Transit Gateway y la descarga local por Bluetooth de los termógrafos al terminal del conductor. La tabla siguiente detalla los medios, caminos alternativos y conmutación:

- Termógrafo–terminal: los termógrafos descargan por Bluetooth al terminal del conductor.

- Nube–VM: AWS DMS accede únicamente a VM-02 de Talca por el túnel IPsec autenticado.

- Sitios–SQS: los eventos de cada sitio, incluidos los cross-docking, llegan a SQS FIFO sin depender de otro sitio.

Los 184 usuarios de administración, comercial y soporte de Talca y Concepción acceden a las consolas y a la administración de Keycloak solo por Verified Access. La consola Angular corre en dos tareas Fargate distribuidas entre dos zonas tras un ALB privado y reenvía las llamadas a la API REST privada por el endpoint de interfaz execute-api. CloudFront publica únicamente los endpoints OIDC necesarios para autenticación y renovación de sesión por la API REST pública sin autorizador hacia Keycloak tras el ALB privado; el verificador local de relevos permanece en cada sitio. Las cadenas usan el canal AS2 descrito en ADR-11 (Anexo 4-O), cuyo transporte mantiene dos tareas Fargate distribuidas entre dos zonas.

La Tabla [18](LAFROX-Subdocumento4.md#tab:conexiones) resume cada conexión con su medio, su camino alternativo y el tiempo de conmutación entre ambos.

<a id="tab:conexiones"></a>

**Tabla 18 — Conexiones de la solución y su camino alternativo**

| **Conexión** | **Medio y protocolo** | **Camino alternativo** | **Conmutación** |
| --- | --- | --- | --- |
| CD Talca con la nube | Fibra D-03, túneles IPsec con BGP | LTE D-04 y, tras él, Starlink D-06 | Menos de 30 s |
| CD Concepción con la nube | Fibra D-03, túneles IPsec con BGP | LTE D-04 y, tras él, Starlink D-06 | Menos de 30 s |
| Cross-docking con la nube | Starlink D-06, túneles IPsec con BGP | LTE D-04 de dos proveedores | Menos de 30 s |
| Terreno con la nube | Red celular, CloudFront, API REST pública | Almacén local del dispositivo | No aplica |
| Termógrafos con el terminal del conductor | BLE con el terminal del conductor, en ruta y al regresar | Registro interno del termógrafo | No aplica |
| Usuarios externos con los portales | Internet, HTTPS por CloudFront | Portal de Clientes instalado, que conserva el pedido hasta reconectar | No aplica |
| Oficinas y trabajo remoto con las consolas | Internet, HTTPS por Verified Access | Otra conexión a Internet | No aplica |
| Cadenas con el canal AS2 | Internet, TLS 1.3 al Network Load Balancer | Reenvío AS2 hasta el acuse MDN | No aplica |
| Región primaria con la secundaria | Replicación nativa de Aurora, DynamoDB y S3 | Respaldo inmutable | Promoción autorizada |

Fuente: elaboración propia.

Los cinco sitios tienen caminos alternativos hacia la nube. Ninguna instalación depende de los sistemas de otra; el terreno opera sin señal y los termógrafos conservan su registro interno. Los portales requieren conexión, salvo el Portal de Clientes instalado, que conserva el catálogo descargado y el pedido armado hasta recuperar señal.

### 4.2.5.2 Superficie de exposición

<a id="sub:superficie"></a>

La Tabla [19](LAFROX-Subdocumento4.md#tab:superficie) delimita las únicas entradas desde redes externas. Cada entrada usa un subdominio propio del dominio del CLIENTE gestionado en Route 53.

<a id="tab:superficie"></a>

**Tabla 19 — Superficie de exposición**

| **Entrada** | **Servicio y puerto** | **Quién accede** | **Control** |
| --- | --- | --- | --- |
| Portales y API | CloudFront, HTTPS 443 | Clientes, transportistas, proveedores y terminales de terreno | WAF, protección contra bots, Shield Advanced y autorizador |
| Identidad | OIDC de Keycloak por CloudFront, HTTPS 443 | Personas usuarias | WAF y límites de tasa |
| Consolas | Verified Access, HTTPS 443 | Oficina y trabajo remoto | Identidad, MFA y postura |
| Canal AS2 | Network Load Balancer, TCP 443 con TLS 1.3 | Cadenas registradas | Lista de IP, certificados, firma y MDN |
| Túneles de sitio | VPN del Transit Gateway, IPsec UDP 500 y 4500 | Firewalls D-01 de los cinco sitios | Autenticación IKE y cifrado IPsec |

Fuente: elaboración propia.

La tabla excluye toda otra entrada desde fuera de la red del CLIENTE. En recuperación ante desastres se activan las mismas entradas en us-east-1. MDM, EDR, SII, Transbank, GIS, notificaciones y telemetría de flota son dependencias de salida, detalladas en el Formulario T-11.

### 4.2.5.3 Puntos de falla en los sitios y en los enlaces

Cada conexión se apoya en equipos del sitio que también pueden fallar. La Tabla [20](LAFROX-Subdocumento4.md#tab:fallas-sitios) recorre esos puntos de falla, desde el enlace hasta la energía del recinto, e indica para cada uno el mecanismo que la resuelve y la contingencia si ese mecanismo no basta.

<a id="tab:fallas-sitios"></a>

**Tabla 20 — Puntos de falla en los sitios y en los enlaces**

| **Punto de falla** | **Resolución** | **Contingencia** |
| --- | --- | --- |
| Fibra y LTE de un centro de distribución | BGP conmuta al túnel IPsec ya establecido por Starlink D-06, con prioridad para DMS/WAL, broker, guías, identidad y telemetría crítica. | La operación local conserva 24 h de autonomía. |
| Caída del enlace de Talca para la oficina | Verified Access admite otra conexión a Internet con los mismos controles. | Plan de rutas y manifiesto aprobados en el WMS antes de las 22:00; tableros y costo de servir esperan el retorno. |
| Starlink de un cross-docking | El LTE de dos proveedores toma el tráfico en menos de 30 s. | La ventana de 3 h opera 100 % local y sincroniza al reconectar. |
| Enlace de Los Ángeles en la madrugada | Starlink queda como camino único, porque la red móvil falla a esa hora. | La ventana de madrugada opera íntegramente local. |
| Firewall de Talca | La unidad pasiva asume las direcciones y los túneles en menos de 30 s. | Operación local 24 h sin enlace. |
| Firewall de Concepción | La unidad pasiva asume el túnel y la conmutación de enlace en menos de 30 s. | La unidad dañada se reemplaza con la de reserva de Talca. |
| Nodo del clúster de Talca | Las VM se reinician en los nodos restantes, con sus datos replicados por Ceph. | Ante la pérdida del clúster, se levanta el WMS de Talca en la nube sobre su copia en Aurora. |
| Instancia de escritura VM-02 | Se reinicia en otro nodo del clúster. | D-05 restaura la base en hasta 4 h sin enlace. |
| Disco de un nodo de Talca | Ceph marca el disco fuera y recompone sus réplicas en los otros nodos. | Durante la recomposición quedan dos réplicas. |
| Miembro del stack de switches de Talca o de Concepción | El otro miembro mantiene el tráfico. | Reposición sin corte con la unidad de reserva de Talca. |
| Servidor activo de Concepción | El servidor en espera, con la base replicada en forma sincrónica, toma su lugar en menos de un minuto; cada servidor tiene RAID 10 y fuentes redundantes. | Si fallan ambos, reposición y reconstrucción de la base desde el estado central. |
| Mini-PC activo de un cross-docking | El mini-PC en espera, con la base replicada en forma sincrónica, toma su lugar en menos de un minuto; cada equipo tiene dos fuentes, dos SSD en RAID 1 y una interfaz a cada switch. | Reposición del equipo dañado desde la reserva de Talca; si fallan ambos, reconstrucción desde el estado central y SQS FIFO. |
| Firewall de un cross-docking | La unidad pasiva del par asume el túnel en menos de 30 s. | La ventana de 3 h opera 100 % local y sincroniza al reconectar. |
| Periféricos de andén | Sin redundancia por equipo. | La etiqueta se emite en otra de las impresoras del centro de distribución. |
| Energía de la sala de Talca | UPS N+1 de 30 min y generador que toma carga en 8 a 15 s. | Estanque de 24 h y contrato de reabastecimiento. |
| Corte de energía en la bodega | Las UPS de los gabinetes de piso sostienen switches PoE, AP e impresoras durante 30 min. | Registro de frío con generador en Talca y UPS de 30 min en Concepción. |
| Climatización de la sala de Talca | Segunda unidad de precisión en N+1. | Alerta del monitoreo de los sensores ambientales. |

Fuente: elaboración propia.

En Concepción, el RAID 10 tolera la falla de un disco y las fuentes redundantes sostienen cada servidor ante la pérdida de un circuito. Si falla el servidor activo, el de espera toma su lugar con la base al día, y solo la pérdida de ambos obliga a reconstruirla desde el estado central alimentado por sus eventos. En Talca, el tablero respaldado por generador mantiene el registro de frío, y en Concepción la UPS del gabinete permite el apagado ordenado. La tabla muestra además que los firewalls van en par en los cinco sitios conforme a RT-08.03 (Bases Técnicas Transversales, cap. 8, p. 18). Concepción y cada cross-docking tienen su cómputo en un par de equipos activo y en espera (RT-03.14; Bases Técnicas Transversales, cap. 3, p. 9). Cada cross-docking tiene además dos switches industriales, y cada equipo, alimentación redundante y discos en RAID 1. La liberación sanitaria y el despacho con guía preemitida no dependen de la nube. En la ventana de Talca, VM-02 se reinicia en otro nodo y otra impresora emite la etiqueta si falla la del andén. Los mecanismos de alta disponibilidad se detallan en la sección [4.2.4.3](LAFROX-Subdocumento4.md#sub:3-alta-disponibilidad).

### 4.2.5.4 Puntos de falla en la nube, el terreno y las integraciones

La Tabla [21](LAFROX-Subdocumento4.md#tab:fallas-nube) completa el recorrido con los puntos de falla que están fuera de los sitios: la nube, el terreno y los sistemas de terceros.

<a id="tab:fallas-nube"></a>

**Tabla 21 — Puntos de falla en la nube, el terreno y las integraciones**

| **Punto de falla** | **Resolución** | **Contingencia** |
| --- | --- | --- |
| Zona de disponibilidad de sa-east-1 | Aurora conmuta en menos de 30 s, ElastiCache en menos de 60 s y Fargate reprograma las tareas. | La operación continúa en las zonas restantes. |
| Región sa-east-1 completa | Tras autorización del CLIENTE se promueve Aurora, se restituyen identidad y API y se valida; entonces Route 53 dirige el tráfico a us-east-1. | RTO de 4 h y RPO de 15 min; bodega y terreno operan localmente durante la conmutación. |
| Túnel VPN de Talca durante la replicación | BGP conmuta entre fibra D-03, LTE D-04 y Starlink D-06 para que DMS siga leyendo VM-02. | La autonomía local conserva la operación mientras se restituye cualquier camino. |
| IdP maestro o enlace de identidad | La caché de solo lectura, de 24 h, conserva los datos de identidad recibidos, y el verificador local habilita los relevos de turno con el manifiesto firmado y el PIN personal. | La credencial de turno dura hasta 8 h en bodega y 14 h en terreno, sin revocación remota durante el corte, y queda disponible la cuenta de último recurso (ADR-06, Anexo 4-O). |
| Señal móvil en ruta | La aplicación opera contra el almacén local del dispositivo. | Sincroniza al reconectar dentro de los 10 min de la Tabla [10](LAFROX-Subdocumento4.md#tab:t29). |
| ERP legado | El trabajador `erp-sync` en VM-04 retiene las solicitudes en la cola local o en SQS y reintenta con la misma clave idempotente. | Ningún camión sale sin documento tributario válido emitido por el ERP. |
| Perfil de API saturado | El balanceador reparte entre tareas y el escalado agrega tareas cuando los procesos PHP-FPM ocupados superan el 70 %. | Limitación de tasa en API Gateway con mensaje explícito al usuario. |
| Mensaje de reconciliación inválido o que falla | El consumidor rechaza el sobre de edición desconocida sin aplicarlo; tras cinco intentos pasa a la cola de mensajes fallidos. | Alarma inmediata y reproceso manual trazable; el grupo afectado no bloquea a los demás. |
| Excursión térmica crítica sin enlace | El gateway bloquea el despacho en menos de 5 s en el borde. | Buffer de 24 h y alerta al reconectar. |
| SII, cadenas o notificaciones | Reintento con espera creciente y cola de mensajes fallidos. | Reproceso desde la cola al recuperarse el tercero. |
| Carga del peak de septiembre | Fargate escala automáticamente por perfil y Aurora ya está dimensionada para 3× sin cambio de instancia. | Limitación de tasa en API Gateway. |

Fuente: elaboración propia.

Las fallas de nube o enlace no detienen la preparación ni la entrega, que se confirman localmente. La pérdida de la región primaria deja sin servicio a los portales y a la analítica hasta promover la réplica. El despacho conserva la guía preemitida al cerrar la carga nocturna; si la carga cambia entre las 05:30 y las 07:00, la guía queda inválida y el ERP de Talca emite otra por cualquiera de sus tres caminos, a los que Concepción y los cross-docking llegan por los suyos. Si no hay camino hasta el ERP, el camión sale solo con la carga amparada por su guía vigente y el ajuste pasa a la ruta siguiente. Si la guía ya se anuló, la salida queda bloqueada hasta disponer de un documento válido; ningún camión sale sin guía válida.

## 4.2.6 Dimensionamiento y plan de capacidad

<a id="sec:dimensionamiento"></a>

El dimensionamiento traduce la volumetría del Caso 02 en capacidad para la operación normal, la ventana protegida de despacho y el peak de septiembre. Las citas nombran las Bases Técnicas del caso y las Bases Técnicas Transversales con su capítulo y página. La cadena es: hechos y requisitos, supuestos mínimos, dieciséis dimensiones del numeral 14.2 de las Bases Técnicas del caso (p. 25), capacidad por lugar de proceso y equipamiento. El Anexo 4-W conserva las sustituciones, el perfil horario, las sensibilidades y los umbrales; esta sección presenta la decisión de arquitectura y su consecuencia operativa.

### 4.2.6.1 Método, fuentes y supuestos

<a id="sec:dimensionamiento-metodo"></a>

Un hecho del caso se cita y no se registra como supuesto. Un requisito proviene de las Bases o del Capítulo 15. Un parámetro de diseño es una decisión que imponemos a la solución. Un supuesto completa una cifra que el caso calla y declara fundamento, impacto y validación. Un cálculo se deriva de las entradas anteriores. Los parámetros de plataforma son 50 ms de CPU por solicitud, 64 MB de memoria por proceso y 150 ms de permanencia del proceso en Fargate; son parámetros de diseño que se perfilan y se verifican en las pruebas de RT-09.06 (Bases Técnicas Transversales, cap. 9, p. 21). Los tiempos de respuesta se evalúan en el percentil 95 conforme al numeral 9.1 de las Bases Técnicas Transversales (cap. 9, p. 21).

La cadena evita mezclar decisiones de diseño con hechos del CLIENTE. En particular, el factor SV-04 se aplica sólo a la hora cargada de cada ventana y no se usa para sumar procesos que ocurren en horas diferentes.

### 4.2.6.2 Perfil de carga y regímenes de diseño

<a id="sec:dimensionamiento-regimenes"></a>

Las Bases Técnicas del caso (anexo B, p. 38) distribuyen la operación en estas ventanas:

- Preparación de 22:00 a 06:00.

- Cross-docking de 03:00 a 06:00.

- Despacho de 05:30 a 07:00.

- Reparto de 07:00 a 19:00.

- Recepción de proveedores de 08:00 a 18:00.

- Preventa de 09:00 a 18:00.

- Sincronización de 17:00 a 20:00.

La hora más exigente es 12:00, con 12,34 TPS normales y 14,66 TPS en septiembre. Esa hora es una convención del cálculo: el factor SV-04 concentra la preventa y el portal en la hora central de su ventana, y el máximo sería el mismo en cualquier otra hora de esa ventana. En esa hora el portal aporta 9,63 TPS y la nube 2,71 TPS normales o 5,03 TPS en peak; Talca, Concepción y cada cross-docking están fuera de sus ventanas de mayor carga. El promedio diario engaña porque oculta la coincidencia de preventa, reparto y sesiones del portal.

La Tabla [22](LAFROX-Subdocumento4.md#tab:dimensionamiento-calendario) resume los factores de calendario que se usan en la memoria.

<a id="tab:dimensionamiento-calendario"></a>

**Tabla 22 — Calendario y factores de diseño**

| **Dato** | **Valor** | **Uso** | **Fuente** |
| --- | --- | --- | --- |
| Días equivalentes de despacho | 22,14 días | 31.000 ÷ 1.400; control 2.100 ÷ 96 = 21,88 | Bases Técnicas del caso, cap. 14, p. 24 y Tabla 2.3; SV-01 |
| Factor de septiembre | 1,857 | 2.600 ÷ 1.400 | Bases Técnicas del caso, cap. 14, p. 24; SV-02 |
| Período peak | 1 al 25 de septiembre | Define el régimen peak | Bases Técnicas del caso, anexo B, p. 38 |
| Totales anuales | 12 × volumen mensual | Evita inventar días hábiles | Bases Técnicas del caso, cap. 14, p. 24 |

Fuente: elaboración propia.

Los 22,14 días son una equivalencia de cálculo, no una cantidad de días hábiles. El peak se obtiene por el cociente entre entregas de septiembre y entregas normales; diciembre no agrega un factor porque el caso identifica septiembre como la mayor exigencia.

### 4.2.6.3 Transacciones por segundo: dimensiones 1–3

<a id="sec:dimensionamiento-tps"></a>

La dimensión 1, «Transacciones por segundo en régimen normal», toma el máximo horario normal. La dimensión 2, «Transacciones por segundo en el peak de la ventana de despacho de 05:30 a 07:00», incluye la cota de emisión de guías y el re-despacho del cross-docking. La dimensión 3, «Transacciones por segundo en el peak de septiembre», toma el máximo horario del perfil de septiembre.

La Tabla [23](LAFROX-Subdocumento4.md#tab:t76) presenta los lugares de proceso y separa el portal de la nube. El despacho se muestra como una cota independiente porque el caso lo identifica como peak actual de emisión de documentos.

<a id="tab:t76"></a>

**Tabla 23 — Transacciones por segundo por lugar de proceso**

| **Lugar o flujo** | **Régimen normal** | **Ventana de despacho** | **Peak septiembre** | **Derivación** |
| --- | --- | --- | --- | --- |
| WMS de Talca | 1,46 TPS | 1,46 TPS | 2,68 TPS | preparación y despacho según perfil horario y SV-03 |
| WMS de Concepción | 0,73 TPS | 0,73 TPS | 1,34 TPS | 2/3 y 1/3 de preparación y despacho; SV-03 |
| Cada cross-docking | 1,17 TPS | 0,78 TPS | 2,17 TPS | Tres operaciones de llegada y una de despacho |
| Nube, sin portal | 2,71 TPS | 0,79 TPS | 5,03 TPS | preventa, reparto, recepción, trazabilidad, guías y sincronización |
| Portal | 9,63 TPS | – | 9,63 TPS | 2.600 ÷ 9 × 2 por SV-04 × 60 ÷ 3.600 |
| Total | 12,34 TPS | 3,76 / 6,94 TPS | 14,66 TPS | El máximo global de septiembre ocurre a las 12:00 con preventa y portal, y el máximo de despacho entre 05:30 y 07:00 llega a 6,94 TPS con guías y re-despacho. |

Fuente: elaboración propia.

El despacho de 05:30 a 07:00 se reparte entre ambos centros conforme a SV-03, en la misma proporción que la preparación. La dimensión 2 toma el máximo real del perfil en las horas 05:00 y 06:00; el tramo 05:30–06:00 se considera uniforme, por lo que resulta 3,76 TPS normal y 6,94 TPS peak. Los aproximadamente 2.852 documentos/día peak son el total de DTE (34.000 ÷ 22,14 × 1,857), no sólo guías; considerarlos todos como guías que deben emitirse antes de la salida es una cota conservadora. Las 2.600 sesiones diarias del portal son un parámetro de diseño: una por cada cliente de food service y de cadenas, 2.100 + 500 (Bases Técnicas del caso, cap. 2, p. 4), y no son las 2.600 visitas diarias de preventa (Bases Técnicas del caso, anexo B, p. 38). La prueba RT-09.06 (Bases Técnicas Transversales, cap. 9, p. 21) es 1,5 × 14,66 = 21,99 TPS y no recibe un segundo multiplicador.

### 4.2.6.4 Personas usuarias, concurrencia y dispositivos: dimensiones 4–6

<a id="sec:dimensionamiento-usuarios"></a>

La dimensión 4, «Personas usuarias registradas, internas y externas», es 15.180 registros: 640 + 160 + 14.200 + 180. La dimensión 5, «Personas usuarias concurrentes en peak», toma el máximo de cada ventana sin sumar turnos que no coinciden. La Tabla [24](LAFROX-Subdocumento4.md#tab:dimensionamiento-concurrencia) muestra la operación sin portal y la cota de sesiones.

<a id="tab:dimensionamiento-concurrencia"></a>

**Tabla 24 — Concurrencia por ventana**

| **Ventana** | **Operación sin portal** | **Portal** | **Máximo** |
| --- | --- | --- | --- |
| Noche: preparación y cross-docking | 120 + 60 + 6 = 186 | – | 186 |
| Despacho | 96 equipos de reparto | – | 96 |
| Día | 62 + 96 + 184 = 342 | 96,30 en régimen | 438,30 |
| Sincronización | 62 + 96 = 158 | – | 158 |
| Cota extrema del portal | 342 | 433,33 | 775,33 |

Fuente: elaboración propia.

La operación sin portal, que carga la Wi-Fi y los sitios, llega a 342 personas o equipos concurrentes durante el día. Los seis del cross-docking son personas con terminal inalámbrico, dos por plataforma (S-35). Los 96 equipos de reparto equivalen a 96 conductores en ruta; la dimensión 5 se expresa en personas o sesiones y no en camiones. La cota extrema del portal se conserva como prueba separada. La dimensión 6, «Dispositivos de terreno en operación simultánea», es 62 preventistas + 96 equipos de reparto = 158.

La cantidad a proveer se informa aparte, por ámbito:

- Bodega: 132 terminales en Talca, 22 de ellos para congelado, y 66 en Concepción.

- Terreno: 69 terminales de preventa, 106 terminales de reparto, 106 impresoras de cabina y 106 terminales de pago.

- Cross-docking y frío: 9 terminales de cross-docking y 31 termógrafos.

Cada cantidad incluye la reserva del 10 % del parque, redondeada hacia arriba, conforme a la tabla de repuestos de las Bases Técnicas Transversales (cap. 8, p. 19). Solo los 22 terminales de la cuadrilla de congelado de Talca son aptos para -22 °C: el congelado representa cerca del 4 % de las líneas y se prepara al final del turno, de modo que la cuadrilla que entra a la cámara es de unas 20 personas (S-34). Concepción no tiene congelado.

### 4.2.6.5 Almacenamiento, retención y migración: dimensiones 7–10

<a id="sec:dimensionamiento-almacenamiento"></a>

La dimensión 7, «Volumen anual de almacenamiento transaccional», la dimensión 8, «Volumen anual de almacenamiento de evidencia de entrega, firmas y fotografías», la dimensión 9, «Volumen anual de almacenamiento de series de temperatura y de posicionamiento», y la dimensión 10, «Volumen total de datos históricos a migrar», se resumen en la Tabla [25](LAFROX-Subdocumento4.md#tab:dimensionamiento-almacenamiento).

<a id="tab:dimensionamiento-almacenamiento"></a>

**Tabla 25 — Volumen, retención y destino de los datos**

| **Dominio** | **Volumen anual** | **Retención** | **Acumulado** | **Destino** |
| --- | --- | --- | --- | --- |
| Datos transaccionales | 50,75 GB/año | 6 años como cota | 304,49 GB | Base local de 4 meses y nube |
| Evidencia de entrega | 87,72 GB/año | 6 años | 526,32 GB | S3 por niveles |
| Temperatura | 0,58 GB/año crudos | 5 años | 2,89 GB crudos | IoT y almacenamiento histórico |
| Posición | 3,20 GB/año crudos | 12 meses | 3,20 GB crudos | Telemetría y almacenamiento histórico |
| Migración histórica | 32,11 GB | Maestros; 36/24/60/24 meses | 30,73–33,49 GB de sensibilidad | Nube después del perfilado |

Fuente: elaboración propia.

La migración no supone eventos históricos digitales de trazabilidad: el caso dice que no existe forma consultable y que el lote se anota en texto libre cuando se anota. Por eso la estimación usa 1.150 recepciones mensuales × 60 meses × 20 líneas por recepción, con sensibilidad de 10 a 30 líneas. El 41 % sin lote del retiro de marzo se usa sólo para saneamiento de calidad, conforme a Bases Técnicas del caso, cap. 7, p. 12.

### 4.2.6.6 Integraciones y ancho de banda por sitio: dimensiones 11–12

<a id="sec:dimensionamiento-enlaces"></a>

La dimensión 11, «Número de integraciones y volumen de mensajes por integración», cuenta únicamente INT-01 a INT-15 del catálogo del apartado 4.1. Portal y llamadas internas a la API quedan fuera. La Tabla [26](LAFROX-Subdocumento4.md#tab:dimensionamiento-integraciones) resume sus 230.252 mensajes diarios normales y 353.333 en peak, incluida la coordinación de reserva de INT-03/04; INT-14 considera 13 nodos activos, seis VMs en Talca, cuatro en Concepción y un mini-PC activo por cada cross-docking, con 1.000 eventos por nodo al día. Suma además 7 nodos en espera, cuatro VMs en Concepción y un mini-PC por cross-docking, con 200 eventos al día, porque no atienden transacciones.

<a id="tab:dimensionamiento-integraciones"></a>

**Tabla 26 — Mensajes de integración por grupo**

| **Integraciones** | **Normal** | **Peak** | **Origen** |
| --- | --- | --- | --- |
| INT-01 a INT-04 | 119.678/día | 222.260/día | Pedidos, entregas, eventos, coordinación de reserva y cota de cross-docking |
| INT-05 | 10.920/día | 10.920/día | 6.048 cámaras + 4.872 termógrafos |
| INT-06 a INT-10 | 8.608/día | 15.905/día | ERP, DTE, EDI, pagos y mapas |
| INT-11 a INT-15 | 91.046/día | 104.248/día | Avisos, réplica, identidad, ADOT y telemetría |
| **Total** | **230.252/día** | **353.333/día** | **15 integraciones** |

Fuente: elaboración propia.

El EDI actual es cero. Desde enero de 2029 opera todos los días, y se dimensiona con la misma hipótesis en régimen y en peak: 11 % de los pedidos, que corresponde a la cadena principal y su 11 % de la venta (SV-05), con cuatro mensajes por pedido. Son 1.400 × 11 % × 4 = 616 mensajes en régimen y 2.600 × 11 % × 4 = 1.144 en peak. La pasarela de pago se acota con un pago electrónico por entrega como máximo y dos mensajes por pago, solicitud y respuesta: 2.800 en régimen y 5.200 en peak. Los 11.800 cobros mensuales del caso son en efectivo y no miden pagos con tarjeta. La Tabla [27](LAFROX-Subdocumento4.md#tab:t81) compara el peor caso del camino principal y el drenaje de los caminos de respaldo.

<a id="tab:t81"></a>

**Tabla 27 — Ancho de banda por sitio y camino**

| **Sitio** | **Camino** | **Subida de diseño** | **Carga evaluada** | **Utilización** |
| --- | --- | --- | --- | --- |
| Talca | D-03 fibra | 20 Mbps | 5,16 Mbps, peor caso | 25,80 % |
| Talca | D-04 LTE | 5 Mbps | 1,87 Mbps, drenaje | 37,43 % |
| Talca | D-06 satélite | 2 Mbps | 1,87 Mbps, drenaje | 93,59 % |
| Concepción | D-03 fibra | 10 Mbps | 2,14 Mbps, peor caso | 21,41 % |
| Concepción | D-04 LTE | 3 Mbps | 1,44 Mbps, drenaje | 47,86 % |
| Concepción | D-06 satélite | 2 Mbps | 1,44 Mbps, drenaje | 71,79 % |
| Cada cross-docking | D-06 satélite | 2 Mbps | 0,41 Mbps, peor caso | 20,65 % |
| Cada cross-docking | D-04 LTE | 2 Mbps | 0,35 Mbps, drenaje | 17,70 % |

Fuente: elaboración propia.

D-03 es fibra, D-04 es LTE y D-06 es satélite, calculado conservadoramente con 2 Mbps de subida mínima supuesta, a confirmar en la instalación. En Talca, el drenaje por satélite usa el 93,59 % de esa subida. Por eso la aceptación exige medir al menos 2,2 Mbps, un 15 % sobre el drenaje para el túnel y las retransmisiones. El tráfico prioritario continuo es 0,014 Mbps en Talca, 0,007 Mbps en Concepción y 0,002 Mbps por cross-docking. En Talca y Concepción, Starlink permanece en espera caliente con terminal encendido, túnel IPsec establecido y BGP de menor preferencia, y solo al caer fibra y LTE transporta DMS/WAL de Talca, broker y outbox, guías hacia ERP y SII, identidad y telemetría crítica conforme al RPO de 15 minutos; en los cross-docking es el camino principal con LTE de dos proveedores como respaldo. El drenaje no incluye oficina: durante un corte no se encola ese tráfico. Sí incluye cambios con WAL, broker, telemetría, observabilidad e incremental de respaldo. Durante la recuperación por D-04, la sincronización tiene prioridad sobre el tráfico de oficina. En la hora punta regresan 64 camiones en total, repartidos por SV-03: el enlace y la Wi-Fi requieren 0,93 Mbps en Talca y 0,47 Mbps en Concepción; en conjunto, 1,40 Mbps. El agregado de la ventana 17:00–20:00 es 0,70 Mbps. El respaldo completo semanal y la aplicación de los terminales de bodega y de reparto caben en la ventana dominical; los equipos de reparto se actualizan en el centro donde estaciona su camión, según SV-03, y los de preventa, por la red móvil. El sistema operativo se distribuye en tandas dominicales de 18 equipos en Talca, 9 en Concepción y 2 en cada cross-docking; una ronda completa ocupa 12 domingos en cada centro. La aplicación se actualiza en un domingo por sitio; la ronda del sistema operativo tiene cadencia semestral.

### 4.2.6.7 Terreno: turno sin señal y sincronización de la flota: dimensiones 13–14

<a id="sec:dimensionamiento-terreno"></a>

La dimensión 13, «Volumen de datos generado por un dispositivo de reparto en un turno completo sin señal», es 9,83 MB para la ruta de 34 clientes; una ruta promedio genera 5,36 MB normales y 8,24 MB en septiembre. La cifra incluye evidencia, una fotografía adicional cuando corresponde y 2 MB de datos locales.

La dimensión 14, «Tiempo de sincronización de la flota al regresar al centro de distribución», se expresa en tiempo: cada dispositivo sincroniza en diez minutos con al menos 0,13 Mbps efectivos. Los 64 camiones de la hora punta se reparten por SV-03: aproximadamente 43 en Talca y 21 en Concepción, con 0,93 y 0,47 Mbps respectivamente en la Wi-Fi y el enlace de cada centro. La flota completa requiere 1,40 Mbps en esa hora. La cota de 34 clientes corresponde a la ruta rural más larga descrita en el caso (Bases Técnicas del caso, cap. 8, p. 16, entrevista al conductor de la ruta Cauquenes); en los centros de distribución la sincronización ocurre por Wi-Fi.

### 4.2.6.8 Capacidad on-premise

<a id="sec:dimensionamiento-onpremise"></a>

La capacidad propuesta conserva maestros, stock, lotes presentes y movimientos de cuatro meses en cada sitio; el histórico vive en la nube. El horizonte cubre el ciclo de conteo de 11.400 ÷ 3.400 = 3,35 meses y la rotación media de 11,4 veces/año. Cada VM se calcula como base de sistema más carga, según la tabla de VMs del Anexo 4-W. El requisito total incorpora el hipervisor (+15 % de vCPU y 2 GB de RAM por nodo) y, en Talca, Ceph: dos OSD de 1 vCPU y 4 GB cada uno, más monitor/manager de 1 vCPU y 2 GB por nodo. La Tabla [28](LAFROX-Subdocumento4.md#tab:t79) resume la capacidad requerida por sitio.

<a id="tab:t79"></a>

**Tabla 28 — Capacidad requerida por sitio**

| **Sitio** | **Base local** | **Requerido actual** | **Requerido a 3×** |
| --- | --- | --- | --- |
| Talca, VM-01 a VM-06 | 5,04 GB y 7,78 GB RAM de trabajo | VMs: 14 vCPU, 23 GB RAM y 210 GB; total: 26 vCPU y 59 GB RAM | VMs: 14 vCPU, 25 GB RAM y 221 GB; total: 26 vCPU y 61 GB RAM |
| Concepción, VM-C01 a VM-C04, por servidor | 2,59 GB y 5,94 GB RAM de trabajo | 12 vCPU, 17 GB RAM y 140 GB | 12 vCPU, 18 GB RAM y 140 GB |
| Cada cross-docking, por mini-PC | 0,63 GB y 4,47 GB RAM de trabajo | 3 vCPU, 5 GB RAM y 50 GB | 3 vCPU, 5 GB RAM y 50 GB |
| Mínimo por nodo de Talca | – | – | 13 vCPU, 31 GB RAM y 221 GB OSD |

Fuente: elaboración propia.

Ceph entrega 1,92 TB útiles con seis NVMe de 960 GB, tres réplicas y sin RAID. Con un nodo caído, Talca conserva 64 vCPU y 128 GB RAM, y Ceph sigue sirviendo los datos con dos réplicas hasta que el nodo vuelve. El umbral de llenado al 80 % es 1,54 TB, superior a los 221 GB requeridos a 3×. Su utilización actual es 40,62 % de CPU, 46,09 % de RAM y 10,94 % de disco; a 3× es 40,62 %, 47,66 % y 11,51 %, respectivamente. Cada servidor de Concepción dispone de 16 hilos, 32 GB RAM y 3,84 TB útiles en RAID 10 y aloja el conjunto completo, activo o en espera; utiliza 75,00 % de CPU, 53,12 % de RAM y 3,65 % de disco actualmente, y 75,00 %, 56,25 % y 3,65 % a 3×. En Talca la redundancia es N+1 dentro del clúster, y sus nodos ofertados de 32 hilos y 64 GB ya cubren 3×. En Concepción y en cada cross-docking la redundancia es un segundo equipo idéntico en espera, de modo que la utilización por equipo no cambia.

### 4.2.6.9 Capacidad en nube

<a id="sec:dimensionamiento-nube"></a>

La plataforma utiliza Fargate, Aurora, ElastiCache, SQS, IoT Core, DynamoDB y S3 como servicios administrados. Una tarea entrega 14 solicitudes por segundo al 70 % de uso con 50 ms de CPU. El escalado reacciona con métricas de un minuto y pone una tarea nueva en servicio en menos de tres minutos, valor de diseño que mide la prueba de carga; el balanceador drena la tarea que sale sin perder transacciones en curso (RT-09.04; Bases Técnicas Transversales, cap. 9, p. 21). La Tabla [29](LAFROX-Subdocumento4.md#tab:dimensionamiento-nube) separa el portal y compara cada perfil con el techo de ocho tareas.

<a id="tab:dimensionamiento-nube"></a>

**Tabla 29 — Procesos Fargate por perfil**

| **Perfil** | **Carga** | **Tareas** | **Techo** | **Conclusión** |
| --- | --- | --- | --- | --- |
| Régimen normal | 12,34 solicitudes/s (nube + portal) | 2 | 8 | Cumple |
| Peak de septiembre | 14,66 solicitudes/s (nube + portal) | 2 | 8 | Cumple |
| Prueba RT-09.06 (Bases Técnicas Transversales, cap. 9, p. 21) | 21,99 solicitudes/s totales, distribuido por perfil horario | 2 | 8 | Una sola multiplicación |
| Cota extrema | 48,37 solicitudes/s (5,03 + 43,33) | 4 | 8 | Bajo el techo |
| Sensibilidad 120 solicitudes | 21,97 / 91,70 solicitudes/s; régimen / cota | 2 / 7 | 8 | Bajo el techo |

Fuente: elaboración propia.

El portal en régimen usa 9,63 solicitudes/s y 96,30 sesiones concurrentes; su cota extrema usa 43,33 solicitudes/s y 433,33 sesiones concurrentes. Con 120 solicitudes por sesión, manteniendo las sesiones repartidas en la hora, el portal alcanza 19,26 solicitudes/s en régimen y 86,67 en la cota extrema; al sumar la nube resultan 21,97 y 91,70 solicitudes/s, que requieren 2 y 7 tareas. El parámetro se mantiene bajo el techo de ocho, pero se perfila en la prueba de carga.

### 4.2.6.10 Plan de capacidad

<a id="sec:dimensionamiento-plan"></a>

La Tabla [30](LAFROX-Subdocumento4.md#tab:dimensionamiento-plan) mantiene separadas la proyección del año 3 y la exigencia técnica de 3×. Cada fila tiene una acción concreta de operación o ampliación.

<a id="tab:dimensionamiento-plan"></a>

**Tabla 30 — Proyección y crecimiento de capacidad**

| **Componente** | **Año 1** | **Año 3** | **3×** | **Acción** |
| --- | --- | --- | --- | --- |
| WMS de Talca, TPS peak | 2,68 | 2,68 × (305.000 ÷ 260.000) = 3,15 | 8,05 | Revisar CPU e IOPS trimestralmente |
| Cada cross-docking, TPS peak | 2,17 | 2,58 | 6,50 | Revisar CPU e IOPS trimestralmente |
| Nube, TPS peak / tareas | 14,66 / 2 | 14,66 × (36.000 ÷ 31.000) = 17,03 / 2 | 43,98 / 4 | Escalamiento automático y prueba trimestral |
| Evidencia anual | 87,72 GB | 87,72 × (36.000 ÷ 31.000) = 101,87 GB | 263,16 GB | Escalar S3 y revisar retención |
| Enlace de Talca, peor caso | 5,16 Mbps | 5,20 Mbps, con los flujos de volumen × 305.000 ÷ 260.000 | 5,64 Mbps | Ampliar D-03 si el percentil 95 supera la cota |
| Terminales de bodega de Talca | 132 | (23 + 3) de congelado + (113 + 12) estándar = 151 | no aplica | Ajustar parque a la dotación |
| Mesa de ayuda, contactos | 2.000/mes | 2.000 × (350 ÷ 310) = 2.258/mes | 6.000/mes | Recalibrar Erlang C trimestralmente |

Fuente: elaboración propia.

La nube escala automáticamente dentro del techo declarado; nodos, almacenamiento local, Wi-Fi y enlaces requieren revisión planificada. La gestión trimestral compara la proyección observada con la cota de 3× y con la incorporación de nuevas unidades.

### 4.2.6.11 Cuello de botella, umbrales y degradación controlada

<a id="sec:dimensionamiento-cuello"></a>

El primer candidato es la emisión de guías del ERP. En el peak se emiten unos 2.852 documentos tributarios electrónicos (DTE) al día. El tiempo disponible por guía depende de la ventana:

- Entre 22:00 y 05:30: máximo de 9,47 segundos por guía.

- En las últimas 3,5 horas: máximo de 4,42 segundos por guía.

- En la ventana actual de despacho: máximo de 1,89 segundos por guía.

La solución emite la guía cuando confirma la carga, durante la noche. Se detectan guías aún no emitidas frente a la hora de salida de cada camión y se prioriza la cola, sin crear un segundo emisor: el ERP conserva la responsabilidad tributaria y la guía acompaña el traslado. Como el caso no documenta las interfaces del ERP y encarga levantarlas en los primeros meses (Bases Técnicas del caso, cap. 5, p. 10), el tiempo real por guía se mide en ese levantamiento; si superara los 4,42 segundos, las cargas se cierran por camión en el orden de salida, para que la emisión empiece antes.

La Tabla [31](LAFROX-Subdocumento4.md#tab:t84) fija los umbrales de respuesta que se observan en percentil 95.

<a id="tab:t84"></a>

**Tabla 31 — Umbrales de respuesta en percentil 95**

| **Operación** | **Umbral** | **Fuente** |
| --- | --- | --- |
| Confirmación de línea de preparación | 1 s | Bases Técnicas del caso, cap. 15, p. 26 |
| Registro de entrega | 2 s | Bases Técnicas del caso, cap. 15, p. 26 |
| Línea de preventa | 1,5 s | Bases Técnicas del caso, cap. 15, p. 26 |
| Consulta de stock y crédito | 2 s | Bases Técnicas del caso, cap. 15, p. 26 |
| Transacción crítica de terreno | 3 s | Bases Técnicas Transversales, cap. 9, p. 21 |
| Carga inicial del portal | 2 s | Bases Técnicas Transversales, cap. 9, p. 21 |
| Navegación | 1 s | Bases Técnicas Transversales, cap. 9, p. 21 |
| API de consulta | 500 ms | Bases Técnicas Transversales, cap. 9, p. 21 |
| API de escritura | 800 ms | Bases Técnicas Transversales, cap. 9, p. 21 |
| Búsqueda compuesta | 3 s | Bases Técnicas Transversales, cap. 9, p. 21 |
| Informe estándar | 30 s | Bases Técnicas Transversales, cap. 9, p. 21 |

Fuente: elaboración propia.

Los otros candidatos son la base WMS, los IOPS, la Wi-Fi y el drenaje. Se detectan con percentil 95, longitud de colas, errores, retransmisiones y tiempo de sincronización. Si se supera una cota, se encola con clave idempotente, se limita la tasa y se muestra un mensaje explícito; no se pierden ni duplican pedidos.

### 4.2.6.12 Validación mediante pruebas de carga y estrés

<a id="sec:dimensionamiento-pruebas"></a>

La prueba RT-09.06 (Bases Técnicas Transversales, cap. 9, p. 21) carga una sola vez 1,5 × la dimensión 3, es decir, 21,99 TPS totales. La Tabla [32](LAFROX-Subdocumento4.md#tab:t86) vincula cada ensayo con la decisión que debe cerrar.

<a id="tab:t86"></a>

**Tabla 32 — Pruebas que confirman el dimensionamiento**

| **Prueba** | **Carga** | **Qué confirma** | **Criterio** |
| --- | --- | --- | --- |
| Carga RT-09.06 (Bases Técnicas Transversales, cap. 9, p. 21) | 21,99 TPS totales, distribuidos por lugar según el perfil horario | CPU, Fargate, portal, WMS, base e IOPS | Percentil 95 |
| Estrés RT-09.06 (Bases Técnicas Transversales, cap. 9, p. 21) | Sobre cota extrema portal y 3× | Umbral de quiebre y degradación | Sin pérdida ni duplicación |
| Corte de enlace | 24 h y drenaje en 2 h | WAL, broker, telemetría y observabilidad | Drenaje completo |
| Sincronización de dispositivo | Peor ruta en 10 min | 0,13 Mbps efectivos | Ruta reconciliada |
| Migración | Dos ensayos independientes | Volumen y calidad histórica | Conciliación de dominios |
| Ventana dominical | Respaldo y actualizaciones | Tandas por sitio y enlace | Cada tanda cabe |

Fuente: elaboración propia.

La prueba de carga conserva tasas por lugar, percentil 95, utilización, colas, errores y comportamiento durante el drenaje; incluye la concurrencia de oficina y trabajo remoto por Verified Access, la API privada, el inicio de sesión y los tableros. Los parámetros confirmados se actualizan en la revisión trimestral de capacidad.

### 4.2.6.13 Síntesis de las dieciséis dimensiones del numeral 14.2

<a id="sec:dimensionamiento-sintesis"></a>

La Tabla [33](LAFROX-Subdocumento4.md#tab:t72) reúne cada dimensión con el nombre literal del Caso 14.2, su valor normal o de ventana, su valor peak o declarado y la derivación correspondiente.

<a id="tab:t72"></a>

**Tabla 33 — Síntesis de las dieciséis dimensiones**

| **N.°** | **Dimensión** | **Valor en régimen normal o ventana** | **Valor en peak o declarado** | **Derivación** |
| --- | --- | --- | --- | --- |
| 1 | Transacciones por segundo en régimen normal | 12,34 TPS a las 12:00 | – | Anexo 4-W, sección 4-W.2 |
| 2 | Transacciones por segundo en el peak de la ventana de despacho de 05:30 a 07:00 | 3,76 TPS | 6,94 TPS | Anexo 4-W, sección 4-W.2 |
| 3 | Transacciones por segundo en el peak de septiembre | – | 14,66 TPS a las 12:00 | Anexo 4-W, sección 4-W.2 |
| 4 | Personas usuarias registradas, internas y externas | 15.180 | – | Anexo 4-W, sección 4-W.3 |
| 5 | Personas usuarias concurrentes en peak | 438,30 en régimen; 342 sin portal | 775,33, cota extrema | Anexo 4-W, sección 4-W.3 |
| 6 | Dispositivos de terreno en operación simultánea | 158 | 158 | Anexo 4-W, sección 4-W.3 |
| 7 | Volumen anual de almacenamiento transaccional | 50,75 GB/año | 7,85 GB mes peak | Anexo 4-W, sección 4-W.4 |
| 8 | Volumen anual de almacenamiento de evidencia de entrega, firmas y fotografías | 87,72 GB/año | 13,58 GB mes peak | Anexo 4-W, sección 4-W.4 |
| 9 | Volumen anual de almacenamiento de series de temperatura y de posicionamiento | 0,58 + 3,20 GB/año crudos | 2,89 + 3,20 GB crudos retenidos | Anexo 4-W, sección 4-W.4 |
| 10 | Volumen total de datos históricos a migrar | 32,11 GB | 30,73–33,49 GB de sensibilidad | Anexo 4-W, sección 4-W.4 |
| 11 | Número de integraciones y volumen de mensajes por integración | 15; 230.252 mensajes/día | 353.333 mensajes/día | Anexo 4-W, sección 4-W.5 |
| 12 | Ancho de banda requerido por sitio, en régimen y en peak | 3,29 / 0,71 / 0,06 Mbps cargados | 5,16 / 2,14 / 0,41 Mbps peor caso | Anexo 4-W, sección 4-W.5 |
| 13 | Volumen de datos generado por un dispositivo de reparto en un turno completo sin señal | 5,36 MB promedio | 9,83 MB, ruta de 34 clientes | Anexo 4-W, sección 4-W.6 |
| 14 | Tiempo de sincronización de la flota al regresar al centro de distribución | 10 min por dispositivo | 10 min después del último camión | Anexo 4-W, sección 4-W.6 |
| 15 | Contactos mensuales a la mesa de ayuda | 2.000 contactos/mes | 2.000 contactos/mes en el escenario conservador; 7 agentes en la hora cargada y 2 en las demás cubren hasta 2.283 | Anexo 4-W, sección 4-W.7 |
| 16 | Dotación de la mesa de ayuda y del equipo de operación | Son 15 personas a 42 h y 17 desde el 26-04-2028 a 40 h. | Son 17 personas en septiembre y diciembre a 42 h y 19 desde el 26-04-2028 a 40 h. | Anexo 4-W, sección 4-W.7 |

Fuente: elaboración propia.

El diseño queda gobernado por tres condiciones operativas. La primera es la emisión de guías del ERP antes de la salida de cada camión, que es la única de las tres cuya capacidad no controla la solución y que por eso se mide primero. La segunda es el enlace de Talca durante el retorno de la flota, cuando la sincronización de los dispositivos se suma al tráfico de oficina. La tercera es el almacenamiento de la evidencia de entrega, que es el volumen que más crece y el que fija la política de niveles de S3. El resto de las dimensiones queda con holgura amplia frente a la capacidad propuesta, incluso con el crecimiento de 3×.

# 4.3 Data center

<a id="cap:4-3-data-center"></a>

La estrategia de centros de datos distribuye la operación productiva entre la región primaria AWS sa-east-1 y la sala técnica secundaria del CD Talca. El dominio de nube se recupera en us-east-1; ante la pérdida de la sala de Talca, su WMS se levanta en la plataforma de nube de la región activa sobre la copia en Aurora. Concepción y las tres plataformas de cross-docking son sitios operacionales autónomos y publican sus eventos para la consolidación central.

La arquitectura fija RTO ≤ 4 h, RPO ≤ 15 min y disponibilidad mensual de 99,95 % por componente de infraestructura, con un compromiso de ≥ 99,9 % para la transacción crítica de extremo a extremo. Esta sección concreta los emplazamientos, servicios y conexiones descritos en 4.2; el equipamiento y los servicios contratados se detallan en el Formulario T-11, entregado como archivo propio.

## 4.3.1 Especificaciones Data Center Primaria

<a id="sec:d-especificaciones-del-sitio-principal-on-"></a>

El Data Center Primario concentra la operación productiva de la solución en dos dominios que se exigen mutuamente por el carácter híbrido obligatorio del despliegue: la región primaria de la nube en sa-east-1, ubicada en São Paulo, Brasil, y la sala técnica secundaria on-premise del centro de distribución de Talca, tipología que fija el propio caso. Ambos dominios se especifican bajo el mismo criterio: un centro de datos comprende no solo los servidores, sino también las condiciones que sostienen la operación sin interrupción: energía acondicionada, clima controlado, conectividad, seguridad física y monitoreo permanente con procedimiento escrito.

Esta sección declara, para cada dominio, el proveedor, la región y las zonas de disponibilidad, los servicios contratados y el sitio on-premise. También fija los objetivos de continuidad verificables que los gobiernan: disponibilidad de infraestructura de 99,95 % mensual por componente y, para los servicios críticos, RTO ≤ 4 h y RPO ≤ 15 min. Sobre estos objetivos se sostiene el compromiso contractual penalizable de ≥ 99,9 % mensual de la transacción de negocio de extremo a extremo. El desglose servicio por servicio y componente por componente se entrega en el Formulario T-11.

### 4.3.1.1 Proveedor

Para la nube en Amazon Web Services todos los servicios se contratan en cuentas del CLIENTE, que son organizadas bajo AWS Control Tower con una cuenta por ambiente de modo que la propiedad de los datos y de la infraestructura es del CLIENTE desde el primer día. Los criterios con que se eligieron esos servicios se explican en el apartado [4.2.3](LAFROX-Subdocumento4.md#sec:servicios-nube). AWS satisface el requisito de presencia de región o zona en Chile o en Sudamérica con la región primaria sa-east-1. El cumplimiento de los estándares y marcos de referencia del Artículo 4.3 de las Bases Administrativas (art. 4.3, p. 5) entre ellos ISO/IEC 27017 (nube) e ISO/IEC 27018 (datos personales en nube) se acredita en la fila 5.23 de la matriz de controles del Anexo 4-R, que responde a RT-11.06 (Bases Técnicas Transversales, cap. 11, p. 23), y no se repite en esta sección.

En el dominio On-premise del CD de Talca, el caso exige cómputo, almacenamiento y procesamiento en las instalaciones del CLIENTE para sostener recepción, preparación y despacho durante un corte de enlace; ello obliga a la modalidad híbrida. Ese alcance requiere cómputo local para la continuidad de un sitio operacional sin albergar el núcleo. Por ello, el sitio adopta la tipología de **sala técnica secundaria o de sitio** del numeral 6.1 de las Bases Técnicas Transversales (cap. 6, p. 14), con disponibilidad de infraestructura de 99,95 % y dimensionamiento proporcional al equipamiento real.

### 4.3.1.2 Región y zonas de disponibilidad

La región primaria de la nube es sa-east-1, ubicada en São Paulo, Brasil. Todo componente con requisito de alta disponibilidad se despliega en al menos dos zonas de disponibilidad; no se acepta un diseño en una sola zona. Aurora PostgreSQL tiene el escritor en sa-east-1a y un lector promovible en sa-east-1b. ECS Fargate, ElastiCache Redis, el balanceador de aplicación y el NAT Gateway operan entre esas mismas dos zonas con conmutación automática; DynamoDB opera Multi-AZ de forma nativa y transparente. El único componente con escritor único es la base de datos, que conmuta de forma automática entre las zonas. Este diseño sostiene el compromiso de extremo a extremo de ≥ 99,9 % mensual de la transacción crítica y la conmutación se verifica en las pruebas de resiliencia por inyección de fallas de la arquitectura de despliegue.

### 4.3.1.3 Servicios contratados en la región primaria

Los servicios contratados en la región primaria son los que agrupa por función la Tabla [11](LAFROX-Subdocumento4.md#tab:servicios-nube) del apartado [4.2.3](LAFROX-Subdocumento4.md#sec:servicios-nube). En esta región se concentran la operación productiva, la analítica y los servicios de detección, cumplimiento y gobierno; todos son servicios administrados, de modo que la solución no opera servidores en la nube.

### 4.3.1.4 Sitio on-premise: CD Talca (sala técnica secundaria)

El caso fija para el CD de Talca una sala técnica secundaria ``dimensionada para sostener recepción, preparación y despacho durante un corte'', y advierte que la sala actual de 25 m2 no cumple el Capítulo 6 de las Bases Técnicas Transversales (RT-06.01 del caso; Bases Técnicas del caso, cap. 15, p. 26). Conforme a la tipología del numeral 6.1 de las Bases Técnicas Transversales (cap. 6, p. 14), no se aplica íntegramente a este sitio el conjunto de exigencias de una sala técnica principal, sino el subconjunto dimensionado al sitio: energía, climatización, control de acceso, detección de incendio y monitoreo. El numeral 6.1 de las Bases Técnicas Transversales (cap. 6, p. 14) exige declarar la tipología y justificar el dimensionamiento, y advierte que ``sobredimensionar el recinto es tan penalizado como subdimensionarlo: ambos revelan que el cálculo de capacidad no se hizo''. El equipamiento real que la sala debe alojar y los cálculos eléctrico y térmico desarrollados a continuación determinan su superficie proyectada; la Figura [27](LAFROX-Subdocumento4.md#fig:recinto-talca) muestra su distribución interna por zonas y líneas de acceso.

La sala aloja el siguiente equipamiento:

- El núcleo del componente on-premise, con el motor WMS y el borde operacional del CD sobre un clúster virtualizado de tres nodos con redundancia N+1, que tolera la pérdida de cualquier nodo manteniendo quórum.

- Una NAS local con el respaldo de recuperación rápida.

- Los dos firewalls de la frontera del sitio.

- El servidor del ERP de 2017 del CLIENTE, trasladado desde la sala actual.

La sala actual de 25 m2 del edificio de oficinas aloja hoy el servidor del ERP de 2017. Ese servidor se traslada sin cambios de software al rack R01 de la sala nueva, durante la Etapa 1, después del hito H3 y antes de la marcha blanca de Talca. El traslado ocurre en una ventana dominical, después de un respaldo completo verificado. Así, el ERP que emite las guías queda con UPS en N+1, generador de 24 horas, climatización redundante y control de acceso. La sala actual queda sin servidores y se libera para otro uso del CLIENTE (Bases Técnicas del caso, cap. 17, p. 33). Si el servidor tiene una sola fuente, se conecta a los circuitos A y B mediante un conmutador de transferencia de rack (RT-08.04; Bases Técnicas Transversales, cap. 8, p. 18).

El listado completo de componentes de sala (UPS, generador, climatización, seguridad física, extinción, cableado y gabinetes) y del equipamiento de cómputo y red que alojan los gabinetes se entrega en el Formulario T-11. La ocupación por rack y el margen de crecimiento se declaran en la Figura [26](LAFROX-Subdocumento4.md#fig:racks-talca).

Para la disponibilidad y la redundancia la disponibilidad de infraestructura comprometida es del 99,95 % mensual por componente en energía del recinto, climatización, red y comunicaciones, servidores y cómputo, y motor de base de datos. Además se sostiene con redundancia N+1 en energía y climatización, con generación autónoma y con monitoreo continuo con alertamiento. No se invoca una clasificación de instalación de terceros (ejemplo un nivel TIER certificado), por lo que los niveles de disponibilidad de infraestructura del numeral 7.2 de las Bases Técnicas Transversales (cap. 7, p. 17) son un medio, no un fin y el compromiso que se mide y se penaliza es el de la transacción de negocio de extremo a extremo.

La Figura [25](LAFROX-Subdocumento4.md#fig:cd-talca) muestra cómo se conecta el equipamiento de la sala con la bodega, la cadena de frío y el ERP.

**Figura 25 — Arquitectura física del sitio on-premise del CD Talca**

![Arquitectura física del sitio on-premise del CD Talca](https://raw.githubusercontent.com/PatricioH315/LafroX/d397c30ff8ad232ec4e3ea02caf5f3cb6800a547/04/figuras/centros_de_datos/Arquitectura_Fisica_CD_Talca.png)

Fuente: elaboración propia.

<a id="fig:cd-talca"></a>

La fibra D-03 es el enlace principal, LTE D-04 el segundo camino y Starlink D-06 el tercero en espera caliente; los tres llegan al par de firewalls, uno activo y otro pasivo. Starlink permanece encendido, con el túnel IPsec establecido y BGP con menor preferencia, y toma el tráfico solo si fallan fibra y LTE. En ese caso, la calidad de servicio prioriza DMS y WAL de Talca, la salida del broker y el outbox, las guías hacia el ERP y el SII, la identidad y la telemetría crítica. El terminal permanece encendido porque adquirir satélites y negociar el túnel durante una falla tardaría minutos; la tarifa plana no agrega costo por ello. Detrás, los dos switches de núcleo y el switch de gestión reparten la red hacia el clúster Proxmox VE con Ceph de tres nodos. El clúster aloja seis máquinas virtuales: VM-01 con el núcleo del WMS, VM-02 con PostgreSQL, VM-03 con RabbitMQ, VM-04 con la capa anticorrupción y los dos procesos de `erp-sync` que conversan con el ERP de 2017, VM-05 con la caché de Keycloak y VM-06 con el colector ADOT y el agente de Systems Manager. La línea punteada representa a AWS DMS, que lee los cambios de VM-02 por la VPN para replicarlos en Aurora. En la bodega, los terminales MC9400 y las impresoras de andén trabajan por Wi-Fi 6E contra el WMS; en la cadena de frío, los sensores entregan sus lecturas a los dos gateways IoT, que las publican por MQTTS y bloquean el despacho ante una excursión crítica y sostenida. El respaldo de recuperación rápida queda en la NAS WORM. La figura muestra que todo lo que la bodega necesita para recibir, preparar y despachar está dentro del sitio, y que la pérdida de un nodo no detiene la operación, porque sus máquinas virtuales se reinician en los otros dos.

La cadena eléctrica sigue esta secuencia: empalme → tablero general → transferencia automática → UPS → PDU del rack → fuente del equipo → servidor.

Esta cadena consta de UPS de doble conversión on-line en configuración N+1 con autonomía mínima de 30 minutos a plena carga y generación autónoma para un rango mínimo de 24 horas continuas, con estanque de combustible dimensionado y contrato de reabastecimiento declarado. La instalación eléctrica es independiente de la del resto del edificio y conforme a la normativa eléctrica chilena vigente, incluida la NCh Elec. 2777; se revisa y mide semestralmente, con informe entregable al CLIENTE, conforme a RT-06.10 (Bases Técnicas Transversales, cap. 6, p. 15).

Para el cálculo de carga eléctrica se usa una cota conservadora por equipo, según la Tabla [34](LAFROX-Subdocumento4.md#tab:4-3-1): en los nodos, la suma de sus dos fuentes, y en los demás equipos, su potencia máxima de ficha. Para el servidor del ERP, cuya ficha no se conoce, se usa la misma cota de un nodo, que se confirma al medirlo en el levantamiento. El Formulario T-11 declara los mismos valores por equipo.

<a id="tab:4-3-1"></a>

**Tabla 34 — Carga eléctrica de TI proyectada del recinto**

| **Equipo** | **Cantidad** | **Potencia de placa por unidad** | **Subtotal** |
| --- | --- | --- | --- |
| Nodo de cómputo del clúster (servidor rack 2U, un procesador) | 3 | 1.600 W (2 fuentes de 800 W) | 4.800 W |
| NAS local | 1 | 400 W | 400 W |
| Firewall del perímetro del sitio | 2 | 150 W | 300 W |
| Conmutador de núcleo (switch core) | 2 | 150 W | 300 W |
| Switch de gestión | 1 | 50 W | 50 W |
| Servidor del ERP de 2017 (del CLIENTE, 2U) | 1 | 1.600 W (cota hasta medirlo) | 1.600 W |
| **Carga TI base** | | | **7.450 W** |
| Consola KVM (cubierta por el margen) | 1 | 50 W | Incluida en el margen |
| Margen de crecimiento a tres años (20 %) | | | + 1.490 W |
| **Carga TI de diseño** | | | **8.940 W ≈ 8,9 kW** |

Fuente: elaboración propia.

El cálculo eléctrico sigue estos pasos:

- Potencia aparente y UPS: con factor de potencia 0,95, 8,9 kW ÷ 0,95 ≈ 9,4 kVA; al 80 % de utilización, 9,4 kVA ÷ 0,8 ≈ 11,8 kVA. El UPS seleccionado es modular de 15 kVA, de doble conversión on-line, en configuración N+1 y con bypass de mantenimiento.

- PUE: la suma de 8,9 kW de carga TI, ≈ 2,7 kW de climatización de precisión, ≈ 0,4 kW de climatización de la sala de UPS, ≈ 0,6 kW de iluminación y apoyo y ≈ 0,78 kW de pérdidas del UPS es ≈ 13,4 kW; 13,4 ÷ 8,9 ≈ 1,5. Los gateways IoT y sus fuentes agregan ≈ 0,1 kW al consumo del sitio, hasta ≈ 13,5 kW, pero quedan fuera del PUE de la sala. El PUE estimado y la carga declarada satisfacen RT-06.11 (Bases Técnicas Transversales, cap. 6, p. 15). El numerador se mide en el tablero del recinto y el denominador a la salida de las PDU, semestralmente y con informe entregable.

- Generador: la carga del sitio de ≈ 13,5 kW, con factor de potencia 0,8, requiere ≈ 13,5 ÷ 0,8 ≈ 16,9 kVA. Se especifica un grupo electrógeno de 25 kVA, que deja la carga de diseño en el 68 % de su capacidad, bajo el 80 %, con estanque para 24 horas continuas y contrato de reabastecimiento.

La climatización de precisión para la operación continua es redundante en configuración N+1 y controla la temperatura y la humedad relativa dentro de los rangos que recomienda el fabricante del equipamiento.

Para calcular la carga térmica, se considera que cada kW eléctrico consumido por el equipamiento se disipa físicamente como aproximadamente 1 kW de calor sensible (≈ 3.412 BTU/h). Como el UPS está en su propia sala, la carga térmica de la sala de servidores corresponde a la carga TI de diseño, como resume la Tabla [35](LAFROX-Subdocumento4.md#tab:4-3-2):

<a id="tab:4-3-2"></a>

**Tabla 35 — Carga térmica sensible proyectada del recinto**

| **Origen del calor** | **Potencia equivalente** |
| --- | --- |
| Carga TI de diseño | 8.940 W |
| **Carga térmica sensible de diseño** | **≈ 8,9 kW** |

Fuente: elaboración propia.

Sobre esa carga se instalan dos unidades de climatización de precisión de 10 kW cada una, en configuración N+1; una sola cubre los 8,9 kW de diseño. La temperatura y la humedad relativa se controlan dentro de los rangos del fabricante del equipamiento. La sala de UPS y baterías dispone de climatización de confort propia de 3,5 kW (≈ 12.000 BTU/h), que mantiene 20–25 °C, y de ventilación; disipa las pérdidas del UPS (≈ 0,78 kW) y el calor de carga de las baterías.

La consola KVM, con 50 W de potencia de placa, el conmutador de transferencia del ERP y los equipos terminales de acceso del operador (ONT de fibra, router LTE y terminal Starlink) quedan cubiertos por el margen de diseño del 20 % de la Tabla [34](LAFROX-Subdocumento4.md#tab:4-3-1), sin alterar el UPS de 15 kVA ni el generador de 25 kVA.

La protección contra incendios reúne estos elementos:

- Detección temprana por aspiración de aire con tecnología láser, tipo AnaLASER.

- Extinción automática con agente limpio tipo FM-200 con aprobación UL e instalación conforme a norma NFPA, con botón de aborto.

- Sistema secundario de extintores portátiles habilitados con mantención y certificación vigentes.

El sistema de detección y extinción se integra al monitoreo en línea y notifica al NOC y a la contraparte del CLIENTE.

La Figura [26](LAFROX-Subdocumento4.md#fig:racks-talca) muestra cómo se reparte el equipamiento de cómputo y red en los dos racks de la sala.

**Figura 26 — Distribución de U y ocupación proyectada de los racks del CD Talca**

![Distribución de U y ocupación proyectada de los racks del CD Talca](https://raw.githubusercontent.com/PatricioH315/LafroX/d397c30ff8ad232ec4e3ea02caf5f3cb6800a547/04/figuras/centros_de_datos/Racks_CD_Talca.png)

Fuente: elaboración propia.

<a id="fig:racks-talca"></a>

El rack R01 aloja los tres nodos del clúster, de 2U cada uno, la consola KVM, la NAS WORM, el servidor del ERP de 2U y su conmutador de transferencia; el rack R02 aloja el ODF, los paneles, los dos switches de núcleo, el switch de gestión, el par de firewalls y la bandeja del operador con la ONT de fibra y el router LTE. R01 ocupa 15U de 42 (36 %) y R02, 12U (29 %). La carga de R01 es de 6,8 kW base y 8,2 kW de diseño, y la de R02, de 0,65 kW base y 0,8 kW de diseño; las cargas base suman los 7.450 W de la Tabla [34](LAFROX-Subdocumento4.md#tab:4-3-1), y las de diseño, los 8,9 kW que resultan al agregar el margen de 20 %. La figura dibuja comprimidos los bloques libres e indica la posición de cada equipo en U. Los racks de servidores son independientes de los racks de equipos de comunicación. La ocupación proyectada reserva margen de crecimiento a tres años, coherente con el 20 % de reserva de la carga eléctrica (Tabla [34](LAFROX-Subdocumento4.md#tab:4-3-1)), de modo que la ocupación declarada y su margen quedan fijados en la figura y en el Formulario T-11.

El control de acceso y la seguridad física del recinto comprenden:

- Seguridad física y control de acceso biométrico basado principalmente en biometría facial con AFIS como respaldo.

- Registro de todo ingreso y egreso en una bitácora auditable con identificación, fecha, hora y motivo.

- Un espacio para atender a las personas en proceso de enrolamiento entre el acceso principal y el término del pasillo de la zona de control, además de una estación de enrolamiento fuera de las instalaciones del recinto técnico.

- Un acceso al término del pasillo que impide el paso de más de una persona a la vez, con nueva verificación de identidad previa al ingreso.

- Videovigilancia y monitoreo IP con imágenes en línea disponibles al menos los últimos 30 días y respaldo recuperable.

Las instalaciones sanitarias, las zonas de seguridad ante emergencia y las áreas exteriores existentes en el edificio del CLIENTE se utilizan, sin implementarlas nuevamente dentro del recinto. La bitácora auditable se conserva por un período de retención no inferior a cinco años, coherente con el piso de retención de la auditoría que fija RT-16.10 (Bases Técnicas Transversales, cap. 16, p. 29).

Los equipos de energía y climatización y los controles de acceso descritos se ordenan físicamente como muestra la Figura [27](LAFROX-Subdocumento4.md#fig:recinto-talca), que distribuye el recinto por zonas y líneas de acceso.

**Figura 27 — Distribución interna del recinto técnico del CD Talca por zonas y líneas de acceso**

![Distribución interna del recinto técnico del CD Talca por zonas y líneas de acceso](https://raw.githubusercontent.com/PatricioH315/LafroX/d397c30ff8ad232ec4e3ea02caf5f3cb6800a547/04/figuras/centros_de_datos/Recinto_CD_Talca.png)

Fuente: elaboración propia.

<a id="fig:recinto-talca"></a>

La distribución ordena el recinto en profundidad progresiva. En el exterior quedan el grupo electrógeno con su estanque, el empalme con la transferencia automática entre red y generador, las condensadoras de la climatización y la llegada independiente de fibra, LTE y Starlink. La fibra y LTE ingresan al edificio por puntos separados y siguen ductos independientes hasta la sala, conforme a RT-06.32 (Bases Técnicas Transversales, cap. 6, p. 17); Starlink constituye el tercer camino. La línea técnica reúne la sala de UPS y baterías, el tablero eléctrico independiente del recinto y la acometida de comunicaciones, junto con la zona de trabajo y la zona de respaldo. La línea restringida contiene solo la sala de servidores y comunicaciones, con los racks R01 y R02, la climatización de precisión y la detección y extinción. El ingreso sigue un único recorrido: acceso principal, pasillo de control con espacio de enrolamiento, esclusa que admite una persona a la vez con nueva verificación y, recién entonces, la sala; la estación de enrolamiento y los baños quedan fuera del recinto. Los puestos de trabajo y el área de respaldo quedan en la línea técnica, separados de la sala de equipos, de modo que las labores habituales de operación no exigen ingresar a la línea restringida. La separación física de generadores y baterías respecto del área de servidores evita que una falla de energía o de clima contamine el cómputo, y deja al proveedor de fibra y al de climatización sin cruzar la última línea del recinto.

El sitio monitorea en línea la temperatura, la humedad y la presencia de agua, con alertamiento integrado a la plataforma de observabilidad. El estado de los puntos controlados del recinto converge en la plataforma de monitoreo, con destinatario, canal, tiempo de respuesta y procedimiento escrito. La observabilidad reutiliza el mecanismo del sitio on-premise hacia la nube que define la arquitectura de despliegue del apartado [4.2.4](LAFROX-Subdocumento4.md#sec:despliegue). La convergencia en un solo tablero constituye la plataforma de observabilidad del sitio. No se declara una plataforma DCIM/BMS de terceros porque las Bases no la exigen y el monitoreo ambiental y de alertas se satisface con el monitoreo en línea y su alertamiento integrado.

El cómputo local corre sobre un clúster virtualizado de tres nodos N+1 con quórum real. Ceph distribuye tres réplicas sobre NVMe sin RAID y tolera la pérdida de un nodo; el respaldo local reside en el NAS D-05 con RAID 6. La selección se justifica en ADR-10 (Anexo 4-O). La instancia de escritura VM-02 se reinicia en otro nodo ante una falla.

## 4.3.2 Especificaciones Data Center Secundario

<a id="sec:e-especificaciones-del-sitio-secundario-y-"></a>

El Data Center Secundario cubre dos dominios de recuperación. La región AWS us-east-1 restituye el dominio de nube ante la pérdida de sa-east-1. La plataforma de nube de la región activa restituye el WMS de Talca ante la pérdida de su sala técnica; si también se pierde sa-east-1, la región activa pasa a ser us-east-1 tras la promoción. Concepción y los cross-docking son sitios operacionales autónomos y no reciben la carga de Talca. Los objetivos para servicios críticos son RTO ≤ 4 h y RPO ≤ 15 min, con respaldo 3-2-1-1-0 y ensayos semestrales. El Formulario T-11 detalla los recursos de recuperación.

### 4.3.2.1 Modalidad del sitio secundario

La modalidad del dominio de nube es activo-pasiva en caliente. La región us-east-1 mantiene una réplica funcional de aplicación y datos con capacidad reducida; ante la declaración del incidente se promueve Aurora y se escala la aplicación. El dominio de Talca conserva en Aurora una copia continua de su WMS y la misma imagen `wms_only` lista para ejecutarse en ECS Fargate. ADR-09 (Anexo 4-O) registra la selección frente a activo-activo y a la restauración en frío. La primera alternativa exigiría coordinar escrituras simultáneas entre regiones; la segunda agrega la reconstrucción de la plataforma al tiempo de recuperación.

### 4.3.2.2 Región o sitio de recuperación

La Tabla [36](LAFROX-Subdocumento4.md#tab:4-3-3) compara los dos destinos de recuperación con sus distancias y amenazas comunes.

<a id="tab:4-3-3"></a>

**Tabla 36 — Destinos de recuperación: distancia y amenazas comunes**

| **Destino** | **Dominio** | **Distancia** | **Amenazas comunes** |
| --- | --- | --- | --- |
| AWS us-east-1 | Nube de sa-east-1 | ≈ 7.700 km desde sa-east-1 | No comparte sismicidad ni red eléctrica con Brasil. |
| Nube sa-east-1; us-east-1 en contingencia regional | WMS de Talca | ≈ 2.700 km de Talca a sa-east-1 | No comparte sismicidad ni suministro eléctrico con Talca. |

Fuente: elaboración propia.

Las distancias de la tabla separan los dominios de falla. La región secundaria se sitúa en Virginia del Norte, Estados Unidos, y la primaria en São Paulo, Brasil. Ambas implican transferencia internacional de datos personales desde Chile. AWS actúa como encargado del tratamiento por cuenta del CLIENTE, responsable de los datos, mediante un contrato de encargo que incorpora las cláusulas contractuales tipo aprobadas para la Ley N° 21.719 (Ley N° 21.719, 2024). Los datos se cifran en reposo con claves KMS administradas por el CLIENTE y en tránsito; se registran las actividades de tratamiento y se controlan y auditan los accesos.

La réplica secundaria se limita a los datos necesarios para continuidad. La analítica opera en sa-east-1 y se copia de forma diferida a la región secundaria, porque conserva los cinco años de registros de temperatura y de trazabilidad de lote; la copia no incluye las posiciones de flota, solo los kilómetros agregados que alimentan el costo de servir. Las posiciones de flota, que son geolocalización de personas trabajadoras, no salen de sa-east-1 y se protegen con copias inmutables en otra cuenta de esa región; ante la pérdida total de sa-east-1 se pierde su historial, que solo alimenta el costo de servir. La región secundaria no se utiliza para consultas de negocio durante la operación normal. El artículo 23 de las Bases Administrativas sujeta la residencia declarada a aprobación del CLIENTE (Bases Administrativas, art. 23, p. 17), hito contractual de la Etapa 1. La propuesta declara sa-east-1 y us-east-1, y presenta para esa aprobación la base de licitud, el contrato de encargo y los resguardos descritos. Se elige us-east-1 porque ofrece todos los servicios de recuperación del diseño: Aurora Global Database, DynamoDB Global Tables, replicación de S3, ECS Fargate y AWS Backup. Una sola región no permite recuperarse de su propia pérdida con un RTO de 4 horas y un RPO de 15 minutos.

### 4.3.2.3 Replicación

La replicación continua usa un mecanismo por dominio, resumido en la Tabla [37](LAFROX-Subdocumento4.md#tab:4-3-4).

<a id="tab:4-3-4"></a>

**Tabla 37 — Replicación y RPO por dominio de datos**

| **Dominio de datos** | **Mecanismo de replicación** | **RPO / retraso declarado** |
| --- | --- | --- |
| Transaccional en nube (crítico) | Aurora Global Database replica la base hacia la región secundaria. | El RPO objetivo es ≤ 15 min y se mide en cada ensayo. |
| WMS de Talca (crítico) | AWS DMS replica PostgreSQL VM-02 por la VPN sobre fibra, LTE o Starlink. | El RPO objetivo es ≤ 15 min y se mide en cada ensayo. |
| Mensajes críticos de cada sitio | El outbox local retiene 24 h de eventos, aun los ya enviados, y el shipper los reenvía a SQS FIFO de la región activa. | El RPO objetivo es ≤ 15 min y se mide en cada ensayo. |
| Evidencias y documentos tributarios (críticos) | S3 Replication Time Control replica los objetos entre regiones y un evento de umbral dispara la recopia de los rezagados. | El RPO objetivo es ≤ 15 min y se mide en cada ensayo. |
| Telemetría de temperatura (crítica) | DynamoDB Global Tables replica las lecturas entre regiones. | El RPO objetivo es ≤ 15 min y se mide en cada ensayo. |
| Analítica (no crítica) | Los respaldos se copian de forma diferida a us-east-1, sin las posiciones de flota. | El RPO es ≤ 24 h. |
| Posiciones de flota (no críticas) | Se conservan solo en sa-east-1, con copia inmutable en otra cuenta de esa región. | El RPO es ≤ 24 h dentro de sa-east-1. |
| Mensajes no críticos | El outbox local conserva los eventos para reenviarlos a la cola de la región activa. | El RPO es ≤ 24 h. |

Fuente: elaboración propia.

La tabla separa la copia DMS del WMS de Talca, destinada a su recuperación, del estado central consolidado por eventos idempotentes de todos los sitios. AWS DMS lee VM-02 por el túnel IPsec; la única conexión iniciada desde la nube hacia un sitio termina en esa VM. Aurora Global Database, DynamoDB Global Tables y la replicación de S3 protegen el dominio de nube. S3 Replication Time Control ofrece que el 99,99 % de los objetos se replique en 15 min; se vigila la métrica de objetos pendientes y un evento de umbral superado dispara la recopia. DynamoDB Global Tables replica de forma asíncrona con retraso típico de segundos y una alarma de `ReplicationLatency` a los 60 s. La edad de las réplicas y las colas se mide continuamente y todos los RPO se verifican en los ensayos semestrales.

### 4.3.2.4 RPO y RTO

La Tabla [38](LAFROX-Subdocumento4.md#tab:4-3-5) fija los objetivos medidos en las pruebas de recuperación.

<a id="tab:4-3-5"></a>

**Tabla 38 — Objetivos de continuidad**

| **Activo** | **Objetivo** | **Valor declarado** |
| --- | --- | --- |
| Servicios críticos | Tiempo de recuperación (RTO) | ≤ 4 h |
| Servicios críticos | Punto de recuperación (RPO) | ≤ 15 min |
| Transacción crítica de extremo a extremo | Disponibilidad mensual | ≥ 99,9 % |
| Infraestructura por componente | Disponibilidad mensual | 99,95 % |

Fuente: elaboración propia.

El RPO de la tabla se sustenta en la extracción continua de datos críticos por tres dominios de falla distintos en los CD: fibra terrestre D-03, red celular D-04 y satélite D-06. En Talca y Concepción, Starlink permanece encendido como tercer camino en espera caliente, con el túnel IPsec establecido y BGP con menor preferencia; toma el tráfico solo si fallan fibra y LTE. En esa situación, la calidad de servicio prioriza DMS y WAL de Talca, la salida del broker y el outbox, las guías hacia el ERP y el SII, la identidad y la telemetría crítica. El terminal encendido evita los minutos necesarios para adquirir satélites y negociar el túnel durante la falla, sin costo adicional por la tarifa plana. La caída simultánea de fibra y LTE, incluso ante un terremoto que afecte la infraestructura terrestre, permite mantener la réplica de Talca y la publicación de eventos dentro del RPO mediante Starlink. En los cross-docking, Starlink es el camino principal y LTE de dos proveedores constituye el respaldo. La bodega conserva 24 h de operación local aunque cambie el camino WAN.

Queda como riesgo residual la falla simultánea de los tres caminos seguida de la destrucción del sitio antes de reponer alguno: en esa secuencia, la última copia remota podría exceder 15 min. Se mitiga con alarmas de retraso de replicación a los 5 y 15 min, reposición del enlace por el proveedor, preemisión de guías al cerrar la carga y conservación local en el NAS WORM de Talca. La autonomía local de 24 h se mantiene durante la atención del incidente. El RTO se verifica levantando la misma imagen del WMS de Talca en Fargate de la región activa y conectando sus terminales por la VPN.

### 4.3.2.5 Procedimiento de conmutación

<a id="sub:conmutacion-regional"></a>

La pérdida regional se atiende con la secuencia de la Tabla [39](LAFROX-Subdocumento4.md#tab:4-3-6). La promoción de Aurora requiere autorización del CLIENTE; Route 53 cambia el tráfico solo después de restituir y validar los servicios.

<a id="tab:4-3-6"></a>

**Tabla 39 — Secuencia de conmutación de región**

| **Paso** | **Acción** | **Ejecución** | **Tiempo** |
| --- | --- | --- | --- |
| 1 | Detección por verificación de salud y alarmas | Route 53 y CloudWatch | < 5 min |
| 2 | Declaración del incidente y autorización de la promoción | CLIENTE, con aviso por SNS | ≤ 30 min |
| 3 | Promoción de Aurora en us-east-1 | Systems Manager Automation | 15–20 min |
| 4 | Escalado de la plataforma de aplicación a carga completa | Systems Manager Automation | ≤ 30 min |
| 5 | Restitución de Keycloak, API pública y privada y Verified Access | Systems Manager Automation | < 15 min |
| 6 | Validación funcional con escrituras de pedidos y sincronización de prueba | Operación | < 15 min |
| 7 | Cambio del tráfico a us-east-1 en Route 53, con TTL de 60 s preparado | Systems Manager Automation | < 5 min |
| 8 | Reconexión de túneles y brokers y redirección de shippers y `erp-sync` a las colas regionales | Systems Manager Automation | < 15 min |

Fuente: elaboración propia.

El peor caso secuencial suma 5 + 30 + 20 + 30 + 15 + 15 + 5 + 15 = 135 min, equivalentes a 2 h 15 min y dentro del RTO de 4 h; el escalado del paso 4 puede ejecutarse en paralelo con la promoción del paso 3 sin reducir este presupuesto conservador. El plan de continuidad designa a un autorizador titular y a un suplente del CLIENTE con facultad delegada; si el titular no responde en 15 min, decide el suplente dentro del máximo de 30 min. La decisión se ensaya en los simulacros semestrales. Las imágenes de ECR se replican entre regiones y las colas SQS FIFO, SQS y SNS equivalentes existen vacías en la región secundaria por infraestructura como código, de modo que el paso 8 redirige allí los `shippers` y `erp-sync` sin depender de la región primaria. Al terminar el paso 8, cada shipper vuelve a publicar su outbox de las últimas 24 h y M2 central vuelve a publicar las solicitudes de reserva pendientes que guarda Aurora. Los consumidores descartan por UUID lo que Aurora ya registró, y `erp-sync` responde una solicitud repetida con el resultado ya registrado. Así, lo aceptado y no consumido en sa-east-1 no se pierde. La preparación de los registros con TTL de 60 s antecede al incidente. No se conmuta automáticamente el tráfico por salud antes de promover la base; el retorno automático permanece deshabilitado. Cada paso queda registrado por Systems Manager y el personal del CLIENTE puede ejecutarlo tras la transferencia de conocimiento.

Cuando se pierde solo la sala de Talca, se detiene la tarea DMS, se habilita para escritura la copia del WMS de Talca en Aurora y se levanta el perfil `wms_only` de la misma imagen en ECS Fargate de la región activa. Los terminales y periféricos de Talca se conectan por VPN mediante fibra, LTE o Starlink. La pérdida de la sala incluye el servidor del ERP, que es del CLIENTE y no se modifica. Mientras el CLIENTE lo restituye, salen solo las cargas con guía preemitida, cuyo folio conserva la copia del WMS en Aurora. Una guía nueva espera el ERP restituido, y `erp-sync` y la ACL se reinstalan desde la misma imagen. Si la región primaria tampoco está disponible, se promueve primero us-east-1 con la secuencia regional descrita y allí se levanta el perfil de Talca. Concepción continúa atendiendo exclusivamente su propia bodega.

### 4.3.2.6 Procedimiento de retorno

El retorno regional se realiza tras resincronizar las réplicas, conciliar las transacciones de la contingencia y transferir los eventos retenidos. La operación valida escrituras y consultas en la región primaria, cambia coordinadamente Route 53 y registra el tiempo real empleado. Cada ensayo semestral incluye el retorno.

Para devolver el WMS a Talca se reconstruye su clúster, se carga VM-02 desde Aurora y se invierte temporalmente el sentido de la replicación hasta igualar los datos. Se detienen las escrituras en nube, se verifica la igualdad, se habilita el escritor local y se reconectan los terminales al WMS del sitio. El corte de vuelta se realiza fuera de las ventanas protegidas.

### 4.3.2.7 Pruebas del plan de recuperación y respaldos

Dos veces al año se ensaya la pérdida regional con escrituras de pedidos y sincronización en us-east-1; con la misma frecuencia se simula la pérdida de la sala de Talca y se levanta su WMS en Fargate sobre la copia en Aurora. Se miden RTO y RPO en cada ensayo y se exige el cumplimiento del 100 % de ambos objetivos. La restauración mensual de respaldos y la inyección de fallas se describen en la sección [4.2.4.6](LAFROX-Subdocumento4.md#sub:6-verificacion-de-la-continuidad).

# Referencias

- Amazon Web Services. (s. f.-a). *Request validation for REST APIs*. <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html>

- Amazon Web Services. (s. f.-b). *Lambda authorizers*. <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html>

- Amazon Web Services. (s. f.-c). *Private integrations*. <https://docs.aws.amazon.com/apigateway/latest/developerguide/private-integration.html>

- Amazon Web Services. (s. f.-d). *GuardDuty Runtime Monitoring*. <https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring.html>

- Amazon Web Services. (s. f.-e). *How Runtime Monitoring works with Fargate (Amazon ECS only)*. <https://docs.aws.amazon.com/guardduty/latest/ug/how-runtime-monitoring-works-ecs-fargate.html>

- Angular. (2026a). *Release policy*. <https://angular.dev/reference/releases>

- Angular. (2026b). *Version compatibility*. <https://angular.dev/reference/versions>

- International Organization for Standardization. (2019). *ISO 22301:2019: Security and resilience—Business continuity management systems—Requirements*. <https://www.iso.org/standard/75106.html>

- International Organization for Standardization. (2022a). *ISO/IEC/IEEE 42010:2022: Software, systems and enterprise—Architecture description*. <https://www.iso.org/standard/74393.html>

- International Organization for Standardization. (2022b). *ISO/IEC 27001:2022*. <https://www.iso.org/standard/27001>

- International Organization for Standardization. (2022c). *ISO/IEC 27002:2022*. <https://www.iso.org/standard/75652.html>

- International Organization for Standardization. (2025). *ISO/IEC 27031:2025: Cybersecurity—Information and communication technology readiness for business continuity*. <https://www.iso.org/standard/27031>

- Laravel. (2026). *Release notes*. <https://laravel.com/framework/docs/releases>

- Ley N.° 21.719. (2024). *Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales*. Diario Oficial de la República de Chile.

- National Institute of Standards and Technology. (2020). *Zero trust architecture* (Special Publication 800-207). U.S. Department of Commerce. <https://doi.org/10.6028/NIST.SP.800-207>

- PHP. (2026). *Supported versions*. <https://www.php.net/supported-versions.php>

- Distribuidora Puelche S.A. (2026c). *Caso 02: Logística. Especificaciones del problema y operación de Distribuidora Puelche S.A.* (Licitación N.º TFEP-01/2026).

- Distribuidora Puelche S.A. (2026b). *Bases Técnicas Transversales de Licitación N.º TFEP-01/2026*.

- Distribuidora Puelche S.A. (2026a). *Bases Administrativas de Licitación N.º TFEP-01/2026*.

- PostgreSQL. (2026). *Versioning policy*. <https://www.postgresql.org/support/versioning/>

- RabbitMQ. (2026). *Release information*. <https://www.rabbitmq.com/release-information>

- Servicio de Impuestos Internos. (2018). *Oficio 781: acuse de recibo*. <https://www.sii.cl/normativa_legislacion/jurisprudencia_administrativa/ley_impuesto_ventas/2018/ja781.htm>

- Servicio de Impuestos Internos. (s. f.-a). *Representación de guía de despacho electrónica*. <https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6599.htm>

- Servicio de Impuestos Internos. (s. f.-b). *Formato de recibos*. <https://www.sii.cl/factura_electronica/desc_19983.pdf>

# Declaración de uso de IA

En cumplimiento de la sección 7.2 de las Aclaraciones de la licitación, la tabla siguiente declara el uso de herramientas de inteligencia artificial en este subdocumento, con la revisión humana de cada parte. La declaración se consolida en el Formulario A-6.

**Tabla 40 — Uso de IA en el Subdocumento 4**

<a id="tab:uso-ia-logica"></a>

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
| --- | --- | --- | --- | --- | --- |
| 4.1 | OpenAI Codex | Redacción, coherencia y verificación documental. | Alto | Alto en vistas asistidas | [[REVISIÓN HUMANA]] |
| 4.1.1 | OpenAI Codex | Especificaciones y soporte de tecnologías. | Alto | No aplica | [[REVISIÓN HUMANA]] |
| 4.2 | Codex | Apoyo a la redacción y verificación de consistencia del apartado | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 4.3 | Codex | Apoyo a la redacción y verificación de consistencia del apartado | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 4-A | Codex | Eventos canónicos. | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 4-B | Codex | Gobierno de integración. | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 4-C | Codex | Carga masiva. | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 4-D | Codex | Módulos y responsabilidades. | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 4-E | Codex | Trazabilidad funcional. | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 4-F | Codex | Límites de contexto. | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 4-G | Codex | Interfaces internas. | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 4-H | Codex | Interfaces externas. | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 4-I | Codex | Cálculos de volumen. | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 4-J | Codex | Funciones offline. | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 4-K | Codex | Reconciliación. | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 4-L | Codex | Decisiones del caso. | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 4-M | Codex | Protocolos de aceptación. | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 4-N | Codex | Correspondencia lógica. | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 4-O | Codex | Especificación y trazabilidad. | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 4-P | Codex | Especificación y trazabilidad. | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 4-Q | Codex | Especificación y trazabilidad. | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 4-R | Codex | Especificación y trazabilidad. | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 4-S | Codex | Especificación y trazabilidad. | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 4-T | Codex | Especificación y trazabilidad. | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 4-U | Codex | Especificación y trazabilidad. | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 4-V | Codex | Especificación y trazabilidad. | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 4-W | Codex | Apoyo a la redacción y verificación de consistencia del apartado | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| T-11 | Codex | Apoyo a la redacción y verificación de consistencia del apartado | Alto | Ninguno | [[REVISIÓN HUMANA]] |
