# LafroX — Resumen de los anexos del Subdocumento 4

[Índice de resúmenes](README.md) · [Documento original](../04_arquitectura/LAFROX-Subdocumento4-Anexos.md)

## Para qué sirve

La síntesis y 4-W.7 incluyen desde el mes 25 mesa de 9 personas (11 en peak) más NOC/SOC de 10: totales 19/21. El índice usa las anclas explícitas A–W. ADR-10 exige excluir al escritor anterior antes de promover y no autoriza promoción por pérdida de ambas redes.

Esta guía explica los 23 anexos del capítulo 4 por separado. Permite elegir el listado, protocolo o cálculo que se necesita sin recorrer todas sus tablas. Los identificadores conservan la nomenclatura del original.

## Anexo 4-A — Catálogo de eventos canónicos

Define los hechos de negocio que se intercambian como eventos: productor, consumidores y partición. El evento describe algo sucedido; permite seguir recepción, pedido, inventario, entrega y custodia entre módulos sin otorgar a un consumidor autoridad sobre los datos del productor.

**Cuándo consultarlo:** para diseñar o revisar un intercambio de eventos y su vínculo con requisitos.

[Ver este anexo en el original](../04_arquitectura/LAFROX-Subdocumento4-Anexos.md#anexo-4-a--cat%C3%A1logo-de-eventos-can%C3%B3nicos)

## Anexo 4-B — Gobierno de la integración

Asigna gobierno a contratos, versiones, cambios, seguridad y evidencia de integración. Cada mecanismo tiene responsable y artefacto verificable. El objetivo es que cambios en ERP, módulos o terceros no se incorporen sin coordinación ni registro.

**Cuándo consultarlo:** antes de cambiar una interfaz, su versión o el procedimiento de publicación.

[Ver este anexo en el original](../04_arquitectura/LAFROX-Subdocumento4-Anexos.md#anexo-4-b--gobierno-de-la-integraci%C3%B3n)

## Anexo 4-C — Escenarios de carga masiva

Describe cargas y descargas masivas y los controles que identifican cada lote procesado. Permite distinguir aceptación, rechazo y reproceso, manteniendo auditoría e integridad. Un proceso masivo debe poder explicar qué registros incorporó y cuáles aisló.

**Cuándo consultarlo:** para importación, exportación, migración o tratamiento de datos por lotes.

[Ver este anexo en el original](../04_arquitectura/LAFROX-Subdocumento4-Anexos.md#anexo-4-c--escenarios-de-carga-masiva)

## Anexo 4-D — Matriz de los doce módulos

Relaciona doce módulos con función, responsabilidad, interfaz, actor y etapa. Recepción, Inventario, Preventa, Rutas, Preparación, Reparto, Cobranza y rendición, Devoluciones y envases, Calidad y trazabilidad, Analítica, Canal moderno y Telemetría son los nombres de M1–M12. M9 trata lote, frío y bloqueo; M12 aporta ruta real y desviaciones. M10 tiene indicadores de E1 y costo de servir de E2.

**Cuándo consultarlo:** para ubicar al responsable de una capacidad y no confundir acceso con propiedad de datos.

[Ver este anexo en el original](../04_arquitectura/LAFROX-Subdocumento4-Anexos.md#anexo-4-d--matriz-de-los-doce-m%C3%B3dulos)

## Anexo 4-E — Trazabilidad funcional

Sigue grupos de requerimientos hasta módulo, capas y evidencia. Es la comprobación de que la arquitectura responde al alcance, y no solo un inventario de herramientas. La evidencia indicada sigue siendo la que debe verificarse durante el proyecto.

**Cuándo consultarlo:** al contrastar un requisito del T-12 con su realización técnica.

[Ver este anexo en el original](../04_arquitectura/LAFROX-Subdocumento4-Anexos.md#anexo-4-e--trazabilidad-funcional)

## Anexo 4-F — Mapa de límites de contexto

Explica las fronteras entre módulos, su colaboración y los contratos compartidos. La capa anticorrupción traduce modelos ajenos, especialmente ERP y cadenas, para que sus cambios no reescriban las reglas internas de la solución.

**Cuándo consultarlo:** cuando un cambio de un módulo o tercero pueda afectar decisiones de otro.

[Ver este anexo en el original](../04_arquitectura/LAFROX-Subdocumento4-Anexos.md#anexo-4-f--mapa-de-l%C3%ADmites-de-contexto)

## Anexo 4-G — Catálogo de interfaces internas

Detalla ocho interfaces internas con identificación estable, modo, volumen, ventana y conducta ante error. Incluye recorridos entre dispositivos, sedes y nube y la coordinación de reserva y retención de INT-03/04. Los volúmenes son escenarios de diseño; el mismo hecho puede atravesar varios contratos.

**Cuándo consultarlo:** para sincronización, reintentos, permisos técnicos o autonomía de los intercambios internos.

[Ver este anexo en el original](../04_arquitectura/LAFROX-Subdocumento4-Anexos.md#anexo-4-g--cat%C3%A1logo-de-interfaces-internas)

## Anexo 4-H — Catálogo de interfaces externas

Detalla siete interfaces externas, dueño interno, contrato y respuesta ante falla. ERP, tributación y servicios de terceros se encapsulan; un timeout no equivale a confirmación o pago aprobado. La ventana requerida por el diseño no es automáticamente un nivel de servicio aceptado por el tercero.

**Cuándo consultarlo:** al preparar acuerdos con proveedores o ensayar indisponibilidad de un tercero.

[Ver este anexo en el original](../04_arquitectura/LAFROX-Subdocumento4-Anexos.md#anexo-4-h--cat%C3%A1logo-de-interfaces-externas)

## Anexo 4-I — Volumen de mensajes

Reúne órdenes de magnitud de mensajes por interfaz, con sus unidades y supuestos. Permite comparar demanda, sin sumar todos los recorridos como operaciones únicas. La coordinación de reserva y retención suma 46.968 mensajes diarios (87.228 en peak), con un máximo de cuatro por línea, y no se suma al drenaje tras un corte.

**Cuándo consultarlo:** para comprobar si un cálculo usa mensajes, transacciones, lecturas o tráfico encadenado.

[Ver este anexo en el original](../04_arquitectura/LAFROX-Subdocumento4-Anexos.md#anexo-4-i--volumen-de-mensajes)

## Anexo 4-J — Funciones sin conexión

Declara funciones disponibles sin enlace, persistencia local, límites y procedimiento al reconectar. Capturar hechos en terreno no confirma stock central, crédito actualizado o autorización de terceros. La autonomía debe preservar también las funciones que dejan de estar disponibles.

**Cuándo consultarlo:** para diseñar experiencia sin señal y procedimientos de continuidad realistas.

[Ver este anexo en el original](../04_arquitectura/LAFROX-Subdocumento4-Anexos.md#anexo-4-j--funciones-sin-conexi%C3%B3n)

## Anexo 4-K — Reglas de reconciliación

Establece reconciliación por regla de negocio, lugar de ejecución y bitácora. Identificadores, versiones, actor y regla aplicada permiten explicar duplicados y conflictos. No decide únicamente por «última hora recibida», lo que podría sobrescribir hechos sanitarios o financieros.

**Cuándo consultarlo:** ante reintentos, mensajes fuera de orden o discrepancias entre sitio y nube.

[Ver este anexo en el original](../04_arquitectura/LAFROX-Subdocumento4-Anexos.md#anexo-4-k--reglas-de-reconciliaci%C3%B3n)

## Anexo 4-L — Decisiones del numeral 16.1

Conserva las dieciséis decisiones abiertas del numeral 16.1 del caso, su respuesta de oferta y quién debe validarla. Relaciona stock, crédito, frío, envases, entrega y demás decisiones operativas con el diseño. Una propuesta escrita no acredita validación del CLIENTE.

**Cuándo consultarlo:** para preparar las decisiones del levantamiento y contrastarlas con SD2/SD3.

[Ver este anexo en el original](../04_arquitectura/LAFROX-Subdocumento4-Anexos.md#anexo-4-l--decisiones-del-numeral-161)

## Anexo 4-M — Verificación de continuidad lógica

Fija ensayos de continuidad lógica: AL-DTE-01 prueba documentos para 96 salidas; AL-DR-01 recuperación; AL-OFF-01 operación desconectada y AL-CLI-01 comportamiento de autoatención. Cada ejecución debe conservar configuración, carga, fallas inyectadas, trazas y acta. El protocolo no es un resultado de prueba.

**Cuándo consultarlo:** antes de aceptar continuidad o afirmar que una contingencia sostiene el despacho.

[Ver este anexo en el original](../04_arquitectura/LAFROX-Subdocumento4-Anexos.md#anexo-4-m--verificaci%C3%B3n-de-continuidad-l%C3%B3gica)

## Anexo 4-N — Correspondencia de componentes lógicos

Relaciona componentes, módulos y servicios transversales con alcance y realización física. Desarrolla la autorización por actor, acción y ámbito de datos: conductor, representante externo, cliente y operador no comparten permisos por aparecer en un mismo flujo. Mantiene la correspondencia con los quince actores del SD3.

**Cuándo consultarlo:** para validar permisos o seguir una función desde usuario hasta componente.

[Ver este anexo en el original](../04_arquitectura/LAFROX-Subdocumento4-Anexos.md#anexo-4-n--correspondencia-de-componentes-l%C3%B3gicos)

## Anexo 4-O — Registro de decisiones de arquitectura

Reúne 22 decisiones ADR, con alternativas descartadas, criterio, consecuencias y evidencia. Explica elecciones de backend, datos, caché, recuperación y continuidad. Su valor es conservar el motivo de la decisión y permitir revisarla mediante gobierno formal.

**Cuándo consultarlo:** cuando se pregunte por qué se eligió una tecnología o un modo de recuperación.

[Ver este anexo en el original](../04_arquitectura/LAFROX-Subdocumento4-Anexos.md#anexo-4-o--registro-de-decisiones-de-arquitectura)

## Anexo 4-P — Tecnologías, soporte y actualización

Distingue versiones de referencia de imágenes exactas de producción y describe soporte/actualización durante 56 meses. Las liberaciones fijan parches, huellas y componentes; versiones posteriores requieren compatibilidad y pruebas. Identifica los perfiles y servicios del monolito Laravel/PHP y sus controles de compatibilidad, sin plantear una migración desde otro backend.

**Cuándo consultarlo:** para mantenimiento, fin de soporte, actualización o revisión de compatibilidad.

[Ver este anexo en el original](../04_arquitectura/LAFROX-Subdocumento4-Anexos.md#anexo-4-p--tecnolog%C3%ADas-soporte-y-actualizaci%C3%B3n)

## Anexo 4-Q — Modelado de amenazas lógicas

Aplica STRIDE: suplantación, alteración, repudio, divulgación, denegación y elevación de privilegios. Cada amenaza de módulo, servicio o integración tiene dueño y prueba negativa. El análisis se revisa al cambiar contratos o superficies expuestas.

**Cuándo consultarlo:** para identificar cómo podría abusarse de un flujo y qué ensayo debe impedirlo.

[Ver este anexo en el original](../04_arquitectura/LAFROX-Subdocumento4-Anexos.md#anexo-4-q--modelado-de-amenazas-l%C3%B3gicas)

## Anexo 4-R — Controles de seguridad y evidencia

Vincula controles de seguridad con su implementación y evidencia prevista. Los identificadores de ISO/IEC 27001/27002 permiten seguir qué control atiende cada mecanismo. La matriz es una propuesta de controles; no constituye certificación por sí misma.

**Cuándo consultarlo:** para auditar protección de datos, acceso y trazabilidad de seguridad.

[Ver este anexo en el original](../04_arquitectura/LAFROX-Subdocumento4-Anexos.md#anexo-4-r--controles-de-seguridad-y-evidencia)

## Anexo 4-S — Puntos de vista y correspondencias

Define interesados, preocupaciones y correspondencias de cinco vistas: lógica, procesos, despliegue, datos y seguridad. La integración las atraviesa y no se presenta como una sexta vista obligatoria. Una decisión debe poder seguirse entre sus representaciones.

**Cuándo consultarlo:** para comprobar que distintos diagramas describen la misma solución.

[Ver este anexo en el original](../04_arquitectura/LAFROX-Subdocumento4-Anexos.md#anexo-4-s--puntos-de-vista-y-correspondencias)

## Anexo 4-T — Desempeño y aceptación lógica

Fija desempeño sobre la operación percibida y confirmada. Una consulta inmediata de datos fechados no equivale a stock confirmado; el timeout del adaptador es distinto del tiempo de experiencia de usuario. Los ensayos deben declarar escenario, carga y criterio de aceptación.

**Cuándo consultarlo:** para establecer pruebas de latencia y evitar medir solo una llamada aislada.

[Ver este anexo en el original](../04_arquitectura/LAFROX-Subdocumento4-Anexos.md#anexo-4-t--desempe%C3%B1o-y-aceptaci%C3%B3n-l%C3%B3gica)

## Anexo 4-U — Prueba de entrega, guía y acuses

Separa documento tributario ERP, prueba operacional de entrega y acuse del destinatario. El acuse técnico del SII no demuestra recepción física de mercadería. Conserva representación documental para traslado y tratamiento de destinatarios no habilitados, sin crear otro emisor fiscal.

**Cuándo consultarlo:** ante disputas de entrega, documentos inválidos o necesidades de evidencia de recepción.

[Ver este anexo en el original](../04_arquitectura/LAFROX-Subdocumento4-Anexos.md#anexo-4-u--prueba-de-entrega-gu%C3%ADa-y-acuses)

## Anexo 4-V — Protocolos de aceptación

Reúne protocolos de aceptación antes de la ola: concurrencia, fallas, reintentos y condiciones de negocio. AL-STOCK-01 y AL-ACT-01 comprueban reserva y autoridad sin doble descuento ni custodia duplicada. Complementa 4-M; las actas deben registrar resultados observados.

**Cuándo consultarlo:** para preparar aceptación técnica o una regresión de interfaces críticas.

[Ver este anexo en el original](../04_arquitectura/LAFROX-Subdocumento4-Anexos.md#anexo-4-v--protocolos-de-aceptaci%C3%B3n)

## Anexo 4-W — Memoria de cálculo del dimensionamiento

La memoria justifica capacidad y cantidades de T-11 en doce apartados. 4-W.1 define entradas/supuestos; .2 calcula TPS; .3 personas, concurrencia y dispositivos; .4 almacenamiento/retención/migración; .5 mensajes y enlaces; .6 terreno y sincronización; .7 atención; .8 capacidad local por máquina virtual; .9 nube; .10 crecimiento y respaldos; .11 cuellos de botella y .12 pruebas.

Entre los resultados están 10.920 muestras térmicas diarias y carga de prueba de 21,99 TPS. El dimensionamiento distingue sitio, ventana y factor de crecimiento; no suma máximos que ocurren en horarios diferentes. La mesa modela llegadas y capacidad, pero abandono y resolución requieren medición real. Los resultados son cálculos de diseño, pendientes de carga, cobertura, restauración y validación de supuestos.

**Cuándo consultarlo:** cuando se necesite justificar una cantidad, reserva, velocidad de enlace o capacidad, en vez de usar solo la cifra resumida.

[Ver este anexo en el original](../04_arquitectura/LAFROX-Subdocumento4-Anexos.md#anexo-4-w--memoria-de-c%C3%A1lculo-del-dimensionamiento)

## Lectura relacionada

El [resumen del Subdocumento 4](LAFROX-Subdocumento4-Resumen.md) explica las decisiones que estos anexos respaldan. Las matrices y protocolos describen compromisos y verificaciones previstas; una prueba solo se considera ejecutada cuando exista su evidencia.

---

**Fuente y actualización:** documento local vigente al 8 de octubre de 2026. Resumen elaborado con asistencia de Codex; no acredita aprobación del CLIENTE ni revisión humana adicional.
