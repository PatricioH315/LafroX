# LafroX — Subdocumento 13: Anexos

Estos anexos detallan lo que el Capítulo 13 resume. El Anexo 13.A define los contratos de datos que cada innovación consume o expone. El Anexo 13.B traza cada innovación con la arquitectura, la EDT, los riesgos y el flujo de caja. El Anexo 13.C reúne en una vista los indicadores y los riesgos de las cinco. El Anexo 13.D responde las observaciones de la instancia anterior. Las fichas formales del Artículo 29° están en el Formulario T-19.

## Anexo 13.A — Contratos de datos de las innovaciones

El RT-26.01 pide declarar qué interfaces consume o expone cada innovación (Distribuidora Puelche S.A., 2026b, RT-26.01). Ninguna innovación abre una interfaz externa nueva: todas viajan por las interfaces del Capítulo 4, sección 4.1.6, y por la cola de sincronización de los terminales. Lo que cada una agrega es un contrato de datos versionado, que se presenta en la Tabla 13.A.1.

**Tabla 13.A.1. Contratos de datos de las innovaciones. Fuente: elaboración propia a partir del Capítulo 4, secciones 4.1 y 4.2, y del Capítulo 5.**

<a id="tab:13A1"></a>

| Contrato | Productor → consumidor | Transporte y capa | Campos principales | Exclusiones y retención |
| --- | --- | --- | --- | --- |
| `inn01.aviso-vencimiento-local.v1` | M10 → M3 (terminal C-01) | Precarga nocturna en la cola de sincronización de M3; capas 5 y 6 | Local, lote, GTIN, saldo estimado, ritmo de reposición, vida útil remanente y su origen (fecha impresa o innovación 3), confianza, acción del catálogo | Sin datos personales del almacenero; retención igual a la del historial de preventa |
| `inn01.respuesta-visita.v1` | M3 (terminal C-01) → M10 | Cola de sincronización de M3, al recuperar señal; capa 5 | Aviso, saldo confirmado, acción aplicada, resultado, preventista seudonimizado | El saldo confirmado no entra al inventario oficial |
| `inn02.paquete-reproduccion.v1` | Terminales C-01, C-02 y C-03 → QA y Preproducción | Envío con cupo de tamaño y frecuencia; trazas OpenTelemetry hacia la capa 8; acceso controlado por la capa 7 | Correlación seudonimizada, versión de la aplicación, transiciones de estado, cola local, reintentos, orden causal, estado de conectividad | Excluye nombres, credenciales, firmas, fotos y contenido comercial; se borra al cerrar el incidente, salvo el escenario de regresión sintetizado |
| `inn03.historia-termica-lote.v1` | B-02 y N-10 → M9, M2, M5 y M10 | Eventos EPCIS 2.0 con datos de sensor (capa 5); series en N-06 y N-10 (capa 6) | Lote, GTIN, familia, tramos (lugar, desde, hasta, sensor, resumen, sin dato), carga acumulada, vida remanente con intervalo, versión del modelo y de los parámetros | Los tramos sin dato nunca se rellenan; series retenidas cinco años |
| `inn04.liquidacion-tramo.v1` | M10 → Finanzas del CLIENTE y ERP | Informe mensual auditado por la capa 7; base versionada en la capa 6 | Período, canasta, índices aplicados, costo comparable, OTIF del período, puntuación, recomendación y respuesta | El dato contable definitivo vive en el ERP; los montos se expresan solo en la Oferta Económica |
| `inn05.hoja-negocio.v1` | M10 → M3 (terminal C-01) y M6 (impresora de cabina) | Precarga cifrada en el terminal; capa 7 limita la hoja al receptor | Local, bloques 1 a 3, bloque 4 si está activo, estado de la copia (pedida, entregada, en espera) | Bloque 4 con umbral mínimo de locales por grupo y supresión de celdas; registro de actividades de tratamiento |

Cada contrato tiene una versión explícita en su nombre. Un cambio de campos produce una versión nueva y convive con la anterior durante la transición, como el resto de los contratos del Capítulo 4. Los contratos de las innovaciones 2 y 5 tratan datos que pasan por la capa de seguridad; por eso el Encargado de Seguridad de la Información los aprueba con su modelado de amenazas (RT-26.07).

## Anexo 13.B — Matriz de trazabilidad

La Tabla 13.B.1 traza cada innovación con la arquitectura (RT-26.01), con la EDT y el cronograma (RT-26.02), con su riesgo (RT-26.04) y con su ubicación en el flujo de caja (Art. 28.2).

**Tabla 13.B.1. Trazabilidad de las innovaciones. Fuente: elaboración propia a partir de los Capítulos 3 y 4, del Formulario T-14, del Anexo 7.D y del Anexo 8.A.**

<a id="tab:13B1"></a>

| Innovación | Capas, componentes y módulos | Paquetes de la EDT y mes de materialización | Riesgo | Flujo de caja (sin montos) |
| --- | --- | --- | --- | --- |
| 1 · Seguimiento de vencimiento posentrega en el local | Capas 1, 4, 5 y 6; C-01; M2, M3, M9 y M10; N-10 | 3.10.1.1 a 3.10.1.4 (meses 7 a 15); materializa en el mes 16; mantenimiento en 8.2.1 | R8-25 | Inversión 7 a 15; costo operacional 16 a 56; beneficio desde el 16 |
| 2 · Reproducción de incidentes de terreno | Capas 1, 7 y 8; C-01, C-02 y C-03; M3, M5 y M6; QA y Preproducción | 3.10.2.1 a 3.10.2.4 (meses 2 a 15) y 8.3.1 (21 a 56); circuito en el mes 5 | R8-26 y R8-24 | Inversión 2 a 10; costo operacional 5 a 56; beneficio desde el 13 |
| 3 · Vida útil remanente por historia térmica del lote | Capas 1, 4, 5, 6 y 7; B-01, B-02, B-03 y C-02; N-06, N-08 y N-10; M2, M5, M9 y M10 | 3.10.3.1 a 3.10.3.4 (meses 3 a 15) y 8.3.2 (26 a 56, semestral); materializa en el mes 16 | R8-27 y R8-23 | Inversión 3 a 15; costo operacional 16 a 56; beneficio desde el 16 |
| 4 · Tramo variable de la Operación ligado al costo de servir | Capas 4, 6 y 7; M6, M7, M8 y M10; N-10; ERP | 5.4.3 (meses 17 a 20), 8.3.3 (21 a 23) y 8.3.4 (24 a 56); primera liquidación en el mes 24 | R8-28 | Inversión 17 a 23; costo operacional 21 a 56; ingreso fijo 21 a 56; ingreso contingente 24 a 56; beneficio desde el 24 |
| 5 · Hoja de negocio del almacenero | Capas 1, 4, 6 y 7; C-01 e impresora de cabina; M3, M6 y M10; N-10 | 3.10.4.1 a 3.10.4.4 (meses 13 a 21), 8.3.5 (22 a 26) y 8.3.6 (24 a 27); materializa en el mes 21 | R8-29 | Inversión 13 a 18 y 24 a 27; costo operacional 21 a 56; beneficio desde el 33 |

La matriz muestra que las cinco innovaciones tienen al menos un paquete de la EDT, un mes de materialización, una ficha de riesgo y un rubro en cada clase del flujo de caja. Los meses coinciden con el Formulario T-14 y con el Anexo 7.D. Las horas de cada paquete están en el Formulario T-15, sección 4.

## Anexo 13.C — Indicadores y riesgos de la cartera

La Tabla 13.C.1 reúne los indicadores de las cinco innovaciones, ordenados por el mes en que se miden por primera vez.

**Tabla 13.C.1. Indicadores de verificación de la cartera. Fuente: Capítulo 13, secciones 13.1.6 a 13.5.6.**

<a id="tab:13C1"></a>

| Id | Línea base | Meta | Primera medición | Antes del mes 16 |
| --- | --- | --- | --- | --- |
| I-01A | Sin medición | ≥ 70 % con ≥ 100 avisos | Mes 15 | Sí |
| I-02A | Incidentes de los meses 5 a 10 | −30 % con ≥ 20 pares | Mes 15 | Sí |
| I-02B | Sin medición | ≥ 80 % | Mes 15 | Sí |
| I-02D | Cero por diseño | 0 | Cada liberación | Sí |
| I-03A | 0 | ≥ 95 % | Mes 15 | Sí |
| I-03B | Sin medición | ≥ 80 % con ≥ 60 lotes por familia | Mes 15 | Sí |
| I-03C | 0 | 100 % | Mes 16 | No |
| I-05B | Prototipo de los meses 13 y 14 | ≥ 80 % de 24 | Antes del mes 19 | No |
| I-02C | Sin medición | 0 | Mes 21 | No |
| I-04B | Sin modelo | 3 de 3 | Meses 21 a 23 | No |
| I-04C | Sin registro | 100 % | Mes 21 | No |
| I-05A | 0 | ≥ 90 % y ≥ 85 % | Mes 27 | No |
| I-05D | No aplica antes de activar | 100 % | Cada emisión | No |
| I-01B | Meses 13 a 15 | −25 % relativo | Mes 28 | No |
| I-01C | Meses 13 a 15 | −20 % relativo | Mes 28 | No |
| I-03D | Meses 13 a 15 | −20 % relativo | Mes 28 | No |
| I-05C | Período previo por ruta | Estimar el efecto | Mes 33 | No |
| I-04A | Canasta de los meses 21 a 23 | ≥ 5 % con OTIF ≥ 95 % | Mes 36 | No |

Seis indicadores de tres innovaciones se miden antes del mes 16, durante la marcha blanca de la Etapa 1. Con ellos LafroX oferta el RT-26.08 (Distribuidora Puelche S.A., 2026b, RT-26.08). Los indicadores de ahorro (I-01B, I-01C, I-03D, I-04A e I-05C) se miden después de al menos doce meses de producción, para que la comparación incluya un ciclo anual completo con el peak de septiembre.

La Tabla 13.C.2 reúne los riesgos de adopción con su evaluación en la escala ordinal del Capítulo 8, sección 8.1.3, donde la probabilidad 3 equivale a un 40 % y la 4 a un 60 %, y el impacto se mide como fracción del esfuerzo afectado.

**Tabla 13.C.2. Riesgos de adopción de la cartera. Fuente: Anexo 8.A y Formulario T-16.**

<a id="tab:13C2"></a>

| Ficha | Innovación | P | I | Exposición |
| --- | --- | --- | --- | --- |
| R8-25 | 1 · Seguimiento de vencimiento posentrega en el local | 4 | 3 | 12 |
| R8-26 | 2 · Reproducción de incidentes de terreno | 3 | 4 | 12 |
| R8-24 | 2 · Reproducción de incidentes de terreno (seguridad) | 3 | 5 | 15 |
| R8-27 | 3 · Vida útil remanente por historia térmica del lote | 4 | 5 | 20 |
| R8-23 | 3 · Vida útil remanente por historia térmica del lote (asociación sensor–lote) | 4 | 5 | 20 |
| R8-28 | 4 · Tramo variable de la Operación ligado al costo de servir | 3 | 4 | 12 |
| R8-29 | 5 · Hoja de negocio del almacenero | 4 | 3 | 12 |

La innovación 3 concentra la mayor exposición, porque su error afectaría una decisión sanitaria. Por eso su regla de diseño es asimétrica: la estimación puede acortar la vida útil de un lote, pero nunca alargarla más allá de la fecha impresa. El valor esperado en horas de cada riesgo y su efecto en la reserva de contingencia están en el Anexo 8.B.

## Anexo 13.D — Resolución de observaciones de la instancia anterior

El Art. 46 de las Bases Administrativas pide resolver en forma explícita las observaciones de la instancia anterior, con una tabla de trazabilidad observación–respuesta–sección modificada (Distribuidora Puelche S.A., 2026a, Art. 46). La Tabla 13.D.1 responde las observaciones formuladas al Capítulo 13.

**Tabla 13.D.1. Trazabilidad de observaciones del Capítulo 13. Fuente: elaboración propia a partir de las observaciones del CLIENTE.**

<a id="tab:13D1"></a>

| N.º | Observación | Respuesta | Sección modificada |
| --- | --- | --- | --- |
| 1 | El impacto económico no puede contener precios | Todo impacto se expresa por rubro, clase y mes, sin montos; la valorización va en la Oferta Económica, Entregable 2, ítem 2.7 | 13.1.5 a 13.5.5; Formulario T-19, campos 10 a 12 |
| 2 | La innovación 1 coincidía con un requisito | Se rehízo como seguimiento en el local, después de la entrega; se separa de la alerta en bodega del RF-02.09 y de la meta de merma del Capítulo 2 | 13.1.2 |
| 3 | La innovación 3 coincidía con un requisito | Se rehízo como vida útil remanente por historia térmica del lote; el registro continuo (criterio 3) queda declarado como base obligatoria y no como innovación | 13.3, 13.3.2 |
| 4 | La innovación 5 debe funcionar con el cliente sin internet | La hoja se entrega en la visita, en pantalla del terminal sin señal o impresa en la entrega siguiente, sin dispositivo ni registro del almacenero | 13.5.2 |
| 5 | Faltaban las fichas T-19 con los siete elementos | Se presenta el Formulario T-19 con una ficha por innovación y los 17 campos del formulario | Formulario T-19 |
| 6 | Cada innovación debe ubicarse en arquitectura, EDT y flujo de caja, con indicador, línea base, meta y mes | Cada innovación declara capas, componentes, módulos, paquetes del T-14, mes de materialización, rubros del flujo de caja e indicadores | Subsecciones 4 a 6 de 13.1 a 13.5; Anexo 13.B |
| 7 | Fuentes APA citadas en el texto y vigentes, incluido EPCIS 2.0 | Se cita EPCIS 2.0 (GS1 AISBL, 2022) y las demás fuentes en el punto de uso, con correspondencia uno a uno con la lista de referencias | 13.1.3 a 13.5.3; Referencias |
| 8 | El Capítulo 13 y el Formulario T-19 deben presentarse completos, con 13.1 a 13.5 y el filtro del Art. 30° | Se presentan los cinco títulos; cada innovación incluye una tabla de lo que ya es alcance obligatorio y de lo que agrega | 13.1.2 a 13.5.2 |
| 9 | La innovación 2 debe justificar por qué no es práctica estándar | Se explica que el defecto típico es un reordenamiento de la cola en la reconexión, que no deja rastro en un reporte de fallos, y se separa del RT-14.06 | 13.2.2 |

Las nueve observaciones se responden en este capítulo y en su formulario. Ninguna requirió cambiar los paquetes, los meses ni las horas de la EDT del Capítulo 7.

## Referencias

Las Bases se citan con su documento y el artículo o código del requisito.

- Distribuidora Puelche S.A. (2026a). *Bases Administrativas de Licitación N.º TFEP-01/2026: Contratación de Solución Integral de Software y Servicios de Operación*, artículos 28 y 46.
- Distribuidora Puelche S.A. (2026b). *Bases Técnicas Transversales de Licitación N.º TFEP-01/2026*, RT-26.01, RT-26.07 y RT-26.08.
- GS1 AISBL. (2022). *EPC Information Services (EPCIS) standard* (versión 2.0). https://ref.gs1.org/standards/epcis/2.0.0/

## Declaración de uso de IA

En cumplimiento de la sección 7.2 de las Aclaraciones de la licitación, la tabla siguiente declara el uso de herramientas de inteligencia artificial en estos anexos, con la revisión humana de cada parte. La declaración se consolida en el Formulario A-6.

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
| --- | --- | --- | --- | --- | --- |
| Anexo 13.A | Claude Code | Definición de los contratos a partir de los Capítulos 4 y 5 | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| Anexo 13.B | Claude Code | Matriz de trazabilidad cotejada con el Formulario T-14 y el Anexo 8.A | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| Anexo 13.C | Claude Code | Consolidación de indicadores y riesgos | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| Anexo 13.D | Claude Code | Tabla de observaciones y respuestas | Medio | Ninguno | [[REVISIÓN HUMANA]] |
