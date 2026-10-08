# LafroX — Resumen del Subdocumento 8: Plan de riesgos

[Índice de resúmenes](README.md) · [Documento original](../08_plan_riesgos/LAFROX-Subdocumento8.md)

## Para qué sirve

Identifica qué podría impedir la aceptación o la continuidad de la solución, quién responde y qué recursos o evidencias se necesitan. Separa riesgos futuros de problemas y dependencias ya conocidos.

## Cómo se gestionan y priorizan

[El ciclo de gestión](../08_plan_riesgos/LAFROX-Subdocumento8.md#81-plan-de-riesgos) sigue identificación, análisis, respuesta y seguimiento. El jefe de proyecto mantiene el registro; los líderes revisan disparadores y los comités deciden tratamiento y escalamiento. El cierre técnico exige evidencia; la aceptación contractual sigue siendo del CLIENTE.

Las escalas **P/I/D** son probabilidad, impacto y dificultad de detección, de **1 a 5**. La exposición es **P × I**; FMEA —análisis de modos de falla y efectos— agrega detección para calcular **NPR = P × I × D**. Estas puntuaciones ordenan prioridades; no son porcentajes de probabilidad del proyecto. El apetito de riesgo fija qué nivel exige tratamiento y escalamiento y cuál se acepta con seguimiento; ningún riesgo de un requisito obligatorio se acepta sin tratamiento.

## Los principales resultados

[El registro](../08_plan_riesgos/LAFROX-Subdocumento8.md#82-identificaci%C3%B3n-y-an%C3%A1lisis-de-riesgos) contiene **32 riesgos**: 13 de solución, 10 de desarrollo y 9 de implantación, dibujados en la RBS de la Figura 8.1. Los siete riesgos que pide el Caso 19 tienen ficha. La prioridad se concentra en despacho, reserva de stock, emisión ERP, frío, seguridad, dotación y aceptación de marchas blancas.

El valor esperado total es **15.076 HH**. Cinco riesgos concentran **67,7 %**: productividad/dotación, atención de mesa, aceptación de marcha blanca, uso indebido de reserva E1 y doble reserva de stock. Un valor esperado combina probabilidad y esfuerzo; no es una factura cierta ni una bolsa que deba sumarse nuevamente a cada escenario.

La simulación documentada usa **5.000 iteraciones** del cronograma. Sus resultados dependen de duraciones, probabilidades y calendario supuestos; no prueban cumplimiento contractual. H6, H7, H11 y H12 no se simulan como entregables equivalentes al resto, y la duración de marcha blanca/operación no queda cubierta por la misma red.

## Reservas y respuesta

[La contingencia](../08_plan_riesgos/LAFROX-Subdocumento8.md#832-reservas-y-cronograma) distingue las **3.072 HH protegidas de E1**, ya incluidas en T-15, de las adicionales. Solo **1.853 HH** de exposición de R8-02/R8-04/R8-14 pueden absorberse allí; por eso el SD8 calcula **13.223 HH adicionales**. No se usa esa capacidad antes del mes 13 ni se presta a E2.

Cada ficha define disparador, responsable, mitigación, contingencia, plazo y evidencia. Los costos monetarios corresponden a la oferta económica; aquí se comparan horas: el costo-beneficio de cada riesgo crítico divide el retrabajo evitado por las HH de su control (Anexo 8.C, Tabla C.5).

## Dónde consultar y qué sigue abierto

T-16 ofrece la tabla breve; 8.A contiene fichas, 8.B prioridades y HH, 8.C escenarios/simulación, 8.D reservas, 8.E condiciones actuales y 8.F innovaciones.

El SD4 cumple el **RPO ≤ 15 min** con tres caminos independientes; el riesgo residual de perder los tres enlaces y luego el sitio, que el SD4 declara y mitiga (4.3.2.4), se trata en R8-05 y se mide en la conmutación real antes del H5 y el H10. Deben comprobarse dotación, revisión contractual, continuidad de 96 despachos y calidad de atención. Ningún riesgo tiene cierre acreditado por la sola redacción de su mitigación.

---

**Fuente y actualización:** documento local vigente al 8 de octubre de 2026. Resumen elaborado con asistencia de Codex; no acredita aprobación del CLIENTE ni revisión humana adicional.
