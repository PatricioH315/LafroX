# Formulario T-18: Propuesta de implantación y puesta en marcha controlada

Este formulario presenta la propuesta de implantación y puesta en marcha controlada que exige el Formulario T-18 de las Bases Administrativas. Cubre por separado la Etapa 1 (marcha blanca de los meses 13 a 15 y producción desde el mes 16) y la Etapa 2 (marcha blanca de los meses 19 y 20 y producción desde el mes 21), el plan de convivencia entre ambas y el procedimiento de reversión. El Subdocumento 7, sección 7.3, resume y analiza esta propuesta.

La propuesta aplica las siete condiciones que el Caso 02 impone a toda estrategia de puesta en producción (sección 13.3), responde los nueve puntos de la sección 17.6 y cumple los requisitos RT-20.01 a RT-20.08 de las Bases Técnicas Transversales. La secuencia de olas, el criterio de avance, la dotación de estabilización y la medición de la adopción son los declarados en el Capítulo 3, sección 3.4.4. La estrategia técnica de despliegue es la de la arquitectura del Capítulo 4, sección 4.1.8, y los paquetes de trabajo citados son los de la EDT del Formulario T-14.

## 1 Reglas comunes de implantación

Las dos etapas siguen las mismas ocho reglas, y cada una responde a una condición del caso o de las Bases:

1. **Convivencia antes del cambio.** Nada entra en producción sin haber convivido con la forma actual de trabajar durante su marcha blanca, con conciliación diaria y posibilidad de volver atrás (Caso 02, sección 13.3, condición 1; RT-20.03).
2. **Fechas prohibidas.** Ningún paso a producción, inicio de ola, corte de datos ni despliegue con impacto en la facturación o en el inventario valorizado ocurre en septiembre, en diciembre ni en los tres primeros días hábiles de un mes (sección 13.3, condición 2; RT-10.05 del caso). Durante el congelamiento total (1 al 25 de septiembre y todo diciembre) no se despliegan cambios.
3. **Olas, no un evento único.** El despliegue avanza por proceso, por sitio y por zona comercial, y nunca afecta a la vez a la bodega, la preventa, el reparto y la facturación (condición 3; RT-20.01).
4. **Ventana de despacho protegida.** No se despliega durante la ventana de 05:30 a 07:00, que no admite indisponibilidad (RT-10.05 del caso). Las intervenciones en bodega se programan y acompañan en el turno de noche, de 22:00 a 06:00 (condición 4).
5. **Despliegue azul-verde con interruptores de funcionalidad.** Cada capacidad nueva se publica en un entorno paralelo y se habilita por sitio y por ola mediante interruptores de funcionalidad, de modo que la reversión técnica consiste en volver a la versión anterior sin reinstalar. Cada operación tiene un único escritor autorizado: no se habilita doble escritura de stock, cobros ni guías de despacho (Capítulo 4, sección 4.1.8 y Tabla 4.1).
6. **Reversión en dos niveles.** El nivel técnico vuelve a la versión anterior de la solución mediante azul-verde o el interruptor de funcionalidad. El operacional vuelve al procedimiento manual con la hoja de picking y la guía en papel; lo ordena el responsable de operaciones del CLIENTE y debe completarse antes de las 05:30. Los registros capturados permanecen en cola y se concilian al retomar (Capítulo 3, sección 3.4.4; RT-20.02).
7. **Estabilización declarada.** Cada paso a producción tiene una estabilización de cuatro semanas por ola, con la dotación declarada en la sección 2.6 y sin costo adicional (condición 7; RT-20.05 y RT-20.06).
8. **Definición de terminado y aceptación.** Ningún entregable de implantación se da por terminado sin código, pruebas, documentación, seguridad y despliegue verificados (RT-20.07). Cada hito se acepta con un protocolo de criterios objetivos y verificables, firmado por la Contraparte Técnica (RT-20.08; Bases Administrativas, Art. 18.1).

## 2 Etapa 1: marcha blanca de los meses 13 a 15 y producción desde el mes 16

La Etapa 1 pone en producción la mayor parte del alcance y concentra doce de los dieciséis resultados de aceptación del caso; por eso su implantación se describe con más detalle que la de la Etapa 2.

### 2.1 Alcance y olas

La Etapa 1 pone en producción la trazabilidad de recepción, la bodega con FEFO y la preparación nocturna, la cadena de frío, la preventa sin conexión, la planificación de rutas, el reparto con prueba de entrega digital, las devoluciones y envases, la rendición y los indicadores operacionales: los módulos M1 a M10 y M12 (paquetes 3.4.1 a 3.4.11 del Formulario T-14). La implantación sigue el orden de las dependencias de datos en tres olas (Capítulo 3, sección 3.4.4; paquete 4.1.1), como presenta la tabla «Olas de implantación de la Etapa 1» (Fuente: Capítulo 3, sección 3.4.4):

| Ola | Procesos y módulos | Avance | Registro oficial al cerrar la ola |
|---|---|---|---|
| 1 | Datos maestros y recepción con lote y vencimiento (M1) | Por sitio | La solución, para recepciones y lotes |
| 2 | Inventario por ubicación y lote con FEFO (M2) y preparación en turno de noche (M5) | Por sitio | La solución, para stock y preparación |
| 3 | Preventa (M3), rutas (M4), reparto (M6), devoluciones y envases (M8) y rendición (M7) | Por zona comercial | La solución, para pedidos, entregas y cobros |

El calendario de las olas está restringido por las Bases. La marcha blanca dura tres meses, unas 13 semanas ($3 \times 52 / 12$). Cada ola necesita cuatro semanas consecutivas cumpliendo su criterio antes de retirar el papel (Capítulo 3, sección 3.4.4), y el Art. 17.3 exige que toda la Etapa 1 opere a volumen real durante las últimas cuatro semanas del período, las semanas 10 a 13. Si las olas fueran estrictamente secuenciales (ola 1 en las semanas 1 a 4 y ola 2 en las 5 a 8), la ola 3 empezaría en la semana 9 y tendría que entrar en todas sus zonas a la vez, lo que contradice el avance zona por zona. Por eso la ola 3 empieza antes de que termine el período de criterio de la ola 2, adelantándose en lo que dure su escalonamiento por zonas, y ambas olas no intervienen el mismo proceso al mismo tiempo, para cumplir la regla 3. La siguiente descripción textual representa la Figura T-18.1, «Olas de la Etapa 1 durante la marcha blanca» (Fuente: elaboración propia a partir del Capítulo 3, sección 3.4.4):

- Eje temporal: semanas 1–13, distribuidas en mes 13 (semanas 1 a 5,33), mes 14 (5,33 a 9,67) y mes 15 (9,67 a 13). H6 está al inicio, en la semana 1; mes 16 (H7) está después de la semana 13.
- Una franja destaca las semanas 10 a 13: toda la Etapa 1 debe operar a volumen real (Art. 17.3).
- Ola 1, recepción con lote (M1; avance por sitio): cuatro semanas en criterio desde la semana 1 hasta la 5; después, la solución es el registro oficial y se retira el papel.
- Ola 2, inventario y preparación (M2 y M5; avance por sitio): cuatro semanas en criterio desde la semana 5 hasta la 9; después, la solución es el registro oficial.
- Ola 3, preventa a rendición (M3, M4, M6, M8 y M7; por zona): entrada escalonada zona por zona entre las semanas 6 y 10; todas las zonas desde la semana 10 hasta la 14 (continuación representada hasta el límite de mes 16). Los comienzos de entrada por zona no tienen fecha fija.
- Los hitos de decisión de avance para las olas 1 y 2 están en las semanas 5 y 9, respectivamente.

La figura muestra que las olas 1 y 2 ocupan las primeras ocho semanas en cumplir su criterio y que la ola 3 entra por zonas antes de la semana 10, de modo que toda la Etapa 1 opere a volumen real en las cuatro semanas de cierre.

### 2.2 Pruebas previas a la marcha blanca y al paso a producción

Antes de cada paso a producción se aprueban las pruebas del numeral 20.1 de las Bases Técnicas Transversales, y su cumplimiento forma parte de la certificación de la Etapa 1 (H5, mes 12; paquete 3.8.7). La tabla «Pruebas previas a la marcha blanca de la Etapa 1» (Fuente: Bases Técnicas Transversales, numeral 20.1, y Formulario T-14) presenta cada prueba con su criterio de éxito:

| Prueba | Criterio de éxito | Paquete |
|---|---|---|
| Integración, regresión e idempotencia | Todos los flujos de integración sin error y batería de regresión sin regresiones | 3.8.1 (H4) |
| Aceptación de usuario y accesibilidad | Casos aprobados y firmados por la Contraparte Técnica; conformidad WCAG 2.2 AA | 3.8.2 |
| Perfil operacional | 14 horas sin señal en terreno y 24 horas sin enlace en el CD, sin pérdidas ni duplicados; uso a −22 °C con guantes | 3.8.3 |
| Carga, estrés y resiliencia | Umbrales del capítulo 9 de las Bases Técnicas Transversales y del RT-09.01 del caso cumplidos a 1,5 veces el peak de septiembre; degradación controlada y recuperación sin intervención | 3.8.4 |
| Recuperación ante desastres | RTO de 4 h o menos y RPO de 15 min o menos en conmutación real (Capítulo 3, Tabla 3.5) | 3.8.5 |
| Seguridad ofensiva | Sin hallazgos críticos ni altos abiertos | 3.8.6 |
| Migración de datos | Dos ensayos previos y conciliación sin diferencias no explicadas | 3.7.1 a 3.7.5 |
| Despliegue sin interrupción | Despliegue azul-verde y reversión ensayados en Preproducción | 3.8.8 y 4.1.2 |

Las pruebas cubren los tres riesgos que el caso hace críticos: la operación sin señal, el peak de septiembre y la recuperación ante desastres. La reversión operacional se ensaya además en Preproducción antes de cada corte (Capítulo 3, sección 3.4.4).

### 2.3 Convivencia con la operación vigente y conciliación diaria

Mientras dura la marcha blanca, la solución convive con la forma actual de trabajar: en bodega, con la hoja de picking impresa; en ruta, con la guía en papel; y en Talca, con el WMS de 2013 en solo lectura como respaldo de consulta hasta el cierre de la marcha blanca del sitio (supuesto S-14). En cada ola se declara cuál es el registro oficial.

Cada día se concilian ambos registros por dominio: documentos, lotes, stock, entregas y cobros. Toda diferencia se clasifica y se explica antes del cierre del día. El papel se retira en cada ola cuando cumple su criterio durante cuatro semanas consecutivas a volumen real (Capítulo 3, sección 3.4.4; RT-20.03; paquete 4.2.1).

### 2.4 Indicadores diarios y umbrales de cierre

La segunda condición del Art. 17.3 exige alcanzar «el volumen de operación real comprometido en el plan de implantación» durante al menos las cuatro últimas semanas. LafroX compromete la operación real completa de cada proceso de la ola, no una muestra ni un grupo piloto. La tabla «Volumen de operación real comprometido en la marcha blanca de la Etapa 1» (Fuente: Caso 02, sección 14.1) expresa ese volumen con las cifras del caso:

| Proceso | Ola | Mes normal | Peak de septiembre |
|---|---:|---:|---:|
| Recepciones de proveedor | 1 | ≈ 1.150 al mes | No informado por el caso |
| Líneas de preparación de pedidos | 2 | ≈ 260.000 al mes | No informado por el caso |
| Visitas de preventa | 3 | ≈ 62.000 al mes | No informado por el caso |
| Pedidos | 3 | ≈ 31.000 al mes | No informado por el caso |
| Entregas | 3 | ≈ 1.400 por día hábil | ≈ 2.600 por día hábil |
| Documentos tributarios emitidos por el ERP | 3 | ≈ 34.000 al mes | No informado por el caso |
| Cobros en efectivo | 3 | ≈ 11.800 al mes | No informado por el caso |
| Devoluciones | 3 | ≈ 900 al mes | No informado por el caso |

El compromiso es que el 100 % del volumen de cada proceso se registre en la solución durante las cuatro últimas semanas, con los demás indicadores en su umbral. Si esas semanas coinciden con un peak, el volumen comprometido es el del peak. Una ola que cubre una sola zona compromete el volumen de esa zona hasta que entran las demás; al cierre de la marcha blanca, todas las zonas están dentro.

Los indicadores se miden y publican cada día con el umbral que exige el Art. 17.3 para cerrar la marcha blanca (RT-20.04), como presenta la tabla «Indicadores diarios y umbrales de cierre de la Etapa 1» (Fuente: Bases Administrativas, Art. 17.3; Caso 02, RT-09.01 y RT-10.05; y Capítulo 3, Tabla 3.5):

| Indicador diario | Umbral | Condición del Art. 17.3 |
|---|---|---|
| Incidentes críticos y altos abiertos atribuibles a la solución | 0 | Primera |
| Transacciones de la ola registradas en la solución sobre el total | 100 % del volumen de la tabla anterior, sostenido durante las últimas 4 semanas | Segunda |
| Indisponibilidad en la ventana de despacho de 05:30 a 07:00 | 0 minutos (RT-10.05 del caso) | Tercera |
| Disponibilidad de la transacción crítica, de extremo a extremo | 99,9 % o más (Capítulo 3, Tabla 3.5) | Tercera |
| Tiempo de respuesta de las transacciones críticas, percentil 95 | Confirmación de línea de preparación hasta 1 s; registro de entrega hasta 2 s; línea de preventa hasta 1,5 s; consulta de stock y crédito hasta 2 s (RT-09.01 del caso) | Tercera |
| Diferencias de conciliación sin explicar | 0 | Cuarta |
| Usuarios de la ola certificados en su perfil | 100 % | Quinta |
| Pedidos perdidos o duplicados por falta de señal | 0 (R18-06) | Cuarta |

La sexta condición es el acta de aceptación firmada por la Contraparte Técnica (paquete 4.2.3, H7). Los resultados del capítulo 18 del caso que se verifican en esta marcha blanca (R18-01 a R18-03, R18-05 a R18-10 y R18-14 a R18-16) se miden con el método y el período del Capítulo 3, Anexo 3.J. La siguiente descripción textual corresponde a la Figura T-18.2, «Ciclo diario de la marcha blanca y condiciones de cierre del Art. 17.3» (Fuente: elaboración propia a partir de las Bases Administrativas, Art. 17.3, y del RT-20.04):

- El ciclo diario forma un circuito: medición de los indicadores del día → comparación con el umbral → decisión de continuar, corregir o revertir → conciliación y publicación del día → nueva medición. En el centro: «Marcha blanca E1 y E2».
- Al cumplirse las seis condiciones copulativas se cierra la marcha blanca. Las condiciones son: (1) sin incidentes críticos ni altos, 0 abiertos; (2) volumen real durante las cuatro últimas semanas, 100 % del volumen comprometido; (3) disponibilidad y desempeño, 0 minutos en la ventana y 99,9 % o más; (4) conciliación sin diferencias, 0 sin explicar y 0 pedidos perdidos; (5) personal capacitado y certificado, 100 % de los usuarios de la ola; (6) acta de la Contraparte Técnica, H7 en Etapa 1 y H12 en Etapa 2.

Cada día se decide entre continuar, corregir o revertir, y la marcha blanca cierra solo cuando las seis condiciones se cumplen a la vez.

### 2.5 Procedimiento de reversión

La reversión la autoriza el responsable de operaciones del CLIENTE cuando un indicador amenaza el despacho. Sus disparadores son observables: pedidos sin sincronizar al inicio de la carga, rutas del día no disponibles para cargar o un defecto crítico en la ventana de despacho. La decisión se toma en el turno de noche, y la vuelta a la hoja de picking y a la guía en papel debe completarse antes de las 05:30, para que los 96 camiones salgan a tiempo. Ese plazo protege el despacho; no es el RTO de recuperación ante desastres. La siguiente descripción textual corresponde a la Figura T-18.3, «Procedimiento de reversión de la Etapa 1» (Fuente: elaboración propia a partir del Capítulo 3, sección 3.4.4, y del paquete 4.1.2):

- El reloj abarca el turno de noche desde las 22:00; preparación, detección y decisión transcurren antes de las 05:30, y el despacho se señala entre 05:30 y 07:00.
- Tres carriles representan al responsable de operaciones del CLIENTE, al Líder de Implantación y Gestión del Cambio y al Líder de Operación / SRE.
- El Líder de Operación / SRE detecta una señal en el monitoreo; el acompañante confirma el impacto y se pregunta si amenaza el despacho.
- Si no lo amenaza, se corrige y la ola continúa.
- Si lo amenaza, la vuelta al papel debe estar completa antes de las 05:30. En el plano operacional se vuelve a la hoja de picking y la guía en papel; en el técnico, se usa el interruptor o la versión anterior. Al retomar, se concilia lo que quedó en cola y la ola reinicia sus cuatro semanas.

No se pierde información: los registros capturados durante la ola quedan en cola y se concilian al retomar. Lo que se pierde es la jornada de operación en la solución nueva para esa ola, que vuelve a empezar su período de cuatro semanas (Capítulo 3, sección 3.4.4; paquete 4.1.2; Caso 02, sección 17.6, punto 4). El tiempo de cada nivel de reversión se mide en el ensayo en Preproducción que precede a cada corte (RT-20.02).

### 2.6 Acompañamiento en terreno y estabilización

Después de cada paso a producción hay cuatro semanas de estabilización por ola, el mismo período que exige el criterio de avance. La dotación se deriva de la operación del caso (Capítulo 3, sección 3.4.4; paquete 4.2.2), como muestra la tabla «Dotación de acompañamiento y estabilización de la Etapa 1» (Fuente: Capítulo 3, sección 3.4.4):

| Frente de acompañamiento | Dotación | Cálculo |
|---|---:|---|
| Bodega, turno de noche (22:00 a 06:00) | 2 personas | 1 por centro de distribución (Talca y Concepción) |
| Plataformas de cross-docking | 3 personas | 1 por plataforma, en la recepción de madrugada y el despacho de la mañana |
| Calle (preventa y reparto) | 7 personas | 96 camiones + 62 preventistas = 158 rutas diarias; 158 / 24 días (lunes a sábado en 4 semanas) ≈ 6,6 |
| Coordinación | 1 persona | Líder de Implantación y Gestión del Cambio |

Si la ola cubre solo una zona, la dotación de calle se reduce en proporción a sus rutas, y la dotación decrece según la curva de adopción, como exige el RT-20.05.

### 2.7 Capacitación y certificación

La capacitación se hace en el puesto y en la ruta, sin detener la venta ni el reparto (Caso 02, sección 13.3, condición 5). Usa las cuatro modalidades del Art. 90.2: presencial en cada sitio, en línea sincrónica, autoformación en línea y acompañamiento en el puesto durante la marcha blanca. Cada perfil se certifica antes de cerrar la marcha blanca, porque el Art. 17.3 exige personal «capacitado y certificado conforme al plan de capacitación aprobado» (paquetes 7.1.1 a 7.1.6 y 7.3.1). Los usuarios administradores y el equipo técnico del CLIENTE se certifican además conforme al Art. 90.4. La tabla «Perfiles operativos y modalidad de capacitación» (Fuente: Capítulo 3, Anexo 3.I, a partir del Caso 02) presenta los perfiles operativos:

| Perfil | Personas | Cómo se capacita sin detener la operación |
|---|---:|---|
| Preparadores | 120 | Aprendizaje en el puesto de 2 horas como máximo (RNF-05.03) y un tutor por turno; capacitación continua por la rotación del 38 % |
| Preventistas | 62 | Prueba de captura sin señal en su propia ruta y acompañamiento en ruta |
| Tripulación propia y peonetas | 84 | Prueba de entrega digital y rendición antes de la ola, y acompañamiento en ruta |
| Conductores de transportistas | ≈ 160 | Incorporación en el andén al asignarse a una ruta, con autenticación y vinculación persona–vehículo–viaje (S-05) |

Los conductores de transportistas no son trabajadores de la compañía. Su incorporación requiere el acuerdo operacional firmado con cada una de las diez empresas (paquete 5.4.1), y una ola de reparto no incluye a una empresa transportista hasta que su acuerdo esté firmado (Capítulo 3, Anexo 3.I; Caso 02, sección 13.3, condición 6). El uso del GPS para control de jornada requiere el acuerdo previo con el sindicato (paquete 5.4.2; S-13).

### 2.8 Medición de la adopción

La adopción se mide por perfil y por ola con los indicadores del Capítulo 3, Anexo 3.I: pedidos capturados en la aplicación sobre el total, entregas con prueba digital, preparadores certificados por turno y conductores con autenticación válida. La meta es que el 100 % de los usuarios de la ola esté certificado y que el 100 % de las transacciones de la ola se registre en la solución al retirar el papel. Si una ola no alcanza la meta, no avanza y se extiende el acompañamiento (paquete 7.2.5).

La respuesta es distinta según el grupo (Caso 02, sección 17.6, punto 7). El personal con 20 o 30 años en la compañía recibe acompañamiento individual en su puesto o ruta y reconocimiento formal de su conocimiento (paquete 7.2.1), y el personal rotativo de preparación cuenta con un tutor por turno y certificación en el puesto (paquete 7.1.2).

### 2.9 Cierre de la marcha blanca y paso a producción

La marcha blanca de la Etapa 1 cierra cuando se cumplen a la vez las seis condiciones del Art. 17.3. El paso a producción ocurre en el mes 16, fuera de las fechas prohibidas, y se formaliza con el acta del H7 (paquete 4.2.3). Si al término del mes 15 no se cumplen las condiciones, la marcha blanca se extiende a costo del adjudicatario, sin mover las fechas de las fases siguientes (Art. 17.3).

## 3 Etapa 2: marcha blanca de los meses 19 y 20 y producción desde el mes 21

La Etapa 2 se implanta sobre la plataforma ya estabilizada de la Etapa 1, con una marcha blanca más corta y en convivencia con la Etapa 1 en producción.

### 3.1 Alcance y despliegue

La Etapa 2 pone en producción el intercambio electrónico de pedidos y avisos de despacho con las cadenas (M11 Canal moderno), el portal de clientes, el portal de transportistas y el costo de servir por cliente y por entrega (M10). Corresponde a los paquetes 3.5.1 a 3.5.4, 3.6.5 y 3.6.6 del Formulario T-14 y se despliega sobre la plataforma de la Etapa 1, sin rehacer su arquitectura (Bases Administrativas, Art. 15.1).

El despliegue avanza por cadena y por grupo de usuarios. Cada cadena se incorpora al intercambio electrónico cuando su perfil está certificado (paquetes 3.6.5 y 3.6.6) y, hasta entonces, sus pedidos siguen con carga manual controlada, que no acredita el resultado R18-13. Los portales se habilitan por grupo de clientes y por transportista, y el costo de servir se habilita para Comercial y Finanzas con los hechos acumulados desde la marcha blanca de la Etapa 1.

El calendario de la Etapa 2 es más estrecho que el de la Etapa 1. Su marcha blanca dura dos meses, unas 8,7 semanas ($2 \times 52 / 12$), y el Art. 17.3 exige volumen real en las cuatro últimas, así que todas las cadenas certificadas, los portales y el costo de servir deben quedar habilitados en las primeras 4,7 semanas ($8{,}7 - 4$). El volumen comprometido incluye el 100 % de los pedidos de las cadenas certificadas, recibidos por intercambio electrónico y con aviso de despacho, y el 100 % de las entregas del período con costo de servir calculado (cerca de 1.400 por día hábil en un mes normal; Caso 02, sección 14.1).

Con el inicio de contrato de febrero de 2027 (Anexo 7.A del Subdocumento 7), el mes 19 cae en agosto de 2028 y el mes 20 en septiembre, lo que tiene tres consecuencias. La primera es que toda habilitación de la Etapa 2 ocurre en agosto, porque el congelamiento total va del 1 al 25 de septiembre (Caso 02, RT-10.05), lo que coincide con el límite de 4,7 semanas. La segunda es que las cuatro semanas de cierre caen en el peak de Fiestas Patrias, cuando las entregas suben de cerca de 1.400 a 2.600 por día y la ventana de despacho opera al máximo; el volumen comprometido es entonces el del peak, en el primer septiembre de la Etapa 1 en producción. La tercera es que entre el 1 y el 25 de septiembre no se despliega ningún cambio sobre ninguna de las dos etapas: ante un defecto de la Etapa 2, la única acción es su reversión por interruptor de funcionalidad (sección 3.4), que vuelve la capacidad al procedimiento anterior sin instalar software.

La capacidad para ese peak se demuestra antes del H11 con las pruebas de carga a 1,5 veces el peak, con ambas etapas activas (paquete 3.9.3). El caso advierte que septiembre es «el período de mayor exigencia sobre cualquier componente nuevo» (sección 13.2).

### 3.2 Pruebas previas

Antes del paso a producción del mes 21 se aprueban las mismas pruebas de la sección 2.2, aplicadas a la Etapa 2 (paquetes 3.9.1 a 3.9.7). Se agrega una exigencia: demostrar que la Etapa 1, ya en producción, no se degrada. Las pruebas de carga se ejecutan con ambas etapas activas (3.9.3), y la recuperación ante desastres, con ambas etapas (3.9.4).

### 3.3 Indicadores diarios y umbrales de cierre

Se aplican los indicadores de la sección 2.4 a los usuarios y transacciones de la Etapa 2, más los propios de su alcance, que presenta la tabla «Indicadores propios de la marcha blanca de la Etapa 2» (Fuente: Capítulo 3, Anexo 3.J, y Bases Administrativas, Art. 17.2):

| Indicador diario | Umbral | Fuente |
|---|---|---|
| Pedidos de cadenas certificadas recibidos por intercambio electrónico | 100 % | R18-13 (Capítulo 3, Anexo 3.J) |
| Avisos de despacho emitidos dentro de 2 minutos de la carga | 100 % | RF-12.09 |
| Entregas con costo de servir calculado | 100 % | R18-11 |
| Datos de la Etapa 1 digitados dos veces o con dos escritores | 0 | Art. 17.2, punto 2 |
| Degradación de los indicadores de la Etapa 1 en producción | Ninguna respecto del mes anterior | Art. 17.2, punto 3 |

Los dos últimos indicadores protegen a la Etapa 1 durante la convivencia. R18-11 se acepta con la reconciliación con la contabilidad del mes (Capítulo 3, Anexo 3.J).

### 3.4 Reversión

La reversión de la Etapa 2 no toca la Etapa 1. Desactiva por interruptor de funcionalidad la capacidad de la Etapa 2 que falla, y la operación vuelve al procedimiento anterior de esa capacidad: carga manual controlada de los pedidos de la cadena, atención asistida a clientes y transportistas, o el cálculo vigente de costos. Ningún despliegue ni reversión ocurre en la ventana de 05:30 a 07:00 ni en fechas prohibidas (paquete 4.1.3).

### 3.5 Estabilización, capacitación y certificación

Después del paso a producción del mes 21 hay cuatro semanas de estabilización, concentrada en los usuarios nuevos: Comercial, Finanzas, las cadenas y los transportistas (paquete 4.3.2). Comercial y Finanzas se certifican en costo de servir antes del cierre de la marcha blanca (paquete 7.3.2), y la gestión del cambio con las cadenas y los transportistas se hace con el paquete 7.2.2.

### 3.6 Cierre y aceptación final

La marcha blanca de la Etapa 2 cierra con las seis condiciones del Art. 17.3. El paso a producción del mes 21 es la aceptación final de la implementación (H12, paquete 4.3.3), condicionada a la constitución de la garantía de correcto funcionamiento (paquete 4.3.4; Bases Administrativas, Art. 37.1).

## 4 Convivencia entre la Etapa 1 y la Etapa 2

La convivencia sigue las reglas del Art. 17.2. En los meses 13 a 15 coexisten la marcha blanca de la Etapa 1 y el desarrollo de la Etapa 2: el desarrollo de la Etapa 2 no despliega en Producción ni modifica las funciones de la Etapa 1 en marcha blanca, y los frentes de ambos esfuerzos están en el Formulario T-15. En los meses 19 y 20 la Etapa 1 está en producción y la Etapa 2 en marcha blanca, con una única fuente de verdad para los datos compartidos (pedidos, clientes, guías y entregas): la Etapa 2 lee y extiende los registros de la Etapa 1, sin copiarlos ni volver a digitarlos. En el mes 21, el paso a producción de la Etapa 2 no degrada la disponibilidad, el desempeño ni la integridad de los datos de la Etapa 1, y la Operación comienza ese mes con ambos alcances. La siguiente descripción textual corresponde a la Figura T-18.4, «Convivencia de la Etapa 1 en producción con la Etapa 2 en marcha blanca» (Fuente: elaboración propia a partir de la arquitectura lógica del Capítulo 4):

- A la izquierda, Etapa 1 en producción incluye M1 Recepción, M2 Inventario, M3 Preventa, M4 Rutas, M5 Preparación, M6 Reparto, M7 Cobranza y rendición, M8 Devoluciones y envases, M9 Calidad y trazabilidad, M10 Analítica (indicadores y OTIF) y M12 Telemetría. Estos módulos escriben en el registro único de la plataforma.
- El registro único contiene clientes, pedidos, guías de despacho, entregas, lotes y cobros, con un solo escritor por dato y sin copias. Se relaciona bidireccionalmente con el ERP, que es el registro contable y el único emisor de la guía de despacho.
- A la derecha, Etapa 2 en marcha blanca incluye M11 Canal moderno, Portal de clientes, Portal de transportistas y M10 Analítica: costo de servir. La Etapa 2 lee y extiende el registro único; no duplica los datos.
- Ningún despliegue de Etapa 2 modifica una función estabilizada de Etapa 1.

La Etapa 1 escribe en el registro único y la Etapa 2 lo lee y lo extiende; ninguna de las dos mantiene una copia de los datos de la otra, por lo que no existe una doble digitación que conciliar.

## 5 Transferencia a la Operación

La transferencia al equipo de TI de cuatro personas del CLIENTE se hace antes del mes 21. Comprende los procedimientos de operación documentados y ensayados y la base de conocimiento (paquetes 7.1.4 y 3.11.2). Sigue una mentoría de seis meses después del paso a producción de la Etapa 2 (paquete 8.5.2; RT-22.07).

Queda como servicio permanente del adjudicatario durante los 36 meses lo que el Capítulo 3, sección 3.4.5, asigna a LafroX: el centro de operaciones, la mesa de servicio, la gestión de incidentes, la continuidad, la seguridad y el mantenimiento, que corresponden a los paquetes 8.1 y 8.2 (Caso 02, sección 17.6, punto 8).

## Referencias

Las Bases se citan con su documento y el artículo, capítulo, sección o código del requisito.

- Distribuidora Puelche S.A. (2026a). *Bases Administrativas de Licitación N.º TFEP-01/2026: Contratación de Solución Integral de Software y Servicios de Operación*.
- Distribuidora Puelche S.A. (2026b). *Bases Técnicas Transversales de Licitación N.º TFEP-01/2026*.
- Distribuidora Puelche S.A. (2026c). *Caso 02: Logística. Especificaciones del problema y operación de Distribuidora Puelche S.A.*
