# Formulario T-10: Metodología para el desarrollo de software

**Licitación:** TFEP-01/2026 — Caso 02: Logística  
**Proponente:** LafroX SpA

Conforme al Formulario T-10 de las Bases Administrativas, LafroX adjunta la información solicitada en el Subdocumento 6, letra b: la sección 6.2, «Metodología de desarrollo de software» ([LAFROX-Subdocumento6.md](LAFROX-Subdocumento6.md#62-metodología-de-desarrollo-software)), desarrollada en detalle en este formulario.

| Contenido | Sección del Subdocumento 6 |
| --- | --- |
| Enfoque RUP iterativo e incremental y sus fases | 6.2 |
| Arquitectura evolutiva, refactorización y deuda técnica | 6.2.1 |
| DevSecOps, integración y entrega continuas, infraestructura como código y pruebas automatizadas | 6.2.2 |
| Ceremonias, artefactos, cadencias y decisiones del desarrollo | 6.2.3 |

## 6.2 Metodología de desarrollo de software

La metodología de desarrollo se coordina con la gestión del proyecto y sus entregas incrementales. Se utiliza **Rational Unified Process (RUP)**, un proceso iterativo e incremental que organiza el desarrollo en cuatro fases y permite gestionar progresivamente requisitos, arquitectura, implementación y pruebas.

La elección de RUP responde a que el proyecto tiene requisitos regulatorios y de continuidad que exigen validar temprano la arquitectura, mantener documentación trazable y realizar entregas formales por etapa, sin renunciar a iteraciones cortas que reduzcan el tiempo hasta disponer de software verificable.

### Fases de RUP

1. **Inicio:** se delimitan el alcance y los objetivos de la solución, se identifican los principales interesados y requisitos, y se elaboran las estimaciones iniciales. También se reconocen los riesgos principales y se establece una visión inicial del producto.
2. **Elaboración:** se profundizan los requisitos, incluidos los casos de uso, y se define la arquitectura de la solución. Se analizan los riesgos prioritarios y se prepara el plan de desarrollo para validar las decisiones de diseño más relevantes antes de construir. Los prototipos con usuarios terminan antes de construir cada módulo.
3. **Construcción:** se desarrollan las capacidades priorizadas mediante iteraciones. En cada iteración se analizan los requisitos correspondientes, se diseña e implementa la solución y se realizan pruebas. Los resultados se revisan con los interesados pertinentes y se ajustan cuando corresponde.
4. **Transición:** se prepara la solución para su uso mediante pruebas de aceptación, resolución de observaciones, preparación de usuarios, marcha blanca y despliegue conforme a los hitos aprobados.

Las iteraciones generan resultados verificables, pero una demostración o incremento no constituye por sí mismo aceptación formal, puesta en producción ni marcha blanca. La marcha blanca y la aceptación formal ocurren en los momentos definidos para cada etapa contractual. Los casos de uso expresan y siguen los requisitos funcionales; la matriz del Formulario T-12 vincula estos requisitos con sus pruebas.

### Etapas, capacidades e iteraciones

La secuencia de iteraciones se coordina con las etapas contractuales:

| Etapa | Capacidades previstas |
| --- | --- |
| **Etapa 1** | Preventa, recepción, bodega, preparación y cross-docking; trazabilidad de lotes y de la cadena de frío; planificación de rutas; confirmación de recepción por los conductores; manejo de efectivo y retiros. |
| **Etapa 2** | Portales e intercambio electrónico con los clientes y, posteriormente, costo de servir. |

La transición se ajusta al cronograma previsto: marcha blanca de la Etapa 1 entre los meses 13 y 15 y paso a producción en el mes 16; marcha blanca de la Etapa 2 en los meses 19 y 20 y paso a producción en el mes 21.

## 6.2.1 Arquitectura evolutiva, refactorización y deuda técnica

La arquitectura se establece durante Elaboración y se aprueba en el hito H2; se valida progresivamente en las iteraciones de Construcción. Cuando nuevos requisitos o resultados de pruebas justifican cambios, la arquitectura se actualiza mediante una nueva versión de la decisión correspondiente en el registro de decisiones de arquitectura del SD4, con fecha, estado y acta del Comité de Arquitectura.

Durante Construcción, el equipo refactoriza el software para mejorar su estructura interna y facilitar su mantenimiento, preservando el comportamiento funcional. Las pruebas automatizadas comprueban que ese comportamiento no haya cambiado.

Las limitaciones o compromisos técnicos que puedan dificultar cambios futuros se registran como deuda técnica, junto con su impacto y prioridad. La deuda que el análisis estático clasifica como bloqueante impide el despliegue. Las demás deudas se planifican en las iteraciones y se revisan en el Comité de Arquitectura.

## 6.2.2 DevSecOps, integración y entrega continuas, infraestructura como código y pruebas automatizadas

### Pipeline y herramientas

Cada cambio pasa por el pipeline de integración continua definido en SD4, sección 4.2. GitLab CI lo orquesta y AWS CodeBuild construye cada imagen de forma hermética, con procedencia SLSA nivel 3. El pipeline ejecuta:

- auditoría de dependencias con `composer audit`;
- pruebas con PHPUnit/PCOV, JUnit 5/Kover, Espresso y Jest;
- análisis estático con PHPStan y Larastan;
- formato con Laravel Pint, detekt, ktlint y ESLint;
- complejidad, duplicación, fronteras modulares y deuda con PHPMD, PHPCPD, PhpMetrics, deptrac y reglas equivalentes en Kotlin/TypeScript;
- pruebas de contrato contra OpenAPI 3.1 y AsyncAPI 2.6;
- SAST/SCA, escaneo de secretos y de imágenes de contenedor con Amazon Inspector/ECR;
- DAST con OWASP ZAP;
- accesibilidad con axe-core y revisión manual;
- carga y estrés con k6;
- resiliencia con AWS Fault Injection Service;
- medición de cobertura.

### Compuertas bloqueantes y coberturas

Las compuertas son obligatorias y bloquean la promoción ante cualquiera de estas condiciones:

- hallazgo de seguridad crítico o alto en dependencias, código, secretos o imagen;
- contrato público roto sin una nueva edición de la interfaz;
- cobertura de la lógica de negocio inferior al **70 %**, conforme a RT-04.11;
- cobertura unitaria global inferior al **80 %**, conforme a la política corporativa de LafroX (paquete 1.5.2);
- deuda técnica bloqueante o una prueba fallida.

Los dos porcentajes son criterios independientes: el 70 % corresponde a cobertura de lógica de negocio según RT-04.11; el 80 % corresponde a cobertura unitaria global según la política de LafroX. No son métricas intercambiables.

### Artefactos, infraestructura y migraciones

La imagen aprobada se firma, se publica en Elastic Container Registry y se promueve entre ambientes por su digest. Así, ningún ambiente recompila la imagen. La infraestructura de los cinco ambientes se describe como código: Terraform administra los recursos con estados separados por ambiente y Ansible configura los hosts. Cada recurso tiene un único propietario de código.

Las migraciones de base de datos siguen la estrategia **expandir y contraer** y declaran su reversión, para permitir gestionar los cambios de esquema de forma compatible y recuperable.

La entrega continua mantiene versiones verificadas y listas para desplegar en cada ambiente. El paso a Producción se ejecuta únicamente dentro de las ventanas permitidas por el caso y, durante el desarrollo, solo en los hitos aprobados. No se despliegan cambios en septiembre, en diciembre ni durante los tres primeros días hábiles de un mes.

## 6.2.3 Ceremonias, cadencias y decisiones del desarrollo

El equipo organiza el trabajo de Construcción en iteraciones de dos semanas.

- **Inicio de iteración:** se revisan requisitos y prioridades, se seleccionan tareas acordes con la capacidad registrada y se aclaran sus criterios de aceptación.
- **Seguimiento:** el equipo utiliza el tablero Kanban para seguir el avance, bloqueos, responsables y dependencias.
- **Cierre:** se demuestra el incremento verificable y se contrasta con sus criterios de aceptación. Cuando corresponde, se presenta a los interesados para recoger observaciones. El equipo revisa dificultades y aprendizajes, y registra acciones de mejora con sus responsables.

La demostración no constituye por sí misma una entrega formal ni una puesta en producción.

### Artefactos de desarrollo

El trabajo mantiene los siguientes artefactos:

- casos de uso;
- matriz de trazabilidad del Formulario T-12;
- registro de decisiones de arquitectura;
- contratos de interfaz;
- registro de deuda técnica;
- informes de pruebas de cada iteración.

### Decisiones y cambios

Las decisiones técnicas necesarias para implementar requisitos se toman dentro del equipo responsable y se documentan cuando afectan la arquitectura, las integraciones, la seguridad o la operación. Las decisiones que cambian la arquitectura pasan por el Comité de Arquitectura.

Si una decisión modifica el alcance, el plazo, los costos o los criterios de aceptación aprobados, se gestiona como solicitud de cambio conforme a la sección 6.1.4.

## Referencias

- Distribuidora Puelche S.A. (2026a). *Bases Administrativas de Licitación N.º TFEP-01/2026*, Formulario T-10.
- LafroX SpA. *Subdocumento 4*, sección 4.2 (arquitectura y pipeline).
- LafroX SpA. *Subdocumento 6*, secciones 6.1.4 (gestión de cambios) y 6.2 (metodología de desarrollo).
- LafroX SpA. *Formulario T-12*, matriz de trazabilidad de requisitos.

## Declaración de uso de IA

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
| --- | --- | --- | --- | --- | --- |
| Formulario T-10 | Claude Code | Portada, correspondencia con la sección 6.2 y adaptación a Markdown del contenido detallado de la metodología | Alto | Ninguno | No documentada |
