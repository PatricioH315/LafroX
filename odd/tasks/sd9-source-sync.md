# Sincronización de las fuentes revisadas del SD9

## Objetivo y alcance

Traer los cambios de `Subdoc/LafroX/SD9_v_nueva` a los cuatro entregables de `09_plan_calidad/v_nueva`, preservando español, estructura Markdown, figuras Mermaid y marcadores de revisión humana. Las fuentes LaTeX se leen; no se escriben ni compilan. `v_vieja`, T-14 y los informes Revision quedan fuera del alcance.

## Autorización y ruta

El usuario confirmó que `rama-md` es la nueva `branch-md`; no se cambia de rama. Ruta delegada: lectura preparatoria y cambios documentales coordinados. Previsión: aproximadamente 180 líneas autorales añadidas y eliminadas; estrategia `ask-on-risk`, sin publicación ni PR. Se actualizará la identidad obsoleta en AGENTS.md y el contexto. No hay prueba RED significativa para una importación documental pasiva.

## Tareas y criterios de aceptación

- [x] SD9-SYNC-01: trasladar redacción, citas, tablas mensuales, restauración y declaraciones de IA desde las fuentes activas, sin corregir silenciosamente inconsistencias ajenas; actualizar identidad de rama.
- [x] SD9-SYNC-02: verificar inventario de secciones, correspondencia de texto y tablas, enlaces locales, estructura y whitespace; registrar cierre, diferencias preservadas y estado de commit.

## Comprobaciones

- Comparación normalizada de cuerpo, anexos, T-13 y T-17 con `contenido.tex` activo de cada uno.
- Tablas con número de celdas uniforme; anclas del índice existentes; enlaces locales resolubles.
- `git diff --check`; inventario exclusivamente `.md`; hashes de T-14 y Revision preservados.
- N/A: ejecución de pruebas, compilación, renderizado PDF y revisión humana.

## Progreso

Exploración completa: nuevas tablas mensuales, cambios de explicación/citas y declaración de IA en cuerpo; roles y paquetes de restauración en T-13; nota de fechas en T-17. Anexos coinciden en contenido. Bases-alignment anterior del cuerpo fuera de `v_nueva` queda intacto. Sincronización y verificación completadas. Siguiente paso: spot-check del coordinador y resolución del commit pendiente; sin push.

## Resultado y evidencia

Sincronizados cuerpo, T-13 y T-17; anexos sin diferencias sustantivas. Nuevas Tablas 9.11 y 9.12: 21 filas mensuales y cinco filas de fase; antiguas 9.11/9.12 renumeradas 9.13/9.14. Figura 9.9 Mermaid adaptada a la vista de meses de la fuente (hitos puntuales colocados al inicio del mes como coordenada gráfica, no como fecha contractual).

Comparación normalizada de todos los párrafos, cabeceras y filas activas: cero diferencias pendientes en cuatro documentos. Estructura: 62 tablas uniformes, 89 encabezados y 21 enlaces de índice válidos; siete marcadores humanos preservados en el cuerpo. Las referencias, listas y figuras existentes se conservan; no se acredita revisión humana. Hashes de T-14 y los dos informes Revision preservados durante la escritura. `git diff --check`: salida 0.

Inconsistencias de la fuente preservadas, no corregidas: el párrafo 9.3.3 cita 36 restauraciones de Operación y añade meses 13–20; además dice «Cada tipo mantiene una separación máxima de seis meses» aunque la intrusión es anual. No se modificaron T-14, Bases, SD8, planillas ni LaTeX. Rollback: los tres entregables de v_nueva y las notas de seguimiento/identidad de esta unidad, sin revertir cambios ajenos. N/A: prueba RED, runtime o PDF. Commit pendiente a cargo del coordinador; sin push.
