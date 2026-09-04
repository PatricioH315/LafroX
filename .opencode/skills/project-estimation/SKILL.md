---
name: project-estimation
description: Estimación de esfuerzo, costos y cronograma del proyecto LafroX: EDT/WBS, nivelación T-15 por rol, dedicación y meses, flujo de caja de 56 meses, fases Etapa 1 (meses 1-15) y Etapa 2 (meses 13-20) y Operación (21-56). Usar cuando el usuario pida estimar esfuerzo, costos, duración, EDT, cronograma, nivelación de recursos, carta Gantt o planificación temporal del caso 02.
---

# Project Estimation (esfuerzo y cronograma)

Estimación de esfuerzo, costos y planificación de la propuesta, alineada al
cronograma obligatorio de 56 meses (Art. 17).

## Cronograma obligatorio (innegociable)

- **Etapa 1**: meses 1–15 (desarrollo, marcha blanca; producción mes 16).
- **Etapa 2**: meses 13–20 (producción mes 21).
- **Operación**: 36 meses (meses 21–56).

## Entregables de estimación

- **EDT/WBS** desglosada hasta nivel de paquetes de trabajo, trazable a los
  requerimientos y a las 5 innovaciones obligatorias.
- **Nivelación T-15**: esfuerzo por rol (roles del CSV `Equipo_y_roles_lafrox.csv`),
  dedicación (%), meses de participación, y carga nivelada (sin picos irreales).
- **Flujo de caja** de 56 meses por etapa/hito, coherente con la oferta económica.
- Dimensionamiento de la volumetría del sistema (Cap. 14.2) con método y supuestos
  explícitos; celdas vacías = no dimensionado.

## Reglas

- No inventar cifras: derivar de la volumetría del Cap. 15 (14.200 clientes,
  31.000 pedidos-mes, 260.000 líneas, 2,4 M unidades-mes, 62 preventistas,
  ~200 conductores, 14.200 puntos de entrega) y de los hitos del Art. 17.
- Septiembre duplica el volumen: planificar capacidad para el peak, no para el promedio.
- La estimación debe sustentar el flujo de caja y la oferta económica (T-15).