# Análisis del Subdocumento 4.2 — Arquitectura física y de despliegue

**Licitación TFEP-01/2026 · Caso 02 — Logística (Distribuidora Puelche S.A.) · LafroX**
**Objeto:** revisión de contenido, coherencia interna, legibilidad y cumplimiento de los requisitos transversales del Subdocumento 4.2.
**Archivo intervenido:** `04_arquitectura/entrega_2/texto/arquitectura_fisica.md`
**Archivo de referencia (no editado):** `04_arquitectura/entrega_1/texto/arquitectura_fisica.md`
**Ponderación T-21:** 16 % del Informe 1 · 12 % del Informe 2 · 10 % de la propuesta final.

> La Entrega 1 es registro congelado de lo entregado el 07-09-2026 y no se edita (regla 6 del `CLAUDE.md`). Todas las correcciones se aplicaron sobre `entrega_2/`, que antes de esta intervención era copia byte a byte de la Entrega 1.

---

## 1 · Resumen del resultado

El subdocumento es técnicamente sólido: 15 decisiones de arquitectura fundadas con alternativas y criterio, emplazamiento híbrido real, operación desconectada resuelta a nivel de componente, dimensionamiento derivado de la volumetría del caso y no de promedios, y 173 códigos RT citados sin uno solo inventado. El problema no era el contenido de ingeniería: eran **cuatro defectos que lo desacreditaban** y una estructura que lo volvía ilegible.

| Defecto | Alcance | Estado |
|---|---|---|
| Disponibilidad del recinto por debajo de la exigida | 3 pasajes, contradicción con el Subdoc 2 | Corregido |
| Siete celdas del numeral 14.2 sin cerrar, una de ellas admitida en el propio texto | Bloqueante G7 sobre un ítem de 16 % | Cerrado con las 16 dimensiones |
| Notas de auditoría interna, historial de versiones y «proponente pendiente de definir» | 6 pasajes | Retirados |
| Citas normativas a números de línea en lugar de artículos | 4 pasajes | Corregidos |
| Jerarquía de encabezados plana: 208 títulos al mismo nivel | Todo el documento | Reestructurado a 3 niveles |

Cobertura de requisitos: **118 de los 161 requisitos obligatorios** de los capítulos que este subdocumento responde están respondidos (73 %). Sumando los dos obligatorios pendientes del Capítulo 05, quedan 45 sin respuesta: a 26 de ellos solo les falta la cita del código, y 19 exigen contenido nuevo, de los cuales 9 son de este subdocumento. El detalle está en la sección 5.

---

## 2 · Correcciones de contenido

### 2.1 Disponibilidad del recinto: se ofrecía menos de lo exigido

El numeral 6.1 de las Transversales abre con una exigencia sin matices: *«el PROPONENTE deberá habilitar un recinto técnico […] con un nivel de disponibilidad de infraestructura de 99,95 %»*, y la tabla del numeral 7.2 la desglosa por componente —energía del recinto, climatización, red, servidores, motor de base de datos y portal—, todos en 99,95 % mensual mínimo.

El documento declaraba la sala de CD Talca en **TIER II, equivalente a 99,741 %** (≈ 22,7 h de corte al año), y lo defendía en tres lugares distintos argumentando que la clasificación del recinto es un medio y no el compromiso contractual. El argumento tiene asidero —el propio numeral 7.2 dice que lo penalizable es el Artículo 78°— pero no salva la exigencia del 6.1, y además **contradecía frontalmente al Subdocumento 2**, que afirma que el Capítulo 6 «exige un nivel de disponibilidad de infraestructura del 99,95 %» y lo alinea con los principios Tier III.

**Corrección aplicada.** Se retiró la clasificación de tercero —las Bases no piden certificación de nivel, sino cumplimiento verificable de cada requisito individual, y el Subdoc 2 ya lo dice así— y se comprometió el 99,95 % mensual por componente, con la redundancia que lo sostiene. Se mantuvo explícita la distinción respecto del Artículo 78°, que es correcta y conviene conservar.

### 2.2 Tipología del recinto mal declarada

El numeral 6.1 obliga a declarar expresamente la tipología de cada sitio y distingue tres: sala técnica principal (aplica RT-06.01 a RT-06.24 íntegros), sala técnica secundaria o de sitio (régimen proporcional) y gabinete o borde operacional.

El documento rotulaba el CD Talca como **«Sala Técnica Secundaria»** y a la vez titulaba su apartado **«Data Center Primaria»**, mientras declaraba cumplir RT-06.01 a RT-06.34 completos. Es decir: entregaba nivel de sala principal bajo etiqueta de sala secundaria. A eso se sumaban tres lecturas incompatibles del mismo recinto entre subdocumentos (el Subdoc 2 pide una sala secundaria en Talca; el supuesto del Subdoc 3 pone la principal en Talca y la secundaria «en otro recinto»).

**Corrección aplicada.** Talca queda declarado como **sala técnica principal**, con el fundamento de que aloja el núcleo —motor de almacenes, base transaccional, broker, capa anticorrupción, caché de identidad, telemetría y respaldo local—, que es literalmente el criterio del numeral 6.1. Concepción y las tres plataformas de cross-docking conservan su tipología de gabinete de borde, que ya era correcta.

### 2.3 El sitio secundario del Capítulo 7 no estaba argumentado

El numeral 7.1 exige un sitio secundario **en dependencias distintas**, con replicación en línea y características equivalentes a las del principal en los servicios críticos. El documento describía tres polos (Talca activo, Concepción activo autónomo, región us-east-1 pasiva) sin decir nunca cuál de ellos satisface el 7.1, lo que dejaba al evaluador decidiendo si la propuesta tiene sitio secundario físico o lo reemplaza por una región de nube.

**Corrección aplicada.** Se añadió el argumento explícito: dos sitios secundarios, uno por dominio del despliegue híbrido —CD Concepción para el componente on-premise y la región us-east-1 para la carga principal en nube—, porque la carga crítica vive en ambos dominios. Y se subió al frente la modalidad declarada y justificada que exige RT-07.01.

### 2.4 Numeral 14.2: siete celdas sin cerrar, una admitida en el texto

El bloqueante G7 trata la celda vacía del 14.2 como dimensionamiento no realizado. El documento abría su apartado de dimensionamiento afirmando «sin celdas vacías» y doscientas líneas después decía textualmente: *«su traducción a mensajes por día es una de las celdas que debe cerrarse (hallazgo D1 de la auditoría de coherencia del Subdocumento 4)»*.

Estaban sin declarar: transacciones por segundo en el peak de la ventana de despacho, personas usuarias registradas, volumen anual de evidencia de entrega, volumen anual de series de temperatura y posicionamiento, volumen de mensajes por integración, contactos mensuales a la mesa de ayuda y dotación de la mesa. Otras tres estaban correctas pero desplazadas al Subdocumento 5.

**Corrección aplicada.** Se añadió al apartado (k) una tabla con **las dieciséis dimensiones**, cada una con valor, método y supuesto, y al apartado (h) el **desglose de mensajes por integración** con su derivación. Dos hallazgos de ingeniería salieron del ejercicio y quedaron incorporados al texto:

- El volumen de mensajes está dominado por las dos series de tiempo: ≈ 112.000 de ≈ 150.000 mensajes diarios son trazabilidad y telemetría, que por diseño no atraviesan la base transaccional.
- La ventana crítica de despacho **no es la de mayor carga**: son ≈ 1,7 TPS en ráfaga contra los ≈ 20 TPS del picking nocturno. Es crítica por indisponibilidad cero, no por volumen. Esto explica y refuerza la decisión de dimensionar el cómputo contra la preparación nocturna y la resiliencia contra la ventana de despacho.

Los valores nuevos (dotación de mesa con Erlang C, volúmenes de evidencia y de series, usuarias registradas, históricos a migrar) **deben validarse con el equipo antes de la entrega**: son derivaciones defendibles de la volumetría del caso, no cifras acordadas.

### 2.5 Citas normativas erróneas

| Cita en el documento | Qué era en realidad | Corrección |
|---|---|---|
| «BA Art. 462» (2 veces) | La línea 462 del archivo de las Bases, no un artículo. El texto citado pertenece al **Art. 27°** (cumplimiento normativo, auditoría y derecho de inspección) | Art. 27° |
| «(L577)» (2 veces) | La línea 577 del archivo del caso. Es la **Restricción no negociable N° 10** (objeción sindical a cámaras en cabina y control de jornada por GPS) | Restricción N° 10 del Cap. 10 |
| «Art. 10° de las Bases Administrativas» para calificar una observación grave | El Art. 10° regula el cómputo de plazos | Numeral 5.4 de las Transversales |
| «BA Art. 5° (capacidad analítica como servicio horizontal)» | El Art. 5° es el orden de precedencia de los documentos | Retirada |
| «Art. 39° (acceso y exportación de datos)» | El Art. 39° es la documentación administrativa obligatoria | Retirada |
| «Cap. 5 (innovación obligatoria de análisis predictivo)» | El Cap. 5 es la exigencia de innovación (Art. 28° a 30°) y no obliga a analítica predictiva | Retirada, ver 2.6 |

Las dos primeras son las más costosas: un evaluador que busque el artículo 462 en un documento de 94 artículos concluye que la propuesta cita sin verificar.

### 2.6 Contradicción sobre inteligencia artificial

El apartado de capa analítica invocaba una «innovación obligatoria de análisis predictivo» inexistente en las Bases, mientras la **Decisión N° 52** del registro y la arquitectura lógica declaran lo contrario: la solución **no incorpora inteligencia artificial ni analítica predictiva**, con declaración fundada, como permite RT-18.01, y el ruteo se resuelve con optimización determinística auditable.

**Corrección aplicada.** El apartado ahora declara el alcance en positivo: la capa analítica queda preparada —lago columnar y almacén analítico— y la renuncia a IA y a analítica predictiva se argumenta con el dato del caso (41 % de recepciones sin lote, 2,3 % de diferencia de inventario: predecir sobre esa base produce confianza injustificada). Es una renuncia razonada, y presentarla así vale más que insinuar una capacidad que la propuesta no ofrece.

> **Consecuencia para otros subdocumentos.** La tabla de emplazamiento del Subdocumento 3 sigue ubicando «componentes de IA» en nube pública. Esa línea contradice la Decisión N° 52 y hay que retirarla. Mientras exista, ISO/IEC 42001 pasaría a ser exigible por RT-15.02, que la condiciona precisamente a que la solución incorpore componentes de IA.

### 2.7 Colisiones de identificador

El documento usaba una serie «D-N» que no coincidía con el registro de 60 decisiones del Subdocumento 3, de modo que el mismo identificador designaba dos cosas distintas:

| Cita | Significaba aquí | Significa en el registro del Subdoc 3 |
|---|---|---|
| D6 | Identidad Modelo B (ADR-06) | Gestión de pagos en efectivo |
| D8 | Puerta de enlace de servicios (ADR-13) | Asignación de inventario concurrente |
| D13 | Gestión de secretos (ADR-15) | Monitoreo y objeción sindical |
| D14 | Plataforma de observabilidad (ADR-14) | Destino del WMS de 2013 |

Además, **nueve pasajes citaban decisiones propias como si pertenecieran al numeral 16.1 del caso**, que tiene exactamente dieciséis: «Decisión 16.1 N° 17, 18, 26, 27, 28, 30, 34, 35». Es un error caro por dónde cae: la columna de origen es lo que la evaluación premia, y atribuirse al caso decisiones propias disimula el trabajo adicional en lugar de exhibirlo —el caso dice expresamente que evaluará favorablemente al proponente que encuentre vacíos no listados.

**Corrección aplicada.** Una sola serie: **ADR-NN** para decisiones de arquitectura, **Decisión N°** para el registro del Subdoc 3, con nota de que las dieciséis primeras son las del 16.1. Las citas válidas (N° 4, N° 11 y N° 14) se precisaron como «numeral 16.1 del caso, decisión N° x». Las series de componente (`VM-`, `D-`, `E-`, `B-`, `N-`, `A-`, `C-`, `R-`) se conservan porque son identificadores de inventario físico, y ahora están explicadas en las convenciones de apertura.

### 2.8 Notas de trabajo que llegaron al entregable

Seis pasajes eran notas internas, no propuesta. El más grave abría el registro de decisiones:

> *«Cambios v01 → v02 (cierre de la auditoría del Subdocumento 4). (1) Se corrigen las cinco menciones a Kong en ADR-01, ADR-06 y ADR-11 […] (2) Se incorporan ADR-13, ADR-14 y ADR-15, que existían como decisiones lógicas sin ADR propio, incumpliendo el apartado 7 del Subdocumento 4 y RT-02.04. (3) […] Empresa proponente: Pendiente de definir.»*

En cuatro líneas le decía al evaluador que una versión anterior nombraba otro producto cinco veces, que incumplía RT-02.04, y que el proponente está por definir en un documento enteramente marcado LafroX. Los otros cinco: la resolución «SEC-01» con su «planteamiento original» y la frase *«no es admisible dejarlo como está: un componente de seguridad sin emplazamiento incumple el Art. 16.2»*; la «Nota (2026-09-06)» que cerraba el «hallazgo D2»; la «Discrepancia resuelta» del token de acceso; el contexto del ADR-15 narrando la corrección de una versión previa; y el código de rúbrica interna «(P5.10)».

**Corrección aplicada.** Los seis se reescribieron como declaraciones de diseño en presente, conservando íntegro el fundamento técnico y eliminando el historial. La decisión sobre el gestor de secretos, por ejemplo, ahora se argumenta por lo que aporta —servicio administrado, sin máquina virtual adicional ni carga de administración para un equipo de cuatro personas, Art. 16.3— en lugar de narrar que una versión anterior tenía un componente sin emplazamiento.

### 2.9 Punteros, erratas y autorreferencias

- **Cadena de referencia rota.** El apartado (d) remitía el detalle de los 14 recintos «a la sección de Arquitectura de Seguridad, §12», y esa §12 remitía a su vez a «la sección de Arquitectura de Seguridad, §12». El plano de distribución interna que exige RT-06.03 no estaba en ninguna de las dos.
- **Punteros a documentos de trabajo no entregados:** «Tabla de Emplazamiento v06», «Arquitectura Lógica v6.2» (5 veces), «AL v1» (3), «Dimensionamiento on-premise v05 §8.4», «Cloud v3.6», «§4.5 Cloud», «S14». Un evaluador no puede seguir ninguna.
- **Puntero autocontradictorio:** la visión general remitía «el dimensionamiento explícito de la volumetría del numeral 14.2 al Subdocumento 5», cuando ese dimensionamiento está en este mismo subdocumento.
- **Erratas:** `ADr-12`, `ERp-sync`, «modulo», «ventanas de taking».

Todo corregido: los punteros externos apuntan ahora a los apartados de esta parte o al Subdocumento 4.1 sin número de versión, y las autorreferencias circulares se resolvieron.

---

## 3 · Estructura y legibilidad

El defecto de legibilidad no era el tamaño: era que **el documento no tenía jerarquía**. Los 208 encabezados de tercer nivel estaban todos al mismo rango, de modo que en cualquier índice automático «ADR-01 — Estilo Arquitectónico» aparecía como hermano de «1. Contexto y Problema», y esa misma entrada «1. Contexto y Problema» se repetía quince veces. Un lector no podía saber si estaba en una sección o en una subsección.

| Métrica | Entrega 1 | Entrega 2 |
|---|---|---|
| Encabezados de 2.º nivel | 14 | 16 |
| Encabezados de 3.er nivel | 208 | 74 |
| Encabezados de 4.º nivel | 0 | 48 |
| Índice legible | no | sí |
| Mapa de navegación | no | sí, con origen normativo por apartado |

Cuatro cambios estructurales:

1. **Un solo esquema de rotulación, (a) a (n).** El documento mezclaba las letras del Formulario T-21 —(a) a (e)— con «Apartado 3 del Subdocumento 4 (T-22)», «Apartado 6», y dos secciones sin rótulo (niveles de servicio y operación desconectada). Además, **dos secciones distintas se declaraban «Apartado 7»**: la capa analítica y el registro de decisiones. Ahora las catorce secciones de contenido van de (a) a (n) y la tabla de apertura dice qué exigencia responde cada una.
2. **Los 75 encabezados repetidos de los ADR pasaron a entradillas en negrita.** Las cinco subsecciones de cada decisión —contexto, alternativas, criterio, decisión, consecuencias— ya no son títulos: son párrafos rotulados. El índice del registro pasó de 90 entradas a 15.
3. **Las subsecciones numeradas con dos niveles bajaron a cuarto nivel.** 54 encabezados del tipo «3.1», «4.2», «10.5» estaban al mismo rango que «3.», «4.», «10.».
4. **Las ocho tablas de cierre repetidas se consolidaron.** Cada uno de los cuatro apartados grandes terminaba con las mismas dos tablas —«Referencias cruzadas con las decisiones de arquitectura» y «Trazabilidad normativa (resumen)»—, obligando a recorrer el documento completo para reconstruir la trazabilidad. Ahora están juntas en el apartado (n), agrupadas por apartado de origen.

Se añadió además una apertura, **«Cómo leer esta parte»**, con la tabla de correspondencia entre secciones y exigencias y las convenciones de referencia: qué significa «§N», qué serie de identificadores designa qué, y qué prefijo de componente corresponde a qué tipo de equipo. Es la pieza que faltaba para que un documento de este tamaño sea navegable.

---

## 4 · ¿Es necesaria esta longitud?

**El texto sí; las planillas, no del todo.** El documento pasó de 1.845 a 1.891 líneas, pero eso incluye tres adiciones sustantivas: el mapa de navegación, la tabla de las dieciséis dimensiones del 14.2 y el desglose de mensajes por integración. Descontadas esas, el texto se redujo.

La longitud del texto está justificada por lo que el T-21 mete dentro de este solo ítem: cinco especificaciones propias más cinco apartados del T-7, incluidos quince ADR completos. No hay aquí relleno que cortar: cada apartado responde una exigencia distinta y verificable.

Donde sí hay redundancia real es en **las 115 planillas**, y no la pude resolver editando el texto porque las tablas viven en los siete `.xlsx`. Tres frentes concretos, en orden de rendimiento:

| Consolidación propuesta | Tablas hoy | Tablas después | Qué se gana |
|---|---|---|---|
| Referencias cruzadas y trazabilidad normativa de los apartados (h), (i), (j), (k) → una sola matriz | 8 (40, 41, 60, 61, 70, 71, 87, 88) | 1 | Se lee la trazabilidad completa en un lugar; hoy son 73 filas repartidas en cuatro apartados |
| Apartado (l), listas de requerimientos y conteos de cobertura | 12 (89–103) | 4 | Las tablas 91 a 94 y 102 a 103 replican el catálogo del Subdoc 3 y su conteo; en una parte física basta el mapeo requerimiento → componente |
| Tablas 27 y 28 (componentes de sala y de sitio secundario) → integrar al inventario del apartado (c) | 2 + 4 del (c) | 4 | El inventario está hoy en dos lugares con criterios distintos |

Efecto estimado: **de 115 a ≈ 95 tablas** sin perder un dato. Requiere editar los `.xlsx`, operación que dejo propuesta y no ejecutada: al fusionar hojas hay que decidir qué columnas sobreviven, y esa es una decisión del equipo.

---

## 5 · Cumplimiento de los requisitos transversales

Medido sobre el subdocumento completo —texto más las 115 planillas—, contra los capítulos que el 4.2 responde. Se cuentan solo los requisitos de carácter **Obligatorio**; los deseables y los «según caso» se omiten de la cuenta.

| Cap. | Materia | Obligatorios | Respondidos | Obligatorios sin respuesta |
|---|---|---|---|---|
| 02 | Arquitectura de referencia | 12 | 9 | RT-02.05 · RT-02.10 · RT-02.13 |
| 03 | Modelo híbrido nube / on-premise | 19 | 18 | RT-03.04 |
| 04 | Ambientes y entrega continua | 12 | 7 | RT-04.03 · RT-04.04 · RT-04.10 · RT-04.11 · RT-04.12 |
| 06 | Site principal on-premise | 31 | 23 | RT-06.02 · RT-06.06 · RT-06.09 · RT-06.19 · RT-06.22 · RT-06.30 · RT-06.31 · RT-06.33 |
| 07 | Site secundario y recuperación ante desastres | 12 | 10 | RT-07.12 · RT-07.13 |
| 08 | Hardware, puestos de trabajo y terreno | 17 | 8 | RT-08.01 · RT-08.02 · RT-08.06 · RT-08.07 · RT-08.09 · RT-08.10 · RT-08.16 · RT-08.17 · RT-08.18 |
| 09 | Desempeño, capacidad y escalabilidad | 8 | 8 | — |
| 10 | Disponibilidad, continuidad y resiliencia | 7 | 4 | RT-10.03 · RT-10.04 · RT-10.06 |
| 11 | Seguridad de la información | 25 | 20 | RT-11.06 · RT-11.12 · RT-11.23 · RT-11.24 · RT-11.26 |
| 12 | Identidad, acceso y sesiones | 10 | 7 | RT-12.02 · RT-12.03 · RT-12.08 |
| 14 | Observabilidad y gestión del servicio | 8 | 4 | RT-14.05 · RT-14.06 · RT-14.07 · RT-14.08 |
| | **Total** | **161** | **118 (73 %)** | **43** |

Además, de los 11 obligatorios del Capítulo 05 que corresponden a este subdocumento —integración (RT-05.16 a RT-05.23) y capa analítica (RT-05.25 a RT-05.30)—, quedan sin respuesta **RT-05.19** y **RT-05.27**.

### 5.1 A veintiséis de los cuarenta y cinco solo les falta la cita

Estos requisitos **están resueltos en el texto** pero sin el código que los identifica. Como el Formulario T-12 se responde código por código, un requisito bien resuelto y mal citado se evalúa igual que uno ausente. Es la corrección más rápida disponible:

| Requisito | Dónde está ya resuelto |
|---|---|
| RT-12.02 · inicio de sesión único con cierre propagado | (i) §4.2 lo describe literalmente |
| RT-12.03 · MFA obligatoria para administradores y acceso externo | (i) §4.2 |
| RT-12.08 · credenciales de vida breve con refresco rotatorio | (i) §4.4, política de sesión |
| RT-03.04 · segmentación por capas, subredes privadas sin alcance público | (j) §2.3, once pasajes |
| RT-02.10 · escalado horizontal automático con umbrales y costo | (k) §5, criterios de escalado declarados |
| RT-11.06 · controles ISO/IEC 27017 y 27018 en nube | (i) §10, transferencia internacional |
| RT-11.12 · protección contra bots y abuso automatizado | (j) §2.5, capa pública |
| RT-11.23 · inventario de componentes en CycloneDX o SPDX | (j) §1, reglas del flujo de integración |
| RT-11.24 · firma de artefactos y procedencia SLSA 3 | (j) §1 y tecnologías del apartado (b) |
| RT-11.26 · proceso de aprobación de dependencias de terceros | (i) §9, ciclo de desarrollo |
| RT-07.12 · prueba de restauración mensual | (e) y (j) §5 |
| RT-04.11 · cobertura de pruebas del 70 % con umbral bloqueante | (j) §1 |
| RT-10.06 · despliegue sin interrupción del servicio | (j) §1, azul-verde con canario |
| RT-14.08 · retención de métricas, registros y trazas con su costo | (i) §7 y la capa de observabilidad |
| RT-08.01 · especificación del equipamiento de cómputo | (c) §c.1 y (k) §4.1 |
| RT-08.02 · almacenamiento redundante con tolerancia declarada | (k) §4.3, RAID 10 sobre NVMe y pool Ceph |
| RT-08.10 · especificación de cada dispositivo de terreno | (c) §c.3, con marca y modelo de referencia |
| RT-08.17 · borrado seguro verificable de medios que salen de servicio | (i) §12 |
| RT-08.18 · disposición final con gestor autorizado | (i) §12 |
| RT-05.19 · identificador de correlación por integración | (h), `transaction_id` propagado, ocho pasajes |
| RT-05.27 · informes de autoservicio con modelo semántico | (l) §7, herramienta de autoservicio |
| RT-06.09 · instalación eléctrica independiente conforme a NCh | (d), normativa eléctrica y puesta a tierra |
| RT-06.22 · espacio de atención para enrolamiento | (i) §12, capas de acceso |
| RT-06.30 · espacio de operación separado de la sala de equipos | (d), NOC contiguo con ventana interior |
| RT-06.33 · conectividad, canalizaciones y ductos | (d), dos ductos de ingreso independientes |
| RT-14.05 · libro de operación y guía de resolución | mención única, conviene reforzar |

### 5.2 Diecinueve exigen contenido nuevo

| Requisito | Qué falta | Dónde corresponde |
|---|---|---|
| RT-07.13 | Tabla de frecuencia de respaldo, retención y tiempo de restauración **por dominio de datos** | Subdoc 4.2 (e) — es de esta parte |
| RT-06.02 | Blindaje perimetral de muros no estructurales, con material y resistencia | Subdoc 4.2 (d) |
| RT-06.06 | Reparto de la obra civil: a cargo del CLIENTE, con especificación y coordinación del proponente | Subdoc 4.2 (d) |
| RT-06.19 | Integración de la detección y extinción al monitoreo en línea, con notificación al NOC y a la contraparte | Subdoc 4.2 (d) |
| RT-06.31 | Declaración de que se usan las instalaciones sanitarias y áreas exteriores existentes, sin duplicarlas | Subdoc 4.2 (d) |
| RT-08.06 | Equipamiento nuevo, sin uso previo, con garantía vigente desde la recepción conforme | Subdoc 4.2 (c) |
| RT-08.07 | Especificación de las estaciones de trabajo de operación y administración | Subdoc 4.2 (c) |
| RT-08.09 | Gestión centralizada de estaciones: cifrado de disco, control de extraíbles, detección y respuesta | Subdoc 4.2 (c) |
| RT-08.16 | Plan de ciclo de vida del equipamiento: recepción, servicio, mantención, retiro y disposición | Subdoc 4.2 (c) o Subdoc 11 |
| RT-02.05 | Capa de servicios sin estado — está en el Subdoc 4.1, no aquí | Subdoc 4.1 (basta citarlo una vez en el T-12) |
| RT-02.13 | Modelo de dominio del negocio con entidades, relaciones y eventos | Subdoc 5 y Subdoc 4.1 |
| RT-04.03 | Control de versiones con ramas protegidas y revisión obligatoria por pares | Subdoc 9 — Informe 2 |
| RT-04.04 | Trazabilidad requerimiento → incidencia → código → prueba → despliegue | Subdoc 9 — Informe 2 |
| RT-04.10 | Migraciones de esquema versionadas, reversibles y compatibles entre dos versiones | Subdoc 9 — Informe 2 |
| RT-04.12 | Métricas de entrega: frecuencia de despliegue, tiempo a producción, tasa de cambios fallidos y restauración | Subdoc 9 — Informe 2 |
| RT-10.03 | Plan de continuidad del negocio conforme a ISO 22301 — es entregable del checklist transversal | Subdoc 11 — propuesta final |
| RT-10.04 | Continuidad TIC conforme a ISO/IEC 27031, articulada con el plan de recuperación | Subdoc 11 — propuesta final |
| RT-14.06 | Análisis de causa raíz obligatorio con informe en cinco días hábiles | Subdoc 10 — propuesta final |
| RT-14.07 | Registros sin datos personales sensibles ni credenciales, con acceso auditado | Subdoc 4.2 (i) o Subdoc 5 |

De los diecinueve, **nueve son de este subdocumento** —los del Capítulo 06 y 08 más RT-07.13—, uno (RT-14.07) se puede resolver aquí o en el Subdocumento 5, y los nueve restantes corresponden legítimamente a subdocumentos que entran en el Informe 2 o en la propuesta final. La concentración en el Capítulo 08 no sorprende: la especificación completa del hardware vive en `Arquitectura/fisica/T-11_Especificaciones_Tecnicas_Ofertadas.md` y el subdocumento solo lleva tablas de resumen.

---

## 6 · Lo que no se resuelve editando el texto

Tres brechas quedan abiertas porque el material existe fuera del entregable o no existe todavía.

**La tabla de emplazamiento de 36 componentes.** El apartado (a) declara 36 componentes —11 on-premise puros, 12 híbridos y 13 servicios administrados— y remite a un documento que no se entrega: `Arquitectura/fisica/Tabla_Emplazamiento_OnPremise_v06.md`, 84 KB. Lo que el subdocumento entrega es una tabla de cinco componentes. El Art. 16.2 califica la asignación sin justificar por componente como **observación grave**, y el entregable N° 3 del checklist transversal exige esa tabla en el Sobre N° 2. La justificación existe y es buena; hay que incorporarla como planilla del subdocumento. Es el cambio de mayor rendimiento pendiente.

**Los planos del recinto.** RT-06.03 exige el plano de distribución interna con separación de zonas y RT-06.05 la elevación de gabinetes. `Diagramas/RT-06_DataCenter/` contiene doce piezas elaboradas —distribución, sala técnica en dos páginas, cadena eléctrica, elevación de racks, gabinetes de borde y ficha técnica— más `DC06_Plano_DataCenter_Primario_Blueprint.png`, y el `Diagramas/README.md` ya verificó por hash que ninguna entró al entregable. El texto corregido remite ahora a «los planos del recinto que acompañan a esta parte»: **hay que incorporarlos o ajustar esa frase**.

**La declaración de funciones no disponibles sin conexión.** RT-03.13 es el entregable N° 4 del checklist transversal. El apartado (h) §11 da la regla general, que es correcta, pero el detalle por componente sigue remitiendo a la tabla de emplazamiento. Se cierra con la misma incorporación anterior.

---

## 7 · Verificación del resultado

Comprobado sobre `04_arquitectura/entrega_2/texto/arquitectura_fisica.md`:

- **173 códigos RT citados, ninguno inexistente** ni fuera del rango del Anexo A.
- **Cero residuos de trabajo**: sin notas de auditoría, sin hallazgos, sin historial de versiones, sin «pendiente de definir», sin códigos de rúbrica interna, sin citas a números de línea.
- **Cero citas a decisiones inexistentes**: las únicas referencias al numeral 16.1 del caso son sus decisiones N° 4, N° 11 y N° 14, que sí existen.
- **Jerarquía válida** de tres niveles, sin encabezados duplicados.
- **47 tablas en formato Markdown, todas bien formadas**; las 115 referencias a planillas intactas, de modo que los siete `.xlsx` siguen siendo válidos sin modificación.
- **Nomenclatura del respaldo** alineada al texto literal de RT-07.09 (3-2-1-0) en sus nueve apariciones, conservando la descripción de las cinco piernas.

## 8 · Orden sugerido para el Informe 2

1. Incorporar la tabla de emplazamiento de 36 componentes como planilla del apartado (a).
2. Incorporar los planos del recinto al apartado (d), o ajustar la remisión.
3. Validar con el equipo los valores nuevos del numeral 14.2 (§2.4 de este análisis).
4. Citar los 26 códigos de la sección 5.1 en las filas donde ya está la sustancia.
5. Escribir los nueve requisitos de la sección 5.2 que son de este subdocumento.
6. Retirar del Subdocumento 3 la línea que emplaza «componentes de IA», por coherencia con la Decisión N° 52.
7. Alinear el Subdocumento 2 con la disponibilidad y la tipología corregidas en §2.1 y §2.2.
8. Decidir la consolidación de planillas de la sección 4, que exige editar los `.xlsx`.
