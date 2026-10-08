# Correcciones del Subdocumento 3, de menor a mayor dificultad

Revisión ampliada: 1 de octubre de 2026.

Esta lista integra los hallazgos de `ANALISIS_SUBDOCUMENTO_3_ACTUAL.md` y la segunda revisión. El orden estima esfuerzo, número de archivos afectados y necesidad de decisiones o antecedentes externos. Dificultad y gravedad son cosas distintas: una contradicción importante puede resolverse con una edición local.

Se revisaron nuevamente cuerpo, catálogos, supuestos, reglas, decisiones, consultas, actores, criterios y correspondencias; se contrastaron requisitos seleccionados del T-12 con las Bases. Se inspeccionó el conjunto completo de páginas del cuerpo en hojas de contacto y páginas representativas de los otros dos PDF. No se afirma una auditoría semántica exhaustiva de las 374 respuestas RT ni una inspección visual completa de las 349 páginas de anexos y T-12.

Las entradas incluyen errores comprobados, precisiones de verificabilidad y cierres que dependen de documentos aún no disponibles. La revisión anterior dio por corregido el horario de soporte en el cuerpo; la segunda detectó que el catálogo RNF todavía conserva el horario anterior. La propuesta de reversión manual también contradice una restricción expresa del caso, además de carecer de tiempo máximo. Esos hallazgos amplían el diagnóstico anterior.

## Ediciones locales: dificultad baja

1. **Actualizar la cantidad de supuestos.** La sección 3.2.2 dice 29, mientras el Anexo 3.C contiene S-01 a S-40. Cambiar a 40 y comprobar las demás menciones. Error comprobado.

2. **Aclarar el universo de requisitos y sus prioridades.** Los 250 son los requisitos del caso y BTT, sin los once propios. El compromiso conjunto es de 261: 175 RF y 86 RNF. La distribución completa es 56 críticos, 162 altos y 43 medios, frente a 54/157/39 del subconjunto de 250. Presentar ambos universos con su alcance explícito. Ubicación: 3.2.3 y comienzo del Anexo 3.A. Error de alcance de la cifra resumen.

3. **Actualizar el README.** Conserva 174 RF, 31 desarrollados, 90 RNF y un estado de matrices abiertas que no describe la versión activa. Actualizar inventario, estado, salidas vigentes y limitaciones. Error comprobado.

4. **Corregir redacción, unidades y capitalización en catálogos.** Hay expresiones como «El sistema registrara», «Los registros son auditable», «registro fotografico», «credencial tecnica», «api», y `m\textasciicircum{}3`. Usar redacción uniforme, acentos y unidades correctamente compuestas. Ubicación: RF-09.03, RF-09.04, RF-06.12, RF-14.01 y RF-11.05, entre otras filas. Corrección editorial.

5. **Eliminar la autorreferencia de RF-03.16.** Su precondición cita RF-03.16 como antecedente del reintento. Referir al pedido local identificado por RF-03.15 y a la recuperación de conectividad. Error comprobado.

6. **Separar restricciones obligatorias de supuestos y consultas resueltas.** S-24 reconoce que es un mínimo obligatorio y que no requiere validación; V-05 dice que no requiere respuesta, dentro de «Consultas abiertas». Conservar referencias históricas si son necesarias, pero clasificar cada registro por su estado y naturaleza. Mejora de consistencia del registro.

7. **Completar las convenciones de respuesta del T-12.** Las convenciones enumeran Sí por etapa, No aplica, No ofertado y Sí (licitación), pero aparecen «Sí (alias)», «Absorbido por…» y «Sí, condicionado». Definir esos estados y qué evidencia exige cada uno. Inconsistencia comprobada.

8. **Ampliar el glosario para distinguir códigos por fuente.** RT se define solamente como requisito BTT, pero el documento también cita códigos RT del caso que pueden tener otro significado. Explicar desde el glosario la regla de identificación por documento de origen. Ubicación: Anexo 3.K. Error de ambigüedad comprobado; la aplicación global corresponde al punto 19.

9. **Corregir la etiqueta de la Figura 3.3.** «Reconexión» queda demasiado próxima y parcialmente superpuesta a los bordes de los nodos en la página 16 del cuerpo. Reposicionarla y comprobar la figura a tamaño de lectura. Defecto visual comprobado.

10. **Mejorar la composición de tablas.** Las páginas examinadas del T-12 y anexos muestran columnas estrechas, palabras partidas en exceso y filas muy altas. Ajustar proporciones, orientación y separación de información extensa, conservando legibilidad. Son 142 páginas de anexos y 207 de T-12; el volumen no es por sí mismo incumplimiento, pero justifica revisar el diseño. Mejora visual comprobada por muestreo.

11. **Actualizar RNF-21.04 con el horario ofertado.** Mantiene 08:00–20:00 en días hábiles, mientras 3.4.5, D-10 y RT-21.07 del T-12 ya declaran atención general 04:00–22:00 de lunes a sábado y ampliación en peaks. Consolidar el horario aplicable y mantener diferenciada la atención de incidentes críticos y altos 24×7. Contradicción comprobada.

## Revisión de tablas y criterios: dificultad media

12. **Completar los umbrales de RNF que siguen siendo vagos.** RNF-04.01 habla de «tiempo acotado» aunque el caso exige menos de 20 minutos; RNF-06.01 no expresa sus 14 horas de autonomía. RNF-09.04 debe aclarar que se captura sin señal en la cámara y se sincroniza al recuperar conectividad, sin suponer cobertura dentro de ella. Corregir la formulación y su prueba. Errores o ambigüedades comprobados.

13. **Identificar en cada fila los parámetros propios de LafroX.** Existe una advertencia general, pero es preferible marcar localmente los valores propuestos frente a los impuestos por las Bases: 30 minutos de uso en cámara, botones de 15×15 mm, misión de 20 líneas, tasa de error del 5 %, tiempos adicionales y metas propias. Así se puede validar cada compromiso sin atribuirlo a la fuente. Precisión de origen, no afirmación de que todos esos valores sean incorrectos.

14. **Separar el envío del ASN del acuse después de la descarga.** RF-12.09 envía el ASN dentro de dos minutos de la carga; RNF-12.03 describe enviar el acuse dentro de 30 minutos después de descargar «junto con el aviso de despacho». Conservar dos eventos y plazos, referidos a la misma guía. Ambigüedad temporal comprobada.

15. **Completar la correspondencia de requisitos propios con las familias.** La Tabla 3.A.2 ya incorpora RF-02.11 y RF-06.14, pero RF-06.06, RF-09.10 y RF-10.01 a RF-10.03 requieren una asociación explícita a familia, capacidad o grupo complementario. La reposición aparece en el cuerpo, sin fila propia en la síntesis de etapas. Actualizar la síntesis y el mapa sin inventar familias del SD2. Mejora de trazabilidad.

16. **Revisar la responsabilidad de los módulos.** El T-12 asigna RF-02.08 (picking) a M2 Inventario y RF-11.07 (liquidación) a M10 Analítica, mientras la Tabla 3.4 identifica M5 Preparación y M7 Cobranza y rendición. Precisar responsable principal y componentes colaboradores. No basta asignar por el prefijo numérico del RF. Ambigüedad comprobada.

17. **Corregir pruebas funcionales que no verifican su función.** RF-01.07 y RF-01.08 están asociados a registro térmico; RF-11.06 también usa una prueba térmica aunque es un tablero. RT-05.23 utiliza esa misma evidencia para estándares sectoriales. Incorporar pruebas de generación y asociación del SSCC, actualización del tablero y validación de los intercambios pertinentes. Errores comprobados.

18. **Corregir métodos de verificación de RNF.** RNF-14.01 (TLS) y RNF-14.05 (EDR) usan prueba de desempeño; RNF-14.07 (controles CI/CD) y RNF-22.02 (material de capacitación) usan recuperación RTO/RPO; RNF-20.01 (disponibilidad mensual) usa un ejercicio de recuperación; RNF-20.06 (conmutación DR) solo inspección documental. Verificar con configuración, ensayos controlados, registros operacionales o inspección según corresponda. Errores comprobados; una prueba complementaria puede mantenerse.

19. **Distinguir las exigencias de códigos RT coincidentes entre caso y BTT.** Hay diferencias comprobadas en RT-03.13, RT-03.24, RT-16.14, RT-16.21, RT-16.30 y RT-21.06. En el T-12, RT-16.14 BTT (motor de reglas) se relaciona con funciones de evidencia de entrega; RT-03.13 BTT (declaración de funciones desconectadas) se vincula a sincronización; RT-03.24 BTT (QoS deseable) figura no ofertado, mientras el mismo código del caso exige estudio de cobertura. Crear identificación por fuente y responder ambas materias, aunque se reutilice un componente. Error comprobado y de extensión transversal.

20. **Distinguir cuándo se entrega y cuándo se verifica cada obligación.** RF-13.01 a RF-13.04 incluyen arquitectura, emplazamiento, ADR y modelo de dominio, que son entregables documentales. Las convenciones generales del T-12 remiten el cumplimiento a la marcha blanca y no precisan obligaciones de oferta, por liberación, anuales o posteriores. Introducir momento y entregable aplicables. Ambigüedad comprobada.

21. **Unificar la interpretación de la promesa 24/48 horas.** El cuerpo y S-21 no califican las horas; RNG-15 agrega «horas hábiles» y cómputo desde el siguiente día hábil después del corte. Definir calendario de servicio, sábados, festivos, comienzo del plazo y tratamiento del pedido sin señal. Mostrar la misma fecha prometida en preventa y usarla en la prueba. Inconsistencia y precisión necesarias.

22. **Dar a cada ola sus propios criterios de avance.** La regla general exige indicadores del Anexo 3.J durante cuatro semanas, pero ese anexo contiene E2, metas anuales y mes 32. Vincular cada ola con resultados aplicables, período, evidencia y aceptación provisional o definitiva. Error de alcance de la regla general.

23. **Completar la fórmula de OTIF y su medición.** S-01 y RNG-09 definen entrega completa y ventana, pero falta cerrar denominador, fecha de corte, pedidos cancelados, reintentos, parciales y agregación de pedidos con varias entregas. Para el trayecto 82,4 % → 90/93/95 %, indicar período de medición y procedimiento de recalibración de la línea base. Precisión necesaria para evitar distintas mediciones.

24. **Precisar la pérdida anual de envases.** R18-12 usa «envases no recuperados ni conciliados sobre parque despachado». Definir si el denominador cuenta unidades del parque o movimientos acumulados, antigüedad para considerar pérdida, envases todavía legítimamente en poder del cliente y tratamiento por canastillos/pallets. Unificar la meta de 7 % con S-26 y el período anual. Ambigüedad de medición comprobada.

25. **Acotar las excepciones a la ocupación mínima.** R18-14 permite despachar bajo el 60 % con autorización, pero no fija límites o revisión del volumen de excepciones. Definir fórmula del promedio ponderado, capacidad útil, viajes incluidos y control de excepciones, para que la meta no se cumpla mediante autorizaciones sistemáticas. En RF-11.05 usar el parámetro S-27 y evitar que el ejemplo de 65 % parezca otra meta. Precisión necesaria.

26. **Hacer verificable el ensayo sin planificador.** R18-16 compara dos semanas con dos semanas previas y excluye incidencias externas. Fijar anticipadamente reglas de comparabilidad y exclusión, quién aprueba el análisis, sustituto que operará y registro de correcciones. La retirada selectiva de incidencias no debe decidirse después de conocer el resultado. Mejora del protocolo.

27. **Explicitar el soporte entre los meses 16 y 20.** E1 está en producción antes de comenzar los 36 meses de Operación en el mes 21. El documento menciona estabilización y cuatro semanas por ola, pero debe identificar el servicio, responsable, cobertura y niveles aplicables al resto de ese período. Brecha de explicitación, sin afirmar que ese soporte esté excluido del contrato.

28. **Precisar ramas, versiones y liberaciones.** 3.4.3 cita una «rama versionada» e integración continua. Definir flujo de integración, aprobación, etiquetado de versiones, promoción de configuración y tratamiento de correcciones urgentes cuando E2 y E1 trabajan en paralelo. Detallar en el documento correspondiente y resumir la regla en SD3. Desarrollo adicional.

## Decisiones operacionales y dependencias: dificultad alta

29. **Validar la dotación de acompañamiento y su calendario.** Siete personas salen de 158 rutas / 24 días; eso prueba una cobertura teórica de una visita por ruta, no la dotación total. Precisar olas simultáneas, desplazamientos, turnos, contingencias y extensión si no se certifica a todos. Vincular bodega, plataformas y calle con T-15 y considerar la dotación de Concepción supuesta en S-39. Validación cuantitativa pendiente.

30. **Concretar el modelo operacional y de soporte.** RNF-21.01 exige ubicación y dotación por turno del NOC; RNF-21.05 pide dimensionamiento del centro de atención; RNF-16.02 exige procedimientos por escenario y automatización progresiva. El cuerpo resume monitoreo y escalamiento, pero faltan artefactos concretos localizados: capacidad de atención, procedimientos de colas, fallas de ERP, sensores y dispositivos, y tareas automatizables. Puede residir en otros subdocumentos, con referencias verificables.

31. **Unificar la base de dimensionamiento del hardware.** S-23 liga 244 personas a dispositivos; S-30 asigna equipos por camión y vuelve a «unas 200 personas». Diferenciar usuarios registrados, concurrencia y terminales compartidos. S-31 supone crecimiento proporcional de camiones y S-38 mantiene fija la flota refrigerada: justificar la mezcla y qué escenario dimensiona cada dispositivo. S-22 y S-40 deben encajar con instalaciones actuales y crecimiento. Inconsistencias y supuestos a consolidar.

32. **Completar el circuito de entrega y acuse.** S-15 incluye nombre del receptor cuando falta firma; RF-06.12 presupone que puede firmar o autorizar fotografía; RF-06.14 depende de RF-06.11/12. Definir tratamiento de negativa total, receptor distinto del titular y falta de señal, preservando evidencia. Distinguir POD, evidencia enviada al ERP y estado del acuse. La alternativa aceptada debe sustentarse en investigación normativa y capacidad real del ERP; V-18 no puede afirmar anticipadamente que nunca cambia el alcance. Brecha funcional y dependencia externa.

33. **Completar el control térmico durante el viaje y sin señal.** RF-09.06 tiene como precondición un camión pendiente de despacho, aunque la regla crítica también se narra durante la ruta. Definir retención antes de la salida y bloqueo de entregas del lote ya en tránsito; quién atiende Calidad, plazos y comportamiento desconectado. RF-09.05 usa 2 °C/15 minutos mientras RF-09.10 permite parametrización: distinguir valor inicial y regla vigente, y definir cómo se verifica continuidad de lecturas, intervalos, calibración y sensores sin datos. Desarrollo de diseño y prueba.

34. **Declarar funciones desconectadas y reglas de reconciliación.** RNF-13.02 pide la declaración, pero el catálogo no la sustituye. Documentar qué sigue funcionando y qué se degrada o detiene por perfil/sitio, incluyendo la promesa comercial. RNG-12 aporta cola y deduplicación, pero no resuelve las reglas deterministas para stock, reservas concurrentes, movimiento del mismo pallet, precio o crédito. Fijar autoridad de datos, orden y resolución por tipo de conflicto. Brecha técnica central.

35. **Separar limpieza del inventario de exactitud de migración.** S-29 usa una discrepancia operativa de 2,3 % como tolerancia de saldos valorizados. Exigir transferencia exacta de los saldos aprobados y gestionar por separado diferencias físico/registro, lotes desconocidos y ajustes autorizados. Para datos sanitarios incompletos de origen, establecer cómo se identifican, validan o aíslan antes del corte. La exigencia de exactitud de lotes no recupera datos inexistentes. Decisión de migración pendiente.

36. **Rediseñar la reversión de la ventana de despacho.** R-01 dice que 05:30–07:00 no puede ejecutarse a mano. 3.4.4 propone como vía operacional volver al procedimiento manual con picking y guías. Además, exige concluir antes de las 05:30 y contempla defectos dentro de esa ventana. Definir una alternativa digital/local o versión previa capaz de sostener el despacho, con datos y documentos disponibles; separar respaldo de papel de continuidad del despacho. Establecer tiempo máximo ensayado, última hora de decisión y actuación después de las 05:30. Contradicción comprobada de alta importancia.

37. **Consolidar un calendario real y control de dependencias.** Integrar fecha de inicio, hitos 16/21, congelamientos, cuatro semanas por ola, enero de 2029, retiro del planificador y entrega del hardware. S-20 y la estrategia de actores dicen que se puede postergar una ola sin alterar hitos, pero no muestran holguras ni contingencia. Las BA 17.3 regulan extensión de marcha blanca y atraso. Definir escenarios, fechas límite y efecto de fallos de supuestos sin prometer que toda demora es absorbible. Depende de planificación y decisiones del mandante.

38. **Garantizar datos de costo de servir para toda la flota.** R18-11 exige 100 % de entregas costeadas. RF-11.02 y RF-14.04 dependen de kilómetros y tiempos de telemetría; RF-14.01 declara integración para 42 camiones propios, mientras hay 54 camiones de terceros. Definir fuentes equivalentes para terceros y para períodos sin GPS, distinguir costos reales/estimados y reconciliar con contabilidad. No afirmar que el GPS por sí solo mide el combustible devengado. Cobertura de datos a demostrar.

39. **Completar la evidencia y el mapeo con la arquitectura.** El cuerpo afirma que M1–M12 son los nombres de la arquitectura y las aclaraciones exigen 100 % de correspondencia con 4.1. No se encontró SD4 en la carpeta revisada. Verificar nombres, límites, responsabilidades, componentes de la base compartida e interfaces cuando esté disponible. En T-12, localizar componente/práctica y sección/página exigidos por BTT 1.5. RT-26.01/02 remiten a 3.2.1, que no presenta arquitectura ni EDT de cada innovación: sustituir por la evidencia correspondiente. Cierre condicionado a documentación real.

40. **Completar la trazabilidad individual a EDT, prueba y aceptación.** Hay 262 filas con paquete por asignar. Vincular requisitos ofertados con paquetes reales de T-14, pruebas identificadas de T-13 y criterios pertinentes. RF-02.10 está ligado a faltantes (R18-15) pese a contribuir a retiro sanitario (R18-01); RF-11.07 se liga a OTIF/costo y debe incluir rendición R18-10. Para requisitos transversales, BA 17.3 no reemplaza su criterio específico. Resolver alias y materias absorbidas con enlaces transitivos auditables. Trabajo extenso y dependiente de planificación, arquitectura y calidad.

41. **Consolidar la fuente de datos y el flujo de generación.** El README recomienda `tablas/generador/gen.py`, pero este produce fragmentos anteriores en `tablas`, mientras los anexos activos usan `tablas_anexo` y el T-12 contiene tablas directamente. Definir una fuente gobernante, actualizar el generador y verificar que reproduce los documentos vigentes sin reintroducir matrices vacías ni perder correcciones. No ejecutar una regeneración hasta resolver esa discrepancia. Corrección estructural de mantenimiento.

42. **Cerrar la revisión humana y la versión formal.** Las portadas declaran versión final, el T-12 mantiene pendientes y las declaraciones de IA dicen «No documentada». Resolver los hallazgos, someter contenido y compromisos a revisión humana real, registrar responsables y resultado, actualizar referencias y recompilar los tres documentos. Comprobar enlaces, índices y páginas después de cambios. La fecha de emisión prefijada del 5 de octubre debe coincidir con la edición que efectivamente se entrega. No sustituir la revisión por una afirmación ficticia. Cierre de entrega dependiente de las correcciones anteriores.

## Cómo ejecutar la lista

El orden anterior sirve para comenzar por tareas pequeñas. Para preparar una entrega, los puntos 19, 32–40 y 42 merecen especial atención por su efecto en cumplimiento y operación, aunque sean más complejos. Los puntos que dependen de SD4, T-13, T-14 o T-15 deben completarse con documentos reales; la falta de esos archivos limita la verificación, no prueba que no existan fuera de esta carpeta.

La segunda revisión no modificó los archivos de la oferta. Esta lista es el resultado consolidado y sustituye la priorización resumida del informe anterior.
