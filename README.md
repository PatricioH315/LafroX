# Licitación TFEP-01/2026 — Caso 02 Logística

Propuesta técnico-económica (licitación **ficticia**) para el caso 02 **"Logística"** (Distribuidora Puelche S.A.). Proyecto de la Escuela de Informática PUCV — Taller de Formulación de Proyectos Informáticos (ICI-5444).

Todo el trabajo es **documentación tipo oferta en español** (arquitectura, servicios, requerimientos, planificación, gestión de riesgos), no código.

## Organización por subdocumento (Formulario T-7)

El repositorio ya **no** se separa por entregas. La estructura primaria son los **14 subdocumentos** de la Propuesta Técnica exigidos por el Formulario T-7 de las Bases Administrativas. Dentro de cada subdocumento conviven las distintas iteraciones como subcarpetas `entrega_1/`, `entrega_2/`, etc.

| # | Carpeta | Estado |
|---|---|---|
| 1 | `01_presentacion_empresa/` | `entrega_1` + `entrega_2` |
| 2 | `02_problema_necesidad/` | `entrega_1` + `entrega_2` |
| 3 | `03_esquema_solucion_alcance/` | `entrega_1` + `entrega_2` |
| 4 | `04_arquitectura/` (lógica **y** física, un solo subdoc en T-7) | `entrega_1` + `entrega_2` |
| 5 | `05_modelo_datos/` | `entrega_1` + `entrega_2` |
| 6 | `06_metodologias/` | `entrega_2` |
| 7 | `07_plan_trabajo_edt/` | `entrega_2` |
| 8 | `08_plan_riesgos/` | `entrega_2` |
| 9 | `09_plan_calidad/` | `entrega_2` |
| 10 | `10_operacion_niveles_servicio/` | pendiente |
| 11 | `11_planes_operacion/` | pendiente |
| 12 | `12_equipo_subcontrataciones/` | pendiente |
| 13 | `13_innovaciones/` | `entrega_1` + `entrega_2` |
| 14 | `14_ventajas_beneficios_consolidacion/` | pendiente |

Dentro de cada `entrega_N/`: `texto/` con la narrativa en Markdown y `tablas/` con las tablas como planillas `.xlsx` (una hoja por tabla). Cada subdocumento tiene su propio `README.md` con el detalle del T-7 y la ficha original.

**Regla dura**: `entrega_1/` es el registro congelado del Informe 1 entregado el 07-09-2026 y **no se edita**. Todo cambio para el Informe 2 vive en `entrega_2/` y queda registrado en [`00_trazabilidad_observaciones/`](00_trazabilidad_observaciones/) (Art. 45 · Formulario T-22).

## Transversales

| Carpeta | Contenido |
|---|---|
| `00_trazabilidad_observaciones/` | Registro de observaciones y respuestas entre entregas, historial y manifiesto de extracción |
| `Bases/` | Documentos rectores y fuente de verdad (precedencia en `AGENTS.md`) |
| `Requerimientos/` | Catálogos RF/RNF/bases, decisiones, reglas de negocio y supuestos |
| `Arquitectura/logica/`, `Arquitectura/fisica/` | Documentos fuente de arquitectura (no entregables) |
| `Diagramas/` | Biblioteca completa: los 15 diagramas del Informe 1 y el material de trabajo del repo |
| `Formularios/` | Formularios técnicos y económicos (T-8, T-9, T-10, T-13, T-14, T-19, T-21, etc.) |
| `Rúbricas/` | Rúbricas de calificación por entregable |
| `Productos/` | El `.docx` de la Entrega 1, formularios T-12, presentación y narración de la Presentación 1 |
| `Trabajos Anteriores/` | Propuestas previas: referencia de **forma**, no de contenido |
| `_staging/` | Archivos en tránsito, no versionado |

## Contexto

- **`AGENTS.md`** — reglas de oro del proyecto (única fuente de verdad). Léelo primero.
- **`CLAUDE.md`** — puntero para usuarios de Claude Code.

## El caso

**Distribuidora Puelche S.A.** — distribuidora de consumo masivo en el centro-sur de Chile: 14.200 puntos de entrega, 62 preventistas, ~200 conductores y una operación de terreno que mezcla preventa, reparto, preparación nocturna y cadena de frío. Los ejes del problema son la **trazabilidad sanitaria** (retiro de lote), la **promesa de entrega** (OTIF) y el **costo de servir**.

## Skills de opencode

Las skills están **versionadas en `.opencode/skills/`** y quedan instaladas al clonar (no dependen de la config global de cada máquina). El skill `licitacion-workflow` orquesta qué skill cargar en cada fase de la propuesta.
