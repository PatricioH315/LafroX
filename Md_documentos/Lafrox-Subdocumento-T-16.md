# Formulario T-16: Plan de riesgos

**Fuente:** `Lafrox-Subdocumento-T-16.tex`. Conversión completa: texto introductorio, los 45 registros T-16, referencias y declaración de uso de IA.

El registro sigue el formato del Formulario T-16 (Distribuidora Puelche S.A., 2026a) y la norma ISO 31000 (International Organization for Standardization [ISO], 2018), conforme al RT-19.04 (Distribuidora Puelche S.A., 2026b). Sus riesgos se anclan en el Caso 02 (Distribuidora Puelche S.A., 2026c, caps. 10 y 19), cubren los temas del índice obligatorio (Distribuidora Puelche S.A., 2026d, sección 11) y se desarrollan en el Subdocumento 8 (LafroX, 2026). El registro contiene 45 riesgos de referencia. Las columnas Prob. e Impacto presentan cada una el nivel ordinal cualitativo y, tras una barra, el valor decimal exacto de su ponderación cualitativa. Estos valores decimales son ponderaciones cualitativas: no representan frecuencias observadas de eventos, estimaciones cuantitativas p₀ ni proporciones de pérdida financiera o de esfuerzo. La columna Exposición muestra el producto decimal de las ponderaciones cualitativas ($q_P\times q_I$) y la zona registrada y adoptada para cada riesgo; los niveles ordinales de P e I permanecen visibles junto a sus valores decimales. El análisis esperado en HH es separado y no forma parte de esta exposición. Las mitigaciones propuestas corresponden a las respuestas indicadas y su eficacia aún está pendiente de verificar. Es la evaluación inicial; ningún riesgo tiene cierre acreditado. El detalle de valores esperados está en el Anexo 8.B; el costo-beneficio de las respuestas, en el Anexo 8.C. Cada responsable dirige su equipo. DAT e IMP conservan su familia de esfuerzo, pero desde el mes 22 la responsabilidad pasa al Líder de Operación / SRE (SD8, Tabla 8.1). No se establece aquí una reserva cuantitativa.


> **Nota:** La exposición cualitativa $q_P\times q_I$ es distinta del valor esperado cuantitativo $p_0\times HH$; el análisis esperado en HH no forma parte de la exposición de esta tabla.

## R-001

- **Riesgo:** Dado que el ERP no cuenta con documentación de interfaces ni permiso para modificarlo, puede que la interfaz disponible no soporte los contratos necesarios, teniendo como consecuencia retrabajo de la ACL y atraso de integración
- **Categoría:** Integración y legado
- **Probabilidad:** 3 / 0,50
- **Impacto:** 2 / 0,40
- **Exposición:** 0,20 (Alta)
- **Mitigación:** Mitigar — Probar lectura, escritura autorizada y emisión con el proveedor; cerrar contrato de interfaz. Validar: Contrato firmado, extracción real, rechazo y reintento probados; no basta OpenAPI interno
- **Responsable:** Bastián Trejo

## R-002

- **Riesgo:** Dado que el cliente desconoce condiciones contractuales de acceso a los datos, puede que el tercero limite API, cuotas o historia, teniendo como consecuencia ingesta incompleta de la flota propia
- **Categoría:** Integración y legado
- **Probabilidad:** 3 / 0,50
- **Impacto:** 1 / 0,20
- **Exposición:** 0,10 (Media)
- **Mitigación:** Mitigar — Acordar licencia de datos, cuotas y prueba de extracción; exigir procedimiento de cambio. Validar: Autorización escrita y prueba de posición/historia con límites contratados
- **Responsable:** Bastián Trejo

## R-003

- **Riesgo:** Dado que el WMS de 2013 y los registros físicos conviven durante la transición, puede que el corte deje saldos divergentes o tareas sin dueño, teniendo como consecuencia reversión y extensión de la convivencia
- **Categoría:** Integración y legado
- **Probabilidad:** 3 / 0,50
- **Impacto:** 2 / 0,40
- **Exposición:** 0,20 (Alta)
- **Mitigación:** Mitigar — Ejecutar un ensayo adicional de delta y reversión con pendientes de recepción, picking y retornos. Validar: Conciliación aprobada por bodega y Finanzas; rollback restaura estado sin doble operación
- **Responsable:** Leandro Chamorro

## R-004

- **Riesgo:** Dado que los lotes están en texto libre y los registros históricos están incompletos, puede que el saneamiento exceda lo previsto o cargue datos inconsistentes, teniendo como consecuencia rechazo de migración y pérdida de trazabilidad
- **Categoría:** Solución y tecnología
- **Probabilidad:** 3 / 0,50
- **Impacto:** 2 / 0,40
- **Exposición:** 0,20 (Alta)
- **Mitigación:** Mitigar — Muestrear datos completos por origen y antigüedad, medir defectos y obtener responsables de corrección. Validar: Perfilado reproducible; rechazos aislados; no fabricar lotes faltantes; conciliación por conjunto
- **Responsable:** Leandro Chamorro

## R-005

- **Riesgo:** Dado que los sitios y móviles acumulan operaciones desconectadas, puede que reintentos y orden parcial dupliquen cobros o reserven stock ya retenido, teniendo como consecuencia inconsistencia entre sitio, nube y ERP
- **Categoría:** Solución y tecnología
- **Probabilidad:** 2 / 0,30
- **Impacto:** 4 / 0,80
- **Exposición:** 0,24 (Alta)
- **Mitigación:** Mitigar — Inyectar fallas después de persistir y antes del acuse, con dos sitios y un móvil. Validar: Prueba con UUID repetido, orden invertido y corte de 24 h; invariantes conciliados
- **Responsable:** Tomás Pérez

## R-006

- **Riesgo:** Dado que Concepción tiene un solo enlace en la situación actual, puede que la redundancia propuesta no conmute o comparta una falla física, teniendo como consecuencia aislamiento del CD y acumulación de operaciones
- **Categoría:** Operación del cliente
- **Probabilidad:** 2 / 0,30
- **Impacto:** 4 / 0,80
- **Exposición:** 0,24 (Alta)
- **Mitigación:** Mitigar — Inspeccionar rutas físicas y simular caída de fibra y LTE con el satélite activo. Validar: Acta de diversidad y prueba de 24 h con recepción, preparación y despacho reales
- **Responsable:** Guillermo Castillo

## R-007

- **Riesgo:** Dado que Los Ángeles presenta señal móvil intermitente en su ventana operacional, puede que el borde o su cola no sostenga la carga de una madrugada sin WAN, teniendo como consecuencia transferencias demoradas y stock desactualizado
- **Categoría:** Operación del cliente
- **Probabilidad:** 3 / 0,50
- **Impacto:** 2 / 0,40
- **Exposición:** 0,20 (Alta)
- **Mitigación:** Mitigar — Medir cobertura nocturna y ensayar las transferencias con corte y reposición de enlace. Validar: Acta nocturna por plataforma, cola durable y conciliación dentro de 2 h
- **Responsable:** Guillermo Castillo

## R-008

- **Riesgo:** Dado que existen rutas sin cobertura hasta el regreso y trabajo bajo lluvia y calor, puede que la aplicación o batería no conserve una jornada completa, teniendo como consecuencia pedido, entrega o cobro perdido y repetición de visitas
- **Categoría:** Solución y tecnología
- **Probabilidad:** 2 / 0,30
- **Impacto:** 2 / 0,40
- **Exposición:** 0,12 (Media)
- **Mitigación:** Mitigar — Ensayar 14 h en ruta con periféricos y batería envejecida, más reconexión en 10 min. Validar: Jornada íntegra reproducible y sin duplicados, bajo condiciones de terreno
- **Responsable:** Tomás Pérez

## R-009

- **Riesgo:** Dado que la operación nocturna requiere relevos mientras la identidad central está inaccesible, puede que el manifiesto venza o admita permisos revocados, teniendo como consecuencia bloqueo de una función válida o acceso indebido
- **Categoría:** Solución y tecnología
- **Probabilidad:** 2 / 0,30
- **Impacto:** 2 / 0,40
- **Exposición:** 0,12 (Media)
- **Mitigación:** Mitigar — Probar dos relevos durante un corte, vencimiento y revocación con el verificador local. Validar: Acta de corte con cambios de turno, denegación y bitácora posterior
- **Responsable:** Álvaro Catalán

## R-010

- **Riesgo:** Dado que la cámara de congelado está a −22 °C y sin señal, puede que la batería, pantalla, lector o impresora falle en uso real, teniendo como consecuencia picking lento o registros incompletos
- **Categoría:** Solución y tecnología
- **Probabilidad:** 2 / 0,30
- **Impacto:** 2 / 0,40
- **Exposición:** 0,12 (Media)
- **Mitigación:** Mitigar — Validar una unidad por tipo en cámara, con guantes, condensación y ciclo entrada/salida. Validar: Ficha exacta y prueba funcional completa antes de compra masiva
- **Responsable:** Bastián Trejo

## R-011

- **Riesgo:** Dado que la regla de excursión no estaba formalizada por producto en el levantamiento, puede que la calibración o parametrización libere un lote no conforme o retenga uno válido, teniendo como consecuencia bloqueo operacional o disposición sanitaria errónea
- **Categoría:** Solución y tecnología
- **Probabilidad:** 2 / 0,30
- **Impacto:** 4 / 0,80
- **Exposición:** 0,24 (Alta)
- **Mitigación:** Mitigar — Validar rangos por familia y contrastar sensor patrón con alarma, desconexión y lectura tardía. Validar: Calidad aprueba reglas; sensor patrón y ensayo de bloqueo; ninguna liberación automática
- **Responsable:** Maximiliano Miño

## R-012

- **Riesgo:** Dado que el caso reporta recepciones sin lote y retiro de nueve días, puede que la cadena de custodia nueva quede incompleta en algún sitio o retorno, teniendo como consecuencia identificación tardía de clientes y lote afectado
- **Categoría:** Solución y tecnología
- **Probabilidad:** 3 / 0,50
- **Impacto:** 4 / 0,80
- **Exposición:** 0,40 (Crítica)
- **Mitigación:** Mitigar — Ejecutar retiro simulado extremo a extremo con lote repartido, devolución y sitio desconectado. Validar: Listado reconciliado contra entregas y devoluciones en menos de 2 h; historia incompleta declarada
- **Responsable:** Maximiliano Miño

## R-013

- **Riesgo:** Dado que salen 96 camiones de 05:30 a 07:00 y septiembre casi duplica el volumen, puede que la carga o un componente común degrade el despacho, teniendo como consecuencia día de operación afectado y SLA incumplido
- **Categoría:** Solución y tecnología
- **Probabilidad:** 2 / 0,30
- **Impacto:** 4 / 0,80
- **Exposición:** 0,24 (Alta)
- **Mitigación:** Mitigar — Probar carga con un nodo fuera, backlog y periféricos reales en ventana de despacho. Validar: Prueba a peak de caso y margen declarado; 96 despachos completos con falla inyectada
- **Responsable:** Guillermo Castillo

## R-014

- **Riesgo:** Dado que la sala actual tiene split, UPS de diez minutos y acceso por llave, puede que la habilitación o redundancia eléctrica falle ante un corte prolongado, teniendo como consecuencia caída de los nodos locales críticos
- **Categoría:** Operación del cliente
- **Probabilidad:** 2 / 0,30
- **Impacto:** 4 / 0,80
- **Exposición:** 0,24 (Alta)
- **Mitigación:** Mitigar — Recepcionar energía, autonomía y climatización con carga, corte y alarma. Validar: Ensayo de energía y carga térmica, PDU/circuitos comprobados y acta de recepción
- **Responsable:** Guillermo Castillo

## R-015

- **Riesgo:** Dado que la operación híbrida produce datos en varios sitios y medios, puede que la restauración o promoción pierda datos o supere los límites, teniendo como consecuencia interrupción prolongada y conciliación extraordinaria
- **Categoría:** Solución y tecnología
- **Probabilidad:** 3 / 0,50
- **Impacto:** 4 / 0,80
- **Exposición:** 0,40 (Crítica)
- **Mitigación:** Mitigar — Ensayar desastre total con escritura en curso, exclusión del escritor y retorno. Validar: Informe medido de conmutación y retorno; incluir pérdida simultánea de WAN y nodo
- **Responsable:** Guillermo Castillo


## R-016

- **Riesgo:** Dado que hay portales externos, flota móvil y datos comerciales sensibles, puede que una vulnerabilidad o cuenta privilegiada comprometa servicio o evidencia, teniendo como consecuencia indisponibilidad, fuga y recuperación forense
- **Categoría:** Solución y tecnología
- **Probabilidad:** 2 / 0,30
- **Impacto:** 4 / 0,80
- **Exposición:** 0,24 (Alta)
- **Mitigación:** Mitigar — Revisar superficie y privilegios; probar restauración aislada y respuesta a credencial comprometida. Validar: Pentest sin hallazgos bloqueantes y ejercicio de contención/recuperación
- **Responsable:** Álvaro Catalán

## R-017

- **Riesgo:** Dado que el sindicato objetó cámaras en cabina y control de jornada por GPS, puede que el uso de ubicación sea rechazado aunque no se instalen cámaras, teniendo como consecuencia adopción suspendida y rediseño de finalidades
- **Categoría:** Personas y adopción
- **Probabilidad:** 3 / 0,50
- **Impacto:** 2 / 0,40
- **Exposición:** 0,20 (Alta)
- **Mitigación:** Mitigar — Acordar finalidades, retención y acceso con sindicato y dirección; demostrar uso sin control de jornada. Validar: Acta de participación, revisión de privacidad y prueba de permisos/retención
- **Responsable:** Patricio Henríquez

## R-018

- **Riesgo:** Dado que 54 camiones pertenecen a diez empresas y sus conductores cambian sin aviso, puede que el acuerdo o enrolamiento no cubra reemplazos, teniendo como consecuencia entregas sin evidencia y trabajo paralelo en papel
- **Categoría:** Personas y adopción
- **Probabilidad:** 3 / 0,50
- **Impacto:** 2 / 0,40
- **Exposición:** 0,20 (Alta)
- **Mitigación:** Mitigar — Probar alta, baja y conductor suplente por cada empresa; pactar obligación de informar reemplazos. Validar: Diez acuerdos y prueba de enrolamiento/soporte que no detenga reparto
- **Responsable:** Patricio Henríquez

## R-019

- **Riesgo:** Dado que la rotación anual es del 38 % y el turno nocturno es crítico, puede que el personal nuevo no alcance autonomía de preparación, teniendo como consecuencia baja productividad y errores de picking
- **Categoría:** Personas y adopción
- **Probabilidad:** 3 / 0,50
- **Impacto:** 1 / 0,20
- **Exposición:** 0,10 (Media)
- **Mitigación:** Mitigar — Validar incorporación de personal nuevo con tareas reales y guías breves de turno. Validar: Medir tiempo, pasos y errores según 3.A.4a con novatos en turno nocturno
- **Responsable:** Patricio Henríquez

## R-020

- **Riesgo:** Dado que preventistas y conductores están en ruta de lunes a sábado, puede que la convocatoria no libere tiempo sin afectar operación, teniendo como consecuencia usuarios no certificados al paso a producción
- **Categoría:** Personas y adopción
- **Probabilidad:** 3 / 0,50
- **Impacto:** 1 / 0,20
- **Exposición:** 0,10 (Media)
- **Mitigación:** Mitigar — Acordar microturnos de entrenamiento y recuperar ausencias por ruta y perfil. Validar: Agenda aprobada, asistencia y prueba práctica individual por perfil
- **Responsable:** Patricio Henríquez

## R-021

- **Riesgo:** Dado que las reglas residen en Hugo Maldonado, que se jubila en dos años, puede que se retire antes de transferir y validar todas las excepciones, teniendo como consecuencia rutas inseguras o promesas incumplidas
- **Categoría:** Personas y adopción
- **Probabilidad:** 3 / 0,50
- **Impacto:** 2 / 0,40
- **Exposición:** 0,20 (Alta)
- **Mitigación:** Mitigar — Capturar y validar reglas por zona con Hugo y un suplente, usando rutas y restricciones reales. Validar: Repositorio aprobado y suplente planifica rutas sin ayuda, sin violar peso/puentes/ventanas
- **Responsable:** Patricio Henríquez

## R-022

- **Riesgo:** Dado que TI del cliente tiene cuatro personas y la operación no puede detenerse, puede que las validaciones o decisiones no lleguen a la fecha requerida, teniendo como consecuencia cadenas de aprobación retrasadas
- **Categoría:** Operación del cliente
- **Probabilidad:** 3 / 0,50
- **Impacto:** 2 / 0,40
- **Exposición:** 0,20 (Alta)
- **Mitigación:** Mitigar — Pactar titulares y suplentes, agenda y SLA de decisiones por hito. Validar: Agenda y acuerdos escritos; ninguna aprobación tácita de aceptación contractual
- **Responsable:** Alex Aravena

## R-023

- **Riesgo:** Dado que septiembre, diciembre y cierres mensuales restringen cambios, puede que una demora desplace un corte o parche a una ventana prohibida, teniendo como consecuencia reprogramación y multa por atraso
- **Categoría:** Operación del cliente
- **Probabilidad:** 2 / 0,30
- **Impacto:** 2 / 0,40
- **Exposición:** 0,12 (Media)
- **Mitigación:** Mitigar — Revalidar calendario por fecha efectiva y reservar alternativa permitida para cada corte. Validar: Calendario validado por contraparte y plan alternativo; emergencia requiere definición contractual
- **Responsable:** Alex Aravena

## R-024

- **Riesgo:** Dado que el cliente compra dispositivos de terreno y LafroX habilita la infraestructura, puede que una compra, entrega o recepción exceda la ventana de la ola, teniendo como consecuencia piloto sin equipos completos o marcha blanca insuficiente
- **Categoría:** Operación del cliente
- **Probabilidad:** 3 / 0,50
- **Impacto:** 2 / 0,40
- **Exposición:** 0,20 (Alta)
- **Mitigación:** Mitigar — Confirmar orden, stock y plazo por ola; homologar alternativa antes de la compra. Validar: Orden y acta de muestra; préstamo o alternativa homologada no reduce población de prueba
- **Responsable:** Bastián Trejo

## R-025

- **Riesgo:** Dado que construcción E2 coincide con marcha blanca E1 y hay líderes con varios roles, puede que la dotación real no sostenga los frentes simultáneos, teniendo como consecuencia atraso de E2 o deterioro de E1
- **Categoría:** Empresa proveedora
- **Probabilidad:** 3 / 0,50
- **Impacto:** 2 / 0,40
- **Exposición:** 0,20 (Alta)
- **Mitigación:** Mitigar — Nominar equipos separados y suplentes; verificar capacidad semanal y contrato de refuerzo. Validar: Cartas y calendario nominal; no sumar las HH de mitigación a capacidad inexistente
- **Responsable:** Alex Aravena

## R-026

- **Riesgo:** Dado que hay seis condiciones copulativas de cierre y revisión contractual, puede que observaciones, capacitación o indicadores sigan abiertos al cierre, teniendo como consecuencia extensión a cargo de LafroX sin mover fases
- **Categoría:** Contrato y licitación
- **Probabilidad:** 3 / 0,50
- **Impacto:** 2 / 0,40
- **Exposición:** 0,20 (Alta)
- **Mitigación:** Mitigar — Revisar evidencia con contraparte antes del hito y ejecutar ensayo de go/no-go. Validar: Checklist de seis condiciones con evidencia; ninguna firma ni prueba se presume
- **Responsable:** Maximiliano Miño

## R-027

- **Riesgo:** Dado que el caso contiene decisiones de diseño y sistemas excluidos con dependencias, puede que una solicitud introduzca trabajo no previsto o duplique sistemas de registro, teniendo como consecuencia sobrecosto y retraso
- **Categoría:** Contrato y licitación
- **Probabilidad:** 3 / 0,50
- **Impacto:** 1 / 0,20
- **Exposición:** 0,10 (Media)
- **Mitigación:** Mitigar — Trazar solicitudes a requisitos, impacto y aprobación antes de construcción. Validar: Registro de cambios, estimación y aprobación; exclusiones no eliminan integración obligatoria
- **Responsable:** Alex Aravena

## R-028

- **Riesgo:** Dado que 38 % del canal tradicional paga en efectivo y hay diferencias mensuales, puede que el circuito de custodia no explique toda diferencia al retorno, teniendo como consecuencia reproceso financiero y exposición del conductor
- **Categoría:** Operación del cliente
- **Probabilidad:** 2 / 0,30
- **Impacto:** 2 / 0,40
- **Exposición:** 0,12 (Media)
- **Mitigación:** Mitigar — Simular caja de turno, faltante, devolución y pago parcial; acordar custodia física con Finanzas. Validar: Cuadre por camión y turno el mismo día; importe externo no se incorpora como costo del proyecto
- **Responsable:** Leandro Chamorro

## R-029

- **Riesgo:** Dado que el ERP es único emisor y el receptor suele carecer de firma avanzada, puede que la prueba de entrega no se vincule o verifique conforme al acto, teniendo como consecuencia rechazo de evidencia y disputa de entrega
- **Categoría:** Regulatorio y externo
- **Probabilidad:** 3 / 0,50
- **Impacto:** 2 / 0,40
- **Exposición:** 0,20 (Alta)
- **Mitigación:** Mitigar — Validar flujo por acto con experto tributario y probar certificado vencido, POD offline y acuse. Validar: Dictamen sobre el flujo y AL-DTE-01 aprobado; no equiparar firma simple y avanzada
- **Responsable:** Bastián Trejo

## R-030

- **Riesgo:** Dado que la cadena exige pedido electrónico, ASN, ventana y POD antes de enero de 2029, puede que su formato, ambiente o certificación no estén disponibles a tiempo, teniendo como consecuencia integración no habilitada y pérdida de capacidad comercial
- **Categoría:** Integración y legado
- **Probabilidad:** 3 / 0,50
- **Impacto:** 2 / 0,40
- **Exposición:** 0,20 (Alta)
- **Mitigación:** Mitigar — Obtener especificación, sandbox, fechas y responsable de certificación; ensayar el flujo completo. Validar: Confirmación escrita de cadena y certificación completa antes del H12; dependencia externa mantiene zona alta
- **Responsable:** Bastián Trejo


## R-031

- **Riesgo:** Dado que el canal tradicional no usa siempre correo y proveedores no acreditan toda apertura, puede que el aviso de llegada no se reciba antes de la salida, teniendo como consecuencia cliente ausente y entrega fallida
- **Categoría:** Integración y legado
- **Probabilidad:** 3 / 0,50
- **Impacto:** 1 / 0,20
- **Exposición:** 0,10 (Media)
- **Mitigación:** Mitigar — Validar contactos y probar fallback por canal con confirmación de entrega; medir apertura por separado. Validar: Prueba de recepción antes de salida; SMS sin lectura informable no cuenta como abierto
- **Responsable:** Tomás Pérez

## R-032

- **Riesgo:** Dado que la solución usa servicios administrados y APIs con contratos propios, puede que la reversibilidad no preserve funcionalidad y evidencia en una salida, teniendo como consecuencia migración costosa y dependencia prolongada
- **Categoría:** Solución y tecnología
- **Probabilidad:** 2 / 0,30
- **Impacto:** 2 / 0,40
- **Exposición:** 0,12 (Media)
- **Mitigación:** Mitigar — Ensayar exportación e importación de un flujo representativo y medir sustitución del servicio no portable. Validar: Ensayo reproducible, licencias y formatos declarados; costo de salida separado de EOL
- **Responsable:** Bastián Trejo

## R-033

- **Riesgo:** Dado que el contrato dura 56 meses y versiones/equipos tienen ciclos de soporte, puede que un componente quede sin parche o repuesto antes del cierre, teniendo como consecuencia actualización no prevista o vulnerabilidad persistente
- **Categoría:** Solución y tecnología
- **Probabilidad:** 3 / 0,50
- **Impacto:** 1 / 0,20
- **Exposición:** 0,10 (Media)
- **Mitigación:** Mitigar — Consolidar fechas EOL/EOS comprobadas y ensayar actualización o sustitución antes del fin de soporte. Validar: Ficha/versiones y calendario anual; presupuesto de reposición pendiente de tarifas
- **Responsable:** Bastián Trejo

## R-034

- **Riesgo:** Dado que se requieren madrugada, peaks, seis sitios y traslados de hasta 340 km, puede que ausencia, demanda o traslado impidan atención dentro del SLA, teniendo como consecuencia interrupción más larga y abandono
- **Categoría:** Empresa proveedora
- **Probabilidad:** 2 / 0,30
- **Impacto:** 2 / 0,40
- **Exposición:** 0,12 (Media)
- **Mitigación:** Mitigar — Simular ausencia y peak de llamadas con traslado; pactar cobertura de suplentes por tecnología. Validar: Prueba de cola con 80 % antes de 20 s, abandono ≤5 % y guardia acreditada
- **Responsable:** Guillermo Castillo

## R-035

- **Riesgo:** Dado que nube, mensajes, licencias y reposiciones tienen consumo y pago durante 56 meses, puede que el consumo o los pagos superen la previsión financiera, teniendo como consecuencia recorte de servicio o necesidad de financiamiento
- **Categoría:** Empresa proveedora
- **Probabilidad:** 3 / 0,50
- **Impacto:** 2 / 0,40
- **Exposición:** 0,20 (Alta)
- **Mitigación:** Mitigar — Construir presupuesto por unidad, peak, divisa y calendario de cobro; probar alertas de consumo. Validar: Oferta económica y flujo de caja revisados; sin tarifas, severidad monetaria sigue pendiente
- **Responsable:** Alex Aravena

## R-036

- **Riesgo:** Dado que el inventario de góndola no pertenece al sistema de registro de Puelche, puede que datos inferidos generen avisos de vencimiento sin confirmación, teniendo como consecuencia visitas improductivas y beneficio no demostrable
- **Categoría:** Personas y adopción
- **Probabilidad:** 3 / 0,50
- **Impacto:** 1 / 0,20
- **Exposición:** 0,10 (Media)
- **Mitigación:** Mitigar — Pilotear por locales voluntarios y separar saldo inferido de observado; validar avisos antes de acción. Validar: Muestra de avisos confirmados, intervención autorizada e indicador INN-01 medido
- **Responsable:** Patricio Henríquez

## R-037

- **Riesgo:** Dado que los fallos aparecen en condiciones de terreno difíciles de replicar, puede que captura y reproducción no conserven el orden causal del incidente, teniendo como consecuencia corrección ineficaz y reapertura de tickets
- **Categoría:** Solución y tecnología
- **Probabilidad:** 3 / 0,50
- **Impacto:** 1 / 0,20
- **Exposición:** 0,10 (Media)
- **Mitigación:** Mitigar — Seleccionar incidentes de prueba y verificar reproducción con datos minimizados y versión exacta. Validar: Escenario reproduce fallo, corrección lo elimina y datos sensibles están protegidos
- **Responsable:** Tomás Pérez

## R-038

- **Riesgo:** Dado que el modelo cinético depende de familia de producto e historia térmica completa, puede que la estimación sea inválida o exceda el uso permitido, teniendo como consecuencia decisión de disposición errónea
- **Categoría:** Solución y tecnología
- **Probabilidad:** 3 / 0,50
- **Impacto:** 2 / 0,40
- **Exposición:** 0,20 (Alta)
- **Mitigación:** Mitigar — Validar por familia contra evidencia del proveedor; mantener modo informativo hasta aceptación. Validar: Validación de Calidad/proveedor; innovación nunca libera ni amplía vencimiento automáticamente
- **Responsable:** Maximiliano Miño

## R-039

- **Riesgo:** Dado que la mejora puede deberse a combustible, malla o mezcla de clientes y no al servicio, puede que la línea base o canasta atribuya un ahorro espurio, teniendo como consecuencia disputa del tramo variable o sacrificio del OTIF
- **Categoría:** Contrato y licitación
- **Probabilidad:** 3 / 0,50
- **Impacto:** 1 / 0,20
- **Exposición:** 0,10 (Media)
- **Mitigación:** Mitigar — Acordar canasta y fórmula; recalcular casos de estacionalidad y OTIF bajo sin pago variable. Validar: Contrato y cálculo auditables por Finanzas; tarifas y techo monetario pendientes
- **Responsable:** Alex Aravena

## R-040

- **Riesgo:** Dado que hay baja alfabetización y agregados de negocios comparables, puede que la hoja no se entienda o permita identificar otro local, teniendo como consecuencia rechazo del servicio y divulgación comercial
- **Categoría:** Personas y adopción
- **Probabilidad:** 3 / 0,50
- **Impacto:** 1 / 0,20
- **Exposición:** 0,10 (Media)
- **Mitigación:** Mitigar — Probar comprensión con locales y revisión de divulgación; desactivar comparativos hasta autorización. Validar: Prueba de comprensión; revisión de privacidad y separación de copias pedidas/entregadas
- **Responsable:** Patricio Henríquez

## R-041

- **Riesgo:** Dado que el cliente tiene cuatro personas de TI y debe sostener o transferir el servicio, puede que documentación, cuentas o exportación no permitan una entrega efectiva, teniendo como consecuencia dependencia al cierre y operación no sostenible
- **Categoría:** Contrato y licitación
- **Probabilidad:** 2 / 0,30
- **Impacto:** 2 / 0,40
- **Exposición:** 0,12 (Media)
- **Mitigación:** Mitigar — Ensayar una entrega parcial a operadores del cliente y corregir runbooks antes del cierre. Validar: Operador receptor ejecuta procedimiento con cuentas propias y exportación reconciliada
- **Responsable:** Guillermo Castillo

## R-042

- **Riesgo:** Dado que el contrato conserva documentos, ubicación y evidencia durante varios años, puede que un cambio o interpretación exija adaptar controles y purga, teniendo como consecuencia retrabajo, conservación indebida o incumplimiento
- **Categoría:** Regulatorio y externo
- **Probabilidad:** 3 / 0,50
- **Impacto:** 2 / 0,40
- **Exposición:** 0,20 (Alta)
- **Mitigación:** Mitigar — Revisar normativa aplicable con asesor competente y ensayar purga con expediente retenido. Validar: Matriz legal actualizada y ensayo de supresión sin reconstrucción; no se certifica legalidad con esta planilla
- **Responsable:** Álvaro Catalán

## R-043

- **Riesgo:** Dado que el POS depende de un tercero y el timeout no equivale a rechazo, puede que el reintento o pago alternativo duplique la obligación, teniendo como consecuencia conciliación, devolución y reclamo del cliente
- **Categoría:** Integración y legado
- **Probabilidad:** 2 / 0,30
- **Impacto:** 2 / 0,40
- **Exposición:** 0,12 (Media)
- **Mitigación:** Mitigar — Inyectar timeout después del cargo y probar consulta, cancelación y autorización de alternativa. Validar: Contrato POS y prueba de un solo cargo económico con correlación y devolución
- **Responsable:** Leandro Chamorro

## R-044

- **Riesgo:** Dado que retornos en terreno y recepción local atraviesan varios registros, puede que una devolución se contabilice dos veces o quede sin vínculo al lote, teniendo como consecuencia saldo, cuenta de envases y trazabilidad incorrectos
- **Categoría:** Operación del cliente
- **Probabilidad:** 2 / 0,30
- **Impacto:** 1 / 0,20
- **Exposición:** 0,06 (Baja)
- **Mitigación:** Mitigar — Probar retorno parcial, sitio offline y reintento con lote retenido y envase recuperado. Validar: Conciliación por cliente/tipo y lote; MERMA/DESTRUCCION no duplica costo
- **Responsable:** Leandro Chamorro

## R-045

- **Riesgo:** Dado que direcciones, pesos y puentes no están plenamente formalizados, puede que geocodificación o propuesta asigne camión/ruta incompatible, teniendo como consecuencia entrega fallida y reproceso de planificación
- **Categoría:** Integración y legado
- **Probabilidad:** 3 / 0,50
- **Impacto:** 2 / 0,40
- **Exposición:** 0,20 (Alta)
- **Mitigación:** Mitigar — Validar rutas por zona y atributos físicos; comparar proveedor GIS y ruta conocida con conductor. Validar: Catálogo de restricciones aprobado y planificación con corrección auditada, incluso sin señal
- **Responsable:** Bastián Trejo

## Referencias

Las fuentes citadas en este documento se listan en formato APA 7.ª edición. Las Bases se citan en el texto con su documento y el artículo, capítulo, sección o código del requisito.

- Distribuidora Puelche S.A. (2026a). *Bases Administrativas de Licitación N.º TFEP-01/2026: Contratación de Solución Integral de Software y Servicios de Operación*.
- Distribuidora Puelche S.A. (2026b). *Bases Técnicas Transversales de Licitación N.º TFEP-01/2026*.
- Distribuidora Puelche S.A. (2026c). *Caso 02: Logística. Especificaciones del problema y operación de Distribuidora Puelche S.A.*
- Distribuidora Puelche S.A. (2026d). *Aclaraciones de la Licitación N.º TFEP-01/2026*.
- LafroX. (2026). Subdocumentos 1 a 7 y 13, con los anexos y formularios citados.
- International Organization for Standardization. (2018). *ISO 31000:2018 Risk management — Guidelines*. ISO.
- Project Management Institute. (2017). *La guía de los fundamentos para la dirección de proyectos (Guía del PMBOK®)* (6.ª ed.), capítulo 11. Project Management Institute.

## Declaración de uso de IA

La tabla declara apoyo de IA conforme a las Aclaraciones §7.2. La revisión humana identifica quién efectivamente verificó cada parte y se consolida en el Formulario A-6.

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
|---|---|---|---|---|---|
| Formulario T-16 | Codex; Claude Code | Registro de 45 riesgos de referencia, responsables temporales y mitigación | Alto | Ninguno | [[REVISIÓN HUMANA]] |
