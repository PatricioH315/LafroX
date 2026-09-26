# Supuestos y dimensionamiento — Caso 02 Logística

Este documento acompaña el dimensionamiento del apartado 4.2.6 y la memoria de cálculo del Anexo 4.B. Su función es separar las cifras literales del caso, los requisitos, las decisiones de diseño y los supuestos sobre el CLIENTE o su entorno. La memoria deriva cada resultado con unidades, perfil horario, sensibilidad y umbral de quiebre.

## 1. Cómo se clasifica cada cifra

Un **hecho** se cita y nunca se registra como supuesto. Un **requisito** proviene de las Bases Técnicas Transversales o del Capítulo 15. Un **parámetro de diseño** es una decisión que impone nuestra solución. Un **supuesto** completa una cifra que el caso calla y declara valor, fundamento, impacto y validación. Un **cálculo** se deriva de las entradas anteriores y pertenece a la memoria.

## 2. Hechos del caso utilizados

| Dato | Valor | Fuente |
|---|---:|---|
| Clientes, productos y proveedores | 14.200 clientes; 8.400 SKU; 180 proveedores | Caso, Tabla 2.2 |
| Pedidos, líneas y unidades | 31.000 pedidos/mes; 260.000 líneas/mes; 2,4 millones de unidades/mes | Caso, Tabla 2.2 |
| Entregas | ≈1.400 normales y ≈2.600 en septiembre | Caso, Tabla 14.1 |
| Viajes, kilómetros y documentos | ≈2.100 viajes/mes; ≈420.000 km/mes; ≈34.000 DTE/mes | Caso, Tabla 14.1 |
| Recepciones, pallets, conteos y devoluciones | 1.150; 14.500; 3.400; ≈900 mensuales | Caso, Tabla 14.1 |
| Canal de preventa | 62 preventistas; unas 2.600 visitas diarias | Caso, Anexo B.1 y Cap. 8, entrevista |
| Flota | 42 camiones propios y 54 de terceros; 18 y 10 refrigerados | Caso, Tabla 2.3 |
| Personas de operación | 640 de personal propio; ≈160 conductores de terceros; 184 de oficina | Caso, Tabla 2.4 |
| Preparación nocturna | 120 personas en el turno de noche de Talca | Caso, Cap. 8, entrevista a la jefa de bodega de Talca |
| Centros y superficies | Talca 18.000 m²; Concepción 9.000 m²; tres plataformas de cross-docking | Caso, Tabla 2.3 y Cap. 3 |
| Inventario y rotación | 11.400 posiciones; 3.400 posiciones contadas al mes; rotación 11,4 veces/año | Caso, Tabla 2.2 y Tabla 2.3 |
| Cadena de frío | Cámara de congelado de Talca a −22 °C; Concepción no tiene congelado | Caso, Tabla 2.3 y Cap. 3 |
| Ventanas operacionales | Preparación 22:00–06:00; cross-docking 03:00–05:00; despacho 05:30–07:00; reparto 07:00–19:00; recepción 08:00–18:00; preventa 09:00–18:00; sincronización 17:00–20:00 | Caso, Anexo B.1 |
| Peak | Del 1 al 25 de septiembre; septiembre multiplica la operación; es el período de mayor exigencia | Caso, Anexo B.2 y Cap. 15 |
| Ruta exigente | 34 clientes | Caso, Cap. 8, entrevista al conductor de la ruta Cauquenes |
| Canal tradicional | La mayoría de los almacenes no tiene internet ni dispositivo; food service y cadenas suman 2.600 clientes habituales | Caso, Cap. 6 y Tabla 2.2 |
| Mensajería actual | EDI actual cero y proveedores sin mensajería estructurada | Caso, Cap. 7.3 |
| Termógrafos | 18 camiones propios y 10 refrigerados de terceros | Caso, Tabla 2.3 |

Los 28 puntos de cámara no se presentan como hecho: son un parámetro de diseño del apartado B-01.

## 3. Requisitos que se aplican

El centro de distribución debe operar 24 horas sin enlace; el dispositivo de terreno debe sostener un turno completo de 14 horas sin cobertura; cada dispositivo debe sincronizar en diez minutos y el centro debe drenar en dos horas: Caso, Cap. 15. La prueba de carga es 1,5 veces el peak declarado y la capacidad debe cubrir tres veces la volumetría inicial: BTT RT-09.06 y BTT RT-09.03.

La ventana de despacho 05:30–07:00 es protegida y no admite indisponibilidad. Los umbrales de respuesta se observan en percentil 95 conforme a BTT 9.1 y al Caso, Cap. 15. La retención es de seis años para evidencia y DTE, cinco años para temperatura, cinco años o más para trazabilidad disponible y doce meses para geolocalización: Caso, Cap. 15.

La mesa atiende de 04:00 a 22:00 de lunes a sábado y opera 24×7 durante septiembre y diciembre; Erlang C y el abandono máximo de 5 % se responden con BTT RT-21.06. La redundancia N+1 y el 10 % de reserva de equipos se responden con BTT RT-03.14, BTT RT-08.03 y BTT 8.4.

El catálogo del apartado 4.1 contiene INT-01 a INT-15. La dimensión 11 cuenta sólo esas integraciones: portal y llamadas internas a la API son carga de aplicación, no mensajes de integración. La posición y la temperatura cuentan sólo cuando su integración está en ese catálogo.

## 4. Supuestos

**S-47. Un pedido genera una entrega.** El cociente 31.000 pedidos/mes ÷ 1.400 entregas/día produce 22,14 días equivalentes y se controla con 2.100 viajes ÷ 96 camiones = 21,88 días. Si no se cumple, cambian evidencia, mensajes y almacenamiento. Se valida conciliando pedidos, guías y entregas del ERP en la Etapa 1. Se usa en las dimensiones 1–3, 7–8, 11 y 13–14.

**S-48. Septiembre escala los flujos de volumen y diciembre no lo supera.** El factor 2.600 ÷ 1.400 = 1,857 es un cálculo; el supuesto es que pedidos, líneas, DTE, evidencia y mensajes crecen juntos porque el caso dice que en septiembre todo se multiplica y lo identifica como la mayor exigencia. Si diciembre supera septiembre, falta capacidad. Se valida con la serie mensual antes de cada congelamiento. Se usa en las dimensiones 1–3 y 7–12.

**S-49. Talca prepara dos tercios de las líneas y Concepción un tercio.** Talca duplica la superficie de Concepción y además abastece los tres cross-docking y parte del surtido de Concepción; la proporción de superficie es, por tanto, un piso razonable, no una medición. Si Concepción prepara más, aumentan su WMS, terminales y enlace. Se valida con la exportación de líneas por centro durante la Etapa 1. Se usa en las dimensiones 1, 7, 12 y en la capacidad local.

**S-50. Concepción tiene 60 personas concurrentes en la preparación nocturna.** El caso informa 120 en Talca y describe Concepción como un centro menor y sin congelado; se adopta la mitad por escala. Si la dotación real es mayor, faltan terminales y capacidad local. Se valida con la dotación nominal y observación de turnos. Se usa en las dimensiones 4–6 y 16.

**S-51. La hora cargada duplica la tasa media de su propia ventana.** El caso concentra el frío al final del turno y el despacho y la sincronización tienen ventanas estrechas. El factor se aplica una sola vez a la hora cargada de preparación, cross-docking, despacho, reparto, recepción, preventa, sincronización, portal y guías; para preventa y portal se ubica a las 12:00 por convención y el máximo no depende de la hora elegida. Si es mayor, el límite puede ser WMS, Wi-Fi, ERP, enlace o nube. Se valida con métricas horarias, percentil 95 y BTT RT-09.06. Se usa en las dimensiones 1–3, 5, 11–12 y en la capacidad.

**S-52. La cadena principal no supera 11 % de los pedidos en el escenario EDI 2029.** Pesa 11 % de la venta, pero sus pedidos son mayores que el promedio; tomar 11 % de los pedidos es una cota conservadora para los mensajes del flujo EDI. Si la mezcla cambia, aumentan las colas. Se valida con el contrato y la certificación del intercambio. Se usa en las dimensiones 11–12.

**S-53. La mesa recibe 2,5 contactos por persona interna al mes, con 10 minutos de atención media y 25 % de contactos en la hora cargada.** El caso no entrega una tasa histórica; el escenario se calcula por Erlang C, repartiendo el 75 % restante en las otras 17 horas. Si la tasa o la duración aumenta, se requieren más personas. Se valida con tickets y recalibración mensual. Se usa en las dimensiones 15–16.

**S-54. Los diez camiones refrigerados de terceros pueden instrumentarse por acuerdo.** La exigencia de cadena de frío permanece, pero el caso indica que esos vehículos pertenecen a transportistas. Si no hay acuerdo, aumenta el registro manual. Se valida con contratos y certificados antes de producción. Se usa en las dimensiones 9, 11 y 12.

**S-55. La API de telemetría de los 42 camiones propios permanece disponible.** El caso menciona una fuente existente, pero no entrega su contrato ni rendimiento. Si cambia, la posición automática se degrada a ruta planificada. Se valida con levantamiento contractual y prueba técnica. Se usa en las dimensiones 9, 11 y 12.

## 5. Parámetros de diseño

| Parámetro | Valor | Por qué y dónde se impone |
|---|---:|---|
| Operaciones de picking | 2 por línea | Lectura y confirmación del flujo del apartado 4.1; se confirma con RT-09.06. |
| Operaciones de preventa | 2 por visita y 1 por línea del pedido | La app consulta stock y crédito y registra las líneas del pedido; se mide por contrato y carga. |
| Operaciones de entrega | 5 por entrega | Estado, evidencia, documento, cobro y cierre del flujo del apartado 4.1. |
| Operaciones de cross-docking | 4 por entrega | Recepción, escaneo, desconsolidación y despacho; cada plataforma se prueba con la cota declarada. |
| Factor horario | S-51 = 2,0 | Sólo en la hora cargada de cada ventana, nunca sobre el total diario. |
| Portal | 60 solicitudes por sesión de 10 minutos; sensibilidad de 120 solicitudes por sesión | 2.600 sesiones diarias repartidas entre 09:00 y 18:00; S-51 duplica sólo la hora cargada. Los 15 minutos se usan para la concurrencia de la sensibilidad, no para concentrar las sesiones. |
| Cross-docking | 2 personas con escáner por plataforma; 6 en total | Cota operacional para las tres plataformas y su carga Wi-Fi; se confirma con el diseño de escáneres. |
| Evidencia | Firma ≤30 KB; fotografía ≤200 KB; una adicional en devolución o rechazo | La App de reparto comprime antes de guardar; se mide en QA. |
| Datos locales de terreno | 2 MB por dispositivo | Ruta, maestros acotados y cola local; se contrasta con la ruta de 34 clientes. |
| Tamaños de registro | 1 KB por línea o evento; 0,5 KB por movimiento | Base inicial con sensibilidad de ±50 % en QA. |
| Horizonte local WMS | 4 meses | Cubre el ciclo de conteo de 11.400 ÷ 3.400 = 3,35 meses y la rotación de 11,4 veces/año; incluye movimientos de conciliación y maestros. |
| Lotes presentes | 3 por SKU | Reserva para coexistencia de lotes y FEFO; se sustituye por el inventario real en la Etapa 1. |
| Plataforma | 50 ms de CPU por solicitud; 64 MB por proceso; 150 ms de permanencia | Valores de diseño que se perfilan y se verifican en BTT RT-09.06; el percentil 95 se evalúa conforme a BTT 9.1. |
| Observabilidad | 250 MB por nodo/día; 1.000 eventos por nodo/día | ADOT conserva registros de error, métricas cada 60 s y 10 % de trazas; se controla por nodo. |
| Temperatura | 28 puntos de cámara cada 5 minutos; 145 bytes y 1 mensaje por lectura | Los puntos de cámara son diseño B-01; los 28 termógrafos del caso transmiten sólo de 05:30 a 19:00. |
| Posición | 145 bytes por evento; un evento cada 30 segundos durante 12 horas de ruta | El flujo de 42 camiones propios produce ≈22.075.200 eventos/año; se comprueba en el perfil de telemetría. |
| Actualizaciones | App ≤100 MB; sistema operativo 2 GB por equipo | Kotlin nativo, SQLite y sin multimedia; el sistema se reparte en tandas trimestrales dominicales. |
| Oficina | 5 MB por persona/hora | Cota para la hora cargada de 184 personas; no se agrega al drenaje durante un corte. |
| Base e hipervisor | Factor 2 de índices y auditoría; 15 % de CPU y 2 GB RAM por nodo | La base local se expresa en disco lógico; N+1 se calcula sólo para el clúster de Talca. |
| Jornada 24×7 | 42 horas semanales; 40 desde el 26-04-2028 | Ley 21.561, reducción gradual; se revisa antes de contratar. |

## 6. Decisiones que reemplazan cifras sin fundamento

Se eliminan los días hábiles anuales, los 16 días del peak, la quincena más 15 %, diciembre 1,5× y los ritmos humanos de 6 y 8 segundos. Los totales anuales son 12 × el volumen mensual; los TPS salen del perfil de 24 horas.

Se eliminan la adopción portal 20 %/5 %, el EDI de 1.000 mensajes diarios, 0,10 GB diarios por cross-docking y 0,20 Mbps de sincronización. El portal usa las 2.600 sesiones habituales y su cota extrema; la sensibilidad de 120 solicitudes por sesión se calcula con las sesiones repartidas en la hora. La dimensión 11 conserva INT-01 a INT-15; el drenaje se calcula sin oficina.

Se reemplaza el horizonte local de dos días por cuatro meses, la dimensión 6 por 158 dispositivos de terreno simultáneos y la cámara de 28 por un parámetro de diseño. La migración de trazabilidad usa recepciones con campo de lote: 1.150 recepciones/mes × 60 meses × 20 líneas por recepción. El 41 % sin lote del retiro de marzo se usa sólo para saneamiento de calidad.

## 7. Supuestos críticos y umbrales de quiebre

El máximo horario normal es 12,30 TPS a las 12:00 y el peak de septiembre es 14,66 TPS a las 12:00; RT-09.06 exige 21,99 TPS. La cota extrema aislada del portal es 43,33 solicitudes/s y, sumada a la nube, requiere cuatro tareas Fargate. Con 120 solicitudes por sesión, las sesiones repartidas dan 19,27 solicitudes/s en régimen y 86,67 en la cota extrema; con la nube resultan 21,93 y 91,70 solicitudes/s, que requieren dos y siete tareas, bajo el techo de ocho.

La peor ruta requiere 0,13 Mbps efectivos por dispositivo. En la hora punta de llegada regresan 64 camiones y la Wi-Fi y el enlace de Talca deben absorber 1,40 Mbps; el agregado de la ventana es 0,70 Mbps. El peor caso de Talca es 5,30 Mbps frente a D-03 de 20 Mbps y el drenaje aislado usa 31,89 % de D-04 de 5 Mbps.

La emisión de 2.852 guías admite 9,47 segundos por guía repartidas en la noche, 4,42 segundos en las últimas 3,5 horas y 1,89 segundos si se concentra en 05:30–07:00. El ERP sin interfaces documentadas es el primer candidato a cuello de botella; el diseño emite la guía al confirmar la carga y conserva al ERP como único emisor.

## 8. Ajustes necesarios en el registro vigente

- **S-17:** separar camiones de conductores; los equipos de reparto se asignan por 96 camiones, no por el número de personas.
- **S-24:** declarar EDI actual cero y usar en 2029 la cota de 11 % de pedidos con el flujo del apartado 4.1.
- **S-25:** trasladar las 16 dimensiones a la memoria, con perfil horario, unidad, sensibilidad y umbral.
- **S-26:** declarar la migración en **32,11 GB**, con sensibilidad **30,73–33,49 GB**, limitada a recepciones con lote para trazabilidad histórica.
- **S-28:** dimensionar la mesa con 2.000 contactos/mes, Erlang C, 7 personas de mesa y 8 personas NOC/SOC a 42 horas; en septiembre y diciembre se agregan posiciones fuera del horario normal para la cobertura 24×7.
- **S-39:** separar continuidad, N+1 y resultados de pruebas; no convertir una capacidad de diseño en evidencia de servicio.
- **S-40:** conservar telemetría de los 42 camiones propios y condicionar la de terceros a S-54.

## 9. Resumen final de supuestos

| Código | Qué suponemos | Cuándo se valida |
|---|---|---|
| S-47 | Un pedido genera una entrega | Conciliación ERP–guías–entregas en Etapa 1 |
| S-48 | Septiembre escala los flujos y diciembre no lo supera | Serie mensual antes del congelamiento |
| S-49 | Talca prepara 2/3 y Concepción 1/3 | Exportación WMS por centro |
| S-50 | Concepción tiene 60 personas nocturnas | Dotación y observación de turnos |
| S-51 | La hora cargada duplica su ventana | Métricas horarias, percentil 95 y RT-09.06 |
| S-52 | La cadena principal no supera 11 % de pedidos | Contrato y certificación EDI |
| S-53 | Mesa: 2,5 contactos, 10 minutos y 25 % en la hora punta | Tickets y recalibración mensual |
| S-54 | Se puede instrumentar la flota refrigerada de terceros | Contratos y certificados |
| S-55 | Sigue disponible la API de telemetría propia | Prueba contractual y técnica |
