---
name: pptx
description: Creación de las presentaciones preparatorias del proyecto LafroX con PowerPoint (.pptx): las 3 presentaciones del cronograma de la licitación y apoyos de avance. Usar cuando el usuario pida crear/modificar presentaciones, slides, pptx o ppt del proyecto.
---

# PPTX (presentaciones de la licitación)

Creación de las presentaciones preparatorias de la propuesta LafroX.

## Herramientas

- Python con `python-pptx` para crear/editar `.pptx`.
- Usar una plantilla base limpia: título, diapositiva de sección, contenido con
  figuras de `Diagramas/`/Mermaid exportado, y diapositivas de cierre con
  conclusiones y próximos pasos.

## Presentaciones del cronograma

El calendario de la licitación exige presentaciones preparatorias (3 principales)
que acompañan los informes T-22. Cada presentación debe:

- Resumir el avance de la fase (requerimientos, arquitectura, plan, riesgos).
- Incluir los diagramas clave (arquitectura lógica/física, EDT, flujo de caja).
- Destacar cómo se cumplen las restricciones obligatorias: híbrido (Art. 16),
  56 meses (Art. 17) y las 5 innovaciones obligatorias.
- Cerrar con decisiones tomadas, supuestos declarados y consultas pendientes
  (Art. 43.3).

## Reglas

- Español, formato oficial de la propuesta.
- No usar figuras o cifras que contradigan los `.md` y planillas fuente:
  la presentación es un resumen, no una nueva fuente de verdad.