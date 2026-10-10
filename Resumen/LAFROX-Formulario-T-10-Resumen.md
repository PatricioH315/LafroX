# LafroX — Resumen del Formulario T-10: Metodología de desarrollo

[Índice de resúmenes](README.md) · [Formulario original](../06_metodolog%C3%ADas/LAFROX-Formulario-T-10.md)

## Para qué sirve

Desarrolla en detalle la metodología de desarrollo de software que SD6 sintetiza. Explica cómo se construye, valida y entrega cada incremento, sin confundir una demostración con aceptación formal.

## Cómo leerlo

La tabla inicial relaciona el contenido con [la sección 6.2 del SD6](../06_metodolog%C3%ADas/LAFROX-Subdocumento6.md#62-metodolog%C3%ADa-de-desarrollo-software). El propio formulario desarrolla 6.2 (RUP, fases y etapas), 6.2.1 (arquitectura evolutiva, refactorización y deuda técnica), 6.2.2 (DevSecOps, pruebas e infraestructura como código) y 6.2.3 (ceremonias, artefactos y decisiones).

**RUP** organiza Inicio, Elaboración, Construcción y Transición. **DevSecOps** incorpora seguridad y operación al proceso de construir y entregar; la entrega continua prepara versiones verificadas para su promoción por ambientes.

## Compromisos esenciales

Las iteraciones de **dos semanas** producen software demostrable y se revisan con criterios de aceptación, sin constituir por sí mismas una entrega formal. La arquitectura se aprueba en H2; sus cambios se registran y pasan por el Comité de Arquitectura.

GitLab CI y CodeBuild construyen la imagen que se firma y promueve por digest, sin recompilar entre ambientes. Las compuertas bloquean pruebas fallidas, hallazgos altos/críticos, contratos rotos sin nueva edición, deuda bloqueante y coberturas insuficientes: **70 % de lógica de negocio** y **80 % de líneas del código modificado** son criterios independientes. Terraform y Ansible gestionan infraestructura/configuración; las migraciones siguen expandir y contraer con reversión. Las liberaciones respetan hitos y ventanas permitidas.

El formulario no inventa un proceso distinto del capítulo ni acredita que las pruebas estén ejecutadas. La revisión humana de su declaración de IA sigue pendiente. El [resumen del SD6](LAFROX-Subdocumento6-Resumen.md) explica umbrales y gobierno; SD4 identifica herramientas y T-14 programa sus entregables.

---

**Fuente y actualización:** documento local vigente al 8 de octubre de 2026. Resumen elaborado con asistencia de Codex; no acredita aprobación del CLIENTE ni revisión humana adicional.
