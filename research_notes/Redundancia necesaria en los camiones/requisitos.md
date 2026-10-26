# Requisitos y contingencias de camiones

## Qué redundancia se exige y qué no se puede dar por necesaria

### Takeaway
No se encontró una exigencia expresa de tolerar dos fallas independientes simultáneas gateway–TC58e, instalar un segundo terminal en cada camión ni agregar un canal cableado de respaldo al Wi-Fi. Sí se exigen contingencias justificadas, repuestos, reposición, autonomía sin cobertura y niveles de servicio medidos; la posibilidad genérica de que un equipo falle no demuestra por sí sola que haya que duplicarlo.

### Cited Findings
- RT-02.11 obliga a declarar los puntos únicos de falla subsistentes y justificar por qué son aceptables; no impone eliminarlos todos. RT-02.09 requiere degradación elegante al caer componentes no críticos. RT-02.04 exige ADR con alternativas y criterio. [Bases Técnicas Transversales, líneas 152–159](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/Bases/Bases_Tecnicas_Transversales.md:152).
- La redundancia explícita de RT-08.03 corresponde a conmutadores de núcleo, cortafuegos y balanceadores, no menciona terminales de mano. RT-03.14 exige redundancia de equipos on-premise críticos, y RT-08.04 contiene una exigencia amplia de alimentación redundante; ninguna de estas cláusulas describe una tolerancia arbitraria a dos equipos de camión fallando simultáneamente. [RT-03.14, línea 209](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/Bases/Bases_Tecnicas_Transversales.md:209); [RT-08.03/04, líneas 461–462](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/Bases/Bases_Tecnicas_Transversales.md:461).
- Para dispositivos de terreno, las Bases exigen adecuación a humedad, vibración, autonomía y caídas; además ciclo de vida, disponibilidad de repuestos y plan de reposición durante los 56 meses. [RT-08.10–14, líneas 480–484](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/Bases/Bases_Tecnicas_Transversales.md:480).
- La exigencia de stock de terreno es 10 % del parque, precargado y disponible en sitio; no es un terminal extra en cada camión (que equivaldría a una política mucho mayor). El stock de componentes críticos es al menos 10 % disponible en Chile. [Bases Técnicas Transversales §8.4, líneas 494–496](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/Bases/Bases_Tecnicas_Transversales.md:494).
- El diseño activo sigue esa reserva: 96 terminales de reparto + 10 repuestos inicialmente; 110 + 11 en el año 3. No consta reserva individual a bordo de los 96 camiones. [SD4 implementos, línea 24](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/04/partes/4.2_fisica/04_c_implementos.tex:24); [memoria de cálculo, línea 158](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/04/anexos/fisica/16_anexo_4b_memoria_calculo.tex:158).
- La solución canónica declara explícitamente el TC58e + sensor independiente como segunda cadena y evita transmisor/alarma adicionales. La garantía propuesta se limita a que una sola falla del kit no permita entregar producto posiblemente comprometido; no cubre dos fallas independientes simultáneas ni destrucción del camión. [Solución canónica, líneas 77–101](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/00/trazabilidad/Solucion_Cadena_de_Frio_en_Ruta.md:77); [línea 489](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/00/trazabilidad/Solucion_Cadena_de_Frio_en_Ruta.md:489); [líneas 633–645](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/00/trazabilidad/Solucion_Cadena_de_Frio_en_Ruta.md:633).
- La revisión académica previa objeta equipos duplicados sin sustento (aproximadamente 200 impresoras/POS para 96 camiones) y apilamiento de redundancia no justificado en almacenamiento; no pide una tercera cadena de vigilancia de camión. [Revisión del informe, líneas 353–356](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/Bases/Revision_informe.md:353); [línea 376](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/Bases/Revision_informe.md:376).

### Inferences
- La necesidad de un segundo terminal a bordo tendría que justificarse por tiempos de restauración, exposición real de la ruta y consecuencias, no por el enunciado tautológico «un terminal puede averiarse».
- Tampoco basta decir «es improbable»: no se han aportado tasas de avería, tiempos de recuperación por ruta ni análisis de causas comunes que permitan cuantificar esa afirmación.
- No encontrar una obligación de tercera cadena no acredita el cumplimiento de todas las obligaciones existentes. Se puede recomendar no sobredimensionar y, a la vez, exigir que se pruebe la contingencia prevista.

### Gaps
- No se localizaron tasas observadas de falla del TC58e o del Wi-Fi de cabina que permitan calificarlas numéricamente como bajas.
- No consta en las fuentes examinadas un protocolo de logística de repuestos hacia un camión concreto en una ruta rural con tiempos medidos. Que no esté un repuesto en cada vehículo no equivale automáticamente a incumplimiento; sí impide presumir recuperación inmediata.

## Qué SLA se aplica realmente y qué alcance tiene

### Takeaway
No es correcto aplicar automáticamente «99,9 % y cero interrupción» a cada dispositivo o a todo momento de una ruta. Las Bases miden servicios de negocio; el SD4 activo clasifica entrega/POD y registro térmico como Alto (99,5 %, resolución 8 h), mientras preparación/despacho y su identidad de bodega son Crítico (99,9 %, resolución 4 h). Las obligaciones de reposición del hardware son una capa distinta.

### Cited Findings
- RT-10.01 exige 99,9 % mensual para servicios clasificados como críticos, medido sobre la transacción de negocio de extremo a extremo; RT-10.02 obliga a clasificar y justificar por impacto. No define un denominador por camión, ruta o terminal, ni autoriza esconder una ruta averiada en un promedio de los otros 95. [Bases Técnicas Transversales, líneas 551–552](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/Bases/Bases_Tecnicas_Transversales.md:551).
- Artículo 78.2 fija los niveles de servicio: Crítico 99,9 % / respuesta 15 min / resolución 4 h; Alto 99,5 % / respuesta 1 h / resolución 8 h. El MTTR crítico mensual es además ≤4 h. [Bases Administrativas, líneas 1158–1173](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/Bases/Bases%20Administrativas.md:1158).
- La clasificación activa del SD4 es explícita: Crítico = preparación/despacho con guía por cambio de carga, bloqueo térmico e identidad de bodega; Alto = entrega y evidencia, planificación, cobranza y registro de temperatura, entre otros. El texto explica que 99,9 % penalizable recae en preparación/despacho e identidad. [SD4 despliegue, líneas 375–400](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/04/partes/4.2_fisica/11_j_despliegue.tex:375).
- El documento canónico de frío dice genéricamente «plataforma de extremo a extremo ≥99,9 % mensual (SD4)», pero ello no sustituye ni amplía silenciosamente la clasificación detallada activa. [Solución canónica, línea 808](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/00/trazabilidad/Solucion_Cadena_de_Frio_en_Ruta.md:808).
- Separadamente, §8.4 exige hardware crítico con soporte24×7 y resolución4h; reemplazo de componente crítico máximo4h desde confirmación de diagnóstico. Hardware no crítico resolución24h hábiles. [Bases Técnicas Transversales, líneas 491–496](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/Bases/Bases_Tecnicas_Transversales.md:491).
- La indisponibilidad cero del caso se refiere a despacho05:30–07:00, no a todo el reparto07:00–19:00 o hasta20:00. [Caso logístico, líneas 568–570](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/Bases/Caso_02_Logistica.md:568); [RT-10.05 del caso, línea741](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/Bases/Caso_02_Logistica.md:741).

### Inferences
- «Se avería un terminal y hay que reemplazarlo» describe una incidencia de hardware y un procedimiento de restauración, no prueba de caída total de la solución.
- La clasificación Alto no permite dejar el reparto sin contingencia; tampoco obliga por sí sola a que cada terminal tenga failover instantáneo o reserva a bordo.
- La fórmula, población, ventana y exclusiones de medición deben quedar explícitas antes de derivar suficiencia de repuestos o tiempo admisible por ruta. No hay fundamento para convertir un SLA de plataforma en garantía física de cobertura o inmunidad total del dispositivo.

### Gaps
- No se encuentra en lo examinado una métrica completa que determine si la disponibilidad de entrega se pondera por terminal, ruta, transacción o ventana; no se concluye cumplimiento ni se valida agregar denominadores.
- El registro térmico Alto y el bloqueo previo de despacho Crítico son funciones/ventanas distintas: hace falta preservar esa distinción al redactar, sin rebajar seguridad alimentaria.

## Wi-Fi local, operación sin cobertura y credenciales

### Takeaway
La pérdida normal de alcance al entrar al local del cliente ya está contemplada; no es la misma condición que una avería de la radio local. La obligación de funcionar sin señal se refiere a cobertura/enlace remoto y no prohíbe usar comunicación local entre sensores, gateway y terminal. La credencial de14h frente a una jornada dimensionada14,5h es una cuestión determinista de autonomía que debe revisarse, no una razón para agregar una tercera cadena aleatoria.

### Cited Findings
- El caso exige un turno completo de14h sin cobertura, registrando íntegramente la jornada; la sincronización al volver no debe superar10min. También reconoce rutas donde la señal móvil vuelve solo al regresar. [Caso logístico, líneas570 y731–732](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/Bases/Caso_02_Logistica.md:570).
- El RT-03.10 transversal se expresa como pérdida total del enlace con la nube; RT-03.11 exige registro local sin pérdida. [Bases Técnicas Transversales, líneas205–208](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/Bases/Bases_Tecnicas_Transversales.md:205).
- La solución canónica usa Wi-Fi local para el latido del gateway y Bluetooth directo para registradores; dice expresamente que no necesitan internet. Al alejarse tras escanear una bajada, no alarma por pérdida de latido; al regresar exige estado actualizado antes de habilitar otra bajada. [Solución canónica, líneas224–238](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/00/trazabilidad/Solucion_Cadena_de_Frio_en_Ruta.md:224).
- V9 prueba entrega y POD fuera del alcance Wi-Fi: «se entrega lo habilitado; no se habilita nada con un latido vencido». V14 prueba terminal reiniciado/reemplazado sin internet y exige recuperar el estado del gateway antes de entregar. [Anexo4-W, líneas409 y414](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/04/anexos/fisica/16_anexo_4b_memoria_calculo.tex:409).
- Si el Wi-Fi sí está averiado, el diseño pasa a NO CONFIABLE y no habilita nueva bajada de frío; no se afirma que el gateway deje de medir ni que falle toda la operación. [Solución canónica, línea502](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/00/trazabilidad/Solucion_Cadena_de_Frio_en_Ruta.md:502).
- El texto activo exige renovar credencial a las12h por IP; SBD no renueva y vencer a las14h impide operaciones protegidas nuevas. El mismo SD4 dimensiona una ruta hasta14,5h (05:30–20:00). [Funciones offline, línea24](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/04/partes/4.1_logica/16_funciones_disponibles_y_no_disponibles_sin_conexion.tex:24); [implementos, línea44](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/04/partes/4.2_fisica/04_c_implementos.tex:44).
- Las V1–V21 se declaran como aceptación propuesta, no resultados ejecutados. V18 mide por tramo la duración de cortes y latencias; las metas móviles≤2min/99% y satelitales≤5min/95% se sujetan a prueba y se declara ausencia de cota remota sin ambos caminos. [Anexo4-W, líneas398,418 y424](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/04/anexos/fisica/16_anexo_4b_memoria_calculo.tex:398).

### Inferences
- No hay contradicción intrínseca entre «operación sin cobertura móvil/internet» y «se usa LAN local»: no se exige que la radio Wi-Fi esté físicamente averiada durante todo el turno. La expresión coloquial «sin ninguna red» debe precisarse para evitar esa confusión.
- La necesidad de cable redundante se decide después de demostrar comportamiento de Wi-Fi, recuperación y efecto real sobre servicio; el contrato no lo exige expresamente. No confundir que un accesorio Ethernet exista comercialmente con una necesidad arquitectónica acreditada.
- La autonomía de sesión exige alinear vigencia/capacidad del turno y recuperación segura; no se arregla duplicando hardware ni confiando en SBD como si fuera conectividadIP. Este punto merece tratamiento puntual pero no cambia el veredicto sobre necesidad de tercera cadena.

### Gaps
- Las fuentes revisadas no acreditan ejecución física de V9,V14,V18 ni máximo observado por ruta; no llamar «validado» lo que solo tiene protocolo.
- No se concluye que la vigencia14h viole automáticamente el mínimo14h; sí hay una tensión con la jornada14,5h y la captura de jornada íntegra que debe alinearse expresamente.
