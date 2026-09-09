---
name: plantuml-diagrams
description: Diagramas PlantUML formales (.puml) del proyecto LafroX para UML/C4 (componente, clase, secuencia, estado) renderizados a PNG/SVG vía Kroki o plantuml local, y guardados en Diagramas/. Usar cuando el usuario pida UML, C4 formal, diagrama de componentes, clases, secuencia formal o .puml dentro de la propuesta.
---

# PlantUML Diagrams (LafroX)

Diagramas UML/C4 formales en PlantUML. Fuente `.puml` versionable; export a
`Diagramas/` como PNG/SVG.

## Uso

- `.puml` en el repo (carpeta `Diagramas/` o junto al `.md` que lo documenta).
- Render: `curl https://kroki.io/plantuml/png` con el contenido codificado, o
  `plantuml` local si está instalado.
- Tipos útiles del proyecto:
  - **C4 component/container**: el monolito modular Django, API Gateway,
    Lambda, Keycloak, Redis, Aurora/PostgreSQL, DynamoDB, TimescaleDB, Redshift,
    y los componentes on-premise (bodega, claves offline).
  - **classDiagram**: modelo de dominio (pedido, lote, temperatura, entrega, envases).
  - **sequenceDiagram formal**: OIDC/Keycloak, EDI con retail, retiro sanitario.
  - **stateDiagram**: ciclo del pedido (toma → confirmación → preparación →
    despacho → entrega → devolución).

## Reglas

- Etiquetas en español.
- Para diagramas de flujo/arquitectura "informales", preferir Mermaid
  (`mermaid-diagrams`); PlantUML queda para UML/C4 formal y de componentes.
- Validar el render (Kroki devuelve error si la sintaxis falla) y guardar el PNG/SVG en `Diagramas/`.