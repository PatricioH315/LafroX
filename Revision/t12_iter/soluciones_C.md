# Soluciones propuestas para las 29 filas C del T-12

Las 29 filas C quedaron en «Cumple parcialmente» porque cada una necesita un dato o una decisión. Este documento propone, para cada una, cómo cerrarla con el menor arrastre posible. Se basa en `plan_C_datos.md`, en las Bases y en fichas públicas de fabricantes, y separa lo que LafroX puede decidir por sí misma de lo que exige un dato real del equipo.

Hay una regla que cambia el panorama. El Art. 50.2 de las Bases Administrativas dice: «la Oferta Técnica no podrá contener información de precios, tarifas, valores unitarios ni cifra alguna que permita inferir el monto de la oferta económica. Su inclusión es causal de exclusión inmediata». Las BA prevalecen sobre las BTT. Por eso, cuando un RT pide un costo, la Oferta Técnica declara el elemento técnico y remite el valor al Formulario E-21 de la Oferta Económica. **No se necesita ningún precio para cerrar esas filas.**

## Grupo 1 — Filas que piden costos: se cierran remitiendo a la Oferta Económica (6)

| ID | Qué pide | Solución técnica (Oferta Técnica) | Dónde va el valor | Destino de la frase | Estado esperado |
|---|---|---|---|---|---|
| RT-08.10 y RNF-23.01 | Marca, modelo, cantidad, características, accesorios, consumibles y costo unitario de cada dispositivo de terreno | El T-11 ya declara todo salvo el costo. Se agrega una nota: «El costo unitario estimado de cada dispositivo se presenta en la Oferta Económica (Formulario E-21, Entregable 2, numeral 2.4), conforme al Art. 50.2 de las Bases Administrativas». | E-21, 2.4 matriz de adquisiciones | T-11, nota bajo la Tabla 1 | Cumple |
| RT-03.08 | Compromiso de capacidad (Savings Plans) reflejado en la estructura de costos | Declarar el instrumento: Compute Savings Plans de un año, sin pago anticipado y renovables, sólo para la capacidad base permanente de ECS Fargate; el peak de septiembre y las corridas de rutas quedan bajo demanda. El plazo de un año permite ajustar el compromiso con la revisión trimestral de capacidad. | E-21, 2.5 infraestructura y alojamiento | SD4 4.2.3.4 | Cumple |
| RT-04.13 | Cuantificar el ahorro de apagar ambientes no productivos e incorporarlo a la estructura de costos | El ahorro en horas ya está cuantificado: 64,3 % de horas de cómputo no productivo (S-43). Se agrega que su valorización monetaria figura en la Oferta Económica. | E-21, 2.5 «optimizaciones previstas en el tiempo» | SD4 4.2.3.4 (párrafo de RT-15.06) | Cumple |
| RT-14.08 | Retención de métricas, registros y trazas, y su costo, distinguiendo línea y archivo | Métricas 13 meses y registros 12 meses en línea más 24 en archivo ya están declarados. Falta trazas: se propone 30 días en línea, sin archivo, porque su valor es diagnóstico. El costo de cada rubro va a la Oferta Económica. | E-21, 2.5 | SD4 4.1.3.8 | Cumple |
| RT-16.24 | Proveedor de cada canal, costo unitario, volumen proyectado y tratamiento del costo variable | Proveedores dentro de AWS, ya usado por INT-11: Amazon SES para correo, AWS End User Messaging SMS para SMS y AWS End User Messaging Social para WhatsApp; el aviso en portal es propio y no tiene costo variable externo. Volumen: 2.800 avisos diarios habituales y 5.200 en el peak (ya calculado), repartidos según la preferencia de cada cliente. El costo unitario y el tratamiento del excedente van como componente variable de la Operación. | E-21, 1.2 componentes variables | SD4-Anexos 4-H (INT-11) | Cumple |

Riesgo: el evaluador podría exigir el costo en el T-12. La respuesta es el Art. 50.2, que es de rango superior y sanciona con exclusión.

## Grupo 2 — Decisiones que LafroX puede tomar sin datos externos (12)

**NOC y SOC (RT-21.01, RNF-21.01 y RT-11.17).** El SD1 (Tabla 1.1) ubica al personal de desarrollo, arquitectura, calidad y seguridad en la «Sede Central (Santiago)» y a los 32 profesionales del NOC en un «Centro de Operaciones» sin ciudad. La portada de la oferta da el domicilio legal en Av. Brasil 2241, Valparaíso. Propuesta: declarar que el NOC y el SOC funcionan en el Centro de Operaciones de LafroX en Santiago, propios y no subcontratados, cada uno con una posición permanente 24×7×365 (4 personas por puesto; 5 desde el 26-04-2028), y resumir sus procedimientos: vigilancia continua, clasificación y escalamiento L1–L3, entrega documentada de turno y verificación de cierre. Destino: SD1 1.1 (viñeta del Centro de Operaciones) y SD4-Anexos 4-W.7. Es una decisión sobre una empresa ficticia que el equipo debe aceptar: no contradice nada, pero fija una ciudad.

**Nombres de dominio expuestos (RT-11.13, RF-14.03-BTT y RF-19.03).** La Tabla 19 del SD4 (4.2.5.2) ya declara las cinco entradas, sus puertos y controles; falta el nombre. Puelche no tiene dominio en las Bases y no conviene inventarlo ni dejar un marcador del tipo «<dominio>» (podría leerse como indicio de IA). Propuesta: agregar a la Tabla 19 una columna «Nombre» con los subdominios `portal`, `api`, `identidad`, `consolas` y `as2`, y una frase: «los nombres se publican como subdominios del dominio corporativo del CLIENTE y se registran en el hito H1; los túneles de sitio se identifican por sitio y región, sin nombre público». Estado esperado: Cumple, con riesgo bajo si el evaluador exige el dominio completo.

**Bolsa de mantención evolutiva (RT-21.19 y RNF-21.08).** La BTT (cap. 21.4) exige una bolsa anual de horas evolutivas comprometida en la oferta, con composición por perfil y procedimiento de solicitud, estimación, aprobación y liquidación. El T-15 ya asigna 4.608 HH de desarrollo (DES) al paquete 8.2.1, «mantenimiento correctivo y evolutivo», durante los 36 meses de Operación. 4.608 ÷ 3 = 1.536 HH por año, para correctivo y evolutivo juntos. El correctivo es obligatorio y sin costo adicional, pero también consume horas. Propuesta: separar esas 1.536 HH anuales en 768 HH evolutivas (la bolsa) y 768 HH correctivas, sin agregar horas. Composición: perfil DES (Laravel/PHP o Kotlin según el cambio). Procedimiento: el CLIENTE solicita, LafroX estima, el CLIENTE aprueba antes de ejecutar, se liquida por HH efectivas y el saldo se acumula al año siguiente (la BTT dice que no se pierde). La tarifa del excedente va al E-21. Destino: T-14, cuenta 8.2, junto al paquete 8.2.1. La proporción 50/50 es una decisión del equipo; si se prefiere otra, sólo cambia la cifra.

**Normas de piso técnico, canalización, cableado y etiquetado (RT-06.04).** Es fácil: el T-11 ya especifica piso técnico, Cat6A, OM4 y certificación de enlaces; sólo falta nombrar las normas. Propuesta: EN 12825:2001 (piso técnico), ANSI/TIA-569-E:2019 (canalizaciones y espacios), ISO/IEC 11801-1:2017 (cableado) y ANSI/TIA-606-D:2021 (administración y etiquetado). Destino: T-11, filas de piso técnico y distribución horizontal, y la referencia en la lista del T-11.

**Telefonía en los puestos de operación (RT-06.29).** Propuesta: telefonía por cliente de software en las estaciones, con auriculares, sobre la conectividad ya prevista en cada sitio, sin central telefónica nueva. Destino: SD4 4.3.1.4, párrafo de la zona de trabajo.

**Valorización de la merma (RF-08.07).** Propuesta: la merma se valoriza al costo unitario contable del ERP vigente al ocurrir el hecho, validado por Finanzas, y se imputa una sola vez a la entrega y cliente cuando existe atribución documentada, sin duplicar devoluciones. Destino: SD5 5.1.11.

**Umbrales de usabilidad por perfil (RT-13.04).** La BTT pide comprometer, por perfil, tiempo máximo de la transacción crítica, pasos máximos, error tolerado y tiempo de aprendizaje. Ya existe el de preparación (2 h, error ≤ 5 %, misión de 20 líneas). Propuesta: una tabla corta con una transacción crítica por perfil (preventista: pedido de 20 líneas; conductor: entrega con evidencia; recepción: recepción de una OC; planificador: revisión de ruta; Calidad: liberación de lote; cliente del portal: pedido en autoservicio), con pasos máximos, tiempo máximo, error tolerado y aprendizaje, calculados con un presupuesto explícito por paso. Destino: SD4 4.1.3.1. Es la más larga de este grupo porque es una tabla, pero no arrastra nada.

## Grupo 3 — Datos de fabricante disponibles en fuentes públicas (6)

**Grado de protección y caídas (RT-08.12 y RNF-23.02).** Valores de fichas publicadas (en su mayoría de distribuidores; antes de entregar conviene cotejarlos con la ficha oficial del fabricante):

| Dispositivo | Protección | Caídas | Fuente |
|---|---|---|---|
| Zebra MC9400 (estándar y Cold Storage) | IP65 e IP68 | 3,65 m a concreto según MIL-STD-810H; 2,4 m en todo el rango de temperatura | Fichas de distribuidores |
| Zebra TC58e | IP65 e IP68 | 1,8 m a concreto con funda protectora | Fichas de distribuidores |
| Zebra EC55 | IP67 | Dato no concordante entre fuentes: tomar el de la ficha oficial | Fichas de distribuidores |
| Zebra ZQ620 Plus | IP54 | 1,52 m a concreto | Fichas de distribuidores |
| Onset InTemp CX450 | IP54 | Sin dato de caída | Manual del fabricante |
| PAX A920 Pro | El fabricante no publica grado IP | Se usa con funda protectora; opera de −10 a 50 °C | Ficha técnica del distribuidor |
| Zebra ZT411 y balanza Dibal BEV | Equipos fijos de interior: el grado IP no aplica a su entorno | — | — |

Destino: T-11, columna de características. Estado esperado: Cumple. El PAX A920 Pro no tiene grado IP: se declara así y se mitiga con funda y uso dentro de la cabina, en vez de afirmar un dato que no existe.

**Condiciones ambientales y autonomía (RT-08.11).** Con la tabla anterior más los rangos de temperatura ya declarados en el T-11, sólo falta la autonomía. Ver RT-17.07.

**Consumo de batería por turno (RT-17.07).** La BTT pide optimizar y declarar el consumo estimado por turno. No hay un número medido y no conviene inventarlo. Propuesta sin cifra inventada: declarar la optimización (sincronización por lotes, reintentos espaciados, descarga por Wi-Fi al retorno) y comprometer como consumo estimado una carga de batería por turno de 14 horas, con recarga en el soporte del vehículo (TC58e, ya previsto en el T-11) y batería de recambio en caliente en el MC9400. El valor medido se verifica en la aceptación en terreno. Destino: SD4 4.2.6.7. Estado esperado: Cumple con riesgo medio: un evaluador estricto podría pedir mAh o porcentaje.

**Estaciones de trabajo y mini-PC (RT-08.01 y RNF-23.04).** Faltan marca, modelo y configuración de las 8 estaciones nuevas, y la CPU exacta del mini-PC E-01 (Advantech ARK-2250). Hallazgo importante: según su ficha, la familia ARK-2250L usa procesadores Intel de 6.ª generación (2015–2016). Con la exigencia de soporte vigente durante los 56 meses (BTT §1.6), conviene revisar ese equipo. Propuesta: el equipo elige un modelo actual de estación (por ejemplo, una línea corporativa de Dell, HP o Lenovo con Intel Core de generación vigente, 16 GB, SSD de 512 GB y dos salidas de video) y confirma o reemplaza el mini-PC por un modelo vigente de la misma clase. Esto es una decisión de compra del equipo, no un dato que se pueda derivar.

## Grupo 4 — Requieren datos reales del equipo (5)

**Huella de carbono anual y metodología (RT-15.03) e intensidad de la región de nube (RT-15.04).** Se puede estimar sin inventar nada en la parte local: la sala de Talca consume como máximo 13,5 kW continuos, es decir, 13,5 × 24 × 365 = 118.260 kWh/año. Con el factor de emisión del Sistema Eléctrico Nacional, que publica el Ministerio de Energía (cerca de 0,2 tCO₂e/MWh en 2024 según la prensa sectorial; hay que tomar la cifra oficial), da del orden de 24 tCO₂e/año. Para la nube, AWS entrega el reporte de huella de la cuenta (Customer Carbon Footprint Tool); la región sa-east-1 está en Brasil, cuyo factor oficial (MCTI) fue de 0,0385 tCO₂/MWh en 2023. Propuesta: metodología GHG Protocol, alcance 2 por ubicación; estimación local calculada con el factor oficial del SEN; nube reportada mensualmente con la herramienta de AWS y declarada en el primer informe anual. Lo que falta es tomar los factores oficiales exactos y su año. Estado esperado: Cumple parcialmente hasta fijar los factores; con ellos, Cumple.

**Certificaciones por persona (RT-15.08).** Hay que indicar qué integrante tiene cada certificación exigida (PMP o PRINCE2, ITIL 4, COBIT, AWS, CISSP/CISM/CEH/OSCP, base de datos e ISTQB), con su vigencia y dedicación. Los nombres del equipo son de personas reales, así que no se pueden inventar certificaciones. Requiere la nómina real.

**Especialistas de operación por tecnología (RT-21.03).** Mismo problema: hay que nominar personas por tecnología (AWS, PostgreSQL/Aurora, red, Laravel/Kotlin, mensajería y seguridad). Opción sin inventar personas: nominar a los responsables ya nombrados en el SD1 (Castillo para SRE y operación; Catalán para seguridad) y cubrir el resto como «especialistas de la División de Infraestructura» con dedicación del T-15. Queda parcial, porque «nominados» exige nombres.

**Misión, visión, valores y oficinas (RT-23.01).** Es contenido corporativo de LafroX que el equipo debe aprobar, y se acredita en el sitio web, no sólo en el documento. Se puede redactar un borrador para su aprobación. Oficinas: Sede Central en Santiago y domicilio legal en Av. Brasil 2241, Valparaíso, ambos ya presentes en el SD1.

## Resumen

| Grupo | Filas | Cómo se cierra | Estado esperado |
|---|---|---|---|
| 1. Costos | 6 | Elemento técnico en la oferta y valor en el E-21 (Art. 50.2 BA) | Cumple |
| 2. Decisiones de LafroX | 12 | Una frase o tabla corta por fila | Cumple |
| 3. Fichas públicas | 6 | Datos de fabricante; dos requieren decisión de compra | Cumple, salvo estaciones y mini-PC hasta que el equipo elija modelos |
| 4. Datos del equipo | 5 | Factores oficiales, nómina real, certificaciones y textos corporativos | Parcial hasta tener los datos |


## Validación independiente (gpt-6.1-sol, solo lectura)

**El Art. 50.2 permite separar los costos, pero no eliminarlos ni cerrar filas mediante una remisión sin respaldo.** BA Arts. 5.1–5.4 y 50.2, junto con Aclaraciones §2, sostienen esa separación. RT-08.10 y RT-14.08 exigen costos; ninguno autoriza incluirlos contra la prohibición administrativa. RT-16.24 menciona expresamente la Oferta Económica. E-21 admite el detalle, pero §2.4 no exige por sí solo costos unitarios: hay que incorporarlos explícitamente. No encontré un E-21 elaborado que permita verificarlos.

Revisión solo lectura. Los veredictos evalúan la solución propuesta: **OK** indica una vía suficiente al completar la evidencia señalada. SDn identifica `LAFROX-Subdocumenton.md`; “Anexos” y T-n identifican sus archivos separados.

| ID | Veredicto | Problema concreto con archivo y sección | Ajuste mínimo propuesto |
|---|---|---|---|
| RT-08.10 | ajustar | T-11, Tabla 1; BA E-21 §2.4: remitir no acredita costos por dispositivo, accesorio y consumible. | Incorporar el detalle unitario en E-21 y citarlo; conservar compra del terreno por CLIENTE. |
| RNF-23.01 | ajustar | T-11, Tabla 1: misma carencia económica; el requisito incluye todos los dispositivos declarados. | Usar la misma matriz económica de RT-08.10, sin duplicarla. |
| RT-03.08 | ajustar | SD4 §4.2.3.4: el compromiso anual no se reajusta trimestralmente por elegir plazo de un año. | Mantener Compute Savings Plans para carga estable; revisión trimestral informa la renovación anual. [AWS](https://aws.amazon.com/savingsplans/faqs/) |
| RT-04.13 | ajustar | SD4 §4.2.3.4 y SD3-Anexos S-43: 64,3 % es potencial; la meta comprometida es ≥60 %, con excepciones. | Remitir la valorización al E-21 §2.5 y distinguir ahorro potencial, meta y medición efectiva. |
| RT-14.08 | ajustar | SD4 §4.1.3.8: faltan plazo de trazas y distinción línea/archivo para métricas; los costos siguen pendientes. | Declarar explícitamente línea/archivo para los tres rubros y costos en E-21; 30 días es viable si se identifica X-Ray. [AWS](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html) |
| RT-16.24 | ajustar | SD4-Anexos 4-H, INT-11 y 4-P: los productos existen, pero SES/Social no estaban elegidos; 2.800/5.200 es total, no volumen por canal. | Elegir proveedor por canal, declarar reparto como supuesto calculado y costos en E-21 §§1.2/2.5. Social requiere región y WABA; no presumir sa-east-1. [AWS](https://docs.aws.amazon.com/general/latest/gr/end-user-messaging.html) |
| RT-21.01 | ajustar | SD1 §1.1/Tabla 1.1: Santiago no está declarado para el Centro de Operaciones; SD4-Anexos 4-W.7 distingue puesto y personas. | Confirmar ubicación; escribir una persona simultánea por turno, cuatro para cobertura y cinco desde 26-04-2028; procedimientos propuestos bastan. |
| RNF-21.01 | ajustar | SD1 §1.1 y SD4-Anexos 4-W.7: misma dependencia; 32 personas corporativas no son dotación asignada a Puelche. | Reutilizar la declaración de RT-21.01, sin sumar personal corporativo al proyecto. |
| RT-11.17 | ajustar | T-15 §5.7 permite contratación o SOC subcontratado; SD6 §6.1.3 mantiene esa alternativa. “Propio” exige resolverla. | Confirmar modalidad y ubicación; conservar una posición 24×7 y cobertura desde mes 13, con relevos acreditados. |
| RT-11.13 | no sirve | SD4 §4.2.5.2, Tabla 19: `portal`, `api`, etc. son etiquetas, no cada dominio completo exigido. | Obtener dominio autorizado y declarar FQDN de cada entrada; mantener parcial mientras falte. |
| RF-14.03-BTT | no sirve | SD4 §4.2.5.2: diferir nombres al H1 no satisface la declaración en oferta. | Usar el mismo inventario completo de RT-11.13. |
| RF-19.03 | no sirve | SD4 §4.2.5.2: persiste exactamente la carencia de nombres completos del T-12. | Reutilizar el inventario; conservar puertos IPsec y servicios existentes. |
| RT-21.19 | ajustar | T-15 §4.2: 4.608 HH en 8.2.1 no justifican reparto 50/50; las 2.304 de 8.2.4 son deuda técnica. BTT §21.4 no limita correctivos. | Proponer explícitamente 768 HH/año DES dentro de 8.2.1, justificar capacidad y aclarar que correctivos no consumen bolsa ni generan excedentes. |
| RNF-21.08 | ajustar | T-14 cuenta 8.2: procedimiento y acumulación son correctos; falta fundamento del tamaño y tarifa efectiva del excedente. | Misma bolsa y procedimiento de RT-21.19; tarifa en E-21 §2.6, manteniendo aparte 8.2.4. |
| RT-06.04 | OK | T-11, filas piso/cableado y distribución; T-14 §6.2.2 ya exige certificación del 100 % de enlaces. | Añadir normas propuestas y relacionarlas con informes por enlace y planos; no basta una lista bibliográfica. |
| RT-06.29 | ajustar | SD4 §4.3.1.4: cliente de software y auriculares no aseguran servicio telefónico; falta declarar Internet para los puestos. | Declarar telefonía operativa y acceso a Internet mediante los enlaces previstos, con auriculares incluidos. |
| RF-08.07 | ajustar | SD5 §5.1.11 y Anexos 5-A/5-H: la frase define valorización, pero `hech_actividad_costo` conserva solo `importe_devoluciones`. | Registrar importe de merma trazado a entrega/cliente e incorporarlo al cálculo existente; aislar casos sin atribución y evitar duplicados. |
| RT-13.04 | ajustar | SD4 §4.1.3.1 y T-14 §2.6.3: se propone una tabla sin valores; seis perfiles omiten otros usuarios de consolas y portales. | Completar cuatro umbrales por perfil pertinente, agrupando equivalentes; distinguir aprendizaje de duración de transacción y preservar RNF-05.03. |
| RT-08.12 | ajustar | T-11, Tabla 1: mezcla MC9400 estándar/Freezer y deja equipos sin IP/caídas. “Interior” no elimina automáticamente la declaración. | Usar fichas oficiales por variante: Freezer 2,1 m en −30/+50 °C; EC55 1,2 m, 1,5 m con funda. Resolver faltantes. [MC9400](https://www.zebra.com/gb/en/products/spec-sheets/mobile-computers/handheld/mc9400-mc9450.html), [EC55](https://www.zebra.com/us/en/products/spec-sheets/mobile-computers/handheld/ec50-ec55.html) |
| RNF-23.02 | ajustar | T-11, terminal PAX: “solo cabina” contradice cobro en local del cliente; funda no acredita IP ni resistencia. | Acreditar protección del conjunto para su uso real o elegir equivalente documentado; conservar parcial ante datos ausentes. |
| RT-08.11 | ajustar | T-11/SD4 §4.2.1.2: faltan humedad, vibración, luminosidad y autonomía pertinente por equipo; IP y temperatura no cubren todo. | Matriz breve equipo/entorno/evidencia; restringir TC58e a reparto y MC9400 Freezer a −22 °C, sin cambiar compras. |
| RT-17.07 | no sirve | SD4 §4.2.6.7: “una carga por 14 h” es una cifra sin fundamento; recarga y recambio describen mitigación, no consumo. | Estimar porcentaje o mAh con perfil de uso y fuente explícitos; conservar 9,83 MB de datos y verificar después en terreno. |
| RT-08.01 | ajustar | T-11, estaciones/E-01: faltan CPU exacta, interfaces, consumo y dimensionamiento de estaciones. BTT §1.6 exige soporte, no generación reciente. | Completar configuración y hoja de soporte; sustituir ARK solo si no acredita vigencia. Su antigüedad es real, su incumplimiento no está demostrado. [Advantech](https://advcloudfiles.advantech.com/ecatalog/2018/09271042.pdf) |
| RNF-23.04 | ajustar | T-11, estación de trabajo: **ya** incorpora las ocho nuevas a gestión, cifrado y controles; T-12 conserva diagnóstico anterior. | Elegir modelo/configuración conservando monitores duales y NCh 2527; actualizar la justificación sin añadir controles repetidos. |
| RT-15.03 | no sirve | SD4 §4.3.1.4/T-14 §8.4.3: 118.260 kWh es cota de Talca, no huella anual de toda la solución; nube diferida al informe futuro. | Estimar ahora todos los sitios y nube con supuestos y factores fechados; usar CCFT después para contrastar, distinguiendo sus alcances. [AWS](https://docs.aws.amazon.com/ccft/latest/releasenotes/what-is-ccftrn.html) |
| RT-15.04 | ajustar | SD4 §4.3.1.4: PUE ≈1,5 ya existe. 0,0385 tCO₂/MWh es factor nacional brasileño de 2023, no intensidad acreditada de sa-east-1. | Declararlo como aproximación de red, con año y límite; obtener intensidad regional sustentada. El factor brasileño citado es real. [MCTI](https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/noticias/2024/02/fator-de-emissao-de-co2-na-geracao-de-energia-eletrica-no-brasil-em-2023-e-o-menor-em-12-anos) |
| RT-15.08 | OK | BTT §15.3 y SD1 §1.5: pedir nómina real es correcto; enumerar familias de certificación sin cantidades no basta. | Persona, certificado vigente, evidencia y dedicación; verificar mínimos 2/5/2/3/2/2/2 y nivel profesional/arquitecto de nube. |
| RT-21.03 | ajustar | SD1 §1.5/T-15 §5.7: “especialistas de Infraestructura” no nomina personas; HH del perfil no acredita dedicación individual. | Tabla persona/tecnología/dedicación, usando integrantes reales y comprobando disponibilidad en Operación. |
| RT-23.01 | OK | BTT §§23.1–23.2: correctamente exige contenido real y web; SD1 §§1.1/1.4 aporta antecedentes, no acredita por sí solo todo el RT. | Completar misión/visión/valores y oficinas confirmadas, publicarlos junto con antecedentes y certificaciones verificables; domicilio legal no equivale a oficina operativa. |

Riesgos generales:

- **Cierre anticipado:** reemplazar datos faltantes por compromisos futuros no permite declarar “Cumple”; la remisión económica tampoco sustituye el E-21.
- **Arrastre evitable:** confirmar SOC, proveedores y hardware antes de cambiar inventarios; preservar HH, S-43, retenciones de auditoría y D-09 sin IA.
- **Evidencia débil:** fichas de distribuidores, ausencia de datos publicada y factores aproximados no acreditan prestaciones; el factor chileno debe tomarse de la [CNE](https://energiaabierta.cl/visualizaciones/factor-de-emision-sic-sing/).
- **Diagnóstico desactualizado:** T-11 ya corrigió los controles de las estaciones nuevas y SD5 ya unificó los cuatro canales; contrastar el T-12 con esos textos antes de propagar cambios.
