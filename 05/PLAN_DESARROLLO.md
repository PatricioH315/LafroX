# Plan de desarrollo — Subdocumento 5

Fecha: 2 de octubre de 2026. Estado: desarrollo documental ejecutado; ensayos y revisión humana corresponden a implantación y presentación final.


## Resultado de ejecución

El índice definitivo sigue las aclaraciones: **5.1 Modelo**, **5.2 Gestión de datos**, **5.3 Estrategia de migración** y **5.4 Estrategia de desempeño**. La división inicial en seis apartados se corrigió: persistencia, analítica y gobierno se desarrollan dentro de 5.2. Esa distribución prevalece sobre la estructura inicial conservada más abajo como registro del plan.

| Etapa | Resultado documental | Evidencia |
| --- | --- | --- |
| P0 | Fuentes fijadas con SHA-256 y discrepancias de códigos cotejadas | FUENTES.json; Anexo 5-H |
| P1 | 59 entidades, 549 atributos, quince dominios y relaciones canónicas | 5.1; Anexos 5-A/B; modelo.json; diccionario.csv |
| P2 | Autoridad por sitio/agregado, transacciones y protocolo de eventos | 5.2; Anexo 5-C |
| P3 | 32,11 GB de migración estimados; saneamiento, dos ensayos, corte y reversión definidos | 5.3; Anexo 5-D |
| P4 | Índices, particiones, caché, consultas y sensibilidad alineados con arquitectura | 5.4; Anexo 5-E; CALCULOS.json |
| P5 | Modelo dimensional, fórmulas, linaje y objetivos 5 min / 2 h / 4 h | 5.2.4; Anexo 5-F |
| P6 | Calidad, protección, auditoría, exportación y retención por representación | 5.2.5–6; Anexo 5-G |
| P7 | Fuentes modulares, diagramas, raíces y compilación en PDFs separados | Raíces LaTeX; compilar_subdocumento_5.ps1 |
| P8 | Matriz de 30 requisitos, escenarios, criterios y condiciones de aceptación | MATRIZ_RT05.csv; Anexo 5-H; VERIFICACION.json |

ENS-1/ENS-2, pruebas AC/VD, aprobación del CLIENTE y revisión humana no se consideran realizados. PD-01–PD-10 del Anexo 5-H registran evidencias de implantación requeridas. La revisión visual y de compilación se registra en VERIFICACION.json.

## Objetivo y base

Desarrollar la propuesta de Modelo y gestión de datos de LafroX a partir de la arquitectura vigente en `rama-latex`, commit `2799de341bb425c0323119ca51d0e51e050d506a`. El resultado debe explicar cómo se representan, persisten, migran, explotan y gobiernan los datos del caso logístico, con trazabilidad a las bases y coherencia entre operación local, nube y dispositivos desconectados.

Fuentes que deben consultarse durante la redacción:

1. Bases Administrativas, Formulario T-7, Subdocumento 5: dominio, persistencia, migración, desempeño, separación transaccional/analítica y ciclo de vida.
2. Bases Técnicas Transversales, capítulo 5: RT-05.01–RT-05.30, distinguiendo requisitos obligatorios, según caso y deseables. Vincular RT-02.13 y los requisitos pertinentes de seguridad, continuidad y movilidad.
3. Caso_02_Logistica: sistemas actuales, volúmenes, ventanas de operación, numerales 15–17, parámetros de retención y alcance histórico.
4. `04/partes/4.1_logica/`, en especial modelo conceptual, módulos, interfaces, tecnologías, reglas de reconciliación, relación POD/DTE/acuse y supuestos.
5. `04/partes/4.2_fisica/`, memoria de cálculo, formularios T-11 y `Dimensionamiento/dimensionamiento/`: emplazamiento, capacidad, recuperación y cargas.
6. `04/anexos/logica/partes/`: eventos, interfaces, límites de contexto, continuidad y aceptación.

Las tres bases están disponibles en `../Bases MarkDown/` respecto de este repositorio dentro del espacio de trabajo. Registrar sus versiones y huellas al iniciar el inventario para que el desarrollo sea reproducible; esa ubicación externa no debe convertirse en una dependencia de compilación. Consultar las aclaraciones y los Subdocumentos 2 y 3 disponibles en `../LafroX-alvaro-md/` cuando afecten alcance o requerimientos.

## Estructura inicial del plan y cobertura (reorganizada conforme al índice obligatorio)

| Apartado | Contenido a desarrollar | Cobertura principal | Detalle de apoyo |
| --- | --- | --- | --- |
| 5.1 Dominio y modelo | Entidades, relaciones, cardinalidades, estados, claves, restricciones, normalización, propietarios y maestros compartidos | T-7 dominio; RT-02.13; RT-05.01 y 09 | DER por dominio; diccionario; matriz entidad–módulo–fuente de verdad |
| 5.2 Persistencia y consistencia | Motor y paradigma por dominio; transacciones; decisión ante particiones; autoridad local/nube; idempotencia, outbox y reconciliación | T-7 persistencia; RT-05.02; vínculos RT-05.16–23 | Matriz dominio–motor–sitio–consistencia; escenarios de conflicto |
| 5.3 Migración | Inventario de fuentes; alcance histórico; estimación de volumen; perfilado, saneamiento, mapeo, cargas, conciliación y reversión | RT-05.11–15 y 22 | Matriz origen–destino; reglas de transformación; protocolos de dos ensayos |
| 5.4 Desempeño | Cargas por consulta; índices; particiones; caché; crecimiento; mantenimiento; criterios de medición | T-7 desempeño; RT-05.05 y requisitos aplicables de capacidad | Catálogo de consultas; presupuesto de almacenamiento y pruebas propuestas |
| 5.5 Analítica | OLTP/OLAP; ingesta y transformación; hechos y dimensiones; indicadores; linaje; latencia; autoservicio y exportación | RT-05.05, 10 y 25–29; decisión de alcance sobre 30 | Modelo dimensional; fichas de indicadores; linaje hasta transacción |
| 5.6 Gobierno y ciclo de vida | Calidad; auditoría; datos personales; retención; archivo; eliminación; exportación y responsabilidades | RT-05.03, 04, 06–10 y 15 | Matrices de calidad, clasificación, retención y controles |

RT-05.16–24 se cotejarán con la arquitectura de integración del Subdocumento 4. En el 5 se precisarán esquemas, identificadores, linaje, validaciones y efectos sobre datos, remitiendo a los contratos de arquitectura. Registrar expresamente la cobertura y los pendientes; no asumir que el número de capítulo técnico coincide con el número de subdocumento.

## Secuencia de desarrollo

| Etapa | Trabajo | Entregables | Dependencia y criterio de cierre |
| --- | --- | --- | --- |
| P0 — Inventario y coherencia | Fijar fuentes, extraer requisitos, revisar cambios de alineación y diferencias lógica/física; separar hechos, decisiones y supuestos | Inventario con versión/huella; matriz de requisitos; registro de decisiones y pendientes | Base inicial. Cada diferencia tiene evidencia, impacto y tratamiento propuesto |
| P1 — Dominio y modelo | Desarrollar 5.1 y cubrir los doce módulos y los quince dominios de almacenamiento; identificar autoridad de maestros ERP | DER, diccionario y matriz de propietarios | P0. Cada entidad tiene identidad, relaciones, reglas y responsable; cada atributo documentado cumple RT-05.01 |
| P2 — Persistencia y continuidad | Desarrollar 5.2; definir límites transaccionales, réplicas, escritura autorizada, sincronización, conflictos y eliminación | Matriz de persistencia y escenarios de fallo/reconexión | P1. Ningún dominio tiene dos autoridades de escritura sin protocolo explícito; consistencia se justifica por operación |
| P3 — Migración | Desarrollar 5.3; mapear legados, estimar volumen y definir saneamiento, ensayos, corte y reversión | Plan de migración, mapeos y actas de ensayo vacías con criterios verificables | P1–P2. Todo alcance histórico tiene destino; cada diferencia de conciliación tiene tratamiento y responsable |
| P4 — Capacidad y desempeño | Desarrollar 5.4 y reconciliar cálculos con el dimensionamiento vigente | Índices y particiones propuestos; cargas representativas; cálculo trazable de capacidad | P1–P2. Se cubren peak de septiembre, sincronización acumulada y retenciones sin doble conteo |
| P5 — Analítica | Desarrollar 5.5; concretar modelo dimensional, ETL, calidad, linaje y tableros del caso | Modelo analítico y fichas de indicadores | P1–P2; ajuste con P4. Cada indicador tiene fórmula, granularidad, fuente, dimensiones, frecuencia y latencia |
| P6 — Gobierno | Desarrollar 5.6 y revisar políticas a través de OLTP, OLAP, dispositivos, archivos y respaldos | Políticas por dominio; matriz de calidad; procedimiento de exportación y eliminación | P1–P5. Se distingue dato operativo, raw, consolidado y copia; las retenciones se aplican a todas sus representaciones |
| P7 — Integración editorial | Redactar síntesis, referencias y supuestos; ensamblar cuerpo y anexos en LaTeX con plantilla LafroX | Raíz independiente, ensambladores, figuras y PDF del Subdocumento 5 | P1–P6. Compilación correcta, referencias resueltas y revisión visual de tablas, figuras y páginas |
| P8 — Revisión de cierre | Cotejar T-7, RT-05 y caso; revisar consistencia con Subdocs 3 y 4 y trazabilidad al T-12 | Matriz de cobertura final y lista explícita de asuntos por validar | P7. Ninguna obligación queda sin respuesta o pendiente identificado; ninguna prueba futura se presenta como ejecutada |

La secuencia expresa dependencias, no fechas comprometidas ni resultados de pruebas. P3, P4 y P5 pueden avanzar de forma independiente una vez estabilizadas las decisiones de P2.

## Decisiones que deben concretarse

- Descomponer los quince dominios lógicos sin confundirlos con quince servidores o motores independientes. Relacionar cada uno con módulos M1–M12 y despliegues del Subdoc-4.
- Precisar qué datos son maestros en Talca, cuáles residen en Aurora y qué subconjunto puede escribir Concepción o cada cross-dock. Especificar el protocolo de sincronización y evitar inferir replicación bidireccional por el solo uso de PostgreSQL.
- Incorporar la recepción física de retornos M8 al modelo local, de acuerdo con el último ajuste de arquitectura, y distinguir recepción, saldo de envases y contabilización.
- Separar pedido, detalle, asignación a lote, movimientos con SSCC, entrega parcial, evidencias POD, DTE y acuse; resolver cardinalidades y estados.
- Identificar la fuente de verdad del ERP para clientes, productos, proveedores, documentos y saldos; documentar identificadores externos y traducción mediante ACL.
- Explicar las decisiones CAP ante pérdida de comunicación por operación; no asignar una etiqueta global al sistema ni prometer consistencia inmediata entre sitios aislados.
- Reconciliar retención raw de telemetría de 30 días con la conservación histórica consolidada exigida por el caso. Incluir deduplicación de lecturas de gateways redundantes.
- Mantener el alcance analítico declarado en arquitectura y registrar el tratamiento de RT-05.30 como deseable, sin introducir analítica predictiva por defecto.

## Parámetros iniciales del caso

Estos valores proceden del caso y deben volver a cotejarse con sus aclaraciones al ejecutar P0.

| Familia | Alcance histórico a migrar | Retención indicada por el caso |
| --- | --- | --- |
| Clientes, productos y proveedores | Maestros completos | Definir ciclo de vida y restricciones por categoría |
| Ventas y pedidos | 3 años | Distinguir datos comerciales de documentos y evidencias relacionados |
| Inventario y movimientos | 2 años | Aplicar retención sanitaria cuando permitan reconstruir trazabilidad |
| Trazabilidad sanitaria | 5 años | Vida útil más 6 meses, con mínimo de 5 años |
| Cuentas por cobrar | Saldos vivos más 2 años | Precisar relación con respaldos y documentos tributarios |
| Documentos tributarios y respaldos | Identificar fuente y relación con el alcance anterior | 6 años |
| Registros de temperatura | Precisar fuente histórica disponible y calidad | 5 años |
| Evidencia de entrega | Precisar fuente histórica disponible y calidad | 6 años |
| Geolocalización de personas | Precisar disponibilidad y minimización | 12 meses |

El volumen total histórico está por estimar. Declarar cantidades, tamaño promedio, índices, crecimiento, copias y margen como supuestos trazables; no presentar una medición inexistente. Distinguir el horizonte de migración del período de retención.

Las referencias RT-05.10 y RT-05.15 usadas en la tabla de parámetros del caso no coinciden literalmente con las denominaciones del capítulo transversal. Conservar fuente y descripción de cada exigencia, registrar la discrepancia y evitar trasladar códigos sin cotejo.

## Anexos previstos

| Anexo | Contenido |
| --- | --- |
| 5-A | Diccionario de datos y reglas de integridad |
| 5-B | DER por dominio, relaciones entre dominios y propietarios |
| 5-C | Persistencia, autoridad y reconciliación por sitio |
| 5-D | Mapeo de migración, reglas de saneamiento y protocolos de conciliación |
| 5-E | Consultas, índices, particiones y memoria de capacidad |
| 5-F | Modelo dimensional, indicadores y linaje |
| 5-G | Calidad, clasificación, retención, archivo y eliminación |
| 5-H | Trazabilidad de requisitos, decisiones, supuestos y aceptación |

Los anexos conservarán el detalle; el cuerpo explicará y justificará las decisiones con referencias a ellos. La nomenclatura es propuesta y se estabilizará en P7.

## Verificación y condiciones de entrega

- Mantener una fila por requisito con fuente, carácter, sección, anexo, evidencia prevista, estado y pendiente; conectar con el T-12 sin duplicar su gobierno.
- Recorrer casos completos: pedido sin conexión y reenvío duplicado; asignación y retiro de lote; entrega parcial con POD/DTE; retorno físico M8; excursión térmica; sincronización tras corte; migración con duplicados y reversión.
- Para migración, definir dos ensayos completos en Preproducción, duración medida, recuentos, sumas de control, muestreo y explicación de diferencias. En la propuesta se entregan procedimientos y criterios, no actas con resultados ficticios.
- Verificar que la exportación cubra todos los datos del CLIENTE en formatos abiertos y que la consulta de históricos no migrados respete retención y permisos.
- Revisar nomenclatura, cifras, estados, límites transaccionales y autoridad de escritura contra la arquitectura base; registrar cambios necesarios antes de propagarlos.
- Compilar el documento y revisar visualmente el PDF completo, especialmente DER, diccionario, tablas extensas, saltos, índices y referencias.
- Entregar fuentes LaTeX, figuras y fuentes editables, PDF, matriz de trazabilidad y registro de supuestos y pendientes. El cierre documental no acredita implementación, migración ni aceptación operativa.
