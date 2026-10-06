# LafroX — rama-latex

Esta rama consolida exclusivamente el Subdocumento 4. Su raíz contiene las carpetas `00` y `04`, los main y su ensamblador, el script de compilación y sus resultados, además de los metadatos internos de Git.

- `00`: plantillas originales, formato común vigente y trazabilidad del traslado.
- `04`: arquitectura lógica 4.1, física 4.2, centros de datos 4.3 y sus complementos.

La incorporación parte de `arquitectura-alvaro` (`e55133c2f91806af03f393776256a2feea23faa7`) y de `Alex_LASECUELA` (`5c5e27059675651dc26f8028ffbaa310950558b0`). El contenido técnico se conserva. Solo se adaptan rutas de figuras e importación, metadatos de las raíces y destinos internos del PDF. Los capítulos ajenos se excluyen de este árbol de trabajo; siguen disponibles en las ramas originales y en el historial.

## Archivos de trabajo

- [Raíz del documento completo](../main.tex).
- [Orden de incorporación](../contenido.tex).
- [Instrucciones de compilación y estructura](../04/README.md).
- [Manifiesto y huellas de origen/destino](trazabilidad/MANIFIESTO.json).
- [Correspondencia de archivos](trazabilidad/ORIGENES.md).
- [Asuntos conservados para revisión posterior](trazabilidad/PENDIENTES.md).

Las dos plantillas de origen permanecen íntegras en `00/plantilla/logica/` y `00/plantilla/fisica/`. Los tres PDF del Subdocumento 4 usan ahora la clase, portada e isotipos de `00/plantilla/formato-base/`, tomados de `rama-formato-Latex-base` (`624c9b0`). Los ajustes de integración están en las tres raíces `.tex`; ver [registro de aplicación del formato](trazabilidad/APLICACION_FORMATO_BASE_2026-10-06.md).

Esta consolidación no acredita cumplimiento total de las Bases ni aprobación del CLIENTE. Los textos, cifras, versiones y decisiones pendientes conservan exactamente su estado de origen.
