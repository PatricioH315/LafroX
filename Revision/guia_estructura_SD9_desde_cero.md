# Guía para construir el SD9 desde cero

Nota de trabajo (no entregable). Parte de la estructura obligatoria del Capítulo 9 y, título por título, indica qué exigen las Bases, qué aportan las clases y el PMBOK, y qué va a los formularios T-13 y T-17 en lugar del cuerpo. No toma como referencia el SD9 existente.

**Precedencia.** Aclaraciones (estructura y presentación) > Bases Administrativas > Bases Técnicas Transversales > Caso 02. Las clases y el PMBOK orientan el método y no crean requisitos. En la oferta, el PMBOK se cita como Project Management Institute (2017), con página; las clases no se citan.

**Peso.** Subdocumento 9 = 8 % del Informe 2 y 6 % de la propuesta final (Formulario T-21).

---

## 0. Esqueleto obligatorio

Los títulos se copian textuales, con la misma numeración y en el mismo orden (Aclaraciones §2). Los subtítulos de nivel 9.x.y son propuestas: se pueden agregar, pero no se puede agregar un 9.4.

```
Índice detallado (con página, linkeable)
Introducción al Plan de calidad          ← texto de introducción del capítulo
9.1 Plan de Calidad
9.2 Estrategia de Aseguramiento de Calidad
9.3 Alineación con Plan de Trabajo
Referencias                              ← sin numerar
Declaración de uso de IA                 ← sin numerar
```

Formularios que acompañan al capítulo, cada uno en su propio archivo y citado en el texto:
- `LAFROX-Formulario-T-13`: plan de pruebas y validación.
- `LAFROX-Formulario-T-17`: protocolo de aceptación.

---

## 1. Introducción al Plan de calidad

**Qué exige (Aclaraciones §2 y §11):** un resumen del capítulo y su conexión con los demás capítulos, anexos y formularios.

**Conexiones que debe nombrar (de las Bases):**
- SD3: requisitos y criterios de aceptación, que son lo que se verifica.
- SD4: los cinco ambientes y la cadena de entrega (BTT cap. 4).
- SD5: calidad de datos según ISO/IEC 25012 (Art. 4.3).
- SD6: DevSecOps y la definición de terminado (RT-20.07).
- SD7: EDT, cronograma e hitos del E-25.
- SD8: riesgos de calidad.
- T-13 y T-17.

**Aporte del caso:** la razón de ser del plan es Puelche. Los resultados de aceptación del Caso, cap. 18, son la meta. Entre ellos: retiro sanitario en menos de 2 h (hoy son 9 días), 100 % de lotes registrados, registro continuo de temperatura, ningún pedido perdido sin señal. También pesa la entrevista a la Jefa de Calidad (Caso cap. 8): pide bloquear el despacho ante una excursión térmica y señala que esa regla no está escrita en ninguna parte.

**Del PMBOK:** p. 300. En industrias reguladas, como salud y transporte, el control de calidad es más estricto. Puelche distribuye alimentos refrigerados bajo fiscalización sanitaria, lo que justifica un plan exigente.

---

## 2. 9.1 Plan de Calidad

**Qué exige (Aclaraciones §11 y T-7):**
1. Marco de aseguramiento de calidad basado en **ISO/IEC 25010** y en **modelos de madurez**.
2. Métricas de calidad del código, **cobertura de pruebas, complejidad y acoplamiento**, con **umbrales bloqueantes**.

**Qué exigen las Bases:**

| Fuente | Exigencia |
|---|---|
| BA Art. 4.3 | ISO/IEC 25010, ISO/IEC 25012 (datos), ISO/IEC/IEEE 29119 (pruebas) y el PMBOK como marco base. Para cada uno hay que mostrar cómo se cumple: mencionarlo sin evidencia vale puntaje cero |
| BA Art. 24 | Umbral numérico para **8 características**: funcionalidad, desempeño, compatibilidad, usabilidad, fiabilidad, seguridad, mantenibilidad y portabilidad. Cobertura ≥ 70 % de la lógica de negocio, bloqueante. Deuda técnica registrada, cuantificada y con presupuesto |
| BTT RT-04.11 | Cobertura ≥ 70 % bloqueante en el flujo de integración continua |
| BTT RT-04.12 | Declarar y medir: frecuencia de despliegue, tiempo del commit a producción, tasa de cambios fallidos y tiempo de restauración |
| Caso cap. 15 y 18 | Parámetros numéricos y los 16 resultados de aceptación |

**Qué aportan las clases y el PMBOK:**

| Contenido | Fuente | Uso en 9.1 |
|---|---|---|
| Componentes del plan de gestión de la calidad: estándares, objetivos, roles, entregables sujetos a revisión, actividades de gestión y control, herramientas, tratamiento de no conformidades y mejora continua | PMBOK p. 286 | Es el índice natural de 9.1.1 |
| Métrica de calidad: atributo + cómo se verificará | PMBOK p. 287 | Toda métrica lleva su método de verificación |
| Calidad frente a grado | PMBOK p. 274 | Justifica comprometer *menos* funciones sin defectos antes que muchas con defectos |
| Prevención antes que inspección | PMBOK p. 274 | Principio que ordena las puertas de 9.2 |
| **Costo de la calidad**: prevención, evaluación, fallas internas y externas | PMBOK pp. 274, 282–283 | Clasificar las HH de calidad de la EDT. **En HH, nunca en dinero** (Art. 50.2) |
| Cinco niveles de gestión de la calidad | PMBOK p. 275 | Declarar el nivel buscado: calidad incorporada al diseño y cultura organizacional |
| Adaptación: normativa y estándares de la industria | PMBOK p. 276 | Normativa sanitaria y cadena de frío |
| Atributos de calidad ISO/IEC 25010 | FEP01 d. 13 | Ver la advertencia de la sección 6 |
| Cómo se escribe un atributo: estímulo, condición, respuesta y métrica con valor | FEP01 d. 15 | Formato obligatorio para cada umbral |
| p95 y no el promedio; latencia, throughput y concurrencia | FEP01 d. 173 | Métricas de desempeño |
| SLI, SLO y SLA | FEP01 d. 174 | Separar la meta interna (SLO) del compromiso contractual (Art. 78) |
| Cálculo de disponibilidad | FEP01 d. 171 | Métricas de fiabilidad |
| Criterio de aceptación con umbral | FEP02 d. 38 | «Sin umbral no se puede recibir ni rechazar» |

**Subtítulos propuestos:**
- **9.1.1 Política, objetivos y gobierno de la calidad.** Objetivos medibles derivados del Caso cap. 18. Roles: Líder de Calidad independiente del equipo de desarrollo, comité y Contraparte Técnica. Distinguir aseguramiento de control (PMBOK p. 290).
- **9.1.2 Estándares aplicados y forma de acreditarlos.** Para cada norma del Art. 4.3, el mecanismo concreto que la hace verificable.
- **9.1.3 Modelo de calidad del producto según ISO/IEC 25010.** Las 8 características del Art. 24, cada una con métrica, umbral y origen; los datos según ISO/IEC 25012.
- **9.1.4 Modelos de madurez.** Por ejemplo, CMMI-DEV para el proceso, OWASP SAMM para el desarrollo seguro (Art. 4.3) e ISO 9001 como sistema de gestión. Debe ser coherente con lo que declara el SD1.
- **9.1.5 Métricas de código con umbral bloqueante.** Cobertura, complejidad ciclomática, acoplamiento, duplicación y deuda bloqueante, cada una con herramienta y puerta.
- **9.1.6 Métricas de proceso y costo de la calidad.** Las métricas del RT-04.12, defectos escapados y densidad de defectos, más el COQ en HH.

**Figuras y tablas sugeridas** (respetando la §4 y la §5: tablas de hasta 5 columnas, nunca del tipo «Concepto | Descripción»):
- Figura «Marco de calidad»: normas → métricas → control → evidencia → aceptación.
- Figura «Modelo ISO/IEC 25010 aplicado a Puelche», con un umbral por característica.
- Tabla «Característica | Métrica | Umbral | Origen».
- Tabla «Métrica de código | Umbral | Herramienta | Puerta».
- Tabla «Categoría COQ | Paquetes EDT | HH | %».

**Va al anexo:** el catálogo completo de métricas por subcaracterística y el catálogo de reglas de análisis estático.

---

## 3. 9.2 Estrategia de Aseguramiento de Calidad

**Qué exige (Aclaraciones §11 y T-7):**
1. Puertas de calidad, revisión por pares, análisis estático y dinámico.
2. Estrategia de pruebas conforme a **ISO/IEC/IEEE 29119**: niveles, tipos, ambientes, datos de prueba y automatización.
3. Verificación, validación y **trazabilidad** entre requerimiento, diseño, código, prueba y despliegue.

**Qué exigen las Bases:**

| Fuente | Exigencia |
|---|---|
| BA Art. 24 | Cuatro ambientes aislados, con Preproducción equivalente a Producción. CI/CD con reversión automatizada. Revisión obligatoria por pares y ramas protegidas. Regresión automatizada. Carga y estrés a 1,5 × el peak. Resiliencia antes de cada paso a producción y semestral |
| BTT 4.1 | Cinco ambientes con su propósito; los datos de Desarrollo y QA son sintéticos o anonimizados |
| BTT RT-04.03 / .04 / .05 / .08 | Ramas protegidas; trazabilidad requerimiento → incidencia → código → prueba → despliegue; integración continua con compilación, pruebas unitarias, análisis estático, SCA, secretos e imágenes, con bloqueo automático; el mismo artefacto se promueve sin recompilar |
| **BTT 20.1** | **La tabla de 10 tipos de prueba, con su momento y criterio de salida. Es el núcleo de 9.2.3 y no se puede omitir ninguno** |
| BTT RT-20.07 | Definición de terminado acordada con el CLIENTE |
| Caso 17.1 | Cadena de trazabilidad: origen → requisito → componente → paquete EDT → prueba → criterio de aceptación |
| Caso cap. 15 y RT-13.08 | Pruebas en terreno: −22 °C con guantes, turno sin señal |
| Ley 21.719 | Datos personales: no se usan datos productivos sin anonimizar |

**Qué aportan las clases y el PMBOK:**

| Contenido | Fuente | Uso en 9.2 |
|---|---|---|
| Gestionar la calidad (aseguramiento del proceso) frente a controlarla (verificación del entregable) | PMBOK pp. 289–290 | Ordena la sección: puertas y auditorías = aseguramiento; pruebas = control |
| Listas de verificación con los criterios de aceptación | PMBOK p. 292 | Revisión de entregables antes de presentarlos al CLIENTE |
| Auditorías de calidad, independientes | PMBOK pp. 294–295 | Auditoría periódica de la trazabilidad |
| Análisis de causa raíz y diagrama de Ishikawa | PMBOK pp. 292–294 | Defectos recurrentes y escapados |
| Inspección = revisión entre pares | PMBOK p. 303 | Sustento de la revisión por pares |
| Pruebas: unitarias, integración, regresión, caja negra/blanca, alfa, estrés | PMBOK pp. 303–304 | Tipos de prueba de 9.2.3 |
| Muestreo estadístico; hojas de verificación | PMBOK pp. 302–303 | Pruebas manuales y en terreno, verificación de anonimización |
| **Diagrama de control: tolerancia frente a límite de control** | PMBOK pp. 274, 304 | Estabilidad del p95 y de la densidad de defectos |
| Histograma y Pareto de causas | PMBOK pp. 293, 304 | Insumo del comité de calidad |
| Mejora continua con PDCA | PMBOK pp. 275, 296 | Ciclo de acciones correctivas con comprobación de eficacia |
| Lecciones aprendidas y retrospectivas | PMBOK pp. 276, 297, 305 | Al cierre de cada certificación y de cada marcha blanca |
| Solicitudes de cambio → control integrado de cambios | PMBOK p. 296 | Una acción de mejora que toca la línea base pasa por el control de cambios (T-9) |
| Matriz de trazabilidad hacia atrás y hacia adelante; línea base; volatilidad | FEP02 d. 30 | Diseño de la matriz |
| Matriz requisito → componente → nodo → atributo | FEP01 d. 277 | Conectar con SD4 |
| Cadena de cinco eslabones; el quinto es la evidencia | FEP04 d. 88 | Cada eslabón debe apuntar a algo verificable |
| **Controlar la calidad (equipo) frente a validar el alcance (cliente)** | FEP02 d. 44; PMBOK p. 305 | Los entregables verificados pasan a la aceptación del T-17 |
| Criterios de aceptación medibles como diferenciador | FEP04 d. 75 | Argumento para el T-17 |

**Subtítulos propuestos:**
- **9.2.1 Puertas de calidad.** Del commit a la operación: qué bloquea cada puerta y quién puede levantarla.
- **9.2.2 Revisión por pares y análisis estático y dinámico.** Incluye SAST, SCA, DAST, accesibilidad y la aplicación móvil.
- **9.2.3 Estrategia de pruebas conforme a ISO/IEC/IEEE 29119.** Niveles de proceso (organizacional, gestión, dinámico), técnicas de diseño (parte 4), niveles y tipos por ambiente, la tabla BTT 20.1, la carga derivada del dimensionamiento del SD4 y la automatización con su cálculo.
- **9.2.4 Datos de prueba.** Sintéticos desde la volumetría del Caso, anonimización de datos históricos, juegos versionados.
- **9.2.5 Verificación, validación y trazabilidad.** Modelo en V por hito y la cadena completa del Caso 17.1 más el RT-04.04.
- **9.2.6 Control de la calidad, no conformidades y mejora continua.** Ciclo del defecto, severidades alineadas con las del SD4, causa raíz, diagrama de control, PDCA, lecciones aprendidas y solicitudes de cambio.

**Figuras sugeridas:** puertas de calidad en la cadena de entrega; niveles de prueba por ambiente; origen de los datos de prueba; modelo en V con hitos; cadena de trazabilidad con un ejemplo real (retiro sanitario); ciclo de vida del defecto; diagrama de control con un ejemplo.

**Va al T-13:** el plan de pruebas completo: niveles, tipos, ambientes, datos, **criterios de entrada y salida**, automatización y **calendario** de carga, resiliencia, recuperación ante desastres y seguridad ofensiva (BA, Formulario T-13).
**Va al anexo:** la matriz de trazabilidad completa y la especificación de los juegos de datos.

---

## 4. 9.3 Alineación con Plan de Trabajo

**Qué exige (Aclaraciones §11):** dónde quedan las actividades de calidad en la EDT y en el cronograma del Capítulo 7.

**Qué exigen las Bases:**

| Fuente | Exigencia |
|---|---|
| BA Art. 17 y E-25 | Cronograma obligatorio y los 12 hitos |
| BA Art. 18 | Aceptación por hito: 10 días hábiles de revisión y una sola subsanación; repetir la misma observación cuenta como atraso imputable |
| BA Art. 17.3 | Seis condiciones para cerrar la marcha blanca; 0 incidentes críticos o altos abiertos |
| BTT 20.1 | Cuándo se ejecuta cada tipo de prueba |
| RT-07.07, RT-10.07, RT-11.20, RT-07.12 | Pruebas periódicas en la Operación: recuperación ante desastres semestral, resiliencia semestral, intrusión anual, restauración de respaldos mensual |
| Caso B.2 | Congelamientos de septiembre y diciembre |

**Qué aportan las clases y el PMBOK:**

| Contenido | Fuente | Uso en 9.3 |
|---|---|---|
| La planificación de la calidad actualiza la línea base del alcance y el **diccionario de la EDT**, que registra los requisitos de calidad | PMBOK p. 287 | Cada paquete de calidad con su criterio de aceptación en el T-14 |
| Pruebas tempranas abaratan la corrección | PMBOK p. 303 | Justifica la ubicación de las pruebas en el cronograma |
| EDT con el 100 % del alcance; diccionario con criterio de aceptación | FEP02 (sección EDT) | La calidad no puede quedar fuera de la EDT |
| Holguras y ruta crítica | FEP02 d. 62–83; PMBOK cap. 6 | Holgura de cada hito frente a una subsanación |

**Subtítulos propuestos:**
- **9.3.1 Actividades de calidad en la EDT.** Paquetes por cuenta con HH del T-15. Es el insumo del COQ de 9.1.6.
- **9.3.2 Calidad en el cronograma y en los hitos.** Hitos que habilita cada prueba, holgura frente a una subsanación, congelamientos y la regla de correcciones durante la marcha blanca.
- **9.3.3 Pruebas periódicas durante la Operación.** Calendario de los meses 21 a 56.

**Figuras y tablas sugeridas:** Gantt de las actividades de calidad (alineado con la figura del SD7); tabla «Hito | Prueba que lo habilita | Reserva | Holgura».

**Va al T-17:** el protocolo de aceptación de cada hito y del producto final: entregables, criterios objetivos, evidencia, plazos de revisión, procedimiento de observaciones y acta (BA, Formulario T-17; RT-20.08).

---

## 5. Cierre

- **Referencias** (sin numerar, APA 7): toda cita del texto debe estar en la lista y toda entrada de la lista debe citarse. Las Bases se citan con documento, artículo o capítulo y página.
- **Declaración de uso de IA** (sin numerar): un texto breve y luego una tabla con una fila por sección, más una por cada anexo y formulario. La columna «Revisión humana» la completa el grupo; si queda vacía, el SD9 se considera no presentado.

---

## 6. Advertencias para quien redacte

1. **25010: ocho o nueve características.** FEP01 d. 13 presenta la versión 2023, con 9 características y nombres nuevos (capacidad de interacción, flexibilidad, seguridad operacional). El Art. 24 exige **las 8 con los nombres antiguos**. Mandan las Bases: se usan esos 8 nombres y se declara la equivalencia con la versión 2023 en una frase.
2. **Ninguna norma sin su mecanismo** (Art. 4.3): por cada estándar, decir cómo se verifica.
3. **Ninguna cifra sin origen** (Aclaraciones §3): cada umbral sale de las Bases, del Caso o de un cálculo mostrado. La carga de prueba se deriva del dimensionamiento del SD4.
4. **COQ sin dinero** (Art. 50.2): en HH y porcentajes.
5. **Coherencia con otros SD** (§7.1 c): los nombres de ambientes, componentes, roles, hitos, severidades y umbrales deben ser idénticos a los del SD1, SD4, SD6, SD7 y SD8.
6. **Tablas de hasta 5 columnas**, con conclusión escrita después de cada una; **figuras** citadas antes y explicadas después, con su fuente.
7. **Texto de caída** bajo cada título, incluidos los subtítulos.
8. **Evitar las palabras de la §7.1 d** («borrador», «pendiente de validar», etc.) aunque el uso sea legítimo.
