## SD13 — alineación LaTeX–Markdown y matriz independiente — 12 de octubre de 2026

Autorización explícita: alinear cuerpo, anexos y T-19 con LaTeX vigente del checkout SD13/LafroX, rama LafroX-Subdoc13-LateX. Trasladar matriz Informe1 a archivo independiente en13_innovaciones, fuera de PDF; columnas exactas Observación del Informe1, Respuesta, Sección modificada. LaTeX: retirado antiguo Anexo13.D, remisiones de introducciones, filaIA correspondiente y portada anexos ajustada A–C. Markdown: tres documentos reconvertidos desde fuentes actuales, figuras enlazadas a activos PDF existentes sin editar imágenes; declaraciónIA consolidada en principal. Matriz separada conserva23observaciones/respuestas (15específicas+8transversales), referencias y revisión editorial acreditada previamente. Sin commit/push ni cambios en otros subdocumentos. Copias previas en SD13/tmp/alineacion-sd13. Verificación final: principal54p y anexos10p recompilados salida0; T-19 conserva13p sin cambiosLaTeX. Matriz ausente de ambosPDF y de índice/anexos/IAprincipal.23observaciones conservadas en MD de3columnas. Espejo reconvertido exacto de los3MD,6figuras enlazadas a PDFvigentes. Ajuste local14pt evita página final con solaURL en anexos, inspeccionada sin choque con firma. Persisten avisos previos de compilación y los demás pendientes del checklist.

# CONTEXTO DE SESIÓN

## Trazabilidad SD1–SD3: entregables en sus carpetas y formato común — 12 de octubre de 2026

**Objetivo/autorización:** usuario pidió llevar cada trazabilidad a carpeta de su informe porque se entrega, y que coincidan columnas/formato. rama-md comprobada; sólo Markdown, sin LaTeX, compilación, commit/push ni cambio de rama. Cambios concurrentes del resto preservados.

**Realizado:** matrices principales en 01_presentacion_empresa/LAFROX-Subdocumento1-Trazabilidad.md, 02_problema_necesidad/LAFROX-Subdocumento2-Trazabilidad.md, 03_esquema_solucion_alcance/LAFROX-Subdocumento3-Trazabilidad.md. Misma estructura: título, introducción neutral, tabla tres columnas «Observación del Informe 1 | Respuesta | Sección modificada», Referencias. 28/32/43 filas originales idénticas por fila, orden y estado; no nuevas observaciones, revisiones humanas ni cierres.

**Separación:** notas de auditoría/compilación/Git/hashes y pendientes administrativos fuera del entregable, conservadas en Revision/auditoria_trazabilidad_SD1.md, SD2.md y SD3.md. Los tres archivos principales antiguos de Revision se trasladan a esos registros; su matriz se reemplaza por enlace al entregable, evitando duplicación canónica. El SD1 histórico trazabilidad_Informe1_Informe2_SD1.md permanece histórico y enlaza nueva matriz. Rutas históricas mencionadas en contexto son historial, no ubicaciones vigentes.

**Verificación:** esquema de tres columnas idéntico, igualdad exacta de filas fuente/destino, todos los enlaces del entregable resuelven. Captura de hashes de filas en salida de verificación. No se interpreta traslado como revisión integral del estado: SD2 conserva estados anteriores y SD3 revisión humana pendiente. No declarar los tres listos/aprobados.

**Preferencia:** trazabilidad es parte de entrega y debe ir junto al subdocumento; consistencia visual y columnas, sin expandir contenido. Memoria Engram suspendida identidadruntime ausente; resumen local antes de responder.

**Siguiente:** revisar actualización de estados si se solicita; publicación/LaTeX no autorizados por este traslado Markdown.


## SD1 Obs.24: cierre mínimo aprobado y remisión aplicada — 12 de octubre de 2026

**Objetivo/autorización:** usuario pidió no hacer más de lo observado y respondió «Okey, dale entonces» a añadir remisión precisa y actualizar matriz. Prevalece sobre propuestas de nueva plantilla o redimensionamiento. rama-md comprobada; fuentes/PDF sólo en ../LafroX-sd1-latex, rama LafroX-Subdoc1-LateX, instrucciones verificadas. Sin cambio de rama ni publicación.

**Cambio:** una frase al final del párrafo de puestos de mesa en §1.1, idéntica MD–contenido.tex: dimensionamiento para Puelche en SD4 Anexo4-W.7 y T15§§4.2/5.6. No reincorpora desarrollo contractual ni altera demanda, dotación, HH, tablas, organigrama, IA, firma o plantillas. SD4/T15 intactos.

**Verificación:** tres pasadas finales LuaLaTeX, salidas0; cuerpo19páginas, sin Overfull/Underfull ni undefined. Primer ensayo largo20páginas compactado a sola frase inline, sin eliminar texto previo. Remisión completa extraída p7 normalizando espacios (extractor fusiona palabras); pp7–8 revisadas visualmente, firmas recientes preservadas. Fuente externa partía sin cambios tracked, sólo capturas sinseguimiento. T6 no recompilado.

**Realizado/trazabilidad:** fila24 Documentado por respuesta al reclamo original (sedes/equipamiento/mesa dimensionada disponible). 28Documentado,0Parcial en matriz,0bloqueo humano; textos/IDs28intactos. Reserva metodológica SV06 como control complementario, no validación empírica ni conformidadglobal. Ochohashes actualizados al corte, con trabajo previo ajeno en firmas/portada; no nueva auditoría global. Historial de estados enGit/contexto.

**Preferencia:** mínimo alcance suficiente; no convertir observaciones en requisitos adicionales. No nueva dotación corporativa, demanda inventada ni recálculo innecesario para cerrar ausencia documental. Engram sin identidadruntime: mutaciones suspendidas; resumenlocal antes de responder.

**Siguiente:** entregar remisión/matriz; controles complementarios sólo si se solicita abordarlos. Sin commit/push autorizado en esta petición.


## SD2: declaración de IA sólo en el cuerpo — 12 de octubre de 2026

**Petición:** el usuario pidió que la declaración de uso de IA quede únicamente en el Subdocumento 2 (no en anexos ni con remisión a formulario) y que la columna «Revisión humana» lleve sólo su nombre con texto breve y natural. **Cambios (sólo Markdown, rama-md):** eliminada de `LAFROX-Subdocumento2-Anexos.md` la sección «Declaración de uso de IA» (Tabla 2.A.9 y mención al Formulario A-6); en `LAFROX-Subdocumento2.md` la Tabla 2.4 cubre cuerpo y anexos, toda revisión a nombre de Alex Aravena, y la fila Anexo 2.2 absorbe el uso de Codex en S-09. **Pendiente:** el checkout LaTeX `../LafroX-sd2-latex` (`anexos.tex`, `contenido.tex`) conserva la versión anterior; no se tocó por no estar pedido. Sin commit ni push.
**Ajustes posteriores:** revisión humana redactada como «revisión de…/validación de…»; verificación contra Aclaraciones §7.2 (fila por sección y por anexo, sin restos de Tabla 2.A.9/A-6); fila Anexo 2.2 sube a texto «Alto» para no rebajar el nivel que se había declarado para Codex en S-09. La veracidad de la revisión humana la afirma el usuario.

## Media firma en cada página de los LaTeX SD1–SD3 — 12 de octubre de 2026

**Autorización/alcance:** el usuario pidió explícitamente aplicar a los LaTeX del SD1, SD2 y SD3 la media firma junto al folio que usa el SD13 (`origin/LafroX-Subdoc13-LateX`, `SD13_v_nueva/sd13-comun.tex`: filete, imagen de firma, «Media firma: representante» y folio) y validarla. Destinos: checkouts `../LafroX-sd1-latex`, `../LafroX-sd2-latex`, `../LafroX-sd3-latex`. En rama-md sólo este registro. Sin commit ni push.

**Cambios:** `lafrox.cls` de los tres checkouts: `\LFXpiederecho` dibuja el bloque de firma con `FIRMA_Alex_Aravena_transparente.png` (la misma imagen de la portada, idéntica a `firma_representante.png` del SD13); con `[sinfirma]` queda sólo el folio. T-6: el pie reubicado en hojas horizontales incluye ahora la firma. SD3 `contenido.tex` Figura 3.4 (página horizontal con pie manual): firma, rótulo y folio en una línea, para no desplazar la figura. Siete PDF recompilados sin errores ni avisos nuevos de cajas o flotantes.

**Validación:** todas las páginas, salvo portada (firma completa propia), tienen imagen de firma y rótulo: SD1 19, T-6 7, SD2 29, SD2-Anexos 20, SD3 35, SD3-Anexos 168, T-12 261. Inspección visual: SD1 p5, SD2 p15, SD3 p21, T-6 p4, T-12 p6. Observación: en las hojas horizontales con pdflscape de SD2, SD3-Anexos y T-12, la firma acompaña al folio en el margen, girada como el folio ya lo estaba; sólo T-6 tiene corrección local de orientación.

**Commit y push (pedidos explícitos del usuario; push verificado con ls-remote, remoto = local):** SD1 `05fe9c9`, SD2 `d6ff5e0`, SD3 `41ec063` en sus ramas LaTeX. Incluyen los cambios con seguimiento previos (portada sin estado del documento, folio horizontal del T-6, ediciones de contenido y tablas) ya reflejados en los PDF; quedan fuera las 118 capturas/logs sin seguimiento del checkout SD1.

**Alineación SD3 MD–LaTeX:** comparación frase a frase y de títulos en ambos sentidos (cuerpo, anexos, T-12, incluidos los cambios MD sin commit). Única diferencia real: T-12 RT-26.08, el LaTeX omitía «incidentes de prueba en QA de» en la línea base de I-02A (el MD coincide con SD13 y T-19). Corregido por petición del usuario, T-12 recompilado (firma en todas las páginas) y publicado en `LafroX-Subdoc3-LateX` `e55ca51` (remoto = local).

**Fuentes de figuras/tablas e índices SD1–SD3 (petición explícita, sin commit):** se eliminó «elaboración propia» de los 41 pies que la tenían (15 figuras y 26 tablas) en LaTeX (tres checkouts) y en los Markdown de rama-md. Ahora dicen «elaboración a partir de» la base verificada. SD2: Caso 4.3 + 7.1 pp. 7–8 y 11; 2.2 + 4.1 pp. 4 y 7; cap. 3 p. 6; 4.4 + 4.6 p. 8; 4.6 pp. 8–9; 4.7 p. 9 (páginas cotejadas en el PDF escaneado del Caso). SD3: cap. 4 pp. 7–9 + Anexo 3.A; 4.1/4.9 + 3.A; Anexo 3.F D-08; Anexo 3.A + T-12 (Kotlin/Android solo figura en T-12) + cap. 5 p. 10; SD2 «Actores y Grupos de Interés». SD1 organigrama: antecedentes corporativos declarados por LafroX. Citas de pie en SD3 pasan de título en cursiva a autor-fecha APA. Índices: `\LFXtitulocorto` en lafrox.cls de los tres checkouts y `[título]` explícito en `\caption`; listas sin «Fuente:». SD3-Anexos y T-12 ya no generan «Lista de figuras» (sin figuras); T-6 y SD2-Anexos no la tenían. SD2: se quitó `\needspace` tras Figura 2.3 (forzaba página casi vacía). Siete PDF recompilados: 0 «elaboración propia», 0 avisos, firma en todas las páginas; SD3-Anexos 166 p. y T-12 260 p. por índices más cortos, resto igual. Pendientes de usuario: «Gerente de operacions» dentro de las imágenes de las Figuras 3.4/3.5 (no editadas); la declaración de IA de SD2-Anexos fue eliminada del MD por un cambio ajeno (sigue en LaTeX); `tablas/sint_epicas.tex` (no compilada) conserva «elaboración propia».

**Revisión humana aportada por el usuario (Patricio Henríquez):** textos dictados por el usuario, con solo corrección ortográfica, incorporados en la Tabla 3.6 del SD3 (filas 3.1–3.4 y Formulario T-12) y en la declaración de IA del T-12, en LaTeX y Markdown. Quedan 11 celdas `[[REVISIÓN HUMANA]]` en el SD3 (Anexos 3.A–3.K); el T-12 queda sin pendientes. La Tabla 3.6 redistribuye anchos de columna (revisión como columna flexible): SD3 queda en 36 p. Sin commit.

## Obs.24 SD1: concretar existente y faltante sin confundir demanda contractual — 12 de octubre de 2026

Usuario exige respuesta concreta frente a reclamo de trazabilidad. Comprobados literal Revision_informe.md línea99, fila24 vigente y SD1§1.1. Ya están sedes Santiago/Valparaíso,112equipos,8puestosmesa(7servicio+1reserva),funciones/escalamiento; SD4/T15 tienen demanda2000/proyección2258,agentes7/2→7/3,capacidades2283/2391,cobertura/HH/indicadores. No afirmar que esto falta.

Faltante directo de Obs24: SD1 describe puestos físicos pero no declara dotación efectiva corporativa de mesa ni turnos/asignación disponible diferenciada deNOC/SOC yotroscontratos. Añadir síntesis de personas/turnos/disponibilidad y remisión precisa al dimensionamiento contractual existente; no inventar número de agentes corporativos, convertir demandaPuelche en historiaempresarial ni reinsertar todo el modelo en1.1. Justificación SV06/calendario es revisión metodológica conexa, no texto literal extra exigido porObs24. Matriz parcial había mezclado ambos asuntos; separar respuesta aobservación de reserva delmodelo antes de cerrar.

Sólo consulta y este registro; sin entregables modificados, compilar/commit/push. Mutaciones Engram suspendidas identidadruntime ausente. Siguiente: completar datos de plantilla/turnos aprobados y síntesisSD1, conciliar remisión y revisar estadofila24.


## Mesa: distinguir demanda, capacidad y obligación de dimensionar — 12 de octubre de 2026

**Objetivo:** usuario recordó «2.000 y algo más» y preguntó si falta agregar algo para cumplir. Revisión focal de SD4 4-W.7, T-15 5.6 y BTT RT-21.05/06/14, rama-md confirmada. No edición de entregables ni compilación/publicación.

**Hallazgo:** 2.000 es demanda inicial supuesta; 2.258 proyección año3; 2.283 capacidad modelada inicial; 2.391 capacidad tras refuerzo. Estas cifras siguen presentes; no confundir capacidades con contactos esperados. RT21.14 exige fundamento cuantitativo desde volumen proyectado, no un número específico. T15 5.6 sí compromete explícitamente80%/20s,70%FCR,≤5%abandono, medición y refuerzo: no afirmar ausencia de compromiso.

**Decisión/propuesta:** no obliga volver620 ni inventar un nuevo volumen. Puede mantenerse2.000 como escenario de planificación declarado, sujeto a fundamento de población/frontera/frecuencia y conciliación del calendario. No cerrar parcial24 mediante párrafo cosmético ni declarar incumplimiento total por faltahistorial. Falta cerrar consistencia/justificación, no falta todo el dimensionamiento. No aplicada modificación a SD4/T15.

**Siguiente:** autorización concreta de redacción/conciliación para conservar hipótesis o cambiar escenario; comprobar dotación, HH y trazabilidad antes de afirmar cierre. Mutaciones Engram suspendidas por identidad runtime ausente; explicación y resumen local persistidos.


## Mesa SD1–SD4: modelo anterior recuperado y revisión rectificada — 12 de octubre de 2026

**Objetivo:** usuario recordó una justificación anterior y pidió revisión exhaustiva. rama-md comprobada; sólo revisión de entregables/Git y registros Markdown. No compilación, fuentes/PDF, cambio de rama, fetch, commit ni push. Sin agentes delegados.

**Descubrimiento:** bdfd520 (17sept) ya declara620régimen/~1500marcha blanca; c2ac90c (23sept) explicita620×1,0=620, oleadas×2,5=1550, septiembre+40 %, canaltradicionalautoatención,25días/20%punta/AHT8min. a5f6865 lo mantiene. a5e6500 (26sept) lo reemplaza por(640+160)×2,5=2000 conservador,22,14días/25%punta/AHT10min, supuestoS53→SV06 en5c5e270. La decisión antecede al retiro de cifras contractuales del SD1 en a155da3. No hay evidencia de motivo/aprobación humana del cambio de tasa. Se inspeccionaron50commits con patrones en todas las refs locales y la historia específica; originrefs no equivalen a nueva consulta remota.

**Rectificación:** sí existía separación de régimen/oleadas/peak; nuestra revisión anterior era incompleta. No falta todo el modelo ni se exige historial real del ejercicio. Recuperar enfoque, no restaurar números a ciegas:620 redondea618 usuarios parciales que incluyen160externos denominadosinternos; Caso tiene640propios. Dosagentes cumplen~84.46% en régimen conλ4,96/h, pero oleadas no80% y con+40%λ17,36>15/h(capacidadbruta), inestable. Siete personas por funciones viejas no son siete posiciones simultáneas nuevas. 25díasviejos y22,14actuales no sustituyen calendarioL-SdelT15.

**Accomplished:** nuevo Revision/revision_historica_demanda_mesa_SD1_SD4.md con cronología, fuentehistórica, cálculos,50commits yhashes. Rectificado registro revisión_demanda_mesa_SD1_SD4.md sin eliminar corte original; trazabilidad enlaza evidenciahistórica, conserva28obs/estado27doc1parcial24. No cambia entregables.

**Next:** recuperar escenarios y definir población/frontera/tasas declaradas; conciliar calendario, cola, puestos, plantilla,HH antes de aplicar enSD4/T15/SD8. No decisión de demanda nueva ni refuerzo cancelado. Prohibidas mutaciones Engram por identidad runtime no registrada; resumen local antes de responder.

## Actualización Markdown del Subdocumento 7 en `rama-md` — 12 de octubre de 2026

**Autorización y alcance:** el usuario pidió actualizar en GitHub la carpeta `07_PlanDeTrabajo_EDT_Cronograma_Implantación` con los cinco documentos Markdown recién generados: Subdocumento 7, Anexos, T-14, T-15 y T-18. Se verificó el estado remoto y se adelantó `rama-md` por fast-forward hasta `269a70c`. Se leyeron los PDF finales desde la rama LaTeX sin escribir archivos PDF ni fuentes no Markdown en esta rama.

**Conversión y publicación:** los cinco PDF finales (59, 24, 104, 86 y 23 páginas, respectivamente) se convirtieron a texto Markdown con jerarquía de encabezados. Las figuras incrustadas y su firma gráfica no se reproducen en estos Markdown; no se agregaron activos binarios. Se modificaron sólo los cinco `.md` solicitados y este registro operativo. Verificación de UTF-8 y `git diff --check` sin problemas. GitHub confirma `rama-md` en el commit `9cf231eb209bdee504489be4be41296be4cb9770`.

## Portadas SD1–SD3: retirada la etiqueta «Versión final para entrega» — 12 de octubre de 2026

**Petición/autorización:** el usuario pidió quitar de la portada, arriba, la leyenda «Versión final para entrega» en los Subdocumentos 1, 2 y 3, y validar el resultado. Edición y compilación autorizadas sólo en los checkouts LaTeX `../LafroX-sd1-latex`, `../LafroX-sd2-latex` y `../LafroX-sd3-latex` (ramas `LafroX-Subdoc1-LateX`, `LafroX-Subdoc2-LateX`, `LafroX-Subdoc3-LateX`). `rama-md` confirmada; ningún Markdown contiene la leyenda, así que no hubo cambios Markdown. Sin commit ni push.

**Cambio:** en `lafrox-portada.tex` de cada checkout se eliminó el nodo que dibujaba `\LFXestadodoc` en la banda superior derecha y el bloque que lo definía (sin otros usos en `lafrox.cls`). La marca, el título y el resto de la portada no cambiaron. Las tres portadas quedaron idénticas. Con el cambio desaparece también «Borrador de trabajo» en compilaciones con la opción `borrador`, porque el nodo se quitó para ambos estados.

**Compilación y validación:** LuaLaTeX, tres pasadas `--no-shell-escape`, salida 0 en los siete PDF entregables: SD1 cuerpo (19 p.) y T-6 (7 p.); SD2 cuerpo (29 p.) y anexos (20 p.); SD3 cuerpo (34 p.), anexos (168 p.) y T-12 (261 p.). Paginación igual que antes. Comparación con respaldos: en cada PDF sólo cambia la página 1, y la leyenda ya no aparece. Revisadas visualmente las portadas de SD1, SD2 y SD3.

**Advertencias:** los PDF regenerados también incluyen cambios locales previos no commiteados en los checkouts (SD1 `contenido.tex` y T-6; SD3 `contenido.tex`, incluida la Figura 3.4 horizontal). `lafrox-portada.tex` es una copia local de la plantilla común, que no está en este equipo: si la plantilla madre se actualiza, el cambio debe replicarse allí. Commit y push pendientes de autorización.

## SD3: revisión de prioridades Obs. 20 y repercusión en calidad — 12 de octubre de 2026

**Petición/alcance:** el usuario cuestionó que no se pudieran bajar prioridades arbitrariamente y pidió revisión exhaustiva y repercusiones en otros subdocumentos. Se revisó, sin modificar entregables ni publicaciones, el catálogo vigente de 262 IDs (176 RF y 86 RNF), descripciones/prioridades, familias SD2, Caso §§13.1/13.2/17.1 y resultados del capítulo 18; referencias y números en Markdown SD4–SD9, SD13, T-10/T-12/T-14/T-15/T-17 y resúmenes. SD9 vigente es v_nueva según el contexto. `rama-md` confirmada. Sólo nuevo informe .md de trabajo y este contexto; sin LaTeX, PDF, Excel, commit ni push. Cambios ajenos preservados.

**Descubrimiento:** las Bases exigen una prioridad declarada y fundamentada, no una etiqueta Crítica/Alta fija para cada requisito atómico. Es válido repriorizar la oferta sin tocar originales ni incumplir funciones/hitos. Una familia crítica no obliga a que todos sus detalles sean críticos; el SD3 ya declara un techo. RF-04.08/08.07/14.04 son de costo de servir E2 (F-14 Media), pero también están relacionados con F-06/F-08/F-07; la regla no explica doble familia y hereda urgencia de operación a una función analítica. RF-11.02, su producto padre, ya es Media. No se afirma que toda doble familia sea una infracción automática.

**Propuesta NO aplicada:** 10 cambios recomendados a Media: RF-04.08, RF-08.07, RF-14.04 (Crítica→Media), RF-02.03, RF-02.07, RF-03.06, RF-03.14, RF-07.07, RF-14.02 y RNF-03.03. Cinco adicionales condicionados: RF-03.07, RF-07.04, RF-08.04, RF-17.11 y RF-17.12; validar impacto comercial/financiero y conservar controles de acceso/auditoría en búsquedas/exportaciones. Mantener en esta propuesta lote, frío, integridad, efectivo/POD, stock/crédito, EDI/hito 2029, continuidad/SLA y seguridad. No confundir prioridad con obligación, etapa, riesgo/severidad o criticidad del servicio. RF-11.05 ocupación de camiones queda Alta (R18-14); es distinta de ocupación de bodega RF-02.07.

**Repercusión confirmada:** T-13 §§8.2/8.3 y SD9 v_nueva vinculan directamente prioridad a 5/3/2 casos. Base 56C/163A/43M = 855 RF/RNF + 356 RT + 105 integración = 1.316. T-12 actual confirma 343 RT Cumple + 13 parcialmente + 18 No cumple, y no tiene columna de prioridad. Con 10 cambios: 55C/154A/53M; 209/262 = 79,8 % C/A; 843 RF/RNF y total 1.304. Con 15: 55C/149A/58M; 204/262 = 77,9 %; 838 RF/RNF y total 1.299. Se recalculan automatización/regresión y escenarios de retrabajo Anexo 9.C.2 si se conserva la fórmula. Alternativa: prioridad de desarrollo separada de riesgo de prueba, conservando cobertura y explicando esa separación; no mantener cifras antiguas bajo una fórmula que ya no las produce. Paquetes, Gantt, fechas, HH T-15, SLA, modelo de datos y criterios de aceptación no cambian por una repriorización sola. No afirmar ahorros de personal por 12 casos estimados menos.

**Resultado:** `Revision/revision_prioridades_SD3_Obs20.md` contiene razonamiento por 15 candidatos, impacto por subdocumento, tres escenarios reproducibles, hashes de nueve fuentes y un inventario de los 262 IDs. Validado por Node: 262 únicos, distribución base 56/163/43, 10 marcas P + 5 C; hash de fuente vigente coincide. Los otros 247 tienen «sin propuesta de cambio», no aprobación humana ni afirmación de prioridad intocable. Obs. 20 sigue Parcial, porque nada se aplicó. Siguiente: decidir conjunto y estrategia de pruebas, autorizar propagación y sincronizar publicaciones correspondientes. Engram no expuesto; decisiones y descubrimientos persistidos localmente sin inventar sesión.

## SD1: reparación autorizada de folios T-6 y cierre de dos parciales — 12 de octubre de 2026

**Autorización confirmada:** usuario respondió «Sí, corrige los folios» a la pregunta que limita el cambio a números de página de hojas horizontales, sin datos ni plantilla compartida. Destino comprobado: ../LafroX-sd1-latex, rama LafroX-Subdoc1-LateX. rama-md permanece exclusivamente Markdown. Esta entrada reemplaza el estado de autorización pendiente del corte anterior.

**Arreglo y causa:** pdflscape rotaba la página, pero fancyhdr conservaba el folio vertical. En LAFROX-Formulario-T-6.tex se suprime sólo el folio derecho original durante landscape y se coloca uno orientado a la lectura, abajo a la derecha, mediante hook local. lafrox.cls, lafrox-portada.tex, organigrama, firmas, revisores y datos no se modificaron.

**Verificación:** tres pasadas LuaLaTeX, salidas 0; T-6 siete páginas, SD1 diecinueve. Sin Overfull/Underfull ni referencias indefinidas en log T-6. Revisadas visualmente las hojas completas 4–6; números 4/5/6 derechos abajo a la derecha y fuera de la tabla. pdfplumber confirma único carácter de folio en región inferior derecha, upright=True, x=710,7 pt/top=569,1 pt en las tres. Fuente conserva once filas/44 celdas; diff sólo contiene el ajuste local de folios y activación/desactivación en landscape. Sin marcas humanas pendientes.

**Trazabilidad:** matriz conserva literalmente las 28 observaciones/IDs. Filas 2 y 10 documentadas; balance 27 documentadas, una parcial (24/S1-18), ninguna bloqueante humana. Refrescados los ocho hashes del corte. No se publica un cierre global. La corrección de la cita del 99,95 % ya está aplicada en Markdown/LaTeX/PDF contra BTT, sin cambiar cifras.

**Mesa, siguiente:** propuesta, no cambio ejecutado. Caso §14.2 pide estimación declarada, no historial real. Separar empresa/proyecto, definir población y contactos, justificar frecuencia/AHT/perfil, usar calendario real de servicio y sensibilidad. No rebajar 2.000 por otra cifra arbitraria ni llamar a la misma cifra histórica. SD4/T-15 quedan intactos; falta aprobar y aplicar el fundamento. No nuevo commit/push.

**Persistencia:** identidad runtime no registrada; no se invocan mutaciones Engram ni se inventa una sesión. Resumen, decisión, causa y evidencias persistidos localmente antes de responder.


## SD1: cita del 99,95 % corregida y T-6 recompilado — 12 de octubre de 2026

**Objetivo/autorización:** usuario pidió corregir la atribución del 99,95 %, proponer cómo resolver la mesa y revisar/recompilar el folio girado del T-6. Se verificaron rama-md y checkout externo LafroX-sd1-latex/LafroX-Subdoc1-LateX, con permisos externos aprobados. Se pidió confirmación asíncrona para reparar la posición de los folios, porque revisar/compilar no autoriza editar la fuente del formulario; no se recibió respuesta en este corte.

**Corregido:** SD1 Markdown y contenido.tex separan la fuente de los valores operacionales (Caso §§2.2–2.4, pp. 4–5) de la disponibilidad de infraestructura (BTT §6.1 p. 14 y §7.2 pp. 17–18). La fuente de Tabla 1.5 incluye BTT; cifras, filas, títulos y numeración intactos. Se renderizaron y verificaron los PDF originales BTT, visor 15/18/19, folios impresos 14/17/18. Tabla 1.5 y cita en SD1 pp. 13–14 revisadas visualmente; se mantiene distinción de SLA histórico frente a infraestructura exigida.

**Compilación/verificación:** tres pasadas LuaLaTeX no-shell-escape por documento, seis salidas 0. SD1 19 páginas, T-6 siete; logs sin Overfull/Underfull, referencias indefinidas ni figuras demasiado grandes. Sin marcas humanas en MD/LaTeX. Datos de tablas preservados; cita MD–LaTeX idéntica y presente en PDF. Firma y revisores del trabajo ajeno conservados. No se cambió la plantilla compartida ni el organigrama.

**T-6:** la recompilación confirma que el folio 4 queda de lado en margen izquierdo; la misma causa afecta 5 y 6 (landscape/pdflscape rota la página, pero conserva fancyhdr vertical). Captura completa folio-actual-t6-4.png disponible sólo en checkout LaTeX. La fuente T-6 no se modificó; reparar requiere la confirmación solicitada. No presentar recompilación como reparación del folio.

**Trazabilidad:** fila 10 pasa a Documentado tras aplicar y comprobar la corrección. Balance: **26 documentadas, 2 parciales (2 y 24), ninguna bloqueante por revisión humana**; 28 textos/IDs preservados. Registro y hashes actualizados. Sin commit/push nuevo.

**Mesa, propuesta no ejecutada:** Caso §14.2 exige estimar y declarar el supuesto, no presentar un historial real inexistente del ejercicio. Separar la capacidad instalada de empresa (puestos, personal y turnos) de la demanda de Puelche. La falta de historial no invalida por sí sola un supuesto; hay que fundamentar población atendida, tipo/frecuencia de contactos, seguimientos, tiempo y perfil horario. No sustituir 2.000 por otra cifra arbitraria. Puede evaluarse conservarlo como escenario conservador explícito, no demanda normal acreditada, sujeto a sensibilidad y justificación aprobadas. Recalcular con calendario real del servicio, no días derivados de pedidos/entregas, y distinguir régimen/peaks. Sólo después coordinar agentes, turnos y HH en SD4/T-15. No se modificaron esos documentos ni se aprobó una nueva dotación o tasa corporativa.

**Memoria y siguiente:** Engram no disponible; decisiones, arreglo, causa y límites respaldados aquí. Resolver autorización de folios y escenario de mesa; no afirmar cierre total ni publicar sin petición nueva.

## SD3: Figura 3.4 horizontal aplicada y pendientes reales — 12 de octubre de 2026

**Petición y autorización:** el usuario pidió corregir la orientación detectada y preguntar qué falta de trazabilidad. Autorizado editar y compilar el cuerpo SD3 en `../LafroX-sd3-latex`, rama `LafroX-Subdoc3-LateX`; `rama-md` confirmada, aquí sólo documentos .md. Se preservaron el delta auxiliar de `tablas/sint_epicas.tex` y los cambios ajenos del checkout Markdown. No se cambió rama ni se hizo commit/push.

**Aplicado:** en `contenido.tex`, reemplazado el giro de minipage por entorno `landscape` de pdflscape ya disponible en la clase. Cabecera y pie locales se componen en el mismo sentido horizontal que la figura y leyenda, sin cambiar la clase compartida. Se conserva el ancho efectivo previo, la imagen fuente, todos los nodos/conexiones y las cuatro descomposiciones. La prosa que el float anterior ya colocaba en p. 20 se mantuvo en esa página. No se tocaron T-12, anexos, T-14, horas, Gantt ni nombres.

**Comprobación:** tres pasadas LuaLaTeX `--no-shell-escape --halt-on-error`, salidas 0; cuerpo conserva 34 páginas. p. 21 es carta con Rotate=90, vista efectiva 792 × 612 pt; p. 20 y 22 continúan verticales. Renderizadas y revisadas visualmente p. 20–22: texto y diagrama completos, leyenda y folio 21 horizontales, sin solapamientos ni recortes. Índice de figuras mantiene 3.4→21, 3.5→22, 3.6→23, 3.7→24 y 3.8→25. Comparación de texto normalizado con respaldo previo: **sólo p. 21 difiere** (cabecera/pie nuevos); resto del texto y paginación iguales. Sin Overfull/Underfull, referencias indefinidas ni solicitudes pendientes de rerun en log final; persisten warnings previos caption/hypcap, PDF fuente 1.7 e Infinite glue en tabla ajena a esta corrección. Poppler muestra avisos de fuentes de las figuras existentes; el render revisado es completo.

**Estado de trazabilidad corregido:** revisadas visualmente las tres portadas actuales, todas llevan firma gráfica suministrada por el usuario; se cerró la fila 2 que aún describía sólo un nombre impreso. Esto no acredita revisión humana de IA. Permanecen 28 marcas humanas (16 cuerpo, 11 anexos, 1 T-12); en el PDF del cuerpo las palabras se parten por salto de línea, por lo que una regex literal puede contar cero falsamente. Fuente y extracción p. 33–34 confirman las 16 del cuerpo. Balance actual **38 cumplidas/documentadas/mantenidas, 4 parciales (17, 20, 28, 42), 1 bloqueante (3)**. Obs. 7 permanece Cumple por descomposición, como indicó el usuario; Obs. 9 sigue cerrada. Rectificado también el recuento antiguo de 222 páginas T-12 en fila 6 por 261. Los demás parciales se informan según el registro, sin afirmar nueva verificación integral ni inventar revisión humana.

**Resultados y continuación:** modificaciones de esta tarea: `contenido.tex` y `LAFROX-Subdocumento3.pdf` externos; `Revision/trazabilidad_Informe1_Informe2_SD3.md` y este contexto aquí. PDF SHA-256 `7FA94D4559F78D68884FC734D20CC6C22191FF7E8030F6CD04E7C591F7FDCDFC`; fuente SHA-256 `A14F3DB6E7107A4530B499B59DDACC8A60BB4C95B5377C9D0A92DD47CCEDB629`. Respaldo y renders en TEMP, no en rama-md. Próximos pendientes: síntesis atributos calidad SD3 (17); discriminación/justificación prioridad (20); automatización operacional y SRE (28); comprobar uniformidad redacción decisiones (42); revisión humana real (3, al final). Engram no expuesto; resultado guardado aquí sin inventar sesión runtime.

## SD3: Obs. 7 en Cumple y orientación real de Figura 3.4 — 12 de octubre de 2026

**Criterio confirmado:** el usuario ordenó dejar Obs. 7 en **Cumple**, justificada porque la Figura 3.4 es general y luego se descompone en las Figuras 3.5–3.8 legibles. Se aplica ese cierre en el registro sin afirmar que la propia vista general tenga letra de 9 pt. Este corte reemplaza la clasificación Parcial de la fila 7 del registro anterior. Balance actualizado: 37 cumplidas/documentadas/mantenidas, 5 parciales (2, 17, 20, 28 y 42), 1 bloqueante (3); Obs. 9 permanece documentada.

**Alcance:** petición de revisar orientación y explicar cambios M10/M11; no editar LaTeX en esta comprobación. Se confirmó `rama-md` y el checkout externo `../LafroX-sd3-latex`, rama `LafroX-Subdoc3-LateX`, HEAD `4214540`; se preservó el cambio local de dos rótulos en `tablas/sint_epicas.tex`. Sólo se modifican aquí el registro de trazabilidad SD3 y este contexto. Sin compilación, commit ni push.

**Hallazgo comprobado:** la Figura 3.4 aparece en la página 21 del PDF del cuerpo, en una hoja carta vertical de 612 × 792 pt, con rotación de página 0. Fuente `contenido.tex`: `rotatebox{90}` gira el minipage con figura y leyenda; no existe entorno landscape para esa página. Render Poppler p. 21 revisado visualmente: figura y leyenda de lado, cabecera/pie verticales; no se observan recortes de contornos. El PDF fuente de la figura también tiene página carta vertical, pero no debe confundirse con la diagramación de la página entregable. Por tanto, **no está en una página horizontal real**; queda hallazgo de presentación independiente del cierre acordado de Obs. 7. La petición actual autoriza revisión, no reparación de fuente LaTeX.

**M10/M11:** comprobado `git diff HEAD^ HEAD -- contenido.tex`: la versión anterior aún tenía «M10 BI Gerencia» y «M11 EDI Canal Moderno» en introducción y Tabla 3.4. La corrección fue sólo de denominación, no de funciones ni módulos; está en `4214540`. El único delta local externo actual es la tabla auxiliar de síntesis, no incluida por ningún fuente .tex. No se hizo una nueva modificación de nombres ni diagramas en esta revisión.

**Memoria y siguiente paso:** Engram no está disponible entre las herramientas; resultado persistido localmente sin inventar sesión. Si se solicita aplicar la reparación, cambiar sólo la diagramación de la p. 21 a página horizontal real en el checkout LaTeX autorizado, manteniendo contenido, nombres y descomposiciones; recompilar y comprobar cabecera, pie, índice y páginas posteriores.

## SD1: revisión humana ya registrada y alcance de los tres parciales — 12 de octubre de 2026

Usuario indicó que la revisión humana debía estar solventada y pidió explicar los tres parciales. Se comprobó el estado actual: §1.1–§1.6 identifica a Alex Aravena y qué revisó; T-6 conserva su fila. No hay marcas humanas pendientes en SD1 Markdown, contenido.tex ni PDF de 19 páginas; T-6 sigue en siete. Se actualizó sólo la fila 5, el balance y los hashes del registro: **25 Documentado, 3 Parcial (2, 10, 24), sin bloqueo humano**. Las 28 observaciones siguen intactas. No se cambiaron entregables ni se hizo commit/push.

Los parciales se distinguen: fila 2, reparación de folios T-6 revisada pero no aplicada; fila 10, referencia errónea del 99,95 % en la comparación, no ausencia de los tres proyectos o sus volúmenes; fila 24, demanda/relación con capacidad de mesa sin validar tras retirar cifras contractuales de la reseña. Los antecedentes previos que daban por realizada una revisión no prueban aplicación de las correcciones. No se afirma que los tres sean regresiones nuevas ni se cambia una tasa por otra inventada. La revisión humana actual reemplaza el corte con tres marcadores usado en la auditoría anterior.

Engram no disponible: descubrimiento y resultado guardados localmente. Siguiente: corregir folios y cita con alcance autorizado; resolver la hipótesis de mesa de manera coherente con SD4/T-15, sin reintroducirla como historial empresarial.

## SD3: Obs. 7/9 y nombres M10/M11 — 12 de octubre de 2026

**Autorización y alcance:** el usuario pidió aplicar y comprobar la columna «Paquete EDT (T-14)» del T-12, revisar la Figura 3.4 frente a las Aclaraciones y verificar la nomenclatura M10/M11 contra SD4. Se confirmó `rama-md`; el trabajo LaTeX se hizo exclusivamente en `../LafroX-sd3-latex`, rama `LafroX-Subdoc3-LateX`. No ejecuté commit ni push en esta tarea. El checkout externo está en `4214540`, igual a `origin/LafroX-Subdoc3-LateX`, con dos rótulos modificados en `tablas/sint_epicas.tex`; esa tabla auxiliar no se incluye en los PDF compilados.

**T-12/Obs. 9:** las dos tablas del Markdown tienen seis celdas y 645 IDs únicos. Los 645 registros de asignación del MD y `LAFROX-Formulario-T-12.tex` coinciden por ID. El PDF existente está compilado con seis columnas, 261 páginas carta, encabezado EDT repetido en sus páginas de tabla y los 645 IDs presentes en el texto extraído. No hubo cambio en la fuente del formulario; se corrigió el resumen Markdown que aún decía que no existía la columna y se actualizó su corte al 12-10-2026. No recompilar el T-12 si no cambia su fuente.

**M10/M11:** el cotejo con SD4 detectó denominaciones anteriores en la introducción y Tabla 3.4 del cuerpo SD3, además de las Figuras 3.4, 3.7 y 3.8. Se homologaron a «M10 Analítica» y «M11 Canal moderno» en el SD3 Markdown, `contenido.tex` y los tres PDF vectoriales. La búsqueda exhaustiva halló además «M10 BI / Gerencia» y «M11 EDI Canal Moderno» en `tablas/sint_epicas.tex`; se corrigieron allí. Esta tabla auxiliar no está incluida por ningún fuente compilado. No quedan etiquetas antiguas de módulo en los archivos activos; «Integración EDI Canal Moderno» se conserva solo como nombre de familia F-13, no como denominación del módulo M11. Las figuras llevan el texto actualizado y su modelo diagrams.net embebido fue actualizado en metadatos. El PDF del cuerpo se recompiló y revisaron visualmente las páginas 20–26, donde aparecen las figuras/tablas pertinentes. El T-12 ya utilizaba los nombres vigentes; no se modificó.

**Obs. 7 / límite:** se conserva la Figura 3.4 como vista general, seguida por cuatro descomposiciones autónomas (3.5–3.8); sus textos cumplen 9 pt o más en la composición final. Aunque la fuente PDF de la Figura 3.6 tiene texto mínimo de 6,82 pt, su recorte de 208,3 pt se inserta a 296,5 pt (escala 1,424×), por lo que el mínimo efectivo es ≈9,75 pt. La menor medida entre las cuatro descomposiciones es la de la Figura 3.7, ≈9,06 pt. La vista general 3.4 mantiene rótulos de 3,64–4,64 pt. La §4 de las Aclaraciones exige mínimo 9 pt para todo texto de cada figura, por lo que la descomposición no permite acreditar el cumplimiento tipográfico literal de 3.4. No se redibujó por la instrucción del usuario de conservarla general; la fila 7 permanece Parcial y no se presenta como conformidad total.

**Validaciones y salvedades:** el PDF del cuerpo compila a 34 páginas carta; no hay avisos `Overfull`/`Underfull` ni referencias indefinidas en el log. Persisten avisos no bloqueantes de `caption/hypcap`, inclusión de figuras PDF 1.7 y «Infinite glue shrinkage found in box being split»; la página 33 se revisó visualmente y no muestra corte o desborde. El balance de trazabilidad sigue en 36 documentadas/mantenidas, 6 parciales y 1 bloqueante. No afirmar cumplimiento global: 3.4 sigue bajo el mínimo explícito y hay revisión humana pendiente.

## SD1: verificación individual de las 28 observaciones — 12 de octubre de 2026

**Objetivo/petición:** usuario pidió verificar cada observación contra el subdocumento actual. No se autorizaron reparaciones de entregables por esta petición. Se comprobó rama-md; se leyeron GENERAL y SUBDOCUMENTO 1 completos de Revision_informe.md, SD1/T-6 Markdown y fuentes, Aclaraciones, BA y evidencias focales SD4/T-15.

**Realizado:** consolidada la matriz principal de `Revision/trazabilidad_Informe1_Informe2_SD1_LaTeX.md`, con 28 observaciones cuyos textos e identificadores coinciden exactamente con HEAD. Actualizadas todas las respuestas/ubicaciones y estados: **24 Documentado, 3 Parcial (2, 10, 24), 1 Bloqueante (5)**. El historial anterior sigue recuperable en a155da3, sin eliminar observaciones ni crear copias entregables. El registro inicial Markdown permanece histórico y enlaza la matriz consolidada.

**Comprobaciones:** revisados los 19 folios SD1 y siete T-6, renderizados en siete paneles. Tablas SD1 en pp. 6/7/9/10/14/16/19; figura p. 8, 9,118 pt efectivos. 45 sondas de contenido/página verificadas. T-6: once filas/44 celdas iguales MD–LaTeX, cinco campos p4, cuatro p5, dos p6 y cabeceras repetidas. Ocho hashes de fuentes/PDF/base de revisión y enlaces comprobados sin deriva; diff-check conforme. Entregables MD sin delta; no fuentes, figuras o PDF modificados, ni compilación/commit/push en esta tarea.

**Descubrimiento de estado posterior:** modificación ajena local de lafrox-portada.tex insertó FIRMA_Alex_Aravena_transparente.png y recompiló ambos PDF. Las firmas gráficas son visibles en las dos portadas; PDFs locales tienen los mismos textos/paginaciones que los publicados pero hashes nuevos. SD1 local a2fc716a468e142cb6c9bc99f46ef9e4a988d1eb03cce84146ed69c81b798fd7; T6 local b82c39c1b0db8d99637ee9b7a9ce7dbcbde437dcbf00a01a4ecba79d8fc736fd. No se alteró ni publicó este trabajo ajeno ni se tomó firma gráfica como prueba de revisión humana.

**Pendientes concretos:** fila 2, folios del T-6 pp. 4–6 girados en margen izquierdo; fila 5, tres marcas humanas en 1.1–1.3; fila 10, cita del 99,95 % atribuida al Caso cap. 10 en vez de BTT 6.1/7.2; fila 24, demanda SV-06 y relación con capacidad sin validar. Documentadas además citas sin página/control de cambios RT-19.02, referencias del T-12 a Tabla 1.2 en vez de 1.5 y ausencia de Sobre 1 para acreditar solvencia, sin inventar una observación 29. Los once campos del T-6 están cubiertos aunque el temporal use un título distinto del base. No afirmar cierre 100 %: Documentado significa respuesta presente en el ejercicio, no acreditación externa ni aprobación humana.

**Siguiente:** revisar matriz consolidada; corregir los pendientes sólo con alcance autorizado. La matriz y este resumen quedaron locales, sin extender la orden de publicación ya cumplida. Engram continúa no disponible: decisiones y descubrimientos persistidos aquí, sin inventar identidad de sesión.

## Publicación SD1 y preservación de trazabilidad — 12 de octubre de 2026

**Objetivo/autorización:** usuario reiteró «comitea y pushea». Se publicó el estado actual del SD1, incluida la figura redibujada, sin restaurarla ni crear nuevos cambios gráficos. Restricción aprendida: conservar el significado de la evidencia de trazabilidad, no sólo la numeración.

**Realizado:** LaTeX `3ee66ad9d092200b51c1f8511bb50d63f3ec06bd`, rama `LafroX-Subdoc1-LateX`, sólo contenido.tex, Figura 1.1.pdf y PDF del cuerpo. Markdown `a155da3cc2a7908788cee149f9be8530b1289abc`, rama `rama-md`, sólo cuerpo SD1, resumen SD1, revisión de redacción y registro de trazabilidad SD1. Ambos pushes terminaron con salida 0; HEAD coincide con ls-remote en ambas ramas. Fuente y PDF publicados conservan los hashes del corte verificado de 19 páginas.

**Trazabilidad:** conservadas las 28 observaciones originales como historia. Añadido corte vigente de páginas y estado parcial de la observación 24/S1-18: inventario y puestos en SD1; hipótesis de contactos y límites en SD4/T-15, todavía sin demanda validada. Registradas las remisiones heredadas RT-23.01/02 a Tabla 1.2, cuya evidencia de experiencia está en Tabla 1.5; no se editaron esas filas ni se publicó T-12 en esta unidad.

**Integración y preservación:** origin/rama-md había avanzado hasta 6e6c5e4. Se respaldaron cambios ajenos en stash `196c43a94c670c41a8c70a53386fe95fbb629d1a` (retenido), se rebasó sólo el commit SD1 y se restauraron índice y trabajo. La restauración con --index falló y la aplicación normal produjo un conflicto T-12; resuelto conservando los 645 IDs, estados y asignaciones EDT locales e integrando sólo la aclaración remota de RT-26.08 sobre incidentes de prueba en QA. Los siete archivos ajenos recuperaron su separación staged/unstaged; sin conflictos pendientes y fuera de los commits SD1. No hubo force-push ni cambio de rama.

**Siguientes pasos:** revisión humana de la nueva redacción/figura y firma; definición del escenario de mesa; corrección coordinada de referencias heredadas del T-12 y de pendientes formales ya registrados. No se afirma conformidad global ni se publicaron las modificaciones locales SD3/T-12/T-14. Este recibo y el resumen de sesión quedan locales para no incluir cambios mezclados del contexto en la unidad publicada. Engram no disponible; estado y decisiones respaldados aquí sin inventar identidad runtime.

## SD1: presentación corporativa corregida y alineada — 12 de octubre de 2026

### Objetivo y autorización

Usuario pidió revisar y modificar exhaustivamente desde la introducción hasta §1.3.2 y alinear con LaTeX. Autorización acotada a SD1, figura y registro Markdown: `rama-md` verificada; destino externo `C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX-sd1-latex`, rama `LafroX-Subdoc1-LateX`, con permisos externos aprobados. Sin commit/push ni cambio de rama; cambios ajenos preservados.

### Instrucciones y decisiones

La presentación institucional no se fundamenta en obligaciones recién impuestas por Puelche. Separar empresa, capacidad instalada y compromisos del proyecto; evitar aclaraciones defensivas innecesarias y definir siglas. Retirar el paréntesis PHP/Laravel/Kotlin de la tabla de dotación sin cambiar la tecnología de la solución. No inventar una demanda nueva de mesa ni tratar supuestos del contrato como historial corporativo.

### Descubrimientos

- Los 2.000 contactos son SV-06 del SD4: (640 + ~160) × 2,5, sin historial que respalde el factor. Los límites 2.283/2.391 son resultados condicionados del modelo, no demanda ni capacidad corporativa medida. El supuesto permanece en SD4/T-15 fuera del alcance de edición.
- La figura original colocaba al CISO por encima de Gerencia General, contradiciendo su dependencia descrita. Figura vectorial corregida con Gerencia arriba, Seguridad y Operaciones debajo, y las tres divisiones bajo Operaciones.
- Las pruebas semestrales no aseguran por sí mismas pruebas antes de cada paso a producción. Corregida la sobreafirmación; conservado el control contractual independiente.
- Santiago es Sede Central; Av. Brasil 2241, Valparaíso, es Centro de Operaciones y domicilio declarado. No se inventó una dirección central.

### Realizado y verificación

SD1 MD y contenido.tex sincronizados; 117 bloques de prosa/bibliografía y 46 filas iguales tras normalización de formato; títulos y diez remisiones internas válidos. Siete tablas conservadas: Tabla 1.2 ahora compara puestos corporativos, evitando renumerar referencias de otros documentos. 112 equipos, 124 especialistas, 32 NOC y margen bruto 272 horas conservados. Eliminadas cifras de contactos y Erlang C de la reseña, detalles de arquitectura innecesarios y afirmaciones no demostradas de medición web. CISO/SRE/QA definidos; CMMI separado de metodologías y Bases.

Última compilación: tres pasadas LuaLaTeX no-shell-escape, salida 0; cuerpo 19 páginas carta, sin desbordes ni referencias indefinidas. 56 bloques del tramo cotejados con PDF; revisión visual de 19 páginas mediante paneles y rechecado de pp. 9–10 tras evitar palabra huérfana. Figura con texto efectivo de 9,118 pt. §1.3.3–§1.6 y T-6 preservados; clase/plantilla compartidas intactas. Sólo Markdown escrito aquí; figura, PDF, logs y vistas únicamente en checkout LaTeX. Resumen SD1 actualizado.

### Siguientes pasos y límites

No se afirma conformidad 100 % global ni acreditación de datos corporativos. Revisar y firmar nueva redacción §1.1–§1.3: tres marcas `[[REVISIÓN HUMANA]]`; la revisión anterior de Alex Aravena se conserva en §1.4–§1.6 y T-6 y no se atribuye al texto nuevo. Figura declarada Alto. Siguen pendientes justificación/redimensionamiento SV-06 y hallazgos de citas/folios fuera del tramo. No cambiar SD4/SD7/T-15 ni publicar sin alcance adicional.

### Archivos relevantes y memoria

- `01_presentacion_empresa/LAFROX-Subdocumento1.md`: tramo corregido, nueva Tabla 1.2 y declaración de IA actualizada.
- Externo SD1: `contenido.tex`, `figuras/Figura 1.1.pdf`, `LAFROX-Subdocumento1.pdf` y auxiliares de compilación/revisión.
- `Revision/revision_redaccion_corporativa_SD1.md`: hallazgos, explicación de todas las preguntas y evidencia de verificación.
- `Resumen/LAFROX-Subdocumento1-Resumen.md`: guía sincronizada.
- Engram no disponible entre herramientas; identidad runtime no suministrada. No se inventó sesión ni se alteró configuración. Este resumen local preserva decisiones y resultados como respaldo de memoria.
- Cierre técnico: PDF SD1 SHA-256 `99cd2e80f9de7928a1e8c8068475e16aa17967d7bb9194f24be52d26f2f675af`; fuente `71cf68f2af44352f276a58345a6c8285aeace64b286b162e88a3688803ee6cf3`. Figura guardada con stream binario para que Git no aplique conversión de finales de línea; `git diff --check` externo conforme. Página 8 final re-renderizada y revisada; geometría sin cambios. Hashes y límites en el informe de revisión.

## T-12 y T-14: brechas mapeadas y columna EDT añadida — 11 de octubre de 2026

El usuario autorizó cerrar las 25 brechas del mapeo y añadir una columna «Paquete EDT (T-14)» al T-12, manteniendo aparte «Sección de la propuesta». Se preservan los 222 códigos y nombres; se ampliaron sólo entregable y criterio de aceptación de 3.3.1, 3.3.5, 3.6.4, 3.7.2, 5.1.2 y 5.1.3. Las 645 filas del T-12 quedaron mapeadas: 415 directas, 193 indirectas y 37 «No aplica». Las 25 brechas iniciales se asignaron a los paquetes existentes; las ocho estaciones se incluyeron en compra y recepción (5.1.2 y 5.1.3). El T-15, sus horas, la Gantt, los diagramas, las fechas y la estructura de la sección 1 no se modificaron. Detalle en `Revision/mapeo_T12_paquetes_EDT_T14.md`. Sin commit ni push.

## SD3: sincronización MD–LaTeX y Obs. 4 — 11 de octubre de 2026

**Autorización:** sincronizar el SD3 Markdown con el checkout LaTeX correspondiente, incorporar la columna «Paquete EDT (T-14)» aprobada por el usuario, revisar completos los PDF de anexos y T-12 para la Obs. 4, corregir únicamente tablas que fallen y recompilar. La petición deja las observaciones 2 y 3 para el final. Destinos: Markdown aquí en `rama-md`; fuentes y PDF en `../LafroX-sd3-latex`, rama `LafroX-Subdoc3-LateX`. Se preservaron cambios locales preexistentes. Sin commit ni push.

**Hecho:** se mantuvieron los 222 códigos y nombres de paquetes del T-14; la sexta columna del T-12 contiene 645 asignaciones (415 directas, 193 indirectas y 37 «No aplica»). La prosa de §3.2.3 y Anexo 3.A describe el mismo formato en MD y LaTeX. El T-12 LaTeX/PDF incluye la columna; el PDF tiene 261 páginas. Para la Obs. 4 se revisaron visualmente las 168 páginas de anexos y las 261 del T-12, incluidas las continuaciones de tablas. Se ajustó el ancho de ID en las Tablas 3.A.6, 3.A.9 y 3.A.10, y el encabezado «ID requerimiento» del T-12 se simplificó a «ID» en MD/LaTeX para evitar su corte tipográfico; no se alteraron filas ni valores.

**Verificación:** los tres PDF son carta y tienen texto seleccionable: cuerpo 34 p., anexos 168 p., T-12 261 p. Tres compilaciones anteriores terminaron con salida 0; tras los últimos ajustes se recompilaron anexos con salida 0. Logs finales sin overfull/underfull ni referencias indefinidas. Se confirmó a vista completa que las cabeceras de continuación se repiten, no hay cortes de filas ni texto fuera de celda y la legibilidad se conserva; muestras de tablas densas se revisaron a mayor resolución. Las tablas de anexos/formularios se verificaron contra el mínimo de 9 pt del Art. 40.4; §5 de las Aclaraciones se aplicó a las tablas del cuerpo, no a anexos/formularios. La escala monoespaciada del T-12 en `lafrox.cls` quedó en 0,96 (9,12 pt nominal sobre base 9,5 pt).

**Pendiente:** 28 celdas de revisión humana; redibujar Figura 3.4 (3,6–4,6 pt; mínimo 9 pt); homologar nombres M10/M11 con SD4; decisiones de prioridad, automatización/SRE y atributos de calidad (filas 17, 20 y 28); firma efectiva de portada. `Revision/trazabilidad_Informe1_Informe2_SD3.md` actualizado: 36 documentadas/mantenidas, 6 parciales (2, 7, 17, 20, 28, 42) y 1 bloqueante (3). Se mantienen la columna T-12 de seis campos solicitada por el usuario y el riesgo de apartarse del formulario base de cinco campos. Sin commit ni push.

## Revisión integral SD1 LaTeX–MD–Aclaraciones — 11 de octubre de 2026

Petición: comprobar exhaustivamente alineación de cuerpo, anexos y T-6 y cumplimiento de Aclaraciones. Auditoría de sólo lectura sobre entregables; no se autorizan correcciones por esta petición de revisión. Resultado: reconversión en memoria de tres fuentes coincide exactamente con tres MD; 120 bloques de prosa del cuerpo, 6 de anexos, 5 del formulario y 44 celdas T-6 cotejados con PDF. Revisadas 31 páginas (21+3+7), índices, figura real, siete tablas cuerpo y declaraciones. No equivale a conformidad 100%.

Hallazgos adicionales: citas a Bases carecen de páginas exigidas por §6; folios T-6 pp.4–6 girados en margen izquierdo, no abajo-derecha (§9); nomenclatura CMMI v2.0/SCAMPI A y renovación requieren homologación (fuente primaria https://cmmiinstitute.com/learning/appraisals/types). Persisten diez celdas de revisión humana (8+1+1, scopes parcialmente repetidos) y tres firmas. Este resultado reemplaza la afirmación anterior de que sólo faltaban revisión humana/firmas. PDF originales BA/BTT/Caso localizados en FEP, sin asignar páginas aún. No autenticar certificados ficticios ni confundir puntos TeX/PDF con infracciones de tamaño.

Registro detallado: Revision/verificacion_integral_SD1_LaTeX_MD_Aclaraciones.md; añadido resultado posterior a trazabilidad sin alterar sus 28 filas. Fuentes, espejos entregables y PDF no modificados durante esta auditoría; sin commit/push nuevo. T-15 PDF sigue excluido por instrucción expresa. Cambios concurrentes preservados. Memoria agent-attributed suspendida por identidad runtime no disponible; estado guardado localmente. Siguiente: si se autorizan correcciones, completar citas con PDF fuente, corregir folios horizontales y homologar CMMI antes de revisión humana/firma/publicación.


## S1-18 ejecutado y coordinación SD1–SD4–T-15 — 11 de octubre de 2026

**Objetivo/autorización:** usuario aprobó incorporar propuesta de capacidad instalada en SD1 LaTeX y MD, sincronizar y revisar coherencia. Durante revisión indicó expresamente no cambiar PDF T-15, sólo su MD y ningún título de paquete. Esa excepción elimina necesidad de localizar/editar/compilar T15LaTeX para esta tarea. Sin autorización nueva de commit/push.

**Realizado SD1:** contenido.tex del checkout LafroX-sd1-latex (rama LafroX-Subdoc1-LateX verificada) incorpora §1.1 inventario ficticio aprobado112=92equipos paraespecialidades (80Santiago+12Valparaíso)+8puestosNOC+8mesa+4repuestos (2porsede). No incluye comprasT11paraCLIENTE. Ocho puestos físicosmesa no equivalen a8agentes por turno. Mesa reservadaPuelche 2.283contactos/mes base inicial (meses21–24contrato) y2.391desde25, 7/2 y7/3puestos simultáneos. Demanda inicial2000; plantilla7y9personas, más2peaksept/dic conformeSD4. DotaciónMesa adicional a124especialistas, no descontada de32NOC niSOC; contactos no son usuarios/tickets distintos. Capacidad dimensionada con supuestos, no capacidadcorporativatotal ni mediciónreal. ErlangC dimensiona espera80%20s; abandono≤5% yFCR≥70% siguenmedición. Recalibración ajusta base, no la sustituye. Referencias internas2026aSD4/2026bSD6/2026cSD7, títulooficialT15Nivelaciónderecursos; fuentes yIAactualizadas, firmas/revisiones reales preservadas pendientes.

**Coherencia:** cotejoSD3§3.4.5, SD4cuerpo yAnexo4-W.7, T15§4.2/5.6/5.7. Se corrigió única frase T15MD que asignaba mesa alNOC; mesaadditional,44especialistas noincluyen mesa, familiaSREagrupaHH no personalidéntico. Dos frases T15 que atribuían tresSLA aErlangC se precisaron aobjetivoespera ymedicióndelosotros. ReferenciaSD1Tabla1.1→1.3porrenumeración. Títulos y todas lasfilas de paquetes/HH delT15 exactosfrenteHEAD; sólofilaSREdedisponibilidad cambia. Fuente/PDFT15 no tocados por petición explícita. ModeloSD4original ysupuestosnuméricos noalterados:SL2283/2agentes80,003%;2391/3agentes95,256%;2391/7peak80,019%. Cota6000contactos dela tabla de crecimientoSD4 no se usócomocapacidadinstalada.

**Verificación y sincronización:** trespasadasLuaLaTeX con--no-shell-escape salida0; cuerpo21páginas,7tablas (inventario/capacidadp7,dotaciónp11,NOCp12,experienciap16,rolesp18,IAp21). Todaslas21páginas inspeccionadas; sinOverfull/Floattoolarge/refindefinidas, índicescorrectos, encabezadoslegibles, análisisposterior. Anexos3p yT6 7punchanged;11campos ypendientes humanos intactos. TresMDreconvertidos desde fuentes actuales, tablasuniformes7/1/2 ylinks/figurascomprobados, sin comandosTeXniCaso02. S1-18/fila24 incorporada en trazabilidad preservando nueva numeración1–28delusuario; pendientesconcretos revisiónhumana/firmas. DifffchecksMDyLaTeXconformes.

**Archivos:** externo contenido.tex yPDF/auxiliares/vistas; fuenteSHA31741d4fa65ee275fe8afb5d44e554509217ccac8fe509174590f06aa8c34ec3;PDFSHAdce24e00a540abf383a394e4c0357adc67f591f3d94f35d964364c9047c4abae. MD01_presentacion_empresa/LAFROX-Subdocumento1.md (anexos/T6sin diffs),07_PlanDeTrabajo_EDT_Cronograma_Implantación/LAFROX-Formulario-T-15.md,Revision/trazabilidad_Informe1_Informe2_SD1_LaTeX.md,contexto. NoediciónSD4/SD3/Base/T14; cambiosconcurrentesSD2yotrosregistros intactos. No commit/pushnuevo. Siguiente:revisiónhumana, firmas ypublicaciónsiusuarioordena. No seafirma coherenciaglobalde todosloscapítulos nimétricasmedidas; verificación centradaencapacidad/roles/horariosrelacionados. Memoriaagent-attributed suspendidapor identidadruntimeausente; resumenlocalpersistido.


## T-12: RT-05.30 y RT-18.08 alineados con SD13 — 11 de octubre de 2026

Por petición del usuario se aplicaron cuatro cambios al T-12: descripciones de RT-05.30 y RT-18.08 separan el cumplimiento (modelo cinético determinista, SD13 13.3.2) del agregado INN-03 y aclaran recalibración frente a reentrenamiento; referencias cambiadas a «SD13, sección 13.3.2, descripción del modelo cinético», «SD13, sección 13.3.6, indicadores de verificación», «T-19, Ficha 3» y «T-14, cuenta 8.3». Se retiraron las citas a Tabla 13.13 (hoy paquetes EDT de INN-03) y 13.16 (hoy riesgos; indicadores son 13.15). Verificado contra SD13 13.3.2/13.3.6, T-19 Ficha 3, T-14 cuenta 8.3 y SD5 5.1.7/5.1.11/5.2.6. Resumen T-12 ajustado. Pendiente: SD13 no usa la palabra «deriva»; el umbral es la recalibración extraordinaria si I-03B < 80 % en dos cortes seguidos, y la línea base de I-03B es «sin medición». Sin commit. Decisión posterior del usuario: la descripción de RT-18.08 vuelve a su texto original («Modelo cinético determinista de INN-03…»), con las referencias corregidas; el resto del capítulo 18 se mantiene coherente con D-09 (sin IA): RT-18.01–18.07 y 18.09 Cumple, 18.10 No cumple. No se modificaron la D-09, el SD13 ni el T-14; el corte de I-03B sigue sin definir.

## Commit y push de ambas ramas SD1 — 11 de octubre de 2026

Petición explícita «comitea y pushea ambas ramas» cumplida. LaTeX: **145fedec927a09fc649e070e33f5f3c29ce66aa8**, rama LafroX-Subdoc1-LateX, dos archivos (contenido.tex y PDF). Markdown: **05f1d66708cbb1f524e1bbb294eeec2786fcec88**, rama rama-md, tres entregables SD1 más registro de trazabilidad y contexto. Ambos pushes a https://github.com/PatricioH315/LafroX.git con salida0; HEAD y ls-remote coinciden en las dos ramas. Staging MD comprobado sólo cinco archivos autorizados .md; diff-check conforme. No se incluyeron los dos cambios SD2 pendientes ni imágenes de revisión. S1-18 sigue sólo propuesta; revisión humana y firmas siguen pendientes. Este recibo posterior al push permanece local y no requiere otro commit; contenido solicitado ya publicado. Memoria agent-attributed suspendida por identidad runtime ausente.


## S1-10 implementado y tres entregables SD1 alineados — 11 de octubre de 2026

**Autorización:** usuario aprobó rangos ficticios de antigüedad y esquema NOC, pidió ejecución en el mismo LaTeX, revisión exhaustiva y alineación con rama-md. S1-18 sólo propuesta, sin implementarlo. Principal rama-md y externo LafroX-Subdoc1-LateX comprobados. No autoriza nuevo commit/push.

**Implementado:** tabla dotación cinco columnas: 48 desarrollo1–8años;15arquitectura3–10;32NOC1–7;12SRE2–8;10QA2–9;7seguridad2–8. Son antecedentes ficticios autorizados del ejercicio, no datos reales ni revisión humana. NOC cuatro equipos7+4reemplazos=32; seis puestos activos (responsable+5operadores), séptimo de equipo releva. Tres franjas00–08/08–16/16–24 y rotación/descansos por cuadrante, reglas relevo/reemplazos/escalamiento, ajuste horario Chile, NOC separado de mesa/SOC y no exclusivo32paraPuelche. Cálculo conservador40h:1280brutas−1008cobertura=272margen para formación, pausas y ausencias; no demuestra por sí solo un cuadrante nominal legal ni capacidad adicional vendible. Consulta DT confirma reducción42en2026/40en2028 (https://dt.gob.cl/portal/1626/w3-article-129225.html), modelo40no depende de42; no se agregó consejo legal ni se afirma aprobación laboral.

**Coherencia y espejo:** se detectó política QA previa sólo en MD:70%negocio+80%global. Preservada trasladándola primero a contenido.tex. Refs/IA agregadas al índice PDF cuerpo. SD1MD y T6MD sincronizados completamente; creado MD de anexos antes ausente. Figura real enlazada desde checkout LaTeX; cero descripciones sustitutorias. Se conserva portada/nomenclatura y títulos obligatorios; índices MD navegables sin folios ficticios. Sólo .md escritos en rama-md. Fuentes/PDF/vistas sólo externos con permisos aprobados. No se cambiaron Bases ni SD2/SD3/SD4/SD9; cambios concurrentes preservados.

**Verificación:** tres pasadas LuaLaTeX cuerpo salida0,19p; anexos3p y T6 7p conservados.29p inspeccionadas visualmente, cinco tablas cuerpo/tres fuera, cero cajas desbordadas/ref indefinidas/Caso02, encabezados completos tras ampliar Personas. Fuente T6/campos intactos; Markdown conserva11campos,6rangos,5+1+2tablas y8+1+1marcadoreshumanos. Links internos y figura comprobados; aritmética124/32/24h/1280/1008/272 y70/80 verificada; diff-check conforme. Registro trazabilidad28filas actualizado, S1-10 incorporado sujeto a revisión del integrante; S1-18 pendiente, firmas y revisión real pendientes.

**Propuesta S1-18 a presentar:** inventario ficticio aún no aprobado:92equipos para Ingeniería/QA/Seguridad/SRE (48+15+10+7+12),8puestos compartidosNOC (6activos+2relevo),8puestosmesa (7hora cargada+1reserva),4equiposrepuesto;total112. No son equipos actuales comprobados ni compras para CLIENTE; requerir aprobación antes de añadirlos a la oferta.  separar inventario corporativo (tipo/cantidad/sede/uso, sin copiar equipos futuros del CLIENTE) y capacidad de mesa. Reusar cálculo vigente tabla de volumetría del SD4 y Anexo4-W.7 y T15:demanda2000contactos/mes,capacidad2283 inicial y2391desde25; son contactos y capacidad del proyecto, no usuarios ni capacidad total corporativa. La dotación global de mesa no figura entre124; cualquier propuesta de personal adicional requiere definir/aprobar su relación con ese conteo. No transformar horas/productividad en prueba de SLA80%/20s ni intercambiar contactos por tickets sin definición.

**Archivos:** externo contenido.tex y PDF/auxiliares; Markdown01_presentacion_empresa/LAFROX-Subdocumento1.md, LAFROX-Subdocumento1-Anexos.md, LAFROX-Formulario-T-6.md; Revision/trazabilidad_Informe1_Informe2_SD1_LaTeX.md; este contexto. Siguiente:definir y autorizar inventario/capacidadcorporativaS1-18 y revisiónhumana. Identidad runtime memoria no confirmada: no escrituras agent-attributed; resumen local preservado.

## Estado vigente — 11 de octubre de 2026: correcciones de revisión SD9

Se corrigieron sólo los cuatro Markdown de SD9 v_nueva: 42 textos de caída, referencia al calendario efectivo T-17 4.1, subtotal de conformidad y modelo paramétrico de no conformidad (93,8 HH por evento interno y 109,8 externo; no pronóstico ni reserva), secuencia PRE-C con restitución y capacidad neta pendiente de confirmación. LaTeX y diagramas actualizados en el repositorio independiente Subdoc/LafroX/SD9_v_nueva, cuatro PDF recompilados. Se conservaron las siete marcas de revisión humana y las firmas pendientes. Bases disponibles sólo en Markdown: lista de 220 pasajes para agregar páginas manualmente en Subdoc/Revision/citas_Bases_SD9_paginas_pendientes.md. No se recuperaron cifras desactualizadas de SD8. Informe de cierre en Subdoc/Revision/correcciones_SD9_2026-10-11.md. No se modificaron los cambios ajenos de SD13 ni se hizo commit.

## Estado vigente — 11 de octubre de 2026: consolidación del SD13 y revisión de la Comisión

Por instrucción del usuario, sólo se editaron los tres archivos de `13_innovaciones/` (cuerpo, anexos y T-19); ningún subdocumento anterior se modificó. Verificado: INN-01 a INN-05 tienen nombre, código, paquetes, meses y riesgos idénticos en T-12, SD5, SD7/7.D, T-14, SD8/8.A/8.F, T-16, SD9 y T-13. Cambios: introducción sin atribuir innovaciones al SD3/SD4 (solo componentes que reutilizan); Figura 13.1 dibujada en Mermaid (antes era descripción textual, indicio §7.1 a); nombres alineados al SD4 (C-01 App de preventa, C-02 App de reparto, C-03 Terminales de bodega, N-10 Plataforma analítica, capa 2 borde); «Investigación adicional declarada» en 13.N.3 y en el campo 5 del T-19; Tabla 13.B.2 de alcance refinado; RT-03.13 retirado de la bitácora; F-14 «Analítica de Costo de Servir»; herramientas citadas a Capítulo 6 y T-10; INN-03.P5 de los meses 32, 44 y 56 (septiembre con inicio feb-2027) activa parámetros después del día 25; índice enlazado en los tres archivos. Revisión en `Revision/revision_comision_informe2_SD13.md`: 0 mientras existan 13 celdas `[[REVISIÓN HUMANA]]`; 60 con ellas completas. Pendientes: revisión humana, imagen de la Figura 13.1 para el PDF, diagramas por innovación. Sin commit.

## Estado vigente — 11 de octubre de 2026: publicación y espejo del Subdocumento 4

El usuario autorizó commit y push y exigió igualdad de contenido entre Markdown y LaTeX. Se actualizó `rama-md` de `cf43057` a `d8bc438` por avance rápido, preservando los cambios locales SD4 en el stash `respaldo SD4 antes de sincronizar y publicar 2026-10-11` y reaplicándolos sin conflictos. La cámara premium del MC9400 agregada por el remoto se conserva. Destinos: únicamente Markdown en este checkout; fuentes y PDF en `../LafroX-rama-latex`, rama comprobada `subdoc-4` desde `292c6e8`.

Se trasladaron a LaTeX las especificaciones vigentes del MD que faltaban: recepción, inventario, control comercial, rutas, cobranza, devolución, EDI y telemetría; ASN al cargar separado del acuse tras descarga; AES-256/KMS, instancias de Preproducción por campaña y herramientas de pruebas. Se trasladaron al MD el diagrama de red corregido por el usuario y la figura de emplazamiento ya existente en LaTeX, sin alterar sus diseños. Ambos cuerpos contienen 27 figuras; referencias renumeradas y figuras enlazadas a los activos reales del checkout LaTeX. Resúmenes SD4 actualizados, sin tocar entregables de otros subdocumentos.

El cotejo de texto normalizado compara cuerpo, anexos y T-11: 1.579, 948 y 110 bloques respectivamente, sin diferencias de contenido. Se distinguen navegación, maquetación y artefactos conocidos del conversor; las 27 figuras se verifican por título, ancla y activo aparte, y 342 enlaces internos son válidos. LaTeX publicado y verificado en origin en `c4d1230`; los enlaces Markdown apuntan a ese commit. PDF compilados: 191/91/46 páginas, sin referencias indefinidas ni desbordamientos. Este estado y el registro `Revision/ALINEACION_MD_LATEX_SD4_2026-10-11.md` integran la unidad Markdown de sincronización autorizada para publicación; verificar su hash y remoto con Git al reanudar.

La figura de red conserva rótulos impresos próximos a 5 puntos al ajustarse a carta: sigue pendiente su legibilidad, sin modificar el XML aprobado. Cinco referencias del T-12 necesitan renumeración (recinto: 25 → 27; racks: 24 → 26), sin editar SD3 por alcance. Ensayos, autorización del mandante y revisión humana mantienen su estado; sincronización no equivale a conformidad total.

## Descubrimiento — remisión IA mal numerada en Aclaraciones, 11 de octubre de 2026

Consulta del usuario sobre «sección 9.1» en declaración IA. Cotejo de ambas copias de Aclaraciones (aportada y Bases del repositorio): regla de prohibición, indicios y sanciones está en §7.1; §9 se titula Recordatorios formales y no tiene §9.1. Art.9.1 BA versa sobre moneda de oferta, no IA. La remisión 9.1 es inconsistente; interpretación por contenido apunta a §7.1, no afirmar origen histórico sin fuente. BA13.5 y A-6 sustentan declaración/revisión/responsabilidad. No se corrigieron Bases ni entregables. Declarar Alto no acredita elaboración o revisión humana ni evita sanciones por los indicios de §7.1; no equivale por sí solo a rechazo automático. Memoria agent-attributed suspendida por identidad runtime ausente; hallazgo preservado localmente.


## Publicación final de ajustes SD1 — 11 de octubre de 2026

Por petición explícita «comitea y pushea», se creó y publicó **f1ef0f0858c3c6a47b91cad1e1c1d3f6123d03ad** en https://github.com/PatricioH315/LafroX.git, rama LafroX-Subdoc1-LateX. HEAD y ls-remote coinciden; commit y push salida 0. Incluye exactamente ocho archivos: contenido.tex, anexos.tex, las raíces SD1/SD1-Anexos/T-6 y sus tres PDF. Diff-check conforme; no se incluyeron imágenes de revisión, otros subdocumentos ni cambios de rama-md. Publicados reemplazo «Caso 02» por «caso», revisión de anexos y presentación del formulario T-6. Las declaraciones de revisión humana y firmas siguen pendientes; no se declara entrega aprobada. Los cambios SD3/T-12 de denominación no forman parte de esta publicación. Objetivo commit/push SD1 completado; registro Markdown permanece local. Memoria agent-attributed suspendida por identidad runtime ausente.


## Revisión autorizada de anexos y T-6 del SD1 — 11 de octubre de 2026

**Objetivo e instrucciones:** usuario confirmó revisar anexos y formulario conforme a Aclaraciones; límites de una página/cinco columnas sólo para cuerpo, no aplicados a estos documentos. T-6 debe conservar detalle de formulario, análisis en cuerpo. Denominación «caso» sin número académico mantenida.

**Realizado:** en checkout externo SD1, rama LafroX-Subdoc1-LateX comprobada, se reformuló anexos.tex sin inventar anexos ausentes ni trasladar cartas del Sobre 1. Referencias coherentes Distribuidora Puelche 2026a/d; IA antes ausente agregada. Se retiraron índices vacíos de tablas/figuras del anexo, manteniendo índice detallado. T-6 mantiene portada, índice y lista de tablas; eliminado índice vacío de figuras. Introducción breve integrada en la primera hoja horizontal de campos, no como capítulo explicativo separado; Referencias y declaración IA final, ambas en índice. Once campos de los tres proyectos preservados exactamente mediante comparación de bloque antes/después; se mantienen orientación horizontal, tres hojas de tabla, encabezados repetidos y filas completas. No cambian montos históricos, contactos, SLA ni otras cifras.

**Coordinación y verificación:** declaración del cuerpo incluye ahora fila de anexos y T-6 revisado, herramientas declaradas y [[REVISIÓN HUMANA]] reales pendientes, sin reutilizar aprobación antigua del formulario. Tres pasadas LuaLaTeX por archivo con salida 0: cuerpo18, anexos3, T-6 7páginas. Inspección visual de todas las páginas de anexos y T-6 y tabla IA del cuerpo; sin desbordes ni referencias indefinidas; cero «Caso 02» en los tres PDF. Encabezados experiencia repetidos p4/5/6; campos íntegros, sin reducirlos para forzar una página. Diff-check externo conforme. Vistas quedan fuera de rama-md.

**Archivos:** externos anexos.tex, LAFROX-Subdocumento1-Anexos.tex, LAFROX-Formulario-T-6.tex, contenido.tex (sólo coordinación IA), PDF/auxiliares. Markdown: registro de trazabilidad SD1 LaTeX y contexto. SD3/T-12, clase común, Bases y otros cambios previos intactos. No se creó nuevo commit/push. Cuerpo y formularios Markdown aún no sincronizados con la versión LaTeX.

**Pendientes:** revisión humana de seis secciones más anexos/T-6, firmas de las portadas y datos corporativos S1-10/S1-18. No se acredita envío ni conformidad global. Memoria agent-attributed suspendida por identidad runtime ausente; resumen local preservado. Siguiente: autorización de publicación si se solicita o sincronización MD explícita, preservando cambios concurrentes.


## Ampliación explícita — denominación del caso en anexos y T-12, 11 de octubre de 2026

El usuario amplió el reemplazo de «Caso 02» por «caso» a anexos y T-12. Se identificó correctamente T-12 como SD3 (T-6 es SD1). Checkout externo `C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX-sd3-latex`, rama comprobada `LafroX-Subdoc3-LateX`. Cambios acotados a anexos.tex (3 menciones), T-12 (34), tablas activas criterios_aceptacion (1), glosario (1), supuestos (16) y vacios (3), más metadato de portada en ambas raíces. Se revisaron 23 fuentes activas; sin cambios de códigos, requisitos, cifras o cuerpo SD3. La clase común y Bases permanecen intactas. PDF SD3/cambios de compilación previos preservados. No extender este reemplazo al cuerpo SD3 sin petición posterior.

Verificado por extracción integral: SD1 18 páginas, anexos SD1 5 y T-6 9, cero menciones «Caso 02» incluyendo portadas, leyendas y referencia. Anexos SD3 y T-12 recompilados con tres pasadas LuaLaTeX, salida 0: 169 y 222 páginas respectivamente. Extracción textual integral verifica cero menciones «Caso 02» en ambos PDF. Estos cambios son locales, no incluidos en commit/push 914b2ca anterior. Cuerpos Markdown no sincronizados. Sin publicación nueva ni edición funcional del formulario. Preferencia del usuario: referirse al caso sin su número académico también en referencias y formularios.


## Estado SD1 — 11 de octubre de 2026: denominación natural del caso

Petición explícita: reemplazar «Caso 02» por «caso», incluida la referencia, para evitar lenguaje académico frente al cliente. En checkout LaTeX SD1 se corrigieron cuatro menciones de contenido.tex: introducción, presentación de experiencia, leyenda Tabla 1.2 y referencia 2026c («Caso: Logística — Especificaciones del Problema y Operación de Distribuidora Puelche S.A.»). En las tres raíces (cuerpo, anexos y T-6) se sobreescribió sólo el metadato de portada a «Caso — Logística», sin cambiar clase compartida, campos del T-6 ni contenido del anexo. Bases originales y títulos de archivos permanecen intactos. Cifras, fuentes y marcadores humanos preservados. Compilación de tres PDF terminada con salida 0 y comprobación integral de ausencia de «Caso 02» conforme; sin nuevo commit/push solicitado.

Corrección del registro previo: push del commit 914b2caa90714ee6ba9ae866f51b477509fffd36 sí se completó tras autorización específica del usuario; ls-remote y HEAD coincidieron. Esa publicación precede al cambio de denominación actual. Estado anterior «push pendiente» supersedido. Memoria agent-attributed suspendida por identidad runtime no confirmada.


## Publicación SD1 — 11 de octubre de 2026

El usuario pidió commit y push, y preguntó si se editaron anexos y formulario. Commit local **914b2ca** creado en `LafroX-Subdoc1-LateX`: sólo contenido.tex, LAFROX-Subdocumento1.tex y LAFROX-Subdocumento1.pdf. Diff-check corregido y conforme. No se incluyeron vistas PNG, T-6 recompilado ni cambios de rama-md/otros subdocumentos. Push no ejecutado: auto-review bloqueó transmisión al GitHub por exigir autorización específica del destino y payload. Se solicitó confirmar `https://github.com/PatricioH315/LafroX.git`, rama `LafroX-Subdoc1-LateX`, para esos tres archivos.

Comprobación adicional: anexos.tex sólo declara ausencia de anexos complementarios y remite al T-6; no fue editado. T-6 conserva portada, preliminares, breve introducción, once campos para tres proyectos y declaración IA; tampoco fue editado. No afirmar que se humanizaron los anexos/formulario. El usuario plantea preferencia por formulario sin desarrollo de capítulo: mantener detalle en campos, análisis en cuerpo; cambios al formato aún no aplicados. Pendiente aprobación del remoto y eventual petición de simplificar T-6/anexos. Identidad de memoria sigue no confirmada; no efectuar escrituras agent-attributed.


## Estado vigente — 11 de octubre de 2026: redacción y diagramación completas del SD1 LaTeX

**Petición y alcance:** el usuario amplió la revisión del organigrama a todo el SD1: redacción natural, punteos útiles y análisis después de cada tabla, conforme al archivo aportado `C:/Users/alexa/Desktop/Universidad/FEP/aclaraciones-licitacion.md`. Autorización de edición y recompilación registrada en AGENTS.md. Rama principal comprobada `rama-md`; fuentes y derivados se editaron sólo en `C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX-sd1-latex` (rama previamente comprobada `LafroX-Subdoc1-LateX`), mediante permisos externos aprobados.

**Accomplished:** se reescribieron las seis secciones sin cambiar títulos obligatorios. Se retiró «Descripción de imagen» y se explicó la figura real mediante responsabilidades y reporte del CISO; listas y párrafos simplificados, sin promesas de riesgo cero ni beneficios de alianzas garantizados. Se agregó análisis de dotación (63+44+10+7=124), experiencia y diferencias entre SLA de servicio e infraestructura, y concentración de diez roles en ocho personas. Tabla 1.3 resumida a tres columnas verticales; cuatro tablas con cita previa y análisis posterior. Se corrigió desborde de IA y salto que dejaba casi vacía la antigua p19. Posición fija de figura/tablas evita que interrumpan listas o adelanten las conclusiones; paquete float sólo en raíz SD1, sin cambiar clase ni T-6. Tres pasadas LuaLaTeX por ajuste con --no-shell-escape; PDF final de 18 páginas, inspección visual integral, sin cajas desbordadas ni referencias indefinidas. Tablas 1.1/1.2/1.3/1.4 en p9/13/15/18; figura y explicación p8. Aviso de MiKTeX sobre comprobación de actualizaciones no afecta salida 0.

**Revisión humana y límites:** declaración de IA conserva seis columnas exigidas, siete filas (seis secciones y T-6), tipografía 9,5pt. Se incorporó OpenAI Codex y se dejaron seis [[REVISIÓN HUMANA]] porque las aprobaciones del texto anterior no validan lo reescrito. T-6 no editado: nueve páginas y revisión anterior preservada. No se fabricaron antigüedad, turnos NOC, inventario/capacidad corporativa, firmas ni revisores. Pendientes S1-10, S1-18 y firmas G1-02/G1-05. No se acredita conformidad final ni autenticación externa de antecedentes. Cuerpo Markdown aún no sincronizado con esta edición; la tabla de trazabilidad actual sí refiere al PDF corregido.

**Archivos relevantes:** checkout externo: contenido.tex y LAFROX-Subdocumento1.tex (float), PDF/auxiliares y vistas; rama-md: AGENTS.md, Revision/trazabilidad_Informe1_Informe2_SD1_LaTeX.md y este contexto. Registro actualizado con 28 filas y páginas nuevas. Sin commit, push ni cambio de rama. Preservar cambios concurrentes SD2/SD3/SD9 y demás historial. Memoria agent-attributed suspendida por falta de identidad runtime confirmada; este resumen local conserva el estado, sin sustituir atribución Engram.

**Next Steps:** revisión del integrante, datos corporativos faltantes y firma. Si se solicita espejo MD, trasladar esta versión sin sobrescribir ajustes de coherencia independientes del cuerpo Markdown.


## Estado vigente — 11 de octubre de 2026: revisión completa y redacción directa de la trazabilidad SD1

El usuario exigió revisar todas las respuestas del registro SD1 y eliminar etiquetas repetitivas como «Documentado». Se reescribieron las28 filas de `Revision/trazabilidad_Informe1_Informe2_SD1_LaTeX.md` con corrección concreta y página, sin prefijos de estado ni cautelas genéricas por fila. Se inspeccionaron las30 páginas (21SD1+9T6) mediante vistas completas y extracción textual. Sólo faltas concretas permanecen: promesas absolutas; antigüedad/turnosNOC; equipamiento/capacidadmesa; Tabla1.4 invade pie y p19 casi vacía; firma y revisión humana pendiente.

Correcciones de errores del asistente: T-7 es válido por BA FormularioT7 y Aclaraciones§11 (estructura de propuesta); T-6 es el formulario complementario de experiencia. Montos históricos son campo obligatorio del T6, no precios ofertados. El evaluador solicita proyectos ficticios/verosímiles: no exigir existencia real en cada respuesta. Se retiró ficha adicional de métricas no exigida. También se corrigió falsa alerta T7 en registro inicial Markdown y se enlazó la tabla LaTeX vigente. Las menciones históricas de T7 «incorrecto» más abajo quedan supersedidas por este cotejo de Bases.

No se editaron fuentes LaTeX, firma o revisores ni se aplicaron arreglos a losPDF; sólo registro y contexto Markdown, más vistas externas autorizadas. Sin commit/push. Preferencia estable: responder qué cambió/dónde y mencionar pendiente sólo cuando falta algo específico. Engram no disponible; resumen y preferencia guardados localmente. Siguiente: equipo decide reparaciones/revisiones humanas; la tabla no debe volver a usar «Documentado» en todas las filas.

## Preferencia de redacción — trazabilidad SD1

El usuario considera artificial y confusa la respuesta «Documentado; entrega pendiente de comprobar» sobre el T-6. Prefiere respuestas directas que describan la corrección visible, sin cautelas genéricas sobre el envío. Se simplificó S1-01 del registro basado en LaTeX: T-6 incorporado como PDF separado, tres proyectos y once campos, con páginas verificadas 5–8. El PDF de nueve páginas fue compilado en la sesión; no confundir acreditaciones pendientes con ausencia del formulario. Engram no disponible; preferencia registrada aquí.

## Estado vigente — 11 de octubre de 2026: fuentes del SD2 actualizadas con GS1 Chile y literatura reciente

A pedido del usuario (usar gs1chile.org/Biblioteca y evitar fuentes de los 2000), se reemplazaron en MD y LaTeX: Scheier (2003) → GS1 Chile (s. f.-a «Comparte», s. f.-c «Servicios/Comercionet») + Moberg y Drummond (2005, RFC 4130 AS2); Jedermann et al. (2014) → Mercier et al. (2017); Rogers y Tibben-Lembke (2001) → Agrawal et al. (2015); se sumó Vidal et al. (2020) al ruteo. La viñeta GS1/EDI de §2.2.2 cita GS1 Chile (s. f.-a, s. f.-b «Identifica») y usa SSCC en vez de GS1-128; se eliminó la referencia no verificable GS1 Chile (2020). Se mantienen de Koster et al. (2007), Guerreiro et al. (2008), Toth y Vigo (2014) y Chopra y Meindl (2016) por ser obras de referencia sin reemplazo verificado. Las revistas PDF de la biblioteca de GS1 Chile (p. ej., n.º 40, enero 2025, trazabilidad) no se leyeron: superan el límite de lectura web y descargarlas requiere autorización.
- Compilado: 29 páginas, sin errores ni cajas desbordadas; 21 referencias, todas citadas.
- Pendiente de verificar por el equipo: SII (2024) «Manual de Procedimientos…» y Código del Trabajo (2002) «Edición oficial», heredadas.

Sin commit ni push.

## Estado anterior — 11 de octubre de 2026: §2.2.4 del SD2 con investigación externa y corte de las 14:00 según B.1

A pedido del usuario (las materias del 16.2 deben apoyarse en investigación, no solo en el caso), se reescribió §2.2.4 en MD y LaTeX: cada materia resume una fuente externa verificada en la web y la contrasta con el caso. Fuentes nuevas en Referencias (APA): GS1 (2016) EANCOM 2002 S4; Scheier (2003) Computerworld; Ministerio de Salud (1996) arts. 71 y 192 (−18 °C, tolerancia breve hasta −12 °C); Jedermann et al. (2014); Chopra y Meindl (2016); Guerreiro et al. (2008); Toth y Vigo (2014); de Koster et al. (2007); Fildes et al. (2022); Rogers y Tibben-Lembke (2001); Boulaksil y Belkora (2017). Se omitieron DOI no verificados (Rogers 2001, Toth y Vigo 2014).
- Corte de las 14:00: justificado ahora con el perfil del día hábil del caso (sección B.1, p. 38), igual que SD4 (planificación 15:00–18:30, preparación 22:00–06:00, despacho 05:30–07:00). Sin cambios en SD3/SD4.
- Se quitó el monto «$45.000» del almacén de Empedrado para no arriesgar la regla de precios.
- Matriz Tabla 2.2 revisada contra Aclaraciones §3 y §5: título con texto, cita previa, fuente, 3 columnas, celdas de una frase, análisis posterior.
- Compilado: cuerpo 29 páginas, sin errores ni cajas desbordadas; Referencias pp. 27–28; Tabla 2.4 pp. 28–29. Trazabilidad SD2 actualizada (filas 7, 9, 15, 20, 27 y 30).
- Observación: la referencia previa «GS1 Chile (2020) … (Versión 20.0)» no se pudo verificar; revisar si existe.

Sin commit ni push.

## Estado anterior — 11 de octubre de 2026: S2-11, S2-16, S2-18 y portada del SD2 aplicados

Por petición explícita del usuario («actúa en lo que tengas que actuar», sin pasar a llevar otros subdocumentos) se editaron el MD del SD2 (cuerpo y anexos) y el checkout LaTeX `../LafroX-sd2-latex` (contenido.tex, anexos.tex y los dos .tex raíz). Sólo .md en rama-md.
- **S2-11 (fila 20):** nueva §2.2.4 «Prácticas de la industria que el caso pide investigar», con las ocho materias del 16.2 que faltaban (EDI, frío, indicadores de servicio, costo de servir/por entrega, VRPTW, picking y ubicación, pronóstico, logística inversa, modelos de atención). Solo datos del caso con página verificada en el PDF original (imagen n = página n−1): secc. 4.1–4.9 pp. 7–9, cap. 1 p. 3, tabla 7.3 p. 12, cap. 8 pp. 13–15, 16.2 pp. 29–30, glosario cap. C pp. 39–40.
- **S2-16 (fila 25):** Tabla 2.2 convertida en matriz influencia (muy alta/alta/media) × interés (alto/muy alto); «Media-alta» → «Media» en la Tabla 2.2 y en el Anexo 2.3 (3 filas), sin mover actores. SD3-Anexos l. 625 (planificador Alta/Muy alto) sigue coherente.
- **S2-18 (fila 27):** el SD3 (S-21, RNG-15, D-03) solo remitía al SD2; se agregó en la tensión 1 la justificación del corte de las 14:00 con el ciclo del caso (rutas 15:00–18:30, preparación 22:00–06:00, despacho de madrugada; secc. 4.4 a 4.6, p. 8).
- **Portada:** clave `caso = {Caso --- Logística}` en los dos .tex raíz del SD2, sin tocar `lafrox.cls`; los demás subdocumentos siguen con «Caso 02».
- **S2-06:** pospuesto por el usuario.
- Compilado: cuerpo 28 páginas, anexos 20, sin errores ni cajas desbordadas. Página 12 casi vacía (Tabla 2.1 pasa entera a la 13). Trazabilidad SD2 actualizada con páginas nuevas.
- **Pendientes fuera del SD2 (no tocados):** RF-10.01 del SD3 sugiere reposición solo con historia de ventas, sin estacionalidad ni promociones, que el SD2 ahora describe como parte del problema; T-14 1.4.1 habla de 17 grupos de interesados frente a 19 actores. Tabla 2.4 de IA: filas 2.2–2.5 anteriores a estos cambios y nivel «Bajo» por revisar.

Sin commit ni push.

## Estado vigente — 11 de octubre de 2026: revisión de pendientes S2-05, S2-06, S2-11, S2-16 y S2-20

- **S2-05 (aprobado):** párrafo de cadena causal al final de §2.2.1, en el MD y en el LaTeX. Recompilado sin errores, desbordes ni avisos (25 páginas); orden de figuras y tablas intacto; paridad MD = LaTeX. Trazabilidad S2-05 → Documentado.
- **Hallazgos, sin cambios** (por instrucción del usuario):
  - **S2-20:** los supuestos existen fuera del SD2: SD3 Anexo 3.C, S-18 (interfaces del ERP), S-19 (telemetría) y S-17 a S-44; SD4 Anexo 4-W, SV-01 a SV-07 (volumen, concurrencia y crecimiento). El SD2 no los menciona.
  - **S2-11:** las materias del 16.2 aparecen como solución en SD3, SD4, SD5 y SD13 (VRP en SD4 4.1, OpenAS2/ASN, regla térmica, olas/FEFO, M8, portal). Pronóstico de demanda prácticamente ausente en toda la propuesta; costo por entrega solo como métrica del SD13.
  - **S2-06:** hay fuentes externas reales en SD13 (GS1 EPCIS 2.0, Koutsoumanis 2005, Jedermann 2014, Riesenegger 2023) y SD4 (SII Oficio 781), pero sin datos cuantitativos de la industria; el SD2 no las usa.
- **S2-20 (aplicado a pedido del usuario):** §2.5.2 en MD y LaTeX: párrafo inicial reescrito (S-01 a S-16 y SP-01 a SP-03 en el Anexo 2.2) y párrafo nuevo que remite a S-17 a S-44 del Anexo 3.C del SD3 (S-18 ERP, S-19 telemetría) y a SV-01 a SV-07 del Anexo 4-W del SD4. Recompilado: 25 páginas, sin errores ni cajas desbordadas; §2.5.2 en pp. 22–23. Trazabilidad fila 29 → Documentado. La fila 2.5 de la Tabla 2.4 de IA es anterior al cambio.
- **S2-16:** se propuso al usuario una matriz influencia × interés en tabla con los 19 actores; pendiente de su aprobación.

Sin commit.

## Estado anterior — 11 de octubre de 2026: MD del SD2 sincronizado con el LaTeX (0a6f788)

Por petición del usuario, se tomó el LaTeX como fuente y se cotejó el MD por bloques (párrafos, ítems, filas de tabla, leyendas y títulos, en orden) en modo estricto y luego por formato (negritas y cursivas). El contenido ya coincidía; se corrigieron en el MD:
- signo menos en «−22 °C» (anexos);
- «$ 4,2 millones» (cuerpo);
- 41 negritas y cursivas en el cuerpo: rótulos de listas, «Decisión que requiere la necesidad:», términos como *fill rate*, *cross-docking*, *AS-IS* y *recall*, y títulos APA de las referencias;
- 4 marcas en los anexos.

Resultado: 0 diferencias de contenido y de formato. Pendiente de decisión: los enlaces del MD `figuras/figura 2.x.pdf` apuntan a una carpeta que solo existe en el checkout LaTeX. Sin commit.

## Estado anterior — 11 de octubre de 2026: SD2 LaTeX publicado con fecha de entrega

Por instrucción del usuario, la fecha de emisión de las portadas del SD2 (cuerpo y anexos) queda en «12 de octubre de 2026». Se fijó con la clave `fecha` de `\datoslafrox` en los dos `.tex` raíz, sin tocar la plantilla común. Se recompiló sin errores ni desbordes (25 y 20 páginas) y se hizo commit y push en `LafroX-Subdoc2-LateX` (0a6f788). En rama-md, los cambios MD del SD2 ya estaban publicados por el usuario (97d7321); se actualizaron la trazabilidad del SD2 y este contexto. Pendientes del SD2: marcador «[[REVISIÓN HUMANA]]» en la Tabla 2.A.9, fila 2.3 de la Tabla 2.4, erratas dentro de las imágenes y «Caso 02» en la plantilla común de portadas.

## Estado anterior — 11 de octubre de 2026: revisión exhaustiva y recompilación del SD2 LaTeX

Por instrucción del usuario («revisa todo exhaustivamente, compila y vuelve a revisar»), se auditó por script el PDF del SD2: orden cita → figura/tabla → análisis, tamaño de letra, ocupación de páginas, cortes de listas y avisos del compilador. También se revisaron visualmente las 25 páginas del cuerpo y las 20 de los anexos.

Cambios en el checkout LaTeX:
- Figuras fijadas con `[H]` (paquete float) para que no se adelanten a su explicación.
- Lista de pasos antes o después de cada figura, elegida entre 32 combinaciones compiladas por el menor espacio en blanco: después en los procesos 1, 3 y 6.
- Listas de pasos que no se cortan entre páginas (`needspace`); `needspace` también antes de 2.3.1 y de la Tabla 2.2.
- `\hyphenation` para Figura, Tabla, Anexo y Restricciones; título 2.5 con salto manual.
- Espacios no separables en «Figura~2.x», «Tabla~2.x» y «Anexo~2.x».
- Signos menos tipográficos.
- Conclusiones nuevas tras la Tabla 2.1 y la Tabla 2.4.
- Anexos: columnas de identificadores y de «Fuente» más anchas; «Muy alta/Muy alto» unificado.

Resultado: cuerpo de 25 páginas y anexos de 20, sin errores, desbordes ni avisos. Todo el texto de las figuras queda en 9,1–9,2 pt. Quedan páginas parcialmente vacías junto a las figuras horizontales (pp. 13 y 17) y antes de las Tablas 2.1 y 2.2 (pp. 9 y 20): son consecuencia de mantener figura y tabla juntas sin violar el orden. MD alineado (orden de figuras de los procesos 1, 3 y 6, frases nuevas, signos menos y mayúsculas). Trazabilidad SD2 reescrita con las páginas finales. Sin commit.

## Estado anterior — 11 de octubre de 2026: SD2 LaTeX ajustado a las Aclaraciones (tablas, figuras y referencias)

Autorización explícita del usuario: dejar el LaTeX del SD2 (`../LafroX-sd2-latex`, rama `LafroX-Subdoc2-LateX`) cumpliendo las Aclaraciones, en especial tablas y figuras, y reemplazar «Caso 02» por «caso», también en la referencia. Se editaron `contenido.tex`, `anexos.tex` y los dos `.tex` raíz, y se recompiló sin errores ni cajas desbordadas: cuerpo de 24 páginas y anexos de 20, sin commit. Cambios:
- Figuras: escala para que todo el texto quede en 9 pt o más (medido entre 9,1 y 9,2), recorte solo de margen en blanco, 2.1 y 2.5 en página horizontal (pdflscape) y la 2.5 armada con las dos páginas de su exportación, sin alterar la imagen.
- Tablas del cuerpo:
  - Tabla 2.1: 4 columnas, una frase por celda, cifras a la derecha, en una página (needspace) y con análisis de sus columnas.
  - Tabla 2.2: sin columna de estrategia, con nuevo análisis de influencia e interés.
  - Tabla 2.3: sin la columna «Origen», que repetía el mismo valor.
  - Tabla 2.4: anchos sin palabras cortadas; guiones desactivados en las tablas del cuerpo.
- Citas a las Bases con página, cotejada en los PDF originales: caso p. 3–39, BA art. 16.1 p. 11 y art. 78 p. 40, BTT cap. 7 pp. 17–18 y RT-03.10/03.12 p. 9. Se agregaron citas a BA (modelo híbrido) y BTT (disponibilidad) para que toda la lista quede citada.
- Anexos: referencias APA completas; tabla de IA renumerada como 2.A.9; sin lista de figuras vacía.
- MD de rama-md alineado con todos estos cambios de texto.
- Trazabilidad SD2 actualizada con las páginas nuevas.

Pendientes: marcador «[[REVISIÓN HUMANA]]» en la 2.A.9 (bloqueante); fila 2.3 de la Tabla 2.4 desactualizada; erratas dentro de las imágenes; fecha de portada 05-10; la plantilla común imprime «Caso 02 — Logística» en todas las portadas (no se tocó).

## Estado vigente — 11 de octubre de 2026: análisis AS-IS del SD2 (observación S2-03)

Por petición del usuario se reescribieron en el MD del SD2 los seis párrafos de análisis de §2.3.2 («breve, redacción humana»). Cada párrafo indica dónde se pierde el dato, su efecto aguas abajo y qué falta medir. Se agregó un párrafo final que conecta los seis procesos con §2.2.1. Solo se usaron cifras ya presentes en el SD2 o en el caso (cap. 4.4: 3,5 h, once hojas, caída de 6 a 9 puntos; $4,2 millones). S2-03 pasa a «Documentado en MD; LaTeX pendiente». La fila 2.3 de la Tabla 2.4 de IA (revisión de Tomás Pérez) es anterior a este cambio y debe volver a revisarse. No se tocó el LaTeX; sin commit.

## Estado vigente — 11 de octubre de 2026: trazabilidad de observaciones del Informe 1 para SD3

Por petición del usuario se recompiló con `latexmk -g` el checkout `../LafroX-sd3-latex` (commit ddee65e), sin errores: cuerpo de 33 páginas, anexos de 169 y T-12 de 222, en carta. Solo cambiaron los PDF y los auxiliares de ese checkout; quedan sin commit. Se creó `Revision/trazabilidad_Informe1_Informe2_SD3.md`, con 38 filas específicas (S3-00 a S3-37) y 5 generales. Pendiente bloqueante: la Tabla 3.6 de IA tiene «No documentada» en las 18 filas y fechas de edición (7-10 y 9-10-2026). Otros pendientes: la Figura 3.4 es ilegible; no hay columna de EDT en el T-12; las prioridades son 84 % Crítica o Alta; faltan automatización y enfoque SRE en §3.4.5; el umbral de §3.4.3 no coincide con D-12; el LaTeX está desfasado de 55b65c6; la fecha de portada es 05-10. No se editaron fuentes ni imágenes; sin commit.

## Estado vigente — 11 de octubre de 2026: excepciones explícitas y revisión compilada del SD1 LaTeX

El usuario ordenó modificar AGENTS.md para admitir excepciones a petición explícita. Se reemplazó el rechazo incondicional por un régimen acotado: rama-md sigue creando/editando/versionando sólo Markdown, pero las operaciones expresamente solicitadas pueden ejecutarse en el checkout LaTeX correspondiente, con comprobación de destino y permisos. Leer/compilar no autoriza editar fuentes ni commit/push. Se registró autorización vigente del SD1 para revisión, compilación y tabla Markdown.

Destino comprobado: `C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX-sd1-latex`, rama `LafroX-Subdoc1-LateX`, HEAD observado c5ea75b; consulta de status falló por entorno/permisos, no se afirmó checkout limpio. Se leyeron fuentes, plantilla y configuración. Primer intento latexmk falló por quoting de -e; compilación directa LuaLaTeX con --no-shell-escape y tres pasadas por archivo terminó con salida 0: SD1 21 páginas, T-6 9. PDF/auxiliares y previsualizaciones quedaron sólo en el checkout LaTeX, mediante permisos escalados aprobados. No se editaron sus fuentes ni configuración.

Registro nuevo separado: `Revision/trazabilidad_Informe1_Informe2_SD1_LaTeX.md`, 28 observaciones y mapa de páginas. Conserva el registro anterior basado en Markdown. Inspección visual focal: SD1 1/8/21 y T-6 6/8/9; lectura de fuentes/índice/texto. Organigrama real y legible en SD1 p8, a diferencia del MD. Formato carta verificado en ambos PDF; cuerpo11pt configurado. Defecto vigente confirmado: Tabla1.4 p21 invade pie; log «Float too large for page by69.95325pt». Portada sigue T-7 y línea de firma vacía; una revisión humana pendiente. Acreditaciones y revisión visual integral no comprobadas. No se aplicaron reparaciones ni se declara conformidad total.

## Resumen de sesión — trazabilidad SD1 y excepción de trabajo

**Objetivo:** responder dónde se exige trazabilidad entre informes y prepararla para SD1 desde Markdown y, por autorización posterior, desde LaTeX compilado. **Instrucción nueva:** ejecutar excepciones expresamente pedidas sin rechazo automático, conservando archivos no Markdown fuera de rama-md. **Completado:** base normativa BA46/T22 localizada; dos registros de28 observaciones; AGENTS actualizado; dos PDF compilados y revisión focal. **Descubrimientos:** ausencia gráfica del MD no implica ausencia en PDF; compilación exitosa no impide desborde visual. **Siguiente:** corregir desborde/portada y completar firma/revisión humana/evidencia sólo con autorización pertinente. **Archivos:** AGENTS.md, los dos registros Revision/trazabilidad_Informe1_Informe2_SD1*.md y este contexto. Sin commit/push/cambio de rama del checkout principal. Preservado archivo concurrente de trazabilidad SD2. Engram no disponible en las herramientas; guardado/resumen de memoria pendientes, registrados localmente.

## Estado vigente — 11 de octubre de 2026: trazabilidad de observaciones del Informe 1 para SD2

Por petición del usuario se contrastó `Revision_informe.md` (SUBDOCUMENTO 2 y generales) con el MD del SD2 y con el checkout `../LafroX-sd2-latex` (commit 1586eb7; PDF de 23 y 21 páginas, carta, revisados en modo de solo lectura). Se creó `Revision/trazabilidad_Informe1_Informe2_SD2.md`, con 23 filas específicas, 9 generales y páginas del PDF. Pendiente bloqueante: el PDF de los anexos muestra «[[REVISIÓN HUMANA]]» en la fila de IA de Codex, y esa tabla repite el número 2.A.8. Otros pendientes: erratas dentro de las Figuras 2.1, 2.2, 2.5 y 2.6, recorte de la 2.5 y cajas que no coinciden con los pasos; matriz influencia–interés sin cuadrantes; supuestos propios incompletos; materias del 16.2 parciales; Referencias de los anexos no APA; fecha de portada 05-10; la carpeta de figuras no existe en rama-md. No se editaron entregables, imágenes ni LaTeX; sin commit.

## Estado vigente — 11 de octubre de 2026: trazabilidad de observaciones del Informe 1 para SD1

Por petición del usuario se leyó `Revision_informe.md` (fuente aportada, sin versionar) en sus apartados GENERAL y SUBDOCUMENTO 1 y se contrastó con SD1 y T-6 actuales. Se creó `Revision/trazabilidad_Informe1_Informe2_SD1.md`: 22 observaciones específicas y seis generales aplicables, en tablas de tres columnas observación–respuesta–ubicación. Se distinguen presencia documental, acreditación pendiente y controles exclusivos del PDF; no se afirma cierre total ni se alteraron entregables. Base normativa comprobada: BA artículo 46° y T-22 Informe 2.

Pendientes observados: Figura 1.1 sólo descrita, sin imagen enlazada; portada SD1 rotulada T-7; antigüedad/turnos corporativos, inventario y dimensionamiento de mesa sin acreditar en SD1; certificados/experiencia/alianzas declarados, no comprobados; una fila de IA con revisión humana pendiente; firma, foliación y forma PDF no comprobadas. No se inventaron antecedentes ni se completaron revisores. Rama comprobada rama-md; sólo Markdown; sin commit/push. Engram no figura entre las herramientas disponibles; guardado y resumen persistente pendientes, con este registro local como respaldo.

## Estado vigente — 11 de octubre de 2026: G5 en H6/H11, arquitectura híbrida en el SD9 y propagación a SD1, SD3, SD6, SD7 y SD8

Por decisión del usuario (Guillermo Castillo), G5 es la puerta de entrada de cada etapa a Producción en H6 y H11; H7 y H12 aceptan la marcha blanca con las seis condiciones del Art. 17.3 y no son una puerta. Reemplaza la regla anterior «G5 permanece H7/H12». SD9 v_nueva: Figura 9.3, Tabla 9.7, 9.2.1, Tablas 9.11/9.12 (filas de hito por entregable, G5 en meses 13 y 19, revisión del CLIENTE en meses 10, 11, 17 y 18), Anexo 9.B y T-17 4.3. Se agregaron los nueve protocolos del SD4, Anexo 4-V (T-13 7.5 nueva; 9.2.3), escenarios de pérdida de fibra/LTE y de gateway de frío (T-13 7.2; 9A-22 = 8 de 8), recuperación del WMS de Talca, umbrales de usabilidad del SD3 Tabla 3.A.4a (9A-18), infraestructura ≥ 99,95 % (9A-20), acoplamiento eferente ≤ 20 clases (Tabla 9.4; 9A-33; siete métricas de código), densidad de defectos > 1,5 × mediana y p95 de búsqueda/informe del SD4 Tabla 31. El costo de la calidad del md (11.136 HH, sin fallas esperadas del SD8) se conserva.

Propagación: T-10 y SD6 con las tres reglas bloqueantes nuevas; SD1 1.3.1 y SD3-Anexos D-12 con 70 % negocio + 80 % global (C-01); T-12 (13 filas) y SD3/SD3-Anexos con citas a la estructura vigente del SD9/T-13/T-17; T-14 con ocho restauraciones 13–20, actas 3.8.7/3.9.6 que exigen 3.8.8/3.9.7 y H4 en el mes 10; SD8, T-16 y resumen del SD8 con línea base 217.543 HH (base 205.135), soporte puente 16.712, peak 69 y reservas no replicadas en el T-15 4.5. Las 7 marcas [[REVISIÓN HUMANA]] siguen pendientes. Rama local md-correcciones desde rama-md cf43057; sin push.

## Estado vigente — 11 de octubre de 2026: SD9 v_nueva sincronizado desde sus fuentes revisadas

El usuario confirmó que `rama-md` es la nueva `branch-md`; AGENTS.md registra la identidad actual, conservando la exclusividad Markdown. Se trasladaron desde `Subdoc/LafroX/SD9_v_nueva` al cuerpo, T-13 y T-17 de `09_plan_calidad/v_nueva/` los cambios de redacción/citas, roles, restauración mensual de meses 13–20 por SRE dentro de 4.2.1/4.3.1, declaración de IA y dos tablas mes a mes (9.11/9.12; reservas y periódicas pasan a 9.13/9.14). Figura 9.9 Mermaid refleja la vista mensual de 56 meses con 12 hitos y 7/6/3 pruebas puntuales. Anexos cotejados sin diferencias sustantivas; no se reescribieron. El cuerpo antiguo fuera de v_nueva, v_vieja, T-14 modificado y los dos informes Revision no versionados quedaron intactos.

Verificación: cero diferencias normalizadas en párrafos, cabeceras y filas de los cuatro inputs activos; 62 tablas uniformes, 89 encabezados y 21 enlaces de índice válidos; `git diff --check` salida 0. Las siete marcas humanas del cuerpo siguen pendientes. Se conservan inconsistencias fuente (36 restauraciones corresponden sólo a Operación; intrusión anual frente a la frase «cada tipo» ≤6 meses), sin corregir documentos externos ni afirmar coherencia global. No se crearon/editaron/compilaron fuentes LaTeX ni derivados. Tarea `odd/tasks/sd9-source-sync.md`; commit pendiente a cargo del coordinador, sin push.

## Estado vigente — 11 de octubre de 2026: revisión v7 del SD9

`Revision/revision_comision_informe2_SD9_v7.md` aplica el prompt del Informe 2 al SD9 ya corregido. Puntaje 0 por las 16 celdas de revisión humana; contenido sin esa causal 40 (provisional). De la v6: 21 corregidas, 4 parciales. Observaciones nuevas N7-01 a N7-13; las mayores: restauración mensual de los meses 13–20 sin paquete en el T-14 (introducida por la v6), sin prueba de retiro sanitario en el T-13, dos tablas con 6 columnas y capacidad de las instancias PRE sin declarar. En esta corrida también se completaron las 5 filas RF-14.xx-BTT de la matriz 9.C (escenario y CP-ID), se alineó el T-10 (Playwright, Pact/Spectral, MobSF) y se sincronizó el Resumen del T-10. El SD8 se está rehaciendo: la sección 4 de la v7 lista lo que hay que re-verificar. Sin commit.

## Estado vigente — 11 de octubre de 2026: cierre de pendientes de la v6 del SD9

Por instrucción del usuario («base sólida y sin contradicciones») se aplicaron los pendientes de la entrada siguiente, sólo Markdown y sin commit. (1) N-07: duplicación de código ≤ 3 % de las líneas, bloqueante en G2, como propuesta de LafroX (SD9 Tabla 9.3, Fig. 9.1 con 6 umbrales, 9A-27, 9B-23, B.2; SD4 ≈l.2255 y T-10 con su bullet de compuertas). (2) H8: subsanación de 4 días hábiles (igual a su reserva) y H1 de 5; holgura H8 = 0 y ninguna negativa (SD9 Tabla 9.13, T-15 5.5, T-16 y SD8 Anexos R8-12/E8-11, T-17 1.2). (3) Feriados: el T-15 declara que no los descuenta (R8-17 los convierte en el mes 1); nota en la Tabla 5.2: límite H2 14-05-2027 (reserva 11) y H3 15-07-2027 (reserva 18); T-17 fichas H2/H3 y SD9 con la misma nota; probabilidades de la Tabla 5.2 no recalculadas. (4) DR: se agregó una prueba en el mes 21 (oct-2028), de modo que son 7 (21, 27, 33, 39, 45, 51, 54); T-14 8.1.3, T-15 (7 ocurrencias, 11,4 HH máximas), SD9 Tabla 9.14/Fig. 9.9/9.3.3 y T-13 T13.6; el planilla LafroX-Calculos-SD9.xlsx (Calendario) y la Fig_9-9 .drawio quedan sin actualizar. (5) SD4 4.2.4.1: instancias efímeras de Preproducción por campaña. Siguen pendientes: imagen enlazada de las 10 figuras, 16 celdas de revisión humana, páginas de las citas a las Bases (requiere PDF) y recalcular las probabilidades del T-15/SD8 con las reservas de H2 y H3.

## Estado vigente — 11 de octubre de 2026: revisión v6 del SD9 aplicada (sin N-07)

Por instrucción del usuario se aplicó `Revision/revision_comision_informe2_SD9_v6.md` al SD9, anexos, T-13 y T-17 (sólo Markdown, sin commit). Aplicado: N-01 (G5 = sólo H7/H12; correcciones de marcha blanca = G0–G4 y G6 más repetición de la prueba afectada, Tabla 9.5 y 9.2.1); N-02 (regla de correcciones en el congelamiento de septiembre de 2028 por cambio de emergencia del SD4 4.2.4.1.4; SD9 9.3.2 y T-13 8.3); N-03 (restauración mensual desde el mes 13; separación de seis meses contada desde el mes 21; RT-07.07 «al menos dos veces al año» y RT-10.07 citados literalmente); N-04 (instancias PRE-M/C/S/A de Preproducción reconstruidas desde código, Tabla 9.11); N-05 (Tabla 9.13 con H1–H5, H8–H10, subsanación de 5 días en H1/H8; H8 queda en −1); N-06 (Tabla 9.12: paquete, ventana, responsable, HH máximas y reserva); N-08/N-09 (acoplamiento en Tabla 9.3; reglas 9B-24 a 9B-27); N-10 (CMMI-DEV v2.0 + OWASP SAMM como modelos de madurez y su uso; sin SCAMPI ni TMMi); N-11 (métricas de defectos y observaciones en Tabla 9.4); N-12 (99,95 % de infraestructura, 9A-17; las métricas 9A-17 a 9A-29 se corrieron a 9A-18 a 9A-30; 30 métricas); N-13; N-14 (Tabla 9.7 riesgos SD8 → prueba; 29119-2); N-15 (escenario y CP-ID por fila en 9.C); N-16 (ventana 05:30–07:00 a 10,41 TPS en Tabla 9.6, T13.3, T-17 H5/H10 y 9A-08); N-17 (Playwright, Pact/Spectral, MobSF; propagados a SD4, SD4-Anexos y T-11); N-18; N-19; N-20; N-21; N-22 a N-26 (voz, glosario, autocita retirada, renumeración de tablas: control documental 9.8, mejora 9.9, paquetes 9.10, campañas 9.11, repetición 9.12, hitos 9.13, periódicas 9.14; T-12 actualizado de Tabla 9.9 a 9.14). Sin aplicar: N-07 (umbral numérico bloqueante de duplicación; contradice la decisión previa del usuario y el SD4 ≈l.2255); páginas de citas a las Bases (requiere PDF); imagen enlazada de las 10 figuras; 16 celdas de revisión humana; Fig_9-9 y Fig_9-1 .drawio desfasadas. Pendientes aguas arriba: T-15 Tabla 5.2 (límites de H2 y H3 caen en feriado; H8 con reserva menor que su subsanación), DR/resiliencia previas al mes 27 si se quiere separación ≤ 6 meses entre la certificación de mayo de 2028 y la Operación, y las instancias de Preproducción en SD4.

## Estado vigente — 11 de octubre de 2026: SD9 alineado con los subdocumentos anteriores

Criterio del usuario: el SD9 se ajusta a SD1–SD7, no al revés (el SD8 es gemelo). Aplicado en SD9, T-13 y T-17: (1) fechas de pruebas periódicas del T-14: DR en 27/33/39/45/51/54 y resiliencia en 26/32/38/44/50/55 (Tabla 9.9, Figura 9.9 Mermaid, 9.3.3, T13.6); intrusión 28/40/52 sin cambio; la primera DR queda a seis meses del inicio de Operación (riesgo frente a Art. 20/RT-07.07, sin resolver); (2) se quitó la carga anual previa al peak por no existir en T-14/T-15; (3) la certificación de cierre H7/H12 se reescribió con los paquetes existentes (3.8.x, 3.9.x, 4.2.3, 4.3.3) y la reserva protegida E1 del T-15; correcciones de marcha blanca repiten solo la prueba afectada; (4) Comité de Calidad sin veto (SD1 l.175); (5) capacidad de evaluadores 16 × 128 = 2.048 HH/mes (T-15 4.1); (6) G5 = pasos H7/H12, versiones quincenales de Operación = G0–G4 y G6 (T-10). Sin cambio: Tabla 9.8 coincide con T-15 Tabla 5.2; campañas simultáneas en Preproducción siguen según T-15 (nota para el SD8, R8-07). Pendientes: Fig_9-9 y Fig_9-1 (.drawio) desfasadas; 16 celdas de revisión humana. Sin commit.

## Estado vigente — 11 de octubre de 2026: SD9 alineado con clases y PMBOK

Por instrucción del usuario se quitó del SD9 lo que no está en clases ni lo exigen las Bases: TMMi (9.1.2, Tabla 9.1 y referencia), reparto del costo de la calidad en HH (9.1.5, ahora «Métricas de proceso») y SLSA nivel 3 (9.2.1). La guía de control pasa a ser Tabla 9.1. Se corrigieron además captions y notas de proceso de la v4 (ver entrada siguiente). Conservado por las Bases: ISO 25010/25012, 29119, CMMI, métricas de código, pentest, WCAG. Luego, por instrucción del usuario, se quitaron los umbrales propios: complejidad cognitiva ≤15, duplicación ≤3 %, deuda ≤5 % y DRE ≥95 % (SD9 Tablas 9.3 y 9.4, 9.1.4, 9.1.5, análisis estático, Figura 9.1; Anexo 9.A 28 métricas con 9A-26 a 9A-28 renumeradas; Anexo 9.B 21 reglas con renumeración 9B-09 a 9B-21). Después, por indicación del usuario, se restituyó lo que SD3/SD4/T-10/T-12 ya mencionaban: SLSA nivel 3 (9.2.1), deuda técnica bloqueante = 0 (T-10) y duplicación medida sin umbral bloqueante (PHPCPD, jscpd; SD4 ≈l.2255). Resultado: Anexo 9.A 29 métricas (9A-26 restituida) y Anexo 9.B 23 reglas (9B-22 y 9B-23 nuevas). Siguen eliminados, por no figurar en subdocumentos anteriores: TMMi, reparto del costo de la calidad, complejidad cognitiva, DRE y los umbrales numéricos de duplicación (3 %) y deuda (5 %). En Diagramas/Fig_9-1 (.drawio) las etiquetas pueden diferir. Sin commit.

## Estado vigente — 11 de octubre de 2026: revisión v4 del SD9

`Revision/revision_comision_informe2_SD9_v4.md` aplica el prompt del Informe 2 al SD9 (cuerpo, anexos, T-13, T-17). Puntaje 0/100 por 16 celdas `[[REVISIÓN HUMANA]]` y notas de proceso en el cuerpo (SD9:391, 403, 440, 522–524); contenido 20. Hallazgos nuevos: el T-14 (8.1.3, 8.2.2) mantiene meses de DR y resiliencia distintos de SD9/T-13 (11 de 12 difieren); las pruebas previas a H7/H12 siguen sin paquete, fecha ni HH; el ambiente del pentest y la resiliencia es contradictorio entre Fig. 9.4, Tabla 9.6 y T-13; Tabla 9.8 sin cambios (feriados, segunda revisión). De 14 hallazgos de v3 re-verificados: 8 corregidos, 2 parciales, 4 no corregidos. No se editaron entregables; sin commit.

## Estado vigente — 11 de octubre de 2026 (madrugada): revisión cruzada del T-12, 645 filas

Por instrucción del usuario («todo lo que diga que se cumple realmente sea así, y viceversa»), revisión fila a fila del T-12 contra Bases y subdocumentos; sólo Markdown en rama-md, sin commit. Informe: `Revision/revision_cruzada_T12_2026-10-11.md`. Comprobado: 374 RT = BTT con texto literal; 26 valores del Caso cap. 15 presentes; Parte A = SD3 por ID y, tras la corrección, por texto (0 diferencias); todas las secciones citadas existen. Ningún estado cambia (614/13/18; A 271/0/0, B 343/13/18) y 9.C sigue sin diferencias: no hay arrastre a SD3 3.2, SD9, T-13 ni planilla. Correcciones: descripciones RF-03.11/03.12/09.06/18.01 iguales al SD3; RT-06.06 y RT-19.09 citaban tablas inexistentes del SD6 (ahora SD6-Anexos 6.B y T-9 3); RT-05.01 121 entidades/987 atributos (resúmenes SD5 también); SD5-Anexos `disposicion` agrega VENTA_DESCUENTO y DEVOLUCION_PROVEEDOR (RF-08.02); ASN al cargar y acuse 30 min tras descarga separados (SD4 4.1.17.1, RNF-12.03 en SD3-Anexos y T-12); RT-21.07/RNF-21.04 declaran críticos y altos 24×7×365 (D-10); RT-03.13/03.24/05.15 responden también el valor del Caso; RF-07.08 y RF-12.07 tenían componente equivocado. Unas 45 filas RF/RNF declaraban «Cumple» sin mecanismo descrito: se agregaron frases en SD4 4.1.3.7 (AES-256), 4.1.4.3 (conteo, vida útil, cross-docking), 4.1.4.4 (consulta y control comercial: crédito > límite alerta, > 110 % bloqueo con supervisor; cliente con mora > 30 días o deuda sobre cupo bloqueado, RF-07.05), 4.1.4.5, 4.1.4.6, 4.1.4.7, 4.1.4.8 (M1, M5, M6, M8, M11, M12) y 4.1.17.1, y en SD4-Anexos 4-A (desvío > 3 km), con 61 celdas del T-12 actualizadas. T-12: referencia «Subdocumentos 1–9 y 13»; finales de línea normalizados a CRLF. Pendientes: cámara del MC9400 para la foto de RF-01.04 (T-11 no la declara); atributos SD5 para pago «En revisión», umbral de envases y peajes; LaTeX de T-12, SD3-Anexos, SD4, SD4-Anexos y SD5-Anexos queda desfasado respecto de esta revisión; la declaración de IA del SD3 dice «No documentada.» en vez de `[[REVISIÓN HUMANA]]`.

## Estado anterior — 11 de octubre de 2026 (madrugada): LaTeX de SD1–SD4 sincronizado con rama-md

Por instrucción del usuario, el MD de `rama-md` (`baf991d` más el cambio sin commit del T-12 MD: RF-03.11/03.12 alineados con la Tabla 3.A.1, RF-09.06, RF-18.01, RT-06.06 y RT-19.09) se trasladó a los worktrees LaTeX, sin tocar LaTeX en rama-md. Ningún LaTeX tenía commits posteriores a su última alineación, así que el MD era la versión más avanzada en los cuatro.

- SD1 (`../LafroX-sd1-latex`): Guillermo Castillo como gerente de servicio dedicado (viñeta de roles y Tabla 1.3). T-6 sin cambios.
- SD2: sin cambios en el MD desde la última alineación; la revisión de cobertura no mostró diferencias de contenido.
- SD3 (`../LafroX-sd3-latex`): catálogo 262 (176 RF), 12 propios (2/6/4), 56/163/43, todos ofertados, 5 materias absorbidas, RF-07.01 propio (Tablas 3.A.3a y 3.A.3b) y renumeración RF-07.02–07.11, F-10, RNF-09.04 «fuera de la cámara», preparadores 120 + 60. T-12 regenerado por filas desde el MD (640 filas; conversor validado con 0 diferencias contra el MD anterior).
- SD4 (`../LafroX-subdoc4`): cambios del MD posteriores a `fd26905` (RT-16.14 Symfony ExpressionLanguage con su referencia y fila del Anexo 4-P, RT-08.04 conmutadores, autonomía condicionada, firewall con salida tributaria, totales 224.652/342.933 con INT-04 dentro de INT-03, cota 111,70, secuencia regional, cobertura regional por servicio, nueva liberación sanitaria en 4-J, RF-07.01 a 07.03 en M7, entre otros). Verificación con `tex2md.py` en ambas direcciones: solo quedan los artefactos conocidos del conversor y dos giros propios del LaTeX («La figura muestra que…», «el Formulario T-11»).
- Los siete PDF compilan sin errores ni referencias indefinidas; los desbordes de la tabla del T-11 son anteriores. Sin commit en ninguna rama.

## Estado anterior — 11 de octubre de 2026: coherencia interna SD4 aplicada

Por instrucción del usuario se ejecutó el plan acotado de coherencia entre 4.1, 4.2, 4.3, anexos y T-11 en `rama-md`, conservando estructura y figuras. Base local `9e4dce0`; el remoto conocido `4212f7c` tiene los mismos tres archivos SD4 antes de editar. Después se realizó pull hasta `78bc2ed` y se reaplicaron sin conflictos las correcciones locales, conservando el stash de respaldo. El usuario solicita registrar estos cinco Markdown con el mensaje `correcciones de coherencia entre documento` y publicarlos en `origin/rama-md`. Registro: `Revision/coherencia_interna_SD4_2026-10-11.md`.

Ajustes: autonomía condicionada y dependencia ERP/SII; bloqueo sanitario distinto de nueva liberación; credencial de 14 h distinta de ruta física de 14,5 h; firewall distingue entradas y salida tributaria; responsabilidades M2/M3/M7 y evento térmico; conmutación tras exclusión del escritor; recuperación de Talca incluye red; reconexión regional antes de validación y tráfico (135 min sin cambio); cobertura regional por canal; INT-04 incluido en INT-03 (224.652/342.933 mensajes/día); perfil cross-docking agregado; cota completa 111,70 solicitudes/s y 8 tareas; promedio de retorno distinto de sensibilidad de 64 simultáneos; recuperación sanitaria <2 h separada del presupuesto regional; BI/API, mTLS/OAuth/IPsec e inventario de ExpressionLanguage.

Pendientes técnicos explícitos: recorrido local de Calidad; restitución de LAN/firewall tras pérdida de sala; recuperación por servicio de consola/rutas/AS2/IoT y caché; consulta sanitaria antes de 2 h; mediciones de concurrencia y ventanas de credenciales. No se inventaron equipos, aprobaciones ni ensayos. T-12 y otros subdocumentos sin cambios; `md para drive/` y stash previo preservados. LaTeX queda pendiente de una sincronización autorizada posterior. Las revisiones humanas conservan su estado.

## Estado vigente — 10 de octubre de 2026 (noche): 15 RF del SD5 en Cumple

## Estado vigente — 10 de octubre de 2026 (noche): 15 RF del SD5 en Cumple

Contrastados contra el SD5 de 32969e4 (más el ajuste sin commit de la línea 257, numeración RF-07.04/.05/.07/.11 correcta): RF-01.08, 01.10, 01.11, 02.01, 02.03, 02.07, 02.08, 03.12, 04.01, 04.03, 07.04, 07.05, 07.07, 08.07 y 11.05 pasan a Cumple en el T-12, con su justificación reescrita sin «Falta» y referencias a SD5 agregadas; el estado del Anexo 9.C quedó sincronizado (sin diferencias; los casos no cambian, 1.308). Luego, por decisión del usuario, RF-18.03 y RT-16.23 (apertura) pasan a Cumple con SD5 5.1.9 (apertura_estado INFORMADA/NO_INFORMADA/NO_SOPORTADA); 9.C sincronizado. T-12: 608/15/22 (RF 181/0/0, RNF 87/1/2, RT 340/14/20). Después, sin paquetes nuevos: T-14 cuenta 8.2 agrega párrafo de bolsa evolutiva (768 HH DES/año dentro de las 4.608 HH de 8.2.1; correctivo sin tope; saldo acumulable por BTT 21.4; excedente con tarifa en la Oferta Económica; procedimiento solicitud/estimación 5 días hábiles/aprobación en Comité/liquidación mensual) y cuenta 8.1 agrega párrafo de traslados (N2 = SRE de 8.2.3, N3 = DES de 8.2.1, N4 fabricante; 8.1.2 son sólo puestos de mesa L1 según T-15 §4.1 y no se usan; recuperación del Art. 78° sigue remota, SD4 4.2.4.3; pasajes en Oferta Económica, BA 11.2 y 50.2). RNF-21.07, RT-21.16, RNF-21.08 y RT-21.19 en Cumple. Arrastre aplicado: SD3 3.2 (261 ofertados, 261/9/1), SD3-Anexos y su resumen (85 RNF ofertados), SD9 9.2.3 (852 + 355 + 105 = 1.312; 1.050 automatizados; 8,8 h; 4,38 h; 262 manuales, 65,5 HH sin cambio), 9.C y Tabla 9.C.1 (616/29; 20 No cumple), T-13. T-12: 612/13/20 (RF 181/0/0, RNF 89/0/1, RT 342/13/19). Planilla LafroX-Calculos-SD9.xlsx no editada (pendiente: RT 342/13/19 y 1.312 casos). RT-05.10, RT-06.12 y RT-07.08 son Deseables en BTT y quedan parciales. Luego, por decisión del usuario, Guillermo Castillo (Líder de Operación / SRE) queda como gerente de servicio dedicado: SD1 viñeta de roles y Tabla 1.3 (100 % meses 21 a 56), T-14 cuenta 8.1 (frase con BA art. 71 y RT-21.02); RNF-21.02 y RT-21.02 en Cumple. Arrastre: SD3 3.2 y SD3-Anexos (262 ofertados, todos Cumple; se corrigieron además dos frases residuales que decían 260 ofertados y 161 altos), resumen SD3-Anexos, SD9 9.2.3 (855 + 356 + 105 = 1.316; 1.053 automatizados; 8,8 h; 4,39 h; 263 manuales ≈ 65,8 HH), 9.C y Tabla 9.C.1 (618/27; 18 No cumple), T-13. T-12: 614/13/18 (RF 181/0/0, RNF 90/0/0, RT 343/13/18); 9.C sincronizado en las 645 filas. Planilla SD9 sin editar (RT 343/13/18; 1.316 casos). LaTeX del T-12, SD1, SD3, SD9 y T-14 desfasado. Sin commit. Ningún otro RT parcial dependía del SD5. El LaTeX del T-12 queda desfasado. Sin commit.

## Estado vigente — 10 de octubre de 2026 (noche): épica 7 restaurada a la numeración original

El CSV original no tiene RF-07.01 (ni RF-06.06). El SD3 entregado en Informe 1 (09ace4c) conservaba RF-07.01 «Cálculo del monto esperado de rendición por camión» (V-10/V-11), igual que RF-06.06; 26c345c (05-10) lo eliminó y corrió la épica (RF-07.02–07.11 → 07.01–07.10), dejando un RF-07.11 «No cumple» duplicado de RF-07.10 y referencias mezcladas (SD4 937/941, SD3 V-10 y fila de la interfaz ERP usaban la numeración original). Por instrucción del usuario se restauró la numeración original: RF-07.02–07.11 = catálogo consolidado; RF-07.01 = requisito propio LafroX (Tablas 3.A.3a y 3.A.3b, Alta/E1, Cumple; M7 calcula el monto esperado por camión y turno con entregas al contado y cobros de cob_cobro). Ahora los 134 RF del consolidado coinciden por ID con el T-12. Ajustados SD3 (catálogo 262 = 176 RF + 86 RNF; 8 propios RF, 12 en total: 2/6/4; 56/163/43; ofertados 260, 56/161/43; 5 materias absorbidas; 271 = 260 + 9 + 2), SD4 M7 (RF-07.01 a 07.03, 07.06 y 07.10, interfaz ERP RF-07.09), SD13 y innovaciones_corregidas (portal RF-07.07), SD9 9.C (RF 176/5/547; 614/31/1.308; 22 No cumple), SD9 9.2.3 (849 + 354 + 105 = 1.308; 1.046 automatizados; 8,7 h; 4,36 h; 262 manuales ≈ 65,5 HH), T-13 y resúmenes SD3. T-12 591/32/22 (A 252/17/2). Pendientes: planilla LafroX-Calculos-SD9.xlsx (1.305→1.308, C42–C44 339/15/20) y LaTeX de T-12/SD3/SD4/SD9 desfasados; el pendiente SD5 «RF-07.11/RF-07.10» del compañero se refiere ahora a RF-07.11 (preventista). Segunda revisión: nota bajo la Tabla 3.A.1 (RF-06.06 y RF-07.01 propios, en 3.A.3b); intro 3.A.3a sin «no ofertadas»; SD5 257 (commit 32969e4 de Bastián, numeración corrida) pasa a RF-07.04/.05/.07/.11. Todas las citas RF/RNF de los entregables existen en el T-12. El SD5 de 32969e4 parece cubrir varios RF que el T-12 aún marca parciales por el SD5 (RF-01.08/.11, RF-02.0x, RF-04.01/.03, RF-11.05, cobranza): revisar. Sin commit.

## Estado vigente — 10 de octubre de 2026 (noche): RT-16.14 y RT-08.04 en Cumple

Informe 2 reprogramado al lunes 12-10-2026 (SD1–9 y 13). Por instrucción del usuario, sólo Markdown en rama-md, sin commit. RT-16.14 (Deseable en BTT; el Caso cap. 15 usa el mismo código para firma/POD): SD4 4.1.3.4 agrega motor de reglas sobre Symfony ExpressionLanguage (evaluación en ejecución sin compilar, variables declaradas por punto de decisión, versión en el registro de parámetros, aprobación de segundo perfil, auditoría con regla/versión/resultado); la frase de RT-16.04 dice ahora «nuevos puntos de decisión» en vez de «nuevas reglas»; referencia Symfony (s. f.). RT-08.04: acotado a la sección 8.1 de BTT; SD4 4.2.1.2 y T-11 declaran dos circuitos por gabinete (PDU A/B en Talca; UPS + circuito directo en borde y piso), segunda fuente del switch de acceso y gateway IoT en circuito distinto, PDU A/B en el borde de Concepción y fila nueva «Conmutador de transferencia de gabinete» (4: Concepción y cross-docking) para Starlink y ONT/router LTE; en Talca van al ATS de rack existente. T-12 590/32/23 (B 339/15/20); 9.C sincronizado (casos sin cambio, 1.305). Planilla SD9 Datos_Base C42–C44 queda en 337/17/20 (no editada). LaTeX de T-12 y SD4 queda desfasado. Validación de numeración: T-12 Parte A y SD3-Anexos tienen los mismos 271 IDs; el catálogo consolidado no tiene RF-07.01 y el SD3 corrió la épica 7 (RF-07.02–07.11 → RF-07.01–07.10); la fila RF-07.11 «No cumple» (T-12 y Tabla 3.A.3a) es residuo de la numeración original y equivale a RF-07.10 «Cumple»: pendiente de decisión. Textos T-12 ≠ Tabla 3.A.1 en RF-03.11 y RF-03.12 (T-12 más estricto: bloquea y notifica), y redacción distinta pero equivalente en RF-18.01 y RNF-23.04. RF-18.03/RT-16.23 (apertura) los levanta el usuario. Propuestos sin aplicar: RNF-21.02/RT-21.02 (JP de Operación como gerente de servicio, T-14 cuenta 8.1) y RNF-21.07/RT-21.16 (traslados N2/N3).

## Estado vigente — 10 de octubre de 2026 (noche): LaTeX de SD1–SD3 alineado con el MD

Por instrucción del usuario, el MD es la fuente y el LaTeX se alineó con él en worktrees separados (`../LafroX-sd1-latex`, `../LafroX-sd2-latex` y `../LafroX-sd3-latex`, ramas locales `LafroX-Subdoc{1,2,3}-LateX` desde origin). No se tocó LaTeX en rama-md. Informe de diferencias: `Revision/revision_md_vs_latex_SD1-SD3.md`.

- El T-12 LaTeX se regeneró completo desde el MD: 5 columnas, escala Cumple/Parcial/No cumple y longtable apaisada (217 p.).
- SD1, SD2 y SD3 (cuerpo y anexos) recibieron los párrafos, filas y tablas del MD: 36 filas RNF, la Tabla 3.A.4a, S-42 a S-44 y las declaraciones de IA.
- Correcciones al MD: referencias LafroX 2026a/2026b en el SD1 (incluye el SD9), autor en la cita (2026c, anexo B.2) y orden de Referencias del SD2, párrafo partido del SD2 y residuos `|}` en dos filas del SD3-Anexos.
- Todo compila. La comparación final solo deja diferencias de maquetación.
- Pendientes: decidir sobre `LAFROX-Subdocumento1-Anexos` (solo existe en LaTeX); RF-03.11 y RF-03.12 difieren entre el T-12 MD y la Tabla 3.A.1; 28 celdas «Origen» truncadas («).») en el SD3-Anexos, presentes en ambos formatos.
- Commit y push en las 4 ramas: rama-md (incluye RT-16.14 y RT-08.04 de la sesión paralela) y LafroX-Subdoc{1,2,3}-LateX. El T-12 LaTeX se regeneró con esos dos cambios. Si el T-12 MD vuelve a cambiar, hay que regenerar su LaTeX.

# CONTEXTO DE SESIÓN

## Estado vigente — 10 de octubre de 2026: correcciones Markdown del SD9 tras revisión

Por instrucción del usuario se corrigieron bloqueos del Subdocumento 9 sólo en Markdown y sin commit. Archivos editados: `09_plan_calidad/LAFROX-Subdocumento9.md`, `09_plan_calidad/LAFROX-Subdocumento9-Anexos.md`, `09_plan_calidad/LAFROX-Formulario-T-13.md`, más registro `odd/tasks/sd9-quality-fix.md` y esta entrada. No se tocaron `.drawio`, `.xlsx`, PDF ni LaTeX. Incidente controlado: un escritor delegado vació accidentalmente `LAFROX-Subdocumento9.md`; se restauró inmediatamente desde `HEAD` antes de aplicar cambios, con worktree inicial limpio, sin pérdida de cambios del usuario.

Cambios aplicados: H6/H11 ya no se describen como primer paso a producción; H7/H12 quedan como pasos contractuales del Formulario E-25 y las repeticiones de intrusión/resiliencia/carga se declaran trabajo de certificación de cierre, no materialización de R8-07. ISO/IEC 25012 ya no se presenta como fuente de 16 indicadores con umbrales; el Anexo 9.A agrega Tabla 9.A.2 con completitud, exactitud y consistencia para migración/marcha blanca/operación, y T-13 incluye esos criterios en migración. Perfil operacional y usabilidad incorporan lluvia, >34 °C, sol directo, una mano y métricas por perfil del RT-13.04. Complejidad cognitiva PHP pasa de PHPMD a PhpMetrics. El calendario SD9/T-13 mueve resiliencia a meses 23/29/35/41/47/53 y DR a 24/30/36/42/48/54 para cubrir el primer semestre de Operación; queda pendiente propagar si se desea plena coherencia con T-14/planilla/figuras draw.io. `git diff --check` OK en archivos editados. Grep sin residuos de «primer paso a Producción», «Capítulo 11», «Figura 7.4», meses antiguos 26/32 y 27/33, ni sobreafirmación de ISO 25012. Persisten `[[REVISIÓN HUMANA]]` como bloqueo humano real; no se completaron.

## Estado vigente — 10 de octubre de 2026 (noche): SD4 Markdown alineado con LaTeX

Por instrucción del usuario, los tres Markdown de `04_arquitectura/` recibieron la redacción pulida del LaTeX de `subdoc-4` (8c3913b) mediante fusión en tres vías (base = MD `df021b9`; se descartaron artefactos del conversor: enlaces de figuras, numeración, prefijo «l» del T-11, restos de capítulo). Entran ~80 párrafos en presente y frases cortas, la corrección 4.2.6.6 del Anexo 4-P, el retiro de nombres de tablas del SD5 (`mae_producto`, `cal_regla_termica`, `env_movimiento`) y las páginas de Bases en el párrafo de despliegue. Cinco conflictos resueltos a favor del contenido más nuevo del MD con la redacción del LaTeX: firma por acto (4.1.17), cambio de emergencia ante congelamiento (4.2.4.1.4) y filas del T-11 (DL20 E-2468, ARK-1251, termógrafo ELA, estación con softphone). La Figura 17 TikZ sigue sólo en LaTeX. Commit `fd26905`. Luego, el contenido del MD posterior a `df021b9` se trasladó al LaTeX en `subdoc-4` `ca84689` (FQDN, TLS 1.3, INT-11, trazas `aws/spans`, firma por acto, termógrafo ELA, baterías S-44, cambio de emergencia, autoescalado, RPO de diseño, NOC/SOC, ARK-1251, T-11 y referencias); PDF recompilados sin referencias indefinidas. La conversión del LaTeX coincide con el MD salvo artefactos del conversor y la Figura 17 TikZ, que sólo existe en LaTeX. Las figuras PNG físicas aún muestran ARK-2250 y Onset CX450 (las edita el usuario en draw.io).

## Estado vigente — 10 de octubre de 2026 (tarde): validación del informe integral

`Revision/validacion_revision_integral.md` valida `Revision/revision_integral_inconsistencias.md` contra `0896cae` (= árbol de trabajo; ningún .md cambió durante la validación). Resultado: 14 fichas vigentes, 3 parciales (RI-01: sólo RT-21.02/21.16 siguen No cumple; RI-06: hoy 15 diferencias T-12/9.C, 582/40/23, regla 9.C.1 daría 1.305 casos, 613 con prueba, 32 sin ella; RI-13: residuo «tercero con limitación de protocolo» en SD4-A 4-R), 2 superadas (RI-09 SOC propio; RI-16 acuse 30 min en SD4 4.1.17.1). RI-05, RI-07 y RI-13 pasan a corrección documental (la decisión ya existe); RI-11 sube a alta por §7.1 a) (Figura 1.1 del SD1 con leyenda sin imagen; 14 destinos SD2/SD3 ausentes). Nuevo N-01: predecesoras por cuenta de la Tabla 6.1 del T-15 incluyen paquetes de etapas posteriores (11 celdas); el Anexo 7.B tiene las dependencias precisas. Barridos sin hallazgo: 38 títulos §11, 1.167 referencias a secciones, anexos/tablas A.n, IDs, fechas H1–H10, meses INN, P/I de 32 riesgos, cifras obsoletas. Los seis frentes Codex fallaron por límite de uso (reinicio 22:01); prompts en el scratchpad de la sesión. No se editaron entregables ni el informe validado; sin commit.

## Estado vigente — 10 de octubre de 2026 (tarde): mini-PC y tableros

Aplicado por instrucción del usuario: mini-PC ARK-2250L (descontinuado) reemplazado por Advantech ARK-1251 con Core Ultra 5-125U según ficha oficial (12–28 VDC, DIN, 2 NVMe M.2, 3 LAN, -20 a 60 °C con 0,7 m/s, máx. 59,44 W); Tabla A.35 del SD4-Anexos recalculada (cross-docking 365 W, 438 W, 0,46 kVA, 61 %; UPS requerida 0,58 kVA) y fila del gabinete del T-11. SD4 4.1.3.8: tablero del mandante con estado del servicio (CloudWatch, un minuto) e indicadores de negocio con latencias de RT-05.29, exportables en CSV y Excel. T-12: RT-08.01, RT-14.02 y RF-16.02 en Cumple; 585/37/23. RT-08.04 queda parcial (decisión). Huella de carbono y certificaciones en espera. Luego: RT-13.04 en Cumple con la nueva Tabla 3.A.4a del SD3-Anexos (preparador, recepción, preventista y conductor: tiempo, pasos, error ≤ 5 % y aprendizaje), métrica 9A-13 del SD9 y fila de 9.C alineadas; T-12 586/36/23. Pendientes: RF-07.11/RF-07.10 (cambio del SD5 especificado al usuario, lo aplica su compañero; luego SD3 3.A.3a, SD4 M7, T-12 y SD9), firma: aplicada. SD4 4.1.17 declara la firma por acto (guía con firma avanzada del CLIENTE por el ERP y verificación de firma y vigencia del certificado; acuse electrónico del receptor habilitado verificado igual, coherente con Anexo 4-U; firma electrónica simple del receptor persona natural, Ley 19.799 art. 2 letra f, como evidencia; V-18 sigue abierta); Ley 19.799 agregada a Referencias del SD4; RF-18.01 y RT-16.17 en Cumple. SD9 sincronizado con el T-12 sin diferencias: 9.C con RT-21.08, RT-21.13 y RT-23.05–23.10 con prueba (8 casos), RT 354/20, total 613 con prueba y 32 sin prueba (23 No cumple + 9 absorbidos), 1.305 casos; SD9 9.2.3 y T-13 actualizados (1.044 automatizados, 261 manuales ≈ 65 HH, regresión 8,7 h / 4,35 h). Por autorización expresa del usuario se alineó la planilla LafroX-Calculos-SD9.xlsx (respaldo previo en el scratchpad): Datos_Base C42–C44 = 337/17/20 (RT Cumple/parcial/No cumple) y comprobación de Casos_Prueba a 1.305 casos, 1.044 automatizados y 261 manuales; recalculado a mano: 8,7 h, 4,35 h y 65,25 HH; Excel recalcula al abrir. T-12 588/34/23. Sin commit.

## Estado vigente — cierre focal T-12, 10 de octubre de 2026

## Estado vigente — cierre focal T-12, 10 de octubre de 2026

Usuario autorizó gpt-6.1-sol y ejecución directa sin delegación ni espera de Engram; rama comprobada rama-md, sin commit. Se editaron únicamente SD4 cuerpo/anexos, SD3 cuerpo y T-12, más registro odd/tasks/cierre-brechas-t12.md y este contexto. Preservados todos los cambios previos. Nueve filas pasan a Cumple: RT-03.08, RT-04.13, RT-14.08, RT-02.10, RNF-19.02, RT-16.24, RT-21.08, RT-21.13 y RNF-12.03. Costos sólo remitidos a Oferta Económica, BA art. 50.2. T-12 conserva 645 IDs, todas las descripciones y filas ajenas; no se editaron conteos. Revisión de Claude posterior: alineados los proveedores de INT-11 (SES, SNS, AWS End User Messaging Social) en SD4 4.1 (mensajería), tabla de integraciones del Anexo 4-H y T-11 «Dependencias de salida»; borrados los registros temporales .codex-flow/live de esta sesión. Estado T-12: 582 Cumple, 40 parciales, 23 No cumple. Pendientes por grupo: 15 RF del SD5 (otra persona); video y prototipo (16, propuesta final 25-11); 9 deseables; decisiones con arrastre a conteos SD3/SD9 (RT-21.02/RNF-21.02, RT-21.16/RNF-21.07, RF-07.11); datos de empresa (RT-15.02, 15.07, 15.08, 21.03, 23.03); huella de carbono (RT-15.03/15.04, en espera); decisiones técnicas (RT-08.01 mini-PC, RT-08.04, RT-13.04 umbrales, RT-14.02/RF-16.02 tiempo real, RF-18.01/RT-16.17 firma avanzada, RNF-21.08/RT-21.19 separar bolsa evolutiva de 4.608 HH, RT-16.23/RF-18.03 apertura SMS no informable). SD9 9.C: RT-23.05–23.10 siguen «No cumple, sin prueba» frente a «Cumple» del T-12.

Fuentes AWS citadas en Referencias SD4 s. f.-f a s. f.-n: trazas CloudWatch Transaction Search en aws/spans, 30 días configurados mediante PutRetentionPolicy, sin archivado adicional; escalado ECS con métricas SQS de un minuto, consumidor >60 s de edad y trabajos >100 mensajes visibles por cola, techo cuatro sin alterar T-11. Proveedores INT-11: SES, SNS/SMS, End User Messaging Social/WhatsApp y portal LafroX Angular/Laravel en Fargate. Apertura condicionada a evento Open, read o acceso autenticado al aviso; SMS no informa apertura, WhatsApp requiere confirmaciones y SES depende del píxel. Acuse comercial en 30 min con ASN de la misma guía sobre INT-08 existente, distinto del MDN y del acuse tributario.

Cinco filas siguen parciales: RT-16.23/RF-18.03 por apertura no informada en todos los mensajes; RNF-21.08/RT-21.19 porque 8.2.1 sólo asigna 4.608 HH DES conjuntas para correctivo/evolutivo (4.608 ÷ 36 × 12 = 1.536 HH anuales conjuntas, NO bolsa evolutiva exclusiva); RT-13.04 por máximo de pasos de transacción y error/aprendizaje de otros perfiles. RNF-05.03 y 9A-13 sólo cubren preparación, ≤2 h y ≤5 % en 20 líneas; RT-25.01 limita acceso, no ejecución. No se repartieron horas ni inventaron umbrales adicionales.

Pendiente SD5, fuera del alcance: registrar not_intento.apertura_fecha (UTC, nullable) y apertura_estado (INFORMADA/NO_INFORMADA/NO_SOPORTADA), con identificación del evento de proveedor para correlación; no equiparar CONFIRMADO con lectura. SD9/9.C queda sin sincronizar por exclusión expresa; no arrastrar conteos ni planillas. SD5, SD9, T-11, T-14, T-15, imágenes y planillas mantienen sus huellas previas. Finales de línea preservados: dueños CRLF y T-12 LF preexistente; contexto previo mixto preservado. git diff --check de los cuatro entregables: salida 0, sólo aviso Git de conversión futura LF→CRLF del T-12. No se acreditan ensayos ni revisión humana. Engram rechazó la mutación por identidad de sesión no confirmada; espejo pendiente.


## Estado vigente — 10 de octubre de 2026: informe integral de inconsistencias, RI-02/RI-03

Por autorización específica del usuario se creó `Revision/revision_integral_inconsistencias.md`, sin aplicar sus soluciones a entregables, sin commit/publicación ni derivados. Cubre 31 documentos SD1–9/13 (10 cuerpos, 9 anexos, 12 formularios) y excluye declaraciones de IA. Contiene 19 grupos: 10 altos, 8 medios, 1 bajo; complejidad 8 alta, 9 media, 2 baja; seis decisiones separadas, propuestas no aceptadas. P01–P06 y la dependencia gráfica se revalidaron; capacitación de Concepción distingue simultaneidad y población total. Las figuras PDF aceptadas de SD4 no son ausencias.

Base: `rama-md`, HEAD `113837d63b9afe6dbbebf489c3941668aebea592` más bytes actuales. Se preservaron cambios externos en SD4/T11/T12 y la entrada de contexto inmediatamente posterior a ésta; no se atribuye autoría. Tras esos cambios, T12/9.C tienen 645 IDs cada uno y 20 diferencias de estado. Conteos actuales T12 RF161/19/1, RNF81/7/2, RT319/33/22; la regla de 9.C deriva 1.303 casos, 611 IDs con prueba propia y 34 sin ella. El informe registra hashes/corte temporal para no confundir HEAD y worktree.

Comprobaciones del escritor: 19 fichas/19 filas de índice/19 IDs únicos; 35 enlaces de fuentes existentes; `git diff --check` salida 0 y control del informe nuevo sin whitespace final; cinco huellas focales estables en lecturas finales. Sólo escribió informe, tarea `odd/tasks/revision-integral-inconsistencias.md` y esta entrada. RI-02 y RI-03 documental independiente completadas. El verificador confirmó fichas/citas altas/normas, comparación de IDs/estados, cálculos 96/115,2/76,8/179,2 HH, población de Concepción sin inferir 180, UTF-8 y controles. Se corrigió el criterio térmico provisional (rango de la ficha con parámetros aún no aprobados), se explicitó BTT:95 sin exclusión automática, se delimitó lectura/muestreo de SD4 y se justificó RI-10 alta como afectación potencial, no pérdida demostrada; se pulieron espacios en prosa. No se acredita compilación, ensayos, simulación reejecutada, certificados/sitio externos ni forma PDF ni aprobación técnica. Engram y revisión nativa no disponibles; espejo pendiente.

## Estado vigente — 10 de octubre de 2026: NOC/SOC en el Centro de Operaciones de Valparaíso

Decisión del usuario: NOC, SOC y mesa en el Centro de Operaciones de LafroX en Valparaíso (Av. Brasil 2241, domicilio ya declarado en SD1/T-6), fuera de los sitios de Puelche, con continuidad en trabajo remoto por Verified Access. SOC propio (no subcontratado): analistas contratados antes del mes 13 bajo el Encargado de Seguridad; opera meses 13–56; NOC con la división NOC 24×7 (puente meses 16–20, Operación 21–56). Alineados SD1 1.1/1.2, SD4-Anexos 4-W.7, T-15 (sección 4 nota C, 4.x nivelación, 5.7), T-14 8.1.5 (título y ventana corregidos de «36 meses» a meses 13–56; las figuras .drawio de la EDT pueden conservar el título anterior y no se editaron), SD7 7.2, SD6 6.1.3, SD6-Anexos, T-9 y resúmenes SD6/T-9. T-12: RT-11.17, RT-21.01 y RNF-21.01 en Cumple; estado 571 Cumple, 49 parciales, 25 No cumple (A 247/21/3; B 324/28/22). Después, por instrucción del usuario («no inventar nada»): SD4 4.2.1.2 declara autonomía y condiciones de uso por terminal sólo con datos de fichas oficiales de Zebra; MC9400 estándar con 22 baterías de repuesto y 5 cargadores de cuatro baterías; EC55 con batería extendida de 4.180 mAh, 450 nits y sin afirmar lectura al sol ni guantes (se comprueban en aceptación); ZQ620 Plus sólo IP54 confirmado y caída mínima de 1,5 m exigida en la compra; PAX sin rango térmico no verificado; reposición de baterías bajo 80 % con Zebra DNA. RT-08.11 en Cumple; estado T-12 572/48/25 (B 325/27/22). Luego: EC55 se mantiene (decisión del usuario). Nuevo supuesto S-44 (turnos de día: 65 por turno al inicio, 73 en el año 3; todos los MC9400 estándar trabajan de noche según Anexo 4-W.3): 81 baterías de repuesto en el año 3 (Talca 51, Concepción 30), 21 cargadores de cuatro baterías y 40 cunas de carga; SD3 registra 44 supuestos. PAX con cargador de vehículo USB-C; ZQ620 Plus y PAX agregados a la lista de autonomía del SD4 4.2.1.2. RT-17.07 en Cumple con consumo máximo comprometido de 80 % por turno medido en aceptación (SD4 4.2.6.7). Revisión Codex: corrigió el cálculo inicial de 42 baterías (mezcla de horizontes); se sincronizaron 26 estados del SD9 Anexo 9.C con el T-12 y el resumen del SD4 (cambio de emergencia). Queda fuera: RT-23.05–23.10 figuran «No cumple, sin prueba» en 9.C pero «Cumple» en el T-12; alinearlos agrega 6 casos de inspección (1.297 → 1.303) y arrastra cifras del SD9 y su planilla. Codex también marcó como cumplimiento discutible TLS (excepción del ERP), RT-11.04 (plazo excedido por decisión del CLIENTE), RPO fuera de base de diseño y FQDN con `<dominio>`: decisiones ya tomadas por el usuario. T-12: 573/47/25.

## Estado vigente — 10 de octubre de 2026: cierre parcial de brechas del T-12 (seguridad, DR, hardware y termógrafo)

Por instrucción del usuario, sólo Markdown en `rama-md`, sin commit. SD4: Tabla 19 con columna FQDN (`<dominio>` = dominio del CLIENTE a confirmar); 4.3.2.4 deja la triple falla con destrucción del sitio fuera de la base de diseño (R8-05); TLS 1.3 en entradas y entre componentes (CloudFront TLSv1.3_2025, AES-GCM, HSTS con preload, alerta ACM 45 días; el ERP de 2017 sólo con TLS 1.2 como excepción si el levantamiento lo exige, porque sus interfaces no están documentadas: Caso cap. 5, p. 10) en 4.1.3.7 y Anexo 4-R; F-03 declara el servidor del ERP como activo del CLIENTE fuera de la solución; 4.2.4.1.4: ante congelamiento, cambio de emergencia solicitado el mismo día y, sin autorización, contención con aceptación del riesgo por el CLIENTE. Termógrafo B-03 cambiado de Onset CX450 (sin API/SDK público) a ELA Blue PUCK T EN12830 (EN 12830:2018, −40 a +85 °C, ±0,5 °C sobre 0 y ±1 °C bajo 0, 4.000 lecturas con CRC16, IP68, batería interna hasta 10 años, comandos DATALOGGER_START/READ_DATA documentados): el terminal lee la temperatura difundida, alerta en cabina y reenvía por celular; SD4 4.1.3.2, 4.1.7, 4.2.1.2 (EN 13486 en la compra), 4.2.2.6 y SD13 13.3 alineados. T-11: fichas IP/caída, MC9400 estándar 7.000 mAh, Freezer 2,1 m, TC58e batería extendida 7.000 mAh y 1,8 m sobre baldosa, DL20 con Xeon E-2468 y 4×1 GbE, normas TIA, softphone, gestión de dispositivos y costo unitario remitido a la Oferta Económica. T-12: 568 Cumple, 52 parciales, 25 No cumple (A 246/22/3; B 322/30/22). RT-06.12 queda parcial por decisión del usuario. Abiertos: ubicación de SOC/NOC (RT-11.17, RT-21.01, RNF-21.01), procesador exacto del mini-PC (ARK-2250L descontinuado; alternativa ARK-1251 cambia consumo 45→≈62 W y el cálculo de UPS del Anexo 4-W), RT-08.04, RT-08.11, termógrafo pendiente de cotejar exactitud con ficha oficial de ELA. El SD9 Anexo 9.C y sus conteos (RT 304/42/28) siguen desfasados del T-12. Video y prototipo quedan No cumple hasta la propuesta final del 25-11-2026. El SD5 lo revisa otra persona; huella de carbono y pendientes sueltos en espera.

## Estado vigente — 10 de octubre de 2026: informe de pendientes interdocumentales CD-03

Por aclaración expresa del usuario, `Revision/revision_consistencia_documental.md` se reescribe como informe actual de coherencia ENTRE documentos, no auditoría de cumplimiento del T-12. Quedan seis grupos P01–P06: innovaciones/H4; H12 con acta, cierre dependiente y HH; cobranza por preventistas; reconexión dentro/fuera de cámara; conjuntos térmicos y réplica regional; cobertura de capacitación de Concepción. Las catorce figuras SD2/SD3 ausentes forman D01, dependencia gráfica separada, no contradicción semántica. No se lista RNF-12.03 parcial como pendiente de coherencia. Se retiran tablas históricas de defectos corregidos; la historia sigue en Git y entradas anteriores de este contexto. CD-01 conserva su cierre en 8463b7b/9c386e1. CD-03 pendiente de readback del padre; no se alteran originales. El usuario solicita commit y push al terminar; los ejecuta el padre después de comprobar. Engram no disponible, espejo pendiente.

## Cierre vigente — 10 de octubre de 2026: consistencia documental CD-01

Correcciones verificadas independientemente y registradas en 8463b7b (28 Markdown). La revisión focal confirmó la independencia del montaje de Concepción y septiembre como fin de construcción/QA de módulos E1, sin mover integración de octubre. CD-01 cerrada; CD-02 y siete asuntos de decisión permanecen abiertos, empezando por innovaciones/H4. Detalle y comprobaciones en odd/tasks/consistencia-documental.md y Revision/revision_consistencia_documental.md. Sin publicación remota. Engram y revisión nativa no disponibles; no se afirma coherencia total ni cierre de figuras, firmas o ensayos.



## Estado vigente — 10 de octubre de 2026: consistencia documental CD-01 aplicada, pendiente de verificación independiente

Autorización actual: revisar y aplicar correcciones simples/medias del informe de consistencia en `rama-md`, sólo Markdown; sin publicación remota. Trabajo y restricciones recuperables en `odd/tasks/consistencia-documental.md`. Se alinearon unidades/ancla SD3, A.31/A.36 y 12,34 TPS SD5, extremos agregados 3.4/3.6 y construcción junio–septiembre, adquisiciones SD6/T-9 con decisiones previas de sala/obra civil/cinco Starlink, C-05 por período e I-04A desde mes 24 con meta mes 36. En 3.B se revisaron 86 filas activas y sólo se cambiaron 36 métodos; no requisitos ni estados. Se sincronizaron resúmenes existentes; no existe guía separada de Anexos SD6 y no se creó una copia auxiliar. Informe: tabla vigente más registro inicial explícitamente histórico, con descarte del falso conteo siete/seis y reconocimiento de cobertura/T-12 ya alineados.

Pendientes con decisión: innovaciones/H4; H12 y reparto HH; cobranza RF-07.10/11; copia térmica interregional; población de capacitación de Concepción; ubicación de catorce figuras SD2/SD3 y compromiso de reconexión interior de cámara. El acuse comercial RNF-12.03 sigue parcial, sin evidencia del plazo/aviso. No se llenaron revisiones humanas ni se acreditaron pruebas. La verificación independiente pidió una corrección acotada: recepción de sala como predecesora sólo de los racks de Talca, Concepción paralelo; QA por módulo agosto–septiembre y R8-11/E8-01 junio–septiembre. Se aplicó sin cambiar fechas ni certificación/integración de octubre. CD-01 permanece sin marcar hasta comprobar esos ajustes; sin commit. Engram y gentle-ai no disponibles: espejo pendiente y sin aprobación nativa. Esta nota no resuelve los pendientes del SD9 de la entrada siguiente.

## Estado vigente — 10 de octubre de 2026: revisión v3 del SD9 y 15 correcciones sin decisión aplicadas

Revisión `Revision/revision_comision_informe2_SD9_v3.md` (42 preguntas de comisión: 16 respondidas, 26 al plan; plan PC-01 a PC-32). Puntaje 0/100 por celdas `[[REVISIÓN HUMANA]]`; contenido 20 antes de corregir, por contradicciones nuevas (H02–H12). Por instrucción del usuario se aplicaron los 15 ítems sin decisión: PC-02, 03, 04, 07, 14, 15, 16, 17, 21, 22, 23, 25, 26, 30 y 31. Sin commit; se editaron también tres .drawio y la planilla, por autorización de esos ítems.

- **Cifras vigentes del SD9:** 1.297 casos (846 + 346 + 105 de contrato, 7 por integración × 15; antes 1.282); ~1.038 automatizados; regresión 8,65 h con un ejecutor y 4,33 h con dos; 259 manuales, ~65 HH. Costo de calidad: prevención 4.224 HH y evaluación 6.624 HH (total 10.848; 3.10.2.4 pasa a prevención). Productividad 6,4 HH/día (T-15 5.1). Reversión operativa E2 ≤ 40 min (T-18 6.4).
- **Anexo 9.C** regenerado desde el T-12: 0 diferencias en 645 IDs (RF 159/21/1, RNF 78/10/2, RT 304/42/28); 259/9/3 se mantiene.
- **Referencias:** «Capítulo 11» → paquetes 8.2.4 y 8.4.1 del T-14; matriz de cobertura → SD7 Tabla 7.2 y Figura 7.16. T-12: 13 RT remiten a SD9/T-13/T-17. McCabe (1976), Martin (2003), W3C (2023), CMMI (2023) e ISO/IEC/IEEE 29119-3:2021 agregados.
- **Contenido:** carga anual en Preproducción (Tabla 9.9, Fig. 9.4); G6 en Tabla 9.5 y Fig. 9.3; acta de la Contraparte Técnica como condición adicional de G5, sin levantar fallas ni defectos críticos/altos; p95 de navegación 1 s, transacción de terreno 3 s, búsqueda compuesta 3 s (RF-17.11 ≤ 2 s) e informe estándar 30 s en 9A-05/06/07 (siguen 29 métricas); resolución determinista de conflictos de stock (SD4 Anexo 4-K, Tabla A.12) en T-13 T13.3 y 9A-19; T-13 3.8.2/3.8.3 = 21-10 → 17-11-2027; siglas definidas en primer uso.
- **Figuras:** Fig. 9.9 (Mermaid y .drawio) con resiliencia sep-29/sep-30 (días 26–30) y DR oct-29/oct-30; Fig. 9.7 .drawio con el nombre completo de 3.4.4.
- **Formato:** declaración de IA con una fila por anexo; celdas `[[REVISIÓN HUMANA]]` pasan de 13 a 16. Índices en Anexos, T-13 y T-17.
- **Planilla `LafroX-Calculos-SD9.xlsx`:** alineada (Casos_Prueba, HH_Calidad, COQ, Datos_Base fila 51, Calendario, ISO25010); respaldo en el scratchpad; sin recálculo (no hay LibreOffice; Excel recalcula al abrir).

Pendientes nuevos detectados por la planilla: con 6,4 HH/día el mes 10 excede la capacidad de evaluadores (845,3 HH frente a 806,4); el T-15 usa 20 días/mes (128 HH) y el SD9 21; el mes 17 tiene evaluadores sin paquete de prueba ni justificación (85 HH). Pendientes con decisión del equipo: PC-01, 05, 06, 08–13, 18–20, 24, 27–29 y 32 de la v3; páginas de citas (requiere PDF). Esta nota supersede la lista de pendientes de la entrada siguiente.

## Estado vigente — 9 de octubre de 2026: pendientes cruzados 1–9 cerrados y tercera revisión del SD9

Por instrucción del usuario se cerraron los pendientes cruzados listados en la revisión del SD9. Sólo Markdown, en `rama-md`; sin commit.

- **SD1:** 1.3.2 presenta la intrusión semestral como política corporativa más estricta que incluye el mínimo de RT-11.20 (anual y antes de cada paso a producción). 1.4 declara la renovación de CMMI-DEV N3 junto con la línea base H1; mientras no se acredite, no se invoca el nivel y rigen los procesos ISO 9001 (coherente con SD9 9.1.2).
- **SD3/Anexos/T-12:** el T-12 se describe con sus cinco columnas; prueba en SD9 Anexo 9.C y criterio en T-17 (SD3 3.2 y Anexo 3.J). RNF-06.02 (→ RT-03.11 y S-24), RNF-06.03 (alias de RT-03.12, verificado con RNF-02.01), RNF-11.03 (→ RF-11.07) y RNF-11.04 (→ RT-05.29) siguen «Cumple», con remisión al requisito que los absorbe. RNF-14.07 se verifica con SAST en G2 y OWASP ZAP en G4.
- **Conteos vigentes:** catálogo de 261 requerimientos (175 RF + 86 RNF; 56/162/43). Se ofertan 259, porque RNF-21.02 y RNF-21.07 (Alta) figuran «No cumple»; lo ofertado se distribuye en 56/160/43 y el catálogo RNF ofertado es de 84. T-12 Parte A = 271 filas = 261 + 10 alias/absorbidas (181 RF, 90 RNF). Conciliación con SD9: 271 = 259 con prueba propia + 9 absorbidas + 3 «No cumple» (RF-07.11, RNF-21.02, RNF-21.07). «Ofertados» ya no se usa para los 261.
- **T-14:** 3.8.7, 3.9.1 y 3.9.6 separan mes de ejecución y mes del hito E-25 (10 → H5 mes 12; 16 → H9 mes 17; 16–17 → H10 mes 18).
- **SD6 6.1.3:** se agregó el refuerzo de evaluadores (hasta 16 por día, meses 9–12 y 16–18), con los meses 11, 12 y 18 reservados a subsanaciones, como SD9 9.3.2.
- **T-15 3.7.3:** la carga de saldos del WMS de Talca en diciembre de 2027 es ensayo en Preproducción; Producción sólo se interviene en el corte 3.7.5 (desde 03-01-2028). Sin conflicto con el congelamiento.
- **SD9/T-13/T-17:** conciliación 259 + 9 + 3 en SD9 9.x (línea ~298); R18 definido en su primer uso en T-17 (hoja H7); septiembre ya no se declara evitado: las resiliencias de los meses 32 y 44 (sep-2029 y sep-2030) se ejecutan entre los días 26 y 30, fuera del congelamiento del 1 al 25 (SD9 ~508/520; T-13 110 y 156); errata de puntuación en SD9-Anexos 130.
- **Revisión:** `Revision/revision_comision_informe2_SD9_v2.md` (la anterior se conserva): 0/100 por las 13 celdas `[[REVISIÓN HUMANA]]` (§7.1 d); contenido sin esa causal, 80 en la escala discreta 0/20/40/60/80/100 (el «70» anterior no es un valor válido). Sus hallazgos 2–5 quedaron corregidos después de emitirla.

Pendientes reales: 13 celdas `[[REVISIÓN HUMANA]]` (sólo un integrante); páginas de 16 de 24 citas a las Bases (requiere PDF final); verificación visual de las figuras .drawio frente al Markdown. El usuario descartó fijar días exactos de las pruebas semestrales. Esta nota supersede la lista de pendientes de la entrada siguiente.

## Estado vigente — 9 de octubre de 2026: coherencia cruzada SD9 aplicada

Por autorización posterior del usuario se aplicaron cambios fuera del SD9 para alinear los documentos relacionados con las correcciones del plan de calidad. Se editaron sólo Markdown.

- **T-14:** paquete 1.5.2 usa cobertura unitaria global ≥80 % y lógica de negocio ≥70 %; 8.1.3 fija DR en meses 27, 33, 39, 45, 51 y 54; 8.2.2 fija intrusión en 28, 40 y 52 y resiliencia en 26, 32, 38, 44, 50 y 55.
- **T-15:** la certificación E1 del resumen inicia el 21-10-2027 y la E2 el 19-05-2028; el texto de 5.2 y la Tabla 6.1 hacen depender 3.8.4/3.8.5/3.8.6/3.8.8 de 3.8.1 y 3.9.3/3.9.4/3.9.5/3.9.7 de 3.9.1. La aceptación 3.9.2 queda 27-05 a 31-05.
- **SD4/T-11/Anexo 4-P:** se incorporaron las herramientas del SD9 al pipeline e inventario (PCOV, JUnit 5, Kover, Jest, PHPMD, PHPCPD, PhpMetrics, deptrac, detekt, ktlint, ESLint, OWASP ZAP, axe-core, k6, AWS Fault Injection Service, Amazon Inspector/ECR). SD4 explicita que cualquier incumplimiento WCAG 2.2 A/AA confirmado bloquea promoción/aceptación.
- **SD6/T-10/Resumen SD6:** cobertura actualizada a lógica de negocio ≥70 % y unitaria global ≥80 %; T-10 incorpora herramientas del pipeline.
- **Revisión SD9:** `Revision/revision_comision_informe2_SD9.md` se actualizó con diagnóstico de contenido 70 sin causal §7.1, seguimiento de correcciones cruzadas y pendientes reales.

Verificación: `git diff --check` sin errores (sólo advertencia CRLF futura en `Revision/revision_comision_informe2_SD9.md`), greps dirigidos sin residuos vigentes de la secuencia/cobertura anteriores salvo archivos históricos (`Revision/revision_comision_informe2.md`, `compct/plan_SD9.md` y estados antiguos del propio contexto), y conteo de archivos. Pendientes: 13 celdas `[[REVISIÓN HUMANA]]`; páginas de citas en PDF; fecha/día exacto si se quiere probar separación semestral con precisión diaria; asuntos no abordados de SD1/SD3/T-12/T-14 3.8.7/3.9.1/3.9.6/SD6 6.1.3/T-15 3.7.3 listados en la revisión. Sin commit.

## SD4 — unidad de commit y comprobación de ramas — 11 de octubre de 2026

Actualización por petición posterior: el usuario autorizó pull y push en rama-md y subdoc-4. La simulación de integración terminó sin conflictos; pull de rama-md incorporó siete commits remotos mediante merge 9187d38 y subdoc-4 ya estaba al día. El push de subdoc-4 publicó d42c58a0ca0490698344c995776d2aed08218b62, confirmado por ls-remote. Tras el rechazo inicial del control automático por destino no confirmado, el usuario respondió «utiliza mis credenciales» a la pregunta que identificaba https://github.com/PatricioH315/LafroX.git; se usó la autenticación configurada y el push tuvo éxito. Los tres enlaces de las nuevas figuras del Markdown apuntan ahora a ese commit publicado. La incorporación de archivos remotos de otros subdocumentos, incluidos los diagramas del SD13, corresponde al pull explícitamente pedido; las nuevas ediciones propias siguen siendo Markdown. Se prepara esta unidad de enlaces/contexto para publicar rama-md y verificar la igualdad de HEAD/remoto.

El usuario autorizó comprobar conflictos y crear un commit en rama-md y otro en subdoc-4; no solicitó push. Se conserva el contenido espejo SD4 (1647/1060/111 bloques sin diferencias), 29 figuras, 132 filas IA con Álvaro Catalán y los PDF 201/100/48 páginas ya verificados. Fetch confirma subdoc-4 sin avance remoto y rama-md con siete commits nuevos de otros subdocumentos, sin cambios remotos en SD4. El contexto incorpora ambas historias; se registra únicamente Markdown y se preservan exportaciones, propuestas y archivos de otros subdocumentos. Los nuevos binarios remotos de SD13 no se incorporan a este checkout exclusivamente Markdown. La simulación de integración y el estado de cada commit se verifican con Git.

## SD4 — correcciones de Aclaraciones y único revisor Álvaro Catalán — 11 de octubre de 2026

Autorización directa: aplicar las propuestas de revisión en LaTeX y Markdown como espejos. El usuario confirmó revisión integral y después pidió «quita a alex aravena solo a mi»: las 132 filas IA identifican únicamente a Álvaro Catalán, sin atribuir mediciones ni pruebas ejecutadas. Esta instrucción supersede la selección previa de Alex como revisor; la portada conserva al representante legal corporativo, función distinta.

Realizado en rama-md y subdoc-4, preservando modificaciones previas: seis menciones enumeradas reemplazadas, tres portadas «Caso — Logística», remisiones obsoletas a tablas sustituidas por referencias automáticas, caída de Anexo4-P, cinco referencias AWS agregadas a anexos, duplicación «Anexo Anexo» corregida en Markdown y conversor. Declaración IA ampliada a108secciones+23anexos+T11=132filas. Tres vistas de red independientes y legibles sustituyen la vista comprimida en el cuerpo; original XML/PDF intacto SHA256 912bf7b551a9bd005b9e8f00b39d265faa7ff34221b6934f33cf4ee33b841aac. Figuras actuales29; Talca27, racks28, recinto29. Anexo4-N añade correspondencia de3.4.3–3.4.6; cotejo9subsecciones,12módulos,15actores. T11 incorpora índice y lista de tablas con Referencias navegables.

Controles finales:29activos,340enlacesinternos,132filas con Álvaro, sin marcadores humanos ni caso enumerado en fuentes vigentes y extracción integralPDF; comparación secuencial MD/TeX sin diferencias en1647/1060/111bloques. Compilación final201/100/48páginas, sinreferenciasindefinidas/caracteresfaltantes/cajasdesbordadas. Nueva red medida10,58puntos enPDF; portadas/índices,18páginasIA,3vistasred, caída4-P, bibliografíaAWS, matrizA14p33 yT11Refs revisadosvisualmente; columnaúltimaA14ampliada sinmodificarceldas. Sólo Markdown escrito enrama-md; scripts, figuras, compilación yQA encheckoutLaTeX. Cierre en Revision/cierre_correcciones_SD4_aclaraciones_2026-10-11.md.

Pendientes reales:12citas deBases sinfolio originalverificado, inventario enRevision/citas_Bases_SD4_paginas_pendientes.md (localmente sóloBasesMD); firma real y consolidaciónA6 porresponsable; remisionesT12 porrenumeración fuera deSD4. No se modificaron otros subdocumentos ni se hizo commit/push. Enlaces afiguras enMD sonrepresentación del espejo, no incumplimiento por sí mismos; evaluación visual sóloPDF.

## SD4 — auditoría completa de tablas y reorganización — 11 de octubre de 2026

El usuario autorizó revisar todas las tablas del SD4, convertir explicaciones extensas en punteos o trasladar matrices largas a anexos, sin alterar contenido técnico. Destinos comprobados: rama-md en LafroX-alvaro-md y subdoc-4 en LafroX-rama-latex. Se conservaron las mejoras locales anteriores y los untracked del usuario, incluidos 05/, md para drive/, propuestas y herramientas previas. Sin commit ni push.

Se revisaron las 39 tablas originales del cuerpo, los anexos y T11. Nueve explicativas pasan a punteos (originales 9,10,12,15,16,19,20,36,38). Tres matrices se trasladan: original6 inventario a4-W/A.35; original7 correspondencia a4-N/A.14; original32 dieciséis dimensiones a4-W/A.30. La original8 (distribución numérica) permanece comoTabla6, porque sí compara varias dimensiones sin descripciones extensas. Cuatro cuadros numéricos extraen explicaciones: original22 derivaciones,26 escenarios de enlace,29 acciones de crecimiento,30 fuentes de umbrales. Dos columnas constantes (estrategia/reversión del WMS y techo8Fargate) se eliminan del cuadro y su valor común queda declarado fuera; ningún dato ni condición cambia.

Resultado: 26 tablas técnicas compactas del cuerpo, todas verticales, con máximo cinco columnas, sin columnas totalmente repetidas/vacías y sin continuación entre páginas. Se reserva espacio según tamaño y se impide la división automática de palabras solo dentro de tablas; tipografía institucional9,5pt sin reducción. IA constituye la excepción obligatoria de Aclaraciones7.2:56filas/seiscolumnas, en vertical, finalidades breves y17alcances largos en punteos fuera de las celdas; conserva56marcas de revisión humana sin fabricar revisores. Anexos40tablas yT11su tabla oficial mantienen el detalle permitido por sección5. Fuentes y derivados soloencheckoutLaTeX; la carpeta04_arquitectura de rama-md sigue con sus tres.md.

Verificación final: espejo0diferencias en1568bloques cuerpo,1050anexos y110T11;343enlaces internos válidos;27figuras ySHA912bf7b551a9bd005b9e8f00b39d265faa7ff34221b6934f33cf4ee33b841aac deldiagrama aprobado intactos. CompilaciónLuaLaTeX: cuerpo183p,anexos99p,T11 46p; sin referencias indefinidas, caracteres faltantes ni desbordamientos. Revisadas visualmente las26tablas técnicas, matricestrasladadas, punteosrepresentativos ydeclaraciónIA. La única tabla del cuerpo que continúa esIA27, obligatoria. Se limpiaron puntuación duplicada y menciones genéricas a tablas convertidas; ubicaciones y números actualizados tambiénenresúmenesSD4. Esta verificación eseditorial, no acredita ensayos de carga ni revisiónhumana.

Auditoría de39decisiones enRevision/AUDITORIA_TABLAS_SD4.md y04/revision/AUDITORIA_TABLAS_SD4.md delLaTeX. El preparador deparches puntual ylas imágenesQA propias se trasladaron, sin borrado, aentrega/_build/reorganizar_tablas.py yentrega/_build/qa_tablas_sd4, ignoradosporGit, para no contaminarlaentrega. El auditorread-only04/herramientas/auditar_espejo.py eliminaNeedspace al comparar, puesesúnicamentemaquetación. Pendientesprevios de mediciones y revisiónreal siguen pendientes.

## SD4 — revisión conforme a Aclaraciones y denominación del caso — 11 de octubre de 2026

Petición: analizar y revisar SD4 según Aclaraciones, comprobar la denominación «Caso 02» y mencionar cada observación. Se revisaron los tres Markdown vigentes en rama-md, HEAD 05f1d66708cbb1f524e1bbb294eeec2786fcec88 con cambios locales previos conservados. Informe en Revision/revision_SD4_aclaraciones_2026-10-11.md: seis menciones del caso enumerado (3 cuerpo/2 anexos/1 T11), 56 marcadores humanos, referencias obsoletas a Tablas 28/29/30, caída faltante en Anexo4-P, citas AWS sin entrada en bibliografía de anexos, citas de Bases sin página y «Anexo Anexo4-W». Se distinguen cuatro observaciones condicionadas: 15 figuras enlazadas frente a12incrustadas enMD, legibilidad histórica Figura24, granularidad de filasIA y formalidadPDF/mapeo100% sin certificar. Títulos obligatorios presentes;26tablas técnicas de2–5columnas;6columnasIA exigidas por§7.2. Se escribió sólo el informe Markdown y este registro; no se corrigieron entregables, no se editó LaTeX ni figuras, no se compiló, no se hizo commit/push ni se atribuyó revisiónhumana real. Preferencia solicitada: «caso» o «caso de logística», sin número; la prohibición literal no proviene de las Aclaraciones.

## SD4 — tabla ADR trasladada al Anexo 4-O — 11 de octubre de 2026

Por petición directa del usuario se retiró la tabla extensa de 4.1.11 y se incorporó al Anexo 4-O como Tabla A.17, delante del registro de fechas y estados (ahora A.18). El cuerpo conserva la explicación y referencia. Encabezados y 22 filas comparados contra el estado previo: intactos; sin duplicación en el cuerpo. Traslado aplicado en rama-md y LaTeX subdoc-4, preservando los cambios locales del plan anterior, untracked y otros subdocumentos. Sin commit ni push.

Se actualizaron exclusivamente referencias y numeración de tablas afectadas en SD4, anexos y T11: tablas posteriores del cuerpo disminuyen una posición y las de anexos desde fecha/estado aumentan una. La referencia al SD9 Tabla 9.11 se conserva sin cambios. Cuatro párrafos del despliegue/dimensionamiento ahora usan referencias automáticas en lugar de números incrustados. El resumen de anexos SD4 identifica la nueva ubicación; no se editaron decisiones, requisitos, tecnologías ni figuras.

Verificación: cero diferencias semánticas MD/TeX (1590 bloques cuerpo, 987 anexos, 110 T11), 342 enlaces internos válidos, 27 figuras sin cambios y diagrama aprobado con SHA256 conservado. PDF recompilados: cuerpo 194 páginas, anexos 94, T11 46; sin referencias indefinidas, caracteres faltantes ni cajas desbordadas. Tabla revisada visualmente en páginas 39–40 de anexos y transición a fecha/estado en 41. Revisiones humanas y mediciones reales del plan anterior continúan pendientes; no se atribuye su realización.

## SD4 — ejecución del plan de integración con SD13 y declaración de IA — 11 de octubre de 2026

El usuario autorizó ejecutar el plan únicamente para SD4 en rama-md y su espejo LaTeX subdoc-4; excluyó las observaciones de otros subdocumentos y las menciones de generación asistida en figuras o sus explicaciones. Remotos consultados: rama-md avanzó por fast-forward a 05f1d66708cbb1f524e1bbb294eeec2786fcec88; subdoc-4 permanece en c4d1230c9246f1a50933a8dc8a9a07b5d13a10be. No se autorizó ni realizó nuevo commit/push. Untracked md para drive/, 05/, propuestas y herramientas anteriores preservados.

Implementación: reconocimiento recíproco de las cinco innovaciones del SD13 en 4.1.4; realización, límites y seis contratos sobre componentes existentes en 4-N. Se mantienen doce módulos, 37 capacidades transversales y quince integraciones base. 4.2.6/4.2.6.12 y 4-W.12 incorporan carga incremental por innovación y recurso, método por ventana y pruebas mixtas/peak/N+1/corte/reconexión, sin consumos ni resultados ficticios. Las 10.920 muestras térmicas base no se duplican. No se presume margen libre ni suficiencia por reutilización. Los indicadores y aceptación funcional de innovaciones siguen en SD13. No se editó SD13, SD5, T12, A6, Bases ni otros subdocumentos.

Declaración IA: 56 filas (32 secciones, 23 anexos, T11), texto Alto conservado y nivel de diagramas corregido para reflejar asistencia real; 56 celdas de revisión humana sin inventar revisores ni aprobación. Sin notas de IA en diagramas o sus explicaciones. Resúmenes de cuerpo y anexos SD4 actualizados.

Verificación: cero diferencias semánticas secuenciales MD/TeX en 1614 bloques del cuerpo, 963 de anexos y 110 de T11; 342 enlaces internos válidos y 27 figuras con activos válidos. Diagrama de red aprobado intacto SHA256 912bf7b551a9bd005b9e8f00b39d265faa7ff34221b6934f33cf4ee33b841aac; ninguna figura editada. Compilación LuaLaTeX correcta: cuerpo 195 páginas, anexos 93 y T11 46; sin referencias indefinidas, caracteres faltantes ni cajas desbordadas. Revisados visualmente pasajes modificados y tabla IA horizontal; un ajuste local de ancho mejora sus columnas. PDF/herramientas de QA sólo en checkout LaTeX; en rama-md se mantienen únicamente los tres .md de 04_arquitectura. Pendientes reales: mediciones, revisión humana y consolidación en A6 por su responsable; no se atribuye ejecución ni conformidad total por describir pruebas.

## Estado vigente — 9 de octubre de 2026: segunda iteración de correcciones SD9 aplicada

Por instrucción del usuario se corrigieron sólo los materiales del SD9 (`09_plan_calidad/`): cuerpo, anexos, T-13 y T-17. No se tocaron otros subdocumentos.

- **Secuencia de pruebas:** en T-13 las pruebas de carga, resiliencia, DR, seguridad, despliegue, aceptación y perfil operacional comienzan después de la integración/regresión de cada etapa; SD9 9.3.2 explicita que la certificación se ejecuta después de integración.
- **H7/H12:** SD9, T-13 y T-17 exigen repetir antes del cierre de marcha blanca la intrusión por tercero, resiliencia y carga aplicable sobre la versión de cierre; si el alcance se acota por correcciones menores, igual debe haber ejecución e informe, no una mera declaración de ausencia de cambios.
- **Periodicidad:** DR queda en meses 27, 33, 39, 45, 51 y 54; resiliencia en 26, 32, 38, 44, 50 y 55, con regla de separación máxima de seis meses. Falta fijar días concretos si se quiere acreditar matemáticamente el máximo de seis meses dentro de cada par de meses.
- **Datos y DR:** se distingue QA/PREPROD/Terreno como ambientes de prueba sin datos productivos no anonimizados, y DR como réplica productiva restringida, auditada y para conmutación real.
- **Anonimización:** se retiró la presunción de irreversibilidad; Anexo 9.D exige prueba documentada de reidentificación además de Macie y bloquea la carga ante atribución a personas o claves mal protegidas.
- **Accesibilidad:** cualquier incumplimiento WCAG 2.2 A/AA confirmado por herramienta o revisión manual bloquea G4; regla 9B-23 alineada.
- **Aceptación:** T-17 y SD9 distinguen H6/H11 como condiciones de entrada a marcha blanca y H7/H12 como cierre con Art. 17.3. H6/H11 separan reversión técnica ≤10 min y reversión operativa documentada.
- **Referencias internas:** Anexo 9.A reemplazó `Carga_Estres` y `Metricas_Codigo` por referencias a secciones reales.

Verificación: conteo de líneas y marcadores en los cuatro archivos, búsqueda de residuos (`Carga_Estres`, `Metricas_Codigo`, regla WCAG grave, meses 26/33 y 27/34, declaración de ausencia de cambios), y `git diff --check` sobre las cuatro rutas; sin diagnósticos. Persisten 13 celdas `[[REVISIÓN HUMANA]]`, que sólo el equipo puede completar. `09_plan_calidad/` sigue sin seguimiento en Git y contiene `.drawio`/`.xlsx` preexistentes; la regla Markdown-only aplica a creación/edición/versionado, no se modificaron esos binarios. Sin commit.

Cambios recomendados fuera del SD9, no aplicados por alcance: alinear T-14 con los nuevos meses de DR/resiliencia si enumera fechas; revisar T-15 si todavía programa 3.8.4–3.8.8 o 3.9.3–3.9.7 en paralelo con integración; revisar SD4/SD6 si hablan de reutilizar evidencia o de criterios WCAG sólo graves; revisar informes de revisión para reflejar el nuevo estado.

## Estado vigente — 9 de octubre de 2026: correcciones internas del SD9 aplicadas

Por instrucción del usuario se aplicaron sólo las correcciones del SD9: cuerpo, anexos, T-13, T-17 y figuras.

- **Figuras:** se retiró «R18» de las figuras y se definió R18-01 a R18-16 en 9.2.5. La Figura 9.7 Mermaid incluye ahora el ejemplo de RF-09.01, y la 9.9 las pruebas periódicas y los congelamientos de la Operación. Fig_9-7.drawio se regeneró.
- **Cuerpo:**
  - la Tabla 9.4 tiene las cuatro métricas DORA (se agregó la frecuencia de despliegue);
  - 9.1.3 dice ahora «siete de ocho» umbrales de las Bases o del Caso;
  - ISO/IEC 25012:2008 e ISO 9001:2015 se citan y están en Referencias;
  - en las puertas G3 y G4 ningún hallazgo de seguridad admite excepción; sólo la regresión de desempeño 9B-22 la admite, también en el Anexo 9.B;
  - 9.3.2 y el T-13 8.1 fundamentan el H6 y el H11 como primer paso a producción y repiten la intrusión acotada y la resiliencia antes del H7 y del H12 si cambió la superficie expuesta, con cargo a R8-07.
- **T-13:** define las siglas de los roles.
- **Anexo 9.D:** deriva los 26 días hábiles.

El Anexo se regenera con `anexos.py` del scratchpad, que ya incluye esos ajustes. Las 14 correcciones pendientes en otros subdocumentos (T-14 1.5.2, SD4 4.1.1 y 4.2.4.1, SD6 6.2.2 y T-10, predecesoras del T-15, SD1 1.3.2 y 1.4, SD3 3.2, 3.J y RNF-14.07, T-12 RNF-06.02/06.03/11.03/11.04, T-14 3.8.7/3.9.1/3.9.6, SD6 6.1.3 y T-15 3.7.3) están listadas al final de `Revision/revision_comision_informe2_SD9.md`. Siguen abiertas las 13 celdas `[[REVISIÓN HUMANA]]` y las páginas de las citas a las Bases. Sin commit.

## Estado vigente — 9 de octubre de 2026: figuras draw.io del SD9 y revisión de la Comisión

**Figuras.** Se crearon las 10 figuras en `09_plan_calidad/Diagramas/` (Fig_9-1 a Fig_9-10, `.drawio`), con el estilo del SD7 y texto de 10 a 14 pt. Son XML válido y se revisaron visualmente con el visor de draw.io. Difieren en detalle de las figuras Mermaid del Markdown (9.4, 9.7 y 9.9 traen más contenido).

**Revisión.** `Revision/revision_comision_informe2_SD9.md` aplica el prompt del Informe 2. Puntaje 0 por el §7.1: 13 celdas `[[REVISIÓN HUMANA]]` y «R18» sin glosario en las figuras 9.6 y 9.7. El diagnóstico de contenido es 20 por contradicciones con otros documentos:
- cobertura: SD9 dice global y el T-14 1.5.2 dice «código modificado»;
- en G3, el Líder de Calidad puede levantar una vulnerabilidad alta de imagen, y eso choca con el SD6 6.2.2 y el RT-04.05;
- 16 herramientas no figuran en el SD4 4.1.1 ni en el SD6;
- el T-15 programa 3.8.4–3.8.8 y 3.9.3–3.9.7 en paralelo con 3.8.1 y 3.9.1, contra la puerta G4.

Errores menores:
- la Tabla 9.4 trae tres métricas DORA, no cuatro;
- el conteo «seis de ocho» de 9.1.3 está mal;
- ISO/IEC 25012 e ISO 9001 no están en Referencias;
- DES no se define en el T-13;
- falta derivar los 26 días hábiles;
- 18 de 27 citas a las Bases no indican página.

RNF-14.06 ya dice «anual»; sólo el SD1 1.3.2 dice semestral. No se modificó ningún entregable en la revisión. Sin commit.

## Estado vigente — 9 de octubre de 2026: SD9 completo (cuerpo, anexos, T-13 y T-17)

Se crearon tres archivos en `09_plan_calidad/`:
- `LAFROX-Subdocumento9-Anexos.md`, con cuatro anexos:
  - 9.A: 29 métricas ISO 25010.
  - 9.B: 24 reglas de análisis y la configuración de las herramientas.
  - 9.C: matriz de 645 IDs generada desde el T-12 y las prioridades del SD3. Da 605 IDs con prueba, 31 «No cumple» y 9 absorbidos o alias, con 1.192 casos más 90 de contrato, en total 1.282.
  - 9.D: 10 juegos de datos y reglas de anonimización.
- `LAFROX-Formulario-T-13.md`, con niveles, ambientes, criterios de entrada y salida, automatización y calendario con fechas del T-15 y meses de la Operación.
- `LAFROX-Formulario-T-17.md`, con el procedimiento del Art. 18, fichas de H1 a H12 y los R18 del producto final.

El cuerpo se ajustó a 1.282 casos, a 1.026 automatizados y a 64 HH manuales. La planilla quedó actualizada en `Diagramas/`.

Inconsistencias nuevas:
- RNF-06.02, 06.03, 11.03 y 11.04 aparecen como «Cumple» con componente propio en el T-12, pero el SD3 (Tabla 3.A.5a) los declara absorbidos o alias.
- El SD3 cuenta 261 requisitos y el T-12 tiene 271 filas.

Faltan los .drawio y la revisión humana.

## Estado anterior — 9 de octubre de 2026: cuerpo del SD9 redactado

Se creó `09_plan_calidad/LAFROX-Subdocumento9.md`, con introducción y las secciones 9.1 (marco, madurez CMMI/TMMi, ISO 25010, métricas de código, proceso y COQ), 9.2 (puertas G0–G6, análisis, 29119, datos de prueba, trazabilidad, defectos) y 9.3 (EDT, hitos, Operación). Tiene 10 figuras Mermaid (9.1–9.10), 9 tablas, referencias APA y la declaración de IA con `[[REVISIÓN HUMANA]]`.

Cifras del documento, tomadas de la planilla:
- 21,99 TPS, 1.163 usuarios, 237 dispositivos, 43,98 TPS a 3× y 10,41 TPS en la ventana de despacho;
- presupuesto de error de 43,2 min;
- 1.288 casos y regresión de 4,3 h con dos ejecutores;
- 10.848 HH de calidad (5,0 %);
- COQ: prevención 3.984, evaluación 6.864, fallas internas 358,4 y externas 2.956,8;
- holgura de H1 −4 y de H8 −6.

El T-12 vigente tiene RT 242/104/28, RF 136/44/1 y RNF 64/24/2. La planilla se regeneró con esos valores y con la hoja de ejecutores paralelos, pero el archivo de la carpeta estaba abierto en Excel y no se pudo reemplazar.

Faltan: Anexos 9.A–9.D, Formularios T-13 y T-17, los .drawio de las figuras, y la propagación de las decisiones de cobertura y pentest a T-14, SD4, SD1 y RNF-14.06. Sin commit.

## Estado vigente — 9 de octubre de 2026: plan del SD9 y planilla de cálculos

Se planificó el SD9 «Plan de calidad». El plan está en `compct/plan_SD9.md` y cubre la estructura 9.1–9.3, las preguntas por sección, las 10 figuras draw.io, los datos obligatorios, los cálculos y las inconsistencias. Se creó `09_plan_calidad/Diagramas/LafroX-Calculos-SD9.xlsx`, con 14 hojas y fórmulas vivas que leen de la hoja Datos_Base. Valores verificados con pycel:
- carga a 1,5×: 21,99 TPS, 1.163 usuarios y 237 dispositivos;
- presupuesto de error crítico: 43,2 min al mes;
- HH: 4.656 HH CAL y 10.848 HH ligadas a calidad (5,0 % de 216.935);
- calendario: 6 pruebas DR, 36 restauraciones, 3 pentests y 6 pruebas de resiliencia en Operación, sin conflictos con congelamientos;
- H1 y H8 con holgura negativa ante observaciones (revisión anticipada).

Decisiones del usuario: cobertura ≥70 % en lógica de negocio Y ≥80 % unitaria global; pentest anual y antes de cada paso a producción. Las correcciones a T-14 1.5.2, SD4 §4.2.4, SD1 §1.3 y RNF-14.06 quedan para la etapa de redacción. Los supuestos (casos por requisito, umbrales de complejidad, duplicación y deuda, meses de las pruebas en Operación) están en amarillo y deben confirmarse. Aún no se redactan el SD9, el T-13, el T-17 ni los .drawio. Sin commit.

## Estado vigente — 9 de octubre de 2026 (noche): 101 parciales A+B aplicados

Se aplicaron las 101 filas A (ya cubiertas) y B (frase simple) de `Revision/t12_iter/parciales_evaluacion.md` en SD4, SD4-Anexos, T-11, T-14, T-15, T-18, SD1, SD3, SD5, SD6 y SD13 (gpt-6.1-sol medio en tres grupos sin archivos compartidos; el grupo SD4 agotó el límite de uso de Codex tras editar y Claude redactó sus filas). Claude revisó y corrigió: páginas de cita, la ventana dominical de RT-17.03/04 (4.2.6.12), la periodicidad de intrusión del SD1 («al menos anual», compatible con T-14 8.2.2) y RF-18.02/RNF-14.06 a Cumple por cobertura cruzada. T-12: Parte A 237/31/3; Parte B 304/42/28. Detalle en `Revision/t12_iter/parciales_aplicacion.md`. Categoría C (29): plan en `Revision/t12_iter/plan_C_datos.md` con 12 C1 que LafroX puede proponer con fundamento y 17 C2 que requieren datos reales (precios, fichas, certificaciones, misión/visión, carbono); las BA prohíben precios en la Oferta Técnica. Categoría D (45) queda en parcial. Pendiente: actualizar los `Resumen/` de los documentos tocados en esta pasada. Sin commit.

## Decisión vigente — 9 de octubre de 2026: figuras PDF aceptadas

El usuario confirmó expresamente que los enlaces a los PDF de las trece figuras lógicas vigentes están bien. H09 se retira del informe de coherencia y de los pendientes; no exigir PNG/SVG ni conversión por el visor Markdown. Se conservan los objetos y enlaces actuales. Balance vigente: diez hallazgos corregidos, uno retirado por criterio confirmado (H09) y uno parcial (H03, definición del CLIENTE sobre congelamientos/intervenciones urgentes). Las 28 revisiones humanas y los ensayos futuros mantienen su estado. Esta decisión supersede las menciones a integración gráfica pendiente de los registros anteriores.


## Estado vigente — 9 de octubre de 2026: correcciones y segunda revisión de coherencia SD4

Por instrucción del usuario se corrigieron SD4 cuerpo/anexos/T-11, SD5 cuerpo/anexos, T-12 y los cuatro resúmenes afectados en `rama-md`, preservando cambios preexistentes. Se distinguió recuperación funcional crítica ≤4 h e histórico completo ≤8 h; promoción con exclusión comprobada y retorno como réplica; calendario sin excepciones supuestas y plazos de vulnerabilidades desde publicación/detección; dotación mes 25 de 19/21; canales comunes y bajas persistentes; ficha/rango térmico versionados y regla PREVENTIVA_FICHA sin aprobador. RT-16.02, RT-16.21 y RF-17.10 pasan a Cumple; RT-11.04 sigue parcial por la aclaración contractual pendiente. T-12 conserva sus 645 IDs y descripciones: A 200/68/3; B 242/104/28.

Se retiró la figura redundante sin objeto y se renumeraron 25 figuras, con referencias coincidentes. Los trece PDF vigentes quedaron como enlaces de apertura, no falsa sintaxis de imagen; NO hay PNG/SVG actuales equivalentes y las versiones antiguas contradicen quince actores y otras reglas. Pendiente su integración gráfica compatible; no generar derivados fuera de la rama para eludir la regla exclusivamente Markdown. Índice de anexos: 23 destinos explícitos válidos; retirados tres residuos restantes y citas 3.4.2.1. Erlang C revalidado (2.283: valle 80,00 %; 2.391: peak 80,02 %, valle con tres 95,26 %); desde mes 25 cálculo a 40 h, sin cambiar personas ni HH.

Informe actualizado: `Revision/revision_coherencia_SD4.md`: 10 hallazgos documentales cerrados; H03 parcial por definición formal del CLIENTE; H09 parcial por presentación gráfica. Conservadas 28 revisiones humanas pendientes en SD4. No afirmar 100 % de cierre ni ensayos ejecutados; quedaron controles de aceptación de partición/retorno y restauración. No se tocaron catálogos originales, archivos LaTeX/PDF/PNG ni se hizo commit/push. Esta nota supersede el estado de la revisión inicial de más abajo.


## Estado vigente — 9 de octubre de 2026 (noche, final): 18 de 21 RT del SD4 aplicados

Decisiones del usuario aplicadas por Codex (gpt-6.1-sol, medio) y revisadas por Claude: RT-16.33 con supuesto S-42 (al menos 15 % menos consultas asistidas de estado de entrega, saldo y documentos al cierre del primer año, línea base en marcha blanca) e indicador en SD4 4.1.3.1; RT-16.18 en Cumple por decisión del usuario (guía firmada por el ERP; XML, acuse SII y POD con hash y Object Lock seis años en 4.1.17), con la advertencia de que una marca de tiempo de registro no es un sello acreditado; RT-06.15 con paneles ciegos y sellado en 4.3.1.4; RT-15.06 con supuesto S-43 (lunes a viernes 08:00–20:00; meta de al menos 60 % menos horas de cómputo no productivo, excepción para correcciones críticas). RT-05.24, RT-15.05 y RT-16.26 quedan en No cumple por decisión del usuario. Una revisión independiente de los 25 RT agregados llevó a seis ajustes (RT-08.18, 08.19, 14.09 sin IA por D-09, 15.06, 16.25 y RF-17.06), SD3 a 43 supuestos, texto de caída en el Anexo 4-P y retiro del residuo «[1]8pt / #12pt». T-12: Parte A 199/69/3; Parte B 240/106/28. Se conservaron los cambios sin commit del usuario (coordinación MD–LaTeX en SD4, anexos y T-11). Pendiente en SD5: dominios de canal de `not_plantilla` (CORREO/WHATSAPP/AVISO_EN_PORTAAL, con errata) frente a EMAIL/SMS/PUSH. Sin commit.

## Estado vigente — 9 de octubre de 2026: revisión de coherencia del SD4 tras reintento

Revisión solicitada desde `rama-md`, sobre HEAD `e76e0c7` más los cambios preexistentes en SD4, anexos, T-11 y T-12. La evidencia se revalidó tras cambios externos. Informe: `Revision/revision_coherencia_SD4.md`, con doce hallazgos: criticidad/restauración 4–8 h; exclusión del escritor al promover standby; congelamientos y correcciones críticas; dotación mes 25 omitida en Tabla 33; justificaciones RT-16.02/21; canales y vigencia de bajas; fuente del rango térmico previo a aprobación; Figura 17 sin objeto; trece PDF usados como imágenes; citas a 3.4.2.1 inexistente; 23 fragmentos del índice de anexos; cinco restos del conversor. La declaración consolidada conserva 28 revisiones humanas pendientes. No se corrigieron entregables: solo informe y esta nota; sin commit/push. Figuras remotas y presentación PDF sin acreditación visual completa. Las afirmaciones de limpieza del registro anterior deben contrastarse con H12: los cinco restos siguen en la versión actual.

## Estado vigente — 9 de octubre de 2026: SD4 alineado entre Markdown y LaTeX

Por decisión del usuario, el MD de `04_arquitectura/` es la base y queda alineado con el LaTeX de `subdoc-4` (`9329485`). Se trajeron desde el LaTeX:

- las figuras nuevas de 4.1 (general, ocho capas y cuatro complementarias, enlazadas a `9329485`), el retiro de la vista resumida y la renumeración de figuras (el T-12 cita ahora las Figuras 25 y 26);
- el texto de 4.1.5 y de las secuencias;
- los nombres funcionales en el cuerpo de 4.1, con sus equivalencias en los Anexos 4-G y 4-P;
- el inventario AWS en el Anexo 4-P y las viñetas de 4.1.

Hay una sola declaración de IA, al final del cuerpo; se quitaron las de los anexos y el T-11. Las referencias están en orden alfabético y sin enlaces a archivos. Se limpiaron restos del conversor.

El contenido del MD (RF-10, nombres del SD3, párrafos RT del T-12, 4.2.1.2, mes 25, etc.) se trasladó al LaTeX en el worktree `../LafroX-subdoc4` (rama `subdoc-4`), por autorización expresa del usuario. Compila limpio (cuerpo de 173 p., anexos de 83 p.). Al reconvertirlo con `tex2md.py` se obtiene este MD, salvo artefactos del conversor. El registro está en `../LafroX-subdoc4/00/trazabilidad/ALINEACION_MD_LATEX_2026-10-09.md`.

Pendiente de decisión: el SD4 cita el SD5 (LafroX 2026a/b). Ninguna de las dos ramas tiene commit.

## Estado vigente — 9 de octubre de 2026: planilla de la carta Gantt actualizada

`07_.../Diagramas/LafroX-Carta-Gantt-SD7.xlsx` regenerada desde el T-15 vigente (respaldo previo en el scratchpad): 222 paquetes y 49 cuentas con meses y HH actuales (204.527 HH), hitos con entregas, probabilidades y P80 del SD8 vigente (H4 86,5 %), hoja «Actividades» renombrada a «Actividades hasta H2» con las 108 actividades de la Tabla 6.1b, 8.1.2 = 54.239 HH, Léeme y Glosario actualizados (planificación gradual, 40 desarrolladores, 216.935 HH). Fórmulas y formato condicional conservados; Excel recalcula al abrir. Sin commit.

## Estado vigente — 9 de octubre de 2026: hallazgos P1–P7 de la sexta revisión corregidos

- P1: 3.6.1–3.6.4 (integraciones externas E1) son predecesoras de 3.8.1 (D-20 ampliada en el Anexo 7.B y nodo nuevo en Fig_7-5); terminan entre el 02-08 y el 01-09-2027; ventanas 6–7 y 7–8. H4 se entrega el 20-10-2027, pero con riesgos baja a 86,5 % (P80 15-11-2027) y H5 a 88,8 % (P80 13-01-2028); ocho juntas 67,6 %.
- P3: el tercer agente de la mesa pasa al mes 25 (14.161 HH); 8.1.2 = 54.239; base 204.527; total 216.935; operación 128.373,67. SD4 4-W.7 y tabla 15 actualizados.
- P4: R8-22 P4 I3 E12 NPR36, VE 2.251,20; contingencia 20.198,98 (9,88 %), residual 14.055,17, capacidad movilizable 238.733,98.
- P2/P6/P7: Tabla 6.1 con «Personas (prom. / máx.)», predecesoras agrupadas por cuenta y nota sobre el análisis adelantado de los módulos.
- Propagado a T-15, SD8, T-16, SD7, Anexo 7.B, SD4 y resúmenes; Fig_T14-2 (barra 3.6 m6–19). El modelo de `compct/` reproduce desde el repositorio. Sin commit.

## Estado vigente — 9 de octubre de 2026: cronograma por paquetes, 40 desarrolladores y mesa en la base

Plan aprobado (`~/.claude/plans/planifica-los-arreglos-diagrmas-compressed-blum.md`) ejecutado. Decisiones: Gantt por paquetes con planificación gradual; R8-22 al plan base; tope de desarrollo 40 (con 30–36 el H4 caía a 50–70 %, se consultó y el usuario eligió 40).
- T-15: §6.1 = Tabla 6.1 de 163 paquetes + Tabla 6.1b (108 actividades de 56 paquetes hasta el H2) + Figura T15.3; las 564 actividades quedan como respaldo en `compct/T15_actividades_internas.md`. Módulos E1 desde el 10-06-2027 (3.3.1/3.3.5/3.3.6 desde el 01-06), nivelados con 40 DES; ventanas 4.2 actualizadas; tabla de clases de tamaño en §4.1; 8.1.2 = 56.024 HH (tercer agente desde el mes 21, 15.946 HH); base 206.312, programación 218.720, operación 130.158,67; peak 68 (mes 15), DES 29 equivalentes (mes 7); §4.5 con contingencia 19.448,58 y total movilizable 239.768,58; Tabla 5.2 (H4 99,6 %, H5 97,8 %).
- SD8/T-16: R8-22 «Demanda de la mesa supera la dotación base», P3 I3 E9, cota 4 h × L–S meses 21–56 = 3.752 HH, VE 1.500,80; registro conjunto 19.448,58 (9,43 %), individual 20.197,76, correlacionado 18.984,96, residual 13.304,77; ocho entregas juntas 77,84 %; 21 críticos. Modelo en `compct/modelo_montecarlo_SD8.md` (DES 40, lee el respaldo interno) reproduce las tablas.
- SD7 (7.2, Tabla 7.4, 7.3.1, 7.3.8), Anexo 7.F, T-14 (Gantt mermaid y diccionario 3.4.x), SD6 6.2 (planificación gradual e iteraciones), SD4 4-W.7 y tabla 15 (tercer agente desde el mes 21: 9 personas, límite 2.391), resúmenes T-15/SD7/SD8.
- Diagramas: Fig_7-7 (barra 3.4), Fig_T14-2 (barras 3.4 y 3.6), Fig_7-8 (nota de planificación gradual), nueva Fig_T15-3_Planificacion_Gradual.drawio. Sin commit. Pendiente: revisión humana y revisión visual en draw.io.

## Estado vigente — 9 de octubre de 2026: quinta revisión del SD8 (Bases, clases y EDT)

EDT_Puelche.drawio = Figuras 7.1–7.3; contiene los 222 paquetes del T-15 y no requiere cambios. Corregidas contradicciones residuales: Anexo 7.F (P7-02 «4 a 35»; política de reservas H2 12, H8 4, H10 25), frase de versión en T-15 5.2, fila de contrato de implantación con opción de 8 personas en SD6 Tabla 6.3, revisión anticipada del H1/H8 en T-15 5.5 y R8-12 (H8: semana del 6-03-2028, control principal). Puntaje 0 por revisión humana; contenido 80. Contraste con FEP04/PMBOK conforme; sugerencia: justificar en 8.3.2 la contingencia de 15,6 % frente al 8 % del ejemplo del curso. Sin commit.

## Estado vigente — 9 de octubre de 2026: diagramas draw.io del SD7 actualizados

El usuario subió `07_.../Diagramas/*.drawio` (7 archivos). Editados: Fig_7-7_T15-1 (barras 1.2.5·2.1.4 y 2.4.2, reserva H8 4 días y 91,1 %, H9 100 %, barra 3.9.2–3.9.7 hasta 12-06-2028, reserva H10 25 días, leyenda D-29 a D-31c), Fig_7-5 (2.4 elaboración m3 y acta m4; D-31c), Fig_T14-2 (barra 2.4 desde 19-04-2027 a 13-03-2028, m3–14; barra 3.9 hasta 12-06-2028). Sin cambios necesarios: Fig_7-4, Fig_7-6_T15-2, Fig_7-8_T14-1, Fig_T14-3. Faltan en la carpeta (no afectados por los cambios del SD8): Figuras 7.1–7.3 (EDT; existe EDT_Puelche.drawio), 7.9–7.12. Sin commit.

## Estado vigente — 9 de octubre de 2026: cuarta revisión de la Comisión del SD8

Puntaje 0 sólo por las 18 celdas `[[REVISIÓN HUMANA]]`; contenido 80/100. Pendientes: (1) firmas reales; (2) H8: con observación formal, entrega 13-03-2028 + 10 días de revisión + 5 de subsanación = 03-04-2028, mes 15; declarar la revisión anticipada del borrador (semana del 6-03-2028) como control principal; (3) opción de 8 personas del contrato de implantación ausente en SD6 6.1.3; (4) revisión anticipada H1/H8 ausente en T-15 5.5. Sin commit.

## Estado vigente — 9 de octubre de 2026: observaciones de la tercera revisión del SD8 corregidas

F1 pasa al 5-05-2028 (1 de mayo feriado; 2–4 son los tres primeros días hábiles): T-15 4.2.3.A01 05–15 may 2028, SD8 C-07 y C.3.1, modelo; simulación sin cambios en sus resultados. H1/H8: revisión del borrador con la Contraparte Técnica una semana antes y subsanación en cinco días hábiles (R8-12, T-16, E8-11). Suplentes desde el mes 22: Trejo para DAT/DES y Miño para IMP (SD8 8.1.2). Opción de hasta 8 personas por cuatro semanas en el contrato de implantación, firmado antes del mes 11 (R8-18, E8-14, T-15 4.5 y 5.7, resumen). Revisión humana: decisión de no completar celdas por el grupo; `Revision/plantilla_revision_humana_IA.md` lista las 18 celdas del SD8 con revisor propuesto y verificación concreta. La entrega sigue bloqueada hasta que los integrantes las firmen. Sin commit.

## Estado vigente — 9 de octubre de 2026: tercera revisión de la Comisión del SD8

Se volvió a aplicar el prompt del Informe 2 al SD8 corregido y se reemplazó `Revision/revision_comision_informe2_SD8.md`. Puntaje 0 sólo por las 18 celdas `[[REVISIÓN HUMANA]]`; diagnóstico de contenido 60/100 (antes 20). SD8, SD7, T-15 y resúmenes coinciden. Pendientes: F1 = 04-05-2028 es el tercer día hábil de mayo si se cuenta el feriado del 1 de mayo (Caso 13.3, punto 2), y figura en SD8 C-07/C.3.1 y T-15 4.2.3.A01; reservas del H8 (4 días) y del H1 (6) menores que los 10 días de subsanación del Art. 18.3; suplente para la concentración de responsabilidades en Castillo desde el mes 22; acreditar la ampliación del contrato de implantación. Sin commit.

## Estado vigente — 9 de octubre de 2026: correcciones de la revisión del SD8 aplicadas

Por instrucción del usuario se corrigieron los hallazgos de `Revision/revision_comision_informe2_SD8.md`. T-15 (Tabla 6.1): 2.2.3 con 4 SEG (1–16 abr 2027); 2.4.1 elaborado 19–29 abr 2027 (ventana 3–3) con predecesoras de diseño; 2.1.4 con 4 ARQ (1–16 feb 2028); 2.4.2 1–13 mar 2028; 3.7.5.A06 «Conciliación final, acta y corte en día permitido», única actividad productiva del corte, después de 3.7.3/3.7.4; 3.9.2.A02–A04 con 5 CAL tras 3.9.1 (D-31) y 3.9.6 1–12 jun 2028; 3.9.3–3.9.5 tras 3.5 (D-31b); predecesoras 1.2.2 y 7.1.4 como paquetes continuos. T-15 4.4 (meses 3, 4, 16, 17), §5.7 CAL 10, Tablas 5.1 y 5.2, §2, §5.2 y nueva §4.5 de reservas; SD7 7.3.1 y Anexo 7.B (D-24, D-31, D-31b, D-31c). Simulación rehecha (5.000 iteraciones): todos los P80 dentro de su límite; mínimo H3 88,3 %, H8 91,1 %, H2 97,4 %; ocho juntas 78,0 %; H6 preparado 96,5 %. R8-07 sin el SOC 8.1.5 (base 2.112 HH, VE 380,16). Registro conjunto 29.647,18 HH (15,57 %), residual 23.503,37; gestión 1.600 HH (módulo D + integración + certificación); total movilizable 234.021,18 HH; sólo IMP excede dotación (meses 15 y 20, ampliación del contrato). SD8: código Python, huellas y rutas retirados del Anexo 8.C (el modelo queda en `compct/modelo_montecarlo_SD8.md`); notas de auditor reescritas; frases repetidas de las 32 fichas consolidadas en la introducción de 8.A; 24 riesgos secundarios específicos; E8-13/E8-14 nuevas (se eliminaron E8-15/E8-16); referencias a las Bases con el formato del SD6/SD7. Resúmenes del SD8 actualizados. Pendiente que sólo puede cerrar el grupo: las 18 celdas `[[REVISIÓN HUMANA]]` del SD8, sus anexos y el T-16 (y las de SD7/T-15 editados). Pendiente fuera del Markdown: figuras 7.7 y T15.1 si muestran reservas antiguas. Sin commit.

## Estado vigente — 9 de octubre de 2026: revisión de la Comisión del SD8 tras «cambios doc 8»

Se volvió a aplicar `Revision/prompt_revision_comision_informe2.md` al SD8, sus Anexos y el T-16 en el estado del commit `ebe5eab`, y se reemplazó íntegramente `Revision/revision_comision_informe2_SD8.md`. Puntaje 0/100 por tres indicios del §7.1: 18 celdas `[[REVISIÓN HUMANA]]` (11 cuerpo, 6 anexos, 1 T-16); contradicción con el SD7 7.3.1 y el T-15 Tabla 5.2 (el SD8 da H2 0 %, H8 0 %, H9 100 %, H10 31,02 %, ocho hitos juntos 0 %; H6 preparado 5,74 %, H7 40,16 %, H12 40,36 %; el SD7/T-15 dicen ≥89,9 % en todos); y código Python con rutas y nombres `.md` en el Anexo 8.C.3.3. Diagnóstico de contenido sin §7.1: 20/100 (antes 40). De H01–H16: 9 corregidos, 5 parciales, 2 no corregidos (revisión humana; contingencia de 35.219,98 HH fuera del T-15, 18,5 % de la base, con 24,5 personas equivalentes extra en el mes 15). Gestión de 400 HH sin dimensionar; R8-22 (11.699 HH) es capacidad de mesa no programada. Las huellas SHA-256 del T-15, el SD7 y sus anexos coinciden: el SD8 se cambió y no se propagó. Los resúmenes del SD8 siguen con 15.076 HH. No se modificó ningún entregable. Sin commit.

## Estado vigente — 9 de octubre de 2026: T-12 reconstruido

Por instrucción del usuario se reemplazó `03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md` con una matriz de cinco columnas exactamente como el Formulario T-12 de las Bases Administrativas: ID requerimiento, Descripción, Cumple, Componente que lo satisface y Sección de la propuesta. Contiene 271 RF/RNF del anexo SD3 (181 RF, 90 RNF) y los 374 RT de las Bases Técnicas Transversales; 645 IDs únicos. El estado usa Cumple, Cumple parcialmente o No cumple; hay 462, 113 y 70 filas respectivamente. Los 26 valores del capítulo 15 del Caso se agregaron a la descripción del RT correspondiente, incluidos los nueve códigos cuyo significado difiere del de las BTT. RT-05.10 y RT-15.02 se ajustaron a cumplimiento parcial al responder conjuntamente el contenido transversal y el del Caso. RF-07.11 se clasificó parcial porque RF-07.10 compromete esa función, aunque el catálogo del anexo contiene una declaración contradictoria. La matriz se generó desde `Revision/T12_mapeo_cumplimiento.md`, contrastando las 374 descripciones RT con las BTT y las 271 descripciones RF/RNF con el anexo SD3. Se cotejaron visualmente los PDF originales de las Bases Administrativas (formulario T-12, página impresa 62), BTT (§1.4–1.5, página impresa 4) y Caso (tabla del capítulo 15, página impresa 27); los PDF son imágenes sin texto extraíble, por lo que el cotejo de todas las filas se hizo con las copias Markdown de las Bases. Verificación automática: 645 filas de cinco celdas, 645 IDs únicos, 26 valores del Caso, 648 referencias numéricas SD con sección existente y 526 referencias a anexos con encabezado existente; `git diff --check` pasó. Quedan 79 filas sin sección acreditable, conforme a sus estados parcial/no cumple. La paginación exigida por BTT §1.5 sigue pendiente del documento paginado. Falta la revisión humana real de la declaración de IA. No se hizo commit.

## Estado vigente — 8 de octubre de 2026 (noche): revisión de cumplimiento del T-12

Decisión del usuario: el T-12 contiene todos los RF y RNF del Anexo del SD3 y los 374 RT de las BTT, con las cinco columnas del formulario de las BA (p. 62/77): ID requerimiento, Descripción, Cumple, Componente que lo satisface, Sección de la propuesta. Se revisó cada fila contra SD1–SD8, SD13, anexos y formularios; el resultado está en `Revision/T12_mapeo_cumplimiento.md` (Parte A 271 filas: 224 cumple, 34 parcial, 13 no; Parte B 374: 239, 76, 59). El T-12 vigente no se modificó. Hallazgos clave: secciones del T-12 apuntan al SD3 y no al desarrollo real; «Base compartida» sin producto ni versión; seis RT «No ofertado» que SD4 sí compromete; códigos del Caso cap. 15 que no coinciden con las BTT (RT-03.13, 03.24, 05.10, 09.01, 15.02, 16.14, 16.21, 16.30, 21.06); RT-13, RT-16, RT-21 y RT-15.03 casi sin desarrollo; RF del caso sin soporte en el modelo de datos del SD5; duplicados RF-19.xx / RF-14.xx-BTT y RF-07.10/07.11. Pendiente: decisión del usuario para aplicar el mapeo al T-12. Sin commit.

## Estado vigente — 8 de octubre de 2026: nueva revisión integral del SD8

Por petición del usuario se volvió a aplicar `Revision/prompt_revision_comision_informe2.md` al SD8, Anexos 8.A–8.F y T-16, contrastando las cuatro Bases y los entregables vigentes SD1–SD7 y SD13. Se reemplazó íntegramente `Revision/revision_comision_informe2_SD8.md`; su revisión anterior y nota posterior ya no representan el estado actual. La revisión general conserva carácter histórico para S8.

- Puntaje del prompt: 0/100 en el ítem 8 (10 % del Informe 2), por 15 filas de revisión humana pendientes: 7 cuerpo, 7 anexos y 1 T-16. No se inventó revisión humana. Diagnóstico de contenido sin §7.1: 40/100, sin efecto en el puntaje.
- Se retiraron hallazgos ya corregidos: RBS ahora Mermaid, apetito, Concepción/peak septiembre, costo-beneficio de 22 críticos, plazos H7/H12, H9 89,9 %, compra/sala, citas y suspensión láctea.
- Se registraron 16 hallazgos identificados H01–H16, con evidencia y acciones: revisión humana; relevo DAT/IMP después del mes 21; horizonte R8-11; simulación sin nueva nivelación, correlación y evidencia reproducible; sensibilidad y exclusión de marchas blancas; contingencia adicional sin curva en T-15; elegibilidad temporal de capacidad protegida; año de impacto para horizontes largos; residual uniforme/estrategia evitar; gestión sin magnitud; costo-beneficio de diez altos; demanda de mesa y base 22.640 HH de R8-11.
- Verificación: 32 fichas/FMEA/T-16 coherentes en P/I/D y productos; 222 paquetes T-15 suman 190.366 HH; VE exacto 15.075,84, residual hipotético 10.802,56 y contingencia adicional declarada 13.223,04 HH. No se ejecutó Monte Carlo ni se acreditaron probabilidades, ensayos o contratos.
- Se comprobó conservación de las huellas SHA-256 de los 26 entregables originales. Sólo se modificaron el informe de revisión y este contexto, ambos Markdown. No se modificó la planilla, el prompt ni las Bases; sin commit ni publicación. Controles exclusivos de PDF pendientes.

## Estado vigente — 8 de octubre de 2026 (noche): coherencia entre subdocumentos aplicada

## Estado vigente — 8 de octubre de 2026 (noche): coherencia entre subdocumentos aplicada

Decisiones del usuario aplicadas a los Markdown de `rama-md` (sin commit):
- Infraestructura on-premise: la provee LafroX dentro del precio del contrato (BA art. 14.2; valorización en la Oferta Económica, art. 50.2). El CLIENTE compra solo el hardware de terreno (E-09). Obra civil de separación: cargo del CLIENTE, LafroX especifica y coordina (RT-06.06). SD6 6.1.3, SD7 7.1.2 y 7.B, T-14 5.1/6.1.1, T-15 §4.1/§5.2/§5.3, SD8 R8-19, C.4, E8-02 y T-16 alineados.
- Fechas de la sala (cronograma por actividad): planos mes 1, orden de compra de LafroX mes 2, instalación mes 3, recepción mes 4, racks meses 4–5, borde de los CD mes 5, gabinetes de cross-docking mes 9.
- Starlink en cinco sitios (Talca, Concepción y tres cross-docking) y ocho planes LTE en SD6 y T-14 5.3; SD1 1.6 menciona los CD.
- Ruta crítica: cadena de la Etapa 2 (H8 13 días, H9 21 días y 89,9 %, H10 28 días). La cadena del ERP (H4/H5), el H3, el planificador, los acuerdos y las cadenas son casi críticos. SD7 7.2.1/7.3.1, 7.B y T-15 §2 alineados.
- Reservas por hito: las de T-15 Tabla 5.2 (6 a 35 días); escalamiento al superar la mitad de la reserva. Corregidos 7.F, T-15 §5.4 y SD6 6.1.5.
- «CD-05» era el complemento de coordinación de datos del SD5 (3-oct); en SD4 es la coordinación de reserva y retención (4.1.4.4; Anexo 4-G; Tabla A.10; Tablas A.32 y A.33). «A31/A32» eran esas tablas antes de renumerarse. Reemplazado en SD7, 7.F, T-14, T-18, SD8 y T-16.
- Laravel: SD4 sin rastro de una versión Django (4.1.7, 4.1.8 «Implantación progresiva por olas», 4.2.4.1.3 «Implantación por olas en los sitios», Anexo 4-P).
- Nombres de módulos de SD3 en todo SD4 (títulos 4.1.4.x, Tabla 8, Anexos 4-D, 4-E, 4-F) y en T-18.
- Reversión técnica ≤ 10 min en SD4 4.2.4.1.2, SD7 Tabla 7.8 y T-18; los 4 h del Art. 78.3 son restauración de incidentes.
- RF-10 (reposición) en SD4 M2, INT-06 y Anexos 4-D/4-E/4-N; la función de abastecimiento se ejerce dentro de perfiles autorizados (SD3 Anexo 3.I), sin actor 16.
- Traslado del servidor del ERP dentro de T-14 6.3.1; T-14 6.3.3/6.3.4 con servidores y mini-PC activo/espera; T-14 4.1.2/4.1.3 corregidos; T-18 fechas prohibidas según SD4 Tabla 14.
- SD4 4.1.21 cita S-22/V-01 (instalaciones); SD4 4.3.1.4 especifica el blindaje junto a la explicación del plano del recinto (RT-06.02) y T-12 RT-06.xx remite a SD4 4.3.1.4.
- SD6: interesados alineados con los 19 actores del SD2; umbral de cobertura igual a SD1. SD2 remite la arquitectura al SD4. T-15 §5.7 explica 6 equivalentes del SOC frente a 4–5 personas del SD4.
- Resumen: T-11, T-15, T-18, SD4-Anexos y SD6 actualizados.
- Pendiente fuera del Markdown: figuras 7.5 y 7.7 del SD7 (marcar la ruta crítica de la Etapa 2) y replicar todo en LaTeX. Ediciones con gpt-6-astra medio (gpt-6.1-sol no disponible) revisadas por Claude; la revisión GPT posterior no se ejecutó por el límite de uso de Codex.

## Estado vigente — 8 de octubre de 2026: SD8 alineado con FEP04 y PMBOK 6 cap. 11

Contraste con FEP04 (d. 6–9, 18–21, 42–54, 59–68, 105, 112) y PMBOK pp. 202, 433–436, 442–444 y 456. Corregido: la Tabla C.5 usaba impacto / costo; ahora usa ahorro esperado (VE inicial − residual, con P un nivel más baja) / HH del control, y sólo R8-11 (17,0), R8-14 (4,2) y R8-18 (2,1) superan 1; los otros 18 críticos se aplican por la regla del nivel crítico. Cada ficha tiene estrategia PMBOK (Mitigar 28, Escalar R8-12/R8-17, Evitar R8-14, Aceptar activamente R8-22), efecto esperado, residual y riesgo secundario; T-16 antepone la estrategia. VE residual del registro 10.803 HH; liberable 4.273 HH. La contingencia sigue en 15.076 HH (VE inicial, FEP04 d. 47–48), forma parte de la línea base y se libera al verificar controles. 8.1.3 declara zonas de acción, tolerancia y umbral; 8.1.1 agrega análisis de reserva, auditoría de riesgos en H5/H10 e informe mensual; O8-01 con estrategia «mejorar». Resúmenes del SD8 actualizados. Pendiente: no hay riesgos de la rama externa de la RBS del PMBOK (cambio normativo, por ejemplo del SII o de la Ley 21.719); agregarlo cambia el VE total y la contingencia citada en SD7, SD13 y T-15. Sin commit.

## Estado vigente — 8 de octubre de 2026: observaciones de la revisión del SD8 corregidas

Se aplicaron en SD8, Anexos y T-16 las observaciones de `Revision/revision_comision_informe2_SD8.md`, salvo valores monetarios y magnitud de la reserva de gestión (por decisión del usuario, hasta la entrega final). Cambios: Figura 8.1 en Mermaid; apetito de riesgo en 8.1.3; mapa de los siete riesgos del Caso 19 en 8.2.1, con Concepción en R8-03 y peak de septiembre en R8-18 (sin cambiar P, I, D ni valor esperado); Tabla C.5 de costo-beneficio de los 22 críticos (HH del paquete de control del T-15 frente al impacto de B.2) y línea específica en cada ficha; glosario de códigos en 8.A; línea de seguimiento repetida movida a la introducción de 8.A; redacción de fichas y T-16; citas APA 1:1 en los tres archivos; leyendas «Tabla 8.N —»; C-04 con 12 puestos. «CD-05», «A31» y «A32» no existen en el SD4: se reemplazaron por coordinación de reserva de INT-03/04, Anexo 4-I y 4-W.5 (R8-02 y R8-06 renombrados). Siguen con esos códigos obsoletos el cuerpo del SD7 (párrafo final, sobre el Anexo 7.F), el Anexo 7.F (P7-09 y P7-10) y el T-18 (§ de CD-05). Pendientes: 13 celdas `[[REVISIÓN HUMANA]]`; Tabla C.4 con 5.000 iteraciones; imagen de la Figura 8.1 para LaTeX. Sin commit.

## Estado vigente — 8 de octubre de 2026: revisión de la Comisión sólo del SD8

`Revision/revision_comision_informe2_SD8.md` aplica el prompt del Informe 2 al SD8 tras corregir sus contradicciones. Puntaje 0 por 13 celdas `[[REVISIÓN HUMANA]]` y RBS en lista; sin la causal, 40 (antes 20). Pendientes: RBS dibujada; riesgos del Caso 19 ausentes (enlace de Concepción; peak de septiembre sobre la marcha blanca E2); costo-beneficio repetido en 32 fichas; referencias sin cita; «13 puestos» de C-04; T-16 R8-11 desalineado con 8.A; cámaras en R8-21. No se modificó ningún entregable. Sin commit.

## Estado vigente — 8 de octubre de 2026: contradicciones del SD8 corregidas

Regla del usuario: en cada contradicción manda el subdocumento anterior, salvo algo muy importante. Se corrigieron en SD8 (cuerpo, anexos y T-16) las siete contradicciones de su hoja en la planilla:
- C-12 (SD4 manda): el RPO ≤15 min se cumple con tres caminos; la falla de los tres seguida de destrucción del sitio es riesgo residual justificado (RT-02.11; SD4 4.3.2.4). Introducción, Tabla 8.1, 8.3.3, R8-05, nota de 8.B, E8-05 y T-16 R8-05 ya no dicen «aceptar el riesgo no satisface Bases».
- C-14: SD8 8.2.3 dice 89,9 % para el H9. Excepción a la regla: también se cambió SD7 7.3.1 a «al menos el 89,9 %», porque es el resultado calculado de su propio T-15 (Tabla 5.2).
- C-15: SD8 8.2.3 aclara que los 9.336 HH de soporte puente son parte de las 16.664 HH del período 16–20 de la Tabla 7.4. La etiqueta de esa fila del SD7 no se tocó.
- C-16 (SD7 7.2.2 manda): E8-01 y R8-11 describen clases de tamaño fundadas en T-12 y T-11 con tríada ±25 %, sin llamarlas «supuestas».
- C-17: «antes del H7 (mes 16) y del H12 (mes 21)» en R8-22, E8-07 y T-16.
- C-18: E8-11 dice que la subsanación consume la reserva del hito; H2–H10 (13–35 días hábiles) la absorben y el H1 (6) no.
- C-21: suspensión del proveedor de lácteos «de marzo a septiembre de 2026» en 8.3.3 y E8-08.
Se actualizaron las declaraciones de IA de los tres archivos y `Resumen/LAFROX-Subdocumento8-Resumen.md`. La planilla `.xlsx` no se modificó (estaba abierta en Excel): falta marcar la columna J de la hoja SD8. Sin commit.

## Estado vigente — 8 de octubre de 2026: segunda revisión de la Comisión y planilla de contradicciones

Se reemplazó `Revision/revision_comision_informe2.md` con una nueva corrida del prompt sobre SD1–SD8 y SD13; el SD9 no se evaluó por instrucción del usuario. Puntaje actual 0 en todos los ítems por las 204 celdas `[[REVISIÓN HUMANA]]`; sin esa causal, 23,4 sobre el 89 % evaluado. Las 22 contradicciones entre subdocumentos (8 altas, 9 medias y 5 bajas) están en `../Contradicciones_LafroX_Informe2.xlsx`, fuera del repositorio porque la rama sólo admite `.md`: hoja Registro con una fila por contradicción y una hoja por subdocumento con todas las contradicciones en que participa, sincronizadas: la acción marcada en la columna J de una hoja aparece en la columna K de la otra y el estado común se recalcula en ambas. No se modificó ningún entregable. Sin commit.

## Estado vigente — 8 de octubre de 2026: guías de lectura en Resumen

El usuario autorizó implementar el plan de `Resumen/` en la rama comprobada `rama-md`, sin cambiar de rama ni realizar commit/publicación. La carpeta contiene 26 guías independientes y `README.md`: nueve subdocumentos (1–8 y 13), siete archivos de anexos que explican 66 anexos individuales y diez formularios. Cada nombre conserva el original con sufijo `-Resumen.md`; la carpeta es plana y exclusivamente Markdown.

Las guías usan el contenido local vigente y distinguen compromisos, supuestos, cálculos y verificaciones pendientes. Se excluyen Bases, material del curso, revisiones, catálogos auxiliares y el borrador de innovaciones. No se alteraron los 26 entregables fuente. Se actualizó el acceso desde README y se registró procedencia en MANIFIESTO. Al cambiar un original se actualiza manualmente su resumen y las guías relacionadas; no existe generación automática.

Durante el cotejo final se incorporaron cambios concurrentes de los originales: SD1 y T-15 describen ahora PHP/Laravel y Kotlin; no se mantiene como pendiente la antigua diferencia con Python/Django. La contingencia adicional vigente del SD8 es 13.223 HH; la cifra histórica 12.004 HH del contexto no se trasladó como diferencia actual al SD7. Siguen descritas diferencias vigentes: doce resultados E1 en el cuerpo SD7 frente a catorce con verificaciones E1 en 7.C/T-18, y responsabilidades/fechas de sala técnica entre SD6, T-11 y T-15. Las guías no las corrigen ni acreditan aceptación.

Verificación completada: 27 archivos Markdown en Resumen, correspondencia uno a uno de los 26 documentos, 66 anexos cubiertos exactamente una vez, 280 enlaces locales con destino y ancla válidos, 24 comprobaciones de cifras clave en las fuentes y tres comprobaciones aritméticas. `git diff --check` pasó. Los hashes de los 26 originales permanecieron iguales respecto de la última lectura completa tras las actualizaciones concurrentes; las únicas modificaciones de esta tarea fuera de Resumen son README, MANIFIESTO y este contexto.

Los encabezados de rama/alcance de los registros anteriores son históricos; esta autorización explícita gobierna la creación de la carpeta Resumen en `rama-md`. La asistencia de IA en las guías no constituye revisión humana adicional de los originales.

## Estado vigente — 8 de octubre de 2026: auditoría de indicios de IA (§7.1)

Se aplicó en las carpetas 01–08 y 13 la auditoría de indicios de IA de las Aclaraciones §7.1. El informe completo está en `Revision/auditoria_indicios_IA.md`.
- **Arreglos aplicados:** PUCV → Distribuidora Puelche (2026a–d); figuras PNG del SD5 enlazadas; limpieza de restos PDF/LaTeX; numeración de tablas, figuras y subtítulos del SD7; reescritura de notas de proceso; normalización de las 24 declaraciones de IA, con `[[REVISIÓN HUMANA]]` donde no hay revisión con nombre; tablas y cálculos nuevos en SD2, SD6 (valor ganado), SD7 (HH por etapa) y SD8 (FMEA top-5); stack del SD1 alineado con Laravel/PHP y Kotlin.
- **Pendiente del equipo:** completar `Revision/plantilla_revision_humana_IA.md` (204 celdas).
- **Contradicciones no corregidas por decisión del usuario:** cámaras, Starlink y sala; nombres de módulos e INT-04; meses de hitos en T-14 y T-16.
- **Pendiente antes de compilar:** replicar todo en LaTeX.

Sin commit.

## Estado vigente — 8 de octubre de 2026: SD13 consolidado

Se crearon `13_innovaciones/LAFROX-Subdocumento13.md`, `LAFROX-Subdocumento13-Anexos.md` (13.A contratos inn01–inn05, 13.B trazabilidad, 13.C indicadores y riesgos, 13.D observaciones) y `LAFROX-Formulario-T-19.md` (5 fichas × 17 campos), a partir de `innovaciones_corregidas.md`. Ese archivo de trabajo se conserva sin versionar y no es entregable. El SD13 se alinea sin cambios con los paquetes, meses y HH de T-14, T-15 y Anexo 7.D.
- Riesgos: se usa la escala 1–5 del SD8 con las fichas R8-23 a R8-29.
- Corrección técnica: se cita 10.920 mensajes diarios (SD4) y CloudWatch sin Grafana.
- Responsables: Chamorro y Henríquez dirigen hasta el mes 21. Después, los paquetes 8.3.x siguen con las siglas DAT e IMP del T-14, en el frente F8 de Castillo; Calidad aprueba los parámetros y Seguridad el bloque 4. No se cambiaron siglas en T-14 ni T-15.

Ajustes cruzados:
- T-12: RT-05.30 «Sí (E1)» mediante INN-03; RT-26.01 a 26.07 remiten al Capítulo 13 y al T-19; RT-26.08 «Sí (E1)» mediante INN-01, INN-02 e INN-03.
- SD5 y SD5-Anexos: 10.920 (28×174) y RT-05.30 ofertado.
- SD8-Anexos: R8-25 redefinida (avisos no confirmados o sin catálogo) y causas secundarias en R8-26, R8-27 y R8-29, sin cambiar P, I, D ni valor esperado; nombres completos en 8.F.
- T-16: mitigación de R8-25.
- SD7: nombres completos en la tabla de innovaciones.

Avisados y no tocados:
- §4.1.6 del SD4 sin contratos inn.
- Nombres M7, M8 y M9 en la Tabla 8 del SD4.
- Python/Django en la Tabla 1.1 del SD1.
- RF-09.06 y RF-08.05 del CSV.
- Impresoras 106 frente a 110.
- Contingencia 12.004 frente a 13.223 HH.
- La columna de revisión humana de la declaración de IA del SD13 lleva marcas «[Integrante: completar…]» que el equipo debe llenar antes de entregar. Sin commit.

## Estado vigente — 7 de octubre de 2026: cronograma por actividad y SD8 cuantitativo

SD7: T-15 §6 programa 564 actividades de 163 paquetes con entregable (≤80 HH, ≤1 quincena) con dependencias del Anexo 7.B (D-16/18/19 por interfaz, D-21b nueva), revisión Art. 18.3 y nivelación con la dotación del SD1; 59 paquetes de esfuerzo continuo por ocurrencia. Total 202.774 HH, peak 69 (mes 15). Reservas por hito en T-15 Tabla 5.2. El usuario aceptó: refuerzo de calidad con evaluadores subcontratados hasta 16/día (meses 9–12 y 16–18, SD6 §6.1.3), compra del CLIENTE dentro del mes siguiente a 5.1.2, y la calibración de escalas del SD8 (P: 5/20/40/60/80 %; I: 0/5/10/20/30 % del esfuerzo afectado). SD8: 32 riesgos, valor esperado 15.076 HH (contingencia adicional 12.004 HH), Monte Carlo con P(H9)=90 % y demás ≥97,7 %, P80 de todos los hitos dentro de su límite. Preferencia del usuario: mover lo menos posible los otros subdocumentos. Material del ramo en `clases + pmbok/` como consultor.

## Estado vigente — 5 de octubre de 2026

Limpieza adicional autorizada: se retira el archivo informativo de anexos del SD1 porque no incorpora anexos complementarios. `01_presentacion_empresa/` conserva cuerpo y T-6; SD3 y SD4 conservan sus tres entregables. El usuario solicita registrar toda esta limpieza en el commit `limpieza de archivos` y publicarlo en `alvaro-md`. Los originales eliminados permanecen recuperables en Git.

Rama comprobada: `alvaro-md`. El usuario autorizó ejecutar y publicar el plan SD3–SD4 con los quince actores de sistema validados con el redactor del SD3, implementado en `26c345c`. SD3 se actualizó desde las inclusiones activas de `Descargas/03_esquema_solucion_alcance/03_esquema_solucion_alcance`; se añadió 3.4.2.1 y matriz de actores, realizada en la lógica del SD4 y Anexo 4-N. CD-05 está integrado en reglas, contratos, volumen y pruebas. Por solicitud posterior, SD3 y SD4 conservan solo cuerpo, anexos y formulario; se eliminan manifiestos de capítulo, registros auxiliares y copias por partes. Editar directamente los tres entregables del capítulo, sin recrear auxiliares. Física, centros de datos, memoria y T-11 conservan su contenido. `md para drive/` es una exportación no versionada y antigua; no forma parte de esta limpieza. Los textos siguientes son historia de sesión.

Dependencias preservadas tras retirar los registros del capítulo: SD2 S-09 y RF-03.11/12 permiten precio al despacho con excepciones mientras SD3 RNG-08 conserva precio pactado; requiere decisión comercial coordinada. CD-05 añade 2N + 2L mensajes y debe incorporarse al dimensionamiento físico; las pruebas AL-STOCK-01 y AL-ACT-01 están descritas, no ejecutadas. Las figuras históricas requieren cotejo de actores/etapas y las aclaraciones cuestionan recortes. La contingencia manual no acredita los 96 despachos críticos. Fechas ADR, revisión humana final, FinOps y el límite residual de DR conservan su estado pendiente; no declarar conformidad total por la limpieza. La evidencia documental original permanece recuperable en el commit `26c345c`.

Este archivo mantiene el contexto mínimo y vigente para trabajar en la rama `branch-md` del repositorio LafroX sin completar vacíos mediante suposiciones. Debe leerse junto con `AGENTS.md` al iniciar o retomar una sesión.

## Identidad y protocolo

- Proyecto y proponente: **LafroX**.
- Licitación académica ficticia: **TFEP-01/2026, Caso 02 — Logística, Distribuidora Puelche S.A.**
- Toda respuesta final del asistente comienza exactamente con `## LafroX`.
- El trabajo y los documentos se redactan en español.

## Regla obligatoria de integridad de branch-md

- Esta es la rama `branch-md` del repositorio LafroX. Solo se crean, editan y versionan documentos `.md`; los metadatos internos de Git son la única excepción.
- Toda petición de crear, editar, compilar, renderizar o convertir contenido a LaTeX debe rechazarse tajantemente dentro de esta rama. No crear archivos `.tex`, `.cls`, `.sty`, plantillas, comandos de compilación ni derivados PDF.
- Respuesta requerida: «No realizaré trabajo en LaTeX en branch-md: esta rama es exclusivamente Markdown y debo preservar su integridad. Puedo resolver la petición en Markdown».
- No cambiar automáticamente de rama, importar archivos LaTeX ni escribir en otro checkout para eludir esta restricción.
- Antes de editar, comprobar que la rama activa sea `branch-md`. Antes de registrar cambios, comprobar que todos los archivos a versionar terminen en `.md`.
- Leer `compct/CONTEXTO_SESION.md` al iniciar o reanudar una sesión. Cada respuesta final comienza exactamente con `## LafroX`.

## Objetivo vigente

Este repositorio es una base documental exclusivamente Markdown para crear, mantener y revisar los Subdocumentos 1, 2 y 3. Incluye sus anexos, los Formularios T-6 y T-12, las Bases rectoras, los catálogos originales de requerimientos y el prompt de revisión.

No contiene arquitectura, subdocumentos 4–14, históricos, binarios, plantillas LaTeX ni herramientas de generación. Una referencia a esos materiales identifica una dependencia futura; no demuestra que el material esté disponible.

## Fuentes de verdad y precedencia

1. `Bases/Bases_Administrativas.md`.
2. `Bases/Bases_Tecnicas_Transversales.md`.
3. `Bases/Caso_02_Logistica.md`.
4. `Bases/aclaraciones-licitacion.md`, posterior y obligatoria para estructura, archivos y presentación.

El caso puede endurecer un requisito transversal, pero no rebajarlo. Ante una contradicción, se registra la inconsistencia o una consulta al mandante; no se corrige silenciosamente.

## Estado confirmado del repositorio

- Las cuatro Bases son copias íntegras de las fuentes del repositorio LafroX al momento de crear este repositorio.
- El Subdocumento 1, su anexo y el Formulario T-6 están convertidos a Markdown y permanecen en archivos separados.
- El Subdocumento 2 y sus anexos están convertidos a Markdown y permanecen en archivos separados.
- Hay diez figuras transcritas como descripciones textuales: un organigrama, seis procesos AS-IS y tres esquemas del Subdocumento 3.
- `Requerimientos/Consolidado_RF.md` contiene 134 registros provenientes del CSV original.
- `Requerimientos/Consolidado_RNF.md` contiene 24 registros provenientes del CSV original.
- `Requerimientos/Requerimientos_Bases.md` conserva las 61 filas físicas y las dos familias de columnas del CSV original.
- `Revision/prompt_revision_comision_informe2.md` adapta la revisión a evidencia por archivo y sección. Las verificaciones exclusivas del PDF quedan pendientes.
- Estado vigente: rama `branch-md` del repositorio LafroX. La copia independiente `LafroX-Markdown` es el origen de importación, no la rama de trabajo. No se ha publicado esta rama.

## Controles contra alucinaciones

Antes de afirmar un dato, requisito, estado o decisión:

1. Buscarlo en las cuatro Bases respetando su precedencia.
2. Verificar si aparece en los subdocumentos o catálogos incluidos.
3. Citar el archivo y la sección que lo sostienen.
4. Si la fuente no está incluida o el dato no está definido, escribir `no verificable con el material disponible` o registrarlo como vacío, supuesto o consulta.
5. No presentar como acreditados los proyectos, certificaciones, alianzas, contactos o antecedentes corporativos del Subdocumento 1 sin evidencia documental externa.
6. No completar celdas vacías de los catálogos sin una fuente verificable.
7. No declarar aprobada la presentación formal: paginación, firma, folio, tipografía y legibilidad se comprueban únicamente en los PDF finales.

## Convenciones de mantenimiento

- Solo se agregan archivos `.md`, además de los metadatos internos de Git.
- Subdocumentos, anexos y formularios permanecen separados.
- Las figuras enlazan su imagen real; el PDF se compila desde LaTeX. Ver la regla de AGENTS.md sobre indicios de IA (Aclaraciones §7.1).
- Toda ampliación del alcance se registra primero en este archivo, en `README.md` y en `MANIFIESTO.md`.
- Después de cada cambio sustantivo se actualiza la sección siguiente para permitir una reanudación segura.

## Último estado de trabajo

**Fecha:** 2026-09-28.

**Completado:** importación de los 17 documentos Markdown a `branch-md`, preservando el contenido documental e incorporando la prohibición explícita de trabajar en LaTeX. La comparación con `tablas_anexo` del Subdocumento 3 detectó diferencias de cantidades, nombres y códigos; los catálogos Markdown no se sustituyeron.

**Siguiente paso:** continuar la revisión o edición de los Subdocumentos 1, 2 y 3 usando únicamente las fuentes incluidas. Cualquier incorporación de arquitectura o de los Subdocumentos 4–14 requiere ampliar expresamente el alcance.

## Última actualización: incorporación del Subdocumento 3

Petición vigente: trasladar todo el material relevante del Subdocumento 3 en exactamente tres documentos Markdown, conservando sus errores. Se incorporaron cuerpo, anexos 3.A–3.K, las 14 tablas de la colección complementaria `tablas_anexo`, tres figuras transcritas y T-12. El T-12 mantiene 174 RF, 90 RNF y 374 RT. La colección complementaria conserva 90 RF y 40 RNF aunque anuncia 91 y 41. Estas versiones no fueron reconciliadas ni sustituyen los CSV convertidos en `Requerimientos/`. Próximo paso: revisión del contenido si el usuario la solicita; no dar por corregidas las discrepancias.

## Ampliación autorizada — ejecución de mejora SD5, 2026-10-03

La rama de esta copia es alvaro-md. El usuario autorizó ejecutar el plan SD5 en el checkout de alvaro-modelo-y-gestion-de-datos y sus correcciones coordinadas. Esta copia permanece exclusivamente Markdown. SD1 corrige la responsabilidad específica del líder de desarrollo a Laravel/PHP; SD4 conserva fuente histórica y añade complemento CD-05 de coordinación de reserva y custodia. T-12 y los catálogos originales no se renumeran ni amplían; RT-05.10/24/30 BTT permanecen no ofertados.

## Revisión de la Comisión — Informe 2, 2026-10-07

Se aplicó `Revision/prompt_revision_comision_informe2.md` a todo el repositorio, sin comprobaciones de forma; el resultado está en `Revision/revision_comision_informe2.md`. Total 1,2 sobre 97 % evaluado: SD1, SD3, SD4, SD6, SD7 y SD8 quedan en 0 por indicios del §7.1 (declaración de IA «Alto» sin revisión humana y notas de proceso en el texto); SD2 queda en 20 por la contradicción de S-09 con el SD3; SD5, SD9 y SD13 no están presentados. No se modificó ningún entregable.

## Revisión de coherencia del SD8 — 2026-10-07

Se corrigió el SD8 (cuerpo, anexos y T-16) según el plan aprobado: Figura 8.1 (RBS) derivada de las 32 fichas del Anexo 8.A; contingencia adicional de 13.223 HH, porque la capacidad protegida E1 sólo absorbe R8-02, R8-04 y R8-14 (1.853 HH); hitos H6, H7, H11 y H12 justificados como no simulados; notas de redondeo y de muestreo de la Tabla C.4; fuentes «Aclaraciones §11, 8.2»; referencias 2026a–d, ISO 31000 e IEC 60812 citadas en el texto; se retiraron las notas de proceso y las menciones al SD5, y se eliminaron E8-11 y E8-12 (las condiciones siguientes se renumeraron). Por decisión del usuario se trajeron desde `LafroX_Markdown` el SD2-Anexos, el SD3, el SD3-Anexos y el T-12 con la regla única de precio acordado al capturar el pedido (S-09, RNG-08, RF-03.11/12) y la reversión del SD3 alineada con el SD7. Pendientes avisados: revisión humana real de las declaraciones de IA, Tabla 6.3 del SD6 (sala en mes 5 frente a meses 3–4 del T-15) y brecha de RPO del SD4. Sin commit.

## Sincronización del Subdocumento 4 — 2026-10-07

Los tres entregables Markdown de `04_arquitectura/` se actualizaron desde las fuentes LaTeX vigentes del checkout hermano `LafroX` mediante `00/herramientas/tex2md.py`. El cotejo previo quedó en `LafroX/00/trazabilidad/ACREDITACION_LATEX_MD_SUBDOC4_2026-10-07.md`. La sincronización incorpora la redundancia activo/en espera de Concepción y cross-docking, T-11, 230.252/353.333 mensajes diarios, 9 terminales de cross-docking, 2.283 contactos/mes de capacidad base de mesa y el retiro de dos importes históricos. Los 26 enlaces de figuras del cuerpo apuntan ahora a los archivos de la revisión LaTeX publicada `d397c30`, incluidos los tres diagramas físicos actualizados; ya no dependen de rutas al checkout hermano. Se eliminaron además un resto `A.table` de los anexos y siete prefijos `l` espurios en categorías del T-11. No se creó LaTeX ni PDF en `rama-md`.

## Estado vigente — 11 de octubre de 2026: alineación del cuerpo de SD9 con las Bases

Por autorización del usuario se corrigió únicamente `09_plan_calidad/LAFROX-Subdocumento9.md` en `rama-md`, más seguimiento `odd/tasks/sd9-bases-alignment.md` y esta entrada. Las Bases prevalecen sobre clases, PMBOK y el extracto del compañero. MTTR usa media mensual contractual (BA 78.3), separada de los máximos individuales de resolución de BA 78.2; presupuesto de error según mes calendario real, con mantenimiento aprobado excluido de la indisponibilidad, no descontado automáticamente del denominador (BA 79.4), y sin autorizar indisponibilidad en despacho. DRE delimita versión, corte y defectos conocidos; sin casos no acredita cumplimiento.

Se corrigió la explicación de 31 sin prueba propia: 22 No cumple (0 RF, 2 RNF, 20 RT) y nueve absorbidos; se conservan 645 ID, 614 con prueba propia y 1.308 casos. Las 10.848 HH se presentan como grupos de paquetes de calidad, no categorías puras de prevención/evaluación; 3.315,2 HH son tres riesgos seleccionados, no toda la no conformidad ni prueba de eficiencia. Se retiraron garantías absolutas de caminos/recurrencia y cierres definitivos de verificación/validación. La certificación de H7/H12 incluye pruebas aplicables de BTT 20.1 y RT-11.20, DR real y accesibilidad; el techo de 2.150,4 HH no acredita capacidad por especialidad ni reserva disponible.

Verificación local: script de lectura y cláusulas, salida 0; aritmética y conteos vigentes cotejados con T-12/9.C; 25 encabezados, 10 bloques Mermaid y 10 marcadores humanos preservados frente a la instantánea original; `git diff --check` sin diagnóstico tras editar la fuente. Documento de tarea y espejo inicial Engram #116 verificados antes de fuente; espejo actualizado y evaluación final a cargo del coordinador. Commit pendiente por instrucción expresa; sin push ni cambio de rama.

Límites: no se inventaron fechas, HH ni división de paquetes mixtos. SD7/T-13 aún requieren autorización para calendarizar y nivelar las recertificaciones H7/H12; SD4 conserva indicadores que necesitan armonización posterior. No se editaron anexos, formularios, Bases, figuras ni planillas. No se acredita coherencia global, pruebas ejecutadas, conformidad final ni revisión humana; se preservan sus marcadores.

Cierre local SD9-01 confirmado por el coordinador: spot-check estructural y `git diff --check` conformes. Evaluación nativa con inventario explícito de la tarea: `passive/non_executable_only`, tres rutas, 95 líneas; `review_due: false` por `passive`, sin revisor ni consentimiento. Las dependencias externas siguen abiertas. Se autoriza una unidad local `docs(quality): align SD9 with tender requirements`, limitada a SD9, su tarea y contexto en `rama-md`; el resultado y la identidad se registrarán en el espejo tras comprobar permisos de Git. Sin push ni cambio de rama.

## Corrección coordinada SD6–SD7–SD9 — 11 de octubre de 2026

Por autorización del usuario se corrigieron los trece hallazgos en SD9 v_nueva y se propagó sólo a SD7 (T-14/T-15/cuerpo), SD6 (coordinación de especialistas) y sus tres resúmenes. G5 contractual permanece H7/H12; Producción supervisada exige control previo H6/H11. Tabla9.8 doce tipos; cinco condiciones físicas y desconexión separada; aceptación doce E1/dos E2 y dos resultados diferidos. Calendario efectivo corrige reservasH1/H2/H3/H4/H5/H8/H9/H10 a5/11/16/18/34/4/19/23, con recepciónH3 el22-06; escenario nominal y probabilidades no se presentan como efectivos.

Reestimación por fase/rol: DR operacional7×80=560; intrusiónE1/E2=320/160; restauraciones13–20=128SRE adicionales, sin reducir coberturaNOC/mesa. Línea base217.543=205.135+9.336+3.072; calidad11.136; curva conservadora máximo69 mes15. Se retiraron cifras/IDs copiados del SD8 sin asignar cero al esfuerzo por fallas. Asignación nominal, capacidad por rol/día/mes y PERT efectivo siguen pendientes; no se acreditan factibilidad, pruebas ejecutadas ni revisión humana.

ChecksPython aritmética56meses/12tipos/44informes y calendario conformes; git diff --check salida0. Assess con inventario explícito medium por AGENTS previo;RDDOFF conservado, sin transición. Estado local en odd/tasks/sd679-quality-coherence.md y espejo Engram; dos unidades,exception-ok autorizado. Sin commit/push/PR; cierre sujeto a revisión independiente y staging que preserve cambios previos. SD8/SD1/SD4/Revision no editados. Comunicar base nueva a responsableSD8, no copiar sus reservas.

Corrección acotada del bloqueo independiente: T-15,4.5 ya no copia reservas/total movilizable ni garantiza cobertura; estima respuesta por evento/especialidad, valida capacidad nominal y requiere autorización. Escenarios5.1–5.4 conservados como históricos nominales no reconciliados; gobierno usa reserva efectivaT-17. Ningún cambio al SD8 ni a otros entregables. Aritmética56meses/217.543/205.135/11.136/44informes y ausencia de garantías antiguas conformes; git diff --check salida0. Pendiente rechecado independiente y commits.

Cierre documental confirmado por verificador independiente (incluido rechecado de la corrección de T-15) y spot-check del coordinador. Implementación/comprobaciones Q1/Q2 conformes; dotación nominal y PERT efectivo siguen pendientes. Commits no realizados: no se retuvieron bytes de baseline que separen hunks propios de importación SD9 previa/T-14 del usuario/AGENTS/contexto. Se evitó staging de procedencia mixta y se preservó todo el estado; no es rechazo de permisos. Gate de commits sigue pendiente, sin afirmar hashes de baseline ni diff exclusivo comprobados. No se publicaron cambios.
## Estado vigente — 11 de octubre de 2026: Excel para paginar citas del SD9

El usuario pidió una hoja editable para completar páginas de los PDF asignados y devolverla para actualizar citas. Creada fuera del repositorio Markdown, en Subdoc/outputs/citas-sd9/LafroX_SD9_citas_paginas_por_completar.xlsx: 371 registros externos (citas y menciones normativas) en «Citas sin página», 207 remisiones internas opcionales y 43 fuentes en «Fuentes y PDF». No se duplicaron 21 referencias que ya indicaban p./pp. (su presencia no implica verificación independiente). Campos manuales amarillos: PDF y versión por fuente; página impresa, página del visor, acción y observaciones por cita. Se conservaron ID estables, contexto literal, archivo/sección/línea y SHA-256 de los cuatro Markdown vigentes; manifiesto de reimportación junto al libro. No se modificaron entregables ni se asignaron páginas. Al recibir el Excel, aplicar sólo datos suministrados tras comprobar fuente/texto, resolver códigos RT ambiguos y después sincronizar la publicación autorizada. Alcance: SD9 v_nueva, no toda la oferta.

## Aclaración vigente — Excel sólo de citas a las Bases

El usuario precisó que el Excel de páginas debe contener sólo citas a las Bases. Modificado el mismo archivo Subdoc/outputs/citas-sd9/LafroX_SD9_citas_paginas_por_completar.xlsx: 317 registros BA/BTT/Caso, sin PMBOK, ISO, OWASP, leyes ni remisiones internas; catálogo reducido a BA, BTT, Caso y códigos RT de fuente ambigua (confirmar BTT/Caso por fila). Eliminada la hoja de remisiones internas. Conservados IDs, ubicaciones, contexto y cualquier entrada manual de las filas retenidas; manifiesto sincronizado. Esta aclaración reemplaza el alcance ampliado de 371+207 registros del párrafo anterior. Los entregables SD9 permanecen intactos.

## Actualización 2026-10-11 — paginación de citas SD9
- Alcance solicitado: sólo Bases Administrativas y Bases Técnicas Transversales; Caso 02 y fuentes externas excluidos.
- PDF originales en Downloads/Bases Caso: BA 77 páginas físicas, BTT 51; versión 1.0 de 18-08-2026. Escaneos sin texto; revisados mediante OCR y comprobaciones visuales. Folio impreso = posición del visor menos 1 en todas las páginas numeradas.
- Hoja Subdoc/outputs/citas-sd9/LafroX_SD9_citas_paginas_por_completar.xlsx actualizada: 205 registros, 199 referencias con páginas y 6 menciones generales No requiere. Folio impreso y página visor separados. Manifest con hashes de PDF y fuentes Markdown.
- Se corrigió extracción de cuatro artículos BA en contextos mixtos y se excluyó una falsa referencia BTT de comparación. El estado previo de 317 registros queda reemplazado.
- Paginación todavía NO aplicada a Markdown/LaTeX/PDF. No se modificaron los cambios ajenos de SD13.

## Cotejo PDF de citas, folios y CMMI SD1 — 11 de octubre de 2026

Usuario pidió revisar muy bien los tres ajustes usando PDF originales, sugiriendo otras ramas/SD4. Localizados BA77p/BTT51p/Caso41p en FEP; originales escaneados sin texto, OCR Windows fuera de rama-md para localizar y verificación visual de páginas pertinentes. Folio impreso=visor−1 en páginas consultadas. Matriz completa en Revision/cotejo_citas_Bases_folios_CMMI_SD1.md con hashes, ubicaciones fuente y páginas impresas/visor. BA Art16p11,17p12,19p14,34p22,39p25,72p38,76p39,78.2p40,T6p56. BTT RT02.02p6,11.20p24,15.2/15.09p28,19.2pp33–34,19.02/03p33,21.02p35,23.01–10p39; disponibilidad6.1p14 y7.2pp17–18. Caso2.2–4pp4–5,10p19,14.2p25,21.06p27.

Hallazgos nuevos: cita del99,95% enTabla1.5 atribuye incorrectamente aCaso cap10; fuente BTT6.1/7.2. Controlcambios cita19.02 pero corresponde19.03+BA72; dividir citas facultades/control. FoliosT6 pp4–6 confirmadosgiradosizquierda; causa landscape+fancyhdrvertical, proponer ajuste localT6no clasecompartida. FuenteCMMIprimaria2020 distingueSCAMPIV1.3bA yV2Benchmark; propuestaDevelopmentV2Nivel3Benchmark, noactualizarversión automáticamente ni autenticar58190. RenovaciónBenchmarkyreferenciacorrecta; documentaciónmétodonopruebaacreditaciónLafroX. Revisiónonly:noeditentregables/fuentes/PDF,nocommitpush; registrosMDactualizados. Memoriaagentesuspendidaruntimeausente. Siguiente:aplicarsiusuariopidecorregir,sinfirmas/revisionesinventadas.

## Estado Git SD1 comprobado — 11 de octubre de 2026

Consulta del usuario sobre sincronización/commit/push, sin orden de publicar. Consulta directa ls-remote: rama-md f4f2ab3014185b1a11bf6f73228b26d1cf8f03af coincide HEAD local; ese commit incluye SD1MD S1-18 y ambos registros de auditoría, sin cambios pendientes en tres entregables SD1MD. LaTeX HEAD/origin permanece145fedec927a09fc649e070e33f5f3c29ce66aa8; contenido.tex y LAFROX-Subdocumento1.pdf siguen modificados locales S1-18, no comiteados/publicados. Por tanto sincronización de contenido local vigente comprobada, pero versiones publicadas de ambas ramas no están alineadas con los últimos cambios. Correcciones de citas/folios/CMMI sólo revisadas, no aplicadas. No se creó commit ni push en esta consulta. Memoriaruntimeausente:registro local.

## Publicación de capacidad instalada SD1 — 11 de octubre de 2026

Objetivo y autorización: usuario ordenó «comitea y push» tras comprobar estado de las dos ramas. Unidad publicada: sólo contenido.tex y LAFROX-Subdocumento1.pdf (S1-18) en LafroX-Subdoc1-LateX; commit8900d674cee739779ee574b23c77ad08b6d0ce55, pushsalida0 yls-remotecoincide. Hashesfuente31741d4fa65ee275fe8afb5d44e554509217ccac8fe509174590f06aa8c34ec3 yPDFdce24e00a540abf383a394e4c0357adc67f591f3d94f35d964364c9047c4abae coincidenversiónauditada. Stagingexactodosarchivos,diff-checkconforme; sinrecompilarporquefuente/PDFnoalteradosdesdeverificación. RollbackacotadoadosarchivosS1-18; noanexos/T6/clase/imágenesniotrasfuentes. MarkdownSD1vigente ya publicadoenf4f2ab3; estaunidadMDsólopublicaregistrocontextoSD1. CambioajenoSD3fuera staging. Próximos:citas/folios/CMMIsiguenrevisadosnoaplicados,firmas/revisiónhumanapendientes. No afirmarentrega100%conforme. Memoriaruntimeausente:resumenlocalpersistido.

## CMMI corregido y demanda de mesa cuestionada — 11 de octubre de 2026

Usuario pidió aplicar correcciónCMMI en SD1 y luego cuestionófuertemente2000contactos/mes. SD1contenido.tex en checkoutLaTeX y SD1MD enrama-md: tres «SCAMPI A» sustituidos por «Benchmark» (antecedente,renovación,referencia); noalterarID58190 ni fechas ficticias. PDFcuerpo recompilado3pasadasLuaLaTeXno-shell-escape,21páginas,3Benchmark,0SCAMPI, sinOverfull/refundefined; inspeccionadaspp14/15/20. No commit/push solicitado. No se tocó T6/anexos/clase. La coherencia terminológica no autentica certificación.

Revisióncifra: CasoPDForiginalcap14.2p25 deja contactosmesa «a estimar». SD4Anexo4-W.7 SV-06 calcula (640trabajadores+~160conductoresexternos)×2,5contactos/persona-mes=2000. Factor2,5,25%hora cargada y22,14díasequivalentes basados31000pedidos/1400entregas no sustentados porregistroservicio; implican30contactos/año/personay~77/díaa26días. Contactosnoequivalenafallas, peronojustificaestacantidad; universo800excluye14200clientes+180proveedores sin definirfrontera de mesa. DetalleRevision/revision_demanda_mesa_SD1_SD4.md. No cambiarbaseporotra inventada ni propagar aSD4/SD7/T15 sin acordar escenario; PDFsT15excluidosporinstrucciónvigente. No afirmar2000demandaobservada ni validada. CambiosajenosSD2/SD3/contextopreservados. Memoriaagent-attributed suspendida identidadruntimeausente; resumenaquí.

## Declaración de IA y T-6 del SD1 — 11 de octubre de 2026

Por petición explícita se cerró la matriz de uso de IA en el cuerpo MD del SD1: texto «Alto» en las secciones 1.1–1.6 y T-6; diagramas «Bajo» en 1.2 (sección de la figura) y «No aplica» en las demás filas; revisor indicado por el usuario: Alex Aravena. Se eliminó la fila de anexos y el archivo Markdown que solo anunciaba que no había anexos complementarios. El T-6 ya no lleva su propia declaración de IA; queda su fila de trazabilidad en la tabla consolidada del SD1. Se aclaró la fila temporal del T-6: los años expresan el período de implementación y el año desde el cual sigue activa la operación, preservando los años declarados. No se modificó la fuente LaTeX ni se compiló; tampoco hubo commit/push.

Por instrucción posterior se sincronizó el checkout `../LafroX-sd1-latex` (rama `LafroX-Subdoc1-LateX`): se aplicaron los mismos estados de IA y la aclaración temporal del T-6, se retiró la declaración duplicada del T-6 y se eliminaron `anexos.tex`, `LAFROX-Subdocumento1-Anexos.tex` y su PDF vacío. El cuerpo SD1 y el T-6 recompilaron con LuaLaTeX (21 y 7 páginas); la extracción de texto confirma etiquetas temporales y revisores; sin errores ni cajas Overfull/Underfull. El cuerpo conserva una advertencia de inclusión de Figura 1.1 (PDF fuente 1.7 frente a máximo 1.5). La edición previa CMMI Benchmark de SD1 también permanece incorporada. Se preservaron imágenes de revisión no versionadas y otros cambios ajenos del checkout. Los cambios SD1 quedaron comprometidos en ambas ramas; publicación remota pendiente. Los cambios ajenos de rama-md siguen fuera del staging.
## Firma manuscrita en portadas LaTeX SD1–SD3 — 12 de octubre de 2026

**Autorización:** el usuario pidió usar la firma presente en `FIRMA_Alex_Aravena_transparente.png` de `rama-md` y añadirla a las portadas LaTeX de los Subdocumentos 1, 2 y 3, compilando y revisando el resultado. Se verificó `rama-md` antes de operar. La imagen fuente quedó intacta y sin versionar; no se crearon ni editaron archivos LaTeX/PDF en `rama-md`.

**Destinos y cambio:** se comprobaron las ramas `LafroX-Subdoc1-LateX`, `LafroX-Subdoc2-LateX` y `LafroX-Subdoc3-LateX`. En cada checkout se copió la imagen de firma y se ajustó solo `lafrox-portada.tex` para colocarla sobre la línea, conservando debajo el nombre/cargo del representante. La plantilla se usa en siete salidas activas: SD1 y T-6; SD2 cuerpo y anexos; SD3 cuerpo, anexos y T-12. No se modificaron las demás fuentes LaTeX. Los cambios locales preexistentes de SD2/SD3 y las imágenes de revisión de SD1 se preservaron.

**Compilación y revisión:** cada una de las siete salidas se compiló tres veces con LuaLaTeX y `--no-shell-escape`, salida 0 en todas. Páginas finales: SD1 19; T-6 7; SD2 cuerpo 29 y anexos 20; SD3 cuerpo 34, anexos 168 y T-12 261. Los logs finales registran la carga del PNG en las siete compilaciones; la revisión de las siete primeras páginas confirmó tinta visible sobre papel blanco, en el espacio de firma, sin recorte ni solapamiento con la línea o los datos identificatorios. El filtro final no encontró errores TeX, cajas Overfull ni referencias indefinidas. No se cambiaron las fechas de emisión ya existentes (SD1/T-6 muestran 5 de octubre). La imagen rasterizada representa visualmente la firma, pero no es una firma electrónica criptográfica.

**Publicación:** sin commit ni push. Se preservaron el estado y los cambios previos; el único cambio en `rama-md` de esta operación, aparte del PNG fuente preexistente, es este registro de contexto.

### Publicación de la firma en LaTeX SD1–SD3 — 12 de octubre de 2026

**Autorización:** tras revisar el alcance, el usuario indicó «comitea los puros latex». Se publicaron únicamente los checkouts y ramas LaTeX SD1, SD2 y SD3; no se creó commit ni se hizo push de `rama-md`.

**Commits y verificación remota:** SD1 `9775a1161d564bf240ee0751f1f0068626aaea5a` (`LafroX-Subdoc1-LateX`); SD2 `ed6551f1498b366ca49d95596a11288fd3012fec` (`LafroX-Subdoc2-LateX`); SD3 `421454011891cd8110707ab35032086889cacb47` (`LafroX-Subdoc3-LateX`). Push de las tres ramas terminó con salida 0, sin force-push; después se verificó por fetch/ls-remote que cada HEAD local coincide con su rama remota. El push SD3 incluye también el commit local previo `ddee65e` que ya estaba ahead de origin.

**Alcance de los commits:** SD1 incluye plantilla de portada, PNG de firma y PDFs compilados del cuerpo y T-6. SD2 incluye los cambios LaTeX/PDF que ya estaban pendientes en ese checkout, además de portada, PNG y PDFs compilados. SD3 incluye los cambios LaTeX/PDF que ya estaban pendientes (incluidas figuras PDF), además de portada, PNG y PDFs compilados. En SD1 se excluyeron todas las imágenes PNG de revisión; no se añadieron archivos de revisión ni Markdown a ninguno de los commits. Los siete PDFs se habían compilado y revisado visualmente antes de publicar.

**Preservación:** siguen sin publicar los cambios de Markdown en `rama-md`, junto con su firma PNG local no versionada y los demás cambios preexistentes. Después de actualizar referencias remotas, `rama-md` aparece cuatro commits detrás de origin; no se hizo pull, rebase ni cambio de rama para no mezclar los cambios concurrentes. El contexto se actualiza aquí como registro local y queda fuera de los commits LaTeX.

## Revisión humana de declaración de IA SD1 — 12 de octubre de 2026

**Autorización y alcance:** el usuario pidió registrar las revisiones aportadas para 1.1–1.6 en la declaración de uso de IA del cuerpo SD1 Markdown y LaTeX. Se verificó `rama-md`; el checkout LaTeX externo quedó en `LafroX-Subdoc1-LateX`. No se editaron A-6, T-6 ni otras secciones.

**Cambios:** `01_presentacion_empresa/LAFROX-Subdocumento1.md` y el `contenido.tex` externo ahora identifican a Alex Aravena y el objeto revisado en cada fila 1.1–1.6: visión/productos/servicios; organigrama/áreas/equipo/antigüedad; modelos de gobierno; experiencia/proyectos; estructura/jerarquía del proyecto; alianzas. Se corrigió el typo «verifcó». El nivel de texto permanece **Alto** en todas esas secciones; diagramas queda **Alto** sólo en 1.2, donde aplica a la Figura 1.1, y «No aplica» en las demás.

**Verificación:** diff-check conforme en Markdown y fuente. `contenido.tex` se compiló tres pasadas con LuaLaTeX y `--no-shell-escape`, todas con salida 0; PDF del cuerpo con 19 páginas, sin errores, cajas Overfull/Underfull ni referencias indefinidas. La extracción confirma las seis revisiones y los niveles; inspección visual de p. 19 confirma que la tabla completa cabe sin cortes y sigue legible. El PDF actualizado permanece sólo en el checkout LaTeX. Se conservaron imágenes de revisión preexistentes sin versionar. Sin commit ni push.

## Revisión de coordinación SD2 Markdown–LaTeX — 12 de octubre de 2026

**Autorización y límites:** a petición del usuario se revisó exhaustivamente la coordinación del Subdocumento 2. Se confirmó `rama-md`; el checkout `../LafroX-sd2-latex` está en `LafroX-Subdoc2-LateX`, HEAD `ed6551f1498b366ca49d95596a11288fd3012fec`, limpio y en seguimiento de origin. `rama-md` está cuatro commits detrás de origin, pero el diff remoto no incluye los dos archivos Markdown del SD2. Revisión de solo lectura: no se editaron fuentes LaTeX ni entregables, no se recompiló y no hubo commit/push.

**Cotejo de contenido:** no se detectaron diferencias sustantivas de texto, cifras, títulos, filas de tablas, referencias o identificadores entre cuerpo/anexos Markdown y `contenido.tex`/`anexos.tex`. Coinciden las seis leyendas de figura, el catálogo F-01–F-14 y RNF, S-01–S-16, SP-01–SP-03, E-01–E-09, R-01–R-12, los 19 actores, los ocho sistemas legados y las declaraciones IA de cuerpo. Las bibliografías tienen 21 entradas en cuerpo y cinco en anexos. La redacción de los seis análisis AS-IS que antes figuraba pendiente en LaTeX ya coincide en los archivos actuales.

**Hallazgos no conformes con “100 %”:** los seis enlaces de figuras del Markdown usan `figuras/figura 2.x.pdf`, pero no resuelven desde `02_problema_necesidad`; los PDF fuente existen en el checkout LaTeX, no en esa ruta. En los PDF compilados del cuerpo, pp. 15 y 21, figura y leyenda están horizontales, pero cabecera, pie y folio quedan girados verticalmente. La Tabla 2.A.9 conserva `[[REVISIÓN HUMANA]]` idéntico en Markdown y LaTeX; no es deriva entre versiones, pero bloquea la entrega hasta revisión humana real.

**PDF y presentación:** cuerpos/anexos actuales: 29 y 20 páginas carta. Se revisaron visualmente portadas, páginas con Figuras 2.1–2.6, tablas finales y el recorrido de anexos (pp. 4–20); no se vio recorte en esos renders. Los logs no muestran `Overfull` ni error fatal, pero contienen avisos `Underfull \hbox` y `Infinite glue shrinkage found in box being split`, por lo que no se describen como logs limpios. No se cambiaron archivos LaTeX. Engram no estuvo disponible en las herramientas de esta sesión; registro conservado aquí.
**Siguiente paso:** sólo si el usuario autoriza correcciones, reencaminar los seis enlaces a imágenes realmente accesibles para Markdown, orientar cabecera/pie/folio de pp. 15 y 21 sin cambiar las figuras, y completar el marcador de la Tabla 2.A.9 únicamente tras la revisión humana efectiva. Revisar de nuevo logs y renders; no publicar sin autorización.

## Obs. 20 SD3: prioridades sin cambios — 12 de octubre de 2026

El usuario decidió no rebajar prioridades para no propagar cambios a SD9, T-13 y Anexo 9.C.2 el día de la entrega. Se mantienen 56 críticos, 163 altos y 43 medios. Se añadió en SD3 §3.2.3 un párrafo que justifica la concentración (Caso cap. 13.1; familias F-12 y F-14 en Media; «Media» no es optativo). La fila 20 de `Revision/trazabilidad_Informe1_Informe2_SD3.md` quedó actualizada. Los diez cambios analizados en `Revision/revision_prioridades_SD3_Obs20.md` quedan como opción no aplicada. Sin commit.

### Obs. 17, 28 y 42 del SD3 — 12 de octubre de 2026

A pedido del usuario se agregaron en el MD del SD3: la síntesis de los atributos de calidad al final de §3.4.2 (interoperabilidad, escalabilidad, desempeño y seguridad, con sus RNF, y remisión al SD4 4.1.3.7 y 4.2.6); el enfoque SRE y la automatización en §3.4.5 (IaC SD4 4.2.3, alertas SD4 4.1.3.8, RNF-19.02, RNF-16.02); y la redacción en oraciones completas de D-08, D-09, D-11 y D-12 (Anexos, Tabla 3.A.9). La trazabilidad deja 42 de 43 observaciones documentadas, con la Obs. 3 como única bloqueante. Las filas 17, 20, 28 y 42 quedan pendientes de traslado al LaTeX: no se tocó el checkout LaTeX y no se hizo commit.

### Traslado al LaTeX del SD3 — 12 de octubre de 2026

**Autorización:** el usuario pidió en el chat «alinéalo con el latex». **Alcance:** trasladar los cambios del MD de las Obs. 17, 20, 28 y 42. **Destino:** checkout `../LafroX-sd3-latex`, rama `LafroX-Subdoc3-LateX`, en `contenido.tex` (§3.2.3, §3.4.2 y §3.4.5) y `tablas_anexo/decisiones.tex` (D-08, D-09, D-11 y D-12). Se conservaron los cambios locales previos del checkout. **Resultado:** `latexmk -g` compiló sin errores el cuerpo (35 páginas, Figura 3.4 sigue horizontal) y los anexos (168 páginas); el T-12 no cambió. La trazabilidad del SD3 quedó actualizada con las nuevas páginas: 42 de 43 observaciones documentadas, con la Obs. 3 como única bloqueante. Sin commit en ninguno de los dos checkouts.

### Declaración de IA SD3: «No aplica» en diagramas — 12 de octubre de 2026

**Autorización:** el usuario pidió, mientras revisaba el PDF LaTeX del SD3, poner «No aplica» en la columna de diagramas donde la sección no tiene diagramas. **Alcance y destino:** en el MD de `rama-md` (cuerpo Tabla 3.6, Anexos Tabla 3.A.15, T-12) y en el checkout `../LafroX-sd3-latex`, rama `LafroX-Subdoc3-LateX` (`contenido.tex`, `tablas_anexo/declaracion_ia.tex`, `LAFROX-Formulario-T-12.tex`). Filas 3.1, 3.2, Anexos 3.A–3.K y T-12 pasan a «No aplica»; 3.3 (Alto) y 3.4 (Ninguno, con figuras) se mantienen. **Resultado:** `latexmk -g` sin errores; cuerpo 36 p. (la Tabla 3.6 continúa en la p. 36), anexos 166 p., T-12 260 p. El usuario acepta las 36 páginas: lo que excede es solo la tabla de declaración de IA, no contenido. Sin commit.
