# Revisión de coherencia: Excel, Entregable 2 y subdocumentos CORRIGIENDO

**Corte de revisión: 15 de noviembre de 2026, America/Santiago. Solo diagnóstico y correcciones propuestas.**

## Dictamen

**Los tres conjuntos todavía no constituyen una línea base económica coherente para entregar.** La aritmética central del Excel concilia, pero el Entregable 2 está desactualizado y existen diferencias de atribución, calendario y alcance que una simple actualización de cifras no resolvería.

Lo más importante:

1. El costo vigente del Excel es **200.329,13 UF** y el precio neto **235.643,21 UF**, no 200.024,98 y 235.308,64 UF. Cambian 55 de las 56 filas del flujo del Entregable 2.
2. Las **200.783,82 HH de los 37 perfiles sí concilian** con el T-15. Las 1.324,80 HH restantes son servicios especializados, no una omisión automática de personal.
3. Las **5.552 HH de innovaciones coinciden en total**, pero no sus perfiles, costo atribuido ni calendario. Cinco combinaciones perfil/mes exceden el presupuesto disponible.
4. No se demuestra la cobertura económica de la nube productiva anterior al mes 21, de los dos controladores inalámbricos ni de todos los servicios independientes.
5. Los beneficios de innovaciones se suman sin demostrar la exclusión de solapamientos que exige el T-19. La caja positiva del escenario base tampoco resiste cualquier atraso de un hito.

Se identifican **18 observaciones**, agrupadas abajo por causa. «Alta» significa que debe resolverse antes de considerar conciliada la oferta; no es una declaración de inadmisibilidad legal. Se distingue error confirmado de cobertura no demostrada. No se cambiaron documentos, fórmulas, precios ni ramas de trabajo.

## 1. Fuentes y método

### Excel vigente

[Archivo revisado en Google Drive](https://docs.google.com/spreadsheets/d/18wI3xm9e1alpcn0JKE8CJcjPKg3G4-UP/edit?gid=1717014239#gid=1717014239), título observado: **LafroX_ModeloFinanciero_3_20261113.xlsx**. Es un XLSX editado desde Google, no se trató como una hoja nativa nueva.

Se exportó una copia de lectura con sus **19 hojas**, fórmulas y valores almacenados. SHA-256 de la copia: `60bd12ea1e06df74795703d467522bde6c50977c6594d43360edd6f34713e5e0`.

### Entregable 2

Rama `LafroX-OfertaEconomica-2-Latex`, commit `68595089`, contrastado con las fuentes del checkout, sin cambios previos rastreados. Se revisaron las siete secciones y se extrajo el texto de los dos PDF locales de 36 páginas, que mantienen las cifras antiguas. No se declara una auditoría visual completa de los PDF.

Entrada: [fuente principal](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/LAFROX_AnalisisFinanciero_2_20261113.tex). Capítulo y secciones: [contenido](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/02_analisis_economico_financiero/contenido.tex).

### Subdocumentos

Se actualizó `origin` mediante fetch, sin cambiar de rama, hacer merge, commit ni push. Para SD8, que no tiene rama denominada CORRIGIENDO, se usó la rama **Revision**, no la antigua. Se revisaron las fuentes vigentes y sus tablas relacionadas. La rama de anexos se consultó solo como complemento; no sustituyó a las versiones CORRIGIENDO por tener un commit más reciente.

| Documento | Referencia revisada | Commit |
|---|---|---|
| SD1 | `origin/LafroX-Subdoc1-LateX-CORRIGIENDO` | `278a4c41` |
| SD2 | `origin/LafroX-Subdoc2-LateX-CORRIGIENDO` | `a72407bc` |
| SD3 | `origin/LafroX-Subdoc3-LateX-CORRIGIENDO` | `40d415db` |
| SD4 | `origin/LafroX-Subdoc4-LateX-corrigiendo` | `69c9a879` |
| SD5 | `origin/LafroX-Subdoc5-LateX-CORRIGIENDO` | `daec1657` |
| SD6 | `origin/LafroX-Subdoc6-LateX-corrigiendo` | `b18698ec` |
| SD7 | `origin/LafroX-Subdoc7-LateX-CORRIGIENDO` | `68669bef` |
| SD9 | `origin/LafroX-Subdoc9-LateX-corrigiendo` | `0c57a4bb` |
| SD13 | `origin/LafroX-Subdoc13-LateX-corrigiendo` | `dd509aa1` |
| SD8 | `origin/Lafrox_Subdocumento_8_Latex_Revision` | `20289fe0` |

Los SD10–12 no se presentan como revisados: no son las versiones CORRIGIENDO que sustentan este cruce del Informe/Entregable 2.

### Alcance de las comprobaciones

- Lectura de las 19 hojas y barrido de errores almacenados, más revisión de referencias y fórmulas relevantes.
- Conciliación independiente de ingresos, costos, VAN, financiamiento, HH, innovaciones y cobertura de operación.
- Cruce de los 37 perfiles y lectura estructurada de las 227 partidas de asignación del T-15.
- Comparación de los 56 meses publicados en E2 con el Excel vigente.
- Contraste de adquisiciones, responsabilidad de compra, servicios, soporte, riesgos, calidad e innovaciones con T-11, T-14, T-15, T-19 y anexos relacionados.
- Uso de las bases contractuales disponibles en el repositorio como criterio de coherencia, especialmente E-21, E-24, E-25 y E-26.

**Límites:** no se recalcularon todas las fórmulas en Excel de escritorio ni se validaron cotizaciones comerciales vigentes, permisos del archivo en Google, implementación real, firmas, homologaciones ni suficiencia legal. El VAN y varios totales se recalcularon independientemente desde los valores mensuales de la exportación. No encontrar una partida identificable no demuestra que un proveedor no la haya incluido en un paquete; demuestra que falta trazabilidad para acreditarlo.

## 2. Diferencias numéricas que debe corregir E2

Valores en UF. Las cifras vigentes siguientes describen **el modelo tal como está**, no el presupuesto final luego de resolver sus brechas de alcance.

| Concepto | E2 publicado | Excel vigente | Diferencia aprox. | Fuente Excel |
|---|---:|---:|---:|---|
| Costo implementación | 88.884,92 | 89.102,44 | 217,52 | `RESUMEN!B10` |
| Costo operación | 111.140,06 | 111.226,69 | 86,63 | `RESUMEN!B11` |
| Costo total | 200.024,98 | 200.329,13 | 304,15 | `RESUMEN!B12` |
| Precio implementación | 105.093,38 | 105.332,65 | 239,27 | `RESUMEN!G10` |
| Precio operación | 130.215,27 | 130.310,57 | 95,30 | `RESUMEN!G11` |
| Precio neto total | 235.308,64 | 235.643,21 | 334,57 | `RESUMEN!G12` |
| Margen monetario | 35.283,66 | 35.314,08 | 30,42 | `RESUMEN!L12` |
| VAN antes de impuestos | 24.691,13 | 24.714,56 | 23,43 | `INDICADORES!B5` |
| Cuota mensual de operación | 3.617,09 | 3.619,74 | 2,65 | `RESUMEN!G11 / 36` |
| Mínimo de caja financiada | 489,87 | 457,68 | -32,19 | `FLUJO CAJA NETO!M8` |
| Caja final financiada | 35.399,78 | 35.430,19 | 30,41 | `FLUJO CAJA NETO!BH8` |

El margen porcentual sigue redondeando a **14,99 %**. La TIR mensual sigue redondeando a **7,13 %**; la anual vigente es **128,45 %**, frente a 128,44 % en E2. La tasa mensual de descuento sigue siendo 0,997768607 %. Estas coincidencias de redondeo no vuelven coherentes las cifras monetarias antiguas.

También cambian IVA y conversiones CLP/USD, importes de cada hito, cuadros anuales, sensibilidad, equilibrio, gráfico de Curva S y su explicación. El costo actual de proveedores es **4.689,66 UF** en implementación y **25.710,16 UF** en operación. Los gastos administrativos son **9.822,14 UF** en total, con **6.229,67 UF** en operación.

## 3. Hallazgos y correcciones propuestas

### C01 · Alta — E2 no reproduce el Excel vigente

**Evidencia.** Introducción y secciones 2.1–2.3, 2.5: cifras de la tabla anterior. Los PDF conservan esas cifras. El contraste mensual detecta **55 de 56 filas** con alguna diferencia superior a 0,011 UF, descartando diferencias de impresión de una centésima.

**Impacto.** Se entregan dos precios y dos evaluaciones distintas. No basta corregir la primera página: las dependencias incluyen flujo mensual, cuadros anuales, IVA, sensibilidad, punto de equilibrio y series gráficas.

**Propuesta.** Resolver primero las brechas del modelo descritas abajo. Después fijar una única versión, regenerar todas las tablas y gráficos desde sus celdas, compilar y volver a comparar. No hacer sustituciones globales de números sin identificar su origen.

### C02 · Media — E2 describe servicios fijos que el Excel ya calcula por mes

**Evidencia.** E2 2.4–2.5 presenta nube de 368,92 UF/mes e Intune de 29,05 UF/mes para 382 equipos durante toda la operación. El Excel mantiene esos valores como base de catálogo, pero `COSTOS!W63:BF63` ajusta QA por calendario y `COSTOS!AA69:BF69` aplica el escalón de Intune a 433 equipos desde M25 (`PARAMETROS!C73:C75`).

La nube operacional vigente suma **13.243,25 UF**, no 13.280,97 UF. Intune suma **1.169,95 UF**, no 1.045,84 UF: 4 meses con 382 equipos y 32 con 433. La diferencia de Intune es **124,11 UF**. No se propone sumar ese incremento otra vez: ya está incorporado en COSTOS.

**Propuesta.** Separar precio unitario, parque y calendario. Presentar costo mensual variable y total real, y explicar que el catálogo base no representa todos los meses. Actualizar también la nube de implementación: ya no son 32,03 UF fijas por mes.

### C03 · Alta — Las innovaciones se valorizan con perfiles distintos a los asignados en T-15

**Evidencia.** `INNOVACIONES!A24:K63` y E2 2.7 simplifican la inversión de INN-02 a QA Senior, INN-04 a Jefe de Proyecto e INN-05 a Coordinador. La tabla de asignación del T-15 reparte esas partidas entre varios perfiles.

Aplicando a **los perfiles de cada partida** los costos UF/HH del mismo Excel:

| Innovación | HH coincidentes | Costo HH atribuido en Excel | Costo HH según asignación T-15 | Diferencia T-15 − Excel |
|---|---:|---:|---:|---:|
| INN-01 | 960,00 | 768,00 | 768,00 | 0,00 |
| INN-02 | 1.536,00 | 752,18 | 726,95 | -25,23 |
| INN-03 | 1.248,00 | 998,40 | 998,40 | 0,00 |
| INN-04 | 688,00 | 997,60 | 650,63 | -346,97 |
| INN-05 | 1.120,00 | 672,00 | 778,87 | 106,87 |
| **Total** | **5.552,00** | **4.188,18** | **3.922,85** | **−265,33** |

Ejemplo determinante: 8.3.4 tiene 343,20 HH PMO y 184,80 HH JP. A 0,60 y 1,45 UF/HH cuesta **473,88 UF**, no las **765,60 UF** de atribuir las 528 HH al JP. En INN-01/03 la mezcla de Datos no cambia el total porque esos perfiles tienen el mismo costo de 0,80 UF/HH, pero sigue siendo necesario respetar su asignación.

**Impacto.** La valorización de cada innovación no se reconstruye desde la planificación que se cita como fuente.

**Propuesta.** Derivar la hoja por código EDT, perfil, HH, mes y costo. Con la asignación actual, las HH sumarían 3.922,85 UF; añadiendo la nube actualmente modelada, el subtotal ilustrativo sería **3.967,10 UF**, antes de resolver consumibles y otras brechas. **No es un ahorro automático de 265,33 UF del proyecto**: las personas ya están presupuestadas globalmente; cambia la atribución del costo.

### C04 · Alta — El calendario de costo de innovaciones no es el del T-15/T-19

**Evidencia.**

| Innovación | Excel/E2 | T-15 y T-19 |
|---|---|---|
| INN-01 | 960 HH repartidas M7–M12 | Paquetes 3.10.1.1–4 en M7–9, M9–10, M9–10 y M11–15 |
| INN-02 | 960 HH concentradas en M9–M10 | Instrumentación desde M2–3, circuito M3–5, cobertura M5–10 y validación M11–15 |
| INN-03 | 960 HH repartidas M7–M12 | Familias/parámetros M3–5, borde M5–9, vista M9–10 y validación M11–15 |
| INN-04 | 160 HH repartidas M17–M23 | 5.4.3: 80 HH M17–20; 8.3.3: 80 HH M21–23 |
| INN-05 | 893,4 HH M13–17 y 226,6 HH M18–23 | 3.10.4.1–4 hasta M21; despliegue 8.3.5 hasta M26; bloque 4, 8.3.6, hasta M27 |

Las HH de operación de INN-03 se ubican en meses dispersos en Excel; T-19 exige recalibraciones M26, 32, 38, 44, 50 y 56. T-15 permite distribuir contablemente una actividad recurrente, pero eso debe explicarse como tal y conciliar con su ejecución, no presentarse como el mismo calendario.

**Propuesta.** Llevar las ventanas de las partidas a la valorización. Separar ejecución, devengo presupuestario y pago cuando sean diferentes. Regenerar la figura de egresos de 2.7: su peak M9–10 no es una representación fiel del plan vigente. No confundir además «inversión de una innovación» con «fase contractual M1–20»: ciertas actividades de habilitación siguen después.

### C05 · Alta — Cinco asignaciones de innovaciones exceden el presupuesto perfil/mes

**Evidencia.** Se sumaron todas las HH de innovaciones por perfil y mes y se compararon con `HH POR ROL Y MES!C8:BF44`, respetando las ventanas inclusivas de INNOVACIONES.

| Perfil | Mes | HH solo innovaciones | HH disponibles del rol | Exceso |
|---|---:|---:|---:|---:|
| Analista QA Senior | 10 | 480,00 | 471,28 | 8,72 |
| Líder de Calidad y Pruebas | 39 | 43,50 | 7,56 | 35,94 |
| Analista QA Senior | 53 | 25,40 | 24,20 | 1,20 |
| Analista QA Senior | 55 | 24,10 | 22,98 | 1,12 |
| Coordinador de Implantación | 18 | 37,77 | 21,22 | 16,55 |

En estos casos la innovación supera incluso la totalidad de horas disponibles, antes de reservar otras tareas. Por ello es falsa la afirmación de E2 2.7 de que cada hora está contenida en un perfil/mes presupuestado.

**Propuesta.** Corregir C03–C04 desde las partidas originales y volver a ejecutar este control. No basta comprobar que el perfil tenga alguna hora ese mes ni que el total anual alcance. No sumar horas nuevas para tapar una redistribución incorrecta.

### C06 · Alta — Se suman beneficios que T-19 ordena no acumular sin conciliación

**Evidencia.** `INNOVACIONES!K84=SUM(K79:K83)` produce **53.878,83 UF**, repetidas como beneficio total del CLIENTE en E2. T-19/SD13 indican expresamente que INN-01 y 03 no se suman entre sí ni a la meta de merma; INN-04 tampoco se suma a 01, 03 o 05. Además, el tiempo de decisión del almacenero es beneficio de un tercero, no ingreso ni ahorro de caja automático de Puelche.

**Impacto.** El total mezcla escenarios que no acreditan aditividad y beneficiarios distintos. El Excel sí hace la suma aritmética, pero no demuestra que sea un beneficio económico agregado válido.

**Propuesta.** Mantener beneficios por innovación y beneficiario, sin total aditivo, hasta construir una matriz de exclusión y atribución por evento/lote/entrega. Separar el beneficio económico incremental del cliente del beneficio del almacenero. Conservar fuera del flujo de LafroX estos ahorros, como ya hace el modelo.

### C07 · Media — La escala y la valoración de beneficios no siguen la adopción y el alcance comparables

**Evidencia.** B-01 aplica la reducción a todas las 2,4 millones de unidades mensuales; el servicio posentrega y su piloto están definidos para locales/rutas elegibles del canal tradicional. B-03 convierte proporción de SKU de frío en proporción de recepciones/lotes, aunque esa equivalencia no está demostrada. B-04 usa 31.000 pedidos, mientras T-19 habla de entregas comparables. B-05 usa todas las visitas estimadas al canal tradicional desde M21, pero el despliegue se completa por olas hasta M26–27 y depende de aceptación.

SD13 también exige descontar canjes y descuentos en el beneficio de INN-01. E2 reconoce que valora a precio de venta y usa máximos, lo que es una cautela útil, pero no reemplaza ese ajuste ni una base elegible. Los cocientes entre SKU, lotes, visitas y canales deben figurar como supuestos de extrapolación, no como mediciones.

**Propuesta.** Usar volumen elegible × cobertura por ola × adopción × cambio causal validado × valor neto evitado. Mantener los supuestos no medidos como escenarios, sin presentarlos como ahorro realizado ni utilizar la cifra agregada para justificar rentabilidad del proveedor. Estimar por separado el costo de intervención/canje y el margen o pérdida realmente evitada.

### C08 · Alta — No se demuestra el costo de la nube productiva antes del mes 21

**Evidencia.** SD4, despliegue, declara cinco ambientes habilitados en H3/M6 y marcha blanca ya en Producción; SD9 aplica G5 a datos/pedidos reales desde M13 y M19. Sin embargo, `COSTOS!D63:V63` usa la estructura de implementación y el cálculo titulado «ambientes no productivos por horario», con Fargate/Aurora de lunes a viernes de 08:00 a 20:00 y cero unidades fuera de horario. La estructura completa operacional empieza en `W63`, M21. Entre M13 y M20 la fila de nube suma solo **346,62 UF**.

**Impacto.** No hay separación auditable que demuestre una base productiva y de recuperación activa compatible con la marcha blanca, producción E1 y operación nocturna. No se afirma que todo el costo operacional deba adelantarse intacto desde M6: es necesario dimensionar cada etapa.

**Propuesta.** Separar DEV/QA/PREPROD de PROD/DR, con alta, recursos mínimos y horario por ambiente. Presupuestar explícitamente la disponibilidad productiva desde el hito técnico que corresponda y desde el uso real de M13. Aplicar apagados únicamente a recursos no productivos elegibles. Recalcular costos, precio, VAN y capital si la conciliación incorpora nuevos importes.

### C09 · Alta — Dos controladores inalámbricos comprometidos no tienen partida identificable

**Evidencia.** T-11 y Anexo 4-W.13 ofertan **dos Cisco CW9800L**, fuentes redundantes CW9800L-RPS y montaje. La implementación detalla switches, 72 AP y otros equipos, pero `ADQUISICIONES IMPLEMENTACIÓN!A15:I23` y PROVEEDORES no identifican los controladores ni su inclusión en otra compra. No son los switches C9300/C9200 ni los 72 AP.

Hay además repuestos por componente comprometidos en T-11 —SSD/fuente de Concepción y disco de NAS— que no se individualizan: el Excel compra cuatro discos NAS y el T-11 describe cuatro instalados más un repuesto.

**Propuesta.** Incorporar cada componente o identificar exactamente el paquete/cotización que lo cubre, con cantidad, accesorios, licencias y costo. Para partidas agregadas como UPS N+1 y gabinetes no inferir suficiencia por cantidad «1»: adjuntar su despiece. La brecha es de cobertura demostrable, no una autorización para inventar precios.

### C10 · Alta — Servicios especializados del T-15 sin conciliación económica explícita

**Evidencia.** T-15 separa **1.324,80 HH** del código 00: 864 HH de implementación y 460,80 de operación. Incluyen 320+160 HH de pruebas ofensivas independientes, 384 HH de instalaciones especializadas y 230,40+230,40 HH de ciberseguridad y revisión eléctrica en operación.

Las instalaciones podrían estar incluidas en compras «con montaje»/obras; por tanto no deben sumarse otra vez automáticamente. Pero el modelo no aporta un puente código 00 → proveedor → contrato/partida → costo/mes. No se identifica una partida propia de pruebas independientes en PROVEEDORES. E2 2.4 dice que LafroX hace las pruebas de aceptación, sin distinguir suficientemente las pruebas que deben ejecutar terceros.

**Propuesta.** Preparar ese puente. Registrar lo ya incluido en equipos/obras con evidencia; valorizar lo no cubierto con su modalidad contractual. No convertir las 1.324,80 HH en personal de nómina ni tratarlas a una tarifa genérica. Aclarar qué aceptación coordina LafroX y qué prueba ejecuta un tercero independiente.

### C11 · Media — La tabla de mantención usa promedios que no reproducen sus paquetes

**Evidencia.** E2 2.6 aplica 0,68 UF/HH a Desarrollo y 0,96 a SRE/DevOps, obtenidos de grupos globales, y atribuye 2.576 HH preventivas a estos últimos. El T-15 asigna mezclas diferentes en cada partida y **230,40 HH de 8.2.6 a un tercero**.

Ejemplos de conciliación con los costos horarios actuales:

- 8.2.1, correctivo + evolutivo: **3.134,59 UF** por su mezcla de perfiles; las dos líneas de E2 suman 3.128,84 UF. El reparto de 50/50 entre correctivo y evolutivo debe declararse como supuesto del desglose si no está fijado por perfil.
- 8.2.4, deuda técnica: **1.558,66 UF**, frente a 1.564,42 UF.
- 8.2.5 + 8.2.7: **1.080,00 UF**, frente a 1.105,18 UF.
- Preventiva 8.1.3 + 8.1.6 + 8.2.3 + parte interna de 8.2.6: **2.183,88 UF de personal interno, más el servicio externo**, cuyo precio no se demuestra. No es equivalente a afirmar un total conciliado de 2.471,31 UF.

**Propuesta.** Sustituir promedios por suma de HH × costo de los perfiles de cada paquete y separar contratistas. Esto corrige atribuciones dentro de costos ya presupuestados; no corresponde añadir todos los subtotales al costo total otra vez.

### C12 · Media — Proveedores y canales económicos distintos a los de la arquitectura

**Evidencia.** SD4/T-11 y catálogo INT-11 declaran SES, SNS y AWS End User Messaging Social, con 2.800/5.200 avisos diarios y costo unitario por canal remitido a la Oferta Económica. PROVEEDORES/servicios externos y E2 mencionan Twilio y Mercado Pago; la fórmula de servicios de operación utiliza 2.000 mensajes y una comisión de 3,19 % sobre 20 millones CLP sin un puente hacia la mezcla y volúmenes del diseño. La arquitectura identifica Transbank entre sus dependencias de pago.

Para la fibra, T-11 prioriza Telsur y reserva otro operador fijo distinto de Entel si no hay factibilidad; E2 y PROVEEDORES presupuestan Entel mientras parte del respaldo LTE también es Entel.

**Propuesta.** Una única matriz servicio/proveedor/canal/volumen/unidad/precio/pagador. Explicar una alternativa aprobada o usar el proveedor del diseño. No asumir que cotizar otro proveedor satisface la diversidad de operadores ni sumar ambos servicios sin descartar duplicación. Separar comisiones de cobro de costos de integración y precisar quién las paga.

### C13 · Media — INN-05 compromete papel y explicación, pero su costo incremental queda en nube

**Evidencia.** T-19 campo 11 incluye papel térmico de copias pedidas y minutos de explicación en la visita. Anexo 4-W distingue el costo por copia de la generación mensual. E2/INNOVACIONES muestran solo **1,16 UF** de costo operacional no-HH de INN-05, correspondiente a nube, sin cantidad/precio de copias ni atribución de ese tiempo. Que el hardware del CLIENTE incluya un rollo inicial no cubre 36 meses de consumo.

**Propuesta.** Definir pagador, tasa de solicitud de copias, papel/merma por copia y tiempo incremental por visita. Si los absorbe el CLIENTE, mostrarlos como costo de adopción del cliente, no ocultarlos ni cargarlos sin más a LafroX. Si las horas ya están incluidas, referenciar su paquete para no duplicarlas.

### C14 · Alta — La línea de respaldo no basta para el atraso de H4 de un mes

**Evidencia.** E2 2.3 presenta una línea de 1.250 UF como respaldo ante atrasos de un hito. En el modelo vigente la caja financiada de M10 es **8.353,03 UF** y H4 suma **10.533,26 UF**.

Prueba independiente, sin modificar el archivo: mover solo H4 de M10 a M11, manteniendo los demás flujos. En M10:

`8.353,03 − 10.533,26 = −2.180,24 UF`.

Incluso usando el máximo de la línea:

`−2.180,24 + 1.250,00 = −930,24 UF`, antes de intereses de esa línea.

**Impacto.** El escenario base sí tiene caja positiva; no es correcto extender esa conclusión a cualquier atraso. La sensibilidad de «ingresos ±20 %» cambia montos, no fechas, y la de «costo HH» cambia costo monetario, no nivelación ni capacidad de personas.

**Propuesta.** Añadir sensibilidad temporal de hitos y su efecto en caja, intereses, línea y capital. Identificar los atrasos que cubre realmente el respaldo y los que exigen más capital o medidas de cobro/costo. Retirar la afirmación genérica de cobertura por reservas: una reserva de HH no equivale a caja bancaria.

### C15 · Media — El Resumen muestra dos nociones de «total del proyecto» sin puente de alcance

**Evidencia.** `RESUMEN!B35:B37` presenta 47.768,44 HH, costo 36.575,17 UF y venta 44.168,35 UF según puntos de caso de uso. La línea base T-15 es 202.108,62 HH y el total financiero vigente 200.329,13/235.643,21 UF. El encabezado «Viabilidad y HH» ayuda a reconocer otra estimación, pero no establece qué fases, servicios, paquetes o esfuerzo cubre y excluye.

**Propuesta.** Rotularlo como estimación alternativa de alcance específico, identificar el perímetro y conciliarlo con la EDT. No comparar esfuerzo de programación/ampliado por UCP con 56 meses de cobertura y soporte como si fueran el mismo total ni utilizar ambas cifras como precio de oferta.

### C16 · Baja — Encabezados de HH conservan totales manuales de otra versión

**Evidencia.** `HH POR ROL Y MES!B9=5.354`, frente a 4.737,83 HH de ese perfil en Sueldos; `B31`, `B32` y `B33` tampoco reproducen el total del perfil anunciado por el encabezado. En particular, Instructor muestra 496 frente a 512 HH mensuales sin capacitación y 4.008 HH incluyendo su capacitación.

**Propuesta.** Elegir y rotular «total servicio sin capacitación» o «total del perfil incluida capacitación» y enlazar su fórmula. Hay 195.535,82 HH en la matriz mensual más **5.248 HH** separadas de capacitación: suman exactamente 200.783,82. Esa separación es correcta; los encabezados manuales no lo son.

### C17 · Media — La copia XLSX no acredita controles de entrada/protección exigidos por E-21

**Evidencia.** Ninguna de las 19 hojas de la exportación tiene protección de hoja activa. PARAMETROS, HH POR ROL Y MES, INNOVACIONES, PROVEEDORES y las hojas de adquisiciones no contienen validaciones de entrada. Existen algunas validaciones en otras hojas: no se afirma que el archivo carezca totalmente de ellas. E-21 exige validación de entradas y protección de fórmulas críticas.

**Propuesta.** Aplicar validaciones por dominio y proteger cálculos dejando entradas habilitadas. Verificarlo en el XLSX que se vaya a entregar. No confundir celdas marcadas como bloqueadas por defecto con protección activa. Los permisos/protecciones de Google no se auditaron y podrían no trasladarse al XLSX.

### C18 · Baja — Las reservas cuadran en presupuesto, pero no en precisión ni en interpretación

**Evidencia.** SD8 Anexo 8.H define prevención 180 HH, contingencia propuesta 821,13 HH y gestión 160 HH, fuera de las 3.072 HH protegidas ya incluidas en S7. El Excel importa celdas de contingencia redondeadas y suma **821,17 HH**: diferencia de 0,04 HH. Sus importes presupuestados son 722,58 UF en implementación y 314,21 en operación. No se detecta que vuelva a añadir las 3.072 HH al total de riesgos.

SD8 aclara que las propuestas requieren autorización y no garantizan suficiencia ni financiamiento. E2 2.2 afirma que las reservas cubren atrasos de aprobación de hitos y aumento de horas sin demostrar esa correspondencia causal, temporal y de caja.

**Propuesta.** Importar precisión de cálculo o declarar tolerancia de impresión. Separar reserva presupuestada, capacidad programada, gasto esperado y autorización de consumo. No presentar la reserva como póliza ilimitada ni como sustituto del financiamiento. Esta observación no justifica sumar otra vez exposición inicial, remanente, contingencia y protección E1.

## 4. Comprobaciones que sí pasan y no deben «corregirse» por error

| Control independiente | Resultado | Estado |
|---|---:|---|
| Ingresos contractuales vs Resumen | 235.643,2106 | Concilia |
| Costos del proyecto vs Resumen | 200.329,1320 | Concilia |
| VAN independiente | 24.714,5612 | Concilia |
| HH perfiles T15 vs Excel | 200.783,8200 | Concilia |
| HH mensuales + capacitacion vs Sueldos | 200.783,8200 | Concilia |
| Perfiles + servicios especializados vs linea base | 202.108,6200 | Concilia |
| HH innovaciones vs paquetes T15 | 5.552,0000 | Concilia |
| Total intereses contrato | 3.683,8858 | Concilia |
| Saldo final financiado | 35.430,1928 | Concilia |
| Porcentajes hitos | 1,0000 | Concilia |
| Horas SOC operacion por calendario | 26.280,0000 | Concilia |
| Horas Mesa N1 operacion | 38.246,0000 | Concilia |
| Horas NOC operacion | 21.748,2000 | Concilia |
| Costo innovaciones nube una vez | 44,2562 | Concilia |

También se comprobó:

- Los 37 perfiles tienen el mismo total HH acumulado en T-15 y Sueldos. Las diferencias por fase/calendario no se calificaron como horas faltantes: T-15 explica su criterio de imputación.
- No aparecieron errores de celda almacenados tipo REF, DIV/0, VALUE, NAME, N/A, NUM o NULL en la copia leída. Esto no prueba que todas las fórmulas sean correctas ni sustituye probar recalculación nativa.
- Las tarifas de los perfiles no están por debajo de las mínimas consignadas en la misma hoja; el control no detectó infracción de ese límite. La conversión del E-24 es coherente: USD 900, UF 40.000, IVA 19 %, 56 meses, crédito 0,9 % mensual y línea 3 %.
- Los porcentajes de los doce hitos suman 100 % y sus meses son los del E-25. La operación factura M21–56.
- Separar flujo puro para VAN de flujo financiado para liquidez es correcto. No deben mezclarse aporte de socios y deuda con ingresos comerciales para «mejorar» el VAN.
- El pago variable de INN-04, hasta 330 UF, se mantiene fuera del precio/VAN base; no se contó como ingreso seguro.
- Los equipos de terreno del CLIENTE están separados del flujo de LafroX. Sus cantidades iniciales y de año 3 no deben añadirse al costo del proveedor sin cambiar la responsabilidad contractual.
- El SOC comienza en M13; el soporte puente y la cobertura posterior son reconocidos en las HH. Los costos de formación están separados de las HH de servicio.
- Las 12.016 HH de calidad del SD9 son un subconjunto de la línea base, no una partida completa nueva a añadir a las 202.108,62 HH.
- La energía consumida en recintos del CLIENTE se explica como su cargo en E2; no se detectó contradicción de pagador en esa descripción. La suficiencia técnica del consumo/PUE no se certifica con este control financiero.

## 5. Cobertura documental y asuntos que siguen sujetos a evidencia

| Documento | Cruce efectuado | Resultado principal |
|---|---|---|
| SD1 | Procedencia de planta, Mesa/SOC y perfiles | No confundir 133 especialistas de planta con 137 plazas de diversas procedencias; no es por sí solo un exceso de plantilla |
| SD2 | Volúmenes, objetivos y merma frente a valorización | La mejora obligatoria y la innovación no deben apropiarse del mismo beneficio |
| SD3 / T-12 | Alcance y paquetes hacia estimación/arquitectura | Se usó como trazabilidad de alcance; no se reestimó individualmente cada requisito funcional |
| SD4 / T-11 / 4-W | Equipos, servicios, ambientes, cobertura y dimensionamiento | Brechas C08–C09 y C12; parque/crecimiento Intune reconocido en Excel |
| SD5 | Datos, migración y separación de responsabilidades | No se identificó una discrepancia monetaria independiente adicional; no se certifica costo detallado de cada política de retención |
| SD6 / anexos / T-9 | Hacer/comprar, calendario y terceros | Secuencia de sala M2 compra/M3 instalación/M4 recepción coincide con E2; separar terceros de pruebas y montaje |
| SD7 / T-14 / T-15 / T-18 | 227 partidas, 37 perfiles, ventanas, soporte y HH | Totales conciliados; atribución y temporalidad de innovaciones no conciliadas |
| SD8 / T-16 / 8.H | Reservas, no duplicación, perfiles y autorización | Precisión menor y necesidad de no prometer cobertura automática |
| SD9 / T-13 / T-17 | Calidad, puertas y producción real en marcha blanca | Refuerza necesidad de nube/terceros; calidad no se suma dos veces |
| SD13 / T-19 | Cinco innovaciones, indicadores, madurez, calendario y costos | Principales diferencias de atribución, calendario, aditividad y adopción |

### Confirmaciones necesarias para cerrar, no errores cuantificados adicionales

1. **Importaciones:** precio puesto en sitio, flete, seguro, impuestos no recuperables, accesorios y plazo de recepción. La mención de una cotización extranjera no acredita costo total entregado. No se recalcularon derechos aduaneros ni se investigaron precios actuales.
2. **Paquetes agregados:** soporte/licencias de red, UPS N+1, baterías, transferencias, repuestos, CA privada y servicios de nube deben tener despiece o justificación de inclusión. No se asignó costo cero por falta de una fila nominal.
3. **Nube:** quedan importes agregados y una «provisión Aurora/DMS por conciliar» de 226,80 USD/mes. Conciliar unidad, región, cantidad, clase, consumo y horario con el diseño antes de sostener que el costo está cerrado. Diferentes tarifas entre regiones no prueban por sí solas una diferencia de tamaño de instancia.
4. **Tiempo vs precio por hora:** el Excel usa 160 para personas equivalentes nominales y T-15 128 HH productivas. E2 lo explica. Debe conservarse esa distinción; dividir por 160 no demuestra que una plaza dedicada solo cueste 80 % si la tarifa ya está definida por hora productiva.

## 6. Orden recomendado de corrección

1. **Fijar línea base técnica y proveedores.** Resolver cobertura de producción anterior a M21, controladores/repuestos, servicios independientes, canales de notificación/pago y diversidad de enlaces.
2. **Rehacer atribución de innovaciones y mantención desde EDT/perfil/mes.** Repetir el control de capacidad; separar inclusión previa de incremento real de costo.
3. **Revisar beneficios sin suma automática.** Alinear población, olas, adopción, beneficiario y valor neto evitado.
4. **Recalcular el modelo y su caja bajo atrasos.** Acordar qué escenario cubre el capital y qué no; mantener netos, IVA, impuestos y financiamiento separados.
5. **Actualizar E2 completo desde el modelo cerrado.** No solo cifras principales: cuadros mensuales/anuales, IVA, gráficos, porcentajes, sensibilidad y texto interpretativo.
6. **Cerrar la entrega.** Corregir encabezados, validar entradas, proteger fórmulas, verificar recálculo nativo, compilar PDF y repetir la comparación contra la versión final.

**Criterio de cierre:** una compra/servicio tiene responsable, cantidad, proveedor o modalidad, costo y calendario trazables; cada HH de innovación pertenece a una partida y cabe en su perfil/mes; cada beneficio tiene beneficiario y regla de no duplicación; E2 reproduce la versión final y el escenario de liquidez que efectivamente se ofrece.

## Anexos de la revisión

- [Conciliación de los 56 meses, con valores E2/Excel y diferencias](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/outputs/coherencia-20261115/conciliacion_mensual_56_meses.csv).
- [Manifiesto de fuentes y commits](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115/manifest.json).
- [Resultados calculados y asignaciones por paquete](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115/metricas.json).
- [Controles independientes](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115/controles.json).

Localizadores principales de la evidencia técnica conservada:

- [T-15, perfiles](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115/fuentes/SD7/formulario-t15/tablas/tab_T15_perfiles_internos.tex).
- [T-15, asignación por partida](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115/fuentes/SD7/formulario-t15/tablas/tab_T15_asignacion_partidas.tex).
- [T-15, método y calendario](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115/fuentes/SD7/formulario-t15/contenido.tex).
- [T-11, inventario](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115/fuentes/SD4/04/formularios/T11/15_anexo_t11.tex).
- [Anexo 4-W, dimensionamiento](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115/fuentes/SD4/04/anexos/fisica/16_anexo_4b_memoria_calculo.tex).
- [T-19, fichas](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115/fuentes/SD13/SD13_v_nueva/T19/contenido.tex).
- [SD13, desarrollo de las innovaciones](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115/fuentes/SD13/SD13_v_nueva/13_innovaciones/contenido.tex).
- [Anexo 8.H, reservas](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115/fuentes/SD8/08_plan_riesgos/anexo-h-reservas.tex).
- [Bases, condiciones E-21/E-24/E-25/E-26](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115/fuentes/SD8/Datos%20externos/Bases/Bases_Administrativas.md).

Se preservaron los archivos originales y los cambios ajenos. El informe y el CSV son resultados de revisión, no versiones corregidas de la oferta.
