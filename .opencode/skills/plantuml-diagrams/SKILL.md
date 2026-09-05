---
name: plantuml-diagrams
description: Crear diagramas UML/C4 formales (.puml) para la propuesta TFEP-01/2026 y renderizarlos a PNG/SVG vía Kroki. Use para C4 de contenedores/componentes y UML formal cuyo fuente exija PlantUML. Trigger: "plantuml", "puml", "kroki", "C4", "diagrama de componentes", "UML".
---

# plantuml-diagrams — Diagramas PlantUML/UML-C4

Crea diagramas PlantUML (.puml) y los renderiza a imagen. Se reserva para UML/C4
formal (p. ej. diagramas de contexto y de contenedores C4). Para flujos/ERse
prefiere Mermaid (ver `mermaid-diagrams` y `AGENTS.md`).

## Exportación vía Kroki

```
curl https://kroki.io/plantuml/svg -d 'delimiter=@d && enc poner la @startuml'
curl https://kroki.io/plantuml/png -d_..._'
```

Regla práctica: enviar el código PlantUML y guardar la imagen en `Diagramas/`.

## Patrón C4 de contexto (referencia Puelche)

```plantuml
@startuml
!theme cerulean-outline
skinparam componentStyle rectangle
actor "Preventista (62)" as A1
rectangle "PLATAFORMA LOGÍSTICA PUELCHE" as P {
  component "Maqueta" as CORE
}
rectangle "Sistemas externos" as EXT {
  component "ERP" as E1
  component "SII / DTE" as E2
  component "EDI canal moderno" as E3
  component "Keycloak IAM" as E7
}
A1 --> CORE
CORE --> E1
CORE --> E7
@enduml
```

## Convenciones

- Codificación UTF-8; tildes conservadas.
- Diagramas de la arquitectura lógica adoptada: 6 capas y 12 módulos M1–M12.
- Registrar el diagrama en `Diagramas/` y su fuente en el `.md`.

## Verificación

- Exportar siempre los `.puml` a imagen (no dejar solo el texto).
- Validar que el C4 de contenedores respete el carácter híbrido y offline.