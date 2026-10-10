# Anexos del Subdocumento 9

Este archivo contiene el detalle que el Subdocumento 9 resume. El Anexo 9.A lista las métricas de calidad del producto por subcaracterística de ISO/IEC 25010; el Anexo 9.B, las reglas de análisis estático y dinámico con su umbral y su puerta; el Anexo 9.C, la matriz de trazabilidad entre los 645 identificadores del Formulario T-12 y su prueba de verificación; y el Anexo 9.D, la especificación de los datos de prueba. El plan de pruebas y validación está en el Formulario T-13 y el protocolo de aceptación, en el Formulario T-17.

## Anexo 9.A — Umbrales de calidad del producto por subcaracterística

Este anexo desarrolla la Tabla 9.2 del Subdocumento 9. Cada fila es una métrica exigible: su umbral es criterio de salida de la prueba indicada, en el ambiente y en el paquete de la EDT que la ejecutan. Los umbrales provienen de las Bases, del Caso o de un subdocumento anterior; los que propone LafroX se identifican como tales en la columna de fuente.

La Tabla 9.A.1 presenta las 29 métricas.

**Tabla 9.A.1 — Métricas y umbrales por subcaracterística de ISO/IEC 25010. Fuente: elaboración propia a partir de las Bases Administrativas, Art. 24, de las Bases Técnicas Transversales, del Caso 02 y del SD4.**

| N.° | Característica | Subcaracterística | Métrica | Umbral | Fuente del umbral | Método de verificación | Ambiente | Paquete EDT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9A-01 | Funcionalidad | Completitud funcional | Requerimientos ofertados con caso de prueba aprobado | 100 % | Caso cap. 17.1; T-14 1.2.4 | Matriz 9.C (requisito → caso → resultado) | QA | 1.2.4, 3.8.1, 3.9.1 |
| 9A-02 | Funcionalidad | Corrección funcional | Casos de aceptación firmados sin defecto crítico/alto abierto | 100 % / 0 | BTT §20.1; BA Art. 17.3 | Pruebas de aceptación con la Contraparte Técnica | PREPROD | 3.8.2, 3.9.2 |
| 9A-03 | Funcionalidad | Pertinencia funcional | Resultados R18 medidos con su método en el mes comprometido | 16 de 16 | Caso cap. 18; SD3 Tabla 3.A.13 | Protocolo de aceptación T-17 | PROD | 4.2, 4.3 |
| 9A-04 | Desempeño | Comportamiento temporal | p95 confirmación de línea de picking | ≤ 1 s | Caso cap. 15 RT-09.01; SD4 Tabla 31 | Prueba de carga a 1,5× el peak | PREPROD | 3.8.4, 3.9.3 |
| 9A-05 | Desempeño | Comportamiento temporal | p95 registro de entrega en el local | ≤ 2 s | Caso cap. 15 RT-09.01 | Prueba de carga y prueba de terreno | PREPROD | 3.8.4, 3.8.3 |
| 9A-06 | Desempeño | Comportamiento temporal | p95 línea de preventa / consulta de stock y crédito | ≤ 1,5 s / ≤ 2 s | Caso cap. 15 RT-09.01 | Prueba de carga | PREPROD | 3.8.4 |
| 9A-07 | Desempeño | Comportamiento temporal | p95 API consulta / escritura / carga de página | ≤ 500 ms / ≤ 800 ms / ≤ 2 s | BTT §9.1; SD4 Tabla 31 | Prueba de carga + regresión de desempeño semanal | QA/PREPROD | 1.5.2, 3.8.4 |
| 9A-08 | Desempeño | Capacidad | TPS sostenidos sin violar los p95 | ≥ 21,99 TPS (Subdocumento 9, sección 9.2.3) | BTT RT-09.06; SD4 §4.2 | Prueba de carga y estrés hasta el quiebre | PREPROD | 3.8.4, 3.9.3 |
| 9A-09 | Desempeño | Utilización de recursos | CPU/memoria en el peak × 1,5 | ≤ 70 % (supuesto) | SD4 plan de capacidad | Telemetría OpenTelemetry durante la prueba | PREPROD | 3.8.4 |
| 9A-10 | Compatibilidad | Interoperabilidad | Contratos OpenAPI 3.1 / AsyncAPI sin ruptura | 0 contratos rotos | BA Art. 23; SD6 §6.2 | Pruebas de contrato en CI | DEV/QA | 1.5.2 |
| 9A-11 | Compatibilidad | Interoperabilidad | Flujos de las 15 integraciones ejecutados sin error | 15 de 15 | BTT §20.1 (integración) | Pruebas de integración en QA | QA | 3.8.1, 3.9.1 |
| 9A-12 | Compatibilidad | Coexistencia | Regresiones de la Etapa 1 al integrar la Etapa 2 | 0 | BA Art. 17.2 | Regresión completa con E1 en producción | QA/PREPROD | 3.9.1 |
| 9A-13 | Usabilidad | Aprendizaje | Tiempo para registrar 20 líneas sin asistencia | ≤ 2 h, error ≤ 5 % | SD3 Anexos RNF; BTT RT-13.04 | Prueba de usabilidad con usuarios reales | PREPROD | 2.6.2, 2.6.3 |
| 9A-14 | Usabilidad | Accesibilidad | Conformidad WCAG 2.2 AA (axe-core + manual) | 0 incumplimientos A/AA | BTT RT-13.01 | Herramienta automática + revisión manual | QA/PREPROD | 3.8.2, 3.9.2 |
| 9A-15 | Usabilidad | Operabilidad en terreno | Uso con guantes a −22 °C, una mano, objetivos táctiles | ≥ 15×15 mm; 30 min a −22 °C | Caso cap. 15 RT-13.08; SD3 Anexos | Prueba del perfil operacional en cámara | Terreno | 3.8.3 |
| 9A-16 | Fiabilidad | Disponibilidad | Disponibilidad mensual de servicios críticos | ≥ 99,9 %; 0 min en 05:30–07:00 | BTT RT-10.01; Caso RT-10.05 | Medición sobre transacción real (marcha blanca y Operación) | PROD | 4.2, 8.1 |
| 9A-17 | Fiabilidad | Tolerancia a fallos | Operación sin enlace del CD / sin señal del dispositivo | 24 h / 14 h, 0 pérdidas ni duplicados | Caso RT-03.10 | Prueba de desconexión controlada | PREPROD/Terreno | 3.8.3 |
| 9A-18 | Fiabilidad | Recuperabilidad | RTO / RPO en conmutación real | ≤ 4 h / ≤ 15 min | SD4 Tabla 38 | Prueba DR antes del paso y semestral | DR | 3.8.5, 3.9.4, 8.1.3 |
| 9A-19 | Fiabilidad | Recuperabilidad | Sincronización tras reconexión | Dispositivo ≤ 10 min; CD ≤ 2 h | Caso RT-03.13 | Prueba de desconexión controlada | PREPROD | 3.8.3 |
| 9A-20 | Seguridad | Integridad / confidencialidad | Hallazgos críticos o altos abiertos (SAST, SCA, DAST, pentest) | 0 | BTT RT-04.05, RT-11.20; BTT §20.1 | Puertas G2/G4 y pentest por tercero | QA/PREPROD | 1.5.2, 3.8.6, 3.9.5 |
| 9A-21 | Seguridad | Confidencialidad | Datos productivos en ambientes no productivos de prueba | 0 registros sin anonimización verificada; DR se trata como réplica productiva restringida | SD3 Anexos RNF; Ley 21.719 | Escaneo Macie de QA y PREPROD y prueba de reidentificación | QA/PREPROD | 1.5.1 |
| 9A-22 | Seguridad | Responsabilidad | Trazas de auditoría de acceso a datos sensibles | 100 % de consultas registradas | Caso RT-16.09 | Prueba funcional de auditoría | QA | 3.8.2 |
| 9A-23 | Mantenibilidad | Capacidad de prueba | Cobertura lógica de negocio / global | ≥ 70 % / ≥ 80 % | BA Art. 24; SD1; SD6 | Puerta G2 en CI | DEV/CI | 1.5.2 |
| 9A-24 | Mantenibilidad | Modularidad | Dependencias prohibidas entre los 12 módulos | 0 violaciones | BTT RT-02.02; SD4 §4.1 | deptrac en CI | DEV/CI | 1.5.2 |
| 9A-25 | Mantenibilidad | Analizabilidad | Complejidad ciclomática por método / cognitiva | ≤ 10 / ≤ 15 | Supuesto LafroX (Subdocumento 9, sección 9.1.4) | Análisis estático en CI | DEV/CI | 1.5.2 |
| 9A-26 | Mantenibilidad | Modificabilidad | Duplicación / razón de deuda técnica | ≤ 3 % / ≤ 5 % | Supuesto LafroX; BA Art. 24 (deuda) | Análisis estático; registro 8.2.4 | DEV/CI | 1.5.2, 8.2.4 |
| 9A-27 | Portabilidad | Instalabilidad | Mismo artefacto promovido QA → PREPROD → PROD sin recompilar | 100 % de despliegues | BTT RT-04.08 | Promoción por digest de imagen firmada | QA→PROD | 3.8.8, 3.9.7 |
| 9A-28 | Portabilidad | Adaptabilidad | Ambientes reconstruidos desde IaC (Terraform/Ansible) | 100 %; ambiente efímero ≤ 30 min (supuesto) | SD4 §4.2; BTT RT-04.14 | Reconstrucción desde código en QA | QA | 1.5.2 |
| 9A-29 | Portabilidad | Reemplazabilidad | Exportación completa en formato abierto | 100 % de entidades | BA Art. 23 | Prueba de exportación | PREPROD | 3.9.2 |

La tabla reúne 29 métricas: funcionalidad 3, desempeño 6, compatibilidad 3, usabilidad 3, fiabilidad 4, seguridad 3, mantenibilidad 4, portabilidad 3. El desempeño y la fiabilidad concentran más métricas porque son las características de las que depende el despacho en la ventana de 05:30 a 07:00 y la operación sin enlace. Las métricas 9A-09, 9A-25, 9A-26 y 9A-28 usan umbrales propuestos por LafroX; las demás reproducen un valor de las Bases, del Caso o del SD4.

## Anexo 9.B — Catálogo de reglas de análisis estático y dinámico

Este anexo detalla las reglas que ejecutan las puertas G1 a G4 descritas en la sección 9.2.1 del Subdocumento 9. Cada regla tiene una herramienta, un umbral y una puerta; ninguna regla bloqueante admite excepción manual, y ninguna regla de seguridad admite excepción en ninguna puerta. La única excepción es la regla 9B-22, de regresión de desempeño, que el Líder de Calidad puede aceptar con registro de deuda cuando la causa está identificada y no se incumple un umbral p95 (Subdocumento 9, sección 9.2.1).

### 9.B.1 Reglas y umbrales

La Tabla 9.B.1 lista las 24 reglas, con la herramienta en cada lenguaje.

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
| 9B-08 | Complejidad ciclomática máxima por método | PHP / Kotlin / TS | PHPMD · detekt · ESLint complexity | ≤ 10 | G2 | Supuesto LafroX (McCabe) |
| 9B-09 | Complejidad cognitiva máxima por método | PHP / Kotlin / TS | PHPMD · detekt · eslint-plugin-sonarjs | ≤ 15 | G2 | Supuesto LafroX |
| 9B-10 | Violaciones de dependencia entre módulos | PHP / Laravel | deptrac | ≤ 0 | G2 | BTT RT-02.02; SD4 sección 4.1 |
| 9B-11 | Inestabilidad de los módulos núcleo (Ce/(Ca+Ce)) | PHP / Laravel | PhpMetrics | ≤ 0,5 | G2 | Supuesto LafroX (Martin) |
| 9B-12 | Duplicación de código | Todos | PHPCPD · jscpd | ≤ 3 % | G2 | Supuesto LafroX |
| 9B-13 | Razón de deuda técnica (esfuerzo de remediación / desarrollo) | Todos | Registro 8.2.4 + análisis estático | ≤ 5 % | G2 | BA Art. 24 (gestión de deuda); supuesto |
| 9B-14 | Infracciones de estilo / lint | Kotlin / Android | detekt + ktlint | ≤ 0 | G1 | Supuesto LafroX |
| 9B-15 | Errores de lint | Angular / TypeScript | ESLint | ≤ 0 | G1 | Supuesto LafroX |
| 9B-16 | Vulnerabilidades críticas o altas (SAST/SCA) | Todos | GitLab SAST + composer audit / npm audit | ≤ 0 | G2 | BTT RT-04.05 |
| 9B-17 | Secretos detectados en el código | Todos | GitLab Secret Detection | ≤ 0 | G1 | BTT RT-04.05, RT-04.09 |
| 9B-18 | Vulnerabilidades críticas o altas en imágenes | Contenedores | Amazon Inspector / ECR scan | ≤ 0 | G3 | BTT RT-04.05 |
| 9B-19 | Alertas altas de DAST | Portales y API | OWASP ZAP | ≤ 0 | G4 | BTT sección 20.1; SD3 RNF-14.07 |
| 9B-20 | Contratos OpenAPI/AsyncAPI rotos | API | Pruebas de contrato | ≤ 0 | G2 | SD6 sección 6.2 |
| 9B-21 | Pruebas en falla | Todos | Ejecución CI | ≤ 0 | G2 | BTT sección 20.1 |
| 9B-22 | Regresión de p95 respecto de la versión anterior | API | k6 en QA (semanal) | ≤ 10 % | G3 | SD4 sección 4.2.4; supuesto del 10 % |
| 9B-23 | Incumplimientos WCAG 2.2 A o AA confirmados | Portales / app | axe-core + revisión manual | ≤ 0 | G4 | BTT RT-13.01 |
| 9B-24 | Revisores aprobadores por solicitud de fusión | Todos | GitLab (rama protegida) | ≥ 1 | G1 | BTT RT-04.03 |

Las 24 reglas se reparten entre PHP, Kotlin, TypeScript y la plataforma. De ellas, 12 exigen cero hallazgos y las demás fijan una cota numérica. Las reglas de cobertura, SAST, SCA, secretos e imágenes cubren los mínimos del RT-04.05 y del RT-04.11; las de complejidad, duplicación, inestabilidad y deuda son propuestas de LafroX con su fuente en la Tabla 9.B.1.

### 9.B.2 Configuración por lenguaje

La configuración de cada herramienta se versiona en el repositorio de cada componente, de modo que un cambio de regla pasa por revisión por pares como cualquier cambio de código. La Tabla 9.B.2 resume la configuración base.

**Tabla 9.B.2 — Configuración base de las herramientas de análisis. Fuente: elaboración propia.**

| Lenguaje o capa | Herramienta | Configuración base |
| --- | --- | --- |
| PHP 8.5 / Laravel 13 | PHPStan + Larastan | Nivel 8; sin línea base de errores heredados; análisis de los 12 módulos y sus pruebas. |
| PHP 8.5 / Laravel 13 | Laravel Pint | Preajuste laravel; verificación en modo de prueba, sin reescritura en CI. |
| PHP 8.5 / Laravel 13 | PHPMD | Reglas de tamaño y complejidad: CyclomaticComplexity 10, NPathComplexity 200, ExcessiveMethodLength 60 líneas. |
| PHP 8.5 / Laravel 13 | deptrac | Una capa por módulo M1 a M12 más la capa compartida; cada módulo sólo accede a otro por su contrato público (interfaces y eventos). |
| PHP 8.5 / Laravel 13 | PHPUnit con PCOV | Informe Cobertura por paquete; la lógica de negocio son los espacios de nombres Domain y Application de cada módulo. |
| Kotlin / Android | detekt + ktlint | Conjunto por defecto con ComplexMethod 10, CognitiveComplexMethod 15 y LongMethod 60; ktlint estándar. |
| Kotlin / Android | JUnit 5 + Kover | Cobertura sobre los módulos de dominio y sincronización; las vistas se prueban con Espresso. |
| Angular / TypeScript | ESLint + Jest | Reglas recomendadas de Angular y TypeScript, complexity 10, sonarjs/cognitive-complexity 15; cobertura de Jest por proyecto. |
| Todos | GitLab SAST, Secret Detection y auditoría de dependencias | Severidades crítica y alta bloquean; media se registra con plazo de 30 días corridos (SD4, sección 4.2.4.1.4). |
| Contenedores | Amazon Inspector / escaneo de ECR | Bloqueo ante vulnerabilidad crítica o alta en la imagen candidata. |
| Portales y API | OWASP ZAP | Escaneo activo en QA guiado por la definición OpenAPI 3.1; alerta alta bloquea G4. |
| Portales y aplicación | axe-core | Reglas WCAG 2.2 A y AA; cualquier incumplimiento confirmado por herramienta o revisión manual bloquea G4. |
| API | k6 | Escenario de regresión semanal en QA; bloquea G3 si el p95 empeora más de 10 % frente a la versión anterior. |

Con esta configuración, las mismas cotas de complejidad rigen en los tres lenguajes, y la frontera entre módulos se verifica en el código y no sólo en el diagrama del SD4. La deuda que una herramienta detecta y que no bloquea queda en el registro de deuda técnica del paquete 8.2.4, con su estimación de esfuerzo, para el cálculo de la razón de deuda de la regla 9B-13.

## Anexo 9.C — Matriz de trazabilidad entre requisitos y pruebas

Este anexo completa la cadena de trazabilidad de la sección 9.2.5 del Subdocumento 9. Para cada uno de los 645 identificadores del Formulario T-12 indica la prueba que lo verifica, el ambiente, el paquete de la EDT que la ejecuta, el hito en que se acepta y el número de casos estimado. El componente que satisface cada requisito y la sección de la propuesta que lo desarrolla están en el Formulario T-12 y no se repiten aquí.

### 9.C.1 Reglas de construcción

La matriz aplica cuatro reglas. Primera: un requisito funcional o no funcional recibe cinco casos si es de prioridad crítica, tres si es alta y dos si es media, según su prioridad en los Anexos 3.A y 3.B del SD3. Segunda: un requisito técnico transversal recibe un caso de verificación. Tercera: un identificador que el SD3 declara absorbido por otra fila, o alias de ella, se verifica con la prueba de esa fila y no suma casos. Cuarta: un identificador en estado «No cumple» queda sin prueba, para que la brecha sea visible. La prueba de los requisitos no funcionales sigue la verificación prevista en el SD3; la de los requisitos técnicos, el capítulo de las Bases Técnicas Transversales al que pertenecen. El paquete y el hito dependen de la etapa del requisito.

La Tabla 9.C.1 resume la matriz.

**Tabla 9.C.1 — Síntesis de la matriz de trazabilidad. Fuente: elaboración propia a partir del Formulario T-12 y del SD3, Anexos 3.A y 3.B.**

| Grupo | Identificadores | Con prueba propia | Sin prueba propia | Casos estimados |
| --- | --- | --- | --- | --- |
| RF | 181 | 175 | 6 | 544 |
| RNF | 90 | 84 | 6 | 302 |
| RT | 374 | 346 | 28 | 346 |
| Contratos de las 15 integraciones | — | — | — | 90 |
| **Total** | **645** | **605** | **40** | **1.282** |

La matriz asigna prueba propia a 605 de los 645 identificadores. Los 40 restantes son 31 en estado «No cumple» y 9 absorbidos por otra fila. Con los 90 casos de contrato de las integraciones, el catálogo suma 1.282 casos, la cifra que usa la sección 9.2.3 del Subdocumento 9.

### 9.C.2 Matriz

La Tabla 9.C.2 presenta la matriz completa, en el orden del Formulario T-12.

**Tabla 9.C.2 — Matriz de trazabilidad entre requisitos y pruebas. Fuente: elaboración propia a partir del Formulario T-12, del SD3, Anexos 3.A y 3.B, y del Formulario T-14.**

| ID | Estado T-12 | Prueba de verificación | Ambiente | Paquete EDT | Hito de aceptación | Casos |
| --- | --- | --- | --- | --- | --- | --- |
| RF-01.01 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 |
| RF-01.02 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 |
| RF-01.03 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 |
| RF-01.04 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-01.05 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-01.06 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-01.07 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 |
| RF-01.08 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 |
| RF-01.09 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 |
| RF-01.10 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 |
| RF-01.11 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 |
| RF-02.01 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-02.02 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-02.03 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-02.04 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-02.05 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-02.06 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 |
| RF-02.07 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-02.08 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-02.09 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-02.10 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-02.11 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-03.01 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 |
| RF-03.02 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 |
| RF-03.03 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-03.04 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 |
| RF-03.05 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 |
| RF-03.06 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-03.07 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-03.08 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 |
| RF-03.09 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 |
| RF-03.10 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-03.11 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 |
| RF-03.12 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 |
| RF-03.13 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 |
| RF-03.14 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-03.15 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 |
| RF-03.16 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 |
| RF-04.01 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-04.02 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 |
| RF-04.03 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-04.04 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-04.05 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-04.06 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 |
| RF-04.07 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-04.08 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 |
| RF-05.01 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-05.02 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-05.03 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-05.04 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-05.05 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-05.06 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-05.07 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-06.01 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-06.02 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 |
| RF-06.03 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 |
| RF-06.04 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 |
| RF-06.05 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 |
| RF-06.06 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-06.07 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 |
| RF-06.08 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-06.09 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-06.10 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-06.11 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 |
| RF-06.12 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 |
| RF-06.13 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 |
| RF-06.14 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-07.01 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-07.02 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-07.03 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-07.04 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-07.05 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-07.06 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 |
| RF-07.07 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 |
| RF-07.08 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-07.09 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-07.10 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-07.11 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RF-08.01 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 |
| RF-08.02 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 |
| RF-08.03 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-08.04 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-08.05 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-08.06 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-08.07 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 |
| RF-09.01 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 |
| RF-09.02 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 |
| RF-09.03 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 |
| RF-09.04 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 |
| RF-09.05 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 |
| RF-09.06 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 |
| RF-09.07 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 |
| RF-09.08 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 |
| RF-09.09 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 |
| RF-09.10 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 |
| RF-10.01 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 |
| RF-10.02 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 |
| RF-10.03 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 |
| RF-11.01 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 |
| RF-11.02 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 |
| RF-11.03 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-11.04 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-11.05 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-11.06 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-11.07 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-11.08 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 |
| RF-12.01 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 |
| RF-12.02 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 |
| RF-12.03 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 |
| RF-12.04 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 |
| RF-12.05 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 |
| RF-12.06 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 |
| RF-12.07 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 |
| RF-12.08 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 |
| RF-12.09 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 |
| RF-12.10 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 |
| RF-12.11 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 |
| RF-12.12 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 |
| RF-12.13 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 3 |
| RF-12.14 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 |
| RF-12.15 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 |
| RF-12.16 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 |
| RF-12.17 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 |
| RF-12.18 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 |
| RF-12.19 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 |
| RF-12.20 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 |
| RF-12.21 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 |
| RF-12.22 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 |
| RF-12.23 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 |
| RF-12.24 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 |
| RF-12.25 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 |
| RF-12.26 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 |
| RF-12.27 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 |
| RF-12.28 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 |
| RF-12.29 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 |
| RF-12.30 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 2 |
| RF-13.01 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-13.02 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-13.03 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-13.04 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-14.01 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 5 |
| RF-14.02 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-14.03 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-14.04 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.9.1 · 3.9.2 | H9 · H10 | 5 |
| RF-14.05 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 3 |
| RF-14.06 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 2 |
| RF-14.01-BTT | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-14.02-BTT | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-14.03-BTT | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-14.04-BTT | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-14.05-BTT | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-15.01 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-15.02 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-15.03 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-15.04 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-15.05 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-16.01 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-16.02 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-16.03 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-16.04 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-17.01 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-17.02 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-17.03 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-17.04 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-17.05 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-17.06 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-17.07 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-17.08 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-17.09 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 2 |
| RF-17.10 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-17.11 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-17.12 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-17.13 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 2 |
| RF-18.01 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-18.02 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 2 |
| RF-18.03 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.1 · 3.9.2 | H4 · H5 · H9 · H10 | 3 |
| RF-19.01 | Cumple | Se verifica con RT-11.03 | — | — | — | 0 |
| RF-19.02 | Cumple | Se verifica con RT-11.05 | — | — | — | 0 |
| RF-19.03 | Cumple parcialmente | Se verifica con RT-11.13 | — | — | — | 0 |
| RF-19.04 | Cumple | Se verifica con RT-11.18 | — | — | — | 0 |
| RF-19.05 | Cumple parcialmente | Se verifica con RT-11.19 | — | — | — | 0 |
| RNF-01.01 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 | H5 | 3 |
| RNF-01.02 | Cumple | Restauración de muestra y política de retención | DR | 3.8.5 | H5 | 5 |
| RNF-01.03 | Cumple | Perfil operacional: sin señal y sin enlace | Terreno · PREPROD | 3.8.3 | H5 | 5 |
| RNF-02.01 | Cumple | Perfil operacional: sin señal y sin enlace | Terreno · PREPROD | 3.8.3 | H5 | 5 |
| RNF-03.01 | Cumple | Perfil operacional: sin señal y sin enlace | Terreno · PREPROD | 3.8.3 | H5 | 3 |
| RNF-03.02 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 | H5 | 3 |
| RNF-03.03 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 | H5 | 3 |
| RNF-04.01 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 | H7 | 2 |
| RNF-05.01 | Cumple | Perfil operacional: sin señal y sin enlace | Terreno · PREPROD | 3.8.3 | H5 | 3 |
| RNF-05.02 | Cumple parcialmente | Usabilidad en terreno con usuarios | Terreno | 3.8.3 | H5 | 5 |
| RNF-05.03 | Cumple parcialmente | Usabilidad en terreno con usuarios | Terreno | 3.8.3 | H5 | 5 |
| RNF-06.01 | Cumple | Perfil operacional: sin señal y sin enlace | Terreno · PREPROD | 3.8.3 | H5 | 2 |
| RNF-06.02 | Cumple | Se verifica con RT-03.11 | — | — | — | 0 |
| RNF-06.03 | Cumple | Se verifica con RNF-02.01 | — | — | — | 0 |
| RNF-07.01 | Cumple | Perfil operacional: sin señal y sin enlace | Terreno · PREPROD | 3.8.3 | H5 | 5 |
| RNF-07.02 | Cumple | Revisión de configuración, SAST/DAST y pentest | QA · PREPROD | 3.8.6 | H5 | 5 |
| RNF-08.01 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 | H5 | 3 |
| RNF-08.02 | Cumple | Restauración de muestra y política de retención | DR | 3.8.5 | H5 | 3 |
| RNF-09.01 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 | H5 | 5 |
| RNF-09.02 | Cumple | Restauración de muestra y política de retención | DR | 3.8.5 | H5 | 5 |
| RNF-09.03 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 | H7 | 3 |
| RNF-09.04 | Cumple | Perfil operacional: sin señal y sin enlace | Terreno · PREPROD | 3.8.3 | H5 | 5 |
| RNF-09.05 | Cumple parcialmente | Perfil operacional: registro térmico | Terreno | 3.8.3 | H5 | 5 |
| RNF-11.01 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 | H5 | 3 |
| RNF-11.02 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 | H7 | 3 |
| RNF-11.03 | Cumple | Se verifica con RF-11.07 | — | — | — | 0 |
| RNF-11.04 | Cumple | Se verifica con RT-05.29 | — | — | — | 0 |
| RNF-12.01 | Cumple | Prueba funcional en marcha blanca | PROD | 4.3 | H12 | 5 |
| RNF-12.02 | Cumple | Prueba funcional en marcha blanca | PROD | 4.3 | H12 | 3 |
| RNF-12.03 | Cumple parcialmente | Prueba funcional en marcha blanca | PROD | 4.3 | H12 | 3 |
| RNF-13.01 | Cumple | Perfil operacional: sin señal y sin enlace | Terreno · PREPROD | 3.8.3 · 3.9.2 | H5 · H10 | 5 |
| RNF-13.02 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 5 |
| RNF-13.03 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-13.04 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-13.05 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-13.06 | Cumple parcialmente | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-13.07 | Cumple | Recuperación ante desastres con conmutación real | DR | 3.8.5 · 3.9.4 | H5 · H10 | 3 |
| RNF-13.08 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-13.09 | Cumple parcialmente | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-14.01 | Cumple parcialmente | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 5 |
| RNF-14.02 | Cumple | Revisión de configuración, SAST/DAST y pentest | QA · PREPROD | 3.8.6 · 3.9.5 | H5 · H10 | 5 |
| RNF-14.03 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-14.04 | Cumple | Revisión de configuración, SAST/DAST y pentest | QA · PREPROD | 3.8.6 · 3.9.5 | H5 · H10 | 3 |
| RNF-14.05 | Cumple parcialmente | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 3 |
| RNF-14.06 | Cumple parcialmente | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-14.07 | Cumple | SAST en G2 y DAST en G4 | QA | 1.5.2 · 3.8.6 | H4 · H5 | 3 |
| RNF-14.08 | Cumple parcialmente | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-14.09 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-14.10 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-14.11 | Cumple | Revisión de configuración, SAST/DAST y pentest | QA · PREPROD | 3.8.6 | H5 | 5 |
| RNF-14.12 | Cumple | Revisión de configuración, SAST/DAST y pentest | QA · PREPROD | 3.8.6 | H5 | 3 |
| RNF-15.01 | Cumple | Revisión de configuración, SAST/DAST y pentest | QA · PREPROD | 3.8.6 · 3.9.5 | H5 · H10 | 5 |
| RNF-15.02 | Cumple | Revisión de configuración, SAST/DAST y pentest | QA · PREPROD | 3.8.6 · 3.9.5 | H5 · H10 | 5 |
| RNF-15.03 | Cumple | Restauración de muestra y política de retención | DR | 3.8.5 · 3.9.4 | H5 · H10 | 3 |
| RNF-16.01 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 3 |
| RNF-16.02 | Cumple parcialmente | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-16.03 | Cumple parcialmente | Revisión de configuración, SAST/DAST y pentest | QA · PREPROD | 3.8.6 · 3.9.5 | H5 · H10 | 5 |
| RNF-17.01 | Cumple | Restauración de muestra y política de retención | DR | 3.8.5 · 3.9.4 | H5 · H10 | 3 |
| RNF-17.02 | Cumple parcialmente | Revisión de configuración, SAST/DAST y pentest | QA · PREPROD | 3.8.6 · 3.9.5 | H5 · H10 | 3 |
| RNF-17.03 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-19.01 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-19.02 | Cumple parcialmente | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-19.03 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-19.04 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 3 |
| RNF-20.01 | Cumple | Recuperación ante desastres con conmutación real | DR | 3.8.5 · 3.9.4 | H5 · H10 | 5 |
| RNF-20.02 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 5 |
| RNF-20.03 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 5 |
| RNF-20.04 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 3 |
| RNF-20.05 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-20.06 | Cumple parcialmente | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 5 |
| RNF-20.07 | Cumple | Recuperación ante desastres con conmutación real | DR | 3.8.5 · 3.9.4 | H5 · H10 | 5 |
| RNF-21.01 | Cumple parcialmente | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 5 |
| RNF-21.02 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RNF-21.03 | Cumple parcialmente | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 3 |
| RNF-21.04 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-21.05 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-21.06 | Cumple parcialmente | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-21.07 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RNF-21.08 | Cumple parcialmente | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-21.09 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-22.01 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-22.02 | Cumple parcialmente | Recuperación ante desastres con conmutación real | DR | 3.8.5 · 3.9.4 | H5 · H10 | 3 |
| RNF-22.03 | Cumple parcialmente | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-22.04 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-22.05 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-22.06 | Cumple | Prueba funcional en marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 3 |
| RNF-23.01 | Cumple parcialmente | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-23.02 | Cumple parcialmente | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-23.03 | Cumple | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RNF-23.04 | Cumple parcialmente | Inspección del expediente de certificación | — | 3.8.7 · 3.9.6 | H5 · H10 | 3 |
| RT-02.01 | Cumple | Revisión de arquitectura y prueba de integración | QA | 2.1 · 3.8.1 | H2 · H4 | 1 |
| RT-02.02 | Cumple | Revisión de arquitectura y prueba de integración | QA | 2.1 · 3.8.1 | H2 · H4 | 1 |
| RT-02.03 | Cumple | Revisión de arquitectura y prueba de integración | QA | 2.1 · 3.8.1 | H2 · H4 | 1 |
| RT-02.04 | Cumple | Revisión de arquitectura y prueba de integración | QA | 2.1 · 3.8.1 | H2 · H4 | 1 |
| RT-02.05 | Cumple | Revisión de arquitectura y prueba de integración | QA | 2.1 · 3.8.1 | H2 · H4 | 1 |
| RT-02.06 | Cumple | Revisión de arquitectura y prueba de integración | QA | 2.1 · 3.8.1 | H2 · H4 | 1 |
| RT-02.07 | Cumple | Revisión de arquitectura y prueba de integración | QA | 2.1 · 3.8.1 | H2 · H4 | 1 |
| RT-02.08 | Cumple | Revisión de arquitectura y prueba de integración | QA | 2.1 · 3.8.1 | H2 · H4 | 1 |
| RT-02.09 | Cumple | Revisión de arquitectura y prueba de integración | QA | 2.1 · 3.8.1 | H2 · H4 | 1 |
| RT-02.10 | Cumple parcialmente | Revisión de arquitectura y prueba de integración | QA | 2.1 · 3.8.1 | H2 · H4 | 1 |
| RT-02.11 | Cumple | Revisión de arquitectura y prueba de integración | QA | 2.1 · 3.8.1 | H2 · H4 | 1 |
| RT-02.12 | Cumple parcialmente | Revisión de arquitectura y prueba de integración | QA | 2.1 · 3.8.1 | H2 · H4 | 1 |
| RT-02.13 | Cumple | Revisión de arquitectura y prueba de integración | QA | 2.1 · 3.8.1 | H2 · H4 | 1 |
| RT-02.14 | Cumple | Revisión de arquitectura y prueba de integración | QA | 2.1 · 3.8.1 | H2 · H4 | 1 |
| RT-03.01 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.02 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.03 | Cumple parcialmente | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.04 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.05 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.06 | Cumple parcialmente | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.07 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.08 | Cumple parcialmente | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.09 | Cumple parcialmente | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.10 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.11 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.12 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.13 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.14 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.15 | Cumple parcialmente | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.16 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.17 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.18 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.19 | Cumple parcialmente | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.20 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.21 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.22 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.23 | Cumple | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
| RT-03.24 | Cumple parcialmente | Corte de enlace y resiliencia del modelo híbrido | PREPROD | 3.8.3 · 3.8.4 | H5 | 1 |
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
| RT-04.13 | Cumple parcialmente | Puertas G1–G5 del pipeline | DEV · QA | 1.5.2 | H3 · H4 | 1 |
| RT-04.14 | Cumple parcialmente | Puertas G1–G5 del pipeline | DEV · QA | 1.5.2 | H3 · H4 | 1 |
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
| RT-05.25 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 |
| RT-05.26 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 |
| RT-05.27 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 |
| RT-05.28 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 |
| RT-05.29 | Cumple | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 |
| RT-05.30 | Cumple parcialmente | Integración, contrato y ensayos de migración | QA · PREPROD | 3.7 · 3.8.1 | H4 · H5 | 1 |
| RT-06.01 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.02 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.03 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.04 | Cumple parcialmente | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.05 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.06 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.07 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.08 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.09 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.10 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.11 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.12 | Cumple parcialmente | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.13 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.14 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.15 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.16 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.17 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.18 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.19 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.20 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.21 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.22 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.23 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.24 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.25 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.26 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.27 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.28 | Cumple parcialmente | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.29 | Cumple parcialmente | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.30 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.31 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.32 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.33 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-06.34 | Cumple | Inspección y recepción técnica del recinto | Sitio Talca | Cuentas 5 y 6 | H3 | 1 |
| RT-07.01 | Cumple parcialmente | Recuperación ante desastres y restauración | DR | 3.8.5 · 3.9.4 · 8.1.3 · 8.1.6 | H5 · H10 · semestral | 1 |
| RT-07.02 | Cumple | Recuperación ante desastres y restauración | DR | 3.8.5 · 3.9.4 · 8.1.3 · 8.1.6 | H5 · H10 · semestral | 1 |
| RT-07.03 | Cumple | Recuperación ante desastres y restauración | DR | 3.8.5 · 3.9.4 · 8.1.3 · 8.1.6 | H5 · H10 · semestral | 1 |
| RT-07.04 | Cumple parcialmente | Recuperación ante desastres y restauración | DR | 3.8.5 · 3.9.4 · 8.1.3 · 8.1.6 | H5 · H10 · semestral | 1 |
| RT-07.05 | Cumple | Recuperación ante desastres y restauración | DR | 3.8.5 · 3.9.4 · 8.1.3 · 8.1.6 | H5 · H10 · semestral | 1 |
| RT-07.06 | Cumple | Recuperación ante desastres y restauración | DR | 3.8.5 · 3.9.4 · 8.1.3 · 8.1.6 | H5 · H10 · semestral | 1 |
| RT-07.07 | Cumple | Recuperación ante desastres y restauración | DR | 3.8.5 · 3.9.4 · 8.1.3 · 8.1.6 | H5 · H10 · semestral | 1 |
| RT-07.08 | Cumple parcialmente | Recuperación ante desastres y restauración | DR | 3.8.5 · 3.9.4 · 8.1.3 · 8.1.6 | H5 · H10 · semestral | 1 |
| RT-07.09 | Cumple | Recuperación ante desastres y restauración | DR | 3.8.5 · 3.9.4 · 8.1.3 · 8.1.6 | H5 · H10 · semestral | 1 |
| RT-07.10 | Cumple | Recuperación ante desastres y restauración | DR | 3.8.5 · 3.9.4 · 8.1.3 · 8.1.6 | H5 · H10 · semestral | 1 |
| RT-07.11 | Cumple | Recuperación ante desastres y restauración | DR | 3.8.5 · 3.9.4 · 8.1.3 · 8.1.6 | H5 · H10 · semestral | 1 |
| RT-07.12 | Cumple | Recuperación ante desastres y restauración | DR | 3.8.5 · 3.9.4 · 8.1.3 · 8.1.6 | H5 · H10 · semestral | 1 |
| RT-07.13 | Cumple | Recuperación ante desastres y restauración | DR | 3.8.5 · 3.9.4 · 8.1.3 · 8.1.6 | H5 · H10 · semestral | 1 |
| RT-07.14 | Cumple | Recuperación ante desastres y restauración | DR | 3.8.5 · 3.9.4 · 8.1.3 · 8.1.6 | H5 · H10 · semestral | 1 |
| RT-08.01 | Cumple parcialmente | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 |
| RT-08.02 | Cumple parcialmente | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 |
| RT-08.03 | Cumple | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 |
| RT-08.04 | Cumple parcialmente | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 |
| RT-08.05 | Cumple parcialmente | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 |
| RT-08.06 | Cumple | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 |
| RT-08.07 | Cumple | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 |
| RT-08.08 | Cumple | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 |
| RT-08.09 | Cumple parcialmente | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 |
| RT-08.10 | Cumple parcialmente | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 |
| RT-08.11 | Cumple parcialmente | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 |
| RT-08.12 | Cumple parcialmente | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 |
| RT-08.13 | Cumple | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 |
| RT-08.14 | Cumple parcialmente | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 |
| RT-08.15 | Cumple | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 |
| RT-08.16 | Cumple | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 |
| RT-08.17 | Cumple | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 |
| RT-08.18 | Cumple | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 |
| RT-08.19 | Cumple | Recepción técnica y prueba de dispositivos | Terreno | 3.8.3 | H5 | 1 |
| RT-09.01 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 1 |
| RT-09.02 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 1 |
| RT-09.03 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 1 |
| RT-09.04 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 1 |
| RT-09.05 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 1 |
| RT-09.06 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 1 |
| RT-09.07 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 1 |
| RT-09.08 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 1 |
| RT-09.09 | Cumple parcialmente | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 1 |
| RT-09.10 | Cumple | Carga a 1,5× el peak y estrés | PREPROD | 3.8.4 · 3.9.3 | H5 · H10 | 1 |
| RT-10.01 | Cumple | Resiliencia por inyección de fallas | PREPROD | 3.8.4 · 3.9.3 · 8.2.2 | H5 · H10 · semestral | 1 |
| RT-10.02 | Cumple | Resiliencia por inyección de fallas | PREPROD | 3.8.4 · 3.9.3 · 8.2.2 | H5 · H10 · semestral | 1 |
| RT-10.03 | Cumple | Resiliencia por inyección de fallas | PREPROD | 3.8.4 · 3.9.3 · 8.2.2 | H5 · H10 · semestral | 1 |
| RT-10.04 | Cumple | Resiliencia por inyección de fallas | PREPROD | 3.8.4 · 3.9.3 · 8.2.2 | H5 · H10 · semestral | 1 |
| RT-10.05 | Cumple | Resiliencia por inyección de fallas | PREPROD | 3.8.4 · 3.9.3 · 8.2.2 | H5 · H10 · semestral | 1 |
| RT-10.06 | Cumple | Resiliencia por inyección de fallas | PREPROD | 3.8.4 · 3.9.3 · 8.2.2 | H5 · H10 · semestral | 1 |
| RT-10.07 | Cumple | Resiliencia por inyección de fallas | PREPROD | 3.8.4 · 3.9.3 · 8.2.2 | H5 · H10 · semestral | 1 |
| RT-10.08 | Cumple | Resiliencia por inyección de fallas | PREPROD | 3.8.4 · 3.9.3 · 8.2.2 | H5 · H10 · semestral | 1 |
| RT-10.09 | Cumple | Resiliencia por inyección de fallas | PREPROD | 3.8.4 · 3.9.3 · 8.2.2 | H5 · H10 · semestral | 1 |
| RT-11.01 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 |
| RT-11.02 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 |
| RT-11.03 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 |
| RT-11.04 | Cumple parcialmente | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 |
| RT-11.05 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 |
| RT-11.06 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 |
| RT-11.07 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 |
| RT-11.08 | Cumple parcialmente | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 |
| RT-11.09 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 |
| RT-11.10 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 |
| RT-11.11 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 |
| RT-11.12 | Cumple parcialmente | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 |
| RT-11.13 | Cumple parcialmente | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 |
| RT-11.14 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 |
| RT-11.15 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 |
| RT-11.16 | Cumple parcialmente | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 |
| RT-11.17 | Cumple parcialmente | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 |
| RT-11.18 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 |
| RT-11.19 | Cumple parcialmente | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 |
| RT-11.20 | Cumple parcialmente | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 |
| RT-11.21 | Cumple parcialmente | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 |
| RT-11.22 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 |
| RT-11.23 | Cumple parcialmente | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 |
| RT-11.24 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 |
| RT-11.25 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 |
| RT-11.26 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 |
| RT-11.27 | Cumple parcialmente | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 |
| RT-11.28 | Cumple | SAST, SCA, DAST y prueba de intrusión | QA · PREPROD | 1.5.2 · 3.8.6 · 3.9.5 · 8.2.2 | H5 · H10 · anual | 1 |
| RT-12.01 | Cumple parcialmente | Prueba funcional de identidad y acceso | QA | 3.8.1 · 3.8.6 | H4 · H5 | 1 |
| RT-12.02 | Cumple | Prueba funcional de identidad y acceso | QA | 3.8.1 · 3.8.6 | H4 · H5 | 1 |
| RT-12.03 | Cumple | Prueba funcional de identidad y acceso | QA | 3.8.1 · 3.8.6 | H4 · H5 | 1 |
| RT-12.04 | Cumple | Prueba funcional de identidad y acceso | QA | 3.8.1 · 3.8.6 | H4 · H5 | 1 |
| RT-12.05 | Cumple | Prueba funcional de identidad y acceso | QA | 3.8.1 · 3.8.6 | H4 · H5 | 1 |
| RT-12.06 | Cumple | Prueba funcional de identidad y acceso | QA | 3.8.1 · 3.8.6 | H4 · H5 | 1 |
| RT-12.07 | Cumple | Prueba funcional de identidad y acceso | QA | 3.8.1 · 3.8.6 | H4 · H5 | 1 |
| RT-12.08 | Cumple | Prueba funcional de identidad y acceso | QA | 3.8.1 · 3.8.6 | H4 · H5 | 1 |
| RT-12.09 | Cumple | Prueba funcional de identidad y acceso | QA | 3.8.1 · 3.8.6 | H4 · H5 | 1 |
| RT-12.10 | Cumple parcialmente | Prueba funcional de identidad y acceso | QA | 3.8.1 · 3.8.6 | H4 · H5 | 1 |
| RT-12.11 | Cumple parcialmente | Prueba funcional de identidad y acceso | QA | 3.8.1 · 3.8.6 | H4 · H5 | 1 |
| RT-12.12 | Cumple parcialmente | Prueba funcional de identidad y acceso | QA | 3.8.1 · 3.8.6 | H4 · H5 | 1 |
| RT-12.13 | Cumple | Prueba funcional de identidad y acceso | QA | 3.8.1 · 3.8.6 | H4 · H5 | 1 |
| RT-13.01 | Cumple parcialmente | Accesibilidad WCAG 2.2 AA y usabilidad | QA · PREPROD · Terreno | 2.6.2 · 3.8.2 · 3.9.2 | H5 · H10 | 1 |
| RT-13.02 | Cumple | Accesibilidad WCAG 2.2 AA y usabilidad | QA · PREPROD · Terreno | 2.6.2 · 3.8.2 · 3.9.2 | H5 · H10 | 1 |
| RT-13.03 | Cumple | Accesibilidad WCAG 2.2 AA y usabilidad | QA · PREPROD · Terreno | 2.6.2 · 3.8.2 · 3.9.2 | H5 · H10 | 1 |
| RT-13.04 | Cumple parcialmente | Accesibilidad WCAG 2.2 AA y usabilidad | QA · PREPROD · Terreno | 2.6.2 · 3.8.2 · 3.9.2 | H5 · H10 | 1 |
| RT-13.05 | Cumple | Accesibilidad WCAG 2.2 AA y usabilidad | QA · PREPROD · Terreno | 2.6.2 · 3.8.2 · 3.9.2 | H5 · H10 | 1 |
| RT-13.06 | Cumple parcialmente | Accesibilidad WCAG 2.2 AA y usabilidad | QA · PREPROD · Terreno | 2.6.2 · 3.8.2 · 3.9.2 | H5 · H10 | 1 |
| RT-13.07 | Cumple parcialmente | Accesibilidad WCAG 2.2 AA y usabilidad | QA · PREPROD · Terreno | 2.6.2 · 3.8.2 · 3.9.2 | H5 · H10 | 1 |
| RT-13.08 | Cumple parcialmente | Accesibilidad WCAG 2.2 AA y usabilidad | QA · PREPROD · Terreno | 2.6.2 · 3.8.2 · 3.9.2 | H5 · H10 | 1 |
| RT-13.09 | Cumple | Accesibilidad WCAG 2.2 AA y usabilidad | QA · PREPROD · Terreno | 2.6.2 · 3.8.2 · 3.9.2 | H5 · H10 | 1 |
| RT-13.10 | Cumple | Accesibilidad WCAG 2.2 AA y usabilidad | QA · PREPROD · Terreno | 2.6.2 · 3.8.2 · 3.9.2 | H5 · H10 | 1 |
| RT-13.11 | Cumple | Accesibilidad WCAG 2.2 AA y usabilidad | QA · PREPROD · Terreno | 2.6.2 · 3.8.2 · 3.9.2 | H5 · H10 | 1 |
| RT-13.12 | Cumple | Accesibilidad WCAG 2.2 AA y usabilidad | QA · PREPROD · Terreno | 2.6.2 · 3.8.2 · 3.9.2 | H5 · H10 | 1 |
| RT-14.01 | Cumple | Prueba de observabilidad y medición en marcha blanca | PREPROD · PROD | 3.8.4 · 4.2 | H5 · H7 | 1 |
| RT-14.02 | Cumple parcialmente | Prueba de observabilidad y medición en marcha blanca | PREPROD · PROD | 3.8.4 · 4.2 | H5 · H7 | 1 |
| RT-14.03 | Cumple | Prueba de observabilidad y medición en marcha blanca | PREPROD · PROD | 3.8.4 · 4.2 | H5 · H7 | 1 |
| RT-14.04 | Cumple parcialmente | Prueba de observabilidad y medición en marcha blanca | PREPROD · PROD | 3.8.4 · 4.2 | H5 · H7 | 1 |
| RT-14.05 | Cumple parcialmente | Prueba de observabilidad y medición en marcha blanca | PREPROD · PROD | 3.8.4 · 4.2 | H5 · H7 | 1 |
| RT-14.06 | Cumple parcialmente | Prueba de observabilidad y medición en marcha blanca | PREPROD · PROD | 3.8.4 · 4.2 | H5 · H7 | 1 |
| RT-14.07 | Cumple parcialmente | Prueba de observabilidad y medición en marcha blanca | PREPROD · PROD | 3.8.4 · 4.2 | H5 · H7 | 1 |
| RT-14.08 | Cumple parcialmente | Prueba de observabilidad y medición en marcha blanca | PREPROD · PROD | 3.8.4 · 4.2 | H5 · H7 | 1 |
| RT-14.09 | Cumple | Prueba de observabilidad y medición en marcha blanca | PREPROD · PROD | 3.8.4 · 4.2 | H5 · H7 | 1 |
| RT-15.01 | Cumple | Inspección documental y medición | — | 3.8.7 | H5 | 1 |
| RT-15.02 | Cumple parcialmente | Inspección documental y medición | — | 3.8.7 | H5 | 1 |
| RT-15.03 | Cumple parcialmente | Inspección documental y medición | — | 3.8.7 | H5 | 1 |
| RT-15.04 | Cumple parcialmente | Inspección documental y medición | — | 3.8.7 | H5 | 1 |
| RT-15.05 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-15.06 | Cumple | Inspección documental y medición | — | 3.8.7 | H5 | 1 |
| RT-15.07 | Cumple parcialmente | Inspección documental y medición | — | 3.8.7 | H5 | 1 |
| RT-15.08 | Cumple parcialmente | Inspección documental y medición | — | 3.8.7 | H5 | 1 |
| RT-15.09 | Cumple parcialmente | Inspección documental y medición | — | 3.8.7 | H5 | 1 |
| RT-16.01 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.02 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.03 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.04 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.05 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.06 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.07 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.08 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.09 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.10 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.11 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.12 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.13 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.14 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.15 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.16 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.17 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.18 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.19 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.20 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.21 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.22 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.23 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.24 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.25 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.26 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-16.27 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.28 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.29 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.30 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.31 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.32 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.33 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-16.34 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 · 3.9.2 | H4 · H5 · H10 | 1 |
| RT-17.01 | Cumple | Perfil operacional móvil | Terreno | 3.8.3 | H5 | 1 |
| RT-17.02 | Cumple parcialmente | Perfil operacional móvil | Terreno | 3.8.3 | H5 | 1 |
| RT-17.03 | Cumple parcialmente | Perfil operacional móvil | Terreno | 3.8.3 | H5 | 1 |
| RT-17.04 | Cumple parcialmente | Perfil operacional móvil | Terreno | 3.8.3 | H5 | 1 |
| RT-17.05 | Cumple | Perfil operacional móvil | Terreno | 3.8.3 | H5 | 1 |
| RT-17.06 | Cumple | Perfil operacional móvil | Terreno | 3.8.3 | H5 | 1 |
| RT-17.07 | Cumple parcialmente | Perfil operacional móvil | Terreno | 3.8.3 | H5 | 1 |
| RT-17.08 | Cumple | Perfil operacional móvil | Terreno | 3.8.3 | H5 | 1 |
| RT-18.01 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 1 |
| RT-18.02 | Cumple parcialmente | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 1 |
| RT-18.03 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 1 |
| RT-18.04 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 1 |
| RT-18.05 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 1 |
| RT-18.06 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 1 |
| RT-18.07 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 1 |
| RT-18.08 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 1 |
| RT-18.09 | Cumple | Sistema y aceptación de usuario | QA · PREPROD | 3.8.1 · 3.8.2 | H4 · H5 | 1 |
| RT-18.10 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-19.01 | Cumple | Auditoría de gobierno: actas, informe y tablero | — | Cuenta 1 | H1 · mensual | 1 |
| RT-19.02 | Cumple parcialmente | Auditoría de gobierno: actas, informe y tablero | — | Cuenta 1 | H1 · mensual | 1 |
| RT-19.03 | Cumple | Auditoría de gobierno: actas, informe y tablero | — | Cuenta 1 | H1 · mensual | 1 |
| RT-19.04 | Cumple | Auditoría de gobierno: actas, informe y tablero | — | Cuenta 1 | H1 · mensual | 1 |
| RT-19.05 | Cumple | Auditoría de gobierno: actas, informe y tablero | — | Cuenta 1 | H1 · mensual | 1 |
| RT-19.06 | Cumple parcialmente | Auditoría de gobierno: actas, informe y tablero | — | Cuenta 1 | H1 · mensual | 1 |
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
| RT-20.07 | Cumple parcialmente | Aceptación y cierre de marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 1 |
| RT-20.08 | Cumple parcialmente | Aceptación y cierre de marcha blanca | PROD | 4.2 · 4.3 | H7 · H12 | 1 |
| RT-21.01 | Cumple parcialmente | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.02 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-21.03 | Cumple parcialmente | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.04 | Cumple | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.05 | Cumple | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.06 | Cumple parcialmente | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.07 | Cumple | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.08 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-21.09 | Cumple parcialmente | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.10 | Cumple parcialmente | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.11 | Cumple | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.12 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-21.13 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-21.14 | Cumple | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.15 | Cumple parcialmente | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.16 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-21.17 | Cumple parcialmente | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.18 | Cumple parcialmente | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.19 | Cumple parcialmente | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.20 | Cumple | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.21 | Cumple parcialmente | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-21.22 | Cumple | Medición mensual de niveles de servicio | PROD | Cuentas 8.1 y 8.2 | Mensual | 1 |
| RT-22.01 | Cumple | Certificación de usuarios | PREPROD · PROD | 7.3.1 · 7.3.2 | H6 · H11 | 1 |
| RT-22.02 | Cumple | Certificación de usuarios | PREPROD · PROD | 7.3.1 · 7.3.2 | H6 · H11 | 1 |
| RT-22.03 | Cumple parcialmente | Certificación de usuarios | PREPROD · PROD | 7.3.1 · 7.3.2 | H6 · H11 | 1 |
| RT-22.04 | Cumple parcialmente | Certificación de usuarios | PREPROD · PROD | 7.3.1 · 7.3.2 | H6 · H11 | 1 |
| RT-22.05 | Cumple | Certificación de usuarios | PREPROD · PROD | 7.3.1 · 7.3.2 | H6 · H11 | 1 |
| RT-22.06 | Cumple | Certificación de usuarios | PREPROD · PROD | 7.3.1 · 7.3.2 | H6 · H11 | 1 |
| RT-22.07 | Cumple | Certificación de usuarios | PREPROD · PROD | 7.3.1 · 7.3.2 | H6 · H11 | 1 |
| RT-22.08 | Cumple | Certificación de usuarios | PREPROD · PROD | 7.3.1 · 7.3.2 | H6 · H11 | 1 |
| RT-22.09 | Cumple parcialmente | Certificación de usuarios | PREPROD · PROD | 7.3.1 · 7.3.2 | H6 · H11 | 1 |
| RT-23.01 | Cumple parcialmente | Inspección del entregable de la oferta | — | — | Presentación de la oferta | 1 |
| RT-23.02 | Cumple parcialmente | Inspección del entregable de la oferta | — | — | Presentación de la oferta | 1 |
| RT-23.03 | Cumple parcialmente | Inspección del entregable de la oferta | — | — | Presentación de la oferta | 1 |
| RT-23.04 | Cumple parcialmente | Inspección del entregable de la oferta | — | — | Presentación de la oferta | 1 |
| RT-23.05 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-23.06 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-23.07 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-23.08 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-23.09 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-23.10 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-24.01 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-24.02 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-24.03 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-24.04 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-24.05 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-24.06 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-25.01 | Cumple parcialmente | Inspección del entregable de la oferta | — | — | Presentación de la oferta | 1 |
| RT-25.02 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-25.03 | Cumple parcialmente | Inspección del entregable de la oferta | — | — | Presentación de la oferta | 1 |
| RT-25.04 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-25.05 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-25.06 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-25.07 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-25.08 | Cumple parcialmente | Inspección del entregable de la oferta | — | — | Presentación de la oferta | 1 |
| RT-25.09 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-25.10 | No cumple | Sin prueba: no ofertado | — | — | — | 0 |
| RT-26.01 | Cumple | Indicador de verificación de la innovación (T-19) | PROD | 3.10 | Según T-19 | 1 |
| RT-26.02 | Cumple | Indicador de verificación de la innovación (T-19) | PROD | 3.10 | Según T-19 | 1 |
| RT-26.03 | Cumple | Indicador de verificación de la innovación (T-19) | PROD | 3.10 | Según T-19 | 1 |
| RT-26.04 | Cumple | Indicador de verificación de la innovación (T-19) | PROD | 3.10 | Según T-19 | 1 |
| RT-26.05 | Cumple | Indicador de verificación de la innovación (T-19) | PROD | 3.10 | Según T-19 | 1 |
| RT-26.06 | Cumple | Indicador de verificación de la innovación (T-19) | PROD | 3.10 | Según T-19 | 1 |
| RT-26.07 | Cumple | Indicador de verificación de la innovación (T-19) | PROD | 3.10 | Según T-19 | 1 |
| RT-26.08 | Cumple | Indicador de verificación de la innovación (T-19) | PROD | 3.10 | Según T-19 | 1 |

La matriz muestra que los requisitos funcionales se aceptan en la certificación de su etapa (H5 o H10), mientras que los no funcionales que dependen de la operación real se aceptan al cierre de la marcha blanca (H7 o H12). Los requisitos técnicos de operación y soporte (capítulo 21) no tienen hito de implementación: se verifican mes a mes con la medición de los niveles de servicio. Cada caso de prueba se identifica como CP-«ID»-nn y lleva el identificador en su anotación de código, de modo que la matriz se regenera desde el repositorio en cada ejecución del pipeline.

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
| JD-09 Integraciones | Mensajes de las 15 integraciones, con casos de error, lentitud, duplicado y orden | 353.333 mensajes diarios en peak | Sintético | QA · PREPROD | Antes de cada ciclo |
| JD-10 Incidentes de terreno | Evidencia de incidentes reproducidos por INN-02 | Según incidentes registrados | Evidencia anonimizada | QA | Permanente como regresión |

Los juegos de día normal y de peak cubren el perfil horario que exige el Caso, porque se generan con la distribución de las cuatro ventanas del SD4: preventa entre 09:00 y 18:00, preparación entre 22:00 y 06:00, despacho entre 05:30 y 07:00 y sincronización entre 17:00 y 20:00. Los pedidos diarios del JD-02 se obtienen de 31.000 pedidos al mes en 26 días hábiles, y los cobros, de 11.800 cobros en efectivo al mes en el mismo período.

### 9.D.2 Reglas de anonimización

Los datos históricos del JD-08 y la evidencia del JD-10 se transforman antes de salir de Producción, con las reglas de la Tabla 9.D.2. Las reglas preservan la integridad referencial y la distribución estadística que necesitan las pruebas. La salida esperada es un conjunto anonimizado para los efectos de prueba, pero no se presume irreversible por declaración: antes de liberarlo se ejecuta una prueba documentada de reidentificación sobre seudónimos, trazas, antecedentes comerciales y evidencias, y cualquier coincidencia atribuible a una persona bloquea la carga.

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

- Distribuidora Puelche S.A. (2026a). *Bases Administrativas de Licitación N.º TFEP-01/2026: Contratación de Solución Integral de Software y Servicios de Operación*.
- Distribuidora Puelche S.A. (2026b). *Bases Técnicas Transversales de Licitación N.º TFEP-01/2026*.
- Distribuidora Puelche S.A. (2026c). *Caso 02: Logística. Especificaciones del problema y operación de Distribuidora Puelche S.A.*
- International Organization for Standardization & International Electrotechnical Commission. (2011). *ISO/IEC 25010:2011 Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models*. ISO.
- LafroX. (2026). Subdocumentos 3, 4, 5, 6 y 9, con los anexos y formularios citados.
- Ley N.º 21.719. (2024). *Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales*. Diario Oficial de la República de Chile.

## Declaración de uso de IA

La tabla declara el apoyo de IA conforme a las Aclaraciones, §7.2.

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
| --- | --- | --- | --- | --- | --- |
| Anexo 9.A | Claude Code | Métricas y umbrales por subcaracterística | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| Anexo 9.B | Claude Code | Reglas y configuración de análisis | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| Anexo 9.C | Claude Code | Generación de la matriz desde el T-12 y el SD3 | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| Anexo 9.D | Claude Code | Juegos de datos y reglas de anonimización | Alto | Ninguno | [[REVISIÓN HUMANA]] |
