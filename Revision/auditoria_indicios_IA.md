# Auditoría de indicios de IA (Aclaraciones §7.1 a–d) — 8 de octubre de 2026

Documento interno del equipo, no entregable. Revisa las carpetas 01 a 08 y 13 contra los cuatro indicios del §7.1. Desde el Informe 2, un solo indicio deja el subdocumento completo en 0, sin subsanación (Art. 55.2).

## 1. Advertencia principal: llevar los cambios a LaTeX

El PDF entregable se compila desde LaTeX. **Todos los cambios de texto de esta auditoría están solo en el Markdown** de `rama-md`. Hay que replicarlos en las fuentes LaTeX antes de compilar; si no, el PDF conserva los indicios. Para ver cada cambio, usar `git diff` sobre `rama-md`. La lista de control de figuras está en la sección 5.

## 2. Arreglos aplicados

| Indicio | Qué se corrigió | Dónde |
| --- | --- | --- |
| d | Se eliminaron los marcadores «Insertar figura 5.X». Las 10 figuras PNG que ya estaban en `05_modelo_datos/Diagramas/` quedaron enlazadas, y se quitó un ancla huérfana (`fig-migracion`). | SD5 y SD5-A |
| d | Las Bases dejaron de atribuirse a la «Pontificia Universidad Católica de Valparaíso (PUCV)». Ahora se citan como Distribuidora Puelche S.A. (2026a–d), con las letras remapeadas en el texto. | SD4, SD4-A, T-11, SD5 y SD5-A |
| d | Se quitaron menciones al proceso de redacción y al curso: «redactor del Subdocumento 3», «Informe 1/2», «clases FEP02», «láminas de Tomás», «conversión Markdown/LaTeX», «se generan al compilar», «estado actual de este archivo», «figura histórica», «programación anterior», «lectura histórica», «versión anterior publicaba…» y «Modelo… provisional». | SD3, SD3-A, SD4, SD5, SD5-A, SD7, SD7-A, T-14, T-15 y SD13-A |
| d | Las notas pendientes se reescribieron como compromisos con responsable y hito: «falta verificar…», «se necesita contrastar…», «objetivos no medidos» y el Anexo 7.F completo. | SD3, SD7, SD7-A y SD8 |
| d | El título fuera del índice «Base vigente de planificación» pasó a 7.3.8, con texto limpio. Los subtítulos del SD7 se numeraron (7.1.1 a 7.3.8), así que las citas «sección 7.3.2», etc., ahora apuntan a secciones que existen. | SD7 |
| d | Se quitaron 2 figuras obsoletas del T-14 (cartas por cuenta con la programación anterior). | T-14 |
| d | Se quitaron los restos de LaTeX: «[-1pt]», «raiz → raiz», «$→$», «$m$», los 47 renglones «Relación entre nodos» y las 23 frases «No sustituye la revisión visual del PDF». | SD7, T-14, T-15, T-18, SD8 y SD13 |
| d | Las citas a etiquetas («Tabla «tab:7-…»») pasaron a números (Tabla 7.N, T14.N, 13.N…), con las leyendas numeradas. | SD7, SD7-A, T-14, T-15, T-18, SD13 y SD13-A |
| d | Se quitaron los restos de la conversión desde PDF: 42 marcas de página, pies y encabezados de página, «continúa en la página siguiente», tablas partidas, descripciones de logotipos y nombres «….pdf». Las oraciones cortadas se volvieron a unir. | SD2, SD2-A, T-6 y SD1 |
| d | Las fechas posteriores a la emisión se unificaron al 05-10-2026 o se quitaron: portadas del SD5 y el SD6, consulta de RabbitMQ y todas las filas de IA. | SD4-A, SD5, SD6 y declaraciones de IA |
| d | Se normalizaron las 24 declaraciones de IA y se agregaron las que faltaban (T-6, T-11 y T-18). Cada una tiene las 6 columnas del §7.2, sin filas vacías ni fechas, y sin las frases «No documentada», «No realizada», «Revisión final no realizada», «se consolida antes de entregar», «Actualización del 6 de octubre…» ni «Texto de caída». Las revisiones con nombre del SD1 y el SD2 se conservaron. | Todos |
| a | SD2: las 6 figuras quedaron en el orden cita → pasos → figura → análisis. Se quitaron las 6 leyendas duplicadas «Transcripción textual», las leyendas citan su fuente de datos y se agregó el análisis de la Tabla 2.3. | SD2 |
| a | SD6: la Tabla 6.3 bajó a 5 columnas. Se agregó el análisis de la Tabla 6.2, la Tabla 6.4 (cálculo del valor ganado al mes 10 con la curva del T-15: PV 35.006 HH, SPI 0,95, CPI 0,97) y la Tabla 6.5 (comités, numerada). | SD6 |
| a | SD7: se agregó la Tabla 7.4 (HH por etapa, que suman 202.774) con su análisis, y se renumeraron las tablas siguientes. | SD7 |
| a | SD8: las 5 tablas del cuerpo quedaron numeradas y tituladas (8.1 a 8.6). La tabla «Rol \| Responsabilidad» pasó a «ámbito de riesgos que vigila». Se agregó la Tabla 8.4 (los 5 riesgos de mayor NPR) con su análisis y el análisis del reparto de la contingencia. | SD8 |
| a | Se agregaron frases introductorias después de los títulos que iban seguidos directamente de una lista o tabla (20 casos). | Varios |
| b | El umbral «≤ 0,3 % contractual» se declaró como meta de diseño, con la base de 2,3 % del caso. Las «entrevistas a actores clave» y el «levantamiento en terreno» se reescribieron como entrevistas del Caso, cap. 8. | SD5 y SD2 |
| c | Stack: Python/Django y SonarQube del SD1 se alinearon con Laravel/PHP, Kotlin y PHPStan/Larastan (SD4, SD6 y T-11), y se quitó la salvedad del T-15. La duración de las iteraciones del SD7 ahora remite al SD6. | SD1, T-15 y SD7 |
| — | `AGENTS.md` y `CONTEXTO_SESION.md` ya no mandan usar descripciones textuales como figuras, y prohíben notas de proceso en los entregables. | Guía del repositorio |

## 3. Pendientes para el equipo (bloquean la entrega)

1. **Revisión humana de la IA.** Quedan 204 celdas `[[REVISIÓN HUMANA]]`. Se completan con `Revision/plantilla_revision_humana_IA.md`, anotando quién revisó y qué verificó realmente. No se entrega mientras `grep -r "REVISIÓN HUMANA"` encuentre alguna.
2. **Contradicciones de diseño que no se corrigieron por decisión del equipo** (indicio c, riesgo de 0):
   - «Terminales, GPS y cámaras» en SD6 l.111 y T-14 (5.4.2), cuando el S-13 del SD2/SD3 dice que no hay cámaras.
   - Starlink en 3 sitios (SD6 y T-14 5.3.3) frente a 5 enlaces (SD4 y T-11 D-06).
   - Sala técnica en el mes 5 (SD6 Tabla 6.3) y «sala desde el mes 4» (T-15 l.93), frente a los meses 2 a 4 (T-14 y tablas del T-15).
   - Nombres de módulos: SD4 Tabla 8 (M7 Rendición, M8 Devoluciones, M9 Calidad) y Tabla A.14 (M4 Ruteo, M5 Picking y carga…) frente a la Tabla 3.4 del SD3.
   - INT-04 «a Talca» (SD7-A l.177) frente a «a la nube» (SD4).
   - Hitos dentro del T-14: «integración mes 16 (H9)», aunque H9 es el mes 17. «Antes H7/mes21» en T-16 y SD8-A debe decir H7 (mes 16) y H12 (mes 21). «Meses 5 y 8» frente a los meses 6 a 8 del Gantt.
3. **Cifras sin derivación (indicio b):**
   - «Hasta 16 evaluadores por día» (SD6, T-15 y SD8-A): las referencias se apoyan unas en otras sin mostrar el cálculo.
   - Ocupación mínima de 60 % y metas OTIF de 90/93/95 % (SD3): indicar si son metas de LafroX o del caso.
   - Metas de merma de 1,0 % y de envases de 7 % (SD2): declararlas como metas de diseño.
   - Números de certificado (SD1 l.193–196): mantenerlos solo si se respaldan en el Sobre 1.
4. **Leyendas «Fuente: elaboración propia.» sin fuente de datos:** quedan alrededor de 50 en el SD4 y algunas en SD1, SD6, SD8 y SD13. No son el indicio a), porque hay figura o tabla, pero conviene completarlas con «a partir de …».

## 4. Verificado sin hallazgos

- No queda ninguna de estas expresiones: «Insertar figura», «[cite», «??», «TODO», «borrador», «PUCV», «Informe 1/2/3», «docente», «profesor», «estudiante», «académico», «FEP0», «No sustituye la revisión visual», «[-1pt]», ««tab:», «del PDF», «No documentada», «No realizada» ni «[Integrante».
- Los usos que siguen son de dominio y están bien: «pendiente de preparación», estados PENDIENTE, «en curso», «no sustituye el POD», «interfaces no documentadas» del caso.
- Ninguna tabla del cuerpo supera las 5 columnas, salvo las de IA, que tienen el formato del §7.2.
- Todos los enlaces de imagen locales existen.
- Los únicos títulos que siguen directamente a una tabla o lista son los índices y las listas de tablas y figuras.

## 5. Lista de control para el checkout LaTeX

| Figura | Qué confirmar |
| --- | --- |
| SD2, Figuras 2.1 a 2.6 | Que exista la imagen BPMN y que la leyenda cite «a partir de Distribuidora Puelche S.A. (2026c), capítulos 4 y 8». |
| SD3, Figuras 3.1 a 3.4 | Que estén las imágenes. La Fig. 3.4 se explica por sus líneas de colores: confirmar que la imagen coincide. |
| SD4, Figura 18 | En el Markdown tiene leyenda pero no imagen. Confirmar que existe en LaTeX; si no, retirarla. |
| SD4, Figuras 1 y 2 | Enlazan archivos `.pdf`, válidos en LaTeX. Confirmar que no son recortes. |
| SD4, Figuras 3, 4, 5, 7, 8, 11, 12 y 13 | Usan `capas_recortes/`. El §4 prohíbe recortes: usar una figura completa por capa si lo son. |
| SD5, Figuras 5.1 a 5.7 y A5.1 a A5.3 | Incluir los PNG de `Diagramas/`. |
| SD6 | El capítulo no tiene figura. Se recomienda agregar el ciclo RUP con las puertas DevSecOps. |
| SD7, Figuras 7.1 a 7.12; T-14, T-15 y T-18 | Que las imágenes TikZ se compilen. En LaTeX, quitar las 2 cartas obsoletas del T-14 (cuentas, meses 1 a 21). |
| SD8, Figura 8.1 (RBS) | Dibujarla. Hoy es una lista. |
| SD13, Figura 13.1 | Dibujar el mapa de las innovaciones sobre las capas. Se recomienda una figura del flujo de historia térmica en 13.3. |
