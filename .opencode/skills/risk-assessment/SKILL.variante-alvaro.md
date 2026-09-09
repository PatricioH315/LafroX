---
name: risk-assessment
description: Evaluación de riesgos técnicos y de proyecto de la propuesta LafroX (Caso 02 Logística): merma 1,7 %, conteo cíclico 2,3 %, OTIF 82,4 %, telemetría y fricción sindical, integración con ERP/WMS heredados, contingencia de 14 h sin señal, septiembre con volumen duplicado. Usar cuando el usuario pida riesgos técnicos, matriz de riesgos, amenazas, mitigaciones o análisis de riesgo del proyecto/caso 02.
---

# Risk Assessment (riesgos técnicos y de proyecto)

Matriz de riesgos técnicos y de gestión para el Caso 02, con probabilidad,
impacto y mitigación. Coherente con la operación dispersa y de terreno.

## Riesgos de contexto a considerar

- **Trazabilidad sanitaria**: origen en la recepción (Cap. 8 Calidad). Retiro
  sanitario < 2 h con 100 % de lote (Cap. 18). Mitigación: registro continuo de
  temperatura y lote desde recepción hasta entrega.
- **Inventario**: diferencia de conteo cíclico 2,3 % y merma por vencimiento
  1,7 %. Mitigación: WMS moderno, asignación de ubicaciones, política de
  vencimiento y envases retornables (68.000 canastillos / 9.400 pallets, 14 %
  pérdida).
- **OTIF base 82,4 %**: 82,4 % entregas completas y a tiempo. Mitigación: ruteo
  con ventanas de tiempo, preventa con stock/crédito, cero pedidos perdidos o
  duplicados.
- **Telemetría y sindicato**: la telemetría se usa como **dato operacional, no de
  control**; se declara el riesgo de fricción sindical y se comunica el marco de
  uso preventivamente.
- **Legado**: ERP con preventa de proveedor desaparecido, WMS 2013, planillas y
  papel. Mitigación: integraciones por capas, canal EDI para retail (RF-12,
  exigencia 2029), migración gradual por Etapas 1 y 2.
- **Conectividad**: rutas rurales y almacenes sin internet; contingencia 14 h
  (RT-03.10) y sincronización RT-03.12.
- **Estacionalidad**: septiembre casi duplica el volumen; dimensionamiento por
  peak, no por promedio.

## Formato de la matriz

| Riesgo | Prob. | Impacto | Nivel | Mitigación | Responsable | Trazabilidad (RT/decisión) |

- Todo riesgo se traza a un RT, decisión 16.1 o párrafo del caso.
- Las mitigaciones se reflejan en arquitectura, EDT y plan de pruebas.