# LafroX — Subdocumento 9: Anexos

Licitación TFEP-01/2026 · Caso 02 — Logística · Distribuidora Puelche S.A.

Estos anexos contienen el detalle que el cuerpo del Subdocumento 9 (SD9) resume. El plan de pruebas está en el Formulario T-13 y el protocolo de aceptación, en el Formulario T-17. En estos anexos, BA, BTT y Caso designan las Bases Administrativas (Distribuidora Puelche S.A., 2026a), las Bases Técnicas Transversales (2026b) y las Bases Técnicas del Caso 02 (2026c).

| Anexo | Contenido | Sección del SD9 que lo cita |
|---|---|---|
| 9.A | Métricas de calidad del producto por característica de ISO/IEC 25010 y de calidad de datos según ISO/IEC 25012 | 9.1.3 |
| 9.B | Puertas de calidad, reglas de bloqueo y herramientas por lenguaje | 9.1.5 y 9.2.1 |
| 9.C | Cálculo del costo de la calidad en horas-hombre | 9.1.6 y 9.3.1 |
| 9.D | Trazabilidad de los resultados del caso hasta su prueba y su hito | 9.2.5 |

---

## Anexo 9.A — Métricas de calidad del producto

Las métricas siguen el modelo de calidad del producto de ISO/IEC 25010 (International Organization for Standardization [ISO] & International Electrotechnical Commission [IEC], 2011) y el modelo de calidad de datos de ISO/IEC 25012 (ISO & IEC, 2008). Cada métrica indica su umbral, su origen, el método con que se verifica, el ambiente y el paquete del Formulario T-14 donde se ejecuta. Los nombres de las características son los del Art. 24 de las Bases Administrativas.

### 9.A.1 Funcionalidad

| ID | Subcaracterística | Métrica | Umbral | Origen | Verificación | Paquete |
|---|---|---|---|---|---|---|
| 9A-01 | Completitud | Requisitos ofertados del T-12 con prueba aprobada | 100 % | Caso, 17.1 | Matriz de trazabilidad generada desde la cadena de integración | 3.8.1; 3.9.1 |
| 9A-02 | Corrección | Defectos críticos o altos abiertos al certificar | 0 | Art. 17.3 | Registro de defectos | 3.8.7; 3.9.6 |
| 9A-03 | Pertinencia | Casos de aceptación firmados por la Contraparte Técnica | 100 % de los casos de la etapa | BTT 20.1 | Aceptación en Preproducción | 3.8.2; 3.9.2 |

### 9.A.2 Desempeño

| ID | Subcaracterística | Métrica | Umbral | Origen | Verificación | Paquete |
|---|---|---|---|---|---|---|
| 9A-04 | Comportamiento temporal | p95 de confirmación de línea de preparación | ≤ 1 s | Caso, RT-09.01 | Carga a 21,99 TPS | 3.8.4; 3.9.3 |
| 9A-05 | Comportamiento temporal | p95 de registro de entrega | ≤ 2 s | Caso, RT-09.01 | Carga a 21,99 TPS | 3.8.4; 3.9.3 |
| 9A-06 | Comportamiento temporal | p95 de línea de preventa | ≤ 1,5 s | Caso, RT-09.01 | Carga a 21,99 TPS | 3.8.4; 3.9.3 |
| 9A-07 | Comportamiento temporal | p95 de consulta de stock y crédito | ≤ 2 s | Caso, RT-09.01 | Carga a 21,99 TPS | 3.8.4; 3.9.3 |
| 9A-08 | Comportamiento temporal | p95 de transacción crítica de terreno, portal, navegación y API | ≤ 3 s; ≤ 2 s; ≤ 1 s; consulta ≤ 500 ms; escritura ≤ 800 ms | BTT, cap. 9; SD4, Tabla 31 | Carga a 21,99 TPS | 3.8.4; 3.9.3 |
| 9A-09 | Capacidad | Carga sostenida sin violar 9A-04 a 9A-08 | 21,99 TPS; 1.163 personas usuarias; 237 dispositivos | Art. 24; RT-09.06; SD4, Tabla 33 | Carga en PRE-C | 3.8.4; 3.9.3 |
| 9A-10 | Capacidad | Ventana de despacho a 1,5 × su peak | 10,41 TPS durante 90 minutos, 0 minutos de indisponibilidad | Caso, RT-10.05; SD4, Tabla 33 | Carga en PRE-C | 3.8.4; 3.9.3 |
| 9A-11 | Capacidad | Crecimiento sin rediseño | 43,98 TPS (3 × el peak) sin cambio de arquitectura | RT-09.03 | Escalón de estrés | 3.8.4; 3.9.3 |
| 9A-12 | Capacidad | Degradación al superar la capacidad | 0 transacciones perdidas; encolamiento y mensaje explícito | RT-09.08 | Escalón de quiebre (4 ×) | 3.8.4; 3.9.3 |

### 9.A.3 Compatibilidad

| ID | Subcaracterística | Métrica | Umbral | Origen | Verificación | Paquete |
|---|---|---|---|---|---|---|
| 9A-13 | Interoperabilidad | Flujos de integración ejecutados sin error | 15 de 15 | BTT 20.1; SD4, sección 4.1 | Integración en QA | 3.8.1; 3.9.1 |
| 9A-14 | Interoperabilidad | Contratos rotos en la cadena de integración | 0 | Art. 4.3 (OpenAPI 3.1, AsyncAPI 2.6) | Pact y Spectral | 1.5.2 |
| 9A-15 | Coexistencia | Regresiones de la Etapa 1 al integrar la Etapa 2 | 0 | Art. 17.2, regla 3 | Regresión de la Etapa 1 | 3.9.1 |

### 9.A.4 Usabilidad

| ID | Subcaracterística | Métrica | Umbral | Origen | Verificación | Paquete |
|---|---|---|---|---|---|---|
| 9A-16 | Accesibilidad | Incumplimientos de WCAG 2.2 A y AA | 0, con informe de conformidad | RT-13.01; Art. 4.3 | axe-core y revisión manual | 3.8.2; 3.9.2 |
| 9A-17 | Operabilidad | Condiciones de terreno superadas: guantes a −22 °C, lluvia, sobre 34 °C, sol directo, una mano | 5 de 5 | Caso, RT-13.08 | Prueba de perfil operacional | 3.8.3 |
| 9A-18 | Eficiencia de uso y aprendizaje | Tiempo, pasos, tasa de error y tiempo de aprendizaje por perfil | Valores comprometidos en el paquete 2.6.3 | RT-13.04 | Pruebas moderadas por perfil | 2.6.3; 3.8.2 |
| 9A-19 | Adaptabilidad de la interfaz | Funciones completas en escritorio, tableta y teléfono | 100 % de las vistas de portales y consolas | RT-13.02 | Regresión visual con Playwright | 3.8.1; 3.9.1 |

### 9.A.5 Fiabilidad

| ID | Subcaracterística | Métrica | Umbral | Origen | Verificación | Paquete |
|---|---|---|---|---|---|---|
| 9A-20 | Disponibilidad | Disponibilidad mensual por nivel de servicio | Crítico ≥ 99,9 %; alto ≥ 99,5 %; medio ≥ 99,0 %; bajo ≥ 98,0 % | Art. 78.2; SD4, Tabla 16 | Observabilidad en marcha blanca y Operación | 4.2.1; 4.3.1; Operación |
| 9A-21 | Disponibilidad | Indisponibilidad entre 05:30 y 07:00, lunes a sábado | 0 minutos | Caso, RT-10.05 | Indicador diario de la marcha blanca | 4.2.1; 4.3.1 |
| 9A-22 | Tolerancia a fallos | Escenarios de inyección superados sin intervención | 6 de 6 (T-13, sección 7.2) | RT-10.07 | AWS FIS y sitio emulado | 3.8.4; 3.9.3; 8.2.2 |
| 9A-23 | Recuperabilidad | RTO y RPO en conmutación real | RTO ≤ 4 h; RPO ≤ 15 min | RT-07.04; RT-07.07 | Conmutación regional | 3.8.5; 3.9.4; 8.1.3 |
| 9A-24 | Recuperabilidad | Restauraciones mensuales exitosas, con tiempo medido | 100 % | RT-07.12 | Restauración de muestra | Marcha blanca; 8.1.6 |
| 9A-25 | Operación desconectada | Registros perdidos o duplicados tras 14 h sin señal y 24 h sin enlace | 0; sincronización ≤ 10 min (dispositivo) y ≤ 2 h (centro de distribución) | Caso, RT-03.10 y RT-03.13 | Perfil operacional y resiliencia | 3.8.3; 3.8.4 |

### 9.A.6 Seguridad

| ID | Subcaracterística | Métrica | Umbral | Origen | Verificación | Paquete |
|---|---|---|---|---|---|---|
| 9A-26 | Resistencia | Hallazgos críticos o altos abiertos (SAST, SCA, DAST, imágenes, intrusión) | 0 | RT-04.05; RT-11.20 | Cadena de integración; tercero independiente | 1.5.2; 3.8.6; 3.9.5; 8.2.2 |
| 9A-27 | Resistencia | Plazo de corrección de hallazgos | Crítico 7 días corridos; alto 15; medio 30 | BA, Art. 21.1; SD4, sección 4.2.4.1.4 | Registro de vulnerabilidades | 8.2.2 |
| 9A-28 | Confidencialidad | Datos productivos sin anonimizar fuera de Producción | 0; 0 hallazgos de Amazon Macie | Ley N.º 21.719; Caso, RT-11.10 | Verificación previa a la liberación de cada juego | Todas las campañas |
| 9A-29 | Confidencialidad | Secretos en código, imágenes o configuración | 0 | RT-04.09 | Escaneo de secretos | 1.5.2 |

### 9.A.7 Mantenibilidad

| ID | Subcaracterística | Métrica | Umbral | Origen | Verificación | Paquete |
|---|---|---|---|---|---|---|
| 9A-30 | Testeabilidad | Cobertura de la lógica de negocio | ≥ 70 % | Art. 24; RT-04.11 | PHPUnit con PCOV; Kover; Jest | 1.5.2 |
| 9A-31 | Testeabilidad | Cobertura unitaria global | ≥ 80 % | Política de LafroX (SD1, 1.3.1) | Ídem | 1.5.2 |
| 9A-32 | Analizabilidad | Complejidad ciclomática por método | ≤ 10 | McCabe (1976) | PHPMD; detekt; ESLint | 1.5.2 |
| 9A-33 | Modularidad | Dependencias prohibidas entre módulos | 0 | Art. 19 (acoplamiento débil) | deptrac; detekt; ESLint | 1.5.2 |
| 9A-34 | Modificabilidad | Duplicación de código | ≤ 3 % de las líneas | Formulario T-10 | PHPCPD; jscpd | 1.5.2 |
| 9A-35 | Modificabilidad | Deuda técnica clasificada como bloqueante | 0 | Art. 24; Formulario T-10 | PhpMetrics y registro de deuda | 1.5.2; 8.2.4 |

### 9.A.8 Portabilidad

| ID | Subcaracterística | Métrica | Umbral | Origen | Verificación | Paquete |
|---|---|---|---|---|---|---|
| 9A-36 | Instalabilidad | Despliegues que promueven el mismo artefacto sin recompilar | 100 % | RT-04.08 | Digest de la imagen en cada ambiente | 3.8.8; 3.9.7 |
| 9A-37 | Adaptabilidad | Ambientes reconstruibles desde código | 5 de 5 | BTT 4.1 | Reconstrucción de las instancias de Preproducción por campaña | 3.1 |
| 9A-38 | Reemplazabilidad | Despliegue y reversión sin interrupción | 0 interrupciones; 0 intervenciones manuales | RT-04.06; RT-04.07 | Demostración en Preproducción | 3.8.8; 3.9.7 |

### 9.A.9 Calidad de datos (ISO/IEC 25012)

| ID | Dimensión | Métrica | Umbral | Origen | Verificación | Paquete |
|---|---|---|---|---|---|---|
| 9A-39 | Completitud | Recepciones con lote registrado, en productos que lo requieren | 100 % | Caso, cap. 18, resultado 2 | Indicador de la marcha blanca | 4.2.1 |
| 9A-40 | Exactitud | Diferencias no explicadas en la conciliación de la migración | 0 | BTT 20.1; SD5, 5.3.5 | Dos ensayos y corte | 3.7.2 a 3.7.5 |
| 9A-41 | Consistencia | Definiciones del indicador de entregas completas y a tiempo | 1 sola | Caso, cap. 18, resultado 4 | Revisión del modelo analítico | 4.2.1 |
| 9A-42 | Actualidad | Latencia de los indicadores de la operación del día | ≤ 5 min | Caso, RT-05.29 | Medición en marcha blanca | 4.2.1 |

---

## Anexo 9.B — Puertas de calidad y reglas de bloqueo

| Puerta | Momento | Reglas que bloquean | Herramienta (PHP · Kotlin · TypeScript) | Quién puede levantar el bloqueo |
|---|---|---|---|---|
| G0 | Compromiso local | Formato; pruebas del módulo en falla | Laravel Pint · ktlint · ESLint; pruebas unitarias | Nadie; se corrige |
| G1 | Solicitud de fusión | Falta la aprobación de un par; secreto detectado; error de lint | Revisión en GitLab; escaneo de secretos | Nadie |
| G2 | Integración continua | 9A-30 a 9A-35 incumplidos; hallazgo crítico o alto de SAST o SCA; contrato roto (9A-14); prueba en falla | PHPStan con Larastan, PHPMD, PHPCPD, PhpMetrics, deptrac · detekt, Kover, jscpd · ESLint, Jest; SAST de GitLab; `composer audit`; Pact; Spectral | Nadie |
| G3 | Promoción a QA | Imagen con vulnerabilidad crítica o alta; regresión de desempeño: p95, errores o colas de la carga de regresión peores que en la última versión aceptada, bajo la misma carga y configuración (SD4, sección 4.2.4.1.4) | Amazon Inspector; k6 | Nadie; se corrige |
| G4 | Promoción a Preproducción | Regresión con fallas; alerta alta de DAST o MobSF; incumplimiento de WCAG 2.2 AA; defecto crítico o alto abierto | Playwright; Espresso; OWASP ZAP; MobSF; axe-core | Nadie |
| G5 | Paso a producción contractual (H7 y H12) | Una prueba del T-13 que habilita el paso no está aprobada; defecto crítico o alto abierto; falta el acta de la Contraparte Técnica | Expediente del T-17 | Nadie. El acta es una condición adicional y no levanta una prueba fallida |
| G6 | Operación | Canario con p95 sobre su umbral o con más errores que la versión estable; presupuesto de error crítico del mes agotado | Cadena de entrega del SD4; observabilidad | Nadie. La reversión del canario es automática; se suspenden los despliegues no correctivos hasta el mes siguiente |

Los umbrales de las puertas son **tolerancias**: el rango que un requisito acepta, como el p95 de 1 s de la línea de preparación. Son distintos de los **límites de control** de la sección 9.2.6 del SD9, que se calculan con la variación histórica de una métrica y sirven para detectar un proceso inestable antes de que llegue a la tolerancia (PMI, 2017, pp. 274 y 304).

---

## Anexo 9.C — Costo de la calidad en horas-hombre

El costo de la calidad se expresa en horas-hombre y no en dinero, porque la Oferta Técnica no puede contener cifras que permitan inferir el monto de la oferta (Art. 50.2). Las categorías son las del PMBOK: prevención, evaluación y fallas (PMI, 2017, pp. 274 y 282–283).

### 9.C.1 Costos de conformidad (programados en la línea base)

| Categoría | Paquete T-14 | Contenido | HH (T-15) |
|---|---|---|---|
| Prevención | 1.2.4 | Matriz de trazabilidad | 80 |
| Prevención | 1.5.1 | Plan de calidad y de pruebas | 80 |
| Prevención | 1.5.2 | Puertas de calidad automáticas | 80 |
| Prevención | 2.6.1 a 2.6.3 | Investigación con usuarios, prototipos e indicadores de usabilidad | 720 |
| Prevención | 3.10.2.1 a 3.10.2.4 | INN-02: reproducción de incidentes de terreno | 960 |
| Prevención | 8.2.4 | Registro y reducción de la deuda técnica en la Operación | 2.304 |
| **Subtotal prevención** | | | **4.224** |
| Evaluación | 3.8.1 a 3.8.8 | Pruebas y certificación de la Etapa 1 | 2.080 |
| Evaluación | 3.9.1 a 3.9.7 | Pruebas y certificación de la Etapa 2 | 1.760 |
| Evaluación | 4.1.2 | Ensayo del procedimiento de reversión | 80 |
| Evaluación | 8.1.3 | Pruebas de recuperación ante desastres en la Operación | 80 |
| Evaluación | 8.1.6 | Restauraciones mensuales en la Operación | 576 |
| Evaluación | 8.2.2 | Vulnerabilidades, intrusión anual e inyección de fallas | 1.152 |
| Evaluación | 8.3.1 | Regresión de INN-02 en la Operación | 576 |
| **Subtotal evaluación** | | | **6.304** |
| **Total de conformidad** | | | **10.528** |

Las 10.528 HH equivalen al 4,9 % de las 216.935 HH de la línea base (10.528 / 216.935 = 0,0485).

**Partidas excluidas.** No se cuentan la migración de datos (cuenta 3.7), cuyos ensayos forman parte del trabajo de migración y no se pueden separar de él, ni la certificación de los usuarios del CLIENTE (7.3.1 y 7.3.2), que verifica personas y no el producto.

### 9.C.2 Costos de no conformidad (esperados en la reserva de contingencia)

| Categoría | Riesgo del SD8 | Evento | HH esperadas (SD8, Anexo 8.B, Tabla B.2) |
|---|---|---|---|
| Falla interna | R8-31 | Observaciones de revisión que obligan a repetir una certificación | 153,60 |
| Falla interna | R8-18 | Marcha blanca que no cumple las seis condiciones del Art. 17.3 | 2.956,80 |
| **Total esperado de fallas internas** | | | **3.110,40** |

Las fallas externas, es decir, los defectos que encuentra el CLIENTE después de la aceptación, se corrigen dentro del mantenimiento correctivo y evolutivo (8.2.1), que no separa ambas clases de trabajo. Por eso no se estiman en horas: se miden en la Operación con la métrica de defectos escapados del SD9, sección 9.1.6, y quedan acotadas por los niveles de servicio del Art. 78.

### 9.C.3 Distribución

| Categoría | HH | Proporción |
|---|---|---|
| Prevención | 4.224,00 | 31,0 % |
| Evaluación | 6.304,00 | 46,2 % |
| Fallas internas esperadas | 3.110,40 | 22,8 % |
| **Total** | **13.638,40** | **100,0 %** |

Proporciones: 4.224 / 13.638,4 = 0,310; 6.304 / 13.638,4 = 0,462; 3.110,4 / 13.638,4 = 0,228.

---

## Anexo 9.D — Trazabilidad de los resultados del caso

La matriz de trazabilidad completa es el entregable del paquete 1.2.4 (H1) y se genera desde el repositorio: cada caso de prueba lleva el identificador de su requisito, cada solicitud de fusión cita el requisito o la incidencia que atiende y cada despliegue registra el digest de su imagen (RT-04.04). En la oferta, la correspondencia entre requisito, componente y sección está en el Formulario T-12.

Este anexo muestra el tramo final de la cadena del Caso, 17.1, para los dieciséis resultados de aceptación: de cada resultado a la prueba que lo ensaya antes de la marcha blanca, al paquete donde se mide y al hito que lo acepta.

| Resultado | Prueba previa (T-13) | Paquete de medición | Hito de aceptación |
|---|---|---|---|
| R18-01 Retiro sanitario en < 2 h | Simulacro sobre datos sintéticos (sección 7.4) | 4.2.1 | H7 |
| R18-02 100 % de recepciones con lote | Casos de recepción; 9A-39 | 4.2.1 | H7 |
| R18-03 Registro continuo de temperatura | Series con excursiones controladas; bloqueo del despacho (sección 7.4) | 4.2.1 | H7 |
| R18-04 OTIF medido de una forma | Revisión del modelo analítico; 9A-41 | 4.2.1 y Operación | Por tramo (meses 15, 19 y 32) |
| R18-05 Stock y crédito en la preventa | 9A-07 | 4.2.1 | H7 |
| R18-06 Ningún pedido perdido sin señal | Jornada de 14 h sin señal (sección 7.3); 9A-25 | 4.2.1 | H7 |
| R18-07 Ruta en < 20 min | Generación con volumen de peak (sección 7.4) | 4.2.1 | H7 |
| R18-08 Prueba de entrega digital el mismo día | Casos de entrega en aceptación | 4.2.1 | H7 |
| R18-09 Cero guías extraviadas o ilegibles | Casos de emisión y consulta de guías | 4.2.1 | H7 |
| R18-10 Rendición cuadrada el mismo día | Casos de cierre por camión | 4.2.1 | H7 |
| R18-11 Costo de servir por cliente | Casos de la Etapa 2 en aceptación | 4.3.1 | H12 |
| R18-12 Control de envases | Casos de saldo por cliente y transportista | 4.2.1 y Operación | H7 (provisional); tras 12 meses de operación, mes 32 (final) |
| R18-13 Pedidos EDI de cadenas | Contratos de integración EDI; 9A-13 | 4.3.1 | H12 |
| R18-14 Ocupación mínima por camión | Casos de planificación de carga | 4.2.1 | H7 |
| R18-15 Causa de cada faltante | Casos de faltante sin conexión | 4.2.1 | H7 |
| R18-16 Operación sin el planificador | Generación automática de rutas (R18-07) | 4.2.1 | H7 |

---

## Referencias

- Distribuidora Puelche S.A. (2026a). *Bases Administrativas, Licitación TFEP-01/2026*.
- Distribuidora Puelche S.A. (2026b). *Bases Técnicas Transversales, Licitación TFEP-01/2026*.
- Distribuidora Puelche S.A. (2026c). *Bases Técnicas del Caso 02 — Logística*.
- International Organization for Standardization & International Electrotechnical Commission. (2008). *ISO/IEC 25012:2008. Software engineering — Software product Quality Requirements and Evaluation (SQuaRE) — Data quality model*.
- International Organization for Standardization & International Electrotechnical Commission. (2011). *ISO/IEC 25010:2011. Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models*.
- Ley N.º 21.719. (2024). *Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales*. Diario Oficial de la República de Chile.
- McCabe, T. J. (1976). A complexity measure. *IEEE Transactions on Software Engineering, SE-2*(4), 308–320.
- Project Management Institute. (2017). *Guía de los fundamentos para la dirección de proyectos (Guía del PMBOK)* (6.ª ed.). Project Management Institute.
