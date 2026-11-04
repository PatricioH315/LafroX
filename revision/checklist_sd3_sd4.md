# Checklist de revisión del prototipo según SD3 y SD4 (Informe 2)

Lista de lo que el prototipo debe demostrar según los requerimientos del **Subdocumento 3** y la arquitectura lógica del **Subdocumento 4** del Informe 2. Cuando el requerimiento cita el caso (Caso 02 Logística) o el SD2, se indica en «Respaldo».

Marque cada casilla solo después de verla funcionando en el prototipo. El prototipo no tiene servidor (Bases Técnicas Transversales, 25.6): lo que depende de integraciones, cálculo central o persistencia se da por cumplido si la pantalla **simula** el resultado de forma creíble (por ejemplo, la alerta que llega, el estado que cambia o el documento que se descarga).

## Constancia: lo que una simulación no puede demostrar

El prototipo es estático: no tiene servidor, base de datos, integraciones ni dispositivos reales. Las Bases Técnicas Transversales (25.6) declaran que nada de eso se exige. Por eso, en los requerimientos de la tabla, el prototipo **solo puede mostrar la pantalla y el resultado simulado**; la parte indicada en «No demostrable» queda pendiente para la construcción y la aceptación.

| # | Límite | Requerimientos afectados | Lo que sí muestra el prototipo | No demostrable |
|---|---|---|---|---|
| 1 | Integración real con el ERP | RF-01.09, RF-02.06, RF-03.11, RF-05.06, RF-06.14, RF-07.04, RF-07.08, RF-07.09, RF-08.02, RF-10.03 | El estado «enviado al ERP» y el mensaje si el ERP no responde | Que la transacción llegue, se concilie y quede sin diferencias |
| 2 | Intercambio EDI con cadenas de supermercados | RF-12.01, RF-12.02, RF-12.04, RF-12.09, RF-12.13 | La bandeja de pedidos EDI, sus validaciones y excepciones | Recepción y envío real de mensajes EDI, ASN y acuses |
| 3 | Dispositivos y sensores | RF-09.03, RF-09.04, RF-09.05, RF-14.01, RF-14.02, RF-14.03, RF-14.04, RF-11.02 | Mapas, curvas de temperatura, alertas y desvíos con datos de ejemplo | Lectura continua de GPS, telemetría y sensores de frío |
| 4 | Lectores e impresoras | RF-01.02, RF-01.07, RF-01.08, RF-05.02, RF-05.05, RF-05.07, RF-06.13 | El botón de escaneo, la validación del código y la etiqueta o comprobante en pantalla | Escaneo GS1 con lector físico e impresión térmica |
| 5 | Plazos y tiempos de respuesta | RF-01.05 (≤ 5 min), RF-07.05 (< 2 s), RF-08.04 (≤ 24 h), RF-12.01 (15 s), RF-12.04 (2 min), RF-12.09 (2 min), RF-12.13 (30 min), RF-17.11 (2 s), RF-06.08 (2 min) | Que el aviso o el resultado aparece | Medir el plazo con carga y datos reales |
| 6 | Resultados operacionales | RF-12.10 (80 % dentro de la ventana), RF-09.01 (retiro en < 2 h con datos reales) | El cálculo y el simulacro con datos de ejemplo | El porcentaje logrado en la operación |
| 7 | Envío real de mensajes | RF-04.06, RF-11.01, RF-12.25, RF-12.27, RF-17.10, RF-18.02, RF-18.03 | La notificación en la app, el aviso de «correo enviado» y la configuración de canales | Entrega de correos y SMS, reintentos y expiración de enlaces |
| 8 | Procesos automáticos de fondo | RF-02.03, RF-06.07, RF-11.01, RF-15.05 | El resultado del proceso (propuesta, reporte, cuenta creada) | La ejecución programada y sin intervención |
| 9 | Seguridad y garantías de integridad | RF-17.04, RF-17.08, RF-18.01, RF-07.09 | La consulta de auditoría, las versiones y la firma en pantalla | Inalterabilidad, cifrado, firma avanzada válida e idempotencia |
| 10 | Identidad real | RF-15.01, RF-15.02, RF-15.03, RF-15.04 | Inicio de sesión unificado, segundo factor y permisos por perfil, simulados | Federación, SSO entre módulos y MFA reales |
| 11 | Concurrencia entre personas usuarias | RF-03.03, RNG-01 | El quiebre parcial cuando el stock no alcanza | Que dos preventistas confirmen a la vez y gane el primero |
| 12 | Sincronización sin conexión real | RF-06.07 y Anexo 4-J (SD4) | La cola de pendientes y la sincronización al volver la señal | Persistencia cifrada en el dispositivo y conciliación con el servidor |
| 13 | Observabilidad y operación | RF-16.01, RF-16.03, RF-16.04 | Tableros y alertas de negocio con datos de ejemplo | Métricas, registros y trazas reales e informes de causa raíz |

Al marcar un requerimiento de esta tabla, verifique solo la columna «Lo que sí muestra el prototipo».

## Cómo usar esta lista

1. Ingrese con el perfil del actor indicado en cada requerimiento.
2. Recorra los módulos en orden (M1 a M12) y luego los transversales.
3. Use «Verificar» como prueba de aceptación: es el criterio que fijó SD3.
4. Registre lo que falte en la tabla de pendientes del final.

## Fuentes

| Fuente | Ubicación | Qué aporta |
|---|---|---|
| SD3, Anexo 3.A, RF del caso | `sd3/tablas_anexo/rf_caso.tex` | Requerimientos funcionales por módulo |
| SD3, Anexo 3.A, RF propios | `sd3/tablas_anexo/rf_propios.tex` | Requerimientos agregados por LafroX |
| SD3, Anexo 3.A, RF de las BTT | `sd3/tablas_anexo/rf_btt.tex` | Identidad, administración, auditoría, notificaciones |
| SD3, reglas de negocio | `sd3/tablas_anexo/reglas_negocio.tex` | RNG-01 a RNG-17 |
| SD3, Anexo 3.A.12a | `sd3/tablas_anexo/actores_sistema.tex` | Los 15 actores y su interfaz |
| SD4, Anexo 4-D | `sd4/04/anexos/logica/partes/05_…matriz_de_los_doce_modulos.tex` | Módulos M1 a M12 |
| SD4, capa de presentación | `sd4/04/partes/4.1_logica/04_capas_de_la_arquitectura.tex` | Canales, tres interacciones, preferencias, responsividad, teclado |
| SD4, Anexo 4-J | `sd4/04/anexos/logica/partes/11_…funciones_sin_conexion.tex` | Comportamiento sin conexión |

---

## 1. Actores del sistema (SD3, Anexo 3.A.12a; SD4, 4.1)

Cada actor debe tener un perfil con su interfaz y su menú. Ningún interesado sin cuenta (Gerenta General, Sindicato, Autoridad Sanitaria) debe aparecer como perfil.

- [ ] **Preventista** — App de preventa. Consulta comercial, captura de pedido y sincronización; sin reserva firme local. Módulos: M3; consulta a M2 y M7. Etapa: E1.
- [ ] **Conductor propio** — App de reparto. Entrega, POD, cobro, devolución y envases de su ruta. Módulos: M6, M7, M8. Etapa: E1.
- [ ] **Conductor externo** — App de reparto. Mismas operaciones de reparto, bajo asignación personal empresa–vehículo–turno. Módulos: M6, M7, M8. Etapa: E1.
- [ ] **Preparador** — App de bodega/HHT. Ejecuta misión, confirma lecturas y registra faltantes; la recepción requiere autorización funcional. Módulos: M5; operaciones autorizadas de M1/M2. Etapa: E1.
- [ ] **Cliente del canal tradicional** — Portal de clientes opcional. Pedido en autoatención y consulta de entregas, documentos y saldo. Módulos: Canal M11; negocio M3, M6, M7. Etapa: E2; atención por preventista desde E1.
- [ ] **Cliente del canal moderno** — Portal de clientes; integración EDI de la cadena. Consulta y pedido; el intercambio EDI utiliza identidad técnica separada. Módulos: M11; negocio M3, M6, M7. Etapa: E2.
- [ ] **Empresa transportista** — Portal de transportistas mediante representante. Consulta rutas y documentos; confirma conductor y vehículo de su empresa. Módulos: Canal M11; M4/M6 y vínculo de M12. Etapa: E2; asignación por despacho en E1.
- [ ] **Proveedor** — Portal de proveedores mediante representante. Consulta sus órdenes y recepciones sin aprobar el ingreso físico. Módulos: Canal M11; M1. Etapa: E2.
- [ ] **Jefa de Calidad** — Consola de Calidad. Parámetros térmicos, evaluación, bloqueo o liberación y retiro con evidencia. Módulos: M9; acciones autorizadas en M2/M5. Etapa: E1.
- [ ] **Gerente Comercial** — Consola comercial y tableros. Reglas y excepciones comerciales; consulta operacional; excepciones del canal moderno. Módulos: M3/M7; M10 y M11. Etapa: E1; canal moderno y costo de servir en E2.
- [ ] **Gerente de Finanzas** — Consola financiera y tableros. Consulta y supervisión de rendición y reglas financieras; costo de servir. Módulos: M7; M10. Etapa: E1; costo de servir en E2.
- [ ] **Planificador de Rutas** — Consola de planificación. Genera, corrige y aprueba rutas; registra restricciones y consulta recorrido. Módulos: M4 y M12. Etapa: E1.
- [ ] **Jefe de TI** — Consola de administración. Identidad, configuración, interfaces, observabilidad y operación técnica con privilegios controlados. Módulos: Base compartida; configuración autorizada por dominio. Etapa: E1/E2.
- [ ] **Gerente de Operaciones** — Consola operacional. Supervisa despacho, excepciones, rutas y continuidad de las olas. Módulos: M2, M4, M5, M6; consulta M9/M10/M12. Etapa: E1; funciones ampliadas según E2.
- [ ] **Jefa de Bodega** — Consola de bodega. Supervisa recepción, inventario, FEFO, preparación y recepción física de retornos. Módulos: M1, M2, M5 y M8. Etapa: E1.
- [ ] El peoneta no comparte la sesión del conductor y no hay cuentas genéricas por cargo (SD4, 4.1).
- [ ] Un actor relacionado con un módulo no ve todas sus funciones: los permisos se acotan por rol (SD4, 4.1).

## 2. Capa de presentación (SD4, Capa 1)

### Canales

- [ ] App de preventa con foto local de stock, precios, crédito y promociones, y captura local de pedidos con identificador único.
- [ ] App de reparto con entrega, prueba de entrega digital (firma, código QR y fotografía), cobranza en ruta y envases retornables.
- [ ] App de bodega para preparación y recepción.
- [ ] Portal de Clientes: pedido en autoservicio y consulta de estado de entrega, documentos y saldo.
- [ ] Portal de transportistas: revisar rutas y confirmar conductor y vehículo.
- [ ] Portal de proveedores: consultar órdenes y recepciones.
- [ ] Consolas de decisión para Calidad, gerencias, planificación y TI.
- [x] Vista ligera del Portal de Clientes para teléfonos de bajo costo: imágenes bajo demanda, listados paginados y sin animaciones.

### Uso y accesibilidad

- [ ] Toda funcionalidad principal de cada perfil se alcanza en **tres interacciones o menos** desde su inicio (RT-13.05).
- [ ] Sistema de diseño común: hasta cinco colores principales, dos familias tipográficas, iconografía coherente, retícula y componentes con estados (RT-13.09).
- [ ] Preferencias por persona: modo claro u oscuro, tamaño de texto y densidad de listados, conservadas en el dispositivo (RT-13.12).
- [ ] Interfaz en español.
- [ ] Responsivo desde la pantalla pequeña con quiebres en 640, 768, 1024, 1280 y 1536 px (RT-13.02).
- [ ] En teléfono: navegación recogida en un menú, formularios en una columna y listados como tarjetas con acceso al detalle.
- [ ] En tableta los controles se redistribuyen y en escritorio aparecen paneles y columnas adicionales, sin perder operaciones.
- [ ] Funciona en ambas orientaciones de tableta.
- [ ] Todo se recorre por teclado, con foco visible y orden acorde a la lectura (RT-13.11).
- [ ] Los diálogos reciben el foco al abrirse y lo devuelven al control de origen al cerrarse.
- [x] Atajos documentados y desactivables para buscar, guardar borrador y volver al inicio del perfil, sin interferir al escribir.
- [ ] Búsqueda global que tolera errores de escritura, filtra por tipo y muestra solo lo que el perfil puede ver (RF-17.11).
- [x] Listados ordenables, filtrables y paginados; la exportación CSV o JSON respeta filtros y orden e incluye todos los registros filtrados (RF-17.12).
- [ ] Registro del cliente del canal moderno con RUT de la empresa, correo corporativo y contraseña; envía confirmación por correo (RF-12.25).
- [ ] Si el RUT no está habilitado, el registro indica contactar al ejecutivo comercial (RF-12.25).
- [ ] En el canal tradicional la activación asistida por SMS es opcional y la compra asistida no exige cuenta.

## 3. Funciones sin conexión (SD4, Anexo 4-J)

El prototipo debe mostrar qué sigue funcionando sin señal y qué ocurre al reconectar.

- [ ] **Pedido preventa** (Captura 14 h) — Sin conexión: Precio y stock informativos, pedido sin confirmar. Al reconectar: M3 coordina la confirmación, M2 valida y retiene stock, y M7 aporta el control de crédito.
- [ ] **Pedido de autoatención** (Captura en el portal instalado) — Sin conexión: Catálogo y precios con fecha, pedido en cola con UUID. Al reconectar: M3 responde al cliente tras la retención de M2 y el control de crédito de M7.
- [ ] **Entrega y POD** (Captura 14 h) — Sin conexión: Evidencia cifrada y cola persistente. Al reconectar: M6 confirma o abre excepción.
- [ ] **Recepción y preparación** (Opera 24 h) — Sin conexión: Registro GS1 y bloqueo térmico local. Al reconectar: Eventos a nube y conciliación.
- [ ] **Cobro en efectivo** (Captura 14 h) — Sin conexión: Comprobante y custodia según política. Al reconectar: M7 rinde y concilia.
- [ ] **Autorización POS** (No disponible) — Sin conexión: Efectivo o crédito autorizado, sin cargo presunto. Al reconectar: Autorizar una sola vez.
- [ ] **Nueva guía electrónica** (Talca: integración local si ERP y comunicación tributaria están disponibles, otros sitios: guía preemitida o conexión hasta Talca.) — Sin conexión: erp-sync en VM-04 consume RabbitMQ de Talca sin depender de la nube. La emisión sigue requiriendo el ERP y su comunicación tributaria. Por salida consume la cola FIFO de solicitudes de los demás sitios, que reciben la respuesta por su cola. Fuera de Talca se requiere un camino del sitio y uno de Talca. Al reconectar: M5 libera solo la carga amparada por la guía vigente. Un ajuste sin camino hasta el ERP pasa a la ruta siguiente. Una guía anulada no se reutiliza: esa salida espera un documento válido.
- [ ] **Ruteo y mapas en línea** (No disponible) — Sin conexión: Usar secuencia y mapas precargados. Al reconectar: Recalcular cambios sin confirmar.
- [ ] **EDI de supermercados** (No disponible) — Sin conexión: Registrar incidente y aviso acordado con cadena. Al reconectar: Cola y bandeja de excepciones.
- [ ] **Tablero central** (No disponible) — Sin conexión: Alarmas y bitácora local sostienen despacho. Al reconectar: Reponer telemetría y estado.
- [ ] **Cadena de frío del camión** (Protección local completa) — Sin conexión: Gateway, alarmas cableadas y TC58e evalúan y retienen por SSCC sin móvil ni satélite. Al reconectar: Reenvío por secuencia; una crítica tardía retiene o abre evaluación de retiro.
- [ ] **Curva y órdenes sin móvil** (Disponibles por Iridium SBD) — Sin conexión: Curva cada 3 min, alarmas inmediatas y bajada de órdenes firmadas; sin cielo espera el aviso remoto. Al reconectar: Conciliar con serie fina; no liberar por recuperación.
- [ ] **Nueva liberación sanitaria** (Disponible localmente para Calidad preinscrita. Consola central requiere enlace.) — Sin conexión: Perfil Kotlin en terminal enrolado → puerta local A-01 → M9. Exige permiso vigente, expediente local suficiente y decisión durable. Si falta una condición, continúa el bloqueo. Al reconectar: M9 publica su decisión con UUID, versión, motivo y evidencia, Calidad resuelve conflictos sin liberación automática.

## 4. Módulos funcionales (SD4, Anexo 4-D; SD3, Anexo 3.A)

### M1 · Recepción

> Responsabilidad: Lote y recepción GS1. Interfaz principal: Evento a M2, ACL con ERP. Actor principal: Jefa de Bodega, Proveedor. Etapa: 1.

- [ ] El módulo M1 existe en el menú de los actores que lo usan.
- [ ] **RF-01.01** — El sistema debe registrar la recepción física de un proveedor validando las cantidades recibidas por SKU contra la OC y generando una alerta por cada discrepancia, sin bloquear el cierre.
  - Actor: Jefa de Bodega · Prioridad/etapa: Crítica / E1
  - Verificar: El comparativo pedido vs. recibido queda registrado al cerrar la recepción y toda discrepancia queda disponible en el módulo de calidad.
- [ ] **RF-01.02** — El sistema debe exigir el número de lote del proveedor en campo estructurado para todo SKU con trazabilidad obligatoria, capturándolo por escaneo GS1 (AI 10) o ingreso manual, y bloqueando el avance si el campo está vacío.
  - Actor: Jefa de Bodega · Prioridad/etapa: Crítica / E1
  - Verificar: El 100 % de los ítems con trazabilidad obligatoria registran lote; campo vacío muestra «Lote requerido para este producto» e impide continuar.
  - Respaldo: Caso, cap. 7.3
- [ ] **RF-01.03** — El sistema debe registrar la fecha de vencimiento en formato DD/MM/AAAA para todo SKU con control de vencimiento habilitado, vinculándola al lote y a la ubicación asignada como entrada para la lógica FEFO.
  - Actor: Jefa de Bodega · Prioridad/etapa: Crítica / E1
  - Verificar: El 100 % de los SKU con control de vencimiento habilitado tienen fecha registrada y asociada al lote al cerrar la recepción; campo vacío bloquea el avance.
  - Respaldo: Caso, cap. 4.8
- [ ] **RF-01.04** — El sistema debe permitir registrar una no conformidad durante la recepción seleccionando su tipo desde una lista predefinida e ingresando SKU, lote, cantidad afectada y al menos una fotografía capturada desde el dispositivo.
  - Actor: Jefa de Bodega · Prioridad/etapa: Alta / E1
  - Verificar: La no conformidad queda registrada con todos los campos requeridos y la fotografía es descargable desde el módulo de calidad.
  - Respaldo: Caso, cap. 4.9, Cap 8 (Entrevista de Calidad), RT-17.06
- [ ] **RF-01.05** — Al confirmar una no conformidad, el sistema debe cambiar automáticamente a estado ‘Cuarentena’ la cantidad afectada del SKU/lote correspondiente, bloqueándola para picking, y notificar al perfil de calidad mediante una alerta en la aplicación.
  - Actor: Jefa de Bodega · Prioridad/etapa: Alta / E1
  - Verificar: La cantidad del lote queda bloqueado para picking de forma inmediata y el perfil de calidad recibe la notificación en ≤ 5 min
  - Respaldo: Caso, cap. 4.9, RT-17.06
- [ ] **RF-01.06** — El sistema debe decodificar códigos de barras GS1 interpretando los AIs 01 (GTIN), 10 (lote), 17 (vencimiento) y 00 (SSCC), autocompletando los campos en pantalla; ante código inválido o no registrado, habilita el ingreso manual.
  - Actor: Jefa de Bodega · Prioridad/etapa: Alta / E1
  - Verificar: Código GS1 válido autocompleta los campos en pantalla; código no encontrado muestra «Producto no encontrado» y habilita ingreso manual.
  - Respaldo: Caso, RT-17.06, Cap. 16.2 (GS1)
- [ ] **RF-01.07** — Al finalizar el registro de un pallet, el sistema debe generar automáticamente un SSCC bajo estándar GS1-128 vinculado al GTIN, lote, fecha de vencimiento y fecha de recepción, e imprimir la etiqueta en la impresora térmica del andén.
  - Actor: Jefa de Bodega · Prioridad/etapa: Media / E1
  - Verificar: SSCC único con AI 00 impreso en GS1-128 y asociado a GTIN, lote, vencimiento y fecha de recepción. La fecha de recepción es dato interno y texto legible; AI 11 identifica producción y no se reutiliza como recepción.
  - Respaldo: RT-05.23
- [ ] **RF-01.08** — El sistema debe permitir asociar un SSCC a una dirección de almacenamiento (pasillo-columna-nivel) escaneando ambas etiquetas y validando la compatibilidad térmica antes de confirmar.
  - Actor: Jefa de Bodega · Prioridad/etapa: Media / E1
  - Verificar: La asociación SSCC–ubicación queda registrada; intento de ubicación incompatible es bloqueado con mensaje descriptivo.
  - Respaldo: Caso, cap. 12 (GS1), RT-05.23
- [ ] **RF-01.09** — Al cerrar una recepción, el sistema debe enviar automáticamente la transacción de ingreso de inventario al ERP mediante su interfaz de integración; si el ERP no está disponible, encola la transacción para reintento automático.
  - Actor: Jefa de Bodega · Prioridad/etapa: Crítica / E1
  - Verificar: La conciliación diaria no muestra diferencias entre el inventario del sistema y el del ERP; ante ERP no disponible, el sistema informa al usuario y reintenta sin intervención.
- [ ] **RF-01.10** — El sistema debe permitir crear y mantener fichas de producto con atributos obligatorios: descripción, formato, GTIN, SKU interno, tipo de almacenamiento, temperatura mínima y máxima (°C), peso neto (kg), dimensiones (cm), días de vida útil, indicadores de trazabilidad y control de vencimiento (sí/no), clasificación sanitaria y RUT del proveedor.
  - Actor: Gerente Comercial / Gerente de Operaciones · Prioridad/etapa: Crítica / E1
  - Verificar: El sistema no permite guardar una ficha con campos obligatorios vacíos y registra historial de cambios de GTIN o SKU con fecha y usuario.
  - Respaldo: Caso, Cap 14.1 (pasa de 8.400 a 9.500 SKu), Cap 8 (Hugo), Cap 16.1 (N11)
- [ ] **RF-01.11** — El sistema debe validar la compatibilidad térmica entre el tipo de almacenamiento del SKU y la zona de temperatura de la ubicación destino al realizar un putaway, bloqueando la operación si no son compatibles.
  - Actor: Jefa de Bodega · Prioridad/etapa: Crítica / E1
  - Verificar: Intento de ubicar un SKU congelado fuera de zona congelada es bloqueado con mensaje «Incompatibilidad térmica: requiere zona congelado».
  - Respaldo: Caso, cap. 4.9, Cap. 10 (restricción 2)

### M2 · Inventario y abastecimiento

> Responsabilidad: Movimientos por sitio, reserva central, FEFO y sugerencia de reposición de compras por SKU y proveedor con promociones comprometidas. Interfaz principal: Consulta de M3/M5, sugerencia aprobada al ERP por la ACL de INT-06. Actor principal: Jefa de Bodega, función de abastecimiento dentro de los perfiles autorizados. Etapa: 1.

- [ ] El módulo M2 existe en el menú de los actores que lo usan.
- [ ] **RF-02.01** — El sistema debe permitir registrar y configurar cada instalación de la red logística (centros de distribución y plataformas de cross-docking), definiendo su topología interna: zonas operativas (seco con rango 15–25 °C, refrigerado con rango 2–8 °C, congelado con rango -18 a -25 °C), pasillos, racks, niveles y posiciones individuales de almacenamiento. La configuración debe estar disponible en modo offline.
  - Actor: Jefe de TI / Jefa de Bodega · Prioridad/etapa: Alta / E1
  - Verificar: (a) Al configurar un nuevo CD, el sistema permite crear y mapear zonas, pasillos y posiciones con coordenada única. (b) Cada posición tiene zona térmica asociada con rango de temperatura. (c) No se permite crear posiciones sin zona asignada. (d) Cambios de topología quedan registrados con usuario, fecha y detalle del cambio.
- [ ] **RF-02.02** — El sistema debe consolidar el stock físico en unidades de cada SKU en todos los nodos de la red logística.
  - Actor: Jefa de Bodega / Gerente de Operaciones · Prioridad/etapa: Alta / E1
  - Verificar: El sistema expone un panel donde el usuario visualiza: (a) el stock físico totalizado por SKU, (b) el desglose por instalación, y (c) el desglose por zona operativa dentro de cada instalación.
- [ ] **RF-02.03** — El sistema debe calcular periódicamente una propuesta de reasignación de ubicaciones (slotting) basada en la clasificación de rotación (ABC) del último período configurable, considerando además peso, volumen y compatibilidad de zona. Los productos de clasificación A deben proponerse en ubicaciones cercanas a los andenes de salida. La propuesta debe ser aprobada por el jefe de bodega antes de generar instrucciones de movimiento.
  - Actor: Jefa de Bodega · Prioridad/etapa: Alta / E1
  - Verificar: (a) Al ejecutar el cálculo, el sistema presenta una propuesta con: producto, ubicación actual, ubicación propuesta, motivo (clasificación ABC, peso, volumen o zona). (b) El jefe de bodega puede aprobar, rechazar o modificar cada movimiento individualmente. (c) Los movimientos aprobados generan instrucciones de reubicación asignables a dispositivos de operarios, con indicación de ubicación origen y destino. (d) Cada reubicación ejecutada queda registrada con operario, fecha/hora, y ubicaciones origen/destino.
- [ ] **RF-02.04** — El sistema debe generar un plan de conteo cíclico mensual que cubra una cantidad de posiciones definidas, seleccionando posiciones por criterios configurables (rotación, valor, discrepancia histórica). Las tareas de conteo deben asignarse a los dispositivos de los operarios de bodega en modo de conteo ciego, sin mostrar la cantidad teórica. Tras el ingreso de la cantidad física, el sistema compara contra el teórico y registra la diferencia con su causa en campo estructurado.
  - Actor: Jefa de Bodega · Prioridad/etapa: Alta / E1
  - Verificar: (a) El operario recibe en su dispositivo la lista de posiciones a contar, sin cantidad teórica visible. (b) Al ingresar la cantidad física, si la diferencia valorizada es menor o igual al umbral configurado por el jefe de bodega para ese recinto, el sistema registra el ajuste automáticamente con la causa seleccionada (sobrante, falta, error de ubicación, daño, vencimiento). (c) Si la diferencia supera el umbral, el sistema marca la tarea como 'Pendiente de Autorización' y notifica al jefe de bodega.
  - Respaldo: Caso, cap. 14.1
- [ ] **RF-02.05** — El sistema debe calcular el stock disponible para venta por SKU y por centro de distribución, definido como la diferencia entre el stock físico registrado y el inventario comprometido por pedidos confirmados pendientes de preparación. En modo desconectado, la consulta debe reflejar el stock al momento de la última sincronización, indicando la antigüedad del dato.
  - Actor: Preventistas / Jefa de Bodega · Prioridad/etapa: Alta / E1
  - Verificar: (a) Al consultar stock, el preventista visualiza la cantidad disponible por SKU para su CD asignado. (b) La consulta refleja el stock actualizado tras cada transacción confirmada. (c) En modo offline, la consulta muestra «Dato de las HH:MM del DD/MM». (d) Al sincronizar un pedido tomado offline, si el stock disponible es insuficiente para alguna línea, el sistema marca esa línea como «sin stock disponible» y notifica al preventista. (e) Los conflictos entre pedidos simultáneos se resuelven por orden de confirmación en el servidor central (S-08, RNG-01); un pedido capturado sin señal toma su lugar al sincronizar.
- [ ] **RF-02.06** — El sistema debe registrar como «en tránsito» todo inventario despachado desde un nodo de origen hacia un nodo destino, desde la carga confirmada hasta la recepción confirmada en destino, y generar la transacción de transferencia correspondiente en el ERP.
  - Actor: Jefa de Bodega / Gerente de Operaciones · Prioridad/etapa: Media / E1
  - Verificar: (a) La consulta distingue stock físico en sitio, comprometido, disponible y en tránsito al sitio, con fecha/hora estimada. (b) El tránsito no suma a disponible hasta la recepción confirmada. (c) Al confirmarla, pasa automáticamente de tránsito a físico en destino. (d) Sin enlace, la recepción se registra localmente y sincroniza al reconectar. (e) Cada transferencia genera el movimiento interbodegas en el ERP; si no está disponible, se encola para reintento automático. (f) El tránsito se muestra como disponibilidad futura separada del stock físico del sitio.
- [ ] **RF-02.07** — El sistema debe permitir consultar el nivel de ocupación de cada centro de distribución, desglosado por zona operativa (seco, refrigerado, congelado), expresado como porcentaje de ubicaciones físicas utilizadas respecto de la capacidad total configurada.
  - Actor: Jefa de Bodega / Gerente de Operaciones · Prioridad/etapa: Alta / E1
  - Verificar: (a) Al consultar la ocupación de un CD, el sistema muestra el porcentaje de ocupación total y por zona (b) El reporte incluye un histórico diario de al menos 12 meses para visualizar tendencias. (c) El reporte es exportable a formato de hoja de cálculo.
- [ ] **RF-02.08** — El sistema debe dirigir la preparación de pedidos (picking) asignando tareas de recolección al dispositivo del preparador, indicando: ubicación, producto, lote, cantidad, y secuencia optimizada de recorrido. El preparador confirma cada línea en el dispositivo. Al no encontrar un producto o encontrar cantidad insuficiente, el preparador debe registrar el faltante con su causa en un campo estructurado (sin stock, producto dañado, producto vencido, error de ubicación, otro).
  - Actor: Jefa de Bodega · Prioridad/etapa: Alta / E1
  - Verificar: (a) El preparador recibe en su dispositivo la lista de líneas a recolectar, ordenadas por secuencia de recorrido óptima. (b) La confirmación de cada línea no supera 1 segundo de respuesta en el dispositivo. (c) Al registrar un faltante, el sistema exige la selección de una causa antes de continuar. (d) Al finalizar la preparación, el sistema actualiza el stock automáticamente y envía los faltantes al área comercial para gestión con el cliente.
  - Respaldo: Caso, Cap. 8, entrevista de Ximena Bravo; Cap. 15, RT-09.01; Cap. 18, criterio 15 (preparación y causa de faltantes)
- [ ] **RF-02.09** — El sistema debe gestionar el almacenamiento de productos con fecha de vencimiento aplicando la regla FEFO (First Expired, First Out), priorizando en la preparación de pedidos los lotes con fecha de vencimiento más próxima. El sistema debe alertar cuando un producto en stock alcance un umbral de vida útil remanente configurable.
  - Actor: Jefa de Bodega · Prioridad/etapa: Alta / E1
  - Verificar: (a) Al generar las tareas de picking, el sistema prioriza las ubicaciones con menor vida útil remanente para cada SKU. (b) Si un producto en stock tiene una vida útil remanente inferior al umbral configurado (ej. 30 días), el sistema genera una alerta al jefe de bodega con la acción recomendada (descuento, devolución al proveedor, destrucción). (c) El sistema genera un reporte semanal de productos próximos a vencer por zona y por SKU.
  - Respaldo: Caso, Cap. 9.10; Cap. 12, inocuidad alimentaria (vencimientos y merma)
  - ⚠ Revisión externa (04-11-2026) · **Sin verificar** · **Corregible fuera del prototipo**: el catálogo del SD3 no le da un título único. `tablas_anexo/rf_caso.tex` y el T-12 lo describen como FEFO con alerta de vida útil; `tablas/anx_rf_vacios.tex` y `tablas/t12_caso.tex` lo llaman «Retención sanitaria de lote en inventario» y lo dejan sin desarrollar. Se unifica en SD3 (rama main) y después se verifica `/inventario`.
- [ ] **RF-02.10** — El sistema debe proveer una interfaz de trazabilidad que permita buscar y detallar el ciclo de vida completo de un lote. Al consultar un lote específico, debe desglosar su estado actual, ubicación física en bodega, datos de recepción de proveedor y detalle de salida (clientes/mermas).
  - Actor: Jefa de Calidad / Jefa de Bodega · Prioridad/etapa: Alta / E1
  - Verificar: (a) El sistema provee un buscador de lotes por SKU, fecha o proveedor, devolviendo una lista con el estado (activo, agotado, en cuarentena). (b) Al seleccionar un lote, se despliega su ficha detallando: SKU, fecha vencimiento y cantidad física remanente por ubicación (pasillo/posición). (c) Se detalla el origen: fecha de recepción, proveedor, cantidad recibida inicial y documento. (d) Se detalla la salida de unidades: guías de despacho, cliente, fecha y cantidad entregada. (e) Se detallan excepciones: mermas, devoluciones o ajustes asociados. (f) Todo el detalle es exportable a hoja de cálculo para retiro sanitario inmediato.
  - Respaldo: Caso, cap. 4.9, Cap. 9.5
- [ ] **RF-02.11** — El sistema debe registrar en cada plataforma de cross-docking la lectura de las unidades logísticas al llegar el camión de línea y al cargarlas en el camión de reparto, con la hora de cada evento, y las excepciones (unidad faltante, sobrante o dañada) con su causa.
  - Actor: Jefa de Bodega / Gerente de Operaciones · Prioridad/etapa: Alta / E1
  - Verificar: Por cada plataforma y día se obtiene el tiempo real entre consolidación, llegada, desconsolidación y despacho, y el detalle de excepciones, para medir la brecha de 16 horas (Subdocumento 2, Anexo 2.2, SP-02).
  - Respaldo: Caso, sección 2.3 y cap. 3; SD2, Anexo 2.1, F-05
- [ ] **RF-10.01** — El sistema debe sugerir la reposición de compras por SKU y proveedor a partir de la historia de ventas, con excepciones revisables.
  - Actor: Jefe de abastecimiento · Prioridad/etapa: Media / E1
  - Verificar: La sugerencia reemplaza la planilla de reposición y queda disponible para revisión (D-05).
  - Respaldo: Caso, sección 4.1 y cap. 5
- [ ] **RF-10.02** — El sistema debe incorporar al cálculo de reposición las promociones comprometidas.
  - Actor: Jefe de abastecimiento · Prioridad/etapa: Media / E1
  - Verificar: La sugerencia incluye las promociones sin agregarlas a mano.
  - Respaldo: Caso, sección 4.1
- [ ] **RF-10.03** — El sistema debe traspasar la sugerencia aprobada al módulo de compras del ERP.
  - Actor: Jefe de abastecimiento · Prioridad/etapa: Media / E1
  - Verificar: El ERP recibe la sugerencia aprobada y conserva la emisión de la orden de compra.
  - Respaldo: Caso, sección 4.1; cap. 10

### M3 · Preventa

> Responsabilidad: Pedido y precio pactado, autoatención desde el Portal de Clientes. Interfaz principal: Reserva coordinada en M2, sincronización. Actor principal: Preventista, clientes autorizados. Etapa: 1, autoatención en 2.

- [ ] El módulo M3 existe en el menú de los actores que lo usan.
- [ ] **RF-03.01** — La app debe mostrar, con conectividad, el stock disponible en tiempo real para cada SKU al tomar el pedido.
  - Actor: Preventistas · Prioridad/etapa: Crítica / E1
  - Verificar: El preventista ve la disponibilidad vigente antes de ofrecer un producto.
  - Respaldo: Caso, Cap. 9.2; Cap. 18, criterio 5
- [ ] **RF-03.02** — La app debe mostrar, sin conectividad, el stock según la última sincronización válida, con su antigüedad visible.
  - Actor: Preventistas · Prioridad/etapa: Crítica / E1
  - Verificar: El preventista ve el dato cacheado y su antigüedad.
  - Respaldo: Caso, Cap. 9.2; Cap. 10, restricción 3 (consulta y operación sin señal)
- [ ] **RF-03.03** — El sistema debe reservar el stock comprometido en el momento de la confirmación del pedido en el servidor central de la solución operacional, por orden de llegada a ese servidor (S-08, RNG-01), sin depender de la disponibilidad del ERP.
  - Actor: Preventistas · Prioridad/etapa: Alta / E1
  - Verificar: Si dos preventistas comprometen el mismo producto, el segundo en confirmar queda con quiebre parcial registrado.
- [ ] **RF-03.04** — La app debe mostrar, con conectividad, el crédito disponible y la deuda vencida del cliente al tomar el pedido.
  - Actor: Preventistas · Prioridad/etapa: Crítica / E1
  - Verificar: El preventista ve crédito y deuda antes de finalizar el pedido.
  - Respaldo: Caso, Cap. 9.2; Cap. 18, criterio 5
- [ ] **RF-03.05** — La app debe mostrar, sin conectividad, el crédito y la deuda según la última sincronización válida, con su antigüedad visible.
  - Actor: Preventistas · Prioridad/etapa: Crítica / E1
  - Verificar: El preventista ve el dato cacheado y su antigüedad.
  - Respaldo: Caso, Cap. 9.2; Cap. 10, restricción 3 (información comercial y operación sin señal)
- [ ] **RF-03.06** — La app debe mostrar el historial de compra del cliente (productos y frecuencia).
  - Actor: Preventistas · Prioridad/etapa: Alta / E1
  - Verificar: El preventista consulta el historial e identifica productos habituales o quiebres.
  - Respaldo: Caso, Cap. 9.2
- [ ] **RF-03.07** — La app debe permitir aplicar una promoción vigente (3x2, descuento por volumen) a una línea de pedido, calculando el descuento automáticamente.
  - Actor: Preventistas · Prioridad/etapa: Alta / E1
  - Verificar: El preventista aplica la promoción y el sistema calcula el descuento.
  - Respaldo: Caso, Cap. 9.2 (promociones y qué ofrecer)
- [ ] **RF-03.08** — El sistema debe alertar al preventista cuando el pedido, sumado a la deuda vencida, supere el límite de crédito del cliente.
  - Actor: Preventistas · Prioridad/etapa: Crítica / E1
  - Verificar: El preventista es alertado antes de enviar el pedido.
  - Respaldo: Caso, Cap. 8, entrevistas de Rubén Salinas y Sandra Riffo; Cap. 9.2 (crédito y pedidos retenidos)
- [ ] **RF-03.09** — El sistema debe bloquear el envío del pedido cuando este, sumado a la deuda vencida, supere el límite de crédito en más de 110 %.
  - Actor: Preventistas · Prioridad/etapa: Crítica / E1
  - Verificar: El pedido no puede enviarse mientras el bloqueo esté activo.
  - Respaldo: Caso, Cap. 9.2 (control de crédito)
- [ ] **RF-03.10** — El sistema debe permitir que un supervisor autorice, de forma registrada, el envío de un pedido bloqueado.
  - Actor: Gerente de Finanzas · Prioridad/etapa: Alta / E1
  - Verificar: Queda registrado supervisor, fecha y hora, y el pedido puede enviarse.
- [ ] **RF-03.11** — El sistema debe registrar y conservar en cada pedido de preventa el precio acordado por el preventista al tomarlo, conforme a las condiciones comerciales autorizadas, sin modificarlo por cambios posteriores de la lista de precios.
  - Actor: Gerente Comercial · Prioridad/etapa: Media / E1
  - Verificar: El pedido conserva el precio acordado y lo transmite al ERP para la facturación.
  - ⚠ Revisión externa (04-11-2026) · **No cumplía** · ✓ **Corregido**: en Ficha de cliente › «Excepciones de precio» se crea una excepción por cliente o, en el canal moderno, por toda la cadena (descuento o precio fijo, con vigencia). Un descuento sobre 15 % queda «Por autorizar» (RNG-16). Los pedidos ya tomados conservan su precio. **Límite de la simulación**: la transmisión del precio al ERP para facturar (Constancia, fila 1).
- [ ] **RF-03.12** — El sistema debe generar una alerta al responsable comercial cuando el importe calculado para el despacho o la facturación difiera del precio registrado en el pedido, para corregir la discrepancia antes de facturar y conservar el precio acordado (RF-03.11).
  - Actor: Gerente Comercial · Prioridad/etapa: Media / E1
  - Verificar: La diferencia queda alertada al responsable comercial y se corrige antes de facturar, conservando el precio acordado.
  - ⚠ Revisión externa (04-11-2026) · **Era parcial** · ✓ **Corregido**: la alerta se calcula en cada pedido no facturado cuyo precio pactado difiere de la lista vigente (hoy, 20 pedidos por el alza de azúcar y leche). Se ven con el filtro «Precio: Con diferencia» de `/pedidos` y desde la tarea T-15 de la bandeja. El destinatario interno es correcto: SD3 pide alertar al responsable comercial, no al cliente.
- [ ] **RF-03.13** — El sistema debe informar al preventista la fecha y ventana horaria de entrega que puede comprometer, considerando stock, capacidad de despacho y restricciones del cliente.
  - Actor: Preventistas · Prioridad/etapa: Crítica / E1
  - Verificar: El preventista visualiza la ventana disponible antes de confirmar; la promesa queda registrada.
  - Respaldo: Caso, Cap. 9.1 (promesa de fecha y franja horaria)
- [ ] **RF-03.14** — El sistema debe generar sugerencias de productos usando historial de compra, frecuencia, productos habituales y promociones vigentes.
  - Actor: Preventistas · Prioridad/etapa: Alta / E1
  - Verificar: Al seleccionar un cliente, se muestran sugerencias según criterios configurados por comercial.
- [ ] **RF-03.15** — La app debe generar un identificador único en el dispositivo al crear un pedido sin conectividad.
  - Actor: Preventistas · Prioridad/etapa: Crítica / E1
  - Verificar: Cada pedido creado sin conectividad tiene un identificador único generado localmente.
  - Respaldo: Caso, Cap. 9.2; Cap. 18, criterio 6 (pedidos sin pérdida ni duplicación)
- [ ] **RF-03.16** — El sistema debe detectar y descartar automáticamente los reenvíos duplicados de un pedido con el mismo identificador único al sincronizar.
  - Actor: Preventistas · Prioridad/etapa: Crítica / E1
  - Verificar: Ningún pedido se pierde ni se duplica al sincronizar; todo reintento queda auditado.
  - Respaldo: Caso, Cap. 9.2; Cap. 18, criterio 6 (pedidos sin pérdida ni duplicación)

### M4 · Rutas

> Responsabilidad: Secuencia y restricciones. Interfaz principal: Ruta aprobada a M6. Actor principal: Planificador de Rutas. Etapa: 1.

- [ ] El módulo M4 existe en el menú de los actores que lo usan.
- [ ] **RF-04.01** — El sistema debe asignar pedidos a la flota, secuenciando la ruta en función de la capacidad volumétrica y zonas logísticas de entrega.
  - Actor: Planificador de Rutas · Prioridad/etapa: Alta / E1
  - Verificar: Se despliega una ruta propuesta con la carga asignada a los vehículos de la flota.
  - Respaldo: Caso, Cap 4.4, Criterio de aceptación #7
- [ ] **RF-04.02** — El sistema debe permitir modificar manualmente la secuencia de ruta y reasignar pedidos entre vehículos
  - Actor: Planificador de Rutas · Prioridad/etapa: Media / E1
  - Verificar: La tabla de ruteo y el ETA se recalculan inmediatamente tras realizar alguna reasignación
  - Respaldo: Caso, Cap. 18, criterio 7 (corrección de rutas)
- [ ] **RF-04.03** — El sistema debe bloquear la adición de líneas de pedido a una ruta si la sumatoria excede los límites de peso o volumen nominales del vehículo.
  - Actor: Planificador de Rutas · Prioridad/etapa: Alta / E1
  - Verificar: Se despliega un error bloqueante impidiendo el cierre del camión hasta reubicar el excedente.
- [ ] **RF-04.04** — El sistema debe permitir la configuración de ventanas horarias específicas por cliente y ajustar la secuencia para cumplirlas.
  - Actor: Planificador de Rutas · Prioridad/etapa: Alta / E1
  - Verificar: El planificador secuencia todas las entregas en ventanas donde el cliente está disponible
  - Respaldo: Caso, Cap. 9.1; Cap. 9.9 (ventanas de recepción y entrega)
- [ ] **RF-04.05** — El sistema debe restringir la asignación de pedidos refrigerados o congelados exclusivamente a vehículos con equipo de frío.
  - Actor: Planificador de Rutas · Prioridad/etapa: Alta / E1
  - Verificar: Se impide la adición de cadena de frío a un camión seco.
  - Respaldo: Caso, Cap. 9.6
- [ ] **RF-04.06** — El sistema debe crear un aviso al contacto del cliente con la hora estimada de llegada incluyendo una ventana de 30 minutos.
  - Actor: Planificador de Rutas · Prioridad/etapa: Media / E1
  - Verificar: El cliente recibe de forma exitosa el mensaje antes de la partida del camión.
  - Respaldo: Caso, Cap. 15, RT-16.21 (avisos de despacho y llegada)
- [ ] **RF-04.07** — El sistema debe permitir parametrizar franjas horarias de recepción en la ficha maestra de cada cliente (Ventana Horaria).
  - Actor: Planificador de Rutas · Prioridad/etapa: Alta / E1
  - Verificar: Ningún horario estimado de llegada es asignado en un horario fuera de la ventana horaria establecida por el cliente.
  - Respaldo: Caso, Cap. 9.1 (ventanas horarias)
- [ ] **RF-04.08** — El sistema debe calcular el costo de cada entrega tras haber sido realizada.
  - Actor: Gerente de Finanzas · Prioridad/etapa: Alta / E2
  - Verificar: El sistema calcula el costo de cada entrega basado en kilómetros, tiempo de descarga, tamaño del pedido y reentregas.
  - Respaldo: Caso, Cap. 9.8; Cap. 18, criterio 11

### M5 · Preparación

> Responsabilidad: Misión y carga confirmada. Interfaz principal: Guía nocturna vía erp-sync y ACL en VM-04. Actor principal: Preparador, Jefa de Bodega. Etapa: 1.

- [ ] El módulo M5 existe en el menú de los actores que lo usan.
- [ ] **RF-05.01** — El jefe de bodega debe poder iniciar la generación manualmente o configurar la generación automática al cierre de pedidos del turno. Las misiones deben permitir agrupación por pedido individual o por consolidación de pedidos de una misma ruta.
  - Actor: Jefa de Bodega · Prioridad/etapa: Alta / E1
  - Verificar: (a) Al generar misiones, la interfaz lista los ítems agrupados por pasillo lógico en secuencia de proximidad. (b) El sistema exige y permite confirmar cada línea digitalmente, exhibiendo: cantidad solicitada, SKU, lote asignado (FEFO) y coordenada exacta de ubicación.
- [ ] **RF-05.02** — El sistema debe exigir la validación de cada línea recolectada escaneando el código GS1. El escaneo debe validar el SKU y capturar el Lote exacto tomado. Permite ingreso manual solo como contingencia auditable.
  - Actor: Preparadores · Prioridad/etapa: Alta / E1
  - Verificar: Si el código de barras escaneado difiere del SKU o Lote instruido, el sistema bloquea la confirmación. Como mecanismo de contingencia, el sistema debe permitir el ingreso manual del código numérico, pero debe registrar obligatoriamente el evento en la bitácora como 'Ingreso Manual' para futura auditoría de calidad.
  - Respaldo: Caso, cap. 12
- [ ] **RF-05.03** — El sistema debe exigir la selección obligatoria de un motivo parametrizable de una lista estructurada, cada vez que se reporte una cantidad recolectada inferior a la solicitada.
  - Actor: Preparadores · Prioridad/etapa: Alta / E1
  - Verificar: Si la cantidad recolectada es inferior a la solicitada, el sistema despliega el campo obligatorio 'Causa de Faltante' con lista predefinida y deshabilita la acción 'Confirmar Línea' hasta su selección.
  - Respaldo: #15
- [ ] **RF-05.04** — El sistema debe secuenciar las líneas de la misión de preparación priorizando las zonas en el siguiente orden: seco → refrigerado → congelado, para minimizar el tiempo de exposición de los productos de frío fuera de su zona térmica.
  - Actor: Preparadores · Prioridad/etapa: Alta / E1
  - Verificar: Ante un pedido mixto, el sistema exige recolectar el 100% de los SKUs de ambiente seco antes de liberar las ubicaciones correspondientes a las cámaras de frío en la interfaz del operario.
- [ ] **RF-05.05** — El sistema debe asignar el inventario para la preparación de pedidos aplicando estrictamente la regla lógica FEFO (First Expired, First Out) según la fecha de vencimiento del lote.
  - Actor: Preparadores · Prioridad/etapa: Alta / E1
  - Verificar: (a) La misión dirige al operario a la coordenada del lote con fecha de vencimiento más próxima. (b) Al escanear un lote más nuevo cuando hay inventario del lote FEFO disponible, el sistema bloquea la confirmación con mensaje «Lote (código de lote) con vencimiento anterior disponible en [ubicación]». (c) Si el lote FEFO no está disponible (ej. dañado), el preparador puede seleccionar el siguiente lote registrando el motivo (lista estructurada: no encontrado, dañado, cantidad insuficiente). (d) La excepción FEFO queda registrada en bitácora de auditoría
- [ ] **RF-05.06** — El sistema debe enviar al ERP, al cerrar una misión de preparación, el detalle consolidado por cada línea: SKU, cantidad efectivamente recolectada y lote correspondiente, vinculado al ID del pedido original.
  - Actor: Jefa de Bodega · Prioridad/etapa: Alta / E1
  - Verificar: Al ejecutar 'Cerrar Misión', el sistema transmite al ERP el objeto completo de la recolección asociado al ID del pedido. El ERP procesa este conjunto de datos ajustando las cantidades finales y registrando los lotes exactos para la emisión de la Guía de Despacho, sin permitir digitación manual.
- [ ] **RF-05.07** — El sistema debe dirigir la carga de pedidos preparados en el camión siguiendo la secuencia inversa de la ruta asignada, garantizando que el primer cliente a visitar sea el último cargado (más accesible). El cargador debe confirmar cada bulto/pallet escaneando su SSCC.
  - Actor: Jefa de Bodega · Prioridad/etapa: Alta / E1
  - Verificar: (a) El dispositivo del cargador indica el siguiente bulto/pallet a subir, mostrando: SSCC, cliente destino y posición en la secuencia. (b) El cargador confirma cada bulto escaneando el SSCC; si escanea un bulto fuera de secuencia, el sistema alerta y solicita confirmación del motivo. (c) Al completar la carga, el sistema verifica que todos los bultos asignados al camión han sido escaneados. (d) Si falta algún bulto, el sistema bloquea la confirmación de carga completa y genera una alerta al jefe de bodega.

### M6 · Reparto

> Responsabilidad: Entrega y POD. Interfaz principal: Evento a M7/M8. Actor principal: Conductor propio, Conductor externo. Etapa: 1.

- [ ] El módulo M6 existe en el menú de los actores que lo usan.
- [ ] **RF-06.01** — El sistema debe permitir marcar la recepción conforme de bultos mediante validación por línea de pedido individual o marcado masivo por guía.
  - Actor: Tripulación propia y peoneta/ Conductores externos · Prioridad/etapa: Alta / E1
  - Verificar: Los elementos marcados como entregados quedan registrados de forma exitosa en la guía.
  - Respaldo: Caso, Cap. 9.4; Cap. 15, RT-16.14 (registro y evidencia de recepción)
- [ ] **RF-06.02** — El sistema debe permitir capturar la firma digital del receptor como evidencia de entrega, asociada a la guía de despacho electrónica.
  - Actor: Tripulación propia y peoneta / Conductores externos/ Canal Tradicional / Food Service / Canal Moderno) · Prioridad/etapa: Crítica / E1
  - Verificar: La firma queda correctamente registrada en la guía de despacho.
  - Respaldo: Caso, Cap. 9.4; Cap. 15, RT-16.14 y RT-17.06; Cap. 16.1, decisión 15 del caso, sobre mecanismo de prueba de entrega
- [ ] **RF-06.03** — El sistema debe permitir reportar un rechazo total o parcial seleccionando la cantidad y el motivo desde un catálogo predefinido.
  - Actor: Tripulación propia y peoneta / Conductores externos · Prioridad/etapa: Media / E1
  - Verificar: Los productos rechazados quedan registrados de forma correcta en la solicitud de rechazo.
  - Respaldo: Caso, Cap. 9.4; Cap. 16.1, decisión 12 (devoluciones y efectos tributarios)
- [ ] **RF-06.04** — El sistema debe permitir reportar un local cerrado, indicando la dirección del cliente.
  - Actor: Tripulación propia y peoneta / Conductores externos · Prioridad/etapa: Media / E1
  - Verificar: El envío se registra como fallido y se agenda para ser entregado en la ventana horaria siguiente mas cercana del cliente.
  - Respaldo: Caso, Cap. 16.1, decisión 3 (local cerrado)
- [ ] **RF-06.05** — El sistema debe permitir digitar el monto exacto recaudado en pagos realizados en efectivo
  - Actor: Tripulación propia y peoneta / Conductores externos · Prioridad/etapa: Crítica / E1
  - Verificar: El monto recibido en efectivo por el conductor queda registrado en el sistema.
  - Respaldo: Caso, Cap. 4.7; Cap. 9.7
- [ ] **RF-06.06** — El sistema debe registrar la hora real de llegada y de término de cada entrega.
  - Actor: Tripulación propia y peoneta / Conductores externos · Prioridad/etapa: Alta / E1
  - Verificar: Cada entrega tiene hora real de llegada y término, que alimenta el cálculo de OTIF (RF-11.03).
- [ ] **RF-06.07** — El sistema debe sincronizarse automaticamente, al detectar la reconexión de señal o el regreso al centro de distribución, sincronizar automaticamente todos los registros generados durante el turno, recuperando la totalidad de los despachos registrados, consolidandolos en un reporte de cierre.
  - Actor: Tripulación propia y peoneta / Conductores externos / Jefa de Bodega / Gerente de Operaciones · Prioridad/etapa: Crítica / E1
  - Verificar: Al llegar al CD o recuperar señal, la app sube la data y el sistema genera automáticamente el reporte de rendición.
- [ ] **RF-06.08** — El sistema debe permitir al conductor de una empresa externa iniciar su jornada usando las credenciales temporales por OTP (código de un solo uso) emitido por su jefe de flota; la sesión común posterior la provee RF-15.02. sin necesidad de correo corporativo.
  - Actor: Tripulación propia y peoneta / Conductores externos / Empresas Transp. · Prioridad/etapa: Alta / E1
  - Verificar: Un conductor nuevo de una empresa externa se autentica en 2 minutos con un código que le da su jefe de flota, y puede iniciar su ruta.
  - Respaldo: Caso, Restricción #6, RT-12.11, Cap. 16.1 (Decisión #5)
  - ⚠ Revisión externa (04-11-2026) · **Era parcial** · ✓ **Corregido**: en `/ingresar` › Credencial de turno, solo entra el código emitido (RUT 15.482.337-9, código 48213705). Otro código o RUT muestra «Código o RUT incorrecto» y 00000000 muestra «Código vencido». **Límite de la simulación**: la emisión real del OTP por el jefe de flota, su expiración y el plazo de 2 minutos (Constancia, filas 5 y 10).
- [ ] **RF-06.09** — Al registrar una entrega, el sistema debe permitir al conductor capturar la cantidad de canastillos y pallets devueltos por el cliente, identificando el tipo y estado.
  - Actor: Tripulación propia y peoneta / Conductores externos · Prioridad/etapa: Alta / E1
  - Verificar: El conductor registra que el cliente devolvió 5 canastillos; el sistema descuenta del saldo del cliente y actualiza el inventario de envases.
  - Respaldo: Caso, cap. 9.7, Criterio Aceptación #12
- [ ] **RF-06.10** — El sistema debe actualizar el saldo del cliente y del parque retornable en línea o en modo diferido según conectividad, asociando el registro a la entrega o a la guía correspondiente
  - Actor: Tripulación propia y peoneta / Conductores externos · Prioridad/etapa: Alta / E1
  - Verificar: El saldo del cliente indica que se devolvieron 5 canastillos y el sistema lo actualiza en el inventario de envases
  - Respaldo: Caso, cap. 9.7, Criterio Aceptación #12
- [ ] **RF-06.11** — El sistema debe ofrecer al cliente la opción de confirmar la recepción mediante un código QR único generado por la app del conductor, cuando el cliente disponga de teléfono inteligente.
  - Actor: Tripulación propia y peoneta / Conductores externos · Prioridad/etapa: Media / E1
  - Verificar: Se resuelve alternativamente la Decisión #15; los clientes con smartphone pueden validar su recepción de forma autónoma.
- [ ] **RF-06.12** — El sistema debe permitir confirmar la recepción del cliente aun si este no dispone de teléfono o conectividad, mediante captura de firma en pantalla o el registro fotografico de la recepcion, dejando evidencia vinculada a la guia de despacho electrónica en su acuse de recibo.
  - Actor: Canal Tradicional / Food Service / Canal Moderno / Tripulación propia y peoneta / Conductores externos · Prioridad/etapa: Media / E1
  - Verificar: Los clientes sin conectividad y sin smartphone pueden validar su recepción de forma autónoma.
- [ ] **RF-06.13** — La app de reparto debe permitir imprimir en terreno un comprobante térmico de entrega para el cliente usando una impresora portátil Bluetooth en aquellos casos donde el cliente requiera respaldo físico.
  - Actor: Tripulación propia y peoneta / Canal Tradicional · Prioridad/etapa: Media / E1
  - Verificar: El cliente del canal tradicional recibe un comprobante físico pequeño, igual que hoy con la guía, pero generado digitalmente.
  - Respaldo: Caso, RT-17.06 (impresora térmica portátil)
- [ ] **RF-06.14** — El sistema debe enviar al ERP, para cada guía de despacho electrónica, la evidencia de recepción capturada en la entrega (firma, fotografía, nombre del receptor o confirmación QR) y recibir de vuelta el estado del acuse de recibo registrado por el ERP, conciliándolo con la guía.
  - Actor: Jefe de TI / Gerente de Finanzas / Tripulación propia y peoneta / Conductores externos · Prioridad/etapa: Alta / E1
  - Verificar: Cada guía queda con su estado de acuse (recibido conforme, con observaciones o sin acuse) visible el mismo día; las guías sin acuse generan una alerta para gestión. La solución no emite documentos tributarios.
  - Respaldo: SD2, Anexo 2.1, F-09

### M7 · Cobranza y rendición

> Responsabilidad: Cobro y descuadre. Interfaz principal: ACL al ERP, evento a M10. Actor principal: Conductores, Gerente de Finanzas. Etapa: 1.

- [ ] El módulo M7 existe en el menú de los actores que lo usan.
- [ ] **RF-07.01** — El sistema debe calcular para cada camión y turno el monto esperado de rendición a partir de las entregas al contado confirmadas y de los cobros registrados en ruta.
  - Actor: Gerente de Finanzas / Tripulación propia y peoneta / Conductores externos · Prioridad/etapa: Alta / E1
  - Verificar: La planilla de rendición (RF-07.02) contrasta lo declarado con el monto esperado y muestra la diferencia a justificar (RF-07.03).
  - Respaldo: Caso, cap. 18, criterio 10
- [ ] **RF-07.02** — El sistema debe generar la planilla digital de rendición individual al retorno del camión, contrastando los valores declarados por el conductor en la aplicación móvil contra las entregas al contado realizadas y facturas cobradas.
  - Actor: Gerente de Finanzas / Tripulación propia y peoneta / Conductores externos · Prioridad/etapa: Alta / E1
  - Verificar: Despliegue automático de la cuadratura en caja mostrando monto esperado vs recaudado y la diferencia resultante a justificar.
- [ ] **RF-07.03** — El sistema debe obligar al registro estructurado y categorizado de causales para cualquier diferencia detectada en la rendición de caja (descuentos comerciales autorizados, diferencias de cambio, siniestro en ruta), bloqueando el cierre de la liquidación si existe saldo sin justificar.
  - Actor: Gerente de Finanzas / Tripulación propia y peoneta / Conductores externos · Prioridad/etapa: Alta / E1
  - Verificar: Cero pesos de descuadre sin motivo formal tipificado, firma digital y asignación de responsabilidad en bitácora.
- [ ] **RF-07.04** — El sistema debe proveer una consola de gestión para la cartera de crédito a 30 días sincronizada con el ERP, asignando carteras de clientes a ejecutivos de cobranza y registrando bitácoras de gestión, compromisos de pago y fechas de recontacto.
  - Actor: Gerente de Finanzas / Canal Tradicional / Canal Moderno · Prioridad/etapa: Alta / E1
  - Verificar: Listado diario de morosidad al día con registro auditable de promesas de pago y tareas automáticas de seguimiento.
- [ ] **RF-07.05** — El sistema debe notificar en la aplicación móvil de preventa el estado de bloqueo o mora de un cliente (>30 días o cupo excedido), bloqueando preventivamente el ingreso de pedidos a crédito y permitiendo únicamente venta al contado o cobro de deuda.
  - Actor: Preventistas / Gerente de Finanzas / Gerente Comercial · Prioridad/etapa: Alta / E1
  - Verificar: Alerta en terminal de preventa en menos de 2 s al seleccionar al cliente, impidiendo el ingreso de órdenes a crédito no autorizadas.
- [ ] **RF-07.06** — El sistema debe integrarse vía Bluetooth con terminales de pago portátil (POS) en la aplicación móvil de reparto para cobro con tarjeta en ruta, capturando el código de autorización bancario y conciliando el voucher automáticamente en la liquidación diaria.
  - Actor: Tripulación propia y peoneta / Conductores externos / Canal Tradicional / Canal Moderno / Gerente de Finanzas · Prioridad/etapa: Alta / E1
  - Verificar: Captura automática del código de autorización POS y conciliación contra la entrega en la rendición diaria de caja sin digitación manual.
  - Respaldo: Caso, RT-17.06, Cap. 9.7
- [ ] **RF-07.07** — El sistema debe disponer en el portal web de autoatención el estado de cuenta y la cartola de antigüedad de deuda (tramos corriente, 30, 60, 90+ días) descargable en formatos PDF y Excel para clientes autenticados.
  - Actor: Canal Tradicional / Canal Moderno / Gerente de Finanzas · Prioridad/etapa: Alta / E2
  - Verificar: Acceso seguro del cliente autenticado a su saldo vivo y detalle de facturas pendientes con opción de descarga de cartola.
- [ ] **RF-07.08** — El sistema debe proveer una bandeja de validación para pagos reportados en el portal web de clientes, permitiendo al cajero verificar el comprobante bancario y autorizar su traspaso estructurado al ERP.
  - Actor: Gerente de Finanzas / Canal Moderno · Prioridad/etapa: Alta / E2
  - Verificar: Pago web queda en estado «En Revisión» hasta que el cajero lo aprueba, momento en que se envía la rebaja contable al ERP.
  - ⚠ Revisión externa (04-11-2026) · **Era parcial** · ✓ **Corregido**: al aprobar un pago web se agrega un mensaje nuevo («Rebaja por pago web…», en cola) en la pestaña «Envío al ERP». **Límite de la simulación**: que la rebaja llegue al ERP real y se concilie (Constancia, fila 1).
- [ ] **RF-07.09** — El sistema debe transferir de forma estructurada, asíncrona e idempotente los comprobantes de recaudación y cierres comerciales aprobados hacia el ERP para actualizar automáticamente las cuentas por cobrar.
  - Actor: Jefe de TI / Gerente de Finanzas · Prioridad/etapa: Alta / E1
  - Verificar: Abonos y cancelaciones contables reflejados en el ERP el mismo día sin intervención manual de digitación (Restricción R4).
- [ ] **RF-07.10** — El sistema debe permitir el registro de anticipos o pagos parciales en entregas al contado desde la aplicación móvil de reparto, emitiendo un comprobante digital de abono y traspasando el saldo insoluto a la cuenta corriente del cliente en el ERP.
  - Actor: Tripulación propia y peoneta / Conductores externos / Canal Tradicional/ Gerente de Finanzas · Prioridad/etapa: Alta / E1
  - Verificar: Registro de abono parcial en app móvil, comprobante digital emitido al cliente y saldo pendiente registrado en cuenta corriente.
- [ ] **RF-07.11** — El sistema debe permitir al preventista registrar la cobranza en efectivo de facturas vencidas en el local del cliente desde su terminal móvil, emitiendo un recibo provisional digital y forzando su rendición diaria en caja.
  - Actor: Preventistas / Gerente de Finanzas / Canal Tradicional · Prioridad/etapa: Alta / E1
  - Verificar: Emisión de recibo digital de cobro en preventa y consolidación automática en la bolsa de dinero a rendir por el vendedor al volver a base.
  - Respaldo: Caso, cap. 8

### M8 · Devoluciones y envases

> Responsabilidad: Retorno y saldo de envases. Interfaz principal: Evento a M2/M7. Actor principal: Conductores, Jefa de Bodega. Etapa: 1.

- [ ] El módulo M8 existe en el menú de los actores que lo usan.
- [ ] **RF-08.01** — El sistema debe permitir al conductor registrar la devolución de productos en el momento de la entrega, capturando SKU, cantidad y motivo (daño / vencimiento / producto no pedido / error), operando en modo offline.
  - Actor: Tripulación propia y peoneta / Conductores externos · Prioridad/etapa: Crítica / E1
  - Verificar: La devolución queda registrada en el dispositivo al momento de la entrega, sin papeleo, y se sincroniza con el sistema central al reconectarse.
  - Respaldo: Caso, cap. 4.8, RT-17.01
- [ ] **RF-08.02** — Al recepcionar una devolución en el andén del CD, el sistema debe permitir seleccionar el destino final del producto (reingreso a stock / venta con descuento / devolución al proveedor / destrucción) y enviar la transacción al ERP mediante su interfaz de integración.
  - Actor: Jefa de Bodega · Prioridad/etapa: Crítica / E1
  - Verificar: El destino queda registrado y la transacción llega al ERP; toda decisión queda trazada con usuario, fecha y destino asignado.
- [ ] **RF-08.03** — El sistema debe mantener una cuenta corriente de envases retornables por cliente, actualizando el saldo en cada entrega y devolución registrada por el conductor.
  - Actor: Tripulación propia y peoneta / Conductores externos · Prioridad/etapa: Alta / E1
  - Verificar: El saldo de envases por cliente queda actualizado tras cada movimiento y es consultable desde el dispositivo del conductor antes de cada entrega.
  - Respaldo: Caso, cap. 16.1 (Decisión #10), Cap 9.7
- [ ] **RF-08.04** — El sistema debe generar una alerta al preventista cuando el saldo de envases retornables de un cliente supere el umbral configurado por el administrador.
  - Actor: Preventistas · Prioridad/etapa: Alta / E1
  - Verificar: El preventista recibe la notificación en ≤ 24 horas de superado el umbral.
- [ ] **RF-08.05** — El sistema debe permitir registrar mermas por vencimiento detectadas en conteo cíclico, preparación de pedidos o góndola del cliente, asociando cada registro al SKU y al lote correspondiente.
  - Actor: Preparadores / Preventistas · Prioridad/etapa: Alta / E1
  - Verificar: La merma identifica SKU, lote, cantidad y origen (conteo, preparación o góndola). El ajuste afecta las existencias bajo custodia correspondientes. Un aviso en góndola de producto ya entregado no vuelve a descontar existencias físicas de la bodega; si retorna, M8 registra el evento.
- [ ] **RF-08.06** — El sistema debe reportar la pérdida de envases retornables desglosada por cliente, tipo de envase y zona, con actualización diaria.
  - Actor: Gerente de Operaciones / Gerente de Finanzas · Prioridad/etapa: Alta / E1
  - Verificar: El reporte identifica los clientes y zonas con mayor pérdida de envases, permitiendo priorizar acciones de recuperación.
- [ ] **RF-08.07** — El sistema debe incluir el costo de devoluciones y mermas por cliente como componente del cálculo del costo de servir (Épica 11).
  - Actor: Gerente de Finanzas · Prioridad/etapa: Alta / E2
  - Verificar: El costo de servir de un cliente con alta tasa de devolución refleja ese costo adicional.
  - ⚠ Revisión externa (04-11-2026) · **Era parcial** · ✓ **Corregido**: el costo de servir suma las devoluciones del cliente según su destino (merma al 100 % del monto; reingreso a stock, 15 %). Prueba: una merma de 900 u de azúcar subió el costo de servir de Almacén Doña Rosa de 15,5 % a 63,9 %, y la ficha muestra la composición recalculada. **Límite de la simulación**: que el cálculo use datos reales y se conserve al recargar.

### M9 · Calidad y trazabilidad

> Responsabilidad: Lote, frío, bloqueo y disposición sanitaria autorizada. Interfaz principal: Estado sanitario a M2/M5, alerta y expediente. Actor principal: Jefa de Calidad. Etapa: 1.

- [ ] El módulo M9 existe en el menú de los actores que lo usan.
- [ ] **RF-09.01** — El sistema debe permitir la trazabilidad 'hacia adelante' (forward tracing): dado un lote específico, debe listar todos los clientes que recibieron productos de ese lote, con fecha de entrega, guía y cantidad.
  - Actor: Jefa de Calidad · Prioridad/etapa: Crítica / E1
  - Verificar: En un simulacro de retiro sanitario, se obtiene en menos de 2 horas la lista de clientes afectados, con trazabilidad desde el proveedor hasta los clientes y archivo exportable (RNF-09.01).
  - Respaldo: Caso, cap. 9.6, Criterio Aceptación #1
- [ ] **RF-09.02** — El sistema debe permitir la trazabilidad 'hacia atrás' (backward tracing): dado un producto en el local del cliente (SKU + lote), debe identificar el origen (proveedor, fecha de recepción y orden de compra)
  - Actor: Jefa de Calidad · Prioridad/etapa: Crítica / E1
  - Verificar: El equipo de calidad puede rastrear el origen de cualquier unidad devuelta, realizando la trazabilidad desde los clientes afectados hasta los productores
  - Respaldo: Caso, cap. 9.6
- [ ] **RF-09.03** — El sistema debe registrar de forma automática y continua la temperatura de las cámaras de refrigerado y congelado, con lecturas cada 5 minutos como mínimo
  - Actor: Jefa de Calidad · Prioridad/etapa: Crítica / E1
  - Verificar: El sistema registrara las temperaturas. Los registros son auditable y se puede exportar para la autoridad sanitaria.
  - Respaldo: Caso, cap. 7.3, Criterio Aceptación #3
- [ ] **RF-09.04** — El sistema debe registrar de forma automática y continua la temperatura en los camiones con equipo de frío (18 propios y 10 de transportistas, todos con sensor instalado antes de la ola de reparto; S-28), durante todo el trayecto desde la carga hasta la entrega.
  - Actor: Jefa de Calidad · Prioridad/etapa: Crítica / E1
  - Verificar: El sistema registrara las temperaturas de los camiones. El cliente o Puelche pueden consultar el registro histórico de temperatura de su envío.
  - Respaldo: Caso, cap. 4.9, Criterio Aceptación #3
- [ ] **RF-09.05** — El sistema debe generar una alerta en tiempo real (notificación en cabina y en plataforma de monitoreo) cuando se detecte una excursión de temperatura que supere la desviación continua de 2 °C por 15 minutos para el tipo de producto.
  - Actor: Jefa de Calidad · Prioridad/etapa: Crítica / E1
  - Verificar: El sistema al registrar una temperatura fuera del rango aceptable, generara una alerta tanto al conductor como al equipo de calidad
  - Respaldo: Caso, Cap. 16.1 (Decisión #4)
- [ ] **RF-09.06** — Ante una excursión térmica crítica y sostenida, el sistema debe bloquear preventivamente el despacho del lote afectado y notificar a Calidad; ante una excursión menor y transitoria, debe emitir una alerta preventiva en cabina. El conductor recibe la alerta y registra sus observaciones; Calidad decide liberar, bloquear o rechazar (Subdocumento 2, sección «Arbitraje de tensiones operacionales y comerciales», tensión 2; Anexo 2.2, S-04).
  - Actor: Tripulación propia y peoneta / Conductores externos · Prioridad/etapa: Media / E1
  - Verificar: El lote queda retenido automáticamente ante excursión crítica; el conductor ve la alerta y registra observaciones; solo Calidad libera, bloquea o rechaza, y su decisión queda registrada.
  - Respaldo: Caso, Cap. 16.1 (Decisión #4)
- [ ] **RF-09.07** — El sistema debe permitir al conductor registrar el rechazo de un producto entregado por 'sospecha de ruptura de cadena de frío', asociando el evento al sensor de temperatura del camión en ese tramo.
  - Actor: Tripulación propia y peoneta / Conductores externos · Prioridad/etapa: Crítica / E1
  - Verificar: Si se rechaza el pedido, el conductor registra el rechazo ingresando evidencia
  - Respaldo: Caso, cap. 8
- [ ] **RF-09.08** — El sistema debe registrar, en el momento de la preparación (picking), el lote específico que se le asigna a cada línea de pedido, para los productos con control sanitario.
  - Actor: Preparadores · Prioridad/etapa: Crítica / E1
  - Verificar: El picking digital registra qué lote concreto sale en cada canastillo/pallet hacia el cliente.
  - Respaldo: Caso, cap. 4.9
- [ ] **RF-09.09** — El sistema debe generar la evidencia de cumplimiento de cadena de frío exigible ante la autoridad sanitaria y ante el cliente, para un envío determinado.
  - Actor: Jefa de Calidad · Prioridad/etapa: Crítica / E1
  - Verificar: La evidencia de cadena de frío de un envío se obtiene sin reconstrucción manual.
  - Respaldo: Caso, Cap. 18 criterio N°3
- [ ] **RF-09.10** — El sistema debe permitir parametrizar por tipo de producto la regla de excursión térmica (desviación y duración).
  - Actor: Jefa de Calidad · Prioridad/etapa: Media / E1
  - Verificar: La alerta y la retención de RF-09.05 y RF-09.06 aplican el parámetro vigente, y cada cambio queda registrado.
  - Respaldo: Caso, sección 16.1, decisión 4; SD2, Anexo 2.2, S-04
- [ ] **RF-09.11** — El sistema debe registrar la salida de cámara y la carga de cada SSCC de frío, calcular su tiempo fuera de frío en el andén y bloquearlo si supera el máximo de su familia.
  - Actor: Tripulación / Jefa de Calidad · Prioridad/etapa: Crítica / E1
  - Verificar: Exposición de andén trazable y bloqueo antes de salir si excede el máximo.
  - Respaldo: Propio LafroX
- [ ] **RF-09.12** — El sistema debe registrar la bajada de cada SSCC de frío y habilitar su entrega solo con estado vigente: latido válido de menos de 30 s, manifiesto vigente, sin retención ni contradicción.
  - Actor: Tripulación · Prioridad/etapa: Crítica / E1
  - Verificar: Fin de la ventana a bordo; POD posterior permitido dentro del local aun fuera del Wi-Fi de cabina.
  - Respaldo: Propio LafroX
- [ ] **RF-09.13** — El terminal debe retener el SSCC afectado ante crítica, contradicción o pérdida del enlace local con el camión, sin depender de red móvil ni satélite.
  - Actor: Tripulación / Jefa de Calidad · Prioridad/etapa: Crítica / E1
  - Verificar: Bloqueo de una nueva bajada con estado no confiable; lo retenido vuelve al CD si no existe decisión en plazo.
  - Respaldo: Propio LafroX
- [ ] **RF-09.14** — El sistema debe registrar la disposición del producto retenido: liberar, vender con descuento si es apto, devolver al proveedor, uso no alimentario autorizado o destrucción autorizada.
  - Actor: Jefa de Calidad · Prioridad/etapa: Crítica / E1
  - Verificar: Decisión trazable; área de no aptos separada y marcada con X roja u otro signo inequívoco (RSA, art. 105).
  - Respaldo: Propio LafroX

### M10 · Analítica

> Responsabilidad: OTIF operacional y costo de servir. Interfaz principal: Consume eventos sin escribir. Actor principal: Gerentes Comercial, de Finanzas y de Operaciones, Jefa de Calidad. Etapa: 1 OTIF, 2 costo.

- [ ] El módulo M10 existe en el menú de los actores que lo usan.
- [ ] **RF-11.01** — El sistema debe programar y distribuir vía correo electrónico reportes ejecutivos consolidados (en formatos PDF y XLSX) con periodicidad semanal y mensual, desglosando la evolución de OTIF, Fill Rate, Merma por vencimiento y Costo de Servir por zona y canal de comercialización.
  - Actor: Gerente de Finanzas / Gerente Comercial / Jefa de Calidad · Prioridad/etapa: Media / E2
  - Verificar: Reportes emitidos automáticamente a las casillas de los gerentes el día 2 de cada mes y cada lunes a las 06:00 AM sin intervención manual.
- [ ] **RF-11.02** — El sistema debe calcular el Costo de Servir real por entrega y por cliente, imputando los costos directos de transporte (combustible devengado vía GPS, peajes, tiempo de conducción y tiempo de descarga) y los costos indirectos prorrateados (bodega y administración).
  - Actor: Gerente de Finanzas / Gerente Comercial · Prioridad/etapa: Media / E2
  - Verificar: Ficha de rentabilidad por cliente actualizada tras cada liquidación, desglosando costos logísticos directos e indirectos y margen neto resultante.
- [ ] **RF-11.03** — El sistema debe calcular diariamente el indicador OTIF por cliente, ruta, zona y total consolidado, definiendo «On-Time» como el cumplimiento de fecha y ventana horaria pactada e «In-Full» como la entrega del 100% de ítems y unidades pedidas, obligando al registro de causal tipificada ante desvíos.
  - Actor: Gerente Comercial / Jefa de Calidad / Tripulación propia y peoneta / Conductores externos · Prioridad/etapa: Alta / E1
  - Verificar: Todas las gerencias visualizan el mismo valor de OTIF diario; ante entregas parciales o tardías se audita el motivo en el sistema.
- [ ] **RF-11.04** — El sistema debe calcular automáticamente el Fill Rate (unidades entregadas vs. pedidas) y el índice de Perfect Order contrastando la orden de venta original contra los datos de entrega física confirmados en el dispositivo móvil de reparto, sin requerir interacción tecnológica del cliente tradicional.
  - Actor: Gerente Comercial / Tripulación propia y peoneta / Conductores externos · Prioridad/etapa: Alta / E1
  - Verificar: Indicador mensual de Perfect Order desglosado por causa raíz (daño, faltante, atraso, documento) contrastado contra la orden de venta original.
- [ ] **RF-11.05** — El sistema debe calcular diariamente la utilización de capacidad volumétrica (m3) y de peso (kg) por viaje despachado, alertando aquellos camiones que salgan con una ocupación inferior al umbral configurable (ej. < 65%).
  - Actor: Planificador de Rutas / Gerente Comercial · Prioridad/etapa: Alta / E1
  - Verificar: Generación de bitácora de viajes subutilizados en la ventana de 05:30 a 07:00 para auditoría y balanceo de carga de transporte.
- [ ] **RF-11.06** — El sistema debe proveer un Tablero de Control Operacional en tiempo real que consolide el avance de rutas de despacho, porcentaje de entregas cumplidas, devoluciones en tránsito, alertas activas de cadena de frío y monto recaudado en efectivo.
  - Actor: Gerente Comercial / Gerente de Finanzas / Jefa de Calidad · Prioridad/etapa: Alta / E1
  - Verificar: Despliegue en vivo en pantallas gerenciales con actualización continua de la distribución y alertas críticas de ruta.
  - Respaldo: Caso, RT-05.29, Cap. 9.1, 9.6
- [ ] **RF-11.07** — El sistema debe procesar automáticamente la liquidación y cierre comercial individual por camión al retornar a base, consolidando documentos tributarios entregados, devoluciones físicas recibidas, cobranzas en efectivo y balance de envases retornables.
  - Actor: Gerente de Finanzas / Tripulación propia y peoneta / Conductores externos · Prioridad/etapa: Alta / E1
  - Verificar: Planilla de cuadratura emitida inmediatamente al arribo del camión para tesorería y bodega, sin rezagos para el día siguiente.
  - Respaldo: Caso, RT-05.29, CA-10
- [ ] **RF-11.08** — El sistema debe segmentar mensualmente la cartera de clientes en matrices de rentabilidad neta (margen comercial vs. costo de servir real), sugiriendo ajustes de frecuencia de visita o umbrales mínimos de compra para clientes no rentables.
  - Actor: Gerente Comercial / Preventistas / Gerente de Finanzas · Prioridad/etapa: Media / E2
  - Verificar: Clasificación automática de clientes en rentables, no rentables y estratégicos, con simulación de impacto de cambio de frecuencias.

### M11 · Canal moderno

> Responsabilidad: Pedido EDI y excepciones. Interfaz principal: Contrato por cadena, M3. Actor principal: Cliente del canal moderno, Gerente Comercial. Etapa: 2.

- [ ] El módulo M11 existe en el menú de los actores que lo usan.
- [ ] **RF-12.01** — El sistema debe recibir el mensaje de pedido electrónico estructurado (EDI/EDIFACT/XML, según el estándar que exija cada cadena registrada del canal moderno).
  - Actor: Canal Moderno · Prioridad/etapa: Alta / E2
  - Verificar: El mensaje recibido queda disponible para su validación (RF-12.02) en un plazo no superior a 15 segundos, identificando la cadena de origen.
  - Respaldo: RT-05.23
- [ ] **RF-12.02** — El sistema debe validar automáticamente el pedido EDI recibido, verificando estructura del mensaje, existencia del cliente, existencia de los productos, cantidades, precios y demás datos obligatorios de la cadena.
  - Actor: Canal Moderno · Prioridad/etapa: Alta / E2
  - Verificar: El pedido queda marcado como válido o inválido, con el detalle de cada validación fallida.
  - Respaldo: Caso, cap. 17.1
- [ ] **RF-12.03** — El sistema debe resolver el código de producto informado por la cadena contra el maestro de productos vigente de Puelche, mediante una tabla de equivalencias por cadena.
  - Actor: Canal Moderno · Prioridad/etapa: Alta / E2
  - Verificar: Cada línea queda asociada a un SKU válido del maestro interno, o marcada como discrepancia no resuelta.
- [ ] **RF-12.04** — El sistema debe registrar automáticamente, sin digitación manual, el pedido EDI válido (RF-12.02, RF-12.03) en el sistema de gestión empresarial.
  - Actor: Canal Moderno · Prioridad/etapa: Alta / E2
  - Verificar: El pedido aparece como pedido único en el sistema de gestión dentro de 2 minutos desde su validación.
- [ ] **RF-12.05** — El sistema debe poner a disposición del proceso de planificación de rutas todo pedido registrado proveniente de un canal electrónico.
  - Actor: Planificador de Rutas · Prioridad/etapa: Alta / E2
  - Verificar: El pedido aparece en el listado de pedidos confirmados del módulo de planificación, sin digitación manual.
- [ ] **RF-12.06** — El sistema debe permitir gestionar, mediante una bandeja de excepciones, los pedidos que no pasaron la validación (RF-12.02) o la resolución de maestro (RF-12.03), permitiendo corregir, rechazar o reprocesar cada uno.
  - Actor: Gerente Comercial · Prioridad/etapa: Alta / E2
  - Verificar: Los pedidos con error aparecen en la bandeja con causa, estado, fecha y responsable.
- [ ] **RF-12.07** — El sistema debe enviar a la cadena de origen una confirmación o rechazo del pedido, indicando la causa cuando no pueda ser aceptado completamente.
  - Actor: Canal Moderno · Prioridad/etapa: Alta / E2
  - Verificar: La cadena recibe automáticamente el mensaje correspondiente.
- [ ] **RF-12.08** — El sistema debe mantener el historial de estados de cada pedido electrónico (recepción, validación, confirmación, preparación, despacho, ASN y prueba de entrega).
  - Actor: Gerente Comercial / Planificador de Rutas · Prioridad/etapa: Alta / E2
  - Verificar: Se puede consultar el estado actual y el historial de eventos con fecha, hora y responsable/sistema
- [ ] **RF-12.09** — El sistema debe generar y enviar al cliente del canal moderno un ASN cuando su pedido queda cargado en el camión, referenciando la guía de despacho electrónica ya emitida, con productos, cantidades y hora estimada de llegada.
  - Actor: Canal Moderno · Prioridad/etapa: Alta / E2
  - Verificar: El cliente recibe el ASN dentro de los 2 minutos posteriores a la carga.
  - Respaldo: entrevista Rubén Salinas
- [ ] **RF-12.10** — El sistema debe planificar la llegada del camión al cliente del canal moderno dentro de la ventana horaria de 30 minutos comprometida.
  - Actor: Planificador de Rutas · Prioridad/etapa: Alta / E2
  - Verificar: El camión llega dentro de la ventana comprometida en el 80 % de los casos.
- [ ] **RF-12.11** — El sistema debe registrar el cumplimiento o incumplimiento de la ventana de 30 minutos para cada entrega del canal moderno, distinguiéndola de la ventana crítica de despacho 05:30-07:00.
  - Actor: Tripulación propia y peoneta / Conductores externos · Prioridad/etapa: Alta / E2
  - Verificar: Toda desviación queda registrada con hora real de llegada.
  - Respaldo: RT-10.05
- [ ] **RF-12.12** — El sistema debe capturar evidencia de entrega en el local del cliente: firma en pantalla del titular cuando pueda firmar, o fotografía de la mercadería más nombre de quien recibe cuando no sea el titular o no pueda firmar.
  - Actor: Tripulación propia y peoneta / Conductores externos · Prioridad/etapa: Alta / E2
  - Verificar: Queda un único registro de evidencia por entrega, con el mecanismo utilizado identificado.
  - Respaldo: Caso, Cap. 16.1, Decisión #15
- [ ] **RF-12.13** — El sistema debe enviar al cliente del canal moderno un acuse de recibo digital de la entrega, articulado con la guía de despacho electrónica y su acuse de recibo tributario.
  - Actor: Canal Moderno · Prioridad/etapa: Alta / E2
  - Verificar: El cliente recibe el comprobante dentro de los 30 minutos posteriores a la descarga.
- [ ] **RF-12.14** — El sistema debe publicar un portal web público, sin autenticación, con el catálogo vigente de productos (sin precios ni stock), contacto comercial e información institucional.
  - Actor: Canal Tradicional / Food Service / Canal Moderno · Prioridad/etapa: Media / E2
  - Verificar: Cualquier visitante ve el catálogo sin poder generar pedidos ni ver precios.
  - Respaldo: Caso, RT-16.30
- [ ] **RF-12.15** — El portal autenticado de clientes debe permitir generar un pedido en autoservicio, validando el mismo crédito y stock que consulta el preventista.
  - Actor: Canal Moderno · Prioridad/etapa: Media / E2
  - Verificar: El cliente genera un pedido válido sin intervención de un preventista.
  - Respaldo: Caso, RT-16.30
- [ ] **RF-12.16** — El portal de clientes debe permitir consultar el estado de sus entregas y la ventana de entrega comprometida.
  - Actor: Canal Moderno · Prioridad/etapa: Media / E2
  - Verificar: El cliente visualiza el estado y compromiso de cada pedido.
  - Respaldo: Caso, RT-16.30 / Cap. 9.1
- [ ] **RF-12.17** — El portal de clientes debe permitir consultar y descargar sus documentos tributarios (factura, guía electrónica, nota de crédito).
  - Actor: Canal Moderno · Prioridad/etapa: Media / E2
  - Verificar: El cliente descarga los documentos correspondientes a sus operaciones.
  - Respaldo: Caso, RT-16.30 / RT-16.14
- [ ] **RF-12.18** — El portal de clientes debe permitir consultar el saldo y estado de cuenta del cliente autenticado, con datos del sistema de gestión.
  - Actor: Canal Moderno · Prioridad/etapa: Media / E2
  - Verificar: El cliente consulta su saldo según la información del sistema de gestión.
  - Respaldo: Caso, RT-16.30
- [ ] **RF-12.19** — El portal de transportistas debe permitir consultar las rutas asignadas a la empresa para el día siguiente.
  - Actor: Empresas Transp. · Prioridad/etapa: Media / E2
  - Verificar: La empresa visualiza el día anterior las rutas asignadas.
  - Respaldo: Caso, RT-16.30
- [ ] **RF-12.20** — El portal de transportistas debe permitir descargar la documentación de despacho de cada ruta asignada.
  - Actor: Empresas Transp. · Prioridad/etapa: Media / E2
  - Verificar: La empresa descarga la documentación correspondiente.
  - Respaldo: Caso, RT-16.30
- [ ] **RF-12.21** — El portal debe permitir confirmar, antes de la ventana de despacho, qué conductor y vehículo ejecutarán cada ruta asignada del día.
  - Actor: Empresas Transp. · Prioridad/etapa: Media / E2
  - Verificar: Queda registrado el conductor/vehículo real; si no se confirma, el sistema mantiene la asignación planificada como supuesto no verificado.
- [ ] **RF-12.22** — El portal de proveedores debe permitir consultar, en modo de solo lectura, el estado de sus órdenes de compra.
  - Actor: Proveedores · Prioridad/etapa: Media / E2
  - Verificar: El proveedor consulta el estado actualizado de sus órdenes.
  - Respaldo: Caso, RT-16.30
- [ ] **RF-12.23** — El portal de proveedores debe permitir consultar, en modo de solo lectura, las recepciones registradas para sus órdenes.
  - Actor: Proveedores · Prioridad/etapa: Media / E2
  - Verificar: El proveedor consulta las recepciones actualizadas.
  - Respaldo: Caso, RT-16.30
- [ ] **RF-12.24** — El portal de proveedores debe permitir consultar, en modo de solo lectura, sus devoluciones y notas de crédito.
  - Actor: Proveedores · Prioridad/etapa: Media / E2
  - Verificar: El proveedor consulta las devoluciones/notas de crédito actualizadas.
  - Respaldo: Caso, RT-16.30
- [ ] **RF-12.25** — El portal debe permitir al cliente del canal moderno registrarse con su RUT de empresa, correo electrónico corporativo y una contraseña, siempre que el RUT esté previamente habilitado en el sistema de gestión como cliente activo de Puelche.
  - Actor: Canal Moderno · Prioridad/etapa: Media / E2
  - Verificar: El cliente queda registrado y recibe un correo de confirmación de cuenta. Si el RUT no está habilitado, el sistema informa que debe contactar a su ejecutivo comercial.
- [ ] **RF-12.26** — El portal debe permitir al cliente autenticarse con su correo y contraseña registrados.
  - Actor: Canal Moderno · Prioridad/etapa: Media / E2
  - Verificar: El cliente accede a su área privada. Tras tres intentos fallidos consecutivos, la cuenta queda bloqueada temporalmente.
- [ ] **RF-12.27** — El portal debe permitir al cliente solicitar un enlace de restablecimiento de contraseña a su correo registrado cuando no recuerde su clave.
  - Actor: Canal Moderno · Prioridad/etapa: Media / E2
  - Verificar: El cliente recibe un enlace válido por tiempo limitado que le permite establecer una nueva contraseña. El enlace expira tras su uso o transcurridos 15 minutos.
- [ ] **RF-12.28** — El portal debe permitir al cliente cerrar su sesión de forma explícita, invalidando el token de sesión activo.
  - Actor: Canal Moderno · Prioridad/etapa: Media / E2
  - Verificar: La sesión queda invalidada y el cliente es redirigido a la pantalla de inicio de sesión.
- [x] **RF-12.29** — El portal debe cerrar automáticamente la sesión del cliente tras un período de inactividad definido, sin requerir acción explícita de cierre.
  - Actor: Canal Moderno · Prioridad/etapa: Media / E2
  - Verificar: La sesión expira y el cliente debe iniciar sesión nuevamente para acceder a su área privada.
- [ ] **RF-12.30** — El portal debe permitir al cliente pagar los pedidos generados en autoservicio (RF-12.15) mediante la plataforma de pagos Transbank.
  - Actor: Canal Moderno · Prioridad/etapa: Media / E2
  - Verificar: El pago es procesado por Transbank y el portal registra la confirmación o rechazo de la transacción.
  - ⚠ Revisión externa (04-11-2026) · **Sin verificar** · **Corregible fuera del prototipo**: falta el título en el catálogo del SD3 (rama main; en `tablas/t12_caso.tex` figura como «Materia sin desarrollar»). Se corrige en SD3. **Límite de la simulación**: el cobro real por Transbank (INT-09); el prototipo solo puede mostrar la confirmación o el rechazo simulados.

### M12 · Telemetría

> Responsabilidad: Ruta real, desviación y datos para costo. Interfaz principal: GPS a M4/M10. Actor principal: Planificador de Rutas, Gerente de Operaciones. Etapa: 1, costo en 2.

- [ ] El módulo M12 existe en el menú de los actores que lo usan.
- [ ] **RF-14.01** — El sistema debe integrarse con la plataforma de telemetría de terceros existente que cubre los camiones propios para consumir datos de posición GPS, velocidad y kilometraje.
  - Actor: Gerente de Operaciones · Prioridad/etapa: Crítica / E1
  - Verificar: El sistema muestra en el mapa la ubicación de los 42 camiones propios, igual que hoy, pero integrado en la nueva solución.
  - Respaldo: Caso, cap. 5 (sistemas actuales) y cap. 10, restricción 6; flota propia: 42; flota de diez transportistas: 54. El proveedor existente cubre solo los 42 propios; S-19
- [ ] **RF-14.02** — El sistema debe mostrar en el mapa las rutas planificadas vs las rutas reales recorridas por cada camión, para identificar desviaciones y optimizar las rutas futuras.
  - Actor: Gerente de Operaciones / Planificador de Rutas · Prioridad/etapa: Alta / E1
  - Verificar: El gerente de operaciones ve que el camión 5 se desvía 5 km en su ruta; investiga si es por tráfico, error del conductor o una parada no registrada.
  - Respaldo: Caso, cap. 5 (sistemas actuales) y cap. 10, restricción 6; flota propia: 42; flota de diez transportistas: 54. SD4, T-11, C-02 (terminal por camión con GPS); RF-06 y RF-14.01
- [ ] **RF-14.03** — El sistema debe generar una alerta cuando el camión se desvíe más de 3 km de la ruta planificada, para que el centro de control pueda reaccionar.
  - Actor: Gerente de Operaciones · Prioridad/etapa: Alta / E1
  - Verificar: El centro de control recibe una alerta si un camión se desvía para investigar si hay un problema (accidente, robo, etc.).
  - Respaldo: Caso, cap. 5 (sistemas actuales) y cap. 10, restricción 6; flota propia: 42; flota de diez transportistas: 54. SD4, T-11, C-02 (terminal por camión con GPS); RF-06 y RF-14.01
- [ ] **RF-14.04** — El sistema debe integrar los datos de telemetría con el módulo de costo de servir, imputando kilómetros recorridos y tiempo de viaje a cada entrega y cliente.
  - Actor: Gerente de Finanzas / Gerente de Operaciones · Prioridad/etapa: Crítica / E2
  - Verificar: El costo de servir por cliente incluye el costo real de los kilómetros recorridos para llegar a su local.
  - Respaldo: Caso, cap. 5 (sistemas actuales) y cap. 10, restricción 6; flota propia: 42; flota de diez transportistas: 54. SD4, T-11, C-02 (terminal por camión con GPS); RF-06 y RF-14.01
- [ ] **RF-14.05** — El sistema debe registrar qué conductor propio o de transportista externo está asociado a cada camión en cada viaje, consumiendo la identidad validada por el mecanismo de autenticación (RF-15.02). Esta vinculación es necesaria para imputar responsabilidades en cobros, entregas y eventos de ruta, y para resolver la Decisión #5.
  - Actor: Tripulación propia y peoneta / Conductores externos / Empresas Transp. · Prioridad/etapa: Alta / E1
  - Verificar: Se resuelve la Decisión #5; el sistema exige que el conductor se identifique (PIN o QR) antes de iniciar la ruta, incluso si es externo.
  - Respaldo: Caso, cap. 5 (sistemas actuales) y cap. 10, restricción 6; flota propia: 42; flota de diez transportistas: 54. La asignación vincula personas, vehículos y viajes; 96 camiones no equivale a 96 conductores
- [ ] **RF-14.06** — El sistema debe permitir la gestión de geocercas zonas geográficas, para identificar cuándo un camión entra o sale de una zona ej: CD Talca, zona de clientes, para medir tiempos de llegada y salida.
  - Actor: Gerente de Operaciones / Tripulación propia y peoneta / Conductores externos · Prioridad/etapa: Media / E1
  - Verificar: El sistema registra automáticamente la hora de llegada del camión al área del cliente, para validar el cumplimiento de la ventana horaria.
  - ⚠ Revisión externa (04-11-2026) · **Era parcial** · ✓ **Corregido**: la geocerca creada aparece en la tabla «Geocercas configuradas» y en el mapa de `/telemetria`, y se conserva mientras dure la pestaña. **Límite de la simulación**: la detección automática de entrada y salida con GPS real (Constancia, fila 3).

## 5. Requerimientos transversales (SD3, RF de las BTT)

### Identidad y acceso

- [ ] **RF-15.01** · Gestión centralizada de identidad — El sistema debe contar con una gestión de identidad centralizada, con federación mediante OpenID Connect y OAuth 2.1, o SAML 2.0 cuando la integración con el CLIENTE lo requiera, e integración con el directorio corporativo del CLIENTE por LDAP o equivalente en la nube.
  - Actor: Jefe de TI · Prioridad/etapa: Alta / E1 y E2
  - Verificar: La identidad de todas las personas usuarias internas es gestionada desde un único punto.
  - Respaldo: BTT, RT-12.01
- [ ] **RF-15.02** · Inicio de sesión único (SSO) para todos los módulos — El sistema debe implementar inicio de sesión único para todos los módulos de la solución, con cierre de sesión propagado a todos ellos.
  - Actor: Jefe de TI · Prioridad/etapa: Alta / E1 y E2
  - Verificar: El usuario se autentica una vez y accede a todos los módulos sin reautenticación.
  - Respaldo: BTT, RT-12.02
- [ ] **RF-15.03** · Autenticación multifactor (MFA) para administradores y acceso externo — El sistema debe exigir autenticación multifactor para personas usuarias administradoras, para todo acceso privilegiado y para todo acceso originado fuera de la red corporativa, soportando factores FIDO2 o claves de acceso.
  - Actor: Jefe de TI · Prioridad/etapa: Alta / E1 y E2
  - Verificar: El acceso a perfiles administradores o desde fuera de la red requiere segundo factor.
  - Respaldo: BTT, RT-12.03
- [ ] **RF-15.04** · Control de acceso basado en roles (RBAC) y segregación de funciones — El sistema debe implementar control de acceso basado en roles, complementado con control basado en atributos donde el proceso lo exija, con matriz de segregación de funciones documentada y verificable.
  - Actor: Jefe de TI · Prioridad/etapa: Alta / E1 y E2
  - Verificar: La matriz de roles y permisos es entregada y aprobada por el CLIENTE.
  - Respaldo: BTT, RT-12.05
- [ ] **RF-15.05** · Aprovisionamiento y desaprovisionamiento automatizado de cuentas — El sistema debe automatizar el aprovisionamiento y desaprovisionamiento de cuentas, ligado al ciclo de vida laboral, con baja efectiva en un plazo no superior a 24 horas desde la desvinculación.
  - Actor: Jefe de TI · Prioridad/etapa: Alta / E1 y E2
  - Verificar: Las cuentas son creadas/eliminadas automáticamente según el estado laboral del usuario.
  - Respaldo: BTT, RT-12.10

### Observabilidad y tableros

- [ ] **RF-16.01** · Observabilidad unificada para nube y on-premise — El sistema debe implementar observabilidad unificada para nube y on-premise, con métricas, registros y trazas distribuidas correlacionadas por un identificador único de transacción, instrumentadas conforme a OpenTelemetry.
  - Actor: Jefe de TI · Prioridad/etapa: Alta / E1 y E2
  - Verificar: El equipo de operaciones del CLIENTE puede consultar métricas, logs y trazas desde una única interfaz.
  - Respaldo: BTT, RT-14.01
- [ ] **RF-16.02** · Acceso del CLIENTE a tableros operacionales y de negocio — El CLIENTE debe disponer de acceso propio y permanente a los tableros operacionales y de negocio, con datos en tiempo real y capacidad de exportación.
  - Actor: Jefe de TI / Gerente de Operaciones / Gerente Comercial / Gerente de Finanzas · Prioridad/etapa: Alta / E1 y E2
  - Verificar: El CLIENTE visualiza los tableros en tiempo real y exporta datos.
  - Respaldo: BTT, RT-14.02
- [ ] **RF-16.03** · Alertamiento basado en síntomas de negocio — El sistema debe implementar alertamiento basado en síntomas de negocio y no sólo en umbrales de infraestructura, con supresión de ruido, agrupación, escalamiento automático y turnos de disponibilidad declarados.
  - Actor: Jefe de TI · Prioridad/etapa: Alta / E1 y E2
  - Verificar: Las alertas se generan por síntomas de negocio (ej. OTIF bajo, pedidos no preparados), no solo por CPU alta.
  - Respaldo: BTT, RT-14.04
- [ ] **RF-16.04** · Análisis de causa raíz obligatorio tras incidente crítico — El sistema (o el equipo del ADJUDICATARIO) debe ejecutar un análisis de causa raíz obligatorio tras cada incidente crítico, con informe entregable dentro de cinco días hábiles y seguimiento de las acciones correctivas hasta su cierre.
  - Actor: Jefe de TI · Prioridad/etapa: Alta / E1 y E2
  - Verificar: El informe de causa raíz es entregado al CLIENTE dentro de los 5 días hábiles.
  - Respaldo: BTT, RT-14.06

### Administración, auditoría y servicios comunes

- [ ] **RF-17.01** · Módulo de administración de usuarios, roles y permisos — El sistema debe disponer de un módulo de administración que permita al CLIENTE, sin intervención del ADJUDICATARIO, gestionar personas usuarias, roles, permisos, unidades organizacionales y sus jerarquías.
  - Actor: Jefe de TI · Prioridad/etapa: Alta / E1 y E2
  - Verificar: El administrador del CLIENTE crea, modifica o elimina usuarios/roles desde la interfaz sin desarrollo.
  - Respaldo: BTT, RT-16.01
- [ ] **RF-17.02** · Parametrización de reglas de negocio desde interfaz de administración — El sistema debe permitir parametrizar reglas de negocio (umbrales, plazos, montos, tolerancias, catálogos, listas de valores, textos de notificación) desde la interfaz de administración, con control de versiones y registro de quién cambió qué y cuándo.
  - Actor: Jefe de TI · Prioridad/etapa: Alta / E1 y E2
  - Verificar: El administrador del CLIENTE modifica parámetros de negocio sin desarrollo, con auditoría de cambios.
  - Respaldo: BTT, RT-16.02
- [ ] **RF-17.03** · Aprobación de dos perfiles para cambios de parámetros con impacto operacional — El sistema debe requerir aprobación de un segundo perfil para todo cambio de parámetro con impacto operacional, quedando registrado con su justificación.
  - Actor: Jefe de TI · Prioridad/etapa: Alta / E1 y E2
  - Verificar: El cambio se aplica solo después de la aprobación de un segundo perfil autorizado.
  - Respaldo: BTT, RT-16.03
- [ ] **RF-17.04** · Registro de auditoría inalterable — El sistema debe registrar toda operación que cree, modifique o elimine información, con identificación de la persona o sistema que la ejecutó, fecha/hora con zona horaria, origen, valores anteriores y posteriores. El registro de auditoría debe ser inalterable y no modificable por ningún perfil.
  - Actor: Jefe de TI · Prioridad/etapa: Alta / E1 y E2
  - Verificar: La auditoría es consultable desde la interfaz y no puede ser alterada ni eliminada.
  - Respaldo: BTT, RT-16.06, RT-16.07
- [ ] **RF-17.05** · Consulta y exportación de auditoría desde la interfaz — El CLIENTE debe poder consultar y exportar la auditoría desde la interfaz, con filtros por persona, período, entidad y tipo de operación, sin requerir acceso a la base de datos.
  - Actor: Jefe de TI · Prioridad/etapa: Alta / E1 y E2
  - Verificar: El auditor consulta y exporta la auditoría con los filtros deseados.
  - Respaldo: BTT, RT-16.08
- [ ] **RF-17.06** · Soporte de flujos de trabajo configurables — El sistema debe soportar flujos de trabajo con estados, transiciones, responsables, plazos, escalamiento automático por vencimiento y delegación por ausencia, configurables por el CLIENTE sin desarrollo (al menos en responsables, plazos y niveles de aprobación).
  - Actor: Jefe de TI · Prioridad/etapa: Alta / E1 y E2
  - Verificar: El administrador del CLIENTE configura flujos de trabajo (ej. aprobación de pedidos, gestión de devoluciones) sin desarrollo.
  - Respaldo: BTT, RT-16.11, RT-16.12
- [ ] **RF-17.07** · Bandeja de tareas unificada — El sistema debe proveer una bandeja de tareas unificada para cada persona usuaria, donde se visualicen todas sus tareas pendientes (aprobaciones, revisiones, excepciones) con priorización y alerta de vencimiento.
  - Actor: Jefe de TI / Gerente Comercial / Gerente de Operaciones / Gerente de Finanzas / Jefa de Calidad / Jefa de Bodega / Planificador de Rutas / Preventistas / Preparadores · Prioridad/etapa: Alta / E1 y E2
  - Verificar: El usuario visualiza y gestiona todas sus tareas desde una única bandeja.
  - Respaldo: BTT, RT-16.13
- [ ] **RF-17.08** · Gestión documental con versionado y control de acceso — El sistema debe gestionar documentos con versionado, metadatos, control de acceso, búsqueda por contenido y por metadato, y previsualización sin descarga. Los documentos deben almacenarse cifrados con verificación de integridad.
  - Actor: Jefe de TI · Prioridad/etapa: Alta / E1 y E2
  - Verificar: Los documentos son almacenados, versionados y accesibles según permisos del usuario.
  - Respaldo: BTT, RT-16.15, RT-16.16
- [ ] **RF-17.09** · Generación de documentos a partir de plantillas — El sistema debe generar documentos a partir de plantillas administrables por el CLIENTE, con datos de la transacción y salida en formato abierto PDF, DOCX o XLSX.
  - Actor: Jefe de TI · Prioridad/etapa: Media / E1 y E2
  - Verificar: El usuario genera el documento con los datos de la transacción.
  - Respaldo: BTT, RT-16.19
- [ ] **RF-17.10** · Notificaciones multicanal (correo, SMS, notificación en app) — El sistema debe enviar notificaciones por al menos tres canales: correo electrónico, notificación en la aplicación y SMS o mensajería instantánea, con plantillas administrables por el CLIENTE.
  - Actor: Jefe de TI · Prioridad/etapa: Alta / E1 y E2
  - Verificar: El usuario recibe la notificación por el canal configurado.
  - Respaldo: BTT, RT-16.20, RT-16.21
- [ ] **RF-17.11** · Búsqueda global con indexación de texto completo — El sistema debe disponer de búsqueda global con indexación de texto completo con tolerancia a errores de escritura, filtros facetados y respeto del control de acceso de la persona que busca.
  - Actor: Jefe de TI / Gerente Comercial / Gerente de Operaciones / Gerente de Finanzas / Jefa de Calidad / Jefa de Bodega / Planificador de Rutas / Preventistas / Preparadores · Prioridad/etapa: Alta / E1 y E2
  - Verificar: El usuario encuentra información relevante mediante una búsqueda que no sobrepase más de 2 segundos en la respuesta y ademas de poder estar filtrada.
  - Respaldo: BTT, RT-16.27
- [x] **RF-17.12** · Listados ordenables, filtrables, paginados y exportables — El sistema debe presentar listados ordenables, filtrables, paginados y exportables en formatos abiertos, con el filtro aplicado reflejado en la exportación.
  - Actor: Jefe de TI / Gerente Comercial / Gerente de Operaciones / Gerente de Finanzas / Jefa de Calidad / Jefa de Bodega / Planificador de Rutas / Preventistas / Preparadores · Prioridad/etapa: Alta / E1 y E2
  - Verificar: El usuario ordena, filtra y exporta los datos del listado.
  - Respaldo: BTT, RT-16.28
- [ ] **RF-17.13** · Portal público con catálogo y contacto (sin autenticación) — El sistema debe disponer de un portal público con la información que el caso determine (catálogo sin precios/stock, contacto, información institucional), accesible sin autenticación, con estándares de accesibilidad y desempeño.
  - Actor: Canal Tradicional / Food Service / Canal Moderno · Prioridad/etapa: Media / E1 y E2
  - Verificar: Cualquier visitante accede al portal público y visualiza la información. En E1 se publican la información institucional y el contacto; en E2 se agrega el catálogo de RF-12.14, que concreta este requisito para el caso.
  - Respaldo: BTT, RT-16.31

### Firma y notificaciones

- [x] **RF-18.01** · Soporte de firma electrónica y firma avanzada cuando corresponda — El sistema debe soportar firma electrónica conforme a la Ley N.º 19.799 (2002, art. 2, letra g, y arts. 3–5). La firma avanzada se aplica cuando corresponda según las exigencias legales y del CLIENTE. Se verifica la validez del certificado al firmar, cuando la modalidad lo requiera, y se genera sello de tiempo y conserva la evidencia de firma (Bases Técnicas Transversales, 2026, cap. 16, RT-16.17 y RT-16.18, p. 30).
  - Actor: Jefe de TI / Gerente de Finanzas · Prioridad/etapa: Alta / E1 y E2
  - Verificar: El documento queda firmado mediante la modalidad aplicable y se conserva su evidencia para la verificación posterior.
  - Respaldo: BTT, RT-16.17, RT-16.18
- [ ] **RF-18.02** · Configuración de preferencias de notificación por usuario — Cada persona usuaria debe poder configurar sus preferencias de canal (correo, SMS, notificación en app) y de frecuencia para las notificaciones, respetando las que el CLIENTE defina como obligatorias.
  - Actor: Jefe de TI / Gerente Comercial / Gerente de Operaciones / Gerente de Finanzas / Jefa de Calidad / Jefa de Bodega / Planificador de Rutas / Preventistas (62 personas) / Preparadores (120 personas) / Tripulación propia y peoneta (84 personas) / Conductores externos (aprox. 160 personas) / Canal Tradicional (11.600 clientes) / Food Service (2.100 clientes) / Canal Moderno (500 puntos) / Empresas Transp. (10 empresas) / Proveedores (180 empresas) · Prioridad/etapa: Media / E1 y E2
  - Verificar: El usuario recibe notificaciones por el canal y frecuencia configurados.
  - Respaldo: BTT, RT-16.22
- [ ] **RF-18.03** · Envío asíncrono de notificaciones con reintento y registro — El sistema debe enviar notificaciones de forma asíncrona, con reintento ante falla, control de duplicados y registro de entrega, apertura y error por cada mensaje.
  - Actor: Jefe de TI · Prioridad/etapa: Alta / E1 y E2
  - Verificar: La notificación es enviada y registrada, si falla, se reintenta según política configurada.
  - Respaldo: BTT, RT-16.23

## 6. Reglas de negocio (SD3, RNG)

Cada regla debe verse aplicada en alguna pantalla: una validación, un bloqueo, un estado o un mensaje.

- [ ] **RNG-01 · Reserva de stock** — El pedido se captura aun sin señal. La reserva firme ocurre al confirmar en el servidor central, por orden de recepción y correlativo de desempate. Al sincronizar, el pedido toma su lugar en ese orden; si falta stock, se notifica el quiebre. Cancelaciones y reducciones liberan unidades reservadas no despachadas; las cantidades adicionales se reservan cuando la modificación llega al servidor, si hay stock. Responsable: Sistema. Relación: Evita doble compromiso; RF-02.05, RF-03.03 (S-08).
- [ ] **RNG-02 · Stock disponible** — Disponible = físico habilitado para venta menos reservas firmes, por centro, producto y lote. El tránsito no se vende antes de la recepción; se excluyen vencidos, dañados, lotes retenidos por Calidad y devoluciones pendientes de evaluación. Responsable: Sistema y Bodega; Calidad determina la habilitación de los lotes retenidos. Relación: Evita sobreventa; RF-02.05, RF-02.06.
- [ ] **RNG-03 · Crédito en preventa** — Consulta límite, deuda y crédito disponible del ERP, con fecha de actualización. El bloqueo aplica la fórmula y el umbral definidos por Finanzas. Toda excepción registra supervisor, pedido, monto y motivo. Sin señal se consulta la última información sincronizada y se captura el pedido; el crédito se revalida al sincronizar. Responsable: Supervisor de crédito, conforme a la política de Finanzas. Relación: Bloqueo o excepción trazable; RF-03.04 a RF-03.10.
- [ ] **RNG-04 · Excursión térmica** — La regla por familia evalúa simuladores de producto y retiene los SSCC afectados y las cantidades de cada lote que contienen; el retiro sanitario por lote inmoviliza todos sus SSCC y destinos identificados. La retención térmica se delimita por exposición y no se propaga a unidades no expuestas solo por compartir lote. La regla retiene las unidades afectadas ante crítica o contradicción con el sensor independiente. Durante la puerta abierta y hasta 10 min después del cierre se suspenden solo las advertencias del aire; la crítica nunca se suspende. Sin parámetros aprobados, toda lectura fuera de la ficha es crítica. Si nadie decide dentro del plazo de la familia, el producto sigue retenido y vuelve al CD; nunca se libera automáticamente. Responsable: Calidad dispone; el conductor no libera. Relación: Decisión por SSCC e incidente; RF-09.03 a RF-09.14 (S-04).
- [ ] **RNG-05 · Local cerrado** — El conductor registra intento, hora y causal. El sistema reagenda a la próxima ventana compatible con la ruta y la conservación del producto. Si el cliente continúa ausente, la mercadería retorna al centro de distribución con trazabilidad. Responsable: Sistema; el planificador puede corregir. Relación: Reentrega y retorno trazables; RF-06.04, RF-04.07 (S-03).
- [ ] **RNG-06 · Devolución** — En la entrega se captura SKU, cantidad, motivo, documento asociado y lote cuando corresponda, aun sin señal. El producto se evalúa antes de habilitarlo para venta. El evento y su evidencia se transmiten al ERP sin duplicar efectos. Responsable: Bodega y Finanzas. Relación: El ERP emite la nota de crédito cuando corresponde; RF-06.03, RF-08.01, RF-08.02 (S-12).
- [ ] **RNG-07 · Envases retornables** — Los 68.000 canastillos y 9.400 pallets se controlan por tipo, cliente y transportista, sin serialización unitaria. Cada movimiento registra origen, destino y cantidad. Saldo = inicial conciliado más entregados menos devueltos y ajustes autorizados. Las diferencias se investigan antes de declararse pérdidas. Responsable: Conductor registra; Finanzas revisa. Relación: Los excesos y pérdidas generan alertas e informes; RF-06.09, RF-08.03 a RF-08.06 (S-10).
- [ ] **RNG-08 · Precio** — Se aplica el precio acordado por el preventista al tomar el pedido y registrado en este. Los cambios posteriores de la lista de precios no modifican el importe acordado con el cliente. Responsable: Preventista, conforme a las condiciones comerciales autorizadas. Relación: El precio cobrado respeta lo acordado en el pedido; RF-03.11 conserva el precio y RF-03.12 detecta discrepancias antes de la facturación (S-09).
- [ ] **RNG-09 · OTIF** — OTIF = pedidos completos y a tiempo / pedidos comprometidos para el período × 100. Exige el 100 % de ítems y unidades dentro de la fecha y ventana pactadas. Cada pedido cuenta una vez; reentregas y cambios de promesa conservan historial. Fill rate y perfect order se miden por separado. Responsable: Gerencia Comercial. Relación: Toda entrega parcial o tardía queda incumplida con causal; RF-11.03 (S-01).
- [ ] **RNG-10 · FEFO** — El picking aplica FEFO entre lotes habilitados y compatibles con las condiciones documentadas del cliente. A igual vencimiento, prioriza la recepción más antigua. Toda exclusión registra causa y responsable. Responsable: Sistema y preparador, conforme a los criterios de habilitación. Relación: Reduce merma; RF-02.09, RF-05.05.
- [ ] **RNG-11 · Maestro de productos** — El maestro interno conserva equivalencias GS1 y externas e historial. Cambiar solo el código mantiene la identidad del producto; cambios de formato, contenido o unidad requieren revisión de Catálogo. Códigos desconocidos o ambiguos van a excepción, sin crear productos automáticamente. Responsable: Administrador de catálogo. Relación: Código no resuelto a bandeja de excepción, sin crear una segunda verdad de producto; RF-01.10, RF-12.03 (S-11).
- [ ] **RNG-12 · Sincronización** — Cola local con identificador único y deduplicación; al restablecer el enlace, sincronización automática con reconciliación determinista, regla de resolución documentada, sin sobrescritura silenciosa de conflictos de versión y con bitácora auditable de las decisiones aplicadas (Bases Técnicas Transversales, 2026, cap. 3, RT-03.12, p. 9). Responsable: Servicio de sincronización. Relación: Sin pedidos perdidos o duplicados; RF-03.15, RF-03.16.
- [ ] **RNG-13 · Secuencia térmica** — El picking sigue seco, refrigerado y congelado, preparando los productos fríos próximos a la carga. Durante esperas e interrupciones se mantienen en su zona térmica; las interrupciones se registran. Responsable: Sistema y preparador. Relación: Evita ruptura de frío; RF-05.04, RF-01.11.
- [ ] **RNG-14 · Capacidad y carga** — La ruta no excede peso, volumen ni condición térmica, y ningún camión sale bajo el umbral de ocupación comprometido en S-27. Responsable: Planificador y cargador. Relación: Respeta la capacidad y el mínimo de ocupación; RF-04.03 a RF-04.05, RF-05.07.
- [ ] **RNG-15 · Corte y promesa** — 24 horas para clientes urbanos con pedidos ingresados antes de las 14:00; 48 horas para los urbanos ingresados a las 14:00 o después y para los clientes rurales, periféricos o abastecidos mediante cross-docking. El corte urbano temprano y la segmentación siguen el arbitraje 1 del Subdocumento 2; la extensión al urbano desde las 14:00 es una regla de LafroX (S-21). Responsable: Comercial y Operaciones. Relación: La fecha prometida se muestra al confirmar el pedido y se conserva para medir OTIF; RF-03.13, RF-04.07 (S-21).
- [ ] **RNG-16 · Descuentos** — El preventista aplica las promociones vigentes. Todo descuento excepcional requiere autorización del supervisor comercial y registro de pedido, monto y motivo antes de confirmar. Responsable: Preventista aplica promociones; supervisor comercial autoriza excepciones. Relación: Descuentos autorizados y trazables; RF-03.07. La autorización de descuentos necesita un requerimiento propio.
- [ ] **RNG-17 · Exposición en andén** — Los escaneos de salida de cámara y carga delimitan el tiempo fuera de frío por SSCC. Superar el máximo de su familia bloquea el SSCC antes de salir. Responsable: Calidad aprueba el máximo por familia. Relación: Historia térmica completa; RF-09.11.

## 7. Requerimientos documentales que no se prueban en el prototipo

Se cumplen en el texto de la propuesta (SD4), no en pantallas. Se listan para no buscarlos en el prototipo.

- **RF-13.01** · Declaración de arquitectura multicapa
- **RF-13.02** · Tabla de emplazamiento nube/on-premise
- **RF-13.03** · Registro de decisiones de arquitectura (ADR)
- **RF-13.04** · Modelo de dominio de negocio

## 7.1 Requerimientos no funcionales (SD3, RNF)

SD3 define 90 RNF. Se clasifican según cómo se verifican: 18 se demuestran en el prototipo, 21 requieren medición o pruebas reales (ver «Constancia») y 51 se cumplen en la propuesta técnica.

### Demostrables en el prototipo

| Código | Requerimiento | Dónde | Qué se ve |
|---|---|---|---|
| **RNF-01.02** | Retención de registros de recepción | `/admin/auditoria` | Política de retención por tipo de dato y restauración simulada de una muestra |
| **RNF-01.03** | Operación offline de recepción (24 horas) | `/recepcion` | Corte de enlace simulado: la recepción sigue en la puerta local y encola sin pérdida |
| **RNF-02.01** | Operación offline del CD (24 horas) | `/inventario` | Corte de enlace simulado en inventario, recepción y preparación, con cola y sincronización |
| **RNF-05.02** | Operabilidad con guantes a −22 °C | `/flujo?paso=4` | Botones de picking de 60 px (≈ 15,9 mm) y sin gestos. ✓ Corregido el 04-11-2026: «Cerrar misión» medía 56 px (14,8 mm); ahora todo `.big-btn` mide 60 px. **Límite de la simulación**: el uso real con guantes a −22 °C |
| **RNF-06.01** | Autonomía de reparto sin cobertura | `/terreno` | La app de reparto completa la ruta sin señal: entregas, cobros y prueba de entrega en cola |
| **RNF-08.02** | Retención de registros de devoluciones y mermas | `/admin/auditoria` | Plazos de retención de devoluciones y mermas, con restauración de muestra |
| **RNF-09.02** | Retención de registros sanitarios y de trazabilidad | `/admin/auditoria` | Retención de registros sanitarios: vida útil + 6 meses, mínimo 5 años |
| **RNF-09.03** | Auditoría de consultas y modificaciones de trazabilidad | `/admin/auditoria` | Consultas a lotes, clientes y geolocalización registradas con su finalidad |
| **RNF-09.04** | Operación sin cobertura y sincronización en cámara de frío | `/preparacion` | La bodega opera sin enlace y sincroniza al recuperar la conexión |
| **RNF-09.05** | Frecuencia de registro de temperatura | `/telemetria` | Lectura de cámaras cada 5 minutos |
| **RNF-09.06** | Alarma en ruta sin red | `/terreno` | Alarma y retención del SSCC en la app de reparto sin red móvil ni satélite |
| **RNF-12.02** | Configurabilidad de integración EDI para nuevas cadenas | `/canal-moderno` | Asistente para configurar el mapeo de una cadena nueva sin desarrollo |
| **RNF-13.01** | Disponibilidad del sitio on-premise durante corte de enlace (24h) | `/inventario` | Operación local de la bodega ante corte total del enlace con la nube |
| **RNF-13.02** | Declaración de funciones no disponibles en modo desconectado | `/terreno` | Panel «Qué funciona sin conexión» con las funciones no disponibles y su alternativa |
| **RNF-14.11** | Privacidad de la geolocalización de personas | `/telemetria` | Posición registrada por camión y ruta, no por persona |
| **RNF-15.01** | Política de sesión: duración, inactividad, renovación, revocación | `/perfil` | Cierre de sesión por inactividad del portal, con prueba de demostración |
| **RNF-15.03** | Registro completo del ciclo de vida de la identidad (auditoría) | `/admin/auditoria` | Altas, cambios de rol y cierres de sesión en la auditoría |
| **RNF-17.01** | Retención de auditoría mínima de 5 años | `/admin/auditoria` | Retención de la auditoría por al menos 5 años |

### No demostrables en una simulación

El prototipo muestra la función, pero el valor exigido solo se comprueba midiendo con datos, equipos o personas reales.

| Código | Requerimiento | Cómo se verifica |
|---|---|---|
| RNF-01.01 | Tiempo de respuesta de registro de ítem en recepción | Tiempo de respuesta medido |
| RNF-03.01 | Tiempo de respuesta de registro de línea de pedido | Tiempo de respuesta medido |
| RNF-03.02 | Tiempo de respuesta de consulta de stock y crédito con conectividad | Tiempo de respuesta medido |
| RNF-03.03 | Tiempo de respuesta de consulta de historial de compra | Tiempo de respuesta medido |
| RNF-04.01 | Tiempo de generación de rutas diarias | Tiempo del motor de ruteo con datos reales |
| RNF-05.01 | Latencia de confirmación de picking ( 1s) | Latencia en el dispositivo |
| RNF-05.03 | Curva de aprendizaje (≤ 2 horas) | Prueba de usabilidad con operarios nuevos |
| RNF-07.01 | Tiempo de sincronización de cobranzas tras reconexión | Sincronización con servidor real |
| RNF-08.01 | Tiempo de registro de devoluciones en el andén | Prueba de desempeño en peak |
| RNF-09.01 | Tiempo de obtención de clientes afectados por lote | Tiempo con datos reales |
| RNF-09.07 | Doble camino siempre activo | Redes móviles e Iridium reales |
| RNF-09.08 | Decisión térmica y registro certificado | Termógrafo certificado y mapeo térmico |
| RNF-09.09 | Coherencia de datos | Coherencia de datos con servidor real |
| RNF-11.01 | Latencia de indicadores operacionales del día | Latencia de datos reales |
| RNF-12.03 | Envío del acuse de recibo al canal moderno | Plazo de envío del acuse |
| RNF-16.01 | Indicadores de nivel de servicio medidos sobre experiencia real del usuario | Medición sobre usuarios reales |
| RNF-17.02 | Exportaciones de gran volumen procesadas de forma asíncrona | Exportaciones de gran volumen en servidor |
| RNF-17.03 | Portal público resistente a picos de tráfico | Picos de tráfico reales |
| RNF-19.04 | Pruebas de carga en Preproducción con 1.5× peak y pruebas de estrés | Pruebas de carga en Preproducción |
| RNF-20.01 | Disponibilidad mensual mínima del 99.9% para servicios críticos | Disponibilidad medida en operación |
| RNF-20.04 | Pruebas de resiliencia con inyección de fallas | Inyección de fallas en infraestructura |

> **No se pueden corregir en el prototipo.** La revisión externa del 04-11-2026 marcó RNF-05.03 (aprender en 2 h) y RNF-08.01 (50 devoluciones en 25 min) como parciales. Quedan así: el prototipo muestra la función, pero el valor exigido solo se mide con personas y carga reales. No cuentan como un defecto del prototipo.

### Documentales

Se cumple en la propuesta técnica (SD4 y anexos), no en pantallas: infraestructura, seguridad, continuidad, soporte, capacitación y hardware.

| Código | Requerimiento |
|---|---|
| RNF-07.02 | Cifrado de datos de pagos y comportamiento comercial |
| RNF-11.02 | Aislamiento del procesamiento analítico y transaccional |
| RNF-12.01 | Hito de producción del canal moderno |
| RNF-13.03 | Redundancia de equipos on-premise críticos |
| RNF-13.04 | Tolerancia del almacenamiento local a la falla de un disco |
| RNF-13.05 | Declaración y justificación del nivel RAID |
| RNF-13.06 | Endurecimiento de sistemas on-premise según CIS Benchmarks |
| RNF-13.07 | Enlace redundante entre on-premise y nube |
| RNF-13.08 | Dimensionamiento de ancho de banda por sitio |
| RNF-13.09 | Estudio de cobertura de red inalámbrica en sitios operacionales (incluye cámaras de frío) |
| RNF-14.01 | Cifrado en tránsito con TLS 1.3 |
| RNF-14.02 | Cifrado en reposo de todos los datos |
| RNF-14.03 | Segregación de red en la nube (subredes privadas) |
| RNF-14.04 | SIEM con casos de uso de detección específicos del negocio |
| RNF-14.05 | Detección y respuesta en puntos finales (EDR) |
| RNF-14.06 | Pruebas de intrusión anuales por tercero independiente |
| RNF-14.07 | Análisis estático de código, SCA y escaneo de contenedores en CI/CD |
| RNF-14.08 | Inventario de componentes de software (SBOM) en formato CycloneDX/SPDX |
| RNF-14.09 | Verificación de procedencia de artefactos según SLSA nivel 3 |
| RNF-14.10 | Prohibición de datos productivos en ambientes no productivos |
| RNF-14.12 | Categorías de datos personales en terreno |
| RNF-15.02 | Credenciales de sesión firmadas y de vida breve |
| RNF-16.02 | Libro de operación y guía de resolución documentados |
| RNF-16.03 | Registros sin datos personales sensibles ni credenciales |
| RNF-19.01 | Cálculo de capacidad con supuestos de usuarios concurrentes y TPS |
| RNF-19.02 | Escalamiento horizontal automático de capas de aplicación e integración |
| RNF-19.03 | Identificación del cuello de botella al crecer la carga |
| RNF-20.02 | Clasificación de servicios por criticidad (crítico, alto, medio, bajo) |
| RNF-20.03 | Plan de continuidad del negocio conforme a ISO 22301 |
| RNF-20.05 | Documentación de comportamiento ante falla de dependencias externas |
| RNF-20.06 | Site secundario para DR: RTO 4h, RPO 15 min |
| RNF-20.07 | Política de respaldo 3-2-1-1-0 (3 copias, 2 medios, 1 fuera de sitio, 1 inmutable, 0 errores) |
| RNF-21.01 | Centro de operaciones de red (NOC) 24×7×365 |
| RNF-21.02 | Gerente de servicio dedicado para el CLIENTE |
| RNF-21.03 | Centro de atención telefónica: 80% en 20 segundos, 70% resolución primer contacto |
| RNF-21.04 | Horario de atención ampliado a 24×7 para incidentes críticos y ventana de despacho (05:30-07:00) |
| RNF-21.05 | Dimensionamiento de la dotación del centro de atención con teoría de colas o Erlang C |
| RNF-21.06 | Canal único de registro de incidentes con ticket y seguimiento |
| RNF-21.07 | Traslado a sitios alejados (Curicó, Chillán, Los Ángeles) para resolución de incidentes |
| RNF-21.08 | Bolsa anual de horas de mantención evolutiva |
| RNF-21.09 | Planificación anual de actualizaciones de versiones de componentes |
| RNF-22.01 | Plan de capacitación estructurado por perfil (usuarios, administradores, técnicos) |
| RNF-22.02 | Material de capacitación en español, editable y de propiedad del CLIENTE |
| RNF-22.03 | Capacitación sin afectar la operación: programación por turnos y horarios acordados |
| RNF-22.04 | Evaluación y certificación de usuarios administradores y equipo técnico |
| RNF-22.05 | Capacitación de personal nuevo del CLIENTE sin costo adicional durante la Operación |
| RNF-22.06 | Acompañamiento y mentoría al equipo técnico del CLIENTE durante 6 meses post producción |
| RNF-23.01 | Especificación de hardware de terreno con marca, modelo, cantidad y características |
| RNF-23.02 | Dispositivos con grado de protección IP y resistencia a caídas coherentes con el entorno |
| RNF-23.03 | Ciclo de vida esperado de cada dispositivo y plan de reposición durante 56 meses |
| RNF-23.04 | Estaciones de trabajo para operación y administración con monitores duales |

> **No se puede corregir en el prototipo.** RNF-12.01 (hito de producción del canal moderno), marcado parcial en la revisión externa del 04-11-2026, es una fecha del plan de trabajo. Se acredita en el SD7 (Gantt y T-15), no en una pantalla.

## 8. Verificación de la continuación (03-11-2026)

Se marcaron los controles de Prioridad 3 comprobados en `revision/verify.cjs`: RF-12.29, RF-17.12, RF-18.01, vista ligera y atajos/borradores. RF-18.01 se marca **solo como simulación**, con evidencia local, sin certificado real ni validez legal. La vista ligera omite las imágenes por completo en vez de descargarlas.

La planilla fue regenerada: 186 RF/RNG con ruta, 10 RT con su evaluación previa y 6 requerimientos documentales. Sus estados indican trazabilidad, no aceptación. No se marcan automáticamente las demás casillas por tener una etiqueta en el código; las verificaciones de Prioridades 1–2 comunicadas en el traspaso no sustituyen repetir cada criterio de esta lista.

Detalle de pruebas, barrido responsive y limitaciones: `revision/verificacion_prioridad3.md`.

## 9. Pendientes detectados

| Código | Pantalla o ruta | Observación | Responsable |
|---|---|---|---|
| Aceptación detallada | Todas las rutas | Repetir criterios no marcados antes de certificar cumplimiento integral; no confundirlos con funcionalidades ausentes | |
| Revisión externa 04-11-2026 | Ver sección 10 | ✓ Corregidos los 8 requerimientos y los 10 datos. Pendiente: las 3 acciones fuera del prototipo (10.2). Los límites de 10.1 no se corrigen | |

## 10. Revisión externa del 04-11-2026: qué se corrige y qué no

Cada observación se clasifica en una de tres categorías. Solo la tercera es un límite del prototipo; las otras dos son defectos.

**Estado al 04-11-2026:** todo lo corregible en el prototipo (10.3 y 10.4) quedó corregido y verificado en el navegador, con el perfil de evaluación, en escritorio y a 375 px, sin errores de JavaScript ni desplazamiento horizontal. Siguen pendientes las tres acciones de 10.2 (fuera del prototipo) y los límites de 10.1, que no se pueden corregir.

- **Corregible en el prototipo**: falta la pantalla, el dato está mal o la simulación no reacciona. Se arregla en `js/` o `css/`.
- **Corregible fuera del prototipo**: depende de publicar el sitio o de corregir otro documento (SD3).
- **No corregible: límite de la simulación**: exige servidor, integración, dispositivos, personas o tiempo reales (Bases Técnicas Transversales, 25.6). Se acredita en otro entregable.

Un mismo requerimiento puede tener una parte corregible y otra no: la parte simulada se corrige y la parte real se declara.

### 10.1 No corregibles: límites de la simulación

| Código | Qué no se puede demostrar | Cómo se acredita |
|---|---|---|
| RT-25.07 | Que el enlace siga en línea durante seis meses: solo se comprueba con el paso del tiempo | Publicación estable y compromiso de mantener el repositorio |
| RT-25.03 | La revisión con lector de pantalla no es una pantalla, es una prueba manual | Informe de conformidad WCAG (entregable 17) |
| RNF-05.02 | Uso real con guantes a −22 °C | Prueba en terreno con el terminal especificado |
| RNF-05.03 | Aprendizaje en 2 h | Prueba de usabilidad con operarios nuevos |
| RNF-08.01 | 50 devoluciones en 25 min | Prueba de desempeño en peak |
| RNF-12.01 | Hito de producción del canal moderno | SD7: Gantt y T-15 |
| RF-03.11, RF-07.08 | Envío y conciliación real con el ERP | Pruebas de integración (Constancia, fila 1) |
| RF-06.08 | Emisión real del OTP, su expiración y el plazo de 2 min | Pruebas de aceptación (Constancia, filas 5 y 10) |
| RF-08.07 | Costo de servir con datos reales y persistencia | Pruebas de aceptación de M10 |
| RF-12.30 | Cobro real por Transbank | Pruebas de integración INT-09 |
| RF-14.06 | Entrada y salida detectadas por GPS real | Pruebas con telemetría (Constancia, fila 3) |

### 10.2 Corregibles fuera del prototipo

| Código | Observación | Acción |
|---|---|---|
| RT-25.06 | patricioh315.github.io/LafroX responde 404 | Activar GitHub Pages en la rama LafroX-Prototipo-HTML y probar el enlace |
| RF-02.09 | Sin título único en el catálogo del SD3 de main | Unificar el título en `sd3/tablas/` y `sd3/tablas_anexo/` |
| RF-12.30 | Sin título en el catálogo del SD3 de main | Completar el título en `sd3/tablas/` |

### 10.3 Corregibles en el prototipo: requerimientos (✓ corregidos el 04-11-2026)

| Código | Observación | Corrección | Dónde verificar |
|---|---|---|---|
| RF-03.11 | No hay excepción de precio por cliente o cadena | ✓ Excepciones por cliente o cadena, con vigencia y autorización sobre 15 % | `/clientes/:id` › Excepciones de precio |
| RF-03.12 | La alerta de cambio de precio existe en un solo pedido | ✓ Se calcula en cada pedido no facturado con diferencia contra la lista vigente | `/pedidos?precio=dif` |
| RF-06.08 | Acepta cualquier código de 8 dígitos | ✓ Solo el código emitido; rechaza el incorrecto y el vencido | `/ingresar` › Credencial de turno |
| RF-07.08 | Al aprobar un pago no aparece en «Envío al ERP» | ✓ Cada aprobación agrega su mensaje | `/rendicion` › Pagos web › Envío al ERP |
| RF-08.07 | Una merma no cambia el costo de servir; el 14 % es fijo | ✓ El costo de servir suma las devoluciones por destino | `/devoluciones/:id` y `/clientes/:id` |
| RF-14.06 | La geocerca nueva no aparece en la lista ni en el mapa | ✓ Aparece en ambos | `/telemetria` › Geocercas |
| RNF-05.02 | «Cerrar misión» mide 14,8 mm | ✓ 60 px (≈ 15,9 mm) | `/flujo?paso=4` |
| RT-25.03 | Botones del paso a paso de 38 px de alto | ✓ 44 px | `/flujo` y todo `.stepper` |

### 10.4 Corregibles en el prototipo: datos simulados (✓ corregidos el 04-11-2026)

Ninguno era un límite de la simulación: eran datos de ejemplo incoherentes entre sí.

| Dato | Incoherencia | Corrección |
|---|---|---|
| Patente KXTR-98 | Estaba en R-09 (con frío) y en R-12 (sin frío) | ✓ Una patente distinta por ruta; KXTR-98 queda solo en R-09 |
| Ruta R-01 | Usaba PFGD-51 en Rutas y KXTR-21 en la app de reparto | ✓ R-01 usa KXTR-21 en todas las pantallas |
| Stock disponible | Negativo en Azúcar, Detergente y Papel higiénico | ✓ Lo reservado nunca supera el stock físico; ningún disponible es negativo |
| Ruta R-10 | Decía «Consolidada · 82 %» y su ocupación seguía en 68 % | ✓ Pasa de 64 % a 82 % al consolidar |
| Plan de rutas | Decía «84 rutas» y la tabla mostraba 12 | ✓ Plan, aviso e inicio dicen 12 rutas y 343 entregas, calculadas de la tabla |
| Devolución DV-5530 | Usaba un lote que no existía para ese producto | ✓ Toda devolución usa producto y lote de una línea de su pedido |
| OTIF por ruta | El eje llegaba a 200 % | ✓ Los ejes en porcentaje terminan en 100 % |
| Alerta térmica | Decía «consigna de 4 °C» y el gráfico marcaba «Meta 8» | ✓ La alerta y el gráfico distinguen consigna (4 °C) y límite de excursión (8 °C). La lectura crítica pasó de 7,9 °C a 8,6 °C, porque 7,9 °C no superaba el límite |
| Pedidos de R-01 | La ruta iba en camino y sus pedidos figuraban como «Capturado sin conexión» | ✓ Los pedidos sin planificar no tienen ruta; los de R-01 están «En ruta» o entregados |
| Segregación de funciones | El aviso solo se activaba para Finanzas | ✓ El aviso revisa todos los roles con «Crear» y «Aprobar», al abrir y al cambiar la matriz |
