# Formulario T-16: Plan de riesgos

**Fuente:** `Lafrox-Subdocumento-T-16.tex`. Conversión del contenido vigente: introducción, los 33 registros T-16 y referencias.

El registro sigue el formato del Formulario T-16, incluido en las Bases Administrativas (Distribuidora Puelche S.A., 2026a, Formulario T-16), y la norma ISO 31000 (International Organization for Standardization [ISO], 2018), conforme al RT-19.04 (Distribuidora Puelche S.A., 2026b). Sus riesgos se anclan en el Caso 02 (Distribuidora Puelche S.A., 2026c, caps. 10 y 19), cubren los temas del índice obligatorio indicado en el Formulario T-16 (Distribuidora Puelche S.A., 2026a) y se desarrollan en el Subdocumento 8 (LafroX, s. f.). El registro contiene los 33 riesgos incluidos en el CSV de análisis cualitativo disponible (R-001 a R-033). Prob. presenta el nivel cualitativo de probabilidad y su factor; Impacto presenta el nivel global cualitativo y su factor. Exposición y zona reproducen los valores del análisis cualitativo, no una estimación monetaria. La columna Mitigación conserva la columna del Formulario T-16 y presenta el disparador observable, la controlabilidad y la detectabilidad del CSV; no representa una acción de mitigación. El responsable corresponde al dueño propuesto en el análisis. Estos juicios cualitativos no son frecuencias observadas ni costos monetarios. El detalle de valores esperados está en el Anexo 8.B; la evaluación de respuestas se desarrolla en el cuerpo del Subdocumento 8. Cada responsable dirige su equipo. DAT e IMP conservan su familia de esfuerzo, pero desde el mes 22 la responsabilidad pasa al Líder de Operación / SRE (SD8, Tabla 8.1). No se establece aquí una reserva cuantitativa.

## R-001

- **Riesgo:** Dado que la habilitación EDI de cada cadena depende de su participación y certificación externa antes de las cuatro semanas finales de evidencia de E2, entonces puede que una cadena incluida en el alcance no complete su participación o certificación EDI antes de la fecha requerida, teniendo como consecuencia que no se acredite completo el intercambio electrónico exigido en E2 y deban reprogramarse pruebas y coordinación.
- **Categoría:** Integración y legado
- **Prob.:** 3 / 0,50
- **Impacto:** 4 / 0,40
- **Expos.:** 0,20 (Alta)
- **Mitigación:** Escalar. La certificación de la cadena depende de una decisión externa que LafroX no puede sustituir. Elevar a la Contraparte Técnica el bloqueo y acordar compromisos de certificación antes de 28 días. La carga manual no acredita E2 ni permite retirar cadenas del alcance.
- **Responsable:** Líder de integraciones

## R-002

- **Riesgo:** Dado que la migración sanitaria utiliza antecedentes del ERP, WMS y planillas y requiere vínculos históricos verificables con evidencia de origen, entonces puede que los datos recibidos contengan faltantes de lote o vínculos históricos que no puedan resolverse con esa evidencia, teniendo como consecuencia que la carga sanitaria afectada quede pendiente de conciliación y decisión documentada, y aumente el trabajo de saneamiento.
- **Categoría:** Solución y tecnología
- **Prob.:** 4 / 0,70
- **Impacto:** 5 / 0,80
- **Expos.:** 0,56 (Crítica)
- **Mitigación:** Escalar. La zona crítica exige decisión de Calidad y del cliente sobre conjuntos cuya historia no puede reconstruirse con evidencia. Elevar el impedimento de aceptación y exigir resolución formal antes del corte. El saneamiento técnico apoya la respuesta; no elimina la falta de historia ni autoriza inventar lotes.
- **Responsable:** Líder de datos

## R-003

- **Riesgo:** Dado que la migración y la reposición dependen de la extensión y calidad efectiva del historial de ventas disponible en el ERP, entonces puede que el historial extraído tenga períodos incompletos o datos que no puedan utilizarse directamente, teniendo como consecuencia que deban ampliarse la preparación y conciliación de la carga y el tratamiento de excepciones de reposición.
- **Categoría:** Integración y legado
- **Prob.:** 3 / 0,50
- **Impacto:** 3 / 0,20
- **Expos.:** 0,10 (Media)
- **Mitigación:** Aceptar activamente. Conservar el tratamiento de excepciones de reposición y prever contingencia para preparación y conciliación adicionales. Activar al comprobar períodos incompletos o inutilizables en V-09. La aceptación se refiere al costo adicional, no a omitir la historia exigida.
- **Responsable:** Líder de datos

## R-004

- **Riesgo:** Dado que la aceptación del inventario migrado requiere conciliar los saldos legados con el conteo físico y aprobar las explicaciones y ajustes antes del corte, entonces puede que se detecten diferencias sin explicación y ajuste aprobados a tiempo, teniendo como consecuencia que deban repetirse el saneamiento y la validación, y la carga afectada no pueda ser aceptada hasta resolverlas.
- **Categoría:** Operación del cliente
- **Prob.:** 4 / 0,70
- **Impacto:** 3 / 0,20
- **Expos.:** 0,14 (Media)
- **Mitigación:** Aceptar activamente. Prever contingencia para repetir conciliación y validación cuando existan diferencias sin explicación o ajuste aprobado antes del corte. Mantener el no-go de la carga hasta resolverlas. Se acepta el esfuerzo adicional, no diferencias de inventario sin justificar.
- **Responsable:** Líder de migración

## R-005

- **Riesgo:** Dado que la carga inicial de M8 requiere saldos de envases por cliente y transportista sustentados en antecedentes conciliables del cliente, entonces puede que los antecedentes entregados no permitan determinar un saldo conciliado por cliente y transportista, teniendo como consecuencia que deban repetirse la preparación y validación de la carga y no pueda demostrarse M8 con saldos iniciales aceptados.
- **Categoría:** Operación del cliente
- **Prob.:** 3 / 0,50
- **Impacto:** 3 / 0,20
- **Expos.:** 0,10 (Media)
- **Mitigación:** Aceptar activamente. Prever contingencia para preparar y validar nuevamente los saldos de M8 con Finanzas. Activar si V-08 no obtiene un saldo conciliable por cliente y transportista. Mantener pendiente la aceptación de la carga mientras falte el saldo aprobado.
- **Responsable:** Líder de migración

## R-006

- **Riesgo:** Dado que las comparaciones históricas de aceptación dependen de horas verificables de entrega y montos esperados de rendición que la captura futura no reconstruye, entonces puede que falten horas verificables de entrega o montos esperados de rendición en los antecedentes históricos, teniendo como consecuencia que no puedan respaldarse con esos registros las comparaciones de OTIF o cuadratura y deba repetirse la validación del período de referencia.
- **Categoría:** Operación del cliente
- **Prob.:** 4 / 0,70
- **Impacto:** 3 / 0,20
- **Expos.:** 0,14 (Media)
- **Mitigación:** Escalar. La selección de registros y período histórico aceptable corresponde a Comercial, Operaciones y Finanzas. Solicitar decisión formal si V-10 no obtiene evidencia verificable. No sustituir unilateralmente la línea base ni presentar captura futura como reconstrucción histórica.
- **Responsable:** Líder funcional

## R-007

- **Riesgo:** Dado que el volumen histórico utilizado para estimar la carga de cartera no acredita que incluya todos los documentos de deuda todavía vigente, entonces puede que se identifiquen documentos de deuda vigente fuera del volumen histórico considerado, teniendo como consecuencia que deban extraerse, transformarse y conciliarse datos adicionales, aumentando el trabajo y el volumen de transferencia de la migración de cartera.
- **Categoría:** Integración y legado
- **Prob.:** 3 / 0,50
- **Impacto:** 3 / 0,20
- **Expos.:** 0,10 (Media)
- **Mitigación:** Aceptar activamente. Prever contingencia para extraer, transformar y conciliar deuda viva adicional. Activar cuando el perfilado detecte documentos vigentes fuera del extracto provisional. Se acepta el retrabajo acotado, manteniendo la obligación de cartera completa.
- **Responsable:** Líder de datos

## R-008

- **Riesgo:** Dado que los trámites tributarios se envían por el sistema de gestión actual del cliente y requieren respuesta del Servicio de Impuestos Internos (SII) para conocer su resultado, entonces puede que el SII no responda mientras se tramita un documento, teniendo como consecuencia que el trámite quede sin confirmación y se retrase su cierre mientras se gestiona y comprueba la respuesta, sin que el silencio equivalga a aprobación.
- **Categoría:** Integración y legado
- **Prob.:** 1 / 0,10
- **Impacto:** 3 / 0,20
- **Expos.:** 0,02 (Baja)
- **Mitigación:** Aceptar pasivamente. Mantener la observación de pendientes y los controles ya previstos para consultar y conciliar el resultado tributario. No proponer inversión preventiva adicional con esta valoración. La ausencia de respuesta no autoriza aprobar el trÁmite ni cerrar el proceso.
- **Responsable:** Líder de operación / SRE

## R-009

- **Riesgo:** Dado que la integración de pagos depende de la respuesta del POS de un tercero y un timeout no permite concluir que el cargo fue rechazado, entonces puede que el POS agote el tiempo de respuesta sin permitir comprobar si se efectuó el cargo, teniendo como consecuencia que el estado del pago quede incierto y sea necesario investigar y conciliarlo con la contraparte financiera antes de resolver la incidencia.
- **Categoría:** Integración y legado
- **Prob.:** 3 / 0,50
- **Impacto:** 3 / 0,20
- **Expos.:** 0,10 (Media)
- **Mitigación:** Aceptar activamente. Prever contingencia para investigar y conciliar resultados inciertos del POS. Activar ante timeout sin confirmación del cargo, consultando la misma clave antes de reintentar. Mantener los controles existentes; no asumir custodia del dinero ni dar por transferido el riesgo al proveedor.
- **Responsable:** Líder de integraciones

## R-010

- **Riesgo:** Dado que la consulta de ubicaciones y la planificación de rutas dependen de un servicio externo de mapas, entonces puede que el servicio externo deje de estar disponible durante la operación, teniendo como consecuencia que se retrasen o interrumpan las tareas de planificación que dependen del servicio y deban atenderse la incidencia y la recuperación.
- **Categoría:** Integración y legado
- **Prob.:** 1 / 0,10
- **Impacto:** 3 / 0,20
- **Expos.:** 0,02 (Baja)
- **Mitigación:** Aceptar pasivamente. Observar disponibilidad y conservar los mecanismos existentes de ruta aprobada y cartografía precargada. Ante caída, aplicar continuidad y comprobar recuperación. Con la zona baja y el VME registrado no se propone contratar una alternativa adicional sin justificar su beneficio.
- **Responsable:** Líder de operación / SRE

## R-011

- **Riesgo:** Dado que la certificación de la parametrización térmica requiere una matriz de umbrales y duraciones por producto aprobada por Calidad del cliente, entonces puede que Calidad no apruebe esa matriz antes del cierre de las pruebas y la marcha blanca de los productos afectados, teniendo como consecuencia que no pueda completarse la evidencia de parametrización y aceptación del alcance térmico y deban reprogramarse validaciones.
- **Categoría:** Operación del cliente
- **Prob.:** 3 / 0,50
- **Impacto:** 5 / 0,80
- **Expos.:** 0,40 (Crítica)
- **Mitigación:** Escalar. La zona crítica depende de una aprobación que solo puede emitir Calidad. Elevar de inmediato la matriz pendiente y exigir decisión formal antes de certificar. Mantener tratamiento térmico preventivo y prohibición de cerrar la marcha blanca sin parÁmetros aprobados; LafroX no puede aprobarlos por el cliente.
- **Responsable:** Líder funcional de Calidad

## R-012

- **Riesgo:** Dado que el cliente compra el equipamiento de terreno conforme a la especificación de LafroX y debe disponer de él antes de cada ola, entonces puede que el cliente o su proveedor no entregue el equipamiento antes de la ola programada, teniendo como consecuencia que no puedan ejecutarse con esos equipos la instalación y las pruebas previstas y deban reprogramarse despliegue y acompañamiento.
- **Categoría:** Operación del cliente
- **Prob.:** 2 / 0,30
- **Impacto:** 4 / 0,40
- **Expos.:** 0,12 (Media)
- **Mitigación:** Escalar. La adquisición y entrega de equipos de terreno corresponde al cliente y su proveedor. Elevar el faltante a la Contraparte Técnica antes de la ola y obtener una decisión de entrega y disponibilidad. No comprar por cuenta del cliente ni asumir una transferencia contractual no acreditada.
- **Responsable:** Líder de implantación

## R-013

- **Riesgo:** Dado que la incorporación de cada empresa transportista al reparto requiere que su acuerdo operativo esté firmado antes de la ola correspondiente, entonces puede que una empresa transportista no firme el acuerdo a tiempo, teniendo como consecuencia que sus conductores no puedan incorporarse ni completar las pruebas de esa ola y quede pendiente demostrar la cobertura del transportista.
- **Categoría:** Personas y adopción
- **Prob.:** 3 / 0,50
- **Impacto:** 3 / 0,20
- **Expos.:** 0,10 (Media)
- **Mitigación:** Escalar. La firma requiere decisión del cliente y del transportista, fuera de la autoridad de LafroX. Elevar el acuerdo pendiente antes de incorporar esa empresa y obtener compromiso formal. No habilitar conductores sin acuerdo ni considerar acreditada su cobertura por mera reprogramación.
- **Responsable:** Líder de implantación

## R-014

- **Riesgo:** Dado que la instalación de termógrafos en camiones refrigerados de terceros requiere acceso al vehículo y autorización de su propietario, entonces puede que el propietario niegue el acceso o la autorización para instalar el equipo, teniendo como consecuencia que no pueda instalarse ni integrarse el termógrafo antes de incorporar la ruta y quede pendiente la evidencia de temperatura.
- **Categoría:** Operación del cliente
- **Prob.:** 2 / 0,30
- **Impacto:** 4 / 0,40
- **Expos.:** 0,12 (Media)
- **Mitigación:** Escalar. La autorización de acceso al camión pertenece a su propietario. Elevar la negativa con la Contraparte Técnica y resolver acceso o alternativa autorizada antes de integrar la ruta. No instalar sin consentimiento ni excluir la evidencia térmica comprometida.
- **Responsable:** Líder de implantación

## R-015

- **Riesgo:** Dado que la implantación exige que los usuarios incorporen sus transacciones al registro oficial de la solución, entonces puede que parte de los usuarios continúe registrando exclusivamente en el procedimiento anterior durante una ola, teniendo como consecuencia que no pueda acreditarse la cobertura de adopción requerida para cerrar esa ola y deba extenderse la intervención de implantación.
- **Categoría:** Personas y adopción
- **Prob.:** 4 / 0,70
- **Impacto:** 4 / 0,40
- **Expos.:** 0,28 (Alta)
- **Mitigación:** Mitigar. Reducir el uso exclusivo del procedimiento anterior mediante piloto y acompaÃ±amiento focalizado por turno, verificando transacciones efectivamente incorporadas al registro oficial. Actuar durante implantación. Antes de aprobar trabajo adicional, costearlo y exigir que cueste menos que la reducción del VME; esa rentabilidad aÃºn no estÁ calculada.
- **Responsable:** Líder de gestión del cambio

## R-016

- **Riesgo:** Dado que parte de las reglas y excepciones de rutas reside en el planificador del cliente y debe transferirse y validarse mientras esté disponible, entonces puede que el planificador deje de estar disponible antes de transferir las excepciones aún no documentadas, teniendo como consecuencia que deba reconstruirse y validarse ese conocimiento con el ayudante y antecedentes históricos, afectando talleres y pruebas de rutas.
- **Categoría:** Personas y adopción
- **Prob.:** 2 / 0,30
- **Impacto:** 5 / 0,80
- **Expos.:** 0,24 (Alta)
- **Mitigación:** Mitigar. Capturar y validar tempranamente excepciones con el planificador, documentar reglas y comprobar su transferencia al ayudante antes de que deje de estar disponible. Actuar en meses 1â€“3. Costear el trabajo adicional y compararlo con la reducción del VME antes de aprobarlo; no suponer que la indisponibilidad se elimina.
- **Responsable:** Líder funcional de rutas

## R-017

- **Riesgo:** Dado que la capacitación y certificación deben realizarse sin detener pedidos, ventas ni reparto, y el cliente debe disponer de los usuarios en los horarios acordados, entonces puede que las necesidades operativas impidan que algunos usuarios asistan a formación y evaluación antes del cierre de su ola, teniendo como consecuencia que deban reprogramarse sesiones y acompañamiento y no pueda acreditarse que esos usuarios están preparados hasta que completen la evaluación.
- **Categoría:** Personas y adopción
- **Prob.:** 2 / 0,30
- **Impacto:** 3 / 0,20
- **Expos.:** 0,06 (Baja)
- **Mitigación:** Aceptar pasivamente. Respetar la zona baja asignada por el equipo y observar asistencia y certificaciones con los controles existentes. Si faltan usuarios, reprogramar su formación y evaluación sin declarar cobertura completa. El VME no demuestra que se haya aprobado una reserva o una nueva acción preventiva.
- **Responsable:** Líder de capacitación

## R-018

- **Riesgo:** Dado que los diseños, pruebas y aceptaciones incluyen actividades que dependen de validaciones o decisiones de áreas del cliente, entonces puede que el área requerida no entregue una validación o decisión en la fecha acordada, teniendo como consecuencia que se detengan o repitan tareas dependientes, se consuma holgura y deban reprogramarse recursos.
- **Categoría:** Operación del cliente
- **Prob.:** 3 / 0,50
- **Impacto:** 4 / 0,40
- **Expos.:** 0,20 (Alta)
- **Mitigación:** Escalar. La validación requerida compete al Área del cliente y su demora excede la autoridad del jefe de proyecto. Elevar el bloqueo a la Contraparte Técnica o comité con la tarea e hito afectados y exigir decisión formal. No tratar el escalamiento como autorización para cambiar fechas o aceptar entregables.
- **Responsable:** Jefe de proyecto

## R-019

- **Riesgo:** Dado que los sitios dependen de servicios externos de fibra, LTE o satélite para conectarse con los servicios centrales, entonces puede que el proveedor interrumpa el enlace utilizado durante pruebas u operación, teniendo como consecuencia que se limite la conexión con servicios centrales y deban gestionarse la restitución y la sincronización posterior.
- **Categoría:** Operación del cliente
- **Prob.:** 1 / 0,10
- **Impacto:** 3 / 0,20
- **Expos.:** 0,02 (Baja)
- **Mitigación:** Aceptar pasivamente. Observar enlaces y edad de colas y mantener la continuidad local y respaldos ya ofertados. Ante corte, coordinar restitución y verificar sincronización. No aÃ±adir una nueva contratación preventiva con esta valoración ni imputar también a SII, POS o mapas la atención del mismo fallo WAN.
- **Responsable:** Líder de operación / SRE

## R-020

- **Riesgo:** Dado que algunos equipos de infraestructura dependen del suministro eléctrico y tienen respaldo de autonomía limitada, entonces puede que un corte de electricidad supere la autonomía del respaldo aplicable en un sitio atendido por LafroX, teniendo como consecuencia que los equipos afectados dejen de prestar servicio hasta restablecer la energía o recuperar la infraestructura.
- **Categoría:** Operación del cliente
- **Prob.:** 1 / 0,10
- **Impacto:** 4 / 0,40
- **Expos.:** 0,04 (Baja)
- **Mitigación:** Aceptar pasivamente. Observar suministro y autonomía del respaldo existente. Si se supera, atender solo los componentes mantenidos por LafroX y verificar su restitución. Conservar la zona baja sin aÃ±adir capacidad eléctrica ni atribuir pérdidas operacionales del cliente al impacto del proyecto.
- **Responsable:** Líder de operación / SRE

## R-021

- **Riesgo:** Dado que la solución propone operar y recuperarse en regiones de nube de Brasil y Estados Unidos, y el tratamiento y transferencia internacional requieren aprobación del cliente, entonces puede que el cliente no otorgue la aprobación necesaria sobre residencia y transferencia de datos al habilitar esos entornos, teniendo como consecuencia que no pueda completarse la habilitación o la evidencia de recuperación afectada hasta resolver formalmente la condición.
- **Categoría:** Regulatorio y externo
- **Prob.:** 2 / 0,30
- **Impacto:** 4 / 0,40
- **Expos.:** 0,12 (Media)
- **Mitigación:** Escalar. La aprobación de residencia y tratamiento de datos corresponde al cliente. Elevar la decisión pendiente con los antecedentes de arquitectura y seguridad antes de habilitar los entornos afectados. No desplegar por cuenta propia en otra región ni afirmar aprobación o licitud no acreditadas.
- **Responsable:** Arquitecto de solución

## R-022

- **Riesgo:** Dado que una intervención para remediar un incidente o vulnerabilidad durante un período congelado requiere autorización del cliente, entonces puede que el cliente no autorice el cambio de emergencia solicitado, teniendo como consecuencia que deba sostenerse la contención y gestionarse el conflicto entre la fecha habilitada y el plazo de remediación, sin que ello implique una exención contractual.
- **Categoría:** Operación del cliente
- **Prob.:** 2 / 0,30
- **Impacto:** 5 / 0,80
- **Expos.:** 0,24 (Alta)
- **Mitigación:** Escalar. La intervención durante un congelamiento requiere autorización escrita del cliente. Elevar el conflicto entre ventana prohibida y plazo de remediación, con evidencia y contención aplicada. Mantener contención mientras se resuelve; la negativa no acredita exención contractual ni permite intervenir sin autorización.
- **Responsable:** Encargado de seguridad

## R-023

- **Riesgo:** Dado que las credenciales pueden ser obtenidas mediante engaño, phishing u otros métodos y usadas sin autorización, entonces puede que un tercero utilice credenciales ajenas para autenticarse como otra persona e intente registrar pedidos o acceder a portales, teniendo como consecuencia que deban investigarse y contenerse los accesos u operaciones afectados y, si la suplantación tiene éxito, puedan atribuirse acciones al titular legítimo.
- **Categoría:** Solución y tecnología
- **Prob.:** 2 / 0,30
- **Impacto:** 5 / 0,80
- **Expos.:** 0,24 (Alta)
- **Mitigación:** Mitigar. Reforzar la verificación de identidad segÃºn perfil, revisar privilegios y probar detección, revocación y trazabilidad de operaciones ante credenciales comprometidas. Actuar antes y durante operación. Costear cualquier refuerzo y comprobar ahorro esperado superior al costo; no inventar probabilidades residuales ni duplicar controles ya incluidos.
- **Responsable:** Encargado de seguridad

## R-024

- **Riesgo:** Dado que la solución recibe de cadenas comerciales mensajes electrónicos de pedidos y avisos de despacho mediante sistemas externos, entonces puede que llegue un mensaje que aparente provenir de una cadena autorizada sin serlo, o cuyo contenido haya sido alterado, teniendo como consecuencia que deba aislarse e investigarse el mensaje antes de procesar operaciones y, si se acepta, pueda alterarse el pedido o aviso correspondiente.
- **Categoría:** Integración y legado
- **Prob.:** 1 / 0,10
- **Impacto:** 3 / 0,20
- **Expos.:** 0,02 (Baja)
- **Mitigación:** Aceptar pasivamente. Mantener observación y validaciones existentes de origen, integridad y correlación EDI. Aislar e investigar mensajes sospechosos antes de procesarlos. Se acepta la exposición residual de zona baja; nunca se acepta como vÁlido un mensaje falso ni se contrata cobertura adicional sin evaluación.
- **Responsable:** Líder de integraciones

## R-025

- **Riesgo:** Dado que los terminales enrolados se utilizan físicamente en ruta y bodega y contienen datos locales asociados a usuarios autorizados, entonces puede que un terminal enrolado se pierda o quede en poder de una persona distinta de su usuario autorizado, teniendo como consecuencia que deban investigarse la posible exposición de datos locales y contenerse accesos indebidos al dispositivo.
- **Categoría:** Solución y tecnología
- **Prob.:** 2 / 0,30
- **Impacto:** 4 / 0,40
- **Expos.:** 0,12 (Media)
- **Mitigación:** Aceptar activamente. Prever contingencia para atender pérdida de custodia y activar los controles existentes de bloqueo, revocación y borrado del terminal. El disparador es el aviso de extravío o uso por persona no autorizada. La cobertura se limita a gestión de dispositivo y datos; no incluye reposición de hardware.
- **Responsable:** Líder de operación / SRE

## R-026

- **Riesgo:** Dado que los portales e interfaces públicas están expuestos a solicitudes de actores externos, entonces puede que un actor dirija ráfagas abusivas de solicitudes para impedir accesos legítimos, teniendo como consecuencia que se degraden los accesos públicos y se requiera contención y verificación de la disponibilidad del servicio.
- **Categoría:** Solución y tecnología
- **Prob.:** 2 / 0,30
- **Impacto:** 4 / 0,40
- **Expos.:** 0,12 (Media)
- **Mitigación:** Transferir â€” propuesta condicionada. Evaluar asignación contractual expresa a un proveedor especializado de la responsabilidad y costo de respuesta DDoS, con cobertura verificable. Solo formalizar si el costo es menor que la reducción del VME. WAF/Shield por sí solos no prueban transferencia; sin contrato aceptado no se considera transferido ni se reduce la valoración.
- **Responsable:** Encargado de seguridad

## R-027

- **Riesgo:** Dado que las cuentas administrativas están expuestas a campañas de phishing y pueden dar acceso privilegiado a la plataforma, entonces puede que un atacante obtenga credenciales administrativas y las utilice para borrar o alterar respaldos o evidencia, teniendo como consecuencia que deban contenerse los accesos comprometidos e investigarse y verificarse la integridad y recuperabilidad de los conjuntos afectados.
- **Categoría:** Solución y tecnología
- **Prob.:** 2 / 0,30
- **Impacto:** 5 / 0,80
- **Expos.:** 0,24 (Alta)
- **Mitigación:** Mitigar. Separar privilegios administrativos de la custodia de copias, reforzar autenticación y verificar inmutabilidad y restauración mediante pruebas. Actuar antes y durante operación. Costear solo refuerzos adicionales y contrastarlos con reducción del VME antes de aprobar; no asumir eliminación del riesgo ni modificar el residual sin evidencia.
- **Responsable:** Encargado de seguridad

## R-028

- **Riesgo:** Dado que los recorridos de prueba se realizan en camiones cuyo funcionamiento mecánico es necesario para completarlos, entonces puede que un camión sufra una falla mecánica durante el recorrido, teniendo como consecuencia que se interrumpa el recorrido y no se completen los casos de prueba programados, por lo que deba repetirse la validación.
- **Categoría:** Operación del cliente
- **Prob.:** 2 / 0,30
- **Impacto:** 2 / 0,10
- **Expos.:** 0,03 (Baja)
- **Mitigación:** Aceptar pasivamente. Observar la disponibilidad del recorrido y, si una falla interrumpe las pruebas, coordinar su repetición con el cliente. La zona baja no justifica por sí sola una acción preventiva nueva. Limitar el efecto de LafroX a tiempo y recursos de validación, sin cubrir mantenimiento del camión.
- **Responsable:** Líder de implantación

## R-029

- **Riesgo:** Dado que los casos de prueba y la evidencia de aceptación requieren completar el recorrido del camión, entonces puede que el camión se vea envuelto en un accidente de tránsito durante el recorrido, teniendo como consecuencia que se interrumpan los casos de prueba y deba coordinarse la repetición de validaciones, consumiendo tiempo y recursos de implantación.
- **Categoría:** Operación del cliente
- **Prob.:** 1 / 0,10
- **Impacto:** 2 / 0,10
- **Expos.:** 0,01 (Baja)
- **Mitigación:** Aceptar pasivamente. Ante aviso de siniestro, coordinar con el cliente otro recorrido autorizado para completar los casos pendientes. Mantener vigilancia ordinaria sin nueva respuesta preventiva. No imputar a LafroX lesiones, indemnizaciones ni reposición de vehículo o carga.
- **Responsable:** Líder de implantación

## R-030

- **Riesgo:** Dado que los recorridos de prueba requieren que el camión llegue al destino previsto para completar los casos y reunir evidencia, entonces puede que el camión sea asaltado, robado o incendiado durante el recorrido, teniendo como consecuencia que se interrumpa la validación y deban reprogramarse y repetirse las pruebas afectadas, con posible consumo adicional de tiempo y recursos.
- **Categoría:** Operación del cliente
- **Prob.:** 1 / 0,10
- **Impacto:** 2 / 0,10
- **Expos.:** 0,01 (Baja)
- **Mitigación:** Aceptar pasivamente. Ante interrupción por asalto, esperar la habilitación segura del cliente y coordinar repetición de las validaciones pendientes. La aceptación cubre la exposición del proyecto en zona baja. No asumir custodia de bienes, pérdidas delictuales o responsabilidad por seguridad del transporte.
- **Responsable:** Líder de implantación

## R-031

- **Riesgo:** Dado que los conductores externos requieren comunicación, autorización y capacitación para utilizar la solución, entonces puede que un transportista presente sin aviso a un reemplazo que aún no esté autorizado o capacitado, teniendo como consecuencia que deban atenderse su habilitación y formación y verificarse las entregas afectadas antes de cerrar la evidencia de la ola.
- **Categoría:** Personas y adopción
- **Prob.:** 3 / 0,50
- **Impacto:** 3 / 0,20
- **Expos.:** 0,10 (Media)
- **Mitigación:** Aceptar activamente. Prever contingencia para habilitación y formación extraordinaria del sustituto. Activar al presentarse un conductor no autorizado o no certificado, respetando el acuerdo del transportista y verificando los registros afectados. No duplicar sesiones ya imputadas a capacitación general.
- **Responsable:** Líder de capacitación

## R-032

- **Riesgo:** Dado que la solución tiene un alcance delimitado por requisitos, exclusiones y decisiones aprobadas, contra el cual deben evaluarse las solicitudes posteriores, entonces puede que la contraparte solicite una función, integración o modificación que exceda el alcance y requiera trabajo adicional, teniendo como consecuencia que deba evaluarse y tramitarse el cambio y, si se aprueba, ajustarse esfuerzo, costo o programación según el impacto acordado.
- **Categoría:** Contrato y licitación
- **Prob.:** 3 / 0,50
- **Impacto:** 3 / 0,20
- **Expos.:** 0,10 (Media)
- **Mitigación:** Aceptar activamente. Prever contingencia para evaluar y tramitar solicitudes fuera de la línea base. Activar al identificar una petición que exceda el alcance acordado y llevarla al control de cambios. Aceptar su evaluación no autoriza implementarla sin aprobación y ajuste contractual; el desarrollo aprobado no forma parte de este impacto.
- **Responsable:** Jefe de proyecto

## R-033

- **Riesgo:** Dado que la solución trata y conserva documentos, ubicación y evidencia durante una vigencia contractual de varios años sujeta a exigencias normativas, entonces puede que una modificación normativa o nueva interpretación aplicable exija ajustar controles, conservación o eliminación de datos, teniendo como consecuencia que deban adaptarse y validarse componentes y procedimientos afectados, con trabajo adicional y posibles ajustes de programación sujetos al contrato.
- **Categoría:** Regulatorio y externo
- **Prob.:** 2 / 0,30
- **Impacto:** 4 / 0,40
- **Expos.:** 0,12 (Media)
- **Mitigación:** Escalar. La interpretación normativa y la decisión sobre obligaciones y cambios contractuales requieren autoridad del cliente y asesoría competente. Elevar el cambio aplicable para definir alcance y financiación, y luego planificar adecuación técnica. No inventar reformas, multas ni cobertura contractual.
- **Responsable:** Arquitecto de solución

## Referencias
Las fuentes citadas en este documento se listan en formato APA 7.ª edición. Las Bases se citan en el texto con su documento y el artículo, capítulo, sección o código del requisito.
\begingroup
Distribuidora Puelche S.A. (2026a). *Bases Administrativas de Licitación N.º TFEP-01/2026: Contratación de Solución Integral de Software y Servicios de Operación*.
Distribuidora Puelche S.A. (2026b). *Bases Técnicas Transversales de Licitación N.º TFEP-01/2026*.
Distribuidora Puelche S.A. (2026c). *Caso 02: Logística. Especificaciones del problema y operación de Distribuidora Puelche S.A.}
International Organization for Standardization. (2018). *ISO 31000:2018 Risk management — Guidelines*. https://www.iso.org/standard/65694.html
LafroX. (s. f.). *Subdocumento 8: Plan de riesgos*.
