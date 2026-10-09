# LAFROX · GRUPO 2 · INFORME 2 · Caso 2 · Distribuidora Puelche S.A.

**Revisión de la Comisión Evaluadora sobre fuentes Markdown — SD8 y su cronograma (SD6, SD7, T-14, T-15).** Sexta corrida de `Revision/prompt_revision_comision_informe2.md`, después de pasar el cronograma a paquetes con planificación gradual, de bajar el tope a 40 desarrolladores y de incluir la mesa con tres agentes en el plan base. Contrasta con las Bases, con las clases (FEP02 y FEP04) y con el PMBOK 6, caps. 6 y 11, y se pregunta otra vez si lo que se propone tiene sentido. La evidencia se cita por archivo y sección.

---

## Dictamen

**Ítem 8 — Puntaje 0/100 (peso 10 %).** La causal sigue siendo la del §7.1 d / §7.2: 18 celdas `[[REVISIÓN HUMANA]]` en el SD8, sus anexos y el T-16. También hay celdas sin revisar en las secciones editadas del SD6 (5), el SD7 (11), el Anexo 7 (3), el T-14 (3), el T-15 (4) y el T-18 (1).

**Diagnóstico de contenido sin §7.1: 80/100.** El cronograma ya no muestra precisión falsa:
- La Tabla 6.1 tiene 163 paquetes y la 6.1b detalla actividades sólo hasta el H2, con planificación gradual según PMBOK, cap. 6, p. 185.
- La contingencia baja a 19.448,58 HH (9,4 %).
- El pico de desarrollo baja a 40 simultáneos (29 equivalentes).
- Todo cuadra entre el SD8, el T-15, el SD7 y los resúmenes.

No sube a 100 por las preguntas de las secciones 2 y 3.

## 1. Lo que quedó bien
- **T-15 «a modo de resumen»** (BA, Formulario T-15): HH por paquete y etapa, curvas, personas, Tabla 6.1 por paquete y Figura T15.3 de planificación gradual. Coherente con el RUP del SD6 6.2.
- **Regla 8/80 aplicada al paquete** (FEP02) y tabla de clases de tamaño con ejemplos (T-15 §4.1).
- **Cifras coherentes:** la Tabla 4.2 suma 206.312 HH, igual que los 163 paquetes de la Tabla 6.1; la curva 4.4 suma 218.720 HH y cuadra por etapa con la §4.3. Sin cifras antiguas en los entregables.
- **Hitos dentro de su límite:** los P80 de los ocho hitos quedan antes de su fecha (Tabla 5.2 = Tabla 8.5 = Tabla C.3); los ocho juntos se cumplen en el 77,8 %.
- **Reservas reflejadas en el plan** (T-15 §4.5). El modelo de `compct/` reproduce las tablas a partir de los archivos del repositorio.

## 2. Preguntas que siguen abiertas (contenido)

**P1. ¿El H4 entrega la Etapa 1 completa?** La prueba de integración 3.8.1 corre del 1 al 20 de octubre de 2027, pero tres integraciones de la Etapa 1 terminan durante esa prueba o después:

| Integración | Termina |
| --- | --- |
| 3.6.2 Pasarela de pago | 06-10-2027 |
| 3.6.3 Mapas y geocodificación | 15-10-2027 |
| 3.6.4 Avisos al cliente | 15-10-2027 |
| 3.6.1 Trazabilidad con proveedores | 10-11-2027, después de la entrega del H4 |

Antes del cambio, 3.6.2–3.6.4 terminaban en agosto o septiembre; la nivelación con 40 desarrolladores las retrasó. El Formulario E-25 define el H4 como el «software de la Etapa 1 para pruebas, con QA superado», y M4 Rutas depende de la geocodificación. **Esto es una regresión del cambio**: hay que ponerle a 3.8.1 la predecesora de 3.6.2–3.6.4 (o declarar qué se prueba con simuladores) y adelantar esas integraciones dentro de la capacidad de 40. Para 3.6.1, explicar que se integra en el H5 o adelantarla.

**P2. ¿Los módulos duran lo que parecen?** En la Tabla 6.1, varios módulos de 960 HH ocupan de 8 a 15 semanas: 3.4.4, 3.4.9 y 3.4.10 van del 14-06 al 24-09-2027, con un máximo de 12 personas. Es el efecto de empezar el análisis en junio y construir cuando hay capacidad. Para un evaluador se lee como equipos que entran y salen. **Sugerencia:** fijar el inicio de cada módulo cerca de su construcción, o explicar en el T-15 §5.1 que el análisis y el diseño de contratos se adelantan a propósito para que la base compartida y los contratos de interfaz se cierren antes de construir.

**P3. ¿Hace falta el tercer agente de la mesa desde el mes 21?** El SD4 (4-W.7 y tabla de proyecciones) estima 2.000 contactos al mes al inicio y 2.258 en el año 3; los dos agentes cubren hasta 2.283. Programarlo desde el mes 21 agrega 15.946 HH durante 36 meses, aunque los dos primeros años la demanda quede bajo el límite. Es prudente, pero el Caso penaliza el sobredimensionamiento tanto como el subdimensionamiento. **Alternativas:** programarlo desde el mes 33 (año 3), cuando la proyección llega a 2.258, o mantenerlo y justificar con una frase que el margen protege el nivel de servicio en los peaks y ante la incertidumbre de una demanda que todavía no se mide.

**P4. ¿P = 3 es coherente para R8-22?** La ficha justifica P = 3 con un margen del 19,6 % (2.391 frente a 2.000), pero el SD4 proyecta 2.258 en el año 3, un margen de sólo 5,9 %. Con la proyección del propio SD4, P = 4 parece más defendible: cambiaría la exposición a 12 y la contingencia en unas 375 HH. Hay que alinear la justificación con la proyección del año 3.

**P5. ¿Es suficiente la reserva del H8?** Cuatro días hábiles y 91,1 % de entrega a tiempo. Depende de la revisión anticipada del borrador (R8-12, T-15 §5.5). Está tratada, pero es el hito más frágil después del H3: conviene que el Comité de Proyecto lo siga como hito con vigilancia especial.

**P6. ¿Se deduce bien la «Personas (máx.)» de la Tabla 6.1?** En los módulos aparece 12, un valor que se da sólo en las actividades de equipo completo. El lector puede leer «12 personas durante 8 a 15 semanas», que serían 3.000 a 5.000 HH, contra las 960 del paquete. Agregar una nota que explique que es el máximo simultáneo y no la dotación permanente, o mostrar en su lugar las personas promedio.

**P7. ¿Las predecesoras de la Tabla 6.1 se pueden leer?** Los módulos listan más de 15 predecesoras (2.4.1, 2.6.2, 3.1.1–3.1.5, 3.3.x…). Es correcto, pero denso. El Anexo 7.B ya las resume por cuenta (D-04, D-05, D-14 a D-19); conviene mostrar en la tabla la dependencia del Anexo 7.B (por ejemplo, «D-04, D-05, D-15») en vez de la lista completa.

## 3. Contraste con las Bases
- **Art. 17° y E-25:** meses y producciones sin cambios (5-05-2028 y 5-10-2028, días permitidos). Si se acepta la P1, el H4 mantiene su contenido.
- **Art. 18.3:** las reservas del H1 y el H8 son menores que el plazo de subsanación; la respuesta está en R8-12 y en el T-15 §5.5. OK.
- **Formulario T-15 «a modo de resumen»:** cumple.
- **Aclaraciones §11, cap. 8:** cumple los títulos e incluye reservas y su reflejo en el cronograma.
- **Caso cap. 6.1 (proporción):** ver P3.

## 4. Diagramas
- Fig_7-7 (barra 3.4 desde el 10-06), Fig_T14-2 (3.4 y 3.6), Fig_7-8 (nota de planificación gradual) y la nueva Fig_T15-3 son coherentes con la Tabla 6.1.
- **Si se acepta la P1**, hay que corregir las barras de 3.6 en las Fig_T14-2 y Fig_7-7. Falta la revisión visual en draw.io.

## Qué se espera
1. Resolver la P1 (H4 con integraciones completas) y volver a nivelar y simular.
2. Decidir la P3 y alinear la P4.
3. Ajustar la presentación de la Tabla 6.1 (P2, P6 y P7).
4. Completar las revisiones humanas.

| Ítem | Peso | Puntaje | Ponderado |
| --- | --- | --- | --- |
| 8. Plan de riesgos — T-16 | 10 % | **0** | **0,0** |

Contenido sin la causal del §7.1: **80/100**.
