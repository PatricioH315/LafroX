# Asuntos conservados para revisión posterior

La petición del usuario limita esta etapa a organizar los archivos y conservar íntegros los textos, tablas, figuras y anexos. Este registro identifica asuntos de integración; no los resuelve.

1. **[Resuelto 2026-10-27] Numeración y estructura de las vistas.** Armonizada la jerarquía editorial de la vista física y centros de datos bajo el Capítulo 4 (Arquitectura del Sistema): se eliminó la redefinición artificial de `\thechapter` en `04/partes/4.2_fisica/contenido.tex`, convirtiendo Arquitectura física y Data center en secciones (`\section`), desplazando sus divisiones a `\subsection`, `\subsubsection` y `\paragraph`, garantizando numeración unificada y continua (`4.2`, `4.3`, etc.) en el índice y marcadores PDF sin colisiones de hipervínculos.
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

## Figuras de red aprobadas — 27-10-2026

El usuario aprobó las nuevas vistas de las figuras 24–26, sin textos explicativos al pie, y autorizó su integración en el cuerpo. Los activos anteriores se conservan. Alcance y verificación en [el registro de integración](FIGURAS_RED_APROBADAS_2026-10-27.md). Esta aprobación gráfica no cierra los ensayos ni las condiciones contractuales de continuidad.

## Estudio de cobertura y red inalámbrica — 6 de noviembre de 2026

D45 cerró el estudio de cobertura en el SD4 (Anexo 4-W.13). Queda pendiente:

- **Figuras (solo a pedido del usuario):** la Figura 28 (racks del CD Talca) no dibuja el par de controladores CW9800L en U30 de R02 ni la ocupación de 13U. La figura del CD Talca no muestra los controladores ni el RADIUS de VM-05.
- **SD3, resuelto** en `LafroX-Subdoc3-LateX-CORRIGIENDO` (`c38619fa`): T-12 (RNF-13.09, RT-03.23, RT-03.24 y RT-06.11 con 9,2 kW) y S-36.
- **SD7, resuelto** en `LafroX-Subdoc7-LateX-CORRIGIENDO` (`1779817f`): 2.1.2 entrega el estudio verificado en el mes 2, 5.1.2 incluye la red inalámbrica, 6.2.3 y 6.3.4 se aceptan con la cobertura medida; espejo Markdown y K4 actualizados, T-14 sin cambio de páginas. Las filas S4-12 y S8-16 de su trazabilidad siguen sin completar, como el resto de esa tabla.
- **SD8:** la revisión pide llevar la cobertura en cámaras al registro de riesgos (S8-16). La nota TR-11 propone no crear un riesgo por defecto; hay que conciliar ambas posturas.
- **Autoridad certificadora y MDM, resuelto en D46:** AWS Private CA y Microsoft Intune quedan nombrados en el SD4 y el T-11.
- **Convención (resuelta el 7 de noviembre de 2026):** la sección de cobertura quedaba fuera del grupo que numera el Anexo 4-W y salía como «4.13»; ahora sale como «4-W.13», igual que las doce anteriores y que las citas del texto.

## Plano acotado del recinto de Talca — 7 de noviembre de 2026

D47 declaró la superficie (≈ 31 m² en cinco recintos, Tabla 26 del 4.3.1.4). Queda pendiente:

- **Figura 29 (a pedido del usuario, al final):** reemplazar el esquema por líneas por un plano en planta acotado, con escala, cotas de cada recinto, puertas, racks y climatización, conforme a RT-06.03. Hoy la figura todavía muestra «Zona de respaldo y repuestos» separada y bitácora, videovigilancia y tablero como zonas.
- **SD3, al cambiar la figura:** la fila RT-06.03 del T-12 dice «Plano de distribución interna por zonas y líneas de acceso»; debería decir «plano acotado».

## Correcciones de 4.1 — 8 de noviembre de 2026

- **Vigencia de reparto verificada en las fuentes y los PDF.** La asignación se emite en la hora anterior a la salida y vence 30 min después del fin programado, con un máximo de 16 h desde la emisión. Se armonizaron 4.1, el Anexo 4-G y dos menciones de continuidad en 4.2. Las 14 h corresponden al mínimo contractual de autonomía sin señal. Se comprobó la regla temporal de AL-ID-01 para emisión al salir y 30/60 min antes de una ruta de 14,5 h.
- **Figuras 1, 2, 4, 6 y 7.** Por instrucción del usuario, la Figura 1 vuelve a usar el original ARQL-01. Las demás usan las imágenes incrustadas en «LafroX - Presentación Informe 2 v10 alterna» (diapositivas 9, 11, 12 y 13 de la copia más reciente), como base visual. Las figuras 4, 6 y 7 usan los doce nombres de módulos del Anexo 4-D. La Figura 4 conserva el recorte del listado de actores. La Figura 1 original se conserva. Por instrucción del usuario, la vista visual de los recorridos central y local se incorpora como Figura 1a, «Resumen lógico», después de la explicación general de 4.1.3. El requisito de legibilidad de la Figura 1 original queda pendiente. La referencia a la página 6 dentro de la Figura 7 pertenece a la vista de la presentación.
- **Pendiente la revisión humana de esta versión.** Registrar nombre, fecha y alcance de la revisión del texto, anexos y figuras de 4.1 y de las referencias de vigencia corregidas. Las revisiones anteriores y la compilación no acreditan este cierre.
