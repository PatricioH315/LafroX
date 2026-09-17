# Capítulo 3 · Esquema de Solución y Alcance (Subdoc. 3)


## 3.1 Solución propuesta

La presente oferta se encarga de proponer el diseño, construcción, implantación y operación de una plataforma digital de logística para Distribuidora Puelche S.A.; no se trata de un módulo concreto ni de la modernización de un sistema aislado: es una plataforma organizada en ocho capas lógicas, con despliegue híbrido en nube + on-premise, diseñada desde el origen del problema.

El problema de Puelche no es una deficiencia puntual, sino tres problemas que se refuerzan entre ellos, por lo que la solución debe ser integral: la trazabilidad de lotes y cadena de frío, la competitividad del servicio y el desconocimiento del costo de servir. La solución ataca los tres en una sola plataforma, de tal forma que las capacidades de cada uno de estos ejes pueda retroalimentar a los demás.

Trazabilidad sanitaria y cadena de frío, como habilitación comercial: Atacamos el origen del sumario sanitario de marzo de 2026: el registro pasará de ser discreto a ser obligatorio y estructurado en el punto de recepción, la operación se modela como trazabilidad lote a lote, de modo que el listado de clientes afectados por un lote obtiene evidencia de forma rápida y con retención de cinco años. La temperatura se registra de forma continua cuando sea posible, alertando de manera temprana ante un eventual problema.

Competitividad: preventa informada y entrega digital: El preventista deja de vender a ciegas y ahora poseerá disponibilidad del stock disponible, crédito, deuda vencida e historial en el momento correcto, bloqueando por crédito en el momento y con excepciones autorizadas de forma registrada. La toma de pedidos opera de forma offline-first un turno completo sin señal, sin pedidos perdidos o duplicados. La entrega se digitaliza con prueba de entrega válida según el perfil del receptor, siendo articulada con la guía de despacho electrónica y su acuse de recibo; el cobro se registra en el momento de forma automática. El canal moderno se atiende con pedidos electrónicos y aviso de despacho anticipado, en producción antes de enero de 2029. Esto hace verificable la promesa de entrega de 24 horas con ventana de 320 minutos, protegiendo el 11 % de la venta.

Costo de servir conocido y control de gestión: El ruteo deja de depender de una planilla personal de 11 hojas: un motor que propone la ruta y permite corregirla, respetando capacidades, cadenas de frío y ventanas horarias. El costo de servir se construye desde el hecho y se calcula por cliente y por entrega; la rendición de efectivo se bloquea ante descuadres sin causal tipificada, y OTIF, Fill Rate y ocupación de flota se miden a diario sobre los datos de la propia operación.

Estos tres ejes se implementan sobre una única plataforma que protege la ventana crítica de despacho 05:30–07:00 con indisponibilidad cero, opera un turno completo sin señal en terreno, mantiene el centro de distribución autónomo 24 h ante un corte de enlace, y se sostiene sobre hardware apto para −22 °C y uso con guantes, sin exigirle al cliente del canal tradicional internet, dispositivo ni medio de pago.

La propuesta se ejecuta dentro del cronograma de 56 meses innegociable (BA Art. 17°) y reconoce los hitos externos que condicionan el diseño y el plan de trabajo:


> **Tabla 7** — 3.1 Solución propuesta · 10 filas · ver planilla del subdocumento


## 3.2 Alcance Etapa 1

El alcance de la Etapa 1 cubre los meses 1 a 15 del cronograma obligatorio (desarrollo, marcha blanca y cierre, con producción en el mes 16 — BA Art. 17°), y se presenta en dos planos: el alcance funcional y el de infraestructura. La separación entre Etapa 1 y Etapa 2 se sustenta en los criterios de asignación de la Decisión 20: (a) la urgencia que el caso declara (trazabilidad sanitaria y captura del conocimiento del planificador antes de su jubilación), (b) las dependencias técnicas entre épicas, (c) el riesgo operacional y (d) los hitos externos del numeral 13.2 (canal moderno en producción antes de enero de 2029 y peak de septiembre), además de la capacidad de absorción del cliente (equipo TIC de 4 personas y marcha blanca por oleadas).


### 3.2.1 Alcance funcional del proyecto


### Lo que hará

Recepción: validación contra OC, registro obligatorio del lote (AI 10) y del vencimiento, no conformidades con cuarentena automática, lectura GS1 y etiquetado SSCC, fichas de producto, compatibilidad térmica en putaway e integración de la recepción con el ERP.

Gestión de almacén e inventario: topología multi-sitio configurable, consolidación de stock multi-nodo, slotting por rotación, conteo cíclico ciego, cálculo de stock disponible para la venta, inventario en tránsito, gestión FEFO con alertas de vida útil y ficha de trazabilidad de lote. Reemplaza el WMS de 2013.

Trazabilidad y cadena de frío: trazabilidad forward y backward por lote bajo el estándar GS1 EPCIS, registro continuo de temperaturas de cámaras y camiones con equipo de frío, excursiones térmicas con alerta y disposición configurable, registro de lotes con control sanitario y generación del cumplimiento de cadena de frío.

Preventa móvil: aplicación nativa offline-first para los 62 preventistas (turno completo de 14 h sin señal), consulta de stock, crédito y deuda vencida en línea y sin conectividad, reserva de stock al confirmar, promociones, ventana de entrega comprometida, pedido con identificador único y descarte de duplicados al sincronizar.

Preparación y picking: misiones de picking, validación por escaneo GS1 con confirmación ≤ 1 s operable con guantes a −22 °C, motivo obligatorio de faltante, asignación FEFO, secuenciación térmica, envío de la preparación al ERP y carga dirigida inversa a la ruta.

Entrega y prueba de entrega: confirmación de bultos, firma digital o evidencia alternativa (QR, o fotografía con nombre del receptor sin conectividad), rechazo de productos, local cerrado con reagendamiento automático, registro de recaudación en ruta, autenticación del conductor externo por OTP, captura y saldo de envases retornables y sincronización del 100 % al reconectar.

Rendición y recaudación: rendición digital individual por camión, causales tipificadas de descuadre con bloqueo del cierre, alerta y bloqueo de crédito en preventa, cobro con POS móvil y abonos parciales en la entrega.

Devoluciones y envases: devoluciones en la entrega, destino de los productos devueltos en el andén, cuenta corriente de envases retornables por cliente, alertas por exceso de envases y registro de mermas por vencimiento en góndola.

Ruteo (Etapa 1): asignación y secuenciación automática que codifica el conocimiento del planificador, ajuste manual y recálculo de ETA y parametrización de ventanas horarias por cliente, para resguardar la continuidad operacional ante la jubilación del planificador.


### 3.2.2 Alcance de infraestructura del proyecto

Plataforma híbrida: nube pública multi-zona (región primaria y secundaria declaradas) más componentes on-premise en los seis sitios, definida como código (IaC), versionada y reproducible en su totalidad.

Seguridad: identidad centralizada con SSO, MFA para administradores y acceso externo, RBAC y segregación de funciones, cero confianza (Zero Trust), matriz de controles trazable a ISO/IEC 27001, plan de respuesta a incidentes y notificación de brechas.

Observabilidad: nube + on-premise con NOC 24×7×365, alertamiento por síntomas de negocio y análisis de causa raíz.

Ambientes y continuidad: habilitación de los cinco ambientes exigidos (DEV, QA, PREPROD, PROD y el ambiente de Recuperación ante Desastres); recuperación ante desastres con RTO ≤ 4 h y RPO ≤ 15 min y respaldo 3-2-1-1-0.

Gestión administrativa: administración de usuarios, parametrización de reglas con aprobación de dos perfiles, registro de auditoría inalterable, flujos de trabajo y bandeja de tareas, gestión documental y notificaciones multicanal.

Integración con el ERP y DTE: ERP y emisión de documentos tributarios (no se reemplazan), maestro de productos y servicios de DTE, mediante capa anticorrupción.

Arquitectura de ocho capas


> **Tabla 8** — 3.2.2 Alcance de infraestructura del proyecto · 9 filas · ver planilla del subdocumento

Modelo de emplazamiento híbrido


> **Tabla 9** — 3.2.2 Alcance de infraestructura del proyecto · 6 filas · ver planilla del subdocumento


## 3.3 Alcance Etapa 2


### 3.3.1 Alcance funcional del proyecto


### Lo que haremos

Canal moderno y portales: recepción y validación del pedido electrónico, resolución de códigos contra el maestro mediante equivalencias por cadena, bandeja de excepciones, confirmación o rechazo a la cadena, aviso de despacho anticipado, planificación de la llegada dentro de la ventana de 30 minutos, evidencia y acuse de recibo digital del canal moderno, portal de clientes con registro, autenticación y consulta de entregas, documentos tributarios y estado de cuenta, portal de transportistas y portal de proveedores. La integración es configurable para nuevas cadenas y queda en producción antes de enero de 2029.

Analítica y control de gestión: OTIF unificado calculado a diario, Fill Rate y Perfect Order medidos con el POD móvil, costo de servir por entrega y por cliente construido desde los hechos operacionales, ocupación de flota, tablero operacional en tiempo real, liquidación y cierre comercial por camión y segmentación de clientes por rentabilidad neta.

Ruteo (Etapa 2): bloqueo por exceso de capacidad, restricción por requisito de cadena de frío, notificación de hora estimada de llegada al cliente y cálculo integral del costo de la entrega realizada.

Telemetría (Etapa 2): telemetría de camiones propios, ruta planificada vs. real, alerta de desviación, geocercas de llegada/salida y vinculación conductor–camión por viaje, respetando el acuerdo sindical y la privacidad del conductor.

Cobranza y cartera: consola de gestión de la cartera de crédito, estado de cuenta en el portal de clientes, validación en tesorería de los pagos web, interfaz asíncrona de cobranzas hacia el ERP y cobranza presencial de facturas.

Envases y devoluciones (Etapa 2): reporte de pérdida de envases retornables por cliente, tipo y zona, e integración de devoluciones y mermas al costo de servir.


### Lo que no haremos

Lo siguiente queda fuera del alcance del proyecto, tanto en la Etapa 1 como en la Etapa 2 (el detalle y el sustento normativo de cada exclusión se consolida en S 3.6):

El reemplazo del sistema de gestión empresarial (ERP) ni de ninguno de sus módulos, ni la emisión de los documentos tributarios electrónicos (los emite el ERP, con el que la solución se integra mediante capa anticorrupción).

La administración de remuneraciones ni de recursos humanos, que residen en el sistema de gestión.

Un sistema de punto de venta para el local del cliente, sin perjuicio del canal de autoatención que la solución ofrece.

El comercio electrónico dirigido al consumidor final.

La conectividad ni los sistemas de información de los puntos de entrega (clientes); la solución opera offline cuando la red no está disponible.

El desarrollo o la fabricación de hardware propio: los dispositivos se adquieren estándar (tip rugged).

La obra civil y la infraestructura de climatización o de energía de los recintos del CLIENTE, salvo la adecuación física de la sala técnica declarada en el padrón de emplazamiento (Decisión 29).


## 3.4 Requerimientos


### 3.4.1 Catálogo de requerimientos funcionales (RF)

El catálogo funcional cubre el ciclo logístico completo: abastecimiento y recepción, gestión de almacén e inventario, preventa, planificación de rutas, preparación y carga, transporte y prueba de entrega, cobranza y efectivo, logística inversa, trazabilidad sanitaria y cadena de frío, indicadores y costo de servir, canal moderno y portales, identidad, observabilidad y firma electrónica. Cada fila indica su etapa de alcance (Etapa 1 y/o Etapa 2, según lo declarado en 3.2 y 3.3), su prioridad y su origen en las Bases o el caso.


> **Tabla 10** — 3.4.1 Catálogo de requerimientos funcionales (RF) · 91 filas · ver planilla del subdocumento


### 3.4.2 Catálogo de requerimientos no funcionales (RNF)

Los requerimientos no funcionales condicionan el diseño de la plataforma: desempeño en terreno, operación sin conectividad, continuidad, comunicaciones, capacidad, seguridad, soporte y formación. Cada fila indica el objetivo verificable que se compromete y su origen.


> **Tabla 11** — 3.4.2 Catálogo de requerimientos no funcionales (RNF) · 41 filas · ver planilla del subdocumento


### 3.4.3 Matriz de trazabilidad requisito → diseño → verificación

La matriz consolida el origen de cada capacidad, el diseño que la implementa (componente o capa de la arquitectura de 3.1 y del modelo de emplazamiento de 3.2.2) y la verificación con la que se demuestra su cumplimiento. Los criterios R18-xx se detallan en 3.11.2; los hitos contractuales, en 3.11.1.


> **Tabla 12** — 3.4.3 Matriz de trazabilidad requisito → diseño → verificación · 19 filas · ver planilla del subdocumento

Las reglas de negocio (S 3.9) se implementan por los RF/RNF citados en cada fila de regla; las decisiones (S 3.8) que las sustentan y los resultados del Capítulo 18 (S 3.11.2) constituyen la verificación de cierre del alcance.


### 3.4.4 Registro de vacíos y consultas al CLIENTE

Los vacíos y ambigüedades detectados en las Bases o el caso se registran aquí con su tratamiento. Las consultas al mandante se formulan conforme al Artículo 43.3 de las Bases Administrativas; los supuestos adoptados se declaran en 3.5 y las decisiones fundadas en 3.8.


> **Tabla 13** — 3.4.4 Registro de vacíos y consultas al CLIENTE · 13 filas · ver planilla del subdocumento


## 3.5 Supuestos


### Supuestos, Exclusiones, Restricciones, Decisiones


> **Tabla 14** — Supuestos, Exclusiones, Restricciones, Decisiones · 47 filas · ver planilla del subdocumento


## 3.6 Exclusiones


> **Tabla 15** — 3.6 Exclusiones · 15 filas · ver planilla del subdocumento


## 3.7 Restricciones


> **Tabla 16** — 3.7 Restricciones · 44 filas · ver planilla del subdocumento


## 3.8 Decisiones


> **Tabla 17** — 3.8 Decisiones · 61 filas · ver planilla del subdocumento


## 3.9 Registro de reglas de negocio


> **Tabla 18** — 3.9 Registro de reglas de negocio · 15 filas · ver planilla del subdocumento


## 3.10 Estrategia para obtener el apoyo de los grupos claves

Los grupos se priorizan con el mapa de influencia e interés del proyecto (cuadrante A: alta influencia y alto interés — involucrar activamente; cuadrante B: alta influencia y bajo interés — mantener satisfecho; cuadrante C: baja influencia y alto interés — mantener informado; cuadrante D: baja influencia y bajo interés — monitorear). La estrategia se conduce por la gerencia de proyecto y el líder de implantación y gestión del cambio, con hitos de involucramiento alineados al cronograma contractual de 56 meses (Etapa 1, producción mes 16; Etapa 2, producción mes 21; Operación):


> **Tabla 19** — 3.10 Estrategia para obtener el apoyo de los grupos claves · 11 filas · ver planilla del subdocumento

La gestión del cambio se activa con la participación de los portavoces de los cuadrantes A y B desde el mes 1 (comunicación, mesas de trabajo y pruebas), de manera que el apoyo sea un insumo de la marcha blanca y no una etapa posterior al diseño. Cada indicador de adopción se incorpora al tablero de implementación y al plan de operación.


## 3.11 Criterios de aceptación del alcance comprometido

El alcance comprometido se considerará cumplido cuando concurran tres condiciones copulativas:

Cada hito contractual del formulario E-25 se acepte conforme al protocolo del formulario T-17.

Cada marcha blanca se cierra bajo las condiciones del artículo 17.3 de las Bases Administrativas.

Los dieciséis resultados de negocio del capítulo 18 del caso se verifiquen con las metas comprometidas. Cada entregable sometido a aceptación incorpora el artefacto en sí, la evidencia objetiva de su verificación, la trazabilidad hacia los requerimientos que satisface y el registro de las observaciones previas resueltas (BA Art. 18.2).


### 3.11.1 Aceptación contractual por hito

Los hitos contractuales H1 a H12 (BA Art. 18.1, Formulario E-25) se entienden cumplidos únicamente con la suscripción del acta de aceptación de la Contraparte Técnica. El protocolo de aceptación de cada hito se formaliza conforme al Formulario T-17 con criterios objetivos y verificables (RT-20.08), sobre la base de:

El artefacto o la funcionalidad comprometida del hito.

La aprobación de las pruebas que le corresponden (unitarias y de componente, integración, sistema y regresión, aceptación de usuario, carga y estrés a 1,5 veces el peak declarado, resiliencia, recuperación ante desastres, seguridad ofensiva, accesibilidad y migración, con sus criterios de salida — Transversales S20.1, Estrategia de pruebas).

La trazabilidad del cumplimiento hacia los requerimientos RF/RNF/RT que satisfacen.

El registro de las observaciones previas resueltas (BA Art. 18.2–18.3).

La aceptación de un entregable no libera al ADJUDICATARIO de la responsabilidad por defectos posteriores (BA Art. 18.4).


### 3.11.2 Resultados de negocio del Capítulo 18: metas, momento y medición

Los dieciséis resultados de negocio del Capítulo 18 del caso son el criterio de aceptación del alcance con el CLIENTE (caso Cap. 18). El nivel comprometido, el momento del cronograma en que se alcanza y el mecanismo de medición son los siguientes:


> **Tabla 20** — 3.11.2 Resultados de negocio del Capítulo 18: metas, momento y medición · 17 filas · ver planilla del subdocumento

LAFROX

Propuesta de Solución — Distribuidora Puelche S.A.

Licitación N° TFEP-01/2026 — Caso 02 Logística

SUBDOCUMENTO 4.1–4.2

Arquitectura de la Solución

Parte 4.1 · Arquitectura Lógica    |    Parte 4.2 · Arquitectura Física y de Despliegue

Informe 1
