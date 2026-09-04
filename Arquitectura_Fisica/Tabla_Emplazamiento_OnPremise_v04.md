# Arquitectura Física — Componente On-Premise
## Distribuidora Puelche S.A. — Caso 02 Logística

> **Nota de alcance:** Este documento cubre exclusivamente el segmento **On-Premise** de la arquitectura híbrida exigida por el Artículo 16°. La contraparte AWS es el documento `Propuesta_Arquitectura_Cloud_Caso02_CLAUDE_v2.md`; la integración entre ambos segmentos se definió al consolidar ambas piezas (ver Sección 3 — Referencias Cruzadas y los reencuadres A-04/A-05/A-01/A-02/D-05). Versión 04 — incorpora decisiones de diseño aprobadas, correcciones de inconsistencias y la alineación de las costuras de integración con la contraparte cloud.

---

## SECCIÓN 1 — TABLA DE EMPLAZAMIENTO

*Justificación componente por componente conforme al Artículo 16°, numeral 16.2, y al capítulo 3.1 de las Bases Técnicas Transversales.*

### Criterios de evaluación

| Criterio | Sigla |
|---|---|
| Latencia | LAT |
| Criticidad operacional | CRIT |
| Volumen de datos local | VOL |
| Disponibilidad de conectividad | CONN |
| Costo total de propiedad | TCO |
| Acoplamiento físico con hardware | HW |

---

### BLOQUE A — NÚCLEO WMS LOCAL

**A-01 — Motor WMS On-Premise**
*(CD Talca — nodo principal; CD Concepción — instancia edge local autónoma)*

| Criterio | Evaluación |
|---|---|
| Emplazamiento | ON-PREMISE |
| LAT | <= 1 s (RNF-05.01) — inviable con latencia de red remota (40–80 ms mínimo hacia nube) |
| CRIT | CRITICO — "si el sistema se cae entre las 5:30 y las 7:00, ese día no hay operación" (Cap. 8, Nelson) |
| VOL | Alto — 260.000 líneas/mes, 2.4M unidades/mes, 11.400 posiciones (Talca) + 9.000 m² (Concepción) |
| CONN | Talca: cortes 4x/año hasta 6 h; cámara congelado sin señal. Concepción: sin respaldo WAN actual (Cap. 6) |
| TCO | CAPEX requerido — la sala actual de Talca (25 m², split AC, UPS 10 min) NO cumple las Bases (Cap. 6, Caso 02). Se requiere habilitación de Sala Técnica Secundaria en Talca y nodo de cómputo local en Concepción |
| HW | Sí — scanners GS1, impresoras térmicas, terminales rugosos, rack de servidores |
Justificación: El turno de picking nocturno (22:00–06:00) involucra 120 personas. RNF-05.01 exige <= 1 s de respuesta incluso en la cámara de congelado a -22°C donde no existe señal de red (Cap. 6). La latencia mínima de ida y vuelta hacia la nube (40–80 ms con fibra en buen estado) más el procesamiento remoto viola el umbral de 1 s. La operación desconectada mínima de 24 h (RT-03.10, RNF-02.01) no puede delegarse a un WMS alojado exclusivamente en nube.
**Relación con el WMS en nube (Aurora):** Este WMS on-premise es el **maestro de la operación de bodega** (recepción, preparación, despacho) y la única instancia que garantiza la autonomía de 24 h (RT-03.10). La capa **Aurora PostgreSQL en la nube NO duplica ni sustituye al WMS**: actúa como **réplica de continuidad/DRP** de este WMS y como OLTP de los procesos que sí corren en nube (preventa, reparto, BI). El flujo bodega↔nube se sincroniza vía el broker A-03 y la VPN, garantizando que si Talca cae, la nube mantiene la última imagen del WMS para recuperación (ver DRP on-premise→nube).
**Tipología de sitios declarada (Cap. 6.1, Bases Técnicas Transversales):**
- **CD Talca:** Sala Técnica Secundaria — cómputo, almacenamiento y telecomunicaciones sustantivos. Aplican RT-06.01 a RT-06.24 de forma proporcional.
- **CD Concepción:** Gabinete de Borde Operacional — instancia WMS edge + switch + firewall + enlace LTE. Garantiza 24 h de autonomía independiente de Talca.
- **Plataformas Cross-Docking (Curicó, Chillán, Los Ángeles):** Gabinete de Borde Operacional (ver E-01).

**Procedimiento de conmutación on-premise: Talca → Concepción (DRP local):**
Si la Sala Técnica Secundaria de Talca sufre indisponibilidad total (fallo de infraestructura, incendio, corte prolongado de energía más allá de UPS), Concepción actúa como **sitio de recuperación primario on-premise** según el siguiente procedimiento:
1. **Detección (0-10 min):** Monitoreo ADOT/F-01 detecta pérdida total de conectividad con Talca; alerta vía SNS al equipo de operaciones.
2. **Verificación (10-20 min):** Confirmación de que Talca no responde (descarte de falso positivo: reinicio de servicios remotos vía SSM Agent si hay conexión parcial).
3. **Activación de Concepción (20-30 min):** Concepción tiene su propia instancia WMS edge (A-01) con base de datos local (A-02 embebida) y Keycloak Master (A-05). Se promueve el nodo de Concepción a **modo primario**: los terminales de picking de Talca (C-03) se reconectan al WMS de Concepción vía WAN (si hay conectividad parcial) o operan en modo offline local.
4. **Sincronización Aurora → Concepción:** Aurora (nube) mantiene la réplica más reciente del WMS (via DMS CDC, RPO ≤ 15 min). Si Concepción necesita restaurar datos fresantes, se ejecuta una restauración puntual desde Aurora hacia la instancia local de Concepción vía VPN (RTO estimado: 1-2 h adicional sobre el RTO normal de 4 h).
5. **Reconducción a Talca:** Una vez restaurada la infraestructura de Talca, se revierte el flujo: Concepción sincroniza sus transacciones acumuladas hacia Aurora (nube), y Talca se restaura desde Aurora + D-05 local. La reconducción se ejecuta en ventana de mantenimiento con validación de integridad.

**Limitación conocida:** Concepción no tiene appliance D-05 equivalente (no declara respaldo local propio). Si Concepción también falla simultáneamente con Talca (evento catastrófico regional), la recuperación depende exclusivamente de Aurora (nube) y del enlace WAN. El RTO en este escenario depende del estado del enlace y del volumen de datos a restaurar.

---

**A-02 — Base de datos transaccional WMS (PostgreSQL)**

| Criterio | Evaluación |
|---|---|
| Emplazamiento | ON-PREMISE |
| LAT | < 5 ms (escritura local sobre SSD NVMe) |
| CRIT | CRITICO — único "sistema de verdad" durante corte de enlace |
| VOL | Alto — 8.400 SKU, 11.400 posiciones, trazabilidad de lote, retención 5 años (RNF-09.02) / 6 años tributario (RNF-01.02) |
| CONN | Escritura local sin pérdida durante desconectado (RT-03.11) |
| TCO | CAPEX en discos SSD NVMe; PostgreSQL sin licencia propietaria; sin egress cost |
| HW | No directamente (interfaz a través del motor WMS) |

Justificación: RT-03.11 exige registro continuo sin pérdida en desconectado. RT-03.14 exige tolerancia a falla de al menos un disco. RAID 5 y RAID 6 se descartan explícitamente: su penalización de escritura (4–6 E/S por escritura en RAID 5) es incompatible con la confirmación de picking en <= 1 s bajo 120 terminales concurrentes (RNF-05.01). Almacenamiento remoto implicaría latencia > 100 ms con jitter, igualmente incompatible. Esta BD local es el "sistema de verdad" de bodega durante la desconexión; su **réplica de DRP vive en Aurora (nube)** (ver A-01), la cual se mantiene al día vía streaming del log WAL a través de la VPN (RPO <= 15 min).
**Esquema físico de almacenamiento aprobado:**
| Capa | RAID | Discos | Descripción |
|---|---|---|---|
| SO + Hipervisor | RAID 1 (espejo) | 2 × SSD 480 GB | Tolera caída de 1 disco; arranque del sistema sin intervención |
| Storage de datos WMS + BD | RAID 10 (espejo + franjas) | 4 × SSD NVMe 1,92 TB + 1 Hot-Spare | Tolera caída de 1 disco por par espejado; Hot-Spare reconstruye automáticamente; lectura paralela en franjas para 120 terminales simultáneos |
**Factor de compra:** capacidad útil = capacidad bruta × 0,5 (RAID 10) → para 2 TB útiles se requieren 4 TB brutos; factor de compra ×2,5 sobre capacidad útil objetivo (incluye Hot-Spare y margen de crecimiento a 5 años). Cálculo definitivo en la sección de dimensionamiento.

**Mecanismo concreto de réplica WAL on-prem → Aurora (nube):** La replicación del WMS on-premise (A-02) hacia Aurora se ejecuta mediante **AWS Database Migration Service (DMS) con CDC (Change Data Capture)**. DMS se despliega como tarea continua en una instancia DMS dentro de la VPC de nube, conectándose al PostgreSQL de Talca a través de la VPN IPsec (D-01→VGW). DMS lee el WAL (write-ahead log) del PostgreSQL on-prem con `wal_level=logical` y aplica los cambios de forma continua en Aurora PostgreSQL como target. Ventajas sobre alternativas (pgBackRest, pglogical): es un servicio AWS gestionado, no requiere agentes adicionales en el on-prem, monitorea lag de replicación en CloudWatch, y soporta transformación de esquema bajo demanda. El lag declarado es < 15 min (cumple RPO ≤ 15 min exigido por Art. 20° / BTT Cap. 7). Requisito previo en A-02: habilitar `wal_level=logical` en postgresql.conf (cambio de configuración sin downtime).

---

**A-03 — Broker de colas offline (RabbitMQ embebido)**

| Criterio | Evaluación |
|---|---|
| Emplazamiento | ON-PREMISE |
| LAT | < 10 ms (encolado local) |
| CRIT | CRITICO — sin broker local, las transacciones del desconectado se pierden |
| VOL | Moderado — ráfagas al reconectar (hasta 24 h de operación acumulada) |
| CONN | Opera completamente sin WAN durante el desconectado |
| TCO | Bajo — software libre, commodity VM |
| HW | No |

Justificación: RT-03.11 y RT-03.12 exigen encolado local con integridad garantizada y sincronización automática y reconciliable al recuperar el enlace. Si el broker fuera remoto, la pérdida del enlace invalidaría el encolado. Política determinista de reconciliación: orden cronológico de timestamp local, con bitácora auditable (RT-03.12).

---

**A-04 — Capa anticorrupción ERP (ACL) — Frontera única del ERP**
*(adaptador entre el WMS, la nube y el ERP existente de 2017, sin documentación técnica de interfaces)*

| Criterio | Evaluación |
|---|---|
| Emplazamiento | ON-PREMISE (frontera única del ERP) |
| LAT | < 50 ms (llamada síncrona local) |
| CRIT | ALTO — sin ACL, un cambio en el ERP rompe el WMS |
| VOL | Bajo — mensajes de integración (texto estructurado) |
| CONN | Encola si ERP no responde; no requiere WAN entre nube y ERP local |
| TCO | Bajo — proceso ligero, VM pequeña |
| HW | No |

Justificación: El ERP de 2017 (sistema de gestión) no tiene documentación técnica de interfaces (Cap. 5) y es el registro contable/tributario que **no se modifica ni se reemplaza** (Cap. 10). La ACL (RT-02.14, RT-05.20) aísla el modelo interno del WMS y de la nube del modelo del ERP, evitando que un cambio en el ERP propague su modelo al núcleo de la solución. Se despliega on-premise **como frontera única de acceso al ERP** porque: (1) el ERP vive on-premise en Talca; (2) latencia de llamadas síncrona nube-a-oficina supera los 50 ms; (3) en modo desconectado la ACL encola las transacciones hacia el ERP sin pérdida (RF-01.09); y (4) concentra el acceso desde la nube: **el worker Celery `celery-erp-sync` (módulo `integraciones` Django) atraviesa la VPN y llega al ERP únicamente vía esta ACL**, nunca directamente, preservando el no-intervención del Cap. 10 y la única vía documentada (contrato OpenAPI en la ACL).

---

**A-05 — Keycloak Master (IdP on-premise)**
*(instancia maestra de Keycloak para autenticación y SSO durante cortes de WAN; la réplica de solo lectura vive en la nube — no un segundo IdP)*

| Criterio | Evaluación |
|---|---|
| Emplazamiento | ON-PREMISE |
| LAT | < 200 ms (autenticación local) |
| CRIT | CRITICO — sin él, los 120 operarios de picking no pueden hacer login durante un corte de WAN, deteniendo la operación nocturna |
| VOL | Bajo — realm de usuarios y tokens JWT (texto compacto) |
| CONN | Funciona sin WAN; sincroniza cambios de identidad (altas/bajas, roles) con la réplica cloud al recuperar el enlace |
| TCO | Bajo — Keycloak open source (licencia Apache 2.0); VM en el hipervisor de Talca y réplica en Concepción |
| HW | No |

Justificación: RF-15.01 exige gestión de identidad centralizada con federación OIDC/OAuth 2.1. RF-15.02 exige SSO para todos los módulos. RF-15.03 exige MFA para administradores. RF-15.04 exige RBAC con matriz de segregación. RF-15.05 exige aprovisionamiento/desaprovisionamiento automático en <= 24 h. El IdP **Keycloak** se despliega en modo híbrido: **Master en on-premise (VM-05 Talca)** que maneja todas las escrituras (altas, bajas, cambios de rol) y una **réplica de solo lectura en la nube** (ECS Fargate) para autenticar usuarios en la nube. Esta configuración resuelve RNF-13.01 (autonomía 24 h): si el enlace WAN cae, los operarios de picking se autentican localmente contra Keycloak Master (PostgreSQL local A-02), sin depender de internet. Al recuperar el enlace, Keycloak Master sincroniza usuarios/roles con la réplica cloud via export/import del Realm. La autoridad última de identidad es única (Keycloak, con master on-premise como fuente de verdad); no se introduce un segundo IdP ni una segunda "verdad" de identidad. A diferencia de Amazon Cognito (que requiere internet para toda autenticación), Keycloak permite operación offline completa, clave para la cámara de congelado a −22 °C sin señal.

---

### BLOQUE B — CADENA DE FRÍO E IoT

**B-01 — Sensores IoT de temperatura**

| Criterio | Evaluación |
|---|---|
| Emplazamiento | ON-PREMISE (hardware en sitio) |
| LAT | < 1 s (tiempo real) |
| CRIT | CRITICO — pérdida de $21M por no demostrar cadena de frío (Cap. 7.3) |
| VOL | Alto — lectura cada 30 s × ~28 sensores (Talca + Concepción) |
| CONN | Cámara congelado sin señal Wi-Fi ni móvil — estructura metálica bloquea (Cap. 6) |
| TCO | Bajo — CAPEX en sensores; sin egress cost |
| HW | Sí — sondas físicas, RS-485/Modbus, malla ZigBee industrial |

Justificación: La Autoridad Sanitaria observó la ausencia total de registro continuo (Cap. 7.3). La cámara de congelado bloquea toda señal inalámbrica. Los sensores deben comunicarse en red industrial cableada (RS-485/Modbus) o malla industrial (ZigBee/LoRa), independiente de la WAN. El rechazo de un camión completo por sospecha de ruptura ($21M, Cap. 7.3) confirma que la lectura debe ser local e inmediata.

---

**B-02 — Gateway / Concentrador IoT local**
*(con runtime AWS IoT Greengrass Core embebido)*

| Criterio | Evaluación |
|---|---|
| Emplazamiento | ON-PREMISE |
| LAT | < 5 s (agregación y detección de excursión) |
| CRIT | ALTO — sin él, las lecturas de la cámara no llegan a ningún sistema |
| VOL | Alto en ráfaga al reconectar (historial acumulado durante desconectado) |
| CONN | Opera sin enlace — persiste localmente; sincroniza al recuperar (RNF-09.04: 14 h) |
| TCO | Bajo — dispositivo edge industrial commodity con runtime Greengrass sin costo adicional de licencia |
| HW | Sí — RS-485, Modbus, protocolos industriales |

Justificación: RT-03.19 valora el procesamiento en el borde. El concentrador ejecuta: (a) ingesta de lecturas en tiempo real, (b) detección de excursiones con umbral configurable (Katherine, Cap. 8), (c) alerta local inmediata al WMS para bloquear despacho, (d) persistencia local durante cortes (14 h, RNF-09.04), (e) sincronización diferida al data lake en nube al recuperar. El runtime **AWS IoT Greengrass Core** se instala en el dispositivo edge, lo que permite ejecutar funciones Lambda locales para el procesamiento de telemetría sin depender del enlace WAN. En la cámara de congelado a -22°C, donde no existe señal (Cap. 6), Greengrass mantiene la lógica de detección de excursiones y el buffer de datos de forma completamente offline. Al recuperar la WAN, sincroniza automáticamente con AWS IoT Core en nube.

---

**B-03 — Termógrafos digitales de camión**

| Criterio | Evaluación |
|---|---|
| Emplazamiento | HIBRIDO (hardware local en camión + sincronización a nube) |
| LAT | Tiempo real (almacenado localmente) |
| CRIT | CRITICO durante el viaje |
| VOL | Moderado — 1 log/min × 18 camiones con equipo de frío |
| CONN | Rutas rurales sin cobertura hasta 2 h (Cap. 6, Jonathan) |
| TCO | Bajo — CAPEX en dispositivos certificados |
| HW | Sí — sensor embebido, BLE/GPS, almacenamiento interno |

Justificación: El termógrafo almacena localmente toda la cadena de temperatura y sincroniza al recuperar cobertura (RNF-09.04). Al regresar a base, los datos se descargan también al Gateway IoT (B-02) como respaldo adicional.

---

### BLOQUE C — DISPOSITIVOS DE OPERACIÓN EN TERRENO

**C-01 — App de Preventa (mobile offline-first)**

| Criterio | Evaluación |
|---|---|
| Emplazamiento | HIBRIDO (app local en dispositivo + backend en nube) |
| LAT | <= 1,5 s por línea (RNF-03-01) — ejecutado localmente |
| CRIT | CRITICO — 62 preventistas, 31.000 pedidos/mes |
| VOL | Bajo — sincronización de pedidos en texto estructurado |
| CONN | Hasta 2 h sin señal en rutas rurales (Cap. 6) |
| TCO | Bajo OPEX — app móvil |
| HW | Sí — cámara del dispositivo para fotos (RF-01.04) |

Justificación: La lógica de toma de pedido, validación de crédito cacheado, cálculo de promociones y generación de ID único offline (RF-03.16) se ejecutan localmente para cumplir <= 1,5 s sin importar la cobertura. Los pedidos offline se encolan con deduplicación automática al sincronizar (RF-03.17). El backend de validación en tiempo real está en nube.

---

**C-02 — App del Repartidor/Conductor (mobile offline-first)**

| Criterio | Evaluación |
|---|---|
| Emplazamiento | HIBRIDO — ejecución y persistencia 100% offline en dispositivo (hasta 14 h); ingesta, conciliación de POD y sincronización con ERP en backend Cloud |
| LAT | Inmediata — toda la lógica de entrega se ejecuta localmente; no depende de señal |
| CRIT | CRITICO — 1.400 entregas/día; ventana de despacho 05:30–07:00 no admite dependencia de red |
| VOL | Bajo en ruta — POD (foto firma), registros de entrega, cobro efectivo; Alto al sincronizar (acumulado 14 h) |
| CONN | Rutas rurales hasta 2 h sin señal; rutas completas recuperan cobertura solo al regresar a base (Cap. 6, 8, Jonathan) |
| TCO | Bajo OPEX — app móvil; CAPEX en dispositivos rugosos con cámara, GPS y BLE |
| HW | Sí — cámara para firma POD digital, GPS integrado, BLE para sincronización con termógrafo (B-03) |

Justificación: RNF-06.02 exige persistir 100% de datos durante mínimo 14 h sin señal. El cobro en efectivo (38% canal tradicional, Cap. 4.7) no puede depender de conexión en ningún momento de la ruta. La app almacena localmente en SQLite cifrado: secuencia de entrega, estado de cada parada, foto de firma POD, devoluciones, cobro en efectivo y lecturas del termógrafo. Al ingresar a zona con cobertura (o al regresar a base), sincroniza automáticamente con el backend Cloud para conciliación de POD y generación de eventos hacia el ERP (RF-02.06). RNF-07.01 exige consolidación de cobranzas en <= 10 min tras conectar a red.

---

**C-03 — Terminales rugosos de bodega (picking)**

| Criterio | Evaluación |
|---|---|
| Emplazamiento | ON-PREMISE (conectado a WMS local) |
| LAT | <= 1 s (RNF-05.01) — online y offline, incluida cámara |
| CRIT | CRITICO — picking nocturno 120 personas, 38% rotación anual |
| VOL | Alto — 260.000 líneas/mes generadas localmente |
| CONN | Cámara congelado sin señal (Cap. 6); bodega general: Wi-Fi local |
| TCO | Bajo — hardware industrial, vida útil 5–7 años |
| HW | Sí — escáner GS1 integrado, pantalla con guantes (RNF-05.02), certificado -22°C |

Justificación: RNF-05.02 exige pantalla operable con guantes térmicos (elementos >= 15×15 mm), funcionalidad 30 min a -22°C. Los dispositivos de consumo masivo fallan a esa temperatura (Cap. 8, Ximena). Se requieren terminales rugosos industriales certificados (IP65, -25°C a +60°C). Operan offline contra el WMS local durante la sesión en cámara; sincronizan al salir. RNF-05.03: curva de aprendizaje <= 2 h.

---

**C-04 — Impresoras térmicas de andén**

| Criterio | Evaluación |
|---|---|
| Emplazamiento | ON-PREMISE |
| LAT | Inmediata — el recepcionista espera la etiqueta para continuar |
| CRIT | MEDIO-ALTO — bloquea cierre de recepción si falla |
| VOL | Bajo — etiquetas de código de barras |
| CONN | LAN de bodega local |
| TCO | Bajo — hardware periférico |
| HW | Sí — impresora térmica, protocolo ZPL/ZPL-II |

Justificación: RF-01.07 exige generar e imprimir la etiqueta SSCC al finalizar el registro del pallet con GTIN (AI 01), lote (AI 10), vencimiento (AI 17) y fecha de recepción (AI 11). Depender de la nube introduciría latencia inaceptable y fallaría durante cortes de enlace.

---

### BLOQUE D — INFRAESTRUCTURA DE RED Y CONECTIVIDAD

**D-01 — Firewall perimetral / UTM**
*(En cada sitio con sala técnica o gabinete de borde: Talca, Concepción y plataformas cross-docking)*

| Criterio | Evaluación |
|---|---|
| Emplazamiento | ON-PREMISE (Talca — Sala Técnica Secundaria; Concepción y Cross-Docking — Gabinete de Borde) |
| LAT | < 1 ms (hardware inline) |
| CRIT | CRITICO — todo el tráfico LAN-WAN pasa por aquí; fallo detiene la sincronización |
| VOL | Alto — todo el tráfico de red local + VPN hacia nube |
| CONN | Gestiona failover fibra -> LTE automáticamente con tiempo de conmutación < 30 s declarado (RT-03.17, RNF-13.07) |
| TCO | CAPEX nuevo — la sala actual de Talca (25 m², acceso por llave) no cumple RT-06.20 (biometría facial) ni RT-06.16 (detección AnaLASER). Se requiere adecuación física de la sala técnica como parte del proyecto |
| HW | No (dispositivo inline de red) |

Justificación: RT-03.17 / RNF-13.07 exige enlace redundante con caminos físicos y proveedores distintos y conmutación automática <= 5 min (en este caso < 30 s). El firewall gestiona las zonas de red (pública, DMZ, aplicación, datos, gestión), controla el failover WAN y cifra el túnel VPN/IPsec hacia la nube. El firewall actúa como **Customer Gateway** de la conexión **AWS Site-to-Site VPN**. Se configuran dos túneles IPsec redundantes hacia el Virtual Private Gateway en la VPC de AWS: túnel primario sobre el enlace de fibra óptica (D-03) y túnel de respaldo sobre el enlace LTE empresarial (D-04). La conmutación entre túneles es automática mediante BGP. Todo el tráfico de la VPN está cifrado con IKEv2/AES-256, sin puertos entrantes públicos adicionales (modelo Zero Trust).

---

**D-02 — Switch de core con VLANs**

| Criterio | Evaluación |
|---|---|
| Emplazamiento | ON-PREMISE |
| LAT | < 0,1 ms (L2 switching) |
| CRIT | CRITICO — fallo del core switch aísla todos los componentes |
| VOL | Todo el tráfico interno |
| CONN | LAN local — independiente de WAN |
| TCO | Medio — CAPEX en equipo de red |
| HW | No |

Justificación: RT-03.23 exige segmentación por tipo de dispositivo. Las VLANs (IoT, Bodega, Gestión, Servidores) aislan los sensores IoT de la base de datos transaccional, reduciendo superficie de ataque lateral. Un sensor comprometido en VLAN-IoT no puede alcanzar la BD en VLAN-Servidores.

---

**D-03 — Enlace WAN primario (fibra óptica)**

| Criterio | Evaluación |
|---|---|
| Emplazamiento | ON-PREMISE (contrato de conectividad) |
| CRIT | ALTO — camino principal para VPN hacia nube y sincronización |
| VOL | Estimado >= 20 Mbps simétrico por CD |
| CONN | Talca: 4 cortes/año hasta 6 h. Concepción: sin respaldo actual |
| TCO | Contrato mensual |
| HW | No |

Justificación: Camino principal para la VPN (RT-03.21) y el broker de colas (A-03). Durante cortes, el sistema on-premise opera en modo desconectado (RT-03.10). Dimensionamiento: >= 20 Mbps simétrico por CD para peak septiembre (2.600 entregas/día + datos IoT).

---

**D-04 — Enlace WAN de respaldo (LTE empresarial)**
*(Requerido en Talca y en Concepción; proveedor distinto al enlace primario de fibra)*

| Criterio | Evaluación |
|---|---|
| Emplazamiento | ON-PREMISE (contrato de conectividad) |
| CRIT | ALTO — conmutación automática < 30 s declarada; sin respaldo, Concepción queda incomunicada indefinidamente (Cap. 6) |
| VOL | Bajo — solo tráfico crítico (VPN, sincronización esencial del broker A-03) en modo respaldo |
| CONN | Activo automáticamente al fallar el primario; D-01 gestiona el failover y prioriza tráfico (QoS) |
| TCO | Contrato mensual adicional por sitio; bajo costo relativo frente al riesgo de corte total en Concepción |
| HW | No |

Justificación: RT-03.17 / RNF-13.07 exige caminos físicos y proveedores **distintos** con conmutación automática <= 5 min. Talca ya tiene respaldo por red móvil de "capacidad reducida" (Cap. 6) — se debe verificar y reforzar el ancho de banda para soportar la VPN durante el peak de septiembre. **Concepción actualmente no tiene ningún respaldo** de WAN: un corte la deja incomunicada (Cap. 6), violando RNF-13.07.

---

**D-05 — Appliance de Respaldo Local (copia local de recuperación rápida)**
*(copia local para recuperación rápida y restauración sin depender del enlace WAN dentro del esquema único 3-2-1-1-0)*

| Criterio | Evaluación |
|---|---|
| Emplazamiento | ON-PREMISE |
| LAT | N/A (proceso batch en ventana de mantenimiento) |
| CRIT | ALTO — sin copia local, la restauración ante ransomware o fallo catastrófico depende 100% de la nube y del enlace WAN |
| VOL | Alto — respaldo diario completo de la BD transaccional (A-02), broker de colas (A-03), configuraciones y logs de auditoría |
| CONN | Proceso local; no requiere WAN para restaurar (RTO independiente del enlace) |
| TCO | Medio — NAS/appliance con almacenamiento WORM o soporte de Object Lock; capacidad dimensionada para retención de 30 días |
| HW | Sí — NAS dedicado con soporte WORM (Write Once Read Many) o appliance de backup |

Justificación: RNF-20.07 exige la política de respaldo **3-2-1-1-0** bajo un **esquema único declarado en el consolidado de la arquitectura híbrida**: (3 copias) datos activos + snapshot local + backup S3; (2 medios) BD/postgres y S3; (1 fuera de sitio) réplica cross-region en us-east-1; **(1 inmutable)** **S3 Object Lock + Backup Vault Lock en la nube** (ni siquiera el root las elimina); (0 errores) verificación mensual de restauración. **D-05 NO cuenta como la pierna "1 inmutable"** — esa es responsabilidad del Object Lock en la nube; D-05 es la **copia local de recuperación rápida** (con WORM local como refuerzo adicional), que permite restaurar el WMS en <= 4 h (RNF-20.06) sin depender del enlace WAN. RPO <= 15 min mediante streaming del log de PostgreSQL (WAL) hacia la nube antes de la copia local.

---

### BLOQUE E — PLATAFORMAS DE CROSS-DOCKING (Curicó, Chillán, Los Ángeles)

**E-01 — Mini-WMS Edge / Agente operacional de cross-docking**

| Criterio | Evaluación |
|---|---|
| Emplazamiento | ON-PREMISE — gabinete de borde operacional |
| LAT | < 2 s (operación local autónoma) |
| CRIT | CRITICO — ventana operacional de 3 h en la madrugada; un fallo detiene el despacho |
| VOL | Bajo — volumen de una plataforma por noche |
| CONN | Solo red móvil 4G (intermitente) |
| TCO | Bajo — mini-PC industrial rugoso + SSD |
| HW | Sí — scanners GS1 |

Justificación: El nodo actúa como un Mini-WMS con motor de datos ligero embebido (SQLite o PostgreSQL) y broker local (A-03 replicado), capaz de: recibir/validar camión de línea, ejecutar desconsolidación de pallets, validar cadena de frío (B-01), registrar re-despacho y sincronizar transacciones diferidamente.

---

### BLOQUE F — OBSERVABILIDAD Y SEGURIDAD

**F-01 — Agente de observabilidad local**
*(AWS Distro for OpenTelemetry — ADOT — + AWS SSM Agent en cada nodo on-premise)*

| Criterio | Evaluación |
|---|---|
| Emplazamiento | ON-PREMISE (agente) + NUBE (plataforma centralizada: Amazon CloudWatch / Grafana OSS autogestionado en ECS Fargate) |
| CRIT | ALTO — sin él hay puntos ciegos prohibidos por RT-03.16 y RF-16.01 |
| VOL | Moderado — métricas, logs y trazas de todos los nodos on-premise |
| CONN | Envío diferido con buffer en disco local durante cortes; SSM Agent conecta sin puertos entrantes abiertos |
| TCO | Bajo — ADOT y SSM Agent son de código libre / incluidos en AWS |
| HW | No |

Justificación: RF-16.01 y RT-03.16 exigen observabilidad unificada nube + on-premise. **AWS Distro for OpenTelemetry (ADOT)** se instala en cada VM y nodo edge; instrumenta el WMS, BD, broker, gateway IoT y red. Durante la pérdida de enlace, el collector almacena el buffer en disco local y lo envía al recuperar, con exportadores nativos a CloudWatch, X-Ray y Prometheus. El **AWS SSM Agent** permite gestión remota (parches, comandos) sin abrir puertos entrantes (modelo Zero Trust sobre la VPN).

---

**F-02 — Gestión centralizada de parches (Ansible)**

| Criterio | Evaluación |
|---|---|
| Emplazamiento | ON-PREMISE |
| CRIT | MEDIO — incumplimiento genera observación grave (RT-03.15, RNF-13.06) |
| VOL | Bajo — descarga de actualizaciones |
| CONN | Descarga con enlace; aplicación de parches es local |
| TCO | Bajo — herramienta libre (Ansible) |
| HW | No |

Justificación: RT-03.15 / RNF-13.06 exige endurecimiento CIS Benchmarks con gestión centralizada. El SSM Agent (F-01) complementa con el inventario de software actualizado en tiempo real.

---

**F-03 — Agente EDR y Gestión de Endpoints**

| Criterio | Evaluación |
|---|---|
| Emplazamiento | ON-PREMISE (agente en cada endpoint) + NUBE (consola centralizada) |
| CRIT | ALTO — RNF-14.05 exige cobertura EDR 24x7 |
| VOL | Bajo — telemetría de comportamiento |
| CONN | Opera localmente; reporta a consola centralizada vía VPN |
| TCO | Medio — licencias por endpoint |
| HW | No |

Justificación: RNF-14.05 exige EDR en todos los endpoints (servidores WMS, nodo edge Concepción, mini-PCs cross-docking, estaciones de trabajo). RNF-23.04 exige cifrado de disco en estaciones de trabajo, gestionado mediante la política centralizada del agente EDR.

---

## SECCIÓN 2 — RESUMEN EJECUTIVO

| ID | Componente | Veredicto | Criterio dominante |
|---|---|:---:|---|
| A-01 | Motor WMS on-premise | ON-PREMISE | Latencia < 1 s + sin señal cámara |
| A-02 | BD transaccional WMS | ON-PREMISE | Escritura local + RAID 10 |
| A-03 | Broker de colas offline | ON-PREMISE | Encolado + reconciliación |
| A-04 | Capa anticorrupción ERP (frontera) | ON-PREMISE | ERP local + latencia síncrona |
| A-05 | Keycloak Master (IdP on-premise) | ON-PREMISE | Login offline 24 h |
| B-01 | Sensores IoT temperatura | ON-PREMISE | Sin señal + protocolo industrial |
| B-02 | Gateway IoT + Greengrass | ON-PREMISE | Edge computing + buffer |
| B-03 | Termógrafos camión | HIBRIDO | Hardware local + sincro nube |
| C-01 | App preventa offline | HIBRIDO | Lógica local < 1,5 s |
| C-02 | App repartidor offline | HIBRIDO | 14 h sin señal + sincro POD |
| C-03 | Terminales bodega | ON-PREMISE | Sin señal + -22°C |
| C-04 | Impresoras andén | ON-PREMISE | Periférico local |
| D-01 | Firewall/UTM + Cust GW | ON-PREMISE | VPN IPsec + failover WAN |
| D-02 | Switch core con VLANs | ON-PREMISE | Segmentación |
| D-03 | Enlace WAN primario | ON-PREMISE | VPN + sincronización |
| D-04 | Enlace WAN respaldo | ON-PREMISE | Proveedor distinto + failover |
| D-05 | Respaldo local (recuperación rápida) | ON-PREMISE | RNF-20.07 3-2-1-1-0 |
| E-01 | Mini-WMS cross-docking | ON-PREMISE | Ventana 3 h madrugada |
| F-01 | ADOT + SSM Agent | ON-PREMISE | RF-16.01, Zero Trust |
| F-02 | Gestión de parches | ON-PREMISE | RNF-13.06, CIS |
| F-03 | Agente EDR endpoints | ON-PREMISE | RNF-14.05, 24x7 |

**17 ON-PREMISE + 4 HÍBRIDOS = 21 componentes totales**

---

## SECCIÓN 3 — REFERENCIAS CRUZADAS

| Exigencia | Donde se cumple en este documento |
|---|---|
| **Art. 16.2** — Justificación 6 criterios | Columnas LAT/CRIT/VOL/CONN/TCO/HW |
| **RT-03.16 / RF-16.01** — Monitoreo | F-01 (ADOT Collector + SSM Agent) |
| **RT-03.17 / RNF-13.07** — Enlace red. | D-03 (fibra) + D-04 (LTE) + D-01 (VPN IPsec BGP) |
| **RT-03.19** — Procesamiento en borde | B-02 (Greengrass Core) + E-01 (mini-WMS) |
| **RF-15.01 a 15.05** — Identidad | A-05 (Keycloak Master on-premise, réplica en nube) |
| **RNF-13.01** — Autonomía 24 h | A-01, A-02, A-03, A-05, E-01, B-02 |
| **RNF-14.05 / RNF-23.04** — EDR | F-03 (Agente EDR en servidores y estaciones) |
| **RNF-20.07** — Respaldo 3-2-1-1-0 | D-05 (copia local de recuperación rápida) + S3 Object Lock/Vault Lock en nube (pierna inmutable) |

---

## LIMITACIONES CONOCIDAS Y MITIGACIONES

| # | Limitación | Impacto | Mitigación declarada |
|---|---|---|---|
| L-01 | **RabbitMQ on-premise (A-03) sin backup durante outage de WAN.** Si el disco falla mientras la VPN está caída, se pierden mensajes encolados (buffer de hasta 24 h). | Pérdida de eventos de negocio no sincronizados con la nube. | Los eventos críticos usan outbox dual-write → Aurora (ACID) + EventBridge (ver doc cloud). En DRP, se reconstruyen desde `audit_log`. Los mensajes no críticos se re-envían al reconectarse el broker. |
| L-02 | **Concepción y cross-docks: sin D-05 equivalente.** No hay NAS WORM local para recuperación rápida. | Si el nodo falla, la restauración depende exclusivamente de Aurora vía VPN (RTO adicional +1-2 h). | WAN redudante (D-03/D-04). En WAN outage, el nodo opera con su BD embebida local y se sincroniza al recuperar conectividad. |
| L-03 | **WLAN para 120 terminales de picking (C-03): sin failover documentado.** | Si el AP o switch WiFi falla, los terminales quedan incomunicados. | Se asume infraestructura WiFi redundante (APs múltiples con controlador) como parte del dimensionamiento de red del RT-06.01. Confirmar en fase de diseño detallado. |
| L-04 | **App móvil (C-01/C-02): pérdida del dispositivo = pérdida de datos locales.** | Se pierde el POD, firma y cobro del último ciclo de reparto. | La central detecta entregas no confirmadas y las re-asigna. El POD original queda en Aurora (sincronizado previo a la pérdida). Riesgo residual: datos generados después de la última sincronización. |
| L-05 | **On-premise: disponibilidad declarada solo para componentes individuales.** No se declara SLA compuesto del sitio Talca. | El SLA compuesto del sitio on-prem puede ser menor que el de la nube. | El SLA ≥ 99.9% del sistema central se declara para la capa cloud (doc cloud). El on-prem se dimensiona para alta disponibilidad individual (RAID 10, UPS, WAN redundante) pero no se compromete un SLA compuesto del sitio — esto es coherente con la decisión de que la nube asume DRP si Talca cae. |

*Versión 04 — Incorpora requerimientos formales de las Bases Técnicas Transversales: A-05 (Keycloak Master on-premise, IdP maestro, réplica de solo lectura en la nube, RF-15.01–15.05), D-05 (copia local de recuperación rápida, RNF-20.07), F-03 (agente EDR, RNF-14.05/RNF-23.04) y declaración de outputs híbridos de AWS en hardware on-premise (Greengrass Core en B-02, Customer Gateway IPsec en D-01, ADOT+SSM en F-01). Además alinea las costuras de integración con la contraparte cloud: A-04 como frontera única del ERP que la nube atraviesa, A-05 como Keycloak Master (no segundo IdP), A-01/A-02 WMS maestro con réplica/DRP en Aurora, y D-05 desligado de la pierna "1 inmutable" (que vive en S3 Object Lock en nube). Incorpora mecanismo concreto de réplica WAL (AWS DMS CDC) y procedimiento de conmutación Talca→Concepción (DRP local).*
