# Subdocumento 4 — Arquitectura lógica y física de la solución

Formulario T-7 (Bases Administrativas). Un único subdocumento que integra la
arquitectura lógica **y** física de la solución. Debe cubrir:

- Arquitectura lógica: capas, módulos, límites de contexto, responsabilidades e interfaces.
- Arquitectura física: emplazamiento de cada componente en nube y on-premise, con justificación por componente conforme al Artículo 16° (despliegue híbrido obligatorio).
- Arquitectura de integración: servicios, contratos, mensajería, versionado y gobierno.
- Arquitectura de seguridad: Zero Trust, capa expuesta, identidad, cifrado y controles.
- Arquitectura de despliegue: ambientes, redes, alta disponibilidad, DR y respaldos.
- Dimensionamiento y plan de capacidad, con supuestos de volumen, concurrencia y crecimiento.
- Decisiones de arquitectura registradas (ADR), con alternativas y criterio de selección.

> La arquitectura debe ser propia de la solución planteada. No se aceptan diagramas genéricos.

## Contenido de esta carpeta

- `entrega_1/` — snapshot congelado (arquitectura lógica y física entregadas el 07-09-2026). **No se edita.**
  - `texto/arquitectura_logica.md` y `texto/arquitectura_fisica.md`
  - `tablas/arquitectura_fisica_*.xlsx` (ADR, dimensionamiento, despliegue, integración, seguridad, BI)
  - `README_logica.md` y `README_fisica.md` con la ficha original de cada parte.
- `entrega_2/` — versión en construcción para el Informe 2 (05-10-2026).

Los diagramas de arquitectura viven en [`Diagramas/`](../Diagramas/) (raíz del repo).
