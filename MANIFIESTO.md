# Manifiesto de procedencia y conversión

## Alcance

La conversión se realizó desde el repositorio LafroX vigente. No constituye revisión humana nueva, aprobación del contenido ni sustitución de la revisión formal de los PDF finales.

| Destino | Fuente | Transformación |
| --- | --- | --- |
| `Bases/*.md` | Los cuatro Markdown de `Bases/` | Copia íntegra, sin reescritura. |
| `01_presentacion_empresa/LAFROX-Subdocumento1.md` | `contenido.tex` y `tablas/equipo.tex` | Conversión de estructura, listas y tablas; organigrama transcrito a descripción textual. |
| `01_presentacion_empresa/LAFROX-Subdocumento1-Anexos.md` | `anexos.tex` | Conversión directa. |
| `01_presentacion_empresa/LAFROX-Formulario-T-6.md` | `LAFROX-Formulario-T-6.tex` | Formulario independiente convertido a tabla Markdown. |
| `02_problema_necesidad/LAFROX-Subdocumento2.md` | `contenido.tex`, `tablas/actores.tex` y `tablas/supuestos.tex` | Conversión de estructura, listas y tablas; seis procesos AS-IS transcritos a descripciones textuales. |
| `02_problema_necesidad/LAFROX-Subdocumento2-Anexos.md` | `anexos.tex` | Conversión de los listados detallados a tablas Markdown. |
| `Requerimientos/*.md` | Tres CSV originales de `Requerimientos/` | Conversión fila por fila; campos e identificadores preservados, incluidas celdas vacías. |
| `Revision/prompt_revision_comision_informe2.md` | Prompt vigente del Informe 2 | Se antepusieron reglas para evidencia por archivo/sección y controles pendientes del PDF. El prompt original quedó incorporado como referencia. |
| `compct/CONTEXTO_SESION.md` | Alcance y estado verificados del repositorio | Contexto compacto de reanudación y controles contra afirmaciones sin fuente. |

## Figuras transcritas

Se transcribieron exactamente siete figuras: el organigrama del Subdocumento 1 y los procesos AS-IS de preventa, recepción, cross-docking, planificación de rutas, reparto y rendición del Subdocumento 2. Cada ficha conserva título, fuente, nodos, secuencia, decisiones y excepciones visibles en la fuente.

## Exclusiones deliberadas

No se copiaron arquitectura, Subdocumentos 3–14, históricos, plantillas LaTeX, archivos binarios, herramientas de generación ni `03_esquema_solucion_alcance/tablas/generador/consolidado.json`.

## Incorporación a branch-md

Se importaron los 17 archivos Markdown de la copia local `LafroX-Markdown` a la raíz de `branch-md`, rama del repositorio LafroX. Se actualizaron únicamente AGENTS, README, este manifiesto y el contexto de sesión para reflejar la rama y su prohibición de trabajo en LaTeX. Los documentos, Bases y catálogos se conservaron byte a byte. No se incorporaron los nuevos anexos del Subdocumento 3.
