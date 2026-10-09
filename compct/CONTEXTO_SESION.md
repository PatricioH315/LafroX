# CONTEXTO DE SESIÓN

## Estado vigente — 9 de octubre de 2026: T-12 reconstruido

Por instrucción del usuario se reemplazó `03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md` con una matriz de cinco columnas exactamente como el Formulario T-12 de las Bases Administrativas: ID requerimiento, Descripción, Cumple, Componente que lo satisface y Sección de la propuesta. Contiene 271 RF/RNF del anexo SD3 (181 RF, 90 RNF) y los 374 RT de las Bases Técnicas Transversales; 645 IDs únicos. El estado usa Cumple, Cumple parcialmente o No cumple; hay 462, 113 y 70 filas respectivamente. Los 26 valores del capítulo 15 del Caso se agregaron a la descripción del RT correspondiente, incluidos los nueve códigos cuyo significado difiere del de las BTT. RT-05.10 y RT-15.02 se ajustaron a cumplimiento parcial al responder conjuntamente el contenido transversal y el del Caso. RF-07.11 se clasificó parcial porque RF-07.10 compromete esa función, aunque el catálogo del anexo contiene una declaración contradictoria. La matriz se generó desde `Revision/T12_mapeo_cumplimiento.md`, contrastando las 374 descripciones RT con las BTT y las 271 descripciones RF/RNF con el anexo SD3. Se cotejaron visualmente los PDF originales de las Bases Administrativas (formulario T-12, página impresa 62), BTT (§1.4–1.5, página impresa 4) y Caso (tabla del capítulo 15, página impresa 27); los PDF son imágenes sin texto extraíble, por lo que el cotejo de todas las filas se hizo con las copias Markdown de las Bases. Verificación automática: 645 filas de cinco celdas, 645 IDs únicos, 26 valores del Caso, 648 referencias numéricas SD con sección existente y 526 referencias a anexos con encabezado existente; `git diff --check` pasó. Quedan 79 filas sin sección acreditable, conforme a sus estados parcial/no cumple. La paginación exigida por BTT §1.5 sigue pendiente del documento paginado. Falta la revisión humana real de la declaración de IA. No se hizo commit.

## Estado vigente — 8 de octubre de 2026 (noche): revisión de cumplimiento del T-12

Decisión del usuario: el T-12 contiene todos los RF y RNF del Anexo del SD3 y los 374 RT de las BTT, con las cinco columnas del formulario de las BA (p. 62/77): ID requerimiento, Descripción, Cumple, Componente que lo satisface, Sección de la propuesta. Se revisó cada fila contra SD1–SD8, SD13, anexos y formularios; el resultado está en `Revision/T12_mapeo_cumplimiento.md` (Parte A 271 filas: 224 cumple, 34 parcial, 13 no; Parte B 374: 239, 76, 59). El T-12 vigente no se modificó. Hallazgos clave: secciones del T-12 apuntan al SD3 y no al desarrollo real; «Base compartida» sin producto ni versión; seis RT «No ofertado» que SD4 sí compromete; códigos del Caso cap. 15 que no coinciden con las BTT (RT-03.13, 03.24, 05.10, 09.01, 15.02, 16.14, 16.21, 16.30, 21.06); RT-13, RT-16, RT-21 y RT-15.03 casi sin desarrollo; RF del caso sin soporte en el modelo de datos del SD5; duplicados RF-19.xx / RF-14.xx-BTT y RF-07.10/07.11. Pendiente: decisión del usuario para aplicar el mapeo al T-12. Sin commit.

## Estado vigente — 8 de octubre de 2026 (noche): coherencia entre subdocumentos aplicada

Decisiones del usuario aplicadas a los Markdown de `rama-md` (sin commit):
- Infraestructura on-premise: la provee LafroX dentro del precio del contrato (BA art. 14.2; valorización en la Oferta Económica, art. 50.2). El CLIENTE compra solo el hardware de terreno (E-09). Obra civil de separación: cargo del CLIENTE, LafroX especifica y coordina (RT-06.06). SD6 6.1.3, SD7 7.1.2 y 7.B, T-14 5.1/6.1.1, T-15 §4.1/§5.2/§5.3, SD8 R8-19, C.4, E8-02 y T-16 alineados.
- Fechas de la sala (cronograma por actividad): planos mes 1, orden de compra de LafroX mes 2, instalación mes 3, recepción mes 4, racks meses 4–5, borde de los CD mes 5, gabinetes de cross-docking mes 9.
- Starlink en cinco sitios (Talca, Concepción y tres cross-docking) y ocho planes LTE en SD6 y T-14 5.3; SD1 1.6 menciona los CD.
- Ruta crítica: cadena de la Etapa 2 (H8 13 días, H9 21 días y 89,9 %, H10 28 días). La cadena del ERP (H4/H5), el H3, el planificador, los acuerdos y las cadenas son casi críticos. SD7 7.2.1/7.3.1, 7.B y T-15 §2 alineados.
- Reservas por hito: las de T-15 Tabla 5.2 (6 a 35 días); escalamiento al superar la mitad de la reserva. Corregidos 7.F, T-15 §5.4 y SD6 6.1.5.
- «CD-05» era el complemento de coordinación de datos del SD5 (3-oct); en SD4 es la coordinación de reserva y retención (4.1.4.4; Anexo 4-G; Tabla A.10; Tablas A.32 y A.33). «A31/A32» eran esas tablas antes de renumerarse. Reemplazado en SD7, 7.F, T-14, T-18, SD8 y T-16.
- Laravel: SD4 sin rastro de una versión Django (4.1.7, 4.1.8 «Implantación progresiva por olas», 4.2.4.1.3 «Implantación por olas en los sitios», Anexo 4-P).
- Nombres de módulos de SD3 en todo SD4 (títulos 4.1.4.x, Tabla 8, Anexos 4-D, 4-E, 4-F) y en T-18.
- Reversión técnica ≤ 10 min en SD4 4.2.4.1.2, SD7 Tabla 7.8 y T-18; los 4 h del Art. 78.3 son restauración de incidentes.
- RF-10 (reposición) en SD4 M2, INT-06 y Anexos 4-D/4-E/4-N; la función de abastecimiento se ejerce dentro de perfiles autorizados (SD3 Anexo 3.I), sin actor 16.
- Traslado del servidor del ERP dentro de T-14 6.3.1; T-14 6.3.3/6.3.4 con servidores y mini-PC activo/espera; T-14 4.1.2/4.1.3 corregidos; T-18 fechas prohibidas según SD4 Tabla 14.
- SD4 4.1.21 cita S-22/V-01 (instalaciones); SD4 4.3.1.4 especifica el blindaje junto a la explicación del plano del recinto (RT-06.02) y T-12 RT-06.xx remite a SD4 4.3.1.4.
- SD6: interesados alineados con los 19 actores del SD2; umbral de cobertura igual a SD1. SD2 remite la arquitectura al SD4. T-15 §5.7 explica 6 equivalentes del SOC frente a 4–5 personas del SD4.
- Resumen: T-11, T-15, T-18, SD4-Anexos y SD6 actualizados.
- Pendiente fuera del Markdown: figuras 7.5 y 7.7 del SD7 (marcar la ruta crítica de la Etapa 2) y replicar todo en LaTeX. Ediciones con gpt-6-astra medio (gpt-6.1-sol no disponible) revisadas por Claude; la revisión GPT posterior no se ejecutó por el límite de uso de Codex.

## Estado vigente — 8 de octubre de 2026: SD8 alineado con FEP04 y PMBOK 6 cap. 11

Contraste con FEP04 (d. 6–9, 18–21, 42–54, 59–68, 105, 112) y PMBOK pp. 202, 433–436, 442–444 y 456. Corregido: la Tabla C.5 usaba impacto / costo; ahora usa ahorro esperado (VE inicial − residual, con P un nivel más baja) / HH del control, y sólo R8-11 (17,0), R8-14 (4,2) y R8-18 (2,1) superan 1; los otros 18 críticos se aplican por la regla del nivel crítico. Cada ficha tiene estrategia PMBOK (Mitigar 28, Escalar R8-12/R8-17, Evitar R8-14, Aceptar activamente R8-22), efecto esperado, residual y riesgo secundario; T-16 antepone la estrategia. VE residual del registro 10.803 HH; liberable 4.273 HH. La contingencia sigue en 15.076 HH (VE inicial, FEP04 d. 47–48), forma parte de la línea base y se libera al verificar controles. 8.1.3 declara zonas de acción, tolerancia y umbral; 8.1.1 agrega análisis de reserva, auditoría de riesgos en H5/H10 e informe mensual; O8-01 con estrategia «mejorar». Resúmenes del SD8 actualizados. Pendiente: no hay riesgos de la rama externa de la RBS del PMBOK (cambio normativo, por ejemplo del SII o de la Ley 21.719); agregarlo cambia el VE total y la contingencia citada en SD7, SD13 y T-15. Sin commit.

## Estado vigente — 8 de octubre de 2026: observaciones de la revisión del SD8 corregidas

Se aplicaron en SD8, Anexos y T-16 las observaciones de `Revision/revision_comision_informe2_SD8.md`, salvo valores monetarios y magnitud de la reserva de gestión (por decisión del usuario, hasta la entrega final). Cambios: Figura 8.1 en Mermaid; apetito de riesgo en 8.1.3; mapa de los siete riesgos del Caso 19 en 8.2.1, con Concepción en R8-03 y peak de septiembre en R8-18 (sin cambiar P, I, D ni valor esperado); Tabla C.5 de costo-beneficio de los 22 críticos (HH del paquete de control del T-15 frente al impacto de B.2) y línea específica en cada ficha; glosario de códigos en 8.A; línea de seguimiento repetida movida a la introducción de 8.A; redacción de fichas y T-16; citas APA 1:1 en los tres archivos; leyendas «Tabla 8.N —»; C-04 con 12 puestos. «CD-05», «A31» y «A32» no existen en el SD4: se reemplazaron por coordinación de reserva de INT-03/04, Anexo 4-I y 4-W.5 (R8-02 y R8-06 renombrados). Siguen con esos códigos obsoletos el cuerpo del SD7 (párrafo final, sobre el Anexo 7.F), el Anexo 7.F (P7-09 y P7-10) y el T-18 (§ de CD-05). Pendientes: 13 celdas `[[REVISIÓN HUMANA]]`; Tabla C.4 con 5.000 iteraciones; imagen de la Figura 8.1 para LaTeX. Sin commit.

## Estado vigente — 8 de octubre de 2026: revisión de la Comisión sólo del SD8

`Revision/revision_comision_informe2_SD8.md` aplica el prompt del Informe 2 al SD8 tras corregir sus contradicciones. Puntaje 0 por 13 celdas `[[REVISIÓN HUMANA]]` y RBS en lista; sin la causal, 40 (antes 20). Pendientes: RBS dibujada; riesgos del Caso 19 ausentes (enlace de Concepción; peak de septiembre sobre la marcha blanca E2); costo-beneficio repetido en 32 fichas; referencias sin cita; «13 puestos» de C-04; T-16 R8-11 desalineado con 8.A; cámaras en R8-21. No se modificó ningún entregable. Sin commit.

## Estado vigente — 8 de octubre de 2026: contradicciones del SD8 corregidas

Regla del usuario: en cada contradicción manda el subdocumento anterior, salvo algo muy importante. Se corrigieron en SD8 (cuerpo, anexos y T-16) las siete contradicciones de su hoja en la planilla:
- C-12 (SD4 manda): el RPO ≤15 min se cumple con tres caminos; la falla de los tres seguida de destrucción del sitio es riesgo residual justificado (RT-02.11; SD4 4.3.2.4). Introducción, Tabla 8.1, 8.3.3, R8-05, nota de 8.B, E8-05 y T-16 R8-05 ya no dicen «aceptar el riesgo no satisface Bases».
- C-14: SD8 8.2.3 dice 89,9 % para el H9. Excepción a la regla: también se cambió SD7 7.3.1 a «al menos el 89,9 %», porque es el resultado calculado de su propio T-15 (Tabla 5.2).
- C-15: SD8 8.2.3 aclara que los 9.336 HH de soporte puente son parte de las 16.664 HH del período 16–20 de la Tabla 7.4. La etiqueta de esa fila del SD7 no se tocó.
- C-16 (SD7 7.2.2 manda): E8-01 y R8-11 describen clases de tamaño fundadas en T-12 y T-11 con tríada ±25 %, sin llamarlas «supuestas».
- C-17: «antes del H7 (mes 16) y del H12 (mes 21)» en R8-22, E8-07 y T-16.
- C-18: E8-11 dice que la subsanación consume la reserva del hito; H2–H10 (13–35 días hábiles) la absorben y el H1 (6) no.
- C-21: suspensión del proveedor de lácteos «de marzo a septiembre de 2026» en 8.3.3 y E8-08.
Se actualizaron las declaraciones de IA de los tres archivos y `Resumen/LAFROX-Subdocumento8-Resumen.md`. La planilla `.xlsx` no se modificó (estaba abierta en Excel): falta marcar la columna J de la hoja SD8. Sin commit.

## Estado vigente — 8 de octubre de 2026: segunda revisión de la Comisión y planilla de contradicciones

Se reemplazó `Revision/revision_comision_informe2.md` con una nueva corrida del prompt sobre SD1–SD8 y SD13; el SD9 no se evaluó por instrucción del usuario. Puntaje actual 0 en todos los ítems por las 204 celdas `[[REVISIÓN HUMANA]]`; sin esa causal, 23,4 sobre el 89 % evaluado. Las 22 contradicciones entre subdocumentos (8 altas, 9 medias y 5 bajas) están en `../Contradicciones_LafroX_Informe2.xlsx`, fuera del repositorio porque la rama sólo admite `.md`: hoja Registro con una fila por contradicción y una hoja por subdocumento con todas las contradicciones en que participa, sincronizadas: la acción marcada en la columna J de una hoja aparece en la columna K de la otra y el estado común se recalcula en ambas. No se modificó ningún entregable. Sin commit.

## Estado vigente — 8 de octubre de 2026: guías de lectura en Resumen

El usuario autorizó implementar el plan de `Resumen/` en la rama comprobada `rama-md`, sin cambiar de rama ni realizar commit/publicación. La carpeta contiene 26 guías independientes y `README.md`: nueve subdocumentos (1–8 y 13), siete archivos de anexos que explican 66 anexos individuales y diez formularios. Cada nombre conserva el original con sufijo `-Resumen.md`; la carpeta es plana y exclusivamente Markdown.

Las guías usan el contenido local vigente y distinguen compromisos, supuestos, cálculos y verificaciones pendientes. Se excluyen Bases, material del curso, revisiones, catálogos auxiliares y el borrador de innovaciones. No se alteraron los 26 entregables fuente. Se actualizó el acceso desde README y se registró procedencia en MANIFIESTO. Al cambiar un original se actualiza manualmente su resumen y las guías relacionadas; no existe generación automática.

Durante el cotejo final se incorporaron cambios concurrentes de los originales: SD1 y T-15 describen ahora PHP/Laravel y Kotlin; no se mantiene como pendiente la antigua diferencia con Python/Django. La contingencia adicional vigente del SD8 es 13.223 HH; la cifra histórica 12.004 HH del contexto no se trasladó como diferencia actual al SD7. Siguen descritas diferencias vigentes: doce resultados E1 en el cuerpo SD7 frente a catorce con verificaciones E1 en 7.C/T-18, y responsabilidades/fechas de sala técnica entre SD6, T-11 y T-15. Las guías no las corrigen ni acreditan aceptación.

Verificación completada: 27 archivos Markdown en Resumen, correspondencia uno a uno de los 26 documentos, 66 anexos cubiertos exactamente una vez, 280 enlaces locales con destino y ancla válidos, 24 comprobaciones de cifras clave en las fuentes y tres comprobaciones aritméticas. `git diff --check` pasó. Los hashes de los 26 originales permanecieron iguales respecto de la última lectura completa tras las actualizaciones concurrentes; las únicas modificaciones de esta tarea fuera de Resumen son README, MANIFIESTO y este contexto.

Los encabezados de rama/alcance de los registros anteriores son históricos; esta autorización explícita gobierna la creación de la carpeta Resumen en `rama-md`. La asistencia de IA en las guías no constituye revisión humana adicional de los originales.

## Estado vigente — 8 de octubre de 2026: auditoría de indicios de IA (§7.1)

Se aplicó en las carpetas 01–08 y 13 la auditoría de indicios de IA de las Aclaraciones §7.1. El informe completo está en `Revision/auditoria_indicios_IA.md`.
- **Arreglos aplicados:** PUCV → Distribuidora Puelche (2026a–d); figuras PNG del SD5 enlazadas; limpieza de restos PDF/LaTeX; numeración de tablas, figuras y subtítulos del SD7; reescritura de notas de proceso; normalización de las 24 declaraciones de IA, con `[[REVISIÓN HUMANA]]` donde no hay revisión con nombre; tablas y cálculos nuevos en SD2, SD6 (valor ganado), SD7 (HH por etapa) y SD8 (FMEA top-5); stack del SD1 alineado con Laravel/PHP y Kotlin.
- **Pendiente del equipo:** completar `Revision/plantilla_revision_humana_IA.md` (204 celdas).
- **Contradicciones no corregidas por decisión del usuario:** cámaras, Starlink y sala; nombres de módulos e INT-04; meses de hitos en T-14 y T-16.
- **Pendiente antes de compilar:** replicar todo en LaTeX.

Sin commit.

## Estado vigente — 8 de octubre de 2026: SD13 consolidado

Se crearon `13_innovaciones/LAFROX-Subdocumento13.md`, `LAFROX-Subdocumento13-Anexos.md` (13.A contratos inn01–inn05, 13.B trazabilidad, 13.C indicadores y riesgos, 13.D observaciones) y `LAFROX-Formulario-T-19.md` (5 fichas × 17 campos), a partir de `innovaciones_corregidas.md`. Ese archivo de trabajo se conserva sin versionar y no es entregable. El SD13 se alinea sin cambios con los paquetes, meses y HH de T-14, T-15 y Anexo 7.D.
- Riesgos: se usa la escala 1–5 del SD8 con las fichas R8-23 a R8-29.
- Corrección técnica: se cita 10.920 mensajes diarios (SD4) y CloudWatch sin Grafana.
- Responsables: Chamorro y Henríquez dirigen hasta el mes 21. Después, los paquetes 8.3.x siguen con las siglas DAT e IMP del T-14, en el frente F8 de Castillo; Calidad aprueba los parámetros y Seguridad el bloque 4. No se cambiaron siglas en T-14 ni T-15.

Ajustes cruzados:
- T-12: RT-05.30 «Sí (E1)» mediante INN-03; RT-26.01 a 26.07 remiten al Capítulo 13 y al T-19; RT-26.08 «Sí (E1)» mediante INN-01, INN-02 e INN-03.
- SD5 y SD5-Anexos: 10.920 (28×174) y RT-05.30 ofertado.
- SD8-Anexos: R8-25 redefinida (avisos no confirmados o sin catálogo) y causas secundarias en R8-26, R8-27 y R8-29, sin cambiar P, I, D ni valor esperado; nombres completos en 8.F.
- T-16: mitigación de R8-25.
- SD7: nombres completos en la tabla de innovaciones.

Avisados y no tocados:
- §4.1.6 del SD4 sin contratos inn.
- Nombres M7, M8 y M9 en la Tabla 8 del SD4.
- Python/Django en la Tabla 1.1 del SD1.
- RF-09.06 y RF-08.05 del CSV.
- Impresoras 106 frente a 110.
- Contingencia 12.004 frente a 13.223 HH.
- La columna de revisión humana de la declaración de IA del SD13 lleva marcas «[Integrante: completar…]» que el equipo debe llenar antes de entregar. Sin commit.

## Estado vigente — 7 de octubre de 2026: cronograma por actividad y SD8 cuantitativo

SD7: T-15 §6 programa 564 actividades de 163 paquetes con entregable (≤80 HH, ≤1 quincena) con dependencias del Anexo 7.B (D-16/18/19 por interfaz, D-21b nueva), revisión Art. 18.3 y nivelación con la dotación del SD1; 59 paquetes de esfuerzo continuo por ocurrencia. Total 202.774 HH, peak 69 (mes 15). Reservas por hito en T-15 Tabla 5.2. El usuario aceptó: refuerzo de calidad con evaluadores subcontratados hasta 16/día (meses 9–12 y 16–18, SD6 §6.1.3), compra del CLIENTE dentro del mes siguiente a 5.1.2, y la calibración de escalas del SD8 (P: 5/20/40/60/80 %; I: 0/5/10/20/30 % del esfuerzo afectado). SD8: 32 riesgos, valor esperado 15.076 HH (contingencia adicional 12.004 HH), Monte Carlo con P(H9)=90 % y demás ≥97,7 %, P80 de todos los hitos dentro de su límite. Preferencia del usuario: mover lo menos posible los otros subdocumentos. Material del ramo en `clases + pmbok/` como consultor.

## Estado vigente — 5 de octubre de 2026

Limpieza adicional autorizada: se retira el archivo informativo de anexos del SD1 porque no incorpora anexos complementarios. `01_presentacion_empresa/` conserva cuerpo y T-6; SD3 y SD4 conservan sus tres entregables. El usuario solicita registrar toda esta limpieza en el commit `limpieza de archivos` y publicarlo en `alvaro-md`. Los originales eliminados permanecen recuperables en Git.

Rama comprobada: `alvaro-md`. El usuario autorizó ejecutar y publicar el plan SD3–SD4 con los quince actores de sistema validados con el redactor del SD3, implementado en `26c345c`. SD3 se actualizó desde las inclusiones activas de `Descargas/03_esquema_solucion_alcance/03_esquema_solucion_alcance`; se añadió 3.4.2.1 y matriz de actores, realizada en la lógica del SD4 y Anexo 4-N. CD-05 está integrado en reglas, contratos, volumen y pruebas. Por solicitud posterior, SD3 y SD4 conservan solo cuerpo, anexos y formulario; se eliminan manifiestos de capítulo, registros auxiliares y copias por partes. Editar directamente los tres entregables del capítulo, sin recrear auxiliares. Física, centros de datos, memoria y T-11 conservan su contenido. `md para drive/` es una exportación no versionada y antigua; no forma parte de esta limpieza. Los textos siguientes son historia de sesión.

Dependencias preservadas tras retirar los registros del capítulo: SD2 S-09 y RF-03.11/12 permiten precio al despacho con excepciones mientras SD3 RNG-08 conserva precio pactado; requiere decisión comercial coordinada. CD-05 añade 2N + 2L mensajes y debe incorporarse al dimensionamiento físico; las pruebas AL-STOCK-01 y AL-ACT-01 están descritas, no ejecutadas. Las figuras históricas requieren cotejo de actores/etapas y las aclaraciones cuestionan recortes. La contingencia manual no acredita los 96 despachos críticos. Fechas ADR, revisión humana final, FinOps y el límite residual de DR conservan su estado pendiente; no declarar conformidad total por la limpieza. La evidencia documental original permanece recuperable en el commit `26c345c`.

Este archivo mantiene el contexto mínimo y vigente para trabajar en la rama `branch-md` del repositorio LafroX sin completar vacíos mediante suposiciones. Debe leerse junto con `AGENTS.md` al iniciar o retomar una sesión.

## Identidad y protocolo

- Proyecto y proponente: **LafroX**.
- Licitación académica ficticia: **TFEP-01/2026, Caso 02 — Logística, Distribuidora Puelche S.A.**
- Toda respuesta final del asistente comienza exactamente con `## LafroX`.
- El trabajo y los documentos se redactan en español.

## Regla obligatoria de integridad de branch-md

- Esta es la rama `branch-md` del repositorio LafroX. Solo se crean, editan y versionan documentos `.md`; los metadatos internos de Git son la única excepción.
- Toda petición de crear, editar, compilar, renderizar o convertir contenido a LaTeX debe rechazarse tajantemente dentro de esta rama. No crear archivos `.tex`, `.cls`, `.sty`, plantillas, comandos de compilación ni derivados PDF.
- Respuesta requerida: «No realizaré trabajo en LaTeX en branch-md: esta rama es exclusivamente Markdown y debo preservar su integridad. Puedo resolver la petición en Markdown».
- No cambiar automáticamente de rama, importar archivos LaTeX ni escribir en otro checkout para eludir esta restricción.
- Antes de editar, comprobar que la rama activa sea `branch-md`. Antes de registrar cambios, comprobar que todos los archivos a versionar terminen en `.md`.
- Leer `compct/CONTEXTO_SESION.md` al iniciar o reanudar una sesión. Cada respuesta final comienza exactamente con `## LafroX`.

## Objetivo vigente

Este repositorio es una base documental exclusivamente Markdown para crear, mantener y revisar los Subdocumentos 1, 2 y 3. Incluye sus anexos, los Formularios T-6 y T-12, las Bases rectoras, los catálogos originales de requerimientos y el prompt de revisión.

No contiene arquitectura, subdocumentos 4–14, históricos, binarios, plantillas LaTeX ni herramientas de generación. Una referencia a esos materiales identifica una dependencia futura; no demuestra que el material esté disponible.

## Fuentes de verdad y precedencia

1. `Bases/Bases_Administrativas.md`.
2. `Bases/Bases_Tecnicas_Transversales.md`.
3. `Bases/Caso_02_Logistica.md`.
4. `Bases/aclaraciones-licitacion.md`, posterior y obligatoria para estructura, archivos y presentación.

El caso puede endurecer un requisito transversal, pero no rebajarlo. Ante una contradicción, se registra la inconsistencia o una consulta al mandante; no se corrige silenciosamente.

## Estado confirmado del repositorio

- Las cuatro Bases son copias íntegras de las fuentes del repositorio LafroX al momento de crear este repositorio.
- El Subdocumento 1, su anexo y el Formulario T-6 están convertidos a Markdown y permanecen en archivos separados.
- El Subdocumento 2 y sus anexos están convertidos a Markdown y permanecen en archivos separados.
- Hay diez figuras transcritas como descripciones textuales: un organigrama, seis procesos AS-IS y tres esquemas del Subdocumento 3.
- `Requerimientos/Consolidado_RF.md` contiene 134 registros provenientes del CSV original.
- `Requerimientos/Consolidado_RNF.md` contiene 24 registros provenientes del CSV original.
- `Requerimientos/Requerimientos_Bases.md` conserva las 61 filas físicas y las dos familias de columnas del CSV original.
- `Revision/prompt_revision_comision_informe2.md` adapta la revisión a evidencia por archivo y sección. Las verificaciones exclusivas del PDF quedan pendientes.
- Estado vigente: rama `branch-md` del repositorio LafroX. La copia independiente `LafroX-Markdown` es el origen de importación, no la rama de trabajo. No se ha publicado esta rama.

## Controles contra alucinaciones

Antes de afirmar un dato, requisito, estado o decisión:

1. Buscarlo en las cuatro Bases respetando su precedencia.
2. Verificar si aparece en los subdocumentos o catálogos incluidos.
3. Citar el archivo y la sección que lo sostienen.
4. Si la fuente no está incluida o el dato no está definido, escribir `no verificable con el material disponible` o registrarlo como vacío, supuesto o consulta.
5. No presentar como acreditados los proyectos, certificaciones, alianzas, contactos o antecedentes corporativos del Subdocumento 1 sin evidencia documental externa.
6. No completar celdas vacías de los catálogos sin una fuente verificable.
7. No declarar aprobada la presentación formal: paginación, firma, folio, tipografía y legibilidad se comprueban únicamente en los PDF finales.

## Convenciones de mantenimiento

- Solo se agregan archivos `.md`, además de los metadatos internos de Git.
- Subdocumentos, anexos y formularios permanecen separados.
- Las figuras enlazan su imagen real; el PDF se compila desde LaTeX. Ver la regla de AGENTS.md sobre indicios de IA (Aclaraciones §7.1).
- Toda ampliación del alcance se registra primero en este archivo, en `README.md` y en `MANIFIESTO.md`.
- Después de cada cambio sustantivo se actualiza la sección siguiente para permitir una reanudación segura.

## Último estado de trabajo

**Fecha:** 2026-09-28.

**Completado:** importación de los 17 documentos Markdown a `branch-md`, preservando el contenido documental e incorporando la prohibición explícita de trabajar en LaTeX. La comparación con `tablas_anexo` del Subdocumento 3 detectó diferencias de cantidades, nombres y códigos; los catálogos Markdown no se sustituyeron.

**Siguiente paso:** continuar la revisión o edición de los Subdocumentos 1, 2 y 3 usando únicamente las fuentes incluidas. Cualquier incorporación de arquitectura o de los Subdocumentos 4–14 requiere ampliar expresamente el alcance.

## Última actualización: incorporación del Subdocumento 3

Petición vigente: trasladar todo el material relevante del Subdocumento 3 en exactamente tres documentos Markdown, conservando sus errores. Se incorporaron cuerpo, anexos 3.A–3.K, las 14 tablas de la colección complementaria `tablas_anexo`, tres figuras transcritas y T-12. El T-12 mantiene 174 RF, 90 RNF y 374 RT. La colección complementaria conserva 90 RF y 40 RNF aunque anuncia 91 y 41. Estas versiones no fueron reconciliadas ni sustituyen los CSV convertidos en `Requerimientos/`. Próximo paso: revisión del contenido si el usuario la solicita; no dar por corregidas las discrepancias.

## Ampliación autorizada — ejecución de mejora SD5, 2026-10-03

La rama de esta copia es alvaro-md. El usuario autorizó ejecutar el plan SD5 en el checkout de alvaro-modelo-y-gestion-de-datos y sus correcciones coordinadas. Esta copia permanece exclusivamente Markdown. SD1 corrige la responsabilidad específica del líder de desarrollo a Laravel/PHP; SD4 conserva fuente histórica y añade complemento CD-05 de coordinación de reserva y custodia. T-12 y los catálogos originales no se renumeran ni amplían; RT-05.10/24/30 BTT permanecen no ofertados.

## Revisión de la Comisión — Informe 2, 2026-10-07

Se aplicó `Revision/prompt_revision_comision_informe2.md` a todo el repositorio, sin comprobaciones de forma; el resultado está en `Revision/revision_comision_informe2.md`. Total 1,2 sobre 97 % evaluado: SD1, SD3, SD4, SD6, SD7 y SD8 quedan en 0 por indicios del §7.1 (declaración de IA «Alto» sin revisión humana y notas de proceso en el texto); SD2 queda en 20 por la contradicción de S-09 con el SD3; SD5, SD9 y SD13 no están presentados. No se modificó ningún entregable.

## Revisión de coherencia del SD8 — 2026-10-07

Se corrigió el SD8 (cuerpo, anexos y T-16) según el plan aprobado: Figura 8.1 (RBS) derivada de las 32 fichas del Anexo 8.A; contingencia adicional de 13.223 HH, porque la capacidad protegida E1 sólo absorbe R8-02, R8-04 y R8-14 (1.853 HH); hitos H6, H7, H11 y H12 justificados como no simulados; notas de redondeo y de muestreo de la Tabla C.4; fuentes «Aclaraciones §11, 8.2»; referencias 2026a–d, ISO 31000 e IEC 60812 citadas en el texto; se retiraron las notas de proceso y las menciones al SD5, y se eliminaron E8-11 y E8-12 (las condiciones siguientes se renumeraron). Por decisión del usuario se trajeron desde `LafroX_Markdown` el SD2-Anexos, el SD3, el SD3-Anexos y el T-12 con la regla única de precio acordado al capturar el pedido (S-09, RNG-08, RF-03.11/12) y la reversión del SD3 alineada con el SD7. Pendientes avisados: revisión humana real de las declaraciones de IA, Tabla 6.3 del SD6 (sala en mes 5 frente a meses 3–4 del T-15) y brecha de RPO del SD4. Sin commit.

## Sincronización del Subdocumento 4 — 2026-10-07

Los tres entregables Markdown de `04_arquitectura/` se actualizaron desde las fuentes LaTeX vigentes del checkout hermano `LafroX` mediante `00/herramientas/tex2md.py`. El cotejo previo quedó en `LafroX/00/trazabilidad/ACREDITACION_LATEX_MD_SUBDOC4_2026-10-07.md`. La sincronización incorpora la redundancia activo/en espera de Concepción y cross-docking, T-11, 230.252/353.333 mensajes diarios, 9 terminales de cross-docking, 2.283 contactos/mes de capacidad base de mesa y el retiro de dos importes históricos. Los 26 enlaces de figuras del cuerpo apuntan ahora a los archivos de la revisión LaTeX publicada `d397c30`, incluidos los tres diagramas físicos actualizados; ya no dependen de rutas al checkout hermano. Se eliminaron además un resto `A.table` de los anexos y siete prefijos `l` espurios en categorías del T-11. No se creó LaTeX ni PDF en `rama-md`.
