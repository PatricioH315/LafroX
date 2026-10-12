# LafroX — Matriz de trazabilidad de observaciones del Subdocumento 5

Respuestas documentales del cuerpo y anexo LaTeX vigentes, conforme al Art. 46. La tabla contiene únicamente las veinte observaciones del Informe 1, cada una con su respuesta y sección modificada. Los ensayos siguen programados para el proyecto; no se presume respuesta oficial a la consulta de códigos.

| Observación del Informe 1| Respuesta | Sección modificada |
| --- | --- | --- |
| No hay modelo de datos; 5.1 solo enumera quince bases lógicas. | Se incorporaron MR general, vistas por dominio y modelo dimensional: diez figuras en el cuerpo. | 5.1; Figuras 5.1–5.10; 5-M |
| No hay diccionario real; se posterga hasta antes de producción. | Diccionario de 121 entidades y 987 atributos, con tipos, dominios, claves, condiciones y controles. | 5-A, A.2–A.10; 5-B–5-C |
| No pueden evaluarse las consultas del proveedor y la autoridad sanitaria. | Cadena lote/unidad/evento/entrega/documento y consulta inversa; universo potencial offline y presupuesto de retiro de 85 min. | 5.1.7; Figura 5.5; 5-J |
| Motor y CAP se presentan en tabla sin analizar compromisos. | Justificación en prosa de motores, autoridad única por agregado y consistencia local con consolidación pendiente. | 5.2.1–5.2.3; 5-B |
| Se cita la decisión 16.1 n.º 18, inexistente. | Referencia retirada; las fuentes identifican decisiones existentes del numeral 16.1. | 5.1; fuentes de Figuras 5.1, 5.2, 5.4 y 5.6 |
| Incorporar alcance histórico y saneamiento: lotes libres, clientes duplicados y saldos de envases. | Históricos delimitados; originales preservados, equivalencias aprobadas y defectos aislados sin inventar historia. | 5.3.1–5.3.5; 5-C; 5-L, A.25 |
| Migración sin volumen, herramientas, tiempos, ventana ni responsables. | Fuente 16,05478 GB; destino estimado 32,10956 GB; herramientas, responsables, dos ensayos, olas, corte y reversa. | 5.3; Tabla 5.2; 5-J; 5-L |
| OK: índices para retiro, partición mensual y orden en mensajería. | Se conservan; claves globales sin partición y detalle temporal con identidad completa, outbox y deduplicación. | 5.4.2–5.4.5; 5-F–5-G |
| La expresión de TPS base y crecimiento es ininteligible. | Se separan régimen 12,34 TPS, pico 14,66 y prueba 21,99; año 3 y crecimiento 3× son escenarios distintos. | 5.4.1; Tabla 5.3; 5.4.6 |
| Identidad de bodega con TTL de 8 h frente a autonomía exigida de 24 h. | Se distinguen autonomía 24 h, identidad 24 h, turnos 8/14 h y manifiesto 26 h con relevos preinscritos. | 5.2.3; Tabla 5.1; 5-G |
| OK: separación OLTP/analítica, latencias, retenciones, inmutabilidad e ISO 25012. | Se mantienen y precisan calidad, archivo, purga, retención legal y conservación de reglas interpretativas. | 5.2.5–5.2.7; 5-D–5-E; 5-H–5-I |
| OK: detecta desajuste RT-05.10/RT-16.10 y lo eleva a consulta. | Correspondencia y consulta documentadas; plazos íntegros conservados. No se presume envío acreditado ni respuesta oficial. | 5.2.7; 5-D, A.14 |
| Faltan esquema estrella dibujado, tableros, destinatarios e indicadores definidos. | Modelo dimensional con granos y claves; fórmulas, audiencia, latencia y linaje. El costo de servir identifica combustible, peajes, conducción, descarga e indirectos, con prorrateos versionados y conciliación con el ERP. | 5.1.11; Figura 5.7; 5.2.6; 5-H, Tablas A.18–A.19 |
| RT-16.08 se atribuye a tres canales; corresponde RT-16.20. | RT-16.20 identifica canales y RT-16.08 consulta/exportación de auditoría. | 5.1.9; 5-B–5-C; A.8 |
| Timbre diferido y guía ausente contradicen ERP único emisor y acompañamiento del traslado. | ERP emite antes del traslado; cambios requieren nueva guía válida. POD no sustituye documento fiscal. | 5.1.8; 5.3.6; 5-J, AL-DTE-01 |
| OK: evidencia por receptor; falta mecanismo de acuse legal. | POD, acuse SII y recibo se diferencian; XML ERP/EDI o constancia impresa según perfil, conforme al Anexo 4-U. | 5.1.8; A.7; 5-C; 5-J |
| Resaltado negro ilegible en páginas 3, 10, 13 y 14. | Retirados los bloques de código con fondo negro; contenido integrado en la plantilla de texto, tablas y figuras. | Cuerpo y anexos |
| Metadatos finales citan documentos inexistentes. | Línea de metadatos retirada; referencias identifican Bases, propuesta y fuentes técnicas concretas, con T-12 adscrito al SD3, T-11 al SD4, T-14 incluido en el anexo y versión EPCIS alineada. | Referencias del cuerpo y anexo |
| Doble numeración 5.1/S5.1 y códigos internos sin explicación. | Numeración 5.1–5.4 y anexos 5-A–5-M; glosario y leyendas definen los identificadores necesarios. | Introducción; 5-A, glosario y A.1 |
| Siglas sin definir, incluida la frase sobre FID. | FID y la frase observada se retiraron; glosario común y desarrollo de CAP en el texto. | Introducción; 5.2.1; 5-A |
