# LafroX — rama-md

Repositorio de fuentes documentales en Markdown para redactar y revisar la propuesta de la licitación ficticia TFEP-01/2026, Caso 02 — Logística. El conjunto local vigente incluye los Subdocumentos 1–8 y 13, con sus anexos y formularios disponibles.

## Guía de lectura — 8 de octubre de 2026

La carpeta [Resumen/](Resumen/README.md) contiene 26 guías independientes y un índice: nueve subdocumentos, siete archivos de anexos (66 anexos individuales) y diez formularios. Cada guía explica propósito, ideas principales, cifras y decisiones, y enlaza al original y sus secciones. Se elaboró a partir de las fuentes locales vigentes, incluidos los cambios disponibles sin registrar; es material de consulta y no un entregable contractual adicional ni una acreditación de revisión humana.

## Contenido

- [`Bases/`](Bases/): cuatro documentos rectores y su precedencia normativa.
- [`01_presentacion_empresa/`](01_presentacion_empresa/): Subdocumento 1 y Formulario T-6 independiente; sin archivo de anexos complementarios.
- [`02_problema_necesidad/`](02_problema_necesidad/): Subdocumento 2 y anexos.
- [`Requerimientos/`](Requerimientos/): los tres catálogos CSV originales convertidos íntegramente a tablas Markdown.
- [`Revision/`](Revision/): prompt de revisión del Informe 2 adaptado a fuentes Markdown.
- [`MANIFIESTO.md`](MANIFIESTO.md): procedencia y reglas de conversión.
- [`compct/CONTEXTO_SESION.md`](compct/CONTEXTO_SESION.md): contexto vigente, controles contra alucinaciones y estado de reanudación.

La carpeta `04_arquitectura/` contiene exclusivamente [Subdocumento 4](04_arquitectura/LAFROX-Subdocumento4.md), [anexos](04_arquitectura/LAFROX-Subdocumento4-Anexos.md) y [Formulario T-11](04_arquitectura/LAFROX-Formulario-T-11.md). Las decisiones pendientes de coherencia se conservan en el contexto general de sesión; los documentos futuros no se consideran disponibles por mencionarlos.

## Rama de trabajo

Esta copia se trabaja actualmente en `rama-md`, según la comprobación del 8 de octubre de 2026 y el plan autorizado para la carpeta Resumen. `alvaro-md`, `branch-md` y `LafroX-Markdown` identifican estados y procedencia históricos. La creación de estas guías no incluye commit ni publicación.

Se rechaza toda petición de trabajo en LaTeX dentro de `branch-md` para preservar su integridad. Consultar `AGENTS.md` y `compct/CONTEXTO_SESION.md` antes de trabajar.

## Subdocumento 3 incorporado

- [Cuerpo](03_esquema_solucion_alcance/LAFROX-Subdocumento3.md).
- [Anexos y material complementario recibido](03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md).
- [Formulario T-12](03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md).

Se conservan las discrepancias de requerimientos por instrucción del usuario. Los catálogos originales de `Requerimientos/` no fueron reemplazados.


La coordinación de reserva comercial y custodia física se consulta en las [reglas de reconciliación del Subdocumento 4](04_arquitectura/LAFROX-Subdocumento4.md#sec:reglas-reconciliacion) y en sus anexos G, I, N y V. Los registros de conversión y copias por partes se conservan en el historial Git, fuera de la estructura vigente de entregables.
