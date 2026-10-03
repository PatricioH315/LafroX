# Correcciones de coherencia — 2026-10-02

Documento interno (no se entrega). Complementa `DECISIONES_COHERENCIA.md` (D1–D12). Las decisiones D13–D29 mandan sobre cualquier texto anterior.

## Reglas generales para quien edite

- **PROHIBIDO tocar imágenes**: no editar, crear, regenerar ni exportar nada en `04/figuras/` ni ningún `.drawio`, `.png` o `.pdf` de figura. Si un texto queda distinto de una figura, NO tocar la figura: anotarlo en el informe final.
- Español formal, sin marcas de asistente, sin «pendiente», «borrador», «por indicación del usuario», etc.
- Tablas del cuerpo (`04/partes/`): una oración por celda, máx. 5 columnas. Anexos y formulario: libres pero legibles.
- Escapar `%`, `_`, `&` en LaTeX. Archivos UTF-8 con LF.
- Citas a las Bases en el cuerpo y anexos: estilo APA ya vigente, p. ej. «RT-08.04 (PUCV, 2026b, cap. 8, p. 18)». PUCV 2026a = caso (`Bases/Caso_02_Logistica.md`), 2026b = Bases Técnicas Transversales (`Bases/Bases_Tecnicas_Transversales.md`), 2026c = Bases Administrativas.
- No cambiar cifras salvo las indicadas aquí. Las cifras salen de `Dimensionamiento/dimensionamiento/resultados.md`.
- Los anexos se renombrarán después (lo hace Claude). **No renombres** «Anexo 4.1-X» ni «Anexo 4.2-A» en esta pasada.

## Decisiones

**D13 Starlink.** En Talca y Concepción Starlink es el **tercer camino en espera caliente**: está encendido, con el túnel IPsec establecido y BGP con menor preferencia. Toma el tráfico solo si fallan fibra y LTE, y entonces prioriza por calidad de servicio DMS/WAL de Talca, la salida del broker y outbox, las guías hacia el ERP y el SII, la identidad y la telemetría crítica. Se mantiene encendido porque un terminal apagado tarda minutos en adquirir satélites y el túnel tendría que negociarse en plena falla; el plan es de tarifa plana, así que estar encendido no agrega costo. En los cross-docking Starlink es el **camino principal**, con LTE de dos proveedores como respaldo. Reemplazar en todas partes «tercer camino activo», «activo y priorizado» y «satélite activo» por esta formulación. ADR-02 (resumen 4.1.11: «Fibra, LTE y satélite en espera caliente en los CD.») y su ficha en Anexo O.

**D14 Ley 21.719.** Solo se contempla el caso en que el CLIENTE no apruebe Estados Unidos, por estar fuera de Sudamérica. En ese caso, la región secundaria, que es un parámetro de la infraestructura como código, se cambia a otra región AWS que el CLIENTE apruebe y que ofrezca Aurora Global Database, DynamoDB Global Tables, replicación de S3, ECS Fargate y AWS Backup; se conservan la arquitectura, el RTO y el RPO. No mencionar un rechazo de Brasil. Se puede conservar la frase sobre categorías no críticas restringidas a la región primaria. Aplicar en 4.3.2 (`06_e`) y en ADR-19 del Anexo O.

**D15 Despacho y guía (RT-10.05: indisponibilidad cero 05:30–07:00).** Los camiones salen con la guía preemitida al cerrar la carga nocturna, sin depender de Internet. Un cambio de carga dentro de la ventana invalida la guía; la nueva se emite por cualquiera de los tres caminos de Talca y Concepción. Si fallan los tres a la vez, el camión sale con la carga que ampara su guía vigente y el ajuste pasa a la ruta siguiente; ningún camión sale sin guía válida. Corregir:
- 4.2 `02_0` («Internet no interviene…»);
- 4.2 `02_c` («Ninguna de estas fallas detiene…»): matizar sin contradecir 4.1;
- 4.1 `18_…` (último párrafo de «Control de liberación»): añadir la salida con la carga amparada.

**D16 Criticidad.** En `11_j`, la emisión de la guía de despacho de la ventana 05:30–07:00 pasa al nivel Crítico. Los demás DTE y la integración con el ERP quedan en Alto.

**D17 Región secundaria sin dependencia de la primaria.**
- ECR replica las imágenes a us-east-1 mediante la replicación entre regiones del registro.
- En us-east-1 existen, creadas por la infraestructura como código y vacías, las colas SQS FIFO, SQS y SNS equivalentes.
- El paso 8 de la conmutación redirige los shippers y erp-sync a esas colas.
- Reflejarlo en la tabla de servicios de `02_b`, la frase de `11_j` sobre la réplica reducida y el registro de imágenes, el paso 8 de `06_e` y las filas N-04 y N-09 del T-11.

**D18 Aurora.** Su capacidad es fija, dimensionada para 3× (ADR-12), y no escala automáticamente. En la tabla de fallas de `02_c`, la fila del peak de septiembre dice que Fargate escala de forma automática por perfil y que Aurora ya está dimensionada para 3× sin cambio de instancia.

**D19 ADR.**
- Cada cita «ADR-xx» debe corresponder al tema de su ficha: 01 estilo; 02 WAN; 03 híbrido/topología; 04 persistencia; 05 mensajería; 06 identidad; 07 movilidad; 08 WMS 2013; 09 DR; 10 Proxmox/Ceph; 11 EDI; 12 capacidad/peak; 13 puertas de enlace; 14 observabilidad; 15 secretos; 16 acceso de personas; 17 guías/erp-sync; 18 protección fuera del sitio/RPO; 19 residencia/regiones; 20 frontend; 21 IaC/cadena; 22 frío en borde.
- Corregir la identidad de contingencia: ADR-15 → ADR-06.
- ADR-12 y la fila N-04 del T-11: la API usa 2 a 4 tareas en el caso base y 7 en la sensibilidad de 91,70 solicitudes/s, ambas bajo el techo de 8.
- ADR-13: incluye la puerta de API local de cada sitio (A-01), que valida esquema, tasa, UUID, permisos y auditoría sin WAN.
- T-11 «Configuración»: «Ansible y Terraform con CDK» → «Terraform y Ansible», porque ADR-21 descarta CDK.

**D20 INT-12.** Los 12.602/23.404 cambios diarios son una **cota conservadora** calculada sobre los movimientos de todos los sitios, no un conteo propio de Talca. Rotularlo así en el Anexo G y en la memoria.

**D21 Rutas de la guía.**
- Talca: M5 → RabbitMQ local de Talca → erp-sync en VM-04 (sin WAN).
- Concepción y cross-docking: RabbitMQ local → shipper → SQS FIFO → erp-sync, que la consume por conexión saliente.
- La prueba de las 96 guías del Anexo M debe cubrir y comprobar ambas rutas.

**D22 Pruebas.** El cambio de carga con nueva guía se ensaya en AL-DTE-01. AL-OFF-01 cubre el despacho con guía válida preemitida, y el cuerpo de 4.1 (`16_…`) remite el cambio de carga a AL-DTE-01.

**D23 Picos.** El máximo horario global de septiembre es 14,66 TPS a las 12:00, con preventa y portal. El máximo dentro de la ventana de despacho 05:30–07:00 es 6,94 TPS. En 4.1 `03_principios` y en la celda «Máximo horario con guías y re-despacho» de `12_k` hay que distinguir ambos.

**D24 Dotación.** En `12_k` (dimensión 16) y en la memoria, explicitar:
- a 42 h: 15 personas normal y 17 en septiembre/diciembre;
- desde el 26-04-2028, a 40 h: 17 personas normal y 19 en peak.

Verificar las cifras con la memoria y `resultados.md` antes de escribir. Si no calzan, NO escribir y reportarlo.

**D25 T-11.**
- (a) Módulos de temperatura con dos fuentes en circuitos distintos.
- (b) Cantidades por región:
  - Aurora: 1 base global con clúster primario en sa-east-1 y secundario en us-east-1.
  - DynamoDB: 2 tablas, temperatura como Global Table en ambas regiones y posiciones solo en sa-east-1.
  - API Gateway y Verified Access: producción en sa-east-1 y réplica reducida en us-east-1.
  - VPN: 2 túneles por sitio y región, es decir, 10 hacia sa-east-1 y 10 preparados hacia us-east-1. Las dos filas de VPN deben remitirse entre sí y no contar doble.
- (c) Las filas de NAS, switches, firewalls y KVM declaran la potencia de placa usada en la Tabla 4.3-1 (`05_d`), con los mismos valores, para que 4.3 sea trazable.
- (d) Repuesto compartido: núcleo de Concepción = **Cisco Catalyst 9300-48P o equivalente**, igual que Talca. Firewalls de ambos CD = mismo modelo, **FortiGate 100F o equivalente**, con doble fuente; así la reserva común es intercambiable.
- (e) Nueva fila «Medio de respaldo físico rotativo», coherente con `11_j`: medio cifrado con rotación semanal hacia custodia externa; cantidad 2 (uno en sitio y uno en custodia) más el servicio de custodia.
- (f) Códigos: la fila «Aplicación» lleva A-01 y la fila «Configuración» lleva F-02.
- (g) Cableado: «Distribución horizontal» = paneles y terminaciones; «Piso técnico y cableado» = recorridos y piso técnico. La certificación por enlace se menciona una sola vez.
- (h) RT:
  - RT-06.10 solo para la revisión y medición semestral; la prueba mensual del generador es un compromiso adicional sin esa cita, y el PUE se cita con el RT que corresponda.
  - RT-06.32 = dos ingresos al **edificio** por puntos separados con ductos independientes hasta la sala, también en `05_d`.
  - RT-08.12 para el terminal de congelado MC9400: IP65 e IP68 y caídas de 3 m sobre concreto según la ficha del fabricante.
  - RT-08.13 se retira de la fila Starlink.
- (i) Citas del T-11 en estilo APA «(PUCV, 2026b, cap. N, p. M)», con una sección «Referencias» breve al final del formulario que liste solo las obras citadas en él.
- (j) Comentarios obsoletos de `04/formulario_T11.tex`: las rutas `04_arquitectura_fisica/...` y la frase «también se incluye al final del subdocumento» son falsas; el T-11 es un archivo propio.

**D26 RPO por dominio (06_e, tabla de replicación).** Clasificar los dominios:
- **Críticos, RPO ≤ 15 min y medidos:** transaccional en nube, WMS de Talca, mensajes críticos, evidencias y documentos tributarios en S3, y telemetría de temperatura.
- **No críticos, ≤ 24 h:** analítica, posiciones de flota y mensajes no críticos.

Garantías y medición:
- S3 usa Replication Time Control: 99,99 % de los objetos en 15 min, métrica de objetos pendientes y evento de umbral superado que dispara la recopia.
- DynamoDB Global Tables es asíncrona con retraso típico de segundos y alarma de ReplicationLatency a 60 s.
- Todo se mide en los ensayos semestrales.

Una oración por celda.

**D27 RTO.**
- El paso 2 (decisión del CLIENTE) tiene un máximo de 30 min. El plan de continuidad designa un autorizador titular y uno suplente del CLIENTE con facultad delegada. Si el titular no responde en 15 min, decide el suplente.
- Peor caso secuencial: 5 + 30 + 20 + 30 + 15 + 15 + 5 + 15 = 2 h 15 min, dentro de 4 h.
- La decisión se ensaya en los simulacros semestrales.
- Actualizar la tabla y el párrafo posterior de `06_e`.

**D28 Servicios singulares.**
- Transporte AS2 y frontend de consolas: 2 tareas en 2 zonas cada uno (RT-03.02).
- Motor de rutas: tarea por corrida. Si falla, ECS la relanza en otra zona y la corrida se repite dentro de la planificación de 15:00 a 18:30. La prueba de aceptación mide el plazo de 20 min por corrida.
- Reflejarlo en el T-11 y donde 4.2 describa estos servicios. Si la memoria cuenta tareas Fargate en su capacidad, reportarlo y no cambiar cifras.

**D29 Auditoría de RT.** En cada archivo asignado, verificar cada cita «RT-xx.yy» contra su texto en `Bases/Bases_Tecnicas_Transversales.md` y en la tabla de parámetros del caso (`Bases/Caso_02_Logistica.md`, que redefine algunos RT). La afirmación citada debe ser lo que el RT exige o algo que lo cumple. Si no calza, corregir la cita (cambiar al RT correcto o quitarla) o la afirmación. Verificar también capítulo y página cuando se den.

**D30 Autoatención del cliente (RT-16.30 y RT-17.01 del caso; restricción 5).** El Portal de Clientes (N-01, Angular) permite pedir en autoservicio y consultar el estado de entrega, los documentos y el saldo. Se publica además como aplicación web progresiva instalable, que es el perfil de autoatención con operación desconectada: sin señal muestra el catálogo y los precios descargados y arma el pedido, que queda en cola con UUID y se envía por /sync/v1. M3 es el dueño único del pedido en sus tres canales (preventista, autoatención y M11). La cuenta la activa el preventista con un código SMS. El canal es opcional. No va en la app Kotlin, que es de trabajadores (MDM y turnos). Prueba AL-CLI-01; decisión en ADR-20.
