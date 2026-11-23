# LafroX — Validaciones para cerrar el SD7

## Resultado de la revisión documental

- T-15 y T-18 coinciden en el expediente por etapa, la firma previa al corte y el registro de producción posterior. El T-10 de SD6 reproduce las fechas nominales de firma y corte. El calendario parte de febrero de 2027 según el Anexo 7.A y sigue sujeto a V-12.
- El T-15 ubica 6.8.6 entre el 2 y el 11 de octubre de 2028 y lo exige antes de firmar H12 el día 17. T-18 y T-17 respaldan el orden de aceptación. Los textos revisados no fijan su inclusión en el expediente del día 2. El acta de inicio 1.1.3 recoge la confirmación sobre ese requisito y la ventana autorizada.
- H5 conserva 32 HH de margen teórico para los trece días críticos. El contraste mensual por origen de SD12 y el diario del T-15 miden intervalos distintos. El T-8 respalda las nominaciones clave y no acredita una asignación diaria de los refuerzos.
- T-15 imputa 9.336 HH del puente de M16 a M20 a 9.3.1. T-18 imputa la cobertura de NOC, mesa y SOC del 1 al 17 de octubre de 2028 a 10.1.1, 10.1.2 y 10.1.4. Las ventanas pertenecen a meses distintos.
- T-13 de SD9, sección 9.3, y el plan operativo de SD11 documentan el protocolo mensual de restauraciones. La secuencia del T-15 desde M13 suma ocho informes de 16 HH antes de Operación y 36 informes durante Operación. La documentación revisada no aporta un calendario de pruebas mensuales anterior a M13. Para la evaluación independiente de seguridad, T-15 reserva 320 HH en E1 y 160 en E2 y T-8 documenta la modalidad de contratación. El alcance y las HH efectivas quedan sujetos a la ejecución.
- El T-15 documenta los rangos PERT por tipo y los riesgos con rangos asimétricos, y deriva los 15 módulos de los requisitos del T-12. Las productividades observadas se calibran cuando se disponga de mediciones de ejecución.

## Confirmación de H7 y H12

Consulta para la Contraparte Técnica, preparada para revisión y sin enviar:

> Para H7 y H12, solicitamos confirmar si puede presentarse un expediente integrado por etapa que incluya la evidencia completa de las últimas cuatro semanas de marcha blanca, la trazabilidad, la resolución de observaciones previas y, en H12, la garantía de correcto funcionamiento. Se mantienen los diez días hábiles del artículo 18.3 y la firma del acta del artículo 17.3 antes de autorizar el corte. ¿Puede incorporarse la constancia del paso efectivo a producción al mismo expediente sin abrir una segunda revisión integral? Si se requiere una aceptación final separada, solicitamos precisar su entregable, momento de presentación y plazo de revisión, sin cambiar los meses contractuales 16 y 21. ¿La verificación de reconstrucción y despliegue del paquete 6.8.6 debe acompañar el ingreso de H12 o puede acreditarse durante la revisión, antes de la firma?

La alternativa se calculó con el calendario de inicio en febrero de 2027 y sin observaciones: entrega 2 de mayo / 2 de octubre de 2028; revisión 3–16 de mayo / 3–17 de octubre; primera ventana de producción 17 de mayo / 18 de octubre. La respuesta de la Contraparte debe confirmar tanto el procedimiento como la forma de registrar el cumplimiento del hito. Un resultado de calendario no acredita una autorización.

## Disponibilidad de recursos

1. Calidad: confirmar los titulares de las diez plazas de planta y tres plazas de refuerzo, sus turnos durante los trece días críticos y la disponibilidad neta de otros servicios. El umbral es 1.049,60 HH; 13 × 13 × 6,4 = 1.081,60 HH, con margen teórico de 32 HH. Si la disponibilidad neta cae por debajo del umbral, recalcular la programación de 6.2.1, 6.2.2, 6.3.1 y 6.4.1 antes de comprometer H5.
2. Implantación: identificar quién cubre cada puesto de acompañamiento y cada turno de despliegue, capacitación y coordinación. El T-15 (tabla de plazas previstas) y SD12 (tabla de demanda por fase) coinciden en una demanda máxima de 26 plazas en M19–M20 frente a 27 previstas, nueve de planta y 18 por obra o faena. El T-8 identifica a los titulares clave; la asignación individual de los turnos de terreno queda para la ejecución. Conciliar los paquetes continuos con los de entregable y el SD12/T-8.

## Calibración del esfuerzo y PERT

Para cada paquete, el responsable presenta el código EDT, las actividades, cantidades, fuente y capacidad efectiva. En software se parte de los requisitos vinculados del T-12 y se separan flujos, interfaces y pruebas. En instalación se usan cantidades del T-11 y tiempos de instalación comprobables; en migración, volúmenes y rendimientos de los ensayos; en implantación, puestos, rutas, turnos y ventanas del T-18. Las coberturas fijadas por calendario conservan su duración contractual.

Por actividad se registra qué cambia entre O, M y P (por ejemplo, reprocesos, disponibilidad de contraparte o rendimiento); no basta aplicar un porcentaje común. Se calcula el esperado del paquete, se compara con las HH base y, si se adopta otra estimación, se vuelven a ejecutar la red, la nivelación y el cruce por perfiles. El escenario de los 15 módulos permite revisar el cálculo; no reemplaza la calibración ni constituye una aprobación de productividad.

## Regeneración y comprobación de la carta vigente

1. Ejecutar `python revision/edt_cpm_20261117.py --output-dir tmp/sd7-correcciones` para obtener las tablas y el JSON de la red. El JSON registra los márgenes separados de firma y corte, el escenario de diez días y el contraste diario de Desarrollo y Calidad.
2. Generar el CPM lógico con `python -B revision/cpm_y_riesgo_sd7.py --output-dir tmp/sd7-correcciones/cpm` y cotejar sus tablas con las publicadas. Con ReportLab disponible, ejecutar `python revision/gantt_local_vector.py --schedule tmp/sd7-correcciones/cronograma_sd7.json --logical-cpm tmp/sd7-correcciones/cpm/cpm-pert-sd7.json --output-dir tmp/sd7-correcciones/gantt`. Añadir `--publish` para instalar las vistas y láminas verificadas y actualizar las llamadas LaTeX.
3. **Validación nominal en GanttProject.** Comparar fechas, ambas duraciones y dependencias. Se verificó la carga y el recálculo del motor por línea de comandos. El guardado y la reapertura por interfaz siguen pendientes.
4. Ejecutar `revision/compilar_local_sd7.ps1` y revisar los PDF y sus referencias antes de instalar los resultados en la raíz.

### Prueba de GanttProject del 21-11-2026

- Se usó GanttProject **3.3.3330** con Java 17.0.21.1. Se verificó el SHA-256 del paquete oficial y de los tres `.gan` de referencia. GanttProject cargó y exportó por CLI **286, 35 y 41 filas** en las vistas de detalle, 56 meses y ruta crítica.
- **Escenario de H12 aprobado en las tres vistas por CLI.** Al cargar una copia con 11 días de revisión para la tarea 277, el motor llevó la firma al **18-10-2028** y el corte y el registro al **19-10-2028**.
- **Vínculos del detalle.** La aplicación rechazó siete vínculos por duplicidad de par origen-destino. La exportación nominal devolvió 622 de los 629 declarados. El generador ahora representa los pares CC/FF mediante seis hitos auxiliares de fin. Una generación de prueba conservó en la aplicación los **635 vínculos de 292 filas** del detalle y repitió con éxito el escenario de H12 en las tres vistas.
- **Calendario nominal pendiente.** GanttProject desplaza el traslado del ERP del **11 al 12 de julio de 2027**, el cierre de evidencia de H7 del **30 de abril al 2 de mayo de 2028** y el de H12 del **30 de septiembre al 2 de octubre de 2028**. También desplaza del 1 al 2 de octubre el comienzo de la transición del mes 21. Una prueba con cinco excepciones laborables recuperó las fechas de los tres primeros eventos, pero cambió **33 filas** respecto de la carga nominal. Por ejemplo, la barra de marcha blanca de E1 terminó el 27 de abril en esa prueba. Se mantiene el T-15 como referencia y la generación corregida queda en temporal.
- **Guardado y reapertura por interfaz pendientes.** La revisión automática de permisos rechazó el acceso a la ventana. La exportación CLI acredita la carga y el recálculo del motor, y sus resultados se conservan con los JSON y CSV en `tmp/sd7-correcciones/validacion-ganttproject`. El cierre requiere una representación de los eventos de fin de semana que preserve las fechas civiles y las duraciones hábiles del T-15, seguida de una nueva prueba nominal y de guardado y reapertura.

### Prueba con excepciones y duraciones recalculadas

- Se activaron como laborables el 11-07-2027, 01-04-2028, 30-04-2028, 30-09-2028 y 01-10-2028. Se recalcularon todas las duraciones y desfases respecto de ese calendario. GanttProject exportó todas las fechas nominales tal como aparecen en el modelo y conservó 635, 25 y 18 vínculos. La prueba de once días de revisión mantuvo la firma el 18-10-2028 y el corte y registro el 19-10-2028 en las tres vistas.
- El costo de esa representación fue modificar 32 duraciones nativas en el detalle, siete en la carta de 56 meses y ocho en la vista crítica. La incompatibilidad se verifica con dos barras. La cobertura del 01 al 17 de octubre debe iniciar el día 1 y conservar 11 días hábiles. Si el día 1 se habilita, quedan como máximo 10 días laborables entre el 02 y el 17. Con el día 18, 9.4.2 puede tener como máximo 11 días laborables entre el 02 y el 18, frente a los 12 del modelo. Por tanto, ninguna selección de excepciones en un único calendario diario permite satisfacer ambos requisitos.
- Se conserva el candidato de prueba con fechas exactas y duraciones de calendario recalculadas. El usuario autorizó mostrar ambas medidas. Los tres editables nominales se regeneraron con las columnas Duración (calendario del motor) y Días hábiles T-15 (valor nominal de la fuente). Esta última es una referencia de línea base que se vuelve a generar desde el T-15 al actualizar la programación. La exportación CLI confirmó por ID todas las fechas, ambas duraciones y los vínculos, y repitió con éxito el escenario de H12. La comprobación de guardado y reapertura por interfaz queda pendiente porque la revisión automática volvió a denegar el acceso a la ventana.

La evidencia local está en `tmp/sd7-cierre-ramas/doble-duracion`. Desde la raíz se puede repetir el cotejo de las seis exportaciones con `python tmp/sd7-cierre-ramas/verificar_gantt.py`.

## Comprobación de los documentos relacionados

- SD9 (84c12443) y T-17: se cruzaron las diez filas con entrega y acta del T-15. H6 y H11 se verificaron como aperturas de marcha blanca. H3 queda con evidencia al 18-06-2027, entrega el 22-06, firma el 07-07 y margen de 16 días hábiles. Se incorpora la autonomía 8.7.3 al expediente de H3 y la verificación previa a la firma de 6.8.6 a H12. Los márgenes de firma y corte de H7/H12 y el efecto del congelamiento se muestran explícitamente.
- SD10 (7f8aadda): se contrastaron los códigos de operación, mantenimiento, mentoría y conocimiento con T-14. El puente de 9.336 HH queda trazado a 9.3.1 y el tramo de transición de M21 a los paquetes operativos correspondientes. Las referencias a apartados del SD8 conservan la numeración de ese documento.
- SD8 (2eb5eea4): la Tabla 7.4 «Horas hombre programadas por etapa» queda en la página 17 de SD7. El total de 3.072 HH de reserva protegida concuerda con las 1.152 HH de marcha blanca E1 más las 1.920 HH de producción y estabilización E1.
- SD6 (85f83505), SD11 (65a89608) y SD12 (a33dea8e): el contraste de aceptación, restauraciones y asignación por rol resultó conforme. El diccionario T-14 y la tabla de asignación de SD12 coinciden en 63 paquetes para SRE, 33 para JP, 33 para Implantación, 27 para Desarrollo, 20 para Arquitectura, 19 para Calidad, 18 para Seguridad y 17 para Datos.
- El control de Excel y E2 queda en la nota de HH mensuales. La curva contiene 56 filas y su acumulado es 203.548,63 HH. El presupuesto de la EDT conserva 203.548,62 HH.
- Se repitió la generación de la red. Coincidieron sus archivos de datos, las tablas de hitos y CPM, las 171 ventanas por código y los archivos .gan nominales, con el mismo inventario de 230 paquetes y la misma línea base.

## Cierre de observaciones de la revisión final

### Emisión y fuentes de cálculo

- Fecha de emisión de la oferta: 25 de noviembre de 2026. El SD6 de la referencia local
  `origin/LafroX-Subdoc6-LateX-corrigiendo` (da5be2fb) fija esa fecha en su portada y en
  la clase de la que heredan T-9 y T-10. SD7, Anexos, T-14, T-15 y T-18 la declaran
  en sus archivos de portada. La revisión de SD7 parte de e977124f con los cambios
  de cierre de esta revisión.
- El CPM lógico y la simulación se reproducen con
  `python -B revision/cpm_y_riesgo_sd7.py --output-dir tmp/sd7-implementar/cpm`.
  Su JSON conserva las fechas tempranas, tardías y niveladas, las holguras, la semilla
  PERT y los escenarios con subsanación. Los resultados dependen de las estimaciones
  y disponibilidades vigentes. El recálculo no sustituye la carta nivelada.
- Los controles quincenales se generan con
  `python -B revision/controles_construccion_sd7.py --output-dir tmp/sd7-implementar/controles`.
  La exportación CSV de GanttProject 3.3 confirmó las fechas y duraciones de las 292
  filas originales y los 35 hitos añadidos. El detalle conserva sus ID anteriores.

### Foliación para la integración de la oferta

El compilador del bloque recibe el folio inicial mediante un envoltorio LaTeX
como el siguiente. El resultado local habitual conserva su numeración propia.

    \def\LFXprimerfolio{137}
    \input{LAFROX-Subdocumento7.tex}

Compilar el envoltorio con LuaLaTeX hasta estabilizar sus índices. El integrador
asigna a cada archivo el siguiente folio disponible según su orden en la oferta
y valida las páginas impresas, el índice maestro y los enlaces del consolidado.
El mismo procedimiento se puede ejecutar con `revision/compilar_local_sd7.ps1 -FirstFolio 137`.
El 137 es un ejemplo. Usar el primer folio efectivo que entregue el integrador.
La prueba con Anexos y T-18 verificó los folios impresos 137–163 y 164–188, respectivamente.

### Evidencia necesaria para actualizar la matriz

- La consulta de la Contraparte sobre H7/H12 permanece preparada en este registro.
  El escenario de diez días de subsanación lleva H1 al 07-04-2027 y H12 al
  07-11-2028. H7 llega al 31-05-2028 sin margen. La tabla de T-15 fija además
  la última fecha de ingreso compatible con ambos plazos, para evaluar alternativas.
- Calidad requiere los turnos disponibles de sus titulares y refuerzos; Dirección
  confirma sus dedicaciones con SD1, SD12 y T-8. La ampliación de mesa nocturna
  suma 552 HH propuestas en los meses 16–19, separadas de la base de 9.336 HH.
  Antes de activarla se confirma la asignación por turno y la imputación de las HH.
- El ensayo de reversión debe dejar listos los 96 despachos a las 05:25 como
  máximo. El tiempo registrado determina si la decisión provisional de las
  04:30 es suficiente. Se conserva la evidencia del ensayo y la conformidad del
  responsable de Operaciones.
- El alcance de la cascada con controles quincenales se presenta al evaluador
  para su aceptación. Los responsables de cada materia registran la revisión
  humana técnica cuando la ejecuten, con fecha, comprobaciones y evidencia.

### Escenarios de recuperación y decisiones pendientes

| Observación | Evidencia de cierre | Responsable propuesto |
| --- | --- | --- |
| 20–21 · H1 | Aprobar la ventana del 22-02 al 02-03-2027 para 1.2.2, 1.2.3, 1.2.4 y 2.1.3. El modelo conserva las precedencias y supera el contraste diario de Calidad. El acta con subsanación cae el 31-03. Antes de cambiar la base, conciliar febrero y marzo, confirmar la capacidad de JP/PMO y acreditar los cuatro entregables. | JP, PMO y Calidad |
| 20–21 · H7/H12 | Registrar en 1.1.3 la respuesta escrita sobre expediente integrado, plazo, firma, corte y evidencia de 6.8.6. H7 conserva ingreso el 02-05 y corte el 31-05 con subsanación. Para H12, el ingreso el 28-09 requiere cerrar cuatro semanas el 27-09, adelantar 9.5.4 y confirmar si 6.8.6 se admite antes de firmar. Si esa ventana no es viable, obtener un procedimiento compatible con el límite de octubre y volver a simular. | JP y Contraparte Técnica |
| 15 y 18 · Dotación | Aprobar el registro con titular, suplente, perfil, fecha, turno, HH disponibles, HH en otros servicios y paquete. Calidad verifica el mínimo de 1.049,60 HH y la cobertura de cada día. Dirección cruza asignación y dedicación con SD1, SD12 y T-8. | Calidad y Dirección |
| 22 y 27 · Reservas y mesa | Aprobar titular, suplente e imputación del tramo 22:00–04:00. Nivelar por paquete, perfil y mes, y conciliar el costo con SD8 antes de activar la cobertura. | Mesa, JP y Dirección |
| 26 · Reversión | Conservar horas de decisión y restauración, hora del último despacho listo, guías ERP, conciliación y conformidad. Repetir antes del corte si los 96 no están listos a las 05:25. | Operaciones y Calidad |
| 07 y 12 · Método y PERT | Registrar la aceptación de los controles quincenales o programar el alcance, prueba y demo de cada incremento solicitado. Para cada paquete que usa un rango genérico, registrar las cantidades, los escenarios O/M/P y su fuente, con responsable de estimación. Recalcular la red tras aprobar los cambios. | Evaluador y líderes de frente |
| 40 y 42 · Oferta final | Aplicar folios consecutivos con el orden de la oferta completa, validar índice y enlaces, y archivar por sección revisor, fecha, comprobación y evidencia de la revisión técnica. | Integrador y líderes técnicos |

El cálculo de H1 obtiene el mismo mínimo agregado, nueve equivalentes de la familia JP, al contrastar las ventanas de la carta actual y de la alternativa. La verificación de flujo por familia se limita a los paquetes con entregable. El registro nominal debe conciliar la capacidad por perfil y el trabajo continuo antes de autorizar el traslado.

El JSON del CPM identifica los 24 paquetes con fundamento PERT específico y los 147 que requieren documentar escenarios propios. Priorizar los que condicionan H1, H7, H12 y la certificación previa al H5. Conservar el inventario regenerado junto con los insumos de estimación.
