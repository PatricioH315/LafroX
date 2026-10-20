# Guion explicado y fundamentado — Presentación del Informe 2

**LafroX · revisión del 20 de octubre de 2026**

Este documento explica las **53 posiciones** del archivo vigente `LafroX - Presentación Informe 2 v10.pptx`. Incluye un texto sugerido para exponer y el fundamento documental de cada una. No modifica la presentación ni sustituye lo entregado. Los textos sugeridos corrigen las simplificaciones detectadas; por eso algunos son más precisos que las notas actuales.

**Cómo leerlo:** «Pos.» es la posición real dentro de PowerPoint; «N.º visible» es el número impreso en la diapositiva. No coinciden: hay ampliaciones 06.1–06.8 y transiciones con número repetido. Los ejemplos didácticos se identifican como tales: no son hechos adicionales del caso.

**Importante:** esto es un guion de estudio completo, no un discurso para leer íntegramente en veinte minutos. Las ocho capas, las nueve fases de la EDT y las siete ramas de riesgos pueden exponerse como recorridos breves. Las referencias [SD1]–[SD13], [BA] y [BTT] se resuelven en el catálogo final. Para las contradicciones, consultar el documento de auditoría que acompaña este guion.

## Primero: ¿a qué se refiere la diapositiva 17?

Hay dos respuestas según la numeración:

### Si te refieres a la posición 17 de PowerPoint: «Datos con una sola verdad» — número visible 08

**La idea central es que la empresa no tenga versiones incompatibles de un mismo hecho.** No significa almacenar todo en una sola base de datos. El informe distribuye la información en quince dominios lógicos y permite bases locales y copias centrales, pero cada agregado tiene una autoridad de escritura definida.

Ejemplo didáctico: bodega confirma una salida de diez cajas contra su inventario local. Si se corta internet, esa salida sigue válida localmente; al reconectar se comunica al centro sin descontarla dos veces. La copia central puede estar atrasada durante el corte: «una verdad» no equivale a «todas las pantallas actualizadas instantáneamente».

La cadena dibujada relaciona cinco conceptos:

1. **Recepción:** registrar qué producto entró, su lote y vencimiento cuando corresponda.
2. **Lote:** conservar su identidad e historia térmica; Calidad resuelve los bloqueos sanitarios.
3. **Unidad logística:** identificar el pallet, caja o contenedor y relacionar su contenido con los productos y lotes. Una unidad no tiene necesariamente un único lote.
4. **Ruta:** saber en qué viaje y parada se transportó ese contenido y con qué evidencia térmica.
5. **Entrega:** unir la mercadería entregada con el cliente y la evidencia de recepción aplicable.

EPCIS 2.0 aporta un formato de eventos para reconstruir qué pasó y cuándo, dónde y sobre qué objetos. No es una base de datos ni una certificación sanitaria. Los quince dominios no son los cinco pasos del dibujo ni quince servidores.

Los aproximadamente **16,05 GB** son una estimación de datos de origen para migrar; los **32,11 GB** estiman almacenamiento de destino con factor dos. «Cero diferencias sin explicar» permite diferencias identificadas, justificadas y aprobadas; no autoriza inventar lotes históricos que nunca se registraron. Tampoco demuestra que la migración ya se haya ejecutado.

**Texto sencillo para explicar esta diapositiva:**

> Esta lámina explica cómo evitamos que bodega, reparto y administración manejen datos distintos sobre una misma mercadería. Registramos el lote al recibir, relacionamos el contenido de las unidades logísticas con sus lotes, seguimos su paso por la ruta y guardamos evidencia de la entrega. Cada dato tiene una autoridad definida para modificarlo. Si se pierde la conexión, el sitio o el móvil conserva los hechos autorizados y los sincroniza después sin duplicar sus efectos. Así podemos reconstruir a qué clientes llegó un lote. Calidad decide sobre su condición sanitaria. La migración se aprobará únicamente con conciliaciones y sin diferencias no explicadas.

**Fundamento:** [SD5], §§5.1.4, 5.1.7, 5.2.1–5.2.5 y 5.3; Tabla 5.2 y Figura 5.5; [SD5-A], diccionario de unidad logística y reglas 5-C. [BA], art. 17.2, exige fuente única y evitar doble digitación durante la convivencia.

### Si te refieres al número 17 que aparece en pantalla: posición 26 — EDT, fase 6 «Infraestructura»

**La idea central es convertir el diseño de arquitectura en instalaciones realmente utilizables.** La arquitectura explica qué necesitamos; Adquisiciones gestiona compras y contratos; esta fase instala, configura, integra y prueba lo adquirido. No se refiere solo a programar software o contratar AWS.

| Cuenta de control | Qué significa en la práctica |
|---|---|
| 6.1 Sala técnica Talca | Preparar energía, climatización, detección/extinción y recepción técnica de la sala. La separación por obra civil corresponde al cliente; LafroX la especifica y coordina según el paquete. |
| 6.2 Cableado | Tender y certificar enlaces, etiquetarlos y entregar planos de lo instalado. |
| 6.3 Racks y gabinetes | Montar servidores, comunicaciones y equipos de borde en Talca, Concepción y los tres cross-docking. |
| 6.4 Seguridad física | Controlar acceso, videovigilancia y custodia física de respaldos. No confundir con ciberseguridad del software. |
| 6.5 Equipamiento de campo | Enrolar terminales, configurar pagos e impresoras e instalar sensores y termógrafos. El cliente compra el equipamiento de terreno conforme a la especificación de LafroX. |
| 6.6 Configuración de sitios | Instalar software base, habilitar comunicaciones y verificar continuidad local. |

La fase tiene **3.840 HH, seis cuentas de control y 24 paquetes**. HH significa esfuerzo de trabajo, no duración: dos técnicos durante ocho horas consumen 16 HH, aunque transcurra un solo día. Los meses 3–12 resumen la ventana global; cada paquete tiene sus propias dependencias y fecha límite.

Ejemplo didáctico: comprar un servidor no demuestra que la bodega resista un corte eléctrico. Debe estar montado, conectado a los circuitos previstos y probado junto con UPS, generador, comunicaciones y aplicaciones.

**Texto para exponer:**

> Esta fase materializa la arquitectura. No basta con tener el software desarrollado o los equipos comprados: debemos dejar operativas la sala de Talca, las redes, los racks, la seguridad física, los dispositivos de terreno y los cinco sitios con cómputo. Por eso la EDT separa seis cuentas de control, con 24 paquetes y 3.840 horas-hombre. Cada paquete termina con una evidencia verificable: enlaces certificados, terminales enrolados, sensores reportando o pruebas de continuidad aprobadas. Las responsabilidades de compra no cambian: el cliente adquiere el equipamiento de terreno y LafroX lo especifica, configura e integra según lo comprometido.

**Fundamento:** [T14], §7.2.6 y Tablas 7.36–7.41; [SD6], §6.1.3; [SD4], §§4.2–4.3. [BA], art. 16, exige despliegue híbrido; [BTT], capítulos 6 y 7, desarrolla infraestructura y continuidad.

---

## Guion por cada diapositiva

### Pos. 1 · Sin número visible · Propuesta técnica

**Qué significa:** presenta al proponente, al mandante y al sistema ofrecido; no comunica resultados ya obtenidos.

**Texto para exponer:**
> Somos LafroX SpA y presentamos la propuesta técnica del Sistema Integral de Gestión Logística Puelche para la licitación TFEP-01/2026. La propuesta abarca la solución, su implantación en dos etapas y su operación posterior. Explicaremos qué problema resuelve, cómo funciona y con qué evidencias se verificará su cumplimiento. Las cifras de mejora que mostraremos son metas y compromisos de la propuesta, no resultados de una implantación ya realizada.

**Fundamento:** [SD1], introducción y §1.5; [SD3], §§3.1–3.2; [BA], arts. 14–17. La distinción entre propuesta y ejecución evita presentar pruebas futuras como realizadas.

### Pos. 2 · N.º visible 01 · Retiro sanitario de marzo de 2026

**Qué significa:** el retiro muestra el costo de no poder relacionar un lote con los clientes que lo recibieron.

**Texto para exponer:**
> El incidente que da urgencia al proyecto es el retiro sanitario de marzo de 2026. Puelche demoró nueve días en reconstruir a qué clientes había llegado el producto y retiró 4.800 kilos. El proveedor involucrado, que representa el 6 % de las ventas, suspendió a Puelche por seis meses. Ese 6 % expresa la relevancia comercial del proveedor: no significa que la empresa haya perdido automáticamente ese porcentaje de ventas durante todo el período.

**Fundamento:** [SD2], §§2.1 y 2.2.1. El diagnóstico atribuye estas cifras al caso; no se encontró en las carpetas un PDF independiente del Caso Logística para verificarlas directamente contra él.

### Pos. 3 · N.º visible 02 · Tres problemas y una causa raíz

**Qué significa:** conecta el problema sanitario, el servicio y el costo de servir con una falla común de captura de datos.

**Texto para exponer:**
> Identificamos tres problemas relacionados: dificultad para acreditar trazabilidad sanitaria, un servicio poco competitivo y desconocimiento del costo real de atender a cada cliente. El diagnóstico encuentra un patrón común: los hechos se registran tarde, en papel o de manera incompleta. Sin lote al recibir, evidencia al entregar y cobro asociado a la entrega, las áreas deben reconstruir después lo ocurrido. Capturar el dato en su origen es la condición para controlar y medir; no afirmamos que sea la única causa posible de toda ineficiencia.

**Fundamento:** [SD2], §§2.1, 2.2.1 y 2.3.2. El 41 % sin lote se limita al producto del retiro, no a todas las recepciones.

### Pos. 4 · N.º visible 03 · Datos clave: situación y metas

**Qué significa:** compara líneas base con referencias o metas. No todas las metas provienen de las bases ni tienen el mismo horizonte.

**Texto para exponer:**
> Partimos de OTIF de 82,4 %, reentregas de 4,2 % y merma por vencimiento de 1,7 %. Buscamos identificar clientes afectados por un lote en menos de dos horas y explicar las diferencias de rendición el mismo día. Para OTIF debemos distinguir la referencia del caso, superior al 95 %, del compromiso que ofertamos: 90 % al mes 15, 93 % al 19 y 95 % al 32. La merma de hasta 1 % es una meta propia de LafroX. El registro completo de lote se exige a los productos que lo requieren.

**Fundamento:** [SD2], Tabla 2.1 y texto explicativo; [SD3], §3.2.5 y criterio R18-04. **Advertencia:** la lámina debe corregirse para no equiparar la referencia «>95 %» con el compromiso ofertado.

### Pos. 5 · N.º visible 04 · Esquema de solución

**Qué significa:** ofrece tres perspectivas del mismo sistema: ciclo logístico, trazabilidad y continuidad.

**Texto para exponer:**
> El primer esquema muestra el flujo desde el pedido hasta la preparación, la entrega y la rendición. El segundo sigue la mercadería por lote y relaciona su historia con los clientes. El tercero explica cómo seguimos trabajando cuando se corta la conexión: catorce horas en terreno y al menos veinticuatro horas en bodega, bajo las autorizaciones previstas. Al recuperar el enlace se sincroniza y concilia. El ERP existente sigue siendo el único emisor tributario; no lo reemplazamos con un segundo emisor.

**Fundamento:** [SD3], §3.3, Figuras 3.1–3.3; [SD5], Tabla 5.1. La sincronización móvil ≤10 minutos y la consolidación de sitio ≤2 horas son compromisos distintos, posteriores al restablecimiento del enlace.

### Pos. 6 · N.º visible 05 · Mapa de módulos

**Qué significa:** diferencia canales de acceso, capacidades del negocio y sistemas con que se integra la solución.

**Texto para exponer:**
> Las siete interfaces son puertas de entrada para los distintos usuarios; los doce módulos ejecutan las reglas de negocio. Recepción, inventario, preparación y calidad conectan la bodega; preventa, rutas, reparto y devoluciones conectan el trabajo en terreno; cobranza y analítica consolidan resultados. El ERP conserva la emisión tributaria y se integra mediante una frontera controlada. La Etapa 2 no agrega solamente M11: también habilita los portales y amplía M10 con costo de servir. M10 ya entrega OTIF en la Etapa 1.

**Fundamento:** [SD3], §§3.2, 3.4.1–3.4.3 y Figuras 3.4–3.8; [SD4], §4.1 y Anexo 4-F. **Corregir nota actual:** «solo M11 espera a la Etapa 2» es una simplificación que deja fuera portales y costo de servir.

### Pos. 7 · N.º visible 06 · Arquitectura lógica general

**Qué significa:** organiza responsabilidades del software, no pisos físicos ni ocho servidores.

**Texto para exponer:**
> Esta vista organiza el sistema en ocho capas. Las primeras seis separan la interfaz, la protección de entrada, el acceso a servicios, las reglas de negocio, la integración y la persistencia. Seguridad y observabilidad atraviesan todas ellas. La separación evita que una aplicación modifique directamente datos ajenos o que cada módulo invente su propia forma de integrarse. El mismo diseño contempla acceso local al WMS cuando no hay enlace con la nube. A continuación se amplía cada responsabilidad.

**Fundamento:** [SD4], §4.1.1 y Figura 1. [BA], arts. 19 y 24, exige arquitectura gobernada y controles verificables. No confundir los doce módulos con doce microservicios independientes: el diseño declara monolito modular.

### Pos. 8 · N.º visible 06.1 · Capa 1: Presentación

**Qué significa:** define qué ve y utiliza cada actor.

**Texto para exponer:**
> La presentación es la parte con la que interactúan preventistas, conductores, bodega, clientes y áreas administrativas. La aplicación Kotlin tiene perfiles diferenciados para el trabajo móvil; los portales y consolas usan la interfaz web. Cada perfil muestra solo las funciones que necesita y respeta sus condiciones de trabajo. El preparador usa un terminal de bodega, mientras que un cliente puede utilizar el portal opcional de la Etapa 2. Que existan varias interfaces no significa que cada una tenga reglas de negocio independientes.

**Fundamento:** [SD4], apartado de capa de presentación y Figura 2; [SD3], §3.4.1. El canal tradicional conserva atención por preventista y no queda obligado a tener internet propio.

### Pos. 9 · N.º visible 06.2 · Capa 2: Borde y exposición

**Qué significa:** protege los puntos por los que llegan solicitudes y conexiones.

**Texto para exponer:**
> Antes de llegar al negocio, el tráfico pasa por controles de borde. La arquitectura combina distribución de contenido, protección frente a ataques, cifrado de las comunicaciones y controles de red en los sitios. El objetivo es reducir exposición y permitir únicamente las entradas previstas. Esta capa filtra y protege, pero no decide si un lote puede venderse o si un cliente tiene crédito: esas decisiones corresponden al negocio. El borde local también considera los componentes de frío que deben seguir funcionando sin WAN.

**Fundamento:** [SD4], capa de borde y exposición; [BTT], capítulos 2 y 11. La defensa de red complementa, pero no reemplaza, autorización y validación funcional.

### Pos. 10 · N.º visible 06.3 · Capa 3: Enlace de servicios

**Qué significa:** controla cómo una interfaz llega a los servicios autorizados.

**Texto para exponer:**
> Esta capa recibe las solicitudes y las dirige al servicio correspondiente después de los controles de acceso aplicables. En la nube aparece la puerta de enlace hacia los servicios privados. En bodega existe una API local del WMS con verificación local, para no depender de internet en cada operación autorizada. Administrar o monitorear infraestructura no concede por sí mismo permisos para realizar operaciones del negocio. Así se conserva una entrada controlada tanto en la nube como en el sitio.

**Fundamento:** [SD4], capa de enlace de servicios y reglas de operación local; [SD5], §5.2.3. Los permisos sin conexión son preemitidos: el sitio no crea autorizaciones nuevas arbitrariamente.

### Pos. 11 · N.º visible 06.4 · Capa 4: Lógica de negocio

**Qué significa:** contiene las reglas que dan sentido a la operación.

**Texto para exponer:**
> Aquí viven las reglas de los doce módulos: qué se puede recibir, reservar, preparar, entregar, cobrar o bloquear. La solución usa un monolito modular Laravel: los módulos comparten una estructura de aplicación, pero mantienen límites y contratos. El perfil local ejecuta las funciones de bodega necesarias para continuar durante una desconexión; no equivale a copiar todas las capacidades centrales en cada terminal. Separar reglas y responsabilidades permite cambiar un módulo sin que otro modifique sus datos por fuera del contrato.

**Fundamento:** [SD4], capa de negocio y catálogo de módulos; Anexos 4-D y 4-F. [SD5], §§5.2.1–5.2.3, establece autoridad y persistencia por agregado.

### Pos. 12 · N.º visible 06.5 · Capa 5: Integración y eventos

**Qué significa:** permite intercambiar hechos entre componentes sin perderlos ni duplicar sus efectos.

**Texto para exponer:**
> Cuando ocurre una recepción o una entrega, otros módulos necesitan conocerla. Esta capa conserva y distribuye esos eventos, integra los sitios y maneja excepciones. Las colas permiten esperar durante una interrupción; al reconectar, los consumidores comprueban qué evento ya procesaron. La frontera del ERP traduce sus contratos sin trasladar sus particularidades al resto del sistema. No prometemos que ningún mensaje se repita: prometemos controlar los reintentos para que una repetición no descuente stock o registre un cobro dos veces.

**Fundamento:** [SD4], capa de integración y Anexos 4-A–4-B, 4-J–4-K; [SD5], §5.2.2. Outbox, inbox e idempotencia sostienen esa garantía de efectos.

### Pos. 13 · N.º visible 06.6 · Capa 6: Acceso a datos

**Qué significa:** selecciona dónde y cómo persistir cada clase de información.

**Texto para exponer:**
> No todos los datos requieren el mismo almacenamiento. Las transacciones y relaciones críticas usan persistencia relacional; la telemetría, los documentos, la caché y la analítica tienen funciones distintas. Los quince dominios delimitan responsabilidad sobre los datos, no quince máquinas obligatorias. Hay datos con autoridad local y datos con autoridad central; las copias de consulta pueden quedar atrasadas durante un corte. La analítica se separa de la transacción para que calcular indicadores no vuelva lento el despacho.

**Fundamento:** [SD4], capa de datos; [SD5], §§5.1.1, 5.2.1 y 5.2.6. [BA], art. 23, exige separación transaccional-analítica.

### Pos. 14 · N.º visible 06.7 · Capa 7: Seguridad transversal

**Qué significa:** protege identidades, permisos, datos y evidencias en todas las capas.

**Texto para exponer:**
> La seguridad no es una pantalla de inicio de sesión. Incluye identidad, autorización por función y ámbito, protección de credenciales, cifrado, seguridad de los equipos y auditoría. Una persona puede estar autenticada y aun así no tener permiso para liberar un lote o modificar crédito. En desconexión solo se aceptan operaciones dentro del permiso ya emitido y de su vigencia. Los registros de auditoría permiten reconstruir quién hizo qué, sin confundir administración de infraestructura con autoridad de negocio.

**Fundamento:** [SD4], capa de seguridad y Anexos 4-Q–4-R; [SD5], Tabla 5.1 y §§5.2.3, 5.2.7; [BTT], capítulo 11. Autonomía de 24 horas y credencial de turno de ocho horas miden objetos distintos; existen relevos preinscritos.

### Pos. 15 · N.º visible 06.8 · Capa 8: Observabilidad transversal

**Qué significa:** permite saber qué ocurre en la operación y localizar una falla de extremo a extremo.

**Texto para exponer:**
> La observabilidad reúne métricas, registros y trazas de nube y sitios. Un identificador de correlación permite seguir una transacción por sus componentes y reconocer dónde se retrasó o falló. El objetivo no es solo comprobar que un servidor esté encendido, sino verificar que un pedido, una preparación o una entrega puedan completarse. Los sitios conservan información cuando no hay enlace y la remiten después. Esta evidencia apoya tanto el soporte como la demostración de los niveles de servicio.

**Fundamento:** [SD4], capa de observabilidad; [BA], art. 25; [BTT], capítulo 14. Supervisar infraestructura no equivale a demostrar disponibilidad de la transacción crítica.

### Pos. 16 · N.º visible 07 · Arquitectura física

**Qué significa:** ubica físicamente los componentes de la arquitectura lógica.

**Texto para exponer:**
> La solución combina nube y cómputo en cinco sitios. La región principal es São Paulo, con despliegue en varias zonas; Virginia soporta recuperación ante desastres. Talca cuenta con un clúster de tres nodos; Concepción tiene servidores activo y en espera; cada cross-docking incorpora dos mini-PC. Los sitios se comunican por conexiones controladas y conservan funciones locales. Las zonas de disponibilidad protegen frente a fallas dentro de una región; la región secundaria atiende otro escenario de desastre. Ninguna sustituye las pruebas de recuperación.

**Fundamento:** [SD4], Figura 14 y §§4.2.2–4.2.5; [BA], art. 16. La figura original incorporada fue inspeccionada. Dos zonas no significan dos regiones, y replicar no reemplaza disponer de respaldos restaurables.

### Pos. 17 · N.º visible 08 · Datos con una sola verdad

**Qué significa:** une captura, autoridad de escritura y cadena de custodia; no impone una base de datos única.

**Texto para exponer:**
> Registramos lote y vencimiento al recibir; relacionamos los productos y lotes con el contenido de las unidades logísticas; seguimos su transporte y guardamos evidencia de entrega. Cada agregado tiene una autoridad para escribirlo y los eventos mantienen la custodia. Calidad toma la decisión sanitaria. Durante una desconexión se conservan hechos autorizados, pero la visión central se completa al sincronizar. La migración parte de unos 16 GB de origen y debe aprobarse con conciliación: ninguna diferencia puede quedar sin explicación.

**Fundamento:** [SD5], §§5.1.4, 5.1.7, 5.2.1–5.2.5 y 5.3. Ver la explicación ampliada al principio. **Corregir etiqueta:** «unidad logística y contenido por producto/lote» es más preciso que «pallet o canastillo con su lote».

### Pos. 18 · N.º visible 09 · Metodología y gobierno

**Qué significa:** combina control formal del contrato con desarrollo incremental y gestión cotidiana del trabajo.

**Texto para exponer:**
> PMBOK aporta líneas base y control del proyecto; RUP ordena el desarrollo iterativo; DevSecOps automatiza controles antes de promover un cambio. Kanban hace visible el trabajo diario, pero no reemplaza la aceptación contractual. Revisamos avance semanalmente y resolvemos decisiones en los comités previstos. SPI y CPI comparan el valor ganado con la programación y el esfuerzo correspondiente; una razón menor que 0,90 activa una alerta. Una iteración de dos semanas puede producir un incremento verificable sin implicar un despliegue inmediato a producción.

**Fundamento:** [SD6], §§6.1–6.2; [T9] y [T10]. Las ventanas de congelamiento y cierre mensual restringen despliegues aunque continúen programación, documentación y otras tareas permitidas.

### Pos. 19 · N.º visible 10 · Fases RUP y ciclo DevSecOps

**Qué significa:** relaciona las fases del trabajo con los controles que atraviesa cada cambio.

**Texto para exponer:**
> Inicio define el encargo; Elaboración valida la arquitectura; Construcción implementa; Transición prepara la entrada operacional. Las horas mostradas corresponden a esas cuatro fases de la EDT. Construcción concentra aproximadamente la mitad de ese subtotal, no la mitad de todo el contrato. Cada cambio pasa por revisión, pruebas y controles automatizados antes de llegar a QA. Los umbrales bloquean el avance cuando no se cumplen, y la seguridad exige ausencia de hallazgos críticos y altos según las reglas de promoción.

**Fundamento:** [T14], fases 1–4; [SD9], §§9.1.5 y 9.2.1. Subtotal RUP: 65.192 HH; Construcción: 33.280 HH, aproximadamente 51,1 %. Ver auditoría sobre la discrepancia «80 % global» frente a «80 % de código modificado» entre subdocumentos.

### Pos. 20 · N.º visible 11 · EDT general

**Qué significa:** descompone el alcance en trabajo controlable. No es todavía un calendario ni un organigrama.

**Texto para exponer:**
> La EDT organiza el proyecto en nueve fases, 49 cuentas de control y 222 paquetes. Una cuenta agrupa trabajo relacionado; el paquete es la unidad que recibe entregable, responsable y criterio de aceptación. Las fases RUP conviven con adquisiciones, infraestructura, capacitación, operación y cierre. Las horas de las nueve fases suman 205.007. La programación completa llega a 217.543 al añadir restauraciones previas, soporte puente y capacidad protegida. Son dos vistas conciliables del esfuerzo, no totales intercambiables.

**Fundamento:** [T14], §§7.1–7.2; [T15], §§7.4.2–7.4.3. Puente exacto: 205.007 + 128 + 9.336 + 3.072 = 217.543 HH. Las HH de Inicio–Transición ya corresponden al desglose presentado: no volver a multiplicarlas por dos por repetirse el ciclo en cada etapa.

### Pos. 21 · N.º visible 12 · EDT: Inicio

**Qué significa:** establece acuerdos y controles antes de ejecutar trabajo sin una definición común.

**Texto para exponer:**
> Inicio reúne nueve cuentas de control. Además de definir el alcance y planificar, identifica interesados, calidad, riesgos, gobierno, cumplimiento y reversibilidad. Su función es acordar qué se va a entregar, cómo se decidirá y con qué evidencia se aceptará. Incluye 6.920 horas-hombre y 35 paquetes en la vista de la EDT. Estos controles se aplican a las etapas correspondientes; no son solo un documento inicial que después se olvida.

**Fundamento:** [T14], §7.2.1, cuentas 1.1–1.9; [SD6], gestión de interesados, integración y líneas base.

### Pos. 22 · N.º visible 13 · EDT: Elaboración

**Qué significa:** reduce incertidumbre de diseño antes de construir o instalar a escala.

**Texto para exponer:**
> Elaboración define y valida arquitectura, seguridad, sala técnica, continuidad y experiencia de usuario. La EDT le asigna seis cuentas, 18 paquetes y 4.320 horas-hombre. El resultado esperado no es simplemente un dibujo: es un diseño revisado con decisiones y criterios verificables. En la Etapa 1 el cierre de diseño se asocia al H2 del mes 4; en la Etapa 2, al H8 del mes 14. Validar temprano evita descubrir una incompatibilidad cuando los módulos ya están construidos.

**Fundamento:** [T14], §7.2.2; tabla de hitos de diseño. Arquitectura es diseño; el montaje efectivo pertenece a la fase 6.

### Pos. 23 · N.º visible 14 · EDT: Construcción

**Qué significa:** convierte el diseño en software, integraciones y evidencias técnicas.

**Texto para exponer:**
> Construcción reúne once cuentas y 79 paquetes, con 33.280 horas-hombre. Incluye ambientes, nube, base compartida, módulos de ambas etapas, integraciones, migración, pruebas, innovaciones y documentación. No equivale únicamente a escribir código: el incremento debe funcionar con los otros componentes y demostrarlo. La separación entre pruebas de E1 y E2 permite aceptar el alcance nuevo sin perder la regresión sobre lo que ya está operativo.

**Fundamento:** [T14], §7.2.3, cuentas 3.1–3.11; [SD9], alineación de certificaciones con las cuentas 3.8 y 3.9.

### Pos. 24 · N.º visible 15 · EDT: Transición

**Qué significa:** lleva una solución técnicamente probada a una operación real controlada.

**Texto para exponer:**
> Transición incluye el plan de implantación, la marcha blanca y la entrada a producción de cada etapa. Durante la marcha blanca se observa la solución con operación real, se concilian registros y se resuelven defectos. No basta con terminar una fecha del Gantt: deben cumplirse conjuntamente las condiciones de aceptación y firmarse el acta. Los pasos contractuales son H7 en el mes 16 y H12 en el mes 21. El acompañamiento y la estabilización previstos no desaparecen al firmar el hito.

**Fundamento:** [T14], §7.2.4; [T18]; [BA], arts. 17.3 y 18. En E2 el acompañamiento de cuatro semanas se distribuye entre meses 21 y 22 según el calendario supuesto.

### Pos. 25 · N.º visible 16 · EDT: Adquisiciones

**Qué significa:** asegura que equipos, servicios y acuerdos estén disponibles antes de necesitarlos.

**Texto para exponer:**
> Esta fase gestiona hardware, nube y licencias, enlaces y acuerdos con terceros. Sus cuatro cuentas y trece paquetes suman 1.040 horas-hombre. El cliente compra el equipamiento de terreno conforme a las especificaciones de LafroX; eso no significa que compre toda la infraestructura. LafroX asume la provisión que le corresponde y la recepción técnica de lo adquirido. Los acuerdos con transportistas, sindicato y otros actores resuelven dependencias que no se solucionan programando una aplicación.

**Fundamento:** [T14], §7.2.5, cuentas 5.1–5.4; [SD6], §6.1.3. Distinguir especificación, compra, recepción técnica e instalación.

### Pos. 26 · N.º visible 17 · EDT: Infraestructura

**Qué significa:** deja listas y probadas las instalaciones que soportarán el sistema.

**Texto para exponer:**
> Aquí pasamos del diseño y las compras a la infraestructura instalada. Preparamos la sala técnica, certificamos cableado, montamos racks y gabinetes, habilitamos seguridad física y configuramos terminales, sensores y sitios. Las seis cuentas reúnen 24 paquetes y 3.840 horas-hombre. Lo importante es su criterio de término: no se acepta por declarar que está instalado, sino con pruebas de energía, enlaces, continuidad y funcionamiento. Estas tareas sostienen la operación híbrida y la posibilidad de que las bodegas continúen sin conexión con la nube.

**Fundamento:** [T14], §7.2.6, Tablas 7.36–7.41; [SD4], arquitectura física y sala técnica. Ver desglose ampliado al principio del documento.

### Pos. 27 · N.º visible 18 · EDT: Capacitación y cambio

**Qué significa:** prepara a los usuarios y a las organizaciones para operar la solución, no solo para asistir a una charla.

**Texto para exponer:**
> La capacitación se organiza por rol y se complementa con gestión del cambio y evaluaciones. Los usuarios deben demostrar que pueden ejecutar sus tareas; asistir a una sesión no equivale a estar certificado. Las tres cuentas suman trece paquetes y 4.736 horas-hombre. La programación respeta turnos, preparación nocturna y despacho. También considera a cadenas y transportistas. La relación sindical tiene acuerdos específicos y no se reduce a la capacitación final.

**Fundamento:** [T14], §7.2.7 y cuenta 5.4.2; [T18]; [BA], art. 17.3; [BTT], capítulo 22.

### Pos. 28 · N.º visible 19 · EDT: Operación y soporte

**Qué significa:** el trabajo continúa después de implantar: hay servicio, mantenimiento, pruebas periódicas y transferencia.

**Texto para exponer:**
> La fase de operación agrupa servicios operacionales, mantenimiento, innovaciones, informes y transferencia. La vista de EDT asigna 129.879 horas-hombre a sus 26 paquetes. No debemos confundir esa clasificación con el bloque temporal de Operación entre los meses 21 y 56, que programa aproximadamente 128.854 horas. La diferencia responde a cómo se imputan paquetes y períodos; no son dos cifras del mismo subtotal. Además, la disponibilidad de personas y las reservas debe verificarse antes de prometer capacidad inmediata.

**Fundamento:** [T14], §7.2.8; [T15], Tabla 7.3 y explicación de imputaciones; [BA], arts. 15 y 17. La operación contractual dura 36 meses y empieza simultáneamente con la producción de E2.

### Pos. 29 · N.º visible 20 · EDT: Cierre

**Qué significa:** distingue finalizar la implementación de salir ordenadamente al término del contrato.

**Texto para exponer:**
> Cierre tiene dos cuentas y cuatro paquetes, con 320 horas-hombre. Una cuenta formaliza el cierre de la implementación; la otra prepara la salida al término del contrato. El cliente debe recibir información, documentación y elementos necesarios para continuar sin dependencia indebida. La reversibilidad se planifica desde el inicio, aunque la salida se ejecute al final. Firmar H12 no equivale a terminar las obligaciones de operación ni a aceptar anticipadamente indicadores cuyo horizonte de medición es posterior.

**Fundamento:** [T14], §7.2.9; plan de reversibilidad; [T17], aceptación diferenciada de OTIF y envases.

### Pos. 30 · N.º visible 21 · Bloques contractuales y frentes

**Qué significa:** diferencia «en qué período del contrato estamos» de «qué equipo o frente trabaja».

**Texto para exponer:**
> El contrato tiene dos etapas de implementación y una fase de Operación. Para ejecutarlas usamos ocho frentes con responsables definidos. No son lo mismo: un frente puede participar en más de un período. Entre meses 13 y 15 coinciden la marcha blanca de E1 y el desarrollo de E2; entre 19 y 20, E1 ya está en producción mientras E2 está en marcha blanca. Los frentes deben proteger la atención de E1 sin consumir el mismo equipo comprometido en construir E2.

**Fundamento:** [BA], arts. 17.1–17.2; [T15], §7.3 y Tabla 7.1. «E1 m1–16» y «E2 m13–21» incluyen los hitos de paso; desarrollo y marcha blanca tienen subperíodos propios.

### Pos. 31 · N.º visible 22 · Gantt de implementación

**Qué significa:** ubica trabajo, restricciones e hitos en el tiempo. Es una síntesis, no la demostración completa de factibilidad.

**Texto para exponer:**
> El Gantt muestra cómo se coordinan diseño, construcción, infraestructura, migración, pruebas y marchas blancas. H7 marca la producción de E1 en el mes 16 y H12 la de E2 en el mes 21. Los congelamientos limitan los despliegues y cada corte debe tener reversión. Las marcas de riesgo señalan meses de atención estimada, no fechas ciertas de ocurrencia. La ubicación de septiembre y diciembre usa el supuesto de inicio en febrero de 2027; si cambia la fecha contractual, hay que recalcularla.

**Fundamento:** [T14], §7.3; [T15], programación y advertencias de recalculación; [T18]; [SD8-A], Anexo 8.B. El T-15 advierte que su red nominal histórica no acredita por sí sola la factibilidad de la línea base vigente.

### Pos. 32 · N.º visible 22 repetido · Continuación del Gantt

**Qué significa:** es un segundo estado de la misma lámina para continuar la exposición; no es un cronograma independiente.

**Texto para exponer:**
> Sobre el mismo calendario, destaquemos la calidad y el cambio organizacional. La certificación y las pruebas habilitantes deben preceder a cada entrada a producción. Las restauraciones de respaldos y la operación continúan después de la implantación. La reversión debe caber en la ventana disponible y preservar el despacho. Por eso el calendario no solo ordena desarrollo: reúne pruebas, personas, cortes y condiciones para aceptar. Los riesgos y la disponibilidad efectiva de especialistas deben contrastarse con esta programación.

**Fundamento:** misma base de la posición 31; [SD9], §9.3 y Figura 9.9. No sumar otra vez las horas por aparecer el Gantt dos veces.

### Pos. 33 · N.º visible 23 · Esfuerzo por mes

**Qué significa:** estima demanda mensual de esfuerzo y de personas equivalentes; no acredita contratos de trabajo ni dotación ya reservada.

**Texto para exponer:**
> La línea base programa 217.543 horas-hombre. El máximo mensual ocurre en el mes 15, con aproximadamente 8.106 horas, cuando se solapan trabajos de ambas etapas y acompañamiento. La demanda publicada es de 69 personas equivalentes por roles. No se obtiene dividiendo sin más las horas totales por una jornada: la curva agrega necesidades por especialidad y usa redondeos. En operación el esfuerzo se estabiliza en el rango mostrado, con variaciones de calendario y cobertura. Antes de ejecutar hay que confirmar disponibilidad y asignaciones nominales.

**Fundamento:** [T15], §§7.4.1–7.4.4, Tablas 7.5–7.6. Capacidad de planificación: 160 HH nominales y 128 efectivas por persona-mes; no es una definición de jornada laboral.

### Pos. 34 · N.º visible 24 · RBS: origen de los riesgos

**Qué significa:** clasifica riesgos por fuente predominante, no por importancia.

**Texto para exponer:**
> El registro vigente tiene 45 riesgos agrupados en siete ramas. Tecnología reúne catorce; integración y legado, siete; operación del cliente, ocho; personas y adopción, siete; contrato, cuatro; regulatorio y externo, dos; y empresa proveedora, tres. Esa agrupación ayuda a asignar vigilancia, pero la rama no determina la gravedad. Los dos críticos son el retiro sin trazabilidad y la recuperación fuera de RTO y RPO. Un riesgo puede afectar a varias áreas aunque se ubique en una sola rama principal.

**Fundamento:** [SD8], §8.3.1 y Figura 8.1; [T16]. Los conteos 14+7+8+7+4+2+3 suman 45.

### Pos. 35 · N.º visible 25 · RBS: visión por cuentas y zonas

**Qué significa:** muestra los mismos riesgos con su clasificación de severidad, no otros 45 riesgos adicionales.

**Texto para exponer:**
> Cada punto representa un riesgo del registro. El color comunica su zona registrada: dos críticos, 23 altos, 19 medios y uno bajo. Una categoría con muchos riesgos no exige necesariamente más contingencia que otra con pocos: también importan probabilidad, impacto y esfuerzo condicional. Las fichas registran responsables y respuestas, pero el informe mantiene pendientes de definición algunos plazos, contingencias y riesgos secundarios. No debemos presentar el plan como si todas las respuestas ya estuvieran validadas o ejecutadas.

**Fundamento:** [SD8], introducción, §8.3 y Figura 8.1; [SD8-A], Anexo 8.A. La reserva de 2.058,5 HH es valor esperado de esfuerzo, no personal movilizado.

### Pos. 36 · N.º visible 26 · RBS rama 1: Solución y tecnología

**Qué significa:** reúne fallas potenciales de la solución y su continuidad técnica.

**Texto para exponer:**
> Esta rama concentra catorce riesgos, incluidos los dos críticos. Si no reconstruimos el lote y los clientes, falla el objetivo sanitario; si no recuperamos dentro de RTO y RPO, falla la continuidad comprometida. También vigilamos duplicados al reconectar, historia de datos, sensores, capacidad y privilegios. La respuesta no consiste en afirmar que la arquitectura es robusta: debe probarse con simulacros de retiro, recuperación, carga e inyección de fallas y con resultados verificables.

**Fundamento:** [SD8], Figura 8.1; [T16], R-004, R-005, R-008–R-013, R-015–R-016, R-032–R-033, R-037–R-038; [SD9], estrategia de pruebas.

### Pos. 37 · N.º visible 27 · RBS rama 2: Integración y legado

**Qué significa:** recoge dependencias y errores en el intercambio con otros sistemas.

**Texto para exponer:**
> La solución debe convivir con el ERP de 2017, integrar información legada y certificar el intercambio electrónico con las cadenas. Los siete riesgos de esta rama incluyen interfaces del ERP, convivencia del WMS, EDI, pagos y geolocalización. Un contrato de interfaz documentado no basta: hay que demostrarlo con mensajes, errores y reintentos reales de prueba. En pagos, una falta de respuesta no prueba que el cobro haya sido rechazado; reintentar sin conciliación puede producir doble cargo.

**Fundamento:** [T16], R-001–R-003, R-030–R-031, R-043 y R-045; [SD5], §5.1.8 y §5.2.3.

### Pos. 38 · N.º visible 28 · RBS rama 3: Operación del cliente

**Qué significa:** muestra condiciones del entorno del cliente que la aplicación no controla por sí sola.

**Texto para exponer:**
> Esta rama contiene ocho riesgos: enlaces, energía, sala, disponibilidad de contrapartes, instalaciones, congelamientos, rendición y custodia de envases. Aunque el software esté listo, una sala no recibida o un dispositivo no instalado puede impedir una ola de implantación. Por eso la respuesta necesita responsables, fechas y pruebas de recepción. Los congelamientos deben incorporarse al calendario desde el inicio; no resolverse al final cuando ya coinciden con un hito contractual.

**Fundamento:** [T16], R-006–R-007, R-014, R-022–R-024, R-028 y R-044; [T14], fases 5–6.

### Pos. 39 · N.º visible 29 · RBS rama 4: Personas y adopción

**Qué significa:** un sistema correcto puede fracasar si no incorpora conocimiento y prácticas reales de quienes lo usan.

**Texto para exponer:**
> Los siete riesgos incluyen objeción sindical, rotación de conductores, trabajo nocturno, capacitación que interrumpe la operación y pérdida del conocimiento de rutas. La mitigación exige acuerdos y aprendizaje por rol, no solo manuales. El conocimiento del planificador debe capturarse antes de depender del nuevo ruteo. Las innovaciones también necesitan validación humana: un aviso que nadie confirma o una hoja que el almacenero no entiende no generan valor por estar técnicamente implementados.

**Fundamento:** [T16], R-017–R-021, R-036 y R-040; [SD3], elicitación temprana del conocimiento; [T14], cuentas 5.4 y 7.1–7.3.

### Pos. 40 · N.º visible 30 · RBS rama 5: Contrato y licitación

**Qué significa:** protege la aceptación, el alcance acordado, la medición de incentivos y la salida.

**Texto para exponer:**
> Los cuatro riesgos de esta rama son marcha blanca sin aceptación, cambios de alcance no aprobados, problemas al atribuir mejoras del costo de servir y una salida incompleta. Terminar tareas no garantiza aceptación: el cliente debe comprobar criterios y firmar el acta. Los cambios de compromiso requieren aprobación previa. En INN-04, el pago variable necesita datos y una comparación acordada; no se puede atribuir todo ahorro al sistema ni deteriorar el servicio para reducir el costo.

**Fundamento:** [T16], R-026–R-027, R-039 y R-041; [BA], arts. 17–18; [SD13], §13.4.

### Pos. 41 · N.º visible 31 · RBS rama 6: Regulatorio y externo

**Qué significa:** agrupa exposición a evidencia insuficiente y a cambios de exigencias externas.

**Texto para exponer:**
> Esta rama tiene dos riesgos altos: evidencia de entrega insuficiente y cambio normativo. Una foto aislada no equivale automáticamente a un acuse válido ni reemplaza los documentos tributarios correspondientes. Debemos vincular evidencia, entrega y documento conforme al protocolo aplicable. Las reglas de conservación y protección de datos también deben revisarse cuando cambian las exigencias. La solución registra y protege evidencia; no convierte por sí sola cualquier archivo en una acreditación suficiente.

**Fundamento:** [T16], R-029 y R-042; [SD4-A], Anexo 4-U; [SD5], documentos, POD y retención. Se describe el diseño ofertado, no un dictamen jurídico sobre suficiencia probatoria.

### Pos. 42 · N.º visible 32 · RBS rama 7: Empresa proveedora

**Qué significa:** analiza riesgos de capacidad y sostenibilidad del propio proveedor.

**Texto para exponer:**
> LafroX también es una fuente de riesgo: puede comprometer a las mismas personas en trabajos simultáneos, subdimensionar el soporte o estimar mal costos y demanda. Tener ocho líderes identificados no demuestra que toda la capacidad de ejecución esté disponible. La planificación debe asignar especialistas y turnos, proteger los frentes solapados y comprobar la suficiencia de mesa, NOC y SOC. Las horas equivalentes y reservas son instrumentos de planificación; requieren recursos y autorizaciones reales para convertirse en capacidad operativa.

**Fundamento:** [T16], R-025, R-034 y R-035; [T15], advertencias sobre disponibilidad nominal y reservas. Ver auditoría sobre la diferencia documental del modelo de SOC.

### Pos. 43 · N.º visible 33 · Diez riesgos de mayor exposición

**Qué significa:** prioriza atención y separa valoración cualitativa de estimación cuantitativa.

**Texto para exponer:**
> La tabla ordena diez riesgos por exposición cualitativa. Los dos críticos tienen ponderación 0,50 por 0,80, igual a 0,40. Ese 0,50 no es la misma cifra que el 35 % inicial usado para estimar esfuerzo esperado: son modelos distintos. Las reducciones porcentuales de la derecha son objetivos condicionados a validar la mitigación. La contingencia calculada suma 2.058,48 horas y la reserva de gestión, 1.600. No deben confundirse con la capacidad protegida ya incluida en la programación ni presentarse como personal inmediatamente disponible.

**Fundamento:** [SD8], escalas cualitativas, valoración de los diez riesgos y apartado de reservas; [SD8-A], Anexo 8.B; [T15], gestión de reservas. El orden de los diez códigos coincide con la Tabla 8.4.

### Pos. 44 · N.º visible 34 · Matriz de exposición

**Qué significa:** ubica riesgos por ponderaciones de probabilidad e impacto. Los valores no son porcentajes exactos de ocurrencia.

**Texto para exponer:**
> La matriz cruza ponderación cualitativa de probabilidad e impacto. El número de cada celda cuenta riesgos y los identificadores permiten encontrarlos en el registro. Los dos críticos se ubican en probabilidad media e impacto alto. No interpretamos la fila 0,5 como una probabilidad estadística exacta ni como el porcentaje del análisis de valor esperado. Para mantener fidelidad con el Informe 2, conviene describir el color como la zona registrada, porque el texto vigente no autoriza recalcularla automáticamente a partir de cortes del producto.

**Fundamento:** [SD8], §§8.2–8.3 y Tabla 8.4; [T16]. **Corregir:** la leyenda de cortes ≥0,08/≥0,20/≥0,40 y la nota causal no reflejan la cautela metodológica expresa del informe.

### Pos. 45 · N.º visible 35 · Normas y leyes

**Qué significa:** conecta referencias exigidas con evidencias verificables; nombrar una norma no acredita cumplimiento.

**Texto para exponer:**
> La propuesta no se limita a citar estándares. Calidad del producto se acredita con métricas y umbrales; calidad de datos, con validaciones y conciliaciones; pruebas, con proceso y evidencia; accesibilidad, con herramientas y revisión manual. La lista también recoge las exigencias operacionales y normativas que el informe relaciona con frío, documentos, conductores y datos personales. Debemos separar esas materias de GS1 y EDI, que son estándares de identificación e intercambio, no leyes. Usamos las referencias tal como las declara el informe.

**Fundamento:** [SD9], Tabla 9.2 y §9.1.4; [SD2], §2.2.2; [BA], art. 4.3. Nombre completo: **ISO/IEC/IEEE 29119**. La fecha de Ley 21.719 se reproduce como afirmación del informe, no como verificación externa de legislación vigente.

### Pos. 46 · N.º visible 36 · Calidad del producto

**Qué significa:** transforma «buena calidad» en condiciones de medición y aceptación.

**Texto para exponer:**
> La calidad se evalúa con requisitos probados, ausencia de defectos críticos y altos al cierre y continuidad de la ventana de despacho. Las ocho características tienen métricas, no calificativos. En desempeño, el p95 significa que al menos el 95 % de las observaciones cumple el tiempo correspondiente bajo la carga de prueba; no es el promedio. En fiabilidad distinguimos transacción crítica de infraestructura: 99,9 % y 99,95 %, respectivamente. Los dieciséis resultados del caso tienen horizontes distintos: OTIF y pérdida anual de envases no quedan aceptados definitivamente por anticipado.

**Fundamento:** [SD9], Tablas 9.1 y 9.3, Figura 9.2 y Anexo 9.D; [T17], §5; [BTT], §7.2. RTO ≤4 horas es tiempo de recuperación; RPO ≤15 minutos es pérdida temporal máxima tolerada de datos.

### Pos. 47 · N.º visible 37 · Calidad que bloquea

**Qué significa:** distingue controles internos de promoción de las condiciones contractuales para aceptar una marcha blanca.

**Texto para exponer:**
> Las siete puertas G0 a G6 controlan el cambio desde el trabajo local hasta producción supervisada. No basta con llegar al final del pipeline: para cerrar la marcha blanca deben cumplirse juntas las seis condiciones contractuales. Se exige ausencia de incidentes críticos o altos abiertos atribuibles a la solución, volumen real comprometido durante al menos las cuatro últimas semanas, disponibilidad y tiempos de respuesta sostenidos, conciliación sin diferencias inexplicadas, capacitación y certificación del personal previsto y acta de la Contraparte Técnica. Una condición no compensa otra.

**Fundamento:** [SD9], §9.2.1; [T17]; [BA], art. 17.3, página impresa 13, PDF página 14. **Corregir condición 3 de la lámina:** «sin caída en despacho» no resume por completo disponibilidad y tiempos de respuesta sostenidos.

### Pos. 48 · N.º visible 38 · Pruebas: del código al terreno

**Qué significa:** cada riesgo se verifica en el ambiente y las condiciones donde puede manifestarse.

**Texto para exponer:**
> Las pruebas avanzan desde componentes y contratos hasta integración, aceptación, carga, resiliencia y operación real. El terreno agrega condiciones que una prueba de escritorio no reproduce: frío, guantes, lluvia, calor, una mano y desconexión. La carga de referencia es 21,99 transacciones por segundo, equivalente a 1,5 veces el peak declarado. El catálogo inicial tiene 1.316 casos, con 80 % automatizados como parámetro de diseño. Las 4,4 horas corresponden a unos 1.053 casos automatizados en dos ejecutores; los 263 manuales requieren unas 65,8 horas-hombre adicionales por ciclo.

**Fundamento:** [SD9], §9.2.3 y Tablas 9.8–9.9; [T13], §8. **Corregir:** no llamar a las 4,4 horas «regresión completa» incluyendo pruebas manuales y físicas. Son estimaciones de planificación, no mediciones de una ejecución acreditada.

### Pos. 49 · N.º visible 39 · Trazabilidad y mejora

**Qué significa:** la trazabilidad aquí es de ingeniería: vincula necesidad, construcción, prueba y aceptación; no es solo trazabilidad de mercadería.

**Texto para exponer:**
> Tomamos el retiro en menos de dos horas y seguimos su evidencia: requisito, módulo M9, paquete de trabajo, prueba, cambio de código, imagen desplegada y acta del hito. Así podemos comprobar qué satisface cada entrega y qué debe repetirse si cambia. PDCA ordena la mejora: planificar, hacer, verificar y actuar sobre resultados. Las 11.136 horas corresponden a conformidad programada, repartida en prevención y evaluación; no son el costo integral de cualquier falla futura. El cierre de una mejora necesita evidencia, no solo una acción declarada.

**Fundamento:** [SD9], §§9.1.6 y 9.2.5, Figuras 9.6–9.8 y Tablas 9.5–9.6. La secuencia lógica es Planificar → Hacer → Verificar → Actuar, independientemente de la ubicación gráfica de las palabras.

### Pos. 50 · N.º visible 40 · Cinco innovaciones

**Qué significa:** propone capacidades adicionales con hipótesis, pilotos y metas; no declara beneficios ya comprobados.

**Texto para exponer:**
> Proponemos cinco innovaciones: avisos de vencimiento posentrega, reproducción de incidentes, vida útil según historia térmica, incentivo por costo de servir y una hoja accesible para el almacenero. Reutilizan la infraestructura prevista: «sin hardware nuevo» se refiere a las innovaciones, no a todo el proyecto. Las metas deben medirse con su base y horizonte. Por ejemplo, el 30 % de diagnóstico se refiere a la mediana y la reducción de costo de servir se evalúa con servicio protegido. La estimación térmica apoya a Calidad; no autoriza por sí sola cambiar vencimientos o liberar alimentos.

**Fundamento:** [SD13], §§13.1–13.5; indicadores I-01B, I-02A, I-03B e I-04A; [T19]. I-01B se mide al mes 28 e I-04A al 36. La maduración y los hitos TRL no tienen el mismo calendario para las cinco innovaciones.

### Pos. 51 · N.º visible 41 · El equipo

**Qué significa:** muestra liderazgo y responsabilidad; no representa por sí sola a todo el personal ejecutor.

**Texto para exponer:**
> Alex Aravena es el jefe de proyecto e interlocutor principal. Siete líderes cubren arquitectura e integración, seguridad, datos, desarrollo, calidad, operación e implantación. Ocho personas asumen los diez roles mínimos mediante las asignaciones del informe. Este equipo directivo no debe confundirse con las 69 personas equivalentes de demanda máxima: esa cifra proviene de la programación por especialidad en el mes 15. La ejecución requiere comprobar dedicaciones, suplencias y disponibilidad efectiva, manteniendo la independencia de la función de calidad frente al desarrollo.

**Fundamento:** [SD1], §1.5 y Tabla 1.6; [T15], curva por rol; [SD9], responsabilidades de aseguramiento. Las 69 personas equivalentes no son 69 contratos acreditados.

### Pos. 52 · N.º visible 42 · «9 días» — transición

**Qué significa:** retoma el problema inicial para preparar el cierre. No agrega otro indicador ni una nueva meta.

**Texto para exponer:**
> Volvamos al punto de partida: nueve días para identificar a los clientes afectados por un lote. El problema no era solamente la lentitud de una consulta, sino la falta de una cadena de hechos registrados y relacionables. La propuesta responde a esa causa mediante captura, identidad, evidencia y control operacional.

**Fundamento:** [SD2], retiro sanitario; [SD3], solución de trazabilidad. Las notas actuales identifican esta lámina como transición automática: no exige detenerse a repetir toda la explicación.

### Pos. 53 · N.º visible 42 repetido · Cierre: de nueve días a menos de dos horas

**Qué significa:** resume el compromiso central, sujeto a implantación, pruebas y aceptación.

**Texto para exponer:**
> Nuestra propuesta busca pasar de reconstruir un retiro durante nueve días a identificar a los clientes afectados en menos de dos horas. Para ello capturamos los hechos donde ocurren, mantenemos autoridad sobre los datos y relacionamos lote, movimiento y entrega con evidencia. La operación autorizada continúa sin señal y la visión central se completa al reconectar y conciliar. No ofrecemos solo pantallas: ofrecemos una implantación con pruebas, responsables y condiciones explícitas de aceptación. Quedamos atentos a sus preguntas.

**Fundamento:** [SD3], R18-01 y solución de trazabilidad; [SD5], custodia y sincronización. **Precisión importante:** el plazo es para identificar clientes afectados; no promete retirar físicamente toda la mercadería en dos horas ni visibilidad central instantánea durante cualquier corte.

---

## Catálogo de fuentes locales

Las referencias corresponden a las copias entregadas disponibles en las carpetas suministradas. Los PDF son la fuente documental; los Markdown acompañantes se utilizaron para localizar secciones. Las Bases son escaneadas y se consultaron mediante OCR; las cláusulas clave de aceptación se contrastaron visualmente. No se trató la validación antigua de v4 como prueba automática de la v10.

- **Presentación revisada:** [v10](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/Principal/LafroX/Presentaciones/LafroX - Presentación Informe 2 v10.pptx>).
- **[SD1]:** [Presentación de la empresa](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 1/LAFROX-Subdocumento1.pdf>).
- **[SD2]:** [Comprensión del problema y necesidad](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 2/LAFROX-Subdocumento2.pdf>).
- **[SD3]:** [Alcance de la solución](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 3/LAFROX-Subdocumento3.pdf>).
- **[SD4]:** [Arquitectura lógica y física](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 4/LAFROX-Subdocumento4.pdf>).
- **[SD4-A]:** [Anexos de arquitectura](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 4/LAFROX-Subdocumento4-Anexos.pdf>).
- **[SD5]:** [Modelo y gestión de datos](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 5/LAFROX-Subdocumento5.pdf>).
- **[SD5-A]:** [Anexos del modelo de datos](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 5/LAFROX-Subdocumento5-Anexos.pdf>).
- **[SD6]:** [Metodologías del proyecto y software](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 6/LAFROX-Subdocumento6.pdf>).
- **[T9]:** [Metodología de gestión](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 6/LAFROX-Formulario-T-9.pdf>).
- **[T10]:** [Metodología de desarrollo](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 6/LAFROX-Formulario-T-10.pdf>).
- **[T14]:** [EDT, diccionario y Gantt](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 7/LafroX-Formulario-T-14.pdf>).
- **[T15]:** [Nivelación de recursos](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 7/LafroX-Formulario-T-15.pdf>).
- **[T18]:** [Implantación y puesta en marcha](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 7/LafroX-Formulario-T-18.pdf>).
- **[SD8]:** [Plan de riesgos](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 8/LafroX-Subdocumento8.pdf>).
- **[SD8-A]:** [Anexos de riesgos](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 8/LafroX-Subdocumento-8-Anexos.pdf>).
- **[T16]:** [Registro de riesgos](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 8/Lafrox-Formulario-T-16.pdf>).
- **[SD9]:** [Plan de calidad](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 9/LAFROX-Subdocumento9.pdf>).
- **[T13]:** [Plan de pruebas y validación](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 9/LAFROX-Formulario-T-13.pdf>).
- **[T17]:** [Protocolo de aceptación](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 9/LAFROX-Formulario-T-17.pdf>).
- **[SD13]:** [Innovaciones](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 13/LAFROX-Subdocumento13.pdf>).
- **[T19]:** [Fichas de innovación](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 13/LAFROX-Formulario-T-19.pdf>).
- **[BA]:** [Bases Administrativas](<C:/Users/henri/Downloads/Bases Caso/Bases Administrativas.pdf>).
- **[BTT]:** [Bases Técnicas Transversales](<C:/Users/henri/Downloads/Bases Caso/Bases Técnicas Transversales.pdf>).

## Key Learnings:

1. La posición 17 explica autoridad y trazabilidad de datos; el número visible 17 explica infraestructura de la EDT.
2. Las cifras solo son defendibles si se conserva su alcance: 205.007 HH de paquetes, 217.543 HH programadas y 4,4 horas de regresión automatizada son magnitudes diferentes.
3. Una meta propuesta, una referencia del caso y una evidencia de cumplimiento no son intercambiables.
