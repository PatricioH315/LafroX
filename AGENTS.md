# AGENTS.MD

## Qué es este proyecto

Proyecto de universidad (PUCV, Escuela de Informática — Taller de Formulación de Proyectos Informáticos, ICI-5444). El objetivo es redactar la propuesta técnico-económica para una licitación pública **ficticia** (Licitación N° TFEP-01/2026) del caso asignado: **Caso 02 — Logística** (Distribuidora Puelche S.A.).

Todo el trabajo se desarrolla en **español** (idioma oficial de la licitación). La salida esperada es documentación tipo oferta (arquitectura, servicios, requerimientos, planificación, evaluación de riesgos), no código.

## Identidad del proponente

- **Empresa proponente:** *(pendiente de definir — usar en columna B de la planilla de consultas, nomenclatura de archivos Art. 43.3, y en todos los documentos/sobres)*.
- **Equipo de trabajo (roles asignados):**
  | Rol | Nombre |
  |---|---|
  | Jefe de Proyecto | Alex Aravena |
  | Arquitecto de Solución | Bastián Trejo |
  | Encargado de Seguridad de la Información | Álvaro Catalán |
  | Líder de Datos | Leandro Chamorro |
  | Líder de Desarrollo | Tomás Pérez |
  | Líder de Calidad | Maximiliano Miño |
  | Líder de Operación / SRE | Guillermo Castillo |
  | Líder de Implantación y Gestión del Cambio | Patricio Henríquez |
- *Fuente: `Trabajos Anteriores/Equipo_y_roles_lafrox.csv` (rol, nombre, certificaciones, dedicación, meses de participación). Las columnas de Dedicación/Meses quedan por llenar.*

## Protocolo de sesión (importante)

- El usuario opera este proyecto bajo el nombre **LafroX**.
- **Cada respuesta final** de texto del asistente debe comenzar con el encabezado `## LafroX`. Esto permite identificar dónde termina una respuesta y dónde inicia una nueva sesión. Aplica a todo mensaje visible, no a las salidas de herramientas.
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
- El problema del caso **no es un sistema legado único**: es un tejido de sistemas (ERP con una preventa de un proveedor desaparecido, WMS de 2013, planillas, papel) más 14.200 puntos de entrega. La diferencia del conteo cíclico de inventario es de **2,3 %** del valor contado y la merma por vencimiento de **1,7 %**, con **82,4 %** de entregas completas y a tiempo. Trazabilidad sanitaria, OTIF y costo de servir son los ejes de negocio.

## Base canónica de trabajo (leer antes de tocar cualquier entregable)

**El repositorio se organiza por los 14 subdocumentos del Formulario T-7**, no por entregas. Cada
carpeta `NN_...` en la raíz es un subdocumento (numeración exacta del T-7) y adentro conviven las
iteraciones como subcarpetas `entrega_1/`, `entrega_2/`, etc.

- `entrega_1/` (dentro de cada subdocumento que corresponda) — **registro congelado** de lo
  efectivamente entregado el 07-09-2026, extraído de `Productos/Informe 1 Entrega 1.docx`. El
  Informe 1 cubrió los subdocumentos 1, 2, 3, 4 (lógica y física), 5 (modelo de datos) y 13
  (innovaciones), cada uno con `texto/` (narrativa `.md`) y `tablas/` (planillas `.xlsx`, una hoja
  por tabla). Los 15 diagramas del `.docx` viven en `Diagramas/` en la raíz. **`entrega_1/` no se
  edita nunca.**
- `entrega_2/` (dentro de cada subdocumento) — **documento de trabajo** para el Informe 2
  (05-10-2026). Nació como copia exacta de `entrega_1/` en los subdocs que ya existían y añade los
  subdocs 6, 7, 8 y 9 (metodologías, plan de trabajo/EDT, riesgos y calidad).
- `00_trazabilidad_observaciones/` en la raíz — bitácora observación → respuesta → sección que exige
  el Art. 45 · T-22, más los manifiestos de extracción y los historiales de cada entrega.

**Reglas de uso:**

1. Todo trabajo para la Entrega 2 **parte del contenido de `entrega_1/`** del mismo subdocumento, no
   de cero y no de otra fuente. Si un subdocumento ya tiene `entrega_1/`, ese es su línea base.
2. **Toda modificación respecto de la Entrega 1 debe quedar registrada** en
   `00_trazabilidad_observaciones/tablas/Trazabilidad_Observaciones_Informe1.xlsx`, con la
   observación que la motiva y la sección modificada. Un cambio sin fila en esa tabla se lee como
   observación no atendida (Art. 45 · T-22).
3. Ante discrepancia entre `entrega_1/` y cualquier otro documento del repositorio sobre **qué se
   entregó**, manda la Entrega 1 (y su origen, el `.docx`).
4. Para decidir **qué contenido conservar**, el criterio es el `.docx` de la Entrega 1. Lo que no
   esté ahí es material de trabajo, no entregable.
5. Los 15 diagramas del `.docx` viven en `Diagramas/` en la raíz junto con el material de trabajo
   del repo. La deduplicación entre `entrega_1/` y `entrega_2/` es deliberada: los diagramas del
   Informe 1 son la línea base y `entrega_2/` los referencia por nombre desde la biblioteca única.


## Carpetas

**Subdocumentos T-7** (uno por carpeta, con numeración exacta del Formulario T-7):

- `01_presentacion_empresa/` · `02_problema_necesidad/` · `03_esquema_solucion_alcance/` · `04_arquitectura/` (lógica **y** física en un solo subdoc, según T-7) · `05_modelo_datos/` · `06_metodologias/` · `07_plan_trabajo_edt/` · `08_plan_riesgos/` · `09_plan_calidad/` · `10_operacion_niveles_servicio/` · `11_planes_operacion/` · `12_equipo_subcontrataciones/` · `13_innovaciones/` · `14_ventajas_beneficios_consolidacion/`.
- Cada subdocumento tiene un `README.md` con el detalle que exige el T-7 y las subcarpetas `entrega_1/` (congelada) y/o `entrega_2/` (trabajo) donde vive su contenido.

**Transversales**:

- `00_trazabilidad_observaciones/` — bitácora de observaciones y respuestas entre entregas (T-22 · Art. 45), manifiestos de extracción del `.docx` e historiales de cada entrega. **Aquí se registra todo cambio** entre `entrega_1/` y `entrega_2/`.
- `Bases/` — documentos rectores (ver precedencia arriba). `Bases/pdf/` guarda los originales.
- `Requerimientos/` — catálogos RF/RNF/bases (`.csv`), decisiones, reglas de negocio, supuestos y justificaciones. Es la fuente de los catálogos que se vuelcan al subdocumento 3.
- `Arquitectura/` — documentos fuente de arquitectura, **no entregables**:
  - `Arquitectura/logica/` — arquitectura lógica vigente (`Arquitectura_Logica_v6-2.md`).
  - `Arquitectura/fisica/` — física consolidada, despliegue, integración, seguridad, dimensionamiento, sala de servidores, tabla de emplazamiento, ADR, BI, T-11, T-12 y el data center (`Subdoc04_DataCenter.md`).
- `Diagramas/` — biblioteca única de diagramas del repositorio: los **15 diagramas del `.docx` de la Entrega 1** (prefijos `ARQL-` y `ARQF-`) más las fuentes `.drawio` y `.png` de trabajo, incluida `RT-06_DataCenter/`. Los subdocumentos referencian los diagramas por nombre desde aquí.
- `Formularios/` — formularios técnicos y económicos (T-8, T-9, T-10, T-13, T-14, T-19, T-21, etc.).
- `Rúbricas/` — rúbricas de calificación por entregable e instrucciones globales de evaluación.
- `Productos/` — salidas entregables y auxiliares: `.docx` de la Entrega 1 (fuente de verdad), planillas T-12, registro de decisiones, plantilla de informe, la presentación PDF y su narración .mp3.
- `Trabajos Anteriores/` — propuestas y respaldos previos. Solo sirven de **referencia de forma**, no de contenido.
- `compct/` — contexto de sesión y protocolo de identidad (`CONTEXTO_SESION.md`). Define el encabezado `## LafroX` que debe comenzar cada respuesta final.
- `.opencode/` — configuración local de opencode: skills versionadas (`.opencode/skills/`), plugin de activación y dependencias. `node_modules/` y `opencode-loop/` no se versionan (ver `.gitignore`).
- `_staging/` — archivos en tránsito, **no versionado** (`.gitignore`). Nada de aquí es fuente: cuando un archivo se consolida, se mueve a su carpeta definitiva.

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

### Reglas de negocio (dentro del registro de requerimientos — Cap. 17.1)

Las reglas de negocio **no van como capítulo aparte del informe** (el T-22 no las pide como sección independiente). Van **dentro del registro de requerimientos del Cap. 17.1** —es decir, dentro del catálogo de requerimientos y su apoyo en el "esquema de solución y alcance" (Informe 1, Subdoc 3)—, como lo exige formalmente el caso. Cada regla se registra con el formato: qué se captura, en qué punto del proceso, por quién y con qué consecuencia si se incumple. Al menos:

- Asignación y reserva de stock (cuándo se compromete: toma, confirmación o preparación; regla ante doble compromiso — decisión 16.1 #8).
- Política de crédito y comportamiento de pago del cliente (lo que el preventista debe ver y las consultas registradas).
- Excursión de temperatura: qué la constituye, quién decide y si el sistema bloquea el despacho automáticamente (decisión 16.1 #4).
- Reintento de entrega / local cerrado: qué se hace y quién decide (decisión 16.1 #3).
- Tratamiento de devoluciones en el momento de la entrega y su efecto sobre el documento tributario emitido (decisión 16.1 #12).
- Control de envases retornables: 68.000 canastillos y 9.400 pallets, pérdida estimada 14 % anual (decisión 16.1 #10).
- Cambio de precio entre toma de pedido y despacho (decisión 16.1 #9).
- Definición unívoca de "entrega cumplida" (completa/parcial) y de la métrica OTIF (decisión 16.1 #1).

Cada regla debe trazar su origen al caso (párrafo, entrevista, indicador o decisión 16.1) y a los requisitos RF/RNF que la implementan, así como su efecto en arquitectura y EDT.

## Inconsistencias detectadas en las Bases (resolver en consultas)

Las siguientes incoherencias existen entre los documentos rectores. **No corregirlas unilateralmente en la propuesta**: cada una es candidata a **consulta al mandante (Art. 43.3)**, declaración de supuesto, o decisión fundada. El proponente que las detecte y las resuelva explícitamente es evaluado favorablemente (el caso premia identificar vacíos no listados). Clasificación por gravedad:

### Alta — afectan diseño o puntaje

1. **Número de instalaciones.** El caso §8 dice "la red de **cinco** instalaciones"; la Tabla 14.1 y RT-21.16 dicen **seis** ("Seis instalaciones en cuatro regiones"). Prevalecería `6` (la fuente mayor y las dos menciones técnicas); confirmar en consulta.
2. **Ponderación T-21 no suma 100%.** La columna "Ponderación" del Formulario T-21 (Bases Admin §1807) suma **98%**, pese a que la fila TOTAL declara **100%**. Impacta el cálculo del puntaje técnico. Verificar si faltó un 2% en algún subdocumento (p.ej. Subdoc 14 "Ventajas" de 3% o el transversal).
3. **Número de ambientes obligatorios.** El Art. 24° (Bases Admin) y E-25/H3 enumeran **cuatro** ambientes; el Art. 3° y las Transversales (§4.1, RT-04.01) exigen **cinco** (incluye el ambiente de Recuperación ante Desastres como 5º). Prevalecen las Transversales (5 ambientes + DR); dejar consistente la propuesta.
4. **Códigos RT mal mapeados en la tabla del Caso Cap. 15.** El apartado "Valores para el Caso 02" referencia códigos que no coinciden con la materia en las Transversales:
   - Red inalámbrica/estudio de sitio: el caso cita **RT-03.24** pero el correcto es **RT-03.23** (RT-03.24 es "Deseable": QoS/priorización).
   - Sincronización tras reconexión: el caso cita **RT-03.13** pero el correcto es **RT-03.12** (RT-03.13 es "funciones no disponibles en modo desconectado").
   - Retención de datos históricos/auditoría: el caso cita **RT-05.10** pero el correcto es **RT-16.10** (RT-05.10 es "Deseable": catálogo de datos/linaje).
   - Tipología del emplazamiento on-premise: el caso cita **RT-06.01**, que en transversales es "espacio de uso exclusivo/aislado", no tipología.
   → En la Matriz de Cumplimiento T-12 responder contra el **código correcto del documento transversal**, usar la materia del caso como valor y, si va a consulta, señalar el desajuste.

### Media — afectan presentación/plan

5. **"Instalaciones" vs "conductores/camiones".** El caso §2.4 habla de ≈84 conductores propios y peonetas; la Tabla 14.1 fila "Conductores" anota "42 propios" (que es el número de **camiones**, §2.3). Ratios de totales ≈200 vs ≈244 según se lea. Aclarar en supuestos: camiones ≠ conductores.
6. **T-22 vs entregables del Cap. 17.1.** El Formulario T-22 (contenido de informes) no menciona explícitamente "registro de reglas de negocio", "registro de supuestos" ni "matriz de trazabilidad" que el caso exige producir (17.1). No crear capítulos extra en el informe: esos entregables **viven dentro del registro de requerimientos del Cap. 17.1** y se reflejan como apoyo en el "esquema de solución y alcance" (Informe 1, Subdoc 3) y en el Subdoc 5 (modelo y gestión de datos), donde el T-22 sí los abriga. Si el cliente espera verlos como ítem propio en algún informe, confirmarlo en consulta.
7. **Fechas de calendario.** (a) El período de registro (Formulario T-20, 14–17 ago) termina **antes** de la publicación de las bases (19 ago); (b) el Informe 1 coincide con la publicación del Acta de Respuestas el 07-09; (c) el Informe 3 y la Presentación 3 caen el mismo día (13-11), en apariencia contra el Art. 45 ("informe con anterioridad a la presentación"). No alterar el cronograma; confirmar fechas en consulta.

### Baja — terminología

8. **Identificador de documentos.** Las Bases del caso se citan como "FEP01.26" / "FEP02.26" (caso y transversales) mientras el identificador oficial del llamado es **TFEP-01/2026**. Estandarizar a `TFEP-01/2026` en la propuesta.
9. **Desconexión: "2 horas" vs "turno de 14 h".** El relato (§6, §8) refiere cortes de "hasta dos horas"; la restricción del Cap. 10 y RT-03.10 exige operar un **turno completo de 14 h** sin señal en contingencia. Escenarios distintos: usar 2 h como nominal y 14 h como contingencia de diseño; documentar ambos.

### Valores verificados consistentes (usar tal cual)

- 14.200 clientes / 31.000 pedidos-mes / 260.000 líneas / 2,4 M unidades-mes.
- Entregas ≈1.400 normal y ≈2.600 peak septiembre; km ≈420.000; documentos tributarios ≈34.000.
- Envases 68.000 canastillos y 9.400 pallets (14 % pérdida anual); preventistas 62; personal CD 310.
- Ventana crítica de despacho 05:30–07:00 con cero indisponibilidad; cutover on-premise 24 h (RT-03.10).
- Prueba de DR semestral (Art. 20) coherente con RT-07.07 (dos veces al año).
- Percentil 95 en tiempos de respuesta (RT-09.01) coherente entre Admin/Transversales/Caso.

## Verificación

No hay build, test ni lint (solo markdown y Excel). La "verificación" del trabajo es la coherencia entre documentos: respetar la precedencia, trazabilidad de requerimientos (requisito RT → módulo → entregable) y consistencia de cifras/plazos con el cronograma obligatorio y con la volumetría del caso.

## Skills y su activación

Las skills se cargan con la herramienta `skill`. El skill **`licitacion-workflow`** (`.opencode/skills/licitacion-workflow/`) es el orquestador: **cárgalo al iniciar cualquier avance de la propuesta**; indica qué skill activar en cada fase. Los skills de trabajo viven en `.opencode/skills/` (todos creados, versionables).

Skill **orquestador** (cargar siempre):

| Skill | Uso |
|---|---|
| `licitacion-workflow` | Orquestación del flujo: qué skill activar en cada fase y qué entregable producir |

Skill **de trabajo** (activados por fase, ver el flujo abajo):

| Skill | Uso en la propuesta |
|---|---|
| `xlsx` | Requerimientos/volumetría, oferta económica (CLP/UF/USD) y flujo de caja (Excel/CSV) |
| `docx` | Llenar formularios/plantillas oficiales (.docx) de los sobres |
| `pptx` | Las 3 presentaciones preparatorias |
| `pdf-handling` | Compilar LaTeX (main.tex) y conformar/exportar la propuesta en PDF |
| `architecture-diagrams` | Diagramas de arquitectura (lógica/física/datos/seguridad/despliegue) y su auditoría |
| `cloud-architecture` | Justificar la arquitectura híbrida nube+on-premise (RT-03) |
| `sre-practices` | Disponibilidad 99,9 %, RTO/RPO, SLOs, observabilidad |
| `project-estimation` | Estimación de esfuerzo y desglose por rol (nivelación T-15) |
| `risk-assessment` | Riesgos técnicos, de desarrollo e implantación (T-16) |
| `legal-risk-assessment` | Riesgos contractuales y legales (Bases, sobres, precedencia) |
| `deep-research` | Investigar lo que el caso no explica (normativa, estándares GS1, mercado) |
| `technical-writing` | Redacción de documentos técnicos extensos |
| `mermaid-diagrams` | Diagramas en Markdown (`mermaid`) que GitHub renderiza nativo |
| `plantuml-diagrams` | Diagramas UML/C4 formales (.puml) renderizados a PNG/SVG vía Kroki |
| `jira-workflow` | Integración opcional con Jira Cloud (no creado aún) |

### Workflow por fase (cómo se combinan los skills)

Este flujo lo coordina `licitacion-workflow`; aquí el resumen para AGENTS.md:

| Fase | Actividad | Skills a cargar |
|---|---|---|
| 0 · Preparación | Leer AGENTS.md, CONTEXTO_SESION, Bases y **la línea base en los `entrega_1/` de cada subdocumento**; fijar estado | `licitacion-workflow` |
| 1 · Comprensión del caso | Problema/necesidad; investigar numeral 16.2 | `deep-research`, `technical-writing` |
| 2 · Requerimientos (Cap 17.1) | Catálogos RF/RNF/Bases, supuestos D1–D40, reglas de negocio, trazabilidad | `xlsx`, `technical-writing` |
| 3 · Arquitectura | Lógica/física/datos, híbrido, modelo de datos | `architecture-diagrams`, `mermaid-diagrams`, `plantuml-diagrams`, `cloud-architecture`, `sre-practices` |
| 4 · Planificación y riesgos | EDT, cronograma 56 meses, equipo, planes | `project-estimation`, `risk-assessment`, `legal-risk-assessment` |
| 5 · Oferta económica | Curva S, costos, VAN/TIR, innovaciones, flujo de caja | `xlsx`, `technical-writing`, `pdf-handling` |
| 6 · Presentaciones (T-22) | Informes 1/2/3 + PPT | `pptx`, `technical-writing`, `docx`, `pdf-handling` |
| Transversal · Formularios y PDF | Formularios de sobres, exportación | `docx`, `pdf-handling`, `architecture-diagrams` |

## Materias a investigar (numeral 16.2 del caso)

**El caso es Logística (distribuidora de consumo masivo), no retail.** El término "retail" aparece en este caso únicamente en un punto: las cadenas de supermercados que son **cliente** del canal moderno de Puelche (con las que se intercambia mensajería electrónica EDI). El giro y el problema del caso son de logística: trazabilidad de lote, cadena de frío, preventa, reparto y costeo logístico.

La lista de investigación se toma literal del numeral 16.2 del caso:

1. Estándares GS1: identificación de productos, de unidades logísticas y de ubicaciones; simbología de códigos de barras; y estándares de trazabilidad de eventos en la cadena de suministro.
2. Intercambio electrónico de datos con cadenas de retail (clientes) en Chile: qué mensajes se exigen, en qué formato y a través de qué intermediarios.
3. Documentos tributarios electrónicos: guía de despacho electrónica, factura, nota de crédito, acuse de recibo y sus efectos legales.
4. Reglamento Sanitario de los Alimentos: almacenamiento, transporte, control de temperatura, registro y retiro de producto.
5. Cadena de frío: rangos por tipo de producto, concepto de excursión térmica, criterios de aceptación/rechazo y tecnologías de registro continuo.
6. Indicadores logísticos: OTIF, fill rate, perfect order, costo de servir y costo por entrega (definición y cálculo sin ambigüedad).
7. Ruteo de vehículos con capacidad y ventanas de tiempo: formulación, métodos y limitaciones frente al conocimiento local del planificador.
8. Estrategias de preparación de pedidos y asignación de ubicaciones en bodega: olas, zonas, lotes y criterios por rotación.
9. Pronóstico de demanda en consumo masivo con estacionalidad fuerte y promociones, y su articulación con inventario y nivel de servicio.
10. Régimen de jornada de los trabajadores del transporte y control de horas de conducción y descanso.
11. Logística inversa: devoluciones, mermas y gestión de activos retornables.
12. Modelos de atención al canal tradicional: preventa, autoventa, autoatención digital y efectos sobre el costo de servir.

## Renderizado de diagramas

Regla de selección:

| Tipo de diagrama | Herramienta | Dónde se ve | Export para `.docx`/`.pdf` |
|---|---|---|---|
| Flujo, arquitectura, secuencia, ER, C4 | **Mermaid** (bloque `mermaid` en el `.md`) | GitHub renderiza nativo | `mmdc -i archivo.mmd -o archivo.svg/png/pdf` |
| UML/C4 formal, componente | **PlantUML** (`.puml`) | Exportar siempre a imagen | `curl https://kroki.io/plantuml/png` |
| Interactivo/animado | `architecture-diagrams` | HTML en navegador | screenshot → PNG |

Convención: la **fuente de los diagramas es texto** dentro de los `.md` de la propuesta (versionable). Los **PNG/SVG/PDF exportados** se guardan en `Diagramas/`. Usar Mermaid por defecto; reservar PlantUML para UML/C4 formal.

### Política de fuente de verdad tecnológica (auditoría de diagramas)

Al auditar los diagramas y documentos de arquitectura que se suban, aplica este criterio definido por LafroX (2026-09-03):

- **La auditoría se contrasta SOLO contra los archivos principales** (Bases, `Requerimientos/`, `_staging/` y fuentes primarias de arquitectura y del caso). **Nunca contra el informe LaTeX ni ninguno de sus derivados** (PDF, capítulos compilados, tablas/catálogos generados): el informe es un artefacto de salida, no autoridad. Si el informe y una fuente principal divergen, manda la fuente principal.
- **Consistencia entre arquitecturas:** la coherencia a validar es **lógica ↔ física** (y ambas contra requerimientos y el caso), no contra doc. compilados.

- **Si el stack del diagrama es aplicable al caso** (cumple lo innegociable: híbrido, offline de primera clase, Zero Trust, multi-zona IaC, sin vendor lock-in, mantenible por equipo TI de 4 personas, cronograma 56 meses) **y no interfiere con los demás puntos del caso**, se **adopta como fuente de verdad tecnológica** (se adapta el resto de la propuesta a él), aunque difiera del informe/premisas previas.
- **Si hay muchas contradicciones**, se **deja tal y como está**, se marca como divergente y se **revisa por separado** (no se fuerza a reconciliar contra otra fuente).
- La tecnología es **neutral** frente a las restricciones del caso (volumetría, trazabilidad, ventana de despacho, cronograma, indicadores). Una diferencia de stack (p.ej. Keycloak/Aurora, Laravel/AWS, 6 vs 8 capas) es una contradicción **entre artefactos internos**, no contra las Bases, salvo que incumpla un RT obligatorio expreso.
- Estado vigente al 2026-09-03: la **arquitectura lógica (`04`/`05`: Keycloak, Laravel, MariaDB/PostgreSQL, Flutter, K8s)** se **adopta como base tecnológica de la propuesta**. La arquitectura física e informe LaTeX (AWS: Cognito/Aurora/DynamoDB/Redshift) quedan **en revisión por separado** por divergencia de stack y de capas (6 vs 8).
