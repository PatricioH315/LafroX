# LafroX — frentes por cadenas de cambios, no por subdocumentos

**Este reparto sustituye operativamente el reparto A–E por SD.** Cada frente recibe una cadena completa de cambios y aplica sus efectos en todos los documentos afectados. No hay entregas K1–K6 que otro frente deba esperar para comenzar o terminar su corrección asignada.

Alcance: tareas restantes de olas 1–4 del plan `me-aburr-de-revisar-rosy-treehouse.md`. **Fuera: 1.1, ola 0 y ola 5.** No crear SD10/11/12/14 ni T-8 del punto 1.1. Fuente original intacta. Este documento organiza; no ejecuta correcciones.

## 1. Qué significa aquí «independientes»

- Cada frente puede ejecutar su cadena de principio a fin sin esperar el resultado de otra IA. Puede tener un orden **interno**, a cargo de su mismo responsable.
- Todos consultan la misma fotografía de los documentos ya disponibles tras las correcciones de ola 0. Leer un dato existente no es depender de que otra IA lo produzca.
- No se afirma que toda la ola 0 esté terminada: el usuario indica que lo está **en su mayoría**. Si falta una decisión que afecta una cadena, ese pendiente se incorpora al frente que la consume; no se asigna a otra IA como requisito previo. Si exige decisión humana, se informa el bloqueo: independencia entre IAs no elimina la necesidad de aprobación del equipo.
- Las dependencias identificadas son del diagnóstico y su cambio propuesto, no una auditoría nueva de todas las ramas. Revalidar cada hallazgo sobre los archivos efectivamente recibidos.
- **Independencia de ejecución no significa edición segura de la misma carpeta.** Algunos frentes cambian zonas distintas de un mismo SD. Trabajan en copias/ramas aisladas, entregando cambios acotados; no cinco versiones enteras para sobrescribir unas con otras. Este plan no desarrolla la consolidación/ola 5.
- Si se exige además que cada frente entregue directamente un SD completo definitivo, sin combinar cambios de otros, habrá que unir los frentes que compartan archivos. No prometer ambas cosas a la vez.

## 2. Dependencias reales encontradas

La flecha significa «si cambia el primero, el segundo debe actualizarse con ese resultado». Cada fila queda íntegramente bajo un mismo frente.

| Cadena del plan original | Por qué debe ir junta | Frente |
|---|---|---|
| 4.1/4.2 → 4.3 → 2.1 → T-15/SD7 | Nuevos riesgos y análisis modifican respuestas, reserva y su programación | F1 |
| 2.4 y 4.11 (dotación/reserva) → capacidad T-15 → capacidad/pruebas SD9 | La decisión sobre evaluadores y dotación altera horas disponibles y ejecución de calidad | F1 |
| 4.5 → riesgo SD8 → reserva/paquete/fecha SD7 → calendario SD9 | Una prueba DR adelantada o reconfigurada debe tener capacidad, respuesta y cronograma consistentes | F1 |
| 1.3/C4 → entregables T-14 → T-15/T-18/T-17 → citas SD9/SD13 | El cierre de marcha blanca y aceptación deben describir los mismos eventos | F1 |
| 1.6/C2 → catálogo SD8 → citas SD13/T-15 | Un ID que se define en SD8 no puede corregirse por separado en sus consumidores | F1 |
| 4.8 y 4.10 → catálogo T-12 → conteos/casos/matriz T-13 y SD9 | Modificar requisitos/estados afecta pruebas previstas y conteos derivados | F2 |
| 2.15 → regla SD3/SD2 → modelo SD5 | La granularidad de retención debe ser la misma en necesidad, regla y datos | F2 |
| 4.7 → SD3 → indicador I-04A/SD13 | OTIF debe tener la misma desigualdad y definición en origen y consumidor | F2 |
| 3.13 → numeración SD4 → 2.11/2.12 en los citantes | Si se corrige jerarquía, las remisiones numéricas deben corregirse en la misma cadena | F3 |
| 3.15 → anexos SD2/SD3 → sus remisiones | No pueden elegirse dos estilos ni renumerarse sin actualizar citantes | F3 |
| 1.5/3.9 → cita identificada → llamada y entrada bibliográfica | Reconstruir bibliografía incluye reparar sus llamadas, no sólo la lista final | F4 |
| 4.6 → plan de renovación SD1 → pasajes propios que afirman vigencia | Renovación y afirmaciones de acreditación deben corregirse conjuntamente | F5 |

**No son dependencias nuevas entre frentes:** usar RTO/RPO de C8, coberturas C7, congelamientos C9, dotación C5 o nombres C10 ya fijados; consultar los IDs/fechas existentes para una figura; corregir una frase de entrada de una lista. No hace falta pedir a otra IA que vuelva a definir esos datos.

## 3. Reparto de ejecución

### F1 — Riesgos, capacidad, cronograma y calidad operativa

**Este es el frente más grande.** No se divide entre «riesgos», «cronograma» y «calidad»: eso volvería a crear las esperas del reparto anterior. Su responsable puede recorrer varios SD, pero cierra toda la cadena por sí mismo.

**Documentos afectados:** SD1 (sólo dotación si cambia), SD6/T-9/T-10, SD7/T-14/T-15/T-18, SD8/T-16, SD9/T-13/T-17/anexos y SD13 (sólo riesgos/fechas y sus efectos).

**Tareas en orden interno:**

1. **Revalidar lo operativo de ola 0:** C2, C4–C9 y C11 en los pasajes relevantes. Resolver sólo remanentes dentro de esta cadena. No reabrir decisiones ya fijadas.
2. **Cerrar decisiones de capacidad y gobierno:** evaluadores de 2.4; 40/48 desarrolladores, contingencia DTE y reserva de 1.600 HH de 4.11; comité/veto de 4.4. Verificar respaldo y elevar decisiones humanas pendientes. Aplicar el resultado en SD1/SD6/SD9/T-15 afectados, sin enviarlo a otra IA para que lo propague.
3. **Cerrar calidad y continuidad operativas:** T-10 y SD9 con umbrales de 2.5 y tres coberturas de 2.6; SOC 2.2; sala técnica 2.3; congelamiento 2.9; RPO 2.7. Los valores fijados por canon se usan directamente. Reversión 2.10: distinguir mecanismo automático y responsabilidad del SRE sin cambiar el diseño de SD4.
4. **Diseñar y programar DR (4.5):** comprobar demostración antes de H5/H10 según C8, periodicidad, ambiente, alcance, evidencia prevista y salida. Actualizar tanto riesgo SD8 como paquetes/horas/calendario SD7/SD9. No marcar pruebas como ejecutadas.
5. **Completar riesgos (4.1–4.3):** obsolescencia, bloqueo por proveedor y escalabilidad; recuperar y adaptar FMEA; respuestas con costo-beneficio, plazo, rol, EDT e hito. Verificar escalas/unidades y no extenderse al modelo económico excluido del original.
6. **Evaluar P7-01…P7-11 y conciliar reservas (2.1):** matriz supuesto → riesgo/respuesta → reserva → paquete/hito. Distinguir HH, dinero y días; evitar doble conteo. Actualizar SD8 y T-15, no dejar remisiones circulares.
7. **Propagar IDs de riesgo (1.6/2.14):** comprobar catálogo y equivalencias recibidos; cerrar los cambios en SD13 y T-15. Mantener riesgos de adopción y oportunidad sin renumeración arbitraria.
8. **Cerrar hitos, actas y aceptación (1.3):** dos actas C4, entregables, revisión/subsanación, evidencia y fechas en todos los afectados. SD13 «transferencia desde el mes 22» (parte temporal de 2.12) se verifica aquí. No cambiar IDs H/EDT por conveniencia de redacción.
9. **Recalcular capacidades y holguras:** personas, jornada, días, meses, HH y reserva; actualizar tablas/figuras operativas derivadas. Revisar T-15 columna peak (parte de 3.12) y retirar huérfanos de 1.3 sólo si se demuestra que no se usan.
10. **Cerrar textos y objetos dependientes de esas decisiones:** indicios de 1.2 cuando revelen riesgos/reservas no resueltos; fuentes y tablas de estos bloques; RBS de SD8 si cambia por nuevos riesgos; figuras metodológicas SD6 y EDT SD7 (3.11), con referencias previas y explicación. F1 es dueño de estos objetos enteros: F4 no los rediseña simultáneamente.

**IDs principales:** 1.2, 1.3, 1.6; 2.1–2.10 excepto cambios estructurales; 2.14; 4.1–4.5, 4.11. También partes operativas de 1.7, 3.8, 3.11, 3.12 y 3.16.

**Cierre autónomo:** riesgos/reservas/capacidad/fechas/pruebas operativas consistentes en todos sus consumidores. No recalcular catálogo de requisitos ni conteos de casos funcionales: son F2. Usar la base de esos datos sin modificarlos.

### F2 — Requisitos, datos, casos de prueba e indicadores

**Documentos afectados:** SD2 (retención), SD3/T-12/anexos, SD5, SD9/T-13/matriz/generadores/anexos y SD13 (OTIF/I-04A).

**Tareas en orden interno:**

1. **Resolver granularidad de retención (2.15):** contrastar SD2 S-04, SD3 RNG-04 y modelo SD5 con las fuentes. Corregir regla y todos sus consumidores; distinguir lote/SSCC según escenario, sin sustitución global ciega.
2. **Resolver brechas concretas (4.8):** RF-14.01 y flota propia/terceros; RNF-04.01 medible; S-22 cinco/seis sitios; colisiones RF-14.01…05 entre documentos fuente. Mantener procedencia e identidad; no inventar cifras ni cambiar IDs ajenos sin mapeo.
3. **Revalidar estados y entidades (4.10):** recuento de entidades 139/121 con criterio explícito; estados actuales de T-12, notas de revisión y alcance realmente ofertado. La revisión humana ausente requiere evidencia del equipo, no declaración automática de cumplimiento.
4. **Cerrar OTIF (4.7):** desigualdad, fórmula, ventana y alcance en SD3; aplicar el mismo criterio en SD13/I-04A, conservando metas intermedias distintas cuando correspondan.
5. **Recontar catálogo:** RF/RNF/RT, prioridades, estados, aliases y filas; reconciliar totales de SD3 y anexos. No heredar números del plan SD9 antiguo ni cifras históricas del diagnóstico.
6. **Aplicar el resultado en calidad:** regenerar matriz y casos previstos de SD9/T-13; documentar supuestos de casos por requisito, exclusiones y conteos derivados. Actualizar también estimaciones de duración que dependan únicamente del volumen de casos, declarando parámetros usados.
7. **Mantener separada la capacidad operativa:** F2 no mueve hitos, modifica dotación ni declara que el volumen de casos cabe en una nueva capacidad aún no combinada. Si un resultado exige cambiar recursos/fechas, **ese subcaso y sus consumidores pasan a F1 completos**; no se deja como espera «F1 me enviará capacidad». Esta es una condición de independencia que debe revalidarse con el hallazgo concreto.
8. **Revisar tablas derivadas del catálogo/modelo:** totales, estados, matriz, indicador OTIF, entidades y sus fuentes. Esos objetos completos pertenecen a F2, no al frente editorial.

**IDs principales:** 2.15, 4.7–4.10; efectos en SD9/T-13 que el reparto anterior dejaba esperando catálogo. 2.16 usa C3 ya fijado; si resta ese ajuste, F2 lo aplica. Partes de 1.7/3.16 vinculadas a sus tablas.

**Cierre autónomo:** fuente, modelo, requisito, conteo, prueba prevista e indicador coinciden. No se necesita una entrega de otra IA para propagar los nuevos datos.

### F3 — Estructura, numeración, terminología y remisiones

**Documentos afectados:** SD4/T-11 y todas las ubicaciones citantes de las olas 2/3; anexos SD2/SD3 para numeración. No se modifica TRZ como tarea 5.4: ola 5 excluida.

**Tareas en orden interno:**

1. **Corregir jerarquía SD4 (3.13):** resolver mezcla `section`/`chapter`, contadores y montaje. Preservar labels existentes cuando sea posible; producir mapa por título/label de la nueva numeración.
2. **Cerrar remisiones de M9 y T-13/T-18 (2.11):** localizar el contenido real y corregir T-11, SD5, SD3 y SD4 que lo citan. El título/label del destino manda sobre números históricos del diagnóstico.
3. **Resolver remisiones no temporales de 2.12:** SD7/SD8 hacia SD4, SD3 y sus anexos. La fecha de transferencia SD13 es F1; las remisiones de TRZ quedan fuera por ola 5.
4. **Acordar y aplicar estilo de anexos SD2/SD3 (3.15):** un solo responsable decide la propuesta, obtiene aprobación humana si falta y aplica el resultado más sus citantes. No repartir el origen y el consumidor.
5. **Cerrar títulos y numeraciones existentes (3.1–3.3, 3.6, parte de 3.8/3.14):** «Metodologías», «Introducción a los Riesgos», cierres sin número, títulos en `minipage`, prefijos de tablas 6.A/6.B y duplicados 8.4. La RBS completa es de F1; F3 sólo informa su regla de numeración sin editar ese objeto.
6. **Aplicar terminología C10 (2.13):** nombre de M12/B-08/ElastiCache y «mes N» en los citantes; no redefinir el diccionario técnico. La aclaración de sala primaria/secundaria (4.9) se hace sin cambiar topología ni compromisos.
7. **Actualizar remisiones afectadas por sus cambios estructurales:** nunca corregir numeración y dejar la propagación para otra IA. No realizar la auditoría global 5.5.

**IDs principales:** 2.11, parte no temporal/no TRZ de 2.12, 2.13; 3.1–3.3, parte estructural de 3.6/3.8/3.14, 3.13, 3.15; 4.9. Títulos T-19/Tabla13.1 de 3.12 también aquí si siguen pendientes.

**Cierre autónomo:** estructura corregida y todas las remisiones existentes de su cadena actualizadas. F1/F2/F4/F5 no renumeran secciones ni cambian IDs estructurales por su cuenta: usan labels/títulos y conservan encabezados. Si una tarea obliga a alterar la estructura, su modificación y sus citantes se trasladan juntos a F3 antes de ejecutarla.

### F4 — Reparación bibliográfica y edición local independiente

**Documentos afectados:** fuentes y pasajes concretos de SD1–SD9/SD13 no reservados a otro frente. No es una «pasada final de todo» que deba esperar a los demás.

**Tareas en orden interno:**

1. **Reconstruir referencias SD5 (1.5):** consultar historial previo a `2f936555` para recuperar contexto, sin revertir mejoras posteriores. Resolver huecos, autor/año/título y llamadas, aplicando C13 a documentos propios.
2. **Cerrar citas aisladas de 3.9:** SD1/T-6, Ministerio de Salud en SD3, Kruchten en SD6, citas SD8/SD13. Localizar fuente real; si es una remisión numérica rota a otro SD, esa ocurrencia es F3, no una reparación bibliográfica de F4.
3. **Editar prosa local:** frases de entrada de listas SD4 (3.4), texto entre tablas SD2 (3.5), separación problema/solución SD2 (3.7), ubicación narrativa de párrafos SD3 (parte no estructural de 3.6), frase trunca T-9 y erratas (parte textual de 3.14). No cambiar reglas de negocio, valores ni encabezados.
4. **Corregir fuentes genéricas y notas editoriales (1.7):** sólo en pasajes no asignados a F1/F2/F5. Una nota que requiere resolver un cálculo o compromiso va al dueño de la cadena, no se borra como estilo.
5. **Revisar tablas estáticas del cuerpo (3.16):** sólo las que no dependen de decisiones de F1/F2/F5 ni cambian estructura F3. Para rediseñar, preservar label/posición de sección y no cambiar contenido técnico; si se precisa renumeración, la tabla y sus remisiones pasan a F3. No revisar aquí las futuras tablas que creen otros frentes.
6. **Declaraciones IA (3.10):** ajustes locales fieles a evidencia ya disponible, sin firmar contenido producido por otros frentes. La de SD8 sigue siendo manual; no trasladarla a una IA. Cada frente actualiza la declaración relativa a su propio trabajo sin inventar acreditación humana.

**IDs principales:** 1.5, partes editoriales de 1.7; 3.4, 3.5, parte de 3.6, 3.7, 3.9, partes de 3.10/3.14/3.16. No incluye limpieza 5.2 ni metadatos 5.3.

**Cierre autónomo:** cada pasaje asignado queda reparado sobre la base común sin reescribir los bloques técnicos de otros frentes. No prometer auditoría final del contenido que otras IAs todavía estén generando.

### F5 — Certificaciones, experiencia y formularios organizacionales

**Documentos afectados:** SD1 y T-6, sus evidencias y remisiones propias; sin crear SD12.

**Tareas en orden interno:**

1. **Revalidar certificaciones (4.6):** empresa/persona, alcance, evidencia y vigencia de CMMI/ISO27001/AWS. Las fechas del diagnóstico son pistas, no sustituyen los documentos disponibles.
2. **Redactar plan de renovación SD1:** responsable entre roles vigentes, actividad, fecha objetivo respecto al inicio del contrato, evidencia a obtener y tratamiento de falta de renovación. No afirmar renovación ya realizada sin respaldo.
3. **Propagar el estado correcto:** corregir pasajes de SD1/T-6 que declaren vigencia incompatible con la evidencia. Identificar si se afirma certificación de persona como si fuera de empresa o viceversa.
4. **Restituir rótulos oficiales T-6 (parte de 3.12):** contrastar la plantilla, restaurar campos alterados y mantener datos de experiencia acreditados; no inventar proyectos, períodos o certificados para rellenar.
5. **Cerrar tablas/declaración de estos bloques:** síntesis y fuentes de certificaciones/experiencia, texto de entrada/cierre y declaración IA de su trabajo. Las citas bibliográficas aisladas de T-6 siguen en F4; no duplicarlas.

**Límite:** no modificar dotación, horas, reserva ni programa de riesgos. Si el plan de renovación exige un cambio efectivo de esos compromisos, mover esa cadena de renovación completa a F1; no declarar independencia ficticia. F5 puede quedar más pequeño o desaparecer si el examen de evidencias demuestra ese enlace.

**IDs principales:** 4.6 (sólo SD1), parte T-6 de 3.12 y ajustes de 3.10/3.16 de sus bloques.

**Cierre autónomo:** plan de renovación y experiencia respaldados, con sus consumidores propios actualizados. Es un frente más liviano; no se fuerza una carga idéntica a la de F1.

## 4. Evitar nuevas dependencias y conflictos de escritura

Estas reglas son parte del reparto, no tareas que deban esperar a otra IA:

1. **Base común recibida:** identificar los commits/archivos disponibles una vez para arrancar. No reconstruir contratos K ni pedir nuevas definiciones de datos ya fijados por el canon.
2. **Propiedad por cambio, no por SD:** F1 puede cambiar fechas en SD13 y F2 su indicador OTIF. Eso no los hace dependientes, siempre que ninguno modifique el objeto del otro.
3. **Objetos enteros con un solo dueño:** una misma tabla, figura, cálculo, generador o párrafo técnico no se reparte entre dos frentes. Las tablas de riesgos/capacidad son F1; catálogo/modelo/pruebas funcionales/OTIF F2; estructura y remisiones F3; tablas estáticas editoriales F4; experiencia/certificaciones F5.
4. **Frontera por operación:** F3 cambia numeración/labels y referencias numéricas; los demás conservan esos elementos. Los demás citan por identidad de destino y mantienen labels existentes. No insertar secciones numeradas que desplacen destinos ajenos sin llevar esa cadena a F3.
5. **Copias independientes:** no usar el mismo checkout para frentes distintos ni hacer push compartido. Entregar diff acotado con objetos y base identificados; nunca sobrescribir el archivo completo con una copia de otro frente. Si se comparte una misma línea/objeto, mover la corrección completa a un único frente.
6. **Validación local:** cada frente prueba cálculos, coherencia de su cadena y compilación de su copia. No afirma haber validado la combinación de cambios que todavía no recibió. No se agenda aquí la ola 5.
7. **Dependencia descubierta:** no crear una espera nueva. Transferir productor y consumidores afectados a un mismo frente; si eso conecta dos cadenas grandes, fusionar esos frentes y reducir su número. El número cinco no es una condición técnica.

## 5. Cobertura y exclusiones explícitas

| IDs originales | Propiedad en este reparto |
|---|---|
| 1.1 | Excluido íntegramente |
| 1.2, 1.3, 1.6 | F1; sólo pendientes después de las correcciones ya recibidas |
| 1.4 | C1 ya corresponde a ola0; si resta un nombre en un objeto de olas1–4, su dueño lo corrige localmente sin reabrir ola0 como frente |
| 1.5 | F4 |
| 1.7 | Dueño del objeto: F1 operativo, F2 catálogo/datos, F3 estructura, F4 editorial, F5 certificados/experiencia |
| 2.1–2.10 | F1; usar valores canonizados sin hacerlos producir de nuevo por otra IA |
| 2.11 | F3 |
| 2.12 | F3 para remisiones estructurales; F1 para fecha de transferencia; TRZ fuera por ola5 |
| 2.13 | F3; diccionario ya establecido como entrada |
| 2.14 | F1 |
| 2.15–2.16 | F2 |
| 3.1–3.3 | F3 |
| 3.4–3.7 | F4 para prosa; F3 para jerarquía/encabezados de3.6 |
| 3.8 | F1 RBS completa; F3 numeración de tablas distintas de ese objeto |
| 3.9 | F4; remisiones numéricas propias se resuelven en F3 |
| 3.10 | Cada dueño respecto a su edición; F4 correcciones locales previas; SD8 manual del equipo |
| 3.11 | F1 |
| 3.12 | F1 T-15; F3 T-19/tipo5; F5 T-6 |
| 3.13, 3.15 | F3 |
| 3.14 | F4 prosa/errata; F3 numeración |
| 3.16 | Cada dueño sobre sus objetos; F4 sólo tablas estáticas no reservadas. No requiere esperar documentos futuros para corregir los existentes |
| 4.1–4.5 | F1 |
| 4.6 | F5, salvo vínculo operativo real que obligue a absorberlo en F1; SD12 excluido |
| 4.7–4.10 | F2, salvo4.9 que es F3 |
| 4.11 | F1 |
| 5.1–5.5 | Fuera del trabajo solicitado ahora |

## 6. Instrucción de inicio para cada IA

> Tu frente es F[N] de PLAN_FRENTES_POR_DEPENDENCIAS_2026-10-27.md. No uses el reparto A–E anterior ni contratos K. Trabaja desde la base de documentos recibida, tomando el canon ya decidido como entrada. Revalida sólo tus hallazgos de olas1–4 y ejecuta toda tu cadena, incluidos sus consumidores en otros SD. No crees capítulos de1.1 ni ejecutes olas0/5. Conserva los objetos asignados a otros frentes, no renumeres por tu cuenta y no escribas en un checkout ajeno. Informa qué cambios son de tu cadena y demuestra su cierre local. Si descubres una dependencia entre frentes, identifica el productor y sus consumidores para reagruparlos; no establezcas una espera nueva. Sin push ni decisiones humanas inventadas.

## 7. Conclusión práctica

**Sí hay cambios independientes; no todos los SD deben esperar a todos los demás.** La mayor cadena interdependiente es la operativa y se concentra en F1. Catálogo/datos/pruebas funcionales se concentra en F2; estructura/remisiones en F3; reparación editorial en F4; certificaciones/experiencia en F5 si no altera recursos/reservas.

Este reparto permite comenzar las cadenas con la misma base, sin intercambiar resultados intermedios entre IAs. Su límite está explícito: se entregan correcciones aisladas por cadena, no cinco SD completos finales sin combinación de cambios. Si las evidencias revelan nuevos enlaces, se fusionan los frentes afectados en vez de esconder la dependencia.
