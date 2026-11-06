# Prompts para sincronizar S4, S7 y S13 con S8

Estos prompts preparan revisiones independientes de los tres subdocumentos. Usá **un prompt por vez** y compartí al ejecutor el prompt completo, la versión vigente del subdocumento indicado y sus fuentes editables. El objetivo es corregir cruces con S8 sin deteriorar la coherencia interna de S4, S7 o S13.

## Contexto y reglas comunes

- El Subdocumento 8 vigente está en `08_plan_riesgos/contenido.tex`, `LAFROX-Subdocumento8-Anexos.tex` (anexos **8.A–8.D**) y `LAFROX-Formulario-T-16.tex`.
- **El Anexo 8.E fue eliminado. No lo recrees, no lo cites como destino y no agregues referencias a él.** Los riesgos internos que S8 mantiene como controles CI no son riesgos transferidos al CLIENTE; su detalle no debe atribuirse a un anexo 8.E inexistente.
- S8 es el documento de referencia para los identificadores, clasificación y reglas de riesgo aquí enumerados; no es permiso para cambiar compromisos ni requisitos propios del subdocumento objetivo.
- Los PDFs de S4, S7 y S13 se encuentran bajo `Datos externos/Informe_2_LafroX/`. En este repositorio no hay fuentes LaTeX editables de esos subdocumentos. Los textos extraídos bajo `tmp/` son evidencia histórica/de navegación, no una versión actual verificada. Confirmá cada cita, página, identificador y valor contra los archivos vigentes que te entregue el usuario.
- Si sólo tenés PDFs y no una fuente editable, **no los modifiques directamente ni fabriques archivos fuente**. Pedí la fuente editable o entregá instrucciones de reemplazo acotadas con documento, sección, página y texto que habría que ajustar.
- Leé completo el subdocumento objetivo, sus anexos y formularios asociados antes de cambiarlo. Después verificá todo el documento, no sólo el párrafo modificado: numeración, referencias cruzadas, indicadores, responsables, fechas, tablas, anexos y formularios.
- Hacé cambios mínimos y relacionados. No reescribas requisitos, compromisos, indicadores o supuestos para “hacerlos coincidir” si eso rompe la lógica interna del subdocumento. Ante conflicto entre dos requisitos fuente, dato no verificable o falta de autorización, no inventes una solución: documentá la discrepancia y pedí decisión.
- No edites S8, otros subdocumentos ni documentos comunes como S6/S9. Si el cambio necesario los afecta, identificá el ajuste requerido y dejalo como dependencia separada.
- Al cerrar, informá: archivos editados (o fuente editable que falta), discrepancias encontradas, cambios concretos, verificaciones de coherencia interna, cruces con S8 corregidos y pendientes. Separá los hechos verificados de los controles/pruebas sólo propuestos; una respuesta o ensayo planificado no demuestra implementación ni eficacia residual.

---

## Prompt 1 — Sincronizar S4 con S8

> Actuá como editor técnico del Subdocumento 4 (arquitectura). Tu tarea es alinear los cruces de S4 con el registro vigente de S8 **sin debilitar la coherencia interna, los requisitos de arquitectura, los objetivos de continuidad ni los compromisos de S4**.
>
> ### Lectura obligatoria
>
> Leé íntegramente el cuerpo, anexos y formularios de S4 —incluido el Formulario T-11— y revisá sus tablas de arquitectura, diagramas, escenarios de falla, objetivos, pruebas, definiciones y referencias cruzadas. Contrastá con `08_plan_riesgos/contenido.tex`, `LAFROX-Subdocumento8-Anexos.tex` (especialmente Anexo 8.D) y `LAFROX-Formulario-T-16.tex`. Verificá los números de sección y página en las versiones actuales; no tomes los números siguientes como prueba sin cotejarlos.
>
> ### Cruces que tenés que resolver
>
> 1. **Identidad y operación degradada — B-S4-01 / CI-048.** El registro vigente clasifica la indisponibilidad de identidad central y la propagación de altas, bajas y revocaciones como control interno CI-048, no como riesgo R-048 transferido al CLIENTE. Alineá el lenguaje de S4 para que la arquitectura, los responsables y las pruebas de operación sin conexión sean consistentes con esa clasificación. Preservá responsabilidades SEG (control), ARQ (diseño), SRE (ejecución) y CAL (verificación) cuando correspondan. Comprobá que AL-OFF-01 cubra 24 horas sin WAN, relevos a las 8 y 16 horas, expiración, denegación y reconciliación antes de H5/H10; no describas un permiso inválido como autorizado por defecto.
> 2. **ERP y emisión de guías — B-S4-02 / R-049.** R-049 es una dependencia del ERP del CLIENTE, emisor único de guías, incluida la pérdida de la sala de Talca. No confundas esta contingencia con R-008 (respuesta del SII), recuperación del WMS, colas locales ni conmutación de la plataforma. Si no existe una guía preemitida todavía válida, una carga modificada o una guía anulada no habilita la salida hasta que pueda emitirse una guía nueva válida. No inventes un segundo emisor ni una excepción al objetivo de recuperación. Conservá separadas las pruebas AL-DTE-01 y AL-DR-01.
> 3. **Autoridad central de escritura y stock — B-S4-03 / CI-050.** La consistencia central y la exclusión del escritor anterior son control interno CI-050, no R-050 transferido al CLIENTE. Verificá que el diseño y AL-STOCK-01/AL-DR-01 cubran conciliación por UUID/sitio, trabajo pendiente no confirmado, promoción controlada y retorno sin doble escritura. Mantené distintos CI-050, R-004 (conciliación inicial) y R-019 (interrupción WAN).
> 4. **POS y SII — CI-009 y R-008.** La falta de respuesta del SII permanece como dependencia externa R-008. Idempotencia, consulta del resultado del POS tras un timeout y prevención de doble débito son obligaciones internas CI-009; no las reclasifiques como riesgos del CLIENTE. Comprobá los casos de timeout antes y después del cargo, consulta con la misma clave y conciliación.
> 5. **Conectividad, energía y cobertura.** Mantené diferenciados la WAN por sitio (R-019), el corte eléctrico externo (R-020), la cobertura RF interior y los fallos de diseño/alta disponibilidad. Comprobá que las rutas de respaldo y los tiempos sean por sitio y componente. Una ruta propuesta no prueba que esté instalada ni que conmute. No equipares una ventana local de 3 horas en cross-docking con 24 horas de autonomía requerida; tampoco una UPS de gabinete de 30 minutos con el generador de Talca de 24 horas. Verificá en cámaras reales la cobertura, los terminales, las puertas y la ocupación antes de afirmar que el diseño fue probado.
> 6. **Autorización de promoción y residencia.** Distinguí la decisión operativa de promoción (R-018; titular y suplente delegados, aviso al suplente a los 15 minutos y decisión dentro de 30 minutos) de la aprobación previa de residencia/transferencia de datos (R-021). El silencio no autoriza promoción ni redirección de tráfico.
> 7. **Continuidad y recuperación.** Conservá los objetivos RTO de 4 horas y RPO de 15 minutos, y separá la evidencia de AL-OFF-01, AL-DTE-01, AL-STOCK-01 y AL-DR-01. El retiro sanitario tiene un máximo de 2 horas; el presupuesto 15+60=75 minutos es un objetivo a probar, no un resultado demostrado. No uses 85 minutos ni una prueba genérica para afirmar cobertura de las 96 salidas, ERP, WMS, identidad y retiro sanitario a la vez.
>
> ### Preservación de coherencia interna y cierre
>
> Antes de editar, identifica las dependencias de cada cambio dentro de S4 (requisitos, diagramas, amenazas, tablas, objetivos, pruebas, anexos, T-11 y referencias). Actualizá todas las apariciones afectadas y no dejes contradicciones internas. Conservá requisitos de seguridad, continuidad, disponibilidad y recuperación; si S4 ofrece un control que aún no está implementado, expresalo como diseño/compromiso o prueba pendiente, no como resultado conseguido.
>
> Al finalizar, entregá una matriz `cruce S8 | ubicación en S4 | cambio | efecto en coherencia interna | evidencia verificada | pendiente`. Enumerá además las comprobaciones completas de S4 y cualquier dependencia que requiera actualizar S8/S7/S9/T-13. No afirmes que un PDF fue editado si sólo generaste instrucciones.

---

## Prompt 2 — Sincronizar S7 con S8

> Actuá como editor técnico del Subdocumento 7 (planificación y despliegue). Alineá las dependencias de S7 con el registro vigente de S8, preservando la lógica interna de EDT, calendario, recursos, olas, capacitación, marcha blanca, reservas y formularios.
>
> ### Lectura obligatoria
>
> Leé íntegramente S7, sus anexos, el Formulario T-14, el cronograma y los formularios T-15/T-18 asociados. Contrastá con `08_plan_riesgos/contenido.tex`, `LAFROX-Subdocumento8-Anexos.tex` (sobre todo 8.A.2 y 8.D) y `LAFROX-Formulario-T-16.tex`. Verificá cada mes, hito y cifra en los documentos vigentes que te entregue el usuario; no uses el texto extraído de `tmp/` como prueba actual.
>
> ### Cruces que tenés que resolver
>
> 1. **Conocimiento del planificador — R-016.** Mantené la transferencia prevista en meses 1–3 y la confirmación del retiro mediante V-14 en el mes 1, sin inventar una fecha de jubilación. Incorporá coherentemente la prueba de que el equipo pueda aplicar rutas y excepciones sin el planificador durante la marcha blanca de meses 13–15. Alineá EDT, responsable, capacitación, aceptación y calendario entre cuerpo, anexos y formularios; no dupliques este mismo evento en otro riesgo.
> 2. **Rotación de preparación nocturna — B-S7-01 / R-042.** S8 trata el 38 % como tasa anual de rotación, **no** como probabilidad del evento. El riesgo es que altas y reemplazos superen la capacidad de tutoría/evaluación o trabajen sin estar preparados. Revisá §7.1.2.7, figura 7.15, T-14 §7.1.2 y T-15: programa continuo en meses 13–56, turno 22:00–06:00, aprendizaje de hasta dos horas, tutor y evaluación antes del trabajo autónomo. Conservá IMP como responsable hasta mes 21 y SRE desde mes 22, con las contrapartes operativas previstas. Diferenciá R-042 de R-017 (inasistencia a capacitación) y R-015 (adopción); no vuelvas a cargar las 2.816 HH ordinarias de capacitación como contingencia de riesgo.
> 3. **Innovación y ventana del piloto.** Mantené diferenciados el paquete 3.10.1.4 de meses 11–15, certificación H5 de meses 11–12 y piloto con locales reales de meses 13–15. No muevas el piloto a meses 11–12 ni conviertas su calendario en resultado ya logrado.
> 4. **Peak de septiembre y cierre de E2 — R-044.** Alineá el supuesto de inicio contractual/calendario con la ventana de septiembre y el cierre de E2 en meses 19–20. R-044 cubre coordinación y recuperación del cierre ante peak/congelamiento; la demostración técnica de capacidad es el control interno CI-047 y no debe duplicarse dentro de R-044. Si las fechas calendario dependen del inicio real, dejalas condicionadas y señalá quién debe confirmarlo; no inventes fechas contractuales.
> 5. **Capacidad, concurrencia y reservas.** Revisá que los picos de trabajo de meses 13–15 y 19–20, las olas, las dependencias y el nivelado de recursos sean coherentes dentro de S7 y sus formularios. S8 informa 1.183,11 HH de exposición esperada para 35 riesgos; los 689,67 HH de los diez mayores son un subconjunto, no otra reserva. Las 1.600 HH de reserva de gestión continúan separadas y sin conciliación resuelta; las 3.072 HH protegidas mencionadas en S7 no deben fusionarse, sumarse ni redefinirse sin una derivación verificable. No declares capacidad, holgura, presupuesto o financiación demostrados si S7 no los demuestra. Las cuatro semanas finales de evidencia de cada marcha blanca no son holgura consumible.
>
> ### Preservación de coherencia interna y cierre
>
> Actualizá en conjunto el calendario, EDT, cargas por perfil, hitos, dependencias, capacitación, marcha blanca y T-14/T-15/T-18 donde haga falta. Revisá referencias inversas y cálculos afectados por cualquier cambio de fecha o duración. No cambies requisitos del CLIENTE para acomodar una estimación; no introduzcas un segundo evento para el mismo hecho.
>
> Al finalizar, entregá una matriz `cruce S8 | ubicación en S7/formulario | calendario antes/después | cambio | verificación interna | evidencia/pending`. Enumerá las comprobaciones de precedencia, fechas, totales, responsabilidades y referencias que ejecutaste, y toda decisión que falta. Diferenciá objetivos propuestos de compromisos aceptados. Si no hay fuentes editables, no modifiques PDFs: entregá instrucciones exactas y solicitá los archivos fuente.

---

## Prompt 3 — Sincronizar S13 con S8

> Actuá como editor técnico del Subdocumento 13 (innovaciones). Alineá sus referencias al registro de riesgos con la clasificación vigente de S8, sin alterar la lógica, alcance, etapas, indicadores, dueños, criterios de habilitación ni compromisos propios de cada innovación.
>
> ### Lectura obligatoria
>
> Leé íntegramente S13, su anexo y el Formulario T-19. Contrastá todas las menciones de riesgos, matrices, ID, probabilidades, impactos, responsables y criterios de habilitación con `08_plan_riesgos/contenido.tex`, `LAFROX-Subdocumento8-Anexos.tex` (8.A–8.D) y `LAFROX-Formulario-T-16.tex`. Verificá directamente en los PDFs vigentes páginas y referencias; los extractos de `tmp/` son pistas históricas, no prueba de la versión actual.
>
> ### Cruces que tenés que resolver
>
> 1. **Reclasificación de riesgos de diseño de innovaciones.** En T-16 los asuntos de diseño y construcción se retiraron del conjunto de riesgos transferidos al CLIENTE. Alineá en todo S13 los seis ID que correspondan: R-034→CI-034, R-035→CI-035, R-036→CI-036, R-037→CI-037, R-038→CI-038 y R-040→CI-040. Revisá texto, tablas, anexos, formularios, referencias cruzadas y menciones a RBS/T-16; no dejes IDs viejos como riesgos vigentes del CLIENTE. Conservá sus controles, dueños, indicadores y puertas de decisión como trabajo interno de diseño/verificación. **El Anexo 8.E fue eliminado: no lo cites ni inventes un nuevo destino de anexo.** Si S13 necesita nombrar el responsable o artefacto de seguimiento interno, usá sólo un destino confirmado en fuentes actuales; si no existe, reportá el vacío en lugar de inventarlo.
> 2. **INN-01 / CI-034 y piloto.** Conservá el paquete 3.10.1.4 en meses 11–15, certificación H5 en meses 11–12 y piloto real con locales en meses 13–15. Alineá la coordinación del piloto (IMP), dirección de INN-01 (DAT) y validación del catálogo (Comercial/Calidad) en meses 7–9, si esas responsabilidades siguen vigentes en el S13 actual. I-01A exige al menos 70 % de aciertos sobre al menos 100 avisos evaluables en el mes 15; no amplíes la innovación a otras rutas sin cumplirlo. Revisa la referencia antigua del tipo R8-25: sustituila sólo después de verificar exactamente qué riesgo/documento cita y cuál es el destino actual CI-034. No elimines ni debilites el piloto al cambiar la clasificación del riesgo.
> 3. **INN-02, INN-03 e INN-05.** Alineá las referencias de diseño/verificación con CI-035–CI-038 y CI-040, preservando sus indicadores, responsables y condiciones para habilitar cada función. No conviertas la reubicación a CI en aceptación del diseño, cierre del control ni reducción automática de sus valoraciones históricas.
> 4. **Mantener R-039 como riesgo del CLIENTE.** No reclasifiques el riesgo de liquidación contractual de INN-04: S8 lo conserva como R-039, impacto 3 y exposición 0,10 (Media). Cotejá en las fuentes vigentes probabilidad 40 %, PERT 61,33 HH y VE 24,53 HH. Alineá su tratamiento con las reglas de mes 20, tres liquidaciones sombra de meses 21–23 y pagos variables desde mes 24; una disputa puede suspender el devengo afectado, pero no el servicio. Si hay valores actuales distintos en S13, identifica qué fuente los gobierna y presenta la discrepancia, no los sobreescribas sin resolverla.
>
> ### Preservación de coherencia interna y cierre
>
> Tras modificar una referencia, comprobá de extremo a extremo cada innovación: descripción, alcance obligatorio/opcional, calendario, etapas, indicador, fuente de datos, dueño, costo/horas, habilitación, riesgo y referencia cruzada. Mantené consistencia entre cuerpo, tablas, anexos y T-19. No cambies un indicador o puerta de seguridad para que coincida con una puntuación de riesgo. No sustituyas términos del contrato ni conviertas una condición pendiente de validación en un hecho cumplido.
>
> Al finalizar, entregá una matriz `innovación/ID anterior | ID vigente | ubicaciones revisadas | cambio | indicador/puerta preservados | coherencia interna verificada | pendiente`. Incluí un recuento de referencias obsoletas que quedaron en cero o explica cada excepción. Si sólo tenés PDFs, no los edites: pedí las fuentes editables o entregá instrucciones de reemplazo acotadas y verificables.
