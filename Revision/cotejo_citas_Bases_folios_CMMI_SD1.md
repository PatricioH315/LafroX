# LafroX — Cotejo de citas, folios del T-6 y CMMI

## Resultado y alcance

11 de octubre de 2026. Revisión solicitada de los tres ajustes del SD1: citas a las Bases, foliación horizontal del T-6 y nomenclatura CMMI. Se leyeron los PDF originales escaneados mediante OCR local y se comprobaron visualmente las páginas relevantes, incluidos sus folios. El OCR sirve para localizar, no para asignar páginas sin verlas.

No se editaron entregables Markdown, fuentes LaTeX ni PDF. Las correcciones indicadas abajo están comprobadas y listas para aplicarse, pero no se presentan como realizadas. No hubo commit/push. Rama Markdown verificada: rama-md; fuente SD1 verificada: LafroX-Subdoc1-LateX.

## PDF fuente y numeración

| Fuente | Ruta original | Páginas físicas | SHA-256 |
|---|---|---:|---|
| BA | C:/Users/alexa/Desktop/Universidad/FEP/Bases Administrativas.pdf | 77 | 7837DC76BD0454F7BC212A64699976F7C111EA9513B2627BD1C1D82A80F0377C |
| BTT | C:/Users/alexa/Desktop/Universidad/FEP/Bases Técnicas Transversales.pdf | 51 | CA500672FB2882EE55B76BB7B7B90D30E4C45216C725811EC2F242164EE47E1E |
| Caso | C:/Users/alexa/Desktop/Universidad/FEP/Caso 02 - Logística.pdf | 41 | 3394651E5730F89B5ACE672B29365268D3D974B823624D0E33F1650219345B0F |

Los folios impresos de las páginas consultadas están desplazados una posición respecto al visor: por ejemplo, Art. 34° está en p. 22 impresa y página 23 del visor. **La cita del entregable debe usar el folio impreso.** No se utilizó el PDF con «Claude» en el nombre ni se tomaron los Markdown del SD4 como sustitutos del original. El checkout LafroX-subdoc4/Bases contiene copias Markdown; los originales se localizaron directamente en FEP.

## Páginas verificadas para las citas

Esta tabla cubre las remisiones explícitas a las Bases presentes en cuerpo, anexos y T-6 y añade las fuentes necesarias para subsanar atribuciones incompletas. Las líneas indicadas corresponden a contenido.tex actual; si se edita, pueden desplazarse.

| Pasaje o aplicación | Documento y disposición | Folio impreso | Página del visor | Acción |
|---|---|---:|---:|---|
| Sitio corporativo, línea 19 | BTT §23.1, RT-23.01 a RT-23.10 | 39 | 40 | Completar documento, sección y página; el rango actualmente figura solo. |
| Arquitectura modular, línea 25 | BA Art. 19° | 14 | 15 | Añadir página. |
| Arquitectura modular, línea 25 | BTT §2.2, RT-02.02 | 6 | 7 | Añadir página. |
| Atención crítica/alta, líneas 31 y 74 | BA Art. 78.2 | 40 | 41 | Añadir página en ambas menciones. |
| Horario de mesa, líneas 31 y 74 | Caso cap. 15, RT-21.06 | 27 | 28 | Fuente directa del horario 04:00–22:00 y peaks; no sustituye la remisión interna a SD3. |
| Metodologías y capacidades, línea 197 | BTT §23.1, RT-23.04 | 39 | 40 | Añadir página. No atribuir a este requisito la concesión de una evaluación CMMI. |
| Pruebas de intrusión, líneas 209 y 213 | BTT §11.3, RT-11.20 | 24 | 25 | Añadir página; confirma tercero independiente, anual y antes de cada paso a producción. |
| Experiencia y acreditaciones, líneas 224, 234 y 236 | BA Art. 34.1 | 22 | 23 | Añadir página en las menciones aplicables. |
| Entrega de certificaciones en Sobre 1, línea 224 | BA Art. 39°, numeral 4 | 25 | 26 | Complementar Art. 34°, que fija idoneidad pero no basta para localizar el contenido del sobre. |
| Certificaciones institucionales, línea 234 | BTT §15.2 | 28 | 29 | Añadir página; ISO 9001 obligatoria vigente, ISO 27001 vigente o plan; ISO 20000-1 deseable vigente o plan declarado. |
| Equivalencia de proyectos, línea 243 / Tabla 1.5 | Caso §§2.2–2.4 | 4–5 | 5–6 | Añadir páginas para cifras, flota, personas y temperatura. |
| 99,95 % de infraestructura, línea 243 / Tabla 1.5 | BTT §6.1 y §7.2, incluida su tabla por componente | 14 y 17–18 | 15 y 18–19 | **Corregir fuente:** no procede atribuir este porcentaje al cap. 10 del caso. Para la comparación por componentes, citar §7.2, pp. 17–18; §6.1, p. 14, acredita el recinto técnico. |
| Proyecto 3 no híbrido, línea 264; alianzas, línea 337 | BA Art. 16.1 | 11 | 12 | Añadir documento y página a ambas menciones. Art. 16° completo continúa en p. 12. |
| Duración y fases contractuales, línea 289 | BA Art. 17.1 | 12 | 13 | Añadir página. Esta fuente prueba fases; no asigna por sí sola los roles del proyecto. |
| Roles mínimos, líneas 291, 302 y fuente Tabla 1.6, línea 306 | BTT §19.2 | 33–34 | 34–35 | Añadir las dos páginas: Implantación continúa en la segunda. |
| Gerente de servicio, línea 298 | BTT §21.1, RT-21.02 | 35 | 36 | Añadir página. |
| Facultades y dedicación del jefe, línea 331 | BTT §19.1, RT-19.02 | 33 | 34 | Citar tras la primera oración. |
| Control de cambios, segunda oración de línea 331 | BTT §19.1, RT-19.03; BA Art. 72° | 33 BTT; 38 BA | 34 BTT; 39 BA | **Corregir atribución:** RT-19.02 no regula control de cambios. Separar las citas de ambas oraciones. |
| Vigencia de certificaciones y reemplazos, línea 333 | BTT §15.3, RT-15.09; BA Arts. 76.1–76.2 | 28 BTT; 39 BA | 29 BTT; 40 BA | Añadir páginas. Traslape de 15 días hábiles y autorización escrita confirmados. |
| Cartas de referencia, anexos | BA Art. 34.1 | 22 | 23 | Añadir folio. Esta página exige carta del mandante para experiencia específica; no autentica la existencia de las cartas locales ni demuestra su envío. |
| Introducción del T-6 | BA Art. 34.1; Formulario T-6 | 22 y 56 | 23 y 57 | Añadir folio de Art. 34° y, si se cita el origen de los once campos, el del propio formulario. |

Las Aclaraciones aportadas están en Markdown sin foliación fija. Sus remisiones a §§1 y 7.2 se conservan por sección; no se inventa un número de página. La bibliografía de una Base completa no debe sustituir las páginas de los pasajes citados.

### Dos errores de referencia confirmados

1. **Disponibilidad:** el caso cap. 10 (p. 19 impresa) contiene restricciones operacionales, no el porcentaje 99,95 %. La cifra de la Tabla 1.5 puede conservarse, pero debe atribuirse a BTT y explicarse con su alcance de infraestructura. No equipararla con el SLA de transacción de negocio ni con los SLA históricos del T-6.
2. **Control de cambios:** RT-19.02 respalda facultades/dedicación del jefe; RT-19.03 y BA Art. 72° respaldan el procedimiento y aprobación de cambios. Ambos RT están en p. 33 BTT; usar esa misma página no elimina la necesidad de corregir el código.

## Foliación del T-6

Comprobadas visualmente sus páginas 4, 5 y 6: el contenido está horizontal, pero el pie empresarial y el número quedaron girados en el borde izquierdo. El defecto persiste en las tres hojas. No hay que reducir los once campos ni llevar la tabla a una sola página.

**Causa:** el formulario usa el entorno landscape de pdflscape, mientras los estilos fancyhdr de la clase conservan los pies de la hoja vertical. La rotación final del PDF no recoloca automáticamente el folio.

**Corrección acotada propuesta:** definir un tratamiento de folio horizontal sólo en el T-6 y sólo durante sus tres hojas de experiencia, suprimir allí el folio vertical para evitar duplicación y dibujar el número derecho y legible en la esquina inferior derecha de la orientación final. Cubrir tanto el estilo plain de la primera hoja como las continuaciones. Restaurar el estilo ordinario al salir del entorno. No modificar la clase común por defecto, ni tocar cuerpo/anexos por este ajuste.

**Prueba requerida tras aplicarlo:** recompilar T-6, comprobar folios 1–7, páginas 4–6 con un único número horizontal abajo a la derecha, encabezados repetidos, filas íntegras, vínculos del índice y conservación de las 44 celdas. Revisar que el folio no tape la tabla. Markdown no requiere un folio dibujado: el ajuste es de presentación PDF.

## CMMI: conclusión y cambio propuesto

El error no es tener una evaluación de madurez Nivel 3: es mezclar el método SCAMPI A con la versión 2.0 declarada y repetirlo en la renovación y en la bibliografía.

La [nota oficial del CMMI Institute de marzo de 2020](https://cmmiinstitute.com/getattachment/5999c594-a532-4cd7-acea-799666e9ea5a/2020-03-March-Quality-Tip-March-Benchmark-CMMI-Appraisal-Activities.pdf), primera página, distingue explícitamente SCAMPI V1.3b A de CMMI V2.0 Benchmark. La [página oficial de tipos de evaluación](https://cmmiinstitute.com/learning/appraisals/types) confirma que Benchmark produce clasificación con vigencia de tres años; Evaluation no produce clasificación, y Sustainment tiene condiciones y vigencia distintas. Por eso no corresponde cambiar el método simplemente a «Evaluation» ni conservar SCAMPI A como sinónimo indistinto.

**Propuesta compatible con el antecedente ficticio del ejercicio:** «CMMI, vista de Desarrollo, versión 2.0, Nivel de Madurez 3; evaluación Benchmark». Homologar la mención institucional de §1.3, el antecedente de §1.4, su renovación y Referencias. Mantener la distinción entre evaluación de madurez y certificación ISO. No cambiar a versión 3.0 por ser más reciente: no se ha probado que ésa fuera la versión del antecedente de 2023.

Para renovar, describir una nueva evaluación Benchmark conforme al modelo/método admisible en esa fecha, antes del vencimiento declarado, sin prometer una renovación SCAMPI A. El resultado y su vigencia deben acreditarse; no se asignan automáticamente por escribir el compromiso.

El número 58190, las fechas de noviembre de 2023/2026 y el supuesto informe siguen siendo antecedentes ficticios declarados del ejercicio: **no fueron autenticados**. Corregir el nombre del método no convierte ese informe en una publicación verificada del CMMI Institute. La referencia bibliográfica debe corresponder al antecedente efectivamente utilizado; la documentación oficial del método se cita por separado, sin presentarla como certificación de LafroX.

## Próximo paso

Aplicar las correcciones verificadas si el usuario solicita corregir: fuentes del SD1 en su checkout LaTeX, recompilación y cotejo de los PDF; espejo de los tres Markdown sólo cuando cambie su contenido. Conservar pendientes las firmas y las revisiones humanas reales. La presente instrucción fue de revisión y no se utilizó como autorización automática para editar entregables.
