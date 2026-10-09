# FORMULACIÓN DE PROYECTOS

## BASES TÉCNICAS PARA LA PREPARACIÓN DE LA PROPUESTA

**Versión 1.0 — Fecha Documento: 18-08-2026**

---

# Bases Técnicas - Logística

**Distribuidora Puelche S.A. — trazabilidad, promesa de entrega y costo de servir en una distribuidora de consumo masivo**

| Campo | Detalle |
|---|---|
| **Asignatura** | Taller de Formulación de Proyectos Informáticos — ICI-5444 |
| **Unidad académica** | Escuela de Informática, Pontificia Universidad Católica de Valparaíso |
| **Profesor** | Antonio Moya Villegas — antonio.moya@pucv.cl |
| **Industria** | Logística — empresa distribuidora de consumo masivo |
| **Mandante** | Distribuidora Puelche S.A. (empresa ficticia) |
| **Operación** | Talca, Concepción y tres plataformas de cross-docking. 14.200 clientes entre O'Higgins y La Araucanía |
| **Documentos que rigen** | Bases Administrativas FEP01.26 y Bases Técnicas Transversales FEP02.26 |
| **Duración del contrato** | 56 meses: implementación en dos etapas y 36 meses de operación |
| **Versión** | 1.0 — agosto de 2026 |

> **Nota importante:** Este documento no es una especificación de requerimientos. Es la descripción de una operación real, con sus datos, sus dolores, sus contradicciones internas y sus vacíos.
> Identificar qué es funcional y qué no lo es, completar lo que falta con supuestos declarados y con reglas de negocio propias de la industria, investigar aquello que el documento no explica, y traducir todo ello en un alcance, una arquitectura, un plan y una estrategia de puesta en producción, es exactamente el trabajo que se está licitando y lo que será evaluado.

---

## CONTENIDO

| Título | Contenido | Capítulos |
|---|---|---|
| **I · El mandante y el encargo** | Cómo llegamos a esta licitación, la compañía, sus cifras y los lugares donde ocurre la operación. | 1 – 3 |
| **II · La operación tal como es hoy** | El ciclo del pedido de la preventa a la cobranza, los sistemas existentes, la conectividad y los indicadores del problema. | 4 – 7 |
| **III · Lo que dicen quienes operan** | Diez entrevistas de levantamiento, con sus contradicciones intactas. | 8 |
| **IV · Lo que el mandante espera** | Expectativas de negocio, restricciones no negociables, exclusiones, marco normativo y prioridades. | 9 – 13 |
| **V · Antecedentes para el dimensionamiento** | Volumetría entregada y volumetría a estimar, parámetros del caso y decisiones deliberadamente no resueltas. | 14 – 16 |
| **VI · Lo que debe producir el proponente** | El trabajo de traducción exigido, los criterios de aceptación y cómo se evaluará este caso. | 17 – 19 |
| **VII · Anexos del caso** | Mapa de sistemas y flujos actuales, perfil y calendario operacional, y glosario de la industria. | A – C |

### Cómo leer este documento

Los Títulos I y II describen la operación. Se entregan con detalle porque de ellos dependen todas las decisiones de diseño: no hay atajo que permita saltarlos.

El Título III recoge las voces de quienes operan. No están de acuerdo entre sí, y esa discrepancia es información, no ruido: revela dónde el proyecto va a encontrar resistencia y qué tensiones habrá que arbitrar.

El Título IV expresa lo que el mandante espera, deliberadamente en lenguaje de negocio y no de requerimientos. El Título V entrega los datos duros que la compañía conoce, señala cuáles debe estimar el proponente, fija los parámetros de los requisitos que las Bases Técnicas Transversales dejaron abiertos al caso, y enumera dieciséis decisiones que el cliente no ha tomado.

El Título VI describe el trabajo exigido y los criterios con que se juzgará. Conviene leerlo primero y volver a él al final.

> **Advertencia particular de este caso.**
> Buena parte de la operación no ocurre en instalaciones de la compañía, sino en la calle y en el local del cliente: 62 preventistas, unos 200 conductores, 14.200 puntos de entrega, rutas rurales sin cobertura y almacenes sin internet.
> El perfil de carga tampoco es plano: la preparación de pedidos es nocturna, el despacho se concentra en 90 minutos de la madrugada, y en septiembre el volumen casi se duplica durante tres semanas. Un dimensionamiento basado en el promedio diario estará equivocado.

---

# TÍTULO I — EL MANDANTE Y EL ENCARGO

## CAPÍTULO 1 · CÓMO LLEGAMOS A ESTA LICITACIÓN

El 3 de marzo de 2026, a las once y veinte de la mañana, sonó el teléfono de Katherine Ñanco Millán, jefa de calidad de Distribuidora Puelche. Era el gerente de aseguramiento de calidad de uno de los proveedores de lácteos más grandes del país. Habían detectado una desviación en un lote de queso fresco y estaban ejecutando un retiro preventivo. Necesitaban saber, ese mismo día, a qué clientes de Puelche había llegado el lote 24-0217.

Katherine tardó nueve días en responder.

Nueve días revisando guías de despacho en papel, cruzando fechas de recepción con fechas de despacho, llamando por teléfono a bodegueros y conductores, preguntándole a preventistas si se acordaban. Al final del ejercicio no pudo entregar una lista: entregó una estimación. Como la estimación no era suficiente, Puelche retiró de todos sus clientes el producto completo, no el lote. Fueron catorce mil doscientas llamadas, cuatro mil ochocientos kilos recuperados y una pérdida directa de treinta y un millones de pesos.

La autoridad sanitaria abrió un sumario. El proveedor, por su parte, envió una carta cortés informando que Puelche quedaba fuera de su lista de distribuidores autorizados por seis meses, «hasta que acredite capacidad de trazabilidad conforme a los estándares de la industria». Ese proveedor representaba el 6 % de las ventas.

Amparo Ossa Bulnes, gerenta general y tercera generación de la familia que fundó la empresa en 1974, convocó al comité ejecutivo la semana siguiente. No fue una reunión cómoda.

«Mi abuelo partió con un camión y una libreta», dijo Amparo. «Cincuenta y dos años después seguimos operando con una libreta. Es más grande, tiene más hojas y algunas están en Excel, pero es una libreta.»

Rubén Salinas Fuentealba, gerente comercial, agregó la segunda mala noticia del mes. La cadena de supermercados regional que es su cliente número uno —el 11 % de la venta— había enviado su carta de condiciones comerciales para el período 2029 en adelante: pedidos por vía electrónica exclusivamente, aviso de despacho anticipado, ventana de entrega de treinta minutos con penalización por incumplimiento y prueba de entrega digital. «Hoy nosotros entregamos entre las ocho y las seis de la tarde», dijo Rubén. «Cuando les preguntamos a qué hora llega el camión, la respuesta honesta es que no sabemos.»

Y había una tercera. Un distribuidor nacional había abierto operación en Talca ocho meses antes, con entrega en veinticuatro horas y una aplicación donde el almacenero hace su pedido solo, ve el stock y sabe a qué hora llega el camión. Puelche entrega en cuarenta y ocho a setenta y dos horas y toma el pedido con un preventista que pasa una vez por semana.

Nelson Quinteros Aravena, gerente de operaciones y logística, planteó el problema desde dentro. «El competidor no tiene mejores camiones que nosotros. Tiene mejor información. Yo despacho mil cuatrocientas entregas al día y no sé, hasta el día siguiente, cuántas llegaron completas y a tiempo. Cuando un cliente reclama que no le llegó, la guía firmada aparece tres semanas después, si aparece.»

Patricio Vergara Undurraga, gerente de administración y finanzas, cerró con la pregunta que nadie quería. «¿Cuánto nos cuesta atender a un almacén de Empedrado que nos compra cuarenta y cinco mil pesos cada dos semanas? No lo sabemos. Tenemos un prorrateo por zona que hicimos el 2016. Puede que estemos perdiendo plata en dos mil clientes y ganándola en tres mil, y estemos tomando decisiones comerciales a ciegas.»

El comité aprobó licitar el proyecto. Amparo dejó por escrito una condición en el acta: «no quiero un sistema que me obligue a cambiar la manera en que el almacenero de la esquina nos compra. Quiero un sistema que nos permita atenderlo mejor que nadie».

> Este documento es el resultado de siete meses de levantamiento en el centro de distribución, en las rutas y en los clientes, y de treinta y cuatro entrevistas.
> No es una especificación. Es la descripción, lo más honesta que el CLIENTE ha sido capaz de hacer, de una operación real con sus datos, sus dolores, sus contradicciones internas y sus vacíos. Traducir esto en requerimientos es el trabajo del PROPONENTE, y es precisamente lo que se evalúa.

---

## CAPÍTULO 2 · LA COMPAÑÍA

### 2.1 Identificación

| Antecedente | Detalle |
|---|---|
| **Razón social** | Distribuidora Puelche S.A. |
| **Giro** | Distribución mayorista de productos de consumo masivo: alimentos, bebidas, aseo del hogar y cuidado personal. |
| **Fundación** | 1974, en Talca, como empresa familiar. Actualmente en su tercera generación. |
| **Casa matriz** | Talca, Región del Maule, contigua al centro de distribución principal. |
| **Cobertura geográfica** | Desde la Región de O'Higgins hasta la Región de La Araucanía. |
| **Canales atendidos** | Canal tradicional (almacenes y minimarkets), food service (restaurantes, casinos, hoteles) y cadenas regionales de supermercados. |
| **Ventas anuales** | $ 148.000 millones. |
| **Propiedad** | Sociedad anónima cerrada, control familiar con 82 %; fondo de inversión regional con 18 %. |

### 2.2 Cifras de la operación

| Indicador | Valor |
|---|---|
| **Clientes activos** | 14.200 |
| **De ellos, canal tradicional** | 11.600 almacenes y minimarkets |
| **De ellos, food service** | 2.100 restaurantes, casinos y hoteles |
| **De ellos, cadenas y supermercados regionales** | 500 puntos de entrega |
| **SKU activos** | 8.400, de los cuales 1.100 son refrigerados o congelados |
| **Proveedores** | 180 |
| **Pedidos procesados al mes** | 31.000 |
| **Líneas de pedido al mes** | 260.000 |
| **Unidades despachadas al mes** | 2.4 millones |
| **Entregas en un día hábil normal** | ≈ 1.400 |
| **Entregas en un día hábil de peak de septiembre** | ≈ 2.600 |
| **Kilómetros recorridos al mes** | ≈ 420.000 |
| **Documentos tributarios emitidos al mes** | ≈ 34.000 |
| **Rotación de inventario** | 11,4 veces al año |
| **Participación de la venta al contado en el canal tradicional** | 38 % |

### 2.3 Instalaciones y flota

| Activo | Cantidad | Observación |
|---|---|---|
| **Centro de distribución Talca** | 18.000 m² | Bodega seca, cámara de refrigerado de 900 m², cámara de congelado de 400 m² a −22 °C, 14 andenes. Opera de lunes a viernes en tres turnos y el sábado hasta las 14:00. |
| **Centro de distribución Concepción** | 9.000 m² | Bodega seca y refrigerado. Sin congelado. Dos turnos. |
| **Plataformas de cross-docking** | 3 | Curicó, Chillán y Los Ángeles, entre 1.200 y 1.800 m² cada una. Sin almacenamiento: reciben en la madrugada y despachan en la mañana. |
| **Camiones propios** | 42 | De 4 a 18 toneladas. 18 con equipo de frío. Antigüedad promedio 6,2 años. |
| **Camiones de transportistas contratados** | 54 | De diez empresas distintas. 10 con equipo de frío. La empresa no controla ni los vehículos ni a sus conductores. |
| **Preventistas** | 62 | Recorren rutas fijas con visita semanal o quincenal según el cliente. |
| **Posiciones de almacenamiento en Talca** | 11.400 | Racks selectivos y piso. Ocupación promedio 87 %. |

### 2.4 Las personas

| Categoría | Dotación | Régimen |
|---|---|---|
| **Personal propio total** | 640 | Turnos según función. |
| **Personal de centro de distribución, todos los turnos** | 310 | Turno de noche de 22:00 a 06:00 para preparación de pedidos. Rotación anual del 38 % en preparación. |
| **Preventistas** | 62 | Jornada en terreno, de lunes a sábado. |
| **Conductores propios y peonetas** | 84 | Salida entre 05:30 y 07:00. Jornada sujeta al régimen especial de conductores. |
| **Conductores de transportistas contratados** | ≈ 160 | No son trabajadores de la compañía. Rotan sin aviso. |
| **Administración, comercial y soporte** | 184 | Jornada ordinaria en Talca y Concepción. |
| **Área de tecnologías de información** | 4 | Todos en Talca. |

---

## CAPÍTULO 3 · LOS LUGARES DONDE OCURRE LA OPERACIÓN

A diferencia de una faena o de una planta, en esta industria buena parte de la operación no ocurre en instalaciones de la compañía sino en la calle y en el local del cliente. El PROPONENTE deberá hacerse cargo de esa dispersión.

| Lugar | Qué ocurre allí | Condiciones relevantes |
|---|---|---|
| **Centro de distribución Talca** | Recepción de proveedores, almacenamiento, preparación de pedidos, consolidación y carga. | Operación en tres turnos. La preparación de pedidos es nocturna. Ambiente de bodega con montacargas en circulación. Cámara de congelado a −22 °C donde los dispositivos electrónicos comunes fallan y no hay cobertura de señal. |
| **Centro de distribución Concepción** | Igual que Talca, con menor escala y sin congelado. | Dos turnos. Depende del abastecimiento desde Talca para parte del surtido. |
| **Plataformas de cross-docking** | Recepción en la madrugada del camión de línea desde Talca, desconsolidación y despacho en la mañana. | Ventana de operación de tres horas. Sin almacenamiento. Personal reducido. Conectividad únicamente por red móvil. |
| **La calle: preventa** | Toma de pedidos en el local del cliente, negociación, gestión de cobranza y colocación de promociones. | 62 personas recorriendo cuatro regiones. Cobertura de red desigual. El preventista trabaja de pie, en la puerta del local, con el teléfono en una mano. |
| **La calle: reparto** | Transporte, entrega, descarga, gestión de devoluciones y cobro al contado. | Rutas urbanas densas y rutas rurales de hasta 240 km. Tramos sin cobertura de hasta dos horas. Lluvia, calor, perros y locales cerrados. |
| **El local del cliente** | Entrega física, verificación, firma, devolución y pago. | 14.200 puntos de entrega. La mayoría son almacenes de barrio sin conexión a internet, atendidos por su dueño o dueña, con espacio reducido para recibir. |
| **Oficinas** | Comercial, administración, finanzas, calidad y tecnologías de información. | Talca y Concepción. Jornada ordinaria. |

> La compañía construyó las plataformas de cross-docking en 2019 para reducir el tiempo de entrega en las zonas más alejadas. La reducción prometida fue de 24 horas y la efectivamente lograda es de 8. Nadie ha investigado por qué. La sospecha interna es que el tiempo se pierde en la consolidación en Talca, pero no hay datos que lo confirmen ni que lo desmientan.

---

# TÍTULO II — LA OPERACIÓN TAL COMO ES HOY

## CAPÍTULO 4 · EL CICLO DEL PEDIDO, DE LA PREVENTA A LA COBRANZA

Lo que sigue es la descripción del proceso tal como ocurre, no como debería ocurrir. Se entrega con este nivel de detalle porque de él dependen las decisiones de alcance, de arquitectura y de trazabilidad que el PROPONENTE deberá tomar.

### 4.1 Abastecimiento y recepción

El área de compras genera las órdenes de compra en el módulo correspondiente del sistema de gestión, a partir de una sugerencia de reposición que calcula una planilla que mantiene el jefe de abastecimiento. La planilla considera la venta de las últimas ocho semanas y un factor de ajuste manual por temporada. Las promociones no entran en el cálculo: se agregan a mano cuando comercial avisa, y comercial no siempre avisa.

Los proveedores confirman las órdenes por correo electrónico. Ninguno lo hace por vía electrónica estructurada. Los avisos de despacho, cuando existen, llegan también por correo, en documento adjunto, en formatos distintos según el proveedor.

El camión del proveedor llega al andén de recepción sin cita previa, salvo tres proveedores grandes que coordinan por teléfono. En temporada alta se forman filas de hasta cinco horas. El recepcionista cuenta la mercadería contra la guía en papel, revisa fechas de vencimiento por muestreo, anota el lote de los productos que lo requieren —cuando el producto lo trae visible— y firma. Después ingresa la recepción al sistema de gestión.

El registro del lote es el punto donde la trazabilidad se pierde por primera vez. Se anota en un campo de texto libre, cuando se anota. En el retiro sanitario de marzo, el 41 % de las recepciones del producto involucrado no tenía lote registrado.

### 4.2 Almacenamiento y control de inventario

El centro de distribución de Talca opera con un sistema de gestión de almacenes instalado en 2013 que controla ubicaciones y stock por posición. El de Concepción no lo usa: allí el control es por planilla. Las plataformas de cross-docking no tienen control de inventario porque, en teoría, no almacenan.

La asignación de ubicación a un producto nuevo la decide el jefe de bodega según su criterio. No existe una regla documentada de asignación por rotación, por peso o por compatibilidad. Los productos de alta rotación quedaron ubicados donde estaban cuando se instaló el sistema, hace trece años, y la rotación cambió.

El conteo cíclico se realiza sobre 3.400 posiciones al mes, en el turno de noche, con planillas impresas. La diferencia promedio es de 2,3 % del valor contado. Las diferencias se ajustan al cierre del mes sin investigación de causa, salvo cuando superan un umbral que nadie ha escrito pero que todos conocen.

### 4.3 Preventa

Sesenta y dos preventistas recorren rutas fijas. Cada cliente recibe visita semanal o quincenal según su clasificación. El preventista lleva un teléfono con una aplicación que la compañía compró en 2016 a un proveedor que ya no existe: no tiene soporte, no se puede modificar y funciona sobre una versión de sistema operativo que los teléfonos nuevos ya no traen.

La aplicación muestra el catálogo y los precios, y permite registrar el pedido. No muestra el stock disponible, no muestra el crédito disponible del cliente ni su deuda vencida, y no muestra el historial de compra. El preventista trabaja con esa información en la cabeza o en un cuaderno.

Cuando no hay señal —lo que ocurre en buena parte de las rutas rurales— la aplicación guarda el pedido y lo envía al recuperar cobertura. En ocasiones no lo envía. En ocasiones lo envía dos veces. Nadie ha medido con qué frecuencia ocurre cada cosa, pero el equipo comercial estima que «pasa todas las semanas».

El pedido llega al sistema de gestión, donde se valida el crédito del cliente. Si el cliente está bloqueado, el pedido queda retenido y alguien de crédito y cobranza lo revisa al día siguiente. El preventista se entera cuando el cliente lo llama para preguntar por qué no llegó su pedido.

### 4.4 Planificación de rutas

Todas las tardes, entre las 15:00 y las 18:30, Hugo Maldonado Sepúlveda arma las rutas del día siguiente. Toma el listado de pedidos confirmados, lo abre en una planilla de cálculo, y distribuye las entregas entre los camiones disponibles considerando la zona, el peso, el volumen, si el pedido requiere frío, las ventanas horarias que conoce de memoria y los caminos que sabe que están malos.

Don Hugo lleva veintiún años haciéndolo. Su planilla tiene once hojas y nadie más la entiende. Cuando él se toma vacaciones, las rutas las arma su ayudante y el cumplimiento de entrega cae entre seis y nueve puntos porcentuales durante esa semana. Le quedan dos años para jubilarse.

La ocupación promedio de los camiones es del 68 % en volumen. Hay días en que un camión sale con 41 %. Nadie mide el costo de esa ineficiencia porque nadie mide el costo del viaje.

### 4.5 Preparación de pedidos y carga

La preparación se realiza en el turno de noche, entre las 22:00 y las 06:00. El preparador recibe una hoja de picking impresa, ordenada por ubicación, y recorre la bodega con un transpaleta armando el pedido en pallets o canastillos. Marca con lápiz lo que va tomando.

Lo que no encuentra o no alcanza queda como faltante y se anota a mano al pie de la hoja. La hoja vuelve a la oficina de bodega, donde alguien digita los faltantes en el sistema para que la facturación se ajuste. Ese es el segundo punto donde se pierde información: el faltante se registra, pero no la causa del faltante.

Los productos refrigerados y congelados se preparan al final del turno para minimizar el tiempo fuera de cámara. En la cámara de congelado, a veintidós grados bajo cero, el preparador trabaja con guantes térmicos y en turnos de treinta minutos. Los dispositivos electrónicos convencionales no operan de forma confiable a esa temperatura y dentro de la cámara no hay cobertura de señal.

La carga se hace por orden de ruta invertido, para que la primera entrega quede accesible. Ese ordenamiento depende de que el cargador sepa la secuencia de la ruta, que está en la planilla de don Hugo.

### 4.6 Transporte y entrega

El camión sale entre las 05:30 y las 07:00 con las guías de despacho impresas y, cuando corresponde, un termógrafo manual que el conductor debe leer y anotar tres veces durante el viaje.

En el local del cliente, el conductor y el peoneta descargan, el cliente revisa, y firma la guía en papel. Si el cliente rechaza un producto —por daño, por fecha de vencimiento próxima o porque no lo pidió— el conductor lo anota en la guía y se lo lleva de vuelta. Si el cliente paga al contado, el conductor recibe el efectivo, lo anota y lo guarda.

Si el local está cerrado, el conductor decide. A veces vuelve más tarde, a veces deja el pedido con el negocio de al lado, a veces se lo lleva de vuelta. No hay una regla escrita y cada conductor hace lo que le parece razonable.

Al regresar, el conductor entrega el fajo de guías firmadas en la oficina. Esas guías se archivan. El 1,1 % mensual no llega, se moja, se pierde o queda ilegible. Cuando un cliente reclama que no recibió un pedido, encontrar su guía toma en promedio doce días.

### 4.7 Cobranza y rendición

El 38 % de las ventas del canal tradicional se cobra en efectivo contra entrega. El conductor rinde a la mañana siguiente en caja, contando el dinero contra el listado de sus entregas del día anterior.

Las diferencias de rendición promedian cuatro millones doscientos mil pesos mensuales entre toda la flota. Se resuelven, en palabras del jefe de tesorería, «conversando». Nadie ha investigado si son errores de conteo, cobros que no se hicieron, descuentos que el conductor otorgó por su cuenta o pérdidas.

El resto de la venta se factura a treinta días. La cobranza la gestiona un equipo de cinco personas por teléfono, con un listado que se genera del sistema de gestión cada lunes.

### 4.8 Devoluciones, mermas y envases retornables

Las devoluciones equivalen al 2,9 % del volumen despachado. Vuelven al centro de distribución en el mismo camión, se reciben en un andén distinto, se revisan y se decide su destino: reingreso a stock, venta con descuento, devolución al proveedor o destrucción. Esa decisión la toma el jefe de bodega producto por producto y no queda registrada de forma estructurada.

La merma por vencimiento equivale al 1,7 % del valor del inventario al año. Se detecta en el conteo cíclico, en la preparación de pedidos o —lo que es peor— en la góndola del cliente, cuando el preventista encuentra producto vencido que Puelche despachó.

La compañía tiene en circulación un parque estimado de sesenta y ocho mil canastillos plásticos y nueve mil cuatrocientos pallets. La palabra «estimado» es literal: no hay control individual. La pérdida anual estimada es del 14 % del parque. Cuando un cliente devuelve canastillos, el conductor los anota en un cuaderno.

### 4.9 Cadena de frío y calidad

Los mil cien productos refrigerados y congelados están sujetos a las exigencias sanitarias correspondientes. La temperatura se controla con termómetros en las cámaras del centro de distribución, con lectura manual dos veces por turno anotada en una planilla, y con termógrafos manuales en los camiones con equipo de frío, con tres lecturas por viaje anotadas por el conductor.

No existe registro continuo ni automático de temperatura en ningún punto de la cadena. La autoridad sanitaria observó esa ausencia en su última fiscalización. El año pasado un cliente de food service rechazó un camión completo por sospecha de ruptura de cadena de frío; Puelche no pudo demostrar lo contrario y asumió la pérdida de veintiún millones de pesos.

La trazabilidad de lote existe en el papel de la recepción y en la memoria de quienes despacharon. No existe en ningún sistema en forma consultable. Eso es lo que produjo los nueve días del Capítulo 1.

---

## CAPÍTULO 5 · LOS SISTEMAS QUE EXISTEN HOY

El PROPONENTE deberá integrarse a este panorama. La columna de destino indica la decisión ya tomada por el CLIENTE respecto de cada sistema; donde dice «decisión del proponente», la decisión no está tomada y debe fundamentarse en la propuesta.

| Sistema | Función | Destino |
|---|---|---|
| **Sistema de gestión empresarial, implantado en 2017** | Ventas, facturación, cuentas por cobrar y por pagar, contabilidad, compras, inventario valorizado y remuneraciones. | Se mantiene. Es el sistema de registro contable y tributario. La solución le entrega datos; no lo reemplaza ni lo modifica. |
| **Facturación electrónica y documentos tributarios** | Emisión de facturas, guías de despacho electrónicas y notas de crédito ante la autoridad tributaria. | Se mantiene, integrada al sistema de gestión. La solución no emite documentos tributarios por su cuenta. |
| **Sistema de gestión de almacenes de 2013** | Control de ubicaciones y de stock por posición, sólo en el centro de distribución de Talca. | Decisión del PROPONENTE: puede mantenerse e integrarse, extenderse a los demás sitios, o reemplazarse. Cualquiera sea la decisión, debe justificarse técnica y económicamente. |
| **Aplicación de preventa de 2016** | Catálogo, precios y toma de pedido en terreno. | Se reemplaza. El proveedor desapareció, no tiene soporte y no es compatible con los dispositivos actuales. |
| **Planilla de planificación de rutas** | Asignación diaria de entregas a camiones y secuenciamiento. | Se reemplaza. Su conocimiento reside en una persona que se jubila en dos años. |
| **Planilla de sugerencia de reposición** | Cálculo de la necesidad de compra por producto. | Se reemplaza. |
| **Telemetría de flota** | Posición y velocidad de los 42 camiones propios, provista por un tercero con su propia plataforma. | Se mantiene como fuente. Debe integrarse. Los 54 camiones de transportistas no están cubiertos. |
| **Planillas y cuadernos** | Recepción de lotes, conteo cíclico, faltantes, devoluciones, envases retornables, temperatura, rendición de efectivo, costo por zona. | Deben desaparecer como sistema de registro. Ese es, en buena medida, el objeto de esta licitación. |

> El CLIENTE no dispone de documentación técnica de las interfaces del sistema de gestión ni del sistema de gestión de almacenes. Tampoco tiene claridad sobre las condiciones contractuales de acceso a los datos de la plataforma de telemetría. Levantar esa información es parte del trabajo del ADJUDICATARIO durante los primeros meses, y el riesgo asociado debe estar reflejado en la propuesta.

---

## CAPÍTULO 6 · CONECTIVIDAD Y CONDICIONES DEL SITIO

| Elemento | Situación actual |
|---|---|
| **Centro de distribución Talca** | Fibra óptica de un proveedor con respaldo por red móvil de capacidad reducida. Cuatro cortes al año en promedio, de hasta seis horas. Durante el corte la bodega sigue trabajando en papel y la información se ingresa después. |
| **Centro de distribución Concepción** | Fibra óptica de un proveedor, sin respaldo. Un corte deja el sitio incomunicado. |
| **Plataformas de cross-docking** | Conectividad exclusivamente por red móvil. En Los Ángeles la señal es intermitente en la madrugada, que es justamente su ventana de operación. |
| **Cámaras de refrigerado y congelado** | Sin cobertura de señal en el interior. La estructura metálica y aislante bloquea la red móvil y la red inalámbrica de la bodega no penetra. |
| **Rutas urbanas** | Cobertura móvil buena en Talca, Curicó, Chillán, Concepción y Los Ángeles. |
| **Rutas rurales** | Cobertura deficiente o nula en tramos de las rutas de Empedrado, Chanco, Cauquenes, Pinto y Alto Biobío. Se registran tramos sin señal de hasta dos horas continuas, y rutas completas donde el conductor recupera cobertura sólo al regresar. |
| **Locales de los clientes** | La mayoría de los almacenes del canal tradicional no tiene conexión a internet ni dispositivo propio disponible para la entrega. |
| **Sala de servidores de Talca** | Recinto de 25 metros cuadrados dentro del edificio de oficinas, con aire acondicionado tipo split, alimentación ininterrumpida de 10 minutos y acceso por llave. No cumple los estándares del Capítulo 6 de las Bases Técnicas Transversales. |
| **Condiciones del trabajo en terreno** | El preventista opera de pie en la puerta del local, con lluvia en invierno y sobre 34 °C en verano. El conductor y el peoneta manipulan carga; el dispositivo debe poder usarse con una sola mano. |

> **La compañía ha sido explícita en dos puntos. Primero: el centro de distribución debe poder recibir, preparar y despachar aunque se corte el enlace. Segundo: la aplicación del repartidor y la del preventista deben funcionar un turno completo sin señal, porque hay rutas donde eso ocurre todos los días.**

---

## CAPÍTULO 7 · LO QUE DUELE: INDICADORES DEL PROBLEMA

Los siguientes datos corresponden al ejercicio 2025 y provienen de los registros de la compañía. Se entregan porque dimensionan el problema y porque el PROPONENTE deberá comprometer mejoras verificables sobre ellos.

### 7.1 Servicio al cliente

| Indicador | Valor 2025 | Referencia |
|---|---|---|
| **Entregas completas y a tiempo (OTIF)** | 82,4 % | sobre 95 % |
| **Cumplimiento de lo pedido (fill rate)** | 91,3 % | sobre 97 % |
| **Quiebre de stock detectado en el momento de la preventa** | 7,8 % de las líneas | bajo 2 % |
| **Reentregas sobre el total de entregas** | 4,2 % | bajo 1 % |
| **Plazo de entrega desde la toma del pedido** | 48 a 72 horas | 24 horas (competencia) |
| **Ventana de entrega comprometida al cliente** | entre 08:00 y 18:00 | 30 minutos (exigencia 2029) |
| **Guías de despacho extraviadas o ilegibles** | 1,1 % mensual | cero |
| **Días para resolver un reclamo de entrega no recibida** | 12 | mismo día |

### 7.2 Operación y costo

| Indicador | Valor 2025 |
|---|---|
| **Tiempo diario dedicado a armar la ruta del día siguiente** | 3,5 horas de una persona |
| **Caída del cumplimiento de entrega cuando el planificador está ausente** | 6 a 9 puntos porcentuales |
| **Ocupación promedio del camión en volumen** | 68 %, con días de 41 % |
| **Tiempo promedio de descarga en el local del cliente** | 22 minutos, con casos de 70 |
| **Diferencia del conteo cíclico de inventario** | 2,3 % del valor contado |
| **Merma por vencimiento** | 1,7 % del valor del inventario al año |
| **Devoluciones sobre el volumen despachado** | 2,9 % |
| **Rotación anual del personal de preparación de pedidos** | 38 % |
| **Diferencias mensuales de rendición de efectivo** | $ 4,2 millones |
| **Pérdida anual estimada del parque de envases retornables** | 14 % |
| **Costo de servir por cliente** | desconocido; se prorratea por zona con un criterio de 2016 |
| **Reducción de plazo prometida por las plataformas de cross-docking** | 24 horas prometidas, 8 logradas |

### 7.3 Calidad, trazabilidad y cumplimiento

| Indicador | Valor 2025 |
|---|---|
| **Días para identificar a los clientes afectados por un retiro sanitario** | 9, con resultado estimado |
| **Recepciones del producto involucrado sin registro de lote** | 41 % |
| **Pérdida directa del retiro sanitario de marzo de 2026** | $ 31 millones |
| **Suspensión comercial impuesta por el proveedor afectado** | 6 meses, sobre el 6 % de las ventas |
| **Registro continuo de temperatura en la cadena** | inexistente |
| **Lecturas de temperatura por viaje** | 3, manuales, anotadas por el conductor |
| **Rechazo de camión completo por sospecha de ruptura de cadena de frío** | 1 evento, $ 21 millones |
| **Observaciones de la autoridad sanitaria en la última fiscalización** | por ausencia de registro continuo de temperatura |
| **Pedidos recibidos por vía electrónica estructurada** | cero |
| **Proveedores que confirman órdenes por vía electrónica estructurada** | cero de 180 |

> Ninguno de estos indicadores se resuelve comprando software. Se resuelven capturando el dato donde ocurre el hecho —en el andén, en la góndola, en la puerta del local, en la cabina del camión— y asegurando que ese dato viaje sin transformarse a mano. El PROPONENTE que entienda esto y lo demuestre en su propuesta tendrá una ventaja evidente sobre quien ofrezca módulos.

---

# TÍTULO III — LO QUE DICEN QUIENES OPERAN

## CAPÍTULO 8 · ENTREVISTAS DE LEVANTAMIENTO

Las siguientes son transcripciones editadas de las entrevistas de levantamiento sostenidas entre septiembre de 2025 y febrero de 2026. Se entregan con sus contradicciones intactas, porque las contradicciones son parte del problema.

El PROPONENTE debe leerlas como lo que son: la palabra de personas que conocen muy bien su parte de la operación y que no tienen por qué conocer la de los demás, ni tienen por qué saber de sistemas. Distinguir el hecho de la opinión, la necesidad del capricho y el problema de la solución que la persona ya se imaginó es parte del trabajo profesional que se está licitando.

---

### Amparo Ossa Bulnes · Gerenta General

Nosotros no vendemos productos, vendemos confianza. El almacenero de Chanco nos compra porque sabe que el jueves llega el camión. Cuando no llega, no pierde una venta: pierde la confianza, y esa no vuelve fácil.

El competidor que entró el año pasado no tiene mejores camiones ni mejores precios. Tiene una aplicación donde el almacenero pide solo, a la hora que quiere, ve el stock y sabe cuándo le llega. Eso es todo lo que tiene, y con eso me está sacando clientes.

El retiro sanitario de marzo fue humillante. No por la plata, que la plata se recupera. Fue porque un proveedor me dijo, por escrito, que no tengo capacidad de trazabilidad. Y tenía razón.

Lo que le pido a quien gane esta licitación es una cosa: no me cambie al cliente. El almacenero de barrio compra como compra, paga en efectivo, no tiene internet ni un teléfono decente. Si su solución supone que el cliente va a cambiar, su solución no sirve. Yo quiero atenderlo mejor, no reemplazarlo por otro tipo de cliente.

Y le voy a decir algo que a lo mejor no debería. Esta empresa es familiar y aquí la gente lleva veinte, treinta años. Si el proyecto los pasa por encima, ellos lo van a hundir sin decir una palabra. Lo he visto antes.

---

### Nelson Quinteros Aravena · Gerente de Operaciones y Logística

Mi indicador principal es el OTIF y está en ochenta y dos coma cuatro. Debería estar sobre noventa y cinco. El problema es que cuando pregunto por qué falló una entrega, tengo cuatro respuestas distintas según a quién le pregunte.

Comercial dice que la bodega no despachó. La bodega dice que el producto no estaba. Compras dice que sí llegó pero tres días después. Y el conductor dice que el local estaba cerrado. Todas pueden ser ciertas y no tengo cómo saber cuál lo es.

Yo despacho mil cuatrocientas entregas al día y me entero de cómo me fue al día siguiente en la mañana, cuando llegan las guías. Un día completo a ciegas. En septiembre, con dos mil seiscientas entregas diarias, son dos días a ciegas porque las guías se acumulan.

El tema de las plataformas de cross-dock me tiene incómodo. Las construimos el 2019 para bajar veinticuatro horas el plazo de entrega y bajamos ocho. Nadie ha investigado por qué. Yo sospecho que el tiempo se pierde en la consolidación en Talca, pero es una sospecha.

Una advertencia: no me toquen el despacho de la mañana. Entre las cinco y media y las siete salen noventa y seis camiones. Si el sistema se cae en esa ventana, ese día no hay operación. No hay plan B, no existe forma de hacerlo a mano en dos horas.

---

### Hugo Maldonado Sepúlveda · Planificador de rutas, 21 años en la empresa

Yo armo las rutas todas las tardes. Me demoro tres horas y media, a veces cuatro cuando hay mucho pedido. Tengo una planilla que hice yo, tiene once hojas, y la verdad es que no sé si alguien más la entiende.

Me dicen que van a poner un software que arma las rutas solo. Yo he visto esos software. El problema es que el software no sabe que en el camino a Pelluhue hay un puente que no aguanta el camión grande. No sabe que a la señora del almacén de Villa Alegre hay que llegarle antes de las once porque después se va a buscar a los nietos. No sabe que el cliente de Longaví no recibe si va el conductor nuevo porque una vez le rompieron una caja.

Todo eso lo tengo en la cabeza. Son veintiún años. Y sí, entiendo que eso es un problema, no me lo tienen que explicar. Me jubilo en dos años.

Si me preguntan qué necesito, le digo: que el sistema me proponga y yo pueda corregir. No que me imponga. Si me impone, va a mandar el camión al puente y después la culpa va a ser mía.

Ah, y necesito que alguien me diga cuánto pesa y cuánto ocupa cada producto. Hoy lo estimo. Hay productos que llevo veinte años estimando mal, seguro.

---

### Ximena Bravo Cortés · Jefa de Bodega, Centro de Distribución Talca

Mi turno crítico es el de noche. De diez a seis de la mañana preparamos todos los pedidos del día siguiente. Son ciento veinte personas y la rotación es del treinta y ocho por ciento al año. Cada mes tengo gente nueva que no sabe dónde está nada.

El picking es con hoja impresa y lápiz. Sé que suena antiguo. También sé que si mañana me ponen un aparato en la mano de una persona que entró hace tres días, en el turno de noche, me van a bajar la productividad un cuarenta por ciento la primera semana. Eso hay que planificarlo bien.

Lo que más me duele son los faltantes. El preparador anota al pie de la hoja lo que no encontró, la hoja va a la oficina y alguien lo digita. Pero nunca anotamos por qué faltó. ¿No había? ¿Estaba mal ubicado? ¿Se lo llevó otro pedido? Sin eso no puedo mejorar nada.

La cámara de congelado es un mundo aparte. Menos veintidós grados. La gente entra media hora y sale. Los teléfonos se apagan solos, las pantallas no responden y adentro no hay señal de nada. Cualquier cosa que diseñen para la bodega tiene que funcionar ahí adentro también, y le adelanto que ahí es donde los proveedores se caen.

Y la ubicación de los productos está mal. Se definió cuando se instaló el sistema el 2013 y la rotación cambió completamente. Hoy tengo productos de alta rotación en el fondo del pasillo doce. Nadie ha querido reordenar la bodega porque hay que parar.

---

### Rubén Salinas Fuentealba · Gerente Comercial

Mis sesenta y dos preventistas están trabajando con una aplicación de hace diez años que compramos a una empresa que ya no existe. No muestra el stock. Entonces el preventista le vende al cliente algo que no hay, el cliente espera, no le llega, y el que queda mal es el preventista.

Tampoco muestra la deuda del cliente. El preventista le toma el pedido, el pedido llega bloqueado por crédito, se queda dos días detenido y nadie le avisa a nadie. El cliente se entera cuando llama enojado.

Yo quiero prometerle al cliente entrega en veinticuatro horas, como el competidor. Operaciones me dice que es imposible. Puede ser, pero entonces alguien me tiene que decir en cuánto sí podemos, para yo prometer eso y cumplirlo. Prometer cuarenta y ocho y entregar en setenta y dos es lo peor de los dos mundos.

Del canal moderno: la cadena grande nos mandó su carta de condiciones. Pedidos electrónicos, aviso de despacho, ventana de treinta minutos, prueba de entrega digital. Si en 2029 no cumplimos eso, perdemos el once por ciento de la venta de un día para otro.

Y quiero decir algo del efectivo, porque sé que finanzas lo quiere eliminar. El treinta y ocho por ciento del canal tradicional paga en efectivo porque no tiene otra forma. Si mañana les decimos que no recibimos efectivo, perdemos tres mil clientes. Esa conversación hay que tenerla con cuidado.

---

### Katherine Ñanco Millán · Jefa de Calidad y Aseguramiento

Los nueve días del retiro sanitario los viví yo. Nueve días buscando en carpetas, llamando conductores, preguntándole a la gente si se acordaba. Al final entregué una estimación, y una estimación no sirve para un retiro.

El problema empieza en la recepción. El lote se anota en un campo de texto libre, cuando se anota. En el producto que nos tocó, el cuarenta y uno por ciento de las recepciones no tenía lote. Y si no lo tengo en la entrada, no lo puedo tener en la salida.

De la cadena de frío: hoy tomamos tres lecturas por viaje, a mano, anotadas por el conductor. No tengo registro continuo en ninguna parte. La autoridad ya nos observó por eso. Y cuando un cliente rechazó el camión completo el año pasado, yo no pude demostrar que la temperatura estuvo bien, porque no tenía cómo.

Yo quiero registro continuo y quiero que el sistema bloquee el despacho si hubo una excursión de temperatura fuera de rango. Sé que operaciones va a pelear conmigo por esto.

Y hay algo que nadie ha definido y que a mí me quita el sueño: qué es exactamente una excursión que invalida el producto. Dos grados por diez minutos, ¿es una excursión? ¿Y por cuarenta minutos? Alguien tiene que escribir esa regla y hoy no está escrita en ninguna parte.

---

### Patricio Vergara Undurraga · Gerente de Administración y Finanzas

Cuatro millones doscientos mil pesos de diferencia de rendición al mes. Eso es lo que se pierde entre lo que los conductores debieron traer y lo que trajeron. Se resuelve conversando, que es la manera educada de decir que no lo investigamos.

No estoy acusando a nadie. Puede ser error de conteo, puede ser un descuento que el conductor dio de buena fe, puede ser un cobro que no se hizo. El punto es que no sé, y no saber es lo que me molesta.

El costo de servir es mi obsesión. Yo prorrateó el costo logístico por zona con un criterio que hicimos el 2016. Con eso decidimos precios y decidimos a quién atender. Es perfectamente posible que estemos perdiendo plata en dos mil clientes y ni siquiera lo sepamos.

Quiero saber cuánto cuesta cada entrega: el kilómetro, el tiempo de descarga, el tamaño del pedido, la frecuencia de visita, la reentrega si la hubo. Con eso puedo tomar decisiones. Sin eso estoy adivinando.

Una advertencia sobre el presupuesto: yo voy a mirar la operación, no la implementación. Un sistema barato de instalar y caro de operar por tres años es peor negocio. Quiero el costo total, mes a mes, hasta el final del contrato. Y todo lo tributario sale del sistema de gestión: no quiero dos verdades ni un segundo emisor de documentos.

---

### Jonathan Curihual Paillán · Conductor repartidor, ruta Cauquenes, 11 años

Mi ruta son doscientos cuarenta kilómetros y treinta y cuatro clientes. Salgo a las seis y llego de vuelta a las siete de la tarde si me va bien.

Desde que paso Villa Alegre hasta que vuelvo, no tengo señal. Nada. Dos horas sin señal fácil, y en invierno más porque el camino se pone malo y me demoro. Si el aparato que me van a dar necesita internet, no me sirve.

Las guías las llevo en un fajo. Se mojan, se arrugan, se me caen. Yo las cuido, pero llueve. Después en la oficina me dicen que falta una y yo tengo que acordarme de quién firmó qué hace tres semanas.

El efectivo es lo que más me preocupa. Ando con un millón, un millón y medio en la cabina algunos días. En Cauquenes ya asaltaron a un colega de otra empresa. Yo entiendo que el cliente paga así, pero uno anda nervioso.

Y cuando el local está cerrado, uno hace lo que puede. A veces vuelvo en la tarde, a veces se lo dejo al vecino que lo conozco hace años, a veces me lo traigo. Nadie me dijo nunca qué es lo correcto. Yo hago lo que creo que es mejor para el cliente.

Una cosa más: yo descargo. Con las dos manos. Si me dan un aparato que hay que tener en una mano y apretar con la otra, no lo voy a usar en la puerta del local con el peoneta esperando.

---

### Sandra Riffo Alarcón · Preventista, canal tradicional, zona Curicó

Yo visito cuarenta y dos clientes al día. Almacenes chicos, la mayoría. Con muchos llevo años y ya sé lo que compran.

Lo que me mata es no saber si hay stock. Le ofrezco al cliente, se entusiasma, hace el pedido, y a los dos días me llama para retarme porque no le llegó la mitad. Yo quedo como mentirosa y no fue culpa mía.

Tampoco sé si el cliente está bloqueado por deuda. Le tomo el pedido feliz y después el pedido queda parado en crédito. Me entero cuando el cliente reclama.

La aplicación se cae. En el campo se cae más. A veces tomo el pedido, lo guardo, y cuando llego a la casa veo que no se mandó. Otras veces se manda dos veces y llegan dos pedidos iguales. Ya aprendí a revisar, pero no debería tener que revisar.

Yo también cobro. Muchos clientes me pagan a mí la factura de la semana pasada. Yo lo anoto en un cuaderno y lo entrego el viernes. Es plata que ando trayendo toda la semana.

Y algo que nadie pregunta: yo veo la góndola del cliente. Veo cuando tiene producto nuestro vencido, veo cuando el competidor le puso un exhibidor, veo cuando está por cerrar. Eso no lo anoto en ninguna parte porque no hay dónde.

---

### Eduardo Kaufmann Vial · Jefe de Tecnologías de Información

Somos cuatro personas para toda la empresa. Cuatro. Yo, dos de soporte y una analista. Con eso mantenemos el sistema de gestión, la red de cinco instalaciones, los computadores, los teléfonos y lo que se caiga.

Si el sistema que ustedes propongan necesita un administrador dedicado, díganlo ahora y cotícenlo, porque no lo tengo y no me lo van a aprobar.

Mi posición es nube, por lo mismo. No quiero más servidores acá. La sala que tenemos son veinticinco metros cuadrados con un aire acondicionado de pared y una UPS que da diez minutos. Es un riesgo.

Pero acá viene el problema y lo digo yo mismo antes de que me lo digan: si se corta la fibra a las cinco de la mañana, no salen los camiones. Y se corta cuatro veces al año. Concepción no tiene ni respaldo. Los cross-dock funcionan solo con red móvil y en Los Ángeles la señal falla justo en la madrugada, que es cuando operan.

Sobre integraciones: el sistema de gestión lo implantamos el 2017 con un partner que ya no trabaja con nosotros. No tengo la documentación de las interfaces. Sé que existen porque las usamos, pero no sé cuáles ni cómo. Eso alguien lo va a tener que levantar.

Y de seguridad: manejamos datos de catorce mil doscientos clientes, con sus datos comerciales y su comportamiento de pago. Y desde que hay GPS en los camiones, manejamos ubicación de personas. Eso me preocupa y no sé si lo estamos haciendo bien.

---

> **Sobre las contradicciones.**
> El PROPONENTE habrá advertido que estas entrevistas no son consistentes entre sí. El gerente comercial quiere prometer entrega en 24 horas y el gerente de operaciones dice que es imposible. La jefa de calidad quiere bloquear el despacho ante una excursión de temperatura y el gerente de operaciones no puede permitirse que se caiga el día. El gerente de finanzas quiere eliminar el efectivo y el gerente comercial dice que eso costaría tres mil clientes. El jefe de tecnologías quiere todo en la nube y él mismo explica por qué la operación no puede depender de ella. El planificador de rutas desconfía del software que su gerente ya dio por hecho.
> Estas tensiones son reales y no se resolverán antes de la adjudicación. Resolverlas —o, cuando no sea posible, proponer una arquitectura que permita convivir con ellas y dejar constancia de la decisión y de su costo— es parte de lo que se está licitando.

---

# TÍTULO IV — LO QUE EL MANDANTE ESPERA

## CAPÍTULO 9 · EXPECTATIVAS DE NEGOCIO

Las siguientes son las expectativas del CLIENTE expresadas como resultados de negocio. Deliberadamente no están escritas como requerimientos. Traducirlas en requerimientos funcionales y no funcionales, priorizarlos, asignarlos a una etapa y hacerlos verificables es trabajo del PROPONENTE.

### 9.1 Cumplir lo que se promete y saberlo el mismo día

El CLIENTE espera comprometer una promesa de entrega concreta —fecha y franja horaria— y cumplirla; y espera saber al final de cada jornada, no al día siguiente, cuántas entregas se cumplieron, cuáles no y por qué. Espera además que todas las áreas midan lo mismo de la misma manera, cosa que hoy no ocurre.

### 9.2 Que el preventista venda con información real

El CLIENTE espera que quien está frente al cliente sepa qué hay disponible, cuánto crédito tiene ese cliente, qué compró antes y qué le conviene ofrecerle. Y espera que el pedido llegue una sola vez, completo, aunque se haya tomado en un lugar sin señal.

### 9.3 Sacar la ruta de la cabeza de una persona

El CLIENTE espera que la planificación diaria de rutas deje de depender del conocimiento acumulado de un individuo, sin perder ese conocimiento. Espera que el sistema proponga y que la persona pueda corregir, y que cada corrección enseñe algo al sistema.

Espera, además, entender por primera vez cuánto cuesta cada viaje y cada entrega.

### 9.4 Que la entrega deje huella digital

El CLIENTE espera terminar con la guía de papel: que la entrega quede registrada en el momento y en el lugar, con la evidencia que corresponda, disponible para el cliente y para la propia empresa de inmediato. Y espera que las diferencias entre lo pedido, lo despachado y lo recibido queden explicadas y no descubiertas tres semanas después.

### 9.5 Responder un retiro sanitario en horas

El CLIENTE espera poder tomar un lote de un proveedor y saber, con evidencia y no con estimación, a qué clientes llegó, en qué fecha, en qué cantidad y con qué documento. Y espera poder recorrer esa cadena también en sentido inverso, desde una unidad en el local del cliente hasta la recepción que la originó.

Esta expectativa no es sólo sanitaria: es la condición que un proveedor ya le impuso por escrito para seguir trabajando con él.

### 9.6 Demostrar la cadena de frío

El CLIENTE espera contar con registro continuo y automático de temperatura en cámaras y en vehículos, con alerta oportuna cuando algo se sale de rango, con evidencia disponible ante la autoridad y ante el cliente, y con una regla escrita —hoy inexistente— que defina cuándo una excursión invalida el producto y quién decide.

### 9.7 Controlar el dinero y los activos que hoy circulan sin control

El CLIENTE espera que el efectivo cobrado en la calle se registre en el momento del cobro y que la rendición cuadre el mismo día. Espera lo mismo respecto de los envases retornables: saber cuántos hay, dónde están y quién los tiene.

El CLIENTE no ha decidido si quiere eliminar el efectivo, reducirlo o simplemente controlarlo. Espera que el PROPONENTE le proponga un camino y le muestre sus consecuencias.

### 9.8 Saber cuánto cuesta atender a cada cliente

El CLIENTE espera conocer el costo de servir por cliente y por entrega, construido desde el hecho —kilómetro recorrido, tiempo de descarga, tamaño del pedido, frecuencia de visita, reentregas— y no desde un prorrateo. Espera usar ese dato para decidir frecuencias de visita, pedidos mínimos y política comercial.

### 9.9 Estar en condiciones de atender al canal moderno

El CLIENTE espera poder recibir pedidos por vía electrónica estructurada, enviar avisos de despacho anticipados, cumplir ventanas horarias estrechas y entregar prueba de entrega digital, porque su principal cliente lo exigirá desde 2029 y porque el resto del canal moderno seguirá el mismo camino.

### 9.10 Comprar mejor

El CLIENTE espera que la sugerencia de reposición considere la venta real, la estacionalidad, las promociones comprometidas y el plazo de cada proveedor, y que deje de depender de una planilla y de que comercial avise a tiempo. Espera bajar el quiebre y bajar la merma por vencimiento al mismo tiempo, que es precisamente lo difícil.

---

## CAPÍTULO 10 · RESTRICCIONES NO NEGOCIABLES

Las siguientes condiciones no están en discusión. Una propuesta que no las respete será evaluada como falta de comprensión del caso.

| N° | Restricción |
|---|---|
| 1 | El despacho de la mañana no se detiene. Entre las 05:30 y las 07:00 salen 96 camiones. No existe forma de ejecutar esa ventana a mano. Un sistema indisponible en ese tramo equivale a un día sin operación. |
| 2 | El centro de distribución debe poder recibir, preparar y despachar durante un corte del enlace. La preparación nocturna y la carga no pueden quedar detenidas por conectividad. |
| 3 | Las aplicaciones de preventa y de reparto deben funcionar un turno completo sin señal. Hay rutas donde el dispositivo no recupera cobertura hasta el regreso. |
| 4 | El sistema de gestión no se reemplaza ni se modifica. Es el sistema de registro contable y tributario. La solución le entrega datos; el sistema de gestión emite los documentos tributarios. No habrá dos verdades ni un segundo emisor. |
| 5 | No se puede exigir al cliente del canal tradicional que tenga internet, dispositivo propio ni medio de pago electrónico. La solución debe funcionar con el cliente tal como es. |
| 6 | La solución debe operar con conductores que no son trabajadores de la compañía: 54 camiones de diez empresas transportistas, con rotación sin aviso. |
| 7 | Los dispositivos que se usen en la cámara de congelado deben operar a −22 °C y sin cobertura de señal en su interior. |
| 8 | Congelamiento operacional: prohibido intervenir sistemas entre el 1 y el 25 de septiembre y durante todo el mes de diciembre. Prohibido intervenir durante los tres primeros días hábiles del mes, por el cierre comercial y contable. |
| 9 | El área de tecnologías de información de la compañía son cuatro personas. Toda función que requiera un especialista dedicado que la compañía no tiene debe ofrecerse como servicio y estar costeada. |
| 10 | El sindicato de conductores objetó formalmente, el año pasado, la instalación de cámaras en cabina y el control de jornada por posicionamiento satelital. Cualquier propuesta que involucre esas tecnologías debe hacerse cargo del asunto. |
| 11 | La rotación anual del personal de preparación de pedidos es del 38 % y el turno crítico es nocturno. Toda solución que exija entrenamiento prolongado para operar en bodega será rechazada. |
| 12 | La emisión de documentos tributarios electrónicos debe cumplir la normativa vigente. La guía de despacho electrónica y su acuse de recibo tienen efectos legales que la solución no puede comprometer. |

---

## CAPÍTULO 11 · EXCLUSIONES EXPLÍCITAS

Para evitar sorpresas, el CLIENTE declara expresamente qué NO está pidiendo:

- No se pide reemplazar el sistema de gestión empresarial ni ninguno de sus módulos, ni la emisión de documentos tributarios electrónicos.
- No se pide administrar remuneraciones ni recursos humanos, que residen en el sistema de gestión.
- No se pide un sistema de punto de venta para el local del cliente, sin perjuicio del canal de autoatención que la solución deba ofrecerle.
- No se pide comercio electrónico dirigido al consumidor final.
- No se pide administrar el contrato ni el pago de las empresas transportistas, sí integrarlas operacionalmente.
- No se pide el diseño de la red logística: la ubicación de los centros de distribución y de las plataformas no está en discusión en este proyecto.
- No se pide automatizar la bodega con equipamiento robotizado ni transportadores.
- No se pide la gestión de la flota en su dimensión mecánica, sin perjuicio de integrar la telemetría existente.
- El hardware de terreno —dispositivos, lectores, impresoras portátiles, sensores— lo adquiere el CLIENTE; el PROPONENTE debe especificar exactamente qué comprar, cuánto y con qué características, conforme al Capítulo 8 de las Bases Técnicas Transversales.

> Que algo esté excluido del alcance no significa que pueda ignorarse en el diseño. La solución debe convivir con todo lo excluido, y las dependencias que ello genera deben estar identificadas, documentadas y consideradas en el plan y en el riesgo.

---

## CAPÍTULO 12 · MARCO NORMATIVO Y COMPROMISOS CON TERCEROS

El PROPONENTE deberá identificar, investigar y considerar en su propuesta el marco que aplica a esta industria. El CLIENTE entrega la orientación inicial; la profundización es parte del trabajo.

| Ámbito | Referencia | Por qué importa aquí |
|---|---|---|
| **Inocuidad alimentaria** | Reglamento Sanitario de los Alimentos y las resoluciones sanitarias de los establecimientos de almacenamiento y distribución. | Obliga a condiciones de almacenamiento, control de temperatura, registro y capacidad de retiro de producto. Es el origen del sumario de marzo de 2026. |
| **Trazabilidad y retiro de productos** | Obligación de identificar el origen y el destino de cada lote y de ejecutar un retiro eficaz. | El proveedor lo exigió por escrito como condición para restablecer la relación comercial. |
| **Documentos tributarios electrónicos** | Normativa de la autoridad tributaria sobre factura, guía de despacho electrónica, nota de crédito y acuse de recibo. | La guía de despacho electrónica es obligatoria y su acuse de recibo tiene efectos legales. Determina cómo puede diseñarse la prueba de entrega. |
| **Mérito ejecutivo de la factura** | Normativa sobre transferencia y mérito ejecutivo de la copia de la factura y sobre el acuse de recibo de las mercaderías. | Condiciona la forma en que se documenta la recepción conforme por parte del cliente. |
| **Plazo de pago** | Normativa sobre pago dentro de plazo a proveedores. | Afecta la gestión de cuentas por pagar y la relación con los 180 proveedores. |
| **Protección de datos personales** | Ley N° 21.719. | La compañía trata datos comerciales y de comportamiento de pago de 14.200 clientes, muchos de ellos personas naturales, y datos de geolocalización de personas trabajadoras. |
| **Jornada de conductores** | Régimen especial de jornada de los trabajadores del transporte y control de horas de conducción y descanso. | Condiciona la planificación de rutas y el uso de datos de posicionamiento para control de jornada. |
| **Derechos del consumidor y del comprador** | Normativa aplicable a devoluciones, cambios y garantías en la relación comercial. | Determina el tratamiento de las devoluciones y su documentación. |
| **Identificación y codificación** | Estándares GS1: identificación de productos, de unidades logísticas y de ubicaciones; mensajería electrónica entre socios comerciales; y estándares de trazabilidad de eventos. | Es el lenguaje que hablan los proveedores y las cadenas. El PROPONENTE deberá investigar qué exige concretamente cada uno. |
| **Responsabilidad penal de la persona jurídica** | Ley N° 20.393 y Ley N° 21.595. | Relevante por el manejo de efectivo, las diferencias de rendición y los controles internos asociados. |

> **Este listado es orientador, no exhaustivo. El PROPONENTE es responsable de identificar la normativa aplicable completa y de acreditar en su propuesta cómo la solución la satisface. Invocar una norma sin explicar qué control concreto la implementa se evaluará como no acreditada.**

---

## CAPÍTULO 13 · HORIZONTE, PRIORIDADES Y ETAPAS

### 13.1 Lo que el comité ejecutivo quiere primero

El comité ejecutivo expresó, sin transformarlo en instrucción técnica, un orden de urgencia: primero la trazabilidad de lote y la cadena de frío, porque de ellas depende la habilitación comercial ante los proveedores y ante la autoridad; luego la preventa y la entrega con evidencia digital, porque de ellas depende no seguir perdiendo clientes frente al competidor; y por último la optimización de rutas y el costo de servir, que el comité considera valiosos pero no urgentes.

Amparo Ossa dejó una observación en el acta que conviene tomar en serio: «me dicen que la ruta es lo menos urgente, pero don Hugo se jubila en dos años y con él se va la operación. A lo mejor lo menos urgente es lo más grave».

Ese orden es una preferencia del mandante, no una definición de alcance. La distribución concreta entre la Etapa 1 y la Etapa 2 la propone el PROPONENTE y debe justificarla en función de las dependencias técnicas, del riesgo, de la capacidad de absorción del CLIENTE y del cronograma contractual obligatorio del Artículo 17° de las Bases Administrativas.

> Una propuesta que se limite a repetir el orden de preferencia del comité sin analizarlo será evaluada como falta de criterio profesional. Si el PROPONENTE considera que hay una dependencia técnica que obliga a alterar ese orden, debe decirlo y fundamentarlo. El CLIENTE contrata ingeniería, no obediencia.

### 13.2 Hitos externos que condicionan el proyecto

| Fecha | Hito externo | Consecuencia |
|---|---|---|
| **Septiembre de cada año** | Peak de Fiestas Patrias. El volumen diario casi se duplica durante tres semanas. | Ventana de congelamiento total. También el período de mayor exigencia sobre cualquier componente nuevo. |
| **Diciembre de cada año** | Peak de Navidad y fin de año. | Segunda ventana de congelamiento total. |
| **Primeros tres días hábiles de cada mes** | Cierre comercial y contable. | Prohibido intervenir sistemas con impacto en facturación o inventario valorizado. |
| **Septiembre de 2026** | Vencimiento de la suspensión comercial impuesta por el proveedor de lácteos. | La compañía debe acreditar capacidad de trazabilidad para restablecer la relación. |
| **Enero de 2029** | Entrada en vigor de las condiciones comerciales de la principal cadena de supermercados. | Pedido electrónico, aviso de despacho, ventana de 30 minutos y prueba de entrega digital deben estar en producción antes de esa fecha. |
| **2030** | Evaluación de apertura de un centro de distribución en la Región de Los Lagos. | No es seguro. Si ocurre, el CLIENTE espera replicar la solución sin rehacerla. |
| **Permanente** | Avance del competidor nacional en la zona. | Cada mes de retraso del proyecto tiene un costo comercial que el PROPONENTE debería ser capaz de estimar. |

### 13.3 Estrategia de puesta en producción esperada

El CLIENTE no impone una estrategia de implantación, pero sí declara las condiciones que cualquier estrategia debe respetar:

1. Nada entra en producción sin haber convivido con la forma actual de trabajar durante la marcha blanca correspondiente, con conciliación entre ambas y con la posibilidad de volver atrás.
2. El paso a producción no puede ocurrir en septiembre ni en diciembre, ni en los tres primeros días hábiles del mes.
3. El despliegue debe poder hacerse por proceso, por sitio o por zona comercial, y no como un único evento que afecte simultáneamente a la bodega, la preventa, el reparto y la facturación.
4. La preparación de pedidos es nocturna: toda intervención en bodega y todo acompañamiento debe considerar el turno de noche.
5. Los preventistas y los conductores están en la calle todos los días. Capacitarlos exige diseñar cómo se hace sin detener la venta ni el reparto.
6. Los conductores de las empresas transportistas no son trabajadores de la compañía: su incorporación requiere un mecanismo distinto y un acuerdo con cada transportista.
7. La estabilización posterior a cada paso a producción debe tener dotación y duración declaradas, y contemplar presencia en bodega y acompañamiento en ruta.

> El CLIENTE ha visto fracasar iniciativas por falta de adopción y su gerenta general lo advirtió de forma explícita: en una empresa donde la gente lleva veinte o treinta años, un proyecto que pase por encima de las personas será hundido sin que nadie diga una palabra. La estrategia de puesta en producción y de adopción pesa, en la evaluación de este caso, tanto como la arquitectura.

---

# TÍTULO V — ANTECEDENTES PARA EL DIMENSIONAMIENTO

## CAPÍTULO 14 · VOLUMETRÍA: LO QUE SE ENTREGA Y LO QUE SE DEBE ESTIMAR

El CLIENTE entrega los volúmenes que efectivamente conoce, porque son los que gobierna su operación. Los volúmenes propios del dimensionamiento de un sistema —concurrencia, transacciones por segundo, almacenamiento, integraciones— no los conoce, y no tiene por qué conocerlos: derivarlos es trabajo de ingeniería del PROPONENTE.

> **Las celdas marcadas como «a estimar» deben completarse en la propuesta con el valor estimado, el método de estimación y los supuestos empleados. Entregar la propuesta con esas celdas vacías, o con valores sin derivación, se evaluará como dimensionamiento no realizado.**

### 14.1 Volumetría operacional entregada por el CLIENTE

| Dimensión | Valor actual | Proyección a 3 años |
|---|---|---|
| **Clientes activos y puntos de entrega** | 14.200 | 15.500 |
| **SKU activos** | 8.400 | 9.500 |
| **De ellos, refrigerados o congelados** | 1.100 | 1.400 |
| **Proveedores** | 180 | 200 |
| **Pedidos al mes** | 31.000 | 36.000 |
| **Líneas de pedido al mes** | 260.000 | 305.000 |
| **Unidades despachadas al mes** | 2,4 millones | 2,8 millones |
| **Entregas en día hábil normal** | ≈ 1.400 | ≈ 1.650 |
| **Entregas en día hábil de peak de septiembre** | ≈ 2.600 | ≈ 3.100 |
| **Viajes de camión al mes** | ≈ 2.100 | ≈ 2.400 |
| **Kilómetros recorridos al mes** | ≈ 420.000 | ≈ 480.000 |
| **Recepciones de proveedor al mes** | 1.150 | 1.300 |
| **Pallets movidos al mes en el centro de distribución de Talca** | 14.500 | 17.000 |
| **Líneas de preparación de pedidos al mes** | 260.000 | 305.000 |
| **Posiciones de conteo cíclico al mes** | 3.400 | 3.900 |
| **Documentos tributarios emitidos al mes** | ≈ 34.000 | ≈ 40.000 |
| **Devoluciones al mes** | ≈ 900 | ≈ 1.000 |
| **Envases retornables en circulación** | 68.000 canastillos y 9.400 pallets | no proyectado |
| **Visitas de preventa al mes** | ≈ 62.000 | ≈ 72.000 |
| **Cobros en efectivo al mes** | ≈ 11.800 | no proyectado |
| **Preventistas** | 62 | 70 |
| **Conductores (42 propios y ≈160 de terceros)** | ≈ 200 | ≈ 230 |
| **Personas en centro de distribución, todos los turnos** | 310 | 350 |
| **Instalaciones a cubrir** | 6, más la calle y 14.200 puntos de entrega | 7 |

### 14.2 Volumetría de sistema que el proponente debe estimar

| Dimensión | Valor |
|---|---|
| **Transacciones por segundo en régimen normal** | *A estimar y declarar como supuesto* |
| **Transacciones por segundo en el peak de la ventana de despacho de 05:30 a 07:00** | *A estimar y declarar como supuesto* |
| **Transacciones por segundo en el peak de septiembre** | *A estimar y declarar como supuesto* |
| **Personas usuarias registradas, internas y externas** | *A estimar y declarar como supuesto* |
| **Personas usuarias concurrentes en peak** | *A estimar y declarar como supuesto* |
| **Dispositivos de terreno en operación simultánea** | *A estimar y declarar como supuesto* |
| **Volumen anual de almacenamiento transaccional** | *A estimar y declarar como supuesto* |
| **Volumen anual de almacenamiento de evidencia de entrega, firmas y fotografías** | *A estimar y declarar como supuesto* |
| **Volumen anual de almacenamiento de series de temperatura y de posicionamiento** | *A estimar y declarar como supuesto* |
| **Volumen total de datos históricos a migrar** | *A estimar y declarar como supuesto* |
| **Número de integraciones y volumen de mensajes por integración** | *A estimar y declarar como supuesto* |
| **Ancho de banda requerido por sitio, en régimen y en peak** | *A estimar y declarar como supuesto* |
| **Volumen de datos generado por un dispositivo de reparto en un turno completo sin señal** | *A estimar y declarar como supuesto* |
| **Tiempo de sincronización de la flota al regresar al centro de distribución** | *A estimar y declarar como supuesto* |
| **Contactos mensuales a la mesa de ayuda** | *A estimar y declarar como supuesto* |
| **Dotación de la mesa de ayuda y del equipo de operación** | *A estimar y declarar como supuesto* |

> Preste atención al perfil de carga de este caso: no es plano. La preventa concentra su actividad entre las 09:00 y las 18:00; la preparación de pedidos entre las 22:00 y las 06:00; el despacho entre las 05:30 y las 07:00; y la sincronización de la flota entre las 17:00 y las 20:00. En septiembre todo se multiplica. Un dimensionamiento basado en el promedio diario estará equivocado.

---

## CAPÍTULO 15 · PARÁMETROS DEL CASO PARA LOS REQUISITOS «SEGÚN CASO»

Las Bases Técnicas Transversales marcan un conjunto de requisitos como «Según caso»: son obligatorios, pero su valor concreto lo fija cada industria. Los valores para el Caso 02 son los siguientes. Cuando este capítulo endurece un umbral del documento transversal, prevalece el más exigente.

| Código | Materia | Valor para el Caso 02 |
|---|---|---|
| **RT-02.12** | Replicación a nuevas unidades | Exigible. La compañía evalúa abrir un centro de distribución en la Región de Los Lagos hacia 2030. La solución debe admitir la incorporación de un nuevo sitio, con su bodega, sus rutas y su cartera, por parametrización. |
| **RT-03.10** | Operación desconectada del componente on-premise | Centro de distribución: mínimo 24 horas continuas de recepción, preparación y despacho sin enlace. Dispositivos de terreno: un turno completo de 14 horas sin cobertura, con capacidad de registrar la jornada íntegra de un repartidor de ruta rural. |
| **RT-03.13** | Sincronización tras la reconexión | La sincronización de un dispositivo de reparto tras un turno completo sin señal no debe superar 10 minutos. La sincronización del centro de distribución tras un corte de 24 horas no debe superar 2 horas y debe resolver de forma determinista los conflictos de stock. |
| **RT-03.24** | Red inalámbrica de los sitios operacionales | Exigible un estudio de cobertura de los centros de distribución que incluya expresamente el interior de las cámaras de refrigerado y de congelado, hoy sin señal, y la propuesta técnica para resolverlo. |
| **RT-05.10** | Retención de datos históricos y de auditoría | Documentos tributarios y su respaldo: 6 años. Registros sanitarios y de trazabilidad de lote: vida útil del producto más 6 meses, con mínimo de 5 años. Registros de temperatura: 5 años. Evidencia de entrega: 6 años. Datos de geolocalización de personas: 12 meses. |
| **RT-05.15** | Datos históricos a migrar | Maestros de clientes, productos y proveedores: completos. Ventas y pedidos: 3 años. Inventario y movimientos: 2 años. Trazabilidad sanitaria: 5 años. Cuentas por cobrar: saldos vivos más 2 años. |
| **RT-05.23** | Estándares sectoriales de intercambio | Estándares GS1 para identificación de productos, unidades logísticas y ubicaciones; mensajería electrónica entre socios comerciales en el formato que exija cada cadena; estándar de trazabilidad de eventos para la cadena de custodia; y el formato de la autoridad tributaria para los documentos electrónicos. |
| **RT-05.29** | Latencia de la capa analítica | Indicadores de la operación del día —entregas cumplidas, faltantes, devoluciones, temperatura— no superior a 5 minutos. Cierre comercial del día no superior a 2 horas tras el retorno del último camión. Indicadores de gestión no superior a 4 horas. |
| **RT-06.01** | Tipología del emplazamiento on-premise | Sala técnica secundaria en el centro de distribución de Talca, dimensionada para sostener recepción, preparación y despacho durante un corte. La sala actual de 25 m² no cumple el Capítulo 6 del documento transversal. Gabinetes de borde en el centro de distribución de Concepción y en las tres plataformas de cross-docking. |
| **RT-09.01** | Transacción operacional crítica | Confirmación de una línea de preparación de pedidos: no superior a 1 segundo. Registro de una entrega en el local del cliente: no superior a 2 segundos. Registro de una línea en la toma de pedido de preventa: no superior a 1,5 segundos. Consulta de stock y crédito en preventa: no superior a 2 segundos. |
| **RT-09.02** | Concurrencia y volumen de transacciones | El PROPONENTE lo deriva de la volumetría del numeral 14.1, considerando el perfil horario descrito, y lo declara conforme al numeral 14.2. |
| **RT-10.05** | Ventana operacional protegida | Ventana crítica de despacho de 05:30 a 07:00 de lunes a sábado: indisponibilidad cero. Preparación de pedidos de 22:00 a 06:00. Recepción de proveedores de 08:00 a 18:00. Congelamiento total del 1 al 25 de septiembre y durante todo diciembre. Congelamiento durante los tres primeros días hábiles de cada mes. |
| **RT-11.10** | Cifrado a nivel de campo | Exigible para el comportamiento de pago y los antecedentes comerciales de los clientes, para los datos de geolocalización de personas y para los datos de medios de pago electrónicos, si se incorporan. |
| **RT-12.11** | Autenticación en el perfil operacional | Conductores de empresas transportistas sin correo corporativo y con rotación sin aviso. Dispositivos compartidos entre turnos en bodega. Personal de preparación con 38 % de rotación anual. Uso con guantes térmicos a −22 °C. Uso a una mano durante la descarga. Uso de pie, a la intemperie, en la puerta del local del cliente. |
| **RT-12.12** | Personas usuarias externas | Clientes del canal tradicional y de food service; cadenas de supermercados; empresas transportistas y sus conductores; y proveedores. |
| **RT-13.08** | Interfaces de terreno | Exigible operación con guantes térmicos, a −22 °C en cámara de congelado, bajo lluvia y sobre 34 °C en verano, a una sola mano, con pantalla legible bajo sol directo, y sin conexión durante un turno completo. |
| **RT-15.02** | Certificaciones sectoriales del adjudicatario | Conocimiento acreditado del Reglamento Sanitario de los Alimentos y de la normativa de documentos tributarios electrónicos. Experiencia comprobable en distribución de consumo masivo o en operación logística con cadena de frío. |
| **RT-16.09** | Registro de consultas a información sensible | Exigible para los antecedentes comerciales y el comportamiento de pago de los clientes, y para los datos de geolocalización de personas, además del registro de modificaciones. |
| **RT-16.14** | Firma electrónica | La prueba de entrega debe articularse con la guía de despacho electrónica y su acuse de recibo conforme a la normativa tributaria vigente. El PROPONENTE deberá investigar y proponer el mecanismo, considerando que el receptor habitual es una persona natural sin firma electrónica avanzada. |
| **RT-16.21** | Canales de notificación | Correo electrónico, notificación en aplicación, mensajería instantánea al cliente del canal tradicional, y mensaje de texto para avisos de despacho y de llegada. El canal debe elegirse por cliente, porque buena parte del canal tradicional no usa correo. |
| **RT-16.30** | Portal público | Catálogo público de productos sin precios. Portal autenticado para clientes, con pedido en autoservicio, estado de entrega, documentos y saldo. Portal autenticado para transportistas y para proveedores. |
| **RT-17.01** | Aplicación móvil | Exigible en cuatro perfiles, todos con operación desconectada: preventa, reparto, preparación y recepción en bodega, y autoatención del cliente. |
| **RT-17.06** | Periféricos a integrar | Lectores de código de barras unidimensionales y bidimensionales, impresora térmica portátil en cabina, sensores de temperatura en cámaras y en vehículos, telemetría de flota, terminales de pago electrónico, balanzas de recepción, y captura de firma y de fotografía en el dispositivo. |
| **RT-21.06** | Horario del centro de atención | De 04:00 a 22:00 de lunes a sábado, con cobertura 24×7 durante los peaks de septiembre y diciembre y ante incidentes de severidad crítica en la ventana de despacho. |
| **RT-21.16** | Traslado a sitios alejados | Exigible. Seis instalaciones en cuatro regiones, entre Curicó y Los Ángeles, con 340 km entre los extremos. |
| **RT-22.04** | Restricción de la capacitación | El personal de preparación trabaja en turno nocturno y rota 38 % al año. Preventistas y conductores están en la calle de lunes a sábado. Los conductores de empresas transportistas no son trabajadores de la compañía y su capacitación requiere acuerdo con cada transportista. |

---

## CAPÍTULO 16 · LO QUE ESTE DOCUMENTO DELIBERADAMENTE NO RESUELVE

Las decisiones que siguen son necesarias para que la solución sea coherente. El CLIENTE no las ha tomado, y no las va a tomar por el PROPONENTE. Resolverlas, dejarlas escritas como supuesto y hacerse cargo de sus consecuencias en la arquitectura, en el alcance y en el costo forma parte del trabajo profesional que se licita.

### 16.1 Decisiones de diseño pendientes

| N° | Decisión no tomada | Por qué importa |
|---|---|---|
| 1 | Qué cuenta como entrega cumplida cuando la entrega es parcial, y cómo se mide el indicador de servicio. | Hoy cada área lo cuenta distinto y por eso nadie se pone de acuerdo sobre el estado real del servicio. |
| 2 | Cuál es la unidad de trazabilidad sanitaria: el lote del proveedor, la caja, el pallet o una unidad logística identificada individualmente. | Determina el volumen de datos, el esfuerzo en recepción y preparación, y la calidad de la respuesta ante un retiro. |
| 3 | Qué se hace cuando el local del cliente está cerrado: reintento, entrega a un tercero, devolución. Y quién decide. | Hoy decide cada conductor según su criterio. Es la causa principal de las reentregas. |
| 4 | Qué constituye una excursión de temperatura que invalida el producto, quién lo decide y si el sistema bloquea el despacho de forma automática. | Es la tensión declarada entre calidad y operaciones. Sin regla escrita no hay control posible. |
| 5 | Cómo se identifica al conductor de una empresa transportista y qué ocurre cuando el transportista lo cambia sin avisar. | Son 54 camiones y unos 160 conductores que no son trabajadores de la compañía. |
| 6 | Qué se hace con el efectivo: eliminarlo, reducirlo o controlarlo. Y quién asume el riesgo del dinero en circulación. | Involucra al 38 % de la venta del canal tradicional, la seguridad de los conductores y $ 4,2 millones mensuales de diferencia. |
| 7 | Cómo se valoriza el costo de servir y qué se hace con los clientes que resulten no rentables. | Es la pregunta que el gerente de finanzas declara como su obsesión y de la que dependen decisiones comerciales. |
| 8 | Cuál es la regla de asignación de stock cuando dos preventistas comprometen el mismo producto y no alcanza para ambos. | Determina si el stock se reserva en la toma del pedido, en la confirmación o en la preparación, y con qué consecuencias. |
| 9 | Qué ocurre cuando el precio cambia entre la toma del pedido y el despacho. | Afecta la facturación, la relación con el cliente y la credibilidad del preventista. |
| 10 | Cómo se controla el parque de envases retornables: por saldo por cliente, por unidad identificada, o no se controla. | Son 68.000 canastillos y 9.400 pallets con una pérdida estimada del 14 % anual. |
| 11 | Qué maestro de productos manda cuando el proveedor cambia el formato, el contenido o el código de un producto. | Con 180 proveedores y 8.400 productos, ocurre todas las semanas y hoy se resuelve caso a caso. |
| 12 | Cómo se procesa una devolución en el momento de la entrega y qué efecto tiene sobre un documento tributario ya emitido. | Tiene consecuencias tributarias y contables que la solución no puede improvisar. |
| 13 | Cómo se resuelve la objeción sindical a las cámaras en cabina y al control de jornada por posicionamiento satelital. | Determina qué tecnologías pueden proponerse y con qué plan de gestión del cambio. |
| 14 | Qué se hace con el sistema de gestión de almacenes de 2013: mantenerlo, extenderlo a los demás sitios o reemplazarlo. | Es la decisión de alcance más costosa del caso y el CLIENTE la delega expresamente en el PROPONENTE. |
| 15 | Cómo se prueba la entrega cuando quien recibe no es el titular, no sabe firmar en pantalla o se niega a hacerlo. | Afecta la validez de la evidencia y su articulación con el acuse de recibo tributario. |
| 16 | Qué se hace con el conocimiento de rutas que hoy reside en una sola persona, antes de que se jubile. | Es un riesgo de continuidad operacional con fecha conocida. |

Esta lista no es exhaustiva. Encontrar los demás vacíos es parte del ejercicio, y el PROPONENTE que identifique vacíos no listados aquí será evaluado favorablemente por ello.

### 16.2 Materias que el proponente deberá investigar

El CLIENTE no espera que el PROPONENTE conozca la distribución de consumo masivo de antemano. Sí espera que la estudie. Las siguientes materias son necesarias para formular una propuesta competente y no se explican en este documento:

- Estándares GS1: identificación de productos, de unidades logísticas y de ubicaciones; simbología de códigos de barras; y estándares de trazabilidad de eventos en la cadena de suministro.
- Intercambio electrónico de datos con cadenas de retail en Chile: qué mensajes se exigen, en qué formato y a través de qué intermediarios.
- Documentos tributarios electrónicos: guía de despacho electrónica, factura, nota de crédito, acuse de recibo y sus efectos legales.
- Reglamento Sanitario de los Alimentos: obligaciones de almacenamiento, transporte, control de temperatura, registro y retiro de producto.
- Cadena de frío: rangos por tipo de producto, concepto de excursión térmica, criterios de aceptación y de rechazo, y tecnologías de registro continuo.
- Indicadores logísticos: OTIF, fill rate, perfect order, costo de servir y costo por entrega. Cómo se definen y cómo se calculan sin ambigüedad.
- El problema de ruteo de vehículos con capacidad y ventanas de tiempo: formulación, métodos de resolución, y sus limitaciones prácticas frente al conocimiento local del planificador.
- Estrategias de preparación de pedidos y de asignación de ubicaciones en bodega: por olas, por zonas, por lotes, y criterios de ubicación por rotación.
- Pronóstico de demanda en consumo masivo con estacionalidad fuerte y promociones, y su articulación con la política de inventario y el nivel de servicio.
- Régimen de jornada de los trabajadores del transporte y control de horas de conducción y descanso.
- Logística inversa: devoluciones, mermas y gestión de activos retornables.
- Modelos de atención al canal tradicional: preventa, autoventa, autoatención digital y sus efectos sobre el costo de servir.

> La calidad de esta investigación se hará evidente en el Informe 1 y en la defensa técnica. Una propuesta que hable de «trazabilidad» sin conocer los estándares de identificación de la industria, o que proponga optimizar rutas sin haber entendido por qué el planificador desconfía, quedará en evidencia frente a la Comisión de Expertos.

---

# TÍTULO VI — LO QUE DEBE PRODUCIR EL PROPONENTE

## CAPÍTULO 17 · EL TRABAJO DE TRADUCCIÓN EXIGIDO

Este documento describe una operación y sus problemas. No contiene un catálogo de requerimientos. Construirlo es la primera tarea del PROPONENTE y la que condiciona todas las demás.

### 17.1 De la necesidad al requerimiento

El PROPONENTE deberá recorrer este documento y producir un catálogo de requerimientos trazable a su origen. Cada requerimiento debe indicar de qué párrafo, entrevista, indicador o restricción proviene, de modo que el CLIENTE pueda verificar que nada quedó fuera y que nada se inventó.

| Producto | Contenido esperado |
|---|---|
| **Catálogo de requerimientos funcionales** | Qué debe hacer la solución, expresado en términos verificables, con identificador, descripción, actor, precondición, resultado esperado, prioridad y origen en este documento. |
| **Catálogo de requerimientos no funcionales** | Desempeño, disponibilidad, seguridad, usabilidad, operabilidad, mantenibilidad, portabilidad y cumplimiento, con umbral numérico y método de verificación. Deben incorporar los parámetros del Capítulo 15 y los requisitos del documento transversal. |
| **Registro de supuestos** | Toda decisión que el PROPONENTE tomó por el CLIENTE, con su fundamento, su impacto si resulta equivocada y la instancia en que se validará. Incluye obligatoriamente las dieciséis decisiones del numeral 16.1. |
| **Registro de reglas de negocio** | Las reglas propias de la industria que la solución debe respetar y que este documento no explicita: asignación de stock, política de crédito, excursión térmica, reintento de entrega, tratamiento de devoluciones, control de envases, entre otras. |
| **Matriz de trazabilidad** | Correspondencia entre origen, requerimiento, componente de la arquitectura, paquete de la EDT, prueba de verificación y criterio de aceptación. |
| **Registro de vacíos y consultas** | Aquello que el PROPONENTE no puede resolver por sí solo y que someterá al CLIENTE durante el período de consultas. |

> **Un requerimiento no es una frase copiada de este documento. «Debe haber trazabilidad de lote» no es un requerimiento: es una necesidad. El requerimiento indica qué se captura, en qué punto del proceso, por quién, con qué dato, con qué tiempo de respuesta y cómo se verifica que se cumplió.**

### 17.2 Distinguir lo funcional de lo no funcional

Buena parte de lo que este documento describe puede leerse de las dos maneras, y la clasificación no es indiferente: determina quién lo verifica, cómo se prueba y en qué momento del proyecto se comprueba. Se ofrecen deliberadamente sin resolver algunos casos limítrofes:

- «La confirmación de una línea de picking no debe superar un segundo»: ¿es un requerimiento no funcional de desempeño, o es funcional porque de él depende que el turno de noche alcance a preparar los pedidos antes de las 06:00?
- «Debe funcionar a −22 °C»: ¿es una restricción de diseño del dispositivo, un requerimiento no funcional de ambiente operativo, o un requerimiento funcional de la preparación de congelados?
- «Debe operar un turno completo sin señal»: ¿es disponibilidad, es una decisión de arquitectura, o es un conjunto de requerimientos funcionales sobre qué puede hacer y qué no el repartidor en modo desconectado?
- «El preventista debe ver el stock disponible»: ¿es una funcionalidad de consulta o una regla de negocio de reserva de inventario?
- «La prueba de entrega debe tener validez ante el cliente»: ¿es trazabilidad, es cumplimiento normativo tributario, o es un requerimiento funcional de captura de evidencia?
- «El sistema debe bloquear el despacho ante una excursión térmica»: ¿es un control de calidad, una regla de negocio o un requerimiento funcional del proceso de carga?

Se evaluará el criterio con que el PROPONENTE resuelve estos casos y la consistencia con que aplica su propio criterio a lo largo de la propuesta, no la coincidencia con una respuesta preestablecida.

### 17.3 Definir el alcance y su reparto entre etapas

A partir del catálogo, el PROPONENTE deberá delimitar el alcance de la Etapa 1 y de la Etapa 2, declarar las exclusiones y justificar el reparto en función de las dependencias técnicas, del riesgo, de los hitos externos del numeral 13.2 y de la capacidad de absorción del CLIENTE.

La justificación debe hacerse cargo explícitamente de la preferencia del comité ejecutivo expresada en el numeral 13.1 —y de la objeción que la propia gerenta general dejó en el acta respecto de la jubilación del planificador—, ya sea acogiéndolas o apartándose de ellas con fundamento técnico.

### 17.4 Diseñar la arquitectura

La arquitectura lógica y física debe ser propia de este caso y reconocible como tal. Debe hacerse cargo, como mínimo, de los siguientes asuntos, todos ellos derivados de lo descrito en este documento:

1. Qué se ejecuta en cada centro de distribución y qué en la nube, y por qué, componente por componente, conforme al Capítulo 3 de las Bases Técnicas Transversales.
2. Cómo se sostiene la recepción, la preparación y el despacho durante un corte de enlace, y cómo se reconcilia el inventario después.
3. Cómo opera un dispositivo de reparto durante un turno completo sin señal, qué puede y qué no puede hacer, y cómo se resuelven los conflictos al sincronizar.
4. Cómo se resuelve la captura de datos dentro de la cámara de congelado, a −22 °C y sin cobertura.
5. Cómo se integra el sistema de gestión empresarial y la emisión de documentos tributarios, en qué sentido, con qué frecuencia y con qué garantía de consistencia.
6. Qué se hace con el sistema de gestión de almacenes de 2013, y qué consecuencias tiene la decisión sobre el alcance, el costo y el riesgo.
7. Cómo se modela la trazabilidad de lote desde la recepción hasta el punto de entrega, y qué estructura de datos la sostiene.
8. Cómo se captura y se conserva la evidencia de entrega, y cómo se articula con la guía de despacho electrónica y su acuse de recibo.
9. Cómo se incorporan a la solución los conductores de empresas transportistas, con sus dispositivos y su rotación.
10. Cómo se sirve el canal moderno con mensajería electrónica estructurada sin construir una integración distinta para cada cadena.
11. Cómo se separa el almacenamiento transaccional del analítico y cómo se sirven los indicadores del día con la latencia comprometida.
12. Qué se hace con la sala de servidores actual, que no cumple el estándar exigido.
13. Cómo absorbe el diseño el peak de septiembre, que casi duplica el volumen durante tres semanas, y qué componente se satura primero.

### 17.5 Planificar de forma realista

El plan de trabajo debe ser específico de esta operación. Un cronograma que podría servir para cualquier proyecto será evaluado como deficiente. En particular deberá reflejar:

- El cronograma contractual obligatorio de 56 meses del Artículo 17° de las Bases Administrativas, sin proponer plazos alternativos.
- Las dos ventanas de congelamiento anual, septiembre y diciembre, que suman casi dos meses sin posibilidad de intervenir.
- El cierre comercial de los tres primeros días hábiles de cada mes.
- El turno nocturno de preparación de pedidos, donde ocurre buena parte de la implantación en bodega.
- La rotación del 38 % anual en preparación, que obliga a un mecanismo de capacitación continua y no a un evento único.
- La imposibilidad de detener la preventa y el reparto para capacitar: 62 preventistas y unos 200 conductores están en la calle de lunes a sábado.
- La negociación con diez empresas transportistas para incorporar a sus conductores y sus vehículos.
- La negociación técnica con las cadenas de supermercados para la mensajería electrónica, que no es una tarea de dos semanas.
- La ausencia de documentación de las interfaces del sistema de gestión, que el CLIENTE reconoce no tener.
- El traspaso del conocimiento de rutas del planificador antes de su jubilación, que tiene fecha y no se puede postergar.
- El solapamiento de los meses 13 a 15 y 19 a 20, con la dotación efectivamente necesaria para sostener dos frentes simultáneos.

### 17.6 Proponer una estrategia de puesta en producción y de operación

El CLIENTE ha declarado que este es el punto donde una empresa familiar de cincuenta y dos años puede hundir un proyecto sin decir una palabra. La propuesta deberá contener una estrategia explícita y no una declaración de intenciones:

1. Qué entra en producción primero, en qué sitio, con qué zona comercial y con qué criterio de avance a la ola siguiente.
2. Cómo conviven la solución y la forma actual de trabajar durante cada marcha blanca, cómo se concilian ambas y en qué momento se apaga la anterior. En bodega esto significa convivir con la hoja de picking; en la ruta, con la guía de papel.
3. Qué indicadores se medirán diariamente durante la marcha blanca y con qué umbral se declara cerrada, conforme al Artículo 17.3 de las Bases Administrativas.
4. Cómo se revierte un paso a producción fallido en la ventana de despacho, en cuánto tiempo y qué se pierde al hacerlo.
5. Qué dotación de acompañamiento habrá en bodega en turno de noche, y cómo se acompaña a un preventista o a un conductor que está en la calle.
6. Cómo se incorpora y se capacita a los conductores de empresas transportistas, que no son trabajadores de la compañía.
7. Cómo se mide la adopción, con qué meta, y qué se hace si la adopción no alcanza la meta. Se espera una respuesta distinta para el personal con veinte años de antigüedad y para el que rota cada seis meses.
8. Cómo se transfiere la operación al equipo del CLIENTE, que son cuatro personas, y qué queda como servicio permanente del ADJUDICATARIO.
9. Cómo se opera durante los 36 meses siguientes, con especial atención a los peaks de septiembre y diciembre y a la ventana crítica de despacho de las mañanas.

---

## CAPÍTULO 18 · CRITERIOS DE ACEPTACIÓN DEL CASO

Los siguientes resultados de negocio son los que el CLIENTE utilizará para juzgar si el PROYECTO fue exitoso. El PROPONENTE deberá comprometerse con ellos, proponer la meta cuando este documento no la fije, indicar en qué momento del cronograma se alcanzará cada uno y cómo se medirá.

| N° | Resultado esperado | Situación actual |
|---|---|---|
| 1 | Ante un retiro sanitario, la lista de clientes afectados por lote se obtiene con evidencia en menos de dos horas. | 9 días, con resultado estimado. |
| 2 | El 100 % de las recepciones registra el lote de los productos que lo requieren. | 41 % sin registro en el producto involucrado. |
| 3 | Existe registro continuo y automático de temperatura en cámaras y vehículos, auditable y disponible para el cliente. | 3 lecturas manuales por viaje. |
| 4 | El indicador de entregas completas y a tiempo se mide de una sola forma y alcanza la meta comprometida por el PROPONENTE. | 82,4 %, medido de forma distinta por cada área. |
| 5 | El preventista conoce el stock disponible y el crédito del cliente en el momento de tomar el pedido. | No los conoce. |
| 6 | Ningún pedido se pierde ni se duplica por falta de señal. | Ocurre semanalmente, sin medición. |
| 7 | La ruta del día siguiente se genera automáticamente en menos de 20 minutos y el planificador puede corregirla, quedando registro de cada corrección. | 3,5 horas de una persona insustituible. |
| 8 | La prueba de entrega es digital y está disponible para el cliente el mismo día. | Guía en papel; 12 días para resolver un reclamo. |
| 9 | Cero guías extraviadas o ilegibles. | 1,1 % mensual. |
| 10 | La rendición del efectivo cuadra el mismo día y toda diferencia queda explicada. | $ 4,2 millones mensuales de diferencia sin investigar. |
| 11 | El costo de servir se conoce por cliente y por entrega, construido desde el hecho. | Prorrateo por zona con criterio de 2016. |
| 12 | El parque de envases retornables se controla y la pérdida anual baja bajo la meta comprometida. | 14 % de pérdida estimada, sin control. |
| 13 | Los pedidos de las cadenas entran por vía electrónica estructurada, sin digitación, y se responde con aviso de despacho. | Cero pedidos electrónicos. |
| 14 | La ocupación de los camiones sube y ningún camión sale bajo el umbral que el PROPONENTE comprometa. | 68 % promedio, con días de 41 %. |
| 15 | La causa de cada faltante queda registrada al momento de producirse. | Se registra el faltante, no la causa. |
| 16 | Don Hugo se puede jubilar sin que la operación se resienta. | El cumplimiento cae 6 a 9 puntos cuando está de vacaciones. |

> El criterio número 16 no es una nota de color. Hoy la planificación diaria de 1.400 entregas depende del conocimiento no documentado de una persona que se jubila dentro del horizonte de este contrato. La propuesta deberá explicar cómo captura ese conocimiento antes de que se vaya.

---

## CAPÍTULO 19 · CÓMO SE EVALUARÁ ESTE CASO

La evaluación se rige por el Título V de las Bases Administrativas y por la ponderación del Formulario T-21. Este capítulo precisa qué se buscará específicamente en el Caso 02 al aplicar esos criterios.

| Ítem | Qué se buscará en este caso |
|---|---|
| **Comprensión del problema** | Que el PROPONENTE distinga los tres problemas entrelazados —habilitación sanitaria y comercial, competitividad del servicio y desconocimiento del costo— y no los trate como uno solo. Que use el vocabulario logístico con propiedad. Que dimensione el problema con los datos entregados y con los que haya investigado. |
| **Esquema de solución y alcance** | Que el alcance sea consecuencia del catálogo de requerimientos y no un listado de módulos. Que la decisión sobre el sistema de gestión de almacenes esté tomada y fundada. Que las exclusiones sean explícitas. |
| **Arquitectura lógica y física** | Que resuelva de forma verificable el despacho durante un corte, el turno completo sin señal, la captura a −22 °C, la integración con el sistema de gestión y con los documentos tributarios, y el peak de septiembre. Que sea propia de Puelche y no un diagrama de referencia con el nombre cambiado. |
| **Modelo y gestión de datos** | Que el modelo de trazabilidad soporte la pregunta del proveedor y la de la autoridad sanitaria. Que las dieciséis decisiones pendientes del numeral 16.1 estén resueltas y declaradas. |
| **Plan de trabajo, EDT y cronograma** | Que refleje las dos ventanas de congelamiento, el cierre mensual, el turno de noche, la rotación en bodega, la calle, los transportistas y la jubilación del planificador. Que la ruta crítica sea creíble. |
| **Plan de riesgos** | Que los riesgos sean de este proyecto: pérdida del conocimiento de rutas, objeción sindical, rechazo de los conductores de terceros, rotación en bodega, ausencia de documentación de interfaces, dependencia de un solo enlace en Concepción, peak de septiembre coincidiendo con una fase del proyecto. |
| **Servicios de operación y niveles de servicio** | Que el modelo de soporte cubra la ventana crítica de despacho de la madrugada, el turno nocturno de bodega y los peaks estacionales. Que la dotación esté dimensionada con método. |
| **Innovaciones** | Que las cinco innovaciones sean pertinentes a la distribución de consumo masivo y a los problemas de Puelche, y no un catálogo de tecnologías de moda. Que la de arquitectura cite fuentes. |
| **Consolidación** | Que la propuesta sea internamente coherente: que la arquitectura sostenga el alcance, que la EDT contenga la arquitectura, que el cronograma refleje la EDT y que el costo derive de todo lo anterior. |

> **Una advertencia final del mandante.**
> En el acta del comité ejecutivo quedó consignado que la solución no puede suponer que el cliente va a cambiar. El almacenero de barrio no tiene internet, paga en efectivo y compra como ha comprado siempre. Una propuesta que resuelva elegantemente la operación asumiendo un cliente digital que no existe será superada por una más sobria que se haga cargo del cliente real.
> Lo mismo vale hacia adentro: en una empresa donde la gente lleva veinte o treinta años, la adopción no se decreta.

---

# TÍTULO VII — ANEXOS DEL CASO

## CAPÍTULO A · MAPA DE SISTEMAS Y FLUJOS DE INFORMACIÓN ACTUALES

Descripción de los flujos de información tal como ocurren hoy. La columna «cómo viaja» es la que explica buena parte de los problemas descritos en el Capítulo 7.

| Origen | Destino | Qué información | Cómo viaja hoy |
|---|---|---|---|
| Planilla de reposición | Compras | Sugerencia de compra por producto | Planilla del jefe de abastecimiento, con ajuste manual por temporada |
| Comercial | Compras | Promociones comprometidas | Correo, cuando se avisa |
| Compras | Proveedor | Orden de compra | Correo electrónico, en documento adjunto |
| Proveedor | Recepción | Aviso de despacho y guía | Correo en formatos distintos según proveedor; guía en papel con el camión |
| Recepción | Sistema de gestión | Cantidades recibidas y lote | Digitación posterior. El lote va en campo de texto libre, cuando se anota |
| Preventista | Sistema de gestión | Pedido del cliente | Aplicación de 2016, con envío diferido que a veces falla o duplica |
| Sistema de gestión | Crédito y cobranza | Pedido retenido por deuda | Revisión manual al día siguiente. El preventista no se entera |
| Sistema de gestión | Planificador de rutas | Listado de pedidos confirmados | Exportación a planilla de once hojas |
| Planificador de rutas | Bodega y conductores | Asignación de entregas y secuencia | Planilla impresa |
| Bodega | Preparador | Hoja de picking ordenada por ubicación | Papel y lápiz |
| Preparador | Oficina de bodega | Faltantes | Anotados a mano al pie de la hoja; la causa no se registra |
| Oficina de bodega | Sistema de gestión | Ajuste del pedido por faltantes | Digitación |
| Sistema de gestión | Facturación electrónica | Documento tributario | Integrado |
| Conductor | Cliente | Entrega y guía de despacho | Papel, firmada a mano |
| Cliente | Conductor | Rechazo, devolución y pago en efectivo | Anotación en la guía y en un cuaderno |
| Conductor | Oficina | Fajo de guías firmadas | Papel, al regreso. 1,1 % no llega o llega ilegible |
| Conductor | Caja | Rendición de efectivo | Conteo manual a la mañana siguiente |
| Termógrafo del camión | Planilla | Tres lecturas de temperatura por viaje | Anotadas a mano por el conductor |
| Cámaras del centro de distribución | Planilla | Dos lecturas por turno | Anotadas a mano |
| Plataforma de telemetría de terceros | Operaciones | Posición y velocidad de 42 camiones propios | Consulta manual en el portal del proveedor |
| Conteo cíclico | Sistema de gestión | Diferencias de inventario | Planilla impresa, ajuste al cierre del mes sin investigación de causa |
| Devoluciones | Jefe de bodega | Destino del producto devuelto | Decisión caso a caso, sin registro estructurado |
| Conductor | Cuaderno | Envases retornables entregados y recibidos | Anotación manual, sin consolidación |
| Sistema de gestión | Finanzas | Costo logístico por zona | Prorrateo con criterio de 2016 |

---

## CAPÍTULO B · CALENDARIO Y PERFIL OPERACIONAL DE REFERENCIA

### B.1 Perfil de un día hábil

| Tramo horario | Qué ocurre | Carga sobre la solución |
|---|---|---|
| **22:00 – 06:00** | Preparación de pedidos en el centro de distribución de Talca, en turno nocturno. | Peak sostenido de transacciones de picking. Es la ventana donde se juega el despacho del día. |
| **03:00 – 05:00** | Llegada del camión de línea a las plataformas de cross-docking y desconsolidación. | Operación en sitios con conectividad sólo por red móvil. |
| **05:30 – 07:00** | Carga y salida de 96 camiones. | Ventana crítica. Indisponibilidad cero. Peak de emisión de documentos y de asignación de rutas. |
| **07:00 – 19:00** | Reparto y entregas en ruta. | Registro en terreno, buena parte sin cobertura. Cobro en efectivo. |
| **08:00 – 18:00** | Recepción de proveedores en los centros de distribución. | Sin cita previa. Filas de hasta cinco horas en temporada alta. |
| **09:00 – 18:00** | Preventa en terreno: 62 personas, unas 2.600 visitas diarias. | Consultas de stock, crédito e historial. Toma de pedidos. |
| **15:00 – 18:30** | Planificación de las rutas del día siguiente. | Hoy manual. Depende de que los pedidos estén cerrados. |
| **17:00 – 20:00** | Regreso de la flota y sincronización de dispositivos. | Peak de sincronización tras un turno completo sin señal en rutas rurales. |
| **Mañana siguiente** | Rendición de efectivo en caja. | Conteo manual contra el listado de entregas del día anterior. |

### B.2 Estacionalidad y ventanas

| Período | Efecto | Consecuencia para el proyecto |
|---|---|---|
| **1 al 25 de septiembre** | Peak de Fiestas Patrias. El volumen diario casi se duplica: de ≈1.400 a ≈2.600 entregas. | Congelamiento total. Prohibido intervenir. Máxima exigencia sobre cualquier componente ya en producción. |
| **1 al 31 de diciembre** | Peak de Navidad y fin de año. | Segundo congelamiento total. |
| **Enero y febrero** | Baja de la demanda del canal tradicional y alza del food service en la costa. | Cambia el mix de rutas y de productos. Buen período para intervenir. |
| **Primeros tres días hábiles de cada mes** | Cierre comercial y contable. | Prohibido intervenir sistemas con impacto en facturación o inventario valorizado. |
| **Semana de pago quincenal y de fin de mes** | Alza de la venta del canal tradicional. | Peak menor, recurrente, que el dimensionamiento debe considerar. |
| **Invierno** | Caminos rurales en mal estado. Rutas más lentas. | Aumenta el tiempo sin cobertura y la duración del turno del repartidor. |
| **Sábado** | Operación hasta las 14:00 en el centro de distribución. Reparto en jornada reducida. | Ventana de intervención acotada. |
| **Domingo** | Sin operación de bodega ni de reparto. | Única ventana amplia de intervención semanal. |

---

## CAPÍTULO C · GLOSARIO DE LA INDUSTRIA

Vocabulario mínimo para leer este documento. No sustituye la investigación exigida en el numeral 16.2.

| Término | Significado |
|---|---|
| **Canal tradicional** | Almacenes de barrio, minimarkets y botillerías. Muchos clientes, pedidos pequeños, alta frecuencia y pago frecuentemente al contado. |
| **Canal moderno** | Cadenas de supermercados y grandes superficies. Pocos clientes, pedidos grandes, exigencias formales de integración y de ventana horaria. |
| **Food service** | Restaurantes, casinos, hoteles y servicios de alimentación. Sensibles a la frescura y a la puntualidad. |
| **Costo de servir** | Costo total de atender a un cliente: transporte, tiempo de descarga, preparación, visita de preventa, cobranza y reentregas. |
| **Cross-docking** | Operación en que la mercadería se recibe y se despacha sin almacenarse, consolidándose para su distribución final. |
| **Excursión térmica** | Salida de un producto de su rango de temperatura permitido, caracterizada por su magnitud y su duración. |
| **Fill rate** | Proporción del pedido que efectivamente se entrega. Puede medirse en líneas, en unidades o en valor, y no da lo mismo cuál se use. |
| **Guía de despacho** | Documento tributario que acompaña el traslado de la mercadería. En su versión electrónica tiene efectos legales y requiere acuse de recibo. |
| **Línea de pedido** | Cada producto distinto dentro de un pedido. Es la unidad natural para medir el esfuerzo de preparación. |
| **Logística inversa** | Flujo de retorno: devoluciones, envases retornables, productos vencidos y material de exhibición. |
| **Merma** | Pérdida de producto por vencimiento, daño, robo o error. Se expresa como porcentaje del valor del inventario o de la venta. |
| **OTIF** | On Time In Full. Entrega completa y a tiempo. Indicador central del servicio logístico; su definición exacta debe acordarse porque admite variantes. |
| **Perfect order** | Pedido entregado completo, a tiempo, sin daño y con la documentación correcta. Indicador más exigente que el OTIF. |
| **Picking** | Preparación de pedidos: recorrido por la bodega tomando los productos que componen cada pedido. |
| **Preventa** | Modalidad en que un vendedor toma el pedido en el local del cliente y la entrega se realiza en un viaje posterior. |
| **Autoventa** | Modalidad en que el vehículo lleva la mercadería y la venta y la entrega ocurren en el mismo acto. |
| **Quiebre de stock** | Situación en que un producto solicitado no está disponible. Puede detectarse en la preventa, en la preparación o en la entrega, y cada momento tiene un costo distinto. |
| **Ruta** | Conjunto ordenado de clientes que atiende un vehículo o un preventista en una jornada. |
| **Slotting** | Asignación de ubicaciones de almacenamiento a los productos según criterios de rotación, peso, volumen y compatibilidad. |
| **SKU** | Stock Keeping Unit. Unidad de mantenimiento de existencias: cada producto distinto que se administra por separado. |
| **Unidad logística** | Agrupación física identificable —pallet, canastillo, caja— que se mueve como una sola cosa y que puede identificarse individualmente. |
| **Ventana de entrega** | Franja horaria dentro de la cual el cliente acepta recibir. Cuanto más estrecha, más difícil de cumplir y más valiosa comercialmente. |
| **Conteo cíclico** | Verificación periódica y parcial del inventario, por posiciones, sin detener la operación. |
| **Retiro de producto** | Procedimiento de recuperación de un producto ya distribuido cuando se detecta un riesgo. Su eficacia depende íntegramente de la trazabilidad. |
| **Trazabilidad hacia atrás y hacia adelante** | Capacidad de saber de dónde vino un producto y a dónde fue. Ambas son exigibles y se apoyan en registros distintos. |
