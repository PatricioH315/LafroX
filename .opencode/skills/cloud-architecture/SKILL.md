---
name: cloud-architecture
description: Justificación y diseño de la arquitectura híbrida nube + on-premise del proyecto LafroX según RT-03: selección de servicios AWS (ECS/Fargate, RDS/Aurora PostgreSQL, Redis, DynamoDB, TimescaleDB, Redshift Serverless, Lambda, API Gateway, S3, CloudWatch), Keycloak como IdP maestro, y su contraparte on-premise. Usar cuando el usuario pida justificar, diseñar, elegir o evaluar la nube, AWS, servicios cloud, arquitectura híbrida o despliegue del caso 02.
---

# Cloud Architecture (híbrido nube + on-premise)

Diseño y justificación de la arquitectura híbrida obligatoria (Art. 16) para el
Caso 02. La carga principal vive en nube pública; bodegas del CD y operación de
terreno (preventa, reparto, recepción) requieren componentes on-premise con
capacidad offline.

## Restricciones que condicionan la nube

- **Operación dispersa y de terreno**: 62 preventistas, ~200 conductores,
  14.200 puntos de entrega, rutas rurales sin cobertura y almacenes sin internet.
- **Desconexión**: nominal 2 h; contingencia de diseño un turno completo de 14 h
  (RT-03.10). La sincronización tras reconexión debe cumplir RT-03.12.
- **Ventana crítica de despacho 05:30–07:00** con cero indisponibilidad.
- **Perfil de carga no plano**: preparación nocturna 22:00–06:00 y septiembre
  casi duplica el volumen (3 semanas).

## Decisiones de diseño registradas (2026-09-04, mantener coherencia)

- Nube: **AWS**. Backend monolito modular **Django** (Python 3.12) servido por
  **API Gateway + Lambda/ECS/Fargate**, módulos M1–M12.
- **Keycloak** (realm "Puelche") como IdP maestro en ECS/Fargate; emisión y
  validación de JWT vía Lambda Authorizers; MFA TOTP; clientes OIDC por superficie.
- On-premise: **Keycloak Local Auth Cache / Offline Proxy** (caché de tokens
  JWT, réplica de solo lectura, TTL 8 h, autonomía 24 h del turno nocturno).
- Datos: **PostgreSQL (RDS/Aurora)** como motor relacional principal, **Redis**
  para cache/sesión, **DynamoDB** para telemetría/catálogos de alta escritura,
  **TimescaleDB** para series temporales (telemetría operacional) y
  **Redshift Serverless** para analítica.
- Sin Cognito: Keycloak es la decisión (alternativa documentada, no implementada).

## Criterios de justificación

- Cada servicio elegido se justifica contra un RT o una decisión 16.1
  (trazabilidad, cadena de frío, telemetría como dato operacional — no de control,
  OTIF, costo de servir).
- La elección debe evitar lock-in cuando sea posible y declarar qué componente
  es on-premise y por qué (bodega, contingencia, turno nocturno).
- Dimensionamiento explícito con método y supuestos (Cap. 14.2); celdas vacías =
  no dimensionado.

## Verificación

- Propuesta NO solo-nube ni solo-on-premise.
- Todos los servicios nombrados corresponden a servicios reales de AWS (evitar
  nombres inventados) o herramientas declaradas (Keycloak, Redis).
- Coherente con los `.md` de arquitectura física y con `Diagramas/`.