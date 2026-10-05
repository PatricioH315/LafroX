# LafroX — Coherencia funcional SD3–SD4

Fecha: 5 de octubre de 2026. Rama: `alvaro-md`. Base local: `e87513b`.

## Fuentes y autorización

El equipo autorizó aplicar el plan de coherencia y publicar sus cambios. La fuente nueva de SD3 es `D:/Usuario/Descargas/03_esquema_solucion_alcance/03_esquema_solucion_alcance`, con contenido.tex, anexos.tex, sus inclusiones activas y LAFROX-Formulario-T-12.tex. Se convirtieron únicamente a Markdown; los originales se conservan. Las tablas auxiliares no incluidas por el ensamblador no sustituyen las tablas vigentes. Se retiró el mobiliario de página del PDF anterior, conservando texto técnico, tablas y referencias. La Figura 3.4 se conserva como descripción estructurada; sus quince actores fueron validados con el redactor de SD3 según comunicación del equipo en esta conversación. Esa validación no equivale a aprobación contractual ni revisión humana final de todos los entregables.

El SD4 parte de la conversión de `rama-latex` en `732a9d6`, más CD-05. Desde esta intervención, la lógica Markdown incorpora decisiones posteriores y ya no es una copia técnica idéntica de aquel commit. Física, centros de datos, memoria 4-W y T-11 mantienen su contenido publicado.

## Cambios implementados

| Materia | Fuente funcional | Realización lógica y evidencia documental |
| --- | --- | --- |
| Quince actores | SD3 Figura 3.4, 3.4.2.1 y Anexo 3.I | SD4 4.1.3.1.1, matriz del Anexo 4-N y AL-ACT-01. |
| Organizaciones y personas | Empresas transportistas, proveedores y conductores del SD3 | Identidad personal del representante, aislamiento por empresa y separación respecto del conductor. |
| Interesados sin cuenta | Diecinueve interesados del SD2/SD3 | Gobierno, sindicato, evidencia sanitaria y peoneta no otorgan acceso automático. Food service conserva su segmento y perfil por canal acordado. |
| Etapas | SD3 3.2.1 y 3.4.2 | OTIF/telemetría en E1, costo de servir y portales en E2; asignación de conductores por despacho en E1. |
| Temperatura | S-04, RNG-04 y RF-09.05/06/07 | Advertencia menor/transitoria y retención crítica/sostenida; umbral, duración y disposición exclusiva de Calidad. |
| Reserva | S-08, RNG-01, RF-03.03 y CD-05 | Orden central con desempate y retención local durable; contratos INT-03/04, 4-I y AL-STOCK-01. |
| Promesa y reentrega | RNG-15 y RNG-05 | Ventana 24/48 h, corte 14:00, intento, reagendamiento y retorno trazable. |
| Precio | RNG-08 de SD3 | Conservación del precio pactado bajo condiciones autorizadas; discrepancias con SD2 y RF históricas registradas abajo. |
| Reversión | SD3 3.4.4 y S-14; caso cap. 10 | Legado en lectura; reversión del nuevo software con escritor único; respaldo manual no acredita las 96 salidas críticas. |
| Referencias RF | Anexo 3.A y T-12 | Cobranza vinculada a RF-07.05/09; ERP por contrato INT-06. No se usa RF-07.06 (estado de cuenta) como cobro. |
| Estado de guía | ERP único emisor; AL-DTE-01 | Propuesta de cambio se pospone si falta conexión; una guía anulada/invalidada no se reutiliza. |

## Dependencias que requieren una decisión compartida

1. **Precio.** SD2 S-09 conserva precio al despacho con excepciones; SD3 S-09/RNG-08 conserva precio pactado y RF-03.11/12 aún describe excepciones al precio de despacho. SD4 realiza la regla explícita del SD3 sin alterar SD2 ni esas filas por inferencia. Comercial y los redactores deben consolidar una regla única y actualizar S-09, RF-03.11/12 y T-12 antes de presentar la oferta o liberar el contrato. El cambio de una lista no se interpreta como autorización para modificar un precio acordado.
2. **Reserva y latencia.** AL-STOCK-01 debe probar confirmación con viaje central–sitio, congestión y pérdida de acuse. Una espera de transporte de 30 segundos no demuestra cumplir las latencias operacionales. No hay resultados de ensayos implantados por esta edición.
3. **Capacidad física.** La coordinación añade 2N + 2L mensajes antes de reintentos. 4-I declara el incremento y su escenario de sensibilidad; 4.2 y 4-W requieren incorporar consumidores/colas por sitio, IAM, tráfico, IOPS y p95 de confirmación. Las cifras físicas actuales siguen siendo la línea base, no el dimensionamiento final del nuevo protocolo.
4. **Figuras.** Los enlaces de SD4 están fijados al commit histórico y no se regeneran en esta rama Markdown. Los rótulos y conexiones de las fuentes gráficas deben cotejarse con el catálogo de quince actores, permisos, etapas y regla térmica antes de entrega. Los recortes de capas conservan la observación de las Aclaraciones.
5. **Continuidad.** La contingencia manual del SD3 no acredita una ventana de despacho que el caso declara imposible de ejecutar a mano. AL-DTE-01 y AL-OFF-01 deben verificar cada sitio con guía válida y los estados descritos; el aislamiento total con pérdida de sitio conserva el límite residual de DR declarado en 4.3.2.
6. **Requisitos y EDT.** Las descripciones y asociaciones históricas de T-12 que no se resuelven por una fuente inequívoca permanecen documentadas. No se inventan paquetes EDT ni resultados de pruebas para completar celdas.
7. **Entrega final.** Fechas históricas ADR, revisión humana, FinOps y discrepancias gráficas anteriores conservan sus registros. La definición de actores validada no acredita aprobación del documento completo.

## Verificación y publicación

La comprobación compara las quince filas de actores en SD3/SD4, la igualdad entre partes y consolidados, identificadores y filas de las fuentes activas, enlaces locales, tablas Markdown y conservación del bloque físico, centros de datos, memoria y T-11. El manifiesto de SD3 registra huellas de fuentes y la verificación de esta intervención. Solo se versionan Markdown del alcance; `md para drive/` permanece fuera del commit.

Se consulta `origin/alvaro-md`, se comprueba avance directo y se crea el commit de coherencia antes de publicar mediante push ordinario. La rama tenía un commit local previo (`e87513b`) que ajusta SD1 y añade CD-05: se revisa como parte de los commits pendientes y su publicación, sin cambiar su historia. El hash final se obtiene de Git, no se inventa dentro del documento.
