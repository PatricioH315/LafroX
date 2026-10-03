# Instrucciones del capítulo 04 en alvaro-md

Estas instrucciones documentan la ampliación expresa autorizada por el usuario para incorporar el apartado 4.1 en la nueva rama `alvaro-md`. Aplican a `04_arquitectura/`; el contenido heredado de Alex-MD conserva sus reglas originales.

- La rama de trabajo para esta carpeta es `alvaro-md`. El nombre `branch-md` de los archivos heredados es contexto de su origen, no el nombre vigente de esta copia.
- Crear y editar únicamente documentos `.md`. Se permite leer las fuentes LaTeX de `rama-latex` y la procedencia de `arquitectura-alvaro` para convertirlas; no se importan fuentes LaTeX ni binarios a esta rama.
- Mantener cuerpo, anexos, procedencia y contexto en archivos separados. Conservar el contenido técnico de la fuente y distinguir conversiones de formato de cambios de diseño.
- El usuario amplió el alcance para importar los Markdown físicos y de centros de datos de `rama-latex` en `MD_4.2_2.3/`. Se conserva 4.1 y no se sustituyen capítulos 1–3. Desde el 3 de octubre de 2026, el usuario autorizó sincronizar todos los Markdown de 4.1–4.3, anexos y T-11 con el contenido efectivo publicado de `rama-latex`. Conservar sus discrepancias de fuente documentadas; no inventar soluciones ni aprobación.
- Conservar las figuras mediante sus referencias originales y explicaciones de lectura. No inventar diagramas ni afirmar que los enlaces sustituyen la revisión visual de una entrega PDF.
- Mantener enlaces relativos para documentos del checkout y enlaces fijados a un commit para las figuras externas.
- Registrar procedencia y comprobaciones en `logica 4.1/MANIFIESTO.md` y estado en `CONTEXTO_SESION.md`.
- Mantener intactos los archivos heredados fuera de esta carpeta para reducir conflictos con Alex-MD.
- Precedencia: las Aclaraciones mandan en estructura y presentación; las Bases Administrativas, Técnicas Transversales y el caso siguen regulando el contenido. Conservar las discrepancias documentadas y no completarlas por suposición.

## Mantenimiento de la versión alineada

- Los documentos canónicos son `LAFROX-Subdocumento4.md`, `LAFROX-Subdocumento4-Anexos.md` y `LAFROX-Formulario-T-11.md`.
- Conservar las partes y regenerar o cotejar los consolidados tras cada cambio; evitar revisiones técnicas divergentes.
- Fuente vigente de esta alineación: `rama-latex`, commit `732a9d6688569bf981594c2e21c47a167b8f8ba7`. El registro ADR está en 4-O y la memoria en 4-W.
- Leer `DISCREPANCIAS_FUENTE.md` antes de atribuir revisión humana, cumplimiento o aceptación al documento.
- Documentar conversiones y comprobaciones en `MANIFIESTO_ALINEACION.md` y `VERIFICACION_ALINEACION.md`.
