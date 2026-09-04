---
name: sre-practices
description: Disponibilidad, confiabilidad y observabilidad de la propuesta LafroX: 99,9 % de disponibilidad, RTO/RPO, SLOs, monitoreo, alertas, prueba de DR semestral (Art. 20) y operación de la ventana crítica de despacho. Usar cuando el usuario pida disponibilidad, SLO, SLA, RTO, RPO, DR, recuperación ante desastres, observabilidad, monitoreo, alertas o continuidad operacional del caso 02.
---

# SRE Practices (confiabilidad del Caso 02)

Definición de los compromisos de servicio y operación de la propuesta.
Cumple los transversales RT-07/RT-09 y el Art. 20 (prueba DR semestral).

## Compromisos base

- **Disponibilidad 99,9 %** de los servicios críticos (RT-09.01, percentil 95 en
  tiempos de respuesta).
- **Cero indisponibilidad en la ventana crítica de despacho 05:30–07:00**.
- **RTO/RPO** definidos explícitamente por componente (nube vs on-premise) y
  alineados con la prueba de DR semestral (RT-07.07).
- **5 ambientes obligatorios + DR** (transversales §4.1, RT-04.01), incluyendo el
  ambiente de Recuperación ante Desastres.
- **Contingencia de 14 h sin señal** (RT-03.10): el sistema debe operar un turno
  completo en modo desconectado y sincronizarse al reconectar (RT-03.12).

## Qué diseñar

- SLOs por servicio (disponibilidad, latencia p95, integridad de datos
  sincronizada, OTIF como indicador de negocio).
- Observabilidad: logs, métricas y trazas (CloudWatch u on-premise), dashboards
  de la operación de terreno (despacho, entregas, contingencias).
- Alertas por excursión térmica, desviación de ruta (telemetría como **dato
  operacional**, no de control) y pérdida de conectividad en bodega.
- Plan de DR: RTO/RPO por componente, prueba semestral documentada, y declaración
  de quién ejecuta el failover en on-premise.

## Verificación

- Los números (99,9 %, RTO/RPO, p95) aparecen coherentes en todos los documentos.
- La DR cumple el Art. 20 (dos veces al año) y RT-07.07.
- No se promete monitoreo de control de conductores (fricción sindical): la
  telemetría se enmarca como registro operacional con finalidad de respaldo.