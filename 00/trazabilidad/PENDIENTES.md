# Asuntos conservados para revisión posterior

La petición del usuario limita esta etapa a organizar los archivos y conservar íntegros los textos, tablas, figuras y anexos. Este registro identifica asuntos de integración; no los resuelve.

1. **Numeración y estructura de las vistas.** La lógica usa el capítulo 4 y la sección 4.1; la física utiliza capítulos rotulados 4.2 y 4.3. Se mantienen sus mecanismos originales, con destinos PDF diferenciados para evitar colisiones. La armonización editorial queda pendiente.
2. **ADR físicos.** El registro físico abre como apartado 4.4 en su fuente. Se conserva el archivo y su posición, sin trasladar ni modificar sus fichas. Su ubicación definitiva se decidirá en una revisión posterior.
3. **T-11 y memoria de cálculo.** Ambos continúan al final del cuerpo físico, conforme al ensamblador original, y cuentan además con raíces independientes. Eliminar su presentación provisional en el cuerpo requiere una instrucción posterior.
4. **Referencias y declaraciones de IA.** La lógica conserva sus cierres y los anexos lógicos también. El bloque físico conserva sus referencias propias. No se fusionan bibliografías ni se reubican declaraciones en esta etapa.
5. **Coherencia técnica.** Cotejar después tecnologías, interfaces, permisos locales, autonomía, protección externa, buffer, observabilidad, emplazamientos, capacidad y ADR. Una diferencia debe registrarse con evidencia y resolverse explícitamente; la consolidación no selecciona automáticamente una versión como ganadora.
6. **Correspondencia con capítulos externos.** Las menciones a 3.3–3.4, modelo de datos y otros subdocumentos se conservan, aunque sus archivos no estén en esta rama. No se importan documentos ajenos para completar esas referencias.
7. **Evidencia y aceptación.** Las condiciones de aceptación, ensayos y decisiones que las fuentes declaran pendientes siguen pendientes. Cambiar la organización de archivos no acredita su ejecución.
8. **Presentación final.** Los números de página y la maquetación pueden variar al compilar un único documento y utilizar una plantilla común para el integrado. Revisar en la siguiente etapa la uniformidad de índice, rótulos, anexos y formularios sin confundirla con preservación del texto.

Durante la revisión visual se amplió únicamente la columna de rótulos de las listas de tablas y figuras en `main.tex` (antes `04/main.tex`) para evitar que los identificadores originales `4.3-1`, etc., se superpusieran a sus títulos. No se renumeró ninguna tabla ni se cambió su título o contenido.

9. **[Resuelto 2026-10-07] Figuras de D41 (RT-03.14).** Las tres figuras ya muestran el par activo/en espera y la réplica sincrónica. `Arquitectura_Fisica_Crossdocking.png` y `Arquitectura_Fisica_CD_Concepcion.png` muestran un solo mini-PC y un solo servidor; `Arquitectura_Fisica_General.png` también debe revisarse. El texto ya describe el par activo/en espera; las figuras deben agregar el segundo equipo y la réplica sincrónica.

## Seguimiento vigente de trazabilidad SD4 — 11 de octubre de 2026

La continuación autorizada por el usuario registra los pendientes actuales P-01–P-13 en [la tabla de observaciones](../../04/revision/TRAZABILIDAD_REVISION_INFORME1_SD4.md). El [cotejo contractual](../../04/revision/COTEJO_TRAZABILIDAD_CONTRACTUAL_SD4.md) confirma 499 filas del T-12 con referencias SD4 y 75 filas con citas numéricas desactualizadas; no modifica T-12 ni otros entregables. Las fuentes efectivas tienen 29 figuras: racks 28 y recinto 29. El cotejo semántico completo, la legibilidad del PDF actual, los ensayos, la revisión humana y las decisiones contractuales permanecen pendientes según la matriz. Las entradas anteriores describen etapas históricas y no sustituyen este seguimiento.

Actualización de cierre: [las correcciones de Aclaraciones](../../04/revision/CIERRE_ACLARACIONES_SD4_2026-10-11.md) registran la revisión humana confirmada por el usuario con Álvaro Catalán como único revisor, los tres PDF compilados de 201/100/48 páginas y la comprobación visual de las páginas modificadas. Estos puntos sustituyen el estado pendiente anterior en su alcance; el cotejo semántico contractual completo, las doce citas sin folio original, los ensayos y las remisiones externas del T-12 mantienen sus pendientes. El usuario autorizó crear los commits locales de rama-md y subdoc-4, sin push; el espejo contiene 1.647/1.060/111 bloques sin diferencias.

## Formato de firma — 12 de octubre de 2026

Aplicado y verificado el formato solicitado del SD1 en los tres PDF del SD4, incluidas páginas horizontales. Detalle en [FIRMA_SD1_APLICADA_SD4_2026-10-12.md](FIRMA_SD1_APLICADA_SD4_2026-10-12.md). La revisión humana y los ensayos técnicos conservan su estado pendiente.

## Cadena de frío — 25 de octubre de 2026

Implementación documental aplicada en SD2–SD7. El registro `IMPLEMENTACION_CADENA_FRIO_2026-10-25.md` reúne las figuras congeladas que requieren actualización, las referencias fuera de alcance de SD9/SD13, los identificadores nuevos, las filas de declaración modificadas y el impacto futuro en Informe 3. Se conservaron todas las figuras y no se crearon entidades en SD5. Las pruebas físicas y las cotizaciones/certificados se especifican, sin acreditarse su ejecución. El T-14 conserva el aviso de ancho de su figura panorámica original, sin modificación de esa figura.

## Resultado de revisión semántica de formularios — 25-10-2026

El [registro semántico](REVISION_SEMANTICA_FORMULARIOS_2026-10-25.md) identifica las brechas de las 653 filas y las condiciones de los 98 recursos del T-11. Se conserva la exclusión de SD13: su vista de INN-03 requiere conciliarse con el kit y doble camino vigentes. La base por camión de un compartimento/una puerta se confirma mediante mapeo; los ocho PC nuevos y el inventario de la entrada SBD requieren detalle de ingeniería. Las brechas de oferta no se cerraron por compilar los PDF.
