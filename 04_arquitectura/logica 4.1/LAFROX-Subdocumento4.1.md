# LafroX — Arquitectura lógica 4.1

[Cuerpo integrado](../LAFROX-Subdocumento4.md) · [Anexos](../LAFROX-Subdocumento4-Anexos.md)

<a id="h-04-partes-4-1-logica-01-introduccion-tex-1"></a>

# 4 Introducción a la Arquitectura lógica y física de la solución

<a id="cap-arquitectura-logica"></a>

El capítulo 4 explica cómo la solución sostiene la operación distribuida de Puelche. La arquitectura lógica define las responsabilidades, los datos y los contratos que permiten ejecutar las capacidades del capítulo 3; la arquitectura física acredita su emplazamiento y continuidad, y la estrategia de centros de datos completa su recuperación. Esta descripción se relaciona con el modelo de datos del Subdocumento 5. Los catálogos, el registro de decisiones de arquitectura (Anexo 4-O) y la memoria de cálculo del dimensionamiento (Anexo 4-W) se entregan en el archivo LAFROX-Subdocumento4-Anexos, y el detalle del equipamiento, en el Formulario T-11, entregado como archivo propio.

<a id="h-04-partes-4-1-logica-01-introduccion-tex-2"></a>

## 4.1 Arquitectura lógica

<a id="sec-arquitectura-logica"></a>

Los anexos 4-A a 4-N detallan eventos, módulos, interfaces, reglas y correspondencias. El Anexo 4-O reúne el registro único ADR-01 a ADR-22; el 4-P presenta las tecnologías y su actualización; los 4-Q y 4-R, amenazas y controles; el 4-S, los puntos de vista y sus reglas de correspondencia; el 4-T, el desempeño; el 4-U, la evidencia documental; y el 4-V, los protocolos de aceptación. El archivo independiente de anexos comienza con un catálogo navegable: cada entrada identifica la sección que la utiliza y el requisito que respalda.

Este apartado desarrolla las responsabilidades y los contratos de la solución y su correspondencia con el esquema y la explicación de 3.3 y 3.4. La correspondencia se establece por capacidad: recepción e inventario (M1–M2), preventa y planificación (M3–M4), preparación y reparto (M5–M6), rendición y devoluciones (M7–M8), calidad y analítica (M9–M10), canal moderno y flota (M11–M12). El emplazamiento, las conexiones y su capacidad corresponden a 4.2; los centros de datos, a 4.3. Los catálogos extensos se entregan en los anexos 4-A a 4-V. El Anexo 4-N verifica las capacidades y contratos; la Tabla de correspondencia de 4.2.2 identifica su realización física.

En Puelche, un pedido debe poder tomarse en una ruta sin cobertura, prepararse durante la noche y llegar al cliente con su lote y su evidencia de entrega identificados. La arquitectura parte de esa continuidad: cada operación se registra donde ocurre y se reconcilia cuando vuelve la conexión. Para ordenar las responsabilidades, la solución se organiza en las ocho capas exigidas por el numeral 2.1 de las Bases Técnicas Transversales (Pontificia Universidad Católica de Valparaíso [PUCV], 2026b, cap. 2, p. 6; RT-02.01).

<a id="h-04-partes-4-1-logica-02-especificaciones-tecnologias-de-software-a-utilizar-tex-3"></a>

### 4.1.1 Especificaciones Tecnologías de Software a utilizar

<a id="subsec-tecnologias-software"></a>

El núcleo de negocio se implementa como monolito modular en Laravel 13 y PHP 8.5. Frente a microservicios por dominio, esta elección conserva una sola base de código y un despliegue comprensible para el equipo TI de cuatro personas; sincronización, mensajería EDI y telemetría se ejecutan como procesos separables cuando su carga lo exija. Laravel proporciona rutas, validación, políticas, contenedor de dependencias y trabajos en cola; las reglas de negocio permanecen en módulos propios, sin depender de esas interfaces. Se seleccionan PostgreSQL/PostGIS para transacciones y geografía, RabbitMQ local para conservar trabajo durante un corte y SQS FIFO para ordenar su entrega por partición al reconectar. Ni el framework ni la cola reemplazan la deduplicación y la conciliación de los consumidores.

Angular y TypeScript sirven los portales; Kotlin nativo en Android permite escaneo, captura de evidencia y almacenamiento cifrado en el parque móvil Zebra. Keycloak emite la identidad central mediante OIDC; las decisiones de autorización siguen siendo de cada servicio. La comparación con microservicios, aplicaciones híbridas y otros productos se resume en la sección de alternativas y en los ADR. Los servicios gestionados de AWS apoyan la ejecución y la integración; su ubicación y redundancia corresponden a 4.2. Estas elecciones deben sostenerse durante el contrato mediante actualización de versiones soportadas, sin prometer que una versión inicial durará 56 meses.

Los principios que gobiernan el diseño son los siguientes:

-  **Continuidad sin conexión.** Preventa y reparto deben registrar un turno completo de 14 horas sin cobertura. El componente local debe mantener al menos 24 horas continuas de operación autónoma y degradada (RT-03.10). La sincronización posterior es idempotente: reenviar un evento no vuelve a ejecutar la operación. Los conflictos se resuelven con reglas de negocio documentadas, no dando prioridad automática al último registro recibido.

-  **Atención adaptada al canal tradicional.** La solución no exige que los 11.600 almacenes instalen una aplicación ni dispongan de conexión propia. El conductor registra la entrega y su confirmación mediante firma o QR; los avisos por WhatsApp/SMS se utilizan cuando el canal está disponible. El almacenero que tiene teléfono puede, además, instalar el Portal de Clientes y armar su pedido sin señal; es un canal opcional que convive con el preventista.

-  **Responsabilidades distribuidas.** Recepción, preparación y despacho conservan su núcleo transaccional disponible en cada sitio. Preventa, reparto y canal moderno disponen de servicios centrales, mientras las aplicaciones de terreno conservan la captura local cuando no pueden alcanzarlos. La ubicación, la capacidad y la redundancia de esos servicios se justifican en 4.2, conforme al Art. 16.

-  **Evolución durante 56 meses.** La Etapa 1 comprende los meses 1–15, con producción en el mes 16; la Etapa 2, los meses 13–20, con producción en el mes 21. Los 36 meses de operación se extienden del mes 21 al 56 (Art. 17).

-  **Verificación explícita del acceso.** La identidad central utiliza OIDC y MFA. Cada servicio verifica autorización, alcance y contexto; una solicitud no se considera confiable solo por provenir de la red corporativa. El cifrado y la auditoría acompañan cada intercambio.

-  **Recuperación y reconciliación.** RT-07.04 exige RTO ≤ 4 horas y RPO ≤ 15 minutos para los servicios críticos. La extracción continua por fibra, LTE y satélite en los CD sostiene el RPO exigido aun ante la caída de los dos medios terrestres. El Anexo 4-M define AL-DR-01; el límite residual se justifica en 4.3.2. Los ambientes, medios de respaldo y conectividad redundante corresponden a 4.2.

-  **Operación sostenible para cuatro personas.** Las herramientas, los procedimientos y el soporte deben permitir que el equipo TI de Puelche administre la solución con el apoyo del adjudicatario durante todo el contrato.

La descripción sigue el marco TOGAF y la organización de vistas de ISO/IEC/IEEE 42010:2022 (International Organization for Standardization [ISO], 2022a). La vista lógica define las responsabilidades de los componentes y sus relaciones con los procesos, los datos, la seguridad y las integraciones. Cada decisión arquitectónica debe conservar su justificación, las alternativas consideradas y los requisitos que la sustentan (PUCV, 2026b, cap. 2, p. 6; RT-02.04).

Las decisiones tecnológicas se registran con alternativas y criterios en el Anexo 4-O; el soporte y la actualización durante el contrato se especifican en el Anexo 4-P.

<a id="h-04-partes-4-1-logica-03-principios-de-integracion-tex-4"></a>

### 4.1.2 Principios de integración

<a id="subsec-principios-integracion"></a>

La integración no es un apéndice: es el tejido que sostiene la operación distribuida de Puelche. El riesgo principal del caso está en las costuras entre sistemas legados sin documentación de interfaces, no en los módulos nuevos. De las Bases Técnicas Transversales (RT-02.06–02.08 y RT-05.16) y del caso 02 se desprenden ocho reglas de diseño:

1.  **Contrato antes que conexión.** Cada interfaz tiene dueño, contrato OpenAPI o AsyncAPI, versión y comportamiento ante falla antes de entrar en operación.

2.  **Asincronía con excepciones justificadas.** Los eventos desacoplan procesos; disponibilidad, crédito, autorización de pago y actos tributarios que exigen respuesta se consultan con tiempo máximo de espera y estado explícito.

3.  **Idempotencia.** Una escritura conserva su UUID en todos los reintentos; el consumidor deduplica y resuelve conflictos por regla de negocio, no por la última marca de tiempo.

4.  **Reconciliación auditable.** Cada conflicto conserva operación, regla, resultado, autor y momento, conforme a la bitácora del Artículo 16.4.

5.  **Frontera única del legado.** La capa anticorrupción traduce hacia el ERP; ningún módulo o portal escribe directamente en él.

6.  **Confianza explícita.** Cada mensaje y llamada se autentica, autoriza y correlaciona; las excepciones de conectividad hacia el sitio son privadas, acotadas y auditadas.

7.  **Falla declarada.** Las quince entradas del catálogo indican si reintentan, se difieren, degradan o requieren procedimiento manual.

8.  **Ventana de despacho protegida.** Las cargas masivas, reprocesos y despliegues de conectores no interrumpen la operación de 05:30 a 07:00.

Estas reglas se verifican en los contratos, el catálogo de interfaces y las pruebas de falla de cada consumidor.

Estos principios se materializan en la capa de integración, los eventos canónicos, la capa anticorrupción, el catálogo de interfaces y las reglas de reconciliación descritas en este apartado.

El núcleo reúne M1–M12 en Laravel 13 sobre PHP 8.5, con dependencias fijadas por `composer.lock`. Cada módulo tiene espacio de nombres, servicios de aplicación, reglas de dominio y adaptadores propios. Esta organización evita que una pantalla o un cambio de proveedor invada otra capacidad. Para 14.200 clientes y unos 31.000 pedidos mensuales, se conserva la sencillez operativa del monolito modular, en línea con el numeral 2.3 de las Bases Técnicas Transversales. Sincronización, EDI y telemetría tienen trabajadores y capacidad de escalado independientes desde el inicio (RT-02.02); su emplazamiento se detalla en 4.2.

La volumetría operativa que condiciona el dimensionamiento es la siguiente: 14.200 clientes activos, 8.400 SKU (que pasan a aproximadamente 9.500), 31.000 pedidos mensuales con 260.000 líneas y 2,4 millones de unidades, aproximadamente 1.400 entregas diarias habituales con un pico de septiembre de 2.600 entregas (volumen casi duplicado durante tres semanas), 96 camiones en la ventana crítica de despacho (42 propios y 54 de transportistas externos), 62 preventistas, aproximadamente 200 conductores, 120 preparadores nocturnos y 310 personas de centro de distribución (PUCV, 2026a, cap. 14, pp. 24–25). El máximo horario global de septiembre alcanza 14,66 TPS a las 12:00, incluida la preventa y el portal; dentro de la ventana de despacho de 05:30 a 07:00, el máximo es 6,94 TPS. El diseño considera ambos picos según el proceso que dimensiona, nunca el promedio, y declara explícitamente los puntos únicos de falla (SPOF) con su mitigación conforme a RT-02.11.

El modelo distingue seis instalaciones: los CD de Talca y Concepción, las plataformas de cross-docking de Curicó, Chillán y Los Ángeles, y la casa matriz de Talca, contigua al CD principal (Caso 02, cap. 2.3). Las primeras cinco ejecutan el mismo perfil `wms_only`, conservan autoridad sobre los movimientos de su bodega y publican eventos idempotentes para consolidar stock y reservas en N-04/N-05; la casa matriz no aloja cómputo propio y utiliza los portales y las consolas en nube. Los identificadores de sitio serán parametrizables para incorporar una séptima instalación proyectada a tres años y evaluar la futura operación en Los Lagos hacia 2030.

<a id="h-04-partes-4-1-logica-04-capas-de-la-arquitectura-tex-5"></a>

### 4.1.3 Capas de la arquitectura

Las ocho capas separan la interacción con las personas, las reglas de negocio y la persistencia. Seguridad y observabilidad atraviesan el conjunto. La vista general permite ubicar cada responsabilidad antes de revisar sus componentes; el inventario trazable se reúne en el Anexo 4-N.

Presentación reúne las superficies de trabajo; borde protege su entrada; puerta de enlace valida solicitudes; negocio decide por módulo; integración intercambia contratos; acceso a datos persiste por propietario. Seguridad y observabilidad atraviesan esas seis responsabilidades.

Las capas 7 y 8 atraviesan las demás; no duplican reglas de negocio.

La arquitectura se presenta primero mediante su vista general completa (Figura [1](../LAFROX-Subdocumento4.md#fig-arql-general-completa)) y después mediante una síntesis de sus ocho capas (Figura [2](../LAFROX-Subdocumento4.md#fig-arql-1)). Ambas vistas se complementan para relacionar las funciones de negocio con los componentes que las sostienen.

![Figura original](https://raw.githubusercontent.com/PatricioH315/LafroX/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/logica/cambios%20laravel/ARQL-01_Vision_general.png)

**Figura 1 — Vista general completa de la arquitectura lógica**

<a id="fig-arql-general-completa"></a>

 Fuente: elaboración propia.

La vista general muestra cómo cada actor accede a la solución desde su aplicación, portal o consola y se relaciona con los módulos M1–M12. Se lee desde las personas hacia las reglas de negocio, las integraciones y los datos, distinguiendo los componentes de nube y los del sitio. Las conexiones representan intercambios sujetos a autorización, no acceso directo a las bases de datos. Seguridad y observabilidad acompañan todo el recorrido; sus controles y las condiciones de operación sin conexión se desarrollan en los apartados siguientes.

[Figura original en PDF](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/logica/ARQL-19_Vista_general_legible.pdf)

**Figura 2 — Vista resumida de las ocho capas lógicas**

<a id="fig-arql-1"></a>

 Fuente: elaboración propia.

La vista resumida destaca la responsabilidad de cada capa: presentación captura y muestra información; borde protege la entrada; las puertas de servicio validan las solicitudes; el negocio aplica las reglas en Laravel; integración conserva y distribuye eventos; y acceso a datos administra la persistencia. Seguridad y observabilidad son transversales, no pasos finales del procesamiento. La puerta local permite que la bodega siga operando sin WAN, mientras las colas conservan el trabajo sin confirmar para reconciliarlo al recuperar la conexión.

<a id="h-04-partes-4-1-logica-04-capas-de-la-arquitectura-tex-6"></a>

#### 4.1.3.1 Capa de presentación (Capa 1)

La Figura [3](../LAFROX-Subdocumento4.md#fig-arql-capa-1) presenta las responsabilidades de esta capa.

![Figura original](https://raw.githubusercontent.com/PatricioH315/LafroX/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/logica/capas_recortes/ARQL-21_Recorte_Presentacion.png)

**Figura 3 — Presentación: aplicaciones y superficies de trabajo**

<a id="fig-arql-capa-1"></a>

   Fuente: elaboración propia.

Las aplicaciones móviles conservan las capturas sin confirmar; los portales y consolas consultan sus dominios mediante APIs autorizadas. El dispositivo y la pantalla no reemplazan la identidad ni los permisos de la persona.

La capa de presentación reúne las herramientas que utiliza cada persona para trabajar: aplicaciones móviles que pueden operar sin conexión y portales web servidos desde la nube. Preventistas, conductores y preparadores capturan hechos operativos; los clientes piden en autoatención y consultan sus datos, y transportistas y proveedores consultan únicamente sus datos autorizados; Calidad, gerencias, planificación y TI toman decisiones desde consolas especializadas. Los permisos se asignan mediante una matriz de roles y atributos: un perfil de interacción no implica por sí solo acceso a todas las funciones del módulo.

Las aplicaciones de los trabajadores (preventa, reparto y bodega) se construyen en Kotlin nativo para Android, decisión alineada con el ecosistema del parque de dispositivos Zebra (EC55, TC58e, MC9400) desplegado en los centros de distribución y con las condiciones de operación del terreno. La app de preventa mantiene una foto local de datos de lectura (stock, precios, crédito, promociones) y captura local de eventos (pedidos, identificadores únicos UUID); la app de reparto gestiona la entrega, la prueba de entrega digital (POD con firma, código QR y fotografía), la cobranza en ruta y el control de envases retornables. Ambas aplicaciones operan con datos locales cifrados y sincronizan de forma idempotente por medio del API Gateway cuando se recupera la conectividad.

Los terminales de bodega (HHT con escáner GS1) descargan las misiones de preparación al inicio del turno y registran su ejecución localmente, incluso en cámaras a -22 °C sin señal. La autonomía mínima de 24 horas comprende el servicio de bodega completo: registro de operaciones, conservación de datos, cambios de turno y control de acceso.

Los portales web, implementados en Angular con Tailwind CSS, permiten a transportistas revisar rutas y a proveedores consultar órdenes y recepciones. El Portal de Clientes permite pedir en autoservicio y consultar el estado de entrega, los documentos y el saldo (RT-16.30 del caso; PUCV, 2026a, cap. 15, p. 27). Se publica además como aplicación web progresiva, instalable desde el navegador en el teléfono del almacenero, y constituye el perfil de autoatención con operación desconectada de RT-17.01 del caso (PUCV, 2026a, cap. 15, p. 27). Sin señal, muestra el catálogo y los precios descargados con su fecha y permite armar el pedido, que queda en cola con su UUID y se envía por `/sync/v1` al recuperar cobertura. El pedido existe para la compañía solo cuando M3 lo recibe; la confirmación de stock, crédito y fecha de entrega espera esa recepción. La cuenta se activa en la visita del preventista con un código enviado por SMS al teléfono registrado, y nadie queda obligado a usarla. El catálogo público admite consulta sin autenticación; las funciones privadas requieren identidad OIDC mediante Keycloak y permisos por rol. El acceso administrativo exige MFA y una ruta autorizada, definida físicamente en 4.2.

Las consolas de rutas, calidad, BI y administración TI acceden a sus dominios mediante APIs autorizadas. Ningún navegador se conecta directamente a las bases de datos. Esta separación permite aplicar las mismas reglas de acceso y auditoría con independencia de la pantalla utilizada.

<a id="h-04-partes-4-1-logica-04-capas-de-la-arquitectura-tex-7"></a>

#### 4.1.3.2 Capa de borde y exposición (Capa 2)

La Figura [4](../LAFROX-Subdocumento4.md#fig-arql-capa-2) presenta las responsabilidades de esta capa.

![Figura original](https://raw.githubusercontent.com/PatricioH315/LafroX/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/logica/capas_recortes/ARQL-22_Recorte_Borde.png)

**Figura 4 — Borde: entradas públicas, privadas y locales**

<a id="fig-arql-capa-2"></a>

   Fuente: elaboración propia.

La entrada pública protege las APIs y rechaza el acceso directo a su origen. El acceso local sostiene la bodega sin WAN; Greengrass procesa los sensores de cámara, mientras AS2 conserva una superficie B2B distinta.

La capa de borde delimita la entrada pública y la entrada de dispositivos de terreno y bodega, donde la conectividad es intermitente. Define las siguientes responsabilidades; su despliegue se especifica en 4.2:

-  **CDN (Amazon CloudFront).** Entrada pública de portales externos y APIs de negocio: distribuye contenido estático y encamina las rutas `/v1` y `/sync/v1` al API Gateway. El acceso directo al origen de esas APIs debe rechazarse y probarse. Las consolas internas usan acceso privado verificado; el transporte AS2 tiene una superficie separada, restringida a contrapartes registradas.

-  **WAF gestionado (AWS WAF y AWS Shield Advanced).** Filtrado de tráfico con reglas OWASP Top 10 y reglas personalizadas por API; protección contra denegación de servicio en capas 3, 4 y 7.

-  **Balanceador de carga (ALB).** Distribuye hacia los servicios privados el tráfico que API Gateway entrega mediante su integración privada. El flujo de acceso público es cliente → CloudFront/WAF → API Gateway → integración privada/ALB → servicio.

-  **Acceso local y continuidad.** Los servicios del sitio aplican control de acceso propio y preservan la operación crítica aun cuando todos los enlaces externos estén indisponibles. En Talca y Concepción, Starlink fijo es el tercer camino en espera caliente tras fibra y LTE; en los cross-docking es el principal, con LTE de dos proveedores como respaldo y conmutación automática en menos de 30 segundos (ADR-02).

-  **AWS IoT Greengrass.** Corre en tres gateways IoT industriales (Moxa UC-8200 o equivalente): dos en el CD Talca, que leen ambas cámaras por Modbus TCP para evitar un punto único de falla, y uno en el CD Concepción. Leen los sensores de cámara por Modbus, bloquean el despacho ante una excursión térmica en menos de 5 segundos y conservan 24 horas de datos sin enlace. No se instala en camiones: la posición de la flota llega por la API del tercero (INT-15). Los termógrafos registran toda la ruta en su memoria interna, avisan por BLE al terminal del conductor aun sin señal y este reenvía el aviso a la nube al recuperar cobertura; al volver el camión, el terminal descarga y envía el registro completo.

En los CD, Starlink permanece encendido con el túnel IPsec establecido y BGP de menor preferencia, por lo que toma tráfico solo cuando fallan fibra y LTE. En esa condición, la calidad de servicio prioriza DMS/WAL de Talca, la salida del broker y outbox, las guías hacia el ERP y el SII, la identidad y la telemetría crítica. Mantener el terminal encendido evita esperar la adquisición de satélites y la negociación del túnel durante la falla; la tarifa plana no añade costo por esa permanencia.

<a id="h-04-partes-4-1-logica-04-capas-de-la-arquitectura-tex-8"></a>

#### 4.1.3.3 Capa de puerta de enlace de servicios (Capa 3)

La Figura [5](../LAFROX-Subdocumento4.md#fig-arql-capa-3) presenta las responsabilidades de esta capa.

![Figura original](https://raw.githubusercontent.com/PatricioH315/LafroX/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/logica/capas_recortes/ARQL-23_Recorte_Puertas.png)

**Figura 5 — Puertas de servicio: recorrido central y local**

<a id="fig-arql-capa-3"></a>

   Fuente: elaboración propia.

El recorrido central valida la identidad y entrega solicitudes a servicios privados. La puerta local atiende al HHT dentro del sitio, sin invocar el Gateway remoto durante un corte; ambos recorridos conservan validación, idempotencia y auditoría.

Amazon API Gateway concentra la publicación de servicios detrás de la entrada pública de CloudFront. El diseño requiere validar la identidad emitida por Keycloak, controlar esquema, cuotas y tasa de solicitudes, y propagar un `transaction_id`. Se selecciona REST API con authorizer REQUEST que verifica firma, emisor, audiencia, expiración y alcance del JWT de Keycloak. Las operaciones sensibles no reutilizan autorizaciones almacenadas; el módulo verifica además recurso y revocación conocida. La integración privada usa VPC Link V2 hacia ALB; la validación básica de Gateway se complementa con el esquema completo en Laravel (AWS, s. f.-a, s. f.-b, s. f.-c; Anexo 4-O, ADR-13). El recorrido físico y el bloqueo efectivo del acceso directo al origen se deben comprobar en 4.2.

La capa publica dos conjuntos de APIs: las de negocio (`/v1`) y las de sincronización offline (`/sync/v1`). El Gateway aplica los controles de entrada y enruta las solicitudes. El servicio de negocio valida el contenido y garantiza la idempotencia de cada escritura mediante su UUID, una ventana de deduplicación documentada y el registro persistente del resultado (RT-02.06).

El ingreso por API Gateway corresponde a los servicios en nube. Durante una interrupción del enlace, la bodega utiliza los servicios de su sitio sin depender del Gateway remoto. Los terminales sin cobertura conservan sus eventos y los entregan al servicio local cuando recuperan comunicación; la reconciliación con la nube ocurre al restablecerse el enlace externo. Los contratos y las reglas de validación se mantienen en ambos recorridos.

La bodega dispone además de una puerta de API *local* como función del motor WMS A-01, en VM-01, VM-C01 y E-01, acotada a la red del sitio y a M1, M2, M5, la recepción física de retornos de M8 y la función local de bloqueo de M9. Los terminales de bodega no llaman a Amazon API Gateway durante un corte: el verificador local valida la autorización de turno y esta función aplica esquema, límites de tasa, tamaño de carga, UUID y registro de auditoría antes de entregar una orden al módulo correspondiente. Este control no publica una segunda entrada en internet ni emite identidades nuevas. La Figura [6](../LAFROX-Subdocumento4.md#fig-arql-17) separa los dos recorridos y muestra cómo se conserva el trabajo hasta la reconexión.

![Figura original](https://raw.githubusercontent.com/PatricioH315/LafroX/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/logica/ARQL-17_Acceso_local_24h.png)

**Figura 6 — Identidad y puerta de API local durante un corte de 24 horas**

<a id="fig-arql-17"></a>

 Fuente: elaboración propia.

El manifiesto de turno firmado por Keycloak llega antes del corte; en cada relevo el verificador local, alojado junto a la caché, valida el manifiesto y un segundo factor local: el PIN personal sobre el terminal enrolado por MDM. El permiso queda limitado a funciones de bodega, mientras los eventos y la bitácora se envían después con su identificador original. La prueba debe iniciar el corte antes de dos relevos sucesivos y medir vencimiento, denegación, reintentos y recuperación; la caché de identidad de 24 horas no emite sesiones y el relevo lo habilita el verificador local.

<a id="h-04-partes-4-1-logica-04-capas-de-la-arquitectura-tex-9"></a>

#### 4.1.3.4 Capa de lógica de negocio (Capa 4)

La Figura [7](../LAFROX-Subdocumento4.md#fig-arql-capa-4) presenta las responsabilidades de esta capa.

![Figura original](https://raw.githubusercontent.com/PatricioH315/LafroX/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/logica/capas_recortes/ARQL-24_Recorte_Negocio.png)

**Figura 7 — Negocio: monolito modular Laravel y sus doce módulos**

<a id="fig-arql-capa-4"></a>

   Fuente: elaboración propia.

La figura reúne los doce módulos de negocio y sus funciones principales, junto con las tecnologías del backend y los sistemas externos con los que se relacionan. Los límites e intercambios de cada contexto se desarrollan en los apartados siguientes.

La capa de servicios de negocio reúne M1–M12 en un monolito modular Laravel. Cada contexto separa `Domain`, `Application`, `Infrastructure` y `Http` bajo un espacio de nombres PSR-4. Los controladores reciben y validan solicitudes; los servicios de aplicación coordinan casos de uso; el dominio decide reservas, bloqueos y rendiciones; los adaptadores traducen persistencia e integraciones. Los módulos se llaman mediante interfaces públicas o eventos versionados: no acceden a las tablas privadas de otro contexto ni importan sus modelos de persistencia. Los proveedores de servicios registran esas interfaces en el contenedor y una prueba de dependencias impide invertir las fronteras. Así, compartir proceso no confunde la propiedad de cada decisión (RT-02.02).

La misma versión del artefacto Laravel ejecuta perfiles separados: API central, WMS local limitado a M1/M2/M5, recepción física de retornos de M8 y bloqueo M9, consumidores de SQS, adaptador AMQP y reglas comerciales EDI de M11. El transporte OpenAS2 es un componente independiente: verifica certificados, firma, cifrado y acuses MDN antes de entregar el mensaje a M11; no ejecuta reglas comerciales ni escribe en el ERP. Cada perfil dispone de cola, concurrencia, permisos y métricas propios. El planificador de tareas tiene una sola autoridad por ambiente. Esta separación permite escalar y reiniciar sincronización, EDI y telemetría sin multiplicar el monolito completo (RT-02.02).

Los módulos evitan estado durable en memoria y pueden crecer por réplicas o por trabajadores independientes, según la demanda. Los umbrales, límites de capacidad, emplazamiento y costos se especifican en 4.2 y en la oferta económica.

<a id="h-04-partes-4-1-logica-04-capas-de-la-arquitectura-tex-10"></a>

#### 4.1.3.5 Capa de integración y eventos (Capa 5)

La Figura [8](../LAFROX-Subdocumento4.md#fig-arql-capa-5) presenta las responsabilidades de esta capa.

![Figura original](https://raw.githubusercontent.com/PatricioH315/LafroX/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/logica/capas_recortes/ARQL-25_Recorte_Integracion.png)

**Figura 8 — Integración: continuidad local y contratos con terceros**

<a id="fig-arql-capa-5"></a>

   Fuente: elaboración propia.

El sitio conserva los eventos hasta confirmar su publicación y el consumidor confirma después de persistir. La ACL concentra el acceso al ERP, único emisor tributario; el hub EDI traduce contratos comerciales y las excepciones permanecen trazables.

La capa de integración conecta la nueva operación con sistemas que Puelche ya utiliza. Sus límites son especialmente importantes ante el ERP de 2017 sin interfaces documentadas y el WMS de 2013. También concentra el intercambio con cadenas del canal moderno, los servicios de pago, los mapas y la telemetría, de modo que un cambio externo no obligue a modificar cada módulo de negocio.

RabbitMQ conserva las colas de integración local. En nube, SQS FIFO ordena los mensajes de reconciliación dentro de cada grupo y SNS difunde eventos y alertas. Los avisos al cliente se entregan mediante SNS o la API del proveedor de notificaciones (INT-11). El orden no se presume global ni se atribuye a toda la cadena de eventos. Los consumidores aplican deduplicación, reintentos con espera creciente y una cola de mensajes fallidos (DLQ), con intervención trazable cuando el procesamiento no puede completarse (RT-02.07).

El shipper publica en la cola SQS FIFO de reconciliación un sobre JSON independiente de PHP con versión, identidad, clave de orden y carga. Un consumidor PHP dedicado lee ese sobre mediante el SDK de AWS, valida su esquema, invoca el caso de uso Laravel y reconoce el mensaje solo después de persistir el resultado. Las solicitudes al ERP viajan por otra cola, la cola FIFO de solicitudes al ERP, que solo lee `erp-sync` en VM-04 de Talca; cada respuesta vuelve a su sitio por una cola FIFO de respuesta propia, que el shipper del sitio lee por conexión saliente y entrega a RabbitMQ local. Los trabajos derivados propios de Laravel usan su conector SQS en colas distintas y declaran grupo y clave de deduplicación cuando requieren orden FIFO. Esta separación evita entregar mensajes externos al deserializador de trabajos del framework. RabbitMQ local se conecta mediante un adaptador AMQP probado con `php-amqplib`; el shipper confirma la publicación en SQS antes de reconocer el mensaje local. No se introduce Redis ni Horizon en los sitios, donde la continuidad depende de PostgreSQL y RabbitMQ.

Las APIs de la plataforma reciben solicitudes por la Capa 3. Los servicios de negocio invocan sus adaptadores de integración cuando necesitan consultar pagos o mapas, con tiempo máximo de espera explícito (RT-02.08). Los intercambios diferidos con ERP, EDI, telemetría y notificaciones utilizan colas y reintentos. La emisión tributaria se canaliza por el ERP mediante la ACL; no se crea un segundo emisor de documentos ante el SII.

El ERP de 2017 se conserva como única fuente de verdad tributaria y único emisor de DTE. La capa anticorrupción (ACL) traduce los contratos de la solución al formato del legado, sin reemplazarlo ni modificar su código. El flujo de rendición es: rendición aprobada → cola FIFO de solicitudes al ERP → `erp-sync` en VM-04 de Talca → ACL local → ERP. Dos procesos de `erp-sync` consumen además RabbitMQ local para las solicitudes del WMS de Talca; acceden a la cola de solicitudes mediante conexión saliente. Ningún módulo, portal o cadena escribe directamente en el ERP. El trabajador usa una clave idempotente por operación y conserva folio, estado y acuse para seguir cada documento hasta su origen; reintentar un trabajo no solicita un segundo documento. M5 solicita la guía al cerrar la carga nocturna; cualquier cambio de carga invalida la guía y exige una nueva. El ERP sigue como único emisor ante el SII por fibra, LTE o satélite.

La integración con las cadenas del canal moderno se resuelve con un hub EDI centralizado en nube. Utiliza mensajes comerciales EANCOM y GS1 XML, y eventos EPCIS para trazabilidad. Cada cadena dispone de un conector configurable, una tabla de equivalencias GTIN (RF-12.03) y una bandeja de excepciones (RF-12.06). El hub transforma los mensajes al modelo canónico y entrega al ERP, exclusivamente mediante la ACL, la información necesaria para sus documentos, incluida la guía de despacho electrónica (GDE). AS2 es uno de los transportes del hub. El canal moderno debe quedar operativo a más tardar en enero de 2029.

**Eventos canónicos del dominio.**

<a id="subsubsec-eventos-canonicos"></a>

Los eventos son el vocabulario del sistema. Se nombran en pasado, son inmutables y llevan `event_id` (UUID), `occurred_at`, `site_id` y `transaction_id`. El catálogo de eventos canónicos del dominio se presenta en el Anexo 4-A. Cada evento declara productor único, consumidores registrados, clave de partición y política de reintento, y su origen se traza a un requisito del caso o a una decisión del numeral 16.1.

Los esquemas AsyncAPI 2.6 versionados por evento se gobiernan desde el Catálogo de interfaces (§ [4.1.6](../LAFROX-Subdocumento4.md#sec-catalogo-interfaces)); `transaction_id` conserva la correlación entre los módulos consumidores.

**Orquestación y coreografía.**

M3 coordina de manera síncrona la confirmación de un pedido y solicita a M2 una reserva: necesita una respuesta única y visible para el preventista. Cuando el pedido queda confirmado, publica `PedidoConfirmado`; M4, M5 y M10 reaccionan a ese hecho; M11 también lo consume solo para pedidos de cadenas, a fin de responder a la cadena mediante su propio consumidor. Esa coreografía evita que M3 conozca el horario de preparación o el esquema analítico. La publicación se registra junto con el cambio de estado mediante una bandeja transaccional de salida (*outbox*); el consumidor confirma su progreso solo después de persistir su resultado. Si falla un consumidor, la cola reintenta y termina en una bandeja de excepción, sin deshacer a ciegas el pedido ya confirmado.

El despacho tiene una coordinación distinta: M5 no libera la carga hasta recibir el resultado de M9 sobre el lote y la guía emitida por el ERP a través de la ACL. Una excursión térmica bloquea localmente la salida aun con el enlace caído; solo Calidad puede liberar el lote tras evaluación registrada. El conductor informa la incidencia y conserva la carga, pero no aprueba su liberación sanitaria. Las Figuras [9](../LAFROX-Subdocumento4.md#fig-arql-15) y [10](../LAFROX-Subdocumento4.md#fig-arql-16) recorren el pedido con y sin conexión y hacen visible dónde cambia una captura sin confirmar a una operación confirmada.

![Figura original](https://raw.githubusercontent.com/PatricioH315/LafroX/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/logica/ARQL-15_Pedido_con_conexion.png)

**Figura 9 — Secuencia lógica del pedido con conexión**

<a id="fig-arql-15"></a>

 Fuente: elaboración propia.

Con conexión, M2 devuelve una reserva explícita y M5 no comienza a preparar un pedido rechazado. La carga preparada sigue retenida si M9 informa un bloqueo o si el ERP no devuelve la guía electrónica. El flujo dibuja esos dos retornos porque un pedido confirmado no autoriza por sí mismo la salida física.

![Figura original](https://raw.githubusercontent.com/PatricioH315/LafroX/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/logica/ARQL-16_Pedido_sin_conexion.png)

**Figura 10 — Secuencia lógica del pedido capturado sin conexión**

<a id="fig-arql-16"></a>

 Fuente: elaboración propia.

Sin conexión, la aplicación conserva la intención de compra, no una reserva firme. El mismo UUID viaja en todos los reintentos; M3 y M2 producen un resultado durable con la regla y la causal de excepción. Si se pierde el acuse de respuesta, el dispositivo conserva el evento y pregunta por ese UUID antes de eliminarlo. Solo un pedido confirmado alimenta M5, lo que permite explicar al cliente un faltante sin duplicar la venta.

**Contratos de integración.**

<a id="subsubsec-contratos-integracion"></a>

Las APIs síncronas se describen en OpenAPI 3.1 por módulo y versión mayor. Cada operación declara dueño, esquema de solicitud y respuesta, identidad requerida, errores de negocio, límites de tasa y fecha de retirada. El Gateway valida la entrada, pero la decisión de negocio y la idempotencia pertenecen al servicio. Las interfaces de sincronización `/sync/v1` reciben lotes con UUID por operación y devuelven un resultado individual, de modo que un error de una entrega no obligue a repetir todas las demás.

Los eventos se describen en AsyncAPI 2.6 con productor único, consumidores, clave de partición, versión, política de reintento y cola de fallidos. Los mensajes viajan al menos una vez: cada consumidor deduplica por `event_id` y preserva orden dentro del agregado que lo exige. OAuth con PKCE protege clientes interactivos; mTLS y credenciales rotadas protegen servicios. `transaction_id` enlaza llamada, evento, resultado y evidencia de auditoría.

**Capa anticorrupción y sustitución del WMS.**

<a id="subsubsec-acl-estrangulamiento"></a>

**Frontera única del ERP (A-04).** El ERP de 2017 no tiene documentación de interfaces. En vez de descubrir su forma real dentro de cada módulo, se levanta una sola frontera: la ACL expone hacia adentro un contrato OpenAPI 3.1 propio de Puelche y absorbe hacia afuera la forma del ERP. Consecuencias:

-  El conocimiento del ERP queda concentrado y documentado en un solo componente, no disperso en doce módulos.

-  Ningún módulo, portal ni cadena de supermercados escribe al ERP: el trabajador `erp-sync` en VM-04 consume RabbitMQ local y, por salida, la cola FIFO de solicitudes al ERP, y llama a la ACL del mismo sitio mediante su contrato versionado.

-  Cuando una capacidad del ERP se absorbe en la plataforma, se retira de la ACL sin tocar a los consumidores.

**Estrangulamiento del WMS de 2013 (ADR-08, Decisión 16.1 N° 14).** El WMS se reemplaza en la Etapa 1 por los módulos M1, M2 y M5 del monolito. Durante la coexistencia el legado queda detrás de la misma ACL. La Tabla [1](../LAFROX-Subdocumento4.md#tab-capacidad-wms) indica qué capacidad se absorbe en cada ola y cómo se revierte por sitio.

<a id="tab-capacidad-wms"></a>

**Tabla 1 — Capacidad absorbida del WMS 2013 por ola**

| **Capacidad WMS 2013** | **Módulo** | **Ola** | **Estrategia / Reversión** |
| --- | --- | --- | --- |
| Recepción GS1 | M1 | 1 | Azul-verde / feature flag (reversión inmediata) |
| Slotting / ubicaciones | M2 | 1–2 | Azul-verde / feature flag |
| Misiones picking HHT | M5 | 2 | Azul-verde / feature flag |
| Conteo cíclico | M2 | 2–3 | Paralelo + comparación / feature flag |

 Fuente: Anexo 4-O, ADR-08, y Caso 02, decisión 16.1 N° 14.

La sustitución por olas permite comprobar cada capacidad antes de retirar la precedente.

No se mantiene el WMS 2013 como sistema operativo en producción tras la Etapa 1. La ACL garantiza que ningún módulo, portal ni cadena escribe al ERP/WMS legado directamente.

**Hub EDI GS1 (ADR-11).** Una cadena nueva se incorpora por configuración de perfil (equivalencias GTIN por cadena, RF-12.03), no por desarrollo. El hub mapea cada cadena contra un modelo canónico GS1, no contra el ERP; así evita construir una integración diferente en los doce módulos de negocio.

**Versionado y gobierno de integración.**

<a id="subsubsec-versionado-gobierno"></a>

Los contratos siguen versiones `major. minor. patch`. Un cambio aditivo conserva compatibilidad; retirar un campo exige marcarlo como obsoleto y anunciar la fecha de salida con al menos seis meses de anticipación. Dos versiones pueden convivir mientras migran los consumidores identificados. Un cambio incompatible requiere aprobación del Comité de Arquitectura, pruebas de contrato y plan de reversión. Los perfiles de cadenas se versionan sin alterar el vocabulario común del hub; los cambios de interfaces tributarias se gestionan en la ACL, no como perfiles EDI. El Anexo 4-B asigna dueño y evidencia a cada mecanismo de gobierno.

El catálogo y las pruebas hacen visible quién responde cuando un contrato cambia o falla.

**Carga y descarga masiva de datos.**

<a id="subsubsec-carga-masiva"></a>

Las importaciones históricas y las extracciones regulatorias utilizan contratos distintos de la operación diaria. El Anexo 4-C compara su mecanismo, la prueba de integridad y el tratamiento de rechazos; ninguna carga masiva desplaza la preparación durante la ventana crítica de despacho.

El procesamiento por lotes conserva totales y rechazos sin bloquear la operación diaria.

**Regla transversal:** ninguna carga masiva se ejecuta dentro de la ventana crítica 05:30–07:00, y toda carga queda registrada y es auditable.

<a id="h-04-partes-4-1-logica-04-capas-de-la-arquitectura-tex-11"></a>

#### 4.1.3.6 Capa de acceso a datos (Capa 6)

La Figura [11](../LAFROX-Subdocumento4.md#fig-arql-capa-6) presenta las responsabilidades de esta capa.

![Figura original](https://raw.githubusercontent.com/PatricioH315/LafroX/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/logica/capas_recortes/ARQL-26_Recorte_Datos.png)

**Figura 11 — Datos: propiedad y persistencia híbrida**

<a id="fig-arql-capa-6"></a>

   Fuente: elaboración propia.

El sitio conserva la autoridad de bodega y el dispositivo mantiene sus capturas hasta recibir confirmación durable. Los servicios centrales separan transacciones, caché, documentos y analítica; ninguna consulta de BI debe competir con el despacho.

La capa de datos distingue quién conserva la información operativa, quién la consolida y quién la consulta para análisis. Esta separación permite que la bodega siga trabajando sin enlace externo y que las consultas gerenciales no compitan con el despacho. Los dominios de información asumen las siguientes responsabilidades:

En la operación local:

-  **CD Talca:** PostgreSQL 16 con PostGIS y perfil `wms_only` como autoridad de los movimientos físicos de Talca, con autonomía mínima de 24 horas.

-  **CD Concepción:** PostgreSQL y el mismo perfil `wms_only`, capaz de sostener 24 horas de operación local sin depender de Talca.

-  **Cross-docking de Curicó, Chillán y Los Ángeles:** el mismo perfil `wms_only` en E-01 para recepción, desconsolidación y despacho. Cada sitio publica su detalle por SQS FIFO hacia la consolidación en nube. Las tres horas indicadas en el caso son una ventana operativa, no una excepción a RT-03.10: el diseño lógico exige al menos 24 horas de continuidad local degradada, cuya suficiencia deberá demostrarse mediante pruebas.

En los servicios centrales, N-04/N-05 consolidan stock por sitio y la reserva de preventa mediante eventos idempotentes; PostgreSQL conserva las transacciones de preventa, reparto y canal moderno; el flujo de telemetría ingresa en DynamoDB y se consolida para análisis en S3 y Redshift mediante Glue; Redis acelera lecturas autorizadas de stock, precios y sesiones; S3 conserva documentos y evidencias. La función de cada almacén, y no su ubicación física, determina qué módulo puede escribir en él. La topología de replicación y recuperación se especifica en 4.2.

No se incorpora Redis local. Al iniciar el turno con conexión, la aplicación solicita a las APIs una copia de stock, precios y demás datos autorizados; los servicios la obtienen de sus almacenes, incluido ElastiCache. El dispositivo conserva esa copia cifrada en SQLite/Room y consulta allí mientras está desconectado. Al reconectar, reconcilia primero las escrituras sin confirmar y actualiza los datos de lectura. Reemplazar la copia de lectura nunca debe borrar pedidos, cobros ni evidencias aún no confirmados por el servidor.

La vigencia de los datos de lectura es independiente de la identidad. Las credenciales de turno duran 8 horas en bodega y 14 horas en terreno; la caché local de identidad es de solo lectura y tiene TTL de 24 horas en VM-05 (Talca), VM-C03 (Concepción) y E-01 de cada cross-docking. Una copia reciente de precios no renueva la sesión y una sesión válida no convierte el stock descargado en una reserva confirmada. El relevo de turno sin IdP lo habilita el verificador local del mismo nodo, conforme a la capa de seguridad de este apartado.

La separación transaccional/analítica es estricta: la analítica no lee del transaccional para evitar degradar la ventana crítica de despacho. Las latencias comprometidas son: operación del día ≤ 5 minutos, cierre comercial ≤ 2 horas, gestión ≤ 4 horas.

Cada evento conserva identidad, estado y resultado hasta recibir confirmación durable. DMS replica el WMS de Talca hacia un esquema de lectura; no escribe en las tablas de negocio centrales. Los consumidores de eventos actualizan estas últimas con deduplicación transaccional por sitio y UUID. Concepción y los cross-docking sincronizan sus eventos sin presumir un flujo DMS propio. Durante un corte cada sitio retiene sus cambios dentro de una capacidad comprobada para 24 horas. La extracción continua de DMS/WAL de Talca y de outbox por fibra, LTE y satélite sostiene RPO ≤ 15 minutos; AL-DR-01 del Anexo 4-M verifica la protección externa y 4.3.2 justifica el límite residual. El esquema 3-2-1-1-0, los medios de respaldo y la restauración se desarrollan en 4.2.

<a id="h-04-partes-4-1-logica-04-capas-de-la-arquitectura-tex-12"></a>

#### 4.1.3.7 Capa de seguridad transversal (Capa 7)

La Figura [12](../LAFROX-Subdocumento4.md#fig-arql-capa-7) presenta las responsabilidades de esta capa.

![Figura original](https://raw.githubusercontent.com/PatricioH315/LafroX/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/logica/capas_recortes/ARQL-27_Recorte_Seguridad.png)

**Figura 12 — Seguridad: identidad y autorización transversal**

<a id="fig-arql-capa-7"></a>

   Fuente: elaboración propia.

Keycloak emite la identidad y cada módulo decide la autorización sobre su recurso. Sin enlace, el verificador usa permisos de turno previamente firmados; el cifrado y la auditoría protegen los datos y decisiones a lo largo de todas las capas.

La seguridad atraviesa las ocho capas. Su unidad de decisión no es la red desde la que llega una solicitud, sino el sujeto, el recurso, la acción y el contexto del turno. Keycloak conserva la autoridad de identidad; el servicio dueño del recurso conserva la decisión de autorización. Esta separación evita que un token válido permita, por sí solo, liberar una carga, consultar crédito o modificar una regla de calidad (PUCV, 2026b, caps. 11–12, pp. 23–26; RT-11.01 y RT-12.05; National Institute of Standards and Technology [NIST], 2020).

**Límites de confianza y capa expuesta.**

La Figura [1](../LAFROX-Subdocumento4.md#fig-arql-general-completa) distingue personas, dispositivos, sitio, servicios centrales y terceros. CloudFront protege los portales externos y sus APIs; el origen de esas APIs rechaza el acceso público directo. Las consolas internas usan acceso verificado por identidad y postura del dispositivo hacia servicios privados. OpenAS2 expone un canal B2B distinto, limitado a contrapartes registradas y con validación criptográfica y MDN; no es una API pública de negocio. Los almacenes de datos no son superficies públicas. El inventario de dominios, puertos y rutas de 4.2 debe representar las tres superficies por separado (RT-11.07 y RT-11.13).

API Gateway verifica la identidad, el alcance, las cuotas, los límites de tasa, el esquema y la carga útil antes de entregar una solicitud; M1–M12 repiten la autorización de negocio sobre el recurso concreto. Los puntos públicos incorporan detección de bots y reto progresivo sin bloquear a una persona legítima. La comunicación entre servicios se autentica mutuamente y se cifra; un evento asíncrono también conserva productor, destinatario, versión, identificador y permisos necesarios. Así se aplica el mismo límite de confianza a REST y a mensajería (RT-11.11–11.12).

La política lógica prohíbe el ingreso público directo a los sitios. Las excepciones de integración a través de un túnel privado no son exposición a internet: se autorizan de forma nominativa, por origen, destino y propósito, y se registran. La única conexión iniciada desde nube hacia un sitio es DMS hacia VM-02 de Talca, nominada y auditada por IPsec; las demás conexiones de los sitios se inician hacia nube. Las reglas de red se especifican en 4.2; una excepción no amplía el permiso de los módulos para escribir directamente en el ERP.

**Identidad, autorización y sesiones.**

La identidad central utiliza OIDC, SSO y MFA. El rol se complementa con atributos de instalación, turno, ruta, dispositivo y empresa transportista. El proveedor solo consulta sus órdenes; el transportista administra sus conductores y rutas asignadas; el conductor actúa sobre su entrega y rendición; Calidad decide sobre un lote bloqueado; y Tesorería aprueba la conciliación, sin que quien registró el cobro pueda aprobar su propia diferencia. Los administradores elevan privilegios por tiempo limitado, con aprobación y registro de sesión. El alta, cambio de rol y baja quedan vinculados al ciclo de vida laboral o contractual, con baja efectiva antes de 24 horas desde la desvinculación, y los administradores usan además claves de acceso FIDO2; las personas externas disponen de registro, verificación y recuperación de acceso sin requerir correo corporativo (RT-12.01–12.06 y RT-12.09–12.12).

En las APIs Laravel, un guard OIDC comprueba firma con las claves publicadas por Keycloak, emisor, audiencia, vencimiento y alcance. Las políticas del módulo dueño verifican además recurso, turno y atributos; se prueban tanto rutas HTTP como trabajos asíncronos para que una cola no eluda la autorización. El acceso local usa exclusivamente el verificador de manifiestos descrito abajo. Laravel no emite otra identidad de usuario mediante Sanctum o Passport: Keycloak sigue siendo el único IdP y la administración de personas se realiza en el portal Angular autorizado.

En conexión, el token de acceso dura como máximo 30 minutos; la inactividad cierra la sesión administrativa a los 15 minutos y las demás a los 30. La credencial de refresco es rotatoria, se invalida ante baja o sospecha de compromiso y no supera 24 horas para acceso ordinario ni 8 horas para privilegios. El cierre de sesión se propaga a los servicios conectados y se impide la concurrencia no autorizada para cuentas compartibles por riesgo. Ninguna credencial se transporta en la URL. Estas duraciones no renuevan ni alargan una autorización offline; responden a los controles de RT-12.07–12.08.

La credencial de turno dura hasta 8 horas en bodega y hasta 14 horas en terreno. Mientras existe enlace, Keycloak renueva al menos cada hora un manifiesto firmado con los turnos y permisos preinscritos para una ventana de 26 horas; así, incluso si el corte comienza justo antes de la renovación siguiente, quedan al menos 25 horas de verificación local. La caché de identidad, de solo lectura y TTL de 24 horas, conserva datos recibidos en VM-05 (Talca), VM-C03 (Concepción) y E-01 de cada cross-docking, pero no emite sesiones. Al relevarse un turno sin enlace, el verificador del mismo nodo comprueba la firma y vigencia del manifiesto y un segundo factor local: el PIN personal sobre el terminal enrolado por MDM; limita el acceso a M1, M2, M5, a la recepción física de retornos de M8 y a las acciones autorizadas de M9, bloquea intentos repetidos y registra cada decisión. El dispositivo compartido identifica el contexto, pero no sustituye la identidad personal del operario. Los detalles de claves y alojamiento pertenecen a 4.2 (ADR-06).

La revocación es inmediata en los servicios conectados. Durante una desconexión no se promete revocación remota instantánea: el permiso local expira al terminar su turno, no se amplía sin enlace y la incidencia se marca para revisar operaciones al reconectar. Una baja conocida localmente bloquea de inmediato la credencial en ese sitio; el verificador sincroniza las revocaciones y auditorías al restablecerse el enlace. Se ensayan dos relevos dentro de 24 horas, vencimiento, pérdida de dispositivo y recuperación del enlace. La cuenta de emergencia exige doble autorización, alcance acotado, custodia fuera de banda, registro y rotación posterior; no reemplaza la autenticación ordinaria de todos los operarios (RT-03.10 y RT-12.13).

**Clasificación, cifrado y custodia.**

La Tabla [2](../LAFROX-Subdocumento4.md#tab-seguridad-clasificacion) resume cómo cambia el control según el dato. La clasificación se aplica al evento, su copia local, las APIs y las exportaciones, no solo a la base de datos central.

<a id="tab-seguridad-clasificacion"></a>

**Tabla 2 — Clasificación lógica y protección de la información**

| **Nivel** | **Ejemplo del caso** | **Regla de acceso** | **Protección adicional** |
| --- | --- | --- | --- |
| Restringido | Credenciales, claves y factores. | Solo custodios nominados. | Claves separadas y auditoría. |
| Confidencial | Crédito, conducta de pago, geolocalización y POD. | Rol, finalidad y registro de consulta. | Cifrado por campo sensible. |
| Interno | Pedidos, movimientos y telemetría operativa. | Módulo dueño y perfiles autorizados. | Cifrado y trazabilidad. |
| Público | Catálogo sin precios. | Lectura anónima controlada. | Integridad y protección antiabuso. |

 Fuente: elaboración propia de LafroX a partir de Bases Técnicas Transversales, RT-11.03/09/10, y Caso 02, capítulo 15.

La categoría confidencial exige separar quién puede usar el dato de quién administra su almacenamiento: el acceso a la base no revela por sí solo comportamiento de pago ni geolocalización. Todo dato en reposo se cifra; los campos sensibles del caso reciben además cifrado por campo. En tránsito se exige TLS 1.3 para las interfaces compatibles, se prohíben TLS 1.0 y 1.1, se automatiza la gestión de certificados y se emplea mTLS entre servicios. La custodia y rotación de claves mantienen separación de funciones. El PAN de tarjetas no se almacena; se usa la tokenización de la pasarela. El RUT requiere una técnica de seudonimización con acceso a la clave separado y una finalidad documentada, sin confundir cifrado reversible con anonimización. La geolocalización de personas conserva la retención de 12 meses del caso y un registro de consultas; la región primaria sa-east-1 y la secundaria us-east-1 implican transferencias internacionales sujetas a aprobación del CLIENTE. AWS actúa como encargado bajo contrato con cláusulas tipo; el CLIENTE administra KMS y la geolocalización de personas se excluye de la réplica secundaria, conforme se desarrolla en 4.3.2 (PUCV, 2026a, cap. 15, pp. 26–30; PUCV, 2026b, cap. 11, pp. 23–24; RT-11.08–11.10 y RT-16.09).

**Amenazas, controles y evidencia.**

El modelado STRIDE toma cada módulo y cada integración externa como unidad de revisión, identifica su límite de confianza, abuso posible, mitigación, responsable y prueba. Para M3, el abuso es reutilizar una credencial o reenviar un pedido: se comprueban enrolamiento, vigencia e idempotencia. Para M5, la elevación indebida de privilegios no debe liberar una carga bloqueada por M9: se prueba la separación de autorizaciones. Para M11 y la ACL, un mensaje EDI repetido o manipulado se rechaza o aísla sin escribir dos veces en el ERP. El Anexo 4-Q registra las amenazas por módulo y frontera; el Anexo 4-R vincula controles ISO/IEC 27001/27002 con responsable y prueba. Son especificaciones de aceptación, no resultados de ensayos ni certificación (ISO, 2022b, 2022c) (RT-11.02 y RT-11.05).

Cada decisión de acceso y cada acción crítica conserva sujeto, empresa si aplica, recurso, operación, resultado, hora, identificador de transacción y regla aplicada. Los eventos de seguridad se envían a una bitácora inalterable y al SIEM; durante un corte se conservan localmente y se remiten con el mismo identificador al reconectar. Las reglas de detección incluyen acceso privilegiado fuera de turno, intentos reiterados de uso de una credencial de conductor revocada, consulta masiva de datos comerciales, alteración de evidencia de temperatura y desvío anómalo de mensajes EDI. Los registros técnicos en CloudWatch se conservan 12 meses en línea y 24 meses adicionales en archivo; los registros de seguridad y auditoría se conservan 7 años bajo Object Lock. La retención de documentos tributarios y POD se gobierna separadamente por su dominio de datos. La plataforma y el SOC que operan estos controles se describen en 4.2 y en el capítulo de servicios (RT-11.14–11.19).

La aceptación de esta vista requiere una prueba de acceso denegado por rol y atributo, una de cifrado de campo con lectura administrativa sin texto claro, una de continuidad y relevo offline, una de revocación al reconectar y una de correlación de un evento de negocio con su alerta de seguridad. Se distinguen dos objetivos de disponibilidad: 99,95 % mensual para la infraestructura del recinto y al menos 99,9 % mensual para el servicio de negocio de extremo a extremo. Ninguno elimina la exigencia de continuidad durante el despacho de 05:30 a 07:00.

<a id="h-04-partes-4-1-logica-04-capas-de-la-arquitectura-tex-13"></a>

#### 4.1.3.8 Capa de observabilidad transversal (Capa 8)

La Figura [13](../LAFROX-Subdocumento4.md#fig-arql-capa-8) presenta las responsabilidades de esta capa.

![Figura original](https://raw.githubusercontent.com/PatricioH315/LafroX/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/logica/capas_recortes/ARQL-28_Recorte_Observabilidad.png)

**Figura 13 — Observabilidad: correlación de nube y sitios**

<a id="fig-arql-capa-8"></a>

   Fuente: elaboración propia.

La correlación permite seguir una operación entre APIs, módulos y consumidores. Durante el corte, el sitio conserva telemetría y mantiene sus alarmas; CloudWatch reúne registros, métricas y trazas para los tableros y la atención de incidentes.

La observabilidad debe ayudar al equipo a responder preguntas operativas: qué pedido quedó sin confirmar, dónde se interrumpió una integración y qué entregas pueden verse afectadas. Para ello reúne métricas, registros y trazas de nube y sitios locales en una misma plataforma (RT-03.16 y Art. 16.4).

La instrumentación utiliza OpenTelemetry para PHP/Laravel y las aplicaciones Kotlin, junto con los registros y métricas disponibles de API Gateway, RabbitMQ, SQS y Greengrass. El identificador `transaction_id` acompaña las solicitudes y los mensajes; los trabajadores extraen el contexto de traza del sobre de evento para correlacionar la operación de negocio, incluidos los procesos asíncronos.

En on-premise, los colectores ADOT, con buffer en disco de 24 horas, recolectan la telemetría local y la exportan a la plataforma única en Amazon CloudWatch: Logs conserva los registros técnicos 12 meses en línea y 24 meses en archivo; Metrics conserva las métricas 13 meses; las trazas y los tableros operacionales también se alojan en CloudWatch (ADR-14).

Los tableros se estructuran en tres niveles: operacional (para el equipo de TI y SRE), gerencial (para la gerencia y jefes) y del mandante (para Puelche, solo lectura con auditoría de consultas, conforme a RT-14.02). Las alertas se formulan por síntomas de negocio, no por causas técnicas, con ventanas de evaluación para evitar falsos positivos y escalamiento por criticidad.

Durante un corte de enlace, el sitio no depende de los tableros centralizados para despachar. Las alarmas locales continúan y los colectores retienen la telemetría para enviarla al restablecer la conexión. La capacidad del buffer de 24 horas debe comprobarse con la carga de diseño; no se presume conservación ilimitada. La retención de métricas, registros técnicos y trazas no sustituye la política de auditoría de negocio exigida por RT-16.10.

<a id="h-04-partes-4-1-logica-05-modulos-funcionales-y-limites-de-contexto-tex-14"></a>

### 4.1.4 Módulos funcionales y límites de contexto

<a id="sec-modulos-funcionales"></a>

Los doce módulos M1–M12 separan decisiones de negocio y conservan su trazabilidad a los requerimientos. El Anexo 4-D identifica responsabilidad, intercambio, actor principal y etapa. Un actor puede participar en varios módulos sin convertirse en propietario de sus datos. El detalle de los módulos críticos se desarrolla inmediatamente después.

Cada módulo tiene un dueño de negocio y una vía explícita para colaborar con los demás.

La correspondencia con los identificadores físicos se detalla en la tabla de correspondencia del apartado 4.2.2 y en el Formulario T-11: N-04 ejecuta los módulos M1–M12 en nube; A-01 ejecuta M1, M2 y M5 como WMS local, además de la recepción física de retornos de M8, sobre A-02 (base transaccional), con A-03 (RabbitMQ), A-04 (ACL del ERP) y A-05 (identidad local) como apoyos. M9 utiliza B-02 (gateways de frío) y N-08 (ingesta IoT); M10 utiliza N-10 (analítica). N-09 proporciona SQS FIFO y SNS a los flujos asíncronos; N-01 a N-03 publican los portales y N-13 gestiona los terminales de bodega y terreno. Estos códigos identifican componentes de despliegue, no módulos de negocio adicionales.

El reparto evita que M6 emita DTE o que M10 escriba pedidos. M1 y M5 entregan datos al ERP únicamente por la capa anticorrupción. M11 entra en la Etapa 2 sin cambiar el dueño de la reserva de stock, que sigue siendo M2. Los límites y dependencias se precisan en el mapa siguiente.

El Anexo 4-E hace visible el paso del requerimiento al componente y a la capa que lo realiza. Es una síntesis de los dominios, no una sustitución del catálogo requisito por requisito del Formulario T-12; allí se debe conservar también origen, etapa, prueba y criterio de aceptación de cada RF y RNF.

La trazabilidad transversal se prueba sobre esos mismos recorridos: RT-03.10 para 24 horas en sitio y 14 horas en terreno, RT-03.12 para reconciliación determinista y RT-03.13 para funciones no disponibles sin conexión y plazos de sincronización del caso en M1, M3, M5 y M6; RT-02.06 mediante UUID y resultado persistente en M2/M3/M6; RT-02.13 mediante el modelo de dominio; y RT-11/12 mediante autorización y auditoría en cada cruce. El entorno de prueba y el caso de aceptación deben reproducir la falla, no limitarse a una marca de cumplimiento.

<a id="h-04-partes-4-1-logica-05-modulos-funcionales-y-limites-de-contexto-tex-15"></a>

#### 4.1.4.1 Mapa de límites de contexto

<a id="subsec-limites-contexto"></a>

El modelo de dominios se organiza mediante límites de contexto explícitos. El Anexo 4-F indica qué módulo entrega información, qué módulo la recibe y dónde se traduce un modelo ajeno. El uso de un vocabulario publicado o de una capa anticorrupción evita que un cambio en el ERP o en una cadena comercial reescriba las reglas de stock y pedido.

El mapa expone dependencias que deben permanecer bajo contratos versionados.

El mapa asigna a cada relación un dueño de contrato y una superficie de intercambio. El catálogo de interfaces (§ [4.1.6](../LAFROX-Subdocumento4.md#sec-catalogo-interfaces)) añade la versión y la conducta ante falla; una relación del Anexo 4-F no equivale por sí sola a un contrato ejecutable.

<a id="h-04-partes-4-1-logica-05-modulos-funcionales-y-limites-de-contexto-tex-16"></a>

#### 4.1.4.2 Módulo de calidad y trazabilidad (M9)

El módulo de trazabilidad resuelve el problema central que motivó la licitación: la incapacidad de responder en tiempo real ante un retiro sanitario. En marzo de 2026, un retiro preventivo de queso fresco tomó 9 días en resolverse de forma inexacta, generando pérdidas de $31 millones, la apertura de un sumario sanitario y la suspensión como distribuidor autorizado por un proveedor clave por seis meses.

La unidad de trazabilidad sanitaria es el lote del proveedor, identificado por el producto (GTIN) y el número de lote. El vencimiento y los registros de temperatura se conservan como atributos asociados; FEFO es la regla de rotación por vencimiento, no parte del identificador. Cada movimiento vincula el lote con la unidad logística identificada mediante SSCC. Esta organización permite seguir el producto aunque cambie de caja o pallet. Como el 41% de las recepciones carece de lote registrado, la captura en recepción es obligatoria para sostener la trazabilidad (RF-01).

La trazabilidad forward/backward se implementa evento a evento conforme al estándar GS1 EPCIS, permitiendo al sistema responder en menos de 2 horas ante un retiro sanitario (Cap. 18), con identificación precisa de los lotes y puntos de entrega afectados. Los registros de temperatura se capturan de forma continua en 21 puntos de temperatura en cámaras (15 en Talca y 6 en Concepción) y 28 termógrafos: 18 en camiones propios y 10 en camiones refrigerados de transportistas. Una lectura fuera del rango configurado genera alerta y retención preventiva automática de la carga en M5, también sin enlace (RF-09.03/05/07); el sistema registra umbral, duración, sensor y lote. La jefatura de Calidad evalúa la excursión y es la única que autoriza una liberación trazada o dispone rechazo. El conductor no puede levantar el bloqueo. M9 integra los sensores de cámara mediante los tres gateways con Greengrass (Capa 2), los termógrafos mediante el terminal del conductor, inventario (M2), preparación (M5) y observabilidad (Capa 8), con evidencia exportable de la decisión.

<a id="h-04-partes-4-1-logica-05-modulos-funcionales-y-limites-de-contexto-tex-17"></a>

#### 4.1.4.3 Módulo de inventario (M2)

El módulo de inventario permite saber qué stock existe, dónde está y qué parte puede comprometerse. Mantiene la operación distribuida entre Talca, Concepción y los tres cross-docks; la casa matriz consulta la información consolidada. Sus capacidades son las siguientes:

-  **Stock por sitio (RF-02.02, RT-02.12).** Cada instalación operativa informa sus movimientos al consolidado. Con conexión se consulta disponibilidad actual; sin ella se muestra la copia descargada, identificada como información con fecha de actualización. La parametrización admite nuevos sitios sin convertir a la casa matriz en una bodega ni asignarle stock operativo por defecto.

-  **Slotting y conteo ciego.** Asignación de ubicaciones por criterio documentado de rotación, peso y compatibilidad, con conteo cíclico de inventario mediado por terminales HHT con escáner GS1, reduciendo la discrepancia actual del 2,3% del valor contado a menos del 1%.

-  **FEFO (First Expired, First Out).** La preparación y el despacho respetan el principio de primer vencimiento, con secuenciación térmica para productos refrigerados y congelados.

-  **Stock disponible.** Con conexión se consulta la disponibilidad mediante APIs. Sin conexión se utiliza la copia autorizada descargada al inicio del turno y almacenada en SQLite/Room. La reserva se confirma en el servicio de negocio; los pedidos capturados sin señal permanecen a la espera de validación. Los conflictos se resuelven con reglas documentadas de asignación y prioridad, no mediante la sola comparación de marcas de tiempo.

<a id="h-04-partes-4-1-logica-05-modulos-funcionales-y-limites-de-contexto-tex-18"></a>

#### 4.1.4.4 Módulo de preventa móvil (M3)

Para los 62 preventistas, tomar un pedido debe seguir siendo posible aun cuando la ruta no tenga cobertura. El módulo reemplaza una aplicación que no consulta stock ni crédito y presenta caídas y duplicación de pedidos. La nueva interacción distingue con claridad lo registrado en el dispositivo de lo confirmado por el servidor:

-  **Toma de pedido offline (RF-03.02).** El preventista toma el pedido sin señal de red. La aplicación mantiene una foto local de datos de lectura (stock, crédito del cliente, precios vigentes, promociones) que se descarga al inicio del turno cuando hay conectividad.

-  **Identificador único y deduplicación (RF-03.16/17).** Cada evento recibe un UUID que se conserva en todos sus reintentos. El servicio de negocio registra su procesamiento y evita ejecutar dos veces la misma operación.

-  **Validación de stock y crédito.** La validación definitiva ocurre en la sincronización con la regla de negocio del servidor (reserva de stock, RF-03.03; crédito del cliente, RF-03.08/09). Sin conexión, el pedido queda como a la espera de validación y se resuelve en la sincronización posterior.

-  **Sincronización diferida.** Al recuperar cobertura, el dispositivo envía las escrituras acumuladas por API Gateway. El Gateway aplica los controles de entrada; el servicio de negocio valida, deduplica, procesa y confirma cada evento. El dispositivo conserva los eventos que aún no tienen confirmación.

-  **Pedido de autoatención (RT-16.30 y RT-17.01 del caso; PUCV, 2026a, cap. 15, p. 27).** M3 recibe también el pedido que el cliente arma en el Portal de Clientes, incluido el armado sin señal en su modo instalable, con la misma deduplicación por UUID y la misma validación de stock y crédito. M3 es el único dueño del pedido en sus tres canales: preventista, autoatención y canal moderno (M11).

La prueba de aceptación de terreno considera un turno de 14 horas sin cobertura. El caso exige que un dispositivo de reparto sincronice esa jornada en un máximo de 10 minutos; para el CD, fija hasta 2 horas tras un corte de 24 horas (RT-03.13 del caso; PUCV, 2026a, cap. 15, p. 26). Estos límites se verifican con la volumetría correspondiente y reconciliación determinista (RT-03.12), sin extender automáticamente el umbral del repartidor a cualquier carga de preventa.

<a id="h-04-partes-4-1-logica-05-modulos-funcionales-y-limites-de-contexto-tex-19"></a>

#### 4.1.4.5 Módulo de planificación de rutas (M4)

El módulo de planificación de rutas automatiza un proceso que actualmente depende de una sola persona (21 años de conocimiento concentrado, con retiro programado en 2 años) que administra una planilla de 11 hojas. El módulo implementa:

-  **Secuenciación automática.** Optimización determinista de rutas con capacidad y ventanas de tiempo (VRP), con objetivo de ejecución inferior a 20 minutos (Cap. 18). El planificador puede conocer las restricciones utilizadas y revisar el resultado.

-  **Ventanas horarias y capacidad.** Considera capacidad de vehículo, ventanas de entrega del cliente y cadena de frío.

-  **Integración con GIS.** Consulta de direcciones, cálculo de ETA y geocercas por API externa, con caché de mapas por zona en dispositivos para degradación a ruta offline con secuencia cargada.

-  **Costo de entrega.** Alimenta el cálculo del costo de servir por cliente, uno de los ejes de evaluación del caso.

La propuesta automática no convierte las excepciones del planificador en reglas opacas: M4 conserva restricción, motivo de ajuste y autor de la ruta aprobada para transferir conocimiento y comprobar el criterio de aceptación.

<a id="h-04-partes-4-1-logica-05-modulos-funcionales-y-limites-de-contexto-tex-20"></a>

#### 4.1.4.6 Módulo de rendición y cobro (M7)

El módulo de rendición y cobro resuelve las diferencias de rendición que promedian $4,2 millones mensuales sin investigación de causa. Implementa:

-  **Rendición digital individual (RF-07.02).** Cada conductor rinde sus cobros del turno de forma digital, con causales de descuadre clasificadas y trazables.

-  **Cobranza en ruta (RF-07.06).** El conductor registra el cobro y conserva su evidencia para la rendición. En pagos con POS móvil, la captura local de una operación no se presenta como autorización bancaria. El tratamiento sin cobertura depende de las capacidades y condiciones acordadas con la pasarela; se concilia al reconectar sin generar cargos duplicados.

-  **Interfaz con ERP (RF-07.09).** La rendición aprobada se publica en la cola FIFO de solicitudes al ERP; dos procesos `erp-sync` en VM-04 de Talca consumen esa cola por conexión saliente y la cola RabbitMQ local, y entregan a la **capa anticorrupción (ACL)** de la misma VM; la ACL integra con el ERP. Nunca hay escritura directa al ERP. El ERP permanece como única fuente de verdad tributaria y único emisor de DTE.

-  **Costo de servir (RF-11).** El módulo alimenta el tablero de BI con el costo real por entrega, incluyendo kilometraje real (telemetría M12), tiempo de servicio y deducciones por devoluciones.

<a id="h-04-partes-4-1-logica-05-modulos-funcionales-y-limites-de-contexto-tex-21"></a>

#### 4.1.4.7 Módulo de analítica y costo de servir (M10)

El módulo de inteligencia de negocio consolida la información operativa en tableros gerenciales de autoservicio (RT-05.27) con modelo semántico en el mismo lenguaje del negocio: OTIF, fill rate, costo por entrega, ocupación de flota y segmentación por canal/cliente.

Los tableros se alimentan del almacén analítico (Redshift Serverless) con latencias comprometidas: operación del día ≤ 5 minutos, cierre comercial ≤ 2 horas, gestión ≤ 4 horas (RT-05.29). El modelo dimensional se estructura en hechos (ventas, entregas, stock, costo de servir) y dimensiones (cliente, SKU, tiempo, ruta, canal), con drill-down hasta línea de pedido y lote para trazabilidad sanitaria completa.

La información es de solo lectura para la analítica, sin acceder al transaccional en vivo, conforme al principio de separación transaccional/analítico. Los informes se programan (diarios, semanales, mensuales) y se exportan de forma asíncrona con firma y checksum (RT-05.28).

El módulo prioriza la calidad de la captura y la disponibilidad de indicadores verificables, dado que el caso informa un 41 % de recepciones sin lote registrado.

Comercial y Finanzas consultan indicadores sobre el mismo modelo semántico, pero solo Tesorería, del área de Finanzas, aprueba las diferencias de rendición; M10 no recibe permiso para modificar cobros.

<a id="h-04-partes-4-1-logica-05-modulos-funcionales-y-limites-de-contexto-tex-22"></a>

#### 4.1.4.8 Recepción, preparación, reparto y servicios asociados

**M1 Recepción** compara lo recibido con la orden de compra, identifica GTIN, lote, vencimiento y SSCC, y registra cuarentena cuando falta evidencia o hay una diferencia. Publica `RecepcionConfirmada` para que M2 ubique el stock; no lo reserva para venta. La información del ERP entra y sale exclusivamente por la capa anticorrupción.

El proveedor consulta el estado de su orden y de la recepción; no accede a las reglas internas de inventario ni confirma unilateralmente un lote.

**M5 Preparación** toma pedidos confirmados y ubicaciones de M2, aplica FEFO y genera misiones verificables con lectura GS1. Conserva localmente cada lectura y la causal de faltante. Una carga no se libera por el mero hecho de estar preparada: la guía se solicita al ERP por `erp-sync` y la ACL al cerrar la carga nocturna. Un cambio de carga invalida la guía, exige una nueva y mantiene bloqueada la salida hasta disponer del documento válido.

El preparador confirma cada lectura en el servicio local; la pérdida del enlace externo no borra la misión ni convierte una carga preparada en una salida autorizada.

**M6 Reparto y entrega** recibe de M4 la ruta y de M5 la carga liberada. El conductor registra receptor, cantidad recibida, rechazos y POD en el dispositivo aun sin señal. M6 no liquida cobros ni emite documentos tributarios; publica el resultado para M7 y M8 y mantiene visible el estado de sincronización por confirmar.

El conductor propio y el externo utilizan el mismo contrato de entrega con identidades personales distintas. La evidencia queda ligada al turno y al receptor, sin exigir que el almacén instale una aplicación.

**M8 Devoluciones y envases** separa la mercadería que regresa de los activos retornables. Cada devolución conserva cantidad, lote, causal y vínculo con la entrega; el ajuste tributario se solicita al ERP por la ACL. Los canastillos y pallets se controlan por saldo de cliente y movimientos firmados, sujetos a conciliación en la rendición.

**M11 Canal moderno** recibe pedidos mediante contratos EDI configurados por cadena, traduce códigos a un vocabulario común y envía el pedido normalizado a M3. Las diferencias de formato y equivalencias van a una bandeja de excepciones; M11 no se convierte en un segundo dueño del pedido ni del inventario.

La cadena intercambia pedidos por el hub EDI; el transportista consulta y asigna viajes desde su portal. Ninguno de esos canales reemplaza el registro personal del conductor que ejecuta M6.

**M12 Telemetría y flota** consume la fuente de posicionamiento existente de los vehículos propios, compara ruta planificada con recorrido y entrega kilómetros a M10 para costo de servir. No incorpora cámaras de cabina ni usa la posición para controlar la jornada laboral. Su falla degrada la visibilidad de ruta, no la captura de entregas de M6.

<a id="h-04-partes-4-1-logica-06-modelo-de-datos-conceptual-tex-23"></a>

### 4.1.5 Modelo de datos conceptual

El modelo de datos de la solución se fundamenta en un conjunto de entidades de negocio canónicas, sus relaciones y eventos, conforme a RT-02.13. Este modelo alimenta la matriz de trazabilidad que exige el numeral 17.1 de las Bases Técnicas del caso (PUCV, 2026a, cap. 17), entregada en el Formulario T-12, y los contratos de integración (OpenAPI 3.1 y AsyncAPI 2.6 por módulo).

Las entidades principales son:

-  **Cliente.** Con RUT, razón social, canal (tradicional, food service, cadenas), crédito, georreferencia y estado de bloqueo. Eventos: creación, actualización y cambio de bloqueo.

-  **Pedido.** Identificador UUID, preventista, cliente, líneas de detalle (SKU, cantidad, precio) y ciclo de vida (tomado → confirmado → preparado → despachado → entregado → rendido). Eventos: toma, confirmación, asignación de línea, despacho y evidencia de entrega.

-  **SKU / Producto.** Con codificación GTIN/GS1, unidad, clasificación de temperatura, rangos térmicos (RF-09.01) y vida útil.

-  **Lote.** Unidad de trazabilidad sanitaria identificada por GTIN y número de lote del proveedor, con vencimiento como atributo asociado. Cada movimiento interno la vincula con su unidad logística SSCC. Eventos: recepción, bloqueo, inicio de retiro sanitario y enlace con unidad logística.

-  **Misión de preparación.** HHT, oleada, ubicación, unidades y ciclo de vida (descargada → ejecutada → cerrada).

-  **Ruta / viaje.** Planificador, vehículo, conductor, ventanas, secuencia de entregas y geocercas.

-  **Entrega.** Pedido, viaje, prueba de entrega (POD: firma, QR, fotografía), documentos DTE y efectivo. Eventos: evidencia, reintento y aprobación de rendición.

-  **Documento tributario.** Factura, boleta, guía de despacho, folio del SII y acuse.

-  **Envase retornable.** Canastillo o pallet, cliente, saldo y pérdida estimada del 14% anual (Decisión 16.1 N° 10). Control por cuenta corriente por cliente, no por unidad identificada.

-  **Sensor / registro térmico.** Dispositivo, lote o posición, temperatura y excursión térmica.

La Figura [14](../LAFROX-Subdocumento4.md#fig-arql-18) dibuja las relaciones mínimas necesarias para responder dos preguntas del caso: de qué lote provino una unidad entregada y a qué clientes llegó un lote que debe retirarse. No pretende ser el diccionario de datos del capítulo 5.

![Figura original](https://raw.githubusercontent.com/PatricioH315/LafroX/732a9d6688569bf981594c2e21c47a167b8f8ba7/04/figuras/logica/ARQL-18_Dominio_trazabilidad.png)

**Figura 14 — Modelo conceptual del pedido, el lote y la entrega**

<a id="fig-arql-18"></a>

 Fuente: elaboración propia de LafroX.

La línea de pedido se asigna a un lote identificado por GTIN y lote del proveedor; los movimientos con SSCC conservan la cadena de custodia hasta la entrega. La entrega vincula la evidencia de recepción y el folio de la guía que el ERP emitió antes del traslado. Un pedido aún puede no tener entrega, y una entrega puede registrar más de una evidencia o un rechazo parcial: esas cardinalidades y estados se concretan en el capítulo 5 sin perder el identificador de origen.

Los eventos usan verbos en pasado y son la base de los esquemas AsyncAPI. Toda escritura offline es idempotente por UUID (RT-02.06).

El almacenamiento se distribuye en quince dominios lógicos: BD_INVENTARIO, BD_PREVENTA, BD_RUTAS (PostGIS), BD_PREPARACION, BD_REPARTO, BD_COBRANZA_FINANZAS, BD_MAESTROS_CONF, BD_GOBIERNO_ACCESO, BD_CALIDAD_TRAZABILIDAD, BD_TELEMETRIA, BD_EDI_CANALMODERNO, BD_BI_GERENCIA, BD_MAILS_NOTIF, REDIS_SESIONES_CACHE y S3_DOCS. El dominio de telemetría conserva la ingesta raw en DynamoDB y su serie consolidada en S3 Parquet y Redshift, procesada con Glue. Esta separación incluye bases transaccionales, almacenes analíticos, caché y objetos; no representa quince servidores físicos ni quince motores de base de datos independientes.

<a id="h-04-partes-4-1-logica-07-catalogo-de-interfaces-tex-24"></a>

### 4.1.6 Catálogo de interfaces

<a id="sec-catalogo-interfaces"></a>

El catálogo identifica quince integraciones por número estable, dueño y superficie contractual. Los anexos 4-G y 4-H reúnen para cada una el modo, volumen esperado, ventana requerida de la contraparte y conducta ante lentitud o error (RT-05.21). Se distingue una ventana requerida por el diseño de un SLA efectivamente acordado con un tercero. El contrato ejecutable OpenAPI o AsyncAPI debe fijar operación o evento, esquema, versión, autenticación, errores y plazo de retirada. La publicación de una ruta genérica por sí sola no equivale a entregar ese contrato.

<a id="h-04-partes-4-1-logica-07-catalogo-de-interfaces-tex-25"></a>

#### 4.1.6.1 Integraciones internas

Las ocho interfaces internas intercambian pedidos, entregas, inventario, identidad y telemetría entre dispositivos, sitios y nube. El Anexo 4-G permite reconocer qué módulo acepta cada mensaje y cómo se conserva cuando falla el enlace.

Las interfaces críticas conservan datos durante el corte y confirman cada operación al reconectar.

INT-01 y INT-02 conservan el UUID de cada operación hasta obtener acuse durable; INT-03 y INT-04 ordenan eventos por sitio o agregado. INT-12 replica únicamente el WMS de Talca a un esquema de lectura separado de las tablas escritas por los consumidores de eventos. La extracción continua por fibra, LTE y satélite sostiene un desfase menor de 15 minutos; AL-DR-01 del Anexo 4-M verifica la pérdida del sitio y 4.3.2 justifica el límite residual.

<a id="h-04-partes-4-1-logica-07-catalogo-de-interfaces-tex-26"></a>

#### 4.1.6.2 Integraciones externas

Las siete interfaces con terceros se encapsulan para que un cambio de proveedor no altere doce módulos a la vez. El Anexo 4-H separa el tercero, el dueño interno del contrato y la conducta ante falla.

La ACL aísla el ERP; ninguna falla de tercero convierte un estado sin confirmar en aprobado.

La integración tributaria INT-07 pasa por el ERP, único emisor de DTE; M5 no llama al SII. La falla de INT-09 impide afirmar que un cargo quedó aprobado. Para INT-08 se preservan el mensaje original, su equivalencia y la respuesta enviada a cada cadena.

**Volumen de mensajes por integración.** Los anexos 4-G y 4-H declaran las quince interfaces; el Anexo 4-I resume órdenes de magnitud y cálculos. No se usa la suma de eventos, consultas, muestras y reenvíos como número de transacciones únicas: una misma operación cruza varias interfaces. La prueba mide además tamaño de mensajes, objetos y WAL. La telemetría se ingiere y consolida por su flujo específico sin competir con las escrituras críticas de despacho (ADR-04).

<a id="h-04-partes-4-1-logica-08-detalle-de-tecnologias-seleccionadas-tex-27"></a>

### 4.1.7 Detalle de tecnologías seleccionadas

A continuación se resume la tecnología de cada capa y su justificación principal:

-  **Backend (12 módulos).** Laravel 13 sobre PHP 8.5, con Composer y `composer.lock`, organizado en contextos M1–M12. PostgreSQL/PostGIS conserva los datos geográficos; M4 usa repositorios espaciales con SQL parametrizado vía PDO/Query Builder y pruebas de consultas. Laravel 13 requiere PHP 8.3 o superior y admite PHP 8.5 (Laravel. (2026). *Release notes*. [https://laravel.com/framework/docs/releases](https://laravel.com/framework/docs/releases).); ambos componentes se actualizarán a versiones con soporte durante los 56 meses.

-  **Frontend web.** Angular 22 con Tailwind CSS y TypeScript 6.0 compatible con su matriz oficial. La integración con Keycloak se implementa mediante OIDC y se mantiene junto con las dependencias del cliente. Las versiones deben actualizarse durante el contrato conforme a sus ciclos de soporte.

-  **Apps de campo (preventa y reparto).** Kotlin Android nativo. Nativo del parque Zebra/Android, escáner GS1 vía Zebra DataWedge, SQLite/Room offline, acceso nativo a GPS, POS y térmica.

-  **Borde y continuidad del acceso (Capa 2).** CloudFront, AWS WAF, AWS Shield Advanced y ALB en nube, con control de acceso local. En los CD, Starlink fijo permanece encendido con IPsec establecido y BGP de menor preferencia tras fibra y LTE; en los cross-docking es el camino principal, con LTE de dos proveedores como respaldo y conmutación automática en menos de 30 segundos (ADR-02), sin sustituir la autonomía del servicio local.

-  **Puerta de enlace de servicios (Capa 3).** Amazon API Gateway para publicar las APIs y aplicar controles de entrada. La configuración debe cubrir la validación de identidad de Keycloak, las cuotas y los límites de solicitudes, conforme a la modalidad de API seleccionada y al flujo descrito en la capa de puerta de enlace de este apartado.

-  **Base de datos transaccional on-premise.** PostgreSQL + PostGIS por sitio con el mismo perfil `wms_only`; cada sitio es autoridad de sus movimientos y N-04/N-05 consolida stock y reservas en nube.

-  **Base de datos nube (OLTP y recuperación).** Amazon Aurora PostgreSQL, con despliegue Multi-AZ y una ventana propuesta de recuperación a un punto en el tiempo (PITR) de 35 días. Los tiempos de conmutación y restauración se verifican mediante pruebas frente a los objetivos RTO/RPO establecidos.

-  **Ingesta IoT / frío.** Amazon DynamoDB e IoT Core reciben las lecturas; Greengrass corre en tres gateways Moxa UC-8200 o equivalentes: dos en Talca, que leen ambas cámaras por Modbus TCP para evitar un punto único de falla, y uno en Concepción; leen sensores por Modbus, bloquean el despacho en menos de 5 segundos y conservan 24 horas sin enlace. Los termógrafos de los camiones registran toda la ruta en memoria interna y alertan por BLE al terminal, que reenvía el aviso al recuperar cobertura y descarga el registro completo al volver. Escrituras serverless con TTL nativo (raw 30 días).

-  **Serie consolidada (OLAP).** S3 Parquet + AWS Glue + Redshift Serverless. OLAP por diseño: DynamoDB raw → Glue → S3 Parquet → Redshift, sin motor de series adicional.

-  **Caché y datos de turno.** Redis acelera las lecturas centrales; no se exige Redis en cada sitio. Las APIs entregan una copia cifrada para SQLite/Room y conservan por separado la cola de escrituras sin confirmar. La identidad usa credenciales de 8 horas en bodega y 14 horas en terreno; su caché local de solo lectura tiene TTL de 24 horas en VM-05, VM-C03 y cada E-01, junto al verificador local de relevos (ADR-06).

-  **Mensajería asíncrona (Capa 5).** RabbitMQ en on-premise mediante adaptador AMQP `php-amqplib`; SQS FIFO con sobre JSON y consumidor PHP para reconciliación, colas SQS separadas para trabajos Laravel, y SNS para difusión y alertas en nube. Un único planificador Laravel programa las tareas periódicas. **Dos procesos `erp-sync` en VM-04 consumen RabbitMQ local y, por salida, la cola FIFO de solicitudes al ERP; ERP integrado exclusivamente vía ACL; Hub EDI GS1 centralizado en nube (EANCOM, GS1 XML, EPCIS), AS2 como transporte.**

-  **Analítica / BI.** S3 Data Lake, Redshift Serverless y Glue ETL. Consultas históricas sin degradar el procesamiento transaccional.

-  **Objetos / documentos.** Amazon S3 con Intelligent-Tiering y Object Lock.

-  **IAM / Identidad (Capa 7).** Keycloak (OIDC, SAML, SSO, MFA) como IdP maestro en nube, con caché local de solo lectura de TTL 24 horas y verificador local con manifiesto firmado y PIN personal en VM-05, VM-C03 y cada E-01.

-  **Gestión de secretos (Capa 7).** AWS Secrets Manager y SSM Parameter Store con rotación automática. Cuenta de emergencia fuera de banda, con doble autorización, registro de uso y rotación posterior de credenciales.

-  **Observabilidad (Capa 8).** OpenTelemetry para PHP/Laravel y colectores ADOT on-premise con buffer en disco de 24 horas; plataforma única Amazon CloudWatch para logs (12 meses en línea + 24 en archivo), métricas (13 meses), trazas y tableros (ADR-14).

-  **Gestión de dispositivos (RT-03.18).** Gestión centralizada mediante MDM (Android Enterprise / Zebra DNA, SaaS), con inventario, configuración, actualización de firmware y aplicaciones, bloqueo y borrado remoto del parque móvil.

-  **Contenedores / orquestación.** Imagen PHP 8.5 con servidor HTTP/PHP-FPM para APIs y procesos PHP CLI separados para colas y programación. ECS Fargate aloja los perfiles centrales; Talca y Concepción ejecutan el perfil `wms_only` sobre máquinas virtuales Proxmox, y Docker Compose ejecuta el mismo perfil `wms_only` en los equipos E-01 de los cross-docking. El código y las migraciones de esquema proceden del mismo artefacto versionado.

-  **Infraestructura como Código.** Terraform administra recursos mediante proveedores y estados separados por ambiente; Ansible configura hosts. CDK no administra los mismos recursos: cada activo tiene un único propietario de infraestructura como código.

-  **CI/CD.** GitLab CI como orquestador + AWS CodeBuild para construcción hermética con procedencia SLSA 3; `composer audit`, PHPUnit, PHPStan/Larastan y Laravel Pint verifican dependencias, comportamiento, análisis estático y formato. `swagger-php` genera OpenAPI 3.1 desde atributos PHP; los esquemas AsyncAPI 2.6 se validan y publican en la misma puerta de calidad.

Los servicios AWS consumidos incluyen: CloudFront, AWS WAF, AWS Shield Advanced, ALB, Network Load Balancer, API Gateway, Verified Access, Aurora, ElastiCache, DynamoDB, S3, Redshift Serverless, ECS Fargate, Lambda (solo como autorizador), Route 53, Secrets Manager, Systems Manager, KMS, IAM, Organizations, IAM Identity Center, CloudWatch, Transit Gateway, NAT Gateway, VPC Endpoints, Site-to-Site VPN, SQS, SNS, AWS Backup, GuardDuty, Security Hub, Security Lake, Macie, Inspector, Config, Database Migration Service, Glue, QuickSight, Elastic Container Registry, CodeBuild, Control Tower, CloudTrail e IoT Core+Greengrass.

Laravel conserva una superficie de APIs, políticas y colas coherente para los doce módulos; Django también permitiría el monolito, pero mantener su runtime junto al nuevo obligaría a operar dos cadenas de dependencias y dos familias de trabajadores. La equivalencia se acepta por contratos y pruebas, no por parecido de bibliotecas. PostgreSQL/PostGIS se prefiere a MariaDB por la combinación de transacciones y consultas geográficas del dominio de rutas y sitios; la prueba cubre consultas espaciales y migración. Keycloak se prefiere a un proveedor de identidad exclusivamente en nube porque permite administrar personal propio y externo sin trasladar la autorización de negocio fuera de M1–M12; el relevo local requiere la prueba de 24 horas. API Gateway reduce administración frente a un gateway propio, sujeto a prueba de cuotas y costo bajo el pico. RabbitMQ local más SQS FIFO conserva el trabajo del sitio sin enlace; la deduplicación y el orden por partición se prueban en los consumidores. Angular se conserva por sus componentes y contratos TypeScript. Los costos, el emplazamiento y la redundancia se comprueban en 4.2 y en el registro ADR.

El núcleo utiliza tecnologías con alternativas de despliegue como Laravel, Angular, PostgreSQL, RabbitMQ y Keycloak. Eso facilita la portabilidad, pero no elimina la dependencia de los servicios administrados de AWS. La reversibilidad documenta contratos, exportación de datos y sustitución de adaptadores, junto con el esfuerzo de migración exigido por RT-03.07, que 4.2 acota por servicio.

El Anexo 4-P reúne versiones de referencia, soporte y criterios de actualización. Las versiones menores se fijan en archivos de bloqueo y SBOM y se promueven mediante pruebas de contrato; no se congela una versión sin soporte por los 56 meses. Laravel, PHP, PostgreSQL, Angular y RabbitMQ se revisan conforme a sus políticas oficiales (Laravel, 2026; PHP, 2026; PostgreSQL, 2026; Angular, 2026a, 2026b; RabbitMQ, 2026).

<a id="h-04-partes-4-1-logica-09-implantacion-progresiva-del-backend-laravel-tex-28"></a>

### 4.1.8 Implantación progresiva del backend Laravel

<a id="sec-transicion-laravel"></a>

La implantación conserva los identificadores M1–M12, sus dueños de datos, las rutas y versiones públicas, los eventos JSON, la identidad Keycloak y las reglas offline. El Anexo 4-P muestra cómo se implementan las capacidades del backend; PostgreSQL/PostGIS, RabbitMQ, SQS y los clientes mantienen sus contratos.

La implementación conserva rutas y contratos, repositorios PostgreSQL/PostGIS y eventos JSON. Sustituye el runtime por Laravel/PHP, separa consumidor de integración y trabajos internos, y prueba identidad, trazas y reversión antes de habilitar cada ola.

La implantación comienza por fijar contratos, dueños de datos y esquema PostgreSQL del WMS de 2013 como línea base de migración. Las migraciones Laravel posteriores son aditivas y compatibles con los lectores de la ola previa. M1/M2/M5 se ensayan en un sitio piloto con el WMS legado disponible para reversión; después se habilitan los demás sitios, módulos y trabajadores. En coexistencia, una operación tiene un único escritor autorizado: no se habilita doble escritura de stock, cobros o DTE. Todo evento que cruza tecnologías usa JSON versionado. La reversión devuelve el tráfico al escritor previo solo después de detener el nuevo, conciliar operaciones sin confirmar y verificar esquemas y contratos compatibles. Cada ola cierra con pruebas de 14 horas en terreno, 24 horas por sitio con dos relevos, emisión de guía previa al despacho, 96 camiones en la ventana crítica y reconciliación sin pedidos duplicados.

<a id="h-04-partes-4-1-logica-10-ambientes-del-ciclo-de-vida-y-promocion-de-componentes-tex-29"></a>

### 4.1.9 Ambientes del ciclo de vida y promoción de componentes

Los cinco ambientes del RT-04.01 cumplen propósitos distintos. En **Desarrollo**, el equipo construye los módulos Laravel y las aplicaciones Kotlin, los contratos y las migraciones con datos sintéticos o anonimizados; las pruebas unitarias no necesitan conectarse al ERP real. En **QA**, se despliegan M1–M12, el verificador local y los adaptadores simulados para ensayar integración, regresión, idempotencia y fallas de enlace con datos controlados. En **Preproducción**, el mismo artefacto y las mismas versiones de contratos se ensayan con topología equivalente a producción y volumen representativo de septiembre; se prueban los 186 terminales de bodega, el relevo de turnos, la emisión de guía por el ERP y la reconciliación. Toda diferencia de escala o configuración se declara antes de aceptar el ensayo, conforme a RT-04.02.

En **Producción**, los módulos sirven datos reales con acceso restringido y auditado; los desarrolladores no corrigen transacciones directamente. El ambiente de **Recuperación ante desastres** conserva la versión compatible de los componentes y permite ensayar conmutación y retorno al menos dos veces al año, sin presumir que una réplica remota contiene eventos aún no enviados desde un sitio aislado. Los cinco deben estar operativos en el hito H3; su emplazamiento, capacidad y segregación de redes se demuestran en 4.2, no mediante el simple nombre del ambiente.

La promoción conserva la identidad del artefacto PHP, `composer.lock` y la versión de esquema desde QA hasta producción. La revisión por pares, pruebas de contrato OpenAPI/AsyncAPI, PHPUnit, PHPStan/Larastan, `composer audit`, análisis de secretos e imágenes bloquean un despliegue defectuoso (RT-04.03–04.05). Cada cambio registra requisito, commit, prueba, aprobación y despliegue; una migración incompatible con eventos sin confirmar se detiene o conserva un lector de la versión precedente. La recuperación ante desastres verifica además la lectura de datos y mensajes generados durante la contingencia antes del retorno al primario.

<a id="h-04-partes-4-1-logica-11-patrones-de-diseno-y-continuidad-tex-30"></a>

### 4.1.10 Patrones de diseño y continuidad

<a id="sec-continuidad-logica"></a>

La continuidad se articula con ISO 22301 para la gestión de continuidad del negocio y con ISO/IEC 27031 para la preparación de las TIC que la sostiene, conforme a RT-10.03 y RT-10.04 (ISO, 2019, 2025). En esta vista, su aplicación se concreta en las dependencias entre módulos, las funciones que pueden continuar desconectadas, los estados sin confirmar y las condiciones para volver a una operación consistente. Esta correspondencia de diseño no constituye una certificación ni acredita por sí sola el cumplimiento integral de las normas.

Ante pérdida de conectividad, M1, M2 y M5 conservan la operación local y M9 mantiene el bloqueo sanitario; M3 y M6 conservan la captura de terreno durante las autonomías definidas. Las confirmaciones que dependen de crédito, stock central o documentos del ERP permanecen explícitamente sin confirmar o bloqueadas según su regla. La continuidad protege la evidencia y la seguridad de la operación: no habilita una salida sin autorización tributaria ni permite levantar un bloqueo sanitario para recuperar velocidad.

La recuperación lógica exige restablecer identidad y autorización, disponer del estado transaccional y de los eventos sin confirmar, y habilitar después el procesamiento y la reconciliación. Cada consumidor confirma solo operaciones persistidas, deduplica los reenvíos y deriva los conflictos a su responsable. Antes de cerrar la contingencia se cotejan pedidos, reservas, lotes, entregas y rendiciones con sus identificadores de origen; las operaciones sin confirmar y las excepciones quedan visibles y auditadas. El orden concreto de restauración y la capacidad de respaldo se documentan en 4.2 y 4.3.

La evidencia de aceptación vincula cada servicio con su requisito, módulo, dependencia, objetivo de recuperación y prueba. Se ensayan pérdida de WAN durante 24 horas en el sitio, captura móvil durante 14 horas, indisponibilidad del ERP, relevo sin IdP y recuperación con mensajes repetidos. Se mide la conservación de operaciones confirmadas, el respeto de los bloqueos, la ausencia de duplicados y el tiempo hasta recuperar un estado conciliado. Una pérdida completa del sitio requiere una prueba de restauración distinta del corte WAN, contrastada con RTO ≤ 4 horas y RPO ≤ 15 minutos para los servicios críticos. La extracción continua por fibra, LTE y satélite sostiene el RPO, verificado con AL-DR-01; 4.3.2 justifica el límite residual.

La arquitectura aplica un conjunto de patrones de diseño que responden a las restricciones específicas de la operación de Puelche:

**Registro local y sincronización idempotente.** Cada escritura recibe un UUID declarado por el cliente que se conserva al reintentar. El evento permanece en la cola local hasta que el servicio de negocio confirma su procesamiento. Ese servicio deduplica dentro de una ventana documentada (RT-02.06) y resuelve conflictos con reglas deterministas y bitácora auditable (RT-03.12). La copia de lectura en SQLite/Room se actualiza por separado. Así, renovar precios o stock no elimina un pedido sin confirmar y el trabajo de terreno no depende de una consulta a Redis en tiempo real.

**Servicios sin estado durable en memoria.** Las bases de datos y las colas conservan el estado de negocio; las sesiones utilizan los mecanismos de identidad definidos. Sustituir una instancia no debe perder el progreso de una operación. El acceso desconectado respeta las vigencias de las credenciales y las restricciones explicadas en la capa de seguridad.

**Degradación controlada sin pérdida silenciosa.** Cuando un componente no responde, la operación continúa en modo reducido informado a la persona usuaria ("modo offline"). Ninguna degradación produce pérdida de una transacción de venta o entrega: si una escritura no llega al servidor, queda en el buffer local del dispositivo, visible como no confirmada y reconciliada en la sincronización posterior (RT-02.09). La clasificación de servicios (RT-10.02) distingue cuatro niveles, conforme a la Tabla de 4.2: crítico, preparación, despacho y emisión de la guía durante la ventana 05:30–07:00, con el bloqueo por excursión térmica y la identidad de bodega que lo habilitan; alto, toma de pedido y consulta de stock y crédito, entrega y evidencia, planificación de rutas, los demás DTE, integración con el ERP, cobranza y rendición, registro de temperatura; medio, canal moderno (EDI), notificaciones, analítica y tableros, portales, consultas de geolocalización, registros de auditoría y seguridad; bajo, reportería e informes a pedido.

**Resiliencia con cortacircuitos y colas.** Las llamadas remotas tienen un tiempo máximo de espera explícito (RT-02.08). Las operaciones reintentables utilizan espera creciente con variación aleatoria y un cortacircuitos que suspende temporalmente las llamadas a un servicio que falla. Si el ERP no está disponible, la preventa conserva la captura de pedidos, mientras las confirmaciones dependientes del legado permanecen sin confirmar. Las colas y sus DLQ permiten recuperar el procesamiento; los consumidores deben deduplicar porque un mensaje puede entregarse más de una vez.

**Integración con legados mediante ACL.** Los módulos M1, M5, M7 y M11 intercambian información con el ERP a través de adaptadores; no absorben su responsabilidad tributaria ni modifican su código. Las capacidades del WMS 2013 se reemplazan gradualmente en M1, M2 y M5. La ACL mantiene separados el modelo de negocio de la solución y los formatos del legado, en coherencia con RT-02.14. No se permiten escrituras directas al ERP.

**Correlación de extremo a extremo.** Cada transacción lleva un `transaction_id` que acompaña las solicitudes y los eventos, incluidos los capturados sin conexión. Al sincronizar, ese identificador permite relacionar métricas, trazas y registros en la plataforma común de observabilidad de nube y sitios locales (RT-03.16 y Art. 16.4).

**Gobierno de contratos y versionado.** Las APIs de negocio y de integración se documentan desde el código, con actualización automática de OpenAPI 3.1 (síncrona) y AsyncAPI 2.6 (eventos), semver estricto, propietario declarado por módulo, compatibilidad hacia atrás y aviso mínimo de 6 meses antes de deprecar una versión (RT-05.16/17).

**Seguridad Zero Trust.** Cada solicitud se verifica explícitamente, sin presuponer la confiabilidad de ninguna red, dispositivo o identidad (NIST, 2020, SP 800-207). Los servicios utilizan mTLS (RT-05.18), los secretos tienen rotación automática (RT-04.09) y los registros de auditoría son inmutables (RT-16.07). La segmentación y las conexiones entrantes al sitio local se especifican en 4.2.

**Separación transaccional y analítica.** Los tableros consultan Redshift Serverless, no el transaccional en vivo. Los eventos incrementales permiten mantener las latencias de hasta 5 minutos para operación, 2 horas para cierre comercial y 4 horas para gestión. Las tareas pesadas se programan fuera de la ventana crítica, sin detener la actualización incremental necesaria para el tablero operacional.

<a id="h-04-partes-4-1-logica-11-patrones-de-diseno-y-continuidad-tex-31"></a>

#### 4.1.10.1 SOLID aplicado a los contratos de negocio

La responsabilidad única se comprueba en el flujo de un pedido: M3 captura y confirma el pedido, M2 decide si reserva stock, M5 ejecuta la preparación y la ACL traduce hacia el ERP. Ninguno de esos componentes puede asumir la decisión del otro por compartir un proceso Laravel. Para extender el canal moderno, M11 incorpora un adaptador por cadena bajo un contrato publicado; M3 no se modifica para aprender un nuevo formato EDI. Esa es la aplicación concreta del principio abierto/cerrado.

Un adaptador nuevo sustituye a uno previo solo si conserva las respuestas, errores e idempotencia exigidos por el contrato versionado: las pruebas de contrato verifican esa sustitución. Las interfaces se separan por capacidad y autorización —consulta de stock, reserva, recepción de POD y liberación sanitaria— para que un cliente de lectura no reciba por accidente una operación de escritura. Finalmente, M3, M5 y M7 dependen de puertos de negocio para inventario, documentos y mensajería, no de llamadas directas al SDK de una nube o a tablas del ERP. En QA se reemplazan esos puertos por dobles de prueba; en producción los adaptadores implementan el contrato. Las pruebas de contrato verifican sustitución, segregación de interfaces e inversión de dependencias.

<a id="h-04-partes-4-1-logica-12-registro-de-decisiones-de-arquitectura-tex-32"></a>

### 4.1.11 Registro de decisiones de arquitectura

<a id="sec-adr"></a>

Las 22 decisiones de arquitectura se resumen en la Tabla [3](../LAFROX-Subdocumento4.md#tab-resumen-adr). El Anexo 4-O contiene para cada ADR la decisión, alternativas, criterio, consecuencias, evidencia y requisitos que la sustentan.

<a id="tab-resumen-adr"></a>

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

<a id="h-04-partes-4-1-logica-13-puntos-unicos-de-falla-y-riesgos-residuales-tex-33"></a>

### 4.1.12 Puntos únicos de falla y riesgos residuales

<a id="sec-spof"></a>

RT-02.11 exige identificar las dependencias singulares que subsisten y justificar el riesgo residual. La Tabla [4](../LAFROX-Subdocumento4.md#tab-spof) distingue su efecto, la continuidad prevista y la condición de aceptación. Una réplica o una cola reduce el impacto, pero no elimina por declaración la dependencia.

<a id="tab-spof"></a>

**Tabla 4 — Dependencias singulares y riesgo residual**

| **Dependencia** | **Efecto si falla** | **Continuidad prevista** | **Aceptación** |
| --- | --- | --- | --- |
| Identidad central | No hay altas ni revocación remota. | Asignaciones vigentes y servicio local. | Prueba de relevo 24 h. |
| ERP y emisión DTE | Se retrasa una nueva guía. | Preemisión nocturna y ERP por tres caminos; la salida sin guía válida se bloquea. | AL-DTE-01 con 96 salidas. |
| Consolidación central de stock | La reserva central queda fechada. | Cada sitio opera localmente y preventa captura pedidos sujetos a validación. | Conciliación de eventos por sitio. |
| SII y pasarela de pago | No hay respuesta en línea. | Reintento y cobro alternativo aprobado. | Sin confirmar no equivale a aprobado. |
| Planificador experto | Faltan decisiones ante excepciones. | Reglas de M4 y suplente capacitado. | Prueba antes de su retiro. |

 Fuente: elaboración propia de LafroX a partir de Bases Técnicas Transversales, RT-02.11, y caso 02.

Las dependencias externas conservan riesgo residual que exige prueba o contingencia aprobada.

El ERP permanece como único emisor ante el SII mediante fibra, LTE y satélite de Talca; un cambio de carga invalida la guía preemitida y exige una nueva. El riesgo de identidad local tampoco se declara cerrado antes de probar cada relevo de turno durante un corte de 24 horas. El emplazamiento y la redundancia física se verifican en 4.2.

<a id="h-04-partes-4-1-logica-14-comparacion-de-alternativas-arquitectonicas-tex-34"></a>

### 4.1.13 Comparación de alternativas arquitectónicas

<a id="sec-alternativas-arquitectonicas"></a>

La comparación considera la carga real, la continuidad desconectada, la reversión y la dotación que deberá operar la solución. La Tabla [5](../LAFROX-Subdocumento4.md#tab-alternativas) resume las elecciones lógicas; los ADR explicitan su criterio y consecuencia operativa. La evaluación económica pertenece a los apartados de costos.

<a id="tab-alternativas"></a>

**Tabla 5 — Alternativas lógicas y criterio de selección**

| **Decisión** | **Seleccionada** | **Alternativa viable** | **Criterio decisivo** |
| --- | --- | --- | --- |
| Estilo del núcleo | Monolito modular M1–M12 con perfiles separados. | Servicios por dominio. | Menor carga operativa con 31.000 pedidos/mes. |
| Framework backend | Laravel 13/PHP 8.5 con límites PSR-4. | Django/Python con los mismos contratos. | Un runtime PHP y pruebas de paridad de contratos, datos y colas. |
| Aplicación terreno | Kotlin nativo. | Desarrollo multiplataforma. | Integración Zebra y persistencia local. |
| Mensajería | Broker local y cola de nube. | Broker solo en nube. | Conservación del trabajo con enlace caído. |
| WMS 2013 | Reemplazo por olas M1/M2/M5. | Sustitución simultánea. | Reversión por sitio y capacidad. |

 Fuente: elaboración propia de LafroX a partir de Registro ADR y volumetría del caso 02.

El WMS y el broker de cada sitio sostienen recepción y despacho sin WAN; el monolito modular acota el número de procesos a operar.

El Artículo 16 de las Bases Administrativas exige el despliegue híbrido. Su distribución concreta corresponde a 4.2.

<a id="h-04-partes-4-1-logica-15-relacion-entre-las-vistas-de-arquitectura-tex-35"></a>

### 4.1.14 Relación entre las vistas de arquitectura

<a id="sec-iso42010"></a>

RT-02.03 exige cinco vistas de la arquitectura: lógica, procesos, despliegue, datos y seguridad. El Anexo 4-S define sus interesados, preocupaciones, modelos y reglas de correspondencia, siguiendo la organización de descripciones de ISO/IEC/IEEE 42010:2022 (ISO, 2022a). La integración atraviesa esas vistas; no se presenta como una sexta vista exigida por la Base.

Operaciones necesita comprobar que un pedido puede avanzar sin perder su lote ni saltarse una autorización; Calidad necesita seguir un lote hasta su receptor; Seguridad necesita distinguir quién puede liberar una carga; y TI necesita aislar una falla y recuperar el estado. Las vistas responden a esas preocupaciones con los mismos identificadores M1–M12, INT-01–15 y los componentes transversales del Anexo 4-N. Así se puede pasar de una secuencia a su dueño de datos, contrato y control sin cambiar de vocabulario.

Las correspondencias se comprueban en ambos sentidos: todo evento tiene productor y consumidores; toda escritura tiene dueño; toda función desconectada tiene persistencia y autorización locales; y todo componente desplegado debe realizar una responsabilidad inventariada. Una diferencia se registra con requisito afectado y ADR responsable. La cobertura lógica del inventario no se confunde con el cotejo de emplazamientos y centros de datos.

La vista lógica desarrolla aquí las responsabilidades y sus relaciones. El despliegue y los centros de datos se acreditan en 4.2–4.3 y el modelo detallado de datos en el capítulo 5; esta distribución de evidencia no sustituye su revisión integrada.

<a id="h-04-partes-4-1-logica-16-funciones-disponibles-y-no-disponibles-sin-conexion-tex-36"></a>

### 4.1.15 Funciones disponibles y no disponibles sin conexión

<a id="sec-funciones-offline"></a>

Conforme a RT-03.10, la captura del turno de 14 horas en terreno y la operación local de 24 horas en los centros de distribución conservan sus eventos hasta recibir confirmación. RT-03.13 de las Bases Transversales exige nombrar también lo que no funciona sin red y el procedimiento que lo suple; el caso fija bajo ese mismo identificador los plazos de sincronización tras la reconexión. El Anexo 4-J distingue ambos casos; una operación sin confirmar nunca equivale a aprobación de un tercero.

La operación local conserva la captura; las autorizaciones externas esperan conexión o procedimiento aprobado. AL-OFF-01, en el Anexo 4-M, exige un corte de 24 horas con relevos a las 8 y 16 horas, verificación de permisos, reinicio de componentes y reconciliación. La prueba incluye recepción, preparación y despacho con guía válida preemitida al cerrar la carga nocturna. AL-DTE-01 ensaya el cambio de carga que invalida esa guía y exige otra mediante `erp-sync` en VM-04, el ERP y cualquiera de los tres caminos de Talca. Aprobar la captura o el relevo de identidad no basta para acreditar la continuidad completa del despacho.

La copia de stock, crédito y precios lleva fecha de actualización; al superar su vigencia se presenta como referencia, no como aprobación de la venta. El conductor tampoco presenta una captura POS como pago autorizado. El Portal de Clientes instalado conserva el catálogo, los precios con su fecha y el pedido armado sin señal; no reserva stock ni confirma precio o fecha de entrega hasta que M3 recibe el pedido, como verifica AL-CLI-01 del Anexo 4-M. Para el relevo de turno en bodega, la validación local de identidad debe probarse durante 24 horas antes de acreditar la autonomía completa.

<a id="h-04-partes-4-1-logica-17-reglas-de-reconciliacion-tex-37"></a>

### 4.1.16 Reglas de reconciliación

<a id="sec-reglas-reconciliacion"></a>

Toda reconciliación se resuelve por regla de negocio declarada, nunca por la sola marca de tiempo. La clave UUID generada por el cliente se conserva en todos los reintentos y el resultado se retiene para deduplicación durante 30 días; un lote más antiguo se aísla para revisión antes de admitir una nueva escritura. El resultado incluye identificador, versión, regla aplicada, actor y fecha. El Anexo 4-K muestra los conflictos de negocio principales.

Los conflictos de negocio dejan rastro de regla y resultado para revisión posterior.

La replicación es un flujo de continuidad, no una regla para resolver conflictos. INT-12 usa DMS desde Talca hacia una réplica de lectura; los demás sitios sincronizan eventos mediante INT-03 e INT-04. Durante un corte, la base de cada sitio conserva autoridad sobre su operación y retiene cambios hasta el acuse durable, dentro de la capacidad dimensionada. La extracción continua por fibra, LTE y satélite en los CD conserva una copia durable fuera del sitio y sostiene RPO ≤ 15 minutos. AL-DR-01 del Anexo 4-M mide el punto recuperable; el límite residual se justifica en 4.3.2.

<a id="h-04-partes-4-1-logica-18-articulacion-entre-prueba-de-entrega-dte-y-acuse-tex-38"></a>

### 4.1.17 Articulación entre prueba de entrega, DTE y acuse

<a id="sec-pod-dte-acuse"></a>

La guía de despacho electrónica debe estar vinculada a la salida de mercadería antes de iniciar el traslado. La aplicación no la emite: M5 entrega los datos de despacho a `erp-sync` en VM-04 y por la capa anticorrupción al ERP, que conserva la responsabilidad tributaria y devuelve folio, estado y documento. M6 captura después la recepción efectiva, incluidos bultos rechazados, identidad del receptor y evidencia. El acuse técnico de recepción o procesamiento ante el SII y el acuse de recepción de mercaderías del destinatario son hechos distintos; cada uno conserva su origen, fecha y estado.

<a id="h-04-partes-4-1-logica-18-articulacion-entre-prueba-de-entrega-dte-y-acuse-tex-39"></a>

#### 4.1.17.1 Secuencia y excepciones

La secuencia lógica es: preparación confirmada en M5; solicitud nocturna de guía al ERP mediante `erp-sync` y ACL de VM-04; autorización de salida con el documento disponible; captura de POD y diferencias en M6; conciliación de la entrega en M7/M8; y, si corresponde, solicitud al ERP de factura, nota de crédito o tratamiento tributario de la devolución. Un mismo `transaction_id` relaciona pedido, guía, entrega, evidencia, acuses y documentos posteriores. El acuse del destinatario se obtiene por el mecanismo que acuerde el CLIENTE conforme a la normativa aplicable; una fotografía o un QR no se presume equivalente por sí solo.

Si el ERP o su canal tributario no confirma la guía antes de la salida, M5 muestra el despacho como bloqueado y lo deriva al responsable de Operaciones y Tributación para aplicar únicamente la contingencia autorizada por el CLIENTE. La captura offline del POD permite registrar una entrega ya despachada; no autoriza emitir retroactivamente una guía desde el teléfono. Esta separación protege la continuidad de la evidencia sin atribuir a la aplicación facultades tributarias que permanecen en el ERP.

<a id="h-04-partes-4-1-logica-18-articulacion-entre-prueba-de-entrega-dte-y-acuse-tex-40"></a>

#### 4.1.17.2 Control de liberación en la ventana crítica

M5 conserva los estados carga confirmada, guía solicitada, resultado incierto, guía disponible y salida liberada. La solicitud lleva una clave estable por despacho y versión de carga. Ante un timeout se consulta el resultado de esa misma solicitud antes de repetirla; no se genera otra guía a ciegas. Solo se libera cuando la guía corresponde a la carga vigente y su evidencia está disponible localmente. Una modificación efectiva de carga invalida la guía y exige que el ERP anule el documento según su procedimiento y emita uno nuevo antes de la salida; si no hay conectividad para emitirlo, se conserva la carga anterior amparada por su guía vigente. El acuse técnico del SII, el documento emitido y la autorización de traslado no se representan con un único booleano.

Al cerrar la carga nocturna se solicita la guía por adelantado, sin confundir anticipación con contingencia. Antes de las 05:30, Operaciones revisa las salidas programadas y las guías disponibles. Durante 05:30–07:00 se prioriza INT-07 sobre reportes y cargas masivas; una incidencia identifica los camiones afectados, hora prevista, responsable y estado documental. Los despachos con documentación válida siguen su curso; ante un cambio de carga, la nueva guía la emite el ERP de Talca por cualquiera de sus tres caminos y, para Concepción y los cross-docking, requiere además un camino disponible del sitio. Ningún perfil de supervisor puede omitir ese control con una autorización genérica.

La preemisión nocturna permite liberar cada camión con la carga amparada por su guía vigente sin depender de Internet durante la ventana; si cambia la carga y no hay camino hasta el ERP, sale solo con la carga que ampara la guía vigente y el ajuste pasa a la ruta siguiente. Ningún camión sale sin guía válida. AL-DTE-01 ensaya las 96 salidas con fallas inyectadas, preemisión nocturna, cambio de carga y emisión del ERP ante el SII por fibra, LTE y Starlink en espera caliente de Talca. La prueba registra folio, anulación, nueva guía y estado de cada salida.

El Anexo 4-U distingue emisión tributaria, constancia operativa y acuse del receptor. La firma, fotografía o QR del POD no se equiparan automáticamente al recibo exigible: el mecanismo se selecciona según el receptor y se canaliza por el ERP o el perfil EDI aprobado (SII, 2018, s. f.-a, s. f.-b).

<a id="h-04-partes-4-1-logica-19-identidad-y-ciclo-de-vida-de-conductores-externos-tex-41"></a>

### 4.1.18 Identidad y ciclo de vida de conductores externos

<a id="sec-conductores-externos"></a>

Los conductores de transportistas externos ( 160, de 10 empresas) no pertenecen a la dotación de Puelche. Antes de entregar una ruta, el transportista declara la identidad del conductor y su vínculo con la empresa. El responsable de despacho aprueba la asignación conductor–vehículo–turno; el alta inicial requiere conexión para verificar un OTP de un solo uso. El identificador del conductor y el del transportista acompañan cada `EntregaRegistrada`. La autorización se limita a la ruta asignada y a M6, M7 y M8 mediante rol y atributos de turno, sitio y dispositivo.

La aplicación conserva localmente una asignación firmada para el turno de hasta 14 horas y permite capturar eventos mientras no exista red. La caché local de identidad, de solo lectura y TTL de 24 horas, no acorta por sí sola la vigencia de esa asignación de terreno; tampoco la renueva. Una persona reemplazante que no fue dada de alta no obtiene una nueva identidad sin conexión. En ese caso Operaciones reasigna el turno a un conductor ya habilitado y registra la excepción; la rotación no autoriza compartir el OTP ni la cuenta del conductor previo.

Al finalizar el turno expiran la asignación y sus permisos. Si se denuncia pérdida de dispositivo o baja anticipada, Keycloak revoca el acceso conectado y el equipo borra los datos al recuperar conexión. Mientras permanezca sin señal no puede prometerse revocación remota inmediata: la duración de la asignación limita la exposición y la incidencia se registra para bloquear la rendición y revisar la evidencia capturada durante el intervalo.

<a id="h-04-partes-4-1-logica-20-primer-cuello-de-botella-bajo-la-carga-de-septiembre-tex-42"></a>

### 4.1.19 Primer cuello de botella bajo la carga de septiembre

<a id="sec-cuello-botella-septiembre"></a>

Septiembre eleva las entregas diarias de aproximadamente 1.400 a 2.600 durante tres semanas. Las 2.600 entregas ocurren a lo largo de la jornada; la ventana 05:30–07:00 concentra la salida de 96 camiones, no todas las firmas de entrega. En esa ventana, el primer cuello de botella probable es la confirmación de guías del ERP mediante la ACL: es una dependencia singular y aumentar réplicas Laravel no acelera al emisor legado. La base transaccional de Talca, la WAN al reconectar y la transferencia de evidencias son candidatos adicionales, no recursos cuya saturación ya se haya medido. La Tabla [6](../LAFROX-Subdocumento4.md#tab-cuello-botella) muestra cómo contrastar la hipótesis; RT-09.05 exige sustentar el primer límite con una prueba reproducible.

<a id="tab-cuello-botella"></a>

**Tabla 6 — Detección del primer cuello de botella**

| **Recurso** | **Señal de saturación** | **Respuesta lógica** | **Prueba** |
| --- | --- | --- | --- |
| ERP por ACL | Aumentan guías sin confirmar y latencia p95 de emisión. | Preemitir al cerrar la carga nocturna; invalidar y reemitir si cambia. | 96 camiones en ventana. |
| VM-02, base transaccional de Talca | Crecen la latencia de confirmación y la espera de escritura. | Medir y aliviar contención de escrituras del WMS local. | Carga de preparación y despacho de Talca. |
| Cola de integración | Crecen edad del mensaje y DLQ. | Priorizar guías; diferir reportes. | Corte y reconexión. |
| M2 en bodega | Crecen espera de reserva y bloqueos de stock. | Serializar por SKU y aislar consultas. | Doble compromiso en peak. |

 Fuente: elaboración propia de LafroX a partir de Caso 02, numeral 14.1 y ventana 05:30–07:00.

La emisión de guías debe medirse antes de atribuir el límite al cómputo escalable.

Al cerrar la carga nocturna, `erp-sync` en VM-04 solicita la guía al ERP mediante la ACL local; el ERP dispone de fibra, LTE y satélite para comunicarse con el SII. Cualquier cambio de carga invalida la guía y exige otra antes de liberar. Se mide el número de guías sin confirmar antes de cada salida y se alerta al responsable de despacho; el camión afectado no se marca como liberado mientras falte el documento o una contingencia autorizada. La prueba de carga debe confirmar si el ERP es efectivamente el primer límite y ajustar esta hipótesis con medición, como exige RT-09.05.

El Anexo 4-T especifica percentiles, ventanas de ensayo, carga de 1,5 veces el peak y escenario de crecimiento de tres veces, con colas y procesos aislados. Los resultados se deben medir; los cálculos de escenario no son evidencia de capacidad ejecutada.

<a id="h-04-partes-4-1-logica-21-decisiones-del-numeral-16-1-del-caso-tex-43"></a>

### 4.1.20 Decisiones del numeral 16.1 del caso

<a id="sec-16-decisiones-caso"></a>

El Anexo 4-L conserva el número y la pregunta de cada una de las dieciséis decisiones del caso. Distingue una regla de diseño de una validación que todavía requiere al CLIENTE: una fila marcada para validación no equivale a una aprobación suya. El registro de supuestos del capítulo 3 debe conservar el fundamento, impacto e instancia de validación de cada decisión.

Las validaciones se identifican por su número de origen para consulta al CLIENTE.

La matriz permite comprobar qué decisión implementa cada módulo. En particular, la identidad externa corresponde al número 5 y el destino del WMS al 14; ninguna de ellas debe desplazarse para llenar una tabla de cumplimiento.

<a id="h-04-partes-4-1-logica-22-condiciones-y-supuestos-de-diseno-tex-44"></a>

### 4.1.21 Condiciones y supuestos de diseño

<a id="sec-contradicciones"></a>

La lógica adopta seis instalaciones en total, de las cuales cinco son sitios logísticos con servicio local y la sexta es la casa matriz de Talca, contigua al CD principal y sin cómputo propio (Caso 02, cap. 2.3). La parametrización de sitios evita codificar el número en cada módulo.

Los cortes frecuentes de dos horas descritos en la operación son el escenario ordinario. Los límites de diseño son más exigentes: un turno de 14 horas en terreno y 24 horas en cada centro de distribución. No se reduce la autonomía porque el incidente más común sea más corto.

El relevo de turnos sin IdP, la autorización tributaria de salida y la pérdida de sitio se verifican con AL-OFF-01, AL-DTE-01 y AL-DR-01 del Anexo 4-M. Los objetivos exigidos siguen siendo RTO ≤ 4 horas y RPO ≤ 15 minutos para servicios críticos. La extracción continua por fibra, LTE y satélite de los CD sostiene el RPO ante la caída de dos caminos; AL-DR-01 verifica el punto recuperable y la recuperación del WMS de Talca en la nube. El límite residual se justifica en 4.3.2.

El Anexo 4-V reúne los protocolos de aceptación AL-DTE-01, AL-POD-01, AL-SLA-01, AL-OFF-01, AL-CLI-01, AL-DR-01 y AL-PERF-01. Las actas registran configuración, fallas inyectadas, puntos de recuperación, salidas documentadas y resultados observados; 4.3.2 justifica el límite residual de continuidad.
