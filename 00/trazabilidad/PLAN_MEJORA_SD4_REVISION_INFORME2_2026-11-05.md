# LafroX — Plan de mejora exclusivo de la sección 4.1

Fecha de actualización: 5 de noviembre de 2026.

Registro interno de planificación de arquitectura lógica. Conserva el nombre del plan anterior para mantener la continuidad, pero su alcance vigente es exclusivamente 4.1 y sus anexos lógicos pertinentes. Las correcciones se implementarán en fuentes LaTeX, fuentes de figuras y sus PDF; no se utilizarán espejos Markdown de subdocumentos.

## 1. Alcance vigente

El plan contiene **11 mejoras: 8 técnicas y 3 transversales aplicadas únicamente a 4.1**, además de 2 tareas de preparación y verificación. Se conservan los identificadores originales para mantener la trazabilidad con el plan amplio anterior.

Incluido:

- Texto de `04/partes/4.1_logica/`.
- Partes de `04/anexos/logica/partes/` que sustentan arquitectura lógica, contratos, controles, soporte y pruebas de 4.1.
- Figuras lógicas y sus fuentes editables, preservando originales, vistas de Tomás y recortes aprobados.
- Referencias utilizadas por 4.1 y las filas de declaración de IA correspondientes a 4.1 y a los anexos intervenidos, aunque estén en archivos compartidos.
- Este registro interno y la trazabilidad de respuestas sobre 4.1.
- Compilación del cuerpo y anexos ensamblados para verificar el contenido lógico, sin modificar por ello el contenido de otras secciones.

Fuera del alcance:

- Fuentes y figuras de 4.2 y 4.3, arquitectura física y centros de datos.
- T-11 y su PDF, memoria física y Anexo 4-W.
- Compras, alternativa de residencia, plano de sala, cobertura Wi-Fi, reposición de hardware, Figura 18 y tabla de TPS.
- Otros subdocumentos, formularios y ramas; las filas 4.2, 4.3 y T-11 de declaraciones compartidas.

Se retiran del plan activo M02–M06, M14, M17, M18 y M21. La versión amplia anterior queda conservada en el respaldo previo. M10, M12, M15, M16, M19 y M20 quedan restringidas por los límites indicados en cada acción.

Una inconsistencia fuera de alcance se documenta como hallazgo interno. Si impide resolver una mejora lógica, esta permanece abierta; no se amplía el alcance ni se declara resuelto el contenido externo. La ejecución documental posterior se registra en la sección 9; los límites de alcance se mantienen.

## 2. Rama y línea base

- Checkout: `D:/Usuario/Documents/Proyecto_Lafrox/LafroX-rama-latex`.
- Rama madre: `LafroX-Subdoc4-LateX`.
- Pull realizado contra `origin/LafroX-Subdoc4-LateX`: sin novedades; la rama estaba al día.
- Rama hija activa: `LafroX-Subdoc4.1-LateX-corrigiendo`, creada desde la rama madre después del pull.
- Commit de creación: `b68ba316d61b7c2d8b129fc16c4a468b22fd4b50`.
- Fecha declarada de oferta en el ensamblador actual: 12 de octubre de 2026; volver a comprobar antes de verificar versiones.
- Cambios locales heredados: `04/AGENTS.md`, `04/formularios/T11/15_anexo_t11.tex`, `entrega/LAFROX-Formulario-T-11.pdf` y archivos sin seguimiento. Se preservan; su existencia no incorpora T-11 al alcance.
- Respaldo previo: `D:/Usuario/Documents/Proyecto_Lafrox/tmp/sd41_preparacion_20261105_204550/`. Incluye inventario con huellas de 206 archivos locales, diferencias de archivos versionados y copia del plan amplio. El inventario no es una copia completa de cada archivo sin seguimiento.
- Fuente principal: `revision_informe_2.md`, apartado SD4.1 y observaciones generales/transversales aplicables.
- Bases y aclaraciones: versiones pertinentes del checkout. `aclaraciones_informe_3.md` se consulta solo en lo aplicable a trazabilidad de respuestas; no incorpora trabajo económico.
- PDF de referencia: cuerpo de 194 páginas y anexos de 117. Los localizadores se comprobarán después de editar.

No se crean commits ni se publica la rama como parte de esta preparación. Los responsables funcionales del plan son propuestas, no designaciones personales. No se fijan HH o fechas sin antecedentes reales.

## 3. Fundamentos lógicos que deben conservarse

1. Monolito modular M1–M12, límites de contexto, contratos y perfiles de ejecución.
2. ERP como único emisor tributario y guía preemitida para despacho sin enlace.
3. Retención térmica local y liberación exclusiva por Calidad con evidencia y permisos válidos.
4. Operación local, reconciliación, outbox e idempotencia durante cortes.
5. Keycloak como autoridad central; la caché descriptiva no emite ni renueva sesiones.
6. Interfaces y registro de alternativas y decisiones de arquitectura.

Toda modificación de política debe tener impacto y evidencia lógica trazables, sin alterar por esta vía las secciones físicas excluidas. Se cotejarán las decisiones históricas con los ADR actuales; una fecha por sí sola no acredita vigencia o aprobación.

## 4. Secuencia

| Etapa | Acciones | Resultado |
| --- | --- | --- |
| A. Preparación | M01 | Línea base protegida y archivos permitidos identificados. |
| B. Continuidad y trazabilidad | M07–M10 | Requisitos críticos verificables y políticas lógicas consistentes. |
| C. Fundamentación y vistas | M11–M13, M15 | Selección tecnológica sustentada y vista general legible. |
| D. Síntesis y declaración | M16, M19, M20 | Fuentes precisas, texto depurado y revisión declarada con veracidad. |
| E. Verificación | M22 | Evidencia de cierre y preservación de contenido excluido. |

M11–M12 pueden adelantarse tras M01. La Figura 1 se finaliza después de estabilizar nombres, tecnologías y políticas. La síntesis y los localizadores definitivos se completan al final.

## 5. Ocho mejoras técnicas de 4.1

### M07 — Trazabilidad individual de requisitos críticos

- Prioridad alta. Responsable propuesto: arquitectura lógica.
- Motivo: el Anexo 4-E agrupa familias; la revisión pide poder comprobar la correspondencia individual con módulos y capas.
- Trabajo: incorporar requisitos críticos individuales con origen, módulo/componente lógico, capa, contrato/interfaz, prueba, criterio medible y localizador exacto del detalle completo. La agrupación puede conservarse como síntesis.
- Archivos: `04/anexos/logica/partes/06_anexo_4_1_e_trazabilidad_funcional.tex`, partes pertinentes de 4-D/4-F/4-N/4-V y `04/partes/4.1_logica/05_modulos_funcionales_y_limites_de_contexto.tex`.
- Límite: citar la matriz maestra y la realización física existente como antecedentes, sin modificarlas si quedan fuera de alcance.
- Cierre: recorrido origen → módulo → capa → contrato/control → prueba → aceptación. Distinguir prueba diseñada de ejecutada. La copia local incluye familias RF-01 a RF-19; no eliminarlas porque la reseña mencione hasta RF-17.

### M08 — Precisar identidad y manifiesto durante cortes

- Prioridad alta. Responsable propuesto: identidad y seguridad lógica.
- Motivo: demostrar operación autorizada durante el corte, con relevos y vencimientos.
- Diagnóstico: el Anexo 4-M, página 34 del PDF de referencia, ya contiene AL-OFF-01 con manifiesto de 26 h, corte de 24 h y relevos a las 8/16 h. Se completa esa evidencia; no se declara inexistente.
- Trabajo: precisar emisión, renovación previa, antigüedad máxima al corte y vigencia remanente; diferenciar manifiesto, caché de 24 h y credencial personal. Verificar firma, turno, rol, sitio, dispositivo, reloj, reinicio, PIN inválido, expiración y reconexión. Explicar las revocaciones que el nodo aislado no puede conocer y la exposición residual.
- Archivos: `04/partes/4.1_logica/04_capas_de_la_arquitectura.tex`, ADR-06 y partes lógicas de 4-J/4-M/4-R/4-V.
- Cierre: política única y protocolo con entradas, pasos, denegaciones, auditoría y criterios medibles. No prometer revocación remota inmediata sin enlace ni atribuir ensayos ejecutados sin evidencia.

### M09 — Cubrir la ruta de 14,5 h con autorización válida

- Prioridad alta. Responsable propuesto: movilidad e identidad. Dependencia: M08.
- Motivo: una asignación de 14 h puede vencer antes de terminar una ruta declarada de 14,5 h.
- Trabajo: separar autonomía contractual mínima, duración operacional, autorización por turno y exposición por pérdida del terminal. Definir la política sin depender de renovación en línea durante el corte; evaluar vencimiento y límites de seguridad.
- Archivos: `04/partes/4.1_logica/19_identidad_y_ciclo_de_vida_de_conductores_externos.tex` y partes de 4-J/4-M/4-R/4-V.
- Límite: no cambiar baterías, hardware, cantidades, T-11 ni duración de ruta declarada en la arquitectura física.
- Cierre: regla coherente con M08 y prueba diseñada para la ruta de 14,5 h. No aumentar TTL sin analizar consecuencias. Una dependencia externa no resuelta mantiene abierta la mejora.

### M10 — Completar controles y riesgos residuales lógicos

- Prioridad alta. Responsable propuesto: arquitectura lógica y seguridad. Dependencias: M08–M09.
- Motivo: los puntos de falla de 4.1 deben mostrar control adoptado, prueba y exposición que subsiste.
- Trabajo: revisar identidad aislada, límites de módulos, contratos, dependencia lógica del ERP, outbox, duplicados y reconciliación. Vincular escenario, control, alternativa, prueba, límite residual y contingencia lógica.
- Archivos: `04/partes/4.1_logica/13_puntos_unicos_de_falla_y_riesgos_residuales.tex`, `22_condiciones_y_supuestos_de_diseno.tex`, partes pertinentes de 4-Q/4-R/4-V y ADR lógicos.
- Límite: no rediseñar infraestructura, regiones o respaldos, ni editar un registro de riesgos externo. No crear IDs que aparenten existir en otro registro.
- Cierre: controles y pruebas trazables; limitaciones residuales explícitas. Registrar efectos externos sin dar por resueltas sus correcciones.

### M11 — Explicar el cambio de Django a Laravel

- Prioridad media. Responsable propuesto: arquitectura lógica.
- Motivo: la comparación existe, pero falta reconocer explícitamente el cambio respecto del Informe 1.
- Trabajo: explicar motivo y consecuencias sobre núcleo modular, perfiles HTTP/CLI, interfaces, pruebas, herramientas y operación. Conservar las alternativas sustentadas. Distinguir cambio de propuesta de migración de código no acreditada.
- Archivos: `04/partes/4.1_logica/08_detalle_de_tecnologias_seleccionadas.tex`, `09_implantacion_progresiva_del_backend_laravel.tex` y ADR-23.
- Cierre: motivo e impacto claros sin inventar experiencia, ahorro, rendimiento o trabajo previo. Los efectos sobre secciones excluidas se registran, no se editan.

### M12 — Verificar versiones y soporte de tecnologías lógicas

- Prioridad alta. Responsable propuesto: arquitectura de software.
- Motivo: defender existencia, compatibilidad y soporte de las versiones ofrecidas.
- Trabajo: comprobar mediante fuentes oficiales lanzamiento estable a la fecha de oferta, compatibilidad del conjunto y actualización de PHP/Laravel, Angular/TypeScript, Kotlin, identidad, mensajería y persistencia utilizadas por 4.1. Registrar fuente y fecha. Existencia actual no demuestra disponibilidad histórica.
- Archivos: `04/partes/4.1_logica/02_especificaciones_tecnologias_de_software_a_utilizar.tex`, `08_detalle_de_tecnologias_seleccionadas.tex`, filas pertinentes del Anexo 4-P y referencias de 4.1.
- Límite: solo entradas que sustentan arquitectura lógica; no editar catálogo físico, licenciamiento o T-11. Si una incompatibilidad exige cambiar la oferta excluida, documentar el impacto y mantener abierta la mejora.
- Cierre: matriz de versión, lanzamiento, compatibilidad y estrategia de soporte fundamentada; sin discrepancias conocidas presentadas como resueltas.

### M13 — Hacer legible la Figura 1

- Prioridad alta. Responsable propuesto: arquitectura lógica y diagramación. Dependencias: políticas, nombres y tecnologías estabilizados.
- Motivo: la vista general de página 13 resulta ilegible al tamaño de impresión.
- Trabajo: simplificar actores, capas y relaciones principales, dejando detalle en las vistas por capa. Comprobar qué fuente se incluye realmente. Generar una variante identificada y conservar originales y vistas aprobadas.
- Archivos: inclusión en `04/partes/4.1_logica/04_capas_de_la_arquitectura.tex`, figuras lógicas y fuentes editables en `04/figuras/`.
- Cierre: rótulos de al menos 9 pt al tamaño final, sin solapamientos; explicación antes/después y coherencia con el detalle. El nombre «9pt» de un archivo no demuestra su escala final.

### M15 — Unificar nombres de módulos dentro de 4.1

- Prioridad media. Responsable propuesto: arquitectura lógica y edición.
- Motivo: diferencias entre nombres de figuras y catálogos, especialmente M10 y M11.
- Trabajo: consultar el catálogo de referencia y uniformar M1–M12 en texto, figuras y anexos lógicos. BI/EDI pueden quedar como funciones o tecnologías con equivalencia explícita. Revisar imágenes, no solo texto LaTeX.
- Archivos: capas, módulos, Anexo 4-D, partes pertinentes de 4-F/4-N y figuras lógicas.
- Límite: no editar el catálogo de otro capítulo ni figuras físicas.
- Cierre: nomenclatura única dentro de 4.1 y sus anexos; diferencias externas registradas como hallazgos.

## 6. Tres mejoras transversales aplicadas solo a 4.1

### M16 — Precisar fuentes de figuras y tablas lógicas

- Prioridad media. Responsable propuesto: edición técnica y arquitectura lógica.
- Motivo: citas generales repetidas no muestran qué dato o criterio sustenta cada figura.
- Trabajo: inventariar únicamente figuras/tablas de 4.1 y anexos intervenidos; separar dato o requisito de origen, criterio técnico y diseño propuesto. Usar fuente y localizador específicos; el propio subdocumento no es evidencia suficiente de un dato externo.
- Archivos: `04/partes/4.1_logica/`, anexos intervenidos y referencias correspondientes.
- Cierre: fuente verificable y pertinente para cada figura/tabla lógica. No cambiar leyendas físicas ni referencias ajenas a 4.1.

### M19 — Sintetizar la sección 4.1

- Prioridad media. Responsable propuesto: edición técnica y arquitectura. Dependencia: decisiones estabilizadas.
- Motivo: extensión y repetición de requisitos, particularmente en 4.1.3.1 y 4.1.3.7.
- Trabajo: conservar decisión, alternativa, fundamento, consecuencia y conclusión. Eliminar duplicaciones; concentrar catálogos en anexos lógicos y remitir con precisión. No trasladar duplicaciones intactas para aparentar reducción.
- Archivos: texto y ensamblador de `04/partes/4.1_logica/`, anexos lógicos pertinentes. Las raíces solo coordinan compilación si resulta necesario.
- Cierre: registro de consolidaciones/traslados y destino, sin pérdida de evidencia. Comparar extensión de 4.1 antes/después sin meta arbitraria para el documento completo. No resumir ni reordenar 4.2/4.3.

### M20 — Declarar uso de IA y revisión de 4.1 con veracidad

- Prioridad media. Responsable propuesto: personas que efectivamente revisen 4.1 y anexos intervenidos.
- Motivo: la revisión debe acreditar comprobaciones técnicas reales, no solo corrección de redacción.
- Trabajo: comprobar procedencia de figuras y uso de IA; registrar verificaciones de identidad, contratos, tecnologías, trazabilidad y decisiones. Ajustar solo fila 4.1 y filas de anexos realmente intervenidos, con evidencia del alcance revisado.
- Archivos: fila 4.1 de `04/partes/cierre/declaracion_de_uso_de_ia.tex`, filas aplicables de anexos lógicos y declaraciones propias de esos anexos.
- Cierre: declaración fiel al uso y trabajo realizados. No añadir nombres, bajar niveles ni atribuir aprobaciones inexistentes. Filas 4.2, 4.3 y T-11 intactas.

## 7. Preparación y verificación

### M01 — Proteger la línea base y comprobar el alcance

- Responsable propuesto: integración documental.
- Realizado en esta preparación: pull, respaldo de diferencias e inventario de archivos locales, creación de rama hija y actualización del plan.
- Antes de implementar: registrar huellas de fuentes protegidas de 4.2/4.3/T-11 y figuras físicas; identificar porciones permitidas de archivos compartidos y ensambladores/figuras realmente incluidos.
- Cierre: los cambios heredados se conservan y se distinguen de los nuevos. La versión amplia del plan sigue recuperable.

### M22 — Compilar y verificar las correcciones de 4.1

- Responsable propuesto: integración y revisión lógica. Dependencia: las 11 mejoras aplicables.
- Trabajo: compilar el cuerpo ensamblado y los anexos necesarios. Usar el modo del cuerpo y la raíz de anexos correspondientes; no regenerar T-11 por ejecutar indiscriminadamente el script completo. No crear como nuevo entregable un subdocumento lógico independiente sin petición del usuario.
- Verificación: comprobar errores, referencias, índices, numeración, figuras, tablas y remisiones de 4.1. Renderizar e inspeccionar páginas afectadas al tamaño final. Cotejar identidad, contratos y versiones entre texto, anexos y figuras.
- Preservación: comparar huellas de fuentes de 4.2/4.3/T-11 y figuras físicas. Si el PDF combinado cambia por desplazamiento de páginas, comprobar que el contenido excluido no fue editado ni se degradó su presentación; distinguir paginación de cambio técnico.
- Cierre: cuerpo y anexos coherentes con las fuentes finales, evidencia visual y registro por observación. T-11 permanece intacto. Compilar no acredita aprobación del solicitante ni revisión humana.

## 8. Seguimiento y condición de cierre

Las 11 mejoras activas son M07, M08, M09, M10, M11, M12, M13, M15, M16, M19 y M20; M01/M22 son preparación y verificación. Cada entrada registrará estado, responsable confirmado cuando exista, observación de origen, archivos/porciones modificadas y evidencia final.

Estados: por ejecutar, en trabajo, verificada localmente, pendiente de antecedente y cerrada. Una dependencia fuera de alcance se registra y mantiene abierta la mejora afectada; no da permiso para intervenir otro capítulo o sección.

Para cerrar deben coincidir fuente LaTeX, figura y PDF, existir evidencia del criterio y no quedar una contradicción material conocida que impida afirmar cumplimiento. No se inventan mediciones, soporte, revisores ni aprobaciones.

La implementación completa exige 11 mejoras cerradas, verificación final satisfactoria y ausencia de cambios nuevos en contenido excluido. La preparación y la ejecución documental se distinguen en el registro siguiente; ninguna comprobación de documentos acredita por sí sola un ensayo de la aplicación.


## 9. Registro de ejecución documental — 5 de noviembre de 2026

Rama de ejecución: `LafroX-Subdoc4.1-LateX-corrigiendo`. Las correcciones se aplicaron a 4.1 y anexos lógicos; las fuentes físicas, T-11 y sus cambios heredados se conservaron.

| ID | Resultado documental | Evidencia principal |
| --- | --- | --- |
| M01 | Verificada | Respaldo de fuentes y PDF; huellas de 34 archivos protegidos. |
| M07 | Implementada | Matriz de 16 obligaciones individuales en 4-E y síntesis de cuatro recorridos en el cuerpo. |
| M08 | Implementada | Política de manifiesto, caché y reloj; AL-OFF-01 ampliado y AL-ID-01 en 4-M. |
| M09 | Implementada | Ruta de 14,5 h; emisión en la hora anterior, margen de 30 min y cota de 16 h; menciones de 4.1/G/H/P conciliadas. |
| M10 | Implementada | Controles y límites residuales en 4.1.12; AL-MOD-01 y AL-FRIO-01, con enlace a 4-R. |
| M11 | Implementada | Cambio explícito del Informe 1 a Laravel y efectos documentados en 4.1.7.1 y ADR-23. |
| M12 | Verificada documentalmente | Registro único de existencia, compatibilidad y soporte en 4-P; referencias oficiales fechadas. No equivale a construir la aplicación. |
| M13 | Verificada en PDF | Nueva Figura 1 vectorial, letra mínima medida de 10,41 pt a escala final; original conservado. |
| M15 | Implementada | Nombres M10 Analítica/M11 Canal moderno en vista general y tres variantes de vistas detalladas. |
| M16 | Implementada | Fuentes propias para figuras lógicas, dominio, protocolos y matriz de backend; ajuste de ancho del productor en 4-A. |
| M19 | Implementada | Catálogos M2/M3/M4/M7 a 4-D, interacción a 4-N y custodia a 4-R. Cuerpo 4.1: 29.005 → 27.048 palabras de fuente, aproximadamente −6,7 %. |
| M20 | Declaración actualizada | Se distingue revisión anteriormente declarada de correcciones comprobadas automáticamente. No se acredita revisión humana adicional. |
| M22 | Verificada documentalmente | Tres pasadas finales por entregable; cero errores de referencia, destinos duplicados o desbordes. PDF revisados visualmente; archivos protegidos intactos. |

Las nuevas pruebas AL-ID-01, AL-MOD-01, AL-FRIO-01 y AL-UI-01 son especificaciones de aceptación con resultados esperados. No se presentan como ensayos realizados sobre una aplicación operativa. Las comprobaciones efectuadas corresponden a fuentes, coherencia temporal del diseño, documentación oficial, compilación y presentación de PDF.

Las 98 páginas de arquitectura física y centros de datos conservan su contenido fuente y número de tablas; los cambios renderizados se limitan a cifras de paginación y referencias recalculadas. No se publica ni se cambia la rama madre.

Resultado final: cuerpo de 192 páginas y anexos de 128 páginas. Registro detallado: `00/trazabilidad/RESULTADO_MEJORAS_SD41_2026-11-05.md`. La sección 4.1 ocupa tres páginas menos; los anexos incorporan el detalle concentrado y la nueva evidencia de aceptación.
