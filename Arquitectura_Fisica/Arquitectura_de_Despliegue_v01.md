# Arquitectura de Despliegue — Caso 02 Logística

## Distribuidora Puelche S.A. — Licitación TFEP-01/2026 (Caso 02 — Logística)

| Atributo | Valor |
|---|---|
| Documento | Arquitectura de despliegue (Subdocumento 4, apartado 5) |
| Versión | v01 |
| Fecha | 2026-09-05 |
| Estado | En revisión interna |
| Autor | Arquitecto de Solución (LafroX) |
| Marco | BA Art. 16 (híbrido) · Art. 20 (DR) · Art. 21–22 (seguridad) · BTT RT-03.xx / RT-04.xx / RT-07.07 / RT-10.01 |
| Fuentes | `Arquitectura_Fisica_Hibrida_Consolidada_Caso02_v02.md` (§4/§5/§8/§10), `Propuesta_Arquitectura_Cloud_Caso02_CLAUDE_v2.md` v3.6 (§2/§6), `Tabla_Emplazamiento_OnPremise_v06.md`, `Dimensionamiento_Infraestructura_OnPremise_v05.md`, `Sala_Servidores_OnPremise_v02.md`, `Registro_Decisiones_Arquitectura_ADR_v01.md` (ADR-03/05/09/10/12) |

> **Finalidad.** Este documento responde el apartado 5 del Subdocumento 4 — **Arquitectura de despliegue: ambientes, redes, alta disponibilidad, recuperación ante desastres y respaldos** — de la Oferta Técnica, y es la vista de despliegue (ISO/IEC/IEEE 42010, RT-02.03) de la arquitectura híbrida. Consolida lo declarado en la fuente única (`Consolidado`) y en el documento de nube (v3.6) sin introducir cifras nuevas.

---

## 1. Ambientes de despliegue (RT-04.01)

Los cinco ambientes obligatorios del numeral 4.1 de las Bases Técnicas Transversales están habilitados como **condición del hito H3** (RT-04.01), aislados entre sí mediante **cuentas AWS separadas** bajo una organización centralizada de AWS Control Tower (aislamiento estricto + SCP):

| Ambiente | Cuenta AWS | VPC | Región | Uso |
|---|---|---|---|---|
| Desarrollo | Cuenta 1 | `10.104.0.0/16` | sa-east-1 | Integración continua, pruebas unitarias automáticas |
| Calidad (QA) | Cuenta 2 | `10.103.0.0/16` | sa-east-1 | Pruebas funcionales, estáticas, DAST/SAST |
| Pre-Producción | Cuenta 3 | `10.102.0.0/16` | sa-east-1 | Marcha blanca, pruebas de aceptación y de carga |
| Producción | Cuenta 4 | `10.101.0.0/16` | sa-east-1 | Operación real (Multi-AZ) |
| Recuperación ante Desastres | Cuenta 5 | `10.201.0.0/16` | us-east-1 | 5.º ambiente obligatorio (RT-04.01) |

Reglas que gobiernan el modelo de ambientes:

- **Paridad Pre-Producción = Producción (RT-04.02):** topología, versiones de componentes y configuración equivalentes; las diferencias por costo se declaran y justifican una a una.
- **On-premise como producción (RT-04.01/RT-03.10):** el despliegue on-premise es **producción** con la imagen única `wms_only`; esa misma imagen recorre Dev→QA→PreProd en la nube antes del cutover en Talca (ventana de 24 h) y en Concepción. **No se mantienen ambientes on-premise separados** — la paridad la garantizan la imagen única y el IaC versionado (RT-03.03).
- **Entrega continua (RT-04.05):** el pipeline CI ejecuta compilación, pruebas unitarias, análisis estático, análisis de composición, escaneo de secretos y escaneo de imágenes de contenedor, con **bloqueo automático del despliegue** ante hallazgos críticos o altos (RT-11.22).
- **Despliegue sin interrupción (RT-04.07):** estrategia **azul-verde** con canario en etapas, demostrada en PreProducción antes de cada paso a producción; reversión automatizada (RT-04.06).
- **Configuración externalizada (RT-04.08):** un mismo artefacto se promueve QA→PreProd→Prod sin recompilación; los secretos viven en gestor de secretos con rotación automática (RT-04.09), sin credenciales embebidas.
- **Datos no productivos (RT-11.25):** Dev, QA y PreProd usan **datos sintéticos** generados desde la volumetría del Cap. 14 del caso; las plantillas próximas a producción pasan por anonimización/seudonimización verificable (Amazon Macie).
- **Sin acceso interactivo a producción (RT-11.27):** los despliegues son exclusivamente por pipeline; el acceso administrativo excepcional es **just-in-time** vía AWS Systems Manager Session Manager con MFA, aprobación y sesión grabada.
- **Reducción de ambientes no productivos fuera de horario (RT-04.13):** Dev/QA/PreProd se apagan o reducen fuera del horario de uso, con el ahorro reflejado en la estructura de costos.
- **Portal web (N-01/N-02/N-03):** la SPA Angular se publica **por ambiente** en S3+CloudFront (bucket y distribución por cuenta AWS) y su backend es la misma imagen Django del ambiente; entra a producción con el **hito de enero 2029** (RNF-12.01).

---

## 2. Redes (topología, segmentación y conectividad)

### 2.1 WAN — tri-camino con SD-WAN (RT-03.17)

Cada instalación dispone de **caminos físicamente independientes** con **conmutación automática en < 30 s** (el requisito exige ≤ 5 min declarados; el diseño opera en < 30 s):

| Camino | Sitios | Rol |
|---|---|---|
| Fibra (D-03) | Talca, Concepción | Enlace principal en los 2 CD |
| Starlink Enterprise LEO (D-06) | 3 cross-docks (Curicó, Chillán, Los Ángeles) + respaldo en los 2 CD | Principal en cross-docks (cubre Los Ángeles 03:00–05:00 sin torres 4G); respaldo automático en CDs |
| LTE dual 4G Cat-12 (D-04) | Todos | 2 proveedores móviles distintos; tercer camino independiente |

SD-WAN con políticas centralizadas y BGP; los cross-docks salen **directo por Starlink a SQS/IoT/SSM** (configuración crítica) y sincronizan detalle a Talca por AMQPS entre brokers (C-13). La pérdida total del enlace se cubre con la **autonomía local 24 h** (CD) / **14 h** (terreno) — RT-03.10, RNF-13.01.

### 2.2 VPN Site-to-Site (costura C1)

- Extremos: **D-01 Firewall/UTM (HA activo-pasivo) → Customer Gateway** en cada CD; extremo cloud **VGW** del VPC Hub.
- Protocolo: **IPsec/IKEv2, AES-256-GCM, BGP, MTU 1436**; 2 túneles (activo + standby). Conmutación < 30 s sobre los tres caminos.

### 2.3 Segmentación de red (sin solapamiento)

| Dominio | Bloque | Segmentación |
|---|---|---|
| Talca | `10.1.x.x` | VLAN 10 (MGT), 20 (SRV), 30 (OPS), 40 (WKS), 50 (IOT) |
| Concepción | `10.2.x.x` | Misma segmentación VLAN |
| Cross-dockings | `10.3.x.x – 10.5.x.x` | Red plana simplificada + salida SSM/IoT outbound |
| VPC Hub | `10.100.0.0/16` | Transit Gateway; adjuntos de VPN |
| VPC Producción | `10.101.0.0/16` | Multi-AZ: DMZ pública `10.101.1.0/24` (az1) y `10.101.2.0/24` (az2) — ALB/WAF/CloudFront origin/NAT GW y portales N-01/N-02/N-03 · subredes app y datos privadas |

Modelo **Hub-and-Spoke** con VPC de tránsito central: la comunicación cross-VPC pasa por el Transit Gateway (inspección) y los servicios AWS (S3, SQS, DynamoDB, KMS, SSM) se consumen por **VPC Endpoints/PrivateLink sin tráfico por internet** (RT-03.03).

### 2.4 Zero Trust — flujos permitidos (BA Art. 21)

Todo el tráfico on-premise → nube es **outbound** (HTTPS/443, MQTTS/8883) sin conexiones entrantes salvo las dos excepciones controladas D-AL-05 sobre túnel IPsec autenticado:

| Flujo | Protocolo | Destino |
|---|---|---|
| Broker (shipper VM-03) → SQS FIFO | HTTPS 443 (VPC Endpoint SQS/PrivateLink) | AWS |
| Telemetría ADOT → CloudWatch/AMP | HTTPS 443 | AWS |
| Greengrass → IoT Core | MQTTS 8883 (X.509) | AWS |
| SSM Agent (todos los nodos) | HTTPS 443 saliente | SSM Endpoint regional |
| Sync WMS Concepción → Talca | TCP 8080 / 5432 | SRV-TALCA (on-prem) |
| Sync cross-dock → Talca (broker a broker) | AMQPS 5671 | SRV-TALCA (on-prem) |
| Caché Keycloak A-05/VM-C03 → S3 (import Realm) | HTTPS 443 (VPC Endpoint S3) | AWS (objeto cifrado) |
| *Excepción*: AWS DMS → PostgreSQL WMS (CDC) | TCP 5432 (over VPN) | VM-02 SRV-TALCA |
| *Excepción*: `celery-erp-sync` → ACL ERP | HTTPS 443 (over VPN) | VM-04 SRV-TALCA |

### 2.5 Capa pública (DMZ) y DNS

- **Primera línea:** CloudFront + AWS WAF v2 (OWASP Top 10 + reglas personalizadas) + Shield Advanced; autenticación API Gateway con Keycloak OIDC, cuotas por cliente y validación de esquema (RT-11.11).
- **DNS:** Route 53 con health checks activos; routing por latencia en operación normal y **failover automático hacia us-east-1** en contingencia.

---

## 3. Alta disponibilidad

### 3.1 Capa cloud (sa-east-1) — Multi-AZ

| Componente | AZ primaria | AZ secundaria | Failover automático |
|---|---|---|---|
| Aurora PostgreSQL | sa-east-1a (Writer) | sa-east-1b (Reader/Failover) | < 30 s |
| DynamoDB | Multi-AZ nativo | — | Transparente |
| EventBridge | 3 brokers en 3 AZ | — | Reelección de líder |
| ECS Fargate | sa-east-1a | sa-east-1b | Application Auto Scaling re-scheduling |
| ElastiCache Redis | sa-east-1a (Primary) | sa-east-1b (Replica) | < 60 s |
| ALB | sa-east-1a | sa-east-1b | Transparente |
| NAT Gateway | sa-east-1a | sa-east-1b (independiente) | Routing automático |

SLA de extremo a extremo sobre la **transacción crítica de negocio ≥ 99,9 % mensual** (RT-10.01, < 8,76 h/año), distinto de la clasificación TIER II del recinto (que es un medio, no el compromiso contractual).

### 3.2 Capa on-premise

| Capa | Diseño | Sustento |
|---|---|---|
| Cómputo | Clúster virtualizado **3 nodos** con replicación síncrona Ceph (factor 2, quórum propio) | Dimensionamiento v05 §1.2.5; elimina el SPOF de un par sin quórum |
| Almacenamiento | **RAID 10** (BD transaccional NVMe, IOPS > 100 k) y **RAID 6 con hot-spare** (evidencia/logs) | ADR-10 · RT-03.14/RNF-13.04/13.05 |
| Red | Par de firewall UTM (HA A/P), 2 switches core + switch de gestión | RNF-13.03 |
| WAN | Tri-camino fibra + Starlink + LTE (SD-WAN) | RT-03.17 |
| Energía | UPS doble conversión **6 kVA N+1** (≥ 30 min a plena carga, RT-06.07) + generador **12 kVA** estanque 24 h (RT-06.08) + ATS | Sala de Servidores v02 §5 |
| Clima | Clima de precisión **N+1** ASHRAE TC 9.9, PUE de diseño 1,7 | Sala de Servidores v02 §5.3 |
| Recinto | Sala mediana, 4 gabinetes, TIER II objetivo (99,741 %) | Sala de Servidores v02 §1 |

VMs dimensionadas con headroom ×1,5 (RNF-19.04) para tolerar **3.900 entregas/día** en el peak de septiembre. SPOF declarados y mitigados (RT-02.11): periféricos de andén (respaldo manual), clúster Talca sin SPOF estructural, Concepción nodo único (autonomía 24 h + DRP), cross-dock mini-PC único (ventana de 3 h + sincronización diferida).

---

## 4. Recuperación ante desastres (BA Art. 20 · RT-07.07 · RNF-20.06)

### 4.1 DRP nube (sa-east-1 → us-east-1) — activo-pasivo warm standby

- **Mecanismo:** Aurora Global Database (réplica us-east-1, lag < 1 s) · DynamoDB Global Tables · **S3 CRR** (RTC < 15 min) · **AWS DMS CDC** del PostgreSQL WMS on-premise (lee `wal_level=logical`; si la VPN cae, encola y reanuda sin pérdida).
- **Objetivos:** **RTO ≤ 4 h / RPO ≤ 15 min** (RNF-20.06); RPO declarado de mensajes no críticos ≤ 24 h, reducido a ≤ 15 min para los críticos con patrón **outbox dual-write**.
- **Modalidad justificada (RT-07.01):** activo-pasivo; activo-activo duplicaría la infraestructura transaccional (~105 TPS peak) con reconciliación de doble escritura sin beneficio frente al RTO comprometido.
- **Procedimiento:** decisión de failover **manual con disparador declarado** (health check de la región primaria < 5 min) y protección contra conmutación innecesaria (confirmación SNS + autorización); pasos 4–7 **automatizados por AWS Systems Manager Automation** (promoción Aurora 15–20 min, escalado ECS, actualización DNS 45–60 min). El RTO se cumple porque la réplica es legible y la región DR está "caliente" (escalable < 30 min a carga completa).
- **Retorno (failback):** procedimiento documentado en 6 pasos — re-sincronización con catch-up verificado, reconciliación de transacciones de la contingencia contra la bitácora (RT-03.12), transferencia de eventos pendientes, conmutación coordinada de DNS, validación funcional e informe con tiempo real.
- **Pruebas:** conmutación real **≥ 2 veces/año** con informe de RTO/RPO efectivos y plan de corrección de brechas (RT-07.07, Art. 20).

### 4.2 DRP local (Talca → Concepción)

- Promoción controlada del WMS edge (VM-C01) mediante **procedimiento de 5 pasos**; Concepción ya opera autónoma (latencia ≤ 1 s de picking, RNF-05.01). **RTO +1–2 h** para la bodega.
- **Identidad sin conmutación local:** el maestro Keycloak está en la nube y las cachés A-05/VM-C03 siguen validando firmas offline — el DRP de identidad es la misma autoridad en nube, sin promoción local a maestro (elimina una clase entera de riesgos de DR).

### 4.3 DRP de la identidad (ADR-06)

El maestro vive en la nube (Multi-AZ) con réplica DR us-east-1; las cachés locales son de solo lectura. No existe maestro local a promover, por lo que la identidad **no depende del switchover**.

---

## 5. Respaldos — esquema 3-2-1-1-0 (RNF-20.07)

**Esquema único** para toda la arquitectura híbrida (nube + on-premise):

| Pierna | Implementación |
|---|---|
| **3 copias** de los datos | (1) Datos activos sa-east-1 + WMS activo Talca; (2) Snapshot automatizado Aurora + respaldo local on-premise (D-05); (3) Backup exportado a S3 |
| **2 medios** | PostgreSQL/Aurora y S3 (almacenamiento de objetos) |
| **1 copia fuera del sitio** | S3 Cross-Region Replication → bucket en us-east-1 |
| **1 copia inmutable** | **S3 Object Lock (WORM, Compliance Mode) + AWS Backup Vault Lock** (ni el root puede eliminarla); `s3-documents-legal` y `s3-audit-logs` en Compliance, no Governance |
| **0 errores** | Restore testing automatizado mensual (Lambda) + verificación de restauración local + prueba DR semestral |

- **D-05 (NAS local con WORM) es la copia local de recuperación rápida** y **NO cuenta como la pierna inmutable**; permite restaurar el WMS en ≤ 4 h (RNF-20.06) sin depender del enlace WAN. RPO ≤ 15 min por AWS DMS CDC del WAL lógico (wal_level=logical) hacia la nube antes de la copia local.
- **Custodia física (RT-06.26/06.27/06.28):** medio de respaldo transportable, cifrado y rotado semanal (RT-07.10), trasladado bajo custodia acreditada a bóveda externa distinta del sitio primario; la pierna inmutable S3 es complementaria, no reemplaza la custodia física.

**Plan AWS Backup:**

| Recurso | Frecuencia | Retención | Destino |
|---|---|---|---|
| Aurora PostgreSQL | Diario + PITR continuo | 35 días | Backup Vault (cifrado CMK) |
| DynamoDB | Diario (On-Demand) | 35 días | Backup Vault |
| EFS | Diario | 30 días | Backup Vault |
| EBS | Diario (snapshots) | 14 días | Backup Vault |
| S3 documentos legales | Continuo (versioning + Object Lock) | 6 años | S3 + réplica CRR |
| Logs de seguridad/auditoría | Continuo | 7 años (Object Lock) | S3 archivo |

Vault Lock con enfriamiento de 3 días y retención mínima de 1 año; una vez bloqueado, ni la cuenta raíz puede eliminar respaldos. Retención sanitaria: **trazabilidad 5 años + vida útil** (D.S. 977/96), consistente con el lago analítico S3 y el repositorio de datos históricos (RT-05.15).

---

## 6. Referencias cruzadas con las decisiones de arquitectura

| ADR | Aporte a la vista de despliegue |
|---|---|
| ADR-03 | Modelo híbrido: borde operacional on-premise + carga principal en nube (justificación Art. 16) |
| ADR-05 | Capa de mensajería RabbitMQ local + SQS/EventBridge (buffer offline, Zero Trust outbound) |
| ADR-09 | DR warm standby activo-pasivo multi-región (RTO/RPO, pruebas 2×/año) |
| ADR-10 | Almacenamiento on-premise y niveles RAID (RAID 10 / RAID 6, RT-03.14) |
| ADR-12 | Cómputo elástico y absorción del peak de septiembre (escala predictiva + reactiva) |

---

## 7. Trazabilidad normativa (resumen)

| Requisito | Cómo se cumple |
|---|---|
| RT-04.01 | 5 ambientes habilitados (hito H3) |
| RT-04.02 | PreProd = Prod en topología, versiones y configuración |
| RT-04.05/04.06 | CI con gates de seguridad y despliegue automatizado con reversión |
| RT-04.07 | Azul-verde/canario demostrado en PreProd |
| RT-04.08/04.09 | Configuración por ambiente y secretos con rotación |
| RT-03.01/03.02 | AWS sa-east-1 primaria/us-east-1 DRP; Multi-AZ en componentes críticos |
| RT-03.03 | IaC 100 % versionado en el repositorio del CLIENTE |
| RT-03.10 | Autonomía 24 h / 14 h sin enlace |
| RT-03.12 | Sincronización automática y reconciliación determinista al reconectar |
| RT-03.14 | RAID declarado y justificado frente a alternativas |
| RT-03.17 | Enlace redundante, caminos/proveedores distintos, conmutación < 30 s |
| RT-07.07 / Art. 20 | Pruebas de DR reales ≥ 2 veces/año con medición de RTO/RPO |
| RT-10.01 | Disponibilidad e2e ≥ 99,9 % mensual sobre la transacción crítica |
| RNF-20.06 / 20.07 | RTO ≤ 4 h / RPO ≤ 15 min · respaldo 3-2-1-1-0 |
| Art. 21 | Zero Trust: solo outbound, sin conexiones entrantes (salvo D-AL-05) |

---

## Referencias

1. `Arquitectura_Fisica_Hibrida_Consolidada_Caso02_v02.md` — fuente única (red §4, costuras §5, HA/DRP §8, ambientes §10).
2. `Propuesta_Arquitectura_Cloud_Caso02_CLAUDE_v2.md` v3.6 — VPC/subredes §2, Multi-AZ §6.1, DRP §6.2, respaldos §6.3.
3. `Tabla_Emplazamiento_OnPremise_v06.md` — Bloques D (red) y N (nube), SPOF §6.
4. `Sala_Servidores_OnPremise_v02.md` — recinto, energía, clima, custodia de medios.
5. `Dimensionamiento_Infraestructura_OnPremise_v05.md` — clúster Ceph, RAID, capacidad.
6. `Registro_Decisiones_Arquitectura_ADR_v01.md` — ADR-03/05/09/10/12.
7. Bases Administrativas — Art. 16, 20, 21, 22. Bases Técnicas Transversales — RT-03.xx, RT-04.xx, RT-07.07, RT-10.01.