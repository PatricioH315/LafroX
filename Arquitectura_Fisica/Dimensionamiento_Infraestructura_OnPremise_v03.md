# Dimensionamiento de Infraestructura On-Premise
## Distribuidora Puelche S.A. — Caso 02 Logística

> **Documento:** Componente de Arquitectura Física — Dimensionamiento de Servidores, Equipamiento y Red
> **Versión:** 03.2 (Alineada con decisiones: Keycloak IdP, Django monolito, réplica DMS CDC a Aurora; v03.2 alinea transporte broker→SQS FIFO vía shipper VM-03, HTTPS/443 PrivateLink, flujos de VLAN 20 y VPN — ver `Arquitectura_Fisica_Hibrida_Consolidada_Caso02_v01.md`)
> **Dependencia:** Tabla de Emplazamiento On-Premise v04 (aprobada)
> **Alcance:** CD Talca, CD Concepción y 3 Plataformas de Cross-Docking (Curicó, Chillán, Los Ángeles)

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
| Sensores de temperatura estimados (Talca + Concepción) | 28 |
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

### 1.2 CD Talca — Clúster de Virtualización en Alta Disponibilidad (N+1)

#### 1.2.1 Servidores Físicos

Se despliegan **2 servidores físicos idénticos** en configuración clúster N+1 sobre **Proxmox VE / KVM**. Ante la caída de un nodo, el hipervisor superviviente asume todas las VMs en ≤ 30 s (HA de Proxmox con quórum externo QDevice; live migration para mantenimientos planificados). La movilidad de VMs entre nodos se sustenta en **almacenamiento replicado de forma síncrona (Ceph)** a través de las interfaces dedicadas de 10GbE (ver 1.2.5).

| Atributo | Nodo-1 (Primario) | Nodo-2 (Secundario / HA) |
|---|---|---|
| **Modelo de referencia** | Servidor rack 1U — Dell PowerEdge R6615 / HPE ProLiant DL325 Gen11 o equiv. | Idéntico al Nodo-1 |
| **CPU** | 1 socket × 16 cores / 32 threads — AMD EPYC 9124 (3,0 GHz base, 3,7 GHz boost) o Xeon equivalente | Ídem |
| **RAM** | **128 GB DDR5 ECC** (8 × 16 GB) — configuración recomendada para N+1 con margen 25 % | Ídem |
| **Almacenamiento SO / Hipervisor** | RAID 1: 2 × SSD SATA 480 GB (espejo) | Ídem |
| **Almacenamiento de Datos** | RAID 10: 4 × NVMe SSD 1,92 TB U.2 + 1 Hot-Spare NVMe 1,92 TB | Ídem |
| **Interfaces de red** | 2 × 10GbE SFP+ (red dedicada de almacenamiento Ceph + tráfico de VM) + 2 × 1GbE RJ-45 (gestión / IPMI) | Ídem |
| **IPMI / iDRAC / iLO** | Sí — gestión fuera de banda | Ídem |
| **Fuente de alimentación** | Dual PSU hot-swap 1+1 | Ídem |
| **Factor de forma** | 1U rack | Ídem |

#### 1.2.2 Esquema RAID aprobado — CD Talca (por nodo)

| Capa | Tipo RAID | Discos | Capacidad bruta | Capacidad útil | Hot-Spare |
|---|---|---|---|---|---|
| SO + Hipervisor | RAID 1 (espejo) | 2 × SSD SATA 480 GB | 960 GB | **480 GB** | No (espejo es tolerante por diseño) |
| Storage de Datos (VMs, BD, broker) | RAID 10 (espejo + franjas) | 4 × NVMe 1,92 TB | 7,68 TB | **3,84 TB** | 1 × NVMe 1,92 TB (reconstrucción automática) |

**Memoria de cálculo del factor de compra:**

| Concepto | Valor |
|---|---|
| Capacidad útil objetivo (BD + WAL + índices + logs 5 años) | ~2 TB |
| Capacidad útil de la combinación 4 × 1,92 TB en RAID 10 | 3,84 TB |
| Factor de compra efectivo (bruto / útil objetivo): 9,6 TB / 2 TB | **×4,8** (supera el mínimo ×2,5 exigido) |
| Costo del Hot-Spare incluido en el factor | 1 × 1,92 TB adicional por servidor |
| Total discos NVMe por servidor | **5 × 1,92 TB = 9,6 TB brutos** |

#### 1.2.3 Máquinas Virtuales — Clúster Talca

| ID | Nombre / Rol | vCPU | RAM | Disco raíz | Disco datos | Criterio de tamaño |
|---|---|---|---|---|---|---|
| VM-01 | **WMS Core** (motor WMS: recepción, picking FEFO, misiones RF, despacho, SSCC GS1) | 8 | 16 GB | 40 GB | 100 GB | 120 terminales concurrentes; ~20 TPS en picking; sin estado persistente propio |
| VM-02 | **PostgreSQL — BD Transaccional (maestro de bodega)** (inventario, lotes, posiciones, SSCC, trazabilidad 5 años; réplica de continuidad/DRP hacia Amazon Aurora en AWS vía WAL streaming, RPO ≤ 15 min) | 8 | 32 GB | 40 GB | 1.500 GB | shared_buffers = 8 GB; effective_cache_size = 24 GB; IOPS pico: 105 TPS × 8 E/S = 840 IOPS → NVMe RAID 10 entrega > 100.000 IOPS |
| VM-03 | **RabbitMQ — Broker de colas offline** (encolado de transacciones durante 24 h sin enlace WAN) | 4 | 8 GB | 30 GB | 200 GB | 24 h × 35 TPS × 3.600 s = ~3 M mensajes; 200 GB >> volumen de mensajes (< 1 KB/mensaje) |
| VM-04 | **ACL ERP — Frontera única de integración** (adaptador WMS/cloud–ERP 2017; encolado offline hacia ERP local) | 4 | 4 GB | 30 GB | 20 GB | Única vía hacia el ERP 2017: el worker Celery `celery-erp-sync` del módulo `integraciones` (Django cloud) lo consume a través de esta ACL vía VPN, nunca directo al ERP; proceso liviano de transformación de mensajes |
| VM-05 | **Keycloak Master (A-05)** (IdP maestro on-premise: autenticación offline 24 h para 120 operarios; sincroniza usuarios/roles con Keycloak Replica cloud) | 4 | 4 GB | 30 GB | 20 GB | Autenticación local sin internet; 120 operarios concurrentes en turno nocturno; emite tokens JWT firmados con la misma clave que la réplica cloud; sincronización vía export/import de Realm al reconectar |
| VM-06 | **ADOT Collector + SSM Agent (F-01)** (telemetría OTEL; buffer offline 24 h; gestión remota Zero Trust sin puertos entrantes) | 2 | 4 GB | 30 GB | 50 GB | Buffer para 24 h de métricas, logs y trazas de todos los nodos on-premise |

**Totales de recursos del clúster Talca:**

| Recurso | Total asignado a VMs | Capacidad física (1 nodo) | Capacidad clúster (2 nodos) | Índice de utilización (N+1) |
|---|---|---|---|---|
| vCPU | 30 vCPU | 32 threads | 64 threads (32 por nodo) | 94 % del nodo superviviente en N+1 — sin overcommit |
| RAM | 68 GB | 128 GB | 128 GB en nodo superviviente | 53 % — margen 47 % para burst y SO |
| Almacenamiento datos | 1.890 GB | 3.840 GB útiles | — | 49 % (margen para crecimiento a 5 años) |

> **Nota de overcommit:** con 16 cores / 32 threads por nodo, el nodo superviviente en N+1 cubre las 30 vCPU asignadas sin sobreasignación (30/32 = 94 %). El esquema anterior (8 cores / 16 threads) implicaba un 188 % de overcommit cuando un nodo debía asumir la carga completa.

#### 1.2.4 NAS / Appliance de Respaldo Local — Recuperación Rápida (D-05)

Dispositivo dedicado, físicamente independiente del clúster de producción. Es la **copia local de recuperación rápida** dentro del esquema único 3-2-1-1-0 (RNF-20.07). **No constituye la pierna "1 inmutable"** del esquema: esa responsabilidad recae exclusivamente en la nube (S3 Object Lock / Backup Vault Lock).

| Atributo | Especificación |
|---|---|
| **Tipo** | NAS rack 1U (ej. Synology RS1221RP+, QNAP TS-873AeU-RP) |
| **Capacidad bruta** | 4 × HDD SATA 4 TB en RAID 6 → 8 TB útiles (tolera 2 discos caídos) |
| **Refuerzo de integridad** | WORM local como refuerzo adicional (retención 30 días); no sustituye la pierna inmutable de nube |
| **Protocolo de respaldo** | WAL streaming de PostgreSQL (RPO ≤ 15 min) + respaldo completo diario en ventana 02:00–04:00 |
| **Conectividad** | 2 × 1GbE en VLAN-Servidores; acceso restringido a VM-02 y sistema de backup |
| **Verificación de restauración** | Prueba mensual automatizada en entorno pre-producción — "0 errores" (RNF-20.07) |
| **RTO objetivo** | ≤ 4 h restauración completa desde NAS local, independiente de WAN (RNF-20.06) |

**Esquema 3-2-1-1-0 unificado (declaración única del consolidado híbrido):**

| Pierna | Detalle |
|---|---|
| **3 copias** | (1) Datos activos locales en NVMe RAID 10 · (2) Copia en NAS local D-05 · (3) Backup en nube |
| **2 medios** | (1) Discos NVMe/HDD locales · (2) Almacenamiento de objetos S3 |
| **1 fuera de sitio** | Backup en AWS — región primaria sa-east-1, réplica cross-region us-east-1 |
| **1 inmutable** | S3 Object Lock + Backup Vault Lock en AWS (ni el root elimina) |
| **0 errores** | Verificación mensual automatizada de restauración |

---

#### 1.2.5 Replicación de almacenamiento para HA (Ceph)

La alta disponibilidad del clúster y la movilidad de VMs entre los dos nodos Proxmox se sustentan en almacenamiento compartido replicado de forma síncrona, sin depender de una cabina externa:

| Atributo | Especificación |
|---|---|
| **Mecanismo** | Ceph sobre Proxmox VE: pool RBD con **réplica síncrona factor 2** (size=2, min_size=1). Cada escritura se confirma sólo después de quedar registrada en los NVMe de ambos nodos |
| **OSDs** | Los volúmenes RAID 10 de cada nodo (1.2.2) se exponen como OSDs del pool Ceph |
| **Monitores y quórum** | 3 MON (uno en cada nodo + monitor testigo externo); corosync con QDevice para evitar split-brain en el HA de VMs |
| **Red dedicada** | Enlace dedicado de almacenamiento entre nodos por las interfaces 10GbE SFP+, con MTU 9000 (jumbo frames) |
| **Failover ante caída de chasis** | El nodo superviviente conserva la copia síncrona íntegra del pool; el HA de Proxmox rearranca las VMs en ≤ 30 s sin pérdida de datos ya confirmados |
| **Migración** | Live migration sin corte de servicio por la red 10GbE dedicada (mantenimientos planificados) |

**Capacidad útil efectiva del pool replicado:** con factor de réplica 2, la capacidad útil total del clúster es 3,84 TB (una copia completa en cada nodo), consistente con el margen de crecimiento declarado en 1.2.3.

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
| VM-C03 | Keycloak Master (réplica) (IdP maestro on-premise Concepción; autenticación offline 24 h; RF-15.01, RNF-13.01) | 2 | 4 GB | 20 GB |
| VM-C04 | ADOT Collector + RabbitMQ (telemetría local + broker de colas de Concepción) | 2 | 4 GB | 50 GB |
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
| **Red** | 2 × 1GbE RJ-45 + módulo 4G Cat-12 (SIM dedicada, proveedor distinto al de los CD) |
| **Temperatura de operación** | -20 °C a +60 °C (certificación industrial) |
| **Protección física** | IP40 mínimo en gabinete cerrado |
| **UPS** | Mini-UPS interna o UPS de riel DIN ≥ 30 min |
| **Gestión remota** | SSM Agent vía VPN 4G (Zero Trust — sin puertos entrantes) |

**Software en nodo edge (contenedores):**

| Componente | Runtime | Descripción |
|---|---|---|
| Mini-WMS Edge | Docker | Recepción camión, desconsolidación, re-despacho, trazabilidad de lote |
| BD local | PostgreSQL 16 (single-node) | Transacciones del turno + buffer de sincronización diferida |
| Broker local | RabbitMQ | Cola de transacciones pendientes hacia WMS Talca |
| ADOT Collector | AWS Distro OT | Buffer de telemetría del nodo |
| Agente EDR | Agente liviano (F-03) | Monitoreo de comportamiento de procesos |

---

### 1.5 Resumen de Hardware — Totales On-Premise

| Sitio | Servidores / Dispositivos | vCPU | RAM | Almacenamiento útil (datos) | IOPS de diseño |
|---|---|---|---|---|---|
| CD Talca (clúster N+1) | 2 × servidor 1U + 1 × NAS | 30 vCPU activos | 128 GB / nodo | 3,84 TB útiles (pool Ceph réplica ×2) + 8 TB NAS | > 100.000 IOPS (NVMe RAID 10) |
| CD Concepción | 1 × servidor compacto 1U | 12 vCPU | 32 GB | 1,92 TB RAID 10 | > 50.000 IOPS |
| Cross-Docking Curicó | 1 × Mini-PC industrial | 6–8 cores | 16 GB | 512 GB NVMe | > 10.000 IOPS |
| Cross-Docking Chillán | 1 × Mini-PC industrial | 6–8 cores | 16 GB | 512 GB NVMe | > 10.000 IOPS |
| Cross-Docking Los Ángeles | 1 × Mini-PC industrial | 6–8 cores | 16 GB | 512 GB NVMe | > 10.000 IOPS |
| **TOTAL** | **7 servidores/dispositivos** | **~68 vCPU** | **~240 GB RAM** | **~8,3 TB datos útiles** | — |

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

### 2.2 Terminales Rugosos de Bodega — Picking en Cámara de Congelado (RNF-05.02)

| Atributo | Especificación mínima | Justificación |
|---|---|---|
| **Cantidad** | 144 en Talca (120 operarios simultáneos + 20 % de reserva) + 30 en Concepción (25 operarios + 20 % de reserva) | 38 % rotación anual de personal; stock de repuesto necesario (Cap. 4, 8) |
| **Modelo de referencia** | Zebra MC9300 Freezer, Honeywell CK65 o equivalente certificado cámara frigorífica | |
| **Temperatura de operación** | -30 °C a +50 °C (certificado) | Cámara congelado -22 °C; margen de 8 °C |
| **Protección** | IP65 (polvo + chorro de agua a presión) | Limpieza diaria con manguera en cámaras |
| **Resistencia a caídas** | 1,8 m sobre concreto (MIL-STD-810H) | Operación con guantes térmicos gruesos |
| **Pantalla** | ≥ 4" — táctil operable con guantes térmicos (gloves mode) o stylus; elementos UI ≥ 15 × 15 mm (RNF-05.02) | |
| **Escáner** | 1D / 2D GS1 integrado (SSCC GS1-128, DataMatrix, QR) | RF-01.07: AI 01, 10, 17 |
| **Batería** | ≥ 10 h de turno continuo, intercambiable en caliente | Turno nocturno 22:00–06:00 + margen |
| **Conectividad** | Wi-Fi 6 (802.11ax) 2,4 / 5 GHz; BLE 5.0 | VLAN-Operaciones; APs industriales en bodega |

---

### 2.3 Impresoras Térmicas de Andén — Etiquetas SSCC (RF-01.07)

| Atributo | Especificación mínima |
|---|---|
| **Cantidad** | 4 en Talca (2 andenes recepción + 2 despacho) + 2 en Concepción |
| **Modelo de referencia** | Zebra ZT411 (4" industrial) / Honeywell PM45 o equiv. |
| **Tipo de impresión** | Transferencia térmica (TTR) — durable en frío y humedad |
| **Resolución** | 203 dpi mínimo (legibilidad GS1-128 garantizada) |
| **Velocidad** | ≥ 8 pulgadas/segundo |
| **Conectividad** | Ethernet 1GbE RJ-45 (VLAN-Operaciones) + USB local |
| **Protocolo** | ZPL II |
| **Contenido de etiqueta** | GTIN (AI 01), N° de lote (AI 10), Vencimiento (AI 17), Recepción (AI 11) — RF-01.07 |
| **Ancho de etiqueta** | 4" (102 mm) — etiqueta estándar de pallet GS1 |

---

### 2.4 Gateway IoT / Concentrador de Sensores de Temperatura (B-02)

| Atributo | Especificación mínima |
|---|---|
| **Cantidad** | 1 en Talca + 1 en Concepción |
| **Modelo de referencia** | Advantech ADAM-6000 series, Moxa MGate o equiv. compatible con AWS IoT Greengrass Core |
| **Puertos RS-485** | ≥ 4 puertos RS-485 (Modbus RTU) para sensores cableados de cámara frigorífica |
| **CPU / RAM** | ARM Cortex-A53 / A72 o equiv.; ≥ 2 GB RAM; ≥ 32 GB eMMC |
| **Temperatura de operación** | -20 °C a +70 °C (montado en pared exterior de la cámara) |
| **Software** | AWS IoT Greengrass Core (runtime local para procesamiento de telemetría offline) |

---

## PARTE 3 — SEGMENTACIÓN DE RED Y DIRECCIONAMIENTO IP

---

### 3.1 Principios de Diseño (Zero Trust)

1. **Segmentación por función:** Ningún dispositivo de una VLAN puede alcanzar directamente a otro de una VLAN distinta sin pasar por el clúster de firewalls (D-01a/D-01b). No se permite enrutamiento directo inter-VLAN en el stack de switches core (D-02a/D-02b).
2. **Mínimo privilegio de red:** Cada VLAN tiene una ACL que permite únicamente los flujos estrictamente necesarios.
3. **IoT completamente aislado:** Los sensores RS-485 y el Gateway (B-01, B-02) no tienen acceso directo a Internet ni a la VLAN de Servidores. Solo el Gateway puede publicar hacia la nube a través de un proxy en el firewall.
4. **Gestión fuera de banda:** Los puertos IPMI/iDRAC/iLO de todos los servidores se conectan exclusivamente a la VLAN de Gestión.
5. **Sin puertos entrantes desde Internet:** Todo el tráfico hacia los nodos on-premise se inicia desde adentro (SSM Agent, VPN IPsec con BGP, ADOT).

---

### 3.2 Matriz de VLANs — CD Talca

| VLAN ID | Nombre | Función | Dispositivos miembros |
|---|---|---|---|
| **VLAN 10** | `MGT-TALCA` | Gestión fuera de banda | iDRAC/iLO servidores, puertos de gestión del stack de switches core (D-02a/D-02b), clúster de firewalls UTM (D-01a/D-01b), NAS (D-05) |
| **VLAN 20** | `SRV-TALCA` | Servidores y BD | VM-01 WMS, VM-02 PostgreSQL, VM-03 RabbitMQ, VM-04 ACL ERP, VM-05 Keycloak Master, VM-06 ADOT |
| **VLAN 30** | `OPS-TALCA` | Operaciones de bodega | Terminales rugosos RF (C-03), impresoras térmicas andén (C-04), APs industriales bodega |
| **VLAN 40** | `WKS-TALCA` | Estaciones de trabajo | PCs de despacho, administración, planificación (RNF-23.04) |
| **VLAN 50** | `IOT-TALCA` | Industrial IoT | Gateway Greengrass (B-02), sensores temperatura (B-01); **sin ruta a Internet directa** |

**Flujos permitidos entre VLANs (política firewall D-01):**

| Origen | Destino | Puerto / Protocolo | Propósito |
|---|---|---|---|
| VLAN 30 (OPS) → VLAN 20 (SRV) | TCP 8080 | API WMS — confirmación de misiones de picking |
| VLAN 40 (WKS) → VLAN 20 (SRV) | TCP 443 (HTTPS) | Portal WMS desde estaciones de trabajo |
| VLAN 50 (IOT) → VLAN 20 (SRV) | TCP 5672 (AMQP) | Gateway IoT publica eventos de temperatura al broker |
| VLAN 20 (SRV) → WAN (AWS VPN) | TCP 443 (HTTPS) | Sync broker→SQS FIFO (shipper VM-03, PrivateLink); telemetría ADOT; SSM |
| VLAN 10 (MGT) → Todos | TCP 22 (SSH) / HTTPS 443 | Gestión administrativa; MFA obligatoria (RF-15.03) |
| Todos → VLAN 20 (SRV): TCP 636 | LDAPS (Keycloak Master local) | Autenticación SSO usuarios offline (RF-15.02) |

---

### 3.3 Matriz de VLANs — CD Concepción

| VLAN ID | Nombre | Función |
|---|---|---|
| **VLAN 11** | `MGT-CONCEP` | Gestión fuera de banda (IPMI, switch, firewall de borde) |
| **VLAN 21** | `SRV-CONCEP` | VMs WMS Edge, PostgreSQL local, Keycloak Master (réplica), ADOT |
| **VLAN 31** | `OPS-CONCEP` | Terminales RF y andén |
| **VLAN 41** | `WKS-CONCEP` | Estaciones de trabajo |
| **VLAN 51** | `IOT-CONCEP` | Gateway IoT local (sensores cámara frigorífica) |

---

### 3.4 Matriz de VLANs — Plataformas Cross-Docking (Curicó, Chillán, Los Ángeles)

Red plana simplificada (gabinete de borde operacional, volumen reducido):

| VLAN ID | Nombre | Función |
|---|---|---|
| **VLAN 60** | `MGT-CDK` | Gestión del mini-PC (acceso SSM Agent via 4G) |
| **VLAN 70** | `OPS-CDK` | Mini-WMS edge + scanners de mano GS1 |

---

### 3.5 Asignación de Rangos IP Privados (RFC 1918)

| Sitio | VLAN | Nombre | Red | Máscara | Gateway | Hosts disponibles |
|---|---|---|---|---|---|---|
| **CD Talca** | 10 | MGT-TALCA | 10.1.10.0 | /24 | 10.1.10.1 | 253 |
| | 20 | SRV-TALCA | 10.1.20.0 | /24 | 10.1.20.1 | 253 |
| | 30 | OPS-TALCA | 10.1.30.0 | /24 | 10.1.30.1 | 253 (144 terminales + impresoras + APs) |
| | 40 | WKS-TALCA | 10.1.40.0 | /24 | 10.1.40.1 | 253 |
| | 50 | IOT-TALCA | 10.1.50.0 | /24 | 10.1.50.1 | 253 (28 sensores + 1 gateway) |
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

Cada CD (Talca y Concepción) establece una **AWS Site-to-Site VPN** con **2 túneles IPsec activos** hacia el Virtual Private Gateway (VGW) de AWS, conforme a RNF-13.07.

```
CD Talca                                     AWS Region
──────────────────────────                   ──────────────────────
Clúster HA Firewalls UTM (D-01a/D-01b)       Virtual Private Gateway
(Activo/Pasivo — Customer Gateway) ──Túnel 1 / IKEv2──▶  Endpoint AZ-a (fibra)
IP pública fibra D-03  AES-256-GCM / SHA-256
                      ──Túnel 2 / IKEv2──▶  Endpoint AZ-b (LTE)
IP pública LTE D-04    BGP failover < 30 s
```

| Parámetro | Túnel Primario | Túnel Secundario |
|---|---|---|
| **Interfaz física** | Fibra óptica (D-03) | LTE empresarial (D-04) |
| **IP Customer Gateway (VIP del clúster HA)** | IP pública fibra | IP pública SIM LTE |
| **IP AWS VGW** | Endpoint AZ-a (asignado por AWS) | Endpoint AZ-b (asignado por AWS) |
| **Protocolo** | IPsec IKEv2 | IPsec IKEv2 |
| **Cifrado** | AES-256-GCM | AES-256-GCM |
| **Autenticación** | SHA-256 | SHA-256 |
| **Grupo DH** | Group 14 (2048-bit) mínimo | Group 14 |
| **Enrutamiento** | BGP (AS on-premise: 65001) | BGP (AS on-premise: 65001) |
| **Conmutación** | — | < 30 s (BFD + reconvergencia BGP) |
| **Failover de la unidad de firewall** | Activo/Pasivo con sincronización de sesiones (túneles IPsec, BGP, NAT); la pasiva asume las VIPs en < 30 s | Ídem |
| **Tráfico en respaldo LTE** | — | Solo: VPN sync broker A-03 + SSM F-01 + ADOT telemetría |
| **MTU** | 1.436 bytes | 1.436 bytes |

**Flujos principales por la VPN:**

| Flujo | Origen | Destino | Protocolo |
|---|---|---|---|
| Sync broker → nube | VM-03 SRV-TALCA (shipper A-03) | SQS FIFO (AWS) | HTTPS 443 (VPC Endpoint SQS / PrivateLink) |
| Telemetría ADOT | VM-06 SRV-TALCA | CloudWatch / X-Ray | HTTPS 443 |
| Greengrass Core → IoT Core | IOT-TALCA Gateway | AWS IoT Core | MQTTS 8883 |
| SSM Agent (gestión remota) | Todos los nodos | SSM Endpoint (regional) | HTTPS 443 saliente |
| Sync WMS Concepción → Talca | SRV-CONCEP | SRV-TALCA | TCP 8080 / 5432 |
| Sync cross-docking → Talca | CDK-xx | SRV-TALCA | AMQPS 5671 |

---

### 3.7 Ancho de Banda Dimensionado por Sitio (RNF-13.08)

| Sitio | Régimen normal | Peak (septiembre) | Justificación |
|---|---|---|---|
| **CD Talca — fibra primaria** | 20 Mbps simétrico | 50 Mbps simétrico | 2.600 entregas × ~15 KB/tx = 312 MB/h peak; telemetría IoT 28 sensores × 1 msg/30 s × 500 B ≈ 1 Mbps; margen para actualizaciones y SSM |
| **CD Talca — LTE respaldo** | 5 Mbps (solo tráfico crítico) | 10 Mbps | Broker sync + SSM Agent únicamente en failover |
| **CD Concepción — fibra** | 10 Mbps simétrico | 20 Mbps simétrico | Volumen proporcional a Talca |
| **CD Concepción — LTE respaldo** | 3 Mbps | 5 Mbps | **Nuevo enlace requerido** (actualmente sin respaldo — viola RNF-13.07) |
| **Cross-Docking (c/u)** | 2 Mbps (LTE 4G) | 5 Mbps (LTE 4G) | Sync ventana 3 h + manifiesto pre-cargado; solo móvil disponible |

---

### 3.8 Alta disponibilidad de la red del sitio principal (RT-08.03)

El CD Talca no admite equipos únicos de perímetro ni de distribución (RT-08.03). La red del sitio principal se corrige de la siguiente forma:

| Equipo | Cantidad | Configuración HA |
|---|---|---|
| Firewall UTM / Customer Gateway (D-01) | 2 | Clúster **Activo/Pasivo** con sincronización de sesiones (NAT, VPN IPsec, BGP, UTM). La unidad pasiva asume las VIPs y los túneles en < 30 s. Cada unidad se conecta a circuitos eléctricos distintos (RT-08.04) |
| Switch core L3 (D-02) | 2 | **Stack / MLAG**: ambos switches operan como un único plano de distribución. Servidores, firewalls y APs se conectan con LACP/MLAG repartido entre ambos miembros; la caída de un miembro no interrumpe el tráfico |

Con esta configuración quedan eliminados los puntos únicos de falla en el perímetro y en la distribución del sitio principal (RT-08.03).

---

## PARTE 4 — INVENTARIO CONSOLIDADO DE HARDWARE

---

### 4.1 Servidores y Dispositivos

| Sitio | Elemento | Cant. | Modelo de referencia |
|---|---|---|---|
| CD Talca | Servidor HA Nodo-1 | 1 | Dell PowerEdge R6615 / HPE ProLiant DL325 Gen11 |
| CD Talca | Servidor HA Nodo-2 | 1 | Ídem |
| CD Talca | NAS Respaldo Local D-05 (recuperación rápida) | 1 | Synology RS1221RP+ (WORM local opcional como refuerzo; la pierna inmutable vive en AWS) |
| CD Talca | Switch Core L3 con VLANs — Stack/MLAG | 2 | Cisco Catalyst 9300-48P (StackWise) o equiv. |
| CD Talca | Firewall UTM / Customer GW — clúster HA Activo/Pasivo | 2 | FortiGate 60F HA A/P / Palo Alto PA-220 A/P o equiv. |
| CD Talca | AP Wi-Fi 6 industrial (bodega) | 6 | Cisco Catalyst 9115 / Aruba AP-515 |
| CD Talca | Gateway IoT + Greengrass | 1 | Advantech ADAM-6000 + Greengrass Core |
| CD Talca | Terminal rugoso picking | 144 | Zebra MC9300 Freezer |
| CD Talca | Impresora térmica andén | 4 | Zebra ZT411 |
| CD Talca | Estación de trabajo + 2 monitores | 5 | PC + 2 × 24" Full HD |
| CD Concepción | Servidor borde compacto | 1 | Dell R250 / HPE DL20 Gen11 |
| CD Concepción | Firewall de borde | 1 | FortiGate 40F o similar |
| CD Concepción | AP Wi-Fi 6 industrial | 3 | Cisco Catalyst 9115 |
| CD Concepción | Gateway IoT + Greengrass | 1 | Ídem Talca |
| CD Concepción | Terminal rugoso picking | 30 | Zebra MC9300 Freezer |
| CD Concepción | Impresora térmica andén | 2 | Zebra ZT411 |
| CD Concepción | Estación de trabajo + 2 monitores | 3 | PC + 2 × 24" Full HD |
| Cross-Docking (×3) | Mini-PC industrial rugoso | 3 | Advantech ARK-2250 / Intel NUC Pro 12 |
| Cross-Docking (×3) | Switch compacto | 3 | Netgear GS308E o similar |
| Cross-Docking (×3) | Scanner de mano GS1 | 6 (2/sitio) | Zebra DS2208 / Honeywell Voyager |

### 4.2 Máquinas Virtuales — Resumen

| VM | Sitio | Rol | vCPU | RAM | Datos |
|---|---|---|---|---|---|
| VM-01 | Talca | WMS Core | 8 | 16 GB | 100 GB |
| VM-02 | Talca | PostgreSQL BD (maestro → réplica Aurora) | 8 | 32 GB | 1.500 GB |
| VM-03 | Talca | RabbitMQ Broker | 4 | 8 GB | 200 GB |
| VM-04 | Talca | ACL ERP (frontera única) | 4 | 4 GB | 20 GB |
| VM-05 | Talca | Keycloak Master (IdP) | 4 | 4 GB | 20 GB |
| VM-06 | Talca | ADOT + SSM Agent | 2 | 4 GB | 50 GB |
| VM-C01 | Concepción | WMS Edge | 4 | 8 GB | 300 GB |
| VM-C02 | Concepción | PostgreSQL local | 4 | 8 GB | 500 GB |
| VM-C03 | Concepción | Keycloak Master (réplica) | 2 | 4 GB | 20 GB |
| VM-C04 | Concepción | ADOT + RabbitMQ | 2 | 4 GB | 50 GB |
| **TOTAL** | | | **42 vCPU** | **92 GB** | **2.760 GB** |

---

*Versión 03 — Alineación con la Tabla de Emplazamiento v04: (1) VM-05/VM-C03 redefinidas como **Keycloak Master** (IdP maestro on-premise, autenticación offline 24 h, sincronización con réplica cloud); (2) VM-04 reforzada como frontera única de integración hacia el ERP 2017 (el worker Celery `celery-erp-sync` cloud la consume vía VPN, nunca directo); (3) VM-02 explicitada como maestro transaccional de bodega con réplica de continuidad/DRP en Amazon Aurora vía WAL streaming (RPO ≤ 15 min); (4) D-05 redefinido como Appliance de Respaldo Local para RTO ≤ 4 h, con la pierna "1 inmutable" del esquema 3-2-1-1-0 única y exclusivamente en AWS (S3 Object Lock / Backup Vault Lock). Se mantienen intactos los puntos fuertes de la v02: HA de red sin SPOF (RT-08.03), CPU EPYC 16c/32t, RAID 1/RAID 10 + Hot-Spare con réplica Ceph, dotación 144/30 terminales y matriz de VLANs + túneles IPsec IKEv2 con BGP AS 65001.*

