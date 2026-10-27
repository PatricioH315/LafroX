# SD9 actualizado desde las fuentes rectoras

**Criterio del usuario:** los otros subdocumentos se toman como fuente de verdad. Las ocho observaciones se tratan como errores internos de actualización del SD9; no se modifican otros capítulos para resolverlas.

## Cambios aplicados

| Hallazgo interno | Corrección en SD9 y asociados |
|---|---|
| I-01, alcance por etapa | H4/H5 verifican las interfaces aplicables a E1; H9/H10 completan las quince con E2 y regresión E1. AL-CLI-01 se asigna al portal construido en E2; AL-STOCK-01 y AL-ACT-01 amplían allí su alcance. |
| I-02, regresión completa | Se distinguen la parte automática y manual. Ambas aportan la evidencia completa aplicable; una ejecución automática nocturna no acredita por sí sola toda la regresión ni las personas para la parte manual. |
| I-03, excepciones | Ninguna persona o comité levanta una puerta fallida ni relaja una exigencia contractual. Las propuestas prospectivas de controles adicionales siguen el control de cambios. |
| I-04, conteos | Se toman del SD3/T-12 los 270 RF/RNF (64 críticos, 163 altos, 43 medios), los 324 RT cumplidos, 28 parciales y 22 no cumplidos, y nueve filas absorbidas/alias sin doble cómputo. |
| I-05, matriz | T-13, sección 8.2, publica una matriz individual prevista de los 644 requisitos y los nueve alias del T-12, además de quince contratos. SD9, sección 9.2.5, es su índice y remisión explícita; Anexo 9.D mantiene el tramo de los dieciséis resultados del caso. |
| I-06, evaluadores | El máximo de dieciséis evaluadores se cita a T-15, sección 7.5.7, Tabla 7.9. No se atribuye al SD6 un compromiso que no está allí; asignaciones y capacidad neta se confirman conforme a T-15. |
| I-07, CMMI | Se usa la evaluación Benchmark n.º 58190 y el régimen de renovación/acreditación declarado por SD1. |
| I-08, cobertura | Se mantienen los controles compatibles: 70 % de lógica de negocio, 80 % global y 80 % de líneas modificadas, sin intercambiar denominadores. El cuerpo distingue ocho métricas bloqueantes; los 42 identificadores 9A se conservan, con los dos controles del 80 % dentro de 9A-31. |

## Cifras actualizadas

- Casos únicos previstos: **1.352** = 64×5 + 163×3 + 43×2 + 352 + 15×7.
- Reparto de planificación: **1.082 automáticos + 270 manuales**.
- Parte automática: **9,02 horas de ejecutor**, aproximadamente 9,0; con dos ejecutores independientes, 4,51, aproximadamente 4,5.
- Parte manual: **67,5 HH por ciclo**. Dieciséis evaluadores exclusivos requerirían al menos diecisiete tandas de quince minutos, 4,25 horas transcurridas; ese máximo no acredita un cuadrante disponible.
- Falla interna: **95,5 HH**; externa: **111,5 HH**; una de cada tipo: **207 HH**, solo como escenario de planificación.
- Conformidad programada: se conservan **12.016 HH** = 4.224 + 7.792 y la base de **220.023 HH** del T-15. No se agregan reservas o HH al proyecto sin autorización. El escenario con dos fallas adicionales sería 12.223 HH únicamente si el retrabajo no está ya imputado.

## Qué acredita la matriz

La matriz contiene identificadores de requisito, prioridad, etapa, estado del T-12, criterio de origen, paquete y casos previstos. El JSON asociado conserva también el criterio y el componente recibidos de las fuentes. Los identificadores de caso son estables por requisito (`RF-09.01/P01`, por ejemplo); los cinco escenarios críticos, tres altos y dos medios siguen la regla de diseño propuesta por el plan, con el detalle ejecutable en H1.

**No acredita pruebas ejecutadas ni cumplimiento nuevo.** Los 22 RT no cumplidos siguen visibles sin casos y los 28 parciales no se convierten en cumplimientos completos. Los nueve alias no generan casos adicionales. El alcance de INT-08 se acepta en E2 conforme a SD7; las demás interfaces de E1 se regresan en E2. Las cinco colisiones RF-14.01–RF-14.05 conservan el sufijo `-BTT` del T-12, pero citan el identificador realmente impreso en la tabla fuente del SD3.

## Fuentes y reproducción

- SD3/T-12: `33508bb3`.
- SD1: `d03bf324`.
- SD6/T-10: `2c88458a`; el cuerpo actualizado ya usa cobertura global, mientras T-10 conserva la de líneas modificadas. Se mantienen ambas en SD9.
- SD7/T-14/T-15/T-18: `c193bfe4`.
- SD4: `708b0a38`.

Desde la raíz:

```powershell
python SD9_v_nueva/revision/generar_matriz_pruebas.py
python SD9_v_nueva/revision/verificar_matriz_pruebas.py
python SD9_v_nueva/revision/verificar_alineacion_sd7.py origin/LafroX-Subdoc7-LateX
```

Las comprobaciones validan 653 identificadores fuente, estados, prioridades, ausencia de duplicados de casos, sus sumas y escenarios, y las 25 filas de campañas/diez hitos sincronizados con T-15. No sustituyen la ejecución del plan, la revisión humana ni las actas del CLIENTE.

Los informes de revisión anteriores se conservan como evidencia histórica y remiten a esta actualización; no son una lista vigente de cambios pendientes en otros capítulos. Las fuentes, PDF y diagramas actualizados se verifican antes de su entrega. No se crea commit ni se publica automáticamente.

## Verificación de presentación

La matriz individual se divide en trece bloques de hasta cincuenta filas para evitar el límite de dimensiones de TeX. El rótulo de bloque forma parte de la cabecera repetida, no queda aislado al pie de una página. El verificador distingue las cifras del catálogo de los parámetros de diseño (por ejemplo, `hsize=1.316`).

## Resultado de validación

- Cuatro documentos compilados con LuaLaTeX, tres pasadas satisfactorias cada uno, sin referencias indefinidas ni desbordamientos en los registros finales.
- PDF actualizados: cuerpo, 35 páginas; anexos, 21; T-13, 76; T-17, 16. El crecimiento del T-13 corresponde a la matriz individual explícita.
- Revisión visual de las cifras, controles de cobertura, matriz (inicio, centro y final), contratos y protocolos por etapa; figuras 9.1, 9.2 y 9.4 verificadas.
- Verificadores de catálogo y de alineación T-15 satisfactorios; los 21 archivos controlados fuera del SD9 conservan su hash anterior.
- El usuario confirmó la revisión humana de los cambios actuales y que se mantiene la declaración existente. Se retiró el estado pendiente de la declaración IA; no se certifican pruebas ejecutadas. Commit autorizado exclusivamente para los archivos del SD9, sin push.
