# Manifiesto de procedencia y conversión

## Alcance

La conversión se realizó desde el repositorio LafroX vigente. No constituye revisión humana nueva, aprobación del contenido ni sustitución de la revisión formal de los PDF finales.

| Destino | Fuente | Transformación |
| --- | --- | --- |
| `Bases/*.md` | Los cuatro Markdown de `Bases/` | Copia íntegra, sin reescritura. |
| `01_presentacion_empresa/LAFROX-Subdocumento1.md` | `contenido.tex` y `tablas/equipo.tex` | Conversión de estructura, listas y tablas; organigrama transcrito a descripción textual. |
| `01_presentacion_empresa/LAFROX-Subdocumento1-Anexos.md` | `anexos.tex` | Conversión directa. |
| `01_presentacion_empresa/LAFROX-Formulario-T-6.md` | `LAFROX-Formulario-T-6.tex` | Formulario independiente convertido a tabla Markdown. |
| `02_problema_necesidad/LAFROX-Subdocumento2.md` | `contenido.tex`, `tablas/actores.tex` y `tablas/supuestos.tex` | Conversión de estructura, listas y tablas; seis procesos AS-IS transcritos a descripciones textuales. |
| `02_problema_necesidad/LAFROX-Subdocumento2-Anexos.md` | `anexos.tex` | Conversión de los listados detallados a tablas Markdown. |
| `Requerimientos/*.md` | Tres CSV originales de `Requerimientos/` | Conversión fila por fila; campos e identificadores preservados, incluidas celdas vacías. |
| `Revision/prompt_revision_comision_informe2.md` | Prompt vigente del Informe 2 | Se antepusieron reglas para evidencia por archivo/sección y controles pendientes del PDF. El prompt original quedó incorporado como referencia. |
| `compct/CONTEXTO_SESION.md` | Alcance y estado verificados del repositorio | Contexto compacto de reanudación y controles contra afirmaciones sin fuente. |

## Figuras transcritas

Se transcribieron exactamente siete figuras: el organigrama del Subdocumento 1 y los procesos AS-IS de preventa, recepción, cross-docking, planificación de rutas, reparto y rendición del Subdocumento 2. Cada ficha conserva título, fuente, nodos, secuencia, decisiones y excepciones visibles en la fuente.

## Exclusiones deliberadas

No se copiaron arquitectura, Subdocumentos 4–14, históricos, plantillas LaTeX, archivos binarios, herramientas de generación ni `03_esquema_solucion_alcance/tablas/generador/consolidado.json`.

## Incorporación a branch-md

Se importaron los 17 archivos Markdown de la copia local `LafroX-Markdown` a la raíz de `branch-md`, rama del repositorio LafroX. Se actualizaron únicamente AGENTS, README, este manifiesto y el contexto de sesión para reflejar la rama y su prohibición de trabajo en LaTeX. Los documentos, Bases y catálogos se conservaron byte a byte. La incorporación posterior del Subdocumento 3 se registra a continuación.

## Conversión del Subdocumento 3

Se importaron `contenido.tex`, `anexos.tex`, `LAFROX-Formulario-T-12.tex` y todos sus fragmentos incluidos. Además, los 14 fragmentos de `tablas_anexo/` se conservan en un apartado complementario del mismo Markdown de anexos, identificados por origen. No se ejecutaron generadores ni compiladores. Se preservan los títulos y las discrepancias existentes; no se acredita revisión humana nueva. Los índices y enlaces son navegación Markdown, no paginación PDF.

Fuentes leídas y huella SHA-256 de esta conversión:

| Fuente en LafroX | SHA-256 |
| --- | --- |
| `03_esquema_solucion_alcance/LAFROX-Formulario-T-12.tex` | `fad15940adf2de30b43b0b426068df9e79dc974f4499a51dc0b59758006fbf6f` |
| `03_esquema_solucion_alcance/anexos.tex` | `1fd5340d32a2020c99b6481bfabecee5124c234e10c4d820ab5b092e8873a1b0` |
| `03_esquema_solucion_alcance/contenido.tex` | `e0c62793d112a6cc5b7f8cfd36251aae8522d7264aaf27cc1de7229e6d3105eb` |
| `03_esquema_solucion_alcance/tablas/anx_correspondencia.tex` | `003de915cb509e28d22faaf090b589ca413cc260d8f201ef8da8d29879b9ede2` |
| `03_esquema_solucion_alcance/tablas/anx_decisiones.tex` | `0dec8dc5fa3553ace92ad960628a9ee5594ba769c40d68282e7e635beaeb862d` |
| `03_esquema_solucion_alcance/tablas/anx_exclusiones.tex` | `2b2af6f16e5810ed6f4a60f2fac2eb595f132f89ff16a7f56de94d6317704bd3` |
| `03_esquema_solucion_alcance/tablas/anx_glosario.tex` | `04df8ec26d1802784d33169037fffbdbea23db7bb8404455b42124e8a1c40903` |
| `03_esquema_solucion_alcance/tablas/anx_grupos.tex` | `02f1f49934f77e718d87b65798ca4980750f056c57927e1c5fb74fddbb261104` |
| `03_esquema_solucion_alcance/tablas/anx_r18.tex` | `771939f06a154ae9b6c7f810d97433ec07ddd5ef579530fe1dcdb556136dbade` |
| `03_esquema_solucion_alcance/tablas/anx_reglas.tex` | `2f29ac6ac8b76c4c7d1491e0e4040a15bdbe3ade68370b7208cc33a1b21621e1` |
| `03_esquema_solucion_alcance/tablas/anx_restricciones.tex` | `dcc5cbc097bdc06dc29457cebbbfc757f70e8be34bcc34476035802ab5889743` |
| `03_esquema_solucion_alcance/tablas/anx_rf.tex` | `b4d02766e3b3621df6bdec41e787f3cbea633604e3eec183d1377656b8640e72` |
| `03_esquema_solucion_alcance/tablas/anx_rf_vacios.tex` | `e136932a18d49f1ca57459158cc06786954d06b3721c1b801f45050759a57427` |
| `03_esquema_solucion_alcance/tablas/anx_rnf.tex` | `368a64553db5282b7722686753e45693d34c417d003d4b652c2543783a71a140` |
| `03_esquema_solucion_alcance/tablas/anx_rnf_vacios.tex` | `a255ef4b8da6587b064e5baace5e69fb9e958f9189a7e269794ee143b80a6aa5` |
| `03_esquema_solucion_alcance/tablas/anx_supuestos.tex` | `c38283a0714df28ed92a73ae7f155ca1f6d91af1e0ab083053a5e9fb2fd43314` |
| `03_esquema_solucion_alcance/tablas/anx_vacios.tex` | `eb6e00ab7f50fe6955b7776e45b4a68285af9937e5549f22f06a6dcb2a8e4dd9` |
| `03_esquema_solucion_alcance/tablas/declaracion_ia.tex` | `409f65f48291904eb898d4c2d51d3a747644d1163249d9d21636025749687f14` |
| `03_esquema_solucion_alcance/tablas/declaracion_ia_anexos.tex` | `1154f67037eb97e21ad3522505b6f2b5c5bfd08033368d099c10a8ffcf89dfcd` |
| `03_esquema_solucion_alcance/tablas/declaracion_ia_t12.tex` | `4f6e4b3576c6302c1f07dbe60d5255bf3d5aeb31c55d9d775ee6288e8c1efda9` |
| `03_esquema_solucion_alcance/tablas/t12_caso.tex` | `090188393b69e9bf2e58ca4d8020aeb3e19cc7f31ea5b9f7d6b6ec71571c35c7` |
| `03_esquema_solucion_alcance/tablas/t12_rt.tex` | `ba1f877ee1919d68ccf66092dc94641cc504c4cc91da81bd999ee828811f9a6b` |
| `03_esquema_solucion_alcance/tablas_anexo/capas.tex` | `6a33030cdd6134f3392afde672eb81f55f04ae1dd634a56df62244b3e3dbb2c3` |
| `03_esquema_solucion_alcance/tablas_anexo/decisiones.tex` | `a62fe9cf8f589fbd7ae31234cf9be043cf3ade18ac6208aa2c1de2fd3c136242` |
| `03_esquema_solucion_alcance/tablas_anexo/emplazamiento.tex` | `2cb63e7b96c7f69cfd1c9348cb7b9c3deccddb66c47e41137e97f80072b760d6` |
| `03_esquema_solucion_alcance/tablas_anexo/estrategia.tex` | `545a0ba8e511076adac50c7b8dbb5a0b77b6655a69774e75b630a3f4116b1057` |
| `03_esquema_solucion_alcance/tablas_anexo/exclusiones.tex` | `626963d7cf59ca00413730b14f9f4fbc6a9ca1c6c42dc3e095812de750b0a42b` |
| `03_esquema_solucion_alcance/tablas_anexo/hitos.tex` | `dc4977390bec17a4788718451ef55bc0f2d59061a3b90c8f50adbde2f1d2329c` |
| `03_esquema_solucion_alcance/tablas_anexo/reglas_negocio.tex` | `758a630cc7a5a508eec7f6b726456ec82843931154d231a8d8580b6a562cffa2` |
| `03_esquema_solucion_alcance/tablas_anexo/restricciones.tex` | `af97c6a8382314107d7ebaef40710c979f911db4ca2a0e92e7a46befad456f76` |
| `03_esquema_solucion_alcance/tablas_anexo/resultados_cap18.tex` | `8d473fa94d8f6581cc7f09453f37be725fb83a44f890e4508c02e425b4d41668` |
| `03_esquema_solucion_alcance/tablas_anexo/rf.tex` | `eea94a910cee6287ca814679dc2d14e959d92d02141903b283c08eb1bd86178d` |
| `03_esquema_solucion_alcance/tablas_anexo/rnf.tex` | `a80b22c932859ef139c53ea67142760b6d285be9aa3de0a4a47ee6244c8cb3b2` |
| `03_esquema_solucion_alcance/tablas_anexo/supuestos.tex` | `193854650f7480f5f7bd89e87677264f43706ca41d83e29fe542e266ac8ad76a` |
| `03_esquema_solucion_alcance/tablas_anexo/trazabilidad.tex` | `13ff945cd7437aff62bc57ecbdca44b2d758a13d8f30de5da964a05718ac250b` |
| `03_esquema_solucion_alcance/tablas_anexo/vacios.tex` | `841413b1096dd8837ee2710aaab789c3c1a014b42f1ea0730b82af45bdbfd240` |


2026-10-03: mejora SD5 autorizada en la rama de datos; cambio coordinado de responsabilidad tecnológica en SD1 y complemento Markdown CD-05 en SD4. No se modifica el alcance no ofertado de T-12.
