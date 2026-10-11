# LafroX — Formulario T-13: Plan de pruebas y validación

Licitación TFEP-01/2026 · Caso 02 — Logística · Distribuidora Puelche S.A.

Este formulario acompaña al Subdocumento 9, Plan de calidad (en adelante, SD9). Contiene el plan de pruebas y validación que exige el Formulario T-13 de las Bases Administrativas: niveles, tipos, ambientes, datos de prueba, criterios de entrada y salida, automatización, y calendario de las pruebas de carga, resiliencia, recuperación ante desastres y seguridad ofensiva (Distribuidora Puelche S.A., 2026a, Formulario T-13). El SD9 resume y analiza este plan; el protocolo con el que el CLIENTE acepta cada hito está en el Formulario T-17.

En este formulario, BA, BTT y Caso designan las Bases Administrativas (Distribuidora Puelche S.A., 2026a), las Bases Técnicas Transversales (2026b) y las Bases Técnicas del Caso 02 (2026c). Mes 1 del contrato = febrero de 2027. Los paquetes de trabajo son los del Formulario T-14 y las fechas y horas, las del Formulario T-15. CAL, SEG, SRE, DAT e IMP designan los roles de calidad y pruebas, seguridad, operación y confiabilidad, datos e implantación del Formulario T-15; la sección 11 indica quién los ejerce.

---

## 1. Objeto, alcance y fuentes

El plan cubre las pruebas de la implementación (meses 1 a 21), de las dos marchas blancas (meses 13 a 15 y 19 a 20) y de la Operación (meses 21 a 56). Se aplica al monolito modular de 12 módulos (M1 a M12), a las 15 integraciones (INT-01 a INT-15), a la aplicación móvil Android en sus cuatro perfiles, a las consolas y portales web, a la infraestructura híbrida y a la migración de datos, tal como los define el Subdocumento 4 (SD4).

Las exigencias que el plan satisface son las siguientes:

| Fuente | Exigencia que rige este plan |
|---|---|
| Bases Administrativas, Art. 4.3 | ISO/IEC/IEEE 29119 para pruebas; ISO/IEC 25010 y 25012 para calidad del producto y de los datos |
| Bases Administrativas, Art. 24 | Cuatro ambientes aislados; regresión automatizada; cobertura ≥ 70 % de la lógica de negocio con umbral bloqueante; carga y estrés a 1,5 × el peak; resiliencia antes de cada paso a producción y semestral |
| Bases Técnicas Transversales (BTT), sección 20.1 | Diez tipos de prueba, con su momento y su criterio de salida |
| BTT, cap. 4 | Cinco ambientes y sus exigencias de datos (4.1); trazabilidad requisito–incidencia–código–prueba–despliegue (RT-04.04); flujo de integración con bloqueo automático (RT-04.05) |
| BTT, cap. 9 | Pruebas de carga y de estrés hasta el punto de quiebre (RT-09.06), con el contenido mínimo de su informe (RT-09.07), y degradación controlada (RT-09.08) |
| BTT, RT-07.07, RT-07.12, RT-10.07, RT-11.20 | Pruebas periódicas de la Operación |
| Caso 02, cap. 15 | Umbrales de respuesta (RT-09.01), operación desconectada (RT-03.10, RT-03.13), ventana protegida y congelamientos (RT-10.05), interfaces de terreno (RT-13.08) |
| Caso 02, cap. 18 | Dieciséis resultados de aceptación del caso (R18-01 a R18-16) |

---

## 2. Proceso de pruebas según ISO/IEC/IEEE 29119

El plan sigue los tres niveles de proceso de ISO/IEC/IEEE 29119-2 (ISO, IEC & IEEE, 2021a):

| Nivel de proceso | Artefacto | Responsable | Revisión |
|---|---|---|---|
| Organizacional | Política de pruebas de LafroX, dentro del sistema de gestión de calidad ISO 9001:2015 | Comité de Calidad y Procesos de LafroX | Anual |
| Gestión de pruebas | Este plan (T-13) y su seguimiento por campaña | Líder de Calidad y Pruebas, Maximiliano Miño | En cada hito y ante cada cambio aprobado de alcance |
| Pruebas dinámicas | Diseño, preparación del ambiente, ejecución e informe de cada caso | Equipo de pruebas (rol CAL) y especialistas (SEG, SRE, DAT, IMP) | En cada ejecución |

La intensidad de la prueba sigue el riesgo del producto, como dispone ISO/IEC/IEEE 29119-1 (ISO, IEC & IEEE, 2022). La prioridad de cada requisito en el catálogo del SD3 (crítica, alta o media) fija cuántos casos se diseñan para él (sección 8). La documentación de pruebas sigue la estructura de ISO/IEC/IEEE 29119-3 (ISO, IEC & IEEE, 2021c): especificación de casos, procedimientos, registro de ejecución, registro de incidencias e informe de finalización.

### 2.1 Técnicas de diseño (ISO/IEC/IEEE 29119-4)

| Tipo de regla | Técnica | Ejemplo en Puelche |
|---|---|---|
| Umbrales numéricos | Partición de equivalencia y valores límite | Rango térmico de un producto refrigerado; límite de crédito del cliente en la preventa |
| Reglas con varias condiciones | Tablas de decisión | Asignación de stock por vencimiento y lote; entrega con local cerrado |
| Ciclos de vida | Transición de estados | Estados del pedido, de la guía de despacho y de la misión de preparación |
| Flujos de usuario | Casos de uso y escenarios | Flujos del SD3 por perfil: preventista, preparador, conductor, bodega |
| Integraciones | Pruebas de contrato | Siete casos por integración: éxito, sin respuesta, con error, con lentitud, duplicado, orden y versión (RT-10.08) |
| Concurrencia y reconexión | Escenarios con conflicto | Dos dispositivos que reservan el mismo lote sin señal y sincronizan después |

---

## 3. Niveles y tipos de prueba

| Nivel o tipo | Ambiente | Herramienta | Automatización | Paquete T-14 | Exigencia |
|---|---|---|---|---|---|
| Unitaria y de componente | Desarrollo y cadena de integración | PHPUnit con PCOV (PHP); JUnit 5 con Kover (Kotlin); Jest (TypeScript) | Total | 1.5.2 | Art. 24; RT-04.11 |
| Contrato de API y eventos | Cadena de integración | Pact; Spectral contra OpenAPI 3.1 y AsyncAPI 2.6 | Total | 1.5.2 | Art. 4.3; RT-10.08 |
| Integración de los 15 flujos | QA | Pruebas automatizadas con simuladores del ERP y de terceros | Total | 3.8.1; 3.9.1 | BTT 20.1 |
| Sistema y regresión | QA | Playwright (consolas y portales); Espresso (Android) | ≥ 80 % de los casos | 3.8.1; 3.9.1 | BTT 20.1; Art. 24 |
| Análisis estático y de seguridad | Cadena de integración | PHPStan con Larastan; PHPMD, PHPCPD, PhpMetrics, deptrac; detekt; ESLint; SAST, SCA, secretos e imágenes | Total | 1.5.2 | RT-04.05 |
| Análisis dinámico de seguridad | QA | OWASP ZAP (web y API); MobSF (Android) | Total | 3.8.1; 3.9.1 | Art. 4.3 (OWASP) |
| Accesibilidad | QA y Preproducción | axe-core y revisión manual con teclado y lector de pantalla | Parcial | 3.8.2; 3.9.2 | RT-13.01 |
| Usabilidad con personas usuarias | Prototipos y Preproducción | Pruebas moderadas por perfil | Manual | 2.6.2; 2.6.3; 3.8.2; 3.9.2 | RT-13.03; RT-13.04 |
| Aceptación de usuario | Preproducción | Casos del SD3 ejecutados por personas del CLIENTE | Manual | 3.8.2; 3.9.2 | BTT 20.1 |
| Perfil operacional de terreno | Terreno, cámara de congelado y Preproducción | Dispositivos reales, Espresso para los flujos repetibles | Parcial | 3.8.3; 3.9.1; 3.9.2 | RT-03.10; RT-03.13; RT-13.08 |
| Carga y estrés | Preproducción | k6 | Total | 3.8.4; 3.9.3 | Art. 24; RT-09.06 a RT-09.08 |
| Resiliencia | Preproducción | AWS Fault Injection Service; desconexiones controladas del sitio emulado; corte de gateways de frío y de enlaces | Total en la inyección; manual en la observación | 3.8.4; 3.9.3; 8.2.2 | RT-10.07 |
| Continuidad de la arquitectura híbrida | Preproducción y sitio emulado | Nueve protocolos del SD4, Anexo 4-V (sección 7.5) | Parcial | 3.8.1; 3.8.3 a 3.8.5; 3.9.1; 3.9.3; 3.9.4 | RT-03.10; RT-07.04 |
| Recuperación ante desastres | Recuperación ante Desastres (us-east-1) | Conmutación regional real y recuperación del WMS de Talca en la nube (AL-DR-01) | Procedimiento automatizado con verificación manual | 3.8.5; 3.9.4; 8.1.3 | RT-07.07 |
| Restauración de respaldos | Producción y Recuperación | Restauración de una muestra representativa | Procedimiento automatizado | 4.2.1; 4.2.2; 4.3.1; 8.1.6 | RT-07.12 |
| Seguridad ofensiva | Preproducción con versión congelada | Tercero independiente | Manual | 3.8.6; 3.9.5; 8.2.2 | RT-11.20 |
| Despliegue sin interrupción y reversión | Preproducción | Cadena de entrega del SD4 (canario con reversión automática) | Total | 3.8.8; 3.9.7 | Art. 24; RT-04.07 |
| Migración de datos | Preproducción | Procedimiento de extracción, carga y conciliación del SD5 | Parcial | 3.7.1 a 3.7.5 | BTT 20.1; RT-05.11 |

Las herramientas son las declaradas en el Formulario T-10 (SD6) y en la cadena de entrega del SD4. Este plan no agrega herramientas nuevas.

---

## 4. Ambientes de prueba

| Ambiente | Pruebas que aloja | Datos | Estado antes de cada ciclo |
|---|---|---|---|
| Desarrollo | Unitarias, de componente y de contrato | Sintéticos | Reconstruible desde código |
| QA | Integración, sistema, regresión, análisis dinámico, accesibilidad automatizada, carga de regresión semanal | Juegos sintéticos versionados | Restituido a un estado conocido (BTT 4.1) |
| Preproducción | Aceptación, carga y estrés, resiliencia, ensayo del paso a producción, migración, seguridad ofensiva | Sintéticos con volumen de peak; históricos anonimizados solo para migración | Equivalente a Producción en topología, configuración y versiones (RT-04.02) |
| Producción | Verificación posterior al despliegue, indicadores diarios de la marcha blanca, restauración de respaldos | Reales | No se prueba con datos ficticios |
| Recuperación ante Desastres | Conmutación real | Réplica productiva protegida | No se usa como ambiente funcional de prueba |

### 4.1 Instancias de Preproducción por campaña

Varias campañas de certificación coinciden en el tiempo y no pueden compartir el ambiente. La resiliencia necesita carga sostenida; la prueba de intrusión exige una versión congelada; la migración carga datos históricos; la aceptación necesita datos estables. Por eso cada campaña usa su propia instancia de Preproducción, reconstruida desde el mismo código y con la misma topología y configuración. Siguen siendo Preproducción y no constituyen un sexto ambiente; se destruyen al cerrar la campaña (RT-04.02; RT-04.14).

| Instancia | Campaña | Condición que exige separarla |
|---|---|---|
| PRE-M | Ensayos de migración | Carga datos históricos anonimizados, que se eliminan al cerrar cada ensayo |
| PRE-C | Carga y estrés, luego resiliencia bajo carga, luego despliegue sin interrupción | La resiliencia y el despliegue se miden bajo la carga sostenida, en secuencia |
| PRE-S | Seguridad ofensiva | Versión congelada; no admite inyección de fallas en paralelo |
| PRE-A | Aceptación de usuario y accesibilidad | Las personas usuarias necesitan datos estables |

---

## 5. Datos de prueba

**Regla.** Ningún ambiente no productivo contiene datos productivos reales sin anonimización verificada. La regla protege los datos personales de clientes, conductores de terceros y la geolocalización de trabajadores (Ley N.º 21.719, 2024) y los campos que el Caso, RT-11.10, exige cifrar: comportamiento de pago, antecedentes comerciales y geolocalización.

| Juego | Origen | Volumen | Ambiente | Control |
|---|---|---|---|---|
| Maestros sintéticos | Generador con las reglas del SD3 y del SD5 | 14.200 clientes, 8.400 SKU (1.100 refrigerados o congelados), 180 proveedores (Caso, 14.1) | QA y Preproducción | Versionado; restituible |
| Transacciones de régimen | Generador sintético | 31.000 pedidos y 260.000 líneas de preparación al mes (Caso, 14.1) | QA y Preproducción | Versionado |
| Transacciones de peak | Generador sintético | Perfil de septiembre: ≈ 2.600 entregas por día (Caso, B.2) | Preproducción (PRE-C) | Versionado |
| Lotes y temperatura | Generador sintético | Lotes con vencimiento; series de temperatura con excursiones controladas | QA y Preproducción | Incluye los casos límite del rango térmico |
| Históricos para migración | Datos del ERP, del WMS de 2013 y de planillas del CLIENTE | 32,11 GB (SD4, Tabla 33, dimensión 10) | Solo PRE-M | Anonimización verificada con Amazon Macie (0 hallazgos) más una prueba de reidentificación sobre una muestra; se eliminan al cerrar el ensayo |
| Incidentes reproducidos | Evidencia de terreno capturada por INN-02, sin datos personales | Según incidentes | Ambientes efímeros por incidencia en QA o Preproducción | Convertidos en casos de regresión permanentes (SD13, sección 13.2) |

---

## 6. Criterios de entrada y de salida

### 6.1 Por nivel de prueba

| Nivel | Criterio de entrada | Criterio de salida |
|---|---|---|
| Unitaria y componente | Cambio con solicitud de fusión que cita su requisito o incidencia | Cobertura de lógica de negocio ≥ 70 % y global ≥ 80 %; 0 pruebas en falla; complejidad ciclomática ≤ 10 por método; 0 dependencias prohibidas entre módulos; acoplamiento eferente ≤ 20 clases por clase; duplicación ≤ 3 % (T-10) |
| Contrato | Contratos OpenAPI 3.1 y AsyncAPI 2.6 versionados | 0 contratos rotos |
| Integración | Imagen promovida a QA sin vulnerabilidades críticas ni altas; simuladores de los 15 flujos disponibles | 15 de 15 flujos sin error (BTT 20.1) |
| Sistema y regresión | Integración aprobada; juego de datos restituido | 100 % de la batería aprobada; 0 regresiones; p95, errores y colas de la carga de regresión no peores que en la última versión aceptada (SD4, sección 4.2.4.1.4) |
| Análisis dinámico | Versión desplegada en QA | 0 alertas altas de DAST; 0 hallazgos críticos o altos de MobSF |
| Aceptación de usuario | Regresión aprobada; 0 defectos críticos o altos abiertos; personas del CLIENTE convocadas y con inducción | Casos de aceptación firmados por la Contraparte Técnica (BTT 20.1) |
| Accesibilidad | Vistas completas en QA | 0 incumplimientos WCAG 2.2 A y AA; informe de conformidad entregado (RT-13.01) |
| Carga | Versión candidata en PRE-C; juego de peak cargado; monitoreo activo | Todos los p95 de la sección 7.1 a 21,99 TPS; 0 transacciones perdidas |
| Estrés | Carga aprobada | Punto de quiebre identificado; degradación con encolamiento y mensaje explícito, sin pérdida (RT-09.08) |
| Resiliencia | Carga sostenida en curso; escenarios de falla aprobados por el Arquitecto de Solución | Recuperación sin intervención en cada escenario; 0 pérdidas (RT-10.07) |
| Recuperación ante desastres | Procedimiento de conmutación aprobado; conmutación fuera de congelamiento, de la ventana de 05:30 a 07:00 y de los tres primeros días hábiles del mes | RTO ≤ 4 h y RPO ≤ 15 min medidos en conmutación real, regional y del WMS de Talca (RT-07.04, RT-07.07; AL-DR-01) |
| Seguridad ofensiva | Versión congelada en PRE-S; alcance acordado con el tercero | 0 hallazgos críticos o altos abiertos (RT-11.20) |
| Perfil operacional | Dispositivos de producción, uno de cada tipo; personas del CLIENTE convocadas | Ver sección 7.3 |
| Migración | Perfilado y saneamiento cerrados (3.7.1); mapeo del SD5, Anexo 5-L | Conciliación sin diferencias no explicadas en cada ensayo; tiempos medidos compatibles con la ventana y con la reversión (SD5, 5.3.5) |
| Despliegue sin interrupción | Estrategia canario configurada | Despliegue y reversión sin interrupción del servicio y sin intervención manual (RT-04.06, RT-04.07) |

### 6.2 Suspensión y reanudación

Una campaña se suspende cuando aparece un defecto crítico que impide seguir ejecutando casos, cuando el ambiente pierde su equivalencia con Producción o cuando los datos dejan de estar en el estado declarado. Se reanuda con el defecto corregido y verificado en QA, con el ambiente reconstruido y con los datos restituidos. Los casos ya aprobados que dependen del componente corregido se ejecutan de nuevo.

---

## 7. Especificación de las pruebas que habilitan cada entrada a Producción

### 7.1 Carga y estrés

La carga se deriva del dimensionamiento del SD4, Tabla 33, y no se elige:

| Magnitud | Peak declarado (SD4) | Factor | Carga de prueba |
|---|---|---|---|
| TPS máximo de septiembre (12:00) | 14,66 TPS | 1,5 (Art. 24; RT-09.06) | 21,99 TPS |
| TPS máximo de la ventana de 05:30 a 07:00 | 6,94 TPS | 1,5 | 10,41 TPS, sostenidos 90 minutos |
| Personas usuarias concurrentes (cota extrema) | 775,33 | 1,5 | 1.163 |
| Dispositivos de terreno simultáneos | 158 | 1,5 | 237 |
| Escalón de crecimiento (RT-09.03) | 14,66 TPS | 3 | 43,98 TPS |
| Escalón de quiebre | 14,66 TPS | 4 | 58,64 TPS |

**Umbrales de salida (p95, SD4, Tabla 31):** confirmación de línea de preparación ≤ 1 s; registro de entrega ≤ 2 s; línea de preventa ≤ 1,5 s; consulta de stock y crédito ≤ 2 s; transacción crítica de terreno ≤ 3 s; carga inicial del portal ≤ 2 s; navegación ≤ 1 s; API de consulta ≤ 500 ms; API de escritura ≤ 800 ms; búsqueda compuesta ≤ 3 s y búsqueda global ≤ 2 s; informe estándar ≤ 30 s.

**Ventana de despacho.** La prueba de 10,41 TPS concentra la emisión de guías en los 90 minutos. Su criterio de salida incluye 0 minutos de indisponibilidad (Caso, RT-10.05).

**Informe (RT-09.07):** curva de tiempo de respuesta frente a carga, punto de saturación, consumo de recursos por componente, y comportamiento durante y después del peak. El informe identifica el primer cuello de botella declarado en el SD4 (RT-09.05) y compara su comportamiento observado con el previsto.

### 7.2 Resiliencia

| Escenario (RT-10.07) | Forma de inyección | Resultado esperado |
|---|---|---|
| Caída de instancia | AWS FIS detiene tareas ECS Fargate | Reemplazo automático sin pérdida |
| Caída de zona de disponibilidad | AWS FIS sobre una zona | Continuidad en las zonas restantes |
| Dependencia externa sin respuesta, con error o lenta | Simulador de la integración afectada | Comportamiento declarado por integración (RT-10.08) |
| Latencia elevada | Inyección de latencia de red | Umbrales de la sección 7.1 o degradación controlada |
| Saturación de disco | Llenado controlado del volumen | Alerta anticipada y continuidad |
| Corte de enlace del centro de distribución por 24 h | Desconexión del sitio emulado | Operación local continua; sincronización ≤ 2 h tras reconectar, con conflictos de stock resueltos de forma determinista (RT-03.10, RT-03.13) |
| Pérdida de fibra y LTE de un centro de distribución | Corte de ambos enlaces en el sitio emulado | Conmutación a Starlink en espera caliente; la emisión de guías por el ERP continúa (SD4, sección 4.1.3.2; AL-DTE-01) |
| Caída de un gateway de frío de Talca | Detención de uno de los dos gateways con Greengrass | El otro gateway lee ambas cámaras; el bloqueo térmico local actúa en ≤ 5 s y la alerta llega a M9 (SD4, ADR-22) |

Los dos últimos escenarios prueban la parte on-premise de la arquitectura híbrida, que el RT-10.07 no enumera pero que el SD4 declara crítica para el despacho y para la cadena de frío.

### 7.3 Perfil operacional de terreno

| Condición (Caso, cap. 15) | Prueba | Criterio de salida |
|---|---|---|
| Turno completo de 14 h sin cobertura | Jornada completa de un repartidor rural, incluida la ruta de 34 clientes (SD4, Tabla 33, dimensión 13) | 0 registros perdidos o duplicados; sincronización ≤ 10 min tras reconectar |
| −22 °C con guantes térmicos | Preparación y recepción en cámara de congelado | Transacción completada con guantes; indicadores RT-13.04 del perfil dentro de umbral |
| Lluvia | Entrega a la intemperie bajo lluvia | Transacción completada; dispositivo operativo |
| Sobre 34 °C | Entrega a la intemperie con calor | Transacción completada; dispositivo operativo |
| Sol directo | Lectura de la pantalla en la puerta del local | Lectura sin error de la persona usuaria |
| Una sola mano durante la descarga | Registro de entrega | Transacción completada con una mano |

Cada perfil mide los cuatro indicadores del RT-13.04 con los valores del SD3, Tabla 3.A.4a (métrica 9A-18): tasa de error ≤ 5 % en todos los perfiles y aprendizaje ≤ 2 h en bodega, ≤ 4 h para el preventista y ≤ 30 min para el conductor.

### 7.4 Pruebas de los resultados del caso

Las pruebas técnicas no aceptan por sí solas los resultados del Caso, cap. 18. Algunos se ensayan antes de la marcha blanca para llegar a ella sin sorpresas:

| Resultado | Ensayo previo | Cuándo |
|---|---|---|
| R18-01: clientes afectados por un lote en menos de 2 h | Simulacro de retiro sanitario sobre datos sintéticos con lotes trazados | Aceptación de la Etapa 1 (3.8.2) |
| R18-03: registro continuo de temperatura | Series con excursiones controladas; verificación del bloqueo del despacho ante una excursión fuera de rango | Integración (3.8.1) y aceptación (3.8.2) |
| R18-06: ningún pedido perdido ni duplicado por falta de señal | Jornada de 14 h sin señal (sección 7.3) | Perfil operacional (3.8.3) |
| R18-07: ruta del día siguiente en menos de 20 minutos | Generación de la ruta con el volumen de un día de peak | Carga (3.8.4) |

Los dieciséis resultados se aceptan con el protocolo del Formulario T-17, en el momento que fija el SD7, Tabla 7.11.

### 7.5 Protocolos de aceptación de la arquitectura híbrida

El SD4, Anexo 4-V, define nueve protocolos que verifican la continuidad de la arquitectura en la nube y en los cinco sitios con servicio local. Se ejecutan en Preproducción antes de la ola aplicable, dentro de las campañas de este plan:

| Protocolo | Qué verifica (SD4, Anexo 4-V) | Campaña de este plan |
|---|---|---|
| AL-DTE-01 | 96 guías por las rutas de Talca y de los demás sitios, con fallas y cambio de carga; emisión por fibra, LTE o Starlink | Resiliencia (3.8.4; 3.9.3) |
| AL-POD-01 | Entrega total, parcial y con receptor sustituto sin señal | Perfil operacional (3.8.3) |
| AL-SLA-01 | Ventanas y cuotas del ERP, del SII y de las contrapartes | Integración (3.8.1; 3.9.1) |
| AL-OFF-01 | Aislamiento de cada sitio por 24 horas, con relevos y despacho con guía preemitida | Resiliencia (3.8.4; 3.9.3) |
| AL-CLI-01 | Pedidos sin señal en el Portal de Clientes instalado y reconexión | Integración (3.8.1; 3.9.1) |
| AL-DR-01 | Corte de los caminos y recuperación del WMS de Talca en la nube | Recuperación ante desastres (3.8.5; 3.9.4) |
| AL-PERF-01 | Carga de 3× con mamparos por perfil | Carga y estrés (3.8.4; 3.9.3) |
| AL-STOCK-01 | Última unidad pedida desde preventa, portal y EDI, con cortes y acuses perdidos | Integración (3.8.1; 3.9.1) |
| AL-ACT-01 | Cada actor con una operación permitida y una denegada | Integración (3.8.1; 3.9.1) |

Cada protocolo deja su acta con la carga, la falla inyectada, el resultado observado y los responsables, y esa acta forma parte del expediente del H5 o del H10 (T-17, sección 3.1).

---

## 8. Automatización

### 8.1 Criterio

La automatización es la regla. Una prueba es manual solo si exige el juicio de una persona usuaria (aceptación, usabilidad, accesibilidad manual), una condición física (perfil operacional) o un tercero independiente (seguridad ofensiva).

### 8.2 Tamaño estimado del catálogo

El catálogo se dimensiona por riesgo, con la prioridad de cada requisito en el SD3, Anexos. Los casos por requisito (cinco, tres y dos según la prioridad; uno por RT; siete por integración) forman la regla de dimensionamiento por riesgo de LafroX, que el plan del H1 contrasta con el diseño real de los casos:

| Grupo | Cantidad | Casos por requisito | Casos |
|---|---|---|---|
| RF y RNF de prioridad crítica | 56 | 5 | 280 |
| RF y RNF de prioridad alta | 163 | 3 | 489 |
| RF y RNF de prioridad media | 43 | 2 | 86 |
| RT en estado «Cumple» o «Cumple parcialmente» en el T-12 | 356 | 1 | 356 |
| Contratos de integración | 15 | 7 | 105 |
| **Total** | | | **1.316** |

Los 262 RF y RNF con prioridad propia son los del catálogo del SD3. Las nueve filas RF y RNF restantes del T-12 (271 en total) se verifican con la fila que las contiene y no suman casos. Los 18 RT en estado «No cumple» no tienen casos; quedan en la matriz de trazabilidad como brecha visible.

### 8.3 Duración de la regresión

El cálculo usa tres parámetros de diseño del plan: 80 % de los casos automatizados, 30 segundos por caso automático y 15 minutos por caso manual. Con ellos: 0,8 × 1.316 ≈ 1.053 casos automáticos. A 30 segundos por caso, la regresión completa toma 1.053 × 0,5 / 60 ≈ 8,8 horas en un ejecutor y ≈ 4,4 horas en dos ejecutores paralelos. Cabe en una ejecución nocturna antes de cada promoción a Preproducción.

Los 263 casos manuales, a 15 minutos cada uno, requieren 263 × 15 / 60 ≈ 65,8 HH por ciclo. Se planifican con los evaluadores en los meses de certificación.

---

## 9. Calendario

### 9.1 Implementación

| Campaña | Paquete | Instancia o ambiente | Inicio | Término | HH (T-15) |
|---|---|---|---|---|---|
| Plan de calidad y de pruebas; revisión preliminar el 05-03-2027 | 1.5.1 | — | 01-03-2027 | 09-03-2027 | 80 |
| Investigación con personas usuarias | 2.6.1 | Puestos de trabajo | 01-03-2027 | 29-03-2027 | 240 |
| Matriz de trazabilidad (H1) | 1.2.4 | — | 01-03-2027 | 09-03-2027 | 80 |
| Prototipos y pruebas de usabilidad | 2.6.2 | Prototipos | 01-04-2027 | 29-04-2027 | 240 |
| Indicadores de usabilidad | 2.6.3 | — | 03-05-2027 | 31-05-2027 | 240 |
| Puertas automáticas activas | 1.5.2 | Cadena de integración | Mes 6 | Mes 20 | 80 |
| Ensayo de migración 1 | 3.7.2 | PRE-M | 04-10-2027 | 03-11-2027 | (en 480 HH del paquete) |
| Integración, regresión e idempotencia E1 (H4) | 3.8.1 | QA | 01-10-2027 | 20-10-2027 | 160 |
| Aceptación y accesibilidad E1 | 3.8.2 | PRE-A | 21-10-2027 | 17-11-2027 | 320 |
| Perfil operacional E1 | 3.8.3 | Terreno y cámara | 21-10-2027 | 17-11-2027 | 320 |
| Carga, estrés y resiliencia E1 | 3.8.4 | PRE-C | 21-10-2027 | 09-11-2027 | 320 |
| Recuperación ante desastres E1 | 3.8.5 | Recuperación | 21-10-2027 | 09-11-2027 | 320 |
| Seguridad ofensiva E1 | 3.8.6 | PRE-S | 21-10-2027 | 09-11-2027 | 320 |
| Despliegue sin interrupción E1 | 3.8.8 | PRE-C | 21-10-2027 | 09-11-2027 | 320 |
| Acta de certificación E1 (H5) | 3.8.7 | — | 18-11-2027 | 29-11-2027 | 160 |
| Ensayo de migración 2 | 3.7.3; 3.7.4 | PRE-M | 01-12-2027 | 31-12-2027 | (en las HH de los paquetes) |
| Acta de conciliación y corte | 3.7.5 | — | 03-01-2028 | 27-01-2028 | 480 |
| Integración y regresión E2 sin afectar E1 (H9) | 3.9.1 | QA | 01-05-2028 | 18-05-2028 | 160 |
| Carga con ambas etapas y resiliencia | 3.9.3 | PRE-C | 19-05-2028 | 26-05-2028 | 320 |
| Recuperación ante desastres con ambas etapas | 3.9.4 | Recuperación | 19-05-2028 | 26-05-2028 | 320 |
| Seguridad ofensiva E2 | 3.9.5 | PRE-S | 19-05-2028 | 26-05-2028 | 160 |
| Despliegue sin interrupción E2 | 3.9.7 | PRE-C | 19-05-2028 | 26-05-2028 | 160 |
| Aceptación y accesibilidad E2 | 3.9.2 | PRE-A | 27-05-2028 | 31-05-2028 | 320 |
| Acta de certificación E2 (H10) | 3.9.6 | — | 01-06-2028 | 12-06-2028 | 160 |

En E2, 3.9.1/3.9.2 incluyen regresión de las cinco condiciones físicas y de desconexión sobre funciones/dispositivos modificados, con evidencia de cobertura para condiciones no modificadas; no se omite el perfil por ausencia de un paquete nuevo.

La campaña de aceptación de la Etapa 2 es breve porque cubre solo el alcance incremental. Los flujos de la Etapa 1 se verifican con la regresión de 3.9.1, que corre antes.

La ventana 21-10 a 09-11-2027 de 3.8.5 comprende preparación no invasiva del 21 al 25 de octubre, ejecución/conmutación y reversión del 26 al 29 de octubre, y análisis/informe hasta el 9 de noviembre. No se interviene el sitio el 1 de noviembre (feriado) ni los días 2, 3 y 4 (primeros tres hábiles efectivos); el análisis no modifica el sitio. La autorización precisa además horario fuera de despacho y reversión segura.

Ninguna ejecución invasiva de campaña que intervenga Producción o el sitio de recuperación cae en un congelamiento (septiembre y diciembre) ni en los tres primeros días hábiles del mes (Caso, RT-10.05). Las campañas en Preproducción pueden hacerlo, porque no tocan Producción.

### 9.2 Marchas blancas y soporte puente

| Período | Prueba | Frecuencia |
|---|---|---|
| Meses 13 a 15 (E1) y 19 a 20 (E2) | Indicadores diarios del Art. 17.3 (SD7, Tabla 7.9) y conciliación con el registro vigente | Diaria |
| Meses 13 a 20 | Restauración de respaldos sobre una muestra representativa, con tiempo medido (RT-07.12), por SRE: 4.2.1 (13–15), 4.2.2 (16–18) y 4.3.1 (19–20); ocho informes distintos de los 36 de 8.1.6 | Mensual |
| Cada corrección | Puertas G0 a G4 y G6, regresión completa, DAST y carga de regresión; repetición de la prueba de certificación afectada | Por corrección |

Cada restauración previa tiene 16 HH SRE (4 preparación, 4 ejecución, 4 validación y 4 informe); se agregan 48 HH a 4.2.1, 48 a 4.2.2 y 32 a 4.3.1 como componentes separados de la cobertura NOC/mesa. Las siete conmutaciones operacionales requieren 560 HH y la recuperación inicial 320 HH según el desglose por actividades/roles del T-15; el mismo formulario justifica 320/160 HH de intrusión E1/E2.

### 9.3 Operación (meses 21 a 56)

| Prueba | Exigencia | Meses | Fechas | Cantidad | Paquete |
|---|---|---|---|---|---|
| Recuperación ante desastres con conmutación real | Al menos dos veces al año (RT-07.07) | 21, 27, 33, 39, 45, 51, 54 | oct-28, abr-29, oct-29, abr-30, oct-30, abr-31, jul-31 | 7 | 8.1.3 |
| Resiliencia por inyección de fallas | Al menos una vez por semestre (RT-10.07) | 26, 32, 38, 44, 50, 55 | mar-29, sep-29, mar-30, sep-30, mar-31, ago-31 | 6 | 8.2.2 |
| Intrusión por tercero independiente | Anual (RT-11.20) | 28, 40, 52 | may-29, may-30, may-31 | 3 | 8.2.2 |
| Restauración de respaldos | Al menos mensual (RT-07.12) | 21 a 56 | Mensual | 36 | 8.1.6 |
| Regresión de INN-02 | Escenarios reproducidos de incidentes | 21 a 56 | Trimestral (informe) | 12 | 8.3.1 |

Las resiliencias de septiembre (meses 32 y 44) se ejecutan en Preproducción, porque septiembre está congelado. Cada prueba periódica produce un informe con el resultado medido, la comparación con su umbral y el plan de corrección de las brechas (RT-07.07).

---

## 10. Defectos

| Severidad | Definición (alineada con el SD4, Tabla 16) | Efecto en las pruebas |
|---|---|---|
| Crítica | Afecta un servicio de nivel crítico: preparación y despacho con emisión de guía en la ventana de 05:30 a 07:00, bloqueo por excursión térmica o identidad de bodega | Detiene la promoción; puede suspender la campaña |
| Alta | Afecta un servicio de nivel alto: preventa y consulta de stock y crédito, entrega y su evidencia, rutas, documentos tributarios, ERP, cobranza, registro de temperatura | Detiene la promoción |
| Media | Afecta un servicio de nivel medio con alternativa operativa | Se registra y se planifica |
| Baja | Afecta la reportería sin impedir operar | Se registra y se planifica |

Cada defecto se registra en GitLab con el caso de prueba, el requisito, el ambiente, la versión y la evidencia. Se cierra solo cuando la prueba que lo detectó pasa y queda incorporada a la regresión. Los hallazgos de seguridad conservan su severidad propia y sus plazos de corrección de 7, 15 y 30 días corridos para severidad crítica, alta y media (BA, Art. 21.1; SD4, sección 4.2.4.1.4).

---

## 11. Roles

| Rol | Persona o equipo | Responsabilidad en este plan |
|---|---|---|
| Líder de Calidad y Pruebas | Maximiliano Miño | Dueño del plan; aprueba el inicio y el cierre de cada campaña; veto sobre la promoción |
| Equipo de pruebas (CAL) | Analistas de pruebas de LafroX, con refuerzo de evaluadores subcontratados en los meses de certificación (SD6, sección 6.1.3) | Diseño, automatización y ejecución |
| Seguridad (SEG) | Encargado de Seguridad, Álvaro Catalán, y tercero independiente | Análisis de seguridad y pruebas de intrusión |
| Operación y confiabilidad (SRE) | Líder de Operación, Guillermo Castillo | Resiliencia, recuperación, restauración, despliegue sin interrupción |
| Datos (DAT) | Líder de Datos, Leandro Chamorro | Ensayos de migración y conciliación |
| Líder Funcional | Patricio Henríquez | Coordina la aceptación con las personas del CLIENTE |
| Contraparte Técnica del CLIENTE | Designada por Distribuidora Puelche | Firma los casos de aceptación y las actas (T-17) |

---

## 12. Informes de prueba

| Informe | Contenido mínimo | Destinatario | Frecuencia |
|---|---|---|---|
| Informe de ejecución de la cadena de integración | Resultados por requisito, cobertura, métricas de código | Equipo y Líder de Calidad | Cada ejecución |
| Informe de campaña | Casos ejecutados, aprobados y fallidos; defectos por severidad; desviaciones del plan; conclusión de salida | Líder de Calidad y Contraparte Técnica | Al cierre de cada campaña |
| Informe de carga | Contenido del RT-09.07 (sección 7.1) | Contraparte Técnica | Por campaña de carga |
| Informe de recuperación ante desastres | RTO y RPO medidos; brechas y su plan de corrección (RT-07.07) | Contraparte Técnica | Por prueba |
| Informe íntegro de intrusión | Hallazgos, severidad, plan de remediación con plazos (RT-11.20) | CLIENTE | Por prueba |
| Informe mensual de calidad | Métricas de proceso, defectos escapados, estado de la matriz de trazabilidad | Comité de Calidad y Contraparte Técnica | Mensual |

---

## Referencias

- Distribuidora Puelche S.A. (2026a). *Bases Administrativas, Licitación TFEP-01/2026*.
- Distribuidora Puelche S.A. (2026b). *Bases Técnicas Transversales, Licitación TFEP-01/2026*.
- Distribuidora Puelche S.A. (2026c). *Bases Técnicas del Caso 02 — Logística*.
- International Organization for Standardization, International Electrotechnical Commission, & Institute of Electrical and Electronics Engineers. (2021a). *ISO/IEC/IEEE 29119-2:2021. Software and systems engineering — Software testing — Part 2: Test processes*.
- International Organization for Standardization, International Electrotechnical Commission, & Institute of Electrical and Electronics Engineers. (2021c). *ISO/IEC/IEEE 29119-3:2021. Software and systems engineering — Software testing — Part 3: Test documentation*.
- International Organization for Standardization, International Electrotechnical Commission, & Institute of Electrical and Electronics Engineers. (2021b). *ISO/IEC/IEEE 29119-4:2021. Software and systems engineering — Software testing — Part 4: Test techniques*.
- International Organization for Standardization, International Electrotechnical Commission, & Institute of Electrical and Electronics Engineers. (2022). *ISO/IEC/IEEE 29119-1:2022. Software and systems engineering — Software testing — Part 1: General concepts*.
- Ley N.º 21.719. (2024). *Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales*. Diario Oficial de la República de Chile.
