# Vistas de arquitectura lógica con Laravel

Estas descripciones precisan el alcance de la vista general y de las trece vistas por actor. Una conexión con un módulo representa una interacción autorizada mediante sus servicios, no acceso directo a sus tablas ni permisos sobre todas sus funciones.

## ARQL-01 · Visión general

[Diagrama](ARQL-01_Vision_general.png). Reúne las ocho capas y relaciona las aplicaciones y portales con los módulos M1–M12 del monolito modular Laravel/PHP. Distingue la persistencia local y central y los intercambios por RabbitMQ, SQS FIFO y adaptadores. Seguridad y observabilidad son responsabilidades transversales. Las rutas simplificadas de esta lámina se complementan con ARQL-17 para el acceso local sin WAN y con ARQL-19 y ARQL-20 para la separación de responsabilidades y procesos.

## ARQL-02 · Preventista

[Diagrama](ARQL-02_Preventista.png). El preventista utiliza la aplicación Kotlin para consultar su copia local de catálogo, precios, stock y crédito y registrar pedidos en M3. Sin señal, conserva cada captura con su UUID; al reconectar, los servicios verifican las condiciones de negocio y devuelven el resultado. Capturar un pedido no equivale a confirmar stock o crédito con información vigente.

## ARQL-03 · Conductor propio

[Diagrama](ARQL-03_Conductor_propio.png). La aplicación de reparto registra la evidencia de entrega en M6, los cobros y la rendición en M7 y las devoluciones y retornables en M8. Conserva los eventos de la ruta para sincronizarlos sin duplicar operaciones. La prueba de entrega se vincula con el documento emitido por el ERP; no reemplaza su función tributaria.

## ARQL-04 · Conductor externo

[Diagrama](ARQL-04_Conductor_externo.png). Destaca el recorrido de entrega de M6 desde un dispositivo BYOD. El alta y el OTP requieren conexión; después, la asignación firmada limita el trabajo a la empresa, ruta y turno autorizados. M7 y M8 se habilitan solo cuando la asignación incluye cobros o devoluciones, conforme al ciclo de vida del conductor externo del 4.1. El énfasis gráfico en M6 no elimina estas funciones ni concede acceso general al sistema.

## ARQL-05 · Cliente del canal tradicional

[Diagrama](ARQL-05_Cliente_canal_tradicional.png). El portal ofrece consulta y autogestión a quienes disponen de conexión, con acceso únicamente a sus pedidos y documentos. Los avisos por SMS o WhatsApp dependen de la disponibilidad del canal. La operación de los almacenes sin internet se sostiene mediante preventa y reparto; no se exige que instalen una aplicación o utilicen el portal.

## ARQL-06 · Cliente del canal moderno

[Diagrama](ARQL-06_Cliente_canal_moderno.png). M11 recibe y valida los mensajes B2B mediante el hub EDI y los transforma a contratos internos. Pedidos, avisos de despacho y acuses se relacionan con M3, M5 y M6 según el proceso. Cada cadena dispone de un contrato de mensaje y tratamiento de excepciones; la entrega técnica de un mensaje no equivale automáticamente a su aceptación comercial.

## ARQL-07 · Transportista

[Diagrama](ARQL-07_Transportista.png). El portal permite consultar las rutas y entregas de la empresa transportista. Los servicios de reparto relacionan el avance con la planificación y la telemetría, respetando el alcance por empresa y asignación. El transportista no consulta directamente los almacenes de rutas o telemetría ni adquiere facultades sanitarias o tributarias.

## ARQL-08 · Proveedor

[Diagrama](ARQL-08_Proveedor.png). El proveedor consulta sus órdenes y recepciones mediante el portal. M1 registra recepción, lotes y discrepancias, mientras la ACL intercambia los datos necesarios con el ERP. La visibilidad del proveedor queda limitada a su relación comercial; las decisiones de aceptación física y sanitaria corresponden al personal autorizado de Puelche.

## ARQL-09 · Preparador

[Diagrama](ARQL-09_Preparador.png). El terminal HHT registra misiones de M5 y movimientos autorizados de M2 mediante los servicios de bodega. Ante pérdida de WAN utiliza la puerta local y el control de turno definidos en ARQL-17, sin depender de Amazon API Gateway. La autonomía de 24 horas comprende datos, eventos y relevo de personas; el escaneo preserva lote y trazabilidad de la preparación.

## ARQL-10 · Jefa de Calidad

[Diagrama](ARQL-10_Jefa_de_calidad.png). La consola de M9 relaciona recepción, lote, temperatura y entrega para investigar no conformidades y ejecutar retiros. M1 aporta la evidencia de recepción. Un bloqueo sanitario impide liberar el lote incluso sin WAN; su levantamiento exige la decisión registrada de una persona de Calidad autorizada.

## ARQL-11 · Gerente Comercial

[Diagrama](ARQL-11_Gerente_comercial.png). Los tableros de M10 reúnen indicadores comerciales y logísticos procedentes de preventa, entregas y devoluciones. Las consultas analíticas utilizan Redshift y muestran su fecha de actualización, evitando cargar las bases transaccionales. OTIF, fill rate y costo de servir deben conservar las definiciones y reglas del catálogo de requerimientos.

## ARQL-12 · Gerente de Finanzas

[Diagrama](ARQL-12_Gerente_finanzas.png). M7 permite seguir cobros, rendiciones y diferencias de conciliación mediante una consola autorizada. La ACL mantiene el intercambio financiero con el ERP, que conserva su responsabilidad contable y tributaria. Un cobro capturado en ruta permanece pendiente hasta completar las validaciones de rendición correspondientes.

## ARQL-13 · Planificador de rutas

[Diagrama](ARQL-13_Planificador_de_rutas.png). M4 combina pedidos y disponibilidad autorizada de inventario con restricciones de vehículos y ventanas de entrega. El servicio GIS aporta geocodificación y estimaciones de recorrido mediante un adaptador. El planificador valida las excepciones y publica la asignación de ruta; consultar M2 o M3 no le permite modificar sus reglas de stock o crédito.

## ARQL-14 · Gerente de TI

[Diagrama](ARQL-14_Gerente_TI.png). La consola administrativa permite supervisar servicios, identidades, integraciones y observabilidad. Su alcance transversal describe la responsabilidad técnica, no una autorización para ejecutar todas las operaciones de M1–M12 ni leer sin restricción sus datos sensibles. Las acciones privilegiadas requieren MFA, permisos específicos y auditoría, con separación de funciones respecto de las aprobaciones de negocio.

## Precisiones para consolidar las láminas

Los originales conservan etiquetas que requieren armonización visual: la caché del IdP indica TTL de 1 hora, mientras el 4.1 distingue renovación del manifiesto cada hora, caché de solo lectura de 24 horas y permisos por turno; el recorrido HHT debe mostrar expresamente la puerta local durante un corte; y la vista general conserva un texto residual «Text». La representación de la conexión al ERP debe leerse a través de la ACL, nunca como escritura directa de un módulo al legado. Estas diferencias deben corregirse en la fuente editable antes de sustituir con estas imágenes las figuras consolidadas del informe.

Los PNG contienen el modelo editable de diagrams.net en sus metadatos y pueden abrirse con esa herramienta. Se preservan los originales y el TXT recibido como referencia del aporte; las descripciones anteriores incorporan las restricciones de negocio y seguridad del subdocumento 4.1.
