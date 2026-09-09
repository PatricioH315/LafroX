---
name: licitacion-workflow
description: Orquestador del flujo de trabajo de la licitación TFEP-01/2026 (Caso 02 Logística, Distribuidora Puelche). Use siempre, al iniciar cualquier avance de la propuesta, para saber qué skill activar en cada fase y qué entregable producir. Gate: es el skill raíz del proyecto; cárguelo antes de cualquier tarea de la propuesta.
---

# Licitación Workflow — TFEP-01/2026 (Caso 02 Logística)

Orquesta el proyecto de formulación de la propuesta técnico-económica para la
licitación pública ficticia **TFEP-01/2026** del caso **02 — Logística**
(Distribuidora Puelche S.A.), asignado en el taller ICI-5444 (PUCV).

**Objetivo.** Producir la documentación de oferta (arquitectura, servicios,
requerimientos, planificación, evaluación de riesgos y oferta económica)
coherente con las Bases, el caso y el cronograma obligatorio de 56 meses.

**Regla de oro:** al comenzar cualquier sesión/avance, cargar este skill.
Él decide el siguiente skill a activar según la fase en curso.

## Base canónica: la Entrega 1 (verificar antes de cualquier avance)

**`Entrega 1/` es el punto de partida obligatorio de la Entrega 2.** Es el registro congelado
de lo entregado el 07-09-2026, extraído de `productos/Informe 1 Entrega 1.docx`.

| Carpeta | Rol | Se edita |
|---|---|---|
| `Entrega 1/` | registro de lo entregado — subdocs 1, 2, 3, 4.1, 4.2, 5, 13 | **no, nunca** |
| `Entrega 2/` | entregable en construcción (Informe 2, 05-10-2026) | **sí, aquí se trabaja** |

Antes de redactar o modificar cualquier subdocumento:

1. **Leer la línea base** en `Entrega 1/<NN_subdoc>/texto/` y `.../tablas/`. Nunca partir de cero
   ni de otra fuente si el subdocumento ya existe ahí.
2. **Escribir el cambio en `Entrega 2/<NN_subdoc>/`**, jamás en `Entrega 1/`.
3. **Registrar el cambio** en `Entrega 2/00_trazabilidad_observaciones/tablas/Trazabilidad_Observaciones_Informe1.xlsx`
   con la observación que lo motiva y la sección modificada. Sin esa fila, el T-22 lo lee como
   observación no atendida (Art. 45).
4. Ante duda sobre **qué se entregó**, manda `Entrega 1/` y su origen, el `.docx`. Lo que no está
   en el `.docx` es material de trabajo, no entregable.

Subdocumentos **nuevos** del Informe 2 (sin línea base porque el Informe 1 no los cubría):
`07_metodologias` (6), `08_plan_trabajo_edt` (7), `09_plan_riesgos` (8), `10_plan_calidad` (9).
Pesan en conjunto **41 %** de la ponderación del Informe 2 (T-21).

**El proyecto LaTeX fue retirado por desactualizado.** No reintroducirlo ni usarlo como fuente.

## Cómo se leen los documentos rectores (precedencia)

Precedencia estricta (Art. 5° de las Bases Administrativas):

1. `Bases/Bases_Administrativas.md` — proceso, contrato, cronograma 56 meses, modelo híbrido.
2. `Bases/Bases_Tecnicas_Transversales.md` — requisitos técnicos codificados **RT-CC.NN** (Obligatorio / Deseable / Según caso).
3. `Bases/Caso_02_Logistica.md` — la narrativa del caso; se traduce a alcance/arquitectura/plan.

El caso puede **endurecer** un transversal, nunca rebajarlo. Ver `AGENTS.md` para
las reglas innegociables (híbrido, offline-first, Zero Trust, 56 meses, 5 innovaciones).

Convención de habilidades: cada habilidad referida aquí vive en
`.opencode/skills/<nombre>/SKILL.md`. Si una no existe al cargarla, avisar a
LafroX (no inventarla).

## Fases y habilidades a activar

### Fase 0 — Preparación y contexto (siempre al iniciar)
Cargar `licitacion-workflow`. Leer `AGENTS.md`, `compct/CONTEXTO_SESION.md`,
`AUDITORIA.md` y las fuentes de `Bases/`. Establecer el estado actual.

### Fase 1 — Comprensión del caso (problema y necesidad)
- **Habilidades:** `deep-research` (normativa GS1, DTE, RSA, cadena de frío, OTIF, ruteo).
- Salida: lectura del caso §2–§16; identificación de dolores, contradicciones y vacíos.
- Referencia: `AUDITORIA.md` §2 (checklist de integridad).

### Fase 2 — Catálogo de requerimientos y reglas de negocio (Cap. 17.1)
- **Habilidades:** `xlsx` (leer/consolidar planillas de requerimientos), `technical-writing`.
- Salida: catálogo RF/RNF/Bases con trazabilidad a origen; registro de supuestos
  (decisiones 16.1 D1–D40); reglas de negocio; matriz de trazabilidad.
- Recursos: `Requerimientos/*.csv`, `Requerimientos/reglas_de_negocio.md`, `Requerimientos/decisiones.md`.

### Fase 3 — Arquitectura de la solución
- **Habilidades:** `architecture-diagrams`, `mermaid-diagrams`, `plantuml-diagrams`,
  `cloud-architecture`, `sre-practices`.
- Salida: arquitectura lógica y física (Informe 1, Subdocs 4.1/4.2), modelo y
  gestión de datos (Subdoc 5), evidenciando el carácter híbrido (Art. 16°).
- Regla: aplicar la política de fuente de verdad tecnológica de `AGENTS.md`.

### Fase 4 — Planificación, alcance y riesgos (Informes 2)
- **Habilidades:** `project-estimation`, `risk-assessment` (y `legal-risk-assessment`
  para el contractual), `technical-writing`.
- Salida: EDT, cronograma de 56 meses alineado con el Art. 17°, equipo (T-8/T-15),
  hitos, planes de riesgo/calidad (T-13/T-16/T-17).

### Fase 5 — Oferta económica y consolidación (Informe 3)
- **Habilidades:** `xlsx`, `technical-writing`, `pdf-handling`.
- Salida: curva S, análisis de costos, VAN/TIR, valorización de las 5 innovaciones,
  flujo de caja mensual, planilla de cálculo económica del CLIENTE.

### Fase 6 — Presentaciones preparatorias (Informes 1, 2 y 3 según T-22)
- **Habilidades:** `pptx`, `technical-writing`, `pdf-handling`.
- Salida: presentación + informe por instancia, conforme al Formulario T-22
  (contenido exigido y subdocumentos adjuntos).

### Transversal — Formularios oficiales .docx y exportación PDF
- **Habilidades:** `docx` (formularios de los sobres, T-6/11/12/14/15/18…,
  nomenclatura Art. 43.3), `pdf-handling`.
- Regla: los diagramas viven como texto (Mermaid/PlantUML) y se exportan a
  `Diagramas/` (PNG/SVG/PDF) con Mermaid por defecto y PlantUML para UML/C4 formal.

## Matriz hitos → habilidades

| Hito / entregable | Habilidades |
|---|---|
| Informe 1 (07-09-2026): Presentación empresa, problema, esquema+alcance, arq. lógica/física, datos, innovaciones | `architecture-diagrams`, `mermaid-diagrams`, `plantuml-diagrams`, `cloud-architecture`, `sre-practices`, `technical-writing`, `docx`, `pptx` |
| Informe 2: correcciones I-1, riesgos, EDT, planificación/hitos | `project-estimation`, `risk-assessment`, `technical-writing`, `docx`, `pptx` |
| Informe 3: proveedores, adquisiciones, curva S, costos, VAN/TIR, innovaciones valorizadas | `xlsx`, `technical-writing`, `docx`, `pptx`, `pdf-handling` |

## Reglas de verificación

- Coherencia de cifras y plazos con el cronograma obligatorio y la volumetría del caso.
- Trazabilidad: requisito RT → módulo → entregable → prueba → criterio de aceptación.
- Respetar precedencia y no corregir unilateralmente las inconsistencias de las Bases.
- Toda respuesta visible inicia con `## LafroX` (protocolo de sesión).