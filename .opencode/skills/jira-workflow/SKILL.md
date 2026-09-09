---
name: jira-workflow
description: Integración opcional con Jira Cloud para la gestión de tareas del proyecto LafroX mediante el MCP de Atlassian (desactivado por defecto en opencode.jsonc). Usar cuando el usuario pida gestionar tareas, issues, épicas o historias en Jira, o activar la integración de Jira Cloud del proyecto.
---

# Jira Workflow (LafroX)

Gestión de tareas del proyecto vía Jira Cloud (opcional). La integración usa el
MCP remoto de Atlassian, **desactivado por defecto** en `opencode.jsonc`.

## Activación

1. En `opencode.jsonc`, poner `"enabled": true` en `mcp.jira` y reiniciar opencode.
2. Autenticarse con la cuenta Atlassian del equipo (flujo authv2 del MCP).
3. Verificar que el servidor MCP `jira` aparezca disponible.

## Uso

- Crear épicas/historias por fase de la propuesta (requerimientos, arquitectura,
  plan, riesgos, oferta) y enlazarlas a los entregables.
- Registrar tareas de auditoría/consolidación de archivos, con responsable por rol
  (equipo del `Equipo_y_roles_lafrox.csv`).
- Sincronizar hitos del cronograma de 56 meses con el tablero (opcional).

## Notas

- Si el MCP no está activado, no insistir: indicar al usuario cómo activarlo.
- No duplicar en Jira la información que ya vive en los `.md`/planillas del repo;
  Jira solo referencia (links) a los entregables.