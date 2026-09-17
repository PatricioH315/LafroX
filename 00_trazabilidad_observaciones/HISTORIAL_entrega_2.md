# Entrega 2 — Informe 2

**Licitación TFEP-01/2026 · Caso 02 — Logística (Distribuidora Puelche S.A.) · LafroX**
**Fecha de entrega: 05-10-2026** (Formulario T-20, actividad N.º 8)


## Qué es esta carpeta

El consolidado de la Entrega 2, con el contenido **descompuesto en archivos separados**:
el texto de cada subdocumento en Markdown, sus tablas como planillas `.xlsx` (una hoja por tabla)
y **todos los diagramas en una carpeta aparte**.


El contenido heredado proviene de `productos/Informe 1 Entrega 1.docx`, que es el criterio
de qué se conserva. Las carpetas nuevas (subdocs. 6, 7, 8 y 9) nacen vacías porque el Informe 1
no las cubría.


## Alcance del Informe 2 (Formulario T-22)

Subdocumentos **1, 2, 3, 4, 5, 6, 7, 8, 9 y 13**, más la tabla de trazabilidad
observación → respuesta → sección exigida por el Art. 45.


Agenda cerrada del T-22 para esta instancia:

1. Correcciones del Informe 1, con tabla de trazabilidad.
2. Análisis de riesgo de la solución.
3. Análisis de riesgo del desarrollo del proyecto.
4. Análisis de riesgo de implantación.
5. EDT del proyecto y equipo de trabajo, coherente con las actividades.
6. Planificación e hitos alineados al cronograma obligatorio de 56 meses (Art. 17).


## Estructura

| Carpeta | Subdoc. | Texto | Planillas | Hojas |
|---|---|---|---|---|
| `00_trazabilidad_observaciones/` | — | — | 1 | 2 |
| `01_presentacion_empresa/` | 1 | 1 | 1 | 1 |
| `02_problema_necesidad/` | 2 | 1 | 1 | 5 |
| `03_esquema_solucion_alcance/` | 3 | 1 | 1 | 14 |
| `04_arquitectura_logica/` | 4.1 | 1 | — | — |
| `05_arquitectura_fisica/` | 4.2 | 1 | 7 | 115 |
| `06_modelo_datos/` | 5 | 1 | 1 | 11 |
| `07_metodologias/` | 6 | — | — | — |
| `08_plan_trabajo_edt/` | 7 | — | — | — |
| `09_plan_riesgos/` | 8 | — | — | — |
| `10_plan_calidad/` | 9 | — | — | — |
| `11_innovaciones/` | 13 | 1 | — | — |
| `Diagramas/` | — | — | — | 15 imágenes rescatadas del `.docx` |
| `Formularios/` | — | — | — | índice de control T-6 … T-19 |

Cada carpeta lleva su propio `README.md` con lo que exige el T-22, su ponderación en el T-21
y su estado actual.


## Convención dentro de cada subdocumento

| Subcarpeta | Contenido |
|---|---|
| `texto/` | Narrativa en Markdown. Las tablas aparecen como referencia `> **Tabla N** — …` que apunta a la planilla |
| `tablas/` | Planillas `.xlsx`, **una hoja por tabla**, con el título de la sección de origen en la fila 1 |

Los diagramas no se guardan dentro de los subdocumentos: viven en `Diagramas/`.


## Reglas que condicionan todo (no negociables)

- **Cronograma de 56 meses** (Art. 17): Etapa 1 meses 1–15 (producción mes 16), Etapa 2 meses 13–20
  (producción mes 21), operación meses 21–56.
- **Despliegue híbrido obligatorio** (Art. 16): nube pública + componentes on-premise. No se admiten
  propuestas solo-nube ni solo-on-premise.
- **Precedencia** (Art. 5): Bases Administrativas > Bases Técnicas Transversales > Caso 02. El caso
  puede endurecer un requisito transversal, nunca rebajarlo.
- La presentación preparatoria es **obligatoria**: no presentar deja fuera del proceso.


## Trazabilidad de la extracción

`_manifiesto_extraccion.tsv` registra, pieza por pieza, de qué sección del `.docx` salió cada
archivo generado.
