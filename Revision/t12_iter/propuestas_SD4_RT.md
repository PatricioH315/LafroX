# LafroX — Propuestas de arquitectura para RT pendientes del T-12

Este informe de trabajo presenta 21 propuestas sin incorporarlas a los entregables ni cambiar sus estados en el T-12: siete obligatorias, una según caso y trece deseables. Los textos de los requisitos y su carácter se reproducen de las Bases Técnicas Transversales; las páginas son las impresas verificadas en la especificación de la tarea. Los borradores deben aprobarse con su alcance, recursos y datos pendientes antes de integrarlos.

## Fuentes y método de búsqueda

Se buscaron las materias en los 25 entregables vigentes de SD1–SD8 y SD13 (cuerpos, anexos y formularios, excluido T-12), y se contrastaron después las 645 filas del T-12 y los catálogos originales de Requerimientos. La búsqueda cubrió sinónimos de navegación, diseño, preferencias, parametrización, flujo, plantillas, auditoría, firma, simulación, autoatención, energía, carbono, pruebas, madurez y canales; se leyeron las secciones de soporte antes de proponer. Una coincidencia en un requisito o una actividad futura no se considera implementación acreditada. La arquitectura elegida sigue siendo Laravel/PHP, Angular 22/Tailwind, Kotlin, Keycloak y los servicios AWS ya declarados.

Las abreviaturas de este informe identifican estos archivos reales:

- SD3: `03_esquema_solucion_alcance/LAFROX-Subdocumento3.md`; SD3-Anexos: `03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md`.
- SD4: `04_arquitectura/LAFROX-Subdocumento4.md`; SD4-Anexos: `04_arquitectura/LAFROX-Subdocumento4-Anexos.md`.
- SD5: `05_modelo_datos/LAFROX-Subdocumento5.md`; SD5-Anexos: `05_modelo_datos/LAFROX-Subdocumento5-Anexos.md`.
- T-11: `04_arquitectura/LAFROX-Formulario-T-11.md`.
- T-12: `03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md`.
- T-14/T-15: `07_PlanDeTrabajo_EDT_Cronograma_Implantación/LAFROX-Formulario-T-14.md` y `LAFROX-Formulario-T-15.md` en la misma carpeta.
- SD8: `08_plan_riesgos/LAFROX-Subdocumento8.md` y `LAFROX-Subdocumento8-Anexos.md`.
- SD13: `13_innovaciones/LAFROX-Subdocumento13.md` y sus anexos.

Las recomendaciones de deseables comparan mérito técnico, esfuerzo y riesgo de contradicción. No se asigna un puntaje unitario por RT ni HH nuevas sin una ponderación y estimación acreditadas. La Oferta Económica no está disponible en este checkout: sus impactos son rubros pendientes, no importes verificados. Ninguna propuesta autoriza reducir las capacidades o compromisos vigentes.

## Obligatorios

Estas siete materias requieren desarrollo concreto para cerrar sus filas; los datos faltantes se indican fuera del borrador de oferta.

### RT-13.05 — Acceso a funciones principales en tres interacciones

**Carácter:** Obligatorio. **Fuente:** Bases Técnicas Transversales, cap. 13, p. 26. **Estado vigente:** No cumple.

**Texto exacto del RT:** «Ninguna funcionalidad principal requerirá más de tres interacciones desde la pantalla de inicio del perfil correspondiente.»

**Base ya existente:** `04_arquitectura/LAFROX-Subdocumento4.md`, 4.1.3.1, define aplicaciones por perfil; su apartado «Actores del sistema, interfaces y autorización» y `03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md`, 3.I, identifican los quince actores. `07_PlanDeTrabajo_EDT_Cronograma_Implantación/LAFROX-Formulario-T-14.md`, cuenta 2.6, paquetes 2.6.1–2.6.3, ya programa investigación, prototipos e indicadores.

**Qué falta:** No hay inventario de funciones principales por perfil ni conteo desde el inicio; las pruebas de usabilidad generales no comprometen el límite.

**Opción recomendada:** Organizar accesos principales por perfil en Angular y Kotlin; mantener una matriz función–perfil–secuencia en la documentación de aceptación. Verificar por separado acceder a la función y completar sus datos, sin excluir pasos de acceso ni sustituir la prueba por el número de menús.

**Sección destino exacta:** SD4 4.1.3.1, después de «Actores del sistema, interfaces y autorización».

**Borrador listo para pegar:**

> Cada perfil dispone de una pantalla de inicio con accesos directos a sus funcionalidades principales. Ninguna requiere más de tres interacciones para acceder desde ese inicio. El inventario por perfil identifica la función, la secuencia y el número de interacciones; se comprueba en los prototipos y se repite en la aceptación de portales, consola y aplicaciones Kotlin. Los permisos determinan los accesos visibles y los pasos de autenticación se documentan separadamente de la navegación desde una sesión iniciada. (Bases Técnicas Transversales, cap. 13, p. 26).

**Dato que debe definir el equipo:** Inventario definitivo de funciones principales por los quince perfiles y convención de conteo acordada con el CLIENTE; no declarar probado el límite antes de recorrer cada secuencia.

**Impactos coordinados:** SD3: vincular los flujos del Anexo 3.I y sus criterios, sin nuevos actores. SD5: no necesita entidades nuevas. T-11: sin hardware adicional. T-14/T-15: revisar alcance y HH de 2.6 y de 3.8.2/3.9.2; no asumir horas disponibles. SD8: tratar riesgo de retrabajo/adopción. Oferta Económica: valorar diseño y pruebas; sin proveedor adicional.

**Complejidad:** Media. **Recomendación:** Aplicar por obligación.

### RT-13.09 — Sistema de diseño documentado

**Carácter:** Obligatorio. **Fuente:** Bases Técnicas Transversales, cap. 13, p. 26. **Estado vigente:** No cumple.

**Texto exacto del RT:** «Existirá un sistema de diseño documentado con paleta de colores acotada, jerarquía tipográfica de a lo más dos familias, iconografía coherente, retícula y componentes reutilizables.»

**Base ya existente:** `04_arquitectura/LAFROX-Subdocumento4.md`, 4.1.3.1 y 4.1.7, selecciona Angular 22/Tailwind y Kotlin nativo; `04_arquitectura/LAFROX-Subdocumento4-Anexos.md`, 4-P, Tabla A.19, gobierna las dependencias; T-14, cuenta 2.6, programa los prototipos. Ninguno define aún el sistema completo.

**Qué falta:** Paleta acotada, jerarquía de hasta dos familias tipográficas, iconografía, retícula y catálogo de componentes con estados y uso.

**Opción recomendada:** Documentar tokens de diseño comunes y realizarlos mediante Tailwind/componentes Angular y equivalentes nativos Kotlin; compartir especificaciones visuales y de interacción, no imponer código web a Zebra.

**Sección destino exacta:** SD4 4.1.3.1; detalle del sistema en Anexo 4-P, dentro del inventario de presentación.

**Borrador listo para pegar:**

> La presentación utiliza un sistema de diseño documentado con paleta acotada, jerarquía tipográfica de a lo más dos familias, iconografía coherente, retícula y espaciado definidos y componentes reutilizables. Cada componente especifica sus estados, uso por perfil, adaptación de pantalla y comportamiento accesible. Los tokens se implementan en Tailwind para los portales y la consola Angular y se reproducen en los componentes nativos Kotlin. La aceptación contrasta las pantallas y sus estados con el catálogo aprobado, incluidos contraste, foco y mensajes de error. (Bases Técnicas Transversales, cap. 13, p. 26).

**Dato que debe definir el equipo:** Paleta, tipografías y licencias, biblioteca de iconos y catálogo inicial; deben cumplir también el máximo de cinco colores principales del RT-25.05 si se aplican al prototipo.

**Impactos coordinados:** SD3: incorporar trazabilidad de RT-13.09 y coherencia con RT-25.05, sin modificar catálogos originales. SD5: sin cambio estructural. T-11: sin cambio. T-14/T-15: estimar sistema y aplicación a perfiles en 2.6 y pruebas 3.8/3.9. SD8: retrabajo, licencias y accesibilidad. Oferta Económica: HH y eventual licencia tipográfica/iconográfica, sin atribuir contratación existente.

**Complejidad:** Media. **Recomendación:** Aplicar por obligación.

### RT-16.04 — Límite entre parametrización y desarrollo

**Carácter:** Obligatorio. **Fuente:** Bases Técnicas Transversales, cap. 16, p. 29. **Estado vigente:** No cumple.

**Texto exacto del RT:** «El PROPONENTE declarará expresamente qué elementos son parametrizables y cuáles requieren desarrollo. Presentar como parametrizable lo que exige desarrollo se evaluará como observación grave.»

**Base ya existente:** `05_modelo_datos/LAFROX-Subdocumento5-Anexos.md`, 5-A, define `mae_parametro` y `mae_parametro_version`; 5-C gobierna sus dominios. `04_arquitectura/LAFROX-Subdocumento4.md`, 4.1.4.2 y 4.1.4.5, desarrolla reglas térmicas y de rutas. SD3-Anexos 3.A incluye RF-17.02; el T-12 lo mantiene parcial por falta de administración general.

**Qué falta:** Inventario expreso por elemento, ámbito, permisos y límites; disponer de un valor JSON versionado no demuestra administración sin desarrollo.

**Opción recomendada:** Inventariar por módulo las claves, tipos, rangos, dueño y vía de edición; construir administración Angular respaldada por políticas Laravel. Distinguir parámetros habilitados de código, esquema, contratos e integraciones.

**Sección destino exacta:** SD4 4.1.3.4, como párrafo de gobierno de reglas; inventario detallado en Anexo 4-P.

**Borrador listo para pegar:**

> Son parametrizables desde la consola del CLIENTE los umbrales, plazos, montos, tolerancias, catálogos, listas y textos que figuren expresamente en el inventario de parámetros habilitados de cada módulo. Cada entrada declara tipo, validación, ámbito, dueño, permiso, versión y vigencia, con auditoría de quién cambió qué y cuándo. Exigen desarrollo los cambios de algoritmo, estructura de datos, contratos de integración y reglas que no estén incluidas en ese inventario. La consola rechaza claves o valores fuera del catálogo; almacenar un valor como JSON no convierte en parametrizable una función que necesita programación. (Bases Técnicas Transversales, cap. 16, p. 29).

**Dato que debe definir el equipo:** Inventario por M1–M12 y responsables del CLIENTE; aprobarlo antes de sustituir el RT por Cumple.

**Impactos coordinados:** SD3: revisar RF-17.02 y RT-16.02/04 conjuntamente. SD5: complementar restricciones, tipos y ámbitos de `mae_parametro_version` en 5-A/5-C. T-11: consola existente; sin equipo nuevo. T-14/T-15: asignar construcción de administración y pruebas a la base compartida y 3.8/3.9, con HH propias si falta cobertura. SD8: cambios erróneos y privilegios. Oferta Económica: construcción y mantenimiento; no tratarlo como simple declaración gratuita.

**Complejidad:** Media. **Recomendación:** Aplicar por obligación.

### RT-16.08 — Consulta y exportación de auditoría por el CLIENTE

**Carácter:** Obligatorio. **Fuente:** Bases Técnicas Transversales, cap. 16, p. 29. **Estado vigente:** No cumple.

**Texto exacto del RT:** «El CLIENTE podrá consultar y exportar la auditoría desde la interfaz, con filtros por persona, período, entidad y tipo de operación, sin requerir acceso a la base de datos.»

**Base ya existente:** `04_arquitectura/LAFROX-Subdocumento4.md`, 4.1.3.7, conserva auditoría de negocio; 4.1.3.8 ofrece tableros de observabilidad. `05_modelo_datos/LAFROX-Subdocumento5-Anexos.md`, 5-A, define `gob_auditoria` con actor, entidad, operación y fechas; SD5 5.2.8 propone exportación autónoma masiva. El tablero técnico no acredita la consulta filtrada de auditoría.

**Qué falta:** Pantalla autorizada con los cuatro filtros exigidos y descarga del resultado sin acceso directo a la base.

**Opción recomendada:** Añadir una vista Angular de auditoría con API Laravel paginada; aplicar alcance por rol/sitio, filtros del registro e historial de consultas/exportaciones. Exportar CSV UTF-8 o JSON; usar trabajo asíncrono cuando el volumen lo exija.

**Sección destino exacta:** SD4 4.1.3.7, al final de «Clasificación, cifrado y custodia».

**Borrador listo para pegar:**

> El CLIENTE dispone en la consola de una consulta de auditoría con filtros combinables por persona, período, entidad y tipo de operación y puede exportar el resultado en CSV UTF-8 o JSON. Una API Laravel autorizada aplica el alcance de consulta, pagina los resultados y genera las exportaciones extensas como trabajos asíncronos con consulta de avance y descarga protegida. No se requiere acceso directo a la base de datos. Cada consulta sensible y exportación conserva actor, filtros, alcance y fecha en la auditoría; la aceptación prueba los cuatro filtros y la denegación fuera de los permisos del perfil. (Bases Técnicas Transversales, cap. 16, p. 29).

**Dato que debe definir el equipo:** Roles autorizados, límite de consulta/volumen y plazo de conservación de exportaciones, coordinados con SD5 5-D.

**Impactos coordinados:** SD3: actualizar evidencia de RT-16.08 y coordinar con RF-17.04, que exige registro e inalterabilidad y no queda acreditado solamente con filtros. SD5: revisar índices 5-F, permisos y retención 5-D/5-E de `gob_auditoria`. T-11: servicios existentes. T-14/T-15: construir y probar vista/API/exportador y valorar HH. SD8: exposición de información y costo de consultas. Oferta Económica: capacidad de exportación y mantenimiento.

**Complejidad:** Media. **Recomendación:** Aplicar por obligación.

### RT-16.12 — Configuración de responsables, plazos y aprobaciones

**Carácter:** Obligatorio. **Fuente:** Bases Técnicas Transversales, cap. 16, p. 30. **Estado vigente:** No cumple.

**Texto exacto del RT:** «Los flujos serán configurables por el CLIENTE sin desarrollo, al menos en lo relativo a responsables, plazos y niveles de aprobación.»

**Base ya existente:** `04_arquitectura/LAFROX-Subdocumento4.md`, 4.1.3.5, «Orquestación y coreografía», desarrolla flujos acotados de excepciones; Anexo 4-B, Tabla A.3, incluye bandeja de excepciones. `05_modelo_datos/LAFROX-Subdocumento5-Anexos.md`, 5-A, dispone de `gob_asignacion` y parámetros versionados; SD3-Anexos 3.A declara RF-17.06.

**Qué falta:** Interfaz del CLIENTE para configurar sin desarrollo los tres elementos y persistencia de definiciones/versiones e instancias del flujo.

**Opción recomendada:** Usar un ejecutor de estados en Laravel y configuración Angular para los flujos definidos, con tablas de definición/versiones/aprobaciones. No introducir un motor BPM nuevo ni confundir configuración de responsables con modificación del algoritmo.

**Sección destino exacta:** SD4 4.1.3.5, «Orquestación y coreografía»; ampliar la bandeja del Anexo 4-B.

**Borrador listo para pegar:**

> Los flujos definidos de aprobación y tratamiento de excepciones permiten al CLIENTE configurar responsables, plazos y niveles de aprobación desde la consola, sin desarrollo. Cada definición tiene versión, ámbito y vigencia; las instancias conservan la versión con la que comenzaron y registran asignaciones, vencimientos y decisiones. El ejecutor Laravel valida los permisos y la secuencia de aprobaciones antes de aplicar una definición. Cambiar las reglas de negocio o incorporar transiciones no habilitadas requiere desarrollo. La aceptación modifica los tres elementos mediante un perfil autorizado del CLIENTE y comprueba su efecto sobre nuevas instancias y la continuidad de las existentes. (Bases Técnicas Transversales, cap. 16, p. 30).

**Dato que debe definir el equipo:** Flujos iniciales, delegación por ausencia y reglas de vencimiento/escalamiento de RF-17.06; ese RF exige más elementos que este RT y podría seguir parcial.

**Impactos coordinados:** SD3: coordinar RF-17.06 y RT-16.11/12, distinguiendo sus exigencias. SD5: añadir definiciones, versiones, instancias y aprobaciones; `gob_asignacion` sola no basta. T-11: sin motor ni servidor adicional por defecto. T-14/T-15: construcción y pruebas en base compartida/módulos y 3.8/3.9 con nueva estimación. SD8: aprobaciones indebidas, vencimientos y migración de flujos activos. Oferta Económica: HH de desarrollo y soporte.

**Complejidad:** Alta. **Recomendación:** Aplicar por obligación.

### RT-16.19 — Documentos desde plantillas del CLIENTE

**Carácter:** Obligatorio. **Fuente:** Bases Técnicas Transversales, cap. 16, p. 30. **Estado vigente:** No cumple.

**Texto exacto del RT:** «La solución generará documentos a partir de plantillas administrables por el CLIENTE, con datos de la transacción y salida en formato abierto.»

**Base ya existente:** `03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md`, 3.A, contiene RF-17.09. SD4 4.1.17 y Anexo 4-U separan POD, guía y acuse. SD5-Anexos 5-A dispone de objetos documentales y `not_plantilla`, que solo es plantilla de avisos; no demuestra un catálogo de plantillas documentales.

**Qué falta:** Administración por el CLIENTE, vínculo con datos de transacción y generación en formato abierto; separar documentos operacionales de emisión tributaria exclusiva del ERP.

**Opción recomendada:** Servicio Laravel para validar y rellenar plantillas declarativas versionadas; editor/administrador Angular limitado a campos autorizados. Renderer aislado sin macros ni ejecución de código, salida PDF interoperable y conservación del original.

**Sección destino exacta:** SD4 4.1.3.4, servicio transversal de documentos; correspondencia documental en Anexo 4-U.

**Borrador listo para pegar:**

> La solución genera documentos operacionales desde plantillas administrables por el CLIENTE en la consola. Las plantillas tienen versión, vigencia y campos autorizados que se completan con los datos de la transacción identificada; el generador valida su estructura y produce una salida PDF interoperable, conservando transacción, versión de plantilla y objeto generado. Se ofrece previsualización antes de publicar y se impide ejecutar código o macros en las plantillas. El servicio no emite DTE: el ERP mantiene su autoridad tributaria. La aceptación modifica una plantilla mediante un perfil del CLIENTE y comprueba el contenido y la apertura del resultado con una herramienta independiente. (Bases Técnicas Transversales, cap. 16, p. 30).

**Dato que debe definir el equipo:** Tipos de documento, variables autorizadas, formato(s) de entrada y herramienta de renderizado compatible con PHP/Laravel, con licencia y mantenimiento comprobados.

**Impactos coordinados:** SD3: revisar RF-17.09 y alcance de documentos; no atribuirlo a `not_plantilla`. SD5: catálogo/versiones de plantilla documental, campos permitidos y enlace de objeto generado en 5-A/5-D. T-11: confirmar runtime sin nuevo servidor por defecto. T-14/T-15: nuevo alcance de servicio/editor y pruebas; estimar HH. SD8: inyección en plantillas, fuga de datos y confusión tributaria. Oferta Económica: HH y eventual licencia de renderer.

**Complejidad:** Media. **Recomendación:** Aplicar por obligación.

### RT-16.33 — Estimación e indicador de reducción de atención asistida

**Carácter:** Obligatorio. **Fuente:** Bases Técnicas Transversales, cap. 16, p. 31. **Estado vigente:** No cumple.

**Texto exacto del RT:** «El PROPONENTE estimará la reducción esperada del volumen de atención asistida por efecto de la autoatención y comprometerá el indicador.»

**Base ya existente:** SD4 4.1.3.1 desarrolla autoatención; Anexo 4-W.7 dimensiona capacidad de mesa, que no es una medición del volumen asistido actual. SD3 3.4.5 conserva canal asistido. T-14, cuenta 8.1, cubre el servicio; SD13 13.5.2 distingue la autoatención obligatoria de INN-05. No hay base observada ni meta de reducción.

**Qué falta:** Estimación fundamentada de reducción, línea base comparable, meta comprometida e indicador; ni la capacidad mensual de la mesa ni los indicadores I-05 prueban esa reducción.

**Opción recomendada:** Clasificar contactos por motivo/canal en la mesa y eventos completados en portal; comparar tasas por igual volumen de transacciones y segmento. Estimar la reducción a partir de consultas elegibles y adopción documentada, sin adjudicar al portal cambios estacionales ni reducción de atención humana forzosa.

**Sección destino exacta:** SD4 4.1.3.1, después del Portal de Clientes; método y aceptación en Anexo 4-T.

**Borrador listo para pegar:**

> LafroX compromete el indicador de reducción de atención asistida por efecto de la autoatención. Para los motivos elegibles, la tasa asistida es el número de contactos asistidos dividido por el número de transacciones del mismo segmento y período; la reducción relativa es uno menos la razón entre esa tasa y la tasa de línea base. La estimación de oferta separa participación de motivos resolubles, adopción esperada y consultas evitables con su fundamento; su valor comprometido es [[META DE REDUCCIÓN FUNDAMENTADA]] para [[PERÍODO Y SEGMENTO]]. El informe mensual compara esa meta con el resultado, documenta estacionalidad y recontactos y conserva la atención asistida de quienes la necesiten. (Bases Técnicas Transversales, cap. 16, p. 31).

**Dato que debe definir el equipo:** Volumen histórico real por motivo, denominador, segmento, período base, horizonte de meta y adopción sustentada. Los dos marcadores requieren decisión y cálculo del equipo; mientras falten, el borrador no cierra RT-16.33 y no se aplica al entregable.

**Impactos coordinados:** SD3: criterios del portal y operación, sin reducir derechos del canal tradicional. SD5: datos/eventos de consulta resuelta y vínculo con contactos/recontactos, con minimización. T-11: no reducir puestos ni capacidad por una estimación sin prueba. T-14/T-15: medición, construcción de indicador e informes en 2.6/8.1; HH por estimar. SD8: adopción insuficiente y beneficio no alcanzado. Oferta Económica: no registrar ahorros antes de estimarlos con base real; separar beneficio y costo de medición.

**Complejidad:** Media. **Recomendación:** Aplicar tras definir datos y meta.

## Según caso

La aplicabilidad de la firma certificada debe resolverse por acto y no se infiere del uso de firma en pantalla en el POD.

### RT-16.18 — Sello de tiempo y evidencia de firma de larga duración

**Carácter:** Según caso. **Fuente:** Bases Técnicas Transversales, cap. 16, p. 30. **Estado vigente:** No cumple.

**Texto exacto del RT:** «Se generará el sello de tiempo y se conservará la evidencia de firma que permita verificar el documento con posterioridad al vencimiento del certificado.»

**Base ya existente:** SD3-Anexos 3.A declara RF-18.01; 3.H, V-18, mantiene pendiente el mecanismo de acuse tributario aceptado. SD4 4.1.17.1 y Anexo 4-U separan POD, DTE del ERP y acuses; SD5-Anexos 5-A contiene `doc_acuse_destinatario`. La firma dibujada o el QR de POD no acreditan sello de tiempo criptográfico.

**Qué falta:** Decisión sobre actos que requieren firma certificada y evidencia suficiente para verificarla después del vencimiento, con validación histórica, sello y conservación.

**Opción recomendada:** Confirmar aplicabilidad por acto; adaptar INT-07/ACL para preservar documentos firmados por el ERP y su evidencia. Para otros actos certificados, interfaz con un servicio de sellado y validación por seleccionar, conservando documento/hash, cadena, estado de revocación y sello. S3 con retención protege el expediente sin sustituir la validación criptográfica.

**Sección destino exacta:** SD4 4.1.17.1, «Secuencia y excepciones»; expediente de evidencia en Anexo 4-U.

**Borrador listo para pegar:**

> Para los actos del caso que requieran firma electrónica basada en certificado, la solución conserva el documento firmado, su integridad, la cadena de certificados, la evidencia de vigencia y revocación al firmar y un sello de tiempo verificable emitido por un servicio de confianza. El expediente permite comprobar posteriormente que la firma era válida en ese instante, incluso después del vencimiento del certificado, y dispone de conservación y renovación de evidencia antes de que se debilite su verificabilidad. La guía tributaria sigue siendo emitida por el ERP; INT-07 obtiene y conserva su expediente sin duplicar la emisión. La aceptación verifica un expediente con certificado vencido a la fecha de comprobación y válido al instante acreditado de firma. (Bases Técnicas Transversales, cap. 16, p. 30).

**Dato que debe definir el equipo:** Actos aplicables, mecanismo confirmado del ERP, formato del expediente, servicio de confianza, retención y costo; V-18 no equivale a exención de RT-16.18. No prometer implementación cerrada sin resolver esas dependencias.

**Impactos coordinados:** SD3: RF-18.01 y V-18, alcance de cada firma. SD5: expediente, hash, certificados, revocación, sello y renovaciones en 5-A/5-D. T-11: verificar software/licencias sin nuevos equipos por suposición. T-14/T-15: acuerdo e integración tributaria, pruebas y custodia; nuevas HH y ventanas por estimar. SD8: dependencia del ERP/servicio de confianza y pérdida de verificabilidad. Oferta Económica: sellos, validación, almacenamiento y servicio contratado cuando se elija.

**Complejidad:** Alta. **Recomendación:** Definir aplicabilidad y resolver; no declarar exención.

## Deseables

Las trece propuestas siguientes se priorizan después de los obligatorios; una recomendación de inclusión no acredita financiación ni cumplimiento actual.

### RT-05.24 — Portal para desarrolladores

**Carácter:** Deseable. **Fuente:** Bases Técnicas Transversales, cap. 5, p. 13. **Estado vigente:** No cumple.

**Texto exacto del RT:** «Se valorará la publicación de un portal de servicios para desarrolladores con documentación navegable, ambiente de pruebas y credenciales de prueba autoservidas.»

**Base ya existente:** SD4 4.1.3.5, «Contratos de integración» y «Versionado y gobierno de integración», declara OpenAPI 3.1/AsyncAPI 2.6; Anexo 4-B, Tabla A.3, menciona catálogo en portal API Gateway; Anexo 4-P detalla CI/CD. T-14 3.11.3 publica documentación y 3.1.1 dispone QA. Eso no demuestra autoservicio de credenciales.

**Qué falta:** Portal navegable conjunto, sandbox delimitado y emisión autoservida de credenciales de prueba.

**Opción recomendada:** Publicar documentación estática generada desde los contratos mediante S3/CloudFront y acceso Keycloak; API Laravel emite credenciales de prueba limitadas a adaptadores simulados en QA, con cuotas, caducidad y revocación.

**Sección destino exacta:** SD4 4.1.3.5, «Versionado y gobierno de integración»; responsabilidades en Anexo 4-B.

**Borrador listo para pegar:**

> El portal de desarrolladores reúne documentación navegable y versionada de OpenAPI y AsyncAPI, ejemplos y un ambiente de pruebas aislado con datos sintéticos. Una persona registrada mediante Keycloak solicita y obtiene credenciales de prueba desde el propio portal, con ámbito, cuota, caducidad y revocación; estas credenciales no habilitan producción ni sistemas reales de terceros. Las pruebas comprueban la navegación de la documentación, la emisión autoservida y la imposibilidad de utilizar las credenciales fuera del sandbox. (Bases Técnicas Transversales, cap. 5, p. 13).

**Dato que debe definir el equipo:** Elegibilidad de desarrolladores, cuotas/caducidad y cobertura del sandbox; no se presume autorización de una cadena o del ERP para ensayos reales.

**Impactos coordinados:** SD3: incorporar el deseable en alcance si se acepta. SD5: solo registro de solicitudes y auditoría; conservar secretos en el servicio ya previsto. T-11: validar capacidad S3/CloudFront/QA existente. T-14/T-15: ampliar 3.11.3 y 3.1.1 con emisión autoservida y pruebas; estimar HH. SD8: abuso de credenciales y exposición de sandbox. Oferta Económica: HH y consumo adicional.

**Complejidad:** Media. **Recomendación:** Incluir si hay tiempo. Aporta mérito de integración, pero la documentación ya existe y el esfuerzo adicional está en seguridad del autoservicio; no hay puntaje unitario acreditado que justifique desplazar obligatorios.

### RT-06.15 — Contención del aire en la sala de Talca

**Carácter:** Deseable. **Fuente:** Bases Técnicas Transversales, cap. 6, p. 15. **Estado vigente:** No cumple.

**Texto exacto del RT:** «El PROPONENTE declarará la estrategia de contención de pasillo frío o caliente y su efecto en la eficiencia energética.»

**Base ya existente:** SD4 4.3.1.4 describe dos racks con funciones distintas, climatización de precisión N+1, plano de recinto y PUE estimado ≈1,5. T-11 conserva ese equipamiento; T-14 2.3.1/5.1.2/6.1.1 gobierna planos, compra e instalación. No hay contención fría/caliente declarada.

**Qué falta:** Estrategia física explícita y su efecto energético; dos racks no demuestran una contención de pasillo.

**Opción recomendada:** Estudiar confinamiento del retorno caliente detrás de los racks, compatible con acceso, extinción y mantenimiento; verificarlo con el plano y fabricante de climatización antes de incorporar elementos. Conservar la separación de racks y N+1.

**Sección destino exacta:** SD4 4.3.1.4, después de climatización y antes de protección contra incendios.

**Borrador listo para pegar:**

> La sala adopta contención del pasillo caliente mediante cierre del retorno y separación de los flujos de suministro y extracción en los racks, con paneles ciegos y sellado de pasos de cable. El diseño mantiene accesibilidad, detección y extinción y funcionamiento N+1. Evitar la mezcla de aire reduce recirculación y trabajo de refrigeración; el efecto se verifica comparando consumo de climatización y PUE bajo cargas TI equivalentes, sin atribuir un ahorro porcentual no medido. El plano aprobado identifica cierres, retorno y acceso para mantenimiento. (Bases Técnicas Transversales, cap. 6, p. 15).

**Dato que debe definir el equipo:** Viabilidad en el recinto existente, dimensiones/elementos y aprobación del diseño térmico y contra incendios. El borrador no basta si el plano no realiza esa contención.

**Impactos coordinados:** SD3: alcance físico y supuesto de obra coordinada, sin traspasar costos a CLIENTE por defecto. SD5: sin cambio. T-11: especificar elementos únicamente si se aprueban. T-14/T-15: recalcular 2.3.1/5.1.2/6.1.1 y HH; preservar secuencia de sala. SD8: circulación, temperatura y recepción. Oferta Económica: materiales, instalación y verificación, sin reducir consumo estimado antes de comprobarlo.

**Complejidad:** Media. **Recomendación:** Incluir si hay tiempo. Mérito energético deseable sin puntaje unitario conocido; exige coherencia del plano y de compra, por lo que no conviene añadir una declaración física que el recinto no pueda cumplir.

### RT-08.15 — Unidad de cada tipo antes de compra masiva

**Carácter:** Deseable. **Fuente:** Bases Técnicas Transversales, cap. 8, p. 19. **Estado vigente:** No cumple.

**Texto exacto del RT:** «El PROPONENTE proveerá una unidad de cada tipo de dispositivo especificado para pruebas de aceptación por parte del CLIENTE, antes de la compra masiva.»

**Base ya existente:** SD4 4.2.1.1/4.2.1.2 y T-11 identifican tipos, incluido MC9400 estándar y versión de congelado. T-14 5.1.3 exige recepción conforme y 2.6/3.8/3.9 prevé pruebas; la recepción de compras masivas no cubre una muestra previa provista por LafroX.

**Qué falta:** Provisión por LafroX de una unidad por cada tipo especificado antes de comprar masivamente y decisión de aceptación del CLIENTE.

**Opción recomendada:** Plan de muestras por tipo de T-11 con accesorios, condiciones reales y acta; distinguir modelos/variantes y no limitarlo a teléfonos. Vincular compras a aceptación y tratar muestras como costo de LafroX sin inventar préstamo del fabricante.

**Sección destino exacta:** SD4 4.2.1.2, al final de criterios de selección, antes del ciclo de retiro.

**Borrador listo para pegar:**

> Antes de autorizar la compra masiva, LafroX provee al CLIENTE una unidad de cada tipo de dispositivo especificado en el Formulario T-11, con los accesorios necesarios para sus pruebas de aceptación. El plan identifica modelo y variante, caso de uso, condición de ensayo y resultado; incluye la variante de congelado cuando corresponda. El CLIENTE registra su aceptación o rechazo y las correcciones exigidas antes de liberar la compra del tipo afectado. Las muestras no se descuentan de la reserva operativa ni sustituyen la recepción conforme del parque completo. (Bases Técnicas Transversales, cap. 8, p. 19).

**Dato que debe definir el equipo:** Listado completo de tipos y variantes, calendario previo a las órdenes y destino patrimonial de muestras tras la prueba.

**Impactos coordinados:** SD3: agregar hito de validación por tipo sin alterar quién compra hardware de terreno. SD5: no cambia el modelo de negocio; requiere registro de activos/muestras en gestión de configuración. T-11: confirmar tipos, accesorios y contabilización. T-14/T-15: actividad previa a compras y antes de 5.1.3; recalcular precedencias y HH. SD8: riesgo de plazos de suministro y rechazo. Oferta Económica: muestras, transporte y pruebas a cargo de LafroX.

**Complejidad:** Media. **Recomendación:** Incluir. El mérito deseable se acompaña de reducción del riesgo de comprar equipos inadecuados; priorizarlo si el costo y el plazo de muestras están financiados, sin prometer gratuidad de proveedores.

### RT-08.19 — Extensión de vida útil cuantificada

**Carácter:** Deseable. **Fuente:** Bases Técnicas Transversales, cap. 8, p. 20. **Estado vigente:** No cumple.

**Texto exacto del RT:** «Se valorará una estrategia de reacondicionamiento o de extensión de vida útil que reduzca el impacto ambiental, cuantificada en la propuesta.»

**Base ya existente:** SD4 4.2.1.2 declara equipamiento nuevo, vida esperada de cinco años, garantía/reserva y ahora retiro certificado. T-14 8.2.3/8.2.7 cubre mantenimiento y disposición. No existe inventario elegible para reacondicionar ni cuantificación ambiental.

**Qué falta:** Estrategia y efecto cuantificado en la oferta; prometer mantenimiento o usar el 10 % de reserva como ahorro no lo cubre.

**Opción recomendada:** Reacondicionar solo activos ya utilizados y técnicamente aptos, después de sanitización, pruebas y comprobación de soporte; no sustituir equipos nuevos de recepción por usados. Calcular unidades/masa de residuo evitada y energía de reparación frente a sustitución con datos comprobables.

**Sección destino exacta:** SD4 4.2.1.2, después de sanitización y disposición final.

**Borrador listo para pegar:**

> La extensión de vida útil se aplica a equipos que, tras su uso, superen la comprobación de seguridad, soporte, batería y desempeño y puedan repararse sin reducir la disponibilidad comprometida. No reemplaza el suministro inicial de equipamiento nuevo ni conserva componentes fuera de soporte. El inventario distingue unidades reparadas y años adicionales de uso; la reducción de residuos se calcula como unidades cuya sustitución se evita multiplicadas por su masa documentada, descontando piezas sustituidas y residuos de reparación. La estimación de oferta es [[UNIDADES ELEGIBLES, MASA Y RESULTADO DEL CÁLCULO]] y se contrasta anualmente con los resultados. (Bases Técnicas Transversales, cap. 8, p. 20).

**Dato que debe definir el equipo:** Activos elegibles, masa de equipos/piezas, horizonte y consumo/materiales de reparación. El marcador impide acreditar cuantificación todavía; no sustituirlo por un porcentaje supuesto.

**Impactos coordinados:** SD3: delimitar extensión sin rebajar RT-08.06/13. SD5: sin cambio de datos de negocio; registro de activos y evidencias. T-11: revisar garantías y compatibilidad, sin cambiar suministro nuevo. T-14/T-15: ampliar 8.2.3/8.2.7 y valorar HH/logística. SD8: obsolescencia y disponibilidad. Oferta Económica: comparación reparación/sustitución y disposición; sin ahorro registrado antes del cálculo.

**Complejidad:** Media. **Recomendación:** Incluir si hay tiempo. Mérito ambiental deseable sin puntos por RT acreditados; su cuantificación exige datos y puede contradecir el equipamiento nuevo si se redacta sin delimitar el ciclo.

### RT-09.10 — Carga periódica automatizada en CI

**Carácter:** Deseable. **Fuente:** Bases Técnicas Transversales, cap. 9, p. 22. **Estado vigente:** No cumple.

**Texto exacto del RT:** «Se valorará la existencia de pruebas de carga automatizadas ejecutadas de forma periódica en el flujo de integración continua, con detección de regresiones de desempeño.»

**Base ya existente:** SD4 4.1.7/4.2.4.1 declara GitLab CI y CodeBuild; 4.2.6.12 y Anexo 4-T definen carga/aceptación. T-14 3.1.4, 3.8.4/3.9.3 programa pipeline y ensayos de carga; SD13 13.2.2 mantiene regresiones de incidentes. No hay ejecución periódica de carga ni comparación automática.

**Qué falta:** Cadencia, escenarios reproducibles, referencia aprobada y bloqueo/detección de regresiones de desempeño en CI.

**Opción recomendada:** Trabajo programado GitLab CI en QA/Preproducción con generador de carga compatible por seleccionar; usar idénticos escenarios, datos y capacidad, guardar percentiles/errores y comparar con referencia por escenario.

**Sección destino exacta:** SD4 4.2.6.12; umbrales por escenario en Anexo 4-T.

**Borrador listo para pegar:**

> GitLab CI ejecuta periódicamente la batería automatizada de carga en un ambiente de pruebas aislado y la repite ante cambios de componentes críticos. Los escenarios, datos, capacidad y referencia de comparación quedan versionados. El trabajo mide latencia en percentil 95, errores y rendimiento por transacción y detecta regresiones respecto de la referencia aprobada y de los máximos contractuales. Un incumplimiento bloquea la promoción y conserva el informe para su corrección. Ningún ensayo genera operaciones reales ni compite con el despacho en Producción. (Bases Técnicas Transversales, cap. 9, p. 22).

**Dato que debe definir el equipo:** Cadencia programada, tolerancia de regresión por escenario y herramienta de carga; no inventar umbrales ni confundir la referencia sintética con SLA medido en usuarios.

**Impactos coordinados:** SD3: pruebas y evidencia del deseable. SD5: conjuntos de datos anonimizados/sintéticos y retención de resultados. T-11: verificar capacidad de ambiente existente. T-14/T-15: ampliar 3.1.4/3.8.4/3.9.3 y operación del pipeline con HH. SD8: regresión y contaminación de ambientes. Oferta Económica: tiempo de cómputo y mantenimiento de batería.

**Complejidad:** Media. **Recomendación:** Incluir. Mérito de calidad con reutilización alta del pipeline y reducción de riesgo operativo; la ventaja no se cuantifica como puntaje individual desconocido.

### RT-11.28 — Madurez del desarrollo seguro con OWASP SAMM

**Carácter:** Deseable. **Fuente:** Bases Técnicas Transversales, cap. 11, p. 24. **Estado vigente:** No cumple.

**Texto exacto del RT:** «Se aplicará el marco OWASP SAMM o equivalente para medir y mejorar la madurez del proceso de desarrollo seguro, con evaluación inicial y reevaluación anual.»

**Base ya existente:** SD4 4.1.3.7 y anexos 4-Q/4-R definen amenazas y controles; 4.1.7/4.2.4.1 incorpora análisis y puertas de seguridad. T-14 2.2.1/8.2.2 cubre seguridad. La presencia de herramientas o pentesting no constituye evaluación de madurez.

**Qué falta:** Marco expreso, evaluación inicial, reevaluación anual y plan de mejora con evidencias.

**Opción recomendada:** Aplicar OWASP SAMM sobre prácticas y artefactos del proceso existente; registrar evaluación por práctica, brecha, responsable y acción. Usar resultado para mejora anual sin afirmar certificación (OWASP Foundation, s. f.).

**Sección destino exacta:** SD4 4.1.3.7, «Amenazas, controles y evidencia»; seguimiento en Anexo 4-R.

**Borrador listo para pegar:**

> LafroX aplica OWASP SAMM para medir y mejorar la madurez del desarrollo seguro. La evaluación inicial registra por práctica el nivel sustentado en evidencia, las brechas y el plan de mejora con responsable y plazo. Se repite anualmente con el mismo alcance y criterio, informa al CLIENTE los cambios y verifica el cierre de acciones mediante artefactos del proceso. El resultado describe madurez observada y no se presenta como certificación de la solución (OWASP Foundation, s. f.). (Bases Técnicas Transversales, cap. 11, p. 24).

**Dato que debe definir el equipo:** Alcance de evaluación, evaluadores, calendario anual y metas por práctica; no inventar nivel de madurez inicial.

**Impactos coordinados:** SD3: incorporar deseable y criterios de evaluación. SD5: sin modelo de negocio nuevo; custodia de evidencias bajo política documental. T-11: sin hardware adicional. T-14/T-15: ampliar 2.2.1/8.2.2 con evaluación y tres ciclos anuales de Operación, valorando HH y continuidad de SEG. SD8: madurez insuficiente y acciones pendientes. Oferta Económica: HH o asesoría si se decide contratarla.

**Complejidad:** Baja. **Recomendación:** Incluir. Añade mérito y una mejora verificable aprovechando controles existentes; el costo está en evaluación y seguimiento y no en otra plataforma.

### RT-13.12 — Modo oscuro y preferencias de interfaz

**Carácter:** Deseable. **Fuente:** Bases Técnicas Transversales, cap. 13, p. 27. **Estado vigente:** No cumple.

**Texto exacto del RT:** «Se valorará el soporte de modo oscuro, de personalización de la interfaz por persona usuaria y de múltiples idiomas cuando el caso lo justifique.»

**Base ya existente:** SD4 4.1.3.1/4.1.7 usa Angular/Tailwind y Kotlin por perfil; 4.1.3.7 gestiona identidad. No hay preferencias visuales ni justificación de idiomas; la interfaz y la oferta se redactan en español.

**Qué falta:** Compromiso de modo oscuro, personalización por persona y decisión fundada sobre idiomas.

**Opción recomendada:** Tokens de tema para Angular/Tailwind y equivalentes Kotlin; guardar tema/densidad/tamaño de texto por identidad, con cache local sin alterar permisos. Mantener español y documentar la necesidad de otros idiomas antes de ofertarlos.

**Sección destino exacta:** SD4 4.1.3.1, después del sistema de diseño propuesto para RT-13.09.

**Borrador listo para pegar:**

> Cada persona puede seleccionar tema claro u oscuro y ajustar tamaño de texto y densidad dentro de los límites de legibilidad y accesibilidad. Las preferencias se conservan por identidad y se reproducen en los portales, la consola y el perfil Kotlin compatible; no modifican permisos ni reglas de negocio. Los temas mantienen WCAG 2.2 AA y se comprueban en aceptación. La interfaz se ofrece en español; la investigación por perfiles determina si el caso justifica otros idiomas y documenta esa decisión antes de ampliar el alcance. (Bases Técnicas Transversales, cap. 13, p. 27).

**Dato que debe definir el equipo:** Preferencias habilitadas y necesidad real de otros idiomas por grupo; una mención condicionada no acredita múltiples idiomas si el caso sí los justifica.

**Impactos coordinados:** SD3: preferencias y alcance de idiomas. SD5: registro de preferencias por persona y política de cache/retención. T-11: probar legibilidad en pantallas Zebra sin cambiar equipos. T-14/T-15: sistema de diseño, Kotlin y pruebas 2.6/3.8/3.9; HH. SD8: accesibilidad y divergencia de temas. Oferta Económica: HH de temas y traducción solo si se incluye.

**Complejidad:** Media. **Recomendación:** Incluir si hay tiempo. Mérito deseable moderado y reutilización del sistema de diseño; dos temas multiplican estados de prueba y los idiomas añaden esfuerzo sin necesidad aún demostrada.

### RT-14.09 — Alertas de anomalías históricas

**Carácter:** Deseable. **Fuente:** Bases Técnicas Transversales, cap. 14, p. 27. **Estado vigente:** No cumple.

**Texto exacto del RT:** «Se valorará la detección proactiva de anomalías mediante análisis del comportamiento histórico, con alerta antes de que el incidente afecte a la operación.»

**Base ya existente:** SD4 4.1.3.8 y Anexo 4-B, Tabla A.3, usa CloudWatch con métricas/alertas; 4.2.6.10/11 gobierna capacidad. T-14 3.1.5 y 8.1.1 cubre observabilidad. Las alertas de umbral actual no prueban comparación histórica.

**Qué falta:** Modelos de comportamiento histórico, señales precursoras y verificación de alerta antes del impacto operativo.

**Opción recomendada:** Usar bandas históricas CloudWatch Anomaly Detection para métricas seleccionadas, con ajuste por patrón horario/semanal, exclusión de mantenimientos y alerta al NOC antes del umbral de afectación; no prometer predicción perfecta (Amazon Web Services, s. f.).

**Sección destino exacta:** SD4 4.1.3.8, tras las alertas por síntomas de negocio.

**Borrador listo para pegar:**

> La observabilidad incorpora bandas de comportamiento histórico en CloudWatch para latencia, acumulación de colas y uso de capacidad. Se ajustan a los patrones horarios y semanales y excluyen períodos de mantenimiento del aprendizaje. El desvío sostenido activa un aviso preventivo al NOC antes de alcanzar el umbral de afectación definido para la señal, conservando también las alarmas estáticas. La aceptación reproduce una degradación progresiva y comprueba la precedencia del aviso respecto del impacto; durante un corte WAN continúan las alarmas locales de la arquitectura (Amazon Web Services, s. f.). (Bases Técnicas Transversales, cap. 14, p. 27).

**Dato que debe definir el equipo:** Métricas elegibles, ventanas, sensibilidad, umbrales y fuente de historia; no afirmar que detecta todo incidente antes de ocurrir.

**Impactos coordinados:** SD3: incluir el deseable y su prueba. SD5: conservar métricas según retención de observabilidad, sin duplicar datos personales. T-11: reutilizar CloudWatch; verificar límites. T-14/T-15: ampliar 3.1.5/8.1.1 y HH de calibración. SD8: falsos positivos, fatiga y pérdida de señal. Oferta Económica: cargos de alarmas/modelos y HH, sin tarifa supuesta.

**Complejidad:** Media. **Recomendación:** Incluir. Mérito de prevención con una capacidad de la plataforma elegida y beneficio operativo claro; financiar las alarmas y su calibración para evitar que la promesa genere ruido.

### RT-15.05 — Comparación de carbono por región

**Carácter:** Deseable. **Fuente:** Bases Técnicas Transversales, cap. 15, p. 28. **Estado vigente:** No cumple.

**Texto exacto del RT:** «Se valorará la elección de regiones de nube con menor intensidad de carbono cuando la latencia y la regulación lo permitan, con el análisis comparativo correspondiente.»

**Base ya existente:** SD4 4.2.3.2 y 4.3.1.2/4.3.2.2 fija sa-east-1 y us-east-1 y restringe geolocalización en la secundaria; Anexo 4-O registra residencia/recuperación. T-14 8.4.3 programa informes de huella. RT-15.04 sigue parcial por intensidad de carbono de la región no aportada.

**Qué falta:** Datos homogéneos de intensidad de carbono y comparación con latencia, disponibilidad de servicios y regulación; un informe anual futuro no constituye el análisis de oferta.

**Opción recomendada:** Comparar las dos regiones elegidas y una candidata sustentada, usando mismo período y metodología. Mantener la topología mientras no exista evidencia que justifique una región de menor carbono sin rebajar latencia, residencia o DR.

**Sección destino exacta:** SD4 4.2.3.2, análisis de residencia y región secundaria; decisión en Anexo 4-O.

**Borrador listo para pegar:**

> La comparación regional evalúa intensidad de carbono documentada, latencia medida desde los sitios, disponibilidad de los servicios utilizados y condiciones de tratamiento y transferencia de datos. Se aplica la misma metodología y período a cada alternativa. Una región de menor intensidad solo se selecciona cuando satisface simultáneamente regulación, desempeño y continuidad; la decisión conserva los datos y restricciones que la sustentan. La topología declarada no se cambia sin demostrar esa equivalencia y actualizar el plan de recuperación. (Bases Técnicas Transversales, cap. 15, p. 28).

**Dato que debe definir el equipo:** Intensidades y fuentes comparables, candidata concreta, mediciones de latencia y análisis regulatorio. El borrador es método, no análisis comparativo completo; no acredita Cumple sin la comparación.

**Impactos coordinados:** SD3: revisar restricciones de residencia solo tras decisión. SD5: replica/retención y transferencias internacionales, preservando exclusión de GPS. T-11: servicios/regiones afectados si se cambia. T-14/T-15: análisis y eventual migración/DR con HH y calendario. SD8: región, regulación, continuidad y dependencia. Oferta Económica: comparación completa de cómputo, egreso, operación y traslado; sin ahorro supuesto.

**Complejidad:** Alta. **Recomendación:** No vale la pena. Para esta iteración el mérito deseable no tiene puntaje unitario acreditado y faltan datos; cambiar regiones puede contradecir continuidad y residencia. Sí conviene reunir la intensidad exigida por el obligatorio RT-15.04.

### RT-15.06 — Metas anuales de reducción de consumo

**Carácter:** Deseable. **Fuente:** Bases Técnicas Transversales, cap. 15, p. 28. **Estado vigente:** No cumple.

**Texto exacto del RT:** «Se valorará la definición de metas de reducción del consumo durante la Operación, con medición y reporte anual.»

**Base ya existente:** SD4 4.3.1.4 mide PUE semestralmente y estima carga; 4.2.6.10 dimensiona capacidad. T-14 8.4.2 trata consumo FinOps y 8.4.3 huella. Ninguno compromete una meta energética de reducción; costo AWS, huella y kWh no son el mismo indicador.

**Qué falta:** Línea base, meta de reducción, medición y reporte anual, preservando N+1 y disponibilidad.

**Opción recomendada:** Medir kWh del recinto y de carga TI, comparar consumo absoluto e intensidad por transacción bajo cargas comparables y definir un plan de reducción por optimización. Para nube usar métricas energéticas del proveedor cuando existan, sin convertir costo directamente a kWh.

**Sección destino exacta:** SD4 4.3.1.4, después del párrafo PUE; enlace al plan de capacidad 4.2.6.10.

**Borrador listo para pegar:**

> La Operación establece una línea base de consumo energético y compromete una reducción de [[META Y MÉTRICA ENERGÉTICA]] en [[HORIZONTE]]. La medición conserva kWh del recinto, kWh de carga TI y volumen operacional, y el informe anual presenta consumo absoluto, intensidad por transacción, PUE y avance contra la meta, explicando crecimiento y estacionalidad. Las acciones de optimización se prueban sin reducir la redundancia ni la disponibilidad. El consumo de nube se informa con datos energéticos disponibles del proveedor y metodología explícita, separadamente del costo financiero. (Bases Técnicas Transversales, cap. 15, p. 28).

**Dato que debe definir el equipo:** Meta sustentada, período base, unidad/denominador y datos energéticos disponibles. No copiar el PUE estimado como reducción ni inventar porcentaje; con marcadores el RT queda sin acreditar.

**Impactos coordinados:** SD3: alcance de meta anual sin debilitar capacidad. SD5: retención de series energéticas en observabilidad, sin nueva entidad de negocio obligatoria. T-11: comprobar medición existente y dispositivos si faltan. T-14/T-15: ampliar 8.4.2/8.4.3 y valorar HH. SD8: ahorro no alcanzado o optimización insegura. Oferta Económica: costo de medición y acciones; beneficio solo con base calculada.

**Complejidad:** Media. **Recomendación:** Incluir si hay tiempo. Hay medición de PUE que reduce esfuerzo, pero falta una meta fundamentada; el mérito deseable no compensa introducir porcentajes sin datos o recortar redundancia.

### RT-16.05 — Simulación antes de publicar parámetros

**Carácter:** Deseable. **Fuente:** Bases Técnicas Transversales, cap. 16, p. 29. **Estado vigente:** No cumple.

**Texto exacto del RT:** «Existirá un ambiente de simulación que permita probar el efecto de un cambio de parámetro antes de aplicarlo a producción.»

**Base ya existente:** SD4 4.1.9/4.2.4.1 dispone de cinco ambientes y datos sintéticos en QA; SD5-Anexos 5-A tiene parámetros versionados. Esos ambientes no incluyen una simulación del efecto de un cambio de parámetro.

**Qué falta:** Acción de simulación accesible y aislada, resultado comparativo y control antes de publicar.

**Opción recomendada:** Desde la administración Angular, ejecutar en QA un trabajo Laravel con escenarios versionados, valor vigente y propuesto; devolver diferencias sin efectos externos. Compartir el evaluador de reglas productivo y marcar límites de predicción.

**Sección destino exacta:** SD4 4.1.9, descripción de QA; relación con administración en 4.1.3.4.

**Borrador listo para pegar:**

> La administración permite simular un cambio de parámetro antes de publicarlo en Producción. Un trabajo en QA evalúa el valor vigente y el propuesto sobre el mismo conjunto de escenarios sintéticos o anonimizados, usando la versión del evaluador de reglas que se pretende liberar. El resultado muestra diferencias, advertencias y escenarios afectados, sin escribir en Producción ni emitir avisos, pagos o documentos reales. La publicación requiere guardar la simulación y su decisión de aprobación; el resultado no se presenta como garantía de comportamiento fuera de los escenarios ensayados. (Bases Técnicas Transversales, cap. 16, p. 29).

**Dato que debe definir el equipo:** Catálogo inicial de parámetros simulables, escenarios, permisos y criterios de aprobación. Dependencia: primero resolver la administración de RT-16.04.

**Impactos coordinados:** SD3: criterio de simulación y relación con RF-17.02. SD5: escenarios/resultados y referencias a versión del parámetro, minimización/retención. T-11: reutilizar QA, confirmar capacidad. T-14/T-15: ampliar administración y 3.1.1 con trabajos/pruebas y HH. SD8: datos sensibles en QA y falsa confianza. Oferta Económica: ejecución y mantenimiento de escenarios.

**Complejidad:** Media. **Recomendación:** Incluir. El mérito deseable se suma a prevención de cambios erróneos y reutiliza QA; incluir junto con el obligatorio RT-16.04 para no duplicar administración.

### RT-16.26 — Acciones desde canales conversacionales

**Carácter:** Deseable. **Fuente:** Bases Técnicas Transversales, cap. 16, p. 30. **Estado vigente:** No cumple.

**Texto exacto del RT:** «Se valorará la integración con canales conversacionales que permitan a la persona usuaria responder y ejecutar acciones desde el propio canal.»

**Base ya existente:** SD4 4.1.6.2 y Anexo 4-H, INT-11, envía correo/SMS/WhatsApp y portal; 4.1.3.1 permite autoatención autenticada. La recepción técnica de un aviso no significa respuesta o ejecución de acciones desde el canal.

**Qué falta:** Canal bidireccional, identidad, autorización, acciones admitidas y registro/idempotencia.

**Opción recomendada:** Adaptador de entrada para el canal de mensajería ya contemplado, validando autenticidad del webhook, identidad y permisos en Laravel/Keycloak. Comenzar con consultas de estado; una acción de negocio exige confirmación y control contra repetición.

**Sección destino exacta:** SD4 4.1.6.2; contrato bidireccional de INT-11 en Anexo 4-H.

**Borrador listo para pegar:**

> El canal conversacional permite consultar el estado de un pedido y ejecutar las acciones de confirmación habilitadas para el perfil dentro del propio canal. El adaptador verifica autenticidad del mensaje, vincula la identidad mediante un desafío seguro y aplica los permisos del servicio; el número de teléfono por sí solo no autoriza acciones. Cada solicitud conserva correlación e identificador de idempotencia, solicita confirmación cuando modifica datos y registra el resultado. Si falla la validación, no ejecuta la acción y remite a la atención asistida. La baja comercial de INT-11 sigue aplicándose a los envíos promocionales. (Bases Técnicas Transversales, cap. 16, p. 30).

**Dato que debe definir el equipo:** Proveedor/API bidireccional, acciones exactas, mecanismo de vinculación y condiciones/tarifas del canal; INT-11 no acredita un contrato vigente.

**Impactos coordinados:** SD3: catálogo de acciones y criterios, sin ampliar actores. SD5: vínculo de identidad/canal y auditoría de entrada/acción. T-11: servicio/adaptador y sus credenciales; sin hardware por defecto. T-14/T-15: ampliar 3.6.4 con recepción/autorización y pruebas; estimar HH. SD8: suplantación, reintentos y dependencia de mensajería. Oferta Económica: tarifas/API y soporte más HH.

**Complejidad:** Alta. **Recomendación:** No vale la pena. En esta iteración añade superficie de seguridad y contrato de canal sin puntos individuales acreditados; portal y avisos cubren el servicio. Priorizar obligatorios antes de ampliar acciones comerciales.

### RT-17.08 — Interfaz ligera para dispositivos modestos

**Carácter:** Deseable. **Fuente:** Bases Técnicas Transversales, cap. 17, p. 32. **Estado vigente:** No cumple.

**Texto exacto del RT:** «Se valorará la disponibilidad de una versión de la interfaz para dispositivos de bajo costo o de generaciones anteriores, ampliando la cobertura de personas usuarias.»

**Base ya existente:** SD4 4.1.3.1 publica PWA opcional y conserva atención presencial; SD5 5.4.4 usa IndexedDB para catálogo/pedidos. Anexo 4-P, Tabla A.19, ahora declara navegadores soportados. No se acredita un perfil ligero ni cobertura de equipos antiguos.

**Qué falta:** Versión ligera y parque mínimo verificado, compatible con soporte y seguridad; antiguo no debe significar navegador vulnerable.

**Opción recomendada:** Perfil ligero en la misma aplicación Angular: carga diferida, páginas cortas, imágenes bajo demanda y contenido esencial, APIs iguales. Validar equipos económicos/anteriores con navegador y OS soportados; no prometer soporte de motores fuera de Baseline.

**Sección destino exacta:** SD4 4.1.3.1, junto al Portal de Clientes; matriz de dispositivos/prueba en Anexo 4-P.

**Borrador listo para pegar:**

> El Portal de Clientes dispone de un perfil ligero con carga diferida, páginas cortas, imágenes bajo demanda y acceso a pedido, entregas y saldo mediante las mismas APIs y permisos. Se valida en dispositivos de bajo costo o de generaciones anteriores que mantengan sistema y navegador soportados en la matriz de compatibilidad. La prueba registra equipo, memoria disponible, navegador, conectividad y resultado de los flujos principales; no se habilitan motores fuera del Baseline de Angular ni sistemas sin soporte de seguridad. El canal asistido continúa disponible para quienes no dispongan de un equipo compatible. (Bases Técnicas Transversales, cap. 17, p. 32).

**Dato que debe definir el equipo:** Equipos mínimos de prueba y límites de memoria/transferencia/tiempo respaldados por ensayos; no prometer todos los teléfonos antiguos.

**Impactos coordinados:** SD3: delimitar cobertura opcional sin exigir dispositivo al tradicional. SD5: paginación/cache y conservación de pedidos sin confirmar. T-11: teléfonos del cliente no son sustitución del parque Zebra; precisar muestras de ensayo. T-14/T-15: ampliar 3.5.2/2.6/3.9.2 y valorar HH. SD8: incompatibilidad y pérdida de captura. Oferta Económica: optimización y laboratorio de pruebas.

**Complejidad:** Media. **Recomendación:** Incluir si hay tiempo. Mérito de cobertura alineado con el caso, pero demanda pruebas reales; respetar Baseline evita contradecir el soporte de Angular para obtener un deseable.

## Referencias de apoyo para integrar los borradores

Las Bases sostienen todos los textos contractuales. Las dos fuentes externas siguientes se citan en las propuestas de RT-11.28 y RT-14.09 y deben incorporarse a las Referencias del SD4 si se acepta su texto. Los restantes borradores se apoyan en la arquitectura local y las Bases, sin afirmar selección de proveedores nuevos.

- Distribuidora Puelche S.A. (2026b). *Bases Técnicas Transversales de Licitación N.º TFEP-01/2026*. [Fuente contractual](../../Bases/Bases_Tecnicas_Transversales.md).
- Amazon Web Services. (s. f.). *Using CloudWatch anomaly detection*. <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html>
- OWASP Foundation. (s. f.). *The model: OWASP SAMM*. <https://owaspsamm.org/model/>

## Tabla resumen

La Tabla 1 resume la complejidad y la prioridad; los requisitos permanecen en No cumple porque estas propuestas no se aplicaron. Los marcadores pendientes de RT-16.33, RT-08.19 y RT-15.06 requieren datos y cálculo antes de integrarse.

**Tabla 1 — Propuestas de RT pendientes y decisión recomendada**

| RT | Carácter | Destino SD4 | Complejidad | Recomendación |
| --- | --- | --- | --- | --- |
| RT-13.05 | Obligatorio | SD4 4.1.3.1, después de «Actores del sistema, interfaces y autorización». | Media | Aplicar por obligación |
| RT-13.09 | Obligatorio | SD4 4.1.3.1; detalle del sistema en Anexo 4-P, dentro del inventario de presentación. | Media | Aplicar por obligación |
| RT-16.04 | Obligatorio | SD4 4.1.3.4, como párrafo de gobierno de reglas; inventario detallado en Anexo 4-P. | Media | Aplicar por obligación |
| RT-16.08 | Obligatorio | SD4 4.1.3.7, al final de «Clasificación, cifrado y custodia». | Media | Aplicar por obligación |
| RT-16.12 | Obligatorio | SD4 4.1.3.5, «Orquestación y coreografía»; ampliar la bandeja del Anexo 4-B. | Alta | Aplicar por obligación |
| RT-16.19 | Obligatorio | SD4 4.1.3.4, servicio transversal de documentos; correspondencia documental en Anexo 4-U. | Media | Aplicar por obligación |
| RT-16.33 | Obligatorio | SD4 4.1.3.1, después del Portal de Clientes; método y aceptación en Anexo 4-T. | Media | Aplicar tras definir datos y meta |
| RT-16.18 | Según caso | SD4 4.1.17.1, «Secuencia y excepciones»; expediente de evidencia en Anexo 4-U. | Alta | Definir aplicabilidad y resolver; no declarar exención |
| RT-05.24 | Deseable | SD4 4.1.3.5, «Versionado y gobierno de integración»; responsabilidades en Anexo 4-B. | Media | Incluir si hay tiempo |
| RT-06.15 | Deseable | SD4 4.3.1.4, después de climatización y antes de protección contra incendios. | Media | Incluir si hay tiempo |
| RT-08.15 | Deseable | SD4 4.2.1.2, al final de criterios de selección, antes del ciclo de retiro. | Media | Incluir |
| RT-08.19 | Deseable | SD4 4.2.1.2, después de sanitización y disposición final. | Media | Incluir si hay tiempo |
| RT-09.10 | Deseable | SD4 4.2.6.12; umbrales por escenario en Anexo 4-T. | Media | Incluir |
| RT-11.28 | Deseable | SD4 4.1.3.7, «Amenazas, controles y evidencia»; seguimiento en Anexo 4-R. | Baja | Incluir |
| RT-13.12 | Deseable | SD4 4.1.3.1, después del sistema de diseño propuesto para RT-13.09. | Media | Incluir si hay tiempo |
| RT-14.09 | Deseable | SD4 4.1.3.8, tras las alertas por síntomas de negocio. | Media | Incluir |
| RT-15.05 | Deseable | SD4 4.2.3.2, análisis de residencia y región secundaria; decisión en Anexo 4-O. | Alta | No vale la pena |
| RT-15.06 | Deseable | SD4 4.3.1.4, después del párrafo PUE; enlace al plan de capacidad 4.2.6.10. | Media | Incluir si hay tiempo |
| RT-16.05 | Deseable | SD4 4.1.9, descripción de QA; relación con administración en 4.1.3.4. | Media | Incluir |
| RT-16.26 | Deseable | SD4 4.1.6.2; contrato bidireccional de INT-11 en Anexo 4-H. | Alta | No vale la pena |
| RT-17.08 | Deseable | SD4 4.1.3.1, junto al Portal de Clientes; matriz de dispositivos/prueba en Anexo 4-P. | Media | Incluir si hay tiempo |

Fuente: Bases Técnicas Transversales y contraste documental de LafroX con los entregables vigentes.

Primero deben resolverse los siete obligatorios y la aplicabilidad de firma; entre los deseables se priorizan muestras previas a compra, carga en CI, SAMM, anomalías y simulación por su relación directa con calidad y continuidad. Carbono regional y acciones conversacionales no se recomiendan en esta iteración por sus dependencias y riesgo de contradicción.

