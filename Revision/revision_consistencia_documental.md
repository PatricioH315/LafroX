# LafroX — Pendientes de coherencia entre documentos

## Resultado vigente

Quedan **seis grupos de contradicciones o ambigüedades documentales** y **una dependencia gráfica separada**: catorce destinos locales de figuras no están disponibles en este checkout. Las correcciones respaldadas de CD-01 están cerradas; no se repiten como pendientes.

Este informe revalida los asuntos abiertos de la revisión anterior sobre `rama-md`, al 10 de octubre de 2026. No constituye una nueva auditoría exhaustiva de todo el proyecto ni una auditoría de cumplimiento del T-12. Ese formulario se cita únicamente cuando aporta una afirmación que contradice otra representación documental. No se modifican entregables originales ni se acreditan ensayos, firmas o aceptación del CLIENTE.

La **prioridad** expresa el impacto de la divergencia; la **complejidad** expresa la coordinación necesaria para resolverla, no un puntaje de cumplimiento. Las Bases prevalecen sobre las decisiones de diseño.

## Pendientes interdocumentales

### P01 — Innovaciones exigidas para H4 terminan después del hito

**Tipo:** contradicción de compromiso y programación. **Prioridad:** alta. **Complejidad:** alta.

- **Evidencia:** T-14, cuenta 3.10, exige INN-01.P2/P3 y INN-03.P3 dentro del H4 ([T-14:1311–1312,1320][t14]). T-15 programa 3.10.1.2, 3.10.1.3 y 3.10.3.3 hasta el 19-11-2027 ([T-15:667–668,676][t15]); H4 se entrega el 20-10 y su límite es 16-11 ([T-15:495][t15]).
- **Impacto:** el producto prometido para H4 no está terminado ni verificable según su propia programación, incluso al límite de entrega.
- **Solución recomendada:** reprogramar el núcleo funcional comprometido y su QA para que esté listo antes de la integración 3.8.1, preservando H4. Recalcular secuencia, predecesoras, carga y capacidad; distinguir el piloto/seguimiento posterior sin trasladar allí las funciones exigidas para H4. Una nueva etiqueta de paquete no resuelve el desfase.
- **Decisión necesaria:** confirmar si se conserva el compromiso funcional en H4 y se autoriza su reprogramación coordinada. No hay fechas factibles ni refuerzos acreditados todavía; cualquier reducción o diferimiento del compromiso requiere decisión expresa.

### P02 — H12, acta final, cierre dependiente y HH usan supuestos incompatibles

**Tipo:** contradicción entre secuencia y representaciones de fecha/esfuerzo. **Prioridad:** alta. **Complejidad:** alta.

- **Evidencia de fechas:** T-15, supuesto de acompañamiento, usa H12 firmado el 05-10-2028 ([T-15:86][t15]); el acta final 4.3.3 se programa del 11 al 19-10 y el cierre 9.1.2 del 02 al 10-10 ([T-15:686,732][t15]). T-14 exige que 9.1.2 se ejecute después de H12 y conserve todas sus actas ([T-14:1761][t14]).
- **Evidencia de HH:** el mismo supuesto reparte 4.3.2 en 2.361,33 HH del mes 21 y 102,67 del mes 22; la curva concentra cierre/estabilización en mes 21 y muestra cero en esa columna del mes 22 ([T-15:86,379–380][t15]).
- **Impacto:** la firma supuesta, el archivo final y el acompañamiento no comparten una única referencia temporal; la curva no reproduce el reparto declarado.
- **Solución recomendada:** establecer una sola secuencia de evidencia, firma de H12, archivo y acompañamiento; después recalcular las mismas cuatro semanas por días reales y actualizar curva, relevos y documentos relacionados. No mover sólo una fecha ni reducir el acompañamiento para conservar la curva.
- **Decisión necesaria:** definir qué acta y fecha representan el cierre efectivo de H12 y desde qué evento comienza el acompañamiento. La fecha resultante debe respetar revisión, dependencias y ventanas del Caso; no se propone una fecha no comprobada.

### P03 — Cobranza presencial por preventistas aparece incluida y excluida

**Tipo:** contradicción de alcance funcional. **Prioridad:** alta. **Complejidad:** alta.

- **Evidencia:** RF-07.10 del T-12 declara captura por el preventista de efectivo por facturas vencidas, recibo provisional y rendición diaria, mediante M3/M7 ([T-12:87][t12]). RF-07.11 excluye la cobranza presencial de facturas como función independiente y limita M7 al reparto ([T-12:88][t12]); el Anexo 3.A reserva la cobranza a crédito al equipo del CLIENTE ([SD3-Anexos:230][a3]).
- **Impacto:** las descripciones no permiten saber si la persona preventista cobra facturas vencidas ni qué captura y rendición se ofrecen. El T-12 es evidencia de esa divergencia, no objeto de una auditoría adicional.
- **Solución recomendada:** definir una sola operación con actor, documentos cobrables, recibo y rendición; si ambas denominaciones describen la misma función, explicitar la equivalencia sin duplicar ni excluir un comportamiento ya comprometido. Si son distintas, documentar el límite verificable de cada una y propagarlo a SD3, SD4 y SD5.
- **Decisión necesaria:** confirmar si la oferta incluye el cobro presencial de facturas vencidas por preventistas, o lo reserva efectivamente al equipo del CLIENTE. No cambiar estados ni denominadores antes de resolver esa definición.

### P04 — Reconexión dentro de cámara frente a sincronización al salir

**Tipo:** contradicción entre requisito redactado y solución. **Prioridad:** media. **Complejidad:** media.

- **Evidencia:** RNF-09.04 dice que recupera conectividad y sincroniza dentro de la cámara ([SD3-Anexos:282][a3]); la solución mantiene captura sin señal y sincroniza al salir ([SD3:207][s3]). El T-12 reproduce ambas afirmaciones en descripción y componente ([T-12:213][t12]).
- **Base aplicable:** el Caso exige operar a −22 °C sin cobertura interior y sin conexión durante un turno completo; no exige recuperar señal dentro ([Caso:574,745][caso]).
- **Impacto:** el criterio de aceptación podría exigir conectividad interior que la solución descrita no garantiza.
- **Solución recomendada:** mantener operación offline dentro y sincronización cuando se recupere conectividad, incluida la salida, conforme a las Bases. Corregir la redacción sólo después de distinguir si la cobertura interior era un compromiso adicional voluntario; no retirarlo por inferencia.
- **Decisión necesaria:** confirmar si se ofertó reconexión interior como condición adicional o si esa frase es una formulación errónea del comportamiento offline.

### P05 — Registros térmicos: restricción regional frente a copia secundaria

**Tipo:** ambigüedad de conjuntos de datos y posible contradicción de réplica. **Prioridad:** alta. **Complejidad:** media.

- **Evidencia:** el Anexo 5-D mantiene `tel_archivo_termino`, serie detallada, sin réplica fuera de la región declarada ([SD5-Anexos:1306][a5]). SD4 4.3.2.2 copia de forma diferida analítica con cinco años de temperatura y trazabilidad a la región secundaria; declara sa-east-1/us-east-1 y aprobación del CLIENTE ([SD4:3182][s4]).
- **Impacto:** no está explícito si la restricción alcanza la misma serie incluida en recuperación o si las dos frases describen conjuntos distintos. No se demuestra una contradicción definitiva sin identificar esos conjuntos.
- **Solución recomendada:** mapear archivo detallado, serie consolidada y analítica a destinos de réplica y retención concretos, y armonizar ambas políticas. Conservar la restricción separada de GPS personal ([SD5-Anexos:1308][a5]); no ampliar réplicas ni presumir autorización del CLIENTE.
- **Decisión necesaria:** precisar qué conjuntos térmicos se copian a us-east-1 y cuáles permanecen sólo en la región primaria; confirmar si `tel_archivo_termino` forma parte de esa copia.

### P06 — Capacitación no delimita preparadores de Talca y Concepción

**Tipo:** ambigüedad de población y cobertura entre representaciones. **Prioridad:** media. **Complejidad:** media.

- **Evidencia:** la estrategia de participación/capacitación nombra 120 preparadores ([SD3-Anexos:602][a3]). S-39 identifica esos 120 en Talca y supone 60 preparadores simultáneos en Concepción, sujetos a levantamiento en mes 1 ([SD3-Anexos:440][a3]).
- **Impacto:** no puede comprobarse si la formación prevista incluye Concepción ni si sus turnos y capacidad están cubiertos. Sesenta posiciones simultáneas no acreditan sesenta personas únicas adicionales.
- **Solución recomendada:** separar cobertura de capacitación por sitio de dotación aún supuesta; incluir explícitamente Concepción y dimensionar personas únicas, turnos y jornadas tras el levantamiento. No reemplazar automáticamente 120 por 180 ni tratar el supuesto como nómina confirmada.
- **Decisión necesaria:** confirmar si la población de capacitación ofertada incluye preparadores de Concepción y si el supuesto S-39 se usa provisionalmente para planificar sus turnos.

## Dependencia documental separada

### D01 — Catorce figuras con destino local no disponible

**Tipo:** falta de evidencia/archivo externo, no contradicción semántica. **Prioridad:** alta para completar la presentación. **Complejidad:** media si existen originales recuperables.

- **Evidencia:** faltan seis destinos `figuras/figura 2.1.pdf` a `figura 2.6.pdf` ([SD2:130,152,174,194,214,238][s2]) y ocho destinos `figures/` de Figuras 3.1–3.8 ([SD3:167,177,187,220,224,232,236,240][s3]). Se comprobó su ausencia sólo en este checkout, no fuera de él.
- **Impacto:** los enlaces locales no permiten abrir la evidencia gráfica que explican los documentos.
- **Solución recomendada:** identificar la ubicación existente y autorizada de las figuras vigentes, cotejar su contenido y ajustar los enlaces Markdown. No crear PDF, convertir imágenes ni retirar figuras para ocultar la dependencia. La aceptación anterior de trece PDF del SD4 no resuelve estos catorce destinos.
- **Dato necesario del equipo:** aportar las ubicaciones de los originales existentes o confirmar que aún no están disponibles.

## Asuntos que ya no quedan pendientes de esta revisión

| Grupo | Cierre documentado |
|---|---|
| Sala, obra civil y Starlink | SD6/T-9 alineados con T-14/T-15: responsabilidad del CLIENTE en separación civil, coordinación/piso de LafroX, montaje por sitio y cinco enlaces; Concepción no depende de recibir la sala de Talca. |
| Calendario agregado | Construcción de módulos E1 junio–septiembre y cierre de QA por módulo agosto–septiembre; fin de 3.4 el 30-09; 3.6 comienza mes 6. Integración/certificación de octubre preservadas. |
| Cifras, referencias y enlaces | 12,34 TPS; A.31/A.36; C-05 2.283/2.391 por período; I-04A seguimiento mes 24/meta mes 36; unidades SLA y ancla SD3 corregidas. |
| Métodos RNF | 86 filas activas revisadas, 36 métodos ajustados para comprobar el criterio, sin cambiar requisitos ni estados. Describe verificaciones previstas, no ensayos realizados. |
| Falsos positivos o diferencias explicadas | Seis indicadores anticipados, no siete; cobertura ≥70 % lógica/≥80 % global ya alineada; portal tradicional opcional; reversión técnica/operacional y denominadores de catálogo/alias/aceptación distintos. |
| RPO residual | SD4 4.3.2.4 documenta la pérdida de sitio tras caída de tres caminos; no se trata como nueva decisión ni se transforma en cumplimiento universal ([SD4:3226][s4]). |

Los cierres de CD-01 se registraron en `8463b7b` y su comprobación en `9c386e1`. Este informe no añade una lista de requisitos parcialmente cumplidos: tales brechas no equivalen por sí solas a contradicciones entre documentos.

## Siguiente paso y límites

Resolver P01 primero y luego las restantes decisiones una por vez. Este informe no autoriza cambios de alcance, cronograma, políticas de datos ni entregables. D01 requiere ubicaciones reales, no una solución ficticia. Permanecen fuera de esta revalidación las firmas/revisión humana, presentación PDF y pruebas técnicas por ejecutar.

[t14]: ../07_PlanDeTrabajo_EDT_Cronograma_Implantación/LAFROX-Formulario-T-14.md
[t15]: ../07_PlanDeTrabajo_EDT_Cronograma_Implantación/LAFROX-Formulario-T-15.md
[t12]: ../03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md
[a3]: ../03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md
[s3]: ../03_esquema_solucion_alcance/LAFROX-Subdocumento3.md
[a5]: ../05_modelo_datos/LAFROX-Subdocumento5-Anexos.md
[s4]: ../04_arquitectura/LAFROX-Subdocumento4.md
[s2]: ../02_problema_necesidad/LAFROX-Subdocumento2.md
[caso]: ../Bases/Caso_02_Logistica.md
