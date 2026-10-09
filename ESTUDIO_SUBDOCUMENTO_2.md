# Estudio del Subdocumento 2 — Problema y necesidad

Fecha: 30 de septiembre de 2026. Revisión de contenido y consistencia; no se modificaron las fuentes de la propuesta.

Se estudiaron `contenido.tex`, `anexos.tex`, los archivos de entrada y README de la carpeta 02, y se contrastaron con el Caso 02, el T-7 administrativo, las aclaraciones y requisitos transversales relevantes. El informe previo del proyecto se usó como antecedente y sus observaciones se volvieron a comprobar en las fuentes actuales. Esta revisión no certifica la diagramación ni una nueva compilación de los PDF.

## 1. Lectura integral del problema

La tesis del documento es que Puelche pierde continuidad de información entre la toma del pedido, la recepción, la preparación, el despacho, la entrega y la cobranza. Cada área conserva parte del dato en un sistema, una planilla, un papel o la memoria de una persona. El problema combina organización, reglas de negocio, captura de datos y tecnología. Reducirlo a obsolescencia del software deja fuera causas relevantes: decisiones no escritas, ausencia de investigación de diferencias, incentivos contradictorios y dependencia de conocimiento individual.

Los tres problemas principales se relacionan así:

| Dimensión | Evidencia del caso | Necesidad que fundamenta |
|---|---|---|
| Trazabilidad e inocuidad | Nueve días para identificar clientes afectados, con resultado estimado; 41 % de recepciones del producto involucrado sin lote; temperatura sin registro continuo | Reconstruir la trayectoria del lote y demostrar las condiciones de conservación |
| Servicio y promesa comercial | OTIF 82,4 %, fill rate 91,3 %, quiebre en 7,8 % de líneas, reentregas 4,2 % | Comprometer entregas viables y conocer faltantes, atrasos y causas desde su origen |
| Control económico | Diferencias de efectivo de $4,2 millones mensuales; costo de servir desconocido; prorrateo de 2016 | Asociar hechos operacionales a cobros y costos, investigar diferencias y decidir con datos |

La fragmentación conecta las tres dimensiones. Un faltante sin causa afecta la promesa y oculta su costo; una entrega sin evidencia dificulta el reclamo y la cobranza; una recepción sin lote impide localizar mercancía y clientes en una contingencia sanitaria. La propuesta necesita conservar esa relación entre hecho, dato, responsable y decisión.

La escala condiciona el diagnóstico: 14.200 puntos de entrega, 96 camiones —42 propios y 54 de terceros—, 62 preventistas, 84 conductores y peonetas propios, aproximadamente 160 conductores externos, 120 preparadores y cuatro personas de TI. Los canales suman 11.600 tradicionales, 2.100 food service y 500 modernos. Dos CD y tres plataformas descritas suman cinco instalaciones; otras partes del caso indican seis. El documento reconoce adecuadamente esa discrepancia.

La operación exige trabajo en terreno, bajo lluvia y calor, con guantes en cámara a −22 °C, sin conectividad y durante turnos nocturnos. Septiembre eleva el volumen de aproximadamente 1.400 a 2.600 entregas diarias. Eso representa un aumento aproximado de 85,7 %, calculado como (2.600 / 1.400 − 1) × 100, y fundamenta analizar picos y ventanas horarias además de promedios.

## 2. Correspondencia con las exigencias del T-7

Las aclaraciones, capítulo 2, y el T-7 exigen comprender y dimensionar el problema, identificar interesados, declarar supuestos y fundamentar información en APA 7. También indican expresamente no mezclar problema y solución.

| Exigencia | Resultado de la revisión |
|---|---|
| Introducción y conexión con otros capítulos | Presente; remite a SD3 y anexos |
| 2.1 Resumen ejecutivo | Presente, con cifras relevantes; contiene algunos hechos que requieren corregir su formulación |
| 2.2 Contexto operacional, regulatorio y estacional | Presente; requiere precisar fuentes y alcance normativo |
| 2.3 Dimensionamiento cualitativo y cuantitativo | Presente, con tabla y seis flujos; falta un protocolo de medición uniforme |
| 2.4 Actores con influencia e interés | Presente: cinco grupos de síntesis y 19 entradas en anexos |
| 2.5 Requerimientos, supuestos, exclusiones y restricciones | Presente y separado en anexos; parte del análisis anticipa decisiones de solución |
| Información de apoyo y APA 7 | Hay citas y bibliografía; algunas referencias externas carecen de identificación comprobable suficiente |

La cobertura estructural es clara. Esto no basta para dar por cerrada la calidad del diagnóstico: la precisión de categorías, denominadores, relaciones causales y respaldo bibliográfico todavía importa.

## 3. Elementos que conviene conservar

1. El 41 % sin lote conserva su población correcta: el producto involucrado en el retiro. SP-03 reconoce que la magnitud general se desconoce.
2. La estimación de 59 reentregas diarias muestra el cálculo 1.400 × 0,042 = 58,8 y declara SP-01. Su validez depende de confirmar el denominador y la equivalencia entre entrega y reentrega.
3. El documento distingue eventos de $31 y $21 millones de un flujo mensual de $4,2 millones. Evita sumarlos como una pérdida anual comprobada.
4. El enigma del cross-docking conserva la brecha de 16 horas como diferencia entre reducción prometida y observada. SP-02 propone medir antes de atribuirla a una actividad.
5. Distingue OTIF de pedido perfecto: la documentación perdida puede afectar el segundo aunque la entrega haya sido completa y puntual.
6. Registra las 16 decisiones abiertas del caso, tres supuestos propios, nueve exclusiones, 12 restricciones y ocho sistemas o registros legados.
7. Preserva condiciones decisivas: ERP contable y tributario, efectivo del canal tradicional, privacidad laboral, continuidad sin enlace y ventanas de intervención.
8. Las familias F-01 a F-14 se identifican como síntesis y no como sustituto del catálogo atómico RF/RNF del SD3 y T-12.

## 4. Hallazgos prioritarios

### 4.1 Identificación de clientes y ejecución del retiro

En `contenido.tex:83`, la tabla denomina el indicador «Demora en retiro de mercado» y compara nueve días con menos de dos horas. El capítulo 18 del caso exige obtener la lista de clientes afectados por lote, con evidencia, en menos de dos horas. El capítulo 7.3 identifica los nueve días con esa búsqueda.

La comparación debe mantener la misma actividad: tiempo para identificar clientes afectados. Localizar destinos, comunicar, bloquear existencias, recuperar físicamente producto y cerrar un retiro son hitos distintos. El resumen también dice que el retiro demoró nueve días; conviene precisar qué demoró exactamente.

### 4.2 Diferencias de efectivo y pérdida demostrada

El resumen y la tabla emplean «fuga de recursos». El caso 4.7 dice que las diferencias no se han investigado: pueden ser errores de conteo, cobros omitidos, descuentos o pérdidas. La redacción transforma una incertidumbre en una conclusión.

La necesidad comprobada es investigar y rastrear diferencias por entrega. Deben medirse por separado diferencias sin explicar, pérdida confirmada y recuperación. Explicar una diferencia no equivale a recuperar dinero. Una proyección de $50,4 millones al año —4,2 × 12— sería una extrapolación de diferencias, nunca un ahorro demostrado.

### 4.3 Sincronización de preventa: contradicción interna

La descripción del flujo aclara que el pedido se transmite al recuperar cobertura y que el envío al final del día está por confirmar. Sin embargo, `contenido.tex:161` vuelve a afirmar que el conflicto aparece «tras la jornada comercial».

Debe conservarse la condición documentada: al recuperar cobertura. También debe distinguirse la falta de stock del bloqueo por crédito. El caso describe pedidos retenidos por crédito y pedidos perdidos o duplicados, pero no establece que todos los quiebres se produzcan porque otros clientes reservaron antes.

### 4.4 Retorno, rechazo y reentrega

La figura de reparto trata local cerrado o disconformidad como una salida única de retorno al CD y la asocia al 4,2 %. El caso 4.6 describe tres conductas ante local cerrado: volver después, dejar con un vecino o retornar. Un rechazo puede afectar solo a una línea. El caso informa devoluciones de 2,9 % del volumen, con otro denominador.

El AS-IS debe conservar intento fallido, rechazo parcial o total, retorno de mercancía y nuevo intento de entrega como eventos distintos. S-03 es una regla futura propuesta; no describe la conducta uniforme actual.

### 4.5 Hechos, hipótesis y decisiones de diseño

La promesa de 24/48 horas, la regla térmica graduada, la sustitución del WMS y el control de envases por saldo son decisiones del proponente. El caso exige resolverlas como supuestos, por lo que su registro en anexos es pertinente. En el cuerpo deben identificarse como propuestas y remitir al SD3 para su justificación.

Hay además causalidad excesiva: `contenido.tex:286` presenta la planificación manual como causa directa de la ocupación de 68 %. Puede contribuir, pero también influyen dispersión geográfica, mezcla de carga, frío, demanda y ventanas. La merma de 1,7 % tampoco demuestra por sí sola ausencia de FEFO como causa exclusiva. «Colapsa inevitablemente» ante picos es una conclusión que requiere un análisis de capacidad.

### 4.6 Soporte del WMS y vínculo con la preventa

El resumen afirma que el WMS tiene soporte discontinuado y describe preventa como módulos satélites del ERP. El caso confirma desaparición del proveedor y falta de soporte de la aplicación de preventa de 2016. Para el WMS confirma antigüedad, cobertura limitada e interfaces sin documentación, pero no explicita soporte discontinuado. Tampoco caracteriza preventa como un módulo del ERP.

Conviene eliminar esas atribuciones o declararlas como datos por confirmar. No son necesarias para fundamentar la fragmentación.

### 4.7 Resistencias y catálogo de interesados

El texto concluye que los clientes acogerán favorablemente cualquier mejora que mantenga su hábito de pago. No consta evidencia de aceptación universal. Mantener compra y efectivo atiende una restricción, pero no garantiza adopción. También falta sustento para ordenar los focos de resistencia de toda la organización a partir de la objeción sindical.

El catálogo llamado «nominal» presenta cargos y colectivos, sin los nombres de entrevistados disponibles en el caso. Sería más preciso denominarlo catálogo por rol, o incorporar nombres para las contrapartes individuales. Las 19 entradas son categorías de interesados; no son 19 personas. Las escalas de influencia e interés necesitan una breve regla de asignación.

## 5. Precisión normativa y bibliográfica

**Cadena de frío.** El RSA distingue almacenamiento en cámaras, transporte interurbano y distribución local. Los artículos 189–191 contemplan registro continuo en cámaras y condiciones diferenciadas de transporte, incluyendo tolerancias transitorias. La redacción de un único umbral universal y «registros inalterables» necesita mayor precisión. La inmutabilidad informática debe atribuirse a la exigencia contractual que corresponda. La decisión de Calidad requiere distinguir temperatura de producto, lectura del sensor y duración de la excursión. Fuente: [RSA, BCN](https://www.bcn.cl/leychile/navegar?idNorma=71271).

**Prueba de entrega y mérito ejecutivo.** F-09 habla de certificar el acuse de GDE ante el SII «con mérito ejecutivo». Debe distinguir evidencia operacional, recibo de mercancías y requisitos legales de la factura. El SII describe el recibo previsto por la Ley 19.983 y sus formatos; una fotografía o nombre del receptor de S-15 no basta por sí solo para declarar cumplido el mecanismo tributario. Fuente: [SII, acuse de recibo](https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6603.htm).

**Jornada.** El artículo 25 bis se refiere a choferes de carga terrestre interurbana; no debe extenderse automáticamente a peonetas y reparto urbano. La DT también identifica cambios desde abril de 2028, relevantes para un proyecto de varios años. Debe caracterizarse cada perfil y ruta antes de asignarle un régimen. Las 14 horas de autonomía tecnológica no determinan una jornada laboral permitida. Fuente: [Dirección del Trabajo](https://dt.gob.cl/portal/1628/w3-article-60075.html).

**Protección de datos.** La fecha del 1 de diciembre de 2026 está respaldada por el registro oficial consultado. La atribución bibliográfica al Ministerio del Interior es incorrecta: el registro identifica al Ministerio Secretaría General de la Presidencia. Fuente: [Ley 21.719, BCN](https://www.bcn.cl/leychile/Navegar?idNorma=1209272&idParte=10527471&idVersion=2026-12-01).

**GS1.** Conviene distinguir GTIN, GLN y SSCC de GS1-128: los primeros son identificadores y el último es una simbología. La unidad logística se identifica mediante SSCC. El anexo S-02 ya hace esa distinción mejor que el cuerpo. Fuentes: [identificadores GS1](https://www.gs1.org/gs1-application-identifiers) y [SSCC](https://www.gs1.org/standards/id-keys/sscc).

Las referencias «GS1 Chile (2020), versión 20.0» y «Manual de Procedimientos y Requisitos DTE, SII (2024)» necesitan documento exacto y enlace verificable. La revisión no comprobó la existencia de esas publicaciones con esos títulos. Es preferible citar fuentes oficiales efectivamente consultadas. Para cada afirmación legal deben agregarse artículos o disposiciones específicos, sin atribuir a la ley umbrales fijados por el caso.

## 6. Cobertura y coherencia de los anexos

Los anexos están bien separados, pero requieren estas comprobaciones:

- F-02 exige captura en cada instalación antes del «ingreso físico». Debe distinguir descarga, inspección, recepción administrativa, cuarentena y disponibilidad del stock. Tampoco todos los productos requieren el mismo lote o formato.
- F-12 describe autoatención como canal de consulta. El caso exige también pedido en autoservicio; el resumen de la familia debe conservar esa función.
- Las 14 familias no muestran explícitamente reposición/pronóstico, devoluciones y envases como familias propias. Eso no prueba ausencia en el catálogo de SD3, pero amerita indicar dónde se agrupan y su correspondencia RF/RNF.
- S-07 valida la metodología de costo de servir antes del mes 13, aunque reconoce que determina datos capturados desde Etapa 1. Las variables y reglas mínimas deben acordarse antes de implementar su captura; el cálculo analítico puede completarse después.
- S-06 permite replantear la conciliación si el cliente elimina efectivo. La hipótesis debe aclarar que no habilita incumplir R-05 ni exigir pago electrónico al canal tradicional.
- La separación entre disponibilidad de componentes de 99,95 % y transacción crítica de 99,9 % concuerda con las BTT. Estas métricas no reemplazan la continuidad exigida para la ventana de despacho.
- RT-03.12 sustenta reconciliación automática y determinista; los tiempos de 10 minutos móvil y dos horas CD se fundamentan en el capítulo 15 del caso. Conviene conservar ambas fuentes y sus alcances.
- El cuerpo distingue congelamiento del 1 al 25 de septiembre y prohibición de paso a producción durante todo septiembre. Mantener esa diferencia en cualquier resumen de calendario.

## 7. Línea base necesaria para defender el diagnóstico

Cada indicador necesita una ficha con fórmula, unidad, numerador, denominador, período, fuente, responsable, casos excluidos y tratamiento de datos faltantes. Para OTIF deben fijarse pedido versus entrega, parciales, cancelaciones, fecha y ventana pactadas. S-01 adopta una definición futura estricta, pero el caso reconoce que las áreas hoy miden distinto: no se puede asumir que el 82,4 % histórico ya use esa definición.

Las referencias «sobre 95 %», «sobre 97 %», «bajo 2 %» y «bajo 1 %» deben diferenciarse de metas contractuales asumidas. Tampoco se puede calcular un retorno económico confiable sin valor de inventario, costo de cada reentrega, márgenes, valor de envases y causas confirmadas de diferencias.

Como registro de evidencia, resulta útil separar: hecho documentado; cálculo derivado; hipótesis por medir; decisión propuesta; vacío por consultar. SP-02 y SP-03 ya ofrecen una base para aplicar esa disciplina al resto del capítulo.

## 8. Orden de revisión propuesto

1. Corregir identificación de clientes frente a retiro, diferencias frente a pérdidas y categorías de reparto.
2. Resolver la contradicción de sincronización y las atribuciones sin respaldo sobre WMS y preventa.
3. Precisar normativa térmica, laboral, tributaria, GS1 y referencias externas.
4. Identificar decisiones propuestas y moderar causalidad y afirmaciones de aceptación.
5. Completar las fichas de línea base y revisar cobertura de las familias frente al catálogo detallado.
6. Adelantar las definiciones de captura que habilitan costo de servir y validar trazabilidad hacia SD3.
7. Actualizar README: describe carpetas `entrega_1`, `entrega_2` y una carpeta de trazabilidad que no aparecen en el inventario actual de archivos.

La estructura y el entendimiento general del negocio pueden conservarse. El trabajo pendiente se concentra en hacer cada afirmación defendible: qué consta, qué se infiere, qué se propone y qué falta medir.
