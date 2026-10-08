# CONTEXTO DE SESIÓN

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
- Las figuras se conservan como descripciones textuales estructuradas mientras el repositorio sea exclusivamente Markdown.
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
