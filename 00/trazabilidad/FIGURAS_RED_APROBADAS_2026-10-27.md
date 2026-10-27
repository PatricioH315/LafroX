# LafroX — Integración de figuras de red aprobadas

El 27 de octubre de 2026 el usuario aprobó expresamente la demo de las figuras 24, 25 y 26 y pidió reemplazar sus versiones en LaTeX. La aprobación corresponde a la demo después de retirar los dos textos explicativos al pie de cada página.

## Activos y correspondencia

| Figura | Activo incorporado | Vista |
| --- | --- | --- |
| 24 | `04/figuras/fisica/Red_01_sitios_regiones_aprobada.pdf` | Sitios y regiones |
| 25 | `04/figuras/fisica/Red_02_red_local_aprobada.pdf` | Red local por tipología |
| 26 | `04/figuras/fisica/Red_03_red_aws_aprobada.pdf` | Red AWS y recuperación |

Las páginas se extrajeron del PDF aprobado sin redibujar ni reexportar. Se verificó identidad del contenido vectorial descomprimido y del texto de cada página frente a la demo. Sus huellas están en `FIGURAS_RED_APROBADAS_2026-10-27.json`. La fuente editable de tres páginas se conserva en `04/figuras/fuentes/fisica/Red_SD4_aprobada_20261027.drawio`.

Los tres PDF anteriores `Red_01_general_legible.pdf`, `Red_02_sitios_legible.pdf` y `Red_03_regiones_legible.pdf`, así como el diagrama original de red y su fuente, se conservan intactos. Los bloques de figura mantienen sus captions y etiquetas; solo se cambian las rutas de imagen. El generador histórico de vistas en tarjetas no genera los nuevos activos.

## Ajustes de correspondencia del texto

En 4.2.4.2 se precisa que Transit Gateway es regional y que las VPC se conectan a él, se distingue el número de túneles por conexión VPN del agrupamiento de caminos WAN, y la descripción de la replicación se remite a la figura 26. Son ajustes de correspondencia con los diagramas aprobados. Se conservan los bloques de direccionamiento, las tipologías de sitio, los objetivos de continuidad y las demás figuras.

La aprobación gráfica del usuario no acredita pruebas ejecutadas ni aceptación del mandante. Tras la integración y verificación, el usuario autorizó crear el commit «correcciones a diagramas» y enviarlo a `origin/subdoc-4`.

## Verificación

Se compiló el cuerpo con LuaLaTeX mediante `compilar.ps1 -SoloMain`, con tres pasadas y salida 0. El resultado conserva 194 páginas. El log final no presenta errores, referencias indefinidas, etiquetas duplicadas ni cajas desbordadas.

Se verificaron las etiquetas y captions de las figuras 24, 25 y 26, que permanecen en las páginas 133, 135 y 137, respectivamente. Se renderizaron e inspeccionaron completas esas tres páginas: gráficos aprobados presentes, rótulos y conectores visibles, sin recortes y sin los textos explicativos retirados de la demo. Las fuentes de las figuras permanecen fuera del dibujo como leyendas del documento.

Se comprobó que los cuatro PDF gráficos anteriores mantienen las huellas previas a esta integración. Las vistas previas de comprobación se guardan en `output/revision_red_20261027/integradas/`, fuera del checkout. `git diff --check` no informa problemas. Los anexos y T-11 no se recompilan en esta integración del cuerpo; sus cambios locales preexistentes proceden de la compilación solicitada anteriormente.
