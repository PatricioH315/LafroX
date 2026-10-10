# Revisión de consistencia documental y complejidad de corrección

**Rama revisada:** `rama-md`  
**Alcance:** documentos de propuesta, subdocumentos, formularios, anexos y resúmenes Markdown. Se excluyó completamente `Requerimientos/` y no se usó como evidencia.  
**Criterio:** complejidad estima el esfuerzo/coordinación para resolver, no la gravedad del incumplimiento.

## Estado vigente — 10 de octubre de 2026

Se revalidó el registro inicial contra los documentos actuales, las Bases y las decisiones del contexto. La tabla siguiente gobierna el seguimiento; las secciones posteriores conservan la fotografía inicial y no deben leerse como lista vigente de defectos. Se aplicaron únicamente correcciones documentales respaldadas, sin cambiar estados de cumplimiento, fechas de aceptación, HH ni requisitos. La comprobación estructural del escritor no sustituye la revisión independiente ni la revisión humana del equipo.

| Tema del registro inicial | Estado vigente | Evidencia o límite |
|---|---|---|
| Sala: secuencia, responsabilidad civil e instalación por sitio | Corregido | SD6 6.1.3, T-9 sección 4 y Anexo 6.B distinguen sistemas mes 3, recepción mes 4, racks meses 4–5, Concepción mes 4, borde CD mes 5 y gabinetes cross-docking mes 9. Obra civil CLIENTE; LafroX especifica/coordina y provee piso técnico, conforme a BTT RT-06.06 y decisiones anteriores. |
| Starlink: tres frente a cinco sitios | Corregido | T-9 y Anexo 6.B incluyen Talca, Concepción y tres plataformas, como T-14 5.3.3. |
| Equivalencia meses 5–8 y fin de módulos 3.4 | Corregido | Junio–septiembre de 2027; agregado T-15 5.1 termina 30-09-2027, máximo de sus hijos en Tabla 6.1. No se modificaron fechas de hijos. |
| Inicio agregado de integraciones 3.6 | Corregido | Gantt T-14 inicia julio de 2027, mes 6; T-15 3.6.2–3.6.4 comienza 01-07-2027. |
| Throughput normal y referencias de capacidad | Corregido | SD5 y protocolo usan 12,34 TPS = 2,71 + 9,63 del perfil SD4 A.31; crecimiento de capacidad remite a A.36, no A.34. |
| Disparador C-05 | Corregido | 2.283 contactos/mes en meses 21–24; 2.391 desde mes 25, conforme a R8-22 y T-16. |
| Ancla del resumen SD3 y unidades SLA | Corregido | Enlace a 3.4.2 Vista general de la solución; objetivos 99,95 % y 99,9 % con unidad explícita. |
| Primera medición I-04A | Corregido | Seguimiento mensual desde mes 24; evaluación de meta mes 36, conforme a SD13 13.4.6 y T-19. |
| Seis frente a siete indicadores anticipados | Hallazgo inicial descartado | Tabla 13.C.1 contiene exactamente seis filas «Sí»; I-03C, mes 16, dice «No». Se mantiene seis. |
| Métodos de verificación RNF | Corrección documental aplicada | Se revisaron las 86 filas activas con método en 3.B y se ajustaron 36 para medir el criterio real: latencia, TLS/EDR, disponibilidad mensual, DR, atención, materiales y capacitación, entre otros. Sólo cambia la columna de método; las pruebas siguen pendientes de ejecución. Catálogos originales y colección complementaria se conservan. |
| Universo de cobertura 80 % | Ya alineado antes de esta intervención | SD4 4.2.4.1 y T-10 compuertas exigen lógica de negocio ≥70 % y cobertura unitaria global ≥80 %. No persiste «sólo código modificado». |
| Descripción de las columnas T-12 | Ya alineada antes de esta intervención | SD3 3.2 y Anexo 3.J describen cinco columnas; prueba en SD9 Anexo 9.C y criterio en T-17. |
| Portal opcional para canal tradicional | No se acredita contradicción por canal | SD3 3.4.2 y Tabla 3.A.12a lo ofrecen opcional en E2; SD4 4.1.1 diferencia activación asistida tradicional y autorregistro moderno. Caso, restricción 5, impide exigir conexión/cuenta, no ofrecer portal. No se amplió alcance. |
| Acuse comercial y MDN técnico | Cumplimiento parcial pendiente, no contradicción directa de estados | RF-12.13 compromete acuse/POD; RNF-12.03 añade plazo de 30 min y aviso vinculado. T-12 mantiene RNF-12.03 parcial por falta de evidencia de esas condiciones; MDN técnico no las demuestra. No se declaró completo. |
| Reversión técnica y recuperación operacional | Sin contradicción | Objetivos distintos: 10 min técnicos y 40 min operacionales; se conservan. |
| Conteos de requisitos y aceptación | Conciliados, con denominadores distintos | Catálogo 261 = 175 RF + 86 RNF; ofertados 259, con 84 RNF. T-12 A tiene 271 filas incluyendo alias/absorbidos. Doce aceptados E1 y catorce con verificaciones están explicados en SD7. Resumen de Anexo 3.B corregido a catálogo/oferta. |
| RPO y pérdida de sitio tras caída de tres enlaces | Excepción residual ya documentada; no cumplimiento universal | SD4 4.3.2.4 y R8-05 explican el escenario; la decisión anterior está en el contexto. Mantener este límite en la lectura de continuidad, sin convertir aceptación del riesgo en garantía técnica. |
| Innovaciones comprometidas para H4 | Requiere decisión | T-14 3.10.1.2/3.10.1.3/3.10.3.3 exigen productos en H4; T-15 los termina el 19-11-2027, después de la entrega 20-10. Resolver compromiso o programación conjunta. |
| H12, acta y paquetes dependientes | Requiere decisión | T-15 4.1 supone firma 05-10-2028; 4.3.3 termina 19-10 y 9.1.2 termina 10-10 pese a requerirse posterior a H12. No se alteraron fechas. |
| HH de estabilización entre meses 21/22 | Pendiente de fecha H12 y recálculo | El supuesto reparte 2.361,33/102,67 HH; la curva no distribuye el segundo importe. No corregir curva aislada ni acortar cuatro semanas. |
| Cobranza de preventistas RF-07.10/07.11 | Requiere decisión | T-12 conserva Cumple/No cumple para funciones solapadas. Resolver alias o exclusión efectiva antes de afectar conciliación y SD9. |
| Sincronización en cámara de frío | Requiere confirmar compromiso | RNF-09.04 conserva conectividad recuperada dentro; solución/T-12 sincronizan al salir. Caso 10, restricción 7, exige operar sin señal interior; no impone reconexión interior. No se retiró un eventual compromiso adicional sin consultar. |
| Copia regional de registros térmicos | Requiere identificar conjuntos y destino | SD5 5-D limita réplica de tel_archivo_termino; SD4 4.3.2 describe copia térmica/analítica en us-east-1. No asumir que son conjuntos diferentes ni ampliar réplica. |
| Población de capacitación | Requiere confirmar alcance de Concepción | 120 preparadores de Talca están documentados; 60 simultáneos en Concepción son supuesto S-39, no nómina adicional acreditada. No convertir automáticamente a 180 personas únicas. |
| Catorce PDF locales sin destino | Dependencia externa pendiente | Seis destinos de SD2 y ocho de SD3 siguen ausentes localmente. No se crearon PDF ni se retiraron figuras. La aceptación anterior de trece PDF del SD4 no resuelve estos destinos. |

**Comprobaciones y pendientes:** lectura cruzada de fuentes, métodos y resúmenes; comprobación aritmética y de extremos agregados; control de cambios exclusivamente Markdown. Firmas/revisión humana, figuras ausentes, presentación PDF y ensayos siguen pendientes. El registro de comandos y la revisión independiente se conserva en `odd/tasks/consistencia-documental.md`; no se afirma aceptación del CLIENTE ni aprobación nativa.

## 1. Registro inicial — contradicciones e inconsistencias reportadas

| Prioridad | Tema | Evidencia | Resolución necesaria |
|---|---|---|---|
| Alta | Cronograma de habilitación de sala | T-9 `06_metodologías/LAFROX-Formulario-T-9.md:84` y Anexo SD6 `06_metodologías/LAFROX-Subdocumento6-Anexos.md:51` sitúan los paquetes 6.1.1–6.1.4 en meses 5–6. T-14 `07_PlanDeTrabajo_EDT_Cronograma_Implantación/LAFROX-Formulario-T-14.md:1485–1489` los programa en mes 3 y recepción de sala en mes 4. | Alinear fechas y dependencias; la versión T-9/Anexo SD6 sitúa trabajos después de la recepción prevista. |
| Alta | Responsabilidad por obra civil | T-9 `:84` y Anexo SD6 `:51` atribuyen la obra civil a LafroX. T-14 `:1485` asigna al CLIENTE la obra civil de separación; LafroX especifica y coordina y provee el piso técnico. | Separar claramente obra civil, coordinación/especificación y suministro de piso técnico. |
| Alta | Instalación frente a montaje por sitio | SD6 `:48`, T-9 `:83` y Anexo SD6 `:50` describen instalación en mes 3. T-14 `:1899` programa racks meses 4–5, gabinete de Concepción mes 4, borde de CD en servicio mes 5 y gabinetes cross-docking mes 9. | Aclarar qué equipos cubre “instalación en mes 3” y cómo se relaciona con montaje y puesta en marcha por sitio. |
| Alta | Paquetes de innovación comprometidos para H4 terminan después del hito | T-14 `07_PlanDeTrabajo_EDT_Cronograma_Implantación/LAFROX-Formulario-T-14.md:1311–1320` requiere productos de INN-01/INN-03 para H4. T-15 `LAFROX-Formulario-T-15.md:667–668,676` termina paquetes asociados el 19-11-2027; H4 se entrega el 20-10 y su límite es 16-11 (`:495`). | Alinear aceptación y fechas de paquetes con H4 y su plazo de revisión. |
| Alta | H12, acta final y paquetes dependientes | T-15 `:86` supone H12 firmado el 05-10-2028; programa el acta final del 11 al 19-10 (`:686`) y paquete dependiente que termina el 10-10 (`:732`). T-14 `:1761` indica que ese paquete ocurre después de H12. | Reconciliar fecha de firma, acta y dependencias de cierre. |
| Alta | HH mensuales de estabilización | T-15 `:86` reparte 4.3.2 entre 2.361,33 HH en mes 21 y 102,67 en mes 22. La curva mensual concentra el cierre/estabilización en el mes 21 y muestra 0 HH en mes 22 (`:379–380`). | Hacer concordar supuesto y curva mensual. |
| Media | Equivalencia de meses para módulos E1 | T-15 `:87,474` identifica meses 5–8 como junio–octubre; con mes 1 en febrero de 2027, esos meses son junio–septiembre. SD8 `08_plan_riesgos/LAFROX-Subdocumento8.md:154` repite la equivalencia. | Corregir los meses o justificar otro calendario. |
| Media | Inicio de integraciones externas en la Gantt | T-14 `:1860` inicia la cuenta 3.6 en agosto de 2027 (mes 7). T-15 `:198,641–643` inicia paquetes 3.6.2–3.6.4 el 1 de julio (mes 6). | Alinear agregado Gantt y paquetes detallados. |
| Media | Fin agregado de módulos 3.4 anterior a paquetes hijos | T-15 `:460` da fin al grupo 3.4 el 27-09-2027; paquetes hijos terminan 28–30 de septiembre (`:628,633–634`). | Extender el fin del agregado o corregir fechas de los hijos. |
| Media | Disparador C-05 no refleja ambos umbrales R8-22 | C-05 SD8-Anexos `08_plan_riesgos/LAFROX-Subdocumento8-Anexos.md:810` dispara refuerzo sobre 2.391 contactos/mes. R8-22 distingue 2.283 hasta mes 24 y 2.391 desde mes 25 (`:433,439`); E8-07 `:1045` y T-16 `LAFROX-Formulario-T-16.md:28` también. | Actualizar C-05 para respetar ambos umbrales por período. |
| Media | Cobranza por preventistas cubierta y excluida | T-12 `03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md:87` marca RF-07.10 «Cumple» para cobranza presencial y asigna M3/M7. La fila siguiente marca RF-07.11 «No cumple» y dice que M7 se limita al reparto (`:88`). Anexo SD3 `LAFROX-Subdocumento3-Anexos.md:92,230` describe RF-07.10 y excluye RF-07.11 como función independiente. | Definir el límite funcional y alinear descripción, alcance y estado de cumplimiento. |
| Media | Acuse comercial de 30 minutos | T-12 marca RF-12.13 «Cumple» (`:129`), mientras RNF-12.03 declara que falta el acuse comercial dentro de 30 minutos y el aviso de despacho asociado (`:221`). | Reconciliar ambas respuestas y distinguir MDN técnico de acuse comercial. |
| Media | Sincronización dentro de cámara de frío | Anexo SD3 `03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md:282` exige recuperar conectividad y sincronizar dentro de la cámara. SD3 `:203` y T-12 `:213` dicen que sincroniza al salir de ella. | Confirmar el comportamiento comprometido y alinear solución y criterio. |
| Media | Portal para clientes tradicionales | Anexo SD3 `:626` atribuye pedido y consultas por portal al cliente tradicional. Otras filas reservan funciones y precondiciones al canal moderno (`:131–146`); SD3 cuerpo `LAFROX-Subdocumento3.md:230` llama opcional al portal tradicional en E2. | Definir funciones, canal y precondiciones de acceso. |
| Media | Throughput normal distinto | SD4-Anexos `04_arquitectura/LAFROX-Subdocumento4-Anexos.md:1371,1393` declara 12,34 TPS; SD5 `05_modelo_datos/LAFROX-Subdocumento5.md:515` y su Anexo `:1607` usan 12,30 TPS. | Fijar línea base para dimensionamiento y pruebas. |
| Media | Referencia equivocada a tabla de capacidad | SD5 `:520,527` remite a Tabla A.34 para cifras 3,15/8,05 TPS. En SD4, A.34 es requerimiento por VM (`04_arquitectura/LAFROX-Subdocumento4-Anexos.md:1543`); el plan de capacidad está en A.36 (`:1609–1613`). | Corregir la referencia cruzada. |
| Media | Universo de medición de cobertura del 80 % | SD4 `04_arquitectura/LAFROX-Subdocumento4.md:2230` formula la compuerta sobre la versión; T-10 `06_metodologías/LAFROX-Formulario-T-10.md:70,73` la limita al código modificado. | Aclarar si el umbral aplica a toda la versión o solo a líneas modificadas. |
| Media | Método de prueba no demuestra siempre el requisito | Anexo SD3 `03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md:307,313,330,347` asocia pruebas de seguridad, RTO/RPO, recuperación o disponibilidad mensual con propiedades diferentes. | Revisar la trazabilidad requisito–criterio–método de verificación. |

## 2. Registro inicial — diferencias, ambigüedades y referencias

| Tema | Evidencia | Estado / aclaración sugerida |
|---|---|---|
| Catorce figuras PDF sin destino local | SD2 `02_problema_necesidad/LAFROX-Subdocumento2.md:130,152,174,194,214,238` enlaza seis PDFs en `figuras/`. SD3 `03_esquema_solucion_alcance/LAFROX-Subdocumento3.md:167,177,187,220,224,232,236,240` enlaza ocho en `figures/`. Los destinos no están en el checkout inspeccionado. | Son enlaces locales sin archivo en esta rama; no prueba que los PDFs no existan fuera de ella. Verificar ubicación prevista o incluir los archivos. |
| Ancla del resumen SD3 | `Resumen/LAFROX-Subdocumento3-Resumen.md:17` usa `#3421-actores-del-sistema-y-relación-con-los-actores-del-negocio`; SD3 tiene el encabezado «3.4.2 Vista general de la solución» (`:216`). | Corregir ancla o destino tras confirmar encabezado válido. |
| Símbolo de porcentaje omitido en tabla SLA | SD3 `:322–323` presenta `≥ 99,95` y `≥ 99,9` sin `%`; el texto aclara porcentajes en `:328`. | Añadir la unidad a la tabla para lectura autónoma. |
| Alcance de compra Starlink | T-9 `06_metodologías/LAFROX-Formulario-T-9.md:90` y Anexo SD6 `LAFROX-Subdocumento6-Anexos.md:57` mencionan tres plataformas; T-11 `04_arquitectura/LAFROX-Formulario-T-11.md:57` y T-14 `07_PlanDeTrabajo_EDT_Cronograma_Implantación/LAFROX-Formulario-T-14.md:1450` contabilizan cinco sitios. | Puede tratarse solo del subconjunto cross-docking; confirmar si la fila de adquisición comprende los dos CD. |
| Primera medición I-04A | Anexo SD13 `13_innovaciones/LAFROX-Subdocumento13-Anexos.md:69` indica primera medición mes 36; SD13 `:529,533` y T-19 `LAFROX-Formulario-T-19.md:96` dicen medición mensual desde mes 24 y meta en mes 36. | Aclarar diferencia entre seguimiento periódico y evaluación de la meta. |
| Conteo de indicadores antes del mes 16 | Anexo SD13 `:52–58` contiene siete filas afirmativas; `:71` dice seis indicadores. | Aclarar si una fila se excluye del conteo y por qué. |
| Copia regional de registros térmicos | SD5-Anexos `05_modelo_datos/LAFROX-Subdocumento5-Anexos.md:1306` dice sin réplica fuera de región declarada. SD4 `04_arquitectura/LAFROX-Subdocumento4.md:3180` incluye registros de temperatura en copia diferida a región secundaria. | Precisar si se trata del mismo conjunto de datos y cuáles son los destinos permitidos. |
| Población de capacitación | SD2 `02_problema_necesidad/LAFROX-Subdocumento2.md:256` y Anexo SD3 `03_esquema_solucion_alcance/LAFROX-Subdocumento3-Anexos.md:137,602` describen 120 preparadores; S-39 agrega por supuesto 60 simultáneos de Concepción (`:440`). | Confirmar si los 60 adicionales están incluidos en la población de capacitación. |
| Reversión técnica frente a recuperación operacional | SD4/T-18 distinguen reversión técnica ≤10 minutos y recuperación operacional de 40 minutos. | No se clasificó como contradicción: son objetivos distintos descritos explícitamente. |
| Conteos de requisitos y aceptación | Las cifras 175 RF/86 RNF ofertados frente a 181/90 filas de T-12 tienen explicación por alias/materias complementarias. Doce resultados aceptados E1 frente a catorce verificados también está explicado en SD7. | No se clasificaron como contradicciones vigentes. |

## 3. Registro inicial — clasificación por complejidad

| Complejidad | Inconsistencia | Motivo de complejidad | Alcance típico de la corrección |
|---|---|---|---|
| Baja | Porcentajes sin `%` en tabla SLA | Corrección editorial localizada, con unidad aclarada en el texto. | Ajuste puntual de tabla y lectura final. |
| Baja | Ancla rota del resumen SD3 | Cambio localizado si existe un encabezado destino correcto. | Actualizar enlace o encabezado. |
| Baja | Referencia A.34/A.36 | Las cifras ya están identificadas; falta corregir destino. | Corregir cita en SD5 y verificar referencias relacionadas. |
| Baja | Meses 5–8 descritos como junio–octubre | Equivalencia de calendario localizada si se mantiene el mes 1. | Cambiar mes final en T-15 y SD8. |
| Baja | Fin de grupo 3.4 antes de paquetes hijos | Ajuste de una fecha agregada, con contraste de las filas hijas. | Corregir agregado o fechas fuente. |
| Baja | Seis frente a siete indicadores anticipados | Conteo local; podría requerir decidir si una fila se excluye. | Corregir cifra o explicar criterio de exclusión. |
| Media | C-05 no refleja umbral 2.283/2.391 | Hay que sincronizar el disparador con reglas por período. | Actualizar C-05 y revisar referencias cruzadas. |
| Media | Throughput 12,34 frente a 12,30 TPS | Hay que escoger base válida y actualizar dimensiones/pruebas dependientes. | Cotejo de cálculos SD4/SD5 y sus protocolos. |
| Media | Primera medición de I-04A | Puede ser una distinción conceptual entre seguimiento y meta. | Aclarar definición y sincronizar anexo, cuerpo y T-19. |
| Media | 120 frente a 180 preparadores | El valor adicional es supuesto y puede afectar planificación de capacitación. | Confirmar población y actualizar plan/capacidad. |
| Media | Tres frente a cinco sitios Starlink | El subconjunto de plataformas puede explicar la diferencia; alcance no es explícito. | Confirmar compras por sitio y corregir fila de adquisición. |
| Media | Tabla SD3 sobre estructura actual de T-12 | Requiere alinear la descripción con las columnas vigentes, no necesariamente rediseñar la matriz. | Corregir prosa y referencias metodológicas. |
| Media | RPO de 15 minutos frente a excepción de pérdida de sitio | La excepción puede ser legítima, pero debe propagarse a las síntesis de continuidad. | Definir escenario y reflejar límite/riesgo en todos los documentos afectados. |
| Media | Métodos de prueba no demuestran criterios | Varias correspondencias requieren revisión por requisito. | Rehacer mapeo de pruebas y criterios en el anexo. |
| Media | Catorce enlaces PDF ausentes localmente | Si existen, incluirlos o corregir rutas; si faltan, recuperarlos o regenerarlos. | Verificar origen y entrega de 14 figuras. |
| Media | Réplica de datos térmicos entre regiones | Requiere precisar si los documentos describen copias diferentes y revisar restricciones de datos. | Aclarar arquitectura y política de retención/replicación. |
| Alta | Secuencia de habilitación de sala | Fechas contradictorias con recepción e hitos; afecta precedencias y preparación de sitio. | Revalidar cronograma, dependencias y criterios de recepción. |
| Alta | Responsabilidad de obra civil | Es una asignación cliente–proveedor que puede afectar contrato, costo y aceptación. | Resolver responsabilidad y separar obra, coordinación y suministro. |
| Alta | Instalación de equipos frente a montaje escalonado | “Instalación” agrupa equipos y sitios que tienen fechas distintas. | Definir entregables por sitio, dependencias y puesta en marcha. |
| Alta | Innovaciones comprometidas para H4 terminan después del hito | Puede requerir reprogramar red de trabajo, QA y revisión del CLIENTE. | Recalcular paquetes, precedencias y criterios de H4. |
| Alta | H12, actas y paquetes dependientes | Varias fechas y dependencias están en orden incompatible. | Replanificar cierre, estabilización, actas y acompañamiento. |
| Alta | HH de estabilización no coinciden entre supuesto y curva | Implica revisar cálculo y distribución de recursos. | Recalcular curva por mes y validar el período de Operación. |
| Alta | Gantt de integraciones empieza después que paquetes | Cambiar el agregado puede afectar hitos y dependencias. | Alinear Gantt y paquetes y verificar impacto en H4. |
| Alta | RF-07.10/RF-07.11 cobranza | La cobertura y exclusión requieren decisión sobre alcance funcional. | Resolver función, componentes y estado de cumplimiento en SD3/T-12. |
| Alta | Acuse comercial marcado Cumple y parcialmente incumplido | Un acuse técnico no equivale al compromiso comercial. | Confirmar solución de extremo a extremo y alinear aceptación. |
| Alta | Sincronización dentro o fuera de cámara | Diferencia funcional sobre operación sin conectividad. | Definir comportamiento y reflejarlo en requisito, arquitectura y cumplimiento. |
| Alta | Portal para canal tradicional | Requiere definir funciones, identidad y precondiciones por canal. | Resolver alcance con actores, seguridad, integración y requisitos. |
| Alta | Umbral 80 % de pruebas usa distinto universo | Cambia la compuerta de promoción y el esfuerzo de pruebas. | Definir universo de medición y armonizar SD4/T-10. |

## Registro inicial — estado de los resúmenes y de la revisión

Se cotejaron 26 resúmenes; 13 se actualizaron y 13 se conservaron. Entre los cambios se encuentran T-9, T-10, T-12, T-6, SD3-Anexos, SD4, SD4-Anexos, SD6, SD7, SD7-Anexos, SD8, SD8-Anexos y T-16. Se corrigieron, entre otros puntos, la matriz y los enlaces de T-12, fechas y contenidos metodológicos de SD6, aceptación/reservas de SD7 y cifras/clasificaciones de SD8.

La revisión no modificó los documentos fuente. `Requerimientos/` quedó excluido. El control de enlaces de los resúmenes modificados revisó 114 destinos locales sin errores; además, se identificaron 14 destinos PDF locales ausentes en SD2/SD3. No se ejecutó un rastreo automatizado completo de anclas ni renderizado PDF.
