# Revisión de coherencia: Excel, Entregable 2 y subdocumentos CORRIGIENDO

**Revisión actualizada al 15 de noviembre de 2026, America/Santiago. Solo diagnóstico. No se aplicaron correcciones.**

Esta revisión vuelve a contrastar el Excel vivo y los commits obtenidos por fetch. No es una copia de la revisión anterior: cambiaron el modelo y SD3, SD7, SD8, SD9 y SD13. Los archivos de revisión anteriores se conservaron.

## Dictamen

**Los tres conjuntos todavía no constituyen una línea base económica coherente para entregar.** La aritmética central del Excel concilia, pero el Entregable 2 está desactualizado y existen diferencias de atribución, calendario y alcance que una simple actualización de cifras no resolvería.

Lo más importante:

1. El costo vigente del Excel es **201.852,72 UF** y el precio neto **237.319,16 UF**, no 200.024,98 y 235.308,64 UF del E2 versionado. Cambian 55 de las 56 filas del flujo. Existe además un PDF alternativo en outputs con 220.875,90/260.429,58 UF, también distinto del Excel.
2. Las **200.783,82 HH de los 37 perfiles sí concilian** con el T-15. Las 1.324,80 HH restantes son servicios especializados, no una omisión automática de personal.
3. Las **5.552 HH de innovaciones coinciden en total**, pero no sus perfiles, costo atribuido ni calendario. Cinco combinaciones perfil/mes exceden el presupuesto disponible.
4. El Excel ya incorpora parte de la nube productiva anterior a M21 y el disco NAS de repuesto. No debe reportarse que siguen totalmente omitidos. Persisten componentes sin cobertura explícita, dos controladores inalámbricos y servicios independientes sin puente económico completo.
5. Los beneficios de innovaciones se suman sin demostrar la exclusión de solapamientos que exige el T-19. INN-05 empieza a generar beneficio en M21 en el Excel, pero SD13 lo sitúa en M33.
6. SD8 incorpora R-036 y propone 837,53 HH de contingencia. El Excel todavía conserva 821,17 HH. La caja positiva del escenario base tampoco resiste cualquier atraso de un hito.

Se identifican **25 observaciones: 12 altas, 12 medias y 1 baja**, agrupadas abajo por causa. «Alta» significa que debe resolverse antes de considerar conciliada la oferta; no es una declaración de inadmisibilidad legal. Se distingue error confirmado de cobertura no demostrada. No se editaron documentos, fórmulas ni precios. Las ramas locales sí se actualizaron por fast-forward conforme a tu solicitud, sin merges entre subdocumentos, commits ni push.

## 1. Fuentes y método

### Excel vigente

[Archivo revisado en Google Drive](https://docs.google.com/spreadsheets/d/18wI3xm9e1alpcn0JKE8CJcjPKg3G4-UP/edit?gid=1717014239#gid=1717014239), título observado: **LafroX_ModeloFinanciero_3_20261113.xlsx**. Es un XLSX editado desde Google, no se trató como una hoja nativa nueva.

Se exportó una copia de lectura con sus **19 hojas**, fórmulas y valores almacenados. SHA-256 de la copia: `7f47c211e3e08754e2c668647fde59aac44855a4d69f777c04267670f9fe1def`.

### Entregable 2

Rama `LafroX-OfertaEconomica-2-Latex`, commit `68595089`, contrastado con las fuentes del checkout, sin cambios previos rastreados. Se revisaron las siete secciones y se extrajo el texto de dos PDF locales de 36 páginas. **No son la misma versión:** el PDF rastreado de la raíz conserva costo/precio 200.024,98/235.308,64 UF; la copia no rastreada de outputs publica 220.875,90/260.429,58 UF, con margen 15,19 % y VAN 28.055,82 UF (página física 7). Ninguno reproduce el Excel de este corte. La rama E2/HEAD es el criterio de la comparación tabular; la copia de outputs se registra como versión alternativa, sin asumir que esté aprobada. No se declara una auditoría visual completa de los PDF.

Entrada: [fuente principal](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/LAFROX_AnalisisFinanciero_2_20261113.tex). Capítulo y secciones: [contenido](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/02_analisis_economico_financiero/contenido.tex).

### Subdocumentos

Se ejecutaron `git fetch --all --prune` y `git pull --ff-only` en E2. En las ramas no abiertas se actualizaron las referencias locales mediante fetch de rama remota a rama local, que rechaza actualizaciones no fast-forward; en el worktree activo de SD4 se ejecutó `pull --ff-only`. Todas las ramas del cuadro quedaron con el mismo SHA local y remoto. Se actualizaron también las ramas financieras y SD8 Revision. No se mezclaron capítulos ni se alteró el checkout actual E2. Para SD8, que no tiene rama denominada CORRIGIENDO, se usó la rama **Revision**, no la antigua. Se revisaron las fuentes vigentes y sus tablas relacionadas. La rama de anexos `63e21571` se consultó solo como complemento; no sustituyó a las versiones CORRIGIENDO por tener un commit más reciente.

| Documento | Referencia revisada | Commit |
|---|---|---|
| SD1 | `origin/LafroX-Subdoc1-LateX-CORRIGIENDO` | `278a4c41` |
| SD2 | `origin/LafroX-Subdoc2-LateX-CORRIGIENDO` | `a72407bc` |
| SD3 | `origin/LafroX-Subdoc3-LateX-CORRIGIENDO` | `c86010b1` |
| SD4 | `origin/LafroX-Subdoc4-LateX-corrigiendo` | `69c9a879` |
| SD5 | `origin/LafroX-Subdoc5-LateX-CORRIGIENDO` | `daec1657` |
| SD6 | `origin/LafroX-Subdoc6-LateX-corrigiendo` | `b18698ec` |
| SD7 | `origin/LafroX-Subdoc7-LateX-CORRIGIENDO` | `0bb2fd07` |
| SD9 | `origin/LafroX-Subdoc9-LateX-corrigiendo` | `4fbaf842` |
| SD13 | `origin/LafroX-Subdoc13-LateX-corrigiendo` | `ef2491c6` |
| SD8 | `origin/Lafrox_Subdocumento_8_Latex_Revision` | `5bb5ebbb` |

Los SD10–12 no se presentan como revisados: no son las versiones CORRIGIENDO que sustentan este cruce del Informe/Entregable 2.

### Alcance de las comprobaciones

- Lectura de las 19 hojas y barrido de errores almacenados, más revisión de referencias y fórmulas relevantes.
- Conciliación independiente de ingresos, costos, VAN, financiamiento, HH, innovaciones y cobertura de operación.
- Cruce de los 37 perfiles y lectura estructurada de las 227 partidas de asignación del T-15.
- Comparación de los 56 meses publicados en E2 con el Excel vigente.
- Contraste de adquisiciones, responsabilidad de compra, servicios, soporte, riesgos, calidad e innovaciones con T-11, T-14, T-15, T-19 y anexos relacionados.
- Comparación directa de los estados de 639 pares reconocidos T-12/T-13, con diez contradicciones; cotejo de seis referencias funcionales con los entregables T-14.
- Uso de las bases contractuales disponibles en el repositorio como criterio de coherencia, especialmente E-21, E-24, E-25 y E-26.

**Límites:** el examen es exhaustivo del cruce económico/documental descrito, no una certificación de todos los 653 requisitos uno por uno ni de cada fórmula por perturbación de entradas. Se inspeccionaron fórmulas, valores exportados y fuentes; la falta de error de celda no demuestra que no existan fórmulas desconectadas (C19). No se recalcularon todas las fórmulas en Excel de escritorio ni se validaron cotizaciones comerciales vigentes, permisos del archivo en Google, implementación real, firmas, homologaciones ni suficiencia legal. El VAN y varios totales se recalcularon independientemente desde los valores mensuales de la exportación. No encontrar una partida identificable no demuestra que un proveedor no la haya incluido en un paquete; demuestra que falta trazabilidad para acreditarlo.

## 2. Diferencias numéricas confirmadas entre E2 y Excel

Valores en UF. Las cifras vigentes siguientes describen **el modelo tal como está**, no el presupuesto final luego de resolver sus brechas de alcance.

| Concepto | E2 publicado | Excel vigente | Diferencia aprox. | Fuente Excel |
|---|---:|---:|---:|---|
| Costo implementación | 88.884,92 | 90.586,68 | 1.701,76 | `RESUMEN!B10` |
| Costo operación | 111.140,06 | 111.266,04 | 125,98 | `RESUMEN!B11` |
| Costo total | 200.024,98 | 201.852,72 | 1.827,74 | `RESUMEN!B12` |
| Precio implementación | 105.093,38 | 106.965,31 | 1.871,93 | `RESUMEN!G10` |
| Precio operación | 130.215,27 | 130.353,85 | 138,58 | `RESUMEN!G11` |
| Precio neto total | 235.308,64 | 237.319,16 | 2.010,52 | `RESUMEN!G12` |
| Margen monetario | 35.283,66 | 35.466,44 | 182,78 | `RESUMEN!L12` |
| VAN antes de impuestos | 24.691,13 | 24.856,03 | 164,90 | `INDICADORES!B5` |
| Cuota mensual operación | 3.617,09 | 3.620,94 | 3,85 | `RESUMEN!G11 / 36` |
| Mínimo de caja financiada | 489,87 | 501,80 | 11,93 | `FLUJO CAJA NETO!M8` |
| Caja final financiada | 35.399,78 | 35.582,55 | 182,77 | `FLUJO CAJA NETO!BH8` |

El margen actual es **14,94 %**, frente a 14,99 % en E2. La TIR mensual actual es **7,20 %**, frente a 7,13 %; la anual es **130,36 %**, frente a 128,44 %. La tasa mensual de descuento permanece en 0,997768607 %. Cambian asimismo el IVA y las conversiones, los importes de hitos, cuadros anuales, sensibilidad, equilibrio y Curva S. No corresponde cambiar solo las cifras de la introducción.

## 3. Hallazgos detallados

| ID | Prioridad | Hallazgo |
|---|---|---|
| C01 | Alta | E2 no reproduce el Excel vigente |
| C02 | Media | E2 mantiene un parque Intune y servicios de implementación de otra versión |
| C03 | Alta | Las innovaciones se valorizan con perfiles distintos a los asignados en T-15 |
| C04 | Alta | El calendario de costo de innovaciones no es el del T-15/T-19 |
| C05 | Alta | Cinco asignaciones de innovaciones exceden el presupuesto perfil/mes |
| C06 | Alta | Se suman beneficios que T-19 ordena no acumular sin conciliación |
| C07 | Media | Beneficios con población no conciliada e INN-05 anticipada doce meses |
| C08 | Alta | La cobertura de nube anterior a M21 está parcialmente incorporada, no completamente demostrada |
| C09 | Alta | Dos controladores inalámbricos y ciertos repuestos no tienen cobertura económica identificable |
| C10 | Alta | Servicios especializados del T-15 sin conciliación económica explícita |
| C11 | Media | La tabla de mantención usa promedios que no reproducen sus paquetes |
| C12 | Media | Proveedores y canales económicos distintos a los de la arquitectura |
| C13 | Media | INN-05 compromete papel y explicación, pero su costo incremental queda en nube |
| C14 | Alta | La línea de respaldo no cubre un atraso de H4 de un mes |
| C15 | Media | El Resumen muestra dos nociones de «total del proyecto» sin puente de alcance |
| C16 | Baja | Encabezados de HH conservan totales manuales de otra versión |
| C17 | Media | La copia XLSX no acredita controles de entrada/protección exigidos por E-21 |
| C18 | Media | SD8 incorpora R-036, pero su contingencia sigue fuera del Excel |
| C19 | Alta | El escenario horario de nube no productiva no llega al flujo y faltan entradas |
| C20 | Alta | La evidencia de innovaciones en M15 no tiene sesiones ni imputación acreditadas |
| C21 | Media | La vista QA aprobada no acredita dotación diaria ni una reserva adicional |
| C22 | Media | Los PDF T-15/T-18 no reflejan las condiciones nuevas de sus fuentes |
| C23 | Alta | Los cobros nominales dependen de entregas/actas aún no acreditadas por la programación |
| C24 | Media | T-13 declara «Cumple» donde T-12 conserva diez cumplimientos parciales |
| C25 | Media | La existencia de un código EDT no demuestra cobertura funcional ni económica |


### C01 · Alta — E2 no reproduce el Excel vigente

**Evidencia.** Introducción y secciones 2.1–2.3, 2.5 y PDF rastreado de la raíz: cifras de la tabla anterior. Además existe una copia distinta en `outputs/LAFROX_AnalisisFinanciero_2_20261113.pdf`, de 36 páginas, cuya página física 7 publica **220.875,90 UF de costo y 260.429,58 UF de precio**, no los importes del Excel ni los del E2 versionado. Su margen es 15,19 % y VAN 28.055,82 UF. Esa copia no rastreada no se considera sustituto aprobado de HEAD; se preserva y se reporta la ambigüedad de versión. El contraste mensual detecta **55 de 56 filas** con alguna diferencia superior a 0,011 UF, descartando diferencias de impresión de una centésima.

**Impacto.** Conviven al menos tres pares costo/precio: el E2 versionado, el PDF alternativo de outputs y el Excel vivo. Sin fijar cuál se entregará, existe riesgo de enviar una evaluación distinta de la sustentada por la planilla. No basta corregir la primera página: las dependencias incluyen flujo mensual, cuadros anuales, IVA, sensibilidad, punto de equilibrio y series gráficas.

**Para considerar conciliado este punto.** Resolver primero las brechas del modelo descritas abajo. Después fijar una única versión, regenerar todas las tablas y gráficos desde sus celdas, compilar y volver a comparar. No hacer sustituciones globales de números sin identificar su origen.

**Localización de fuente:** [02_analisis_economico_financiero/contenido.tex, línea 5](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/02_analisis_economico_financiero/contenido.tex); [secciones/2-2_evaluacion_financiera.tex, línea 39](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/02_analisis_economico_financiero/secciones/2-2_evaluacion_financiera.tex).

### C02 · Media — E2 mantiene un parque Intune y servicios de implementación de otra versión

**Evidencia.** E2 2.4–2.5 usa Intune de 29,05 UF/mes para 382 equipos durante la operación. `COSTOS!AA69:BF69` ya aplica 433 equipos desde M25, según `PARAMETROS!C73:C75`; `PROVEEDORES!F74` muestra 433. El costo real de Intune es 1.169,95 UF, frente a 1.045,84 UF de 36 meses al parque inicial: diferencia 124,11 UF. Este importe ya está dentro del Excel: no se debe sumarlo otra vez.

E2 sigue describiendo la nube de implementación como 32,03 UF/mes desde M2. La fila 63 del modelo ya incluye calendario no productivo y cargos productivos M6–20; no es esa mensualidad fija. La nube operacional base vuelve a ser 368,9158714 UF/mes: no se repite aquí el antiguo hallazgo de ahorro QA ya aplicado, porque la versión actual dejó ese escenario fuera de su fórmula efectiva (C19).

**Consecuencia.** No se puede reconstruir el costo mensual vigente con el catálogo y el texto de E2.

**Localización de fuente:** [secciones/2-4_estrategia_adquisiciones.tex, línea 43](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/02_analisis_economico_financiero/secciones/2-4_estrategia_adquisiciones.tex).

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

**Para considerar conciliado este punto.** Derivar la hoja por código EDT, perfil, HH, mes y costo. Con la asignación actual, las HH sumarían 3.922,85 UF; añadiendo la nube actualmente modelada, el subtotal ilustrativo sería **3.967,10 UF**, antes de resolver consumibles y otras brechas. **No es un ahorro automático de 265,33 UF del proyecto**: las personas ya están presupuestadas globalmente; cambia la atribución del costo.

**Localización de fuente:** [tablas/tab_T15_asignacion_partidas.tex, línea 225](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/fuentes/SD7/formulario-t15/tablas/tab_T15_asignacion_partidas.tex).

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

**Para considerar conciliado este punto.** Llevar las ventanas de las partidas a la valorización. Separar ejecución, devengo presupuestario y pago cuando sean diferentes. Regenerar la figura de egresos de 2.7: su peak M9–10 no es una representación fiel del plan vigente. No confundir además «inversión de una innovación» con «fase contractual M1–20»: ciertas actividades de habilitación siguen después.

**Localización de fuente:** [tablas/tab_T15_asignacion_partidas.tex, línea 125](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/fuentes/SD7/formulario-t15/tablas/tab_T15_asignacion_partidas.tex).

### C05 · Alta — Cinco asignaciones de innovaciones exceden el presupuesto perfil/mes

**Evidencia.** Se sumaron todas las HH de innovaciones por perfil y mes y se compararon con `HH POR ROL Y MES!C8:BF44`, respetando las ventanas inclusivas de INNOVACIONES.

| Perfil | Mes | HH solo innovaciones | HH disponibles del rol | Exceso |
|---|---:|---:|---:|---:|
| Analista QA Senior | 10 | 480,00 | 471,28 | 8,72 |
| Líder de Calidad y Pruebas | 39 | 43,50 | 7,56 | 35,94 |
| Analista QA Senior | 53 | 25,40 | 24,20 | 1,20 |
| Analista QA Senior | 55 | 24,10 | 22,98 | 1,12 |
| Coordinador de Implantación | 18 | 37,77 | 21,22 | 16,55 |

En estos casos la innovación supera incluso la totalidad de horas disponibles, antes de reservar otras tareas. Por ello, la afirmación de E2 2.7 de que cada hora cae en un mes en que el perfil trabaja no demuestra que esas horas quepan en el presupuesto del perfil/mes. El control cuantitativo encuentra sobreasignación, aunque exista actividad del perfil.

**Para considerar conciliado este punto.** Corregir C03–C04 desde las partidas originales y volver a ejecutar este control. No basta comprobar que el perfil tenga alguna hora ese mes ni que el total anual alcance. No sumar horas nuevas para tapar una redistribución incorrecta.

**Localización de fuente:** [secciones/2-7_valorizacion_innovaciones.tex, línea 45](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/02_analisis_economico_financiero/secciones/2-7_valorizacion_innovaciones.tex).

### C06 · Alta — Se suman beneficios que T-19 ordena no acumular sin conciliación

**Evidencia.** `INNOVACIONES!K84=SUM(K79:K83)` produce **53.878,83 UF**, repetidas como beneficio total del CLIENTE en E2. T-19/SD13 indican expresamente que INN-01 y 03 no se suman entre sí ni a la meta de merma; INN-04 tampoco se suma a 01, 03 o 05. Además, el tiempo de decisión del almacenero es beneficio de un tercero, no ingreso ni ahorro de caja automático de Puelche.

**Impacto.** El total mezcla escenarios que no acreditan aditividad y beneficiarios distintos. El Excel sí hace la suma aritmética, pero no demuestra que sea un beneficio económico agregado válido.

**Para considerar conciliado este punto.** Mantener beneficios por innovación y beneficiario, sin total aditivo, hasta construir una matriz de exclusión y atribución por evento/lote/entrega. Separar el beneficio económico incremental del cliente del beneficio del almacenero. Conservar fuera del flujo de LafroX estos ahorros, como ya hace el modelo.

**Localización de fuente:** [13_anexos/contenido.tex, línea 125](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/fuentes/SD13/SD13_v_nueva/13_anexos/contenido.tex).

### C07 · Media — Beneficios con población no conciliada e INN-05 anticipada doce meses

**Evidencia.** B-01 aplica la reducción a todas las 2,4 millones de unidades mensuales; el servicio posentrega y su piloto están definidos para locales/rutas elegibles del canal tradicional. B-03 convierte proporción de SKU de frío en proporción de recepciones/lotes, aunque esa equivalencia no está demostrada. B-04 usa 31.000 pedidos, mientras T-19 habla de entregas comparables. B-05 usa todas las visitas estimadas al canal tradicional desde M21, pero el despliegue se completa por olas hasta M26–27 y depende de aceptación. Además, el Anexo 13.B, fila de INN-05, fija el beneficio desde **M33**, mientras `INNOVACIONES!H83=21` y E2 2.7 usan M21. Aun manteniendo la misma tasa hipotética de 101,2957746 UF/mes, M33–56 serían 24 meses y **2.431,10 UF**, no 36 meses y 3.646,65 UF: se anticipan **1.215,55 UF**. Este ajuste de calendario no valida por sí solo la población, causalidad ni valoración del beneficio.

SD13 también exige descontar canjes y descuentos en el beneficio de INN-01. E2 reconoce que valora a precio de venta y usa máximos, lo que es una cautela útil, pero no reemplaza ese ajuste ni una base elegible. Los cocientes entre SKU, lotes, visitas y canales deben figurar como supuestos de extrapolación, no como mediciones.

**Para considerar conciliado este punto.** Usar volumen elegible × cobertura por ola × adopción × cambio causal validado × valor neto evitado. Mantener los supuestos no medidos como escenarios, sin presentarlos como ahorro realizado ni utilizar la cifra agregada para justificar rentabilidad del proveedor. Estimar por separado el costo de intervención/canje y el margen o pérdida realmente evitada.

**Localización de fuente:** [13_anexos/contenido.tex, línea 40](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/fuentes/SD13/SD13_v_nueva/13_anexos/contenido.tex).

### C08 · Alta — La cobertura de nube anterior a M21 está parcialmente incorporada, no completamente demostrada

**Cambio verificado.** El Excel añadió `ADQUISICIONES IMPLEMENTACIÓN!O49:S55`: Aurora Producción, Aurora Recuperación y Fargate Recuperación desde M6; DMS desde M13. La suma S55 es **1.473,99 UF** y está enlazada en `COSTOS!H63:V63`. Es incorrecto afirmar que toda esa nube sigue ausente.

**Brecha vigente.** La nueva tabla no individualiza Fargate de Producción permanente. El bloque Fargate de implementación `O8:Z45` sigue bajo el título de ambientes no productivos, con 19 tareas en horario y cero fuera de él. El único Fargate explícito del añadido es Recuperación y usa `ADQUISICIONES OPERACION!G82`, el núcleo de DR. Tampoco se demuestra el despiece productivo de red, balanceo, seguridad, almacenamiento, tráfico y soporte durante M6–20 frente a los importes de pruebas anteriores. SD4 habilita cinco ambientes en H3/M6; SD9 exige datos y pedidos reales desde M13 y M19, además de E1 en producción M16–20.

**Consecuencia.** Hay cobertura nueva real, pero falta probar qué recursos del diseño operan 24/7, cuáles están dentro de cada agregado y desde cuándo. No se cuantifica un faltante neto ni se propone duplicar la factura completa de operación.

**Localización de fuente:** [09_plan_calidad/contenido.tex, línea 156](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/fuentes/SD9/SD9_v_nueva/09_plan_calidad/contenido.tex).

### C09 · Alta — Dos controladores inalámbricos y ciertos repuestos no tienen cobertura económica identificable

**Evidencia.** T-11 y Anexo 4-W.13 ofertan **dos Cisco CW9800L**, fuentes CW9800L-RPS y montaje. El Excel individualiza switches y 72 AP, pero no los controladores ni el paquete que los incluya, en `ADQUISICIONES IMPLEMENTACIÓN!A15:I23` o PROVEEDORES. Los switches C9300/C9200 no son esos controladores. Los repuestos por componente de Concepción —SSD y fuente— tampoco tienen conciliación explícita con las cantidades agregadas.

**Cambio verificado.** El disco NAS ya no es una omisión: `ADQUISICIONES IMPLEMENTACIÓN!F37=5` y `PROVEEDORES!F31=5`, con descripción de cuatro instalados y un repuesto. No se mantiene el hallazgo anterior de cuatro discos solamente.

**Consecuencia.** La oferta técnica compromete equipos concretos sin una partida o cotización enlazada que acredite su costo. Una compra agregada de UPS N+1 o gabinetes puede contener varios componentes, pero su cantidad «1» por sí sola ni prueba ni refuta esa cobertura.

**Localización de fuente:** [fisica/16_anexo_4b_memoria_calculo.tex, línea 522](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/fuentes/SD4/04/anexos/fisica/16_anexo_4b_memoria_calculo.tex).

### C10 · Alta — Servicios especializados del T-15 sin conciliación económica explícita

**Evidencia.** T-15 separa **1.324,80 HH** del código 00: 864 HH de implementación y 460,80 de operación. Incluyen 320+160 HH de pruebas ofensivas independientes, 384 HH de instalaciones especializadas y 230,40+230,40 HH de ciberseguridad y revisión eléctrica en operación.

Las instalaciones podrían estar incluidas en compras «con montaje»/obras; por tanto no deben sumarse otra vez automáticamente. Pero el modelo no aporta un puente código 00 → proveedor → contrato/partida → costo/mes. No se identifica una partida propia de pruebas independientes en PROVEEDORES. E2 2.4 dice que LafroX hace las pruebas de aceptación, sin distinguir suficientemente las pruebas que deben ejecutar terceros.

**Para considerar conciliado este punto.** Preparar ese puente. Registrar lo ya incluido en equipos/obras con evidencia; valorizar lo no cubierto con su modalidad contractual. No convertir las 1.324,80 HH en personal de nómina ni tratarlas a una tarifa genérica. Aclarar qué aceptación coordina LafroX y qué prueba ejecuta un tercero independiente.

**Localización de fuente:** [tablas/tab_T15_asignacion_partidas.tex, línea 115](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/fuentes/SD7/formulario-t15/tablas/tab_T15_asignacion_partidas.tex).

### C11 · Media — La tabla de mantención usa promedios que no reproducen sus paquetes

**Evidencia.** E2 2.6 aplica 0,68 UF/HH a Desarrollo y 0,96 a SRE/DevOps, obtenidos de grupos globales, y atribuye 2.576 HH preventivas a estos últimos. El T-15 asigna mezclas diferentes en cada partida y **230,40 HH de 8.2.6 a un tercero**.

Ejemplos de conciliación con los costos horarios actuales:

- 8.2.1, correctivo + evolutivo: **3.134,59 UF** por su mezcla de perfiles; las dos líneas de E2 suman 3.128,84 UF. El reparto de 50/50 entre correctivo y evolutivo debe declararse como supuesto del desglose si no está fijado por perfil.
- 8.2.4, deuda técnica: **1.558,66 UF**, frente a 1.564,42 UF.
- 8.2.5 + 8.2.7: **1.080,00 UF**, frente a 1.105,18 UF.
- Preventiva 8.1.3 + 8.1.6 + 8.2.3 + parte interna de 8.2.6: **2.183,88 UF de personal interno, más el servicio externo**, cuyo precio no se demuestra. No es equivalente a afirmar un total conciliado de 2.471,31 UF.

**Para considerar conciliado este punto.** Sustituir promedios por suma de HH × costo de los perfiles de cada paquete y separar contratistas. Esto corrige atribuciones dentro de costos ya presupuestados; no corresponde añadir todos los subtotales al costo total otra vez.

**Localización de fuente:** [secciones/2-6_mantencion_soporte.tex, línea 35](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/02_analisis_economico_financiero/secciones/2-6_mantencion_soporte.tex).

### C12 · Media — Proveedores y canales económicos distintos a los de la arquitectura

**Evidencia.** SD4/T-11 y catálogo INT-11 declaran SES, SNS y AWS End User Messaging Social, con 2.800/5.200 avisos diarios y costo unitario por canal remitido a la Oferta Económica. PROVEEDORES/servicios externos y E2 mencionan Twilio y Mercado Pago; la fórmula de servicios de operación utiliza 2.000 mensajes y una comisión de 3,19 % sobre 20 millones CLP sin un puente hacia la mezcla y volúmenes del diseño. La arquitectura identifica Transbank entre sus dependencias de pago.

Para la fibra, T-11 prioriza Telsur y reserva otro operador fijo distinto de Entel si no hay factibilidad; E2 y PROVEEDORES presupuestan Entel mientras parte del respaldo LTE también es Entel.

**Para considerar conciliado este punto.** Una única matriz servicio/proveedor/canal/volumen/unidad/precio/pagador. Explicar una alternativa aprobada o usar el proveedor del diseño. No asumir que cotizar otro proveedor satisface la diversidad de operadores ni sumar ambos servicios sin descartar duplicación. Separar comisiones de cobro de costos de integración y precisar quién las paga.

**Localización de fuente:** [secciones/2-4_estrategia_adquisiciones.tex, línea 40](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/02_analisis_economico_financiero/secciones/2-4_estrategia_adquisiciones.tex).

### C13 · Media — INN-05 compromete papel y explicación, pero su costo incremental queda en nube

**Evidencia.** T-19 campo 11 incluye papel térmico de copias pedidas y minutos de explicación en la visita. Anexo 4-W distingue el costo por copia de la generación mensual. E2/INNOVACIONES muestran solo **1,16 UF** de costo operacional no-HH de INN-05, correspondiente a nube, sin cantidad/precio de copias ni atribución de ese tiempo. Que el hardware del CLIENTE incluya un rollo inicial no cubre 36 meses de consumo.

**Para considerar conciliado este punto.** Definir pagador, tasa de solicitud de copias, papel/merma por copia y tiempo incremental por visita. Si los absorbe el CLIENTE, mostrarlos como costo de adopción del cliente, no ocultarlos ni cargarlos sin más a LafroX. Si las horas ya están incluidas, referenciar su paquete para no duplicarlas.

**Localización de fuente:** [T19/contenido.tex, línea 141](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/fuentes/SD13/SD13_v_nueva/T19/contenido.tex).

### C14 · Alta — La línea de respaldo no cubre un atraso de H4 de un mes

**Evidencia.** E2 2.3 presenta una línea de 1.250 UF como respaldo ante atrasos de un hito. En el Excel actual la caja financiada de M10 es **8.471,96 UF** (`FLUJO CAJA NETO!N8`) y H4 vale **10.696,53 UF** (`N30`).

Prueba independiente sin modificar el libro: desplazar solo el cobro de H4 de M10 a M11, dejando iguales los demás flujos. Caja de M10: `8.471,96 − 10.696,53 = −2.224,57 UF`. Con toda la línea de 1.250 UF: **−974,57 UF**, antes de los intereses de esa línea.

**Consecuencia.** La caja positiva del escenario base es verdadera, pero no acredita cobertura de cualquier atraso. «Ingresos ±20 %» cambia importes, no calendario. Una reserva de HH no equivale a liquidez bancaria. Este cálculo no es una predicción de atraso: es una refutación concreta de la cobertura genérica que afirma E2.

**Localización de fuente:** [secciones/2-3_curva_s.tex, línea 34](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/02_analisis_economico_financiero/secciones/2-3_curva_s.tex).

### C15 · Media — El Resumen muestra dos nociones de «total del proyecto» sin puente de alcance

**Evidencia.** `RESUMEN!B35:B37` presenta 47.768,44 HH, costo 36.575,17 UF y venta 44.168,35 UF según puntos de caso de uso. La línea base T-15 es 202.108,62 HH y el total financiero vigente 201.852,72/237.319,16 UF. El encabezado «Viabilidad y HH» ayuda a reconocer otra estimación, pero no establece qué fases, servicios, paquetes o esfuerzo cubre y excluye.

**Para considerar conciliado este punto.** Rotularlo como estimación alternativa de alcance específico, identificar el perímetro y conciliarlo con la EDT. No comparar esfuerzo de programación/ampliado por UCP con 56 meses de cobertura y soporte como si fueran el mismo total ni utilizar ambas cifras como precio de oferta.

### C16 · Baja — Encabezados de HH conservan totales manuales de otra versión

**Evidencia.** `HH POR ROL Y MES!B9=5.354`, frente a 4.737,83 HH de ese perfil en Sueldos; `B31`, `B32` y `B33` tampoco reproducen el total del perfil anunciado por el encabezado. En particular, Instructor muestra 496 frente a 512 HH mensuales sin capacitación y 4.008 HH incluyendo su capacitación.

**Para considerar conciliado este punto.** Elegir y rotular «total servicio sin capacitación» o «total del perfil incluida capacitación» y enlazar su fórmula. Hay 195.535,82 HH en la matriz mensual más **5.248 HH** separadas de capacitación: suman exactamente 200.783,82. Esa separación es correcta; los encabezados manuales no lo son.

### C17 · Media — La copia XLSX no acredita controles de entrada/protección exigidos por E-21

**Evidencia.** Ninguna de las 19 hojas de la exportación tiene protección de hoja activa. PARAMETROS, HH POR ROL Y MES, INNOVACIONES, PROVEEDORES y las hojas de adquisiciones no contienen validaciones de entrada. Existen algunas validaciones en otras hojas: no se afirma que el archivo carezca totalmente de ellas. E-21 exige validación de entradas y protección de fórmulas críticas.

**Para considerar conciliado este punto.** Aplicar validaciones por dominio y proteger cálculos dejando entradas habilitadas. Verificarlo en el XLSX que se vaya a entregar. No confundir celdas marcadas como bloqueadas por defecto con protección activa. Los permisos/protecciones de Google no se auditaron y podrían no trasladarse al XLSX.

### C18 · Media — SD8 incorpora R-036, pero su contingencia sigue fuera del Excel

**Evidencia.** SD8 actual, Anexo 8.H, trabaja con **36 riesgos**, exposición inicial de **1.199,52 HH**, contingencia p1H0 de **837,53 HH**, prevención 180 y gestión 160. R-036 agrega 16,40 HH: 9,84 de ARQ y 6,56 de CAL, uniformes en M1–56, sin trabajo preventivo adicional.

`COSTOS!C111:C117` sigue sumando **821,17 HH**. Frente al valor publicado por SD8 faltan **16,36 HH de conciliación**, no solo las 0,04 HH de redondeo detectadas antes. El componente R-036, valorado con los costos representativos vigentes ARQ 1,10 y CAL 0,60 UF/HH, equivale a **14,76 UF**, antes de resolver las centésimas de importación y su aprobación. No es un costo autorizado automáticamente ni corresponde sumarlo a ciegas.

La protección S7 de 3.072 HH ya integra las 202.108,62 HH. SD8 exige no duplicarla y advierte que la reserva propuesta no prueba suficiencia ni financiamiento. E2 2.2 todavía presenta reservas como cobertura de atrasos y mayor esfuerzo sin el puente causal y de caja (véase C14).

**Consecuencia.** El registro de riesgos, su distribución y su presupuesto no están en la misma versión.

**Localización de fuente:** [08_plan_riesgos/anexo-h-reservas.tex, línea 22](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/fuentes/SD8/08_plan_riesgos/anexo-h-reservas.tex).

### C19 · Alta — El escenario horario de nube no productiva no llega al flujo y faltan entradas

**Evidencia de fórmula.** `ADQUISICIONES OPERACION!O8:AA43` calcula 36 meses del escenario QA Fargate: por ejemplo X8=22,3872 USD frente a AA8=61,904 USD ya incluidos. Sin embargo, `COSTOS!W63:BF63` solo busca ajustes en las filas **44:151**, no en 8:43.

El nuevo bloque O44:AA151 contiene Desarrollo Fargate, Preproducción Fargate y Preproducción Aurora para M21–56, pero **las 108 filas carecen de las seis entradas Q:U y AA**. La fórmula X devuelve vacío al no alcanzar `COUNT(...)=6`. La fórmula de COSTOS excluye esas filas con `ISNUMBER` y toma ajuste cero. Por eso el costo efectivo permanece en **368,9158714 UF/mes**, total **13.280,97 UF**, aunque la hoja muestra un escenario horario calculado.

O154:U160 muestra además un comparador 24/7 frente a 12 h con ahorro directo de **2.053,02 UF** bajo sus propios supuestos. Ese comparador no es una sustitución efectiva de recursos en el flujo. El rótulo de escenario por sí solo no lo convierte en ahorro presupuestado.

**Consecuencia.** El libro puede aparentar una evaluación FinOps completa mientras el flujo ignora el QA calculado y convierte datos faltantes en ajuste cero. No se afirma que el ahorro deba descontarse entero ni que el costo base sea cero: faltan aprobar configuración, costo previo incluido y enlace de cada ambiente.

### C20 · Alta — La evidencia de innovaciones en M15 no tiene sesiones ni imputación acreditadas

**Evidencia.** SD13 Anexo 13.B.1 y T-15 reconocen que 3.10.1.4, 3.10.2.4 y 3.10.3.4 distribuyen preliminarmente 240 HH por paquete entre M11–15: en M15 son 48 HH por paquete, **96 HH de Datos y 48 HH de Calidad**. Pero la programación diaria termina los tres el **20-03-2028**. El **28-04-2028** es fin tardío CPM, no fecha de ejecución programada. Los marcadores auxiliares no tienen carga.

El mismo anexo dice que la hoja Innovaciones no permite identificar la imputación por paquete/perfil/mes y exige registro de sesiones, disponibilidad, predecesora y entrega. Las cinco sobreasignaciones de C05 son en otros meses.

**Consecuencia.** La igualdad global de HH no demuestra que el piloto real, las veinte parejas de reproducción y los sesenta lotes por familia estén programados con personal disponible en abril. **No se reportan 144 HH faltantes** ni se sugiere sumarlas: es una brecha de programación y trazabilidad ya reconocida por los documentos vigentes.

**Localización de fuente:** [13_anexos/contenido.tex, línea 61](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/fuentes/SD13/SD13_v_nueva/13_anexos/contenido.tex).

### C21 · Media — La vista QA aprobada no acredita dotación diaria ni una reserva adicional

**Evidencia.** SD7 T-15 §6.1 y SD9 Anexo 9.E.1 publican **83 ventanas QA** de hasta 14 días en 15 paquetes. T-15 declara aprobación de esa vista como complemento, condicionada a no alterar el modelo financiero, y dice expresamente que no acredita personal para las sesiones. T-13 §8.3 exige 66,5 HH manuales por regresión completa: al menos 11 evaluadores-día con 6,4 HH netas, antes de coordinación e incidencias. El techo de 16 evaluadores no es asignación nominal.

El propio SD9 distingue presupuesto de paquetes, automatización y cuadrante de personas. Las 12.016 HH de calidad siguen siendo parte de la línea base, no un costo nuevo.

**Consecuencia.** No puede inferirse que 83 ventanas aprobadas demuestren todas las regresiones financiadas y niveladas, ni multiplicar sin más 83×66,5 y declararlo déficit: primero se debe fijar alcance de cada sesión y horas ya incluidas. El punto pendiente es el puente ventana→sesión→perfil/día→HH existentes.

**Localización de fuente:** [formulario-t15/contenido.tex, línea 342](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/fuentes/SD7/formulario-t15/contenido.tex); [T13/contenido.tex, línea 370](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/fuentes/SD9/SD9_v_nueva/T13/contenido.tex).

### C22 · Media — Los PDF T-15/T-18 no reflejan las condiciones nuevas de sus fuentes

**Evidencia.** La rama SD7 avanzó a `0bb2fd07` cambiando contenido fuente de T-15 y T-18, sin actualizar sus PDF versionados. El T-15 PDF, página física **72**, conserva el cierre de H7/H12 con una sola acta y la redistribución de HH M21–22 ante atraso; la fuente vigente lo presenta como escenario nominal sujeto a confirmación escrita y no autoriza redistribuir HH sin cambio aprobado. En la página **106** el PDF afirma iteraciones de hasta 14 días, mientras la fuente reconoce seis ventanas originales mayores y las desdobla en la vista de 83 ventanas.

El T-18 PDF, páginas físicas **16 y 18**, conserva los pasos a producción como fechas afirmativas (17-05 y 18-10 de 2028); su fuente vigente agrega firma previa y confirmación escrita de una ventana fuera del despacho.

**Consecuencia.** Leer la rama actual no garantiza leer el mismo compromiso en el PDF entregable. No se recompiló ni corrigió ningún PDF durante esta revisión. La numeración anterior es física del archivo, no folio impreso.

**Localización de fuente:** [formulario-t18/contenido.tex, línea 132](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/fuentes/SD7/formulario-t18/contenido.tex).

### C23 · Alta — Los cobros nominales dependen de entregas/actas aún no acreditadas por la programación

**Evidencia.** SD13 Anexo 13.B.1 y T-15 distinguen entregas nominales y finalización diaria:

| Hito | Entrega nominal | Fin programado del paquete de control |
|---|---|---|
| H4 | 20-10-2027 | 3.8.1: 22-10-2027 |
| H5 | 24-11-2027 | 3.8.7: 01-12-2027 |
| H10 | 27-06-2028 | 3.9.6: 28-06-2028 |

SD7 admite entregas incrementales H4, pero exige identificar qué informe y evidencia hacen admisible el incremento y qué trabajo queda. SD13 advierte que un fin temprano CPM no prueba entrega completa ni firma, y que H5/H10 requieren acreditar expediente y pruebas precedentes. El procedimiento integrado H7/H12 está sujeto a confirmación escrita; no constituye por sí mismo cobro asegurado.

**Consecuencia.** Excel/E2 modelan el calendario nominal de ingresos, mientras la planificación conserva condiciones pendientes que pueden cambiar el cobro efectivo. No se afirma que todo hito vaya a atrasarse ni que la diferencia de dos días de H4 por sí sola cambie de mes: el hallazgo es la ausencia de evidencia conciliada de aceptación y escenario temporal. El impacto de un mes de atraso de H4 está cuantificado en C14.

**Localización de fuente:** [13_anexos/contenido.tex, línea 74](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/fuentes/SD13/SD13_v_nueva/13_anexos/contenido.tex).


### C24 · Media — T-13 declara «Cumple» donde T-12 vigente conserva diez cumplimientos parciales

**Evidencia.** Se compararon los estados de las 639 filas comunes reconocidas directamente por el cotejo de texto entre T-12 vigente y `SD9_v_nueva/T13/matriz_requisitos.tex`. Se encontraron diez diferencias de estado, todas de «Cumple parcialmente» en T-12 a «Cumple» en T-13:

`RF-18.03`, `RNF-20.06`, `RNF-23.02`, `RT-03.18`, `RT-07.04`, `RT-08.12`, `RT-08.14`, `RT-11.04`, `RT-16.18` y `RT-16.23`.

Ejemplo confirmado: T-12 línea 596 reconoce que RT-16.18 no acredita aún el mecanismo de sello de tiempo y verificación después del vencimiento del certificado. T-13 línea 636 lo trata como «Cumple», prevé /P01 y describe la marca del registro como sello de tiempo. No se está evaluando aquí su suficiencia jurídica: se verifica que los documentos afirman estados diferentes del mismo requisito.

La comparación reconoce 639 pares; no interpreta los identificadores no reconocidos por el parser como requisitos perdidos. Los alias/absorbidos se tratan aparte y no se suman como requisitos nuevos. El resumen del T-12 declara 599 cumplimientos, 32 parciales y 22 no cumplimientos, pero no se presenta ese resumen como un recuento independiente completo de este script.

**Consecuencia.** El alcance efectivamente ofertado y sus brechas no son iguales en el catálogo y la matriz de pruebas. Un presupuesto basado en que esas funciones están cerradas no queda acreditado por un estado de prueba desactualizado. No se valoriza ninguna corrección técnica ni se declara que las pruebas se hayan ejecutado.

**Localización de fuente:** [T-12 vigente, líneas 18 y 596](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/fuentes/SD3/LAFROX-Formulario-T-12.tex); [T-13, matriz, línea 636](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/fuentes/SD9/SD9_v_nueva/T13/matriz_requisitos.tex); [cotejo de estados reproducible](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/cotejo_estados_T12_T13.json).

### C25 · Media — La existencia de un código EDT no demuestra cobertura funcional ni económica

**Evidencia.** El T-12 usa 3.3.5 para RF-17.02 (parametrización de reglas), RF-17.08 (gestión documental), RT-16.14 (motor de reglas) y RT-16.29 (exportación asíncrona). Usa 3.6.4 para RF-17.09 y RT-16.19 (generación de documentos). En el T-14, `tab_T14_20.tex`, 3.3.5 entrega un **registro auditable de stock, lotes y cobros**; en `tab_T14_23.tex`, 3.6.4 entrega **integración del servicio de avisos INT-11**. Varias filas de T-12 ya dicen «alcance por precisar en T-14».

**Consecuencia.** Hay referencia sintáctica a paquetes existentes, pero el entregable y aceptación de esos paquetes no explicitan toda la funcionalidad que se les atribuye. Por eso no queda probado el puente requisito→entregable EDT→HH/perfil→costo para esas funciones. No se concluye que estén necesariamente sin implementar o sin presupuesto: falta precisar qué trabajo existente las contiene y con qué criterio de aceptación. El total de HH conciliado no sustituye esta evidencia.

**Localización de fuente:** [T-12, líneas 204, 210–211 y 592–607](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/fuentes/SD3/LAFROX-Formulario-T-12.tex); [T-14, 3.3.5, línea 8](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/fuentes/SD7/formulario-t14/tablas/tab_T14_20.tex); [T-14, 3.6.4, línea 7](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/fuentes/SD7/formulario-t14/tablas/tab_T14_23.tex).

## 4. Comprobaciones que sí pasan y cambios ya incorporados

| Control independiente | Resultado | Estado |
|---|---:|---|
| Ingresos contractuales vs Resumen | 237.319,16 | Concilia |
| Costos del proyecto vs Resumen | 201.852,72 | Concilia |
| VAN independiente | 24.856,03 | Concilia |
| HH perfiles T15 vs Excel | 200.783,82 | Concilia |
| HH mensuales + capacitacion vs Sueldos | 200.783,82 | Concilia |
| Perfiles + servicios especializados vs linea base | 202.108,62 | Concilia |
| HH innovaciones vs paquetes T15 | 5.552,00 | Concilia |
| Total intereses contrato | 3.683,89 | Concilia |
| Saldo final financiado | 35.582,55 | Concilia |
| Porcentajes hitos | 1,00 | Concilia |
| Horas SOC operacion por calendario | 26.280,00 | Concilia |
| Horas Mesa N1 operacion | 38.246,00 | Concilia |
| Horas NOC operacion | 21.748,20 | Concilia |
| Costo innovaciones nube una vez | 44,26 | Concilia |

**Cambios ya incorporados que no deben reportarse como intactos:** nube pre-M21 por 1.473,99 UF; quinto disco NAS; Intune 433 desde M25; SD13 distingue fin programado/CPM y condiciones de evidencia; SD7/SD9 distinguen aprobación de vista QA de dotación. Los cambios documentales no cierran automáticamente sus puentes económicos.

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
| SD3 / T-12 | Alcance y paquetes hacia estimación/arquitectura | Diez estados no conciliados con T-13 y seis referencias EDT sin alcance explícito; no se reestimó cada requisito |
| SD4 / T-11 / 4-W | Equipos, servicios, ambientes, cobertura y dimensionamiento | Brechas C08–C09 y C12; parque/crecimiento Intune reconocido en Excel |
| SD5 | Datos, migración y separación de responsabilidades | No se identificó una discrepancia monetaria independiente adicional; no se certifica costo detallado de cada política de retención |
| SD6 / anexos / T-9 | Hacer/comprar, calendario y terceros | Secuencia de sala M2 compra/M3 instalación/M4 recepción coincide con E2; separar terceros de pruebas y montaje |
| SD7 / T-14 / T-15 / T-18 | 227 partidas, 37 perfiles, ventanas, soporte y HH | Totales conciliados; atribución y temporalidad no conciliadas; PDF T-15/T-18 desactualizados |
| SD8 / T-16 / 8.H | Reservas, no duplicación, perfiles y autorización | R-036 y contingencia no importados; no prometer cobertura automática |
| SD9 / T-13 / T-17 | Calidad, puertas y producción real en marcha blanca | Estados T-13 desactualizados respecto de T-12; dotación QA pendiente; calidad no se suma dos veces |
| SD13 / T-19 | Cinco innovaciones, indicadores, madurez, calendario y costos | Diferencias de atribución, calendario, aditividad y adopción; evidencia M15 pendiente |

### Confirmaciones necesarias para cerrar, no errores cuantificados adicionales

1. **Importaciones:** precio puesto en sitio, flete, seguro, impuestos no recuperables, accesorios y plazo de recepción. La mención de una cotización extranjera no acredita costo total entregado. No se recalcularon derechos aduaneros ni se investigaron precios actuales.
2. **Paquetes agregados:** soporte/licencias de red, UPS N+1, baterías, transferencias, repuestos, CA privada y servicios de nube deben tener despiece o justificación de inclusión. No se asignó costo cero por falta de una fila nominal.
3. **Nube:** quedan importes agregados y una «provisión Aurora/DMS por conciliar» de 226,80 USD/mes. Conciliar unidad, región, cantidad, clase, consumo y horario con el diseño antes de sostener que el costo está cerrado. Diferentes tarifas entre regiones no prueban por sí solas una diferencia de tamaño de instancia.
4. **Tiempo vs precio por hora:** el Excel usa 160 para personas equivalentes nominales y T-15 128 HH productivas. E2 lo explica. Debe conservarse esa distinción; dividir por 160 no demuestra que una plaza dedicada solo cueste 80 % si la tarifa ya está definida por hora productiva.

## 6. Dependencias para una futura conciliación — no aplicadas

1. **Fijar línea base técnica y proveedores.** Resolver cobertura de producción anterior a M21, controladores/repuestos, servicios independientes, canales de notificación/pago y diversidad de enlaces.
2. **Rehacer atribución de innovaciones y mantención desde EDT/perfil/mes.** Repetir el control de capacidad; separar inclusión previa de incremento real de costo.
3. **Revisar beneficios sin suma automática.** Alinear población, olas, adopción, beneficiario y valor neto evitado.
4. **Recalcular el modelo y su caja bajo atrasos.** Acordar qué escenario cubre el capital y qué no; mantener netos, IVA, impuestos y financiamiento separados.
5. **Actualizar E2 completo desde el modelo cerrado.** No solo cifras principales: cuadros mensuales/anuales, IVA, gráficos, porcentajes, sensibilidad y texto interpretativo.
6. **Cerrar la entrega.** Corregir encabezados, validar entradas, proteger fórmulas, verificar recálculo nativo, compilar PDF y repetir la comparación contra la versión final.

**Criterio de cierre:** una compra/servicio tiene responsable, cantidad, proveedor o modalidad, costo y calendario trazables; cada HH de innovación pertenece a una partida y cabe en su perfil/mes; cada beneficio tiene beneficiario y regla de no duplicación; E2 reproduce la versión final y el escenario de liquidez que efectivamente se ofrece.

## Anexos de la revisión

- [Conciliación de los 56 meses, con valores E2/Excel y diferencias](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/outputs/coherencia-20261115-actualizada/conciliacion_mensual_56_meses.csv).
- [Manifiesto de fuentes y commits](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/manifest.json).
- [Resultados calculados y asignaciones por paquete](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/metricas.json).
- [Controles independientes](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/controles.json).

Localizadores principales de la evidencia técnica conservada:

- [T-15, perfiles](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/fuentes/SD7/formulario-t15/tablas/tab_T15_perfiles_internos.tex).
- [T-15, asignación por partida](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/fuentes/SD7/formulario-t15/tablas/tab_T15_asignacion_partidas.tex).
- [T-15, método y calendario](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/fuentes/SD7/formulario-t15/contenido.tex).
- [T-11, inventario](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/fuentes/SD4/04/formularios/T11/15_anexo_t11.tex).
- [Anexo 4-W, dimensionamiento](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/fuentes/SD4/04/anexos/fisica/16_anexo_4b_memoria_calculo.tex).
- [T-19, fichas](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/fuentes/SD13/SD13_v_nueva/T19/contenido.tex).
- [SD13, desarrollo de las innovaciones](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/fuentes/SD13/SD13_v_nueva/13_innovaciones/contenido.tex).
- [Anexo 8.H, reservas](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/fuentes/SD8/08_plan_riesgos/anexo-h-reservas.tex).
- [Bases, condiciones E-21/E-24/E-25/E-26](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-actualizada/fuentes/SD8/Datos%20externos/Bases/Bases_Administrativas.md).

Se preservaron los archivos originales y los cambios ajenos. El informe y el CSV son resultados de revisión, no versiones corregidas de la oferta.

## Key Learnings:

1. Conciliar las HH totales no acredita su asignación por perfil, mes, paquete y sesión.
2. La revisión debe fijar rama, commit, hash del Excel y PDF concreto: las copias locales pueden representar líneas base diferentes.

## Registro de integridad

El checkout E2 continúa en `68595089`, sin diferencias rastreadas frente a HEAD antes y después. Las correcciones aquí descritas **no se aplicaron**. Se crearon solo el informe, CSV y evidencias de auditoría en carpetas nuevas.

**Criterio de clasificación:** error confirmado = contradicción verificable o cálculo reproducido; cobertura no demostrada = no se identificó una partida/puente suficiente, sin asumir costo cero; condición pendiente = la propia documentación exige autorización, asignación o evidencia no acreditada. No se declara inadmisibilidad legal ni suficiencia comercial.
