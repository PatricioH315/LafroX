---
name: mermaid-diagrams
description: Diagramas Mermaid dentro de los .md del proyecto LafroX (flujo, arquitectura, secuencia, ER, C4, Gantt) que GitHub renderiza nativo, y exportación a PNG/SVG/PDF con mmdc. Usar cuando el usuario pida un diagrama de flujo, secuencia, arquitectura, ER, gantt o gráfico en markdown con mermaid dentro de la propuesta.
---

# Mermaid Diagrams (LafroX)

Creación de diagramas Mermaid versionables en los `.md` del proyecto. Source de
los diagramas = texto en `.md`; exportados en `Diagramas/`.

## Uso

- Bloque `mermaid` dentro del `.md` para render nativo en GitHub.
- Tipos típicos del proyecto:
  - `flowchart` para procesos (preventa, despacho, recepción, devoluciones).
  - `sequenceDiagram` para integraciones EDI y flujos de autenticación OIDC.
  - `erDiagram` para el modelo de datos.
  - `gantt` para el cronograma de 56 meses (Etapas 1/2 y Operación).
  - `classDiagram`/`stateDiagram-v2` para componentes y estados de pedidos.
- Etiquetas en **español**, coherentes con la terminología del caso
  (preventa, OTIF, excursión térmica, canastillos, etc.).

## Exportación

- Con `@mermaid-js/mermaid-cli`: `mmdc -i archivo.mmd -o archivo.svg` (o `-p` PDF,
  `-b white` para fondo).
- Guardar el export en `Diagramas/` con nombre descriptivo.

## Verificación

- Validar la sintaxis antes de exportar (el render de GitHub falla con sintaxis
  rota). Para diagramas grandes (> ~20 nodos), probar render local.
- No usar `mermaid` para UML/C4 formal: usar PlantUML (`plantuml-diagrams`).