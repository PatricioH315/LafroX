# LafroX — Correcciones y segunda revisión de coherencia del Subdocumento 4

Fecha: 9 de octubre de 2026. Rama efectiva: `rama-md`. Base Git: `e76e0c7` más cambios preexistentes, que se conservaron. Trabajo exclusivamente Markdown, sin commit ni push.

**Resultado: diez hallazgos documentales cerrados, H09 retirado por aceptación expresa del usuario y H03 con cierre parcial.** Los enlaces a las figuras PDF vigentes son válidos para el documento y no requieren conversión a imágenes. H03 necesita definición formal del CLIENTE. Además, se mantienen las 28 revisiones humanas pendientes de la declaración consolidada de SD4; no se acredita aceptación operacional.

## Resultado por hallazgo

| Hallazgo inicial | Estado tras corrección | Cambio y evidencia vigente |
| --- | --- | --- |
| H01 · Criticidad y restauración 4–8 h | Cerrado documentalmente | SD4 4.2.4.5, Tabla 17: temperatura, POD y DTE recuperan su porción funcional crítica en ≤4 h y RPO ≤15 min; histórico completo ≤8 h sin bloquear operación. El ensayo distingue ambos tiempos. Las Tablas 37–38 mantienen la criticidad y sus objetivos. |
| H02 · Dos escritores al promover | Cerrado documentalmente | SD4 4.2.4.3 exige apagado/exclusión comprobada antes de promover; pérdida de ambas redes solo genera alarma. Sin exclusión, réplica de lectura y nuevas confirmaciones suspendidas. Retorno como réplica, sin promoción automática del antiguo primario. Conmutación <1 min desde exclusión comprobada; recuperación total ≤4 h si exige presencia. Propagado a Tabla 20, ADR-10 y T-11. Aceptación incluye partición, pérdida de réplica y retorno. |
| H03 · Congelamientos y parches críticos | Parcial: definición contractual pendiente | SD4 4.2.4.1.4 distingue cinco días hábiles habilitados para cambios ordinarios, medición calendario, restauración en cuatro horas y desarrollo de un parche. Se mantienen 7/15/30 días corridos desde publicación/detección. Contención no equivale a remediación. Intervención prohibida exige aclaración formal del CLIENTE; no se inventa excepción ni se pausa el plazo. RT-11.04 conserva Cumple parcialmente por este escenario. |
| H04 · Dotación mes 25 | Cerrado | Tabla 33, dimensión 16: 19 personas normales y 21 peak desde mes 25; mesa 9/11 más NOC/SOC 10, como 4-W.7 y T-15. El cálculo de 348 horas-posición usa jornada vigente de 40 h: 8,70 →9. No cambian personas ni HH programadas. |
| H05 · Justificaciones RT-16.02/21 | Cerrado | RT-16.02 referencia consola, mae_parametro_version y gob_auditoria. RT-16.21 referencia administración CLIENTE, variables, versionado y elección de canales por cliente. Ambos pasan a Cumple con soporte documental; no se inventa implantación. |
| H06 · Canales y baja comercial | Cerrado documentalmente | SD5 5.1.9 y anexos 5-A–5-C/5-F: CORREO, SMS, WHATSAPP, AVISO_EN_PORTAL comunes a plantilla/preferencia/intento. Preferencia única por cliente/finalidad/categoría/canal; plantilla/versionado acredita contexto inicial y no reinicia baja. Verificación antes de emitir/reintentar; separación OPERACIONAL/COMERCIAL y retención de la decisión. Pedido/entrega son referencias condicionales, sin entrega ficticia para publicidad. RF-17.10 pasa a Cumple. |
| H07 · Rango térmico previo a aprobación | Cerrado documentalmente | SD4 4.1.4.8; SD5 5.1.3/5.1.7 y 5-A–5-C: mae_producto conserva tipo, mínimo/máximo y ficha/versionado; cal_regla_termica conserva copia del origen. PREVENTIVA_FICHA tiene duración cero, severidad CRITICA y aprobador nulo; bloquea, no libera. Parámetro ausente retiene. Distribución local/gateway con acuse. Calidad emite nueva versión APROBADA, conservando excursiones y expediente. RF-01.10/11 siguen parciales por los demás atributos/datos de ubicación faltantes. |
| H08 · Figura sin objeto | Cerrado | Se retiró la leyenda redundante sin imagen y su ancla. El emplazamiento remite a la Figura 14 existente. Renumeradas figuras posteriores y referencias del cuerpo/T-12: 25 figuras, sin huecos ni referencias numéricas discordantes. |
| H09 · Enlaces a figuras PDF | Retirado: formato aceptado por el usuario | El usuario confirmó expresamente que apuntar a los PDF vigentes está bien. Se conservan las trece figuras PDF mediante sus enlaces y las doce imágenes PNG existentes. No se exige generar PNG/SVG ni se mantiene un pendiente por visualización integrada en Markdown. La aceptación del formato no implica una revisión visual que no se haya realizado. |
| H10 · 3.4.2.1 inexistente | Cerrado | Tres citas del cuerpo/anexos pasan a SD3 3.4.2; se conserva referencia al Anexo 3.I donde corresponde. No se agregó sección ficticia. |
| H11 · Índice de anexos | Cerrado | Los 23 enlaces A–W usan anclas explícitas existentes anx:A–anx:V y anx:42A. |
| H12 · Restos de conversión | Cerrado | Los dos residuos del cuerpo ya habían sido retirados por trabajo previo. Se retiraron A.table, 4-W.section y anexo42A.section del anexo. Segunda búsqueda sin resultados. |

«Cerrado documentalmente» significa que la propuesta describe el mecanismo, sus condiciones y su verificación coherentemente; no significa que el sistema ya esté construido o ensayado.

## Segunda revisión y comprobaciones

- T-12: 645 filas, cinco columnas, 645 identificadores únicos. Comparación antes/después: identificadores y descripciones intactos. Parte A: 200 Cumple / 68 parciales / 3 No cumple; Parte B: 242 / 104 / 28.
- Referencias de figura del cuerpo: números coinciden con los objetos/anclas; secuencia 1–25. T-12 cita racks/recinto como Figuras 24 y 25.
- Índice de anexos: 23 destinos existentes. Sin citas 3.4.2.1 ni los cinco residuos originales.
- Diccionario 5-A: canales comunes; aprobación condicional de regla térmica; ficha/origen/versionado presentes. La unicidad de preferencias se propaga a 5-B y 5-F. Las vistas gráficas del SD5 resumen relaciones; el diccionario y las restricciones expresan los atributos/nulabilidad vigentes.
- Erlang C recalculado: 2.000 contactos/mes →90,61 % peak con siete agentes y 84,16 % valle con dos; 2.283 →83,47 %/80,00 %; 2.391 →80,02 % peak, 78,32 % valle con dos y 95,26 % con tres. Confirma límites y refuerzo del mes 25.
- Cantidades de equipos, retenciones, quince actores, decisiones RT recientes, proyección de capacidad y programación de HH conservadas. Cambios propagados a los cuatro resúmenes de SD4/SD5.
- git diff --check sin errores. Todos los archivos creados/editados por esta corrección terminan en .md. No se editaron catálogos originales, LaTeX, PDF ni PNG.

La exclusión y el retorno del primario se contrastaron con la [documentación primaria PostgreSQL 16, §27.3](https://www.postgresql.org/docs/16/warm-standby-failover.html). Esa fuente exige evitar dos primarios y señala que PostgreSQL no proporciona por sí solo la detección/gestión de failover. La propuesta incorpora el procedimiento externo y pruebas; no se declara que VRRP lo resuelva por sí solo.

## Pendientes que impiden afirmar cierre al 100 %

1. **CLIENTE:** resolver formalmente la intervención urgente necesaria durante un congelamiento total. Se mantuvo el conflicto visible y el estado parcial de RT-11.04.
2. **Equipo humano:** completar las 28 revisiones efectivamente realizadas en la declaración del SD4; no se sustituyeron por una revisión de IA.
3. **Aceptación operacional futura:** ejecutar pruebas de conmutación/partición/retorno, restauración, carga y cobertura. Aquí se revisó la documentación y se recalculó la capacidad de mesa; no se ejecutaron ensayos del sistema.

Sin puntaje de Comisión ni acreditación de firmas, revisión humana o aprobación del CLIENTE. Este informe sustituye el listado de hallazgos vigentes de la revisión inicial; sus ubicaciones antiguas ya no describen el árbol corregido.
