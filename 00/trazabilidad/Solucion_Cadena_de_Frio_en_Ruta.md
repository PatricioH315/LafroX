# Cadena de frío en ruta: solución técnica para los camiones refrigerados de Puelche

**LafroX · Caso 02 · Documento de trabajo del Subdocumento 4 · versión 7 · 24‑10‑2026**

**Estado:** base de ingeniería para construir y probar. **No autoriza compras** hasta aprobar las pruebas de §14. No está incorporado al texto del Subdocumento 4.

> **Documento interno con precios.** Las Bases Administrativas (art. 50.2) prohíben en la Oferta Técnica «información de precios, tarifas, valores unitarios ni cifra alguna que permita inferir el monto de la oferta económica», con exclusión inmediata. Antes de llevar cualquier parte al Subdocumento 4 hay que **quitar §16 y todo valor en CLP o USD**.

**Etiquetas:** [H] verificado en la fuente citada · [I] inferencia de diseño · [C] requiere confirmación escrita o prueba · [E] estimación · [P] compromiso propio de LafroX, no exigido por las Bases.

---

## 1. El problema

| Hecho del caso | Consecuencia |
|---|---|
| Un cliente de food service rechazó un camión completo por sospecha de ruptura de cadena de frío. Puelche no pudo demostrar lo contrario | Pérdida de CLP 21 millones (Caso §4.9) |
| La autoridad sanitaria observó la ausencia de registro continuo de temperatura | Observación en fiscalización (Caso §4.9) |
| El retiro de marzo de 2026 tardó 9 días y terminó en una estimación | Sumario y 6 meses fuera de un proveedor que representa el 6 % de las ventas (Caso cap. 1) |

El caso pide registro continuo y automático, alerta oportuna, evidencia ante la autoridad y el cliente, y una regla escrita (§9.6; criterio de aceptación n.º 3).

El diseño persigue dos cosas:
- que una excursión produzca una **intervención a tiempo**;
- que, mientras nadie decida, **ningún producto posiblemente comprometido se entregue**.

---

## 2. Requisitos e indicadores

| # | Requisito | Indicador |
|---|---|---|
| R1a | Registro completo de cada viaje | % de viajes con registro completo y conciliado; un viaje con huecos es incumplimiento |
| R1b | Gestión de fallas de integridad | % de fallas detectadas y gestionadas en plazo |
| R2 | Aviso oportuno | Tiempos técnicos hasta la emisión (§11.1) y objetivos operativos de acuse y acción (§11.3) |
| R3 | Temperatura en los indicadores del día | **≤ 5 min, como fija el caso (RT‑05.29)** con cualquier camino disponible (§5.4). Sin ninguna red (túneles) se declara **operación degradada**: los datos se guardan y suben al reconectar |
| R4 | SLA contractual | Compromisos escritos de los proveedores trasladados al SLA de LafroX |
| R5 | Evidencia en la puerta del cliente | Curva operativa en el TC58e con su antigüedad visible |
| R6 | Protección local | Ningún SSCC posiblemente comprometido se entrega sin una decisión válida de Calidad, aunque no haya comunicación ni funcione el evaluador principal |
| R7 | Operación sin señal y sincronización (caso) | 14 h sin cobertura sin perder datos; sincronización de la jornada en ≤ 10 min al reconectar (RT‑03.10 y RT‑03.13 del caso) |

---

## 3. Arquitectura

### 3.1 Principio y alcance de la garantía

`sensor → detección → evento (productor, época, secuencia, compartimento, incidente, versión de regla) → retención local → envío por caminos independientes → recepción persistida con la obligación de notificar → notificación → acuse humano → acción → decisión firmada sobre una revisión de estado → aplicación local confirmada`

**Garantía de diseño (a demostrar en las pruebas de §14):** ninguna falla de **un solo componente** del sistema de medición, alarma, evaluación o comunicación del camión permite **entregar** un SSCC posiblemente comprometido. Esto incluye que el controlador siga encendido pero evalúe mal.

**No cubre, y se declara:**
- destrucción física del camión;
- falla del sistema eléctrico del camión que agote además las baterías A y B;
- dos fallas independientes simultáneas.

Estar en una zona sin cobertura **no** cuenta como falla: es una condición normal y se prueba combinada con fallas de equipo.

### 3.2 Medición

| Elemento | Función | Nota |
|---|---|---|
| **Sondas de aire cableadas** (retorno y puertas) | Advertencia | Adquisición cada 5 s |
| **Sonda de producto** cableada | Crítica, en familias de carga **validadas** por mapeo | En una familia no validada, la crítica se decide con la sonda de aire |
| **Sondas del módulo independiente** | Respaldo | **Una por compartimento**, con límite inferior y superior (§3.3) |
| **Termógrafos EN 12830** (ELA Blue PUCK T) | Registro certificado de instrumento | **Cantidad y ubicación según el mapeo de cada compartimento.** La base de cálculo son 2 por camión, juntos en el punto crítico. Se exige referencia exacta, firmware y certificado EN 13486 [C] |
| **Sensor de puerta** y **contacto de alarma del equipo de frío** | Explicar cada advertencia y anticipar la falla del equipo | Base: 1 sensor por puerta de carga |
| **Estudio de mapeo** por tipo de caja, compartimento y familia de carga | Ubicaciones, tolerancias y validación de la sonda de producto | Previo al piloto |

**Notas de medición:**
- **Resolución y exactitud son cosas distintas.** El protocolo transmite 0,01 °C, pero las decisiones consideran la incertidumbre de calibración y una **histéresis** alrededor de cada umbral.
- **Discrepancias.** Las sondas (cada 5 s) pueden detectar una excursión corta que el termógrafo (cada 5 min) no registra. En ese caso, la serie primaria de las sondas alrededor del incidente se conserva en el expediente junto al registro certificado, y la discrepancia queda documentada.

### 3.3 Equipos en el camión

| Equipo | Función | Candidato | Prueba |
|---|---|---|---|
| **Controlador local** (circuito A) | Adquisición, evaluación, máquina de estados, cola persistente, publicación por C1/C2/C3, latido y curva al TC58e. Requisitos: Ethernet, LTE propio, entradas para sondas, E/S digitales, serie aislada, watchdog de hardware, programable | Gateway industrial programable [C]. El FMC650 no sirve: sin Ethernet ni Wi‑Fi, y su SBD no lleva la temperatura [H] | V1 |
| **Módulo de alarma independiente** (circuito B) | Por compartimento: límites inferior y superior, retardo conservador, **enclavamiento** hasta el reconocimiento de Calidad, supervisión de cable abierto o en corto, zumbador propio | Controlador de alarma industrial [C] | V6, V16 |
| **Transmisor local de la alarma independiente** (circuito B) | Emite por Bluetooth, dentro de la cabina, «alarma independiente activa». El TC58e lo escucha **sin pasar por el controlador** | Transmisor de E/S por Bluetooth [C] | V16 |
| **Iridium Edge Pro** (circuito B) | SBD propio (productor B) y del controlador; supervisa el latido del controlador; reenvía la alarma independiente; recibe órdenes | Programable, IP67, 7–32 V [H]. La potencia publicada (1,6 W) difiere de una ficha anterior (2 A a 7 V): se dimensiona con el pico [C] | V2, V10 |
| **Router de banda ancha** (circuito C) | Starlink u OneWeb, dos módems de operadores distintos, Certus opcional; red de cabina | Clase Peplink MAX HD4 [H compatibilidad Certus] | [C] |
| **Internet satelital principal** | Starlink Performance [H] u OneWeb gestionado por Hughes Chile [H] | Comparación en el piloto | [C] |
| **Iridium Certus 700** (opcional) | Respaldo IP y voz [H] | MissionLINK 700 | Solo si el piloto mide aporte |
| **TC58e** (existente) | Retención por SSCC, verificación del estado al entregar, órdenes firmadas, curva en la puerta | App Kotlin del SD4 | V3, V7, V11, V14, V15, V17–V19 |

**Aislamiento entre circuitos:**
- Las señales entre A y B (serie, contactos) van **aisladas** (optoacopladas o con aislamiento galvánico) y con protección contra transitorios.
- Cada circuito tiene su retorno y su fusible.
- La alimentación vehicular se prueba con arranque, caída de tensión, batería envejecida y temperatura extrema (V5).

### 3.4 Caminos de la alarma

| Camino | Ruta | Qué transporta |
|---|---|---|
| **C0 Cabina** | Controlador → luz y zumbador 1 · módulo independiente → zumbador 2 y transmisor Bluetooth → TC58e | Alarmas y retención local |
| **C1 Banda ancha** | Controlador → Ethernet → router → IoT Core | Eventos y lecturas |
| **C2 Celular propio** | Controlador → LTE → IoT Core | Eventos y lecturas |
| **C3 Satélite de alarmas** | Controlador o módulo independiente → Edge Pro → SBD → Iridium | Eventos, lotes de lecturas, supervisión |

**Cuándo se usa cada camino:**
- **Eventos de advertencia o críticos:** siempre por **C1, C2 y C3 en paralelo**.
- **Lecturas:** por un camino IP. Se pasa al siguiente camino **si no llega el acuse de aplicación A2 en 20 s**, sin mirar el estado del módem. Así se cubren DNS caído, certificado rechazado o consumidor detenido.
- C1 y C2 usan **`clientId` distintos** (`<camión>-eth`, `<camión>-lte`). Dos conexiones con el mismo `clientId` hacen que AWS IoT desconecte la anterior [H].

**Ruta alternativa ante caída de la región principal: pendiente de validación (V12).** Iridium admite varios destinos SBD por equipo [H]. **Se pretende** que un receptor fuera de sa‑east‑1 decodifique el mensaje y llame a la guardia **sin depender de M9**. Faltan por confirmar [C]:
- que coexista con CloudConnect;
- que CloudConnect opere en sa‑east‑1;
- que el mensaje llegue legible;
- que exista una guardia que lo supervise.

### 3.5 Energía

| Circuito | Equipos | Respaldo |
|---|---|---|
| **A · Alarma principal** | Controlador, sondas principales, luz y zumbador 1 | Batería y cargador A; ≥ 24 h |
| **B · Alarma de respaldo** | Módulo independiente con sus sondas, zumbador 2, transmisor Bluetooth, Edge Pro | Batería y cargador B, separados de A; ≥ 24 h |
| **C · Banda ancha** | Starlink u OneWeb, router, Certus | UPS dimensionada con la carga medida (Starlink Performance consume 75–100 W [H]) |

### 3.6 Red local de cabina

- El controlador envía al TC58e, **cada 10 s**, un **latido firmado de frescura**. Incluye:
  - la secuencia;
  - la hora de la última adquisición de cada sonda;
  - el contador de ciclos del evaluador;
  - el estado de cada compartimento;
  - la revisión de estado vigente.
- **El TC58e rechaza un latido** si alguna sonda tiene un dato de más de 30 s o si el contador del evaluador no avanzó. Un proceso de comunicaciones vivo con la adquisición congelada **no** pasa como sano.
- La curva operativa llega por el Wi‑Fi de cabina o, si este falla, por Bluetooth dentro de la cabina. El TC58e muestra su antigüedad.
- **En Android**, la recepción corre en un **servicio en primer plano**, conforme a las restricciones de Android para Bluetooth en segundo plano [H]. Al abrirse o reiniciarse, la aplicación arranca en **NO CONFIABLE** y no habilita entregas hasta recibir un latido válido.

---

## 4. Formatos y contratos de mensaje

**Manifiesto del viaje:** se firma y se carga en el controlador, el Edge Pro y el TC58e en el chequeo previo al despacho. Contiene:
- el identificador compacto del viaje (4 bytes);
- los compartimentos;
- las familias de carga y sus reglas vigentes;
- el mapa de sensores;
- la lista de SSCC por compartimento.

Los mensajes se refieren al manifiesto por identificadores cortos. Esto funciona **sin consultar la región principal**, porque el receptor alternativo tiene una copia del manifiesto.

**Productores e identidad:** el controlador es el **productor A** y el Edge Pro el **productor B**. Cada productor lleva una **época**, que se incrementa en cada arranque o reemplazo, y una **secuencia** persistente y monótona dentro de esa época. Así el Edge Pro emite sus propias alarmas con su propia secuencia cuando el controlador está caído.

**Esquemas SBD de subida** (máximo 340 bytes [H]), con encabezado común de 22 bytes: versión, tipo, productor y época, secuencia, viaje, hora UTC y código de autenticación truncado.

| Tipo | Contenido después del encabezado | Tamaño |
|---|---|---|
| Lectura | Compartimento, minuto inicial y *n* minutos × 3 sondas × 2 bytes (un **lote** = 1 minuto de todas las sondas = 6 bytes) | 22 + 3 + 6·*n*; **máximo 52 minutos por mensaje** |
| Alarma | Compartimento, incidente, severidad, regla y versión, temperatura y duración | ≈ 34 |
| Salud | Bits de sensores, circuitos A y B, últimas secuencias de A y B | ≈ 30 |
| Acuse | Productor, época y secuencia confirmada | ≈ 30 |

En operación normal solo con C3 se envía **un mensaje cada 3 minutos con 3 lotes (≈ 43 bytes)**. Por SBD solo se recupera la **última hora** pendiente; el resto espera a C1/C2. **Las alarmas tienen cola propia y siempre salen primero.**

**Orden de decisión** (bajada, máximo 270 bytes [H]):

| Campo | Bytes |
|---|---|
| Versión, tipo, decisión (liberar, bloquear, rechazar, autorizar entrega) | 3 |
| Viaje, compartimento e incidente | 9 |
| Versión de la decisión | 2 |
| **Revisión de estado evaluada** y última secuencia considerada por productor | 12 |
| Emisión y caducidad | 8 |
| Alcance: hash de 16 bytes de un subconjunto de SSCC del manifiesto, más su cantidad | 18 |
| Identificador de clave | 1 |
| Firma ECDSA P‑256 de AWS KMS (formato DER, hasta 72 bytes) | ≤ 72 |
| **Total** | **≤ 125** |

La orden **no lista SSCC**: referencia un subconjunto del manifiesto mediante su hash. Si el TC58e no tiene ese manifiesto, **rechaza la orden y mantiene la retención**. El tamaño real se valida en V2 y V15 con mensajes binarios. Controlador, Edge Pro y backend comparten **vectores de prueba binarios**.

---

## 5. Reglas, estados y orden de los eventos

### 5.1 Reglas por familia

- Calidad define cada regla por familia de producto y compartimento: límites, sensor de referencia, umbrales del módulo independiente y **criterio de exposición**. El criterio indica si la exposición es continua o acumulada, en qué ventana, cómo se recupera y sus excepciones. Esto evita que excursiones intermitentes reinicien el contador y nunca lleguen a crítica.
- Activación con segundo aprobador (RT‑16.03) y prueba en QA (RT‑16.05).
- Si la carga no tiene una regla vigente confirmada en el controlador, el Edge Pro y el TC58e, **el camión no sale**.

### 5.2 Estados

- **Retenciones por SSCC e incidente.** El estado del compartimento se **deriva** de las retenciones abiertas; nunca las borra.
- Por compartimento: `NORMAL → ADVERTENCIA → CRÍTICA → RETENIDO → {LIBERADO | BLOQUEADO | RECHAZADO}`, más **NO CONFIABLE** (§7.2).
- Una recuperación de temperatura solo cierra una ADVERTENCIA. Nunca cierra CRÍTICA ni RETENIDO.

### 5.3 Orden y eventos tardíos

| Situación | Tratamiento |
|---|---|
| Duplicado | Se descarta por productor, época y secuencia |
| Evento tardío **de otro compartimento** | Se procesa con normalidad: las secuencias ordenan el transporte, **no invalidan contenido sanitario** |
| **Crítica tardía** de un compartimento con estado más reciente | **Se procesa siempre.** Abre una retención o reabre el incidente. Si los SSCC ya se entregaron, abre una **evaluación de retiro** en M9 |
| Hueco en la secuencia | M9 pide el reenvío del tramo faltante. Mientras falte, marca el compartimento como **PENDIENTE DE VERIFICACIÓN** en el expediente |
| Recuperación tardía con secuencia menor que una crítica ya aplicada | Se guarda; no cambia el estado |

La prueba V13 inyecta mensajes duplicados, retrasados y reordenados por los tres caminos y entre compartimentos.

### 5.4 Latencia de las lecturas hasta los indicadores (RT‑05.29: ≤ 5 min)

| Tramo | Con C1/C2 | Solo C3 |
|---|---|---|
| Edad de la muestra al enviar | ≤ 1 min | ≤ 3 min (lote cada 3 min) |
| Cola y transmisión | ≤ 20 s | ≤ 60 s [C] |
| Persistencia y disponibilidad en el tablero | ≤ 30 s | ≤ 30 s |
| **Total** | **≤ 2 min** | **≤ 4,5 min [C, V10]** |

Sin ninguna red se aplica operación degradada declarada.

---

## 6. Detección y salud de los sensores

- **Advertencia:** sonda de aire fuera de rango (considerando la histéresis) de forma sostenida durante 30 s. La detección tarda 35 s más el tiempo de respuesta de la sonda, que se mide en V1.
- **Crítica:** según el criterio de exposición de la familia (§5.1).

**Matriz de fallas de medición:**

| Falla | Estado | Alcance de la retención | Para recuperar |
|---|---|---|---|
| Sonda de aire sin datos o implausible, con la otra sonda de aire del compartimento sana | ADVERTENCIA técnica | Ninguna, si la otra sonda y el termógrafo concuerdan dentro de la tolerancia | Reparación al regreso |
| Ambas sondas de aire del compartimento fallan | **NO CONFIABLE** del compartimento | Todos los SSCC del compartimento | Sondas sanas y serie continua, o decisión de Calidad |
| Sonda de producto falla | Las críticas pasan a decidirse con aire (más conservador) | Ninguna adicional | Reparación al regreso |
| Sonda desviada pero plausible (diferencia con el termógrafo del mismo punto mayor que la tolerancia más la incertidumbre) | **NO CONFIABLE** del compartimento | Todos sus SSCC | Calidad, con la descarga del termógrafo |
| Sonda del módulo independiente falla (cable abierto o en corto) | Pérdida del respaldo informada | Ninguna; **el siguiente viaje no sale** hasta repararla | Reparación |
| Contradicción: el módulo independiente alarma y el controlador dice NORMAL | **RETENIDO** | Todos los SSCC del compartimento | Decisión de Calidad |

---

## 7. Protección local en el camión

### 7.1 Ante una excursión

| Estado | Sistema | Conductor |
|---|---|---|
| ADVERTENCIA | Luz y zumbador; causa probable | Corrige y registra. Sigue entregando |
| CRÍTICA / RETENIDO | El TC58e retiene los SSCC del incidente y bloquea su prueba de entrega, también sin señal | No entrega lo retenido |
| Sin decisión de Calidad | Escalamiento (§9) | Aplica el **procedimiento de contingencia de su ruta**, previamente aprobado: detención segura, trasbordo, destino alternativo o retorno, con custodia de la carga |

**Al iniciar y al confirmar cada entrega**, el TC58e verifica:
- un latido válido de **menos de 30 s**;
- que no haya retención sobre esos SSCC;
- la versión vigente del manifiesto;
- que el estado **no cambió durante la operación**.

Si algo no se cumple, no confirma la entrega. Así se acota la ventana en que una falla del controlador podría dejar un estado viejo. La prueba V17 se hace con el conductor **dentro del local del cliente**.

**El bloqueo es informático y operacional, no físico:** no impide descargar a mano. Lo complementan la capacitación (RT‑22.04), la segregación de lo retenido en la caja y el registro de toda excepción.

### 7.2 NO CONFIABLE

**El TC58e pasa a NO CONFIABLE** y retiene todos los SSCC de frío del compartimento afectado cuando ocurre cualquiera de estas cosas:
- pasan 30 s sin un latido válido de frescura;
- recibe una «alarma independiente» por el transmisor de cabina;
- arranca o se reinicia la aplicación;
- se reemplaza el terminal.

**Para salir de NO CONFIABLE** hacen falta, a la vez:
- que el controlador entregue una serie **continua de sus propias sondas** que cubra todo el intervalo;
- que todas esas sondas estén sanas;
- que no haya crítica en el intervalo;
- que la regla sea la misma y el registro haya sobrevivido al reinicio.

Si no se cumplen, solo sale con una **decisión de Calidad**. La foto de la pantalla del equipo de frío es **evidencia auxiliar**: no reconstruye la exposición. Recuperar la comunicación **solo** cierra la causa «falta de información»; no borra otras retenciones.

**Terminal de reserva o reinstalado:** arranca en NO CONFIABLE. Recupera del controlador, por la red de cabina, el manifiesto firmado, las retenciones abiertas, las decisiones aplicadas y las últimas versiones antirrepetición. Hasta completarlo, no habilita entregas (V18).

### 7.3 Órdenes de decisión

| Requisito | Implementación |
|---|---|
| Autor | Perfil Calidad en Keycloak con segundo factor |
| Contexto | Viaje, compartimento, incidente, subconjunto de SSCC y **revisión de estado evaluada** |
| Antirrepetición | Versión monótona por incidente; el TC58e guarda la última versión aplicada |
| Validez | Solo se aplica si: el incidente sigue abierto; la versión es mayor; no caducó; **la revisión de estado del TC58e es igual a la evaluada por Calidad** (si el TC58e conoce eventos posteriores, rechaza y pide una nueva evaluación); y la orden autoriza los SSCC concretos |
| Disposición frente a autorización | La **disposición sanitaria** («el producto está apto») es distinta de la **autorización para entregar ahora**. Si al llegar la liberación el compartimento **sigue fuera de rango**, la entrega sigue bloqueada |
| Alcance | Una liberación de un incidente no levanta retenciones de otros |
| Confirmación | El TC58e devuelve «aplicada» o «rechazada» con el motivo |
| Ante duda | Se mantiene la retención |
| Rutas | Por C1/C2 al TC58e; por SBD: Edge Pro → controlador → TC58e. Si el controlador falló, la orden espera; el producto sigue retenido, que es el estado seguro |

### 7.4 Reloj

- **Hora:** GNSS como fuente principal y NTP como secundaria. Desviación máxima tolerada: 2 s.
- **Intervalos** (latidos, caducidades, retardos): se miden con reloj **monótono**.
- **Auditoría:** usa UTC trazable.
- **Si el reloj no es confiable** (sin GNSS ni NTP desde el arranque, o salto detectado), los eventos se marcan y **ninguna orden se aplica por comparación de horas**: las decisiones se validan por revisión de estado y versión, no por hora.

### 7.5 Credencial de terreno de 14 h

El SD4 limita la credencial a 14 h, y una ruta puede durar 14,5 h. Con internet en el camión, el TC58e **renueva la credencial a las 12 h** por cualquier camino IP. Si no hay ningún camino en ese momento, rige el SD4: se conserva lo capturado y las nuevas operaciones protegidas esperan la renovación. Ese caso se declara como operación degradada.

---

## 8. Acuses, bandeja de salida y retención post‑A2

| Acuse | Qué confirma | Uso |
|---|---|---|
| A1 `PUBACK` | Llegada al broker | No permite borrar |
| **A2 Ingesta** | Evento y obligación de notificar guardados en la misma transacción (bandeja de salida del SD4) | El evento sale de la **cola de envío** |
| A3 por canal | Cada canal informa: pendiente, aceptado o fallido | Diagnóstico; **no** inicia relojes |
| A4 Entrega del proveedor | Informativo (los recibos de SMS pueden tardar hasta 72 h [H]) | No se usa para tiempos |
| **A5 Acuse humano** | Persona identificada, incidente concreto. La respuesta por SMS debe incluir el **código del incidente**; un «OK» sin código no cierra nada | Detiene el escalamiento por falta de acuse |
| **A6 Acción** | Decisión o acción registrada | Detiene el escalamiento por falta de acción |

**Archivo local después de A2.** El evento sale de la cola de envío, pero el controlador conserva una **copia confirmada durante 72 h**, o hasta que la plataforma confirme la replicación en us‑east‑1. Ante la pérdida de la región después de A2, el camión **reenvía** esos eventos al endpoint de recuperación (V20).

---

## 9. Notificación y escalamiento

- **El reloj de escalamiento parte de A2.** El tiempo total se informa desde la detección.
- Cada canal tiene su propio estado y su propio plazo. **No se espera a que todos terminen.**
- Si **ningún canal fue aceptado** en 60 s, se genera una alerta técnica al NOC.

| Severidad | t = 0 (desde A2) | Escalamiento por falta de acuse (A5) | Escalamiento por falta de acción (A6) |
|---|---|---|---|
| ADVERTENCIA | Aviso en la aplicación, SMS y WhatsApp en paralelo | Voz al vencer el plazo de la familia | Segundo nivel al vencer el plazo de acción |
| CRÍTICA, NO CONFIABLE, «controlador caído», contradicción | Aviso en la aplicación, SMS, WhatsApp **y voz**, en paralelo | Segundo nivel y jefatura | Jefatura y despacho |

**Canales:**
- SMS por SNS.
- WhatsApp por AWS End User Messaging Social (INT‑11).
- Voz por AWS End User Messaging SMS and Voice (Chile soporta voz [H]).

Calidad fija los plazos por familia con justificación sanitaria.

---

## 10. Fallas de la nube por etapa

| Etapa | Detector | Plazo | Recuperación | Copia durable |
|---|---|---|---|---|
| Certificado del dispositivo rechazado | El controlador: sin conexión MQTT | 20 s | Pasa al otro camino IP y a C3; alerta de certificado | Cola local |
| Regla de IoT Core sin coincidencia | El controlador: sin A2 | 20 s | Otro camino y C3; incidente técnico | Cola local |
| Error en la acción de una regla | Acción de error de IoT Core → SQS [H] | Inmediato | Reproceso desde SQS | SQS |
| Consumidor detenido | Antigüedad del mensaje en SQS | 60 s | Reinicio automático y alarma | SQS |
| M9 cae después de guardar | Antigüedad de la bandeja de salida | 60 s | Despachador reintenta | Aurora |
| Proveedor de mensajería caído | Ningún canal aceptado | 60 s | Otros canales; NOC | Bandeja de salida |
| **Región sa‑east‑1 caída** | **Monitoreo sintético desde fuera de la región** (us‑east‑1 y un servicio externo) | 2 min | Ruta SBD alternativa (V12), conmutación del SD4 4.3.2, reenvío del archivo post‑A2 | Archivo local de 72 h |

CloudWatch en la misma región no es el único detector de una caída de esa región.

---

## 11. SLA y objetivos

### 11.1 SLA técnico

| Tramo | Con C1/C2 | Solo C3 |
|---|---|---|
| T1 · Fuera de rango → advertencia | ≤ 35 s + respuesta de la sonda (objetivo ≤ 20 s) [E] | Igual |
| T2 · → alarma en cabina y retención local | ≤ 5 s | ≤ 5 s |
| T3 · → A2 | ≤ 30 s | ≤ 3 min [C] |
| T4 · A2 → primer canal aceptado | ≤ 15 s | ≤ 15 s |
| **Advertencia emitida** | **≤ 2 min** | **≤ 5 min** |

### 11.2 SLA de LafroX con Puelche

| # | Compromiso | Meta |
|---|---|---|
| SLA‑1a | Viajes con registro completo y conciliado | ≥ 99,5 % [P] |
| SLA‑1b | Fallas de integridad gestionadas | 100 % en ≤ 24 h [P] |
| SLA‑2 / 3 | Advertencia emitida con C1/C2 / solo C3 | ≤ 2 min en ≥ 99 % / ≤ 5 min en ≥ 95 % |
| SLA‑4 | Temperatura en los indicadores del día | ≤ 5 min (RT‑05.29) con cualquier camino; operación degradada declarada sin red |
| SLA‑5 | Curva en la puerta, con antigüedad ≤ 5 min o marcada como incompleta | 100 % |
| SLA‑6 | Retención local ante CRÍTICA, NO CONFIABLE o contradicción | 100 % [a demostrar] |
| SLA‑7 | Expediente certificado conciliado | ≤ 2 h tras el regreso [P] |
| SLA‑8 | Retiro sanitario por lote con historia térmica | < 2 h (criterio n.º 1) |
| SLA‑9 | Plataforma de extremo a extremo | ≥ 99,9 % mensual (SD4) |

### 11.3 Objetivos operativos (Puelche, con soporte de LafroX)

- **A5 y A6** en los plazos por familia, con turnos de guardia durante las rutas, nómina, teléfonos de servicio y simulacros.
- **Procedimientos de contingencia** por ruta (§7.1).

### 11.4 Proveedores

- **Starlink directo:** según la página oficial consultada el 23‑10‑2026, el SLA del 99,9 % no cubre el kit Performance Gen 3 ni la Mini, y excluye obstrucciones [H]. Se exige confirmación contractual.
- **Servicios gestionados** (Hughes Chile, Entel Empresas, Movistar Empresas, Tesacom), **Iridium y operadores celulares:** por contrato [C].

---

## 12. Trazabilidad, retención y evidencia

| Riesgo | Control |
|---|---|
| Salida sin medición, regla o respaldo | **Chequeo previo al despacho en M5:** termógrafos registrando, calibración vigente, sondas sanas, controlador, módulo independiente, transmisor y Edge Pro operativos, baterías A y B cargadas, manifiesto y reglas cargados en los tres equipos. Si algo falla, el camión no sale |
| Sensor equivocado | Asociación termógrafo ↔ camión ↔ viaje ↔ SSCC por escaneo; sellos |
| Borrado de memoria del termógrafo | Reinicio solo por perfil autorizado y solo con el A2 de una descarga completa con CRC válido; contraseñas BLE/NFC en Secrets Manager con auditoría (ELA [H]) |
| Huecos | Conciliación; cada hueco abre una falla (SLA‑1b) y cuenta contra SLA‑1a |
| Manipulación antes de subir | El CRC16 no autentica [H, NIST]. El TC58e firma la descarga y registra su hash. **Riesgo residual:** el termógrafo no firma sus lecturas |
| Retención documental | S3 con bloqueo de objetos **en modo cumplimiento**. Plazos: **temperaturas 5 años** y **evidencia de entrega 6 años** (RT‑05.10 del caso); incidentes y decisiones con el plazo mayor de lo que respaldan. Las claves KMS se conservan por el mismo plazo. Exportación en formato abierto (RT‑05.22) y relación lectura ↔ incidente ↔ decisión ↔ POD por identificadores |

---

## 13. Recálculo de cantidades y dimensionamiento (24‑10‑2026)

Base: constantes de `Dimensionamiento/dimensionamiento/calculo.py` (fuente única de la memoria de cálculo del SD4):
- 28 camiones con frío (18 propios y 10 de terceros; caso, tabla de flota);
- ventana de ruta de 14,5 h;
- 145 bytes por lectura;
- factor de almacenamiento 0,25;
- reserva del 10 % por tipo, redondeada hacia arriba (BTT §8.4);
- la flota refrigerada no crece al año 3 (S‑38).

### 13.1 Cantidades del T‑11

| Componente | Instalados | Reserva | **Total** | T‑11 actual |
|---|---|---|---|---|
| **Termógrafos EN 12830 (B‑03)** | 56 (2 × 28) | 6 | **62** | 31 (28 + 3) |
| Controlador local | 28 | 3 | 31 | — |
| Módulo de alarma independiente | 28 | 3 | 31 | — |
| Transmisor Bluetooth de la alarma independiente | 28 | 3 | 31 | — |
| Iridium Edge Pro | 28 | 3 | 31 | — |
| Router multi‑módem | 28 | 3 | 31 | — |
| Kit Starlink u OneWeb | 28 | 3 | 31 | — |
| Sondas cableadas principales (3 por camión) | 84 | 9 | 93 | — |
| Sonda del módulo independiente (1 por compartimento; base 1) | 28 | 3 | 31 | — |
| Sensor de puerta (1 por puerta de carga; base 1) | 28 | 3 | 31 | — |
| Batería y cargador del circuito A | 28 | 3 | 31 | — |
| Batería y cargador del circuito B | 28 | 3 | 31 | — |
| UPS del circuito C | 28 | 3 | 31 | — |
| Luz y zumbador (2 por camión) | 56 | 6 | 62 | — |
| SIM M2M (2 del router + 1 del controlador) | 84 | 9 | 93 | — |
| Iridium Certus 700 (opcional) | 0 o 28 | 0 o 3 | 0 o 31 | — |

- Los 31 termógrafos actuales se reutilizan: se compran **31 adicionales**, si el mapeo confirma 2 por camión.
- Las bases «1 por compartimento» y «1 por puerta» se ajustan con el inventario real de carrocerías.
- Los TC58e (96 + 10) no cambian.

### 13.2 Lecturas y mensajes por día (INT‑05)

| Concepto | Actual (SD4) | Nuevo | Cálculo |
|---|---|---|---|
| Lecturas de cámaras | 6.048 | 6.048 | 21 × 288 (sin cambio) |
| Lecturas de termógrafos | 4.872 | **9.744** | 56 × 174 |
| Lecturas de sondas de camión | — | **73.080** | 28 × 3 × 870 (una por minuto en 14,5 h) |
| **Lecturas de camiones** | **4.872** | **82.824** | **× 17,0** |
| **Lecturas totales** | **10.920** | **88.872** | **× 8,1** |
| Mensajes de camión a IoT Core | 4.872 | **24.360** | 28 × 870 (un mensaje por minuto con las 3 sondas) |
| Eventos (C1 + C2) | — | 224 [E] | 28 × 4 eventos × 2 caminos |
| Descargas certificadas | — | 56 archivos | Una por termógrafo y día |
| **INT‑05, mensajes/día** | **10.920** | **30.632** | 6.048 + 24.360 + 224 |
| **Total de integraciones** (tabla de 4.2.11 y Anexo 4‑I) | **224.652 / 342.933** | **244.364 / 362.645** | + 19.712 |
| Total bruto de `calculo.py` | 230.252 / 353.333 | 249.964 / 373.045 | + 19.712 |

**Mensajes SBD** (cola SQS, aparte de IoT Core), con un lote cada 3 min (20 mensajes por hora) solo cuando no hay C1/C2:

| Escenario | Por camión y día | Por camión y mes (26 días) | Flota por día | Bytes por camión y mes |
|---|---|---|---|---|
| Normal (4 h sin IP) | 80 | 2.080 | 2.240 | ≈ 83 KB |
| Adverso (14,5 h sin IP) | 290 | 7.540 | 8.120 | ≈ 302 KB |

A eso se suman las alarmas, los acuses de bajada y las órdenes. Se cotiza **por mensaje**, incluidos los mínimos de facturación.

### 13.3 Almacenamiento y ancho de banda

| Concepto | Actual | Nuevo |
|---|---|---|
| Temperatura, crudo por año | 0,58 GB | **4,70 GB** |
| Temperatura, almacenado por año (factor 0,25) | 0,14 GB | **1,18 GB** |
| Temperatura, crudo en 5 años | 2,89 GB | **23,52 GB** |
| DynamoDB N‑06 (30 días) | 0,048 GB | **0,387 GB** |
| Archivos certificados de termógrafo | — | ≈ 0,21 GB/año; 1,07 GB en 5 años (S3 con bloqueo de objetos) |
| Datos IP por camión (≈ 300 bytes por mensaje con TLS) | — | ≈ 0,26 MB/día; ≈ 6,8 MB/mes. No afecta el plan Starlink de 50 GB |
| Descargas de termógrafos por la red del CD | — | ≈ 0,58 MB/día. Sin efecto en la tabla de ancho de banda de 4.2.11 |

**Conclusión:** el volumen crece 8 veces en lecturas y casi 3 veces en mensajes de INT‑05, pero sigue siendo pequeño:
- 30.632 mensajes al día equivalen a 0,35 mensajes por segundo en promedio;
- 23,5 GB en 5 años.

**No cambia** la elección de IoT Core, DynamoDB ni S3, ni el ancho de banda de los sitios. Sí cambian las cifras publicadas.

### 13.4 Lugares del SD4 que cambian si se adopta (no aplicado)

| Archivo | Línea | Cambio |
|---|---|---|
| `04/formularios/T11/15_anexo_t11.tex` | 55 | B‑03: 28 + 3 = 31 → 56 + 6 = 62 |
| `04/formularios/T11/15_anexo_t11.tex` | 92 | N‑08: «3 gateways y 28 termógrafos» → 28 controladores, 28 Edge Pro y 56 termógrafos; filas nuevas de §13.1 |
| `04/partes/4.2_fisica/12_k_dimensionamiento.tex` | 123 | Temperatura: 0,58 → 4,70 GB/año; 2,89 → 23,52 GB en 5 años |
| `04/partes/4.2_fisica/12_k_dimensionamiento.tex` | 140 y total | INT‑05: 10.920 → 30.632; total 224.652/342.933 → 244.364/362.645 |
| `04/anexos/logica/partes/10_anexo_4_1_i_volumen_de_mensajes.tex` | 14 y 25 | Igual que 4.2.11 |
| `04/anexos/logica/partes/08_anexo_4_1_g_catalogo_de_interfaces_internas.tex` | 46 | INT‑05: nuevo volumen, una lectura por minuto, lote SBD cada 3 min |
| `04/anexos/fisica/16_anexo_4b_memoria_calculo.tex` | 197, 214, 243, 386 | Lecturas, totales y GB/día de telemetría |
| `04/partes/4.2_fisica/02_a_emplazamiento.tex` | 196, 238 | N‑08 y B‑03 |
| `04/partes/4.1_logica/05_modulos_funcionales_y_limites_de_contexto.tex` | 45 | 28 → 56 termógrafos, más las sondas |
| `Dimensionamiento/dimensionamiento/calculo.py` | 83, 408, 438 | Parámetros nuevos: termógrafos por camión, sondas por camión y minutos por mensaje |
| Figura ARQL‑01 | — | Muestra 230.252 en el total de mensajes: debe actualizarla el equipo en draw.io |

---

## 14. Pruebas de viabilidad (antes de cualquier compra)

Las excursiones de prueba usan sondas o carga de ensayo, nunca alimento comercial.

| # | Prueba | Aprobación |
|---|---|---|
| V1 | Controlador por Ethernet y LTE con A2; cola persistente; respuesta de cada sonda | Evento completo; respuesta ≤ objetivo |
| V2 | Calentar la sonda, sin router ni LTE; capturar el SBD crudo | Formato de §4 íntegro; llega a M9 y a un responsable; vuelve el A2 |
| V3 | TC58e lee los termógrafos con el controlador apagado | Si falla, queda solo como visor |
| V4 | Bluetooth a través de la caja cargada | Si falla, los termógrafos se leen al regreso |
| V5 | Alimentación: autonomía de A, B y C; arranque, caída de tensión, batería envejecida, temperatura extrema | A y B ≥ 24 h, sin reinicios |
| V6 | Controlador o circuito A sin energía durante una excursión | Zumbador 2; el Edge Pro envía alarma y «controlador caído»; **el TC58e retiene** |
| V7 | Sin Bluetooth desde la caja y sin internet | Curva en el TC58e con su antigüedad |
| V8 | C1 y C2 simultáneos durante horas | Sin desconexiones por `clientId` |
| V9 | Evento persistido con la notificación interrumpida; descarga cortada; corte de energía durante la escritura | Se recupera la notificación; no se borra el registro; no se reutilizan secuencias |
| V10 | Solo SBD en escenario normal y adverso, con alarmas durante la recuperación de curvas | Las alarmas no esperan; latencia de lectura ≤ 4,5 min; consumo real de mensajes |
| V11 | Crítica sin acuse; acuse sin acción | Escalan los dos relojes |
| V12 | Caída regional simulada sin celular | Alerta legible a una guardia que acusa |
| V13 | Duplicados, retrasos y reordenamiento, incluida una **crítica tardía de otro compartimento** | La crítica produce su efecto; el estado final es correcto en los tres sistemas |
| V14 | **Adquisición congelada con el proceso de comunicaciones vivo** | El latido de frescura falla y el TC58e retiene en ≤ 30 s |
| V15 | Órdenes repetidas, antiguas, caducadas, de otro incidente, con firma inválida, **basadas en una revisión anterior** o con el producto **aún fuera de rango** | Todas rechazadas o sin autorización de entrega |
| V16 | Alarma independiente con el controlador diciendo NORMAL | El TC58e retiene por la señal Bluetooth de cabina |
| V17 | Falla del controlador **durante una entrega dentro del local del cliente** | No se confirma la entrega con un estado vencido |
| V18 | TC58e reiniciado, reemplazado, restaurado desde una copia vieja o con la base local borrada, sin internet | Ninguna entrega antes de recuperar el estado del controlador |
| V19 | Android: pantalla apagada, otra aplicación, ahorro de batería, proceso terminado, permisos revocados, actualización por MDM | Al volver, arranca en NO CONFIABLE y se recupera |
| V20 | Pérdida de la región justo después de A2 | El evento y su notificación se recuperan desde el archivo local |
| V21 | Turno completo de 14 h sin señal y reconexión, con POD, fotos, curvas, eventos y decisiones simultáneos | Sin pérdida de datos y sincronización ≤ 10 min (RT‑03.13 del caso) |
| V22 | Fallas de sonda de §6 (abierta, en corto, desviada) | Se aplica la matriz |

Además se prueban **combinaciones normales de operación**: sin celular más avería de un equipo, motor apagado más batería envejecida, mala visibilidad satelital más reinicio.

---

## 15. Piloto y criterios estadísticos

- **Descubrimiento de fallas:** 6 semanas en 4 camiones (Empedrado/Chanco/Cauquenes, Pinto/Alto Biobío, uno urbano y uno de transportista). Se comparan Starlink y OneWeb, con y sin Certus.
- **Acreditación de porcentajes**, con cero fallas y 95 % de confianza:

| Meta a demostrar | Ensayos independientes necesarios |
|---|---|
| ≥ 95 % | ≈ 59 |
| ≥ 99 % | ≈ 300 |
| ≥ 99,5 % (SLA‑1a) | ≈ 598 viajes |

- **Representatividad:** los porcentajes se acreditan **por población** (por ruta y por camino), sin mezclar laboratorio y ruta en un solo número.
- **Validación en producción:** los SLA se miden con todos los eventos reales y provocados de los primeros 3 meses de operación, antes de fijarlos en el contrato.

---

## 16. Costos (interno; **no va a la Oferta Técnica**, BA art. 50.2)

**Publicados:**
- Starlink Performance: CLP 1.476.000 con IVA.
- Prioridad Local 50 GB: CLP 38.500/mes [H].

**Por cotizar en Chile [C]:**
- Equipos de §13.1.
- Desarrollo e integración del controlador, el Edge Pro y el protocolo.
- Plan SBD por mensaje en escenario normal y adverso.
- Guardias de Calidad.
- Mensajería y voz.
- Instalación, calibración y recambio.
- Firmware, licencias, soporte y repuestos.
- Servicio en camiones de terceros.
- Planes M2M.

**Requisito previo a cualquier instalación:** una matriz de certificación de Subtel por equipo y función radioeléctrica [C].

No se presenta un total hasta tener cotizaciones.

---

## 17. Opciones de conectividad revisadas

| Opción | Situación en Chile | Rol |
|---|---|---|
| Celular, dos operadores | Disponible [H] | Siempre |
| Starlink (directo o vía Entel Empresas, Movistar Empresas, Hughes/Speedcast o Tesacom) | Disponible; uso en movimiento autorizado [H] | Internet principal (candidato) |
| OneWeb gestionado por Hughes Chile | Ofrecido con movilidad [H]; contrato en movimiento [C] | Internet principal (candidato) |
| Iridium SBD (Edge Pro) | Globalsat Chile o Compan [H] | Satélite de alarmas. **No elimina las obstrucciones**: los árboles y cerros también lo degradan [H] |
| Iridium Certus 200/700 | Globalsat Chile o Compan [H] | Respaldo IP y de voz opcional |
| Satélite al celular Entel‑Starlink | SMS y apps desde 2026, solo en teléfonos de una lista sin Zebra [H] | Procedimiento del conductor |
| Iridium NTN Direct y otros NB‑IoT satelitales | Anunciados o en pruebas; **sin oferta comercial validada en Chile** [H/C] | Reevaluar si aparece una oferta local |
| Inmarsat BGAN | Globalsat Chile [H] | No preferido: satélite geoestacionario bajo hacia el norte [I]. **Confirmar con la geometría de las rutas** antes de descartarlo |
| Viasat IoT Pro, Intelsat FlexMove | No confirmados [C] | No considerados |
| HughesNet | Servicio fijo [H] | No aplica |

---

## 18. Fuentes (consultadas el 23 y 24‑10‑2026)

**Proyecto:**
- Caso 02, BTT y Bases Administrativas (art. 50.2): `Bases/`
- Subdocumento 4, T‑11, Anexos 4‑B, 4‑G y 4‑I, y SD3.
- `Dimensionamiento/dimensionamiento/calculo.py` y `resultados.md`.

**Equipos y servicios:**
- Teltonika FMC650: https://teltonika-gps.com/products/trackers/fmc650 · SBD: https://wiki.teltonika-gps.com/view/FMC650_Short_Burst_Data
- Iridium Edge Pro: https://www.iridium.com/products/iridium-edge-pro · ficha anterior: https://www.asiasatellite.co/vi/mwdownloads/download/link/id/452
- Iridium CloudConnect: https://www.iridium.com/services/iridium-cloudconnect
- Tamaños SBD: https://www.iridium.com/services/enhanced-short-burst-data-us-government
- Destinos SBD: https://metocean.com/?p=2912
- Iridium NTN Direct: https://www.iridium.com/services/iridium-ntn-direct
- Iridium y obstrucciones: https://ifp.iridium.com/go-exec-faqs/
- MissionLINK 700: https://www.iridium.com/products/missionlink-700
- Peplink con Iridium: https://www.iridium.com/peplink-iridium

**Starlink:**
- Movilidad terrestre: https://starlink.com/cl/business/mobility
- SLA: https://starlink.com/cl/support/article/b7142f8e-9762-6fcf-03f5-0d53c2895b3f
- Ficha Performance: https://starlink.com/public-files/specification_sheet_performance.pdf

**Proveedores en Chile:**
- Hughes Chile: https://www.hughes.com/cl/soluciones/servicios-satelitales-systems-terrestre/hughes-leo
- Entel Empresas: https://ce.entel.cl/tendencias-tecnologicas/articulos/entel-empresas-junto-a-starlink
- Movistar: https://www.df.cl/empresas/telecom-tecnologia/tras-acuerdo-de-distribucion-con-starlink-ya-no-existe-lugar-al-que
- Tesacom: https://www.tesacom.net/transporte
- Globalsat: https://www.gsat.cl/collections/internet-satelital-portatil
- Subtel, satélite al celular: https://www.subtel.gob.cl/chile-se-posiciona-como-primer-pais-de-la-region-y-quinto-del-mundo-entel-y-starlink-d2c-amplian-sus-servicios-incluyendo-aplicaciones-como-whatsapp-y-google-maps/
- Subtel, certificación de equipos: https://www.subtel.gob.cl/certificacion-de-equipos-de-telecomunicaciones/

**ELA:**
- Ficha: https://elainnovation.com/en/catalogue/blue-puck-t-en12830-en/
- Nota de aplicación: https://www.logicbus.com.mx/pdf/catalogos/Application-Note-datalogger-EN-12830-04B-EN.pdf

**AWS y Android:**
- Bandeja de salida transaccional: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html
- MQTT: https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html
- `clientId`: https://docs.aws.amazon.com/iot/latest/developerguide/iot-policy-actions.html
- Errores de reglas: https://docs.aws.amazon.com/iot/latest/developerguide/rule-error-handling.html
- Recibos SMS: https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-sets-event-destinations.html
- KMS Sign: https://docs.aws.amazon.com/kms/latest/APIReference/API_Sign.html
- Voz por país: https://docs.aws.amazon.com/end-user-messaging/latest/userguide/nx-supported-countries-south-america.html
- Android, Bluetooth en segundo plano: https://developer.android.com/develop/connectivity/bluetooth/ble/background

**Otras:**
- NIST, CRC: https://csrc.nist.gov/glossary/term/cyclic_redundancy_check
- Mediciones de Starlink en movimiento: https://arxiv.org/html/2512.19639v2 · https://arxiv.org/html/2403.13497v1
- Plantaciones en Empedrado: https://www.mdpi.com/1999-4907/9/3/141/htm

---

## 19. Estado de las observaciones de revisión (v4, v5 y v6)

**Estados posibles:** **corregido** (cambio de definición o de texto) · **corregido en diseño, pendiente de prueba** · **pendiente de terceros**.

| Observación | Dónde | Estado |
|---|---|---|
| v4 · Controlador como punto único; A2 y notificación; recibo de SMS; SBD frente a telemetría; `clientId`; R1; curva sin Bluetooth | §3, §4, §7, §8 | Corregido en diseño, pendiente de prueba (V1, V6–V10) |
| v4/v5 · Caída de AWS y ruta alternativa | §3.4, §10 | Pendiente de terceros y prueba (V12, V20) |
| v5 · Baterías independientes; retención sin controlador; órdenes firmadas; emisión frente a acuse; reglas por familia | §3.5, §5, §7 | Corregido en diseño, pendiente de prueba |
| v6‑1 · Crítica tardía archivada | §5.3 | Corregido en diseño, pendiente de prueba (V13) |
| v6‑2 · Escalamiento bloqueado por un canal | §8, §9 | Corregido en diseño, pendiente de prueba (V11) |
| v6‑3 · Controlador vivo pero erróneo | §3.6, §7.2, transmisor de cabina | Corregido en diseño, pendiente de prueba (V14, V16) |
| v6‑4 · Fallas de sensor sin consecuencia | §6 | Corregido; prueba V22 |
| v6‑5 · «25 lotes por mensaje» | §4 (lote = 6 bytes; máximo 52 minutos por mensaje) | Corregido |
| v6‑6 · Esquema SBD incompleto | §4 (manifiesto, productores, épocas, cinco esquemas, vectores de prueba) | Corregido en diseño, pendiente de prueba |
| v6‑7 · Tamaño de la orden marcado [H] | §4 (≤ 125 bytes calculados; ya no se marca como verificado) | Corregido en diseño, pendiente de prueba (V15) |
| v6‑8 · Liberación con contexto viejo | §7.3 (revisión de estado; disposición separada de la autorización) | Corregido en diseño, pendiente de prueba (V15) |
| v6‑9 a 11 · Ventana de 2 min, terminal de reserva, Android | §3.6, §7.1, §7.2 | Corregido en diseño, pendiente de prueba (V17–V19) |
| v6‑12 a 14 · Módulo de umbral fijo, estados por lote, salida de NO CONFIABLE | §3.3, §5.2, §7.2 | Corregido |
| v6‑15 · Activación de C3 | §3.4 (por ausencia de A2) | Corregido |
| v6‑16 · Latencia de los lotes SBD | §5.4 (lote cada 3 min; ≤ 4,5 min) | Corregido en diseño, pendiente de prueba (V10) |
| v6‑17 · A5 sin acción | §8, §9 (dos relojes; acuse con código de incidente) | Corregido |
| v6‑18 · Fallas de nube | §10 | Corregido |
| v6‑19 · Archivo post‑A2 | §8 | Corregido en diseño, pendiente de prueba (V20) |
| v6‑20 · Reloj | §7.4 | Corregido |
| v6 · Medición, alimentación, antenas, bloqueo informático, contingencia | §3.2, §3.3, §7.1, V5 | Corregido; antenas y Subtel pendientes de terceros |
| v6 · Bases: cantidades, telemetría, RT‑05.29, 14 h y sincronización, retención, precios | §13, §5.4, §7.5, V21, §12, aviso inicial | **Recalculado y corregido**; el SD4 no se modifica hasta adoptar |
