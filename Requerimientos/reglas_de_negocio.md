# Registro de Reglas de Negocio — Caso 02 · Logística (Distribuidora Puelche S.A.)

Licitación TFEP-01/2026. Documento de trabajo del catálogo de requerimientos (Cap. 17.1).

> **Propósito.** Las reglas que la solución debe respetar y que el caso **no explicita** como requerimiento
> formal. Este registro es un entregable intermedio dentro del diagrama de traducción del Cap. 17.1 del caso:
> se redacta aquí como referencia de trabajo y se **incorpora al informe** dentro del "esquema de solución y
> alcance" / registro de requerimientos del Cap. 17.1 (no como capítulo aparte, conforme al T-22 y a la
> política de AGENTS).
>
> **Formato (alfabético, trazable):** por cada regla se indica qué se captura, en qué punto del proceso,
> por quién, con qué consecuencia si se incumple, más el origen en el caso y el (los) requerimiento(s)
> RF/RNF que la implementa(n).

Convención de códigos: `RNG-XX` (regla de negocio). Las reglas se derivan de las **decisiones 16.1 ya
resueltas** (ver `decisiones.md` D1–D40) y de las bases, de modo que **no contradicen** el resto de la propuesta.
El origen cita el párrafo / entrevista / indicador / decisión del caso o el RT correspondiente.

---

## 1. Reglas por dominio de negocio

### 1.1 Reglas de inventario y stock

**RNG-01 — Asignación y reserva de stock (momento y orden).**

| Dato | Contenido |
|---|---|
| **Qué captura** | El momento en que el stock se compromete y el criterio de orden ante pedidos que compiten por el mismo producto. |
| **En qué punto** | Al **confirmar** el pedido en el sistema de gestión (servidor central); no en la toma ni en la preparación. |
| **Por quién** | Sistema de gestión, en la confirmación; el preventista lo gatilla; el jefe de bodega administra la regla. |
| **Regla** | La reserva se hace efectiva por orden de llegada de la confirmación. El segundo preventista que confirma sobre el mismo stock queda con **quiebre parcial registrado** (no bloquea al primero). |
| **Si se incumple** | Doble compromiso de stock → quiebres de despacho no previstos, OTIF caído y reclamos del cliente. |
| **Origen** | Caso Cap. 16.1, Decisión **D8**; entrevista preventa (Cap. 8). |
| **RF/RNF que la implementan** | RF-03.03 (reserva en confirmación), RF-02.05 (stock disponible), RF-05.03 (faltante con causa). |

**RNG-02 — Stock disponible vs. comprometido y en tránsito.**

| Dato | Contenido |
|---|---|
| **Qué captura** | La definición de "stock disponible para venta" y el tratamiento del inventario en tránsito. |
| **En qué punto** | En la consulta de stock (preventa) y en la consolidación multi-sitio (bodega). |
| **Por quién** | Sistema; lo consulta el preventista y el jefe de bodega. |
| **Regla** | Disponible = físico − comprometido por pedidos confirmados pendientes de preparar. El stock **en tránsito NO suma** al disponible hasta la recepción confirmada en destino. En modo offline, el dato es **indicativo** con antigüedad visible; los conflictos de sincronización se resuelven por orden cronológico de registro. |
| **Si se incumple** | Sobreventa de stock físico no disponible o venta de inventario en tránsito → quiebres y diferencias de inventario. |
| **Origen** | Caso Cap. 2.3 (abastecimiento multi-sitio), Cap. 16.1 **D8**; RT-03.12. |
| **RF/RNF que la implementan** | RF-02.05 (stock disponible), RF-02.06 (en tránsito), RF-03.02 (stock offline). |

**RNG-10 — FEFO y vida útil remanente.**

| Dato | Contenido |
|---|---|
| **Qué captura** | El orden de salida del inventario y la alerta por vencimiento. |
| **En qué punto** | En la asignación de picking (preparación) y en la alarma de vida útil en bodega. |
| **Por quién** | Sistema (dirige el picking); preparador lo confirma; jefe de bodega gestiona alertas. |
| **Regla** | El picking asigna estrictamente **FEFO** (First Expired, First Out) por fecha de vencimiento de lote, con bitácora de excepción si el lote FEFO no está disponible. Se alerta cuando la vida útil remanente baja del umbral configurable (p. ej. 30 días). |
| **Si se incumple** | Salida de lote de mayor vida útil → vencimiento en almacén, merma (1,7 %) y riesgo sanitario. |
| **Origen** | Caso Cap. 4.8, Cap. 9.10; RF-02.09. |
| **RF/RNF que la implementan** | RF-05.05 (asignación FEFO en picking), RF-02.09 (gestión vencimiento), RF-05.03 (motivo de faltante). |

---

### 1.2 Reglas de crédito

**RNG-03 — Política de crédito en preventa.**

| Dato | Contenido |
|---|---|
| **Qué captura** | El límite de crédito del cliente y el comportamiento ante su superación al tomar el pedido. |
| **En qué punto** | En la toma del pedido por el preventista (en línea y offline). |
| **Por quién** | Preventista consulta; supervisor de crédito autoriza excepciones; sistema aplica bloqueos. |
| **Regla** | Un pedido que (sumado a la deuda vencida) supere el límite de crédito **dispara alerta**; si supera el **110 %** del límite, **bloquea el envío**. Toda excepción se autoriza de forma **registrada** por el supervisor de crédito (queda evaluador: supervisor, fecha y hora). En modo offline la excepción queda **aprobada a la sincronización** con respaldo presencial. |
| **Si se incumple** | Ventas a clientes morosos sin control → riesgo de cartera y descuadre (vinculado a la diferencia de $4,2 M/mes). |
| **Origen** | Caso Cap. 16.1 **D8/D40**, Cap. 8 (finanzas/cobranza). |
| **RF/RNF que la implementan** | RF-03.04/03.05 (consulta crédito), RF-03.08 (alerta), RF-03.09 (bloqueo 110 %), RF-03.10 (excepción). |

---

### 1.3 Reglas de calidad y cadena de frío

**RNG-04 — Excursión térmica y disposición del producto.**

| Dato | Contenido |
|---|---|
| **Qué captura** | Qué constituye una excursión térmica, quién decide y el efecto sobre el despacho. |
| **En qué punto** | En el transporte (equipo de frío) y en cámaras; en el bloqueo de despacho ante la excursión. |
| **Por quién** | Jefa de calidad define los parámetros (tiempo y grados por tipo de producto); el sistema alerta; el **conductor** decide la disposición final de la entrega en ruta. |
| **Regla** | Una excursión se define por **parámetros configurables** de tiempo y grados (RF-09.06). El sistema **alerta en tiempo real** (RF-09.05). El **bloqueo del despacho NO es automático**: el sistema habilita la acción y el conductor decide según el tipo de producto (RF-09.07). Monitorear ≠ decidir (HACCP/GDP exige decisión documentada). |
| **Si se incumple** | Producto con excursión despachado sin decisión → riesgo sanitario y retiro (pérdida como la del caso: 9 días, $31 M). |
| **Origen** | Caso Cap. 16.1 **D4**, Cap. 10 (restricción), RT-17.06; Cap. 17.2 (caso límite "bloquear el despacho"). |
| **RF/RNF que la implementan** | RF-09.05 (alerta), RF-09.06 (parametrización), RF-09.07 (bloqueo/decide conductor), RF-01.11 (valida térmica putaway). |

**RNG-13 — Secuenciación térmica de picking y validación por zona.**

| Dato | Contenido |
|---|---|
| **Qué captura** | El orden de recolección para minimizar la exposición térmica en pedidos mixtos y la validación de zona. |
| **En qué punto** | En la preparación de pedidos (picking) y en el putaway/almacenaje. |
| **Por quién** | Sistema (secuencia); preparador confirma; operador valida en putaway. |
| **Regla** | Las misiones se secuencian **seco → refrigerado → congelado**; se recoge el 100 % de los SKU de ambiente seco antes de liberar las ubicaciones de cámara. En putaway se valida la **compatibilidad térmica** de la ubicación destino; un SKU congelado no puede ubicarse fuera de zona congelada. |
| **Si se incumple** | Ruptura de cadena de frío → producto rechazado en recepción o despacho, merma y riesgo sanitario. |
| **Origen** | Caso Cap. 4.5, Cap. 2.3; RF-01.11, RF-04.05. |
| **RF/RNF que la implementan** | RF-05.04 (secuenciación térmica), RF-01.11 (validación térmica putaway), RF-01.08 (compatibilidad de ubicación). |

---

### 1.4 Reglas de reparto y entrega

**RNG-05 — Reintento de entrega / local cerrado.**

| Dato | Contenido |
|---|---|
| **Qué captura** | La conducta ante un local cerrado en la ventana comprometida y quién decide. |
| **En qué punto** | En la entrega, cuando el local está cerrado dentro de la ventana asignada. |
| **Por quién** | Conductor reporta "local cerrado"; el **sistema reagenda automáticamente**; el planificador administra la ventana registrada por cliente. |
| **Regla** | Si el local está cerrado en la ventana, el conductor reporta la condición, el sistema registra el envío **fallido** y lo **reagenda a la ventana horaria siguiente** más cercana registrada en la ficha del cliente. El **conductor no decide** por su cuenta; si persiste la indisponibilidad, los productos **regresan al almacén**. |
| **Si se incumple** | Reentregas no controladas (causa principal actual) → OTIF bajo y costo de servir alto. |
| **Origen** | Caso Cap. 16.1 **D3**, Cap. 8 (conductor/reparto). |
| **RF/RNF que la implementan** | RF-06.04 (local cerrado + reagenda), RF-04.07 (ventanas por cliente), RF-04.06 (ETA). |

**RNG-09 — Definición de "entrega cumplida", OTIF y Fill Rate.**

| Dato | Contenido |
|---|---|
| **Qué captura** | El criterio unívoco de entrega cumplida y las métricas de servicio. |
| **En qué punto** | En la medición diaria del servicio (OTIF/Fill Rate) y en la decisión de entrega parcial. |
| **Por quién** | Gerente comercial (métrica); sistema registra el POD; jefa de calidad contribuye. |
| **Regla** | Una entrega parcial **NO cuenta** como entrega cumplida: "In-Full" exige el 100 % de ítems y unidades. "On-Time" = fecha y ventana pactada. Fill Rate = unidades entregadas vs. pedidas. Perfect Order se contrasta contra la orden original. Toda entrega parcial queda como **desvío auditado** con causal tipificada. |
| **Si se incumple** | Criterios distintos por área → imposibilidad de acordar el estado real del servicio (problema declarado). |
| **Origen** | Caso Cap. 16.1 **D1**; Cap. 14.2 (OTIF 82,4 % actual, meta > 95 %). |
| **RF/RNF que la implementan** | RF-11.03 (OTIF diario), RF-11.04 (Fill Rate/Perfect Order). |

**RNG-14 — Capacidad del vehículo y carga dirigida inversa a ruta.**

| Dato | Contenido |
|---|---|
| **Qué captura** | Los límites de capacidad del vehículo y el orden de carga para respetar la secuencia de ruta. |
| **En qué punto** | En la asignación/planificación de rutas y en la carga del camión. |
| **Por quién** | Planificador (asignación); sistema bloquea; cargador ejecuta carga dirigida. |
| **Regla** | No se asigna una línea de pedido a una ruta si la sumatoria excede los **límites de peso o volumen nominales** del vehículo; y no se admite producto de **cadena de frío** en vehículo sin equipo de frío. La carga se dirige **en secuencia inversa a la ruta** (primer cliente a visitar = última bulto en subir); al completar, se verifica que todos los bultos fueron escaneados. |
| **Si se incumple** | Sobrecarga → rechazo en el andén o multa por peso; cadena de frío en vehículo seco → producto no entregable; carga fuera de secuencia → pérdida de tiempo de descarga. |
| **Origen** | Caso Cap. 4.4 y 4.5 (planetario y carga); criterio de aceptación #14. |
| **RF/RNF que la implementan** | RF-04.03 (bloqueo por capacidad), RF-04.05 (restricción cadena de frío), RF-05.07 (carga inversa). |

---

### 1.5 Reglas de devoluciones, envases y maestros

**RNG-06 — Tratamiento de devoluciones y efecto sobre el documento tributario.**

| Dato | Contenido |
|---|---|
| **Qué captura** | La devolución en el momento de la entrega y su efecto tributario/contable. |
| **En qué punto** | En la entrega (POD) y en el destino del devuelto en el andén de retorno. |
| **Por quién** | Conductor registra la devolución; jefe de bodega decide el destino en el andén; finanzas ejecuta la nota de crédito. |
| **Regla** | La devolución se registra en el POD (total o parcial, con SKU, cantidad y motivo desde catálogo), operando **offline**. Al retorno, el destino (reingreso a stock, venta con descuento, devolución al proveedor o destrucción) se decide en el andén y se transmite al ERP. El efecto sobre el **documento tributario ya emitido** se resuelve con **nota de crédito** emitida por el ERP (que no se reemplaza) por la cantidad rechazada, con retención legal mínima (6 años). |
| **Si se incumple** | Devoluciones sin registro → descuadre contable/financiero y pérdida de trazabilidad del devuelto. |
| **Origen** | Caso Cap. 16.1 **D12**, Cap. 9.8; RT-16.14. |
| **RF/RNF que la implementan** | RF-06.03 (rechazo), RF-08.01 (devolución offline), RF-08.02 (destino → ERP); RNF-08.02 (retención). |

**RNG-07 — Control de envases retornables.**

| Dato | Contenido |
|---|---|
| **Qué captura** | El mecanismo de control del parque de envases retornables. |
| **En qué punto** | En cada entrega (descuento de saldo) y devolución (suma), con actualización en línea o diferida. |
| **Por quién** | Conductor captura (RF-06.09); sistema lleva la cuenta corriente por cliente; preventista recibe alertas. |
| **Regla** | Se controla por **saldo por cliente** (cuenta corriente de envases retornables), no por unidad identificada. Cada entrega descuenta y cada devolución suma al saldo. Se alerta al preventista cuando el saldo supera el umbral configurado y se reporta diariamente la pérdida por cliente, tipo y zona. |
| **Si se incumple** | Pérdida no controlada del parque (68.000 canastillos / 9.400 pallets, 14 % anual) → costo de reposición. |
| **Origen** | Caso Cap. 16.1 **D10**, Cap. 14.1 (volumetría). |
| **RF/RNF que la implementan** | RF-08.03 (cuenta corriente), RF-08.04 (alerta), RF-08.06 (reporte pérdida), RF-06.09 (captura devolución). |

**RNG-08 — Cambio de precio entre toma de pedido y despacho.**

| Dato | Contenido |
|---|---|
| **Qué captura** | El precio aplicable cuando cambia entre la toma del pedido y el despacho. |
| **En qué punto** | En la facturación / despacho de la línea. |
| **Por quién** | Administrador comercial configura la excepción; sistema aplica el por defecto; el cliente recibe la alerta. |
| **Regla** | Por defecto se cobra el **precio vigente al despacho** de cada línea. Solo si hay una **excepción explícita** configurada por cliente o cadena se respeta el precio de la toma del pedido. Sin excepción y con cambio de precio, el sistema **alerta al cliente** antes de o junto con la facturación. |
| **Si se incumple** | Cobro inesperado al cliente → reclamos, pérdida de confianza y litigios de facturación. |
| **Origen** | Caso Cap. 16.1 **D9**, Cap. 9.3. |
| **RF/RNF que la implementan** | RF-03.11 (precio de despacho por defecto), RF-03.12 (excepción), RF-03.13 (alerta al cliente). |

**RNG-11 — Maestro de productos y resolución de códigos externos (GS1).**

| Dato | Contenido |
|---|---|
| **Qué captura** | Qué maestro manda ante cambios de formato/código del proveedor y cómo se resuelven los códigos de cadenas. |
| **En qué punto** | En la ficha de producto y en la recepción de pedidos EDI del canal moderno. |
| **Por quién** | Administrador de catálogo mantiene la ficha; sistema resuelve equivalencias; operador de excepciones EDI gestiona lo no resuelto. |
| **Regla** | Prevalece el **maestro interno de Puelche**: la ficha de producto es la única fuente autorizada y conserva historial de cambios de GTIN/SKU. Todo código externo (proveedor o cadena) se resuelve contra el maestro mediante una **tabla de equivalencias por cadena**; lo no resuelto queda en **bandeja de excepciones**. |
| **Si se incumple** | Cambio de código del proveedor no resuelto → producto duplicado o ilegible en bodega/preventa y pedidos EDI rechazados. |
| **Origen** | Caso Cap. 16.1 **D11**, Cap. 16.2 (GS1). |
| **RF/RNF que la implementan** | RF-01.10 (ficha de producto), RF-12.03 (equivalencias), RF-12.06 (excepciones EDI). |

---

### 1.6 Reglas de integración y sincronización

**RNG-12 — Enlace, sincronización y resolución de conflictos.**

| Dato | Contenido |
|---|---|
| **Qué captura** | El comportamiento tras la reconexión del enlace y el criterio de resolución de conflictos. |
| **En qué punto** | En toda operación desconectada (CD 24 h, terreno 14 h) y su reconciliación posterior. |
| **Por quién** | Sistema de sincronización automática; bitácora auditable. |
| **Regla** | Restablecido el enlace, la sincronización es **automática, con reconciliación determinista de conflictos**, regla de resolución documentada y **bitácora auditable** de las decisiones aplicadas. En terreno (14 h sin señal) el dato offline es indicativo; se registra la antigüedad y el stock se valida contra el servidor al reconectar. |
| **Si se incumple** | Pedidos perdidos o duplicados en la reconexión y quiebres de stock no reconciliados. |
| **Origen** | RT-03.12 (obligatorio); caso Cap. 10 (offline 14 h); Cap. 16.1 **D8**. |
| **RF/RNF que la implementan** | RF-02.05 (stock offline + antigüedad), RF-03.16/03.17 (idempotencia de pedido), RNF-13.01/13.02 (operación degradada/lista). |

---

## 2. Trazabilidad resumida (regla → decisiones 16.1 → RF/RNF)

| Código | Regla | Decisión | RF/RNF principal | Tipo |
|---|---|---|---|---|
| RNG-01 | Reserva de stock | D8 | RF-03.03, RF-02.05 | Regla |
| RNG-02 | Stock disponible / en tránsito | D8 | RF-02.05, RF-02.06 | Regla |
| RNG-03 | Política de crédito | D8/D40 | RF-03.04–03.10 | Regla |
| RNG-04 | Excursión térmica | D4 | RF-09.05–09.07, RF-01.11 | Regla / calidad |
| RNG-05 | Local cerrado / reintento | D3 | RF-06.04, RF-04.07 | Regla |
| RNG-06 | Devoluciones + DTE | D12 | RF-06.03, RF-08.01/08.02 | Regla |
| RNG-07 | Envases retornables | D10 | RF-08.03/08.04/08.06 | Regla |
| RNG-08 | Cambio de precio | D9 | RF-03.11–03.13 | Regla |
| RNG-09 | Entrega cumplida / OTIF | D1 | RF-11.03, RF-11.04 | Regla |
| RNG-10 | FEFO / vida útil | — | RF-05.05, RF-02.09 | Regla |
| RNG-11 | Maestro productos / GS1 | D11 | RF-01.10, RF-12.03/12.06 | Regla |
| RNG-12 | Sincronización / conflictos | — (RT-03.12) | RF-02.05, RF-03.16/17 | Regla |
| RNG-13 | Secuencia térmica / zona | — | RF-05.04, RF-01.11/01.08 | Regla |
| RNG-14 | Capacidad vehículo / carga | — | RF-04.03/04.05, RF-05.07 | Regla |

---

## 3. Casos límite del Cap. 17.2 (criterio de clasificación aplicado)

Para mantener la **consistencia** exigida por el Cap. 17.2, el criterio aplicado a los casos limítrofes es:

| Caso límite (Cap. 17.2) | Clasificación | Justificación del criterio |
|---|---|---|
| "Confirmación de línea de picking ≤ 1 s" | **No funcional de desempeño** (RNF-05.01) | Umbral numérico y método de verificación; no cambia la semántica del negocio. |
| "Debe funcionar a −22 °C" | **No funcional de ambiente operativo** (RNF-05.02) | Restricción del dispositivo/operación, no una regla de negocio. |
| "Debe operar un turno completo sin señal" | **Arquitectura + NF de disponibilidad** (RT-03.12, RNF-13.01) | Define qué puede/no puede el dispositivo; su efecto de negocio se captura en RNG-12. |
| "El preventista debe ver el stock disponible" | **No funcional/RNG** (RNG-01/02) + consulta (RF-03.02) | La **consulta** es funcional; la **reserva** es regla de negocio (RNG-01). |
| "La prueba de entrega debe tener validez" | **Funcional** (RF-06.02/06.11/06.12) + **RT-16.14** | Captura de evidencia; la articulación tributaria es RT. |
| "El sistema debe bloquear el despacho ante excursión" | **Regla de negocio** (RNG-04) | Define quién decide la disposición del producto (calidad vs. operaciones), que es la esencia de una regla. |

> **Consistencia:** el criterio rector es que una **regla de negocio** decide sobre **entidades de negocio**
> (stock, crédito, producto, entrega) y **quién está autorizado** a decidir; un **RF** implementa una acción
> verificable; un **RNF** impone un umbral/método. Se aplica igual en todo el catálogo.

---

*Documento de trabajo de `Requerimientos/`. Se trasladará al informe (Cap. 17.1 — esquema de solución y alcance) sin duplicar como capítulo aparte.*