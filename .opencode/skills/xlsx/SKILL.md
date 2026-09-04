---
name: xlsx
description: Trabajo con planillas Excel de la propuesta LafroX: catálogo de requerimientos (RF/RNF/OP), registro de supuestos y reglas de negocio, matriz de trazabilidad, matriz de cumplimiento T-12, nivelación T-15, oferta económica (CLP/UF/USD) y flujo de caja. Usar cuando el usuario pida crear/modificar planillas, tablas Excel o xlsx dentro del proyecto (requerimientos, volumetría, oferta económica, flujo de caja, costo de servir).
---

# XLSX (planillas de la licitación)

Generación y mantención de las planillas Excel del proyecto LafroX. Todo en
español; los montos requieren formato CLP/UF/USD explícito y coherencia con el
flujo de caja de 56 meses.

## Herramientas

- Python con `openpyxl` (o `pandas` + `openpyxl`) para leer/escribir `.xlsx`.
- Preservar encabezados, anchos de columna, formato de números y hojas existentes.
- Verificar el resultado releyendo el archivo tras escribirlo (celdas, fórmulas, hojas).

## Planillas del proyecto

| Planilla | Contenido esencial |
|---|---|
| Catálogo RF/RNF/OP | ID, tipo, descripción, origen (párrafo/entrevista/indicador/restricción), RT asociado, prioridad |
| Registro de supuestos | Incluir obligatoriamente las 16 decisiones del numeral 16.1 del caso |
| Reglas de negocio | Captura, punto del proceso, responsable, consecuencia si se incumple (Cap. 17.1) |
| Matriz de trazabilidad | Origen → requerimiento → componente → EDT → prueba → criterio de aceptación |
| Matriz T-12 | Respuesta uno a uno contra los RT-CC.NN transversales (código correcto) |
| Nivelación T-15 | Esfuerzo por rol, dedicación y meses (roles del `TrabajosAnteriores/Equipo_y_roles_lafrox.csv`) |
| Oferta económica | Precios en CLP/UF/USD, desglose por ítem y etapa |
| Flujo de caja | 56 meses, hitos de las Etapas 1 y 2 y Operación |

## Reglas de contenido

- **Volumetría real del caso** (Cap. 15): ninguna cifra inventada o contradictoria
  (14.200 clientes, 31.000 pedidos-mes, 260.000 líneas, 2,4 M unidades-mes, etc.).
- **Cronograma 56 meses innegociable** (Art. 17).
- **Trazabilidad**: cada requerimiento debe referenciar su RT y su origen.
- Si un dato no está definido, dejarlo como celda vacía o marcarlo como supuesto —
  nunca rellenar con valores inventados sin marca.