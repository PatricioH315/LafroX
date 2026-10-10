# Revisión de la Comisión — Informe 2 · Subdocumento 9 (v2)

LAFROX · GRUPO 2 · INFORME 2 · Caso 2 · Distribuidora Puelche S.A.

Revisión aplicada con `Revision/prompt_revision_comision_informe2.md` sobre las fuentes Markdown vigentes al 9 de octubre de 2026, después de las ediciones de coherencia en SD1, SD3 (cuerpo, anexos y T-12), SD6, T-14 y T-15. Conforme a la regla del repositorio, la evidencia se cita por archivo y línea o sección. Paginación, índice paginado, folio, firma, tamaño tipográfico, legibilidad de figuras y plantilla quedan pendientes de la compilación del PDF final.

**Archivos recibidos:** `09_plan_calidad/LAFROX-Subdocumento9.md`, `LAFROX-Subdocumento9-Anexos.md`, `LAFROX-Formulario-T-13.md`, `LAFROX-Formulario-T-17.md`. Nomenclatura conforme (Aclaraciones §1). Un formulario por archivo.

**Documentos revisados:** Subdocumento 9 (556 líneas, 10 figuras, 9 tablas en el cuerpo); Anexos (848 líneas); Formulario T-13 (172 líneas); Formulario T-17 (233 líneas). Contrastados contra las cuatro Bases, SD1, SD3 y anexos, T-12, SD6, T-14, T-15 y Anexo 7.

## CORRECCIONES DEL INFORME 1

No aplica: el SD9 no se presentó en el Informe 1. Se verifica en su lugar el estado de los hallazgos de la revisión previa `Revision/revision_comision_informe2_SD9.md`: de 9 pendientes cruzados, 8 están corregidos y 1 queda parcial; la causal §7.1 d sigue abierta.

## 9. PLAN DE CALIDAD — Formularios T-13 y T-17 (8 %)

[9.1 Plan de Calidad · 9.2 Estrategia de Aseguramiento de Calidad · 9.3 Alineación con Plan de Trabajo]

**Revisión: (Puntaje 0)**

**Veredicto.** El subdocumento se tiene por no presentado. Persisten 13 celdas `[[REVISIÓN HUMANA]]` sin completar en las declaraciones de IA: 7 en el cuerpo (líneas 550–556), 4 en los anexos (845–848), 1 en el T-13 (172) y 1 en el T-17 (233). Son cuadros de aprobación en blanco (Aclaraciones §7.1 d) y, desde el Informe 2, dejan el ítem en 0 sin subsanación. Sin esa causal, el contenido alcanzaría 80 en la escala discreta: las armonizaciones cruzadas pedidas ya están aplicadas y quedan sólo faltas menores. El «70» de la revisión anterior no pertenece a la escala del prompt (0, 20, 40, 60, 80, 100).

### Introducción al Plan de calidad

- OK - El texto de introducción va bajo el título y conecta con SD3–SD8, SD13, Anexos 9.A–9.D y los Formularios T-13 y T-17.

### 9.1 Plan de Calidad

- OK - 29 métricas con umbral por característica ISO/IEC 25010 (Anexo 9.A); umbrales de código bloqueantes en la Tabla 9.3: cobertura global ≥ 80 % y lógica ≥ 70 %, ciclomática ≤ 10, cognitiva ≤ 15, duplicación ≤ 3 %.
- OK - 9.1.2 (líneas 91–95): la SCAMPI A vence en noviembre de 2026; la renovación se presenta con el H1 y, mientras no se acredita, rige ISO 9001. SD1, sección 1.4 (línea 205), dice ahora lo mismo y remite a SD9 9.1.2. **Coherente.**
- OK - El costo de la calidad se reproduce: 3.984 + 6.864 = 10.848 HH; fallas 358,4 + 2.956,8 HH; razón 3,3; ninguna cifra en dinero.
- Observación menor: 9.1.2 cita «CMMI Institute, 2018» como modelo, y SD1 cita el informe de evaluación «CMMI Institute, 2023». No hay contradicción, pero las dos fuentes deben distinguirse en Referencias.

### 9.2 Estrategia de Aseguramiento de Calidad

- OK - Recalculo de las pruebas del caso (línea 294): 1,5 × 14,66 = 21,99 TPS; 1,5 × 775,33 = 1.163; 1,5 × 158 = 237; 3 × 14,66 = 43,98; 1,5 × 6,94 = 10,41 TPS.
- OK - Recalculo de casos (líneas 298–302): 56 × 5 + 160 × 3 + 43 × 2 = 846; 846 + 346 + 90 = 1.282; 80 % = 1.026; 1.026 × 0,5 min = 8,55 h, 4,3 h en dos ejecutores. Coincide con el Anexo 9.C, Tabla 9.C.1 (544 + 302 + 346 + 90).
- OK - Anexo 9.C, línea 366: RNF-14.07 se verifica «SAST en G2 y DAST en G4». SD3 Anexo 3.B (línea 313) dice ahora lo mismo; T-12 (línea 237) registra SAST, SCA, DAST y escaneo de imágenes con bloqueo. **Coherente.**
- OK - Las cuatro filas absorbidas (RNF-06.02, 06.03, 11.03, 11.04) se verifican en el Anexo 9.C (líneas 333–347) con la misma fila absorbente que T-12 (líneas 204–218) y SD3 Tabla 3.A.5a (líneas 368–372). **Coherente.**
- Observación: el conteo del SD3 y el del SD9 difieren en la clasificación. SD3 (línea 103) llama «261 requerimientos ofertados» a 175 RF + 86 RNF, y «10 filas de alias o materias absorbidas» a 6 RF + 4 RNF. SD9 (línea 298) prueba 259 «ofertados» y declara «nueve absorbidos». La diferencia se explica: RNF-21.02 y RNF-21.07 están en «No cumple» en el T-12 (líneas 264 y 269), pero el SD3 los cuenta como ofertados, y RF-07.11, también en «No cumple» (T-12, línea 88), entra en las 10 filas del SD3. La aritmética cuadra (175 + 84 = 259; 5 RF + 4 RNF = 9), pero ningún documento escribe esa conciliación. Un evaluador que compare «261» con «259» y «10» con «9» no encuentra la explicación (Aclaraciones §3).
- Errata: Anexo 9.C, línea 130: «de las integraciones. el catálogo suma 1.282 casos. la cifra que usa…». Hay puntos donde corresponden comas y la frase siguiente empieza con minúscula.

### 9.3 Alineación con Plan de Trabajo

- OK - Tabla 9.8 (líneas 483–486): H5 en el mes 12 con certificación hasta el 29-11-2027; H9 en el mes 17 con 3.9.1 hasta el 18-05-2028; H10 en el mes 18. T-14 separa ahora la ejecución del mes del hito: 3.8.7 «Ejecución: mes 10. Hito H5 […]: mes 12»; 3.9.1 meses 16/17; 3.9.6 meses 16–17/18 (T-14, líneas 1275, 1290 y 1295). **Coherente.**
- OK - SD6, línea 48: el refuerzo de evaluadores cubre los meses 9–12 y 16–18, con ejecución en 9, 10, 16 y 17 y subsanación en 11, 12 y 18, igual que SD9 9.3.2 (línea 471). **Coherente.**
- OK - T-15, línea 479: la carga de saldos de Talca (3.7.3) y su segundo ensayo (3.7.4) se ejecutan en diciembre de 2027 sobre Preproducción, sin intervenir Producción; la carga productiva ocurre sólo con el corte 3.7.5 (03-01-2028 a 27-01-2028). Con el mes 1 en febrero de 2027, diciembre de 2027 es el mes 11, que coincide con el «11–11» del T-15 (línea 205). El congelamiento queda resuelto.
- OK - Tabla 9.9 (líneas 514–518) y T-14 8.1.3 y 8.2.2: 6 pruebas de recuperación ante desastres (27…54), 6 de resiliencia (26…55), 3 de intrusión (28, 40, 52) y 36 restauraciones. Separación ≤ 6 meses en cada serie.
- Observación: la resiliencia de los meses 32 y 44 cae en septiembre (septiembre de 2029 y de 2030). La línea 508 dice que el calendario «evitan el congelamiento de septiembre», y la línea 520 que, si se programa en septiembre, se ejecuta fuera del 1 al 25. Ambas frases se pueden cumplir a la vez, pero el plan no dice que esas dos pruebas se hacen entre el 26 y el 30, justo al final del peak de tres semanas (Caso, cap. 13 y línea 54). Falta fijar ese período o mover las pruebas.

### Formularios T-13 y T-17

- OK - T-13: niveles, tipos, ambientes, datos, criterios de entrada y salida, suspensión, roles y calendario de carga, resiliencia, recuperación ante desastres e intrusión. Siglas DES, CAL, IMP, SRE, SEG y DAT definidas.
- OK - T-17: expediente del Art. 18.2, plazos 10 + 10, observaciones con atraso imputable, fichas H1–H12 en los meses del E-25, y H7 y H12 con repetición de intrusión, resiliencia y carga.
- Código sin glosario previo: T-17, línea 134 (ficha H7), usa «resultados R18» antes de la sección 3 (línea 200), donde se definen R18-01 a R18-16. La declaración de IA del T-17 (línea 233) repite «resultados R18». Corresponde al indicio de la Aclaración §7.1, código interno sin glosario en el lugar de uso.

### Consistencia

| Decisión | SD9 | Otro documento | Estado |
| --- | --- | --- | --- |
| Pruebas de intrusión | Anuales por tercero, antes de cada paso y repetidas antes de H7/H12 | SD1 líneas 182–185: semestral como política corporativa que incluye y supera el mínimo contractual anual | OK |
| Renovación CMMI-DEV N3 | Renovación con el H1; mientras tanto, ISO 9001 | SD1 1.4, línea 205 | OK |
| 261 / 271 filas | 645 ID; 259 probados, 9 absorbidos | SD3 línea 103: 261 + 10 = 271 | Parcial (conciliación no escrita) |
| RNF absorbidos | Fila absorbente en el Anexo 9.C | T-12 y SD3 Tabla 3.A.5a con la misma fila | OK |
| RNF-14.07 | SAST G2 y DAST ZAP G4 | SD3 Anexo 3.B y T-12 | OK |
| Meses de hito E-25 | Tabla 9.8 | T-14: ejecución separada del hito | OK |
| Refuerzo de evaluadores | Subsanación en los meses 11, 12 y 18 | SD6, línea 48 | OK |
| Saldos de Talca | — | T-15: Preproducción en diciembre; Producción en el corte de enero | OK |
| Remisión a pruebas y criterios | Anexo 9.C y T-17 | SD3 línea 107 y Anexo 3.J, línea 642 | OK |

### Forma e indicios de uso de IA

- Crítico: 13 celdas `[[REVISIÓN HUMANA]]` vacías (archivos y líneas indicados en el veredicto). Causal §7.1 d: subdocumento en 0.
- Citas a las Bases: 16 de 24 citas «Distribuidora Puelche S.A., 2026…» del cuerpo no indican página (Aclaraciones §6). Se verifica en el PDF; no se inventan páginas.
- Precios: 0 apariciones de «$», «USD», «CLP» o «UF» en los cuatro archivos (Art. 50.2).
- Sin marcadores «TODO», «??», «[INSERTAR», nombres de archivo como fuente ni ruptura de la ficción.

### Qué se espera en el Informe 3

- Un integrante identificado debe firmar las 13 celdas de revisión humana e indicar qué verificó.
- Escribir en SD3 3.2 o en el Anexo 9.C la conciliación 261/259 y 10/9, con RF-07.11, RNF-21.02 y RNF-21.07 en «No cumple».
- Definir R18 antes de la ficha H7 del T-17, o remitir allí a la sección 3.
- Fijar entre el 26 y el 30 de septiembre las resiliencias de los meses 32 y 44, o moverlas fuera de septiembre.
- Corregir la puntuación de la línea 130 del Anexo 9.C y completar las páginas de las citas a las Bases en el PDF.

## Estado de los hallazgos de la revisión anterior

| N.° previo | Hallazgo | Estado |
| --- | --- | --- |
| Causal §7.1 d | 13 celdas de revisión humana | **Abierto** |
| Pendiente 1 | SD1, intrusión semestral | Resuelto (SD1, líneas 182–185) |
| Pendiente 2 | SD3 remite al Anexo 9.C y al T-17 | Resuelto (SD3, línea 107; Anexo 3.J, línea 642) |
| Pendiente 3 | T-12, fila absorbente de RNF-06.02/06.03/11.03/11.04 | Resuelto (T-12, líneas 204–218) |
| Pendiente 4 | SD3, explicar 261 frente a 271 | Resuelto en SD3; parcial respecto del 259/9 del SD9 |
| Pendiente 5 | SD1, renovación CMMI | Resuelto (SD1, línea 205) |
| Pendiente 6 | SD3, RNF-14.07 con G2/G4 | Resuelto (SD3 Anexos, línea 313) |
| Pendiente 7 | T-14, mes de ejecución frente al mes del hito | Resuelto (T-14, líneas 1275, 1290 y 1295) |
| Pendiente 8 | SD6, meses 11, 12 y 18 | Resuelto (SD6, línea 48) |
| Pendiente 9 | T-15, saldos de Talca en diciembre | Resuelto (T-15, línea 479) |
| Citas sin página | Bases sin página | Abierto (pendiente PDF) |

## CONSIDERACIONES TRANSVERSALES

- **Trazabilidad.** La cadena del retiro de lote en menos de 2 h sigue completa: Caso cap. 18 → RF-09.01 → M9 → 3.4.4 → CP-RF-09.01 → JD-07 → R18-01 en H7.
- **Coherencia entre plan, equipo y arquitectura.** Las HH de calidad (10.848) coinciden con el T-15. El refuerzo de evaluadores y su uso por mes son ahora iguales en SD6 y SD9.
- **Fundamentación ingenieril.** Los cálculos de carga, casos, regresión, costo de la calidad y holguras se reproducen sin diferencias.
- **Uso de IA.** La única causal dura vigente son las celdas de revisión humana. El uso de «R18» en el T-17 es menor.
- **Cumplimiento.** No hay precios, plazos fuera del Art. 17° ni archivos mal nominados.

| Ítem | Peso | Puntaje | Ponderado |
| --- | --- | --- | --- |
| 9. Plan de calidad — T-13 y T-17 | 8 % | 0 | 0,0 |
| Diagnóstico de contenido sin la causal §7.1 (no suma) | — | 80 | — |
