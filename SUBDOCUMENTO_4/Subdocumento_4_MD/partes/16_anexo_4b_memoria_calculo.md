<!-- Fuente: Subdocumento_4_LateX/04_arquitectura_fisica/partes/16_anexo_4b_memoria_calculo.tex — conversión fiel; editar el .tex y regenerar -->

**Metadatos de portada**

- Documento: Propuesta Técnica
- Subtítulo: Anexo 4.B --- Memoria de cálculo del dimensionamiento
- Alcance: Subdocumento 4 --- Anexos
- Formulario: Anexo 4.B
- Fecha: 05 de octubre de 2026
- Versión: 2.0

# Anexo 4.B. Memoria de cálculo del dimensionamiento

{4.B.}
{anexo4B.}
{0}

<a id="sec:anexo-4b-entradas"></a>
## 4.B.1 Entradas, requisitos, parámetros y supuestos

Este anexo sustenta el dimensionamiento del apartado 4.2.6 y entrega la memoria de cálculo que respalda el Formulario T-11. Su alcance comprende las dieciséis dimensiones, la capacidad por sitio, la nube, los enlaces, la migración, el crecimiento y las pruebas de aceptación. Los supuestos de volumen, concurrencia y crecimiento que exige el Formulario T-7 (SV-01 a SV-07) se declaran en este anexo; los que fijan las cantidades de implementos (S-28 y S-30 a S-41) se registran en el Subdocumento 3.

La Tabla [29](#tab:anexo-4b-hechos) concentra los hechos que alimentan las fórmulas y conserva su cita en la forma de la propuesta.

<a id="tab:anexo-4b-hechos"></a>
**Tabla 29.** Hechos del caso utilizados
| Dato | Valor | Fuente |
| --- | --- | --- |
| Volumetría comercial | 31.000 pedidos; 260.000 líneas; 2,4 millones de unidades mensuales | Bases Técnicas del caso, Cap. 2, p. 4 |
| Entregas | ≈ 1.400 normales y ≈ 2.600 en septiembre | Bases Técnicas del caso, Cap. 14, p. 24 |
| Documentos tributarios electrónicos (DTE) y transporte | ≈ 34.000 documentos tributarios electrónicos, ≈ 2.100 viajes de camión y ≈ 420.000 km recorridos al mes | Bases Técnicas del caso, Cap. 14, p. 24 |
| Operación de terreno | 62 preventistas; 42 camiones propios; 54 de terceros; 184 personas de administración, comercial y soporte | Bases Técnicas del caso, Cap. 2, p. 5 |
| Bodegas | 120 personas nocturnas en Talca; 18.000 m² y 9.000 m² | Bases Técnicas del caso, Cap. 8, p. 14, entrevista; Bases Técnicas del caso, Cap. 2, p. 5 |
| Ventanas | Preparación 22:00–06:00; despacho 05:30–07:00; sincronización 17:00–20:00 | Bases Técnicas del caso, Anexo B, p. 38 |
| Ruta y frío | 34 clientes en una ruta máximo actualmente; 18 camiones propios y 10 de terceros con equipo de frío; Talca a {-}22 °C | Bases Técnicas del caso, Cap. 8, p. 16, entrevista al conductor; Bases Técnicas del caso, Cap. 2, p. 5 |

La Tabla [30](#tab:anexo-4b-parametros) fija los valores que impone la propuesta. Un valor de diseño se confirma mediante perfilado, QA o prueba de carga, pero no se presenta como un hecho del CLIENTE.

<a id="tab:anexo-4b-parametros"></a>
**Tabla 30.** Parámetros de diseño
| Parámetro | Valor | Justificación y uso | Confirmación |
| --- | --- | --- | --- |
| Operaciones de flujo | 2 por línea: lectura de ubicación o lote y confirmación; 5 por entrega: estado, evidencia, documento, cobro y cierre; 4 por cross-docking: recepción, escaneo, desconsolidación y despacho | Flujo del apartado 4.1 | RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21) |
| Preventa | 2 consultas por visita y 1 operación por línea | Stock, crédito y pedido | Contrato y carga |
| Concentración horaria | SV-04 = 2,0, sólo en la hora cargada | Frío, despacho, reparto y sincronización | Perfil de 24 h |
| Portal | 60 solicitudes por sesión de 10 minutos; sensibilidad de 120 por sesión | Cota de sesiones; las sesiones se reparten en la hora y 15 minutos sólo determinan concurrencia | RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21) |
| Registro y movimiento | 1 KB; 0,5 KB | Almacenamiento y base local; sensibilidad ±50 % | QA |
| Base local | 4 meses más maestros y lotes presentes | Ciclo de conteo y conciliación | Levantamiento WMS |
| Evidencia | 30 KB de firma; 200 KB de foto; una adicional en devolución | Compresión en App de reparto | QA |
| Plataforma | 50 ms de CPU por solicitud; 64 MB por proceso; 150 ms de permanencia | Capacidad de VM y nube; se perfila y verifica en la prueba de carga | RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21) y Bases Técnicas Transversales, Cap. 9, p. 21 |
| Observabilidad | 250 MB y 1.000 eventos por nodo/día | ADOT: registros, métricas y trazas | Operación |
| Actualizaciones | App ≤100 MB; sistema operativo 2 GB | Tandas dominicales sin bodega ni reparto | Anexo B.2 |

La Tabla [31](#tab:anexo-4b-supuestos) declara el fundamento, impacto y validación de cada supuesto. Ninguno reemplaza un dato literal del caso.

<a id="tab:anexo-4b-supuestos"></a>
**Tabla 31.** Supuestos de volumen
| Código | Qué suponemos y por qué | Si resulta equivocado | Cómo y cuándo se valida |
| --- | --- | --- | --- |
| SV-01 | Un pedido genera una entrega; 31.000/1.400 produce 22,14 días y concuerda con 2.100/96. | Cambian evidencia, mensajes y almacenamiento. | Conciliación ERP–guías–entregas en Etapa 1. |
| SV-02 | Septiembre escala los flujos de volumen y diciembre no supera su exigencia; el factor 1,857 es cálculo. | Falta capacidad en el nuevo peak. | Serie mensual antes del congelamiento. |
| SV-03 | Talca prepara 2/3 y Concepción 1/3 por superficies y función de abastecimiento adicional. | Faltan terminales, WMS o enlace en el centro subestimado. | Exportación WMS por centro. |
| SV-04 | La hora cargada duplica la media de su propia ventana, una sola vez. | El cuello se traslada a WMS, ERP, Wi-Fi o nube. | Perfil horario y RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21). |
| SV-05 | La cadena principal no supera 11 % de los pedidos en el escenario EDI 2029; el caso informa que pesa 11 % de la venta, y como sus pedidos son mayores que el promedio, tomar 11 % de los pedidos es una cota holgada. | Aumentan colas EDI. | Contrato y certificación del intercambio. |
| SV-06 | 2,5 contactos por persona/mes, 10 minutos y 25 % en hora cargada. | Se requieren más personas. | Tickets y Erlang C mensual. |
| SV-07 | La API de telemetría de los camiones propios continúa disponible. | Posición automática se degrada a ruta planificada. | Prueba contractual y técnica. |

<a id="sec:anexo-4b-dimensiones-1-3"></a>
## 4.B.2 Dimensiones 1–3: transacciones por segundo

Se calcula el máximo horario de cada lugar para no sumar ventanas que no coinciden. Los días equivalentes son 31.000 ÷ 1.400 = 22,14 días y el control cruzado es 2.100 ÷ 96 = 21,88 días. El factor de septiembre es 2.600 ÷ 1.400 = 1,857.

La preparación normal de Talca se calcula como 11.742 líneas por noche × 2 operaciones × 2/3 ÷ 28.800 segundos = 0,54 TPS de media; la hora cargada de SV-04 alcanza 1,09 TPS. A las 05:00 el despacho local agrega su flujo y el máximo horario del WMS de Talca es 1,64 TPS normal y 3,02 TPS en septiembre.

La nube suma preventa, reparto, recepción, trazabilidad, guías, sincronización y el escenario EDI. El portal queda separado: 2.600 ÷ 9 × 2 por SV-04 = 578 sesiones en la hora cargada; 578 × 60 ÷ 3.600 = 9,63 solicitudes/s y 578 × 10 ÷ 60 = 96,30 concurrentes. La cota extrema es 2.600 × 60 ÷ 3.600 = 43,33 solicitudes/s y 433,33 concurrentes. Las 2.600 sesiones diarias del portal son un parámetro de diseño: se toma una sesión por cada cliente de food service y de cadenas, 2.100 + 500 = 2.600 (Bases Técnicas del caso, Cap. 2, p. 4). No son las 2.600 visitas diarias de preventa (Bases Técnicas del caso, Anexo B, p. 38); que las dos cifras coincidan es casualidad.

La dimensión 1 es **12,30 TPS a las 12:00** en régimen normal. La dimensión 2 es **1,68 TPS normal y 3,05 TPS peak** en la cota de despacho con guías. La dimensión 3 es **14,66 TPS a las 12:00** en septiembre. RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21) es 1,5 × 14,66 = **21,99 TPS**.

La Tabla [32](#tab:anexo-4b-horario) conserva el perfil hora por hora que produce esos máximos.

<a id="tab:anexo-4b-horario"></a>
**Tabla 32.** Perfil horario por lugar de proceso
| Hora | Talca N/P | Concepción N/P |  | Nube N/P | Portal N/P | Total N/P |
| --- | --- | --- | --- | --- | --- | --- |
| 00:00 | 0,54 / 1,01 | 0,27 / 0,50 | 0,00 / 0,00 | 0,74 / 1,37 | 0,00 / 0,00 | 1,55 / 2,88 |
| 01:00 | 0,54 / 1,01 | 0,27 / 0,50 | 0,00 / 0,00 | 0,74 / 1,37 | 0,00 / 0,00 | 1,55 / 2,88 |
| 02:00 | 0,54 / 1,01 | 0,27 / 0,50 | 0,00 / 0,00 | 0,74 / 1,37 | 0,00 / 0,00 | 1,55 / 2,88 |
| 03:00 | 0,54 / 1,01 | 0,27 / 0,50 | 0,78 / 1,44 | 0,74 / 1,37 | 0,00 / 0,00 | 2,33 / 4,33 |
| 04:00 | 0,54 / 1,01 | 0,27 / 0,50 | 1,56 / 2,89 | 0,74 / 1,37 | 0,00 / 0,00 | 3,11 / 5,77 |
| 05:00 | 1,64 / 3,02 | 0,54 / 1,01 | 0,00 / 0,00 | 0,79 / 1,47 | 0,00 / 0,00 | 2,98 / 5,50 |
| 06:00 | 1,11 / 2,00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,68 / 1,26 | 0,00 / 0,00 | 1,79 / 3,26 |
| 07:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,84 / 1,56 | 0,00 / 0,00 | 0,84 / 1,56 |
| 08:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,84 / 1,57 | 0,00 / 0,00 | 0,84 / 1,57 |
| 09:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 1,68 / 3,15 | 4,81 / 4,81 | 6,49 / 7,96 |
| 10:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 1,68 / 3,15 | 4,81 / 4,81 | 6,49 / 7,97 |
| 11:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 1,68 / 3,15 | 4,81 / 4,81 | 6,49 / 7,96 |
| 12:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 2,67 / 5,03 | 9,63 / 9,63 | 12,30 / 14,66 |
| 13:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 1,68 / 3,15 | 4,81 / 4,81 | 6,49 / 7,96 |
| 14:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 1,68 / 3,15 | 4,81 / 4,81 | 6,49 / 7,96 |
| 15:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 1,68 / 3,15 | 4,81 / 4,81 | 6,49 / 7,96 |
| 16:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 1,68 / 3,15 | 4,81 / 4,81 | 6,49 / 7,96 |
| 17:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 2,45 / 4,59 | 4,81 / 4,81 | 7,27 / 9,41 |
| 18:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 2,40 / 4,45 | 0,00 / 0,00 | 2,40 / 4,45 |
| 19:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 1,46 / 2,71 | 0,00 / 0,00 | 1,46 / 2,71 |
| 20:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,68 / 1,26 | 0,00 / 0,00 | 0,68 / 1,26 |
| 21:00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,68 / 1,26 | 0,00 / 0,00 | 0,68 / 1,26 |
| 22:00 | 0,54 / 1,01 | 0,27 / 0,50 | 0,00 / 0,00 | 0,74 / 1,37 | 0,00 / 0,00 | 1,55 / 2,88 |
| 23:00 | 0,54 / 1,01 | 0,27 / 0,50 | 0,00 / 0,00 | 0,74 / 1,37 | 0,00 / 0,00 | 1,55 / 2,88 |

La fila de las 12:00 gobierna los TPS totales porque coincide la hora cargada de preventa, reparto y portal. La hora de preparación conserva la mayor carga local de WMS, pero no la mayor suma de lugares.

<a id="sec:anexo-4b-dimensiones-4-6"></a>
## 4.B.3 Dimensiones 4–6: personas, concurrencia y dispositivos

La dimensión 4 es (640 + 160) + 14.200 + 180 = **15.180 personas o entidades**. La dimensión 5 toma el mayor resultado entre ventanas: noche 120 + 60 (S-39) + 6 (S-35) = 186; despacho 96; día sin portal 62 + 96 + 184 = 342; portal en régimen 342 + 96,30 = **438,30**; portal extremo 342 + 433,33 = **775,33**. La dimensión 6 es 62 + 96 = **158 dispositivos de terreno en operación simultánea**.

El parque separado de la dimensión 6 se distribuye así:

- Bodega: 132 terminales en Talca, 22 de ellos para congelado, y 66 en Concepción.
- Terreno: 69 terminales de preventa, 106 de reparto, 106 impresoras y 106 terminales de pago.
- Cross-docking y frío: 7 terminales de cross-docking y 31 termógrafos.

Cada cantidad aplica los supuestos S-28 y S-30 a S-41, registrados en el Subdocumento 3, y la reserva del 10 % del parque de cada tipo, redondeada hacia arriba, conforme a la tabla de repuestos de las Bases Técnicas Transversales (Cap. 8, p. 19):

- Equipos de reparto (S-30): 96 camiones + 10 de reserva = 106 de cada dispositivo. A tres años (S-31), los viajes crecen 2.400 ÷ 2.100 = 1,143, es decir, 14,3 %; la flota llega a 96 × 1,143 = 109,7, unos 110 camiones, y el parque a 110 + 11 = 121, es decir, 15 unidades más de cada dispositivo.
- Terminales de preventa (S-32): 62 + 7 = 69. A tres años, 70 preventistas, un 12,9 % más, y 70 + 7 = 77, es decir, 8 más.
- Terminales de bodega: se comparten entre turnos (RT-12.11; Bases Técnicas del caso, Cap. 15, p. 27), sin personal de carga adicional (S-33), de modo que los fija el turno nocturno: 120 preparadores en Talca y 60 en Concepción (S-39). En Talca, 20 son de la cuadrilla de congelado (S-34): los productos de frío son 1.100 ÷ 8.400 = 13,1 % del surtido y el congelado ocupa 400 ÷ 1.300 = 30,8 % del área fría, de modo que el congelado es cerca de 13,1 % × 30,8 % = 4,0 % de las líneas; 120 personas × 8 h = 960 horas-persona, cuyo 4,0 % son 38,4 horas, concentradas en las últimas 2 horas del turno: 38,4 ÷ 2 = 19,2, unas 20 personas. Talca suma 20 + 2 de congelado y 100 + 10 estándar, Concepción 60 + 6, y los cross-docking 6 + 1 (S-35): 205 en total. A tres años (S-32), la dotación de los centros de distribución crece 350 ÷ 310 = 12,9 %: Talca llega a 23 + 3 de congelado y 113 + 12 estándar, y Concepción a 68 + 7; con los 7 de los cross-docking, el parque llega a 233, es decir, 28 más.
- Termógrafos: 28 + 3 = 31, para los 18 camiones con frío propios y los 10 de transportistas (S-28), sin compra por crecimiento (S-38).

<a id="sec:anexo-4b-dimensiones-7-10"></a>
## 4.B.4 Dimensiones 7–10: almacenamiento, retención y migración

El almacenamiento transaccional se calcula con 1.300.000 eventos = 260.000 líneas × 5, 520.000 operaciones = 260.000 líneas × 2, 155.000 operaciones = 31.000 pedidos × 5 y 279.050 movimientos = 260.000 líneas + 14.500 pallets + 3.400 conteos + 1.150 recepciones. Por tanto, ((1.300.000 + 520.000 + 155.000) × 1 KB + 279.050 × 0,5 KB) × 2 × 12 = **50,75 GB/año** y seis años acumulan **304,49 GB** como cota de retención. La evidencia es 30 KB + 200 KB × (1 + 900 ÷ 31.000) = **235,81 KB por entrega** y genera **87,72 GB/año**; en el mes peak alcanza 13,58 GB.

La temperatura separa cámaras y camiones: 21 puntos instalados × 288 lecturas/día = 6.048 lecturas de cámara, con la cámara de Concepción estimada por S-37, y 28 termógrafos × 162 lecturas/día entre 05:30 y 19:00 = 4.536 lecturas de camión; el total es 10.584 mensajes/día. Con 145 bytes por lectura, son 0,56 GB/año crudos, 0,14 GB/año almacenados con factor 0,25 y 2,80 GB crudos en cinco años. La posición produce 42 camiones × 12 h × 120 eventos/h × 365 = 22.075.200 eventos/año; se cuentan los 365 días como cota, aunque el domingo no hay reparto; con 145 bytes son 3,20 GB crudos y 0,80 GB almacenados en 12 meses. Son filas separadas porque sus retenciones son distintas.

La dimensión 10 se estima por dominio:

- Maestros completos: 34.180 KB.
- Ventas y pedidos: 3 años y 10.476.000 KB.
- Inventario y movimientos: 2 años y 3.348.600 KB.
- Recepciones con campo de lote: 5 años y 1.380.000 KB.
- Cuentas por cobrar: 2 años y 816.000 KB.

La suma de 16.054.780 KB × 2 ÷ 1.000.000 = **32,11 GB**. Con 10 o 30 líneas por recepción, el intervalo es **30,73–33,49 GB**. No se multiplican eventos históricos de trazabilidad: el caso declara que no existe una forma consultable. El 41 % sin lote sólo orienta el saneamiento.

<a id="sec:anexo-4b-dimensiones-11-12"></a>
## 4.B.5 Dimensiones 11–12: integraciones, mensajes y enlaces

La dimensión 11 cuenta los quince contratos INT-01 a INT-15 del apartado 4.1. La Tabla [33](#tab:anexo-4b-integraciones) deja el volumen por integración; las solicitudes del portal y las llamadas internas no aparecen.

<a id="tab:anexo-4b-integraciones"></a>
**Tabla 33.** Mensajes por integración
| Integración | Normal/día | Peak/día | Origen del volumen |
| --- | --- | --- | --- |
| INT-01 Pedido preventa y consulta | 1.400 | 2.600 | 1.400 × 1; 2.600 × 1, por SV-01 |
| INT-02 Entrega, POD y cobro | 7.000 | 13.000 | 1.400 × 5; 2.600 × 5 |
| INT-03 Eventos de bodega a nube | 58.710 | 109.032 | 260.000 ÷ 22,14 × 5; peak × 1,857 |
| INT-04 Detalle cross-docking a Talca | 5.600 | 10.400 | 1.400 × 4; cota de una plataforma |
| INT-05 Eventos de temperatura | 10.584 | 10.584 | 6.048 + 4.536 lecturas/día |
| INT-06 ERP 2017 | 2.025 | 3.762 | 1.400 + 1.150 ÷ 22,14 + 900 ÷ 22,14 + 11.800 ÷ 22,14; peak × 1,857 |
| INT-07 DTE/SII | 3.071 | 5.703 | 34.000 ÷ 22,14 × 2; peak × 1,857 |
| INT-08 Cadenas modernas EDI | 0 | 1.144 | 0 actual; 2.600 × 11 % × 4 |
| INT-09 Pasarela de pago | 533 | 990 | 11.800 ÷ 22,14; peak × 1,857 |
| INT-10 Mapas y geocodificación | 96 | 96 | 96 camiones × 1 |
| INT-11 Avisos al cliente | 2.800 | 5.200 | 1.400 × 2; 2.600 × 2 |
| INT-12 Cambios de datos a réplica | 12.602 | 23.404 | 279.050 ÷ 22,14; peak × 1,857 |
| INT-13 Identidad a sitio | 760 | 760 | 380 dispositivos × 2 |
| INT-14 Métricas y trazas | 10.000 | 10.000 | 10 nodos × 1.000 |
| INT-15 Telemetría existente | 60.480 | 60.480 | 42 × 12 × 120 |
| **Total** | **175.661** | **257.155** | **15 integraciones** |

Para la dimensión 12, el drenaje se obtiene sumando los aportes acumulados en 24 horas y dividiendo por 2 horas:

- Aportes en Talca: los cambios de 0,041 GB/día viajan como WAL, que no se suma aparte: WAL = 3 × 0,041 = 0,123 GB/día; broker = 0,5 × 0,041 = 0,020 GB/día; telemetría = 10.584 × 145 ÷ 1.000.000.000 ÷ 2 = 0,001 GB/día; observabilidad = 5 × 0,25 = 1,25 GB/día; incremental de respaldo = 0,041 GB/día.
- Resultado por sitio: Talca suma 1,43 GB/día y drena 1,59 Mbps; la hora cargada de oficina y retorno de flota suma 3,71 Mbps, por lo que el peor caso es 3,71 + 1,59 = **5,30 Mbps**. Concepción acumula 0,59 GB/día y drena 0,66 Mbps; cada cross-docking acumula 0,27 GB/día y drena 0,30 Mbps.
- Utilización de enlaces: Talca, 26,51 % de D-03 y 31,88 % de D-04; Concepción, 7,68 % y 21,93 %; cada cross-docking, 17,41 % de D-06 y 14,92 % de D-04.

La utilización de respaldo divide sólo el drenaje por D-04, porque la sincronización tiene prioridad sobre la oficina durante la recuperación.

La ventana dominical usa ocho horas sin operación de bodega ni reparto. En Talca, el respaldo completo de 15,12 GB se convierte en 1,68 horas sobre 20 Mbps y la App de reparto, 23,80 GB, en 2,64 horas; juntas requieren 4,32 horas. Una tanda de 16 sistemas operativos de 2 GB agrega 3,56 horas y ocupa 7,88 horas, por lo que cabe una tanda por domingo y se necesitan 15 domingos para 238 equipos. En Concepción, respaldo de 7,76 GB y aplicación de 6,60 GB requieren 3,19 horas; una tanda de 10 sistemas operativos ocupa 7,64 horas y se necesitan 7 domingos. En cada cross-docking, el respaldo de 1,89 GB y la aplicación de sus 2 terminales, 0,20 GB, requieren 2,33 horas sobre 2 Mbps; con los 2 sistemas operativos la ventana ocupa 6,77 horas y basta un domingo. En cada sitio, el tamaño de la aplicación es ≤100 MB por equipo y preventa usa la red móvil; las actualizaciones se escalonan trimestralmente.

<a id="sec:anexo-4b-dimensiones-13-14"></a>
## 4.B.6 Dimensiones 13–14: terreno y sincronización

La peor ruta produce 34 × 235,81 KB ÷ 1.024 + 2 MB = **9,83 MB**. La ruta promedio produce 5,36 MB normales y 8,24 MB en septiembre. Para diez minutos, el umbral es 9,83 MB × 8 ÷ 600 segundos = **0,13 Mbps efectivos**.

La dimensión 14 es un tiempo. Los 96 camiones regresan entre 17:00 y 20:00; con SV-04, 96 ÷ 3 × 2 = **64 camiones** llegan en la hora punta. Su carga es 64 × 9,83 MB × 8 ÷ 3.600 segundos = **1,40 Mbps** en Wi-Fi y enlace. La flota completa agrega 0,70 Mbps durante las tres horas y queda sincronizada aproximadamente diez minutos después del último camión.

<a id="sec:anexo-4b-dimensiones-15-16"></a>
## 4.B.7 Dimensiones 15–16: mesa de ayuda y operación

La mesa de ayuda se dimensiona en cuatro pasos:

1. Demanda horaria: (640 + 160) × 2,5 = **2.000 contactos mensuales**. Con 22,14 días equivalentes, la hora cargada concentra 2.000 × 25 % ÷ 22,14 = 22,58 contactos/hora y cada una de las otras 17 horas recibe 2.000 × 75 % ÷ 22,14 ÷ 17 = 3,98 contactos/hora.
2. Resultado Erlang C: con 10 minutos de atención media, 80 % de respuestas antes de 20 segundos y abandono ≤5 %, exige 7 agentes en la hora cargada y 2 en las demás.
3. Dotación simultánea: (7 + 17 × 2) × 6 = 246 horas-posición semanales; 246 ÷ 42 = 5,86, pero la dotación no puede ser menor que las 7 posiciones simultáneas, por lo que la mesa requiere **7 personas**.
4. Capacidad máxima de siete agentes: Al resolver el mismo cálculo, el límite es 2.391 contactos/mes; 2.391 × 25 % ÷ 22,14 = 27,00 contactos/hora cargada y 2.391 × 75 % ÷ 22,14 ÷ 17 = 4,99 contactos/hora en las demás franjas.

La cobertura 24×7 de septiembre y diciembre requiere, además, al menos una posición de mesa en las horas 22:00–04:00 de lunes a sábado y durante los domingos: 6 × 6 + 24 = 60 horas-posición semanales; 60 ÷ 42 = 1,43, por lo que se agregan **2 personas** y la mesa peak queda en 9. Un NOC y un SOC de una posición cada uno requieren 2 × (168 ÷ 42) = **8 personas**; desde el 26-04-2028 requieren 2 × (168 ÷ 40) = **10 personas**. La dotación total es 15 personas en operación normal y 17 en septiembre/diciembre a 42 horas; con 40 horas, 17 y 19. Las funciones NOC/SOC pueden ser subcontratadas conforme a RT-21.01 (Bases Técnicas Transversales, Cap. 21, p. 35) y RT-11.17 (Bases Técnicas Transversales, Cap. 11, p. 24).

<a id="sec:anexo-4b-onpremise"></a>
## 4.B.8 Capacidad on-premise por VM

La base local contiene maestros, stock, lotes presentes y movimientos del horizonte de cuatro meses. El tamaño usa 1 KB por registro, 0,5 KB por movimiento y factor 2 de índices y auditoría. La RAM de la base usa 4 GB más 25 % del tamaño a 3×.

<a id="tab:anexo-4b-vm"></a>
**Tabla 34.** Requerimiento por VM real del diseño
| VM o equipo | Requerido actual | Requerido a 3× | Sitio |
| --- | --- | --- | --- |
| VM-01 | 3 vCPU; 4 GB; 50 GB; 25 IOPS | 3 vCPU; 4 GB; 50 GB; 73 IOPS | Talca |
| VM-02 | 3 vCPU; 6 GB; 20 GB; 25 IOPS | 3 vCPU; 8 GB; 31 GB; 73 IOPS | Talca |
| VM-03 | 2 vCPU; 4 GB; 50 GB; 25 IOPS | 2 vCPU; 4 GB; 50 GB; 73 IOPS | Talca |
| VM-04 | 2 vCPU; 2 GB; 20 GB; 5 IOPS | 2 vCPU; 2 GB; 20 GB; 13 IOPS | Talca |
| VM-05 | 2 vCPU; 2 GB; 20 GB; 25 IOPS | 2 vCPU; 2 GB; 20 GB; 73 IOPS | Talca |
| VM-06 | 2 vCPU; 4 GB; 50 GB; 49 IOPS | 2 vCPU; 4 GB; 50 GB; 97 IOPS | Talca |
| VM-C01 | 3 vCPU; 4 GB; 50 GB; 9 IOPS | 3 vCPU; 4 GB; 50 GB; 25 IOPS | Concepción |
| VM-C02 | 3 vCPU; 5 GB; 20 GB; 9 IOPS | 3 vCPU; 6 GB; 20 GB; 25 IOPS | Concepción |
| VM-C03 | 2 vCPU; 2 GB; 20 GB; 9 IOPS | 2 vCPU; 2 GB; 20 GB; 25 IOPS | Concepción |
| VM-C04 | 2 vCPU; 4 GB; 50 GB; 17 IOPS | 2 vCPU; 4 GB; 50 GB; 33 IOPS | Concepción |
| Mini-PC | 3 vCPU; 5 GB; 50 GB; 70 IOPS | 3 vCPU; 5 GB; 50 GB; 208 IOPS | Cada cross-docking |

Talca requiere 17 vCPU, 24 GB RAM y 210 GB actuales; a 3×, 17 vCPU, 26 GB y 221 GB. Con un nodo caído, el T-11 deja 128 vCPU, 256 GB RAM y 3.840 GB lógicos: la utilización es 13,28 % / 9,38 % / 5,47 % actual y 13,28 % / 10,16 % / 5,76 % a 3× para CPU, RAM y disco. La configuración mínima sin marca que cumple N+1 y 3× es 9 vCPU, 13 GB RAM y 221 GB lógicos por nodo.

<a id="sec:anexo-4b-nube"></a>
## 4.B.9 Capacidad en nube

El perfil de API atiende aplicaciones y portales N-01 a N-03. Una tarea Fargate entrega 0,70 ÷ 0,05 = **14,00 solicitudes/s**. La tabla de carga es: régimen, 12,30 solicitudes/s de nube más portal y 2 tareas; peak, 14,66 y 2; RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21), 21,99 y 2; cota extrema, 5,03 + 43,33 = 48,37 y 4. La sensibilidad de 120 solicitudes por sesión conserva las sesiones repartidas en la hora: 2,67 + 19,27 = 21,93 y 2 tareas en régimen; 5,03 + 86,67 = 91,70 y 7 tareas en cota. Todos los casos quedan bajo el techo de 8 tareas.

<a id="sec:anexo-4b-crecimiento"></a>
## 4.B.10 Crecimiento, enlaces y ventana dominical

La proyección de año 3 de la Tabla 14.1 es 36.000 pedidos, 305.000 líneas, 1.650 entregas normales, 3.100 entregas peak y 40.000 DTE mensuales. Cada componente usa una base distinta:

- WMS Talca = 3,02 × (305.000 ÷ 260.000) = 3,54 TPS.
- Nube más portal = 14,66 × (36.000 ÷ 31.000) = 17,03 solicitudes/s.
- Evidencia = 87,72 × (36.000 ÷ 31.000) = 101,87 GB/año.
- Enlace de Talca = 5,34 Mbps por el nuevo flujo de cambios.
- Terminales de bodega de Talca = (23 + 3) de congelado + (113 + 12) estándar = 151.
- Mesa = 2.000 × (350 ÷ 310) = 2.258 contactos/mes.

Por separado, RT-09.03 (Bases Técnicas Transversales, Cap. 9, p. 21) exige 3×: 93.000 pedidos, 780.000 líneas, 4.200/7.800 entregas y 102.000 DTE mensuales.

<a id="tab:anexo-4b-plan"></a>
**Tabla 35.** Plan de capacidad
| Componente | Año 1 | Año 3 | 3× | Acción |
| --- | --- | --- | --- | --- |
| WMS de Talca, TPS peak | 3,02 | 3,54 | 9,06 | Revisar CPU e IOPS trimestralmente |
| Nube, TPS peak / tareas | 14,66 / 2 | 17,03 / 2 | 43,98 / 4 | Escalamiento y prueba trimestral |
| Evidencia anual | 87,72 GB | 101,87 GB | 263,16 GB | Escalar S3 y retención |
| Enlace de Talca, peor caso | 5,30 Mbps | 5,34 Mbps | 8,71 Mbps | Ampliar D-03 si p95 supera la cota |
| Terminales de bodega de Talca | 132 | 151 | no aplica | Ajustar parque a la dotación |
| Mesa, contactos mensuales | 2.000 | 2.258 | 6.000 | Recalibrar Erlang C |

La prueba RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21) usa una sola multiplicación: 14,66 × 1,5 = 21,99 TPS. Las tareas, colas y almacenamiento en nube escalan por política; la reserva N+1, la Wi-Fi y los enlaces se amplían mediante revisión planificada.

<a id="sec:anexo-4b-umbrales"></a>
## 4.B.11 Umbrales de quiebre y cuello de botella

La sensibilidad de SV-04 antes de alcanzar la capacidad CPU calculada es Talca 593,84×, Concepción 221,88×, cada cross-docking 9,69× y nube más portal 7,64×. La peor ruta exige 0,13 Mbps efectivos y la hora punta de retorno exige 1,40 Mbps agregados.

La emisión de guías es el primer candidato a cuello de botella: 2.852 guías admiten 9,47 segundos cada una en la preparación completa, 4,42 segundos al final del turno y 1,89 segundos en la ventana actual. Se observan guías aún no emitidas frente a la salida, tiempo del ERP, cola, base WMS, IOPS, Wi-Fi y drenaje en percentil 95. La degradación controlada encola con clave idempotente, aplica límite de tasa y muestra un mensaje explícito; el ERP sigue siendo el único emisor.

<a id="sec:anexo-4b-pruebas"></a>
## 4.B.12 Pruebas de carga, estrés y operación

La carga RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21) se ejecuta a **21,99 TPS totales**, distribuidos por lugar según el perfil horario, sin multiplicar cada lugar por separado. El estrés que exige el mismo RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21) supera la cota extrema del portal y la volumetría 3×. La prueba de corte dura 24 horas y debe drenar en dos; la sincronización de la peor ruta debe completar en diez minutos. Se ejecutan dos ensayos de migración conforme a RT-05.13 (Bases Técnicas Transversales, Cap. 5, p. 12) y una verificación de la ventana dominical para cada sitio.

Se conservan percentil 95, utilización, colas, errores, pérdida o duplicación, estado de conciliación y parámetros confirmados. El perfil horario, la migración y la operación dominical se cierran con evidencia de prueba, sin convertir el resultado medido en un hecho previo.
