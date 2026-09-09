---
name: licitacion-workflow
description: Skill orquestador del proyecto LafroX (Licitación TFEP-01/2026, Caso 02 Logística — Distribuidora Puelche S.A.). Cárgalo SIEMPRE al iniciar cualquier avance de la propuesta; indica qué skill activar en cada fase (requerimientos, arquitectura, planificación, riesgos, oferta, presentaciones, informes). Use when working on lafrox, licitación, propuesta, caso 02, puelche, sobres, T-12, T-15, T-21, T-22, EDT, cronograma 56 meses.
---

# Licitación Workflow (LafroX)

Orquestador del flujo de trabajo de la propuesta técnico-económica para la
licitación pública ficticia **TFEP-01/2026 — Caso 02: Logística (Distribuidora
Puelche S.A.)**. Proyecto de la PUCV (Taller de Formulación de Proyectos
Informáticos, ICI-5444). Todo el trabajo se redacta en **español**.

## Protocolo de sesión

1. **Cada respuesta final** de texto comienza con el encabezado `## LafroX`
   (fuente: `compct/CONTEXTO_SESION.md`). Las salidas de herramientas no lo llevan.
2. El usuario se identifica como **LafroX**. Usar esa firma en documentos que lo requieran.
3. Respecto a documentos rectores, rige la precedencia estricta del Art. 5°:
   1. `Bases/Bases_Administrativas.md`
   2. `Bases/Bases_Tecnicas_Transversales.md`
   3. `Bases/Caso_02_Logistica.md`
   El caso puede **endurecer** un requisito transversal, nunca **rebajarlo**.

## Restricciones innegociables del diseño (verificar en todo avance)

- **Despliegue híbrido obligatorio** (Art. 16): nube pública + componentes on-premise.
  No se admiten propuestas solo-nube ni solo-on-premise.
- **Cronograma 56 meses** (Art. 17): Etapa 1 meses 1–15 (producción mes 16),
  Etapa 2 meses 13–20 (producción mes 21), Operación 21–56. Salidas no negociables.
- **5 innovaciones obligatorias** (Cap. 5 Bases Admin), una por tipo, trazables con
  arquitectura, EDT y flujo de caja.
- **Volumetría del Caso 02** (Cap. 15): 14.200 clientes, 31.000 pedidos-mes,
  260.000 líneas, 2,4 M unidades-mes, 62 preventistas, ~200 conductores,
  14.200 puntos de entrega, 68.000 canastillos / 9.400 pallets (14 % pérdida),
  2,3 % conteo cíclico, 1,7 % merma, 82,4 % OTIF base. Ventana crítica de despacho
  05:30–07:00. Preparación nocturna 22:00–06:00.
- **Códigos RT**: responder contra el código correcto del documento transversal
  (RT-03.23 no 03.24; RT-03.12 no 03.13; RT-16.10 no 05.10), usando la materia del
  caso como valor.
- **Inconsistencias de las Bases**: no corregirlas unilateralmente. Cada una es
  candidata a consulta al mandante (Art. 43.3), supuesto declarado o decisión fundada.

## Fases y skill a activar

| Fase | Skill a activar | Qué produce |
|---|---|---|
| Inicio de avance | `licitacion-workflow` (este) | Marco y fases |
| Entendimiento / investigación | `deep-research` | Normativa, estándares GS1, EDI, DTE, cadena de frío |
| Requerimientos (Cap. 17.1) | `xlsx` + `requirements-gathering` | Catálogo RF/RNF/OP, supuestos, reglas de negocio, trazabilidad |
| Arquitectura lógica/física/datos/seguridad | `architecture-diagrams` + `cloud-architecture` | Diagramas y justificación híbrida (RT-03) |
| Disponibilidad y operación | `sre-practices` | 99,9 %, RTO/RPO, SLO, DR semestral, observabilidad |
| Estimación y cronograma | `project-estimation` | EDT, nivelación T-15, flujo de caja, 56 meses |
| Riesgos | `risk-assessment` / `legal-risk-assessment` | Matriz de riesgos técnicos y contractuales |
| Oferta económica | `xlsx` | Planilla CLP/UF/USD, flujo de caja |
| Formularios oficiales / consultas | `docx` | Sobres, plantillas, consultas Art. 43.3 |
| Presentaciones (3) | `pptx` | Presentaciones preparatorias |
| Documentos extensos | `technical-writing` | Informes T-22 y subdocumentos |
| Diagramas en Markdown | `mermaid-diagrams` (default) / `plantuml-diagrams` | Fuentes versionables en `.md` |
| Export final | `pdf-handling` | Propuesta final en PDF |
| Gestión de tareas (opcional) | `jira-workflow` | Integración Jira Cloud (MCP desactivado por defecto) |

## Activación

Al cargar este skill: identificar la fase actual, activar el/los skill(s) de la
fila correspondiente con la herramienta `skill` y confirmar al usuario qué flujo
se inicia. Si la fase no está clara, preguntar antes de avanzar.