# Auditoría de coherencia — Presentación v10 e Informe 2

**LafroX · 20 de octubre de 2026**

## Conclusión ejecutiva

La narrativa central —capturar datos en origen para mejorar trazabilidad, servicio y costo de servir— está respaldada por el Informe 2. **No conviene presentar la v10 sin precisar aceptación, OTIF, etapas y tiempo de regresión.** Además, el informe entregado contiene diferencias reales sobre el SOC y la cobertura de pruebas que la presentación no puede resolver por sí sola.

No todo lo señalado es una contradicción numérica. Se distinguen:

- **Error o discrepancia:** una afirmación difiere de la fuente o presenta una condición incompleta como equivalente.
- **Inconsistencia entre documentos:** dos partes de lo entregado sostienen versiones distintas. Requiere acordar una versión; no elegirla silenciosamente.
- **Ambigüedad u omisión:** el dato puede ser correcto, pero sin alcance, horizonte o conciliación induce una lectura equivocada.
- **Precisión menor:** nombre, redondeo o redacción que no cambia la propuesta.

**Prioridad alta:** corregir antes de exponer. **Media:** explicar y preferiblemente corregir. **Baja:** ajuste editorial. No se modificaron el PPTX ni los documentos entregados.

## Alcance y método

- Presentación vigente: **53 posiciones**, incluyendo ampliaciones y transiciones. Se extrajeron texto y notas de las 53, y se inspeccionaron las figuras generales de arquitectura incorporadas.
- Se contrastaron los temas de las láminas con los PDF y Markdown de SD1–SD9 y SD13, sus formularios y anexos pertinentes, disponibles en la carpeta de Informe 2.
- Se extrajo texto de los PDF del informe para confirmar hallazgos decisivos, no solo de sus versiones Markdown.
- Las Bases Administrativas y Técnicas Transversales son escaneadas: se obtuvo OCR de sus 77 y 51 páginas. El art. 17.3 se comprobó además visualmente contra el PDF.
- La revisión anterior `Validacion_Presentacion_Informe2.md` corresponde a v4. Sirvió como antecedente, no como validación de v10.
- **No se encontró un PDF separado del Caso 02 Logística ni las aclaraciones originales.** Sus hechos se contrastaron con la transcripción y las referencias del Informe 2, no con un original inexistente entre los archivos suministrados.
- Esta auditoría revisa coherencia documental. No acredita pruebas ejecutadas, certificaciones externas, factibilidad real ni cumplimiento jurídico actualizado fuera de los documentos.

**Numeración:** «Pos.» es la posición real en PowerPoint; «visible» es el número impreso. La posición 17 es «Datos con una sola verdad» (visible 08); el visible 17 es Infraestructura, posición 26.

## Cambios de mayor prioridad en la presentación

### H01 · Alta · La condición 3 de aceptación quedó reducida a una condición más estrecha

**Dónde:** pos. 47, visible 37, «Calidad que bloquea».

**Presentación:** bajo «Art. 17.3 · 6 condiciones para aceptar», el punto 3 dice «Sin caída en despacho».

**Fuente:** [BA], art. 17.3, página impresa 13 / PDF página 14: exige cumplir sostenidamente **los indicadores comprometidos de disponibilidad y tiempo de respuesta**, durante el mismo período de al menos las cuatro últimas semanas. La continuidad del despacho es una exigencia adicional específica, no reemplaza todo el punto.

**Por qué importa:** se podría aceptar un sistema que no se cae durante el despacho, pero incumple latencia o disponibilidad en el período evaluado. No sería equivalente a lo requerido por el artículo.

**Redacción recomendada para el punto 3:**
> Disponibilidad y tiempos de respuesta cumplidos durante las cuatro últimas semanas.

**Precisar además al exponer:** cero incidentes **abiertos, atribuibles a la solución**, críticos o altos; volumen real **comprometido**; personal certificado según el plan; acta suscrita por la Contraparte Técnica. Las seis condiciones son conjuntas. No basta cumplir cinco.

### H02 · Alta · Se confunde la referencia OTIF con el compromiso ofertado

**Dónde:** pos. 4, visible 03, meta «>95 %»; notas actuales de esa lámina.

**Presentación:** «Hoy 82,4 % / Meta >95 %», sin horizonte.

**Fuentes:** [SD2], Tabla 2.1, efectivamente muestra «sobre 95 %» como referencia del caso. [SD3], §3.2.5, R18-04, compromete **90 % al mes 15, 93 % al mes 19 y 95 % al mes 32**; distingue expresamente esa trayectoria de la referencia del caso. [T17], §5, conserva aceptación diferenciada.

**Diagnóstico:** no es una cifra inventada, pero sí una discrepancia de origen, operador matemático y horizonte al presentarla como la meta ofertada. «>95 %» no equivale a «95 %».

**Redacción recomendada:**
> OTIF: 82,4 % inicial → 90 % m15 → 93 % m19 → 95 % m32. Referencia del caso: >95 %.

**No hacer:** prometer que H7 o H12 aceptan anticipadamente el último tramo de OTIF.

### H03 · Alta · «Solo M11 espera a Etapa 2» contradice el alcance de las interfaces y de M10

**Dónde:** notas de pos. 6, visible 05, «Mapa de módulos»; lectura conjunta con las arquitecturas de pos. 7–8.

**Presentación, nota:** «Solo el canal moderno (M11) espera a la Etapa 2». La propia lámina indica M10 «Etapa 1 y 2».

**Fuentes:** [SD3], §§3.1, 3.2 y 3.4: el portal de clientes, el intercambio electrónico y el costo de servir completan E2. M10 entrega OTIF en E1 y costo de servir en E2. La arquitectura de [SD4] declara «Portales: etapa 2» y explica que M11 habilita portales y canal moderno.

**Por qué importa:** la frase sugiere que todos los canales y toda la analítica existen en E1. Cambia lo que un usuario podría esperar en cada entrega.

**Redacción recomendada:**
> E1 incorpora el núcleo operacional y OTIF; E2 habilita portales, canal moderno/EDI y costo de servir en M10.

**Clasificación:** inconsistencia de las notas con el alcance documentado, no error de los doce códigos M1–M12.

### H04 · Alta · «4,4 h de regresión completa» excluye las pruebas manuales

**Dónde:** pos. 48, visible 38, y sus notas.

**Presentación:** «4,4 h · regresión completa, en una noche», junto a «1.316 casos / 80 % automatizados».

**Fuente confirmada:** [SD9], §9.2.3, PDF página 20. El cálculo usa unos **1.053 casos automáticos**, 30 segundos cada uno y **dos ejecutores paralelos**. Además registra **263 manuales a 15 minutos**, unas **65,8 HH por ciclo**. [T13], §8, desarrolla la automatización.

**Comprobación:**

- 1.053 × 30 s = 31.590 s ≈ 8,8 horas en un ejecutor.
- Con dos ejecutores y reparto ideal: ≈4,4 horas de reloj.
- 263 × 15 min = 3.945 min = 65,75 HH manuales.

**Diagnóstico:** el propio SD9 usa la expresión «regresión completa» para el subconjunto automático y luego separa los manuales; la presentación amplifica esa ambigüedad. Ni esas 65,8 HH se convierten automáticamente en 65,8 horas de duración —puede haber paralelismo— ni toda la batería física se termina en 4,4 horas.

**Redacción recomendada:**
> Regresión automatizada: ≈4,4 h con dos ejecutores. Manuales: ≈65,8 HH/ciclo, programadas aparte.

**Precisar:** son parámetros de planificación, no duración medida de una batería ejecutada.

### H05 · Alta · Falta conciliar el total de la EDT con el total programado

**Dónde:** pos. 20–29 frente a pos. 33, visibles 11–20 frente a 23.

**Presentación:** las nueve fases muestran 6.920, 4.320, 33.280, 20.672, 1.040, 3.840, 4.736, 129.879 y 320 HH. Después se anuncia 217.543 HH programadas.

**Comprobación:** el primer conjunto suma **205.007 HH**, no 217.543. Faltan **12.536 HH** si el oyente interpreta ambas vistas como el mismo desglose completo.

**Fuente confirmada:** [T15], §7.4.3, PDF páginas 28–29, sí contiene el puente:

| Componente | HH |
|---|---:|
| 222 paquetes de la EDT | 205.007 |
| Restauraciones previas a Operación | 128 |
| Soporte puente | 9.336 |
| Reserva protegida | 3.072 |
| **Línea base programada** | **217.543** |

**Diagnóstico:** no hay un error aritmético demostrado en el informe. Hay **dos alcances de estimación que la presentación muestra sin conciliación**.

**Redacción recomendada:**
> EDT: 205.007 HH en paquetes. Programación: 217.543 HH al incorporar restauraciones, soporte puente y capacidad protegida.

**No hacer:** cambiar alguna fase para que el total cuadre artificialmente ni sumar nuevamente la capacidad protegida como si no estuviera incluida.

## Inconsistencias del propio Informe 2 que afectan la defensa

### H06 · Alta · El alcance del 80 % de cobertura cambia entre subdocumentos

**Dónde repercute:** pos. 19 y 46, visibles 10 y 36, y cualquier explicación del pipeline.

**Presentación y SD9:** «80 % global».

**Fuente contraria:** [SD6], §6.2.2, PDF página 6: **80 % de cobertura de líneas para el código modificado**. [SD9], Tabla 9.4, PDF página 12: **80 % de cobertura unitaria global**. [SD1], §1.3.1, PDF página 11, también exige 80 % global. El 70 % de lógica de negocio aparece como obligación separada, respaldada por [BA], art. 24, y [BTT], RT-04.11.

**Por qué es una contradicción real:** el conjunto de líneas evaluadas cambia. Un cambio pequeño puede estar muy probado y aun así no cumplir cobertura global del sistema. Ambas políticas podrían coexistir, pero los documentos no explican que sean dos umbrales adicionales diferentes.

**Acción necesaria:** acordar si la política exige 80 % global, 80 % de código modificado o ambos, y alinear SD1/SD6/T-10/SD9 y notas. **No se puede inferir del requisito de las Bases que el 80 % global sea obligatorio por ellas:** el 80 % es compromiso propio según el informe.

**Mientras se resuelve, texto honesto:**
> Exigimos al menos 70 % en lógica de negocio. El alcance exacto del umbral adicional del 80 % debe uniformarse entre las metodologías y el plan de calidad.

### H07 · Alta · El SOC figura a la vez como condicional y como propio con ubicación declarada

**Dónde repercute:** defensa de capacidad, operaciones, seguridad, adquisiciones y esfuerzo; pos. 25, 33, 42 y 51.

**Versión A:** [SD6], §6.1.3, PDF página 5: SOC 24×7 **condicional a subcontratación**; RT-11.17 «cumplimiento parcial» porque la ubicación no está declarada.

**Versión B:** [T15], §7.4.1, PDF página 12: SOC **propio de LafroX**, desde su Centro de Operaciones en **Valparaíso**, con HH imputadas. [SD1] también describe NOC y SOC en Valparaíso, aunque distingue analistas contratados de la planta técnica.

**Base:** [BTT], RT-11.17, permite propio o subcontratado, pero exige declarar ubicación, dotación y procedimientos. El problema no es que la subcontratación esté prohibida: es que lo entregado no tiene una versión coherente sobre modalidad y estado de cumplimiento.

**Acción necesaria:** fijar la modalidad real, ubicación, cobertura, dotación y evidencias, y corregir las declaraciones de cumplimiento y las adquisiciones. **No asegurar oralmente que la contradicción está resuelta ni que el servicio ya está contratado.**

### H08 · Media · El SD8 contiene una tensión entre su tabla de cortes y su regla de zonas registradas

**Dónde:** pos. 44, visible 34, leyenda «Crítica ≥0,40 / Alta ≥0,20 / Media ≥0,08» y notas.

**Una parte de la fuente sí respalda los cortes:** [SD8], escala de exposición, PDF página 8, publica esos intervalos.

**Pero la misma fuente lo matiza en sentido contrario:** inmediatamente después afirma que la zona se adopta del registro vigente y **«no se infiere a partir de umbrales sobre la exposición decimal»**; repite esa cautela en el análisis cualitativo, PDF página 12.

**Diagnóstico preciso:** no sería correcto acusar a la presentación de inventar los umbrales. La presentación toma una tabla existente, pero su nota explica el color como consecuencia automática de esos cortes y omite la regla textual contraria. **La inconsistencia está también dentro del SD8.**

**Redacción segura mientras se unifica:**
> Matriz por ponderaciones cualitativas; colores según zona adoptada del registro vigente.

**Acción:** acordar si los intervalos son una regla automática o solo una descripción de las zonas del registro y reescribir el SD8 sin las dos afirmaciones incompatibles. No reclasificar riesgos silenciosamente.

### H09 · Media · El calendario de riesgos se presenta con más certeza que la reconocida por el SD8

**Dónde:** pos. 31–32, visibles 22, y sus notas: riesgos por mes y «se concentran en el mes 11».

**Qué sí está respaldado:** [SD8-A], Anexo 8.B, tabla cuantitativa, contiene columna **Mes estimado**: por ejemplo, R-001 en m2, R-015 en m11 y R-012 en m12. Mostrar esas marcas como estimaciones es consistente con esa tabla.

**Cautela omitida:** [SD8], §8.3.2, PDF página 15, afirma que las asignaciones por mes y perfil y su encaje con el T-15 siguen pendientes de evidencia actualizada; advierte que los análisis de codificación anterior no tienen un crosswalk verificable hacia el registro vigente. [T15], PDF páginas 6 y 38, también conserva escenarios históricos sujetos a recálculo.

**Diagnóstico:** una marca de «mes estimado» no demuestra consumo de contingencia, concentración cuantificada de HH ni capacidad programada para responder. Tampoco prueba que el riesgo ocurra en ese mes.

**Redacción recomendada:**
> Meses estimados del Anexo 8.B; asignación de contingencia por perfil y encaje con la línea base pendientes de validación.

## Ambigüedades técnicas y de alcance

### H10 · Media · «Pallet o canastillo con su lote» simplifica en exceso el modelo

**Dónde:** pos. 17, visible 08.

**Presentación:** una unidad parece tener un único lote y se ejemplifica con canastillo.

**Fuente:** [SD5], §5.1.4 y Figura 5.2, separa unidad logística de contenido. [SD5-A], diccionario y reglas 5-C, tipifica la unidad como **PALLET, CAJA o CONTENEDOR**. El contenido relaciona productos, lotes y cantidades. El control de envases retornables es otro aspecto del modelo.

**Diagnóstico:** no implica que un canastillo jamás pueda funcionar físicamente como contenedor; lo no respaldado es presentarlo sin mapeo como el tipo explícito del diccionario o sugerir siempre relación uno a uno unidad–lote.

**Redacción recomendada:**
> Unidad logística y contenido por producto, lote y cantidad.

**Para explicar:** un lote es identidad sanitaria; una unidad logística agrupa contenido. No son el mismo objeto.

### H11 · Media · «Trazable de punta a punta, aun sin señal» no significa visibilidad central inmediata

**Dónde:** notas del cierre, pos. 53, y lectura de pos. 5 y 17.

**Fuente:** [SD5], §§5.2.1–5.2.3, separa confirmación local de consolidación central. La sincronización móvil es ≤10 minutos al recuperar enlace y la consolidación del sitio ≤2 horas después de recuperarlo.

**Riesgo:** interpretar que la nube conoce inmediatamente una entrega que permanece en un terminal sin cobertura. El informe niega esa equivalencia.

**Redacción recomendada:**
> Registro y evidencia local durante el corte; trazabilidad central completada al reconectar y conciliar.

**Relacionado:** «retiro en <2 h» se refiere a identificar clientes afectados, no a recoger físicamente toda la mercadería en dos horas. El ensayo debe demostrarlo; el diseño por sí solo no es evidencia de aceptación.

### H12 · Media · La disponibilidad de infraestructura quedó fuera del resumen de fiabilidad

**Dónde:** pos. 46, visible 36, «Fiabilidad ≥99,9 % · RTO ≤4 h · RPO ≤15 min».

**Fuente:** [SD9], Tabla 9.3, PDF página 10, y [BTT], §7.2: **99,9 % para la transacción crítica de extremo a extremo** y **99,95 % para los componentes de infraestructura enumerados**. [BA], art. 21/78, distingue servicio crítico de infraestructura.

**Diagnóstico:** el 99,9 % no es falso. Falta especificar el objeto medido y el umbral adicional. RTO y RPO tampoco son promesas universales para cualquier objeto o incidente sin considerar escenarios y riesgo residual.

**Redacción recomendada:**
> Transacción crítica ≥99,9 %; infraestructura ≥99,95 %; RTO/RPO según escenarios comprometidos.

**No es contradicción:** exigir cero minutos de caída entre 05:30 y 07:00 junto con un porcentaje mensual. Son restricciones simultáneas sobre ventanas distintas.

### H13 · Media · Un paso de DevSecOps omite «críticas» aunque la lámina de calidad sí lo exige

**Dónde:** pos. 19, visible 10: G3 «sin vulnerabilidades altas»; pos. 47, visible 37: G3 «sin vulnerabilidades críticas o altas».

**Fuente:** [SD9], estrategia de aseguramiento y Anexo 9.B; [BTT], RT-04.05, rechaza críticos y altos no corregidos conforme al control aplicable.

**Diagnóstico:** puede ser abreviación de lenguaje, pero deja dos reglas impresas con distinto alcance. En una defensa, «altas» como categoría no incluye automáticamente «críticas».

**Redacción recomendada en ambas:**
> Sin vulnerabilidades críticas ni altas abiertas.

### H14 · Media · Operación por fase de EDT no equivale a Operación por bloque contractual

**Dónde:** pos. 20 y 28 frente al bloque de pos. 30 y a la curva de pos. 33.

**Datos:** fase 8 de EDT = **129.879 HH**; bloque de Operación m21–56 = **128.853,67 HH** según [T15], Tabla 7.4, PDF página 28.

**Diagnóstico:** diferencia de **1.025,33 HH**, que no basta para declarar error: la fuente explica que los cierres, estabilización y tareas continuadas se imputan por alcance y período. Hay paquetes que no coinciden exactamente con el bloque temporal. La presentación debe advertir la diferencia de clasificación.

**Redacción recomendada:**
> Fase 8 EDT: 129.879 HH. Bloque temporal de Operación m21–56: 128.853,67 HH. Vistas diferentes según T-15.

**No hacer:** restar o agregar esas 1.025,33 HH a la línea base sin reconstruir las imputaciones.

### H15 · Media · «Costo de la calidad: 11.136 HH» no es el costo integral de calidad

**Dónde:** pos. 49, visible 39. Las notas son más precisas que el rótulo.

**Fuente:** [SD9], §9.1.6, Tabla 9.6: **conformidad programada** de 11.136 HH = prevención 4.224 + evaluación 6.912. Los escenarios de fallas internas y externas se tratan separadamente; no son frecuencia prevista ni reserva garantizada.

**Diagnóstico:** la cifra y el 5,1 % son correctos. El título puede hacer creer que incluye cualquier reproceso, defecto o falla de operación.

**Redacción recomendada:**
> Conformidad programada: 11.136 HH, 5,1 % de la línea base.

**Comprobación:** 11.136 / 217.543 ≈5,12 %; prevención ≈37,9 %, evaluación ≈62,1 %.

## Precisiones menores que conviene incorporar

### P01 · Baja · Nombre incompleto del estándar de pruebas

**Dónde:** pos. 45, visible 35: «ISO/IEC 29119».

**Corregir a:** **ISO/IEC/IEEE 29119**, como [SD9], Tabla 9.2, y [BA], referencias de pruebas. Es un ajuste de denominación, no cambia los niveles de proceso.

### P02 · Baja · La contingencia se redondea con distinta precisión

**Dónde:** pos. 35–42 muestra 2.058,5 HH; pos. 43 y notas, 2.058 HH.

**Fuente:** [SD8], contingencia adoptada **2.058,480 HH**. Son redondeos compatibles, pero innecesariamente distintos.

**Sugerencia:** usar **2.058,48 HH** de forma uniforme. Mantener separadas las 1.600 HH de gestión y las 3.072 HH protegidas ya incluidas en T-15. El valor esperado no es suma cierta de trabajo que necesariamente ocurrirá.

### P03 · Media · La mitad de las horas se refiere al subtotal RUP, no al contrato

**Dónde:** notas pos. 19: «la construcción concentra la mitad de las horas».

**Cálculo:** 33.280 / 65.192 ≈51,1 % de Inicio+Elaboración+Construcción+Transición; 33.280 / 217.543 ≈15,3 % de la programación completa.

**Sugerencia:** «Construcción concentra aproximadamente la mitad del subtotal de las cuatro fases RUP». La lámina ya ofrece el contexto; precisarlo evita una lectura global falsa.

### P04 · Media · Los indicadores de innovación pierden horizonte o población al resumirse

**Dónde:** pos. 50, visible 40.

**Fuente:** [SD13], indicadores de cada innovación.

| Rótulo resumido | Precisión necesaria |
|---|---|
| −25 % de vencido | Reducción relativa de vencimiento posentrega; I-01B, contraste al mes 28, con base de rutas de control. No equivale a toda la merma de bodega. |
| −30 % horas de diagnóstico | Reducción de la **mediana**, con al menos veinte pares comparables; I-02A. |
| ±15 % en ≥80 % de los lotes | Comparación con evaluación de Calidad, error referido a vida nominal, al menos sesenta lotes por familia; I-03B. No extiende automáticamente el vencimiento legal. |
| ≥5 % menos costo, OTIF ≥95 % | Meta I-04A del mes 36; canasta comparable y correcciones de mezcla/estacionalidad. La regla de pago previa protege el tramo OTIF vigente para cada mes. |
| TRL 2 → 4 → 6 | Ruta de maduración de la propuesta integrada. No prueba que las cinco lleguen a TRL6 en el mismo mes: INN-04, por ejemplo, lo ubica al 23. |

**Sugerencia:** no sobrecargar la lámina; incorporar estas distinciones en el guion y responder con el indicador específico.

### P05 · Media · Congelamiento de septiembre y ventanas nocturnas requieren alcance explícito

**Dónde:** notas pos. 18 y 31–32: «nada se despliega en septiembre»; notas pos. 17: migración 22:00–06:00.

**Fuente:** [SD5], §5.3.4, excluye **1–25 de septiembre**, **1–31 de diciembre** y los **tres primeros días hábiles** del cierre mensual; permite ventana nocturna condicionada a proteger despacho **05:30–07:00** y conservar reversión. Otros resúmenes del informe usan «septiembre y diciembre» sin detallar fechas.

**Diagnóstico:** bloquear septiembre completo es una política más restrictiva, no prueba por sí misma incumplimiento. Debe acordarse si es una decisión propia o una abreviación. La ventana 22:00–06:00 se superpone treinta minutos con el despacho protegido: la fuente advierte la restricción, por lo que no se puede prometer indisponibilidad hasta las 06:00.

**Redacción recomendada:**
> Despliegues fuera de los congelamientos y del cierre mensual; cada corte y reversión protege el despacho 05:30–07:00.

### P06 · Baja · Baseline, referencia y compromiso están mezclados en «HOY/META»

**Dónde:** pos. 4.

El retiro es un incidente de marzo de 2026; varios indicadores son datos base de 2025; la meta de merma es propia de LafroX. «Hoy» no significa que todos fueron medidos el 20 de octubre de 2026. «Diferencias de rendición $4,2 M/mes → mismo día» cambia además de magnitud: de importe mensual a tiempo de resolución.

**Sugerencia:** usar «Línea base del caso» y «Resultado/compromiso», e indicar para rendición: «100 % de diferencias explicadas el mismo día», según el requisito y su criterio preciso. No inventar que ya desaparecieron los $4,2 millones.

### P07 · Baja · GS1/EDI aparece dentro del bloque «Leyes»

**Dónde:** pos. 45.

GS1 y EDI son estándares y mecanismos de identificación/intercambio, no leyes. Se pueden mantener en la misma diapositiva, pero cambiar el encabezado a «Exigencias normativas y de interoperabilidad» o separar esa fila. El guion no valida legislación externa: reproduce su tratamiento en el Informe 2.

### P08 · Baja · Números de diapositiva duplicados y posiciones diferentes

Las ampliaciones 06.1–06.8 desplazan las posiciones; el número visible 22 aparece en dos Gantt y el 42 en transición y cierre. No es una contradicción técnica, pero ya impidió identificar inequívocamente la «17».

**Sugerencia:** al coordinar el ensayo decir «posición 26, visible 17, Infraestructura» o renumerar todas las posiciones si se quiere navegación inequívoca. No es necesario eliminar las transiciones si tienen una función de presentación.

## Aspectos revisados que no deben denunciarse como contradicciones

1. **9 días, 4.800 kg, seis meses y 6 %:** coinciden con SD2. La restricción del 41 % al producto del retiro también está bien indicada en la v10.
2. **16 GB de origen frente a 32 GB de destino:** no se contradicen. [SD5], Tabla 5.2, separa 16,05478 GB fuente de 32,10956 GB estimados en destino. El alcance aún depende del perfilado; no son 32 GB necesariamente transferidos por red.
3. **Cero diferencias sin explicar:** no significa igualdad ciega de todos los saldos ni cero registros aislados. Exige tratamiento y aprobación de diferencias conforme al criterio aplicable.
4. **Catorce horas móviles, veinticuatro horas de sitio, manifiesto de 26 horas y credencial de bodega de ocho horas:** corresponden a objetos diferentes; no son cuatro versiones del mismo plazo. Los relevos autorizados son parte del diseño.
5. **99,9 % mensual y cero caída en despacho:** son requisitos simultáneos, no porcentajes incompatibles.
6. **Ocho líderes y 69 personas equivalentes:** el primer dato describe gobierno, el segundo demanda de ejecución. Tampoco equivale a 69 personas acreditadas y disponibles.
7. **Siete interfaces, doce módulos y quince dominios:** cuentan elementos distintos; no deben igualarse. Las quince integraciones del plan de pruebas tampoco son las siete interfaces de usuario.
8. **Dos zonas principales y una región de recuperación:** son mecanismos complementarios. No confundir zona con región.
9. **Riesgo con ponderación 0,50 y probabilidad inicial 35 %:** no es necesariamente error. El SD8 separa la escala cualitativa de la probabilidad usada en el valor esperado. La tabla de riesgos debería titularlas con claridad.
10. **Sin hardware nuevo en innovaciones:** no niega la compra e instalación de equipos en el proyecto. Significa que esas innovaciones reutilizan la infraestructura prevista.
11. **ISO/IEC 25010 con ocho características:** corresponde al marco contractual expresado por las Bases y el informe; no se ha sustituido arbitrariamente por otra edición.
12. **$4,2 millones del diagnóstico:** es una pérdida/diferencia histórica del caso, no un precio de la oferta. El art. 50.2 prohíbe precios/tarifas o cifras que permitan inferir el monto ofertado; no se declara infracción solo por mostrar este antecedente.

## Preguntas difíciles y respuestas defendibles

**«¿Las nueve fases suman 217.543 horas?»**
> No. Los 222 paquetes suman 205.007; la programación incorpora 128 HH de restauraciones previas, 9.336 de soporte puente y 3.072 de capacidad protegida. Así llega a 217.543 sin cambiar el desglose base.

**«¿Se aceptan los dieciséis resultados al llegar a H12?»**
> No todos definitivamente. El T-17 diferencia doce resultados en H7 y dos en H12; OTIF se confirma por tramos hasta el mes 32 y envases necesita doce meses de medición para la aceptación final.

**«¿Cómo puede haber una sola verdad si hay varias bases?»**
> Porque se define autoridad por agregado y se controla la publicación de eventos. Varias copias pueden existir, pero no se permite que todas modifiquen libremente el mismo saldo; la copia central puede atrasarse durante un corte.

**«¿El algoritmo térmico decide que se puede vender un alimento?»**
> No. Relaciona historia y estimación para apoyar una decisión. Calidad conserva la autoridad y se deben cumplir los criterios sanitarios; no se inventan lecturas ni se modifica automáticamente el vencimiento nominal.

**«¿Están demostradas las 4,4 horas?»**
> No son una medición de ejecución: son una estimación para el subconjunto automático con dos ejecutores y parámetros declarados. La prueba manual se programa aparte.

**«¿La reserva de 2.058,48 HH garantiza que cualquier riesgo cabe?»**
> No. Es valor esperado agregado de riesgos identificados. Su distribución por perfil y calendario y su conciliación con T-15 requieren validación; la reserva de gestión tiene otra finalidad y autorización.

**«¿El SOC es propio o subcontratado?»**
> El informe entregado contiene ambas descripciones. Hay que fijar y documentar la modalidad, ubicación y dotación antes de sostener cumplimiento completo; no sería honesto negar la discrepancia.

## Orden recomendado para corregir, sin reescribir toda la presentación

1. Pos. 47: restituir disponibilidad **y** tiempos de respuesta en la condición 3.
2. Pos. 4: distinguir referencia OTIF de compromiso e hitos.
3. Nota pos. 6: corregir el alcance de E2; pos. 48: acotar las 4,4 horas a automatización.
4. Pos. 20/33: añadir el puente de 12.536 HH; pos. 28: aclarar fase EDT frente a bloque temporal.
5. Acordar versiones únicas de cobertura y SOC en los documentos entregados; no solo en el guion.
6. Homologar G3, unidad logística, conformidad programada y disponibilidad por objeto.
7. Aclarar zonas de riesgos, reservas y calendario estimado sin convertirlos en hechos acreditados.
8. Ajustar denominaciones y numeración. Ensayar con el guion explicado, sin leer todos los detalles de las ampliaciones.

## Fuentes principales y localización verificable

Las páginas de esta sección son páginas del PDF; el art. 17.3 está en página PDF 14, rotulada 13 en el documento. Las secciones permiten localizar también las versiones Markdown acompañantes.

| Clave | Documento local | Puntos usados |
|---|---|---|
| Presentación | [v10](<C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Bases PTE/Principal/LafroX/Presentaciones/LafroX - Presentación Informe 2 v10.pptx>) | Texto y notas de 53 posiciones; arquitectura incorporada. |
| SD1 | [Presentación de la empresa](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 1/LAFROX-Subdocumento1.pdf>) | SOC, dotación y Tabla 1.6. |
| SD2 | [Comprensión del problema](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 2/LAFROX-Subdocumento2.pdf>) | Tabla 2.1, origen de líneas base y metas; límites del 41 %. |
| SD3 | [Alcance](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 3/LAFROX-Subdocumento3.pdf>) | §3.2.5 R18-04; portales y M10 por etapa. |
| SD4 | [Arquitectura](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 4/LAFROX-Subdocumento4.pdf>) | Ocho capas, portales E2, cómputo local y nube. |
| SD5 | [Datos](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 5/LAFROX-Subdocumento5.pdf>) | §§5.1.4, 5.2.1–5.2.3 y 5.3; Tabla 5.2, PDF35. |
| SD5-A | [Anexos de datos](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 5/LAFROX-Subdocumento5-Anexos.pdf>) | Diccionario y dominio de `inv_unidad_logistica.tipo`; contenido. |
| SD6 | [Metodologías](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 6/LAFROX-Subdocumento6.pdf>) | SOC en PDF5; 80 % código modificado en PDF6. |
| T14 | [EDT](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 7/LafroX-Formulario-T-14.pdf>) | Nueve fases; infraestructura §7.2.6. |
| T15 | [Recursos](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 7/LafroX-Formulario-T-15.pdf>) | SOC PDF12; paquetes y total PDF28–29; cautelas de red y reservas PDF6/38. |
| T18 | [Implantación](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 7/LafroX-Formulario-T-18.pdf>) | Olas, acompañamiento y condiciones operacionales. |
| SD8 | [Riesgos](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 8/LafroX-Subdocumento8.pdf>) | Contingencia PDF5/13/15; cortes y zonas PDF8/12. |
| SD8-A | [Anexos de riesgos](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 8/LafroX-Subdocumento-8-Anexos.pdf>) | Fichas 8.A y tabla 8.B, probabilidades y mes estimado. |
| T16 | [Registro de riesgos](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 8/Lafrox-Formulario-T-16.pdf>) | Clasificaciones y códigos R-001–R-045. |
| SD9 | [Calidad](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 9/LAFROX-Subdocumento9.pdf>) | Umbrales PDF10/12; regresión PDF20; conformidad §9.1.6. |
| T13 | [Pruebas](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 9/LAFROX-Formulario-T-13.pdf>) | §8, catálogo y automatización. |
| T17 | [Aceptación](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 9/LAFROX-Formulario-T-17.pdf>) | §5, resultados con aceptación diferenciada. |
| SD13 | [Innovaciones](<C:/Users/henri/Downloads/Informe_2_LafroX/Informe_2_LafroX/Subdocumento 13/LAFROX-Subdocumento13.pdf>) | I-01B, I-02A, I-03B, I-04A; TRL de INN-04. |
| BA | [Bases Administrativas](<C:/Users/henri/Downloads/Bases Caso/Bases Administrativas.pdf>) | Arts. 17.2–17.3, 18, 24 y 50.2. |
| BTT | [Bases Técnicas Transversales](<C:/Users/henri/Downloads/Bases Caso/Bases Técnicas Transversales.pdf>) | §7.2, RT-04.11 y RT-11.17. |

## Key Learnings:

1. Una cifra puede ser correcta en su fuente y volverse engañosa al perder su población, horizonte o alcance.
2. Las diferencias del SOC y del 80 % de cobertura existen dentro del Informe 2: no se arreglan únicamente cambiando una diapositiva.
3. La aceptación contractual exige evidencia conjunta; completar el cronograma o el pipeline no sustituye las condiciones del art. 17.3.
