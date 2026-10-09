# LafroX — Informe de aplicación de siete RT obligatorios en SD4

Se aplicó la Parte 1 de la especificación `p7.md` en el checkout actual, rama comprobada `rama-md`, y se elaboraron sin aplicar las 21 propuestas de su Parte 2. La autorización específica de la tarea y el estado reciente del contexto prevalecen sobre los nombres de rama históricos de AGENTS.md. Se conservaron los cambios previos del T-12, los informes de revisión y el contexto; no se hizo commit ni publicación.

## Aplicación y estado del T-12

La Tabla 1 identifica el desarrollo que respalda cada cambio. «Cumple» expresa cobertura documental del compromiso, no ejecución de ensayos, certificaciones ya emitidas ni recepción por el CLIENTE.

**Tabla 1 — Desarrollo aplicado y estado final de los siete RT**

| RT | Archivo y sección exacta | Desarrollo aplicado | Estado T-12 y fundamento |
| --- | --- | --- | --- |
| RT-06.25 | `04_arquitectura/LAFROX-Subdocumento4.md`, 4.3.1.4 | Solicitud y autorización, verificación biométrica, acceso temporal, acompañamiento durante toda la visita, bitácora con tercero y acompañante, cierre y revocación; fabricantes, mantenedores y auditores incluidos. | Cumple: el procedimiento cubre acompañamiento obligatorio y registro, incluidos ingresos urgentes. |
| RT-08.17 | `04_arquitectura/LAFROX-Subdocumento4.md`, 4.2.1.2 | Inventario y custodia, método adecuado de purga o destrucción, verificación y certificado al CLIENTE para todo almacenamiento retirado; servidores, NAS, HDD/SSD, mini-PC, terminales y medio físico rotativo. | Cumple: explicita borrado seguro verificable y certificado de sanitización o destrucción, sin asumir que borrar archivos o restablecer el equipo basta. |
| RT-08.18 | `04_arquitectura/LAFROX-Subdocumento4.md`, 4.2.1.2 | Gestor autorizado y registrado, comprobación de habilitación, trazabilidad y certificado de disposición al CLIENTE; separación de certificados de disposición y sanitización. | Cumple: cubre gestor, normativa aplicable y certificación final, sin inventar nombre ni contrato del gestor. |
| RT-13.02 | `04_arquitectura/LAFROX-Subdocumento4.md`, 4.1.3.1 | Diseño desde pantalla pequeña con puntos Tailwind en rem, equivalencias y reorganización de menú, formularios, listados y paneles; conservación de operaciones; pruebas de transiciones/orientaciones. | Cumple: cubre escritorio, tableta, teléfono, quiebres coherentes y adaptación del contenido. Kotlin queda expresamente vinculado a pantalla fija por modelo Zebra. |
| RT-13.10 | `04_arquitectura/LAFROX-Subdocumento4.md`, 4.1.3.1; `04_arquitectura/LAFROX-Subdocumento4-Anexos.md`, 4-P, Tabla A.19 | Cuatro filas de navegadores/sistemas, versiones estables mayores vigente y anterior, registro de números exactos y ensayos por liberación, incorporación por nueva estable y parches; compatibilidad Baseline Angular. | Cumple: matriz y política explícitas y verificables, sin números de versión de navegador inventados. |
| RT-13.11 | `04_arquitectura/LAFROX-Subdocumento4.md`, 4.1.3.1 | Navegación íntegra por teclado, orden/foco visible, diálogos, controles semánticos, atajos documentados/desactivables y pruebas en web y teclado físico o conectado en Kotlin. | Cumple: cubre navegación completa, foco lógico y atajos frecuentes, enlazados con WCAG 2.2 AA. |
| RT-16.25 | `04_arquitectura/LAFROX-Subdocumento4.md`, 4.1.6.2; `04_arquitectura/LAFROX-Subdocumento4-Anexos.md`, 4-H, INT-11 | Separación operacional/comercial; remitente, finalidad y baja por canal; registro de preferencia; comprobación previa a envíos/reintentos y supresión desde la solicitud, incluidas colas. | Cumple: respeto normativo y baja comercial cuando corresponde, conservando avisos necesarios sin publicidad. |

Fuente: Bases Técnicas Transversales, caps. 6 (p. 16), 8 (p. 20), 13 (p. 26) y 16 (p. 30), y desarrollo aplicado a los entregables de LafroX.

Las siete filas pasaron de No cumple a Cumple. Se modificaron solamente Cumple, Componente y Sección; ID y Descripción permanecieron intactos. En la Tabla A.19 se amplió una tabla existente, sin crear tablas intermedias ni alterar numeraciones o sus referencias.

## Coherencia con la Parte A

Se revisaron todas las descripciones RF/RNF del T-12 buscando materias equivalentes. RF-18.02 continúa en Cumple parcialmente: su componente y sección incorporan la baja comercial de INT-11, pero sigue faltando configuración individual completa de canal y frecuencia con políticas obligatorias. No se eliminó su «Falta: …».

RF-17.10 sigue parcial por la administración de plantillas por el CLIENTE; RF-18.03, por registro de apertura; RF-04.06, por destinatario de ETA en el modelo. La baja no resuelve esos elementos. RF-17.13 conserva su estado por el portal público y los criterios de accesibilidad existentes; no se inventa informe de conformidad. No se encontraron RF/RNF equivalentes que pudieran pasar justificadamente a Cumple por los nuevos textos de teclado, navegadores, acceso acompañado o retiro. También se conservan los estados de RT-13.01 y de los requisitos de prototipo/corporativo que exigen más evidencia que diseño responsivo y teclado.

## Otros archivos actualizados

Se actualizó `Resumen/LAFROX-Subdocumento4-Resumen.md` con presentación, matriz de navegadores, baja comercial, sanitización/disposición y acceso acompañado. Las nuevas fuentes se añadieron a las Referencias del SD4; la Ley N.º 19.496 se añadió además al anexo por su cita propia. Se verificaron en documentación oficial Angular/Baseline, Tailwind, WCAG, normativa chilena y NIST.

Las declaraciones de IA solo cambiaron la finalidad en las filas afectadas: 4.1, 4.2, 4.3, 4-H y 4-P del cuerpo; H y P del anexo. La fila 4.1.1 y las restantes se preservaron. Permanecen las 28 marcas de revisión humana del cuerpo y las 43 del archivo de anexos; ninguna se completó ni borró. La revisión humana real continúa pendiente.

`Revision/t12_iter/README.md` incorpora los dos informes y aclara que esta aplicación prevalece para las ocho filas editadas sobre los estados anteriores. `compct/CONTEXTO_SESION.md` registra el resultado actual.

## Contraste con T-11 y T-14

El T-11 mantiene el control biométrico, AFIS, esclusa y bitácora conservada cinco años o más, compatibles con el procedimiento de terceros. El T-14, cuenta 8.2, paquete 8.2.7, ya compromete ciclo de vida, reposiciones y disposición registrada de cada equipo retirado. No se identificó una contradicción con los siete desarrollos aplicados y ninguno de esos dos formularios se modificó. Sus huellas SHA-256 quedaron iguales a las capturadas al iniciar esta tarea.

El detalle de certificados y controles de retiro deberá traducirse a instrucciones y evidencias de ejecución en 8.2.7. Ese paquete programa Operación, meses 21–56; el compromiso arquitectónico de sanitizar todo medio retirado rige también durante implementación y soporte puente. Conviene explicitar su asignación temporal en planificación, sin suponer HH adicionales disponibles ni modificar aquí el T-14/T-15.

## Incoherencias y dependencias encontradas

El modelo de notificaciones de `05_modelo_datos/LAFROX-Subdocumento5-Anexos.md`, 5-A, Tabla A.8, requiere alineación posterior, fuera de las ediciones autorizadas en esta tarea:

- `not_preferencia` solo define cliente, plantilla/versión y activa; no explicita destinatario por persona, alcance comercial, canal, fecha ni origen de baja. El nuevo texto es un compromiso arquitectónico, no una afirmación de que esos atributos ya existen en el diccionario.
- Los dominios de `not_plantilla.tipo_aviso` y `not_aviso.tipo` enumeran avisos operacionales (PEDIDO, PREPARACION, DESPACHO, ENTREGA, INCIDENCIA, COBRANZA, RETIRO); falta la clasificación comercial y su control de elegibilidad si se habilitan esos envíos. No se deben etiquetar promociones como transaccionales.
- `not_plantilla.canal` enumera CORREO, SMS, WHATSAPP y AVISO_EN_PORTAAL, mientras `not_intento.canal` usa EMAIL, SMS y PUSH. La nomenclatura y la cobertura de WhatsApp/portal difieren; el valor AVISO_EN_PORTAAL contiene un error de escritura. No se corrigió sin autorización de ampliar el modelo.
- `not_aviso.entrega_id` es obligatorio: los futuros avisos comerciales no necesariamente se vinculan a una entrega. Debe resolverse la cardinalidad sin debilitar la trazabilidad de los avisos operacionales.

El SD3 mantiene las notas históricas sobre prueba/criterio del T-12 y su declaración «T-12: EDT y pruebas», y `Resumen/LAFROX-Formulario-T-12-Resumen.md` está desactualizado según el contexto previo. No se modificaron porque no forman parte de esta aplicación. El T-12 conserva sus cinco columnas oficiales.

## Propuestas y decisiones del equipo

`Revision/t12_iter/propuestas_SD4_RT.md` contiene las 21 propuestas solicitadas, ordenadas en siete obligatorias, una según caso y trece deseables. Todas conservan No cumple en el T-12. Cada ficha reproduce texto y carácter de las Bases, identifica soporte existente y faltante, propone solución y destino exactos, ofrece borrador, enumera datos por definir e impactos en SD3, SD5, T-11, T-14/T-15, SD8 y Oferta Económica, y clasifica complejidad. Las deseables tienen recomendación y razón sin inventar puntos ni horas.

El equipo debe resolver especialmente las materias siguientes:

- Completar el inventario de funciones principales, sistema de diseño, parámetros y flujos configurables; definir roles y límites de consulta de auditoría y plantillas documentales.
- Fundamentar línea base y meta de RT-16.33. La capacidad dimensionada de mesa no se utiliza como atención asistida observada; el borrador contiene marcadores fuera de los entregables.
- Resolver aplicabilidad de RT-16.18 por acto, capacidad real del ERP y servicio de confianza; V-18 no equivale a exención. No confundir firma dibujada/QR con firma certificada de larga duración.
- Financiar muestras de RT-08.15 y confirmar sus tipos/calendario; cuantificar RT-08.19 y RT-15.06 antes de integrar sus borradores. RT-15.05 exige datos regionales comparables, latencia y regulación y no se recomienda en esta iteración.
- Elegir el gestor autorizado y las herramientas de sanitización conforme a cada medio y comprobar documentación/contratación al ejecutar. No se atribuyó nombre de proveedor, contrato ni certificación existente.
- Coordinar el modelo de notificaciones y asignar pruebas/HH de los siete compromisos dentro de la planificación; no reducir capacidad de atención por una reducción aún no demostrada. La Oferta Económica no está disponible en este checkout.

NIST SP 800-88 Rev. 1 era una referencia opcional en la especificación. Se utilizó Rev. 2, publicada en septiembre de 2025 y vigente en la fecha de trabajo; la Rev. 1 fue retirada y sustituida, según [NIST](https://csrc.nist.gov/pubs/sp/800/88/r1/final). La política de comunicaciones se contrastó con [Ley N.º 19.496, art. 28 B](https://www.bcn.cl/leychile/navegar?idNorma=61438); la disposición se apoya en [Ley N.º 20.920](https://www.bcn.cl/leychile/navegar?idNorma=1090894). Las referencias aplicables están además en los entregables donde se citan.

## Verificaciones

La Tabla 2 resume los controles realizados frente al estado capturado al comenzar, preservando los cambios del usuario que ya estaban en el árbol de trabajo.

**Tabla 2 — Controles documentales y resultado**

| Control | Resultado |
| --- | --- |
| Rama | `rama-md`; no se cambió de rama. |
| Integridad T-12 | 645 filas, todas de cinco celdas, 645 IDs únicos. |
| ID y Descripción | Huella conjunta idéntica a la inicial; ningún ID ni descripción cambió. |
| Filas editadas | Exactamente ocho: siete RT y RF-18.02; solo columnas permitidas. |
| Estados Parte A | 197 Cumple, 69 Cumple parcialmente, 5 No cumple. |
| Estados Parte B | 222 Cumple, 106 Cumple parcialmente, 46 No cumple. |
| Referencias T-12 | 1.031 menciones explícitas de secciones SD, 1.233 de anexos, 1.114 de tablas y 5 de figuras contrastadas; destinos existentes. |
| Propuestas | 21 IDs únicos, textos y caracteres coincidentes con las Bases; siete obligatorios, uno según caso y trece deseables; todos siguen No cumple. |
| Destinos y enlaces | Secciones propuestas existentes; 346 enlaces locales de cuerpo, anexos, resumen y propuestas contrastados, incluidos los seis nuevos. |
| Fuentes nuevas | Citas y entradas de Referencias correspondientes, incluidas las fuentes técnicas de apoyo de las propuestas. |
| Numeración | Se preservó la numeración de todas las tablas; matriz incorporada a A.19 con cita previa, fuente y explicación posterior. |
| Revisión humana | 28 marcas en cuerpo y 43 en anexos preservadas; no se acreditó revisión humana adicional. |
| Conservación | T-11, T-14, T-15, SD3, SD5, SD8, memoria 4-W y figuras sin cambios de esta tarea. |
| Archivos | Ocho archivos creados/editados por esta tarea, todos `.md`, usando apply_patch. |
| Git | `git diff --check` limpio; sin commit ni push. |

Fuente: comparación de huellas iniciales/finales, validadores documentales ejecutados sobre el contenido real y comprobaciones de Git.

Los resultados acreditan coherencia documental de las ediciones. No se ejecutaron ensayos de aceptación, visitas reales, borrados de medios, controles de proveedor, implementación de las propuestas ni evaluación de presentación paginada.

