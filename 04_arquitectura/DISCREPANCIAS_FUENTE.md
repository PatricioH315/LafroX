# LafroX — Discrepancias conservadas de la fuente

Actualización del 5 de octubre de 2026: la lógica y sus anexos incorporan correcciones de diseño autorizadas y dejan de ser una conversión literal de la fuente indicada abajo. El registro vigente de cambios y dependencias es [Coherencia SD3–SD4](COHERENCIA_SD3_SD4_2026-10-05.md); el contenido siguiente conserva las observaciones de la conversión original.

Fecha: 3 de octubre de 2026. Fuente fijada: `rama-latex`, `732a9d6688569bf981594c2e21c47a167b8f8ba7`.

La sincronización conserva el texto efectivo del fuente. Este registro distingue problemas documentales de la fuente de errores de conversión. No se atribuye aprobación contractual, revisión humana ni ejecución de ensayos a la conversión.

## Confirmadas por contraste textual

1. **Declaración de IA.** El cierre del cuerpo declara revisión final no realizada y remite a 22 anexos, mientras el catálogo contiene 23 (4-A–4-W). Las tablas de IA de anexos mantienen filas «No realizada». Se preservan esas declaraciones para no inventar una revisión humana. La cobertura de 4.2, 4.3, W y T-11 debe revisarse antes de una entrega final.
2. **Adquisición de equipamiento.** La introducción vigente de T-11 atribuye la compra del equipamiento físico al CLIENTE. El informe `REVISION_T11_2026-10-03.md` cuestiona esa atribución frente al alcance contractual. Se conserva la frase para alinear versiones; resolver responsabilidades requiere una corrección explícita del fuente y su sincronización posterior.
3. **Calendario y redondeo.** Las fórmulas muestran 22,14 días y factor 1,857, pero los resultados publicados usan más precisión. Por ejemplo, dividir 260.000 por 22,14 y multiplicar por cinco no produce exactamente 58.710. Se conserva el resultado publicado y el texto de su derivación; no se recalcula usando únicamente el número redondeado.
4. **INT-12.** G declara 12.602/23.404 cambios como cota conservadora de todos los sitios; I lo resume como cambios a réplica y lo combina con WAL de Talca. Se conserva la diferenciación del detalle: no presentar esa cota como medición propia de Talca.
5. **Dotación auxiliar.** El resumen de `Dimensionamiento/dimensionamiento/resultados.md` no debe sustituir la tabla normal/peak del cuerpo y de W. Los Markdown preservan las tablas de los fragmentos entregables.

## Asuntos que los registros de revisión mantienen abiertos

- Fechas de ADR y FinOps aparecen como asuntos omitidos por decisiones D34/D35; la conversión no los completa.
- Los registros señalan diferencias de figuras respecto de ECR, gateways y bandejas, además del uso de recortes de capas. Se enlazan las figuras efectivamente publicadas; no se certificó su revisión visual ni se recrearon.
- El informe de T-11 contiene propuestas que ya no describen el árbol efectivo: la fila A-04 de ACL/erp-sync sí existe en la fuente convertida. Cada hallazgo requiere volver a contrastarse antes de una corrección; no copiar listas históricas de pendientes sin verificación.
- Capacidades o modelos adicionales solicitados en los informes de revisión no se inventan durante esta sincronización.

## Representación Markdown

Las referencias a páginas se sustituyen por enlaces a las secciones correspondientes. Los cuatro gráficos TikZ se identifican por título, fuente y transcripción de rótulos; esa representación conserva información textual, pero no la geometría ni el diseño gráfico. Las fórmulas usan símbolos Unicode y los identificadores conservan sus nombres. Los 26 archivos de figuras enlazados se verificaron contra el árbol Git fijado.

Fuentes de revisión: [Revisión general](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/00/trazabilidad/REVISION_INCOHERENCIAS_2026-10-03.md), [Revisión T-11](https://github.com/PatricioH315/LafroX/blob/732a9d6688569bf981594c2e21c47a167b8f8ba7/00/trazabilidad/REVISION_T11_2026-10-03.md).
