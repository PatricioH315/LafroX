---
name: architecture-diagrams
description: Diseño de diagramas de arquitectura del proyecto LafroX (lógica, física, datos, seguridad y despliegue) con Mermaid por defecto, PlantUML para UML/C4 formal y draw.io para interactivo. Usar cuando el usuario pida diagramar, dibujar, maquetar la arquitectura, capas, componentes, despliegue híbrido o pedir un diagrama de arquitectura del caso 02.
---

# Architecture Diagrams (LafroX)

Diagramas de la propuesta de arquitectura para el Caso 02 (Distribuidora Puelche).
Toda arquitectura debe ser **híbrida obligatoria** (Art. 16): nube pública +
componentes on-premise.

## Reglas de selección

| Tipo | Herramienta | Dónde se ve | Export |
|---|---|---|---|
| Flujo, arquitectura, secuencia, ER, C4 | **Mermaid** (`mermaid` en `.md`) | GitHub renderiza nativo | `mmdc -i x.mmd -o x.svg/png` |
| UML/C4 formal, componente | **PlantUML** (`.puml`) | Exportar a imagen | `curl https://kroki.io/plantuml/png` |
| Interactivo/animado | draw.io | HTML en navegador | screenshot → PNG |

La **fuente de los diagramas es texto** en los `.md` (versionable). Los PNG/SVG/PDF
exportados van a `Diagramas/`.

## Capas esperadas

- **Lógica**: módulos del monolito modular (M1–M12, Django), actores funcionales,
  canal EDI, integraciones (preventa, WMS, ERP, telemetría operacional).
- **Física**: emplazamiento híbrido — nube AWS (+ Keycloak como IdP, RDS/Aurora
  PostgreSQL, Redis, DynamoDB, TimescaleDB, Redshift Serverless) y on-premise
  (bodega del CD, contingencias sin conexión, turno nocturno 14 h).
- **Datos**: modelo conceptual/lógico por dominio; capa de cache (Redis) y
  analítica separada.
- **Seguridad**: Keycloak (realm Puelche, JWT/OIDC), MFA, Zero Trust, cifrado;
  postura por capa.
- **Despliegue**: ambientes (según transversales: 5 + DR), pipelines, DR semestral.

## Verificación

- El diagrama cumple híbrido (Art. 16) y 56 meses (Art. 17) si aplica fases.
- Las cifras de contexto (volumetría) usan los valores del Cap. 15.
- La fuente Mermaid/PlantUML se valida antes de exportar (`mmdc`/Kroki con
  sintaxis correcta).
- El diagrama final editado se guarda en `Diagramas/` y su fuente en el `.md`
  correspondiente.