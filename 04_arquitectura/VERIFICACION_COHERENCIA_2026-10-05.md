# LafroX — Verificación de coherencia SD3–SD4

Fecha: 5 de octubre de 2026. Verificación documental anterior al commit y push.

| Comprobación | Resultado |
| --- | --- |
| Fuentes activas SD3 | 22, con huellas en el manifiesto de SD3. |
| Tablas y filas de origen | 52 tablas; 1.182 filas de datos. |
| T-12 | 181 RF, 90 RNF y 374 RT; RT sin duplicados. |
| Actores | Quince nombres y filas coincidentes en Anexo 3.I y Anexo 4-N. |
| Partes lógicas / consolidados | Correspondencia íntegra tras normalizar rutas de enlaces. |
| Enlaces locales del cuerpo/anexos SD3–SD4 | 333 referencias comprobadas: archivo y ancla disponibles. |
| Física y centros de datos | Bloque 4.2–4.3 y cierre común idéntico al estado inicial de Git. |
| Memoria 4-W y cierre de anexos | Idénticos al estado inicial de Git. |
| T-11 | Idéntico al estado inicial de Git. |
| Nuevos protocolos | AL-STOCK-01 y AL-ACT-01 descritos en 4-V; sin atribuir ensayos realizados. |
| Volumen lógico | 2N + 2L; escenario de una retención por línea: 23.484/43.614 mensajes adicionales y total 202.145/303.769 antes de liberaciones/reintentos. |
| Tablas Markdown de SD3 | Separadores y anchura de filas válidos, sin comandos de renderizado o restos de paginación. |

Fuente de cálculo: N régimen = techo(260.000 ÷ (31.000/1.400)) = 11.742; N peak = techo(260.000 ÷ (31.000/1.400) × (2.600/1.400)) = 21.807. No es un máximo si una línea requiere retenciones de varios lotes o sitios. Se conserva la línea base física y se registra el recálculo de capacidad como dependencia.

Las comprobaciones son documentales. No se ejecutaron sistemas, pruebas operacionales, revisión gráfica completa, homologación de terceros ni revisión humana final. La coherencia de precio con SD2/RF históricas, las figuras fijadas al commit de origen y la incorporación física de CD-05 permanecen explícitas en [Coherencia SD3–SD4](COHERENCIA_SD3_SD4_2026-10-05.md). No se declara la oferta 100 % conforme por esta edición.

## Huellas del contenido técnico revisado

Estas huellas identifican el contenido anterior a publicación; el commit resultante se verifica en Git.

| Documento | SHA-256 del texto UTF-8 normalizado |
| --- | --- |
| 03_esquema_solucion_alcance/LAFROX-Subdocumento3.md | `9208d98eb2d6809e60c9e6718eae2e06eeffe0acad90f4b03d13ee20675d3f9a` |
| 03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md | `d0c49b9ab0ef833c844a819ae649784490c85539e5aaf1e3021d08f14fcdf0dc` |
| 03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md | `64369c3e2f6a28a97ae677dab8423778275a228eae5a64294a3cfe0f7f6845c2` |
| 04_arquitectura/LAFROX-Subdocumento4.md | `b00bc5ee3845df710a7e700cdc695ffcfd15a24c8f93b27e8e506cf1a4034a75` |
| 04_arquitectura/LAFROX-Subdocumento4-Anexos.md | `994836221c2fe4b82f3e97b6c8435d60415cd0983c723093cd356fdec83a665e` |
