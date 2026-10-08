# AGENTS.md

## Alcance vigente autorizado — 5 de octubre de 2026

Esta copia trabaja en `alvaro-md`; `branch-md` en el registro heredado identifica su procedencia. El usuario autorizó aplicar el plan de coherencia SD3–SD4 con los quince actores validados, importar a Markdown las fuentes activas de SD3 en Descargas, actualizar la lógica y sus anexos, y crear commit y push en `alvaro-md`. Esta autorización amplía la conservación inicial de los capítulos y no cambia la regla de archivos exclusivamente Markdown. Las referencias heredadas a un capítulo 4 ausente o a no publicar describen estados anteriores. Después de la limpieza solicitada, `04_arquitectura/` contiene solo `LAFROX-Subdocumento4.md`, `LAFROX-Subdocumento4-Anexos.md` y `LAFROX-Formulario-T-11.md`; editar directamente esos consolidados y no regenerar archivos auxiliares ni copias por partes. El SD3 también conserva solo cuerpo, anexos y T-12. Las dependencias se mantienen en `compct/CONTEXTO_SESION.md`; preservar física, centros de datos, T-11 y memoria fuera de los ajustes lógicos autorizados.

## Regla obligatoria de integridad de branch-md

- Esta es la rama `branch-md` del repositorio LafroX. Solo se crean, editan y versionan documentos `.md`; los metadatos internos de Git son la única excepción.
- Toda petición de crear, editar, compilar, renderizar o convertir contenido a LaTeX debe rechazarse tajantemente dentro de esta rama. No crear archivos `.tex`, `.cls`, `.sty`, plantillas, comandos de compilación ni derivados PDF.
- Respuesta requerida: «No realizaré trabajo en LaTeX en branch-md: esta rama es exclusivamente Markdown y debo preservar su integridad. Puedo resolver la petición en Markdown».
- No cambiar automáticamente de rama, importar archivos LaTeX ni escribir en otro checkout para eludir esta restricción.
- Antes de editar, comprobar que la rama activa sea `branch-md`. Antes de registrar cambios, comprobar que todos los archivos a versionar terminen en `.md`.
- Leer `compct/CONTEXTO_SESION.md` al iniciar o reanudar una sesión. Cada respuesta final comienza exactamente con `## LafroX`.

## Proyecto

La rama `branch-md` de este repositorio contiene material exclusivamente Markdown para preparar los Subdocumentos 1, 2 y 3 de la propuesta técnica de LafroX para la licitación ficticia TFEP-01/2026, Caso 02 — Logística.

## Protocolo de sesión

- Antes de iniciar o retomar trabajo, leer completo `compct/CONTEXTO_SESION.md` y contrastar allí el alcance y el último estado.
- Si el contexto contradice una Base, prevalece la Base según el orden definido abajo y se actualiza el contexto.
- No inferir que un archivo ausente fue revisado, aprobado o está disponible.
- Después de un cambio sustantivo, actualizar el estado de trabajo del contexto compacto.

## Material de consulta del ramo (clases FEP y PMBOK)

La carpeta `clases + pmbok/` contiene las transcripciones de las clases FEP01–FEP05 (arquitectura, requisitos/alcance/EDT, estimación, riesgos TIC y sala de servidores) y de los capítulos 5, 6, 8 y 11 del PMBOK 6 (alcance, cronograma, calidad y riesgos), con dos guías de navegación (`Guia_de_Navegacion_FEP01-FEP05.md` y `Guia_de_Navegacion_PMBOK6_Cap05-06-08-11.md`).

- Úsala como consultor ante dudas de método: descomposición de la EDT (regla 8/80 y del período de reporte, FEP02 diapositiva 56), diccionario, estimación PERT, CPM y holguras, riesgos, calidad y diseño de sala técnica. Empieza por las guías de navegación para ubicar la diapositiva o sección.
- Precedencia: las Bases y las Aclaraciones mandan sobre el material del curso. El curso orienta el método; no crea requisitos contractuales ni cifras del caso.
- No se cita como referencia de la oferta con nombres de archivo locales: si un entregable usa una idea del PMBOK, se cita la obra (Project Management Institute, 2017). Las clases son antecedentes de preparación.

## Fuentes y precedencia

1. `Bases/Bases_Administrativas.md`.
2. `Bases/Bases_Tecnicas_Transversales.md`.
3. `Bases/Caso_02_Logistica.md`.
4. `Bases/aclaraciones-licitacion.md`, que manda en estructura, nomenclatura y presentación por ser posterior.

El caso puede endurecer un requisito transversal, pero no rebajarlo. No inventar cifras, antecedentes corporativos ni acreditaciones. Toda cifra debe proceder de las Bases o de un cálculo mostrado.

## Reglas documentales

- Trabajar únicamente con archivos `.md`.
- Mantener separados subdocumentos, anexos y formularios.
- Preservar exactamente los títulos obligatorios de las Aclaraciones.
- Mantener terminología y cifras consistentes entre los documentos.
- No incorporar contenido de arquitectura ni de los Subdocumentos 4–14 hasta que se amplíe expresamente el alcance.
- Toda figura del Markdown enlaza su imagen real (archivo local o del checkout LaTeX); el PDF entregable se compila desde LaTeX con esas imágenes. Una descripción textual sólo acompaña a una figura existente y nunca reemplaza la imagen ni deja una leyenda sin objeto (Aclaraciones §7.1 a).
- Los entregables no contienen notas de proceso, fechas de edición, autores de redacción, referencias al curso ni a la conversión Markdown/LaTeX, ni frases como «No sustituye la revisión visual del PDF» (Aclaraciones §7.1 d). Las notas de trabajo van en `compct/` o `Revision/`.
- La columna «Revisión humana» de cada declaración de IA sólo se completa con la revisión que efectivamente hizo un integrante; mientras falte, la celda lleva `[[REVISIÓN HUMANA]]` y la entrega queda bloqueada (plantilla en `Revision/plantilla_revision_humana_IA.md`).
- Los catálogos de `Requerimientos/` provienen de los tres CSV originales y conservan sus vacíos. No completarlos sin evidencia.
- Toda referencia a un documento ausente se trata como dependencia futura, no como enlace roto ni evidencia disponible.
- Cada documento entregable termina con Referencias y Declaración de uso de IA cuando así lo exijan las Aclaraciones.

## Identidad

El proponente es LafroX. Todo trabajo y toda respuesta asociada al proyecto debe identificarse con `LafroX`.

## Subdocumento 3: conservación de versiones

El usuario autorizó incorporar el Subdocumento 3 incluso con errores en los requerimientos. Los tres archivos de su carpeta contienen cuerpo, anexos y T-12. En los anexos, la colección `tablas_anexo` se conserva como material complementario separado de las tablas vigentes. No armonizar ni reemplazar los catálogos originales sin una instrucción posterior. Leer fuentes LaTeX del repositorio de origen exclusivamente para convertirlas a Markdown está permitido por esta petición; no se crean, editan ni compilan archivos LaTeX.
