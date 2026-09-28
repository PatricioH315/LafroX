<a id="seccion-1"></a>

# Anexos del Subdocumento 3

## Índice

- [Anexo 3.A — Catálogo de requerimientos funcionales](#seccion-2)
- [Anexo 3.B — Catálogo de requerimientos no funcionales](#seccion-3)
- [Anexo 3.C — Registro de supuestos](#seccion-4)
- [Anexo 3.D — Registro de exclusiones](#seccion-5)
- [Anexo 3.E — Registro de restricciones](#seccion-6)
- [Anexo 3.F — Registro de decisiones de alcance y de diseño](#seccion-7)
- [Anexo 3.G — Registro de reglas de negocio](#seccion-8)
- [Anexo 3.H — Registro de vacíos y consultas](#seccion-9)
- [Anexo 3.I — Participación de los grupos de interés](#seccion-10)
- [Anexo 3.J — Criterios de aceptación](#seccion-11)
- [Anexo 3.K — Glosario de siglas y códigos](#seccion-12)
- [Material complementario recibido: tablas_anexo](#seccion-13)
  - [Material recibido: capas](#seccion-14)
  - [Material recibido: decisiones](#seccion-15)
  - [Material recibido: emplazamiento](#seccion-16)
  - [Material recibido: estrategia](#seccion-17)
  - [Material recibido: exclusiones](#seccion-18)
  - [Material recibido: hitos](#seccion-19)
  - [Material recibido: reglas negocio](#seccion-20)
  - [Material recibido: restricciones](#seccion-21)
  - [Material recibido: resultados cap18](#seccion-22)
  - [Material recibido: rf](#seccion-23)
  - [Material recibido: rnf](#seccion-24)
  - [Material recibido: supuestos](#seccion-25)
  - [Material recibido: trazabilidad](#seccion-26)
  - [Material recibido: vacios](#seccion-27)
- [Referencias](#seccion-28)
- [Declaración de uso de IA](#seccion-29)


Estos anexos detallan el estado de los catálogos y registros que el cuerpo resume. Se utilizan como fuentes las Bases del caso y los subdocumentos 1 y 2 (Distribuidora Puelche S.A., 2026; LafroX, 2026). El Formulario T-12 se entrega como archivo independiente; no está incrustado aquí.

**Nota de trabajo:** Los campos vacíos conservan materias sin desarrollo. Para completarlos se requiere la evidencia indicada junto a cada registro; no representan exclusiones del alcance ni cumplimiento acreditado.

<a id="seccion-2"></a>

## Anexo 3.A — Catálogo de requerimientos funcionales

Se distinguen los requerimientos desarrollados y las materias cuyo desarrollo permanece vacío. La correspondencia identifica los RF resumidos del Subdocumento 2 sin renumerarlos.

La Tabla [3.A.1](#tabla-3-a-1) presenta requerimientos funcionales con desarrollo respaldado.

<a id="tabla-3-a-1"></a>

**Tabla 3.A.1 — Requerimientos funcionales con desarrollo respaldado. Fuente: Bases del caso y SD2, anexo 2.1.**

| **ID** | **Descripción y actor** | **Precondición** | **Resultado** | **Prioridad / etapa** | **Origen** |
| --- | --- | --- | --- | --- | --- |
| RF-01.02 | Registrar el lote de todo producto que requiere trazabilidad en la recepción. Actor: Recepción | Producto sujeto a trazabilidad recibido. | Recepción asociada al lote. | Crítica / E1 | Caso, cap. 18, criterio 2; SD2, anexo 2.1, RF-02 |
| RF-01.03 | Registrar el vencimiento del producto recibido. Actor: Recepción | Producto recibido con fecha de vencimiento. | Vencimiento disponible para gestión FEFO. | Alta / E1 | SD2, anexo 2.1, RF-02 y RF-03 |
| RF-01.06 | Capturar el código GS1-128 de los productos recibidos. Actor: Recepción | Código disponible en el producto. | Código asociado al registro de recepción. | Alta / E1 | SD2, anexo 2.1, RF-02 |
| RF-02.08 | Asignar existencias para preparación siguiendo FEFO. Actor: Bodega | Existencias con vencimiento registrado. | Asignación ordenada por vencimiento. | Alta / E1 | SD2, anexo 2.1, RF-03 |
| RF-03.01 | Mostrar stock disponible en la consulta en línea al tomar el pedido. Actor: Preventista | Inicio de captura del pedido. | Información de stock visible durante la consulta en línea. | Crítica / E1 | Caso, cap. 18, criterio 5; SD2, anexo 2.1, RF-01 |
| RF-03.02 | Mostrar la información de stock disponible en el dispositivo durante una toma sin señal. Actor: Preventista | Inicio de captura del pedido. | Información local de stock visible sin conexión; regla de reserva aún sin desarrollar. | Crítica / E1 | Caso, cap. 18, criterio 5; SD2, anexo 2.1, RF-01 |
| RF-03.04 | Mostrar crédito y deuda del cliente en la consulta en línea. Actor: Preventista | Cliente identificado. | Información comercial visible en línea. | Crítica / E1 | Caso, cap. 18, criterio 5; SD2, sección 2.5 y anexo 2.1, RF-01 |
| RF-03.05 | Mostrar crédito y deuda del cliente con la información disponible sin conexión. Actor: Preventista | Cliente identificado. | Información comercial local visible sin señal. | Crítica / E1 | Caso, cap. 18, criterio 5; SD2, sección 2.5 y anexo 2.1, RF-01 |
| RF-03.16 | Evitar la duplicación de pedidos al recuperar conectividad. Actor: Preventa | Pedidos capturados sin señal. | Pedidos sincronizados sin duplicación. | Crítica / E1 | Caso, cap. 18, criterio 6 |
| RF-04.01 | Generar automáticamente la ruta del día siguiente en menos de 20 minutos. Actor: Planificador | Pedidos y restricciones de ruta disponibles. | Ruta propuesta para revisión. | Alta / E1 | Caso, cap. 18, criterio 7; SD2, anexo 2.1, RF-06 |
| RF-04.02 | Permitir corregir la ruta propuesta y registrar cada corrección. Actor: Planificador | Ruta propuesta disponible. | Ruta corregida con registro de cambios. | Alta / E1 | Caso, cap. 18, criterio 7; SD2, anexo 2.1, RF-06 |
| RF-05.01 | Generar y consolidar hojas digitales de preparación por olas y zonas. Actor: Jefatura de bodega | Pedidos disponibles para preparación. | Trabajo de preparación organizado por olas. | Alta / E1 | SD2, anexo 2.1, RF-04 |
| RF-05.03 | Registrar la causa de cada faltante en el momento de producirse. Actor: Preparador | Faltante detectado durante preparación. | Faltante asociado a su causa. | Alta / E1 | Caso, cap. 18, criterio 15 |
| RF-05.05 | Asignar existencias para preparación siguiendo FEFO. Actor: Bodega | Existencias con vencimiento registrado. | Asignación ordenada por vencimiento. | Alta / E1 | SD2, anexo 2.1, RF-03 |
| RF-06.02 | Capturar firma en pantalla como parte de la prueba digital de entrega. Actor: Conductor y receptor | Entrega en el punto del cliente. | Firma asociada al registro de entrega. | Crítica / E1 | SD2, anexo 2.1, RF-08 |
| RF-06.05 | Registrar el cobro en efectivo en el punto de entrega. Actor: Conductor | Cliente paga en efectivo. | Cobro asociado a la entrega para rendición. | Alta / E1 | Caso, cap. 10, restricción 5; cap. 18, criterio 10; SD2, RF-10 |
| RF-06.12 | Registrar la recepción de mercadería sin conectividad. Actor: Conductor y receptor | Entrega en zona sin señal. | Evidencia conservada para sincronización. | Crítica / E1 | Caso, cap. 10, restricción 3; SD2, RF-08 |
| RF-07.02 | Conciliar el efectivo el mismo día y registrar la explicación de toda diferencia. Actor: Tesorería y conductor | Cobros y dinero rendido disponibles. | Rendición conciliada con diferencias explicadas. | Alta / E1 | Caso, cap. 18, criterio 10; SD2, RF-10 |
| RF-07.03 | Conciliar el efectivo el mismo día y registrar la explicación de toda diferencia. Actor: Tesorería y conductor | Cobros y dinero rendido disponibles. | Rendición conciliada con diferencias explicadas. | Alta / E1 | Caso, cap. 18, criterio 10; SD2, RF-10 |
| RF-09.01 | Obtener los clientes afectados por un lote con evidencia en menos de dos horas. Actor: Calidad | Lote sujeto a investigación o retiro. | Relación de destinos y clientes afectados disponible. | Crítica / E1 | Caso, cap. 18, criterio 1; SD2, RF-11 |
| RF-09.02 | Reconstruir el origen del lote asociado a una entrega. Actor: Calidad | Lote sujeto a investigación o retiro. | Origen y movimientos del lote identificables. | Crítica / E1 | Caso, cap. 18, criterio 1; SD2, RF-11 |
| RF-09.03 | Registrar automáticamente la temperatura de cámaras de forma continua. Actor: Calidad | Operación de almacenamiento o transporte refrigerado. | Registro térmico de cámaras auditable y disponible. | Crítica / E1 | Caso, cap. 18, criterio 3; SD2, RF-07 |
| RF-09.04 | Registrar automáticamente la temperatura de vehículos de forma continua. Actor: Calidad | Operación de almacenamiento o transporte refrigerado. | Registro térmico de transporte auditable y disponible. | Crítica / E1 | Caso, cap. 18, criterio 3; SD2, RF-07 |
| RF-09.05 | Alertar ante excursiones térmicas. Actor: Calidad y operaciones | Lecturas disponibles y regla térmica definida. | Alerta disponible para tratamiento operacional. | Crítica / E1 | SD2, RF-07; Caso, cap. 16.1, decisión 4 |
| RF-11.02 | Determinar costo de servir por cliente y entrega a partir de hechos operacionales. Actor: Finanzas | Hechos de cada entrega disponibles. | Costo individual disponible para análisis. | Media / E2 | Caso, cap. 18, criterio 11; SD2, RF-14 |
| RF-11.03 | Medir las entregas completas y a tiempo con una única definición. Actor: Operaciones | Entrega y compromiso comercial registrados. | Indicador comparable entre áreas. | Alta / | Caso, cap. 18, criterio 4 |
| RF-12.01 | Recibir pedidos electrónicos estructurados de las cadenas, sin redigitación. Actor: Canal moderno | Intercambio habilitado con la cadena. | Pedido recibido por intercambio electrónico. | Alta / E2 | Caso, cap. 18, criterio 13; SD2, RF-13 |
| RF-12.09 | Responder al pedido de la cadena con aviso de despacho. Actor: Canal moderno | Intercambio habilitado con la cadena. | Aviso de despacho emitido al canal moderno. | Alta / E2 | Caso, cap. 18, criterio 13; SD2, RF-13 |
| RF-12.14 | Permitir consultar el catálogo en línea. Actor: Cliente | Información comercial disponible. | Catálogo disponible para consulta. | Media / E2 | SD2, anexo 2.1, RF-12 |
| RF-12.16 | Permitir consultar el estado del pedido y entrega en el portal. Actor: Cliente | Información comercial disponible. | Estado disponible para el cliente. | Media / E2 | SD2, anexo 2.1, RF-12 |
| RF-12.17 | Permitir consultar la documentación de facturación en el portal. Actor: Cliente | Información comercial disponible. | Documentos disponibles para consulta. | Media / E2 | SD2, anexo 2.1, RF-12 |

**Nota de trabajo:** La descomposición es parcial; las etapas vacías no están asignadas. Para completarlo se requiere cerrar las materias del registro siguiente y la correspondencia del catálogo.

La Tabla [3.A.2](#tabla-3-a-2) presenta correspondencia entre rf resumidos del sd2 y rf detallados del sd3.

<a id="tabla-3-a-2"></a>

**Tabla 3.A.2 — Correspondencia entre RF resumidos del SD2 y RF detallados del SD3. Fuente: SD2, anexo 2.1; consolidación del SD3.**

| **RF del SD2** | **RF del SD3 con desarrollo respaldado** | **Etapa SD2** | **Prioridad SD2** |
| --- | --- | --- | --- |
| RF-01 | RF-03.01, RF-03.02, RF-03.04, RF-03.05, RF-03.16 | E1 | Crítica |
| RF-02 | RF-01.02, RF-01.03, RF-01.06 | E1 | Crítica |
| RF-03 | RF-02.08, RF-05.05 | E1 | Alta |
| RF-04 | RF-05.01 | E1 | Alta |
| RF-05 |  | E1 | Alta |
| RF-06 | RF-04.01, RF-04.02 | E1 | Alta |
| RF-07 | RF-09.03, RF-09.04, RF-09.05 | E1 | Crítica |
| RF-08 | RF-06.02, RF-06.12 | E1 | Crítica |
| RF-09 |  | E1 | Alta |
| RF-10 | RF-06.05, RF-07.02, RF-07.03 | E1 | Alta |
| RF-11 | RF-09.01, RF-09.02 | E1 | Crítica |
| RF-12 | RF-12.14, RF-12.16, RF-12.17 | E2 | Media |
| RF-13 | RF-12.01, RF-12.09 | E2 | Alta |
| RF-14 | RF-11.02 | E2 | Media |

**Nota de trabajo:** RF-05 y RF-09 del SD2 aún no tienen una correspondencia detallada validada; los demás enlaces son parciales. Para completarlo se requiere descomponer cross-docking y acuse tributario, y revisar cobertura completa sin reutilizar identificadores con otro significado.

La Tabla [3.A.3](#tabla-3-a-3) presenta identificadores rf conservados sin desarrollo adoptado.

<a id="tabla-3-a-3"></a>

**Tabla 3.A.3 — Identificadores RF conservados sin desarrollo adoptado. Fuente: inventario previo del SD3; no constituye compromiso.**

| **ID** | **Materia del catálogo de trabajo** | **Descripción** | **Etapa** | **Prioridad** |
| --- | --- | --- | --- | --- |
| RF-01.01 | Recepción y Validación de Cantidades contra OC |  |  |  |
| RF-01.04 | Registro de No Conformidades en Recepción |  |  |  |
| RF-01.05 | Cuarentena Automática por No Conformidad |  |  |  |
| RF-01.07 | Generación e Impresión de Etiqueta SSCC |  |  |  |
| RF-01.08 | Asignación de SSCC a Ubicación de Almacenamiento |  |  |  |
| RF-01.09 | Integración de Recepción con ERP |  |  |  |
| RF-01.10 | Gestión de Fichas de Producto |  |  |  |
| RF-01.11 | Validación de Compatibilidad Térmica en Putaway |  |  |  |
| RF-02.01 | Configuración de topología de instalaciones |  |  |  |
| RF-02.02 | Consolidación de stock físico multi-sitio |  |  |  |
| RF-02.03 | Reasignación de ubicaciones (slotting) |  |  |  |
| RF-02.04 | Conteo cíclico en modo ciego |  |  |  |
| RF-02.05 | Cálculo de stock disponible para la venta |  |  |  |
| RF-02.06 | Gestión de inventario en tránsito |  |  |  |
| RF-02.07 | Consulta de nivel de ocupación por zona |  |  |  |
| RF-02.09 | Retención sanitaria de lote en inventario |  |  |  |
| RF-02.10 | Ficha de trazabilidad de lote |  |  |  |
| RF-03.03 | Reserva de stock al confirmar el pedido |  |  |  |
| RF-03.06 | Consulta de historial de compra del cliente |  |  |  |
| RF-03.07 | Aplicación de promociones a una línea de pedido |  |  |  |
| RF-03.08 | Alerta por superación del límite de crédito |  |  |  |
| RF-03.09 | Bloqueo de envío por exceso de crédito |  |  |  |
| RF-03.10 | Autorización de excepción por supervisor de crédito |  |  |  |
| RF-03.11 | Configuración de excepción de precio por cliente o cadena |  |  |  |
| RF-03.12 | Alerta al cliente por cambio de precio |  |  |  |
| RF-03.13 | Información de ventana de entrega comprometible |  |  |  |
| RF-03.14 | Sugerencia de productos al preventista |  |  |  |
| RF-03.15 | Generación de identificador único de pedido offline |  |  |  |
| RF-04.03 | Bloqueo de asignación por exceso de capacidad |  |  |  |
| RF-04.04 | Ajuste de secuencia de ruta por ventanas horarias |  |  |  |
| RF-04.05 | Restricción de vehículos por requisito de cadena de frío |  |  |  |
| RF-04.06 | Notificación de hora estimada de llegada al cliente |  |  |  |
| RF-04.07 | Parametrización de ventanas horarias |  |  |  |
| RF-04.08 | Cálculo integral del costo de entrega realizada |  |  |  |
| RF-05.02 | Validación de líneas por escaneo GS1 |  |  |  |
| RF-05.04 | Secuenciación térmica de misiones |  |  |  |
| RF-05.06 | Envío de preparación al ERP |  |  |  |
| RF-05.07 | Carga dirigida inversa a ruta |  |  |  |
| RF-06.01 | Confirmación de recepción de bultos |  |  |  |
| RF-06.03 | Reporte de rechazo de productos |  |  |  |
| RF-06.04 | Reporte de local cerrado y reagendamiento automático |  |  |  |
| RF-06.06 | Registro de hora real de llegada y término de la entrega |  |  |  |
| RF-06.07 | Sincronización automática de registros de turno |  |  |  |
| RF-06.08 | Autenticación del conductor externo por clave de un solo uso |  |  |  |
| RF-06.09 | Captura de devolución de envases retornables |  |  |  |
| RF-06.10 | Actualización de saldo de envases retornables |  |  |  |
| RF-06.11 | Confirmación de recepción mediante QR |  |  |  |
| RF-06.13 | Impresión de comprobante térmico en terreno |  |  |  |
| RF-07.01 | Cálculo del monto esperado de rendición por camión |  |  |  |
| RF-07.04 | Consola de Gestión de Cartera de Crédito |  |  |  |
| RF-07.05 | Alerta y Bloqueo de Crédito en Preventa |  |  |  |
| RF-07.06 | Cobro con Terminal POS Móvil en Ruta |  |  |  |
| RF-07.07 | Consulta de Estado de Cuenta en Portal de Clientes |  |  |  |
| RF-07.08 | Validación en Tesorería de Pagos Web |  |  |  |
| RF-07.09 | Interfaz Asíncrona de Cobranzas hacia ERP |  |  |  |
| RF-07.10 | Registro de Abonos y Pagos Parciales en Entrega |  |  |  |
| RF-07.11 | Cobranza Presencial de Facturas por Preventistas |  |  |  |
| RF-08.01 | Registro de Devoluciones en Ruta |  |  |  |
| RF-08.02 | Gestión del Destino de Productos Devueltos |  |  |  |
| RF-08.03 | Gestión de Cuenta Corriente de Envases Retornables |  |  |  |
| RF-08.04 | Alertas por Exceso de Envases Retornables |  |  |  |
| RF-08.05 | Registro de Mermas por Vencimiento |  |  |  |
| RF-08.06 | Reporte de Pérdida de Envases Retornables |  |  |  |
| RF-08.07 | Integración de Devoluciones y Mermas al Costo de Servir |  |  |  |
| RF-09.06 | Retención automática del lote ante excursión térmica |  |  |  |
| RF-09.07 | Registro de rechazo del cliente por sospecha de ruptura de frío |  |  |  |
| RF-09.08 | Registro de lotes con control sanitario |  |  |  |
| RF-09.09 | Generación de cumplimiento de cadena de frío |  |  |  |
| RF-09.10 | Parametrización de la regla de excursión térmica |  |  |  |
| RF-10.01 | Sugerencia de reposición de compras por SKU y proveedor |  |  |  |
| RF-10.02 | Incorporación de promociones comprometidas a la reposición |  |  |  |
| RF-10.03 | Traspaso de la sugerencia aprobada al módulo de compras del ERP |  |  |  |
| RF-11.01 | Distribución Automática de Reportes Ejecutivos |  |  |  |
| RF-11.04 | Medición de Fill Rate y Perfect Order con POD Móvil |  |  |  |
| RF-11.05 | Monitoreo y Alerta de Ocupación de Flota |  |  |  |
| RF-11.06 | Tablero de Control Operacional en Tiempo Real |  |  |  |
| RF-11.07 | Liquidación y Cierre Comercial por Camión |  |  |  |
| RF-11.08 | Segmentación de Clientes por Rentabilidad Neta |  |  |  |
| RF-12.02 | Validación automática del pedido EDI |  |  |  |
| RF-12.03 | Resolución del código de producto contra el maestro de Puelche |  |  |  |
| RF-12.04 | Registro automático del pedido EDI válido en el sistema de gestión |  |  |  |
| RF-12.05 | Disponibilización del pedido a la planificación de despacho |  |  |  |
| RF-12.06 | Gestión de excepciones de pedidos EDI inválidos |  |  |  |
| RF-12.07 | Confirmación o rechazo del pedido a la cadena de origen |  |  |  |
| RF-12.08 | Historial de estados del pedido electrónico |  |  |  |
| RF-12.10 | Planificación de la llegada dentro de la ventana de 30 minutos |  |  |  |
| RF-12.11 | Registro del cumplimiento de la ventana de entrega |  |  |  |
| RF-12.12 | Captura de evidencia de entrega en canal moderno |  |  |  |
| RF-12.13 | Envío de acuse de recibo digital al cliente |  |  |  |
| RF-12.15 | Pedido en autoservicio para clientes del canal moderno |  |  |  |
| RF-12.18 | Consulta de saldo y estado de cuenta en el portal de clientes |  |  |  |
| RF-12.19 | Consulta de rutas asignadas en el portal de transportistas |  |  |  |
| RF-12.20 | Descarga de documentación de despacho en el portal de transportistas |  |  |  |
| RF-12.21 | Confirmación diaria de conductor y vehículo |  |  |  |
| RF-12.22 | Consulta de órdenes de compra en el portal de proveedores |  |  |  |
| RF-12.23 | Consulta de recepciones en el portal de proveedores |  |  |  |
| RF-12.24 | Consulta de devoluciones y notas de crédito en el portal de proveedores |  |  |  |
| RF-12.25 | Registro de cliente en el portal |  |  |  |
| RF-12.26 | Inicio de sesión en el portal de clientes |  |  |  |
| RF-12.27 | Recuperación de contraseña |  |  |  |
| RF-12.28 | Cierre de sesión en el portal de clientes |  |  |  |
| RF-12.29 | Expiración automática de sesión por inactividad |  |  |  |
| RF-12.30 | Pago electrónico de pedidos de autoservicio |  |  |  |
| RF-13.01 | Declaración de arquitectura multicapa |  |  |  |
| RF-13.02 | Tabla de emplazamiento nube/on-premise |  |  |  |
| RF-13.03 | Registro de decisiones de arquitectura (ADR) |  |  |  |
| RF-13.04 | Modelo de dominio de negocio |  |  |  |
| RF-14.01 | Integración con telemetría de camiones propios |  |  |  |
| RF-14.02 | Visualización de rutas planificadas vs reales |  |  |  |
| RF-14.03 | Alerta de desviación de ruta |  |  |  |
| RF-14.04 | Integración de telemetría con costo de servir |  |  |  |
| RF-14.05 | Vinculación conductor-camión en cada viaje |  |  |  |
| RF-14.06 | Gestión de geocercas para control de llegada/salida |  |  |  |
| RF-15.01 | Gestión centralizada de identidad |  |  |  |
| RF-15.02 | Inicio de sesión único (SSO) para todos los módulos |  |  |  |
| RF-15.03 | Autenticación multifactor (MFA) para administradores y acceso externo |  |  |  |
| RF-15.04 | Control de acceso basado en roles (RBAC) y segregación de funciones |  |  |  |
| RF-15.05 | Aprovisionamiento y desaprovisionamiento automatizado de cuentas |  |  |  |
| RF-16.01 | Observabilidad unificada para nube y on-premise |  |  |  |
| RF-16.02 | Acceso del CLIENTE a tableros operacionales y de negocio |  |  |  |
| RF-16.03 | Alertamiento basado en síntomas de negocio |  |  |  |
| RF-16.04 | Análisis de causa raíz obligatorio tras incidente crítico |  |  |  |
| RF-17.01 | Módulo de administración de usuarios, roles y permisos |  |  |  |
| RF-17.02 | Parametrización de reglas de negocio desde interfaz de administración |  |  |  |
| RF-17.03 | Aprobación de dos perfiles para cambios de parámetros con impacto operacional |  |  |  |
| RF-17.04 | Registro de auditoría inalterable |  |  |  |
| RF-17.05 | Consulta y exportación de auditoría desde la interfaz |  |  |  |
| RF-17.06 | Soporte de flujos de trabajo configurables |  |  |  |
| RF-17.07 | Bandeja de tareas unificada |  |  |  |
| RF-17.08 | Gestión documental con versionado y control de acceso |  |  |  |
| RF-17.09 | Generación de documentos a partir de plantillas |  |  |  |
| RF-17.10 | Notificaciones multicanal (correo, SMS, notificación en app) |  |  |  |
| RF-17.11 | Búsqueda global con indexación de texto completo |  |  |  |
| RF-17.12 | Listados ordenables, filtrables, paginados y exportables |  |  |  |
| RF-17.13 | Portal público con catálogo y contacto (sin autenticación) |  |  |  |
| RF-18.01 | Soporte de firma electrónica avanzada (Ley 19.799) |  |  |  |
| RF-18.02 | Configuración de preferencias de notificación por usuario |  |  |  |
| RF-18.03 | Envío asíncrono de notificaciones con reintento y registro |  |  |  |
| RF-19.01 | Clasificación de información por nivel de sensibilidad |  |  |  |
| RF-19.02 | Matriz de controles de seguridad trazable a ISO 27001/27002 |  |  |  |
| RF-19.03 | Declaración de superficie de exposición |  |  |  |
| RF-19.04 | Plan de respuesta a incidentes de seguridad |  |  |  |
| RF-19.05 | Notificación de brecha de seguridad al CLIENTE |  |  |  |

**Nota de trabajo:** Estos identificadores conservan su materia, pero no un requisito aprobado. Para completarlo se requiere contrastar cada materia con las Bases y completar actor, precondición, resultado, origen y prioridad.

<a id="seccion-3"></a>

## Anexo 3.B — Catálogo de requerimientos no funcionales

Se conservan los umbrales contrastados; el resto de los identificadores requiere desarrollo. Un campo de método vacío no acredita una prueba.

La Tabla [3.A.4](#tabla-3-a-4) presenta rnf con umbral respaldado.

<a id="tabla-3-a-4"></a>

**Tabla 3.A.4 — RNF con umbral respaldado. Fuente: Bases y SD2.**

| **ID** | **Materia** | **Umbral** | **Método de verificación** | **Origen** |
| --- | --- | --- | --- | --- |
| RNF-01.03 | Recepción sin enlace y entrega diferida al ERP | Recepción operable durante cortes de enlace. |  | Caso, cap. 10, restricción 2 |
| RNF-02.01 | Sincronización del centro de distribución tras un corte de 24 h | Sincronización del centro tras 24 horas de corte en no más de 2 horas, con resolución determinista de conflictos. |  | Caso, cap. 15, fila de sincronización; BTT, RT-03.12 |
| RNF-04.01 | Tiempo de generación de la ruta del día siguiente | Generación de la ruta del día siguiente en menos de 20 minutos. |  | Caso, cap. 18, criterio 7 |
| RNF-05.02 | Operabilidad con guantes térmicos a -22 °C | Dispositivos operables a -22 °C y sin señal en la cámara. |  | Caso, cap. 10, restricción 7 |
| RNF-06.01 | Persistencia local de la jornada de reparto | Registrar la jornada íntegra de reparto durante 14 horas sin cobertura. |  | Caso, cap. 15, RT-03.10; SD2, RNF-RESIL |
| RNF-06.03 | Sincronización del dispositivo de reparto tras 14 h sin señal | Sincronización del dispositivo tras un turno sin señal en no más de 10 minutos. |  | Caso, cap. 15, fila de sincronización; BTT, RT-03.12 |
| RNF-09.01 | Respuesta a un retiro sanitario | Lista de clientes afectados por lote con evidencia en menos de 2 horas. |  | Caso, cap. 18, criterio 1 |
| RNF-12.01 | Hito de producción del canal moderno | Capacidades exigidas por la principal cadena en producción antes de enero de 2029. |  | Caso, sección 13.2 |
| RNF-13.01 | Operación autónoma del componente on-premise | Recepción, preparación y despacho autónomos durante al menos 24 horas sin enlace. |  | Caso, cap. 15; BTT, RT-03.10 |
| RNF-20.06 | Recuperación ante desastres | RTO ≤ 4 horas; RPO ≤ 15 minutos para servicios críticos; prueba de conmutación al menos dos veces al año. |  | BTT, RT-07.04 y RT-07.07; SD2, RNF-DR |
| RNF-21.01 | Centro de operaciones de red | Monitoreo operacional 24 × 7. |  | SD1, sección 1.1; SD2, anexo 2.3, Jefe de TI |
| RNF-22.03 | Capacitación sin detener la operación | Capacitación y acompañamiento sin detener venta ni reparto y considerando turno nocturno. |  | Caso, sección 13.3, condiciones 4 y 5 |
| RNF-23.01 | Especificación del hardware de terreno | Especificar cantidades y características del hardware de terreno que compra el CLIENTE. |  | Caso, cap. 11 |

**Nota de trabajo:** Los métodos vacíos todavía no constituyen pruebas diseñadas. Para completarlo se requiere definir procedimiento, datos, instrumento y evidencia.

La Tabla [3.A.5](#tabla-3-a-5) presenta identificadores rnf sin umbral adoptado.

<a id="tabla-3-a-5"></a>

**Tabla 3.A.5 — Identificadores RNF sin umbral adoptado. Fuente: inventario previo del SD3; no constituye compromiso.**

| **ID** | **Materia del catálogo de trabajo** | **Umbral** | **Método** |
| --- | --- | --- | --- |
| RNF-01.01 | Tiempo de registro de un ítem en recepción |  |  |
| RNF-01.02 | Retención de registros de recepción |  |  |
| RNF-03.01 | Registro de una línea de pedido en preventa |  |  |
| RNF-03.02 | Consulta de stock y crédito en preventa |  |  |
| RNF-03.03 | Consulta del historial de compra |  |  |
| RNF-05.01 | Confirmación de una línea de picking |  |  |
| RNF-05.03 | Curva de aprendizaje del preparador |  |  |
| RNF-06.02 | Duración del acceso sin conexión por perfil |  |  |
| RNF-07.01 | Preconciliación de cobranzas al reconectar |  |  |
| RNF-07.02 | Cifrado a nivel de campo de datos de pago y de comportamiento de pago |  |  |
| RNF-08.01 | Registro de una devolución en el andén de retorno |  |  |
| RNF-08.02 | Retención de devoluciones y mermas |  |  |
| RNF-09.02 | Retención de la trazabilidad sanitaria |  |  |
| RNF-09.03 | Registro de consultas a la trazabilidad y a información sensible |  |  |
| RNF-09.04 | Captura de temperatura sin señal |  |  |
| RNF-09.05 | Frecuencia de registro de temperatura |  |  |
| RNF-11.01 | Latencia de los indicadores de la operación del día |  |  |
| RNF-11.02 | Desacople entre analítica y transacción |  |  |
| RNF-11.03 | Cierre comercial del día |  |  |
| RNF-11.04 | Latencia de los indicadores de gestión |  |  |
| RNF-12.02 | Incorporación de una cadena nueva sin desarrollo |  |  |
| RNF-12.03 | Envío del acuse de recibo al canal moderno |  |  |
| RNF-13.02 | Funciones no disponibles sin conexión |  |  |
| RNF-13.03 | Redundancia de equipos on-premise críticos |  |  |
| RNF-13.04 | Tolerancia a la falla de disco |  |  |
| RNF-13.05 | Nivel RAID declarado |  |  |
| RNF-13.06 | Endurecimiento de sistemas on-premise |  |  |
| RNF-13.07 | Enlace redundante entre sitio y nube |  |  |
| RNF-13.08 | Ancho de banda por sitio |  |  |
| RNF-13.09 | Cobertura inalámbrica en los sitios |  |  |
| RNF-14.01 | Cifrado en tránsito |  |  |
| RNF-14.02 | Cifrado en reposo |  |  |
| RNF-14.03 | Segregación de red en nube |  |  |
| RNF-14.04 | Correlación de eventos de seguridad |  |  |
| RNF-14.05 | Detección y respuesta en puntos finales |  |  |
| RNF-14.06 | Pruebas de intrusión |  |  |
| RNF-14.07 | Análisis de código y de dependencias |  |  |
| RNF-14.08 | Inventario de componentes de software |  |  |
| RNF-14.09 | Procedencia de artefactos |  |  |
| RNF-14.10 | Datos productivos en ambientes no productivos |  |  |
| RNF-14.11 | Privacidad de la geolocalización de personas |  |  |
| RNF-14.12 | Categorías de datos personales en terreno |  |  |
| RNF-15.01 | Política de sesión |  |  |
| RNF-15.02 | Credenciales de sesión |  |  |
| RNF-15.03 | Auditoría del ciclo de vida de la identidad |  |  |
| RNF-16.01 | Indicadores de nivel de servicio sobre la experiencia real |  |  |
| RNF-16.02 | Libros de operación y guías de resolución |  |  |
| RNF-16.03 | Registros sin datos sensibles ni credenciales |  |  |
| RNF-17.01 | Retención de la auditoría |  |  |
| RNF-17.02 | Exportaciones de gran volumen |  |  |
| RNF-17.03 | Portal público ante picos de tráfico |  |  |
| RNF-19.01 | Cálculo de capacidad |  |  |
| RNF-19.02 | Escalamiento horizontal automático |  |  |
| RNF-19.03 | Componente que se satura primero |  |  |
| RNF-19.04 | Pruebas de carga y estrés |  |  |
| RNF-20.01 | Disponibilidad de los servicios críticos |  |  |
| RNF-20.02 | Clasificación de servicios por criticidad |  |  |
| RNF-20.03 | Continuidad del negocio |  |  |
| RNF-20.04 | Pruebas de resiliencia |  |  |
| RNF-20.05 | Comportamiento ante falla de dependencias externas |  |  |
| RNF-20.07 | Política de respaldo |  |  |
| RNF-21.02 | Gerente de servicio dedicado |  |  |
| RNF-21.03 | Umbrales de atención de la mesa |  |  |
| RNF-21.04 | Horario de atención |  |  |
| RNF-21.05 | Dimensionamiento de la mesa de ayuda |  |  |
| RNF-21.06 | Canal único de registro |  |  |
| RNF-21.07 | Traslado de especialistas a sitios alejados |  |  |
| RNF-21.08 | Bolsa anual de mantención evolutiva |  |  |
| RNF-21.09 | Actualización anual de componentes de base |  |  |
| RNF-22.01 | Plan de capacitación por perfil |  |  |
| RNF-22.02 | Material de capacitación |  |  |
| RNF-22.04 | Certificación de administradores y técnicos |  |  |
| RNF-22.05 | Capacitación del personal nuevo del CLIENTE |  |  |
| RNF-22.06 | Mentoría al equipo de TI del CLIENTE |  |  |
| RNF-23.02 | Protección de los dispositivos de terreno |  |  |
| RNF-23.03 | Ciclo de vida de los dispositivos |  |  |
| RNF-23.04 | Estaciones de trabajo de operación y administración |  |  |

**Nota de trabajo:** No se trasladan cifras del catálogo previo sin contraste. Para completarlo se requiere documentar umbral, fuente exacta, método y etapa por requerimiento.

<a id="seccion-4"></a>

## Anexo 3.C — Registro de supuestos

Las dieciséis materias del numeral 16.1 conservan sus identificadores. Solo se desarrolla lo respaldado; las notas indican qué falta resolver.

La Tabla [3.A.6](#tabla-3-a-6) presenta supuestos y decisiones pendientes de completar.

<a id="tabla-3-a-6"></a>

**Tabla 3.A.6 — Supuestos y decisiones pendientes de completar. Fuente: registro previo; SD2 y Bases para las decisiones expresamente desarrolladas.**

| **ID** | **Materia** | **Contenido respaldado** | **Fuente del contenido** | **Nota de trabajo: falta completar** |
| --- | --- | --- | --- | --- |
| S-01 | Entrega cumplida y OTIF |  |  | Resolver la materia y documentar fundamento, consecuencias e instancia de validación. |
| S-02 | Unidad de trazabilidad sanitaria |  |  | Resolver la materia y documentar fundamento, consecuencias e instancia de validación. |
| S-03 | Local cerrado |  |  | Resolver la materia y documentar fundamento, consecuencias e instancia de validación. |
| S-04 | Excursión térmica |  |  | Resolver la materia y documentar fundamento, consecuencias e instancia de validación. |
| S-05 | Conductor de empresa transportista |  |  | Resolver la materia y documentar fundamento, consecuencias e instancia de validación. |
| S-06 | Efectivo | Se mantiene el cobro en efectivo y se registra para conciliación; no se exige pago electrónico al canal tradicional. | Caso, cap. 10, restricción 5; SD2, RF-10 | Definir custodia, límites y responsabilidades por dinero en circulación. |
| S-07 | Costo de servir |  |  | Resolver la materia y documentar fundamento, consecuencias e instancia de validación. |
| S-08 | Asignación de stock |  |  | Resolver la materia y documentar fundamento, consecuencias e instancia de validación. |
| S-09 | Cambio de precio entre toma y despacho |  |  | Resolver la materia y documentar fundamento, consecuencias e instancia de validación. |
| S-10 | Envases retornables |  |  | Resolver la materia y documentar fundamento, consecuencias e instancia de validación. |
| S-11 | Maestro de productos |  |  | Resolver la materia y documentar fundamento, consecuencias e instancia de validación. |
| S-12 | Devolución en la entrega |  |  | Resolver la materia y documentar fundamento, consecuencias e instancia de validación. |
| S-13 | Objeción sindical |  |  | Resolver la materia y documentar fundamento, consecuencias e instancia de validación. |
| S-14 | Sistema de gestión de almacenes de 2013 | Reemplazo modular progresivo del sistema de bodega. | SD2, anexo 2.3, inventario de sistemas legados | Fundamentar alternativas y definir transición, migración y reversión; la decisión de alcance no acredita su diseño. |
| S-15 | Prueba de entrega sin firma del titular |  |  | Resolver la materia y documentar fundamento, consecuencias e instancia de validación. |
| S-16 | Conocimiento del planificador | Capturar el conocimiento del planificador mediante talleres en los meses 1 a 3, bajo el supuesto de cooperación durante los primeros cuatro meses. | SD2, sección 2.5, supuesto 1 | Confirmar fecha de retiro y definir prueba de transferencia a un reemplazo. |
| S-17 | Fecha de inicio del contrato |  |  | Resolver la materia y documentar fundamento, consecuencias e instancia de validación. |
| S-18 | Interfaces del ERP |  |  | Resolver la materia y documentar fundamento, consecuencias e instancia de validación. |
| S-19 | Acceso a la telemetría existente |  |  | Resolver la materia y documentar fundamento, consecuencias e instancia de validación. |
| S-20 | Hardware de terreno disponible |  |  | Resolver la materia y documentar fundamento, consecuencias e instancia de validación. |
| S-21 | Promesa de entrega |  |  | Resolver la materia y documentar fundamento, consecuencias e instancia de validación. |
| S-22 | Seis instalaciones, cinco con cómputo |  |  | Resolver la materia y documentar fundamento, consecuencias e instancia de validación. |
| S-23 | Tripulación por camión |  |  | Resolver la materia y documentar fundamento, consecuencias e instancia de validación. |
| S-24 | Desconexión nominal y de diseño |  |  | Resolver la materia y documentar fundamento, consecuencias e instancia de validación. |
| S-25 | Historia de ventas para la reposición |  |  | Resolver la materia y documentar fundamento, consecuencias e instancia de validación. |

**Nota de trabajo:** Los campos vacíos no representan decisiones adoptadas ni conformidad del CLIENTE. Para completarlo se requiere resolver cada decisión del numeral 16.1 y los supuestos adicionales.

<a id="seccion-5"></a>

## Anexo 3.D — Registro de exclusiones

Las nueve exclusiones del capítulo 11 se conservan expresamente. Los identificadores adicionales permanecen vacíos hasta verificar su fundamento.

La Tabla [3.A.7](#tabla-3-a-7) presenta exclusiones explícitas.

<a id="tabla-3-a-7"></a>

**Tabla 3.A.7 — Exclusiones explícitas. Fuente: Caso, cap. 11.**

| **ID** | **Exclusión** |
| --- | --- |
| EX-01 | No se pide reemplazar el sistema de gestión empresarial ni ninguno de sus módulos, ni la emisión de documentos tributarios electrónicos. |
| EX-02 | No se pide administrar remuneraciones ni recursos humanos, que residen en el sistema de gestión. |
| EX-03 | No se pide un sistema de punto de venta para el local del cliente, sin perjuicio del canal de autoatención que la solución deba ofrecerle. |
| EX-04 | No se pide comercio electrónico dirigido al consumidor final. |
| EX-05 | No se pide administrar el contrato ni el pago de las empresas transportistas, sí integrarlas operacionalmente. |
| EX-06 | No se pide el diseño de la red logística: la ubicación de los centros de distribución y de las plataformas no está en discusión en este proyecto. |
| EX-07 | No se pide automatizar la bodega con equipamiento robotizado ni transportadores. |
| EX-08 | No se pide la gestión de la flota en su dimensión mecánica, sin perjuicio de integrar la telemetría existente. |
| EX-09 | El hardware de terreno —dispositivos, lectores, impresoras portátiles, sensores— lo adquiere el CLIENTE; el PROPONENTE debe especificar exactamente qué comprar, cuánto y con qué características, conforme al Capítulo 8 de las Bases Técnicas Transversales. |
| EX-10 |  |
| EX-11 |  |

<a id="seccion-6"></a>

## Anexo 3.E — Registro de restricciones

Se reproducen las doce restricciones del caso. Las filas adicionales vacías requieren cotejo específico y no modifican las obligaciones de las Bases.

La Tabla [3.A.8](#tabla-3-a-8) presenta restricciones del caso.

<a id="tabla-3-a-8"></a>

**Tabla 3.A.8 — Restricciones del caso. Fuente: Caso, cap. 10.**

| **ID** | **Restricción** | **Origen** |
| --- | --- | --- |
| R-01 | El despacho de la mañana no se detiene. Entre las 05:30 y las 07:00 salen 96 camiones. No existe forma de ejecutar esa ventana a mano. Un sistema indisponible en ese tramo equivale a un día sin operación. | Caso, cap. 10, restricción 1 |
| R-02 | El centro de distribución debe poder recibir, preparar y despachar durante un corte del enlace. La preparación nocturna y la carga no pueden quedar detenidas por conectividad. | Caso, cap. 10, restricción 2 |
| R-03 | Las aplicaciones de preventa y de reparto deben funcionar un turno completo sin señal. Hay rutas donde el dispositivo no recupera cobertura hasta el regreso. | Caso, cap. 10, restricción 3 |
| R-04 | El sistema de gestión no se reemplaza ni se modifica. Es el sistema de registro contable y tributario. La solución le entrega datos; el sistema de gestión emite los documentos tributarios. No habrá dos verdades ni un segundo emisor. | Caso, cap. 10, restricción 4 |
| R-05 | No se puede exigir al cliente del canal tradicional que tenga internet, dispositivo propio ni medio de pago electrónico. La solución debe funcionar con el cliente tal como es. | Caso, cap. 10, restricción 5 |
| R-06 | La solución debe operar con conductores que no son trabajadores de la compañía: 54 camiones de diez empresas transportistas, con rotación sin aviso. | Caso, cap. 10, restricción 6 |
| R-07 | Los dispositivos que se usen en la cámara de congelado deben operar a -22 °C y sin cobertura de señal en su interior. | Caso, cap. 10, restricción 7 |
| R-08 | Congelamiento operacional: prohibido intervenir sistemas entre el 1 y el 25 de septiembre y durante todo el mes de diciembre. Prohibido intervenir durante los tres primeros días hábiles del mes, por el cierre comercial y contable. | Caso, cap. 10, restricción 8 |
| R-09 | El área de tecnologías de información de la compañía son cuatro personas. Toda función que requiera un especialista dedicado que la compañía no tiene debe ofrecerse como servicio y estar costeada. | Caso, cap. 10, restricción 9 |
| R-10 | El sindicato de conductores objetó formalmente, el año pasado, la instalación de cámaras en cabina y el control de jornada por posicionamiento satelital. Cualquier propuesta que involucre esas tecnologías debe hacerse cargo del asunto. | Caso, cap. 10, restricción 10 |
| R-11 | La rotación anual del personal de preparación de pedidos es del 38 % y el turno crítico es nocturno. Toda solución que exija entrenamiento prolongado para operar en bodega será rechazada. | Caso, cap. 10, restricción 11 |
| R-12 | La emisión de documentos tributarios electrónicos debe cumplir la normativa vigente. La guía de despacho electrónica y su acuse de recibo tienen efectos legales que la solución no puede comprometer. | Caso, cap. 10, restricción 12 |
| R-13 |  |  |
| R-14 |  |  |
| R-15 |  |  |
| R-16 |  |  |
| R-17 |  |  |
| R-18 |  |  |
| R-19 |  |  |
| R-20 |  |  |
| R-21 |  |  |
| R-22 |  |  |

**Nota de trabajo:** La interpretación de las restricciones no define una arquitectura implementada. Para completarlo se requiere completar diseño y evidencia respetando estas condiciones.

<a id="seccion-7"></a>

## Anexo 3.F — Registro de decisiones de alcance y de diseño

Se conservan las materias del registro anterior sin presentar como adoptadas las decisiones que no cuentan con respaldo consolidado.

La Tabla [3.A.9](#tabla-3-a-9) presenta registro de decisiones de alcance y diseño.

<a id="tabla-3-a-9"></a>

**Tabla 3.A.9 — Registro de decisiones de alcance y diseño. Fuente: registro de decisiones y Bases.**

| **ID** | **Materia** | **Decisión** | **Fundamento** |
| --- | --- | --- | --- |
| D-01 | Reparto entre etapas | Etapa 1 habilita captura, OTIF y continuidad; Etapa 2 incorpora canal moderno y costo de servir. | La segunda etapa depende de hechos operacionales confiables. |
| D-02 | Medición de OTIF | M10 calcula OTIF diariamente; el costo de servir se completa en Etapa 2. | Evita definiciones distintas por área. |
| D-03 | Promesa de entrega | Se parametriza por cliente, zona y capacidad; no hay una ventana universal. | El caso distingue canales y cobertura rural. |
| D-04 | Aceptación | Los criterios del Cap. 18 se prueban en marcha blanca con evidencia y responsable. | Una pantalla no demuestra un resultado de negocio. |
| D-05 | Reposición | Usa historia de ventas y excepciones revisables. | Sustituye la planilla sin convertir una estimación en decisión irreversible. |
| D-06 | Implantación | Despliegue por proceso y zona, con capacitación, conciliación y marcha blanca. | El despacho no admite un corte general. |
| D-07 | Reversión | Responsable operativo autoriza reversión; registros quedan en cola para conciliación. | Preserva evidencia y evita pérdida o duplicación. |
| D-08 | Modo desconectado | Terreno opera 14 h y CD 24 h con captura local, UUID y sincronización idempotente. | Obligación del caso y RT-03.10/03.12. |
| D-09 | Analítica avanzada | Ruteo determinístico y explicable; no se incorpora IA como sustituto de reglas. | El planificador debe revisar y corregir la ruta. |
| D-10 | Mesa de servicio | Atención 04:00–22:00 L–S y 24x7 en septiembre y diciembre. | Horario particular exigido por el caso. |

**Nota de trabajo:** Las decisiones son propuestas de la oferta; su aceptación se verifica en la instancia de gobierno correspondiente. Para completarlo se requiere conservar la evidencia de validación y sus efectos en la planificación.

<a id="seccion-8"></a>

## Anexo 3.G — Registro de reglas de negocio

Estas reglas forman parte del registro de requerimientos. Sus campos vacíos requieren precisar captura, punto del proceso, autoridad, consecuencia e identificadores relacionados.

La Tabla [3.A.10](#tabla-3-a-10) presenta registro de reglas de negocio.

<a id="tabla-3-a-10"></a>

**Tabla 3.A.10 — Registro de reglas de negocio. Fuente: Caso, cap. 16.1 y 17.1; reglas_de_negocio.md.**

| **ID** | **Materia** | **Qué y dónde se captura** | **Quién decide** | **Consecuencia y RF** |
| --- | --- | --- | --- | --- |
| RNG-01 | Reserva de stock | Reserva al confirmar; offline muestra antigüedad. | Sistema y bodega. | Evita doble compromiso; RF-02.05, RF-03.03. |
| RNG-02 | Stock disponible | Disponible = físico menos comprometido; tránsito no se vende antes de recepción. | Sistema y bodega. | Evita sobreventa; RF-02.05, RF-02.06. |
| RNG-03 | Crédito en preventa | Consulta límite y deuda; excepción registrada. | Supervisor de crédito. | Bloqueo o excepción trazable; RF-03.04–03.10. |
| RNG-04 | Excursión térmica | Sensor registra, sistema alerta y retiene el lote. | Calidad. | Liberación o disposición trazable; RF-09.03–09.10. |
| RNG-05 | Local cerrado | Conductor registra; sistema propone próxima ventana. | Planificador. | Reentrega trazable; RF-06.04, RF-04.07. |
| RNG-06 | Devolución | Captura SKU, cantidad y motivo aun sin señal. | Bodega y Finanzas. | Proceso tributario en ERP; RF-06.03, RF-08.01–02. |
| RNG-07 | Envases retornables | Entrega descuenta y devolución suma saldo por cliente. | Conductor y preventista. | Controla pérdida; RF-06.09, RF-08.03–06. |
| RNG-08 | Precio | Precio de despacho; excepción configurada por cliente o cadena. | Administrador comercial. | Alerta al cliente; RF-03.11–03.13. |
| RNG-09 | OTIF | In-Full exige unidades completas y On-Time ventana pactada. | Gerencia comercial. | Parcial queda con causal; RF-11.03–04. |
| RNG-10 | FEFO | Picking prioriza vencimiento y deja excepción. | Sistema y preparador. | Reduce merma; RF-02.08, RF-05.05. |
| RNG-11 | Maestro de productos | Maestro interno conserva equivalencias GS1 y externas. | Administrador de catálogo. | Excepción para código no resuelto; RF-01.10, RF-12.03. |
| RNG-12 | Sincronización | Cola local con UUID, deduplicación y bitácora. | Servicio de sincronización. | Sin pedidos perdidos o duplicados; RF-03.15–16. |
| RNG-13 | Secuencia térmica | Picking sigue seco, refrigerado y congelado. | Sistema y preparador. | Evita ruptura de frío; RF-05.04, RF-01.11. |
| RNG-14 | Capacidad y carga | Ruta no excede peso, volumen ni condición térmica. | Planificador y cargador. | Evita rechazo; RF-04.03–05, RF-05.07. |
| RNG-15 | Corte y promesa | Corte y ventana se parametrizan por cliente y zona. | Comercial y operaciones. | No promete plazo universal; RF-03.13, RF-04.07. |
| RNG-16 | Descuentos | Excepción comercial se registra antes de confirmar. | Supervisor comercial. | Evita descuento sin trazabilidad; RF-03.07, RF-03.10. |

**Nota de trabajo:** Cada regla debe validarse durante el levantamiento y mantenerse configurable cuando dependa de un parámetro comercial o sanitario. Para completarlo se requiere registrar la evidencia de esa validación.

<a id="seccion-9"></a>

## Anexo 3.H — Registro de vacíos y consultas

Se separa la identificación de un vacío de su resolución. Ninguna fila acredita una respuesta recibida del CLIENTE.

La Tabla [3.A.11](#tabla-3-a-11) presenta vacíos e inconsistencias para revisión.

<a id="tabla-3-a-11"></a>

**Tabla 3.A.11 — Vacíos e inconsistencias para revisión. Fuente: contraste de Bases, SD2 y SD3.**

| **ID** | **Materia** | **Nota de trabajo: evidencia requerida** |
| --- | --- | --- |
| V-01 | Número de instalaciones: cinco en entrevista, seis en volumetría; SD2 indica 14 CD. | Confirmar universo de instalaciones; no trasladar 14 CD al diseño. |
| V-02 | La ponderación del Formulario T-21 suma 98 % aunque su total declara 100 %. | Contrastar el planteamiento original y documentar tratamiento antes de cerrar la consulta. |
| V-03 | 84 conductores y peonetas frente a 42 conductores propios en la Tabla 14.1. | Contrastar el planteamiento original y documentar tratamiento antes de cerrar la consulta. |
| V-04 | Cuatro ambientes (Art. 24 y E-25) frente a cinco más recuperación (Art. 3 y RT-04.01). | Contrastar el planteamiento original y documentar tratamiento antes de cerrar la consulta. |
| V-05 | Códigos de sincronización y otras materias del capítulo 15 no coinciden con BTT. | Usar código transversal por materia y registrar el valor particular del caso; completar cotejo por fila. |
| V-06 | Relato de cortes de 2 h frente a la exigencia de 14 h. | Contrastar el planteamiento original y documentar tratamiento antes de cerrar la consulta. |
| V-07 | Alta y recuperación de credenciales de personas sin correo. | Contrastar el planteamiento original y documentar tratamiento antes de cerrar la consulta. |
| V-08 | 41 % de recepciones del producto retirado sin lote en origen. | Contrastar el planteamiento original y documentar tratamiento antes de cerrar la consulta. |
| V-09 | No existe saldo inicial de envases por cliente. | Contrastar el planteamiento original y documentar tratamiento antes de cerrar la consulta. |
| V-10 | El Cap. 5 manda reemplazar la planilla de reposición y el catálogo inicial no tenía requerimiento. | Contrastar el planteamiento original y documentar tratamiento antes de cerrar la consulta. |
| V-11 | Faltaban la hora real de entrega y el monto esperado de rendición, sin los cuales el OTIF y la cuadratura no se calculan. | Contrastar el planteamiento original y documentar tratamiento antes de cerrar la consulta. |
| V-12 | Regla escrita de excursión térmica y responsable de la disposición. | Contrastar el planteamiento original y documentar tratamiento antes de cerrar la consulta. |
| V-13 | Inicio calendario del contrato no consolidado. | Confirmar fecha de inicio y compatibilidad de los meses 16 y 21 con congelamientos y enero de 2029. |
| V-14 | La suspensión del proveedor de lácteos vence en septiembre de 2026, antes del inicio del contrato; no está definido qué evidencia de trazabilidad acepta el proveedor. | Contrastar el planteamiento original y documentar tratamiento antes de cerrar la consulta. |
| V-15 | Disponibilidad y retiro del planificador. | Confirmar fecha; conservar talleres meses 1 a 3 del SD2, sin fijar retiro entre meses 8 y 13. |
| V-16 | Condiciones contractuales de acceso a los datos de la telemetría del tercero. | Confirmar acceso, condiciones contractuales e interfaces antes de definir la integración. |
| V-17 | Rotación de 38 % atribuida a conductores externos en SD2. | El caso atribuye ese porcentaje a preparación de pedidos; no trasladarlo a conductores. |
| V-18 | SD2 menciona 99,5 % y referencias RNF que requieren cotejo. | Definir disponibilidad por servicio contra Bases; no usar experiencia corporativa como SLA contractual. |
| V-19 | SD2 propone ventanas comerciales y corte horario. | Confirmar capacidad y condiciones de la promesa antes de convertirla en garantía de servicio. |
| V-20 | Referencias a arquitectura, EDT, pruebas e innovaciones de documentos aún no revisados. | Completar vínculos tras revisar esos documentos; mantener campos vacíos. |
| V-21 | SD2 menciona SAP Business One y Manhattan; no se adopta la marca como evidencia técnica. | Acreditar fabricante, versión e interfaces antes de diseñar integración o migración. |

<a id="seccion-10"></a>

## Anexo 3.I — Participación de los grupos de interés

Se mantienen los 19 actores del Subdocumento 2. La estrategia respaldada no sustituye la asignación pendiente de momento, responsable e indicador.

La Tabla [3.A.12](#tabla-3-a-12) presenta participación de los 19 actores consolidados.

<a id="tabla-3-a-12"></a>

**Tabla 3.A.12 — Participación de los 19 actores consolidados. Fuente: SD2, sección 2.4 y anexo 2.3.**

| **Actor** | **Participación coherente con SD2** | **Momento** | **Responsable** | **Indicador** |
| --- | --- | --- | --- | --- |
| Gerenta General | Revisar la síntesis de resultados y las tensiones de alcance. | Inicio, piloto y seguimiento | Jefe de Proyecto | Participación y adopción registradas |
| Gerente Comercial | Revisar stock visible y promesa comercial. | Inicio, piloto y seguimiento | Líder de Implantación | Participación y adopción registradas |
| Gerente de Operaciones | Revisar preparación, despacho y continuidad. | Inicio, piloto y seguimiento | Jefe de Proyecto | Participación y adopción registradas |
| Gerente de Finanzas | Revisar conciliación y costo de servir. | Inicio, piloto y seguimiento | Líder de Datos | Participación y adopción registradas |
| Jefa de Calidad | Revisar captura de lote, frío y retiro. | Inicio, piloto y seguimiento | Encargado de Seguridad | Participación y adopción registradas |
| Jefa de Bodega | Revisar FEFO y preparación en el turno nocturno. | Inicio, piloto y seguimiento | Líder de Implantación | Participación y adopción registradas |
| Jefe de TI | Validar interfaces y necesidades de soporte. | Inicio, piloto y seguimiento | Arquitecto de Solución | Participación y adopción registradas |
| Planificador de Rutas | Participar en captura de heurísticas y corrección de rutas. | Inicio, piloto y seguimiento | Líder de Implantación | Participación y adopción registradas |
| Preventistas | Revisar captura de pedidos en terreno. | Inicio, piloto y seguimiento | Líder de Implantación | Participación y adopción registradas |
| Tripulación propia | Revisar entrega digital y registro de efectivo. | Inicio, piloto y seguimiento | Líder de Implantación | Participación y adopción registradas |
| Conductores externos | Revisar incorporación y uso de la aplicación en ruta. | Inicio, piloto y seguimiento | Líder de Implantación | Participación y adopción registradas |
| Empresas transportistas | Acordar incorporación operacional de sus conductores. | Inicio, piloto y seguimiento | Jefe de Proyecto | Participación y adopción registradas |
| Preparadores | Revisar listas digitales y aprendizaje en el puesto. | Inicio, piloto y seguimiento | Líder de Implantación | Participación y adopción registradas |
| Sindicato de Choferes | Revisar tratamiento de datos de vehículo y personas. | Inicio, piloto y seguimiento | Jefe de Proyecto | Participación y adopción registradas |
| Canal Tradicional | Mantener compra y pago sin dispositivos obligatorios. | Inicio, piloto y seguimiento | Gerente Comercial | Participación y adopción registradas |
| Food Service | Revisar ventanas de atención y evidencia de entrega. | Inicio, piloto y seguimiento | Gerente Comercial | Participación y adopción registradas |
| Canal Moderno | Revisar pedido electrónico y aviso de despacho. | Inicio, piloto y seguimiento | Gerente Comercial | Participación y adopción registradas |
| Proveedores | Revisar captura de códigos y lote en recepción. | Inicio, piloto y seguimiento | Jefa de Bodega | Participación y adopción registradas |
| Autoridad Sanitaria | Disponer de evidencia de trazabilidad y temperatura. | Inicio, piloto y seguimiento | Jefa de Calidad | Participación y adopción registradas |

**Nota de trabajo:** Las actividades se detallan durante el inicio y cada ola; los indicadores se revisan en comité de proyecto. Para completarlo se requiere conservar minutas, asistencia y resultados de adopción.

<a id="seccion-11"></a>

## Anexo 3.J — Criterios de aceptación

Se conservan los resultados y situaciones actuales del capítulo 18. Las metas propias, momento y método aún deben completarse.

La Tabla [3.A.13](#tabla-3-a-13) presenta resultados de aceptación exigidos por el caso.

<a id="tabla-3-a-13"></a>

**Tabla 3.A.13 — Resultados de aceptación exigidos por el caso. Fuente: Caso, cap. 18, p. 35.**

| **ID** | **Resultado exigido** | **Situación actual** | **Meta propia** | **Momento / método** |
| --- | --- | --- | --- | --- |
| R18-01 | Ante un retiro sanitario, la lista de clientes afectados por lote se obtiene con evidencia en menos de dos horas. | 9 días, con resultado estimado. |  |  |
| R18-02 | El 100 % de las recepciones registra el lote de los productos que lo requieren. | 41 % sin registro en el producto involucrado. |  |  |
| R18-03 | Existe registro continuo y automático de temperatura en cámaras y vehículos, auditable y disponible para el cliente. | 3 lecturas manuales por viaje. |  |  |
| R18-04 | El indicador de entregas completas y a tiempo se mide de una sola forma y alcanza la meta comprometida por el PROPONENTE. | 82,4 %, medido de forma distinta por cada área. |  |  |
| R18-05 | El preventista conoce el stock disponible y el crédito del cliente en el momento de tomar el pedido. | No los conoce. |  |  |
| R18-06 | Ningún pedido se pierde ni se duplica por falta de señal. | Ocurre semanalmente, sin medición. |  |  |
| R18-07 | La ruta del día siguiente se genera automáticamente en menos de 20 minutos y el planificador puede corregirla, quedando registro de cada corrección. | 3,5 horas de una persona insustituible. |  |  |
| R18-08 | La prueba de entrega es digital y está disponible para el cliente el mismo día. | Guía en papel; 12 días para resolver un reclamo. |  |  |
| R18-09 | Cero guías extraviadas o ilegibles. | 1,1 % mensual. |  |  |
| R18-10 | La rendición del efectivo cuadra el mismo día y toda diferencia queda explicada. | $ 4,2 millones mensuales de diferencia sin investigar. |  |  |
| R18-11 | El costo de servir se conoce por cliente y por entrega, construido desde el hecho. | Prorrateo por zona con criterio de 2016. |  |  |
| R18-12 | El parque de envases retornables se controla y la pérdida anual baja bajo la meta comprometida. | 14 % de pérdida estimada, sin control. |  |  |
| R18-13 | Los pedidos de las cadenas entran por vía electrónica estructurada, sin digitación, y se responde con aviso de despacho. | Cero pedidos electrónicos. |  |  |
| R18-14 | La ocupación de los camiones sube y ningún camión sale bajo el umbral que el PROPONENTE comprometa. | 68 % promedio, con días de 41 %. |  |  |
| R18-15 | La causa de cada faltante queda registrada al momento de producirse. | Se registra el faltante, no la causa. |  |  |
| R18-16 | Don Hugo se puede jubilar sin que la operación se resienta. | El cumplimiento cae 6 a 9 puntos cuando está de vacaciones. |  |  |

**Nota de trabajo:** Los límites expresos del caso se conservan; las metas a cargo del proponente y la verificación aún están vacías. Para completarlo se requiere fijar OTIF, envases y ocupación, así como momento y protocolo de medición por resultado.

<a id="seccion-12"></a>

## Anexo 3.K — Glosario de siglas y códigos

El glosario aclara las denominaciones utilizadas en esta versión.

La Tabla [3.A.14](#tabla-3-a-14) presenta siglas utilizadas.

<a id="tabla-3-a-14"></a>

**Tabla 3.A.14 — Siglas utilizadas. Fuente: terminología de las Bases y SD2.**

| **Sigla** | **Significado** |
| --- | --- |
| RF | Requerimiento funcional; los RF-01 a RF-14 del SD2 son resúmenes, no equivalen por número a las épicas del SD3. |
| RNF | Requerimiento no funcional. |
| RT | Requisito codificado de las Bases Técnicas Transversales. |
| ERP | Sistema de gestión empresarial conservado como registro contable y emisor tributario. |
| WMS | Sistema de gestión de almacenes. |
| FEFO | Primero en vencer, primero en salir. |
| OTIF | Entregas completas y a tiempo; su regla de cómputo aún debe cerrarse. |
| POD | Prueba de entrega. |
| EDI | Intercambio electrónico estructurado de documentos. |
| RTO / RPO | Objetivos de tiempo de recuperación y pérdida de datos admisible. |

<a id="seccion-13"></a>

## Material complementario recibido: tablas_anexo

Nota de conversión: esta colección no está incluida por el archivo de anexos vigente. Se conserva separadamente, sin sustituir ni reconciliar los registros de los anexos 3.A–3.K y del T-12. Sus rótulos anuncian 91 RF y 41 RNF, pero sus filas contienen 90 RF y 40 RNF. Se preservan esas discrepancias.

<a id="seccion-14"></a>

### Material recibido: capas

Origen de esta tabla: 03_esquema_solucion_alcance/tablas_anexo/capas.tex.

<a id="tabla-3-a-15"></a>

**Tabla 3.A.15 — Las ocho capas de la plataforma y su aplicación en Puelche**

| **Capa** | **Aplicación en la distribuidora** |
| --- | --- |
| Presentación | Portal de administración en Talca y Concepción; aplicación móvil de preventa; aplicación de reparto; aplicación de recepción y picking en bodega; autoatención de clientes, transportistas y proveedores. |
| Borde y exposición | Red de distribución de contenido y cortafuegos de aplicación gestionado para el portal público y las interfaces expuestas a proveedores y cadenas, con terminación TLS 1.3. |
| Puerta de enlace de servicios | Punto único de publicación de las interfaces de pedidos, crédito, trazabilidad, entrega e intercambio con cadenas. |
| Servicios de negocio | Módulos sin estado: preventa, planificación de rutas, bodega y picking, trazabilidad y retiros, cadena de frío, entrega y prueba de entrega, cobranza y efectivo, devoluciones y envases, costeo, y reposición y compras. |
| Integración y eventos | Bus de mensajería que desacopla preventa, crédito, bodega, ruta, reparto y facturación, con colas y reintento para los dispositivos sin señal. |
| Datos | Base transaccional —pedidos, stock, trazabilidad de lote, temperatura y prueba de entrega— separada del almacén analítico que sostiene OTIF, fill rate y costo de servir. |
| Seguridad transversal | Identidad federada, cifrado en tránsito y en reposo, y cifrado a nivel de campo para datos comerciales, de pago y de geolocalización. |
| Observabilidad transversal | Métricas, registros y trazas correlacionados de Talca, Concepción, las tres plataformas de cross-docking y los dispositivos de terreno. |

<a id="seccion-15"></a>

### Material recibido: decisiones

Origen de esta tabla: 03_esquema_solucion_alcance/tablas_anexo/decisiones.tex.

<a id="tabla-3-a-16"></a>

**Tabla 3.A.16 — Registro de decisiones: decisión no tomada, decisión adoptada, justificación y requerimiento relacionado (61 filas)**

| **N°** | **Decisión no tomada** | **Por qué importa** | **Decisión Tomada** | **Justificación** | **Origen** | **Req relacionado** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Qué cuenta como entrega cumplida cuando la entrega es parcial, y cómo se mide el indicador de servicio. | Hoy cada área lo cuenta distinto y por eso nadie se pone de acuerdo sobre el estado real del servicio. | Una entrega parcial NO cuenta como entrega cumplida: para OTIF, «In-Full» exige el 100 % de ítems y unidades pedidas. El indicador de servicio se mide diario con OTIF por cliente, ruta, zona y consolidado (RF-11.03), y con Fill Rate = unidades entregadas vs. pedidas y Perfect Order contrastada contra la orden original (RF-11.04). | Los RF definen las métricas: RF-11.03 fija OTIF («On-Time» = fecha y ventana pactada; «In-Full» = 100 % de ítems y unidades) y obliga causal tipificada ante desvíos; RF-11.04 mide Fill Rate y Perfect Order con el POD móvil. Toda entrega parcial queda como desvío auditado y unifica el criterio entre áreas. | Tabla Cap 16.1 | RF-11.03 RF-11.04 |
| 2 | Cuál es la unidad de trazabilidad sanitaria: el lote del proveedor, la caja, el pallet o una unidad logística identificada individualmente. | Determina el volumen de datos, el esfuerzo en recepción y preparación, y la calidad de la respuesta ante un retiro. | La unidad de trazabilidad sanitaria es el LOTE del proveedor (AI 10), registrado obligatoriamente en la recepción (RF-01.02). El SSCC (RF-01.07) identifica la unidad logística física (pallet) y queda asociado al lote en almacenamiento y preparación, pero el retiro y las trazabilidades forward/ backward se resuelven por lote (RF-02.10, RF-09.01). | RF-01.02 obliga el lote por SKU con trazabilidad obligatoria; RF-01.07 vincula el SSCC a GTIN + lote + vencimiento; RF-02.10 y RF-09.01 consultan y rastrean por LOTE (no por caja ni SSCC). La caja/ pallet/ SSCC son unidades físicas de manipulación; la unidad de control sanitario y de memoria legal es el lote, lo que acota el volumen de datos y el esfuerzo de recepción sin perder respuesta ante un retiro. | Tabla Cap 16.1 | RF-01.02 RF-01.07 RF-02.10 RF-09.01 |
| 3 | Qué se hace cuando el local del cliente está cerrado: reintento, entrega a un tercero, devolución. Y quién decide. | Hoy decide cada conductor según su criterio. Es la causa principal de las reentregas. | Si el local está cerrado en la ventana comprometida, el conductor reporta «local cerrado» indicando la dirección; el sistema registra el envío como fallido y lo reagenda automáticamente a la ventana horaria siguiente más cercana del cliente (RF-06.04), registrada en su ficha (RF-04.07). El conductor no decide por su cuenta; si persiste la indisponibilidad, los productos regresan al almacén. | RF-06.04 automatiza la respuesta al local cerrado (registro de fallido + reagendamiento automático a la próxima ventana del cliente), eliminando el criterio individual del conductor y sistematizando las reentregas. Esta regla, más la ventana registrada por cliente (RF-04.07), reemplaza el comportamiento actual y ataca la causa principal de reentregas. | Tabla Cap 16.1 | RF-06.04 |
| 4 | Qué constituye una excursión de temperatura que invalida el producto, quién lo decide y si el sistema bloquea el despacho de forma automática. | Es la tensión declarada entre calidad y operaciones. Sin regla escrita no hay control posible. | Una excursión térmica se define por parámetros configurables de tiempo y grados según el tipo de producto (RF-09.06), definidos por la jefa de calidad. El sistema alerta en tiempo real al conductor y al equipo de calidad cuando se supera el umbral (RF-09.05). El bloqueo del despacho NO es automático: lo habilita el sistema y lo decide el conductor según el tipo de producto (RF-09.07). | RF-09.06 permite escribir la regla como parámetros (tiempo/ grados); RF-09.05 genera la alerta en cabina y plataforma; RF-09.07 deja el bloqueo del despacho al criterio del conductor, no automático. El RSA (D.S. 977/ 96) fija el piso normativo de la cadena de frío; la regla operacional específica la define Puelche con los parámetros configurables. Referencia: https:/ /www.chileatiende.gob.cl/ fichas/ 16583-autorizacion-sanitaria-para-vehiculos-de-transporte-de-alimentos. | Tabla Cap 16.1 | RF-01.11 RF-09.05 RF-09.06 RF-09.07 |
| 5 | Cómo se identifica al conductor de una empresa transportista y qué ocurre cuando el transportista lo cambia sin avisar. | Son 54 camiones y unos 160 camiones que no son trabajadores de la compañía. | Confirmación diaria obligatoria de conductor y vehículo en el portal de transportistas antes de la ventana de despacho (RF-12.21); si no se confirma, el sistema mantiene la asignación planificada como «supuesto no verificado». El conductor real se autentica en el dispositivo con OTP entregado por su jefe de flota (RF-06.08) o con PIN/ QR al iniciar la ruta (RF-14.07), quedando registrada la vinculación conductor–camión del viaje. | RF-12.21 documenta la confirmación diaria y su fallback; RF-06.08 autentica al conductor externo por OTP en ≤ 2 min sin correo corporativo; RF-14.07 exige la identificación (PIN o QR) antes de iniciar la ruta y registra qué conductor operó cada camión en cada viaje; el cambio sin aviso se resuelve porque quien llega se identifica y responde por el viaje. | Tabla Cap 16.1 | RF-06.08 RF-14.07 |
| 6 | Qué se hace con el efectivo: eliminarlo, reducirlo o controlarlo. Y quién asume el riesgo del dinero en circulación. | Involucra al 38% de la venta del canal tradicional, la seguridad de los conductores y $4,2 millones mensuales de diferencia. | Se mantiene el pago en efectivo (38 % del canal tradicional) con alternativas para reducirlo: encargo por web y pago con tarjeta/ POS móvil. El riesgo del dinero en circulación se controla y se asigna responsabilidad mediante rendición digital individual por camión (RF-07.02), causales tipificadas obligatorias de descuadre con firma digital y bloqueo del cierre si queda saldo sin justificar (RF-07.03). | RF-07.02 genera la cuadratura (monto esperado vs. recaudado) al retorno del camión; RF-07.03 obliga causal estructurada y bloquea la liquidación ante descuadre sin justificar, dejando responsable identificado con firma; RF-07.06 (POS móvil) y RF-07.10 (abonos parciales) soportan la reducción del efectivo; RF-06.05 registra el monto recaudado en ruta. | Tabla Cap 16.1 | RF-06.05 RF-07.02 RF-07.03 RF-07.06 RF-07.10 |
| 7 | Cómo se valoriza el costo de servir y qué se hace con los clientes que resulten no rentables. | Es la pregunta que el gerente de finanzas declara como su obsesión y de la que dependen decisiones comerciales. | El costo de servir se valoriza por entrega y por cliente: costos directos de transporte (combustible devengado vía GPS, peajes, tiempo de conducción y de descarga) más costos indirectos prorrateados de bodega y administración (RF-11.02, RF-04.08), incluidas devoluciones, mermas y pérdida de envases (RF-08.07, RF-08.06). Los clientes no rentables no se eliminan: se segmentan mensualmente en matriz de rentabilidad neta (margen vs. costo de servir) y se sugiere ajustar frecuencia de visita o umbral mínimo de compra (RF-11.08). | RF-11.02 define la imputación directa/ indirecta del costo de servir; RF-04.08 calcula el costo por entrega realizada; RF-08.07 integra devoluciones y mermas al costo; RF-11.08 entrega la matriz de rentabilidad neta y la simulación de impacto para gestionar clientes no rentables sin decisiones según intuición. | Tabla Cap 16.1 | RF-04.08 RF-11.02 |
| 8 | Cuál es la regla de asignación de stock cuando dos preventistas comprometen el mismo producto y no alcanza para ambos. | Determina si el stock se reserva en la toma del pedido, en la confirmación o en la preparación, y con qué consecuencias. | La reserva se hace efectiva al CONFIRMAR el pedido en el sistema de gestión (servidor central), por orden de llegada: el segundo preventista queda con quiebre parcial registrado (RF-03.03). En modo offline el stock es indicativo con antigüedad visible (RF-02.05); al sincronizar, los conflictos se resuelven por orden cronológico de registro (RF-02.05e) y las líneas sin stock disponible se marcan «sin stock» con notificación al preventista (RF-02.05d). | RF-03.03 fija la reserva en la confirmación y el quiebre del segundo confirmado; RF-02.05 define el stock disponible (físico - comprometido), el dato indicativo en offline y la resolución cronológica de conflictos; RF-05.03 asegura el registro del faltante con causa. Evita la arquitectura de reserva distribuida en la toma del pedido. | Tabla Cap 16.1 | RF-02.05 RF-03.03 RF-05.03 |
| 9 | Qué ocurre cuando el precio cambia entre la toma del pedido y el despacho. | Afecta la facturación, la relación con el cliente y la credibilidad del preventista. | Por defecto se cobra el PRECIO VIGENTE AL DESPACHO de cada línea (RF-03.11). Solo si se configura una excepción explícita por cliente o cadena, se respeta el precio de la toma del pedido (RF-03.12); sin excepción y con cambio de precio, el sistema alerta al cliente antes de o junto con la facturación (RF-03.13). | Los RF fijan como regla por defecto el precio vigente al despacho (RF-03.11) y la excepción «precio de toma de pedido» como configuración particular por cliente/ cadena (RF-03.12), con aviso al cliente (RF-03.13). La decisión previa («cobrar siempre el precio ofrecido por el preventista») contradice el por defecto del RF-03.11 y se reformula conforme al catálogo. | Tabla Cap 16.1 | RF-03.11 RF-03.12 RF-03.13 |
| 10 | Cómo se controla el parque de envases retornables: por saldo por cliente, por unidad identificada, o no se controla. | Son 68.000 canastillos y 9.400 pallets con una pérdida estimada del 14% anual. | Se controla por SALDO POR CLIENTE (cuenta corriente de envases retornables), no por unidad identificada individualmente. Cada entrega descuenta y cada devolución suma al saldo, actualizado en línea o diferido según conectividad (RF-08.03, RF-06.09). Se alerta al preventista cuando el saldo supera el umbral configurado (RF-08.04) y se reporta diariamente la pérdida por cliente, tipo y zona (RF-08.06). | RF-08.03 define la cuenta corriente por cliente como mecanismo de control (viable para 68.000 canastillos; el control por unidad identificada sería inviable y desproporcionado); RF-06.09 captura devoluciones por tipo y estado; RF-08.04 y RF-08.06 atacan la pérdida del 14 % anual con alertas y reporte de recuperación. | Tabla Cap 16.1 | RF-06.09 RF-08.03 RF-08.04 RF-08.06 |
| 11 | Qué maestro de productos manda cuando el proveedor cambia el formato, el contenido o el código de un producto. | Con 180 proveedores y 8.400 productos, ocurre todas las semanas y hoy se resuelve caso a caso. | Prevalece el maestro interno de Puelche: la ficha de producto es la única fuente autorizada (RF-01.10) y conserva historial de cambios de GTIN/ SKU. Todo código externo (proveedor o cadena) se resuelve contra el maestro mediante una tabla de equivalencias por cadena (RF-12.03); lo no resuelto queda en bandeja de excepciones (RF-12.06). | RF-01.10 exige la ficha con atributos obligatorios e historial de cambios de código; RF-12.03 resuelve códigos externos con equivalencias; RF-12.06 gestiona los casos no resueltos en bandeja. Así el cambio de formato/ código del proveedor no altera el maestro interno y queda trazado con fecha y usuario. | Tabla Cap 16.1 | RF-01.04 RF-01.10 RF-12.03 RF-12.06 |
| 12 | Cómo se procesa una devolución en el momento de la entrega y qué efecto tiene sobre un documento tributario ya emitido. | Tiene consecuencias tributarias y contables que la solución no puede improvisar. | La devolución se registra en el POD al momento de la entrega, total o parcial, con SKU, cantidad y motivo desde catálogo (RF-06.03), operando offline (RF-08.01). Al retorno, el destino del producto devuelto (reingreso a stock, venta con descuento, devolución al proveedor o destrucción) se decide en el andén y se transmite al ERP (RF-08.02). El efecto sobre el documento tributario ya emitido se resuelve con nota de crédito emitida por el ERP (que no se reemplaza) por la cantidad rechazada, articulada con el registro de rechazo (RNF-08.02). | RF-06.03 genera la solicitud de rechazo estructurada en la entrega; RF-08.01 la soporta sin señal; RF-08.02 gestiona el destino y la transacción al ERP; RNF-08.02 confirma la retención mínima de 6 años de las notas de crédito asociadas. El sistema registra la evidencia y finanzas ejecuta la nota de crédito sobre la GDE. | Tabla Cap 16.1 | RF-06.03 RF-08.01 |
| 13 | Cómo se resuelve la objeción sindical a las cámaras en cabina y al control de jornada por posicionamiento satelital. | Determina qué tecnologías pueden proponerse y con qué plan de gestión del cambio. | No se proponen cámaras en cabina. El control de jornada y de tiempos de conducción/ descanso mediante GPS se implementa solo con acuerdo sindical, protegiendo la privacidad de los datos del conductor (RF-14.05); la telemetría se limita a datos del vehículo y la ruta: posición, velocidad y kilometraje (RF-14.01), alerta de desviación &gt; 3 km (RF-14.04) y geocercas para tiempos de llegada/ salida (RF-14.08). El plan de gestión del cambio con el sindicato inicia en la Etapa 1. | La objeción sindical (Restricción N° 10) queda atendida porque RF-14.05 condiciona el uso del GPS para jornada al acuerdo sindical y a la privacidad; los demás RF de telemetría usan datos del vehículo y la ruta, no del conductor, y RF-14.02 extiende la visibilidad a transportistas externos solo por acuerdo operativo. | Tabla Cap 16.1 | RF-14.01 RF-14.02 RF-14.04 RF-14.08 |
| 14 | Qué se hace con el sistema de gestión de almacenes de 2013: mantenerlo, extenderlo a los demás sitios o reemplazarlo. | Es la decisión de alcance más costosa del caso y el CLIENTE la delega expresamente en el PROPONENTE. | Reemplazarlo. La Épica 2 exige capacidades que el WMS de 2013 no provee: topología multi-sitio configurable (RF-02.01), consolidación multi-nodo (RF-02.02), slotting ABC (RF-02.03), conteo cíclico ciego (RF-02.04) y picking FEFO dirigido (RF-02.08), además de operación offline de 24 h (RNF-02.01). La decisión la delega el CLIENTE (Cap. 16.1) y sustenta la propuesta con plan de migración de datos históricos y plan de reversión. | Los RF-02.xx exigen funcionalidades modernas de gestión de almacén que el sistema de 2013 no contempla y que son necesarias para cumplir los criterios de aceptación; el CLIENTE delega expresamente la decisión. Implica planificar la migración (RT-05.11/ RT-05.14), la estrategia de despliegue azul-verde y el plan de reversión. | Tabla Cap 16.1 | RF-02.01 RF-02.02 RF-02.03 RF-02.04 RF-02.08 |
| 15 | Cómo se prueba la entrega cuando quien recibe no es el titular, no sabe firmar en pantalla o se niega a hacerlo. | Afecta la validez de la evidencia y su articulación con el acuse de recibo tributario. | La prueba de entrega es la firma en pantalla del titular (RF-06.02). Cuando quien recibe no es el titular, no sabe firmar o se niega, se captura una alternativa válida vinculada a la GDE: fotografía de la mercadería + nombre del receptor en texto (RF-06.12) o código QR de confirmación si el cliente tiene smartphone (RF-06.11); el comprobante térmico portátil respalda al canal tradicional (RF-06.13). | RF-06.02 aporta la firma digital; RF-06.12 formaliza la alternativa sin firma operando sin conectividad; RF-06.11 resuelve el receptor con smartphone; RF-06.13 (impresora térmica Bluetooth) complementa el respaldo físico. Se articula con el acuse de recibo digital y tributario (RF-12.12, RF-12.13). | Tabla Cap 16.1 | RF-06.02 RF-06.11 RF-06.13 |
| 16 | Qué se hace con el conocimiento de rutas que hoy reside en una sola persona, antes de que se jubile. | Es un riesgo de continuidad operacional con fecha conocida. | El conocimiento de rutas se codifica antes de la jubilación y se transfiere al motor de ruteo: sesiones de transferencia del planificador + parametrización de sus reglas (zonas logísticas, capacidades, ventanas horarias) en la asignación y secuenciación automática (RF-04.01), conservando la modificación manual y el recálculo de ETA (RF-04.02, RF-04.04). La captura se ejecuta en la Etapa 1 para que el motor quede operativo antes de la fecha de salida. | RF-04.01 materializa el conocimiento tácito en el motor automático de rutas (asignación/ secuenciación por capacidad y zonas); RF-04.02/ RF-04.04 preservan la flexibilidad de ajuste y el respeto de ventanas; RF-05.07 liga la ruta a la carga dirigida. Mitiga el riesgo de continuidad operacional con fecha conocida (BTC 13.1, 17.3). | Tabla Cap 16.1 | RF-04.01 RF-04.02 RF-04.04 RF-05.07 |
| 17 | Asignar componentes a la nube o utilizar infraestructura on-premise. | La solución debe ser obligatoriamente híbrida y se debe justificar la asignación de cada componente. | On-premise: el componente de gestión de almacén y el borde operacional (CD) por operación offline de 24 h (RNF-02.01) y latencia de confirmación de picking ≤ 1 s incluyendo la cámara de congelado (RNF-05.01). Nube pública: analítica/ BI, tableros, portales público y de autoatención, EDI del canal moderno y servicios elásticos. La tabla de emplazamiento por componente se entrega y justifica como entregable (RF-13.02, RT-03.01). | RNF-02.01 obliga la operación autónoma del CD por 24 h sin enlace (almacén on-premise); RNF-05.01 exige ≤ 1 s en el dispositivo de congelado (borde/ on-premise); el criterio de emplazamiento RT-03.01/ Cap. 3.1 (latencia, criticidad, volumen, regulación, elasticidad) asigna el resto a la nube. La solución cumple la modalidad híbrida obligatoria (BA Art. 16.2). | Cap 3.1 Bases Técnicas | RNF-02.01 RNF-05.01 |
| 18 | Selección del motor de bases de datos a utilizar. | La solución debe sostener escritura transaccional local durante 24 horas sin enlace en cada centro de distribución y, a la vez, consultas geográficas para el ruteo y series de temperatura con retención de 5 años. Elegir mal el paradigma obliga a rediseñar la capa de datos o a operar motores que un área de cuatro personas no puede mantener; el transversal además exige justificar expresamente la posición ante el teorema CAP. | Motor relacional transaccional (p. ej., PostgreSQL) para los dominios de pedidos, inventario, trazabilidad y facturación, con consistencia inmediata (ACID) exigida por la operación offline y la reconciliación determinista; más un motor analítico separado (columnar) para BI y el tablero en tiempo real (RF-11.06), desacoplado del transaccional para no degradar picking y preventa (RNF-11.02). | RT-05.02 exige declarar el paradigma y motor por dominio con su posición en el teorema CAP. La criticidad transaccional y la operación desconectada (RNF-02.01) justifican un motor relacional ACID; RF-11.06 y RNF-11.02 separan el procesamiento analítico (OLAP) del OLTP. | RT-05.02 Bases Técnicas | RF-11.06 |
| 19 | Declaración si la aplicación será nativa, híbrida o web progresiva. | Define si el terminal puede operar un turno completo de 14 horas sin señal y si accede a los periféricos que la operación exige: escáner de códigos, impresora térmica de cabina, cámara, posicionamiento y terminal de pago. Determina también si se puede usar con guantes térmicos a menos 22 grados, a una sola mano durante la descarga y con pantalla legible bajo sol directo. Es la decisión que define si el reparto y la preventa pueden trabajar donde efectivamente trabajan. | NATIVA para los perfiles de terreno (preventista, reparto, preparación/ recepción de bodega) por: consulta de stock sin conectividad (RF-03.02), acceso a periféricos (escáner GS1, impresora térmica Bluetooth RF-06.13, cámara, GPS, balanza), operabilidad con guantes a -22 °C (RNF-05.02), persistencia de un turno completo sin señal (RNF-06.01) y curva de aprendizaje ≤ 2 h (RNF-05.03). La autoatención del cliente se resuelve con aplicación web (portal/ PWA). | RT-07.01 exige declarar el tipo de aplicación. Los RNF del caso (offline 14 h, guantes, periféricos, cámara de -22 °C) exigen acceso nativo al dispositivo, no alcanzable de forma robusta con PWA/ híbrida; se asume como trade-off el costo de mantención de las plataformas nativas de terreno. | RT-07.01 Bases técnicas | RF-03.02 RNF-05.02 RNF-05.03 |
| 20 | Cómo se reparte el alcance entre Etapa 1 y Etapa 2, respetando las fechas críticas del contrato (canal moderno antes de enero 2029) y el riesgo de salida del planificador de rutas. | El comité ejecutivo sugirió un orden, pero es una preferencia, no una definición de alcance; la salida del planificador es un riesgo con fecha conocida. | La Etapa 1 prioriza trazabilidad y cadena de frío, abastecimiento/ recepción, gestión de almacén e inventario, y la captura temprana del conocimiento del planificador en el motor de ruteo (RF-04.01); la Etapa 2 incorpora canal moderno (EDI + portal), analítica/ costo de servir y el resto del ruteo. El canal moderno queda en producción antes de enero de 2029 (RNF-12.01). | RNF-12.01 fija la fecha límite del canal moderno en enero de 2029; la Etapa 1 se alinea con la urgencia que el caso declara (trazabilidad/ frío primero) y con la captura del conocimiento de rutas antes de la jubilación; la trazabilidad (RF-02.10, RF-09.01) y el ruteo (RF-04.01) son el núcleo urgente de la Etapa 1. | Cap 16.1, BTC 13.1, 17.3 | RNF-12.01 RF-04.01 RF-09.01 RF-02.10 |
| 21 | Metas concretas para los 16 resultados de negocio del Capítulo 18 (el caso entrega el diagnóstico actual, no el compromiso). | Fijar el nivel comprometido es trabajo del proponente y define los umbrales de las marchas blancas y del servicio. | Se comprometen metas con curva de mejoramiento gradual, no un valor plano desde el mes 1: OTIF 90 % al cierre de la Etapa 1 → 93 % al mes 12 → 95 % en régimen estable (RF-11.03, base de cálculo explícita = caja/ SKU/ orden y ventana horaria definida); Fill Rate ≥ 97 % (RF-11.04); ocupación de flota ≥ 75 % con alerta bajo 65 % (RF-11.05); reentregas ≤ 1 % de las entregas del mes; pérdida de envases ≤ 7 % anual (RF-08.06); listado de clientes afectados por lote en &lt; 2 h (RNF-09.01). | El benchmark de la industria muestra que el OTIF parte bajo y mejora con el tiempo: Walmart abrió en 75 % y los principales CPG estaban en 10–36 % al lanzarse el KPI; el rango "bueno" actual es 90–95 % (retail) y 88–94 % (cadena de frío). La curva gradual hace el compromiso alcanzable y auditable (RT-20.04 por ola), cada escalón anclado en los RF de medición (RF-11.03/ 11.04) con latencia diaria (RNF-11.01). | Cap 18, BTC Cap. 18 | RF-11.03 RF-11.04 RF-11.05 RF-08.06 RNF-09.01 RNF-11.01 |
| 22 | Qué ventana de entrega puede prometer el preventista y a qué hora corta la toma de pedidos del turno. | Define la duración del día logístico, qué se puede comprometer al cliente y cuándo se dispara la preparación. | El preventista muestra la «ventana de entrega comprometible» (RF-03.14) calculada desde la ficha del cliente (RF-04.07) y el plan de transporte; la llegada se planifica dentro de esa ventana de 30 minutos (RF-12.10) y el ETA se avisa al cliente (RF-04.06). La hora de corte del turno es parametrizable por zona comercial: al cierre se dispara la generación automática de misiones de picking (RF-05.01) y todo pedido posterior entra al ciclo siguiente. | RF-03.14 obliga a informar la ventana comprometible; RF-04.07 y RF-12.10 garantizan que el ruteo respete la ventana pactada; RF-04.06 avisa el ETA; RF-05.01 ata la generación de misiones al cierre de pedidos del turno, que es la base de la hora de corte. | Cap 9.1, 9.9 | RF-03.14 RF-04.07 RF-12.10 RF-04.06 RF-05.01 |
| 23 | Qué reemplaza la planilla manual de «sugerencia de reposición» del preventista (Cap. 9.10). | El catálogo de requerimientos no contiene un RF dedicado; dejarlo sin resolver es un vacío que debe declararse (BTC 17.1). | Se declara el vacío y se resuelve sin requerimiento nuevo a medida: la app de preventa genera la sugerencia de reposición desde el historial de compra, frecuencia y promociones vigentes (RF-03.15), y el preventista registra en la misma visita mermas por vencimiento en góndola (RF-08.05). El reemplazo de la planilla queda cubierto por la funcionalidad de preventa móvil. | RF-03.15 genera sugerencias al preventista por historial/ frecuencia/ promociones (la base funcional de la reposición); RF-08.05 permite registrar mermas detectadas en la góndola del cliente; al no existir RF específico, el vacío se eleva en el registro de vacíos citando Cap. 9.10 y Cap. 5. | Cap 9.10, Cap 5 | RF-03.15 RF-08.05 |
| 24 | Si la observación de góndola que hace el preventista se registra en el sistema y con qué profundidad. | Es información que hoy se pierde; no se deben fotografiar góndolas (evita datos personales e imágenes sin utilidad operacional). | Se registra de forma estructurada y liviana en la app de preventa: merma por vencimiento en góndola con SKU y lote (RF-08.05) y alertas por exceso de envases retornables (RF-08.04). No se capturan fotografías de góndolas ni datos sensibles; la alerta de envases llega al preventista en ≤ 24 h de superado el umbral. | RF-08.05 cubre el registro en góndola (SKU + lote); RF-08.04 alerta por saldo de envases; ambos son operables desde el dispositivo del preventista en modo desconectado, sin crear nuevas categorías de datos sensibles (RNF-16.03, RNF-14.01). | Cap 9.10, Cap 8 | RF-08.05 RF-08.04 |
| 25 | Cómo se captura y se comunica el dato dentro de la cámara de congelado (-22 °C, sin señal), donde los dispositivos convencionales fallan. | Es condición para el picking dentro del congelado; hoy las cámaras de frío no tienen señal. | Terminales resistentes aptos para -22 °C con interfaz operable con guantes térmicos (RNF-05.02), sin gestos complejos, con confirmación de picking ≤ 1 s dentro de la cámara (RNF-05.01), almacenamiento local del turno completo y sincronización del 100 % al reconectar (RNF-09.04); la cobertura inalámbrica dentro de las cámaras se resuelve mediante el estudio de cobertura obligatorio que las incluye (RNF-13.09). | RNF-05.01 exige ≤ 1 s también dentro de la cámara; RNF-05.02 exige operabilidad con guantes térmicos; RNF-09.04 exige persistencia y sincronización del 100 %; RNF-13.09 obliga el estudio de cobertura Wi-Fi en cámaras de refrigerado y congelado con solución técnica propuesta. El bloqueo de despacho tras una excursión no es automático: monitorear ≠ decidir (HACCP/ GDP exige decisión documentada); el sistema alerta y habilita, pero la disposición final (liberar/ bloquear/ rechazar) la adopta la autoridad de calidad de Puelche con reglas pre-acordadas por tipo de producto. | BTC 17.4.4, Cap 8 | RNF-05.01 RNF-05.02 RNF-09.04 RNF-13.09 |
| 26 | Redundancia del enlace de comunicaciones de cada sitio on-premise con la nube. | Concepción hoy no tiene respaldo y Los Ángeles pierde señal justo en su ventana de operación; el CD debe aguantar un corte de enlace. | Todo sitio on-premise contará con enlace redundante con caminos físicos y proveedores distintos, con conmutación automática ≤ 5 min (RNF-13.07). La redundancia de enlace se complementa con la operación autónoma degradada de 24 h (RNF-13.01) para el caso de pérdida total y con el dimensionamiento de ancho de banda por sitio (RNF-13.08). | RNF-13.07 exige enlace redundante con vías y proveedores distintos y conmutación ≤ 5 min; RNF-13.01 garantiza la operación local de 24 h sin enlace; RNF-13.08 exige dimensionar el ancho de banda en régimen y peak, base para dimensionar ambos enlaces. | Cap 6, RT-03.17 | RNF-13.07 RNF-13.01 RNF-13.08 |
| 27 | Modalidad del sitio secundario de recuperación ante desastres y objetivos RTO/ RPO del respaldo. | Define el costo y la complejidad de la continuidad; el caso exige sitio secundario con RTO y RPO declarados. | Sitio secundario activo-pasivo en la nube, en región distinta, con RTO ≤ 4 h y RPO ≤ 15 min para los servicios críticos (RNF-20.06) y pruebas de conmutación al menos 2 veces al año; respaldo 3-2-1-1-0 (RNF-20.07) con pruebas mensuales de restauración. | RNF-20.06 fija los objetivos y la cadencia de pruebas; el volumen transaccional del caso no justifica activo-activo (costo y complejidad de reconciliación), decisión que se documenta frente a la alternativa (RT-07.01); RNF-20.07 fija la política de respaldo. | RNF-20.06, RT-07.01 | RNF-20.06 RNF-20.07 |
| 28 | Nivel RAID y redundancia del almacenamiento on-premise. | El caso exige declarar y justificar el nivel RAID frente a alternativas y tolerar la falla de al menos un disco. | Equipos críticos on-premise redundantes (RNF-13.03) y almacenamiento que tolere la falla de al menos un disco (RNF-13.04): RAID 6 para datos e inventario de bodega y RAID 10 para los servicios transaccionales, con paridad y hot-spare, declarado y justificado frente a alternativas (RNF-13.05). | RNF-13.03 exige redundancia de equipos críticos; RNF-13.04 exige tolerancia a falla de al menos un disco; RNF-13.05 obliga a declarar el nivel RAID y justificarlo frente a alternativas (RT-03.14). | RT-03.14 | RNF-13.03 RNF-13.04 RNF-13.05 |
| 29 | Emplazamiento físico (tipología de recinto) de cada uno de los seis sitios, dado que la sala actual de Talca (25 m<sup>2</sup>) no cumple el estándar. | Determina la inversión en obra civil y dónde reside el respaldo on-premise. | Talca mantiene la sala técnica principal sobre su unidad de almacenamiento; se habilita una sala secundaria en otro recinto para el respaldo on-premise; Concepción y las tres plataformas de cross-docking usan gabinetes de borde industrializados, al igual que el borde operacional del CD. La tipología por sitio, junto con la adecuación física de la sala actual, se entrega como parte del padrón de emplazamiento (RT-06.01, Cap. 6.1). | RT-06.01/ Cap. 6.1 define la tipología sala principal–sala secundaria–gabinete de borde y exige declararla por sitio; la sala actual no cumple el estándar, por lo que se planifica su adecuación; la redundancia de equipos (RNF-13.03) y el DR (RNF-20.06) condicionan la sala secundaria. | Cap 6.1, RT-06.01 | RT-06.01 RNF-13.03 |
| 30 | Qué componente se satura primero al absorber el peak de septiembre (casi el doble de volumen) y cómo se diseña para eso. | Es obligatorio identificar el cuello de botella y su estrategia de resolución (RT-09.05). | El cuello de botella del peak de septiembre se identifica en la confirmación/ persistencia transaccional de pedidos y en la ingesta de telemetría de la flota; se resuelve con escalamiento horizontal automático de las capas de aplicación e integración (RNF-19.02), con el punto de saturación declarado y monitoreado (RNF-19.03) y validado con pruebas de carga de 1,5× peak y de estrés hasta el punto de quiebre (RNF-19.04). | RNF-19.01 exige el cálculo de capacidad con los supuestos de usuarios concurrentes y TPS del caso; RNF-19.02 exige escalamiento horizontal automático; RNF-19.03 exige identificar y resolver el cuello de botella; RNF-19.04 fija las pruebas de carga 1,5× peak y las de estrés. | Cap 17.4.13 (BTC), Cap 14.2 | RNF-19.01 RNF-19.02 RNF-19.03 RNF-19.04 |
| 31 | Qué funciones no estarán disponibles en modo desconectado y qué procedimiento manual las suple (CD y terreno). | Declararlo es obligatorio (RT-03.13); omitirlo se evalúa como observación grave. | En el CD ante corte de 24 h (RNF-02.01) no está disponible la consolidación multi-sitio en línea (RF-02.02); se suple con reporte local de stock y procedimiento manual. En terreno (14 h sin señal) no están disponibles la autorización de excepción de crédito por supervisor (RF-03.10) y la confirmación en línea del stock consolidado; el preventista usa stock indicativo local (RF-02.05) y la excepción queda aprobada-diferida al sincronizar, con respaldo presencial de llamada al supervisor. | RNF-13.02 obliga a declarar la lista y su procedimiento suplente; el detalle se apoya en los RF que soportan offline (RF-02.05, RF-06.12 POD) frente a los que dependen de red (RF-02.02, RF-03.10). La declaración se entrega con el RNF-13.02 y se valida en las pruebas de resiliencia (RNF-20.04). | RT-03.13 | RNF-13.02 RNF-02.01 RF-02.05 RF-03.10 |
| 32 | Estrategia de migración de datos históricos, con el sistema de gestión de 2017 que no se reemplaza. | La tabla RT-05.15 define volúmenes por dominio; la convivencia con el ERP/ GDE obliga a definir qué se migra y qué se conserva en origen. | Migración por dominio en ventanas sin operación, con reglas de transformación, criterios de calidad y plan de reversión (RT-05.11 a RT-05.14): maestros completos; ventas y pedidos 3 años; inventario 2 años; trazabilidad sanitaria 5 años; cuentas por cobrar en estado abierto. Se conservan como piso legal 5 años de trazabilidad y 6 años de documentos tributarios (RNF-01.02, RNF-08.02, RNF-09.02); el ERP/ GDE se mantiene como fuente de los documentos durante la cohabitación, con capa anticorrupción (RT-05.20). | RT-05.11 a RT-05.14 exigen plan de migración (alcance, transformación, calidad, ejecución, reversión) y RT-05.15 fija los volúmenes por dominio del Caso 02; los RNF de retención (RNF-01.02, RNF-08.02, RNF-09.02) determinan el piso legal de los datos que se transfieren o se conservan en origen. | RT-05.11 a RT-05.15 | RT-05.11 RT-05.12 RT-05.13 RT-05.14 RT-05.15 RNF-01.02 RNF-08.02 RNF-09.02 |
| 33 | Modelo de mesa de ayuda y soporte en terreno, en horarios y en sitios alejados (Curicó, Chillán, Los Ángeles). | La operación ocurre de noche y de madrugada; los sitios alejados no pueden quedar sin soporte. | Centro de atención con horario mínimo 08:00–20:00 ampliado a 24×7 para incidentes críticos y para la ventana de despacho 05:30–07:00 (RNF-21.04), con 80 % de las llamadas atendidas en 20 s y 70 % de resolución al primer contacto (RNF-21.03). La dotación se dimensiona con fundamento en Erlang C (RNF-21.05) según el volumen de contactos del caso; canal único con ticket y seguimiento (RNF-21.06) y traslado de especialistas de niveles 2–3 a los sitios alejados cuando se requiera (RNF-21.07). | RNF-21.04 fija el horario y la cobertura de la ventana de despacho; RNF-21.03 fija los umbrales de atención; RNF-21.05 exige el fundamento cuantitativo del dimensionamiento (Erlang C); RNF-21.06 exige el canal único con ticket; RNF-21.07 cubre los sitios alejados con traslado incluido en la oferta. | RNF-21, Cap 17 | RNF-21.04 RNF-21.03 RNF-21.05 RNF-21.06 RNF-21.07 |
| 34 | Cómo se registran y recuperan credenciales las personas usuarias externas sin correo corporativo (conductores de transportistas, canal tradicional, proveedores). | El alta de portal del catálogo (RF-12.25 a RF-12.27) asume correo; los conductores rotan sin aviso y el canal tradicional no usa correo. | Identidad centralizada con SSO y directorio (RF-15.01, RF-15.02); el alta y autoservicio del canal moderno usa el flujo por correo (RF-12.25/ 26/ 27). Para los usuarios sin correo (conductores y personal de terreno) la cuenta se crea y se recupera con factor presencial —OTP emitido por el jefe de flota (RF-06.08) y credencial inicial entregada en la sesión de dotación— sin depender del correo. Todo acceso externo y privilegiado exige MFA (RF-15.03). | RF-15.01/ RF-15.02 dan la identidad centralizada; RF-15.03 exige MFA para el acceso externo; RF-12.25 a RF-12.27 cubren el canal moderno; RF-06.08 autentica al conductor externo con OTP en ≤ 2 min sin correo corporativo, mecanismo reutilizable para el registro y la recuperación previstos en RT-12.12. | RT-12.12, BTC 15 | RF-15.01 RF-15.02 RF-15.03 RF-12.25 RF-12.26 RF-12.27 RF-06.08 |
| 35 | Modelo de datos de la trazabilidad (eventos vs. estados) y su estándar de intercambio. | La trazabilidad forward/ backward con retiro &lt; 2 h depende de cómo se modelan, registran y conservan los eventos. | La trazabilidad se modela por LOTES con eventos de negocio (recepción RF-01.02, almacenamiento, asignación en picking RF-09.09, carga RF-05.07, entrega POD) bajo el patrón eventos–datos del estándar GS1 EPCIS, vinculando cada evento al lote (AI 10) y a la unidad logística SSCC (RF-01.07). La consulta de clientes afectados (RF-09.01/ RF-09.02) se resuelve sobre este registro con respuesta ≤ 2 h (RNF-09.01) y retención de vida útil + 6 meses con piso de 5 años (RNF-09.02). | Los RF fijan los puntos de captura del lote (RF-01.02, RF-09.09, RF-05.07) y las consultas forward/ backward (RF-09.01/ 09.02); EPCIS es el estándar GS1 que el caso invoca (BTC 16.2); RNF-09.01/ 09.02 fijan el desempeño y la retención. El modelo se declara en el diccionario de datos (RT-05.01). | Cap 4.9, 9.5, 9.6 | RF-01.02 RF-01.07 RF-09.09 RF-05.07 RF-09.01 RF-09.02 RNF-09.01 RNF-09.02 |
| 36 | Estrategia de puesta en producción por oleadas y criterios de avance y cierre de cada marcha blanca. | Un paso único afectaría simultáneamente bodega, preventa, reparto y facturación; el caso exige oleadas con umbrales. | Puesta en producción por oleadas por sitio y zona comercial: 1) bodega (recepción, inventario, picking); 2) preventa móvil por zona; 3) reparto/ POD por empresa transportista; 4) facturación e integración con ERP/ GDE. El avance entre oleadas exige cumplir los indicadores de la marcha blanca (OTIF y Fill Rate, RF-11.03/ RF-11.04) y la certificación de administradores y técnicos (RNF-22.04); la capacitación se programa sin detener la operación (RNF-22.03) y la bodega arranca cuando se cumple la curva de aprendizaje de ≤ 2 h (RNF-05.03). | RT-20.02 exige oleadas y RT-20.04 los umbrales diarios de cierre; RF-11.03/ RF-11.04 instrumentan los indicadores de avance; RNF-22.04 condiciona el cierre a la certificación; RNF-22.03 y RNF-05.03 ordenan la capacitación y el arranque de bodega sin afectar la operación. | RT-20.02, RT-20.04, BTC 17.6.1 | RF-11.03 RF-11.04 RNF-22.04 RNF-22.03 RNF-05.03 |
| 37 | Cómo se prepara la solución para un eventual nuevo centro de distribución en la Región de Los Lagos (2030), sin rediseño. | El caso exige multi-tenencia o parametrización para replicar la solución (RT-02.12). | La solución se diseña con topología de instalaciones configurable (RF-02.01) y consolidación de stock multi-sitio (RF-02.02): un nuevo CD de Los Lagos se incorpora por configuración (zonas, pasillos, posiciones, nodo de la red) sin desarrollo a medida, reutilizando las reglas de ruteo, preventa y reparto ya parametrizadas. | RF-02.01 exige registrar y configurar cada instalación de la red (CD y cross-docks) con su topología interna; RF-02.02 consolida el stock de todos los nodos; RT-02.12 exige multi-tenencia o parametrización para replicar la solución sin rediseño. | RT-02.12, BTC 15 | RF-02.01 RF-02.02 |
| 38 | Cómo se articula la evidencia del POD con la guía de despacho electrónica (GDE) y su acuse de recibo, cuando el receptor no tiene firma electrónica avanzada. | La articulación tributaria es obligatoria (RT-16.14) y el receptor habitual es persona natural sin firma avanzada. | La evidencia capturada en la entrega (firma en pantalla RF-06.02, QR RF-06.11 o fotografía + nombre en offline RF-06.12) queda vinculada a la GDE y a su acuse de recibo digital/ tributario (RF-12.12, RF-12.13); el acuse se envía al cliente del canal moderno dentro de los 30 minutos de la descarga (RF-12.13). La firma electrónica avanzada (RF-18.01, Ley 19.799) se reserva a los actos que el caso exige, sin exigírsela al receptor tradicional. | RF-06.02/ 11/ 12 ofrecen la evidencia según el perfil del receptor (con o sin smartphone, con o sin conectividad); RF-12.12/ 12.13 articulan el POD con la GDE y el acuse digital; RF-18.01 y RT-16.14 fijan el alcance legal de la firma electrónica cuando el receptor es persona natural. | RT-16.14, Cap 9.9 | RF-06.02 RF-06.11 RF-06.12 RF-12.12 RF-12.13 RF-18.01 |
| 39 | Alcance del monitoreo continuo (nivel de servicio y cobertura horaria), respondiendo si «es necesario un monitoreo constante». | La operación nocturna y la ventana de despacho sin plan B hacen del monitoreo 24×7 una condición de continuidad. | Monitoreo 24×7×365 (NOC, RNF-21.01) con observabilidad unificada de nube y on-premise (RF-16.01) y alertamiento por síntomas de negocio —OTIF bajo, pedidos no preparados— y no solo por umbrales de infraestructura (RF-16.03), con turnos de disponibilidad declarados. Sí es necesario: la preparación ocurre de noche y la ventana de despacho (05:30–07:00) no tiene plan B manual (Restricción N° 1). El objeto de este monitoreo es la plataforma, la infraestructura y los indicadores de operación/ negocio (sistemas, bodega, OTIF, cadena de frío), NO el conductor: no se incorporan cámaras en cabina ni uso del GPS para control de jornada, que se rigen exclusivamente por la Decisión 13 y el acuerdo sindical (RF-14.05). La telemetría se limita a datos del vehículo y la ruta (RF-14.01/ 03/ 06/ 09); por tanto no topa con la Restricción N° 10. | RNF-21.01 exige NOC 24×7×365; RF-16.01 instrumenta la observabilidad unificada; RF-16.03 exige alertas por síntomas de negocio con escalamiento automático y turnos declarados; RNF-21.04 cubre la ventana de despacho. Sin monitoreo nocturno, un corte en bodega permanecería sin detectar hasta la mañana. La distinción frente a la Restricción N° 10 es de objeto: aquí se monitorea el sistema y la operación (RF-16 series/ RNF-21), mientras que el control del conductor por GPS solo procede vía RF-14.05 con acuerdo sindical (Decisión 13); los RF-14 que integran el monitoreo vehicular usan datos del vehículo y la ruta, no de la jornada del conductor. | Cap 17, RNF-21.01 | RNF-21.01 RF-16.01 RF-16.03 RNF-21.04 RF-14.05 RF-14.01 |
| 40 | Cómo se controlan los descuentos y promociones en terreno (conductor/ preventista), ante la diferencia reportada de $4,2 millones mensuales (Cap. 4.7). | Sin regla, el «descuento de buena fe» queda sin registro y el descuadre de caja se perpetúa. | El conductor no aplica descuentos libres en la entrega: solo se aplican promociones vigentes del catálogo (RF-03.07). Toda diferencia de recaudación se explica con causal tipificada dentro de RF-07.03 (descuento comercial autorizado, diferencia de cambio, siniestro en ruta), bloqueando el cierre de la liquidación si queda saldo sin justificar; el caso excepcional que requiere autorización se resuelve con aprobación registrada de supervisor (RF-03.10). | RF-07.03 obliga al registro de causales de descuadre (incluido «descuentos comerciales autorizados») con firma digital y bloqueo del cierre; RF-03.07 limita la aplicación de promociones a las vigentes; RF-03.10 permite la autorización excepcional registrada. Con esto los $4,2 M mensuales se vuelven trazables y auditables. | Cap 4.7, Cap 9.7 | RF-03.07 RF-07.03 RF-03.10 |
| 41 | Dónde viven, cómo rotan y quién custodia los secretos de integración: credenciales del sistema de gestión de 2017, certificados de mensajería electrónica de cada cadena, credenciales de la autoridad tributaria y de la pasarela de pago, y las credenciales de servicio entre módulos. | El Artículo 21.4 prohíbe de forma absoluta las credenciales embebidas en código, imágenes o configuración, y exige un gestor con rotación automática. Un gestor autoalojado agrega una máquina que hay que sellar y desellar a mano, y el área de tecnologías de información del CLIENTE son cuatro personas. | AWS Secrets Manager para los secretos con rotación y SSM Parameter Store para la configuración no sensible, consumidos de forma SALIENTE desde los nodos on-premise por VPC Endpoint. Se descarta HashiCorp Vault autoalojado. La credencial de la cuenta de emergencia queda deliberadamente FUERA DE LÍNEA, en sobre sellado con doble firma en el recinto de custodia de la sala. | Vault exigía una máquina virtual con alta disponibilidad, respaldo, licencia y un procedimiento de desellado manual que puede requerirse de madrugada, en una operación cuya ventana crítica es 05:30–07:00 con indisponibilidad cero comprometida. Además, tal como estaba declarado no tenía emplazamiento físico en ninguna vista, lo que incumple el Artículo 16.2. El servicio administrado cumple el 21.4 sin agregar infraestructura y no rompe Zero Trust porque el consumo es saliente. La cuenta de emergencia va fuera de línea justamente porque es la única credencial que debe seguir siendo utilizable cuando no hay ni identidad ni enlace. | Art. 21.4; Art. 16.2 y 16.3 | RT-04.09 RT-11.09 RT-03.15 RT-12.13 |
| 42 | Qué componente cumple el rol de puerta de enlace de servicios y quién lo opera. | Por ahí entra todo: las interfaces de negocio, la sincronización diferida de preventa y reparto, y los tres portales del canal moderno. El Artículo 21.2 no pide 'un gateway': pide autenticación, autorización, cuotas, límites de tasa, validación de esquema e inspección de carga útil, todo en el borde. | Amazon API Gateway como capa 3 única, con autorizador de identidad contra el servidor de identidad maestro, validación de esquema, cuotas y límites por actor y por ruta, versionado y asignación del identificador de transacción. Kong Gateway queda declarado como alternativa de código abierto evaluada y no adoptada. | Kong obligaba a operar nodos propios con alta disponibilidad, parches y versiones a cargo de un equipo de cuatro personas, y a ponerlos en la ruta de la venta durante la ventana de despacho. El servicio administrado cumple literalmente el 21.2 sin desarrollo propio. La reversibilidad se mantiene porque los contratos son estándares abiertos y la lógica vive en el backend, no en la puerta de enlace: migrar sería reconfigurar rutas, no reescribir servicios. | Art. 21.2; Art. 16.3 | RT-02.01 RT-11.11 RT-05.16 RT-05.18 |
| 43 | Si la observabilidad es una sola plataforma o dos —una en la nube y otra autoalojada en cada centro de distribución— y qué se ve durante un corte de enlace de 24 horas. | El Artículo 16.4 y el requisito transversal exigen que el monitoreo del componente on-premise se integre a LA MISMA plataforma que la nube, sin puntos ciegos. Un conjunto autoalojado por sitio es, por definición, una segunda plataforma, y hay que declarar honestamente qué se pierde cuando cae el enlace. | Una sola plataforma. El on-premise solo EMITE: colectores con buffer en disco de 24 horas que exportan a la plataforma de nube (métricas compatibles con Prometheus, registros, trazas y tableros). Se descarta el conjunto Prometheus, Grafana y Loki autoalojado por sitio. Durante un corte no hay tableros centralizados, pero no se pierde ninguna señal y las alarmas locales del equipamiento siguen operando. | La norma pide una plataforma, no dos: usa la palabra 'misma'. El 'sin puntos ciegos' se resuelve con el buffer de 24 horas —exactamente la autonomía comprometida del centro de distribución—, no con una segunda plataforma. Y ninguna decisión crítica depende de un tablero: el bloqueo de despacho por excursión térmica es local, la alarma de cámara es acústica y luminosa, y los sensores de sala reportan al sistema del recinto. Lo que se pierde en contingencia es visibilidad agregada, no capacidad de operar. No hay bloqueo de proveedor porque la instrumentación es un estándar neutral y las métricas son compatibles con Prometheus. | Art. 16.4; RT-03.16 | RT-03.16 RT-14.01 RT-14.08 RT-09.01 |
| 44 | Cómo se gestionan los cerca de 270 dispositivos de terreno: enrolamiento, política, actualización, inventario y borrado cuando un dispositivo se pierde o una persona deja de trabajar. | La gestión remota y centralizada de dispositivos es obligatoria, y aquí el parque no está en oficinas: son preventistas y conductores en la calle, con 38 % de rotación anual en preparación y cerca de 160 conductores de terceros que rotan sin aviso. Hasta ahora se mencionaba de forma transversal, sin componente ni emplazamiento. | Se declara un componente propio con emplazamiento: gestión de dispositivos como servicio gestionado sobre el ecosistema Android empresarial del fabricante del parque, incorporado a la tabla de emplazamiento y al inventario ofertado. Cubre enrolamiento contra el usuario antes del turno, política de cifrado y bloqueo, modo quiosco, actualización de aplicación y de caché de turno, inventario por número de serie y BORRADO REMOTO SELECTIVO de los datos de la aplicación sin tocar la información personal del dispositivo. | El requisito es obligatorio y no se cumple con una mención: sin componente no hay emplazamiento justificado ni costo, que es lo que exige el Artículo 16.2. El parque es cien por ciento de un solo fabricante y sistema operativo, de modo que el ecosistema gestionado es el camino nativo y evita integrar herramientas por separado. No se autoaloja por la misma razón que el gestor de secretos: cuatro personas de tecnologías de información. El borrado selectivo es lo que permite cortar el acceso de un conductor externo el mismo día en que el transportista lo cambia. | RT-03.18; Cap. 2.4 y Cap. 15 del caso | RT-03.18 RT-08.14 RT-12.10 RF-03.16 RF-06.12 |
| 45 | Cuántos terminales de reparto se compran: uno por persona o uno por tripulación, dado que el caso da tres cifras que parecen contradictorias. | El caso declara 42 camiones propios, 84 conductores propios y peonetas, y una tabla de volumetría que dice 42 conductores propios. Según cómo se lea, el parque de terminales, impresoras de cabina y terminales de pago cambia en 42 unidades por ítem, con impacto directo en la oferta económica. | Se declara el supuesto que reconcilia las tres cifras sin residuo: los 84 son UNA TRIPULACIÓN POR CAMIÓN, es decir 42 conductores más 42 peonetas. El terminal, la impresora de cabina y el terminal de pago se asignan POR TRIPULACIÓN, no por persona. El parque queda en 42 más reserva para conductores propios y cerca de 160 más reserva para externos. Se eleva como consulta al mandante. | 42 conductores más 42 peonetas coincide exactamente con los 42 camiones propios del capítulo de instalaciones y con los 42 conductores propios de la tabla de volumetría, de modo que es la única lectura que no deja cifra suelta. Operativamente se sostiene: el peoneta manipula carga y trabaja junto al conductor, que es quien porta el dispositivo, y el propio caso exige que el equipo se use a una sola mano durante la descarga. Si el CLIENTE exigiera un terminal por persona, el parque propio sube de 42 a 84 por ítem y el efecto —del orden de 113 mil dólares antes de reservas— se traslada a la oferta. | Cap. 2.3 y 2.4 frente a la Tabla 14.1 | RT-08.10 RT-13.08 RT-17.06 |
| 46 | Si los datos personales pueden replicarse fuera de Chile hacia la región de recuperación, con qué base de licitud y con qué resguardos. | La región secundaria está en los Estados Unidos y hacia allá se replican la base transaccional —con antecedentes comerciales y saldos—, la telemetría y la evidencia de entrega con fotografías y firmas. El Artículo 23 exige declarar la residencia y, para toda transferencia internacional de datos personales, base de licitud y resguardos conforme a la ley de protección de datos. La arquitectura declaraba la región y la distancia, pero no esto. | Se declara la transferencia como tal y se acota: cifrado con clave gestionada por el CLIENTE, acuerdo de tratamiento con cláusulas de transferencia, MINIMIZACIÓN —la región secundaria no se explota analíticamente, solo sostiene continuidad— y EXCLUSIÓN de los datos de geolocalización de personas de la replicación transfronteriza, que permanecen solo en la región primaria con retención de 12 meses. La residencia queda sujeta a aprobación expresa del CLIENTE; si no la aprueba, la alternativa declarada es recuperación intrarregional con respaldo inmutable. | Es una exigencia literal del Artículo 23 que no estaba respondida. La exclusión de la geolocalización tiene además fundamento del caso: es el dato con objeción sindical explícita y con la retención más corta, y no es necesario para reanudar la operación, de modo que mantenerlo en una sola jurisdicción reduce la superficie legal sin costo de continuidad. | Art. 23; Ley 21.719; Cap. 12 del caso | RT-05.07 RT-05.08 RT-11.10 RT-16.09 RT-07.02 |
| 47 | Cuál es el compromiso contractual de disponibilidad: el 99,95 % por componente de infraestructura o el 99,9 % de la transacción de negocio de extremo a extremo. | El capítulo de niveles de servicio fija 99,95 % mensual para energía del recinto, climatización, red, servidores, motor de base de datos y portal, y a la vez declara que el compromiso que se mide y se penaliza es el de extremo a extremo. Un recinto clasificado TIER II ofrece 99,741 %, por debajo del 99,95 % de energía, y eso hay que explicarlo antes de que lo pregunten. | El compromiso contractual medido y penalizado es la DISPONIBILIDAD DE EXTREMO A EXTREMO DE LA TRANSACCIÓN CRÍTICA DE NEGOCIO, igual o superior a 99,9 % mensual. Los niveles por componente se declaran como objetivos internos de diseño y se alcanzan por redundancia, no por la clasificación del recinto: energía con sistema ininterrumpido en configuración N+1 más generador y transferencia automática, climatización N+1, red con tres caminos y conmutación bajo 30 segundos, cómputo en clúster con tolerancia a la caída de un nodo, y base de datos con conmutación automática. | La propia norma dice que los niveles de infraestructura son un medio y no un fin. La clasificación TIER II describe el recinto; el 99,95 % por componente se consigue con la redundancia declarada, que es lo que efectivamente evita la interrupción. Declararlo así evita el error contrario —comprometer un TIER superior que encarece la obra sin mejorar el indicador que se penaliza— y deja explícito que el sobredimensionamiento del recinto se castiga tanto como el subdimensionamiento. | Cap. 7.2 de las Transversales; Art. 78; RT-10.01 | RT-10.01 RT-06.07 RT-06.13 RT-03.17 RNF-20.06 |
| 48 | Dónde está el centro de operaciones de seguridad, con qué dotación y con qué procedimientos. | El requisito es obligatorio y pide las tres cosas expresamente. Aquí el turno de preparación es nocturno y la ventana de despacho es de madrugada: un centro de operaciones que solo cubra horario de oficina no sirve para esta operación. | Centro de operaciones de seguridad EN CHILE, propio o subcontratado a un proveedor con presencia nacional, con sitio de respaldo declarado y capacidad de operar de forma remota. Dotación: un analista de primer nivel por turno en cobertura continua, un segundo nivel de guardia con escalamiento en 30 minutos o menos, y el Encargado de Seguridad de la Información como tercer nivel para severidad crítica, con refuerzo del primer nivel en los peaks de septiembre y diciembre y en la ventana 05:30–07:00. Procedimientos documentados de monitoreo, clasificación, búsqueda proactiva, escalamiento, comunicación en 2 horas y notificación de brecha en 24 horas. | El refuerzo está puesto donde el caso concentra el riesgo, no de forma pareja: septiembre y diciembre casi duplican el volumen y la ventana de despacho tiene indisponibilidad cero comprometida. La ubicación en Chile facilita la coordinación con el equipo del CLIENTE y el cumplimiento de los plazos de comunicación, que se cuentan en horas. | RT-11.17; RT-21.06; Cap. 13.2 del caso | RT-11.17 RT-11.15 RT-11.18 RT-11.19 RT-21.06 |
| 49 | Con qué criterio se aprueba la incorporación de una biblioteca o dependencia de terceros al software. | Es obligatorio declarar el proceso con criterios de licencia, mantención activa y ausencia de vulnerabilidades conocidas. Sin criterio escrito, la decisión la toma quien escribe la línea de código, y el efecto aparece años después en la operación. | Proceso con TRES CRITERIOS COPULATIVOS: licencia compatible con el uso del CLIENTE —permisivas admitidas, licencias de reciprocidad fuerte rechazadas en componentes que se distribuyan o expongan como servicio salvo autorización expresa—; mantención activa, con publicación en los últimos 12 meses, más de un mantenedor y respuesta documentada a incidencias de seguridad; y ausencia de vulnerabilidades críticas o altas sin corrección disponible. Levanta el Líder de Desarrollo con evidencia de los tres, aprueba el Comité de Arquitectura, y queda en el registro de dependencias junto al inventario de componentes de la versión. El flujo de integración bloquea automáticamente lo que no esté en el registro. | Los tres criterios son los que el requisito nombra, y se hacen verificables porque cada uno tiene evidencia asociada y el bloqueo es automático, no una buena intención. Vincularlo al inventario de componentes de cada versión permite responder, ante una vulnerabilidad publicada, qué versiones en producción la contienen. | Art. 21.4; RT-11.26 | RT-11.26 RT-11.22 RT-11.23 RT-11.24 |
| 50 | Cómo se gobiernan los contratos de las interfaces: formato, versionado, obsolescencia y quién aprueba un cambio que rompe compatibilidad. | El caso se juega en las integraciones: un sistema de gestión sin interfaces documentadas, una preventa cuyo proveedor desapareció, mensajería electrónica con cadenas que fijan su propia especificación y un hito contractual en enero de 2029. Sin gobierno, cada integración nueva es un proyecto. | Catálogo único versionado como registro de las integraciones: interfaces síncronas en OpenAPI 3.1 y flujos por eventos en AsyncAPI 2.6, cada contrato con módulo dueño, versión semántica, estado y fecha de retiro. Evolución aditiva primero; versionado semántico estricto; preaviso mínimo de seis meses y doble versión concurrente durante la migración; todo cambio que rompe compatibilidad lo aprueba el Comité de Arquitectura con plan de migración y consumidores identificados uno a uno. No se publica ni se retira ninguna versión en septiembre, en diciembre ni en los tres primeros días hábiles del mes. | El preaviso de seis meses y el versionado semántico son exigencia normativa; el aporte de la decisión es atarlos al calendario real del caso —las dos ventanas de congelamiento y el cierre mensual— y hacer que lo que no está en el catálogo no se despliegue. Las especificaciones de las cadenas y de la autoridad tributaria no las controla el proponente: se versionan como perfiles y se prueban contra el banco de pruebas de cada contraparte antes de activarse. | Art. 19 y Art. 23; RT-05.16 y RT-05.17; Cap. 13.2 del caso | RT-05.16 RT-05.17 RT-05.19 RT-02.02 |
| 51 | Cómo se incorpora una cadena de supermercados nueva a la mensajería electrónica sin construir una integración distinta para cada una. | Es uno de los trece puntos que el capítulo de arquitectura del caso exige resolver, y tiene fecha: las condiciones comerciales de la principal cadena entran en vigor en enero de 2029. Hoy hay cero pedidos electrónicos y las diferencias de maestro se resuelven caso a caso. | Concentrador de intercambio electrónico basado en estándares globales de identificación, con un modelo canónico propio al que se mapea cada cadena, y no al revés. Una cadena nueva se incorpora por CONFIGURACIÓN DE PERFIL —equivalencias de código de producto por cadena y parámetros de la ventana— y pruebas de conexión, no por desarrollo. Se acompaña de una bandeja de excepciones operada por una persona responsable y de un portal de servicios con banco de pruebas y credenciales autoservidas. | Los conectores punto a punto multiplican los adaptadores y la lógica de mapeo por cada cadena, y dejan al sistema de gestión expuesto en la frontera. Mapear contra un modelo canónico y no contra el sistema de gestión es lo que hace que el esfuerzo marginal de la cadena número dos sea configuración. El portal con banco de pruebas existe porque cada cadena tiene su propio equipo técnico: permite que se integren por ensayo propio en vez de por reuniones, que es lo que hace realista la fecha de 2029. | Cap. 17.4 punto 10; Cap. 13.2 del caso; RT-05.23 | RT-05.23 RT-05.21 RT-05.24 RF-12.03 RF-12.06 RNF-12.01 |
| 52 | Si la solución incorpora inteligencia artificial o analítica predictiva, y en qué. | El capítulo de inteligencia artificial permite no proponerla, pero exige declararlo de forma fundada; y la analítica predictiva es un requisito valorado. Proponer un modelo que nadie pueda mantener durante 56 meses es peor que no proponerlo. | NO se propone inteligencia artificial ni analítica predictiva en el alcance contratado, con declaración fundada. Se deja la capa analítica PREPARADA —lago de datos en formato columnar y almacén analítico— para incorporarla cuando el CLIENTE tenga la madurez de datos que hoy no tiene. El ruteo se resuelve con optimización determinística, no con aprendizaje automático. | Es una renuncia razonada, no una omisión. El pronóstico de demanda con estacionalidad fuerte y promociones exige reentrenamiento y gobierno de modelo que un área de cuatro personas no sostiene, y el caso parte de una base de datos con 41 % de recepciones sin lote y 2,3 % de diferencia de inventario: predecir sobre datos así produce confianza injustificada. Los problemas del caso —trazabilidad, ruteo, evidencia de entrega, costo de servir— se resuelven antes con datos confiables y reglas explícitas. El ruteo determinístico además es auditable y corregible por el planificador, que es exactamente lo que pide el criterio de aceptación número 7. | Cap. 18 del transversal (RT-18); RT-05.30; Cap. 8 del caso (entrevista del planificador) | RT-18.01 RT-05.30 RF-04.01 RNF-04.01 |
| 53 | Con qué capacidad de cómputo se genera la ruta del día siguiente en menos de 20 minutos y dónde se ejecuta. | Es el criterio de aceptación número 7 del caso: hoy tarda 3,5 horas de una persona insustituible que se jubila dentro del horizonte del contrato. El compromiso estaba declarado, pero el motor no estaba dimensionado en ninguna parte, y resolver capacidad y ventanas horarias para cerca de 2.600 entregas y 96 camiones es una carga de cómputo por lote, no una consulta. | El motor de ruteo se ejecuta como tarea por lote en la nube, con recursos propios y separados de la carga transaccional, en la ventana previa a la planificación y fuera de la ventana crítica de despacho. Se dimensiona contra el peak de septiembre —cerca de 2.600 entregas y 96 vehículos con capacidad y ventanas de tiempo— con presupuesto de tiempo de 20 minutos y corte por tiempo con la mejor solución encontrada, de modo que SIEMPRE entregue una ruta dentro del plazo aunque no sea la óptima. El planificador puede corregirla y cada corrección queda registrada. | Separar el motor de la carga transaccional evita que la planificación compita con la operación del día. El corte por tiempo con la mejor solución encontrada es lo que convierte el compromiso de 20 minutos en algo cumplible: en optimización con capacidad y ventanas no se garantiza el óptimo en tiempo acotado, pero sí una solución factible y buena. Registrar cada corrección del planificador es, además, el mecanismo por el cual su conocimiento se convierte en parámetro del sistema antes de que se jubile. | Cap. 18 criterio 7; Cap. 8 del caso; Cap. 16.1 N° 16 | RF-04.01 RF-04.02 RNF-04.01 RT-09.01 RT-09.02 |
| 54 | Cómo se acredita la trazabilidad entre un requerimiento, el cambio de código que lo implementa, la prueba que lo verifica y el despliegue que lo pone en producción. | Es obligatorio y es lo que permite responder, ante una observación del mandante, en qué versión quedó resuelto y con qué evidencia. También es lo que hace auditable el reparto entre las dos etapas, que se solapan entre los meses 13 y 20. | Cadena verificable con puntos de control automáticos: el identificador del requerimiento se escribe en la incidencia; la incidencia se nombra en la rama y en cada confirmación, y el gancho del repositorio RECHAZA la confirmación que no la cite; la solicitud de incorporación no se puede fusionar sin la prueba automatizada que cubre ese requerimiento; y el despliegue registra el identificador de la imagen junto a las incidencias que incorpora. Se adopta además ambiente efímero por solicitud de incorporación, creado y destruido automáticamente. | La trazabilidad declarada como intención no se sostiene; declarada como tres bloqueos automáticos, sí. El ambiente efímero se adopta porque entre los meses 13 y 20 conviven la marcha blanca de la primera etapa y el desarrollo de la segunda, y un ambiente de calidad compartido se vuelve el cuello de botella entre frentes; sobre cómputo elástico su costo es proporcional a la vida de la rama. | RT-04.04 y RT-04.14; Art. 17.2 del cronograma obligatorio | RT-04.04 RT-04.14 RT-04.05 RT-20.02 |
| 55 | Si se compromete una meta de reducción del consumo energético durante los 36 meses de Operación y cómo se verifica. | Es un requisito valorado y una de las pocas palancas de sostenibilidad que la solución controla directamente. Declarar una meta sin medición es una declaración de intenciones. | Trayectoria comprometida y medida sobre el indicador de eficiencia del recinto: 1,70 o menos al inicio, 1,65 o menos al cierre del segundo año y 1,60 o menos al cierre del tercero, sobre medición continua en dos puntos. Palancas declaradas: confinamiento del pasillo frío, ajuste de las consignas de temperatura dentro del rango de la norma a medida que la carga real se estabiliza, y apagado o reducción de los ambientes no productivos fuera de horario. Informe anual de eficiencia con el consumo absoluto y la comparación con el año anterior. | La meta es verificable porque los dos puntos de medición ya están instalados por otro requisito y el informe declara el consumo absoluto además del índice, de modo que no se puede mejorar el indicador simplemente aumentando la carga. Las tres palancas son las que el propio diseño habilita, no genéricas: el ahorro real está en los ambientes no productivos, que es donde está el consumo evitable. | RT-15.06; RT-04.13; Cap. 6.1 del transversal | RT-15.06 RT-06.11 RT-04.13 RT-15.01 |
| 56 | Con qué marco se mide y se mejora la madurez del proceso de desarrollo seguro, y hasta qué nivel se compromete. | Es un requisito valorado que pide evaluación inicial y reevaluación anual. Comprometer un nivel alto de forma transversal durante 56 meses es fácil de escribir y difícil de sostener. | Se aplica el marco de madurez de desarrollo seguro sobre sus cinco dominios, con evaluación inicial en el mes 3 del proyecto —que fija la línea base y el objetivo por práctica— y reevaluación anual con informe al CLIENTE. Se compromete MADUREZ 2 en las prácticas que tocan directamente la operación de Puelche: modelado de amenazas, pruebas de seguridad, gestión de defectos y gestión de dependencias. MADUREZ 1 en el resto. | Comprometer madurez 3 transversal habría sido una declaración que no se sostiene con el equipo del CLIENTE durante todo el contrato, y las Bases penalizan tanto sobredimensionar como subdimensionar. Concentrar el nivel 2 en las cuatro prácticas que efectivamente protegen la operación —y decir por qué— es más defendible que un número parejo. La evaluación en el mes 3 permite corregir dentro de la primera etapa y no al final. | RT-11.28; Art. 21.4 | RT-11.28 RT-11.02 RT-11.04 RT-11.26 |
| 57 | Cuál es la sexta instalación y si lleva cómputo propio, dado que el caso dice cinco en un capítulo y seis en la tabla de volumetría y en el requisito de traslados. | Determina el alcance de la red, del soporte, de los traslados a sitios alejados y del dimensionamiento. Además es una contradicción visible dentro de las propias Bases, y el caso premia detectar y resolver los vacíos. | Se declara la lectura única: SEIS INSTALACIONES, de las cuales CINCO ALOJAN CÓMPUTO —los dos centros de distribución y las tres plataformas de cross-docking—. La sexta es la casa matriz y oficinas de Talca, contigua al centro de distribución principal, que se sirve de la red y de los sistemas del centro y no lleva nodo de cómputo propio, pero sí cuenta para cobertura de red, soporte y traslados. La topología queda parametrizable para la séptima instalación proyectada y para el eventual centro de la Región de Los Lagos hacia 2030. Se eleva como consulta al mandante. | Prevalece el seis de la tabla de volumetría y del requisito de traslados por ser la fuente mayor y las dos menciones técnicas. La lectura se sostiene porque el propio caso ubica la casa matriz contigua al centro de distribución de Talca y sitúa las oficinas en Talca y Concepción: no es una instalación operacional con bodega, y por eso cuenta para red y soporte pero no para stock ni para cómputo. Así el inventario multisitio se declara sobre cinco sitios y la cobertura sobre seis, sin contradicción. | Cap. 2.1, Cap. 3 y S8 del caso frente a la Tabla 14.1 y RT-21.16 | RT-21.16 RT-02.12 RF-02.01 RF-02.02 |
| 58 | Qué se hace con el dato que falta en el origen al migrar, en particular con el lote ausente en el 41 % de las recepciones del producto involucrado en la suspensión comercial. | Es la diferencia entre partir de un indicador real y partir de uno inventado. Si se deduce el lote, la trazabilidad queda contaminada desde el primer día y el retiro sanitario en menos de dos horas se vuelve indemostrable. | NO se deduce ni se completa el dato ausente. El movimiento se migra marcado como 'lote no registrado en origen' y se EXCLUYE del cálculo de cobertura de trazabilidad. Lo mismo con la diferencia de 2,3 % del conteo cíclico y con la cuenta de envases retornables, que hoy no existe como saldo por cliente: se migra el estado real y el saldo inicial se levanta con un inventario de apertura acordado con el CLIENTE. | Inventar el dato produciría una cobertura de trazabilidad aparente del cien por ciento sobre registros que no la tienen, que es justamente lo que impidió responder al proveedor de lácteos en nueve días. Migrar marcado hace que el indicador de partida sea verdadero y, por lo tanto, que la mejora comprometida sea medible y auditable. Es también la única lectura compatible con el criterio de aceptación número 2, que exige el 100 % de las recepciones con lote hacia adelante, no hacia atrás. | Cap. 7.3 y Cap. 18 criterios 1 y 2 del caso; RT-05.12 | RT-05.12 RT-05.14 RF-01.03 RF-09.01 RNF-09.02 |
| 59 | Cuánto dura una sesión y un token en cada perfil, y cómo se autentica quien trabaja un turno completo sin señal. | El Artículo 22 exige política de sesión declarada, y aquí las condiciones descartan la contraseña: guantes térmicos a menos 22 grados, uso a una mano durante la descarga, de pie a la intemperie en la puerta del local, dispositivos compartidos entre turnos y 38 % de rotación anual. | Política única: identificador de sesión de 1 hora, token de acceso de 30 minutos y token de refresco de 30 días rotativo con detección de reúso. TOKEN SIN CONEXIÓN CON DURACIÓN POR PERFIL: 8 horas en el turno nocturno de bodega y 14 horas en el turno completo de reparto y en la jornada de preventa, renovado al inicio de turno con cobertura o contra la caché local de identidad. En terreno el número personal desbloquea el token local y no autentica contra el servidor por transacción; el dispositivo enrolado es el factor de posesión. Cierre por inactividad a los 30 minutos en consolas y 60 en superficies de lectura, una sesión activa por actor de terreno, e identificador de sesión prohibido en la dirección web. | La duración del token sin conexión se fija por PERFIL y no por un valor único porque los turnos son distintos: 8 horas cubre la preparación nocturna y 14 el turno completo de una ruta rural donde el conductor recupera cobertura solo al regresar. Renovarlo al inicio de turno garantiza que la ventana cubra la jornada aunque el dispositivo no vuelva a ver señal, sin autenticación en la ruta. Dispositivo más número personal satisface el doble factor sin exigir un segundo aparato a quien trabaja con guantes. | Art. 22; RT-12.07, RT-12.11 y RT-12.12; Cap. 6 y Cap. 15 del caso | RT-12.07 RT-12.11 RT-12.12 RT-13.08 RNF-06.02 RNF-13.01 |
| 60 | Cuál es el volumen total de datos históricos a migrar y si condiciona el dimensionamiento. | El numeral de volumetría del caso lo exige explícitamente y advierte que entregar la celda vacía se evalúa como dimensionamiento no realizado. Además determina si la migración es un problema de capacidad o de calidad. | Se estima en cerca de 9,6 GB en el origen y cerca de 20 GB en destino con índices, derivado de la volumetría del caso: maestros completos, ventas y pedidos de 3 años, inventario y movimientos de 2 años, trazabilidad sanitaria de 5 años y cuentas por cobrar con saldos vivos más 2 años. NO se migra la evidencia de entrega histórica —hoy es papel— ni los documentos tributarios en sí, cuyos metadatos sí se migran para reconstruir la cuenta corriente. | La derivación usa las cifras de la tabla de volumetría y no supuestos genéricos: pedidos y líneas por mes multiplicados por los meses de profundidad exigida, con tamaños unitarios declarados y un recargo por índices. La conclusión que importa es que 20 GB frente a un almacenamiento útil de 5,76 TB significa que LA MIGRACIÓN NO CONDICIONA EL DIMENSIONAMIENTO: lo que condiciona el plan es la calidad del origen, que es donde está el riesgo real con dos sistemas sin documentación de interfaces. | Numeral 14.2 del caso; RT-05.11 y RT-05.15 | RT-05.11 RT-05.15 RT-09.01 RT-03.14 |

<a id="seccion-16"></a>

### Material recibido: emplazamiento

Origen de esta tabla: 03_esquema_solucion_alcance/tablas_anexo/emplazamiento.tex.

<a id="tabla-3-a-17"></a>

**Tabla 3.A.17 — Modelo de emplazamiento híbrido: qué va dónde y por qué**

| **Componente** | **Emplazamiento** | **Justificación** |
| --- | --- | --- |
| Recepción, picking y carga en los centros de distribución de Talca y Concepción | On-premise, con réplica a nube | Debe seguir operando durante un corte de enlace (restricción N.° 2); el ambiente incluye montacargas y cámara de congelado a -22 °C sin cobertura de señal. |
| Plataformas de cross-docking de Curicó, Chillán y Los Ángeles | Gabinete de borde, con conectividad exclusiva por red móvil | Sin almacenamiento propio, ventana de operación de tres horas y sin fibra óptica disponible. |
| Preventa y reparto en dispositivos de terreno | Aplicación que opera sin red, con sincronización diferida a nube | Deben operar un turno completo sin señal, en rutas rurales de hasta 240 kilómetros (restricción N.° 3). |
| Trazabilidad de lote, cadena de frío, analítica, portal y componentes de inteligencia artificial | Nube pública, región Chile o Sudamérica | Volumen variable y sin acoplamiento a equipamiento físico; requiere elasticidad durante el peak de septiembre. |
| Telemetría de los 42 camiones propios | Se integra desde la plataforma del proveedor externo que ya la provee | Fuente existente que se preserva; los 54 camiones de transportistas no están cubiertos y se incorporan mediante un mecanismo a definir con cada empresa (Decisión N.° 5). |

<a id="seccion-17"></a>

### Material recibido: estrategia

Origen de esta tabla: 03_esquema_solucion_alcance/tablas_anexo/estrategia.tex.

<a id="tabla-3-a-18"></a>

**Tabla 3.A.18 — Estrategia de involucramiento por grupo de interés**

| **Grupo y cuadrante** | **Estrategia y canales** | **Momento y responsable** | **Indicador de adopción** |
| --- | --- | --- | --- |
| Sindicato de conductores <br> Influencia alta, interés alto <br> Cuadrante A | Resolver en mesas de trabajo la objeción a las cámaras en cabina y al control de jornada por posicionamiento satelital: la geolocalización se usa para control operativo y logístico, no para supervisión de jornada (RT-10.05). Acuerdo por escrito antes de la marcha blanca de reparto. | Meses 6–12 en diseño y 13–15 en marcha blanca <br> Patricio Henríquez | Carta de compromiso firmada; cero paralizaciones en marcha blanca |
| Equipo de TI del cliente <br> Influencia alta, interés medio <br> Cuadrante B | Todo componente que requiera administración dedicada se oferta como servicio gestionado y costeado (RT-03.16), con transferencia de conocimiento, documentación operacional y mesas técnicas mensuales. | Meses 1–16 <br> Guillermo Castillo | Mesa técnica mensual en agenda; 100 % de guías de operación entregadas |
| Jefa de calidad <br> Influencia alta, interés alto <br> Cuadrante A | Codiseño de trazabilidad por lote, cadena de frío y retiro sanitario; validación de los criterios de excursión térmica y de bloqueo de despacho; definición de registros y alertas. | Meses 4–12 en requerimientos y 13–15 en marcha blanca <br> Maximiliano Miño | Aprobación de trazabilidad en pruebas de aceptación; ejercicio de retiro bajo dos horas en marcha blanca |
| Planificador de rutas <br> Influencia media, interés alto <br> Cuadrante C | Ruteo automático construido con su conocimiento local: el planificador corrige y cada corrección queda registrada (RF-04.02). Capacitación y acompañamiento antes de la producción de la Etapa 1. | Meses 13–16 <br> Patricio Henríquez | Planificadores certificados; ninguna corrección sin registro |
| Bodega, turno de noche <br> Influencia alta, interés medio <br> Cuadrante B | Hardware rugerizado operable con guantes a -22 °C, confirmación en un segundo o menos y sin entrenamiento prolongado. Participación en la marcha blanca nocturna y validación de las misiones de picking. | Meses 13–15 <br> Patricio Henríquez | Pruebas de aceptación con 120 preparadores; cero reclamos ergonómicos |
| Preventistas <br> Influencia media, interés alto <br> Cuadrante C | Pruebas de aceptación con los 62 preventistas sobre consulta de stock, crédito y deuda vencida, y operación sin señal durante 14 horas. Incentivo por adopción de la toma con los tres datos consultados. | Meses 13–16, con pilotos previos <br> Maximiliano Miño y Patricio Henríquez | Porcentaje de tomas con triple consulta registrada |
| Transportistas externos <br> Influencia media, interés bajo <br> Cuadrantes B y D | Incorporación ágil de conductores que rotan sin aviso, con alta y baja en 24 horas o menos (RF-15.05), clave de un solo uso en la entrega, kit de incorporación y validación de la prueba de entrega con firma digital. | Meses 13–16 y durante la Operación <br> Guillermo Castillo | Alta o baja de conductor en 24 horas o menos; entregas con prueba firmada |
| Gerencia de finanzas <br> Influencia baja, interés medio <br> Cuadrante B | Reportes de costo de servir y de costo por entrega en los tableros, alineación de la recaudación con el descuadre registrado por causal, y avance financiero en los reportes de hito. | Continuo desde el mes 16 <br> Alex Aravena | Descuadre de recaudación explicado por causal en su totalidad |
| Cadenas del canal moderno <br> Influencia baja, interés medio <br> Cuadrante B | Intercambio electrónico y guías electrónicas probados con cada cadena antes de producción, con mesa de continuidad para el acuse de recibo. | Meses 10–16 <br> Leandro Chamorro | Cadenas con intercambio certificado al alta |
| Proveedores <br> Influencia baja, interés bajo <br> Cuadrante D | Incorporación al portal de recepción y trazabilidad de lote, comunicación por el canal digital de Puelche y acuerdos de entrega tipo. | Meses 10–16 <br> Leandro Chamorro | Porcentaje de recepciones con lote registrado |

<a id="seccion-18"></a>

### Material recibido: exclusiones

Origen de esta tabla: 03_esquema_solucion_alcance/tablas_anexo/exclusiones.tex.

<a id="tabla-3-a-19"></a>

**Tabla 3.A.19 — Registro de exclusiones: categoría, origen, sustituto y riesgo (15 filas)**

| **ID** | **Descripción** | **Categoría** | **Origen** | **Sustituto** | **Riesgo** |
| --- | --- | --- | --- | --- | --- |
| EX-01 | El proyecto no contempla el reemplazo, modificación o desarrollo del Sistema de Gestión Empresarial actual ni de ninguno de sus módulos. Asimismo, queda expresamente fuera del alcance la funcionalidad de emisión de Documentos Tributarios Electrónicos. | Arquitectura de Sistemas y Cumplimiento Tributario | Capítulo 11, Caso_02_Logistica.md | Sistema de Gestión Empresarial actual | La falta de documentación de las interfaces actuales dificulta la integración, arriesgando la consistencia transaccional y la validez legal de las entregas. |
| EX-02 | El proyecto no contempla el desarrollo ni la integración de módulos para la administración de remuneraciones o recursos humanos. Estas funciones continuarán operando y residiendo exclusivamente en el Sistema de Gestión Empresarial actual. | Gestión Administrativa Interna | Capítulo 11, Caso_02_Logistica.md | Sistema de gestión actual | Dificulta vincular el desempeño logístico con los pagos e incrementa la tensión por el control de jornada laboral. |
| EX-03 | Queda excluido del alcance el desarrollo o implementación de un sistema de Punto de Venta (POS) para el local físico del cliente. Esta exclusión no limita ni afecta el desarrollo del canal de autoatención que la solución debe proveer. | Sistemas de Operación Física | Capítulo 11, Caso_02_Logistica.md | Canal de autoatención del cliente | Mantiene la dependencia de procesos manuales en el almacén, limitando la adopción tecnológica total en el último tramo. |
| EX-04 | Queda expresamente fuera del alcance el diseño, desarrollo o habilitación de plataformas de comercio electrónico (e-commerce) orientadas al consumidor final (B2C). | Modelo de Negocio y Segmento de Mercado | Capítulo 11, Caso_02_Logistica.md | Foco en distribución comercial mayorista | Limita la capacidad de adaptación comercial de la empresa frente a futuros modelos de venta directa al consumidor. |
| EX-05 | Queda fuera del alcance la administración contractual y la gestión de pagos o facturación a las empresas transportistas. Sin embargo, el proyecto sí contempla su integración a nivel estrictamente operacional. | Gestión Comercial y Financiera de Proveedores | Capítulo 11, Caso_02_Logistica.md | Integración operacional de los transportistas actuales | La constante rotación sin aviso de los choferes externos dificultará su control, trazabilidad y capacitación operativa. |
| EX-06 | El proyecto no contempla el diseño estratégico de la red logística. La ubicación física, capacidad y configuración actual de los centros de distribución y plataformas operativas se asumen como definiciones dadas y no serán objeto de análisis ni rediseño dentro de este proyecto. | Consultoría Estratégica y Diseño de Cadena de Suministro | Capítulo 11, Caso_02_Logistica.md | Red logística actual | Perpetúa las ineficiencias estructurales preexistentes, como las inexplicables demoras operativas descubiertas en las plataformas de cross-docking. |
| EX-07 | Queda expresamente excluida la automatización física de bodegas y centros de distribución, incluyendo la implementación, control o integración directa de equipamiento robotizado, cintas transportadoras (conveyors) u otro hardware de automatización industrial. | Infraestructura Física y Automatización Industrial | Capítulo 11, Caso_02_Logistica.md | Personal y transpaletas manuales | Depender de procesos manuales perpetúa la vulnerabilidad frente a la altísima rotación del personal de preparación nocturna. |
| EX-08 | El alcance no incluye el desarrollo de funcionalidades para la gestión del mantenimiento mecánico o estado técnico de la flota de vehículos. Esta exclusión no limita la ingesta, lectura o integración de datos provenientes de los sistemas de telemetría actualmente operativos. | Mantenimiento de Activos Físicos | Capítulo 11, Caso_02_Logistica.md | Telemetría ya existente | Deja puntos ciegos operativos críticos, ya que la telemetría actual no cubre a los camiones subcontratados. |
| EX-09 | Queda excluida del alcance del PROPONENTE la adquisición, financiamiento y provisión física del hardware de terreno (dispositivos móviles, lectores de códigos, impresoras portátiles y sensores). Dicha compra es responsabilidad exclusiva del CLIENTE. No obstante, el PROPONENTE asume la obligación de especificar detalladamente las cantidades, características y requisitos técnicos de este equipamiento, en estricto cumplimiento con el Capítulo 8 de las Bases Técnicas Transversales. | Adquisición de Infraestructura y Responsabilidad Financiera | Capítulo 11, Caso_02_Logistica.md | Especificación técnica detallada del equipamiento requerido | Separar la responsabilidad de compra puede ocasionar retrasos o la adquisición de equipos incompatibles con temperaturas extremas. |
| EX-10 | Queda excluida del alcance del proyecto la ejecución de la obra civil necesaria para la separación física de las instalaciones en el recinto técnico principal (on-premise). Dicha obra es de cargo exclusivo del CLIENTE, restringiéndose la responsabilidad del PROPONENTE a su especificación técnica. | Infraestructura Física y Obra Civil | Bases_Tecnicas_Transversales.md, Capítulo 6, RT-06.06 | Habilitación del site principal on-premise | Una descoordinación entre el diseño técnico (proveedor) y la ejecución física (cliente) podría generar retrasos críticos en la habilitación del recinto y afectar el cronograma general. |
| EX-11 | Queda excluida del alcance la implementación o construcción de nuevas instalaciones sanitarias, zonas de seguridad ante emergencia y áreas exteriores para el personal de operación de la plataforma, permitiéndose expresamente el uso de las ya existentes en el edificio del CLIENTE. | Infraestructura Física y Espacios de Trabajo | Bases_Tecnicas_Transversales.md, Capítulo 6, RT-06.31 | Espacio de operación del personal on-premise | El contratista dependerá enteramente de los estándares, capacidad y continuidad de los servicios generales que provee el cliente in situ para su propio equipo de operación. |
| EX-12 | Quedan excluidos del alcance de soporte de la Mesa de Ayuda (Nivel 2) la resolución de aquellos incidentes relativos a procedimientos propios de la operación del CLIENTE o a aplicaciones que no hayan sido provistas por el ADJUDICATARIO, siendo éstos de responsabilidad exclusiva del CLIENTE y no derivables a la mesa. | Gestión de Servicios y Soporte Técnico | Bases_Tecnicas_Transversales.md, Capítulo 21, Tabla Nivel 2 | Mesa de ayuda y centro de atención telefónica | Riesgo de insatisfacción y fricción operativa si los usuarios intentan reportar fallas de sistemas heredados a la nueva mesa de ayuda, exigiendo un triage riguroso de rechazo de tickets. |
| EX-13 | Queda excluido de los requisitos del prototipo interactivo (exigido en la Oferta Técnica) el desarrollo de funcionalidad real de servicios de fondo, conexión a base de datos, procesamiento real de datos, integración con servicios externos, autenticación real o persistencia de la información ingresada. | Exigencias de Presentación de la Propuesta | Bases_Tecnicas_Transversales.md, Capítulo 25, Sección 25.6 | Prototipo interactivo de interfaz y diseño UX/ UI | Previene el encarecimiento desproporcionado de la fase de licitación, enfocando la evaluación estrictamente en la experiencia de usuario y diseño front-end sin exigir backend funcional prematuro. |
| EX-14 | Quedan excluidos del alcance de responsabilidad financiera del CLIENTE los reembolsos o indemnizaciones por concepto de gastos en los que incurran los PROPONENTES durante el estudio, preparación, presentación y defensa de sus ofertas (incluyendo pruebas de concepto, viajes o asesorías), siendo éstos de cargo exclusivo de los oferentes. | Condiciones Administrativas y Financieras del Proceso | Bases Administrativas.md, Título I, Capítulo 1, Art. 11.2 | Gastos de participación en la licitación | Blinda patrimonialmente al mandante frente a posibles reclamos de resarcimiento económico por costos hundidos si una empresa no resulta adjudicada o la licitación se declara desierta. |

<a id="seccion-19"></a>

### Material recibido: hitos

Origen de esta tabla: 03_esquema_solucion_alcance/tablas_anexo/hitos.tex.

<a id="tabla-3-a-20"></a>

**Tabla 3.A.20 — Hitos contractuales y externos que condicionan el alcance**

| **Hito** | **Fecha** | **Origen** |
| --- | --- | --- |
| Término de desarrollo y marcha blanca de la Etapa 1 | Mes 15 | Artículo 17<sup>o</sup> |
| Producción de la Etapa 1 | Mes 16 | Artículo 17<sup>o</sup> |
| Marcha blanca de la Etapa 2, en paralelo con la Etapa 1 | Meses 13–20 | Artículo 17.2 |
| Producción de la Etapa 2 | Mes 21 | Artículo 17<sup>o</sup> |
| Inicio y término de la Operación | Meses 21–56 | Artículo 17<sup>o</sup> |
| Peak de pedidos de septiembre, con el doble de volumen durante tres semanas | Septiembre de cada año | Caso, sección 13.2 |
| Congelamiento de intervenciones: del 1 al 25 de septiembre, todo diciembre y los tres primeros días hábiles de cada mes | Anual | Restricción N.° 8; caso, sección 13.2 |
| Canal moderno con pedidos electrónicos, aviso anticipado y ventana de 30 minutos | Antes de enero de 2029 | Caso, sección 2.1; RNF-12.01 |
| Captura del conocimiento de rutas antes del retiro del planificador | Etapa 1, antes de su fecha de salida | Caso, sección 13.1; decisión 16.1 N.° 16 |

<a id="seccion-20"></a>

### Material recibido: reglas negocio

Origen de esta tabla: 03_esquema_solucion_alcance/tablas_anexo/reglas_negocio.tex.

<a id="tabla-3-a-21"></a>

**Tabla 3.A.21 — Registro de reglas de negocio**

| **ID** | **Regla** | **Definición operativa** |
| --- | --- | --- |
| RNG-01 | Asignación y reserva de stock | La reserva se produce al confirmar el pedido, no al tomarlo ni al prepararlo, y se resuelve por orden de llegada. El segundo preventista que confirma sobre el mismo stock queda con quiebre parcial y no bloquea al primero. |
| RNG-02 | Stock disponible, comprometido y en tránsito | Disponible es el físico menos el comprometido. El tránsito no suma hasta que la recepción se confirma. Sin conexión el dato es indicativo y se muestra con su antigüedad; los conflictos se resuelven por orden cronológico. |
| RNG-03 | Política de crédito en preventa | Superar el límite dispara alerta; por sobre el 110 % se bloquea el envío. Las excepciones las autoriza un supervisor y quedan registradas; sin conexión se aprueban al sincronizar. |
| RNG-04 | Excursión térmica y disposición del producto | Los parámetros de tiempo y grados los define la jefa de calidad y son configurables. La alerta es inmediata, pero el bloqueo no es automático: el conductor decide la disposición según el producto. |
| RNG-05 | Reintento de entrega y local cerrado | El conductor reporta local cerrado, el sistema registra el fallido y reagenda a la siguiente ventana del cliente. El conductor no decide. Si la indisponibilidad persiste, los productos vuelven al almacén. |
| RNG-06 | Devoluciones y efecto tributario | La devolución se registra en la prueba de entrega, sin conexión y con motivo tomado de catálogo. El destino se decide en el andén de retorno y pasa al ERP. El documento ya emitido se resuelve con nota de crédito, con retención legal de seis años. |
| RNG-07 | Control de envases retornables | Se lleva saldo por cliente en cuenta corriente, no por unidad identificada. La entrega descuenta y la devolución suma; el preventista recibe alerta al superar el umbral y se emite reporte diario de pérdida. |
| RNG-08 | Cambio de precio entre toma y despacho | Por defecto se cobra el precio vigente al despacho. Solo una excepción explícita respeta el de la toma. Si hay cambio y no hay excepción, se alerta al cliente. |
| RNG-09 | Entrega cumplida, OTIF y fill rate | Una entrega parcial no cuenta como cumplida: *in full* exige el 100 % de ítems y unidades. *On time* se mide contra fecha y ventana. El fill rate compara unidades entregadas contra pedidas. Toda parcial queda como desvío auditado con causal. |
| RNG-10 | FEFO y vida útil remanente | El picking sigue estrictamente el vencimiento de lote, con bitácora de excepción. Se alerta bajo un umbral configurable, del orden de 30 días. |
| RNG-11 | Maestro de productos y códigos externos | Prevalece el maestro interno de Puelche como única fuente autorizada, con historial de códigos. Los códigos externos se resuelven por tabla de equivalencias por cadena; lo no resuelto pasa a bandeja de excepciones. |
| RNG-12 | Sincronización y resolución de conflictos | Al reconectar, la sincronización es automática con reconciliación determinista y bitácora auditable. Durante las 14 horas de terreno el dato sin conexión es indicativo y el stock se valida contra el servidor al reconectar. |
| RNG-13 | Secuenciación térmica y validación por zona | La secuencia de picking es seco, refrigerado y congelado. La compatibilidad térmica se valida al ubicar: un congelado no puede quedar fuera de zona congelada. |
| RNG-14 | Capacidad del vehículo y carga dirigida | No se asigna carga que exceda el peso o el volumen nominal, ni cadena de frío a un vehículo sin equipo. La carga se ordena en secuencia inversa a la ruta y se verifica el escaneo de todos los bultos. |

<a id="seccion-21"></a>

### Material recibido: restricciones

Origen de esta tabla: 03_esquema_solucion_alcance/tablas_anexo/restricciones.tex.

<a id="tabla-3-a-22"></a>

**Tabla 3.A.22 — Registro de restricciones: tipo, origen e impacto (44 filas)**

| **ID** | **Descripción** | **Tipo** | **Origen** | **Impacto** |
| --- | --- | --- | --- | --- |
| R-01 | La ventana de despacho matutino (05:30 a 07:00) no se puede detener bajo ninguna circunstancia. | Operacional | Caso_02_Logística (Capítulo 10) | Un sistema indisponible en ese tramo equivale a un día completo sin operación. |
| R-02 | El centro de distribución debe poder recibir, preparar y despachar incluso durante un corte de enlace a internet. | Operacional | Caso_02_Logística (Capítulo 10) | Garantiza que la preparación nocturna y la carga no queden detenidas por problemas de conectividad. |
| R-03 | Las aplicaciones móviles de terreno deben funcionar un turno completo sin señal. | Operacional | Caso_02_Logística (Capítulo 10) | Asegura la continuidad en rutas rurales donde el dispositivo no recupera cobertura hasta el regreso. |
| R-04 | El sistema de gestión empresarial actual no se reemplaza ni se modifica. | Sistema Core | Caso_02_Logística (Capítulo 10) | Previene discrepancias tributarias y contables, evitando que existan "dos verdades" o un segundo emisor de documentos. |
| R-05 | No se puede exigir al cliente tradicional que tenga internet, dispositivos o medios de pago electrónicos. | Usuario Final | Caso_02_Logística (Capítulo 10) | Protege la relación comercial obligando a que la solución funcione con el cliente tal como opera en la actualidad. |
| R-06 | La solución debe operar con conductores de empresas externas (transportistas). | Recursos Humanos | Caso_02_Logística (Capítulo 10) | Obliga a diseñar mecanismos ágiles de incorporación, ya que estos conductores rotan sin aviso previo. |
| R-07 | Los dispositivos utilizados en la cámara de congelado deben operar a -22 °C y sin señal en su interior. | Tecnológico | Caso_02_Logística (Capítulo 10) | Evita fallas de hardware en ambientes extremos que paralizarían el trabajo de los preparadores de pedidos. |
| R-08 | Toda función que requiera un administrador dedicado debe ofrecerse como servicio y estar costeada. | Recursos Humanos | Caso_02_Logística (Capítulo 10) | Previene la sobrecarga del actual equipo de TI del cliente, que cuenta con solo 4 personas. |
| R-09 | Se prohíbe implementar soluciones que requieran entrenamiento prolongado para operar en bodega. | Recursos Humanos | Caso_02_Logística (Capítulo 10) | Su incumplimiento será causal de rechazo debido a que el personal del turno de noche tiene una rotación del 38 % anual. |
| R-10 | Se prohíbe intervenir los sistemas del 1 al 25 de septiembre, todo diciembre y los primeros tres días hábiles de cada mes. | Planificación | Caso_02_Logística (Capítulo 10) | Protege la operación durante los peaks de ventas y cierres comerciales; ignorarlo pone en riesgo la facturación y el inventario valorizado. |
| R-11 | Cualquier propuesta con cámaras en cabina o control de jornada por GPS debe considerar la objeción sindical. | Legal / Laboral | Caso_02_Logística (Capítulo 10) | Determina qué tecnologías son viables y condiciona el plan de gestión del cambio para evitar conflictos laborales. |
| R-12 | La emisión de documentos tributarios electrónicos (DTE) debe cumplir estrictamente con la normativa vigente. | Legal / Tributario | Caso_02_Logística (Capítulo 10) | Asegura que la guía de despacho electrónica y su acuse de recibo mantengan sus efectos legales. |
| R-13 | Exclusión explícita de desarrollo de ciertos módulos (facturación, RRHH, POS, flota mecánica). | Alcance | Caso_02_Logística (Capítulo 11) | Obliga a que la solución propuesta conviva con los sistemas excluidos y a que estas dependencias se reflejen en el plan de riesgos. |
| R-14 | La Oferta Técnica (Sobre N° 2) no puede contener información de precios, tarifas o valores. | Administrativo | Bases Administrativas (Art. 50) | Su inclusión es causal de exclusión inmediata y automática del proceso de licitación. |
| R-15 | Las modificaciones contractuales durante la ejecución no podrán superar el 20 % del valor original del contrato. | Contractual | Bases Administrativas (Art. 72) | Limita legalmente los aumentos de presupuesto; cualquier cambio no aprobado corre por cuenta y riesgo del proponente. |
| R-16 | El prototipo interactivo UX/ UI no requiere conexión a bases de datos ni servicios de fondo reales. | Presentación | Bases Técnicas Transversales (Capítulo 25) | Permite enfocar la evaluación en el diseño, la usabilidad y la comprensión de los flujos, aunque se penalizarán los diseños estáticos no navegables. |
| R-17 | Límite y núcleo de subcontratación: Máximo 40% del valor del contrato y prohibición de externalizar el núcleo del negocio (aplicaciones e información críticas). | Contractual | Art. 73.1 y 73.2 BA | Obliga a mantener el control directo sobre la custodia de datos y limita el uso de terceros. |
| R-18 | La licitación es de etapa única con plazos fatales e improrrogables para la entrega simultánea de tres sobres. | Restricción de Cronograma / Adquisiciones | Bases Administrativas (Art. 7° y 10°) | Limita el tiempo del proyecto en la fase de preventa; cualquier atraso en los hitos causa la exclusión automática. |
| R-19 | Las ofertas económicas que se sitúen fuera del intervalo de confianza obtienen automáticamente 0 puntos en la evaluación económica. | Restricción de Costo / Adquisiciones | Bases Administrativas (Art. 60° y 61°) | Acota las opciones de fijación de precios, impidiendo estrategias de "precio bajo para ganar" o sobreprecios. |
| R-20 | Las ofertas deben expresarse en CLP, UF y USD con tipo de cambio fijo, manteniendo precios firmes en las Etapas 1 y 2, y reajuste tope IPC en Operación. | Restricción de Costo | Bases Administrativas (Art. 9°) | Limita la capacidad del director de proyecto para traspasar riesgos inflacionarios o cambiarios al cliente. |
| R-21 | El proponente debe entregar garantías de Seriedad por USD 500.000, Fiel Cumplimiento por USD 1.000.000 y Correcto Funcionamiento por el 5% del valor de implementación. | Restricción de Costo / Contractual | Bases Administrativas (Art. 35° al 37°) | Limita el flujo de caja del contratista y exige alta liquidez para ejecutar el proyecto. |
| R-22 | Todo el proceso, las interfaces y la documentación operativa dirigida a usuarios finales deben entregarse íntegramente en español. | Restricción de Alcance (Comunicaciones) | Bases Administrativas (Art. 8°) | Obliga a descartar soluciones extranjeras que no cuenten con soporte nativo o localizado al español. |
| R-23 | El video de presentación no puede superar los 5 minutos y todos los integrantes clave del equipo deben aparecer al menos 10 segundos cada uno. | Restricción de Alcance / Adquisiciones | Bases Técnicas Transversales (Cap. 24) | Restringe la libertad creativa y de formato; el incumplimiento causa descalificación automática. |
| R-24 | La página web corporativa del proponente debe mantenerse activa y disponible ininterrumpidamente durante todo el proceso de licitación. | Restricción de Calidad / Adquisiciones | Bases Técnicas Transversales (RT-23.06) | Impone un SLA no negociable sobre los propios activos digitales del proveedor bajo pena de descalificación. |
| R-25 | El contrato tiene una duración total e indivisible de 56 meses, con un cronograma obligatorio que no admite plazos distintos. | Restricción de Cronograma | Bases Administrativas (Art. 15° y 17°) | El cronograma general está impuesto por el cliente; no se pueden proponer plazos alternativos de ejecución. |
| R-26 | El total de multas aplicadas en un período de doce meses no podrá exceder el 15 % del valor del contrato correspondiente a ese período. | Restricción Contractual | Bases Administrativas (Art. 80°) | Habilita al cliente a imponer el término anticipado del contrato si las desviaciones superan este límite. |
| R-27 | Se prohíbe al adjudicatario reutilizar los desarrollos específicos del proyecto para otros clientes sin autorización previa y escrita. | Restricción Legal / Contractual | Bases Administrativas (Art. 84.7) | Limita la capacidad de comercializar el software a futuro, afectando el cálculo del retorno de inversión (ROI). |
| R-28 | La solución debe ser obligatoriamente híbrida, con la carga principal en una nube pública regional y componentes on-premise críticos. | Restricción Técnica (Alcance) | Bases Administrativas (Art. 16°); Bases Técnicas Transversales (RT-03.01) | Invalida diseños técnicos alternativos (ej. 100% Cloud o 100% físico) limitando las opciones de arquitectura. |
| R-29 | Todo componente ofertado debe contar con soporte vigente del fabricante que cubra la totalidad del período contractual de 56 meses. | Restricción de Calidad / Riesgo | Bases Técnicas Transversales (Cap. 1.6) | Obliga a descartar tecnologías emergentes inestables o versiones próximas a quedar sin soporte. |
| R-30 | La propuesta debe incluir obligatoriamente cinco innovaciones específicas (producto, proceso, tecnología, modelo de negocio e impacto). | Restricción de Alcance | Bases Administrativas (Art. 28°) | Obliga al equipo a integrar y costear alcance adicional no derivado directamente de la operación diaria. |
| R-31 | El desarrollo de la Etapa 2 debe ejecutarse en paralelo con la marcha blanca y estabilización de la Etapa 1. | Restricción de Cronograma / Recursos | Bases Administrativas (Art. 17.2); Caso_02_Logistica (Cap. 13) | Limita la optimización de recursos, obligando a disponer de frentes de trabajo simultáneos sin reutilizar al mismo equipo. |
| R-32 | La estrategia de despliegue debe permitir liberar cambios sin interrupción del servicio, utilizando técnicas como azul-verde o canario. | Restricción Técnica (Calidad) | Bases Técnicas Transversales (RT-04.06 y 04.07) | Restringe los métodos de despliegue convencionales y obliga a implementar infraestructura como código desde el día uno. |
| R-33 | La lista de clientes afectados por un retiro sanitario debe obtenerse con evidencia en menos de dos horas. | Restricción de Calidad (Desempeño) | Caso_02_Logistica (Cap. 18) | Impone métricas de rendimiento inflexibles que condicionan el motor de bases de datos analítico elegido. |
| R-34 | Las transacciones operacionales críticas deben cumplir umbrales de latencia estrictos medidos en el percentil 95 (ej. 1 segundo para picking). | Restricción de Calidad (Desempeño) | Bases Técnicas Transversales (RT-09.01) | Obliga a diseñar mecanismos complejos de caché y prohíbe el uso de promedios simples para justificar rendimiento. |
| R-35 | Los servicios críticos deben cumplir un RTO máximo de 4 horas y un RPO máximo de 15 minutos, con respaldos bajo esquema inmutable 3-2-1-0. | Restricción Técnica (Calidad) | Bases Técnicas Transversales (RT-07.04 y 07.09) | Obliga al diseño e inversión en un sitio secundario activo/ pasivo o activo/ activo innegociable. |
| R-36 | El recinto técnico principal on-premise exige control de acceso por biometría facial, detección de humo AnaLASER y extinción FM-200. | Restricción de Alcance (Infraestructura) | Bases Técnicas Transversales (RT-06.16 a 06.20) | Fija estándares constructivos obligatorios que inflan el costo base de infraestructura local del proyecto. |
| R-37 | La arquitectura debe basarse en Zero Trust, utilizando exclusivamente TLS 1.3 y aplicando cifrado en reposo y a nivel de campo para datos sensibles. | Restricción Técnica (Seguridad) | Bases Técnicas Transversales (RT-11.01, 11.08 y 11.10) | Limita el uso de arquitecturas de red perimetrales y protocolos de conexión obsoletos. |
| R-38 | Se prohíbe absolutamente mantener credenciales embebidas en el código o transportar identificadores de sesión en la ruta de la dirección web. | Restricción Técnica (Seguridad) | Bases Técnicas Transversales (RT-04.09 y 12.08) | Obliga a integrar gestores de llaves (KMS) y prohíbe prácticas de desarrollo inseguras comunes. |
| R-39 | Las personas desarrolladoras no pueden tener acceso interactivo a producción y se prohíbe usar datos reales no anonimizados en pruebas. | Restricción de Recursos / Seguridad | Bases Técnicas Transversales (RT-11.25 y 11.27) | Acota fuertemente cómo el equipo técnico puede operar y hacer troubleshooting de incidencias. |
| R-40 | Se debe garantizar contractualmente que los datos del cliente no se usarán para entrenar modelos de inteligencia artificial de terceros. | Restricción Legal / Riesgo | Bases Técnicas Transversales (RT-18.02 y 18.03) | Impide el uso indiscriminado de APIs públicas de IA, obligando a usar modelos privados o anonimizados. |
| R-41 | La plataforma debe retener documentos tributarios y evidencia por 6 años, registros sanitarios por 5 años y datos de geolocalización por 12 meses. | Restricción Legal / Alcance | Bases Técnicas Transversales (RT-05.10); Caso_02_Logistica (Cap. 15) | Obliga a asumir costos fijos de almacenamiento de largo plazo dictados por normativas gubernamentales/ sanitarias. |
| R-42 | Todo reemplazo del equipo clave exige un período de traslape mínimo de 15 días hábiles sin costo adicional para el cliente. | Restricción de Recursos / Costos | Bases Administrativas (Art. 76.2) | Limita la libertad del proveedor para reasignar a su propio personal interno sin penalización financiera. |
| R-43 | El flujo de integración continua debe bloquear automáticamente el despliegue si la cobertura de pruebas de lógica de negocio es inferior al 70 %. | Restricción de Calidad / Proceso | Bases Técnicas Transversales (RT-04.11) | Impone un estándar mínimo de programación (como Test-Driven Development) ineludible para el equipo de desarrollo. |

<a id="seccion-22"></a>

### Material recibido: resultados cap18

Origen de esta tabla: 03_esquema_solucion_alcance/tablas_anexo/resultados_cap18.tex.

<a id="tabla-3-a-23"></a>

**Tabla 3.A.23 — Resultados de negocio del Capítulo 18: meta, momento y medición**

| **Código** | **Meta comprometida** | **Momento** | **Medición y evidencia** |
| --- | --- | --- | --- |
| R18-01 | Ante un retiro sanitario, la lista de clientes afectados por lote se obtiene con evidencia en menos de dos horas, cubriendo el 100 % del lote. | En operación desde la producción de la Etapa 1, mes 16. | Ejercicio de trazabilidad hacia adelante y hacia atrás sobre los eventos GS1 EPCIS, midiendo desde la consulta hasta la lista con evidencia. Línea base: 9 días. |
| R18-02 | El 100 % de las recepciones de productos que lo requieren registra el lote. | En operación desde el mes 16. | Porcentaje de órdenes de compra y recepciones con lote capturado, auditado en los conteos cíclicos. Línea base: 41 % sin registro. |
| R18-03 | Registro continuo y automático de temperatura en cámaras y en vehículos con equipo de frío, auditable y disponible para el cliente. | En operación desde el mes 16. | Serie de temperatura por sensor con integridad comprobable y cumplimiento de cadena de frío por viaje. Reemplaza las tres lecturas manuales de cada viaje. |
| R18-04 | OTIF con mejora gradual: 90 % al cierre de la Etapa 1, 93 % al mes 12 y 95 % en régimen. | Curva gradual desde la marcha blanca, meses 13–15, y en régimen durante la Operación. | OTIF diario por cliente, ruta, zona y consolidado, con base de cálculo explícita e *in full* al 100 %. Línea base: 82,4 %. |
| R18-05 | El preventista conoce el stock disponible, el crédito y la deuda vencida del cliente en el punto de toma, con y sin conectividad. | En operación desde el mes 16. | Porcentaje de tomas con consulta registrada de los tres datos; pruebas de aceptación con los 62 preventistas; prueba de operación sin red durante 14 horas. |
| R18-06 | Ningún pedido se pierde ni se duplica por falta de señal. | En operación desde el mes 16. | Reconciliación de sincronización por turno con bitácora auditable; conteo de duplicados descartados y de pedidos no sincronizados. |
| R18-07 | La ruta del día siguiente se genera de forma automática en menos de 20 minutos y toda corrección queda registrada. | En operación desde el mes 16. | Tiempo de generación medido en operación diaria y bitácora de correcciones del planificador. Línea base: 3,5 horas. |
| R18-08 | La prueba de entrega es digital y está disponible para el cliente el mismo día; el acuse del canal moderno se envía dentro de los 30 minutos siguientes a la descarga. | Prueba de entrega desde el mes 16; acuse del canal moderno con la Etapa 2, mes 21. | Porcentaje de entregas con prueba digital —firma en pantalla, código QR o fotografía con nombre del receptor— y evidencia publicada el mismo día; acuse por vía electrónica. |
| R18-09 | Cero guías extraviadas o ilegibles, con guía de despacho electrónica integrada a la prueba de entrega. | En operación desde el mes 16. | Conciliación diaria de guías emitidas contra pruebas de entrega recibidas, y reclamos por guía ilegible o extraviada. Línea base: 1,1 % mensual. |
| R18-10 | La rendición del efectivo cuadra el mismo día y toda diferencia queda explicada con causal tipificada. | En operación desde el mes 16. | Cuadratura por camión entre monto esperado y recaudado al retorno, con bloqueo del cierre ante saldo sin justificar. Elimina el descuadre de $4,2 millones mensuales sin investigar. |
| R18-11 | El costo de servir se conoce por cliente y por entrega, construido desde los hechos operacionales. | Con la producción de la Etapa 2, mes 21. | Costeo de cada entrega desde kilómetros, tiempo de conducción y de descarga y peajes reales; consolidación mensual y matriz de rentabilidad por cliente. Reemplaza el prorrateo por zona de 2016. |
| R18-12 | El parque de envases retornables se controla por cuenta corriente por cliente y la pérdida baja al 7 % anual o menos. | Control desde el mes 16; meta anual consolidada al mes 12 de operación. | Saldo por cliente actualizado en cada entrega y devolución, y reporte diario de pérdida por cliente, tipo y zona. Línea base: 14 %. |
| R18-13 | Los pedidos del canal moderno entran por vía electrónica estructurada, sin digitación, y se responde con aviso de despacho. | Con la Etapa 2, mes 21, y en producción antes de enero de 2029. | Porcentaje de pedidos de cadenas recibidos por intercambio electrónico y resueltos contra el maestro por equivalencias, sin digitación manual, con aviso de despacho transmitido. |
| R18-14 | La ocupación de los camiones sube al 75 % o más y ningún camión sale bajo el umbral de 65 % sin alerta. | Con la producción de la Etapa 2, mes 21. | Ocupación por camión y por ruta alimentada por la telemetría, con alerta bajo el umbral declarado. Línea base: 68 %, con días de 41 %. |
| R18-15 | La causa de cada faltante queda registrada en el momento en que se produce. | En operación desde el mes 16. | Porcentaje de registros de faltante con causal obligatoria en la preparación. |
| R18-16 | El conocimiento de rutas queda codificado en el motor antes de la jubilación del planificador, sin que la operación se resienta. | Captura durante la Etapa 1, meses 1–15, antes de su fecha de salida. | Sesiones de transferencia y parametrización validada del motor; cumplimiento de OTIF y de ocupación sin degradación durante sus ausencias. |

<a id="seccion-23"></a>

### Material recibido: rf

Origen de esta tabla: 03_esquema_solucion_alcance/tablas_anexo/rf.tex.

<a id="tabla-3-a-24"></a>

**Tabla 3.A.24 — Catálogo de requerimientos funcionales (91 requerimientos)**

| **ID** | **Requerimiento** | **Épica** | **Etapa** | **Prioridad** | **Origen** |
| --- | --- | --- | --- | --- | --- |
| RF-01.02 | Registro obligatorio del lote del proveedor (AI 10) en recepción | Abastecimiento y Recepción | Etapa 1 | Muy Alta | Cap. 4.1, 4.9 y 7.3 |
| RF-01.03 | Registro de fecha de vencimiento vinculada al lote | Abastecimiento y Recepción | Etapa 1 | Muy Alta | Cap. 4.1 y 4.8 |
| RF-01.04 | Registro de no conformidades en recepción (con fotografía) | Abastecimiento y Recepción | Etapa 1 | Alta | Cap. 4.1, 4.9, Cap. 8 (Calidad), RT-17.06 |
| RF-01.07 | Generación e impresión de etiqueta SSCC | Abastecimiento y Recepción | Etapa 1 | Media | Cap. 4.2, Cap. 12 (GS1), RT-05.23 |
| RF-01.10 | Gestión de fichas de producto (maestro interno autorizado) | Abastecimiento y Recepción | Etapa 1 | Muy Alta | Cap. 14.1, Cap. 8 (Hugo), Cap. 16.1 (Decisión 11) |
| RF-01.11 | Validación de compatibilidad térmica en putaway | Abastecimiento y Recepción | Etapa 1 | Muy Alta | Cap. 2.3, 4.9 y 10 (Restricción 2) |
| RF-02.01 | Configuración de topología de instalaciones | Almacén e Inventario | Etapa 1 | Muy Alta | Cap. 2.3, RT-02.12 |
| RF-02.02 | Consolidación de stock físico multi-sitio | Almacén e Inventario | Etapa 1 | Alta | Cap. 2.3 |
| RF-02.03 | Reasignación de ubicaciones (slotting) | Almacén e Inventario | Etapa 1 | Muy Alta | Cap. 8 (Ximena) |
| RF-02.04 | Conteo cíclico en modo ciego | Almacén e Inventario | Etapa 1 | Alta | Cap. 4.2 y 14.1 |
| RF-02.05 | Cálculo de stock disponible para la venta | Almacén e Inventario | Etapa 1 | Alta | Cap. 16.1 (Decisión 8) |
| RF-02.08 | Gestión FEFO y alertas de vida útil | Almacén e Inventario | Etapa 1 | Muy Alta | Cap. 4.2 y 4.8 |
| RF-02.10 | Ficha de trazabilidad de lote | Almacén e Inventario | Etapa 1 | Muy Alta | Cap. 1, 4.9 y 9.5 |
| RF-03.02 | Consulta de stock disponible sin conectividad | Preventa | Etapa 1 | Muy Alta | Cap. 16.1 (Decisión 8), RT-03.10 |
| RF-03.03 | Reserva de stock al confirmar el pedido | Preventa | Etapa 1 | Alta | Cap. 16.1 (Decisión 8) |
| RF-03.04 | Consulta de crédito y deuda vencida en línea | Preventa | Etapa 1 | Muy Alta | Cap. 9.4 (crédito) |
| RF-03.05 | Consulta de crédito y deuda vencida sin conectividad | Preventa | Etapa 1 | Muy Alta | Cap. 9.4, RT-03.10 |
| RF-03.07 | Aplicación de promociones vigentes a una línea de pedido | Preventa | Etapa 1 | Alta | Cap. 4.7 y 9.7 |
| RF-03.10 | Autorización de excepción por supervisor de crédito (registrada) | Preventa | Etapa 1 | Alta | Cap. 16.1 (Decisión 8) |
| RF-03.11 | Cobro por defecto del precio vigente al despacho | Preventa | Etapa 1 | Muy Alta | Cap. 16.1 (Decisión 9) |
| RF-03.12 | Excepción de precio por cliente o cadena (precio de la toma) | Preventa | Etapa 1 | Alta | Cap. 16.1 (Decisión 9) |
| RF-03.13 | Alerta al cliente por cambio de precio | Preventa | Etapa 1 | Alta | Cap. 16.1 (Decisión 9) |
| RF-03.14 | Información de la ventana de entrega comprometible | Preventa | Etapa 1 | Alta | Cap. 9.1 y 9.9 |
| RF-03.15 | Sugerencia de reposición al preventista | Preventa | Etapa 1 | Alta | Cap. 9.10 (vacío V-01) |
| RF-03.16 | Identificador único de pedido offline y descarte de duplicados | Preventa | Etapa 1 | Muy Alta | Cap. 16.1 (Decisión 8), Cap. 18 (criterio 6) |
| RF-04.01 | Asignación y secuenciación automática de rutas | Planificación de Rutas | Etapa 1 | Alta | Cap. 4.4, Cap. 18 (criterio 7) |
| RF-04.02 | Modificación manual de rutas y recálculo de ETA | Planificación de Rutas | Etapa 1 | Media | Cap. 8 (planificador), Cap. 16.1 (Decisión 16) |
| RF-04.04 | Ajuste de secuencia de ruta por ventanas horarias | Planificación de Rutas | Etapa 1 | Alta | Cap. 9.1 y 9.9 |
| RF-04.06 | Notificación de hora estimada de llegada al cliente | Planificación de Rutas | Etapa 2 | Media | Cap. 9.9 |
| RF-04.07 | Parametrización de ventanas horarias por cliente | Planificación de Rutas | Etapa 1 | Alta | Cap. 9.1 y 9.9 |
| RF-04.08 | Cálculo integral del costo de entrega realizada | Planificación de Rutas | Etapa 2 | Alta | Cap. 9.8, Cap. 16.1 (Decisión 7) |
| RF-05.01 | Generación de misiones de picking | Preparación (Picking) y Carga | Etapa 1 | Muy Alta | Cap. 4.5 |
| RF-05.03 | Motivo obligatorio de faltante | Preparación (Picking) y Carga | Etapa 1 | Muy Alta | Cap. 8, Cap. 18 (criterio 15) |
| RF-05.07 | Carga dirigida inversa a ruta | Preparación (Picking) y Carga | Etapa 1 | Alta | Cap. 4.5, Cap. 18 (criterio 14) |
| RF-06.02 | Captura de firma digital del receptor | Transporte, Entrega y POD | Etapa 1 | Muy Alta | Cap. 9.9, RT-16.14 |
| RF-06.03 | Reporte de rechazo de productos | Transporte, Entrega y POD | Etapa 1 | Media | Cap. 4.6 y 4.8 |
| RF-06.04 | Reporte de local cerrado y reagendamiento automático | Transporte, Entrega y POD | Etapa 1 | Media | Cap. 16.1 (Decisión 3) |
| RF-06.05 | Registro de recaudación de pagos en efectivo | Transporte, Entrega y POD | Etapa 1 | Muy Alta | Cap. 4.7 |
| RF-06.08 | Autenticación del conductor externo por OTP | Transporte, Entrega y POD | Etapa 1 | Alta | Restricción 6, RT-12.11, Cap. 16.1 (Decisión 5) |
| RF-06.09 | Captura de devolución de envases retornables | Transporte, Entrega y POD | Etapa 1 | Alta | Cap. 4.8 y 9.7, Cap. 18 (criterio 12) |
| RF-06.11 | Confirmación de recepción mediante QR | Transporte, Entrega y POD | Etapa 1 | Media | Cap. 16.1 (Decisión 15) |
| RF-06.12 | Confirmación de recepción sin conectividad (firma o fotografía) | Transporte, Entrega y POD | Etapa 1 | Media | Cap. 16.1 (Decisión 15) |
| RF-06.13 | Impresión de comprobante térmico en terreno | Transporte, Entrega y POD | Etapa 1 | Media | RT-17.06 |
| RF-07.02 | Rendición digital individual de efectivo | Cobranza y Efectivo | Etapa 1 | Muy Alta | Cap. 4.7, Cap. 18 (criterio 10) |
| RF-07.03 | Registro obligatorio de causales de descuadre en caja | Cobranza y Efectivo | Etapa 1 | Muy Alta | Cap. 4.7 y 9.7, Cap. 18 (criterio 10) |
| RF-07.06 | Cobro con terminal POS móvil en ruta | Cobranza y Efectivo | Etapa 1 | Alta | RT-17.06, Cap. 9.7 |
| RF-07.10 | Registro de abonos y pagos parciales en la entrega | Cobranza y Efectivo | Etapa 1 | Alta | Cap. 4.7 |
| RF-08.01 | Registro de devoluciones en ruta (modo offline) | Logística Inversa | Etapa 1 | Muy Alta | Cap. 4.6 y 4.8, RT-17.01 |
| RF-08.02 | Gestión del destino de productos devueltos | Logística Inversa | Etapa 1 | Muy Alta | Cap. 4.8, Cap. 10 (Restricción 4) |
| RF-08.03 | Gestión de cuenta corriente de envases retornables | Logística Inversa | Etapa 1 | Alta | Cap. 4.8 y 9.7, Cap. 16.1 (Decisión 10) |
| RF-08.04 | Alertas por exceso de envases retornables | Logística Inversa | Etapa 1 | Alta | Cap. 4.8 y 9.7 |
| RF-08.05 | Registro de mermas por vencimiento (góndola incluida) | Logística Inversa | Etapa 1 | Alta | Cap. 4.8, Cap. 10 (Restricción 4) |
| RF-08.06 | Reporte de pérdida de envases retornables | Logística Inversa | Etapa 1 | Alta | Cap. 4.8, Cap. 18 (criterio 12) |
| RF-08.07 | Integración de devoluciones y mermas al costo de servir | Logística Inversa | Etapa 2 | Alta | Cap. 9.8 |
| RF-09.01 | Trazabilidad forward por lote (clientes afectados) | Trazabilidad y Cadena de Frío | Etapa 1 | Muy Alta | Cap. 1 y 9.6, Cap. 18 (criterio 1) |
| RF-09.02 | Trazabilidad backward por lote | Trazabilidad y Cadena de Frío | Etapa 1 | Muy Alta | Cap. 4.9 y 9.6 |
| RF-09.05 | Registro continuo y alerta de excursiones térmicas | Trazabilidad y Cadena de Frío | Etapa 1 | Muy Alta | Cap. 8 (Calidad), Cap. 16.1 (Decisión 4) |
| RF-09.06 | Parámetros configurables de la excursión térmica | Trazabilidad y Cadena de Frío | Etapa 1 | Media | Cap. 8 (Calidad vs Operaciones), Cap. 16.1 (Decisión 4) |
| RF-09.07 | Decisión de bloqueo o liberación del despacho (no automática) | Trazabilidad y Cadena de Frío | Etapa 1 | Muy Alta | Cap. 4.9 y 8, Cap. 16.1 (Decisión 4) |
| RF-09.09 | Generación de cumplimiento de cadena de frío | Trazabilidad y Cadena de Frío | Etapa 1 | Muy Alta | Cap. 4.9, Cap. 18 (criterio 3) |
| RF-11.02 | Cálculo del costo de servir por entrega y por cliente | Costo de Servir e Indicadores | Etapa 2 | Muy Alta | Cap. 4.4, 7.2 y 9.8, Cap. 18 (criterio 11) |
| RF-11.03 | Cálculo diario unificado del indicador OTIF | Costo de Servir e Indicadores | Etapa 1 | Muy Alta | Cap. 7.1 y 9.1, Cap. 18 (criterio 4) |
| RF-11.04 | Medición de Fill Rate y Perfect Order con el POD móvil | Costo de Servir e Indicadores | Etapa 1 | Muy Alta | Cap. 7.1, 9.4 y 16.2, Cap. 18 (criterio 8) |
| RF-11.05 | Monitoreo y alerta de ocupación de flota | Costo de Servir e Indicadores | Etapa 2 | Alta | Cap. 4.4 y 7.2, Cap. 18 (criterio 14) |
| RF-11.06 | Tablero de control operacional en tiempo real | Costo de Servir e Indicadores | Etapa 2 | Alta | RT-05.29, Cap. 9.1 y 9.6 |
| RF-11.08 | Segmentación de clientes por rentabilidad neta | Costo de Servir e Indicadores | Etapa 2 | Alta | Cap. 7.2 y 9.8, Cap. 16.1 (Decisión 7) |
| RF-12.01 | Recepción de pedido electrónico | Canal Moderno (EDI) y Portales | Etapa 2 | Alta | Cap. 9.9, RT-05.23 |
| RF-12.03 | Resolución del código de producto contra el maestro de Puelche | Canal Moderno (EDI) y Portales | Etapa 2 | Alta | Cap. 16.1 (Decisión 11) |
| RF-12.06 | Gestión de excepciones de pedidos EDI inválidos | Canal Moderno (EDI) y Portales | Etapa 2 | Alta | Cap. 17.1/ 17.2 |
| RF-12.09 | Envío de aviso de despacho anticipado (ASN) | Canal Moderno (EDI) y Portales | Etapa 2 | Alta | Cap. 9.9 (entrevista Rubén Salinas) |
| RF-12.10 | Planificación de la llegada dentro de la ventana de 30 minutos | Canal Moderno (EDI) y Portales | Etapa 2 | Alta | Cap. 9.9 |
| RF-12.12 | Captura de evidencia de entrega en canal moderno | Canal Moderno (EDI) y Portales | Etapa 2 | Alta | Cap. 9.9, Cap. 16.1 (Decisión 15) |
| RF-12.13 | Envío de acuse de recibo digital al cliente | Canal Moderno (EDI) y Portales | Etapa 2 | Alta | Cap. 9.9 |
| RF-12.21 | Confirmación diaria de conductor y vehículo | Canal Moderno (EDI) y Portales | Etapa 2 | Media | Cap. 16.1 (Decisión 5) |
| RF-12.25 | Registro de cliente en el portal | Canal Moderno (EDI) y Portales | Etapa 2 | Muy Alta | RT-12.12 |
| RF-12.26 | Inicio de sesión en el portal de clientes | Canal Moderno (EDI) y Portales | Etapa 2 | Muy Alta | RT-12.12 |
| RF-12.27 | Recuperación de contraseña | Canal Moderno (EDI) y Portales | Etapa 2 | Alta | RT-12.12 |
| RF-13.02 | Declaración y justificación del emplazamiento por componente | Emplazamiento | Ambas | Alta | RT-03.01, RT-06.01 |
| RF-14.01 | Integración con telemetría de camiones propios | Flota y Telemetría | Etapa 2 | Muy Alta | Cap. 5, RT-17.06 |
| RF-14.02 | Visualización de rutas planificadas vs reales | Flota y Telemetría | Etapa 2 | Alta | Cap. 3 y Cap. 8 (Nelson) |
| RF-14.04 | Integración de telemetría con el costo de servir | Flota y Telemetría | Etapa 2 | Muy Alta | Cap. 9.8 |
| RF-14.05 | Vinculación conductor-camión en cada viaje | Flota y Telemetría | Etapa 2 | Alta | Cap. 16.1 (Decisión 5), Cap. 4.6 |
| RF-14.07 | Identificación del conductor (PIN o QR) al iniciar la ruta | Flota y Telemetría | Etapa 1 | Alta | Restricción 10, RT-12.11 |
| RF-14.08 | Gestión de geocercas para control de llegada/ salida | Flota y Telemetría | Etapa 2 | Alta | RT-14, acuerdo sindical |
| RF-15.01 | Identidad centralizada con SSO y directorio | Identidad y Accesos | Etapa 1 | Muy Alta | Art. 22, RT-12.07 |
| RF-15.02 | Alta de usuarios y gestión de credenciales | Identidad y Accesos | Etapa 1 | Muy Alta | Art. 22, RT-12.07, RT-12.12 |
| RF-15.03 | MFA para el acceso externo y privilegiado | Identidad y Accesos | Etapa 1 | Muy Alta | Art. 22, RT-12.11 |
| RF-16.01 | Observabilidad unificada de nube y on-premise | Observabilidad | Etapa 1 | Muy Alta | Art. 16.4, RT-03.16 |
| RF-16.03 | Alertas por síntomas de negocio | Observabilidad | Etapa 1 | Muy Alta | RNF-21, Cap. 17 |
| RF-18.01 | Firma electrónica avanzada (Ley 19.799) para los actos que el caso exige | Firma Electrónica | Etapa 2 | Alta | RT-16.14, Cap. 9.9 |

<a id="seccion-24"></a>

### Material recibido: rnf

Origen de esta tabla: 03_esquema_solucion_alcance/tablas_anexo/rnf.tex.

<a id="tabla-3-a-25"></a>

**Tabla 3.A.25 — Catálogo de requerimientos no funcionales (41 requerimientos)**

| **ID** | **Requerimiento** | **Objetivo / valor comprometido** | **Origen** |
| --- | --- | --- | --- |
| RNF-01.02 | Retención de registros de recepción | Trazabilidad sanitaria y no conformidades: mínimo 5 años; documentos con efecto tributario: mínimo 6 años | Cap. 7, RT-16.10 |
| RNF-02.01 | Operación autónoma del centro de distribución | Almacén funciona mínimo 24 h continuas sin enlace; sincronización ≤ 2 h con resolución determinista de conflictos | Cap. 10 (Restricción 2), RT-03.10, RT-03.13 |
| RNF-04.01 | Tiempo del motor de ruteo | Asignación y secuencia completa en menos de 20 minutos | Cap. 18 (criterio 7), Cap. 8 |
| RNF-05.01 | Latencia de confirmación de picking | ≤ 1 s por línea (conectado y offline, incluida la cámara a -22 °C) | RT-09.01 |
| RNF-05.02 | Operabilidad con guantes térmicos | Elementos interactivos ≥ 15 × 15 mm, sin gestos complejos; dispositivo funcional 30 min a -22 °C | RT-13.08, RT-12.11, Cap. 10 (Restricción 7) |
| RNF-05.03 | Curva de aprendizaje | ≤ 2 horas; misión de ≥ 20 líneas con ≤ 5 % de error medido en 3 operarios nuevos | Cap. 4.2, Cap. 8 (Ximena) |
| RNF-06.01 | Persistencia local de la ruta | 100 % de los datos cifrados en local; operación completa de ≥ 14 h sin cobertura | Cap. 6, RT-03.10 |
| RNF-06.02 | Duración del token sin conexión por perfil | 8 h (turno de bodega) y 14 h (reparto y preventa), renovado al inicio del turno | Art. 22, RT-12.07, RT-12.11, RT-12.12 |
| RNF-08.02 | Retención de devoluciones y mermas | Trazabilidad sanitaria: mínimo 5 años; notas de crédito asociadas: mínimo 6 años | Cap. 7, RT-16.10 |
| RNF-09.01 | Respuesta a retiro sanitario | Listado de clientes afectados por lote en menos de 2 horas, con evidencia exportable | Cap. 18 (criterio 1) |
| RNF-09.02 | Retención de trazabilidad sanitaria | Vida útil del producto + 6 meses, con piso mínimo de 5 años | Cap. 9.6, RT-16.10 |
| RNF-09.04 | Operación sin señal en cámaras de frío | Sin pérdida de lecturas; sincronización del 100 % del historial al reconectar | RT-03.10 |
| RNF-11.01 | Latencia de tableros operacionales | Indicadores del día desplegados ≤ 5 minutos desde la ingesta | RT-09.01 |
| RNF-11.02 | Desacople OLAP/ BI del OLTP | Cero degradación de picking (≤ 1 s) y preventa (≤ 1,5 s) bajo reportes masivos | Cap. 15 (volumetría) |
| RNF-12.01 | Hito de producción del canal moderno | EDI y portal de autoatención en producción antes de enero de 2029 | Cap. 2.1, RT-12 |
| RNF-13.01 | Operación autónoma degradada del CD | 24 h ante pérdida total del enlace | Cap. 10 (Restricción 2) |
| RNF-13.02 | Declaración de funciones no disponibles en desconexión | Lista explícita por modo (CD de 24 h y terreno de 14 h) con procedimiento suplente | RT-03.13 |
| RNF-13.03 | Redundancia de equipos críticos on-premise | Equipos críticos redundantes en los sitios | RT-03.14 |
| RNF-13.04 | Tolerancia a falla de disco | Almacenamiento que tolere la falla de al menos un disco | RT-03.14 |
| RNF-13.05 | Declaración del nivel RAID | Nivel declarado y justificado frente a alternativas | RT-03.14 |
| RNF-13.07 | Enlace redundante | Caminos físicos y proveedores distintos; conmutación automática ≤ 5 min | RT-03.17 |
| RNF-13.08 | Dimensionamiento del ancho de banda | Régimen y peak (septiembre) por sitio | RT-03.23 |
| RNF-13.09 | Estudio de cobertura inalámbrica | Incluye cámaras de refrigerado y congelado, con solución técnica propuesta | RT-03.23 |
| RNF-14.01 | Privacidad de la geolocalización de personas | Retención 12 meses; sin replicación transfronteriza; solo por acuerdo sindical | Ley 21.719, Cap. 10 (Restricción 10) |
| RNF-16.03 | Limitación de categorías de datos sensibles | No se crean nuevas categorías de datos sensibles con la captura en terreno | Ley 21.719 |
| RNF-19.01 | Cálculo de capacidad | Usuarios concurrentes y TPS declarados con la volumetría del caso | RT-09.05, Cap. 14.2 |
| RNF-19.02 | Escalamiento horizontal automático | Capas de aplicación e integración | RT-09.05 |
| RNF-19.03 | Identificación del cuello de botella | Punto de saturación del peak de septiembre declarado y monitoreado | RT-09.05, Cap. 14.2 |
| RNF-19.04 | Pruebas de carga y estrés | Carga a 1,5 × peak; estrés hasta el punto de quiebre | RT-09.05, Transversales S 20.1 |
| RNF-20.04 | Pruebas de resiliencia | Validación de la operación degradada | Transversales S 20.1 |
| RNF-20.06 | Recuperación ante desastres | RTO ≤ 4 h y RPO ≤ 15 min; pruebas de conmutación ≥ 2 veces al año | BA Art. 20, RT-07.07 |
| RNF-20.07 | Política de respaldo | Regla 3-2-1-1-0 con pruebas mensuales de restauración | RT-07.07 |
| RNF-21.01 | Centro de operaciones (NOC) | Monitoreo 24 × 7 × 365 | Cap. 17, RNF-21 |
| RNF-21.03 | Umbrales de atención de la mesa de ayuda | 80 % de llamadas atendidas en 20 s; 70 % de resolución al primer contacto | RT-21 |
| RNF-21.04 | Cobertura horaria de soporte | 24 × 7 para incidentes críticos y para la ventana de despacho 05:30–07:00 | RT-21, Cap. 10 (Restricción 1) |
| RNF-21.05 | Dimensionamiento de la mesa de ayuda | Fundamento cuantitativo con Erlang C | RT-21 |
| RNF-21.06 | Canal único con ticket | Ticket único con seguimiento y escalamiento | RT-21 |
| RNF-21.07 | Traslado de especialistas a sitios alejados | Curicó, Chillán y Los Ángeles incluido en la oferta | RT-21.16 |
| RNF-22.03 | Capacitación sin detener la operación | Programada sobre los turnos, sin pausa operacional | RT-20 |
| RNF-22.04 | Certificación de administradores y técnicos | Antes del cierre de cada hito y de cada oleada | RT-20 |

<a id="seccion-25"></a>

### Material recibido: supuestos

Origen de esta tabla: 03_esquema_solucion_alcance/tablas_anexo/supuestos.tex.

<a id="tabla-3-a-26"></a>

**Tabla 3.A.26 — Registro de supuestos: descripción, consecuencia si es incorrecto y origen (47 filas)**

| **Supuesto** | **Descripción** | **Caso si supuesto es incorrecto** | **Origen** |
| --- | --- | --- | --- |
| Entrega cumplida (OTIF) | El indicador de entregas completas y a tiempo (OTIF) medirá el éxito basándose únicamente en el cumplimiento del 100 % de ítems y unidades dentro de la franja horaria acordada (ventana de 30 minutos). Toda entrega parcial o fuera de la ventana penaliza el indicador de servicio. | El indicador no refleja el desempeño real (una parcial aparecería como cumplida) y la base de cálculo sería discutible en la evaluación. | Decisión 1, RF-11.03/ 11.04, RF-12.10 |
| Local cerrado o ausencia del cliente | Ante un local cerrado en la ventana comprometida, el conductor reporta «local cerrado», el sistema registra el envío fallido y lo reagenda automáticamente a la ventana más cercana del cliente. Si persiste la indisponibilidad, la mercadería regresa al CD. Prohibido entregar a vecinos o terceros; el conductor no decide. | Las reentregas quedan fuera de control y vuelve el criterio individual de cada conductor (causa actual de reentregas). | Decisión 3, RF-06.04 |
| Gestión de pagos en efectivo | El efectivo representa el 38 % de las ventas del canal tradicional y produce diferencias mensuales de rendición de $4,2 millones. Se mantiene como medio de pago, ofreciendo alternativas de reducción (encargo por web y POS móvil), con módulo de reparto que cuadra montos recaudados contra despachos (asíncrono) y causales tipificadas de descuadre. | Los $4,2 M/ mes de descuadre persisten y se arriesga excluir a los clientes que solo pagan en efectivo; inseguridad del dinero en ruta. | Decisión 6 (Cap. 4.7, 9.7), RF-07.02/ 07.03/ 07.06 |
| Asignación de inventario concurrente | El stock de los 8.400 SKU activos se reserva al confirmar el pedido en el servidor central, por orden de llegada. En modo offline el stock es indicativo con antigüedad visible; al sincronizar, los conflictos se resuelven por orden cronológico de captura y las líneas sin stock se marcan «sin stock» con aviso al preventista. | Doble compromiso de stock y quiebres de pedido no informados a tiempo. | Decisión 8, RF-03.03, RF-02.05, RF-05.03 |
| Envases retornables | El parque de 68.000 canastillos y 9.400 pallets se controla por cuentas corrientes de saldo por cliente y por transportista (descuenta en cada entrega, suma en cada devolución), no por serialización unitaria, con alerta por umbral y reporte diario de pérdida. | Se mantiene la pérdida del 14 % anual y no hay trazabilidad del activo retornable. | Decisión 10, RF-08.03/ 08.04/ 08.06, RF-06.09 |
| Alteración de precios | Por defecto se cobra el precio ofrecido por los preventistas de cada línea (RF-03.11). Solo con excepción configurada por cliente o cadena se respeta el precio tomado en preventa (RF-03.12), alertando al cliente ante el cambio (RF-03.13). | Facturación inconsistente y desconfianza del preventista/ cliente si se asume «cobrar siempre el precio vigente al despacho». | Decisión 9, RF-03.11/ 03.12/ 03.13 |
| Sistema de Gestión de Almacenes (WMS) | El WMS de 2013 que opera en Talca se reemplaza íntegramente por el módulo de la solución, unificando Concepción y los tres cross-docking bajo un único estándar de control y trazabilidad, con migración de datos históricos y plan de reversión. | Se mantiene el archipiélago de WMS/ planillas por sitio y no se alcanza el control y la trazabilidad exigidos. | Decisión 14, RF-02.xx, RT-05.11 a 05.15 |
| Trazabilidad sanitaria | La unidad de trazabilidad obligatoria (proveedor lácteo y autoridad) es el lote del proveedor (AI 10) con su fecha de vencimiento. El SSCC identifica la unidad logística física (pallet), pero el retiro y las trazabilidades forward/ backward se resuelven por lote. Se descarta la serialización unitaria. | La volumetría transaccional se dispara (2,4 M de unidades mensuales) y la respuesta a retiro &lt; 2 h se degrada si se busca por caja/ SSCC. | Decisión 2, RF-01.02/ 01.07/ 02.10/ 09.01 |
| Cadena de frío y excursiones térmicas | La excursión se define como un umbral parametrizable de tiempo y grados por tipo de producto, configurado por la jefa de calidad (RF-09.06). Valor de referencia inicial: desviación &gt; 2 °C por más de 15 minutos. El sistema alerta en tiempo real (RF-09.05) y habilita el bloqueo, pero la decisión de liberar/ bloquear/ rechazar no es automática (RF-09.07). | Sin regla escrita, el control de calidad no puede ejercerse y cada excursión se resuelve según criterio de terreno. | Decisión 4, RF-09.05/ 09.06/ 09.07, RSA DS 977 |
| Identificación de flota externa | Los 160 conductores de las 10 empresas transportistas acceden con dispositivo gestionado y autenticación rápida OTP (RF-06.08) o PIN/ QR al iniciar la ruta (RF-14.07); la empresa confirma diariamente conductor y vehículo en el portal antes de la ventana de despacho (RF-12.21), quedando registrada la vinculación conductor–camión del viaje. | Los conductores quedan no identificables al rotar sin aviso (situación actual) y la auditoría del viaje es imposible. | Decisión 5, RF-06.08, RF-14.07, RF-12.21 |
| Monitoreo y objeción sindical | La telemetría y el posicionamiento serán de uso exclusivamente operacional (datos del vehículo y la ruta: posición, velocidad, kilometraje). No se incorporan cámaras en cabina; el uso del GPS para control de jornada solo procede con acuerdo sindical y protección de la privacidad del conductor. | Riesgo de conflicto laboral y de incumplir la Restricción N.<sup>o</sup> 10; el monitoreo quedaría limitado a datos de vehículo/ ruta. | Decisión 13, RF-14.01/ 04/ 05/ 08, Restricción N.<sup>o</sup> 10 |
| Cálculo del costo de servir | El modelo prorrateado de 2016 se sustituye por un costeo basado en actividades (ABC): consume kilómetros de la telemetría, tiempos de descarga en el local, porcentaje volumétrico del pedido y la tasa de entregas, imputando directos e indirectos por entrega y por cliente. | El costo por entrega sigue siendo prorrateo histórico y las decisiones comerciales no se sustentan. | Decisión 7, RF-11.02, RF-04.08 |
| Prueba de entrega alternativa | La prueba de entrega es la firma en pantalla del titular. Cuando quien recibe no es el titular, no sabe firmar o se niega, se captura evidencia alternativa vinculada a la GDE: fotografía + nombre del receptor o código QR, con comprobante térmico portátil para el canal tradicional. La firma electrónica avanzada (Ley 19.799) se reserva solo a los actos que el caso exige; la evidencia alternativa no equivale a firma avanzada. | El acuse de recibo pierde validez y el POD es discutible ante un reclamo. | Decisión 15 y 38, RF-06.02/ 06.11/ 06.12/ 06.13, RF-12.12/ 12.13 |
| Conectividad de terreno | Los cortes de conectividad nominales se acotan a ≈2 horas; el diseño de contingencia garantiza operar un turno completo de 14 h sin señal en preventa y reparto (las 24 h del CD se cubren con el supuesto S-41), con sincronización del 100 % al reconectar. | Si los cortes exceden 14 h, la operación degradada no puede sostener el volumen del turno y se acumulan sincronizaciones. | Cap. 6/ 8, RT-03.10, Restricción N.<sup>o</sup> 3 (cap. 10) |
| Integración con el ERP (2017) | El ERP no se reemplaza ni se modifica; se dispone de una API o capa de integración accesible que la solución usa para leer maestros (productos, clientes, crédito) y entregar preventa, inventario, POD y recaudación, manteniendo el ERP como único emisor tributario. | Si la API no existe o es insuficiente, se requieren adaptadores ETL/ antigüedad adicionales, con impacto en costo y cronograma. | Restricción N.<sup>o</sup> 4 (cap. 10), Decisión 32, RT-05.20 |
| Datos del WMS de 2013 | El WMS de 2013 permite exportación de solo lectura de los datos históricos necesarios para la migración (maestros, inventario y trazabilidad mínima), con calidad declarada por dominio. | Si los datos no son extraíbles o están deteriorados, la migración exige reconciliación manual y afecta el plan de la Épica 2. | Decisión 14, RT-05.11 a 05.15 |
| Composición de la flota (camiones ≠ conductores) | La flota se compone de 42 camiones propios (4–18 t, 18 con frío) y 54 camiones de transportistas contratados (10 empresas, 10 con frío) = 96 camiones en la ventana de despacho (Restricciones N.<sup>o</sup> 1 y 6). Conductores: 84 propios y peonetas (S2.4) frente a los «42 propios» que la Tabla 14.1 anota en la fila Conductores (cifra que coincide con los camiones, no con los conductores) y ≈160 de terceros; totales ≈200 (Tabla 14.1) vs ≈244 (S2.4). La composición exacta se declara como supuesto y se valida en consulta (Art. 43.3): camiones ≠ conductores. | Un dimensionamiento errado de dispositivos, licencias y autenticación (OTP/ PIN-QR) deja flota sin cobertura o costos excesivos. | Decisión 5, 2.3/ 2.4, Tabla 14.1 |
| Régimen de jornada del transporte | La planificación de rutas respeta el régimen especial de jornada de los trabajadores del transporte (horas de conducción y descanso); el motor de ruteo parametriza estos límites como restricciones de factibilidad. | Una ruta inviable por jornada genera reentregas y riesgo de sanción laboral. | investigación 16.2 N.<sup>o</sup> 10, RF-04.01 |
| Ventanas de congelamiento | No se interviene producción del 1 al 25 de septiembre, durante todo diciembre ni en los tres primeros días hábiles de cada mes (peak y cierre contable); los despliegues se programan fuera de esas ventanas. | Un despliegue en peak detiene la operación y la facturación; incumplimiento contractual. | Restricción N.<sup>o</sup> 8 (cap. 10), Cap. 13.2 |
| Ventana crítica de despacho | La ventana de despacho 05:30–07:00 opera con cero indisponibilidad; el cutover on-premise (&lt; 24 h) y los cambios críticos se ejecutan fuera de esa ventana. | Un sistema indisponible en esa ventana equivale a un día completo sin operación. | Restricción N.<sup>o</sup> 1 (cap. 10), RT-03.10 |
| Hardware de terreno | Los dispositivos rugged (bodega, preventa, reparto), escáneres GS1, impresoras térmicas Bluetooth y sensores de temperatura se adquieren con lead time compatible con los hitos de marcha blanca, con soporte del fabricante cubierto los 56 meses. | Atrasos de adquisición retrasan las oleadas de puesta en producción; hardware sin soporte incumple el Cap. 1.6. | Cap. 8 (BTT: especificación del hardware y dispositivos de terreno), Cap. 1.6 (soporte de fabricante 56 meses) |
| Operación a -22 °C | Existen terminales rugged en el mercado capaces de operar a -22 °C con guantes térmicos y confirmación de picking ≤ 1 s dentro de la cámara (escaneo GS1). | Si el hardware no tolera -22 °C, el picking de congelados no puede digitalizarse y se mantiene la hoja impresa. | Cap. 8, RNF-05.01/ 05.02, Restricción N.<sup>o</sup> 7 |
| Capacitación y curva de aprendizaje | Preventistas, conductores y preparadores completan una capacitación breve (curva de aprendizaje ≤ 2 h); la alta rotación (38 % anual en bodega) se absorbe con sesiones de re-capacitación continua sin detener la operación. | Interfaces complejas o capacitación insuficiente provocan rechazo, errores de bodega y descuadres de caja. | Restricción N.<sup>o</sup> 11 (cap. 10), RT-22.04, RNF-05.03, RNF-22.03/ 22.04 |
| Canal moderno y EDI | A partir de enero de 2029 operan las integraciones EDI con los ≈500 puntos del canal moderno (cadenas de supermercados), en los formatos y por los intermediarios que exigen las cadenas; el canal queda en producción antes de esa fecha. | Puelche no cumple las condiciones comerciales del canal moderno y pierde el ≈11 % de sus ventas (2029). | RNF-12.01, Cap. 9.11, investigación 16.2 N.<sup>o</sup> 2 |
| Volumetría de sistema (14.2) | Las 16 dimensiones de volumetría que el caso deja «a estimar» (TPS en régimen, en peak de despacho y de septiembre, usuarios concurrentes, dispositivos simultáneos, volúmenes de almacenamiento y migración, integraciones, ancho de banda, datos por turno sin señal, sincronización de flota, mesa de ayuda) se estiman y se declaran con su método y supuestos para el dimensionamiento. | Celdas vacías o valores sin derivación se evalúan como «dimensionamiento no realizado» (Cap. 14.2). | Cap. 14.2, RT-09.01, RNF-19.01 |
| Migración de datos históricos | La migración cubre: maestros completos; ventas y pedidos 3 años; inventario 2 años; trazabilidad sanitaria 5 años; cuentas por cobrar abiertas. Piso legal de retención: 5 años registros sanitarios y 6 años documentos tributarios, manteniéndose el ERP como fuente documental durante la cohabitación. | Huecos de trazabilidad sanitaria invalidan la respuesta a retiro &lt; 2 h y hay incumplimiento de retención normativa. | Decisión 32, RT-05.11 a 05.15, RNF-01.02/ 08.02/ 09.02 |
| Recuperación ante desastres | Sitio secundario activo-pasivo en la nube en región distinta, con RTO ≤ 4 h y RPO ≤ 15 min para servicios críticos y respaldo 3-2-1-1-0; pruebas de conmutación al menos 2 veces al año (restauración mensual). | Incumplimiento de los objetivos de continuidad y multas por indisponibilidad. | Decisión 27, RNF-20.06/ 20.07, RT-07.07, BA Art. 20 |
| Mesa de ayuda y soporte en terreno | Atención mínima 08:00–20:00 ampliada a 24×7 para incidentes críticos y para la ventana 05:30–07:00; 80 % de llamadas atendidas en 20 s y 70 % resolución al primer contacto; dotación dimensionada con Erlang C; traslado de especialistas a sitios alejados (Curicó, Chillán, Los Ángeles) incluido en la oferta. | La operación nocturna y los sitios alejados quedan sin soporte y un corte nocturno pasa inadvertido hasta la mañana. | Decisión 33, RNF-21.03/ 04/ 05/ 06/ 07 |
| Equipo TI del cliente (4 personas) | Toda función que requiera un especialista dedicado que el cliente no tiene se ofrece como servicio (mesa de ayuda, SRE, administración de nube) costeada en la oferta, en vez de cargar al equipo interno de 4 personas. | El equipo de TI de Puelche se satura y el servicio se degrada al término del contrato. | Restricción N.<sup>o</sup> 9 (cap. 10), Decisión 33, RNF-21 |
| Datos personales y estándares | El tratamiento de datos (14.200 clientes —muchos personas naturales— y geolocalización de terreno) se rige por la Ley N.<sup>o</sup> 21.719; la interoperabilidad usa los estándares GS1 (GTIN, SSCC, GLN, EPCIS) y la telemetría no geolocaliza al conductor fuera del vehículo sin acuerdo sindical. | Incumplimiento normativo (sanción), litigios sindicales y fallas de interoperabilidad con proveedores y canal moderno. | Ley 21.719 (BA), investigación 16.2 N.<sup>o</sup> 1 (GS1), Decisión 13 |
| Crédito y comportamiento de pago | El preventista ve en línea el nivel de crédito y la deuda vencida del cliente y, sin conectividad, un valor indicativo con antigüedad; la excepción de crédito la aprueba el supervisor y queda registrada (aprobada-diferida al sincronizar, con respaldo presencial). El sistema respeta la línea de crédito otorgada por finanzas, no la redefine. | Se despacha a clientes sin saldo, se generan quiebres de cartera y nuevos descuadres de recaudación. | Cap. 9.3/ 9.4, RF-03.05/ 03.06/ 03.09/ 03.10, Decisión 31 (RF-02.05, RF-03.10) |
| Promociones y descuentos en terreno | En el reparto solo se aplican las promociones vigentes del catálogo; el conductor no aplica descuentos libres en la entrega y toda diferencia de recaudación se explica con causal tipificada. | El «descuento de buena fe» sin registro perpetúa los $4,2 M/ mes de descuadre. | Cap. 4.7/ 9.7, Decisión 40, RF-03.07, RF-07.03, RF-03.10 |
| Maestro de productos | El maestro interno de Puelche prevalece como única fuente de productos y conserva el historial de cambios de GTIN/ SKU; todo código externo (proveedor o cadena) se resuelve por tabla de equivalencias por cadena y lo no resuelto queda en bandeja de excepciones. | El cambio de formato/ código del proveedor (frecuente con 8.400 productos) genera duplicados y pedidos con producto incorrecto. | Decisión 11, RF-01.04/ 01.10/ 12.03/ 12.06 |
| Cliente del canal tradicional | No se exige al cliente del canal tradicional internet, dispositivo propio ni medio de pago electrónico: la solución funciona con el cliente tal como opera (efectivo, sin conexión, sin firma digital). | Exigir cambios al cliente lo empuja a la competencia (la app del competidor) y rompe la relación comercial. | Restricción N.<sup>o</sup> 5 (cap. 10), Cap. 9.1 |
| Transferencia del planificador de rutas | Antes de la jubilación del planificador de rutas (≈2 años) se ejecutan sesiones de transferencia de conocimiento y parametrización de sus reglas (zonas, capacidades, ventanas, caminos) en el motor de ruteo, durante la Etapa 1. | El conocimiento crítico de rutas se pierde y el motor parte sin la experticia local (riesgo de continuidad con fecha conocida). | Decisión 16, RF-04.01/ 04.02/ 04.04, Cap. 9.2, BTC 13.1/ 17.3 |
| Reemplazo de planillas | La planilla de sugerencia de reposición del preventista y la planilla de rutas se reemplazan por funciones del sistema (RF-03.15, RF-04.01); sus datos históricos (frecuencias, rutas) están disponibles para la parametrización inicial. | Si la información histórica no se transfiere, el motor de ruteo y las sugerencias parten sin base y se pierde capacidad de reposición. | Cap. 9.10, Decisiones 23 y 16, RF-03.15, RF-04.01 |
| Línea base de indicadores | Los indicadores actuales del Cap. 18 (OTIF 82,4 %, fill rate 91,3 %, conteo cíclico 2,3 %, merma 1,7 %) se calculan con la misma metodología de medición que fijará el sistema, para comparar mejoras y certificar la línea base de cada meta. | Metas no comparables con el diagnóstico: la mejora se mide contra una base distinta y la evaluación lo descuenta. | Cap. 18, Decisión 21, RF-11.03/ 11.04 |
| Hora de corte y ventana comprometible | Cada zona comercial tiene una hora de corte del turno de preventa parametrizable: al cierre se disparan las misiones de picking y los pedidos posteriores entran al ciclo siguiente; el preventista informa la ventana de entrega comprometible de 30 minutos con aviso de ETA. | Sin hora de corte, el ciclo de preparación nocturna se desalinea y la promesa de entrega pierde validez. | Decisión 22, RF-03.14/ 04.06/ 04.07/ 05.01/ 12.10, Cap. 9.1/ 9.9 |
| Enlaces redundantes por sitio | Cada sitio on-premise dispondrá de enlace redundante con caminos físicos y proveedores distintos, con conmutación automática ≤ 5 min (incluye Concepción —hoy sin respaldo— y Los Ángeles, que pierde señal en su ventana de operación). | Un corte de enlace en la madrugada detiene la operación de un sitio y no hay forma de conmutar manualmente. | Cap. 6, Decisión 26, RT-03.17, RNF-13.07 |
| Integración de la telemetría actual | La plataforma actual de telemetría (tercero) expone por API la posición y velocidad de los 42 camiones propios y se integra como fuente; la cobertura de telemetría se extiende a los 54 camiones de transportistas. | El costo de servir en tiempo real (RF-11.02) y la alerta de desviación (RF-14.04) no pueden operar sin el dato del vehículo. | Cap. 8 (telemetría de flota), Decisión 13, RF-14.01/ 04/ 08 |
| Operación autónoma del CD (24 h) | El componente on-premise del centro de distribución opera de forma autónoma y degradada 24 horas continuas sin enlace a la nube (recepción, preparación y despacho), con el borde operacional y el stock local como respaldo. | La preparación nocturna y la carga se detienen ante un corte prolongado de fibra (la fibra se corta ≈4 veces al año). | Restricción N.<sup>o</sup> 2 (cap. 10), RT-03.10, RNF-02.01, Decisión 17 |
| Adecuación física de los recintos on-premise | La sala técnica principal de Talca (25 m<sup>2</sup>, no cumple el estándar) se adecúa; se habilita una sala secundaria en otro recinto para el respaldo; Concepción y las tres plataformas de cross-docking usan gabinetes de borde industrializados, igual que el borde operacional del CD. La tipología por sitio se declara en el padrón de emplazamiento. | Una tipología/ obra civil no declarada por sitio se evalúa como emplazamiento no resuelto (RT-06.01). | Cap. 6.1, Decisión 29, RT-06.01 |
| Autenticación y recuperación de credenciales | Los usuarios internos y del canal moderno usan SSO con recuperación por correo; los usuarios sin correo (conductores de transportistas, personal de terreno) se autentican y recuperan credenciales con factor presencial (OTP del jefe de flota o credencial inicial entregada en dotación). Todo acceso externo y privilegiado exige MFA. | Los conductores externos rotan sin aviso; sin factor presencial quedan bloqueados y el viaje no es auditable. | Decisión 34, RT-12.12, RF-15.01/ 02/ 03, RF-06.08 |
| Articulación tributaria POD ↔ GDE | El ERP/ GDE expone los servicios para consultar la guía de despacho electrónica y emitir la nota de crédito por la cantidad rechazada; el sistema registra la evidencia y no emite documentos tributarios por cuenta propia. | Sin esos servicios expuestos, la devolución en la entrega no se refleja tributariamente y aparecen «dos verdades». | Decisión 12, RF-06.03, RF-08.01/ 08.02, RNF-08.02, Restricción N.<sup>o</sup> 12 (cap. 10) |
| Puesta en producción por oleadas | La producción se despliega por oleadas (bodega → preventa → reparto → facturación/ ERP), avanzando solo cuando se cumplen los umbrales de marcha blanca (OTIF y fill rate) y la certificación de administradores y técnicos. | Un paso único afectaría simultáneamente bodega, preventa, reparto y facturación, sin reversión por oleada. | Decisión 36, RT-20.02/ 20.04, RNF-22.03/ 22.04, RF-11.03/ 11.04 |
| Nuevo CD en la Región de Los Lagos (2030) | La eventual incorporación de un nuevo centro de distribución (Los Lagos, hacia 2030) se resuelve por configuración y parametrización —sin desarrollo a medida— reutilizando las reglas de ruteo, preventa y reparto. | Si la solución no es replicable por configuración, el crecimiento futuro del cliente exige un rediseño. | RT-02.12, Decisión 37, RF-02.01/ 02.02 |

<a id="seccion-26"></a>

### Material recibido: trazabilidad

Origen de esta tabla: 03_esquema_solucion_alcance/tablas_anexo/trazabilidad.tex.

<a id="tabla-3-a-27"></a>

**Tabla 3.A.27 — Matriz de trazabilidad: origen, requisito, diseño y verificación**

| **Origen** | **Requisito(s)** | **Diseño (componente / capa)** | **Verificación (prueba / evidencia)** | **Criterio de aceptación** |
| --- | --- | --- | --- | --- |
| Cap. 4.1, 4.9 y 7.3; Cap. 10 (Restricción 2) | RF-01.02/ 01.03/ 01.04, RNF-01.02 | Servicio de recepción y maestro de producto; capa de datos (lotes AI 10 / SSCC) | Pruebas de recepción contra OC real y etiquetas GS1; prueba de retención de 5 años | R18-01, R18-02 |
| Cap. 16.1 (Decisión 8); Cap. 9.10; Cap. 10 (Restricción 3) | RF-03.02/ 03.03/ 03.15/ 03.16, RNF-06.01 | App móvil de preventa offline-first; colas de sincronización (capa de integración) | UAT con los 62 preventistas; prueba offline de 14 h; prueba de reconciliación y descarte de duplicados | R18-05, R18-06 |
| Cap. 18 (criterio 7); Cap. 8 (planificador) | RF-04.01/ 04.02/ 04.04/ 04.07, RNF-04.01 | Motor de ruteo en tarea por lotes en la nube, separado de la carga transaccional | Prueba de carga con el peak de septiembre (≈2.600 entregas / 96 vehículos); cronometraje &lt; 20 min; bitácora de correcciones | R18-07, R18-16 |
| Cap. 8 (Ximena); RT-09.01; Cap. 10 (Restricción 7) | RF-05.01/ 05.03/ 05.07, RNF-05.01/ 05.02/ 05.03 | Módulo de bodega y picking (on-premise en CD, terminales rugged) | Prueba de latencia en 100 escaneos; prueba en cámara a -22 °C con guantes; curva de aprendizaje con 3 operarios nuevos | R18-15 |
| Cap. 4.6, 4.8 y 9.9; Cap. 16.1 (Decisión 15); RT-16.14 | RF-06.02/ 06.03/ 06.04/ 06.11/ 06.12/ 06.13, RF-18.01 | App de reparto y POD; impresora térmica Bluetooth; articulación con la GDE | Pruebas de POD con firma, QR y fotografía en offline; prueba de acuse de recibo vinculado a la GDE | R18-08, R18-09 |
| Cap. 4.7 y 9.7; Cap. 10 (Restricción 6) | RF-07.02/ 07.03/ 07.06/ 07.10 | Módulo de rendición y recaudación; POS móvil | Cuadratura por camión en marcha blanca; prueba de bloqueo del cierre ante descuadre sin causal | R18-10 |
| Cap. 4.8 y 9.7; Cap. 16.1 (Decisión 10) | RF-08.03/ 08.04/ 08.06, RNF-08.02 | Cuenta corriente de envases retornables; capa de datos | Prueba de saldo por cliente tras entrega/ devolución; reporte diario de pérdida | R18-12 |
| Cap. 1, 4.9 y 9.6; RSA D.S. 977/ 96 | RF-09.01/ 09.02/ 09.09, RNF-09.01/ 09.02/ 09.04 | Eventos GS1 EPCIS en la capa de datos; registro continuo de temperatura | Ejercicio de retiro con lote trazado (&lt; 2 h); auditoría de la serie de temperatura por viaje | R18-01, R18-03 |
| Cap. 8 (Calidad vs Operaciones); Cap. 16.1 (Decisión 4) | RF-09.05/ 09.06/ 09.07 | Parámetros configurables de excursión; alertas en cabina y plataforma | Prueba de umbral paramétrico; prueba de decisión documentada de bloqueo/ liberación | R18-03 |
| Cap. 7.1 y 9.1; Cap. 18 (criterio 4) | RF-11.03/ 11.04, RNF-11.01/ 11.02 | Almacén analítico (OLAP) separado del transaccional (OLTP); tableros | OTIF y Fill Rate diarios durante la marcha blanca; prueba de cero degradación bajo reportes | R18-04 |
| Cap. 7.2 y 9.8; Cap. 16.1 (Decisión 7) | RF-11.02/ 11.06/ 11.08, RF-04.08 | Costeo ABC, tablero operacional y matriz de rentabilidad (Etapa 2) | Consolidación mensual del costo por entrega y por cliente | R18-11 |
| Cap. 9.9; RT-05.23; RNF-12.01 | RF-12.01/ 12.03/ 12.06/ 12.09/ 12.10/ 12.12/ 12.13 | Concentrador EDI con modelo canónico y portales (Etapa 2) | Pruebas de conexión contra el banco de pruebas de cada cadena; hito de producción antes de enero de 2029 | R18-13 |
| Cap. 16.1 (Decisión 5); Cap. 10 (Restricción 10) | RF-12.21, RF-06.08, RF-14.05/ 14.07, RNF-14.01 | Portal de transportistas; identidad externa con factor presencial (OTP) | Prueba de enrolamiento y autenticación de conductor externo ≤ 2 min; plan de acuerdo sindical | R18-14 |
| RT-03.10, RT-03.13 y RT-03.17; Cap. 10 (Restricción 2) | RNF-13.01/ 13.02/ 13.07/ 13.08/ 13.09 | Red on-premise; enlace redundante; observabilidad de borde | Pruebas de resiliencia por corte de enlace de 24 h; conmutación ≤ 5 min; estudio de cobertura | Transversales S 20.1; hitos E-25 |
| RT-09.05; Cap. 14.2 (volumetría) | RNF-19.01/ 19.02/ 19.03/ 19.04 | Escalamiento horizontal automático; monitoreo de saturación | Prueba de carga a 1,5 × peak; prueba de estrés hasta el punto de quiebre | Hitos 1.3 y 1.4 del E-25 |
| BA Art. 20; RT-07.07 | RNF-20.06/ 20.07 | Sitio secundario activo-pasivo; respaldo 3-2-1-1-0 | Pruebas semestrales de conmutación; restauración mensual | Hito de DR del E-25 |
| Cap. 17; Cap. 10 (Restricción 1) | RNF-21.01/ 21.03/ 21.04/ 21.05/ 21.06/ 21.07 | NOC 24 × 7 × 365; mesa de ayuda dimensionada con Erlang C | Pruebas de umbrales de atención durante la ventana 05:30–07:00 | SLA de la Operación |
| RT-20.02 y RT-20.04; RNF-22.03/ 22.04 | RF-11.03/ 11.04 | Plan de implantación por oleadas (bodega → preventa → reparto → facturación) | Certificación de administradores y técnicos; umbrales de cierre por oleada | Hitos E-25 |

<a id="seccion-27"></a>

### Material recibido: vacios

Origen de esta tabla: 03_esquema_solucion_alcance/tablas_anexo/vacios.tex.

<a id="tabla-3-a-28"></a>

**Tabla 3.A.28 — Vacíos detectados, tratamiento adoptado y estado**

| **ID** | **Vacío o ambigüedad** | **Tratamiento** | **Estado** |
| --- | --- | --- | --- |
| V-01 | La planilla manual de sugerencia de reposición del preventista no tiene requerimiento dedicado en el catálogo (caso, capítulos 5 y 9.10). Deja la cobertura de reposición aparentemente incompleta. | Consulta conforme al Artículo 43.3; resolución declarada: RF-03.15 más RF-08.05. | Resuelto, Decisión 23 |
| V-02 | Número de instalaciones: cinco según el capítulo 8 del caso, seis según la Tabla 14.1 y RT-21.16. Afecta alcance de red, soporte, traslados y dimensionamiento. | Consulta conforme al Artículo 43.3; lectura declarada: seis sitios, cinco con cómputo. | Elevado a consulta, Decisión 57 |
| V-03 | Flota: 42 camiones, 84 conductores y peonetas, y 42 conductores según la Tabla 14.1. Afecta la oferta económica de terminales, impresoras de cabina y terminales de pago. | Consulta conforme al Artículo 43.3; supuesto adoptado: una tripulación por camión, 42 conductores más 42 peonetas. | Elevado a consulta, Decisión 45 |
| V-04 | Número de ambientes: cuatro según el Artículo 24<sup>o</sup> y el Formulario E-25, cinco más recuperación ante desastres según el Artículo 3<sup>o</sup> y RT-04.01. Afecta el diseño de infraestructura y su costo. | Resuelto por precedencia: cinco ambientes más el de recuperación ante desastres. | Resuelto, S 3.2.2 |
| V-05 | La ponderación del Formulario T-21 suma 98 % aunque su total declara 100 %. Afecta el cálculo del puntaje técnico. | Declarada y elevada a consulta; no se altera el formulario. | Elevado a consulta |
| V-06 | Fechas de calendario: el registro del Formulario T-20 cierra antes de la publicación de las bases; el Informe 1 coincide con el Acta de Respuestas; el Informe 3 y la Presentación 3 caen el mismo día. | No se altera el cronograma; se eleva consulta. | Elevado a consulta |
| V-07 | Códigos RT mal referenciados en la tabla de valores del capítulo 15 del caso: RT-03.24 por RT-03.23, RT-03.13 por RT-03.12, RT-05.10 por RT-16.10, y RT-06.01 citado como tipología de emplazamiento. | Se responde contra el código correcto del documento transversal y se señala el desajuste. | Resuelto, Matriz T-12 |
| V-08 | Desconexión: el relato del caso refiere cortes de hasta dos horas, mientras el capítulo 10 y RT-03.10 exigen operar un turno completo de 14 horas sin señal. | Se documentan dos escenarios: 2 horas como nominal y 14 horas como contingencia de diseño. | Resuelto, supuesto S-41 |
| V-09 | Alta y recuperación de credenciales de usuarios sin correo corporativo (RT-12.12). Afecta a conductores externos y al canal tradicional. | Identidad centralizada con factor presencial mediante clave de un solo uso, y doble factor para acceso externo. | Resuelto, Decisión 34 |
| V-10 | Lote ausente en el 41 % de las recepciones del producto suspendido. Afecta la fidelidad de la trazabilidad de partida. | No se deduce el dato: la migración lo marca y lo excluye de la cobertura de trazabilidad. | Resuelto, Decisión 58 |
| V-11 | El saldo inicial de la cuenta corriente de envases retornables no existe en el origen. Afecta el control de 68.000 canastillos y 9.400 pallets. | Inventario de apertura acordado con el CLIENTE. | Resuelto, Decisión 58 |
| V-12 | Razón social del proponente pendiente de definir, con efecto en la nomenclatura de archivos del Artículo 43.3 y en la planilla de consultas. | Definición previa a la presentación; nomenclatura estandarizada a TFEP-01/2026. | Pendiente formal |

<a id="seccion-28"></a>

## Referencias

Las fuentes de los registros son las siguientes; cada tabla identifica el capítulo, código o sección utilizado.

- Distribuidora Puelche S.A. (2026). *Caso 02: Logística y Bases Técnicas Transversales de la licitación TFEP-01/2026*.
- LafroX. (2026). *Subdocumentos 1 y 2 y anexos; catálogo previo del Subdocumento 3 como inventario de materias*.

<a id="seccion-29"></a>

## Declaración de uso de IA

La tabla declara el trabajo realizado en cada anexo, sin atribuir una revisión humana no documentada.

La Tabla [3.A.29](#tabla-3-a-29) registra la asistencia utilizada en esta revisión.

<a id="tabla-3-a-29"></a>

**Tabla 3.A.29 — Declaración de uso de IA. Fuente: registro de esta revisión.**

| **Sección** | **Herramienta** | **Finalidad** | **Nivel texto** | **Nivel diagramas** | **Revisión humana** |
| --- | --- | --- | --- | --- | --- |
| 3.A | Codex | Contraste y edición. | Alto | Ninguno | No documentada. |
| 3.B | Codex | Contraste y edición. | Alto | Ninguno | No documentada. |
| 3.C | Codex | Contraste y edición. | Alto | Ninguno | No documentada. |
| 3.D | Codex | Contraste y edición. | Alto | Ninguno | No documentada. |
| 3.E | Codex | Contraste y edición. | Alto | Ninguno | No documentada. |
| 3.F | Codex | Contraste y edición. | Alto | Ninguno | No documentada. |
| 3.G | Codex | Contraste y edición. | Alto | Ninguno | No documentada. |
| 3.H | Codex | Contraste y edición. | Alto | Ninguno | No documentada. |
| 3.I | Codex | Contraste y edición. | Alto | Ninguno | No documentada. |
| 3.J | Codex | Contraste y edición. | Alto | Ninguno | No documentada. |
| 3.K | Codex | Contraste y edición. | Alto | Ninguno | No documentada. |

**Nota de trabajo:** Falta registrar quién revisó y qué verificó. Para completarlo se requiere revisión humana efectiva del contenido y su consolidación en el Formulario A-6.


> Nota de conversión: se conserva el contenido vigente, incluidos títulos, errores, notas de trabajo, campos vacíos y diferencias entre versiones. Las figuras están transcritas a texto. Las menciones de arquitectura y otros subdocumentos son referencias del original, no evidencia incorporada o verificada en esta conversión.
