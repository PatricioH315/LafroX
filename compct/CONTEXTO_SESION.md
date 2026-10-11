# CONTEXTO DE SESIÓN
## Estado vigente — 11 de octubre de 2026: correcciones de revisión SD9

Se corrigieron sólo los cuatro Markdown de SD9 v_nueva: 42 textos de caída, referencia al calendario efectivo T-17 4.1, subtotal de conformidad y modelo paramétrico de no conformidad (93,8 HH por evento interno y 109,8 externo; no pronóstico ni reserva), secuencia PRE-C con restitución y capacidad neta pendiente de confirmación. LaTeX y diagramas actualizados en el repositorio independiente Subdoc/LafroX/SD9_v_nueva, cuatro PDF recompilados. Se conservaron las siete marcas de revisión humana y las firmas pendientes. Bases disponibles sólo en Markdown: lista de 220 pasajes para agregar páginas manualmente en Subdoc/Revision/citas_Bases_SD9_paginas_pendientes.md. No se recuperaron cifras desactualizadas de SD8. Informe de cierre en Subdoc/Revision/correcciones_SD9_2026-10-11.md. No se modificaron los cambios ajenos de SD13 ni se hizo commit.

## Estado vigente — 11 de octubre de 2026: consolidación del SD13 y revisión de la Comisión

Por instrucción del usuario, sólo se editaron los tres archivos de `13_innovaciones/` (cuerpo, anexos y T-19); ningún subdocumento anterior se modificó. Verificado: INN-01 a INN-05 tienen nombre, código, paquetes, meses y riesgos idénticos en T-12, SD5, SD7/7.D, T-14, SD8/8.A/8.F, T-16, SD9 y T-13. Cambios: introducción sin atribuir innovaciones al SD3/SD4 (solo componentes que reutilizan); Figura 13.1 dibujada en Mermaid (antes era descripción textual, indicio §7.1 a); nombres alineados al SD4 (C-01 App de preventa, C-02 App de reparto, C-03 Terminales de bodega, N-10 Plataforma analítica, capa 2 borde); «Investigación adicional declarada» en 13.N.3 y en el campo 5 del T-19; Tabla 13.B.2 de alcance refinado; RT-03.13 retirado de la bitácora; F-14 «Analítica de Costo de Servir»; herramientas citadas a Capítulo 6 y T-10; INN-03.P5 de los meses 32, 44 y 56 (septiembre con inicio feb-2027) activa parámetros después del día 25; índice enlazado en los tres archivos. Revisión en `Revision/revision_comision_informe2_SD13.md`: 0 mientras existan 13 celdas `[[REVISIÓN HUMANA]]`; 60 con ellas completas. Pendientes: revisión humana, imagen de la Figura 13.1 para el PDF, diagramas por innovación. Sin commit.

## Estado vigente — 11 de octubre de 2026: publicación y espejo del Subdocumento 4

El usuario autorizó commit y push y exigió igualdad de contenido entre Markdown y LaTeX. Se actualizó `rama-md` de `cf43057` a `d8bc438` por avance rápido, preservando los cambios locales SD4 en el stash `respaldo SD4 antes de sincronizar y publicar 2026-10-11` y reaplicándolos sin conflictos. La cámara premium del MC9400 agregada por el remoto se conserva. Destinos: únicamente Markdown en este checkout; fuentes y PDF en `../LafroX-rama-latex`, rama comprobada `subdoc-4` desde `292c6e8`.

Se trasladaron a LaTeX las especificaciones vigentes del MD que faltaban: recepción, inventario, control comercial, rutas, cobranza, devolución, EDI y telemetría; ASN al cargar separado del acuse tras descarga; AES-256/KMS, instancias de Preproducción por campaña y herramientas de pruebas. Se trasladaron al MD el diagrama de red corregido por el usuario y la figura de emplazamiento ya existente en LaTeX, sin alterar sus diseños. Ambos cuerpos contienen 27 figuras; referencias renumeradas y figuras enlazadas a los activos reales del checkout LaTeX. Resúmenes SD4 actualizados, sin tocar entregables de otros subdocumentos.

El cotejo de texto normalizado compara cuerpo, anexos y T-11: 1.579, 948 y 110 bloques respectivamente, sin diferencias de contenido. Se distinguen navegación, maquetación y artefactos conocidos del conversor; las 27 figuras se verifican por título, ancla y activo aparte, y 342 enlaces internos son válidos. LaTeX publicado y verificado en origin en `c4d1230`; los enlaces Markdown apuntan a ese commit. PDF compilados: 191/91/46 páginas, sin referencias indefinidas ni desbordamientos. Este estado y el registro `Revision/ALINEACION_MD_LATEX_SD4_2026-10-11.md` integran la unidad Markdown de sincronización autorizada para publicación; verificar su hash y remoto con Git al reanudar.

La figura de red conserva rótulos impresos próximos a 5 puntos al ajustarse a carta: sigue pendiente su legibilidad, sin modificar el XML aprobado. Cinco referencias del T-12 necesitan renumeración (recinto: 25 → 27; racks: 24 → 26), sin editar SD3 por alcance. Ensayos, autorización del mandante y revisión humana mantienen su estado; sincronización no equivale a conformidad total.

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
