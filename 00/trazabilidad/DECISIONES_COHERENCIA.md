# Decisiones de coherencia del Subdocumento 4 (2026-10-01)

Registro interno de trabajo (no se publica). Todas las ediciones de 4.1, 4.2, 4.3, T-11 y anexos deben quedar alineadas con estas decisiones. Redacción final: español formal, sin notas al redactor, sin "pendiente", "borrador", "versión anterior", sin mencionar IA ni revisiones, sin precios.

## D1. RPO con el sitio aislado: tercer camino satelital en los CD

- Talca y Concepción incorporan un tercer camino de enlace: Starlink fijo (componente D-06, el mismo producto de los cross-docking), alimentado desde circuitos respaldados (en Talca, UPS y generador del recinto; en Concepción, UPS del gabinete).
- No es un enlace ocioso: es un camino activo de tercer nivel que, por calidad de servicio, transporta primero la replicación (DMS/WAL de Talca, salida del broker y outbox de cada sitio), la emisión de guías hacia el ERP y el SII, la identidad y la telemetría crítica; la oficina solo lo usa si caen fibra y LTE.
- Con tres caminos de dominios de falla distintos (fibra terrestre, red celular y satélite) cada CD mantiene la extracción continua de sus datos, por lo que el RPO ≤ 15 min (RT-07.04) se cumple también cuando caen fibra y LTE, incluido el terremoto que derriba la infraestructura terrestre.
- Cross-docking ya tiene satélite + LTE de dos proveedores (tres medios de transmisión).
- Límite residual, declarado UNA sola vez en 4.3.2 (subsección RPO y RTO) y solo referenciado desde 4.1 y 4.2: la falla simultánea de los tres caminos seguida de la destrucción del sitio antes de reponer alguno. Se declara como riesgo residual (RT-02.11) con sus mitigaciones: alarmas de retraso de replicación a 5 y 15 min, reposición del enlace por el proveedor, preemisión de guías y conservación local (NAS WORM en Talca). No se suspende la operación local (RT-03.10 manda 24 h autónomas).
- Se eliminan AL-BR-01, la "resolución formal del mandante" y toda frase que diga que el diseño no demuestra o no cumple el RPO.
- ADR-02 cambia: la alternativa "tri-camino" pasa a ser la adoptada en los CD.

## D2. Sitios principal y secundario; Concepción deja de ser respaldo de Talca

- 4.3.1 Data Center Primario: región AWS sa-east-1 (dominio nube) + sala técnica secundaria del CD Talca (dominio on-premise).
- 4.3.2 Data Center Secundario:
  - Dominio nube: región us-east-1 (activo-pasivo en caliente, igual que hoy).
  - Dominio on-premise de Talca: la plataforma de nube. Si se pierde la sala o el clúster de Talca, el perfil `wms_only` de Talca (misma imagen) se levanta en ECS Fargate de la región activa sobre la copia del WMS de Talca en Aurora (réplica DMS, que se habilita para escritura al detener la tarea DMS); los terminales y periféricos de Talca se conectan por la VPN por cualquiera de los tres caminos; si la región sa-east-1 tampoco está disponible, se hace en us-east-1 tras su promoción. RTO ≤ 4 h; RPO ≤ 15 min (DMS continuo + D1). Distancia Talca–São Paulo ≈ 2.700 km (amenazas comunes: ninguna sísmica ni eléctrica compartida).
  - Retorno: se reconstruye el clúster de Talca, se carga VM-02 desde Aurora y se invierte el sentido de la réplica hasta igualar; el corte de vuelta se hace fuera de las ventanas protegidas.
- Concepción es un sitio operacional autónomo (gabinete de borde). Ya no "asume la carga de Talca" ni tiene "RTO adicional de 1 a 2 h". Si falla su servidor, se repone y su base se reconstruye desde el estado central (eventos); los cross-docking igual.
- Concepción conserva firewalls y switches de núcleo en par por RT-08.03 (obligatorio para núcleo y cortafuegos en todo sitio), no por ser "sitio de recuperación".

## D3. Guía de despacho sin WAN

- El trabajador `erp-sync` deja de correr en Fargate: corre en Talca, en VM-04 junto a la ACL, con 2 procesos.
- Consume (a) la cola local RabbitMQ de Talca con las solicitudes del WMS de Talca (guías), sin depender del enlace, y (b) por conexión saliente, la cola SQS con las solicitudes originadas en la nube y en los demás sitios (Concepción, cross-docking, rendiciones, devoluciones, EDI). Publica los resultados por la misma vía.
- Preemisión: la guía se solicita al cerrar la carga en la noche. Un cambio de carga invalida la guía anterior (el ERP la anula según su procedimiento) y exige una nueva; ningún camión sale sin documento válido.
- El ERP sigue siendo el único emisor y conserva su comunicación con el SII por los tres caminos de Talca (D1).
- Consecuencia: desaparece la conexión entrante desde la nube a VM-04. La única conexión iniciada desde la nube hacia un sitio es AWS DMS hacia VM-02 (Talca), por el túnel IPsec, nominada y auditada.
- AL-DTE-01 se transforma en una prueba de aceptación (96 salidas con fallas inyectadas), no en una brecha.

## D4. Stock: sitios independientes y consolidación en la nube

- Cada sitio (Talca, Concepción, cada cross-docking) es autoridad sobre los movimientos físicos de su propia bodega; todos corren el mismo perfil `wms_only`. Se eliminan "Talca maestro", "Concepción edge" y "mini-WMS" como roles distintos (el cross-docking corre el mismo perfil en E-01).
- La consolidación global (stock por sitio, reserva central de M2 para preventa) vive en la nube (N-04/N-05) y se alimenta por eventos idempotentes (INT-03).
- Se elimina la conexión Concepción–Talca por TCP 8080/5432 y la de cross-docking–Talca por AMQPS 5671. Los cross-docking publican solo hacia SQS FIFO. INT-04 se renombra "Detalle de cross-docking a la nube" (mismo volumen).
- Transferencias entre CD (Talca abastece parte del surtido de Concepción) se registran como despacho en origen y recepción en destino, conciliadas en la nube.
- El SPOF "Maestro bodega Talca" se reemplaza por "Consolidación central de stock": efecto, la reserva central queda fechada; continuidad, cada sitio opera localmente y la preventa captura pedidos pendientes de validación.

## D5. Residencia de datos y Ley 21.719

- Se declara: región primaria sa-east-1 (São Paulo, Brasil) y secundaria us-east-1 (Virginia del Norte, EE. UU.). Ambas implican transferencia internacional desde Chile, no solo la réplica.
- Base de licitud y resguardos: AWS actúa como encargado del tratamiento por cuenta del CLIENTE (responsable), mediante contrato de encargo que incorpora las cláusulas contractuales tipo aprobadas para la Ley N° 21.719; cifrado en reposo con claves KMS administradas por el CLIENTE y en tránsito; minimización (la analítica y la geolocalización de personas no se replican a us-east-1); registro de actividades de tratamiento; control y auditoría de accesos.
- Art. 23 de las Bases Administrativas: la residencia es "declarada y sujeta a aprobación del CLIENTE". La propuesta lo reconoce como hito contractual de la Etapa 1 y NO dice que "no depende de aprobaciones".
- Garantía de continuidad si el CLIENTE no aprueba alguna región o categoría: la región secundaria es un parámetro de la infraestructura como código; cualquier región AWS que el CLIENTE apruebe y que ofrezca Aurora Global Database, DynamoDB Global Tables, replicación de S3, ECS Fargate y AWS Backup mantiene los mismos RTO y RPO sin cambiar la arquitectura. Si el CLIENTE restringe una categoría de datos a la región primaria, esa categoría se excluye de la réplica (como ya ocurre con la geolocalización) y se protege con copias inmutables en otra cuenta de la misma región; solo pueden restringirse así categorías no críticas.
- Justificación principal: 4.3.2 (Región o sitio de recuperación). 4.1 (capa 7) y 4.2.3.2 la referencian.

## D6. Talca: nodos y almacenamiento

- Nodo del clúster (3 iguales): HPE ProLiant DL345 Gen11 o Dell PowerEdge R7615: 1 AMD EPYC 9124 de 16 núcleos (32 hilos), 64 GB DDR5 ECC (4 × 16 GB, ampliable), arranque en 2 M.2 de 480 GB en RAID 1, 2 NVMe de 960 GB por nodo para Ceph (sin RAID, controlador en modo HBA), 2 puertos de 10 GbE, 2 fuentes redundantes Flex Slot de 800 W en circuitos A/B. La placa por nodo sigue siendo 1.600 W, por lo que la tabla eléctrica 4.3-1 no cambia.
- Ceph: 6 OSD (2 por nodo), réplica size=3, min_size=2, 3 monitores (uno por nodo). Tolera la caída de un nodo con quórum. Capacidad útil ≈ 5,76 TB brutos ÷ 3 = 1,92 TB (≤ 80 % de llenado ≈ 1,5 TB) frente a 221 GB requeridos a 3×.
- La sobrecarga de Ceph entra al cálculo: por OSD 1 vCPU y 4 GB; monitor/manager 1 vCPU y 2 GB por nodo.
- NAS D-05: Synology RackStation RS2423RP+ o equivalente, fuente redundante, 4 discos de 4 TB en RAID 6 (≈ 8 TB útiles), instantáneas inmutables (WORM).
- Se elimina "Ceph sobre RAID 10" y "segunda copia".

## D7. Fuentes redundantes (RT-08.04) y energía fuera de la sala

- Servidor de Concepción: HPE ProLiant DL20 Gen11 con Xeon E-2400 de 8 núcleos, 32 GB, RAID 10 de 4 SSD de 1,92 TB y 2 fuentes redundantes Flex Slot de 500 W en circuitos distintos.
- Mini-PC E-01: se mantiene (Advantech ARK-2250 o equivalente, entrada 9–36 VDC), alimentado por dos fuentes DIN de 24 VDC en circuitos distintos (una desde la UPS del gabinete y otra desde la red) con módulo de redundancia.
- Switch de cada cross-docking: dos switches industriales gestionables con PoE+ y doble entrada de alimentación redundante (Moxa EDS-P506E-4PoE o equivalente) por plataforma, cada uno alimentado por dos fuentes DIN en circuitos distintos; mini-PC con dos interfaces, una a cada switch; cada AP en un switch distinto. Total 6 + 1 de reserva = 7. Esto además cumple RT-08.03 (núcleo sin punto único). La fila de switches por cross-docking en la tabla de 4.2.1 pasa de 1 a 2.
- Firewalls de cross-docking: Fortinet FortiGate Rugged 60F-3G4G o equivalente, doble entrada DC, módem LTE de doble SIM.
- Firewalls de Talca y Concepción: con doble fuente. Switches de acceso C9200-24P: con segunda fuente. Consola KVM: sobre IP con doble fuente. NAS: fuente redundante. Gateways IoT: ya tienen doble entrada.
- Equipos terminales del operador (ONT de fibra, router LTE del operador, terminal Starlink): su redundancia es la del camino (tres caminos independientes en circuitos distintos).
- Terminales móviles operan con batería; los AP reciben PoE desde switches con doble fuente; impresoras, balanzas y estaciones de trabajo no se fabrican con doble fuente: se cubren con redundancia por cantidad (otra unidad del andén o reserva) y circuitos protegidos. Esta interpretación se declara UNA vez en 4.2.1.
- Se elimina en todo el documento "fuente única", "punto único de falla aceptado" para el servidor de Concepción, el mini-PC y el switch; el mini-PC sigue siendo equipo único por sitio (cubierto por la autonomía local, la reposición desde Talca y la reconstrucción desde la nube).
- Energía fuera de la sala:
  - Gabinetes de piso de las bodegas (Talca 4, Concepción 2): una UPS en línea de 1,5 kVA por gabinete, 30 min a plena carga, que alimenta el switch de acceso PoE (y por él los AP) y la impresora de andén más cercana.
  - Gateways IoT y módulos de temperatura: dos fuentes de 24 VDC; en Talca una de ellas se alimenta desde el tablero del recinto (UPS y generador), para que el registro de frío continúe durante un corte prolongado; en Concepción, desde la UPS del gabinete.
  - Concepción, gabinete de borde: UPS en línea de 3 kVA con 30 min a plena carga para servidor, firewalls, switches de núcleo y Starlink. Sin generador: el CD no tiene generación propia y sin red eléctrica la bodega no opera (iluminación, cámaras, cargadores); la UPS cubre cortes breves y el apagado ordenado, y los datos ya están replicados fuera del sitio. Es la tipología de borde del numeral 6.1 (protección eléctrica).
  - Cross-docking: la UPS interna de 30 min del gabinete se mantiene; segundo circuito directo de red para las segundas fuentes.

## D8. Térmico de la sala de Talca

- Carga térmica de la sala de servidores = carga TI de diseño 7,0 kW (las pérdidas del UPS ya no se suman, porque el UPS está en su propia sala). Se mantienen 2 unidades de precisión de 10 kW en N+1.
- Sala de UPS y baterías: climatización propia de confort de 3,5 kW (≈ 12.000 BTU/h) que mantiene 20–25 °C, temperatura recomendada para baterías VRLA, más ventilación; disipa las pérdidas del UPS (≈ 0,61 kW) y el calor de carga de baterías.
- Recalcular en 4.3.1: consumo de la climatización de precisión proporcional a 7,0 kW (≈ 2,1 kW), consumo de la climatización de la sala de UPS (≈ 0,4 kW), iluminación y apoyo 0,6 kW, pérdidas UPS 0,61 kW, gateways IoT y sus fuentes ≈ 0,1 kW → total ≈ 10,8 kW; PUE ≈ 10,7 ÷ 7,0 ≈ 1,5 (PUE sin los gateways, que no son de la sala; declarar el criterio). Generador: con ≈ 10,8 kW y factor de potencia 0,8 se requieren ≈ 13,5 kVA; con margen de 80 % de carga máxima se especifica un grupo de 20 kVA (sube desde 15 kVA). El UPS de 10 kVA no cambia (solo carga TI).

## D9. Conmutación regional

Secuencia (tabla 4.3-6), en serie y peor caso:
1. Detección por verificación de salud y alarmas — Route 53 y CloudWatch — < 5 min.
2. Declaración del incidente y autorización de la promoción — CLIENTE, con aviso por SNS — tiempo de decisión.
3. Promoción de Aurora en us-east-1 — Systems Manager Automation — 15–20 min.
4. Escalado de la plataforma de aplicación a carga completa — Systems Manager Automation — < 30 min (puede correr en paralelo con 3).
5. Restitución de Keycloak, API pública y privada y Verified Access — Systems Manager Automation — < 15 min.
6. Validación funcional con escrituras de pedidos y sincronización de prueba — Operación — < 15 min.
7. Cambio del tráfico a us-east-1 en Route 53 (registros con TTL de 60 s preparados de antemano) — Systems Manager Automation — < 5 min.
8. Reconexión de los túneles de los sitios y de los brokers — Systems Manager Automation — < 15 min.
Suma ≈ 1 h 45 min más la decisión, dentro de RTO 4 h. No hay conmutación automática del tráfico por salud antes de promover la base; el retorno automático está deshabilitado. Se elimina "Actualización de DNS 45–60 min".

## D10. Registro ADR único

- Un solo registro: Anexo 4.1-O "Registro de decisiones de arquitectura", en el archivo de anexos del Subdocumento 4. Contiene ADR-01 a ADR-22 con: decisión, alternativas evaluadas, criterio de selección, consecuencias, evidencia exigida y requisitos que la sustentan (RT-02.04).
- Lista: 01 Estilo arquitectónico; 02 Conectividad WAN (tres caminos); 03 Modelo híbrido y topología de sitios (D4); 04 Persistencia políglota; 05 Mensajería asíncrona (única conexión entrante: DMS); 06 Identidad híbrida; 07 Movilidad de terreno; 08 Destino del WMS 2013; 09 Estrategia de recuperación ante desastres (D2); 10 Plataforma on-premise: virtualización y almacenamiento (D6); 11 Integración B2B/EDI; 12 Capacidad y peak (Aurora de tamaño fijo dimensionada para 3×, sin cambio de instancia durante el congelamiento; escalado de Fargate por perfil; mamparos); 13 Puerta de enlace de servicios; 14 Observabilidad; 15 Gestión de secretos; 16 Acceso de personas internas y remotas; 17 Emisión de guías y liberación documental (D3; reemplaza ADR-L01); 18 Protección de datos fuera del sitio (D1; reemplaza ADR-L02); 19 Residencia de datos y regiones (D5); 20 Frontend web (Angular frente a React/Vue); 21 Infraestructura como código y cadena de entrega (Terraform + Ansible, GitLab CI + CodeBuild); 22 Cadena de frío en el borde (Greengrass en gateways frente a lectura directa a nube o PLC).
- IOPS en ADR-10 con la base del Anexo 4.2-A (sin "~840").
- El cuerpo conserva en 4.1.11 una tabla resumen (ID, decisión, alternativa principal descartada, criterio decisivo), con una frase por celda. Se elimina el capítulo "Registro de decisiones de arquitectura" (4.4) del cuerpo. Las referencias del cuerpo a `\ref{sub:adr-xx}` se reemplazan por "ADR-xx (Anexo 4.1-O)".

## D11. Ventana de cross-docking

- Ventana de 3 h (Caso, tabla de sitios): 03:00–06:00. 03:00–05:00 llegada del camión de línea y desconsolidación (cronograma del caso); 05:00–06:00 re-despacho. Las 4 operaciones por entrega se reparten: recepción, escaneo y desconsolidación en 03:00–05:00; despacho en 05:00–06:00.

## D12. Archivos de entrega

- LAFROX-Subdocumento4.pdf: cuerpo 4.1–4.3, Referencias y Declaración de uso de IA al final.
- LAFROX-Subdocumento4-Anexos.pdf: anexos 4.1-A a 4.1-V (4.1-O = registro ADR) y Anexo 4.2-A "Memoria de cálculo del dimensionamiento" (antes "Anexo 4.B"; secciones 4.2-A.1…).
- LAFROX-Formulario-T-11.pdf: formulario propio.
- El cuerpo cita anexos y formulario por nombre, sin `\ref` entre archivos.

## D41. RT-03.14: equipos on-premise críticos en par (2026-10-07)

- Decisión del usuario: Opción A. Concepción y cada cross-docking pasan de un equipo único a un par idéntico, uno activo y otro en espera. Talca conserva su clúster N+1.
- Concepción: dos HPE DL20 con Proxmox VE, sin clúster. El activo ejecuta VM-C01 a VM-C04 y el otro sus copias. Cross-docking: dos E-01 por plataforma (T-11: 6 + 1 de reserva).
- Mecanismo común: PostgreSQL con réplica sincrónica al equipo en espera; keepalived (VRRP) mueve la dirección virtual del sitio en menos de un minuto; el de espera se promueve solo si pierde al activo por sus dos interfaces; al tomar el control republica el outbox de 24 h y la nube deduplica por UUID; si cae el de espera, la réplica pasa a asíncrona con alerta.
- El equipo en espera no atiende transacciones: WMS y shipper detenidos. Su observabilidad se modela en 20 % de un nodo activo (0,05 GB y 200 eventos por día). INT-14 = 14.400; totales 230.252 / 353.333; drenaje Concepción 1,44 Mbps y cross-docking 0,35 Mbps.
- Energía: UPS de Concepción de 3 a 5 kVA (3,42 kVA, 68 %); cross-docking 0,42 kVA (57 % de 0,75 kVA). EDR: 11 equipos físicos y 14 VM.
- Archivos: 4.1 (capas), 4.2.0, 02_a (incl. figura TikZ), 02_c, 04_c, 11_j (alta disponibilidad y pruebas), 12_k, Anexos 4-G, 4-I, 4-O (ADR-10), 4-W, T-11 y `calculo.py`.
