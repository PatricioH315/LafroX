# Análisis cuantitativo focalizado de los diez mayores valores esperados

## Objetivo
Ampliar la subsección de análisis cuantitativo de SD8 con una tabla e interpretación de los diez riesgos que más contribuyen al valor esperado de esfuerzo.

## Decisiones
- Seleccionar y ordenar por valor esperado descendente: `VE_i = p₀_i × HH_condicional_i`, con HH redondeado/formateado exactamente como en Anexo 8.B.
- La selección cuantitativa es distinta de la selección cualitativa por qP×qI; no describir los diez como de mayor zona cualitativa.
- Mostrar ID, evento/consecuencia resumidos desde T-16, p₀, impacto condicional en HH y VE en HH.
- No confundir contribución de riesgo individual con una reserva separada; total de 2.058,480 HH se explica en el texto existente. Sin Monte Carlo ni percentiles.
- No presentar CSV externo como cita oficial SD8; usar Anexo 8.B/T-16 como datos reproducidos en los entregables.

## Alcance y resguardos
- Editar solo `08_plan_riesgos/contenido.tex`, subsección `Análisis cuantitativo`.
- Preservar cambios previos locales y la tabla íntegra de Anexo 8.B.
- No tocar PDF, Anexo 8.B, T-16 ni otros documentos; no crear commit.

## Tareas
1. [done] Añadir una tabla con descripción breve, p₀, HH condicional y VE para los diez riesgos con mayor valor esperado, preservando exactamente la fórmula y los datos vigentes.
2. [done] Añadir interpretación de los principales impulsores, empates y contribución acumulada; dejar claro que son valores esperados, no simulación ni clase cualitativa.
3. [done] Verificar orden, valores, cobertura y consistencia textual; ejecutar `git diff --check`. No compilar si hay riesgo de sobrescribir PDFs.

## Evidencia
- Anexo 8.B, líneas 82–127, contiene p₀, HH condicional y VE de 45 IDs; total VE 2.058,480 HH.
- T-16, líneas 28–72, contiene los enunciados de riesgo actuales.
- Ranking preliminar descendente de VE: R-030 (116,000), R-004 (100,800), R-003/R-026 (80,640), R-012/R-015 (70,560), R-001/R-021/R-038 (68,400), R-018 (67,680). Suma preliminar top 10: 792,080 HH (≈38,5% del total).
- Verificación independiente: los diez valores y el orden coinciden con Anexo 8.B; recálculo suma 792,080 HH = aproximadamente 38,5% de 2.058,480 HH; resúmenes cotejados con T-16 y `git diff --check` pasó.
- Notación de VE y subtotal usa coma decimal, consistente con el resto del documento.
- La modificación es documental; test funcional RED no aplica. No se compiló ni generó PDF.
