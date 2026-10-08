# LafroX — Resumen del Subdocumento 6: Metodologías

[Índice de resúmenes](README.md) · [Documento original](../06_metodolog%C3%ADas/LAFROX-Subdocumento6.md)

## Para qué sirve

Define cómo se dirige el proyecto y cómo se desarrolla el software. SD7 convierte estas prácticas en paquetes, responsables y fechas; T-9 y T-10 remiten a las dos metodologías.

## Gestión del proyecto

[La gestión](../06_metodolog%C3%ADas/LAFROX-Subdocumento6.md#61-metodolog%C3%ADa-de-gesti%C3%B3n-de-proyectos) adapta el **PMBOK**: líneas base de alcance y calendario, control de cambios, gestión de interesados, comunicaciones, compras, riesgos y calidad. El tablero Kanban ordena el trabajo cotidiano; las decisiones contractuales siguen necesitando sus instancias y actas.

El avance se mide con **valor ganado**: se reconoce trabajo aceptable en puntos definidos, sin equiparar horas consumidas a resultados terminados. La Tabla 6.4 ilustra un corte de mes 10 con SPI 0,95 y CPI 0,97, índices de avance y eficiencia de esfuerzo; son un ejemplo de control, no mediciones de ejecución. Los comités revisan dependencias, observaciones y desviaciones. El seguimiento es semanal, el Comité de Proyecto quincenal y las instancias ejecutiva, de arquitectura y operación tienen cadencias mensuales según su ámbito. Las actas de comité se levantan dentro de **dos días hábiles**.

## Desarrollo iterativo y entrega

[El desarrollo](../06_metodolog%C3%ADas/LAFROX-Subdocumento6.md#62-metodolog%C3%ADa-de-desarrollo-software) usa **RUP**, proceso iterativo con Inicio, Elaboración, Construcción y Transición. La arquitectura se valida temprano y el software avanza en iteraciones de **dos semanas**, con demostración y revisión del incremento. La deuda técnica y los ajustes de arquitectura quedan registrados.

[DevSecOps](../06_metodolog%C3%ADas/LAFROX-Subdocumento6.md#622-devsecops-integraci%C3%B3n-y-entrega-continuas-infraestructura-como-c%C3%B3digo-y-pruebas-automatizadas) incorpora seguridad y pruebas en la entrega. GitLab CI y CodeBuild construyen un artefacto verificable, que se promueve sin recompilar entre ambientes. Se bloquea la promoción ante fallas, contratos rotos, hallazgos altos/críticos o deuda bloqueante. Los umbrales distinguen **70 % de cobertura de lógica de negocio** exigida y **80 % de cobertura unitaria del código modificado** como política corporativa.

## Compras y condiciones de ejecución

[Las adquisiciones](../06_metodolog%C3%ADas/LAFROX-Subdocumento6.md#613-gesti%C3%B3n-de-adquisiciones) asignan responsable, fecha necesaria, dependencia y evidencia de recepción. El documento asigna al CLIENTE la compra del terreno y sala técnica; LafroX especifica e instala. Para las certificaciones contempla refuerzo de Calidad con evaluadores subcontratados hasta **16 por día** en las ventanas indicadas.

## Relaciones y aspectos pendientes

T-14 describe entregables y T-15 programa personas y revisión del CLIENTE. La Tabla 6.3 ubica necesidad de equipamiento de sala en **mes 5**, mientras la secuencia del T-15 adelanta su habilitación a meses **3–4**. Además, T-11 declara provisión on-premise por el adjudicatario, frente a la compra de sala asignada al CLIENTE aquí. Son diferencias documentales que requieren coordinación; el resumen conserva ambas fuentes.

La metodología es una propuesta de ejecución. Los ensayos, la dotación nominal y la revisión humana pendiente no se consideran cumplidos por estar descritos.

---

**Fuente y actualización:** documento local vigente al 8 de octubre de 2026. Resumen elaborado con asistencia de Codex; no acredita aprobación del CLIENTE ni revisión humana adicional.
