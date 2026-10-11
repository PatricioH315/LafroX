# LafroX — Trazabilidad de observaciones del Informe 1: Subdocumento 2

## Alcance y criterio de lectura

Tabla de observación–respuesta–sección modificada exigida por las Bases Administrativas, artículo 46° y Formulario T-22, apartado «Informe y presentación 2». Se contrastan las observaciones de `Revision_informe.md`, apartado «SUBDOCUMENTO 2», y las observaciones generales que alcanzan al SD2, con:

- el Markdown actual de `rama-md`: `02_problema_necesidad/LAFROX-Subdocumento2.md` y `LAFROX-Subdocumento2-Anexos.md`;
- el checkout LaTeX del SD2 (`../LafroX-sd2-latex`, rama `LafroX-Subdoc2-LateX`), ajustado el 11-10-2026 a las Aclaraciones y recompilado sin errores, cajas desbordadas ni avisos: cuerpo de 25 páginas y anexos de 20, ambos en tamaño carta. Cambios publicados en el commit 0a6f788 de esa rama.

Las páginas de la tercera columna son las de esos PDF («p.» = cuerpo; «Anexos p.» = PDF de anexos) y coinciden con sus índices impresos. Si se recompilan, hay que cotejarlas de nuevo.

**Borrador de trabajo:** las observaciones se sintetizan fielmente; no son citas literales. «Documentado» significa que la respuesta está en el MD y en el PDF actuales, no que la Comisión la haya aceptado. «Parcial» y «Pendiente» identifican lo que no corresponde declarar resuelto.

## Observaciones específicas del Subdocumento 2

| Observación del Informe 1 | Respuesta / corrección comprobable en el informe actual | Sección modificada / ubicación actual |
|---|---|---|
| S2-01. Crítico: no existe resumen ejecutivo; el documento parte en «2.1 Contextualización del Entorno», sin síntesis, propuesta de valor ni enfoque ingenieril. | **Documentado según las Aclaraciones.** Se creó §2.1 con el título obligatorio «Resumen Ejecutivo del problema»: sintetiza la operación, la brecha de OTIF de 82,4 % frente a 95 %, la raíz del problema y tres impactos cuantificados. Las Aclaraciones posteriores limitan el 2.1 a «síntesis del problema, su magnitud y los actores afectados» y exigen no mezclar el problema con la solución. Por eso, la propuesta de valor y el enfoque se trasladaron al SD3, §3.1. | SD2, §2.1, p. 5; SD3, §3.1. |
| S2-02. OK: buen AS-IS de las siete fases y de los dos puntos donde se pierde la trazabilidad. | **Se mantiene y se amplía.** Son seis procesos, cada uno con su lista de pasos, su diagrama y un párrafo de análisis. | SD2, §2.3.2.1–2.3.2.6, p. 11–20; Figuras 2.1–2.6. |
| S2-03. Las secciones 2.3 (AS-IS) y 2.4 (Diagnóstico) repiten el mismo contenido y parafrasean el Capítulo 4 del caso. | **Documentado.** Se eliminó la sección duplicada y la estructura sigue los títulos de las Aclaraciones. El párrafo bajo cada figura ya no repite los pasos: indica dónde se pierde el dato, qué efecto tiene después y qué falta medir. Un párrafo final conecta los seis procesos con los tres problemas de §2.2.1. Las listas de pasos siguen el orden del caso porque describen el AS-IS. | SD2, §2.3.1, p. 10; §2.3.2, p. 11–20, párrafo final en p. 20; Anexos, Tabla 2.A.4, p. 11–12. |
| S2-04. Errores de lectura: el 7,8 % de quiebre se detecta en la preventa, no en la entrega, y «4,2 % de reentregas ≈ 588/mes» está mal calculado (≈ 59 al día). | **Documentado.** El 7,8 % se refiere a líneas de pedido de la preventa, como en el caso. Las reentregas se muestran con el cálculo 1.400 × 0,042 = 58,8 ≈ 59 al día, condicionadas al supuesto SP-01. | SD2, §2.1, p. 5; §2.2.1, p. 6; Tabla 2.1, p. 10; §2.3.2.5, p. 19; Anexos, SP-01, p. 11. |
| S2-05. No distingue los tres problemas del Cap. 19 del caso y los presenta sin jerarquía ni relación causal. | **Parcial.** §2.2.1 separa los tres problemas y cita el capítulo 19 del caso. §2.1 declara la causa común, y el párrafo final de §2.3.2 muestra cómo la pérdida del dato en cada proceso los encadena. No hay un análisis causal dedicado entre los tres problemas. | SD2, §2.1, p. 5; §2.2.1, p. 6; §2.3.2, p. 20. |
| S2-06. No hay datos investigados fuera del caso ni se detecta el vacío del cross-docking. | **Parcial.** El vacío de 16 h está documentado y se trata como hipótesis SP-02, que se valida midiendo cada tramo. Las fuentes externas son normativas (Ley 21.719, art. 25 bis del Código del Trabajo, SII y GS1); no hay datos cuantitativos de la industria. | SD2, §2.3.2, p. 11; Figura 2.3, p. 15; §2.2.2, p. 7; Anexos, SP-02, p. 11–12. |
| S2-07. OK: marco normativo pertinente y vinculado al caso. | **Se mantiene.** Se agregó la normativa laboral del transporte. | SD2, §2.2.2, p. 7. |
| S2-08. El marco legal ocupa cinco páginas y está escrito como solución. | **Documentado.** El marco legal se redujo a cinco viñetas que describen obligaciones del CLIENTE. Las tensiones de §2.2.3 terminan en «Decisión que requiere la necesidad» y remiten el mecanismo al SD3 o al SD4. Se quitó de la Tabla 2.2 la columna de estrategia, que adelantaba la gestión del cambio. | SD2, §2.2.2, p. 7; §2.2.3, p. 8–9; Tabla 2.2, p. 21. |
| S2-09. Cierra con una frase de evaluador («… no será competitiva»). | **Documentado.** La frase no aparece en el MD ni en el PDF. | SD2, §2.2.2, p. 7–8. |
| S2-10. La estacionalidad solo aparece como prohibición de intervenir sistemas. | **Documentado.** Se analiza el efecto del peak de septiembre (de ≈ 1.400 a ≈ 2.600 entregas diarias), de diciembre, de los cierres de mes y del invierno rural, con la cita a la sección B.2 del caso, pp. 38–39. La prohibición queda separada como restricción R-08. | SD2, §2.2.2, p. 8; Tabla 2.3, p. 23. |
| S2-11. No se desarrolla ninguna de las doce materias del numeral 16.2. | **Parcial.** Desarrolladas: GS1, mensajes EDI, GDE y acuse de recibo, RSA, jornada del transporte, OTIF (S-01), *fill rate* y pedido perfecto, y costo de servir (S-07). No desarrolladas: intermediarios del EDI, frío por producto y tecnologías de registro, costo por entrega, ruteo VRPTW, estrategias de picking, pronóstico de demanda, logística inversa (solo S-10 y S-12) y modelos de atención al canal tradicional. | SD2, §2.2.2, p. 7; §2.3.1, p. 10; Anexos, Tabla 2.A.3, p. 7–11. |
| S2-12. Declara que el 99,95 % «se alinea con Tier III», mientras el SD4.2 diseña Tier II. | **Documentado.** El SD2 no menciona ningún Tier. El 99,95 % y el 99,9 % se citan desde las BTT, cap. 7, pp. 17–18, igual que en el SD4. | SD2, §2.5.1, p. 22; Anexos, Tabla 2.A.2, p. 6–7. |
| S2-13. OK: mapa de once actores. | **Se mantiene y se amplía** a 19 actores. | SD2, §2.4, p. 20–21; Anexos, Tabla 2.A.7, p. 15–18. |
| S2-14. Faltan la gerenta general, el gerente de operaciones, la jefa de bodega, el sindicato, las transportistas, los proveedores, la autoridad sanitaria y food service. | **Documentado.** Los ocho figuran en la Tabla 2.A.7 y agrupados en la Tabla 2.2. | SD2, Tabla 2.2, p. 21; Anexos, Tabla 2.A.7, p. 15–18. |
| S2-15. «Conductor repartidor propio (42 personas)»: 42 son los camiones; son 84 conductores y peonetas. | **Documentado.** | SD2, §2.1, p. 5; Tabla 2.2, p. 21; Anexos, Tabla 2.A.7. |
| S2-16. Es una tabla, no una matriz influencia–interés, y no deriva en estrategia. | **Parcial.** La Tabla 2.2 agrupa a los actores por influencia e interés. El análisis concluye que el interés no discrimina (todos alto o muy alto), que la diferencia está en la influencia, y qué tipo de gestión requiere cada grupo. La estrategia por actor está en el Anexo 2.3 y en el SD3. No hay una figura de matriz con cuadrantes. | SD2, §2.4, Tabla 2.2 y análisis, p. 20–21; Anexos, Tabla 2.A.7. |
| S2-17. No se analizan las contradicciones entre los entrevistados. | **Documentado.** Se analizan las cinco tensiones, cada una con la decisión que requiere. | SD2, §2.2.3, p. 8–9. |
| S2-18. La promesa de 24 h se adopta como meta sin arbitrar la tensión. | **Documentado.** La promesa queda segmentada en 24/48 h, igual que en el SD3 (RNG-15). El SD2 no muestra el cálculo de capacidad que justifica el corte de las 14:00. | SD2, §2.2.3, tensión 1, p. 8; SD3, §3.2.2 y §3.2.4. |
| S2-19. Los supuestos son las restricciones del Cap. 10 copiadas. | **Documentado.** Las restricciones tienen su propia tabla («No son supuestos ni exclusiones») y se citan con la página del caso. | Anexos, Tabla 2.A.6, p. 13–14; Tabla 2.A.3, p. 7–11; SD2, Tabla 2.3, p. 23. |
| S2-20. No hay supuestos propios ni impacto si resultan falsos. | **Parcial.** Cada supuesto tiene «Si resulta falso» y validación, y hay tres supuestos propios (SP-01 a SP-03). Faltan supuestos sobre volumetría de sistema, interfaces del ERP y contrato de telemetría, y §2.5.2 sigue siendo un solo párrafo. | SD2, §2.5.2, p. 22; Anexos, Tablas 2.A.3 y 2.A.4, p. 7–12. |
| S2-21. Cita en APA, pero no hay lista de referencias. | **Documentado.** El cuerpo y los anexos tienen listas APA 7.ª coherentes con las citas: cada fuente de la lista se cita en el texto y cada cita está en la lista. Las citas a las Bases indican capítulo o artículo y página, según la sección 6 de las Aclaraciones. La referencia del caso usa su título real, sin «Caso 02». | SD2, Referencias, p. 23–24; Anexos, Referencias, p. 19. |
| S2-22. Seis marcadores «[INSERTAR DIAGRAMA DE FLUJO n…]»: los diagramas nunca se hicieron. | **Documentado.** No quedan marcadores. Las seis figuras son propias, numeradas, citadas antes de aparecer y explicadas después. Se verificó en el PDF que el orden cita → figura → análisis se cumple en las seis. | SD2, Figuras 2.1–2.6, p. 12–19. |
| S2-23. Cero figuras en 23 páginas. | **Documentado, con dos defectos menores.** Seis figuras, con todo su texto en 9 pt o más (medido en el PDF: entre 9,1 y 9,2 pt). Cada una queda fija donde se cita (no flota a otra página). Las Figuras 2.1 y 2.5 van en página horizontal. Los recortes solo quitan margen en blanco. La Figura 2.5 se arma con las dos páginas de su exportación y ya no corta la última caja. Pendiente: erratas dentro de las imágenes («enERP», «41% sin lote Riesgo», «enpapel», «No Diferencias no conciliadas»), texto que toca el borde en dos cajas de la Figura 2.4, y cajas numeradas distinto que los pasos del texto. | SD2, Figuras 2.1–2.6, p. 12 (2.1), 14, 15, 16, 18 (2.5) y 19. |

## Observaciones generales aplicables al Subdocumento 2

| Observación del Informe 1 | Respuesta / corrección comprobable en el informe actual | Sección modificada / ubicación actual |
|---|---|---|
| G2-01. Sin identidad de empresa. | **Documentado.** Se usa la plantilla `lafrox.cls`, con logotipo, encabezado y pie con folio. | Cuerpo y anexos, todas las páginas. |
| G2-02. Las portadas rompen la ficción y se rotulan «Formulario T-22». | **Documentado.** Las portadas no tienen datos del curso y se rotulan «Formulario T-7». La fecha de emisión es el 12 de octubre de 2026. Pendiente: la plantilla común imprime «Caso 02 — Logística» en todas las portadas. | Cuerpo y anexos, p. 1. |
| G2-03. A4 y cuerpo menor a 11 pt. | **Documentado.** Tamaño carta y cuerpo de 11 pt. | `lafrox.cls`. |
| G2-04. Sin índice, folio ni firma. | **Parcial.** Hay índice enlazable, listas y folio; los anexos ya no traen una lista de figuras vacía. La firma efectiva no se puede comprobar en el archivo. | Cuerpo, p. 1–4; anexos, p. 1–3. |
| G2-05. El documento resume y el anexo lista. | **Documentado.** | SD2, §2.5, p. 22–23; Anexos, p. 4–19. |
| G2-06. Palabras partidas en columnas angostas y filas cortadas sin encabezado. | **Documentado.** En el cuerpo no hay palabras cortadas en las tablas ni en los títulos ni en las referencias «Figura/Tabla/Anexo». Las tablas tienen 5 columnas o menos, salvo la 2.4, cuyo formato fija la sección 7.2. Las celdas tienen una sola frase y las cifras van a la derecha. Las Tablas 2.1, 2.2 y 2.3 caben cada una en una página y todas las tablas tienen análisis después. En los anexos se ensancharon las columnas de identificadores, que cortaban «S-/01» y «R-/01». | SD2, Tablas 2.1–2.4, p. 10–25; Anexos, Tablas 2.A.1–2.A.8. |
| G2-07. Indicios de IA: desde el Informe 2, cualquiera deja el subdocumento con puntaje 0. | **Pendiente bloqueante.** El PDF de anexos muestra el marcador «[[REVISIÓN HUMANA]]» en la Tabla 2.A.9. Además, en la Tabla 2.4, la fila 2.3 («Bajo», revisión de Tomás Pérez) es anterior a la redacción asistida de los párrafos de §2.3.2 y debe actualizarla el equipo. | Anexos, Tabla 2.A.9, p. 20; SD2, Tabla 2.4, p. 24–25. |
| G2-08. Un integrante lee y firma cada PDF. | **Pendiente de acreditar.** | SD2, Tabla 2.4; Anexos, Tabla 2.A.9. |
| G2-09. Ningún precio en la Oferta Técnica. | **Documentado.** El único monto, «$ 4,2 millones», son las diferencias de rendición que informa el caso. | SD2, Tabla 2.1, p. 10. |

## Pendientes antes de usar la tabla como registro de cierre

1. **Bloqueante:** completar la revisión humana de la Tabla 2.A.9 y actualizar la fila 2.3 de la Tabla 2.4 (G2-07).
2. Corregir en draw.io las erratas de las Figuras 2.1, 2.2, 2.5 y 2.6, el texto pegado al borde en la 2.4 y la numeración de las cajas; las imágenes no se editaron (S2-23).
3. Decidir si se agrega una figura de matriz influencia–interés (S2-16), supuestos propios sobre volumetría, ERP y telemetría (S2-20) y las materias pendientes del 16.2 (S2-11).
4. Decidir si la plantilla común deja de mostrar «Caso 02» en las portadas de todos los subdocumentos.

## Fuentes de cotejo

- [Revisión del Informe 1](../Revision_informe.md): «GENERAL», «SUBDOCUMENTO 2» y «CONSIDERACIONES TRANSVERSALES».
- [Subdocumento 2](../02_problema_necesidad/LAFROX-Subdocumento2.md) y [Anexos](../02_problema_necesidad/LAFROX-Subdocumento2-Anexos.md).
- Checkout LaTeX `../LafroX-sd2-latex`: `LAFROX-Subdocumento2.pdf` y `LAFROX-Subdocumento2-Anexos.pdf`.
- [Aclaraciones](../Bases/aclaraciones-licitacion.md): secciones 2 a 7 y estructura del Capítulo 2.
- Páginas de las Bases cotejadas en los PDF originales: Bases Administrativas, Bases Técnicas Transversales y caso.
