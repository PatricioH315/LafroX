# LafroX — Formulario T-19: Fichas de innovación

Este formulario contiene una ficha por cada una de las cinco innovaciones obligatorias del Artículo 28° de las Bases Administrativas, con los campos del Formulario T-19 en su orden (Distribuidora Puelche S.A., 2026a, Art. 29° y Formulario T-19). El análisis de cada innovación está en el Capítulo 13, secciones 13.1 a 13.5. Los campos de inversión, costo operacional y beneficio se expresan sin montos, por la restricción del Art. 50.2; su valorización está en la Oferta Económica, Entregable 2, ítem 2.7. Los requisitos RT citados corresponden a las Bases Técnicas Transversales (Distribuidora Puelche S.A., 2026b). La probabilidad y el impacto usan la escala ordinal 1 a 5 del Capítulo 8, sección 8.1.3.

## Ficha 1 — Innovación 1

Ficha de la innovación 1, «Seguimiento de vencimiento posentrega en el local», desarrollada en el Capítulo 13, sección 13.1.

| Campo | Contenido |
| --- | --- |
| 1. Tipo de innovación | 1 — Producto o servicio |
| 2. Nombre de la innovación | Seguimiento de vencimiento posentrega en el local (INN-01) |
| 3. Problema u oportunidad del caso que resuelve | Merma por vencimiento de 1,7 % del valor del inventario al año, detectada incluso en la góndola del cliente (Distribuidora Puelche S.A., 2026c, cap. 4.8); la preventista ve producto vencido de Puelche y no tiene dónde registrarlo (cap. 8). La pérdida posterior a la entrega no tiene medición ni momento para evitarse. |
| 4. Tecnología, práctica o modelo que la sustenta | Regla de cobertura por par lote–local: saldo estimado (entregas menos devoluciones, confirmado en la visita) dividido por el ritmo de reposición del historial de M3 (RF-03.14), comparado con la vida útil remanente del lote (innovación 3 o fecha impresa, RF-01.03). Aviso con acción de un catálogo aprobado por Comercial y Calidad. Agrega a lo obligatorio el seguimiento en el local y antes de la pérdida. |
| 5. Nivel de madurez y escala utilizada | Escala TRL de la Comisión Europea. Cálculo de cobertura: aritmética conocida. Servicio integrado: TRL 2; objetivo TRL 4 al mes 10 y TRL 6 al mes 15. |
| 6. Fuentes citadas (APA 7.ª ed.) | European Commission (2016); Riesenegger et al. (2023). |
| 7. Dónde se inserta en la arquitectura | M10 Analítica (capa 4, datos en N-10, capa 6) calcula la lista nocturna con datos de M2, M9 y M3; M3 Preventa la entrega en el terminal C-01 (capa 1) sin señal; la respuesta vuelve por la cola de sincronización (capa 5). Contrato `inn01.aviso-vencimiento-local.v1` y `inn01.respuesta-visita.v1` (Anexo 13.A). |
| 8. Paquetes de la EDT que la ejecutan | 3.10.1.1 (INN-01.P1), 3.10.1.2 (P2), 3.10.1.3 (P3) y 3.10.1.4 (P4); en operación, mantenimiento dentro de 8.2.1. Responsable: DAT. |
| 9. Mes del cronograma en que se materializa | Mes 16 (piloto en la marcha blanca de los meses 13 a 15). |
| 10. Inversión requerida | Horas de datos, desarrollo móvil y diseño del catálogo (meses 7 a 15) y acompañamiento del piloto en terreno (meses 13 a 15). Sin hardware ni licencias. |
| 11. Efecto en el costo operacional | Cálculo nocturno y almacenamiento en nube; mantención de la regla y del catálogo (meses 16 a 56). |
| 12. Beneficio esperado y su cuantificación | Unidades vencidas evitadas en el local por costo unitario, menos canjes y descuentos; desde el mes 16. No se suma a la meta de merma del Capítulo 2 ni a la innovación 3. |
| 13. Indicador de verificación, línea base y meta | I-01A: avisos confirmados / evaluables; base sin medición; meta ≥ 70 % con ≥ 100 avisos. I-01B: vencido en el local / entregado; base meses 13 a 15; meta −25 %. I-01C: devoluciones por vencimiento próximo / devoluciones; base meses 13 a 15; meta −20 %. |
| 14. Momento de medición | I-01A en el mes 15; I-01B e I-01C en el mes 28. |
| 15. Riesgo de adopción, probabilidad e impacto | R8-25: avisos falsos por compras irregulares o aviso sin acción posible. P = 4, I = 3, exposición 12. |
| 16. Estrategia de mitigación | No liberar sin cumplir I-01A; mostrar la confianza de cada aviso; confirmar el saldo en la visita; catálogo como condición de activación. |
| 17. Plan de contingencia si no rinde lo esperado | Degradar a aviso solo por vida útil remanente del lote; mantener el aviso informativo y escalar a Comercial. La trazabilidad de lote obligatoria sigue operando. |

## Ficha 2 — Innovación 2

Ficha de la innovación 2, «Reproducción de incidentes de terreno», desarrollada en el Capítulo 13, sección 13.2.

| Campo | Contenido |
| --- | --- |
| 1. Tipo de innovación | 2 — Proceso |
| 2. Nombre de la innovación | Reproducción de incidentes de terreno (INN-02) |
| 3. Problema u oportunidad del caso que resuelve | Pedidos perdidos o duplicados por falta de señal «semanalmente, sin medición» (Distribuidora Puelche S.A., 2026c, cap. 18, criterio 6; cap. 8); rutas con tramos sin señal de hasta dos horas (cap. 6). Los fallos llegan a la mesa como relatos no reproducibles. |
| 4. Tecnología, práctica o modelo que la sustenta | Circuito incidente → paquete sanitizado con el orden causal de la cola local, reintentos y conectividad → reproducción en QA o Preproducción con recursos efímeros (Terraform) → corrección validada contra el paquete → regresión permanente en GitLab CI. Agrega a lo obligatorio (RT-10.07, RT-14.06) la cobertura de incidentes no críticos y el cierre por reproducción. |
| 5. Nivel de madurez y escala utilizada | Escala TRL de la Comisión Europea. Piezas (CI/CD, entornos efímeros, trazas): TRL 9. Circuito para terminales sin señal: TRL 2; objetivo TRL 4 al mes 5 y TRL 6 al mes 15. |
| 6. Fuentes citadas (APA 7.ª ed.) | Shahin et al. (2017); DORA (2024); European Commission (2016). |
| 7. Dónde se inserta en la arquitectura | Terminales C-01 (M3), C-03 (M5) y C-02 (M6) en la capa 1 emiten la evidencia; capa 8 (OpenTelemetry y Amazon CloudWatch) correlaciona; capa 7 sanitiza y controla el acceso; reproducción dentro de QA y Preproducción, sin un sexto ambiente. Contrato `inn02.paquete-reproduccion.v1` (Anexo 13.A). |
| 8. Paquetes de la EDT que la ejecutan | 3.10.2.1 (INN-02.P1), 3.10.2.2 (P2), 3.10.2.3 (P3), 3.10.2.4 (P4, primera parte) y 8.3.1 (P4, segunda parte). Responsable: CAL. |
| 9. Mes del cronograma en que se materializa | Circuito inicial en el mes 5; beneficio medido en el mes 15. |
| 10. Inversión requerida | Horas de instrumentación de terminales y sanitización (meses 2 a 5) y de cobertura de M3, M5 y M6 (meses 5 a 10). No duplica las pruebas obligatorias de la cuenta 3.8. |
| 11. Efecto en el costo operacional | Cómputo efímero por corrida en QA y Preproducción (meses 5 a 56) y mantención de escenarios (meses 21 a 56). |
| 12. Beneficio esperado y su cuantificación | Horas de diagnóstico y regresiones repetidas evitadas; desde el mes 13. El criterio 6 del caso no se cuenta como beneficio de la innovación. |
| 13. Indicador de verificación, línea base y meta | I-02A: mediana de horas hasta la causa reproducida; base meses 5 a 10; meta −30 % con ≥ 20 pares. I-02B: paquetes que reproducen / admitidos; meta ≥ 80 %. I-02C: reaperturas por la misma causa; meta 0. I-02D: paquetes con datos prohibidos; meta 0. |
| 14. Momento de medición | I-02A e I-02B en el mes 15 y trimestral después; I-02C mensual desde el mes 21; I-02D en cada liberación. |
| 15. Riesgo de adopción, probabilidad e impacto | R8-26: reproducción que no explica el incidente o consumo de batería; P = 3, I = 4, exposición 12. R8-24: datos personales en los paquetes; P = 3, I = 5, exposición 15. |
| 16. Estrategia de mitigación | Comparar con el estado observado y revisión de muestras por Calidad; cupo y frecuencia de captura; sanitización por reglas fijas y modelado de amenazas (RT-26.07). |
| 17. Plan de contingencia si no rinde lo esperado | Reproducción semiautomática con paquete armado por soporte; captura solo a solicitud; suspender el conjunto afectado. Se mantienen el diagnóstico convencional y las pruebas obligatorias. |

## Ficha 3 — Innovación 3

Ficha de la innovación 3, «Vida útil remanente por historia térmica del lote», desarrollada en el Capítulo 13, sección 13.3.

| Campo | Contenido |
| --- | --- |
| 1. Tipo de innovación | 3 — Tecnológica o de arquitectura |
| 2. Nombre de la innovación | Vida útil remanente por historia térmica del lote (INN-03) |
| 3. Problema u oportunidad del caso que resuelve | Mil cien productos refrigerados y congelados sin registro continuo de temperatura (Distribuidora Puelche S.A., 2026c, cap. 4.9); rechazo de un camión completo sin poder demostrar la cadena de frío (cap. 4.9); la jefa de Calidad no sabe qué consecuencia tiene una excursión (cap. 8); exclusión por el proveedor de lácteos hasta acreditar trazabilidad (cap. 1 y 13.2). |
| 4. Tecnología, práctica o modelo que la sustenta | Eventos EPCIS 2.0 con datos de sensor por cada movimiento del lote; asociación lote–sensor por lugar y tiempo sin rellenar tramos; modelo cinético determinista por familia (Arrhenius o Q10) con parámetros aprobados por Calidad; cálculo en el borde (B-02) y en la nube (N-10). Agrega a lo obligatorio (criterio 3, RF-09.03 a RF-09.10, RNG-04) una vida útil remanente por lote. Oferta el RT-05.30. |
| 5. Nivel de madurez y escala utilizada | Escala TRL de la Comisión Europea. EPCIS 2.0: estándar publicado. Modelos cinéticos: validados experimentalmente. Integración en Puelche: TRL 2; objetivo TRL 4 al mes 10 y TRL 6 al mes 15. |
| 6. Fuentes citadas (APA 7.ª ed.) | GS1 AISBL (2022); Koutsoumanis et al. (2005); Jedermann et al. (2014); European Commission (2016). |
| 7. Dónde se inserta en la arquitectura | B-01, B-02, B-03 y C-02 (borde y capa 1); N-08 Ingesta de IoT y N-06 Telemetría cruda, con los 10.920 mensajes diarios ya dimensionados; capa 5 con eventos EPCIS; M9 muestra y Calidad dispone; M2 y M5 reciben orden sugerido; M10 sobre N-10 (capa 6) calcula; capa 7 versiona el modelo. Contrato `inn03.historia-termica-lote.v1` (Anexo 13.A). |
| 8. Paquetes de la EDT que la ejecutan | 3.10.3.1 (INN-03.P1), 3.10.3.2 (P2), 3.10.3.3 (P3), 3.10.3.4 (P4) y 8.3.2 (P5). Responsable: DAT. |
| 9. Mes del cronograma en que se materializa | Mes 16, en apoyo a la decisión de Calidad; orden sugerido habilitado por familia al cumplir I-03B. |
| 10. Inversión requerida | Horas de datos y Calidad (meses 3 a 5); horas de borde, eventos y vista en M9 (meses 5 a 10); validación con lotes reales, con laboratorio externo si se contrata (meses 11 a 15). Sin hardware ni ingesta adicional. |
| 11. Efecto en el costo operacional | Cómputo en el borde y en N-10 (meses 16 a 56); recalibración semestral de parámetros (meses 26, 32, 38, 44, 50 y 56). |
| 12. Beneficio esperado y su cuantificación | Retenciones y descartes sin justificación térmica evitados; rechazos por fecha próxima evitados; dato de vida útil consumida para decidir reubicar o descartar. Desde el mes 16. No se suma a la meta de merma ni a la innovación 1. |
| 13. Indicador de verificación, línea base y meta | I-03A: historia térmica completa; base 0; meta ≥ 95 %. I-03B: estimación dentro de ±15 %; base sin medición; meta ≥ 80 % con ≥ 60 lotes por familia. I-03C: excursiones con vida consumida registrada; base 0; meta 100 %. I-03D: retenidos o descartados por vencimiento; base meses 13 a 15; meta −20 %. |
| 14. Momento de medición | I-03A e I-03B en el mes 15; I-03C mensual desde el mes 16; I-03D en el mes 28. |
| 15. Riesgo de adopción, probabilidad e impacto | R8-27: parámetros no representativos o lectura de la estimación como permiso para relajar RNG-04; P = 4, I = 5, exposición 20. R8-23: asociación sensor–lote errónea; P = 4, I = 5, exposición 20. |
| 16. Estrategia de mitigación | Validación por familia antes de habilitar; la estimación nunca alarga la vida más allá de la fecha impresa; la regla graduada y el bloqueo no cambian; tramos sin dato explícitos. |
| 17. Plan de contingencia si no rinde lo esperado | La familia queda con historia visible y FEFO por fecha impresa; estimación visible solo en M9; lote marcado «historia incompleta», sin estimación. |

## Ficha 4 — Innovación 4

Ficha de la innovación 4, «Tramo variable de la Operación ligado al costo de servir», desarrollada en el Capítulo 13, sección 13.4.

| Campo | Contenido |
| --- | --- |
| 1. Tipo de innovación | 4 — Modelo de negocio o de contratación |
| 2. Nombre de la innovación | Tramo variable de la Operación ligado al costo de servir (INN-04) |
| 3. Problema u oportunidad del caso que resuelve | Costo logístico prorrateado por zona con un criterio de 2016; Finanzas no sabe cuánto cuesta atender a un almacén de Empedrado (Distribuidora Puelche S.A., 2026c, cap. 1; criterio 11). TI de cuatro personas: toda función especializada debe ofrecerse como servicio costeado (cap. 10, restricción 9). |
| 4. Tecnología, práctica o modelo que la sustenta | Pago fijo más tramo variable con techo, ligado a la reducción comparable del costo por entrega sobre una canasta congelada, con índices de ajuste y protección del OTIF; acompañamiento comercial con la segmentación del RF-11.08. Agrega a lo obligatorio (F-14, componentes variables del E-25) una métrica de negocio del CLIENTE. |
| 5. Nivel de madurez y escala utilizada | Escala TRL de la Comisión Europea aplicada a la práctica contractual. Pago por nivel de servicio: TRL 9. Pago ligado al costo de servir: TRL 2; TRL 4 en el mes 20, TRL 6 en el 23 y TRL 7 en el 24. |
| 6. Fuentes citadas (APA 7.ª ed.) | FitzGerald et al. (2023); European Commission (2016). |
| 7. Dónde se inserta en la arquitectura | M6, M7 y M8 aportan hechos; M10 calcula costo comparable y OTIF sobre N-10 (capa 6); la capa 6 versiona la base; la capa 7 audita la cifra; el dato contable vive en el ERP. Contrato `inn04.liquidacion-tramo.v1` (Anexo 13.A). |
| 8. Paquetes de la EDT que la ejecutan | 5.4.3 (INN-04.P1), 8.3.3 (P2) y 8.3.4 (P3). Responsable: JP. |
| 9. Mes del cronograma en que se materializa | Acompañamiento desde el mes 21; primera liquidación con efecto de pago en el mes 24. |
| 10. Inversión requerida | Horas de diseño de la atribución, canasta e índices (meses 17 a 20) y del ensayo en sombra (meses 21 a 23). |
| 11. Efecto en el costo operacional | Acompañamiento comercial (meses 21 a 56) y conciliación mensual con Finanzas (meses 24 a 56). Para LafroX, el tramo es ingreso contingente que vale cero en los meses 21 a 23. |
| 12. Beneficio esperado y su cuantificación | Reducción verificable del costo por entrega de Puelche, desde el mes 24; Puelche paga menos si la solución no rinde y nunca más que el máximo. No se suma a las innovaciones 1, 3 o 5. |
| 13. Indicador de verificación, línea base y meta | I-04A: 1 − costo comparable / costo de referencia; base canasta de los meses 21 a 23; meta ≥ 5 % con OTIF ≥ 95 %. I-04B: liquidaciones en sombra reproducidas por Finanzas; meta 3 de 3. I-04C: recomendaciones con respuesta y efecto; meta 100 %. |
| 14. Momento de medición | I-04A en el mes 36 y mensual desde el 24; I-04B en los meses 21 a 23; I-04C mensual desde el mes 21. |
| 15. Riesgo de adopción, probabilidad e impacto | R8-28: variación del costo por causas externas o reducción por degradación del servicio, con disputa en la liquidación. P = 3, I = 4, exposición 12. |
| 16. Estrategia de mitigación | Canasta, índices y regla estacional fijados antes de la primera liquidación; protección del OTIF; denominador sin exclusiones; reproducción por Finanzas. |
| 17. Plan de contingencia si no rinde lo esperado | Acotar el tramo al cumplimiento del OTIF; suspender el devengo del período en disputa según el contrato; volver a la estructura de pago de las Bases. |

## Ficha 5 — Innovación 5

Ficha de la innovación 5, «Hoja de negocio del almacenero», desarrollada en el Capítulo 13, sección 13.5.

| Campo | Contenido |
| --- | --- |
| 1. Tipo de innovación | 5 — Experiencia de usuario, sostenibilidad o impacto social |
| 2. Nombre de la innovación | Hoja de negocio del almacenero (INN-05) |
| 3. Problema u oportunidad del caso que resuelve | 11.600 almacenes y minimarkets (Distribuidora Puelche S.A., 2026c, cap. 2.2) a los que no se puede exigir internet ni dispositivo (cap. 10, restricción 5); 38 % de la venta del canal se cobra en efectivo (cap. 4.7); un competidor ofrece una aplicación de autoatención (cap. 1). Puelche no devuelve al local la información de sus compras. |
| 4. Tecnología, práctica o modelo que la sustenta | Hoja por local con cuatro bloques (compras, productos dejados de pedir, por vencer, comparación agregada opcional), entregada en pantalla del terminal sin señal o impresa en la cabina; control de divulgación estadística y k-anonimidad para el bloque 4. Agrega a lo obligatorio (RF-11.08, RT-16.32, portal) una lectura del propio negocio sin internet. |
| 5. Nivel de madurez y escala utilizada | Escala TRL de la Comisión Europea. Informe sobre datos propios y control de divulgación: TRL 9. Uso en el micro-comercio sin conectividad: TRL 2; objetivo TRL 4 en los meses 13 y 14 y TRL 6 en los meses 19 y 20. |
| 6. Fuentes citadas (APA 7.ª ed.) | Hundepool et al. (2026); Sweeney (2002); Ley N.º 21.719 (2024); European Commission (2016). |
| 7. Dónde se inserta en la arquitectura | M10 calcula sobre N-10 (capa 6); M3 muestra en el terminal C-01 (capa 1); M6 imprime con la impresora de cabina del camión (Formulario T-11); la capa 7 limita la hoja al receptor y audita el tratamiento. Contrato `inn05.hoja-negocio.v1` (Anexo 13.A). |
| 8. Paquetes de la EDT que la ejecutan | 3.10.4.1 (INN-05.P1), 3.10.4.2 (P2), 3.10.4.3 (P3), 3.10.4.4 y 8.3.5 (P4) y 8.3.6 (P5). Responsable: IMP. |
| 9. Mes del cronograma en que se materializa | Mes 21 para los bloques 1 a 3; bloque 4 desde el mes 27, solo con dictamen legal favorable. |
| 10. Inversión requerida | Investigación con usuarios y prueba de comprensión (meses 13 y 14); privacidad, cálculo, precarga e impresión en cabina (meses 14 a 18); revisión legal del bloque 4 (meses 24 a 27). Sin hardware adicional. |
| 11. Efecto en el costo operacional | Cálculo mensual y papel térmico de las copias pedidas; minutos de explicación en la visita (meses 21 a 56). |
| 12. Beneficio esperado y su cuantificación | Efecto en la frecuencia y el tamaño del pedido y retención frente al competidor, valorizado solo si se demuestra al mes 33. Beneficio social: la información de gestión llega al cliente pequeño sin exigirle conexión. |
| 13. Indicador de verificación, línea base y meta | I-05A: hojas mostradas / locales que aceptan, y copias entregadas / pedidas; base 0; meta ≥ 90 % y ≥ 85 %. I-05B: comprensión; base prototipo; meta ≥ 80 % de 24. I-05C: compra en rutas con hoja frente a rutas sin hoja; meta estimar el efecto. I-05D: emisiones del bloque 4 sobre el umbral; meta 100 %. |
| 14. Momento de medición | I-05B antes del mes 19; I-05A en el mes 27; I-05C en el mes 33; I-05D en cada emisión. |
| 15. Riesgo de adopción, probabilidad e impacto | R8-29: el almacenero no la lee o no la entiende, o el bloque 4 permite inferir cifras de un vecino. P = 4, I = 3, exposición 12. |
| 16. Estrategia de mitigación | Prueba de comprensión y co-diseño; umbral y supresión verificados en cada emisión; revisión legal previa al bloque 4. |
| 17. Plan de contingencia si no rinde lo esperado | Versión de un bloque explicada de palabra en la visita; no activar el bloque 4. La visita, el efectivo y los canales obligatorios no cambian. |

Las cinco fichas comparten tres reglas: ninguna innovación agrega hardware al Formulario T-11, ninguna incorpora un modelo aprendido y ninguna cuenta como beneficio propio una meta que ya es alcance obligatorio. Los paquetes y meses coinciden con el Formulario T-14 y con el Anexo 7.D, y los riesgos con el Formulario T-16.

## Referencias

Las Bases se citan con su documento y el artículo, capítulo o código del requisito.

- DORA. (2024). *Accelerate state of DevOps report 2024*. Google Cloud. https://dora.dev/research/2024/dora-report/
- Distribuidora Puelche S.A. (2026a). *Bases Administrativas de Licitación N.º TFEP-01/2026: Contratación de Solución Integral de Software y Servicios de Operación*, artículos 28, 29 y 50.2, y Formulario T-19.
- Distribuidora Puelche S.A. (2026b). *Bases Técnicas Transversales de Licitación N.º TFEP-01/2026*, RT-05.30, RT-10.07, RT-14.06, RT-16.32 y RT-26.07.
- Distribuidora Puelche S.A. (2026c). *Caso 02: Logística. Especificaciones del problema y operación de Distribuidora Puelche S.A.*, capítulos 1, 2, 4, 6, 8, 10, 13 y 18.
- European Commission. (2016). Technology readiness levels (TRL). En *Horizon 2020 work programme 2016–2017: General annexes* (Anexo G). https://ec.europa.eu/research/participants/data/ref/h2020/other/wp/2016_2017/annexes/h2020-wp1617-annex-g-trl_en.pdf
- FitzGerald, C., Tan, S., Carter, E., & Airoldi, M. (2023). Contractual acrobatics: A configurational analysis of outcome specifications and payment in outcome-based contracts. *Public Management Review, 25*(9), 1796–1814. https://doi.org/10.1080/14719037.2023.2244501
- GS1 AISBL. (2022). *EPC Information Services (EPCIS) standard* (versión 2.0). https://ref.gs1.org/standards/epcis/2.0.0/
- Hundepool, A., Domingo-Ferrer, J., Franconi, L., Giessing, S., Lenz, R., Naylor, J., Schulte Nordholt, E., Seri, G., De Wolf, P.-P., Tent, R., Młodak, A., Gussenbauer, J., & Wilak, K. (2026). *Handbook on statistical disclosure control* (2.ª ed.). Center of Excellence SDC. https://sdctools.github.io/HandbookSDC/
- Jedermann, R., Nicometo, M., Uysal, I., & Lang, W. (2014). Reducing food losses by intelligent food logistics. *Philosophical Transactions of the Royal Society A, 372*(2017), 20130302. https://doi.org/10.1098/rsta.2013.0302
- Koutsoumanis, K., Taoukis, P. S., & Nychas, G.-J. E. (2005). Development of a Safety Monitoring and Assurance System for chilled food products. *International Journal of Food Microbiology, 100*(1–3), 253–260. https://doi.org/10.1016/j.ijfoodmicro.2004.10.024
- Ley N.º 21.719. (2024). Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales. Diario Oficial, 13 de diciembre de 2024. https://www.bcn.cl/leychile/navegar?idNorma=1209272
- Riesenegger, L., Santos, M. J., Ostermeier, M., Martins, S., Amorim, P., & Hübner, A. (2023). Minimizing food waste in grocery store operations: Literature review and research agenda. *Sustainability Analytics and Modeling, 3*, 100023. https://doi.org/10.1016/j.samod.2023.100023
- Shahin, M., Babar, M. A., & Zhu, L. (2017). Continuous integration, delivery and deployment: A systematic review on approaches, tools, challenges and practices. *IEEE Access, 5*, 3909–3943. https://doi.org/10.1109/ACCESS.2017.2685629
- Sweeney, L. (2002). k-anonymity: A model for protecting privacy. *International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems, 10*(5), 557–570. https://doi.org/10.1142/S0218488502001648

## Declaración de uso de IA

En cumplimiento de la sección 7.2 de las Aclaraciones de la licitación, la tabla siguiente declara el uso de herramientas de inteligencia artificial en este formulario, con la revisión humana de cada parte. La declaración se consolida en el Formulario A-6.

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
| --- | --- | --- | --- | --- | --- |
| Fichas 1 a 5 | Claude Code | Traslado de las secciones 13.1 a 13.5 a los 17 campos del formulario y cotejo con los Formularios T-14 y T-16 | Alto | Ninguno | [[REVISIÓN HUMANA]] |
