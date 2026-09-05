---
name: sre-practices
description: Definir disponibilidad 99,9 %, RTO/RPO, SLOs y observabilidad de la solución TFEP-01/2026 (Caso 02 Logística). Use al dimensionar SLA, planes de servicio en operación, monitoreo y niveles de servicio (Servicios de operación y niveles de servicio), y al justificar la disponibilidad crítica. Trigger: "99,9", "SLA", "RTO", "RPO", "disponibilidad", "SLO", "observabilidad", "niveles de servicio", "monitoreo".
---

# sre-practices — Disponibilidad, RTO/RPO, SLOs y observabilidad

Define los niveles de servicio y la observabilidad de la plataforma, coherentes
con los RT transversales y con la criticidad de la operación logística.

## Cifras y restricciones canónicas

- Disponibilidad objetivo del servicio: **99,9 %** (referencia transversal).
- Ventana crítica de despacho **05:30–07:00** con **cero indisponibilidad**.
- Cutover on-premise: **24 h** (RT-03.10); terreno **14 h sin señal**.
- Prueba de **DR semestral** (Art. 20, RT-07.07).
- Percentil 95 en tiempos de respuesta (RT-09.01).

## RTO/RPO sugeridos (coherentes con on-premise + nube DR)

On-premise por CD:
- RPO = 15 min (WAL streaming a Aurora), RTO = 4 h vía copia local NAS.
- Failover ante caída de chasis Proxmox: rearranque de VMs ≈ 30 s (N+1, Ceph).

## Observabilidad

- Prometheus/Grafana (métricas), ADOT/OpenTelemetry (trazas), CloudWatch/X-Ray
  (log), SSM (gestión saliente, Zero Trust).
- Telemetría IoT (Greengrass → AWS IoT Core MQTTS 8883) con buffer offline.

## Niveles de servicio

- Para el Ítem "Servicios de operación y niveles de servicio" (T-22 Informe 3):
  definir SLOs, SIs y mecanismos de reporte; alinear con RT transversal.
- Incluir Plan Mantención Preventiva/Evolutiva y Plan Servicios de Operación.

## Verificación

- Coherente con disponibilidad 99,9 %, RTO/RPO definidos y prueba DR semestral.
- La observabilidad no debe asumir conectividad permanente (offline-first).