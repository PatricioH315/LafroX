# LafroX — Resumen de los anexos del Subdocumento 3

[Índice de resúmenes](README.md) · [Documento original](../03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md)

## Para qué sirve

Esta guía explica los 11 anexos del capítulo 3 por separado. Permite elegir el listado, protocolo o cálculo que se necesita sin recorrer todas sus tablas. Los identificadores conservan la nomenclatura del original.

## Anexo 3.A — Catálogo de requerimientos funcionales

Detalla los 175 requisitos funcionales ofertados: 134 del caso, 34 de las Bases y 7 propios. Identifica actor, comportamiento, precondición, resultado, prioridad y etapa. Relaciona las familias F-01–F-14 con requisitos atómicos. Los códigos RF-14.01–05-BTT distinguen obligaciones de seguridad de los códigos de telemetría del caso; compartir número no hace equivalentes ambas obligaciones.

**Cuándo consultarlo:** para conocer exactamente qué debe hacer una función y evitar confundir 175 compromisos con las 181 filas RF del T-12.

[Ver este anexo en el original](../03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md#anexo-3a--cat%C3%A1logo-de-requerimientos-funcionales)

## Anexo 3.B — Catálogo de requerimientos no funcionales

Define los umbrales y verificaciones de disponibilidad, autonomía, desempeño, seguridad y operación. El conjunto ofertado suma 86 RNF al incluir requisitos propios; el T-12 contiene 90 filas al agregar alias y materias absorbidas. Las pruebas tienen que demostrar el umbral en el escenario aplicable: no basta con describir un mecanismo técnico.

**Cuándo consultarlo:** para convertir una cualidad como «resiliente» o «rápido» en una condición verificable.

[Ver este anexo en el original](../03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md#anexo-3b--cat%C3%A1logo-de-requerimientos-no-funcionales)

## Anexo 3.C — Registro de supuestos

Registra S-01–S-43 con fundamento, impacto y validación. Los primeros dieciséis conservan decisiones del SD2; los demás desarrollan metas, capacidad y condiciones de implantación. S-42 compromete al menos 15 % menos consultas asistidas por cliente activo al cierre del primer año de Operación, con línea base en marcha blanca. S-43 fija Desarrollo, QA y Preproducción de lunes a viernes de 08:00 a 20:00, salvo ventanas de prueba programadas por el CLIENTE y activación inmediata para correcciones críticas; 60/168 horas fundamentan una meta de al menos 60 % menos cómputo. No acredita aprobación del CLIENTE. Por ejemplo, los datos incompletos de inventario se investigan: el 2,3 % de diferencia actual no es tolerancia automática de migración.

**Cuándo consultarlo:** cuando una cantidad, plazo o comportamiento dependa de una hipótesis aún por confirmar.

[Ver este anexo en el original](../03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md#anexo-3c--registro-de-supuestos)

## Anexo 3.D — Registro de exclusiones

Conserva las nueve exclusiones del caso: ERP, remuneraciones, POS del cliente, venta al consumidor final, liquidación de transportistas, red logística, robotización, mantención mecánica y compra del hardware de terreno. Integrar transportistas no significa administrar sus contratos. Excluir la compra de equipos no elimina la obligación de LafroX de especificarlos.

**Cuándo consultarlo:** al revisar si una solicitud nueva pertenece al contrato o exige control de cambios.

[Ver este anexo en el original](../03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md#anexo-3d--registro-de-exclusiones)

## Anexo 3.E — Registro de restricciones

Relaciona las doce restricciones con el diseño: despacho de 96 camiones sin interrupción, autonomía de 24 h en CD y 14 h en terreno, ERP como emisor, frío a −22 °C, fechas prohibidas y equipo TI limitado. Preserva canal tradicional, privacidad y reglas de emisión tributaria. Son límites obligatorios, no riesgos que puedan aceptarse para omitirlos.

**Cuándo consultarlo:** antes de aprobar una arquitectura, corte o procedimiento de contingencia.

[Ver este anexo en el original](../03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md#anexo-3e--registro-de-restricciones)

## Anexo 3.F — Registro de decisiones de alcance y de diseño

Registra elecciones de alcance y diseño con sus fundamentos, incluyendo reparto entre etapas, ambientes y criterios comunes. D-03, D-11 y D-12 unifican valores que tuvieron más de una formulación. El registro identifica decisiones de LafroX y no convierte su aceptación por el comité en un hecho ya ocurrido.

**Cuándo consultarlo:** para entender por qué se eligió una alternativa y dónde registrar su modificación.

[Ver este anexo en el original](../03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md#anexo-3f--registro-de-decisiones-de-alcance-y-de-dise%C3%B1o)

## Anexo 3.G — Registro de reglas de negocio

Fija quién decide ante cada evento y qué consecuencia tiene. RNG-01 reserva en confirmación central; RNG-04 gradúa respuesta térmica con decisión de Calidad; RNG-08 conserva precio pactado y RNG-09 define OTIF. RNG-15 diferencia promesa urbana según hora de captura y promesa rural/periférica/cross-docking. Las reglas parametrizables necesitan valores y autorizaciones trazables.

**Cuándo consultarlo:** cuando dos módulos deban responder de la misma forma a stock, precio, crédito, temperatura o entrega.

[Ver este anexo en el original](../03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md#anexo-3g--registro-de-reglas-de-negocio)

## Anexo 3.H — Registro de vacíos y consultas

Distingue preguntas pendientes de resoluciones documentales. V-04 y V-05 están resueltas documentalmente; V-03 adopta cinco ambientes pero mantiene pendiente aclaración formal. V-01 pregunta por cinco o seis instalaciones y V-12 por inicio contractual. Ninguna fila acredita respuesta recibida del mandante ni aceptación operacional.

**Cuándo consultarlo:** antes de tratar una fecha, cantidad de sitios o aclaración como confirmada.

[Ver este anexo en el original](../03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md#anexo-3h--registro-de-vac%C3%ADos-y-consultas)

## Anexo 3.I — Participación de los grupos de interés

Organiza participación de los diecinueve interesados con actividad, momento, responsable, indicador y respuesta ante resistencia. Un apartado distingue quince actores de aplicaciones y portales. Representantes de proveedores/transportistas acceden a su organización; conductor externo conserva identidad propia. Food service mantiene su segmento sin crear automáticamente un actor adicional.

**Cuándo consultarlo:** para planificar adopción y acceso; la matriz de permisos por acción se realiza en Anexo 4-N.

[Ver este anexo en el original](../03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md#anexo-3i--participaci%C3%B3n-de-los-grupos-de-inter%C3%A9s)

## Anexo 3.J — Criterios de aceptación

Convierte los dieciséis resultados R18 en metas, momento y método. Incluye retiro en menos de 2 h, lotes completos, continuidad y rutas en menos de 20 minutos. OTIF usa metas propias 90/93/95 % en meses 15/19/32. Algunos resultados se aceptan provisionalmente y se confirman tras operación; una marcha blanca no demuestra por sí sola una mejora anual.

**Cuándo consultarlo:** para preparar las pruebas y distinguir aceptación provisional de verificación definitiva.

[Ver este anexo en el original](../03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md#anexo-3j--criterios-de-aceptaci%C3%B3n)

## Anexo 3.K — Glosario de siglas y códigos

Explica siglas y códigos de los anexos y T-12: Bases, requerimientos, módulos y conceptos logísticos/técnicos. Facilita leer la trazabilidad sin confundir identificadores de familias con requisitos individuales o códigos de documentos diferentes.

**Cuándo consultarlo:** cuando una sigla o un código impida seguir la lectura.

[Ver este anexo en el original](../03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md#anexo-3k--glosario-de-siglas-y-c%C3%B3digos)

## Lectura relacionada

El [resumen del Subdocumento 3](LAFROX-Subdocumento3-Resumen.md) explica las decisiones que estos anexos respaldan. Las matrices y protocolos describen compromisos y verificaciones previstas; una prueba solo se considera ejecutada cuando exista su evidencia.

---

**Fuente y actualización:** documento local vigente al 8 de octubre de 2026. Resumen elaborado con asistencia de Codex; no acredita aprobación del CLIENTE ni revisión humana adicional.
