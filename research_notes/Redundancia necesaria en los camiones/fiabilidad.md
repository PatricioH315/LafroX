# Fiabilidad y proporcionalidad de la redundancia

## ¿Es estrictamente necesario agregar una tercera cadena y duplicar el terminal?

### Takeaway
**No se deriva una necesidad técnica automática de los escenarios revisados.** La propuesta de tercera cadena, repuesto en cada camión y cable alternativo fue prematura: debe justificarse frente a la función que se debe conservar, el tiempo de reposición tolerable y los resultados de pruebas. Un componente susceptible de averiarse no demuestra por sí solo un defecto arquitectónico.

### Cited Findings
- La fuente canónica exige explícitamente evitar sobreingeniería y que cada componente cubra una necesidad no cubierta por otro; seleccionó TC58e más sensor independiente como segunda cadena. [Fuente canónica, líneas 75–98](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/00/trazabilidad/Solucion_Cadena_de_Frio_en_Ruta.md:75).
- La alternativa de alarma independiente y transmisor adicional de v8 se descartó expresamente por duplicar la función del TC58e y su sensor independiente; no fue un olvido documental. [Fuente canónica, líneas 585–593](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/00/trazabilidad/Solucion_Cadena_de_Frio_en_Ruta.md:585).
- El objetivo de diseño es evitar una entrega posiblemente comprometida ante una falla simple, no garantizar operación normal ante cualquier avería doble. El terminal muerto impide registrar entregas hasta usar reserva. La doble falla independiente está fuera de la cobertura declarada. [Fuente canónica, líneas 631–644](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/00/trazabilidad/Solucion_Cadena_de_Frio_en_Ruta.md:631).
- La definición técnica de tolerancia a fallas se refiere a conservar una función especificada ante un número y tipo especificados de fallas; no equivale a infalibilidad universal. [NASA, Systems Engineering Handbook, líneas web 703–711](https://www.nasa.gov/reference/system-engineering-handbook-appendix/).
- El análisis FMEA debe fijar previamente el alcance y nivel de tolerancia, identificar consecuencias y compensaciones, y considerar el impacto de modificaciones. Esta metodología no prescribe que todo fallo concebible exija otro equipo. [NASA, Software FMEA, secciones Ground Rules y Process Introduction](https://swehb.nasa.gov/pages/viewpage.action?pageId=72024565). Es referencia metodológica, **no requisito contractual aplicable a camiones**.
- Existe reserva del 10 % de equipos de reparto: 96+10 inicialmente y 110+11 al año 3; el documento no establece un terminal extra por cada camión. [Implementos, línea 24](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/04/partes/4.2_fisica/04_c_implementos.tex:24).

### Inferences
- **TC58e:** sí es una dependencia de disponibilidad de la función de entrega digital. Su avería no apaga la vigilancia térmica del gateway. Llamarlo simplemente «punto único de falla de la solución» exagera el alcance.
- Un repuesto a bordo puede acortar la interrupción, pero no es automáticamente obligatorio: su necesidad depende del plazo de restauración comprometido, distancias, acceso a reservas y efecto real de detener nuevas entregas de frío. No confundir reserva existente con reposición instantánea.
- **Wi-Fi:** un fallo del enlace es una dependencia de disponibilidad para obtener estado fresco antes de la siguiente bajada, pero la respuesta diseñada es conservadora: no autorizar una nueva entrega sin estado fiable. Cable alternativo puede mejorar disponibilidad, no es requisito obvio de seguridad ni obligación deducible de que Ethernet exista como accesorio.
- **Tercera cadena:** solo debería elevarse a necesidad si se exige explícitamente conservar evaluación/alarma o entrega normal después de dos fallas independientes, o el análisis/pruebas revela un riesgo inaceptable que no cubran controles y reposición actuales. No recomiendo regresar a v8 con la evidencia actual.

### Gaps
- La investigación contractual del otro frente debe determinar si hay un objetivo concreto de restauración aplicable al terminal en ruta o exigencia de operación sin interrupción bajo avería física. Sin ese objetivo no se puede declarar obligatorio ni suficiente un repuesto por camión.
- No hay resultados físicos de aceptación que permitan afirmar ya satisfecha la respuesta a cada avería. La garantía canónica es de diseño a demostrar.

## ¿Son fallas de probabilidad baja? ¿Qué independencia existe realmente?

### Takeaway
**No hay tasas del caso que permitan etiquetarlas como bajas ni altas.** La distinción útil ahora es entre avería común de un dispositivo, pérdida de una función, operación degradada y fallo de causa común; la severidad y recuperación importan además de la frecuencia.

### Cited Findings
- El TC58e tiene batería propia de 7.000 mAh y cargador de vehículo; el kit alimenta gateway e Iridium desde su propia UPS, mientras sensor independiente y termógrafo usan baterías internas. Son defensas contra una pérdida simple de alimentación, no una demostración de independencia absoluta. [Implementos, línea 44](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/04/partes/4.2_fisica/04_c_implementos.tex:44); [Canónico, líneas 216–220](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/00/trazabilidad/Solucion_Cadena_de_Frio_en_Ruta.md:216).
- Gateway y terminal evalúan la misma regla con implementaciones distintas; el terminal usa sensor y termógrafo independientes y retiene por contradicción. [Canónico, líneas 222–238](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/00/trazabilidad/Solucion_Cadena_de_Frio_en_Ruta.md:222).
- La redundancia solo obtiene todo su beneficio probabilístico bajo independencia; controles, energía, ubicación y vulnerabilidades compartidas pueden producir fallas de causa común. Más unidades idénticas no eliminan ese límite. [NASA NTRS, Common Cause Failures Dominate and Defeat Redundancy](https://ntrs.nasa.gov/citations/20240013667). **No transferir al caso los porcentajes genéricos citados por esa publicación.**
- El criterio de interpretación técnica debe separar falla de un componente, consecuencia funcional, detección, compensación y efectos de una corrección. [NASA, Software FMEA](https://swehb.nasa.gov/pages/viewpage.action?pageId=72024565).

### Inferences
- No se puede multiplicar dos probabilidades desconocidas ni decir «como son dos equipos, sería casi imposible». Tampoco se puede elevar la doble falla a prioridad principal sin datos.
- Un error común en umbral/regla aprobada no se corrige añadiendo una tercera copia de la misma regla; deben validarse parámetros y casos límite. Implementaciones distintas reducen algunos errores comunes de código, no una especificación errónea compartida.
- Una caída de alimentación del gateway que también derriba su Wi-Fi y el módem no son tres fallas independientes: son efectos del mismo dominio de fallo. La batería del TC58e y los registradores aporta separación funcional importante.
- Daño físico a cabina, perturbación eléctrica más allá de protección, fallo común de mantenimiento o despliegue son escenarios para revisar separación y contención; no están demostrados ni cuantificados aquí como frecuentes.
- Un repuesto sin carga, credenciales, manifiesto/retenciones actuales y procedimiento de recuperación puede no restaurar servicio. Más hardware también agrega configuración, mantenimiento, fallas latentes, interfaces y pruebas. Esa complejidad debe justificarse, no darse por gratuita.

### Gaps
- No se encontraron en las fuentes locales revisadas MTBF, tasas por viaje de avería de TC58e/Wi-Fi/gateway, tiempo real de reparación ni datos de fallas simultáneas.
- Especificaciones IP, resistencia a caída y batería son condiciones de diseño/aceptación, no una probabilidad de fallo del sistema integrado.

## ¿Qué pasa concretamente en cada escenario y qué decisión corresponde?

### Takeaway
La respuesta proporcionada es mantener el diseño actual mientras se comprueba el cumplimiento de sus contingencias y aceptación; no añadir automáticamente otra cadena por una avería doble hipotética. **Debe corregirse el lenguaje anterior: dos equipos apagados no equivalen a autorizar una entrega insegura.**

### Cited Findings
- El gateway mantiene vigilancia mientras el conductor se aleja con el terminal. El terminal puede completar una entrega ya habilitada fuera del Wi-Fi; debe recobrar un latido válido antes de otra bajada. [Canónico, líneas 224–238](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/00/trazabilidad/Solucion_Cadena_de_Frio_en_Ruta.md:224).
- Las pruebas previstas incluyen gateway muerto, lectura congelada, contradicción de sensores, POD fuera del Wi-Fi, reposición/reinicio de terminal sin internet, arranque/corte de batería y recuperación de comunicaciones. [Canónico, V5–V14, líneas 773–782](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/00/trazabilidad/Solucion_Cadena_de_Frio_en_Ruta.md:773).
- El bloqueo es informático, no una cerradura física. Ignorarlo manualmente tiene controles operacionales documentados; no puede resolverse afirmando que digitalmente se impide abrir la caja. [Canónico, líneas 639–644](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/00/trazabilidad/Solucion_Cadena_de_Frio_en_Ruta.md:639).
- Hay chequeo previo de sensores, gateway, satélite, UPS, manifiesto y reglas, además de salida degradada ante gateway no disponible. [Canónico, líneas 363–373](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/00/trazabilidad/Solucion_Cadena_de_Frio_en_Ruta.md:363). La salida degradada no equivale a mismas prestaciones; debe cotejarse su coherencia con los requisitos del frente contractual.

### Inferences

| Escenario | Protección/evidencia local | Disponibilidad de entrega digital | Contingencia prevista | ¿Nueva redundancia estrictamente justificada? |
|---|---|---|---|---|
| TC58e muerto | Gateway sigue evaluando y alarmando; registradores siguen | No puede habilitar/registrar nuevas entregas desde el terminal muerto | Reserva y recuperación de estado local | No automáticamente; comprobar tiempo de reposición aceptable |
| Wi-Fi averiado con gateway sano | Gateway sigue evaluando; terminal conserva lectura Bluetooth independiente | Completa lo ya habilitado; nuevas bajadas de frío esperan estado fiable | NO CONFIABLE, restituir enlace antes de nueva autorización | Cable solo si la necesidad de disponibilidad lo exige o las pruebas justifican |
| Conductor fuera del alcance en entrega normal | Gateway vigila; terminal conserva entrega habilitada | Entrega en curso se completa | Resincro al volver, antes de siguiente bajada | No es una avería ni motivo de añadir red |
| Gateway apagado, TC58e sano | Detecta falta de latido; conserva sensor independiente y evidencia | Retiene frío, no continúa como si nada | NO CONFIABLE y procedimiento de recuperación | Segunda cadena ya existente; no se demuestra necesidad de tercera |
| Gateway y TC58e apagados | Sensores/termógrafo pueden conservar registro por batería, **no consta evaluación/alarma activa independiente** | No hay terminal operativo que autorice o registre POD | No hacer entrega de frío sin comprobación; restituir equipo y reconciliar evidencia | No se infiere obligación de tolerar dos fallas; revisar solo contra requisito explícito o riesgo inaceptable |
| Umbral/regla común incorrecto | Ambas cadenas podrían coincidir en decisión equivocada | Podría aparentar normalidad | Validación de regla y mapeo con Calidad; casos negativos | Una tercera copia no lo soluciona; prioridad es validación |
| Falla de UPS del kit con TC58e y registradores cargados | Se pierde gateway/satélite, permanece la cadena portátil | Retención conservadora al perder latido | V5/V6, repuesto/reparación | Revisar aislamiento y prueba existente, no sumar equipos sin análisis |

**Veredicto:** no sostener la propuesta anterior de rediseño obligatorio. La conclusión correcta es «la avería del terminal o Wi-Fi puede interrumpir una función y está contemplada con respuesta segura; no basta ese hecho para exigir duplicación adicional». Lo necesario es acreditar el comportamiento y tener una contingencia de reposición compatible con el servicio comprometido. No hay evidencia para afirmar infalibilidad ni probabilidad baja, y tampoco para afirmar que las prestaciones ya estén ensayadas.

### Gaps
- Las pruebas son especificaciones, no resultados ejecutados. La tabla describe diseño e inferencia de sus dependencias, no mediciones.
- La matriz no determina por sí sola cumplimiento de disponibilidad global/por ruta: requiere denominador y objetivo contractual correctos, además de tiempos reales de recuperación.
