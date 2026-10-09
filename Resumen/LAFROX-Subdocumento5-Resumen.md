# LafroX — Resumen del Subdocumento 5: Modelo y gestión de datos

[Índice de resúmenes](README.md) · [Documento original](../05_modelo_datos/LAFROX-Subdocumento5.md)

## Para qué sirve

La ficha versionada conserva tipo y rango térmico de origen. Antes de aprobación de Calidad, una regla PREVENTIVA_FICHA bloquea a la primera lectura válida fuera de rango; ausencia de parámetros mantiene el lote retenido. Plantillas, preferencias e intentos comparten cuatro canales y la baja comercial persiste entre versiones.

Explica qué información registra la solución, quién puede modificarla, cómo se conserva y cómo se migra desde los sistemas actuales. Su objetivo es que lotes, pedidos, entregas y cobros mantengan una historia verificable.

## El modelo en lenguaje de negocio

El [modelo](../05_modelo_datos/LAFROX-Subdocumento5.md#51-modelo) separa producto, lote sanitario y unidad logística; también distingue pedido, promesa, reserva, misión de preparación, entrega e intento. Esa separación evita que una segunda visita cuente como otro pedido o que un código externo cree un producto distinto.

El diccionario de Anexo 5-A contiene **111 entidades y 791 atributos**. Los quince almacenes lógicos distribuyen responsabilidades; no significan quince motores independientes. Una referencia entre dominios no se presenta automáticamente como una clave física de base de datos.

## Autoridad y operación sin conexión

La [gestión de datos](../05_modelo_datos/LAFROX-Subdocumento5.md#52-gesti%C3%B3n-de-datos) mantiene un escritor autorizado por conjunto de negocio. Bodega puede confirmar operaciones contra su base local; terreno registra hechos autorizados en el dispositivo. La réplica y la consolidación no otorgan una segunda autoridad.

Negocio, auditoría y la cola de salida se escriben juntos. Un identificador único permite reintentar sin repetir descuentos de stock o cobros: eso es **idempotencia**. Redis es una caché reconstruible, no el registro oficial. El ERP sigue siendo el único emisor fiscal; una captura de pago no acredita autorización bancaria.

## Indicadores y conservación

El OTIF se calcula contra la **promesa ORIGINAL**, contando cada pedido comprometido una sola vez e incluyendo no entregados. Una revisión posterior de la promesa no mejora artificialmente ese indicador. La analítica se separa del despacho para no competir por su capacidad.

La [retención](../05_modelo_datos/LAFROX-Subdocumento5.md#527-retenci%C3%B3n-archivado-eliminaci%C3%B3n-y-protecci%C3%B3n) depende de la clase de dato: documentos y prueba de entrega **6 años**, detalle térmico **5 años**, GPS personal **12 meses totales** y auditoría **7 años**. Se conservan reglas y calibraciones mientras hagan falta para interpretar expedientes. Las suspensiones de eliminación por conservación legal se respetan.

## Migración y desempeño

La [migración](../05_modelo_datos/LAFROX-Subdocumento5.md#53-estrategia-de-migraci%C3%B3n) incluye maestros, ventas de tres años, inventario de dos años, trazabilidad disponible y cartera viva con historia. La base estimada es **16,05478 GB** de fuente y **32,10956 GB** de destino con factor 2; son estimaciones sujetas a perfilado. No se inventan lotes, fechas ni columnas del legado.

Se requieren al menos dos ensayos completos, conciliación, deltas del período y reversión con un escritor único. [Las pruebas de desempeño](../05_modelo_datos/LAFROX-Subdocumento5.md#54-estrategia-de-desempe%C3%B1o) usan escenarios de SD4; el retiro en menos de dos horas debe cubrir también exposición potencial y datos pendientes de sedes desconectadas.

## Relaciones y estados

SD3/T-12 fija obligaciones; SD4/T-11 fija autoridades y capacidad; SD7 programa migración. **RT-05.10 y RT-05.24 no están ofertados** como capacidades deseables; **RT-05.30 se oferta mediante INN-03** del SD13. Diccionario, fórmulas e indicadores no acreditan por sí solos automatizaciones adicionales. Las pruebas descritas están propuestas para el proyecto.

---

**Fuente y actualización:** documento local vigente al 8 de octubre de 2026. Resumen elaborado con asistencia de Codex; no acredita aprobación del CLIENTE ni revisión humana adicional.
