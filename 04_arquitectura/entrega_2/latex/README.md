# Subdocumento 4.1: arquitectura lógica

Versión 0.2 preliminar. Integra `arquitectura_logica_version67.md`, aportado por Álvaro, sobre el preliminar 0.1 y la línea base de Entrega 1. La redacción se reorganiza para explicar primero la responsabilidad y después el componente que la implementa.

## Archivos y compilación

- Narrativa editable: `../texto/arquitectura_logica.md`.
- Versión para la plantilla LafroX: `subdoc_4.1.tex`.
- Compilación desde la raíz: `lualatex --interaction=nonstopmode --synctex=1 main.tex`.
- Repetir la compilación cuando se solicite actualizar índices o referencias. El resultado es `main.pdf` en la raíz.
- Ambos formatos contienen la misma narrativa. Si se edita uno, debe mantenerse el otro sincronizado.

La configuración LuaLaTeX y las recomendaciones de LaTeX Workshop y Live Share se conservan. Para colaborar, abrir la raíz del repositorio en VS Code, iniciar Live Share y compartir una terminal Read/Write solo con las personas autorizadas. No se inicia ni comparte una sesión automáticamente.

## Mejoras incorporadas

| Sección | Cambio |
| --- | --- |
| 4.1–4.2 | Responsabilidades de bodega y nube, seis instalaciones como supuesto y roles diferenciados por sitio. |
| 4.2.5 y 4.3.5 | ERP conservado como único emisor tributario, acceso exclusivo por ACL y flujo SQS → celery-erp-sync → ACL → ERP. Hub EDI GS1 con conectores por cadena y AS2 como transporte. |
| 4.2.6–4.2.7 | Sin Redis local; copia de lectura en SQLite/Room separada de las escrituras pendientes. Identidad central, credenciales de 8/14 horas y acceso de emergencia controlado. |
| 4.2.6–4.2.8 | Funciones de respaldo diferenciadas, recuperación regional condicionada, retención de métricas de 13 meses y distinción entre disponibilidad de infraestructura y de negocio. |
| 4.3–4.6 | Sin IA predictiva en el alcance propuesto, sustitución del WMS en M1/M2/M5, mantenimiento de versiones y límites explícitos de portabilidad. |
| 4.7 | Se conservan 14 imágenes de la biblioteca, identificadas como vistas heredadas pendientes de concordancia con esta revisión. |

## Correcciones de coherencia frente al adjunto

- Se conserva la separación navegador/API/base de datos y el flujo API Gateway → integración privada/ALB → servicio.
- Las tres horas del cross-docking son su ventana operativa (Caso 02, descripción de instalaciones), no una rebaja a la autonomía mínima de 24 horas de RT-03.10.
- El ERP no se reemplaza ni pierde su responsabilidad tributaria. La sustitución gradual corresponde al WMS.
- La actualización de la copia de lectura no borra la cola de eventos pendientes.
- Los 56 meses de contrato no se presentan como soporte garantizado de una sola versión. Tampoco se garantiza un failover de Aurora inferior a 30 segundos ni un RPO remoto de 15 minutos durante un corte prolongado.
- La captura offline del cobro no equivale a autorización bancaria. La ausencia de IA es una decisión de alcance, no una prohibición de RT-18.
- La actualización incremental de BI se mantiene; las tareas pesadas se desplazan fuera de la ventana crítica para no contradecir la latencia operacional de 5 minutos.

## Validaciones pendientes antes de aprobar

1. Demostrar el relevo de turnos durante 24 horas sin IdP, con caché de 8 horas, sin suponer renovación automática de credenciales.
2. Confirmar los 11 roles canónicos y su correspondencia con las 13 vistas de perfiles heredadas.
3. Resolver con el mandante la discrepancia de instalaciones y aprobar las condiciones de recuperación entre regiones y tratamiento de datos.
4. Validar los RTO/RPO, las retenciones, los contratos de pago y las referencias ADR/D citadas por la revisión 67 contra los documentos rectores.
5. Actualizar la concordancia gráfica de las vistas heredadas y verificar la delimitación de IA frente a las innovaciones comprometidas.

La integración se registra como observación 12 de la planilla T-22. No se modifica `entrega_1/`, ningún archivo de arquitectura física ni las imágenes compartidas. Esta revisión no constituye aprobación técnica ni contractual del diseño.
