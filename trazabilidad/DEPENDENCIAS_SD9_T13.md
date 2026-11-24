# Ajustes que debe incorporar el T-13 del SD9

Este registro reúne las dependencias vigentes para la rama de corrección del SD9 y el historial de contrastes. El cotejo vigente identifica sus fuentes en la sección SD3-04. El primer corte comparó el T-13 `0c57a4bb`, el T-14 `68669bef` y el SD4 `69c9a879` con el T-12 de entonces. El registro documenta comprobaciones de trazabilidad y pruebas previstas.

## Punto 4: seguridad, certificaciones y operación

- RT-15.08 figura como «Cumple» en T-12 y T-13. El cotejo documental del T-8 y los Anexos 12.B a 12.D de SD12 (rama de corrección, `69a17f01`) vincula las nueve personas con credenciales a su cargo, perfil, dedicación declarada y período. El décimo integrante, Rodrigo Valdés, figura asignado a Integración sin certificación exigida. Se conserva RT-15.08/P01 como prueba prevista.
- RNF-14.01, RT-11.08 y RT-21.03 figuran como parciales en ambos formularios. El T-13, sección 8.2, precisa las verificaciones previstas. Para cerrar RT-21.03 se requiere la validación del cuadrante nominal del Anexo 10.D, B-02, que ya distingue responsables de coordinación y puestos de guardia. RT-21.03 remite a 10.1.1, 10.1.2 y 10.1.4 del T-14.
- La matriz T-13 vigente se genera desde la revisión SD3 `1763cabf`. RNF-14.01 publica en su ficha individual el criterio normativo del catálogo y la aceptación por tramo del T-12.

### Solicitud de aclaración al evaluador

Registro interno de coordinación. El T-20 fijó el período formal de consultas del 20 de agosto al 1 de septiembre de 2026 y la publicación del acta el 7 de septiembre. En las ramas consultadas se localizaron las aclaraciones generales y las del Informe 3. Las generales observan el uso de certificaciones sin respaldo obtenible. En esas fuentes no se encontró una autorización específica para cerrar estas filas con las constancias actuales. Si el equipo tiene el acta de respuestas, revisarla primero. La solicitud siguiente queda preparada para el canal académico y su respuesta debe quedar registrada con fecha, fuente y alcance.

> Profesor, estamos cerrando la matriz T-12 de LafroX para el Caso 02, Logística, de la licitación TFEP-01/2026. Agradeceríamos su orientación sobre tres criterios de la entrega final.
>
> 1. Para RT-11.08 y RNF-14.01, el caso no documenta las interfaces del ERP de 2017. ¿Qué respaldo de diseño y prueba prevista admite para declarar TLS 1.3 cuando el enlace real no está disponible en el ejercicio? ¿Cómo debemos declarar un servicio de terceros cuya documentación contempla TLS 1.2?
> 2. Para el seguimiento de ISO/IEC 27001 al inicio contractual, ¿qué documento debe incorporarse si se recurre al plan firmado con hitos verificables del artículo 34.1?
> 3. Para RT-21.03, el T-8 nomina a los responsables principales y el T-15 respalda las plazas y horas. ¿La entrega final requiere titulares y suplentes nominados en cada turno o admite formalizar las guardias pendientes en un hito? Si admite lo segundo, ¿qué datos se deben acreditar en la entrega?

Fuentes de la consulta: Bases Administrativas, arts. 34.1 y 43 y Formulario T-20, actividades 4 y 5. Bases Técnicas Transversales, RT-11.08, RT-15.07 y RT-21.03. Caso 02, cap. 5. Aclaraciones generales, versión histórica `3dfe43de`, y aclaraciones del Informe 3, `2b04aaa7`.

### Inventario TLS para Arquitectura y Seguridad

El Anexo 4-H del SD4 identifica las interfaces y el Anexo 4-R contiene la política y la matriz «Tramos de cifrado en tránsito y respaldo pendiente». El T-11 identifica el adaptador ERP en VM-04 en Talca y las dependencias de salida. El Excel aporta el presupuesto de certificados, que sirve como respaldo de costos. Arquitectura debe registrar cada extremo, ambiente, versión admitida, configuración propuesta y fuente de la confirmación. La versión negociada y el resultado se completan cuando se ejecute una prueba autorizada.

| Enlace | Respaldo disponible | Dato que debe confirmar el responsable |
|---|---|---|
| INT-06, ERP 2017–ACL de Talca | T-11 y Anexo 4-H identifican la ACL en VM-04. El ERP se conserva y sus interfaces requieren levantamiento. La salida ACL–SQS es otro tramo. AWS documenta TLS 1.2 como mínimo y recomienda 1.3. [Protección de datos de Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/data-protection.html) | El 23 de noviembre de 2026, Leandro informó que cuenta con la confirmación del equipo del ERP y que coincide con TLS 1.3 para ERP–ACL de Talca. La oferta exige TLS 1.3. El ensayo previsto del T-13 registrará la configuración y versión negociada por ambiente, por separado para ERP–ACL y ACL–SQS. |
| INT-07, DTE y estados | El ERP sigue siendo el emisor. El SII documenta ambientes de certificación y producción para consulta de estado de envío. [Manual del SII](https://www.sii.cl/factura_electronica/factura_mercado/estado_envio.pdf) | Integración: separar el tramo de la solución del tramo operado por el ERP, identificar a su dueño y confirmar el alcance del requisito en cada extremo. |
| INT-08, EDI por cadena | El Anexo 4-R declara TLS 1.3 para la entrada AS2 de LafroX. | Integración y M11: confirmar por cadena y por dirección el extremo, el perfil AS2 y la versión admitida. |
| INT-09, pasarela de pago | Anexo 4-H identifica M7 y T-11 enumera Transbank. Webpay publica los hosts de integración y producción. Falta identificar el producto de M7. [Ambientes de Transbank](https://transbankdevelopers.com/documentacion/como_empezar) | Integración y M7: confirmar producto, ambiente y extremo exacto con el proveedor. Registrar el respaldo para ese producto. |
| INT-10, mapas y geocodificación | El Anexo 4-H identifica a M4 como dueño interno. | M4: confirmar proveedor, API, ambiente y compatibilidad del extremo seleccionado. |
| INT-11, Amazon SES | AWS documenta TLS 1.3 para la API HTTPS. AWS describe por separado el tramo de entrega al servidor de correo receptor. | Notificaciones: fijar el extremo y la configuración de la API. Confirmar si el tramo de entrega al receptor queda dentro del alcance y documentar su tratamiento. [Protocolos de Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/security-protocols.html) |
| INT-11, Amazon SNS | La documentación indica un mínimo de TLS 1.2 o posterior. | Notificaciones: verificar TLS 1.3 para el extremo que se utilizará, con su respaldo. [Seguridad de Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/infrastructure-security.html) |
| INT-11, AWS End User Messaging Social | AWS describe TLS 1.2 en las comunicaciones con aplicaciones y Meta. Para la API indica TLS 1.2 o posterior como requisito de cliente. | Arquitectura y Notificaciones: precisar ambos tramos. Si el tramo documentado con TLS 1.2 queda en alcance, confirmar si hay una modalidad compatible. Si no existe, registrar la brecha y evaluar una alternativa con TLS 1.3 que preserve la función de aviso y su trazabilidad. [Cifrado en tránsito de AWS End User Messaging Social](https://docs.aws.amazon.com/social-messaging/latest/userguide/data-protection.html#data-encryption-in-transit) |
| INT-15, telemetría existente | El Anexo 4-H identifica una API de solo lectura para M12. | M12: confirmar proveedor, versión de la API y TLS del extremo existente. |
| Otras dependencias y enlaces internos | T-11 identifica Intune/Zebra, Falcon y GuardDuty. Microsoft publica los extremos de Intune. El Anexo 4-R documenta el transporte de los enlaces internos. [Extremos de Microsoft Intune](https://learn.microsoft.com/en-us/intune/fundamentals/endpoints) | Arquitectura: completar el inventario de extremos, incluir MDM y EDR, y registrar el protocolo aplicable. Separar los túneles IPsec/IKE de las sesiones TLS que transporten. |

### Evaluación de WhatsApp Cloud API directa

| Tramo o comprobación | Resultado y condición para adoptar |
|---|---|
| Envío LafroX → Meta | Graph API admite TLS 1.3. Exigir TLS 1.3 desde el trabajador de notificaciones y conservar la prueba prevista de la versión negociada y del certificado válido. [Seguridad de Graph API](https://developers.facebook.com/docs/graph-api/guides/secure-requests/) |
| Retorno Meta → LafroX | Meta documenta HTTPS, firma de eventos y reintentos. Falta una referencia explícita de TLS 1.3 para el retorno o un webhook real de prueba que llegue a una entrada configurada exclusivamente con TLS 1.3. Cotejar el identificador del mensaje, entrega, lectura cuando se informe y error, con deduplicación y verificación de firma. [Webhooks de Meta](https://developers.facebook.com/docs/graph-api/webhooks/getting-started/) |
| Volumen y costo | La hoja PROVEEDORES, fila 108, conserva AWS End User Messaging Social y deja el precio según plantilla y destino. Los 2.800/5.200 avisos diarios de INT-11 agregan todos los canales. Para conciliar Meta directa, separar la cuota de WhatsApp, proyectar mensajes facturables entregados por mes y multiplicarlos por la tarifa de utilidad del mercado del destinatario y tramo de volumen correspondientes. Registrar proveedor, costo unitario y tratamiento variable en la Oferta Económica cuando proceda. [Tarifas oficiales de Meta](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/) |

La evaluación se incorpora a 4-R. INT-11 conserva el proveedor ofertado mientras falten el respaldo del retorno y la conciliación económica. Su uso de TLS 1.2 se registra como brecha. Los dos requisitos permanecen parciales.

### Expediente de certificaciones del Sobre 1

RT-15.07 figura como «Cumple» con las constancias vigentes a la presentación de la oferta (25 de noviembre de 2026, T-20, actividad 12). El caso P01 conserva el cotejo documental previsto. La renovación de ISO/IEC 27001 se controla para el inicio del contrato en el seguimiento de RT-15.09.

| Constancia | Referencia del expediente | Acción pendiente |
|---|---|---|
| ISO 9001:2015 | `SIM-CERT-9001-0001`, Bureau Veritas, noviembre de 2028 | Cotejar titular, alcance y vigencia a la fecha de la oferta. |
| ISO/IEC 27001:2022 | `SIM-CERT-27001-0002`, AENOR, 22 de enero de 2027 | Obtener el respaldo de renovación previsto en SD1. Si el evaluador admite la alternativa del art. 34.1, preparar el plan formal firmado, con hitos verificables dentro de los primeros doce meses del contrato, y registrar su aceptación para efectos del requisito correspondiente. |
| CMMI-DEV nivel 3 | `SIM-CERT-CMMI-0003`, evaluación registrada hasta noviembre de 2026 | Obtener el resultado de la reevaluación y su ADS, identificado en SD1, sección 1.4. Si sigue pendiente, conservarla como antecedente de trayectoria en SD1 y distinguirla de las acreditaciones vigentes en el Sobre 1. |
| ISO/IEC 20000-1:2018 | `SIM-CERT-20000-0004`, SGS, mayo de 2027 | Cotejar titular, alcance y vigencia a la fecha de la oferta. |

El expediente debe registrar el código de verificación cuando lo emita el organismo o la constancia de que no corresponde. Las referencias `SIM-CERT` identifican las piezas del ejercicio. Fuentes: SD1, sección 1.4, y Sobre 1, Certificaciones del proponente.

### SD3-17 — Cuadrante B-02 de Operación

El Anexo 10.D, B-02 del SD10 recoge las seis nominaciones y dedicaciones de T-8 y siete filas de cobertura por tecnología. El SD12, sección 12.1.5, aporta perfiles de suplencia. El T-15 asigna 0 HH de Operación al perfil 12S, suplente propuesto de Integración. Si se utiliza ese perfil en M21–M56, queda por conciliar su dedicación o designar otra suplencia respaldada. Los compromisos de 12.D coinciden con las dedicaciones de coordinación del T-8. El Excel de referencia, hoja «HH POR ROL Y MES», confirma 0 HH en W16:BF16 para 12S, 962 HH en W40 para Mesa M21, 1.570 HH en AH40 para Mesa M32 y 696 HH en O44 para SOC M13. Las asignaciones individuales de guardia, la fecha de confirmación y su respaldo figuran pendientes.

**Solicitud de datos para Guillermo Castillo**

> Guillermo, estamos completando el Anexo 10.D, B-02 para cerrar SD3-17. ¿Puedes confirmar, para plataforma y nube, redes/NOC, seguridad/SOC, aplicaciones, datos, integraciones críticas y Mesa N1, quién será titular y suplente, qué competencia respalda cada asignación, en qué turno o ventana y período actuará, qué HH o porcentaje compromete y cuál será su canal de escalamiento? Necesitamos contrastar las asignaciones con T-8 y T-15, en especial el arranque del SOC en M13, el relevo de Mesa a NOC de 20:00 a 22:00 y los cuadrantes de M21 y M32. Por favor indica la fecha de validación y el respaldo de los responsables de cada área.

RT-21.03 y RT-21.03/P01 remiten al cuadrante B-02. Registrar validación con fecha, responsable, cobertura verificada y ubicación del respaldo. Conservar «Cumple parcialmente» mientras falten las asignaciones o su confirmación.

### Registro de cierre

Al recibir cada respuesta, guardar fecha, responsable, fuente y ubicación de la evidencia. Incorporarla en la rama de corrección del SD1, SD4 o SD10 según corresponda. Cambiar el estado en T-12 y T-13 únicamente cuando el respaldo cubra el criterio completo. Al regenerar el T-13, verificar las 653 filas y actualizar el recuento y los PDF. RT-15.08 ya figura como «Cumple» en los dos formularios.

## SD3-04 — Pruebas y criterios del T-12

Las dos partes del formulario incorporan «Prueba prevista o evidencia» antes del criterio. La columna identifica el caso o rango del T-13, el respaldo documental cuando corresponde y la remisión de los nueve alias. Las 22 filas «No cumple» figuran sin prueba prevista. La revisión reemplaza 336 frases genéricas por condiciones comprobables de las Bases y del caso, y explicita el alcance de las filas parciales. Los estados de la oferta se cotejan con la evidencia de ejecución.

| Fila o grupo | Comprobación específica pendiente |
|---|---|
| RT-03.24 | Contrastar la cobertura predictiva con la medición en las cámaras. |
| RT-07.04 y RNF-20.06 | Registrar el resultado para el escenario residual AL-DR-01. |
| RT-08.12 y RNF-23.02 | Completar las fichas de compra y verificar el resguardo del PAX A920 Pro. |
| RT-11.04 | Acreditar el plazo de remediación si el cambio de emergencia queda sin autorización durante congelamiento. |
| RT-16.18 | Comprobar la verificación de firma tras el vencimiento del certificado con el sello de tiempo previsto. |
| RT-16.23 y RF-18.03 | Obtener del proveedor evidencia de apertura por SMS si ofrece ese evento. |
| Punto 4 | Completar TLS por enlace, constancias del Sobre 1 y cuadrante B-02 según el registro anterior. |

### Cotejo vigente con SD9 y SD7

El T-12 `0167f99d`, el T-13 `a85b1dac` y el diccionario del T-14 `b3113e46` son las fuentes de este cotejo. El verificador confirma 653 IDs, 644 fichas, nueve alias, 1.223 casos por requisito y 105 por contrato. Los estados y códigos EDT coinciden entre formularios. La coincidencia del código EDT no acredita por sí sola que el paquete cubra todas las condiciones.

| Elemento | Acción pendiente |
|---|---|
| RF-17.09 | Incorporar al criterio del T-13 la edición de plantillas por el administrador, ya exigida por T-12 y el paquete 3.3.6. Mantener la generación y verificación en los tres formatos. |
| RF-18.03 | Incorporar al criterio del T-13 el registro de entrega, apertura y error. Verificar los estados según el canal y consignar la limitación de apertura de SMS. |
| RNF-14.01 y SD3-15 | El criterio individual del T-13 ya muestra el alcance del T-12. Seguridad y Arquitectura deben acreditar los extremos del inventario 4-R, incluidas las versiones del ERP y los terceros. Cualquier tramo exigido sin compatibilidad respaldada queda como brecha. Registrar su resolución antes de cerrar SD3-15. |
| RT-06.06, RT-11.25 y RT-18.09 | Describir en el criterio el documento o resultado que se comprobará. Ahora las tres filas reproducen su descripción. |
| RT-16.19 | El T-12 cita 5.2.4, cuyo entregable es la integración de avisos. Contrastar el requisito de plantillas con 3.3.6 y conciliar el alcance de formatos con RF-17.09. |
| RT-16.29 | El T-12 cita 3.3.2, cuyo entregable es auditoría de stock, lotes y cobros. Identificar el paquete que cubre la exportación asíncrona y su aviso sin bloquear la sesión. |
| RT-16.14 | Contrastar 3.3.4 para el motor de reglas y 4.3.3/5.1.1 para la relación entre prueba de entrega, guía y acuse. Separar las dos verificaciones en la ficha. |
| RT-26.01 y RT-26.03 | Trazar arquitectura y madurez a entregables o paquetes hoja. La referencia vigente identifica las cuentas 7.1 a 7.5. |

La matriz del SD3 incorpora las 17 observaciones del cuadro general del Informe 2 en `3201afc1`. SD3-16 está corregida en RT-15.04, que declara PUE e intensidad de carbono. SD3-17 sigue parcial hasta formalizar el cuadrante B-02. SD13-02 requiere alinear el texto de la matriz general con el T-12 y el SD13, que distinguen el modelo de RT-05.30 del aporte operacional de INN-03.

## Historial de cotejos anteriores

Los resultados siguientes corresponden a las instantáneas indicadas en el encabezado del documento. Las diferencias vigentes se registran en el cotejo anterior.

### Estados y alcances

Actualizar de «Cumple» a «Cumple parcialmente» las fichas siguientes, conservando el detalle de la parte cubierta y de la brecha:

| Identificador | Materia que no se acredita totalmente |
|---|---|
| RF-18.03, RT-16.23 | Apertura de cada SMS cuando el proveedor no la informa. |
| RNF-23.02, RT-08.12 | Grado IP del PAX y características aún condicionadas a la compra para determinados equipos. |
| RT-03.18, RT-08.14 | Todas las funciones remotas de gestión para todos los dispositivos de borde. |
| RT-11.04 | Plazos máximos de remediación si no se autoriza el cambio de emergencia durante congelamiento. |
| RNF-20.06, RT-07.04 | RPO de quince minutos ante el aislamiento de los tres enlaces seguido de destrucción del sitio antes de replicar. |

En el T-13 contrastado las nueve fichas todavía declaran «Cumple». Su procedimiento de prueba debe verificar tanto lo ofrecido como la limitación, sin presentar el requisito íntegro como aprobado. La matriz T-13 contiene 22 fichas parciales mientras su texto introductorio indica 18; T-12 contiene 31 filas parciales.

### Origen y alias

- Corregir en T-13 la transcripción de RT-07.09: las Bases y T-12 indican 3-2-1-1-0, no 3-2-1-0. Las 374 exigencias transversales y los 26 complementos del Caso coinciden en texto normalizado con las fuentes después de ese ajuste; la comparación textual no certifica la solución ni la prueba.
- Actualizar el origen de RF-09.09: capítulo 12 del Caso, no sección 12.
- Actualizar el origen de RF-12.10: retirar RT-10.05 como fuente de la ventana de entrega de 30 minutos; ese código trata la ventana operacional protegida.
- Declarar los requisitos absorbentes de RF-19.01 a RF-19.05: RT-11.03, RT-11.05, RT-11.13, RT-11.18 y RT-11.19, respectivamente. Mantener cero casos adicionales y seguir la prueba de la fila absorbente.
- Mantener los otros cuatro alias y su destino conforme al Anexo 3.A.5a; distinguir el RT-03.13 del Caso de los códigos transversales.

### Componentes, paquetes y pruebas

- Conciliar RF-01.09: T-12 distingue el evento `RecepcionConfirmada` que alimenta M2 de la solicitud al ERP encolada y procesada por INT-06/ACL con reintento automático. Verificar además que el paquete de integración y los casos previstos cubran el intercambio y la caída del ERP.
- Actualizar los 62 criterios de los catálogos RF modificados en SD3. Sus identificadores individuales aparecen en `auditoria_pendientes_sd3.csv` con `criterio_coincide_catalogo=False`; no se consideran diferencias de contenido las de mera puntuación o formato. Incorporar los cambios de componentes y referencias del mismo inventario y regenerarlo desde el SD3 definitivo.
- Para la columna de componentes, la comparación textual muestra 108 fichas con redacción distinta de la matriz T-13. Algunas diferencias son abreviaciones equivalentes y deben cotejarse por su alcance antes de actualizar; no deben interpretarse automáticamente como 108 errores funcionales.
- Conciliar en T-13 los estados parciales de RNF-20.06 y RT-07.04: el Anexo 4-M de SD4 describe el caso de aislamiento de los tres enlaces seguido de destrucción del sitio como brecha del RPO, sin asumir aceptada una excepción.
- Sustituir en RT-26.02 las cuentas 3.10 y 8.3 por los 23 paquetes hoja de las cinco innovaciones identificados en el T-12 actual. RT-26.01 y RT-26.03 siguen citando la cuenta 3.10 y requieren identificar si existe un paquete específico que cubra su propósito documental.
- Conciliar los nuevos ajustes de RF-01.05 (añade 3.4.2 para M2), RF-12.05 (M11 entrega el pedido a M3 y M4 lo planifica; añade 3.4.7), RF-12.12 (firma o fotografía y nombre según corresponda), RF-12.14 y RF-12.17. La descripción abreviada de M5 y de los portales se aplicó a RF-05.01, RF-05.02, RF-05.05, RF-05.07, RF-12.14 a RF-12.19, RF-12.22, RF-12.23, RF-12.26, RF-12.28 y RF-12.29.
- Corregir los nombres de herramientas en RNF-14.07, RT-04.05 y RT-11.22: PHPStan y PHPUnit, según corresponda. En RT-05.10 explicitar, como en T-12, que el catálogo con linaje automatizado no se oferta; la retención del Caso se mantiene y el cumplimiento sigue siendo parcial.
- Revisar las observaciones técnicas del cotejo de SD4 `04/revision/COTEJO_TRAZABILIDAD_CONTRACTUAL_SD4.md`: en particular RNF-20.06 y RT-07.04, por el escenario de aislamiento seguido de destrucción del sitio; RT-03.24, por las fuentes y la distinción entre estimación de cobertura y medición; y RT-16.18, por la suficiencia del sello temporal. Son hallazgos a contrastar, no resultados de pruebas ejecutadas ni cambios automáticos de estado.
- Conciliar los ajustes posteriores del T-12 en RF-01.11, RF-03.03, RF-04.08, RF-12.04, RF-12.16, RF-19.05 y RT-03.10. RF-03.03 incorpora el paquete 3.4.2 de Inventario; RT-03.10 incorpora 3.4.8 de Reparto para la jornada de 14 horas. El T-13 debe reflejar ambas fuentes en RT-03.10 y sus escenarios de 24 horas en el CD y 14 horas en terreno. No se han ejecutado esas pruebas.
- El diccionario T-14 de SD7, cuenta 3.3, identifica 3.3.5 con auditoría de stock, lotes y cobros: esa descripción no acredita por sí sola el motor de reglas y su parametrización (RF-17.02 y RT-16.14) ni toda la gestión documental (RF-17.08). La cuenta 3.6 identifica 3.6.4 con avisos a clientes: no demuestra por sí sola la generación general de documentos de RF-17.09. Se requiere asignar o definir paquetes que cubran esas funciones y conciliar T-12/T-13/T-14; no se inventan códigos de paquete en SD3.
- Conciliar las 40 fichas cuyo componente se abrevia en T-12: RF-01.01, RF-01.03 a RF-01.06, RF-01.08, RF-01.11, RF-02.01 a RF-02.03, RF-02.05, RF-02.07, RF-02.09, RF-03.01 a RF-03.08, RF-03.10 a RF-03.16, RF-04.01 a RF-04.05, RF-04.08, RF-12.02, RF-12.04, RF-12.05 y RF-12.07 a RF-12.09. Verificar que cada síntesis conserve la misma función y que las versiones sigan localizables en SD4 y T-11.
- RNF-23.01, RNF-23.02 y RT-08.11 ya usan en T-13 una síntesis con remisión al T-12; conservarla solo si refleja el componente vigente y el estado actualizado.
- RT-26.01 y RT-26.03 remiten a la cuenta 3.10. Seguir las tareas concretas de cada innovación en el T-14 y T-19 y verificar su pertinencia por requisito. Una cuenta no es un paquete hoja.
- Para RT-16.14, documentar escenarios diferenciados para el motor de reglas de las Bases Transversales y para la articulación de la prueba de entrega y el acuse exigida por el Caso. Verificar además los demás códigos RT compartidos por ambas fuentes sin presumir equivalencia de significado.
- Conciliar todas las demás discrepancias que surjan del cotejo semántico individual. Los identificadores `/Pnn` del formulario son pruebas previstas: completar sus pasos, datos, ambientes y evidencias en la etapa que el T-13 establece; no declarar una prueba ejecutada por su presencia en la matriz.

El inventario `auditoria_pendientes_sd3.csv` contiene las 653 filas, sus referencias y el resultado individual del examen de componentes. La mayoría tiene lectura preliminar y conserva pendiente el contraste semántico de fuente, alcance del paquete y suficiencia de prueba. La correspondencia de texto o números no prueba suficiencia semántica.
