# Revisión interdocumental posterior a la conciliación de frío

## Dictamen

La contradicción de cadena de frío entre SD4, SD13, T-19 y la respuesta RT-26.01 del T-12 se corrigió documentalmente. No se presenta esta corrección como aceptación del CLIENTE, revisión humana ni ensayo ejecutado. La oferta conserva otras brechas: no se declara admisible en su conjunto.

## Alcance y fuentes

- Bases Administrativas, Bases Técnicas Transversales, Caso 02 y Aclaraciones conservadas en `Bases/`.
- Relectura de los hallazgos sobre las ramas de subdocumentos inventariadas en Git; los originales históricos no se convierten en la versión final por su nombre o fecha.
- Correcciones en `subdoc-4` y en los worktrees asociados a `LafroX-Subdoc13-LateX` y `LafroX-Subdoc3-LateX`. No se hizo push.
- **SD7, SD8 y SD9 no se editaron.** Por instrucción expresa, no se concilian en esta tarea HH, simulaciones, calendario ni cobertura de T-13. SD7 cambió durante el trabajo: su rama remota cacheada avanzó de `240e7e02` a `dd7bee76`; no se reutiliza el dictamen anterior de H12 como si describiera necesariamente esa revisión.
- Las referencias `origin/*` son las disponibles en este repositorio; no se hizo fetch ni se afirma que sean el último estado del servidor remoto.

## Corrección de arquitectura aplicada

| Tema | Resultado |
|---|---|
| Captura de cámara | Se conserva B-01/B-02, sin sustituir la solución vigente. |
| Captura de camión | Kit B-03 a B-15; B-04 procesa tres PT100 mediante B-05/B-06. |
| Segunda evaluación | C-02/B-08 independiente; latido firmado por Wi-Fi cada 10 s y lectura con antigüedad máxima de 30 s. |
| Aviso remoto | Móvil e Iridium SBD en paralelo para alarmas y órdenes; no se espera al retorno para alertar. |
| Sin ambos caminos | Continúan protección, retención y evidencia local; no se promete aviso remoto inmediato. |
| Confirmación | M9 persiste evento y obligación de aviso antes de A2. |
| Duplicados | Productor, arranque y secuencia concilian lo recibido por ambos transportes. |
| Series y lotes | SSCC, cámara–andén–compartimento, origen de sensor y versiones; contraste de originales B-03/B-08 y serie B-04. |
| Volumetría | 30.548 mensajes/día y 127.848 lecturas/día. Los 8.120 mensajes SBD de transporte no se suman como eventos nuevos. |
| INN-03 | Reutiliza la captura obligatoria; el modelo no libera cargas bloqueadas, sustituye FEFO ni prolonga la fecha impresa. |
| Efecto económico | No se vuelve a cargar el kit ni su conectividad a la innovación. El procesamiento derivado se separa de la vigilancia y se contrasta con la capacidad; no se inventan mediciones ni precios. |
| Pruebas | Se identifican RF-09.11–RF-09.14, RNF-09.06–RNF-09.09 y V1–V21 en la delimitación de alcance de SD13. No se alteró T-13, expresamente fuera de alcance. |

Se actualizaron el texto, la ficha 3 del T-19, el contrato y las matrices de anexos de SD13; INT-IOT, OBS-LOCAL y el recorrido de INN-03 del Anexo 4-N; el emplazamiento de camiones; y cuatro vistas utilizadas por los documentos. Los PDF y las fuentes gráficas originales se conservaron. Las vistas generales nuevas son propias, no recortes: muestran las ocho capas/doce módulos y los emplazamientos concretos, con referencias al detalle de capas y al Anexo 4-N.

El T-12 conserva sus 653 filas y el texto de todas las exigencias. Solo cambia RT-26.01: su respuesta ya corresponde a las fuentes conciliadas y pasa a **Cumple documentalmente** según la semántica de la matriz. No se cambiaron los estados de seguridad, hardware, calidad, riesgo ni planificación. Resultado agregado: 596 Cumple, 35 Cumple parcialmente y 22 No cumple; **no es un puntaje de evaluación ni una certificación contractual**.

## ¿Son resolubles las cuatro brechas de seguridad?

No se ha acreditado una imposibilidad general de la solución, pero no se pueden cerrar todas solo mediante redacción. No se aplicó un rediseño de seguridad en esta tarea.

| Brecha | Vía de solución y condición de cierre | Estado |
|---|---|---|
| RT-12.03 — MFA externo | Especificar la política para cada perfil humano: clientes, proveedores, representantes de transportistas, administradores y terreno. Keycloak admite flujos obligatorios de segundo factor. La API debe comprobar el nivel de autenticación; no basta confiar en lo solicitado por el navegador. En terreno se necesita prueba de posesión de la clave del terminal más factor personal, no solo afirmar que está enrolado. Separar identidades técnicas B2B de sesiones humanas. Verificar alta, renovación, recuperación y revocación. | **Vía técnica disponible; pendiente de implementación documental y pruebas.** |
| RT-11.07 — AS2 | Recanalizar su publicación a una entrada protegida por CloudFront/WAF y bloquear el acceso directo al origen; conservar en OpenAS2 la validación criptográfica y de negocio. Probar mensajes firmados/cifrados, cabeceras MIME/AS2, POST, MDN síncrono/asíncrono, tamaño, tiempos y rechazo de bypass. WAF no equivale a validación del contenido AS2 cifrado. | **Viable como cambio de diseño; no probado ni aplicado.** |
| RT-11.08 — TLS 1.3 y legado | Comprobar los endpoints y bibliotecas reales del ERP y de cada contraparte. Si soportan TLS 1.3, actualizar configuración/conector y ensayar. Un proxy que mantiene un tramo TLS 1.2 no acredita TLS 1.3 extremo a extremo. Si un tercero o el ERP no lo soporta dentro del alcance permitido, se necesita una solución de integración compatible o una aclaración formal; no se presupone la aprobación de una excepción. | **Cierre condicionado a compatibilidad y alcance; no garantizado hoy.** |
| RT-11.04 — Parches y congelamiento | Diseñar emergencia, reversión y responsables para cumplir 7/15/30 días. Si el congelamiento contractual prohíbe la intervención necesaria, debe resolverse formalmente esa prioridad antes de ofertar; la simple aceptación de riesgo del CLIENTE no elimina el máximo exigido. No se promete autorización que no existe. | **Necesita conciliación técnica y contractual; no cerrado.** |

Fuentes primarias consultadas:

- [Keycloak — flujos de autenticación](https://www.keycloak.org/docs/latest/server_admin/index.html#_authentication-flows).
- [AWS WAF — recursos compatibles](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html): incluye CloudFront y ALB, no habilita asociar WAF directamente a un NLB.
- [CloudFront — comportamiento de solicitudes a orígenes](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorCustomOrigin.html): métodos y cabeceras requieren configuración; el transporte no se da por compatible sin ensayo.

## Revisión completa: situación de los hallazgos

| Hallazgo | Situación posterior |
|---|---|
| Marcadores de IA de SD4 | El commit `5667161b` ya los había retirado. Se comprueba su ausencia en el PDF actual; esta tarea no inventa ni amplía una revisión humana previa. |
| Cadena de frío SD4/SD13/T19/T12 | **Corregida documentalmente**, con los límites de verificación indicados. |
| Cronograma / H12 | **Fuera de alcance por edición concurrente de SD7**. No se modifica ni se declara cerrado. |
| Seguridad RT-11.04/.07/.08 y RT-12.03 | **Abierta**; factibilidad y condiciones detalladas arriba. |
| Especificación de hardware | **Abierta**. T-11 se conserva como control sin cambios de contenido; no se inventaron marcas/modelos ni ensayos para cerrar prestaciones aún no acreditadas. |
| Conciliación SD9/T-13, HH y simulaciones SD8 | **Excluida expresamente** de las correcciones mientras se edita SD7. |
| Variantes de SD8 y nomenclatura | **Pendiente de selección e integración**: no mezclar identificadores o PDF de ramas diferentes. Los nombres de archivo deben cumplir las Aclaraciones §1 y BA art. 40.4. |
| Habilitantes BA art. 34 | **No acreditados íntegramente en la evidencia examinada**. Las declaraciones de SD1/T-6 no sustituyen certificados, cartas y demás respaldos exigidos. No se afirma falsedad ni ausencia definitiva. |
| Video y prototipo | **No acreditados por la matriz disponible**; no se inventa su entrega ni se equiparan con una intención de desarrollar pruebas durante el contrato. |
| SD10–SD12 y SD14 | Las ramas consultadas no acreditan el paquete final desarrollado. No es por sí solo una omisión del Informe 2, cuyo alcance fija T-22; sí debe resolverse para la propuesta final. |

BA art. 58 excluye ítem bajo 30, total ponderado bajo 60, subdocumento obligatorio omitido o mínimos transversales no acreditados. Las Aclaraciones §7.1 tienen un régimen específico desde el Informe 2. No se asignan puntajes hipotéticos ni se equiparan requisitos deseables con causales automáticas de exclusión.

## Evidencia reproducible y límites

- `verificar_coherencia_frio.py` comprueba contratos documentales, las 653 filas, preservación de originales, fuentes vectoriales, apertura de PDF, texto seleccionable y foliación.
- `VERIFICACION_COHERENCIA_FRIO_2026-10-25.json` registra resultados, páginas y SHA-256 de los PDF efectivos, incluido T-11 como control.
- Resultado final: **54 comprobaciones correctas y siete PDF verificados**; seis entregables actualizados y T-11 conservado sin cambios de contenido. Sin referencias indefinidas ni caracteres faltantes en las compilaciones finales. El cuerpo de SD4, SD13, sus anexos y T-19/T-12 no presentan desbordes nuevos. El Anexo 4-A, no editado, conserva cuatro avisos de 1,23–1,52 pt por `TC58e` en su tabla de eventos; quedan identificados como observación de maquetación, no como una prueba de inadmisibilidad.
- En las tres vistas actualizadas de SD4 se verificaron tamaños mínimos de letra de 9,16 pt (general lógica), 9,20 pt (borde) y 11,31 pt (general física) dentro del PDF de entrega.
- En SD3, `revision/CONCILIACION_FRIO_RT26_2026-10-25.json` conserva el antes/después de la única fila modificada.
- Revisión visual de las figuras nuevas y de páginas afectadas de cuerpos, anexos y formularios. La inspección visual se complementa con medición de letra, no con una declaración genérica de legibilidad.
- No se ejecutaron pruebas físicas de kits, conexiones satelitales, integración con ERP/contrapartes, cotizaciones, certificaciones ni aprobación del CLIENTE. La revisión humana posterior de los cambios debe realizarla el equipo; no se acredita con compilación o auditoría asistida.
- Se conservan los archivos de trabajo ajenos `reports/` y `research_notes/` y las ediciones concurrentes de otras ramas. No se realizó commit ni push de esta corrección.
