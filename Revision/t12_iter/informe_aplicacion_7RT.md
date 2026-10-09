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

## Segunda aplicación (mínimo arrastre)

En `rama-md` se incorporaron 14 RT con frases en SD4 o su Anexo 4-R, reutilizando Angular, Laravel, QA, CI, CloudWatch y los datos de SD5. La Tabla 3 identifica lo escrito por RT y su estado final; SD4 y SD4-Anexos conservan las rutas declaradas en la primera aplicación. Los siete RT no aplicados conservan No cumple y sus datos o decisiones faltantes figuran en `propuestas_SD4_RT.md`.

**Tabla 3 — Texto incorporado y estado final de los RT**

| RT | Lo escrito | Archivo y sección | Estado final T-12 |
| --- | --- | --- | --- |
| RT-05.24 | Sin texto nuevo; falta dato o decisión identificado en el informe de decisiones. | — | No cumple |
| RT-06.15 | Sin texto nuevo; falta dato o decisión identificado en el informe de decisiones. | — | No cumple |
| RT-08.15 | LafroX provee una unidad de cada tipo y variante del T-11 para aceptación antes de la compra masiva; se incorpora al parque o reserva dimensionados. | SD4 4.2.1.2 | Cumple |
| RT-08.19 | Mantención y repuestos para vida útil esperada de 60 meses; sin renovación general al mes 56: residuos de esa renovación diferidos 4 meses, 7,1 % del período contractual. | SD4 4.2.1.2 | Cumple |
| RT-09.10 | CI ejecuta carga de regresión automatizada en QA en cada versión candidata y al menos semanalmente, y antes de liberar en Preproducción; compara percentil 95, errores y colas con la versión aceptada y bloquea regresiones. | SD4 4.2.4.1.1; SD4-Anexos 4-W.12 | Cumple |
| RT-11.28 | Seguridad aplica OWASP SAMM al inicio del desarrollo y anualmente; mide madurez por práctica y sigue acciones de mejora con responsable y evidencias. | SD4-Anexos 4-R | Cumple |
| RT-13.05 | Accesos a todas las funciones principales de cada perfil Angular/Kotlin en un máximo de tres interacciones desde su inicio, comprobados en prototipos y aceptación. | SD4 4.1.3.1 | Cumple |
| RT-13.09 | Sistema de diseño documentado común a Angular/Tailwind y Kotlin: hasta cinco colores principales, a lo más dos familias tipográficas, iconografía, retícula y componentes reutilizables. | SD4 4.1.3.1 | Cumple |
| RT-13.12 | Modo claro/oscuro, tamaño de texto y densidad configurables por persona y conservados en su dispositivo; español para los perfiles del caso, sin exigencia de otros idiomas. | SD4 4.1.3.1 | Cumple |
| RT-14.09 | Detección de anomalías de Amazon CloudWatch sobre la historia horaria y semanal de latencia, errores y colas; alerta al NOC/SRE antes de alcanzar los límites; aceptación con degradación gradual. | SD4 4.1.3.8 y 4.2.6.11 | Cumple |
| RT-15.05 | Sin texto nuevo; falta dato o decisión identificado en el informe de decisiones. | — | No cumple |
| RT-15.06 | Sin texto nuevo; falta dato o decisión identificado en el informe de decisiones. | — | No cumple |
| RT-16.04 | Consola Angular/Laravel administra valores de reglas implementadas, catálogos, listas, textos y sitios con versión y auditoría; algoritmos, reglas nuevas, estados/transiciones, esquemas, contratos y transportes nuevos requieren desarrollo. | SD4 4.1.3.4; SD5-Anexos 5-A | Cumple |
| RT-16.05 | QA simula cambios de parámetro con las mismas transacciones y datos controlados, compara valor vigente/propuesto y exige comprobación y aprobación antes de Producción. | SD4 4.1.9 y 4.2.4.1 | Cumple |
| RT-16.08 | Consola Angular/API Laravel consulta gob_auditoria por persona, período, entidad y operación; exporta resultado filtrado CSV UTF-8/JSON con permisos, sin acceso a la base; trabajo asíncrono para grandes volúmenes. | SD4 4.1.3.7; SD5-Anexos 5-A; SD5 5.2.8 | Cumple |
| RT-16.12 | CLIENTE configura en consola responsables por rol/sitio, plazos y niveles de aprobación de flujos existentes; gob_asignacion y mae_parametro_version conservan vigencias y parámetros, con segregación obligatoria. | SD4 4.1.3.4; SD4-Anexos 4-B; SD5-Anexos 5-A | Cumple |
| RT-16.18 | Sin texto nuevo; falta dato o decisión identificado en el informe de decisiones. | — | No cumple |
| RT-16.19 | CLIENTE administra plantillas versionadas de avisos y comprobantes en Angular; Laravel combina datos autorizados de pedido/entrega y descarga HTML abierto, reutilizando not_plantilla/cuerpo_ref. | SD4 4.1.6.2; SD5-Anexos 5-A | Cumple |
| RT-16.26 | Sin texto nuevo; falta dato o decisión identificado en el informe de decisiones. | — | No cumple |
| RT-16.33 | Sin texto nuevo; falta dato o decisión identificado en el informe de decisiones. | — | No cumple |
| RT-17.08 | Vista ligera del Portal de Clientes para teléfonos de bajo costo o generaciones anteriores: imágenes bajo demanda, paginación y sin animaciones; navegadores/sistemas compatibles y aceptación en esos equipos. | SD4 4.1.3.1; SD4-Anexos 4-P (Tabla A.19) | Cumple |

Fuente: textos aplicados a los archivos indicados y matriz T-12 vigente; requisitos de las Bases Técnicas Transversales y Caso 02, cap. 15.

El cálculo de RT-08.19 usa exclusivamente cinco años de vida útil y 56 meses de contrato: 60 − 56 = 4 meses y 4 ÷ 56 × 100 = 7,1 %. Expresa aplazamiento de renovación y residuos; no es ahorro de masa, energía o carbono. Para RT-16.33 se contrastaron los 2.000 contactos/mes proyectados, la capacidad de 2.283 de 4-W.7 y la autoatención de 4.1.3.1/4.1.4.4: ninguno aporta una proporción de contactos evitables o adopción. Para RT-16.18, Caso 15 exige articular POD, guía y acuse, pero no acredita sello de tiempo o verificación tras vencer el certificado; la consulta V-18 no permite declarar cumplimiento.

La Tabla 4 registra las cinco filas RF ajustadas; se conservaron ID y Descripción.

**Tabla 4 — Coherencia de la Parte A**

| RF | Estado final | Cobertura y límite | Sección |
| --- | --- | --- | --- |
| RF-17.02 | Cumple | Consola Angular/API Laravel administra umbrales, plazos, montos, tolerancias, catálogos, listas y textos de reglas implementadas; mae_parametro/mae_parametro_version y auditoría conservan versión, vigencia, autor y fecha. | SD4 4.1.3.4; SD4 4.1.4.2; SD5-Anexos 5-A; SD5 5.2.2 |
| RF-17.05 | Cumple | Consola Angular/API Laravel consulta y exporta gob_auditoria con filtros por persona, período, entidad y operación; resultado filtrado CSV UTF-8/JSON, con permisos y sin acceso a base de datos. | SD4 4.1.3.7; SD5-Anexos 5-A; SD5 5.2.8 |
| RF-17.06 | Cumple parcialmente | Flujos existentes con estados y transiciones; CLIENTE configura responsables, plazos y niveles en Angular mediante gob_asignacion/mae_parametro_version. Falta: configuración de estados y transiciones, escalamiento automático por vencimiento y delegación por ausencia. | SD4 4.1.3.4 y 4.1.3.5; SD4-Anexos 4-B; SD5-Anexos 5-A |
| RF-17.09 | Cumple parcialmente | Plantillas administrables por el CLIENTE y comprobantes de pedido/entrega con datos transaccionales en HTML abierto. Falta: salida PDF, DOCX o XLSX. | SD4 4.1.6.2; SD5-Anexos 5-A |
| RF-17.10 | Cumple parcialmente | INT-11 envía correo, SMS/WhatsApp y avisos en portal; CLIENTE administra cuerpo y versión de not_plantilla en consola Angular. Falta: coherencia de los dominios de canal entre not_plantilla y not_intento para WhatsApp y aviso en portal. | SD4 4.1.6.2; SD4-Anexos 4-H (INT-11); SD5-Anexos 5-A (Tabla A.8) |

Fuente: comparación entre las descripciones intactas del T-12 y los textos aplicados al SD4 y sus datos de soporte en SD5.

RF-17.03 permanece parcial: no se agregó aprobación de segundo perfil para todo cambio operacional ni su justificación. RF-18.01 sigue parcial por firma/certificado/sello de tiempo; RF-18.02, por preferencias de canal y frecuencia por persona (el tema visual no las satisface). RF-17.12 sigue parcial: la consulta de auditoría no equivale a listados generales ordenables y paginados. Se revisaron los RNF relacionados con interfaz, equipos y servicio sin atribuirles cobertura adicional.

Se actualizaron solo las finalidades de las filas afectadas en las declaraciones de IA: cuerpo 4.1, 4.2 y 4-R; anexos R, 4.1.3, 4.1.6 y 4.1.9. Permanecen intactas las 28 marcas `[[REVISIÓN HUMANA]]` del cuerpo y las 43 de anexos. El resumen del SD4 recoge los nuevos compromisos. Las referencias nuevas son los dos documentos SD5 citados en el cuerpo y OWASP SAMM en 4-R, contrastado con su [modelo oficial](https://owaspsamm.org/model/).

Verificación: 645 filas de cinco celdas e IDs únicos, ID/Descripción idénticos a HEAD; 19 filas modificadas solo en Cumple, Componente y Sección (14 RT y cinco RF). Parte A: 199 Cumple, 69 Cumple parcialmente y 3 No cumple; Parte B: 236, 106 y 32, respectivamente. Se conservaron figuras, tablas, memoria 4-W y T-11; no se modificaron SD3, SD5, SD8, T-14 ni T-15. Solo se editaron Markdown dentro de SD4, SD4-Anexos, T-12, resumen del SD4 y `Revision/t12_iter/`, mediante apply_patch; sin commit ni push.

Estado para reanudación: esta segunda aplicación y el informe de decisiones representan las 21 decisiones actuales. RT-05.24, RT-06.15, RT-15.05, RT-15.06, RT-16.18, RT-16.26 y RT-16.33 siguen pendientes. Los compromisos documentales no acreditan implementación, ejecución de ensayos ni revisión humana.

Control final: `git diff --check` limpio; siete archivos `.md` dentro del alcance; 351 enlaces locales contrastados por archivo y sección y 22 referencias explícitas SD de las filas editadas, además de anexos y referencias consecutivas. Se comprobó conservación exacta de todas las tablas ajenas a las declaraciones de IA, todos los encabezados y figuras del cuerpo/anexos y el contenido completo de 4-W. La rama continúa en `rama-md`.



Ajustes posteriores de la revisión: RT-09.10 pasa de una ejecución nocturna a una ejecución por versión candidata y semanal dentro del horario de uso de QA, para no contradecir el apagado de ambientes no productivos de 4.2.4.1; RT-14.09 usa la detección de anomalías nativa de Amazon CloudWatch en lugar de un análisis propio en el planificador; las citas al Subdocumento 5 se simplifican a (LafroX, 2026a/2026b, sección o anexo).
