# Anexos del Subdocumento 2: Comprensión del problema y de la necesidad

El presente documento recopila los listados detallados que sustentan el análisis del problema y de la necesidad presentado en el cuerpo del Subdocumento 2, conforme a las directrices de la Sección 11 de las Aclaraciones de la Licitación.

## Anexo 2.1: Listado de Requerimientos del Cliente

A partir de la narrativa del Caso 02, las entrevistas a los actores clave y las Bases Técnicas Transversales, se identifican catorce familias funcionales prioritarias y cinco condiciones no funcionales rectoras. Los códigos **F-01 a F-14** identifican familias de síntesis de este anexo; el catálogo atómico y sus códigos RF/RNF se desarrollan en el Subdocumento 3 y en el Formulario T-12.

**Catálogo consolidado de Requerimientos Funcionales del Caso 02**

| % C1.2cm L3.5cm Y C1.6cm C1.8cm% **Familia** | **Nombre del Requerimiento** | **Descripción Operativa y Criterio de Verificación** | **Prioridad** | **Etapa** F-01 | Preventa Móvil Desconectada | Captura de pedidos en terreno bajo paradigma *offline-first*, validando reglas de stock y crédito localmente con sincronización asíncrona determinista. | Crítica | Etapa 1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F-02 | Recepción y Control de Lotes | Captura obligatoria de identificadores GS1, lote y fecha de vencimiento en la recepción de las seis instalaciones antes de autorizar el ingreso físico. | Crítica | Etapa 1 |  |  |  |  |
| F-03 | Gestión de Bodega y FEFO | Control de existencias físicas y asignación de despachos bajo lógica estricta *First Expired, First Out* en cámaras de frío (-22 °C) y secos. | Alta | Etapa 1 |  |  |  |  |
| F-04 | Picking por Olas en Almacén | Generación y consolidación de hojas de preparación digitales por zonas de almacenamiento, reduciendo traslados y tiempos de armado nocturno. | Alta | Etapa 1 |  |  |  |  |
| F-05 | Cross-Docking Controlado | Registro y control de la transferencia entre recepción y despacho mediante lectura de unidades logísticas, con medición del tiempo real del proceso y de sus excepciones. | Alta | Etapa 1 |  |  |  |  |
| F-06 | Planificación Dinámica de Rutas | Propuesta y secuenciación de rutas según capacidad, zonas, ventanas horarias y restricciones de terreno, conservando la corrección manual y capturando las heurísticas del planificador. | Alta | Etapa 1 |  |  |  |  |
| F-07 | Telemetría y Control de Frío | Monitoreo continuo de temperatura vehicular y en cámaras fijas con registro inmutable y alertas automáticas graduadas ante excursión térmica. | Crítica | Etapa 1 |  |  |  |  |
| F-08 | Entrega Digital y POD | Captura en terreno de la prueba de entrega con firma en pantalla o evidencia alternativa, georreferenciación y registro estructurado de devoluciones o rechazos. | Crítica | Etapa 1 |  |  |  |  |
| F-09 | Acuse de Recibo Legal de GDE | Integración bidireccional con ERP para certificar el acuse de recibo de la Guía de Despacho Electrónica ante el SII con mérito ejecutivo. | Alta | Etapa 1 |  |  |  |  |
| F-10 | Conciliación de Efectivo | Registro del cobro en el local y cuadratura de la recaudación al retorno, con causales tipificadas y responsable identificado para toda diferencia. | Alta | Etapa 1 |  |  |  |  |
| F-11 | Trazabilidad y Retiro Sanitario | Motor de búsqueda bidireccional capaz de localizar la trayectoria completa de un lote (desde proveedor a cliente final) en menos de 2 horas. | Crítica | Etapa 1 |  |  |  |  |
| F-12 | Autoatención de Clientes | Canal de consulta para los clientes que dispongan de conectividad, sin exigir internet, dispositivo propio ni pago electrónico al canal tradicional. | Media | Etapa 2 |  |  |  |  |
| F-13 | Integración EDI Canal Moderno | Pasarela de mensajería electrónica estándar GS1/EDI (órdenes de compra, DESADV, facturación) requerida para la retención del retail hacia 2029. | Alta | Etapa 2 |  |  |  |  |
| F-14 | Analítica de Costo de Servir | Modelación granular del costo real de distribución por cliente, canal, ruta y tipología de carga, superando el prorrateo estático de 2016. | Media | Etapa 2 |  |  |  |  |

**Requerimientos No Funcionales rectores del proyecto**

| % C1.8cm L3.2cm Y C2.2cm% **Código** | **Dimensión de Calidad** | **Criterio y Métrica de Aceptación** | **Estándar / Base** RNF-DISP | Disponibilidad del Servicio | Disponibilidad mensual ≥ 99,95% para los componentes de infraestructura y ≥ 99,9% para la transacción crítica de extremo a extremo. | BTT, §7.2; Art. 78° BA |
| --- | --- | --- | --- | --- | --- | --- |
| RNF-REND | Sincronización tras reconexión | Sincronización móvil completa en un máximo de 10 minutos tras 14 horas sin señal y sincronización de un centro de distribución en un máximo de 2 horas tras 24 horas desconectado. | Caso, Cap. 15; BTT, RT-03.12 |  |  |  |
| RNF-RESIL | Autonomía Desconectada | Capacidad de operación autónoma en terminales móviles de 14 horas de turno y en centros de distribución de ≥ 24 horas sin enlace WAN. | Caso, Cap. 10; BTT, RT-03.10 |  |  |  |
| RNF-SEG | Ciberseguridad y Privacidad | Cifrado de datos locales y en tránsito, autenticación multifactor y preparación para el cumplimiento de Ley 21.719 desde su entrada en vigencia. | ISO/IEC 27001; Ley 21.719 |  |  |  |
| RNF-DR | Continuidad y Recuperación | Centro de datos secundario con RTO ≤ 4 horas y RPO ≤ 15 minutos, validado mediante simulacros semestrales obligatorios. | BTT, RT-07.04 y RT-07.07 |  |  |  |

## Anexo 2.2: Listado de Supuestos, Exclusiones y Restricciones

La Tabla tab:supuestos-ingenieria registra como supuestos de formulación las dieciséis decisiones que el numeral 16.1 del caso exige resolver. Cada fila explicita la conducta adoptada y la consecuencia principal que debe asumir el diseño; el registro detallado y la trazabilidad a requisitos se mantienen en el catálogo canónico del proyecto.

**Supuestos de formulación derivados de las decisiones pendientes del caso**

| % C1.0cm L6.0cm L7.0cm L3.2cm% **ID** | **Supuesto adoptado** | **Consecuencia asumida por la propuesta** | **Origen** S-01 | OTIF considera cumplida solo la entrega del 100% de ítems y unidades dentro de la fecha y ventana pactadas. | Toda entrega parcial o tardía se registra como incumplida, con causal; *fill rate* y *perfect order* se miden por separado. | Caso, 16.1, decisión 1. |
| --- | --- | --- | --- | --- | --- | --- |
| S-02 | La unidad de trazabilidad sanitaria es el lote del proveedor; el SSCC identifica la unidad logística asociada. | La recepción captura lote y vencimiento, y el retiro sanitario se consulta hacia atrás y hacia adelante por lote. | Caso, 16.1, decisión 2. |  |  |  |
| S-03 | Ante local cerrado, el conductor registra el intento y el sistema reagenda a la próxima ventana disponible; no se entrega a terceros. | Si el cliente continúa ausente, la mercadería retorna al centro de distribución con trazabilidad del evento. | Caso, 16.1, decisión 3. |  |  |  |
| S-04 | La excursión térmica se parametriza por tipo de producto; Calidad decide liberar, bloquear o rechazar. | El sistema alerta y habilita el bloqueo, pero no invalida automáticamente el producto. | Caso, 16.1, decisión 4. |  |  |  |
| S-05 | Cada transportista confirma conductor y vehículo antes del despacho; el conductor real se autentica al iniciar la ruta. | La rotación sin aviso queda resuelta mediante la vinculación auditada entre persona, vehículo y viaje. | Caso, 16.1, decisión 5. |  |  |  |
| S-06 | Se mantiene el efectivo y se reduce mediante medios alternativos; cada camión realiza rendición digital individual. | Toda diferencia exige causal tipificada y responsable identificado antes del cierre. | Caso, 16.1, decisión 6. |  |  |  |
| S-07 | El costo de servir se calcula por actividad, entrega y cliente, usando distancia, tiempos, volumen, devoluciones y activos retornables. | Los clientes no rentables se segmentan para revisar frecuencia y pedido mínimo; no se eliminan automáticamente. | Caso, 16.1, decisión 7. |  |  |  |
| S-08 | El stock se reserva al confirmar el pedido en el servidor central, por orden cronológico. | En modo desconectado el stock es indicativo; los conflictos se resuelven al sincronizar y se notifica el quiebre. | Caso, 16.1, decisión 8. |  |  |  |
| S-09 | Rige el precio vigente al despacho, salvo excepción configurada por cliente o cadena. | Un cambio sin excepción se informa al cliente y queda trazado antes o junto con la facturación. | Caso, 16.1, decisión 9. |  |  |  |
| S-10 | Los 68.000 canastillos y 9.400 pallets se controlan por saldo de cliente y transportista, sin serialización unitaria. | Entregas y devoluciones actualizan la cuenta corriente; los excesos y pérdidas generan alertas e informes. | Caso, 16.1, decisión 10. |  |  |  |
| S-11 | El maestro interno de Puelche prevalece y conserva equivalencias e historial de cambios de códigos externos. | Los códigos sin equivalencia quedan en una bandeja de excepciones y no crean una segunda verdad de producto. | Caso, 16.1, decisión 11. |  |  |  |
| S-12 | La devolución se registra en la entrega con SKU, cantidad y motivo; el ERP emite la nota de crédito cuando corresponde. | La solución transmite el evento y la evidencia, sin transformarse en un segundo emisor tributario. | Caso, 16.1, decisión 12. |  |  |  |
| S-13 | No se instalan cámaras en cabina; el uso de GPS para jornada queda sujeto a acuerdo sindical y protección de privacidad. | La telemetría operacional se limita a vehículo y ruta hasta disponer de dicho acuerdo. | Caso, 16.1, decisión 13. |  |  |  |
| S-14 | El WMS de 2013 se reemplaza por la solución común para las instalaciones, con migración y reversión. | Se elimina la fragmentación entre WMS y planillas, asumiendo el esfuerzo de migrar y reconciliar datos. | Caso, 16.1, decisión 14. |  |  |  |
| S-15 | La prueba principal es la firma en pantalla; si no es posible, se captura fotografía, nombre del receptor o confirmación QR vinculada a la GDE. | La alternativa conserva fecha, ubicación e identidad disponible y se articula con el acuse tributario. | Caso, 16.1, decisión 15. |  |  |  |
| S-16 | El conocimiento del planificador se captura en la Etapa 1 y se parametriza en el motor de rutas antes de su jubilación. | El sistema propone rutas y conserva corrección manual; cada regla transferida queda documentada y probada en terreno. | Caso, 16.1, decisión 16. |  |  |  |

La Tabla tab:anexo_exclusiones detalla las exclusiones explícitas de alcance que delimitan la responsabilidad contractual del proponente, garantizando la viabilidad del proyecto.

**Exclusiones explícitas del alcance del proyecto**

| % C1.0cm L3.5cm Y L3.8cm% **N°** | **Exclusión de Alcance** | **Justificación Técnica y Contractual** | **Manejo / Mitigación** E-01 | Reemplazo o modificación del sistema de gestión empresarial. | El ERP de 2017 sigue siendo el registro contable y tributario y conserva sus módulos. | Integración desacoplada y una sola fuente oficial. |
| --- | --- | --- | --- | --- | --- | --- |
| E-02 | Administración de remuneraciones y recursos humanos. | Estas funciones residen en el sistema de gestión empresarial. | Solo se integran identidades o datos mínimos cuando un proceso lo requiera. |  |  |  |
| E-03 | Punto de venta para el local del cliente. | El caso no solicita operar la venta interna del almacenero. | Se ofrece autoatención sin convertir la solución en POS del cliente. |  |  |  |
| E-04 | Comercio electrónico al consumidor final. | El alcance atiende la relación B2B de Puelche con sus clientes. | Los canales digitales se limitan al catálogo, pedido y seguimiento B2B. |  |  |  |
| E-05 | Administración contractual o pago de transportistas. | El contrato exige integración operacional, no liquidar contratos de transporte. | Se intercambian asignaciones, eventos y evidencias del viaje. |  |  |  |
| E-06 | Diseño de la red logística. | La ubicación de centros de distribución y plataformas no está en discusión. | El despliegue se adapta a las seis instalaciones declaradas. |  |  |  |
| E-07 | Automatización robotizada de bodega. | No se solicitan robots ni transportadores. | Se digitalizan recepción, ubicación, preparación y despacho con apoyo móvil. |  |  |  |
| E-08 | Gestión mecánica de la flota. | Mantenciones, repuestos y condición mecánica permanecen fuera del alcance. | Se integra la telemetría existente para fines operacionales. |  |  |  |
| E-09 | Compra del hardware de terreno por el proponente. | El CLIENTE adquiere dispositivos, lectores, impresoras y sensores. | El proponente especifica cantidades y características en el Formulario T-11. |  |  |  |

La Tabla tab:anexo_restricciones reproduce las doce restricciones no negociables que condicionan la solución. No son supuestos ni exclusiones: su cumplimiento es obligatorio y debe demostrarse en arquitectura, plan de trabajo y pruebas.

**Restricciones no negociables del Caso 02**

| % C1.0cm L6.0cm Y% **N°** | **Restricción** | **Implicación para la propuesta** R-01 | Entre 05:30 y 07:00 salen 96 camiones y el despacho no puede detenerse. | Continuidad y cambios fuera de la ventana crítica. |
| --- | --- | --- | --- | --- |
| R-02 | El centro de distribución debe recibir, preparar y despachar durante un corte del enlace. | Operación local autónoma durante al menos 24 horas. |  |  |
| R-03 | Preventa y reparto deben funcionar un turno completo sin señal. | Persistencia local por 14 horas y sincronización posterior controlada. |  |  |
| R-04 | El ERP no se reemplaza ni modifica y sigue emitiendo los documentos tributarios. | Integración desacoplada sin segundo registro contable ni tributario. |  |  |
| R-05 | No se exige internet, dispositivo propio ni pago electrónico al canal tradicional. | La operación se completa con recursos de Puelche y admite efectivo. |  |  |
| R-06 | La solución opera con 54 camiones de diez transportistas y conductores que rotan sin aviso. | Identificación rápida y acuerdo operacional con cada transportista. |  |  |
| R-07 | Los dispositivos de cámara operan a -22 °C y sin señal. | Equipos aptos para frío, guantes y trabajo desconectado. |  |  |
| R-08 | No se interviene del 1 al 25 de septiembre, durante diciembre ni los tres primeros días hábiles de cada mes. | Despliegues, pruebas y reversión se programan fuera de esos períodos. |  |  |
| R-09 | TI dispone de cuatro personas. | Toda especialidad permanente que no exista en el CLIENTE se presta como servicio. |  |  |
| R-10 | El sindicato objetó cámaras en cabina y control de jornada por GPS. | No se incluyen cámaras; el uso laboral del GPS exige acuerdo y medidas de privacidad. |  |  |
| R-11 | Preparación rota 38% anual y trabaja en turno nocturno. | La interfaz y capacitación deben admitir aprendizaje breve y recambio frecuente. |  |  |
| R-12 | La emisión y el acuse de documentos tributarios electrónicos deben respetar la normativa vigente. | El diseño conserva validez legal, evidencia y trazabilidad con el ERP. |  |  |

## Anexo 2.3: Otros Listados (Actores del Ecosistema y Sistemas Legados)

La Tabla tab:anexo_actores_extendido presenta el catálogo nominal y extendido de los 19 actores que componen el ecosistema humano y operacional de Distribuidora Puelche S.A.

**Catálogo nominal extendido de los 19 actores del ecosistema Puelche**

| % L3.0cm L2.8cm L5.5cm C2.0cm C1.8cm L4.0cm% **Actor / Cargo** | **Rol en el Ecosistema** | **Ineficiencia que Enfrenta en la Situación Actual** | **Influencia** | **Interés** | **Estrategia de Adopción** Gerenta General | Patrocinadora y Alta Dirección | Falta de información consolidada para arbitrar disputas internas y riesgo sanitario latente. | Muy Alta | Muy Alto | Cuadro de mando ejecutivo y reportabilidad estratégica. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gerente Comercial | Conducción de Ventas | Pérdida de ventas por quiebres en preventa y riesgo de perder canal moderno en 2029. | Muy Alta | Muy Alto | Visibilidad de inventario y promesa de entrega confiable. |  |  |  |  |  |
| Gerente de Operaciones | Ejecución Logística | Brecha no investigada entre la reducción prometida y la observada en cross-docking; dificultad para cumplir entregas en 24 h. | Alta | Muy Alto | Medición de tiempos y validación de mejoras antes de su implantación. |  |  |  |  |  |
| Gerente de Finanzas | Control Financiero | Fuga de dinero en efectivo y falta de costeo de servir por cliente y ruta. | Muy Alta | Muy Alto | Conciliación atómica y reportería de rentabilidad. |  |  |  |  |  |
| Jefa de Calidad | Aseguramiento Sanitario | Registro térmico manual, sin alertas de excursión y 9 días para recall sanitario. | Alta | Muy Alto | Telemetría inmutable y recall automatizado <2 horas. |  |  |  |  |  |
| Jefa de Bodega | Custodia de Inventarios | Conteo cíclico con 2,3% de descuadre y 1,7% de merma por vencimiento. | Alta | Muy Alto | WMS móvil con trazabilidad FEFO por código de barra. |  |  |  |  |  |
| Jefe de TI | Operación Tecnológica | Equipo de 4 personas incapaz de soportar nuevos sistemas sin soporte externo 24×7. | Alta | Muy Alto | Servicios gestionados de operación y soporte L1/L2/L3. |  |  |  |  |  |
| Planificador de Rutas | Diagramación Logística | Dependencia de planillas Excel personales; jubilación en dos años sin relevo preparado. | Alta | Muy Alto | Elicitación formal de heurísticas en motor de ruteo. |  |  |  |  |  |
| Preventistas (62 personas) | Captura de Pedidos | Aplicación móvil obsoleta sin visibilidad de inventario ni crédito; 7,8% de pedidos mutilados. | Alta | Alto | App móvil moderna con stock y crédito precargado. |  |  |  |  |  |
| Tripulación propia y peoneta (84 personas) | Despacho y Cobranza | Transporte de efectivo con riesgo de asalto; rendición manual diferida y guías en papel. | Alta | Alto | Prueba digital de entrega (POD) y cuadratura en ruta. |  |  |  |  |  |
| Conductores externos (aprox. 160 personas) | Flota Tercerizada | Rotación sin aviso, sin vínculo laboral directo y resistencia a sistemas complejos. | Alta | Alto | Interfaz intuitiva en smartphone sin fricción operativa. |  |  |  |  |  |
| Empresas Transp. (10 empresas) | Proveedores de Flete | Discrepancias tarifarias por demoras en muelle y guías físicas extraviadas. | Media-alta | Alto | Liquidación transparente basada en eventos digitales. |  |  |  |  |  |
| Preparadores (120 personas) | Picking en Almacén | Preparación con hojas de papel impresas en frío extremo (-22 °C) sin señal móvil. | Alta | Alto | Terminales robustos para frío y listas digitales por ola. |  |  |  |  |  |
| Sindicato de Choferes | Representación Laboral | Oposición frontal a cámaras en cabina y monitoreo por GPS invasivo de la jornada. | Alta | Alto | Protocolo de privacidad enfocado en la carga y el camión. |  |  |  |  |  |
| Canal Tradicional (11.600 clientes) | Clientes Almaceneros | Sin internet ni computadores; pagan en efectivo; castigan faltantes cambiando de proveedor. | Muy alta | Alto | Servicio fluido sin exigir tecnología al almacenero. |  |  |  |  |  |
| Food Service (2.100 clientes) | Hoteles y Restaurantes | Exigen despacho estricto antes de las 10:00 y certificación de cadena de frío intacta. | Muy alta | Alto | Ventanas matinales garantizadas y certificado térmico. |  |  |  |  |  |
| Canal Moderno (500 puntos) | Cadenas de Retail | Exigencia contractual de EDI, GDE digital y OTIF ≥ 95% a contar de enero 2029. | Muy alta | Alto | Interoperabilidad GS1/EDI y acuse electrónico legal. |  |  |  |  |  |
| Proveedores (180 empresas) | Suministro de Carga | Largas filas de espera en muelle; en el producto involucrado en el retiro, 41% de recepciones sin lote. | Media-alta | Alto | Turnos de descarga y lectura rápida GS1-128 en muelle. |  |  |  |  |  |
| Autoridad Sanitaria | Fiscalización SEREMI | Potestad de aplicar sumarios sanitarios y clausuras ante brotes alimentarios (RSA). | Media-alta | Alto | Auditoría inalterable de lotes y cadena de frío 24×7. |  |  |  |  |  |

La Tabla tab:anexo_legados resume el inventario de sistemas informáticos heredados que operan actualmente en Distribuidora Puelche S.A.

**Inventario de sistemas legados de Distribuidora Puelche S.A.**

| % L2.8cm L2.2cm L2.0cm Y L2.8cm% **Sistema / Aplicación** | **Tipo / Versión** | **Año Inicio** | **Estado Operacional y Deficiencias** | **Destino en el Proyecto** ERP Principal | Sistema de gestión empresarial | 2017 | Operativo como registro contable y tributario; interfaces no documentadas. | Se conserva y se integra sin modificarlo. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| WMS Bodega | Sistema de gestión de almacén | 2013 | Soporte discontinuado; opera en Talca mientras Concepción usa planillas. | Reemplazo progresivo con migración y reversión. |  |  |  |  |
| App Preventa | Desarrollo a medida | No informado | Proveedor desaparecido; sin visibilidad de stock ni crédito en línea. | Sustitución por la aplicación móvil de preventa. |  |  |  |  |
| Planificador de Rutas | Planilla de cálculo | No informado | Depende de un usuario único y de conocimiento no documentado. | Sustitución por motor de rutas con corrección manual. |  |  |  |  |
| Rendición de Valores | Formularios en papel | No informado | Rendición D+1 manuscrita; diferencias mensuales de $4,2 millones. | Digitalización y conciliación por camión y responsable. |  |  |  |  |
