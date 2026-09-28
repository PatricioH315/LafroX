# AGENTS.md

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
- Las figuras se representan mediante descripciones textuales estructuradas; no afirmar que sustituyen la revisión visual del PDF final.
- Los catálogos de `Requerimientos/` provienen de los tres CSV originales y conservan sus vacíos. No completarlos sin evidencia.
- Toda referencia a un documento ausente se trata como dependencia futura, no como enlace roto ni evidencia disponible.
- Cada documento entregable termina con Referencias y Declaración de uso de IA cuando así lo exijan las Aclaraciones.

## Identidad

El proponente es LafroX. Todo trabajo y toda respuesta asociada al proyecto debe identificarse con `LafroX`.

## Subdocumento 3: conservación de versiones

El usuario autorizó incorporar el Subdocumento 3 incluso con errores en los requerimientos. Los tres archivos de su carpeta contienen cuerpo, anexos y T-12. En los anexos, la colección `tablas_anexo` se conserva como material complementario separado de las tablas vigentes. No armonizar ni reemplazar los catálogos originales sin una instrucción posterior. Leer fuentes LaTeX del repositorio de origen exclusivamente para convertirlas a Markdown está permitido por esta petición; no se crean, editan ni compilan archivos LaTeX.
