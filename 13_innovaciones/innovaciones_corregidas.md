# Subdocumento 13 — Innovaciones corregidas (borrador de trabajo)

**Base:** las cinco innovaciones de `13_innovaciones/13_innovaciones/contenido.tex` (cartera v4).

**Referencia para corregirlas:** los SD1 a SD4 de `LafroX-Markdown`:
- módulos, reglas y requerimientos del SD3 y su T-12;
- componentes y herramientas del SD4 y su T-11;
- metas del SD2;
- roles del SD1.

**Formato:** markdown de trabajo, sin cuidar el formato final. Las metas son propuestas de diseño. Los paquetes `INN-0N.Pn` son el insumo para la EDT del SD7.

Calendario (Art. 17° y E-25):

| Hito | Mes |
|---|---|
| H3 | 6 |
| H4 | 10 |
| H5 | 12 |
| Marcha blanca E1 | 13–15 |
| H7, producción E1 | 16 |
| H9 | 17 |
| H10 | 18 |
| Marcha blanca E2 | 19–20 |
| H12, producción E2 | 21 |
| Operación | 21–56 |

---

## Qué se corrigió respecto de la v4

| N.º | v4 | Corregida | Correcciones principales |
|---|---|---|---|
| 1 | Alerta de vida útil antes del vencimiento | **Seguimiento de vencimiento posentrega en el local** | El nombre se confundía con la alerta de vida útil remanente en bodega que exige RF-02.09. Se agregan paquetes, mes y meta, que faltaban. La meta se separa de la de merma ≤ 1,0 %, ya comprometida en el SD2. El ritmo de consumo se obtiene del historial de compra de M3 (RF-03.14). |
| 2 | La condición adversa como parte del proceso de construcción | **Reproducción de incidentes de terreno** | El deslinde era falso: QA ya ensaya fallas de enlace (SD4 §4.1.9) y RT-10.07 / RNF-20.04 ya exigen inyección de fallas antes de cada paso a producción. Se elimina el «ambiente adicional», que contradecía los cinco ambientes del SD4. El centro pasa a ser el incidente real (la «contracara» de la v4). |
| 3 | La visita de preventa como instrumento de medición del mercado | **NUEVA: Vida útil remanente por historia térmica del lote** | La anterior no era tecnológica ni de arquitectura (era un método de encuesta), y el caso la pide casi literalmente (cap. 8, entrevista a la preventista). |
| 4 | Tramo de la Operación remunerado contra nivel de servicio y costo de servir | **Tramo variable de la Operación ligado al costo de servir** | Las Bases sí prevén pagos variables (estructura de pagos de la Operación, E-25). Se elimina la «consulta del Art. 43.3» y el «\$45.000». Se fija la estructura sin montos y la protección con las metas de OTIF del SD3. |
| 5 | El almacenero como dueño de su propio dato | **Hoja de negocio del almacenero** | La impresora de cabina es del camión (T-11), no del preventista. Ley 19.628 → Ley 21.719. El bloque comparativo queda condicionado. Se agregan paquetes, mes y metas. |

Segunda ronda (2026-10-02, tras la revisión de Comisión del listado):

| N.º | Corrección |
|---|---|
| 1 | El ritmo de reposición sale del historial de M3 (RF-03.14), no de una consulta al ERP que el SD4 no declara. Se corrige lo que se atribuía a Riesenegger et al. (2023). |
| 2 | Deslinde frente a RT-14.06 (causa raíz de incidentes críticos) y explicación de por qué un reporte de fallos estándar no basta. |
| 3 | El primer párrafo declara que el registro continuo es base obligatoria. INN-03 oferta y cumple RT-05.30. Se quita «(nueva)» del título. |
| 4 | Se conecta con la restricción 9 (TI de cuatro personas). Madurez con escala TRL y fuente en lugar de la escala propia. Tabla de ingresos y costos por mes. |
| 5 | Caso del local sin pedido esa semana, medido en I-05A. |
| Todas | Tabla de ubicación en el flujo de caja (rubro, clase de la planilla del CLIENTE y meses), sin montos. Códigos F-14 y R18-04 con su nombre. |

Correcciones comunes a las cinco:
- Se eliminan las 10 notas «Pendiente del Subdocumento 7 / del Informe 3» y las 7 «Marcas».
- Módulos con los nombres del SD3 (§3.4 y T-12): M2 Inventario, M3 Preventa, M5 Preparación, M6 Reparto, M7 Cobranza y rendición, M8 Devoluciones y envases, M9 Calidad y trazabilidad, M10 Analítica.
- Componentes físicos del SD4 §4.2.
- Responsables tomados del SD1 §1.5.

---

## Introducción del capítulo (texto propuesto)

El Artículo 28° exige cinco innovaciones, una por tipo, trazables con la arquitectura, con la EDT y con el flujo de caja. Este capítulo las presenta en ese orden. Cada una desarrolla los siete elementos del Artículo 29°.

**Conexión con los demás capítulos:**
- Cada innovación se ubica en los módulos del Subdocumento 3 y en los componentes del Subdocumento 4 (RT-26.01).
- Sus paquetes y meses alimentan la EDT y el cronograma del Subdocumento 7 (RT-26.02).
- Sus riesgos entran al registro del Subdocumento 8, y sus pruebas al plan de calidad del Subdocumento 9.
- Ninguna incorpora inteligencia artificial, por lo que no se aplica el Capítulo 18 de las Bases Técnicas (RT-26.06).
- Ninguna agrega hardware al T-11.
- La valorización va en la Oferta Económica (Art. 50.2).
- Las fichas formales están en el Formulario T-19.

---

## 13.1 Innovación 1

**Tipo 1, producto o servicio: Seguimiento de vencimiento posentrega en el local (INN-01).** Es un servicio que sigue los lotes de Puelche después de entregarlos. Avisa al preventista qué lotes de ese local no alcanzarán a venderse antes de vencer y con qué acción autorizada puede evitarse la pérdida.

### Problema
- La merma por vencimiento es el 1,7 % del valor del inventario al año. Se detecta tarde: en el conteo, en la preparación o «en la góndola del cliente» (Caso, cap. 4.8).
- La preventista lo confirma: ve el producto vencido de Puelche en la góndola y no tiene dónde anotarlo (Caso, cap. 8).
- El rechazo por vencimiento próximo es causa habitual de devolución.
- La pérdida que ocurre **después de la entrega** no tiene medición propia.

### Deslinde
| Ya es alcance obligatorio | Dónde |
|---|---|
| FEFO estricto en la asignación del picking | RF-05.05 (M5), RF-02.09 (M2), RNG-10 |
| **Alerta cuando un producto en stock alcanza un umbral de vida útil remanente** | RF-02.09: es una alerta **en bodega**, sobre el stock propio |
| Picking dirigido con causa de faltante, incluido «producto vencido» | RF-02.08 |
| Registro de la merma ya detectada, incluida la de la góndola | RF-08.05 (M8) |
| Sugerencia de productos por historial | RF-03.14 (M3) |
| Ciclo de vida del lote hasta el cliente | RF-02.10, RF-01.03 |
| **Merma ≤ 1,0 % del inventario, a 12 meses de operación** | SD2, Tabla 2.1 (meta base) |

**Lo agregado:** el seguimiento **en el local** y **antes** de la pérdida, con una acción comercial y su cierre. Todo el alcance obligatorio ocurre dentro de la bodega o después de que la merma ya existe. Para no apropiarse de la meta base, la innovación **no se mide con la merma de inventario**, sino con el vencimiento posentrega (I-01B).

### Tecnología
- **Regla de cobertura:** para cada par lote–local, se compara la cobertura en días (saldo estimado / ritmo de reposición) con la vida útil remanente del lote.
- **Saldo estimado:** sale de las entregas por lote y las devoluciones, y **se confirma en la visita**.
- **Ritmo de reposición:** se estima con el historial de compra por cliente y producto que M3 Preventa ya mantiene para sus sugerencias (RF-03.14). Es reposición, no venta al consumidor; por eso se confirma.
- **Vida útil remanente:** es la de INN-03 cuando el lote es refrigerado o congelado y ya tiene esa estimación; en los demás casos, la fecha impresa (RF-01.03).
- **Datos insuficientes:** muestra fecha y cantidad, sin simular una predicción.
- **Límites:** el saldo estimado nunca entra al inventario oficial ni bloquea una venta. La disposición sanitaria sigue siendo de M9.

### Madurez
- Escala TRL (European Commission, 2016).
- El cálculo de cobertura es aritmética conocida.
- La estimación del ritmo por local en el canal tradicional, con compras irregulares, decide la calidad del aviso.
- Riesenegger et al. (2023) revisan la merma de alimentos en la operación del supermercado: pedido, exhibición, precio y retiro de producto por vencer. Es el mismo punto de la cadena donde actúa esta innovación. Las prácticas que reseñan las ejecuta el propio comercio con sus sistemas. Lo propio aquí es que el distribuidor las lleve a un almacén que no tiene sistema, a través de la visita del preventista.
- El servicio integrado parte en **TRL 2**. Objetivos: **TRL 4 al mes 10** (H4, con datos sintéticos) y **TRL 6 al mes 15** (piloto en marcha blanca).

### Incorporación
**Arquitectura:**
- Capa 4: M10 Analítica calcula la lista en la noche con datos de M2 Inventario, M9 Calidad y trazabilidad y el historial de compra de M3 Preventa.
- M3 Preventa la entrega en el terminal C-01 (capa 1). Viaja en el terminal y funciona sin señal (SD4 §4.1.15).
- La respuesta de la visita vuelve por la cola de sincronización de M3.
- No se abre una API pública.

**Piloto:** 120 locales de 12 rutas, con ≥ 100 avisos evaluables. Es una decisión de diseño, no una muestra representativa.

| Paquete | Meses | Entregable | Rama EDT |
|---|---|---|---|
| INN-01.P1 | 7–9 | Catálogo de acciones autorizadas (Comercial + Calidad) y protocolo del piloto | Etapa 1 |
| INN-01.P2 | 9–10 | Estimador de saldo y ritmo; confirmación de existencias (software H4) | Etapa 1 |
| INN-01.P3 | 9–10 | Lista sin conexión y respuesta de visita en M3 (software H4) | Etapa 1 |
| INN-01.P4 | 11–15 | Certificación H5, piloto en marcha blanca e informe de habilitación | Etapa 1 |

**Materialización:** mes 16. **Responsable:** Líder de Datos (Leandro Chamorro); Comercial y Calidad del CLIENTE validan el catálogo.

### Impacto económico (sin montos)
- **Inversión:** HH de datos, desarrollo móvil (Kotlin) y acompañamiento del piloto, meses 7–15. No requiere hardware ni licencias.
- **Costo operacional:** cálculo nocturno, almacenamiento y minutos de visita, meses 16–56.
- **Beneficio:** unidades vencidas evitadas en el local × costo unitario, menos canjes y descuentos. No se suma al beneficio de la meta base de merma ni al de INN-03.

**Ubicación en el flujo de caja** (sin montos; la valorización va en la Oferta Económica, Informe 3):

| Rubro | Clase (planilla del CLIENTE) | Meses |
|---|---|---|
| HH de datos, desarrollo móvil y diseño del catálogo | Inversión / RR. HH. | 7–15 |
| Acompañamiento del piloto en terreno | Inversión / RR. HH. | 13–15 |
| Cálculo nocturno y almacenamiento en nube | Operación | 16–56 |
| Mantención de la regla y del catálogo | Operación / RR. HH. | 16–56 |
| Beneficio: unidades vencidas evitadas, neto de canjes | Beneficio | Desde el 16; primera medición en el 28 |

### Indicador
| Id | Indicador | Línea base | Meta | Momento |
|---|---|---|---|---|
| I-01A | Avisos con riesgo confirmado / avisos evaluables | Sin medición | ≥ 70 % con ≥ 100 avisos | Mes 15 |
| I-01B | Unidades vencidas en el local / unidades entregadas (cohorte del piloto) | Medición de los meses 13–15 | −25 % relativo | Mes 28 |
| I-01C | Devoluciones con causal «vencimiento próximo» / devoluciones (rutas del piloto) | Medición de los meses 13–15; el caso no la desagrega | −20 % relativo | Mes 28 |

### Riesgo
| Riesgo | P / I | Mitigación | Contingencia |
|---|---|---|---|
| Avisos falsos por compras irregulares del canal tradicional | Media / Alto | No liberar sin I-01A; mostrar la confianza de cada aviso; confirmar en la visita | Degradar a aviso solo por vida útil remanente del lote, sin estimar el ritmo |
| Aviso sin acción posible (no hay catálogo de canje) | Media / Alto | El catálogo (P1) es condición de activación | Mantener solo el aviso informativo y escalar a Comercial |

---

## 13.2 Innovación 2

**Tipo 2, proceso: Reproducción de incidentes de terreno (INN-02).** Cambia cómo se atiende un fallo de terreno. El incidente real se convierte en un escenario reproducible, la corrección se valida contra ese escenario y solo entonces se cierra.

### Problema
- Los pedidos se pierden o duplican por falta de señal «semanalmente, sin medición» (Caso, cap. 18, criterio 6).
- La preventista cuenta que a veces el pedido «no se mandó» y otras «se manda dos veces» (Caso, cap. 8).
- Los fallos ocurren donde no se programa: rutas de Empedrado, Chanco, Cauquenes, Pinto y Alto Biobío sin señal hasta dos horas, cámara a −22 °C, ventana 05:30–07:00 y peak de septiembre.
- Llegan a la mesa de ayuda como un relato que no se puede reproducir en un escritorio.

### Deslinde
| Ya es alcance obligatorio | Dónde |
|---|---|
| Inyección controlada de fallas antes de cada paso a producción y semestral en operación | RT-10.07; RNF-20.04 en el T-12 |
| QA ensaya integración, regresión, idempotencia y **fallas de enlace** con datos controlados | SD4 §4.1.9 |
| Preproducción: aceptación, carga y resiliencia con topología equivalente | SD4 §4.1.9 |
| Revisión por pares, pruebas de contrato, PHPUnit, PHPStan y análisis de secretos como bloqueo | SD4 §4.1.9 (RT-04.03–04.05) |
| Reconciliación determinista y bitácora | RT-03.12, RT-03.13 |
| Análisis de causa raíz de todo incidente **crítico**, con informe en cinco días hábiles y seguimiento de las acciones correctivas | RT-14.06 (RF-16.04 en el catálogo) |

**Por qué un reporte de fallos estándar no basta.** Las herramientas corrientes de reporte de fallos móviles registran caídas de la aplicación y los pasos previos. El defecto típico de Puelche no es una caída. La aplicación sigue funcionando y el pedido se pierde o se duplica porque la cola local y el servidor procesaron los eventos en otro orden durante la reconexión. Ese defecto no deja rastro en un reporte de fallos. Solo se reproduce con el orden causal de la cola local, los reintentos y el estado de conectividad, que es lo que contiene el paquete de esta innovación.

**Lo que agrega frente a RT-14.06:** RT-14.06 exige explicar por escrito la causa de los incidentes **críticos**. Esta innovación cubre también los incidentes **no críticos** de terreno, que son los frecuentes («semanal»). Además, cambia el criterio de cierre: no basta un informe de causa; el incidente se cierra cuando la corrección pasa la reproducción del caso real. El informe de RT-14.06 se alimenta del mismo paquete, sin duplicar el trabajo.

**Lo agregado:** todo lo anterior prueba fallas **que el equipo imagina**. La innovación agrega el circuito para fallas **que ocurrieron en la calle**, en cuatro pasos:
1. El terminal arma un paquete sanitizado con la secuencia causal.
2. QA lo reproduce.
3. La corrección se valida contra ese mismo paquete.
4. El escenario queda como regresión permanente.

El incidente no se cierra sin reproducción satisfactoria y confirmación del actor de terreno.

### Tecnología
- **Contrato `inn02.paquete-reproduccion.v1`:** correlación seudonimizada, versión de la aplicación Kotlin, transiciones de estado, cola local, reintentos, orden causal y estado de conectividad. Excluye nombres, credenciales, firmas, fotos y contenido comercial.
- **Reproducción:** con recursos efímeros (Terraform) **dentro de QA o Preproducción**. No es un sexto ambiente: se respetan los cinco del RT-04.01.
- **Integración:** se engancha a la cadena GitLab como un trabajo más.
- **Correlación:** la traza viaja con OpenTelemetry hacia la capa 8 (CloudWatch y Grafana).
- **Límites:** frío, guantes y batería no se simulan; requieren prueba física con el dispositivo.
- **Fundamento:** entrega continua (Shahin et al., 2017). Se usan las métricas DORA (2024) de fallo de cambio y recuperación como contexto.

### Madurez
- Las piezas (CI/CD, entornos efímeros, trazas distribuidas) están en **TRL 9** (Shahin et al., 2017).
- El circuito incidente → paquete → reproducción → cierre, aplicado a terminales que trabajan sin señal, parte en **TRL 2**.
- Objetivos: **TRL 4 al mes 5** (pérdida y retorno de red) y **TRL 6 al mes 15** (marcha blanca con incidentes reales).

### Incorporación
**Arquitectura:**
- C-01 (M3 Preventa), C-03 (M5 Preparación) y C-02 (M6 Reparto) emiten la evidencia, con cupo para no competir con los pedidos.
- La capa 8 correlaciona; la capa 7 sanitiza y controla el acceso.

**Flujo de responsabilidades:**
- Operación/SRE recoge la evidencia.
- Calidad admite el paquete.
- Desarrollo corrige.

| Paquete | Meses | Entregable | Rama EDT |
|---|---|---|---|
| INN-02.P1 | 2–3 | Medición inicial de incidentes y contrato de evidencia sanitizado | Gestión y Calidad |
| INN-02.P2 | 3–5 | Circuito mínimo: pérdida y retorno de red en M3 | Gestión y Calidad |
| INN-02.P3 | 5–10 | Cobertura de M3, M5 y M6 | Gestión y Calidad |
| INN-02.P4 | 11–56 | Validación comparada (13–15) y mantenimiento de escenarios en operación | Gestión y Calidad → Operación |

**Materialización:** circuito inicial en el mes 5; beneficio medido al 15. **Responsables:** Líder de Calidad (Maximiliano Miño) y Líder de Operación/SRE (Guillermo Castillo). El Encargado de Seguridad (Álvaro Catalán) aprueba la sanitización (RT-26.07).

### Impacto económico (sin montos)
- **Inversión:** instrumentación de los terminales y circuito, meses 2–10. No duplica el presupuesto de pruebas obligatorias.
- **Costo operacional:** cómputo efímero por corrida y mantenimiento de escenarios, meses 11–56.
- **Beneficio:** horas de diagnóstico evitadas y regresiones repetidas evitadas. «Cero pedidos perdidos» es el criterio 6 y no se cuenta como beneficio de la innovación.

**Ubicación en el flujo de caja** (sin montos):

| Rubro | Clase (planilla del CLIENTE) | Meses |
|---|---|---|
| HH de instrumentación de terminales y sanitización | Inversión / RR. HH. | 2–5 |
| HH de cobertura de M3, M5 y M6 | Inversión / RR. HH. | 5–10 |
| Cómputo efímero por corrida en QA y Preproducción | Operación | 5–56 |
| Mantención de escenarios | Operación / RR. HH. | 11–56 |
| Beneficio: horas de diagnóstico y regresiones evitadas | Beneficio | Desde el 13; primera medición en el 15 |

### Indicador
| Id | Indicador | Línea base | Meta | Momento |
|---|---|---|---|---|
| I-02A | Mediana de horas desde la admisión del incidente hasta la causa reproducida | Incidentes de los meses 5–10, con diagnóstico convencional | −30 % relativo, con ≥ 20 pares comparables | Mes 15 |
| I-02B | Incidentes de terreno admitidos cuyo paquete reproduce la causa / admitidos | Sin medición | ≥ 80 % | Mes 15; trimestral después |
| I-02C | Incidentes reabiertos por la misma causa tras el cierre | Sin medición | 0 | Mensual desde el mes 16 |
| I-02D | Paquetes con datos prohibidos | Cero por diseño | 0 | En cada liberación |

### Riesgo
| Riesgo | P / I | Mitigación | Contingencia |
|---|---|---|---|
| Reproducción artificial que no explica el incidente | Media / Alto | Comparar con el estado observado; revisión de muestras por Calidad | Reproducción semiautomática con un paquete armado por soporte |
| Datos personales en los paquetes o consumo de batería | Media / Alto | Sanitización por reglas fijas, cupo y frecuencia de captura; modelado de amenazas (RT-26.07) | Captura solo a solicitud de soporte |

---

## 13.3 Innovación 3

**Tipo 3, tecnológica o de arquitectura: Vida útil remanente por historia térmica del lote (INN-03).** Cada lote refrigerado o congelado acumula su historia de temperatura desde la recepción hasta la entrega. Con un modelo cinético por familia de producto, la solución estima cuánta vida útil le queda realmente, no solo la que dice la etiqueta.

El registro continuo de temperatura en cámaras y vehículos es alcance obligatorio (criterio 3 del caso; RT-17.06, periféricos) y **no es la innovación**. La innovación es lo que se construye sobre ese registro: asociar cada serie al lote que estuvo expuesto a ella y convertirla en una vida útil remanente por lote.

### Problema
- Hay 1.100 productos refrigerados y congelados y 28 camiones con frío. Hoy no hay registro continuo en ningún punto de la cadena (Caso, cap. 4.9).
- Un cliente de food service rechazó un camión completo y Puelche no pudo demostrar que la temperatura estuvo bien.
- La jefa de calidad pregunta: «Dos grados por diez minutos, ¿es una excursión? ¿Y por cuarenta minutos?» (Caso, cap. 8).
- La solución ya define cuándo hay excursión: 2 °C de desviación sostenida por 15 minutos, parametrizable por tipo de producto (RF-09.05, RF-09.10). La regla graduada del SD3 (RNG-04) deja la disposición final a Calidad. Lo que nadie define es **qué consecuencia tuvo esa excursión sobre la vida útil del lote**. Con eso Calidad tendría que decidir entre liberar, rebajar la vida útil o descartar. Hoy esa decisión se toma sin dato.
- La fecha impresa supone una cadena de frío perfecta, que nadie puede acreditar.

### Deslinde
| Ya es alcance obligatorio | Dónde |
|---|---|
| Registro continuo de temperatura en cámaras y vehículos | Criterio 3; RF-09.03, RF-09.04 (M9) |
| Serie sin brechas: un intervalo sin lectura se registra como evento | RNF-09.05 |
| Alerta en tiempo real de excursión (2 °C por 15 min) y regla parametrizable por tipo de producto | RF-09.05, RF-09.10 |
| Respuesta graduada: advertencia o retención preventiva; disposición de Calidad | RF-09.06 en la versión del SD3 y su T-12; RNG-04 (SD3 §3.2.4) |
| Rechazo de un producto por sospecha de ruptura de la cadena de frío | RF-09.07 |
| **Evidencia de cumplimiento de la cadena de frío ante la autoridad sanitaria y ante el cliente** | RF-09.09 |
| Bloqueo en el borde < 5 s y buffer de 24 h | SD4 §4.2, componente B-02 |
| Trazabilidad por eventos GS1 EPCIS | SD4 §4.1, hub EDI y trazabilidad |
| FEFO por fecha de vencimiento | RF-05.05, RF-02.09, RNG-10 |
| Analítica predictiva | RT-05.30 es **deseable**: «se valorará», no se exige. Esta innovación es la forma en que LafroX lo oferta (ver más abajo) |

**Lo agregado:** una **medida continua por lote**, la vida útil remanente estimada, derivada de su historia térmica real.
- **Para Calidad:** la regla graduada y el bloqueo no cambian. La medida le da a Calidad evidencia cuantitativa para disponer en la zona gris.
- **Para la bodega:** M2 y M5 reciben un orden de salida sugerido por vida útil remanente real, que Calidad habilita familia por familia. Es una sugerencia, no un reemplazo de RF-05.05.
- **Para INN-01:** recibe una vida útil más realista.

### Tecnología
1. **EPCIS 2.0 con datos de sensor.** La versión 2.0 del estándar agregó `sensorElementList` para adjuntar lecturas o resúmenes de sensor a un evento de negocio (GS1 AISBL, 2022). Cada movimiento del lote (recepción, ubicación en cámara, carga del SSCC al camión, entrega) lleva el resumen térmico del tramo: mínimo, máximo, minutos fuera de rango y carga térmica acumulada.
2. **Asociación lote ↔ sensor por lugar y tiempo.** En cámara, el lote toma la serie del punto B-01 de su zona (21 puntos en total); en ruta, la del termógrafo B-03 de su camión (28 en total). Un tramo sin dato queda marcado como tal y **nunca se rellena**.
3. **Modelo cinético por familia** (lácteos, cecinas, congelados, etc.). Usa la dependencia de la velocidad de deterioro con la temperatura (Arrhenius/Q10), integrada sobre la historia real.
   - Es el principio del sistema SMAS (Koutsoumanis et al., 2005) y del FEFO dinámico en logística de alimentos (Jedermann et al., 2014).
   - El modelo es **determinista**: los parámetros vienen de la literatura y de la ficha del proveedor, y Calidad los aprueba. No es aprendizaje automático.
4. **Cálculo distribuido:**
   - **En el borde:** el gateway B-02 (IoT Greengrass, CD Talca y Concepción) acumula la carga térmica de los lotes en cámara aunque el CD esté 24 h sin enlace.
   - **En el camión:** el terminal C-02 recibe la serie de B-03 por Bluetooth (como ya define el SD4) y resume el tramo sin señal.
   - **En la nube:** N-10 Analítica consolida y recalcula.
   - Es un patrón de **proyección derivada de eventos**: la estimación se puede reconstruir con otra versión del modelo para auditoría.

**Contrato:** `inn03.historia-termica-lote.v1`. Campos: lote, GTIN, familia, tramos (lugar, desde, hasta, sensor, resumen, sin dato), carga acumulada, vida remanente con intervalo y versiones del modelo y de los parámetros.

**Cumplimiento de RT-05.30.** Este requisito valora la analítica predictiva «con el modelo, sus variables, su métrica de desempeño y su plan de reentrenamiento documentados». INN-03 los declara así:

| Elemento | Definición |
|---|---|
| Modelo | Cinética de deterioro por familia (Arrhenius/Q10) integrada sobre la historia térmica del lote. Determinista, no aprendido. |
| Variables | Serie de temperatura por tramo, tiempo en cada tramo, familia del producto, vida útil nominal del proveedor y parámetros cinéticos aprobados. |
| Métrica de desempeño | Proporción de lotes con vida remanente estimada dentro de ±15 % de la vida nominal respecto de la evaluación de Calidad (I-03B). |
| Plan de reentrenamiento | Recalibración semestral de los parámetros por familia con los lotes evaluados del período (INN-03.P5). Recalibración extraordinaria si I-03B baja del 80 % en dos cortes seguidos. |

Al no ser un modelo aprendido, no se aplica el capítulo 18 de las Bases Técnicas (RT-26.06). Igual se declaran línea base, métrica y deriva, como pediría RT-18.08.

### Madurez
- EPCIS 2.0 es un estándar publicado (GS1 AISBL, 2022).
- Los modelos cinéticos de vida útil están validados experimentalmente (Koutsoumanis et al., 2005). Jedermann et al. (2014) documentan FEFO dinámico en logística refrigerada.
- Escala: European Commission (2016). La integración propuesta (borde sin enlace, asociación por eventos y uso por Calidad en Puelche) parte en **TRL 2**.
- Objetivos: **TRL 4 al mes 10** (H4, con series y eventos sintéticos) y **TRL 6 al mes 15** (marcha blanca con lotes reales).

### Incorporación
**Arquitectura:**

| Componente / módulo (SD3 y SD4) | Rol |
|---|---|
| B-01 sensores, B-03 termógrafos | Fuente de las series (ya ofertadas) |
| B-02 gateway IoT | Acumula la carga térmica sin enlace |
| C-02 terminal de reparto | Resume el tramo en ruta |
| N-08 Ingesta IoT, N-06 Telemetría cruda | Ingesta; reutiliza los 10.584 mensajes diarios ya dimensionados |
| Capa 5 | Eventos EPCIS con datos de sensor |
| M9 Calidad y trazabilidad | Muestra la historia y la estimación; Calidad dispone y aprueba los parámetros |
| M2 Inventario / M5 Preparación | Orden de salida sugerido, habilitado por familia |
| M10 Analítica (N-10) | Modelo, recálculo y publicación; series retenidas 5 años |
| Capa 7 | Versionado y aprobación de modelo y parámetros |

| Paquete | Meses | Entregable | Rama EDT |
|---|---|---|---|
| INN-03.P1 | 3–5 | Familias priorizadas (lácteos primero, por la suspensión del proveedor de lácteos; Caso, cap. 13), parámetros aprobados por Calidad y protocolo de validación | Etapa 1 |
| INN-03.P2 | 5–9 | Asociación lote–sensor por eventos EPCIS y cálculo en B-02 y C-02 | Etapa 1 |
| INN-03.P3 | 9–10 | Vista en M9, publicación en N-10 y orden sugerido a M2/M5 (software H4) | Etapa 1 |
| INN-03.P4 | 11–15 | Certificación H5 y validación en marcha blanca contra la evaluación de Calidad | Etapa 1 |
| INN-03.P5 | 16–56 | Revisión semestral de parámetros y extensión a nuevas familias | Operación |

**Materialización:** mes 16, en apoyo a la decisión de Calidad. El orden sugerido se activa por familia cuando esa familia cumple I-03B.

**Responsables:** Líder de Datos (Leandro Chamorro) y Arquitecto de Solución (Bastián Trejo); validación del Líder de Calidad (Maximiliano Miño) y de la jefa de Calidad del CLIENTE.

### Impacto económico (sin montos)
- **Inversión:** HH de datos, borde y Calidad, meses 3–15. La validación con lotes reales puede requerir laboratorio externo; es un rubro de la Oferta Económica.
- **Costo operacional:** cómputo en el borde y en N-10 y revisión semestral, meses 16–56. No agrega hardware ni ingesta.
- **Beneficio, por tres vías:**
  - menos lotes retenidos o descartados sin justificación térmica real;
  - menos rechazos por fecha próxima, porque sale primero lo que tiene menos vida real;
  - ante un rechazo como el del camión de food service, la evidencia de temperatura ya la entrega RF-09.09. La innovación agrega, para cada lote, cuánta vida útil consumió el evento, que es lo que define si se reubica en otro cliente o se descarta.

  No se suma a la meta base de merma (SD2) ni a INN-01.

**Ubicación en el flujo de caja** (sin montos):

| Rubro | Clase (planilla del CLIENTE) | Meses |
|---|---|---|
| HH de datos y Calidad: familias, parámetros y protocolo | Inversión / RR. HH. | 3–5 |
| HH de borde, eventos y vista en M9 | Inversión / RR. HH. | 5–10 |
| Validación con lotes reales (laboratorio externo, si se contrata) | Inversión / proveedores | 11–15 |
| Cómputo en el borde y en N-10 | Operación | 16–56 |
| Recalibración semestral de parámetros | Operación / RR. HH. | 16–56, cada 6 meses |
| Beneficio: retenciones y descartes evitados; rechazos por fecha próxima evitados | Beneficio | Desde el 16; primera medición en el 28 |

### Indicador
| Id | Indicador | Línea base | Meta | Momento |
|---|---|---|---|---|
| I-03A | Lotes de familias priorizadas con historia térmica completa / lotes de esas familias | 0 (no hay registro continuo) | ≥ 95 %; los tramos sin dato se informan con causa | Mes 15 y mensual |
| I-03B | Lotes evaluados con vida remanente estimada dentro de ±15 % de la vida nominal respecto de la evaluación de Calidad / lotes evaluados | Sin medición | ≥ 80 %, con ≥ 60 lotes por familia | Mes 15, por familia |
| I-03C | Excursiones dispuestas por Calidad con la vida útil consumida registrada / excursiones alertadas (RF-09.05) | 0 | 100 % | Desde el mes 16 |
| I-03D | Lotes de familias habilitadas retenidos o descartados en bodega por vencimiento / lotes recibidos de esas familias | Medición de los meses 13–15 | −20 % relativo | Mes 28 |

### Riesgo
| Riesgo | P / I | Mitigación | Contingencia |
|---|---|---|---|
| Parámetros que no representan los productos de Puelche | Media / Alto | Validación por familia (I-03B) antes de habilitar el orden sugerido | La familia queda con historia visible y FEFO por fecha impresa |
| Que Operaciones lea la estimación como permiso para relajar RNG-04 | Media / Alto | La regla graduada y el bloqueo de B-02 no cambian; la estimación solo informa a Calidad | Mostrar la estimación solo en M9, no en M5 |
| Lote movido sin evento (asociación errónea) | Media / Medio | Tramos sin dato explícitos; control de eventos de ubicación en M2 | Lote marcado «historia incompleta», sin estimación |

---

## 13.4 Innovación 4

**Tipo 4, modelo de negocio o de contratación: Tramo variable de la Operación ligado al costo de servir (INN-04).** Durante la Operación, una parte acotada del pago mensual se liga a una mejora verificable del costo por entrega de Puelche. El tramo no se paga si el OTIF baja de su meta.

### Problema
- El costo logístico se prorratea por zona con un criterio de 2016.
- El gerente de finanzas no sabe cuánto cuesta atender a un almacén de Empedrado que compra «cuarenta y cinco mil pesos cada dos semanas» (Caso, cap. 1).
- El SD2 identifica la opacidad del costo de servir como uno de los tres problemas centrales.
- Conocer el costo es obligatorio; que el dato se convierta en decisión comercial no lo es. Con tarifa plana, al proveedor le da lo mismo.
- El área de TI de Puelche son cuatro personas, y toda función que requiera un especialista que la compañía no tiene debe ofrecerse como servicio y estar costeada (Caso, cap. 10, restricción 9). Convertir la segmentación por costo de servir en recomendaciones de malla de atención es análisis de datos que Puelche no tiene quién haga. Por eso esta innovación lo entrega como servicio gestionado de la Operación, costeado dentro del pago mensual y no como una carga para el equipo de TI.

### Deslinde
| Ya es alcance obligatorio | Dónde |
|---|---|
| Costo de servir por cliente y por entrega, desde el hecho | Criterio 11; familia F-14 «Costo de servir», asignada a la Etapa 2 (SD3 §3.2.1); RF-11.01 a RF-11.08 (M10) |
| Segmentación por rentabilidad neta con sugerencia de frecuencia y pedido mínimo | RF-11.08 |
| OTIF único con metas de 90 % (mes 15), 93 % (mes 19) y 95 % (mes 32) | Criterio 4; SD3 §3.2.5, criterio de aceptación R18-04 «Confiabilidad del servicio» |
| **Pago de la Operación con componentes fijos y variables y métricas que afectan el variable** | Bases Adm., estructura de pagos de la Operación; Formulario E-25 |
| Multas por incumplimiento de nivel de servicio | Bases Adm., hito mensual en producción |

**Lo agregado:** las Bases prevén el variable, pero ligado a métricas de **servicio del proveedor**. Esta innovación lo liga a una métrica de **negocio del CLIENTE** (reducción comparable del costo por entrega) con dos protecciones:
- el OTIF debe estar en su meta;
- una canasta congelada impide bajar costos dejando de atender a clientes caros.

### Modelo
- **Estructura:** tarifa fija (mayor parte del pago) + tramo máximo con techo. Los valores se fijan solo en la Oferta Económica.
- **Línea base:** se forma con hechos de los meses 21–23 (la Etapa 2 entra a producción en el mes 21). La canasta se congela por zona, canal, distancia y condición térmica, con pesos fijos.
- **Ajustes:** combustible, mix y septiembre se ajustan con índices documentados antes de liquidar.
- **Puntuación:** reducción comparable / 5 %, acotada a [0, 1]. Se paga solo si el OTIF del período ≥ meta del SD3.
- **Acompañamiento:** LafroX entrega periódicamente la segmentación de RF-11.08 con una recomendación de malla de atención. **Decide el gerente comercial de Puelche.** Se registran la recomendación, la respuesta y el efecto.
- **Lo que no cambia:** no se compensan multas, no se excluyen entregas fallidas del denominador y no se supera el precio máximo.

### Madurez
- **Escala:** TRL de la European Commission (2016), aplicada a la práctica contractual y no a un componente tecnológico. Cada nivel se traduce en un hito verificable del contrato:

| Nivel | Significado en esta innovación | Mes |
|---|---|---|
| TRL 2 | Modelo de pago y regla de atribución formulados (estado actual) | Oferta |
| TRL 4 | Fórmula simulada con casos y aprobada por Finanzas del CLIENTE (INN-04.P1) | 20 |
| TRL 6 | Tres liquidaciones en sombra reproducidas sin diferencia (INN-04.P2) | 23 |
| TRL 7 | Liquidación con efecto de pago aceptada en operación real (INN-04.P3) | 24 |

- **Componentes por separado:**
  - los contratos con pago ligado al nivel de servicio son práctica corriente en servicios de tecnología (TRL 9);
  - ligar el variable a una métrica del **negocio del cliente**, el costo de servir, no lo es, y por eso el conjunto parte en TRL 2.
- **Fuente:** FitzGerald et al. (2023) analizan contratos por resultados. Muestran que la forma en que se especifica el resultado y su lógica de pago determinan si el contrato es liquidable o termina en disputa, y que la especificación débil es el modo de falla más frecuente. Por eso la canasta, los índices y la protección del OTIF se fijan antes de la primera liquidación.

### Incorporación
**Arquitectura:**
- M6 Reparto y M7 Cobranza y rendición aportan los hechos.
- M8 Devoluciones y envases aporta los retornos.
- M10 Analítica calcula el costo comparable y el OTIF sobre N-10.
- La capa 6 versiona la base; la capa 7 audita la cifra liquidada.
- El dato contable definitivo vive en el ERP.

| Paquete | Meses | Entregable | Rama EDT |
|---|---|---|---|
| INN-04.P1 | 17–20 | Reglas de atribución, canasta, índices y traducción a la Oferta Económica | Etapa 2 |
| INN-04.P2 | 21–23 | Línea base y tres liquidaciones en sombra, sin efecto de pago | Operación |
| INN-04.P3 | 24–56 | Liquidación mensual y acompañamiento comercial | Operación |

**Materialización:** acompañamiento desde el mes 21; primera liquidación en el mes 24. **Responsable:** Jefe de Proyecto (Alex Aravena); Finanzas y contraparte técnica del CLIENTE.

### Impacto económico (sin montos)
- **Estructura:** fijo en los 36 meses + tramo con techo. El tramo vale 0 en los meses 21–23; desde el 24 se paga la puntuación × tramo máximo, a mes vencido (E-25).
- **Para Puelche:** paga menos si la solución no rinde y nunca más del máximo.
- **Para LafroX:** el tramo es ingreso contingente.
- **Beneficio:** ahorro operacional verificable, sin sumar lo ya atribuido a INN-01, INN-03 o INN-05.

**Ubicación en el flujo de caja** (sin montos). Al ser tipo 4, se separa lo que es costo de lo que es ingreso de LafroX:

| Rubro | Clase (planilla del CLIENTE) | Meses |
|---|---|---|
| HH de diseño de la atribución, canasta e índices | Inversión / RR. HH. | 17–20 |
| HH del ensayo en sombra | Inversión / RR. HH. | 21–23 |
| Servicio de acompañamiento comercial (restricción 9) | Operación / RR. HH. | 21–56 |
| Conciliación mensual con Finanzas | Operación / gasto administrativo | 24–56 |
| Ingreso de LafroX: pago fijo | Ingreso | 21–56 |
| Ingreso de LafroX: tramo variable | Ingreso contingente; vale 0 en 21–23 | 24–56, a mes vencido |
| Beneficio del CLIENTE: reducción del costo por entrega | Beneficio | Desde el 24; meta en el 36 |

### Indicador
| Id | Indicador | Línea base | Meta | Momento |
|---|---|---|---|---|
| I-04A | 1 − costo comparable del período / costo de referencia | Canasta de los meses 21–23 | ≥ 5 %, con OTIF ≥ 95 % | Mes 36; mensual desde el 24 |
| I-04B | Liquidaciones reproducidas por Finanzas sin diferencia / liquidaciones en sombra | Sin modelo | 3 de 3 | Meses 21–23 |
| I-04C | Recomendaciones con respuesta y efecto registrado / recomendaciones | Sin registro | 100 % | Desde el mes 21 |

### Riesgo
| Riesgo | P / I | Mitigación | Contingencia |
|---|---|---|---|
| Variación del costo por causas externas (combustible, cambio de malla, septiembre) | Alta / Alto | Canasta, índices y regla estacional fijados en P1, antes de la primera liquidación | Acotar el tramo al cumplimiento del OTIF, que es atribuible, y mantener el acompañamiento en la tarifa fija |
| Bajar el costo degradando el servicio o excluyendo clientes | Media / Alto | Protección del OTIF; denominador sin exclusiones; reproducción por Finanzas | Suspender el devengo del período en disputa según el contrato |

---

## 13.5 Innovación 5

**Tipo 5, experiencia de usuario, sostenibilidad o impacto social: Hoja de negocio del almacenero (INN-05).** Una hoja por local, entregada en la visita, que devuelve al cliente del canal tradicional la información que Puelche ya tiene sobre sus compras, sin exigirle dispositivo, conexión ni registro.

### Problema
- Son 11.600 almacenes y minimarkets.
- El cliente del canal tradicional no tiene internet ni teléfono adecuado (Caso, cap. 10, restricción 5), y el 38 % de la venta del canal se paga en efectivo.
- Un competidor ofrece una aplicación donde el almacenero hace su pedido solo (Caso, cap. 1).
- Puelche sabe qué compra cada local, qué dejó de pedir y qué tiene por vencer, pero no se lo devuelve.

### Deslinde
| Ya es alcance obligatorio | Dónde |
|---|---|
| Segmentación por rentabilidad, construida **para** Comercial y Finanzas | RF-11.08 (M10, Etapa 2) |
| Autoatención de saldo, pedido y última entrega | RT-16.32 |
| Portal web con estado de cuenta, saldo, entregas y documentos (requiere sesión e internet) | RF-07.06, RF-12.15 a RF-12.18 |
| Personas usuarias con baja alfabetización digital | Bases Adm., Art. 26° |
| Comprobante de entrega | Criterio 8 |

**Lo agregado:** una lectura **de su propio negocio con Puelche**, entregada por el canal que el cliente ya usa (la visita). El costo de acceso lo asume Puelche.

### Tecnología
**Cuatro bloques:**
1. Qué compró, por categoría, contra su período anterior.
2. Qué dejó de pedir: productos habituales ausentes hace 2 o 3 ciclos.
3. Qué tiene por vencer. Viene de INN-01 y se omite si no hay datos confirmados.
4. **Opcional y condicionado:** cómo le va frente al agregado de locales comparables de su zona.
   - Nunca muestra un local identificable.
   - Aplica umbral mínimo de locales por grupo y supresión de celdas, según el control de divulgación estadística (Hundepool et al., 2026) y la k-anonimidad (Sweeney, 2002).
   - Se activa solo después de una revisión legal bajo la Ley 21.719.

**Entrega:**
- **En pantalla:** M3 la muestra en el terminal del preventista (C-01). Se calcula antes de la ruta y viaja cifrada, así que funciona sin señal.
- **Impresa, si el cliente la pide:** M6 la imprime con la impresora de cabina del camión (Zebra ZQ620, una por camión; T-11) y se entrega con la guía en la **entrega siguiente**. El preventista no lleva impresora.
- **Si esa semana el local no hace pedido,** no hay entrega y la copia impresa no llega. La copia queda pendiente para la próxima entrega a ese local, y la hoja en pantalla sí se mostró en la visita. I-05A mide aparte las copias pedidas y las entregadas, para que esta brecha sea visible.

### Madurez
- El informe sobre datos propios y el control de divulgación están en **TRL 9** (Hundepool et al., 2026; Sweeney, 2002).
- Su utilidad para el micro-comercio sin conectividad no está probada: el conjunto parte en **TRL 2**.
- Objetivos: TRL 4 con la prueba de comprensión (meses 13–14) y TRL 6 en la marcha blanca de la Etapa 2 (meses 19–20).

### Incorporación
**Arquitectura:**
- M10 Analítica calcula los bloques en N-10 (capa 6).
- M3 Preventa los muestra en C-01.
- M6 Reparto imprime la copia en la cabina.
- La capa 7 limita la hoja al receptor y audita el tratamiento (registro de actividades del Art. 27°).

| Paquete | Meses | Entregable | Rama EDT |
|---|---|---|---|
| INN-05.P1 | 13–14 | Prototipo en papel y pantalla; prueba de comprensión con 24 locales | Etapa 2 |
| INN-05.P2 | 14–15 | Privacidad (Ley 21.719), verificación del receptor, retención e impresión en cabina | Etapa 2 |
| INN-05.P3 | 15–17 | Cálculo, precarga y bloques 1–3 (software H9) | Etapa 2 |
| INN-05.P4 | 18–26 | Certificación H10, marcha blanca 19–20, producción 21 y despliegue gradual por rutas | Etapa 2 → Operación |
| INN-05.P5 | 24–27 | Bloque 4: revisión legal, parámetros de agrupación y activación condicionada | Operación |

**Materialización:** mes 21 (bloques 1–3); bloque 4 desde el mes 27 si se aprueba. **Responsable:** Líder de Implantación y Gestión del Cambio (Patricio Henríquez); Encargado de Seguridad para la privacidad.

### Impacto económico (sin montos)
- **Inversión:** investigación con usuarios, diseño y privacidad, meses 13–18.
- **Costo operacional:** cálculo mensual, minutos de explicación y papel térmico de las copias pedidas, meses 21–56. La impresora ya está ofertada.
- **Beneficio comercial:** frecuencia y tamaño del pedido en los locales que la reciben, y retención frente al competidor con aplicación. Se valoriza solo si se demuestra al mes 33.
- **Beneficio social:** la información de gestión deja de ser privilegio del cliente grande.

**Ubicación en el flujo de caja** (sin montos):

| Rubro | Clase (planilla del CLIENTE) | Meses |
|---|---|---|
| Investigación con usuarios y prueba de comprensión | Inversión / RR. HH. | 13–14 |
| HH de privacidad, cálculo, precarga e impresión en cabina | Inversión / RR. HH. | 14–18 |
| Revisión legal del bloque 4 | Inversión / proveedores | 24–27 |
| Cálculo mensual y papel térmico de las copias pedidas | Operación | 21–56 |
| Minutos de explicación en la visita | Operación (tiempo de preventa) | 21–56 |
| Beneficio: efecto en frecuencia y tamaño del pedido, si se demuestra | Beneficio | Desde el 33 |

### Indicador
| Id | Indicador | Línea base | Meta | Momento |
|---|---|---|---|---|
| I-05A | Locales con hoja mostrada en la visita / locales elegibles que aceptan. Submedida: copias impresas entregadas / copias pedidas | 0 | ≥ 90 % de hojas mostradas; ≥ 85 % de copias entregadas dentro de dos ciclos de visita; también se informa sobre los 11.600 | Mes 27 |
| I-05B | Participantes que interpretan bien 3 preguntas / participantes | Prototipo de los meses 13–14 | ≥ 80 % de 24 | Antes del mes 19 |
| I-05C | Frecuencia y tamaño de compra en rutas con hoja frente a rutas aún sin hoja | Período previo por ruta | Estimar el efecto; no se promete un alza | Mes 33 |
| I-05D | Emisiones del bloque 4 con todos los grupos ≥ umbral / emisiones del bloque 4 | No aplica antes de activar | 100 % | Cada emisión |

### Riesgo
| Riesgo | P / I | Mitigación | Contingencia |
|---|---|---|---|
| Inferir las cifras del vecino a partir del bloque 4 | Media / Muy alto | Umbral y supresión verificados en cada emisión; revisión legal previa | No activar el bloque 4; los bloques 1–3 son datos propios, sin riesgo de divulgación |
| Que el almacenero no la lea o no la entienda | Media / Medio | Prueba de comprensión (I-05B) | Versión de un bloque, explicada de palabra en la visita |

---

## Vista para la EDT del SD7

| Rama | Paquetes | Meses |
|---|---|---|
| Gestión del Proyecto y Calidad | INN-02.P1–P3 | 2–10 |
| Etapa 1 | INN-01.P1–P4, INN-03.P1–P4 | 3–15 |
| Etapa 2 | INN-04.P1, INN-05.P1–P4 | 13–26 |
| Operación | INN-02.P4, INN-03.P5, INN-04.P2–P3, INN-05.P4–P5 | 11–56 |

**Cambios que necesita el SD7 actual:**
- Cambiar la Innovación 3 por INN-03.
- Usar los nombres nuevos.
- Escribir las etapas con los meses del Art. 17° (desarrollo 1–12 / marcha blanca 13–15 / producción 16; desarrollo 13–18 / marcha blanca 19–20 / producción 21), en lugar de «Etapa 1 (Mes 1 al 15)».

---

## Inconsistencias de los SD1–SD4 que tocan a las innovaciones

1. **Nombres de módulos.**
   - El SD3 y su T-12 usan «M7 Cobranza y rendición», «M8 Devoluciones y envases», «M9 Calidad y trazabilidad» y «M12 Telemetría».
   - La tabla de correspondencia del SD4 §4.2 usa «M7 Rendición», «M8 Devoluciones», «M9 Calidad» y «M12 Flota».
   - Este documento usa los del SD3. Hay que unificarlos en el SD4.
2. **Tecnología de desarrollo.** El SD1 §1.5 dice «monolito modular en Python/Django», y el SD4 dice Laravel (PHP) y Kotlin. INN-02 usa las del SD4.
3. **RT-26.08 «no ofertado» en el T-12.** INN-01, INN-02 e INN-03 miden su beneficio antes del mes 16, así que se podría ofertar. Decidir si se cambia en el T-12.
4. **Meta base de merma ≤ 1,0 % (SD2, Tabla 2.1).** Ninguna innovación puede contarla como beneficio propio. Ya está separada en INN-01 e INN-03.
5. **RT-05.30 «no ofertado» en el T-12.** INN-03 ahora lo declara ofertado y lo cumple: modelo, variables, métrica y plan de reentrenamiento. **Hay que cambiar esa fila del T-12 a «Ofertado mediante INN-03»**; si no, el S13 y el T-12 se contradicen.
6. **Ninguna innovación aparece en el SD3, su T-12 ni el SD4.** El profesor lo observó en el Informe 1 (RT-26.01). Como mínimo: requisitos de las innovaciones en el T-12 y sus contratos (`inn01` a `inn05`) en el catálogo de interfaces del SD4 §4.1.6.
7. **RF-09.06 en el consolidado de RF (CSV) frente al SD3.** El CSV dice que el sistema permitirá «al conductor bloquear el despacho del camión según su criterio». El SD3, su T-12 y RF-09.10 (propio LafroX) dicen retención preventiva y disposición de Calidad. El profesor ya marcó esta contradicción en el Informe 1 («bloqueo automático (S4.1) contra decisión del conductor (S3)»). INN-03 cita la versión del SD3. Hay que corregir el CSV o declararlo superado.
8. **RF-08.05 en el CSV:** su resultado esperado habla de «pérdida de envases», no de merma por vencimiento. Es un error de copia del catálogo; no afecta a INN-01, pero conviene corregirlo.

## Decisiones pendientes del equipo
- Techo del tramo de INN-04 (va en la Oferta Económica).
- Familias priorizadas y laboratorio para validar INN-03.
- Umbral mínimo de locales por grupo para el bloque 4 de INN-05.
- Verificar contra el original las referencias nuevas (GS1 2022, Koutsoumanis 2005, Jedermann 2014, Ley 21.719).

## Referencias
- DORA. (2024). *Accelerate state of DevOps report 2024*. Google Cloud. https://dora.dev/research/2024/dora-report/
- European Commission. (2016). Technology readiness levels (TRL). En *Horizon 2020 work programme 2016–2017: General annexes* (Anexo G). https://ec.europa.eu/research/participants/data/ref/h2020/other/wp/2016_2017/annexes/h2020-wp1617-annex-g-trl_en.pdf
- FitzGerald, C., Tan, S., Carter, E., & Airoldi, M. (2023). Contractual acrobatics: A configurational analysis of outcome specifications and payment in outcome-based contracts. *Public Management Review, 25*(9), 1796–1814. https://doi.org/10.1080/14719037.2023.2244501
- GS1 AISBL. (2022). *EPC Information Services (EPCIS) standard* (versión 2.0). https://ref.gs1.org/standards/epcis/2.0.0/
- Hundepool, A., Domingo-Ferrer, J., Franconi, L., Giessing, S., Lenz, R., Naylor, J., Schulte Nordholt, E., Seri, G., De Wolf, P.-P., Tent, R., Młodak, A., Gussenbauer, J., & Wilak, K. (2026). *Handbook on statistical disclosure control* (2.ª ed.). Center of Excellence SDC. https://sdctools.github.io/HandbookSDC/
- Jedermann, R., Nicometo, M., Uysal, I., & Lang, W. (2014). Reducing food losses by intelligent food logistics. *Philosophical Transactions of the Royal Society A, 372*(2017), 20130302. https://doi.org/10.1098/rsta.2013.0302
- Koutsoumanis, K., Taoukis, P. S., & Nychas, G.-J. E. (2005). Development of a Safety Monitoring and Assurance System for chilled food products. *International Journal of Food Microbiology, 100*(1–3), 253–260. https://doi.org/10.1016/j.ijfoodmicro.2004.10.024
- Ley N.º 21.719 de 2024. Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales. Diario Oficial, 13 de diciembre de 2024. https://www.bcn.cl/leychile/navegar?idNorma=1209272
- Riesenegger, L., Santos, M. J., Ostermeier, M., Martins, S., Amorim, P., & Hübner, A. (2023). Minimizing food waste in grocery store operations: Literature review and research agenda. *Sustainability Analytics and Modeling, 3*, 100023. https://doi.org/10.1016/j.samod.2023.100023
- Shahin, M., Babar, M. A., & Zhu, L. (2017). Continuous integration, delivery and deployment: A systematic review on approaches, tools, challenges and practices. *IEEE Access, 5*, 3909–3943. https://doi.org/10.1109/ACCESS.2017.2685629
- Sweeney, L. (2002). k-anonymity: A model for protecting privacy. *International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems, 10*(5), 557–570. https://doi.org/10.1142/S0218488502001648
