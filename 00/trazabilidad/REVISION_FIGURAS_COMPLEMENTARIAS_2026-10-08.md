# Revisión de las figuras complementarias de 4.1

Rama: `subdoc-4`. El usuario autorizó ejecutar el plan de validación, sustitución y retiro de las figuras identificadas por su numeración anterior: 2, 6, 9, 10 y 14.

## Decisiones e integración

| Figura anterior | Decisión | Figura actual | Fundamento |
| --- | --- | --- | --- |
| 2 — Vista resumida | Retirada del cuerpo | Sin sustitución | La vista general, la introducción de las capas y las ocho vistas detalladas ya cumplen esa función. Se conserva el resumen textual. |
| 6 — Acceso local durante 24 horas | Rehecha | 5 | Explica preparación de identidad, verificación en relevos y recuperación. No duplica la topología de la capa 3. |
| 9 — Pedido con conexión | Rehecha | 8 | Secuencia de componentes y confirmación durable; no repite todo el ciclo operacional de SD3. |
| 10 — Pedido sin conexión | Rehecha | 9 | Distingue captura pendiente, sincronización, deduplicación y confirmación; utiliza los mismos participantes que la secuencia conectada. |
| 14 — Modelo conceptual | Reformulada | 13 | Vista de entidades, propietarios y contratos de eventos. El detalle relacional, atributos y cardinalidades corresponden a SD5. |

La numeración actual se genera automáticamente en LaTeX. Se mantienen los identificadores de las cuatro figuras sustituidas y se retira `fig:arql-1`, correspondiente a la vista resumida. Se ajustaron sus referencias previas y explicaciones posteriores. Los originales continúan conservados en `04/figuras/logica/`; retirarlos del cuerpo no borra sus archivos. El general y las ocho vistas por capa permanecen íntegros.

## Fundamento y límites del alcance

Se contrastaron las Aclaraciones, secciones de diagramas y capítulos 3, 4 y 5, RT-02.13 de las Bases Técnicas Transversales, el cuerpo MD disponible del SD3 y la copia local `05/salida/LAFROX-Subdocumento5.pdf`. Esta copia de SD5 es material de comparación, no evidencia de que sea la última versión publicada; no se edita ni se incorpora a Git en esta tarea.

La continuidad local se sustenta en 4.1.3.3 y 4.1.3.7: Keycloak es el único IdP, el manifiesto firmado cubre 26 horas con renovación horaria cuando hay enlace, la caché de identidad conserva TTL de 24 horas y el verificador no crea identidades. Las funciones locales incluyen recepción física de retornos de M8 y acciones autorizadas de M9. Se elimina del diagrama la cantidad de 120 HHT para no confundir los 120 preparadores con los 186 terminales del dimensionamiento físico. No se cambian cantidades ni realizaciones físicas.

Las secuencias se sustentan en 4.1.4, «Reserva comercial y retención física por sitio», y en INT-03/04 del Anexo 4-G. M2 central solo confirma después del acuse durable del sitio. El shipper recoge solicitudes por conexión saliente de la cola de coordinación; el dibujo representa mensajes lógicos, no conexiones entrantes desde nube. La línea del sitio agrupa su shipper, broker y M2. La transacción local conserva retención, auditoría y outbox. Sin acuse, el pedido permanece pendiente; los reenvíos conservan UUID y resultado. Las secuencias terminan en confirmación y habilitación de preparación; M4 y M10 figuran como consumidores en el texto. Calidad y la guía válida del ERP continúan condicionando la salida y se explican en su apartado específico.

La vista de dominio conserva el alcance de RT-02.13 mediante entidades, responsables e intercambios, sin reproducir un segundo modelo relacional. El ERP mantiene maestros autorizados y emisión tributaria. M3 es productor de `PedidoConfirmado` y M6 de `EntregaRegistrada`, conforme al Anexo 4-A. Compartir Laravel no habilita escritura en datos privados de otro módulo. El POD se distingue del DTE y del acuse.

## Estándar gráfico y archivos

Se utilizó como referencia `04/figuras/fuentes/Arquitectura-logica-general-y-8-capas.drawio.xml`: Arial, colores de actores, módulos como contextos delimitados, servicios locales verdes, identidad violeta y bordes ortogonales. Se reutilizó el icono de Keycloak del XML aprobado. Las secuencias emplean líneas de vida y mensajes por su propósito específico; no se fuerzan a una vista estática por capas. Las cuatro vistas son páginas independientes, no recortes. Los títulos formales y las fuentes quedan fuera de las imágenes.

- Editable: `04/figuras/fuentes/Arquitectura-logica-vistas-complementarias.drawio.xml`, cuatro páginas.
- Publicación: cuatro PDF vectoriales en `04/figuras/logica/complementarias/`.
- Previsualizaciones y comprobación: `output/pdf/figuras-complementarias/`, fuera del repositorio.
- Integración: `04/partes/4.1_logica/04_capas_de_la_arquitectura.tex` y `06_modelo_de_datos_conceptual.tex`.

## Revisión

### Precisión posterior de la figura 9

Se ajustan únicamente tres etiquetas de la secuencia sin conexión: «turno de 14 h» identifica el período de captura; «AL RECUPERAR LA CONEXIÓN» introduce el envío por `/sync/v1`; y la nota final explicita que los eventos se conservan hasta recibir confirmación con el mismo UUID. Se mantienen participantes, flechas, geometría y tamaño de letra. El texto técnico ya describía estas reglas y no requiere cambios.

La revisión visual corrigió texto fuera de recuadros, etiquetas sobre flechas y exceso de altura de la secuencia offline. Se comprobaron flechas, direcciones de confirmación, participantes, títulos y fuentes. Las cuatro vistas alcanzan letra mínima de 9 puntos en el documento impreso; el informe reproducible `output/pdf/figuras-complementarias/verificacion-final.json` registra sus páginas y medidas. Se comprueba además ausencia del símbolo de sección, referencias indefinidas y desbordamientos `Overfull`, y preservación exacta del XML aprobado del general.

Esta validación corresponde al contenido y presentación de las cuatro vistas nuevas. No acredita pruebas operacionales ni aprobación humana del equipo. La legibilidad impresa pendiente del general y de algunas vistas por capa anteriores conserva su estado; no se amplían ni se rediseñan en esta tarea. No se modifican fuentes de 4.2, 4.3, anexos ni formularios, ni archivos de `rama-md`. No se hace commit ni push.
