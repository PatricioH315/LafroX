# Dimensionamiento de Infraestructura On-Premise
## Distribuidora Puelche S.A. — Caso 02 Logística

> **Documento:** Componente de Arquitectura Física — Dimensionamiento de Servidores, Equipamiento y Red
> **Versión:** 05
> **Dependencia:** Tabla de Emplazamiento On-Premise v06 (aprobada) · Sala de Servidores On-Premise v02 (recintos/energía/clima/racks)
> **Alcance:** CD Talca, CD Concepción y 3 Plataformas de Cross-Docking (Curicó, Chillán, Los Ángeles)
>
> **Cambios clave v03 → v04:**
> 1. **Clúster Talca de 3 nodos** (exigencia del profesor: "el clúster mínimo son tres nodos, con dos no hay dónde mover las cargas"). Se elimina el esquema 2 nodos + QDevice: el quórum queda garantizado por 3 nodos reales (3 MON) y la redundancia N+1 sostiene 30 vCPU con 2 supervivientes al 47 %.
> 2. **Ceph sobre 3 nodos**: pool RBD réplica 2, 12 OSDs (4 por nodo), 3 MON con quórum mayoritario real.
> 3. **Totales corregidos** (§1.5): RAM física 464 GB (no "~240 GB"), vCPU asignados ~60 (no "~68"), almacenamiento útil 9,22 TB + 8 TB NAS (no "~8,3 TB").
> 4. **Prueba DR semestral declarada** (RT-06.10 / Art. 20 de las Bases Administrativas) además de la restauración mensual (RNF-20.07).
> 5. **Cross-Docking con LTE dual (2 proveedores)** para cumplir RT-03.17 donde solo existe red móvil.
> 6. **Dispositivos de terreno definidos** según Tabla v06 §4 (EC55, TC58e, ZQ620 Plus, PAX A920 Pro, MC9400 Cold Storage, ZT411, Dibal BEV, DS2208, Ebyte ME31, Onset CX450).
> 7. **IdP alineado a Keycloak (Modelo B)** — VM-05/VM-C03 pasan de "Cognito Auth Cache" a "Keycloak Local Auth Cache / Offline Proxy" (TTL 8 h, solo lectura, autoridad en nube) — D6 Arquitectura Lógica v1.
>
> **Cambios clave v04 → v05 (cierre de brechas de la Matriz de Cumplimiento BTT on-premise):**
> 1. **Nuevas PARTES 5 a 9** que declaran los requisitos obligatorios de los capítulos 7 (Recuperación ante Desastres), 8 (Hardware y medios), 10 (Disponibilidad y resiliencia), 11 (Seguridad de la Información), 12 (Identidad y accesos) y 14 (Observabilidad) aplicables al segmento on-premise.
> 2. **Cifrado de respaldos** (RT-07.10, RT-11.09) y **TLS 1.3** en tránsito (RT-11.08) declarados en PARTE 8.
> 3. **S.M.A.R.T. / monitoreo predictivo de medios** (RT-08.02), **control de dispositivos extraíbles** (RT-08.09), **eficiencia energética** (RT-08.08), **equipamiento nuevo sin uso previo** (RT-08.06) y **procedimiento de ampliación** (RT-08.05) declarados en PARTE 6.
> 4. **Garantías y niveles de reemplazo (§ 8.4)** comprometidos en PARTE 6, con el detalle por dispositivo en Tabla v06 §4.2.
> 5. **SLO e2e ≥ 99,9 % mensual sobre la transacción crítica** (RT-10.01) en PARTE 7, coherente con Sala v02 §7.
> 6. Referencias cruzadas actualizadas a Tabla v06 y Sala v02.
>
> **Cambios clave v05 → v06 (cierre del Cap. 9 — Desempeño, capacidad y escalabilidad):**
> 1. **Nueva PARTE 10** que declara el capítulo 9 completo (RT-09.01 a RT-09.10): capacidad de diseño (RT-09.01), concurrencia con umbrales p95 (RT-09.02), **crecimiento 3× sin rediseño en 3 años** (RT-09.03), escalamiento horizontal ≤ 15 min sin pérdida (RT-09.04), **primer cuello de botella = escritura transaccional de VM-02 PostgreSQL** con detección y resolución (RT-09.05), pruebas de carga/estrés 1,5× peak en Preproducción integradas al **Formulario T-13** (RT-09.06/09.07), degradación controlada (RT-09.08), gestión trimestral de capacidad (RT-09.09) y carga automatizada en CI (RT-09.10, Deseable).
>
> **Cambios clave v06 → v07 (incorporación de enlace satelital Starlink en los 5 sitios fijos — Cotización Starlink 56 meses, 05-09-2026):**
> 1. **Nuevo camino WAN D-06 (Starlink)** en los **5 sitios on-premise**: en los CDs (Talca y Concepción) opera como **respaldo automático** preferente (fibra D-03 → Starlink → LTE D-04, SD-WAN), **cerrando la brecha de Concepción (RNF-13.07** — "nuevo enlace requerido" §3.7); en las **3 plataformas de cross-docking** (Curicó, Chillán, Los Ángeles) pasa a ser el **enlace principal**, resolviendo la intermitencia de señal móvil de Los Ángeles entre 03:00–05:00 (exactamente su ventana operacional) que dejaba a la plataforma sin cobertura en plena operación.
> 2. **SD-WAN multi-WAN** sobre el clúster de firewalls D-01 (Talca) y el firewall de borde (Concepción): 3 interfaces WAN (fibra D-03 + Starlink D-06 + LTE D-04) con selección automática de camino y conmutación < 30 s; en los cross-docks el kit Starlink se conecta al switch compacto/mini-PC y el módulo 4G Cat-12 del mini-PC conserva el **LTE dual (2 proveedores)** como respaldo automático (RT-03.17).
> 3. **Inventario actualizado (§4.1):** 5 kits Starlink fijos (1 Talca, 1 Concepción, 3 cross-docks) con plan de datos priorizado (1 TB Talca/Concepción · 500 GB cross-docks) y reposición de hardware del 15 % durante los 56 meses (RT-08.13); kits energizados desde PDU-B en Talca (RT-08.04) y mini-UPS en los cross-docks; antena en techumbre con ingreso por canalización protegida (RT-06.32).

---

## PARTE 1 — INVENTARIO FÍSICO Y DIMENSIONAMIENTO DE SERVIDORES

---

### 1.1 Premisas de Dimensionamiento

| Parámetro | Valor base (Caso 02, Cap. 3–4) |
|---|---|
| Líneas de picking / mes | 260.000 |
| Unidades despachadas / mes | 2.400.000 |
| SKU activos | 8.400 |
| Posiciones de almacén | 11.400 |
| Operarios de picking simultáneos (turno nocturno) | 120 |
| Terminales RF concurrentes | 120 |
| Preventistas con app móvil | 62 |
| Entregas / día (régimen normal) | 1.400 |
| Entregas / día (peak septiembre) | 2.600 |
| Camiones con cadena de frío | 18 |
| Puntos de medición de temperatura (Talca + Concepción) | 28 (≈ 7 módulos Ebyte de 4 canales) |
| Sitios on-premise | 5 (Talca, Concepción, Curicó, Chillán, Los Ángeles) |

**Carga de diseño:** Se dimensiona al **peak de septiembre (2.600 entregas/día)** multiplicado por el factor de seguridad **×1,5** (RNF-19.04), es decir, la infraestructura debe tolerar 3.900 entregas/día sin degradación.

**TPS estimado (peak):**

| Flujo | Cálculo | TPS estimado |
|---|---|---|
| Confirmaciones de picking | 120 terminales × 1 conf / 6 s promedio | ~20 TPS |
| Pedidos preventa (09:00–13:00) | 62 preventistas × 1 línea / 8 s | ~8 TPS |
| Movimientos inventario + sincronización | Suma de flujos | ~35 TPS |
| **TPS de diseño (burst ×3)** | 35 × 3 | **~105 TPS** |

---

### 1.2 CD Talca — Clúster de Virtualización en Alta Disponibilidad (N+1, 3 nodos)

> **Exigencia del profesor (Sala_De_Servidores.md §7):** "El clúster mínimo son tres nodos: con dos no hay dónde mover las cargas cuando uno cae o se mantiene". El clúster de Talca se construye con **3 nodos idénticos**; la pérdida de un nodo deja 2 supervivientes con capacidad de sobra bajo N+1 (47 % vCPU) y permite **mantenimiento en caliente** de un nodo sin degradar el otro par.

#### 1.2.1 Servidores Físicos

Se despliegan **3 servidores físicos idénticos** en configuración clúster N+1 sobre **Proxmox VE / KVM**. Ante la caída de un nodo, los 2 hipervisores supervivientes asumen todas las VMs en ≤ 30 s (HA de Proxmox con quórum de 3 nodos; live migration para mantenimientos planificados). La movilidad de VMs entre nodos se sustenta en **almacenamiento replicado de forma síncrona (Ceph)** a través de las interfaces dedicadas de 10GbE (ver 1.2.5).

| Atributo | Nodo-1 | Nodo-2 | Nodo-3 |
|---|---|---|---|
| **Modelo de referencia** | Servidor rack 1U — Dell PowerEdge R6615 / HPE ProLiant DL325 Gen11 o equiv. | Ídem | Ídem |
| **CPU** | 1 socket × 16 cores / 32 threads — AMD EPYC 9124 (3,0 GHz base, 3,7 GHz boost) o Xeon equivalente | Ídem | Ídem |
| **RAM** | **128 GB DDR5 ECC** (8 × 16 GB) | Ídem | Ídem |
| **Almacenamiento SO / Hipervisor** | RAID 1: 2 × SSD SATA 480 GB (espejo) | Ídem | Ídem |
| **Almacenamiento de Datos** (OSD Ceph) | RAID 10: 4 × NVMe SSD 1,92 TB U.2 + 1 Hot-Spare NVMe 1,92 TB | Ídem | Ídem |
| **Interfaces de red** | 2 × 10GbE SFP+ (red dedicada Ceph + tráfico VM) + 2 × 1GbE RJ-45 (gestión / IPMI) | Ídem | Ídem |
| **IPMI / iDRAC / iLO** | Sí — gestión fuera de banda (VLAN MGT-TALCA) | Ídem | Ídem |
| **Fuente de alimentación** | Dual PSU hot-swap 1+1 (PDU A/B) | Ídem | Ídem |
| **Factor de forma** | 1U rack | Ídem | Ídem |

#### 1.2.2 Esquema RAID aprobado — CD Talca (por nodo)

| Capa | Tipo RAID | Discos | Capacidad bruta | Capacidad útil | Hot-Spare |
|---|---|---|---|---|---|
| SO + Hipervisor | RAID 1 (espejo) | 2 × SSD SATA 480 GB | 960 GB | **480 GB** | No (espejo es tolerante por diseño) |
| Storage de Datos (OSD del pool Ceph) | RAID 10 (espejo + franjas) | 4 × NVMe 1,92 TB | 7,68 TB por nodo → 23,04 TB entre 3 nodos | **3,84 TB por nodo → 11,52 TB entre 3 nodos** | 1 × NVMe 1,92 TB por nodo (reconstrucción automática del OSD) |

**Memoria de cálculo del factor de compra:**

| Concepto | Valor |
|---|---|
| Capacidad útil bruta del clúster (3 nodos × RAID 10 de 3,84 TB) | 11,52 TB |
| Pool Ceph con réplica factor 2 (cada dato se replica en 2 nodos distintos) | **5,76 TB útiles** |
| Requerimiento de datos del clúster (VM-01..VM-06) | 1.890 GB (≈1,85 TB) |
| Utilización del pool | 1,85 / 5,76 ≈ **32 %** (margen ~68 % para crecimiento 5 años) |
| Factor de compra efectivo (bruto total / útil pool) | 23,04 TB / 5,76 TB = **×4,0** (supera el mínimo ×2,5) |
| Crecimiento estimado 5 años | 1.890 GB × 3 ≈ 5,7 TB < 5,76 TB (margen consistente) |

#### 1.2.3 Máquinas Virtuales — Clúster Talca

| ID | Nombre / Rol | vCPU | RAM | Disco raíz | Disco datos | Criterio de tamaño |
|---|---|---|---|---|---|---|
| VM-01 | **WMS Core** (motor WMS: recepción, picking FEFO, misiones RF, despacho, SSCC GS1) | 8 | 16 GB | 40 GB | 100 GB | 120 terminales concurrentes; ~20 TPS en picking; sin estado persistente propio |
| VM-02 | **PostgreSQL — BD Transaccional (maestro de bodega)** (inventario, lotes, posiciones, SSCC, trazabilidad 5 años; réplica DRP hacia Amazon Aurora vía WAL streaming, RPO ≤ 15 min) | 8 | 32 GB | 40 GB | 1.500 GB | shared_buffers = 8 GB; effective_cache_size = 24 GB; 105 TPS × 8 E/S = 840 IOPS → NVMe RAID 10 entrega > 100.000 IOPS |
| VM-03 | **RabbitMQ — Broker de colas offline** (encolado 24 h sin WAN) | 4 | 8 GB | 30 GB | 200 GB | 24 h × 35 TPS × 3.600 s = ~3 M mensajes; 200 GB >> (< 1 KB/msj) |
| VM-04 | **ACL ERP — Frontera única de integración** (adaptador WMS/cloud–ERP 2017; encolado offline) | 4 | 4 GB | 30 GB | 20 GB | Única vía hacia el ERP 2017; los servicios cloud (svc-erp-integration) lo consumen vía VPN, nunca directo |
| VM-05 | **Keycloak Local Auth Cache / Offline Proxy (A-05, Modelo B D6)** (caché local de identidades/tokens del IdP Keycloak; TTL 8 h; solo lectura; SSO para 120 operarios) | 4 | 4 GB | 30 GB | 20 GB | Caché de tokens JWT emitidos por Keycloak (maestro en nube) con validación local de firma; 120 operarios concurrentes; TTL 8 h = turno; autoridad única de identidad en nube |
| VM-06 | **OpenTelemetry Collector (ADOT) + SSM Agent (F-01, Capa 8 D9)** (telemetría OTEL; buffer offline 24 h; Zero Trust sin puertos entrantes) | 2 | 4 GB | 30 GB | 50 GB | Buffer para 24 h de métricas, logs y trazas de todos los nodos on-premise |

**Totales de recursos del clúster Talca:**

| Recurso | Total asignado a VMs | Capacidad física (1 nodo) | Capacidad clúster (3 nodos) | Utilización bajo N+1 (2 nodos supervivientes) |
|---|---|---|---|---|
| vCPU | 30 | 32 threads | 96 threads | 30 / 64 = **47 %** (margen 53 %) — sin overcommit |
| RAM | 68 GB | 128 GB | 384 GB | 68 / 256 = **27 %** (margen 73 %) |
| Almacenamiento (pool) | 1.890 GB | 3,84 TB por nodo (RAID 10) | 11,52 TB bruto → **5,76 TB pool (réplica 2)** | 32 % del pool (margen a 5 años) |

> **Nota de overcommit:** con 3 nodos y N+1, el par superviviente ofrece 64 threads para las 30 vCPU (47 %). Aun ante la falla simultánea/dura de 2 nodos, el nodo único restante cubriría 30/32 ≈ 94 % en modo degradado declarado (sin sobreasignación). Este esquema cumple la exigencia del profesor de **mínimo 3 nodos** y elimina el riesgo de split-brain del esquema anterior de 2 nodos con QDevice.

#### 1.2.4 NAS / Appliance de Respaldo Local — Recuperación Rápida (D-05)

Dispositivo dedicado, físicamente independiente del clúster de producción. Es la **copia local de recuperación rápida** dentro del esquema único 3-2-1-1-0 (RNF-20.07). **No constituye la pierna "1 inmutable"**: esa responsabilidad recae exclusivamente en la nube (S3 Object Lock / Backup Vault Lock).

| Atributo | Especificación |
|---|---|
| **Tipo** | NAS rack 2U (ej. Synology RS1221RP+ — 12 bahías, 2U —, QNAP TS-873AeU-RP) |
| **Capacidad bruta** | 4 × HDD SATA 4 TB en RAID 6 → 8 TB útiles (tolera 2 discos caídos) |
| **Refuerzo de integridad** | WORM local como refuerzo adicional (retención 30 días); no sustituye la pierna inmutable de nube |
| **Protocolo de respaldo** | WAL streaming de PostgreSQL (RPO ≤ 15 min) + respaldo completo diario en ventana 02:00–04:00 |
| **Conectividad** | 2 × 1GbE en VLAN-Servidores; acceso restringido a VM-02 y sistema de backup |
| **Verificación de restauración** | Prueba mensual automatizada en entorno pre-producción — "0 errores" (RNF-20.07) |
| **RTO objetivo** | ≤ 4 h restauración completa desde NAS local, independiente de WAN (RNF-20.06) |

**Prueba DR semestral (declarada — RT-06.10 / Art. 20 Bases Administrativas):**

| Ítem | Detalle |
|---|---|
| Periodicidad | **Semestral** (además de la restauración mensual RNF-20.07) |
| Alcance | (1) Restauración del WMS desde la copia local D-05 y verificación de datos; (2) conmutación del plano de datos hacia la réplica/DRP Aurora en la nube (RPO ≤ 15 min, RTO ≤ 4 h); (3) validación de la sincronización diferida del broker A-03 al reconectar; (4) revisión y medición semestral de las instalaciones eléctricas del recinto (RT-06.10) |
| Entregable | Informe de prueba DR con resultados, tiempos medidos y observaciones; disponible para el CLIENTE (Art. 20) |
| Responsable | Jefe de TI (Puelche) + adjudicatario |

**Esquema 3-2-1-1-0 unificado (declaración única del consolidado híbrido):**

| Pierna | Detalle |
|---|---|
| **3 copias** | (1) Datos activos locales en NVMe RAID 10 (pool Ceph) · (2) Copia en NAS local D-05 · (3) Backup en nube |
| **2 medios** | (1) Discos NVMe/HDD locales · (2) Almacenamiento de objetos S3 |
| **1 fuera de sitio** | Backup en AWS — región primaria sa-east-1, réplica cross-region us-east-1 |
| **1 inmutable** | S3 Object Lock + Backup Vault Lock en AWS (ni el root elimina) |
| **0 errores** | Verificación mensual automatizada de restauración + **prueba DR semestral** |

---

#### 1.2.5 Replicación de almacenamiento para HA (Ceph — 3 nodos)

La alta disponibilidad del clúster y la movilidad de VMs entre los tres nodos Proxmox se sustentan en almacenamiento compartido replicado de forma síncrona, sin depender de una cabina externa:

| Atributo | Especificación |
|---|---|
| **Mecanismo** | Ceph sobre Proxmox VE: pool RBD con **réplica síncrona factor 2** (size=2, min_size=1). Cada escritura se confirma sólo después de quedar registrada en los NVMe de 2 nodos |
| **OSDs** | Cada volumen RAID 10 de un nodo (1.2.2) se expone como **4 OSDs por nodo** → **12 OSDs totales** |
| **Monitores y quórum** | **3 MON (uno por nodo)**; quórum mayoritario real sin depender de monitor externo/QDevice. Falla de 1 nodo → quórum 2/3 OK; falla de 2 nodos → modo degradado read-only (min_size=1) hasta reconstrucción |
| **Red dedicada** | Enlace dedicado de almacenamiento entre nodos por las interfaces 10GbE SFP+, con MTU 9000 (jumbo frames) |
| **Failover ante caída de chasis** | Los 2 nodos supervivientes conservan copias síncronas íntegras; el HA de Proxmox rearranca las VMs en ≤ 30 s sin pérdida de datos ya confirmados |
| **Migración y mantenimiento** | Live migration sin corte por la red 10GbE dedicada; un nodo puede mantenerse en caliente mientras la carga queda en el par restante (N+1) |

**Capacidad útil efectiva del pool replicado:** con factor de réplica 2 sobre 3 nodos, la capacidad útil total es **5,76 TB** (11,52 TB brutos / 2), consistente con el margen de crecimiento declarado en 1.2.3 (1.890 GB actuales ≈ 32 %).

> El esquema de réplica Ceph protege la continuidad ante la caída de un chasis; la protección contra pérdida lógica (borrado accidental, corrupción, ransomware) sigue a cargo del respaldo local D-05 (recuperación rápida ≤ 4 h) y de la copia fuera de sitio con pierna inmutable en la nube — S3 Object Lock / Backup Vault Lock (esquema 3-2-1-1-0, RNF-20.07).

---

### 1.3 CD Concepción — Servidor de Borde (Gabinete de Borde Operacional)

Instancia WMS edge autónoma que garantiza 24 h de operación independiente de Talca.

| Atributo | Especificación |
|---|---|
| **Tipo** | Servidor rack compacto 1U/2U (Dell PowerEdge R250, HPE ProLiant DL20 Gen11, Supermicro 510T o equiv.) |
| **CPU** | 1 socket × Intel Xeon E-2300 (6 cores / 12 threads, 3,4 GHz base) |
| **RAM** | 32 GB DDR4 ECC (2 × 16 GB) — ampliable a 64 GB |
| **Almacenamiento SO** | RAID 1: 2 × SSD SATA 480 GB |
| **Almacenamiento Datos** | RAID 10: 4 × NVMe SSD 960 GB + 1 Hot-Spare 960 GB → 1,92 TB útiles |
| **Red** | 2 × 1GbE RJ-45 (producción) + 1 × 1GbE (gestión / IPMI) |
| **Fuente** | Dual PSU hot-swap 1+1 |

**VMs en Concepción:**

| VM | Rol | vCPU | RAM | Disco datos |
|---|---|---|---|---|
| VM-C01 | WMS Edge (instancia local bodega Concepción; sincronización diferida con WMS Talca) | 4 | 8 GB | 300 GB |
| VM-C02 | PostgreSQL local (BD transaccional autónoma durante corte WAN) | 4 | 8 GB | 500 GB |
| VM-C03 | **Keycloak Local Auth Cache / Offline Proxy** (caché de identidades/tokens TTL 8 h; solo lectura; RF-15.01, RNF-13.01 — Modelo B) | 2 | 4 GB | 20 GB |
| VM-C04 | OpenTelemetry Collector (ADOT) + RabbitMQ (telemetría local + broker de colas de Concepción) | 2 | 4 GB | 50 GB |
| **Total** | | **12 vCPU** | **24 GB** | **870 GB** |

---

### 1.4 Plataformas de Cross-Docking — Mini-PC Industrial (E-01)

Un nodo por plataforma: **Curicó, Chillán, Los Ángeles**. Sin hipervisor — contenedores Docker / Podman sobre Linux.

| Atributo | Especificación |
|---|---|
| **Tipo** | Mini-PC industrial rugoso (Advantech ARK-2250, Intel NUC Pro 12 Enterprise, AAEON BOXER-6641 o equiv.) |
| **CPU** | Intel Core i5 / i7 12ª gen (6–8 cores; rango temperatura industrial -20 °C a +60 °C) |
| **RAM** | 16 GB DDR4 SO-DIMM |
| **Almacenamiento SO** | 1 × SSD M.2 NVMe 256 GB |
| **Almacenamiento Datos** | 1 × SSD M.2 NVMe 512 GB (BD embebida + buffer broker local) |
| **Red** | 2 × 1GbE RJ-45 + **puerto WAN ethernet al router Starlink (enlace principal, D-06)** + **módulo 4G Cat-12 LTE DUAL SIM (respaldo, 2 proveedores distintos)** |
| **Temperatura de operación** | -20 °C a +60 °C (certificación industrial) |
| **Protección física** | IP40 mínimo en gabinete cerrado |
| **UPS** | Mini-UPS interna o UPS de riel DIN ≥ 30 min (RT-06.07); alimenta también el router Starlink del gabinete |
| **Gestión remota** | SSM Agent vía VPN Starlink/LTE (Zero Trust — sin puertos entrantes) |

> **Justificación de red redundante (RT-03.17 / RNF-13.07 en sitios solo-móvil):** en las plataformas de cross-docking no existe fibra (Cap. 6) y la red móvil es intermitente (Los Ángeles pierde señal entre 03:00–05:00, exactamente su ventana operacional). Para satisfacer RT-03.17 (caminos físicos y **proveedores distintos** con conmutación automática) se incorpora el **kit Starlink fijo (D-06) como enlace principal satelital** conectado por ethernet al switch compacto del gabinete, con el **módulo 4G Cat-12 LTE dual (2 proveedores) del mini-PC como respaldo automático**: la conmutación del satelital al LTE ocurre en < 5 min (objetivo < 30 s para la ventana operacional) y la operación del turno de 3 h es 100 % local (RT-03.10/RT-03.11), por lo que el enlace solo sostiene la sincronización diferida. Esta es la mitigación formal del SPOF de enlace declarado en Tabla v06 §4 y resuelve el caso crítico de Los Ángeles descrito en la Cotización Starlink.

**Software en nodo edge (contenedores):**

| Componente | Runtime | Descripción |
|---|---|---|
| Mini-WMS Edge | Docker | Recepción camión, desconsolidación, re-despacho, trazabilidad de lote |
| BD local | PostgreSQL 16 (single-node) | Transacciones del turno + buffer de sincronización diferida |
| Broker local | RabbitMQ | Cola de transacciones pendientes hacia WMS Talca |
| OpenTelemetry Collector (ADOT) | AWS Distro OT | Buffer de telemetría del nodo |
| Agente EDR | Agente liviano (F-03) | Monitoreo de comportamiento de procesos |

---

### 1.5 Resumen de Hardware — Totales On-Premise (corregidos)

| Sitio | Servidores / Dispositivos | vCPU asignados | RAM asignada | RAM física | Almacenamiento útil (datos) | IOPS de diseño |
|---|---|---|---|---|---|---|
| CD Talca (clúster 3 nodos N+1) | 3 × servidor 1U + 1 × NAS | 30 | 68 GB | **384 GB** (3 × 128 GB) | **5,76 TB pool Ceph (réplica 2, 3 nodos)** + 8 TB NAS (respaldo) | > 100.000 IOPS (NVMe RAID 10) |
| CD Concepción | 1 × servidor compacto 1U | 12 | 24 GB | **32 GB** | 1,92 TB RAID 10 | > 50.000 IOPS |
| Cross-Docking Curicó | 1 × Mini-PC industrial | 6 | 8 GB | 16 GB | 512 GB NVMe | > 10.000 IOPS |
| Cross-Docking Chillán | 1 × Mini-PC industrial | 6 | 8 GB | 16 GB | 512 GB NVMe | > 10.000 IOPS |
| Cross-Docking Los Ángeles | 1 × Mini-PC industrial | 6 | 8 GB | 16 GB | 512 GB NVMe | > 10.000 IOPS |
| **TOTAL** | **7 servidores/dispositivos de cómputo + 1 NAS** | **~60 vCPU** | **~116 GB asignados** | **464 GB físicos** | **~9,2 TB útiles datos + 8 TB NAS** | — |

> **Corrección de la v03:** los totales declarados anteriormente ("~68 vCPU", "~240 GB RAM", "~8,3 TB útiles") no se reproducían de la tabla de detalle (la RAM física era 2×128 = 256 GB en Talca, no 240). Con el clúster de 3 nodos (384 GB Talca) los totales reales son: **60 vCPU asignados**, **464 GB RAM físicos** y **~9,2 TB de almacenamiento útil de datos + 8 TB de NAS de respaldo**.

---

## PARTE 2 — EQUIPAMIENTO OPERACIONAL Y PERIFÉRICOS

---

### 2.1 Estaciones de Trabajo — Operación y Administración (RNF-23.04)

| Atributo | Especificación mínima |
|---|---|
| **Cantidad** | 5 en Talca (despacho, adm., planificación, calidad, TI) + 3 en Concepción |
| **CPU** | Intel Core i5 / i7 12ª gen o AMD Ryzen 5 / 7 equivalente |
| **RAM** | 16 GB DDR4 / DDR5 |
| **Almacenamiento** | SSD NVMe 512 GB — **cifrado de disco activado** (BitLocker / LUKS gestionado desde F-03 EDR) |
| **Monitores** | **2 × monitor 24" Full HD** (NCh 2527: iluminación, posición y ángulo ergonómico) |
| **Gestión centralizada** | Domain join o MDM; política aplicada vía Ansible (F-02) |
| **Conectividad** | 1GbE cableado a VLAN-Estaciones de Trabajo; Wi-Fi desactivado en estaciones de administración |

---

### 2.2 Terminales Rugosos de Bodega — Picking en Cámara de Congelado (RNF-05.02) — Zebra MC9400 Cold Storage

| Atributo | Especificación mínima | Justificación |
|---|---|---|
| **Cantidad** | 144 en Talca (120 operarios simultáneos + 20 % de reserva) + 30 en Concepción (25 + 20 %) | 38 % rotación anual; stock de repuesto (Cap. 4, 8) |
| **Modelo de referencia** | **Zebra MC9400 Cold Storage (modelo Freezer)** — certificado cámara frigorífica | Sustituye la referencia MC9300 Freezer de la v03 |
| **Temperatura de operación** | **−30 °C** (certificado freezer) | Cámara congelado −22 °C; margen de 8 °C |
| **Protección** | IP65 (polvo + chorro de agua) | Limpieza diaria con manguera en cámaras |
| **Resistencia a caídas** | Caídas sobre concreto (estándar industrial MIL-STD-810H) | Operación con guantes térmicos gruesos |
| **Pantalla** | ≥ 4" — táctil operable con guantes (gloves mode) o stylus; UI ≥ 15 × 15 mm (RNF-05.02) | |
| **Escáner** | **Lector SE58 de rango extendido (~100 pies)** para 1D/2D + GS1 (SSCC GS1-128, DataMatrix, QR) | RF-01.07: AI 01, 10, 17 |
| **Batería** | **Freezer 5.000 mAh**, ≥ 10 h turno, intercambiable en caliente; pistol grip | Turno 22:00–06:00 + margen |
| **Conectividad** | **Wi-Fi 6E (802.11ax) 2,4/5/6 GHz; BT 5.3**; Android 13→18 | VLAN-Operaciones; APs industriales en bodega |
| **Ciclo de vida** | Android 13→18 (soporte extendido) | Alineado a los 56 meses + operación |

---

### 2.3 Impresoras Térmicas de Andén — Etiquetas SSCC (RF-01.07) — Zebra ZT411

| Atributo | Especificación mínima |
|---|---|
| **Cantidad** | 4 en Talca (2 andenes recepción + 2 despacho) + 2 en Concepción |
| **Modelo de referencia** | **Zebra ZT411** (4" industrial) |
| **Tipo de impresión** | Transferencia térmica (TTR) — durable en frío y humedad |
| **Resolución** | 203 dpi mínimo (legibilidad GS1-128 garantizada) |
| **Velocidad** | ≥ 14 pulgadas/segundo |
| **Conectividad** | Ethernet 1GbE RJ-45 (VLAN-Operaciones) + USB local |
| **Protocolo** | **ZPL II + XML-Enabled Printing**; plataforma Print DNA |
| **Contenido de etiqueta** | GTIN (AI 01), N° de lote (AI 10), Vencimiento (AI 17), Recepción (AI 11) — RF-01.07 |
| **Ancho de etiqueta** | 4" (102 mm) — etiqueta estándar de pallet GS1 |

---

### 2.4 Balanza de Recepción — Dibal BEV (C-05)

| Atributo | Especificación mínima |
|---|---|
| **Cantidad** | 2 en Talca (andenes de recepción) + 1 en Concepción |
| **Modelo de referencia** | **Dibal BEV** — plataforma ME + indicador DMI-610 Inox |
| **Resolución** | 6.000 divisiones |
| **Interfaces** | **Doble RS-232**; Ethernet opcional; RS-485/422 |
| **Integración** | Captura de peso al Módulo M1 (RF-01.01) sin digitación manual; conexión en VLAN-Operaciones |
| **Uso** | Validación de unidades vs OC en recepción; soporte a detección de merma |

---

### 2.5 Terminal de Preventa — Zebra EC55 (C-01)

| Atributo | Especificación mínima |
|---|---|
| **Cantidad** | 62 + reserva 20 % (~75 unidades) |
| **Modelo de referencia** | **Zebra EC55** |
| **Peso / protección** | 173 g · **IP67** · **−10…+50 °C** |
| **Lector** | **2D SE4100** (lectura GS1 en punto de venta) |
| **Batería** | 4.180 mAh |
| **Sistema / soporte** | Android 14 · **8 años de soporte LifeGuard** (cubre 56 meses del contrato con holgura) |
| **Cámara** | Sí (RF-01.04: fotos de producto/promociones) |
| **App** | App Preventa Flutter offline-first (C-01) |

---

### 2.6 Terminal de Reparto — Zebra TC58e + Impresora ZQ620 Plus + POS PAX A920 Pro (C-02)

| Atributo | Especificación mínima — Terminal |
|---|---|
| **Cantidad** | Conductores propios 42 + pool conductores externos ~160 (parque único TC58e) + reserva |
| **Modelo de referencia** | **Zebra TC58e** (5G) |
| **Lector** | **SE55** (1D/2D) |
| **Batería** | Estándar + **batería extendida 7.000 mAh** (turno completo 14 h sin señal) |
| **Conectividad** | **BT 5.3 + BLE secundario** (sincro termógrafo B-03) · **GPS dual L1/L5** |
| **Protección** | **IP65/68** · caídas 2,4 m |
| **Sistema** | Android 13→17 (soporte extendido) |
| **App** | App Reparto Flutter offline-first (C-02) — POD foto/firma, QR, cobranza, devoluciones |

| Atributo | Especificación mínima — Impresora de cabina |
|---|---|
| **Modelo de referencia** | **Zebra ZQ620 Plus** (3" portátil) |
| **Protocolos** | **ZPL / EPL / CPCL** |
| **Batería** | PowerPrecision+ 3.250 mAh |
| **Gestión** | **Link-OS** (gestión remota centralizada RT-03.18) |
| **Protección** | **IP54** |

| Atributo | Especificación mínima — POS móvil de cabina |
|---|---|
| **Modelo de referencia** | **PAX A920 Pro** |
| **Sistema** | **Android 14** · **PCI PTS 7.x** · **EMV L1/L2** |
| **Impresora integrada** | 80 mm/s (comprobante en ruta, RF-22/DF) |
| **Batería** | 5.150 mAh |
| **Gestión** | **PAXSTORE** (gestión de terminales de pago, RT-03.18) |
| **Integración** | Cobro con tarjeta en ruta (RF-07.06) vía app de reparto (Bluetooth) |

---

### 2.7 Gateway IoT / Concentrador de Sensores de Temperatura (B-02)

| Atributo | Especificación mínima |
|---|---|
| **Cantidad** | 1 en Talca + 1 en Concepción |
| **Modelo de referencia** | Advantech ADAM-6000 series, Moxa MGate o equiv. compatible con AWS IoT Greengrass Core |
| **Puertos RS-485** | ≥ 4 puertos RS-485 (Modbus RTU) sobre los módulos Ebyte (B-01) |
| **CPU / RAM** | ARM Cortex-A53 / A72 o equiv.; ≥ 2 GB RAM; ≥ 32 GB eMMC |
| **Temperatura de operación** | -20 °C a +70 °C (montado en pared exterior de la cámara) |
| **Software** | AWS IoT Greengrass Core (procesamiento de telemetría offline) |

---

### 2.8 Sensores IoT de Temperatura — Ebyte ME31-XDXX0400 (B-01)

| Atributo | Especificación mínima |
|---|---|
| **Cantidad** | **7 módulos** (28 puntos de medición ≈ 7 × 4 canales) — Talca + Concepción |
| **Modelo de referencia** | **Ebyte ME31-XDXX0400** |
| **Canales** | **4 canales PT100 (2/3 hilos) por módulo**, montaje riel DIN |
| **Exactitud** | **±0,1 % ± 1 °C (25±5 °C); ±0,5 % ± 1 °C full range** → ≈ **±1,1 °C a −22 °C**; sonda **3 hilos** (compensación de resistencia de cable) |
| **Protocolo** | **RS-485 / Modbus RTU + Modbus TCP (Ethernet)** (red industrial cableada; cámara sin señal inalámbrica — Cap. 6) |
| **Muestreo** | **1 Hz** (muy por sobre los 30 s del caso) |
| **Rango** | **−40…+85 °C** (cámara −22 °C con margen) |
| **Integración** | Maestro Modbus → Gateway B-02 (Greengrass) → alerta de excursión térmica y bloqueo de despacho |

---

### 2.9 Termógrafos Digitales de Camión — Onset InTemp CX450 (B-03)

| Atributo | Especificación mínima |
|---|---|
| **Cantidad** | 18 (camiones con equipo de frío) |
| **Modelo de referencia** | **Onset InTemp CX450** |
| **Rango** | **−30…+70 °C ±0,5 °C** (multi-rango; GDP/GMP) |
| **Registro** | ~103.400 mediciones por unidad; reutilizable |
| **Conectividad** | **BLE** — sincroniza al terminal del conductor (TC58e) en ruta y al Gateway (B-02) en base |
| **Calibración** | **NIST 2 puntos** (evidencia auditable para Autoridad Sanitaria, Cap. 7.3) |
| **Batería** | AAA (reemplazable) |

---

### 2.10 Escáner de Mano GS1 — Cross-Docking (E-01) — Zebra DS2208

| Atributo | Especificación mínima |
|---|---|
| **Cantidad** | 6 (2 por plataforma de cross-docking) |
| **Modelo de referencia** | **Zebra DS2208** |
| **Lectura** | **1D/2D + GS1 DataBar** |
| **Decodificación** | **PRZM** (lectura brusca de códigos dañados) |
| **Interfaces** | USB / RS-232 / Keyboard Wedge |
| **Accesorio** | **Intellistand** (hands-free en mesa de desconsolidación) |
| **Garantía** | 60 meses |

---

## PARTE 3 — SEGMENTACIÓN DE RED Y DIRECCIONAMIENTO IP

---

### 3.1 Principios de Diseño (Zero Trust)

1. **Segmentación por función:** Ningún dispositivo de una VLAN puede alcanzar directamente a otro de una VLAN distinta sin pasar por el clúster de firewalls (D-01a/D-01b). No se permite enrutamiento directo inter-VLAN en el stack de switches core (D-02a/D-02b).
2. **Mínimo privilegio de red:** Cada VLAN tiene una ACL que permite únicamente los flujos estrictamente necesarios.
3. **IoT completamente aislado:** Los sensores RS-485 y el Gateway (B-01, B-02) no tienen acceso directo a Internet ni a la VLAN de Servidores. Solo el Gateway puede publicar hacia la nube a través de un proxy en el firewall.
4. **Gestión fuera de banda:** Los puertos IPMI/iDRAC/iLO de todos los servidores se conectan exclusivamente a la VLAN de Gestión.
5. **Sin puertos entrantes desde Internet:** Todo el tráfico hacia los nodos on-premise se inicia desde adentro (SSM Agent, VPN IPsec con BGP, OTel/ADOT).
6. **Segmentación inalámbrica (RT-03.23):** la red Wi-Fi de bodega separa dispositivos rugosos (MC9400) de APs de administración y de estaciones; autenticación por certificado de empresa; cobertura verificada por estudio de sitio.

---

### 3.2 Matriz de VLANs — CD Talca

| VLAN ID | Nombre | Función | Dispositivos miembros |
|---|---|---|---|
| **VLAN 10** | `MGT-TALCA` | Gestión fuera de banda | iDRAC/iLO servidores, puertos de gestión del stack de switches core (D-02a/D-02b), clúster de firewalls UTM (D-01a/D-01b), NAS (D-05) |
| **VLAN 20** | `SRV-TALCA` | Servidores y BD | VM-01 WMS, VM-02 PostgreSQL, VM-03 RabbitMQ, VM-04 ACL ERP, VM-05 Keycloak Auth Cache, VM-06 OTel/ADOT |
| **VLAN 30** | `OPS-TALCA` | Operaciones de bodega | Terminales rugosos MC9400 (C-03), impresoras ZT411 (C-04), balanzas Dibal (C-05), APs industriales bodega |
| **VLAN 40** | `WKS-TALCA` | Estaciones de trabajo | PCs de despacho, administración, planificación (RNF-23.04) |
| **VLAN 50** | `IOT-TALCA` | Industrial IoT | Gateway Greengrass (B-02), módulos Ebyte ME31 (B-01); **sin ruta a Internet directa** |

**Flujos permitidos entre VLANs (política firewall D-01):**

| Origen | Destino | Puerto / Protocolo | Propósito |
|---|---|---|---|
| VLAN 30 (OPS) → VLAN 20 (SRV) | TCP 8080 | API WMS — confirmación de misiones de picking |
| VLAN 40 (WKS) → VLAN 20 (SRV) | TCP 443 (HTTPS) | Portal WMS desde estaciones de trabajo |
| VLAN 50 (IOT) → VLAN 20 (SRV) | TCP 5672 (AMQP) | Gateway IoT publica eventos de temperatura al broker |
| VLAN 20 (SRV) → WAN (AWS VPN) | TCP 443 / AMQPS 5671 | Sincronización diferida; telemetría OTel/ADOT |
| VLAN 10 (MGT) → Todos | TCP 22 (SSH) / HTTPS 443 | Gestión administrativa; MFA obligatoria (RF-15.03) |
| Todos → VLAN 20 (SRV): TCP 636 | LDAPS (caché Keycloak local) | Autenticación SSO usuarios (RF-15.02) |

---

### 3.3 Matriz de VLANs — CD Concepción

| VLAN ID | Nombre | Función |
|---|---|---|
| **VLAN 11** | `MGT-CONCEP` | Gestión fuera de banda (IPMI, switch, firewall de borde) |
| **VLAN 21** | `SRV-CONCEP` | VMs WMS Edge, PostgreSQL local, Keycloak Auth Cache (réplica), OTel/ADOT |
| **VLAN 31** | `OPS-CONCEP` | Terminales MC9400, impresoras y balanza de andén |
| **VLAN 41** | `WKS-CONCEP` | Estaciones de trabajo |
| **VLAN 51** | `IOT-CONCEP` | Gateway IoT local (módulos Ebyte) |

---

### 3.4 Matriz de VLANs — Plataformas Cross-Docking (Curicó, Chillán, Los Ángeles)

Red plana simplificada (gabinete de borde operacional, volumen reducido):

| VLAN ID | Nombre | Función |
|---|---|---|
| **VLAN 60** | `MGT-CDK` | Gestión del mini-PC (acceso SSM Agent via 4G) |
| **VLAN 70** | `OPS-CDK` | Mini-WMS edge + escáneres de mano GS1 (DS2208) |

---

### 3.5 Asignación de Rangos IP Privados (RFC 1918)

| Sitio | VLAN | Nombre | Red | Máscara | Gateway | Hosts disponibles |
|---|---|---|---|---|---|---|
| **CD Talca** | 10 | MGT-TALCA | 10.1.10.0 | /24 | 10.1.10.1 | 253 |
| | 20 | SRV-TALCA | 10.1.20.0 | /24 | 10.1.20.1 | 253 |
| | 30 | OPS-TALCA | 10.1.30.0 | /24 | 10.1.30.1 | 253 (144 terminales + impresoras + balanzas + APs) |
| | 40 | WKS-TALCA | 10.1.40.0 | /24 | 10.1.40.1 | 253 |
| | 50 | IOT-TALCA | 10.1.50.0 | /24 | 10.1.50.1 | 253 (7 módulos Ebyte + 1 gateway) |
| **CD Concepción** | 11 | MGT-CONCEP | 10.2.10.0 | /24 | 10.2.10.1 | 253 |
| | 21 | SRV-CONCEP | 10.2.20.0 | /24 | 10.2.20.1 | 253 |
| | 31 | OPS-CONCEP | 10.2.30.0 | /24 | 10.2.30.1 | 253 |
| | 41 | WKS-CONCEP | 10.2.40.0 | /24 | 10.2.40.1 | 253 |
| | 51 | IOT-CONCEP | 10.2.50.0 | /24 | 10.2.50.1 | 253 |
| **Cross-Docking Curicó** | 60/70 | CDK-CURICO | 10.3.0.0 | /24 | 10.3.0.1 | 253 |
| **Cross-Docking Chillán** | 60/70 | CDK-CHILLAN | 10.4.0.0 | /24 | 10.4.0.1 | 253 |
| **Cross-Docking Los Ángeles** | 60/70 | CDK-LOSANG | 10.5.0.0 | /24 | 10.5.0.1 | 253 |
| **AWS VPCs (Hub + Ambientes)** | VPC-AWS | 10.100.0.0 – 10.104.0.0 | /16 c/u | — | VPC Hub (10.100) + Prod (10.101) a Dev (10.104) |

**Espacio de direccionamiento total:** 10.1.0.0–10.5.255.255 (On-Premise) + 10.100.0.0/16 a 10.104.0.0/16 (AWS Hub y Ambientes) — sin solapamiento entre sitios ni con AWS.

---

### 3.6 Túneles IPsec Redundantes hacia AWS

Cada CD (Talca y Concepción) establece una **AWS Site-to-Site VPN** con **2 túneles IPsec activos** hacia el Virtual Private Gateway (VGW) de AWS, conforme a RNF-13.07. El **SD-WAN del firewall (D-01)** selecciona el camino activo entre **fibra (D-03), Starlink (D-06) y LTE (D-04)**; los dos túneles activos corren sobre los dos mejores caminos del momento (fibra + Starlink) y el tercero queda disponible como camino alterno sin pérdida de sesión.

```
CD Talca                                     AWS Region
──────────────────────────                   ──────────────────────
Clúster HA Firewalls UTM (D-01a/D-01b)       Virtual Private Gateway
(Activo/Pasivo — Customer Gateway) ──Túnel 1 / IKEv2──▶  Endpoint AZ-a (fibra D-03)
IP pública fibra D-03  AES-256-GCM / SHA-256
                      ──Túnel 2 / IKEv2──▶  Endpoint AZ-b (Starlink D-06)
IP pública Starlink    BGP failover < 30 s
                      ··· Camino alterno IKEv2 ···> Endpoint AZ-b (LTE D-04)
                      IP pública SIM LTE    SD-WAN/QoS: respaldo de respaldo
```

| Parámetro | Túnel Primario | Túnel Secundario | Camino alterno |
|---|---|---|---|
| **Interfaz física** | Fibra óptica (D-03) | **Starlink satelital (D-06)** | LTE empresarial (D-04) — activo solo si fallan D-03 y D-06 |
| **IP Customer Gateway (VIP del clúster HA)** | IP pública fibra | IP pública terminal Starlink | IP pública SIM LTE |
| **IP AWS VGW** | Endpoint AZ-a (asignado por AWS) | Endpoint AZ-b (asignado por AWS) | Endpoint AZ-b (mismo o VPN adicional del VGW) |
| **Protocolo** | IPsec IKEv2 | IPsec IKEv2 | IPsec IKEv2 |
| **Cifrado** | AES-256-GCM | AES-256-GCM | AES-256-GCM |
| **Autenticación** | SHA-256 | SHA-256 | SHA-256 |
| **Grupo DH** | Group 14 (2048-bit) mínimo | Group 14 | Group 14 |
| **Enrutamiento** | BGP (AS on-premise: 65001) | BGP (AS on-premise: 65001) | BGP (AS on-premise: 65001) |
| **Conmutación** | — | < 30 s (BFD + reconvergencia BGP) | SD-WAN QoS; manual/automático por monitor de enlace |
| **Failover de la unidad de firewall** | Activo/Pasivo con sincronización de sesiones (túneles IPsec, BGP, NAT); la pasiva asume las VIPs en < 30 s | Ídem | Ídem |
| **Tráfico en respaldo** | — | Solo si cae D-03: VPN sync broker A-03 + SSM F-01 + OTel telemetría + sync WMS/BD | Solo si caen D-03 y D-06: broker + SSM + OTel (tráfico crítico) |
| **MTU** | 1.436 bytes | 1.436 bytes | 1.436 bytes |

> **Nota cross-docking:** los 3 cross-docks no levantan túnel IPsec hacia el VGW (salida directa a SQS/IoT/SSM por Starlink/4G, D-AL-04); el enlace Starlink principal (D-06) y el LTE dual del mini-PC sostienen esa salida y la sincronización AMQPS del broker hacia Talca. Si se requiere VPN en un cross-dock, el mini-PC puede levantar el mismo túnel sobre el camino Starlink sin cambios de hardware.

**Flujos principales por la VPN:**

| Flujo | Origen | Destino | Protocolo |
|---|---|---|---|
| Sync broker → nube | VM-03 SRV-TALCA | SQS / Amazon MQ AWS | AMQPS 5671 |
| Telemetría OTel | VM-06 SRV-TALCA | CloudWatch / X-Ray / AMP | HTTPS 443 |
| Greengrass Core → IoT Core | IOT-TALCA Gateway | AWS IoT Core | MQTTS 8883 |
| SSM Agent (gestión remota) | Todos los nodos | SSM Endpoint (regional) | HTTPS 443 saliente |
| Sync WMS Concepción → Talca | SRV-CONCEP | SRV-TALCA | TCP 8080 / 5432 |
| Sync cross-docking → Talca | CDK-xx (VPN 4G dual) | SRV-TALCA | AMQPS 5671 |

---

### 3.7 Ancho de Banda Dimensionado por Sitio (RNF-13.08)

| Sitio | Régimen normal | Peak (septiembre) | Justificación |
|---|---|---|---|
| **CD Talca — fibra primaria (D-03)** | 20 Mbps simétrico | 50 Mbps simétrico | 2.600 entregas × ~15 KB/tx = 312 MB/h peak; telemetría IoT 28 sensores × 1 msg/30 s × 500 B ≈ 1 Mbps; margen para actualizaciones y SSM |
| **CD Talca — Starlink respaldo (D-06)** | **Plan 1 TB prioritario** (~50–100 Mbps); conmutación automática al caer D-03 | Ídem | Respaldo preferente de Talca (Fibra se corta hasta 4×/año por hasta 6 h, Cap. 6); sostiene la VPN completa + sync broker + SSM + telemetría durante el corte (RT-03.17, RT-03.10) |
| **CD Talca — LTE terciario (D-04)** | 5 Mbps (solo tráfico crítico) | 10 Mbps | Broker sync + SSM Agent únicamente si fallan D-03 y D-06 |
| **CD Concepción — fibra (D-03)** | 10 Mbps simétrico | 20 Mbps simétrico | Volumen proporcional a Talca |
| **CD Concepción — Starlink respaldo (D-06)** | **Plan 1 TB prioritario**; conmutación automática al caer D-03 | Ídem | **Cierra la brecha de Concepción (RNF-13.07)**: antes "nuevo enlace requerido" — actualmente sin respaldo; el satelital provee el respaldo automático sin depender de nueva obra móvil (RT-03.17) |
| **CD Concepción — LTE terciario (D-04)** | 3 Mbps | 5 Mbps | Camino alterno sobre red móvil (proveedor distinto a D-03) |
| **Cross-Docking (c/u) — Starlink principal (D-06)** | **Plan 500 GB prioritario** | Ídem | Enlace principal satelital: resuelve la intermitencia de señal móvil de **Los Ángeles entre 03:00–05:00** (ventana operacional) y la dependencia exclusiva de red móvil en Curicó/Chillán; sync ventana 3 h + manifiesto pre-cargado |
| **Cross-Docking (c/u) — LTE dual respaldo** | 2 Mbps (LTE 4G) | 5 Mbps (LTE 4G) | Respaldo automático del módulo 4G Cat-12 del mini-PC (**2 proveedores, conmutación automática — RT-03.17** y cotización Starlink) |

> **Fuente del nuevo camino:** `Cotizacion_Starlink_Sucursales_56meses.docx.md` (05-09-2026). Con el satelital, el hueco histórico de Concepción ("nuevo enlace requerido") y el caso crítico de Los Ángeles quedan cubiertos por enlace físico independiente de la red móvil/terrestre.

---

### 3.8 Alta disponibilidad de la red del sitio principal (RT-08.03)

El CD Talca no admite equipos únicos de perímetro ni de distribución (RT-08.03). La red del sitio principal se corrige de la siguiente forma:

| Equipo | Cantidad | Configuración HA |
|---|---|---|
| Firewall UTM / Customer Gateway (D-01) | 2 | Clúster **Activo/Pasivo** con sincronización de sesiones (NAT, VPN IPsec, BGP, UTM). La unidad pasiva asume las VIPs y los túneles en < 30 s. **SD-WAN multi-WAN**: 3 interfaces WAN (fibra D-03 · Starlink D-06 · LTE D-04) con selección automática de camino y QoS (RT-03.24). Cada unidad se conecta a circuitos eléctricos distintos (RT-08.04) y a PDU A/B |
| Switch core L3 (D-02) | 2 | **Stack / MLAG**: ambos switches operan como un único plano de distribución. Servidores, firewalls y APs se conectan con LACP/MLAG repartido entre ambos miembros; la caída de un miembro no interrumpe el tráfico |

Con esta configuración quedan eliminados los puntos únicos de falla en el perímetro y en la distribución del sitio principal (RT-08.03). El cableado estructurado certificado y el esquema de racks/energía se detallan en **Sala_Servidores_OnPremise_v02**.

---

## PARTE 4 — INVENTARIO CONSOLIDADO DE HARDWARE

---

### 4.1 Servidores y Dispositivos (cómputo y red)

| Sitio | Elemento | Cant. | Modelo de referencia |
|---|---|---|---|
| CD Talca | Servidor clúster (Nodo-1) | 1 | Dell PowerEdge R6615 / HPE ProLiant DL325 Gen11 (1U, EPYC 16c/32t, 128 GB) |
| CD Talca | Servidor clúster (Nodo-2) | 1 | Ídem |
| CD Talca | Servidor clúster (Nodo-3) | 1 | Ídem |
| CD Talca | NAS Respaldo Local D-05 (recuperación rápida) | 1 | Synology RS1221RP+ (WORM local refuerzo; pierna inmutable en AWS) |
| CD Talca | Switch Core L3 con VLANs — Stack/MLAG | 2 | Cisco Catalyst 9300-48P (StackWise) o equiv. |
| CD Talca | Firewall UTM / Customer GW — clúster HA Activo/Pasivo | 2 | FortiGate 60F HA A/P / Palo Alto PA-220 A/P o equiv. |
| CD Talca | AP Wi-Fi 6E industrial (bodega) | 6 | Cisco Catalyst 9115 / Aruba AP-515 |
| CD Talca | Gateway IoT + Greengrass | 1 | Advantech ADAM-6000 + Greengrass Core |
| CD Talca | **Kit Starlink fijo (respaldo D-06)** | 1 | Starlink Enterprise fijo (estándar/alto rendimiento): antena techumbre + router, plan 1 TB prioritario (Cotización Starlink) |
| CD Concepción | Servidor borde compacto | 1 | Dell R250 / HPE DL20 Gen11 |
| CD Concepción | Firewall de borde | 1 | FortiGate 40F o similar |
| CD Concepción | AP Wi-Fi 6E industrial | 3 | Cisco Catalyst 9115 |
| CD Concepción | Gateway IoT + Greengrass | 1 | Ídem Talca |
| CD Concepción | **Kit Starlink fijo (respaldo D-06)** | 1 | Ídem Talca (cierra RNF-13.07) |
| Cross-Docking (×3) | Mini-PC industrial rugoso (**enlace principal Starlink + LTE dual respaldo**) | 3 | Advantech ARK-2250 / Intel NUC Pro 12 |
| Cross-Docking (×3) | Switch compacto | 3 | Netgear GS308E o similar |
| Cross-Docking (×3) | **Kit Starlink fijo (enlace principal D-06)** | 3 | Ídem; plan 500 GB prioritario; antena techumbre + router → switch compacto |

> **Nota enlaces WAN consolidados (D-03/D-06/D-04):** fibra primaria en CDs (D-03) + satelital Starlink (D-06) como respaldo automático de CDs y principal de cross-docks + LTE (D-04) como camino alterno/terciario (dual 2 proveedores en cross-docks). Detalle de ancho de banda en §3.7. Los **5 kits Starlink** (2 CDs + 3 cross-docks) se incorporan al inventario de HW según la Cotización Starlink 05-09-2026 y se respaldan en el plan de reposición (§6.3, RT-08.13: reposición de hardware 15 % / 56 meses).

### 4.2 Dispositivos de Terreno (Tabla v06 §4)

| Sitio | Elemento | Cant. | Modelo de referencia |
|---|---|---|---|
| Talca + Concepción | Terminal rugoso picking (freezer) | 144 Talca + 30 Concepción | **Zebra MC9400 Cold Storage (Freezer)** |
| Talca / Concepción | Impresora térmica andén | 4 / 2 | **Zebra ZT411** |
| Talca / Concepción | Balanza recepción | 2 / 1 | **Dibal BEV** (ME + DMI-610 Inox) |
| Preventa | Terminal preventa | 62 + 20 % | **Zebra EC55** |
| Reparto | Terminal reparto (parque único: propios + externos) | 42 + ~160 + reserva | **Zebra TC58e** (5G, SE55, bat. 7.000 mAh) |
| Cabina | Impresora térmica portátil | Por camión | **Zebra ZQ620 Plus** |
| Cabina | POS móvil Bluetooth | Por camión | **PAX A920 Pro** |
| Cross-Docking (×3) | Escáner de mano GS1 | 6 (2/sitio) | **Zebra DS2208** |
| Cámaras (IoT) | Sensor de temperatura (módulo 4 canales) | 7 módulos (28 puntos) | **Ebyte ME31-XDXX0400** |
| Frío en ruta | Termógrafo de camión | 18 | **Onset InTemp CX450** |
| Oficinas | Estación de trabajo + 2 monitores | 5 Talca + 3 Concepción | PC + 2 × 24" Full HD |

### 4.3 Máquinas Virtuales — Resumen

| VM | Sitio | Rol | vCPU | RAM | Datos |
|---|---|---|---|---|---|
| VM-01 | Talca | WMS Core | 8 | 16 GB | 100 GB |
| VM-02 | Talca | PostgreSQL BD (maestro → réplica Aurora) | 8 | 32 GB | 1.500 GB |
| VM-03 | Talca | RabbitMQ Broker | 4 | 8 GB | 200 GB |
| VM-04 | Talca | ACL ERP (frontera única) | 4 | 4 GB | 20 GB |
| VM-05 | Talca | **Keycloak Local Auth Cache / Offline Proxy (Modelo B)** | 4 | 4 GB | 20 GB |
| VM-06 | Talca | OTel Collector (ADOT) + SSM Agent | 2 | 4 GB | 50 GB |
| VM-C01 | Concepción | WMS Edge | 4 | 8 GB | 300 GB |
| VM-C02 | Concepción | PostgreSQL local | 4 | 8 GB | 500 GB |
| VM-C03 | Concepción | **Keycloak Auth Cache (réplica local, Modelo B)** | 2 | 4 GB | 20 GB |
| VM-C04 | Concepción | OTel (ADOT) + RabbitMQ | 2 | 4 GB | 50 GB |
| **TOTAL** | | | **42 vCPU** | **92 GB** | **2.760 GB** |

---

## PARTE 5 — RECUPERACIÓN ANTE DESASTRES Y CONTINUIDAD (CAP. 7)

> Las PARTES 5 a 10 cierran las brechas obligatorias detectadas en la Matriz de Cumplimiento BTT (on-premise) para los capítulos 7, 8, 9, 10, 11, 12 y 14. Los procedimientos de alcance híbrido/nube se declaran aquí como compromiso on-premise y se articulan con los documentos de nube y de arquitectura lógica del consolidado.

### 5.1 Modalidad de DR declarada (RT-07.01)

| Par Rol | Rol | Modalidad | Justificación (RTO/costo) |
|---|---|---|---|
| Talca (CD principal) | **Activo** — operación normal | — | Menor latencia, WMS maestro (A-01/A-02) |
| Réplica Aurora (nube, AWS) | **Pasivo (promueble)** | Activo-Pasivo | RTO ≤ 4 h / RPO ≤ 15 min; costo OPEX de réplica sin sobredimensionar cómputo on-premise |
| Concepción (edge) | **Activo local autónomo** (opera 24 h aunque Talca caiga) | Activo-Pasivo regional + autónomo | Mantiene la operación del Biobío sin depender del enlace; no compite por el rol primario |

Se declara **modalidad activo-pasivo** entre el sitio primario (Talca, activo) y la réplica de continuidad en la nube (pasiva promueble), más la instancia edge de Concepción **activa de forma autónoma para su propia operación** (justificada por RNF-13.01: 24 h de autonomía y por el costo de habilitar un sitio secundario on-premise completo). No se implementa activo-activo por el costo de doblar cómputo y el perfil de carga (un turno por sitio, ventanas sin solapamiento).

### 5.2 Distancia del sitio secundario y amenazas comunes (RT-07.02)

| Par | Distancia aprox. | Amenazas comunes evaluadas |
|---|---|---|
| Talca ↔ Nube AWS sa-east-1 (São Paulo) | ~2.300 km (dos regiones/países) | Sin eventos sísmicos/eléctricos en común; degradación regional de cable submarino (mitigada por caminos WAN de tecnologías distintas: fibra D-03 + **satelital Starlink D-06** + LTE D-04) |
| Talca ↔ Concepción (edge) | ~250–400 km | Terremoto/maremoto de zona costera (ambas regiones); corte eléctrico en malla nacional; incendio en instalación — sin dependencia de red entre ambas (operación autónoma 24 h) |
| Cross-docking (Curicó, Chillán, Los Ángeles) | Local a Talca (60–280 km) | Corte eléctrico local y de red móvil; la ventana de 3 h es 100 % local (RT-03.10/03.11) |

Se declara análisis formal de amenazas comunes: **no existe un evento único que derribe simultáneamente Talca, la nube y la instancia edge** (distintas regiones físicas y distintos contribuyentes de red/energía). En el improbable caso de doble afectación Talca+nube, Concepción queda operando autónoma 24 h y re-sincroniza al restablecerse (RPO ≤ 15 min).  <a name="parte5"></a>

### 5.3 Replicación con medición y alerta de retraso (RT-07.03)

- **Mecanismo:** streaming del log WAL de PostgreSQL de VM-02 (Talca) hacia la réplica Aurora (RPO ≤ 15 min), vía VPN IKEv2/AES-256 (3.6); replicación Ceph síncrona intra-clúster (1.2.5).
- **Medición y alertamiento:** se miden continuamente el **lag de replicación** (bytes y segundos) y el estado del WAL; **alerta automática al NOC y al Jefe de TI** si el lag supera los **5 minutos** (umbral intermedio) o los **15 minutos** (RPO declarado, alarma prioridad alta). Métrica expuesta en Prometheus/Grafana y correlacionada en la plataforma OTel (F-01).
- El repliegue del retardo a cero se verifica en la prueba DR semestral (5.6).

### 5.4 Procedimiento de conmutación documentado y automatizado (RT-07.05)

Procedimiento **documentado, probado y en lo posible automatizado** de conmutación (DR) y de conmutación regional:

| Paso | Acción | Responsable | Tiempo |
|---|---|---|---|
| 1 | Detección de indisponibilidad de Talca (alarma OTel/CloudWatch + NOC) | Monitoreo | < 1 min |
| 2 | Verificación cruzada del estado (healthcheck WMS, BD, enlace) para descartar falso positivo | NOC | ≤ 5 min |
| 3 | Decisión de conmutación con autorización del Jefe de TI on-call y el ADJUDICATARIO | Jefe de TI | ≤ 10 min |
| 4 | Promoción de la réplica Aurora a maestro (failover de la BD); DNS dirijo a DR | Runbook automatizado (semi-automático) | ≤ 30 min |
| 5 | Reconexión del broker A-03 y sincronización diferida de cross-docking/borde hacia el DR | Broker/ACL | simultáneo |
| 6 | Validación funcional de la transacción crítica de negocio e2e | Calidad/Operación | ≤ 4 h (RTO) |

El runbook vive en el sistema de gestión de cambios (Ansible — F-02) versionado, con checklists de rollback y tiempos medidos de la última prueba DR.  <a name="parte5d"></a>

### 5.5 Procedimiento de retorno con reconciliación de datos (RT-07.06)

| Paso | Acción |
|---|---|
| 1 | Reponer Talca (energía, red, clúster) con conmutación controlada: Talca vuelve a ser maestro |
| 2 | **Ventanilla de escritura única:** congelar escrituras de borde/cross-docking en DR y redirigir a Talca |
| 3 | **Reconciliación determinista** (RT-03.12): broker A-03 y colas de borde drenan en orden cronológico de timestamp local; resolución de conflictos de stock por regla definida (prevalencia de contadores físicos + bitácora) |
| 4 | Verificación de integridad (checksum de lotes y trazabilidad) y cierre de hueco de datos; validar lag = 0 |
| 5 | Informe de retorno al CLIENTE con tiempos y resultados; revisión post-mortem del evento |

### 5.6 Formato de informe de prueba DR y plan de corrección (RT-07.07)

Prueba DR **2 veces al año** (semestral — Art. 20; D 1.2.4). El informe entregable al CLIENTE incluye: fecha/ventana, alcance (restauración desde D-05, promoción Aurora, sync broker, medición eléctrica RT-06.10), **RTO y RPO medidos** (objetivo: RTO ≤ 4 h, RPO ≤ 15 min), resultados por paso, desviaciones, **plan de corrección con plazo y responsable** (observaciones cerradas en la siguiente prueba), y firmas. Se declara el compromiso de que una prueba fallida no se da por aprobada: se corrige y se reprueba dentro del mismo semestre.

### 5.7 Respaldos cifrados en reposo y en tránsito (RT-07.10)

| Destino del respaldo | Cifrado en reposo | Cifrado en tránsito | Gestión de clave |
|---|---|---|---|
| NAS local D-05 (copia rápida) | **Cifrado del volumen (LUKS/SED)** en las 4× HDD RAID 6 | Red VLAN-Servidores cifrada (VPN/IPsec intra-sede) | Clave **CMK propia (KMS), independiente de las claves de producción**; copia de emergencia de la clave bajo custodia del CLIENTE |
| Réplica Aurora (nube) | SSE-KMS de AWS (CMK dedicada) | TLS 1.3 / VPN IKEv2 (3.6) | CMK KMS en AWS con rotación anual |
| Copia inmutable S3 (Object Lock / Vault Lock) | **SSE-KMS (S3)** | TLS 1.3 en tránsito | CMK KMS; sellada por Vault Lock |

La clave de respaldo es **independiente de las claves de cifrado de datos de producción** (RT-07.10 / RT-11.09): un compromiso del cifrado operacional no expone los respaldos históricos. Restauración verificada mensualmente ("0 errores", RNF-20.07).

### 5.8 Tabla por dominio: frecuencia, retención y restauración (RT-07.13)

| Dominio de datos | Frecuencia de respaldo | Retención | Tiempo de restauración objetivo |
|---|---|---|---|
| BD transaccional WMS (inventario, lotes, trazabilidad) | WAL continuo (RPO ≤ 15 min) + completo diario 02:00–04:00 | 30 días en D-05 · 6 años tributario (RNF-01.02) / 5 años sanitario (RNF-09.02) en nube | ≤ 4 h (restauración completa) · ≤ 1 h (PITR) |
| Broker de colas / mensajes | Completo diario en ventana de mantenimiento | 30 días | ≤ 4 h |
| Configuración de red/seguridad (VLANs, firewall, túneles) | Completo semanal (export) | 12 meses | ≤ 2 h |
| Logs y auditoría | Streaming continuo a SIEM/bucket | 12 meses en línea + 24 meses archivados (RT-11.14) | ≤ 4 h |
| Telemetría IoT (cadena de frío) | Continuo (buffer 14 h) + diario | 2 años (Autoridad Sanitaria) | ≤ 4 h |
| POD (foto/firma), documentos tributarios | Sincronización diaria a nube | Según normativa DTE/contable | ≤ 4 h |

### 5.9 Restauración granular (RT-07.14 — Deseable)

Se declara soporte de restauración **granular** habilitado por la tecnología: PITR de PostgreSQL (restauración a un punto en el tiempo), recuperación de tablas/registros desde el WAL, y restauración a nivel de archivo/snapshot en el NAS D-05 y S3. Política de prueba mensual incluye al menos un caso de restauración granular.

---

## PARTE 6 — MONITOREO DE MEDIOS, CICLO DE VIDA Y GARANTÍAS (CAP. 8)

### 6.1 Monitoreo predictivo de salud de almacenamiento (RT-08.02)

Capa de **monitoreo predictivo (S.M.A.R.T. y equivalente NVMe)** sobre todos los medios de almacenamiento, con alertamiento automático antes del fallo:

| Medio | Monitoreo | Acción ante umbral |
|---|---|---|
| SSD/NVMe del clúster (RAID 1/RAID 10, OSDs Ceph) | **S.M.A.R.T.** / NVMe Health + predictor de retiro (wear-leveling, reallocated sectors, media errors) vía Proxmox/Ceph | Reemplazo preventivo del disco y reconstrucción automática (Hot-Spare); alerta al NOC |
| HDD del NAS D-05 (RAID 6) | S.M.A.R.T. + scrub mensual de integridad (RAID consistency check) | Sustitución preventiva antes de la pérdida de 2ª tolerancia; verificación de restauración mensual |
| SSDs de borde (Concepción, mini-PC cross-docking) | S.M.A.R.T. vía agente gestionado (SSM/F-02) | Reemplazo preventivo con stock seco declarado |

Los tres medios del esquema 3-2-1-1-0 con `0 errores` (D 1.2.4) se refuerzan con este monitoreo predictivo; el objetivo es **reemplazar antes de fallar**, no detectar después.

### 6.2 Procedimiento de ampliación documentado (RT-08.05)

Margen de crecimiento declarado por recurso (D 1.2.3: 47 % vCPU N+1, 73 % RAM, 68 % pool Ceph; reserva 20–30 % por rack — S §6). Procedimiento de ampliación cuando un recurso supere el 70 % de utilización sostenida (2 semanas):

| Paso | Acción | Plazo |
|---|---|---|
| 1 | Diagnóstico y propuesta de ampliación (informe de utilización) | 10 días hábiles |
| 2 | Aprobación del CLIENTE (CAPEX/OPEX según corresponda) | 5 días hábiles |
| 3 | Pedido y recepción de hardware (nodo adicional, OSD, NAS, enlace) | 30–60 días |
| 4 | **Ampliación no disruptiva:** alta en caliente de OSD Ceph / nodo (live migration, sin cortar la ventana operacional) | 1–2 días hábiles |
| 5 | Verificación y actualización del inventario/ DCIM | Inmediato |

Escala a 3 años proyectada: nuevo nodo (1U) simple para Talca; NAS adicional para retención creciente; aumento de enlace al peak de 2.600 entregas.

### 6.3 Equipamiento nuevo, sin uso previo y garantía de fábrica (RT-08.06)

Todos los equipos (servidores, NAS, red, dispositivos de terreno) son **nuevos, sin uso previo** (0 h de operación al momento de la entrega) y con **garantía de fábrica vigente** durante el período exigido (56 meses). Garantías destacadas: servidores 5 años NextBusinessDay, NAS 5 años, DS2208 60 meses, MC9400/TC58e/EC55 con plan Zebra OneCare Plus; la cobertura de garantía y soporte se detalla por dispositivo en Tabla v06 §4.1/§4.2.

### 6.4 Eficiencia energética de estaciones y equipos (RT-08.08)

- Monitor dual por estación con **certificación Energy Star**; equipos con **fuentes 80 Plus Gold o superior** (servidores, NAS y estaciones).
- PUE de diseño 1,7 con medición continua (S §5.4); climatización con free cooling (S §5.3).
- Fase fuera de horario: políticas de suspensión en estaciones y consolidación de VMs (overcommit cero, pero apagado programado de VMs no críticas fuera del turno).

### 6.5 Control de dispositivos extraíbles (RT-08.09)

| Control | Implementación |
|---|---|
| **Bloqueo USB por defecto** | Todo puerto USB de estaciones y servidores **en whitelist**: solo periféricos autorizados (teclado, mouse, escáner, lectores, impresoras). Dispositivos de almacenamiento extraíble **bloqueados por política** impuesta vía EDR (F-03) y Ansible (F-02) |
| Autorización excepcional | Memorias USB cifradas de uso autorizado con registro en inventario de medios (RT-06.28) y cifrado de contenido |
| Bitácoras | Eventos de inserción/expulsión de dispositivos a SIEM, con alerta de anomalías (pasado el alto, horario no hábil) |
| En terreno | Terminales de terreno con hardware cerrado (sin acceso físico del usuario a puerto OTG) y MAM que fuerza la app gestionada |

### 6.6 Garantías y niveles de reemplazo (§ 8.4 de las Transversales)

Compromiso formal del PROPONENTE por los 56 meses (detallado por dispositivo en **Tabla v06 §4.2**):

| Elemento | Compromiso |
|---|---|
| Hardware crítico | Soporte **24×7**, atención en sitio y resolución en **≤ 4 h** |
| Hardware no crítico | Soporte en horario hábil, resolución en **≤ 24 h** |
| Software de base | Soporte continuo del fabricante durante todo el contrato |
| Stock de repuestos | **≥ 10 % del parque** por tipo de componente crítico, **disponible en Chile** |
| Reemplazo de componente crítico | **≤ 4 h** desde la confirmación del diagnóstico |
| Dispositivos de terreno | **Stock en sitio = 10 % del parque** por modelo, con configuración precargada |

### 6.7 Plan de ciclo de vida del equipamiento (RT-08.16)

Plan completo por equipo, documentado y versionado en la herramienta de gestión (F-02):

| Etapa | Actividad | Entregable |
|---|---|---|
| **Recepción** | Inspección, verificación de nuevo/sin uso, inventario fotográfico, registro en DCIM/CMDB | Acta de recepción |
| **Puesta en servicio** | Instalación, configuración base (CIS), primera carga, pruebas funcionales | Checklist puesta en servicio |
| **Mantención** | Mantenimiento preventivo programado (clima/UPS termografía semestral RT-06.10, discos SMART, firmware/parches) | Bitácora de mantención |
| **Actualización** | Parches de seguridad y firmware en ventana nocturna sin interrupción (RT-10.05/10.06) | Registro de cambios |
| **Retiro** | **Borrado seguro verificable (6.8)** y baja del inventario | Certificado de sanitización |
| **Disposición final** | Entrega a gestor autorizado conforme a normativa (6.9) | Certificado de disposición |

### 6.8 Borrado seguro y verificable de medios que salen de servicio (RT-08.17)

- Todo medio de almacenamiento retirado (HDD/SSD/NVMe, NAS, terminales con memoria interna, cintas/medios removibles) pasa por **sanitización verificable** (los estándares NIST SP 800-88 / DoD 5220.22-M, con verificación post-borrado).
- El CLIENTE recibe un **certificado de destrucción o de sanitización** de cada medio, con número de serie, método, fecha y responsable.
- Los medios que no permitan sanitización confiable se **destruyen físicamente** con certificado de destrucción (RT-11.14 mantiene el registro del evento para auditoría).

### 6.9 Disposición final con gestor autorizado (RT-08.18)

- La disposición final del equipamiento electrónico se realiza con **gestor autorizado** por la autoridad ambiental (REP — Ley 20.920 y normativa de residuos aplicable), con traslado trazable (guía electrónica).
- Se entrega al CLIENTE el **certificado de disposición final** de cada equipo, en coherencia con el plan de ciclo de vida (6.7).

### 6.10 Reacondicionamiento y extensión de vida útil (RT-08.19 — Deseable)

Se valora la **reutilización interna** de equipos retirados en buen estado (terminales reacondicionadas como pool de respaldo no crítico, monitores a bodega de repuestos) cuantificada en la oferta económica como reducción de CAPEX de reposición; aplica solo a equipos con certificado de sanitización previo.

> **Costo unitario (RT-08.10):** el detalle de marca, modelo, cantidad, características, accesorios, consumibles y **costo unitario estimado (USD referencial)** de los dispositivos de terreno está en **Tabla v06 §4**, y el inventario físico consolidado en PARTE 4 de este documento.

---

## PARTE 7 — DISPONIBILIDAD, CONTINUIDAD Y RESILIENCIA (CAP. 10)

### 7.1 Disponibilidad de extremo a extremo (RT-10.01)

Se declara **disponibilidad mensual ≥ 99,9 % de extremo a extremo** sobre la **transacción crítica de negocio** (toma de pedido → preparación → despacho → POD → conciliación), medida sobre la experiencia real del usuario en el percentil 95 (RT-09.01) y sobre las ventanas operacionales (turno nocturno y ventana de despacho 05:30–07:00). La **TIER II (99,741 %) es la clasificación de la infraestructura del recinto** (un medio), no el SLO contractual: el e2e ≥ 99,9 % se alcanza con clúster de 3 nodos HA, **enlaces WAN redundantes de 3 tecnologías (fibra D-03 + satelital Starlink D-06 + LTE D-04) con conmutación < 30 s (SD-WAN)**, UPS ≥ 30 min / generador 24 h (Sala v02) y DRP con RTO ≤ 4 h / RPO ≤ 15 min. Se resuelve así la aparente contradicción declarada en la Matriz de Cumplimiento (la Sala v02 §7 declara ambas capas explícitamente).

### 7.2 Plan de continuidad del negocio — BCP (RT-10.03)

El **plan de continuidad (BCP)** del consolidado híbrido se declara conforme a **ISO 22301**, con ALC (aceptable level of continuity) por servicio crítico (WMS, BD, broker, cadena de frío), estrategias de continuidad por escenario (corte de energía, corte de enlace, pérdida de nodo, incendio, cyber-incidente) y criterios de invocación del DR. El BCP reside en el consolidado de arquitectura; este documento declara su aplicabilidad on-premise y su trazabilidad a RT-07 (PARTE 5).

### 7.3 Continuidad TIC — ISO/IEC 27031 (RT-10.04)

La continuidad TIC se declara conforme a **ISO/IEC 27031** (trazabilidad readines for business continuity), articulada con el BCP (7.2) y el Cap. 7: estructura de eventos (indisponibilidad, falla, desastre), prioridad de recuperación por componente on-premise, y la prueba semestral como ejercicio de validación (PARTE 5.6). Referencia al documento de seguridad/continuidad del consolidado.

### 7.4 Ventanas de mantenimiento y aviso (RT-10.05)

- **Ventana nominal de mantenimiento:** nocturna 00:00–04:00 (fuera de picking 22:00–06:00 y de la ventana crítica 05:30–07:00), con mantenimientos planificados usando N+1/live migration **sin interrupción** de la operación diurna.
- Para **cualquier actividad que implique riesgo de indisponibilidad** de un servicio crítico: **aviso al CLIENTE con ≥ 10 días hábiles de anticipación**, con detalle de alcance, ventana, duración, mitigación y plan de contingencia.

### 7.5 Despliegue de cambios sin interrupción (RT-10.06)

Estrategia de despliegue declarada: **rolling updates** sobre el clúster (live migration con HA 3 nodos), **blue-green/canary** para WMS y servicios de integración, cambios de firmware/parches en N+1 (un nodo a la vez), y topología del broker A-03 tolerante a reinicio de un miembro. No se planifica ni admite despliegue que requiera interrumpir la ventana operacional.

### 7.6 Pruebas de resiliencia por inyección de fallas (RT-10.07)

Programa de resiliencia declarado: **chaos/inyección de fallas semestral** (además de la prueba DR) y **antes de producción** (marcha blanca), con casos de uso del proceso real de bodega/despacho: caída de un nodo, pérdida del enlace WAN, falla de disco (reconstrucción), detención del broker, sobrecarga de I/O en peak. Resultados, tiempos y correcciones se documentan y se reportan al CLIENTE; las vulneraciones detectadas se incorporan al plan de corrección de la prueba siguiente.

### 7.7 Matriz de dependencias externas y comportamiento ante falla (RT-10.08)

| Dependencia externa | Fallo (caída) | Error/lentitud | Plan de respuesta |
|---|---|---|---|
| Enlace WAN fibra (D-03) | Conmutación automática a **Starlink (D-06)** (SD-WAN/BGP < 30 s); operación local 24 h | QoS prioriza broker/crítico; degradación de sincronización diferida | Protocolo en runbook 9.11; aviso al proveedor de fibra |
| Enlace WAN Starlink (D-06) — respaldo de CDs / principal de cross-docks | En CDs: operación por fibra (o LTE terciario); en cross-docks: conmutación a LTE dual | Rain fade/condiciones atmosféricas (banda Ka): degradación tasada del satelital; QoS prioriza broker/crítico | Monitoreo de pérdida de paquete/SNR del enlace satelital; aviso al proveedor Starlink; soporte LTE dual automático |
| Enlace WAN LTE (D-04) — terciario | Operación por fibra o Starlink; redundancia cubierta por D-03/D-06 | Sin conmutación (ultimo camino); se monitorea | Revisión de SIM/proveedor |
| ERP 2017 (A-04) | ACL encola mensajes (24 h) sin pérdida y los drena al recuperar | Encolado con reintentos y backoff | Runbook de integración |
| IdP Keycloak (nube) | Caché local A-05 (TTL 8 h) sostiene login; OTP offline | Login degradado sin sincronización | Re-sincronización automática al recuperar |
| AWS (réplica Aurora, S3) | Talca sigue operando local; DR se recupera cuando AWS disponibiliza | Lag de replicación alertado (5.3) | DR alternativo Concepción edge |
| SII/DTE (emisión) | Documentos quedan pendientes de timbraje y se emiten al recuperar | Reintentos y cola DTE | Procedimiento manual de respaldo (Sec. 1.1 Tabla v06) |
| Autoridad Sanitaria (notificaciones) | Alertas locales (B-02) sostienen el bloqueo de frío | — | Evidencia local NIST + informe |

### 7.8 Presupuesto de error por servicio crítico (RT-10.09 — Deseable)

Se propone presupuesto de error mensual para la transacción crítica: **≤ 0,1 % del tiempo (≈ 43 min/mes)** con desglose por componente (red 10 min, infraestructura 15 min, aplicación 10 min, dependencias externas 8 min), a revisar trimestralmente con el CLIENTE como insumo del SLO contractual (7.1).

---

## PARTE 8 — SEGURIDAD DE LA INFORMACIÓN ON-PREMISE (CAP. 11)

> Complementa F-01/F-02/F-03 (Tabla v06) y la arquitectura Zero Trust (PARTE 3). Los procesos de alcance corporativo en el consolidado se referencian; los compromisos operativos on-premise se declaran aquí.

### 8.1 Modelado de amenazas por componente (RT-11.02)

Se aplica **STRIDE** por componente y por integración crítica on-premise: WMS/BD (T · S), broker (R), ACL-ERP (T · D), caché Keycloak (T · D), IoT/Greengrass (R · T · D), VPN/firewall (E · D), NOC/DCIM (D). El modelado detallado vive en el **documento de seguridad del consolidado**; este documento declara la aplicación y su revisión **con cada cambio de arquitectura y al menos anualmente**, trazada a la matriz de controles (8.4).

### 8.2 Clasificación de la información (RT-11.03)

Niveles de clasificación aplicados on-premise: **Público, Interno, Confidencial, Restringido** (secretos/firma). Matriz de controles por nivel:

| Nivel | Ejemplos on-premise | Controles mínimos |
|---|---|---|
| Restringido | Claves KMS/HSM, credenciales de servicio, firmas privadas DTE, backup keys | Gestión privilegiada PAM (9.2), break-glass (9.7), HSM/KMS, cifrado campo (8.7) |
| Confidencial | BD WMS (inventario, clientes, trazabilidad), POD, tokens, auditoría | Cifrado en reposo (8.6), TLS 1.3 (8.5), RBAC (Tabla v06 A-05) |
| Interno | Logs de operación, métricas, configuraciones | Acceso por rol, retención (9.14) |
| Público | Material informativo interno no sensible | — |

La matriz de trazabilidad a ISO/IEC 27001 completa está en el documento de seguridad del consolidado; esta declaración fija los niveles on-premise y su referencia.

### 8.3 Gestión de vulnerabilidades y plazos (RT-11.04)

Programa on-premise declarado con plazos contractuales:

| Severidad | Definición | Plazo de corrección |
|---|---|---|
| **Crítica** | CVSS ≥ 9,0 o explotación activa | **7 días** |
| **Alta** | CVSS 7,0–8,9 | **15 días** |
| **Media** | CVSS 4,0–6,9 | **30 días** |

Escaneo de vulnerabilidades **automatizado semanal** (agente en servidores y estaciones — F-02/F-03), escaneo externo trimestral, y **validación de corrección** con re-escaneo. La trazabilidad (hallazgo → corrección → verificación) se reporta al CLIENTE trimestralmente.

### 8.4 Matriz de controles ISO/IEC 27001/27002 (RT-11.05)

La matriz de controles del consolidado (ISO/IEC 27001 A.5–A.18 e ISO/IEC 27002) se declara como **referencia única**; este documento declara que sus componentes on-premise (red, almacenamiento, endpoints, sala) quedan **cubiertos por los controles de dicha matriz**, con evidencia en la auditoría anual y en los simulacros (8.14/8.15). El control de gestión de incidentes está en 8.11/8.12.

### 8.5 TLS 1.3 en tránsito y gestión de certificados (RT-11.08)

- **TLS 1.3** obligatorio en todo tráfico con cifrado de capa de aplicación que toque nodos on-premise: portal WMS, API WMS terminales, sincronización broker → nube, telemetría OTel, acceso a tableros. Se declara **HSTS** en las interfaces web y **deshabilitado** TLS 1.0/1.1 y cifrados débiles (RC4, CBC sin AEAD).
- La **VPN IPsec** on-premise↔nube usa IKEv2/AES-256-GCM (PARTE 3.6).
- **Gestión de certificados:** inventario centralizado (Ansible — F-02) con **renovación automática y alerta a 30 días** del vencimiento; revisión del AC de confianza y de las cadenas en la prueba semestral.

### 8.6 Cifrado en reposo con gestión de claves (RT-11.09)

| Elemento | Cifrado en reposo | Gestión de claves |
|---|---|---|
| Almacenamiento clúster (OSD Ceph / RAID 10) | **LUKS/dm-crypt o NVMe SED** por OSD/disco | **KMS con CMK dedicada on-premise** (o HSM de borde); clave custodiada y respaldada |
| NAS D-05 | **LUKS/SED** (cilindro de respaldo cifrado) | CMK independiente de producción (RT-07.10) |
| BD PostgreSQL (datos en disco) | Cifrado del sistema de archivos subyacente (LUKS) | CMK dedicada |
| Estaciones de trabajo | **BitLocker/LUKS** gestionado (F-03) | Claves en AD/Intune/Key Server |
| Terminales de terreno | Cifrado de datos del dispositivo (Android full-disk/FBE) + app en sandbox | MDM (RT-03.18) |
| Nube (réplica Aurora, S3 inmutable) | **SSE-KMS** (AWS KMS/CMK) | CMK AWS, rotación anual |

**Rotación de claves** declarada: claves de cifrado de datos **anual** (o ante revocación/compromiso), claves maestras KMS conforme al calendario del proveedor, **sin degradación del servicio** (rotación online). Los respaldos cifrados conservan la versión de clave necesaria para su restauración auditable.

### 8.7 Cifrado a nivel de campo (RT-11.10 — Según caso)

Se declara **aplicable** a un subconjunto de datos sensibles según el caso: número de documento (RUT) de clientes en la BD WMS y en logs se pseudonimiza **cifrando a nivel de campo** (pgcrypto con clave en KMS) y los datos de tarjeta (PAN) del POS **no se almacenan on-premise** (tokenización en la pasarela — PCI PTS 7.x, PAX A920 Pro). El inventario de campos cifrados se incluye en la matriz de clasificación (8.2).

### 8.8 Superficie de exposición completa (RT-11.13)

Inventario consolidado de exposición on-premise (protocolos/puertos por sitio):

| Sitio | Servicios expuestos | Puertos/protocolos | ¿Accesible desde Internet? |
|---|---|---|---|
| Talca (red interna) | Portal WMS, API WMS, Postgres (interno), LDAPS caché, AMQP broker, SSH gestión | 443/TCP, 8080/TCP, 5432/TCP, 636/TCP, 5671–5672/TCP, 22/TCP (VLAN MGT, MFA) | **No** — solo vía VPN Zero Trust |
| Talca (borde) | Clúster HA firewall (Customer GW) | IPsec 500/4500/UDP | Sí — solo terminales IPsec, sin otros servicios |
| Talca (IoT) | Gateway Greengrass → IoT Core | MQTTS 8883 (saliente) | No — sin puertos entrantes (Zero Trust) |
| Concepción / Cross-docking | Gabinete de borde (mini-PC) | IPsec 500/4500/UDP; SSM 443 (saliente) | Únicamente 4G VPN IPsec / SSM |
| Estaciones/TI | — | 443 (proxy) | No |

Regla declarada: **ningún nodo on-premise abre puertos entrantes**; toda gestión entra por SSM Agent / VPN (Zero Trust — PARTE 3).  <a name="parte8"></a>

### 8.9 Eventos centralizados, inalterables y con retención (RT-11.14)

- Todos los eventos de seguridad on-premise (autenticación, cambios de configuración, accesos, EDR, firewall, DCIM/bélico) se centralizan en **una plataforma única (SIEM)** con **ingesta continua** (OTel/ADOT — F-01).
- **Inalterabilidad:** sellado/append-only (WORM local + bucket S3 con Object Lock en el SIEM o almacenamiento de logs); ni los administradores del sistema modifican eventos sellados.
- **Retención:** 12 meses en línea + 24 meses archivados (total 36 meses), superando el mínimo; la retención de evidencias sanitarias (cadena de frío) es de 2 años en línea (5.8).

### 8.10 SIEM y SOC 24×7 (RT-11.15 / RT-11.17)

- **SIEM del consolidado** con casos de uso del proceso logístico (excursión térmica junto a indicadores de red, fraude de reparto, anomalía de inventario) — referenciado como única plataforma nube+on-premise (F-01).
- **SOC 24×7** declarado (propio o subcontratado) con ubicación, dotación mínima (1 analista L1 por turno + L2 on-call), catálogo de procedimientos (monitoreo SIEM, EDR hunting, escalamiento) y cobertura contractual de ambos segmentos. La localización/capacidad se formaliza en el documento de seguridad del consolidado.

### 8.11 Plan de respuesta a incidentes (RT-11.18)

Plan de respuesta a incidentes declarado: fases (preparación, detección y análisis, contención, erradicación y recuperación, post-incidente), roles on-premise (Líder de Seguridad — Álvaro Catalán, Jefe de TI on-call, NOC, SOC), **comunicación del incidente al CLIENTE en ≤ 2 horas** desde la confirmación, y escalamiento definido por severidad. Referencia al plan del consolidado; los runbooks de respuesta específicos (ransomware, intrusión, indisponibilidad) se prueban en los simulacros (8.14/8.15).

### 8.12 Notificación de brechas (RT-11.19)

Protocolo declarado: **notificación de cualquier brecha de seguridad en ≤ 24 horas** desde su conocimiento (a la Autoridad y al CLIENTE según corresponda), e **informe de causa raíz en ≤ 5 días hábiles** con medidas correctivas y de prevención. Plantilla y canales definidos en el plan de incidentes (8.11).

### 8.13 Pentest por tercero independiente (RT-11.20)

- **Pentest anual** por tercero independiente (alcance on-premise + nube) y **pentest pre-producción** antes del go-live de la Etapa 1 (mes 16) y de la Etapa 2 (mes 21).
- Alcance declarado: WMS, ACL-ERP, caché IdP, VPN/router, IoT/Greengrass, red inalámbrica (RT-03.23) y superficie de exposición (8.8). Hallazgos se alimentan a la gestión de vulnerabilidades (8.3) y al plan de corrección.

### 8.14 Simulacros de incidente con el CLIENTE (RT-11.21 — Deseable)

Se proponen **simulacros de incidente anuales con participación del CLIENTE** (al menos un escenario anual: ransomware / indisponibilidad del WMS / excursión térmica), con informe y plan de mejora; se coordina con la prueba DR semestral (7.6) y con la reevaluación del BCP (7.2).

---

## PARTE 9 — IDENTIDAD, ACCESOS Y OBSERVABILIDAD (CAP. 12 Y 14)

### 9.1 Matriz de segregación de funciones — SoD (RT-12.05)

Matriz de separación de funciones acorde a RBAC+ABAC (Keycloak Modelo B — Tabla v06 A-05):

| Función | Crear usuario | Otorgar rol | Aprobar cambios | Operar NOC | Gestionar claves |
|---|---|---|---|---|---|
| Jefe de TI | ✔ | ✔ | ✔ (en su dominio) | ✔ | ✔ (custodia) |
| Administrador locales (adjudicatario) | ✔ | ✔ | — | ✔ | ✔ (uso) |
| Operador NOC | — | — | — | ✔ | — |
| Soporte/técnicos | — | — | — | — (reportados a NOC) | — |
| Auditor (CLIENTE) | — | — | — | (solo lectura) | — |

La misma persona **nunca** aprueba y ejecuta un cambio ni gestiona claves y audita su uso; combinaciones conflictivas se bloquean en Keycloak con política de consentimiento/dual. Matriz completa en el documento de identidad del consolidado.

### 9.2 Gestión de accesos privilegiados — PAM (RT-12.06)

- **Elevación temporal** de privilegios (break-glass controlado mediante solicitud con aprobación — flujo definido en 9.7), **con grabación de sesión** (registro de consola/terminal) en el NOC.
- Accesos administrativos (servidores, firewall, NAS, Keycloak, SIEM) pasan por la **bóveda PAM** con rotación automática de credenciales locales y **MFA obligatoria** (RT-12.03); sin contraseñas estáticas compartidas.
- Sesión privilegiada **auditada y en tiempo real** con alerta de actividad anómala (SIEM 8.10).

### 9.3 Política de sesión completa (RT-12.07)

| Parámetro | Valor declarado |
|---|---|
| Duración máxima de sesión interactiva | 8 h (turno) — refleja TTL 8 h del caché A-05 |
| Inactividad en terminales de terreno | Bloqueo a los 5 min con re-autenticación |
| Inactividad en estaciones/administración | Bloqueo a los 10 min |
| Revocación | Inmediata al cambiar rol/perfil (Keycloak propaga ≤ 15 min; baja ≤ 24 h, RT-12.10) |
| Concurrencia | Límite por usuario por rol; consola de sesiones activas |
| Cierre de sesión único (SSO) | Propagado (RT-12.02) en todos los clientes federados |

### 9.4 Credenciales de vida breve con refresco rotatorio (RT-12.08)

- Tokens **JWT de vida corta** (acceso ≤ 5 min y refresh ≤ 8 h con rotación y revocación por dispositivo) emitidos por Keycloak (nube) y **validados localmente** por el caché A-05 durante la desconexión.
- Sin identificadores de sesión en URLs; cookies `Secure` + `HttpOnly` + `SameSite`. Refresco rotatorio con detección de reuso (revocación de la sesión comprometida).

### 9.5 Auditoría del ciclo de vida de la identidad (RT-12.09)

Registro **no repudiable** de todo el ciclo de vida de la identidad on-premise: enrolamiento, autenticación, cambio de roles, elevación, revocación, cierre de sesión y cuentas de emergencia; sellado en el SIEM (8.9) y retención conforme 8.9/9.14. Informes de auditoría disponibles al CLIENTE.

### 9.6 Aprovisionamiento/desaprovisionamiento automatizado (RT-12.10)

- **Aprovisionamiento automatizado** desde RR. HH./gestión (SCIM vía Keycloak): el alta de identidad, roles y dispositivos (MDM) ocurre sin intervención manual; **baja de accesos en ≤ 24 horas** desde el evento de salida (y revocación inmediata de tarjetas/biometría local de la sala — S §4).
- Registro de cada aprovisionamiento/desaprovisionamiento en el SIEM (9.5).

### 9.7 Cuenta de emergencia — break-glass (RT-12.13)

| Ítem | Declaración |
|---|---|
| Cuenta(s) de emergencia | Mínimo local física en cada sitio (talonario sellado + llave/modalidad custodiada) y una cuenta break-glass cloud |
| Custodia | Sobre doble custodia: Líder de Seguridad (Álvaro Catalán) + Jefe de TI; apertura solo ante incidente declarado |
| Uso | Registro de la apertura (quién, cuándo, motivo), sesión grabada (PAM 9.2), revisión posterior obligatoria |
| Control | La cuenta se rota tras cada uso, se monitorea por SIEM con alerta inmediata de uso (9.2/8.10) |

### 9.8 Tableros operacionales y de negocio para el CLIENTE (RT-14.02)

- **Tableros operacionales** (DCIM/BMS de la sala — S §4, observabilidad OTel F-01) y **tableros de negocio** (OTIF, entregas, excursiones térmicas, stock) **accesibles al CLIENTE en tiempo real** vía portal seguro (TLS 1.3 — 8.5), con **exportación** (CSV/PDF/API) y trazabilidad de quien consulta (SIEM 8.9).
- Disponibilidad de tableros ≥ 99,9 % dentro del SLO (7.1); acceso por roles (9.1) y correlación por `transaction_id` (F-01).

### 9.9 SLI sobre experiencia real del usuario (RT-14.03)

SLIs **sobre experiencias reales** (percentil 95, RT-09.01) y no solo sintéticas: tiempo de respuesta e2e de la transacción crítica (registros de la app Reparto/Preventa y terminales RF), tasa de éxito de sincronización, latencia de serialización de picking, disponibilidad de la transacción crítica por ventana (05:30–07:00). Métricas RUM/CEM recopiladas en OTel (F-01) y reportadas al CLIENTE trimestralmente.

### 9.10 Alertamiento por síntomas de negocio (RT-14.04)

Además de alertas de infraestructura, se definen **alertas por síntomas de negocio**: OTIF por debajo de meta por turno, bloqueos de despacho por excursión térmica, colas broker acumuladas > umbral (indicia de pérdida de sincronización), devoluciones anómalas, conteo cíclico discrepante. Reglas en Prometheus/Alertmanager y alarmas a NOC + Jefe de TI on-call con prioridad según impacto (S §4.4).

### 9.11 Libro de operación y guías de resolución (RT-14.05)

**Runbook completo** por escenario on-premise (conmutación DR, retorno, caída de nodo, pérdida de enlace, falla de disco, reinicio del broker, excursión térmica, incidente de seguridad): pasos, responsables, tiempos, comandos, verificaciones y rollback. Versionado en el sistema de gestión (F-02), probado en ejercicios y disponible al NOC 24×7.

### 9.12 RCA en incidentes críticos (RT-14.06)

**Análisis de causa raíz obligatorio en incidentes críticos** (aquellos que afectan la ventana operacional o el SLO): entregado al CLIENTE en **≤ 5 días hábiles**, con 5 Why/gráfico de causa, evidencias (logs sellados 8.9), medidas correctivas con plazo y responsable, y seguimiento de su cierre en la siguiente prueba/auditoría.

### 9.13 Saneamiento de logs (RT-14.07)

- **Logs sin datos personales sensibles ni credenciales**: se aplica **seudonimización/masking automático** (RUT, correos, tokens, PAN) en la ingesta; se cifran a nivel de campo los campos que deban conservarse (8.7).
- El **acceso a logs** es por rol, autenticado y **auditado** (quién vio qué y cuándo — SIEM); los logs originales sellados solo los leen los roles de auditoría.

### 9.14 Retención de métricas, registros y trazas (RT-14.08)

| Tipo | En línea | Archivado | Costo declarado |
|---|---|---|---|
| Métricas (Prometheus/AMP) | 13 meses | — | OPEX de almacenamiento de métricas en el paquete de observabilidad |
| Logs (SIEM/bucket) | 12 meses | 24 meses (objeto) | OPEX S3 incluido en el costo de nube + NAS para archivo local |
| Trazas (OTel/X-Ray) | 90 días | 12 meses | Incluido en el paquete Sigv4/otlp |
| Evidencia sanitaria (frío) | 2 años | — | Cumplimiento sanitario (5.8) |

La política de retención se reporta al CLIENTE y su cumplimiento se audita en las pruebas DR/auditorías anuales.

### 9.15 Detección proactiva de anomalías (RT-14.09 — Deseable)

Se propone detección proactiva de anomalías con modelado estadístico/ML de series de tiempo (ingesta IoT, TPS, latencias, OTIF) sobre el stack de observabilidad, con alertas de desviación temprana — complementaria a los umbrales estáticos de 9.10.

---

## PARTE 10 — DESEMPEÑO, CAPACIDAD Y ESCALABILIDAD (CAP. 9)

> Esta parte cierra el capítulo 9 del transversal (RT-09.01 a RT-09.10) para el segmento on-premise, articulado con el cálculo de capacidad declarado en §1 y con el **Formulario T-13 (Plan de Pruebas y Validación)** donde se calendarizan las pruebas de carga/estrés (RT-09.06).

### 10.1 Umbrales de tiempo de respuesta aplicables (Cap. 9.1 + caso)

Se adoptan los umbrales del numeral 9.1 del transversal, interpretados con los valores por transacción del caso (Tabla 15 RT-09.01):

| Umbral | Valor |
|---|---|
| Confirmación de una línea de preparación de pedidos | **≤ 1 s** (referencia 9.1) |
| Registro de una entrega en el local del cliente | **≤ 2 s** |
| Registro de una línea en toma de pedido de preventa | **≤ 1,5 s** |
| Consulta de stock y crédito en preventa | **≤ 2 s** |
| Transacción operacional crítica de terreno, e2e | **≤ 3 s** (definido por el caso: registro entrega ≤ 2 s; en su defecto 3 s del 9.1) |
| Respuesta de una API de consulta simple | ≤ 500 ms |
| Respuesta de una API de escritura transaccional | ≤ 800 ms |
| Navegación entre vistas ya cargadas | ≤ 1 s |
| Búsqueda con criterios compuestos | ≤ 3 s |
| Informe estándar en línea / lote / archivo 100 MB / arranque frío | 30 s / 10.000 reg-min / 60 s / 60 s |

Percentil objetivo: **p95** en todos los casos (coherente con RT-09.01 del caso).

### 10.2 Cálculo de capacidad que sustenta el dimensionamiento (RT-09.01 — OBL)

El cálculo de capacidad está declarado en §1 de este documento: carga de diseño = **peak septiembre (2.600 entregas/día) × 1,5 = 3.900 entregas/día** (RNF-19.04), TPS de diseño **~105 TPS** (burst ×3), almacenamiento a 5 años con margen 68 % del pool Ceph, y enlaces WAN dimensionados por ventana (20→50 Mbps Talca, 10→20 Mbps Concepción, LTE dual en cross-docking). Supuestos de usuarios concurrentes: 62 preventistas + ~200 conductores + 310 personas del CD + terminales de bodega (144) y call center. Crecimiento anual declarado en 10.3.

### 10.3 Crecimiento sin rediseño — 3× en 3 años (RT-09.03 — OBL)

| Recurso | Diseño (3.900 entregas/día) | 3× volumetría (7.800 entregas/día) | Sustento |
|---|---|---|---|
| vCPU clúster Talca | 30 / 64 = **47 %** (N+1) | ~90 asignadas → ampliación según el procedimiento RT-08.05: adición de vCPU dentro del físico existente y, al acercarse al margen, **inserción del 4º servidor idéntico** (rack R04 de crecimiento, §1.5) elevando el pool a 96 threads + N+1 real; el 4º nodo mantiene la misma arquitectura (no es rediseño) | §1.2.3 / §5.6 |
| RAM | 68 / 256 = **27 %** | ~205 GB → dentro de los 384 GB físicos | §1.2.3 |
| Pool Ceph (réplica 2) | 32 % utilizado | ≤ 96 % de 5,76 TB → ampliación por adición de OSD/NVMe, sin rediseño | §1.2.3 |
| Enlace Talca | 20→50 Mbps | 50 / 100 Mbps (contrato escalonado del equipamiento §5.5) | §5.5 |
| TPS VM-02 | ~105 | ~315 (8 TPS/vCPU → 39 TPS/vCPU) | §1.2.4 |

La solución soporta 3× la volumetría inicial **sin rediseño de arquitectura** (misma topología de clúster, mismas VLAN, mismo esquema de réplica): el crecimiento se absorbe con ampliación dentro del margen físico y con el contrato escalonado de los enlaces (§5.5, RT-08.05).

### 10.4 Escalamiento horizontal y automático (RT-09.04 — OBL)

- **Capas de integración (broker A-03 / RabbitMQ)** y **agentes de ingestión (ADOT, workers de sincronización)**: escalamiento horizontal mediante publicación de réplicas en el clúster Proxmox y adición de CTs/VMs, **tiempo de reacción declarado ≤ 15 min** (playbook de auto-escalado).
- **Motor WMS (VM-01)** y **PostgreSQL (VM-02)**: escala vertical dentro del margen N+1 (8→12 vCPU VM-02) como primera acción; la capa de **lectura** escala horizontal con réplica de solo-lectura para pick duro (22:00–06:00).
- **Sin pérdida de transacciones en curso**: colas **persistentes** (durable) en A-03 y buffer de sincronización diferida en Concepción/cross-docking garantizan que una PCM de escalado no pierda mensajes (RT-03.11).

### 10.5 Primer cuello de botella al crecer la carga (RT-09.05 — OBL)

**Componente que primero se satura: la escritura transaccional de VM-02 (PostgreSQL, maestro de bodega), en la ventana de despacho 05:30–07:00 y el consiguiente drenaje del broker.**

| Componente | Por qué es el primero | Cómo se detecta | Cómo se resuelve |
|---|---|---|---|
| **VM-02 PostgreSQL (escritura/commit OLTP)** | Todo el picking (22:00–06:00) y el despacho massivo (05:30–07:00, 2.600/3.900 eventos) pasan por el maestro: es el único punto de escritura; a 3× carga, los commits (8 IOPS/tx ≈ 2.500 IOPS en peak 3×) degradan antes que CPU/disco (NVMe entrega > 100.000 IOPS, §1.2.4) | OTel/Prometheus: **p95 de escritura transaccional > 800 ms** (umbral 9.1) o commit ×3 sobre base; cola de espera de procesos Backend > 5–10; IO wait > 15 % sostenido; eventos alertados al NOC (parte 9) y al tablero del CLIENTE | 1) Escala vertical dentro del margen N+1 (8→12 vCPU, 32→64 GB); 2) **particionado mensual** de transacciones de bodega y **PgBouncer** (pool de conexiones, evita churn); 3) réplica de solo-lectura para consultas; 4) si el margen se agota: **4º nodo / sharding** y muerte del pico de despacho |
| **VM-01 WMS Core (CPU)** | Segundo en saturar: el motor WMS procesa las líneas de pick del CD | p95 tiempo de confirmación de línea > 1 s; CPU > 70 % sostenido 2 semanas | Escala vertical hasta el margen; reparto de olas de picking y arraigado de réplica de lectura |
| **Enlace WAN D-03/D-04 (Talca 20/50 Mbps)** | A 3× carga, la ventana de sincronización 17:00–20:00 (broker + IoT + WAL AMQP) puede acercar el enlace al 70–80 % | Utilización del enlace > 70 % sostenida en la ventana (SNMP/Telemetry del router, §5.5); backlog del broker creciendo hacia el 17:00 | QoS priorizando broker crítico y WAL; colas diferidas fuera de la ventana; escalado a **50/100 Mbps** (contrato escalonado §5.5) |
| **Wi-Fi 6E bodega (6 AP)** | A 3× con 405+ terminales simultáneos por turno, airtime > 50 % en los puntos de congestión | Análisis del airtime (controlador WLC), tasa de reintentos y latencia por AP | 7º AP en la zona de mayor densidad; banda de retorno cableada |

> **Prueba que lo verifica:** la curva de RT-09.07 debe mostrar el **punto de quiebre** del comienzo de saturación coincidente con la escritura transaccional de VM-02 (confirmación con la prueba de estrés de 10.6). Las pruebas de carga/estrés y el acta de resultados se integran al **Formulario T-13 (Plan de Pruebas y Validación)**.

### 10.6 Pruebas de carga y estrés (RT-09.06 / RT-09.07 — OBL)

- **Carga (RNF-19.04):** sobre **Preproducción**, **1,5 × peak = 5.850 entregas/día** equivalente (~160 TPS sostenidos), con los perfiles horarios reales (picking nocturno, despacho 05:30–07:00, preventa diurna).
- **Estrés:** incremento progresivo hasta identificar el **punto de quiebre** (objetivo: igual o superior a 3× la volumetría, 10.3).
- **Informe de carga (RT-09.07):** curva de tiempo de respuesta vs carga, punto de saturación, consumo de recursos (CPU/RAM/IOPS/enlace/colas) y comportamiento durante/después del peak — insumo para el hito de producción (mes 16) y para la actualización semestral de capacidad (RT-09.09).
- Programas de pruebas con **k6/Gatling + custom drivers** contra las APIs (svc-erp-integration, svc-broker), replicadas en Preproducción. Cortes de prueba: Etapa 1 (mes 13), Etapa 2 (mes 19) y re-ejecución trimestral (10.9). **Calendario e hitos formales en el Formulario T-13.**

### 10.7 Degradación controlada (RT-09.08 — OBL)

Al superarse la capacidad (más allá del punto de quiebre declarado en 10.6), la solución degrada de forma controlada:

1. **Encolamiento** en A-03 (colas persistentes, ventaja de atención priorizada para el broker crítico WMS);
2. **Limitación de tasa** (rate limiting del API gateway por cliente/concurrente) manteniendo procesamiento de fondo;
3. **Mensaje explícito a la persona usuaria** ("operación en cola, se procesará en X segundos") en terminales de preventa/reparto y en el WMS — **nunca error genérico ni pérdida silenciosa de transacciones**;
4. En el caso extremo (modo degradado ante falla de 2 nodos de 3), se declara operación de contingencia según parte 2, manteniendo la ventana de despacho 05:30–07:00 sin indisponibilidad (RT-03.10).

### 10.8 Gestión de capacidad en Operación (RT-09.09 — OBL)

- **Proyección trimestral** de crecimiento (volumetría, TPS, almacenamiento, enlaces) con el Líder de Datos y el SRE, consolidada en el tablero de capacidad del CLIENTE (parte 9.10).
- **Alertas anticipadas de agotamiento:** disparo automático al superar **70 % de utilización sostenida (2 semanas)** en vCPU, RAM, pool Ceph, IOPS, airtime Wi-Fi o enlace WAN (alineado con §6 / RT-08.05); reporte al CLIENTE con propuesta de ajuste de dimensionamiento y de costo en el mes siguiente.
- La re-ejecución trimestral de las pruebas de carga (10.6) alimenta la proyección y cierra el ciclo preventivo.

### 10.9 Pruebas de carga automatizadas en CI (RT-09.10 — Deseable)

Se propone como valor la automatización de pruebas de carga en el pipeline de integración continua (GitLab CI con k6), ejecutando un set canónico de escenarios (stocks/crédito, confirmación de línea, registro de entrega) en cada release candidato, con umbrales que bloquean el merge si superan los valores de 10.1 — detección temprana de regresiones de desempeño.

---

*Versión 04 — Cambios respecto de la v03: (1) clúster Talca ampliado a 3 nodos (exigencia del profesor, mínimo 3 nodos) con Ceph de 12 OSDs y quórum real de 3 MON (sin QDevice); (2) totales corregidos en §1.5 (60 vCPU asignados / 464 GB RAM físicos / ~9,2 TB útiles + 8 TB NAS); (3) prueba DR semestral declarada (RT-06.10 / Art. 20) sobre D-05 y Aurora; (4) cross-docking con LTE dual (2 proveedores, RT-03.17); (5) dispositivos definidos según Tabla v05 §4 (MC9400 Cold Storage, EC55, TC58e, ZQ620 Plus, PAX A920 Pro, ZT411, Dibal BEV, DS2208, Ebyte ME31, CX450); (6) VM-05/VM-C03 alineadas a Keycloak Local Auth Cache / Offline Proxy (D6, Modelo B). Se mantienen intactos los puntos fuertes de la v03: HA de red sin SPOF (RT-08.03), RAID 1/RAID 10 + Hot-Spare con réplica Ceph, dotación 144/30 terminales, matriz de VLANs y túneles IPsec IKEv2 con BGP AS 65001.*

*Versión 05 — Cierre de brechas de la Matriz de Cumplimiento BTT (on-premise): nuevas PARTES 5 a 9 que declaran los requisitos obligatorios de los capítulos 7 (modalidad, distancia, procedimientos de conmutación/retorno, cifrado de respaldos RT-07.10, tabla por dominio, restauración granular), 8 (S.M.A.R.T. RT-08.02, ampliación RT-08.05, equipamiento nuevo RT-08.06, eficiencia RT-08.08, control de extraíbles RT-08.09, § 8.4 garantías/repuestos, ciclo de vida RT-08.16, borrado seguro RT-08.17, disposición RT-08.18), 10 (SLO e2e ≥ 99,9 % RT-10.01, BCP, mantenimientos, despliegue sin interrupción, resiliencia, dependencias), 11 (TLS 1.3 RT-11.08, cifrado en reposo RT-11.09, superficie de exposición, SIEM/SOC, incidentes, pentest) y 12/14 (SoD, PAM, sesiones, break-glass, tableros al CLIENTE, SLI real, runbook, RCA, retención). Referencias cruzadas actualizadas a Tabla v06 y Sala v02.*

*Versión 06 — Cierre del capítulo 9 (Desempeño, capacidad y escalabilidad): nueva **PARTE 10** que declara RT-09.01 (cálculo de capacidad trazado a §1), RT-09.02 (concurrencia con umbrales p95), **RT-09.03 (crecimiento 3× sin rediseño en 3 años**, vCPU 47 %→ margen dentro del físico, enlace 50/100 Mbps escalonado), RT-09.04 (escalamiento horizontal ≤ 15 min de reacción, colas persistentes sin pérdida), **RT-09.05 (primer cuello de botella = escritura transaccional de VM-02 PostgreSQL en ventana 05:30–07:00 y drenaje del broker**, con detección OTel/Prometheus y resolución: PgBouncer + particionado + réplica de lectura + 4º nodo; luego VM-01 WMS, enlace D-03 y Wi-Fi), RT-09.06/09.07 (pruebas de carga 1,5× peak = 5.850 entregas/día y estrés hasta el punto de quiebre, informadas en el **Formulario T-13**), RT-09.08 (degradación controlada: encolamiento + rate limiting + mensaje explícito), RT-09.09 (gestión trimestral con alerta 70 %/2 semanas) y RT-09.10 (Deseable: carga automatizada en CI con k6). Referencias cruzadas a Tabla v06 y Sala v02.*

*Versión 07 — Ajuste de especificación del sensor IoT B-01 (alineado con Tabla v06 §2.8, nota 06d): módulo Ebyte **ME31-XDXX0400** (4 canales PT100 2/3 hilos por módulo, sonda 3 hilos con compensación de cable, exactitud ±0,5 % ± 1 °C ≈ ±1,1 °C a −22 °C) en lugar de ME31-XDXX0800-485 (8 canales); 28 puntos ≈ **7 módulos** (antes 4); protocolo **RS-485/Modbus RTU + Modbus TCP (Ethernet)**; VLAN 50 IOT-TALCA y fila de sensores en §1.5/tabla resumen actualizadas.*