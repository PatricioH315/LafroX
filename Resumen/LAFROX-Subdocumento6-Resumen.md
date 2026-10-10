# LafroX — Resumen del Subdocumento 6: Metodologías

[Índice de resúmenes](README.md) · [Documento original](../06_metodolog%C3%ADas/LAFROX-Subdocumento6.md)

## Para qué sirve

Define cómo se dirige el proyecto y cómo se desarrolla el software. SD7 convierte estas prácticas en paquetes, responsables y fechas; T-9 y T-10 desarrollan, respectivamente, el detalle de gestión y desarrollo que SD6 sintetiza.

## Gestión del proyecto

[La gestión](../06_metodolog%C3%ADas/LAFROX-Subdocumento6.md#61-metodolog%C3%ADa-de-gesti%C3%B3n-de-proyectos) adapta el **PMBOK**: líneas base de alcance y calendario, control de cambios, gestión de interesados, comunicaciones, compras, riesgos y calidad. El tablero Kanban ordena el trabajo cotidiano; las decisiones contractuales siguen necesitando sus instancias y actas.

El avance se mide con **valor ganado**, sin equiparar horas consumidas a resultados terminados. SD6 remite al **T-9** para el cálculo, los umbrales, los plazos de recuperación, las matrices de interesados/comunicaciones y la composición y cadencia exactas de los comités. Su sección 6 reconoce HH en puntos definidos; SPI o CPI <0,90, o desviación >10 %, exige plan de recuperación en cinco días hábiles. El seguimiento semanal no sustituye las decisiones formales ni sus actas.

## Desarrollo iterativo y entrega

[El desarrollo](../06_metodolog%C3%ADas/LAFROX-Subdocumento6.md#62-metodolog%C3%ADa-de-desarrollo-software) usa **RUP**, proceso iterativo con Inicio, Elaboración, Construcción y Transición. La arquitectura se valida temprano y el software avanza en iteraciones regulares, cuya cadencia de **dos semanas**, demostración y revisión se detallan en **T-10**. La deuda técnica y los ajustes de arquitectura quedan registrados.

[DevSecOps](../06_metodolog%C3%ADas/LAFROX-Subdocumento6.md#622-devsecops-integraci%C3%B3n-y-entrega-continuas-infraestructura-como-c%C3%B3digo-y-pruebas-automatizadas) incorpora seguridad y pruebas en la entrega. SD6 sintetiza compuertas y promoción de artefactos sin reconstrucción; **T-10** detalla GitLab CI, CodeBuild, firma, infraestructura como código y migraciones reversibles. Se bloquea la promoción ante fallas, contratos rotos, hallazgos altos/críticos o deuda bloqueante. Los umbrales distinguen **70 % de cobertura de lógica de negocio** exigida y **80 % de cobertura unitaria global** como política corporativa.

## Compras y condiciones de ejecución

[Las adquisiciones](../06_metodolog%C3%ADas/LAFROX-Subdocumento6.md#613-gesti%C3%B3n-de-adquisiciones) asignan responsable, fecha necesaria, dependencia y evidencia de recepción. El CLIENTE compra el equipamiento de terreno conforme a las especificaciones de LafroX. Para los equipos de la sala, incluidos racks, servidores y borde, SD6 indica orden de compra de LafroX en **mes 2** e instalación en **mes 3**; la recepción de la sala es en **mes 4**. La recepción técnica de equipos y su commissioning son hitos distintos, sin fecha especificada aquí. El registro completo está en **T-9**. LafroX contrata cinco enlaces Starlink. T-15 contempla refuerzo de Calidad con evaluadores subcontratados hasta **16 por día** en las ventanas indicadas. El SOC 24×7 subcontratable es condicional y RT-11.17 conserva cumplimiento parcial por ubicación no declarada; no se acredita contratación.

## Relaciones y aspectos pendientes

T-14 describe entregables y T-15 programa personas y revisión del CLIENTE. Las adquisiciones y reglas de valor ganado se consultan en T-9, no en las antiguas Tablas 6.3 y 6.4. Las referencias a T-14/T-15 orientan la programación, sin convertir una fecha de recepción de sala en recepción técnica o puesta en servicio de todos los equipos.

La metodología es una propuesta de ejecución. Los ensayos, la dotación nominal y la revisión humana pendiente no se consideran cumplidos por estar descritos.

---

**Fuente y actualización:** documento local vigente al 8 de octubre de 2026. Resumen elaborado con asistencia de Codex; no acredita aprobación del CLIENTE ni revisión humana adicional.
