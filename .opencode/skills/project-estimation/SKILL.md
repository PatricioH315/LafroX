---
name: project-estimation
description: Estimar esfuerzo y desglosar por rol (nivelación T-15) para la EDT y cronograma de 56 meses del proyecto TFEP-01/2026. Use al dimensionar el plan de trabajo, la EDT, la planificación de hitos y la nivelación del equipo (Formularios T-14/T-15/T-18). Trigger: "estimación", "esfuerzo", "EDT", "cronograma", "nivelación", "T-15", "plan de trabajo", "equipo de trabajo".
---

# project-estimation — Estimación de esfuerzo y nivelación (T-15)

Estima el esfuerzo del proyecto y lo desglosa por rol, coherente con la EDT, el
cronograma contractual obligatorio de **56 meses** (Art. 17°) y el equipo de TI
de **4 personas** (operación/soporte), además del equipo de implantación.

## Estructura del cronograma obligatorio (Art. 17°)

- Etapa 1: meses 1–15 (desarrollo, marcha blanca, producción mes 16).
- Etapa 2: meses 13–20 (producción mes 21).
- Operación: 36 meses (meses 21–56).
- Salidas por etapa: no negociables.

## Principios de estimación (T-15, nivelación)

- Actividades **concretas** de la propuesta, no genéricas (el T-22 evalúa con
  severidad planes que podrían servir a cualquier proyecto).
- Desglose por rol (equipo asignado en `Equipo_y_roles_lafrox.csv`): PM, Arquitecto,
  Seguridad, Datos, Desarrollo, Calidad, SRE, Implantación.
- Nivelar carga: evitar sobre-asignación de un rol en una misma ventana.
- Volumetría del caso como base: 31.000 pedidos/mes, 260.000 líneas, 62
  preventistas, cutover 24 h, marcha blanca gradual.

## Salidas típicas

- EDT (WBS) → hitos → cronograma con fechas del calendario oficial.
- Nivelación de recursos (T-15) y plan de trabajo (T-14/T-18).
- Equipo coherente con las actividades (T-8).

## Verificación

- Fechas del cronograma alineadas con la licitación y sin contradicciones de
  calendario (ver AUDITORIA §2.4).
- No exceder el cronograma de 56 meses ni omitir hitos obligatorios.