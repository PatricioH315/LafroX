# Formulario T-17: Protocolo de aceptación

Este formulario adjunta la propuesta de Protocolo de Aceptación de cada hito y del producto final, como exigen las Bases Administrativas para el Formulario T-17 y el RT-20.08. Para cada hito indica:

- los entregables;
- los criterios de aceptación objetivos;
- la evidencia requerida;
- los plazos de revisión;
- el procedimiento de observaciones;
- el acta de conformidad.

El protocolo aplica los Arts. 17.3 y 18 de las Bases Administrativas. Las pruebas que generan la evidencia están en el Formulario T-13. Su fundamento, en el Subdocumento 9, sección 9.3.2.

## Índice

- [1. Procedimiento general](#1-procedimiento-general)
  - [1.1 Expediente de aceptación](#11-expediente-de-aceptación)
  - [1.2 Plazos](#12-plazos)
  - [1.3 Observaciones y subsanación](#13-observaciones-y-subsanación)
  - [1.4 Acta de conformidad](#14-acta-de-conformidad)
- [2. Fichas por hito](#2-fichas-por-hito)
  - [H1 — Línea base de alcance y matriz de trazabilidad (mes 2)](#h1--línea-base-de-alcance-y-matriz-de-trazabilidad-mes-2)
  - [H2 — Arquitectura, plan de seguridad y modelo de datos (mes 4)](#h2--arquitectura-plan-de-seguridad-y-modelo-de-datos-mes-4)
  - [H3 — Infraestructura híbrida y ambientes (mes 6)](#h3--infraestructura-híbrida-y-ambientes-mes-6)
  - [H4 — Software de la Etapa 1 para pruebas (mes 10)](#h4--software-de-la-etapa-1-para-pruebas-mes-10)
  - [H5 — Certificación de la Etapa 1 (mes 12)](#h5--certificación-de-la-etapa-1-mes-12)
  - [H6 — Inicio de la marcha blanca de la Etapa 1 (mes 13)](#h6--inicio-de-la-marcha-blanca-de-la-etapa-1-mes-13)
  - [H7 — Paso a producción de la Etapa 1 (mes 16)](#h7--paso-a-producción-de-la-etapa-1-mes-16)
  - [H8 — Línea base y diseño de la Etapa 2 (mes 14)](#h8--línea-base-y-diseño-de-la-etapa-2-mes-14)
  - [H9 — Software de la Etapa 2 para pruebas (mes 17)](#h9--software-de-la-etapa-2-para-pruebas-mes-17)
  - [H10 — Certificación de la Etapa 2 y cierre del desarrollo (mes 18)](#h10--certificación-de-la-etapa-2-y-cierre-del-desarrollo-mes-18)
  - [H11 — Inicio de la marcha blanca de la Etapa 2 (mes 19)](#h11--inicio-de-la-marcha-blanca-de-la-etapa-2-mes-19)
  - [H12 — Paso a producción de la Etapa 2 y aceptación final (mes 21)](#h12--paso-a-producción-de-la-etapa-2-y-aceptación-final-mes-21)
- [3. Aceptación del producto final](#3-aceptación-del-producto-final)
- [Declaración de uso de IA](#declaración-de-uso-de-ia)

## 1. Procedimiento general

El procedimiento es el mismo para todos los hitos. Cambian los entregables, los criterios y la evidencia, que se detallan en la sección 2.

### 1.1 Expediente de aceptación

Cada hito se presenta con un expediente que contiene los cuatro elementos del Art. 18.2:

1. El entregable o artefacto: el documento, el software en su versión etiquetada o la infraestructura habilitada.
2. La evidencia objetiva de su verificación: los informes de prueba del Formulario T-13, con los resultados medidos frente a cada criterio.
3. La trazabilidad hacia los requisitos que satisface: el extracto de la matriz del Anexo 9.C correspondiente al hito.
4. El registro de las observaciones previas resueltas, con la evidencia de cada corrección.

Antes de entregarlo, el Líder de Calidad verifica que el expediente esté completo y firma una lista de comprobación con los criterios de la ficha del hito.

### 1.2 Plazos

El expediente se presenta en la fecha de entrega programada del Formulario T-15, Tabla 5.2, y nunca después de la fecha límite: diez días hábiles antes del último día hábil del mes del hito. El CLIENTE dispone de diez días hábiles para revisarlo y pronunciarse (Art. 18.3). Para los hitos H1 y H8, cuya reserva es menor que el plazo de subsanación, LafroX presenta una versión preliminar a la Contraparte Técnica una semana antes de la entrega, para resolver antes las observaciones de fondo (Formulario T-15, sección 5.5).

### 1.3 Observaciones y subsanación

La Contraparte Técnica formula sus observaciones por escrito, una por fila. Cada fila indica el entregable, el criterio de la ficha que considera incumplido, la evidencia que lo muestra y si la observación impide la aceptación o puede cerrarse después del acta con un plazo acordado. LafroX dispone de diez días hábiles para subsanar (Art. 18.3) y responde cada fila con la corrección y su evidencia. Una segunda presentación con observaciones de la misma naturaleza constituye atraso imputable a LafroX. Por eso cada observación se registra con su causa en el registro de calidad y se revisa contra los expedientes siguientes.

### 1.4 Acta de conformidad

El hito se entiende cumplido sólo con el acta firmada por la Contraparte Técnica (Art. 18.1). La aceptación no libera a LafroX de su responsabilidad por defectos posteriores (Art. 18.4). La Tabla T17.1 define el contenido mínimo del acta.

**Tabla T17.1 — Contenido del acta de conformidad. Fuente: elaboración propia a partir de las Bases Administrativas, Art. 18.**

| Campo | Contenido |
| --- | --- |
| Hito y entregables | Código del hito del Formulario E-25 y lista de entregables con su versión |
| Fechas | Entrega, observaciones, subsanación y firma |
| Criterios | Cada criterio de la ficha con su resultado: cumplido o no cumplido |
| Evidencia | Referencia a cada informe del expediente |
| Observaciones | Observaciones resueltas y, si las hay, observaciones no bloqueantes con su plazo de cierre |
| Firmas | Contraparte Técnica del CLIENTE; Jefe de Proyecto y Líder de Calidad de LafroX |

## 2. Fichas por hito

Cada ficha resume el hito del Formulario E-25, su fecha de entrega y su fecha límite según el Formulario T-15, los entregables, los criterios objetivos y la evidencia. Los hitos H6, H7, H11 y H12 tienen fecha contractual fija, pero no se aceptan con el mismo tipo de condición: H6 y H11 habilitan el inicio de la marcha blanca y se aceptan con condiciones de entrada; H7 y H12 cierran la marcha blanca y se aceptan con las condiciones copulativas del Art. 17.3.

### H1 — Línea base de alcance y matriz de trazabilidad (mes 2)

La ficha del H1 cierra el levantamiento.

| Campo | Contenido |
| --- | --- |
| Entregables | Línea base de alcance de la Etapa 1; matriz de trazabilidad (1.2.4); plan de calidad y de pruebas (1.5.1) |
| Criterios | 100 % de los requisitos ofertados con componente, paquete de la EDT y prueba prevista; cero requisitos sin origen; supuestos del SD3 validados o con consulta registrada |
| Evidencia | Matriz exportada desde el repositorio; acta de validación de los supuestos |
| Fechas | Entrega 09-03-2027; fecha límite 17-03-2027; reserva 6 días hábiles; versión preliminar una semana antes |
| Responsable | Líder de Calidad (matriz) y Jefe de Proyecto (línea base) |

### H2 — Arquitectura, plan de seguridad y modelo de datos (mes 4)

La ficha del H2 cierra el diseño de la Etapa 1.

| Campo | Contenido |
| --- | --- |
| Entregables | Documento de arquitectura y registro de decisiones; plan de seguridad; modelo de datos; informe de usabilidad (2.6.2) |
| Criterios | Cada componente del SD3 mapeado en la arquitectura lógica y física; cada decisión con alternativas y criterio; modelo de datos que responde la consulta de un retiro sanitario; flujos críticos probados con usuarios |
| Evidencia | Revisión del Comité de Arquitectura; informe de pruebas de usabilidad con hallazgos y cambios de diseño (RT-13.03) |
| Fechas | Entrega 29-04-2027; fecha límite 17-05-2027; reserva 12 días hábiles |
| Responsable | Arquitecto de Solución |

### H3 — Infraestructura híbrida y ambientes (mes 6)

La ficha del H3 habilita los ambientes donde se ejecutan las pruebas.

| Campo | Contenido |
| --- | --- |
| Entregables | Ambientes de Desarrollo, QA, Preproducción, Producción y Recuperación ante Desastres; sala técnica de Talca; observabilidad operativa; pipeline con las puertas G0 a G3 |
| Criterios | Cinco ambientes operativos (RT-04.01); Preproducción equivalente a Producción, con las diferencias declaradas en el SD4; ambientes reconstruibles desde código; puertas bloqueando con un cambio de prueba que incumple cada umbral |
| Evidencia | Informe de habilitación por ambiente; ejecución del pipeline que muestra cada puerta bloqueando; tablero de observabilidad con trazas de extremo a extremo |
| Fechas | Entrega 21-06-2027; fecha límite 16-07-2027; reserva 19 días hábiles |
| Responsable | Líder de Operación (SRE) |

### H4 — Software de la Etapa 1 para pruebas (mes 10)

La ficha del H4 acredita que el software está listo para certificar.

| Campo | Contenido |
| --- | --- |
| Entregables | Versión etiquetada de la Etapa 1; informe de integración, regresión e idempotencia (3.8.1); informe de cobertura |
| Criterios | 15 de 15 integraciones sin error; batería de regresión sin fallas; cobertura ≥ 70 % en lógica de negocio y ≥ 80 % global; 0 defectos críticos o altos abiertos |
| Evidencia | Informes por módulo entregados entre agosto y octubre de 2027; informe final de 3.8.1; extracto de la matriz 9.C para la Etapa 1 |
| Fechas | Entrega 20-10-2027; fecha límite 16-11-2027; reserva 19 días hábiles |
| Responsable | Líder de Calidad |

### H5 — Certificación de la Etapa 1 (mes 12)

La ficha del H5 certifica la Etapa 1 antes de su marcha blanca.

| Campo | Contenido |
| --- | --- |
| Entregables | Acta de certificación (3.8.7) con los informes de 3.8.2 a 3.8.6 y 3.8.8 |
| Criterios | Casos de aceptación firmados; p95 de la Tabla 9.2 a 21,99 TPS; punto de quiebre registrado; recuperación sin intervención ante cada falla; RTO ≤ 4 h y RPO ≤ 15 min; 0 hallazgos críticos o altos de la prueba de intrusión; 0 pérdidas y 0 duplicados en 14 h sin señal y 24 h sin enlace; WCAG 2.2 AA; despliegue sin interrupción y reversión ≤ 10 min |
| Evidencia | Informes del Formulario T-13, sección 10, incluidos la curva de carga (RT-09.07) y el informe íntegro del tercero (RT-11.20) |
| Fechas | Entrega 29-11-2027; fecha límite 17-01-2028; reserva 35 días hábiles |
| Responsable | Líder de Calidad |

### H6 — Inicio de la marcha blanca de la Etapa 1 (mes 13)

La ficha del H6 habilita la operación supervisada.

| Campo | Contenido |
| --- | --- |
| Entregables | Plan de reversión ensayado (4.1.2); registro de usuarios capacitados de la primera ola; migración conciliada (3.7.5) |
| Criterios | Reversión técnica ensayada en ≤ 10 minutos para el cambio de versión y reversión operativa de extremo a extremo en ≤ 40 minutos; 100 % de los usuarios de la ola capacitados; 0 diferencias no explicadas en la conciliación de la migración |
| Evidencia | Informe del ensayo de reversión con ambos cronómetros; registro de capacitación; acta de corte por sitio |
| Fechas | Fecha contractual fija: mes 13 (febrero de 2028) |
| Responsable | Líder Funcional (IMP) |

### H7 — Paso a producción de la Etapa 1 (mes 16)

La ficha del H7 cierra la marcha blanca con las seis condiciones copulativas del Art. 17.3.

| Campo | Contenido |
| --- | --- |
| Entregables | Informe de cierre de la marcha blanca con los indicadores diarios del SD7, Tabla 7.9; informe de los resultados de aceptación del Caso 02, capítulo 18 (R18, sección 3), que corresponden a la Etapa 1 |
| Criterios | 0 incidentes críticos o altos abiertos; 100 % del volumen real durante las cuatro últimas semanas; 0 minutos de indisponibilidad entre 05:30 y 07:00 y disponibilidad ≥ 99,9 %; p95 cumplidos; 0 diferencias de conciliación sin explicar; 100 % de usuarios certificados; prueba de intrusión por tercero, resiliencia y carga aplicable repetidas sobre la versión de cierre; resultados R18 de la Etapa 1 en su meta (sección 3) |
| Evidencia | Serie diaria de los indicadores de las cuatro últimas semanas; registros de conciliación; registro de certificación de usuarios; informes de intrusión, resiliencia y carga del cierre de marcha blanca |
| Fechas | Fecha contractual fija: mes 16 (mayo de 2028) |
| Responsable | Jefe de Proyecto |

### H8 — Línea base y diseño de la Etapa 2 (mes 14)

La ficha del H8 cierra el diseño de la Etapa 2.

| Campo | Contenido |
| --- | --- |
| Entregables | Línea base de alcance de la Etapa 2; diseño detallado; matriz de trazabilidad actualizada |
| Criterios | 100 % de los requisitos de la Etapa 2 con componente, paquete y prueba prevista; diseño sin cambios a contratos de la Etapa 1 en producción sin nueva versión de la interfaz |
| Evidencia | Matriz 9.C de la Etapa 2; registro de decisiones actualizado |
| Fechas | Entrega 13-03-2028; fecha límite 17-03-2028; reserva 4 días hábiles; versión preliminar en la semana del 6-03-2028 |
| Responsable | Arquitecto de Solución |

### H9 — Software de la Etapa 2 para pruebas (mes 17)

La ficha del H9 acredita que el software de la Etapa 2 está listo para certificar, sin afectar la Etapa 1.

| Campo | Contenido |
| --- | --- |
| Entregables | Versión etiquetada de la Etapa 2; informe de integración y regresión (3.9.1) |
| Criterios | 0 regresiones en la Etapa 1; integraciones de la Etapa 2 sin error; cobertura ≥ 70 % y ≥ 80 %; 0 defectos críticos o altos abiertos |
| Evidencia | Informe de 3.9.1; informe de cobertura; extracto de la matriz 9.C |
| Fechas | Entrega 18-05-2028; fecha límite 16-06-2028; reserva 21 días hábiles |
| Responsable | Líder de Calidad |

### H10 — Certificación de la Etapa 2 y cierre del desarrollo (mes 18)

La ficha del H10 certifica la Etapa 2 con ambas etapas activas.

| Campo | Contenido |
| --- | --- |
| Entregables | Acta de certificación (3.9.6) con los informes de 3.9.2 a 3.9.5 y 3.9.7 |
| Criterios | Casos de aceptación firmados por cadenas, transportistas, Comercial y Finanzas; p95 a 1,5× el peak con ambas etapas; RTO y RPO con ambas etapas; 0 hallazgos críticos o altos; WCAG 2.2 AA en los portales; despliegue sin interrumpir ninguna de las dos etapas |
| Evidencia | Informes del Formulario T-13 para la Etapa 2 |
| Fechas | Entrega 12-06-2028; fecha límite 17-07-2028; reserva 25 días hábiles |
| Responsable | Líder de Calidad |

### H11 — Inicio de la marcha blanca de la Etapa 2 (mes 19)

La ficha del H11 habilita la operación supervisada de la Etapa 2 en convivencia con la Etapa 1.

| Campo | Contenido |
| --- | --- |
| Entregables | Plan de reversión de la Etapa 2; registro de usuarios capacitados (7.3.2); cadenas certificadas para la mensajería electrónica |
| Criterios | Reversión técnica de la Etapa 2 en ≤ 10 minutos sin afectar la Etapa 1; reversión operativa de extremo a extremo en ≤ 40 minutos, el mismo objetivo que el Formulario T-18, sección 6.4, fija para el ensayo previo a cada corte; 100 % de los usuarios definidos certificados; fuente única de verdad para los datos compartidos (Art. 17.2) |
| Evidencia | Ensayo de reversión en Preproducción con cronómetro técnico y operativo; registro de certificación; informe de conciliación entre etapas |
| Fechas | Fecha contractual fija: mes 19 (agosto de 2028) |
| Responsable | Líder Funcional (IMP) |

### H12 — Paso a producción de la Etapa 2 y aceptación final (mes 21)

La ficha del H12 cierra la implementación y acepta el producto final.

| Campo | Contenido |
| --- | --- |
| Entregables | Informe de cierre de la marcha blanca de la Etapa 2; informe de los 16 resultados R18 (sección 3); expediente del producto final |
| Criterios | Las seis condiciones del Art. 17.3 para la Etapa 2; disponibilidad, desempeño e integridad de la Etapa 1 no degradados (Art. 17.2); prueba de intrusión por tercero, resiliencia y carga aplicable repetidas sobre la versión de cierre; resultados R18 en su meta, con las aceptaciones provisionales de la sección 3 |
| Evidencia | Serie diaria de indicadores; matriz 9.C completa con el estado de prueba de los 645 identificadores; informes de intrusión, resiliencia y carga del cierre de marcha blanca |
| Fechas | Fecha contractual fija: mes 21 (octubre de 2028) |
| Responsable | Jefe de Proyecto |

## 3. Aceptación del producto final

El producto final se acepta en el H12 con los 16 resultados del Caso 02, capítulo 18. La Tabla T17.2 resume, para cada uno, la meta, el momento y el método de medición del SD3, Anexo 3.J, Tabla 3.A.13, y la evidencia que se agrega al expediente.

**Tabla T17.2 — Resultados de aceptación del Caso y su evidencia. Fuente: elaboración propia a partir del SD3, Anexo 3.J, Tabla 3.A.13.**

| ID | Meta | Momento | Evidencia |
| --- | --- | --- | --- |
| R18-01 | Lista de clientes afectados por lote en < 2 h | Marcha blanca E1 | Simulacro de retiro con un lote real, cronometrado (JD-07 en el ensayo previo) |
| R18-02 | 100 % de recepciones con lote | Marcha blanca E1 | Recepciones con lote / recepciones que lo requieren, cuatro semanas |
| R18-03 | 100 % de cámaras y vehículos con registro térmico continuo | Marcha blanca E1 | Auditoría de series térmicas sin brechas y consulta del CLIENTE |
| R18-04 | OTIF 90 % (mes 15), 93 % (mes 19), 95 % (mes 32) | Mensual | Medición diaria con una sola definición; tramo del mes 32 aceptado en Operación |
| R18-05 | 100 % de pedidos con stock y crédito visibles | Marcha blanca E1 | Registro de consultas por pedido |
| R18-06 | 0 pedidos perdidos y 0 duplicados por falta de señal | Certificación y marcha blanca E1 | Prueba de 14 h sin señal y conciliación diaria |
| R18-07 | Ruta del día siguiente en < 20 min, corregible y registrada | Marcha blanca E1 | Medición diaria del tiempo de generación |
| R18-08 | 100 % de entregas con prueba de entrega el mismo día | Marcha blanca E1 | Pruebas de entrega / entregas, y constancia de recepción o consulta |
| R18-09 | 0 % de guías extraviadas o ilegibles | Marcha blanca E1 | Verificación de todas las guías del período |
| R18-10 | 100 % de diferencias de rendición con causa el mismo día | Marcha blanca E1 | Cierre diario por camión |
| R18-11 | 100 % de entregas con costo de servir | Marcha blanca E2 | Reconciliación con la contabilidad del mes |
| R18-12 | Pérdida de envases ≤ 7 % del parque al año | Marcha blanca E1 y 12 meses de Operación | Saldo conciliado por cliente y transportista; aceptación final tras 12 meses |
| R18-13 | 100 % de pedidos de cadenas certificadas por EDI | Marcha blanca E2 | Pedidos EDI / pedidos de cadenas y avisos de despacho en ≤ 2 min |
| R18-14 | Ocupación mínima 60 % por camión y promedio > 68 % | Marcha blanca de la ola de reparto | Ocupación de cada salida durante cuatro semanas |
| R18-15 | 100 % de faltantes con causa al producirse | Marcha blanca E1 | Trazabilidad del evento, incluso sin conexión |
| R18-16 | OTIF sin caída sin el planificador | Marcha blanca E1 | Dos semanas sin el planificador frente a dos semanas comparables |

Catorce resultados se aceptan al cierre de una marcha blanca. Dos se aceptan en forma provisional y se confirman en Operación: el tramo del mes 32 de R18-04 y la pérdida anual de R18-12, tras 12 meses. Para ellos, el acta del H12 registra la aceptación provisional, y la confirmación se registra en un acta posterior firmada por la Contraparte Técnica.

## Declaración de uso de IA

La tabla declara el apoyo de IA conforme a las Aclaraciones, §7.2.

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
| --- | --- | --- | --- | --- | --- |
| Formulario T-17 | Claude Code | Procedimiento, fichas por hito y resultados R18 desde el SD3, el T-15 y el E-25 | Alto | Ninguno | [[REVISIÓN HUMANA]] |
