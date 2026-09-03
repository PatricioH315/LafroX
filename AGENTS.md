# AGENTS.MD

## Qué es este proyecto

Proyecto de universidad (PUCV, Escuela de Informática — Taller de Formulación de Proyectos Informáticos, ICI-5444). El objetivo es redactar la propuesta técnico-económica para una licitación pública **ficticia** (Licitación N° TFEP-01/2026) del caso asignado: **Caso 02 — Logística** (Distribuidora Puelche S.A.).

Todo el trabajo se desarrolla en **español** (idioma oficial de la licitación). La salida esperada es documentación tipo oferta (arquitectura, servicios, requerimientos, planificación, evaluación de riesgos), no código.

## Identidad del proponente

- **Empresa proponente:** *(pendiente de definir — usar en columna B de la planilla de consultas, nomenclatura de archivos Art. 43.3, y en todos los documentos/sobres)*.
- **Equipo:** *(pendiente de definir — integrantes del grupo)*.

## Protocolo de sesión (importante)

- El usuario opera este proyecto bajo el nombre **lafrox**.
- **Cada respuesta final** de texto del asistente debe comenzar con el encabezado `## lafrox`. Esto permite identificar dónde termina una respuesta y dónde inicia una nueva sesión. Aplica a todo mensaje visible, no a las salidas de herramientas.
- El archivo `compct/CONTEXTO_SESION.md` es la fuente completa de este protocolo. Si no aparece el encabezado, el usuario debe asumir que la respuesta está incompleta o que se inició una sesión nueva.

## Fuentes y precedencia

Los tres documentos de `Bases/` son la fuente de verdad. Orden de precedencia estricto (Art. 5° de las Bases Administrativas):

1. `Bases/Bases_Administrativas.md` — reglas del proceso y del contrato: participación, cronograma obligatorio de 56 meses, modelo de despliegue híbrido, hitos, formularios/sobres, evaluación y las 5 innovaciones obligatorias.
2. `Bases/Bases_Tecnicas_Transversales.md` — requisitos técnicos comunes a las 13 industrias, codificados como **RT-CC.NN** (Obligatorio / Deseable / Según caso). Deben responderse uno a uno en el **Formulario T-12**.
3. `Bases/Caso_02_Logistica.md` — el caso en sí. **No es una especificación de requerimientos**: traducir su narrativa (dolores, contradicciones, vacíos) en alcance, arquitectura, plan y estrategia es exactamente lo que se evalúa.

Regla de precedencia: el caso puede **endurecer** un requisito transversal, nunca **rebajarlo**. Un requisito marcado "Según caso" se completa con la volumetría/valores del Capítulo 15 del caso (si el caso no lo define, rige el valor por defecto del transversal).

## Reglas que condicionan todo el diseño

- **Despliegue híbrido obligatorio** (Art. 16): carga principal en nube pública + componentes on-premise. No se admiten propuestas solo-nube ni solo-on-premise.
- **Cronograma de 56 meses innegociable** (Art. 17): Etapa 1 (meses 1–15: desarrollo, marcha blanca, producción mes 16), Etapa 2 (meses 13–20, producción mes 21), Operación 36 meses (21–56). Salidas no negociables.
- **5 innovaciones obligatorias** (Cap. 5 Bases Admin), una por tipo, trazables con arquitectura, EDT y flujo de caja.
- **La operación es dispersa y de terreno**: preventa, reparto, preparación y recepción ocurren en la calle y en el local del cliente, no en oficinas. 62 preventistas, ~200 conductores, 14.200 puntos de entrega, rutas rurales sin cobertura y almacenes sin internet.
- **El perfil de carga no es plano**: preparación nocturna (22:00–06:00), despacho concentrado en la ventana 05:30–07:00, y septiembre casi duplica el volumen durante tres semanas. Un dimensionamiento basado en promedio está equivocado.
- El problema del caso **no es un sistema legado único**: es un tejido de sistemas (ERP con una preventa de un proveedor desaparecido, WMS de 2013, planillas, papel) más 14.200 puntos de entrega con 12,4 % de discrepancia de inventario y 82,4 % de entregas completas y a tiempo. Trazabilidad sanitaria, OTIF y costo de servir son los ejes de negocio.

## Carpetas

- `Bases/` — documentos rectores (ver precedencia arriba).
- `Requerimientos/` — planillas Excel de requerimientos (catálogos RF / RNF / OP, registro de supuestos, reglas de negocio, trazabilidad, vacíos). *(En elaboración.)*
- `productos/` — salidas entregables: consultas al mandante (`.docx`), planilla de consultas con nomenclatura Art. 43.3 (`.xlsx`) y registro de decisiones del caso.
- `TrabajosAnteriores/` — subdocumentos de propuestas/consultas previas. Solo sirven de **referencia de forma**, no de contenido.
- `Diagramas/` — PNG/SVG/PDF exportados de diagramas (Mermaid/PlantUML) para incrustar en `.docx` y PDF final. La fuente de los diagramas vive en los `.md` (ver "Renderizado de diagramas").
- `compct/` — contexto de sesión y protocolo de identidad (`CONTEXTO_SESION.md`). Define el encabezado `## lafrox` que debe comenzar cada respuesta final.
- `.opencode/` — configuración local de opencode: skills versionadas (`.opencode/skills/`), plugin de activación y dependencias. `node_modules/` y `opencode-loop/` (sesiones locales) no se versionan (ver `.gitignore`).

## Traza del proyecto (lo que produce el proponente)

Conforme al Capítulo 17 del caso, el trabajo de traducción exige:

- Catálogo de **requerimientos funcionales** (RF) y **no funcionales** (RNF), cada uno trazable a su origen (párrafo, entrevista, indicador o restricción).
- **Registro de supuestos** — obligatorio incluir las 16 decisiones del numeral 16.1.
- **Registro de reglas de negocio** (asignación de stock, crédito, excursión térmica, reintento, devoluciones, envases).
- **Matriz de trazabilidad** (origen → requerimiento → componente → EDT → prueba → criterio de aceptación).
- **Registro de vacíos y consultas** al CLIENTE.
- Definición de **alcance y reparto entre Etapas 1 y 2**, exclusiones y justificación.
- Dimensionamiento explícito de la volumetría de sistema (numeral 14.2), con método y supuestos; celdas vacías = dimensionamiento no realizado.
- Criterios de aceptación del **Capítulo 18** (retiro sanitario < 2 h, 100 % lote, registro continuo de temperatura, OTIF con meta, preventa con stock/crédito, cero pedidos perdidos/duplicados, ruta automática < 20 min).

## Verificación

No hay build, test ni lint (solo markdown y Excel). La "verificación" del trabajo es la coherencia entre documentos: respetar la precedencia, trazabilidad de requerimientos (requisito RT → módulo → entregable) y consistencia de cifras/plazos con el cronograma obligatorio y con la volumetría del caso.

## Skills y su activación

Las skills se cargan con la herramienta `skill`. El skill **`licitacion-workflow`** (`.opencode/skills/licitacion-workflow/`) es el orquestador: **cárgalo al iniciar cualquier avance de la propuesta**; indica qué skill activar en cada fase.

Skills de trabajo previstas para este proyecto (versión en `.opencode/skills/` cuando se definan):

| Skill | Uso en la propuesta |
|---|---|
| `licitacion-workflow` | Orquestación: qué skill activar en cada fase (cargar siempre) |
| `xlsx` | Requerimientos/volumetría, oferta económica (CLP/UF/USD) y flujo de caja (Excel) |
| `docx` | Llenar formularios/plantillas oficiales (.docx) de los sobres |
| `pptx` | Las 3 presentaciones preparatorias |
| `pdf-handling` | Conformar/exportar la propuesta final en PDF |
| `architecture-diagrams` | Diagramas de arquitectura (lógica/física/datos/seguridad/despliegue) |
| `cloud-architecture` | Justificar la arquitectura híbrida nube+on-premise (RT-03) |
| `sre-practices` | Disponibilidad 99,9 %, RTO/RPO, SLOs, observabilidad |
| `project-estimation` | Estimación de esfuerzo y desglose por rol (nivelación T-15) |
| `legal-risk-assessment` / `risk-assessment` | Evaluación de riesgos contractuales y técnicos |
| `deep-research` | Investigar lo que el caso no explica (normativa, estándares GS1, mercado) |
| `technical-writing` | Redacción de documentos técnicos extensos |
| `mermaid-diagrams` | Diagramas en Markdown (`mermaid`) que GitHub renderiza nativo |
| `plantuml-diagrams` | Diagramas UML/C4 formales (.puml) renderizados a PNG/SVG vía Kroki |
| `jira-workflow` | Integración opcional con Jira Cloud |

## Materias a investigar (numeral 16.2 del caso)

Estándares GS1; intercambio electrónico con cadenas de retail en Chile; documentos tributarios electrónicos (guía de despacho, factura, acuse de recibo); Reglamento Sanitario de los Alimentos y cadena de frío; OTIF/fill rate/costo de servir; ruteo de vehículos con ventanas de tiempo; preparación de pedidos y asignación de ubicaciones; pronóstico de demanda con estacionalidad; régimen de jornada de conductores; logística inversa; y modelos de atención al canal tradicional.

## Renderizado de diagramas

Regla de selección:

| Tipo de diagrama | Herramienta | Dónde se ve | Export para `.docx`/`.pdf` |
|---|---|---|---|
| Flujo, arquitectura, secuencia, ER, C4 | **Mermaid** (bloque `mermaid` en el `.md`) | GitHub renderiza nativo | `mmdc -i archivo.mmd -o archivo.svg/png/pdf` |
| UML/C4 formal, componente | **PlantUML** (`.puml`) | Exportar siempre a imagen | `curl https://kroki.io/plantuml/png` |
| Interactivo/animado | `architecture-diagrams` | HTML en navegador | screenshot → PNG |

Convención: la **fuente de los diagramas es texto** dentro de los `.md` de la propuesta (versionable). Los **PNG/SVG/PDF exportados** se guardan en `Diagramas/`. Usar Mermaid por defecto; reservar PlantUML para UML/C4 formal.
