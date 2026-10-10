# LafroX — Resumen del Subdocumento 3: Alcance de la solución

[Índice de resúmenes](README.md) · [Documento original](../03_esquema_solucion_alcance/LAFROX-Subdocumento3.md)

## Para qué sirve

Define qué construye LafroX, cómo se reparte entre etapas y qué evidencia debe permitir aceptarlo. Es el puente entre el diagnóstico del SD2 y el diseño técnico del SD4.

## Qué incluye y cuándo se entrega

La **Etapa 1** incorpora recepción con lotes, inventario y preparación, preventa sin señal, rutas, frío, reparto, devoluciones, rendición y trazabilidad. La **Etapa 2** agrega portales, intercambio electrónico con cadenas y costo de servir, usando los hechos capturados en la primera. Véase [el reparto funcional](../03_esquema_solucion_alcance/LAFROX-Subdocumento3.md#321-reparto-entre-etapas-y-dependencias).

El [calendario contractual](../03_esquema_solucion_alcance/LAFROX-Subdocumento3.md#312-implementaci%C3%B3n-implantaci%C3%B3n-y-operaci%C3%B3n) fija desarrollo E1 en meses **1–12**, marcha blanca **13–15** y producción **16**; desarrollo E2 **13–18**, marcha blanca **19–20** y producción **21**. La Operación cubre los meses **21–56**, 36 meses. La fecha real de inicio sigue siendo una consulta; los meses relativos no equivalen a fechas confirmadas.

## Cómo funcionaría

Doce módulos de negocio comparten identidad, integración, auditoría y operación desconectada. La captura en terreno conserva información hasta sincronizar; una captura sin señal no equivale a stock reservado ni a un pedido central confirmado. El ERP sigue siendo el único emisor de documentos tributarios. La [definición de actores](../03_esquema_solucion_alcance/LAFROX-Subdocumento3.md#342-vista-general-de-la-soluci%C3%B3n) distingue **15 actores del sistema** de los **19 interesados del negocio**; participar en un comité no concede una cuenta de acceso.

Las [reglas de negocio](../03_esquema_solucion_alcance/LAFROX-Subdocumento3.md#324-reglas-de-negocio-y-consultas) mantienen el precio acordado al capturar el pedido, registran excepciones de crédito y reservan stock al confirmar en el servidor central. Calidad dispone sobre lotes con excursiones térmicas. El canal tradicional conserva la visita y el efectivo.

## Cifras y aceptación

El [catálogo ofertado](../03_esquema_solucion_alcance/LAFROX-Subdocumento3.md#323-cat%C3%A1logo-de-requerimientos-y-correspondencia) contiene **175 requerimientos funcionales** y **86 no funcionales**. T-12 incluye **181 filas RF y 90 RNF** al añadir materias absorbidas, alias o no ofertadas; no son conteos intercambiables.

La aceptación exige, entre otros resultados, identificar afectados por lote en **menos de 2 horas**, capturar lote donde corresponde y sincronizar sin perder ni duplicar pedidos. Las metas propias de OTIF son **90 % en mes 15, 93 % en mes 19 y 95 % en mes 32**; no son resultados ya alcanzados. Véase [cómo se verifica](../03_esquema_solucion_alcance/LAFROX-Subdocumento3.md#325-criterios-de-aceptaci%C3%B3n).

## Implantación y pendientes

Las olas deben demostrar cuatro semanas de operación real, usuarios certificados, conciliación y acta de la Contraparte Técnica. La reversión debe restituir el despacho antes de las **05:30**; volver al papel no demuestra capacidad para 96 camiones. El objetivo de **40 minutos** necesita ensayo.

Los anexos separan requisitos, supuestos, exclusiones, restricciones, decisiones, reglas y consultas. Consultarlos evita tratar una hipótesis como aprobación. SD7 programa el trabajo y SD8 evalúa las condiciones que amenazan su aceptación.

---

**Fuente y actualización:** documento local vigente al 8 de octubre de 2026. Resumen elaborado con asistencia de Codex; no acredita aprobación del CLIENTE ni revisión humana adicional.
