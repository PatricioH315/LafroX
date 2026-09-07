# PROPUESTA DE ARQUITECTURA DE INFRAESTRUCTURA CLOUD
## Caso 02: Sistema Logístico de Cadena de Frío con Operación Edge
### Versión 3.6 — Documento de Arquitectura Técnica Formal (Alineado con decisiones arquitectónicas y con el segmento on-premise)

---

## TABLA DE CONTENIDOS

1. [Visión General de la Arquitectura Cloud](#1-visión-general-de-la-arquitectura-cloud)
2. [Topología de Red y Conectividad](#2-topología-de-red-y-conectividad)
3. [Cómputo](#3-cómputo)
   - 3.1 Django Monolito Modular
   - 3.2 Computación Serverless (vs. instancias permanentes)
   - 3.3 Keycloak (IdP)
   - 3.4 Edge Greengrass
   - 3.5 Dimensionamiento
4. [Almacenamiento y Bases de Datos](#4-almacenamiento-y-bases-de-datos)
   - 4.5 FinOps
   - 4.6 Reversibilidad
5. [Seguridad, Identidad y Cumplimiento](#5-seguridad-identidad-y-cumplimiento)
6. [Alta Disponibilidad (HA) y DRP](#6-alta-disponibilidad-ha-y-drp)
7. [Matriz de Justificación Arquitectónica Exhaustiva](#7-matriz-de-justificación-arquitectónica-exhaustiva)

---

## 1. VISIÓN GENERAL DE LA ARQUITECTURA CLOUD

### 1.1 Resumen Ejecutivo

La presente arquitectura responde a los requerimientos del Caso 02 de Logística, un sistema de gestión de cadena de frío que opera en condiciones extremas: temperaturas de −22 °C, hasta 14 horas de operación sin conectividad, peaks de procesamiento en septiembre, y la necesidad de reconciliar datos de forma asíncrona con sistemas ERP que no pueden ser intervenidos. La solución debe garantizar trazabilidad completa de temperatura, integridad de documentos tributarios y fiscales, y resiliencia operacional tanto en el borde (edge) como en la nube central.

La arquitectura propuesta adopta un modelo **Cloud-First Híbrido con WMS On-Premise**, donde la nube pública aloja el monolito Django modular (todos los módulos de negocio), el motor analítico (Redshift), la integración IoT, y los servicios de identidad (Keycloak). El WMS (inventario, picking, recepción) se ejecuta on-premise en VM-01 (Talca) para garantizar operación sin internet en la cámara de congelado a −22 °C. Una única imagen Docker de Django opera en dos modos: `MODE=full` (cloud, todos los módulos) y `MODE=wms_only` (on-premise, solo módulos de bodega). Sincronización continua vía AWS DMS CDC (RPO ≤ 15 min).

> **Vistas arquitectónicas conforme ISO/IEC/IEEE 42010 (RT-02.03):** la descripción de la arquitectura se organiza en las cinco vistas exigidas — **lógica** (Arquitectura Lógica v1, Diagramas/Maqueta), **de procesos** (flujos Mermaid + plantillas de despliegue), **de despliegue** (este documento §2/§7 + Arquitectura Física Consolidada), **de datos** (§3 y propuesta de datos) y **de seguridad** (§5 y matriz de seguridad) —, manteniendo cada vista trazable al modelo de capas del Cap. 2.

### 1.2 Evaluación y Selección del Proveedor Cloud

De acuerdo con el Art. 16.3 de las Bases Administrativas, el proveedor de nube debe ser de carácter público, multi-zona, con capacidades de IAM, servicios administrados y segmentación de red. Se evalúan los tres grandes proveedores:

| Criterio | AWS | Azure | Google Cloud |
|---|---|---|---|
| Presencia de regiones en Latinoamérica | São Paulo, Chile (anunciado) | Brasil Sur, Chile | São Paulo |
| Servicios IoT administrados | AWS IoT Core + Greengrass | Azure IoT Hub + IoT Edge | Cloud IoT Core (deprecado → alternativas) |
| Edge Computing maduro | AWS Greengrass v2 ✅ | Azure IoT Edge ✅ | — |
| Certificaciones de seguridad (ISO 27001, SOC 2) | ✅ | ✅ | ✅ |
| Gestión de claves (KMS) | AWS KMS + CloudHSM | Azure Key Vault + HSM | Cloud KMS + HSM |
| Cumplimiento normativo Chile (Ley 21.719 datos personales, Ley 21.663 ciberseguridad, SII) | ✅ | ✅ | ✅ |
| Madurez de servicios administrados (RDS, ECS Fargate, EventBridge) | Alta | Alta | Media |
| Soporte multi-cuenta y Control Tower | AWS Control Tower ✅ | Azure Management Groups ✅ | Resource Hierarchy |

**Decisión: Amazon Web Services (AWS)**

**Justificación:** AWS presenta la mayor madurez en servicios de IoT con soporte real para Edge Computing en condiciones de conectividad intermitente (AWS IoT Greengrass), lo cual es un requerimiento no negociable del Caso 02 (operación a −22 °C sin señal). Adicionalmente, la disponibilidad de la región **sa-east-1 (São Paulo)** como región primaria y la región emergente de **us-east-1 (Virginia)** como región secundaria para DRP garantiza latencias aceptables y cumplimiento normativo. AWS Control Tower permite el aislamiento estricto de los **5 ambientes mandatados** (Desarrollo, QA, Preproducción, Producción y **Recuperación ante Desastres**) mediante cuentas AWS separadas bajo una organización centralizada. La oferta de servicios administrados (Amazon RDS, Amazon Aurora, Amazon EventBridge, Amazon ECS con AWS Fargate) cubre el 100% de los requerimientos técnicos transversales.

### 1.3 Principios Arquitectónicos Rectores

1. **Zero Trust por defecto:** Ningún componente confía implícitamente en otro. Toda comunicación requiere autenticación, autorización y cifrado.
2. **Stateless en cómputo, Stateful en persistencia:** Los servicios de aplicación no mantienen estado; el estado reside exclusivamente en las capas de persistencia gestionadas.
3. **Diseño para el fallo:** Se asume que cualquier componente puede fallar. Los servicios edge operan de forma autónoma durante 14h+ sin pérdida de datos.
4. **Idempotencia en todas las integraciones:** Los mensajes procesados múltiples veces producen el mismo resultado, resolviendo la reconciliación asíncrona post-desconexión.
5. **Inmutabilidad de datos críticos:** Los registros de temperatura, documentos tributarios y logs de auditoría son inmutables una vez escritos.
6. **Separación estricta OLTP/OLAP:** Las cargas transaccionales y analíticas se ejecutan en motores independientes para garantizar el rendimiento de ambas.
7. **Infraestructura como Código (IaC):** El 100% de la infraestructura se define mediante AWS CloudFormation y/o Terraform, con pipelines de CI/CD para cada ambiente. **Todo el código de infraestructura queda versionado en el repositorio del CLIENTE (RT-03.03), revisable y reproducible; no se admite infraestructura creada manualmente por consola, salvo la cuenta raíz inicial, cuya creación queda documentada.**

---

## 2. TOPOLOGÍA DE RED Y CONECTIVIDAD

### 2.1 Arquitectura de Red General

La topología de red se estructura en torno a un modelo **Hub-and-Spoke** con un VPC de tránsito central que conecta todos los entornos, más VPCs dedicados por ambiente para lograr el aislamiento estricto requerido por las Bases Técnicas (Cap. 4).

```
INTERNET
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│  AWS Shield Advanced (Anti-DDoS)                            │
│  AWS WAF v2 (OWASP Top 10 + Reglas Personalizadas)          │
│  Amazon CloudFront (CDN + TLS 1.3)                          │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│  VPC HUB / TRÁNSITO  (10.100.0.0/16)  — Región sa-east-1   │
│  AWS Transit Gateway                                         │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Subred Pública DMZ    (10.100.1.0/24)               │   │
│  │  - Application Load Balancer (ALB)                   │   │
│  │  - API Gateway (REST + WebSocket)                    │   │
│  │  - NAT Gateway (HA multi-AZ)                         │   │
│  └──────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Subred Privada Servicios  (10.100.2.0/24)           │   │
│  │  - AWS PrivateLink endpoints                         │   │
│  │  - VPC Endpoints (S3, SQS, DynamoDB, KMS, SSM)      │   │
│  └──────────────────────────────────────────────────────┘   │
└────────────────────────┬────────────────────────────────────┘
                         │ AWS Transit Gateway
          ┌──────────────┼──────────────┬──────────────┬──────────────┬──────────────┐
          │              │              │              │              │              │
          ▼              ▼              ▼              ▼              ▼
    VPC-PROD       VPC-PREPROD      VPC-QA        VPC-DEV      VPC-DR
 (10.101.0.0/16) (10.102.0.0/16) (10.103.0.0/16) (10.104.0.0/16) (us-east-1)
  Cuenta AWS-P   Cuenta AWS-PP  Cuenta AWS-Q  Cuenta AWS-D  Cuenta AWS-DR
```

### 2.2 Diseño de Subredes por VPC de Producción

Cada VPC de producción (y por analogía los demás ambientes) implementa tres capas de subredes en **dos o más Zonas de Disponibilidad (AZ)**:

| Capa | Subred | CIDR (ejemplo) | Componentes |
|---|---|---|---|
| **Pública (DMZ)** | `sn-pub-az1` | 10.101.1.0/24 | ALB, WAF, CloudFront Origin, NAT GW |
| **Pública (DMZ)** | `sn-pub-az2` | 10.101.2.0/24 | ALB redundante, NAT GW secundario |
| **Privada App** | `sn-app-az1` | 10.101.10.0/24 | ECS Fargate tareas, Lambda, EventBridge |
| **Privada App** | `sn-app-az2` | 10.101.11.0/24 | ECS Fargate tareas, Lambda, EventBridge |
| **Privada Data** | `sn-data-az1` | 10.101.20.0/24 | RDS/Aurora Primary, ElastiCache, OpenSearch |
| **Privada Data** | `sn-data-az2` | 10.101.21.0/24 | RDS/Aurora Replica, ElastiCache Replica |
| **IoT / Edge** | `sn-iot-az1` | 10.101.30.0/24 | AWS IoT Core endpoints, MQTT ingestion |
| **IoT / Edge** | `sn-iot-az2` | 10.101.31.0/24 | AWS IoT Core endpoints redundantes |

**Diagrama de Arquitectura de Subredes (VPC-PROD)**
*Este diagrama ilustra cómo la tabla anterior se traduce físicamente dentro del VPC de Producción, separando por capas de seguridad (horizontal) y por Zonas de Disponibilidad (vertical).*

```text
╔══════════════════════════════════════════════════════════════════════════╗
║  ELEMENTOS GLOBALES (capa de red global, fuera del VPC):                 ║
║  CloudFront + WAF + Shield (primera línea) · Route 53 (DNS) ·            ║
║  AWS Global Accelerator · AWS IoT Core (MQTT global) ·                   ║
║  Keycloak (IdP) · S3 (Data Lake/backup) · EventBridge                    ║
╚══════════════════════════════════════════════════════════════════════════╝
                              │  Ingreso Internet / usuarios móviles
                              ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                           VPC-PROD (10.101.0.0/16)                      │
│                                                                         │
│        ZONA DE DISPONIBILIDAD 1 (AZ1)    ZONA DE DISPONIBILIDAD 2 (AZ2) │
│                                                                         │
│  ┌───────────────────────────────┐   ┌───────────────────────────────┐  │
│  │ CAPA PÚBLICA (DMZ)            │   │ CAPA PÚBLICA (DMZ)            │  │
│  │ sn-pub-az1 (10.101.1.0/24)    │   │ sn-pub-az2 (10.101.2.0/24)    │  │
│  │ - ALB (HTTP/HTTPS microsrv.)  │   │ - ALB Redundante              │  │
│  │ - NLB (MQTT IoT TCP/8883)     │   │ - NLB Redundante              │  │
│  │ - NAT Gateway 1               │   │ - NAT Gateway 2               │  │
│  └──────────────┬────────────────┘   └───────────────┬───────────────┘  │
│                 │                                    │                  │
│  ┌──────────────▼────────────────┐   ┌───────────────▼───────────────┐  │
│  │ CAPA PRIVADA APP              │   │ CAPA PRIVADA APP              │  │
│  │ sn-app-az1 (10.101.10.0/24)   │   │ sn-app-az2 (10.101.11.0/24)   │  │
│  │ - Fargate (Django monolito) │   │ - Fargate (Django monolito) │  │
│  └──────────────┬────────────────┘   └───────────────┬───────────────┘  │
│                 │                                    │                  │
│  ┌──────────────▼────────────────┐   ┌───────────────▼───────────────┐  │
│  │ CAPA PRIVADA DATA             │   │ CAPA PRIVADA DATA             │  │
│  │ sn-data-az1 (10.101.20.0/24)  │   │ sn-data-az2 (10.101.21.0/24)  │  │
│  │ - Aurora/RDS (Primary+Read)   │   │ - Aurora/RDS (Réplica)        │  │
│  │ - ElastiCache Redis (caché)   │   │ - ElastiCache Redis (réplica) │  │
│  │ (DynamoDB = serverless global)│   │                               │  │
│  └───────────────────────────────┘   └───────────────────────────────┘  │
│                                                                         │
│  ┌───────────────────────────────┐   ┌───────────────────────────────┐  │
│  │ CAPA IOT / EDGE               │   │ CAPA IOT / EDGE               │  │
│  │ sn-iot-az1 (10.101.30.0/24)   │   │ sn-iot-az2 (10.101.31.0/24)   │  │
│  │ - AWS IoT Core Endpoints      │   │ - AWS IoT Core Endpoints      │  │
│  │ - Regla MQTT -> Lambda val.   │   │ - Regla redundante            │  │
│  └───────────────────────────────┘   └───────────────────────────────┘  │
│                                                                         │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │  VIRTUAL PRIVATE GATEWAY (VGW) — terminación de la VPN híbrida   │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                      │ Site-to-Site VPN IPsec / Direct Connect          │
└──────────────────────┼──────────────────────────────────────────────────┘
                       ▼
        ON-PREMISE (Talca/Concepción/Cross-dock): firewall D-01 (Customer
        Gateway) · WMS A-01 · BD A-02 · ACL ERP A-04 · Broker A-03
```
**Notas del diagrama:**
- **Elementos globales** (CloudFront/WAF/Shield, Route 53, Global Accelerator, AWS IoT Core, Keycloak, S3, EventBridge, DynamoDB) son servicios administrados a nivel de región/cuenta y **no residen en una subred** del VPC; se representan fuera del borde del VPC.
- **NLB dedicado para MQTT (TCP/8883):** ingesta masiva de telemetría de temperatura (sección 2.3), en la DMZ junto al ALB.
- **VGW / VPN Site-to-Site / Direct Connect:** terminación en la nube de la conectividad hacia el on-premise (sección 2.4); el extremo customer-side (firewall D-01) se diseña en la contraparte on-premise.
- **Capa Data:** Aurora/RDS (OLTP) + ElastiCache Redis (caché/sesiones); DynamoDB es serverless global y no se instancia en una subred.

**Reglas de Seguridad de Grupos (Security Groups) y Network ACLs:**
- Las subredes de datos **no aceptan tráfico directo desde internet** en ninguna circunstancia.
- La comunicación entre capas se permite únicamente en los puertos estrictamente necesarios (principio de mínimo privilegio).
- Los Network ACLs actúan como segunda línea de defensa, con reglas deny-all de entrada excepto para puertos explícitamente autorizados.

### 2.3 Balanceo de Carga

- **Amazon CloudFront:** Distribución global con TLS 1.3, caching de contenido estático, integración con WAF y Shield Advanced. Actúa como primera línea de distribución y protección.
- **Application Load Balancer (ALB):** Para el monolito Django HTTP/HTTPS con routing basado en rutas (`/api/v1/logistics/*`), soporte de WebSocket para telemetría en tiempo real y health checks automáticos. Distribuido en múltiples AZ.
- **Network Load Balancer (NLB):** Para el ingreso de datos MQTT de IoT (protocolo TCP/8883) con alta throughput y latencia ultra-baja, necesario para la ingesta masiva de telemetría de temperatura.
- **AWS API Gateway (RT-11.11):** Como fachada unificada del monolito Django, con throttling, autenticación vía Keycloak OIDC y AWS WAF integrado. Aplica **cuotas y límites de tasa** por cliente (usage plans/API keys), **validación de esquema** de peticiones (request models OpenAPI) e **inspección de carga útil** (parsing y validación estricta del body antes del backend), rechazando tráfico que no cumple el contrato de interfaz.

### 2.4 Conectividad Segura con On-Premise y Edge (terminación en la nube)

> **Alcance cloud-only:** Este documento diseña únicamente la terminación en la nube de las conexiones hacia el on-premise y el borde. La infraestructura física on-premise (bodegas, dispositivos edge, terminales) se diseña en paralelo; aquí solo se definen los puntos de terminación y los protocolos que la nube expone para recibirlos.

- **AWS Site-to-Site VPN / AWS Direct Connect:** Terminación en la nube de los túneles IPSec/IKEv2 que conectan las instalaciones físicas (Talca, Concepción y cross-docks) con los VPCs de producción. La nube provee el gateway de VPN privado (amazon-side) y el VIF de Direct Connect; el extremo on-premise (customer-side) se define en la sección on-premise paralela. BGP para enrutamiento dinámico y failover.
- **AWS IoT Core (MQTT/HTTPS):** Punto de entrada cloud para los dispositivos edge (vehículos refrigerados, cámaras de congelado, preventistas/conductores). Soporta reconexión automática y encolamiento de mensajes durante desconexiones. Incluye el registro central, la resolución de credenciales (X.509) y las IoT Policies.
- **AWS IoT Greengrass v2 (gestión cloud del borde):** Desde la nube se orquesta y versiona el runtime edge (despliegue de componentes, Stream Manager, actualizaciones OTA, gemelos digitales). El borde opera offline ≥14h y sincroniza al recuperar enlace.

### 2.5 Conectividad Multi-Región para DRP

- **Región Primaria:** `sa-east-1` (São Paulo, Brasil)
- **Región Secundaria DRP:** `us-east-1` (Virginia del Norte, EE.UU.)
- **Amazon Route 53:** DNS con health checks activos y failover automático. Políticas de routing: Latency-based para operación normal, Failover para DRP.
- **AWS Global Accelerator:** Acelera el tráfico de usuarios mediante la red troncal global de AWS, reduciendo la latencia de reconexión durante eventos de failover.

---

## 3. CÓMPUTO

### 3.1 Arquitectura de Aplicación: Django Monolito Modular

**Amazon ECS con AWS Fargate (Elastic Container Service)** despliega una **única imagen Docker de Django** como monolito modular. La decisión de monolito modular (en lugar de microservicios) se fundamenta en:

- **Equipo reducido (4 personas):** Un monolito en Python/Django es operativamente sostenible; 8 microservicios en 4 lenguajes distintos (Python, Java, Go, Node.js) exigen conocimiento operativo que el equipo no tiene.
- **Volumen moderado (~31.000 pedidos/mes):** No se justifica la complejidad de microservicios para este volumen. Un monolito bien dimensionado (2-3 instancias) maneja la carga con margen.
- **Mismo código, dos despliegues:** Una sola imagen Docker opera en dos modos: `MODE=full` (cloud, todos los 12 módulos) y `MODE=wms_only` (on-premise, solo inventario + picking + recepción). Esto garantiza consistencia de lógica de negocio entre cloud y WMS local.
- **Cumplimiento del rechazo a "monolito sin despliegue independiente" (Cap. 2, Bases Admin, y BTT §4.1):** El monolito modular **no es un monolito monolítico**: cada módulo Django (inventario, picking, recepción, telemetría, bi, ...) es un namespace Python/Celery desplegable por separado, con sus propias migraciones, colas SQS y autoscaling independiente. Los módulos críticos (picking/recepción en el borde, telemetría/calidad en la nube) pueden **desplegarse, versionarse y escalarse de forma independiente** dentro de la misma imagen vía perfiles de tarea ECS; esto satisface la exigencia de despliegue independiente de componentes críticos sin incurrir en la complejidad operativa de microservicios. Las integraciones (ERP vía ACL, EDI, SII) se aíslan en el módulo `integraciones` con contrato versionado, respondiendo a la capa de integración explícita y gobernada (Cap. 2).

#### Módulos del Sistema

| Módulo Django | Responsabilidad | Despliegue |
|---|---|---|
| `inventario` | Gestión de stock, ubicaciones, lotes, vencimientos | Cloud + On-Premise |
| `picking` | Preparación de pedidos, ola, asignación de ubicaciones | Cloud + On-Premise |
| `recepcion` | Recepción de mercadería, control de temperatura, conformidad | Cloud + On-Premise |
| `preventa` | Toma de pedidos, validación de crédito/stock, catálogo | Solo Cloud |
| `reparto` | Despacho, seguimiento GPS, POD, devoluciones | Solo Cloud |
| `rutas` | Optimización de rutas, asignación de camiones, ventanas de tiempo | Solo Cloud |
| `cobranza` | Rendición de efectivo, liquidación, estado de cuenta | Solo Cloud |
| `calidad` | Control de temperatura, excursiones térmicas, trazabilidad sanitaria | Solo Cloud |
| `bi` | Costo de servir, OTIF, Fill Rate, tableros, reportes | Solo Cloud |
| `edi` | Intercambio electrónico con cadenas (clientes retail) | Solo Cloud |
| `telemetria` | Ingesta IoT, GPS, alertas de cadena de frío | Solo Cloud |
| `integraciones` | ERP (lectura vía ACL), SII, servicios externos | Solo Cloud |

#### Workers Celery (Tareas Asíncronas)

Las tareas que en arquitectura de microservicios eran servicios separados, se ejecutan como **workers Celery** dentro del mismo contenedor o en contenedores separados del mismo código:

| Worker Celery | Trigger | Responsabilidad |
|---|---|---|
| `celery-reconciliation` | Cola SQS post-desconexión | Reconciliación asíncrona de datos acumulados durante offline |
| `celery-erp-sync` | Cola SQS programada | Sincronización lectura con ERP vía ACL on-premise |
| `celery-report-generator` | Celery Beat (periódico) | Generación automática de reportes ejecutivos (RF-11.01) |
| `celery-alert-engine` | EventBridge rules | Procesamiento de alertas por síntomas de negocio |
| `celery-analytics-exporter` | CDC Aurora → EventBridge | Exportación de datos de Aurora hacia Redshift |

**Documentación de contratos de interfaz (RT-05.16, RT-05.17):** Los servicios síncronos (REST/GraphQL) se documentan en **OpenAPI 3.1** generada desde el código (DRF Spectacular). Los flujos dirigidos por eventos se documentan en **AsyncAPI 2.6+** generada desde las definiciones de EventBridge (eventos entre módulos Django) y de SQS (colas Celery). Toda interfaz se versiona semánticamente con compatibilidad hacia atrás y política de obsolescencia de 6 meses (RT-05.17). El catálogo vivo de contratos se publica en un repositorio Git compartido con la contraparte técnica (sincronización automática en cada build).

**Coexistencia de mensajería (on-premise vs nube):** La capa de mensajería del sistema opera en dos dominios coordinados: (1) **on-premise** usa **RabbitMQ** (A-03) como broker de colas offline en cada CD, con buffers locales de 24 h para transacciones y telemetría cuando el enlace WAN no está disponible; (2) **cloud** usa **Amazon SQS** (colas de trabajo Celery: reconciliación, ERP sync), **Amazon EventBridge** (bus de eventos entre módulos Django y reglas de alertas) y **AWS IoT Core** ( MQTT para ingesta de telemetría desde Greengrass). El envío del broker local hacia la nube lo ejecuta un **shipper residente en VM-03 (modo `wms_only`)**: publica el buffer RabbitMQ en orden cronológico e idempotente hacia la cola **SQS FIFO** por HTTPS/443 vía **VPC Endpoint SQS (PrivateLink)**; el worker `celery-reconciliation` procesa la cola al recuperar el enlace WAN. Esto no abre conexiones entrantes al on-premise (Zero Trust); AMQPS 5671 queda reservado a la sincronización entre brokers locales on-premise (cross-dock → Talca). Esta dualidad es inherente al modelo híbrido (Art. 16): el broker local garantiza la autonomía de 24 h (RNF-13.01) y la nube provee durabilidad y escalabilidad. Ambos dominios se declaran explícitamente en la matriz de integración (§7.7, §7.9).

**Configuración ECS Fargate:**
- **Tareas ECS Fargate** dimensionadas en vCPU/RAM (no requiere nodos EC2 gestionados): tareas tipo `2 vCPU / 4 GB` para el monolito Django y workers Celery.
- **AWS Application Auto Scaling** para auto-scaling inteligente durante peaks (septiembre: escalado hasta 3× la capacidad base).
- **Target Tracking Auto Scaling** basado en métricas de CPU y memoria.
- **Namespace ECS** único con RBAC a nivel de Django (groups/permissions de Django ORM, no de ECS).

### 3.2 Computación Serverless

**AWS Lambda** se utiliza solo para cargas event-driven que requieren ejecución ultrarrápida y sin estado. La mayoría de tareas asíncronas se ejecutan en workers Celery (§3.1). **Análisis comparativo frente a instancias permanentes (RT-03.09):** para el perfil variable del caso (peak de septiembre ≈ doble volumen, carga dispersa de telemetría IoT) se comparó el **tco de Fargate/Lambda (escalado a cero y escala automática, pago por uso) vs. un clúster EC2 permanente dimensionado al peak**: el EC2 permanente exige capacidad ociosa gran parte del año ≥ 3× la media mensual (≈ COP adicional anual declarado en §4.5), frente a Fargate con auto-scaling que reduce el costo anual en ≈ 30-40 % manteniendo los umbrales del RT-09.4. La comparación queda registrada en la estructura de costos (FinOps §4.5) y en el dimensionamiento (Dimensionamiento on-premise).

| Función Lambda | Trigger | Propósito |
|---|---|---|
| `fn-iot-validator` | AWS IoT Core Rules | Validación en tiempo real de lecturas de temperatura fuera de rango |
| `fn-document-signer` | S3 Event / SNS | Firma digital de documentos tributarios (DTE / guía de despacho electrónica) |

**Tareas migradas a Celery workers (ya no son Lambda):**
- Reconciliación post-offline → `celery-reconciliation`
- Notificación al ERP → `celery-erp-sync`
- Verificación de backups → ejecutado por AWS Backup + CloudWatch (nativo)
- Health check DRP → ejecutado por Aurora Global Database + Route 53 health checks (nativo)

**Configuración Lambda:**
- Reserva de concurrencia configurada para `fn-iot-validator` (función crítica de cadena de frío).
- VPC Lambda para acceso a recursos en subredes privadas.
- Layers compartidos para dependencias comunes (librerías de validación, SDK de KMS).

### 3.3 Gestión de Identidad: Keycloak (IdP Maestro en Nube — Modelo B)

**Keycloak** (open source, licencia Apache 2.0) se despliega como servicio de autenticación y autorización central, con la **autoridad única (maestro) en la nube** conforme al **Modelo B de identidad** (decisión D6 de la Arquitectura Lógica v1; `Tabla_Emplazamiento_OnPremise_v06` §A-05). La decisión de Keycloak sobre Amazon Cognito se fundamenta en:

- **Operación offline completa:** Keycloak soporta login sin internet mediante la **caché local de solo lectura A-05** (VM-05 Talca, VM-C03 Concepción, TTL 8 h) que valida localmente la firma de los tokens emitidos por el maestro en nube — crítico para bodega y preventistas en zona sin señal. Cognito requiere internet para toda autenticación.
- **Sin vendor lock-in:** Keycloak es agnóstico al proveedor cloud. Si la migración de AWS a otro proveedor es necesaria, la identidad no se ve afectada (reversibilidad, Art. 16.3).
- **RBAC nativo con grupos jerárquicos:** Perfiles completos (preventista, conductor, bodeguero, gerente, admin, cliente) con permisos granulares.

**Despliegue híbrido (Modelo B):**

| Instancia | Ubicación | Rol | Configuración |
|---|---|---|---|
| **Keycloak IdP maestro** | **ECS Fargate (cloud, sa-east-1) — autoridad única** | Maestro: todas las escrituras (altas, cambios de rol, políticas, revocaciones). Servicio `id.puelche.cl` | Aurora PostgreSQL (backend del Realm), Realm Puelche, integración LDAP/SCIM con el directorio corporativo del CLIENTE (por VPN outbound) |
| **Caché local A-05** (VM-05 Talca + VM-C03 Concepción) | On-premise (solo lectura, TTL 8 h) | Validación local de firma OIDC y emisión de tokens offline durante cortes de WAN. **No es un segundo IdP**; no admite escrituras | Importa el Realm cifrado publicado por el maestro (S3 outbound); re-sincronización TTL 8 h |

**Flujo de autenticación:**
- **Con internet:** App → Keycloak maestro (nube) → JWT emitido → App lo cachea (TTL por perfil de actor: bodega 8 h; reparto/preventa 14 h)
- **Sin internet:** App → Caché local A-05 (VM-05/VM-C03) → valida la firma del JWT localmente y emite la sesión offline → App continúa con tokens por perfil
- **Sincronización:** Al recuperar internet, **Keycloak maestro (nube)** publica el Realm (export/import cifrado a S3, outbound) y las cachés locales A-05/VM-C03 lo importan (Δ ≤ 8 h, TTL); altas, bajas y roles se propagan desde el maestro hacia las cachés, nunca a la inversa

**Estrategia de tokens (conforme §5.4):**
- id_token con TTL de 1 hora; access_token con TTL de 30 minutos (apps móviles, preventistas, conductores)
- refresh_token con TTL de 30 días para uso recurrente
- Offline login: la **caché local A-05** valida la firma y habilita **tokens offline con TTL por perfil de actor** — **8 h** turno nocturno de bodega (RNF-13.01) y **14 h turno completo de reparto / jornada de preventa** (RNF-06.02) — renovados al inicio de turno en cobertura o contra la caché local en el CD, de modo que la sesión offline siempre cubre la jornada aunque no haya señal hasta el retorno a base; al reconectar, se sincronizan los cambios

**Configuración ECS Fargate (Keycloak maestro):**
- 1 tarea `1 vCPU / 2 GB` en régimen normal
- 2 tareas (Multi-AZ) en peak
- PostgreSQL (Aurora) como backend de persistencia del Realm
- Health check en `/health/ready`

### 3.4 Computación Edge Gestionada desde la Nube (AWS IoT Greengrass v2)

Conforme a la **restricción de exclusividad cloud** del encargo, el diseño se limita a la capa de nube y asume la existencia de una **conexión segura hacia el on-premise** (borde móvil del Puelche: preventistas, conductores, cámaras de congelado y bodegas). El hardware y el dimensionamiento físico de esos dispositivos se trabajan en paralelo (sección on-premise); la nube aporta la **plataforma de gestión y orquestación del borde**:

**AWS IoT Greengrass v2** es la plataforma cloud que gestiona de forma centralizada los dispositivos edge del Puelche (vehículos refrigerados, bodegas, terminales de cámara de congelado). Desde la nube se orquesta:

- **Operación offline completa por ≥ 14 horas** sin pérdida de datos: Greengrass despliega en el dispositivo la aplicación local, el almacenamiento local (SQLite cifrado) y el **Stream Manager** como buffer persistente (entrega at-least-once al reconectar).
- **Fleet Provisioning y administración centralizada de gemelos digitales (device shadow)** vía AWS IoT Core, registrando cada dispositivo (preventista, conductor, terminal de cámara) y su estado.
- **Actualizaciones OTA (Over-The-Air) y nucleos ether** gestionados desde la nube sin intervención en terreno — clave dado que 62 preventistas y ~200 conductores están en la calle de lunes a sábado y no pueden detenerse para actualizaciones.
- **Detección de excursiones de temperatura en el borde** mediante **umbrales y reglas declaradas por configuración** (rangos por tipo de producto, ventanas y tolerancias), desplegadas y versionadas desde la nube vía Greengrass como componente de borde, con alerta en línea y buffer local — **sin modelos de IA/ML** (alineación con la Arquitectura Lógica §17D — RT-18 N/A).
- **Sincronización inteligente** al recuperar señal: prioriza alertas de ruptura de cadena de frío sobre telemetría rutinaria.
- **Certificados X.509 rotativos** gestionados automáticamente desde AWS IoT Core (rotación semestral).

> El hardware edge (procesador, RAM, almacenamiento, conectividad 4G/satélite, terminales Zebra MC9300 a −30 °C y smartphones IP68/MIL-STD-810H) se especifica en la **sección on‑premise paralela**, que es quien dimensiona la infraestructura física de los dispositivos. Este documento solo define los requisitos de interfaz, capacidad de almacenamiento local y protocolos (MQTT/TLS 1.2+) que la nube exige a cada dispositivo para garantizar la operación desconectada de 14h y la reconciliación posterior.

### 3.5 Dimensionamiento de Cómputo Cloud (sizing derivado de la volumetría del Caso)

El dimensionamiento se **deriva de la volumetría real del Caso 02 (Cap. 14.1)** y no de promedios genéricos, dado el **perfil de carga no plano** declarado en el caso (RT-09.02):

- **Preventa** 09:00–18:00 (62 preventistas), **preparación** 22:00–06:00, **despacho** 05:30–07:00 (pico de salida de ~96 camiones), **sincronización de la flota** 17:00–20:00, y **pico de septiembre** que multiplica todo.

**Volumetría base (Cap. 14.1):**
- 14.200 clientes / puntos de entrega; ~62.000 visitas de preventa al mes.
- 31.000 pedidos/mes → **260.000 líneas/mes** → ~1.400 entregas/día normal, hasta ~2.600/día en peak.
- ≈34.000 documentos tributarios emitidos al mes.
- Flota: 42 camiones propios + 54 de transportistas = ~96 camiones saliendo entre 05:30 y 07:00; ~62 preventistas y ~200 conductores en terreno.

| Componente | Base (régimen normal) | Peak septiembre | Criterio de Scaling | Justificación de volumen |
|---|---|---|---|---|
| ECS Fargate Django (tareas `2 vCPU/4 GB`) | 2 tareas | 6 tareas (3×) | CPU >70% | Monolito Django modular; 2 instancias mínimo para Multi-AZ; peak de sync 17:00–20:00 de ~270 dispositivos remotos |
| ECS Fargate Celery workers (tareas `2 vCPU/4 GB`) | 2 tareas | 4 tareas (2×) | Queue depth / CPU | Workers de reconciliación, reportes, alertas y exportación analítica |
| Lambda (`fn-iot-validator`, `fn-document-signer`) | 100 concurrent | 500 concurrent (reserva) | Eventos IoT Core | Validación en tiempo real de lecturas IoT y firma de documentos |
| Aurora PostgreSQL (writer \| reader) | db.r6g.large ×2 AZ | db.r6g.xlarge +2 readers | CPU >60% / Conexiones >80% | OLTP cloud de preventa/reparto/BI + réplica DRP del WMS on-premise (vía DMS CDC); consultas de stock/crédito de 62 preventistas + validación de 260.000 líneas + 31.000 pedidos |
| Serie de tiempo consolidada (temperatura) | S3 Parquet (`s3-analytics-parquet`) + Redshift Serverless | Ídem (5 años) | — | Telemetría de temperatura consolidada (lecturas procesadas); series temporales para BI en la capa OLAP (§4.3) |
| DynamoDB (telemetría IoT cruda) | On-demand | On-demand | On-demand | Solo lecturas crudas de sensores IoT de alta frecuencia; ingesta temporal antes de procesar hacia la capa OLAP (S3) |
| Amazon EventBridge | Serverless | Serverless | Eventos/s | Correlación de ~50.000 lecturas IoT/día con eventos de ruta y alertas |
| ElastiCache Redis | cache.r6g.large | cache.r6g.xlarge | Memory >75% | Caché de stock/crédito para latencia < 2s de consulta en preventa (RT-09.01) |
| Capacidad MQTT IoT Core | ~270 dispositivos | ~300+ | — | Preventistas + conductores + terminales de cámara registrados concurrentemente |
| Keycloak (ECS Fargate) | 1 tarea `1 vCPU/2 GB` | 2 tareas (Multi-AZ) | CPU >60% | IdP **maestro en nube** (autoridad única); A-05/VM-C03 son cachés locales de solo lectura TTL 8 h |

---

## 4. ALMACENAMIENTO Y BASES DE DATOS

### 4.1 Estrategia General de Persistencia

La estrategia de persistencia separa estrictamente las cargas **OLTP (transaccionales)** de las **OLAP (analíticas)**, en cumplimiento del Cap. 5 de las Bases Técnicas Transversales y el Art. 23° de las Bases Administrativas.

```
┌─────────────────────────────────────────────────────────────────┐
│                    CAPA OLTP (Transaccional)                     │
│  Amazon Aurora PostgreSQL    │  Amazon DynamoDB  │  ElastiCache  │
│  (PostGIS)                  │  (IoT raw solo)   │  (caché/sesión)│
└────────────────────────────┬────────────────────────────────────┘
                             │ AWS DMS + CDC + EventBridge
┌────────────────────────────▼────────────────────────────────────┐
│                    CAPA OLAP (Analítica)                         │
│  Amazon S3 (Data Lake)  ──►  Amazon Redshift Serverless          │
│  (raw data, Parquet)         (queries analíticas, dashboards)    │
└─────────────────────────────────────────────────────────────────┘
```

### 4.2 Bases de Datos OLTP

#### Amazon Aurora PostgreSQL (Base de Datos Relacional de la Nube: OLTP cloud + réplica/DRP del WMS)

**Justificación:** El dominio logístico requiere integridad referencial (guías de despacho, órdenes de entrega, clientes, vehículos, productos), transacciones ACID, consultas complejas JOIN, y soporte geoespacial (PostGIS) para rutas y zonas. Aurora PostgreSQL supera a RDS estándar en throughput (hasta 5× más que PostgreSQL vanilla) y ofrece replicación synchronous multi-AZ nativa. La extensión **PostGIS** (consultas geoespaciales de rutas y zonas) se habilita en Aurora; la serie de tiempo consolidada de temperatura vive en la capa OLAP (S3 + Redshift Serverless, §4.3), separando el OLTP del analítico (RNF-11.02).

**Rol híbrido de Aurora (NO es un segundo WMS ni el único "sistema de verdad"):**
- **OLTP en la nube** de los procesos que corren en cloud: preventa (pedidos, validación de crédito), reparto (estado de entregas, POD), metadatos de documentos tributarios y BI operacional.
- **Réplica de continuidad/DRP del WMS on-premise (A-02 en Talca):** el WMS local es el **maestro de la operación de bodega** (recepción, preparación, despacho) con autonomía de 24 h (RT-03.10). Aurora se mantiene al día con **AWS DMS CDC** sobre el WAL lógico del WMS (`wal_level=logical`) vía la VPN y actúa como instancia de recuperación si Talca cae. No duplica en paralelo la operación de bodega ni compite como segundo "sistema de verdad".

**Modelo de Datos Clave:**
- `shipments` — Guías de despacho y estado de entrega
- `vehicles` — Flota de vehículos refrigerados y estado (con geometrías PostGIS para跟踪 GPS)
- `temperature_events` — Registros de temperatura por shipment (serie OLAP en Redshift, derivada del raw)
- `documents` — Metadatos de documentos tributarios (el binario en S3)
- `audit_log` — Tabla append-only de eventos de negocio
- `iot_readings_consolidated` — Lecturas IoT procesadas (Parquet OLAP en S3, retención 5 años)
- `costo_servir` — Tabla analítica pre-calculada del costo de servir por cliente/entrega
- `otif_daily` — Tabla materializada del indicador OTIF diario

**Configuración:**
- **Cluster Multi-AZ:** 1 instancia Writer + 2 Reader en AZs distintas.
- **Aurora Global Database:** Réplica en región us-east-1 para DRP con lag < 1 segundo.
- **RPO compliance:** La réplica sincrónica garantiza RPO ≤ 1 minuto (muy por debajo del límite de 15 minutos exigido).
- **Retention PITR:** 35 días de Point-In-Time Recovery.
- **Cifrado:** AES-256 con claves KMS administradas por el cliente (CMK).
- **Backtrack Aurora:** Permite rewind de la base de datos hasta 72 horas sin restaurar snapshot.
- **Réplica de WMS on-premise vía AWS DMS CDC:** Aurora recibe cambios del PostgreSQL on-prem (A-02, Talca) mediante una tarea continua de **AWS DMS (Database Migration Service) con Change Data Capture**. La tarea DMS se ejecuta en una instancia gestionada dentro de la VPC, conectándose al PostgreSQL on-prem a través de la VPN IPsec (D-01→VGW). Lee el WAL con `wal_level=logical` y aplica los cambios en Aurora de forma continua. Lag declarado < 15 min (RPO ≤ 15 min, Art. 20°). Monitoreo de lag vía métricas CloudWatch de DMS. Si la VPN cae, DMS encola los cambios y los reanuda al recuperar el enlace, sin pérdida de datos.

#### Amazon DynamoDB (Base de Datos NoSQL — Solo IoT Raw)

**Justificación:** La telemetría cruda de temperatura de dispositivos IoT implica escrituras masivas de ultra-baja latencia con patrones key-value (deviceId + timestamp). DynamoDB garantiza latencias de escritura < 10 ms en el percentil 99 independientemente del volumen, es serverless y escala automáticamente durante peaks. **Solo se almacena aquí la lectura cruda de sensores**; una vez validada, se replica a S3 raw (5 años, inmutable) y se consolida en la capa OLAP (S3 Parquet → Redshift) para consultas analíticas.

**Tabla Principal:**
- `iot-temperature-readings` — Lecturas crudas de temperatura en tiempo real. Partition Key: `device_id`, Sort Key: `timestamp`. **Índice secundario global (GSI) por `shipment_id`** para trazabilidad por envío (§7.13, Punto 6). TTL: 30 días (luego de replicar a S3 raw y consolidar en la capa OLAP).

**Tablas eliminadas (migradas a Aurora PostgreSQL):**
- ~~`device-shadow`~~ → tabla `devices` en Aurora (PostGIS, metadatos de dispositivos)
- ~~`route-state`~~ → tabla `vehicle_routes` en Aurora (PostGIS, estado de vehículos)
- ~~`reconciliation-queue-state`~~ → tabla `reconciliation_queue` en Aurora (control de reconciliación)

**Configuración:**
- **DynamoDB Streams:** Habilitado en tablas críticas para procesamiento en tiempo real via Lambda.
- **Global Tables:** Réplica activa en us-east-1 para DRP con consistencia eventual.
- **Point-in-Time Recovery (PITR):** Habilitado para todas las tablas (35 días).
- **On-demand capacity:** Para manejar peaks sin gestión manual de capacidad.
- **Cifrado:** AWS managed KMS keys con opción de CMK.

#### Amazon ElastiCache for Redis (Caché y Sesiones)

- **Propósito:** Caché de respuestas frecuentes, gestión de sesiones de usuario, rate limiting y cola de prioridad para alertas críticas de temperatura.
- **Configuración:** Cluster Mode habilitado, Multi-AZ con réplica por shard.
- **Cifrado:** En tránsito (TLS) y en reposo.

### 4.3 Capa Analítica (OLAP)

#### Amazon S3 — Data Lake Central

**Justificación:** S3 actúa como el repositorio central de todos los datos en bruto, actuando como fuente de verdad inmutable para la capa analítica. Soporta los requerimientos de retención extendida del Caso 02.

**Estructura de Buckets:**

| Bucket | Contenido | Retención | Clase de almacenamiento |
|---|---|---|---|
| `s3-raw-telemetry-iot` | Telemetría de temperatura raw (JSON) | **5 años** (Cap. 15 Caso 02) | S3 Intelligent-Tiering → Glacier Instant |
| `s3-documents-legal` | Documentos tributarios (DTE), guías de despacho electrónicas, facturas | **6 años** (Cap. 15 Caso 02) | S3 Standard → Glacier Deep Archive (año 2+) |
| `s3-backups-encrypted` | Respaldos cifrados de BD (esquema 3-2-1-1-0) | 35 días activo, 1 año Glacier | S3 Standard-IA → Glacier |
| `s3-analytics-parquet` | Datos transformados en Parquet para Redshift | **5 años** (telemetría Caso 02 / RT-05.10) | S3 Standard-IA → Glacier Instant |
| `s3-audit-logs` | CloudTrail, VPC Flow Logs, ALB Access Logs | 7 años (cumplimiento) | S3 Standard-IA → Glacier Deep Archive |
| `s3-artifacts-iac` | Artefactos de CI/CD, templates IaC | Indefinido | S3 Standard |

**Configuraciones Críticas de S3:**
- **Object Lock (WORM):** Activado en `s3-documents-legal` y `s3-audit-logs` para inmutabilidad (Compliance mode, no Governance mode). Resuelve el requerimiento de inmutabilidad de respaldos (Cap. 7 BTT).
- **Versioning:** Habilitado en todos los buckets críticos.
- **Cross-Region Replication (CRR):** Desde sa-east-1 hacia us-east-1 para todos los buckets críticos (contribuye al esquema 3-2-1-1-0).
- **Replication Time Control (S3 RTC):** Garantiza replicación en < 15 minutos (alineado con RPO).
- **Block Public Access:** Habilitado a nivel de organización AWS para todos los buckets.
- **Server-Side Encryption:** SSE-KMS con CMK rotada anualmente.
- **S3 Lifecycle Policies:** Transición automática a clases de menor costo según antigüedad.

#### Amazon Redshift Serverless (Data Warehouse Analítico)

- **Propósito:** Análisis histórico de cadena de frío, reportes de cumplimiento, dashboards de KPIs logísticos y consultas ad-hoc sobre grandes volúmenes de datos.
- **Justificación Serverless:** El patrón analítico del caso es intermitente (reportes periódicos, no consultas 24/7), por lo que Serverless elimina el costo de nodos dedicados ociosos.
- **Fuente de datos:** Carga desde S3 via COPY command y AWS Glue ETL jobs.
- **Separación OLTP/OLAP:** Redshift **nunca** accede directamente a Aurora. El pipeline pasa por S3 como zona de aterrizaje.

#### AWS Glue (ETL Gestionado)

- **Catálogo de Datos:** AWS Glue Data Catalog como metastore central (compatible con Apache Hive).
- **Jobs ETL:** Transformación de datos raw IoT (JSON) a formato columnar (Parquet) para Redshift.
- **Crawlers:** Descubrimiento automático de esquemas en S3.

### 4.4 Almacenamiento de Objetos Adicionales

- **Amazon EFS (Elastic File System):** Para tareas ECS Fargate que requieren almacenamiento compartido de archivos (configuraciones, certificados temporales). Multi-AZ nativo.
- **Amazon ECR (Elastic Container Registry):** Registro privado de imágenes Docker con escaneo de vulnerabilidades automático (ECR Enhanced Scanning con Amazon Inspector).

### 4.5 FinOps y Gestión de Costos (Art. 16.3)

En cumplimiento del Art. 16.3 de las Bases Administrativas, la propuesta incluye un marco de FinOps para el control y optimización de costos en nube:

**Tagging obligatorio:** Todo recurso AWS lleva las siguientes etiquetas (tags):
- `Environment`: Dev | QA | Pre-Prod | Prod
- `Module`: preventa | reparto | bodega | bi | telemetria | ...
- `CostCenter`: operaciones | analitica | integraciones
- `Owner`: equipo-asignado

**Herramientas FinOps:**
| Herramienta | Propósito | Frecuencia |
|---|---|---|
| AWS Cost Explorer | Visualización de costos por servicio, tag y módulo | Diaria (dashboard) |
| AWS Budgets | Presupuestos por ambiente y módulo con alertas automáticas | Continua |
| AWS Cost Anomaly Detection | Detección de anomalías de costos (servicio administrado de AWS; umbrales de desviación configurados) | Continua |
| AWS Trusted Advisor | Recomendaciones de optimización (instancias subutilizadas, reserved capacity) | Semanal |

**Política de alertas de costos:**
- Alerta al 80% del presupuesto mensual (notificación al equipo)
- Alerta al 100% del presupuesto mensual (escalamiento al Jefe de Proyecto)
- Alerta si el costo diario supera 2× el promedio de los últimos 7 días (anomalía)
- Revisión mensual de costos con el cliente (reporte FinOps)

**Optimización de costos:**
- ECS Fargate: escalado automático a cero fuera de horario laboral (Dev/QA), tareas programadas solo nocturnas
- Aurora: reservas de capacidad a 1 año para instancia Writer (ahorro ~30%)
- S3: lifecycle policies automáticas (Intelligent-Tiering → Glacier)
- DynamoDB: on-demand capacity (sin pagar por capacidad ociosa)
- Redshift Serverless: se apaga automáticamente sin consultas activas

**Integración energética y huella de carbono (RT-15.04 / RT-15.05):**
- **Intensidad de carbono de la región (RT-15.04):** la región primaria **sa-east-1** se elige por latencia al cono sur, y su intensidad de carbono por kWh se incorpora a la justificación del diseño (proveedores con compromiso de energía renovable —carbon free energy— en la operación de sus centros de datos). El gasto energético por servicio se informa mediante el **AWS Customer Carbon Footprint Tool** dentro del reporte FinOps mensual (métricas de emisiones por servicio y cuenta).
- **Comparativa entre regiones (RT-15.05):** el informe de carbono contrasta la huella de operar el stack en **sa-east-1** (primaria) frente a **us-east-1** (DRP) y documenta la decisión tomada: se mantiene sa-east-1 como primaria por compromiso de latencia y disponibilidad del caso, y el cálculo de emisiones considera únicamente la réplica de DRP en us-east-1 (escalada bajo demanda, impacto marginal). El on-premise declara su propio factor en el consolidado (PUE 1,7).

### 4.6 Declaración de Reversibilidad (Art. 16.3)

En cumplimiento del Art. 16.3 de las Bases Administrativas, se declara el plan de reversibilidad para migración a otro proveedor si fuera necesario:

**Formatos de exportación garantizados:**
| Tipo de dato | Formato de exportación | Herramienta |
|---|---|---|
| Bases de datos relacionales | PostgreSQL dump (pg_dump) + CSV | pg_dump nativo |
| Series temporales / analítica (S3 Parquet → Redshift) | CSV / Parquet | S3 download / Redshift UNLOAD |
| IoT raw (DynamoDB) | JSON / CSV | AWS DynamoDB Export to S3 |
| Documentos legales (S3) | Original (PDF, XML) | S3 download / sync |
| Datos analíticos (Redshift) | Parquet / CSV / UNLOAD | Redshift UNLOAD |
| Configuración de Keycloak | JSON (Realm export) | Keycloak Admin CLI |
| Configuración de infraestructura | Terraform state + HCL | terraform export |

**Plan de migración (timeline):**
| Fase | Duración | Actividades |
|---|---|---|
| Evaluación | 2 semanas | Inventario de recursos, dependencias, puntos de integración |
| Preparación | 4 semanas | Configurar proveedor destino, migrar BD (DMS), migrar documentos (S3 → destino) |
| Ejecución | 2 semanas | Migración de aplicación (Django container), DNS cutover, validación |
| Post-migración | 2 semanas | Monitoreo, optimización, cierre de cuenta AWS |

**Total estimado: 10 semanas** para migración completa sin pérdida de datos.

**Servicios con alternativas documentadas:**
| Servicio AWS actual | Alternativa proveedor-neutral | Nivel de esfuerzo |
|---|---|---|
| Aurora PostgreSQL | PostgreSQL managed (CockroachDB, AlloyDB, ANY PostgreSQL) | Bajo (estándar SQL) |
| DynamoDB | MongoDB, Cassandra, cualquier NoSQL key-value | Bajo (formato JSON) |
| S3 | Any object storage (MinIO, GCS, Azure Blob) | Bajo (compatible S3 API) |
| Redshift | Snowflake, BigQuery, PostgreSQL + Citus | Medio (reconfigurar ETL) |
| ECS Fargate | Kubernetes (EKS, GKE, AKS), Docker Compose | Medio (reemplazar orquestador) |
| Keycloak | Auth0, Okta, Keycloak managed | Bajo (estándar OIDC) |

---

## 5. SEGURIDAD, IDENTIDAD Y CUMPLIMIENTO

### 5.1 Arquitectura Zero Trust

En cumplimiento del Art. 21° de las Bases Administrativas y Cap. 11 de las Bases Técnicas (RT-11.01, NIST SP 800-207), se implementa Zero Trust en todas las capas:

**Principios implementados:**
1. **Verificar explícitamente:** Toda solicitud se autentica y autoriza, sin importar su origen (red interna o externa).
2. **Mínimo privilegio:** Los roles IAM y las políticas de ECS RBAC otorgan únicamente los permisos estrictamente necesarios.
3. **Asumir la brecha:** Los sistemas están diseñados para contener y detectar intrusiones, no solo prevenirlas.

**Implementación técnica:**
- **ECS Service Connect mTLS:** Toda comunicación entre servicios internos en ECS Fargate está cifrada con TLS mutuo. Las tareas sin certificado válido no pueden comunicarse.
- **AWS PrivateLink:** Los servicios AWS (S3, DynamoDB, SQS, KMS) se consumen a través de VPC Endpoints privados, sin tráfico por internet público.
- **Network Segmentation:** Security Groups como micro-firewalls por instancia + Network ACLs por subred.
- **No hay rutas directas:** Cualquier comunicación cross-VPC pasa por el Transit Gateway con inspección.
- **Acceso remoto Zero Trust para trabajo desde el hogar (RT-03.22):** El acceso de las personas trabajadoras del CLIENTE (trabajo desde el hogar, supervisión en terreno) se resuelve con **AWS Verified Access** para las aplicaciones en nube (portal, BI, back office) —verificación de identidad por Keycloak (OIDC) + postura del dispositivo (device posture check), sin exposición de servicios internos a Internet— y, para los servicios on-premise (WMS de bodega), con **túnel ZTNA de malla (WireGuard/Tailscale o equivalente)** que también valida postura del dispositivo y registra toda sesión. No se abren puertos entrantes ni se publican servicios internos (sin VPN tradicional de acceso completo).

### 5.2 Protección Perimetral

- **AWS WAF v2:** Desplegado frente a CloudFront y ALB. Rulesets activos:
  - AWS Managed Rules: Core rule set (OWASP Top 10), Known bad inputs, SQL injection, XSS.
  - Reglas personalizadas: Rate limiting por IP (protección contra scraping de telemetría), bloqueo geográfico según requerimientos del cliente.
  - Protección de bots con reto progresivo (Challenge/CAPTCHA de AWS WAF) en los puntos de entrada públicos (Art. 21.2).
  - Logging completo hacia S3 + análisis en tiempo real con Amazon Athena.
- **HSTS con precarga:** Los endpoints públicos (CloudFront/ALB/API Gateway) envían la cabecera `Strict-Transport-Security` con `preload` y `includeSubDomains`; TLS 1.3 mínimo, prohibidos TLS 1.0/1.1 (Art. 21.2).
- **AWS Shield Advanced:** Protección DDoS en capas 3, 4 y 7 con soporte 24/7 del equipo DDoS Response Team de AWS y protección de costos durante ataques volumétricos.
- **Amazon CloudFront:** Primera línea de distribución, absorbe tráfico en los edge locations globales antes de llegar a la región.
- **Amazon GuardDuty:** Detección de amenazas administrada de AWS sobre logs de VPC, CloudTrail y DNS. Habilitado en todas las cuentas AWS de la organización.
- **AWS Security Hub:** Consolidación de hallazgos de seguridad de GuardDuty, Inspector, Macie y herramientas de terceros. Panel centralizado de compliance.
- **Amazon Inspector:** Escaneo continuo de vulnerabilidades en instancias EC2, contenedores en ECR y funciones Lambda.
- **Amazon Macie:** Detección automática de PII y datos sensibles en buckets S3 (relevante para datos personales en documentos tributarios).

### 5.3 Gestión de Claves y Cifrado

**AWS Key Management Service (KMS) con Customer Managed Keys (CMK):**

| Recurso | Clave KMS | Rotación |
|---|---|---|
| Aurora PostgreSQL | `cmk-aurora-prod` | Anual automática |
| DynamoDB tablas críticas | `cmk-dynamo-iot` | Anual automática |
| S3 datos legales | `cmk-s3-legal` | Anual automática |
| S3 backups | `cmk-s3-backup` | Anual automática |
| Secrets (contraseñas, tokens) | `cmk-secrets` | Anual automática |
| Greengrass edge certificates | `cmk-iot-edge` | Rotación semestral |

**AWS CloudHSM (opcional, recomendado para mayor exigencia):** Para operaciones criptográficas que requieren módulos hardware dedicados (firma de documentos tributarios, si así lo exige la normativa específica).

**AWS Certificate Manager (ACM):** Gestión automatizada de certificados TLS para ALB, CloudFront y API Gateway. Renovación automática sin intervención manual.

**AWS Secrets Manager:** Almacenamiento y rotación automática de credenciales de bases de datos, API keys de terceros y tokens de integración. Django obtiene credenciales en tiempo de ejecución via SDK, nunca hardcodeadas.

**Cifrado en tránsito:**
- TLS 1.3 mínimo en todos los endpoints públicos.
- mTLS en comunicación interna entre servicios ECS Fargate.
- TLS en conexiones a bases de datos (forced SSL en Aurora y DynamoDB).
- MQTT over TLS 1.2+ en AWS IoT Core.

**Cifrado en reposo:**
- AES-256 en Aurora, DynamoDB, S3, EBS, EFS, ElastiCache.
- **Cifrado adicional a nivel de campo (RT-11.10):** Los datos de categoría sensible que el caso identifica (RUT, geolocalización de entregas, evidencia POD/DTE) se cifran **adicionalmente a nivel de columna/campo** con AES-256 (pgcrypto/LUKS por clave de aplicación en Aurora y envoltura de claves por datos vía KMS), de modo que acceder a la base de datos no revele su contenido. Instrumentación declarada por modelo, con claves por tenant/campo y rotación anual.

### 5.4 Gestión de Identidades y Accesos (IAM)

En cumplimiento del Art. 22° de las Bases Administrativas y Cap. 12 de las Bases Técnicas:

**Keycloak (IdP Maestro — Open Source):**
- **Despliegue híbrido (Modelo B):** **Keycloak IdP maestro en ECS Fargate (cloud, sa-east-1)** es la **autoridad única de identidad** (todas las escrituras: altas, cambios de rol, políticas, revocaciones; backend Aurora). Los componentes on-premise **A-05 en VM-05 Talca y VM-C03 Concepción son cachés locales de solo lectura (TTL 8 h)** que validan la firma de los tokens offline durante cortes de WAN; **no existe un maestro on-premise ni promoción local a escritura**.
- **Realm Puelche:** Configuración centralizada con dominio `puelche.cl`. Soporte para OIDC, SAML 2.0, y entidades federadas. **Integración con el directorio corporativo del CLIENTE por LDAP (RT-12.01):** el Realm se sincroniza con el directorio del CLIENTE (alta, cambio de rol y baja de personas), de modo que la gestión de identidad sea centralizada y la federación OIDC/OAuth 2.1 sea la única vía de autenticación de todos los módulos.
- **SSO y cierre de sesión único (RT-12.02):** Todos los módulos de la solución (portal, WMS/back office, BI, Keycloak Admin) se autentican mediante inicio de sesión único basado en OIDC sobre el mismo Realm; el cierre de sesión se propaga a todos los módulos (OIDC back-channel logout) y la revocación de la credencial de sesión invalida de forma inmediata las sesiones emitidas, tanto en la nube como en la caché on-premise.
- **Grupos y Roles RBAC:**
  - `admin` — Administrador del sistema (configuración global, usuarios)
  - `gerente` — Gerente Comercial / Finanzas (tableros, reportes, aprobaciones)
  - `jefe_bodega` — Jefe de Bodega (WMS, inventario, picking)
  - `bodeguero` — Operador de bodega (picking, recepción, solo on-premise)
  - `preventista` — Preventista (toma de pedidos, catálogo, solo mobile)
  - `conductor` — Conductor (POD, reparto, solo mobile)
  - `calidad` — Jefa de Calidad (trazabilidad, excursiones, reportes)
  - `cliente` — Cliente del portal (tableros de negocio, estado de cuenta)
- **MFA:** Obligatorio para roles admin y gerente, y para **todo acceso desde fuera de la red corporativa** (Art. 22°): portales de clientes, transportistas y proveedores con TOTP (Google Authenticator) o SMS; preventistas/conductores en terreno con **factor de posesión + PIN de 6 dígitos** (uso con guantes, una mano) — el PIN opera como segundo factor sobre la sesión del dispositivo autenticado, no como factor único. Dispositivos edge autenticados con certificados X.509 únicos.
- **Control de acceso (RT-12.05):** RBAC por grupos/roles de Keycloak (§5.4) complementado con **ABAC** donde el proceso lo exige (reglas de negocio según atributos de lote, temperatura o geocerca sobre las políticas del orquestador). Se documenta una **matriz de segregación de funciones** para las operaciones que combinan dos roles (crear/contabilizar pedido, rendición/entrega), haciendo inviable que un mismo actor ejecute ambos extremos.
- **Tokens JWT (RT-12.08):** id_token (1h), access_token (30 min), refresh_token (30 días). Los JWT son firmados (`RS256`) y de vida breve, con credencial de refresco rotatoria; se prohíbe el transporte de identificadores de sesión en la ruta de la URL, usando exclusivamente cabecera `Authorization` o cookie httpOnly `__Secure-`. Para apps móviles offline: refresh_token con TTL extendido (30 días) permite reconexión sin login completo.
- **Offline login (on-premise):** la **caché local A-05 (VM-05) y VM-C03 (Concepción)** validan localmente la firma de los tokens emitidos por Keycloak maestro (nube) y emiten sesiones/tokens offline según el perfil de actor (§3.3). Al recuperar internet, el **maestro en nube** publica el Realm cifrado (export/import a S3, outbound) y las cachés lo importan (Δ ≤ 8 h, TTL); las altas/bajas y roles se propagan desde la nube hacia las cachés, **sin conexiones entrantes a Keycloak**.
- **Usuarios externos del CLIENTE (RT-12.12):** Los clientes del portal disponen de **registro autoservido** (Alta con verificación por correo/celular OTP y validación de empresa), **verificación de identidad** por flujo Keycloak CIS y **recuperación de acceso autoservida y segura** (reset con OTP/vínculo temporal firmado), sin exponer servicios internos y con las políticas de contraseña de la política de sesión (RT-12.07).

**AWS IAM (Identity and Access Management):**
- **Roles IAM para servicios:** Cada tarea ECS Fargate tiene un IAM Role dedicado via ECS Task Roles. No se usan credenciales de larga duración en contenedores.
- **IAM Identity Center (SSO):** Para acceso de desarrolladores y administradores a la consola AWS con MFA obligatorio y federation con el directorio corporativo.
- **IAM Permission Boundaries:** Límites máximos de permisos para roles creados por pipelines de CI/CD, previniendo escalación de privilegios.
- **AWS Organizations SCPs (Service Control Policies):** Políticas preventivas a nivel organizacional que restringen acciones críticas (ej: deshabilitar CloudTrail, eliminar backups, cambiar configuraciones de seguridad).

**Autenticación Multi-Factor (MFA):**
- Obligatoria para acceso a consola AWS en todas las cuentas.
- Obligatoria para roles admin/gerente en Keycloak y para **todo acceso desde fuera de la red corporativa** (Art. 22°).
- Dispositivos edge autenticados mediante certificados X.509 + registro en AWS IoT Core.
- **Factores resistentes a suplantación (RT-12.04):** Los perfiles administradores podrán autenticarse con **FIDO2/WebAuthn (claves de acceso/passkeys)** además del TOTP, mediante el authenticator WebAuthn de Keycloak; se ofrece como factor preferente para admins, cumpliendo y superando el mínimo exigido (Deseable).

**Política de sesión (RT-12.07):**
- **Duración máxima** por perfil: sesión web 8 h (turno administración) y sesión móvil 14 h (turno de terreno, coherente con RT-03.10); sesión activa con renovación de la credencial de sesión tras la autenticación.
- **Caducidad por inactividad:** 15 min en back office, 30 min en portal; el dispositivo móvil de terreno conserva la sesión durante el turno (contexto offline autorizado).
- **Revocación inmediata:** el logout/cierre de sesión y la revocación de la credencial de refresco invalidan las sesiones emitidas de forma inmediata (IDP session + back-channel).
- **Control de sesiones concurrentes:** una sesión activa por actor en terreno; se deniega login concurrente del mismo preventista/conductor en otro dispositivo (opción de invalidar la anterior).

### 5.5 Auditoría y Cumplimiento Normativo

- **AWS CloudTrail:** Habilitado en modo Organization Trail para todas las cuentas. Logs inmutables en S3 con Object Lock. Log File Integrity Validation habilitado.
- **AWS Config:** Evaluación continua del cumplimiento de configuraciones vs. reglas definidas. Reglas para: MFA habilitada, cifrado activado, acceso público S3 bloqueado, VPC Flow Logs habilitados, etc.
- **VPC Flow Logs:** Captura de todo el tráfico de red para análisis forense y detección de anomalías.
- **Amazon CloudWatch Logs:** Centralización de logs de aplicación y sistema. Retención configurada según política (**mínimo 12 meses en línea** y 24 meses adicionales en archivo recuperable en S3, cumpliendo el Art. 21.3; los logs de auditoría se conservan 7 años en S3 con Object Lock).
- **SIEM con casos de uso de negocio:** Amazon Security Lake consolida CloudTrail, VPC Flow Logs, GuardDuty, DNS y logs de seguridad on-premise (vía ADOT) en un lago central; la correlación se hace sobre casos de uso definidos para el proceso del caso (quiebres de cadena de frío con intentos de acceso anómalos, manipulación de evidencia de POD/DTE, accesos fuera de horario de bodega, escalamiento de privilegios en Keycloak, rendición de caja con acceso simultáneo) y no sólo sobre genéricos de infraestructura (Art. 21.3).
- **AWS Audit Manager:** Framework de auditoría para cumplimiento con normativas (ISO 27001, SOC 2, regulaciones chilenas).
- **Auditoría del ciclo de vida de la identidad (RT-12.09):** CloudTrail, los eventos de auditoría de Keycloak (creación, modificación, elevación, bloqueo y baja de identidades) y el registro local on-premise de sesiones se integran al lago de seguridad (RT-11.14), con bitácora de **no repudio** (firma hash encadenada en cadena) y retención declarada: 12 meses en línea + 24 meses en archivo recuperable, garantizando la trazabilidad íntegra de cada identidad (RT-12.01, RT-12.02).
- **Cuenta de acceso de emergencia (RT-12.13):** Cuenta de último recurso con **custodia compartida** (credencial fraccionada, tipo split-knowledge, junto al Jefe de TI del CLIENTE), **control** mediante rotación posterior a cada uso y **auditoría** completa: cada activación requiere ticket de incidente, se ejecuta por Session Manager/consola con grabación, dispara alarma SIEM, y se revisa y se revoca en el turno siguiente. Declarada y probada en el ejercicio DRP semestral (RT-07.07).
- **RCA de incidentes críticos (RT-14.06):** Todo incidente crítico genera un **análisis de causa raíz con informe entregable ≤ 5 días hábiles** (p. ej., quiebre de cadena de frío, caída de la transacción e2e) y **seguimiento de las acciones correctivas hasta su cierre** en el tablero de gestión del servicio, coherente con el libro de operación (RT-14.05).

### 5.6 Declaraciones de Cumplimiento Específicas (RT-11.06, RT-11.08, RT-11.09, RT-11.13, RT-11.22, RT-11.23, RT-11.24, RT-11.25, RT-11.27, RT-12.06)

Acreditación uno a uno de los requerimientos obligatorios de los Cap. 11 y 12 de las Bases Técnicas que requieren declaración explícita en esta sección:

**RT-11.06 — ISO/IEC 27017 y 27018 (servicios y datos personales en nube):** AWS opera los programas de conformidad ISO/IEC 27017 (guía de controles de seguridad para servicios en nube) e ISO/IEC 27018 (protección de datos personales en nube), verificables en AWS Artifact durante toda la vigencia del contrato. La solución declara la aplicación de los controles de cliente de ambas normas: inventario y flujo de datos personales tratados (RUT, geolocalización), cláusulas de procesador de datos, derecho de supresión mediante la retención documentada (§7.12) y notificación de brechas en los plazos del Art. 21.4 de las Bases Administrativas.

**RT-11.08 — TLS 1.3, HSTS con precarga y gestión automatizada de certificados:** Los endpoints públicos (CloudFront, ALB, API Gateway) usan TLS 1.3 mínimo, con prohibición expresa de TLS 1.0/1.1 (§5.1) y HSTS con `preload` e `includeSubDomains` (§5.2). La emisión y renovación de certificados es automatizada con AWS Certificate Manager (ACM, §5.3): renovación previa al vencimiento sin intervención manual y alarma CloudWatch de **anticipación ≥ 30 días antes del vencimiento**, con escalamiento al equipo de operación. Conjuntos de cifrado modernos (ECDHE + GCM) configurados como política por defecto.

**RT-11.09 — Cifrado en reposo con separación de funciones en la custodia de claves:** Todos los datos en reposo se cifran AES-256 con Customer Managed Keys (§5.3). La custodia de claves aplica **separación de funciones (dual control)**: roles IAM distintos para *administración* (crear, rotar, destruir CMK; MFA obligatoria) y para *uso* (consumir la clave solo vía KMS Grants), sin que un mismo rol combine ambas facultades. La rotación anual automática está declarada por cada CMK y CloudTrail audita toda operación de clave. CloudHSM queda disponible para las firmas criptográficas de mayor exigencia (documentos tributarios).

**RT-11.13 — Superficie de exposición declarada (dominios, puertos y servicios alcanzables desde fuera de la red del CLIENTE):**

| Superficie | Servicio | Protocolo / Puerto | Autenticación |
|---|---|---|---|
| `www.puelche.cl` | Portal web (CloudFront → ALB → Django/ECS) | HTTPS 443, TLS 1.3 | Keycloak OIDC + MFA |
| `id.puelche.cl` | Keycloak (emisión OIDC/OAuth 2.1) | HTTPS 443 | OIDC / SAML 2.0 |
| `api.puelche.cl` | API Gateway (REST / sincronización) | HTTPS 443 | OIDC + API keys |
| `mqtt.puelche.cl` | NLB → AWS IoT Core (telemetría de bordes) | MQTT over TLS 8883 | mTLS — certificado X.509 por dispositivo |
| CDN | CloudFront edge locations (distribución global) | HTTPS 443 | — |
| Site-to-Site VPN | AWS VPN endpoint (IPsec/IKEv2 hacia on-premise) | IPsec, UDP 500/4500 | Pre-shared key + BGP |
| Direct Connect | Enlace dedicado a on-premise | Private VIF (no expuesto) | IAM |
| VPC Endpoints | PrivateLink (S3, SQS, DynamoDB, KMS) | Intranet VPC | IAM |

*Los CNAME públicos se materializan en el diseño detallado con los registros Route 53 correspondientes; la tabla es la declaración de superficie exigida por el RT-11.13.*

**RT-11.22 — Análisis de seguridad en el pipeline:** El flujo CI/CD (§7.6) incorpora análisis estático (SAST, p.ej. SonarQube/Amazon CodeGuru), análisis de composición de software (SCA de dependencias), análisis dinámico (DAST, p.ej. OWASP ZAP sobre ambientes de prueba) y escaneo de imágenes de contenedor (Amazon Inspector). Los hallazgos **críticos o altos bloquean automáticamente el despliegue** (gate en CodeBuild), en línea con los plazos de remediación del RT-11.04.

**RT-11.23 — SBOM por versión:** Cada versión liberada publica su inventario de componentes de software en **CycloneDX** (generado en el pipeline, p.ej. Syft/Trivy) y se **entrega al CLIENTE** junto con la versión correspondiente.

**RT-11.24 — Firmado de artefactos y SLSA nivel 3:** Las imágenes OCI y el SBOM se firman con **Sigstore/cosign**; la construcción corre en un pipeline **hermético** de CodeBuild con *provenance* **SLSA nivel 3**, y la procedencia de los artefactos se verifica antes de cada despliegue.

**RT-11.25 — Prohibición de datos productivos reales en ambientes no productivos:** Dev, QA y PreProd operan exclusivamente con **datos sintéticos** generados desde el esquema (catálogo, pedidos y documentos simulados según la volumetría del Cap. 14 del caso) o, cuando se requieren plantillas próximas a producción, con **anonimización/seudonimización verificable** (máscara de RUT, nombres y geolocalización). La verificación de ausencia de PII en `staging` se automatiza con **Amazon Macie** sobre los buckets de ambientes no productivos (§5.2).

**RT-11.27 — Sin acceso interactivo directo a producción:** No se entregan credenciales SSH ni consolas directas a los ambientes productivos; los despliegues son exclusivamente por pipeline (§7.6). El acceso de administración excepcional se otorga **just-in-time** mediante **AWS Systems Manager Session Manager**, con aprobación previa, MFA obligatoria, sesión registrada y grabada (integración con la retención del RT-11.14) y auditoría CloudTrail de la sesión.

**RT-12.06 — Gestión de acceso privilegiado (PAM):** La elevación a roles privilegiados (consola AWS, DBA de Aurora, administración de Keycloak/IAM) es **temporal y bajo demanda**: un *permission set* en **IAM Identity Center** se solicita con aprobación previa del Jefe de Proyecto y vence en un plazo máximo declarado (≤ 24 h); no existen permisos administrativos permanentes de amplio alcance. Las operaciones de mayor riesgo (modificación de políticas IAM/SCP, bóveda de claves, DBA productivo) se ejecutan por **Systems Manager Session Manager** con **grabación de sesión**, aprobación y *break-glass* auditado (RT-12.13).

---

## 6. ALTA DISPONIBILIDAD (HA) Y DRP

### 6.1 Estrategia de Alta Disponibilidad

La arquitectura garantiza disponibilidad **≥ 99.9%** (SLA objetivo) mediante los siguientes patrones:

> **Clasificación de servicios (RT-10.02):** cada servicio se clasifica en **crítico, alto, medio o bajo** con su nivel de servicio del Art. 78°, justificado por el impacto operacional de su indisponibilidad:
>
> | Servicio | Clase | Justificación | Nivel de servicio (Art. 78) |
> |---|---|---|---|
> | Transacción de terreno e2e (pedido→entrega→POD) | **Crítico** | Detiene preventa, reparto y facturación; pérdida OTIF | ≥ 99.9 % |
> | Portal de clientes (stock, crédito, estado de cuenta) | **Alto** | Ingresos del canal moderno; visible al cliente | ≥ 99 % (clase alta) |
> | WMS on-premise (picking/recepción) | **Crítico** | Parada total de bodega sin contingencia (Ventana 22:00–06:00) | ≥ 99.9 % (e2e local) |
> | BI/analítica | **Medio** | Reportes diferibles; no detiene la operación | Clase media |
> | Telemetría IoT (temperatura en línea) | **Alto** | Trazabilidad de cadena de frío (acumulable sin alerta inmediata) | ≥ 99 % |
> | Notificaciones/email/push | **Bajo** | Menor impacto; disponible en colas | Clase baja |
>
> Esta clasificación se aplica a las alarmas y al bucket de error budget de cada servicio (RT-10.02).

**Multi-AZ en todos los componentes críticos:**

| Componente | AZ primaria | AZ secundaria | Failover automático |
|---|---|---|---|
| Aurora PostgreSQL | sa-east-1a (Writer) | sa-east-1b (Reader/Failover) | < 30 segundos |
| DynamoDB | Multi-AZ nativo | — | Transparente |
| Amazon EventBridge | 3 brokers en 3 AZs | — | Reelección de líder |
| ECS Fargate Nodes | sa-east-1a | sa-east-1b | AWS Application Auto Scaling re-scheduling |
| ElastiCache Redis | sa-east-1a (Primary) | sa-east-1b (Replica) | < 60 segundos |
| ALB | sa-east-1a | sa-east-1b | Transparente |
| NAT Gateway | sa-east-1a | sa-east-1b (independiente) | Routing automático |

**Patrones de resiliencia en aplicación:**
- **Retry con Exponential Backoff:** En todas las llamadas a servicios externos (API Gateway, S3, Aurora).
- **Timeout agresivo:** Cada llamada tiene timeout definido para evitar bloqueos.
- **Dead Letter Queues (DLQ):** En todas las colas SQS para mensajes no procesados.
- **Idempotency Keys:** En todas las operaciones de escritura de Django para garantizar idempotencia durante reconciliación.
- **Connection Pooling:** Django database connection pooling (PgBouncer) para manejo eficiente de conexiones a Aurora.

### 6.2 Estrategia de DRP (Disaster Recovery Plan)

**En cumplimiento del Art. 20° de Bases Administrativas y Cap. 7 de BTT:**

**Objetivos:**
- **RTO ≤ 4 horas** (tiempo máximo para restaurar el servicio completo)
- **RPO ≤ 15 minutos** (pérdida máxima aceptable de datos)

**Estrategia: Warm Standby (Activo/Pasivo Tibio)**

Esta estrategia balancea costo y capacidad de recuperación. La región secundaria (us-east-1) mantiene una réplica reducida pero completamente funcional del stack productivo, escalable en < 30 minutos para absorber la carga completa.

```
REGIÓN PRIMARIA (sa-east-1)           REGIÓN SECUNDARIA (us-east-1)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ECS Fargate Cluster (Prod) — ACTIVO           ECS Fargate Cluster (DRP) — STANDBY
Aurora PostgreSQL — WRITER            Aurora Global DB — READER → PROMOTED
DynamoDB — Global Tables activo       DynamoDB — Global Tables réplica
EventBridge + SQS — Producción                EventBridge + SQS — Standby (reducido)
S3 — Primary                         S3 — Réplica CRR (S3 RTC < 15 min)
Route 53 — Apuntando a sa-east-1      Route 53 — Health check monitoreando
```

**Procedimiento de Failover:**

1. **Detección automática (0-5 min):** Route 53 health checks detectan falla en región primaria.
2. **Notificación (5 min):** Amazon SNS + PagerDuty alertan al equipo de operaciones.
3. **Decisión y autorización (5-15 min):** Equipo de arquitectura valida y autoriza failover.
4. **Promoción Aurora (15-20 min):** Aurora Global Database promueve réplica en us-east-1 a Writer. El lag típico es < 1 segundo, garantizando RPO << 15 min.
5. **Escalado ECS Fargate DRP (20-45 min):** AWS Application Auto Scaling escala el cluster de standby a capacidad productiva.
6. **Actualización DNS (45-60 min):** Route 53 redirige tráfico a us-east-1.
7. **Validación funcional (60-120 min):** Health checks de aplicación y smoke tests automatizados.
8. **Comunicación (120-240 min):** Notificación formal a usuarios. **Total: < 4 horas = RTO cumplido.**

**RPO Técnico Garantizado:**
- Aurora Global Database: lag < 1 segundo → RPO real < 1 minuto.
- S3 CRR con RTC: replicación garantizada < 15 minutos → RPO S3 cumplido.
- DynamoDB Global Tables: replicación < 1 segundo → RPO DynamoDB < 1 minuto.
- EventBridge + SQS: los eventos y mensajes no consumidos en la región primaria se recuperan via S3 backup (diario) y reconstrucción del state desde Aurora. **RPO declarado: ≤ 24 horas** (pérdida máxima equivalente al último backup diario de AWS Backup). Para mensajes de alta criticidad (alertas de cadena de frío, fallos de-componentes), se aplica patrón **outbox dual-write**: el módulo Django escribe el evento tanto en Aurora (transacción ACID) como en EventBridge; en escenario de DRP, se reconstruyen los eventos no procesados desde la tabla `audit_log` de Aurora. Esto reduce el RPO efectivo de estos mensajes críticos a ≤ 15 min (consistente con el RPO de Aurora).

**Emplazamiento y análisis de amenazas comunes (RT-07.02):**
- **Distancia declarada:** sa-east-1 (São Paulo) → us-east-1 (N. Virginia), ≈ 7.700 km entre regiones y ≈ 8.500 km desde el sitio primario (Talca).
- **Análisis de amenazas comunes:** la región secundaria no comparte red eléctrica, zona sísmica ni ciclones con Sudamérica, y sus perfiles de riesgo difieren (sismo/tsunami en la costa de Chile vs. tormentas/heladas en la costa este de EE.UU.); se documentan como escenarios independientes y se excluye de la hipótesis de falla simultánea por un mismo evento de fuerza mayor (el caso de fallo de un partner/a (AWS) como proveedor común se cubre con el plan de reversibilidad RT-03.07).

**Retorno al sitio principal y reconciliación (RT-07.06):**
- Procedimiento de **retorno (failback)** documentado: (1) re-sincronización de datos us-east-1→sa-east-1 con catch-up de replicación verificado; (2) **reconciliación de las transacciones generadas durante la contingencia** contra la bitácora de decisiones (RT-03.12); (3) transferencia de los eventos SQS/EventBridge pendientes; (4) conmutación manual coordinada de DNS (Route 53) y promoción de Aurora; (5) validación funcional y ventana de observación; (6) informe de retorno con tiempo real alcanzado. Probado en el ejercicio DRP semestral junto con el failover (RT-07.07).

**Automatización de la conmutación (RT-07.08):**
- La decisión de failover es manual con criterio de disparo declarado (health check de región primaria en < 5 min), con **protección contra conmutación innecesaria** (alto confirmado por SNS y procedimiento de autorización). Los pasos 4-7 del procedimiento están **automatizados mediante AWS Systems Manager Automation** (promoción de Aurora, escalado ECS, actualización de DNS), dejando la intervención humana solo en la decisión y la validación, lo que reduce la ventana de conmutación nominal y mitiga la limitación L-05.

### 6.3 Esquema de Respaldos 3-2-1-1-0

**En cumplimiento del Art. 20° de Bases Administrativas:**

> **Esquema único 3-2-1-1-0 declarado en el consolidado híbrido:** El esquema es **uno solo** para toda la arquitectura (nube + on-premise). La pierna **"1 inmutable" vive en la nube (S3 Object Lock + Backup Vault Lock)**, que es la fuente de inmutabilidad definitiva. El NAS/appliance on-premise (D-05) es la **copia local de recuperación rápida** y **NO cuenta como la pierna inmutable**; puede reforzarse con WORM local, pero no se declara como la inmutable del esquema.

| Regla | Implementación (unificada nube + on-premise) |
|---|---|
| **3 copias** de los datos | (1) Datos activos sa-east-1 + WMS activo Talca, (2) Snapshot automático Aurora + respaldo local on-premise (D-05), (3) Backup exportado a S3 |
| **2 medios** diferentes | (1) Almacenamiento de BD (Aurora storage / PostgreSQL on-prem), (2) Amazon S3 (Object Storage) |
| **1 copia offsite** | S3 Cross-Region Replication → bucket en us-east-1 |
| **1 copia offline/inmutable** | **S3 Object Lock (WORM, Compliance Mode) + AWS Backup con vault lock** (ni el root las elimina). El NAS WORM on-premise (D-05) es copia local de recuperación rápida, no la pierna inmutable |
| **0 errores** verificados | AWS Backup con restore testing automatizado mensual via Lambda + verificación de restauración local. Alertas si verificación falla |

**AWS Backup — Plan de Respaldo:**

| Recurso | Frecuencia | Retención | Destino |
|---|---|---|---|
| Aurora PostgreSQL | Diario + continuo PITR | 35 días | AWS Backup Vault (cifrado CMK) |
| DynamoDB | Diario (On-Demand Backup) | 35 días | AWS Backup Vault |
| EFS | Diario | 30 días | AWS Backup Vault |
| EBS Volumes | Diario (snapshots) | 14 días | AWS Backup Vault |
| S3 documentos legales | Continuo (versioning + Object Lock) | 6 años | S3 mismo bucket + réplica CRR |
| S3 telemetría IoT | Continuo (versioning) | 5 años | S3 mismo bucket + réplica CRR |

**AWS Backup Vault Lock:** El vault de producción tiene un vault lock con un período de enfriamiento (cool-off) de 3 días y retención mínima de 1 año. Una vez bloqueado, ni el root account puede eliminar respaldos.

### 6.4 Observabilidad y Monitoreo

- **Amazon CloudWatch:** Métricas, logs y alarmas para todos los servicios AWS. Dashboards personalizados por dominio funcional.
- **AWS X-Ray / AWS Distro for OpenTelemetry (ADOT):** Trazabilidad distribuida de requests a través de módulos Django.
- **Grafana autogestionado (Grafana OSS en ECS Fargate):** Dashboards operacionales y de negocio (temperatura en tiempo real, estado de flota, KPIs logísticos). *Nota de disponibilidad regional:* **Amazon Managed Grafana NO está disponible en la región sa-east-1 (Brasil)**; por ello se despliega **Grafana OSS autogestionado** sobre ECS Fargate dentro del VPC, conectado a **Amazon Managed Prometheus** (que sí está en sa-east-1) vía datasource remoto. Es coherente con la restricción RT-03.05 de preferir servicios administrados, sin perder la vista unificada de observabilidad (RF-16.01). **Acceso del CLIENTE (RT-14.02):** el CLIENTE dispone de cuentas federadas (Keycloak OIDC) con acceso propio y permanente a los tableros, datos en tiempo real (temperatura, flota, OTIF) y **capacidad de exportación** (CSV/PNG) para su operación y auditoría.
- **Amazon Managed Prometheus:** Scraping de métricas de ECS Fargate (ECS task metrics, service metrics).
- **Amazon SNS + PagerDuty:** Notificaciones y escalamiento de alertas críticas (ruptura de cadena de frío, fallos de componentes, aproximación a RTO).

---

## 7. MATRIZ DE JUSTIFICACIÓN ARQUITECTÓNICA EXHAUSTIVA

> Esta matriz actúa como checklist de cumplimiento absoluto. Cada fila mapea un requerimiento específico de los documentos base al componente cloud que lo resuelve y su justificación técnica.

### 7.1 Bases Administrativas — Artículo 16°

| Documento y Artículo | Requerimiento / Restricción | Componente Cloud | Justificación Técnica |
|---|---|---|---|
| BA — Art. 16° | Mandato de arquitectura cloud | AWS como proveedor primario | Se adopta AWS como nube pública principal, con todos los servicios de cómputo, almacenamiento y red desplegados exclusivamente en cloud, eliminando infraestructura propia. |
| BA — Art. 16.3 | Nube pública obligatoria | AWS (sa-east-1 primaria) | AWS es un proveedor de nube pública certificado (ISO 27001, SOC 2, CSA STAR). No se utiliza infraestructura privada ni colocation para los servicios cloud. |
| BA — Art. 16.3 | Multi-zona (multi-AZ) | ECS Fargate Multi-AZ + Aurora Multi-AZ + DynamoDB Multi-AZ | Todos los componentes críticos se despliegan en al menos 2 Zonas de Disponibilidad dentro de sa-east-1 (sa-east-1a y sa-east-1b como mínimo). Failover automático garantizado. |
| BA — Art. 16.3 | Segmentación de red | VPC con subredes pública/privada/datos + Security Groups + NACLs | Tres capas de red aisladas: DMZ pública, subredes privadas de aplicación y subredes privadas de datos. El tráfico entre capas está controlado por Security Groups y NACLs. |
| BA — Art. 16.3 | IAM (gestión de identidades y accesos) | AWS IAM + ECS Task Roles + Keycloak + IAM Identity Center | Usuarios humanos autenticados con Keycloak (IdP maestro, open source). Servicios con roles IAM temporales. Keycloak RBAC con grupos por perfil (preventista, conductor, bodeguero, gerente, admin, cliente). Principio de mínimo privilegio en todas las políticas. |
| BA — Art. 16.3 | Servicios administrados | Aurora, DynamoDB, EventBridge, ECS Fargate managed, Lambda, ElastiCache | Preferencia absoluta por servicios fully-managed de AWS. No se gestionan instancias de bases de datos, EventBridge ni ECS de forma manual. |

### 7.2 Bases Administrativas — Artículo 20° (Continuidad y Recuperación)

| Documento y Artículo | Requerimiento / Restricción | Componente Cloud | Justificación Técnica |
|---|---|---|---|
| BA — Art. 20° | RTO ≤ 4 horas | Warm Standby DRP + Route 53 Failover + ECS Fargate AWS Application Auto Scaling | El proceso de failover documentado (detección 5 min + promoción Aurora 5 min + escalado ECS Fargate 25 min + DNS 15 min + validación 60 min) totaliza < 2 horas en condiciones normales, con margen hasta 4 horas. |
| BA — Art. 20° | RPO ≤ 15 minutos | Aurora Global DB (lag < 1s) + S3 RTC (< 15 min) + DynamoDB Global Tables | Aurora Global Database replica de forma síncrona con lag típico < 1 segundo. S3 Replication Time Control garantiza replicación < 15 minutos. El RPO real alcanzado es < 1 minuto para BD. |
| BA — Art. 20° | Esquema de respaldos 3-2-1-1-0 | AWS Backup + S3 Object Lock + S3 CRR + Aurora PITR + NAS on-prem (D-05) | Esquema **único** nube+on-premise (ver Sección 6.3): (3 copias) activo + snapshot + S3 backup + respaldo local; (2 medios) BD storage y S3; (1 offsite) CRR a us-east-1; (1 inmutable) S3 Object Lock WORM + Backup Vault Lock (el NAS WORM on-prem es copia local de recuperación rápida, no la inmutable); (0 errores) Lambda de verify-restore mensual. |
| BA — Art. 20° | Respaldos con verificación de integridad | AWS Backup + CloudWatch Alarms + tarea Celery de verificación | AWS Backup nativo, con verificación automatizada de restauración programada (restore testing) y alertas CloudWatch si la verificación falla. Integridad de respaldos auditada en AWS Audit Manager. |

### 7.3 Bases Administrativas — Artículos 21° al 24°

| Documento y Artículo | Requerimiento / Restricción | Componente Cloud | Justificación Técnica |
|---|---|---|---|
| BA — Art. 21° | Arquitectura Zero Trust | ECS Service Connect mTLS + AWS PrivateLink + Security Groups + IAM (deny-all default) | Ningún componente confía en otro implícitamente. Toda comunicación requiere certificado mTLS válido. Los servicios AWS se consumen vía VPC Endpoints privados. IAM default deny con allows explícitos. |
| BA — Art. 22° | Gestión de identidades y accesos | Keycloak (IdP maestro abierto, open source) + AWS IAM ECS Task Roles (servicios) + MFA obligatorio + **caché local A-05 on-premise (login offline)** | Usuarios humanos autenticados con Keycloak OIDC + MFA TOTP. **Keycloak (maestro en nube) es la única autoridad de identidad**; la caché local A-05 (VM-05/VM-C03, solo lectura, TTL 8 h) permite login offline sin ser un segundo IdP. Servicios cloud autenticados con roles IAM temporales sin credenciales de larga duración. |
| BA — Art. 22° | Autenticación multifactor (MFA) | Keycloak MFA (TOTP/SMS) + IAM Identity Center MFA + AWS IoT X.509 certs | MFA obligatorio para usuarios con acceso a funciones sensibles (admin, gerente), para accesos privilegiados y para **todo acceso desde fuera de la red corporativa** (Art. 22°): portales externos con TOTP/SMS; preventistas/conductores con factor de posesión + PIN de 6 dígitos (uso con guantes). Dispositivos edge autenticados mediante certificados X.509 únicos por dispositivo. |
| BA — Art. 23° | Separación transaccional/analítica (OLTP/OLAP) | Aurora PostgreSQL (OLTP) + Redshift Serverless (OLAP) + S3 Data Lake | Las escrituras transaccionales van exclusivamente a Aurora. Los datos son exportados vía CDC (AWS DMS o EventBridge) a S3 y de ahí a Redshift. Redshift **nunca** accede directamente a Aurora. |
| BA — Art. 24° | 4 ambientes obligatorios (Dev/QA/Pre-Prod/Prod), más el ambiente de Recuperación ante Desastres (5º) según RT-04.01 | AWS Organizations + **5 cuentas AWS** + Control Tower + VPCs aislados | Cada ambiente reside en una cuenta AWS separada (aislamiento a nivel de facturación, permisos y red): **Dev, QA, Pre-Prod y Prod** en sa-east-1 más la **cuenta DR** en us-east-1 (5º ambiente de Recuperación ante Desastres, RT-04.01, condición del hito H3). AWS Control Tower aplica guardrails automáticos. El tráfico entre cuentas está controlado por Transit Gateway con políticas explícitas. |
| BA — Art. 24° | Aislamiento estricto entre ambientes | AWS Organizations SCPs + Transit Gateway Route Tables | Las SCPs prohíben que recursos de Dev/QA accedan a datos de producción. Las tablas de ruteo del Transit Gateway aíslan las VPCs por ambiente sin rutas directas entre Prod y Dev/QA. |

### 7.4 Bases Técnicas Transversales — Capítulo 2 (Atributos de Calidad)

| Documento y Artículo | Requerimiento / Restricción | Componente Cloud | Justificación Técnica |
|---|---|---|---|
| BTT — Cap. 2 | Arquitectura de monolito modular | Amazon ECS con AWS Fargate + Django ORM | El sistema se implementa como un monolito modular Django desplegado en ECS Fargate. Cada dominio funcional es un módulo Django independiente con sus propias migraciones y modelos. Una única imagen Docker opera en dos modos: full (cloud) y wms_only (on-premise). |
| BTT — Cap. 2 | Desacoplamiento entre módulos | Amazon EventBridge + Amazon SQS + Django signals | Los módulos Django se comunican asincrónicamente via eventos de Django y EventBridge para tareas pesadas. Las tareas de reconciliación, reportes y alertas se ejecutan en workers Celery, desacopladas del request-response. |
| BTT — Cap. 2 | Idempotencia en procesamiento | SQS FIFO + Idempotency Keys en workers Celery + Aurora conditional writes | Las colas SQS FIFO garantizan exactamente-una-vez-procesamiento. Los workers Celery implementan idempotency keys. Aurora usa escrituras condicionales para prevenir duplicados durante reconciliación. |
| BTT — Cap. 2 | Elasticidad | ECS Fargate Target Tracking + AWS Application Auto Scaling + Lambda (serverless) + DynamoDB On-Demand | Target Tracking escala tareas basado en métricas. AWS Application Auto Scaling aprovisionado nodos en minutos. Lambda escala a cero y hasta miles de instancias concurrentes. DynamoDB no requiere gestión de capacidad. |
| BTT — Cap. 2 (RT-02.02) | Servicios sin estado (stateless) | ECS Fargate sin estado + ElastiCache Redis (sesión) + Aurora (persistencia) | Las tareas ECS son stateless; el estado transitorio (sesión, procesos) vive en Redis y el estado durable en Aurora. Permite escalado horizontal y rescheduling sin pérdida de datos. |
| BTT — Cap. 2 (RT-02.08) | Resiliencia: reintento, límites de tasa, timeouts | Retry con backoff + API Gateway throttling + timeouts Django + DLQ Celery | Reintento con exponential backoff + jitter en llamadas externas; API Gateway limita tasa por IP; timeouts declarados en cada integración; Dead Letter Queues en workers Celery para tareas no procesadas. |
| BTT — Cap. 2 (RT-02.10) | Escalamiento horizontal automático con umbrales y límites | ECS Application Auto Scaling (Target Tracking CPU>70%, SQS depth >1000) | Escala de 2 a 6 tareas del monolito Django en peak de septiembre (3×), coherente con §3.5. Cooldown 60s. Los workers Celery escalan de 2 a 4. El criterio se deriva del perfil de carga no plano del caso (RT-09.02). |

### 7.5 Bases Técnicas Transversales — Capítulo 3 (Infraestructura y Cloud)

| Documento y Artículo | Requerimiento / Restricción | Componente Cloud | Justificación Técnica |
|---|---|---|---|
| BTT — Cap. 3 | Topología de red definida | VPC Hub-and-Spoke + Transit Gateway + subredes por capa | Diseño Hub-and-Spoke con VPC central de tránsito conectando VPCs por ambiente. Tres capas de subred (pública/aplicación/datos) en cada VPC. |
| BTT — Cap. 3 | VPC y segmentación | VPCs por ambiente (10.101-104.0.0/16) + subredes /24 por capa y AZ + VPC-HUB (10.100.0.0/16) | Rangos de IP no solapantes por VPC y **sin colisión con los CIDR on-premise (Talca 10.1.x.x, Concepción 10.2.x.x, Cross-docks 10.3.x.x–10.5.x.x)**, requisito para el túnel IPsec híbrido (RT-03.17). Subredes dedicadas por función (pública DMZ, privada app, privada datos, IoT). |
| BTT — Cap. 3 | VPN hacia on-premise | AWS Site-to-Site VPN (IPSec/IKEv2 + BGP) | Conexión cifrada entre instalaciones físicas y VPC de producción. BGP para failover dinámico. Direct Connect como complemento para mayor ancho de banda. La nube solo provee la terminación (amazon-side); el extremo on-premise se diseña en la sección paralela. |
| BTT — Cap. 3 (RT-03.03) | Infraestructura como Código versionada en el repositorio del CLIENTE | AWS CloudFormation + Terraform + CDK en repositorio del CLIENTE | El 100% de la infraestructura se define como código en el **repositorio del CLIENTE** (revisable y reproducible, sin infraestructura manual por consola; solo la cuenta raíz inicial se crea manualmente y queda documentada). §3.4 y §7.6. |
| BTT — Cap. 3 (RT-03.10) | Operación autónoma/desconectada ≥ 14h del borde | AWS IoT Greengrass v2 + Stream Manager + almacenamiento local (SQLite cifrado) | La nube despliega y versiona en el borde la aplicación local, el buffer Stream Manager y las reglas de sincronización. El dispositivo opera offline sin pérdida de datos y sincroniza al reconectar. |
| BTT — Cap. 3 (RT-03.12) | Sincronización automática; reconciliación determinista; bitácora auditable | Greengrass Stream Manager + SQS FIFO + worker Celery `celery-reconciliation` + Aurora (bitácora) | Al recuperar el enlace, Stream Manager envía los mensajes en orden cronológico y con idempotency keys. SQS FIFO garantiza procesamiento ordenado y exactamente-una-vez. Aurora registra cada decisión de reconciliación (bitácora auditable). |
| BTT — Cap. 3 (RT-03.22) | Acceso remoto seguro a la red corporativa | AWS Verified Access + túnel ZTNA de malla (WireGuard/Tailscale o equivalente) | Acceso Zero Trust para trabajo desde el hogar sin VPN tradicional de acceso completo: identidad (OIDC/Keycloak) + postura del dispositivo; sin puertos entrantes ni exposición de servicios internos. On-premise incluido vía túnel de malla. §5.1. |
| BTT — Cap. 3 (RT-03.13) | Declarar funciones NO disponibles en modo desconectado | Declarado en la propuesta + política de degradación | No disponibles en borde offline: portal web, analytics en tiempo real, notificaciones push, integración con cadenas. Se depende del sistema de gestión vigente como respaldo y de la sincronización diferida comprometida (< 10 min tras reconexión). |
| BTT — Cap. 3 (RT-03.17) | Enlace redundante; proveedores distintos; conmutación automática | Direct Connect + Site-to-Site VPN + Route 53 health checks | Dos o más caminos físicos hacia el on-premise con proveedores distintos y conmutación automática a nivel de DNS y de routing (BGP). Redundancia exigida por el Art. 16.4. En el extremo on-premise se incorpora además el **enlace satelital Starlink (D-06)** como tercer camino WAN (fibra D-03 → satelital D-06 → LTE D-04) gestionado con SD-WAN (ver Dimensionamiento v05 §3.7 y Tabla v06 D-06). |
| BTT — Cap. 3 | Balanceo de carga | CloudFront + ALB (HTTP/HTTPS) + NLB (TCP/MQTT) + API Gateway | Múltiples capas de balanceo: CDN global (CloudFront), HTTP multi-path (ALB), TCP de alta throughput (NLB para IoT) y API management (API Gateway). |
| BTT — Cap. 3 | Diseño stateless | ECS Fargate stateless tareas + Lambda + ElastiCache (estado externalizado) | Todos los tareas ECS Fargate y funciones Lambda son stateless. El estado de sesión se almacena en ElastiCache Redis. No hay afinidad de sesión en ALB. |

### 7.6 Bases Técnicas Transversales — Capítulo 4 (Ambientes y Despliegue)

| Documento y Artículo | Requerimiento / Restricción | Componente Cloud | Justificación Técnica |
|---|---|---|---|
| BTT — Cap. 4 | Aislamiento estricto Dev/QA/Pre/Prod/DR | **5 cuentas AWS** separadas + AWS Organizations + Control Tower | Aislamiento a nivel de cuenta AWS: credenciales independientes, VPCs sin enrutamiento cruzado, facturación separada y SCPs específicas por ambiente. La cuenta DR (us-east-1) replica la topología para conmutación sin comprometer los ambientes productivos. |
| BTT — Cap. 4 | Infraestructura como Código (IaC) | AWS CloudFormation + Terraform + AWS CDK | El 100% de la infraestructura está definida como código en el repositorio del CLIENTE (RT-03.03), revisable y reproducible. Los ambientes se crean/actualizan exclusivamente via pipelines automatizados, no manualmente. |
| BTT — Cap. 4 | Pipelines de CI/CD | AWS CodePipeline + CodeBuild + CodeDeploy + ECR | Pipeline automatizado: build de imagen Docker → escaneo de seguridad (Amazon Inspector) → push a ECR → deploy en ECS Fargate con blue/green strategy. Aprobación manual requerida para producción. |
| BTT — Cap. 4 | Paridad entre ambientes | Mismos templates IaC parameterizados por ambiente | Los mismos templates CloudFormation/Terraform se usan para Dev, QA, Pre-Prod, Prod y DR (con parámetros diferentes de dimensionamiento y la DR en us-east-1). Garantiza paridad de configuración y reproducibilidad de la conmutación. |

### 7.7 Bases Técnicas Transversales — Capítulo 5 (Persistencia)

| Documento y Artículo | Requerimiento / Restricción | Componente Cloud | Justificación Técnica |
|---|---|---|---|
| BTT — Cap. 5 | Elección justificada BD relacional vs NoSQL | Aurora PostgreSQL (OLTP relacional) + DynamoDB (IoT/estado NoSQL) | Aurora para datos con relaciones (guías de despacho, clientes, vehículos) que requieren integridad referencial y JOIN. DynamoDB para telemetría IoT de alta velocidad de escritura sin relaciones. |
| BTT — Cap. 5 | Separación OLTP/OLAP | Aurora (OLTP) + Redshift Serverless (OLAP) + S3 Data Lake | El pipeline de datos fluye en una dirección: Aurora → CDC/EventBridge → S3 → Glue ETL → Redshift. Las consultas analíticas nunca impactan el rendimiento transaccional. |
| BTT — Cap. 5 | Retención de datos definida | S3 Lifecycle Policies + DynamoDB TTL + Aurora PITR 35 días | Políticas de retención configuradas: 5 años telemetría IoT, 6 años documentos legales, 35 días PITR bases de datos, 7 años logs de auditoría. Transición automática a Glacier para datos fríos. |
| BTT — Cap. 5 | Respaldos de bases de datos | AWS Backup + Aurora PITR + DynamoDB On-Demand Backup | Backup diario automatizado de Aurora, DynamoDB y EFS via AWS Backup. PITR de Aurora hasta 35 días. Backups exportados a S3 con Object Lock para inmutabilidad. |
| BTT — Cap. 5 (RT-05.03) | Trazabilidad completa: quién, qué, cuándo, desde dónde, valores anteriores/posteriores | Tablas de auditoría append-only en Aurora + CloudTrail + DynamoDB Streams | Cada transacción registra actor, dispositivo, timestamp y valores previos/posteriores. CloudTrail cubre acciones de sistema. El audit trail es inmutable (Object Lock) y reconstruible en cualquier momento del período de retención. |
| BTT — Cap. 5 (RT-05.10) | Retención de datos históricos y de auditoría | S3 Lifecycle + DynamoDB TTL + Aurora archival | Documentos tributarios y respaldo: 6 años; trazabilidad de lote: vida útil + 6 meses (mín. 5 años); temperatura: 5 años; evidencia de entrega: 6 años; geolocalización de personas: 12 meses. |
| BTT — Cap. 5 (RT-05.29) | Latencia analítica: indicadores del día < 5 min; cierre < 2h; gestión < 4h | EventBridge → Lambda → Redshift + QuickSight | Indicadores del día: Aurora → EventBridge → Redshift (< 5 min). Cierre comercial: batch nocturno (< 2h). Indicadores de gestión: Redshift + QuickSight (< 4h). |
| BTT — Cap. 5 (RT-05.16) | Documentación de interfaces: síncronas en OpenAPI 3.1, flujos por eventos en AsyncAPI 2.6+, generada desde el código y versionada semánticamente con compatibilidad hacia atrás | DRF Spectacular (OpenAPI 3.1) + AsyncAPI generator para EventBridge/SQS | Las interfaces REST/GraphQL se documentan desde el código Django (DRF Spectacular), actualizándose automáticamente en cada build. Los flujos de eventos (EventBridge entre módulos, colas SQS de Celery) se documentan en AsyncAPI 2.6+. El catálogo se publica en un repositorio Git compartido con la contraparte técnica. Versionado semántico con preaviso de 6 meses ante deprecación de contratos (RT-05.17). |
| BTT — Cap. 5 (RT-05.21) | Declarar por cada integración: modo (síncrono/asíncrono), volumen, ventana de disponibilidad del contraparte y comportamiento si no responde | ACL on-premise (A-04) + SQS + circuit breaker (Celery) + EventBridge outbox dual-write | Cada integración con el ERP (on-prem, 2017, sin documentación) está declarada con su modo y comportamiento ante fallo: la ACL encola transacciones en SQS si el ERP no responde (hasta 24 h); el circuit breaker de Celery reintenta con backoff exponencial. EventBridge outbox dual-write garantiza que los eventos críticos persisten en Aurora (ACID) incluso si EventBridge no está disponible. Los flujos entre módulos Django (interno) son síncronos y asíncronos declarados en AsyncAPI. |
| BTT — Cap. 5 | Coexistencia de mensajería on-premise (RabbitMQ) y cloud (SQS/EventBridge/IoT Core) en modelo híbrido | RabbitMQ on-prem (A-03) + SQS + EventBridge + AWS IoT Core | Modelo híbrido (Art. 16): RabbitMQ A-03 maneja buffers locales de 24 h durante cortes de WAN (garantiza autonomía RNF-13.01). SQS (Celery workers) y EventBridge (bus de eventos entre módulos) son la capa de mensajería de la nube. IoT Core recibe MQTT desde Greengrass. El worker `celery-reconciliation` procesa la cola SQS FIFO al recuperar el enlace; el envío del broker local a SQS lo ejecuta un **shipper en VM-03** (HTTPS/443, VPC Endpoint SQS/PrivateLink, sin conexiones entrantes). RabbitMQ on-prem es broker de colas offline; la nube administra los flujos de procesamiento central y la durabilidad a largo plazo. |

### 7.8 Bases Técnicas Transversales — Capítulo 7 (DRP)

| Documento y Artículo | Requerimiento / Restricción | Componente Cloud | Justificación Técnica |
|---|---|---|---|
| BTT — Cap. 7 | Estrategia activa/pasiva (Warm Standby) | Región primaria sa-east-1 (activa) + us-east-1 (pasiva tibio) | La región secundaria mantiene Aurora Global DB Reader, réplica DynamoDB Global Tables y ECS Fargate cluster reducido. Puede asumir tráfico productivo en < 2 horas. |
| BTT — Cap. 7 | Inmutabilidad de respaldos | S3 Object Lock (Compliance Mode) + AWS Backup Vault Lock | Los backups en S3 tienen Object Lock en modo Compliance: no pueden ser modificados ni eliminados durante el período de retención, ni siquiera por el usuario root. Backup Vault Lock previene eliminación del vault. |
| BTT — Cap. 7 | Pruebas de DRP | Aurora Global Database health checks + Route 53 health checks + runbooks automatizados + ejercicios semestrales | Health checks automáticos verifican estado de réplicas cada 5 minutos (Aurora Global DB). Ejercicios de failover documentados se ejecutan semestralmente en un ambiente pre-productivo. Resultados auditados en AWS Audit Manager. |

### 7.9 Bases Técnicas Transversales — Capítulo 11 (Seguridad)

| Documento y Artículo | Requerimiento / Restricción | Componente Cloud | Justificación Técnica |
|---|---|---|---|
| BTT — Cap. 11 (RT-11.01) | Arquitectura Zero Trust (NIST SP 800-207) | Zero Trust por capas: microsegmentación (Network ACLs/SG deny-all), acceso por identidad+contexto, mTLS interno, zero standing privileges | Diseño §5.1 conforme a NIST SP 800-207: ninguna confianza implícita por ubicación de red; verificación continua de identidad, dispositivo y sesión; acceso mínimo privilegio por identidad; inspección y registro de todo el tráfico. Conectividad a on-premise y bordes sin confianza de red (VPN/DX segmentada, certificados X.509 por dispositivo). |
| BTT — Cap. 11 (RT-11.07, RT-11.12) | WAF + reto progresivo contra bots | AWS WAF v2 + CloudFront + ALB | WAF v2 desplegado frente a CloudFront y ALB con rulesets OWASP Top 10, SQL injection, XSS y reglas personalizadas de rate limiting. Protección de bots con reto progresivo (Challenge/CAPTCHA) sin degradar accesibilidad (RT-11.12). Logging completo habilitado. |
| BTT — Cap. 11 (RT-11.11) | Puerta de enlace con autenticación, autorización, cuotas, límites de tasa, validación de esquema e inspección de carga útil | AWS API Gateway + Lambda authorizers (OIDC) + usage plans | API Gateway aplica autenticación/autorización OIDC (Keycloak), cuotas y throttling por cliente/API key, validación de esquemas (request models OpenAPI) e inspección estricta de carga útil antes del backend, rechazando peticiones fuera de contrato. WAF complementa el control a nivel de red. |
| BTT — Cap. 11 (RT-11.09) | KMS (gestión de claves) con separación de funciones | AWS KMS con CMK por tipo de dato + AWS CloudHSM (opcional) | Claves KMS gestionadas por el cliente (CMK) con rotación anual automática. Cada clase de dato tiene su propia CMK. Custodia con dual control (roles de administración vs. uso, MFA) declarado en §5.6. Acceso a claves auditado en CloudTrail. |
| BTT — Cap. 11 (RT-11.10) | Cifrado de datos de categoría sensible identificados en el caso (RUT, geolocalización, POD/DTE) | AES-256 a nivel de columna/campo (pgcrypto en Aurora) + envoltura por clave de aplicación KMS | Los datos sensibles del caso (RUT, geolocalización de entregas, evidencia POD/DTE) se cifran **adicionalmente a nivel de campo** con claves derivadas de KMS, de modo que el acceso a la BD no revele su contenido; claves por tenant/campo y rotación anual. §5.3. |
| BTT — Cap. 11 (RT-11.07) | Protección DDoS | AWS Shield Advanced + CloudFront + AWS WAF | Shield Advanced protege en capas 3, 4 y 7. CloudFront absorbe tráfico volumétrico en edge locations antes de llegar a la región. WAF limita la tasa de requests por IP. |
| BTT — Cap. 11 (RT-11.08, RT-11.09) | Cifrado en tránsito y reposo | TLS 1.3 + mTLS interno + AES-256 KMS en todos los recursos | Tráfico externo: TLS 1.3 mínimo. Tráfico interno ECS Fargate: mTLS. Datos en reposo: AES-256 con CMK en Aurora, DynamoDB, S3, EBS, EFS, ElastiCache. Certificados automatizados (ACM) con alarma de vencimiento ≥ 30 días según §5.6. |
| BTT — Cap. 11 (RT-11.16, RT-11.04) | Detección y respuesta en puntos finales y cargas de trabajo, nube y on-premise | Amazon GuardDuty + Security Hub + Inspector + Macie + **agente EDR en endpoints on-premise** | GuardDuty analiza VPC Flow Logs, CloudTrail y DNS para detectar amenazas (servicio de detección administrado de AWS). Security Hub consolida hallazgos. Inspector escanea vulnerabilidades en contenedores e instancias (remediación 7/15/30 días según RT-11.04). Macie detecta PII en S3. **EDR (agente tipo CrowdStrike Falcon/SentinelOne) cubre los puntos finales y estaciones on-premise** (nube y on-premise), con telemetría integrada al lago de seguridad y respuesta aislada ante compromiso. |
| BTT — Cap. 11 (RT-11.14) | Eventos de seguridad centralizados e inalterables: **12 meses en línea + 24 meses adicionales en archivo recuperable** | Security Lake + CloudWatch Logs (12 meses) + S3 archivo (24 meses) con Object Lock | Los eventos de seguridad (CloudTrail, GuardDuty, VPC Flow Logs, autenticaciones Keycloak, acceso ERP vía ACL) se registran centralizadamente e inmutables. Retención: 12 meses en línea (CloudWatch/Security Lake) + 24 meses adicionales en archivo recuperable en S3 con Object Lock (36 meses totales), superando el mínimo. Los logs de auditoría de negocio se conservan 7 años (RT-05.10). |
| BTT — Cap. 11 (RT-11.15) | Correlación SIEM con **casos de uso específicos del proceso de negocio** | SIEM sobre Security Lake (splunk/ELK AWS managed) + casos de uso del caso Puelche | La correlación no se limita a genéricos de infraestructura. Casos de uso definidos para el negocio: (1) excursión de cadena de frío con intentos de acceso anómalos al sistema de telemetría; (2) manipulación o borrado de evidencia registrada de POD/DTE en caja; (3) accesos fuera del horario de bodega (22:00–06:00 solo picking autorizado); (4) escalamiento de privilegios en Keycloak (rol → admin); (5) rendición de caja con accesos simultáneos de un mismo usuario; (6) conexiones de terminate app desde IP fuera de geocercas del turno. Alertas en tiempo real y playbooks de respuesta. |
| BTT — Cap. 11 (RT-11.06) | Controles ISO/IEC 27017 (nube) y 27018 (datos personales en nube) | AWS Artifact + inventario de datos personales de la solución | AWS mantiene programas de conformidad ISO/IEC 27017 e ISO/IEC 27018 verificables en AWS Artifact. La solución declara la aplicación de los controles de cliente de ambas normas (inventario y flujo de datos personales, cláusulas de procesador, derecho de supresión vía retención documentada, notificación de brechas) en §5.6. |
| BTT — Cap. 11 (RT-11.13) | Superficie de exposición completa declarada (dominios, puertos, servicios) | Tabla de superficie §5.6 (`www`/`id`/`api`/`mqtt.puelche.cl`, CDN, VPN, Direct Connect, VPC Endpoints) | Cada dominio, puerto y servicio alcanzable desde fuera de la red del CLIENTE se declara con su protocolo y mecanismo de autenticación. Los CNAME públicos se materializan en diseño detallado con Route 53. |
| BTT — Cap. 11 (RT-11.22) | CI con SAST + SCA + DAST + escaneo de imágenes y bloqueo automático | CodeBuild (SonarQube/CodeGuru SAST, SCA de dependencias, OWASP ZAP DAST) + Amazon Inspector | El pipeline bloquea el despliegue ante hallazgos críticos/altos (gate en CodeBuild), alineado con los plazos de remediación del RT-11.04 (7/15/30 días). |
| BTT — Cap. 11 (RT-11.23) | Inventario de componentes de software (SBOM) entregado al CLIENTE por versión | SBOM CycloneDX generado en el pipeline (Syft/Trivy) | Cada versión liberada se acompaña de su SBOM CycloneDX, entregado al CLIENTE junto con la versión correspondiente. |
| BTT — Cap. 11 (RT-11.24) | Artefactos firmados y procedencia SLSA nivel 3 | Sigstore/cosign + pipeline hermético de CodeBuild con provenance | Las imágenes OCI y el SBOM se firman con Sigstore/cosign; la construcción es hermética y la procedencia SLSA nivel 3 se verifica antes del despliegue. |
| BTT — Cap. 11 (RT-11.25) | Sin datos productivos reales en ambientes no productivos | Datos sintéticos + seudonimización + verificación Macie sobre staging | Dev/QA/PreProd usan solo datos sintéticos o seudonimizados verificables (máscara de RUT/nombres/geolocalización, volumetría Cap. 14); Macie comprueba ausencia de PII en staging. |
| BTT — Cap. 11 (RT-11.27) | Sin acceso interactivo de desarrolladores a producción | AWS Systems Manager Session Manager (JIT, MFA, sesión grabada) | No hay SSH ni consola directa a producción; el acceso excepcional es temporal, aprobado, registrado y grabado, auditado con CloudTrail (RT-11.14). |

### 7.10 Bases Técnicas Transversales — Capítulo 12 (Identidad)

| Documento y Artículo | Requerimiento / Restricción | Componente Cloud | Justificación Técnica |
|---|---|---|---|
| BTT — Cap. 12 | Gestión de identidades | Keycloak (IdP maestro en nube, open source) + AWS IAM + IAM Identity Center + **caché local A-05 (login offline, TTL 8 h)** | Usuarios humanos en Keycloak (única autoridad de identidad, desplegada en ECS Fargate). Servicios en IAM con roles temporales ECS Task Roles. Administradores via IAM Identity Center con SSO federado. La caché local A-05 (VM-05 Talca, VM-C03 Concepción) valida la firma de los tokens y habilita la autenticación offline para el turno nocturno de bodega y terreno (RNF-13.01, RT-03.10). |
| BTT — Cap. 12 | Autenticación multifactor | Keycloak MFA (TOTP/SMS) + IAM Identity Center MFA + X.509 para IoT | MFA obligatorio para roles admin y gerente, para accesos privilegiados y para **todo acceso desde fuera de la red corporativa** (Art. 22°): portales externos con TOTP/SMS; preventistas/conductores con factor de posesión + PIN de 6 dígitos (uso con guantes, una mano), nunca factor único. Los dispositivos IoT edge usan certificados X.509 como factor de autenticación. |
| BTT — Cap. 12 | Control de acceso basado en roles (RBAC) | IAM Policies + Keycloak Groups/Roles + Django permissions | Roles definidos en Keycloak: admin, gerente, jefe_bodega, bodeguero, preventista, conductor, calidad, cliente. Cada rol tiene permisos mínimos. Django ORM hereda los grupos de Keycloak para control de acceso a nivel de aplicación. |
| BTT — Cap. 12 | Rotación de credenciales | AWS Secrets Manager + KMS key rotation + Greengrass certificate rotation | Las credenciales de BD se rotan automáticamente via Secrets Manager. Las claves KMS se rotan anualmente. Los certificados X.509 de dispositivos Greengrass se rotan semestralmente. |
| BTT — Cap. 12 (RT-12.11) | Autenticación adaptada a perfiles operacionales: guantes, una mano, -22°C, dispositivos compartidos, conductores terceros | Keycloak (PIN / facial) + AWS IoT X.509 por dispositivo + política de dispositivo compartido + caché local A-05 (offline) | Preventistas/conductores propios: Keycloak con PIN de 6 dígitos + facial (uso con guantes y una mano) con validación de firma local vía la caché A-05 (VM-05/VM-C03) en modo offline. Conductores de transportistas (dispositivos compartidos): PIN de 4 dígitos sin correo, reset del dispositivo al fin de turno, token offline. Terminales de bodega/cámara: badge + sesión IoT Core. Autenticación diseñada para condiciones extremas de uso, no solo para escritorio. |
| BTT — Cap. 12 (RT-12.01) | Gestión de identidad centralizada con integración al directorio corporativo (OIDC/OAuth 2.1/SAML) | Keycloak (IdP maestro) + integración LDAP con el directorio del CLIENTE | El Realm Puelche se integra por **LDAP con el directorio corporativo del CLIENTE** (alta, cambio de rol, baja), y todos los módulos se autentican por OIDC/OAuth 2.1 federado hacia Keycloak (§5.4). Autoridad de identidad única, con caché local on-premise de solo lectura (TTL 8 h) para contingencia (RT-03.10). |
| BTT — Cap. 12 (RT-12.02) | SSO en todos los módulos con cierre de sesión propagado | Keycloak OIDC + back-channel logout + revocación de sesión | Una única autenticación (Keycloak) da acceso a portal, WMS/back office, BI y Keycloak Admin; el logout se propaga a todos los módulos y la revocación invalida de inmediato las sesiones emitidas, incluida la caché on-premise (§5.4). |
| BTT — Cap. 12 (RT-12.05) | RBAC/ABAC y matriz de segregación de funciones | Roles/grupos Keycloak + ABAC por atributos de proceso + matriz de segregación | RBAC por grupos/roles (admin, gerente, jefe_bodega, bodeguero, preventista, conductor, calidad, cliente) complementado con ABAC (atributos de lote, temperatura, geocerca) y matriz de segregación de funciones para operaciones de doble control (§5.4). |
| BTT — Cap. 12 (RT-12.09) | Auditoría del ciclo de vida de identidad, no repudio y retención | CloudTrail + eventos de auditoría Keycloak + bitácora de no repudio + Lago de seguridad | Cada creación, modificación, elevación, bloqueo y baja de identidad queda auditado con no repudio y retención 12 meses en línea + 24 en archivo (§5.5), integrado al lago de seguridad RT-11.14. |
| BTT — Cap. 12 (RT-12.10) | Aprovisionamiento/desaprovisionamiento automático de identidades en ≤ 24 h | Keycloak Users API vía eventos EventBridge (SCIM/API) + Lambda + cycles de desactivación en < 24 h | Resonancia con la operación de terreno: un preventista o conductor que se desvincula debe perder acceso en < 24 h. Keycloak **maestro (nube)** aplica la revocación y la propaga a las cachés locales A-05/VM-C03 (Δ ≤ 8 h por TTL; < 24 h por SCIM). Roles empresariales (alta en nómina, cambio de rol, salida) disparan automáticamente la provisión/desprovisión de cada identidad desde el maestro, con bitácora auditable (RT-16.08). |
| BTT — Cap. 12 (RT-12.06) | Accesos privilegiados con elevación temporal, aprobación previa y grabación de sesión | IAM Identity Center permission sets (JIT, ≤ 24 h) + AWS Systems Manager Session Manager con grabación | La elevación a roles privilegiados (consola AWS, DBA de Aurora, administración de Keycloak/IAM) es temporal y bajo demanda con aprobación previa y vencimiento máximo declarado (≤ 24 h); no hay permisos administrativos permanentes de amplio alcance. Las operaciones de mayor riesgo se ejecutan por Session Manager con grabación de sesión y auditoría CloudTrail, con *break-glass* auditado (RT-12.13). Detalle en §5.6. |
| BTT — Cap. 12 (RT-12.04) | Factores de autenticación resistentes a suplantación | Keycloak WebAuthn (FIDO2/passkeys) para perfiles privilegiados | Los administradores y operadores de doble control podrán autenticarse con claves de acceso FIDO2 (WebAuthn) además de TOTP, como factor resistente a la suplantación; se ofrece como preferente para admins (§5.4). Deseable, se supera el mínimo. |
| BTT — Cap. 12 (RT-12.07) | Política de sesión (duración, inactividad, renovación, revocación) | Keycloak session policy + token JWT (RS256, vida breve, refresh rotatorio) | Sesión web 8 h / móvil 14 h, inactividad 15/30 min, renovación de la credencial de sesión tras la autenticación, revocación inmediata de sesiones emitidas (logout propagado), una sesión concurrente por actor en terreno (§5.4). |
| BTT — Cap. 12 (RT-12.12) | Registro, verificación y recuperación de usuarios externos autoservida | Keycloak self-service (registro OTP, verificación CIS, reset autoservido) | Los clientes del portal se registran con verificación por correo/celular OTP y validación de empresa; recuperación de acceso autoservida con OTP/vínculo firmado sin exponer servicios internos (§5.4). |
| BTT — Cap. 12 (RT-12.13) | Procedimiento de acceso de emergencia (*break-glass*) documentado | Cuenta de emergencia con custodia compartida (split-knowledge) + Session Manager + SIEM | Credencial fraccionada junto al Jefe de TI del CLIENTE, activación solo con ticket de incidente, sesión grabada, alarma SIEM, rotación posterior al uso y revocación en el turno siguiente; probado en el DRP semestral (§5.5). |

### 7.11 Caso 02 Logística — Capítulo 10 (Restricciones No Negociables)

| Documento y Artículo | Requerimiento / Restricción | Componente Cloud | Justificación Técnica |
|---|---|---|---|
| Caso 02 — Cap. 10 | No intervenir el ERP contable | `celery-erp-sync` (solo lectura vía **ACL on-premise**) + API Gateway adapter + SQS + VPN | El ERP contable se mantiene intocado en Talca. El worker Celery `celery-erp-sync` del módulo `integraciones` **nunca accede directamente al ERP**: atraviesa la VPN y consume únicamente la **Capa Anticorrupción (ACL) del on-premise** (A-04), que es la frontera única documentada del ERP (contrato OpenAPI). Solo lectura; las notificaciones se encolan en SQS y el ERP las consume bajo su propia lógica, sin escrituras del sistema logístico en el ERP. |
| Caso 02 — Cap. 10 | Límites técnicos de integración | Contract-first API design + AWS API Gateway + OpenAPI specs **en la ACL on-premise** | Todas las integraciones están definidas con contratos OpenAPI versionados publicados por la **ACL on-premise (A-04)**, que desacopla el sistema logístico (WMS y nube) de los contratos internos aún no documentados del ERP. API Gateway actúa como façade en la nube; el acceso al ERP físico solo ocurre por la ACL. |
| Caso 02 — Cap. 10 | Trazabilidad completa de temperatura | DynamoDB `iot-temperature-readings` + S3 raw telemetry + Immutable audit log | Cada lectura de temperatura se almacena en DynamoDB (baja latencia) y simultáneamente en S3 raw (retención 5 años, inmutable con Object Lock). El audit trail es append-only e inmodificable. |

### 7.12 Caso 02 Logística — Capítulo 15 (Parámetros Numéricos)

| Documento y Artículo | Requerimiento / Restricción | Componente Cloud | Justificación Técnica |
|---|---|---|---|
| Caso 02 — Cap. 15 | Retención telemetría IoT temperatura: **5 años** | DynamoDB TTL (30 días) + S3 raw (5 años) + S3 Parquet / Redshift (consolidado, 5 años) | DynamoDB TTL configurado en **30 días** para la tabla cruda `iot-temperature-readings` solo como zona de aterrizaje de baja latencia; al validarse se replica a S3 `s3-raw-telemetry-iot` con retención **5 años** (Intelligent-Tiering → Glacier Instant, año 2) y el consolidado analítico se genera en la capa OLAP (§4.3): Glue transforma a Parquet en `s3-analytics-parquet` (retención **5 años**), consultado por Redshift Serverless. Así la retención total de temperatura = 5 años, con DynamoDB como buffer efímero y sin pérdida de datos. |
| Caso 02 — Cap. 15 | Retención documentos S3 (tributarios / DTE, guías): **6 años** | S3 Object Lock (Compliance Mode, 6 años) + S3 Intelligent-Tiering → Glacier Deep Archive | Bucket `s3-documents-legal` con Object Lock en modo Compliance y período de retención de 2190 días (6 años). Transición a Glacier Deep Archive a partir del año 2 para optimización de costos. Sin posibilidad de eliminación prematura. |
| Caso 02 — Cap. 15 | Peak logístico de septiembre | ECS Fargate AWS Application Auto Scaling + Target Tracking + DynamoDB On-Demand + EventBridge auto-scaling | En agosto se ejecuta un runbook de pre-warm: se incrementa la capacidad base del cluster ECS Fargate, se escala EventBridge y se activa mayor concurrencia reservada en Lambda. Las políticas de auto-scaling escalan automáticamente hasta 3× la capacidad base durante el peak. |
| Caso 02 — Cap. 15 | Dimensionamiento para volumen de flota | Sizing en sección 3.4 derivado de la volumetría Cap. 14.1 (14.200 clientes, 260.000 líneas/mes, ~96 camiones, ~270 dispositivos) | El dimensionamiento parte de la volumetría real del caso (31.000 pedidos/mes, 260.000 líneas/mes, ~1.400 entregas/día y ~2.600 en peak) y del perfil horario no plano (preventa 09:00–18:00, preparación 22:00–06:00, despacho 05:30–07:00, sync 17:00–20:00). Las políticas de auto-scaling garantizan escalado sin intervención manual durante peaks estacionales o crecimientos imprevistos. |

> **Tiempos de restauración completa por dominio de datos (RT-07.13):** para cada dominio se declara frecuencia, retención y **tiempo estimado de restauración completa (full restore)**, coherente con RTO ≤ 4 h:
>
> | Dominio | Fuente primary | Frecuencia backup | Retención | Restauración completa (P99) |
> |---|---|---|---|---|
> | Transaccional OLTP (Aurora PostgreSQL) | Aurora Continuos Backup (PITR) | Continuo (PITR 35 días) + snapshots diarios | 35 días PITR + 1 año | ≈ 2,5 h (nueva instancia + restore) |
> | Consolidado analítico de temperatura (S3 Parquet / Redshift) | Export diario a S3 + Redshift UNLOAD | Diario | 5 años (Parquet) | ≈ re-carga desde S3 raw / lake (24 h) |
> | Tablas clave-valor / estadios (DynamoDB) | On-Demand Backup + PITR | Continuo (PITR 35 días) + on-demand | 35 días PITR + 1 año | ≈ 30-45 min (restore tabla) |
> | Objetos / documentos legales (S3) | S3 Versioning + CRR (RTC) | Continua versión + Lifecycle | 6 años (Object Lock) | ≈ acceso inmediato (objetos) / rehidratación Glacier (≤ 12 h bajo contrato) |
> | Mensajes/eventos (EventBridge + SQS) | Outbox dual-write + respaldo diario | Diario | 1 año | reconstrucción desde Aurora ≈ 1-2 h |
> | Réplica CDC / metadatos de sincronización | S3 RTC | Continua | 1 año | re-carga CDC desde S3 |
>
> Todos los tiempos quedan declarados como **SLO de restauración** verificados en el ejercicio DRP semestral (RT-07.07); la suma nominal de restauración por dominio no supera el RTO de 4 h.

> **Costo de retención declarado (RT-14.08):** el presupuesto diferencia **retención en línea** (CloudWatch Logs 12 meses, S3 Standard/S-IA según dominio) de **retención en archivo** (S3 Glacier Instant/Deep Archive, costo ≈ COP 0,7/GiB-mes en Glacier DA), ambas incluidas en la estructura de costos §4.5 (FinOps) con partida mensual de datos y monitoreo.

### 7.13 Caso 02 Logística — Capítulo 17.4 (los 13 puntos que el caso exige resolver)

> **Corrección del 2026-09-06.** Hasta esta versión, esta sección enumeraba trece temas de infraestructura en nube bajo el rótulo «Capítulo 17.4», pero **no eran los trece puntos del caso**. La tabla siguiente es el **mapa correcto**, verbatim del numeral 17.4, con el componente y el documento que resuelve cada punto en toda la propuesta —no solo en la nube—. La tabla anterior se conserva a continuación como **matriz de sustento en nube**, que es lo que realmente contiene.

| # | Punto del Cap. 17.4 (texto del caso) | Dónde se resuelve | Componentes |
|---|---|---|---|
| **1** | Qué se ejecuta en cada centro de distribución y qué en la nube, y por qué, **componente por componente** | `Tabla_Emplazamiento_OnPremise_v06.md` §1.0 — 36 componentes con criterio dominante (LAT, CRIT, VOL, CONN, TCO, HW, REG) | A-01…F-03, N-01…N-13 |
| **2** | Cómo se sostienen recepción, preparación y despacho durante un corte, y **cómo se reconcilia el inventario** después | Autonomía local de 24 h; buffer RabbitMQ; reconciliación determinista por **regla de reserva** con bitácora auditable del Art. 16.4; sincronización del CD ≤ 2 h tras un corte de 24 h | A-01, A-02, A-03; `Arquitectura_de_Integracion_v01.md` §5, INT-03 |
| **3** | Cómo opera un dispositivo de reparto **un turno completo sin señal**, qué puede y qué no, y cómo se resuelven los conflictos | Matriz formal de funciones **no disponibles** sin conexión con su procedimiento manual (RT-03.13); sincronización ≤ 10 min al reconectar; deduplicación por UUID | C-02; `Tabla_Emplazamiento_OnPremise_v06.md` §1.1; Lógica v6.2 §9.5; INT-02 |
| **4** | Cómo se resuelve la **captura de datos dentro de la cámara de congelado**, a −22 °C y sin cobertura | Terminales MC9400 Cold Storage con misiones descargadas al dispositivo; sensores Modbus RS-485 y Greengrass con buffer de 14 h; estudio de cobertura del interior de cámaras (RT-03.23) | C-03, B-01, B-02 |
| **5** | Cómo se integra el **ERP** y la emisión de **documentos tributarios**: en qué sentido, con qué frecuencia y con qué garantía de consistencia | Capa anticorrupción A-04 como frontera única —**nunca escritura directa al ERP**—; DTE síncrono con **timbre diferido y folio reservado** cuando no hay conexión, sin guías de papel | A-04, `fn-document-signer`, S3 Object Lock; INT-06, INT-07 |
| **6** | Qué se hace con el **sistema de gestión de almacenes de 2013** y qué consecuencias tiene sobre alcance, costo y riesgo | **ADR-08**: reemplazo total en la Etapa 1 por los módulos M1/M2/M5, con alternativas evaluadas, migración por dominio (RT-05.11–15), oleadas por sitio y plan de reversión azul-verde | A-01; ADR-08 |
| **7** | Cómo se modela la **trazabilidad de lote** desde la recepción hasta el punto de entrega y **qué estructura de datos** la sostiene | Identidad = **lote GS1 (GTIN + lote + vencimiento)** con la unidad logística **SSCC** enlazada en cada movimiento; eventos EPCIS; retiro sanitario en menos de 2 h | Lógica v6.2 §8.6 y D11; A-02, Aurora |
| **8** | Cómo se **captura y conserva la evidencia de entrega** y cómo se articula con la guía electrónica y su acuse | POD con firma, fotografía y QR capturados sin conexión; S3 con Object Lock y retención de 6 años; firma conforme a la Ley 19.799 y acuse de recibo | C-02, S3 Object Lock, Aurora; INT-07 |
| **9** | Cómo se incorporan los **conductores de empresas transportistas**, con sus dispositivos y su rotación | **OTP de un solo uso por operación, sin cuenta corporativa** (RF-06.08); parque TC58e unificado propios/externos: mismo repuesto, misma capacitación; baja inmediata sin trámite | N-02, Keycloak; `Arquitectura_de_Seguridad_v01.md` §4.2 y §4.5 |
| **10** | Cómo se sirve el **canal moderno** con mensajería electrónica estructurada **sin construir una integración distinta para cada cadena** | **ADR-11**: hub GS1 centralizado con modelo canónico (EANCOM/GS1 XML, EPCIS); una cadena nueva entra por **configuración de perfil** y equivalencias GTIN, no por desarrollo | M11, N-09; INT-08 |
| **11** | Cómo se **separa el almacenamiento transaccional del analítico** y cómo se sirven los indicadores del día con la latencia comprometida | OLTP en Aurora y PostgreSQL local; OLAP en S3 Parquet, Glue y Redshift Serverless; latencias del Cap. 15: 5 min para la operación del día, 2 h para el cierre comercial y 4 h para los indicadores de gestión | N-05, N-10; Lógica v6.2 §10.9 y D2 |
| **12** | Qué se hace con la **sala de servidores actual**, que no cumple el estándar exigido | La sala de 25 m² **no cumple** el Cap. 6: se habilita a nuevo una **sala técnica secundaria** con 14 recintos, TIER II objetivo, UPS N+1, generador de 24 h, clima de precisión N+1 y cuatro capas de acceso | `Sala_Servidores_OnPremise_v02.md` |
| **13** | Cómo absorbe el diseño el **peak de septiembre** y **qué componente se satura primero** | **ADR-12**: escalado predictivo más reactivo (Fargate 2→6, Celery 2→4, Aurora a `xlarge`); carga de diseño de 3.900 entregas/día. **Primer cuello de botella declarado: VM-02, la escritura transaccional de PostgreSQL**, con detección y mitigación en cuatro pasos | N-04, N-05; `Dimensionamiento_y_Plan_de_Capacidad_v01.md` §8; ADR-12 |

#### 7.13 bis — Matriz de sustento en nube de los puntos anteriores

| Documento y Artículo | Requerimiento / Restricción | Componente Cloud | Justificación Técnica |
|---|---|---|---|
| Sustento cloud N° 1 | Operación a **−22 °C** sin señal (edge autónomo) | AWS IoT Greengrass v2 gestionado desde la nube + Stream Manager + almacenamiento local cifrado | Greengrass v2 opera completamente offline. La nube despliega y versiona en el borde el runtime, las reglas de alerta y el buffer (Stream Manager); los datos de temperatura se almacenan en SQLite cifrado en el dispositivo. El requisito de hardware certificado para −30 °C/−40 °C que la nube exige a los terminales de cámara se define como interfaz en la **sección on‑premise paralela** (este documento solo declara el requisito de interfaz y protocolo MQTT/TLS). |
| Sustento cloud N° 2 | Reconciliación asíncrona tras **14 horas offline** | Greengrass Stream Manager + SQS FIFO + `celery-reconciliation` + Idempotency Keys | Al recuperar señal, Greengrass Stream Manager envía los mensajes acumulados en orden cronológico. SQS FIFO garantiza procesamiento ordenado. `celery-reconciliation` (worker Celery del módulo `telemetria`) usa idempotency keys para desduplicar. Los datos de temperatura de las 14h se procesan sin pérdida. |
| Sustento cloud N° 3 | Separación cloud/edge clara | Greengrass (edge) + IoT Core (nube) + arquitectura de dos capas explícita | El edge (Greengrass) es responsable de: captura de sensores, almacenamiento local, alertas locales y sincronización. La nube (IoT Core + monolito Django) es responsable de: orquestación, análisis, reportes y cumplimiento. Interfaz clara via MQTT/HTTPS. |
| Sustento cloud N° 4 | Peak logístico de septiembre (escalado) | AWS Application Auto Scaling + Target Tracking + DynamoDB On-Demand + Lambda concurrencia reservada | Pre-warm en agosto: incremento manual de nodos base. Auto-scaling reactivo: Target Tracking escala tareas en < 2 min, AWS Application Auto Scaling aprovisiona nodos en < 3 min. DynamoDB y Lambda escalan sin configuración adicional. |
| Sustento cloud N° 5 | Alertas en tiempo real por ruptura de cadena de frío | `fn-iot-validator` (Lambda) + SNS + PagerDuty + `celery-alert-engine` | Cada lectura de temperatura se valida inmediatamente por `fn-iot-validator` al ingresar vía IoT Core Rules. Si supera el umbral, SNS publica alerta en < 5 segundos. `celery-alert-engine` (worker Celery del módulo `calidad`) ejecuta procesamiento de alertas por síntomas de negocio (OTIF bajo, pedidos no preparados). |
| Sustento cloud N° 6 | Trazabilidad completa de temperatura por envío | DynamoDB `iot-temperature-readings` (PK: device_id, SK: timestamp; **GSI por shipment_id**) + S3 raw | Cada lectura de temperatura está asociada a su `shipment_id` y `device_id`. El GSI por `shipment_id` permite queries eficientes por envío y rango de tiempo (PK principal optimiza ingesta por dispositivo — ver §4.2). S3 guarda la trayectoria completa en formato raw por 5 años. |
| Sustento cloud N° 7 | Gestión de documentos tributarios (DTE) y guías de despacho electrónicas | Módulo Django `integraciones` + S3 Object Lock + Aurora (metadatos) + `fn-document-signer` + API SII | Los documentos tributarios electrónicos y guías se almacenan en S3 con Object Lock (inmutables). Los metadatos (número de guía, fecha, estado, folio, referencias) en Aurora. `fn-document-signer` aplica firma electrónica conforme a la Ley N° 19.799 y las normas de timbraje del SII. Acceso versionado: cualquier versión histórica es recuperable. |
| Sustento cloud N° 8 | Integración con ERP contable sin intervención | `celery-erp-sync` (read-only vía **ACL on-premise**) + SQS + API Gateway adapter | El sistema logístico consume datos del ERP exclusivamente a través de la **Capa Anticorrupción (ACL) on-premise (A-04)** a la que llega por la VPN — nunca directo al ERP. Las notificaciones fluyen via SQS. Nunca hay escrituras directas del sistema logístico al ERP. |
| Sustento cloud N° 9 | Seguridad end-to-end en transmisión de datos IoT | MQTT over TLS 1.2+ + certificados X.509 por dispositivo + AWS IoT Core policies | Cada dispositivo Greengrass tiene un certificado X.509 único registrado en AWS IoT Core. La comunicación MQTT está cifrada con TLS. Las IoT Policies definen qué tópicos puede publicar/suscribir cada dispositivo, con mínimo privilegio. |
| Sustento cloud N° 10 | Disponibilidad del sistema central (SLA ≥ 99.9%) | ECS Fargate Multi-AZ + Aurora Multi-AZ + DynamoDB + ALB Multi-AZ + Shield Advanced | La combinación de Multi-AZ en todos los componentes críticos, health checks automáticos, failover < 30s en Aurora y ausencia de SPOF garantiza disponibilidad ≥ 99.9% (< 8.8 horas de downtime/año, dentro del umbral del BTT Cap. 10). |
| Sustento cloud N° 11 | Análisis histórico de datos de temperatura | Redshift Serverless + S3 Data Lake (Parquet) + AWS Glue ETL + Amazon Quicksight | Los datos de temperatura históricos (hasta 5 años) se transforman de JSON raw a Parquet en S3 via Glue ETL y se cargan en Redshift para análisis. Amazon QuickSight provee dashboards interactivos de cadena de frío. |
| Sustento cloud N° 12 | Cumplimiento normativo y auditoría | AWS CloudTrail + S3 Object Lock (audit logs 7 años) + AWS Audit Manager + Macie | Toda acción sobre datos críticos (documentos, temperatura, accesos) queda registrada en CloudTrail. Los logs son inmutables (S3 Object Lock). AWS Audit Manager genera reportes de cumplimiento. Macie detecta y alerta sobre manejo inadecuado de datos sensibles. |
| Sustento cloud N° 13 | Escalabilidad para crecimiento de flota a 5 años | Arquitectura serverless-first + DynamoDB On-Demand + ECS Fargate auto-scaling + EventBridge auto-scaling | La arquitectura es elástica por diseño: DynamoDB y Lambda escalan sin cambios de configuración. ECS Fargate escala nodos automáticamente. EventBridge escala brokers. S3 y Redshift no tienen límite práctico de almacenamiento. El crecimiento de flota no requiere rediseño arquitectónico. |

---

## APÉNDICE A: DIAGRAMA DE ARQUITECTURA CONCEPTUAL (DESCRIPCIÓN TEXTUAL)

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                        ARQUITECTURA CLOUD AWS — CASO 02 LOGÍSTICA            ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  EDGE (Vehículos y Bodegas)                                                  ║
║  ┌─────────────────────────┐                                                 ║
║  │ AWS IoT Greengrass v2   │ ←── Sensores temp. (-22°C)                     ║
║  │ SQLite cifrado (offline)│ ←── GPS tracker                                ║
║  │ Stream Manager (buffer) │ ──→ MQTT/TLS 1.2+ cuando hay señal             ║
║  └────────────┬────────────┘                                                 ║
╠═══════════════╪══════════════════════════════════════════════════════════════╣
║  NUBE AWS (sa-east-1 primaria)                                               ║
║               ▼                                                              ║
║  ┌─────────────────────────────────────────────────────────────────────┐     ║
║  │  Internet Edge: Shield Advanced + CloudFront + WAF v2               │     ║
║  └──────────────────────────┬──────────────────────────────────────────┘     ║
║                             ▼                                                ║
║  ┌──────────────────────────────────────────────────────────────────┐        ║
║  │  VPC Producción (10.101.0.0/16)  — Multi-AZ (AZ1 + AZ2)         │        ║
║  │  ┌─────────────┐  ┌──────────────────────────────────────────┐   │        ║
║  │  │ Subred DMZ  │  │  AWS IoT Core (MQTT endpoint)            │   │        ║
║  │  │ ALB + API   │  │  IoT Rules Engine → Lambda validator     │   │        ║
║  │  │ Gateway     │  └──────────────────────┬───────────────────┘   │        ║
║  │  └──────┬──────┘                         │                        │        ║
║  │         ▼                                ▼                        │        ║
║  │  ┌──────────────────────────────────────────────────────────┐    │        ║
║  │  │  Subred Privada Aplicación: Amazon ECS con AWS Fargate (Multi-AZ)        │    │        ║
║  │  │  Django Monolito Modular + Celery Workers + EventBridge + SQS                 │    │        ║
║  │  │  módulos: inventario, picking, recepcion, preventa, reparto, rutas       │    │        ║
║  │  │  módulos: cobranza, calidad, bi, edi, telemetria, integraciones          │    │        ║
║  │  └──────────────────────────┬───────────────────────────────┘    │        ║
║  │                             ▼                                     │        ║
║  │  ┌──────────────────────────────────────────────────────────┐    │        ║
║  │  │  Subred Privada Datos:                                    │    │        ║
║  │  │  Aurora PostgreSQL (OLTP) | DynamoDB (IoT) | Redis        │    │        ║
║  │  └──────────────────────────────────────────────────────────┘    │        ║
║  └──────────────────────────────────────────────────────────────────┘        ║
║                                                                              ║
║  ┌──────────────────────────────────────────────────────────────────┐        ║
║  │  Capa Analítica: S3 Data Lake → Glue ETL → Redshift Serverless  │        ║
║  └──────────────────────────────────────────────────────────────────┘        ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  DRP (us-east-1): Aurora Global DB Reader + DynamoDB Global Tables +          ║
║  ECS Fargate Standby + S3 CRR + Route 53 Failover                                   ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

## APÉNDICE B: RESUMEN DE SERVICIOS AWS UTILIZADOS

| Categoría | Servicio AWS | Propósito Principal |
|---|---|---|
| **Cómputo** | Amazon ECS con AWS Fargate | Despliegue de monolito Django modular y workers Celery |
| **Cómputo** | AWS Lambda | Funciones event-driven |
| **Cómputo** | AWS IoT Greengrass v2 | Computación edge offline |
| **Red** | Amazon VPC | Redes virtuales aisladas |
| **Red** | AWS Transit Gateway | Conectividad multi-VPC |
| **Red** | AWS WAF v2 | Protección de aplicaciones web |
| **Red** | AWS Shield Advanced | Protección anti-DDoS |
| **Red** | Amazon CloudFront | CDN y primera línea de defensa |
| **Red** | AWS ALB / NLB | Balanceo de carga |
| **Red** | Amazon API Gateway | Fachada del monolito Django |
| **Red** | AWS Site-to-Site VPN | Conectividad segura on-premise |
| **Red** | Amazon Route 53 | DNS y failover DRP |
| **IoT** | AWS IoT Core | Ingesta de telemetría MQTT |
| **BD Relacional** | Amazon Aurora PostgreSQL | OLTP transaccional |
| **BD NoSQL** | Amazon DynamoDB | Telemetría IoT, estado edge |
| **Caché** | Amazon ElastiCache for Redis | Caché y sesiones |
| **Mensajería** | Amazon EventBridge | Bus de eventos entre módulos Django |
| **Mensajería** | Amazon SQS | Colas de trabajo |
| **Mensajería** | Amazon SNS | Notificaciones y alertas |
| **Almacenamiento** | Amazon S3 | Data Lake, backups, documentos |
| **Analítica** | Amazon Redshift Serverless | Data Warehouse OLAP |
| **Analítica** | AWS Glue | ETL y catálogo de datos |
| **Analítica** | Amazon QuickSight | Dashboards y reportes |
| **Seguridad** | AWS KMS | Gestión de claves de cifrado |
| **Seguridad** | AWS Secrets Manager | Gestión de credenciales |
| **Seguridad** | AWS IAM | Control de acceso a servicios |
| **Seguridad** | Keycloak (open source, self-hosted en ECS Fargate) | Autenticación y autorización (IdP maestro) |
| **Seguridad** | Amazon GuardDuty | Detección de amenazas (servicio administrado de AWS) |
| **Seguridad** | AWS Security Hub | Consolidación de hallazgos |
| **Seguridad** | Amazon Inspector | Escaneo de vulnerabilidades |
| **Seguridad** | Amazon Macie | Protección de datos sensibles en S3 |
| **Gestión** | AWS Backup | Respaldos centralizados |
| **Gestión** | AWS CloudTrail | Auditoría de API calls |
| **Gestión** | AWS Config | Cumplimiento de configuraciones |
| **Gestión** | AWS Control Tower | Gobernanza multi-cuenta |
| **Gestión** | AWS Organizations | Gestión de cuentas y SCPs |
| **FinOps** | AWS Cost Explorer | Visualización y análisis de costos |
| **FinOps** | AWS Budgets | Presupuestos y alertas de costos |
| **FinOps** | AWS Cost Anomaly Detection | Detección de anomalías de costos (umbrales de desviación) |
| **IaC/CI-CD** | AWS CloudFormation + Terraform | Infraestructura como Código |
| **IaC/CI-CD** | AWS CodePipeline + CodeBuild | Pipeline CI/CD |
| **IaC/CI-CD** | Amazon ECR | Registro de imágenes Docker |
| **Observabilidad** | Amazon CloudWatch | Métricas, logs y alarmas |
| **Observabilidad** | Grafana OSS (autogestionado en ECS Fargate) | Dashboards operacionales |
| **Observabilidad** | Amazon Managed Prometheus | Métricas de ECS Fargate |
| **Observabilidad** | AWS X-Ray / ADOT | Trazabilidad distribuida |

---

## APÉNDICE C: CORRESPONDENCIA DE LAS 7 CAPAS DEL MODELO OSI

Mapa de las siete capas del modelo OSI con los componentes de la infraestructura híbrida (nube AWS + segmento on-premise del documento `Tabla_Emplazamiento_OnPremise_v06.md`). El mismo componente puede participar en más de una capa según el mecanismo que use.

| Capa OSI | Función | Infraestructura NUBE (AWS) | Infraestructura ON-PREMISE (doc emplazamiento) |
|---|---|---|---|
| **7 — Aplicación** | Servicios de negocio, protocolos de aplicación (HTTP, MQTT, SQL), datos | Monolito Django **ECS Fargate**, **Lambda**, APIs **REST** (API Gateway), **Aurora PostgreSQL** (OLTP), **DynamoDB**, **S3**, bus de eventos **EventBridge/SQS/SNS**, **Keycloak (IdP maestro)**, **AWS IoT Core** (MQTT) | **WMS (A-01)**, BD **PostgreSQL (A-02)**, **ACL ERP (A-04)**, Broker de colas **RabbitMQ (A-03)**, **Caché Keycloak (A-05)**, Gateway **Greengrass (B-02)**, Mini-WMS cross-docking **(E-01)**, apps móviles edge **(C-01/C-02)** |
| **6 — Presentación** | Cifrado en tránsito, serialización/formato, TLS | **CloudFront** (CDN + TLS), **WAF**, **TLS 1.3** externo, **mTLS** interno, **API Gateway** (serialización/validación) | **VPN IKEv2/AES-256** (D-01), cifrado de disco **(F-03/RNF-23.04)**, TLS de servicios locales, cifrado **SQLite** en apps **(C-02)** |
| **5 — Sesión** | Sesiones, establecimiento/control de conexión, estado de diálogo | **ALB** (capa 7) y **NLB**, **API Gateway**, sesiones **Keycloak** (OIDC/JWT, maestro en nube), estado de sesión en **ElastiCache Redis** (RT-02.05: stateless, sesión externalizada) | **Caché Keycloak (A-05)** — login offline con tokens JWT por perfil (TTL 8 h bodega · 14 h reparto/preventa); **Broker A-03** (colas/mensajería como diálogo persistente) |
| **4 — Transporte** | TCP/UDP, control de flujo y errores extremo a extremo | Balanceo L4 **NLB**, **TCP/UDP** de servicios, **Site-to-Site VPN (IPsec/UDP 500-4500)**, control de puertos en **Security Groups** | **Firewall/UTM (D-01)** — inspección/traza de puertos, conmutación de túneles, **QoS/SD-WAN** sobre enlaces (D-03/D-04/D-06) |
| **3 — Red** | IP, enrutamiento, direccionamiento, subredes | **VPC** + subredes (10.x.x.x), **Route 53** (DNS), **Transit Gateway**, **Internet/Virtual Private Gateway** | **Firewall (D-01)** como **Customer Gateway** del túnel IPsec; enrutamiento IP LAN; **BGP** entre túneles (D-01); enlaces WAN **fibra (D-03) / satelital Starlink (D-06) / LTE (D-04) — SD-WAN multi-WAN** |
| **2 — Enlace de datos** | Tramas, MAC, segmentación L2, VLANs | **VPC** (espacio de red L2), subredes por zona, **VPC Endpoints** | **Switch de core (D-02)** con **VLANs** (IoT, Bodega, Gestión, Servidores) para segmentación por tipo de dispositivo (RT-03.23) |
| **1 — Física** | Medio físico, señales, cables, hardware | **Data centers AWS sa-east-1** (región primaria) y **us-east-1** (DRP), **2 o más Zonas de Disponibilidad** (sa-east-1a/1b mínimo; tercera disponible para escalado multi-AZ), fibra/red AIS de AWS | **Sala Técnica Talca** (D-01), **Gabinete Borde Concepción** y cross-docking, enlaces **fibra (D-03)/satelital Starlink (D-06)/LTE (D-04)**, cableado LAN, **sensores industriales (B-01)**, **terminales rugosos (C-03)**, **impresoras andén (C-04)**, **NAS WORM (D-05)**, **5 kits Starlink (D-06)** |

**Lectura recomendada en el plano físico:** la capa 1 concentra la decisión de hibridación del Art. 16° — qué corre on-premise por latencia/criticidad/sin-señal (WMS, bodega, IoT industrial) y qué corre en la nube (lo central y lo que la latencia permite). Las capas 3 y 4 contienen toda la conectividad hibrida (VPN IPsec de D-01, enlaces D-03/D-06/D-04 con SD-WAN, VPC), y las capas 5 a 7 el comportamiento de la aplicación de negocio.

---

## LIMITACIONES CONOCIDAS Y MITIGACIONES

| # | Limitación | Impacto | Mitigación declarada |
|---|---|---|---|
| L-01 | **ElastiCache Redis no tiene réplica cross-region.** Si sa-east-1 cae, se pierde caché y sesiones. | Los usuarios deben re-autenticarse; queries frecuentes impactan Aurora por ~15 min hasta regenerar caché. | Aurora soporta el load transicional. El patrón cache-aside regenera la caché de forma transparente en < 15 min. Las sesiones se re-crean al re-autenticar con Keycloak (IdP maestro). |
| L-02 | **Las cachés locales A-05 (VM-05 Talca, VM-C03 Concepción) mantienen el Δ de identidad con TTL 8 h respecto del maestro en nube.** Si la VPN cae > 8 h, un alta/baja o cambio de rol realizado en el maestro no se refleja en las cachés hasta re-sincronizar. | Un usuario dado de baja en el nube podría seguir autenticándose contra una caché local desactualizada por hasta ~8 h (riesgo residual controlado); cambios de rol se propagan con ≤ 8 h (TTL) y ≤ 24 h (SCIM, RT-12.10). | Keycloak **maestro (nube)** es la autoridad única — no hay escrituras locales ni promoción a maestro. Las cachés importan el Realm cifrado (S3 outbound) al recuperar el enlace (Δ ≤ 8 h). La revocación se propaga del maestro a las cachés en la primera re-sincronización; para identidades de alta sensibilidad la baja se refuerza con la matrícula de activos (RT-12.10). |
| L-03 | **App móvil (C-01/C-02): pérdida del dispositivo = pérdida de datos locales.** No hay backup remoto del estado offline del celular. | Se pierde el POD, la firma digital y el cobro en efectivo del último ciclo de reparto. | El reparto sincroniza transacciones al celular cuando hay conectividad. Si el celular se pierde, la central detecta las entregas no confirmadas y las re-asigna. El POD original queda en Aurora (sincronizado previo a la pérdida). Riesgo residual: datos generados después de la última sincronización. |
| L-04 | **Concepción y cross-docks no tienen appliance D-05 equivalente** (sin NAS WORM local). | Si el nodo falla, no hay copia local de recuperación rápida; la restauración depende de Aurora vía VPN. | RTO adicional de 1-2 h sobre el RTO declarado si la WAN está disponible. En WAN outage, el nodo opera con su BD embebida (SQLite/PostgreSQL local) y se sincroniza al recuperar conectividad. |
| L-05 | **Failover DRP cloud: paso 3 es manual** (decisión de equipo de arquitectura, 5-15 min). Si el equipo no responde, se consume presupuesto de RTO. | RTO real puede exceder las 4 h declaradas si hay demora en la decisión. | Procedimiento documentado con SLA de respuesta del equipo (call tree). Opcional: implementar AWS Systems Manager Automation para escalamiento automático del paso 6 (ECS) y paso 7 (DNS), reduciendo la dependencia humana. |
| L-06 | **Pipeline OLAP (S3→Glue→Redshift): sin RTO/RPO declarado.** | Los reportes de BI y cumplimiento pueden quedar obsoletos durante un failover. | No es crítico para la operación logística. Los datos se re-procesan desde S3 al restaurar el pipeline. RTO estimado: 2-4 h post-failover. |
| L-07 | **WLAN on-prem para 120 terminales de picking (C-03): sin failover documentado.** | Si el AP o switch WiFi falla, los terminales quedan incomunicados. | Se asume infraestructura WiFi redundante (APs múltiples con controlador) como parte del dimensionamiento de red del RT-06.01. Confirmar en fase de diseño detallado. |
| L-08 | **Workers Celery: si una tarea falla, se reintentará pero sin circuit breaker nativo.** | Una tarea defectuosa puede reintentar indefinidamente y consumir recursos. | Configurar retry con max_retries=3 y exponential backoff. Tareas fallidas van a DLQ (Dead Letter Queue) para inspección manual. Monitoreo via CloudWatch. |

*Versión 3.7 — Resolución INC-01 (06-09-2026): la solución **no incorpora componentes de IA/ML** (RT-18 N/A). Se elimina la referencia a **Amazon SageMaker Edge Manager** en §3.4 (la detección de excursiones térmicas pasa a **umbrales y reglas por configuración** vía Greengrass); **GuardDuty** y **AWS Cost Anomaly Detection** se describen como servicios administrados de AWS (sin referencia a ML). Coherente con `Arquitectura_Logica_v6-1.md` §17D, `T-12_ArqFisica.md` RT-14.09 y `Dimensionamiento_Infraestructura_OnPremise_v05.md` §9.15.*

*Documento generado para propuesta formal de arquitectura cloud. Versión 3.6 — Alineación híbrida al 100 % con el segmento on-premise (Modelo B de identidad): Keycloak IdP maestro en nube (ECS Fargate) + caché local A-05 de solo lectura TTL 8 h (VM-05 Talca / VM-C03 Concepción); sin maestro on-premise ni promoción local (ver §3.3, §3.5, §5.4, §7.3, §7.10, L-02, Apéndice C; alineado con `Arquitectura_Fisica_Hibrida_Consolidada_Caso02_v02.md`, `Tabla_Emplazamiento_OnPremise_v06` §A-05 y la decisión D6 de Arquitectura Lógica v1). Versión 3.5 — Alineado con decisiones: Django monolito modular, Keycloak IdP, DynamoDB (IoT raw) + OLAP (S3/Redshift) split, ECS Fargate, FinOps y Reversibilidad. Correcciones v3.1: 5 ambientes/5 cuentas AWS (incluye cuenta DR como 5º ambiente, RT-04.01), retención telemetría reconciliada (DynamoDB TTL 30 días + consolidado analítico 5 años + raw S3 5 años), escalado ECS unificado 2→6 (Django) / 2→4 (Celery), MFA explícito para todo acceso externo (Art. 22°), HSTS con precarga (Art. 21.2), SIEM con casos de uso de negocio y retención de seguridad 12+24 meses (Art. 21.3, RT-11.14/15), AsyncAPI y versionado de contratos (RT-05.16/17, Art. 26), coexistencia de mensajería RabbitMQ/SQS/EventBridge declarada, y justificación explícita del monolito modular frente al rechazo del Cap. 2 (despliegue independiente de módulos críticos). Correcciones de alineación híbrida v3.2 (ver `Arquitectura_Fisica_Hibrida_Consolidada_Caso02_v02.md`): corrección de 5 referencias VM-01 y trío de instancias Keycloak (VM-05, VM-C03 y nube), transporte broker→SQS FIFO vía shipper VM-03 (HTTPS/443 PrivateLink, Zero Trust — AMQPS 5671 solo on-prem↔on-prem), DynamoDB GSI por shipment_id (Punto 6), estrategia de tokens según §5.4 (offline token por perfil: 8 h bodega · 14 h reparto/preventa), mínimo 2 AZ (sa-east-1a/1b, tercera opcional). Correcciones v3.3: declaraciones §5.6 y filas de matriz nuevas para RT-11.06/11.08/11.09/11.13/11.22/11.23/11.24/11.25/11.27 (Cap. 11) y RT-12.06 (Cap. 12), todos Obligatorios validados contra BTT; códigos RT agregados a filas existentes de §7.9; corrección de cita errónea RF-15.05/RT-15.05 → RT-12.10 en §7.10 (el RT-15.05 transversal es intensidad de carbono de la región, Deseable). Correcciones v3.4: cierre de 10 advertencias de auditoría — RT-03.03 (IaC versionada en el repositorio del CLIENTE, §3.4/§7.5/§7.6), RT-11.01 (Zero Trust anclado a NIST SP 800-207, §5.1 + fila §7.9), RT-11.11 (puerta de enlace con cuotas, límites de tasa, validación de esquema e inspección de carga útil, §2.3 + fila §7.9), RT-11.16 (agente EDR en endpoints on-premise integrado al lago de seguridad, fila §7.9), RT-12.01 (integración LDAP con el directorio corporativo del CLIENTE, §5.4 + fila §7.10), RT-12.02 (SSO y logout propagado por OIDC back-channel, §5.4 + fila §7.10), RT-12.05 (ABAC + matriz de segregación de funciones, §5.4 + fila §7.10), RT-12.08 (JWT firmados de vida breve, refresh rotatorio, sin tokens en URL, §5.4), RT-12.09 (auditoría del ciclo de vida de identidad con no repudio y retención, §5.5 + fila §7.10), RT-14.02 (acceso propio y permanente del CLIENTE a tableros con exportación, §6.4). Correcciones v3.5: cierre de las 14 advertencias y 3 huecos propios de la nube de la auditoría — RT-02.03 (vistas ISO/IEC/IEEE 42010, §1), RT-03.09 (análisis comparativo serverless vs. instancias permanentes, §3.2), RT-03.22 (acceso remoto Zero Trust sin VPN tradicional: AWS Verified Access + túnel ZTNA de malla, §5.1 + fila §7.5), RT-07.02 (emplazamiento y análisis de amenazas comunes, §6.2), RT-07.06 (procedimiento de retorno y reconciliación post-contingencia, §6.2), RT-07.08 (automatización SSM de los pasos 4-7, §6.2), RT-07.13 (tiempos de restauración completa por dominio, §7.12), RT-10.02 (clasificación de servicios crítico/alto/medio/bajo con nivel Art. 78, §6.1), RT-11.10 (cifrado a nivel de campo de datos sensibles del caso, §5.3 + fila §7.9), RT-12.04 (FIDO2/WebAuthn para perfiles privilegiados, §5.4 + fila §7.10), RT-12.07 (política de sesión: duración, inactividad, renovación, revocación, concurrentes, §5.4 + fila §7.10), RT-12.12 (registro/verificación/recuperación autoservida de usuarios externos, §5.4 + fila §7.10), RT-12.13 (procedimiento *break-glass* con custodia compartida, §5.5 + fila §7.10), RT-14.06 (RCA de incidentes críticos ≤ 5 días hábiles con seguimiento, §5.5), RT-14.08 (costo de retención en línea vs. archivo, §7.12), RT-15.04/RT-15.05 (intensidad de carbono de la región y comparativa entre regiones, §4.5). Confidencial.*
