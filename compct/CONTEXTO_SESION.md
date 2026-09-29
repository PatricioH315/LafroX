# CONTEXTO DE SESIÓN

## Estado vigente — Anexo 2 disponible y actualización de pendientes del ítem 3, 29-09-2026

El usuario incorporó `02_problema_necesidad/LAFROX-Subdocumento2-Anexos.md` y pidió actualizar el documento de pendientes y confirmar si solo faltaban dependencias posteriores. Se leyó completo el anexo y se actualizó el mismo `Revision/LAFROX-Pendientes-item3-2026-09-29.md`, conservando sus 32 acciones. Se retiró la dependencia por ausencia del Anexo 2 y se corrigieron los diagnósticos correspondientes. No se editaron los entregables ni los CSV; continúa la autorización previa para informe/contexto en `arquitectura-basti`, sin cambio de rama, commits o publicación.

El anexo confirma F-01–F-14 (no RF para las familias de SD2), cinco RNF rectores, S-01–S-16, E-01–E-09, R-01–R-12, 19 actores y cinco sistemas legados. Confirma el reemplazo progresivo del WMS y la captura de conocimiento en E1; no respalda talleres meses 1–3 ni cuatro meses de cooperación. S-04 deja a Calidad liberar/bloquear/rechazar y al sistema alertar/habilitar bloqueo, por lo que se agregó la discrepancia con la retención automática de SD3. S-03 adopta reagendamiento del sistema; S-09 precio vigente al despacho. El planificador tiene influencia Alta e interés Muy Alto; el actor nominal Tripulación propia y peoneta incluye explícitamente peonetas. RNF-DISP distingue 99,95 % infraestructura de 99,9 % transacción crítica; no se verifican 14 CD, marcas SAP/Manhattan ni 38 % de rotación de conductores en SD2/anexo.

Se registran precauciones de consistencia: F-02 menciona recepción en seis instalaciones sin diferenciar oficinas; la estrategia del actor Empresas Transp. sobre liquidación no puede ampliar la administración/pago excluidos por E-05; el OTIF ≥95 % atribuido a condiciones de canal moderno requiere distinguir meta de referencia del Caso y condición específica de carta 2029. El anexo contiene restos de formato y primeras filas mezcladas con encabezados: no se declaró aprobado ni completo en presentación, y no se editó.

Conclusión vigente: NO faltan solamente subdocumentos posteriores. Hay insumos para ejecutar muchos pendientes propios de SD3/Anexo 3/T-12, pero siguen sin ejecutarse (catálogos, decisiones, reglas, metas, aceptación y respuestas). Los vínculos posteriores principales son SD4 (arquitectura), SD7 (EDT) y SD9/T-13 (pruebas); SD5/6/10/13 aportarán acreditaciones según requisito. Subsisten también confirmaciones del CLIENTE y revisión humana/formal cuando no realizadas. Se incorporó al informe una tabla que separa los tres grupos y evita dar por cerrado SD3 por la sola incorporación del Anexo 2. Los tres entregables de SD3 conservan los hashes comprobados en la revisión anterior.

## Estado vigente — informe de pendientes del ítem 3 sobre archivos actuales, 29-09-2026

El usuario pidió revisar la carpeta `03_esquema_solucion_alcance/` y crear un documento con todo lo que falta según Aclaraciones y Revision_informe, sin confundir el alcance con otros subdocumentos y manteniendo consistencia con SD1/SD2 y Requerimientos. Se creó `Revision/LAFROX-Pendientes-item3-2026-09-29.md`, con 32 acciones, evidencia, criterios de cierre, límites de alcance y dependencias. No se aplicaron correcciones a los entregables ni a los CSV.

Se observó `arquitectura-basti`. Ante la regla de comprobar `branch-md` antes de editar, el usuario autorizó expresamente crear solo el informe Markdown y actualizar este contexto en la rama actual, sin cambiar de rama ni hacer commits. No se realizaron cambios de rama, commits ni publicación.

El estado presente difiere de revisiones históricas de v1: en la carpeta existen únicamente los tres archivos sin sufijo v1. El cuerpo tiene calendario correcto y apartados de implementación, implantación y operación; el T-12 sí existe. Anexos vigentes: 31 RF desarrollados + 143 sin descripción/etapa/prioridad adoptadas; 13 RNF con umbral + 77 sin umbral, los 90 sin método; 25 supuestos, 22 sin contenido ni fuente; 16 criterios, todos sin meta propia ni momento/método en sus columnas. T-12: 174 RF + 90 RNF, con seis columnas de cumplimiento/trazabilidad vacías en las 264 filas y 220 orígenes vacíos; 374 RT con Cumple/componente/sección/evidencia vacíos. RF-11.03 no tiene etapa. La colección complementaria está dentro del anexo y conserva precio de 113 mil dólares, umbral térmico sin sustento localizado y contradicciones de conductor/Calidad, horario y marcha blanca E2. No reutilizar el diagnóstico anterior de Tabla 3.A.5 eliminada ni de correcciones cerradas.

El anexo del SD2 no está presente y no se recuperó: su nomenclatura, supuestos e inventario nominal quedan no verificables. El cuerpo actual del SD2 sí fija 24 h urbanas con corte a las 14:00 y 48 h rurales/periféricas/cross-docking; atribuye 38 % de rotación a preparadores, no a conductores; no menciona 14 CD. SD1 declara cinco ambientes totales incluido DR, RTO ≤4 h/RPO ≤15 min y cobertura corporativa del 80 %. Los CSV actuales tienen 134 RF del caso, 34 RF de Bases con cinco colisiones de seguridad/telemetría (RF-14.01–14.05), 24 RNF del caso y 58 de Bases; los RNF-03-01/02/03 usan guiones donde T-12 usa puntos. Se documentaron adicionales del T-12 sin borrar ni armonizar catálogos.

Próximo paso: si se solicita ejecutar, aplicar las acciones sobre los archivos actuales, conservando material histórico separado y registrando dependencias reales de SD4, SD5, SD6, SD7, SD9, SD10 y SD13. No inventar arquitectura, EDT ni pruebas ausentes. La verificación visual final y los PDF no se realizaron ni se autorizan por este informe. Los estados anteriores se conservan como historia y no prevalecen sobre esta observación de archivos presentes.

## Estado vigente — actores, precondiciones y nomenclatura de los cuatro CSV, 29-09-2026

El usuario autorizó reemplazar actores ajenos al Anexo 2, eliminar la columna `Actor` de ambos CSV no funcionales, sustituir las precondiciones «Ninguna.» por argumentos sustentados y usar `Caso_Logistica` como nombre documental en los orígenes de ambos consolidados. Se actualizaron los cuatro CSV en la rama observada `arquitectura-basti`, sin cambiar ramas, registrar commits ni publicar.

Los actores de los dos CSV funcionales usan exclusivamente nombres exactos del catálogo de ecosistema del Anexo 2.3 de `02_problema_necesidad/LAFROX-Subdocumento2-Anexos.md`; las participaciones múltiples se separan por ` / `. Los roles operativos no catalogados se vincularon con el cargo o colectivo del ecosistema correspondiente (por ejemplo, recepción con Jefa de Bodega, cobranza con Gerente de Finanzas y administración técnica con Jefe de TI). En requisitos técnicos de Bases, el actor corresponde a la contraparte del ecosistema del CLIENTE; las obligaciones del PROPONENTE y ADJUDICATARIO permanecen en las descripciones, sin transferencia contractual de responsabilidad.

Cambios: 134 actores y 134 orígenes normalizados en RF del caso; 34 actores ajustados en RF de Bases; columnas Actor eliminadas en ambos RNF; 24 orígenes normalizados en RNF del caso. Se sustituyeron 68 precondiciones «Ninguna.» (1 RF del caso, 6 RNF del caso, 16 RF de Bases y 45 RNF de Bases) por contextos de aplicación o eventos derivados de los requisitos y sus fuentes, con localizadores. Estas formulaciones no agregan aprobaciones ni dependencias contractuales nuevas.

Verificación antes/después y lectura posterior: se mantienen 134, 24, 34 y 58 filas, sus identificadores y orden; cero celdas vacías y cero precondiciones «Ninguna.»; las columnas de actores solo existen en los funcionales y cada nombre pertenece al Anexo 2.3. Se conservaron descripciones, prioridades, resultados y restantes columnas fuera de los cambios autorizados, además de la representación CSV de los campos no modificados. El Anexo 2 y los entregables del Subdocumento 3 no se editaron. El estado de los apartados siguientes es histórico cuando difiere de este seguimiento.

## Estado vigente — completar vacíos de los cuatro CSV, 29-09-2026

El usuario solicitó expresamente actualizar los cuatro CSV de `Requerimientos/`, completando únicamente celdas vacías con respaldo en el Caso 02 y las Bases Técnicas Transversales y Administrativas, sin agregar, eliminar ni modificar requerimientos. Esta petición autoriza para esta tarea la edición de esos CSV, como excepción al formato exclusivamente Markdown indicado anteriormente. Se observó `arquitectura-basti` y se mantuvo el trabajo local conforme a la instrucción registrada de no cambiar ramas; no se hicieron cambios de rama, commits ni publicación.

Se completaron 99 celdas: 39 en el consolidado funcional (134 filas), 48 en el consolidado no funcional (24 filas) y 12 en los no funcionales de Bases (58 filas). El CSV funcional de Bases (34 filas) no tenía celdas vacías y quedó idéntico byte por byte. Se conservaron encabezados, orden, identificadores, todas las filas y todos los valores originalmente poblados, incluidos guiones usados como contenido. La comprobación antes/después validó que cada diferencia correspondiera exclusivamente a una celda originalmente vacía; se preservó la representación original del resto del CSV.

Las nuevas referencias de origen incluyen localizadores y distinguen el respaldo general de detalles que el Caso no define, por ejemplo Transbank, expiración de contraseñas, umbrales de recepción e historial, reglas de crédito y reserva. Estas observaciones no corrigen ni validan los requisitos preexistentes. Los títulos se sintetizaron de las descripciones existentes y los actores se tomaron del proceso o del sistema identificado; no se agregaron responsables nuevos.

En el seguimiento del mismo día, el usuario reiteró la correspondencia de fuentes: los dos consolidados se completan desde el Caso 02 y los dos catálogos de Bases desde las Bases Técnicas Transversales y Administrativas; exigió que no quedaran celdas vacías. Se completaron las tres precondiciones pendientes usando el contexto de aplicación de las obligaciones, sin afirmar que las fuentes establezcan una condición previa adicional: RNF-13.03, solución con equipos on-premise críticos; RNF-13.05, definición del esquema de almacenamiento local (ambas sustentadas en RT-03.14 y Art. 16.4); RNF-22.02, preparación del material de capacitación por perfiles (RT-22.01, RT-22.03 y Arts. 90.1 y 90.3). Cada celda incluye sus localizadores.

Estado final: 102 celdas completadas acumuladas y cero celdas vacías en los cuatro CSV (134, 24, 58 y 34 filas, respectivamente). La última comprobación verificó que solo cambiaran esas tres celdas previamente vacías y que los otros tres archivos quedaran idénticos byte por byte respecto del inicio del seguimiento. Los entregables del Subdocumento 3 permanecen fuera de esta tarea. Los apartados anteriores y posteriores que declaran intactos los catálogos describen estados históricos.

## Encargo vigente para aplicar la revisión de comisión

A petición del usuario se creó `Revision/LAFROX-Instrucciones-IA-aplicar-correcciones-v1.md`, documento autónomo de ejecución con las 18 acciones H01–H18, ubicación, pasos y criterios de cierre, fuentes, exclusiones y comprobación final. La otra IA debe editar los tres v1, no producir otra revisión. Este encargo sustituye para esta ejecución las listas anteriores. Se preservan las declaraciones de IA y los documentos fuera del ítem 3; los datos sin evidencia no se inventan. En esta tarea solo se creó el encargo y se actualizó este contexto: no se aplicaron las correcciones a los entregables ni se realizaron operaciones de Git.

## Estado vigente — revisión de comisión de los v1, 29-09-2026

Se creó `Revision/LAFROX-Revision-comision-item3-v1-2026-09-29.md` aplicando el prompt de Informe 2 únicamente al ítem 3. Los tres entregables quedaron intactos (hashes SHA-256 verificados antes/después). Declaración y tablas de IA excluidas. La aplicación literal del árbol arroja 0/100 por tres notas del revisor dentro de prioridades RNF, fuera de esa exclusión; no es una nota oficial ni una afirmación de autoría. Hay 77 referencias T-12 a Tabla 3.A.5 eliminada, once RNF con «Valor según bases», contradicciones de soporte, pentesting y etapas, y defectos de aceptación. El informe contiene hallazgos y criterios de corrección para otra IA.

El precio histórico y la colección complementaria ya NO están en el anexo entregable actual. Los estados anteriores que dicen lo contrario son historial. Parte A tiene 174 RF + 5 OF + 90 RNF = 269 filas; Parte B, 374 RT. Se mantuvo la rama observada `arquitectura-basti`, sin operaciones de cambio de rama, commits ni publicación, conforme a la instrucción previa del usuario sobre trabajo local. Los PDF y los entregables de otros ítems no fueron evaluados ni exigidos como contenido de SD3.

## Aclaración vigente del encargo para otra IA

El usuario aclaró que el documento debe instruir a otra IA a APLICAR las correcciones, no a analizar solamente. Se creó `instrucciones_ia_aplicar_item3_2026-09-29.md` con 18 correcciones ejecutables, criterios de cierre y entrega de los tres Markdown corregidos. Reemplaza como encargo vigente el documento de análisis anterior. Incluye conservación separada del material histórico fuera de la oferta, exclusión íntegra de declaración de IA y límites frente a otros subdocumentos. En esta conversación se prepararon las instrucciones; no se editaron los entregables ni se operó sobre Git.

## Estado vigente al 29-09-2026 — revisión de nuevos v1 y encargo de análisis solamente

Se revisaron las copias v1 actualizadas contra Aclaraciones, el apartado S3 de Revision_informe, el prompt de comisión Informe 2 adaptado a Markdown y la consistencia con SD1/SD2. Se creó únicamente como documento de entrega `instrucciones_ia_analisis_item3_2026-09-29.md`, con 18 focos sustentados, para que otra IA ANALICE SIN EDITAR. Excluye declaración/tablas de IA y distingue el contenido de S3 del detalle propio de SD4/5/6/7/9/10. No se aplicaron correcciones a los tres entregables.

El estado cambió respecto de las revisiones anteriores: los 143 RF ya tienen desarrollo y existen cinco OF (269 filas en Parte A del T-12); se repararon las doce filas RT y el cálculo de migración ahora suma 9.600.100 KB. Persisten o reaparecieron el precio de 113 mil dólares en la decisión complementaria 45, 66 RNF por definir, 16 métodos RNF vacíos, EX-10/11 y R-13–22 vacíos, campos insuficientes de supuestos, 374 localizadores RT a las Bases y 352 evidencias genéricas. Hay contradicciones en confirmación offline, acuses por etapa, disponibilidad, envases y S-24, así como falsas atribuciones al SD2 y notas editoriales fuera de la declaración de IA. No reutilizar las 28 acciones anteriores como diagnóstico íntegramente vigente.

Se mantuvo arquitectura-basti, sin cambiar ramas, registrar commits ni publicar. Los apartados siguientes son historial cuando discrepan de este estado.

## Estado vigente — nueva revisión de los tres entregables actualizados

Se creó `acciones_item3_revision_actualizada.md` a solicitud del usuario, con 28 acciones sobre cuerpo, anexos y T-12. Se excluyeron las tablas y declaraciones de uso de IA. No se modificaron los tres entregables ni los catálogos originales. Se mantuvo la rama `arquitectura-basti`, sin cambios de rama, commits ni publicaciones, conforme a la indicación previa del usuario.

Esta revisión **rectifica el cierre integral declarado más abajo**: todavía quedan pendientes. Se comprobaron errores de moneda en S-06/V-22 (dólares en lugar de pesos), doce filas de Parte B del T-12 con respuesta en la columna Carácter, asociaciones semánticas incorrectas (por ejemplo RNF-14.01 cifrado ligado a OTP y ocupación), 143 RF sin desarrollo, metas abiertas de envases/ocupación, incoherencias de soporte y supuestos, errores de cálculo en 3.L y sesgo en el denominador de cobertura histórica. El SD2 sí contiene la promesa 24/48 horas con corte a las 14:00; la afirmación de que aún la deja por parametrizar es falsa. Las dependencias reales de arquitectura, EDT y pruebas no se consideran evidencia disponible ni se exige inventarlas.

Se reconocen las mejoras ya aplicadas: retiro de precio y umbral térmico sin fuente, desarrollo de RNF y supuestos, reducción de filas vacías y ampliación de implementación/operación. El nuevo documento distingue esas mejoras de los pendientes actuales. Las notas históricas posteriores se conservan como historial, no como estado vigente.

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
- Las figuras se conservan como descripciones textuales estructuradas mientras el repositorio sea exclusivamente Markdown.
- Toda ampliación del alcance se registra primero en este archivo, en `README.md` y en `MANIFIESTO.md`.
- Después de cada cambio sustantivo se actualiza la sección siguiente para permitir una reanudación segura.

## Último estado de trabajo

**Fecha:** 2026-09-28.

**Completado:** importación de los 17 documentos Markdown a `branch-md`, preservando el contenido documental e incorporando la prohibición explícita de trabajar en LaTeX. La comparación con `tablas_anexo` del Subdocumento 3 detectó diferencias de cantidades, nombres y códigos; los catálogos Markdown no se sustituyeron.

**Siguiente paso:** continuar la revisión o edición de los Subdocumentos 1, 2 y 3 usando únicamente las fuentes incluidas. Cualquier incorporación de arquitectura o de los Subdocumentos 4–14 requiere ampliar expresamente el alcance.

## Última actualización: incorporación del Subdocumento 3

Petición vigente: trasladar todo el material relevante del Subdocumento 3 en exactamente tres documentos Markdown, conservando sus errores. Se incorporaron cuerpo, anexos 3.A–3.K, las 14 tablas de la colección complementaria `tablas_anexo`, tres figuras transcritas y T-12. El T-12 mantiene 174 RF, 90 RNF y 374 RT. La colección complementaria conserva 90 RF y 40 RNF aunque anuncia 91 y 41. Estas versiones no fueron reconciliadas ni sustituyen los CSV convertidos en `Requerimientos/`. Próximo paso: revisión del contenido si el usuario la solicita; no dar por corregidas las discrepancias.

## Última actualización: copias v1 del Subdocumento 3

**Fecha:** 2026-09-28. El usuario autorizó tres copias editables del Subdocumento 3, idénticas a los originales salvo correcciones sustentadas, conservando intactos los archivos fuente.

Archivos creados en `03_esquema_solucion_alcance/`: `LAFROX-Subdocumento3-v1.md`, `LAFROX-Subdocumento3-Anexos-v1.md` y `LAFROX-Formulario-T-12-v1.md`.

Correcciones aplicadas:

- Nomenclatura: el SD2 usa familias F-01 a F-14 y el SD3 usa RF y RNF. Se corrigieron todas las citas «SD2, RF-xx» a «SD2, F-xx», incluidos los rótulos de las Tablas 3.A.1 y 3.A.2, sin renumerar los identificadores del SD3.
- Regla térmica: se adoptó el supuesto S-04 del Anexo 2.2 del SD2. El sistema registra, alerta y habilita el bloqueo; Calidad decide liberar, bloquear o rechazar. Se corrigieron el cuerpo, RF-09.06, RF-09.07, el supuesto S-04, la regla RNG-04 y la decisión 4 de la colección complementaria, que atribuían la decisión al conductor.
- Horario de soporte: 04:00–22:00 de lunes a sábado es el RT-21.06 del caso y endurece el piso de 8:00–20:00 del RT-21.07 sin rebajarlo. El monitoreo 24×7 del RNF-21.01 se distinguió del horario de la mesa de servicio.
- Instalaciones: se adoptó la lectura de seis sitios, cinco con cómputo, coincidente con el supuesto S-22 del SD2. Los «14 CD» pertenecen al antecedente LogiNacional del SD1, no al SD2; se corrigió la entrada V-01.
- Conteos: los rótulos anunciaban una fila más de la existente en las Tablas 3.A.16, 3.A.19, 3.A.22, 3.A.24, 3.A.25 y 3.A.26. Se ajustaron a 60, 14, 43, 90, 40 y 46.
- Trazabilidad: se documentó en prosa la correspondencia de los cinco RNF rectores del SD2 (RNF-DISP, RNF-REND, RNF-RESIL, RNF-SEG y RNF-DR) con los RNF del SD3, verificada por umbrales.
- Notas internas: se convirtieron en prosa declarativa las 19 notas de trabajo y 4 notas de conversión de la revisión externa. Se preservaron sin cambio las notas de la sección «Declaración de uso de IA», cuya redacción corresponde al usuario.
- Referencias: la Tabla 3.4 se attribuyó a elaboración propia a partir de la sección 3.1.1 y se retiró la referencia inexistente a la arquitectura lógica v6-2. Se eliminó la URL malformada de ChileAtiende y la atribución de la disposición del lote al conductor.
- Enlaces internos del cuerpo: apuntan a las copias `-v1.md`. Comprobación automática: 0 enlaces internos rotos y 0 filas de tabla con columnas divergentes en los tres archivos.

Elementos que no se modificaron, por decisión expresa del usuario: la declaración de uso de IA, el nombre de la herramienta y las 29 celdas de revisión humana en «No documentada». Tampoco se tocaron los originales ni el material de los Subdocumentos 4–14, que sigue siendo dependencia futura.

Corrección de una afirmación previa: el precio «113 mil dólares antes de reservas» de la decisión complementaria 45 y el umbral de referencia «desviación > 2 °C por más de 15 minutos» sí existían en los anexos v1. La afirmación anterior de que no existían fue errónea y no debe reutilizarse. La URL de ChileAtiende en el cuerpo y la decisión asignada al conductor no existían como tales. Con la revisión integral posterior, el precio y el umbral fueron retirados de los entregables. La colisión semántica de RF-14.01 a RF-14.05 (flota en el consolidado, seguridad en Requerimientos_Bases) quedó documentada en el Anexo 3.A.

## Última actualización: revisión integral y documento de acciones del ítem 3

El usuario pidió revisar exclusivamente los tres archivos v1 como documentos originales y después generar un documento Markdown con todo lo pendiente, excluyendo las tablas de uso de IA. Se creó `acciones_item3_revision_integral.md`, con acciones por archivo, prioridades, criterios de cierre, dependencias futuras y correcciones al diagnóstico de acciones v2. Los tres entregables no fueron modificados.

La rama observada es `arquitectura-basti`, no `branch-md`. Informado de la discrepancia y consultado por la creación local, el usuario indicó: «no actualices ninguna branch, ya vere yo cuando suba esto». Se realizó trabajo documental local sin cambiar ramas, registrar commits ni publicar. Esta indicación no autoriza cambios de Git en futuras tareas.

Correcciones al contexto anterior: el anexo v1 sí contiene el precio «113 mil dólares antes de reservas» en la decisión complementaria 45 y el umbral de referencia «desviación > 2 °C por más de 15 minutos» en los supuestos complementarios. RNG-04 todavía dice que el sistema retiene el lote; el cuerpo del SD2 y su anexo tampoco coinciden completamente en el bloqueo térmico. Las afirmaciones previas de ausencia o armonización completa no deben reutilizarse. El SD2 disponible no contiene el supuesto S-22 ni el compromiso literal de cooperación del planificador durante cuatro meses que se le atribuye en SD3.

Estado: documento de acciones preparado; correcciones de los entregables aún no ejecutadas. Las tablas de uso de IA están excluidas del plan por instrucción del usuario. Los catálogos de Requerimientos permanecen intactos.

## Última actualización: ejecución parcial del plan de acciones del ítem 3

**Fecha:** 2026-09-28. Se comenzó a aplicar `acciones_item3_revision_integral.md` sobre los tres archivos `-v1.md`, sin tocar los originales ni las tablas de uso de IA.

Aplicado en los entregables:

- B-01: retirado el precio «113 mil dólares antes de reservas» de la decisión complementaria 45.
- B-15: retirado el umbral «> 2 °C por más de 15 minutos»; se declara que no se adopta valor numérico sin fuente. RNG-04 ya no atribuye la retención automática al sistema.
- B-05: los RNF rectores se atribuyen al Anexo 2.1 del SD2; la disponibilidad de infraestructura (99,95 %) y la de transacción crítica (99,9 %) quedan separadas.
- B-04: registradas las colisiones por fuente RF-02.08/02.09, RF-09.06/09.07, RF-14.01–14.07, RNF-14.01 y RNF-16.03 en el Anexo 3.A; RF-14.07 no existe en el consolidado ni en el T-12.
- B-07: S-16 reencuadrado como propuesta propia de LafroX; eliminada la atribución inexistente de S-22 al SD2. Ampliado después al cierre completo de la Tabla 3.A.6, registrado más abajo.
- B-08: retiradas del registro vigente las filas vacías EX-10/11 y R-13–R-22; las obligaciones administrativas quedan separadas en la colección complementaria.
- B-09: precisadas las reglas RNG-01, RNG-04, RNG-05, RNG-07, RNG-08 y RNG-15 (reserva central vs consulta offline, regla térmica por producto, reagendamiento, sentido del saldo de envases, precio al despacho y promesa 24/48 h).
- B-11: diferenciados momento, responsable e indicador de los 19 actores del Anexo 3.I.
- A-01: F-05 (cross-docking) y F-09 (acuse de la GDE) quedan con requisito candidato y etapa; fill rate se asigna a la Etapa 1 y costo de servir a la Etapa 2.
- A-02: la promesa de entrega se fija en 24 h urbanas con corte a las 14:00 y 48 h rurales/periféricas/cross-docking, con la discrepancia con el SD2 declarada como dependencia externa.
- A-04: completada la Tabla 3.A.13 con meta, momento y método; OTIF con mejora gradual 90/93/95 %; envases y ocupación con la dependencia declarada, sin inventar el porcentaje ni el umbral.
- A-05: cobertura de pruebas adoptada en 80 % (política corporativa del SD1), por encima del piso del 70 % del RT-04.11.
- A-06: procedimiento de reversión con disparadores, autoridad, pasos y tratamiento de transacciones capturadas.
- A-07: tabla de indicadores de operación con servicio, objetivo, medición, frecuencia, responsable y respuesta; NOC 24×7 separado de la mesa 04:00–22:00 L–S.
- A-08: tratados los hitos externos de septiembre de 2026 y enero de 2029 sin inventar fecha de inicio; explicada la preferencia del comité y la objeción de la gerenta sobre el planificador, distinguida de la objeción sindical.

- A-11 (parcial): eliminadas las tres notas «Nota de conversión» (fin de Subdoc3-v1, Anexos-v1 y T-12-v1) y catorce líneas «Origen de esta tabla: …/tablas_anexo/*.tex» del Anexos-v1, por ser penalizables conforme a `Revision_informe.md` 254/255/513 y a las Aclaraciones 7.1(d). Queda pendiente la ubicación de índice e introducción, los localizadores y páginas verificables de las Bases y la referencia residual «F-02 y RF-03».
- B-06: añadido «Método de verificación» a las 13 filas de la Tabla 3.A.4 y reescrita la Tabla 3.A.5 completa (77 RNF) con columnas `ID | Materia | Umbral adoptado o propuesto | Método de verificación | Origen y carácter», distinguiendo umbral contractual (RT/Bases) de propuesto (catálogos de trabajo). Los siete RNF sin identificador propio se resolvieron por homólogo RF/RT. Los marcos de apertura y el título de la Tabla 3.A.5 quedaron actualizados.
- B-14 (parcial): corregida la fila `RNF-06.02` de la Tabla 3.A.5 al valor con fuente (8 h turno de bodega y 14 h reparto/preventa, con renovación local al inicio de turno), reemplazando el 24 h que confundía el token de acceso con la autonomía del CD.

- C-01/C-02/C-03/C-04 (T-12, avance): con autorización del usuario se llenó el formulario mediante el script temporal `fill_t12.ps1` (UTF-8 sin BOM, CRLF). Parte A: 264 filas RF/RNF con convención de respuesta (Comprometido / Comprometido (deseable) / Aplica (según caso) / Dependencia futura), componente/EDT/prueba/sección/criterio y origen respaldado completado desde la carpeta `Requerimientos/` solo cuando existe; 67 orígenes quedan vacíos por ser vacíos reales del catálogo. Parte B: 374 filas RT con Cumple por carácter (313 Comprometido, 40 Comprometido (deseable), 21 Aplica (según caso)). Ninguna celda Cumple vacía. La EDT se marca como dependencia futura del Capítulo 7 (Subdocumento 7) y la prueba como dependencia futura del Capítulo 9 / T-13; no se inventaron paquetes ni casos de prueba. Corregidos dos regex (`R[FN]F`→`RN?F`) que omitían los RF-13 a RF-18. Actualizada la prosa de Convenciones e introducción del T-12. C-04 cerrado: en el anexo 3.A.1 (RF-01.03) se eliminó la referencia residual «F-02 y RF-03», que queda como «F-02».

- A-11 y B-16 (cerrados en la parte verificable, con revisión contra `Revision_informe.md` 254/255/257 y `aclaraciones-licitacion.md` cap. 3): eliminadas todas las citas de nombres de archivo como fuente (`LAFROX-Subdocumento3-Anexos-v1.md`, `LAFROX-Formulario-T-12-v1.md`, `reglas_de_negocio.md`, `Caso_02_Logistica.md`, `Bases_Tecnicas_Transversales.md`, `Bases Administrativas.md`) y sustituidas por referencias documentales (Bases Administrativas, Bases Técnicas Transversales, Caso, SD2, SD3); eliminadas las tres notas de corrección de versión anterior que la revisión señalaba (decisión previa del precio, «tal como estaba declarado», «que no estaba respondida»); retirada la nota de discrepancia 91/41 y el rótulo con el nombre de la carpeta complementaria; corregido el criterio `R18-14` de la fila de autenticación de conductores en la Tabla 3.A.27 a `R18-08, R18-09`; retiradas las páginas no verificables (`pp. 12-13`, `p. 35`, `p. 23`); ampliadas las notas «esta versión» a «este documento»; ampliado el glosario de la Tabla 3.A.14 con SD2, BTT, BTC, R18, RNG, F, D, S, EX, R y V. Verificado que no quedan referencias a archivos, páginas, notas de versión ni nombres de carpeta en los tres archivos v1, y que siguen en UTF-8 sin BOM y CRLF.

- B-07 (cerrado): la Tabla 3.A.6 pasó de `ID | Materia | Contenido respaldado | Fuente | Evidencia que falta` a `ID | Materia | Decisión de la oferta | Fundamento | Consecuencia si falla | Instancia y responsable de validación`, con las 25 filas completas y sin celdas vacías. Las dieciséis materias del numeral 16.1 son S-01 a S-16 y las nueve adicionales S-17 a S-25. Se conservan los contenidos previos de S-04, S-06, S-14, S-16 y S-22. La instancia y el responsable se toman de la Tabla 3.A.12. S-17 declara que la oferta no fija fecha calendario de inicio y expresa el cronograma de 56 meses en meses relativos. Añadidas al Anexo 3.H las consultas V-22 (custodia del dinero en circulación) y V-23 (especificación y compra del hardware de terreno), y enlazadas desde la Tabla 3.A.6 las evidencias pendientes a V-01, V-03, V-10, V-12, V-15, V-16, V-22 y V-23. Corregida la atribución de V-01, que atribuía el supuesto S-22 al SD2, y registrada en el Anexo 3.A la colisión de la serie V-01 a V-12 entre el registro vigente y la colección complementaria. La tabla se ampliaron a siete columnas con `Requerimientos relacionados`, verificados uno por uno contra el catálogo vigente: RF-14.09 se descartó porque no existe, y la identificación por código o QR de S-05 se declara solo en la colección complementaria.
- B-14 (cerrado en la parte del ítem 3): nuevo Anexo 3.L con la Tabla 3.A.30, que deriva los 9,43 GB en origen y los 20 GB en destino con el método y los tamaños unitarios declarados, a partir de la volumetría del cap. 14.1 y de RT-05.15. En el mismo anexo se declaran de forma expresa seis dependencias o supuestos: tamaños unitarios, parque de dispositivos de conductores externos (nuevo vacío V-24), continuidad de identidad de 8 y 14 horas frente a la autonomía de 24 h del centro de distribución (nuevo vacío V-25), compromiso simultáneo del 99,95 % por componente y del 99,9 % de extremo a extremo en el vacío V-18, metas de resultados como propuestas propias y cobertura de trazabilidad en dos series separadas en V-08. Resuelta la mención a componentes de inteligencia artificial de la Tabla 3.A.17 con la decisión vigente D-09, y corregidas en el T-12 las doce filas afectadas: RT-18.01 a RT-18.09 pasan a «Aplica (sin componentes de inteligencia artificial en el alcance contratado)», RT-05.30 y RT-18.10 a «No comprometido (deseable)» y RT-26.06 a «Aplica (condicionado)».

Pendiente de ejecución: nada del plan de acciones del ítem 3. C-05 queda cerrado: los 16 resultados del capítulo 18 están en el Anexo 3.J con meta, momento y método de medición; las 16 decisiones del numeral 16.1 están en el Anexo 3.C con decisión, fundamento, consecuencia si falla, instancia y responsable, más los requerimientos que las implementan; las nueve exclusiones, las doce restricciones y las familias F-01 a F-14 constan en los Anexos 3.D, 3.E y 3.A; y la cadena origen, requerimiento, solución, etapa y aceptación es recorrible en la Parte A del Formulario T-12, donde la EDT y las pruebas quedan marcadas como dependencia futura del Subdocumento 7 y del Capítulo 9. F-05 (cross-docking) y F-09 (acuse de la guía de despacho electrónica) conservan requisito candidato y etapa, declarados como tales. Verificado que ninguna de las tres tablas tiene filas con conteo de columnas distinto del encabezado, y que los tres archivos siguen en UTF-8 sin BOM y CRLF.

La rama de trabajo sigue siendo `arquitectura-basti` por indicación del usuario; no se cambió de rama, no se registraron commits ni se publicó. La declaración de uso de IA, el nombre de la herramienta y las 29 celdas «No documentada» permanecen intactos.

## Última actualización — documento de ejecución para otra IA

A petición del usuario se creó `instrucciones_ia_correccion_item3.md`: encargo autónomo con fuentes necesarias, límites, secuencia de ejecución, las 28 acciones completas y formato de entrega de los tres archivos corregidos más registro de cierre. No requiere adjuntar la revisión anterior, pero sí los entregables y sus fuentes. En esta tarea no se aplicaron las correcciones ni se modificaron los tres entregables; se preparó exclusivamente el documento para transferir el encargo. Continúa excluida la modificación de las tablas y declaraciones de uso de IA. No se realizaron operaciones de cambio de rama, commits o publicación.
