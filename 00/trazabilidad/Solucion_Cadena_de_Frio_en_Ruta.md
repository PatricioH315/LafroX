# Cadena de frío en ruta: alertas y registro de temperatura en los camiones refrigerados de Puelche

**LafroX · Caso 02 · Documento de trabajo del Subdocumento 4 · versión 9.4 · 24‑10‑2026**

**Estado:** base de ingeniería para cotizar, construir y probar. **No autoriza compras** hasta aprobar las pruebas de §17 y obtener cotización escrita de un proveedor con domicilio en Chile. No está incorporado al texto de ningún subdocumento.

> Este documento **no contiene precios**. Las Bases Administrativas (art. 50.2) prohíben en la Oferta Técnica «información de precios, tarifas, valores unitarios ni cifra alguna que permita inferir el monto de la oferta económica». Los costos se tratan aparte, en el Informe 3.

**Etiquetas:** [H] verificado en la fuente citada · [I] inferencia de diseño · [C] requiere confirmación escrita o prueba · [E] estimación · [P] compromiso propio de LafroX, no exigido por las Bases.

**Términos usados en este documento:**

| Término | Significado |
|---|---|
| **Caja** o **carrocería refrigerada** | La parte de carga del camión, detrás de la cabina: el furgón aislado donde viaja el producto, enfriado por el equipo de frío. «Techo de la caja» es su parte superior, el punto más alto del camión |
| **Celular** o **red móvil** | La red 4G de los operadores chilenos (Entel, Movistar, Claro, WOM). El gateway la usa con sus propias SIM, igual que un teléfono usa sus datos móviles. No es un teléfono |
| **Gateway** | El computador industrial que va fijo en la cabina: mide, decide, guarda y transmite |
| **Satélite** | Red Iridium: mensajes cortos en ambos sentidos, siempre activa, con o sin red móvil. No es internet satelital |
| **TC58e** | El terminal Zebra que ya usa el conductor para entregar |
| **Simulador de producto** | Sonda dentro de una botella con glicol, que se calienta al ritmo del alimento |
| **SSCC** | Código de cada unidad logística (pallet o bulto) que se escanea |

---

## 1. El problema y lo que ya comprometimos

| Hecho del caso | Consecuencia |
|---|---|
| Un cliente de food service rechazó un camión completo por sospecha de ruptura de la cadena de frío y Puelche no pudo demostrar lo contrario | Pérdida de CLP 21 millones (Caso §4.9) |
| La autoridad sanitaria observó la ausencia de registro continuo de temperatura | Observación en la fiscalización (Caso §4.9) |
| Hoy el conductor lee un termógrafo manual tres veces por viaje | No hay registro continuo ni alerta (Caso §4.9) |
| Rutas rurales con tramos sin señal de hasta dos horas y rutas completas sin señal hasta el regreso | Empedrado, Chanco, Cauquenes, Pinto y Alto Biobío (Caso, tabla de cobertura) |

El Caso pide registro continuo y automático, alerta oportuna, evidencia ante la autoridad y el cliente, y una regla escrita (§9.6; criterio de aceptación n.º 3). La revisión del Informe 1 exigió explícitamente **alerta en ruta para los 28 vehículos con frío**.

**Compromisos del SD3 que este diseño debe respetar:**

| Código | Compromiso |
|---|---|
| RF‑09.04 | Registro automático y continuo en los 28 camiones con frío (18 propios y 10 de transportistas, S‑28) |
| RF‑09.05 | Alerta en tiempo real, en cabina y en la plataforma, ante una desviación continua de 2 °C por 15 min, parametrizable por tipo de producto |
| RF‑09.06 | Ante una excursión crítica y sostenida, bloqueo preventivo del lote afectado y aviso a Calidad. Calidad decide liberar, bloquear o rechazar |
| RF‑09.07 | El rechazo por sospecha de ruptura queda asociado al sensor del camión en ese tramo |
| RNF‑09.05 | Frecuencia parametrizable, suficiente para detectar 2 °C por 15 min. Un intervalo sin lectura es un evento |
| RNG‑04 | Respuesta graduada: advertencia ante una excursión menor y transitoria; retención preventiva ante una crítica y sostenida. **La disposición final es siempre de Calidad** y nunca se delega al conductor. Mientras Calidad no apruebe los parámetros de un producto, toda lectura fuera del rango de su ficha es crítica |
| RT‑05.29 | Temperatura en los indicadores de la operación del día con ≤ 5 min de demora |
| RT‑03.10 y RT‑03.13 | Terreno: turno completo de 14 h sin señal; sincronización de la jornada en ≤ 10 min |

---

## 2. Normativa aplicable

| Fuente | Qué exige | Cómo lo cumple el diseño |
|---|---|---|
| **Reglamento Sanitario de los Alimentos (DS 977/96), art. 68** [H] | Alimentos perecibles con frío: vehículo de carrocería cerrada, equipo capaz de mantener la temperatura, **termómetro legible desde el exterior**, higiene y autorización sanitaria del vehículo | El chequeo previo registra por camión el termómetro exterior y la vigencia de la autorización sanitaria (§8.1) |
| **RSA, art. 190** [H] | Transporte interurbano de congelados: producto a −18 °C o menos, termómetro exterior y **dispositivos que registren la temperatura durante el transporte**. Se tolera que el **producto** suba hasta −15 °C, situación que debe corregirse rápidamente | Registro continuo (§4). Para congelados, un simulador de producto sobre −15 °C es crítica (§7) |
| **RSA, art. 191** [H] | Reparto local de congelados a minoristas: todo aumento sobre −18 °C por el mínimo tiempo y **nunca sobre −12 °C** | Regla de la familia congelados en reparto local (§7) |
| **RSA, art. 303** [H] | Cecinas: transporte refrigerado entre 0 y 6 °C | Regla de la familia cecinas (§7) |
| **Reglamento (CE) 37/2005, art. 2** [H] | Vigilar la **temperatura del aire** con instrumentos de registro conformes a **EN 12830, EN 13485 y EN 13486**; registros fechados y guardados al menos un año | Termógrafo EN 12830 en el aire (§4); se guarda 5 años (RT‑05.10) |
| **Codex CAC/RCP 8‑1976, §4.7** [H] | Congelados: preenfriar el compartimento antes de cargar; en distribución, el paquete más caliente no debe superar −12 °C | Preenfriamiento verificado antes de cargar (§8.1) |
| **FDA, 21 CFR 1.908(a)(6)** [H] (referencia internacional, no obligatoria en Chile) | Si se sospecha una falla de temperatura, el alimento **no se vende ni se distribuye** hasta que una persona calificada determine que no se volvió inseguro | Retención por SSCC en el TC58e hasta la decisión de Calidad (§7, §10) |
| **FDA, 21 CFR 1.908(e)(2)** [H] (referencia) | El transportista debe poder **demostrar** que mantuvo la temperatura | Curva en la puerta del cliente y expediente certificado (§8.5, §8.7) |

**Por qué aire y producto se miden distinto.** El RSA fija límites sobre la **temperatura del producto** (arts. 190 y 191). El Reglamento europeo pide registrar la **temperatura del aire** con instrumentos certificados. Las dos mediciones cumplen funciones distintas:

- El **aire** reacciona en segundos cuando se abre la puerta: sirve para el registro certificado y para detectar a tiempo una falla del equipo de frío.
- El **producto** cambia despacio: es lo que define si el alimento sigue apto.

La práctica de la industria para estimar la temperatura del producto sin perforarlo es la **sonda simuladora de producto**: una sonda dentro de una botella con glicol o un bloque sólido que se calienta y se enfría al ritmo del alimento. Un fabricante informa que, al abrir la puerta de una cámara de ensayo, la sonda de aire subió 7 a 10 grados mientras los simuladores permanecieron estables, y otro que su uso elimina las falsas alarmas por apertura de puerta [H, fuentes de fabricantes: Copeland/Cooper‑Atkins, Primex]. Es práctica de la industria, no exigencia legal; por eso el diseño mantiene además el termógrafo de aire certificado.

---

## 3. Criterio de diseño y decisiones

### 3.1 Criterio

**La mejor solución técnica, sin sobreingeniería.** Cada componente debe cubrir un requisito o una falla que ningún otro cubre. Si dos piezas hacen lo mismo, sobra una. El precio no limita la elección; sí la limitan la disponibilidad en Chile y la complejidad innecesaria, porque la complejidad también es una fuente de fallas.

| Componente | Requisito o falla que cubre | Si se quita |
|---|---|---|
| Gateway del camión (controlador A) | Mide, decide y protege aunque el conductor se baje con el TC58e | No hay vigilancia en vivo durante la entrega |
| Dos SIM de operadores distintos | Caída o falta de cobertura de un operador | Más horas sin datos en ruta |
| Iridium Edge, en ambos sentidos y siempre activo | Alerta, curva y órdenes de Calidad en las rutas rurales sin red móvil (RT‑05.29, revisión del Informe 1) | La nube y Calidad quedan ciegas por horas en las rutas rurales |
| Dos simuladores de producto | Decisión con temperatura de producto; una falla no detiene el reparto | Una sonda dañada deja el compartimento NO CONFIABLE |
| Sonda de aire de retorno | Detecta temprano la falla del equipo de frío | Se descubre tarde, cuando el producto ya se calentó |
| Sensor independiente en glicol | Detecta que el gateway mide o decide mal (falla silenciosa) | Una falla silenciosa del gateway permite entregar producto comprometido |
| Termógrafo EN 12830 en aire | Evidencia certificada ante la autoridad y el cliente | El registro no tiene valor de instrumento certificado |
| Sensor de puerta | Evita falsas alarmas y detecta puerta abierta prolongada | Advertencias falsas en cada entrega urbana |
| UPS del kit | Vigilancia con el motor apagado | Sin registro durante las detenciones |
| TC58e (existente) como segunda cadena | Evalúa la misma regla con el sensor independiente y frena la entrega | No hay quien bloquee la entrega ni quien vigile al gateway |

### 3.2 Decisiones (24‑10‑2026)

1. **Mismo kit para los 28 camiones**, propios y de transportistas. El supuesto S‑28 del SD3 hay que reescribirlo: hoy habla solo de un termógrafo (§22.3 y §22.13).
2. **Plataforma de borde única:** el camión corre **AWS IoT Greengrass V2**, igual que los gateways de cámara de los CD (B‑02). La regla térmica es **el mismo componente de software** en cámaras y camiones.
3. **Red móvil de dos operadores y satélite Iridium, los dos siempre activos y en ambos sentidos.** Por satélite viajan siempre las alarmas, la curva cada 3 minutos y las órdenes de Calidad; por la red móvil, cuando hay, la curva cada minuto. Detectar, alarmar y frenar la entrega no dependen de ninguna red (§6.1). **Sin internet satelital** en el camión.
4. **La decisión se toma con simuladores de producto.** El aire diagnostica y queda en el registro certificado.
5. **La segunda cadena la forman el TC58e y un sensor independiente**, sin transmisor ni alarma adicionales.
6. **Termógrafo EN 12830 cada 1 minuto.**
7. **Tiempo fuera de frío en el andén** calculado con los escaneos de M5.
8. **Acción por defecto:** lo retenido sigue retenido y vuelve al CD; Calidad decide. No requiere una guardia nueva.
9. **El registro de temperatura no guarda posición GPS.** El tramo se deduce de la secuencia de entregas.
10. **Solo equipos con presencia comercial en Chile**, o marcados [C] hasta obtener cotización local (§15).

---

## 4. Qué se mide y cómo se asigna a cada SSCC

**Se mide por compartimento, no por producto.** La mayoría de los camiones tiene un solo compartimento; algunos tienen dos (frío y congelado, con división). Cada sensor pertenece a un compartimento.

**Cada SSCC se asigna a un compartimento y a un intervalo de tiempo.** El manifiesto del viaje (§8.1) dice qué SSCC va en qué compartimento. Los escaneos marcan cuándo entró al camión y cuándo salió (§8.4). Con eso, la **historia térmica de cada SSCC** es:

`tiempo fuera de frío en el andén (§8.2) + curva de su compartimento desde que se cargó hasta que se bajó`

**Historia completa de cada SSCC:** cámara del CD (sensores B‑01, por ubicación) → andén → compartimento del camión → entrega. Un **pedido** es un conjunto de SSCC, así que su historia es la de sus SSCC.

**Ejemplo.** Pedido 4521 del almacén «Don Lucho», 2 SSCC de lácteos:

| Hora | Evento | Qué se registra |
|---|---|---|
| 02:10–04:05 | En la cámara de Talca | Curva de la cámara donde estaban ubicados |
| 04:05 | Escaneo al salir de la cámara | Empieza el tiempo fuera de frío |
| 04:17 | Escaneo de carga en el camión 12 | 12 min fuera de frío; dentro del máximo de la familia |
| 04:17–09:47 | A bordo | Curva del compartimento en ese intervalo |
| 09:47 | Escaneo de bajada en la entrega 7 | Fin de su historia en el camión |
| 10:30–11:00 | Excursión en el camión | **No afecta al pedido 4521**: ya estaba entregado. Sí afecta a los SSCC que seguían a bordo |

En la puerta, el almacenero ve justamente esa curva: la de su pedido, no la del día completo del camión.

**Por qué basta medir el compartimento y no cada envase:**

- Dentro de una caja cerrada, todos los envases comparten el mismo aire frío. Lo que los diferencia es **dónde están** (cerca de la puerta se calienta más; cerca del evaporador, menos) y **con qué temperatura entraron**.
- **La posición** la cubre el mapeo térmico (V4): encuentra el punto más caliente de cada tipo de caja, y ahí se ponen los simuladores. Se mide el **peor caso**: si ese punto cumple la regla, todos los envases la cumplen. Si no la cumple, se retiene lo que corresponda, que es la decisión conservadora.
- **La temperatura de entrada** la cubren la curva de la cámara, el tiempo fuera de frío en el andén y el preenfriamiento del camión (§8.1 y §8.2).
- Es el mismo método que usa la normativa europea, que registra el aire del medio de transporte (Reglamento CE 37/2005).

**Por qué no un registrador por pedido:** son unas 1.400 entregas al día a almacenes que no devolverían el aparato. Haría falta uno desechable por pedido, o recuperarlo en cada puerta, y no mejoraría la decisión: el punto más caliente ya está medido. Sería sobreingeniería. **Excepción opcional:** en pedidos grandes de food service, un registrador reutilizable por pallet, que el conductor retira en la entrega después de mostrar la curva. El caso de los CLP 21 millones fue un camión completo de un solo cliente: ahí la curva del compartimento ya es la curva de ese cliente.

**La decisión es por SSCC, según su familia.** La misma curva puede dejar retenido un yogur y no un queso con un rango más amplio. Por eso:

- un SSCC **ya entregado** antes de la excursión no queda afectado; su curva hasta la entrega forma parte de su expediente;
- un SSCC **todavía a bordo** en el compartimento afectado queda retenido **si la excursión supera la regla de su familia**;
- en un camión de un solo compartimento, una excursión grave puede retener **todo el frío que queda a bordo**; los SSCC sin cadena de frío siguen su ruta. §8.3 explica cómo el aviso temprano permite salvar la carga antes de llegar a eso.

**Puntos de medición por compartimento (base: un compartimento por camión):**

| Punto | Equipo | Lo lee | Para qué |
|---|---|---|---|
| Aire de retorno | Sonda PT100 | Gateway | Diagnóstico del equipo de frío; advertencia temprana |
| Simulador de producto, punto crítico | Sonda PT100 en botella de glicol | Gateway | **Decide** advertencia y crítica |
| Simulador de producto, punto secundario | Sonda PT100 en botella de glicol | Gateway | Redundancia del punto anterior |
| Sensor independiente | Sensor Bluetooth EN 12830 en botella de glicol, junto al simulador crítico | TC58e | Vigila que el gateway mida y decida bien |
| Aire, registro certificado | Termógrafo Bluetooth EN 12830, cada 1 min | TC58e | Evidencia ante la autoridad y el cliente |
| Puerta de carga | Sensor magnético | Gateway | Explica las variaciones del aire y detecta puerta abierta prolongada |
| Alarma del equipo de frío | Contacto del equipo, si existe | Gateway | Anticipa la falla del equipo |

La ubicación del punto crítico y el volumen de las botellas los fija el **ensayo de mapeo** de cada tipo de caja (V4), antes del piloto.

---

## 5. Arquitectura

### 5.1 Vista por capas

| Capa | Dónde | Qué hay | Responsabilidad |
|---|---|---|---|
| **Medición** | Caja refrigerada | 3 sondas PT100, sensor independiente, termógrafo, sensor de puerta | Medir |
| **Borde** | Cabina | Gateway con Greengrass, Iridium Edge, TC58e | Decidir, proteger, guardar y transmitir **sin depender de la red** |
| **Transporte** | — | LTE de dos operadores; Iridium SBD | Llevar mensajes en ambos sentidos |
| **Nube** | AWS sa‑east‑1, recuperación en us‑east‑1 | IoT Core, Iridium CloudConnect, SQS, M9 (Aurora con bandeja de salida), DynamoDB N‑06, S3 con bloqueo de objetos, KMS, mensajería | Registrar, avisar, decidir y producir evidencia |
| **Personas** | — | Conductor, Calidad (responsable de llamada), despacho | Actuar |

Principio: **la protección del producto ocurre en el borde.** La nube avisa, registra y permite decidir, pero el producto queda protegido aunque la nube o la red no estén.

### 5.2 Equipos del camión

| Equipo | Función | Candidato | Prueba |
|---|---|---|---|
| **Gateway (controlador A)** | Corre Greengrass: lee las sondas, evalúa la regla, guarda y transmite, maneja el Iridium Edge, publica el latido al TC58e | Familia del B‑02 de los CD: **Moxa UC‑8200** con LTE Cat 4 y doble SIM, 2 puertos Ethernet, puertos serie, 4 entradas y 4 salidas digitales, ranura Wi‑Fi, doble entrada de energía de 12–48 VDC, golpes y vibración según IEC 60068 (2 Grms), −40…70 °C con LTE [H]. **No tiene homologación vehicular E‑mark** [H]: se instala sobre base antivibración y con acondicionador de energía automotriz, y se prueba en V5 | V1, V5 |
| Módulo de sondas | Convierte las sondas PT100 en lecturas digitales y las entrega por Ethernet (Modbus TCP) | **Moxa ioLogik E1260‑T**: 6 entradas para PT100 de 2 o 3 hilos, resolución 0,1 °C, −40…75 °C [H]. Mismo representante que el gateway | V1 |
| **Iridium Edge** | Módem satelital SBD con antena integrada, IP67. El gateway lo maneja por RS‑232 con comandos AT: envía datos binarios propios y recibe mensajes de bajada [H]. Mensajes de hasta 340 bytes de subida y 270 de bajada [H] | Globalsat Chile [H] | V2, V18, V19 |
| **Sensor independiente** | Mide la temperatura de producto simulada, con su propia batería, y la transmite por Bluetooth | **Teltonika EYE SENSOR EN12830**: clase de exactitud 0,5, calibración en laboratorio ISO 17025, memoria de 345 días, −20…+60 °C [H] | V3, V8 |
| **Termógrafo EN 12830** | Registro certificado del aire, cada 1 min | El mismo **EYE SENSOR EN12830**, en el aire [H]. En compartimentos de congelado bajo −20 °C, ver §15 | V3 |
| **TC58e** (existente) | Pantalla y freno del conductor; segunda cadena de evaluación | App Kotlin del SD4 | V8, V9, V14 |
| Sensor de puerta, luz y zumbador, UPS y protección del kit | §5.4 y §5.5 | Genéricos automotrices [C] | V5 |

### 5.3 Software en el borde (componentes de Greengrass)

| Componente | Origen | Función |
|---|---|---|
| Lectura de sondas | Propio, sobre Modbus TCP (AWS ofrece un componente solo para Modbus RTU [H]) | Lee las sondas del ioLogik cada 5 s |
| **Regla térmica** | Propio; **el mismo** que corre en los gateways de cámara (SD4 4.1, Capa 2) | Estados, histéresis, ventana de puerta, crítica por familia |
| Envío a la nube | Stream Manager, de AWS | Cola persistente con reintentos hacia IoT Core; sobrevive cortes de energía |
| Broker MQTT local y autenticación de dispositivos cliente | Componentes de AWS | El TC58e se conecta al gateway como dispositivo cliente, con certificado |
| Latido | Propio | Latido firmado cada 10 s al TC58e (§5.6) |
| Satélite | Propio | Arma y envía los mensajes SBD, recibe las órdenes de Calidad y las entrega al TC58e |
| Configuración | Sombra del dispositivo (AWS) | Manifiesto del viaje, reglas vigentes y parámetros |
| Actualización | Despliegues de Greengrass (AWS) | Actualiza el software de toda la flota por etapas, con reversión |

Son propios la lectura de sondas, el latido y el componente satelital, más la regla térmica, que se reutiliza de los CD. El resto lo provee AWS y ya forma parte del SD4. Greengrass V2 corre sobre Linux en procesadores Arm como el del UC‑8200; Moxa no publica un procedimiento propio, por lo que la instalación se valida en V1 [C].

### 5.4 Conexiones entre equipos

| Desde | Hacia | Medio | Señal |
|---|---|---|---|
| Sondas | Módulo de sondas | Cable PT100, 3 hilos | Temperatura |
| Módulo de sondas | Gateway, puerto Ethernet 2 | Ethernet, Modbus TCP | 3 lecturas cada 5 s |
| Sensor de puerta | Gateway, entrada digital 1 | Contacto | Puerta abierta o cerrada |
| Equipo de frío | Gateway, entrada digital 2 | Contacto, si existe | Alarma del equipo de frío |
| Ignición del camión | Gateway, entrada digital 3 | Contacto | Motor encendido o apagado |
| Gateway, salida digital | Luz y zumbador de cabina | Relé | Alarma en cabina |
| Gateway | Iridium Edge | RS‑232 y línea de encendido | Mensajes satelitales en ambos sentidos |
| Gateway | TC58e | Wi‑Fi de cabina, MQTT local | Latido, curva, órdenes de Calidad |
| Sensor independiente y termógrafo | TC58e | Bluetooth | Lectura en vivo y descarga de memoria |

### 5.5 Energía

- El kit tiene **su propia UPS**, alimentada desde la batería del camión con fusible y corte por bajo voltaje, para no descargar la batería de arranque. Autonomía ≥ 24 h con el motor apagado.
- El gateway y el Iridium Edge van en la UPS. El sensor independiente y el termógrafo usan su batería interna.
- Protección contra sobretensión de arranque y desconexión de batería en camiones de 12 y 24 V (V5).

### 5.6 Latido y doble evaluación en el TC58e

**Latido.** Cada 10 s, el gateway envía al TC58e un latido firmado con: secuencia, hora de la última lectura de cada sonda, valores de los simuladores, contador de ciclos del evaluador, estado de cada compartimento y revisión de estado vigente. El TC58e **lo rechaza** si alguna sonda tiene un dato de más de 30 s o si el contador no avanzó: un gateway encendido con la lectura congelada no pasa como sano.

**Doble evaluación.** Mientras está en la cabina, el TC58e lee por Bluetooth el sensor independiente y el termógrafo, y **evalúa la misma regla** con su propia implementación en Kotlin. Pasa a **RETENIDO por contradicción** si:

- según el sensor independiente hay crítica y el gateway dice NORMAL; o
- el simulador del gateway y el sensor independiente difieren más que la tolerancia del mapeo; o
- el aire del gateway y el termógrafo difieren más que la tolerancia del mapeo.

Si el conductor se baja, al volver el TC58e completa la serie que le faltó con la memoria del sensor independiente [C, V3].

**Nada de esto usa internet.** El Wi‑Fi de la cabina es una red local que arma el gateway, como un router doméstico sin conexión a internet. El Bluetooth es directo entre el sensor y el TC58e, y la luz y el zumbador van cableados. Todo funciona igual en un túnel o en una zona sin red móvil.

**Cuando el conductor se aleja del camión.** Si el TC58e pierde el latido justo después de un escaneo de bajada, entiende que el conductor está entregando y no suena. Al volver al alcance de la cabina, exige un latido válido antes de habilitar otra bajada y muestra cualquier alarma ocurrida mientras tanto. Si el latido se pierde sin una bajada en curso, por ejemplo mientras el camión avanza, pasa a NO CONFIABLE y alarma.

La app recibe el latido y lee Bluetooth en un **servicio en primer plano** (restricción de Android [H]). Al abrirse o reiniciarse arranca en **NO CONFIABLE** hasta recibir un latido válido.

---

## 6. Caminos de los datos

### 6.1 Detectar, frenar y avisar son tres cosas distintas

| Qué | Dónde ocurre | ¿Necesita red? |
|---|---|---|
| Detectar la excursión | Gateway del camión, y el TC58e como segunda cadena | **No** |
| Alarmar al conductor | Luz, zumbador y TC58e, en la cabina | **No** |
| Frenar la entrega del producto afectado | TC58e | **No** |
| Avisar a Calidad, mostrar la curva en el tablero y recibir su orden | Nube | **Sí**: red móvil o satélite |

Por eso una zona sin señal, un túnel o una quebrada **nunca** impiden que el producto quede retenido. Lo único que puede atrasarse es el aviso a Calidad.

### 6.2 Dos caminos, siempre activos

**Lo que dice el Caso:** las rutas urbanas (Talca, Curicó, Chillán, Concepción y Los Ángeles) tienen buena cobertura móvil. Las rutas rurales (Empedrado, Chanco, Cauquenes, Pinto y Alto Biobío) tienen tramos sin señal de hasta 2 h continuas, y hay rutas completas en que el conductor recupera la señal solo al volver; en invierno el tiempo sin cobertura aumenta (Caso, tablas de cobertura y de estacionalidad). Por eso el satélite **no es un respaldo ocasional**: en las rutas rurales es el camino principal. Los dos caminos funcionan siempre y en paralelo:

| Qué se envía | Red móvil, cuando hay | Satélite, siempre |
|---|---|---|
| Alarmas | De inmediato | De inmediato y en paralelo, con cola propia y prioridad |
| Curva | Cada 1 min: valor, mínimo y máximo de cada sonda, puerta y estado | Cada 3 min, con los últimos 3 min (≈ 43 bytes) |
| Órdenes de Calidad | Al TC58e por su propia SIM o por el gateway | Por el gateway, que las recoge en cada sesión satelital |

- **No hay que decidir cuándo cambiar de camino:** el satélite transmite siempre. Así también se evita el caso de una red móvil que muestra señal pero no deja pasar los datos.
- M9 descarta los duplicados que llegan por los dos caminos y, cuando llega la curva por la red móvil, reemplaza los lotes satelitales por la serie minuto a minuto.
- **Red móvil:** MQTT sobre TLS hasta AWS IoT Core, con un certificado por camión. Una regla deja el mensaje en SQS; M9 lo guarda y confirma al camión (A2). El gateway conserva una copia 72 h (§12).
- **Satélite:** Iridium CloudConnect, o la conexión directa del proveedor, entrega en SQS y M9 lo procesa igual (§12).
- Al recuperar la red móvil, el gateway sube la curva fina y la jornada se sincroniza en ≤ 10 min (RT‑03.13).

### 6.3 Una ruta rural, paso a paso

| Momento | En el camión | En la nube | Calidad |
|---|---|---|---|
| Sale de la zona con red móvil | Sin cambios | Sigue recibiendo por satélite | — |
| Cada 3 min | — | Curva de los últimos 3 min | Ve la curva con ≤ 4,5 min de antigüedad |
| Excursión | Luz, zumbador y retención en el TC58e | Alarma por satélite en ≤ 3 min [C, V2] | Aviso por app, SMS y voz; puede decidir y enviar la orden por satélite |
| Vuelve la red móvil | Sube la curva fina | Reemplaza los lotes | — |
| Regreso al CD | Descarga de los registradores | Expediente certificado en ≤ 2 h | Decide lo pendiente |

### 6.4 Túneles, quebradas y bosque denso

- **En un túnel no funcionan ni la red móvil ni el satélite.** Ningún sistema puede transmitir ahí sin infraestructura dentro del túnel.
- Mientras tanto, el camión sigue detectando, alarmando y frenando la entrega. Los mensajes esperan en la cola y salen apenas el camión vuelve a ver cielo o señal. Un túnel dura minutos.
- **En quebradas y bosque denso Iridium se degrada, pero sus satélites están en movimiento:** la geometría cambia cada pocos minutos y el gateway reintenta en cada ventana [I]. La prueba V18 mide en las rutas reales cuánto dura, como máximo, un corte de cielo.
- El producto con una retención activa **no se puede entregar**, haya o no red: lo impide el TC58e.

**Volumen satelital** (el satélite transmite toda la jornada de 14,5 h):

| Por camión y día | Por camión y mes (26 días) | Flota por día |
|---|---|---|
| 290 lotes, más alarmas y órdenes | 7.540 | 8.120 |

### 6.5 Coherencia de los datos

Con dos caminos, colas, túneles y reintentos, un mismo dato puede llegar dos veces, tarde o desordenado. Estas reglas mantienen la coherencia entre el gateway, el TC58e y la nube:

| Regla | Cómo se cumple |
|---|---|
| **Nada se pierde** | Cada mensaje queda en la cola persistente del gateway hasta su confirmación (A2), y después en el archivo de 72 h. El TC58e guarda sus propios eventos sin red (RT‑03.10) |
| **Nada se duplica** | Cada mensaje lleva productor (gateway o TC58e), número de arranque y secuencia. M9 procesa una sola vez cada combinación, llegue por la red móvil o por el satélite |
| **Ningún hueco pasa inadvertido** | M9 detecta los saltos de secuencia y pide el tramo faltante. Mientras falte, el compartimento queda «pendiente de verificación» en el expediente |
| **El orden lo da la secuencia, no la hora de llegada** | Un mensaje que llega tarde, por ejemplo después de un túnel, se ubica en su lugar en la curva |
| **Una crítica tardía siempre cuenta** | Abre la retención; si esos SSCC ya se entregaron, abre la evaluación de retiro (§8.8) |
| **Una recuperación tardía nunca cierra nada** | Solo puede cerrar una advertencia, nunca una crítica ni una retención |
| **La serie fina manda** | Los lotes satelitales sirven para el seguimiento en vivo. Cuando llega la serie minuto a minuto, la reemplaza. La evidencia usa la serie fina y el termógrafo certificado |
| **Las órdenes no pisan hechos nuevos** | Una orden de Calidad evaluada sobre un estado antiguo se rechaza (§10.3) |
| **La hora** | Intervalos con reloj monótono; hora de GNSS o NTP. Si la hora no es confiable, se ordena por secuencia |
| **El cierre** | El expediente se sella solo después de conciliar las tres series y los escaneos (§8.6) |

El camión es la autoridad sobre lo que ocurre en ruta: las retenciones se aplican ahí y la nube las refleja. Ninguna regla depende de que la red esté disponible en un momento dado.

---

## 7. Reglas y estados

### 7.1 Regla por familia

Calidad define cada regla por familia de producto y compartimento: límites, punto de referencia, criterio de exposición (continua o acumulada, en qué ventana) y plazos de acuse y acción. Se activa con segundo aprobador (RT‑16.03) y prueba en QA (RT‑16.05). Las reglas respetan, como mínimo, el RSA:

| Familia | Límite mínimo legal | Crítica |
|---|---|---|
| Congelados, interurbano | Producto ≤ −18 °C; tolerancia hasta −15 °C (RSA 190) | Simulador sobre −15 °C |
| Congelados, reparto local | Nunca sobre −12 °C (RSA 191) | Simulador sobre −12 °C, o sobre −18 °C más allá del tiempo que fije Calidad |
| Cecinas | 0–6 °C (RSA 303) | Simulador fuera de 0–6 °C según el criterio de exposición |
| Demás refrigerados | Según la ficha del producto | Simulador 2 °C sobre el límite durante 15 min (RF‑09.05) o el criterio acumulado de la familia |

Mientras Calidad no apruebe los parámetros de un producto, rige RNG‑04: toda lectura fuera del rango de su ficha es crítica.

### 7.2 Advertencia, crítica y puertas

| Situación | Resultado |
|---|---|
| Simulador cruza el límite de la familia, sostenido 30 s (con histéresis) | **ADVERTENCIA**: el conductor corrige (cierra, revisa el equipo) |
| Aire fuera de rango más de 10 min **con la puerta cerrada** | **ADVERTENCIA**: probable falla del equipo de frío |
| Puerta abierta más de 5 min seguidos | **ADVERTENCIA**: puerta abierta prolongada |
| Con la puerta abierta y hasta 10 min después de cerrarla | El aire **no** genera advertencias. El simulador sigue evaluando: **la crítica nunca se suspende** |
| Simulador cumple el criterio de crítica de la familia | **CRÍTICA** → los SSCC afectados pasan a **RETENIDO** |
| Contradicción entre el gateway y el sensor independiente (§5.6) | **RETENIDO**; decide Calidad |

Los tiempos de 10 y 5 min son valores iniciales [P]; Calidad los ajusta con el piloto.

### 7.3 Estados

- Por compartimento: `NORMAL → ADVERTENCIA → CRÍTICA → RETENIDO → {LIBERADO | BLOQUEADO | RECHAZADO}`, más **NO CONFIABLE**.
- Las retenciones son **por SSCC e incidente**. El estado del compartimento se deriva de ellas y nunca las borra.
- Una recuperación de temperatura solo cierra una ADVERTENCIA; nunca cierra CRÍTICA ni RETENIDO.

### 7.4 Fallas de medición

| Falla | Estado | Alcance | Recuperación |
|---|---|---|---|
| Sonda de aire sin datos o implausible | ADVERTENCIA técnica | Ninguno; decide el simulador | Reparación al regreso |
| Un simulador falla y el otro está sano | ADVERTENCIA técnica | Ninguno; decide el simulador sano | Reparación al regreso |
| Ambos simuladores fallan | **NO CONFIABLE** del compartimento | Todos sus SSCC de frío | Simuladores sanos y serie continua, o decisión de Calidad |
| Simulador y sensor independiente difieren más que la tolerancia | **RETENIDO** por contradicción | Todos sus SSCC de frío | Calidad, con la descarga del termógrafo y del sensor independiente |
| Sensor independiente o termógrafo sin datos | ADVERTENCIA técnica en el TC58e | Ninguno; el gateway sigue protegiendo | Reemplazo en el chequeo previo del viaje siguiente |

---

## 8. Recorrido de un viaje

### 8.1 Antes de salir (CD, durante la carga nocturna)

- **Asignación:** M4 asigna carga de frío solo a camiones con kit operativo y autorización sanitaria vigente (RSA 68).
- **Preenfriamiento:** antes del primer escaneo de carga, el aire del compartimento debe estar en la temperatura de la familia (Codex §4.7). Si no lo está, M5 no habilita la carga de frío en ese camión y M4 reasigna.
- **Manifiesto del viaje:** al cargar, M5 escanea cada SSCC y arma el manifiesto: compartimento, familia, regla vigente y sensores. El manifiesto firmado llega al gateway por su sombra y al TC58e.
- **Chequeo previo**, integrado al cierre de carga y no a la ventana de 05:30–07:00:
  - sondas y simuladores sanos; sensor independiente y termógrafo registrando y asociados al camión por escaneo;
  - gateway e Iridium Edge respondiendo; UPS cargada;
  - manifiesto y reglas cargados;
  - termómetro exterior del equipo de frío legible (RSA 68).
- **Salida degradada:** si el gateway falla y no hay kit de reserva, el camión **sale igual**: el TC58e lee el termógrafo y el sensor independiente por Bluetooth y evalúa la regla, que es el funcionamiento que hoy describe el SD4. M9 marca ese viaje como «vigilancia reducida» y avisa a Calidad. El despacho de la mañana no se detiene.

### 8.2 Tiempo fuera de frío en el andén

- Cada SSCC de frío se escanea **al salir de la cámara** (MC9400 en la puerta de la cámara; escaneo nuevo) y **al cargarse en el camión** (escaneo de carga existente).
- M5 calcula los minutos fuera de frío. Si el SSCC espera en una antecámara refrigerada con sensor de cámara, ese tiempo cuenta como frío.
- Calidad fija el máximo por familia. Si un SSCC lo supera, **queda bloqueado antes de salir** (RF‑09.06). El camión sale con el resto.
- El tiempo se suma a la historia térmica del SSCC (§4).

### 8.3 En ruta y ante una falla del equipo de frío

Medición, decisión local, alerta en cabina y transmisión según §5 a §7. Si el equipo de frío del camión falla, **no se pierde automáticamente toda la carga**:

1. **Aviso temprano.** El aire de la caja sube primero. Con la puerta cerrada, más de 10 min fuera de rango da ADVERTENCIA de probable falla del equipo (§7.2). En ese momento el producto todavía está bien: los simuladores, igual que el alimento, se calientan más lento que el aire.
2. **Cuánto tiempo queda.** Con la tendencia de los simuladores, el gateway estima para cada familia a bordo los minutos que faltan para cruzar su regla, y los muestra al conductor y a despacho [I; la velocidad real de calentamiento la mide V4].
3. **Qué hace despacho**, según el procedimiento de contingencia de la ruta, aprobado de antemano: reiniciar o reparar el equipo si se puede; trasbordar el frío a otro camión con frío cercano; o volver al CD. Si hay tiempo y la regla lo permite, adelantar las entregas de frío más cercanas.
4. **Qué queda retenido.** Solo los SSCC todavía a bordo cuya familia superó su regla. Lo ya entregado no se afecta, los productos con más tolerancia pueden seguir y lo seco sigue su ruta.
5. **Si el equipo no se recupera y no hay trasbordo,** con el tiempo la caja supera todas las reglas y entonces sí se retiene todo el frío que queda a bordo. Es lo correcto: entregar ese producto es justamente el riesgo sanitario y comercial del caso de los CLP 21 millones.

### 8.4 Al bajar cada SSCC de frío

- El conductor **escanea el SSCC al bajarlo del camión** (escaneo nuevo, solo para frío). En ese momento el TC58e verifica: latido válido de menos de 30 s, ninguna retención sobre ese SSCC, ninguna contradicción vigente y manifiesto vigente.
- Si todo está en orden, el SSCC queda **habilitado para entregar**. El POD puede registrarse después **dentro del local**, aunque el TC58e ya no alcance el Wi‑Fi de la cabina.
- Si el SSCC vuelve al camión (rechazo o local cerrado), se escanea de nuevo y retoma su compartimento.
- Un SSCC retenido aparece **en rojo** en el TC58e, con la instrucción de no entregarlo.

### 8.5 En la puerta del cliente

- El TC58e muestra la curva del compartimento hasta la bajada del SSCC, con su antigüedad.
- Si el cliente rechaza por sospecha de ruptura, el rechazo queda ligado al tramo entre la entrega anterior y la actual (RF‑09.07), sin usar GPS.

### 8.6 Regreso al CD

- El TC58e descarga por Bluetooth el termógrafo y el sensor independiente, verifica su integridad, firma el hash y lo sube.
- Solo con la confirmación de la nube se libera la memoria de los registradores.
- M9 concilia las tres series (gateway, sensor independiente y termógrafo). Cada hueco abre una falla de integridad.
- Lo retenido se segrega en el andén y Calidad decide.

### 8.7 Expediente y retiro

- En ≤ 2 h tras el regreso queda el **expediente certificado** del viaje: curva certificada, serie operativa, serie independiente, eventos, decisiones y POD.
- Para un retiro sanitario, M9 cruza lote → SSCC → viaje → historia térmica en minutos (criterio n.º 1, < 2 h).

### 8.8 Ruptura confirmada: qué pasa realmente

Una ruptura queda **confirmada** cuando un simulador cumple el criterio de crítica de su familia, o cuando hay una contradicción entre el gateway y el sensor independiente y Calidad la confirma. Desde ese momento el producto afectado **no se puede distribuir ni vender** mientras no se determine que es apto: el RSA prohíbe la tenencia, distribución y comercialización de alimentos alterados (art. 102).

| # | Fase | Cuándo | Qué pasa | Quién | Registro |
|---|---|---|---|---|---|
| 1 | Retención en ruta | Segundos | Los SSCC afectados quedan RETENIDOS en el TC58e. El conductor los aparta dentro de la caja y sigue entregando lo no afectado | Sistema y conductor | M9 (incidente) y M6 |
| 2 | Aviso | ≤ 2 min por red móvil; ≤ 5 min por satélite | Calidad y despacho reciben el incidente con la curva y la lista de SSCC y pedidos afectados | M9 | M9 |
| 3 | Contingencia | Minutos | Despacho decide trasbordo, retorno o seguir solo con lo no afectado (§8.3) | Despacho | M4 y M6 |
| 4 | En la puerta del cliente afectado | Al llegar | Se entrega lo no afectado. Las líneas retenidas quedan «no entregadas, motivo: cadena de frío», con la curva como respaldo | Conductor | M6 (POD con diferencias) |
| 5 | Pedido y documentos | Mismo día | M7 y M8 concilian la entrega y el ERP emite el ajuste tributario que corresponda, según el flujo del SD4 (4.1, articulación entre POD y DTE). M4 programa la reposición en la ruta siguiente | M6, M7, M8, ERP y M4 | ERP y M8 |
| 6 | Regreso al CD | Al volver | Lo retenido baja a un área de productos no aptos, separada y marcada con una X roja u otro signo inequívoco (RSA art. 105). M2 lo deja BLOQUEADO: no se puede preparar ni vender | Bodega | M2 y M8 |
| 7 | Disposición | Al regreso, o antes si Calidad decide en ruta | Ver la tabla siguiente | Calidad | M9, M8 y ERP |
| 8 | Lo ya entregado | Al conciliar las tres series | Si la conciliación muestra que la ruptura empezó antes de lo detectado, M9 lista los SSCC entregados en ese intervalo y sus clientes, y Calidad evalúa el retiro (criterio n.º 1: < 2 h) | M9 y Calidad | M9 |
| 9 | Camión | Mismo día | El camión queda «sin frío apto» en M4 hasta verificar la reparación con un preenfriamiento y un chequeo del kit. Si es de un transportista, se le informa con la evidencia | M4 y Operaciones | M4 |
| 10 | Expediente | ≤ 2 h tras el regreso | Curvas de las tres series, línea de tiempo, SSCC y pedidos afectados, decisiones firmadas, POD y fotos de la segregación. Sirve ante la autoridad, el cliente, el transportista y el seguro | M9 | S3, 5 años |
| 11 | Aprendizaje | En la semana | Análisis de causa sin culpa; indicadores en M10 (excursiones y mermas por camión, ruta y equipo); ajuste de reglas o del mapeo si corresponde | Calidad y LafroX | M10 |

**Disposiciones posibles** (decide Calidad, nunca el conductor; RNG‑04):

| Disposición | Cuándo | Cómo |
|---|---|---|
| **Liberar** | La evaluación muestra que el producto sigue apto: la excursión quedó dentro de lo que tolera según su ficha o según el proveedor | Vuelve a stock. INN‑03 recalcula su vida útil remanente y M2 lo prioriza por FEFO |
| **Vender con descuento** | Solo si Calidad lo libera como apto, por ejemplo con menor vida útil remanente | M8, «venta con descuento». Un alimento alterado no se puede vender (RSA art. 102) |
| **Devolver al proveedor** | Si hay acuerdo con el proveedor | M8, «devolución al proveedor» |
| **Uso no alimentario o alimento animal** | No apto para consumo humano | Solo con desnaturalización autorizada por la autoridad sanitaria (RSA art. 105) |
| **Destruir** | No apto y sin otro destino | Destrucción autorizada y disposición final en un recinto adecuado (RSA art. 105). M8, «destrucción» |

**Congelados que se descongelaron:** no se pueden volver a congelar para venderlos como congelados. El RSA exige rotularlos «producto descongelado, no volver a congelar», y solo un establecimiento autorizado puede descongelar para la venta (art. 192). En la práctica, un congelado que superó su regla no vuelve a stock como congelado [I; Calidad lo confirma con la autoridad sanitaria].

---

## 9. Qué ve el conductor

| Estado | Cabina | TC58e | Qué hace el conductor |
|---|---|---|---|
| NORMAL | — | Verde | Entrega |
| ADVERTENCIA | Luz y zumbador | Amarillo, con la causa probable | Corrige (cierra la puerta, revisa el equipo) y sigue entregando |
| CRÍTICA / RETENIDO | Luz y zumbador | SSCC afectados **en rojo**; no permite habilitarlos | No entrega lo retenido; sigue con el resto |
| NO CONFIABLE | El TC58e suena y vibra | Todo el frío del compartimento en rojo | No entrega el frío de ese compartimento hasta que vuelva el latido o decida Calidad |

**El bloqueo es informático:** impide registrar la entrega, no abrir la puerta. Lo complementan el rojo en el TC58e, la capacitación del conductor (RT‑22.04) y el registro: una entrega sin POD aparece como no realizada y avisa al supervisor.

---

## 10. Avisos, escalamiento y decisión de Calidad

### 10.1 Avisos

- El escalamiento parte cuando M9 guarda el evento (A2). El tiempo total se informa desde la detección.
- **ADVERTENCIA:** aviso en la app de Calidad, SMS y WhatsApp.
- **CRÍTICA, NO CONFIABLE, contradicción o «kit sin reportar»:** además, llamada de voz.
- Dos relojes: sin **acuse** (respuesta con el código del incidente) se escala al segundo nivel; sin **acción** se escala a la jefatura y a despacho.
- Canales: SMS por SNS; WhatsApp por la integración INT‑11; voz por AWS End User Messaging (Chile admite voz [H]).

### 10.2 Quién decide y cuándo

- **La decisión nunca es urgente para la operación:** lo retenido queda apartado y el camión sigue entregando el resto.
- **Acción por defecto:** si nadie decide en el plazo de la familia, lo retenido **sigue retenido y vuelve al CD**. Calidad decide al regreso con la curva completa. La acción por defecto nunca libera producto (RNG‑04).
- **Responsable de llamada:** para los casos en que conviene decidir en ruta (por ejemplo, un cliente de food service esperando un pedido grande), se avisa a la persona de Calidad de turno, según una lista rotativa del personal existente que define Puelche. No se crea una guardia nueva.

### 10.3 Orden de Calidad

- Calidad decide en M9 con segundo factor (Keycloak) y **ve la revisión de estado** sobre la que decide.
- La orden se firma con AWS KMS (ECDSA P‑256) y ocupa ≤ 125 bytes, por lo que cabe en un mensaje satelital de bajada (270 bytes) [I].
- Llega al TC58e por **su propio celular** (SIM del MDM), por el gateway con celular o, sin celular, **por satélite a través del gateway**.
- El TC58e la aplica solo si: el incidente sigue abierto; la versión es mayor que la última aplicada; no caducó; la revisión de estado coincide con la evaluada; y el compartimento ya volvió al rango. **Disposición sanitaria** («el producto está apto») y **autorización para entregar ahora** son cosas distintas.
- Ante cualquier duda, el producto sigue retenido.

---

## 11. Qué pasa cuando algo falla

**Garantía de diseño (a demostrar en §17):** ninguna falla de un solo componente del kit permite **entregar** un SSCC posiblemente comprometido. No cubre la destrucción física del camión ni dos fallas independientes a la vez. Estar sin señal no es una falla: es una condición normal y se prueba combinada con fallas de equipo.

| Falla | Quién la detecta | Qué ocurre | ¿Se protege el producto? |
|---|---|---|---|
| Sin red móvil | — | Todo sigue por satélite, que transmite siempre | Sí |
| Sin red móvil ni cielo (túnel, quebrada) | — | Detecta, alarma y frena la entrega igual; el aviso a Calidad sale con la primera señal o el primer cielo | Sí |
| Falla del equipo de frío | Gateway (aire con la puerta cerrada) | Advertencia temprana, minutos restantes por familia y plan de §8.3 | Sí |
| Gateway apagado | TC58e (sin latido en 30 s) | NO CONFIABLE y retención; la nube alerta «kit sin reportar» | Sí |
| Gateway con la lectura congelada | TC58e (latido de frescura) | Retención en ≤ 30 s | Sí |
| Gateway mide mal (sondas o módulo) con valores plausibles | TC58e (sensor independiente) | Retención por contradicción | Sí |
| Gateway decide mal y dice NORMAL | TC58e (misma regla sobre el sensor independiente) | Retención por contradicción | Sí |
| Sensor independiente o termógrafo caídos | TC58e | El gateway sigue protegiendo; se informa | Sí |
| Iridium Edge caído | Gateway | Todo sigue por la red móvil; en zona sin red, el aviso espera la señal | Sí |
| Wi‑Fi de cabina caído | TC58e | NO CONFIABLE; no se habilita la bajada de frío | Sí |
| TC58e reiniciado o reemplazado | TC58e | Arranca en NO CONFIABLE hasta recuperar del gateway el manifiesto, las retenciones y las decisiones aplicadas | Sí |
| Cae AWS sa‑east‑1 | Monitoreo externo | El gateway conserva 72 h de lo confirmado y lo reenvía; la conmutación a us‑east‑1 sigue el SD4 4.3.2 | Sí; el aviso depende del respaldo |

---

## 12. Nube

| Elemento | Detalle |
|---|---|
| **Ingesta por celular** | AWS IoT Core, MQTT sobre TLS, un certificado por camión con aprovisionamiento de flota de Greengrass. Regla → SQS |
| **Ingesta por satélite** | Opción preferida: Iridium CloudConnect, con colas SQS en nuestra cuenta para mensajes de subida, de bajada, confirmación y error; Iridium indica que funciona en todas las regiones de AWS [H, fuente del proveedor]. No se encontró un distribuidor latinoamericano que lo ofrezca [C]. Alternativa: el servicio SBD estándar del proveedor entrega por conexión directa a un receptor en ECS, que deja los mensajes en la misma cola. Segundo destino en us‑east‑1 [C] |
| **M9** | Descarta duplicados por camión, arranque y secuencia. Guarda el evento y la obligación de avisar en la misma transacción de Aurora (bandeja de salida del SD4) y responde A2. Reemplaza los lotes satelitales por la serie fina cuando llega |
| **Posición** | El registro de temperatura no guarda GPS. La posición se usa solo para el reloj del gateway |
| **Serie operativa** | DynamoDB N‑06, 30 días, réplica en us‑east‑1 |
| **Registro de 5 años** | S3 con bloqueo de objetos en modo cumplimiento: temperaturas 5 años y evidencia de entrega 6 años (RT‑05.10). Los archivos de los registradores se guardan tal como se descargan, y sus lecturas también como registros para consultarlas |
| **Tablero** | Temperatura del día con ≤ 5 min de demora por celular o por satélite (RT‑05.29). Sin ningún camino, el tablero muestra la última curva recibida con su antigüedad (operación degradada declarada) |
| **Archivo post‑A2** | El gateway conserva 72 h la copia de lo confirmado, o hasta que la plataforma confirme la réplica en us‑east‑1 |
| **Reloj** | GNSS del gateway como fuente principal y NTP como secundaria. Los intervalos se miden con reloj monótono. Si la hora no es confiable, las órdenes se validan por versión y revisión de estado, nunca por hora |
| **Credencial de 14 h** | Se renueva a las 12 h por cualquier camino IP. Sin celular rige el SD4: lo capturado se conserva y las nuevas operaciones protegidas esperan la renovación (operación degradada) |

---

## 13. Cómo lo montamos

### 13.1 Qué se construye

| Pieza | Trabajo |
|---|---|
| Componentes de Greengrass | Reutilizar la regla térmica de los CD; desarrollar el latido y el componente satelital |
| M9 | Manifiesto viaje–compartimento–SSCC, retenciones por SSCC, tiempo en andén, conciliación de las tres series, orden firmada, acción por defecto y escalamiento |
| App del TC58e | Latido, doble evaluación, lectura Bluetooth del sensor independiente y del termógrafo, escaneo de bajada, retención en rojo, aplicación de órdenes |
| Infraestructura como código | IoT Core, aprovisionamiento de flota, CloudConnect y sus colas, reglas, KMS y alarmas de monitoreo |

### 13.2 Banco de pruebas

Un kit completo con una caja térmica de ensayo en el laboratorio de LafroX: V1–V3, V5–V8, V11, V13, V14, V16, V17 y V19 (§17), antes de tocar un camión.

### 13.3 Mapeo térmico

Por cada tipo de carrocería: camión cargado con producto de ensayo, aperturas de puerta como en una ruta urbana, comparación entre núcleo de producto, simuladores y aire (V4). Resultado: punto crítico, volumen de las botellas y tolerancias de la doble evaluación.

### 13.4 Instalación física en cada camión

| Lugar | Qué se instala |
|---|---|
| Cabina | Gabinete del gateway y la UPS (detrás del asiento o bajo la consola); luz y zumbador en el tablero; el TC58e en su soporte existente |
| Techo de la carrocería refrigerada, en el frente (el punto más alto del camión) | Iridium Edge (antena integrada) y antena de red móvil y GNSS, con vista despejada del cielo; cables a la cabina por un pasacables sellado |
| Pared frontal de la carrocería, la que da a la cabina | Pasamuros sellado para los cables de las sondas; módulo de sondas en una caja estanca del lado de la cabina |
| Interior de la carrocería | Sonda de aire en la boca del evaporador; simulador crítico y sensor independiente juntos en el punto del mapeo; simulador secundario al centro; termógrafo en el aire, en el punto del mapeo |
| Puertas de carga | Sensor magnético en cada una |
| Alimentación | Desde la batería del camión, con fusible y corte por bajo voltaje; ignición a una entrada digital |

La instalación la hace un taller automotriz con procedimiento escrito y lista de verificación. Tiempo por camión: medio día [E].

### 13.5 Puesta en marcha de cada camión

1. Aprovisionamiento del gateway en la flota de Greengrass (certificado propio).
2. Asociación del sensor independiente y del termógrafo al camión por escaneo.
3. Chequeo completo (§8.1) y prueba de alarma con una excursión simulada.
4. Acta de recepción por camión.

### 13.6 Piloto y despliegue

- **Piloto:** 6 semanas en 4 camiones (dos de rutas rurales, uno urbano y uno de transportista), con V18 en rutas reales.
- **Despliegue:** los 28 camiones antes de que parta la ola de reparto (T‑18), al ritmo de medio día por camión y taller [E].
- **Operación:** actualizaciones por despliegues de Greengrass, por etapas y con reversión; calibración anual; revisión del glicol y de las baterías de los sensores.

---

## 14. Alternativas evaluadas y por qué no se eligieron

Todas se descartaron por razones técnicas, no de precio.

### 14.1 Medición y decisión

| Alternativa | Por qué no mejora el diseño |
|---|---|
| Decidir con la sonda de aire | Falsas alarmas en cada apertura de puerta; el RSA fija límites sobre el producto |
| Sonda de núcleo que perfora el producto | Destructiva; no aplica a producto envasado en reparto |
| Termógrafo leído por el TC58e como única medición (SD4 actual) | El terminal se baja con el conductor; sin aviso remoto sin cobertura; la revisión del Informe 1 lo objetó. Se conserva como **salida degradada** |
| Telemetría del propio equipo de frío (marcas de reefer) | Marcas distintas en 28 camiones, incluidos los de transportistas; datos en la nube del fabricante; sin vínculo con el SSCC; no todos los equipos la tienen |

### 14.2 Borde

| Alternativa | Por qué no mejora el diseño |
|---|---|
| Router Teltonika RUT956 con aplicación propia (v8) | Viable, con filial en Chile y homologación vehicular E‑mark, pero obliga a programar la cola, los reintentos, los certificados y las actualizaciones que Greengrass ya resuelve, y deja dos plataformas de borde distintas (cámaras y camiones). Queda como **alternativa** si el UC‑8200 no aprueba V1 o V5 |
| Segunda cadena con hardware propio: alarma independiente y transmisor FMC650 con su satélite (v8) | Duplica equipos para lo que el TC58e y un sensor independiente ya cubren (§3.1 y §11). Además, el satélite del FMC650 solo envía el estado de sus entradas, sin curva ni órdenes |
| Plataforma comercial de flota (Webfleet, Wialon) | Orientada a la posición; la temperatura queda en la nube de un tercero; sin retención local por SSCC |
| Bloqueo físico (cerradura electrónica en la caja) | Sobreingeniería: el bloqueo por SSCC en el TC58e, el rojo y la capacitación cubren el riesgo; una cerradura afecta a la operación y a los camiones de terceros |
| Predicción con inteligencia artificial en el camión | Sobreingeniería: la estimación de vida útil ya está en la nube (INN‑03) |

### 14.3 Satélite

| Alternativa | Por qué no mejora el diseño |
|---|---|
| Starlink Mini u OneWeb (internet satelital) | Banda ancha que la cadena de frío no usa. La banda Ku necesita una vista amplia del cielo y se degrada más bajo el follaje que la banda L de Iridium; antena mayor; 20–40 W (Mini) o 75–100 W (Performance) [H]. No mejora ni la alarma ni la curva de 3 min |
| Iridium Certus | Internet de banda estrecha con terminal mayor; no aporta para mensajes de 43 bytes |
| Inmarsat o Viasat IsatData Pro (satélite geoestacionario; Globalsat Chile lo ofrece [H]) | Técnicamente viable, pero el satélite geoestacionario está siempre en la misma dirección, hacia el norte: un cerro o una ladera en esa dirección lo bloquea durante todo el tramo. Los satélites de Iridium pasan en órbita baja con ángulos que cambian [I] |
| Myriota (satélite IoT de bajo consumo; Globalsat Chile [H]) | Latencia de hasta 30–35 min [H] |
| NB‑IoT satelital | Sin oferta comercial confirmada en Chile [C] |
| Satélite al celular (Entel‑Starlink) | Solo en teléfonos de una lista que no incluye Zebra [H]; sin integración |

### 14.4 Operación

| Alternativa | Por qué no mejora el diseño |
|---|---|
| Bloquear el camión completo ante una excursión | Contradice la restricción del Caso: el despacho de la mañana no se detiene |
| Guardia de Calidad de 05:30 a 20:00 | Innecesaria con la acción por defecto (§10.2); RNG‑04 se cumple igual |
| Guardar la posición GPS con la temperatura | No aporta a la cadena de frío; la geolocalización de personas se guarda solo 12 meses (RT‑05.10) |

### 14.5 Comparación de soluciones completas

| Criterio | SD4 actual (termógrafo + TC58e) | Gateway solo con red móvil | Gateway + Starlink | Telemetría del equipo de frío | Plataforma de flota (Webfleet, Wialon) | v8 (dos cadenas de hardware) | **v9 (esta)** |
|---|---|---|---|---|---|---|---|
| Registro certificado continuo | Sí | Sí | Sí | Depende de la marca | Depende del sensor | Sí | **Sí** |
| Alerta con red móvil | Solo con el conductor en la cabina | Sí | Sí | Sí | Sí | Sí | **Sí** |
| Alerta sin red móvil | No | No | Solo con cielo despejado | No | Solo posición | Solo estado | **Sí** |
| Curva sin red móvil (RT‑05.29) | No | No | Solo con cielo despejado | No | No | No | **Sí, cada 3 min** |
| Calidad decide en ruta sin red móvil | No | No | Solo con cielo despejado | No | No | No | **Sí** |
| Protege si el equipo principal falla o mide mal | No | No | No | No | No | Sí | **Sí** |
| Retención por SSCC | Parcial | Sí | Sí | No | No | Sí | **Sí** |
| Sin falsas alarmas por puertas | No | Sí, con simuladores | Sí, con simuladores | No | No | Sí | **Sí** |
| Mismo software que las cámaras | No | No | No | No | No | No | **Sí** |
| Tipos de equipo por camión (sin contar SIM) | 1 | 9 | 10 | 0–1 | 2–3 | 13 | **10** |

La v9 es la única que cumple todas las filas. Tiene menos tipos de equipo que la v8 y los mismos que la opción con Starlink, que no cumple tres filas.

### 14.6 Qué garantiza el diseño y qué no

**Ningún sistema es infalible.** El diseño garantiza esto, a demostrar en las pruebas de §17:

1. **Ninguna falla de un solo componente permite entregar producto posiblemente comprometido.** Si falla el gateway, lo detecta el TC58e. Si mide o decide mal, lo detecta el sensor independiente. Si falla el TC58e, el conductor no puede registrar entregas hasta usar uno de reserva.
2. **Todo queda registrado**, con o sin red, y se concilia al regreso con el termógrafo certificado.
3. **La alarma llega en ≤ 2 min con red móvil y en ≤ 5 min por satélite**, en los porcentajes de §18.

**Lo que no garantiza, y se declara:**

- **Dos fallas independientes a la vez**, por ejemplo el gateway y el TC58e en el mismo viaje.
- **Túneles, quebradas y bosque denso sin red móvil ni cielo:** la alarma en la cabina y el bloqueo de la entrega ocurren igual, porque no dependen de la red. Lo que espera es solo el **aviso a Calidad**, que sale con la primera señal o el primer cielo; V18 mide cuánto dura eso como máximo.
- **Descarga a mano ignorando el sistema:** el bloqueo es informático; lo cubren el rojo en el TC58e, la capacitación y el registro de la entrega sin POD.
- **La calidad de la regla:** el sistema aplica la regla que Calidad aprueba; una regla mal definida da decisiones malas.
- **Se mide la caja, no cada envase:** los simuladores representan al producto en el punto crítico que fija el mapeo, no a cada unidad.

---

## 15. Equipos y disponibilidad en Chile

**Regla:** ningún equipo entra al T‑11 sin cotización escrita de un proveedor con domicilio en Chile, certificación Subtel cuando emita radio y, para los registradores, certificado EN 12830 del modelo.

| Equipo | Candidato | Presencia en Chile | Falta confirmar |
|---|---|---|---|
| Gateway | Moxa UC‑8200 con LTE (familia del B‑02) | **Techvalue**, Antonio Varas 894, Providencia, Santiago: «representante oficial de Moxa para Chile y Perú», con líneas de gateways IIoT y computadores [H] | Cotización, Wi‑Fi como punto de acceso, Greengrass V2 instalado (V1), comportamiento vehicular (V5) |
| Gateway alternativo | Teltonika RUT956 | **Teltonika de Chile** [H]. Tiene homologación vehicular E‑mark (ECE R10, como subconjunto electrónico) [H] | Desarrollo propio en lugar de Greengrass (§14.2) |
| Módulo de sondas | Moxa ioLogik E1260‑T | **Techvalue** (misma marca que el gateway) [H] | Cotización |
| Módem satelital | Iridium Edge y servicio SBD | **Globalsat Chile**, Santiago: socio de Iridium; ofrece Iridium Edge, SBD y M2M [H] | Stock, plan por mensaje y forma de entrega: CloudConnect o conexión directa (§12) |
| Sensor independiente y termógrafo | Teltonika EYE SENSOR EN12830, −20…+60 °C | **Teltonika de Chile** [H] | Stock, certificado, lectura en vivo y descarga desde la app del TC58e |
| Registradores para congelado bajo −20 °C | Sensitech TempTale Ultra BLE (−30…+70 °C, Bluetooth, calibración trazable a NIST, modo de uso múltiple [H]) o ELA Blue PUCK T EN12830 (−40…+85 °C [H]) | Sensitech: filial chilena Comercial Sensitech South America Ltda. [H]. ELA: sin distribuidor en Latinoamérica; solo importación [H] | Sensitech no publica certificación EN 12830 [C]; protocolo Bluetooth para la app del TC58e [C]. Antes, confirmar cuántos compartimentos viajan bajo −20 °C: el Caso no lo dice |
| Sondas PT100 y botellas de glicol | Instrumentación genérica | Uso común; no se encontró una tienda específica [C] | Cotización local; volumen según V4 |
| UPS, acondicionador de energía, sensor de puerta, luz y zumbador | Genéricos automotrices | Uso común [C] | Cotización local |
| TC58e | Zebra (existente) | SD4 [H] | — |

**Certificación Subtel.** Hay dos trámites [H]:
- **Equipos de alcance reducido** (Bluetooth, Wi‑Fi y dispositivos IoT, como el EYE SENSOR y el Wi‑Fi del gateway): certificación gratuita de Subtel, con respuesta en 20 días hábiles.
- **Equipos que usan la red móvil** (el módem LTE del gateway): homologación multibanda ante una entidad homologadora; un laboratorio informa unas 8 semanas.

La solicitud la presenta el fabricante o el proveedor. El T‑11 exige el certificado en la entrega, y el cronograma (SD7) reserva ese plazo antes del banco de pruebas. Para el Iridium Edge, el certificado lo entrega Globalsat Chile [C].

---

## 16. Cantidades y dimensionamiento

Base: `Dimensionamiento/dimensionamiento/calculo.py` (fuente única del SD4): 28 camiones con frío (18 propios y 10 de transportistas); ventana de ruta de 14,5 h = 870 min; 145 bytes por lectura; factor de almacenamiento 0,25; reserva del 10 % por tipo, redondeada hacia arriba (BTT §8.4); la flota con frío no crece (S‑38).

### 16.1 Cantidades

| Componente | Por camión | Instalados | Reserva | **Total** | T‑11 hoy |
|---|---|---|---|---|---|
| Termógrafo EN 12830 en aire (B‑03) | 1 por compartimento (base 1) | 28 | 3 | **31** | 31 (misma cantidad; cambian modelo, intervalo y función) |
| Sensor independiente EN 12830 en glicol | 1 por compartimento | 28 | 3 | 31 | — |
| Gateway con Greengrass | 1 | 28 | 3 | 31 | — |
| Módulo de sondas | 1 | 28 | 3 | 31 | — |
| Sondas PT100 (1 aire + 2 simuladores) | 3 | 84 | 9 | 93 | — |
| Botellas simuladoras (2 del gateway + 1 del sensor independiente) | 3 | 84 | 9 | 93 | — |
| Iridium Edge | 1 | 28 | 3 | 31 | — |
| Antena LTE/GNSS | 1 | 28 | 3 | 31 | — |
| Sensor de puerta (1 por puerta de carga; base 1) | 1 | 28 | 3 | 31 | — |
| Luz y zumbador de cabina | 1 | 28 | 3 | 31 | — |
| UPS del kit | 1 | 28 | 3 | 31 | — |
| Protección de alimentación | 1 | 28 | 3 | 31 | — |
| SIM M2M (doble SIM del gateway) | 2 | 56 | 6 | 62 | — |

- Las bases «1 por compartimento» y «1 por puerta» se ajustan con el inventario real de carrocerías. Un compartimento adicional suma 3 sondas, 3 botellas, 1 termógrafo y 1 sensor independiente.
- El contacto de alarma del equipo de frío no es una compra: se cablea si el equipo lo tiene.
- Los TC58e (110 + 11) no cambian.

### 16.2 Mensajes por día (INT‑05)

| Concepto | Actual (SD4) | Nuevo | Cálculo |
|---|---|---|---|
| Lecturas de cámaras | 6.048 | 6.048 | 21 × 288 (sin cambio) |
| Mensajes del gateway por celular | — | 24.360 | 28 × 870 (uno por minuto con las 3 sondas) |
| Eventos | — | 112 | 28 × 4 [E] |
| Descargas de los registradores (termógrafo y sensor independiente) | — | 28 | Una por camión y día |
| Lecturas de termógrafo reenviadas en vivo | 4.872 | — | Ya no se reenvían en vivo; llegan en la descarga |
| **INT‑05, mensajes/día** | **10.920** | **30.548** | + 19.628 |
| **Total de integraciones** (4.2.11 y Anexo 4‑I) | **224.652 / 342.933** | **244.280 / 362.561** | + 19.628 en régimen y en peak |
| Total bruto de `calculo.py` | 230.252 / 353.333 | 249.880 / 372.961 | + 19.628 |

Los mensajes satelitales van aparte (§6.4): 8.120 al día en la flota, porque el satélite transmite toda la jornada.

### 16.3 Almacenamiento y datos

| Concepto | Actual | Nuevo |
|---|---|---|
| Lecturas de temperatura por día | 10.920 | **127.848** (6.048 de cámaras + 73.080 de sondas + 24.360 de termógrafos + 24.360 de sensores independientes) |
| Temperatura, crudo por año | 0,58 GB | **6,77 GB** |
| Temperatura, almacenado por año (factor 0,25) | 0,14 GB | **1,69 GB** |
| Temperatura, crudo en 5 años | 2,89 GB | **33,83 GB** |
| DynamoDB N‑06 (30 días) | 0,048 GB | **0,556 GB** |
| Datos celulares del gateway (≈ 300 bytes por mensaje con TLS) | — | ≈ 261 KB/día y ≈ 6,8 MB/mes por camión |

El volumen crece unas 11,7 veces en lecturas, pero sigue siendo pequeño: 30.548 mensajes al día son 0,35 por segundo en promedio. **No cambia** la elección de IoT Core, DynamoDB ni S3, ni el ancho de banda de los sitios.

### 16.4 Lugares del SD4 que cambian si se adopta (no aplicado)

Solo el SD4. Los demás subdocumentos están en §22.

| Archivo | Líneas | Cambio |
|---|---|---|
| `04/partes/4.1_logica/02_especificaciones_tecnologias_de_software_a_utilizar.tex` y `08_detalle_de_tecnologias_seleccionadas.tex` | — | 4.1.1: Greengrass también en el camión, Iridium SBD y CloudConnect; alternativas de §14 |
| `04/partes/4.1_logica/04_capas_de_la_arquitectura.tex` | 156 | Reemplazar «No se instala en camiones» por el gateway con Greengrass en cada camión y la doble evaluación en el terminal |
| `04/partes/4.1_logica/05_modulos_funcionales_y_limites_de_contexto.tex` | 45, 52 y 55 | Puntos de medición, integración del kit, termógrafo cada 1 min y simuladores de producto |
| `04/partes/4.1_logica/07_catalogo_de_interfaces.tex` | — | INT‑05 con dos caminos: celular y satélite, en ambos sentidos |
| `04/partes/4.1_logica/12_registro_de_decisiones_de_arquitectura.tex` y Anexo 4‑O (`18_anexo_4_1_o_decisiones_logicas.tex`) | — | ADR nuevo: borde Greengrass en el camión, celular y satélite Iridium; alternativas de §14 |
| `04/partes/4.1_logica/13_puntos_unicos_de_falla_y_riesgos_residuales.tex` | — | Matriz de §11 y riesgos residuales de §19 |
| `04/partes/4.1_logica/16_funciones_disponibles_y_no_disponibles_sin_conexion.tex` | — | Sin celular: protección local completa, curva y órdenes por satélite |
| Anexo 4‑A (`02_anexo_4_1_a_catalogo_de_eventos_canonicos.tex`) | — | Eventos nuevos: advertencia, crítica, retención por SSCC, contradicción, NO CONFIABLE, kit sin reportar, orden de Calidad aplicada o rechazada |
| Anexo 4‑G (`08_anexo_4_1_g_catalogo_de_interfaces_internas.tex`) | 46 | INT‑05: nuevo volumen, un mensaje por minuto, lote satelital cada 3 min |
| Anexo 4‑I (`10_anexo_4_1_i_volumen_de_mensajes.tex`) | 14 y 25 | Igual que 4.2.11 |
| Anexo 4‑N (`15_anexo_4_1_n_correspondencia_de_componentes_logicos.tex`) | — | Correspondencia M9 ↔ gateway del camión, CloudConnect y N‑08 |
| Anexo 4‑P (`19_anexo_4_1_p_tecnologias_soporte.tex`) | — | Despliegues de Greengrass para la flota de camiones |
| Anexo 4‑Q (`20_anexo_4_1_q_modelado_amenazas.tex`) | — | Amenazas del kit: suplantación del camión, latido falso, orden repetida, mensaje satelital falso, manipulación de los registradores |
| `04/partes/4.2_fisica/02_0_arquitectura_fisica.tex` | 45 | El terminal deja de ser el evaluador principal en ruta |
| `04/partes/4.2_fisica/02_a_emplazamiento.tex` | 132 (figura), 196 y 238 | N‑08, B‑03 y componentes nuevos |
| `04/partes/4.2_fisica/02_b_servicios_nube.tex` | — | CloudConnect y sus colas SQS |
| `04/partes/4.2_fisica/02_c_conexiones.tex` | 27, 30 y 47 | Flujos nuevos: gateway por celular y por satélite; Bluetooth de los registradores al terminal |
| `04/partes/4.2_fisica/04_c_implementos.tex` | — | 4.2.1: resumen del kit y su disponibilidad en Chile |
| `04/partes/4.2_fisica/11_j_despliegue.tex` | — | Actualización por etapas del software de los camiones |
| `04/partes/4.2_fisica/12_k_dimensionamiento.tex` | 123, 140 y 143 | Temperatura: 0,58 → 6,77 GB/año; 2,89 → 33,83 GB en 5 años. INT‑05: 10.920 → 30.548; total 224.652/342.933 → 244.280/362.561 |
| `04/anexos/fisica/16_anexo_4b_memoria_calculo.tex` | 27, 29, 152, 161, 197, 223, 234, 243 y 386 | Dimensiones 9 y 11, implementos, lecturas, totales, telemetría diaria e INN‑03 |
| `04/partes/4.3_centros_de_datos/06_e_sitio_secundario.tex` | — | 4.3.2: CloudConnect con segundo destino en us‑east‑1 y archivo de 72 h en el camión |
| `04/formularios/T11/15_anexo_t11.tex` | 55 | B‑03: EYE SENSOR EN12830 o equivalente, cada 1 min |
| `04/formularios/T11/15_anexo_t11.tex` | 92 | N‑08: 3 gateways de cámara y 28 gateways de camión |
| `04/formularios/T11/15_anexo_t11.tex` | 38 y filas nuevas | 62 SIM M2M; filas nuevas de §16.1 |
| `Dimensionamiento/dimensionamiento/calculo.py` | 83, 162, 408 y 438 | Parámetros nuevos: sondas por camión, sensor independiente, minutos por mensaje, eventos y descargas |
| Figura ARQL‑01 | — | Muestra 230.252 en el total de mensajes: debe actualizarla el equipo en draw.io |

---

## 17. Pruebas de viabilidad (antes de cualquier compra)

Las excursiones de prueba usan carga de ensayo, nunca alimento comercial.

| # | Prueba | Aprobación |
|---|---|---|
| V1 | Gateway con Greengrass: Modbus cada 5 s, regla, Stream Manager, IoT Core con A2, latido por MQTT local, actualización y reversión | Evento completo; sin pérdida tras corte de energía |
| V2 | Iridium Edge manejado por el gateway, sin SIM: alarma, lote de 3 min y orden de bajada | Alarma en ≤ 3 min; lote y orden íntegros según el formato |
| V3 | Sensor independiente y termógrafo: lectura en vivo y descarga de memoria desde el TC58e, intervalo de 1 min | Series completas; certificado EN 12830 del modelo |
| V4 | **Mapeo y simuladores:** camión cargado con producto de ensayo, 15 aperturas de puerta; comparar núcleo de producto, simuladores y aire | Los simuladores siguen al producto dentro de la tolerancia; define punto crítico, volumen y tolerancias |
| V5 | Alimentación en 12 y 24 V: arranque, caída de tensión, desconexión de batería, batería envejecida, temperatura extrema | Autonomía ≥ 24 h, sin reinicios |
| V6 | Gateway sin energía durante una excursión | El TC58e retiene en ≤ 30 s y alarma; la nube alerta «kit sin reportar» |
| V7 | Gateway encendido con la lectura congelada | El latido falla y el TC58e retiene en ≤ 30 s |
| V8 | Error inyectado en la evaluación o en las sondas del gateway | El TC58e retiene por contradicción |
| V9 | Escaneo de bajada y POD dentro del local, fuera del alcance del Wi‑Fi | Se entrega lo habilitado; no se habilita nada con un latido vencido |
| V10 | Turno de 14 h sin celular y reconexión, con POD, fotos, curvas y eventos simultáneos | Lotes satelitales completos; sincronización ≤ 10 min (RT‑03.13) |
| V11 | Duplicados, retrasos y reordenamiento por red móvil y satélite, incluidos un túnel simulado y una crítica que llega tarde | Estado final correcto en el gateway, el TC58e y M9; la crítica tardía retiene o abre la evaluación de retiro |
| V12 | Crítica sin acuse; acuse sin acción; nadie decide | Escalan los dos relojes; se aplica la acción por defecto |
| V13 | Órdenes repetidas, antiguas, caducadas, de otro incidente, con firma inválida, sobre una revisión anterior o con el producto fuera de rango, por celular y por satélite | Todas rechazadas o sin autorización de entrega |
| V14 | TC58e reiniciado, reemplazado o con la base local borrada, sin internet | Ninguna entrega antes de recuperar el estado del gateway |
| V15 | Tiempo fuera de frío en el andén | El SSCC que supera el máximo queda bloqueado antes de salir |
| V16 | Fallas de sonda: abierta, en corto, desviada | Se aplica la matriz de §7.4 |
| V17 | Pérdida de la región justo después de A2 | El evento y su aviso se recuperan desde el archivo de 72 h |
| V18 | Satélite en rutas reales: Empedrado/Chanco/Cauquenes y Pinto/Alto Biobío, con bosque, quebradas y túneles, en verano y en invierno | Porcentaje de mensajes entregados, latencia y duración máxima de cada corte de cielo, medidos por tramo |
| V19 | Orden de Calidad por satélite en una zona sin red móvil | Llega al TC58e y se aplica o se rechaza según §10.3 |
| V20 | Falla del equipo de frío en ruta, con carga de ensayo | Advertencia temprana con la puerta cerrada; minutos restantes por familia; retención solo de lo que supera su regla |
| V21 | Ruptura confirmada de punta a punta: retención, entrega parcial, ajuste tributario, reposición, área de no aptos, disposición y expediente | Cada fase de §8.8 queda registrada y el pedido del cliente se repone |

**Piloto:** 6 semanas en 4 camiones (§13.6). Los porcentajes se acreditan por población (ruta y camino), con cero fallas y 95 % de confianza: ≈ 59 ensayos para ≥ 95 %, ≈ 300 para ≥ 99 % y ≈ 598 viajes para ≥ 99,5 %. Los SLA se fijan en el contrato después de medir los primeros 3 meses de operación.

---

## 18. SLA

| # | Compromiso | Meta |
|---|---|---|
| SLA‑1a | Viajes con registro completo y conciliado | ≥ 99,5 % [P] |
| SLA‑1b | Fallas de integridad gestionadas | 100 % en ≤ 24 h [P] |
| SLA‑2 | Alerta emitida con celular: detección (≤ 35 s) + cabina (≤ 5 s) + A2 (≤ 30 s) + primer canal aceptado (≤ 15 s) | ≤ 2 min en ≥ 99 % |
| SLA‑3 | Alerta emitida por satélite, que transmite siempre, con o sin red móvil | ≤ 5 min en ≥ 95 % [C, V2 y V18] |
| SLA‑4 | Temperatura en los indicadores del día | ≤ 5 min por celular o por satélite (RT‑05.29); sin ningún camino, última curva con su antigüedad (operación degradada declarada) |
| SLA‑5 | Curva en el TC58e al bajar cada SSCC | 100 % |
| SLA‑6 | Retención local ante CRÍTICA, NO CONFIABLE o contradicción | 100 % [a demostrar] |
| SLA‑7 | Expediente certificado conciliado | ≤ 2 h tras el regreso [P] |
| SLA‑8 | Retiro sanitario por lote con historia térmica | < 2 h (criterio n.º 1) |
| SLA‑9 | Plataforma de extremo a extremo | ≥ 99,9 % mensual (SD4) |

Los tiempos de detección se miden desde que **el simulador cruza el umbral**. El retardo del simulador frente al aire es intencional: reproduce el del producto. Por satélite, la curva tiene hasta 3 min de antigüedad al enviarse; con la transmisión y el registro, llega en ≤ 4,5 min [C, V2].

---

## 19. Riesgos residuales declarados

1. **Bloqueo informático:** impide registrar la entrega, no descargar a mano. Mitigación: rojo en el TC58e, capacitación y entrega sin POD como incidente.
2. **Sin red móvil ni cielo** (túneles, quebradas): el camión detecta, alarma y frena la entrega igual; solo el aviso a Calidad espera la primera señal o el primer cielo.
3. **Gateway caído en una zona sin red móvil:** el TC58e alarma al conductor y frena la entrega. Como el satélite transmite cada 3 min, la nube nota el silencio y alerta «kit sin reportar» a los 6 min; no puede saber si es una falla o un corte de cielo hasta que vuelva la señal.
4. **Registradores:** su integridad se verifica en la descarga y el TC58e firma el hash; el CRC por sí solo no autentica [H, NIST].
5. **Desarrollo propio:** el latido, el componente satelital y la doble evaluación en el TC58e (V1, V2, V8).
6. **Gateway sin homologación vehicular:** el UC‑8200 es industrial, no automotriz. Se mitiga con base antivibración, acondicionador de energía y la prueba V5; si V5 falla, se usa la alternativa Teltonika RUT956, que sí tiene E‑mark (§14.2).
7. **Congelados bajo −20 °C:** ningún registrador EN 12830 con distribuidor en Chile cubre ese rango; hay que elegir entre acreditar EN 12830 en Sensitech o importar ELA (§15).
8. **Equipos marcados [C] en §15:** no entran al T‑11 sin cotización local.
9. **Cambio operativo:** dos escaneos nuevos (salida de cámara y bajada de SSCC de frío).

---

## 20. Fuentes (consultadas el 23 y 24‑10‑2026)

**Proyecto:** Caso 02, BTT, Bases Administrativas (art. 50.2), Aclaraciones y revisión del Informe 1 (`Bases/`); SD3 (T‑12, RF‑09.04 a 09.07, RNF‑09.05, RNG‑04, S‑28); Subdocumento 4, T‑11, Anexos 4‑B, 4‑G y 4‑I; ramas vigentes de los demás subdocumentos; `Dimensionamiento/dimensionamiento/calculo.py`.

**Normativa:**
- Reglamento Sanitario de los Alimentos, DS 977/96, texto actualizado a mayo de 2024 (arts. 67, 68, 190, 191 y 303): https://dinta.cl/wp-content/uploads/2024/06/DECRETO_977_96_actualizado_-mayo-2024_DINTA.pdf · versión Minsal: https://www.minsal.cl/wp-content/uploads/2017/04/DECRETO_977_96_actualizado_a-octubre-2016.pdf
- Reglamento (CE) 37/2005: https://www.legislation.gov.uk/eur/2005/37 · https://eur-lex.europa.eu/eli/reg/2005/37/oj/eng
- Codex CAC/RCP 8‑1976 (FAO): https://www.fao.org/4/Y0681E/y0681e07.htm
- FDA, 21 CFR 1.908: https://www.law.cornell.edu/cfr/text/21/1.908

**Simuladores de producto (fuentes de fabricantes):**
- Primex, especificaciones de Thermobuffer: https://support.primexinc.com/hc/en-us/articles/360052788694-Thermobuffer-specifications
- Copeland (Cooper‑Atkins), simulador sólido: https://d1-live.copeland.com/documents/product-sheet-nist-traceable-vial-solid-buffered-probe-en-8123544.pdf
- Kelsius, aire frente a producto: https://kelsius.com/tag/cold-chain-logistics/

**Equipos, servicios y proveedores en Chile:**
- Moxa UC‑8200: https://www.moxa.com/en/products/industrial-computing/arm-based-computers/uc-8200-series · ficha: https://www.moxa.com/getmedia/29c68302-7841-4a4a-a8f6-85b666baccfb/moxa-uc-8200-series-datasheet-v3.4.pdf
- AWS IoT Greengrass, adaptador Modbus‑RTU: https://docs.aws.amazon.com/greengrass/v2/developerguide/modbus-rtu-protocol-adapter-component.html
- Iridium Edge, interfaz RS‑232 con comandos AT: https://www.europasatellite.com/Iridium-Edge-Short-Burst-Data-SBD-Modem-s/Iridium-Edge.htm · nota de aplicación de Senquip: https://docs.senquip.com/app_notes/APN0018%20Rev%20A%20-%20Using%20Iridium%20Satellite%20with%20a%20Senquip%20Device.pdf
- Iridium CloudConnect: https://www.iridium.com/services/iridium-cloudconnect · guía de inicio en AWS: https://iridium.com/blog/on-cloud-66-series-part-1-introducing-the-iridium-cloudconnect-sbd-on-aws-quick-start-truly-global-iot-in-just-a-few-clicks
- Iridium SBD: https://www.iridium.com/services/iridium-short-burst-data-sbd
- Globalsat Chile: https://www.gsat.cl/ · Iridium Edge en Globalsat: https://globalsat.com/solutions/m2m/iridium-edge · Globalsat e Iridium en Chile: https://globalsat.com/news/globalsat-group-and-iridium-present-the-iridium-next-constellation-and-iridium-certus-services-in-chile
- Globalsat Chile y Myriota: https://mineriaenergia.com/globalsat-chile-se-capacita-en-la-tecnologia-satelital-para-iot-de-myriota/ · latencia de Myriota: https://myriota.com/hyperpulse-5g/
- Teltonika EYE SENSOR EN12830: https://wiki.teltonika-gps.com/images/b/b1/EYE_SENSOR_EN12830_Datasheet_1.0.pdf · https://wiki.teltonika-gps.com/view/BTSMP1
- Teltonika de Chile: https://www.getonbrd.com/jobs/programacion/networking-and-iot-engineer-teltonika-de-chile-santiago · https://congreso.america-digital.com/iot-solutions-for-connectivity-fleet-management-tracking-and-ev-charging-teltonika-increases-the-value-of-your-business/?lang=en
- RUT956 (alternativa): https://www.gowifi.co.nz/specs/rut956-datasheet-v13.pdf · homologación E‑mark: https://wiki.teltonika-networks.com/view/RUT956_E-mark
- Techvalue, representante oficial de Moxa en Chile y Perú: https://techvalue.cl/moxa
- Moxa ioLogik E1260: https://www.moxa.com/Products/INDUSTRIAL-EDGE-CONNECTIVITY/Controllers-and-IOs/Universal-Controllers-and-I-Os/ioLogik-E1200-Series/ioLogik-E1260
- Sensitech TempTale Ultra BLE: https://www.sensitech.com/de/media/TT_Ultra_BLE_LS_0822_web_tcm969-156705.pdf
- Subtel, certificación de equipos de alcance reducido: https://www.subtel.gob.cl/certificacion-de-equipos-de-telecomunicaciones/ · guía de laboratorio sobre homologación en Chile: https://appluslaboratories-test.applus.solutions/dam/PDFServices/Laboratories/GLOBAL/chile-radio-type-approval-(subtel)_es.pdf
- ELA Blue PUCK T EN12830: https://elainnovation.com/en/catalogue/blue-puck-t-en12830-en/
- Starlink Mini en movimiento: https://www.satelliteinternet.com/resources/starlink-mini-while-driving/ · consumo: https://www.dishytech.com/starlink-mini-review/

**AWS y Android:**
- Bandeja de salida transaccional: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html
- MQTT en IoT Core: https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html
- KMS Sign: https://docs.aws.amazon.com/kms/latest/APIReference/API_Sign.html
- Voz por país: https://docs.aws.amazon.com/end-user-messaging/latest/userguide/nx-supported-countries-south-america.html
- Android, Bluetooth y servicios en segundo plano: https://developer.android.com/develop/connectivity/bluetooth/ble/background

**Otras:** NIST, CRC: https://csrc.nist.gov/glossary/term/cyclic_redundancy_check

---

## 21. Cambios respecto de la versión 8

| Tema | v8 | v9 |
|---|---|---|
| Controlador | Teltonika RUT956 con aplicación propia | Gateway con Greengrass, la misma plataforma de los CD; el RUT956 queda como alternativa |
| Satélite | FMC650 con Iridium Edge: solo estado de entradas | Iridium Edge manejado por el gateway: alarmas, curva cada 3 min y órdenes de Calidad |
| Segunda cadena | Alarma independiente + relé + FMC650 + batería B | TC58e con doble evaluación + sensor independiente EN 12830 en glicol |
| Termógrafo | ELA o Sensitech | Teltonika EYE SENSOR EN12830 (Teltonika de Chile); ELA solo para congelado bajo −20 °C |
| Receptores en la nube | Receptor de flota y receptor satelital propios | Iridium CloudConnect a SQS; sin receptor de flota |
| SIM M2M | 93 | 62 |
| INT‑05 | 35.532 mensajes/día | 30.548 mensajes/día |
| Nuevas secciones | — | Criterio de diseño (§3.1), arquitectura por capas (§5.1), software en el borde (§5.3), montaje (§13) y alternativas descartadas (§14) |
| v9.1 | — | Glosario; Moxa con representante oficial en Chile (Techvalue); módulo de sondas Moxa ioLogik E1260‑T; alternativa a CloudConnect; registradores para congelado; trámites Subtel; comparación de soluciones completas (§14.5) y garantías y límites (§14.6) |
| v9.2 | — | Red móvil y satélite siempre activos en paralelo (§6.2); detectar, alarmar y frenar sin red (§6.1); túneles y cortes de cielo (§6.4); plan ante falla del equipo de frío (§8.3); alerta «kit sin reportar» por silencio satelital; prueba V20 |
| v9.3 | — | Coherencia de los datos (§6.5); protocolo ante ruptura confirmada con RSA arts. 102, 105 y 192 (§8.8); pruebas V11 ampliada y V21 |
| v9.4 | — | Mapa por subdocumento reescrito con sección, archivo, línea, acción y fuente (§22); orden de edición sugerido |

---

## 22. Qué se agrega en cada subdocumento

> **Alcance aprobado (24‑10‑2026):** se implementa solo en SD2 (solo normativa), SD3, SD4, SD5 (sin entidades nuevas ni cambios de diagramas), SD6 y SD7. **No** se toca SD1, SD8, SD13 ni el Informe 3 por ahora. Las instrucciones vigentes para implementar están en `BRIEF_IMPLEMENTACION_CADENA_FRIO.md`; las filas de este mapa para SD1, SD8, SD13 y el Informe 3 quedan solo como referencia.

**Regla:** el diseño completo vive en el **SD4**. Cada uno de los demás subdocumentos toma solo lo que le corresponde según el índice obligatorio de las Aclaraciones (§11) y remite al SD4 para el detalle. Ningún subdocumento repite el diseño. Las cifras de todos los subdocumentos deben coincidir con §16.

**Cómo leer las tablas.** «Archivo:línea» indica dónde está hoy el texto en la rama vigente de cada subdocumento, revisada el 24‑10‑2026; las líneas pueden moverse con otras ediciones. Acción: **Agregar** (texto nuevo), **Cambiar** (reemplazar lo que dice hoy) o **Revisar** (comprobar coherencia, sin cambio previsto).

### 22.1 SD1 — Presentación de la empresa (rama `LafroX-Subdoc1-LateX`)

| Sección | Archivo:línea | Acción | Qué va | Fuente |
|---|---|---|---|---|
| 1.1 Presentación de la empresa | `contenido.tex:24` | Cambiar (opcional) | En la línea de negocio «Trazabilidad y telemetría de frío industrial», agregar «con alerta en ruta por red móvil y satélite» | §3.2 |
| 1.6 Alianzas | `contenido.tex:332` | Revisar | No agregar a Moxa, Teltonika, Globalsat ni Sensitech: son proveedores del proyecto, no alianzas de la empresa | §15 |

### 22.2 SD2 — Comprensión del problema (rama `LafroX-Subdoc2-LateX`)

| Sección | Archivo:línea | Acción | Qué va | Fuente |
|---|---|---|---|---|
| 2.2.1 Los tres problemas entrelazados | `contenido.tex:41` | Revisar | Ya describe el registro manual sin alarmas; sin cambio | §1 |
| 2.2.2 Contexto operacional, normativo y estacionalidad | `contenido.tex:53` | Cambiar | Completar el RSA: arts. 68 (vehículo, termómetro exterior, autorización), 190 (registro en transporte; tolerancia de −15 °C), 191 (−12 °C en reparto local), 303 (cecinas 0–6 °C), 102 (prohibición de distribuir alimento alterado), 105 (área de no aptos y destino autorizado) y 192 (no volver a congelar) | §2 y §8.8 |
| 2.2.2 (estacionalidad) | `contenido.tex:53` | Agregar | En invierno aumenta el tiempo sin cobertura en las rutas rurales (Caso, tabla de estacionalidad) | §6.2 |
| 2.2.3 Arbitraje de tensiones | `contenido.tex:68` | Revisar | Ya fija el control graduado y que Calidad decide (S‑04); coincide con el diseño | §7 |
| 2.2.4 Prácticas de la industria | `contenido.tex:80` | Cambiar | Hoy cita los arts. 71 y 192: agregar los de transporte (190 y 191). Agregar un párrafo: aire frente a producto, simuladores de producto y registro EN 12830 (Reglamento CE 37/2005), con fuentes APA | §2 |
| Referencias | `contenido.tex:383` | Agregar | Reglamento (CE) 37/2005, Codex CAC/RCP 8‑1976 y la versión actualizada del DS 977/96 | §20 |
| 2.3, 2.4 y Anexo 2.3 | — | Revisar | Sin cambio: describen el problema, no la solución | — |

### 22.3 SD3 — Esquema de solución y alcance (rama `LafroX-Subdoc3-LateX`)

| Sección | Archivo:línea | Acción | Qué va | Fuente |
|---|---|---|---|---|
| 3.1.1 Capacidades de la solución | `contenido.tex:11` | Cambiar | «Registro continuo, alerta y decisión en ruta, también sin red móvil, y bloqueo de la entrega del producto afectado sin depender de la red» | §3.2 y §6.1 |
| 3.2.2 Exclusiones, restricciones y supuestos | `contenido.tex:100` | Revisar | Remitir al supuesto S‑28 corregido | §22.13 |
| Anexo 3.C, supuesto **S‑28** | `tablas_anexo/supuestos.tex:33` | Cambiar | De «un termógrafo» a «el kit de cadena de frío (gateway, sondas, sensor independiente, termógrafo y módem satelital)». LafroX provee, instala y mantiene el kit (antes lo compraba el CLIENTE) | §3.2 y §15 |
| 3.2.3 Catálogo de requerimientos | `contenido.tex:122` | Revisar | RF‑09.03 a 09.10 y RNF‑09.05 se mantienen | §1 |
| Anexo 3.B, requisitos propios | `tablas_anexo/rnf_propios.tex:6` | Agregar | Requisitos propios nuevos, con umbral: alerta por satélite ≤ 5 min con o sin red móvil; curva en los indicadores ≤ 5 min por cualquiera de los dos caminos; detección y bloqueo sin red; decisión con simulador de producto; doble evaluación en el terminal; tiempo máximo fuera de frío en el andén | §6, §7 y §18 |
| 3.2.4 Reglas de negocio (RNG‑04) | `contenido.tex:152` | Cambiar | Agregar: acción por defecto (lo retenido vuelve al CD y decide Calidad), ventana de puerta, retención por contradicción y disposiciones ante una ruptura confirmada | §7.2, §8.8 y §10.2 |
| Anexo 3.G, reglas de negocio | `tablas_anexo/reglas_negocio.tex:9` | Cambiar y agregar | RNG‑04 ampliada y regla nueva: tiempo máximo fuera de frío por familia | §8.2 |
| 3.2.5 Criterios de aceptación | `contenido.tex:162` | Cambiar | R18‑03 medido con la conciliación de las tres series en el 100 % de los camiones con frío | §8.6 |
| Anexo 3.J, R18‑03 | `tablas_anexo/criterios_aceptacion.tex:8` | Cambiar | Método de verificación: conciliación de las tres series y prueba V21 | §17 |
| 3.3.2 Trazabilidad y cadena de frío | `contenido.tex:232` y `:249` | Cambiar | Hoy vincula la lectura «por ubicación o viaje». Reemplazar por la historia térmica por SSCC: cámara, andén y compartimento, con escaneos de salida de cámara, carga y bajada; ejemplo de un pedido | §4 |
| 3.4.1 Aplicación en la jornada operacional | `contenido.tex:278` | Agregar | Escaneos nuevos (salida de cámara y bajada de SSCC de frío) y qué ve el conductor | §8.2, §8.4 y §9 |
| 3.4.5 Operación | `contenido.tex:478` | Agregar | Plan ante falla del equipo de frío y protocolo ante ruptura confirmada | §8.3 y §8.8 |
| 3.4.6 Participación de los grupos de interés | `contenido.tex:522` | Agregar | Calidad aprueba las reglas por familia y la lista de llamada | §10.2 |
| Formulario T‑12 | `LAFROX-Formulario-T-12.tex:120–127, 236, 300–301, 406 y 604` | Cambiar | Columna de componente de RF‑09.03 a 09.10, RNF‑09.05, RNF‑23.01/02, RT‑05.29 y RT‑17.06: gateway del camión con Greengrass, Iridium Edge, sensor independiente, termógrafo EYE EN12830 y CloudConnect | §5.2 |

### 22.4 SD4 — Arquitectura (rama `subdoc-4`)

El detalle por archivo y línea está en §16.4. Resumen por sección:

| Sección | Archivos | Acción | Qué va | Fuente |
|---|---|---|---|---|
| 4.1 Capas | `04/partes/4.1_logica/04_capas_de_la_arquitectura.tex:156` | Cambiar | Greengrass también en el camión; doble evaluación en el TC58e | §5.1 |
| 4.1 Módulos | `05_modulos_funcionales_y_limites_de_contexto.tex:45, 52 y 55` | Cambiar | M9 dueño de reglas, retenciones y disposiciones; puntos de medición; termógrafo cada 1 min | §4 y §7 |
| 4.1 Interfaces | `07_catalogo_de_interfaces.tex` y Anexo 4‑G | Cambiar | INT‑05 con red móvil y satélite, siempre activos | §6.2 |
| 4.1 Seguridad | Anexo 4‑Q | Agregar | Amenazas del kit y controles: certificado por camión, latido firmado, órdenes firmadas con KMS | §5.6 y §10.3 |
| 4.1 Funciones sin conexión | `16_funciones_disponibles_y_no_disponibles_sin_conexion.tex` | Agregar | Detectar, alarmar y frenar sin red; coherencia de datos | §6.1 y §6.5 |
| 4.1 Puntos únicos de falla | `13_puntos_unicos_de_falla_y_riesgos_residuales.tex` | Agregar | Matriz de fallas y riesgos residuales | §11 y §19 |
| 4.1.1 Tecnologías de software | `02_especificaciones_tecnologias_de_software_a_utilizar.tex` y `08_detalle_de_tecnologias_seleccionadas.tex` | Agregar | Greengrass en el borde, Iridium SBD y CloudConnect; alternativas | §5.3 y §14 |
| ADR | `12_registro_de_decisiones_de_arquitectura.tex` y Anexo 4‑O | Agregar | ADR nuevo con las alternativas de §14 | §14 |
| 4.2 Física | `04/partes/4.2_fisica/02_a_emplazamiento.tex`, `02_b_servicios_nube.tex`, `02_c_conexiones.tex` y `11_j_despliegue.tex` | Cambiar | Componentes, emplazamiento, conexiones, puntos de falla y despliegue | §5, §12 y §13 |
| 4.2 Dimensionamiento | `12_k_dimensionamiento.tex`, Anexos 4‑B y 4‑I, `calculo.py` | Cambiar | INT‑05 30.548/día; 6,77 GB/año | §16 |
| 4.2.1 Implementos y T‑11 | `04_c_implementos.tex` y `04/formularios/T11/15_anexo_t11.tex` | Cambiar y agregar | Filas de §16.1 y disponibilidad en Chile | §15 y §16.1 |
| 4.3.2 Data center secundario | `04/partes/4.3_centros_de_datos/06_e_sitio_secundario.tex` | Agregar | Segundo destino satelital y archivo de 72 h | §12 |

### 22.5 SD5 — Modelo y gestión de datos (rama `LafroX-Subdoc5-LateX`, carpeta `05_modelo_datos/`)

| Sección | Archivo:línea | Acción | Qué va | Fuente |
|---|---|---|---|---|
| 5.1.7 Trazabilidad sanitaria y cadena de custodia | `partes/5_1_modelo.tex:135` | Agregar | Manifiesto viaje–compartimento–SSCC; retención por SSCC e incidente; disposición; historia térmica por SSCC (cámara, andén y camión) | §4 y §8.8 |
| 5.1.10 Telemetría, caché y objetos | `partes/5_1_modelo.tex:218` y `:223` | Cambiar | 10.920 muestras/día → 127.848 lecturas y 30.548 mensajes al día; lotes satelitales reemplazados por la serie fina | §6.5 y §16 |
| 5.2.2 Transaccionalidad, aislamiento e idempotencia | `partes/5_2_gestion.tex:17` | Agregar | Productor, arranque y secuencia; procesamiento único; huecos; crítica tardía | §6.5 |
| 5.2.7 Retención, archivado, eliminación y protección | `partes/5_2_gestion.tex:72` | Agregar | Temperatura 5 años; archivo original de los registradores en S3 con bloqueo; sin posición GPS | §12 |
| 5.4.2 Consultas críticas e índices | `partes/5_4_desempeno.tex:17` | Agregar | Índice por SSCC, compartimento e intervalo de tiempo | §4 |
| Anexo 5‑A, diccionario | `anexos/tablas/A_4.tex:81` (cal_excursion), `A_9.tex:7` (tel_lectura_cruda) y `A_10.tex:114` (hech_excursion) | Agregar | Entidades nuevas: dispositivo del kit, manifiesto, retención por SSCC, orden de Calidad, disposición, exposición en andén, lote satelital | §4, §6 y §8.8 |
| Anexo 5‑C, dominios de valores | `anexos/contenido.tex:185` | Cambiar | Catálogo `origen`: hoy CAMARA y TERMOGRAFO_VEHICULO; agregar SONDA_AIRE, SIMULADOR y SENSOR_INDEPENDIENTE. Estados de retención y disposiciones | §7.3 y §8.8 |
| Anexo 5‑D, retención por dominio | `anexos/contenido.tex:248` | Agregar | Retención de las tres series y del expediente | §12 |
| Anexo 5‑F, índices | `anexos/contenido.tex:272` | Agregar | El índice de 5.4.2 | §4 |

### 22.6 SD6 — Metodologías (rama `LafroX-Subdoc6-LateX`)

| Sección | Archivo:línea | Acción | Qué va | Fuente |
|---|---|---|---|---|
| 6.1.3 Gestión de adquisiciones | `subdocumento_6/contenido.tex:35` | Agregar | Regla: ningún equipo sin cotización de un proveedor con domicilio en Chile y certificación Subtel; plazos de Subtel en el cronograma | §15 |
| Anexo 6.B, adquisiciones | `subdocumento_6/tablas/adquisiciones.tex:4` | Cambiar y agregar | Dividir la fila de terreno: equipos de uso a cargo del CLIENTE; sistema de cadena de frío (sensores y gateways de cámara y kits de camión) a cargo de LafroX. Fila nueva: SIM M2M y servicio satelital, a cargo de LafroX | §15 y §22.13 |
| Anexo 6.A, interesados | `anexos.tex:21` | Revisar | Ya incluye la jefatura de Calidad | — |
| 6.2.2 DevSecOps | `subdocumento_6/contenido.tex:64` | Agregar | Despliegue por etapas del software del camión con Greengrass, con reversión | §13.6 |

### 22.7 SD7 — Plan de trabajo, EDT y cronograma (rama `LafroX-Subdoc7-LateX`)

| Sección | Archivo:línea | Acción | Qué va | Fuente |
|---|---|---|---|---|
| T‑14, paquete 3.4.4 | `formulario-t14/contenido.tex:217` y `tablas/tab_T14_21.tex:7` | Cambiar | Reglas, retención por SSCC, acción por defecto, disposiciones, doble evaluación en el TC58e | §7, §8.8 y §10 |
| T‑14, paquete 3.4.5 | `formulario-t14/contenido.tex:219` y `tablas/tab_T14_21.tex:8` | Cambiar | «Ingesta de temperatura… (M12 Telemetría)» → componentes de Greengrass del camión, red móvil y satélite, a cargo de **M9**, como dice el SD4 | §5.3 y §22.13 |
| T‑14, paquete 5.1.1 | `formulario-t14/contenido.tex:389` | Cambiar | Especificación de compra del kit para el CLIENTE, con certificación Subtel | §15 |
| T‑14, paquete 6.5.4 | `formulario-t14/contenido.tex:469` y `tablas/tab_T14_40.tex:7` | Cambiar | «Termógrafos instalados…» → kit de cadena de frío instalado y recibido en los 28 camiones | §13.4 y §13.5 |
| T‑14, paquetes nuevos | Fases 2 y 4 | Agregar | Banco de pruebas del kit; mapeo térmico por tipo de carrocería; piloto de 6 semanas en 4 camiones | §13.2, §13.3 y §13.6 |
| T‑14, paquetes 7.1.3 y 7.2.4 | `formulario-t14/contenido.tex:491` y `:507` | Agregar | Capacitación en los escaneos nuevos y en el rojo del TC58e; procedimientos de contingencia por ruta y de ruptura confirmada | §8.3, §8.8 y §9 |
| 7.3.3 Plan de implantación y puesta en marcha | `subdocumento-07/contenido.tex:382` | Agregar | Piloto antes de la ola de reparto; los 28 kits instalados antes de que parta | §13.6 |
| T‑18, olas | `formulario-t18/tablas/tab_T18_olas_alcance.tex:4` y `:6` | Cambiar | Olas 1 y 3: temperatura a cargo de M9 (no M12); kit antes de la ola 3 | §13.6 |
| T‑15, nivelación de recursos | `formulario-t15/contenido.tex:72` | Agregar | Horas de los componentes de borde, M9, app del TC58e, mapeo, instalación y piloto | §13.1 |
| Anexo 7.C, R18‑03 | `subdocumento-07-anexos/tablas/tab_7C1.tex:6` | Cambiar | Paquetes nuevos que acreditan R18‑03 | §17 |
| Anexo 7.E, INT‑05 | `subdocumento-07-anexos/tablas/tab_7E2.tex:8` | Cambiar | Paquetes y volumen nuevos de INT‑05 | §16.2 |
| Anexo 7.F, supuestos de planificación | `subdocumento-07-anexos/contenido.tex:57` | Agregar | Plazos de Subtel y de las cotizaciones como supuestos del cronograma | §15 |

### 22.8 SD8 — Plan de riesgos (rama `Lafrox_Subdocumento_8_Latex_Nuevo`)

| Sección | Archivo:línea | Acción | Qué va | Fuente |
|---|---|---|---|---|
| 8.2.1 RBS | `08_plan_riesgos/contenido.tex:103` | Agregar | Riesgos nuevos en la rama «Solución y tecnología» | §19 |
| T‑16, R‑011 | `Lafrox-Subdocumento-T-16.tex:39` | Cambiar | Ampliar la mitigación con el mapeo térmico, los simuladores y la doble evaluación | §5.6 y §13.3 |
| T‑16, riesgos nuevos (desde R‑046) | `Lafrox-Subdocumento-T-16.tex`, después de `:73` | Agregar | Cobertura satelital en rutas reales y en invierno (V18); disponibilidad y certificación de equipos en Chile; Greengrass en el UC‑8200 y su comportamiento vehicular (V1, V5); desarrollo propio del borde y del TC58e; adopción de los escaneos nuevos; registrador para congelado bajo −20 °C | §15 y §19 |
| Anexos: causa–evento–efecto y análisis cuantitativo | `LafroX-Subdocumento-8-Anexos.tex:37` y `:141` | Agregar | Fichas y valores de los riesgos nuevos; actualizar R‑011 | §19 |
| 8.3.1 Respuestas y costo‑beneficio | `08_plan_riesgos/contenido.tex:180` | Agregar | Respuesta, disparador, responsable y plazo de cada riesgo nuevo | §19 |
| — | — | No agregar | **No** se declara el riesgo de rechazo de los transportistas | Decisión del 24‑10‑2026 |

### 22.9 SD9 — Plan de calidad (rama `LafroX-Subdoc9-LateX`, carpeta `SD9_v_nueva/`)

| Sección | Archivo:línea | Acción | Qué va | Fuente |
|---|---|---|---|---|
| 9.2.3 Estrategia de pruebas | `09_plan_calidad/contenido.tex:175` | Agregar | Banco de pruebas, mapeo, piloto y pruebas de campo del kit | §13 y §17 |
| 9.2.4 Datos de prueba | `09_plan_calidad/contenido.tex:224` | Agregar | Series con aperturas de puerta, turno sin red, túnel simulado, mensajes satelitales y errores inyectados | §17 |
| 9.3.1 Actividades de calidad en la EDT | `09_plan_calidad/contenido.tex:270` | Agregar | Ubicación de V1–V21 en los paquetes del SD7 | §17 y §22.7 |
| 9.3.3 Pruebas periódicas durante la Operación | `09_plan_calidad/contenido.tex:353` | Agregar | Prueba periódica del camino satelital, calibración y revisión del kit | §13.6 |
| T‑13, §5 Datos de prueba | `T13/contenido.tex:135` (fila de temperatura en `:144`) | Cambiar | Los datos de 9.2.4 | §17 |
| T‑13, §7.3 Perfil operacional de terreno | `T13/contenido.tex:233` | Agregar | V9, V10, V18 y V20 | §17 |
| T‑13, §7.4 Resultados del caso | `T13/contenido.tex:251` (R18‑03 en `:258`) | Cambiar | Hoy dice «verificación del bloqueo del despacho»; precisar: bloqueo del SSCC antes de salir y retención en ruta; agregar V21 | §8.2, §8.8 y §17 |
| T‑17, §5 Aceptación de resultados del caso | `T17/contenido.tex:197` (R18‑03 en `:205`) | Cambiar | Criterio con conciliación de las tres series y SLA de §18 | §18 |
| Anexo 9.D, trazabilidad de resultados | `09_anexos/contenido.tex:259` | Cambiar | R18‑03 → V1–V21 → paquetes del SD7 | §17 |

### 22.10 SD13 — Innovaciones (rama `LafroX-Subdoc13-LateX`, carpeta `SD13_v_nueva/`)

| Sección | Archivo:línea | Acción | Qué va | Fuente |
|---|---|---|---|---|
| 13.3 Innovación 3 (INN‑03), «Tecnología, práctica o modelo» | `13_innovaciones/contenido.tex:290` | Agregar | Los simuladores dan una temperatura de producto, mejor insumo para estimar la vida útil remanente que el aire | §2 y §4 |
| 13.3, «Diseño de la incorporación» | `13_innovaciones/contenido.tex:338` | Agregar | INN‑03 recalcula la vida útil del producto liberado tras una excursión (disposición «liberar») | §8.8 |
| T‑19, ficha 3, campo 7 | `T19/contenido.tex:81` | Cambiar | Componentes: hoy B‑01 a B‑03, C‑02, N‑06 y N‑08 con 10.920 mensajes; agregar el gateway del camión, el sensor independiente y 30.548 mensajes/día | §5.2 y §16 |
| T‑19, ficha 3, campo 15 | `T19/contenido.tex:89` | Cambiar | Riesgo R8‑27 (identificador antiguo) → identificador vigente del SD8 | §22.13 |
| Anexo 13.B, matriz de trazabilidad | `13_anexos/contenido.tex:38` y `:51` | Cambiar | Componentes nuevos | §5.2 |

### 22.11 Oferta económica e Informe 3 (13‑11‑2026)

| Entregable | Qué va | Fuente |
|---|---|---|
| Informe 3: proveedores clave | Techvalue (Moxa), Globalsat Chile (Iridium), Teltonika de Chile (EYE SENSOR) y el proveedor del registrador de congelado | §15 |
| Informe 3: adquisiciones clave; E‑21, 2.4 | Matriz y cronograma de compra del kit, certificación Subtel y, si corresponde, importación | §15 |
| E‑21, 2.1 y 2.5: costos | El sistema de cadena de frío lo compra LafroX: entra como inversión de LafroX, junto con la especificación, el desarrollo, la integración, la instalación y el piloto. Operación: 62 SIM M2M y 8.120 mensajes satelitales al día, según quién los contrate | §16 y §22.13 |
| E‑21, 2.6: mantención | Calibración, baterías de los sensores, glicol y repuestos | §13.6 |
| E‑21, 2.3: curva S; 2.2: VAN y TIR | Compra antes del banco de pruebas y del piloto; despliegue antes de la ola de reparto | §13 |
| E‑21, 2.7: innovaciones | INN‑03 con su insumo nuevo | §22.10 |

### 22.12 Transversal

- **Declaración de uso de IA** de cada subdocumento que cambie: nueva fila o fila actualizada (Aclaraciones §7.2).
- **Formulario T‑12:** cada cambio de las tablas anteriores debe quedar trazado a su requerimiento.
- **Orden de edición sugerido:** SD3 (supuesto y reglas) → SD4 → SD5 → SD7 → SD8 → SD9 → SD13 → SD2 → SD6 → SD1. Primero lo que define el alcance; después lo que lo usa.

### 22.13 Inconsistencias que el mapa destapa

1. **M9 o M12.** El SD4 asigna la temperatura a M9 (con B‑02 y N‑08) y deja a M12 solo la posición. El SD7 (paquete 3.4.5) y el T‑18 asignan la ingesta de temperatura a M12. Hay que alinear el SD7 con el SD4.
2. **S‑28 y quién compra.** S‑28 cubre hoy solo un termógrafo y dice que lo compra el CLIENTE; el Anexo 6.B pone sensores, termógrafos y gateways junto a los terminales. Decisión del 24‑10‑2026: **LafroX provee, instala y mantiene el sistema de cadena de frío** (sensores y gateways de cámara y los kits de camión), porque es infraestructura que LafroX opera y de la que dependen sus niveles de servicio; el CLIENTE compra solo los equipos de uso (terminales, impresoras, terminales de pago y balanzas). Las SIM M2M y el servicio satelital también los contrata LafroX. Afecta al Informe 3, que por ahora no se edita.
3. **«Bloqueo del despacho».** El SD9 lo usa en general. El diseño bloquea el SSCC antes de salir (andén) y lo retiene en ruta; no bloquea el camión.
4. **SD13.** La ficha de INN‑03 cita 10.920 mensajes y el riesgo R8‑27, que ya no existe en el SD8 vigente.
5. **SD2.** Cita los arts. 71 y 192 del RSA; para el transporte rigen los arts. 68, 190 y 191.
6. **SD4.** El texto actual dice que Greengrass «no se instala en camiones» (`04_capas_de_la_arquitectura.tex:156`); este diseño lo instala (§16.4).
7. **B‑01 del T‑11.** Los sensores de cámara usan un módulo Ebyte sin distribuidor chileno confirmado. Conviene evaluar el mismo Moxa ioLogik E1260‑T, que tiene representante en Chile.
