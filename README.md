# Licitación TFEP-01/2026 — Caso 02 Logística

Propuesta técnico-económica (licitación **ficticia**) para el caso 02 **"Logística"** (Distribuidora Puelche S.A.). Proyecto de la Escuela de Informática PUCV — Taller de Formulación de Proyectos Informáticos (ICI-5444).

Todo el trabajo es **documentación tipo oferta en español** (arquitectura, servicios, requerimientos, planificación, gestión de riesgos), no código.

## Estructura

| Carpeta | Contenido |
|---|---|
| `Bases/` | Documentos rectores y fuente de verdad (precedencia en `AGENTS.md`) |
| `Requerimientos/` | Planillas Excel de requerimientos (catálogo RF / RNF / OP, supuestos, reglas de negocio, trazabilidad, vacíos) |
| `productos/` | Salidas: consultas al mandante, planilla de consultas, registro de decisiones |
| `TrabajosAnteriores/` | Subdocumentos de propuestas previas: referencia de **forma**, no de contenido |
| `Diagramas/` | PNG/SVG/PDF exportados de diagramas para incrustar en `.docx` y PDF |
| `_staging/` | Archivos en tránsito antes de consolidarse en las carpetas definitivas |

## Contexto

- **`AGENTS.md`** — reglas de oro del proyecto (única fuente de verdad). Léelo primero.
- **`CLAUDE.md`** — puntero para usuarios de Claude Code.

## El caso

**Distribuidora Puelche S.A.** — distribuidora de consumo masivo en el centro-sur de Chile: 14.200 puntos de entrega, 62 preventistas, ~200 conductores y una operación de terreno que mezcla preventa, reparto, preparación nocturna y cadena de frío. Los ejes del problema son la **trazabilidad sanitaria** (retiro de lote), la **promesa de entrega** (OTIF) y el **costo de servir**.

## Skills de opencode

Las skills están **versionadas en `.opencode/skills/`** y quedan instaladas al clonar (no dependen de la config global de cada máquina). El skill `licitacion-workflow` orquesta qué skill cargar en cada fase de la propuesta.
