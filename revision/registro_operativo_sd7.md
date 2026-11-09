# LafroX — Registro interno de dotación y calibración del SD7

El T-15 conserva 220.023 HH. La búsqueda en los subdocumentos disponibles y sus versiones CORRIGIENDO identificó capacidades de planta, reglas de cobertura y refuerzos propuestos; no identificó una nómina por turno con disponibilidad aprobada ni un registro de HH medidas por actividad. Este registro organiza la asignación y la medición sin atribuir disponibilidad ni resultados a personas concretas.

| Frente | Plazas y ventana que deben asignarse | Comprobación antes de autorizar |
| --- | --- | --- |
| Calidad, 3.8.2–3.8.5 | Del 25-10 al 11-11-2027, 13 plazas: dos para función 16 y once para función 19; procedencia prevista: diez de planta y tres de refuerzo. Del 12-11 al 19-11, hasta diez plazas para terminar 3.8.2 y 3.8.3. | El responsable registra la persona y la franja de cada plaza; comprueba los recursos compartidos por prueba y la ausencia de doble asignación. Máximo diario: 81,6 HH frente a 83,2 HH en el tramo crítico. |
| Infraestructura, mes 6 | Dos jornadas de apoyo de 6,4 HH en ambientes u observabilidad (funciones 14/29), sin usar los relevos de NOC, N1 o SOC. | Infraestructura ubica las jornadas en los días de concurrencia efectiva. El contraste mensual arroja 9,77 HH de exceso; las dos jornadas aportan 12,8 HH. |
| Implantación | Dos puestos de bodega 22:00–06:00, tres de plataformas según ola, siete de ruta según salida y uno de coordinación. Capacitación y despliegue se asignan por separado. | Cruzar persona, sitio y turno con la jornada en ruta, la ventana de bodega y los servicios continuos. Distinguir puestos simultáneos y personas de relevo. |
| Servicios continuos | NOC, Mesa N1 y SOC por cobertura del calendario; restantes actividades por ocurrencia o quincena. | Conciliar cada turno y su relevo con las 59 partidas continuas y con la carga de paquetes con entregable. |

Por cada plaza, registrar: identificador interno de la persona, competencias habilitadas, función, paquete, fecha, hora de inicio y fin, HH disponibles tras otros compromisos y responsable que autoriza. Consolidar por persona y fecha incluso cuando cambie de función.

## Asignación operativa por código de puesto

Estos códigos identifican plazas de programación, no personas contratadas ni una nómina confirmada.

| Puestos | Función | Asignación de jornada o turno |
| --- | --- | --- |
| CAL-P01 y CAL-P02 | 16: liderazgo y revisión técnica | Jornada diurna de certificación del 25-10 al 19-11-2027, en las 19 jornadas hábiles del T-15. Se reparte entre ambas plazas por igual la carga diaria de función 16: **96 HH por plaza** en total. CAL-P01 conserva la aprobación y CAL-P02 ejecuta las revisiones y coordinación asignadas. |
| CAL-P03 a CAL-P10 | 19: ejecución y automatización | Misma jornada diurna en los 19 días. Atienden 3.8.2–3.8.5 hasta el 11-11 y solo 3.8.2–3.8.3 en los seis días restantes. |
| CAL-R01 a CAL-R03 | 19: refuerzos de certificación | Jornada diurna del 25-10 al 11-11-2027, trece jornadas de hasta 6,4 HH efectivas por plaza. Uso exclusivo en certificación en esas franjas. |
| SRE-R01 | Apoyo de infraestructura, función 29 | Dos jornadas diurnas, **1 y 2 de julio de 2027**, en el escenario por capacidad de la sección 5. Apoya configuración de dispositivos de 3.2.6, con 6,4 HH por jornada, dentro de sus HH estimadas. Estas fechas corresponden al escenario de capacidad, no a la carta base. |
| IMP-B01 y B02 | 26: apoyo de bodega | Un puesto en Talca y uno en Concepción, turno 22:00–06:00, durante las jornadas de acompañamiento reforzado del T-18. |
| IMP-X01 a X03 | 27: plataformas | Un puesto por plataforma, en la recepción de madrugada y el despacho de la mañana de su ola. |
| IMP-R01 a R07 | 28: acompañamiento en ruta | Un puesto por salida asignada, según itinerario y ola. No se asignan a bodega ni a la mesa en la misma franja. |
| IMP-C01 | 21: coordinación | 160 HH durante cuatro semanas de acompañamiento. Coordina relevos y traspasos; capacitación y despliegue se registran por separado. |

El cuadro diario generado por el script fija la carga de cada prueba y función. La función 19 se reparte entre sus once plazas en el tramo crítico y entre las ocho de planta después, con un máximo de 6,4 HH por plaza al día. Las pruebas que comparten equipo, ambiente o apoyo se calendarizan en franjas separadas dentro de la jornada. Los relevos de NOC, Mesa N1 y SOC conservan sus propios turnos de servicio y no cubren los puestos de esta tabla.

## Responsabilidad y cobertura nominal

| Frente | Responsable de asignar y controlar | Puestos de ejecución |
| --- | --- | --- |
| Certificación de Calidad | Líder de Calidad y Pruebas, función 16. CAL-P01 mantiene la aprobación y CAL-P02 apoya las revisiones. | CAL-P01 a P10; CAL-R01 a R03 en el tramo crítico. |
| Apoyo de Infraestructura | Líder de Operación/SRE, función 24. El T-14 identifica a Guillermo Castillo como gerente de servicio en Operación, meses 21–56; esa dedicación no se usa como disponibilidad para las jornadas del mes 6. | SRE-R01, función 29, días 1 y 2 de julio de 2027 en el escenario de capacidad. |
| Acompañamiento de Implantación | Líder de Implantación y Gestión del Cambio, función 21, a cargo de IMP-C01 y del cuadro de relevos. | IMP-B01/B02, IMP-X01 a X03 e IMP-R01 a R07, con las ventanas de la tabla anterior. |
| NOC, Mesa N1 y SOC | Gerencia de Servicio coordina la cobertura; el Encargado de Seguridad controla el turno SOC. | Operadores y relevos de cada servicio, separados de certificación e implantación. |

La asignación de una persona a un código requiere cruzar su especialidad, jornada y otros compromisos. La sección de organización del SD1 corregido no constituye un registro de disponibilidad por turno. Las nominaciones de una versión anterior no se trasladan automáticamente a los turnos de este escenario.

## Mediciones para validar los supuestos de esfuerzo

| Familia de medición | Actividades de referencia | Datos que se registran |
| --- | --- | --- |
| Software | 3.4.1 recepción; 3.4.6 preventa sin conexión; 3.5.3 portal de transportistas. | Requisitos aceptados por tipo, complejidad e interfaces; HH directas, integración, pruebas y reproceso. |
| Migración e integración | 3.7.1–3.7.4 y 3.6.5–3.6.6. | Volumen tratado o mensajes comprobados, HH efectivas, repeticiones y tiempos de espera por contraparte por separado. |
| Calidad | 3.8.2–3.8.5. | Casos ejecutados, datos/ambiente, HH de ejecución y coordinación, regresiones y reprocesos. |
| Infraestructura e implantación | Instalaciones y olas del T-14/T-18. | Equipos o puestos cubiertos, jornadas, HH efectivas y pérdidas de capacidad por incidencias o turnos. |

La razón observada es HH efectivas divididas por unidades aceptadas, con el alcance y la fuente registrados. Las esperas se usan para recalcular duración cuando corresponda; no se suman como esfuerzo ejecutado. Los valores O/M/P se contrastan con el trabajo comparable y los reprocesos registrados. Sin una medición aprobada se conserva el escenario PERT como contraste, sin reemplazar la línea base.

El script `contrastar_esfuerzo_capacidad_sd7.py` genera el cuadro de las 19 jornadas de Calidad, las tres estimaciones por paquete y el cuadro mensual en el directorio temporal. Las 1.280 HH de las cuatro pruebas se conservan: 1.056 en el intervalo crítico y 224 en las seis jornadas siguientes.

## Evidencia para aprobación interna

Reejecutado el cálculo sobre las fuentes actuales: 227 paquetes y 220.023 HH conciliadas. Calidad utiliza como máximo 81,6 de las 83,2 HH diarias de las plazas previstas; Infraestructura requiere 9,77 HH adicionales de capacidad en el mes 6 y el refuerzo previsto aporta 12,8 HH. Son comprobaciones de capacidad bajo las plazas del plan, no de disponibilidad efectiva.

Para cerrar dotación, el responsable confirma el registro de asignación por persona y turno, incluidos refuerzos de Calidad e Infraestructura, Implantación y servicios continuos, y documenta la comprobación de solapamientos. La evidencia de cierre es el registro aprobado, con su responsable, fecha y ubicación.

Para cerrar el criterio de planificación, el responsable puede aprobar 220.023 HH como línea base y 213.877,67 HH como contraste PERT. La aprobación de este criterio no equivale a validar productividad observada ni a adoptar el escenario como nueva línea base. Para adoptar el escenario se necesitan las mediciones comparables y el recálculo de fechas, capacidad y costeo descritos arriba.
