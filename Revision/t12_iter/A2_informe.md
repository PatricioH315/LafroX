# Informe del Formulario T-12 — Lote A2

## 1. Cambios de estado respecto del T-12 de origen

El lote contiene 135 filas: 94 Cumple, 34 Cumple parcialmente y 7 No cumple.

| ID | Estado de origen → final | Cambio y fundamento |
|---|---|---|
| RF-07.11 | Cumple parcialmente → No cumple | El Anexo 3.A declara que esta función no se oferta de forma independiente; M7 cubre cobranza y rendición de pagos del reparto. SD3-Anexos 3.A, Tabla 3.A.3a; SD4 4.1.4.6 y Anexo 4-E, Tabla A.6. |
| RF-10.01 | Cumple parcialmente → Cumple | M2 asigna la sugerencia de reposición por SKU/proveedor y su traspaso por INT-06; SD5 modela inventario y ventas. SD4 4.1.4.3, Anexos 4-D/4-E, Tablas A.5/A.6; SD5 5.1.4. |
| RF-10.02 | Cumple parcialmente → Cumple | M2 incorpora promociones comprometidas al cálculo de reposición; la familia tiene módulo y soporte de datos. SD4 4.1.4.3, Anexos 4-D/4-E, Tablas A.5/A.6; SD5 5.1.4. |
| RF-14.03-BTT | Cumple → Cumple parcialmente | La Tabla 19 enumera servicios, puertos y controles, pero no informa los FQDN efectivos. SD4 4.2.5.2, Tabla 19. |
| RF-14.04-BTT | Cumple parcialmente → Cumple | T-14 define clasificación, escalamiento, plazos, responsables y aviso crítico al CLIENTE dentro de 2 h. T-14 cuentas 2.2.3 y 8.1.5; SD4-Anexos 4-R, Tabla A.23. |
| RF-16.03 | Cumple parcialmente → Cumple | El componente CloudWatch cubre alertas por síntoma, ventanas y criticidad; T-15 desarrolla cobertura y turnos. Los parámetros detallados del alertamiento corresponden al requerimiento y su verificación en ejecución. SD4 4.1.3.8; SD4-Anexos 4-W.7; T-15 5.7. |
| RF-16.04 | No cumple → Cumple parcialmente | SD1 compromete postmortem aprobado y publicado para incidentes P1/P2, pero no el plazo de 5 días hábiles ni el seguimiento hasta cierre. SD1 1.3.3. |
| RF-17.06 | No cumple → Cumple parcialmente | Hay flujos acotados de excepciones con estados, responsables y aprobaciones; falta un motor configurable por el CLIENTE con vencimiento y delegación. SD4 4.1.3.5 y Anexo 4-B. |
| RF-17.08 | No cumple → Cumple parcialmente | S3_DOCS aporta versionado, permisos, cifrado e integridad; faltan búsqueda por contenido/metadatos y vista previa. SD4-Anexos 4-N, DAT-OBJ; SD5 5.2.7. |
| RF-18.01 | No cumple → Cumple parcialmente | M6 y el Anexo 4-U describen POD y acuse, pero no firma avanzada, validación de certificado ni sello de tiempo. SD4 4.1.17.1 y Anexo 4-U. |
| RF-18.03 | Cumple → Cumple parcialmente | INT-11 incluye envío asíncrono, reintentos e idempotencia; el modelo conserva entrega/error, no apertura por mensaje. SD4-Anexos 4-H, INT-11; SD5-Anexos 5-A. |
| RF-19.03 | Cumple → Cumple parcialmente | La Tabla 19 no contiene los nombres DNS/FQDN finales, igual que RF-14.03-BTT. SD4 4.2.5.2, Tabla 19. |
| RF-19.04 | Cumple parcialmente → Cumple | T-14 acredita plan, responsables, escalamiento y aviso crítico dentro de 2 h, en línea con RF-14.04-BTT. T-14 cuentas 2.2.3 y 8.1.5; SD4-Anexos 4-R, Tabla A.23. |
| RNF-05.02 | Cumple → Cumple parcialmente | El MC9400 Cold Storage Freezer soporta frío y uso con guantes; no se acreditan tamaño/gestos de controles ni una prueba de 30 min a −22 °C. T-11 C-03; SD4 4.2.1.2. |
| RNF-05.03 | Cumple → Cumple parcialmente | T-14 fija misión, error, tutoría y duración; no restringe la capacitación al recinto de bodega. T-14 cuenta 7.1.2; T-18 2.7. |
| RNF-09.05 | Cumple → Cumple parcialmente | El volumen permite calcular intervalos de 5 min y se registran lecturas faltantes, pero no se declara la parametrización por producto ni la detección de 2 °C/15 min. SD4 4.1.4.2 y Anexo 4-W.5; SD5 5.1.7; T-11 B-01/B-03. |
| RNF-12.03 | Cumple → Cumple parcialmente | INT-08 acredita el MDN técnico, que no es el acuse comercial ≤30 min desde descarga vinculado a la misma guía. SD4 4.1.17.1, Anexos 4-H, INT-08, y 4-U. |
| RNF-13.09 | Cumple → Cumple parcialmente | El diseño Wi-Fi es preliminar; falta el estudio dentro de las cámaras de frío sin señal y cerrar su solución. SD4 4.2.1.1; T-11, Red inalámbrica industrial. |
| RNF-14.01 | Cumple → Cumple parcialmente | Se describe TLS 1.3 y gestión de certificados, pero no cobertura integral, suites, HSTS con precarga ni alerta anticipada. SD4 4.1.3.7; SD4-Anexos 4-R, Tabla A.23. |
| RNF-14.08 | Cumple → Cumple parcialmente | Se genera SBOM CycloneDX/SPDX por liberación, sin compromiso de entrega al CLIENTE. SD4 4.1.9; SD4-Anexos 4-R, Tabla A.23, control 5.9. |
| RNF-16.01 | Cumple parcialmente → Cumple | La observabilidad OpenTelemetry/CloudWatch fija correlación y métricas; Anexo 4-T mide p95 sobre operaciones percibidas y confirmadas. SD4 4.1.3.8; SD4-Anexos 4-T. |
| RNF-16.03 | No cumple → Cumple parcialmente | Los registros tienen acceso controlado y auditado; falta eliminar o enmascarar datos personales sensibles y credenciales antes de su ingreso. SD4 4.1.3.7–4.1.3.8; SD5 5.2.2. |
| RNF-20.03 | Cumple parcialmente → Cumple | SD4 y T-14 incluyen plan ISO 22301, análisis de impacto, escenarios, respaldo manual y criterios de activación por proceso. SD4 4.1.10 y 4.2.4.6; T-14 cuenta 2.5.1. |
| RNF-21.06 | No cumple → Cumple | D-10 establece ticket único, clasificación de severidad, escalamiento L1/L2/L3 y seguimiento hasta cierre. SD3-Anexos 3.D, fila D-10. |
| RNF-22.03 | Cumple → Cumple parcialmente | Se programa por turnos, noche y rotación, pero no se cubren expresamente peaks y ventanas operacionales ni horarios acordados. T-14 cuentas 7.1.1–7.1.2; T-18 2.7; SD7 7.1.2. |
| RNF-23.02 | Cumple → Cumple parcialmente | T-11 solo declara IP/caída para algunos modelos; faltan datos verificables para el resto de terminales, periféricos y sensores. T-11 C-01–C-05, B-01/B-03. |
| RNF-23.04 | Cumple → Cumple parcialmente | Se indican ocho estaciones con monitores duales y NCh 2527; administración/cifrado se describen para 184 equipos existentes, no para las nuevas. T-11, Estación de trabajo. |

## 2. Cambios respecto de la salida previa

| ID | Estado previo → final | Fundamento y evidencia |
|---|---|---|
| RF-07.11 | Cumple parcialmente → No cumple | El catálogo excluye la oferta independiente y M7 no desarrolla cobro presencial de facturas por preventistas. SD3-Anexos 3.A, Tabla 3.A.3a; SD4 4.1.4.6 y Anexo 4-E, Tabla A.6. |
| RF-15.03 | Cumple parcialmente → Cumple | Keycloak 26.x aporta MFA/FIDO2 para administradores y AWS Verified Access protege accesos externos a consola con MFA; el detalle de alcance se construye conforme al requisito. SD4 4.1.3.7 y 4.2.2.4; SD4-Anexos 4-R, Tabla A.23; T-11, AWS Verified Access. |
| RF-16.03 | Cumple parcialmente → Cumple | CloudWatch cubre alertas de síntomas/ventanas/criticidad y T-15 declara turnos; agrupación, supresión y escalamiento forman parte de la función comprometida y verificable. SD4 4.1.3.8; SD4-Anexos 4-W.7; T-15 5.7. |
| RF-17.02 | Cumple → Cumple parcialmente | El modelo versionado y M9 acreditan almacenamiento de parámetros y la regla térmica por producto; falta el módulo e interfaz para administrar el conjunto general de reglas desde el CLIENTE. SD4 4.1.3.1 y 4.1.4.2; SD5-Anexos 5-A. |
| RF-17.05 | Cumple → No cumple | La propuesta acredita el registro en gob_auditoria, pero no el módulo e interfaz de consulta y exportación para el CLIENTE. SD4 4.1.3.1/4.1.3.7; SD5 5.2.2 y Anexos 5-A. |
| RF-17.10 | Cumple → Cumple parcialmente | INT-11 y not_plantilla sustentan el envío y el modelo de plantillas; falta la interfaz de administración por el CLIENTE. SD4 4.1.3.1; SD4-Anexos 4-H/4-I; SD5-Anexos 5-A. |
| RF-17.12 | Cumple → No cumple | Anexo 4-C y SD5 describen exportación analítica/regulatoria, pero no un módulo responsable de listados ordenables, filtrables y paginados. SD4-Anexos 4-C; SD5 5.2.6 y 5.2.8. |
| RF-17.13 | Cumple parcialmente → Cumple | S3/CloudFront soporta el portal público sin autenticación y T-14 fija WCAG 2.2 AA para la prueba de accesibilidad; contenido y controles visuales quedan en el compromiso funcional. SD4 4.1.3.1/4.2.5.2; T-14 cuentas 3.8.2 y 3.9.2. |
| RNF-14.06 | Cumple parcialmente → Cumple | T-14 compromete pentest independiente antes de H5/H10 y una prueba anual durante Operación; SD1 declara frecuencia semestral, más exigente que el mínimo anual. T-14 filas 3.8.6/3.9.5 y cuenta 8.2.2; SD1 1.3.2. |
| RNF-21.03 | Cumple parcialmente → Cumple | T-15 5.6 compromete medición de atención, abandono y resolución al primer contacto, calibración Erlang A y ajuste de capacidad; los tres umbrales se siguen por contacto. T-15 5.6; SD4 4.2.6.10 y Anexos 4-W.7. |

### Ajustes de componente, cifra y referencia

- Se corrigió RNF-21.01 a 8 personas totales para NOC y SOC, 4 por puesto; desde el 26-04-2028 son 10 totales, 5 por puesto, según SD4-Anexos 4-W.7 y T-15 4.1/5.7.
- RF-13.03 conserva ADR-01 a ADR-22, conforme a SD4 4.1.11 y Anexos 4-O, Tabla A.17.
- RF-15.01 identifica Keycloak 26.x y OIDC/SAML declarados; registra como faltantes OAuth 2.1 y el directorio corporativo del CLIENTE, no presupone esos conectores.
- RF-17.03 identifica cambiador/aprobador de mae_parametro_version y concreta la ausencia de justificación y aprobación obligatoria en SD5-Anexos 5-A.
- Los componentes de RF-02.11, RF-06.06, RF-06.14, RF-09.10, RNF-06.01, RNF-06.03, RNF-09.01 y RF-10.01–10.03 se enlazaron con SD4-Anexos 4-D/4-E; se añadió 3.J R18-03/R18-08 cuando aplica.
- Para las 37 filas parciales o no cumplidas, el campo de componente especifica la falta y cita el apartado donde el soporte no aparece. RF-19.01–19.05 conserva coherencia con RF-14.01-BTT–14.05-BTT.
- RNF-06.02 consigna los valores del caso por perfil: 24 h en bodega y 14 h en reparto/campo, con SD4 4.1.15/Anexo 4-J y SD5 5.1.4/5.1.6.
- RNF-09.05 conserva el cálculo del intervalo de 5 min: 288 lecturas/cámara/día y 174 por termógrafo en la ventana de 14,5 h de SD4-Anexos 4-W.5.
- RNF-11.03 y RNF-11.04 consignan cierre comercial en ≤2 h desde el retorno del último camión e indicadores en ≤4 h, conforme al Caso 02, cap. 15, SD4 4.1.4.7 y SD5 5.2.6.

## 3. Componentes sin versión en la propuesta

Las versiones que sí declara la propuesta se conservan literalmente: Angular 22.x, Keycloak 26.x, Laravel 13.x, PHP 8.5.x, PostgreSQL 16.x, RabbitMQ 4.x y AWS IoT Greengrass V2. No se agrega versión o modelo no escrito.

| Producto o componente | Filas afectadas | Lugar propuesto para declarar versión/modelo |
|---|---|---|
| Kotlin/Android y Room/SQLite (rama estable, sin número concreto) | RF-06.06, RF-06.14, RNF-03.01, RNF-03.03, RNF-06.01, RNF-06.02 | SD4-Anexos 4-P, Tabla A.19; T-11 C-01/C-02/C-03 para compatibilidad del terminal. |
| OpenAS2/JVM (rama soportada, sin versión concreta) | RNF-12.02, RNF-12.03 | SD4-Anexos 4-P, Tabla A.19; SD4-Anexos 4-H, INT-08. |
| SDK/colector OpenTelemetry y AWS Distro for OpenTelemetry (versiones estables, sin número concreto) | RF-16.01 | SD4-Anexos 4-P, Tabla A.19; SD4 4.1.3.8. |
| Ansible (versiones estables, sin versión concreta) | RNF-13.06 | SD4-Anexos 4-P, Tabla A.19; SD4 4.2.2.5 y T-11 F-02. |
| Proxmox VE y Ceph (sin versión concreta) | RNF-13.03, RNF-13.04, RNF-13.05 | SD4-Anexos 4-P, Tabla A.19; SD4 4.2.1.2 y T-11, plataforma on-premise. |
| ElastiCache for Redis y Aurora PostgreSQL (sin versión/engine concreto en la oferta) | RNF-03.02; RF-02.11 | SD4-Anexos 4-P, Tabla A.19; SD4 4.2.4.2 y 4.2.2.7, respectivamente. |
| CrowdStrike Falcon y GuardDuty Runtime Monitoring (sin versión de agente/servicio declarada) | RNF-14.05 | SD4-Anexos 4-P, Tabla A.19; SD4 4.2.3.1 y T-11 F-03. |
| PHPStan/Larastan, GitLab CI y AWS CodeBuild (sin número de versión) | RNF-14.07, RNF-14.09 | SD4-Anexos 4-P, Tablas A.19–A.20; SD4 4.1.9 y 4.1.7. |
| Servicios AWS sin versión de servicio/engine individualizada: CloudWatch, QuickSight, SNS, SQS FIFO, S3/Object Lock, CloudFront, KMS, Backup/Vault Lock, GuardDuty Runtime Monitoring, Verified Access, ECS Fargate, Redshift Serverless, ElastiCache for Redis y Aurora PostgreSQL | RF-06.06, RF-06.14, RF-15.03, RF-16.01, RF-16.02, RF-16.03, RF-17.08, RF-17.10, RF-17.13, RNF-01.02, RNF-03.02, RNF-04.01, RNF-07.01, RNF-07.02, RNF-11.02, RNF-14.02–14.05, RNF-16.03, RNF-17.01, RNF-17.03, RNF-19.02, RNF-20.07 | SD4-Anexos 4-P, Tabla A.19, con API/engine por servicio y versión de referencia al liberar; indicar también en la sección de cada servicio. |
| Puntos de acceso Wi-Fi 6E industrial (sin marca/modelo final) | RNF-13.09 | T-11, Red inalámbrica industrial, al cerrar estudio y dimensionamiento; SD4 4.2.1.1. |
| Ocho estaciones de trabajo nuevas (sin marca/modelo) | RNF-23.04 | T-11, Estación de trabajo. |

## 4. Declaraciones faltantes

| ID | Subdocumento y sección existente | Borrador |
|---|---|---|
| RF-07.11 | SD4 4.1.4.6; SD4-Anexos 4-E, Tabla A.6; SD5 5.1.8 | M7 incluirá el cobro presencial de facturas por preventistas, con captura individual y rendición vinculada a cada factura. Los medios de pago y reglas de conciliación se definirán con el CLIENTE. |
| RF-14.03-BTT | SD4 4.2.5.2, Tabla 19 | La Tabla 19 identifica para cada servicio alcanzable su FQDN definitivo, puerto, servicio y control de borde. FQDN por servicio: dato a definir por el equipo. |
| RF-14.05-BTT | T-14 cuenta 8.1.5; SD1 1.3.3 | Toda brecha se notificará al CLIENTE dentro de 24 horas con un informe preliminar. El análisis de causa raíz se entregará dentro de los cinco días hábiles siguientes, con acciones y plazos de remediación. |
| RF-15.01 | SD4 4.1.3.7; SD4-Anexos 4-O, ADR-06, y 4-P, Tabla A.19; T-11 A-05 | Keycloak 26.x centralizará la identidad y federará mediante OpenID Connect y OAuth 2.1; cuando la integración lo requiera, se habilitará SAML 2.0 y la conexión al directorio corporativo del CLIENTE por LDAP o equivalente en nube. |
| RF-16.04 | SD1 1.3.3 | Tras cada incidente crítico se emitirá el análisis de causa raíz dentro de cinco días hábiles. Cada acción correctiva tendrá responsable, seguimiento y evidencia hasta su cierre. |
| RF-17.01 | SD4 4.1.3.7; SD4-Anexos 4-N, Tabla A.16; SD5 5.1.3 | La consola permitirá al CLIENTE administrar personas, roles, permisos, unidades organizacionales y jerarquías sin intervención del ADJUDICATARIO. |
| RF-17.02 | SD4 4.1.3.1 y 4.1.4.2; SD5-Anexos 5-A | La consola del CLIENTE permitirá configurar umbrales, plazos, montos, tolerancias, catálogos, listas de valores y textos de notificación sin desarrollo. Cada cambio se almacenará como una versión con su valor, autor y fecha. |
| RF-17.05 | SD4 4.1.3.1; SD4-Anexos 4-D (Tabla A.5) y 4-E (Tabla A.6); SD5 5.2.2 y SD5-Anexos 5-A | El CLIENTE consultará desde la consola la auditoría por persona, período, entidad y tipo de operación, y exportará el resultado sin acceder a la base de datos. Las consultas y exportaciones conservarán actor y fecha en la auditoría. |
| RF-17.03 | SD4 4.1.4.2; SD5-Anexos 5-A | Todo cambio de parámetro operacional quedará pendiente hasta la aprobación de un segundo perfil. Se conservarán la justificación, el actor, la fecha y la versión de cada cambio. |
| RF-17.06 | SD4 4.1.3.5; SD4-Anexos 4-B | El CLIENTE configurará sin desarrollo los estados, transiciones, responsables, plazos y niveles de aprobación. El sistema escalará vencimientos y permitirá delegar tareas por ausencia. |
| RF-17.07 | SD4 4.1.3.5; SD4-Anexos 4-B | Cada persona usuaria tendrá una bandeja única con sus aprobaciones, revisiones y excepciones pendientes, priorizadas y con alerta de vencimiento. |
| RF-17.08 | SD4-Anexos 4-N, DAT-OBJ; SD5 5.2.7 | S3_DOCS permitirá buscar documentos por contenido y metadatos, y previsualizarlos sin descarga. Mantendrá versionado, permisos, cifrado e integridad verificable. |
| RF-17.09 | SD4 4.1.3.1; SD5 5.2.7 | La consola permitirá al CLIENTE administrar plantillas con datos de transacción y generar documentos en PDF, DOCX o XLSX. El módulo responsable y su soporte técnico quedan por definir por el equipo. |
| RF-17.10 | SD4 4.1.3.1; SD4-Anexos 4-H (INT-11); SD5-Anexos 5-A | El CLIENTE administrará las plantillas de notificación desde la consola, con publicación por correo electrónico, aviso en la aplicación y SMS o mensajería instantánea. |
| RF-17.11 | SD4 4.1.3.1; SD5 5.2.6 | La solución incorporará búsqueda global de texto completo, tolerancia a errores y filtros facetados, aplicando en cada resultado los permisos de la persona que consulta. El componente responsable queda por definir por el equipo. |
| RF-17.12 | SD4 4.1.3.1; SD4-Anexos 4-D (Tabla A.5) y 4-E (Tabla A.6); SD4-Anexos 4-C (Tabla A.4); SD5 5.2.6 y 5.2.8 | Las consolas presentarán listados ordenables, filtrables y paginados. La exportación en formato abierto conservará los filtros aplicados al listado. |
| RF-18.01 | SD4 4.1.17.1; SD4-Anexos 4-U | Para guías, acuses y contratos que lo requieran se aplicará firma electrónica avanzada conforme a la Ley 19.799. Se verificará el certificado, se generará sello de tiempo y se conservará la evidencia de firma. |
| RF-18.02 | SD4 4.1.3.1; SD5 5.1.9; SD5-Anexos 5-A | Cada persona usuaria podrá configurar canal y frecuencia de notificación. El sistema respetará las políticas obligatorias que defina el CLIENTE. |
| RF-18.03 | SD4-Anexos 4-H, INT-11; SD5 5.1.9 y Anexos 5-A | Cada mensaje conservará entrega, apertura o error, junto con sus reintentos y clave de idempotencia. |
| RF-19.03 | SD4 4.2.5.2, Tabla 19 | La Tabla 19 identifica para cada servicio alcanzable su FQDN definitivo, puerto, servicio y control de borde. FQDN por servicio: dato a definir por el equipo. |
| RF-19.05 | T-14 cuenta 8.1.5; SD1 1.3.3 | Toda brecha se notificará al CLIENTE dentro de 24 horas con un informe preliminar. El análisis de causa raíz se entregará dentro de los cinco días hábiles siguientes, con acciones y plazos de remediación. |
| RNF-05.02 | SD4 4.2.1.2; T-11 C-03; T-14 fila 3.8.3 | La interfaz de picking tendrá controles de al menos 15 × 15 mm y no requerirá gestos complejos. El terminal mantendrá operación durante 30 minutos continuos a −22 °C con guantes; se verificará en la prueba del perfil operacional. |
| RNF-05.03 | T-14 cuenta 7.1.2; T-18 2.7 | La capacitación asistida para la misión de picking se realizará dentro del recinto de bodega y no se programarán sesiones fuera de él. Se mantienen los umbrales de misión, error y duración comprometidos. |
| RNF-09.05 | SD4 4.1.4.2 y Anexos 4-W.5; SD5 5.1.7; T-11 B-01/B-03 | La frecuencia de captura será parametrizable por tipo de producto y permitirá identificar una desviación de 2 °C sostenida durante 15 minutos. Frecuencia por producto: dato a definir por el equipo; cada lectura ausente generará un evento. |
| RNF-12.03 | SD4 4.1.17.1; SD4-Anexos 4-H, INT-08, y 4-U | El acuse comercial de cada entrega se enviará dentro de 30 minutos desde la descarga y se asociará al aviso de despacho de la misma guía. El MDN técnico se conservará como acuse de transporte separado. |
| RNF-13.06 | SD4 4.2.2.5; SD4-Anexos 4-O, ADR-21; T-11 F-02 | Los sistemas on-premise se endurecerán según los CIS Benchmarks aplicables. La ventana de aplicación de parches y su reversión se acordarán con el CLIENTE antes de cada ciclo. |
| RNF-13.09 | SD4 4.2.1.1; T-11, Red inalámbrica industrial | Se ejecutará el estudio de cobertura en los centros, incluido el interior de las cámaras de refrigerado y congelado, y se implementará la solución resultante. Cantidad y modelos finales de puntos de acceso: datos a definir por el equipo tras el estudio. |
| RNF-14.01 | SD4 4.1.3.7; SD4-Anexos 4-R, Tabla A.23 | Todo el tráfico empleará TLS 1.3; se prohibirán TLS 1.0/1.1, se declararán suites modernas, se activará HSTS con precarga y se automatizarán emisión, rotación y alertas anticipadas de certificados. La lista concreta de suites queda por definir por el equipo. |
| RNF-14.08 | SD4 4.1.9; SD4-Anexos 4-R, Tabla A.23, control 5.9 | Cada versión liberada se acompañará de su SBOM CycloneDX o SPDX y se entregará al CLIENTE. |
| RNF-16.02 | SD4-Anexos 4-B; T-14 cuenta 8.1 | Se mantendrá un libro de operación y una guía de resolución para cada escenario de falla previsible. Las tareas repetitivas se automatizarán progresivamente con aprobación y evidencia. |
| RNF-16.03 | SD4 4.1.3.7 y 4.1.3.8; SD5 5.2.2 | Antes de almacenar registros, la solución eliminará o enmascarará datos personales sensibles y credenciales. El acceso continuará controlado por rol, auditado y trazable. |
| RNF-19.02 | SD4 4.2.4.1.1 y 4.2.6.9; Oferta Económica | Las capas de aplicación e integración escalarán horizontalmente con umbrales, límites y reacción declarados. El costo asociado se incorporará a la Oferta Económica; umbrales, límites y monto: datos a definir por el equipo. |
| RNF-21.01 | SD4-Anexos 4-W.7; T-15 4.1 y 5.7 | El NOC 24×7×365 tendrá ubicación, procedimientos y dotación por turno declarados. Ubicación y procedimientos concretos: datos a definir por el equipo. |
| RNF-21.02 | T-14 cuenta 8.1; T-15 5.7 | LafroX designará un gerente de servicio dedicado como contraparte permanente del CLIENTE durante Operación. La asignación nominal se definirá por el equipo. |
| RNF-21.07 | T-14 cuenta 8.1; T-15 5.7 | Los especialistas L2/L3 se trasladarán a Curicó, Chillán y Los Ángeles por el medio más rápido cuando sea necesario, sin reducir la atención de otros sitios. El costo del traslado se incluirá en la oferta; monto: dato a definir por el equipo. |
| RNF-21.08 | T-14 cuenta 8.2 | La bolsa anual de mantención evolutiva declarará horas por perfil y el procedimiento de solicitud, estimación, aprobación y liquidación. Horas por perfil: datos a definir por el equipo. |
| RNF-22.02 | T-14 cuentas 7.1.5 y 8.5.3 | Todo el material se entregará en español, en formato editable y como propiedad del CLIENTE, incluyendo manuales por perfil, guías rápidas, preguntas frecuentes, videos y base de conocimiento consultable. |
| RNF-22.03 | T-14 cuentas 7.1.1–7.1.2; T-18 2.7; SD7 7.1.2 | La capacitación se programará por turnos y horarios acordados sin afectar despacho matinal ni preparación nocturna, y se evitarán los peaks de septiembre y diciembre. El calendario se definirá con el CLIENTE. |
| RNF-23.01 | T-11 C-01–C-05, B-01/B-03 y Estación de trabajo | Cada equipo de terreno incluirá marca, modelo, cantidad, características, accesorios, consumibles y costo unitario estimado. Costos unitarios: datos a definir por el equipo. |
| RNF-23.02 | T-11 C-01–C-05 y B-01/B-03 | La ficha de cada modelo declarará IP y altura de caída, respaldados por ficha del fabricante y adecuados al entorno previsto. Los datos faltantes por modelo se definirán por el equipo antes de la oferta final. |
| RNF-23.04 | T-11, Estación de trabajo | Las ocho estaciones nuevas se identificarán por marca y modelo y tendrán dos monitores, ergonomía NCh 2527, gestión centralizada y cifrado de disco. Marca/modelo de referencia: dato a definir por el equipo. |

## 5. Incoherencias detectadas en otros documentos
- RT-14.04 figura Cumple parcialmente y RF-16.03 cumple. El catálogo propio deriva expresamente de RT-14.04 y las descripciones exigen el mismo alertamiento; la arquitectura acredita CloudWatch y turnos SOC/NOC (SD4 4.1.3.8; SD4-Anexos 4-W.7; T-15 5.7), por lo que ambos estados deben armonizarse con ese soporte.
- RF-17.02 y RT-16.02 quedan ambos parciales: el modelo y M9 cubren parámetros versionados y la regla térmica por producto, pero falta la interfaz/módulo de parametrización general. RF-17.05/RT-16.08 quedan ambos No cumple por falta de interfaz de consulta/exportación.
- RF-17.06 es parcial, mientras RT-16.11 y RT-16.12 son No cumple. RF-17.06 acredita flujos acotados de excepciones; las filas RT requieren un soporte general de workflow configurable por CLIENTE que no está descrito.
- RF-17.08 es parcial frente a RT-16.15 No cumple y RT-16.16 parcial: S3 acredita control de acceso, versionado, cifrado e integridad, mientras no se acredita búsqueda documental ni vista previa.
- RF-17.10 es parcial: RT-16.20 cumple el envío multicanal y RT-16.21 es parcial porque falta administración de plantillas por el CLIENTE.
- RF-17.12 y RT-16.28 quedan No cumple: la descarga analítica/regulatoria de SD4-Anexos 4-C y SD5 5.2.8 no identifica un módulo de listados con orden, filtros, paginación y exportación del filtro.
- RF-18.01 es parcial y reúne RT-16.17 parcial y RT-16.18 No cumple; RF-18.02 y RT-16.22 son parciales por preferencia por cliente, sin configuración individual por persona.
- RF-18.03 es parcial, mientras RT-16.23 figura Cumple: ambos derivan el mismo requisito, pero not_aviso/not_intento no registran apertura por mensaje (SD4-Anexos 4-H, INT-11; SD5-Anexos 5-A).

- RT-02.04 del T-12 menciona ADR-01 a ADR-21, mientras RF-13.03 y SD4 4.1.11/Anexo 4-O mantienen ADR-01 a ADR-22.
- RT-11.13 figura Cumple, aunque RF-14.03-BTT y RF-19.03 son parciales porque la Tabla 19 no contiene FQDN efectivos.
- RT-11.18 figura parcial, mientras RF-14.04-BTT y RF-19.04 cumplen por el plan, plazos, responsables y aviso crítico acreditados en T-14 cuentas 2.2.3/8.1.5.
- RT-03.23 figura Cumple, mientras RNF-13.09 es parcial: falta el estudio de cobertura dentro de cámaras sin señal.
- RT-11.08 figura Cumple, mientras RNF-14.01 es parcial por falta de cobertura integral TLS 1.3, suites modernas, HSTS con precarga y alerta anticipada.
- RT-11.20 y RNF-14.06 cumplen el mínimo anual y las pruebas antes de producción; SD1 1.3.2 declara frecuencia semestral y T-14 cuenta 8.2.2 frecuencia anual. La frecuencia semestral supera el mínimo, pero ambos documentos deberían expresar una misma cadencia.
- RT-11.23 figura Cumple, mientras RNF-14.08 es parcial porque el compromiso de generar SBOM no incluye su entrega al CLIENTE.
- RT-14.06 figura No cumple y RF-16.04 parcial. La materia coincide en análisis de causa raíz de incidentes críticos, pero RF-16.04 acredita postmortem P1/P2 y añade plazo/cierre correctivo; debe alinearse la valoración común.
- RT-14.07 figura No cumple y RNF-16.03 parcial: SD4/SD5 acreditan logs con acceso controlado/auditado, pero no depuración de datos sensibles antes de registrarlos.
- RT-21.06 y RNF-21.03 cumplen; T-15 5.6 define métricas telefónicas, FCR, abandono y ajuste de dotación.
- RT-21.15 figura No cumple, mientras RNF-21.06 cumple por la fila D-10; confirmar si el canal único con ticket y ciclo completo tiene igual alcance en ambos.
- RT-22.04 figura Cumple, mientras RNF-22.03 es parcial porque faltan las ventanas y peaks operacionales explícitos.
- RT-08.12 figura Cumple, mientras RNF-23.02 es parcial porque faltan IP/caída para varios modelos T-11.
- RT-08.09 figura Cumple, aunque RNF-23.04 es parcial: la gestión/cifrado se describen para 184 equipos existentes, no para las ocho estaciones nuevas.
- En el T-12 general, RT-11.17 y RT-21.01 atribuyen 8–10 personas a un solo puesto NOC. SD4-Anexos 4-W.7 y T-15 4.1/5.7 fijan 4 personas por puesto para NOC y SOC (8 total) y 5 por puesto desde el 26-04-2028 (10 total); RNF-21.01 ya expresa el total y la cifra por puesto.
- SD5-Anexos, Tabla A.8, emplea etiquetas de canales distintas entre tablas: CORREO/SMS/WHATSAPP/AVISO_EN_PORTAAL y EMAIL/SMS/PUSH. RF-17.10 acredita los canales de envío, pero permanece parcial porque falta la interfaz de administración de plantillas por el CLIENTE; el catálogo de códigos requiere armonización.
- RF-19.01–RF-19.05 y RF-14.01-BTT–RF-14.05-BTT son equivalentes en materia; sus estados/componentes se alinean: clasificación y matriz cumplen, superficie y brecha son parciales por FQDN e informe/RCA faltantes, y plan de incidentes cumple.
- T-11 conserva dimensionamiento preliminar de Wi-Fi; no acredita estudio realizado en cámaras de frío.
- T-11 describe gestión/cifrado para 184 equipos existentes; no extiende esa evidencia a las ocho estaciones nuevas.
