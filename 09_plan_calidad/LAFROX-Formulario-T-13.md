# Formulario T-13: Plan de pruebas y validación

Este formulario adjunta el plan de pruebas conforme al Subdocumento 9, como exigen las Bases Administrativas para el Formulario T-13. Contiene los niveles, tipos, ambientes, datos de prueba, criterios de entrada y salida, la automatización y el calendario de las pruebas de carga, de resiliencia, de recuperación ante desastres y de seguridad ofensiva. Su estructura sigue la del plan de pruebas de ISO/IEC/IEEE 29119-3. La estrategia y su fundamento están en el Subdocumento 9, sección 9.2. Los umbrales, en el Anexo 9.A. La matriz entre requisitos y pruebas, en el Anexo 9.C. Los juegos de datos, en el Anexo 9.D.

## 1. Alcance y elementos de prueba

El plan cubre la implementación de las Etapas 1 y 2 (meses 1 a 21) y las pruebas periódicas de la Operación (meses 21 a 56). Los elementos de prueba son los componentes de la solución del SD4:

- el monolito modular en Laravel 13 sobre PHP 8.5, con los módulos M1 Recepción, M2 Inventario, M3 Preventa, M4 Rutas, M5 Preparación, M6 Reparto, M7 Cobranza y rendición, M8 Devoluciones y envases, M9 Calidad y trazabilidad, M10 Analítica, M11 Canal moderno y M12 Telemetría;
- las 15 integraciones, INT-01 a INT-15;
- la aplicación Android en Kotlin, en sus cuatro perfiles de terreno;
- las consolas y los portales en Angular;
- la infraestructura híbrida de nube y sitios on-premise;
- la migración de los datos históricos.

Quedan fuera del plan los sistemas del CLIENTE que la solución integra, como el ERP y el servicio del SII. Se prueban sus interfaces con adaptadores simulados en QA y con el sistema real en Preproducción, pero no su lógica interna.

## 2. Niveles y tipos de prueba

La Tabla T13.1 define cada tipo de prueba, su nivel según ISO/IEC/IEEE 29119, su objetivo, la técnica de diseño y el responsable de su ejecución. Los responsables son los roles del Formulario T-15: DES (desarrollo), CAL (calidad y pruebas), IMP (implantación), SRE (operación y confiabilidad), SEG (seguridad) y DAT (datos).

**Tabla T13.1 — Niveles y tipos de prueba. Fuente: elaboración propia a partir del Subdocumento 9, sección 9.2.3, y de las Bases Técnicas Transversales, sección 20.1.**

| Tipo | Nivel | Objetivo | Técnica de diseño | Responsable |
| --- | --- | --- | --- | --- |
| Unitaria y de componente | Componente | Reglas de negocio de cada módulo | Particiones de equivalencia, valores límite, tablas de decisión | DES |
| Contrato | Integración | Cumplimiento de OpenAPI 3.1 y AsyncAPI por proveedor y consumidor | Casos por contrato: éxito, error, lentitud, duplicado, orden, versión | DES |
| Integración | Integración | Flujos de las 15 integraciones de extremo a extremo | Casos de uso y transición de estados | CAL |
| Sistema y regresión | Sistema | Comportamiento completo de la versión candidata | Casos de uso del SD3; batería automatizada | CAL |
| Aceptación de usuario | Aceptación | Validación con personas del CLIENTE | Escenarios de operación por perfil | CAL e IMP |
| Usabilidad | Aceptación | Indicadores de usabilidad del RT-13.04 | Pruebas moderadas con tareas medidas | IMP |
| Accesibilidad | Sistema | Conformidad WCAG 2.2 AA | Herramienta automática y revisión manual | CAL |
| Perfil operacional | Sistema | 14 h sin señal, 24 h sin enlace, −22 °C con guantes | Escenarios de terreno con dispositivos reales | CAL |
| Carga y estrés | Sistema | Umbrales p95 a 1,5× el peak y punto de quiebre | Perfil horario del SD4, escalones de carga | CAL y SRE |
| Resiliencia | Sistema | Degradación controlada y recuperación sin intervención | Inyección de fallas | CAL y SRE |
| Recuperación ante desastres | Sistema | RTO ≤ 4 h y RPO ≤ 15 min | Conmutación regional real | CAL y SRE |
| Seguridad ofensiva | Sistema | Sin hallazgos críticos ni altos | Prueba de intrusión por tercero independiente | SEG |
| Migración | Sistema | Conciliación sin diferencias no explicadas | Dos ensayos completos y conciliación por dominio | DAT y CAL |
| Despliegue y reversión | Sistema | Paso sin interrupción y reversión ≤ 10 min | Ensayo azul-verde con canario | SRE |

## 3. Ambientes de prueba

Cada tipo de prueba se ejecuta en el ambiente más bajo donde su resultado es válido. La Tabla T13.2 asigna las pruebas a los cinco ambientes del SD4, Tabla 12, y a terreno.

**Tabla T13.2 — Pruebas por ambiente. Fuente: elaboración propia a partir del SD4, sección 4.2.4.1.**

| Ambiente | Pruebas | Juegos de datos (Anexo 9.D) | Disponibilidad |
| --- | --- | --- | --- |
| Desarrollo | Unitaria, componente, contrato | JD-01 reducido | Horario de uso; efímero por rama |
| QA | Integración, sistema, regresión, DAST, accesibilidad, regresión de desempeño semanal | JD-01, JD-02, JD-06, JD-09, JD-10 | Horario de uso; ejecución nocturna de la regresión |
| Preproducción | Aceptación, carga y estrés, resiliencia, corte de enlace, migración, despliegue y reversión | JD-01 a JD-09 | Por ventana de prueba programada |
| Terreno y cámara | Perfil operacional con dispositivos reales | JD-04 | Programada con Operaciones del CLIENTE |
| Producción | Marcha blanca, prueba de intrusión anual, resiliencia semestral | Datos reales | Fuera de la ventana de 05:30 a 07:00 y de los congelamientos |
| Recuperación ante Desastres | Conmutación regional | Réplica productiva del ambiente Producción, con acceso restringido y auditado | Programada, fuera de congelamientos |

## 4. Datos de prueba

Ningún ambiente no productivo de prueba usa datos productivos sin anonimización verificada con Amazon Macie. Esta regla cubre Desarrollo, QA, Preproducción y Terreno. El ambiente de Recuperación ante Desastres es parte de la continuidad productiva: contiene una réplica de Producción sólo para conmutación real, con acceso restringido, auditoría y controles equivalentes a Producción; no se usa como ambiente de pruebas funcionales. Los diez juegos de datos del Anexo 9.D se generan desde la volumetría del Caso, sección 14.1, se versionan y se restituyen antes de cada ciclo. El juego de peak escala el día normal por 2.600 / 1.400 = 1,86, de modo que la prueba de carga opera sobre unas 18.600 líneas de preparación y 2.600 entregas por día. Los datos históricos se usan sólo en los ensayos de migración, anonimizados con las reglas de la Tabla 9.D.2, y se eliminan al cerrar cada ensayo.

## 5. Criterios de entrada y salida

Una prueba no comienza si no se cumple su criterio de entrada, y no se da por aprobada si no se cumple su criterio de salida. La Tabla T13.3 los define.

**Tabla T13.3 — Criterios de entrada y salida por tipo de prueba. Fuente: elaboración propia a partir de las Bases Técnicas Transversales, sección 20.1, del Caso 02, capítulo 15, y del SD4.**

| Tipo | Criterio de entrada | Criterio de salida |
| --- | --- | --- |
| Unitaria y de componente | Cambio en solicitud de fusión | Cobertura ≥ 70 % en lógica de negocio y ≥ 80 % global; 0 pruebas en falla |
| Contrato | Contrato publicado en el repositorio | 0 contratos rotos |
| Integración | Versión candidata en QA; adaptadores simulados disponibles | 15 de 15 flujos sin error; 0 regresiones |
| Sistema y regresión | Integración aprobada; datos JD-02 restituidos | Batería completa sin fallas; 0 defectos críticos o altos abiertos |
| Aceptación de usuario | Sistema aprobado; usuarios del CLIENTE capacitados en el escenario | Casos firmados por la Contraparte Técnica |
| Usabilidad | Prototipo o versión del flujo crítico | 20 líneas en ≤ 2 h con error ≤ 5 %; indicadores del RT-13.04 cumplidos |
| Accesibilidad | Vistas completas en QA | 0 incumplimientos WCAG 2.2 A y AA; informe de conformidad |
| Perfil operacional | Dispositivos del modelo comprometido; JD-04 cargado | 0 pérdidas y 0 duplicados; dispositivo sincronizado en ≤ 10 min; CD en ≤ 2 h; operación con guantes a −22 °C |
| Carga y estrés | Preproducción equivalente a Producción; JD-03 cargado; observabilidad activa | p95 de la Tabla 9.2 a 21,99 TPS; punto de quiebre registrado; sin pérdida al superar la capacidad |
| Resiliencia | Carga sostenida en curso; escenarios de falla aprobados | Recuperación sin intervención en cada escenario; 0 transacciones perdidas |
| Recuperación ante desastres | Réplica sincronizada; procedimiento aprobado | RTO ≤ 4 h y RPO ≤ 15 min medidos |
| Seguridad ofensiva | Versión congelada en Preproducción; alcance firmado con el tercero | 0 hallazgos críticos o altos abiertos; plan de remediación de los demás |
| Migración | Perfilado y saneamiento aprobados (3.7.1) | 0 diferencias no explicadas en la conciliación por dominio |
| Despliegue y reversión | Versión aprobada en sistema | Despliegue sin interrupción; reversión ≤ 10 min |

## 6. Suspensión y reanudación

Una prueba se suspende ante un defecto crítico que impida continuarla, ante una diferencia entre Preproducción y Producción que invalide el resultado o ante la indisponibilidad del juego de datos. Se reanuda desde el inicio del escenario afectado, no desde el punto de falla, cuando el defecto está corregido y verificado en QA. Una prueba de carga, de resiliencia o de recuperación suspendida dos veces por la misma causa se escala al Comité de Calidad. Si la suspensión compromete la fecha de entrega de un hito, el Jefe de Proyecto activa el disparador del riesgo correspondiente del SD8.

## 7. Automatización

La automatización es el criterio por defecto. La Tabla T13.4 indica la herramienta, el grado de automatización y la forma de ejecución de cada tipo de prueba.

**Tabla T13.4 — Automatización por tipo de prueba. Fuente: elaboración propia a partir del Subdocumento 9, secciones 9.2.2 y 9.2.3.**

| Tipo | Herramienta | Automatización | Ejecución |
| --- | --- | --- | --- |
| Unitaria y de componente | PHPUnit, JUnit 5, Jest | Total | Cada cambio (G2) |
| Contrato | Pruebas de contrato OpenAPI y AsyncAPI | Total | Cada cambio (G2) |
| Integración y regresión | PHPUnit, Espresso, Jest | Mayoritaria | Nocturna, dos ejecutores paralelos (≈ 4,3 h) |
| Accesibilidad | axe-core más revisión manual | Parcial | Cada promoción a Preproducción (G4); cualquier incumplimiento WCAG 2.2 A o AA confirmado bloquea |
| DAST | OWASP ZAP | Total | Cada promoción a Preproducción (G4) |
| Carga y estrés | k6 | Total | Regresión semanal en QA; prueba completa por certificación |
| Resiliencia | AWS Fault Injection Service; desconexión controlada del sitio emulado | Total | Por certificación y semestral |
| Recuperación ante desastres | Procedimiento automatizado de conmutación (SD4, Tabla 39) | Mayoritaria | Por certificación y semestral |
| Perfil operacional y usabilidad | Espresso y prueba con personas | Parcial | Por certificación |
| Seguridad ofensiva | Tercero independiente | Manual | Antes de cada paso a producción y anual |

Con 1.282 casos estimados y el 80 % automatizado, la regresión nocturna ejecuta 1.026 casos. Los 256 casos manuales requieren unas 64 HH por ciclo y se planifican con los evaluadores en los meses de certificación (Subdocumento 9, sección 9.2.3).

## 8. Calendario

El calendario de la implementación usa las fechas de los paquetes del Formulario T-15, sección 6.1. El de la Operación fija meses que evitan el congelamiento del 1 al 25 de septiembre, todo diciembre y los tres primeros días hábiles de cada mes (Caso 02, capítulo 15, RT-10.05).

### 8.1 Implementación (meses 1 a 21)

La Tabla T13.5 presenta las pruebas de la implementación con sus fechas y el hito que habilitan.

**Tabla T13.5 — Calendario de pruebas de la implementación. Fuente: elaboración propia a partir del Formulario T-15, sección 6.1, y del Formulario E-25.**

| Prueba | Paquete | Inicio | Término | Hito |
| --- | --- | --- | --- | --- |
| Usabilidad con usuarios y prototipos | 2.6.2 | 01-04-2027 | 29-04-2027 | H2 |
| Perfilado y saneamiento de datos | 3.7.1 | 04-08-2027 | 01-10-2027 | H4 |
| Integración, regresión e idempotencia E1 | 3.8.1 | 01-10-2027 | 20-10-2027 | H4 |
| Ensayos de migración en Preproducción | 3.7.2 | 04-10-2027 | 03-11-2027 | H5 |
| Seguridad ofensiva E1 | 3.8.6 | 21-10-2027 | 09-11-2027 | H5 |
| Carga 1,5× peak, estrés y resiliencia E1 | 3.8.4 | 21-10-2027 | 09-11-2027 | H5 |
| Recuperación ante desastres E1 | 3.8.5 | 21-10-2027 | 09-11-2027 | H5 |
| Despliegue sin interrupción E1 | 3.8.8 | 21-10-2027 | 09-11-2027 | H5 |
| Aceptación y accesibilidad E1 | 3.8.2 | 10-11-2027 | 17-11-2027 | H5 |
| Perfil operacional: sin señal, sin enlace, −22 °C | 3.8.3 | 10-11-2027 | 17-11-2027 | H5 |
| Certificación E1 | 3.8.7 | 18-11-2027 | 29-11-2027 | H5 |
| Ensayo de reversión de la Etapa 1 | 4.1.2 | 01-12-2027 | 09-12-2027 | H6 |
| Integración y regresión E2 | 3.9.1 | 01-05-2028 | 18-05-2028 | H9 |
| Despliegue sin interrupción E2 | 3.9.7 | 19-05-2028 | 26-05-2028 | H10 |
| Carga con ambas etapas y resiliencia | 3.9.3 | 19-05-2028 | 26-05-2028 | H10 |
| Recuperación ante desastres E1 + E2 | 3.9.4 | 19-05-2028 | 26-05-2028 | H10 |
| Seguridad ofensiva E2 | 3.9.5 | 19-05-2028 | 26-05-2028 | H10 |
| Aceptación y accesibilidad E2 | 3.9.2 | 27-05-2028 | 31-05-2028 | H10 |
| Certificación E2 | 3.9.6 | 01-06-2028 | 12-06-2028 | H10 |

Las pruebas de carga, resiliencia, recuperación y seguridad ofensiva de cada etapa comienzan después de la integración y regresión de su alcance, terminan antes de su certificación y terminan antes del inicio de la marcha blanca, que es el primer paso a Producción de cada alcance (H6 en el mes 13 y H11 en el mes 19). Antes del H7 y del H12 se repiten la prueba de intrusión por tercero, la prueba de resiliencia y la prueba de carga aplicable sobre la versión que cerrará la marcha blanca. Si durante la marcha blanca sólo hubo correcciones menores, el alcance de esas pruebas se acota a los componentes y superficies expuestas afectados, pero la ejecución y su informe son obligatorios. Ninguna prueba cae en un congelamiento. El ensayo de reversión se ejecuta en Preproducción en diciembre y no interviene Producción.

### 8.2 Operación (meses 21 a 56)

La Tabla T13.6 presenta las pruebas periódicas de la Operación, con el mes del contrato y su mes calendario.

**Tabla T13.6 — Calendario de pruebas periódicas de la Operación. Fuente: elaboración propia a partir del Subdocumento 9, Tabla 9.9.**

| Prueba | Frecuencia | Meses del contrato | Meses calendario | Cantidad |
| --- | --- | --- | --- | --- |
| Resiliencia por inyección de fallas | Semestral, con separación máxima de seis meses | 26, 32, 38, 44, 50, 55 | mar-2029, sep-2029, mar-2030, sep-2030, mar-2031, ago-2031 | 6 |
| Recuperación ante desastres | Semestral, con separación máxima de seis meses | 27, 33, 39, 45, 51, 54 | abr-2029, oct-2029, abr-2030, oct-2030, abr-2031, jul-2031 | 6 |
| Seguridad ofensiva por tercero | Anual | 28, 40, 52 | may-2029, may-2030, may-2031 | 3 |
| Carga previa al peak de septiembre | Anual | 31, 43, 55 | ago-2029, ago-2030, ago-2031 | 3 |
| Restauración de respaldos | Mensual | 21 a 56 | oct-2028 a sep-2031 | 36 |

Las cantidades coinciden con los entregables de los paquetes 8.1.3, 8.1.6 y 8.2.2 del Formulario T-14. Las pruebas que intervienen Producción o el sitio de recuperación se programan después del tercer día hábil del mes y fuera de la ventana de 05:30 a 07:00. La programación mantiene una separación máxima de seis meses entre ejecuciones del mismo tipo; las pruebas de septiembre se ejecutan antes del día 1 o después del día 25, según la ventana aprobada, para respetar el congelamiento operacional.

## 9. Roles y responsabilidades

El Líder de Calidad, Maximiliano Miño, es dueño de este plan, aprueba los criterios de entrada y salida y firma los informes de prueba. El rol CAL diseña y ejecuta las pruebas de integración, sistema, aceptación, carga y recuperación. SRE opera la infraestructura de prueba y la inyección de fallas. SEG contrata y supervisa al tercero de la prueba de intrusión. DAT ejecuta los ensayos de migración. IMP conduce las pruebas con personas usuarias. La Contraparte Técnica del CLIENTE firma los casos de aceptación y las actas de cada hito.

## 10. Informes y entregables de prueba

Cada prueba produce un informe con el alcance ejecutado, los resultados frente a cada criterio de salida, los defectos y su estado, y la evidencia: registros de ejecución, capturas, métricas y trazas. El informe de carga incluye la curva de tiempo de respuesta frente a carga, el punto de saturación, el consumo de recursos y el comportamiento durante y después del peak (RT-09.07). El informe de recuperación incluye el RTO y el RPO medidos y el plan de corrección de brechas (RT-07.07). La prueba de intrusión se entrega íntegra al CLIENTE con su plan de remediación (RT-11.20). El informe de accesibilidad separa el resultado automático de axe-core de la revisión manual; cualquier incumplimiento WCAG 2.2 A o AA confirmado queda como bloqueo de aceptación hasta corregirse. Los informes se agregan al expediente del hito que habilitan, conforme al Formulario T-17.

## Declaración de uso de IA

La tabla declara el apoyo de IA conforme a las Aclaraciones, §7.2.

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
| --- | --- | --- | --- | --- | --- |
| Formulario T-13 | Claude Code | Estructura del plan, criterios y calendario desde el T-15 | Alto | Ninguno | [[REVISIÓN HUMANA]] |
