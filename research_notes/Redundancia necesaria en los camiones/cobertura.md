# Cobertura conjunta de los camiones

## ¿Móvil e Iridium cubren el problema operativo previsto?

### Takeaway
Sí: la elección de dos operadores móviles más Iridium SBD aborda precisamente las rutas rurales sin red móvil. No es correcto presentar esas zonas rurales como una falla todavía sin solución. Tampoco equivale a cobertura ininterrumpida dentro de cualquier obstrucción física.

### Cited Findings
- El caso informa buena cobertura móvil urbana; cobertura deficiente o nula en Empedrado, Chanco, Cauquenes, Pinto y Alto Biobío; tramos de hasta dos horas sin señal y rutas que solo recuperan cobertura al volver. Esto describe la red móvil del caso, NO una medición de la solución móvil más Iridium. El invierno alarga ese tiempo por rutas más lentas. — [Caso, líneas 283–289, 458 y 1006](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/Bases/Caso_02_Logistica.md).
- El diseño mantiene ambos medios activos: alarmas inmediatas por los dos; curva móvil cada minuto y satelital cada tres minutos; órdenes por ambos. No espera una caída para conmutar a satélite. En las rutas sin móvil, el satélite es un camino normal de operación. — [Diseño canónico, líneas 255–269](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/00/trazabilidad/Solucion_Cadena_de_Frio_en_Ruta.md).
- La tabla vigente de conexiones confirma móvil de dos operadores e Iridium SBD en paralelo, bidireccionales; protección local sin red. — [Conexiones SD4, líneas 27–30 y 47](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/04/partes/4.2_fisica/02_c_conexiones.tex).
- El fabricante ofrece SBD para mensajes cortos bidireccionales, con cobertura global y banda L resistente al clima. Esa descripción de servicio no promete un máximo de interrupción por obstáculo. — [Iridium SBD, apartados de servicio y disponibilidad](https://www.iridium.com/services/iridium-short-burst-data-sbd).
- Iridium exige montaje horizontal del Edge, vista despejada de 360° y preferentemente sobre el activo. Es una exigencia de instalación, no un motivo para duplicar indiscriminadamente equipos. — [Guía original Iridium, página 2, alojada por Teltonika](https://wiki.teltonika-gps.com/images/2/23/IRDM_Iridium_Edge_Quick_Installation_Guide.pdf).

### Inferences
- La formulación correcta es: «el satélite cubre las zonas sin móvil; la vigilancia local cubre los intervalos sin ningún enlace». El supuesto contrario —que una ruta rural sin móvil deja necesariamente horas sin aviso remoto— no está demostrado para este diseño.
- Hay excepciones físicamente posibles además del túnel: un techo opaco a radio, o terreno/vegetación que bloquee las trayectorias disponibles. Para afectar ambos medios debe coincidir además la ausencia de móvil. Son escenarios posibles, no hechos observados ni frecuencias calculadas en Puelche.
- Cambiar a otro satélite puede ayudar ante obstrucción parcial; no atraviesa una obstrucción total. Agregar otro módem de la misma red junto al primero no demuestra por sí solo una solución al túnel.
- La necesidad concreta es verificar instalación y desempeño en ruta. La sola existencia de obstrucciones no justifica un tercer medio remoto ni otra cadena de hardware.

### Gaps
- No hay en lo revisado medición conjunta de los dos operadores e Iridium por tramo real. No se puede afirmar ni que sea insuficiente ni que tenga 100% de cobertura temporal.
- No hay inventario de túneles, detenciones bajo techo, obstrucciones o tiempos máximos reales que permita cuantificar sus frecuencias.

## ¿La espera sería solo de unos minutos?

### Takeaway
Los minutos son la escala prevista para avisar por el satélite cuando hay enlace, y una interrupción breve al pasar un túnel es razonable como escenario. No hay evidencia para garantizar que toda coincidencia de falta de móvil y cielo se resuelva en un número fijo de minutos.

### Cited Findings
- Ground Control explica que se necesita línea de vista; un satélite cruza el cielo en menos de diez minutos y el movimiento posibilita transmitir incluso con vista fuertemente obstruida mediante un diseño apropiado. Con cielo despejado cita aproximadamente una operación de envío/recepción cada diez segundos. Ninguna de esas cifras es una cota universal para recuperar señal. — [Ground Control, About Iridium](https://docs.groundcontrol.com/iot/rockblock/iridium).
- Iridium distingue medición y transmisión; recomienda distribuir los envíos, comprobar resultados y aplicar espera entre reintentos. La guía advierte que insistir sin éxito puede activar bloqueo de acceso de hasta diez minutos. También identifica obstrucción, cambio de satélite y contención como causas de fallo de una sesión. No establece duración máxima de una obstrucción. — [Iridium SBD Best Practices v2, páginas 5 y 11](https://metocean.com/wp-content/uploads/2020/06/DEV_Iridium-SBD_Best-Practices-Guide_NOV17.pdf).
- El plan propone aviso móvil ≤2 min en ≥99% y satelital ≤5 min en ≥95%, sujetos a V2/V18; sin ambos medios sigue la alarma/retención local y se mide cuánto tarda el aviso. — [Anexo físico, línea 424](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/04/anexos/fisica/16_anexo_4b_memoria_calculo.tex).
- La curva se agrupa cada tres minutos; las alarmas tienen envío inmediato y prioridad. No debe confundirse agrupación de curva con espera programada de toda alarma. La antigüedad de curva de hasta 4,5 min es una cota de diseño por demostrar, no la latencia de radio aislada. — [Diseño canónico, líneas 261–277 y 810](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/00/trazabilidad/Solucion_Cadena_de_Frio_en_Ruta.md).
- El propio diseño indica que en túneles la cola sale al primer cielo o señal, y que V18 mide el corte máximo de cielo en quebradas y bosque. La frase genérica «un túnel dura minutos» no sustituye una medición del recorrido ni considera una detención. — [Diseño canónico, líneas 281–286](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/00/trazabilidad/Solucion_Cadena_de_Frio_en_Ruta.md).

### Inferences
- Tres relojes diferentes: (1) adquisición/agrupación de lecturas, (2) sesión y reintentos de transporte, (3) ingestión y aviso a Calidad. El SLA remoto es de extremo a extremo; una transmisión individual rápida no demuestra ese SLA.
- «Iridium se mueve y vuelve en unos minutos» es una expectativa plausible ante obstrucción parcial, NO un máximo garantizado. Tampoco hay base para pintar ausencias prolongadas como habituales.
- El presupuesto de reintentos del componente SBD debe evaluarse en V2/V18 para que el software no cree demoras evitables. La advertencia de bloqueo de diez minutos es una condición de implementación del servicio, no una afirmación de que el diseño actual lo esté sufriendo.

### Gaps
- No hay distribución observada de latencia ni duración de cortes. Los objetivos 99% y 95% no son resultados del piloto.
- No se encontró máximo universal de blackout en las fuentes primarias. La ausencia de esa cota no prueba que las rutas reales tengan cortes fuera del objetivo.

## ¿Qué hace falta validar y qué no justifica agregar redundancia?

### Takeaway
Hace falta ejecutar la aceptación que ya está prevista, no declarar defectuosa la selección móvil más satélite antes de ensayarla. La cobertura física y las fallas dobles de gateway/terminal son problemas distintos.

### Cited Findings
- V2 verifica alarmas, lotes y órdenes por Iridium sin SIM; V18 recorre rutas reales, bosque, quebradas y túneles en verano e invierno, y mide entregabilidad, latencia y corte máximo por tramo; V19 comprueba recepción/aplicación de la orden de Calidad sin móvil. — [Anexo físico, líneas 402, 418–419](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/04/anexos/fisica/16_anexo_4b_memoria_calculo.tex).
- La sección de aceptación dice expresamente que son pruebas propuestas y no resultados ejecutados; banco y piloto tienen alcances específicos. — [Anexo físico, línea 398 y siguientes](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/04/anexos/fisica/16_anexo_4b_memoria_calculo.tex).
- La detección, alarma al conductor y retención local están separadas del aviso remoto. — [Diseño canónico, líneas 244–253](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/00/trazabilidad/Solucion_Cadena_de_Frio_en_Ruta.md).

### Inferences
- Evidencia mínima: medir extremo a extremo, ambos medios activos, identificar tramos por separado, incluir detenciones y zonas parcialmente obstruidas, comprobar comandos de bajada y reenvío tras recuperar conexión. Estos detalles operacionalizan V18; no son prueba ejecutada ni rediseño aprobado.
- Una falla física simultánea del gateway y TC58e no se deduce de que no haya cobertura. A la inversa, duplicar ambos no asegura que un mensaje atraviese un túnel. No usar uno de estos escenarios para justificar hardware contra el otro.
- Si los ensayos cumplen los objetivos, no hay fundamento de cobertura para agregar otro medio. Si no cumplen, se corrige el tramo/procedimiento/instalación o el diseño concreto que falle; no se salta automáticamente a duplicar todo.
- Frase al usuario: «Sí, esa es la idea del móvil más Iridium: que la falta de señal celular no deje la ruta incomunicada. Mi respuesta anterior sobredimensionó el problema. Lo que queda por comprobar es cuánto duran las excepciones físicas de esas rutas, no si cualquier zona rural nos deja sin servicio».
- Frase al usuario: «No necesitamos prometer que ninguna radio pueda perder señal. Necesitamos demostrar que la combinación cumple el aviso comprometido y que el producto sigue protegido durante una interrupción breve».

### Gaps
- Esta revisión no ejecutó radioensayos ni modificó el diseño; no acredita cobertura o SLA.
- No se determina aquí si las reglas de credencial de 14 h cumplen el turno: ese es otro análisis, asignado al investigador de requisitos.
