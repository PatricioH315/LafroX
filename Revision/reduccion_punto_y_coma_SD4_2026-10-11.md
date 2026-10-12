# LafroX — reducción de puntos y coma del SD4

Petición: reducir su utilización y conservarlos donde permitan interpretar correctamente el contenido. Aplicado al cuerpo, anexos, T-11 y leyendas vectoriales inventariadas, sincronizando Markdown y LaTeX.

## Criterio aplicado

- Oraciones independientes y condiciones: punto seguido y mayúscula inicial.
- Enumeraciones simples: coma, manteniendo el orden de los elementos.
- Enumeraciones complejas: conservar el punto y coma cuando los elementos contienen comas o elipsis y necesitan separación inequívoca.
- Citas: conservarlo para distinguir fuentes o referencias diferentes dentro de una misma cita.
- Sintaxis técnica de LaTeX y estilos XML: conservar los separadores que no son puntuación visible.

Se conservaron palabras, cifras, códigos y decisiones técnicas. En la introducción se completó la elipsis «Los centros de datos corresponden a 4.3.» para evitar una oración incompleta. Álvaro Catalán sigue como único revisor en las 132 filas de la declaración de IA.

## Resultado

Los tres Markdown pasan de 1.763 a 118 signos: 46 en cuerpo, 59 en anexos y 13 en T-11. Además se sustituyeron los 12 signos de 11 figuras vectoriales, conservando operaciones gráficas y geometría. Se guardaron originales en el directorio de comprobación del checkout LaTeX. Las figuras modificadas del Markdown enlazan sus archivos locales actuales.

El conteo del texto extraído de los PDF se registra por separado en `entrega/_build/qa_puntuacion_sd4/verificacion.json`, porque mide el resultado de la composición. La reducción es de aproximadamente un 93 % respecto del inventario inicial de 1.775 apariciones.

Verificación final: PDF cuerpo 46 signos y 201 páginas, anexos 61 signos y 100 páginas, T-11 13 signos y 48 páginas. Comparación Markdown–LaTeX: cero diferencias en los bloques cotejados de los tres documentos. Compilación sin referencias indefinidas, caracteres ausentes ni cajas Overfull.

Comprobaciones: recompilación de los tres PDF, comparación de bloques de contenido Markdown–LaTeX, revisión de registros de compilación e inspección visual de páginas de texto, tablas y las 11 figuras modificadas. El inventario PC-0001–PC-1775 se conserva como registro histórico anterior a esta corrección.

Fuentes y PDF permanecen en `LafroX-rama-latex`, rama `subdoc-4`. En `rama-md` sólo se editaron documentos Markdown. Sin nuevo commit ni push.
