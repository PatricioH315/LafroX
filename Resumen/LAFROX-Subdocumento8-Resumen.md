# LafroX — Resumen del Subdocumento 8: Plan de riesgos

[Índice de resúmenes](README.md) · [Documento original](../08_plan_riesgos/LAFROX-Subdocumento8.md)

## Para qué sirve

Identifica qué podría impedir la aceptación o la continuidad de la solución, quién responde y con qué horas y evidencias se trata cada riesgo. Los riesgos son de esta solución: cada uno nombra un componente, sitio, paquete o actor de Puelche. Los problemas ya conocidos se registran aparte, como condiciones de evidencia del Anexo 8.E.

## Cómo se gestionan

[El ciclo de gestión](../08_plan_riesgos/LAFROX-Subdocumento8.md#81-plan-de-riesgos) sigue la norma ISO 31000: identificación, análisis, respuesta y seguimiento. El jefe de proyecto mantiene un registro único y los ocho líderes vigilan cada uno su ámbito (Tabla 8.1). Los disparadores se revisan cada semana, el Comité de Proyecto revisa todos los riesgos cada quince días, los comités Ejecutivo y de Arquitectura deciden cada mes, y desde el mes 13 el Comité de Operación sigue los riesgos de servicio. En marcha blanca el seguimiento es diario.

[Las escalas](../08_plan_riesgos/LAFROX-Subdocumento8.md#813-escalas-previas-al-an%C3%A1lisis) **P, I y D** (probabilidad, impacto y dificultad de detección) van de **1 a 5**. La exposición es **P × I** y se clasifica en baja, moderada, alta (8–14) y crítica (15–25). Para cuantificar, cada nivel de P equivale a un tramo de probabilidad (por ejemplo, 4 = 60 %) y cada nivel de I a una fracción del esfuerzo de los paquetes afectados (por ejemplo, 5 = 30 %).

El **apetito de riesgo** fija una regla de acción por zona. Un riesgo crítico, o con impacto 5, se evita, se mitiga o se escala antes de su hito, aunque su retorno en horas sea bajo. Uno alto se mitiga con un control de la EDT. Uno moderado se acepta activamente, con reserva y disparador, y uno bajo, pasivamente. La **tolerancia** es cero días de atraso en los hitos del Art. 17° y en el despacho de la madrugada, y el **umbral** de escalamiento es todo riesgo crítico o un consumo de reserva mayor que el previsto. Al cierre de cada etapa, una auditoría de riesgos comprueba que el proceso funciona.

## Qué riesgos se identificaron

[El registro](../08_plan_riesgos/LAFROX-Subdocumento8.md#821-rbs-y-an%C3%A1lisis-separados) tiene **32 riesgos**, ordenados en la RBS de la **Figura 8.1** en tres ramas, una por cada análisis que pide el T-22:

- **Solución (13):** emisión de guías en el ERP, reserva de stock, autonomía sin enlace, capacidad, RPO, seguridad, obsolescencia y bloqueo por proveedor.
- **Desarrollo (10):** interfaces sin documentación, productividad y dotación, contrapartes del CLIENTE, conocimiento de rutas, migración y certificación con las cadenas.
- **Implantación (9):** fecha de inicio y congelamientos, marchas blancas, suministros de la sala, adopción, transportistas y sindicato, mesa de ayuda e innovaciones.

Los **siete riesgos que el Caso 02 pide en su capítulo 19** tienen ficha:

| Riesgo del caso | Ficha |
| --- | --- |
| Pérdida del conocimiento de rutas | R8-13 |
| Objeción sindical | R8-21 |
| Rechazo de los conductores de terceros | R8-21 |
| Rotación en bodega | R8-20 |
| Interfaces sin documentación | R8-10 |
| Un solo enlace en Concepción | R8-03 |
| Peak de septiembre durante una fase del proyecto | R8-18 |

El enlace de Concepción lo resuelve el SD4 con tres caminos independientes, y R8-03 lo verifica cortando los tres durante 24 horas. El peak de septiembre cae sobre el cierre de la marcha blanca de la Etapa 2. R8-18 lo trata habilitando todo en agosto y probando la carga a 1,5 veces el peak antes del H11.

## Qué muestra el análisis

**Cualitativo (FMEA).** El número de prioridad **NPR = P × I × D** ordena los riesgos. Los más altos son la caída del ERP o una guía invalidada (R8-01), un ataque a datos críticos (R8-07) y una vida útil insegura estimada por INN-03 (R8-27), con 80. Les sigue la pérdida del sitio por sobre el RPO (R8-05), con 75. R8-05 es poco probable, pero sólo se detecta al ocurrir; por eso se ensaya antes del corte.

**Cuantitativo.** [El valor esperado](../08_plan_riesgos/LAFROX-Subdocumento8.md#823-an%C3%A1lisis-cuantitativo) del registro conjunto suma **29.647,18 HH**, el 15,6 % de las 190.366 HH base del T-15. Dos riesgos concentran el **66,8 %**: la demanda de la mesa de ayuda (R8-22) y la productividad o dotación (R8-11).

La **simulación de Monte Carlo** recorre 5.000 veces las 564 actividades del T-15, con duraciones PERT, la ocurrencia de cada riesgo y nivelación diaria de recursos. En todos los hitos, la fecha P80 queda antes de la fecha límite. El más expuesto es el **H3, con 88,3 %** de entrega a tiempo, por el suministro de la sala (R8-19); le sigue el H8, con 91,1 %. Las ocho entregas se cumplen juntas en el 78,0 % de las iteraciones, y R8-11 es el riesgo que más pesa en el plazo. La preparación del H6 se cumple en el 96,5 % y la del H11 en el 100 %; las seis condiciones de cierre de cada marcha blanca se tratan con R8-18.

## Cómo se responde

Cada ficha del Anexo 8.A fija responsable, estrategia, disparador, plazo, mitigación, contingencia, efecto esperado, riesgo residual, riesgo secundario y evidencia de cierre. Las estrategias son las cinco del PMBOK para amenazas y se eligen según quién controla la causa:

| Estrategia | Riesgos | Por qué |
| --- | --- | --- |
| Mitigar | 28 | LafroX controla la causa |
| Escalar | R8-12 y R8-17 | Dependen de decisiones del CLIENTE |
| Evitar | R8-14 | Separar los equipos de las dos etapas elimina la causa |
| Aceptar activamente | R8-22 | La demanda de la mesa no admite un control previo; hay contingencia y disparador |
| Transferir | Ninguno | Contratar a un tercero no traslada la obligación de LafroX |

Cada respuesta deja un **residual**: con la probabilidad un nivel más baja tras verificar cada control, el registro conjunto baja de 29.647,18 a **23.503,37 HH**. Las respuestas también crean **riesgos secundarios**, anotados en cada ficha; algunos son riesgos propios, como R8-31, que nace de certificar en paralelo a la revisión del CLIENTE.

[El costo-beneficio](../08_plan_riesgos/LAFROX-Subdocumento8.md#831-respuestas-y-costo-beneficio-t%C3%A9cnico) sigue la regla del PMBOK: una respuesta se justifica si reduce el valor esperado más de lo que cuesta. El Anexo 8.C, Tabla C.5, divide el ahorro esperado de cada riesgo crítico por las HH de su paquete de control, ya incluido en el T-15:

- En **3 de 21** el retorno supera 1: la nivelación de recursos frente a R8-11 (17,0) y R8-14 (4,2), y el plan de olas con la certificación de usuarios frente a R8-18 (2,1).
- En los **otros 18** el ahorro medido sólo en HH de retrabajo es menor que el costo, porque ese impacto no incluye la detención del despacho, la sanción sanitaria ni el atraso de un hito. Se aplican igual por la regla del nivel crítico, y la mayoría son pruebas o actas que las Bases exigen.

## Reservas

[La reserva de contingencia](../08_plan_riesgos/LAFROX-Subdocumento8.md#832-reservas-y-cronograma) es el registro conjunto, **29.647,18 HH**. Ningún riesgo coincide con la ventana y los perfiles de la capacidad protegida de la Etapa 1, por lo que no se descuenta nada de ella. El T-15, sección 4.5, refleja la contingencia por período y la compara con la dotación: cabe en todos los roles salvo implantación en los meses 15 y 20, que se cubre con la opción de hasta 8 personas adicionales del contrato de implantación.

La **reserva de cronograma** son las reservas de cada hito del T-15, de 4 a 35 días hábiles, con la fecha P80 antes de la fecha límite. La **reserva de gestión**, de **1.600 HH**, cubre un evento no identificado equivalente a rehacer un módulo de clase D con su integración y certificación; no forma parte de la línea base, la autoriza el Comité Ejecutivo y su valorización va en la Oferta Económica.

## Condiciones antes de declarar la propuesta factible

[El cierre del plan](../08_plan_riesgos/LAFROX-Subdocumento8.md#833-factibilidad-y-aceptaci%C3%B3n) remite al Anexo 8.E, con doce condiciones de evidencia que tienen responsable y hito límite. Las principales:

- **RPO:** el SD4 cumple el RPO ≤ 15 min con tres caminos independientes. La caída de los tres seguida de la destrucción del sitio queda como riesgo residual justificado (SD4, sección 4.3.2.4). R8-05 lo trata con alarmas de replicación a los 5 y 15 min, preemisión de guías y almacenamiento local inalterable, y la conmutación real lo mide antes del H5 y del H10.
- **Coordinación de reserva:** su carga, con cuatro mensajes por línea de pedido (SD4, Anexo 4-I), se verifica en la prueba de concurrencia previa al H4.
- **Proveedor de lácteos:** la suspensión, de marzo a septiembre de 2026, es un antecedente. La consulta V-13 precisa en el mes 1 qué evidencia de trazabilidad restablece la relación.
- **Además:** dotación nominal antes de la línea base, continuidad de los 96 despachos y calidad de atención de la mesa.

Ningún riesgo se da por cerrado con sólo escribir su mitigación: el cierre exige la prueba o el acta indicada.

## Dónde consultar

| Para | Ver |
| --- | --- |
| La lista breve de los 32 riesgos | Formulario T-16 |
| La ficha completa de cada riesgo y el glosario de códigos | Anexo 8.A |
| FMEA y valor esperado en HH | Anexo 8.B |
| Escenarios, costo-beneficio y simulación | Anexo 8.C |
| Reglas de uso de las reservas | Anexo 8.D |
| Condiciones de evidencia actuales | Anexo 8.E |
| Riesgos de adopción de las innovaciones | Anexo 8.F |

**Siguen abiertos:** la revisión humana de la Declaración de uso de IA, la sensibilidad de la Tabla C.4, hoy con 3.000 iteraciones, y la imagen de la Figura 8.1 para el PDF.

---

**Fuente y actualización:** documento local vigente al 8 de octubre de 2026, tras las correcciones de la revisión de la Comisión. Resumen elaborado con asistencia de Codex y Claude Code; no acredita aprobación del CLIENTE ni revisión humana adicional.
