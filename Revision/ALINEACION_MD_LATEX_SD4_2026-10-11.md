# LafroX — Espejo Markdown y LaTeX del Subdocumento 4

## Alcance

El usuario autorizó commit y push y exigió igualdad de contenido entre ambos formatos. `rama-md` mantiene exclusivamente Markdown; las fuentes, figuras y PDF se conservan en `subdoc-4`. `04_arquitectura/` mantiene exactamente cuerpo, anexos y T-11, sin copias auxiliares.

El avance de `cf43057` a `d8bc438` preservó el trabajo local SD4 mediante el stash `respaldo SD4 antes de sincronizar y publicar 2026-10-11`, reaplicado sin conflictos. Se conservan los demás stashes y `md para drive/`. No se editan entregables ajenos al SD4 ni el T-12.

## Versión LaTeX comprobada

Commit publicado y verificado en origin: `c4d1230c9246f1a50933a8dc8a9a07b5d13a10be` (`subdoc-4`). Los 27 enlaces de figuras del Markdown apuntan a sus activos en ese commit, no a una rama mutable ni a una propuesta anterior.

## Controles

| Entregable | Bloques cotejados | Diferencias normalizadas |
| --- | --- | --- |
| Cuerpo 4.1–4.3 | 1.579 | 0 |
| Anexos 4-A–4-W | 948 | 0 |
| T-11 | 110 | 0 |

La comparación secuencial incluye párrafos, viñetas, títulos, cifras, referencias y filas de tabla. Se normalizan sintaxis de énfasis, espacios, símbolos y macros de presentación; navegación y metadatos gráficos se comprueban aparte. Coinciden 27 títulos y números de figura, con 27 activos existentes. Los 342 enlaces internos entre los tres entregables tienen destino y ancla válidos.

Se trasladaron a LaTeX las especificaciones vigentes de módulos, ASN/acuse, seguridad, Preproducción y herramientas de pruebas que faltaban, incluida la cámara premium del MC9400. El Markdown incorpora el diagrama de red corregido y la figura de emplazamiento ya existente en LaTeX, con referencias renumeradas. Los resúmenes del SD4 se actualizaron.

XML aprobado del diagrama de red: SHA-256 `912bf7b551a9bd005b9e8f00b39d265faa7ff34221b6934f33cf4ee33b841aac`, idéntico al archivo enviado por el usuario. La Figura 24 queda en 4.2.4.2, página 132 del PDF actual. No se alteró su diseño.

Compilación LaTeX: cuerpo 191 páginas, anexos 91 y T-11 46, sin referencias indefinidas, desbordamientos ni caracteres faltantes. Se revisaron visualmente las páginas afectadas; persiste el aviso histórico de nombre/ruta de clase. Los rótulos menores del diagrama de red impreso quedan próximos a 5 puntos: no se acredita un mínimo de 9 puntos.

## Límites y dependencia externa

La igualdad entre formatos no constituye conformidad contractual total, prueba ejecutada ni revisión humana. El riesgo residual de RPO y los ensayos conservan su estado.

Cinco referencias del T-12 requieren ajuste por renumeración, fuera del alcance autorizado: RT-06.02, RT-06.03, RT-06.22 y RT-06.30 deben citar Figura 27 (recinto), y RT-06.05 Figura 26 (racks). No se modifica el Subdocumento 3 en esta tarea.

[Registro y controles reproducibles en LaTeX](https://github.com/PatricioH315/LafroX/blob/c4d1230c9246f1a50933a8dc8a9a07b5d13a10be/04/revision/ALINEACION_MD_LATEX_2026-10-11.md).
