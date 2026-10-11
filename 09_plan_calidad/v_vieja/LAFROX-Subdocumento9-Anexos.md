# Anexos del Subdocumento 9

Este archivo contiene el detalle que el Subdocumento 9 resume. El Anexo 9.A lista las métricas de calidad del producto por subcaracterística de ISO/IEC 25010; el Anexo 9.B, las reglas de análisis estático y dinámico con su umbral y su puerta; el Anexo 9.C, la matriz de trazabilidad entre los 645 identificadores del Formulario T-12 y su prueba de verificación; y el Anexo 9.D, la especificación de los datos de prueba. El plan de pruebas y validación está en el Formulario T-13 y el protocolo de aceptación, en el Formulario T-17. Las siglas BA, BTT, CAL, DES, IMP, SEG, SRE, DAT, SAST, SCA, DAST, SLSA, PCOV, p95, TPS, JD-nn, 9A-nn, 9B-nn y R18-nn se definen en la introducción del Subdocumento 9.

## Índice

- [Anexo 9.A — Umbrales de calidad del producto por subcaracterística](#anexo-9a--umbrales-de-calidad-del-producto-por-subcaracterística)
- [Anexo 9.B — Catálogo de reglas de análisis estático y dinámico](#anexo-9b--catálogo-de-reglas-de-análisis-estático-y-dinámico)
  - [9.B.1 Reglas y umbrales](#9b1-reglas-y-umbrales)
  - [9.B.2 Configuración por lenguaje](#9b2-configuración-por-lenguaje)
- [Anexo 9.C — Matriz de trazabilidad entre requisitos y pruebas](#anexo-9c--matriz-de-trazabilidad-entre-requisitos-y-pruebas)
  - [9.C.1 Reglas de construcción](#9c1-reglas-de-construcción)
  - [9.C.2 Matriz](#9c2-matriz)
- [Anexo 9.D — Especificación de los datos de prueba](#anexo-9d--especificación-de-los-datos-de-prueba)
  - [9.D.1 Volumen de los juegos de datos](#9d1-volumen-de-los-juegos-de-datos)
  - [9.D.2 Reglas de anonimización](#9d2-reglas-de-anonimización)
- [Referencias](#referencias)
- [Declaración de uso de IA](#declaración-de-uso-de-ia)

## Anexo 9.A — Umbrales de calidad del producto por subcaracterística

Este anexo desarrolla la Tabla 9.2 del Subdocumento 9. Cada fila es una métrica exigible: su umbral es criterio de salida de la prueba indicada, en el ambiente y en el paquete de la EDT que la ejecutan. Los umbrales provienen de las Bases, del Caso o de un subdocumento anterior; los que propone LafroX se identifican como tales en la columna de fuente.

La Tabla 9.A.1 presenta las 30 métricas.

**Tabla 9.A.1 — Métricas y umbrales por subcaracterística de ISO/IEC 25010. Fuente: elaboración propia a partir de las Bases Administrativas, Art. 24, de las Bases Técnicas Transversales, del Caso 02 y del SD4.**

| N.° | Característica | Subcaracterística | Métrica | Umbral | Fuente del umbral | Método de verificación | Ambiente | Paquete EDT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9A-01 | Funcionalidad | Completitud funcional | Requerimientos ofertados con caso de prueba aprobado | 100 % | Caso cap. 17.1; T-14 1.2.4 | Matriz 9.C (requisito → caso → resultado) | QA | 1.2.4, 3.8.1, 3.9.1 |
| 9A-02 | Funcionalidad | Corrección funcional | Casos de aceptación firmados sin defecto crítico/alto abierto | 100 % / 0 | BTT §20.1; BA Art. 17.3 | Pruebas de aceptación con la Contraparte Técnica | PREPROD | 3.8.2, 3.9.2 |
| 9A-03 | Funcionalidad | Pertinencia funcional | Resultados R18 medidos con su método en el mes comprometido | 16 de 16 | Caso cap. 18; SD3 Tabla 3.A.13 | Protocolo de aceptación T-17 | PROD | 4.2, 4.3 |
| 9A-04 | Desempeño | Comportamiento temporal | p95 confirmación de línea de picking | ≤ 1 s | Caso cap. 15 RT-09.01; SD4 Tabla 31 | Prueba de carga a 1,5× el peak | PREPROD | 3.8.4, 3.9.3 |
| 9A-05 | Desempeño | Comportamiento temporal | p95 registro de entrega en el local / otra transacción crítica de terreno, de extremo a extremo | ≤ 2 s / ≤ 3 s | Caso cap. 15 RT-09.01; BTT §9.1; SD4 Tabla 31 | Prueba de carga y prueba de terreno | PREPROD | 3.8.4, 3.8.3 |
| 9A-06 | Desempeño | Comportamiento temporal | p95 línea de preventa / consulta de stock y crédito / búsqueda con criterios compuestos (búsqueda global de RF-17.11) / informe estándar en línea | ≤ 1,5 s / ≤ 2 s / ≤ 3 s (≤ 2 s) / ≤ 30 s | Caso cap. 15 RT-09.01; BTT §9.1; SD3 Anexo 3.A, RF-17.11; SD4 Tabla 31 | Prueba de carga | PREPROD | 3.8.4, 3.9.3 |
| 9A-07 | Desempeño | Comportamiento temporal | p95 API consulta / escritura / carga de página / navegación entre vistas ya cargadas | ≤ 500 ms / ≤ 800 ms / ≤ 2 s / ≤ 1 s | BTT §9.1; SD4 Tabla 31 | Prueba de carga con medición en el navegador + regresión de desempeño semanal | QA/PREPROD | 1.5.2, 3.8.4 |
| 9A-08 | Desempeño | Capacidad | TPS sostenidos sin violar los p95 | ≥ 21,99 TPS; ≥ 10,41 TPS durante la ventana de 05:30 a 07:00, con 0 min de indisponibilidad (Subdocumento 9, sección 9.2.3) | BTT RT-09.06; Caso RT-10.05; SD4 §4.2 | Prueba de carga y estrés hasta el quiebre, y prueba de la ventana de despacho con la emisión de guías concentrada | PREPROD | 3.8.4, 3.9.3 |
| 9A-09 | Desempeño | Utilización de recursos | CPU/memoria en el peak × 1,5 | ≤ 70 % (supuesto) | SD4 plan de capacidad | Telemetría OpenTelemetry durante la prueba | PREPROD | 3.8.4 |
| 9A-10 | Compatibilidad | Interoperabilidad | Contratos OpenAPI 3.1 / AsyncAPI sin ruptura | 0 contratos rotos | BA Art. 23; SD6 §6.2 | Pruebas de contrato en CI | DEV/QA | 1.5.2 |
| 9A-11 | Compatibilidad | Interoperabilidad | Flujos de las 15 integraciones ejecutados sin error | 15 de 15 | BTT §20.1 (integración) | Pruebas de integración en QA | QA | 3.8.1, 3.9.1 |
| 9A-12 | Compatibilidad | Coexistencia | Regresiones de la Etapa 1 al integrar la Etapa 2 | 0 | BA Art. 17.2 | Regresión completa con E1 en producción | QA/PREPROD | 3.9.1 |
| 9A-13 | Usabilidad | Aprendizaje | Tiempo, pasos, error y aprendizaje por perfil; registrar 20 líneas sin asistencia y, por perfil, tiempos de la Tabla 3.A.4a del SD3 | Preventista: 20 líneas en ≤ 2 h y error ≤ 5 %; conductor/reparto: entrega completa en ≤ 3 min, ≤ 8 pasos y error ≤ 5 %; bodega: confirmación de línea en ≤ 1 s y error ≤ 5 %; segundo flujo sin asistencia por perfil; valores de la Tabla 3.A.4a | SD3 Anexos RNF; BTT RT-13.04 | Prueba de usabilidad con usuarios reales por perfil | PREPROD/Terreno | 2.6.2, 2.6.3 |
| 9A-14 | Usabilidad | Accesibilidad | Conformidad WCAG 2.2 AA (axe-core + manual) | 0 incumplimientos A/AA | BTT RT-13.01; W3C (2023) | Herramienta automática + revisión manual | QA/PREPROD | 3.8.2, 3.9.2 |
| 9A-15 | Usabilidad | Operabilidad en terreno | Uso con guantes a −22 °C, lluvia, >34 °C, sol directo, una mano y objetivos táctiles | ≥ 15×15 mm; 30 min a −22 °C; flujo completado bajo lluvia, >34 °C y sol directo sin pérdida ni error crítico | Caso cap. 15 RT-13.08; SD3 Anexos | Prueba del perfil operacional en cámara y terreno | Terreno | 3.8.3 |
| 9A-16 | Fiabilidad | Disponibilidad | Disponibilidad mensual de servicios críticos | ≥ 99,9 %; 0 min en 05:30–07:00 | BTT RT-10.01; Caso RT-10.05 | Medición sobre transacción real (marcha blanca y Operación) | PROD | 4.2, 8.1 |
| 9A-17 | Fiabilidad | Disponibilidad | Disponibilidad mensual de cada componente de la infraestructura: energía, climatización, red, servidores, base de datos y portal | ≥ 99,95 % | BTT cap. 7, sección 7.2; SD4 sección 4.2 | Medición mensual por componente con el monitoreo del NOC | PROD | 4.2, 8.1 |
| 9A-18 | Fiabilidad | Tolerancia a fallos | Operación sin enlace del CD / sin señal del dispositivo | 24 h / 14 h, 0 pérdidas ni duplicados | Caso RT-03.10 | Prueba de desconexión controlada | PREPROD/Terreno | 3.8.3 |
| 9A-19 | Fiabilidad | Recuperabilidad | RTO / RPO en conmutación real | ≤ 4 h / ≤ 15 min | SD4 Tabla 38 | Prueba DR antes del paso y semestral | DR | 3.8.5, 3.9.4, 8.1.3 |
| 9A-20 | Fiabilidad | Recuperabilidad | Sincronización tras reconexión y resolución de conflictos de stock del CD | Dispositivo ≤ 10 min; CD ≤ 2 h; 100 % de los conflictos de stock resueltos con la regla del SD4, Anexo 4-K, Tabla A.12, con el mismo resultado al repetir la reconciliación | Caso RT-03.13; BTT RT-03.12; SD4 Anexo 4-K | Prueba de desconexión controlada con reservas concurrentes del mismo stock, reconciliadas dos veces sobre los mismos eventos y comparadas con su bitácora | PREPROD | 3.8.3 |
| 9A-21 | Seguridad | Integridad / confidencialidad | Hallazgos críticos o altos abiertos (SAST, SCA, DAST, pentest) | 0 | BTT RT-04.05, RT-11.20; BTT §20.1 | Puertas G2/G4 y pentest por tercero | QA/PREPROD | 1.5.2, 3.8.6, 3.9.5 |
| 9A-22 | Seguridad | Confidencialidad | Datos productivos en ambientes no productivos de prueba | 0 registros sin anonimización verificada; DR se trata como réplica productiva restringida | SD3 Anexos RNF; Ley 21.719 | Escaneo Macie de QA y PREPROD y prueba de reidentificación | QA/PREPROD | 1.5.1 |
| 9A-23 | Seguridad | Responsabilidad | Trazas de auditoría de acceso a datos sensibles | 100 % de consultas registradas | Caso RT-16.09 | Prueba funcional de auditoría | QA | 3.8.2 |
| 9A-24 | Mantenibilidad | Capacidad de prueba | Cobertura lógica de negocio / global | ≥ 70 % / ≥ 80 % | BA Art. 24; SD1; SD6 | Puerta G2 en CI | DEV/CI | 1.5.2 |
| 9A-25 | Mantenibilidad | Modularidad | Acoplamiento entre los 12 módulos: dependencias prohibidas; inestabilidad Ce/(Ca+Ce) de los módulos núcleo en PHP | 0 violaciones; inestabilidad ≤ 0,5 (supuesto) | BTT RT-02.02; SD4 §4.1; Martin (2003) | deptrac y PhpMetrics en PHP; detekt en Kotlin; ESLint en TypeScript | DEV/CI | 1.5.2 |
| 9A-26 | Mantenibilidad | Analizabilidad | Complejidad ciclomática por método | ≤ 10 | Supuesto LafroX (Subdocumento 9, sección 9.1.4) | PHPMD, detekt y ESLint miden la ciclomática según lenguaje | DEV/CI | 1.5.2 |
| 9A-27 | Mantenibilidad | Modificabilidad | Deuda técnica bloqueante / duplicación de código | 0 / ≤ 3 % de las líneas (supuesto) | SD4 §4.2.4.1; T-10; propuesta de LafroX para la duplicación | Análisis estático (PhpMetrics, PHPCPD, jscpd); registro 8.2.4 | DEV/CI | 1.5.2, 8.2.4 |
| 9A-28 | Portabilidad | Instalabilidad | Mismo artefacto promovido QA → PREPROD → PROD sin recompilar | 100 % de despliegues | BTT RT-04.08 | Promoción por digest de imagen firmada | QA→PROD | 3.8.8, 3.9.7 |
| 9A-29 | Portabilidad | Adaptabilidad | Ambientes reconstruidos desde IaC (Terraform/Ansible) | 100 %; ambiente efímero ≤ 30 min (supuesto) | SD4 §4.2; BTT RT-04.14 | Reconstrucción desde código en QA | QA | 1.5.2 |
| 9A-30 | Portabilidad | Reemplazabilidad | Exportación completa en formato abierto | 100 % de entidades | BA Art. 23 | Prueba de exportación | PREPROD | 3.9.2 |

La tabla reúne 30 métricas: funcionalidad 3, desempeño 6, compatibilidad 3, usabilidad 3, fiabilidad 5, seguridad 3, mantenibilidad 4, portabilidad 3. El desempeño y la fiabilidad concentran más métricas porque son las características de las que depende el despacho en la ventana de 05:30 a 07:00 y la operación sin enlace. Las métricas 9A-04 a 9A-07 cubren los 11 umbrales p95 de la Tabla 31 del SD4. Los umbrales propuestos por LafroX son el 70 % de utilización de la métrica 9A-09, la inestabilidad de 9A-25, la complejidad ciclomática de 9A-26, la duplicación de 9A-27 y los 30 minutos del ambiente efímero de 9A-29; las demás reproducen un valor de las Bases, del Caso o de un subdocumento anterior.

La calidad de datos se mide con los indicadores del SD5. La Tabla 9.A.2 explicita los tres indicadores que este plan agrega como criterio de salida para migración, marcha blanca y operación.

**Tabla 9.A.2 — Indicadores de calidad de datos ISO/IEC 25012 usados por el plan. Fuente: SD5, sección 5.2.5 y Anexos 5-C y 5-H.**

| Dimensión | Indicador | Umbral | Punto de medición | Prueba / paquete |
| --- | --- | --- | --- | --- |
| Completitud | Entidades críticas migradas con clave, estado y trazabilidad exigida | 100 % en SKU, clientes, ubicaciones, lotes, saldos, documentos y reglas vigentes | Ensayos de migración y corte | T-13 Migración; 3.7.2–3.7.5 |
| Exactitud | Saldos, lotes y documentos conciliados contra origen aprobado | 0 diferencias no explicadas; diferencias justificadas con acta del responsable de datos | Ensayos de migración, marcha blanca y cierre de hito | T-13 Migración; T-17 H5/H10/H12 |
| Consistencia | Integridad referencial y reglas de dominio de 5-C aprobadas | 100 % de reglas críticas sin rechazo abierto; todo rechazo con causa y tratamiento | Carga en Preproducción, marcha blanca y tablero de datos | T-13 Sistema y migración; paquete 8.1 |

Estos indicadores cubren el mínimo que exige el RT-05.04 —completitud, exactitud y consistencia— y remiten las demás dimensiones de ISO/IEC 25012 al tablero y las reglas del SD5.

## Anexo 9.B — Catálogo de reglas de análisis estático y dinámico

Este anexo detalla las reglas que ejecutan las puertas G1 a G4 descritas en la sección 9.2.1 del Subdocumento 9. Cada regla tiene una herramienta, un umbral y una puerta; ninguna regla bloqueante admite excepción manual, y ninguna regla de seguridad admite excepción en ninguna puerta. La única excepción es la regla 9B-19, de regresión de desempeño, que el Líder de Calidad puede aceptar con registro de deuda cuando la causa está identificada y no se incumple un umbral p95 (Subdocumento 9, sección 9.2.1).

### 9.B.1 Reglas y umbrales

La Tabla 9.B.1 lista las 27 reglas, con la herramienta en cada lenguaje.

**Tabla 9.B.1 — Reglas de análisis, umbral y puerta. Fuente: elaboración propia a partir de las Bases Técnicas Transversales, RT-04.03, RT-04.05 y RT-04.11, del SD4, sección 4.2.4.1, y del SD6, sección 6.2.2.**

| N.° | Regla | Lenguaje o capa | Herramienta | Operador y umbral | Puerta | Fuente |
| --- | --- | --- | --- | --- | --- | --- |
| 9B-01 | Cobertura de lógica de negocio | PHP / Laravel | PHPUnit + Xdebug/PCOV | ≥ 70 % | G2 | BA Art. 24; RT-04.11 |
| 9B-02 | Cobertura unitaria global | PHP / Laravel | PHPUnit + Xdebug/PCOV | ≥ 80 % | G2 | SD1 sección 1.3; SD6 sección 6.2 |
| 9B-03 | Cobertura de lógica de negocio | Kotlin / Android | JUnit 5 + Kover | ≥ 70 % | G2 | BA Art. 24; RT-04.11 |
| 9B-04 | Cobertura unitaria global | Kotlin / Android | JUnit 5 + Kover | ≥ 80 % | G2 | SD1 sección 1.3; SD6 sección 6.2 |
| 9B-05 | Cobertura unitaria global | Angular / TypeScript | Jest (Istanbul) | ≥ 80 % | G2 | SD1 sección 1.3; SD6 sección 6.2 |
| 9B-06 | Errores de análisis estático (nivel 8) | PHP / Laravel | PHPStan + Larastan | ≤ 0 | G2 | SD4 sección 4.2.4; SD6 |
| 9B-07 | Infracciones de estilo | PHP / Laravel | Laravel Pint | ≤ 0 | G1 | SD4 sección 4.2.4 |
| 9B-08 | Complejidad ciclomática máxima por método | PHP / Kotlin / TS | PHPMD · detekt · ESLint complexity | ≤ 10 | G2 | Supuesto LafroX (McCabe, 1976) |
| 9B-09 | Violaciones de dependencia entre módulos | PHP / Laravel | deptrac | ≤ 0 | G2 | BTT RT-02.02; SD4 sección 4.1 |
| 9B-10 | Inestabilidad de los módulos núcleo (Ce/(Ca+Ce)) | PHP / Laravel | PhpMetrics | ≤ 0,5 | G2 | Supuesto LafroX (Martin, 2003) |
| 9B-11 | Infracciones de estilo / lint | Kotlin / Android | detekt + ktlint | ≤ 0 | G1 | Supuesto LafroX |
| 9B-12 | Errores de lint | Angular / TypeScript | ESLint | ≤ 0 | G1 | Supuesto LafroX |
| 9B-13 | Vulnerabilidades críticas o altas (SAST/SCA) | Todos | GitLab SAST + composer audit / npm audit | ≤ 0 | G2 | BTT RT-04.05 |
| 9B-14 | Secretos detectados en el código | Todos | GitLab Secret Detection | ≤ 0 | G1 | BTT RT-04.05, RT-04.09 |
| 9B-15 | Vulnerabilidades críticas o altas en imágenes | Contenedores | Amazon Inspector / ECR scan | ≤ 0 | G3 | BTT RT-04.05 |
| 9B-16 | Alertas altas de DAST | Portales y API | OWASP ZAP | ≤ 0 | G4 | BTT sección 20.1; SD3 RNF-14.07 |
| 9B-17 | Contratos OpenAPI/AsyncAPI rotos | API | Pact (consumidor y proveedor) · Spectral (definiciones) | ≤ 0 | G2 | SD6 sección 6.2 |
| 9B-18 | Pruebas en falla | Todos | Ejecución CI | ≤ 0 | G2 | BTT sección 20.1 |
| 9B-19 | Regresión de p95 respecto de la versión anterior | API | k6 en QA (semanal) | ≤ 10 % | G3 | SD4 sección 4.2.4; supuesto del 10 % |
| 9B-20 | Incumplimientos WCAG 2.2 A o AA confirmados | Portales / app | axe-core + revisión manual | ≤ 0 | G4 | BTT RT-13.01 |
| 9B-21 | Revisores aprobadores por solicitud de fusión | Todos | GitLab (rama protegida) | ≥ 1 | G1 | BTT RT-04.03 |
| 9B-22 | Deuda técnica clasificada como bloqueante | PHP / Laravel | PhpMetrics + registro 8.2.4 | ≤ 0 | G2 | T-10, sección 6.2 |
| 9B-23 | Duplicación de código | PHP / Kotlin / TypeScript | PHPCPD · jscpd | ≤ 3 % de las líneas | G2 | Supuesto LafroX; SD4 sección 4.2.4.1 |
| 9B-24 | Cobertura de lógica de negocio | Angular / TypeScript | Jest (Istanbul) sobre servicios, almacenes de estado, validadores y guardas | ≥ 70 % | G2 | BA Art. 24; RT-04.11 |
| 9B-25 | Importaciones prohibidas entre módulos | Kotlin / Android | detekt (ForbiddenImport) | ≤ 0 | G2 | BTT RT-02.02; SD4 sección 4.1 |
| 9B-26 | Importaciones prohibidas y ciclos entre módulos | Angular / TypeScript | ESLint (no-restricted-imports e import/no-cycle) | ≤ 0 | G2 | BTT RT-02.02; SD4 sección 4.1 |
| 9B-27 | Hallazgos críticos o altos de seguridad de la aplicación | Android | MobSF contra OWASP MASVS, estático y dinámico | ≤ 0 | G2 y G4 | BTT RT-04.05 |

Las 27 reglas se reparten entre PHP, Kotlin, TypeScript y la plataforma. De ellas, 16 exigen cero hallazgos y las 11 restantes fijan una cota numérica o se miden sin bloqueo. Las reglas de cobertura, SAST, SCA, secretos e imágenes cubren los mínimos del RT-04.05 y del RT-04.11; las de complejidad ciclomática, inestabilidad y duplicación son propuestas de LafroX; la de deuda bloqueante recoge lo ya declarado en el SD4 y el T-10, con su fuente en la Tabla 9.B.1.

### 9.B.2 Configuración por lenguaje

La configuración de cada herramienta se versiona en el repositorio de cada componente, de modo que un cambio de regla pasa por revisión por pares como cualquier cambio de código. La Tabla 9.B.2 resume la configuración base.

**Tabla 9.B.2 — Configuración base de las herramientas de análisis. Fuente: elaboración propia.**

| Lenguaje o capa | Herramienta | Configuración base |
| --- | --- | --- |
| PHP 8.5 / Laravel 13 | PHPStan + Larastan | Nivel 8; sin línea base de errores heredados; análisis de los 12 módulos y sus pruebas. |
| PHP 8.5 / Laravel 13 | Laravel Pint | Preajuste laravel; verificación en modo de prueba, sin reescritura en CI. |
| PHP 8.5 / Laravel 13 | PHPMD | Reglas de tamaño y complejidad ciclomática: CyclomaticComplexity 10, NPathComplexity 200, ExcessiveMethodLength 60 líneas. |
| PHP 8.5 / Laravel 13 | PhpMetrics | Inestabilidad de módulos núcleo ≤ 0,5; deuda técnica clasificada como bloqueante = 0. |
| PHP / TypeScript | PHPCPD y jscpd | Medición de duplicación en cada integración; sobre el 3 % de las líneas bloquea G2. |
| PHP 8.5 / Laravel 13 | deptrac | Una capa por módulo M1 a M12 más la capa compartida; cada módulo sólo accede a otro por su contrato público (interfaces y eventos). |
| PHP 8.5 / Laravel 13 | PHPUnit con PCOV | Informe Cobertura por paquete; la lógica de negocio son los espacios de nombres Domain y Application de cada módulo. |
| Kotlin / Android | detekt + ktlint | Conjunto por defecto con ComplexMethod 10 y LongMethod 60; ktlint estándar. |
| Kotlin / Android | JUnit 5 + Kover | Cobertura sobre los módulos de dominio y sincronización; las vistas se prueban con Espresso. |
| Angular / TypeScript | ESLint + Jest | Reglas recomendadas de Angular y TypeScript, complexity 10, no-restricted-imports con los paquetes internos de cada módulo e import/no-cycle; cobertura de Jest por proyecto, con un informe aparte para servicios, almacenes de estado, validadores y guardas, que son la lógica de negocio. |
| Kotlin / Android | detekt (ForbiddenImport) | Prohíbe importar los paquetes internos de otro módulo; sólo se admiten sus interfaces públicas. |
| Android | MobSF | Análisis estático del paquete en G2 y dinámico sobre un dispositivo de QA antes de G4, contra OWASP MASVS; un hallazgo crítico o alto bloquea. |
| Angular / TypeScript | Playwright | Pruebas de extremo a extremo de las consolas y los portales en QA, sobre los flujos del SD3 por perfil. |
| API y mensajería | Pact y Spectral | Pact ejecuta en G2 las expectativas de cada consumidor contra el proveedor; Spectral valida las definiciones OpenAPI 3.1 y AsyncAPI. |
| Todos | GitLab SAST, Secret Detection y auditoría de dependencias | Severidades crítica y alta bloquean; media se registra con plazo de 30 días corridos (SD4, sección 4.2.4.1.4). |
| Contenedores | Amazon Inspector / escaneo de ECR | Bloqueo ante vulnerabilidad crítica o alta en la imagen candidata. |
| Portales y API | OWASP ZAP | Escaneo activo en QA guiado por la definición OpenAPI 3.1; alerta alta bloquea G4. |
| Portales y aplicación | axe-core | Reglas WCAG 2.2 A y AA; cualquier incumplimiento confirmado por herramienta o revisión manual bloquea G4. |
| API | k6 | Escenario de regresión semanal en QA; bloquea G3 si el p95 empeora más de 10 % frente a la versión anterior. |

Con esta configuración, las mismas cotas de complejidad rigen en los tres lenguajes, y la frontera entre módulos se verifica en el código y no sólo en el diagrama del SD4. La deuda que una herramienta detecta y que no bloquea queda en el registro de deuda técnica del paquete 8.2.4.

## Anexo 9.C — Matriz de trazabilidad entre requisitos y pruebas

Este anexo completa la cadena de trazabilidad de la sección 9.2.5 del Subdocumento 9. Para cada uno de los 645 identificadores del Formulario T-12 indica la prueba que lo verifica, el ambiente, el paquete de la EDT que la ejecuta, el hito en que se acepta y el número de casos estimado. El componente que satisface cada requisito y la sección de la propuesta que lo desarrolla están en el Formulario T-12 y no se repiten aquí.

### 9.C.1 Reglas de construcción

La matriz aplica cuatro reglas. Primera: un requisito funcional o no funcional recibe cinco casos si es de prioridad crítica, tres si es alta y dos si es media, según su prioridad en los Anexos 3.A y 3.B del SD3. Segunda: un requisito técnico transversal recibe un caso de verificación, porque cada uno enuncia una condición de las Bases con su criterio de aceptación; si el texto enumera varias condiciones, el caso las recorre todas y el informe las registra por separado. Tercera: un identificador que el SD3 declara absorbido por otra fila, o alias de ella, se verifica con la prueba de esa fila y no suma casos. Cuarta: un identificador en estado «No cumple» queda sin prueba, para que la brecha sea visible. La prueba de los requisitos no funcionales sigue la verificación prevista en el SD3; la de los requisitos técnicos, el capítulo de las Bases Técnicas Transversales al que pertenecen. Cuando la prueba es la de sistema y aceptación de usuario, la fila copia el resultado esperado del SD3 o el texto del requisito, de modo que el caso verifica esa condición y no una genérica. Los requisitos de entregables de la oferta, sin ambiente ni paquete de la EDT, se inspeccionan en el documento que los contiene al presentar la oferta. El paquete y el hito dependen de la etapa del requisito.

La Tabla 9.C.1 resume la matriz.

**Tabla 9.C.1 — Síntesis de la matriz de trazabilidad. Fuente: elaboración propia a partir del Formulario T-12 y del SD3, Anexos 3.A y 3.B.**

| Grupo | Identificadores | Con prueba propia | Sin prueba propia | Casos estimados |
| --- | --- | --- | --- | --- |
| RF | 181 | 176 | 5 | 547 |
| RNF | 90 | 86 | 4 | 308 |
| RT | 374 | 356 | 18 | 356 |
| Contratos de las 15 integraciones | — | — | — | 105 |
| **Total** | **645** | **618** | **27** | **1.316** |

La matriz asigna prueba propia a 618 de los 645 identificadores. Los 27 restantes son 18 en estado «No cumple» y 9 absorbidos por otra fila. Con los 105 casos de contrato de las integraciones, siete por cada una de las 15, el catálogo suma 547 + 308 + 356 + 105 = 1.316 casos, la cifra que usa la sección 9.2.3 del Subdocumento 9.

### 9.C.2 Matriz

La Tabla 9.C.2 presenta la matriz completa, en el orden del Formulario T-12.

**Tabla 9.C.2 — Matriz de trazabilidad entre requisitos y pruebas. Fuente: elaboración propia a partir del Formulario T-12, del SD3, Anexos 3.A y 3.B, y del Formulario T-14.**

| ID | Estado T-12 | Prueba de verificación | Ambiente | Paquete EDT | Hito de aceptación | Casos |
| --- | --- | --- | --- | --- | --- | --- |
| RF-01.01 | Cumple | Sistema y aceptación de usuario — El comparativo pedido vs. recibido queda registrado al cerrar la recepción y toda discrepancia queda disponible en el módulo de calidad. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 · CP-RF-01.01-01 a -05 |
| RF-01.02 | Cumple | Sistema y aceptación de usuario — El 100 % de los ítems con trazabilidad obligatoria registran lote; campo vacío muestra "Lote requerido para este producto" e impide continuar. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 · CP-RF-01.02-01 a -05 |
| RF-01.03 | Cumple | Sistema y aceptación de usuario — El 100 % de los SKU con control de vencimiento habilitado tienen fecha registrada y asociada al lote al cerrar la recepción; campo vacío bloquea el avance. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 · CP-RF-01.03-01 a -05 |
| RF-01.04 | Cumple | Sistema y aceptación de usuario — La no conformidad queda registrada con todos los campos requeridos y la fotografía es descargable desde el módulo de calidad. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-01.04-01 a -03 |
| RF-01.05 | Cumple | Sistema y aceptación de usuario — La cantidad del lote queda bloqueado para picking de forma inmediata y el perfil de calidad recibe la notificación en ≤ 5 min | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-01.05-01 a -03 |
| RF-01.06 | Cumple | Sistema y aceptación de usuario — Código GS1 válido autocompleta los campos en pantalla; código no encontrado muestra "Producto no encontrado" y habilita ingreso manual. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-01.06-01 a -03 |
| RF-01.07 | Cumple | Sistema y aceptación de usuario — El SSCC se genera y la etiqueta se imprime con los campos GTIN (AI 01), lote (AI 10), fecha de vencimiento (AI 17) y fecha de recepción (AI 11). | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 · CP-RF-01.07-01 a -02 |
| RF-01.08 | Cumple | Sistema y aceptación de usuario — La asociación SSCC–ubicación queda registrada; intento de ubicación incompatible es bloqueado con mensaje descriptivo. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 · CP-RF-01.08-01 a -02 |
| RF-01.09 | Cumple | Sistema y aceptación de usuario — La conciliación diaria no muestra diferencias entre el inventario del sistema y el del ERP; ante ERP no disponible, el sistema informa al usuario y reintenta sin intervención. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 · CP-RF-01.09-01 a -05 |
| RF-01.10 | Cumple | Sistema y aceptación de usuario — El sistema no permite guardar una ficha con campos obligatorios vacíos y registra historial de cambios de GTIN o SKU con fecha y usuario. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 · CP-RF-01.10-01 a -05 |
| RF-01.11 | Cumple | Sistema y aceptación de usuario — Intento de ubicar un SKU congelado fuera de zona congelada es bloqueado con mensaje "Incompatibilidad térmica: requiere zona congelado". | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 · CP-RF-01.11-01 a -05 |
| RF-02.01 | Cumple | Sistema y aceptación de usuario — (a) Al configurar un nuevo CD, el sistema permite crear y mapear zonas, pasillos y posiciones con coordenada única. (b) Cada posición tiene zona térmica asociada con rango de temperatura. (c) No se permite crear posiciones sin zona asignada. (d) Cambios de topología quedan registrados con usuario, fecha y detalle del cambio. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-02.01-01 a -03 |
| RF-02.02 | Cumple | Sistema y aceptación de usuario — El sistema expone un panel donde el usuario visualiza: (a) el stock físico totalizado por SKU, (b) el desglose por instalación, y (c) el desglose por zona operativa dentro de cada instalación. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-02.02-01 a -03 |
| RF-02.03 | Cumple | Sistema y aceptación de usuario — (a) Al ejecutar el cálculo, el sistema presenta una propuesta con: producto, ubicación actual, ubicación propuesta, motivo (clasificación ABC, peso, volumen o zona). (b) El jefe de bodega puede aprobar, rechazar o modificar cada movimiento individualmente. (c) Los movimientos aprobados generan instrucciones de reubicación asignables a dispositivos de operarios, con indicación de ubicación origen y destino. (d) Cada reubicación ejecutada queda registrada con operario, fecha/hora, y ubicaciones origen/destino. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-02.03-01 a -03 |
| RF-02.04 | Cumple | Sistema y aceptación de usuario — (a) El operario recibe en su dispositivo la lista de posiciones a contar, sin cantidad teórica visible. (b) Al ingresar la cantidad física, si la diferencia valorizada es menor o igual al umbral configurado por el jefe de bodega para ese recinto, el sistema registra el ajuste automáticamente con la causa seleccionada (sobrante, falta, error de ubicación, daño, vencimiento). (c) Si la diferencia supera el umbral, el sistema marca la tarea como 'Pendiente de Autorización' y notifica al jefe de bodega. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-02.04-01 a -03 |
| RF-02.05 | Cumple | Sistema y aceptación de usuario — (a) Al consultar stock, el preventista visualiza la cantidad disponible por SKU para su CD asignado. (b) La consulta refleja el stock actualizado tras cada transacción confirmada. (c) En modo offline, la consulta muestra «Dato de las HH:MM del DD/MM». (d) Al sincronizar un pedido tomado offline, si el stock disponible es insuficiente para alguna línea, el sistema marca esa línea como «sin stock disponible» y notifica al preventista. (e) Los conflictos entre pedidos simultáneos se resuelven por orden de confirmación en el servidor central (S-08, RNG-01); un pedido capturado sin señal toma su lugar al sincronizar. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-02.05-01 a -03 |
| RF-02.06 | Cumple | Sistema y aceptación de usuario — (a) Al consultar stock, el usuario visualiza: stock físico en sitio, stock comprometido, stock disponible y stock en tránsito hacia ese sitio con fecha/hora estimada de llegada. (b) El stock en tránsito NO se suma al disponible para venta hasta la recepción confirmada en destino. (c) Al confirmar la recepción en destino, el stock se transfiere automáticamente de «en tránsito» a «físico en sitio». (d) Si el nodo destino está offline al recibir el envío, el operario registra la recepción localmente y el sistema sincroniza al reconectarse. (e) Cada transferencia genera la transacción de movimiento inter-bodegas en el ERP; si el ERP no está disponible, la transacción se encola para reintento automático. (f) El stock en tránsito se muestra como disponibilidad futura, diferenciado del stock físico presente en el sitio. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 · CP-RF-02.06-01 a -02 |
| RF-02.07 | Cumple | Sistema y aceptación de usuario — (a) Al consultar la ocupación de un CD, el sistema muestra el porcentaje de ocupación total y por zona (b) El reporte incluye un histórico diario de al menos 12 meses para visualizar tendencias. (c) El reporte es exportable a formato de hoja de cálculo. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-02.07-01 a -03 |
| RF-02.08 | Cumple | Sistema y aceptación de usuario — (a) El preparador recibe en su dispositivo la lista de líneas a recolectar, ordenadas por secuencia de recorrido óptima. (b) La confirmación de cada línea no supera 1 segundo de respuesta en el dispositivo. (c) Al registrar un faltante, el sistema exige la selección de una causa antes de continuar. (d) Al finalizar la preparación, el sistema actualiza el stock automáticamente y envía los faltantes al área comercial para gestión con el cliente. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-02.08-01 a -03 |
| RF-02.09 | Cumple | Sistema y aceptación de usuario — (a) Al generar las tareas de picking, el sistema prioriza las ubicaciones con menor vida útil remanente para cada SKU. (b) Si un producto en stock tiene una vida útil remanente inferior al umbral configurado (ej. 30 días), el sistema genera una alerta al jefe de bodega con la acción recomendada (descuento, devolución al proveedor, destrucción). (c) El sistema genera un reporte semanal de productos próximos a vencer por zona y por SKU. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-02.09-01 a -03 |
| RF-02.10 | Cumple | Sistema y aceptación de usuario — (a) El sistema provee un buscador de lotes por SKU, fecha o proveedor, devolviendo una lista con el estado (activo, agotado, en cuarentena). (b) Al seleccionar un lote, se despliega su ficha detallando: SKU, fecha vencimiento y cantidad física remanente por ubicación (pasillo/posición). (c) Se detalla el origen: fecha de recepción, proveedor, cantidad recibida inicial y documento. (d) Se detalla la salida de unidades: guías de despacho, cliente, fecha y cantidad entregada. (e) Se detallan excepciones: mermas, devoluciones o ajustes asociados. (f) Todo el detalle es exportable a hoja de cálculo para retiro sanitario inmediato. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-02.10-01 a -03 |
| RF-02.11 | Cumple | Sistema y aceptación de usuario — Por cada plataforma y día se obtiene el tiempo real entre consolidación, llegada, desconsolidación y despacho, y el detalle de excepciones, para medir la brecha de 16 horas (LafroX, 2026a, Anexo 2.2, SP-02). | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-02.11-01 a -03 |
| RF-03.01 | Cumple | Sistema y aceptación de usuario — El preventista ve la disponibilidad vigente antes de ofrecer un producto. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 · CP-RF-03.01-01 a -05 |
| RF-03.02 | Cumple | Sistema y aceptación de usuario — El preventista ve el dato cacheado y su antigüedad. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 · CP-RF-03.02-01 a -05 |
| RF-03.03 | Cumple | Sistema y aceptación de usuario — Si dos preventistas comprometen el mismo producto, el segundo en confirmar queda con quiebre parcial registrado. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-03.03-01 a -03 |
| RF-03.04 | Cumple | Sistema y aceptación de usuario — El preventista ve crédito y deuda antes de finalizar el pedido. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 · CP-RF-03.04-01 a -05 |
| RF-03.05 | Cumple | Sistema y aceptación de usuario — El preventista ve el dato cacheado y su antigüedad. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 · CP-RF-03.05-01 a -05 |
| RF-03.06 | Cumple | Sistema y aceptación de usuario — El preventista consulta el historial e identifica productos habituales o quiebres. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-03.06-01 a -03 |
| RF-03.07 | Cumple | Sistema y aceptación de usuario — El preventista aplica la promoción y el sistema calcula el descuento. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-03.07-01 a -03 |
| RF-03.08 | Cumple | Sistema y aceptación de usuario — El preventista es alertado antes de enviar el pedido. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 · CP-RF-03.08-01 a -05 |
| RF-03.09 | Cumple | Sistema y aceptación de usuario — El pedido no puede enviarse mientras el bloqueo esté activo. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 · CP-RF-03.09-01 a -05 |
| RF-03.10 | Cumple | Sistema y aceptación de usuario — Queda registrado supervisor, fecha y hora, y el pedido puede enviarse. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-03.10-01 a -03 |
| RF-03.11 | Cumple | Sistema y aceptación de usuario — El pedido conserva el precio acordado y lo transmite al ERP para la facturación. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 · CP-RF-03.11-01 a -02 |
| RF-03.12 | Cumple | Sistema y aceptación de usuario — La diferencia queda alertada al responsable comercial y se corrige antes de facturar, conservando el precio acordado. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 · CP-RF-03.12-01 a -02 |
| RF-03.13 | Cumple | Sistema y aceptación de usuario — El preventista visualiza la ventana disponible antes de confirmar; la promesa queda registrada. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 · CP-RF-03.13-01 a -05 |
| RF-03.14 | Cumple | Sistema y aceptación de usuario — Al seleccionar un cliente, se muestran sugerencias según criterios configurados por comercial. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-03.14-01 a -03 |
| RF-03.15 | Cumple | Sistema y aceptación de usuario — Cada pedido creado sin conectividad tiene un identificador único generado localmente. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 · CP-RF-03.15-01 a -05 |
| RF-03.16 | Cumple | Sistema y aceptación de usuario — Ningún pedido se pierde ni se duplica al sincronizar; todo reintento queda auditado. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 · CP-RF-03.16-01 a -05 |
| RF-04.01 | Cumple | Sistema y aceptación de usuario — Se despliega una ruta propuesta con la carga asignada a los vehículos de la flota. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-04.01-01 a -03 |
| RF-04.02 | Cumple | Sistema y aceptación de usuario — La tabla de ruteo y el ETA se recalculan inmediatamente tras realizar alguna reasignación | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 · CP-RF-04.02-01 a -02 |
| RF-04.03 | Cumple | Sistema y aceptación de usuario — Se despliega un error bloqueante impidiendo el cierre del camión hasta reubicar el excedente. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-04.03-01 a -03 |
| RF-04.04 | Cumple | Sistema y aceptación de usuario — El planificador secuencia todas las entregas en ventanas donde el cliente está disponible | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-04.04-01 a -03 |
| RF-04.05 | Cumple | Sistema y aceptación de usuario — Se impide la adición de cadena de frío a un camión seco. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-04.05-01 a -03 |
| RF-04.06 | Cumple | Sistema y aceptación de usuario — El cliente recibe de forma exitosa el mensaje antes de la partida del camión. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 · CP-RF-04.06-01 a -02 |
| RF-04.07 | Cumple | Sistema y aceptación de usuario — Ningún horario estimado de llegada es asignado en un horario fuera de la ventana horaria establecida por el cliente. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-04.07-01 a -03 |
| RF-04.08 | Cumple | Sistema y aceptación de usuario — El sistema calcula el costo de cada entrega basado en kilómetros, tiempo de descarga, tamaño del pedido y reentregas. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 · CP-RF-04.08-01 a -03 |
| RF-05.01 | Cumple | Sistema y aceptación de usuario — (a) Al generar misiones, la interfaz lista los ítems agrupados por pasillo lógico en secuencia de proximidad. (b) El sistema exige y permite confirmar cada línea digitalmente, exhibiendo: cantidad solicitada, SKU, lote asignado (FEFO) y coordenada exacta de ubicación. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-05.01-01 a -03 |
| RF-05.02 | Cumple | Sistema y aceptación de usuario — Si el código de barras escaneado difiere del SKU o Lote instruido, el sistema bloquea la confirmación. Como mecanismo de contingencia, el sistema debe permitir el ingreso manual del código numérico, pero debe registrar obligatoriamente el evento en la bitácora como 'Ingreso Manual' para futura auditoría de calidad. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-05.02-01 a -03 |
| RF-05.03 | Cumple | Sistema y aceptación de usuario — Si la cantidad recolectada es inferior a la solicitada, el sistema despliega el campo obligatorio 'Causa de Faltante' con lista predefinida y deshabilita la acción 'Confirmar Línea' hasta su selección. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-05.03-01 a -03 |
| RF-05.04 | Cumple | Sistema y aceptación de usuario — Ante un pedido mixto, el sistema exige recolectar el 100% de los SKUs de ambiente seco antes de liberar las ubicaciones correspondientes a las cámaras de frío en la interfaz del operario. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-05.04-01 a -03 |
| RF-05.05 | Cumple | Sistema y aceptación de usuario — (a) La misión dirige al operario a la coordenada del lote con fecha de vencimiento más próxima. (b) Al escanear un lote más nuevo cuando hay inventario del lote FEFO disponible, el sistema bloquea la confirmación con mensaje «Lote (código de lote) con vencimiento anterior disponible en [ubicación]». (c) Si el lote FEFO no está disponible (ej. dañado), el preparador puede seleccionar el siguiente lote registrando el motivo (lista estructurada: no encontrado, dañado, cantidad insuficiente). (d) La excepción FEFO queda registrada en bitácora de auditoría | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-05.05-01 a -03 |
| RF-05.06 | Cumple | Sistema y aceptación de usuario — Al ejecutar 'Cerrar Misión', el sistema transmite al ERP el objeto completo de la recolección asociado al ID del pedido. El ERP procesa este conjunto de datos ajustando las cantidades finales y registrando los lotes exactos para la emisión de la Guía de Despacho, sin permitir digitación manual. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-05.06-01 a -03 |
| RF-05.07 | Cumple | Sistema y aceptación de usuario — (a) El dispositivo del cargador indica el siguiente bulto/pallet a subir, mostrando: SSCC, cliente destino y posición en la secuencia. (b) El cargador confirma cada bulto escaneando el SSCC; si escanea un bulto fuera de secuencia, el sistema alerta y solicita confirmación del motivo. (c) Al completar la carga, el sistema verifica que todos los bultos asignados al camión han sido escaneados. (d) Si falta algún bulto, el sistema bloquea la confirmación de carga completa y genera una alerta al jefe de bodega. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-05.07-01 a -03 |
| RF-06.01 | Cumple | Sistema y aceptación de usuario — Los elementos marcados como entregados quedan registrados de forma exitosa en la guía. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-06.01-01 a -03 |
| RF-06.02 | Cumple | Sistema y aceptación de usuario — La firma queda correctamente registrada en la guía de despacho. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 · CP-RF-06.02-01 a -05 |
| RF-06.03 | Cumple | Sistema y aceptación de usuario — Los productos rechazados quedan registrados de forma correcta en la solicitud de rechazo. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 · CP-RF-06.03-01 a -02 |
| RF-06.04 | Cumple | Sistema y aceptación de usuario — El envío se registra como fallido y se agenda para ser entregado en la ventana horaria siguiente mas cercana del cliente. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 · CP-RF-06.04-01 a -02 |
| RF-06.05 | Cumple | Sistema y aceptación de usuario — El monto recibido en efectivo por el conductor queda registrado en el sistema. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 · CP-RF-06.05-01 a -05 |
| RF-06.06 | Cumple | Sistema y aceptación de usuario — Cada entrega tiene hora real de llegada y término, que alimenta el cálculo de OTIF (RF-11.03). | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-06.06-01 a -03 |
| RF-06.07 | Cumple | Sistema y aceptación de usuario — Al llegar al CD o recuperar señal, la app sube la data y el sistema genera automáticamente el reporte de rendición. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 · CP-RF-06.07-01 a -05 |
| RF-06.08 | Cumple | Sistema y aceptación de usuario — Un conductor nuevo de una empresa externa se autentica en 2 minutos con un código que le da su jefe de flota, y puede iniciar su ruta. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-06.08-01 a -03 |
| RF-06.09 | Cumple | Sistema y aceptación de usuario — El conductor registra que el cliente devolvió 5 canastillos; el sistema descuenta del saldo del cliente y actualiza el inventario de envases. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-06.09-01 a -03 |
| RF-06.10 | Cumple | Sistema y aceptación de usuario — El saldo del cliente indica que se devolvieron 5 canastillos y el sistema lo actualiza en el inventario de envases | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-06.10-01 a -03 |
| RF-06.11 | Cumple | Sistema y aceptación de usuario — Se resuelve alternativamente la Decisión #15; los clientes con smartphone pueden validar su recepción de forma autónoma. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 · CP-RF-06.11-01 a -02 |
| RF-06.12 | Cumple | Sistema y aceptación de usuario — Los clientes sin conectividad y sin smartphone pueden validar su recepción de forma autónoma. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 · CP-RF-06.12-01 a -02 |
| RF-06.13 | Cumple | Sistema y aceptación de usuario — El cliente del canal tradicional recibe un comprobante físico pequeño, igual que hoy con la guía, pero generado digitalmente. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 · CP-RF-06.13-01 a -02 |
| RF-06.14 | Cumple | Sistema y aceptación de usuario — Cada guía queda con su estado de acuse (recibido conforme, con observaciones o sin acuse) visible el mismo día; las guías sin acuse generan una alerta para gestión. La solución no emite documentos tributarios. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-06.14-01 a -03 |
| RF-07.01 | Cumple | Sistema y aceptación de usuario — La planilla de rendición (RF-07.02) contrasta lo declarado con el monto esperado y muestra la diferencia a justificar (RF-07.03). | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-07.01-01 a -03 |
| RF-07.02 | Cumple | Sistema y aceptación de usuario — Despliegue automático de la cuadratura en caja mostrando monto esperado vs recaudado y la diferencia resultante a justificar. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-07.02-01 a -03 |
| RF-07.03 | Cumple | Sistema y aceptación de usuario — Cero pesos de descuadre sin motivo formal tipificado, firma digital y asignación de responsabilidad en bitácora. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-07.03-01 a -03 |
| RF-07.04 | Cumple | Sistema y aceptación de usuario — Listado diario de morosidad al día con registro auditable de promesas de pago y tareas automáticas de seguimiento. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-07.04-01 a -03 |
| RF-07.05 | Cumple | Sistema y aceptación de usuario — Alerta en terminal de preventa en menos de 2 s al seleccionar al cliente, impidiendo el ingreso de órdenes a crédito no autorizadas. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-07.05-01 a -03 |
| RF-07.06 | Cumple | Sistema y aceptación de usuario — Captura automática del código de autorización POS y conciliación contra la entrega en la rendición diaria de caja sin digitación manual. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-07.06-01 a -03 |
| RF-07.07 | Cumple | Sistema y aceptación de usuario — Acceso seguro del cliente autenticado a su saldo vivo y detalle de facturas pendientes con opción de descarga de cartola. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 · CP-RF-07.07-01 a -03 |
| RF-07.08 | Cumple | Sistema y aceptación de usuario — Pago web queda en estado «En Revisión» hasta que el cajero lo aprueba, momento en que se envía la rebaja contable al ERP. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 · CP-RF-07.08-01 a -03 |
| RF-07.09 | Cumple | Sistema y aceptación de usuario — Abonos y cancelaciones contables reflejados en el ERP el mismo día sin intervención manual de digitación (Restricción R4). | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-07.09-01 a -03 |
| RF-07.10 | Cumple | Sistema y aceptación de usuario — Registro de abono parcial en app móvil, comprobante digital emitido al cliente y saldo pendiente registrado en cuenta corriente. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-07.10-01 a -03 |
| RF-07.11 | Cumple | Sistema y aceptación de usuario — Emisión de recibo digital de cobro en preventa y consolidación automática en la bolsa de dinero a rendir por el vendedor al volver a base. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-07.11-01 a -03 |
| RF-08.01 | Cumple | Sistema y aceptación de usuario — La devolución queda registrada en el dispositivo al momento de la entrega, sin papeleo, y se sincroniza con el sistema central al reconectarse. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 · CP-RF-08.01-01 a -05 |
| RF-08.02 | Cumple | Sistema y aceptación de usuario — El destino queda registrado y la transacción llega al ERP; toda decisión queda trazada con usuario, fecha y destino asignado. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 · CP-RF-08.02-01 a -05 |
| RF-08.03 | Cumple | Sistema y aceptación de usuario — El saldo de envases por cliente queda actualizado tras cada movimiento y es consultable desde el dispositivo del conductor antes de cada entrega. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-08.03-01 a -03 |
| RF-08.04 | Cumple | Sistema y aceptación de usuario — El preventista recibe la notificación en ≤ 24 horas de superado el umbral. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-08.04-01 a -03 |
| RF-08.05 | Cumple | Sistema y aceptación de usuario — La merma queda registrada por SKU y lote, con su origen (conteo, preparación o góndola), y descuenta el stock disponible. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-08.05-01 a -03 |
| RF-08.06 | Cumple | Sistema y aceptación de usuario — El reporte identifica los clientes y zonas con mayor pérdida de envases, permitiendo priorizar acciones de recuperación. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-08.06-01 a -03 |
| RF-08.07 | Cumple | Sistema y aceptación de usuario — El costo de servir de un cliente con alta tasa de devolución refleja ese costo adicional. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 · CP-RF-08.07-01 a -03 |
| RF-09.01 | Cumple | Sistema y aceptación de usuario — En un simulacro de retiro sanitario, se obtiene en menos de 2 horas la lista de clientes afectados, con trazabilidad desde el proveedor hasta los clientes y archivo exportable (RNF-09.01). | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 · CP-RF-09.01-01 a -05 |
| RF-09.02 | Cumple | Sistema y aceptación de usuario — El equipo de calidad puede rastrear el origen de cualquier unidad devuelta, realizando la trazabilidad desde los clientes afectados hasta los productores | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 · CP-RF-09.02-01 a -05 |
| RF-09.03 | Cumple | Sistema y aceptación de usuario — El sistema registrara las temperaturas. Los registros son auditable y se puede exportar para la autoridad sanitaria. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 · CP-RF-09.03-01 a -05 |
| RF-09.04 | Cumple | Sistema y aceptación de usuario — El sistema registrara las temperaturas de los camiones. El cliente o Puelche pueden consultar el registro histórico de temperatura de su envío. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 · CP-RF-09.04-01 a -05 |
| RF-09.05 | Cumple | Sistema y aceptación de usuario — El sistema al registrar una temperatura fuera del rango aceptable, generara una alerta tanto al conductor como al equipo de calidad | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 · CP-RF-09.05-01 a -05 |
| RF-09.06 | Cumple | Sistema y aceptación de usuario — El lote queda retenido automáticamente ante excursión crítica; el conductor ve la alerta y registra observaciones; solo Calidad libera, bloquea o rechaza, y su decisión queda registrada. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 · CP-RF-09.06-01 a -02 |
| RF-09.07 | Cumple | Sistema y aceptación de usuario — Si se rechaza el pedido, el conductor registra el rechazo ingresando evidencia | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 · CP-RF-09.07-01 a -05 |
| RF-09.08 | Cumple | Sistema y aceptación de usuario — El picking digital registra qué lote concreto sale en cada canastillo/pallet hacia el cliente. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 · CP-RF-09.08-01 a -05 |
| RF-09.09 | Cumple | Sistema y aceptación de usuario — La evidencia de cadena de frío de un envío se obtiene sin reconstrucción manual. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 · CP-RF-09.09-01 a -05 |
| RF-09.10 | Cumple | Sistema y aceptación de usuario — La alerta y la retención de RF-09.05 y RF-09.06 aplican el parámetro vigente, y cada cambio queda registrado. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 · CP-RF-09.10-01 a -02 |
| RF-10.01 | Cumple | Sistema y aceptación de usuario — La sugerencia reemplaza la planilla de reposición y queda disponible para revisión (D-05). | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 · CP-RF-10.01-01 a -02 |
| RF-10.02 | Cumple | Sistema y aceptación de usuario — La sugerencia incluye las promociones sin agregarlas a mano. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 · CP-RF-10.02-01 a -02 |
| RF-10.03 | Cumple | Sistema y aceptación de usuario — El ERP recibe la sugerencia aprobada y conserva la emisión de la orden de compra. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 · CP-RF-10.03-01 a -02 |
| RF-11.01 | Cumple | Sistema y aceptación de usuario — Reportes emitidos automáticamente a las casillas de los gerentes el día 2 de cada mes y cada lunes a las 06:00 AM sin intervención manual. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 · CP-RF-11.01-01 a -02 |
| RF-11.02 | Cumple | Sistema y aceptación de usuario — Ficha de rentabilidad por cliente actualizada tras cada liquidación, desglosando costos logísticos directos e indirectos y margen neto resultante. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 · CP-RF-11.02-01 a -02 |
| RF-11.03 | Cumple | Sistema y aceptación de usuario — Todas las gerencias visualizan el mismo valor de OTIF diario; ante entregas parciales o tardías se audita el motivo en el sistema. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-11.03-01 a -03 |
| RF-11.04 | Cumple | Sistema y aceptación de usuario — Indicador mensual de Perfect Order desglosado por causa raíz (daño, faltante, atraso, documento) contrastado contra la orden de venta original. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-11.04-01 a -03 |
| RF-11.05 | Cumple | Sistema y aceptación de usuario — Generación de bitácora de viajes subutilizados en la ventana de 05:30 a 07:00 para auditoría y balanceo de carga de transporte. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-11.05-01 a -03 |
| RF-11.06 | Cumple | Sistema y aceptación de usuario — Despliegue en vivo en pantallas gerenciales con actualización continua de la distribución y alertas críticas de ruta. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-11.06-01 a -03 |
| RF-11.07 | Cumple | Sistema y aceptación de usuario — Planilla de cuadratura emitida inmediatamente al arribo del camión para tesorería y bodega, sin rezagos para el día siguiente. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-11.07-01 a -03 |
| RF-11.08 | Cumple | Sistema y aceptación de usuario — Clasificación automática de clientes en rentables, no rentables y estratégicos, con simulación de impacto de cambio de frecuencias. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 · CP-RF-11.08-01 a -02 |
| RF-12.01 | Cumple | Sistema y aceptación de usuario — El mensaje recibido queda disponible para su validación (RF-12.02) en un plazo no superior a 15 segundos, identificando la cadena de origen. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 · CP-RF-12.01-01 a -03 |
| RF-12.02 | Cumple | Sistema y aceptación de usuario — El pedido queda marcado como válido o inválido, con el detalle de cada validación fallida. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 · CP-RF-12.02-01 a -03 |
| RF-12.03 | Cumple | Sistema y aceptación de usuario — Cada línea queda asociada a un SKU válido del maestro interno, o marcada como discrepancia no resuelta. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 · CP-RF-12.03-01 a -03 |
| RF-12.04 | Cumple | Sistema y aceptación de usuario — El pedido aparece como pedido único en el sistema de gestión dentro de 2 minutos desde su validación. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 · CP-RF-12.04-01 a -03 |
| RF-12.05 | Cumple | Sistema y aceptación de usuario — El pedido aparece en el listado de pedidos confirmados del módulo de planificación, sin digitación manual. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 · CP-RF-12.05-01 a -03 |
| RF-12.06 | Cumple | Sistema y aceptación de usuario — Los pedidos con error aparecen en la bandeja con causa, estado, fecha y responsable. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 · CP-RF-12.06-01 a -03 |
| RF-12.07 | Cumple | Sistema y aceptación de usuario — La cadena recibe automáticamente el mensaje correspondiente. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 · CP-RF-12.07-01 a -03 |
| RF-12.08 | Cumple | Sistema y aceptación de usuario — Se puede consultar el estado actual y el historial de eventos con fecha, hora y responsable/sistema | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 · CP-RF-12.08-01 a -03 |
| RF-12.09 | Cumple | Sistema y aceptación de usuario — El cliente recibe el ASN dentro de los 2 minutos posteriores a la carga. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 · CP-RF-12.09-01 a -03 |
| RF-12.10 | Cumple | Sistema y aceptación de usuario — El camión llega dentro de la ventana comprometida en el 80 % de los casos. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 · CP-RF-12.10-01 a -03 |
| RF-12.11 | Cumple | Sistema y aceptación de usuario — Toda desviación queda registrada con hora real de llegada. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 · CP-RF-12.11-01 a -03 |
| RF-12.12 | Cumple | Sistema y aceptación de usuario — Queda un único registro de evidencia por entrega, con el mecanismo utilizado identificado. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 · CP-RF-12.12-01 a -03 |
| RF-12.13 | Cumple | Sistema y aceptación de usuario — El cliente recibe el comprobante dentro de los 30 minutos posteriores a la descarga. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 · CP-RF-12.13-01 a -03 |
| RF-12.14 | Cumple | Sistema y aceptación de usuario — Cualquier visitante ve el catálogo sin poder generar pedidos ni ver precios. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 · CP-RF-12.14-01 a -02 |
| RF-12.15 | Cumple | Sistema y aceptación de usuario — El cliente genera un pedido válido sin intervención de un preventista. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 · CP-RF-12.15-01 a -02 |
| RF-12.16 | Cumple | Sistema y aceptación de usuario — El cliente visualiza el estado y compromiso de cada pedido. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 · CP-RF-12.16-01 a -02 |
| RF-12.17 | Cumple | Sistema y aceptación de usuario — El cliente descarga los documentos correspondientes a sus operaciones. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 · CP-RF-12.17-01 a -02 |
| RF-12.18 | Cumple | Sistema y aceptación de usuario — El cliente consulta su saldo según la información del sistema de gestión. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 · CP-RF-12.18-01 a -02 |
| RF-12.19 | Cumple | Sistema y aceptación de usuario — La empresa visualiza el día anterior las rutas asignadas. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 · CP-RF-12.19-01 a -02 |
| RF-12.20 | Cumple | Sistema y aceptación de usuario — La empresa descarga la documentación correspondiente. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 · CP-RF-12.20-01 a -02 |
| RF-12.21 | Cumple | Sistema y aceptación de usuario — Queda registrado el conductor/vehículo real; si no se confirma, el sistema mantiene la asignación planificada como supuesto no verificado. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 · CP-RF-12.21-01 a -02 |
| RF-12.22 | Cumple | Sistema y aceptación de usuario — El proveedor consulta el estado actualizado de sus órdenes. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 · CP-RF-12.22-01 a -02 |
| RF-12.23 | Cumple | Sistema y aceptación de usuario — El proveedor consulta las recepciones actualizadas. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 · CP-RF-12.23-01 a -02 |
| RF-12.24 | Cumple | Sistema y aceptación de usuario — El proveedor consulta las devoluciones/notas de crédito actualizadas. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 · CP-RF-12.24-01 a -02 |
| RF-12.25 | Cumple | Sistema y aceptación de usuario — El cliente queda registrado y recibe un correo de confirmación de cuenta. Si el RUT no está habilitado, el sistema informa que debe contactar a su ejecutivo comercial. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 · CP-RF-12.25-01 a -02 |
| RF-12.26 | Cumple | Sistema y aceptación de usuario — El cliente accede a su área privada. Tras tres intentos fallidos consecutivos, la cuenta queda bloqueada temporalmente. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 · CP-RF-12.26-01 a -02 |
| RF-12.27 | Cumple | Sistema y aceptación de usuario — El cliente recibe un enlace válido por tiempo limitado que le permite establecer una nueva contraseña. El enlace expira tras su uso o transcurridos 15 minutos. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 · CP-RF-12.27-01 a -02 |
| RF-12.28 | Cumple | Sistema y aceptación de usuario — La sesión queda invalidada y el cliente es redirigido a la pantalla de inicio de sesión. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 · CP-RF-12.28-01 a -02 |
| RF-12.29 | Cumple | Sistema y aceptación de usuario — La sesión expira y el cliente debe iniciar sesión nuevamente para acceder a su área privada. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 · CP-RF-12.29-01 a -02 |
| RF-12.30 | Cumple | Sistema y aceptación de usuario — El pago es procesado por Transbank y el portal registra la confirmación o rechazo de la transacción. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 · CP-RF-12.30-01 a -02 |
| RF-13.01 | Cumple | Sistema y aceptación de usuario — El diagrama de arquitectura identifica cada capa, sus componentes y las interfaces entre ellas, siguiendo ISO/IEC/IEEE 42010. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-13.01-01 a -03 |
| RF-13.02 | Cumple | Sistema y aceptación de usuario — La tabla de emplazamiento cubre el 100% de los componentes de la solución, con justificación documentada para cada uno. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-13.02-01 a -03 |
| RF-13.03 | Cumple | Sistema y aceptación de usuario — El registro ADR es entregable contractual y se actualiza con cada decisión arquitectónica relevante. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-13.03-01 a -03 |
| RF-13.04 | Cumple | Sistema y aceptación de usuario — El modelo de dominio es entregado como parte de la oferta técnica, con notación UML. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-13.04-01 a -03 |
| RF-14.01 | Cumple | Sistema y aceptación de usuario — El sistema muestra en el mapa la ubicación de los 42 camiones propios, igual que hoy, pero integrado en la nueva solución. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 · CP-RF-14.01-01 a -05 |
| RF-14.02 | Cumple | Sistema y aceptación de usuario — El gerente de operaciones ve que el camión 5 se desvía 5 km en su ruta; investiga si es por tráfico, error del conductor o una parada no registrada. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-14.02-01 a -03 |
| RF-14.03 | Cumple | Sistema y aceptación de usuario — El centro de control recibe una alerta si un camión se desvía para investigar si hay un problema (accidente, robo, etc.). | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-14.03-01 a -03 |
| RF-14.04 | Cumple | Sistema y aceptación de usuario — El costo de servir por cliente incluye el costo real de los kilómetros recorridos para llegar a su local. | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 5 · CP-RF-14.04-01 a -05 |
| RF-14.05 | Cumple | Sistema y aceptación de usuario — Se resuelve la Decisión #5; el sistema exige que el conductor se identifique (PIN o QR) antes de iniciar la ruta, incluso si es externo. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 · CP-RF-14.05-01 a -03 |
| RF-14.06 | Cumple | Sistema y aceptación de usuario — El sistema registra automáticamente la hora de llegada del camión al área del cliente, para validar el cumplimiento de la ventana horaria. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 · CP-RF-14.06-01 a -02 |
| RF-14.01-BTT | Cumple | Sistema y aceptación de usuario — El sistema debe permitir clasificar la información del CLIENTE por nivel de sensibilidad (pública, interna, confidencial, restringida), con controles diferenciados por nivel documentados en una matriz. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-14.01-BTT-01 a -03 |
| RF-14.02-BTT | Cumple | Sistema y aceptación de usuario — El PROPONENTE debe mantener una matriz de controles de seguridad trazable a ISO/IEC 27001 e ISO/IEC 27002, indicando el control, su implementación concreta en la solución y la evidencia que lo acredita. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-14.02-BTT-01 a -03 |
| RF-14.03-BTT | Cumple | Sistema y aceptación de usuario — El PROPONENTE debe declarar la superficie de exposición completa de la solución: cada nombre de dominio, puerto y servicio alcanzable desde fuera de la red del CLIENTE. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-14.03-BTT-01 a -03 |
| RF-14.04-BTT | Cumple | Sistema y aceptación de usuario — El PROPONENTE debe disponer de un plan de respuesta a incidentes de seguridad que defina clasificación, cadena de escalamiento, plazos, responsables y protocolo de comunicación al CLIENTE dentro de las 2 horas de detectado un incidente de severidad crítica. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-14.04-BTT-01 a -03 |
| RF-14.05-BTT | Cumple | Sistema y aceptación de usuario — El sistema (o el equipo de seguridad del ADJUDICATARIO) debe notificar al CLIENTE cualquier brecha de seguridad o de datos personales dentro de las 24 horas de su detección, con informe preliminar, y entregar el análisis de causa raíz dentro de los 5 días hábiles siguientes. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-14.05-BTT-01 a -03 |
| RF-15.01 | Cumple | Sistema y aceptación de usuario — La identidad de todas las personas usuarias internas es gestionada desde un único punto. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-15.01-01 a -03 |
| RF-15.02 | Cumple | Sistema y aceptación de usuario — El usuario se autentica una vez y accede a todos los módulos sin reautenticación. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-15.02-01 a -03 |
| RF-15.03 | Cumple | Sistema y aceptación de usuario — El acceso a perfiles administradores o desde fuera de la red requiere segundo factor. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-15.03-01 a -03 |
| RF-15.04 | Cumple | Sistema y aceptación de usuario — La matriz de roles y permisos es entregada y aprobada por el CLIENTE. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-15.04-01 a -03 |
| RF-15.05 | Cumple | Sistema y aceptación de usuario — Las cuentas son creadas/eliminadas automáticamente según el estado laboral del usuario. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-15.05-01 a -03 |
| RF-16.01 | Cumple | Sistema y aceptación de usuario — El equipo de operaciones del CLIENTE puede consultar métricas, logs y trazas desde una única interfaz. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-16.01-01 a -03 |
| RF-16.02 | Cumple | Sistema y aceptación de usuario — El CLIENTE visualiza los tableros en tiempo real y exporta datos. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-16.02-01 a -03 |
| RF-16.03 | Cumple | Sistema y aceptación de usuario — Las alertas se generan por síntomas de negocio (ej. OTIF bajo, pedidos no preparados), no solo por CPU alta. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-16.03-01 a -03 |
| RF-16.04 | Cumple | Sistema y aceptación de usuario — El informe de causa raíz es entregado al CLIENTE dentro de los 5 días hábiles. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-16.04-01 a -03 |
| RF-17.01 | Cumple | Sistema y aceptación de usuario — El administrador del CLIENTE crea, modifica o elimina usuarios/roles desde la interfaz sin desarrollo. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-17.01-01 a -03 |
| RF-17.02 | Cumple | Sistema y aceptación de usuario — El administrador del CLIENTE modifica parámetros de negocio sin desarrollo, con auditoría de cambios. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-17.02-01 a -03 |
| RF-17.03 | Cumple | Sistema y aceptación de usuario — El cambio se aplica solo después de la aprobación de un segundo perfil autorizado. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-17.03-01 a -03 |
| RF-17.04 | Cumple | Sistema y aceptación de usuario — La auditoría es consultable desde la interfaz y no puede ser alterada ni eliminada. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-17.04-01 a -03 |
| RF-17.05 | Cumple | Sistema y aceptación de usuario — El auditor consulta y exporta la auditoría con los filtros deseados. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-17.05-01 a -03 |
| RF-17.06 | Cumple | Sistema y aceptación de usuario — El administrador del CLIENTE configura flujos de trabajo (ej. aprobación de pedidos, gestión de devoluciones) sin desarrollo. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-17.06-01 a -03 |
| RF-17.07 | Cumple | Sistema y aceptación de usuario — El usuario visualiza y gestiona todas sus tareas desde una única bandeja. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-17.07-01 a -03 |
| RF-17.08 | Cumple | Sistema y aceptación de usuario — Los documentos son almacenados, versionados y accesibles según permisos del usuario. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-17.08-01 a -03 |
| RF-17.09 | Cumple | Sistema y aceptación de usuario — El usuario genera el documento con los datos de la transacción. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 2 · CP-RF-17.09-01 a -02 |
| RF-17.10 | Cumple | Sistema y aceptación de usuario — El usuario recibe la notificación por el canal configurado. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-17.10-01 a -03 |
| RF-17.11 | Cumple | Sistema y aceptación de usuario — El usuario encuentra información relevante mediante una búsqueda que no sobrepase más de 2 segundos en la respuesta y ademas de poder estar filtrada. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-17.11-01 a -03 |
| RF-17.12 | Cumple | Sistema y aceptación de usuario — El usuario ordena, filtra y exporta los datos del listado. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-17.12-01 a -03 |
| RF-17.13 | Cumple | Sistema y aceptación de usuario — Cualquier visitante accede al portal público y visualiza la información. En E1 se publican la información institucional y el contacto; en E2 se agrega el catálogo de RF-12.14, que concreta este requisito para el caso. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 2 · CP-RF-17.13-01 a -02 |
| RF-18.01 | Cumple | Sistema y aceptación de usuario — El documento queda firmado mediante la modalidad aplicable y se conserva su evidencia para la verificación posterior. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-18.01-01 a -03 |
| RF-18.02 | Cumple | Sistema y aceptación de usuario — El usuario recibe notificaciones por el canal y frecuencia configurados. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 2 · CP-RF-18.02-01 a -02 |
| RF-18.03 | Cumple | Sistema y aceptación de usuario — La notificación es enviada y registrada, si falla, se reintenta según política configurada. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 · CP-RF-18.03-01 a -03 |
| RF-19.01 | Cumple | Se verifica con RT-11.03 | — | — | — | 0 |
| RF-19.02 | Cumple | Se verifica con RT-11.05 | — | — | — | 0 |
| RF-19.03 | Cumple | Se verifica con RT-11.13 | — | — | — | 0 |
| RF-19.04 | Cumple | Se verifica con RT-11.18 | — | — | — | 0 |
| RF-19.05 | Cumple | Se verifica con RT-11.19 | — | — | — | 0 |
| RNF-01.01 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 | H5 | 3 · CP-RNF-01.01-01 a -03 |
| RNF-01.02 | Cumple | Restauración de muestra y política de retención | DR | 3.8.5 | H5 | 5 · CP-RNF-01.02-01 a -05 |
| RNF-01.03 | Cumple | Perfil operacional: sin señal y sin enlace | Terreno · PREPROD | 3.8.3 | H5 | 5 · CP-RNF-01.03-01 a -05 |
| RNF-02.01 | Cumple | Perfil operacional: sin señal y sin enlace | Terreno · PREPROD | 3.8.3 | H5 | 5 · CP-RNF-02.01-01 a -05 |
| RNF-03.01 | Cumple | Perfil operacional: sin señal y sin enlace | Terreno · PREPROD | 3.8.3 | H5 | 3 · CP-RNF-03.01-01 a -03 |
| RNF-03.02 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 | H5 | 3 · CP-RNF-03.02-01 a -03 |
| RNF-03.03 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 | H5 | 3 · CP-RNF-03.03-01 a -03 |
| RNF-04.01 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 | H7 | 2 · CP-RNF-04.01-01 a -02 |
| RNF-05.01 | Cumple | Perfil operacional: sin señal y sin enlace | Terreno · PREPROD | 3.8.3 | H5 | 3 · CP-RNF-05.01-01 a -03 |
| RNF-05.02 | Cumple | Usabilidad en terreno con usuarios | Terreno | 3.8.3 | H5 | 5 · CP-RNF-05.02-01 a -05 |
| RNF-05.03 | Cumple | Usabilidad en terreno con usuarios | Terreno | 3.8.3 | H5 | 5 · CP-RNF-05.03-01 a -05 |
| RNF-06.01 | Cumple | Perfil operacional: sin señal y sin enlace | Terreno · PREPROD | 3.8.3 | H5 | 2 · CP-RNF-06.01-01 a -02 |
| RNF-06.02 | Cumple | Se verifica con RT-03.11 | — | — | — | 0 |
| RNF-06.03 | Cumple | Se verifica con RNF-02.01 | — | — | — | 0 |
| RNF-07.01 | Cumple | Perfil operacional: sin señal y sin enlace | Terreno · PREPROD | 3.8.3 | H5 | 5 · CP-RNF-07.01-01 a -05 |
| RNF-07.02 | Cumple | Revisión de configuración, SAST/DAST y pentest | QA · PREPROD | 3.8.6 | H5 | 5 · CP-RNF-07.02-01 a -05 |
| RNF-08.01 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 | H5 | 3 · CP-RNF-08.01-01 a -03 |
| RNF-08.02 | Cumple | Restauración de muestra y política de retención | DR | 3.8.5 | H5 | 3 · CP-RNF-08.02-01 a -03 |
| RNF-09.01 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 | H5 | 5 · CP-RNF-09.01-01 a -05 |
| RNF-09.02 | Cumple | Restauración de muestra y política de retención | DR | 3.8.5 | H5 | 5 · CP-RNF-09.02-01 a -05 |
| RNF-09.03 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 | H7 | 3 · CP-RNF-09.03-01 a -03 |
| RNF-09.04 | Cumple | Perfil operacional: sin señal y sin enlace | Terreno · PREPROD | 3.8.3 | H5 | 5 · CP-RNF-09.04-01 a -05 |
| RNF-09.05 | Cumple | Perfil operacional: registro térmico | Terreno | 3.8.3 | H5 | 5 · CP-RNF-09.05-01 a -05 |
| RNF-11.01 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 | H5 | 3 · CP-RNF-11.01-01 a -03 |
| RNF-11.02 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 | H7 | 3 · CP-RNF-11.02-01 a -03 |
| RNF-11.03 | Cumple | Se verifica con RF-11.07 | — | — | — | 0 |
| RNF-11.04 | Cumple | Se verifica con RT-05.29 | — | — | — | 0 |
| RNF-12.01 | Cumple | Prueba funcional en marcha blanca | PROD | 4.3 | H12 | 5 |
| RNF-12.02 | Cumple | Prueba funcional en marcha blanca | PROD | 4.3 | H12 | 3 |
| RNF-12.03 | Cumple | Prueba funcional en marcha blanca | PROD | 4.3 | H12 | 3 |
| RNF-13.01 | Cumple | Perfil operacional: sin señal y sin enlace | Terreno · PREPROD | 3.8.3 · 3.9.2 | H5 · H10 | 5 |
| RNF-13.02 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 5 |
| RNF-13.03 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-13.04 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-13.05 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-13.06 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-13.07 | Cumple | Recuperación ante desastres con conmutación real | DR | 3.8.5 · 3.9.4 | H5 · H10 | 3 |
| RNF-13.08 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-13.09 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-14.01 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 5 |
| RNF-14.02 | Cumple | Revisión de configuración, SAST/DAST y pentest | QA · PREPROD | 3.8.6 · 3.9.5 | H5 · H10 | 5 |
| RNF-14.03 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-14.04 | Cumple | Revisión de configuración, SAST/DAST y pentest | QA · PREPROD | 3.8.6 · 3.9.5 | H5 · H10 | 3 |
| RNF-14.05 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 3 |
| RNF-14.06 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-14.07 | Cumple | SAST en G2 y DAST en G4 | QA | 1.5.2 · 3.8.6 | H4 · H5 | 3 |
| RNF-14.08 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-14.09 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-14.10 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-14.11 | Cumple | Revisión de configuración, SAST/DAST y pentest | QA · PREPROD | 3.8.6 | H5 | 5 |
| RNF-14.12 | Cumple | Revisión de configuración, SAST/DAST y pentest | QA · PREPROD | 3.8.6 | H5 | 3 |
| RNF-15.01 | Cumple | Revisión de configuración, SAST/DAST y pentest | QA · PREPROD | 3.8.6 · 3.9.5 | H5 · H10 | 5 |
| RNF-15.02 | Cumple | Revisión de configuración, SAST/DAST y pentest | QA · PREPROD | 3.8.6 · 3.9.5 | H5 · H10 | 5 |
| RNF-15.03 | Cumple | Restauración de muestra y política de retención | DR | 3.8.5 · 3.9.4 | H5 · H10 | 3 |
| RNF-16.01 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 3 |
| RNF-16.02 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-16.03 | Cumple | Revisión de configuración, SAST/DAST y pentest | QA · PREPROD | 3.8.6 · 3.9.5 | H5 · H10 | 5 |
| RNF-17.01 | Cumple | Restauración de muestra y política de retención | DR | 3.8.5 · 3.9.4 | H5 · H10 | 3 |
| RNF-17.02 | Cumple | Revisión de configuración, SAST/DAST y pentest | QA · PREPROD | 3.8.6 · 3.9.5 | H5 · H10 | 3 |
| RNF-17.03 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-19.01 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-19.02 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-19.03 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-19.04 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 3 |
| RNF-20.01 | Cumple | Recuperación ante desastres con conmutación real | DR | 3.8.5 · 3.9.4 | H5 · H10 | 5 |
| RNF-20.02 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 5 |
| RNF-20.03 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 5 |
| RNF-20.04 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 3 |
| RNF-20.05 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-20.06 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 5 |
| RNF-20.07 | Cumple | Recuperación ante desastres con conmutación real | DR | 3.8.5 · 3.9.4 | H5 · H10 | 5 |
| RNF-21.01 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 5 |
| RNF-21.02 | Cumple | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 3 |
| RNF-21.03 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 3 |
| RNF-21.04 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-21.05 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-21.06 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-21.07 | Cumple | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 3 |
| RNF-21.08 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-21.09 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-22.01 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-22.02 | Cumple | Recuperación ante desastres con conmutación real | DR | 3.8.5 · 3.9.4 | H5 · H10 | 3 |
| RNF-22.03 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-22.04 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-22.05 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-22.06 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-23.01 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-23.02 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-23.03 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-23.04 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RT-02.01 | Cumple | Revisión de arquitectura y prueba de integración | QA | 2.1 · 3.8.1 | H2 · H4 | 1 |
| RT-02.02 | Cumple | Revisión de arquitectura y prueba de integración | QA | 2.1 · 3.8.1 | H2 · H4 | 1 |
| RT-02.03 | Cumple | Revisión de arquitectura y prueba de integración | QA | 2.1 · 3.8.1 | H2 · H4 | 1 |
| RT-02.04 | Cumple | Revisión de arquitectura y prueba de integración | QA | 2.1 · 3.8.1 | H2 · H4 | 1 |
| RT-02.05 | Cumple | Revisión de arquitectura y prueba de integración | QA | 2.1 · 3.8.1 | H2 · H4 | 1 |
| RT-02.06 | Cumple | Revisión de arquitectura y prueba de integración | QA | 2.1 · 3.8.1 | H2 · H4 | 1 |
| RT-02.07 | Cumple | Revisión de arquitectura y prueba de integración | QA | 2.1 · 3.8.1 | H2 · H4 | 1 |
| RT-02.08 | Cumple | Revisión de arquitectura y prueba de integración | QA | 2.1 · 3.8.1 | H2 · H4 | 1 |
| RT-02.09 | Cumple | Revisión de arquitectura y prueba de integración | QA | 2.1 · 3.8.1 | H2 · H4 | 1 |
| RT-02.10 | Cumple | Revisión de arquitectura y prueba de integración | QA | 2.1 · 3.8.1 | H2 · H4 | 1 |
| RT-02.11 | Cumple | Revisión de arquitectura y prueba de integración | QA | 2.1 · 3.8.1 | H2 · H4 | 1 |
| RT-02.12 | Cumple | Revisión de arquitectura y prueba de integración | QA | 2.1 · 3.8.1 | H2 · H4 | 1 |
| RT-02.13 | Cumple | Revisión de arquitectura y prueba de integración | QA | 2.1 · 3.8.1 | H2 · H4 | 1 |
| RT-02.14 | Cumple | Revisión de arquitectura y prueba de integración | QA | 2.1 · 3.8.1 | H2 · H4 | 1 |
| RT-03.01 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.02 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.03 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.04 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.05 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.06 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.07 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.08 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.09 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.10 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.11 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.12 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.13 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.14 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.15 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.16 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.17 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.18 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.19 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.20 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.21 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.22 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.23 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.24 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-04.01 | Cumple | Puertas G1–G5 del pipeline | DEV · QA | 1.5.2 | H3 · H4 | 1 |
| RT-04.02 | Cumple | Puertas G1–G5 del pipeline | DEV · QA | 1.5.2 | H3 · H4 | 1 |
| RT-04.03 | Cumple | Puertas G1–G5 del pipeline | DEV · QA | 1.5.2 | H3 · H4 | 1 |
| RT-04.04 | Cumple | Puertas G1–G5 del pipeline | DEV · QA | 1.5.2 | H3 · H4 | 1 |
| RT-04.05 | Cumple | Puertas G1–G5 del pipeline | DEV · QA | 1.5.2 | H3 · H4 | 1 |
| RT-04.06 | Cumple | Puertas G1–G5 del pipeline | DEV · QA | 1.5.2 | H3 · H4 | 1 |
| RT-04.07 | Cumple | Puertas G1–G5 del pipeline | DEV · QA | 1.5.2 | H3 · H4 | 1 |
| RT-04.08 | Cumple | Puertas G1–G5 del pipeline | DEV · QA | 1.5.2 | H3 · H4 | 1 |
| RT-04.09 | Cumple | Puertas G1–G5 del pipeline | DEV · QA | 1.5.2 | H3 · H4 | 1 |
| RT-04.10 | Cumple | Puertas G1–G5 del pipeline | DEV · QA | 1.5.2 | H3 · H4 | 1 |
| RT-04.11 | Cumple | Puertas G1–G5 del pipeline | DEV · QA | 1.5.2 | H3 · H4 | 1 |
| RT-04.12 | Cumple | Puertas G1–G5 del pipeline | DEV · QA | 1.5.2 | H3 · H4 | 1 |
| RT-04.13 | Cumple | Puertas G1–G5 del pipeline | DEV · QA | 1.5.2 | H3 · H4 | 1 |
| RT-04.14 | Cumple | Puertas G1–G5 del pipeline | DEV · QA | 1.5.2 | H3 · H4 | 1 |
| RT-05.01 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 |
| RT-05.02 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 |
| RT-05.03 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 |
| RT-05.04 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 |
| RT-05.05 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 |
| RT-05.06 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 |
| RT-05.07 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 |
| RT-05.08 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 |
| RT-05.09 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 |
| RT-05.10 | Cumple parcialmente | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 |
| RT-05.11 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 |
| RT-05.12 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 |
| RT-05.13 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 |
| RT-05.14 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 |
| RT-05.15 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 |
| RT-05.16 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 |
| RT-05.17 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 |
| RT-05.18 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 |
| RT-05.19 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 |
| RT-05.20 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 |
| RT-05.21 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 |
| RT-05.22 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 |
| RT-05.23 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 |
| RT-05.24 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-05.25 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 · CP-RT-05.25-01 |
| RT-05.26 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 · CP-RT-05.26-01 |
| RT-05.27 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 · CP-RT-05.27-01 |
| RT-05.28 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 · CP-RT-05.28-01 |
| RT-05.29 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 · CP-RT-05.29-01 |
| RT-05.30 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 · CP-RT-05.30-01 |
| RT-06.01 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.01-01 |
| RT-06.02 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.02-01 |
| RT-06.03 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.03-01 |
| RT-06.04 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.04-01 |
| RT-06.05 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.05-01 |
| RT-06.06 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.06-01 |
| RT-06.07 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.07-01 |
| RT-06.08 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.08-01 |
| RT-06.09 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.09-01 |
| RT-06.10 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.10-01 |
| RT-06.11 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.11-01 |
| RT-06.12 | Cumple parcialmente | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.12-01 |
| RT-06.13 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.13-01 |
| RT-06.14 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.14-01 |
| RT-06.15 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.15-01 |
| RT-06.16 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.16-01 |
| RT-06.17 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.17-01 |
| RT-06.18 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.18-01 |
| RT-06.19 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.19-01 |
| RT-06.20 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.20-01 |
| RT-06.21 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.21-01 |
| RT-06.22 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.22-01 |
| RT-06.23 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.23-01 |
| RT-06.24 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.24-01 |
| RT-06.25 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.25-01 |
| RT-06.26 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.26-01 |
| RT-06.27 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.27-01 |
| RT-06.28 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.28-01 |
| RT-06.29 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.29-01 |
| RT-06.30 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.30-01 |
| RT-06.31 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.31-01 |
| RT-06.32 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.32-01 |
| RT-06.33 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.33-01 |
| RT-06.34 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 · CP-RT-06.34-01 |
| RT-07.01 | Cumple | Recuperación ante desastres y restauración | DR | 3.8.5 · 3.9.4 · 8.1.3 · 8.1.6 | H5 · H10 · semestral | 1 · CP-RT-07.01-01 |
| RT-07.02 | Cumple | Recuperación ante desastres y restauración | DR | 3.8.5 · 3.9.4 · 8.1.3 · 8.1.6 | H5 · H10 · semestral | 1 · CP-RT-07.02-01 |
| RT-07.03 | Cumple | Recuperación ante desastres y restauración | DR | 3.8.5 · 3.9.4 · 8.1.3 · 8.1.6 | H5 · H10 · semestral | 1 · CP-RT-07.03-01 |
| RT-07.04 | Cumple | Recuperación ante desastres y restauración | DR | 3.8.5 · 3.9.4 · 8.1.3 · 8.1.6 | H5 · H10 · semestral | 1 · CP-RT-07.04-01 |
| RT-07.05 | Cumple | Recuperación ante desastres y restauración | DR | 3.8.5 · 3.9.4 · 8.1.3 · 8.1.6 | H5 · H10 · semestral | 1 · CP-RT-07.05-01 |
| RT-07.06 | Cumple | Recuperación ante desastres y restauración | DR | 3.8.5 · 3.9.4 · 8.1.3 · 8.1.6 | H5 · H10 · semestral | 1 · CP-RT-07.06-01 |
| RT-07.07 | Cumple | Recuperación ante desastres y restauración | DR | 3.8.5 · 3.9.4 · 8.1.3 · 8.1.6 | H5 · H10 · semestral | 1 · CP-RT-07.07-01 |
| RT-07.08 | Cumple parcialmente | Recuperación ante desastres y restauración | DR | 3.8.5 · 3.9.4 · 8.1.3 · 8.1.6 | H5 · H10 · semestral | 1 · CP-RT-07.08-01 |
| RT-07.09 | Cumple | Recuperación ante desastres y restauración | DR | 3.8.5 · 3.9.4 · 8.1.3 · 8.1.6 | H5 · H10 · semestral | 1 · CP-RT-07.09-01 |
| RT-07.10 | Cumple | Recuperación ante desastres y restauración | DR | 3.8.5 · 3.9.4 · 8.1.3 · 8.1.6 | H5 · H10 · semestral | 1 · CP-RT-07.10-01 |
| RT-07.11 | Cumple | Recuperación ante desastres y restauración | DR | 3.8.5 · 3.9.4 · 8.1.3 · 8.1.6 | H5 · H10 · semestral | 1 · CP-RT-07.11-01 |
| RT-07.12 | Cumple | Recuperación ante desastres y restauración | DR | 3.8.5 · 3.9.4 · 8.1.3 · 8.1.6 | H5 · H10 · semestral | 1 · CP-RT-07.12-01 |
| RT-07.13 | Cumple | Recuperación ante desastres y restauración | DR | 3.8.5 · 3.9.4 · 8.1.3 · 8.1.6 | H5 · H10 · semestral | 1 · CP-RT-07.13-01 |
| RT-07.14 | Cumple | Recuperación ante desastres y restauración | DR | 3.8.5 · 3.9.4 · 8.1.3 · 8.1.6 | H5 · H10 · semestral | 1 · CP-RT-07.14-01 |
| RT-08.01 | Cumple | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 · CP-RT-08.01-01 |
| RT-08.02 | Cumple | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 · CP-RT-08.02-01 |
| RT-08.03 | Cumple | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 · CP-RT-08.03-01 |
| RT-08.04 | Cumple | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 · CP-RT-08.04-01 |
| RT-08.05 | Cumple | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 · CP-RT-08.05-01 |
| RT-08.06 | Cumple | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 · CP-RT-08.06-01 |
| RT-08.07 | Cumple | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 · CP-RT-08.07-01 |
| RT-08.08 | Cumple | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 · CP-RT-08.08-01 |
| RT-08.09 | Cumple | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 · CP-RT-08.09-01 |
| RT-08.10 | Cumple | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 · CP-RT-08.10-01 |
| RT-08.11 | Cumple | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 · CP-RT-08.11-01 |
| RT-08.12 | Cumple | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 · CP-RT-08.12-01 |
| RT-08.13 | Cumple | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 · CP-RT-08.13-01 |
| RT-08.14 | Cumple | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 · CP-RT-08.14-01 |
| RT-08.15 | Cumple | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 · CP-RT-08.15-01 |
| RT-08.16 | Cumple | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 · CP-RT-08.16-01 |
| RT-08.17 | Cumple | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 · CP-RT-08.17-01 |
| RT-08.18 | Cumple | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 · CP-RT-08.18-01 |
| RT-08.19 | Cumple | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 · CP-RT-08.19-01 |
| RT-09.01 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 1 · CP-RT-09.01-01 |
| RT-09.02 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 1 · CP-RT-09.02-01 |
| RT-09.03 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 1 · CP-RT-09.03-01 |
| RT-09.04 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 1 · CP-RT-09.04-01 |
| RT-09.05 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 1 · CP-RT-09.05-01 |
| RT-09.06 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 1 · CP-RT-09.06-01 |
| RT-09.07 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 1 · CP-RT-09.07-01 |
| RT-09.08 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 1 · CP-RT-09.08-01 |
| RT-09.09 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 1 · CP-RT-09.09-01 |
| RT-09.10 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 1 · CP-RT-09.10-01 |
| RT-10.01 | Cumple | Resiliencia por inyección de fallas | PREPROD | 3.8.4 · 3.9.3 · 8.2.2 | H5 · H10 · semestral | 1 · CP-RT-10.01-01 |
| RT-10.02 | Cumple | Resiliencia por inyección de fallas | PREPROD | 3.8.4 · 3.9.3 · 8.2.2 | H5 · H10 · semestral | 1 · CP-RT-10.02-01 |
| RT-10.03 | Cumple | Resiliencia por inyección de fallas | PREPROD | 3.8.4 · 3.9.3 · 8.2.2 | H5 · H10 · semestral | 1 · CP-RT-10.03-01 |
| RT-10.04 | Cumple | Resiliencia por inyección de fallas | PREPROD | 3.8.4 · 3.9.3 · 8.2.2 | H5 · H10 · semestral | 1 · CP-RT-10.04-01 |
| RT-10.05 | Cumple | Resiliencia por inyección de fallas | PREPROD | 3.8.4 · 3.9.3 · 8.2.2 | H5 · H10 · semestral | 1 · CP-RT-10.05-01 |
| RT-10.06 | Cumple | Resiliencia por inyección de fallas | PREPROD | 3.8.4 · 3.9.3 · 8.2.2 | H5 · H10 · semestral | 1 · CP-RT-10.06-01 |
| RT-10.07 | Cumple | Resiliencia por inyección de fallas | PREPROD | 3.8.4 · 3.9.3 · 8.2.2 | H5 · H10 · semestral | 1 · CP-RT-10.07-01 |
| RT-10.08 | Cumple | Resiliencia por inyección de fallas | PREPROD | 3.8.4 · 3.9.3 · 8.2.2 | H5 · H10 · semestral | 1 · CP-RT-10.08-01 |
| RT-10.09 | Cumple | Resiliencia por inyección de fallas | PREPROD | 3.8.4 · 3.9.3 · 8.2.2 | H5 · H10 · semestral | 1 · CP-RT-10.09-01 |
| RT-11.01 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 · CP-RT-11.01-01 |
| RT-11.02 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 · CP-RT-11.02-01 |
| RT-11.03 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 · CP-RT-11.03-01 |
| RT-11.04 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 · CP-RT-11.04-01 |
| RT-11.05 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 · CP-RT-11.05-01 |
| RT-11.06 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 · CP-RT-11.06-01 |
| RT-11.07 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 · CP-RT-11.07-01 |
| RT-11.08 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 · CP-RT-11.08-01 |
| RT-11.09 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 · CP-RT-11.09-01 |
| RT-11.10 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 · CP-RT-11.10-01 |
| RT-11.11 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 · CP-RT-11.11-01 |
| RT-11.12 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 · CP-RT-11.12-01 |
| RT-11.13 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 · CP-RT-11.13-01 |
| RT-11.14 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 · CP-RT-11.14-01 |
| RT-11.15 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 · CP-RT-11.15-01 |
| RT-11.16 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 · CP-RT-11.16-01 |
| RT-11.17 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 · CP-RT-11.17-01 |
| RT-11.18 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 · CP-RT-11.18-01 |
| RT-11.19 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 · CP-RT-11.19-01 |
| RT-11.20 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 · CP-RT-11.20-01 |
| RT-11.21 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 · CP-RT-11.21-01 |
| RT-11.22 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 · CP-RT-11.22-01 |
| RT-11.23 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 · CP-RT-11.23-01 |
| RT-11.24 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 · CP-RT-11.24-01 |
| RT-11.25 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 · CP-RT-11.25-01 |
| RT-11.26 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 · CP-RT-11.26-01 |
| RT-11.27 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 · CP-RT-11.27-01 |
| RT-11.28 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 · CP-RT-11.28-01 |
| RT-12.01 | Cumple | Prueba funcional de identidad y acceso | QA | 3.8.1 · 3.8.6 | H4 · H5 | 1 · CP-RT-12.01-01 |
| RT-12.02 | Cumple | Prueba funcional de identidad y acceso | QA | 3.8.1 · 3.8.6 | H4 · H5 | 1 · CP-RT-12.02-01 |
| RT-12.03 | Cumple | Prueba funcional de identidad y acceso | QA | 3.8.1 · 3.8.6 | H4 · H5 | 1 · CP-RT-12.03-01 |
| RT-12.04 | Cumple | Prueba funcional de identidad y acceso | QA | 3.8.1 · 3.8.6 | H4 · H5 | 1 · CP-RT-12.04-01 |
| RT-12.05 | Cumple | Prueba funcional de identidad y acceso | QA | 3.8.1 · 3.8.6 | H4 · H5 | 1 · CP-RT-12.05-01 |
| RT-12.06 | Cumple | Prueba funcional de identidad y acceso | QA | 3.8.1 · 3.8.6 | H4 · H5 | 1 · CP-RT-12.06-01 |
| RT-12.07 | Cumple | Prueba funcional de identidad y acceso | QA | 3.8.1 · 3.8.6 | H4 · H5 | 1 · CP-RT-12.07-01 |
| RT-12.08 | Cumple | Prueba funcional de identidad y acceso | QA | 3.8.1 · 3.8.6 | H4 · H5 | 1 · CP-RT-12.08-01 |
| RT-12.09 | Cumple | Prueba funcional de identidad y acceso | QA | 3.8.1 · 3.8.6 | H4 · H5 | 1 · CP-RT-12.09-01 |
| RT-12.10 | Cumple | Prueba funcional de identidad y acceso | QA | 3.8.1 · 3.8.6 | H4 · H5 | 1 · CP-RT-12.10-01 |
| RT-12.11 | Cumple | Prueba funcional de identidad y acceso | QA | 3.8.1 · 3.8.6 | H4 · H5 | 1 · CP-RT-12.11-01 |
| RT-12.12 | Cumple | Prueba funcional de identidad y acceso | QA | 3.8.1 · 3.8.6 | H4 · H5 | 1 · CP-RT-12.12-01 |
| RT-12.13 | Cumple | Prueba funcional de identidad y acceso | QA | 3.8.1 · 3.8.6 | H4 · H5 | 1 · CP-RT-12.13-01 |
| RT-13.01 | Cumple | Accesibilidad WCAG 2.2 AA y usabilidad | QA · PREPROD · Terreno | 2.6.2 · 3.8.2 · 3.9.2 | H5 · H10 | 1 · CP-RT-13.01-01 |
| RT-13.02 | Cumple | Accesibilidad WCAG 2.2 AA y usabilidad | QA · PREPROD · Terreno | 2.6.2 · 3.8.2 · 3.9.2 | H5 · H10 | 1 · CP-RT-13.02-01 |
| RT-13.03 | Cumple | Accesibilidad WCAG 2.2 AA y usabilidad | QA · PREPROD · Terreno | 2.6.2 · 3.8.2 · 3.9.2 | H5 · H10 | 1 · CP-RT-13.03-01 |
| RT-13.04 | Cumple | Accesibilidad WCAG 2.2 AA y usabilidad | QA · PREPROD · Terreno | 2.6.2 · 3.8.2 · 3.9.2 | H5 · H10 | 1 · CP-RT-13.04-01 |
| RT-13.05 | Cumple | Accesibilidad WCAG 2.2 AA y usabilidad | QA · PREPROD · Terreno | 2.6.2 · 3.8.2 · 3.9.2 | H5 · H10 | 1 · CP-RT-13.05-01 |
| RT-13.06 | Cumple | Accesibilidad WCAG 2.2 AA y usabilidad | QA · PREPROD · Terreno | 2.6.2 · 3.8.2 · 3.9.2 | H5 · H10 | 1 · CP-RT-13.06-01 |
| RT-13.07 | Cumple | Accesibilidad WCAG 2.2 AA y usabilidad | QA · PREPROD · Terreno | 2.6.2 · 3.8.2 · 3.9.2 | H5 · H10 | 1 · CP-RT-13.07-01 |
| RT-13.08 | Cumple | Accesibilidad WCAG 2.2 AA y usabilidad | QA · PREPROD · Terreno | 2.6.2 · 3.8.2 · 3.9.2 | H5 · H10 | 1 · CP-RT-13.08-01 |
| RT-13.09 | Cumple | Accesibilidad WCAG 2.2 AA y usabilidad | QA · PREPROD · Terreno | 2.6.2 · 3.8.2 · 3.9.2 | H5 · H10 | 1 · CP-RT-13.09-01 |
| RT-13.10 | Cumple | Accesibilidad WCAG 2.2 AA y usabilidad | QA · PREPROD · Terreno | 2.6.2 · 3.8.2 · 3.9.2 | H5 · H10 | 1 · CP-RT-13.10-01 |
| RT-13.11 | Cumple | Accesibilidad WCAG 2.2 AA y usabilidad | QA · PREPROD · Terreno | 2.6.2 · 3.8.2 · 3.9.2 | H5 · H10 | 1 · CP-RT-13.11-01 |
| RT-13.12 | Cumple | Accesibilidad WCAG 2.2 AA y usabilidad | QA · PREPROD · Terreno | 2.6.2 · 3.8.2 · 3.9.2 | H5 · H10 | 1 · CP-RT-13.12-01 |
| RT-14.01 | Cumple | Prueba de observabilidad y medición en marcha blanca | PREPROD · PROD | 3.8.4 · 4.2 | H5 · H7 | 1 · CP-RT-14.01-01 |
| RT-14.02 | Cumple | Prueba de observabilidad y medición en marcha blanca | PREPROD · PROD | 3.8.4 · 4.2 | H5 · H7 | 1 · CP-RT-14.02-01 |
| RT-14.03 | Cumple | Prueba de observabilidad y medición en marcha blanca | PREPROD · PROD | 3.8.4 · 4.2 | H5 · H7 | 1 · CP-RT-14.03-01 |
| RT-14.04 | Cumple | Prueba de observabilidad y medición en marcha blanca | PREPROD · PROD | 3.8.4 · 4.2 | H5 · H7 | 1 · CP-RT-14.04-01 |
| RT-14.05 | Cumple | Prueba de observabilidad y medición en marcha blanca | PREPROD · PROD | 3.8.4 · 4.2 | H5 · H7 | 1 · CP-RT-14.05-01 |
| RT-14.06 | Cumple | Prueba de observabilidad y medición en marcha blanca | PREPROD · PROD | 3.8.4 · 4.2 | H5 · H7 | 1 · CP-RT-14.06-01 |
| RT-14.07 | Cumple | Prueba de observabilidad y medición en marcha blanca | PREPROD · PROD | 3.8.4 · 4.2 | H5 · H7 | 1 · CP-RT-14.07-01 |
| RT-14.08 | Cumple | Prueba de observabilidad y medición en marcha blanca | PREPROD · PROD | 3.8.4 · 4.2 | H5 · H7 | 1 · CP-RT-14.08-01 |
| RT-14.09 | Cumple | Prueba de observabilidad y medición en marcha blanca | PREPROD · PROD | 3.8.4 · 4.2 | H5 · H7 | 1 · CP-RT-14.09-01 |
| RT-15.01 | Cumple | Inspección documental y medición | — | 3.8.7 | H5 | 1 · CP-RT-15.01-01 |
| RT-15.02 | Cumple parcialmente | Inspección documental y medición | — | 3.8.7 | H5 | 1 · CP-RT-15.02-01 |
| RT-15.03 | Cumple parcialmente | Inspección documental y medición | — | 3.8.7 | H5 | 1 · CP-RT-15.03-01 |
| RT-15.04 | Cumple parcialmente | Inspección documental y medición | — | 3.8.7 | H5 | 1 · CP-RT-15.04-01 |
| RT-15.05 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-15.06 | Cumple | Inspección documental y medición | — | 3.8.7 | H5 | 1 · CP-RT-15.06-01 |
| RT-15.07 | Cumple parcialmente | Inspección documental y medición | — | 3.8.7 | H5 | 1 · CP-RT-15.07-01 |
| RT-15.08 | Cumple parcialmente | Inspección documental y medición | — | 3.8.7 | H5 | 1 · CP-RT-15.08-01 |
| RT-15.09 | Cumple | Inspección documental y medición | — | 3.8.7 | H5 | 1 · CP-RT-15.09-01 |
| RT-16.01 | Cumple | Sistema y aceptación de usuario — La solución dispondrá de un módulo de administración que permita al CLIENTE, sin intervención del ADJUDICATARIO, gestionar personas usuarias, roles, permisos, unidades organizacionales y sus jerarquías. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.01-01 |
| RT-16.02 | Cumple | Sistema y aceptación de usuario — Las reglas de negocio parametrizables —umbrales, plazos, montos, tolerancias, catálogos, listas de valores, textos de notificación— serán configurables desde la interfaz de administración, con control de versiones y registro de quién cambió qué y cuándo. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.02-01 |
| RT-16.03 | Cumple | Sistema y aceptación de usuario — Todo cambio de parámetro con impacto operacional requerirá aprobación de un segundo perfil y quedará registrado con su justificación. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.03-01 |
| RT-16.04 | Cumple | Sistema y aceptación de usuario — El PROPONENTE declarará expresamente qué elementos son parametrizables y cuáles requieren desarrollo. Presentar como parametrizable lo que exige desarrollo se evaluará como observación grave. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.04-01 |
| RT-16.05 | Cumple | Sistema y aceptación de usuario — Existirá un ambiente de simulación que permita probar el efecto de un cambio de parámetro antes de aplicarlo a producción. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.05-01 |
| RT-16.06 | Cumple | Sistema y aceptación de usuario — Toda operación que cree, modifique o elimine información quedará registrada con identificación de la persona o del sistema que la ejecutó, fecha y hora con zona horaria, origen, valores anteriores y valores posteriores. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.06-01 |
| RT-16.07 | Cumple | Sistema y aceptación de usuario — El registro de auditoría será inalterable y no podrá ser modificado ni eliminado por ningún perfil, incluido el administrador de la plataforma. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.07-01 |
| RT-16.08 | Cumple | Sistema y aceptación de usuario — El CLIENTE podrá consultar y exportar la auditoría desde la interfaz, con filtros por persona, período, entidad y tipo de operación, sin requerir acceso a la base de datos. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.08-01 |
| RT-16.09 | Cumple | Sistema y aceptación de usuario — Las consultas a información sensible quedarán registradas, no sólo las modificaciones. Caso 02, cap. 15 — Registro de consultas a información sensible: Exigible para los antecedentes comerciales y el comportamiento de pago de los clientes, y para los datos de geolocalización de personas, además del registro de modificaciones. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.09-01 |
| RT-16.10 | Cumple | Sistema y aceptación de usuario — El período de retención de la auditoría será el que fije el caso y, en su defecto, no inferior a cinco años. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.10-01 |
| RT-16.11 | Cumple | Sistema y aceptación de usuario — La solución soportará flujos de trabajo con estados, transiciones, responsables, plazos, escalamiento automático por vencimiento y delegación por ausencia. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.11-01 |
| RT-16.12 | Cumple | Sistema y aceptación de usuario — Los flujos serán configurables por el CLIENTE sin desarrollo, al menos en lo relativo a responsables, plazos y niveles de aprobación. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.12-01 |
| RT-16.13 | Cumple | Sistema y aceptación de usuario — Toda solicitud pendiente será visible para su responsable en una bandeja de tareas unificada, con priorización y alerta de vencimiento. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.13-01 |
| RT-16.14 | Cumple | Sistema y aceptación de usuario — El motor de reglas permitirá definir condiciones de negocio evaluables sin recompilación, con trazabilidad de qué regla se aplicó a cada transacción. Caso 02, cap. 15 — Firma electrónica: La prueba de entrega debe articularse con la guía de despacho electrónica y su acuse de recibo conforme a la normativa tributaria vigente. El PROPONENTE deberá investigar y proponer el mecanismo, considerando que el receptor habitual es una persona natural sin firma electrónica avanzada. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.14-01 |
| RT-16.15 | Cumple | Sistema y aceptación de usuario — La solución gestionará documentos con versionado, metadatos, control de acceso, búsqueda por contenido y por metadato, y previsualización sin descarga. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.15-01 |
| RT-16.16 | Cumple | Sistema y aceptación de usuario — Los documentos se almacenarán cifrados, con verificación de integridad y retención conforme a la política del caso. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.16-01 |
| RT-16.17 | Cumple | Sistema y aceptación de usuario — La solución soportará firma electrónica conforme a la Ley N° 19.799, con firma avanzada para los actos que el caso lo requiera, y verificación de validez del certificado al momento de la firma. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.17-01 |
| RT-16.18 | Cumple | Sistema y aceptación de usuario — Se generará el sello de tiempo y se conservará la evidencia de firma que permita verificar el documento con posterioridad al vencimiento del certificado. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.18-01 |
| RT-16.19 | Cumple | Sistema y aceptación de usuario — La solución generará documentos a partir de plantillas administrables por el CLIENTE, con datos de la transacción y salida en formato abierto. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.19-01 |
| RT-16.20 | Cumple | Sistema y aceptación de usuario — La solución enviará notificaciones por al menos tres canales: correo electrónico, notificación en la aplicación y mensajería instantánea o SMS, según lo que el caso requiera. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.20-01 |
| RT-16.21 | Cumple | Sistema y aceptación de usuario — Las plantillas de notificación serán administrables por el CLIENTE, con variables de la transacción, y versionadas. Caso 02, cap. 15 — Canales de notificación: Correo electrónico, notificación en aplicación, mensajería instantánea al cliente del canal tradicional, y mensaje de texto para avisos de despacho y de llegada. El canal debe elegirse por cliente, porque buena parte del canal tradicional no usa correo. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.21-01 |
| RT-16.22 | Cumple | Sistema y aceptación de usuario — Cada persona usuaria podrá configurar sus preferencias de canal y de frecuencia, respetando las notificaciones que el CLIENTE defina como obligatorias. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.22-01 |
| RT-16.23 | Cumple | Sistema y aceptación de usuario — El envío será asíncrono, con reintento ante falla, control de duplicados y registro de entrega, apertura y error por cada mensaje. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.23-01 |
| RT-16.24 | Cumple | Sistema y aceptación de usuario — El PROPONENTE declarará el proveedor de cada canal, su costo unitario, su volumen proyectado y el tratamiento del costo variable en la Oferta Económica. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.24-01 |
| RT-16.25 | Cumple | Sistema y aceptación de usuario — Las notificaciones respetarán la normativa de comunicaciones comerciales y permitirán la baja cuando corresponda. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.25-01 |
| RT-16.26 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-16.27 | Cumple | Sistema y aceptación de usuario — La solución dispondrá de búsqueda global con indexación de texto completo, tolerancia a errores de escritura, filtros facetados y respeto del control de acceso de la persona que busca. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.27-01 |
| RT-16.28 | Cumple | Sistema y aceptación de usuario — Los listados serán ordenables, filtrables, paginados y exportables en formatos abiertos, con el filtro aplicado reflejado en la exportación. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.28-01 |
| RT-16.29 | Cumple | Sistema y aceptación de usuario — Las exportaciones de gran volumen se procesarán de forma asíncrona, con notificación al completarse y sin bloquear la sesión. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.29-01 |
| RT-16.30 | Cumple | Sistema y aceptación de usuario — Toda exportación de información sensible quedará registrada en la auditoría, con identificación de quién exportó qué y cuándo. Caso 02, cap. 15 — Portal público: Catálogo público de productos sin precios. Portal autenticado para clientes, con pedido en autoservicio, estado de entrega, documentos y saldo. Portal autenticado para transportistas y para proveedores. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.30-01 |
| RT-16.31 | Cumple | Sistema y aceptación de usuario — La solución dispondrá de un portal público con la información que el caso determine, accesible sin autenticación, con los mismos estándares de accesibilidad y desempeño que el resto de la plataforma. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.31-01 |
| RT-16.32 | Cumple | Sistema y aceptación de usuario — Las personas usuarias externas dispondrán de autoatención para las consultas de mayor frecuencia, evitando el contacto telefónico para operaciones simples. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.32-01 |
| RT-16.33 | Cumple | Sistema y aceptación de usuario — El PROPONENTE estimará la reducción esperada del volumen de atención asistida por efecto de la autoatención y comprometerá el indicador. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.33-01 |
| RT-16.34 | Cumple | Sistema y aceptación de usuario — El portal público resistirá picos de tráfico sin degradar los servicios transaccionales internos, mediante aislamiento de recursos y caché. | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 · CP-RT-16.34-01 |
| RT-17.01 | Cumple | Perfil operacional móvil | Terreno | 3.8.3 | H5 | 1 · CP-RT-17.01-01 |
| RT-17.02 | Cumple | Perfil operacional móvil | Terreno | 3.8.3 | H5 | 1 · CP-RT-17.02-01 |
| RT-17.03 | Cumple | Perfil operacional móvil | Terreno | 3.8.3 | H5 | 1 · CP-RT-17.03-01 |
| RT-17.04 | Cumple | Perfil operacional móvil | Terreno | 3.8.3 | H5 | 1 · CP-RT-17.04-01 |
| RT-17.05 | Cumple | Perfil operacional móvil | Terreno | 3.8.3 | H5 | 1 · CP-RT-17.05-01 |
| RT-17.06 | Cumple | Perfil operacional móvil | Terreno | 3.8.3 | H5 | 1 · CP-RT-17.06-01 |
| RT-17.07 | Cumple | Perfil operacional móvil | Terreno | 3.8.3 | H5 | 1 · CP-RT-17.07-01 |
| RT-17.08 | Cumple | Perfil operacional móvil | Terreno | 3.8.3 | H5 | 1 · CP-RT-17.08-01 |
| RT-18.01 | Cumple | Sistema y aceptación de usuario — El PROPONENTE declarará cada componente de inteligencia artificial: propósito, modelo o servicio empleado, proveedor, versión y ubicación de procesamiento de los datos. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 1 · CP-RT-18.01-01 |
| RT-18.02 | Cumple | Sistema y aceptación de usuario — Se garantizará contractualmente que los datos del CLIENTE no serán utilizados para entrenar modelos de terceros, salvo autorización expresa y escrita. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 1 · CP-RT-18.02-01 |
| RT-18.03 | Cumple | Sistema y aceptación de usuario — Se documentarán los límites de uso, los casos en que el resultado requiere validación humana previa y el procedimiento de supervisión. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 1 · CP-RT-18.03-01 |
| RT-18.04 | Cumple | Sistema y aceptación de usuario — Los riesgos de sesgo, alucinación, fuga de información y uso indebido se evaluarán y mitigarán conforme al NIST AI Risk Management Framework 1.0 y a la norma ISO/IEC 42001. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 1 · CP-RT-18.04-01 |
| RT-18.05 | Cumple | Sistema y aceptación de usuario — Toda interacción relevante con un componente de inteligencia artificial quedará registrada para efectos de auditoría y trazabilidad, incluyendo la entrada, la salida y la decisión humana posterior. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 1 · CP-RT-18.05-01 |
| RT-18.06 | Cumple | Sistema y aceptación de usuario — El componente podrá desactivarse sin comprometer la operación del resto de la solución, y existirá un procedimiento manual de respaldo para la función que automatiza. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 1 · CP-RT-18.06-01 |
| RT-18.07 | Cumple | Sistema y aceptación de usuario — Cuando el resultado se presente a una persona usuaria, se indicará expresamente que fue generado o sugerido de forma automática, y su nivel de confianza cuando el modelo lo provea. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 1 · CP-RT-18.07-01 |
| RT-18.08 | Cumple | Sistema y aceptación de usuario — Los modelos predictivos declararán sus variables de entrada, su métrica de desempeño, su línea base y su plan de reentrenamiento y de detección de deriva. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 1 · CP-RT-18.08-01 |
| RT-18.09 | Cumple | Sistema y aceptación de usuario — La responsabilidad por los resultados de los componentes de inteligencia artificial recae íntegramente en el ADJUDICATARIO, conforme al Artículo 86° de las Bases Administrativas. | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 1 · CP-RT-18.09-01 |
| RT-18.10 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-19.01 | Cumple | Auditoría de gobierno: actas, informe y tablero | — | Cuenta 1 | H1 · mensual | 1 |
| RT-19.02 | Cumple | Auditoría de gobierno: actas, informe y tablero | — | Cuenta 1 | H1 · mensual | 1 |
| RT-19.03 | Cumple | Auditoría de gobierno: actas, informe y tablero | — | Cuenta 1 | H1 · mensual | 1 |
| RT-19.04 | Cumple | Auditoría de gobierno: actas, informe y tablero | — | Cuenta 1 | H1 · mensual | 1 |
| RT-19.05 | Cumple | Auditoría de gobierno: actas, informe y tablero | — | Cuenta 1 | H1 · mensual | 1 |
| RT-19.06 | Cumple | Auditoría de gobierno: actas, informe y tablero | — | Cuenta 1 | H1 · mensual | 1 |
| RT-19.07 | Cumple | Auditoría de gobierno: actas, informe y tablero | — | Cuenta 1 | H1 · mensual | 1 |
| RT-19.08 | Cumple | Auditoría de gobierno: actas, informe y tablero | — | Cuenta 1 | H1 · mensual | 1 |
| RT-19.09 | Cumple | Auditoría de gobierno: actas, informe y tablero | — | Cuenta 1 | H1 · mensual | 1 |
| RT-19.10 | Cumple | Auditoría de gobierno: actas, informe y tablero | — | Cuenta 1 | H1 · mensual | 1 |
| RT-20.01 | Cumple | Aceptación y cierre de marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 1 |
| RT-20.02 | Cumple | Aceptación y cierre de marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 1 |
| RT-20.03 | Cumple | Aceptación y cierre de marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 1 |
| RT-20.04 | Cumple | Aceptación y cierre de marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 1 |
| RT-20.05 | Cumple | Aceptación y cierre de marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 1 |
| RT-20.06 | Cumple | Aceptación y cierre de marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 1 |
| RT-20.07 | Cumple | Aceptación y cierre de marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 1 |
| RT-20.08 | Cumple | Aceptación y cierre de marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 1 |
| RT-21.01 | Cumple | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.02 | Cumple | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.03 | Cumple parcialmente | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.04 | Cumple | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.05 | Cumple | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.06 | Cumple | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.07 | Cumple | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.08 | Cumple | Revisión mensual de la atención por nivel y de la base de conocimiento | PROD | Cuentas 8.1 y 8.5 | Mensual | 1 |
| RT-21.09 | Cumple | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.10 | Cumple | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.11 | Cumple | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.12 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-21.13 | Cumple | Inspección del tablero del CLIENTE y de sus permisos | PROD | Cuenta 8.1 | Mensual | 1 |
| RT-21.14 | Cumple | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.15 | Cumple | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.16 | Cumple | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.17 | Cumple | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.18 | Cumple | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.19 | Cumple | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.20 | Cumple | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.21 | Cumple | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.22 | Cumple | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-22.01 | Cumple | Certificación de usuarios | PREPROD · PROD | 7.3.1 · 7.3.2 | H6 · H11 | 1 |
| RT-22.02 | Cumple | Certificación de usuarios | PREPROD · PROD | 7.3.1 · 7.3.2 | H6 · H11 | 1 |
| RT-22.03 | Cumple | Certificación de usuarios | PREPROD · PROD | 7.3.1 · 7.3.2 | H6 · H11 | 1 |
| RT-22.04 | Cumple | Certificación de usuarios | PREPROD · PROD | 7.3.1 · 7.3.2 | H6 · H11 | 1 |
| RT-22.05 | Cumple | Certificación de usuarios | PREPROD · PROD | 7.3.1 · 7.3.2 | H6 · H11 | 1 |
| RT-22.06 | Cumple | Certificación de usuarios | PREPROD · PROD | 7.3.1 · 7.3.2 | H6 · H11 | 1 |
| RT-22.07 | Cumple | Certificación de usuarios | PREPROD · PROD | 7.3.1 · 7.3.2 | H6 · H11 | 1 |
| RT-22.08 | Cumple | Certificación de usuarios | PREPROD · PROD | 7.3.1 · 7.3.2 | H6 · H11 | 1 |
| RT-22.09 | Cumple | Certificación de usuarios | PREPROD · PROD | 7.3.1 · 7.3.2 | H6 · H11 | 1 |
| RT-23.01 | Cumple | Inspección del entregable de la oferta | — | — | Presentación de la oferta | 1 |
| RT-23.02 | Cumple | Inspección del entregable de la oferta | — | — | Presentación de la oferta | 1 |
| RT-23.03 | Cumple parcialmente | Inspección del entregable de la oferta | — | — | Presentación de la oferta | 1 |
| RT-23.04 | Cumple | Inspección del entregable de la oferta | — | — | Presentación de la oferta | 1 |
| RT-23.05 | Cumple | Inspección del entregable de la oferta | — | — | Presentación de la oferta | 1 |
| RT-23.06 | Cumple | Inspección del entregable de la oferta | — | — | Presentación de la oferta | 1 |
| RT-23.07 | Cumple | Inspección del entregable de la oferta | — | — | Presentación de la oferta | 1 |
| RT-23.08 | Cumple | Inspección del entregable de la oferta | — | — | Presentación de la oferta | 1 |
| RT-23.09 | Cumple | Inspección del entregable de la oferta | — | — | Presentación de la oferta | 1 |
| RT-23.10 | Cumple | Inspección del entregable de la oferta | — | — | Presentación de la oferta | 1 |
| RT-24.01 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-24.02 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-24.03 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-24.04 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-24.05 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-24.06 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-25.01 | Cumple parcialmente | Inspección del entregable de la oferta | Documento de la oferta | Sin paquete de la EDT | Presentación de la oferta | 1 · CP-RT-25.01-01 |
| RT-25.02 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-25.03 | Cumple parcialmente | Inspección del entregable de la oferta | Documento de la oferta | Sin paquete de la EDT | Presentación de la oferta | 1 · CP-RT-25.03-01 |
| RT-25.04 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-25.05 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-25.06 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-25.07 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-25.08 | Cumple parcialmente | Inspección del entregable de la oferta | Documento de la oferta | Sin paquete de la EDT | Presentación de la oferta | 1 · CP-RT-25.08-01 |
| RT-25.09 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-25.10 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-26.01 | Cumple | Indicador de verificación de la innovación (T-19) | PROD | 3.10 | Según T-19 | 1 · CP-RT-26.01-01 |
| RT-26.02 | Cumple | Indicador de verificación de la innovación (T-19) | PROD | 3.10 | Según T-19 | 1 · CP-RT-26.02-01 |
| RT-26.03 | Cumple | Indicador de verificación de la innovación (T-19) | PROD | 3.10 | Según T-19 | 1 · CP-RT-26.03-01 |
| RT-26.04 | Cumple | Indicador de verificación de la innovación (T-19) | PROD | 3.10 | Según T-19 | 1 · CP-RT-26.04-01 |
| RT-26.05 | Cumple | Indicador de verificación de la innovación (T-19) | PROD | 3.10 | Según T-19 | 1 · CP-RT-26.05-01 |
| RT-26.06 | Cumple | Indicador de verificación de la innovación (T-19) | PROD | 3.10 | Según T-19 | 1 · CP-RT-26.06-01 |
| RT-26.07 | Cumple | Indicador de verificación de la innovación (T-19) | PROD | 3.10 | Según T-19 | 1 · CP-RT-26.07-01 |
| RT-26.08 | Cumple | Indicador de verificación de la innovación (T-19) | PROD | 3.10 | Según T-19 | 1 · CP-RT-26.08-01 |

La matriz muestra que los requisitos funcionales se aceptan en la certificación de su etapa (H5 o H10), mientras que los no funcionales que dependen de la operación real se aceptan al cierre de la marcha blanca (H7 o H12). Los requisitos técnicos de operación y soporte (capítulo 21) no tienen hito de implementación: se verifican mes a mes con la medición de los niveles de servicio. Cada caso de prueba se identifica como CP-«ID»-nn, por ejemplo CP-RF-01.01-03, y lleva el identificador en su anotación de código; la última columna de la matriz lista los casos de cada requisito, de modo que la matriz se regenera desde el repositorio en cada ejecución del pipeline.

## Anexo 9.D — Especificación de los datos de prueba

Este anexo detalla los juegos de datos que usa la estrategia de la sección 9.2.4 del Subdocumento 9. Ningún juego de datos de prueba contiene datos productivos sin anonimización verificada con Amazon Macie y con una prueba de reidentificación documentada. Cada juego se versiona y se restituye a un estado conocido antes de su ciclo de pruebas. El sitio de Recuperación ante Desastres no es un juego de prueba: es una réplica productiva restringida para conmutación real.

### 9.D.1 Volumen de los juegos de datos

Los volúmenes se derivan de la volumetría del Caso, sección 14.1. El juego de peak escala el día normal por la razón entre las entregas de un día de peak y las de un día normal: 2.600 / 1.400 = 1,86. La operación trabaja de lunes a sábado, de modo que un mes tiene 6 × 52 / 12 = 26 días hábiles. Con 260.000 líneas de preparación al mes y esos 26 días hábiles, un día normal tiene unas 10.000 líneas y un día de peak, unas 18.600. La Tabla 9.D.1 presenta los juegos.

**Tabla 9.D.1 — Juegos de datos de prueba. Fuente: elaboración propia a partir del Caso 02, sección 14.1, y del SD5, sección 5.3.**

| Juego | Contenido | Volumen | Origen | Ambiente | Restitución |
| --- | --- | --- | --- | --- | --- |
| JD-01 Maestros | Clientes y puntos de entrega, SKU, proveedores, ubicaciones, vehículos, conductores y preventistas | 14.200 clientes; 8.400 SKU (1.100 con frío); 180 proveedores; 62 preventistas; 200 conductores | Sintético | DEV · QA · PREPROD | Antes de cada ciclo |
| JD-02 Día normal | Pedidos, líneas, preparación, carga, entregas, cobros y guías de un día hábil | ≈ 1.190 pedidos; ≈ 10.000 líneas; ≈ 1.400 entregas; ≈ 450 cobros en efectivo | Sintético | QA · PREPROD | Antes de cada ciclo |
| JD-03 Día de peak | El día normal escalado al peak de septiembre | ≈ 18.600 líneas; ≈ 2.600 entregas | Sintético | PREPROD | Antes de cada prueba de carga |
| JD-04 Turno sin señal | Jornada completa de un repartidor de ruta rural y de un preventista, registrada sin conexión | 14 h de eventos por dispositivo; 158 dispositivos simultáneos | Sintético | PREPROD · Terreno | Antes de cada prueba de desconexión |
| JD-05 Corte del CD | 24 h de recepción, preparación y despacho de Talca sin enlace | Un día de peak del CD de Talca | Sintético | PREPROD | Antes de cada prueba de corte |
| JD-06 Frío | Series de temperatura de cámaras y vehículos con excursiones térmicas controladas | Lecturas por sensor durante 30 días, con excursiones en los límites del rango | Sintético | QA · PREPROD | Antes de cada ciclo |
| JD-07 Retiro sanitario | Lote sembrado en recepción y distribuido a clientes para el simulacro de retiro | 1 lote trazado de recepción a entrega | Sintético | PREPROD | Antes de cada simulacro |
| JD-08 Migración | Históricos del CLIENTE anonimizados para los dos ensayos | 32,11 GB de destino | Histórico anonimizado | PREPROD | Por ensayo; se elimina al cerrar el ensayo |
| JD-09 Integraciones | Mensajes de las 15 integraciones, con casos de ausencia de respuesta, error, lentitud, duplicado y orden | 353.333 mensajes diarios en peak | Sintético | QA · PREPROD | Antes de cada ciclo |
| JD-10 Incidentes de terreno | Evidencia de incidentes reproducidos por INN-02 | Según incidentes registrados | Evidencia anonimizada | QA | Permanente como regresión |

Los juegos de día normal y de peak cubren el perfil horario que exige el Caso, porque se generan con la distribución de las cuatro ventanas del SD4: preventa entre 09:00 y 18:00, preparación entre 22:00 y 06:00, despacho entre 05:30 y 07:00 y sincronización entre 17:00 y 20:00. Los pedidos diarios del JD-02 se obtienen de 31.000 pedidos al mes en 26 días hábiles, y los cobros, de 11.800 cobros en efectivo al mes en el mismo período.

### 9.D.2 Reglas de anonimización

Los datos históricos del JD-08 y la evidencia del JD-10 se transforman antes de salir de Producción, con las reglas de la Tabla 9.D.2. Las reglas preservan la integridad referencial y la distribución estadística que necesitan las pruebas. La salida esperada es un conjunto anonimizado para los efectos de prueba; antes de liberarlo se ejecuta una prueba documentada de reidentificación sobre seudónimos, trazas, antecedentes comerciales y evidencias, y cualquier coincidencia atribuible a una persona bloquea la carga.

**Tabla 9.D.2 — Reglas de anonimización por categoría de dato. Fuente: elaboración propia a partir de la Ley N.º 21.719 y del Caso 02, capítulo 15, RT-11.10.**

| Categoría | Ejemplo | Regla |
| --- | --- | --- |
| Identificador de persona | RUT de cliente, conductor o preventista | Seudónimo determinista con clave secreta por ambiente, que conserva las relaciones entre tablas |
| Nombre y contacto | Nombre, teléfono, correo | Reemplazo por valores sintéticos del mismo formato |
| Geolocalización de personas | Trazas de conductores y preventistas | Generalización a la comuna y desplazamiento temporal; se eliminan las trazas fuera de jornada |
| Antecedentes comerciales | Comportamiento de pago, crédito, deuda | Perturbación por tramos que conserva la distribución, sin valores reales individuales |
| Evidencia de entrega | Firma, fotografía, nombre del receptor | Sustitución por imágenes sintéticas y nombres ficticios |
| Documentos tributarios | Folio, receptor, montos | Folios de prueba y receptores seudonimizados; los montos se perturban por tramos |

Toda copia transformada pasa por Amazon Macie y por la prueba de reidentificación antes de llegar a Preproducción. Un hallazgo de dato personal, una clave de seudonimización mal protegida o una coincidencia que permita atribuir una fila a una persona detiene la carga y obliga a corregir la regla que falló. Los datos del JD-08 se eliminan de forma segura al cerrar cada ensayo de migración, conforme a la política de eliminación del SD5, sección 5.2.

## Referencias

Las fuentes citadas en estos anexos se listan en formato APA 7.ª edición. Las Bases se citan en el texto con su documento y el artículo, capítulo, sección o código del requisito.

- Distribuidora Puelche S.A. (2026a). *Bases Administrativas de Licitación N.º TFEP-01/2026: Contratación de Solución Integral de Software y Servicios de Operación*.
- Distribuidora Puelche S.A. (2026b). *Bases Técnicas Transversales de Licitación N.º TFEP-01/2026*.
- Distribuidora Puelche S.A. (2026c). *Caso 02: Logística. Especificaciones del problema y operación de Distribuidora Puelche S.A.*
- International Organization for Standardization & International Electrotechnical Commission. (2011). *ISO/IEC 25010:2011 Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models*. ISO.
- Ley N.º 21.719. (2024). *Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales*. Diario Oficial de la República de Chile.
- Martin, R. C. (2003). *Agile software development: Principles, patterns, and practices*. Prentice Hall.
- McCabe, T. J. (1976). A complexity measure. *IEEE Transactions on Software Engineering, SE-2*(4), 308–320.
- World Wide Web Consortium. (2023). *Web Content Accessibility Guidelines (WCAG) 2.2*. W3C.

## Declaración de uso de IA

La tabla declara el apoyo de IA conforme a las Aclaraciones, §7.2.

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
| --- | --- | --- | --- | --- | --- |
| Anexo 9.A | Claude Code | Métricas y umbrales por subcaracterística | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| Anexo 9.B | Claude Code | Reglas y configuración de análisis | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| Anexo 9.C | Claude Code | Generación de la matriz desde el T-12 y el SD3 | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| Anexo 9.D | Claude Code | Juegos de datos y reglas de anonimización | Alto | Ninguno | [[REVISIÓN HUMANA]] |
