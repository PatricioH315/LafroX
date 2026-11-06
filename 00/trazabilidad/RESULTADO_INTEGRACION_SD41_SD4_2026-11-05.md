# LafroX — Integración verificada de 4.1 en SD4 corrigiendo

Fecha: 5 de noviembre de 2026. Registro interno de ejecución; las fuentes de subdocumentos siguen siendo LaTeX y sus PDF. Este documento forma parte del commit de merge que consolida ambas líneas de trabajo.

## Puntas integradas

- Destino previo: `31221b23f92122136cfcb59554da18fb6b0dacab`, corrección de máximos coincidentes de TPS.
- Origen: `964736de83cf175b899cbbd56d940bf05407f303`, que incluye `8e00de50b02c837eb6a61165e7d740c349e2ab6f` (cambios de recorreccion logica) y el plan versionado por separado.
- Base común: `b68ba316d61b7c2d8b129fc16c4a468b22fd4b50`.
- Rama destino local: `LafroX-Subdoc4-LateX-corrigiendo`.
- Checkout separado: `D:/Usuario/Documents/Proyecto_Lafrox/tmp/sd4-corrigiendo-integracion`.

## Protección y resolución

Se guardaron copias de los PDF originales de destino, el parche de cambios locales y huellas de archivos del checkout original. Se crearon referencias de recuperación `respaldo/sd4-corrigiendo-antes-merge-20261105` y `respaldo/sd41-antes-integracion-20261105`.

La integración se preparó en la rama temporal `integracion/sd41-a-sd4-corrigiendo-20261105`. Los únicos conflictos fueron los dos PDF ensamblados. Se regeneraron desde las fuentes combinadas; no se eligió un PDF antiguo de una rama como resultado final. No se modificaron las fuentes técnicas durante esta resolución.

Los 30 archivos no PDF del commit técnico de 4.1 se conservan exactamente. El plan se incorporó con su cierre actualizado. Los diez archivos propios del cambio TPS de destino distintos de los dos PDF conservaron su contenido exacto, incluidos fuentes/cálculo de TPS y T-11. También se preservó todo archivo de destino no afectado por los commits entrantes.

El checkout original sigue en la rama 4.1. Sus 205 archivos locales inventariados, excluido el plan que se versionó deliberadamente, conservan sus huellas. Los cambios anteriores de AGENTS y T-11 no se incluyeron en el merge. La plantilla se tomó de la fuente versionada en el checkout limpio, sin copiar los wrappers locales sin seguimiento del origen.

## Comprobaciones realizadas

- `python -B Dimensionamiento/dimensionamiento/verificar_tps.py`: correcto. Verifica Tabla 14, 24 horas, 288 tasas por representación, máximos y ensayos.
- Máximos conservados: 12,34 TPS normal, 3,76 TPS despacho normal, 6,94 TPS despacho de septiembre y 14,66 TPS máximo de septiembre. Los ensayos separados conservan 21,99 TPS y 10,41 TPS.
- Tres pasadas de LuaLaTeX por cada PDF final, sin referencias indefinidas, etiquetas/destinos duplicados ni desbordes.
- Inspección visual de Figura 1, trazabilidad, identidad, soporte, protocolos y páginas de TPS del cuerpo y anexos. Figura 1 conserva letra mínima de 10,41 pt al tamaño final.
- Índices y referencias estabilizados; los dos PDF incluyen ambas líneas de corrección.
- Origin se consultó de nuevo antes del cierre y seguía en `31221b23`.

Las verificaciones corresponden a integración, documentación, cálculos y PDF. No acreditan ejecución de los protocolos de aceptación sobre una aplicación operativa ni revisión humana adicional.

## PDF integrados

- `entrega/LAFROX-Subdocumento4.pdf`: 192 páginas; SHA-256 `d15db8d7f4ed60f88a45496e2bb9d9357f9eb0d9470724d48167871e1de33579`.
- `entrega/LAFROX-Subdocumento4-Anexos.pdf`: 128 páginas; SHA-256 `bcfb18848907f8832f71f0e940b9d18a2e66bf0d07343445ca629ecf09a3672a`.

## Trazabilidad y alcance del cierre

Este registro y el plan actualizado se incluyen con las fuentes y los PDF en el commit de merge. Sus dos padres permiten identificar las puntas conservadas sin reescribir la historia. La rama temporal se convierte en la rama destino local solo tras la verificación. No se ejecuta push; origin conserva su estado remoto previo.

Respaldos, registros de compilación, capturas y verificaciones: `D:/Usuario/Documents/Proyecto_Lafrox/tmp/sd4-integracion-respaldo-20261105/`.
