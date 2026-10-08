# LafroX — Resumen del Subdocumento 4: Arquitectura lógica y física

[Índice de resúmenes](README.md) · [Documento original](../04_arquitectura/LAFROX-Subdocumento4.md)

## Para qué sirve

Explica cómo se implementa técnicamente el alcance, dónde se ejecuta cada componente y cómo se sostiene la operación ante fallas. Se lee en tres partes: lógica, infraestructura física y recuperación de centros de datos.

## Arquitectura lógica: responsabilidades e intercambios

La [arquitectura lógica](../04_arquitectura/LAFROX-Subdocumento4.md#41-arquitectura-l%C3%B3gica) organiza **ocho capas**: presentación, borde, puerta de servicios, negocio, integración, datos, seguridad y observabilidad. El negocio se divide en **doce módulos M1–M12**, con responsabilidad y propiedad de datos definidas.

El núcleo usa **Laravel 13 y PHP 8.5** como monolito modular: una base de código con procesos críticos separables, para mantener un despliegue operable por el pequeño equipo TI. PostgreSQL/PostGIS sostiene datos transaccionales; las aplicaciones móviles conservan capturas locales. Keycloak gestiona identidad y CloudWatch reúne observabilidad. Estas son tecnologías declaradas en la fuente, no una verificación de sus versiones externas.

Las **15 integraciones** separan ocho contratos internos y siete externos. La integración con ERP se encapsula; el ERP conserva emisión fiscal. La prueba de entrega, la guía tributaria y los acuses son registros distintos. Los reintentos usan identificadores únicos para evitar efectos duplicados. Véanse [el catálogo](../04_arquitectura/LAFROX-Subdocumento4.md#416-cat%C3%A1logo-de-interfaces) y [la articulación documental](../04_arquitectura/LAFROX-Subdocumento4.md#4117-articulaci%C3%B3n-entre-prueba-de-entrega-dte-y-acuse).

## Arquitectura física: nube y autonomía local

La [arquitectura física](../04_arquitectura/LAFROX-Subdocumento4.md#42-arquitectura-f%C3%ADsica) combina servicios de AWS con operación local en Talca, Concepción y tres plataformas de cross-docking. Talca tiene un clúster local; Concepción y las plataformas cuentan con equipos activos y en espera. La conectividad combina fibra, red móvil y satélite según el sitio.

Los cinco ambientes separan construcción, pruebas y operación. La promoción usa artefactos verificados y reversión controlada; la bodega conserva **24 horas** de autonomía y terreno **14 horas**. La reserva central y las decisiones que dependen de terceros no se convierten en confirmaciones locales por perder conexión.

## Capacidad y equipos

El [dimensionamiento](../04_arquitectura/LAFROX-Subdocumento4.md#426-dimensionamiento-y-plan-de-capacidad) parte de escenarios y supuestos, con detalle en Anexo 4-W. Las quince integraciones representan **230.252 mensajes diarios normales** y **353.333 en peak**; no son transacciones únicas sumables. La telemetría térmica aporta **10.920 muestras diarias**. La prueba de carga de referencia es **21,99 TPS**, transacciones por segundo, distribuida por lugar.

T-11 distingue unidades instaladas, repuestos y crecimiento. Por ejemplo, el parque inicial de reparto parte de **96 + 10 de reserva = 106** por tipo correspondiente; **110 instaladas + 11 de reserva = 121** es la proyección del año 3. La memoria permite comprobar el período de cada cantidad antes de comparar cifras.

## Recuperación y límites

La [estrategia de centros de datos](../04_arquitectura/LAFROX-Subdocumento4.md#43-data-center) usa región primaria **sa-east-1** y secundaria **us-east-1**. Los objetivos críticos son **RTO ≤ 4 h** —tiempo de recuperación— y **RPO ≤ 15 min** —antigüedad máxima de la copia recuperable—. Infraestructura **99,95 %**, transacción crítica **99,9 %** y cero interrupción en despacho son obligaciones diferentes.

[El riesgo residual](../04_arquitectura/LAFROX-Subdocumento4.md#4324-rpo-y-rto) es perder los tres caminos de comunicación y después el sitio antes de reponer un enlace: la última copia remota podría superar 15 minutos. Las colas locales no demuestran por sí solas ese RPO. Los anexos 4-M y 4-V fijan ensayos; su descripción no acredita ejecución.

## Dónde continuar

SD5 detalla los datos; T-11 las especificaciones; SD7 el despliegue; SD8 los riesgos. Los anexos 4-A–4-W permiten consultar eventos, interfaces, decisiones, seguridad y cálculos sin recorrer nuevamente todo el capítulo.

---

**Fuente y actualización:** documento local vigente al 8 de octubre de 2026. Resumen elaborado con asistencia de Codex; no acredita aprobación del CLIENTE ni revisión humana adicional.
