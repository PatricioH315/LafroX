---
name: docx
description: Llenar y generar documentos Word (.docx) blancos, formularios oficiales de los sobres y entregables del proyecto TFEP-01/2026. Use cuando haya que crear, completar o editar formularios T-*, documentos de consulta al mandante (Art. 43.3), resúmenes ejecutivos o informes en formato Word con nomenclatura oficial. Trigger: "docx", "word", "formulario", "sobre", "consulta al mandante", "plantilla .docx".
---

# docx — Formularios y documentos Word

Genera y completa documentos `.docx` para la licitación TFEP-01/2026 (Caso 02
Logística): formularios oficiales de los sobres, documentos de consulta al
mandante y otros entregables previstos en Word.

## Formularios oficiales (Formulario/subre de la licitación)

Llenar según las Bases Administrativas y el caso. Formularios relevantes:

- T-6  (presentación de la empresa)
- T-8  (equipo de trabajo, subcontrataciones y alianzas)
- T-9  (metodología de gestión de proyectos)
- T-10 (metodología de desarrollo de software)
- T-11 (arquitectura física / especificaciones implementos y datacenters)
- T-12 (esquema de solución y alcance)
- T-13 / T-17 (plan de calidad)
- T-14 / T-15 / T-18 (plan de trabajo, EDT, cronograma)
- T-16 (plan de riesgos)
- T-19 (innovaciones)
- T-20 / T-21 / T-22 (proceso/evaluación/contenido — leer, no llenar)

## Convenciones de nomenclatura (Art. 43.3)

- Identificador oficial de la licitación: **TFEP-01/2026**.
- Archivos de consultas/entregables con la nomenclatura que exige el Art. 43.3.
- No usar «FEP01.26»/«FEP02.26» (inconsistencia de Bases); estandarizar a TFEP-01/2026.

## Contenido por tipo de documento

- **Consulta al mandante (Art. 43.3):** cada vacío/inconsistencia de las Bases se
  plantea como consulta fundada. No corregir unilateralmente las inconsistencias
  listadas en `AGENTS.md`; son candidatas a consulta/supuesto/decisión.
- **Resumen ejecutivo:** problema dimensionado con datos cuantitativos, supuestos
  del análisis y datos de apoyo referenciados; no mezclar con la solución.
- **Informes (T-22):** respetar la estructura de subdocumentos para cada instancia.

## Buenas prácticas de escritura académica/técnica

- Redacción en español, formal y sin ambigüedad.
- Tablas y referencias coherentes; trazabilidad de requerimientos.
- No incluir fórmulas genéricas ni diagramas genéricos que valgan para cualquier proyecto.

## Verificación

- Validar contra la plantilla oficial (no inventar campos); conservar la estructura.
- Revisar ortografía, cifras (cronograma 56 meses, volumen del caso) y encabezados.