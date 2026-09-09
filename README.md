# Licitación TFEP-01/2026 — Caso 02 Logística

Propuesta técnico-económica (licitación **ficticia**) para el caso 02 **"Logística"** (Distribuidora Puelche S.A.). Proyecto de la Escuela de Informática PUCV — Taller de Formulación de Proyectos Informáticos (ICI-5444).

Todo el trabajo es **documentación tipo oferta en español** (arquitectura, servicios, requerimientos, planificación, gestión de riesgos), no código.

## Entregas

| Carpeta | Rol | Se edita |
|---|---|---|
| `Entrega 1/` | **Base canónica.** Registro congelado del Informe 1 entregado el 07-09-2026, extraído de `productos/Informe 1 Entrega 1.docx`. Subdocs 1, 2, 3, 4.1, 4.2, 5 y 13 | **no** |
| `Entrega 2/` | Entregable en construcción para el Informe 2 (05-10-2026). Agrega los subdocs 6, 7, 8 y 9 | **sí** |

Todo trabajo para la Entrega 2 parte de la línea base de la Entrega 1, y todo cambio se registra en
`Entrega 2/00_trazabilidad_observaciones/` (Art. 45 · Formulario T-22).

Dentro de cada subdocumento: `texto/` con la narrativa en Markdown y `tablas/` con las tablas como
planillas `.xlsx` (una hoja por tabla). Los diagramas van en carpeta aparte, `Diagramas/` de cada entrega.

## Estructura

| Carpeta | Contenido |
|---|---|
| `Bases/` | Documentos rectores y fuente de verdad (precedencia en `AGENTS.md`) |
| `Requerimientos/` | Catálogos RF/RNF/bases, decisiones, reglas de negocio y supuestos |
| `Arquitectura/logica/`, `Arquitectura/fisica/` | Documentos fuente de arquitectura (no entregables) |
| `Diagramas/` | Biblioteca de diagramas del repositorio, incluida `RT-06_DataCenter/` |
| `rubricas/` | Rúbricas de calificación por entregable |
| `productos/` | El `.docx` de la Entrega 1, formularios T-12 y plantilla de informe |
| `TrabajosAnteriores/` | Propuestas previas: referencia de **forma**, no de contenido |
| `_staging/` | Archivos en tránsito, no versionado |

## Contexto

- **`AGENTS.md`** — reglas de oro del proyecto (única fuente de verdad). Léelo primero.
- **`CLAUDE.md`** — puntero para usuarios de Claude Code.

## El caso

**Distribuidora Puelche S.A.** — distribuidora de consumo masivo en el centro-sur de Chile: 14.200 puntos de entrega, 62 preventistas, ~200 conductores y una operación de terreno que mezcla preventa, reparto, preparación nocturna y cadena de frío. Los ejes del problema son la **trazabilidad sanitaria** (retiro de lote), la **promesa de entrega** (OTIF) y el **costo de servir**.

## Skills de opencode

Las skills están **versionadas en `.opencode/skills/`** y quedan instaladas al clonar (no dependen de la config global de cada máquina). El skill `licitacion-workflow` orquesta qué skill cargar en cada fase de la propuesta.
