# LafroX — Revisión integral de inconsistencias

## 1. Resultado y límites de la decisión

**La propuesta tiene desarrollo técnico sustantivo, pero requiere resolver 19 grupos de problemas antes de afirmar coherencia integral.** Hay 10 de severidad alta, 8 media y 1 baja; ninguno se clasifica crítico con la evidencia disponible. Complejidad: 8 alta, 9 media y 2 baja. La gravedad mide impacto; la complejidad mide coordinación para resolverlo, no horas.

Este informe propone soluciones implementables, **no autoriza ni aplica cambios a los entregables**. No es un dictamen de adjudicación, una certificación técnica ni un puntaje de Comisión. Las declaraciones de uso de IA se excluyen íntegramente de la evaluación.

Primero corresponde resolver obligaciones de soporte y seguridad, reglas sanitarias y de cobranza; después reconstruir programación factible y propagarla a calidad/riesgos. Cambiar únicamente textos o fechas no demuestra capacidad, cumplimiento ni aceptación.

**Corte de evidencia:** 10-10-2026, lectura focal final iniciada a las 15:02 hora de Chile. Rama `rama-md`; HEAD `113837d63b9afe6dbbebf489c3941668aebea592`. La auditoría comenzó con checkout limpio. Durante la preparación hubo una edición externa del S4, preservada: agrega FQDN y precisa escenarios del RPO residual. Las citas de S4 corresponden al archivo de trabajo actual, no exclusivamente a HEAD; SHA-256 de ese archivo: `55F7F708B227454ED2FCD943A00FE2410EB4085C7F1E89EC8DE7448C75409C0F`. La revisión final debe comprobar estabilidad de esta huella.

Se consultó la rama local `subdoc-4`, revisión `e151405fb4b80d557b5ef856fac7418c96d2fcb3`, sólo como antecedente y para objetos gráficos; no sustituye los Markdown actuales. Las 25 figuras de S4 apuntan a objetos existentes en `93294853b248c4bbf257a0a8c1981bea5f13fce5`: 13 PDF y 12 PNG. Los enlaces PDF aceptados no constituyen figuras ausentes. No se consultaron remotos ni se generaron derivados.

**Actualización acotada del corte:** a las 15:07:58 del 10-10-2026 se detectaron además cambios externos en T12, T11 y contexto. Se preservaron y se volvió a comparar T12/9.C: ahora hay 20 estados distintos, no los ocho del HEAD inicial. Los seis RT que cambian de No cumple a Cumple siguen siendo los únicos que añaden casos según la regla actual; el total propuesto 1.303 no cambia. La procedencia/autorización de esos cambios no se atribuye en este informe. Baseline efectivo: HEAD más esos bytes del worktree.

| Fuente focal | SHA-256 al corte actualizado |
|---|---|
| T12 | `07D9245A7F39DE8E80AD17AC8671108619FF4BAA86C651D8E2F337B11351D998` |
| T11 | `853B5CF68F2EF28C8C11CDB0D3177A44D6BB115BD740F57D37C3B542B85CDB89` |
| S9A | `4646E13836BB46E36295F09CFE00DC6F1276696DB0F1F75C79F5DE32F9629C6F` |
| T15 | `F60D9C711E23B5F383B8B41CE417CE9E4BD6D4B917DB37F2B8BA7D2857A28464` |

## 2. Inventario, fuentes y profundidad real

Los identificadores entre corchetes resuelven en el registro de fuentes del final a **rutas absolutas exactas**. `[T15]:660`, por ejemplo, significa el archivo T15 y su línea 660, numerada desde 1. Las superficies de corrección de cada ficha usan esos mismos identificadores; son propuestas para una autorización posterior.

| SD | Cuerpo | Anexos | Formularios | Cobertura de lectura |
|---|---|---|---|---|
| 1 | S1 | — | T6 | Lectura documental del capítulo, estructura/equipo y experiencia; acreditación externa no comprobada |
| 2 | S2 | S2A | — | Problema, actores, supuestos, exclusiones y figuras; cruces funcionales con S3 |
| 3 | S3 | S3A | T12 | Cuerpo y anexos; catálogo y T12 contrastados, estados comparados con 9.C |
| 4 | S4 | S4A | T11 | Lectura documental de lógica/física/DC y anexos; cálculos focales y objetos gráficos |
| 5 | S5 | S5A | — | Cuerpo y políticas/migración; diccionario por muestra crítica, no campo por campo |
| 6 | S6 | S6A | T9, T10 | Metodologías, adquisiciones, desarrollo y cadencias; lectura documental |
| 7 | S7 | S7A | T14, T15, T18 | EDT/diccionario, hitos, programación, implantación y dependencias; cálculos focales |
| 8 | S8 | S8A | T16 | Riesgos, escalas, reservas y calendario; modelo leído, no reejecutado |
| 9 | S9 | S9A | T13, T17 | Calidad, matriz de 645 IDs, planes y aceptación; cobertura computada documentalmente |
| 13 | S13 | S13A | T19 | Cinco innovaciones, contratos, indicadores, paquetes y trazabilidad |

**Total: 31 documentos, 10 cuerpos, 9 archivos de anexos y 12 formularios.** Se revisan los anexos contenidos en esos archivos, no se confunde un archivo consolidado con un único anexo. SD10–12 y SD14 no están disponibles en las ocho ramas locales consultadas por el equipo; no se penalizan como capítulos faltantes del Informe 2 ni se inventa su contenido.

Rigen [BA], [BTT], [CASO] y [ACL]. El prompt de Descargas es referencia de rúbrica: sus ausencias históricas y automatismos no prevalecen sobre las fuentes actuales. Se leyó el contexto de sesión, distinguiendo entradas vigentes e históricas; P01–P06 de la revisión anterior se revalidan abajo. CodeGraph no proporcionó índice útil para este material; se usó lectura y búsquedas Markdown, sin inicializar herramientas.

### 2.1 Comprobaciones transversales y resultados que no son hallazgos nuevos

| Control | Resultado y alcance |
|---|---|
| Títulos y formularios | Existen las secciones obligatorias de los diez cuerpos y los doce formularios correspondientes a [ACL] §11. En S4, 4.2/4.3 usan otro nivel de encabezado pero no están ausentes. Errata de formulario en S6A: RI-18 |
| Precios ofertados | El rastreo de monedas/montos no encontró una tarifa ofertada del proyecto. Los rangos UF del T6:72 son contratos anteriores, no precio de esta oferta; $4,2 millones en S2:87 proviene del Caso. Campos CLP del diccionario son tipos de datos. No se aplica exclusión económica por esas cifras. [BA]:792 prohíbe el precio ofertado, no los antecedentes del problema |
| Precio comercial del pedido | RF-03.11 en T12:43 conserva precio capturado; no se reproduce como vigente el defecto histórico de precio al despacho |
| Actores y módulos | Quince actores de sistema y equivalencias funcionales S3/S4 presentes; actores/interesados del diagnóstico no son el mismo universo. No se exige un actor 16 por abastecimiento |
| Ambientes/despliegue | S4 §4.2.4 describe Desarrollo, QA, Preproducción, Producción y DR, artefacto común e implantación por sitios. La presencia de diseño no acredita despliegues realizados |
| Autonomía/identidad | Diseño de 24 h en CD y turnos de terreno, verificación local de identidad y manifiesto de 26 h; no se ha ensayado expiración/revocación. Cámara interior: RI-12 |
| DR/RTO | Conmutación y exclusión de escritor descritas; presupuesto focal de 135 min inferior a 4 h. Histórico completo 8 h se distingue de recuperación funcional crítica 4 h. Clasificación de series térmicas: RI-10 |
| RPO residual | S4:3226 ahora delimita escenarios y registra pérdida de tres caminos más destrucción del sitio. Es límite de diseño conocido, no ensayo aprobado ni cumplimiento universal. No se reabre la ausencia histórica de explicación; cualquier aceptación contractual permanece del CLIENTE |
| Dotación/canales/umbrales | Tercer agente de mesa desde mes 25 y ajuste de jornada documentados. Canales CORREO/SMS/WHATSAPP/AVISO_EN_PORTAL alineados en la muestra. Cobertura ≥70 % de lógica y ≥80 % global coherente S1/S6/S9; no se repiten erratas ya corregidas |
| Cálculos focales | Térmica: 21×288 + 28×174 = 10.920 lecturas/día. Migración: 16,05478 GB fuente ×2 = 32,10956 GB destino; no significa tráfico doble. Eléctrico: 7.450 W×1,2=8.940 W. Reservas individual 20.948,16 y conjunta 20.198,98 son magnitudes distintas conciliadas |
| Gráficos y enlaces | S4:25 objetos reales; S5:10 PNG reales. RI-11 cubre destinos ausentes S1/S2/S3. Legibilidad, recortes, tamaño impreso y composición final PDF no verificados |
| Residuos editoriales/referencias | Rastreo focal de notas de proceso y referencias/anclas, sin causal global nueva por IA ni por sintaxis matemática. RI-18 registra la errata concreta; no se acredita un barrido perfecto de cada referencia bibliográfica |
| Calendario | Congelamientos y fechas futuras son compromisos; no ensayos cumplidos. Ventanas/HH, gates y secuencia: RI-02 a RI-05, una sola ficha por causa, aunque se propague a varios SD |

### 2.2 Trazabilidad de Informe 1: disponible, pero no integralmente acreditada

[BA]:749 exige tabla observación–respuesta–sección modificada; [BA]:333 exige observaciones previas resueltas. S5A, Anexo 5-K, Tabla A.24:1664–1670 y S13A, Anexo 13.D:99–109 sí contienen respuestas parciales. No hay original íntegro de observaciones de Comisión ni matriz integral que permita medir un porcentaje real de cierre.

Muestra directamente comprobada de S5A:
- Línea 1664, «Modelo, relaciones y diccionario insuficientes»: remite a 5.1/5-A/5-B/5-C; prueba en PREPROD futura.
- Línea 1665, «CAP, motor y autoridad no justificados»: remite a 5.2.1–3/5-B; ensayo offline programado.
- Línea 1666, «Migración sin volumen, herramientas, responsables ni ventana»: remite a 5.3/5-L/5-J; perfilado/actas y tiempos futuros.

El XLSX histórico de `main/Alex_LASECUELA` tiene diez filas de auditoría interna de SD4.2, no es el original de Comisión. Encabezado residual, rutas gráficas y política de sesión son antecedentes internos, no tres observaciones oficiales acreditadas. Para SD4.1/4.2 no se presume trazabilidad formal inexistente. El equipo debe aportar el original y reconciliar las tablas existentes; **no se inventa denominador ni porcentaje de corrección**.

## 3. Escalas y registro priorizado

**Severidad:** crítica = exclusión o daño grave inmediato inequívocamente acreditado; alta = obligación necesaria, criterio de aceptación o regla de negocio comprometidos; media = ambigüedad técnica/documental material que requiere definición; baja = defecto editorial localizado sin alteración sustancial del diseño. La clasificación se refiere a la evidencia de propuesta, no a incidentes ejecutados.

**Complejidad:** baja = modificación localizada y verificable; media = varias representaciones, catálogo o prueba; alta = decisión de alcance/arquitectura o reprogramación con capacidad, dependencias y propagación. Un defecto alto puede ser fácil de corregir y una ambigüedad media puede requerir mucho trabajo.

Tipos: **D** corrección documental directa; **T** ajuste técnico/documental; **E** decisión del equipo antes de modificar. La tabla indica tipo predominante; las fichas precisan qué permanece sin decisión.

| ID | SD | Problema | Severidad | Complejidad | Tipo | Dependencias |
|---|---|---|---|---|---|---|
| RI-01 | 1/3/7 | Soporte obligatorio excluido o no desarrollado | Alta | Alta | T | Dotación/alcance de operación |
| RI-02 | 7/8/9 | HH imposibles en ventanas de pruebas | Alta | Alta | T | RI-05, recursos y calendario |
| RI-03 | 7/9 | H12, archivo y acompañamiento incompatibles | Alta | Alta | E | Acta, RI-02 |
| RI-04 | 7/13 | Innovaciones llegan después de sus gates | Alta | Alta | T | RI-02, RI-05 |
| RI-06 | 3/9 | Estados y casos de prueba desactualizados | Alta | Media | D | Fuente T12 y modelo de casos |
| RI-07 | 3/4/5/13 | Bloqueo térmico OR frente a AND | Alta | Media | E | Calidad, reglas y pruebas |
| RI-08 | 2/3/4/5 | Cobranza de preventistas incluida/excluida | Alta | Alta | E | Alcance, catálogo/aceptación |
| RI-09 | 4/6 | SOC obligatorio condicionado y sin ubicación | Alta | Media | T | Modelo propio/subcontratado |
| RI-10 | 3/4/5 | Serie térmica: réplica, región y criticidad indefinidas | Alta | Alta | E | Clasificación/residencia/DR |
| RI-16 | 3/4/5/9 | Acuse comercial de 30 min sin solución completa | Alta | Alta | T | Cadenas, INT-08, evidencia |
| RI-05 | 7/8/9 | Predecesoras de pruebas no son únicas | Media | Alta | E | RI-02, red de actividades |
| RI-11 | 1/2/3 | Organigrama y catorce destinos gráficos no disponibles | Media | Media | T | Originales gráficos |
| RI-12 | 3/4 | Reconexión dentro de cámara vs al salir | Media | Media | E | Compromiso adicional/cobertura |
| RI-13 | 4 | Excepción TLS 1.3 sin límite contractual | Media | Media | E | Terceros y pruebas |
| RI-14 | 3/7 | Universo de capacitación de Concepción ambiguo | Media | Media | E | Levantamiento y turnos |
| RI-15 | 3/4/5/9 | Descuento excepcional sin requisito propio trazado | Media | Media | T | Supervisor comercial |
| RI-17 | 6/7 | T9 mantiene montaje general en mes 3 | Media | Baja | D | Cronograma por sitio |
| RI-19 | 4 | Cota por cross-docking vs volumen agregado ambigua | Media | Media | E | Distribución por sitio |
| RI-18 | 6 | Anexos atribuidos a T6 en vez de T9/T10 | Baja | Baja | D | Ninguna decisión de alcance |

## 4. Fichas accionables

### RI-01 — Soporte obligatorio pendiente de oferta

**Alta · complejidad alta · T · brecha de cumplimiento confirmada.**
- **Evidencia:** [T12]:599/605/610/613, RT-21.02/.08/.13/.16: «No cumple»; .02 indica «Falta: designar un gerente de servicio dedicado». [S3]:103 excluye RNF-21.02 y RNF-21.07.
- **Norma comprobada:** [BTT]:926,939,944 exige gerente dedicado, orientación y acceso a indicadores; :959 traslado según caso; [CASO]:754 lo hace exigible. No se usa RT-21.12 deseable como bloqueo.
- **Impacto:** la exclusión de un RNF propio no elimina el RT obligatorio equivalente; operación no queda completamente ofertada. [BTT]:95 establece puntaje cero en el ítem afectado cuando un requisito obligatorio se incumple u omite. Para obligaciones de seguridad, continuidad o arquitectura, además habilita la exclusión; no la establece automáticamente ni permite recalcular aquí notas de Comisión.
- **Solución propuesta:** diseñar gerente/dedicación, catálogo de consultas, indicadores autorizados y procedimiento/logística N2/N3 sin desatender otros sitios. Reconciliar RNF/RT y dotación/HH con funciones ya existentes; no cambiar a «Cumple» por una remisión vacía.
- **Superficie si se autoriza:** S1, S3, S3A, T12, S4, S4A, T14, T15, S9A. **Dependencia:** definición y asignación operativa; SD10 ausente no demuestra cobertura.
- **Cierre:** [ ] cuatro RT con componente/criterio/evidencia; [ ] roles y traslados compatibles con calendario; [ ] exclusiones y matriz de pruebas conciliadas.

### RI-02 — Capacidad insuficiente en ventanas de pruebas

**Alta · complejidad alta · T · contradicción aritmética confirmada.**
- **Evidencia:** [T15] §6:542 «6,4 HH efectivas por persona y día»; Tabla 6.1:654–665 declara horas, máximo de personas y fechas incompatibles. T13 reproduce ventanas.
- **Cálculo conservador:** 3.9.2, 320 HH, 27–31 mayo 2028, máximo 5: tres días L–V×5×6,4=96 HH. 3.9.3/.4/.5: 320 HH cada uno, 19–26 mayo, seis días×3×6,4=115,2 HH cada uno. 3.9.7:160 HH frente a 76,8. 3.8.4/.5/.8:320 HH cada uno, 21 octubre–9 noviembre 2027, catorce días×2×6,4=179,2 HH. No se restan feriados: la contradicción subsiste sin endurecer el cálculo.
- **Norma:** [ACL]:295–300 exige secuenciamiento/estimación y Gantt coherentes; [BA]:313 exige demostrar nivelación.
- **Impacto:** las tablas no acreditan que puedan ejecutarse los esfuerzos ni gates; probabilidades del modelo no reparan esta incompatibilidad.
- **Solución:** recalcular capacidad por paquete/día/perfil y recursos compartidos; elegir ventanas o dotación factibles sin reducir QA ni mover hitos por inferencia. Reejecutar red y análisis cuantitativo sólo tras aprobar la base.
- **Superficie:** T15, T13, T14, S7, S7A, S8, S8A, T16, S9, S9A, T17. **Dependencia:** RI-05 y disponibilidad real del equipo.
- **Cierre:** [ ] HH≤capacidad diaria de cada paquete; [ ] sin sobreasignación simultánea; [ ] feriados/calendario explícitos; [ ] hitos y modelo reproducibles actualizados.

### RI-03 — H12, archivo y acompañamiento sin una secuencia común

**Alta · complejidad alta · E · contradicción documental confirmada.**
- **Evidencia:** [T15]:86 supone «H12 firmado el 5 de octubre de 2028» y 2.361,33/102,67 HH; :686–687 programa 4.3.3 hasta 19 octubre y su antecedente 4.3.4 hasta 10 octubre; :731–732 cierra 9.1.1/.2 el 10 octubre. [S7A]:77–78 D-33/D-34 exige aceptación antes del cierre; [T14]:1761 exige archivo «todas las actas de H1 a H12» «Después del H12».
- **Norma:** [BA]:331 hito cumplido únicamente con acta; :318–325 condiciones copulativas de cierre; :335 revisión/subsanación.
- **Impacto:** cierre y reparto de acompañamiento se apoyan en firma anterior a sus evidencias.
- **Solución:** definir evento/acta que constituye H12, secuenciar aceptación/archivo y recalcular cuatro semanas por días reales, relevos y curva. No imponer 19 octubre como nueva fecha ni acortar acompañamiento para mantener HH por mes.
- **Superficie:** T15, T14, S7, S7A, T18, S9, T17, S1/S4 en distribución operativa afectada. **Dependencia:** equipo/Contraparte y ventanas contractuales.
- **Cierre:** [ ] ninguna actividad previa a H12 necesita acta futura; [ ] todas las actas archivadas después; [ ] reparto mensual reproduce fechas efectivas y cuatro semanas.

### RI-04 — Innovaciones comprometidas llegan después de integración/certificación

**Alta · complejidad alta · T · contradicción de gates confirmada.**
- **Evidencia:** [T14]:1311–1312/1320 «Entra al H4»; [S13]:112–113/369 vincula INN-01.P2/P3 e INN-03.P3 a H4; [T15]:667–668/676 termina el 19 noviembre 2027, después del H4 del 20 octubre y límite 16 noviembre (:495). INN-05.P3 termina 9 junio 2028 y .P4 empieza 3 julio (:680–681), aunque [S13]:608–609 exige H9 y certificación H10, programados 18 mayo/12 junio.
- **Norma:** [ACL]:294 incluye innovaciones en 100 % de EDT; [BA]:490 exige diseño/paquete/mes de incorporación.
- **Impacto:** el núcleo prometido no puede integrar/ser certificado en el gate que declara.
- **Solución:** separar núcleo verificable de piloto/seguimiento posterior, preservar compromisos y añadir predecesoras reales antes de integración/certificación; recalcular capacidad. Diferir alcance exige decisión expresa, no cambio de etiqueta.
- **Superficie:** S13, S13A, T19, T14, T15, S7A, S7, S8/S8A, S9/T13. **Dependencias:** RI-02/RI-05.
- **Cierre:** [ ] cada entrega INN tiene gate y predecesoras; [ ] QA y núcleo anteriores al gate; [ ] fechas factibles propagadas.

### RI-05 — Predecesoras incompatibles de pruebas no funcionales

**Media · complejidad alta · E · contradicción de red confirmada.**
- **Evidencia:** [S7A]:63 D-21 b y :74 D-31 b dicen «no dependen del resultado funcional» de 3.8.1/3.9.1; [T15]:654–658/661–665 sí declara esos paquetes como predecesoras.
- **Norma:** [ACL]:295–297 exige secuenciamiento coherente y CPM; no prescribe cuál opción debe elegir el equipo.
- **Impacto:** una red distinta cambia fecha temprana, reserva y riesgo del mismo gate.
- **Solución:** decidir el estado técnico necesario para carga/DR/seguridad/respaldo: versión integrada disponible o integración funcional aceptada. Modelar un evento de disponibilidad separado si corresponde, no borrar dependencias indiscriminadamente.
- **Superficie:** S7A, T15, T13, S9, S8/S8A/T16 y modelo de respaldo existente si se autoriza separadamente. **Dependencia:** RI-02.
- **Cierre:** [ ] una red canónica con criterio de entrada observable; [ ] fechas y simulación derivan de esa red; [ ] no hay aceptación adelantada ficticia.

### RI-06 — Matriz 9.C y catálogo de casos desactualizados

**Alta · complejidad media · D · divergencia de estados confirmada.**
- **Evidencia:** [T12]:629–638 RT-23.01/.02/.05–.10 «Cumple»; [S9A]:766–775 usa parcial para los dos primeros y «No cumple / Sin prueba: no ofertado / 0» para los seis últimos. Misma población de 645 IDs; comparación actual completa: 20 estados diferentes. Los otros 12 son RF14.03-BTT/19.03, RNF20.06/23.01/.02 y RT06.04/.29/07.04/08.10/.12/.14/11.13, Cumple en T12:159/189/261/278/279/374/399/408/428/430/432/469 frente a parcial en S9A:303/333/405/422/423/511/536/545/565/567/569/606. No modifican el número de casos porque ya tenían prueba.
- **Regla comprobada:** [S9A]:131 da un caso por RT no absorbido/ofertado. :139–145 conserva RT346 y total 1.297. [ACL]:329 exige trazabilidad; [BA]:333 evidencia y requisitos satisfechos.
- **Impacto/cálculo:** con los estados actuales y sin variar la regla: RT352 casos; total 544+302+352+105=1.303, 611 IDs con prueba propia y 34 sin ella (25 No cumple y 9 alias/absorbidos). T12 actual, orden Cumple/parcial/No cumple: RF161/19/1; RNF81/7/2; RT319/33/22; total 561/59/25. No se demuestra con ello WCAG, certificaciones ni disponibilidad del sitio externo.
- **Solución:** sincronizar estados desde fuente canónica, crear seis casos omitidos y recomputar tiempos/automatización/esfuerzo mediante el modelo explícito, no sumar HH arbitrarias.
- **Superficie:** S9A, S9:300–303, T13:123 y cifras derivadas T15/S7/S8 sólo si el modelo cambia. T12 únicamente si se decide corregir su evaluación fuente.
- **Cierre:** [ ] cero diferencias no justificadas de IDs/estados; [ ] sumas por familia y casos reproducidas; [ ] números derivados recomputados; [ ] verificaciones externas permanecen pendientes.

### RI-07 — Predicado térmico OR frente a AND

**Alta · complejidad media · E · contradicción sanitaria confirmada.**
- **Evidencia:** [S5] §5.1.1:141 «una crítica o sostenida activa el bloqueo» y §5.1.7:227 «crítico o sostenido». [S3A] RNG-04:533 y [S4] §4.1.4.2:835 dicen «crítica y sostenida»; S4A:443 coincide con AND.
- **Norma:** [ACL]:232–243 exige correspondencia de solución/arquitectura y :54 consistencia técnica. [CASO] exige registro térmico y decisión sanitaria, pero no resuelve por sí solo este operador.
- **Impacto:** OR y AND producen bloqueos distintos frente a lectura crítica breve o moderada sostenida.
- **Solución:** obtener decisión de Calidad sobre predicado normal aprobado y tabla de verdad; conservar aparte PREVENTIVA_FICHA, donde lectura fuera de ficha bloquea provisionalmente hasta aprobación. No usar esa regla provisional para justificar el OR de la regla final.
- **Superficie:** S3/S3A, S4/S4A, S5/S5A, S13/S13A, T12, S9A. **Dependencia:** parámetros por producto/etapa.
- **Cierre:** [ ] un predicado normal común; [ ] casos críticos breves, moderados sostenidos y lectura fuera del rango de la ficha con parámetros aún no aprobados; [ ] liberación sólo por Calidad; [ ] textos/contratos/pruebas alineados.

### RI-08 — Cobranza presencial de facturas por preventistas incluida y excluida

**Alta · complejidad alta · E · contradicción de alcance confirmada; histórica P03 vigente.**
- **Evidencia:** [T12]:87 RF-07.10 «facturas vencidas» y «rendición diaria» con M3/M7; :88 RF-07.11 «No cumple» limita M7 a reparto. [S3A]:92 incluye la función; :230 la excluye como independiente.
- **Norma:** [CASO] entrevista Sandra:480 incluye cobro de facturas anteriores y :544 exige registro en el momento/rendición el mismo día; [ACL]:229 trazabilidad del alcance.
- **Impacto:** actor/documentos cobrables no son unívocos; no es suficiente decir que ambos requisitos tienen nombres parecidos.
- **Solución:** definir operación única por actor, documento, recibo, caja y cierre. Si son alias, registrar equivalencia sin quitar comportamiento; si son funciones distintas, límites verificables. Mantener auditoría/idempotencia de cobros.
- **Superficie:** S2/S2A, S3/S3A, T12, S4/S4A, S5/S5A, S9A. **Dependencia:** responsable comercial/Finanzas; no rebajar Caso por exclusión propia.
- **Cierre:** [ ] recorrido preventista-factura-recibo-rendición completo; [ ] RF07.10/.11 conciliados; [ ] prueba y datos coherentes.

### RI-09 — SOC obligatorio con cobertura condicionada y ubicación no declarada

**Alta · complejidad media · T · cobertura documental incompleta confirmada.**
- **Evidencia:** [S6]:48 «SOC 24x7 es condicional a su subcontratación»; [T9]:94 «cobertura y niveles de servicio quedan sujetos a contratación»; [S6A]:61 reconoce ubicación no declarada.
- **Norma:** [BTT]:595 RT-11.17 exige SOC24×7 propio o subcontratado y ubicación/dotación/procedimientos.
- **Impacto:** la alternativa de adquisición no puede condicionar una prestación obligatoria; dotación estimada en S4A no acredita ubicación. [BTT]:95 asigna puntaje cero al ítem afectado por incumplimiento u omisión de requisitos obligatorios; en seguridad, continuidad o arquitectura habilita además la exclusión conforme al Art. 58°, sin hacerla automática. Se conserva severidad alta: este informe no dicta exclusión ni recalcula notas.
- **Solución:** comprometer 24×7 en ambas modalidades, indicar sede/operación propuesta, turnos, escalamiento y procedimientos; dejar la evidencia de contrato como futura sin declarar contratación ya realizada.
- **Superficie:** S6/S6A/T9, S4/S4A/T11, T12 y T14/T15 si cambia dotación. **Dependencia:** modalidad SOC real propuesta.
- **Cierre:** [ ] obligación no condicional; [ ] ubicación y dotación declaradas; [ ] procedimientos y evidencia futura diferenciados.

### RI-10 — Conjuntos térmicos, región de réplica y RPO sin clasificación inequívoca

**Alta · complejidad alta · E · ambigüedad material, no pérdida de datos demostrada; P05 vigente.** La severidad alta se justifica por la posible afectación de datos sanitarios críticos y objetivos obligatorios de continuidad, no porque se haya observado una pérdida ni probado incumplimiento de cada conjunto histórico.
- **Evidencia:** [S5A] 5-D:1306 guarda serie detallada cinco años «sin réplica fuera de la región declarada». [S4] §4.3.2.2:3182 copia a secundaria analítica con cinco años de temperatura/trazabilidad. :3198 clasifica telemetría crítica con RPO≤15 min; analítica tiene ≤24 h. [S5]:263 raw 30 d/detalle 5 años y «El agregado no permite reconstruir una lectura perdida»; [S4]:1810 expira raw consolidado.
- **Norma:** [BTT]:420 y [BA]:358 RPO15 min/RTO4 h para servicios críticos; [S3A] RNF09.02:280 identifica registro sanitario crítico con piso 5 años. La norma no permite inferir que todo agregado tenga RPO15 min ni que el archivo completo sea no crítico.
- **Impacto:** no se puede seguir inequívocamente qué lectura original es recuperable, dónde y con qué pérdida; tampoco decidir si 1306 y 3182 describen la misma serie.
- **Solución:** tabla por dataset (raw, detallado, versiones interpretativas, agregado, evidencia sanitaria), criticidad, autoridad, retención, región, réplica/backup, RPO/RTO y reconstrucción. Confirmar destino de tel_archivo_termino con CLIENTE; mantener GPS personal separado, sin ampliar autorización internacional.
- **Superficie:** S3A, S4/S4A, S5/S5A, T12, S8A, S9A/T13. **Dependencia:** residencia/clasificación y aprobación contractual; no basta renombrar «analítica».
- **Cierre:** [ ] trazabilidad lectura-original-archivo-réplica; [ ] ningún dato crítico queda sólo en agregado; [ ] políticas regionales y objetivos consistentes; [ ] restauración futura medirá detalle perdido.

### RI-11 — Evidencia gráfica no disponible en S1/S2/S3

**Media · complejidad media · T · dependencia documental confirmada.**
- **Evidencia:** [S1] §1.2:140 describe organigrama sin objeto gráfico; [S2]:130/152/174/194/214/238 enlaza seis PDF figura 2.1–2.6; [S3]:167/177/187/220/224/232/236/240 enlaza ocho objetos de figures/. Destinos/nombres no están en checkout ni como objetos coincidentes en las ocho ramas locales examinadas.
- **Norma:** [ACL]:196 exige organigrama explicado y :61 figuras integradas. Esto no es una acusación de IA.
- **Impacto:** lector del Markdown no puede abrir/cotejar esas figuras. No se niega que un PDF antiguo pueda contener equivalente incrustado; equivalencia/vigencia no comprobada.
- **Solución:** localizar originales autorizados, cotejar vigencia (actores/cifras/reglas) y corregir enlaces; si no existen, decidir producción gráfica en flujo autorizado, sin generar derivados dentro de esta tarea ni eliminar figuras para ocultar carencia.
- **Superficie:** S1, S2, S3; rutas gráficas reales sólo tras autorización. **Dependencia:** aporte de originales.
- **Cierre:** [ ] organigrama objeto real; [ ]14 destinos existentes y correctos; [ ] figuras vigentes explicadas; [ ] presentación PDF se comprueba por separado.

### RI-12 — Sincronización dentro de cámara frente a sincronización al salir

**Media · complejidad media · E · contradicción de compromiso confirmada; P04 vigente.**
- **Evidencia:** [S3A]:282 RNF09.04 «al recuperar conectividad dentro de la cámara»; [S3]:207 «sincronización diferida al salir»; [T12]:213 reproduce ambas.
- **Norma:** [CASO]:574/745 exige operación a−22°C sin cobertura interior/turno sin conexión; no exige señal dentro.
- **Impacto:** aceptación podría exigir una cobertura interior no ofrecida por la solución.
- **Solución:** confirmar si conectividad interior es compromiso adicional o redacción errónea. Expresar operación offline y sincronización ante conectividad efectiva, incluida salida; no retirar por inferencia un compromiso voluntario.
- **Superficie:** S3/S3A/T12, S4/S4A y S9A si criterio cambia. **Dependencia:** decisión de alcance/levantamiento.
- **Cierre:** [ ] condición de reconexión única y comprobable; [ ] autonomía/reconciliación sin pérdida ni duplicación; [ ] no promesa de señal inexistente.

### RI-13 — Excepción TLS1.3 abierta para terceros

**Media · complejidad media · E · ambigüedad contractual, no negociación insegura observada.**
- **Evidencia:** [S4]:725 «TLS1.3 para las interfaces compatibles»; [S4A]:1175 «Un tercero con limitación de protocolo exige excepción documentada y tratamiento».
- **Norma:** [BTT]:581 y [BA]:379 exigen TLS1.3, sin excepción automática por incompatibilidad.
- **Impacto:** documentación de excepción no equivale a autorización para rebajar el requisito.
- **Solución:** inventariar interfaces/versión exigida y cerrar la cláusula: TLS1.3 obligatorio; incompatibilidad bloquea incorporación o requiere pronunciamiento formal del CLIENTE. Un proxy compatible no demuestra por sí solo conformidad de un tramo inseguro.
- **Superficie:** S4/S4A/T11/T12, S9A. **Dependencia:** datos de terceros y criterio contractual.
- **Cierre:** [ ] versión/terminación por tramo; [ ] sin fallback autorizado por texto unilateral; [ ] pruebas de negociación previstas, no declaradas ejecutadas.

### RI-14 — Capacitación no identifica universo de Concepción

**Media · complejidad media · E · ambigüedad de cobertura; P06 revalidado.**
- **Evidencia:** [S3A] estrategia:602 «Preparadores (120 personas)»; S-39:440 identifica 120 de Talca y supone «60 preparadores a la vez» en Concepción, sujetos a levantamiento mes 1.
- **Norma:** [BTT]:985 capacitación por perfil y :990 actualización/personal nuevo; [BA]:324 exige personal capacitado/certificado para cierre de marcha blanca. [CASO]:129/157 distingue ambos CD y turnos.
- **Impacto:** no se acredita que 120 sea universo total ni que formación cubra turnos de Concepción; 60 simultáneos no equivale a 60 personas únicas adicionales.
- **Solución:** incluir cobertura explícita por sitio/perfil, separar aforo simultáneo, dotación y personas únicas; dimensionar jornadas/turnos con levantamiento y regla de actualización sin costo adicional. No reemplazar 120 por 180 automáticamente.
- **Superficie:** S3A, S3, T14/T15/T18, T12 si refiere población. **Dependencia:** nómina/turnos y levantamiento; no inventar cifras.
- **Cierre:** [ ] ambos CD explícitos; [ ] universo único y simultaneidad separados; [ ] cobertura/jornadas/certificación trazadas al plan.

### RI-15 — Descuento excepcional sin requisito propio trazado

**Media · complejidad media · T · brecha de trazabilidad, no ausencia de implementación probada.**
- **Evidencia:** [S3A] RNG16:545 «La autorización de descuentos necesita un requerimiento propio» remite RF03.07 promociones.
- **Norma:** [ACL]:229 exige catálogo priorizado/trazable; [BA]:333 trazabilidad hacia requisitos satisfechos.
- **Impacto:** promoción vigente y excepción autorizada no son el mismo criterio de aceptación.
- **Solución:** crear requisito propio sólo con autorización, o demostrar que uno existente cubre supervisor/pedido/monto/motivo antes de confirmar. Mapear actor, campos y prueba con motivo de rechazo, no añadir ID arbitrario al catálogo.
- **Superficie:** S3A/S3/T12, S4A, S5A, S9A. **Dependencia:** definición comercial y esquema de IDs.
- **Cierre:** [ ] autorización excepcional verificable; [ ] requisito/contrato/datos/caso enlazados; [ ] contador y alias reconciliados si cambia población.

### RI-16 — Acuse comercial dentro de 30 min no desarrollado completamente

**Alta · complejidad alta · T · brecha reconocida en la oferta, no contradicción semántica.**
- **Evidencia:** [T12]:221 RNF12.03 «Cumple parcialmente» y «Falta: envío del acuse comercial [...] dentro de30min desde la descarga»; ofrece MDN técnico de transporte hasta 15 min.
- **Norma/compromiso:** RNF12.03 trazado en S3A3.B; [CASO]:579/748 articula entrega/guía/acuse; [ACL]:229–230 requiere criterios de aceptación del alcance comprometido.
- **Impacto:** MDN confirma transporte AS2, no recepción comercial de la entrega; no satisface el reloj desde descarga.
- **Solución:** definir evento de descarga, evidencia comercial, generación/entrega/acuse, vínculo con guía y aviso, canal por cadena, cola offline y tratamiento del plazo. Confirmar límites de terceros sin afirmar efectos legales acreditados.
- **Superficie:** S3A/T12, S4/S4A(INT08/4-U), S5/S5A, S9A/T13. **Dependencia:** contratos de cadenas, evento y norma tributaria verificada por responsables.
- **Cierre:** [ ] acuse comercial distinto de MDN; [ ] reloj 30 min/end-to-end; [ ] prueba descarga-guía-aviso-recibo; [ ] excepciones/falla/offline tratadas.

### RI-17 — Narración de adquisiciones conserva mes 3 para todo equipamiento

**Media · complejidad baja · D · contradicción localizada.**
- **Evidencia:** [T9] §4:75 «incluidos racks, servidores y equipos de borde [...] instalación en mes3»; Tabla:83–84 sitúa racks 4–5, Concepción 4, bordeCD5/cross 9. [S6]:48 usa el calendario por sitio correcto.
- **Norma:** [ACL]:281 gestión de adquisiciones y :295–296 consistencia con plan/metodología.
- **Impacto:** relato contradice secuencia recibo-sala-montaje-puesta en servicio aunque tablas estén corregidas.
- **Solución:** reemplazar generalización del párrafo por distinción sistemas de sala 3/recepción 4 y montaje/puesta en servicio por sitio, remitiendo a tabla y T14/T15. No cambiar calendario correcto.
- **Superficie:** T9:75. **Dependencia:** ninguna decisión nueva si se conserva tabla vigente.
- **Cierre:** [ ] narración y tabla idéntica secuencia; [ ] recepción de sala no igual a commissioning de todos los equipos.

### RI-18 — Identificación de formulario errónea en anexos de metodologías

**Baja · complejidad baja · D · defecto editorial confirmado.**
- **Evidencia:** [S6A]:5 «Formulario: Formulario T-6».
- **Norma:** [ACL]:281/287 asigna T9/T10 a metodologías; T6 corresponde experiencia [ACL]:202.
- **Impacto:** identificación documental induce remisión al formulario de otro capítulo.
- **Solución:** identificar anexos de S6 y T9/T10 pertinentes, sin renombrar T6 ni mover contenido.
- **Superficie:** S6A:5. **Dependencia:** ninguna.
- **Cierre:** [ ] identificación y referencias de portada acordes con contenido/índice.

### RI-19 — Cota de cada cross-docking frente a volumen agregado

**Media · complejidad media · E · ambigüedad de dimensionamiento, no error global demostrado.**
- **Evidencia:** [S4] Tabla 23:2708 «Cada cross-docking»1,17/0,78/2,17 TPS; [S4A] TablaA.32:1471 INT04 toma 1.400×4=5.600 diarios y dice «cota de una plataforma». A.31 descompone operaciones locales; A.36 y perfil agregado ya fueron corregidos en CD-01.
- **Norma:** [ACL]:253 dimensionamiento con supuestos de volumen/concurrencia/crecimiento.
- **Impacto:** no queda inequívoco qué población es reparto real por sitio y cuál cota conservadora aplicada independientemente para dimensionar hardware.
- **Solución:** declarar distribución normal/peak por sitio y agregación, rotular cotas locales y explicar si total INT04 es agregado o extremo de una plataforma. Recalcular sólo magnitudes afectadas por esa definición.
- **Superficie:** S4§4.2.6, S4A4-W/T11 si cambia capacidad. **Dependencia:** reparto operacional por plataforma.
- **Cierre:** [ ] población/unidad de cada fila explícita; [ ] totales sin doble conteo; [ ] cotas por sitio diferenciadas. No multiplicar tráfico global por 3 sin demostrar reparto.

## 5. Orden de resolución y decisiones del equipo

1. **Cerrar decisiones de alcance/regla:** RI-01/07/08/09/10/12/13/14/15/16. Identificar quién valida y qué parte se compromete; no cambiar estados sin diseño/evidencia.
2. **Fijar una sola red y capacidad:** RI-05→RI-02→RI-04/03. Conservar hitos de Bases; toda alternativa de dotación/ventana debe mostrar factibilidad y disponibilidad.
3. **Propagar derivados:** RI-06 y efectos de calendario a S7/S8/S9/S13/formularios. Reejecución futura de modelo/pruebas bajo autorización; no validar simulación con sólo coincidencia de cifras.
4. **Resolver evidencia/edición localizada:** RI-11/17/18/19; recuperar fuentes reales, no sustituir figuras actuales S4/S5 por antiguas.
5. **Revisión integral posterior:** comprobar IDs/contratos/actores/fechas/HH/retención/RPO/títulos/enlaces y trazabilidad contra observaciones originales aportadas.

Decisiones reales, separadas de correcciones directas:
- **D-01:** regla térmica normal AND u OR validada por Calidad, distinta de régimen provisional.
- **D-02:** cobranza de preventistas: alias de función comprometida o límites distintos; excluir lo exigido por Caso no es alternativa equivalente.
- **D-03:** cuál acta/evento constituye H12 y desde cuándo se cuenta acompañamiento.
- **D-04:** precondición real de pruebas no funcionales y asignación factible de recursos.
- **D-05:** datasets térmicos/regiones/criticidad, modalidad SOC y tratamiento de terceros TLS: no presumir aprobación.
- **D-06:** alcance adicional de reconexión interior, universo de capacitación y reparto por plataforma.

Cada decisión debe recibirse de a una con su evidencia. Donde hay un requisito obligatorio, la alternativa no es «cumplir o no cumplir» sin consecuencia: procede ofertar solución conforme o plantear formalmente la imposibilidad al mandante. Ampliar dotación preserva ventanas pero requiere disponibilidad/costo separado de la oferta técnica; ampliar ventanas reduce presión pero puede consumir reservas y violar gates. Esos tradeoffs deben calcularse, no elegirse en este informe.

## 6. Lista de cierre y límites de verificación

- [ ] Equipo acepta/rechaza cada solución propuesta y autoriza superficies concretas.
- [ ] Decisiones D-01–D-06 registradas sin datos inventados.
- [ ] Causas resueltas en fuente canónica; derivados y formularios actualizados.
- [ ] Cálculos de capacidad por día y red recalculados; modelos/simulaciones reejecutados con evidencia.
- [ ] MatrizT12/9.C sin divergencias injustificadas; sumas y esfuerzo derivados reproducibles.
- [ ] Observaciones originales de Informe 1 incorporadas a trazabilidad completa, preservando respuestas ya existentes.
- [ ] Figuras/enlaces reales disponibles; legibilidad PDF revisada posteriormente en entorno autorizado.
- [ ] Ensayos DR, carga, offline, migración, TLS y acuses ejecutados en hitos previstos; hoy son futuros.
- [ ] Certificaciones, alianzas, proyectos, testimonios y sitio institucional acreditados por evidencia externa autorizada.

**Lo no acreditado no equivale automáticamente a un defecto:** no se ejecutó aplicación, DDL, migración ni infraestructura; no se reejecutó Monte Carlo; no se probó disponibilidad externa, WCAG ni vigencia de certificados; no se abrió una conexión remota; no se compiló/renderizó/transformó LaTeX ni PDF. El diccionario SD5 no se verificó atributo por atributo. Las comprobaciones de cálculos, contratos, tablas y referencias fueron focales o por muestra; la lectura documental no implica validación exhaustiva de cada atributo ni ejecución de ningún DDL. El barrido de enlaces no demuestra cada ancla bibliográfica externa ni cada imagen incrustada histórica. Las fechas de 2027/2028 son programación futura, no hechos cumplidos.

Históricos preservados: CD-01, precio del pedido, canales, escritores al promover standby, recuperación 4/8 h, A.31/A.36 y reservas conciliadas no se presentan como defectos pendientes antiguos. P01→RI-04; P02→RI-03; P03→RI-08; P04→RI-12; P05→RI-10; P06→RI-14; D01→RI-11.

### Control del propio informe

Documento pasivo: no aplica RED/GREEN. Comprobaciones estructurales del informe: inventario de 31 documentos, 19 IDs y 19 fichas, enlaces locales y `git diff --check`; los resultados observados se registran en la tarea. RI-03, verificación independiente documental, completada: las 19 fichas, citas de severidad alta, normas, cálculos focales, comparación de 645 IDs/20 estados distintos, cinco huellas y codificación UTF-8 fueron comprobados. Se incorporaron sus correcciones puntuales de régimen térmico provisional, consecuencia normativa, alcance de lectura y justificación de severidad. Esto no acredita ejecución técnica ni aprobación de la propuesta. `git diff --check` no incluye el informe y la tarea aún no versionados: su whitespace se comprobó mediante script de lectura. No hay aprobación nativa: herramienta no disponible. Espejo Engram pendiente por indisponibilidad. Escribir este informe no implementa los arreglos.

## 7. Registro de fuentes

[S1]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/01_presentacion_empresa/LAFROX-Subdocumento1.md
[T6]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/01_presentacion_empresa/LAFROX-Formulario-T-6.md
[S2]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/02_problema_necesidad/LAFROX-Subdocumento2.md
[S2A]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/02_problema_necesidad/LAFROX-Subdocumento2-Anexos.md
[S3]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/03_esquema_solucion_alcance/LAFROX-Subdocumento3.md
[S3A]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md
[T12]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md
[S4]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/04_arquitectura/LAFROX-Subdocumento4.md
[S4A]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/04_arquitectura/LAFROX-Subdocumento4-Anexos.md
[T11]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/04_arquitectura/LAFROX-Formulario-T-11.md
[S5]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/05_modelo_datos/LAFROX-Subdocumento5.md
[S5A]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/05_modelo_datos/LAFROX-Subdocumento5-Anexos.md
[S6]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/06_metodologías/LAFROX-Subdocumento6.md
[S6A]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/06_metodologías/LAFROX-Subdocumento6-Anexos.md
[T9]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/06_metodologías/LAFROX-Formulario-T-9.md
[T10]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/06_metodologías/LAFROX-Formulario-T-10.md
[S7]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/07_PlanDeTrabajo_EDT_Cronograma_Implantación/LAFROX-Subdocumento7.md
[S7A]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/07_PlanDeTrabajo_EDT_Cronograma_Implantación/LAFROX-Subdocumento7-Anexos.md
[T14]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/07_PlanDeTrabajo_EDT_Cronograma_Implantación/LAFROX-Formulario-T-14.md
[T15]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/07_PlanDeTrabajo_EDT_Cronograma_Implantación/LAFROX-Formulario-T-15.md
[T18]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/07_PlanDeTrabajo_EDT_Cronograma_Implantación/LAFROX-Formulario-T-18.md
[S8]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/08_plan_riesgos/LAFROX-Subdocumento8.md
[S8A]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/08_plan_riesgos/LAFROX-Subdocumento8-Anexos.md
[T16]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/08_plan_riesgos/LAFROX-Formulario-T-16.md
[S9]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/09_plan_calidad/LAFROX-Subdocumento9.md
[S9A]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/09_plan_calidad/LAFROX-Subdocumento9-Anexos.md
[T13]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/09_plan_calidad/LAFROX-Formulario-T-13.md
[T17]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/09_plan_calidad/LAFROX-Formulario-T-17.md
[S13]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/13_innovaciones/LAFROX-Subdocumento13.md
[S13A]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/13_innovaciones/LAFROX-Subdocumento13-Anexos.md
[T19]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/13_innovaciones/LAFROX-Formulario-T-19.md
[BA]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/Bases/Bases_Administrativas.md
[BTT]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/Bases/Bases_Tecnicas_Transversales.md
[CASO]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/Bases/Caso_02_Logistica.md
[ACL]: C:/Users/alexa/Desktop/Universidad/FEP/LafroX/LafroX/Bases/aclaraciones-licitacion.md

