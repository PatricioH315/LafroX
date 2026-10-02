# LafroX — Subdocumento 4

Esta carpeta amplía el contenido heredado de `Alex-MD` con la arquitectura lógica del apartado 4.1. La ampliación fue solicitada expresamente por el usuario el 1 de octubre de 2026 para trabajar en una nueva rama llamada `alvaro-md`.

## Contenido incorporado

- [Arquitectura lógica: cuerpo completo del Subdocumento 4.1](<logica 4.1/LAFROX-Subdocumento4.1.md>).
- [Anexos 4.1-A a 4.1-V e índice trazable](<logica 4.1/LAFROX-Subdocumento4.1-Anexos.md>).
- [Manifiesto de conversión, fuentes y huellas SHA-256](<logica 4.1/MANIFIESTO.md>).
- [Contexto de trabajo de esta incorporación](CONTEXTO_SESION.md).
- [Arquitectura física, centros de datos y complementos importados de rama-latex](MD_4.2_2.3/README.md).
- [Procedencia y huellas de la importación física](MANIFIESTO_IMPORTACION_FISICA.md).

El cuerpo y los anexos lógicos se mantienen separados, siguiendo la organización de las carpetas 01, 02 y 03 de Alex-MD. Se incorporó además la carpeta `MD_4.2_2.3` desde `rama-latex`, commit `95ed2c9a1cc20aa7ad9f3ebbe03cafa0e1e1259c`, con sus 15 Markdown: física, centros de datos, ADR, referencias, T-11 y memoria de cálculo. Se conservan la organización y el contenido de origen, ajustando únicamente enlaces externos. No se fusiona ni armoniza la lógica con la física en esta operación.

## Procedencia y compatibilidad

La rama `alvaro-md` se creó desde `Alex-MD`, commit `09ace4cea5b96ca641368c56996367ff7f26ea50`. El contenido lógico se convirtió desde `arquitectura-alvaro`, commit `e55133c2f91806af03f393776256a2feea23faa7`, leyendo el ensamblador LaTeX y sus 50 fragmentos de cuerpo y anexos. Se conserva el texto técnico, incluidos sus supuestos, decisiones y pendientes; la conversión no constituye una nueva auditoría de cumplimiento.

Todos los archivos añadidos son Markdown. Los capítulos 1, 2 y 3, las Bases y los archivos compartidos heredados permanecen intactos para facilitar un futuro merge con Alex-MD. Las instrucciones y manifiestos propios de 4.1 se guardan aquí y no sustituyen los de la raíz.

Las 14 figuras se identifican mediante enlaces a los originales fijados al commit de origen, junto con sus títulos, fuentes y explicaciones de lectura. No se sustituyen los diagramas ni los recortes aprobados por dibujos nuevos. Consultarlos requiere acceso a GitHub; no se incorporan binarios al checkout Markdown.

## Navegación

El índice del cuerpo permite recorrer sus apartados; el catálogo de anexos enlaza los 22 anexos y mantiene sus requisitos asociados. Los números de página propios del PDF se reemplazan por enlaces a secciones. Los apartados Referencias y Declaración de uso de IA se conservan en ambos documentos.
