# Aplicación del formato común al Subdocumento 4

Fecha: 6 de octubre de 2026. Rama de trabajo: `rama-latex`.

## Origen y alcance

Se incorporaron sin alterar `lafrox.cls`, `lafrox-portada.tex` y los dos isotipos de `origin/rama-formato-Latex-base` (`624c9b0`) en `00/plantilla/formato-base/`. Las clases de origen lógico y físico permanecen en sus rutas históricas para preservar la trazabilidad del traslado.

Las tres raíces (`main.tex`, `04/anexos_logica.tex`, `04/formulario_T11.tex`) apuntan a esa única clase y usan los isotipos de la misma carpeta. Se retiraron los parches de portada y pie que buscaban campos ausentes en el formato base. El principal usa los índices de la clase y conserva la numeración corrida de figuras y tablas. Para mantener el contenido de 4.2 y 4.3, `main.tex` agrega `placeins` y el comando de fuente de figuras, presentes en la clase anterior pero ausentes en la base.

No se modificaron los fragmentos técnicos de `04/partes/`, anexos ni formularios para este cambio de presentación. El cambio de diseño altera la paginación. La fecha y los datos institucionales existentes se conservaron; su validez editorial sigue siendo materia de revisión independiente.

## Comprobación

LuaLaTeX completó tres pasadas sin errores para los tres archivos. Resultados con el nuevo formato: cuerpo 146 páginas, anexos 80 páginas y Formulario T-11 32 páginas. Se verificaron visualmente las tres portadas, una página de prosa y páginas de tablas continuadas. La tercera pasada no mostró referencias o citas indefinidas. Persisten algunos avisos de cajas anchas en el cuerpo y el formulario; su máximo fue 8,35 pt y 14,52 pt respectivamente, menor o igual al observado en la compilación previa.

`compilar.ps1` conserva los tres nombres de salida en `entrega/` y ahora detecta la instalación privada de MiKTeX si `lualatex` no aparece todavía en el PATH.
Se ejecutó el script completo después de la revisión, con salida correcta para los tres PDF de `entrega/`. Antes de actualizarlos se guardó una copia local de los PDF existentes en `entrega/_build/antes-formato-base-2026-10-06/`.
