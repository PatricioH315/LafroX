# LafroX — Antecedentes de auditoría de trazabilidad SD3

# LafroX — Trazabilidad de observaciones del Informe 1: Subdocumento 3

## Alcance y criterio de lectura

Tabla de observación–respuesta–sección modificada exigida por las Bases Administrativas, artículo 46°, y por el Formulario T-22, apartado «Informe y presentación 2». Se contrastan las observaciones de `Revision_informe.md`, apartado «SUBDOCUMENTO 3», más las generales que alcanzan al SD3, con:

- el Markdown actual de `rama-md`: `03_esquema_solucion_alcance/LAFROX-Subdocumento3.md`, `LAFROX-Subdocumento3-Anexos.md` y `LAFROX-Formulario-T-12.md`;
- el checkout LaTeX del SD3 (`../LafroX-sd3-latex`, rama `LafroX-Subdoc3-LateX`, HEAD `4214540`), sincronizado con el MD y compilado el 12-10-2026 con `latexmk -g`: cuerpo de 35 páginas, anexos de 168 y T-12 de 261, en carta. Los tres PDF contienen texto seleccionable. Después de compilar solo se homologaron dos rótulos en una tabla auxiliar que no se incluye en esos PDF.

Las páginas de la tercera columna son las del PDF recompilado («p.» = cuerpo; «Anexos p.» = PDF de anexos). MD y LaTeX tienen ahora el mismo contenido: se trasladaron al LaTeX los cambios de 55b65c6 (D-12, 9A-18, remisiones al T-13 §8.2 y al SD9 §9.2.5), las quince filas del T-12 alineadas después con SD9, SD13, T-13 y T-17, y la columna EDT autorizada posteriormente.

**Actualización posterior:** el T-12 mantiene seis columnas, incluida «Paquete EDT (T-14)», en Markdown y PDF; contiene 645 asignaciones. Los seis paquetes existentes del T-14 se ampliaron sin agregar paquetes. §3.2.3 del cuerpo y la descripción del Anexo 3.A están sincronizados con ese formato. La columna adicional fue solicitada expresamente por el usuario.

**Borrador de trabajo:** las observaciones se sintetizan fielmente; no son citas literales. «Documentado» significa que la respuesta está presente en el MD y en el PDF actuales, no que la Comisión la haya aceptado. «Parcial» y «Pendiente» identifican lo que no corresponde declarar resuelto.

**Balance de 43 observaciones (corte de esta actualización):** 42 cumplidas, documentadas o mantenidas; 1 pendiente bloqueante (3). Las observaciones 17, 20, 28 y 42 se cerraron el 12-10-2026 en MD y LaTeX; el cuerpo recompiló en 35 páginas y los anexos en 168. La observación 2 se actualizó al comprobar las firmas gráficas suministradas por el usuario en las tres portadas. La observación 7 queda en «Cumple», justificada por la vista general y su descomposición posterior; la Figura 3.4 está ahora en una página horizontal. La observación 9 se considera documentada en el alcance acordado: el paquete EDT figura en las 645 filas, y el texto MD/LaTeX y el PDF están sincronizados. Estos estados no equivalen a aprobación de la Comisión.

## Observaciones del Informe 1

Una fila por observación, en el orden del Informe 1: primero las generales que alcanzan a este subdocumento y luego las propias del subdocumento.

La matriz principal se trasladó a [LAFROX-Subdocumento3-Trazabilidad.md](../03_esquema_solucion_alcance/LAFROX-Subdocumento3-Trazabilidad.md). Este archivo conserva exclusivamente antecedentes de auditoría; no es el entregable de trazabilidad.


## Correspondencia con «Qué se espera en el Informe 2»

| Expectativa del Informe 1 | Estado | Filas |
|---|---|---|
| Documento de 25 a 35 páginas con esquema y diagrama, alcance por etapa y secciones de implementación, implantación y operación. | Cumplido (35 páginas). Vista general y descomposición posterior en figuras de detalle legibles. | filas 6, 7, filas 24–28 |
| Catálogos, supuestos, restricciones y decisiones en el T-12 y en anexos, con los campos del 17.1 y en tablas legibles. | Cumplido. Las tablas del PDF de anexos siguen siendo densas: 168 páginas. | filas 15, 16, filas 18, 19, 22 |
| T-12 con asignación de paquete EDT por requerimiento. | Cumplido en el alcance acordado: columna presente en las 645 filas y sincronizada a LaTeX/PDF. | fila 9 |
| Resolver la excursión térmica, arbitrar la promesa y alinear las etapas con el Art. 17°. | Cumplido. | filas 13, 36, 38 |
| Eliminar el precio. | Cumplido. | fila 39 |

## Pendientes antes de usar la tabla como registro de cierre

1. **Bloqueante:** completar con un integrante las 28 celdas `[[REVISIÓN HUMANA]]` (16 del cuerpo, 11 de anexos y 1 del T-12) con la revisión que realmente haga (fila 3).
2. **Obs. 7 cerrada en el criterio acordado y orientación corregida:** la Figura 3.4 sigue siendo general, justificada por las Figuras 3.5–3.8 de detalle. La p. 21 usa ahora `landscape`, con rotación de página de 90° y vista efectiva de 792 × 612 pt; figura, leyenda, cabecera y folio se leen horizontalmente. El cuerpo recompiló entonces en 34 páginas y se revisaron p. 20–22; no se alteró la imagen fuente ni el contenido del modelo.
3. **Resuelto:** las filas 17, 20, 28 y 42 se trasladaron al LaTeX (`contenido.tex` y `tablas_anexo/decisiones.tex`) y se recompilaron cuerpo (35 p.) y anexos (168 p.); MD y PDF coinciden. El T-12 no cambió.
4. **Resuelto:** nombres M10/M11 cotejados con SD4 y homologados como «M10 Analítica» y «M11 Canal moderno» en texto, Tabla 3.4, Figuras 3.4, 3.7 y 3.8 y fuente auxiliar de tabla; la denominación F-13 «Integración EDI Canal Moderno» se conserva por ser nombre de familia, no del módulo.
5. **Para el final:** completar la revisión humana efectiva de la fila 3 con quién revisó y qué verificó. Las firmas gráficas de las portadas ya están presentes y comprobadas (fila 2); no sustituyen esa revisión humana.

## Fuentes de cotejo

- [Revisión del Informe 1](../Revision_informe.md): «GENERAL», «SUBDOCUMENTO 3» y «CONSIDERACIONES TRANSVERSALES».
- [Subdocumento 3](../03_esquema_solucion_alcance/LAFROX-Subdocumento3.md), [Anexos](../03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md) y [Formulario T-12](../03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md).
- Checkout LaTeX `../LafroX-sd3-latex`, rama `LafroX-Subdoc3-LateX`, HEAD `4214540`: `LAFROX-Subdocumento3.pdf`, `LAFROX-Subdocumento3-Anexos.pdf` y `LAFROX-Formulario-T-12.pdf` compilados el 12-10-2026; la fuente auxiliar `tablas/sint_epicas.tex` no está incluida en el PDF.
- PDF originales del caso, BA y BTT en `FEP/` para los folios citados (folio impreso = página del visor − 1).
- [Aclaraciones](../Bases/aclaraciones-licitacion.md): estructura del Capítulo 3 y secciones 3 a 9.
- [Bases Administrativas](../Bases/Bases_Administrativas.md): artículo 46° y Formulario T-22.
