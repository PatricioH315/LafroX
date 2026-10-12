# LafroX — Revisión de puntos y coma del SD4

**Registro histórico previo a la corrección.** La reducción autorizada posteriormente se documenta en [Reducción aplicada](reduccion_punto_y_coma_SD4_2026-10-11.md). Las cifras y ubicaciones de este inventario describen la versión anterior.

Fecha: 11 de octubre de 2026. Fuentes locales publicadas: rama-md y subdoc-4. Revisión de puntuación solicitada por el usuario; no se modificaron cuerpo, anexos, T-11, fuentes LaTeX ni figuras.

## Conteo y alcance

El inventario contiene **1.775 apariciones numeradas individualmente**. Los tres Markdown aportan 1.763 signos; el texto seleccionable del PDF aporta doce adicionales que están dentro de figuras vectoriales. La extracción integral de los PDF da 862 en cuerpo, 700 en anexos y 213 en T-11. No se cuentan separadores de programación LaTeX o estilos de los archivos de dibujo. Las imágenes rasterizadas no fueron sometidas a OCR: el conteo corresponde al texto de los documentos y a las figuras con texto seleccionable.

| Documento | Apariciones | Numeración global | Inventario comentado |
| --- | ---: | --- | --- |
| Cuerpo | 862 | PC-0001–PC-0862 | [Abrir](punto_y_coma_SD4_cuerpo_2026-10-11.md) |
| Anexos | 700 | PC-0863–PC-1562 | [Abrir](punto_y_coma_SD4_anexos_2026-10-11.md) |
| T-11 | 213 | PC-1563–PC-1775 | [Abrir](punto_y_coma_SD4_T11_2026-10-11.md) |

## Cómo leer los comentarios

Cada fila identifica una aparición del signo, no sólo un párrafo. Si una línea contiene cinco puntos y coma, se registran cinco números. La ubicación textual indica línea, columna y posición del signo dentro de esa línea. Los fragmentos muestran el signo revisado en negrita; las líneas completas se consultan mediante su enlace.

Las recomendaciones son editoriales: un punto y coma admisible no se considera automáticamente un error. Se conserva cuando separa citas, códigos o elementos complejos. Se propone punto seguido cuando divide afirmaciones completas, y reorganización cuando la frase o celda acumula demasiadas ideas. En condiciones y excepciones se mantiene expresamente el vínculo lógico. Una modificación de signos nunca debe cambiar cifras, permisos, dependencias ni criterios de aceptación.

Los conteos por categoría cuentan signos, no errores ni párrafos distintos. Una recomendación de revisión indica una oportunidad de mejorar la lectura, no una incorrección demostrada.

## Clasificación contextual

| Uso | Cantidad |
| --- | ---: |
| Párrafo denso | 446 |
| Dos ideas relacionadas | 404 |
| Separación en tabla | 349 |
| Referencia | 280 |
| Celda extensa | 161 |
| Contraste o condición | 69 |
| Condición en tabla | 27 |
| Lista de códigos | 16 |
| Texto de figura | 12 |
| Enumeración | 9 |
| Conector lógico | 2 |

## Observaciones de mayor interés

1. **Introducción del capítulo:** PC-0001 separa la arquitectura lógica de la física. Recomiendo dos oraciones: «…capítulo 3. La arquitectura física…».
2. **Catálogo de anexos en 4.1:** los seis signos de la línea 129 son una enumeración compleja. Están justificados; no recomiendo sustituirlos todos por comas.
3. **Correspondencia de vistas en 4.1:** la línea 131 mezcla una elipsis y dos comprobaciones. Los comentarios proponen frases completas y puntos seguidos.
4. **Citas y listas de identificadores:** conservar los separadores necesarios para distinguir requisitos y documentos dentro de paréntesis o matrices.
5. **Párrafos densos:** dar prioridad a los casos marcados «Priorizar revisión». Dividir por responsabilidades, condiciones y consecuencias; evitar una sustitución automática global.
6. **T-11 y anexos:** numerosos signos compactan especificaciones. Revisar por celda y por atributo; una ficha técnica admite separaciones que en un párrafo del cuerpo resultarían pesadas.
7. **Figuras:** los doce casos adicionales tienen comentario específico en el inventario del cuerpo. Destacan las leyendas nominales de las Figuras 17 y 25, donde un rótulo o dos líneas pueden resultar más claros.

Los tres inventarios son la lista exhaustiva del alcance textual señalado. No se realizó reemplazo de puntuación, commit ni push.
