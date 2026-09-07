---
name: architecture-diagrams
description: Diseñar y auditar diagramas de arquitectura (lógica, física, datos, seguridad, despliegue) del proyecto TFEP-01/2026 cumpliendo la política de fuente de verdad tecnológica de AGENTS.md. Use al elaborar o revisar cualquier diagrama de arquitectura de la solución Puelche (híbrida nube+on-premise). Trigger: "arquitectura", "diagrama de arquitectura", "6 capas", "fuente de verdad tecnológica", "renderizado de diagramas".
---

# architecture-diagrams — Diagramas de arquitectura

Diseña, renderiza y audita los diagramas de arquitectura de la solución (Caso 02
Logística, Distribuidora Puelche). Cubre arquitectura lógica, física, de datos,
de seguridad y de despliegue, con carácter **híbrido obligatorio (Art. 16°)**.

## Selección de herramienta (regla de AGENTS.md)

| Tipo de diagrama | Herramienta |
|---|---|
| Flujo, arquitectura, secuencia, ER, C4 | **Mermaid** (fuente en `.md`) |
| UML/C4 formal, componente | **PlantUML** (`.puml`) |
| Interactivo/animado | HTML en navegador → screenshot PNG |

- La fuente de los diagramas es **texto** dentro de los `.md` de la propuesta.
- Los exportados se guardan en `Diagramas/`.
- Mermaid por defecto; PlantUML para UML/C4 formal.

## Arquitectura lógica adoptada (fuente de verdad tecnológica)

Según decisión LafroX 2026-09-03:

- **Stack lógico (adoptado):** Keycloak (OIDC/MFA), Laravel PHP (monolito modular,
  API Gateway), Angular+Tailwind + Flutter (preventa/reparto offline), Redis,
  RabbitMQ, PostgreSQL+PostGIS on-prem por CD, TimescaleDB, Aurora/RDS analítica
  nube, S3, Kubernetes multi-zona + Terraform (IaC), Prometheus/Grafana.
- **6 capas:** Cliente/Actores → Presentación → Negocio (12 módulos M1–M12) →
  Cache/Offline/Mensajería → Datos (híbrida) → Servicios externos.
- Evidenciar offline-first, Zero Trust, multi-zona IaC, sin vendor lock-in,
  mantenible por equipo TI de 4 personas.

## Arquitectura física (en revisión por separado)

- La física (AWS Cognito/Aurora/DynamoDB/Redshift, 8 capas) diverge del lógico.
  No forzar reconciliación con el lógico: marcar divergencia y revisar aparte.
- On-premise: FortiGate HA, Cisco Catalyst, Proxmox N+1 + Ceph, NAS D-05,
  VLANs por sitio (10.x.x.0/24), IoT RS-485/Modbus, 6 sitios.

## Auditoría de diagramas subidos

Al auditar diagramas que lleguen (p. ej. desde `_staging`), aplicar la política de
fuente de verdad tecnológica (ver `AGENTS.md`):

- Extraer las etiquetas de texto de los `.drawio` (`<mxCell value="...">`) para
  leer el contenido real (páginas, actores, capas, stack, conexiones).
- Detectar si un diagrama proviene de otro caso (p. ej. plantillas de Salud) y
  **no** consolidarlo como arquitectura Puelche (error de dominio).
- Verificar actores canónicos (62 preventistas, 42 propios, ~160 externos, 120
  preparadores, 11.600 trad / 500 moderno) y trazado de módulos a RF.
- Registrar veredicto/hallazgos en `AUDITORIA.md`.

## Lo innegociable de verificar en todo diagrama

- Híbrido (nube + on-prem) · offline-first (14 h sin señal) · Zero Trust
  (Keycloak OIDC/MFA, mTLS) · multi-zona IaC (Terraform/K8s) · sin vendor lock-in ·
  disponibilidad (RTO/RPO definidos, prueba DR semestral) · ventana 05:30–07:00
  con cero indisponibilidad.

## Mapa arquitectónico interactivo (2026-09-07)

- Artefacto: `Diagramas/arq_mapa_hibrido.html` — mapa híbrido auto-contenido con zoom al DC
  (última milla → nube AWS sa-east-1/DR us-east-1 → WAN 3 caminos → CD Talca → sala blanca
  R01–R04 → borde Concepción/cross-docks). Preview: `arq_mapa_hibrido_preview.png`.
- Para iterar con Open Design (instalado en `C:\Users\henri\AppData\Local\open-design`,
  Node 24 portable en `Programs\node24`): daemon `http://127.0.0.1:7456`, UI web
  `http://localhost:5173`, con el agente opencode como motor de diseño.
- Zoom por doble-clic (data-zx/zy/zw/zh), tooltips por id (objeto `meta`), leyenda de
  zonas RT-06.03. Antes de regenerar, confirmar stack consolidado del Subdoc 4
  (Django/AWS/Keycloak/Kotlin/Angular; no Laravel/Flutter — quedaron descartados).