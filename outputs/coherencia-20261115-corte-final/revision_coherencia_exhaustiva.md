# Revisión exhaustiva de coherencia: Excel, Entregable 2 y subdocumentos CORRIGIENDO

**15 de noviembre de 2026 · America/Santiago · Solo diagnóstico. No se corrigió la oferta ni el Excel.**

## Dictamen ejecutivo

**Los documentos todavía no forman una línea base económica y técnica coherente para entregar.** La suma principal del Excel y las HH totales concilian. Los problemas principales están en la versión publicada de E2, la atribución y nivelación de las innovaciones, los compromisos de pruebas y aceptación, y ciertas coberturas económicas aún sin demostrar.

Esta revisión usa una **nueva exportación autenticada del Excel** y las ramas actualizadas, no los números de los informes previos. Se conservan los identificadores C01–C25 para facilitar seguimiento y se agregan C26–C27. Las observaciones anteriores que ya no describen la versión actual se retiran expresamente.

### Hallazgos principales

1. **E2 sigue publicando 200.024,98 UF de costo y 235.308,64 UF de precio neto.** El Excel actual tiene **203.680,04 UF y 239.329,21 UF**. Difieren 55 de las 56 filas del flujo mensual.
2. Las **200.783,82 HH internas** sí coinciden con los 37 perfiles del T-15. Con 1.324,80 HH de terceros se obtienen las **202.108,62 HH** del plan. No hay que tratar esa diferencia como personal omitido.
3. Las innovaciones suman las mismas **5.552 HH**, pero la mezcla de perfiles no es la del T-15 y ahora hay **13 combinaciones perfil/mes sobreasignadas**. Ampliar ventanas globales no las nivela.
4. **Se incorporaron costos reales antes omitidos:** Fargate productivo, red/seguridad productiva y los dos controladores inalámbricos con accesorios/repuestos. No se repiten como si siguieran ausentes. Persisten partidas pendientes y alcances no conciliados.
5. SD13 ya identifica sesiones de evidencia de abril de 2028, pero contradicen las fechas y la distribución de perfiles del T-15. SD9 asigna QA a paquetes donde el T-15 no asigna esos perfiles.
6. Una demora de un mes en H4 deja **−1.310,87 UF aun usando toda la línea de respaldo**, bajo la prueba aislada descrita en C14. La caja positiva del escenario nominal no prueba esa cobertura.

**Prioridad no equivale a sanción contractual:** Alta = afecta la conciliación sustantiva del costo, capacidad, aceptación o liquidez. Media = contradicción documental o cobertura pendiente que debe explicitarse. Baja = defecto acotado de presentación o escenario no aplicado. No se declara inadmisibilidad jurídica ni un presupuesto corregido.

## 1. Fuentes, actualización y límites

### Excel

[Archivo de referencia suministrado](https://docs.google.com/spreadsheets/d/18wI3xm9e1alpcn0JKE8CJcjPKg3G4-UP/edit?gid=1717014239#gid=1717014239). Título observado: **LafroX_ModeloFinanciero_3_20261113.xlsx**, en modo de edición de archivos Microsoft Excel de Google. Se exportó una copia de lectura de las **19 hojas**, preservando fórmulas y valores almacenados. No se creó una hoja nativa ni se escribió en el original.

SHA-256 de la copia revisada: `3e66f11b564fe6ef9de668e91ed7cc060c2f67eed1ee84e371d1cf58184eb34b`. Registro del corte analítico: **15-11-2026, 16:28 America/Santiago**. La copia está congelada para reproducibilidad; cambios posteriores del archivo vivo no quedan cubiertos.

### Git

Se ejecutó **`git fetch --all --prune`** y **`git pull --ff-only origin LafroX-OfertaEconomica-2-Latex`**. Las ramas no abiertas se actualizaron mediante fetch remoto→rama local **sin forzar**, equivalente a incorporar únicamente el avance permitido de cada rama sin cambiar de checkout ni mezclar subdocumentos. SD4, abierto en otro worktree, se actualizó con **`pull --ff-only`**. Las refs locales revisadas quedaron iguales a sus remotas en el corte.

No se hicieron merges entre capítulos, commits, push, sustituciones de fuentes ni recompilaciones de entregables. Los fast-forward son la actualización solicitada por el usuario, no correcciones hechas durante la revisión.

SD8 no tiene una rama denominada CORRIGIENDO: se tomó explícitamente **Revision** como complemento y se distingue de las ramas solicitadas. La rama de anexos se usa para contrastar trazabilidad, no como sustituto aprobado de las versiones de cada subdocumento.

| Documento | Rama revisada | Commit |
|---|---|---|
| SD1 | `LafroX-Subdoc1-LateX-CORRIGIENDO` | `278a4c41` |
| SD2 | `LafroX-Subdoc2-LateX-CORRIGIENDO` | `a72407bc` |
| SD3 | `LafroX-Subdoc3-LateX-CORRIGIENDO` | `0ef1bf86` |
| SD4 | `LafroX-Subdoc4-LateX-corrigiendo` | `5485aaf9` |
| SD5 | `LafroX-Subdoc5-LateX-CORRIGIENDO` | `daec1657` |
| SD6 | `LafroX-Subdoc6-LateX-corrigiendo` | `68a9f14f` |
| SD7 | `LafroX-Subdoc7-LateX-CORRIGIENDO` | `8216b639` |
| SD9 | `LafroX-Subdoc9-LateX-corrigiendo` | `007949aa` |
| SD13 | `LafroX-Subdoc13-LateX-corrigiendo` | `31117a1f` |
| SD8 | `Lafrox_Subdocumento_8_Latex_Revision` | `c619c8e7` |
| Anexos | `LAFROX-Subdocumentos-Anexos` | `053f7663` |
| E2 | `LafroX-OfertaEconomica-2-Latex` | `6b55a222` |

### Qué se comprobó

- Inventario y lectura de las 19 hojas; fórmulas de resultados y precedentes relevantes; barrido de errores de celda almacenados.
- Recálculo independiente de ingresos, costo, VAN, caja financiada, cobertura de soporte, reservas y costo atribuido a innovaciones.
- Comparación de los **56 meses** de E2, **37 perfiles** y **239 filas de asignación** del T-15: 227 códigos EDT únicos, sus desgloses repetidos y siete ajustes/reservas sin código propio. Se preservaron las filas repetidas al conciliar el total, no se sobrescribieron como si cada código fuera una sola fila.
- Cruce de compras/servicios del T-11, responsabilidades, T-14/T-15/T-18, calidad T-13/T-17, riesgo T-16/8.H e innovaciones T-19.
- Comparación de **639 pares de estados reconocidos T-12/T-13**, con revisión directa de las diez diferencias. No se interpretan filas no reconocidas/alias como requisitos perdidos.
- Extracción de los PDF versionados E2, T-15 y T-18 y de la copia alternativa local de E2. No se confundió fuente actual con PDF actualizado.
- Revalidación de los cambios nuevos de SD3, SD4, SD6, SD7, SD9 y SD13, incluida evidencia que invalida afirmaciones de la revisión anterior.

### Límites de la conclusión

Es una revisión exhaustiva del **cruce económico/documental descrito**, no una certificación técnica individual de los 653 requisitos ni un ensayo de infraestructura. No se perturbaron todas las entradas en Excel de escritorio ni se certificó el recálculo de cada fórmula en ese motor. Se leyeron fórmulas y valores exportados y se recalcularon independientemente los resultados indicados. Cero errores de celda no significa cero errores de lógica.

No se auditaron cotizaciones comerciales vigentes, acreditaciones, firmas, permisos de Google ni suficiencia jurídica. Salvo la regla LCU de C27, contrastada con documentación primaria de AWS, se evalúa la coherencia de la propia documentación. Una compra sin desglose no se considera automáticamente omitida: se distingue **contradicción confirmada**, **cobertura no demostrada** y **condición pendiente**. No deben sumarse todos los montos observados como si fueran incrementos independientes del costo del proyecto.

## 2. Cifras de E2 frente al Excel actual

Valores en UF. Son las cifras del modelo tal como está, no de un presupuesto corregido.

| Concepto | E2 | Excel actual | Diferencia Excel−E2 | Fuente Excel |
|---|---:|---:|---:|---|
| Costo implementación | 88.884,92 | 92.411,99 | 3.527,07 | `RESUMEN!B10` |
| Costo operación | 111.140,06 | 111.268,05 | 127,99 | `RESUMEN!B11` |
| Costo total | 200.024,98 | 203.680,04 | 3.655,06 | `RESUMEN!B12` |
| Precio implementación | 105.093,38 | 108.973,15 | 3.879,77 | `RESUMEN!G10` |
| Precio operación | 130.215,27 | 130.356,06 | 140,79 | `RESUMEN!G11` |
| Precio neto total | 235.308,64 | 239.329,21 | 4.020,57 | `RESUMEN!G12` |
| Margen monetario | 35.283,66 | 35.649,17 | 365,51 | `RESUMEN!L12` |
| VAN antes de impuestos | 24.691,13 | 24.976,69 | 285,56 | `INDICADORES!B5` |
| Cuota mensual operación | 3.617,09 | 3.621,00 | 3,91 | `RESUMEN!G11/36` |
| Mínimo de caja financiada | 489,87 | 206,78 | -283,09 | `FLUJO CAJA NETO!M8` |
| Caja final financiada | 35.399,78 | 35.765,28 | 365,50 | `FLUJO CAJA NETO!BH8` |

El margen actual es **14,90 %**. La TIR mensual es **7,14 %** y la anual **128,84 %**. La tasa mensual de descuento permanece en **0,997768607 %**. Cambian también IVA, conversiones, cuadros anuales, sensibilidad, punto de equilibrio, hitos y Curva S.

## 3. Hallazgos detallados

Cada observación distingue evidencia, efecto y lo que queda sin acreditar. Las indicaciones de conciliación son criterios de cierre, no cambios aplicados.

| ID | Prioridad | Hallazgo |
|---|---|---|
| C01 | Alta | E2 no reproduce el modelo financiero vigente |
| C02 | Media | El catálogo de operación e implementación de E2 sigue siendo de otra versión |
| C03 | Alta | Las innovaciones usan perfiles y costos distintos a las partidas del T-15 |
| C04 | Alta | Las ventanas macro de innovaciones no reproducen su reparto por paquete |
| C05 | Alta | Trece combinaciones perfil/mes exceden el presupuesto disponible |
| C06 | Alta | El beneficio total suma efectos que SD13 prohíbe acumular sin conciliación |
| C07 | Media | Los beneficios usan población y adopción completas sin conciliarlas con el despliegue |
| C08 | Alta | La cobertura productiva previa a M21 mejoró, pero siguen previsiones sin aplicar y componentes sin puente |
| C09 | Media | Los equipos antes omitidos ya están presupuestados; licencias, soporte y entrega siguen pendientes |
| C10 | Alta | Los servicios especializados del T-15 no tienen conciliación económica explícita |
| C11 | Media | El costo de mantención usa promedios que no reproducen sus paquetes |
| C12 | Media | El proveedor, canal y volumen económico no son los del diseño técnico |
| C13 | Media | INN-05 conserva impresión física sin cobertura del consumible ni criterio de pagador |
| C14 | Alta | La línea de respaldo no cubre una demora de un mes de H4 |
| C15 | Media | El Resumen llama total del proyecto a dos estimaciones de alcances no conciliados |
| C16 | Baja | La columna de total HH contiene valores manuales antiguos |
| C17 | Media | La exportación XLSX no acredita los controles de entrada y protección de E-21 |
| C18 | Media | La contingencia de SD8 incluye R-036 y la del Excel todavía no |
| C19 | Alta | El escenario de nube no productiva de operación está desconectado o sin entradas |
| C20 | Alta | Las sesiones M15 nuevas contradicen fechas y perfiles del T-15 |
| C21 | Media | La asignación QA de SD9 no corresponde a los perfiles de sus paquetes T-15 |
| C22 | Media | Los PDF versionados T-15 y T-18 no representan sus fuentes actuales |
| C23 | Alta | H4 y los cobros nominales conservan condiciones de aceptación sin conciliar |
| C24 | Media | T-13 declara Cumple en diez requisitos que T-12 declara parciales |
| C25 | Media | Los códigos EDT citados no acreditan toda la cobertura funcional y económica |
| C26 | Media | El estado Cumple de RT-26.04 contradice la propia descripción de riesgos de innovación |
| C27 | Baja | La previsión LCU suma dimensiones donde corresponde la dimensión máxima |

### C01 · Alta — E2 no reproduce el modelo financiero vigente

**Confirmado.** Tanto las fuentes como la página física 7 del PDF versionado de E2 publican los valores antiguos de la tabla anterior. Difieren **55/56 filas** del cuadro mensual con tolerancia de 0,011 UF para evitar falsos positivos de impresión. El costo total difiere **3.655,06 UF** y el precio **4.020,57 UF**.

Además, `outputs/LAFROX_AnalisisFinanciero_2_20261113.pdf`, no rastreado, publica **220.875,90/260.429,58 UF**, margen 15,19 % y VAN 28.055,82 UF, también en página física 7. No se lo considera reemplazo aprobado de la rama: conviven **tres versiones económicas distintas**.

**Efecto.** El documento de explicación no permite reconstruir la planilla que se entregaría. Actualizar solo la introducción dejaría flujos, tablas, impuestos, sensibilidad y gráficos contradictorios. Primero debe definirse el modelo final y luego regenerarse su publicación completa.

**Localización:** [E2: 02_analisis_economico_financiero/contenido.tex, línea 5](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/E2/02_analisis_economico_financiero/contenido.tex); [E2: 02_analisis_economico_financiero/secciones/2-2_evaluacion_financiera.tex, línea 39](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/E2/02_analisis_economico_financiero/secciones/2-2_evaluacion_financiera.tex).

### C02 · Media — El catálogo de operación e implementación de E2 sigue siendo de otra versión

**Confirmado.** E2 usa Intune para 382 equipos, 29,05 UF/mes durante toda la operación. El Excel cambia a **433 equipos desde M25**: `PARAMETROS!C73:C75`, `PROVEEDORES!F74` y `COSTOS!AA69:BF69`. El costo Intune es **1.169,95 UF**, frente a 1.045,84 UF manteniendo 382: **124,11 UF ya incorporadas**, que no deben sumarse de nuevo.

La nube de implementación tampoco se reconstruye con los 32,03 UF/mes desde M2 que describe E2. `COSTOS!C63:V63` suma **3.492,00 UF**, con cargos productivos por fase. Las compras adicionales C09 también están ya en el Excel, no en el catálogo publicado.

**Efecto.** Cambian cantidades, calendario y composición, no solo el total. El puente de catálogo→consumo→costo mensual debe reproducir la misma versión.

**Localización:** [E2: 02_analisis_economico_financiero/secciones/2-4_estrategia_adquisiciones.tex, línea 43](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/E2/02_analisis_economico_financiero/secciones/2-4_estrategia_adquisiciones.tex); Excel `COSTOS!63,69`.

### C03 · Alta — Las innovaciones usan perfiles y costos distintos a las partidas del T-15

**Confirmado.** `INNOVACIONES!A24:K63` y E2 2.7 atribuyen INN-02 principalmente a QA Senior, INN-04 a Jefe de Proyecto e INN-05 al Coordinador. T-15 distribuye esas mismas HH entre varios perfiles.

| Innovación | HH totales coincidentes | Costo HH Excel/E2 | Costo HH por mezcla real T-15 | Diferencia T-15−Excel |
|---|---:|---:|---:|---:|
| INN-01 | 960 | 768,00 | 768,00 | 0,00 |
| INN-02 | 1.536 | 752,18 | 726,95 | −25,23 |
| INN-03 | 1.248 | 998,40 | 998,40 | 0,00 |
| INN-04 | 688 | 997,60 | 650,63 | −346,97 |
| INN-05 | 1.120 | 672,00 | 778,87 | 106,87 |
| **Total** | **5.552** | **4.188,18** | **3.922,85** | **−265,33** |

Ejemplo: 8.3.4 son **343,20 HH PMO +184,80 HH JP**: 473,88 UF con las tarifas del propio Excel, no 765,60 UF por imputar 528 HH completas al JP. En INN-01/03 los perfiles de Datos tienen igual costo horario, por eso la mezcla no cambia el total; sí importa para su capacidad.

**Efecto.** No es reconstruible la atribución por innovación desde la planificación citada. **No es un ahorro automático de 265,33 UF del proyecto**, porque los perfiles ya están presupuestados globalmente. El criterio es rastrear EDT→perfil→HH→mes→tarifa, sin añadir nuevamente esas HH al costo total.

**Localización:** [SD7: formulario-t15/tablas/tab_T15_asignacion_partidas.tex, línea 128](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD7/formulario-t15/tablas/tab_T15_asignacion_partidas.tex); [E2: 02_analisis_economico_financiero/secciones/2-7_valorizacion_innovaciones.tex, línea 37](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/E2/02_analisis_economico_financiero/secciones/2-7_valorizacion_innovaciones.tex); Excel `INNOVACIONES!J64`.

### C04 · Alta — Las ventanas macro de innovaciones no reproducen su reparto por paquete

**Parcialmente atendido, aún no conciliado.** Se ampliaron las ventanas de INN-01/02/03 e INN-05 en Excel y E2. Las revisiones de INN-03 ahora coinciden con SD7/SD13 en M24,27,30,36,39,42,48,51,54. Ese avance no arregla la asignación del resto:

| Caso | Reparto Excel/E2 | Partidas T-15 |
|---|---|---|
| INN-01 inversión | 960 HH uniformes M7–15 | Cuatro partidas de 240 en M7–9, M9–10, M9–10 y M11–15 |
| INN-02 inversión | 960 HH uniformes M2–15 | 240 en M2–3, M3–5, M5–10 y M11–15 |
| INN-03 inversión | 960 HH uniformes M3–15 | 240 en M3–5, M5–9, M9–10 y M11–15 |
| INN-04 | 160 HH JP M17–23 | 80 en M17–20 y 80 en M21–23, además con mezcla PMO/JP |
| INN-05 | 893,4 HH Coordinador M13–21 y 226,6 M22–27 | Cuatro partidas de 240, más 80 de despliegue M22–26 y 80 del bloque legal M24–27; perfiles mixtos |

**Efecto.** Coincidir en primer/último mes y HH totales no implica coincidir en la carga mensual ni en el trabajo que financia cada fase. Los casos de C05 son una consecuencia comprobable. No debe redistribuirse costo o esfuerzo sin preservar sus partidas y autorización.

**Localización:** [SD7: formulario-t15/tablas/tab_T15_asignacion_partidas.tex, línea 125](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD7/formulario-t15/tablas/tab_T15_asignacion_partidas.tex); Excel `INNOVACIONES!E24:H63`.

### C05 · Alta — Trece combinaciones perfil/mes exceden el presupuesto disponible

**Confirmado por recálculo.** Se distribuyeron las HH de cada fila `INNOVACIONES!24:63` uniformemente dentro de su ventana inclusiva, como hace su costo mensual K, y se sumaron por perfil/mes. Se compararon con `HH POR ROL Y MES!C8:BF44`.

| Perfil | Mes | HH solo innovaciones | HH totales disponibles | Exceso mínimo |
|---|---:|---:|---:|---:|
| Ingeniero de Datos y Bases Senior | 3 | 73,85 | 51,98 | 21,87 |
| Analista QA Senior | 4 | 68,57 | 47,29 | 21,28 |
| Ingeniero de Datos y Bases Senior | 4 | 73,85 | 62,47 | 11,38 |
| Analista QA Senior | 7 | 68,57 | 33,74 | 34,83 |
| Analista QA Senior | 8 | 68,57 | 38,71 | 29,86 |
| Analista QA Senior | 12 | 68,57 | 35,64 | 32,93 |
| Ingeniero de Datos y Bases Senior | 13 | 180,51 | 66,40 | 114,11 |
| Coordinador de Implantación | 18 | 99,27 | 21,22 | 78,05 |
| Coordinador de Implantación | 24 | 37,77 | 0,00 | 37,77 |
| Coordinador de Implantación | 27 | 37,77 | 31,89 | 5,88 |
| Líder de Calidad y Pruebas | 39 | 43,50 | 7,56 | 35,94 |
| Analista QA Senior | 53 | 25,40 | 24,20 | 1,20 |
| Analista QA Senior | 55 | 24,10 | 22,98 | 1,12 |

**Efecto.** La innovación sola excede el presupuesto total del perfil, incluso antes de sus otras tareas. Es especialmente directo el Coordinador en **M24: 37,77 HH atribuidas frente a cero**. Los cinco casos de la revisión anterior ya no son la lista válida: ahora son trece.

El control no supone que las personas deban trabajar 160 HH adicionales ni propone agregar las diferencias al proyecto. Primero deben conciliarse los perfiles/paquetes reales C03–C04 y repetirse la nivelación. Comprobar que un perfil tiene alguna actividad en el mes no demuestra capacidad suficiente.

**Localización:** Excel `INNOVACIONES!E24:H63` y `HH POR ROL Y MES!C8:BF44`; [CSV con los 13 casos](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/outputs/coherencia-20261115-corte-final/sobrecarga_innovaciones_perfil_mes.csv).

### C06 · Alta — El beneficio total suma efectos que SD13 prohíbe acumular sin conciliación

**Confirmado.** `INNOVACIONES!K84=SUM(K79:K83)` suma **53.878,83 UF**, repetidas como beneficio total del CLIENTE en E2. SD13 conserva la regla de que los efectos **no se suman entre sí**. INN-01/03 pueden actuar sobre pérdidas relacionadas; INN-04 tampoco se agrega sin excluir coincidencias. INN-05 valora tiempo del almacenero, no ingreso ni ahorro de caja automático de Puelche.

**Efecto.** La suma es aritméticamente correcta pero no demuestra un beneficio económico agregado válido y mezcla beneficiarios. Debe acreditarse exclusión/atribución por evento, lote o entrega y separar el beneficio de Puelche del de terceros. La cautela «valores máximos» no acredita aditividad. Es correcto que estos beneficios no entren en el flujo de LafroX; ese control no corrige la suma presentada.

**Localización:** [SD13: SD13_v_nueva/13_anexos/contenido.tex, línea 125](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD13/SD13_v_nueva/13_anexos/contenido.tex); [E2: 02_analisis_economico_financiero/secciones/2-7_valorizacion_innovaciones.tex, línea 5](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/E2/02_analisis_economico_financiero/secciones/2-7_valorizacion_innovaciones.tex); Excel `INNOVACIONES!K84`.

### C07 · Media — Los beneficios usan población y adopción completas sin conciliarlas con el despliegue

**Brecha de supuestos, no error de suma.** SD13 nuevo ya declara equivalencias antes implícitas: una entrega por pedido y un lote por recepción ponderada por proporción de SKU. No son mediciones de la población elegible.

- B-01 aplica reducción a las **2,4 millones de unidades mensuales**, aunque piloto/acciones se dirigen a locales y rutas elegibles del canal tradicional.
- B-03 estima **150,60 lotes/mes** con 1.150 recepciones ×1.100/8.400 SKU; la equivalencia de SKU y lotes no está validada.
- B-04 usa **31.000 pedidos** como entregas comparables. Debe conservarse como supuesto, no como hecho medido.
- B-05 usa **50.647,89 decisiones/mes desde M21**, aunque el despliegue por olas sigue M22–26 y la medición de cobertura llega M27. No se aplica un factor de cobertura/adopción por ola.
- SD13 pide descontar canjes/descuentos de INN-01; E2 valora lo evitado a precio de venta, no a pérdida o margen neto evitado.

**Cambio que se retira:** ya no corresponde afirmar una contradicción automática de doce meses M21/M33 en INN-05. El anexo diferencia **minutos del almacenero desde M21** de **efecto comercial desde M33**. No se impone el antiguo ajuste de −1.215,55 UF.

**Efecto.** Hay escenarios exploratorios, no beneficios ya acreditados. La conciliación exige volumen elegible, cobertura, adopción, cambio causal y valor neto por beneficiario.

**Localización:** [SD13: SD13_v_nueva/13_anexos/contenido.tex, línea 40](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD13/SD13_v_nueva/13_anexos/contenido.tex); [SD13: SD13_v_nueva/13_anexos/contenido.tex, línea 129](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD13/SD13_v_nueva/13_anexos/contenido.tex); Excel `INNOVACIONES!A79:K83`.

### C08 · Alta — La cobertura productiva previa a M21 mejoró, pero siguen previsiones sin aplicar y componentes sin puente

**Cobertura incorporada, no omisión total.** El nuevo Excel individualiza y enlaza a `COSTOS!H63:V63`:

| Bloque de ADQUISICIONES IMPLEMENTACIÓN | Cobertura | Total UF |
|---|---|---:|
| O51:S54 | Aurora Producción/Recuperación, Fargate Recuperación y DMS | 1.473,99 |
| O59:S60 | 11 tareas Fargate productivas M6–20; dos AS2 M19–20 | 235,39 |
| O66:S76 | ALB, VPN/TGW São Paulo, NAT, CA, Shield y almacenamiento Aurora | 956,60 |
| **S78** | **Productivo identificado antes de M21** | **2.665,98** |

No se confirmó doble conteo de esos tres bloques en la fórmula inspeccionada: cada rango se agrega una vez. **Se retira el hallazgo de Fargate productivo sin partida.**

**Brechas actuales:**

1. `O122:V150`, **«pendiente de aplicar»**, cifra **399,20 UF** de tráfico, LCU, respaldo y soporte. No alimenta `COSTOS!63` ni S78. Ese importe no demuestra por sí solo faltante neto: hay que conciliarlo con agregados existentes para evitar solapamientos.
2. Verified Access está calculado: **P112=263,62 UF**, pero **P101=0**, cobertura previa declarada P109=0 y P113=0. SD4 lo ofrece para el acceso de 184 usuarios internos y administración. El escenario está apagado en preM21; falta acreditar cobertura/decisión por fase, no simplemente sumarlo.
3. SD4 exige recuperación regional con **TGW y VPN propios en Virginia** además de otros componentes. El bloque nuevo identifica VPN/TGW São Paulo, no un puente completo de recursos de recuperación por mes.
4. El antiguo agregado B11 de 275,79 USD/mes está descrito para seguridad/monitoreo/respaldos de **ambientes de prueba**. No acredita por sí solo todos los costos productivos ni su soporte.

**Efecto.** La nueva inversión es real, pero el alcance completo aún no es reconstruible. No se cuantifica un déficit neto sumando escenarios apagados o pendientes a ciegas. C19 trata aparte los ambientes no productivos de operación.

**Localización:** Excel `ADQUISICIONES IMPLEMENTACIÓN!O49:V150`, `COSTOS!C63:V63`; [SD4: 04/partes/4.2_fisica/02_b_servicios_nube.tex, línea 109](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD4/04/partes/4.2_fisica/02_b_servicios_nube.tex); [SD4: 04/partes/4.2_fisica/02_c_conexiones.tex, línea 35](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD4/04/partes/4.2_fisica/02_c_conexiones.tex).

### C09 · Media — Los equipos antes omitidos ya están presupuestados; licencias, soporte y entrega siguen pendientes

**Se retira la omisión anterior.** `ADQUISICIONES IMPLEMENTACIÓN!A85:I93` incorpora:

| Equipo/repuesto | Cantidad | Costo UF |
|---|---:|---:|
| Cisco CW9800L | 2 | 544,41 |
| CW9800L-RPS | 2 | 35,54 |
| Bandeja doble CW9800L-RMNT | 1 | 14,83 |
| SSD HPE 1,92 TB | 1 | 32,35 |
| Fuente HPE 500 W | 1 | 2,52 |
| **Total incorporado** | | **629,65** |

I24 e I42 enlazan estos importes y llegan a **FLUJO CAJA NETO!F66**, por lo que no están solo en una nota. El disco NAS también está cubierto: cinco unidades, cuatro instaladas y una de repuesto.

**Pendiente real.** La fila A92 «Licencias, soporte y despacho» no tiene cantidad/costo. Los estados del propio bloque dicen cotización local pendiente, confirmar disponibilidad y homologar el SSD con los discos instalados. E2 y PROVEEDORES no presentan el mismo catálogo completo.

**Efecto.** Existe una previsión de equipos, pero todavía no costo integral puesto en sitio ni acreditación de configuración/licencias y plazo. No se declara que falten otros 629,65 UF ni que esos precios sean cotizaciones comerciales cerradas.

**Localización:** Excel `ADQUISICIONES IMPLEMENTACIÓN!A85:I93,I24,I42`, `FLUJO CAJA NETO!F66`; [SD4: 04/formularios/T11/15_anexo_t11.tex, línea 36](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD4/04/formularios/T11/15_anexo_t11.tex).

### C10 · Alta — Los servicios especializados del T-15 no tienen conciliación económica explícita

**Cobertura no demostrada.** El código 00 del T-15 contiene **1.324,80 HH**: 864 de implementación y 460,80 de operación. Incluye **320+160 HH de pruebas ofensivas independientes**, 384 HH de instalaciones especializadas y 230,40+230,40 HH de ciberseguridad y revisión eléctrica en operación.

Las instalaciones podrían estar incluidas en compras «con montaje» u obras. Por eso no deben convertirse en costo adicional automáticamente. Pero no se aporta el puente **código 00→servicio/contrato→proveedor→costo→mes** y no se identifica una partida específica de pruebas independientes en PROVEEDORES. E2 atribuye a LafroX pruebas de aceptación sin distinguir suficientemente la ejecución independiente comprometida.

**Efecto.** Conciliar las HH de nómina no acredita haber costeado esos contratos. No corresponde añadir 1.324,80 HH a personal interno ni valorarlas todas a una tarifa genérica. Hay que demostrar inclusión previa o costo contractual específico.

**Localización:** [SD7: formulario-t15/tablas/tab_T15_asignacion_partidas.tex, línea 115](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD7/formulario-t15/tablas/tab_T15_asignacion_partidas.tex); [SD7: formulario-t15/tablas/tab_T15_asignacion_partidas.tex, línea 216](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD7/formulario-t15/tablas/tab_T15_asignacion_partidas.tex); Excel `PROVEEDORES`.

### C11 · Media — El costo de mantención usa promedios que no reproducen sus paquetes

**Confirmado.** E2 2.6 aplica 0,68 UF/HH a Desarrollo y 0,96 a SRE/DevOps, promedios de grupos globales. T-15 usa mezclas distintas por partida y asigna **230,40 HH preventivas a terceros**.

| Partida | Costo por perfiles reales del T-15 | Publicación E2 |
|---|---:|---:|
| 8.2.1 correctivo/evolutivo | 3.134,59 UF | 3.128,84 UF entre ambas líneas |
| 8.2.4 deuda técnica | 1.558,66 UF | 1.564,42 UF |
| 8.2.5+8.2.7 | 1.080,00 UF | 1.105,18 UF |
| Preventiva: 8.1.3+8.1.6+8.2.3+parte interna 8.2.6 | 2.183,88 UF **más servicio externo no acreditado** | 2.471,31 UF como si todo fuera personal interno |

El reparto 50/50 entre correctivo y evolutivo debe identificarse como supuesto si no lo fija la asignación por perfil.

**Efecto.** El desglose no es una suma de las horas/perfiles que dice utilizar. Son atribuciones dentro de costos ya globalmente presupuestados, no subtotales que deban agregarse otra vez al costo total.

**Localización:** [E2: 02_analisis_economico_financiero/secciones/2-6_mantencion_soporte.tex, línea 35](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/E2/02_analisis_economico_financiero/secciones/2-6_mantencion_soporte.tex); [SD7: formulario-t15/tablas/tab_T15_asignacion_partidas.tex, línea 215](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD7/formulario-t15/tablas/tab_T15_asignacion_partidas.tex).

### C12 · Media — El proveedor, canal y volumen económico no son los del diseño técnico

**Confirmado.** T-11/INT-11 declaran **SES, SNS y AWS End User Messaging Social**, con 2.800/5.200 avisos diarios y precio unitario por canal remitido a la oferta económica. PROVEEDORES y E2 presupuestan **Twilio y Mercado Pago**; la fórmula de operación usa 2.000 mensajes y comisión de 3,19 % sobre 20 millones CLP, sin puente con la mezcla/volumen del diseño. La arquitectura identifica **Transbank** como dependencia de pago.

La fibra técnica prioriza **Telsur**, o un operador fijo distinto de Entel si no hay factibilidad, porque el respaldo LTE de los CD es Entel. La planilla/E2 presupuestan **Entel** para fibra; parte de LTE cita Virgin donde el diseño establece Entel/Claro.

**Efecto.** No queda probado que los montos financien el mismo servicio ni la diversidad de operadores ofrecida. Debe conciliarse servicio, proveedor o alternativa aprobada, volumen, unidad, tarifa, pagador y calendario. Cotizar dos servicios distintos no autoriza asumir equivalencia ni cobrarlos ambos.

**Localización:** [SD4: 04/formularios/T11/15_anexo_t11.tex, línea 37](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD4/04/formularios/T11/15_anexo_t11.tex); [SD4: 04/formularios/T11/15_anexo_t11.tex, línea 114](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD4/04/formularios/T11/15_anexo_t11.tex); Excel `PROVEEDORES!B42:L47,B71:L76`.

### C13 · Media — INN-05 conserva impresión física sin cobertura del consumible ni criterio de pagador

**Cobertura pendiente, con cambio reconocido.** T-19 nuevo retiró el papel térmico de su descripción de costo operacional y atribuye la explicación a tiempo de preventa de Puelche. Pero la impresión física **sigue ofertada**, incluso en los campos cercanos del mismo T-19 y en el capítulo de innovación.

Excel/E2 presentan **1,16 UF** de costo operacional no-HH de INN-05, correspondiente a nube. No hay cantidad/precio de copias durante 36 meses ni regla de quién paga papel, merma y tiempo incremental. Un rollo inicial con el equipo no acredita el consumo contractual completo.

**Efecto.** Borrar el consumible del campo de costos no prueba que esté cubierto. Si lo absorbe el CLIENTE debe quedar como costo de adopción y ajustarse la lectura del beneficio; si lo absorbe LafroX debe existir partida. No se inventa un costo ni se carga automáticamente a LafroX lo que pudiera corresponder al cliente.

**Localización:** [SD13: SD13_v_nueva/T19/contenido.tex, línea 137](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD13/SD13_v_nueva/T19/contenido.tex); [E2: 02_analisis_economico_financiero/secciones/2-7_valorizacion_innovaciones.tex, línea 61](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/E2/02_analisis_economico_financiero/secciones/2-7_valorizacion_innovaciones.tex); Excel `INNOVACIONES!C-06` (fila 74).

### C14 · Alta — La línea de respaldo no cubre una demora de un mes de H4

**Confirmado mediante prueba aislada fuera del libro.** E2 presenta una línea de **1.250 UF** como respaldo ante atraso de un hito. La caja financiada de M10 es **8.336,45 UF** y el cobro H4 **10.897,32 UF**.

Si solo se desplaza ese cobro de M10 a M11, manteniendo los demás flujos:

`Caja M10 = 8.336,45 − 10.897,32 = -2.560,87 UF`.

Usando toda la línea: **-1.310,87 UF**, antes de intereses de esa línea. El modelo no fue editado para hacer esta prueba.

**Efecto.** La caja positiva nominal es verdadera, pero no respalda una afirmación genérica de cobertura frente a atrasos. «Ingresos ±20 %» prueba importes, no calendario; una reserva de HH no aporta liquidez bancaria. No se pronostica que H4 vaya a atrasarse ni se prescribe un financiamiento nuevo.

**Localización:** [E2: 02_analisis_economico_financiero/secciones/2-3_curva_s.tex, línea 34](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/E2/02_analisis_economico_financiero/secciones/2-3_curva_s.tex); Excel `FLUJO CAJA NETO!N8,N30`, `PARAMETROS!C51`.

### C15 · Media — El Resumen llama total del proyecto a dos estimaciones de alcances no conciliados

**Confirmado.** `RESUMEN!B35:B37` publica **47.768,44 HH, 36.575,17 UF de costo y 44.168,35 UF de venta** según puntos de caso de uso. La línea base del T-15 es 202.108,62 HH y el modelo total 203.680,04/239.329,21 UF.

El encabezado «Viabilidad y HH» ayuda a distinguir otra estimación, pero las filas siguen llamándose «Cantidad HH Proyecto», «Costo Total ... del Proyecto» y «Venta Total ... del Proyecto» sin definir fases/servicios incluidos y excluidos.

**Efecto.** No es válido compararlas como dos totales equivalentes ni concluir sobre/subestimación solo por su diferencia. Falta el puente del perímetro UCP con la EDT y los 56 meses de cobertura. La razón 2,77 % de innovaciones usa HH internas; sobre el total con terceros sería aproximadamente 2,75 %, por lo que también debe mantenerse claro el denominador.

**Localización:** Excel `RESUMEN!A30:C37`, `MODELO PUNTOS CASO DE USO!N39,N42,N46`.

### C16 · Baja — La columna de total HH contiene valores manuales antiguos

**Confirmado.** `HH POR ROL Y MES!B9=5.354`, mientras el perfil PMO suma **4.737,83 HH** en Sueldos. B31=1.152,45 frente a 1.534,85; B32=2.304,88 frente a 2.986,71. B33 muestra **496** para Instructor, frente a **512 HH mensuales sin capacitación** y **4.008 HH con ella**.

**Efecto.** Los encabezados pueden inducir a tomar como línea base cifras de otra versión. Debe distinguirse «servicio sin capacitación» de «total del perfil» y usar el mismo concepto. No hay omisión de capacitación: la matriz mensual **195.535,82 HH +5.248 HH** separadas suma exactamente **200.783,82 HH**.

**Localización:** Excel `HH POR ROL Y MES!B9,B31:B33`, `COSTOS HH - SUELDOS!E9,E31:E33`.

### C17 · Media — La exportación XLSX no acredita los controles de entrada y protección de E-21

**Confirmado en la copia entregable examinada.** Ninguna de las 19 hojas tiene protección de hoja activa. PARAMETROS, HH POR ROL Y MES, INNOVACIONES, PROVEEDORES y adquisiciones no tienen validaciones de entrada. Hay algunas en otras hojas: no se afirma que el libro carezca de toda validación.

E-21 pide validación de entradas y protección de fórmulas críticas. Celdas marcadas como bloqueadas por defecto no equivalen a protección activa.

**Efecto.** El archivo descargable no demuestra esos controles. La conclusión no se extiende a permisos/protecciones de Google, que no se auditaron y pueden no trasladarse al XLSX. Debe comprobarse el archivo que efectivamente se entregue, sin confundir control de edición con exactitud de cálculos.

**Localización:** [SD8: Datos externos/Bases/Bases_Administrativas.md, línea 1938](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD8/Datos%20externos/Bases/Bases_Administrativas.md); metadatos de las 19 hojas exportadas.

### C18 · Media — La contingencia de SD8 incluye R-036 y la del Excel todavía no

**Confirmado.** Anexo 8.H trabaja con **36 riesgos**, exposición inicial **1.199,52 HH**, contingencia propuesta **837,53 HH**, prevención 180 y gestión 160. R-036 añade **16,40 HH**, 9,84 ARQ y 6,56 CAL, uniformes M1–56, sin prevención adicional.

`COSTOS!C111:C117` sigue sumando **821,17 HH**. La diferencia respecto del importe publicado es **16,36 HH**, no solo 0,04 de redondeo. El componente R-036 se valora en **14,76 UF** con las tarifas representativas ARQ 1,10/CAL 0,60, antes de resolver centésimas, solapamiento y aprobación.

**Efecto.** Registro de riesgo y presupuesto están en versiones diferentes. Esa cifra no es una adición autorizada. Las **3.072 HH protegidas de E1 ya están en 202.108,62 HH**, no deben sumarse ni prestarse a E2. SD8 exige demostrar coincidencia riesgo–paquete–perfil/mes antes de reconocer solapamiento; tampoco asegura suficiencia estadística ni liquidez.

**Localización:** [SD8: 08_plan_riesgos/anexo-h-reservas.tex, línea 4](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD8/08_plan_riesgos/anexo-h-reservas.tex); Excel `COSTOS!C111:C117`.

### C19 · Alta — El escenario de nube no productiva de operación está desconectado o sin entradas

**Confirmado por precedentes de fórmula.** `ADQUISICIONES OPERACION!O8:AA43` calcula 36 meses de QA Fargate. `COSTOS!W63:BF63` busca ajustes solo en **filas 44:151**, excluyendo 8:43.

Las **108 filas 44:151** de Desarrollo Fargate, Preproducción Fargate y Preproducción Aurora carecen de las **seis entradas Q:U y AA**: 648 entradas vacías. X devuelve vacío porque no se cumple `COUNT(...)=6`; la fórmula de COSTOS usa `ISNUMBER` y convierte su participación en **ajuste cero**.

Así, el flujo conserva **368,9158714 UF/mes** de nube operacional. El comparador 24/7 frente a horario reducido y el QA calculado no equivalen a ahorro aplicado. Para QA, su diferencia bruta contra el costo previo declarado es −1.432,7808 USD en 36 meses; no es ahorro automáticamente válido sin probar inclusión previa/configuración.

**Efecto.** La existencia de un escenario FinOps no prueba que esté funcionando en el flujo. Los datos faltantes se silencian en cero sin señal de incompletitud. No se debe descontar todo el comparador ni asumir que el costo base es cero: hay que identificar ambientes, costo previo y decisión efectiva.

**Localización:** Excel `ADQUISICIONES OPERACION!O8:AA151,O154:U160`, `COSTOS!W63:BF63`.

### C20 · Alta — Las sesiones M15 nuevas contradicen fechas y perfiles del T-15

**Avance reconocido.** SD13 ahora sí define **EV-15-01/02/03, del 03 al 28 de abril de 2028**, con 48 HH por sesión. Ya no se informa «no existen sesiones».

**Contradicciones vigentes:**

1. T-15 diario mantiene el **20-03-2028** como término de 3.10.1.4, 3.10.2.4 y 3.10.3.4. SD13 coloca la evidencia que los cierra en abril y utiliza el fin tardío CPM 28-04 como si autorizara la ejecución, sin conciliar la programación diaria. T-15 advierte que su reparto mensual preliminar no acredita asignación diaria.
2. SD13 imputa **48 HH Senior** por sesión. Cada paquete de Datos tiene 128 Senior+64 Junior+48 Líder en M11–15: abril uniforme serían **25,6 Senior+12,8 Junior+9,6 Líder**, no 48 Senior. El paquete QA equivale a **33,272 Senior+11,128 Junior+3,6 Líder**, no 48 Senior.
3. Afirmar que caben porque abril tiene 533 HH globales de Datos y 154 de Calidad no comprueba el saldo después del resto del trabajo ni la coincidencia de perfil.

**Efecto.** Existe evidencia prevista, pero no un calendario y una imputación compatibles. **No son 144 HH faltantes** ni deben añadirse automáticamente: debe conciliase la ejecución de las existentes con sus otros compromisos y sucesoras.

**Localización:** [SD13: SD13_v_nueva/13_anexos/contenido.tex, línea 61](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD13/SD13_v_nueva/13_anexos/contenido.tex); [SD7: formulario-t15/contenido.tex, línea 121](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD7/formulario-t15/contenido.tex); [SD7: formulario-t15/tablas/tab_T15_asignacion_partidas.tex, línea 128](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD7/formulario-t15/tablas/tab_T15_asignacion_partidas.tex).

### C21 · Media — La asignación QA de SD9 no corresponde a los perfiles de sus paquetes T-15

**Contradicción nueva confirmada.** SD9 da titular QA Senior y relevos QA Junior/Líder de Calidad a las **83 ventanas** de 15 paquetes de construcción. Su anexo afirma que esas horas ya están valorizadas **«dentro de los paquetes 3.4 y 3.5»**, sin trasladarlas entre paquetes, meses o perfiles.

Sin embargo, `tab_T15_asignacion_partidas.tex:84–98` **no contiene 19S, 19J ni 16 en ninguno de los 3.4.* o 3.5.***; asigna Desarrollo o Datos. Tener HH QA globales en el mes no demuestra que estén en esas partidas.

SD9 también actualiza el subtotal de calidad **12.016→12.058,66 HH**: banco+mapa+piloto son 922,66 y no 880 HH. Es corrección/reclasificación de subtotal, no aumento automático de la línea base 202.108,62. El equipo compartido de 13 personas y 83,2 HH netas/día sigue requiriendo cuadrante real; máximos de 14 personas por paquete no son necesariamente 14 adicionales simultáneos.

**Efecto.** Asignar un nombre de rol a una ventana no prueba imputación económica ni nivelación. No se calcula déficit como 83×66,5 HH ni se suman nuevamente todas las HH de calidad. Debe existir puente ventana→sesión→persona/perfil/día→partida ya financiada. La trazabilidad complementaria de anexos marca este frente como corregido; esa etiqueta no subsana la contradicción con el T-15.

**Localización:** [SD9: SD9_v_nueva/09_anexos/contenido.tex, línea 319](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD9/SD9_v_nueva/09_anexos/contenido.tex); [SD7: formulario-t15/tablas/tab_T15_asignacion_partidas.tex, línea 84](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD7/formulario-t15/tablas/tab_T15_asignacion_partidas.tex); [SD9: SD9_v_nueva/T13/contenido.tex, línea 377](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD9/SD9_v_nueva/T13/contenido.tex).

### C22 · Media — Los PDF versionados T-15 y T-18 no representan sus fuentes actuales

**Confirmado.** El T-15 PDF de **139 páginas** conserva en página física **72** la redistribución de HH M21–22 si se atrasa el acta. La fuente actual habla de escenario nominal sujeto a confirmación escrita y no autoriza redistribuir HH sin cambio aprobado. En página **106** mantiene la declaración de iteraciones de hasta 14 días sin la distinción actual de seis ventanas mayores y su desdoble auxiliar.

T-18 PDF de **25 páginas**, páginas físicas **16 y 18**, conserva pasos a producción 17-05/18-10-2028 como fechas afirmativas; su fuente agrega firma previa y confirmación escrita de ventana fuera del despacho. Los commits nuevos de SD7 no actualizaron esos PDF.

**Efecto.** Revisar la última rama no equivale a tener el último compromiso en el archivo entregable. La observación compara contenido, no solo fechas del archivo. La numeración es física del PDF. No se recompiló nada durante esta revisión.

**Localización:** [SD7: LAFROX-Formulario-T-15.pdf](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD7/LAFROX-Formulario-T-15.pdf); [SD7: LAFROX-Formulario-T-18.pdf](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD7/LAFROX-Formulario-T-18.pdf); [SD7: formulario-t15/contenido.tex, línea 259](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD7/formulario-t15/contenido.tex); [SD7: formulario-t18/contenido.tex, línea 132](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD7/formulario-t18/contenido.tex).

### C23 · Alta — H4 y los cobros nominales conservan condiciones de aceptación sin conciliar

**Parcialmente aclarado, aún abierto.** SD13 explica ahora que H5/H10 entregan el expediente antes de cerrar administrativamente el paquete: no se repite que toda diferencia entre fecha de paquete y entrega prueba un atraso. En H4 sí mantiene **entrega nominal 20-10-2027** y **último informe de módulo 22-10-2027**, que se agrega como incremento final.

T-17 conserva la secuencia de revisión desde la entrega del 20 y acta 04-11, pero el expediente con el último incremento no está completo ese día. Su aceptación H4 exige 100 % de flujos E1 sin error y cero regresiones. Es preciso conciliar qué revisión corre por incremento y cuándo empieza la revisión del expediente completo.

Para H7/H12, T-15 sigue requiriendo **confirmación escrita de la Contraparte** del acta integrada y ventana de corte. SD9/anexos describen el mecanismo más afirmativamente, pero esa redacción no constituye el acta del cliente. Excel/E2 modelan ingresos nominales sin mostrar su sensibilidad de calendario.

**Efecto.** No se afirma atraso contractual automático ni cambio de mes por dos días de H4; se identifica un puente no cerrado entre expediente, revisión, acta y cobro. C14 muestra una consecuencia si el cobro cambia de mes. Un documento interno no acredita aprobación externa ni cobro garantizado.

**Localización:** [SD13: SD13_v_nueva/13_anexos/contenido.tex, línea 74](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD13/SD13_v_nueva/13_anexos/contenido.tex); [SD9: SD9_v_nueva/T17/contenido.tex, línea 143](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD9/SD9_v_nueva/T17/contenido.tex); [SD9: SD9_v_nueva/T17/contenido.tex, línea 165](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD9/SD9_v_nueva/T17/contenido.tex); [SD7: formulario-t15/contenido.tex, línea 272](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD7/formulario-t15/contenido.tex).

### C24 · Media — T-13 declara Cumple en diez requisitos que T-12 declara parciales

**Confirmado con las versiones nuevas.** Entre **639 pares reconocidos**, persisten estas diez discrepancias:

| Requisito | Estado T-12 | Estado T-13 | Líneas T12/T13 |
|---|---|---|---|
| RF-18.03 | Cumple parcialmente | Cumple | 218 / 219 |
| RNF-20.06 | Cumple parcialmente | Cumple | 297 / 299 |
| RNF-23.02 | Cumple parcialmente | Cumple | 315 / 322 |
| RT-03.18 | Cumple parcialmente | Cumple | 371 / 366 |
| RT-07.04 | Cumple parcialmente | Cumple | 459 / 469 |
| RT-08.12 | Cumple parcialmente | Cumple | 481 / 496 |
| RT-08.14 | Cumple parcialmente | Cumple | 483 / 498 |
| RT-11.04 | Cumple parcialmente | Cumple | 511 / 531 |
| RT-16.18 | Cumple parcialmente | Cumple | 596 / 636 |
| RT-16.23 | Cumple parcialmente | Cumple | 601 / 641 |

Ejemplo RT-16.18: T-12 reconoce que falta acreditar sello de tiempo y verificación tras vencimiento del certificado; T-13 trata la marca temporal del registro como sello de tiempo y declara Cumple. Se contrasta el estado documental, no se dictamina suficiencia jurídica.

**Efecto.** Catálogo y plan de pruebas no afirman el mismo alcance ofertado. Que una prueba esté prevista no demuestra que se haya ejecutado ni que una brecha del diseño esté resuelta. Los cinco requisitos modificados por los últimos commits no cierran estas diez filas. El recuento no certifica los 653 requisitos completos ni trata alias como requisitos extra.

**Localización:** [SD3: LAFROX-Formulario-T-12.tex, línea 218](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD3/LAFROX-Formulario-T-12.tex); [SD9: SD9_v_nueva/T13/matriz_requisitos.tex, línea 219](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD9/SD9_v_nueva/T13/matriz_requisitos.tex); [CSV de discrepancias](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/outputs/coherencia-20261115-corte-final/diferencias_estados_T12_T13.csv).

### C25 · Media — Los códigos EDT citados no acreditan toda la cobertura funcional y económica

**Confirmado como brecha de trazabilidad.** T-12 utiliza **3.3.5** para RF-17.02 (reglas), RF-17.08 (gestión documental), RT-16.14 (motor de reglas) y RT-16.29 (exportación asíncrona). Usa **3.6.4** para RF-17.09 y RT-16.19 (generación de documentos).

En T-14, 3.3.5 entrega un **registro auditable de stock, lotes y cobros** y 3.6.4 la **integración del servicio de avisos INT-11**. Sus entregables/aceptación no explicitan todas las funciones atribuidas; varias filas de T-12 ya dicen «alcance por precisar en T-14».

**Efecto.** Existe enlace a un código válido, pero no el puente completo requisito→entregable aceptable→HH/perfil→costo. No se concluye que esas funciones estén necesariamente sin implementar o sin presupuesto: debe identificarse qué trabajo existente las contiene y con qué aceptación. La igualdad de HH totales no reemplaza esa evidencia.

**Localización:** [SD3: LAFROX-Formulario-T-12.tex, línea 204](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD3/LAFROX-Formulario-T-12.tex); [SD7: formulario-t14/tablas/tab_T14_20.tex, línea 8](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD7/formulario-t14/tablas/tab_T14_20.tex); [SD7: formulario-t14/tablas/tab_T14_23.tex, línea 7](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD7/formulario-t14/tablas/tab_T14_23.tex).

### C26 · Media — El estado Cumple de RT-26.04 contradice la propia descripción de riesgos de innovación

**Confirmado en T-12/T-13.** RT-26.04 exige para **cada innovación** riesgo de adopción, probabilidad, impacto, mitigación y contingencia. La respuesta actual declara que INN-01/02/03/05 se gestionan con CT-08 a CT-13 **sin puntuación de probabilidad por impacto**; solo INN-04 remite a R-027 con probabilidad e impacto en T-16. Aun así T-13 marca Cumple.

Los controles del Anexo 8.E tienen responsables, acciones y criterios de prueba; eso no equivale por sí solo a la evaluación de probabilidad e impacto que la misma fila exige para cada innovación.

**Efecto.** Riesgo declarado, criterio de aceptación y estado de cumplimiento no son coherentes. No se deben convertir los controles en riesgos monetizados adicionales sin estimación, ni asumir que los 36 riesgos de SD8 ya cubren cuantitativamente todo el riesgo de adopción de las cinco innovaciones.

**Localización:** [SD9: SD9_v_nueva/T13/matriz_requisitos.tex, línea 770](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD9/SD9_v_nueva/T13/matriz_requisitos.tex); [SD8: 08_plan_riesgos/anexo-e-controles.tex, línea 20](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/fuentes/SD8/08_plan_riesgos/anexo-e-controles.tex); T-12 fila RT-26.04.

### C27 · Baja — La previsión LCU suma dimensiones donde corresponde la dimensión máxima

**Error confirmado, solo en escenario pendiente.** `ADQUISICIONES IMPLEMENTACIÓN!P128` usa:

`=P123+P126/25/3600+P126*P127/3000/3600+P126*2/1000/3600`

Obtiene **1.227,78 LCU-h** sumando tráfico, conexiones nuevas, activas y reglas. AWS factura la **dimensión máxima por hora**, no su suma. La regla se verificó en [documentación oficial de precios Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/pricing/), ejemplos de Application Load Balancer.

Bajo la homogeneidad mensual que supone esa tabla, domina la dimensión de bytes (1.000). El exceso ilustrativo es **2,51 USD/mes**, aproximadamente **0,92 UF en 15 meses**, incluido el soporte de 9 % usado por el escenario. Con perfiles horarios variables debe calcularse el máximo horario y sumar las horas; un máximo de agregados mensuales no sustituye siempre ese perfil.

**Efecto acotado.** V150 está «pendiente de aplicar» y desconectado del flujo: **no infla el costo total vigente**. Es un defecto de la previsión, no un sobrecosto actual demostrado. No se aplicó ninguna corrección.

**Localización:** Excel `ADQUISICIONES IMPLEMENTACIÓN!O122:V150`, especialmente `P128`.

## 4. Controles que sí concilian

Estos resultados no cierran las discrepancias de alcance, pero evitan diagnosticar faltantes inexistentes.

| Control independiente | Resultado | Estado |
|---|---:|---|
| Ingresos contractuales vs Resumen | 239.329,21 | Concilia |
| Costos vs Resumen | 203.680,04 | Concilia |
| VAN independiente | 24.976,69 | Concilia |
| HH perfiles vs T15 | 200.783,82 | Concilia |
| HH mensuales + capacitación | 200.783,82 | Concilia |
| HH con servicios externos | 202.108,62 | Concilia |
| HH innovaciones T15 | 5.552,00 | Concilia |
| Porcentajes hitos | 1,00 | Concilia |
| SOC HH operación | 26.280,00 | Concilia |
| Mesa HH operación | 38.246,00 | Concilia |
| NOC HH operación | 21.748,20 | Concilia |
| Nube innovación sin duplicación | 44,26 | Concilia |
| Caja final financiada | 35.765,28 | Concilia |
| 239 filas T15 con desgloses y ajustes vs línea base | 202.108,62 | Concilia |
| Servicios externos código00 todas las filas T15 | 1.324,80 | Concilia |
| Perfiles internos todas las filas T15 | 200.783,82 | Concilia |

Otros controles y avances reconocidos:

- Cero errores de celda almacenados en la exportación. No se presenta como certificación de recálculo completo o de lógica correcta.
- 37 perfiles T-15 coinciden individualmente con Sueldos. Mesa N1, NOC y SOC conservan cobertura por calendario, no una conversión artificial a 128 HH/mes.
- No se vuelve a sumar el costo de HH de innovaciones ni las 3.072 HH protegidas E1 como partidas nuevas. La nube incremental de innovaciones entra una sola vez.
- Ya existe Fargate productivo previo a M21 y nuevos cargos de red/seguridad. Las compras CW9800L y repuestos ahora sí llegan al flujo.
- El NAS incluye disco de repuesto. Intune incorpora el parque ampliado de 433 equipos.
- INN-03 ya no contempla laboratorio externo como costo base. No se vuelve a observar como gasto ausente obligatorio.
- Las revisiones de parámetros INN-03 están alineadas entre SD7 y SD13. INN-05 distingue ahorro de minutos desde M21 de efecto comercial desde M33.
- SD13 identifica tres sesiones de abril; SD9 identifica roles QA y actualiza su subtotal. El avance es real, aunque la imputación siga contradictoria.
- H5/H10 distinguen expediente entregado de consolidación administrativa posterior. La mera diferencia de fechas ya no se toma como prueba automática de atraso.

## 5. Cobertura por subdocumento

| Documento | Frentes contrastados | Resultado |
|---|---|---|
| SD1 CORRIGIENDO | Dotación declarada, centros, NOC/mesa/SOC, cobertura propia/compartida | No se convierte planta total en personas dedicadas al proyecto; horas de cobertura concilian. Las HH no prueban por sí solas disponibilidad nominal simultánea. |
| SD2 CORRIGIENDO | Alcance, etapas, responsabilidades y separación CLIENTE/proveedor | No se identificó una contradicción económica independiente adicional al cruce de alcance/calendario expuesto. No se certifica cada cláusula. |
| SD3 CORRIGIENDO / T-12 | Alcance y estados de requisitos, EDT y correspondencias | Diez discrepancias T12/T13, seis referencias EDT con cobertura por precisar y RT26.04 inconsistente. |
| SD4 CORRIGIENDO / T-11 / 4-W | Arquitectura, compras, regiones, ambientes, conectividad, notificaciones, impresión | Costos nuevos reconocidos; siguen pendientes alcance de nube, cobertura regional, catálogo/pagador/licencias y proveedores diferentes. |
| SD5 CORRIGIENDO | Datos, migración, retención y responsabilidad del CLIENTE | No se identificó un monto independiente adicional probado. No se certificó costo individual de cada política de retención/transferencia. |
| SD6 CORRIGIENDO / T-9 / T-10 | Hacer/comprar, metodología, terceros, orden compra/instalación/recepción | Secuencia M2 compra/M3 instalación/M4 recepción compatible. El costo de terceros independientes necesita puente; metodología no prueba nivelación diaria. |
| SD7 CORRIGIENDO / T-14/T-15/T-18 | 239 filas de asignación, 227 códigos EDT, 37 perfiles, 56 meses, aceptación y soporte | Totales HH conciliados, también sumando todas las filas por perfil; atribución temporal/perfiles de innovaciones no. PDF no equivalentes a fuentes nuevas. |
| SD8 Revision / T-16 / 8.H | 36 riesgos, reservas y no duplicación | R-036 sin importación económica; reserva propuesta no demuestra autorización, suficiencia ni caja. |
| SD9 CORRIGIENDO / T-13/T-17 | Pruebas, QA, calidad, puertas y aceptación | Diez estados inconsistentes, QA asignada a partidas sin esos perfiles, aceptación H4 no conciliada. |
| SD13 CORRIGIENDO / T-19 | Cinco innovaciones, beneficios, sesiones, madurez y calendario | Totales HH iguales pero perfiles/capacidad y aditividad no. Supuestos de cobertura/adopción no validados. |
| Anexos complementarios | Estados de observaciones y enlaces a las ramas anteriores | Marcar un frente «corregido» no acredita acta externa, nivelación ni cierre económico. Se contrastó con sus fuentes, no se usó como autoridad para declararlo cerrado. |

**SD10–12 no se presentan como auditados:** no hay rama CORRIGIENDO de ellos en el inventario y no sustentan este cruce específico de E2. No se confundió una rama antigua con una versión corregida.

## 6. Qué debe quedar conciliado antes de considerar cerrada la revisión

No se aplicó ninguno de estos cambios. Son criterios verificables para que quien corrija cierre cada frente:

1. **Una versión económica única:** resolver las decisiones del modelo y reproducirla en fuentes/PDF E2, tablas mensuales/anuales, impuestos y gráficos.
2. **Puente de alcance a costo:** cada compra y servicio tiene cantidad, configuración, pagador, proveedor/modalidad, precio integral y mes; distinguir lo ya incluido de una ampliación real.
3. **Puente de esfuerzo a capacidad:** cada HH de innovación/prueba pertenece a un paquete y perfil, cabe en el mes/día con sus otras tareas y respeta la programación/aceptación.
4. **Beneficios separados por beneficiario:** no acumular efectos solapados; usar población elegible, cobertura, adopción y valor neto demostrable o etiquetar claramente un escenario.
5. **Riesgo y liquidez distintos:** conciliar SD8 con Excel y mostrar qué demoras cubre realmente la caja/línea. No convertir reserva de HH en dinero disponible.
6. **Entrega consistente:** estados T12/T13, T14 y pruebas expresan el mismo alcance; PDF se corresponden con fuentes; validaciones/protecciones se verifican en el XLSX efectivamente entregado.

No es correcto sumar 265,33 UF, 399,20 UF, 263,62 UF, 629,65 UF y todas las HH observadas para obtener un «nuevo costo»: algunos importes son atribuciones, otros ya están incluidos y otros requieren excluir duplicaciones/definir pagador.

## 7. Archivos de la revisión

- [Conciliación de los 56 meses](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/outputs/coherencia-20261115-corte-final/conciliacion_mensual_56_meses.csv)
- [Sobrecargas de innovaciones por perfil y mes](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/outputs/coherencia-20261115-corte-final/sobrecarga_innovaciones_perfil_mes.csv)
- [Diferencias de estados T-12/T-13](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/outputs/coherencia-20261115-corte-final/diferencias_estados_T12_T13.csv)
- [Controles independientes](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/outputs/coherencia-20261115-corte-final/controles_independientes.csv)
- [Índice de observaciones](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/outputs/coherencia-20261115-corte-final/indice_hallazgos.csv)
- [Manifiesto de commits y fuentes congeladas](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/manifest.json)
- [Métricas calculadas y asignaciones únicas por código (sin desgloses repetidos)](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/metricas.json)
- [Las 239 filas T15 completas, con desgloses y ajustes](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/asignaciones_completas_T15.json)
- [Metadatos y hash del Excel](C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/tmp/coherencia-20261115-corte-final/metadatos.json)

## Integridad y estado final

El checkout de E2 quedó en **`6b55a222`**, tras el pull solicitado. SD4 quedó en `5485aaf9` en su worktree. No se corrigieron las fuentes ni el Excel, no se guardó/exportó una versión modificada, no se recompilaron PDF, ni se hicieron commits o push. Se preservaron archivos previos no rastreados. Los únicos archivos nuevos propios son el informe, CSV y evidencias separadas de auditoría.

**27 observaciones: 11 altas, 14 medias y 2 bajas.** El número cuenta causas documentadas, no 27 incrementos independientes del presupuesto.

## Key Learnings:

1. La coincidencia de HH totales no acredita la atribución por paquete, perfil, mes y sesión, ni la disponibilidad después de otras tareas.
2. Una revisión debe congelar Excel, commit y PDF concreto y retirar hallazgos ya resueltos: en este corte sí se incorporaron controladores, Fargate productivo y sesiones M15.
