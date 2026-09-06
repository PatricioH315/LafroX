# Dimensionamiento y Plan de Capacidad — Caso 02 Logística

## Distribuidora Puelche S.A. — Licitación TFEP-01/2026 (Caso 02 — Logística)

| Atributo | Valor |
|---|---|
| Documento | Dimensionamiento y plan de capacidad (Subdocumento 4, apartado 6) |
| Versión | v01 |
| Fecha | 2026-09-05 |
| Estado | En revisión interna |
| Autor | Arquitecto de Solución (LafroX) |
| Marco | BA Art. 16 (híbrido) · BTT RT-09.01…09.09 (capacidad y desempeño) · RT-03.20 (ancho de banda) · RNF-19.01–19.04 · T-13 |
| Fuentes | `Caso_02_Logistica.md` (Tabla 14.1, Cap. 15), `Bases_Tecnicas_Transversales.md` (RT-09.xx), `Dimensionamiento_Infraestructura_OnPremise_v05.md` (§1/§3.7/§10), `Propuesta_Arquitectura_Cloud_Caso02_CLAUDE_v2.md` v3.6 (§3.5), `Tabla_Emplazamiento_OnPremise_v06.md`, `Registro_Decisiones_Arquitectura_ADR_v01.md` (ADR-01/04/10/12) |

> **Finalidad.** Este documento responde el apartado 6 del Subdocumento 4 — **Dimensionamiento y plan de capacidad: volúmenes, concurrencia y crecimiento** — de la Oferta Técnica, conforme al numeral 14.2 del Caso (dimensionamiento explícito con método y supuestos, sin celdas vacías). Declara la carga de diseño, los supuestos de volumen y crecimiento, y sus criterios (RT-09.01…09.09, RNF-19.04), **sin introducir cifras nuevas** respecto de las fuentes señaladas, de las que es un consolidado coherente.

---

## 1. Criterios y método de dimensionamiento (RT-09.01, RT-09.02)

El dimensionamiento se deriva de la **volumetría real del Caso (Tabla 14.1 / Cap. 14 y 15)**, no de promedios genéricos, dado el **perfil de carga no plano** (RT-09.02):

| Ventana | Perfil |
|---|---|
| Preventa | 09:00–18:00 (62 preventistas con EC55) |
| Preparación (pick duro) | 22:00–06:00 (120 terminales RF, −22 °C) |
| Despacho | 05:30–07:00 (~96 camiones; 42 propios + 54 transportistas) |
| Sincronización de flota | 17:00–20:00 (~270 dispositivos remotos) |
| Peak de septiembre | ≈ 2× el volumen regular durante tres semanas |

**Reglas que gobiernan el dimensionamiento:**

- **Carga de diseño (RNF-19.04):** peak de septiembre (2.600 entregas/día) × **1,5 = 3.900 entregas/día** toleradas sin degradación.
- **TPS de diseño:** burst ×3 → **~105 TPS** (ver §3).
- **Crecimiento (RT-09.03):** la solución soporta **3× la volumetría inicial sin rediseño en 3 años** (misma topología, §6).
- **Umbrales (RT-09.01):** percentil **p95** en toda medición (Tabla 15), con umbrales por operación (§7).
- **Sin capacidad ociosa financiada (RT-15.01):** el cómputo elástico en nube escala automática (ADR-12); el on-premise se dimensiona al margen útil sin sobrecompra.
- **Coherencia interna:** los totales de este documento concuerdan con la Tabla 14.1 (volumetría), `Dimensionamiento v05` (on-premise), Cloud v3.6 §3.5 (nube) y el ADR (ADR-01, 04, 10, 12 y decisiones 16.1 N° 28 y N° 30).

---

## 2. Volumetría de referencia (Tabla 14.1 Caso 02)

### 2.1 Valores base de dimensionamiento

| Magnitud | Valor base |
|---|---|
| Clientes activos / puntos de entrega | 14.200 |
| Pedidos | 31.000 / mes |
| Líneas de pedido | 260.000 / mes |
| Unidades despachadas | 2.400.000 / mes |
| SKU activos | 8.400 |
| Posiciones de almacén (Talca) | 11.400 (87 % ocupación) |
| Entregas / día (régimen normal) | 1.400 |
| Entregas / día (peak septiembre) | 2.600 |
| Kilometraje | ≈ 420.000 km / mes |
| Documentos tributarios | ≈ 34.000 / mes |
| Camiones con cadena de frío | 18 |
| Puntos de medición de temperatura | 28 (≈ 7 módulos Ebyte de 4 canales) |
| Sitios on-premise | 5 (Talca, Concepción, Curicó, Chillán, Los Ángeles) |

> **Nota de coherencia (instalaciones):** la Tabla 14.1 y RT-21.16 reportan **6 instalaciones** (7 a tres años); el despliegue físico ubica cómputo en los **5 sitios on-premise** listados + borde en terreno (calle y 14.200 puntos). La divergencia 5/6 (Tabla 14.1 vs §8 del Caso) está declarada en las consultas al mandante (Art. 43.3) y no altera el dimensionamiento: el cómputo se emplaza en los 5 sitios, la 6.ª instalación es de red/almacenamiento sin nodo de cómputo propio.

### 2.2 Proyección a 3 años (Caso 02)

| Magnitud | Base (año 0) | Año 3 | Variación |
|---|---|---|---|
| Clientes | 14.200 | 15.500 | +9 % |
| Pedidos / mes | 31.000 | 36.000 | +16 % |
| Líneas / mes | 260.000 | 305.000 | +17 % |
| Entregas / día (normal) | 1.400 | 1.650 | +18 % |
| Entregas / día (peak) | 2.600 | 3.100 | +19 % |
| Kilometraje / mes | 420.000 km | 480.000 km | +14 % |
| DTE / mes | ≈ 34.000 | ≈ 40.000 | +18 % |
| Instalaciones | 6 (5 con cómputo) | 7 | — |

Los recursos se dimensionan, además, para **3× la volumetría inicial sin rediseño (RT-09.03)**: la proyección real del Caso a 3 años (+16–19 %) queda muy por debajo del límite de diseño, dejando margen ante crecimiento mayor al modelado (ADR-12).

---

## 3. Concurrencia y TPS de diseño

### 3.1 Usuarios y terminales concurrentes

| Rol | Concurrencia | Dispositivo |
|---|---|---|
| Preventistas | 62 simultáneos | Zebra EC55 (parque 62 + reserva 20 %) |
| Conductores (reparto) | ~200 simultáneos | Zebra TC58e (parque único 42 propios + ~160 externos + reserva) |
| Personal de centro de distribución | 310 (turno) | Estaciones y terminales fijas |
| Operarios de picking simultáneos (turno nocturno) | 120 | Zebra MC9400 Cold Storage (pool Talca 144 = 120 + 20 %; Concepción 30) |
| Terminales RF concurrentes | 120 (base de diseño) | Ídem |
| Call center / supervisión | ~20 | Estaciones |
| **Dispositivos móviles registrados (MQTT/IoT Core)** | **~270** (hasta ~300+ en peak) | EC55 + TC58e + terminales de cámara |

### 3.2 TPS estimados (peor ventana, fuente: Dimensionamiento v05 §1.1)

| Flujo | Cálculo | TPS |
|---|---|---|
| Confirmaciones de picking | 120 terminales × 1 confirmación / 6 s | ~20 TPS |
| Pedidos de preventa (09:00–13:00) | 62 preventistas × 1 línea / 8 s | ~8 TPS |
| Movimientos de inventario + sincronización | Suma de flujos (broker, WMS, IoT) | ~35 TPS |
| **TPS de diseño (burst ×3)** | 35 × 3 en peak de septiembre | **~105 TPS** |

> El burst ×3 absorbe el peak de septiembre y las ráfagas de la ventana de sincronización 17:00–20:00. El **~105 TPS** es el valor único de diseño citado por ADR-01, ADR-12 y Cloud v3.6 §3.5, y sustenta el dimensionamiento de IOPS de VM-02 (§4.3) y del escalado ECS (ADR-12).

---

## 4. Dimensionamiento on-premise (ADR-10)

### 4.1 Cómputo — CD Talca (clúster N+1, 3 nodos Proxmox/Ceph)

| Recurso | Asignado | Físico (clúster) | Utilización bajo N+1 |
|---|---|---|---|
| vCPU | 30 | 96 threads (3 nodos × 32) | 30 / 64 = **47 %** (2 supervivientes) |
| RAM | 68 GB | 384 GB (3 × 128) | 68 / 256 = **27 %** |
| Almacenamiento (pool Ceph, réplica 2) | 1.890 GB | **5,76 TB útiles** (12 OSDs, RAID 10 NVMe) | **32 %** |

**VMs del clúster Talca (familia C1…C6 de la Tabla v06 §1.0):**

| VM | Rol | vCPU | RAM | Disco datos |
|---|---|---|---|---|
| VM-01 | WMS Core (picking FEFO, misiones RF, despacho, SSCC GS1) | 8 | 16 GB | 100 GB |
| VM-02 | PostgreSQL — BD transaccional del maestro de bodega | 8 (→12) | 32 GB (→64) | 1.500 GB |
| VM-03 | RabbitMQ — broker de colas offline (buffer 24 h) | 4 | 8 GB | 200 GB |
| VM-04 | ACL ERP — frontera única de integración | 4 | 4 GB | 20 GB |
| VM-05 | Keycloak Local Auth Cache / Offline Proxy (A-05, Modelo B) | 4 | 4 GB | 20 GB |
| VM-06 | OpenTelemetry Collector + SSM Agent (buffer 24 h) | 2 | 4 GB | 50 GB |

### 4.2 Cómputo — Concepción (edge) y cross-docking

| Sitio | Capacidad | Rol |
|---|---|---|
| CD Concepción (C3) | 12 vCPU / 24 GB / RAID 10 (4×NVMe 960 GB + hot-spare) | WMS en modo reducido 24 h sin enlace (RNF-13.01) |
| Plataformas de cross-docking (E-01) | Mini-PC industrial (Advantech ARK-2250 / NUC Pro 12) | Mini-WMS E-01 + router Starlink (enlace principal) + LTE dual de respaldo |

### 4.3 Almacenamiento (ADR-10, RT-03.14)

| Capa | Esquema | Capacidad útil |
|---|---|---|
| BD transaccional + pool de datos | Ceph réplica 2 sobre RAID 10 NVMe (≈ 4× factor de compra) | 5,76 TB pool (margen 68 % a 5 años) |
| Crecimiento 5 años | 1.890 GB × 3 | ≈ 5,7 TB < 5,76 TB ✓ |
| Respaldo de recuperación rápida (D-05) | NAS 2U, RAID 6 (4 × 4 TB) + WORM local | 8 TB |
| IOPS VM-02 | 105 TPS × 8 E/S = 840 IOPS requeridas | NVMe RAID 10 > 100.000 IOPS ✓ |

### 4.4 Ancho de banda WAN por sitio (RT-03.20 / RNF-13.08, fuente: Dimensionamiento v05 §3.7)

| Sitio | Régimen normal | Peak septiembre | Respaldo (autoconmutación < 30 s) |
|---|---|---|---|
| CD Talca (D-03/D-06/D-04) | 20 Mbps fibra | 50 Mbps | Starlink 1 TB (50–100 Mbps) · LTE 5→10 Mbps |
| CD Concepción | 10 Mbps fibra | 20 Mbps | Starlink 1 TB · LTE 3→5 Mbps |
| Cross-docking (×3) | Starlink 500 GB principal | Ídem | LTE dual 2→5 Mbps (2 proveedores) |

> **Cohesión con el apartado 5 (despliegue):** estos valores son los declarados en `Arquitectura_de_Despliegue_v01.md` §2 y en Cloud v3.6 §2 (VPN IPsec dual por CD).

---

## 5. Dimensionamiento nube (ADR-12, Cloud v3.6 §3.5)

| Componente | Base (normal) | Peak septiembre | Criterio de escalado |
|---|---|---|---|
| ECS Fargate Django (tareas `2 vCPU / 4 GB`) | 2 | 6 (3×) | Target Tracking CPU > 70 % |
| ECS Fargate Celery workers (`2 vCPU / 4 GB`) | 2 | 4 (2×) | Cola (queue depth) / CPU |
| AWS Lambda (`fn-iot-validator`, `fn-document-signer`) | 100 concurrencias | 500 (reserva) | Eventos IoT Core / S3 |
| Aurora PostgreSQL (writer \| reader) | `db.r6g.large` × 2 AZ | `db.r6g.xlarge` + 2 readers | CPU > 60 % / Conexiones > 80 % |
| ElastiCache Redis | `cache.r6g.large` | `cache.r6g.xlarge` | Memoria > 75 % (stock/crédito < 2 s) |
| DynamoDB (telemetría IoT cruda) | On-demand | On-demand | Sin gestión de capacidad |
| Amazon EventBridge | Serverless | Serverless | Escala con el evento |
| AWS IoT Core (MQTT) | ~270 dispositivos | ~300+ | Concurrencia de terreno |
| Keycloak IdP maestro (Fargate) | 1 tarea `1 vCPU / 2 GB` | 2 tareas (Multi-AZ) | CPU > 60 % |

**Escalado automático (RT-09.04):**
- **Predictivo + reactivo (ADR-12):** pre-warm en agosto de las tareas ECS, concurrencia reservada Lambda y EventBridge; reactivo con Target Tracking en < 2 min · aprovisionamiento en < 3 min · cooldown 60 s.
- **Serverless-first:** DynamoDB On-Demand, Lambda y EventBridge escalan sin configuración adicional; la capacidad se paga por uso (sin capacidad ociosa, RT-15.01 — FinOps Cloud §4.5).

---

## 6. Plan de capacidad y crecimiento 3× sin rediseño (RT-09.03)

El crecimiento se absorbe **con el mismo diseño** (sin cambio de topología, VLAN, réplica ni nube):

| Recurso | Diseño (3.900 entregas/día) | 3× (7.800 entregas/día) | Acción declarada |
|---|---|---|---|
| vCPU clúster Talca | 30 / 64 = 47 % (N+1) | ~90 asignadas | Ampliación RT-08.05; al acercarse al margen, inserción del **4.º servidor idéntico** (rack R04 de crecimiento, Sala §6.2) → 96 threads + N+1 real |
| RAM | 68 / 256 = 27 % | ~205 GB | Dentro de los 384 GB físicos ✓ |
| Pool Ceph | 32 % de 5,76 TB | ≤ 96 % | Ampliación por adición de OSD/NVMe, sin rediseño |
| Enlace Talca / Concepción | 20→50 / 10→20 Mbps | 50 / 100 Mbps | Contrato escalonado de enlaces (§3.7) |
| TPS VM-02 | ~105 | ~315 | Escala vertical 8→12 vCPU (32→64 GB) + particionado mensual |

En nube, el 3× se absorbe por **auto-scaling** (Fargate 2→6, Celery 2→4, Lambda hasta 500, Aurora `xlarge` + readers), sin rediseño arquitectónico — misma decisión ADR-12 que fija el límite de elasticidad del peak.

---

## 7. Umbrales de desempeño (RT-09.01 — Tabla 15, percentil p95)

| Operación | Umbral (p95) |
|---|---|
| Confirmación de una línea de preparación de pedidos (picking) | ≤ 1 s |
| Registro de una entrega en el local del cliente | ≤ 2 s |
| Registro de una línea en toma de pedido de preventa | ≤ 1,5 s |
| Consulta de stock y crédito en preventa | ≤ 2 s |
| Transacción operacional crítica de terreno (e2e) | ≤ 3 s |
| Navegación entre vistas ya cargadas | ≤ 1 s |
| Búsqueda con criterios compuestos | ≤ 3 s |

Los umbrales se verifican con monitoreo OTel/Prometheus (CloudWatch) y se prueban en Pre-Producción (§10).

---

## 8. Primer cuello de botella (RT-09.05)

**VM-02 (PostgreSQL — escritura transaccional del maestro de bodega)** se satura primero a medida que crece la carga: todo el picking (22:00–06:00) y el despacho masivo (05:30–07:00) pasan por el único punto de escritura.

| Detección | Mitigación |
|---|---|
| p95 de escritura > 800 ms; commit ×3 sobre la base; IO wait > 15 %; cola Backend > 5–10 | 1) Escala vertical 8→12 vCPU / 32→64 GB (margen N+1) · 2) particionado mensual + PgBouncer · 3) réplica de solo lectura · 4) 4.º nodo / sharding al agotar margen |

En nube el equivalente es Aurora (writer + readers); EventBridge/SQS absorben el pico de sincronización 17:00–20:00 (ADR-05).

---

## 9. Degradación controlada (RT-09.08)

- **Enlace WAN:** QoS prioriza broker/WAL; colas diferidas fuera de la ventana; conmutación SD-WAN < 30 s entre fibra/Starlink/LTE.
- **Offline:** buffers RabbitMQ de 24 h (RNF-13.01) y buffers OTel de 24 h; reconciliación cronológica e idempotente al reconectar (RT-03.12).
- **Nube:** throttling en API Gateway, timeouts y reintentos con backoff en Celery, DLQ para tareas fallidas.

---

## 10. Pruebas de carga y estrés (RT-09.06 / RT-09.07 — T-13)

| Prueba | Carga | Escenario |
|---|---|---|
| Carga (RNF-19.04) | **1,5 × peak = 5.850 entregas/día ≈ 160 TPS sostenidos** | Pre-Producción, perfiles horarios reales (pick nocturno, despacho, preventa) |
| Estrés | Incremento hasta el **punto de quiebre ≥ 3×** | Curva de tiempo de respuesta vs carga |
| Informe de carga (RT-09.07) | Curvas, saturación, recursos (CPU/RAM/IOPS/enlace/colas) | Insumo al hito de producción (mes 16) y a la actualización de capacidad (RT-09.09, §11) |

Herramientas: **k6/Gatling** + drivers a medida contra las APIs (svc-erp-integration, svc-broker). Cortes: Etapa 1 (mes 13), Etapa 2 (mes 19), re-ejecución trimestral. **Calendario e hitos formales en el Formulario T-13.**

---

## 11. Actualización del plan de capacidad (RT-09.09)

- **Gestión de capacidad durante la Operación con proyección trimestral de crecimiento** (RT-09.09): consumo real vs. proyectado (vCPU/RAM/almacenamiento/enlace/colas/TPS), con **alertas anticipadas de agotamiento al 70 % / 2 semanas** y propuesta de ajuste de dimensionamiento y de costo.
- **Ventana de ampliación** conforme al procedimiento RT-08.05 (adición de vCPU/OSD dentro del físico; contrato escalonado de enlaces; 4.º nodo al acercarse al margen). La revisión se apoya en el informe de carga (RT-09.07) como insumo del hito de producción (mes 16).
- **Nube:** revisión FinOps (§4.5 Cloud) — evaluar umbrales Target Tracking y concurrencia reservada con al menos 30 días antes del peak de septiembre.

---

## 12. Referencias cruzadas con las decisiones de arquitectura

| ADR | Aporte a la vista de capacidad |
|---|---|
| ADR-01 | Monolito modular: el peak se absorbe con réplicas de la misma imagen (2→6 Fargate) |
| ADR-04 | Persistencia políglota: DynamoDB On-Demand (IoT) + Aurora (OLTP) + OLAP S3/Redshift (series consolidadas) |
| ADR-10 | Almacenamiento on-premise: RAID 10 NVMe > 100.000 IOPS, pool Ceph 5,76 TB |
| ADR-12 | Absorción del peak de septiembre con cómputo elástico (escala predictiva + reactiva) |

---

## 13. Trazabilidad normativa (resumen)

| Requisito | Cómo se cumple |
|---|---|
| RT-09.01 | Cálculo de capacidad con supuestos (§2–§3); umbrales p95 (§7) y Tabla 15 |
| RT-09.02 | Perfil de carga no plano como base del diseño (§1) |
| RT-09.03 | 3× en 3 años sin rediseño (§6) |
| RT-09.04 | Escalado horizontal automático con umbrales y límites (§5) |
| RT-09.05 | Primer cuello de botella declarado y mitigado (§8) |
| RT-09.06 / 09.07 | Pruebas de carga/estrés 1,5× peak en PreProd + informe de carga (§10, T-13) |
| RT-09.08 | Degradación controlada por servicio (§9) |
| RT-09.09 | Gestión trimestral de capacidad con alertas anticipadas y propuesta de ajuste (§11) |
| RT-15.01 | Sin capacidad ociosa financiada (auto-scaling + escala vertical dentro del margen) |
| RNF-19.04 | Pruebas 1,5× peak (§10) y carga de diseño 3.900 entregas/día (§3) |

---

## Referencias

1. `Caso_02_Logistica.md` — Tabla 14.1 (volumetría y proyección 3 años), Cap. 14/15 (valores), RNF-19.01–19.04.
2. `Bases_Tecnicas_Transversales.md` — RT-09.01…09.09, RT-03.20, RT-15.01.
3. `Dimensionamiento_Infraestructura_OnPremise_v05.md` — premisas §1.1, clúster §1.2, ancho de banda §3.7, crecimiento y pruebas §10.
4. `Propuesta_Arquitectura_Cloud_Caso02_CLAUDE_v2.md` v3.6 — §3.2/§3.5 (sizing y auto-scaling), §4.5 (FinOps).
5. `Tabla_Emplazamiento_OnPremise_v06.md` — §1.0 (componentes C1…C6, 35 ítemes) y §4 (dispositivos).
6. `Registro_Decisiones_Arquitectura_ADR_v01.md` — ADR-01/04/10/12.
7. `Arquitectura_de_Despliegue_v01.md` — ambientes (5), redes y HA con los que este documento es consistente.