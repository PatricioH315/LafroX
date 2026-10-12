# Auditoría de indicios de IA (Aclaraciones §7.1 a–d) — Subdocumento 13 — 11 de octubre de 2026

Documento interno del equipo, no entregable. Revisa el Subdocumento 13, sus anexos y el Formulario T-19 contra los cuatro indicios del §7.1. Desde el Informe 2, un solo indicio deja el subdocumento completo en 0, sin subsanación (Art. 55.2).

**Material revisado:** los tres PDF compilados desde LaTeX (`SD13_v_nueva`: 52, 15 y 14 páginas), que es lo que recibe la Comisión, y sus fuentes Markdown en `13_innovaciones/`.

## 1. Resultado por indicio

| Indicio | Qué se revisó | Resultado |
| --- | --- | --- |
| a) Figuras y tablas integradas | 34 leyendas del cuerpo (28 tablas y 6 figuras) y 7 de los anexos: cita antes, análisis después, títulos seguidos de tabla o lista sin frase, leyendas «Fuente: elaboración propia.» sin fuente de datos. | Sin hallazgos. Las 6 figuras están dibujadas (draw.io) y cada una se cita antes y se explica después. |
| b) Cifras derivables y líneas base obtenibles | 19 datos del Caso, 7 del SD4 y 10 citas a otros subdocumentos y RT: merma 1,7 %, 1.100 SKU refrigerados, 18 + 10 camiones con frío, 11.600 almacenes, 38 % al contado, 10.920 lecturas (6.048 + 4.872), congelamiento del 1 al 25 de septiembre, vencimiento de la suspensión en septiembre de 2026, entrevistas citadas, OTIF 90/93/95 %, Anexo 8.F O8-01, inicio en febrero de 2027, entre otros. | Sin hallazgos. Todas las cifras se encuentran en la fuente citada. Las líneas base sin historia se declaran «Sin medición» y las reducciones se presentan como metas de diseño, no como resultados. |
| c) Contradicción con otro subdocumento | SD1, SD4, SD7, SD8, T-12, T-14, T-15 y T-16. | **Pendiente externo:** el T-14 todavía asigna 8.3.2, 8.3.5 y 8.3.6 a DAT e IMP y cuenta las revisiones de 8.3.2 «desde el inicio de Operación». Se corrige en el SD7. El acoplamiento de INN-03 con el RT-05.30 en el T-12 es un riesgo del Art. 30°, no una contradicción. |
| d) Marcadores, notas, referencias inexistentes, cuadros en blanco, ruptura de la ficción | Texto completo de los tres PDF con 40 patrones (marcadores, notas de proceso, nombres de archivo, curso y docencia, «falta», «pendiente», «no acreditada», entre otros). | **Crítico:** las 16 celdas «No acreditada» de la Declaración de uso de IA equivalen a cuadros de aprobación en blanco. **Corregido:** las filas 17 y 21 del Anexo 13.D citaban la observación con «Asignatura, Unidad, Profesor», «curso» y «notas del asistente»; se reformularon. El resto de las coincidencias son falsos positivos («falta de señal», «recursos», «Investigación adicional declarada», que exige el RT-26). |

## 2. Arreglos aplicados en esta auditoría

| Indicio | Qué se corrigió | Dónde |
| --- | --- | --- |
| d | Filas 17 y 21 de la Tabla 13.D.2: «datos ajenos a la licitación» y «notas de proceso dentro del entregable», en lugar de citar los términos del curso y del asistente. | `13_anexos/contenido.tex` y `LAFROX-Subdocumento13-Anexos.md` |

## 3. Pendientes que bloquean la entrega

1. **Revisión humana de la IA (indicio d, crítico).** Las 16 filas de la Declaración de uso de IA (11 en el SD13, 4 en los anexos y 1 en el T-19) dicen «No acreditada», y el texto previo afirma que la revisión no está acreditada. Cada fila debe indicar el integrante, su rol y qué verificó, solo con revisiones que hayan ocurrido (`Revision/plantilla_revision_humana_IA.md`). Al completarlas, se elimina la frase «La revisión humana aún no está acreditada…».
2. **T-14 (indicio c).** Columna «Resp.» de 8.3.2, 8.3.5 y 8.3.6, y frase «contados desde el inicio de Operación». En corrección por el equipo del SD7.

## 4. Pasajes que el grupo debe poder explicar en una interrogación

La Comisión puede pedir que se explique cualquier pasaje (§7.1, último párrafo). Estos son los de mayor carga técnica:

- Modelo cinético de Arrhenius o Q10 y cómo se integra la carga térmica sobre la historia del lote (13.3.2).
- Por qué el reordenamiento de la cola en la reconexión no deja rastro en un reporte de fallos (13.2.2) y cómo se forman los pares de I-02A (13.2.6).
- Umbral mínimo por grupo, supresión de celdas y k-anonimidad en el bloque 4 de INN-05 (13.5.2).
- Puntuación del tramo variable (reducción comparable dividida por 5 %, acotada entre 0 y 1) y la canasta congelada (13.4.2).
- Escala TRL y por qué cada innovación parte en TRL 2 (13.N.3).

## 5. Formato de la Declaración de uso de IA (Aclaraciones §7.2)

Segunda pasada sobre los Markdown sincronizados con LaTeX. La §7.1 repite el resultado de la sección 1: las únicas coincidencias reales son las 16 celdas «No acreditada».

| Requisito de la §7.2 | SD13 | Anexos | T-19 |
| --- | --- | --- | --- |
| Va al final, después de las Referencias | Cumple | Cumple | Cumple |
| Texto breve antes de la tabla | Cumple | Cumple | Cumple |
| Seis columnas con los nombres exactos | Cumple | Cumple | Cumple |
| Una fila por sección, anexo y formulario | Cumple (11 filas: introducción, 13.1 a 13.5, 13.A a 13.D y T-19) | Cumple (4 filas) | Cumple (1 fila) |
| Niveles de la escala (Ninguno, Bajo, Medio, Alto) | Cumple | Cumple | Cumple |
| Consolidación en el Formulario A-6 | Declarada | Declarada | Declarada |
| Revisión humana: quién y qué verificó | **No cumple** (11 celdas «No acreditada») | **No cumple** (4) | **No cumple** (1) |

**Corregido en esta pasada:** el Anexo 13.D declaraba nivel «Medio» en texto, pero su matriz de trazabilidad se reconstruyó completa con asistencia de IA el 11 de octubre. Pasa a «Alto», con la finalidad actualizada, en la declaración del SD13 y en la de los anexos. Declarar menos uso del real se evalúa como uso no declarado (§7.2, último párrafo).

**Al completar la revisión humana**, cada integrante debe confirmar también que el nivel declarado de su fila corresponde a lo que el grupo hizo. «Medio» exige que el grupo haya reescrito y verificado el borrador; si no fue así, corresponde «Alto».
