<!-- Fuente: Subdocumento_4_LateX/04_arquitectura_fisica/partes/14_m_decisiones_adr.tex — conversión fiel; editar el .tex y regenerar -->

<a id="sec:m-registro-de-decisiones-de-arquitectura"></a>
# 4.4 Registro de decisiones de arquitectura

Registro consolidado de las dieciséis decisiones de arquitectura que condicionan la solución. Para cada decisión se declara la elección, las alternativas descartadas y el criterio de selección; cuando corresponde, se exige evidencia verificable.

<a id="sub:adr-01"></a>
## 4.4.1 ADR-01 · Estilo arquitectónico

**Decisión adoptada.** Monolito modular en Laravel 13 sobre PHP 8.5, con los módulos M1–M12 separados por espacios de nombres PSR-4 y dependencias fijadas por `composer.lock`. Un solo artefacto, construido una vez por versión, se ejecuta en perfiles separados: API y `wms_only` con PHP-FPM, y shipper, consumidor de reconciliación, trabajos y planificador como procesos PHP de línea de comandos. El motor de optimización de rutas de M4 y el transporte AS2 de M11 quedan fuera del artefacto, tras un contrato versionado.

**Alternativas descartadas:**

- *Monolito modular en Django y Python 3.12*: técnicamente viable con los mismos contratos, pero la arquitectura lógica adopta Laravel y mantener ambos runtimes obligaría a operar dos cadenas de construcción, de dependencias y de parches.
- *Microservicios en EKS*: el caso no exige desplegar ni escalar cada módulo por separado, cuatro personas no operan un plano de control y el costo total de propiedad en 56 meses sube sin beneficio.
- *Monolito clásico del WMS de 2013*: sin fronteras de módulo y con el proveedor desaparecido, lo que impide desplegar los módulos por separado.
- *Traducir a PHP el ruteo y el AS2 sin prueba*: la equivalencia de un solver o de un conector no se deduce del cambio de lenguaje, por eso ambos se aíslan.

**Criterio de selección.** Coherencia con la arquitectura lógica (4.1); pertinencia al volumen real; operabilidad por cuatro personas; despliegue y escalado independiente por perfil sin particionar el dominio.

**Consecuencias.** La imagen incluye PHP-FPM, el intérprete de línea de comandos y las extensiones declaradas en la arquitectura de despliegue; el pipeline agrega `composer audit`, PHPUnit, PHPStan/Larastan y Pint; el dimensionamiento de los perfiles se recalcula para PHP en lugar de trasladar los valores anteriores. El motor de ruteo agrega una imagen propia al pipeline y una tarea de Fargate bajo demanda.

**Evidencia exigida.** Pruebas de paridad de contratos, datos y colas; prueba de carga por perfil; y, para el motor de ruteo, la generación de rutas de toda la operación en menos de 20 minutos, que es condición de aceptación del motor que se seleccione.

<a id="sub:adr-02"></a>
## 4.4.2 ADR-02 · Conectividad WAN

**Decisión adoptada.** Doble camino por sitio: fibra + LTE en los centros de distribución, Starlink + LTE en los cross-docking. Conmutación automática $<$ 30 s.

**Alternativas descartadas:**

- *Fibra en cross-docks*: naves industriales sin cobertura de fibra; costo de obra desproporcionado.
- *VSAT GEO*: latencia 500–700 ms RTT; penaliza el tiempo de respuesta y cuesta más.
- *Tri-camino (fibra + Starlink + LTE)*: tercer camino no aporta disponibilidad significativa dado que cada sitio opera autónomamente ante pérdida total de enlace (24 h CD, 14 h terreno).

**Criterio de selección.** Dos caminos de física distinta evitan el punto único de falla; la autonomía local cubre la pérdida total de enlace, por lo que un tercer camino es innecesario; cero mantención de radio para el equipo de 4 personas del CLIENTE.

<a id="sub:adr-03"></a>
## 4.4.3 ADR-03 · Modelo de despliegue híbrido

**Decisión adoptada.** Borde operacional on-premise (WMS maestro Talca, edge Concepción, WMS en cross-docks) + carga principal en AWS. 11 componentes on-prem, 12 híbridos, 13 nube pura.

**Alternativas descartadas:** *Solo nube*: inadmisible; sin enlace la bodega muere en minutos; picking en cámara -22 °C inviable con RTT 40–80 ms; *Solo on-premise*: inadmisible.

**Criterio de selección.** Único modelo que cumple el despliegue híbrido obligatorio; latencia ≤ 1 s en cámara resuelta localmente; autonomía 24 h CD / 14 h terreno; TCO contenido con servicios administrados AWS.

<a id="sub:adr-04"></a>
## 4.4.4 ADR-04 · Persistencia políglota

**Decisión adoptada.** PostgreSQL+PostGIS (transaccional WMS, CP), Aurora (OLTP cloud + DRP), DynamoDB (IoT raw, AP, TTL 30 d), S3+Redshift Serverless (OLAP + series de temperatura), S3 Object Lock/Glacier (retención legal por dominio de datos, de 5 a 7 años según la tabla de respaldos). La aplicación accede a PostgreSQL con PDO y el Query Builder de Laravel; las consultas geográficas de M4 usan SQL PostGIS parametrizado sobre índices espaciales GiST, y el esquema evoluciona con migraciones Laravel aditivas. La réplica DMS del WMS alimenta solo un esquema de réplica de lectura; el estado central se actualiza por los eventos de reconciliación, con una clave de origen única por evento.

**Alternativas descartadas:**

- *Motor único relacional*: no escala ingesta IoT sin degradar picking.
- *InfluxDB*: segundo motor exótico a operar; serie de tiempo cabe en capa OLAP.
- *DynamoDB para todo*: no ofrece ACID cross-tabla para reconciliación determinista.

**Criterio de selección.** Posición CAP declarada por dominio; 3 motores administrados operables por el equipo de TI del CLIENTE; retención sanitaria D.S. 977/96 con inmutabilidad; RPO ≤ 15 min por réplica Aurora.

<a id="sub:adr-05"></a>
## 4.4.5 ADR-05 · Mensajería asíncrona

**Decisión adoptada.** La cadena de eventos sigue cuatro pasos:

1. Publicación local: RabbitMQ opera por sitio con colas durables, mensajes persistentes y confirmación de publicación, como buffer de 24 h.
2. Envío del shipper: un proceso PHP con el adaptador AMQP `php-amqplib` publica cada evento como sobre JSON canónico y versionado en una cola SQS FIFO de reconciliación, por HTTPS hacia un VPC Endpoint, y solo retira el mensaje local cuando SQS confirma la recepción.
3. Consumo: un proceso PHP dedicado lee esa cola con el SDK de AWS y valida el esquema del sobre.
4. Confirmación: el consumidor aplica el sobre y confirma solo después de persistir el resultado.

Los trabajos internos de Laravel usan colas SQS distintas, de modo que ningún sobre externo llega al deserializador de trabajos del framework. IoT Core MQTT mantiene la ingesta del borde.

**Alternativas descartadas:**

- *REST síncrono*: no sobrevive un corte a mitad de ventana y rompe la reconciliación.
- *Kafka/MSK*: operar clústeres en cinco sitios es desproporcionado para el equipo disponible y para el volumen de mensajes del caso.
- *Una sola cola SQS para eventos y trabajos*: acopla el formato externo al serializador del framework e impide versionar el sobre.
- *Redis y Horizon en los sitios*: agregan un tercer motor local sin mejorar la durabilidad que ya dan PostgreSQL y RabbitMQ.
- *Workers Celery*: correspondían al backend Django y se retiran con él.

**Criterio de selección.** Resiliencia offline (buffer local y reproducción idempotente); reconciliación determinista; independencia del formato respecto del lenguaje; Zero Trust (todo saliente); costo total proporcional al volumen.

**Consecuencias.** La cola FIFO agrupa el orden por sitio y agregado de negocio, deduplica por el identificador del evento, usa una visibilidad de 60 s, cinco intentos antes de la cola de mensajes fallidos y una retención de 4 días; la base central guarda la clave de origen de cada evento aplicado para impedir su doble aplicación. El consumidor acepta la versión vigente del sobre y la anterior. Las alarmas vigilan la edad del mensaje más antiguo, la profundidad por grupo y los mensajes fallidos.

**Evidencia exigida.** Prueba de corte de 24 h por sitio con drenaje completo sin pérdida ni duplicados, dentro de las 2 h comprometidas; prueba de mensajes duplicados, fuera de orden y de versión desconocida.

<a id="sub:adr-06"></a>
## 4.4.6 ADR-06 · Identidad híbrida (Modelo B)

**Decisión adoptada.** Keycloak IdP maestro en AWS (ECS Fargate, 2 tareas Multi-AZ, backend Aurora) + caché local solo lectura (TTL 24 h, igual a la autonomía del CD) en Talca, Concepción y los cross-docking, con un verificador local en el mismo nodo que, en cada relevo de turno sin enlace, valida el manifiesto de turno firmado por Keycloak y un segundo factor local: el PIN personal sobre el terminal enrolado por MDM. Con enlace, Keycloak renueva el manifiesto al menos cada hora para una ventana de 26 h, de modo que un corte iniciado justo antes de una renovación conserva al menos 25 h de verificación local. La caché de 24 h y la credencial de turno cumplen propósitos distintos: la caché conserva los datos de identidad y de turno recibidos y no emite sesiones, mientras que la credencial de turno —hasta 8 h en bodega y 14 h en reparto— limita cuánto dura el acceso de una persona; así, un corte de 24 h cubre dos relevos en bodega, cada uno habilitado por el verificador. Durante el corte no se promete revocación remota inmediata. El backend Laravel valida los JWT OIDC de Keycloak —firma con las claves publicadas, emisor, audiencia, vencimiento y alcance— y aplica políticas por recurso, turno, ruta, sitio y empresa; no se incorpora Sanctum ni Passport como segundo emisor de identidades. OTP para conductores externos.

**Alternativas descartadas:**

- *IdP solo nube*: paraliza bodega ante corte.
- *AD maestro local*: duplica administración, crea maestro a promover en DR.
- *Keycloak maestro local*: nube no puede autenticar si el enlace cae.

**Criterio de selección.** Autonomía offline sin maestro local a promover; autoridad única en nube; OTP sin correo para externos; autenticación multifactor; operado por el equipo reducido del CLIENTE sin directorio propietario.

<a id="sub:adr-07"></a>
## 4.4.7 ADR-07 · Movilidad de terreno

**Decisión adoptada.** App nativa Android Kotlin para preventa, reparto y picking. SQLite/Room, SDK Zebra DataWedge (GS1 + QR), impresión BT (ZQ620), POS PAX. Dispositivos Rugged: EC55, TC58e, MC9400 Cold Storage.

**Alternativas descartadas:** *PWA*: no controla SDK Zebra de forma fiable ni persiste turno completo sin capa nativa; *Híbrida Flutter*: runtime intermedio degrada interacción con periféricos industriales.

**Criterio de selección.** Control nativo de periféricos (DataWedge intents); offline total 14 h con sincro $<$ 10 min; UI para guantes -22 °C, una mano, lluvia; curva de aprendizaje ≤ 2 h; un artefacto para 3 perfiles.

<a id="sub:adr-08"></a>
## 4.4.8 ADR-08 · Destino del WMS legado 2013

**Decisión adoptada.** Reemplazo total en Etapa 1 por módulo WMS del monolito: Talca maestro, Concepción edge, cross-docks sobre E-01. Migración por dominio, oleadas por sitio, reversión azul-verde. Durante la coexistencia cada operación tiene un único escritor autorizado, de modo que el WMS de 2013 y el nuevo nunca escriben a la vez stock, cobros o documentos tributarios; la reversión devuelve el tráfico al escritor anterior solo tras detener el nuevo y conciliar los pendientes.

**Alternativas descartadas:** *Mantener e integrar*: proveedor desaparecido, sin soporte; no soporta multi-sitio, picking FEFO (primero en expirar, primero en salir), SSCC GS1 ni conteo cíclico ciego; *Extender a otros sitios*: arrastra riesgo de soporte inexistente en ventana crítica.

**Criterio de selección.** Funciones de bodega que el WMS de 2013 no contempla; riesgo operacional inaceptable; TCO amortizado con reducción conteo 2,3 %→0,3 % y merma 1,7 %→$<$1 %; reversión azul-verde garantizada.

<a id="sub:adr-09"></a>
## 4.4.9 ADR-09 · Estrategia DR

**Decisión adoptada.** Activo-pasivo warm standby multi-región: DMS CDC desde VM-02 de Talca hacia Aurora y Aurora Global Database hacia us-east-1; los demás sitios sincronizan eventos por colas. DRP local Talca→Concepción (RTO +1–2 h); pruebas 2×/año; respaldo 3-2-1-1-0 con S3 Object Lock.

**Alternativas descartadas:**

- *Activo-activo*: duplica infraestructura y exige reconciliación de doble escritura sin beneficio medible.
- *Backup + restore frío*: exige reconstruir la plataforma y restaurar los datos antes de operar, lo que no es compatible con el RTO de 4 h.
- *Solo intrarregional*: degrada el objetivo de continuidad, porque ante la caída de la región la recuperación dependería de reconstruir la plataforma desde respaldos; se descarta y la recuperación en us-east-1 queda declarada de forma incondicional.

**Criterio de selección.** RTO ≤ 4 h / RPO ≤ 15 min; proporcionalidad al volumen; DR de identidad resuelto en nube; pruebas semestrales reales.

<a id="sub:adr-10"></a>
## 4.4.10 ADR-10 · Almacenamiento on-premise y RAID

**Decisión adoptada.** RAID 10 NVMe en los nodos del clúster de Talca y RAID 10 sobre las cuatro bahías del servidor de Concepción; RAID 6 en el NAS de respaldo local D-05; la evidencia de entrega vive en S3; clúster Proxmox VE con almacenamiento Ceph en N+1.

**Alternativas descartadas:** *RAID 5*: probabilidad de URE durante rebuild en discos 8–16 TB; solo tolera 1 fallo; *RAID 1 puro para todo*: sobre-costo 50 % aplicado a datos no críticos sin beneficio proporcional.

**Criterio de selección.** IOPS deterministas en ventana de despacho ($>$100 K vs. 840 necesarios); tolerancia a fallo de disco con justificación; TCO contenido con RAID 10 solo en lo transaccional.

<a id="sub:adr-11"></a>
## 4.4.11 ADR-11 · Integración B2B/EDI canal moderno

**Decisión adoptada.** Hub EDI centralizado GS1 (EANCOM/GS1 XML + EPCIS) en nube, con conector configurable por cadena, equivalencias GTIN, bandeja de excepciones y ACL hacia ERP/GDE; la transformación y las reglas corren en el perfil EDI de Laravel. Canal moderno operativo ≤ enero 2029. El transporte AS2 usa OpenAS2, de licencia BSD, corre en un contenedor propio de ECS Fargate tras un Network Load Balancer con paso TLS directo en TCP 443: TLS 1.3 termina en el contenedor. El grupo de seguridad admite solo las IP registradas de cada cadena; el transporte firma y cifra mensajes, administra certificados por cadena y acuses MDN, y entrega al perfil EDI por contrato versionado. Los certificados se guardan en Secrets Manager (sección [4.4.15](14_m_decisiones_adr.md#sub:adr-15)).

**Alternativas descartadas:**

- *Punto a punto por cadena*: multiplica adaptadores y su mantenimiento.
- *EDI delegado al ERP*: expone una frontera frágil y permite escritura directa desde la cadena, contra Zero Trust.
- *AWS Transfer Family*: su servidor AS2 recibe por HTTP en TCP 5080 y no satisface TLS 1.3 en tránsito (RT-11.08; Bases Técnicas Transversales, Cap. 11, p. 23).
- *Biblioteca PHP para AS2*: carece de implementación validada con las cadenas.

**Criterio de selección.** Estandarización GS1, esfuerzo marginal por cadena nueva, aislamiento del ERP por la ACL, TLS 1.3 verificable y plazo de enero de 2029; el contenedor propio es la excepción a la preferencia por servicios administrados (RT-03.05; Bases Técnicas Transversales, Cap. 3, p. 8) necesaria para cumplir RT-11.08 (Bases Técnicas Transversales, Cap. 11, p. 23).

**Evidencia exigida.** Prueba de interoperabilidad por cadena con TLS 1.3, firma, cifrado, certificado y MDN antes de habilitarla.

<a id="sub:adr-12"></a>
## 4.4.12 ADR-12 · Absorción del peak de septiembre

**Decisión adoptada.** El cómputo elástico escala de forma independiente por perfil:

- API con PHP-FPM: de 2 a 4 tareas en el peak y techo de 8, por procesos ocupados sobre 70 %.
- Consumidor de reconciliación: de 2 a 4 tareas, por la edad del mensaje más antiguo.
- Trabajos: de 2 a 4 tareas, por la profundidad de cada cola, con `erp-sync` fijo en 2 procesos para no saturar el ERP.
- Planificador: una sola tarea.

Escala de forma predictiva y reactiva el cómputo elástico. Aurora pasa de large a xlarge (escritor en sa-east-1a y un lector promovible en sa-east-1b), y DynamoDB opera bajo demanda. La capacidad *Base* se contrata mediante Savings Plans y el peak se cubre con cómputo efímero.

**Alternativas descartadas:**

- *Capacidad fija al peak*: paga 12 meses la capacidad de 3 semanas.
- *Solo escala reactiva*: el peak de septiembre es predecible y la reactiva sola introduce retardo en la ventana crítica.
- *Trasladar las cifras del backend anterior (6 tareas de aplicación y 4 de workers Celery)*: eran supuestos de otro runtime y no valen para PHP-FPM.

**Criterio de selección.** Perfil no plano al peak ×1,5; cuello de botella identificado; FinOps: base reservada y peak efímero; congelamiento del 1 al 25 de septiembre y de diciembre.

**Consecuencias.** El número de tareas se deriva de dos supuestos declarados en el dimensionamiento —50 ms de CPU y 150 ms de residencia por solicitud— y no de una medición; las conexiones a PostgreSQL quedan acotadas por el número de procesos de cada perfil.

**Evidencia exigida.** Prueba de carga en Preproducción que mida el consumo real por solicitud y por sobre, la saturación de PHP-FPM, las conexiones, la edad de las colas y el rendimiento del ERP; si difieren de los supuestos, se recalculan tareas y procesos antes del paso a producción.

<a id="sub:adr-13"></a>
## 4.4.13 ADR-13 · Puerta de enlace de servicios

**Decisión adoptada.** Amazon API Gateway aloja dos API REST. La regional pública solo admite CloudFront: este agrega un encabezado de origen secreto exigido por el WAF regional y el endpoint predeterminado execute-api está deshabilitado. La privada solo admite el endpoint de interfaz execute-api de la VPC de Producción mediante política `aws:SourceVpce`. En las rutas protegidas, ambas usan la única función Lambda como autorizador de JWT de Keycloak (firma con claves publicadas, emisor, audiencia y vencimiento), modelos de validación de solicitud, planes de uso con cuotas y límites de tasa, inspección WAF e integración privada por VPC Link hacia el ALB privado. Laravel valida reglas de negocio y autorización por recurso; cada sitio mantiene la puerta de API local del WMS.

**Alternativas descartadas:**

- *Kong autoadministrado*: agrega un componente crítico que parchar en la ruta de la venta.
- *HTTP API con autorizador JWT nativo*: no ofrece API privada ni validación de modelos de solicitud.
- *Validación del token solo en Laravel*: la puerta no autentica e incumple RT-11.11 (Bases Técnicas Transversales, Cap. 11, p. 23).

**Criterio de selección.** Autenticación y validación en la puerta, separación de entradas pública y privada y acceso restringido al origen.

**Evidencia exigida.** Prueba de acceso directo denegado al origen público y a la API privada fuera del endpoint autorizado.

<a id="sub:adr-14"></a>
## 4.4.14 ADR-14 · Plataforma de observabilidad

**Decisión adoptada.** Plataforma única en nube: instrumentación con OpenTelemetry para PHP y Laravel y para las aplicaciones Kotlin, con el `transaction_id` propagado por HTTP, RabbitMQ, SQS y la capa anticorrupción; métricas propias por perfil (procesos PHP-FPM ocupados, reinicios, profundidad y edad de cola por grupo, mensajes fallidos, latencia del ERP y de escritura de VM-02); colectores ADOT on-premise con buffer 24 h, logs en CloudWatch Logs (12+24 m), métricas en CloudWatch Metrics (13 meses) y trazas en CloudWatch con retención declarada. Tableros nativos de CloudWatch para operación.

**Alternativas descartadas:** *Prometheus+Grafana+Loki local + cloud*: dos plataformas, cuando las Bases piden una sola; VM-06 sin capacidad; *AMP + X-Ray + Grafana*: cuatro servicios de observabilidad para un equipo de 4 personas; complejidad operativa desproporcionada sin ganancia funcional sobre CloudWatch nativo.

**Criterio de selección.** Las Bases piden una sola plataforma de observabilidad; buffer ADOT resuelve «sin puntos ciegos» durante corte; ninguna decisión 05:30–07:00 depende de tablero; CloudWatch es nativo de AWS y no requiere infraestructura adicional; el equipo del CLIENTE no opera servidores de observabilidad.

<a id="sub:adr-15"></a>
## 4.4.15 ADR-15 · Gestión de secretos

**Decisión adoptada.** AWS Secrets Manager (secretos con rotación: ERP, SII, Transbank, certificados AS2/EDI) + SSM Parameter Store (config no sensible). Consumo outbound por VPC Endpoint. Cifrado CMK KMS, separación de funciones. Cuenta de último recurso con credenciales en sobre sellado fuera de línea.

**Alternativas descartadas:** *HashiCorp Vault autoadministrado*: modo sellado tras reinicio exige intervención humana de madrugada; agrega infraestructura; *Sin gestor centralizado*: las Bases lo prohíben.

**Criterio de selección.** Servicio administrado sin desellado manual; Zero Trust (consumo outbound); separación de funciones vía IAM y CloudTrail; contingencia offline independiente de la nube.

<a id="sub:adr-16"></a>
## 4.4.16 ADR-16 · Acceso de personas internas y remotas

**Decisión adoptada.** AWS Verified Access protege por aplicación las consolas internas y la administración de Keycloak para oficina y trabajo remoto. Usa Keycloak con MFA como proveedor de confianza OIDC de usuario y CrowdStrike Falcon (F-03) como proveedor de postura de dispositivo; AWS WAF se asocia a la instancia. Su destino es el ALB privado del frontend Angular en Fargate, que reenvía llamadas a la API REST privada por el endpoint execute-api.

**Alternativas descartadas:** *Client VPN*: concede acceso de red y requiere un manejador de conexión adicional para verificar postura; *Solo VPN de sitio*: no cubre el trabajo remoto de RT-03.22 (Bases Técnicas Transversales, Cap. 3, p. 10) y confía en la ubicación de red.

**Criterio de selección.** Acceso por aplicación con identidad, MFA y postura para ambos orígenes, conforme a RT-03.22 (Bases Técnicas Transversales, Cap. 3, p. 10), RT-11.01 (Bases Técnicas Transversales, Cap. 11, p. 23) y RT-12.03 (Bases Técnicas Transversales, Cap. 12, p. 25).

**Evidencia exigida.** Pruebas de acceso con MFA y postura válida e inválida desde oficina y trabajo remoto.
