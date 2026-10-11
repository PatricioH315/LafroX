# Visibilidad del SD9 y documentos conectados

## Objetivo y alcance
Corregir diagramas recortados, tablas estrechas y títulos genéricos en SD9, anexos, T-13 y T-17. Preservar contenido técnico, relaciones, revisión humana pendiente y datos sin confirmar. Markdown y clase compartida son solo lectura.

## Ruta y previsión
Ruta delegada por preparación y escritura de múltiples archivos. Tres tareas. Previsión de 600–900 líneas de composición documental; estrategia ask-on-risk. Las diez fuentes nativas contienen 898 líneas. No se autoriza publicar. Sin commits: no incorporar cambios preexistentes del usuario; el coordinador conserva la decisión sobre la frontera de entrega. Espejo Engram a cargo del coordinador.

## Comprobación inicial
RED estructural observado: 83 paneles recortados y 10 vistas generales rasterizadas; títulos Detalle tabular; matriz de anexos con columnas Estado 1,1 cm y Ambiente 1,5 cm; listas de figuras vacías en documentos sin figuras. Documento visual pasivo: no hay prueba unitaria RED/GREEN pertinente; se comprueban fuentes, conservación, compilación y páginas renderizadas.

## Tareas
- [x] T1 Rediseñar diagramas SD9 y matrices nativas sin recortes, con todas las relaciones y textos originales. Diez entradas nativas; ocho grafos con 71 aristas originales, reproducidas en vista general y detalles independientes (142 conectores). Matriz 9.4 en dos paneles tabulares nativos de cuatro columnas; cronograma 9.9 en dos diagramas longitudinales, con meses, hitos, años, barras y leyendas del original. Tipografía de tarjetas y fuentes 9,5 pt, sin escalado de imágenes. Conservación documentada en figuras/visibilidad/conservacion.json.
- [x] T2 Mejorar tablas y títulos en documentos conectados. Matriz de anexos horizontal, Estado 3 cm y Ambiente 2,7 cm; saltos entre palabras, sin guionado automático en esa matriz. Conservados los 640 identificadores únicos de las 645 filas. Títulos descriptivos y numeración coherente T13/T17/9.A–D. T-13 mejora distribución y segmentación del perfil operacional. T-17 destina 3 cm a Campo y el resto al contenido; H11 completo en página 12. Listas de figuras vacías suprimidas localmente, sin modificar la clase.
- [x] T3 Compilar cuatro raíces y verificar advertencias, conservación y renderizados finales. Cuatro compilaciones latexmk satisfactorias, resultados y cobertura indicados abajo.

## Evidencia de compilación y conservación
Comando para cada raíz: latexmk -lualatex -interaction=nonstopmode -halt-on-error <raíz>.tex. Todos exit 0 con acceso aprobado a configuración MiKTeX. Primer intento restringido falló por RegOpenKeyExW, acceso al registro; no se modificó la instalación.
- LAFROX-Subdocumento9.pdf: 68 páginas; cero Overfull, caracteres ausentes y referencias indefinidas; un Underfull leve en etiqueta Fiabilidad de Figura 9.2.
- LAFROX-Subdocumento9-Anexos.pdf: 96 páginas; cero Overfull, Underfull, caracteres ausentes y referencias indefinidas.
- LAFROX-Formulario-T-13.pdf: 16 páginas; cero advertencias anteriores.
- LAFROX-Formulario-T-17.pdf: 15 páginas; cero advertencias anteriores.
Cero BORRADOR, títulos Detalle tabular y residuos de codificación en los cuatro PDF. Se mantienen 10/4/1/1 entradas REVISIÓN HUMANA, así como contacto y nomenclatura pendientes; no se simulan revisiones ni aprobaciones. Cero inclusiones de imágenes/recortes en el cuerpo. El mínimo extraído en las páginas de detalle es 8,966 puntos PDF, equivalente a 9 puntos TeX en leyendas; tarjetas de 9,5 puntos TeX.

## Cobertura visual
Renderizados Poppler de las 195 páginas finales, inspeccionados en nueve hojas de contacto. Alta resolución de todas las páginas de figuras y de los formularios; inspección ampliada de diagramas de detalle representativos, matriz 9.4, cronograma e hitos, primer/últimos bloques de matriz de anexos, perfil operacional T-13, H11 T-17 y declaración SD9. Las adiciones finales de leyendas de grupos/años se recompilaron y sus páginas 11 y 56 se renderizaron nuevamente. No se observaron nodos, títulos, flechas ni filas recortados en la comprobación final. Algunas tablas continúan legítimamente entre filas con encabezados repetidos. Los encabezados y pies SD9 66/67 están en los PNG finales; no se reprodujo el defecto de la revisión anterior. La presentación conjunta de imágenes en la herramienta puede ocultar zonas: contrastar con PNG individual y píxeles del archivo antes de diagnosticar el PDF.
Archivos de prueba bajo la carpeta de visualizaciones autorizada: poppler-*-sheet-*.png, poppler-*-hi-*.png, poppler-t13-*.png, poppler-t17-*.png, visibility-checks.json y registros build/final.

## Pendientes y siguiente paso
La mejora visual está implementada; no certifica la entrega contractual ni sustituye revisión humana. Inconsistencia técnica preexistente conservada y comunicada: Figura 9.9 original sitúa resiliencias de Operación en meses 26/32/38/44/50/55 y DR en 27/33/39/45/51/54; T-13 declara resiliencias 23/29/35/41/47/53 y DR 24/30/36/42/48/54. Requiere elegir programación válida y alinear con T-15; no se inventó un calendario nuevo. Persisten revisión humana, datos de portada y consolidación A-6 pendientes. Valoración nativa, revisión independiente y eventual commit de frontera acotada corresponden al coordinador; no se inició revisión sobre una candidatura preexistente no autorizada ni se hicieron operaciones remotas.
