# LafroX — Cotejo de trazabilidad contractual SD4

Fecha: 11 de octubre de 2026. Registro de trabajo en `subdoc-4`. Se conserva el estado local de ambos checkouts. Se revisan fuentes Markdown y fragmentos LaTeX actuales; no se modifica T-12 ni el contenido de los entregables.

## Alcance y resultado

- T-12 leído: 645 filas, incluidas las variantes con sufijo `-BTT`; 499 citan SD4. Otras seis citan T-11 sin citar SD4, por lo que el universo ampliado es 505 filas.
- Las 752 menciones explícitas a secciones del cuerpo SD4 se resuelven en 83 encabezados distintos, dentro de sus 108 encabezados numerados. No se encontraron secciones inexistentes en esas menciones.
- Se confirmaron 34 formas de referencia desactualizadas a tablas/figuras, repetidas en 82 citas de 75 filas distintas. La existencia de la sección no subsana el rótulo numérico equivocado.
- El cuerpo efectivo contiene 29 figuras: red general 24, red local 25, conectividad regional 26, arquitectura Talca 27, racks 28 y recinto 29. La numeración de 27 figuras de los registros anteriores es histórica.
- El control estructural cubre todas las filas que citan SD4; el cotejo semántico es dirigido a los casos documentados abajo. No se declara concluida la auditoría semántica de las 499 filas ni se cambian sus estados de cumplimiento.

## Referencias externas que requieren corrección

Los destinos se proponen a partir del título y del tema actual. Si una matriz se convirtió en punteos o se trasladó a anexos, se indica ese destino; no se realiza sustitución aritmética de números. Los casos condicionados requieren leer el requisito antes de editar T-12.

| Cita actual del T-12 | Filas afectadas | Destino vigente / revisión necesaria |
| --- | --- | --- |
| SD4-Anexos 4-O (Tabla A.17) | RF-13.03, RT-02.04 | 4-O, Tabla A.18 (resumen ADR); A.19 para fecha y estado. |
| SD4-Anexos 4-R (Tabla A.23) | RF-14.01-BTT, RF-14.02-BTT, RF-19.01, RF-19.02, RNF-14.04, RNF-14.05, RNF-14.07, RNF-14.09, RNF-15.03, RNF-16.03, RT-11.03, RT-11.05, RT-11.16, RT-11.17, RT-12.09, RT-14.07 | 4-R, Tabla A.25 (controles). A.23 corresponde ahora a amenazas de módulos. |
| SD4 4.2.5.2 (Tabla 19) | RF-14.03-BTT, RF-19.03, RT-11.13 | 4.2.5.2, Tabla 11 (superficie de exposición). |
| SD4-Anexos 4-R (Tabla A.23, controles 5.24 y 5.26) | RF-14.04-BTT, RF-19.04, RT-11.18 | 4-R, Tabla A.25, controles 5.24 y 5.26. |
| SD4-Anexos 4-P (Tabla A.19) y 4-R (Tabla A.23) | RF-15.03 | 4-P, Tablas A.20–A.21 según tecnología y soporte; 4-R, Tabla A.25. |
| SD4 4.2.6.11 (Tabla 31) | RF-17.11, RT-09.01, RT-09.02, RT-09.05, RT-16.27 | 4.2.6.11, Tabla 22 (pruebas de dimensionamiento). |
| SD4-Anexos 4-P (Tabla A.19) | RF-17.13, RNF-21.09, RT-13.10, RT-17.03, RT-17.04, RT-17.05, RT-17.08 | 4-P, Tablas A.20–A.21 según el componente y la vigencia exigidos; verificar el detalle de cada fila. |
| SD4 4.1.17 y 4.2.4.5 (Tabla 17) | RF-18.01, RT-16.18 | 4.1.17 y listado de retención por dominio de 4.2.4.5; completar con 4-U para evidencia documental. |
| SD4 4.2.4.2 (Tabla 15) y 4.2.5.2 (Tabla 19) | RNF-14.03, RT-03.04 | 4.2.4.2, clasificación de servicios en punteos y Tabla 9 de segmentación según requisito; 4.2.5.2, Tabla 11. |
| SD4-Anexos 4-R (Tabla A.23, controles 8.10 y 8.11) | RNF-14.10, RT-11.25 | 4-R, Tabla A.25, controles 8.10 y 8.11. |
| SD4-Anexos 4-T (Tabla A.25) | RNF-16.01, RT-09.01, RT-09.06, RT-09.07, RT-14.03 | 4-T, Tabla A.27 (objetivos y escenarios de desempeño). |
| SD4 4.3.2.4 (Tabla 38) y 4.2.4.3 | RNF-20.01 | 4.3.2.4, Tabla 26 (objetivos de continuidad); conservar 4.2.4.3. |
| SD4 4.1.10 y 4.2.4.3 (Tabla 16) | RNF-20.02 | 4.1.10 y listado de respaldo/restauración por dominio en 4.2.4.3. |
| SD4 4.3.2.4 (Tabla 38) | RNF-20.06, RT-07.04 | 4.3.2.4, Tabla 26 (objetivos de continuidad). |
| SD4 4.2.4.2 (Tabla 15) | RT-02.12 | 4.2.4.2, clasificación de servicios en punteos; Tabla 9 si se busca segmentación. Confirmar intención de cada requisito. |
| SD4 4.2.4.5 (Tabla 17) | RT-05.10 | 4.2.4.5, listado de retención por dominio; ya no es Tabla 17. |
| SD4-Anexos 4-P (Tabla A.20) | RT-05.16 | 4-P, Tabla A.22 si la remisión busca la implementación lógica Laravel; A.20 es ahora el ciclo de soporte. |
| SD4 4.3.1.4 (Figura 25) | RT-06.02, RT-06.03, RT-06.22, RT-06.30 | 4.3.1.4, Figura 29 (recinto). |
| SD4 4.3.1.4 (Figura 24) | RT-06.05 | 4.3.1.4, Figura 28 (racks). |
| SD4 4.3.1.4 (Tabla 34) | RT-06.11, RT-08.01 | 4.3.1.4, Tabla 23 (carga eléctrica). |
| SD4 4.3.1.4 (Tabla 35) | RT-06.13 | 4.3.1.4, Tabla 24 (carga térmica). |
| SD4 4.3.2.2 (Tabla 36) | RT-07.02 | 4.3.2.2, Tabla 25 (distancias y amenazas comunes). |
| SD4 4.3.2.3 (Tabla 37) | RT-07.03 | 4.3.2.3, listado de replicación/RPO por dominio. |
| SD4 4.3.2.5 (Tabla 39) | RT-07.05 | 4.3.2.5, secuencia de conmutación en punteos. |
| SD4-Anexos 4-W.8 (Tablas A.34 y A.35) | RT-08.01 | 4-W.8, Tablas A.38 (VM) y A.39 (carga/UPS); comprobar cuál respalda cada magnitud. |
| SD4 4.2.4.3 (Tabla 16) | RT-08.03, RT-10.01, RT-10.02 | 4.2.4.3, listado de respaldo/restauración por dominio. |
| SD4 4.2.6.10 (Tabla 30) | RT-08.05, RT-09.02, RT-09.03 | 4.2.6.10, Tabla 21 (umbrales en percentil 95). |
| SD4 4.2.1.1 (Tabla 7) | RT-08.07 | Inventario trasladado a 4-W/Tabla A.35; conservar justificación de 4.2.1.1 y T-11. |
| SD4 4.2.4.1.1 (Tabla 13) | RT-09.04 | 4.2.4.1.1, Tabla 8 (ventanas de despliegue). |
| SD4 4.2.6.9 (Tabla 29) | RT-09.04 | 4.2.6.9, Tabla 20 (proyección y crecimiento). |
| SD4 4.1.19 (Tabla 6) | RT-09.05 | 4.1.19, Tabla 5 (primer cuello de botella). |
| SD4 4.2.6.12 (Tabla 32) | RT-09.06, RT-09.07, RT-09.08 | Síntesis trasladada a 4-W/Tabla A.30; conservar remisión de 4.2.6.12. |
| SD4 4.2.4.1.4 (Tabla 14) | RT-10.05 | 4.2.4.1.4 y Tabla 9 (direccionamiento/segmentación). |
| SD4-Anexos 4-R (Tabla A.23, controles 8.29, 8.31 y 8.32) | RT-11.27 | 4-R, Tabla A.25, controles 8.29, 8.31 y 8.32. |

## Cotejo semántico dirigido y condiciones de cierre

| Requisito / tema | Evidencia localizada en SD4 y T-11 | Resultado del cotejo / cierre necesario |
| --- | --- | --- |
| RF-01.04, fotografía de no conformidad | 4.1.4.8 y T-11 C-03 estándar premium con cámara trasera de 16 MP. | La configuración antes omitida está declarada. Mantener prueba de captura; no se verificó aquí la ficha externa del fabricante. |
| RF-09.04, frío en 28 camiones | 4.1.4.2, 4-W.4 y T-11 B-03: 18 propios más 10 externos. | Cobertura del parque documentada; lectura, asociación al camión y continuidad durante ruta requieren ensayo. |
| RF-09.05, alerta en cabina y plataforma | T-12 declara BLE al TC58e y reenvío inmediato con cobertura o al recuperarla. | La alerta local tiene recorrido; la plataforma depende de cobertura. Registrar esa limitación al cotejar la exigencia de tiempo real; no afirmar recepción remota durante un aislamiento. |
| RF-09.06, bloqueo y disposición sanitaria | 4.1.4.2 y 4-N identifican A-01/A-02/C-03 y permisos de Calidad; M9 conserva bloqueo preventivo. | Hay realización local declarada, pero falta evidencia de aceptación del recorrido de identidad, permiso, disposición y auditoría; no atribuir la decisión al conductor. |
| RT-03.10, 24 h local y 14 h de terreno | 4.1.15, 4.2.2.7, 4-J/4-M y AL-OFF-01. | Captura y relevo documentados. Despacho depende de guía válida preemitida; cambio de carga exige ERP/servicio tributario. El ensayo debe incluir esa condición. |
| RT-03.13, sincronización y funciones no disponibles | 4.1.15–16, 4-J/4-K y 4-W.6; caudal por simultaneidad y acuse durable. | Cubre ambos significados del código. Los plazos de 10 min/2 h siguen sujetos a medición y reconciliación; el promedio horario no basta. |
| RT-03.24, QoS y estudio de cámaras | 4.2.5.1 desarrolla prioridades; 4.2.1.2 y supuestos S-36 describen estimación y estudio inalámbrico. | El T-12 cita 4.2.4.2 y 4.3.1.4, que no son las referencias más precisas para ambos mecanismos. Añadir los apartados específicos y evidencia de estudio/aceptación; no tratar la estimación de AP como cobertura medida. |
| RT-04.02, equivalencia de Preproducción | 4.1.9 usa 207 terminales; 4.2.4.1 declara diferencias; T-11 y 4-W distinguen 207 al inicio y 235 en año 3. | El parque inicial tiene respaldo y el crecimiento está derivado. Aclarar qué campaña prueba cada parque; no confundir diferencia temporal con concurrencia nocturna de 186. |
| RT-06.02/03/05/22/30, recinto y racks | Los objetos están presentes en 4.3.1.4, figuras 28 y 29. | Error de referencia confirmado en T-12; no equivale a ausencia de los objetos. La revisión gráfica de requisitos materiales sigue pendiente. |
| RT-06.11/13, carga eléctrica y climatización | 4.3.1.4, Tablas 23–24 y memoria 4-W.8. | Hay cálculo/diseño; referencias de T-12 desactualizadas. No acredita medición real ni aceptación de equipos. |
| RNF-20.06 y RT-07.04, RTO/RPO | 4.3.2.3–4, AL-DR-01, exclusión del escritor y restitución de conectividad de Talca. | Brecha contractual real ante aislamiento total seguido de destrucción; su registro en R8-05 no autoriza la excepción. Los estados Cumple del T-12 requieren decisión y justificación antes de acreditar conformidad incondicional. |
| RT-07.05/07, conmutación y pruebas | 4.3.2.5–7 y protocolos AL-DR-01; consulta sanitaria regional prevista en 75 min. | Procedimiento y objetivos documentados; falta evidencia de conmutación real, RTO/RPO y consulta sanitaria completa en menos de 2 h. |
| RT-05.10, linaje y retención | 4.2.4.5 conserva retención por dominio; T-12 declara falta de catálogo con linaje automatizado. | Mantener separación: retención documentada no cierra el linaje faltante. No elevar la fila parcial por actualizar su referencia. |
| RT-16.16, cifrado e integridad de documentos | La cita A.15 de 4-N lleva a una matriz de módulos, no al detalle de custodia. 4.1.17, 4-U y retención 4.2.4.5 desarrollan la evidencia. | Cita existente pero insuficientemente específica. Añadir evidencia directa de cifrado, integridad y retención, además del recurso físico. |
| RT-16.18, conservación tras vencer certificado | 4.1.17 y 4-U; T-12 menciona XML, acuse, hash, marca temporal y cadena de verificación. | El respaldo documental está descrito; la simple marca temporal de un registro no demuestra por sí sola el sello exigido. Cotejar protocolo/autoridad temporal y prueba de verificación posterior antes de cerrar. |

## Preservación y reproducibilidad

Las huellas siguientes identifican los archivos leídos para este corte. Si otra tarea modifica sus fuentes, recalcular los conteos y destinos antes de cerrar un pendiente.

| Fuente leída | SHA-256 |
| --- | --- |
| T-12 | `569d66f0745a264e61a3453df7c4f814cd6144d007ab924b20967db9890cc21c` |
| SD4 | `0198286485d3fbc4737cd31f9b139904f0a80f4ddb2c5f278ee148bb44ffc3cb` |
| SD4-Anexos | `255a3f999aa4fc4dde5f0a452ff6cd60f41f72d16ef6a44323ac853e222d898a` |
| T-11 | `0b5e92d68c7f00ee8e654ae21386820d57538bf25c75bf24d25fd5b3f4ba83c0` |

Filas distintas con referencias desactualizadas: RF-13.03, RF-14.01-BTT, RF-14.02-BTT, RF-14.03-BTT, RF-14.04-BTT, RF-15.03, RF-17.11, RF-17.13, RF-18.01, RF-19.01, RF-19.02, RF-19.03, RF-19.04, RNF-14.03, RNF-14.04, RNF-14.05, RNF-14.07, RNF-14.09, RNF-14.10, RNF-15.03, RNF-16.01, RNF-16.03, RNF-20.01, RNF-20.02, RNF-20.06, RNF-21.09, RT-02.04, RT-02.12, RT-03.04, RT-05.10, RT-05.16, RT-06.02, RT-06.03, RT-06.05, RT-06.11, RT-06.13, RT-06.22, RT-06.30, RT-07.02, RT-07.03, RT-07.04, RT-07.05, RT-08.01, RT-08.03, RT-08.05, RT-08.07, RT-09.01, RT-09.02, RT-09.03, RT-09.04, RT-09.05, RT-09.06, RT-09.07, RT-09.08, RT-10.01, RT-10.02, RT-10.05, RT-11.03, RT-11.05, RT-11.13, RT-11.16, RT-11.17, RT-11.18, RT-11.25, RT-11.27, RT-12.09, RT-13.10, RT-14.03, RT-14.07, RT-16.18, RT-16.27, RT-17.03, RT-17.04, RT-17.05, RT-17.08.

No se ejecutaron ensayos, compilación ni revisión visual nueva del PDF. El estado semántico completo de las 499 filas sigue pendiente; este registro permite priorizar y revisar las correcciones externas de T-12.
