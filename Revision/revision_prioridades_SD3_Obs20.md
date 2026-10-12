# LafroX — Obs. 20: prioridades revisables e impacto documental

## Resultado y alcance

**Sí se pueden reducir prioridades.** No son cifras intocables ni todas vienen fijadas por las Bases. La propuesta distingue 10 cambios recomendados y 5 adicionales condicionados; no se ha aplicado ninguno. La razón para no cambiar al azar es conservar una justificación defendible y las dependencias que el propio proyecto creó, especialmente la fórmula de casos de prueba.

Revisados los 262 IDs únicos del catálogo activo (176 RF y 86 RNF), sus descripciones y prioridades; las familias y etapas del SD2; el criterio del Caso, §§13.1, 13.2, 17.1 y resultados del capítulo 18; y referencias/priorización en los documentos Markdown disponibles SD4–SD9, SD13, T-10, T-12, T-14, T-15, T-17 y resúmenes. SD9 vigente: carpeta v_nueva según el contexto; v_vieja se distingue como histórico. El inventario al final cubre todos los IDs; «sin propuesta de cambio» no afirma que cada prioridad restante sea intocable ni que haya sido validada por el CLIENTE.

Sólo análisis. No se modifican catálogo, originales de Requerimientos, subdocumentos, formularios, LaTeX ni PDF. La Obs. 20 permanece Parcial hasta decidir, aplicar y sincronizar una solución. No se deduce aprobación del CLIENTE de esta revisión.

## 1. Qué permite la fuente contractual

- El Caso §13.1 establece preferencia: primero trazabilidad y frío, luego preventa y entrega; rutas y costo de servir se consideran valiosos pero menos urgentes. También reconoce la jubilación del planificador y exige que el proponente fundamente su orden por dependencias, riesgo, adopción y cronograma. No asigna una etiqueta Crítica/Alta/Media a cada ID atómico del catálogo.
- El Caso §17.1 exige que el catálogo funcional declare prioridad y origen; exige ingeniería propia, no copiar una clasificación sin análisis.
- El SD2 asigna prioridades a 14 familias. Una familia crítica no hace críticos todos sus detalles. El propio SD3 define la prioridad de familia como techo; bajar un detalle por debajo de ese techo no obliga a bajar la familia entera.
- Los tres requisitos de costo de servir señalados están vinculados tanto a F-14 (Media) como a una familia operacional de mayor prioridad. La regla actual no explica cómo resuelve esa doble pertenencia. No se declara una infracción automática: se recomienda decidir por la función específica del requisito, no por la etiqueta más alta de cualquiera de sus relaciones.
- Los consolidados originales conservan sus vacíos y valores históricos. La oferta puede justificar su clasificación detallada en SD3 sin reescribir el material de origen; una modificación de originales requeriría alcance específico.

### Cuatro conceptos que no se deben mezclar

| Concepto | Qué se conserva al bajar una prioridad |
|---|---|
| Obligación/alcance | El requisito continúa ofertado, implementado y verificado; Media no significa opcional ni No cumple. |
| Etapa/hito | No se cambia E1/E2 ni el hito externo; no se aplaza una función fuera de su compromiso. |
| Riesgo/severidad | No se rebaja la severidad de un defecto, un incidente, una vulnerabilidad ni la criticidad de un servicio/SLA. |
| Prioridad de desarrollo | Sí se puede distinguir un control indispensable de una ayuda de consulta, presentación u optimización. |

Criterio recomendado: Crítica para evitar interrupción irreversible de la operación esencial, pérdida/duplicación de datos clave, riesgo sanitario, incumplimiento de protección esencial o hito rector; Alta para flujos importantes y dependencias de cierre; Media para consultas, presentaciones y optimizaciones complementarias. El hecho de estar exigido no basta por sí solo para llamar Alta a toda mejora de interfaz. Tampoco basta estar en E2 para llamarla Media: EDI y el hito de enero de 2029 siguen protegidos.

## 2. Diez reducciones recomendadas

| ID | Capacidad | Actual | Propuesta | Justificación y protección que permanece |
|---|---|---|---|---|
| RF-04.08 | Costo de cada entrega | Alta | Media | Su función pertenece al costo de servir de F-14 (Media, E2), no a la secuenciación indispensable de rutas de E1. Mantener el resultado R18-11 y todos los costos exigidos. |
| RF-08.07 | Costo de devoluciones y mermas | Alta | Media | Es una entrada del cálculo RF-11.02, ya Media; no es el registro o disposición sanitaria de una devolución. Mantener esas funciones y el resultado R18-11. |
| RF-14.04 | Telemetría para costo de servir | Crítica | Media | El uso analítico de kilómetros/tiempos en E2 no debe heredar automáticamente la criticidad del control térmico. Mantener sensores, alertas y bloqueo térmico con sus prioridades actuales. |
| RF-02.03 | Slotting ABC | Alta | Media | Recomendación periódica de optimización sobre posiciones ya válidas, con aprobación de Bodega. No altera FEFO, compatibilidad térmica, stock ni picking. |
| RF-02.07 | Reporte de ocupación de bodega | Alta | Media | Consulta, historia y exportación para gestión; no es el bloqueo de capacidad ni el indicador de ocupación de camiones R18-14. El inventario fuente permanece protegido. |
| RF-03.06 | Historial de compras | Alta | Media | Apoyo comercial al preventista, separado de disponibilidad de stock, crédito, confirmación e integridad del pedido. |
| RF-03.14 | Sugerencias de productos | Alta | Media | Recomendación comercial derivada del historial y promociones; no es necesaria para registrar un pedido correcto ni controlar el crédito. |
| RF-07.07 | Cartola descargable en portal | Alta | Media | Autoservicio E2, comparable al saldo/estado de cuenta RF-12.18 ya Media. No se rebajan liquidación diaria, registro de efectivo ni autorización/conciliación bancaria. |
| RF-14.02 | Mapa comparativo de rutas | Alta | Media | Vista de comparación para análisis y optimización futura. No es la captura de telemetría, identificación del conductor ni la reacción a una alerta de accidente/robo. |
| RNF-03.03 | Latencia de consulta de historial | Alta | Media | Misma urgencia de negocio que el historial RF-03.06. Se mantiene el límite de 2 segundos y la prueba de desempeño; no se cambia la latencia de stock/crédito ni toma del pedido. |

RF-04.08, RF-08.07 y RF-14.04 merecen prioridad en la corrección: el producto analítico que alimentan, RF-11.02, ya tiene prioridad Media. No se elimina R18-11 ni se mueve la Etapa 2. Para RF-07.07, la coincidencia de contenido con RF-12.18 sirve para comparar urgencia, no para fusionar o eliminar IDs.

## 3. Cinco reducciones adicionales, condicionadas

| ID | Capacidad | Actual | Propuesta posible | Condición para aceptarla |
|---|---|---|---|---|
| RF-03.07 | Promociones | Alta | Media | Sólo si se clasifica como apoyo comercial y no como una regla que condiciona la confirmación/precio del pedido. Mantener pruebas de cálculo de descuentos, autorizaciones y exactitud financiera. |
| RF-07.04 | Gestión de cartera y recontactos | Alta | Media | Separar la bitácora/CRM de cobranza de los controles de mora, cupo y rendición que siguen protegidos. Confirmar con Finanzas que el flujo no sea condición de cierre de caja. |
| RF-08.04 | Aviso por saldo alto de envases | Alta | Media | Complemento de recuperación, no la cuenta corriente ni el registro de retornos. Confirmar su aporte al resultado de reducción de pérdidas R18-12; mantener la alerta en 24 horas. |
| RF-17.11 | Búsqueda global | Alta | Media | Prioridad funcional secundaria respecto de las consultas operacionales especializadas. Mantener acceso limitado por rol, pruebas de acceso indebido y límite de 2 segundos; no rebajar el riesgo de seguridad por cambiar la urgencia de negocio. |
| RF-17.12 | Funciones de listados y exportación | Alta | Media | Ordenación/filtrado genéricos pueden ser secundarios, siempre que se mantengan exportación fiel al filtro, integridad, autorización y auditoría, sin interrumpir consultas esenciales. |

No se recomienda meter estas cinco en el mismo paquete sin revisar las condiciones. Para requisitos amplios, bajar su prioridad de desarrollo no prueba que deba bajar su intensidad de pruebas. La cantidad real de casos debe seguir cubriendo todas las condiciones, incluso si excede el mínimo aritmético del plan.

## 4. Qué no conviene bajar para cambiar el porcentaje

Mantener las prioridades actuales, en esta propuesta, de lote y vencimiento, trazabilidad hacia delante/atrás, frío y bloqueo sanitario, integridad de sincronización, stock/crédito de preventa, POD, efectivo/conciliación, FEFO, permisos/cifrado/sesiones, continuidad/DR y SLA, EDI/acuse/ventana comercial y capacitación condicionante de aceptación. Mantener también los indicadores ligados directamente a resultados de aceptación: RF-11.03 OTIF, RF-11.04 fill rate, RF-11.05 ocupación de camiones y RF-11.07 cierre comercial. RF-02.07 mide ocupación de bodega: no es la misma función que RF-11.05.

RF-14.03 se mantiene Alta: su texto contempla reacción del centro de control ante desvíos y ejemplos de accidente/robo; no se propone rebajarla por parecerse al mapa analítico RF-14.02. El control de pérdidas de envases RF-08.06 se mantiene Alta por su relación con R18-12; se distingue del aviso auxiliar RF-08.04 condicionado.

No es necesario lograr una proporción artificial 50/50. La observación exige discriminación razonada; el porcentaje por sí solo no demuestra ni refuta la priorización. Aun aplicando 15 cambios, casi 78 % seguiría en Crítica/Alta: no vender ese escenario como desaparición matemática de la concentración.

## 5. Repercusiones comprobadas

| Documento | Repercusión de cambiar prioridades | Acción necesaria / no necesaria |
|---|---|---|
| SD3 cuerpo §3.2.3 y Anexos 3.A/3.B | Valores por ID; explicación de la escala y totales 56/163/43. | Actualizar las filas elegidas, regla para detalles/doble familia y resumen; conservar ID, descripción, precondición, resultado, etapa y origen. |
| SD2 Anexo 2.1 | Familias F-01–F-14 son techo y contexto de urgencia. | No cambiar familias ni sus etapas para estos 10 cambios; justificar por qué un detalle es menos urgente que la familia. |
| T-12 | Tiene seis columnas, ninguna de prioridad. | No añadir columnas, no cambiar Cumple ni paquetes EDT. Verificar las remisiones; las 645 filas permanecen. |
| SD4/T-11 | Referencias a capacidades, permisos, servicios y SLAs. | No cambia arquitectura, dimensionamiento, hardware o criticidad de servicio por una etiqueta de prioridad funcional. |
| SD5 | Modelo, reglas y datos de los mismos IDs. | No cambia esquema de datos ni regla de negocio si no se cambia la función. |
| SD6/T-10 | Prioridades guían las iteraciones de Construcción (T-10, párrafo de iteraciones). | Revisar el backlog, no la metodología ni sus fases; no mover compromisos de etapa. |
| SD7/T-14/T-15 | Paquetes y esfuerzo programado para alcance completo. | No cambian los 222 paquetes, sus fechas, la Gantt ni HH por cambiar sólo prioridad. Conservar la capacidad de pruebas como margen; no inferir ahorro de dotación de una regla aritmética de casos. |
| SD8 | Prioridad/severidad del riesgo no es prioridad del requisito. | No modificar matriz de riesgos o reservas automáticamente; sólo si se alterase exposición o respuesta. |
| SD9 cuerpo §9.2.3 y estrategia | Declara 56/163/43, total 1.316, automatización, duración y HH manuales. | Recalcular si se mantiene el vínculo de casos a prioridad; o separar explícitamente prioridad de desarrollo e intensidad por riesgo para conservar las pruebas. |
| T-13 §§8.2/8.3 | Regla directa: Crítica=5, Alta=3, Media=2 casos por requisito. | Tabla de dimensionamiento y regresión deben concordar. No dejar las cifras anteriores describiendo nuevas prioridades. |
| SD9 Anexo 9.C.2 | Usa 263 casos manuales, 65,8 HH, costos de fallas 93,8/109,8 HH. | Recalcular escenarios de retrabajo si se reduce el catálogo aritmético; no cambiar las 11.136 HH programadas de conformidad por defecto. |
| T-17 | Aceptación exige pruebas aplicables aprobadas, sin defectos críticos/altos abiertos. | No rebajar puertas ni resultados del caso. Remisiones al T-13 permanecen; prioridad Media no exonera aceptación. |
| SD13 | INN-02 reutiliza escenarios de pruebas/regresión y hechos operacionales. | Mantener interfaces y obligaciones; comprobar consistencia con el T-13 si se modifica el diseño de casos. No se encontró un total numérico de casos que requiera reemplazo directo allí. |
| Resúmenes y trazabilidad | Explican catálogo y estado de Obs. 20. | Sincronizar explicación y balance cuando la corrección esté aplicada, no ahora. |
| LaTeX/PDF | Son publicaciones del contenido, no fuentes de una prioridad diferente. | Después de autorización, sincronizar SD3 y documentos de calidad afectados en sus checkouts autorizados; aquí sólo .md. No se revisó ni editó LaTeX en esta tarea. |
| v_vieja del SD9 | Contiene las cifras antiguas y una matriz detallada histórica. | No sobrescribir para simular actualización; diferenciar versión histórica y vigente. |

### Dimensión de las pruebas: una consecuencia real, no hipotética

Se mantienen en los escenarios los 356 RT y 15 integraciones (7 casos por integración) del T-13 vigente. Cotejo con el T-12 actual: 343 RT «Cumple» + 13 «Cumple parcialmente» = 356; otros 18 RT dicen «No cumple». Fórmula: N = 5C + 3A + 2M + 356 + 15×7. Las 262 prioridades siguen correspondiendo a 262 requisitos, no a las 271 filas RF/RNF del T-12 (incluyen nueve absorbidas).

| Magnitud | Vigente | Sólo 10 recomendadas | Con las 5 condicionadas |
|---|---:|---:|---:|
| Crítica | 56 | 55 | 55 |
| Alta | 163 | 154 | 149 |
| Media | 43 | 53 | 58 |
| Crítica + Alta | 219 (83,6 %) | 209 (79,8 %) | 204 (77,9 %) |
| Casos RF/RNF | 855 | 843 | 838 |
| Casos totales | 1316 | 1304 | 1299 |
| Automáticos (80 %, redondeados) | 1053 | 1043 | 1039 |
| Manuales (resto exacto) | 263 | 261 | 260 |
| Regresión, un ejecutor, horas | 8,775 | 8,692 | 8,658 |
| Regresión, dos ejecutores, horas | 4,388 | 4,346 | 4,329 |
| Ejecución manual, HH/ciclo | 65,75 | 65,25 | 65,00 |
| Falla interna, HH/evento sin redondear | 93,75 | 93,25 | 93,00 |
| Falla externa, HH/evento sin redondear | 109,75 | 109,25 | 109,00 |

Los escenarios se calcularon con Node a partir de las filas actuales y el conjunto explícito de IDs propuestos. Redondear sólo para presentación. Los tiempos son supuestos del plan (30 s automático y 15 min manual), no mediciones ni ahorro garantizado. El escenario principal reduce 12 casos estimados; no libera automáticamente personal o HH de T-15. Se conserva todo el alcance y su aceptación.

**Alternativa sin reducción de pruebas:** repriorizar el desarrollo pero mantener el catálogo de casos, explicando en T-13/SD9 que la intensidad se establece por riesgo de fallo y cobertura, no por la nueva prioridad comercial. Las etiquetas deben dejar de describir directamente las clases de riesgo en la fórmula; mantener 1.316 sin aclarar esa separación sería inconsistente. Esta alternativa tampoco está aplicada.

## 6. Propuesta de ejecución, pendiente de autorización

1. Aprobar los 10 cambios principales; resolver separadamente las cinco condiciones, sin perseguir una cuota de prioridad.
2. Actualizar SD3 y explicación de priorización, sin tocar originales o alcance.
3. Elegir mantener la fórmula actual y recalcular los números de T-13/SD9, o conservar la cobertura existente mediante una clasificación de riesgo explícita. No bajar seguridad, privacidad ni aceptación.
4. Mantener Gantt, paquetes, fechas, HH, hitos y pruebas especializadas contractuales. Comprobar sólo impactos reales, no reemplazar toda coincidencia de palabras Alta/Crítica en otros documentos.
5. Sincronizar los entregables afectados con sus publicaciones LaTeX/PDF bajo alcance explícito y actualizar Obs. 20 sólo tras verificar la propagación.

## 7. Evidencia, versiones y límites

- Caso §13.1 y §17.1: criterio profesional de priorización y campos del catálogo; §13.2 y capítulo 18: hitos y resultados que se preservan.
- SD2 Anexo 2.1: F-14 Media; F-12 Media; F-06 Alta; F-07 y F-08 Crítica.
- SD3 Anexos 3.A/3.B y Tabla 3.A.2: inventario, prioridades y correspondencia a múltiples familias.
- T-13 v_nueva §§8.2/8.3: cinco/tres/dos casos, 1.316 total y modelo de duración.
- SD9 v_nueva §9.2.3 y Anexo 9.C.2: dependencia explícita y retrabajo.
- T-10: priorización en iteraciones. T-17: condiciones de aceptación no exentas por Media.
- Revisadas todas las filas vigentes del catálogo; no se realizó una nueva auditoría integral de cada arquitectura ni de todas las citas del proyecto. No se verificaron fórmulas de los Excel ni contenido de PDFs/otras ramas en esta tarea. Si se utilizan como entregables activos, necesitan su propia sincronización posterior.

### Hashes del corte leído (SHA-256)

| Archivo | SHA-256 |
|---|---|
| Bases/Caso_02_Logistica.md | 2a1ed88f764873d200b75e05bb4eed72f7e145bf46f4a545ee0619b1c7b76b88 |
| 02_problema_necesidad/LAFROX-Subdocumento2-Anexos.md | 27bf374d1e19a7f0075ac2ecf229bb67a4366069a6ab8c5f0777bd7d897a818b |
| 03_esquema_solucion_alcance/LAFROX-Subdocumento3.md | 6d474ce5bfe996f1d4872b1e7e91b6f4a22ed8d918b27a8200e5bcecf3cb80fa |
| 03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md | a8cf971eaf0f30f3a4960c205c158236284c18d87dabe36810d3f626e7a9e0ef |
| 03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md | d59de3f3e9ecb87e89edf184063d307a30fe0f80bfb11648b97d406af8b39597 |
| 09_plan_calidad/v_nueva/LAFROX-Formulario-T-13.md | fafa51a79e10cb394eb6ff3ad4036290bde732ec1db8d8f6a00bebeee46596fb |
| 09_plan_calidad/v_nueva/LAFROX-Subdocumento9.md | 583de290cf18ffbfdd4372086ad229209e6b609fd3967eba0477f2bfa0e3318e |
| 09_plan_calidad/v_nueva/LAFROX-Subdocumento9-Anexos.md | 9c3117bc7e63066fa70da79b56e2473baec6a2557de4034bce0effda0fc80c83 |
| 09_plan_calidad/v_nueva/LAFROX-Formulario-T-17.md | 03669690ae704689e48a9ab780afee962afe557f5498b203a335b35b4648931d |

## 8. Inventario completo del corte: 262 IDs únicos

P = cambio principal recomendado; C = cambio condicionado; — = sin propuesta de cambio en este análisis. «Propuesta» no sustituye la prioridad vigente. Los textos breves son extractos para localizar la fila; el catálogo conserva la descripción y sus criterios íntegros.

| ID | Vigente | Etapa | Propuesta principal | Marca | Capacidad (extracto) |
|---|---|---|---|---|---|
| RF-01.01 | Crítica | E1 | Crítica | — | El sistema debe registrar la recepción física de un proveedor validando las cantidades recibidas por SKU … |
| RF-01.02 | Crítica | E1 | Crítica | — | El sistema debe exigir el número de lote del proveedor en campo estructurado para todo SKU con trazabilid… |
| RF-01.03 | Crítica | E1 | Crítica | — | El sistema debe registrar la fecha de vencimiento en formato DD/MM/AAAA para todo SKU con control de venc… |
| RF-01.04 | Alta | E1 | Alta | — | El sistema debe permitir registrar una no conformidad durante la recepción seleccionando su tipo desde un… |
| RF-01.05 | Alta | E1 | Alta | — | Al confirmar una no conformidad, el sistema debe cambiar automáticamente a estado ‘Cuarentena’ la cantida… |
| RF-01.06 | Alta | E1 | Alta | — | El sistema debe decodificar códigos de barras GS1 interpretando los AIs 01 (GTIN), 10 (lote), 17 (vencimi… |
| RF-01.07 | Media | E1 | Media | — | Al finalizar el registro de un pallet, el sistema debe generar automáticamente un SSCC bajo estándar GS1-… |
| RF-01.08 | Media | E1 | Media | — | El sistema debe permitir asociar un SSCC a una dirección de almacenamiento (pasillo-columna-nivel) escane… |
| RF-01.09 | Crítica | E1 | Crítica | — | Al cerrar una recepción, el sistema debe enviar automáticamente la transacción de ingreso de inventario a… |
| RF-01.10 | Crítica | E1 | Crítica | — | El sistema debe permitir crear y mantener fichas de producto con atributos obligatorios: descripción, for… |
| RF-01.11 | Crítica | E1 | Crítica | — | El sistema debe validar la compatibilidad térmica entre el tipo de almacenamiento del SKU y la zona de te… |
| RF-02.01 | Alta | E1 | Alta | — | El sistema debe permitir registrar y configurar cada instalación de la red logística (centros de distribu… |
| RF-02.02 | Alta | E1 | Alta | — | El sistema debe consolidar el stock físico en unidades de cada SKU en todos los nodos de la red logística… |
| RF-02.03 | Alta | E1 | Media | P | El sistema debe calcular periódicamente una propuesta de reasignación de ubicaciones (slotting) basada en… |
| RF-02.04 | Alta | E1 | Alta | — | El sistema debe generar un plan de conteo cíclico mensual que cubra una cantidad de posiciones definidas,… |
| RF-02.05 | Alta | E1 | Alta | — | El sistema debe calcular el stock disponible para venta por SKU y por centro de distribución, definido co… |
| RF-02.06 | Media | E1 | Media | — | El sistema debe registrar como «en tránsito» todo inventario despachado desde un nodo de origen hacia un … |
| RF-02.07 | Alta | E1 | Media | P | El sistema debe permitir consultar el nivel de ocupación de cada centro de distribución, desglosado por z… |
| RF-02.08 | Alta | E1 | Alta | — | El sistema debe dirigir la preparación de pedidos (picking) asignando tareas de recolección al dispositiv… |
| RF-02.09 | Alta | E1 | Alta | — | El sistema debe gestionar el almacenamiento de productos con fecha de vencimiento aplicando la regla FEFO… |
| RF-02.10 | Alta | E1 | Alta | — | El sistema debe proveer una interfaz de trazabilidad que permita buscar y detallar el ciclo de vida compl… |
| RF-03.01 | Crítica | E1 | Crítica | — | La app debe mostrar, con conectividad, el stock disponible en tiempo real para cada SKU al tomar el pedid… |
| RF-03.02 | Crítica | E1 | Crítica | — | La app debe mostrar, sin conectividad, el stock según la última sincronización válida, con su antigüedad … |
| RF-03.03 | Alta | E1 | Alta | — | El sistema debe reservar el stock comprometido en el momento de la confirmación del pedido en el servidor… |
| RF-03.04 | Crítica | E1 | Crítica | — | La app debe mostrar, con conectividad, el crédito disponible y la deuda vencida del cliente al tomar el p… |
| RF-03.05 | Crítica | E1 | Crítica | — | La app debe mostrar, sin conectividad, el crédito y la deuda según la última sincronización válida, con s… |
| RF-03.06 | Alta | E1 | Media | P | La app debe mostrar el historial de compra del cliente (productos y frecuencia). |
| RF-03.07 | Alta | E1 | Alta | C | La app debe permitir aplicar una promoción vigente (3x2, descuento por volumen) a una línea de pedido, ca… |
| RF-03.08 | Crítica | E1 | Crítica | — | El sistema debe alertar al preventista cuando el pedido, sumado a la deuda vencida, supere el límite de c… |
| RF-03.09 | Crítica | E1 | Crítica | — | El sistema debe bloquear el envío del pedido cuando este, sumado a la deuda vencida, supere el límite de … |
| RF-03.10 | Alta | E1 | Alta | — | El sistema debe permitir que un supervisor autorice, de forma registrada, el envío de un pedido bloqueado… |
| RF-03.11 | Media | E1 | Media | — | El sistema debe registrar y conservar en cada pedido de preventa el precio acordado por el preventista al… |
| RF-03.12 | Media | E1 | Media | — | El sistema debe generar una alerta al responsable comercial cuando el importe calculado para el despacho … |
| RF-03.13 | Crítica | E1 | Crítica | — | El sistema debe informar al preventista la fecha y ventana horaria de entrega que puede comprometer, cons… |
| RF-03.14 | Alta | E1 | Media | P | El sistema debe generar sugerencias de productos usando historial de compra, frecuencia, productos habitu… |
| RF-03.15 | Crítica | E1 | Crítica | — | La app debe generar un identificador único en el dispositivo al crear un pedido sin conectividad. |
| RF-03.16 | Crítica | E1 | Crítica | — | El sistema debe detectar y descartar automáticamente los reenvíos duplicados de un pedido con el mismo id… |
| RF-04.01 | Alta | E1 | Alta | — | El sistema debe asignar pedidos a la flota, secuenciando la ruta en función de la capacidad volumétrica y… |
| RF-04.02 | Media | E1 | Media | — | El sistema debe permitir modificar manualmente la secuencia de ruta y reasignar pedidos entre vehículos |
| RF-04.03 | Alta | E1 | Alta | — | El sistema debe bloquear la adición de líneas de pedido a una ruta si la sumatoria excede los límites de … |
| RF-04.04 | Alta | E1 | Alta | — | El sistema debe permitir la configuración de ventanas horarias específicas por cliente y ajustar la secue… |
| RF-04.05 | Alta | E1 | Alta | — | El sistema debe restringir la asignación de pedidos refrigerados o congelados exclusivamente a vehículos … |
| RF-04.06 | Media | E1 | Media | — | El sistema debe crear un aviso al contacto del cliente con la hora estimada de llegada incluyendo una ven… |
| RF-04.07 | Alta | E1 | Alta | — | El sistema debe permitir parametrizar franjas horarias de recepción en la ficha maestra de cada cliente (… |
| RF-04.08 | Alta | E2 | Media | P | El sistema debe calcular el costo de cada entrega tras haber sido realizada. |
| RF-05.01 | Alta | E1 | Alta | — | El jefe de bodega debe poder iniciar la generación manualmente o configurar la generación automática al c… |
| RF-05.02 | Alta | E1 | Alta | — | El sistema debe exigir la validación de cada línea recolectada escaneando el código GS1. El escaneo debe … |
| RF-05.03 | Alta | E1 | Alta | — | El sistema debe exigir la selección obligatoria de un motivo parametrizable de una lista estructurada, ca… |
| RF-05.04 | Alta | E1 | Alta | — | El sistema debe secuenciar las líneas de la misión de preparación priorizando las zonas en el siguiente o… |
| RF-05.05 | Alta | E1 | Alta | — | El sistema debe asignar el inventario para la preparación de pedidos aplicando estrictamente la regla lóg… |
| RF-05.06 | Alta | E1 | Alta | — | El sistema debe enviar al ERP, al cerrar una misión de preparación, el detalle consolidado por cada línea… |
| RF-05.07 | Alta | E1 | Alta | — | El sistema debe dirigir la carga de pedidos preparados en el camión siguiendo la secuencia inversa de la … |
| RF-06.01 | Alta | E1 | Alta | — | El sistema debe permitir marcar la recepción conforme de bultos mediante validación por línea de pedido i… |
| RF-06.02 | Crítica | E1 | Crítica | — | El sistema debe permitir capturar la firma digital del receptor como evidencia de entrega, asociada a la … |
| RF-06.03 | Media | E1 | Media | — | El sistema debe permitir reportar un rechazo total o parcial seleccionando la cantidad y el motivo desde … |
| RF-06.04 | Media | E1 | Media | — | El sistema debe permitir reportar un local cerrado, indicando la dirección del cliente. |
| RF-06.05 | Crítica | E1 | Crítica | — | El sistema debe permitir digitar el monto exacto recaudado en pagos realizados en efectivo |
| RF-06.07 | Crítica | E1 | Crítica | — | El sistema debe sincronizarse automaticamente, al detectar la reconexión de señal o el regreso al centro … |
| RF-06.08 | Alta | E1 | Alta | — | El sistema debe permitir al conductor de una empresa externa iniciar su jornada usando las credenciales t… |
| RF-06.09 | Alta | E1 | Alta | — | Al registrar una entrega, el sistema debe permitir al conductor capturar la cantidad de canastillos y pal… |
| RF-06.10 | Alta | E1 | Alta | — | El sistema debe actualizar el saldo del cliente y del parque retornable en línea o en modo diferido según… |
| RF-06.11 | Media | E1 | Media | — | El sistema debe ofrecer al cliente la opción de confirmar la recepción mediante un código QR único genera… |
| RF-06.12 | Media | E1 | Media | — | El sistema debe permitir confirmar la recepción del cliente aun si este no dispone de teléfono o conectiv… |
| RF-06.13 | Media | E1 | Media | — | La app de reparto debe permitir imprimir en terreno un comprobante térmico de entrega para el cliente usa… |
| RF-07.02 | Alta | E1 | Alta | — | El sistema debe generar la planilla digital de rendición individual al retorno del camión, contrastando l… |
| RF-07.03 | Alta | E1 | Alta | — | El sistema debe obligar al registro estructurado y categorizado de causales para cualquier diferencia det… |
| RF-07.04 | Alta | E1 | Alta | C | El sistema debe proveer una consola de gestión para la cartera de crédito a 30 días sincronizada con el E… |
| RF-07.05 | Alta | E1 | Alta | — | El sistema debe notificar en la aplicación móvil de preventa el estado de bloqueo o mora de un cliente (>… |
| RF-07.06 | Alta | E1 | Alta | — | El sistema debe integrarse vía Bluetooth con terminales de pago portátil (POS) en la aplicación móvil de … |
| RF-07.07 | Alta | E2 | Media | P | El sistema debe disponer en el portal web de autoatención el estado de cuenta y la cartola de antigüedad … |
| RF-07.08 | Alta | E2 | Alta | — | El sistema debe proveer una bandeja de validación para pagos reportados en el portal web de clientes, per… |
| RF-07.09 | Alta | E1 | Alta | — | El sistema debe transferir de forma estructurada, asíncrona e idempotente los comprobantes de recaudación… |
| RF-07.10 | Alta | E1 | Alta | — | El sistema debe permitir el registro de anticipos o pagos parciales en entregas al contado desde la aplic… |
| RF-07.11 | Alta | E1 | Alta | — | El sistema debe permitir al preventista registrar la cobranza en efectivo de facturas vencidas en el loca… |
| RF-08.01 | Crítica | E1 | Crítica | — | El sistema debe permitir al conductor registrar la devolución de productos en el momento de la entrega, c… |
| RF-08.02 | Crítica | E1 | Crítica | — | Al recepcionar una devolución en el andén del CD, el sistema debe permitir seleccionar el destino final d… |
| RF-08.03 | Alta | E1 | Alta | — | El sistema debe mantener una cuenta corriente de envases retornables por cliente, actualizando el saldo e… |
| RF-08.04 | Alta | E1 | Alta | C | El sistema debe generar una alerta al preventista cuando el saldo de envases retornables de un cliente su… |
| RF-08.05 | Alta | E1 | Alta | — | El sistema debe permitir registrar mermas por vencimiento detectadas en conteo cíclico, preparación de pe… |
| RF-08.06 | Alta | E1 | Alta | — | El sistema debe reportar la pérdida de envases retornables desglosada por cliente, tipo de envase y zona,… |
| RF-08.07 | Alta | E2 | Media | P | El sistema debe incluir el costo de devoluciones y mermas por cliente como componente del cálculo del cos… |
| RF-09.01 | Crítica | E1 | Crítica | — | El sistema debe permitir la trazabilidad 'hacia adelante' (forward tracing): dado un lote específico, deb… |
| RF-09.02 | Crítica | E1 | Crítica | — | El sistema debe permitir la trazabilidad 'hacia atrás' (backward tracing): dado un producto en el local d… |
| RF-09.03 | Crítica | E1 | Crítica | — | El sistema debe registrar de forma automática y continua la temperatura de las cámaras de refrigerado y c… |
| RF-09.04 | Crítica | E1 | Crítica | — | El sistema debe registrar de forma automática y continua la temperatura en los camiones con equipo de frí… |
| RF-09.05 | Crítica | E1 | Crítica | — | El sistema debe generar una alerta en tiempo real (notificación en cabina y en plataforma de monitoreo) c… |
| RF-09.06 | Media | E1 | Media | — | Ante una excursión térmica crítica y sostenida, el sistema debe bloquear preventivamente el despacho del … |
| RF-09.07 | Crítica | E1 | Crítica | — | El sistema debe permitir al conductor registrar el rechazo de un producto entregado por 'sospecha de rupt… |
| RF-09.08 | Crítica | E1 | Crítica | — | El sistema debe registrar, en el momento de la preparación (picking), el lote específico que se le asigna… |
| RF-09.09 | Crítica | E1 | Crítica | — | El sistema debe generar la evidencia de cumplimiento de cadena de frío exigible ante la autoridad sanitar… |
| RF-11.01 | Media | E2 | Media | — | El sistema debe programar y distribuir vía correo electrónico reportes ejecutivos consolidados (en format… |
| RF-11.02 | Media | E2 | Media | — | El sistema debe calcular el Costo de Servir real por entrega y por cliente, imputando los costos directos… |
| RF-11.03 | Alta | E1 | Alta | — | El sistema debe calcular diariamente el indicador OTIF por cliente, ruta, zona y total consolidado, defin… |
| RF-11.04 | Alta | E1 | Alta | — | El sistema debe calcular automáticamente el Fill Rate (unidades entregadas vs. pedidas) y el índice de Pe… |
| RF-11.05 | Alta | E1 | Alta | — | El sistema debe calcular diariamente la utilización de capacidad volumétrica (m^3) y de peso (kg) por via… |
| RF-11.06 | Alta | E1 | Alta | — | El sistema debe proveer un Tablero de Control Operacional en tiempo real que consolide el avance de rutas… |
| RF-11.07 | Alta | E1 | Alta | — | El sistema debe procesar automáticamente la liquidación y cierre comercial individual por camión al retor… |
| RF-11.08 | Media | E2 | Media | — | El sistema debe segmentar mensualmente la cartera de clientes en matrices de rentabilidad neta (margen co… |
| RF-12.01 | Alta | E2 | Alta | — | El sistema debe recibir el mensaje de pedido electrónico estructurado (EDI/EDIFACT/XML, según el estándar… |
| RF-12.02 | Alta | E2 | Alta | — | El sistema debe validar automáticamente el pedido EDI recibido, verificando estructura del mensaje, exist… |
| RF-12.03 | Alta | E2 | Alta | — | El sistema debe resolver el código de producto informado por la cadena contra el maestro de productos vig… |
| RF-12.04 | Alta | E2 | Alta | — | El sistema debe registrar automáticamente, sin digitación manual, el pedido EDI válido (RF-12.02, RF-12.0… |
| RF-12.05 | Alta | E2 | Alta | — | El sistema debe poner a disposición del proceso de planificación de rutas todo pedido registrado provenie… |
| RF-12.06 | Alta | E2 | Alta | — | El sistema debe permitir gestionar, mediante una bandeja de excepciones, los pedidos que no pasaron la va… |
| RF-12.07 | Alta | E2 | Alta | — | El sistema debe enviar a la cadena de origen una confirmación o rechazo del pedido, indicando la causa cu… |
| RF-12.08 | Alta | E2 | Alta | — | El sistema debe mantener el historial de estados de cada pedido electrónico (recepción, validación, confi… |
| RF-12.09 | Alta | E2 | Alta | — | El sistema debe generar y enviar al cliente del canal moderno un ASN cuando su pedido queda cargado en el… |
| RF-12.10 | Alta | E2 | Alta | — | El sistema debe planificar la llegada del camión al cliente del canal moderno dentro de la ventana horari… |
| RF-12.11 | Alta | E2 | Alta | — | El sistema debe registrar el cumplimiento o incumplimiento de la ventana de 30 minutos para cada entrega … |
| RF-12.12 | Alta | E2 | Alta | — | El sistema debe capturar evidencia de entrega en el local del cliente: firma en pantalla del titular cuan… |
| RF-12.13 | Alta | E2 | Alta | — | El sistema debe enviar al cliente del canal moderno un acuse de recibo digital de la entrega, articulado … |
| RF-12.14 | Media | E2 | Media | — | El sistema debe publicar un portal web público, sin autenticación, con el catálogo vigente de productos (… |
| RF-12.15 | Media | E2 | Media | — | El portal autenticado de clientes debe permitir generar un pedido en autoservicio, validando el mismo cré… |
| RF-12.16 | Media | E2 | Media | — | El portal de clientes debe permitir consultar el estado de sus entregas y la ventana de entrega compromet… |
| RF-12.17 | Media | E2 | Media | — | El portal de clientes debe permitir consultar y descargar sus documentos tributarios (factura, guía elect… |
| RF-12.18 | Media | E2 | Media | — | El portal de clientes debe permitir consultar el saldo y estado de cuenta del cliente autenticado, con da… |
| RF-12.19 | Media | E2 | Media | — | El portal de transportistas debe permitir consultar las rutas asignadas a la empresa para el día siguient… |
| RF-12.20 | Media | E2 | Media | — | El portal de transportistas debe permitir descargar la documentación de despacho de cada ruta asignada. |
| RF-12.21 | Media | E2 | Media | — | El portal debe permitir confirmar, antes de la ventana de despacho, qué conductor y vehículo ejecutarán c… |
| RF-12.22 | Media | E2 | Media | — | El portal de proveedores debe permitir consultar, en modo de solo lectura, el estado de sus órdenes de co… |
| RF-12.23 | Media | E2 | Media | — | El portal de proveedores debe permitir consultar, en modo de solo lectura, las recepciones registradas pa… |
| RF-12.24 | Media | E2 | Media | — | El portal de proveedores debe permitir consultar, en modo de solo lectura, sus devoluciones y notas de cr… |
| RF-12.25 | Media | E2 | Media | — | El portal debe permitir al cliente del canal moderno registrarse con su RUT de empresa, correo electrónic… |
| RF-12.26 | Media | E2 | Media | — | El portal debe permitir al cliente autenticarse con su correo y contraseña registrados. |
| RF-12.27 | Media | E2 | Media | — | El portal debe permitir al cliente solicitar un enlace de restablecimiento de contraseña a su correo regi… |
| RF-12.28 | Media | E2 | Media | — | El portal debe permitir al cliente cerrar su sesión de forma explícita, invalidando el token de sesión ac… |
| RF-12.29 | Media | E2 | Media | — | El portal debe cerrar automáticamente la sesión del cliente tras un período de inactividad definido, sin … |
| RF-12.30 | Media | E2 | Media | — | El portal debe permitir al cliente pagar los pedidos generados en autoservicio (RF-12.15) mediante la pla… |
| RF-14.01 | Crítica | E1 | Crítica | — | El sistema debe integrarse con la plataforma de telemetría de terceros existente que cubre los camiones p… |
| RF-14.02 | Alta | E1 | Media | P | El sistema debe mostrar en el mapa las rutas planificadas vs las rutas reales recorridas por cada camión,… |
| RF-14.03 | Alta | E1 | Alta | — | El sistema debe generar una alerta cuando el camión se desvíe más de 3 km de la ruta planificada, para qu… |
| RF-14.04 | Crítica | E2 | Media | P | El sistema debe integrar los datos de telemetría con el módulo de costo de servir, imputando kilómetros r… |
| RF-14.05 | Alta | E1 | Alta | — | El sistema debe registrar qué conductor propio o de transportista externo está asociado a cada camión en … |
| RF-14.06 | Media | E1 | Media | — | El sistema debe permitir la gestión de geocercas zonas geográficas, para identificar cuándo un camión ent… |
| RF-13.01 | Alta | E1 y E2 | Alta | — | El PROPONENTE debe declarar la arquitectura lógica de la solución organizada en las 8 capas del modelo de… |
| RF-13.02 | Alta | E1 y E2 | Alta | — | El PROPONENTE debe presentar una tabla de emplazamiento que asigne cada componente de la solución a nube … |
| RF-13.03 | Alta | E1 y E2 | Alta | — | El PROPONENTE debe mantener un registro de decisiones de arquitectura (ADR) fechado, con la alternativa e… |
| RF-13.04 | Alta | E1 y E2 | Alta | — | El PROPONENTE debe presentar un modelo de dominio del negocio del caso, con las entidades principales, su… |
| RF-14.01-BTT | Alta | E1 y E2 | Alta | — | El sistema debe permitir clasificar la información del CLIENTE por nivel de sensibilidad (pública, intern… |
| RF-14.02-BTT | Alta | E1 y E2 | Alta | — | El PROPONENTE debe mantener una matriz de controles de seguridad trazable a ISO/IEC 27001 e ISO/IEC 27002… |
| RF-14.03-BTT | Alta | E1 y E2 | Alta | — | El PROPONENTE debe declarar la superficie de exposición completa de la solución: cada nombre de dominio, … |
| RF-14.04-BTT | Alta | E1 y E2 | Alta | — | El PROPONENTE debe disponer de un plan de respuesta a incidentes de seguridad que defina clasificación, c… |
| RF-14.05-BTT | Alta | E1 y E2 | Alta | — | El sistema (o el equipo de seguridad del ADJUDICATARIO) debe notificar al CLIENTE cualquier brecha de seg… |
| RF-15.01 | Alta | E1 y E2 | Alta | — | El sistema debe contar con una gestión de identidad centralizada, con federación mediante OpenID Connect … |
| RF-15.02 | Alta | E1 y E2 | Alta | — | El sistema debe implementar inicio de sesión único para todos los módulos de la solución, con cierre de s… |
| RF-15.03 | Alta | E1 y E2 | Alta | — | El sistema debe exigir autenticación multifactor para personas usuarias administradoras, para todo acceso… |
| RF-15.04 | Alta | E1 y E2 | Alta | — | El sistema debe implementar control de acceso basado en roles, complementado con control basado en atribu… |
| RF-15.05 | Alta | E1 y E2 | Alta | — | El sistema debe automatizar el aprovisionamiento y desaprovisionamiento de cuentas, ligado al ciclo de vi… |
| RF-16.01 | Alta | E1 y E2 | Alta | — | El sistema debe implementar observabilidad unificada para nube y on-premise, con métricas, registros y tr… |
| RF-16.02 | Alta | E1 y E2 | Alta | — | El CLIENTE debe disponer de acceso propio y permanente a los tableros operacionales y de negocio, con dat… |
| RF-16.03 | Alta | E1 y E2 | Alta | — | El sistema debe implementar alertamiento basado en síntomas de negocio y no sólo en umbrales de infraestr… |
| RF-16.04 | Alta | E1 y E2 | Alta | — | El sistema (o el equipo del ADJUDICATARIO) debe ejecutar un análisis de causa raíz obligatorio tras cada … |
| RF-17.01 | Alta | E1 y E2 | Alta | — | El sistema debe disponer de un módulo de administración que permita al CLIENTE, sin intervención del ADJU… |
| RF-17.02 | Alta | E1 y E2 | Alta | — | El sistema debe permitir parametrizar reglas de negocio (umbrales, plazos, montos, tolerancias, catálogos… |
| RF-17.03 | Alta | E1 y E2 | Alta | — | El sistema debe requerir aprobación de un segundo perfil para todo cambio de parámetro con impacto operac… |
| RF-17.04 | Alta | E1 y E2 | Alta | — | El sistema debe registrar toda operación que cree, modifique o elimine información, con identificación de… |
| RF-17.05 | Alta | E1 y E2 | Alta | — | El CLIENTE debe poder consultar y exportar la auditoría desde la interfaz, con filtros por persona, perío… |
| RF-17.06 | Alta | E1 y E2 | Alta | — | El sistema debe soportar flujos de trabajo con estados, transiciones, responsables, plazos, escalamiento … |
| RF-17.07 | Alta | E1 y E2 | Alta | — | El sistema debe proveer una bandeja de tareas unificada para cada persona usuaria, donde se visualicen to… |
| RF-17.08 | Alta | E1 y E2 | Alta | — | El sistema debe gestionar documentos con versionado, metadatos, control de acceso, búsqueda por contenido… |
| RF-17.09 | Media | E1 y E2 | Media | — | El sistema debe generar documentos a partir de plantillas administrables por el CLIENTE, con datos de la … |
| RF-17.10 | Alta | E1 y E2 | Alta | — | El sistema debe enviar notificaciones por al menos tres canales: correo electrónico, notificación en la a… |
| RF-17.11 | Alta | E1 y E2 | Alta | C | El sistema debe disponer de búsqueda global con indexación de texto completo con tolerancia a errores de … |
| RF-17.12 | Alta | E1 y E2 | Alta | C | El sistema debe presentar listados ordenables, filtrables, paginados y exportables en formatos abiertos, … |
| RF-17.13 | Media | E1 y E2 | Media | — | El sistema debe disponer de un portal público con la información que el caso determine (catálogo sin prec… |
| RF-18.01 | Alta | E1 y E2 | Alta | — | El sistema debe soportar firma electrónica conforme a la Ley N.º 19.799 (2002, art. 2, letra g, y arts. 3… |
| RF-18.02 | Media | E1 y E2 | Media | — | Cada persona usuaria debe poder configurar sus preferencias de canal (correo, SMS, notificación en app) y… |
| RF-18.03 | Alta | E1 y E2 | Alta | — | El sistema debe enviar notificaciones de forma asíncrona, con reintento ante falla, control de duplicados… |
| RF-02.11 | Alta | E1 | Alta | — | El sistema debe registrar en cada plataforma de cross-docking la lectura de las unidades logísticas al ll… |
| RF-06.14 | Alta | E1 | Alta | — | El sistema debe enviar al ERP, para cada guía de despacho electrónica, la evidencia de recepción capturad… |
| RF-06.06 | Alta | E1 | Alta | — | El sistema debe registrar la hora real de llegada y de término de cada entrega. |
| RF-07.01 | Alta | E1 | Alta | — | El sistema debe calcular para cada camión y turno el monto esperado de rendición a partir de las entregas… |
| RF-09.10 | Media | E1 | Media | — | El sistema debe permitir parametrizar por tipo de producto la regla de excursión térmica (desviación y du… |
| RF-10.01 | Media | E1 | Media | — | El sistema debe sugerir la reposición de compras por SKU y proveedor a partir de la historia de ventas, c… |
| RF-10.02 | Media | E1 | Media | — | El sistema debe incorporar al cálculo de reposición las promociones comprometidas. |
| RF-10.03 | Media | E1 | Media | — | El sistema debe traspasar la sugerencia aprobada al módulo de compras del ERP. |
| RNF-12.01 | Crítica | E2 | Crítica | — | El portal de autoatención de clientes (RF-12.15 a RF-12.18) y la recepción EDI (RF-12.01 a RF-12.09) debe… |
| RNF-12.02 | Alta | E2 | Alta | — | El mecanismo de recepción EDI debe permitir configurar el mapeo de mensajería de una nueva cadena sin des… |
| RNF-03.01 | Alta | E1 | Alta | — | El tiempo para registrar una línea de pedido no debe superar 1,5 segundos, con o sin señal parcial. |
| RNF-03.02 | Alta | E1 | Alta | — | El tiempo para consultar stock y crédito con conectividad no debe superar 2 segundos. |
| RNF-03.03 | Alta | E1 | Media | P | El tiempo para consultar el historial de compra con conectividad no debe superar 2 segundos. |
| RNF-01.01 | Alta | E1 | Alta | — | El tiempo de procesamiento para el registro de cada ítem en recepción, desde la confirmación del escaneo … |
| RNF-01.02 | Crítica | E1 | Crítica | — | El sistema debe conservar los registros de recepción según el plazo por tipo de dato: trazabilidad sanita… |
| RNF-01.03 | Crítica | E1 | Crítica | — | El sistema debe operar en modo desconectado durante mínimo 24 horas continuas sin pérdida de datos y sinc… |
| RNF-02.01 | Crítica | E1 | Crítica | — | El sistema de gestión de almacén (inventario, movimientos, conteos, consultas de stock) debe operar en mo… |
| RNF-05.01 | Alta | E1 | Alta | — | La confirmación de una línea de picking (escaneo + validación + almacenamiento local) no debe superar 1 s… |
| RNF-05.02 | Crítica | E1 | Crítica | — | La interfaz de picking debe ser operable sin precisión de toque fino, con elementos interactivos de al me… |
| RNF-05.03 | Crítica | E1 | Crítica | — | Un nuevo operario de preparación, sin experiencia previa con el sistema, debe completar una misión de pic… |
| RNF-08.01 | Alta | E1 | Alta | — | El registro de una devolución en el andén del CD (escaneo + selección de destino) no debe superar 30 segu… |
| RNF-08.02 | Alta | E1 | Alta | — | Los registros de devoluciones y mermas deben conservarse según el plazo por tipo de dato: trazabilidad sa… |
| RNF-09.01 | Crítica | E1 | Crítica | — | El sistema tiene un tiempo de respuesta para generar el listado de clientes afectados por un lote (RF-09.… |
| RNF-09.02 | Crítica | E1 | Crítica | — | El sistema debe conservar los registros sanitarios y de trazabilidad de lote durante el período mínimo le… |
| RNF-09.03 | Alta | E1 | Alta | — | El sistema debe registrar todas las consultas y modificaciones de información sensible —trazabilidad (lot… |
| RNF-09.04 | Crítica | E1 | Crítica | — | El sistema debe funcionar Sin cobertura de señal y sincronizando al recuperar conectividad fuera de la cá… |
| RNF-07.01 | Crítica | E1 | Crítica | — | El sistema debe sincronizar la información de preconciliación de cobranzas capturada en la aplicación móv… |
| RNF-07.02 | Crítica | E1 | Crítica | — | El sistema debe cifrar a nivel de campo (AES-256 en reposo, TLS 1.3 en tránsito) los datos de pagos en ef… |
| RNF-04.01 | Media | E1 | Media | — | El motor de ruteo debe procesar la asignación y secuencia completa de la matriz diaria de entregas en un … |
| RNF-06.01 | Media | E1 | Media | — | El sistema debe persistir el 100% de los datos necesarios en el almacenamiento cifrado local para ejecuta… |
| RNF-11.01 | Alta | E1 | Alta | — | El sistema debe desplegar los indicadores operacionales del día con una latencia no superior a 5 minutos … |
| RNF-11.02 | Alta | E1 | Alta | — | El sistema debe desacoplar el procesamiento analítico y de reportería (OLAP/BI) del motor transaccional o… |
| RNF-13.01 | Crítica | E1 y E2 | Crítica | — | El componente on-premise debe operar de forma autónoma y degradada ante la pérdida total del enlace con l… |
| RNF-13.02 | Crítica | E1 y E2 | Crítica | — | El PROPONENTE debe declarar qué funciones NO estarán disponibles en modo desconectado y qué procedimiento… |
| RNF-13.03 | Alta | E1 y E2 | Alta | — | Los equipos on-premise críticos deben ser redundantes. |
| RNF-13.04 | Alta | E1 y E2 | Alta | — | El almacenamiento local debe tolerar la falla de al menos un disco |
| RNF-13.05 | Alta | E1 y E2 | Alta | — | el PROPONENTE debe declarar el nivel RAID escogido y justificarlo frente a las alternativas. |
| RNF-13.06 | Alta | E1 y E2 | Alta | — | Los sistemas on-premise deben endurecerse conforme a los CIS Benchmarks aplicables, con gestión centraliz… |
| RNF-13.07 | Alta | E1 y E2 | Alta | — | El enlace entre el sitio on-premise y la nube debe ser redundante, con caminos físicos y proveedores dist… |
| RNF-13.08 | Alta | E1 y E2 | Alta | — | El PROPONENTE debe dimensionar el ancho de banda requerido por sitio, en régimen normal y en peak, y just… |
| RNF-13.09 | Alta | E1 y E2 | Alta | — | El PROPONENTE debe realizar un estudio de cobertura de red inalámbrica en los centros de distribución, qu… |
| RNF-14.01 | Crítica | E1 y E2 | Crítica | — | Todo el tráfico en tránsito debe emplear TLS 1.3, con prohibición expresa de TLS 1.0 y 1.1, conjuntos de … |
| RNF-14.02 | Crítica | E1 y E2 | Crítica | — | La totalidad de los datos en reposo debe estar cifrada, con claves gestionadas en un servicio de gestión … |
| RNF-14.03 | Alta | E1 y E2 | Alta | — | En la nube, la red debe segmentarse por capas, con subredes privadas para aplicación y datos, y exposició… |
| RNF-14.04 | Alta | E1 y E2 | Alta | — | Los eventos de seguridad deben registrarse de forma centralizada e inalterable, y correlacionarse en una … |
| RNF-14.05 | Alta | E1 y E2 | Alta | — | Se debe implementar detección y respuesta en puntos finales (EDR) y en cargas de trabajo, tanto en nube c… |
| RNF-14.06 | Alta | E1 y E2 | Alta | — | Se deben ejecutar pruebas de intrusión (pentesting) por un tercero independiente del ADJUDICATARIO, anual… |
| RNF-14.07 | Alta | E1 y E2 | Alta | — | El flujo de integración continua debe incorporar análisis estático de código (SAST), análisis de composic… |
| RNF-14.08 | Alta | E1 y E2 | Alta | — | Cada versión liberada debe acompañarse de su inventario de componentes de software en formato CycloneDX o… |
| RNF-14.09 | Alta | E1 y E2 | Alta | — | Los artefactos deben firmarse y su procedencia debe verificarse conforme a SLSA nivel 3 o superior. |
| RNF-14.10 | Alta | E1 y E2 | Alta | — | Queda prohibido el uso de datos productivos reales en ambientes no productivos sin anonimización o seudon… |
| RNF-15.01 | Crítica | E1 y E2 | Crítica | — | El sistema debe implementar política de sesión con duración máxima, caducidad por inactividad, renovación… |
| RNF-15.02 | Crítica | E1 y E2 | Crítica | — | Las credenciales de sesión deben ser firmadas y de vida breve, con credencial de refresco rotatoria. Qued… |
| RNF-15.03 | Alta | E1 y E2 | Alta | — | El sistema debe registrar auditoría completa del ciclo de vida de la identidad: creación, modificación, e… |
| RNF-16.01 | Alta | E1 y E2 | Alta | — | Los indicadores de nivel de servicio deben medirse sobre la experiencia real de la persona usuaria (perce… |
| RNF-16.02 | Alta | E1 y E2 | Alta | — | El PROPONENTE debe documentar un libro de operación y una guía de resolución para cada escenario de falla… |
| RNF-16.03 | Crítica | E1 y E2 | Crítica | — | Los registros (logs) de la solución no deben contener datos personales sensibles ni credenciales, y su ac… |
| RNF-17.01 | Alta | E1 y E2 | Alta | — | El período de retención de la auditoría debe ser el que fije el caso y, en su defecto, no inferior a cinc… |
| RNF-17.02 | Alta | E1 y E2 | Alta | — | Las exportaciones de gran volumen deben procesarse de forma asíncrona, con notificación al completarse y … |
| RNF-17.03 | Alta | E1 y E2 | Alta | — | El portal público debe resistir picos de tráfico sin degradar los servicios transaccionales internos, med… |
| RNF-19.01 | Alta | E1 y E2 | Alta | — | El PROPONENTE debe presentar el cálculo de capacidad que sustenta su dimensionamiento, con los supuestos … |
| RNF-19.02 | Alta | E1 y E2 | Alta | — | Las capas de aplicación e integración deben escalar horizontalmente de forma automática, con umbrales, lí… |
| RNF-19.03 | Alta | E1 y E2 | Alta | — | El PROPONENTE debe identificar el componente que primero se convertirá en cuello de botella al crecer la … |
| RNF-19.04 | Alta | E1 y E2 | Alta | — | Se deben ejecutar pruebas de carga sobre Preproducción con un volumen equivalente a 1,5 veces el peak dec… |
| RNF-20.01 | Crítica | E1 y E2 | Crítica | — | La solución debe alcanzar una disponibilidad mensual mínima de 99.9% para los servicios clasificados como… |
| RNF-20.02 | Crítica | E1 y E2 | Crítica | — | El PROPONENTE debe clasificar cada servicio de la solución en crítico, alto, medio o bajo, justificando l… |
| RNF-20.03 | Crítica | E1 y E2 | Crítica | — | El PROPONENTE debe elaborar un plan de continuidad del negocio conforme a ISO 22301, con análisis de impa… |
| RNF-20.04 | Alta | E1 y E2 | Alta | — | Se deben ejecutar pruebas de resiliencia mediante inyección controlada de fallas (caída de instancia, de … |
| RNF-20.05 | Alta | E1 y E2 | Alta | — | El PROPONENTE debe documentar, por cada dependencia externa, el comportamiento de la solución cuando esa … |
| RNF-20.06 | Crítica | E1 y E2 | Crítica | — | El PROPONENTE debe habilitar un sitio secundario para recuperación ante desastres, con RTO ≤ 4 horas y RP… |
| RNF-20.07 | Crítica | E1 y E2 | Crítica | — | La política de respaldo debe seguir el esquema 3-2-1-1-0: tres copias, en dos medios distintos, una fuera… |
| RNF-21.01 | Crítica | E1 y E2 | Crítica | — | El ADJUDICATARIO debe disponer de un centro de operaciones de red (NOC) con cobertura 24×7×365, propio o … |
| RNF-21.02 | Alta | E1 y E2 | Alta | — | El ADJUDICATARIO debe designar un gerente de servicio dedicado como contraparte permanente del CLIENTE du… |
| RNF-21.03 | Alta | E1 y E2 | Alta | — | El centro de atención debe cumplir un tiempo de atención al usuario final de 80% antes de 20 segundos y u… |
| RNF-21.04 | Alta | E1 y E2 | Alta | — | El horario mínimo de atención será de 08:00 a 20:00 en días hábiles, ampliado a 24×7 para los incidentes … |
| RNF-21.05 | Alta | E1 y E2 | Alta | — | El PROPONENTE debe dimensionar la dotación del centro de atención con fundamento cuantitativo, empleando … |
| RNF-21.06 | Alta | E1 y E2 | Alta | — | Debe existir un canal único de registro de incidentes y solicitudes, con número de ticket, clasificación … |
| RNF-21.07 | Alta | E1 y E2 | Alta | — | Los especialistas de niveles 2 y 3 deben trasladarse a los sitios alejados (Curicó, Chillán, Los Ángeles)… |
| RNF-21.08 | Alta | E1 y E2 | Alta | — | El PROPONENTE debe declarar el tamaño de la bolsa anual de horas de mantención evolutiva, su composición … |
| RNF-21.09 | Alta | E1 y E2 | Alta | — | Las actualizaciones de versión de los componentes de base (sistemas operativos, bases de datos, framework… |
| RNF-22.01 | Alta | E1 y E2 | Alta | — | El PROPONENTE debe presentar un plan de capacitación estructurado por perfil: personas usuarias finales, … |
| RNF-22.02 | Alta | E1 y E2 | Alta | — | Todo el material de capacitación debe entregarse en español, en formato editable (Word, PowerPoint, etc.)… |
| RNF-22.03 | Alta | E1 y E2 | Alta | — | La capacitación no podrá afectar la operación del CLIENTE: se programará por turnos y en horarios acordad… |
| RNF-22.04 | Alta | E1 y E2 | Alta | — | Las personas usuarias administradoras y el equipo técnico del CLIENTE deben ser evaluados y certificados … |
| RNF-22.05 | Alta | E1 y E2 | Alta | — | Durante la Operación, el ADJUDICATARIO debe ejecutar al menos dos jornadas anuales de actualización y cap… |
| RNF-22.06 | Alta | E1 y E2 | Alta | — | El ADJUDICATARIO debe proveer acompañamiento y mentoría al equipo técnico del CLIENTE durante al menos se… |
| RNF-23.01 | Alta | E1 y E2 | Alta | — | El PROPONENTE debe especificar cada dispositivo de terreno (lectores de código, impresoras térmicas, sens… |
| RNF-23.02 | Alta | E1 y E2 | Alta | — | Los dispositivos de terreno deben declarar su grado de protección contra polvo y agua (IP) y su resistenc… |
| RNF-23.03 | Alta | E1 y E2 | Alta | — | El PROPONENTE debe indicar el ciclo de vida esperado de cada dispositivo de terreno, la disponibilidad de… |
| RNF-23.04 | Alta | E1 y E2 | Alta | — | El PROPONENTE debe especificar las estaciones de trabajo requeridas para la operación y administración de… |
| RNF-09.05 | Crítica | E1 | Crítica | — | Cada cámara y cada vehículo con frío registra temperatura con una frecuencia, parametrizable por tipo de … |
| RNF-12.03 | Alta | E2 | Alta | — | El acuse de recibo digital de cada entrega a una cadena se envía dentro de los 30 minutos posteriores a l… |
| RNF-14.11 | Crítica | E1 | Crítica | — | Hasta el acuerdo con el sindicato, la posición se registra por vehículo y ruta, no por persona, y no se u… |
| RNF-14.12 | Alta | E1 | Alta | — | El 100 % de los campos con datos personales capturados en terreno (receptor, conductor, preventista, clie… |
