# Arquitectura Física — Componente On-Premise
## Distribuidora Puelche S.A. — Caso 02 Logística

> **Nota de alcance:** Este documento cubre exclusivamente el segmento **On-Premise** de la arquitectura híbrida exigida por el Artículo 16°. La contraparte AWS es el documento `Propuesta_Arquitectura_Cloud_Caso02_CLAUDE_v2.md`; la integración entre ambos segmentos se definió al consolidar ambas piezas (ver Sección 3 — Referencias Cruzadas y los reencuadres A-04/A-05/A-01/A-02/D-05). 
>
> **Versión 05 — Cambios respecto de la v04:**
> 1. **IdP alineado con la Arquitectura Lógica v1 (D6, 2026-09-04):** A-05 pasa de *"caché offline de Amazon Cognito"* a **Caché local de autenticación del IdP Keycloak (Modelo B de identidad)**. La autoridad única de identidad vive en **Keycloak IdP maestro (ECS/Fargate, nube)**; el componente on-premise es una **caché local de solo lectura con TTL 8 h** para sostener la autonomía 24 h de los CD y los 14 h de terreno (RT-03.10). Cognito queda **descartado como dependencia** (solo alternativa). *Reconciliación resuelta en `Propuesta_Arquitectura_Cloud_Caso02_CLAUDE_v2.md` **v3.6** (Modelo B en §3.3/§3.5/§5.4/§7.3/§7.10/L-02/Apéndice C) y consolidada en `Arquitectura_Fisica_Hibrida_Consolidada_Caso02_v02.md`.*
> 2. **Conteo corregido:** 20 ON-PREMISE + 3 HÍBRIDOS (B-03, C-01, C-02) = 23 componentes totales (la v04 declaraba erróneamente 17 + 4; las filas C-05 Balanza Dibal BEV y D-06 Enlace WAN satelital Starlink se incorporaron en corrección).
> 3. **Dispositivos de terreno definidos** (EC55, TC58e, MC9400 Cold Storage, ZT411, PAX A920 Pro, ZQ620 Plus, Dibal BEV, Onset InTemp CX450, Ebyte ME31 — ver Sección 4).
> 4. **Citas RT verificadas contra el transversal:** A-02 → RT-03.14 (tolerancia a falla de disco / RAID) y D-02 → RT-03.23 (segmentación de red inalámbrica) son **códigos reales** del Cap. 3; se mantienen con la nota de mapeo.
> 5. **Sala de Servidores habilitada como entregable aparte:** diseño físico del recinto de Talca (recintos, energía, clima, PUE, TIER, racks y cableado) en **`Sala_Servidores_OnPremise_v02.md`** (actualizada a v02 conforme a la Matriz de Cumplimiento). El detalle de hardware está en **`Dimensionamiento_Infraestructura_OnPremise_v05.md`**.
>
> **Versión 06 — Cambios respecto de la v05:**
> 1. **RT-03.13 declarado (Sección 1.1):** matriz de funciones NO disponibles en modo desconectado con el procedimiento manual que las suple (la omisión se evalúa como observación grave — RT-03.13 OBL).
> 2. **RT-08.10 cumplido (Sección 4):** costo unitario estimado (USD referenciales) incorporado para cada dispositivo de terreno, completando marca, modelo, cantidad, características mínimas, accesorios y consumibles.
> 3. **RT-08.13 y §8.4 cumplidos (Secciones 4.1 y 4.2):** ciclo de vida esperado por dispositivo, disponibilidad de repuestos y plan de reposición durante los 56 meses; garantías y niveles de reemplazo (soporte 24×7 con resolución en sitio ≤ 4 h para hardware crítico, 24 h horario hábil para no crítico, stock de repuestos ≥ 10 % del parque por tipo de componente crítico en Chile, reemplazo de componente crítico ≤ 4 h, y stock de reemplazo en sitio = 10 % del parque de terreno con configuración precargada).
> 4. **Referencias cruzadas actualizadas:** Sala_Servidores_OnPremise_v02 y Dimensionamiento_Infraestructura_OnPremise_v05 en todo el documento.
>
> **Versión 06c — Cierre de pendientes (alcance arquitectura física on-premise):**
> 1. **RT-06.26 (custodia de medios de respaldo del sitio primario)** cumplido en **D-05**: se declara el **servicio de custodia de medios en un medio físico transportable a otro lugar** cuando el CLIENTE lo determine, complementaria (no sustituida) por la pierna inmutable S3 — detalle en Tabla v06 D-05 y Sala v02 §4.5.
> 2. **RT-06.27 (condiciones ambientales del recinto de custodia)** cumplido en **Sala v02** (§4.5, recinto de 10 m²): luminosidad LED sin UV, humedad 40–60 %, ventilación forzada y 18–27 °C.
> 3. **RT-08.15 (unidad de muestra por tipo de dispositivo para pruebas de aceptación del CLIENTE)** cumplido en **Sección 4.3** de este documento: 1 unidad de cada tipo de dispositivo, sin cargo, para pruebas de aceptación antes de la compra masiva.

---

## SECCIÓN 1 — TABLA DE EMPLAZAMIENTO

*Justificación componente por componente conforme al Artículo 16°, numeral 16.2, y al capítulo 3.1 de las Bases Técnicas Transversales.*

### Sección 1.1 — Funciones NO disponibles en modo desconectado (RT-03.13)

*RT-03.13 (OBL): el PROPONENTE declara qué funciones NO estarán disponibles en modo desconectado y qué procedimiento manual las suple. La matriz distingue autonomía nominal (2 h, Cap. 6/8) de contingencia de diseño (14 h terreno, 24 h CD — RT-03.10/RNF-13.01).*

| Función / componente | Disponible desconectado | NO disponible en modo desconectado (RT-03.13) | Procedimiento manual que la suple |
|---|---|---|---|
| **Preventa (C-01)** | Toma de pedido, precios y crédito cacheados, ID único offline, deduplicación (RF-03.16/17) | Validación de crédito en tiempo real contra backend, promociones/precios recién publicados en nube, consulta de stock global | El preventista emplea la lista de precios y saldo de crédito del caché del turno (TTL 8 h, A-05); pedido sobre saldo cacheado → coordinación telefónica con oficina de crédito con evento en bitácora; al reconectar el sistema valida y marca discrepancias para revisión (RF-03.17) |
| **Reparto y cobranza (C-02)** | Entrega, POD (foto firma), devoluciones, cobro en efectivo, actualización local de ruta | Autorización de tarjeta en línea (auth de la pasarela) y validación antifraude; preconciliación en nube | El POS captura la transacción como *pending* para autorización diferida al reconectar; si no procede, cobro en efectivo o giro a crédito con firma del cliente y nota de envío manual; conciliación en base al reconectar (RNF-07.01 ≤ 10 min) |
| **WMS bodega (A-01/A-02)** | Recepción, preparación, despacho, conteo cíclico y trazabilidad local contra BD local (RT-03.10/03.11) | Sincronización con ERP maestro (A-04), maestro de productos recién actualizado desde nube, BI/dashboards cloud | Cambios de maestro se aplican al reconectar con reconciliación determinista de stock (RT-03.12); si la dirección lo exige durante la contingencia, se lleva reporte manual de operación en planilla (caso extremo documentado) |
| **Autenticación (A-05)** | Login/SSO offline con caché TTL 8 h (validación local de firma OIDC) | Alta/baja de usuarios, cambio de roles/permisos, reset de contraseña, re-registro MFA, OTP nuevo para externos | El administrador local habilita acceso temporal de emergencia registrado en bitácora; altas/bajas y roles se sincronizan desde Keycloak al recuperar el enlace (RF-15.05 ≤ 24 h) |
| **Cadena de frío (B-01/B-02)** | Lectura continua cada 30 s, detección de excursión y bloqueo de despacho 100 % local, buffer offline 14 h | Alerta externa (SMS/email a la Autoridad Sanitaria) y telegestión remota desde nube | La excursión la decide el sistema local (alarma acústica/luz y sensor RT-06.14 en el NOC) y el Jefe de TI on-call 24×7; el bloqueo de despacho es local y no depende de la alerta remota |
| **Observabilidad (F-01)** | Métricas, logs y trazas bufferizadas en disco durante el corte | Dashboards centralizados en nube (CloudWatch/AMP) durante el corte | El NOC on-premise (Prometheus/Grafana/Loki local) mantiene la vista completa; el envío diferido cierra el hueco al reconectar (RT-03.16) |
| **Cross-docking (E-01)** | Ventana de 3 h 100 % local: recepción, desconsolidación, validación de frío, re-despacho | Visibilidad global en nube, planificación central de rutas, sincronización con WMS maestro (diferida) | Operación según papeleta generada al inicio del turno; sincronización diferida al reconectar con reconciliación (RT-03.11) |

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
| LAT | ≤ 1 s (RNF-05.01) — inviable con latencia de red remota (40–80 ms mínimo hacia nube) |
| CRIT | CRITICO — "si el sistema se cae entre las 5:30 y las 7:00, ese día no hay operación" (Cap. 8, Nelson) |
| VOL | Alto — 260.000 líneas/mes, 2,4M unidades/mes, 11.400 posiciones (Talca) + 9.000 m² (Concepción) |
| CONN | Talca: cortes 4x/año hasta 6 h; cámara congelado sin señal. Concepción: sin respaldo WAN actual (Cap. 6) |
| TCO | CAPEX requerido — la sala actual de Talca (25 m², split AC, UPS 10 min) NO cumple las Bases (Cap. 6, Caso 02). Se requiere habilitación de Sala Técnica Secundaria en Talca (ver Sala_Servidores_OnPremise_v02) y nodo edge local en Concepción |
| HW | Sí — terminales GS1 (C-03), impresoras (C-04), balanza (C-05), clúster de 3 nodos (Dimensionamiento v05) |
Justificación: El turno de picking nocturno (22:00–06:00) involucra 120 personas. RNF-05.01 exige ≤ 1 s de respuesta incluso en la cámara de congelado a -22°C donde no existe señal de red (Cap. 6). La latencia mínima de ida y vuelta hacia la nube (40–80 ms con fibra en buen estado) más el procesamiento remoto viola el umbral de 1 s. La operación desconectada mínima de 24 h (RT-03.10, RNF-02.01) no puede delegarse a un WMS alojado exclusivamente en nube.
**Relación con el WMS en nube (Aurora):** Este WMS on-premise es el **maestro de la operación de bodega** (recepción, preparación, despacho) y la única instancia que garantiza la autonomía de 24 h (RT-03.10). La capa **Aurora PostgreSQL en la nube NO duplica ni sustituye al WMS**: actúa como **réplica de continuidad/DRP** de este WMS y como OLTP de los procesos que sí corren en nube (preventa, reparto, BI). El flujo bodega↔nube se sincroniza vía el broker A-03 y la VPN, garantizando que si Talca cae, la nube mantiene la última imagen del WMS para recuperación (ver DRP on-premise→nube y la prueba DR semestral en Dimensionamiento v05 §1.2.4).
**Tipología de sitios declarada (Cap. 6.1, Bases Técnicas Transversales; RT-06.01 del caso):**
- **CD Talca:** Sala Técnica Secundaria — cómputo, almacenamiento y telecomunicaciones sustantivos. La sala actual de 25 m² NO cumple el Cap. 6; se habilitará el recinto según **Sala_Servidores_OnPremise_v02** (RT-06.01 a RT-06.24 aplican proporcionalmente a la tipología).
- **CD Concepción:** Gabinete de Borde Operacional — instancia WMS edge + switch + firewall + **enlaces fibra (D-03) + Starlink respaldo (D-06) + LTE (D-04) satelital/terrestre**. Garantiza 24 h de autonomía independiente de Talca.
- **Plataformas Cross-Docking (Curicó, Chillán, Los Ángeles):** Gabinete de Borde Operacional (ver E-01) con **enlace Starlink principal (D-06) + LTE dual respaldo (2 proveedores)** (RT-03.17).

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

Justificación: RT-03.11 exige registro continuo sin pérdida en desconectado. **RT-03.14** (código real del Cap. 3 del transversal) exige tolerancia a falla de al menos un disco; la declaración del nivel RAID se hace en el Dimensionamiento v05 §1.2.2 (**RAID 10 + Hot-Spare**; se descartan RAID 5/6 sin paridad de escritura). Esta BD local es el "sistema de verdad" de bodega durante la desconexión; su **réplica de DRP vive en Aurora (nube)** (ver A-01), la cual se mantiene al día vía streaming del log WAL a través de la VPN (RPO ≤ 15 min).
**Esquema físico de almacenamiento aprobado:**
| Capa | RAID | Discos | Descripción |
|---|---|---|---|
| SO + Hipervisor | RAID 1 (espejo) | 2 × SSD 480 GB | Tolera caída de 1 disco; arranque del sistema sin intervención |
| Storage de datos WMS + BD | RAID 10 (espejo + franjas) + Hot-Spare | 4 × SSD NVMe 1,92 TB + 1 Hot-Spare | Tolera caída de 1 disco por par espejado; Hot-Spare reconstruye automáticamente; lectura paralela en franjas para 120 terminales simultáneos |
**Replicación de datos a nivel de clúster:** los volúmenes de datos se replican **de forma síncrona entre los 3 nodos** del clúster Proxmox (Ceph, factor de replicación 2 con quórum real de 3 nodos — **ya no 2 nodos más QDevice**), eliminando el SPOF de un par sin quórum (ver Dimensionamiento v05 §1.2.5).

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

Justificación: El ERP de 2017 (sistema de gestión) no tiene documentación técnica de interfaces (Cap. 5) y es el registro contable/tributario que **no se modifica ni se reemplaza** (Cap. 10). La ACL (RT-02.14, RT-05.20) aísla el modelo interno del WMS y de la nube del modelo del ERP, evitando que un cambio en el ERP propague su modelo al núcleo de la solución. Se despliega on-premise **como frontera única de acceso al ERP** porque: (1) el ERP vive on-premise en Talca; (2) latencia de llamadas síncrona nube-a-oficina supera los 50 ms; (3) en modo desconectado la ACL encola las transacciones hacia el ERP sin pérdida (RF-01.09); y (4) concentra el acceso desde la nube: **el microservicio cloud `svc-erp-integration` atraviesa la VPN y llega al ERP únicamente vía esta ACL**, nunca directamente, preservando el no-intervención del Cap. 10 y la única vía documentada (contrato OpenAPI en la ACL).

---

**A-05 — Caché Local de Autenticación — IdP Keycloak (Modelo B)**
*(caché offline de solo lectura del IdP **Keycloak** para autenticación y SSO durante cortes de WAN — no un segundo IdP; autoridad única en nube)*

| Criterio | Evaluación |
|---|---|
| Emplazamiento | ON-PREMISE (VM-05 en Talca; réplica solo lectura en VM-C03 Concepción) |
| LAT | < 200 ms (validación de firma y sesión local) |
| CRIT | CRITICO — sin él, los 120 operarios de picking no pueden hacer login durante un corte de WAN, deteniendo la operación nocturna |
| VOL | Bajo — tokens JWT y caché de identidades (texto compacto) |
| CONN | Funciona sin WAN (TTL 8 h = turno nocturno completo); sincroniza altas/bajas y roles al recuperar el enlace |
| TCO | Bajo — caché offline del IdP **Keycloak** (open source, sin costo de licencia de identidad); VM en el hipervisor de Talca y réplica en Concepción |
| HW | No |

Justificación: **D6 de la Arquitectura Lógica v1 (2026-09-04)**: Keycloak es el IdP maestro (ECS/Fargate, nube) con perfiles por actor; Cognito queda **solo como alternativa**, no como dependencia. RF-15.01 exige gestión de identidad centralizada con federación OIDC/OAuth 2.1; RF-15.02 SSO; RF-15.03 MFA; RF-15.04 RBAC; RF-15.05 aprovisionamiento/desaprovisionamiento en ≤ 24 h. **Modelo B de identidad: autoridad única en nube + caché local on-prem TTL 8 h** (RT-03.10: 24 h CD · 14 h terreno). El proxy local valida la firma de los tokens emitidos por Keycloak, emite credenciales de sesión de corta vida (RNF-15.02) y registra el ciclo de vida de la identidad localmente (RNF-15.03). La autoridad última de alta/baja y roles sigue en Keycloak (nube); la caché es de **solo lectura** con TTL 8 h y se re-sincroniza al recuperar el enlace. El OTP para conductores externos (RF-06.08) también se sirve desde Keycloak, con caché local para verificación offline del turno.

---

### BLOQUE B — CADENA DE FRÍO E IoT

**B-01 — Sensores IoT de temperatura (cámaras −22 °C)**
*(Módulos Ebyte ME31-XDXX0400 — 7 módulos × 4 canales PT100 2/3 hilos, exactitud ±0,5 % ± 1 °C (≈ ±1,1 °C a −22 °C), protocolo RS-485/Modbus RTU + Modbus TCP, 28 puntos de medición)*

| Criterio | Evaluación |
|---|---|
| Emplazamiento | ON-PREMISE (hardware en sitio) |
| LAT | < 1 s (tiempo real vía Modbus RTU) |
| CRIT | CRITICO — pérdida de $21M por no demostrar cadena de frío (Cap. 7.3) |
| VOL | Alto — lectura cada 30 s × ~28 puntos (Talca + Concepción) |
| CONN | Cámara congelado sin señal Wi-Fi ni móvil — estructura metálica bloquea (Cap. 6); red industrial cableada RS-485 independiente de la WAN |
| TCO | Bajo — CAPEX en sensores; sin egress cost |
| HW | Sí — 7 × Ebyte ME31-XDXX0400 (4 canales PT100 2/3 hilos por módulo, riel DIN, −40…+85 °C, 1 Hz) |

Justificación: La Autoridad Sanitaria observó la ausencia total de registro continuo (Cap. 7.3). La cámara de congelado bloquea toda señal inalámbrica. Los sensores se comunican en **red industrial cableada RS-485/Modbus RTU** (28 puntos ≈ 7 módulos de 4 canales, sonda 3 hilos), independiente de la WAN. El rechazo de un camión completo por sospecha de ruptura ($21M, Cap. 7.3) confirma que la lectura debe ser local e inmediata. **Sonda 3 hilos con compensación de cable y exactitud ≈ ±1,1 °C a −22 °C para que la regla de excursión (magnitud + duración) sea defendible ante la Autoridad Sanitaria.** La telegestión y la alerta de excursión térmica se integran al Gateway B-02 y al WMS (bloqueo de despacho).

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
| HW | Sí — RS-485, Modbus RTU (maestro sobre los módulos Ebyte B-01), protocolos industriales |

Justificación: RT-03.19 valora el procesamiento en el borde. El concentrador ejecuta: (a) ingesta de lecturas en tiempo real, (b) detección de excursiones con umbral configurable, (c) alerta local inmediata al WMS para bloquear despacho, (d) persistencia local durante cortes (14 h, RNF-09.04), (e) sincronización diferida al data lake en nube al recuperar. El runtime **AWS IoT Greengrass Core** se instala en el dispositivo edge, lo que permite ejecutar funciones Lambda locales para el procesamiento de telemetría sin depender del enlace WAN. En la cámara de congelado a -22°C, donde no existe señal (Cap. 6), Greengrass mantiene la lógica de detección de excursiones y el buffer de datos de forma completamente offline. Al recuperar la WAN, sincroniza automáticamente con AWS IoT Core en nube.

---

**B-03 — Termógrafos digitales de camión**
*(Onset InTemp CX450 — BLE, −30…+70 °C ±0,5 °C, registro NIST 2 puntos, apto GDP/GMP, reutilizable)*

| Criterio | Evaluación |
|---|---|
| Emplazamiento | HIBRIDO (hardware local en camión + sincronización a nube) |
| LAT | Tiempo real (almacenado localmente en el sensor) |
| CRIT | CRITICO durante el viaje (18 camiones con equipo de frío) |
| VOL | Moderado — 1 log/min × 18 camiones → ~103.400 mediciones por unidad |
| CONN | Rutas rurales sin cobertura hasta 2 h; sincroniza vía BLE al dispositivo del conductor y por Gateway al volver a base (RNF-09.04) |
| TCO | Bajo — CAPEX en dispositivos certificados NIST, reutilizables |
| HW | Sí — sensor embebido, BLE, registro automático, acreditación GDP/GMP |

Justificación: El termógrafo registra la cadena de temperatura a bordo y sincroniza vía BLE con el terminal del conductor (TC58e) y, al regresar a base, con el Gateway IoT (B-02) como respaldo. La evidencia es auditable (NIST) y cumple los requisitos de la Autoridad Sanitaria (Cap. 7.3).

---

### BLOQUE C — DISPOSITIVOS DE OPERACIÓN EN TERRENO

**C-01 — App de Preventa (mobile offline-first) sobre terminal Zebra EC55**

| Criterio | Evaluación |
|---|---|
| Emplazamiento | HIBRIDO (app local en dispositivo + backend en nube) |
| LAT | ≤ 1,5 s por línea (RNF-03-01) — ejecutado localmente |
| CRIT | CRITICO — 62 preventistas, 31.000 pedidos/mes |
| VOL | Bajo — sincronización de pedidos en texto estructurado |
| CONN | Hasta 2 h sin señal en rutas rurales (Cap. 6) |
| TCO | Bajo OPEX — app móvil; CAPEX en terminal **Zebra EC55** (173 g; IP67; −10…+50 °C; lector 2D SE4100; batería 4.180 mAh; Android 14 con 8 años de soporte LifeGuard) |
| HW | Sí — cámara (RF-01.04), lector 2D SE4100 para lectura GS1 |

Justificación: La lógica de toma de pedido, validación de crédito cacheado, cálculo de promociones y generación de ID único offline (RF-03.16) se ejecutan localmente para cumplir ≤ 1,5 s sin importar la cobertura. Los pedidos offline se encolan con deduplicación automática al sincronizar (RF-03.17). El backend de validación en tiempo real está en nube.

---

**C-02 — App del Repartidor/Conductor (mobile offline-first) sobre Zebra TC58e + impresora ZQ620 Plus + POS PAX A920 Pro**

| Criterio | Evaluación |
|---|---|
| Emplazamiento | HIBRIDO — ejecución y persistencia 100% offline en dispositivo (hasta 14 h); ingesta, conciliación de POD y sincronización con ERP en backend Cloud |
| LAT | Inmediata — toda la lógica de entrega se ejecuta localmente; no depende de señal |
| CRIT | CRITICO — 1.400 entregas/día; ventana de despacho 05:30–07:00 no admite dependencia de red |
| VOL | Bajo en ruta — POD (foto firma), registros de entrega, cobro efectivo; Alto al sincronizar (acumulado 14 h) |
| CONN | Rutas rurales hasta 2 h sin señal; rutas completas recuperan cobertura solo al regresar a base (Cap. 6, 8) |
| TCO | Bajo OPEX — app móvil; CAPEX en **Zebra TC58e** (5G; SE55; batería ext. 7.000 mAh; BT 5.3 + BLE secundario; GPS dual L1/L5; IP65/68; caídas 2,4 m; Android 13→17) para conductores propios y pool de externos (parque único) |
| HW | Sí — cámara para firma POD digital, GPS dual, BLE para sincronización con termógrafo (B-03) y movilidad **impresora térmica de cabina Zebra ZQ620 Plus** (Link-OS, IP54) + **POS móvil Bluetooth PAX A920 Pro** (PCI PTS 7.x, EMV L1/L2, Android 14, impresora integrada 80 mm/s) para cobranza con tarjeta (RF-07.06) |

Justificación: RNF-06.02 exige persistir 100% de datos durante mínimo 14 h sin señal. El cobro en efectivo (38% canal tradicional, Cap. 4.7) no puede depender de conexión en ningún momento de la ruta. La app almacena localmente en SQLite cifrado: secuencia de entrega, estado de cada parada, foto de firma POD, devoluciones, cobro en efectivo y lecturas del termógrafo. Al ingresar a zona con cobertura (o al regresar a base), sincroniza automáticamente con el backend Cloud para conciliación de POD (RF-02.06). RNF-07.01 exige consolidación de cobranzas en ≤ 10 min tras conectar a red. El POS PAX A920 Pro cubre RF-07.06 (cobro con tarjeta en ruta) con acreditación PCI PTS 7.x.

---

**C-03 — Terminales rugosos de bodega (picking) — Zebra MC9400 Cold Storage (Freezer)**

| Criterio | Evaluación |
|---|---|
| Emplazamiento | ON-PREMISE (conectado a WMS local) |
| LAT | ≤ 1 s (RNF-05.01) — online y offline, incluida cámara |
| CRIT | CRITICO — picking nocturno 120 personas, 38% rotación anual |
| VOL | Alto — 260.000 líneas/mes generadas localmente |
| CONN | Cámara congelado sin señal (Cap. 6); bodega general: Wi-Fi 6E local |
| TCO | Bajo — hardware industrial certificado para congelado, vida útil 5–7 años |
| HW | Sí — **Zebra MC9400 Cold Storage (modelo Freezer)**; −30 °C; lector SE58 de rango extendido (~100 pies); batería freezer 5.000 mAh; pistol grip para operación con guantes; Android 13→18; Wi-Fi 6E + BT 5.3; cumple RNF-05.02 y RT-08.14 |

Justificación: RNF-05.02 exige pantalla operable con guantes térmicos (elementos ≥ 15×15 mm), funcionalidad 30 min a -22°C. Los dispositivos de consumo masivo fallan a esa temperatura (Cap. 8, Ximena). El MC9400 Cold Storage está certificado para cámara frigorífica (−30 °C), con pistol grip y lector de rango extendido que reduce devoluciones de escaneo con guantes gruesos. Operan offline contra el WMS local durante la sesión en cámara; sincronizan al salir. RNF-05.03: curva de aprendizaje ≤ 2 h.

---

**C-04 — Impresoras térmicas de andén — Zebra ZT411**

| Criterio | Evaluación |
|---|---|
| Emplazamiento | ON-PREMISE |
| LAT | Inmediata — el recepcionista espera la etiqueta para continuar |
| CRIT | MEDIO-ALTO — bloquea cierre de recepción si falla |
| VOL | Bajo — etiquetas de código de barras |
| CONN | LAN de bodega local |
| TCO | Bajo — hardware periférico |
| HW | Sí — **Zebra ZT411** (203 dpi, 14 ips; ZPL II + XML-Enabled Printing; Ethernet; Print DNA) |

Justificación: RF-01.07 exige generar e imprimir la etiqueta SSCC al finalizar el registro del pallet con GTIN (AI 01), lote (AI 10), vencimiento (AI 17) y fecha de recepción (AI 11). Depender de la nube introduciría latencia inaceptable y fallaría durante cortes de enlace.

---

**C-05 — Balanza de recepción en andén — Dibal BEV**

| Criterio | Evaluación |
|---|---|
| Emplazamiento | ON-PREMISE |
| LAT | Inmediata — pesaje al ingreso del pallet |
| CRIT | MEDIO — evidencia de recepción (RF-01.01) y verificación de merma |
| VOL | Bajo — lecturas de peso por pallet |
| CONN | LAN de bodega local (Ethernet opcional) |
| TCO | Bajo — balanza industrial |
| HW | Sí — **Dibal BEV** (plataforma ME + indicador DMI-610 Inox; doble RS-232, Ethernet opcional, RS-485/422; 6.000 divisiones) |

Justificación: El pesaje de recepción se integra al Módulo M1 (RF-01.01) para validar unidades vs OC y detectar mermas. La integración local (doble RS-232 / Ethernet) permite captura automática sin digitación manual.

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
| CONN | **SD-WAN multi-WAN**: gestiona el failover automático entre **fibra (D-03) → Starlink (D-06) → LTE (D-04)** con conmutación < 30 s (RT-03.17, RNF-13.07) |
| TCO | CAPEX nuevo — la sala actual de Talca (25 m², acceso por llave) no cumple RT-06.20 (biometría facial) ni RT-06.16 (detección AnaLASER). Adecuación física en Sala_Servidores_OnPremise_v02 |
| HW | No (dispositivo inline de red) |

Justificación: RT-03.17 / RNF-13.07 exige enlace redundante con caminos físicos y proveedores distintos y conmutación automática ≤ 5 min (en este caso < 30 s). El firewall gestiona las zonas de red (pública, DMZ, aplicación, datos, gestión), controla el failover WAN y cifra el túnel VPN/IPsec hacia la nube. El firewall actúa como **Customer Gateway** de la conexión **AWS Site-to-Site VPN**. Se configuran túneles IPsec redundantes hacia el Virtual Private Gateway en la VPC de AWS: túnel primario sobre el enlace de fibra óptica (D-03) y túnel secundario sobre el **enlace satelital Starlink (D-06)**; un tercer camino LTE (D-04) queda disponible como alterno vía **SD-WAN multi-WAN** (3 tecnologías/proveedores distintos). La conmutación entre caminos es automática mediante BGP/BFD. Todo el tráfico de la VPN está cifrado con IKEv2/AES-256, sin puertos entrantes públicos adicionales (modelo Zero Trust).

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

Justificación: **RT-03.23** (código real del Cap. 3 del transversal — red inalámbrica y segmentación por tipo de dispositivo) exige segmentación. Las VLANs (IoT, Bodega, Gestión, Servidores) aíslan los sensores IoT de la base de datos transaccional, reduciendo superficie de ataque lateral. Un sensor comprometido en VLAN-IoT no puede alcanzar la BD en VLAN-Servidores.

---

**D-03 — Enlace WAN primario (fibra óptica)**

| Criterio | Evaluación |
|---|---|
| Emplazamiento | ON-PREMISE (contrato de conectividad) |
| CRIT | ALTO — camino principal para VPN hacia nube y sincronización |
| VOL | Estimado ≥ 20 Mbps simétrico por CD |
| CONN | Talca: 4 cortes/año hasta 6 h (respaldo por **Starlink D-06**). Concepción: respaldo satelital **D-06** incorporado |
| TCO | Contrato mensual |
| HW | No |

Justificación: Camino principal para la VPN (RT-03.21) y el broker de colas (A-03). Durante cortes, el sistema on-premise opera en modo desconectado (RT-03.10). Dimensionamiento: ≥ 20 Mbps simétrico por CD para peak septiembre (2.600 entregas/día + datos IoT).

---

**D-04 — Enlace WAN de respaldo/móvil (LTE empresarial)**
*(En Talca y Concepción: camino terciario tras fibra D-03 y satelital D-06; proveedor distinto al enlace primario de fibra; en plataformas cross-docking: LTE dual con 2 proveedores, respaldo del satelital principal)*

| Criterio | Evaluación |
|---|---|
| Emplazamiento | ON-PREMISE (contrato de conectividad) |
| CRIT | ALTO — conmutación automática < 30 s; en Concepción sujeto a que falle también el satelital D-06 |
| VOL | Bajo — solo tráfico crítico (VPN, sincronización esencial del broker A-03) en modo respaldo |
| CONN | Activo automáticamente al fallar los caminos D-03/D-06; D-01 gestiona el failover y prioriza tráfico (QoS) |
| TCO | Contrato mensual adicional por sitio; bajo costo relativo frente al riesgo de corte total |
| HW | No |

Justificación: RT-03.17 / RNF-13.07 exige caminos físicos y proveedores **distintos** con conmutación automática ≤ 5 min. En los CDs el LTE (D-04) refuerza el respaldo **satelital Starlink (D-06)** como tercer camino (misma tecnología de enlace distinta a fibra y a satélite), de modo que **Concepción deja de estar sin respaldo** (Cap. 6): el hueco declarado "nuevo enlace requerido" en Dimensionamiento v05 §3.7 queda cubierto por D-06; el LTE permanece como camino alterno de red móvil. **Plataformas cross-docking (E-01):** el **LTE dual con 2 proveedores distintos** pasa a ser el **respaldo automático** del enlace satelital principal (D-06), satisfaciendo RT-03.17 incluso donde solo existía red móvil (justificación formal en Dimensionamiento v05 §1.4).

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
| TCO | Medio — NAS/appliance con almacenamiento WORM o soporte de Object Lock; retención 30 días |
| HW | Sí — NAS dedicado con soporte WORM, dimensionado en Dimensionamiento v05 §1.2.4 |

Justificación: RNF-20.07 exige la política de respaldo **3-2-1-1-0** bajo un **esquema único declarado en el consolidado de la arquitectura híbrida**: (3 copias) datos activos + snapshot local + backup S3; (2 medios) BD/postgres y S3; (1 fuera de sitio) réplica cross-region en us-east-1; **(1 inmutable)** **S3 Object Lock + Backup Vault Lock en la nube** (ni siquiera el root las elimina); (0 errores) verificación mensual de restauración **más prueba DR semestral declarada** (Valor: RT-06.10 del transversal y Art. 20 de las Bases Administrativas). **D-05 NO cuenta como la pierna "1 inmutable"** — esa es responsabilidad del Object Lock en la nube; D-05 es la **copia local de recuperación rápida** (con WORM local como refuerzo adicional), que permite restaurar el WMS en ≤ 4 h (RNF-20.06) sin depender del enlace WAN. RPO ≤ 15 min mediante streaming del log de PostgreSQL (WAL) hacia la nube antes de la copia local.

**RT-06.26 — custodia de medios de respaldo del sitio primario (servicio de custodia y transporte físico):** la pierna S3/Aurora **no basta**; sobre D-05 se declara el **servicio de custodia de los medios de respaldo del sitio primario en un medio físico transportable a otro lugar cuando el CLIENTE lo determine**. La copia de D-05 se materializa además en un **medio físico transportable cifrado** (disco extraíble/nube local, conforme RT-07.10/RT-11.09) que rota semanalmente (RT-06.28) y se traslada desde el recinto de custodia de la Sala (Sala v02 §4.5) hacia una **bóveda de custodia externa** (otro lugar geográfico) mediante **servicio de custodia/transporte acreditado**, con cadena de custodia y bitácora de entrada/salida (RT-06.28). El **recinto de custodia de 10 m²** cumple las condiciones ambientales del **RT-06.27** (luminosidad LED sin UV, humedad 40–60 %, ventilación forzada, 18–27 °C). La pierna inmutable S3 (Object Lock) es complementaria y no reemplaza este medio físico transportable.

---

**D-06 — Enlace WAN satelital (Starlink Enterprise fijo) — NUEVO**
*(Respaldo automático de los CDs Talca y Concepción; enlace principal de las 3 plataformas de cross-docking; 5 kits — Cotización Starlink 56 meses, 05-09-2026)*

| Criterio | Evaluación |
|---|---|
| Emplazamiento | ON-PREMISE — antena en techumbre + router dentro del recinto/gabinete (contrato de conectividad Starlink Enterprise) |
| CRIT | ALTO — en los cross-docks es el **enlace principal** (resuelve la intermitencia de señal móvil de Los Ángeles entre 03:00–05:00, exactamente su ventana operacional); en los CDs el respaldo automático de la fibra |
| VOL | Medio — plan priorizado: **1 TB/mes (CDs)** y **500 GB/mes (cross-docks)**, tráfico de sincronización VPN/broker/SSM/telemetría |
| CONN | **Conmutación automática < 30 s en CDs** (SD-WAN/BGP: fibra → Starlink → LTE); en cross-docks conmutación automática a **LTE dual** (RT-03.17). MTU túnel 1.436 bytes |
| TCO | CAPEX de 5 kits (reposición de hardware 15 % / 56 meses, RT-08.13) + plan mensual de 56 meses (cotización adjunta) |
| HW | Sí — 5 kits Starlink Enterprise fijos (dish + router), 1 por sitio |

Justificación: RT-03.17 / RNF-13.07 exige **caminos físicos y proveedores distintos**. Un camino satelital (Starlink) es físicamente independiente de la infraestructura terrestre/móvil y de los cables submarinos regionales, lo que aporta una tercera tecnología a los CDs (fibra → **satelital** → LTE) y **el** enlace principal estable donde solo existía red móvil intermitente (cross-docks; Los Ángeles pierde señal 03:00–05:00). Con D-06 queda **cerrada la brecha de Concepción registrada en v05 §3.7** ("nuevo enlace requerido" bajo RNF-13.07) y el SPOF de enlace declarado en §4. Se energiza desde PDU-B/UPS (Sala v02 §5.2) y en cross-docks desde la mini-UPS del gabinete (RT-06.07). Antena en techumbre con ingreso por canalización protegida hasta la MMR (RT-06.32). Detalle de ancho de banda y failover en Dimensionamiento v05 §3.6/§3.7.

---

### BLOQUE E — PLATAFORMAS DE CROSS-DOCKING (Curicó, Chillán, Los Ángeles)

**E-01 — Mini-WMS Edge / Agente operacional de cross-docking + escáner GS1 (Zebra DS2208)**

| Criterio | Evaluación |
|---|---|
| Emplazamiento | ON-PREMISE — gabinete de borde operacional |
| LAT | < 2 s (operación local autónoma) |
| CRIT | CRITICO — ventana operacional de 3 h en la madrugada; un fallo detiene el despacho |
| VOL | Bajo — volumen de una plataforma por noche |
| CONN | **Starlink principal (D-06)** + **LTE dual respaldo (2 proveedores)** — sincronización diferida; operación 100% local en ventana de 3 h (RT-03.10) |
| TCO | Bajo — mini-PC industrial rugoso + SSD |
| HW | Sí — **escáner de mano GS1 Zebra DS2208** (1D/2D + GS1 DataBar; PRZM; USB/RS-232/KBW; garantía 60 meses) ×2 por plataforma |

Justificación: El nodo actúa como un Mini-WMS con motor de datos ligero embebido (SQLite o PostgreSQL) y broker local (A-03 replicado), capaz de: recibir/validar camión de línea, ejecutar desconsolidación de pallets, validar cadena de frío (B-01), registrar re-despacho y sincronizar transacciones diferidamente. **El enlace satelital Starlink (D-06) pasa a ser el enlace principal** del cross-dock: satisface RT-03.17 (caminos/proveedores distintos) y elimina la dependencia exclusiva de la red móvil, **intermitente en Los Ángeles entre 03:00–05:00** (justo la ventana operacional); el **LTE dual (2 proveedores) del módulo 4G Cat-12** del mini-PC queda como respaldo automático (ver D-04/D-06). La ventana operacional de 3 h no depende del enlace (RT-03.10 + RT-03.11 local).

---

### BLOQUE F — OBSERVABILIDAD Y SEGURIDAD

**F-01 — Agente de observabilidad local**
*(OpenTelemetry Collector — ADOT — + AWS SSM Agent en cada nodo on-premise; Capa 8 de la Arquitectura Lógica v1)*

| Criterio | Evaluación |
|---|---|
| Emplazamiento | ON-PREMISE (agente) + NUBE (plataforma centralizada: Prometheus/Grafana/Loki on-prem + CloudWatch / X-Ray / AMP en nube) |
| CRIT | ALTO — sin él hay puntos ciegos prohibidos por RT-03.16 y RF-16.01 |
| VOL | Moderado — métricas, logs y trazas de todos los nodos on-premise |
| CONN | Buffer en disco local durante cortes; envío diferido; SSM Agent conecta sin puertos entrantes abiertos (Zero Trust) |
| TCO | Bajo — ADOT y SSM Agent son abiertos / incluidos en AWS |
| HW | No |

Justificación: **D9 (Arquitectura Lógica v1)** y RF-16.01/RT-03.16 exigen observabilidad unificada nube + on-premise sobre **OpenTelemetry**. **ADOT (AWS Distro for OpenTelemetry)** se instala en cada VM y nodo edge; instrumenta WMS, BD, broker, gateway IoT y red. Durante la pérdida de enlace, el collector bufferiza en disco y envía al recuperar; el stack on-prem es **Prometheus/Grafana/Loki**, con exportadores a CloudWatch/X-Ray/AMP en nube y correlación por `transaction_id`. El **AWS SSM Agent** permite gestión remota (parches, comandos) sin abrir puertos entrantes.

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
|---|---|---|:---:|---|
| A-01 | Motor WMS on-premise | ON-PREMISE | Latencia < 1 s + sin señal cámara |
| A-02 | BD transaccional WMS | ON-PREMISE | Escritura local + RAID 10 (RT-03.14) |
| A-03 | Broker de colas offline | ON-PREMISE | Encolado + reconciliación |
| A-04 | Capa anticorrupción ERP (frontera) | ON-PREMISE | ERP local + latencia síncrona |
| A-05 | Caché autenticación local (IdP Keycloak, Modelo B) | ON-PREMISE | Login offline 24 h (TTL 8 h) |
| B-01 | Sensores IoT temperatura (Ebyte ME31) | ON-PREMISE | Sin señal + Modbus RTU industrial |
| B-02 | Gateway IoT + Greengrass | ON-PREMISE | Edge computing + buffer |
| B-03 | Termógrafos camión (Onset CX450) | HIBRIDO | Hardware local + sincro nube |
| C-01 | App preventa offline (Zebra EC55) | HIBRIDO | Lógica local < 1,5 s |
| C-02 | App repartidor offline (TC58e + ZQ620 Plus + PAX A920 Pro) | HIBRIDO | 14 h sin señal + sincro POD |
| C-03 | Terminales bodega (MC9400 Cold Storage) | ON-PREMISE | Sin señal + -22°C |
| C-04 | Impresoras andén (ZT411) | ON-PREMISE | Periférico local |
| C-05 | Balanza recepción (Dibal BEV) | ON-PREMISE | Local M1, merma |
| D-01 | Firewall/UTM + Cust GW | ON-PREMISE | VPN IPsec + failover WAN |
| D-02 | Switch core con VLANs | ON-PREMISE | Segmentación (RT-03.23) |
| D-03 | Enlace WAN primario | ON-PREMISE | VPN + sincronización |
| D-04 | Enlace WAN respaldo | ON-PREMISE | Proveedor distinto + failover |
| D-05 | Respaldo local (recuperación rápida) | ON-PREMISE | RNF-20.07 3-2-1-1-0 |
| D-06 | Enlace WAN satelital (Starlink Enterprise) | ON-PREMISE | Camino satelital D-06 (respaldo CDs / cierre brecha Concepción / principal cross-docks) — RT-03.17 |
| E-01 | Mini-WMS cross-docking (+DS2208) | ON-PREMISE | Ventana 3 h madrugada |
| F-01 | OTel (ADOT) + SSM Agent | ON-PREMISE | RF-16.01, Zero Trust |
| F-02 | Gestión de parches | ON-PREMISE | RNF-13.06, CIS |
| F-03 | Agente EDR endpoints | ON-PREMISE | RNF-14.05, 24x7 |

**20 ON-PREMISE + 3 HÍBRIDOS (B-03, C-01, C-02) = 23 componentes totales** *(corrige la métrica "17 + 4" de la v04; incluye las filas nuevas C-05 Balanza Dibal BEV y D-06 Enlace WAN satelital Starlink)*

---

## SECCIÓN 3 — REFERENCIAS CRUZADAS Y TRAZABILIDAD CON LA ARQUITECTURA LÓGICA

| Exigencia | Donde se cumple en este documento |
|---|---|
| **Art. 16.2** — Justificación 6 criterios | Columnas LAT/CRIT/VOL/CONN/TCO/HW |
| **RT-02.11** — SPOF declarados | Sección 4 (SPOF) + nota de quórum clúster 3 nodos (A-02) |
| **RT-03.16 / RF-16.01** — Monitoreo | F-01 (OTel/ADOT + SSM Agent; Capa 8) |
| **RT-03.17 / RNF-13.07** — Enlace red. | D-03 (fibra) + **D-06 (satelital Starlink)** + D-04 (LTE, 2 proveedores; dual en cross-dock) + D-01 (VPN IPsec BGP / SD-WAN multi-WAN) |
| **RT-03.19** — Procesamiento en borde | B-02 (Greengrass Core) + E-01 (mini-WMS) |
| **RT-03.14 / RT-03.23** — Citas verificadas | A-02 (RAID 10, tolerancia a disco) · D-02 (segmentación inalámbrica) |
| **RF-15.01 a 15.05 / D6 (Arquitectura Lógica v1)** — Identidad | A-05 — **Caché local del IdP Keycloak (Modelo B, autoridad única en nube, TTL 8 h)** |
| **D7 / D9 (Arquitectura Lógica v1)** — Híbrido obligatorio + OTel | Componentes on-premise + F-01 (Capa 8) |
| **RNF-13.01** — Autonomía 24 h | A-01, A-02, A-03, A-05, E-01, B-02 |
| **RNF-14.05 / RNF-23.04** — EDR | F-03 (Agente EDR en servidores y estaciones) |
| **RNF-20.07** — Respaldo 3-2-1-1-0 | D-05 (copia local) + S3 Object Lock/Vault Lock en nube (pierna inmutable) + prueba DR semestral |
| **RT-03.13** — Funciones no disponibles en modo desconectado | Sección 1.1 (matriz por función/componente con procedimiento manual de sustitución) |
| **RT-06.01 a RT-06.24** — Cap. 6 (tipología, sala, energía, clima, seguridad física, cableado) | **Sala_Servidores_OnPremise_v02.md** (entregable de Sala de Servidores) |
| **RT-08.10** — Especificación de dispositivos con costo unitario | Sección 4 (modelo, cantidad, características, accesorios, consumibles y USD referencial) |
| **RT-08.13** — Ciclo de vida, repuestos y reposición 56 meses | Sección 4.1 |
| **§ 8.4** — Garantías, repuestos y niveles de reemplazo | Sección 4.2 |
| **RT-08.15** — Unidad por tipo de dispositivo para pruebas de aceptación del CLIENTE | Sección 4.3 (1 unidad por tipo, sin cargo, antes de la compra masiva) |
| **RT-06.26** — Custodia de medios de respaldo del sitio primario | D-05 (servicio de custodia/transporte de medio físico transportable) + Sala v02 §4.5 (recinto de custodia) |
| **RT-06.27** — Condiciones ambientales del recinto de custodia | Sala v02 §4.5 (recinto de 10 m²: luminosidad, humedad 40–60 %, ventilación, 18–27 °C) |

---

## SECCIÓN 4 — DISPOSITIVOS DE TERRENO (parque definido, alineado con la Arquitectura Lógica v1)

> Lista de dispositivos del proponente (sujeto a ajustes de cantidad según turnos y reservas; detalle de nodos y servidores en **Dimensionamiento_Infraestructura_OnPremise_v05**).

| Ítem | Caso de uso | Dispositivo | Cantidad base | Modelo | Costo unitario estimado (USD ref.) |
|---|---|---|---|---|
| 1 | Preventa | Terminal móvil de preventa | 62 + reserva 20 % | **Zebra EC55** | ≈ USD 1.200 |
| 2 | Reparto — conductores propios | Terminal rugosa de reparto | 42 + reserva | **Zebra TC58e** (5G, SE55, batería ext. 7.000 mAh, BT 5.3 + BLE, GPS L1/L5, IP65/68, Android 13→17) | ≈ USD 1.400 |
| 3 | Cabina de despacho | Impresora térmica portátil de cabina | Por camión con app reparto | **Zebra ZQ620 Plus** (3", ZPL/EPL/CPCL, Link-OS, IP54, batería PowerPrecision+ 3.250 mAh) | ≈ USD 700 |
| 4 | Cabina de despacho | POS móvil Bluetooth | Por camión (cobranza tarjeta) | **PAX A920 Pro** (Android 14, PCI PTS 7.x, EMV L1/L2, impresora integrada 80 mm/s, PAXSTORE) | ≈ USD 600 |
| 5 | Reparto — conductores externos (~160) | Terminal de reparto (parque único con ítem 2) | ~160 + reserva | **Zebra TC58e** (idéntico al ítem 2) | ≈ USD 1.400 |
| 6 | Bodega −22 °C | Terminal RF (pool) | Talca 144 (120 + 20 %) · Concepción 30 | **Zebra MC9400 Cold Storage (Freezer)** (−30 °C, SE58 ~100 pies, batería freezer 5.000 mAh, pistol grip, Android 13→18, Wi-Fi 6E) | ≈ USD 4.500 |
| 7 | Andén | Impresora térmica de andén | 4 Talca · 2 Concepción | **Zebra ZT411** (ZPL II + XML-Enabled; 203 dpi; 14 ips; Ethernet; Print DNA) | ≈ USD 2.300 |
| 8 | Recepción | Balanza de recepción | 2 Talca · 1 Concepción | **Dibal BEV** (plataforma ME + DMI-610 Inox; doble RS-232, Ethernet; 6.000 divisiones) | ≈ USD 1.800 |
| 9 | Cross-docking | Scanner de mano GS1 | 6 (2 × plataforma) | **Zebra DS2208** (1D/2D + GS1 DataBar; PRZM; USB/RS-232/KBW; garantía 60 meses) | ≈ USD 180 |
| 10 | Cámaras (IoT) | Sensor IoT de temperatura | 28 puntos ≈ 7 módulos | **Ebyte ME31-XDXX0400** (4 canales PT100 2/3 hilos/módulo; ±0,5 % ± 1 °C ≈ ±1,1 °C a −22 °C; RS-485/Modbus RTU + Modbus TCP; 1 Hz; −40…+85 °C; riel DIN) | ≈ USD 700 (módulo de 4 canales con sondas) |
| 11 | Cadena de frío en ruta | Termógrafo de camión | 18 (camiones con frío) | **Onset InTemp CX450** (BLE; −30…+70 °C ±0,5 °C; 103.400 mediciones; NIST 2 ptos; GDP/GMP) | ≈ USD 150 |
| 12 | Enlace satelital WAN (D-06) | Kit Starlink Enterprise fijo (antena + router) | 5 (2 CDs + 3 cross-docks) | **Starlink Enterprise** (activación Business/Enterprise, plan priorizado 1 TB CDs / 500 GB cross-docks; cotización 56 meses adjunta) | Ver cotización Starlink (incluye instalación en techumbre) |

> **Accesorios y consumibles declarados (RT-08.10):** cradle/multi-slot y baterías de repuesto por terminal (EC55, TC58e, MC9400), cabezal térmico y rollos para ZT411/ZQ620, papel papel térmico de 3" y 4" (consumible), rótulos ZD labels, cables USB/RS-232 y fuente para DS2208, sondas PT100 de repuesto para ME31 (4 canales reemplazables por módulo) y certificados NIST de recalibración anual para CX450. Los valores son referenciales de mercado (USD, 2026), sujetos a cotización formal; su compra es de cargo del CLIENTE conforme al Art. 14.2.

### Sección 4.1 — Ciclo de vida, repuestos y plan de reposición (RT-08.13)

*RT-08.13 (OBL): ciclo de vida esperado por dispositivo, disponibilidad de repuestos y plan de reposición durante los 56 meses del Contrato.*

| Dispositivo | Ciclo de vida esperado | Disponibilidad de repuestos | Plan de reposición (56 meses) |
|---|---|---|---|
| Zebra EC55 | 5 años + soporte LifeGuard Android hasta 8 años (2148) | Baterías, pantallas y cradles de repuesto disponibles vía canal Zebra/canal autorizado en Chile | Reemplazo 1:1 ante falla o al cuarto año (depreciación por turnos de preventa) con stock de reposición seco del **10 %** |
| Zebra TC58e | 6 años (parque único ~200) | Baterías ext. 7.000 mAh, BLE periféricos en stock; garantía del fabricante + plan de reparación 48 h | Reposición escalonada: 20 % al mes 36 y 20 % al mes 48 (ciclo de batería 2 turnos/día); stock seco 10 % |
| Zebra ZQ620 Plus | 5 años | Cabezales térmicos y baterías PowerPrecision+ en stock en Chile | Reemplazo de cabezal por desgaste (≈ 50 km de impresión) y unidad completa ante falla |
| PAX A920 Pro | 4–5 años (ciclo PCI PTS) | Baterías, impresora integrada y lector en stock vía PAXSTORE/canal | Actualización de batch PCI y reposición al mes 48 para mantener acreditación |
| MC9400 Cold Storage (Freezer) | 5–7 años (certificado cámara) | Pistol grip, baterías freezer 5.000 mAh, SE58, módulo Wi-Fi 6E en stock | Reposición por ciclo cámara o falla; stock seco 10 % en Talca (precargado, RT-03.18) |
| Zebra ZT411 | 5–7 años | Cabezal térmico, rodillos, fuente y placa lógica en stock | Mantenimiento preventivo anual y reemplazo de cabezal programado en la cuenta de mantenimiento |
| Dibal BEV | 10 años (equipo industrial) | Celdas de carga y placas del indicador DMI-610 en stock | Reemplazo solo ante falla de celda; calibración anual certificada |
| Zebra DS2208 | 5 años (garantía 60 meses incluida) | Cable y pie de apoyo en stock; garantía del fabricante cubre los 56 meses | Reemplazo 1:1 dentro de garantía; reposición al mes 52 |
| Ebyte ME31 + sondas PT100 | 5–7 años | Módulos ME31 y sondas PT100 en bodega | Reposición de módulo/sonda por canal según resultado de calibración anual (RT-03.18/19) |
| Onset InTemp CX450 | 5 años (reutilizable) | — (dispositivo cerrado; recalibración NIST anual) | Recalibración NIST anual; reemplazo ante falla de registro con stock seco 10 % |
| **Starlink Enterprise (D-06)** | 5+ años (HW satelital fijo) | Antena y router con reemplazo vía proveedor Starlink (soporte Enterprise) | **Reposición de hardware 15 % / 56 meses** conforme a la cotización comercial (RT-08.13); plan de datos activo durante todo el Contrato |

### Sección 4.2 — Garantías y niveles de reemplazo (§ 8.4 de las Transversales)

*Garantías, repuestos y niveles de reemplazo exigidos por § 8.4 y comprometidos formalmente por el PROPONENTE por los 56 meses del Contrato.*

| Elemento (§ 8.4) | Exigencia mínima | Compromiso declarado |
|---|---|---|
| Hardware crítico | Soporte 24×7 con atención en sitio y resolución en 4 horas | **Soporte 24×7, atención en sitio en ≤ 4 h** para servidores (clúster Talca, nodo Concepción), equipos de red core (D-01/D-02), UPS/generador/clima de la sala (Cap. 6) y Gateway IoT B-02 |
| Hardware no crítico | Soporte en horario hábil con resolución en 24 horas | Soporte en horario hábil con **resolución en ≤ 24 h** para periféricos (ZT411, Dibal BEV, DS2208, ME31) y dispositivos de terreno fuera de la ventana operacional |
| Software de base y de plataforma | Soporte continuo del fabricante durante todo el período contractual | Soporte continuo declarado: Proxmox VE (suscripción), PostgreSQL (comunidad + soporte distribuidor), sistemas operativos y firmware de red con actualización garantizada durante los 56 meses |
| Stock de repuestos | Al menos 10 % del parque instalado por tipo de componente crítico, disponible en Chile | **Stock en Chile ≥ 10 % del parque** por tipo de componente crítico (fuentes, discos SSD/NVMe del clúster, UPS, ventiladores climate, módulos SFP, baterías) |
| Reemplazo de componente crítico en falla | Máximo 4 horas desde la confirmación del diagnóstico | **Reemplazo ≤ 4 h** desde la confirmación del diagnóstico para componente crítico (disco del RAID/Ceph, fuente, switch, módulo de UPS) |
| Dispositivos de terreno | Stock de reemplazo en sitio equivalente al 10 % del parque, con configuración precargada | **Stock en sitio = 10 % del parque** por modelo (EC55, TC58e, MC9400 Freezer, ZQ620 Plus, PAX A920, DS2208) **con configuración precargada** (Wi-Fi, MDM, apps, certificados) y activación en línea vía gestión de flota RT-03.18 |

### Sección 4.3 — Unidad de muestra por tipo de dispositivo para pruebas de aceptación del CLIENTE (RT-08.15)

*RT-08.15 (Deseable): "El PROPONENTE proveerá una unidad de cada tipo de dispositivo especificado para pruebas de aceptación por parte del CLIENTE, antes de la compra masiva." Se declara la provisión de **una (1) unidad de cada tipo de dispositivo de terreno**, sin costo para el CLIENTE, para pruebas de aceptación en condiciones reales antes de la compra masiva de cada hito de producción (Etapa 1 mes 16 y Etapa 2 mes 21).*

| Tipo de dispositivo | Modelo | Unidad de muestra (RT-08.15) | Prueba de aceptación del CLIENTE |
|---|---|---|---|
| Terminal de preventa | Zebra EC55 | **1** | Validación en terreno: app offline, lectura GS1, batería turno |
| Terminal de reparto | Zebra TC58e | **1** | Validación en ruta real: POD, GPS, BLE termógrafo, batería 14 h |
| Impresora de cabina | Zebra ZQ620 Plus | **1** | Impresión de comprobante desde la app |
| POS móvil | PAX A920 Pro | **1** | Cobro con tarjeta EMV en ruta (RF-07.06) |
| Terminal rugoso bodega | Zebra MC9400 Cold Storage (Freezer) | **1** | Picking en cámara −22 °C con guantes (RNF-05.02/05.03) |
| Impresora de andén | Zebra ZT411 | **1** | Impresión etiqueta SSCC GS1 (RF-01.07) |
| Balanza de recepción | Dibal BEV | **1** | Pesaje integrado M1 (RF-01.01) |
| Escáner de mano GS1 | Zebra DS2208 | **1** | Lectura GS1 DataBar en cross-docking |
| Sensor IoT de temperatura | Ebyte ME31-XDXX0400 (módulo + sondas) | **1 módulo (4 canales)** | Lectura 1 Hz, integración Modbus/Greengrass |
| Termógrafo de camión | Onset InTemp CX450 | **1** | Registro NIST, sync vía BLE al terminal |

> La unidad de muestra se entrega en el hito de producción correspondiente y **antes de emitir la compra masiva** de cada lote (Etapa 1 / Etapa 2), conforme a la planificación de la Tabla v06 §4 y al Plan de Pruebas y Validación (Formulario T-13). El resultado de la aceptación queda documentado en el acta de aceptación del CLIENTE (Art. 18 del caso).

**SPOF declarados (RT-02.11):** (1) Andén/balanzas e impresoras de un sitio son periféricos locales con vía de fallo de negocio acotada (bloqueo de andén puntual) — mitigación por redundancia de unidades y respaldo manual. (2) Clúster Talca: N+1 real con 3 nodos y quórum propio — SPOF estructural eliminado. (3) Concepción: nodo único edge (SPOF admitido) — mitigado por la funcionalidad autónoma 24 h y por DRP en nube. (4) Cross-docking: mini-PC único por plataforma (SPOF admitido) — ventana operacional 3 h + respaldo por procedimiento y sincronización diferida (RT-03.11).

---

*Versión 05 — Alineación con la Arquitectura Lógica v1 (D6/D7/D9): IdP Keycloak Modelo B (autoridad única en nube + caché local TTL 8 h); conteo corregido 19 + 3 = 22 (incluye fila C-05 Balanza Dibal BEV); dispositivos de terreno definidos (EC55, TC58e, ZQ620 Plus, PAX A920 Pro, MC9400 Cold Storage, ZT411, Dibal BEV, DS2208, Ebyte ME31, Onset CX450); citas RT-03.14/RT-03.23 verificadas en el transversal; referencias a la Sala de Servidores (Sala_Servidores_OnPremise_v02) y al Dimensionamiento v05 (clúster de 3 nodos, DR semestral, LTE dual en cross-docking). Reconciliación de IdP **cerrada**: el documento cloud pasó a Modelo B en su **v3.6** (§3.3/§3.5/§5.4/§7.3/§7.10/L-02/Apéndice C) y el consolidado quedó en `Arquitectura_Fisica_Hibrida_Consolidada_Caso02_v02.md`.*

*Versión 06 — Corrección de brechas de la Matriz de Cumplimiento BTT (on-premise): **RT-03.13** declarado (Sección 1.1 — matriz de funciones no disponibles en modo desconectado con procedimiento manual); **RT-08.10** cumplido (Sección 4 — costo unitario estimado USD referencial por dispositivo, con accesorios y consumibles); **RT-08.13** y **§ 8.4** cumplidos (Secciones 4.1 y 4.2 — ciclo de vida, repuestos y plan de reposición de 56 meses; garantías 24×7/4 h, 24 h horario hábil, stock ≥ 10 % en Chile, reemplazo crítico ≤ 4 h y 10 % en sitio precargado). Referencias cruzadas actualizadas a Sala v02 y Dimensionamiento v05.*

*Versión 06c — Cierre de pendientes del alcance arquitectura física on-premise: **RT-06.26** cumplido en D-05 (servicio de custodia de medios del sitio primario en medio físico transportable a otro lugar cuando el CLIENTE lo determine, con bóveda externa y bitácora RT-06.28; la pierna S3 es complementaria, no la única); **RT-06.27** cumplido en Sala v02 §4.5 (recinto de custodia de 10 m² con luminosidad/humedad/ventilación/temperatura controladas); **RT-08.15** cumplido en Sección 4.3 (1 unidad por tipo de dispositivo, sin cargo, para pruebas de aceptación del CLIENTE antes de la compra masiva, Etapa 1 y Etapa 2).*


*Versión 06d — Integración del enlace satelital Starlink (Cotización 05-09-2026): nuevo componente **D-06** (5 kits; respaldo automático de Talca/Concepción cerrando la brecha RNF-13.07 y enlace principal de las 3 cross-docks), SD-WAN multi-WAN tri-camino en D-01, LTE como camino terciario en CDs y respaldo del satelital en cross-docks, conteo 20+3=23 y trazabilidad RT-03.17/RNF-13.07/RT-08.10/RT-08.13 actualizada. Coherente con Dimensionamiento v05, Sala v02 y Consolidado v02.*

*Versión 06d — Ajuste de especificación del sensor IoT B-01 (alineado con Dimensionamiento v05 §2.8): módulo Ebyte **ME31-XDXX0400** (4 canales PT100 2/3 hilos por módulo, sonda 3 hilos con compensación de cable, exactitud ±0,5 % ± 1 °C ≈ ±1,1 °C a −22 °C) en lugar de ME31-XDXX0800-485 (8 canales); 28 puntos ≈ **7 módulos** (antes 4); protocolo **RS-485/Modbus RTU + Modbus TCP**; maestro del Gateway B-02 sobre los módulos Ebyte B-01; costo unitario referencia actualizado en Sección 4.*