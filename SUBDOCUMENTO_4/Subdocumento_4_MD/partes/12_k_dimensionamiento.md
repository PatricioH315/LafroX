<!-- Fuente: Subdocumento_4_LateX/04_arquitectura_fisica/partes/12_k_dimensionamiento.tex — conversión fiel; editar el .tex y regenerar -->

<a id="sec:dimensionamiento"></a>
## 4.2.6 Dimensionamiento y plan de capacidad

El dimensionamiento traduce la volumetría del Caso 02 en capacidad para la operación normal, la ventana protegida de despacho y el peak de septiembre. Las citas nombran las Bases Técnicas del caso y las Bases Técnicas Transversales con su capítulo y página. La cadena es: hechos y requisitos, supuestos mínimos, dieciséis dimensiones del numeral 14.2 de las Bases Técnicas del caso (p. 25), capacidad por lugar de proceso y equipamiento. El Anexo 4.B conserva las sustituciones, el perfil horario, las sensibilidades y los umbrales; esta sección presenta la decisión de arquitectura y su consecuencia operativa.

<a id="sec:dimensionamiento-metodo"></a>
### 4.2.6.1 Método, fuentes y supuestos

Un hecho del caso se cita y no se registra como supuesto. Un requisito proviene de las Bases o del Capítulo 15. Un parámetro de diseño es una decisión que imponemos a la solución. Un supuesto completa una cifra que el caso calla y declara fundamento, impacto y validación. Un cálculo se deriva de las entradas anteriores. Los parámetros de plataforma son 50 ms de CPU por solicitud, 64 MB de memoria por proceso y 150 ms de permanencia del proceso en Fargate; son parámetros de diseño que se perfilan y se verifican en las pruebas de RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21). Los tiempos se evalúan en percentil 95 conforme a las Bases Técnicas Transversales, Cap. 9, p. 21.

La Figura [11](12_k_dimensionamiento.md#fig:dimensionamiento-cadena) resume esta cadena. El resultado de cada etapa alimenta la siguiente: la volumetría determina las tasas, las tasas determinan capacidad y la capacidad determina los equipos.

<a id="fig:dimensionamiento-cadena"></a>
**Figura 11.** Cadena de cálculo del dimensionamiento.

> Figura compuesta en TikZ en el LaTeX; ver main.pdf, página 64.

- Volumetría<br>del caso
- Supuestos<br>mínimos
- 16 dimensiones<br>del numeral 14.2
- Capacidad por<br>lugar de proceso
- Equipos,<br>enlaces y nube

La cadena evita mezclar decisiones de diseño con hechos del CLIENTE. En particular, el factor SV-04 se aplica sólo a la hora cargada de cada ventana y no se usa para sumar procesos que ocurren en horas diferentes.

<a id="sec:dimensionamiento-regimenes"></a>
### 4.2.6.2 Perfil de carga y regímenes de diseño

El Bases Técnicas del caso, Anexo B, p. 38 distribuye la operación en estas ventanas:

- Preparación de 22:00 a 06:00.
- Cross-docking de 03:00 a 05:00.
- Despacho de 05:30 a 07:00.
- Reparto de 07:00 a 19:00.
- Recepción de proveedores de 08:00 a 18:00.
- Preventa de 09:00 a 18:00.
- Sincronización de 17:00 a 20:00.

El perfil de 24 horas de la Figura [12](12_k_dimensionamiento.md#fig:dimensionamiento-perfil) muestra las tasas totales calculadas para esas superposiciones.

<a id="fig:dimensionamiento-perfil"></a>
**Figura 12.** Tasas totales por hora en régimen normal y en septiembre.

> Figura compuesta en TikZ en el LaTeX; ver main.pdf, página 65.

- TPS
- máximo a las 12:00: 12,30 y 14,66 TPS
- día normal
- peak de septiembre
- Etiquetas del eje vertical: 0, 5, 10, 15; eje vertical: TPS; etiquetas del eje horizontal: 00:00, 03:00, 06:00, 09:00, 12:00, 15:00, 18:00, 21:00, 24:00; máximo a las 12:00: 12,30 y 14,66 TPS; leyenda: día normal, peak de septiembre; ventanas: Preparación, Despacho, Preventa, Sincronización.

La hora más exigente es 12:00, con 12,30 TPS normales y 14,66 TPS en septiembre. Esa hora es una convención del cálculo: el factor SV-04 concentra la preventa y el portal en la hora central de su ventana, y el máximo sería el mismo en cualquier otra hora de esa ventana. En esa hora el portal aporta 9,63 TPS y la nube 2,67 TPS normales o 5,03 TPS en peak; Talca, Concepción y cada cross-docking están fuera de sus ventanas de mayor carga. El promedio diario engaña porque oculta la coincidencia de preventa, reparto y sesiones del portal.

La Tabla [16](#tab:dimensionamiento-calendario) resume los factores de calendario que se usan en la memoria.

<a id="tab:dimensionamiento-calendario"></a>
**Tabla 16.** Calendario y factores de diseño
| Dato | Valor | Uso | Fuente |
| --- | --- | --- | --- |
| Días equivalentes de despacho | 22,14 días | 31.000 ÷ 1.400; control 2.100 ÷ 96 = 21,88 | Bases Técnicas del caso, Cap. 14, p. 24 y Tabla 2.3; SV-01 |
| Factor de septiembre | 1,857 | 2.600 ÷ 1.400 | Bases Técnicas del caso, Cap. 14, p. 24; SV-02 |
| Período peak | 1 al 25 de septiembre | Define el régimen peak | Bases Técnicas del caso, Anexo B, p. 38 |
| Totales anuales | 12 × volumen mensual | Evita inventar días hábiles | Bases Técnicas del caso, Cap. 14, p. 24 |

Los 22,14 días son una equivalencia de cálculo, no una cantidad de días hábiles. El peak se obtiene por el cociente entre entregas de septiembre y entregas normales; diciembre no agrega un factor porque el caso identifica septiembre como la mayor exigencia.

<a id="sec:dimensionamiento-tps"></a>
### 4.2.6.3 Transacciones por segundo: dimensiones 1–3

La dimensión 1, «Transacciones por segundo en régimen normal», toma el máximo horario normal. La dimensión 2, «Transacciones por segundo en el peak de la ventana de despacho de 05:30 a 07:00», incluye la cota de emisión de guías. La dimensión 3, «Transacciones por segundo en el peak de septiembre», toma el máximo horario del perfil de septiembre.

La Tabla [17](#tab:t76) presenta los lugares de proceso y separa el portal de la nube. El despacho se muestra como una cota independiente porque el caso lo identifica como peak actual de emisión de documentos.

<a id="tab:t76"></a>
**Tabla 17.** Transacciones por segundo por lugar de proceso
| Lugar o flujo | Régimen normal | Ventana de despacho | Peak septiembre | Derivación |
| --- | --- | --- | --- | --- |
| WMS de Talca | 1,64 TPS | 1,11 TPS | 3,02 TPS | preparación y despacho según perfil horario |
| WMS de Concepción | 0,54 TPS | – | 1,01 TPS | 2/3 y 1/3 de las líneas; SV-03 |
| Cada cross-docking | 1,56 TPS | – | 2,89 TPS | 4 operaciones por entrega |
| Nube, sin portal | 2,67 TPS | 0,68 TPS | 5,03 TPS | preventa, reparto, recepción, trazabilidad, guías y sincronización |
| Portal | 9,63 TPS | – | 9,63 TPS | 2.600 ÷ 9 × 2 por SV-04 × 60 ÷ 3.600 |
| Total | 12,30 TPS | 1,68 / 3,05 TPS | 14,66 TPS | máximo horario; despacho con guías |

El flujo de preparación visible es 11.742 líneas por noche × 2 operaciones × 2/3 ÷ 28.800 segundos = 0,54 TPS de media de ventana para Talca. Al aplicar SV-04 sólo a la hora cargada, llega a 1,09 TPS; a las 05:00 se suma el despacho y el WMS de Talca alcanza 1,64 TPS normal. En septiembre llega a 3,02 TPS al incluir el factor de volumen. Las 2.600 sesiones habituales del portal pertenecen a food service y cadenas (Bases Técnicas del caso, Cap. 2, p. 4) y no son las 2.600 visitas diarias de preventa (Bases Técnicas del caso, Anexo B, p. 38); la coincidencia numérica no implica que sean el mismo flujo. La prueba RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21) es 1,5 × 14,66 = 21,99 TPS y no recibe un segundo multiplicador.

<a id="sec:dimensionamiento-usuarios"></a>
### 4.2.6.4 Personas usuarias, concurrencia y dispositivos: dimensiones 4–6

La dimensión 4, «Personas usuarias registradas, internas y externas», es 15.180 registros: 640 + 160 + 14.200 + 180. La dimensión 5, «Personas usuarias concurrentes en peak», toma el máximo de cada ventana sin sumar turnos que no coinciden. La Tabla [18](#tab:dimensionamiento-concurrencia) muestra la operación sin portal y la cota de sesiones.

<a id="tab:dimensionamiento-concurrencia"></a>
**Tabla 18.** Concurrencia por ventana
| Ventana | Operación sin portal | Portal | Máximo |
| --- | --- | --- | --- |
| Noche: preparación y cross-docking | 120 + 60 + 6 = 186 | – | 186 |
| Despacho | 96 equipos de reparto | – | 96 |
| Día | 62 + 96 + 184 = 342 | 96,30 en régimen | 438,30 |
| Sincronización | 62 + 96 = 158 | – | 158 |
| Cota extrema del portal | 342 | 433,33 | 775,33 |

La operación sin portal, que carga la Wi-Fi y los sitios, llega a 342 personas o equipos concurrentes durante el día. Los seis del cross-docking son personas con terminal inalámbrico, dos por plataforma (S-35). Los 96 equipos de reparto equivalen a 96 conductores en ruta; la dimensión 5 se expresa en personas o sesiones y no en camiones. La cota extrema del portal se conserva como prueba separada. La dimensión 6, «Dispositivos de terreno en operación simultánea», es 62 preventistas + 96 equipos de reparto = 158.

La cantidad a proveer se informa aparte, por ámbito:

- Bodega: 132 terminales en Talca, 22 de ellos para congelado, y 66 en Concepción.
- Terreno: 69 terminales de preventa, 106 terminales de reparto, 106 impresoras de cabina y 106 terminales de pago.
- Cross-docking y frío: 7 terminales de cross-docking y 31 termógrafos.

Cada cantidad incluye la reserva del 10 % del parque, redondeada hacia arriba, conforme a la tabla de repuestos de las Bases Técnicas Transversales (Cap. 8, p. 19). Solo los 22 terminales de la cuadrilla de congelado de Talca son aptos para {-}22 °C: el congelado representa cerca del 4 % de las líneas y se prepara al final del turno, de modo que la cuadrilla que entra a la cámara es de unas 20 personas (S-34). Concepción no tiene congelado.

<a id="sec:dimensionamiento-almacenamiento"></a>
### 4.2.6.5 Almacenamiento, retención y migración: dimensiones 7–10

La dimensión 7, «Volumen anual de almacenamiento transaccional», la dimensión 8, «Volumen anual de almacenamiento de evidencia de entrega, firmas y fotografías», la dimensión 9, «Volumen anual de almacenamiento de series de temperatura y de posicionamiento», y la dimensión 10, «Volumen total de datos históricos a migrar», se resumen en la Tabla [19](#tab:dimensionamiento-almacenamiento).

<a id="tab:dimensionamiento-almacenamiento"></a>
**Tabla 19.** Volumen, retención y destino de los datos
| Dominio | Volumen anual | Retención | Acumulado | Destino |
| --- | --- | --- | --- | --- |
| Datos transaccionales | 50,75 GB/año | 6 años como cota | 304,49 GB | Base local de 4 meses y nube |
| Evidencia de entrega | 87,72 GB/año | 6 años | 526,32 GB | S3 por niveles |
| Temperatura | 0,56 GB/año crudos | 5 años | 2,80 GB crudos | IoT y almacenamiento histórico |
| Posición | 3,20 GB/año crudos | 12 meses | 3,20 GB crudos | Telemetría y almacenamiento histórico |
| Migración histórica | 32,11 GB | Maestros; 36/24/60/24 meses | 30,73–33,49 GB de sensibilidad | Nube después del perfilado |

La migración no supone eventos históricos digitales de trazabilidad: el caso dice que no existe forma consultable y que el lote se anota en texto libre cuando se anota. Por eso la estimación usa 1.150 recepciones mensuales × 60 meses × 20 líneas por recepción, con sensibilidad de 10 a 30 líneas. El 41 % sin lote del retiro de marzo se usa sólo para saneamiento de calidad, conforme a Bases Técnicas del caso, Cap. 7, p. 12.

<a id="sec:dimensionamiento-enlaces"></a>
### 4.2.6.6 Integraciones y ancho de banda por sitio: dimensiones 11–12

La dimensión 11, «Número de integraciones y volumen de mensajes por integración», cuenta únicamente INT-01 a INT-15 del catálogo del apartado 4.1. Portal y llamadas internas a la API quedan fuera. La Tabla [20](#tab:dimensionamiento-integraciones) resume sus 175.661 mensajes diarios normales y 257.155 en peak.

<a id="tab:dimensionamiento-integraciones"></a>
**Tabla 20.** Mensajes de integración por grupo
| Integraciones | Normal | Peak | Origen |
| --- | --- | --- | --- |
| INT-01 a INT-04 | 72.710/día | 135.032/día | Pedidos, entregas, eventos y cota de cross-docking |
| INT-05 | 10.584/día | 10.584/día | 6.048 cámaras + 4.536 termógrafos |
| INT-06 a INT-10 | 5.725/día | 11.695/día | ERP, DTE, EDI, pagos y mapas |
| INT-11 a INT-15 | 86.642/día | 99.844/día | Avisos, réplica, identidad, ADOT y telemetría |
| **Total** | **175.661/día** | **257.155/día** | **15 integraciones** |

El EDI actual es cero y el escenario 2029 se limita a 11 % de los pedidos de la cadena principal, que pesa 11 % de la venta (SV-05). La Tabla [21](#tab:t81) compara la hora cargada, el drenaje y el peor caso con el enlace principal y el respaldo de cada sitio.

<a id="tab:t81"></a>
**Tabla 21.** Ancho de banda por sitio
| Sitio | Régimen cargado | Drenaje 24 h/2 h | Peor caso | Utilización principal / respaldo LTE (drenaje prioritario) |
| --- | --- | --- | --- | --- |
| Talca, D-03 / D-04 | 3,71 Mbps | 1,59 Mbps | 5,30 Mbps | 26,51 % / 31,88 % |
| Concepción, D-03 / D-04 | 0,11 Mbps | 0,66 Mbps | 0,77 Mbps | 7,68 % / 21,93 % |
| Cada cross-docking, D-06 / D-04 | 0,05 Mbps | 0,30 Mbps | 0,35 Mbps | 17,41 % / 14,92 % |

En esta comparación, D-03 es el enlace de fibra, D-04 el enlace LTE y D-06 el enlace satelital. El drenaje no incluye oficina: durante un corte no se encola ese tráfico. Sí incluye cambios con WAL, broker, telemetría, observabilidad e incremental de respaldo. Durante la recuperación por D-04, la sincronización tiene prioridad sobre la oficina conforme a RT-03.24 (Bases Técnicas Transversales, Cap. 3, p. 10). Talca agrega 1,40 Mbps en la hora punta de retorno de 64 camiones; el agregado de la ventana 17:00–20:00 es 0,70 Mbps. El respaldo completo semanal y la App de reparto caben en la ventana dominical; el sistema operativo se distribuye en tandas de 16 equipos en Talca, 10 en Concepción y 2 en cada cross-docking.

<a id="sec:dimensionamiento-terreno"></a>
### 4.2.6.7 Terreno: turno sin señal y sincronización de la flota: dimensiones 13–14

La dimensión 13, «Volumen de datos generado por un dispositivo de reparto en un turno completo sin señal», es 9,83 MB para la ruta de 34 clientes; una ruta promedio genera 5,36 MB normales y 8,24 MB en septiembre. La cifra incluye evidencia, una fotografía adicional cuando corresponde y 2 MB de datos locales.

La dimensión 14, «Tiempo de sincronización de la flota al regresar al centro de distribución», se expresa en tiempo: cada dispositivo sincroniza en diez minutos con al menos 0,13 Mbps efectivos. Los 64 camiones de la hora punta requieren 1,40 Mbps en la Wi-Fi y el enlace de Talca; la flota termina unos diez minutos después de la llegada del último camión. La cota de 34 clientes corresponde a la ruta rural más larga descrita en el caso (Bases Técnicas del caso, Cap. 8, p. 16, entrevista al conductor de la ruta Cauquenes); en el centro de distribución la sincronización ocurre por Wi-Fi.

<a id="sec:dimensionamiento-onpremise"></a>
### 4.2.6.8 Capacidad on-premise

La capacidad propuesta conserva maestros, stock, lotes presentes y movimientos de cuatro meses en cada sitio; el histórico vive en la nube. El horizonte cubre el ciclo de conteo de 11.400 ÷ 3.400 = 3,35 meses y la rotación media de 11,4 veces/año. Cada VM se calcula como base de sistema más carga; se agregan un 15 % de CPU y 2 GB de RAM por nodo para el hipervisor.

<a id="tab:t79"></a>
**Tabla 22.** Capacidad requerida por sitio
| Sitio | Base local | Requerido actual | Requerido a 3× |
| --- | --- | --- | --- |
| Talca, VM-01 a VM-06 | 5,04 GB; 7,78 GB RAM de trabajo | 17 vCPU; 24 GB RAM; 210 GB | 17 vCPU; 26 GB RAM; 221 GB |
| Concepción, VM-C01 a VM-C04 | 2,59 GB; 5,94 GB RAM de trabajo | 10 vCPU; 15 GB RAM; 140 GB | 10 vCPU; 16 GB RAM; 140 GB |
| Cada cross-docking, mini-PC | 0,63 GB; 4,47 GB RAM de trabajo | 3 vCPU; 5 GB RAM; 50 GB | 3 vCPU; 5 GB RAM; 50 GB |
| Configuración mínima por nodo | – | – | 9 vCPU; 13 GB RAM; 221 GB lógicos |

La configuración mínima N+1, con dos nodos sobrevivientes y réplica de almacenamiento, aplica sólo al clúster de Talca. Concepción y cada cross-docking se dimensionan con un nodo por sitio, como fija el apartado 4.2.2. En Talca el mínimo lo fija la redundancia, no la carga: la configuración cubre 3×, es decir, un margen de crecimiento de +200 % sobre la carga actual.

<a id="sec:dimensionamiento-nube"></a>
### 4.2.6.9 Capacidad en nube

La plataforma utiliza Fargate, Aurora, ElastiCache, SQS, IoT Core, DynamoDB y S3 como servicios administrados. Una tarea entrega 14 solicitudes por segundo al 70 % de uso con 50 ms de CPU. La Tabla [23](#tab:dimensionamiento-nube) separa el portal y compara cada perfil con el techo de ocho tareas.

<a id="tab:dimensionamiento-nube"></a>
**Tabla 23.** Procesos Fargate por perfil
| Perfil | Carga | Tareas | Techo | Conclusión |
| --- | --- | --- | --- | --- |
| Régimen normal | 12,30 solicitudes/s (nube + portal) | 2 | 8 | Cumple |
| Peak de septiembre | 14,66 solicitudes/s (nube + portal) | 2 | 8 | Cumple |
| Prueba RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21) | 21,99 solicitudes/s totales, distribuido por perfil horario | 2 | 8 | Una sola multiplicación |
| Cota extrema | 48,37 solicitudes/s (5,03 + 43,33) | 4 | 8 | Bajo el techo |
| Sensibilidad 120 solicitudes | 21,93 / 91,70 solicitudes/s; régimen / cota | 2 / 7 | 8 | Bajo el techo |

El portal en régimen usa 9,63 solicitudes/s y 96,30 sesiones concurrentes; su cota extrema usa 43,33 solicitudes/s y 433,33 sesiones concurrentes. Con 120 solicitudes por sesión, manteniendo las sesiones repartidas en la hora, el portal alcanza 19,27 solicitudes/s en régimen y 86,67 en la cota extrema; al sumar la nube resultan 21,93 y 91,70 solicitudes/s, que requieren 2 y 7 tareas. El parámetro se mantiene bajo el techo de ocho, pero se perfila en la prueba de carga.

<a id="sec:dimensionamiento-plan"></a>
### 4.2.6.10 Plan de capacidad

La Tabla [24](#tab:dimensionamiento-plan) mantiene separadas la proyección del año 3 y la exigencia técnica de 3×. Cada fila tiene una acción concreta de operación o ampliación.

<a id="tab:dimensionamiento-plan"></a>
**Tabla 24.** Proyección y crecimiento de capacidad
| Componente | Año 1 | Año 3 | 3× | Acción |
| --- | --- | --- | --- | --- |
| WMS de Talca, TPS peak | 3,02 | 3,02 × (305.000 ÷ 260.000) = 3,54 | 9,06 | Revisar CPU e IOPS trimestralmente |
| Nube, TPS peak / tareas | 14,66 / 2 | 14,66 × (36.000 ÷ 31.000) = 17,03 / 2 | 43,98 / 4 | Escalamiento automático y prueba trimestral |
| Evidencia anual | 87,72 GB | 87,72 × (36.000 ÷ 31.000) = 101,87 GB | 263,16 GB | Escalar S3 y revisar retención |
| Enlace de Talca, peor caso | 5,30 Mbps | 5,34 Mbps, con los flujos de volumen × 305.000 ÷ 260.000 | 8,71 Mbps | Ampliar D-03 si el percentil 95 supera la cota |
| Terminales de bodega de Talca | 132 | (23 + 3) de congelado + (113 + 12) estándar = 151 | no aplica | Ajustar parque a la dotación |
| Mesa de ayuda, contactos | 2.000/mes | 2.000 × (350 ÷ 310) = 2.258/mes | 6.000/mes | Recalibrar Erlang C trimestralmente |

La nube escala automáticamente dentro del techo declarado; nodos, almacenamiento local, Wi-Fi y enlaces requieren revisión planificada. La gestión trimestral compara la proyección observada con la cota de 3× y con la incorporación de nuevas unidades.

<a id="sec:dimensionamiento-cuello"></a>
### 4.2.6.11 Cuello de botella, umbrales y degradación controlada

El primer candidato es la emisión de guías del ERP. En el peak se emiten unos 2.852 documentos tributarios electrónicos (DTE) al día. El tiempo disponible por guía depende de la ventana:

- Entre 22:00 y 05:30: máximo de 9,47 segundos por guía.
- En las últimas 3,5 horas: máximo de 4,42 segundos por guía.
- En la ventana actual de despacho: máximo de 1,89 segundos por guía.

La solución emite la guía cuando confirma la carga, durante la noche. Se detectan guías aún no emitidas frente a la hora de salida de cada camión y se prioriza la cola, sin crear un segundo emisor: el ERP conserva la responsabilidad tributaria y la guía acompaña el traslado. Como el caso no documenta las interfaces del ERP y encarga levantarlas en los primeros meses (Bases Técnicas del caso, Cap. 5, p. 10), el tiempo real por guía se mide en ese levantamiento; si superara los 4,42 segundos, las cargas se cierran por camión en el orden de salida, para que la emisión empiece antes.

La Tabla [25](#tab:t84) fija los umbrales de respuesta que se observan en percentil 95.

<a id="tab:t84"></a>
**Tabla 25.** Umbrales de respuesta en percentil 95
| Operación | Umbral | Fuente |
| --- | --- | --- |
| Confirmación de línea de preparación | 1 s | Bases Técnicas del caso, Cap. 15, p. 26 |
| Registro de entrega | 2 s | Bases Técnicas del caso, Cap. 15, p. 26 |
| Línea de preventa | 1,5 s | Bases Técnicas del caso, Cap. 15, p. 26 |
| Consulta de stock y crédito | 2 s | Bases Técnicas del caso, Cap. 15, p. 26 |
| Transacción crítica de terreno | 3 s | Bases Técnicas Transversales, Cap. 9, p. 21 |
| Carga inicial del portal | 2 s | Bases Técnicas Transversales, Cap. 9, p. 21 |
| Navegación | 1 s | Bases Técnicas Transversales, Cap. 9, p. 21 |
| API de consulta | 500 ms | Bases Técnicas Transversales, Cap. 9, p. 21 |
| API de escritura | 800 ms | Bases Técnicas Transversales, Cap. 9, p. 21 |
| Búsqueda compuesta | 3 s | Bases Técnicas Transversales, Cap. 9, p. 21 |
| Informe estándar | 30 s | Bases Técnicas Transversales, Cap. 9, p. 21 |

Los otros candidatos son la base WMS, los IOPS, la Wi-Fi y el drenaje. Se detectan con percentil 95, longitud de colas, errores, retransmisiones y tiempo de sincronización. Si se supera una cota, se encola con clave idempotente, se limita la tasa y se muestra un mensaje explícito; no se pierden ni duplican pedidos.

<a id="sec:dimensionamiento-pruebas"></a>
### 4.2.6.12 Validación mediante pruebas de carga y estrés

La prueba RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21) carga una sola vez 1,5 × la dimensión 3, es decir, 21,99 TPS totales. La Tabla [26](#tab:t86) vincula cada ensayo con la decisión que debe cerrar.

<a id="tab:t86"></a>
**Tabla 26.** Pruebas que confirman el dimensionamiento
| Prueba | Carga | Qué confirma | Criterio |
| --- | --- | --- | --- |
| Carga RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21) | 21,99 TPS totales, distribuidos por lugar según el perfil horario | CPU, Fargate, portal, WMS, base e IOPS | Percentil 95 |
| Estrés RT-09.06 (Bases Técnicas Transversales, Cap. 9, p. 21) | Sobre cota extrema portal y 3× | Umbral de quiebre y degradación | Sin pérdida ni duplicación |
| Corte de enlace | 24 h y drenaje en 2 h | WAL, broker, telemetría y observabilidad | Drenaje completo |
| Sincronización de dispositivo | Peor ruta en 10 min | 0,13 Mbps efectivos | Ruta reconciliada |
| Migración | Dos ensayos independientes | Volumen y calidad histórica | Conciliación de dominios |
| Ventana dominical | Respaldo y actualizaciones | Tandas por sitio y enlace | Cada tanda cabe |

La prueba de carga conserva tasas por lugar, percentil 95, utilización, colas, errores y comportamiento durante el drenaje; incluye la concurrencia de oficina y trabajo remoto por Verified Access, la API privada, el inicio de sesión y los tableros. Los parámetros confirmados se actualizan en la revisión trimestral de capacidad.

<a id="sec:dimensionamiento-sintesis"></a>
### 4.2.6.13 Síntesis de las dieciséis dimensiones del numeral 14.2

La Tabla [27](#tab:t72) reúne cada dimensión con el nombre literal del Caso 14.2, su valor normal o de ventana, su valor peak o declarado y la derivación correspondiente.

<a id="tab:t72"></a>
**Tabla 27.** Síntesis de las dieciséis dimensiones
| N.° | Dimensión | Valor en régimen normal o ventana | Valor en peak o declarado | Derivación |
| --- | --- | --- | --- | --- |
| 1 | Transacciones por segundo en régimen normal | 12,30 TPS a las 12:00 | – | Anexo 4.B, sección 4.B.2 |
| 2 | Transacciones por segundo en el peak de la ventana de despacho de 05:30 a 07:00 | 1,68 TPS | 3,05 TPS | Anexo 4.B, sección 4.B.2 |
| 3 | Transacciones por segundo en el peak de septiembre | – | 14,66 TPS a las 12:00 | Anexo 4.B, sección 4.B.2 |
| 4 | Personas usuarias registradas, internas y externas | 15.180 | – | Anexo 4.B, sección 4.B.3 |
| 5 | Personas usuarias concurrentes en peak | 438,30 en régimen; 342 sin portal | 775,33, cota extrema | Anexo 4.B, sección 4.B.3 |
| 6 | Dispositivos de terreno en operación simultánea | 158 | 158 | Anexo 4.B, sección 4.B.3 |
| 7 | Volumen anual de almacenamiento transaccional | 50,75 GB/año | 7,85 GB mes peak | Anexo 4.B, sección 4.B.4 |
| 8 | Volumen anual de almacenamiento de evidencia de entrega, firmas y fotografías | 87,72 GB/año | 13,58 GB mes peak | Anexo 4.B, sección 4.B.4 |
| 9 | Volumen anual de almacenamiento de series de temperatura y de posicionamiento | 0,56 + 3,20 GB/año crudos | 2,80 + 3,20 GB crudos retenidos | Anexo 4.B, sección 4.B.4 |
| 10 | Volumen total de datos históricos a migrar | 32,11 GB | 30,73–33,49 GB de sensibilidad | Anexo 4.B, sección 4.B.4 |
| 11 | Número de integraciones y volumen de mensajes por integración | 15; 175.661 mensajes/día | 257.155 mensajes/día | Anexo 4.B, sección 4.B.5 |
| 12 | Ancho de banda requerido por sitio, en régimen y en peak | 3,71 / 0,11 / 0,05 Mbps cargados | 5,30 / 0,77 / 0,35 Mbps peor caso | Anexo 4.B, sección 4.B.5 |
| 13 | Volumen de datos generado por un dispositivo de reparto en un turno completo sin señal | 5,36 MB promedio | 9,83 MB, ruta de 34 clientes | Anexo 4.B, sección 4.B.6 |
| 14 | Tiempo de sincronización de la flota al regresar al centro de distribución | 10 min por dispositivo | 10 min después del último camión | Anexo 4.B, sección 4.B.6 |
| 15 | Contactos mensuales a la mesa de ayuda | 2.000 contactos/mes | 2.000 contactos/mes en el escenario conservador; 7 agentes cubren hasta 2.391 | Anexo 4.B, sección 4.B.7 |
| 16 | Dotación de la mesa de ayuda y del equipo de operación | 7 + 8 = 15 personas a 42 h | 7 + 2 + 8 = 17 personas en peak | Anexo 4.B, sección 4.B.7 |

El diseño queda gobernado por tres condiciones operativas. La primera es la emisión de guías del ERP antes de la salida de cada camión, que es la única de las tres cuya capacidad no controla la solución y que por eso se mide primero. La segunda es el enlace de Talca durante el retorno de la flota, cuando la sincronización de los dispositivos se suma al tráfico de oficina. La tercera es el almacenamiento de la evidencia de entrega, que es el volumen que más crece y el que fija la política de niveles de S3. El resto de las dimensiones queda con holgura amplia frente a la capacidad propuesta, incluso con el crecimiento de 3×.
