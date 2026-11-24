# Cotejo de orígenes de la Tabla 3.A.1

## Alcance y versiones

La Tabla 3.A.1 contiene 134 requisitos funcionales. El inventario `localizacion_origenes_3a1.csv` localiza las secciones, capítulos y códigos que puede reconocer automáticamente en sus columnas de origen. Se consultaron las Bases del Caso y las Bases Transversales de la rama corregida del SD4 y los anexos y el cuerpo de la rama corregida del SD2. Que un localizador exista no demuestra que todas las condiciones del requisito provengan de él; esa comprobación se registra por separado.

## Análisis individual

| Requisito | Fuente examinada y hallazgo | Resultado |
|---|---|---|
| RF-01.01 | Caso §4.1 describe la recepción, el conteo contra la guía y el ingreso posterior; Caso §9.4 trata diferencias entre lo pedido, despachado y recibido en el contexto de la entrega al cliente. Los pasajes examinados no formulan literalmente la alerta por SKU ni la regla de no bloquear el cierre de la recepción del proveedor. | El Caso sustenta la recepción y el conteo contra la guía. La comparación por SKU con la OC, la alerta por discrepancia, el cierre sin bloqueo y la disponibilidad del comparativo para Calidad se identifican como definiciones de diseño de LafroX. La sección 9.4 trata la entrega al cliente y no se usa como fundamento de estos controles de recepción. |

El resultado anterior no anticipa el de las demás filas. Sus localizadores se enumeran en el inventario, pero el contraste semántico de las restantes está pendiente.
