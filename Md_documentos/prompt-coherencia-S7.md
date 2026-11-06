# Prompt de coherencia para el Subdocumento 7 (S7)

**Uso:** copiá este prompt completo y entregalo junto con la versión vigente de S7 y sus fuentes editables. El objetivo es sincronizar los cruces con S8 sin deteriorar la coherencia interna de la planificación, calendario, recursos, olas, capacitación, reservas o formularios de S7.

## Contexto y límites

- La fuente de referencia vigente de S8 está en `08_plan_riesgos/contenido.tex`, `LAFROX-Subdocumento8-Anexos.tex` (anexos 8.A–8.D) y `LAFROX-Formulario-T-16.tex`.
- El Anexo 8.E fue eliminado. No lo recrees ni lo cites como destino. CI son controles internos, no riesgos transferidos al CLIENTE.
- En este repositorio S7 está disponible como PDF bajo `Datos externos/Informe_2_LafroX/`; no hay fuente LaTeX editable de S7. Los textos extraídos bajo `tmp/` son evidencia histórica/de navegación, no verificación actual.
- Si sólo tenés el PDF, no lo edites ni fabriques fuente. Pedí la fuente editable o entregá instrucciones de reemplazo acotadas, con documento, sección, página y texto.
- Verificá fechas, páginas, valores e IDs contra las versiones vigentes. S8 orienta la clasificación de riesgos; no autoriza cambiar compromisos ni supuestos contractuales de S7.
- No edites S8, S4, S9, T-14/T-15/T-18 fuera de la fuente propia de S7 ni otros documentos. Señalá dependencias externas como pendientes.

## Prompt

> Actuá como editor técnico del Subdocumento 7 (planificación y despliegue). Alineá sus dependencias con el registro vigente de S8 preservando la coherencia interna de EDT, calendario, recursos, olas, capacitación, marcha blanca, reservas y formularios.
>
> Leé íntegramente S7, sus anexos, el cronograma y los Formularios T-14, T-15 y T-18 asociados. Contrastá con `08_plan_riesgos/contenido.tex`, `LAFROX-Subdocumento8-Anexos.tex` (en particular 8.A.2 y 8.D) y `LAFROX-Formulario-T-16.tex`. Verificá cada mes, hito, cifra y referencia en las versiones actuales; no uses extractos de `tmp/` como prueba actual.
>
> ### Cruces que tenés que resolver
>
> 1. **Conocimiento del planificador — R-016.** Conservá la transferencia de conocimiento prevista en meses 1–3 y la confirmación del retiro mediante V-14 en mes 1, sin inventar una fecha de jubilación. Alineá la prueba de que el equipo pueda aplicar rutas y excepciones sin el planificador durante la marcha blanca de meses 13–15 con EDT, responsables, capacitación, aceptación y calendario. No dupliques el mismo evento en otro riesgo.
> 2. **Rotación de preparación nocturna — B-S7-01 / R-042.** S8 trata el 38 % como tasa anual de rotación, **no** como probabilidad. El evento es que las altas superen la capacidad de tutoría/evaluación o trabajen personas no preparadas. Contrastá §7.1.2.7, Figura 7.15, T-14 §7.1.2 y T-15: programa meses 13–56, turno 22:00–06:00, aprendizaje máximo de dos horas, tutor y evaluación antes del trabajo autónomo. Conservá IMP hasta mes 21 y SRE desde mes 22, con las contrapartes operativas previstas. Diferenciá R-042 de R-017 (inasistencia) y R-015 (adopción); no vuelvas a contabilizar las 2.816 HH ordinarias de capacitación como contingencia de riesgo.
> 3. **Innovación y ventana del piloto.** Mantené separados el paquete 3.10.1.4 de meses 11–15, certificación H5 de meses 11–12 y piloto con locales reales de meses 13–15. No cambies el piloto a meses 11–12 ni describas su calendario como resultado logrado.
> 4. **Peak de septiembre y cierre E2 — R-044.** Alineá el supuesto de inicio contractual/calendario con la ventana de septiembre y cierre E2 en meses 19–20. R-044 abarca coordinación y recuperación del cierre ante peak/congelamiento; la demostración técnica de capacidad es control interno CI-047, no la dupliques en R-044. Si las fechas dependen del inicio real, mantenelas condicionadas e identificá quién debe confirmarlas. No inventes fechas contractuales.
> 5. **Capacidad, concurrencia y reservas.** Revisá picos de meses 13–15 y 19–20, olas, dependencias y nivelado de recursos dentro de S7 y formularios. S8 informa 1.183,11 HH de exposición esperada de 35 riesgos; 689,67 HH de los diez mayores son subconjunto, no una reserva adicional. Las 1.600 HH de reserva de gestión siguen separadas y sin conciliación resuelta; no fusiones, sumes ni redefinas las 3.072 HH protegidas de S7 sin derivación verificable. No declares capacidad, holgura, presupuesto o financiación demostrados sin evidencia. Las cuatro semanas finales de evidencia de cada marcha blanca no son holgura consumible.
>
> ### Coherencia interna y cierre
>
> Actualizá en conjunto calendario, EDT, cargas por perfil, hitos, dependencias, capacitación, marcha blanca y formularios asociados donde corresponda. Revisá referencias inversas y cálculos afectados por cambios de fechas/duraciones. No alteres requisitos del CLIENTE para acomodar estimaciones ni dupliques el mismo evento. Ante datos contradictorios o no verificables, documentá la discrepancia y pedí decisión; no inventes.
>
> Al finalizar, entregá una matriz `cruce S8 | ubicación en S7/formulario | calendario antes/después | cambio | verificación interna | evidencia/pending`. Enumerá comprobaciones de precedencia, fechas, totales, responsabilidades y referencias, más las decisiones pendientes. Diferenciá objetivos propuestos de compromisos aceptados. Si no hay fuente editable, no modifiques PDFs: entregá instrucciones precisas y pedí los archivos fuente.

## Criterio de finalización

- Fechas, hitos, cargas, dependencias y formularios no se contradicen dentro de S7.
- R-042 y R-044 están delimitados sin duplicar R-015/R-017/CI-047.
- Las reservas y horas de riesgo se distinguen de la capacidad/financiación aprobadas.
- Las pruebas propuestas no se presentan como evidencia de ejecución.