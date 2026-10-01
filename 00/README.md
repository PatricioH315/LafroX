# LafroX — rama-latex

Esta rama consolida exclusivamente el Subdocumento 4. Su raíz contiene las carpetas `00` y `04`, además de los metadatos internos de Git.

- `00`: plantillas originales y trazabilidad del traslado.
- `04`: arquitectura lógica 4.1, física 4.2, centros de datos 4.3 y sus complementos.

La incorporación parte de `arquitectura-alvaro` (`e55133c2f91806af03f393776256a2feea23faa7`) y de `Alex_LASECUELA` (`5c5e27059675651dc26f8028ffbaa310950558b0`). El contenido técnico se conserva. Solo se adaptan rutas de figuras e importación, metadatos de las raíces y destinos internos del PDF. Los capítulos ajenos se excluyen de este árbol de trabajo; siguen disponibles en las ramas originales y en el historial.

## Archivos de trabajo

- [Raíz del documento completo](../04/main.tex).
- [Orden de incorporación](../04/contenido.tex).
- [Instrucciones de compilación y estructura](../04/README.md).
- [Manifiesto y huellas de origen/destino](trazabilidad/MANIFIESTO.json).
- [Correspondencia de archivos](trazabilidad/ORIGENES.md).
- [Asuntos conservados para revisión posterior](trazabilidad/PENDIENTES.md).

Las dos plantillas de origen permanecen íntegras: la del apartado lógico se usa para sus compilaciones independientes; la de Alex se usa para el documento integrado, el T-11 y la memoria física. No se reescribe ninguna clase para armonizar estilos.

Esta consolidación no acredita cumplimiento total de las Bases ni aprobación del CLIENTE. Los textos, cifras, versiones y decisiones pendientes conservan exactamente su estado de origen.
