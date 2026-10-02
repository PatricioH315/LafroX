# Memoria de cálculo de dimensionamiento

Los cálculos siguientes expresan la fórmula, la sustitución y el resultado con unidades. Las tasas se obtienen del perfil de 24 horas y los redondeos de integraciones se aplican antes de sumar.

## Entradas y control de calendario

Los días equivalentes son 31.000 pedidos/mes ÷ 1.400 entregas/día = **22,14 días**; el control cruzado es 2.100 viajes ÷ 96 camiones = **21,88 días**. El factor peak es 2.600 ÷ 1.400 = **1,857**. Los totales anuales se obtienen como 12 × el volumen mensual de la Tabla 14.1.

## Dimensiones 1–3: transacciones por segundo

Se calcula el máximo horario de cada régimen para evitar sumar ventanas que no coinciden. La fórmula de una ventana es volumen del flujo × operaciones ÷ duración de la ventana × SV-04 sólo en su hora cargada.
En régimen normal el máximo horario es **12,30 TPS a las 12:00**. Los máximos por lugar son Talca 1,46, Concepción 0,73, cada cross-docking 1,56, nube 2,67 y portal 9,63 TPS.
En septiembre el máximo es **14,66 TPS a las 12:00**. Por lugar: Talca 2,68, Concepción 1,34, cada cross-docking 2,89, nube 5,03 y portal 9,63 TPS.
La dimensión 2 toma el mayor total horario dentro de 05:30–07:00: las horas 05:00 y 06:00, suponiendo uniforme el tramo 05:30–06:00; resulta **5,50 TPS** peak y **2,98 TPS** normal. Los 2.852 DTE/día peak son el total de documentos tributarios electrónicos, no sólo guías; tratarlos todos como guías que deben emitirse antes de la salida constituye una cota conservadora. Para el portal, 2.600 ÷ 9 × 2 por SV-04 × 60 ÷ 3.600 = 9,63 solicitudes/s.
La prueba BTT RT-09.06 aplica una sola vez 1,5 × 14,66 = **21,99 TPS**.

### Perfil horario de 24 horas

La tabla conserva las tasas por hora y por lugar. La fila máxima explica la dimensión 1 y la dimensión 3.
| Hora | Talca normal / peak | Concepción normal / peak | Cross-docking normal / peak | Nube normal / peak | Portal normal / peak | Total normal / peak |
|---:|---:|---:|---:|---:|---:|---:|
| 00:00 | 0,54 / 1,01 | 0,27 / 0,50 | 0,00 / 0,00 | 0,74 / 1,37 | 0,00 / 0,00 | 1,55 / 2,88 |
| 01:00 | 0,54 / 1,01 | 0,27 / 0,50 | 0,00 / 0,00 | 0,74 / 1,37 | 0,00 / 0,00 | 1,55 / 2,88 |
| 02:00 | 0,54 / 1,01 | 0,27 / 0,50 | 0,00 / 0,00 | 0,74 / 1,37 | 0,00 / 0,00 | 1,55 / 2,88 |
| 03:00 | 0,54 / 1,01 | 0,27 / 0,50 | 0,78 / 1,44 | 0,74 / 1,37 | 0,00 / 0,00 | 2,33 / 4,33 |
| 04:00 | 0,54 / 1,01 | 0,27 / 0,50 | 1,56 / 2,89 | 0,74 / 1,37 | 0,00 / 0,00 | 3,11 / 5,77 |
| 05:00 | 1,46 / 2,68 | 0,73 / 1,34 | 0,00 / 0,00 | 0,79 / 1,47 | 0,00 / 0,00 | 2,98 / 5,50 |
| 06:00 | 0,74 / 1,33 | 0,37 / 0,67 | 0,00 / 0,00 | 0,68 / 1,26 | 0,00 / 0,00 | 1,79 / 3,26 |
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

El máximo normal ocurre a las 12:00 y el de septiembre a las 12:00; el portal aporta 9,63 y 9,63 TPS en esa hora, mientras la nube aporta 2,67 y 5,03. El promedio diario oculta la coincidencia de preventa, reparto y sesiones del portal.

## Dimensiones 4–6: personas, concurrencia y dispositivos

Las personas o entidades registradas son (640 + 160) + 14.200 + 180 = **15.180**. La concurrencia máxima por ventana es noche 186, despacho 96, día sin portal 342, sincronización 158, y día con portal en régimen **438,30**; la cota extrema del portal es **775,33**.
La dimensión 6 es 62 preventistas + 96 equipos de reparto = **158 dispositivos de terreno**. El parque a proveer se informa aparte.

## Dimensiones 7–10: almacenamiento y migración

El almacenamiento transaccional parte de 1.300.000 eventos (260.000 líneas × 5), 520.000 operaciones (260.000 líneas × 2), 155.000 operaciones (31.000 pedidos × 5) y 279.050 movimientos (260.000 líneas + 14.500 pallets + 3.400 conteos + 1.150 recepciones). La fórmula es ((1.300.000 + 520.000 + 155.000) × 1 KB + 279.050 × 0,5 KB) × 2 × 12 = **50,75 GB/año**; seis años acumulan **304,49 GB** como cota de retención.
La evidencia es 30 KB + 200 KB × (1 + 900 ÷ 31.000) = **235,81 KB por entrega**; genera **87,72 GB/año** y **13,58 GB en el mes peak**.
Temperatura: 6.048 lecturas/día de las cámaras + 4.536 de los termógrafos de camión = 10.584 mensajes/día; con 145 bytes por lectura son 0,56 GB/año crudos y 0,14 GB/año almacenados, 2,80 GB crudos en 5 años. Posición: 22.075.200 eventos/año, 3,20 GB crudos y 0,80 GB almacenados en 12 meses; cada evento usa 145 bytes. La copia almacenada usa factor 0,25.
La migración suma maestros 34.180 KB, ventas y pedidos 10.476.000 KB, inventario y movimientos 3.348.600 KB, recepciones con lote 1.380.000 KB y cuentas por cobrar 816.000 KB. Con factor 2: **32,11 GB**, sensibilidad **30,73–33,49 GB**.

## Dimensiones 11–12: integraciones y enlaces

El apartado 4.1 contiene 15 integraciones. La dimensión 11 suma **178.661 mensajes/día normal** y **260.155 peak**; portal y llamadas internas a la API quedan fuera. El EDI actual es cero; el escenario 2029 usa la cota de 11 % de pedidos.
| Integración | Mensajes/día normal | Mensajes/día peak | Origen del volumen |
|---|---:|---:|---|
| INT-01 Pedido preventa y consulta | 1.400 | 2.600 | 1.400 × 1; 2.600 × 1; SV-01 |
| INT-02 Entrega, POD y cobro | 7.000 | 13.000 | 1.400 × 5; 2.600 × 5 |
| INT-03 Eventos de bodega a nube | 58.710 | 109.032 | 260.000 ÷ 22,14 × 5; peak × 1,857 |
| INT-04 Detalle cross-docking a Talca | 5.600 | 10.400 | 1.400 × 4; cota de una plataforma |
| INT-05 Eventos de temperatura | 10.584 | 10.584 | 6.048 cámaras + 4.536 termógrafos |
| INT-06 ERP 2017 | 2.025 | 3.762 | 1.400 + 1.150 ÷ 22,14 + 900 ÷ 22,14 + 11.800 ÷ 22,14; peak × 1,857 |
| INT-07 DTE/SII | 3.071 | 5.703 | 34.000 ÷ 22,14 × 2; peak × 1,857 |
| INT-08 Cadenas modernas EDI | 0 | 1.144 | 0 actual; 2.600 × 11 % × 4 |
| INT-09 Pasarela de pago | 533 | 990 | 11.800 ÷ 22,14; peak × 1,857 |
| INT-10 Mapas y geocodificación | 96 | 96 | 96 camiones × 1 |
| INT-11 Avisos al cliente | 2.800 | 5.200 | 1.400 × 2; 2.600 × 2 |
| INT-12 Cambios de datos a réplica | 12.602 | 23.404 | 279.050 ÷ 22,14; peak × 1,857 |
| INT-13 Identidad a sitio | 760 | 760 | 380 dispositivos × 2 |
| INT-14 Métricas y trazas | 13.000 | 13.000 | 13 nodos × 1.000 |
| INT-15 Telemetría existente | 60.480 | 60.480 | 42 × 12 × 120; SV-07 |
| **Total** | **178.661** | **260.155** | **15 integraciones; portal y API interna fuera** |

El drenaje contiene sólo cambios con WAL, vaciado del broker, telemetría, observabilidad e incremental de respaldo acumulados durante 24 horas; no incluye tráfico de oficina. El peor caso suma la hora cargada con oficina y la sincronización de la flota cuando corresponde. D-06 se calcula con 2 Mbps de subida garantizada mínima supuesta, un parámetro conservador de diseño que se confirma en la instalación.
- Talca: régimen cargado 3,29 Mbps; drenaje 1,87 Mbps; peor caso 5,16 Mbps; D-03 25,80 % y D-04 para drenaje 37,43 %. Datos acumulables: 1,68 GB/día.
- Concepción: régimen cargado 0,67 Mbps; drenaje 1,21 Mbps; peor caso 1,88 Mbps; D-03 18,82 % y D-04 para drenaje 40,45 %. Datos acumulables: 1,09 GB/día.
- Cada cross-docking: régimen cargado 0,05 Mbps; drenaje 0,30 Mbps; peor caso 0,35 Mbps; D-06 17,41 % y D-04 para drenaje 14,92 %. Datos acumulables: 0,27 GB/día.
El retorno se reparte según SV-03: 64 camiones en la hora punta total de 17:00–20:00 requieren 0,93 Mbps en Talca y 0,47 Mbps en Concepción para Wi-Fi y enlace; la flota completa requiere 1,40 Mbps en esa hora y 0,70 Mbps agregados en las tres horas. Cada dispositivo queda sincronizado en diez minutos.

## Dimensiones 13–14: terreno y sincronización

La peor ruta genera 34 × 235,81 KB ÷ 1.024 + 2 MB = **9,83 MB** por dispositivo. Una ruta promedio genera **5,36 MB** normal y **8,24 MB** en septiembre.
Con 9,83 MB, el umbral de quiebre de sincronización es 9,83 MB × 8 ÷ 600 s = **0,13 Mbps efectivos**; el diseño exige que cada dispositivo disponga de al menos ese caudal.

## Dimensiones 15–16: mesa de ayuda y operación

La mesa recibe 2.000 contactos/mes en el escenario de 2,5 contactos por persona interna. La hora cargada concentra el 25 %: 22,58 contactos/hora; las otras 17 horas reciben 3,98 cada una. Erlang C exige 7 agentes en la hora cargada y 2 en las demás; la suma semanal es 246 horas-posición y requiere **7 personas** a 42 horas semanales.
La operación 24×7 de septiembre y diciembre requiere ocho personas para un NOC y un SOC de una posición cada uno: 168 ÷ 42 = 4 personas por posición. Desde el 26-04-2028, 168 ÷ 40 = 5; el total mesa más NOC/SOC es **15** y luego **17 personas**.

## Capacidad on-premise

La base local incluye maestros, stock, lotes presentes y movimientos de cuatro meses; el histórico de retención vive en la nube. La RAM de la base es 4 GB más 25 % del tamaño a 3×; cada VM suma base de sistema y carga.
| VM/equipo | Requerido actual | Requerido 3× | Sitio |
|---|---|---|---|
| VM-01 | 3 vCPU, 4 GB RAM, 50 GB disco lógico, 22 IOPS | 3 vCPU, 4 GB RAM, 50 GB disco lógico, 65 IOPS | Talca |
| VM-02 | 3 vCPU, 6 GB RAM, 20 GB disco lógico, 22 IOPS | 3 vCPU, 8 GB RAM, 31 GB disco lógico, 65 IOPS | Talca |
| VM-03 | 2 vCPU, 4 GB RAM, 50 GB disco lógico, 22 IOPS | 2 vCPU, 4 GB RAM, 50 GB disco lógico, 65 IOPS | Talca |
| VM-04 | 2 vCPU, 2 GB RAM, 20 GB disco lógico, 5 IOPS | 2 vCPU, 2 GB RAM, 20 GB disco lógico, 13 IOPS | Talca |
| VM-05 | 2 vCPU, 2 GB RAM, 20 GB disco lógico, 22 IOPS | 2 vCPU, 2 GB RAM, 20 GB disco lógico, 65 IOPS | Talca |
| VM-06 | 2 vCPU, 4 GB RAM, 50 GB disco lógico, 43 IOPS | 2 vCPU, 4 GB RAM, 50 GB disco lógico, 86 IOPS | Talca |
| VM-C01 | 3 vCPU, 4 GB RAM, 50 GB disco lógico, 11 IOPS | 3 vCPU, 4 GB RAM, 50 GB disco lógico, 33 IOPS | Concepción |
| VM-C02 | 3 vCPU, 5 GB RAM, 20 GB disco lógico, 11 IOPS | 3 vCPU, 6 GB RAM, 20 GB disco lógico, 33 IOPS | Concepción |
| VM-C03 | 2 vCPU, 2 GB RAM, 20 GB disco lógico, 11 IOPS | 2 vCPU, 2 GB RAM, 20 GB disco lógico, 33 IOPS | Concepción |
| VM-C04 | 2 vCPU, 4 GB RAM, 50 GB disco lógico, 22 IOPS | 2 vCPU, 4 GB RAM, 50 GB disco lógico, 43 IOPS | Concepción |
| Mini-PC | 3 vCPU, 5 GB RAM, 50 GB disco lógico, 70 IOPS | 3 vCPU, 5 GB RAM, 50 GB disco lógico, 208 IOPS | Cada cross-docking |
Las VMs de Talca suman 14 vCPU, 22 GB RAM, 210 GB disco lógico, 136 IOPS; con hipervisor (+15 % vCPU y 2 GB RAM por cada uno de 3 nodos físicos) requieren 17 vCPU, 28.0 GB RAM, 210 GB disco lógico, 136 IOPS actual y 17 vCPU, 30.0 GB RAM, 221 GB disco lógico, 359 IOPS a 3×. Las VMs de Concepción suman 10 vCPU, 15 GB RAM, 140 GB disco lógico, 55 IOPS; con hipervisor (+15 % vCPU y 2 GB RAM por nodo físico) requieren 12 vCPU, 17.0 GB RAM, 140 GB disco lógico, 55 IOPS actual y 12 vCPU, 18.0 GB RAM, 140 GB disco lógico, 142 IOPS a 3×. Frente al T-11 con un nodo caído, la utilización de Talca es 13,28 / 10,94 / 5,47 % actual y 13,28 / 11,72 / 5,76 % a 3× para CPU/RAM/disco. La configuración mínima N+1 y 3× por nodo es 9 vCPU, 15 GB RAM y 221 GB lógicos; la redundancia fija el mínimo.

## Capacidad en nube

El perfil de API atiende aplicaciones y portales N-01 a N-03. Una tarea Fargate entrega 0,70 ÷ 0,05 = **14,00 solicitudes/s**. Régimen: 12,30 solicitudes/s y 2 tareas; peak: 14,66 y 2; RT-09.06: 21,99 y 2; cota extrema: 48,37 y 4; sensibilidad de 120 solicitudes por sesión: 21,93 y 2 en régimen, 91,70 y 7 en cota. El techo es ocho tareas.

## Ventana dominical

- Talca: respaldo completo a 3× 15,12 GB y aplicación 23,80 GB requieren 4,32 h; la tanda de sistema operativo es 16 equipos, 7,88 h por domingo y una ronda completa ocupa 15 domingos. La aplicación se actualiza en un domingo por sitio; el sistema operativo se distribuye en tandas dominicales, con cadencia semestral.
- Concepción: respaldo completo a 3× 7,76 GB y aplicación 6,60 GB requieren 3,19 h; la tanda de sistema operativo es 10 equipos, 7,64 h por domingo y una ronda completa ocupa 7 domingos. La aplicación se actualiza en un domingo por sitio; el sistema operativo se distribuye en tandas dominicales, con cadencia semestral.
- Cada cross-docking: respaldo completo a 3× 1,89 GB y aplicación 0,20 GB requieren 2,33 h; la tanda de sistema operativo es 2 equipos, 6,77 h por domingo y una ronda completa ocupa 1 domingos. La aplicación se actualiza en un domingo por sitio; el sistema operativo se distribuye en tandas dominicales, con cadencia semestral.

## Crecimiento, umbrales y cuello de botella

Año 3 usa 36.000 pedidos/mes (36.000 ÷ 31.000 = 1,16×), 305.000 líneas/mes (1,17×), 1.650/3.100 entregas/día y 40.000 DTE/mes. Por separado, 3× es 93.000 pedidos, 780.000 líneas, 4.200/7.800 entregas y 102.000 DTE mensuales.
La tabla de capacidad del año 3 se obtiene con una base por métrica: WMS Talca 2,68 × (305.000 ÷ 260.000) = 3,15 TPS; nube más portal 14,66 × (36.000 ÷ 31.000) = 17,03 solicitudes/s; evidencia 87,72 × (36.000 ÷ 31.000) = 101,87 GB/año; Talca usa 5,20 Mbps en el peor caso y 5,64 Mbps a 3×; bodega Talca usa 151 terminales; mesa conserva 2.258 contactos/mes. La columna 3× cubre carga técnica, no aumenta el parque de personas.
El umbral de SV-04, expresado como múltiplo de la tasa peak antes de saturar la capacidad calculada, es Talca 667,46×, Concepción 166,87×, cada cross-docking 9,69× y nube más portal 7,64×. La cota extrema combinada requiere 4 tareas; la sensibilidad exige 7 y se mantiene bajo el techo de ocho.
Para los 2.852 DTE peak, el tiempo máximo por documento es 27.000 ÷ 2.852 = 9,47 s si se reparte en toda la preparación; 4,42 s si se concentra al final; y 1,89 s si se conserva la práctica actual. El diseño emite el documento cuando confirma la carga, durante la noche. Se detectan documentos pendientes frente a la hora de salida de cada camión; se resuelve priorizando la cola y reconciliando el folio, sin crear otro emisor: el ERP sigue siendo el único emisor y el documento acompaña el traslado.
Con siete agentes, el escenario de mesa tolera aproximadamente 2.391 contactos mensuales antes de requerir una posición adicional. Se observan percentiles 95, colas, errores, IOPS, Wi-Fi, ERP y drenaje en RT-09.06 y en la operación.

## Fuentes de validación

El perfilado confirma tamaños de registros y migración; la prueba de carga confirma CPU, residencia Fargate, concurrencia y tasas; la prueba de corte confirma drenaje y la prueba dominical confirma respaldo y actualizaciones. Ninguna de estas verificaciones reemplaza el valor de diseño declarado.
