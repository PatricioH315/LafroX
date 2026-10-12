# LafroX — Cotejo de contenido SD4 Markdown y LaTeX

Revisión: 12 de octubre de 2026. Petición: comprobar que SD4 de `subdoc-4` y `rama-md` tenga el mismo contenido. Se leyeron las fuentes actuales de ambos checkouts, incluidos sus cambios locales pendientes. No se modificaron entregables, fuentes, figuras ni PDF; no se compiló ni se hizo commit o push.

Checkouts: `LafroX-rama-latex` en `subdoc-4` (HEAD `d42c58a0ca0490698344c995776d2aed08218b62`) y `LafroX-alvaro-md` en `rama-md` (HEAD `0afbfa149f907ff8e1de5f50e5cd69021cabc4ba`). Los HEAD identifican las bases: el resultado corresponde al contenido local pendiente, no certifica igualdad de versiones publicadas.

## Resultado

El contenido técnico y las palabras coinciden en cuerpo, anexos y T-11. No hay igualdad literal completa: quedan tres diferencias menores de puntuación sin cambio de sentido.

| Documento | Bloques MD | Bloques LaTeX | Diferencias de contenido normalizado |
| --- | ---: | ---: | ---: |
| Cuerpo 4.1–4.3 y cierre | 1.647 | 1.647 | 0 |
| Anexos 4-A–4-W y cierre | 1.060 | 1.060 | 0 |
| T-11 | 111 | 111 | 0 |
| Total | 2.818 | 2.818 | 0 |

## Diferencias de puntuación confirmadas

| Ubicación | Markdown | LaTeX |
| --- | --- | --- |
| Cuerpo: MD línea 2766; `04/partes/4.2_fisica/12_k_dimensionamiento.tex`, línea 76 | `re-despacho.` | `re-despacho..` |
| Anexo 4-W, fila INT-08: MD línea 1682; `04/anexos/fisica/16_anexo_4b_memoria_calculo.tex`, línea 217 | `1.400 × 11 % × 4, 2.600 × 11 % × 4` | `1.400 × 11 % × 4; 2.600 × 11 % × 4` |
| Anexo 4-W, piso de Talca y Concepción: MD línea 1780; mismo fuente, línea 302 | `1,5 kVA, 59 %` | `1,5 kVA; 59 %` |

La representación del signo menos (`−` frente a `-`) en una resta de mensajes y los delimitadores de `<dominio>` son diferencias de formato/conversión; conservan el mismo significado.

## Método y figuras

Se ejecutó `04/herramientas/auditar_espejo.py`, que expande las entradas `main.tex`, `04/anexos_logica.tex` y `04/formulario_T11.tex` y coteja secuencialmente su conversión en memoria con los tres Markdown. Incluye títulos, prosa, viñetas, cifras, referencias, filas de tablas y declaraciones de IA. Se excluyen navegación propia del formato y metadatos gráficos. Se complementó con una comparación que conserva puntuación y símbolos, revisando los casos distintos directamente en las fuentes.

Las 29 leyendas de figuras del cuerpo coinciden exactamente en título y orden con las 29 leyendas de las fuentes LaTeX. Los 29 enlaces de imágenes tienen activo existente y corresponden al mismo archivo usado en el checkout LaTeX. En enlaces fijados a un commit, se compararon los bytes del objeto Git con el activo local; en enlaces locales, se comprobó el archivo de destino. No se descargaron imágenes ni se accedió a la red.

Esta revisión comprueba correspondencia de contenido entre fuentes actuales; no es una nueva revisión visual del PDF, comprobación de cumplimiento contractual ni revisión humana de la oferta.
