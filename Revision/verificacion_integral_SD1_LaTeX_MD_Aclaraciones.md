# LafroX — Verificación integral del SD1

Revisión del 11 de octubre de 2026. Alcance: cuerpo, anexos y Formulario T-6; fuentes LaTeX, espejos Markdown y PDF actuales. Es un registro de trabajo, no un entregable ni una aprobación humana.

## Resultado

**Los tres Markdown están alineados en contenido con sus fuentes LaTeX. No corresponde afirmar cumplimiento al 100 % de las Aclaraciones: quedan cinco pendientes, incluyendo tres ajustes adicionales detectados en esta revisión.**

## Correspondencia de versiones

| Documento | Fuente → Markdown | Comprobación adicional contra PDF | Páginas PDF |
|---|---|---|---:|
| SD1 | Reconversión en memoria, sin diferencias | 120 bloques de prosa/listas coinciden tras normalización y exclusión de encabezados/pies | 21 |
| Anexos | Reconversión en memoria, sin diferencias | Seis bloques de prosa coinciden | 3 |
| T-6 | Reconversión en memoria, sin diferencias | Cinco bloques de prosa y 44 celdas: once campos por cuatro columnas | 7 |

No se pretende igualdad de maquetación entre Markdown y PDF. El espejo Markdown conserva títulos, contenido, tablas, referencias y declaraciones; la foliación y el índice con páginas se verifican en el PDF. El organigrama enlaza su activo real.

## Pendientes

1. **Citas a las Bases sin página — Aclaraciones §6.** Las citas indican artículo, sección o código, pero omiten el folio de la fuente. Ejemplos: BA Art. 34°, BTT §15.2 y RT-19.02 en el cuerpo; revisar también las citas de anexos y T-6. Debe completarse la página comprobándola en los PDF originales, no usando la página del SD1. Se localizaron los originales en la carpeta FEP; su existencia no significa que esta revisión haya asignado los folios.
2. **Foliación horizontal del T-6 — Aclaraciones §9.** En sus páginas 4–6, el folio queda girado en el margen izquierdo de la página visualizada, no en el extremo inferior derecho. Los números son consecutivos; el defecto es su posición y orientación. La tabla puede conservar las tres páginas horizontales.
3. **Nomenclatura CMMI — coherencia técnica.** §1.4 y Referencias mezclan CMMI versión 2.0 con SCAMPI A y anuncian renovación mediante SCAMPI A. Debe homologarse modelo, método y referencia según el antecedente que realmente se declare. El [CMMI Institute](https://cmmiinstitute.com/learning/appraisals/types) distingue actualmente Benchmark, Sustainment, Evaluation y Action Plan Reappraisal. Este hallazgo no autentica el número ficticio de evaluación ni autoriza inventar una acreditación.
4. **Revisión humana — Aclaraciones §7.2.** Permanecen ocho celdas pendientes en la declaración del cuerpo (seis secciones, anexos y T-6), más una en anexos y una en T-6. Son diez celdas distribuidas entre tres documentos, no diez revisiones de contenido independientes. Debe completarlas quien efectivamente revise la versión vigente. Ubicación: SD1 p. 21, anexos p. 3 y T-6 p. 7.
5. **Firmas — Aclaraciones §9.** Las tres portadas mantienen nombre y línea vacía. Falta la firma efectiva en cuerpo, anexos y formulario.

Los puntos 1–3 amplían el registro previo: no era correcto seguir declarando que sólo faltaban revisión humana y firmas.

## Comprobaciones conformes

- Títulos obligatorios del capítulo 1 conservados; secciones con introducción y desarrollo, no sólo tablas.
- Tablas del cuerpo citadas y explicadas; siete tablas en vertical y sin desbordes. La declaración IA tiene las seis columnas exigidas específicamente por §7.2, no se trata como infracción al límite orientativo de cinco columnas.
- Figura 1.1 real, numerada, citada y explicada; texto del organigrama aproximadamente de 9,47 puntos en el PDF.
- Anexos y formulario separados. No se impone a su detalle el límite orientativo de una página del cuerpo.
- T-6 conserva los once campos para los tres proyectos, encabezados repetidos y filas completas. Sus montos históricos no se presentan como precios de la oferta.
- Referencias y Declaración de uso de IA al final, en ese orden y sin numeración; navegación del índice PDF comprobada.
- Papel carta, texto seleccionable y configuración nominal de cuerpo de 11 puntos. No se confunden los puntos TeX con puntos PDF ni los superíndices con el tamaño ordinario del texto.
- Sin referencias indefinidas ni desbordamientos en los registros finales de compilación; se revisó la presentación de las 31 páginas.
- No quedan rótulos «Descripción de imagen» como sustitución de figura ni referencias visibles «Caso 02» en estos entregables.
- Dotación, relevos NOC e inventario/capacidad coinciden entre las versiones. Mesa adicional a los 124 especialistas; capacidad reservada para Puelche, no capacidad total corporativa. Contactos no se equiparan con usuarios o tickets únicos.
- Coherencia de capacidad contrastada con los pasajes relacionados de SD3, SD4 y T-15 Markdown. Por instrucción del usuario, el PDF T-15 no se modificó; no se afirma sincronización de ese PDF.

## Límites y estado de trabajo

No se autenticaron certificados, alianzas ni proyectos ante terceros. Los antecedentes ficticios aprobados del ejercicio no son mediciones o acreditaciones reales. El cotejo entre versiones no demuestra envío, aceptación ni revisión humana. La comprobación de otros subdocumentos se limita a las referencias de capacidad y dotación relacionadas; no constituye auditoría global de toda la oferta.

En esta revisión no se editaron fuentes LaTeX, entregables Markdown ni PDF, ni se realizó commit/push. Se actualizaron únicamente registros Markdown de revisión y contexto. La versión de Aclaraciones usada es la aportada en `C:/Users/alexa/Desktop/Universidad/FEP/aclaraciones-licitacion.md`.

Fuentes SD1: `C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX-sd1-latex`, rama `LafroX-Subdoc1-LateX`. Espejos: `C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/01_presentacion_empresa`, rama `rama-md`.

## Cotejo posterior con los PDF originales

La revisión solicitada de citas, folios y CMMI quedó desarrollada en [Cotejo de fuentes](cotejo_citas_Bases_folios_CMMI_SD1.md). Ya se verificaron las páginas impresas frente a los PDF escaneados. Además de completar folios, debe corregirse la atribución del 99,95 % de infraestructura (BTT, no Caso cap. 10) y separar RT-19.02 para facultades del jefe de RT-19.03 para control de cambios. Folios horizontales T-6 confirmados y causa identificada. La fuente primaria CMMI de 2020 distingue SCAMPI V1.3b A de V2.0 Benchmark. Estos ajustes aún no se aplicaron a los entregables: esta petición fue de revisión.
