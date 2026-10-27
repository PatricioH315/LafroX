# Formulario T-15 — Cronograma y asignación de recursos

> Texto extraído del [PDF final](LAFROX-Formulario-T-15.pdf). Las figuras y la composición visual se consultan en el PDF.

LafroX SpA
LICITACIÓN PÚBLICA
Licitación N.° TFEP-01/2026
Proyecto de Plataforma Digital de Misión Crítica
Caso — Logística
Sobre N.° 2 — Oferta Técnica
Propuesta Técnica
Formulario T-15 — Nivelación de Recursos
Subdocumento 07 · Formulario T-15
MANDANTE
Distribuidora Puelche S.A.
PROPONENTE
LafroX SpA
RUT 77.418.902-K
Av. Brasil 2241, Valparaíso
REPRESENTANTE LEGAL
Alex Aravena
Jefe de Proyecto y Apoderado
contacto@lafrox.cl
+56 32 250 4100
FECHA DE EMISIÓN
12 de octubre de 2026
FIRMA DEL REPRESENTANTE LEGAL
Alex Aravena
Jefe de Proyecto y Apoderado · LafroX SpA
LAFROX-Formulario-T-15.pdf 1


---

LafroX SpA
Índice general
Índice general 2
Lista de tablas 3
Lista de figuras 4
Formulario T-15: Nivelación de recursos 5
1 Método de estimación y de programación 5
1.1 Estimación 5
1.2 Programación 5
2 Ruta crítica y holguras 6
3 Frentes de trabajo y solapamientos 7
4 Modelo cuantitativo de recursos 10
4.1 Supuestos y cálculo 10
4.2 Horas por los 227 paquetes 13
4.3 Resumen T-15 29
4.4 Curvas mensuales: horas por etapa y personas por rol 31
4.5 Reservas de contingencia y de gestión 41
5 Red agregada, restricciones y escenarios de calendario 41
5.1 Cálculo reproducible 41
5.2 Lectura de las secuencias y las restricciones 55
5.3 Reservas y análisis PERT de duración 55
5.4 Gobierno 57
5.5 Presentación de entregables y revisión del CLIENTE 57
5.6 Medición de los niveles de atención 59
5.7 Dotación requerida, roles mínimos y dotación declarada 59
6 Lista de actividades: regla del 8/80 y del período de reporte 62
6.1 Paquetes con entregable y planificación gradual 63
6.2 Paquetes de esfuerzo continuo 92
Referencias 99
LafroX SpA
Formulario T-15
Media firma: Alex Aravena
2


---

LafroX SpA
Lista de tablas
Tabla 1 Frentes de trabajo. 8
Tabla 2 Supuestos y cálculo. 12
Tabla 3 Horas por los 227 paquetes. 15
Tabla 4 Resumen T-15. 30
Tabla 5 Curva mensual de horas por etapa. 32
Tabla 6 Curva mensual de personas por rol. 37
Tabla 7 Fechas tempranas, tardías y holguras de los 168 paquetes con entregable. 44
Tabla 8 CPM y PERT de los hitos con la línea base de 220.023 HH. 56
Tabla 9 Secuencia de cierre, producción y aceptación. 58
Tabla 10 Dotación requerida, roles mínimos y dotación declarada. 60
Tabla 11 Programación de los paquetes con entregable. 66
Tabla 12 Actividades de los paquetes que terminan hasta el H2. 77
Tabla 13 Actividades de los paquetes que terminan hasta el H2. 83
Tabla 14 Actividades de los paquetes de esfuerzo continuo. 93
LafroX SpA
Formulario T-15
Media firma: Alex Aravena
3


---

LafroX SpA
Lista de figuras
Figura 1 Camino que controla el H12 y su holgura contractual. 7
Figura 2 Frentes de trabajo de los meses 1 a 21 y solapamientos del artículo 17.2 de las
Bases Administrativas (p. 13). 9
Figura 3 Planificación gradual del cronograma. 64
LafroX SpA
Formulario T-15
Media firma: Alex Aravena
4


---

Formulario T-15: Nivelación de recursos
Este formulario presenta la información de planificación que pide el Formulario T-15 de
las Bases Administrativas para el Subdocumento 7: el método con que se estiman las horas
hombre de cada paquete, la programación sobre la red de dependencias, la ruta crítica y sus
holguras, y los frentes de trabajo, con el detalle de los solapamientos de los meses 13 a 15 y 19 a
20. Los paquetes de trabajo son los de la EDT del Formulario T-14. Este formulario no contiene
precios ni costos (artículo 50.2 de las Bases Administrativas (p. 29)).
En este formulario, BA, BTT y Caso designan las Bases Administrativas, las Bases Técnicas
Transversales y las Bases Técnicas del caso.
1 Método de estimación y de programación
La estimación y la programación siguen el PMBOK y la técnica PERT, de modo que cada
duración y cada holgura se puedan reconstruir a partir de valores declarados.
1.1 Estimación
El esfuerzo de cada paquete se estima con tres valores en horas hombre (Project Manage-
ment Institute [PMI], 2017, p. 201): el optimista (O), que corresponde al mejor escenario; el más
probable (M), con recursos y productividad realistas; y el pesimista (P), que corresponde al
peor escenario. La incertidumbre de cada estimación se representa con una distribución beta,
que el PMBOK admite entre las distribuciones para modelar la incertidumbre (PMI, 2017, p.
432). Con ella, la técnica PERT calcula el valor esperado y la desviación (Malcolm et al., 1959):
T_E = (O + 4M + P) / 6; 𝜎 = (P − O) / 6.
La p. 201 del PMBOK presenta también la distribución triangular, (𝑂+𝑀+𝑃)/3. Se usa la beta
porque pondera más el valor más probable, que se funda en los requerimientos y cantidades
de cada paquete.
Las bases de cada estimación se declaran por tipo de paquete. Los módulos y las inte-
graciones se estiman con los requerimientos del Formulario T-12 asignados al paquete; la
infraestructura, con las cantidades del Formulario T-11; la implantación y la capacitación, con
las personas y rutas del caso y la dotación del Formulario T-18, sección 2.6; y la operación, con
los horarios de cobertura de los paquetes 8.1.1 y 8.1.2 y la periodicidad de los informes. Los
paquetes de la fase 8 son de esfuerzo continuo: su estimación es mensual y se multiplica por
los 36 meses de operación.
1.2 Programación
La duración se contrasta con esfuerzo, capacidad efectiva y dependencias. La sección 6
programa los paquetes y descompone en actividades de 8 a 80 HH, que caben en una quincena,
LafroX SpA
Formulario T-15
Media firma: Alex Aravena
5


---

LafroX SpA Formulario T-15: Nivelación de recursos
sólo los que terminan hasta el H2; los demás se detallan por planificación gradual antes de
cada fase. Las ventanas de la sección 4 son supuestos de asignación y la red agregada de la
sección 5 explicita el cálculo del calendario. Las dependencias entre paquetes están en el
Anexo 7.B del Subdocumento 7, y sobre esa red se aplica el método de la ruta crítica (PMI, 2017,
pp. 210–211): una pasada hacia adelante da el inicio y el fin tempranos; una pasada hacia atrás,
desde los meses fijos del artículo 17 de las Bases Administrativas (pp. 12–13), da el inicio y el
fin tardíos; la diferencia LS − ES es la holgura total; la holgura libre se calcula respecto del ES
de sus sucesores. Los hitos del Formulario E-25 son restricciones de fecha fija: un camino que
no llega a su hito tiene holgura negativa y obliga a replanificar.
La sección 5 calcula CPM y PERT sobre la línea base vigente de 220.023 HH e incorpora
las revisiones del CLIENTE como retardos. Las fechas fuente de la sección 6 se conservan; las
fechas calculadas se presentan aparte. La red agregada obtiene holguras no negativas y tres
días para H12, condicionadas a los supuestos de recursos y aceptación. La Tabla 9 identifica
por separado una incompatibilidad entre el plazo completo de revisión del cierre de marcha
blanca y las fechas objetivo de producción. Por ello, esas holguras no acreditan por sí solas
la viabilidad integral de la aceptación. La asignación nominal y la nivelación fina también
requieren validación.
2 Ruta crítica y holguras
La red de la sección 5 identifica como camino controlante del H12 el cierre de la marcha
blanca de la Etapa 2 (4.3.1), la preparación del acta 4.3.3 y los diez días hábiles de revisión del
CLIENTE. La garantía 4.3.4 se constituye en septiembre, en paralelo con la marcha blanca,
porque es un trámite financiero que no interviene sistemas y no tiene predecesoras; así no se
suma a la cadena del acta. El acta calculada cae el 25 de octubre de 2028 frente al límite del 31
de octubre: holgura contractual de tres días hábiles. La Tabla 8 conserva la diferencia entre
entrega y acta.
LafroX SpA
Formulario T-15
Media firma: Alex Aravena
6


---

LafroX SpA Formulario T-15: Nivelación de recursos
4.3.1 — Marcha blanca de la
Etapa 2
Meses 19 y 20
Cierre: 30 de septiembre de
2028
4.3.4 — Garantía
de correcto funcionamiento
7 días hábiles; 80 HH
13 al 25 de septiembre de 2028
4.3.3 — Preparación del acta de aceptación
7 días hábiles; 80 HH
Entrega calculada: 11 de octubre de 2028
Revisión del CLIENTE — Art. 18.3
10 días hábiles
Acta calculada: 25 de octubre de 2028
Figura 1 Camino que controla el H12 y su holgura contractual. Fuente: elaboración a partir del T-15, secciones
5.1–5.3 y 6.1.
La figura muestra la cadena que controla H12; las demás ramas se calculan en la Tabla 7. H7
y H12 tienen holguras contractuales de dos y tres días hábiles, y H8, de catorce. Los ciclos
de marcha blanca mantienen sus ventanas completas, sin utilizar sus cuatro semanas finales
como reserva.
La holgura se gestiona en las instancias de gobierno de la EDT: el avance de la ruta crítica
y de los caminos casi críticos se revisa en la reunión semanal y en el Comité de Proyecto
quincenal (paquetes 1.3.5 y 1.8.3); toda desviación que comprometa un hito se escala al Comité
Ejecutivo con su análisis de impacto (paquetes 1.4.3 y 1.8.2); y el informe mensual con valor
ganado avisa toda desviación mayor al 10 % con su plan dentro de cinco días hábiles (paquete
1.8.6).
3 Frentes de trabajo y solapamientos
Un frente de trabajo es un equipo con un responsable y un conjunto de cuentas de control
que avanza en paralelo con los demás. La Tabla 1 define los frentes a partir de la EDT del
Formulario T-14 y de los responsables de su diccionario. F3 se divide en los tres subfrentes
del Capítulo 3, sección 3.4.3 (Subdocumento 3): bodega y calidad (M1, M2, M5, M9 y M12);
preventa, rutas y reparto (M3, M4, M6 y M8); y datos y rendición (M7 y M10).
LafroX SpA
Formulario T-15
Media firma: Alex Aravena
7


---

LafroX SpA Formulario T-15: Nivelación de recursos
Tabla 1 Frentes de trabajo. Fuente: (Formulario T-14).
Frente Responsable Cuentas de control Meses activos
F1 Dirección, gobierno
y cumplimiento
Jefe de Proyecto 1.1 a 1.4, 1.6 a 1.9, 5.4.1
a 5.4.3, 8.4, 9
1 a 56
F2 Arquitectura, seguri-
dad y datos
Arquitecto de Solución,
con Seguridad y Datos
2.1 a 2.6, 3.3, 3.7, 3.11 1 a 21
F3 Construcción y co-
rrecciones E1
Líder de Desarrollo 3.4, 3.6.1 a 3.6.4, 3.10.1
a 3.10.3; capacidad
protegida 4.2.2
1 a 20
F4 Construcción de la
Etapa 2
Líder de Desarrollo 3.5, 3.6.5, 3.6.6, 3.10.4 13 a 20
F5 Plataforma, infra-
estructura y soporte
puente
Líder de Operación /
SRE
3.1, 3.2, 5.1 a 5.3, 6.1 a
6.6; soporte 4.2.2
1 a 20
F6 Calidad y pruebas Líder de Calidad 1.5, 3.8, 3.9 1 a 21
F7 Implantación y ges-
tión del cambio
Líder de Implantación y
Gestión del Cambio
4.1 a 4.3, 7.1 a 7.3 2 a 21: diagnóstico
del cambio en 2–6,
preparación desde el 8 y
piloto de frío en 10–11
F8 Operación y soporte Líder de Operación /
SRE
8.1 a 8.3, 8.5 21 a 56
Los frentes se sincronizan en los hitos del Formulario E-25 y en los comités del artículo 71
de las Bases Administrativas (p. 37), cuyas actas registran los acuerdos entre frentes (paquetes
1.8.2 a 1.8.5). La Figura 2 presenta su ventana de actividad entre los meses 1 y 21.
LafroX SpA
Formulario T-15
Media firma: Alex Aravena
8


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
2027
1
feb
2
mar
3
abr
4
may
5
jun
6
jul
7
ago
8
sep
9
oct
10
nov
11
dic
2028
12
ene
13
feb
14
mar
15
abr
16
may
17
jun
18
jul
19
ago
20
sep
21
oct
Mes contractual →
Hitos del Formulario E-25
H1 H2 H3 H4
H6
H7
H8
H9
H10
H11
H12
F1 Dirección, gobierno y cumplimiento
Jefe de Proyecto · meses 1 a 56
→ hasta
el mes
56
F2 Arquitectura, seguridad y datos
Arquitecto de Solución · meses 1 a 21
F3 Construcción y correcciones E1
Líder de Desarrollo · meses 1 a 20 4.2.2 capacidad protegida
F4 Construcción de la Etapa 2
Líder de Desarrollo · meses 13 a 20
F5 Plataforma, infraestructura y soporte
puente 4.2.2 soporte puente
F6 Calidad y pruebas
Líder de Calidad · meses 1 a 21
F7 Implantación y gestión del cambio
Líder de Implantación y GC · meses 9 a 21
F8 Operación y soporte
Líder de Operación / SRE · meses 21 a 56
8.1–8.3,
8.5:
desde el
mes 21
hasta el
56
Solapamiento · meses 13 a 15 Solapamiento · meses 19 y 20
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
Leyenda Ventana del frente (Tabla T15.1) Cuentas de control activas (GanttPRO) Capacidad protegida / soporte puente 4.2.2
Solapamiento de etapas (Art. 17.2) Septiembre y diciembre (sin pasos a producción) Hito del Formulario E-25 (en su mes contractual)
H5
Líder de Operación / SRE · meses 1 a 20
Figura 2 Frentes de trabajo de los meses 1 a 21 y solapamientos del artículo 17.2 de las Bases Administrativas (p. 13). Fuente: elaboración a partir de la Tabla 1 y
(Formulario T-14).
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
9


---

LafroX SpA Formulario T-15: Nivelación de recursos
En los meses 13 a 15 trabajan a la vez F7, en la marcha blanca de la Etapa 1; F3, en las
correcciones de esa marcha blanca; F4, en el desarrollo de la Etapa 2; F6, en las pruebas de
ambas etapas; y F1 y F2. F3 y F4 dependen del mismo rol, el Líder de Desarrollo, y por eso
son equipos distintos: el equipo que atiende la marcha blanca no puede ser el que desarrolla
la Etapa 2 (artículo 17.2 de las Bases Administrativas (p. 13), punto 1). En los meses 19 y 20
trabajan F7, en la marcha blanca de la Etapa 2; F4, en sus correcciones; F6; y el soporte de la
Etapa 1 en producción.
4 Modelo cuantitativo de recursos
Base de cálculo: estimación por clases de tamaño trazable al T-12 y al T-11, que se recalcula
con el equipo al establecer la línea base y que el Capítulo 8 usa para cuantificar los riesgos. La
productividad y la dotación se contrastan con el avance real en cada Comité de Proyecto.
4.1 Supuestos y cálculo
Los supuestos y el cálculo del modelo de recursos son los siguientes.
• Capacidad nominal asumida: 160 HH/persona-mes; disponibilidad programable 80 %;
capacidad efectiva 128 HH. El 20 % cubre ausencias y coordinación no imputada. No es
una jornada contractual ni un cálculo de cumplimiento laboral.
• Esfuerzo inicial por clase y paquete: G gestión/acta 80 HH; E diseño/configuración/inno-
vación 240 HH; D módulo 960 HH; I integración/migración 480 HH; V prueba 320 HH
(integración y cierres de certificación: 160 HH); T instalación/capacitación 160 HH. Las
clases de tamaño se fundan en los requerimientos del T-12 y en las cantidades del T-11, y se
recalculan con el equipo al establecer la línea base. La tabla al final de esta sección explica
qué contiene cada clase.
• R identifica esfuerzo recurrente mensual, incluidos equivalentes mensuales de actividades
anuales/semestrales: la distribución contable no cambia la frecuencia de ejecución del
T-14.
• A identifica acompañamiento: 13 puestos simultáneos de terreno/coordinación; 12 × 24
días × 8 horas + 160 HH de coordinación = 2.464 HH por cuatro semanas; soporte E1 meses
16–20 con previsión 2.464/1.312/544/544/544 HH para puestos 13/7/3/3/3, condicionada a
los indicadores del T-18. La estabilización 4.3.2 abarca desde el paso a producción de la
Etapa 2, el 5 de octubre de 2028, hasta el 30 de noviembre, según la carta Gantt del T-14;
sus cuatro semanas reforzadas empiezan después de la firma de H12: con el acta calculada
para el 25 de octubre de 2028 en la Tabla 8, el acompañamiento comienza el 26 de octubre,
termina el 22 de noviembre y ocupa 5 de sus 24 días de lunes a sábado en el mes 21 y 19
en el mes 22. A razón de 2.464/24 HH por día, la imputación es 513,33 HH en el mes 21
y 1.950,67 HH en el mes 22. La fecha es un supuesto de programación, sujeto a la firma
efectiva del CLIENTE; si cambia, se recalcula el reparto sin acortar las cuatro semanas.
LafroX SpA
Formulario T-15
Media firma: Alex Aravena
10


---

LafroX SpA Formulario T-15: Nivelación de recursos
• C identifica cobertura por horas-posición del calendario real, con el mes 1 en febrero de
2027 (Anexo 7.A). NOC (8.1.1) y SOC (8.1.5) mantienen un puesto 24×7 cada uno: días del
mes × 24, es decir 744 HH en un mes de 31 días, 720 en uno de 30 y 672 en febrero. La mesa
(8.1.2, primera línea de incidentes del artículo 78 de las Bases Administrativas (p. 40)) aplica
las posiciones del SD4 (Subdocumento 4), Anexo 4-W.7: 7 en la hora cargada y 2 en las otras
17 horas de 04:00 a 22:00, o 41 horas-posición por día de lunes a sábado, y desde el mes 25
un tercer agente en esas 17 horas, 58 horas-posición por día, con el que la dotación cubre
los tres niveles de servicio hasta 2.391 contactos al mes (SD4, Anexo 4-W.7); en septiembre y
diciembre se suman 6 horas-posición de 22:00 a 04:00 de lunes a sábado y 24 los domingos.
Así, un mes de 26 días de lunes a sábado exige 26 × 41 = 1.066 HH de mesa, y septiembre de
2028 exige 26 × 47 + 4 × 24 = 1.318 HH. El SOC es propio de LafroX y opera desde su Centro
de Operaciones en Valparaíso (RT-11.17; SD4, Anexo 4-W.7); sus HH se imputan aquí. Las
posiciones de la mesa provienen de un Erlang C con supuestos de demanda: no acreditan
abandono ni resolución al primer contacto, que se miden según la sección 5.6. La curva
dimensiona relevos con 128 HH efectivas.
• O = 0,75M; P = 1,25M; E = (O + 4M + P)/6 = M. Para A/C, O = M = P: no se reduce cobertura
por un escenario optimista. Los riesgos de demanda y ausencias se tratan separadamente.
• E se reparte uniformemente entre los meses inclusivos declarados como presupuesto preli-
minar, salvo las pruebas de certificación reprogramadas 3.9.2–3.9.7 y el acompañamiento
4.3.2, que se imputan por los días de ejecución de cada mes. Las ventanas relativas pueden
abarcar meses de reserva sin trabajo continuo: la Tabla 11 fija el inicio y fin de los paquetes
con entregable y el diccionario T-14 mantiene las restricciones de aceptación. Coincidir en
un mes no demuestra que una precedencia dentro del mes se haya satisfecho.
• La envolvente anterior calcula personas por rol/mes = techo(HH del rol / 128). Para la
ampliación de cadena de frío se agrega por separado techo(HH incrementales del rol /
128) a esa envolvente, reservando refuerzo propio sin presumir capacidad libre en equipos
anteriores. El presupuesto mensual de HH suma solo el trabajo estimado, no la capacidad
ociosa de ese redondeo; la curva de personas es una cota de asignación conservadora. El
cálculo reproducible y su base publicada se conservan en el registro de planificación del
T-15. Se suman techos por familia de trabajo dirigida por el rol; el responsable nominado
dirige el equipo, no ejecuta solo todas las HH. JP/ARQ y los otros códigos identifican equipos
con liderazgo y apoyo competente: un valor 5 en JP significa cinco personas equivalentes
de dirección/documentación, no cinco jefes de proyecto. La sección 5.7 compara la curva
con la dotación declarada y con los roles mínimos; antes de aprobar recursos se deben
asignar personas distintas con competencias y turnos verificables.
• Reserva protegida E1 en meses 13–20: dos desarrolladores y un QA, 256 HH DES + 128 HH
CAL/mes; no se presta a E2 ni se duplica como trabajo base.
• Soporte puente E1 meses 16–20: NOC + mesa con la misma regla de calendario que la ope-
ración (1.851, 1.786, 1.810, 1.851 y 2.038 HH; total 9.336 HH), imputado a 4.2.2 y financiado
dentro de implementación. El SOC opera desde el mes 13 por 8.1.5, porque la marcha
blanca ya trata datos reales. Operación contractual empieza en el mes 21.
LafroX SpA
Formulario T-15
Media firma: Alex Aravena
11


---

LafroX SpA Formulario T-15: Nivelación de recursos
• Las ventanas de la sección 4.2 reservan capacidad por mes; no son equivalentes a los días
efectivos de todas las actividades de la sección 6.1. Cuando el paquete empieza o termina
dentro de una ventana más amplia, los meses sin ejecución son margen de programación,
no trabajo adicional ni un cambio de alcance. Los planos 2.3.1/2.3.2 se hacen en el mes 1, la
especificación y compra 5.1.2 en el mes 2, la instalación 6.1.1–6.1.4 en el mes 3 y la recepción
6.1.5 en el mes 4 (D-09 a D-11). Los prototipos 2.6.2 terminan antes de la construcción
3.4 (D-05); la identidad 3.3.1 empieza después del plan de seguridad (D-06); los módulos
se programan con dependencias por interfaz (D-16, D-18 y D-19); y las certificaciones
empiezan al terminar su prueba de integración (D-21 y D-31). La actualización anual del
Plan de Reversibilidad 1.7.2 ocurre en el mes 15, primer aniversario de su entrega del mes
3; las siguientes son 8.1.4. El acompañamiento de salida 9.2.1 ocupa los meses 54 a 56 para
cubrir sus 90 días dentro del contrato.
La clase es una estimación por analogía y no una tarifa: fija el esfuerzo esperado de un paquete
típico de su tipo, y el equipo lo ajusta en la línea base.
La Tabla 2 presenta supuestos y cálculo.
Tabla 2 Supuestos y cálculo. Fuente: elaboración a partir de las secs. 4.1–4.4 de este formulario y de (Formulario
T-14, paquetes de trabajo).
Clase Qué contiene Esfuerzo Ejemplo y razón
G Documento o acta de
gestión con un respon-
sable y una revisión
80 HH 1.1.1 Acta de consti-
tución: dos personas
una semana, porque
formaliza decisiones ya
tomadas en la oferta
E Diseño, configuración
o especificación que
requiere análisis, elabo-
ración y revisión
240 HH 2.2.3 Plan de respuesta
a incidentes de segu-
ridad: análisis, elabo-
ración y revisión con
cuatro especialistas
continúa en la página siguiente
LafroX SpA
Formulario T-15
Media firma: Alex Aravena
12


---

LafroX SpA Formulario T-15: Nivelación de recursos
Tabla 2 — continuación
Clase Qué contiene Esfuerzo Ejemplo y razón
D Módulo funcional con
sus requerimientos del
T-12, contratos de in-
terfaz, construcción en
incrementos, pruebas e
integración en QA
960 HH M4 Rutas (3.4.7) y M5
Preparación (3.4.3) tie-
nen el mismo tamaño
porque concentran
reglas y pantallas com-
parables; un módulo
de catálogo más sim-
ple queda en la misma
clase, porque la clase
cubre el promedio de
los once módulos y la
diferencia se ajusta con
el equipo en la línea
base
I Interfaz o migración
con análisis de mues-
tras reales, contrato,
adaptador, pruebas de
falla y entrega
480 HH 3.3.2 ERP: interfaces sin
documentación (Caso
cap. 17.5), por eso exige
análisis con muestras y
pruebas de lentitud
V Prueba ampliada con
preparación de datos,
dos ciclos y regresión
320 HH (160 en integra-
ción y cierre)
3.8.4 Carga a 1,5 veces
el peak de septiembre
T Instalación o capacita-
ción con ejecución y
acta
160 HH 6.1.1 Coordinación de la
obra civil y piso técnico
de la sala
4.2 Horas por los 227 paquetes
La ampliación de frío agrega 1.200 HH: banco 2.4.3, 320 HH (pruebaV); mapeo 2.4.4, 240 HH
(diseño E); piloto 4.1.4, 320 HH (prueba V); compra 5.1.4, 240 HH (especificación E); contratos
5.3.4, 80 HH (gestión G). Reestima 1.280 HH adicionales en paquetes existentes: 480 HH en
3.4.4 para reglas, escaneos y disposición; 480 HH en 3.4.5 para Greengrass e ingesta satelital;
160 HH en 6.5.4 para instalación y recepción del kit; 80 HH en 7.1.3 para inducción y 80 HH en
7.2.4 para contingencia y ruptura. El incremento total es 2.480 HH, estimación por analogía con
las clases del formulario, sujeta a validación del equipo en la línea base; no es una medición
de trabajo ya ejecutado. El banco valida el prototipo antes de la construcción de la versión
integrada; sus pruebas se repiten sobre esa versión antes del piloto.
LafroX SpA
Formulario T-15
Media firma: Alex Aravena
13


---

LafroX SpA Formulario T-15: Nivelación de recursos
La tabla siguiente presenta las horas de cada paquete con sus tres estimaciones y su valor
esperado.
La Tabla 3 presenta horas por los 227 paquetes.
LafroX SpA
Formulario T-15
Media firma: Alex Aravena
14


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 3 Horas por los 227 paquetes. Fuente: elaboración a partir de las secs. 4.1–4.4 de este formulario y de (Formulario T-14, EDT).
EDT Clase Rol Meses O HH M HH P HH E HH
1.1.1 G JP 1–1 60.00 80.00 100.00 80.00
1.1.2 G JP 1–1 60.00 80.00 100.00 80.00
1.1.3 G JP 1–1 60.00 80.00 100.00 80.00
1.2.1 G ARQ 1–1 60.00 80.00 100.00 80.00
1.2.2 G IMP 1–3 60.00 80.00 100.00 80.00
1.2.3 G ARQ 1–4 60.00 80.00 100.00 80.00
1.2.4 G CAL 2–2 60.00 80.00 100.00 80.00
1.2.5 G ARQ 13–13 60.00 80.00 100.00 80.00
1.3.1 G JP 1–1 60.00 80.00 100.00 80.00
1.3.2 G JP 2–2 60.00 80.00 100.00 80.00
1.3.3 G JP 2–2 60.00 80.00 100.00 80.00
1.3.4 G JP 2–2 60.00 80.00 100.00 80.00
1.3.5 R JP 1–20 360.00 480.00 600.00 480.00
1.4.1 G JP 1–1 60.00 80.00 100.00 80.00
1.4.2 G JP 1–1 60.00 80.00 100.00 80.00
1.4.3 R JP 1–56 672.00 896.00 1120.00 896.00
1.5.1 G CAL 2–2 60.00 80.00 100.00 80.00
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
15


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 3 — continuación
EDT Clase Rol Meses O HH M HH P HH E HH
1.5.2 G CAL 6–20 60.00 80.00 100.00 80.00
1.6.1 G JP 2–2 60.00 80.00 100.00 80.00
1.6.2 R JP 1–20 120.00 160.00 200.00 160.00
1.7.1 G JP 3–3 60.00 80.00 100.00 80.00
1.7.2 G JP 15–15 60.00 80.00 100.00 80.00
1.8.1 R JP 1–20 240.00 320.00 400.00 320.00
1.8.2 R JP 1–56 336.00 448.00 560.00 448.00
1.8.3 R JP 1–20 180.00 240.00 300.00 240.00
1.8.4 R ARQ 1–56 336.00 448.00 560.00 448.00
1.8.5 R SRE 13–56 264.00 352.00 440.00 352.00
1.8.6 R JP 1–20 360.00 480.00 600.00 480.00
1.8.7 R JP 2–56 330.00 440.00 550.00 440.00
1.8.8 R JP 1–56 336.00 448.00 560.00 448.00
1.9.1 G SEG 1–1 60.00 80.00 100.00 80.00
1.9.2 G SEG 1–1 60.00 80.00 100.00 80.00
1.9.3 G SEG 2–2 60.00 80.00 100.00 80.00
1.9.4 R SEG 1–56 168.00 224.00 280.00 224.00
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
16


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 3 — continuación
EDT Clase Rol Meses O HH M HH P HH E HH
1.9.5 R JP 1–56 168.00 224.00 280.00 224.00
2.1.1 E ARQ 2–2 180.00 240.00 300.00 240.00
2.1.2 E ARQ 2–2 180.00 240.00 300.00 240.00
2.1.3 E DAT 2–2 180.00 240.00 300.00 240.00
2.1.4 E ARQ 13–13 180.00 240.00 300.00 240.00
2.2.1 E SEG 2–2 180.00 240.00 300.00 240.00
2.2.2 E SEG 3–10 180.00 240.00 300.00 240.00
2.2.3 E SEG 3–3 180.00 240.00 300.00 240.00
2.2.4 E SEG 2–2 180.00 240.00 300.00 240.00
2.3.1 E SRE 1–2 180.00 240.00 300.00 240.00
2.3.2 E SRE 1–2 180.00 240.00 300.00 240.00
2.3.3 E SRE 2–2 180.00 240.00 300.00 240.00
2.4.1 E ARQ 3–3 180.00 240.00 300.00 240.00
2.4.2 E ARQ 13–13 180.00 240.00 300.00 240.00
2.4.3 V SRE 3–3 240.00 320.00 400.00 320.00
2.4.4 E ARQ 4–4 180.00 240.00 300.00 240.00
2.5.1 E SRE 3–3 180.00 240.00 300.00 240.00
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
17


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 3 — continuación
EDT Clase Rol Meses O HH M HH P HH E HH
2.5.2 E SRE 3–3 180.00 240.00 300.00 240.00
2.6.1 E IMP 2–2 180.00 240.00 300.00 240.00
2.6.2 E IMP 3–3 180.00 240.00 300.00 240.00
2.6.3 E IMP 4–4 180.00 240.00 300.00 240.00
3.1.1 E SRE 5–5 180.00 240.00 300.00 240.00
3.1.2 E SRE 5–5 180.00 240.00 300.00 240.00
3.1.3 E SRE 5–5 180.00 240.00 300.00 240.00
3.1.4 E SRE 4–4 180.00 240.00 300.00 240.00
3.1.5 E SRE 5–5 180.00 240.00 300.00 240.00
3.2.1 E SRE 4–4 180.00 240.00 300.00 240.00
3.2.2 E SRE 4–4 180.00 240.00 300.00 240.00
3.2.3 E SRE 4–4 180.00 240.00 300.00 240.00
3.2.4 E SRE 4–4 180.00 240.00 300.00 240.00
3.2.5 E SEG 4–4 180.00 240.00 300.00 240.00
3.2.6 E SRE 5–5 180.00 240.00 300.00 240.00
3.3.1 I SEG 5–7 360.00 480.00 600.00 480.00
3.3.2 I ARQ 5–6 360.00 480.00 600.00 480.00
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
18


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 3 — continuación
EDT Clase Rol Meses O HH M HH P HH E HH
3.3.3 I ARQ 5–6 360.00 480.00 600.00 480.00
3.3.4 I ARQ 5–6 360.00 480.00 600.00 480.00
3.3.5 I ARQ 5–7 360.00 480.00 600.00 480.00
3.3.6 I ARQ 5–7 360.00 480.00 600.00 480.00
3.4.1 D DES 5–7 720.00 960.00 1200.00 960.00
3.4.2 D DES 5–7 720.00 960.00 1200.00 960.00
3.4.3 D DES 5–7 720.00 960.00 1200.00 960.00
3.4.4 D DES 5–8 1080.00 1440.00 1800.00 1440.00
3.4.5 D DES 5–7 1080.00 1440.00 1800.00 1440.00
3.4.6 D DES 5–7 720.00 960.00 1200.00 960.00
3.4.7 D DES 5–8 720.00 960.00 1200.00 960.00
3.4.8 D DES 5–8 720.00 960.00 1200.00 960.00
3.4.9 D DES 5–8 720.00 960.00 1200.00 960.00
3.4.10 D DES 5–9 720.00 960.00 1200.00 960.00
3.4.11 D DAT 8–8 720.00 960.00 1200.00 960.00
3.5.1 D DES 14–15 720.00 960.00 1200.00 960.00
3.5.2 D DES 14–15 720.00 960.00 1200.00 960.00
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
19


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 3 — continuación
EDT Clase Rol Meses O HH M HH P HH E HH
3.5.3 D DES 14–15 720.00 960.00 1200.00 960.00
3.5.4 D DAT 14–15 720.00 960.00 1200.00 960.00
3.6.1 I DAT 7–8 360.00 480.00 600.00 480.00
3.6.2 I DES 6–7 360.00 480.00 600.00 480.00
3.6.3 I DES 6–7 360.00 480.00 600.00 480.00
3.6.4 I DES 6–7 360.00 480.00 600.00 480.00
3.6.5 I DES 13–18 360.00 480.00 600.00 480.00
3.6.6 I DES 17–19 360.00 480.00 600.00 480.00
3.7.1 I DAT 7–9 360.00 480.00 600.00 480.00
3.7.2 I DAT 9–10 360.00 480.00 600.00 480.00
3.7.3 I DAT 11–11 360.00 480.00 600.00 480.00
3.7.4 I DAT 11–11 360.00 480.00 600.00 480.00
3.7.5 I DAT 12–12 360.00 480.00 600.00 480.00
3.8.1 V CAL 9–9 120.00 160.00 200.00 160.00
3.8.2 V CAL 9–10 240.00 320.00 400.00 320.00
3.8.3 V CAL 9–10 240.00 320.00 400.00 320.00
3.8.4 V CAL 9–10 240.00 320.00 400.00 320.00
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
20


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 3 — continuación
EDT Clase Rol Meses O HH M HH P HH E HH
3.8.5 V CAL 9–10 240.00 320.00 400.00 320.00
3.8.6 V SEG 9–10 240.00 320.00 400.00 320.00
3.8.7 V CAL 10–11 120.00 160.00 200.00 160.00
3.8.8 V SRE 9–10 240.00 320.00 400.00 320.00
3.9.1 V CAL 16–16 120.00 160.00 200.00 160.00
3.9.2 V CAL 17–17 240.00 320.00 400.00 320.00
3.9.3 V CAL 16–17 240.00 320.00 400.00 320.00
3.9.4 V CAL 16–17 240.00 320.00 400.00 320.00
3.9.5 V SEG 16–16 120.00 160.00 200.00 160.00
3.9.6 V CAL 17–17 120.00 160.00 200.00 160.00
3.9.7 V SRE 16–17 120.00 160.00 200.00 160.00
3.10.1.1 E DAT 7–9 180.00 240.00 300.00 240.00
3.10.1.2 E DAT 9–10 180.00 240.00 300.00 240.00
3.10.1.3 E DAT 9–10 180.00 240.00 300.00 240.00
3.10.1.4 E DAT 11–15 180.00 240.00 300.00 240.00
3.10.2.1 E CAL 2–3 180.00 240.00 300.00 240.00
3.10.2.2 E CAL 3–5 180.00 240.00 300.00 240.00
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
21


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 3 — continuación
EDT Clase Rol Meses O HH M HH P HH E HH
3.10.2.3 E CAL 5–10 180.00 240.00 300.00 240.00
3.10.2.4 E CAL 11–15 180.00 240.00 300.00 240.00
3.10.3.1 E DAT 3–5 180.00 240.00 300.00 240.00
3.10.3.2 E DAT 5–9 180.00 240.00 300.00 240.00
3.10.3.3 E DAT 9–10 180.00 240.00 300.00 240.00
3.10.3.4 E DAT 11–15 180.00 240.00 300.00 240.00
3.10.4.1 E IMP 13–14 180.00 240.00 300.00 240.00
3.10.4.2 E IMP 14–15 180.00 240.00 300.00 240.00
3.10.4.3 E IMP 15–17 180.00 240.00 300.00 240.00
3.10.4.4 E IMP 18–21 180.00 240.00 300.00 240.00
3.11.1 G ARQ 15–21 60.00 80.00 100.00 80.00
3.11.2 G SRE 10–20 60.00 80.00 100.00 80.00
3.11.3 G DES 4–20 60.00 80.00 100.00 80.00
3.11.4 G DES 4–20 60.00 80.00 100.00 80.00
3.11.5 G DES 6–20 60.00 80.00 100.00 80.00
4.1.1 G IMP 10–10 60.00 80.00 100.00 80.00
4.1.2 G IMP 11–11 60.00 80.00 100.00 80.00
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
22


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 3 — continuación
EDT Clase Rol Meses O HH M HH P HH E HH
4.1.3 G IMP 17–17 60.00 80.00 100.00 80.00
4.1.4 V IMP 10–11 240.00 320.00 400.00 320.00
4.2.1 A IMP 13–15 7392.00 7392.00 7392.00 7392.00
4.2.2 A IMP 16–20 5408.00 5408.00 5408.00 5408.00
4.2.3 G JP 16–16 60.00 80.00 100.00 80.00
4.3.1 A IMP 19–20 4928.00 4928.00 4928.00 4928.00
4.3.2 A IMP 21–22 2464.00 2464.00 2464.00 2464.00
4.3.3 G JP 21–21 60.00 80.00 100.00 80.00
4.3.4 G JP 20–20 60.00 80.00 100.00 80.00
5.1.1 G ARQ 2–2 60.00 80.00 100.00 80.00
5.1.2 G ARQ 2–2 60.00 80.00 100.00 80.00
5.1.3 G SRE 5–5 60.00 80.00 100.00 80.00
5.1.4 E ARQ 1–2 180.00 240.00 300.00 240.00
5.2.1 G SRE 2–2 60.00 80.00 100.00 80.00
5.2.2 G SRE 4–4 60.00 80.00 100.00 80.00
5.2.3 G ARQ 4–4 60.00 80.00 100.00 80.00
5.3.1 G SRE 4–4 60.00 80.00 100.00 80.00
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
23


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 3 — continuación
EDT Clase Rol Meses O HH M HH P HH E HH
5.3.2 G SRE 4–4 60.00 80.00 100.00 80.00
5.3.3 G SRE 4–4 60.00 80.00 100.00 80.00
5.3.4 G SRE 2–2 60.00 80.00 100.00 80.00
5.4.1 G IMP 9–12 60.00 80.00 100.00 80.00
5.4.2 G IMP 9–12 60.00 80.00 100.00 80.00
5.4.3 G JP 17–20 60.00 80.00 100.00 80.00
5.4.4 G JP 7–7 60.00 80.00 100.00 80.00
6.1.1 T SRE 3–3 120.00 160.00 200.00 160.00
6.1.2 T SRE 3–3 120.00 160.00 200.00 160.00
6.1.3 T SRE 3–3 120.00 160.00 200.00 160.00
6.1.4 T SRE 3–3 120.00 160.00 200.00 160.00
6.1.5 T SRE 4–4 120.00 160.00 200.00 160.00
6.2.1 T SRE 4–4 120.00 160.00 200.00 160.00
6.2.2 T SRE 6–6 120.00 160.00 200.00 160.00
6.2.3 T SRE 7–7 120.00 160.00 200.00 160.00
6.3.1 T SRE 4–5 120.00 160.00 200.00 160.00
6.3.2 T SRE 4–5 120.00 160.00 200.00 160.00
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
24


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 3 — continuación
EDT Clase Rol Meses O HH M HH P HH E HH
6.3.3 T SRE 4–4 120.00 160.00 200.00 160.00
6.3.4 T SRE 9–9 120.00 160.00 200.00 160.00
6.4.1 T SEG 5–5 120.00 160.00 200.00 160.00
6.4.2 T SEG 5–5 120.00 160.00 200.00 160.00
6.4.3 T SEG 5–6 120.00 160.00 200.00 160.00
6.5.1 T SRE 9–12 120.00 160.00 200.00 160.00
6.5.2 T SRE 10–12 120.00 160.00 200.00 160.00
6.5.3 T SRE 9–11 120.00 160.00 200.00 160.00
6.5.4 T SRE 8–12 240.00 320.00 400.00 320.00
6.5.5 T SRE 10–12 120.00 160.00 200.00 160.00
6.5.6 T SRE 9–12 120.00 160.00 200.00 160.00
6.6.1 T SRE 5–5 120.00 160.00 200.00 160.00
6.6.2 T SRE 5–5 120.00 160.00 200.00 160.00
6.6.3 T SRE 5–5 120.00 160.00 200.00 160.00
7.1.1 T IMP 10–12 120.00 160.00 200.00 160.00
7.1.2 R IMP 13–56 2112.00 2816.00 3520.00 2816.00
7.1.3 T IMP 11–20 180.00 240.00 300.00 240.00
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
25


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 3 — continuación
EDT Clase Rol Meses O HH M HH P HH E HH
7.1.4 T IMP 15–20 120.00 160.00 200.00 160.00
7.1.5 T IMP 10–18 120.00 160.00 200.00 160.00
7.1.6 T IMP 10–12 120.00 160.00 200.00 160.00
7.2.1 T IMP 10–16 120.00 160.00 200.00 160.00
7.2.2 T IMP 16–18 120.00 160.00 200.00 160.00
7.2.3 T IMP 2–6 120.00 160.00 200.00 160.00
7.2.4 T IMP 8–20 180.00 240.00 300.00 240.00
7.2.5 T IMP 13–21 120.00 160.00 200.00 160.00
7.3.1 T IMP 13–15 120.00 160.00 200.00 160.00
7.3.2 T IMP 18–18 120.00 160.00 200.00 160.00
8.1.1 C SRE 21–56 26280.00 26280.00 26280.00 26280.00
8.1.2 C SRE 21–56 54239.00 54239.00 54239.00 54239.00
8.1.3 V SRE 21–56 420.00 560.00 700.00 560.00
8.1.4 R JP 21–56 216.00 288.00 360.00 288.00
8.1.5 C SEG 13–56 32112.00 32112.00 32112.00 32112.00
8.1.6 R SRE 21–56 432.00 576.00 720.00 576.00
8.2.1 R DES 21–56 3456.00 4608.00 5760.00 4608.00
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
26


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 3 — continuación
EDT Clase Rol Meses O HH M HH P HH E HH
8.2.2 R SEG 21–56 864.00 1152.00 1440.00 1152.00
8.2.3 R SRE 21–56 864.00 1152.00 1440.00 1152.00
8.2.4 R DES 21–56 1728.00 2304.00 2880.00 2304.00
8.2.5 R SRE 21–56 216.00 288.00 360.00 288.00
8.2.6 R SRE 21–56 216.00 288.00 360.00 288.00
8.2.7 R SRE 21–56 648.00 864.00 1080.00 864.00
8.3.1 R CAL 21–56 432.00 576.00 720.00 576.00
8.3.2 R DAT 21–56 216.00 288.00 360.00 288.00
8.3.3 G JP 21–23 60.00 80.00 100.00 80.00
8.3.4 R JP 24–56 396.00 528.00 660.00 528.00
8.3.5 G IMP 22–26 60.00 80.00 100.00 80.00
8.3.6 G IMP 24–27 60.00 80.00 100.00 80.00
8.4.1 R SRE 21–56 432.00 576.00 720.00 576.00
8.4.2 R SRE 21–56 432.00 576.00 720.00 576.00
8.4.3 R SRE 21–56 216.00 288.00 360.00 288.00
8.4.4 R JP 21–56 216.00 288.00 360.00 288.00
8.5.1 R IMP 21–56 864.00 1152.00 1440.00 1152.00
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
27


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 3 — continuación
EDT Clase Rol Meses O HH M HH P HH E HH
8.5.2 G IMP 21–27 60.00 80.00 100.00 80.00
8.5.3 R SRE 21–56 432.00 576.00 720.00 576.00
9.1.1 G DES 21–21 60.00 80.00 100.00 80.00
9.1.2 G JP 21–22 60.00 80.00 100.00 80.00
9.2.1 G JP 54–56 60.00 80.00 100.00 80.00
9.2.2 G SEG 56–56 60.00 80.00 100.00 80.00
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
28


---

LafroX SpA Formulario T-15: Nivelación de recursos
Se agregan explícitamente soporte puente SRE de 4.2.2 = 9336.00 HH y reserva F3/QA = 8 ×
(256 + 128) = 3.072 HH. Las ocho restauraciones previas a Operación aportan 128 HH SRE: 48 en
4.2.1, 48 en 4.2.2 y 32 en 4.3.1. Cada una supone 16 HH para preparación, ejecución, validación
e informe. Son distintas de las 36 restauraciones de 8.1.6 durante Operación. Al activar los
respaldos antes del mes 13 se verificará si RT-07.12 exige pruebas mensuales adicionales; en
ese caso se programarán y reestimarán expresamente, sin imputarlas a las ocho ya contadas.
Las siete conmutaciones reales de 8.1.3 se estiman en 80 HH por campaña, 560 HH en total.
Las pruebas de intrusión E1 y E2 se estiman en 320 y 160 HH respectivamente; la reducción
en E2 exige que el inventario y los procedimientos de E1 sean reutilizables. Se confirmarán
horas, alcance y disponibilidad con el tercero independiente antes de ejecutar. Las 128 HH de
restauraciones se suman a las 207.487 HH de los 227 paquetes para formar las 207.615 HH de
base; el soporte puente y la reserva protegida se agregan por separado en las curvas siguientes.
4.3 Resumen T-15
La Tabla 4 resume las horas programadas por etapa contractual y añade el peak de la curva
conjunta en su período. El asterisco distingue esa cifra de la dotación exclusiva de una etapa:
los equipos comparten períodos y sus peaks no se suman. La columna se obtiene como máximo
de «Personas totales» de la Tabla 6 entre los meses indicados. Son personas equivalentes de
planificación, no simultaneidad diaria acreditada. El peak exclusivo de cada etapa requiere la
asignación detallada por actividad; no se deduce de HH acumuladas ni se presenta una cifra
inventada.
LafroX SpA
Formulario T-15
Media firma: Alex Aravena
29


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 4 Resumen T-15. Fuente: elaboración a partir de las secs. 4.1–4.4 de este formulario y de (Formulario T-14, EDT).
Etapa HH base y cobertura HH reserva protegida HH programadas Frentes Meses N.° personas
(peak)*
E1 Desarrollo 40569.48 0 40569.48 F1,F2,F3,F5,F6,F7 1–12 48
E1 Marcha blanca 11214.55 1152 12366.55 F1,F2,F3,F5,F6,F7 13–15 58
E2 Desarrollo 11406.54 0 11406.54 F1,F2,F4,F5,F6,F7 13–18 64
E2 Marcha blanca 7387.91 0 7387.91 F1,F2,F4,F6,F7 19–20 57
E1 Producción y estabili-
zación
14824.31 1920 16744.31 F3,F5,F6,F7 16–20 64
Operación 128853.67 0 128853.67 F1,F8 21–56 46
E2 Cierre y estabiliza-
ción posterior al H12
2694.54 0 2694.54 F1,F2,F4,F6,F7 21–22 46
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
30


---

LafroX SpA Formulario T-15: Nivelación de recursos
Total exacto de paquetes y componentes = 220023.00 HH (207.487 HH de los 227 paquetes +
128 HH de restauraciones previas a Operación + 9.336 HH de soporte puente + 3.072 HH de
reserva protegida); peak mensual conjunto = 64 personas equivalentes en el mes 16, cuando
coinciden el paso a producción de la Etapa 1 con su estabilización y soporte puente y las
pruebas de certificación de la Etapa 2. En el solapamiento de los meses 13 a 15 el máximo es de
58 personas, en el mes 14: la construcción de los cuatro módulos de la Etapa 2 se reparte en los
meses 14 y 15, con cinco personas por módulo como máximo, en lugar de concentrarse en abril.
La mesa y el SOC dimensionados en el SD4, aplicados sobre el calendario real, determinan las
horas de operación y de soporte puente. La implementación imputada a los meses 21 y 22 se
separa de Operación; las actividades generales que continúan como servicio permanecen en
Operación. Los peaks de etapas no se suman. Las centésimas de presentación se distribuyen
por mayor resto entre meses y se concilian por etapa; la suma publicada conserva 220.023 HH
exactas. La mesa de ayuda de 8.1.2 incluye desde el mes 25, cuando empieza el tercer año del
contrato y la demanda proyectada llega a 2.258 contactos al mes, un tercer agente en las franjas
de menor demanda (17 horas por día de lunes a sábado, 14.161 HH), con el que la dotación
base cubre los tres niveles de servicio hasta 2.391 contactos al mes (SD4, Anexo 4-W.7). En los
meses 21 a 24, con 2.000 contactos estimados, bastan dos agentes en esas franjas (límite 2.283).
4.4 Curvas mensuales: horas por etapa y personas por rol
La tabla siguiente presenta, mes a mes, las horas por etapa y las personas equivalentes por
rol.
La Tabla 5 presenta curva mensual de horas por etapa.
LafroX SpA
Formulario T-15
Media firma: Alex Aravena
31


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 5 Curva mensual de horas por etapa. Fuente: elaboración a partir de la sección 4.4 de este formulario.
Mes E1 desarrollo E1 MB E2 desarrollo E2 MB E1 producción
y estabiliza-
ción
Operación E2 cierre y
estabilización
posterior al
H12
Total HH
1 1535.81 0.00 0.00 0.00 0.00 0.00 0.00 1535.81
2 3109.52 0.00 0.00 0.00 0.00 0.00 0.00 3109.52
3 2681.67 0.00 0.00 0.00 0.00 0.00 0.00 2681.67
4 3382.78 0.00 0.00 0.00 0.00 0.00 0.00 3382.78
5 5271.21 0.00 0.00 0.00 0.00 0.00 0.00 5271.21
6 5567.52 0.00 0.00 0.00 0.00 0.00 0.00 5567.52
7 5339.82 0.00 0.00 0.00 0.00 0.00 0.00 5339.82
8 4795.32 0.00 0.00 0.00 0.00 0.00 0.00 4795.32
9 3426.38 0.00 0.00 0.00 0.00 0.00 0.00 3426.38
10 2169.70 0.00 0.00 0.00 0.00 0.00 0.00 2169.70
11 1953.48 0.00 0.00 0.00 0.00 0.00 0.00 1953.48
12 1336.27 0.00 0.00 0.00 0.00 0.00 0.00 1336.27
13 0.00 3959.16 788.57 0.00 0.00 0.00 0.00 4747.73
14 0.00 4340.25 2251.43 0.00 0.00 0.00 0.00 6591.68
15 0.00 4067.14 2125.71 0.00 0.00 0.00 0.00 6192.85
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
32


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 5 — continuación
Mes E1 desarrollo E1 MB E2 desarrollo E2 MB E1 producción
y estabiliza-
ción
Operación E2 cierre y
estabilización
posterior al
H12
Total HH
16 0.00 0.00 2468.35 0.00 4721.47 0.00 0.00 7189.82
17 0.00 0.00 2209.57 0.00 3504.46 0.00 0.00 5714.03
18 0.00 0.00 1562.91 0.00 2760.46 0.00 0.00 4323.37
19 0.00 0.00 0.00 3769.86 2785.46 0.00 0.00 6555.32
20 0.00 0.00 0.00 3618.05 2972.46 0.00 0.00 6590.51
21 0.00 0.00 0.00 0.00 0.00 3198.26 703.88 3902.14
22 0.00 0.00 0.00 0.00 0.00 3232.55 1990.66 5223.21
23 0.00 0.00 0.00 0.00 0.00 3440.54 0.00 3440.54
24 0.00 0.00 0.00 0.00 0.00 3247.92 0.00 3247.92
25 0.00 0.00 0.00 0.00 0.00 3341.50 0.00 3341.50
26 0.00 0.00 0.00 0.00 0.00 3688.21 0.00 3688.21
27 0.00 0.00 0.00 0.00 0.00 3585.83 0.00 3585.83
28 0.00 0.00 0.00 0.00 0.00 3635.78 0.00 3635.78
29 0.00 0.00 0.00 0.00 0.00 3529.78 0.00 3529.78
30 0.00 0.00 0.00 0.00 0.00 3577.78 0.00 3577.78
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
33


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 5 — continuación
Mes E1 desarrollo E1 MB E2 desarrollo E2 MB E1 producción
y estabiliza-
ción
Operación E2 cierre y
estabilización
posterior al
H12
Total HH
31 0.00 0.00 0.00 0.00 0.00 3635.78 0.00 3635.78
32 0.00 0.00 0.00 0.00 0.00 3741.78 0.00 3741.78
33 0.00 0.00 0.00 0.00 0.00 3729.11 0.00 3729.11
34 0.00 0.00 0.00 0.00 0.00 3529.78 0.00 3529.78
35 0.00 0.00 0.00 0.00 0.00 3853.78 0.00 3853.78
36 0.00 0.00 0.00 0.00 0.00 3635.78 0.00 3635.78
37 0.00 0.00 0.00 0.00 0.00 3317.78 0.00 3317.78
38 0.00 0.00 0.00 0.00 0.00 3577.78 0.00 3577.78
39 0.00 0.00 0.00 0.00 0.00 3623.11 0.00 3623.11
40 0.00 0.00 0.00 0.00 0.00 3635.78 0.00 3635.78
41 0.00 0.00 0.00 0.00 0.00 3471.78 0.00 3471.78
42 0.00 0.00 0.00 0.00 0.00 3635.78 0.00 3635.78
43 0.00 0.00 0.00 0.00 0.00 3635.78 0.00 3635.78
44 0.00 0.00 0.00 0.00 0.00 3741.78 0.00 3741.78
45 0.00 0.00 0.00 0.00 0.00 3729.11 0.00 3729.11
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
34


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 5 — continuación
Mes E1 desarrollo E1 MB E2 desarrollo E2 MB E1 producción
y estabiliza-
ción
Operación E2 cierre y
estabilización
posterior al
H12
Total HH
46 0.00 0.00 0.00 0.00 0.00 3529.78 0.00 3529.78
47 0.00 0.00 0.00 0.00 0.00 3853.78 0.00 3853.78
48 0.00 0.00 0.00 0.00 0.00 3635.78 0.00 3635.78
49 0.00 0.00 0.00 0.00 0.00 3317.77 0.00 3317.77
50 0.00 0.00 0.00 0.00 0.00 3577.77 0.00 3577.77
51 0.00 0.00 0.00 0.00 0.00 3623.10 0.00 3623.10
52 0.00 0.00 0.00 0.00 0.00 3635.77 0.00 3635.77
53 0.00 0.00 0.00 0.00 0.00 3471.77 0.00 3471.77
54 0.00 0.00 0.00 0.00 0.00 3746.88 0.00 3746.88
55 0.00 0.00 0.00 0.00 0.00 3599.99 0.00 3599.99
56 0.00 0.00 0.00 0.00 0.00 3888.44 0.00 3888.44
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
35


---

LafroX SpA Formulario T-15: Nivelación de recursos
La Tabla 6 presenta curva mensual de personas por rol.
LafroX SpA
Formulario T-15
Media firma: Alex Aravena
36


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 6 Curva mensual de personas por rol. Fuente: elaboración a partir de la sección 4.4 de este formulario.
Mes JP ARQ SEG DAT DES CAL SRE IMP Personas
totales
1 5 3 2 0 0 0 4 1 15
2 4 7 5 2 0 3 4 3 28
3 2 2 3 1 0 2 12 3 25
4 1 3 3 1 1 1 17 3 30
5 1 11 5 2 10 2 15 0 46
6 1 8 4 1 31 1 2 0 48
7 2 1 1 8 31 1 2 0 46
8 1 1 1 10 27 1 1 1 43
9 1 1 3 8 3 8 7 3 34
10 1 1 2 3 1 6 6 5 25
11 1 1 1 9 1 2 2 5 22
12 1 1 1 5 0 1 5 2 16
13 1 5 6 0 3 2 2 24 43
14 1 1 6 6 15 2 2 25 58
15 2 1 6 4 14 2 2 24 55
16 2 1 9 0 4 7 18 23 64
17 2 1 6 0 4 6 16 15 50
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
37


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 6 — continuación
Mes JP ARQ SEG DAT DES CAL SRE IMP Personas
totales
18 1 1 6 0 4 2 16 9 39
19 1 1 6 0 4 2 16 27 57
20 2 1 6 0 2 1 17 26 55
21 3 1 7 1 3 2 17 6 40
22 2 1 6 1 2 1 16 17 46
23 1 1 7 1 2 1 18 1 32
24 1 1 7 1 2 1 16 2 31
25 1 1 6 1 2 1 18 1 31
26 1 1 7 1 2 1 20 2 35
27 1 1 6 1 2 2 20 1 34
28 1 1 7 1 2 1 20 1 34
29 1 1 6 1 2 1 19 1 32
30 1 1 7 1 2 1 19 1 33
31 1 1 7 1 2 1 20 1 34
32 1 1 6 1 2 1 21 1 34
33 1 1 7 1 2 2 21 1 36
34 1 1 6 1 2 1 19 1 32
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
38


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 6 — continuación
Mes JP ARQ SEG DAT DES CAL SRE IMP Personas
totales
35 1 1 7 1 2 1 21 1 35
36 1 1 7 1 2 1 20 1 34
37 1 1 6 1 2 1 18 1 31
38 1 1 7 1 2 1 19 1 33
39 1 1 6 1 2 2 20 1 34
40 1 1 7 1 2 1 20 1 34
41 1 1 6 1 2 1 19 1 32
42 1 1 7 1 2 1 20 1 34
43 1 1 7 1 2 1 20 1 34
44 1 1 6 1 2 1 21 1 34
45 1 1 7 1 2 2 21 1 36
46 1 1 6 1 2 1 19 1 32
47 1 1 7 1 2 1 21 1 35
48 1 1 7 1 2 1 20 1 34
49 1 1 6 1 2 1 18 1 31
50 1 1 7 1 2 1 19 1 33
51 1 1 6 1 2 2 20 1 34
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
39


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 6 — continuación
Mes JP ARQ SEG DAT DES CAL SRE IMP Personas
totales
52 1 1 7 1 2 1 20 1 34
53 1 1 6 1 2 1 19 1 32
54 1 1 7 1 2 2 21 1 36
55 1 1 7 1 2 1 19 1 33
56 1 1 7 1 2 1 21 1 35
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
40


---

LafroX SpA Formulario T-15: Nivelación de recursos
La curva de personas es una envolvente conservadora de demanda, no disponibilidad
acreditada. En calidad, los meses 16 y 17 requieren respectivamente siete y seis personas
equivalentes: la carga CAL sin reserva es de 741,33 y 549,33 HH, a la que se agregan 128 HH
mensuales de reserva exclusiva E1 antes de redondear a 128 HH por persona. La factibilidad
requiere asignar cada rol de la curva y comprobar las concurrencias diarias de certificación y
continuidad. El registro nominal de personas y los turnos se aprueban junto con la línea base
del H1. La reserva E1 es exclusiva; el trabajo de E2 usa capacidad adicional. La revisión de HH
modifica conjuntamente dotación, cronograma y exposición de SD8.
4.5 Reservas de contingencia y de gestión
Las 220.023 HH de la sección 4.3 son la línea base programada e incluyen 3.072 HH pro-
tegidas para correcciones de la Etapa 1. Esa capacidad no se suma nuevamente ni acredita
cobertura de cualquier contingencia. Las reservas adicionales de riesgos del SD8 (Subdocu-
mento 8) se administran por separado y deben conciliarse con la nueva línea base antes de
afirmar capacidad movilizable. La holgura contractual de cada hito se calcula en la Tabla 8
con las HH, el calendario y las precedencias vigentes. Es un margen de programación, no
capacidad nominal movilizable ni reserva monetaria.
La contingencia por riesgo requiere la conciliación del responsable de SD8: riesgo vigente,
respuesta, paquete, perfil, período, unidad y autorización. Las 1.600 HH de reserva de gestión
no se incorporan al total programado ni a la dotación mientras no cuenten con fundamento,
aprobación y asignación de recursos. Son distintas de las 1.600 HH de pruebas de la Etapa 2, ya
incluidas en la cuenta 3.9. Ninguna reserva de riesgos se interpreta como capacidad nominal
disponible; su consumo requiere autorización y asignación registrada. HH, dinero y días de
holgura son magnitudes diferentes y no se suman entre sí.
5 Red agregada, restricciones y escenarios de calendario
El CPM/PERT utiliza las HH de las secciones 4.2–4.4 y las fechas y predecesoras de la sección
6.1. Se conservan los 227 paquetes y las 220.023 HH: 168 paquetes tienen entregable y 59 son
de esfuerzo continuo. El cálculo no reprograma las fechas publicadas: expone sus resultados
lógicos y las diferencias con ventanas e hitos.
5.1 Cálculo reproducible
La red agregada modela 399 eventos y 581 relaciones. Cada paquete con entregable tiene
inicio y fin; las revisiones de aceptación del CLIENTE y las condiciones de marcha blanca y
del piloto son eventos separados. La revisión del acta de cierre previa a producción se evalúa
adicionalmente en la Tabla 9; no se presupone absorbida por las revisiones H7/H12. Se aplica
una pasada hacia adelante y otra hacia atrás (PMI, 2017, pp. 210–211). La tabla detallada permite
comprobar fechas tempranas, tardías y holguras.
LafroX SpA
Formulario T-15
Media firma: Alex Aravena
41


---

LafroX SpA Formulario T-15: Nivelación de recursos
• Calendario. El mes 1 corresponde al supuesto de febrero de 2027. El desarrollo y la revisión
administrativa usan el calendario interno de lunes a viernes y feriados previstos; entre sus
exclusiones están el 21 de junio de 2027, el 20 de junio de 2028, el 27 de octubre y el 1 de
noviembre de 2028. Este calendario requiere confirmación con el CLIENTE antes de aprobar
la línea base; cualquier diferencia obliga a recalcular. NOC, mesa y acompañamiento
conservan sus calendarios de servicio de la sección 4.1; no se transforman en trabajo
administrativo de lunes a viernes.
• Duración. Para cada paquete se cuentan los días laborables de su ventana diaria y se
comprueba el mínimo ⌈𝐻𝐻/(6,4 𝑛máx)⌉. La duración usada es el mayor de ambos. Es una
duración agregada reservada, no una declaración de que el equipo máximo trabaje todos los
días. Las actividades de la sección 6 mantienen el límite de una quincena. Las ocho semanas
de homologación y las seis semanas de piloto se conservan en las ventanas publicadas.
• Trabajo interno y margen. En módulos, las puertas de contratos e integración usan sus HH
efectivas y la construcción usa ⌈(𝐻𝐻 −240)/(6,4 𝑛máx)⌉. El vínculo global inicio–fin conserva
toda la ventana publicada, con sus esperas y márgenes. Así, una espera por interfaz no
vuelve a contarse como construcción obligatoria. El recálculo conserva las fechas de los
168 paquetes publicados; es una comprobación lógica con equipos máximos supuestos, no
una nivelación diaria demostrada.
• Precedencias. FC conecta el fin del predecesor con el inicio del sucesor; CC conecta sus
inicios. La disponibilidad de QA condiciona la entrega del módulo, no su análisis en DEV.
En las interfaces, la entrega precedente condiciona el último incremento de integración del
sucesor; se reserva al menos una actividad de 80 HH con su equipo máximo. En los módulos,
A01/A02 y el incremento final se representan como puertas internas: la construcción espera
el contrato A02 precedente y la integración espera la entrega precedente. Las actividades
restantes se detallan por planificación gradual. Para el corte, los ensayos condicionan A06
y no el análisis preparatorio. No se elimina una dependencia por incumplir una fecha
programada.
• Cadena de frío. Se incluyen banco 2.4.3, mapeo 2.4.4, homologación y compra 5.1.4, con-
tratos 5.3.4, módulos 3.4.4/3.4.5 y piloto 4.1.4. El contrato de banco depende del inicio de la
especificación, CC. El piloto espera H4 y cuatro actas parciales de kits; la ola de reparto
espera el piloto y las 28 actas. No se exige la instalación de los 28 kits para empezar el piloto
de cuatro camiones.
• CLIENTE. La entrega y el acta son eventos distintos. Cada entrega de hito reserva diez días
hábiles para revisión (BA, art. 18.3); se calcula su fecha límite retrocediendo desde el último
día laborable del mes contractual. H6 y H11 son comienzos de marcha blanca, no actas
finales con otros diez días de revisión.
• Holguras. La pasada inversa impone tanto la ventana máxima de cada paquete como las
fechas contractuales. Una holgura negativa identifica una restricción incompatible; no
autoriza desplazar el contrato. La holgura de un hito compara el acta calculada con su
límite; la de un paquete también considera su ventana propia y puede ser menor.
LafroX SpA
Formulario T-15
Media firma: Alex Aravena
42


---

LafroX SpA Formulario T-15: Nivelación de recursos
• Recursos. Las HH y los máximos de equipo provienen de la sección 6.1. Este CPM es
condicional a su disponibilidad y no acredita asignación nominal ni nivelación fina entre
actividades. La capacidad mensual se contrasta con la sección 4 y la dotación de la sección
5.7. Ningún resultado probabilístico sustituye esa comprobación.
La Tabla 7 presenta fechas tempranas, tardías y holguras de los 168 paquetes con entregable.
LafroX SpA
Formulario T-15
Media firma: Alex Aravena
43


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 7 Fechas tempranas, tardías y holguras de los 168 paquetes con entregable. Fuente: elaboración a partir de las secciones 4.2, 5.1 y 6.1 y del Anexo 7.B.
EDT Dura-
ción
(días)
Inicio tem-
prano
Fin temprano Inicio tardío Fin tardío Hol-
gura
(días)
HH
1.1.1 7 01-02-2027 09-02-2027 18-02-2027 26-02-2027 13 80
1.1.2 7 01-02-2027 09-02-2027 18-02-2027 26-02-2027 13 80
1.1.3 7 01-02-2027 09-02-2027 18-02-2027 26-02-2027 13 80
1.2.1 7 01-02-2027 09-02-2027 18-02-2027 26-02-2027 13 80
1.2.3 7 01-02-2027 09-02-2027 20-05-2027 31-05-2027 77 80
1.2.4 7 01-03-2027 09-03-2027 08-03-2027 16-03-2027 5 80
1.2.5 7 01-02-2028 09-02-2028 09-02-2028 17-02-2028 6 80
1.3.1 7 10-02-2027 18-02-2027 18-02-2027 26-02-2027 6 80
1.3.2 7 01-03-2027 09-03-2027 22-03-2027 31-03-2027 15 80
1.3.3 7 01-03-2027 09-03-2027 22-03-2027 31-03-2027 15 80
1.3.4 7 01-03-2027 09-03-2027 22-03-2027 31-03-2027 15 80
1.4.1 7 01-02-2027 09-02-2027 18-02-2027 26-02-2027 13 80
1.4.2 7 01-02-2027 09-02-2027 18-02-2027 26-02-2027 13 80
1.5.1 7 01-03-2027 09-03-2027 22-03-2027 31-03-2027 15 80
1.6.1 7 01-03-2027 09-03-2027 22-03-2027 31-03-2027 15 80
1.7.1 7 01-04-2027 09-04-2027 22-04-2027 30-04-2027 15 80
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
44


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 7 — continuación
EDT Dura-
ción
(días)
Inicio tem-
prano
Fin temprano Inicio tardío Fin tardío Hol-
gura
(días)
HH
1.7.2 7 03-04-2028 11-04-2028 20-04-2028 28-04-2028 12 80
1.9.1 7 01-02-2027 09-02-2027 18-02-2027 26-02-2027 13 80
1.9.2 7 01-02-2027 09-02-2027 18-02-2027 26-02-2027 13 80
1.9.3 7 01-03-2027 09-03-2027 22-03-2027 31-03-2027 15 80
2.1.1 20 01-03-2027 29-03-2027 03-03-2027 31-03-2027 2 240
2.1.2 20 01-03-2027 29-03-2027 03-03-2027 31-03-2027 2 240
2.1.3 20 01-03-2027 29-03-2027 03-03-2027 31-03-2027 2 240
2.1.4 12 01-02-2028 16-02-2028 02-02-2028 17-02-2028 1 240
2.2.1 20 01-03-2027 29-03-2027 03-03-2027 31-03-2027 2 240
2.2.3 12 01-04-2027 16-04-2027 02-04-2027 19-04-2027 1 240
2.2.4 20 01-03-2027 29-03-2027 03-03-2027 31-03-2027 2 240
2.3.1 21 01-02-2027 01-03-2027 19-02-2027 19-03-2027 14 240
2.3.2 21 01-02-2027 01-03-2027 19-02-2027 19-03-2027 14 240
2.3.3 20 01-03-2027 29-03-2027 03-03-2027 31-03-2027 2 240
2.4.1 9 19-04-2027 29-04-2027 20-04-2027 30-04-2027 1 240
2.4.2 8 17-02-2028 28-02-2028 18-02-2028 29-02-2028 1 240
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
45


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 7 — continuación
EDT Dura-
ción
(días)
Inicio tem-
prano
Fin temprano Inicio tardío Fin tardío Hol-
gura
(días)
HH
2.4.3 22 01-04-2027 30-04-2027 01-04-2027 30-04-2027 0 320
2.4.4 19 03-05-2027 28-05-2027 04-05-2027 31-05-2027 1 240
2.5.1 21 01-04-2027 29-04-2027 02-04-2027 30-04-2027 1 240
2.5.2 21 01-04-2027 29-04-2027 02-04-2027 30-04-2027 1 240
2.6.1 20 01-03-2027 29-03-2027 03-03-2027 31-03-2027 2 240
2.6.2 21 01-04-2027 29-04-2027 02-04-2027 30-04-2027 1 240
2.6.3 20 03-05-2027 31-05-2027 03-05-2027 31-05-2027 0 240
3.1.1 14 01-06-2027 18-06-2027 09-06-2027 30-06-2027 6 240
3.1.2 14 01-06-2027 18-06-2027 09-06-2027 30-06-2027 6 240
3.1.3 14 01-06-2027 18-06-2027 09-06-2027 30-06-2027 6 240
3.1.4 20 03-05-2027 31-05-2027 03-05-2027 31-05-2027 0 240
3.1.5 14 01-06-2027 18-06-2027 09-06-2027 30-06-2027 6 240
3.2.1 20 03-05-2027 31-05-2027 03-05-2027 31-05-2027 0 240
3.2.2 20 03-05-2027 31-05-2027 03-05-2027 31-05-2027 0 240
3.2.3 20 03-05-2027 31-05-2027 03-05-2027 31-05-2027 0 240
3.2.4 20 03-05-2027 31-05-2027 03-05-2027 31-05-2027 0 240
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
46


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 7 — continuación
EDT Dura-
ción
(días)
Inicio tem-
prano
Fin temprano Inicio tardío Fin tardío Hol-
gura
(días)
HH
3.2.5 20 03-05-2027 31-05-2027 03-05-2027 31-05-2027 0 240
3.2.6 19 01-06-2027 29-06-2027 02-06-2027 30-06-2027 1 240
3.3.1 45 01-06-2027 05-08-2027 15-06-2027 31-08-2027 10 480
3.3.2 21 01-06-2027 01-07-2027 15-06-2027 30-07-2027 10 480
3.3.3 25 01-06-2027 07-07-2027 15-06-2027 30-07-2027 10 480
3.3.4 21 10-06-2027 12-07-2027 15-06-2027 30-07-2027 3 480
3.3.5 43 01-06-2027 03-08-2027 15-06-2027 31-08-2027 10 480
3.3.6 39 07-06-2027 03-08-2027 15-06-2027 31-08-2027 6 480
3.4.1 41 10-06-2027 10-08-2027 15-06-2027 27-08-2027 3 960
3.4.2 42 10-06-2027 11-08-2027 15-06-2027 27-08-2027 3 960
3.4.3 45 14-06-2027 18-08-2027 24-06-2027 31-08-2027 7 960
3.4.4 74 14-06-2027 29-09-2027 15-06-2027 30-09-2027 1 1440
3.4.5 53 14-06-2027 30-08-2027 15-06-2027 31-08-2027 1 1440
3.4.6 42 16-06-2027 17-08-2027 24-06-2027 31-08-2027 5 960
3.4.7 58 16-06-2027 08-09-2027 09-07-2027 30-09-2027 15 960
3.4.8 59 16-06-2027 09-09-2027 24-06-2027 30-09-2027 5 960
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
47


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 7 — continuación
EDT Dura-
ción
(días)
Inicio tem-
prano
Fin temprano Inicio tardío Fin tardío Hol-
gura
(días)
HH
3.4.9 71 18-06-2027 30-09-2027 18-06-2027 30-09-2027 0 960
3.4.10 75 10-06-2027 04-10-2027 24-06-2027 12-10-2027 5 960
3.4.11 17 02-09-2027 27-09-2027 07-09-2027 30-09-2027 3 960
3.5.1 32 15-03-2028 28-04-2028 15-03-2028 28-04-2028 0 960
3.5.2 32 15-03-2028 28-04-2028 15-03-2028 28-04-2028 0 960
3.5.3 32 15-03-2028 28-04-2028 15-03-2028 28-04-2028 0 960
3.5.4 32 15-03-2028 28-04-2028 15-03-2028 28-04-2028 0 960
3.6.1 23 02-08-2027 01-09-2027 30-08-2027 30-09-2027 20 480
3.6.2 22 01-07-2027 02-08-2027 02-08-2027 31-08-2027 21 480
3.6.3 22 01-07-2027 02-08-2027 02-08-2027 31-08-2027 21 480
3.6.4 22 01-07-2027 02-08-2027 02-08-2027 31-08-2027 21 480
3.6.5 107 01-02-2028 04-07-2028 28-02-2028 31-07-2028 19 480
3.6.6 57 01-06-2028 23-08-2028 09-06-2028 31-08-2028 6 480
3.7.1 42 04-08-2027 01-10-2027 31-08-2027 29-10-2027 19 480
3.7.2 21 04-10-2027 03-11-2027 02-11-2027 30-11-2027 19 480
3.7.3 22 01-12-2027 31-12-2027 01-12-2027 31-12-2027 0 480
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
48


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 7 — continuación
EDT Dura-
ción
(días)
Inicio tem-
prano
Fin temprano Inicio tardío Fin tardío Hol-
gura
(días)
HH
3.7.4 22 01-12-2027 31-12-2027 01-12-2027 31-12-2027 0 480
3.7.5 19 03-01-2028 27-01-2028 05-01-2028 31-01-2028 2 480
3.8.1 13 05-10-2027 22-10-2027 13-10-2027 29-10-2027 5 160
3.8.2 19 25-10-2027 19-11-2027 04-11-2027 30-11-2027 7 320
3.8.3 19 25-10-2027 19-11-2027 04-11-2027 30-11-2027 7 320
3.8.4 13 25-10-2027 11-11-2027 12-11-2027 30-11-2027 13 320
3.8.5 13 25-10-2027 11-11-2027 12-11-2027 30-11-2027 13 320
3.8.6 13 25-10-2027 11-11-2027 12-11-2027 30-11-2027 13 320
3.8.7 8 22-11-2027 01-12-2027 22-12-2027 31-12-2027 21 160
3.8.8 13 25-10-2027 11-11-2027 12-11-2027 30-11-2027 13 320
3.9.1 13 02-05-2028 18-05-2028 05-05-2028 23-05-2028 3 160
3.9.2 10 02-06-2028 15-06-2028 06-06-2028 19-06-2028 2 320
3.9.3 10 19-05-2028 01-06-2028 06-06-2028 19-06-2028 12 320
3.9.4 10 19-05-2028 01-06-2028 06-06-2028 19-06-2028 12 320
3.9.5 6 19-05-2028 26-05-2028 24-05-2028 31-05-2028 3 160
3.9.6 7 16-06-2028 28-06-2028 21-06-2028 30-06-2028 2 160
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
49


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 7 — continuación
EDT Dura-
ción
(días)
Inicio tem-
prano
Fin temprano Inicio tardío Fin tardío Hol-
gura
(días)
HH
3.9.7 10 19-05-2028 01-06-2028 06-06-2028 19-06-2028 12 160
3.10.1.1 49 02-08-2027 08-10-2027 20-08-2027 29-10-2027 14 240
3.10.1.2 34 01-10-2027 19-11-2027 13-10-2027 30-11-2027 7 240
3.10.1.3 34 01-10-2027 19-11-2027 13-10-2027 30-11-2027 7 240
3.10.1.4 78 01-12-2027 20-03-2028 11-01-2028 28-04-2028 28 240
3.10.2.1 36 01-03-2027 20-04-2027 11-03-2027 30-04-2027 8 240
3.10.2.2 49 01-04-2027 09-06-2027 20-04-2027 30-06-2027 13 240
3.10.2.3 90 01-06-2027 08-10-2027 23-07-2027 30-11-2027 35 240
3.10.2.4 78 01-12-2027 20-03-2028 11-01-2028 28-04-2028 28 240
3.10.3.1 49 01-04-2027 09-06-2027 20-04-2027 30-06-2027 13 240
3.10.3.2 72 07-06-2027 20-09-2027 20-07-2027 29-10-2027 28 240
3.10.3.3 34 01-10-2027 19-11-2027 13-10-2027 30-11-2027 7 240
3.10.3.4 78 01-12-2027 20-03-2028 11-01-2028 28-04-2028 28 240
3.10.4.1 36 01-02-2028 21-03-2028 11-02-2028 31-03-2028 8 240
3.10.4.2 35 01-03-2028 19-04-2028 10-03-2028 28-04-2028 7 240
3.10.4.3 48 03-04-2028 09-06-2028 21-04-2028 30-06-2028 13 240
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
50


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 7 — continuación
EDT Dura-
ción
(días)
Inicio tem-
prano
Fin temprano Inicio tardío Fin tardío Hol-
gura
(días)
HH
3.10.4.4 62 03-07-2028 29-09-2028 31-07-2028 31-10-2028 20 240
4.1.1 7 02-11-2027 10-11-2027 22-11-2027 30-11-2027 14 80
4.1.2 7 01-12-2027 10-12-2027 23-12-2027 31-12-2027 15 80
4.1.3 7 01-06-2028 09-06-2028 21-06-2028 30-06-2028 13 80
4.1.4 29 09-11-2027 20-12-2027 22-11-2027 31-12-2027 9 320
4.2.3 7 05-05-2028 15-05-2028 09-05-2028 17-05-2028 2 80
4.3.3 7 02-10-2028 11-10-2028 05-10-2028 16-10-2028 3 80
4.3.4 7 13-09-2028 25-09-2028 21-09-2028 29-09-2028 4 80
5.1.1 7 01-03-2027 09-03-2027 22-03-2027 31-03-2027 15 80
5.1.2 7 02-03-2027 10-03-2027 22-03-2027 31-03-2027 14 80
5.1.3 7 01-06-2027 09-06-2027 18-06-2027 30-06-2027 13 80
5.1.4 42 01-02-2027 31-03-2027 01-02-2027 31-03-2027 0 240
5.2.1 7 01-03-2027 09-03-2027 22-03-2027 31-03-2027 15 80
5.2.2 7 03-05-2027 11-05-2027 20-05-2027 31-05-2027 13 80
5.2.3 7 03-05-2027 11-05-2027 20-05-2027 31-05-2027 13 80
5.3.1 7 03-05-2027 11-05-2027 20-05-2027 31-05-2027 13 80
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
51


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 7 — continuación
EDT Dura-
ción
(días)
Inicio tem-
prano
Fin temprano Inicio tardío Fin tardío Hol-
gura
(días)
HH
5.3.2 7 03-05-2027 11-05-2027 20-05-2027 31-05-2027 13 80
5.3.3 7 03-05-2027 11-05-2027 20-05-2027 31-05-2027 13 80
5.3.4 10 01-03-2027 12-03-2027 17-03-2027 31-03-2027 12 80
5.4.1 7 01-10-2027 12-10-2027 21-01-2028 31-01-2028 77 80
5.4.2 7 01-10-2027 12-10-2027 21-01-2028 31-01-2028 77 80
5.4.3 7 01-06-2028 09-06-2028 21-09-2028 29-09-2028 75 80
5.4.4 7 02-08-2027 10-08-2027 23-08-2027 31-08-2027 15 80
6.1.1 14 01-04-2027 20-04-2027 13-04-2027 30-04-2027 8 160
6.1.2 14 01-04-2027 20-04-2027 13-04-2027 30-04-2027 8 160
6.1.3 14 01-04-2027 20-04-2027 13-04-2027 30-04-2027 8 160
6.1.4 14 01-04-2027 20-04-2027 13-04-2027 30-04-2027 8 160
6.1.5 14 03-05-2027 20-05-2027 03-05-2027 20-05-2027 0 160
6.2.1 14 03-05-2027 20-05-2027 11-05-2027 31-05-2027 6 160
6.2.2 13 01-07-2027 20-07-2027 13-07-2027 30-07-2027 8 160
6.2.3 14 02-08-2027 19-08-2027 12-08-2027 31-08-2027 8 160
6.3.1 13 24-05-2027 09-06-2027 24-05-2027 09-06-2027 0 160
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
52


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 7 — continuación
EDT Dura-
ción
(días)
Inicio tem-
prano
Fin temprano Inicio tardío Fin tardío Hol-
gura
(días)
HH
6.3.2 13 24-05-2027 09-06-2027 24-05-2027 09-06-2027 0 160
6.3.3 14 03-05-2027 20-05-2027 11-05-2027 31-05-2027 6 160
6.3.4 13 01-10-2027 20-10-2027 13-10-2027 29-10-2027 7 160
6.4.1 14 01-06-2027 18-06-2027 09-06-2027 30-06-2027 6 160
6.4.2 13 07-06-2027 24-06-2027 10-06-2027 30-06-2027 3 160
6.4.3 13 22-06-2027 09-07-2027 13-07-2027 30-07-2027 14 160
6.5.1 70 06-10-2027 14-01-2028 22-10-2027 31-01-2028 11 160
6.5.2 51 04-11-2027 14-01-2028 19-11-2027 31-01-2028 11 160
6.5.3 35 06-10-2027 25-11-2027 12-11-2027 31-12-2027 25 160
6.5.4 94 01-09-2027 14-01-2028 16-09-2027 31-01-2028 11 320
6.5.5 51 04-11-2027 14-01-2028 19-11-2027 31-01-2028 11 160
6.5.6 70 06-10-2027 14-01-2028 22-10-2027 31-01-2028 11 160
6.6.1 13 10-06-2027 30-06-2027 10-06-2027 30-06-2027 0 160
6.6.2 13 10-06-2027 30-06-2027 10-06-2027 30-06-2027 0 160
6.6.3 7 10-06-2027 18-06-2027 18-06-2027 30-06-2027 6 160
7.1.1 38 02-11-2027 24-12-2027 09-12-2027 31-01-2028 26 160
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
53


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 7 — continuación
EDT Dura-
ción
(días)
Inicio tem-
prano
Fin temprano Inicio tardío Fin tardío Hol-
gura
(días)
HH
7.1.6 38 02-11-2027 24-12-2027 09-12-2027 31-01-2028 26 160
7.2.2 38 02-05-2028 23-06-2028 06-06-2028 31-07-2028 25 160
7.2.3 60 01-03-2027 25-05-2027 04-05-2027 30-07-2027 45 160
7.3.1 39 01-02-2028 24-03-2028 06-03-2028 28-04-2028 24 160
7.3.2 17 03-07-2028 25-07-2028 07-07-2028 31-07-2028 4 160
9.1.1 7 02-10-2028 11-10-2028 20-10-2028 31-10-2028 13 80
9.1.2 7 26-10-2028 07-11-2028 22-11-2028 30-11-2028 17 80
9.2.2 7 01-09-2031 09-09-2031 22-09-2031 30-09-2031 13 80
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
54


---

LafroX SpA Formulario T-15: Nivelación de recursos
5.2 Lectura de las secuencias y las restricciones
Ningún paquete presenta holgura negativa frente a su ventana ni frente a un hito. La
integración de cobranza 3.4.10 espera la entrega de reparto 3.4.8 y termina el 4 de octubre
de 2027, por lo que su ventana llega al mes 9; el acta de certificación 3.8.7 termina el 1 de
diciembre y su ventana abarca los meses 10 y 11. Es un trámite documental y no interviene
sistemas en el congelamiento de diciembre. H4 y H5 conservan dieciséis y veinte días hábiles.
La Tabla 7 muestra la holgura de cada paquete. El cierre formal 9.1.2 espera el acta H12 y se
programa del 26 de octubre al 7 de noviembre de 2028, en los meses 21 y 22, porque es un
trámite posterior a la aceptación final. El cálculo incorpora las dependencias de preparación,
interfaces, integración y revisión.
En E1, la integración final de cobranza tras la entrega de reparto lleva el cierre calculado
de 3.4.10 al 4 de octubre de 2027 y la integración 3.8.1 al 22 de octubre. Las pruebas de acepta-
ción/sin conexión concluyen el 19 de noviembre y la certificación 3.8.7, el 1 de diciembre. H4 y
H5 quedan dentro de sus límites contractuales y de sus ventanas. La certificación E2 concluye
el 28 de junio de 2028 y su revisión lleva H10 al 12 de julio, dentro del mes 18.
El piloto comienza el 9 de noviembre de 2027, el día siguiente al acta del H4, y termina el 20
de diciembre, en los meses 10 y 11. Su tramo de diciembre no contraviene el congelamiento:
la solución todavía no está en producción, los camiones siguen operando con sus termógrafos
actuales y el piloto no modifica el ERP, el WMS ni la facturación. Ningún kit se instala ni se
ajusta en la ventana de despacho de 05:30 a 07:00. La recepción completa de kits precede a la
ola de reparto del mes 14.
5.3 Reservas y análisis PERT de duración
Se mantiene la hipótesis explícita 𝑂 = 0,75𝑑, 𝑀 = 𝑑 y 𝑃 = 1,25𝑑 para la duración agregada
con el equipo previsto: 𝑇𝐸 = (𝑂 + 4𝑀 + 𝑃)/6 = 𝑑 y 𝜎 = (𝑃 − 𝑂)/6 = 𝑑/12 (Malcolm et al., 1959).
La varianza de un camino suma las varianzas de sus duraciones, bajo independencia; los diez
días de revisión y los inicios contractuales son restricciones fijas y no reciben varianza de
esfuerzo. La aproximación normal Φ((𝐿 − 𝑇𝐸)/𝜎) es una probabilidad condicional del camino
controlante, no del proyecto completo. No se calcula una probabilidad para H6/H11 cuando el
control es sólo su fecha fija de inicio.
La Tabla 8 presenta cPM y PERT de los hitos con la línea base de 220.023 HH.
LafroX SpA
Formulario T-15
Media firma: Alex Aravena
55


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 8 CPM y PERT de los hitos con la línea base de 220.023 HH. Fuente: elaboración a partir de las secciones 4.2, 5.1 y 6.1, y del Anexo 7.B.
Hito Entrega
calculada
Acta o inicio
calculado
Límite con-
tractual
Hol-
gura
(días)
Camino controlante Dura-
ción del
camino
(días)
Sigma
(días)
PERT con-
dicional
H1 09-03-2027 23-03-2027 31-03-2027 5 1.2.4 7.0 0,58 >99,9 %
H2 29-04-2027 13-05-2027 31-05-2027 11 2.4.1 9.0 0,75 >99,9 %
H3 18-06-2027 06-07-2027 30-07-2027 17 3.1.5 14.0 1,17 >99,9 %
H4 22-10-2027 08-11-2027 30-11-2027 16 3.8.1 13.0 1,08 >99,9 %
H5 01-12-2027 03-01-2028 31-01-2028 20 3.8.7 8.0 0,67 >99,9 %
H6 01-02-2028 01-02-2028 01-02-2028 0 Inicio contractual fijo 0 — —
H8 28-02-2028 13-03-2028 31-03-2028 14 2.4.2 8.0 0,67 >99,9 %
H7 15-05-2028 29-05-2028 31-05-2028 2 4.2.3 7.0 0,58 >99,9 %
H9 18-05-2028 01-06-2028 30-06-2028 19 3.9.1 13.0 1,08 >99,9 %
H10 28-06-2028 12-07-2028 31-07-2028 13 3.9.6 7.0 0,58 >99,9 %
H11 01-08-2028 01-08-2028 01-08-2028 0 Inicio contractual fijo 0 — —
H12 11-10-2028 25-10-2028 31-10-2028 3 4.3.3 7.0 0,58 >99,9 %
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
56


---

LafroX SpA Formulario T-15: Nivelación de recursos
H12 tiene entrega calculada el 11 de octubre de 2028; sus diez días de revisión van del 12
al 25 de octubre, descontando los fines de semana. Frente al 31 de octubre quedan tres días
hábiles: 26, 30 y 31 de octubre, porque el 27 es feriado. La holgura proviene de constituir la
garantía 4.3.4 en septiembre, en paralelo con la marcha blanca, y no de acortar la revisión del
CLIENTE ni las cuatro semanas finales de evidencia.
La cuantificación de riesgos del SD8 (valores esperados de esfuerzo, Anexo 8.B) no se
recalcula aquí ni se traduce en fechas para esta red. Incorporar riesgos correlacionados,
subsanaciones, tiempos de suministro y disponibilidad real requiere su conciliación específica.
El PERT no mide la probabilidad de cumplir la aceptación copulativa de una marcha blanca.
5.4 Gobierno
Se mantienen las 220.023 HH y las fechas programadas. Toda desviación que consuma
la holgura de un paquete se presenta al Comité de Proyecto con su plan de recuperación;
cualquier reprogramación obliga a repetir las pasadas y el presupuesto mensual. Las cuatro
semanas finales de marcha blanca y los diez días de revisión del CLIENTE no son reserva de
trabajo del proponente.
Las cuatro semanas de acompañamiento se mantienen como presupuesto de planificación
de la sección 4.1, sujeto a la firma efectiva del H12. Su fecha presupuestada no demuestra que
la revisión haya concluido. Toda firma posterior exige redistribuir las mismas HH entre meses
y revisar relevos sin acortar el acompañamiento.
5.5 Presentación de entregables y revisión del CLIENTE
La Tabla 8 distingue entrega, acta calculada y límite contractual; la sección 6.1 conserva la
propuesta de fechas fuente. Los entregables del H4 admiten presentación por incrementos; el
último informe de integración y la revisión completa quedan reflejados en la red. La subsa-
nación no está incluida como trabajo ordinario dentro de los diez días de revisión: si ocurre,
consume holgura adicional.
H1, H7 y H12 disponen de cinco, dos y tres días hábiles de holgura contractual, menos que
los diez días de subsanación. La preparación y revisión preliminar del expediente reducen
errores, pero no sustituyen los diez días de revisión formal, la subsanación ni una segunda
revisión. No se presupone aprobada una revisión anticipada de evidencia que aún no se ha
producido. H8 dispone de catorce días porque el diseño de la Etapa 2 se entrega en febrero de
2028.
Dos actas por etapa y condición previa a producción.. El acta de cierre pertenece a 4.2.1/4.3.1 y
habilita producción; el acta de aceptación H7/H12 corresponde a 4.2.3/4.3.3 y es posterior. La
Tabla 9 separa evidencia, entrega, revisión, firma y producción bajo el calendario supuesto. La
revisión durante la marcha blanca puede preparar el expediente, pero no demuestra aceptación
de sus últimos 28 días antes de completarlos.
LafroX SpA
Formulario T-15
Media firma: Alex Aravena
57


---

LafroX SpA Formulario T-15: Nivelación de recursos
Tabla 9 Secuencia de cierre, producción y aceptación. Fuente: fechas publicadas de T-15 y calendario supuesto de
la sección 5.1; plazos de BA, art. 18.3, según T-17, secciones 1 y 2.
Evento Etapa 1 Etapa 2 Condición
Evidencia final com-
pleta
03–30 abril 2028 03–30 septiembre
2028
Últimos 28 días completos; no
se recortan ni se sustituyen por
preparación del expediente.
Entrega completa de
cierre, escenario
02 mayo 2028 02 octubre 2028 Primer día hábil posterior a la
evidencia; no es una entrega anti-
cipada aprobada.
Revisión de cierre,
si aplica el plazo
completo
03–16 mayo 2028 03–17 octubre 2028 Diez días hábiles desde el siguien-
te a la entrega; sin observaciones
ni segunda revisión.
Acta de cierre 4.2.1 /
4.3.1
Objetivo: fin del
mes 15
Objetivo: fin del
mes 20
La firma requiere evidencia com-
pleta y revisión concluida. El
escenario anterior no demuestra
encaje con este objetivo.
Paso a producción
objetivo
05 mayo 2028 05 octubre 2028 Requiere acta de cierre previa. Só-
lo hay dos días de revisión entre la
entrega del escenario y esta fecha;
incompatibilidad por resolver.
Entrega de acepta-
ción H7 / H12
15 mayo 2028 11 octubre 2028 Expediente de aceptación poste-
rior a producción; estas fechas no
sustituyen la revisión del cierre.
Revisión de acepta-
ción publicada
16–29 mayo 2028 12–25 octubre 2028 Diez días hábiles bajo el calenda-
rio supuesto.
Acta de aceptación
objetivo
29 mayo 2028 (H7) 25 octubre 2028
(H12)
Condicionada a cierre y produc-
ción previos, garantía aplicable y
resolución de observaciones.
Si se exige el plazo completo del art. 18.3 al cierre, no cabe antes de las fechas objetivo del
5 de mayo y del 5 de octubre. Tampoco cabe una subsanación de diez días más una segunda
revisión. La Contraparte Técnica debe precisar por escrito el procedimiento aplicable a estas
actas y su encaje con el art. 17.3 antes de aprobar la línea base. Si no permite conservar las
fechas, se presenta la reprogramación para aprobación; la carta publicada permanece como
objetivo condicionado, sin autorizar producción sin acta. El protocolo T-17 del SD9, secciones
1, 2 y 4.1, debe recibir la misma decisión.
LafroX SpA
Formulario T-15
Media firma: Alex Aravena
58


---

LafroX SpA Formulario T-15: Nivelación de recursos
5.6 Medición de los niveles de atención
Durante la atención de 04:00 a 22:00 de lunes a sábado y su cobertura 24×7 en los peaks de
septiembre y diciembre y ante incidentes críticos en la ventana de despacho, LafroX atenderá
al menos el 80 % de los contactos antes de 20 segundos, resolverá al menos el 70 % en el primer
contacto y mantendrá el abandono en un máximo del 5 %. Estos resultados se medirán y
reportarán mensualmente y activarán las medidas de recalibración y refuerzo previstas en
esta sección (BTT, cap. 21, RT-21.06, p. 36; Caso, cap. 15, pp. 26–27).
El Erlang C de la mesa (SD4, Anexo 4-W.7) dimensiona la espera con llegadas de Poisson,
atención exponencial y paciencia infinita. Sirve para el 80 % de respuestas antes de 20 segundos,
pero no modela el abandono ni la resolución al primer contacto del RT-21.06 de las Bases
Técnicas Transversales (p. 36). Para ambos se aplica medición: desde la marcha blanca de
la Etapa 1, la mesa registra por contacto la hora de llegada, de respuesta o de abandono y si
se resolvió sin escalar. Con al menos cuatro semanas de registros se calibra un modelo con
abandono (Erlang A) usando la paciencia observada, y se recalcula la dotación de 8.1.2 antes
del mes 21. La resolución al primer contacto se sostiene con la base de conocimiento de 3.11 y
la capacitación de 7.1, y se informa mensualmente. Si un indicador no se cumple durante dos
meses seguidos, se aumenta la dotación de la franja afectada sin esperar la revisión anual.
5.7 Dotación requerida, roles mínimos y dotación declarada
La curva de la sección 4.4 y la carga diaria de la sección 6.1 se comparan con la dotación
técnica declarada en el SD1, Tabla 1.1. Las personas equivalentes de la curva son HH del mes
divididas por 128; las simultáneas son las que trabajan el mismo día según el cronograma por
actividad, y son las que la dotación debe cubrir. La comparación muestra dónde la curva cabe
en las divisiones de LafroX y dónde se requiere asignación, contratación o subcontratación
antes de aprobar la línea base. Como las personas de esas divisiones atienden otros contratos,
la asignación nominal se confirma antes del H1.
La Tabla 10 presenta dotación requerida, roles mínimos y dotación declarada.
LafroX SpA
Formulario T-15
Media firma: Alex Aravena
59


---

LafroX SpA Formulario T-15: Nivelación de recursos
Tabla 10 Dotación requerida, roles mínimos y dotación declarada. Fuente: (Bases Técnicas Transversales, sección
19.2, pp. 33–34); (Bases Administrativas, Formulario T-15, p. 63); y la curva de este formulario.
Fa-
milia
T-15
Peak de la curva División del SD1 que
la provee
Dotación
declarada
Condición
DES 31 equivalentes en
meses 6 y 7. El máxi-
mo diario de 40 no
queda acreditado por
la curva mensual; re-
quiere nivelación de
actividades.
Desarrollo de soft-
ware
48 Son 48 integrantes declarados
de la división, no 48 personas
disponibles para este contrato.
El Líder de Desarrollo confirma
asignación y competencias antes
de comprometer concurrencia
diaria.
SRE 17 equivalentes en el
mes 4; 24 simultáneas
en el mes 4; 16 a 21 en
Operación; el tercer
agente de la mesa se
suma desde el mes 25
SRE y Cloud (12) y
NOC 24×7 (32)
44 Los meses 3 a 6 concentran la
instalación de sala, racks y sitios:
energía, climatización e incendio
(6.1.2–6.1.4) los ejecutan instala-
dores especializados supervisados
por SRE. NOC y mesa se cubren
con personal del NOC con turnos
asignados.
SEG 9 en el mes 16 con el
SOC; 6 simultáneas
sin el SOC
CISO y especialistas
en ciberseguridad
7 El puesto SOC 24×7 suma 744
HH en un mes de 31 días, es
decir, 6 personas equivalentes
con las 128 HH efectivas de la
sección 4.1; el SD4, Anexo 4-
W.7, lo cubre con 4 personas
a 42 horas semanales (5 desde
el 26-04-2028) y la diferencia
corresponde a ausencias y relevos.
Se cubre con un SOC propio
en el Centro de Operaciones
de LafroX en Valparaíso, con
analistas contratados antes del
mes 13 bajo el Encargado de
Seguridad (RT-11.17), con las
mismas horas de la sección 4.2.
continúa en la página siguiente
LafroX SpA
Formulario T-15
Media firma: Alex Aravena
60


---

LafroX SpA Formulario T-15: Nivelación de recursos
Tabla 10 — continuación
Fa-
milia
T-15
Peak de la curva División del SD1 que
la provee
Dotación
declarada
Condición
CAL 8 equivalentes en mes
9; la curva mensual
no demuestra con-
currencia diaria de
certificación.
Aseguramiento y
automatización de
pruebas
10 La división declara 10. No se
acredita un refuerzo de 16 evalua-
dores/día: su alcance, personas,
días, HH y contratación deben
confirmarse con el responsable
de metodología y pruebas antes
de aprobar la capacidad.
ARQ y
DAT
11 y 10 equivalentes;
concurrencia diaria
conjunta sujeta a
comprobación.
Arquitectura de so-
lución e integración
15 Arquitectura y datos comparten
la división; la asignación nominal
debe respetar su capacidad de 15
personas por día.
IMP 27 equivalentes en
mes 19; simultaneidad
diaria sujeta al calen-
dario y asignación
nominal.
La Tabla 1.1 no
tiene una división
de implantación
— Los 13 puestos de acompaña-
miento se cubren con personal
de implantación contratado para
las marchas blancas y capaci-
tado en 7.1. El contrato incluye
una opción de hasta 8 personas
adicionales por cuatro semanas
para contingencias de la marcha
blanca (sección 4.5).
JP 5 en el mes 1 Dirección de Opera-
ciones, fuera de la
Tabla 1.1
— Personas de dirección y documen-
tación, no cinco jefes de proyecto.
La obra civil de separación de 6.1.1 corresponde al CLIENTE (RT-06.06); LafroX especifica y
coordina, y provee el piso técnico y las instalaciones de su alcance. El mes 3 es una necesidad
de la programación, no una fecha de entrega ya confirmada por el CLIENTE. El acta de dispo-
nibilidad del recinto debe preceder a los trabajos que dependan de ella; 6.1.5 recibe también
la obra de 6.1.1, además de energía, climatización e incendio. Un retraso se analiza frente a
H3 antes de iniciar montaje.
La contratación de analistas del SOC propio debe completarse antes del mes 13 bajo SEG.
La cobertura 24×7 y los relevos se incluyen en 8.1.5; el total de siete especialistas declarados
no demuestra por sí solo disponibilidad simultánea para SOC y las demás tareas de seguridad.
Se confirma su asignación por turno y se contrasta el equipo compartido de ARQ/DAT con su
capacidad conjunta de 15.
LafroX SpA
Formulario T-15
Media firma: Alex Aravena
61


---

LafroX SpA Formulario T-15: Nivelación de recursos
La suma de máximos de paquetes cuyas ventanas coinciden es una cota superior, no
demanda simultánea demostrada. A su vez, repartir uniformemente HH en la ventana sólo da
una demanda media hipotética. Con esas reglas, el escenario uniforme alcanza 40,79 DES y
12,96 CAL en determinados días: señala necesidad de nivelación, pero no prueba un máximo
real de 40 ni disponibilidad de 16 evaluadores. La aprobación exige un calendario de actividades
con personas distintas, competencias, dedicaciones y cobertura de los servicios continuos.
Existe además una condición necesaria más fuerte: entre el 25-10 y el 11-11-2027, los
paquetes CAL 3.8.2 a 3.8.5 deben ejecutar al menos 1.049,60 HH dentro del intervalo, aun
aprovechando al máximo sus días exteriores. Trece días hábiles con diez personas a 6,4 HH/día
ofrecen 832 HH: faltan 217,60 HH. La capacidad requerida en algún momento es al menos
trece personas CAL, sin incluir servicios continuos. Por tanto, las diez declaradas no bastan
bajo estas ventanas y máximos; se necesita refuerzo asignado o una nivelación que revise
esas restricciones antes de aprobar la línea base. Este mínimo no demuestra que trece sean
suficientes ni acredita una contratación; no se agrega esfuerzo ni se modifican fechas por
inferencia.
Los roles mínimos del numeral 19.2 de las Bases Técnicas Transversales (p. 34) se imputan
a las familias así. El Jefe de Proyecto (100 % en implementación) se imputa a JP en los meses
1–21. El Líder de Desarrollo (100 % en implementación) se imputa a ARQ en los meses 1–4,
donde participa en el diseño 2.1 y en los prototipos 2.6.2, y a DES desde el mes 4 (3.11.3/
3.11.4 y los módulos); por eso la curva muestra DES cero en los meses 1–3 sin que el rol
quede sin horas. El Líder Funcional (100 % en implementación) se imputa a IMP en los meses
1–4 (1.2.2 y 2.6) y a CAL e IMP desde el mes 5 (pruebas de aceptación y olas). El Líder de
Integración (permanente en implementación) se imputa a ARQ (1.2.3, 3.3 y 3.6). Ninguna de
estas imputaciones agrega horas: forman parte de las horas de los paquetes donde trabajan. El
SD1, sección 1.5 (Subdocumento 1), nomina a las personas que ocupan cada rol.
6 Lista de actividades: regla del 8/80 y del período de reporte
La EDT del Formulario T-14 llega hasta el paquete de trabajo; fuera de ella, cada paquete se
descompone en las actividades que permiten programarlo, asignarlo y controlarlo (PMI, 2017,
pp. 183–185). Las actividades cumplen dos reglas de tamaño:
• Regla del 8/80. Cada actividad requiere entre 8 y 80 horas hombre de esfuerzo.
• Regla del período de reporte. Cada actividad cabe en una quincena, el período de reporte
del Comité de Proyecto (paquete 1.8.3): dura como máximo diez días hábiles. Con 6,4 HH
efectivas por persona y día, una actividad de 80 HH con dos personas dura ⌈80 ÷ 12,8⌉ =
7 días hábiles; si su ventana es más corta, se le asignan más personas. Toda actividad de
nivel de esfuerzo se divide en relevos de 64 HH como máximo.
La descomposición no cambia las HH de la sección 4: la suma de las actividades de cada
paquete es igual a su esfuerzo esperado E. Las actividades heredan el responsable y la ventana
del paquete. La Tabla 11 da las fechas de cada paquete y la Tabla 12 las actividades hasta el H2.
LafroX SpA
Formulario T-15
Media firma: Alex Aravena
62


---

LafroX SpA Formulario T-15: Nivelación de recursos
Por planificación gradual (PMI, 2017, p. 185), antes de cada fase se detallan las actividades de
la fase siguiente con las estimaciones del equipo, sin mover los hitos ni consumir más reserva
que la registrada. El avance se informa por el código de la actividad, que cuelga del código de
su paquete.
6.1 Paquetes con entregable y planificación gradual
La Tabla 11 conserva la programación propuesta de los 168 paquetes con entregable: rol,
personas, HH, inicio, fin y predecesoras. Las personas se expresan como promedio en los días
con trabajo y como máximo simultáneo; como la ventana puede incluir días de margen, el
promedio puede superar el cociente entre las HH y los días de la ventana. La Tabla 7 presenta
por separado las fechas calculadas y holguras de esas mismas HH y restricciones, sin sustituir
las fechas propuestas. QA condiciona la entrega; CC condiciona el inicio; las interfaces condi-
cionan contratos y entrega/integración. Los 59 paquetes continuos mantienen sus calendarios
de servicio. La planificación gradual descompone los paquetes siguientes al H2 antes de cada
fase; no se declara nivelación nominal validada.
Cada paquete se descompone en actividades de 8 a 80 HH que caben en una quincena, con
una plantilla por clase: un módulo (D, 960 HH) se construye en iteraciones de dos semanas
con análisis, diseño de contratos, incrementos, pruebas de contrato, integración en QA y
entrega; una integración (I, 480 HH), en seis actividades; un diseño (E, 240 HH), en tres; una
instalación o capacitación (T, 160 HH), en dos, y una prueba ampliada (V, 320 HH), en cuatro.
La Tabla 12 detalla las 119 actividades de los 60 paquetes que terminan hasta el H2 (mes 4).
El resto se descompone por planificación gradual (PMI, 2017, p. 185): antes de cada fase (H2,
H4, H8 y H9) el líder del frente detalla las actividades de la fase siguiente con la estimación
del equipo, el Comité de Proyecto las aprueba como iteraciones del proceso del SD6, sección
6.2 (Subdocumento 6), y se actualiza la línea base sin mover los hitos ni las fechas límite de la
Tabla 8.
La Figura 3 muestra qué parte del cronograma se detalla en la oferta y en qué momento se
detalla el resto.
LafroX SpA
Formulario T-15
Media firma: Alex Aravena
63


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Inicio, alcance y diseño
E1
Actividades
de 8 a 80 HH
Construcción E1:
base compartida,
módulos e integraciones
Se detalla antes del
H2 (mes 4)
Certificación y marcha
blanca
E1
Se detalla antes del H4
(mes 10)
Diseño y construcción
E2
Antes del H8
con línea base E2
Certificación y marcha
blanca
E2
Se detalla antes del
H9 (mes 17)
H2 H4 H8 H9
1
feb
2
mar
3
abr
4
may
5
jun
6
jul
7
ago
8
sep
9
oct
10
nov
11
dic
12
ene
13
feb
14
mar
15
abr
16
may
17
jun
18
jul
19
ago
20
sep
21
oct
2027 2028
Figura 3 Planificación gradual del cronograma. Fuente: elaboración a partir de las Tablas 11 y 12.
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
64


---

LafroX SpA Formulario T-15: Nivelación de recursos
La figura muestra que sólo los cuatro primeros meses, hasta el H2, se presentan descom-
puestos en actividades. Cada fase posterior tiene sus paquetes, fechas y dependencias fijos,
y se detalla en un punto de replanificación ubicado antes del hito que la precede, cuando el
equipo ya conoce el trabajo: así el cronograma no promete el día exacto de una actividad que
ocurrirá un año después.
LafroX SpA
Formulario T-15
Media firma: Alex Aravena
65


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 11 Programación de los paquetes con entregable. Fuente: elaboración a partir de las secciones 4.1, 4.2 y 5.1 de este formulario y (Subdocumento 7,
Anexo 7.B).
Paquete Rol Personas (prom.
/ máx.)
HH Inicio Fin Predecesoras (cuenta o paquete)
1.1.1 JP 1,8 / 2 80 01-02-2027 09-02-2027 —
1.1.2 JP 1,8 / 2 80 01-02-2027 09-02-2027 —
1.1.3 JP 1,8 / 2 80 01-02-2027 09-02-2027 —
1.2.1 ARQ 1,8 / 2 80 01-02-2027 09-02-2027 —
1.2.3 ARQ 1,8 / 2 80 01-02-2027 09-02-2027 —
1.2.4 CAL 1,8 / 2 80 01-03-2027 09-03-2027 —
1.2.5 ARQ 1,8 / 2 80 01-02-2028 09-02-2028 —
1.3.1 JP 1,8 / 2 80 10-02-2027 18-02-2027 —
1.3.2 JP 1,8 / 2 80 01-03-2027 09-03-2027 —
1.3.3 JP 1,8 / 2 80 01-03-2027 09-03-2027 —
1.3.4 JP 1,8 / 2 80 01-03-2027 09-03-2027 —
1.4.1 JP 1,8 / 2 80 01-02-2027 09-02-2027 —
1.4.2 JP 1,8 / 2 80 01-02-2027 09-02-2027 —
1.5.1 CAL 1,8 / 2 80 01-03-2027 09-03-2027 —
1.6.1 JP 1,8 / 2 80 01-03-2027 09-03-2027 —
1.7.1 JP 1,8 / 2 80 01-04-2027 09-04-2027 —
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
66


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 11 — continuación
Paquete Rol Personas (prom.
/ máx.)
HH Inicio Fin Predecesoras (cuenta o paquete)
1.7.2 JP 1,8 / 2 80 03-04-2028 11-04-2028 —
1.9.1 SEG 1,8 / 2 80 01-02-2027 09-02-2027 —
1.9.2 SEG 1,8 / 2 80 01-02-2027 09-02-2027 —
1.9.3 SEG 1,8 / 2 80 01-03-2027 09-03-2027 —
2.1.1 ARQ 1,8 / 2 240 01-03-2027 29-03-2027 1.2.1 (D-01, por etapa)
2.1.2 ARQ 1,8 / 2 240 01-03-2027 29-03-2027 —
2.1.3 DAT 1,8 / 2 240 01-03-2027 29-03-2027 —
2.1.4 ARQ 3,1 / 4 240 01-02-2028 16-02-2028 —
2.2.1 SEG 1,8 / 2 240 01-03-2027 29-03-2027 —
2.2.3 SEG 3,1 / 4 240 01-04-2027 16-04-2027 —
2.2.4 SEG 1,8 / 2 240 01-03-2027 29-03-2027 —
2.3.1 SRE 1,8 / 2 240 01-02-2027 01-03-2027 —
2.3.2 SRE 1,8 / 2 240 01-02-2027 01-03-2027 —
2.3.3 SRE 1,8 / 2 240 01-03-2027 29-03-2027 —
2.4.1 ARQ 4,2 / 5 240 19-04-2027 29-04-2027 2.1.1–2.1.3, 2.2.1, 2.2.3, 2.2.4
2.4.2 ARQ 4,7 / 5 240 17-02-2028 28-02-2028 1.2.5, 2.1.4
2.5.1 SRE 1,8 / 2 240 01-04-2027 29-04-2027 —
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
67


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 11 — continuación
Paquete Rol Personas (prom.
/ máx.)
HH Inicio Fin Predecesoras (cuenta o paquete)
2.5.2 SRE 1,8 / 2 240 01-04-2027 29-04-2027 —
2.6.1 IMP 1,8 / 2 240 01-03-2027 29-03-2027 —
2.6.2 IMP 1,8 / 2 240 01-04-2027 29-04-2027 —
2.6.3 IMP 1,8 / 2 240 03-05-2027 31-05-2027 —
3.1.1 SRE 2,5 / 3 240 01-06-2027 18-06-2027 3.2.1, 3.2.2, 3.2.4, 3.2.5 (D-08)
3.1.2 SRE 2,5 / 3 240 01-06-2027 18-06-2027 3.2.1, 3.2.2, 3.2.4, 3.2.5 (D-08)
3.1.3 SRE 2,5 / 3 240 01-06-2027 18-06-2027 3.2.1, 3.2.2, 3.2.4, 3.2.5 (D-08)
3.1.4 SRE 1,8 / 2 240 03-05-2027 31-05-2027 —
3.1.5 SRE 2,5 / 3 240 01-06-2027 18-06-2027 —
3.2.1 SRE 1,8 / 2 240 03-05-2027 31-05-2027 5.2.1 (D-07)
3.2.2 SRE 1,8 / 2 240 03-05-2027 31-05-2027 5.2.1 (D-07)
3.2.3 SRE 1,8 / 2 240 03-05-2027 31-05-2027 5.2.1 (D-07)
3.2.4 SRE 1,8 / 2 240 03-05-2027 31-05-2027 5.2.1 (D-07)
3.2.5 SEG 1,8 / 2 240 03-05-2027 31-05-2027 5.2.1 (D-07)
3.2.6 SRE 1,8 / 2 240 01-06-2027 29-06-2027 5.2.1 (D-07)
3.3.1 SEG 3,3 / 4 480 01-06-2027 05-08-2027 2.2.1 (D-06)
3.3.2 ARQ 3,6 / 4 480 01-06-2027 01-07-2027 1.2.3 (D-02)
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
68


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 11 — continuación
Paquete Rol Personas (prom.
/ máx.)
HH Inicio Fin Predecesoras (cuenta o paquete)
3.3.3 ARQ 3,3 / 4 480 01-06-2027 07-07-2027 —
3.3.4 ARQ 3,6 / 4 480 10-06-2027 12-07-2027 —
3.3.5 ARQ 3,3 / 4 480 01-06-2027 03-08-2027 —
3.3.6 ARQ 3,3 / 4 480 07-06-2027 03-08-2027 —
3.4.1 DES 7,1 / 12 960 10-06-2027 10-08-2027 2.4.1, 2.6.2, 3.1 (QA), 3.3 (CC)
3.4.2 DES 7,5 / 12 960 10-06-2027 11-08-2027 2.4.1, 2.6.2, 3.1 (QA), 3.3 (CC)
3.4.3 DES 6,0 / 12 960 14-06-2027 18-08-2027 2.4.1, 2.6.2, 3.1 (QA), 3.3 (CC), 3.4.1/3.4.2 (interfaz)
3.4.4 DES 11,8 / 12 1440 14-06-2027 29-09-2027 2.4.1, 2.6.2, 3.1 (QA), 3.3 (CC), 3.4.1/3.4.2 (interfaz),
2.4.3, 2.4.4
3.4.5 DES 11,3 / 12 1440 14-06-2027 30-08-2027 2.4.1, 2.6.2, 3.1 (QA), 3.2.3, 3.3 (CC), 2.4.3, 2.4.4
3.4.6 DES 7,5 / 12 960 16-06-2027 17-08-2027 2.4.1, 2.6.2, 3.1 (QA), 3.3 (CC), 3.4.2 (CC)
3.4.7 DES 8,3 / 12 960 16-06-2027 08-09-2027 1.2.2, 2.4.1, 2.6.2, 3.1 (QA), 3.3 (CC), 3.4.3/3.4.6 (inter-
faz)
3.4.8 DES 8,3 / 12 960 16-06-2027 09-09-2027 2.4.1, 2.6.2, 3.1 (QA), 3.3 (CC), 3.4.3/3.4.6 (interfaz)
3.4.9 DES 8,3 / 12 960 18-06-2027 30-09-2027 2.4.1, 2.6.2, 3.1 (QA), 3.3 (CC)
3.4.10 DES 7,5 / 12 960 10-06-2027 04-10-2027 2.4.1, 2.6.2, 3.1 (QA), 3.3 (CC), 3.4.8 (interfaz)
3.4.11 DAT 8,9 / 12 960 02-09-2027 27-09-2027 2.4.1, 2.6.2, 3.1 (QA), 3.3 (CC)
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
69


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 11 — continuación
Paquete Rol Personas (prom.
/ máx.)
HH Inicio Fin Predecesoras (cuenta o paquete)
3.5.1 DES 4,7 / 5 960 15-03-2028 28-04-2028 1.2.5, 2.4.2 (D-29)
3.5.2 DES 4,7 / 5 960 15-03-2028 28-04-2028 1.2.5, 2.4.2 (D-29)
3.5.3 DES 4,7 / 5 960 15-03-2028 28-04-2028 1.2.5, 2.4.2 (D-29)
3.5.4 DAT 4,7 / 5 960 15-03-2028 28-04-2028 1.2.5, 2.4.2 (D-29)
3.6.1 DAT 3,3 / 4 480 02-08-2027 01-09-2027 —
3.6.2 DES 3,3 / 4 480 01-07-2027 02-08-2027 —
3.6.3 DES 3,3 / 4 480 01-07-2027 02-08-2027 —
3.6.4 DES 3,3 / 4 480 01-07-2027 02-08-2027 —
3.6.5 DES 2,1 / 4 480 01-02-2028 04-07-2028 —
3.6.6 DES 2,1 / 4 480 01-06-2028 23-08-2028 —
3.7.1 DAT 3,3 / 4 480 04-08-2027 01-10-2027 —
3.7.2 DAT 3,6 / 4 480 04-10-2027 03-11-2027 —
3.7.3 DAT 3,3 / 4 480 01-12-2027 31-12-2027 —
3.7.4 DAT 3,3 / 4 480 01-12-2027 31-12-2027 —
3.7.5 DAT 3,9 / 5 480 03-01-2028 27-01-2028 3.7.1, 3.7.2, 3.7.3, 3.7.4
3.8.1 CAL 1,8 / 2 160 05-10-2027 22-10-2027 3.4, 3.6.1–3.6.4 (D-20)
3.8.2 CAL 2,5 / 3 320 25-10-2027 19-11-2027 3.8.1
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
70


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 11 — continuación
Paquete Rol Personas (prom.
/ máx.)
HH Inicio Fin Predecesoras (cuenta o paquete)
3.8.3 CAL 2,5 / 3 320 25-10-2027 19-11-2027 3.8.1
3.8.4 CAL 3,6 / 4 320 25-10-2027 11-11-2027 3.8.1
3.8.5 CAL 3,6 / 4 320 25-10-2027 11-11-2027 3.8.1
3.8.6 SEG 3,9 / 6 320 25-10-2027 11-11-2027 3.8.1
3.8.7 CAL 3,1 / 4 160 22-11-2027 01-12-2027 3.8.2, 3.8.3, 3.8.4, 3.8.5, 3.8.6, 3.8.8
3.8.8 SRE 3,6 / 4 320 25-10-2027 11-11-2027 3.8.1
3.9.1 CAL 1,8 / 2 160 02-05-2028 18-05-2028 3.5
3.9.2 CAL 5,0 / 5 320 02-06-2028 15-06-2028 3.9.1
3.9.3 CAL 5,0 / 5 320 19-05-2028 01-06-2028 3.9.1
3.9.4 CAL 5,0 / 5 320 19-05-2028 01-06-2028 3.9.1
3.9.5 SEG 4,2 / 5 160 19-05-2028 26-05-2028 3.9.1
3.9.6 CAL 3,6 / 4 160 16-06-2028 28-06-2028 3.9.1, 3.9.2, 3.9.3, 3.9.4, 3.9.5, 3.9.7
3.9.7 SRE 2,5 / 3 160 19-05-2028 01-06-2028 3.9.1
3.10.1.1 DAT 1,8 / 2 240 02-08-2027 08-10-2027 —
3.10.1.2 DAT 1,8 / 2 240 01-10-2027 19-11-2027 —
3.10.1.3 DAT 1,8 / 2 240 01-10-2027 19-11-2027 —
3.10.1.4 DAT 1,8 / 2 240 01-12-2027 20-03-2028 —
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
71


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 11 — continuación
Paquete Rol Personas (prom.
/ máx.)
HH Inicio Fin Predecesoras (cuenta o paquete)
3.10.2.1 CAL 1,8 / 2 240 01-03-2027 20-04-2027 —
3.10.2.2 CAL 1,8 / 2 240 01-04-2027 09-06-2027 —
3.10.2.3 CAL 1,8 / 2 240 01-06-2027 08-10-2027 —
3.10.2.4 CAL 1,8 / 2 240 01-12-2027 20-03-2028 —
3.10.3.1 DAT 1,8 / 2 240 01-04-2027 09-06-2027 —
3.10.3.2 DAT 1,8 / 2 240 07-06-2027 20-09-2027 —
3.10.3.3 DAT 1,8 / 2 240 01-10-2027 19-11-2027 —
3.10.3.4 DAT 1,8 / 2 240 01-12-2027 20-03-2028 —
3.10.4.1 IMP 1,8 / 2 240 01-02-2028 21-03-2028 —
3.10.4.2 IMP 1,8 / 2 240 01-03-2028 19-04-2028 —
3.10.4.3 IMP 1,8 / 2 240 03-04-2028 09-06-2028 —
3.10.4.4 IMP 1,8 / 2 240 03-07-2028 29-09-2028 —
4.1.1 IMP 1,8 / 2 80 02-11-2027 10-11-2027 —
4.1.2 IMP 1,8 / 2 80 01-12-2027 10-12-2027 —
4.1.3 IMP 1,8 / 2 80 01-06-2028 09-06-2028 —
4.2.3 JP 1,8 / 2 80 05-05-2028 15-05-2028 4.2.1, 7.3.1 (D-28)
4.3.3 JP 1,8 / 2 80 02-10-2028 11-10-2028 4.3.1, 4.3.4, 7.1.4, 7.3.2 (D-33)
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
72


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 11 — continuación
Paquete Rol Personas (prom.
/ máx.)
HH Inicio Fin Predecesoras (cuenta o paquete)
4.3.4 JP 1,8 / 2 80 13-09-2028 25-09-2028 —
5.1.1 ARQ 1,8 / 2 80 01-03-2027 09-03-2027 —
5.1.2 ARQ 1,8 / 2 80 02-03-2027 10-03-2027 2.3.1, 2.3.2 (D-09)
5.1.3 SRE 1,8 / 2 80 01-06-2027 09-06-2027 —
5.2.1 SRE 1,8 / 2 80 01-03-2027 09-03-2027 —
5.2.2 SRE 1,8 / 2 80 03-05-2027 11-05-2027 —
5.2.3 ARQ 1,8 / 2 80 03-05-2027 11-05-2027 —
5.3.1 SRE 1,8 / 2 80 03-05-2027 11-05-2027 —
5.3.2 SRE 1,8 / 2 80 03-05-2027 11-05-2027 —
5.3.3 SRE 1,8 / 2 80 03-05-2027 11-05-2027 —
5.4.1 IMP 1,8 / 2 80 01-10-2027 12-10-2027 —
5.4.2 IMP 1,8 / 2 80 01-10-2027 12-10-2027 —
5.4.3 JP 1,8 / 2 80 01-06-2028 09-06-2028 —
5.4.4 JP 1,8 / 2 80 02-08-2027 10-08-2027 —
6.1.1 SRE 1,8 / 2 160 01-04-2027 20-04-2027 5.1.2 (D-10)
6.1.2 SRE 1,8 / 2 160 01-04-2027 20-04-2027 5.1.2 (D-10)
6.1.3 SRE 1,8 / 2 160 01-04-2027 20-04-2027 5.1.2 (D-10)
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
73


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 11 — continuación
Paquete Rol Personas (prom.
/ máx.)
HH Inicio Fin Predecesoras (cuenta o paquete)
6.1.4 SRE 1,8 / 2 160 01-04-2027 20-04-2027 5.1.2 (D-10)
6.1.5 SRE 1,8 / 2 160 03-05-2027 20-05-2027 5.1.2, 6.1.1–6.1.4 (recepción)
6.2.1 SRE 1,8 / 2 160 03-05-2027 20-05-2027 —
6.2.2 SRE 1,8 / 2 160 01-07-2027 20-07-2027 —
6.2.3 SRE 1,8 / 2 160 02-08-2027 19-08-2027 —
6.3.1 SRE 1,8 / 2 160 24-05-2027 09-06-2027 6.1.5 (D-11)
6.3.2 SRE 1,8 / 2 160 24-05-2027 09-06-2027 6.1.5 (D-11)
6.3.3 SRE 1,8 / 2 160 03-05-2027 20-05-2027 —
6.3.4 SRE 1,8 / 2 160 01-10-2027 20-10-2027 —
6.4.1 SEG 1,8 / 2 160 01-06-2027 18-06-2027 —
6.4.2 SEG 1,8 / 2 160 07-06-2027 24-06-2027 —
6.4.3 SEG 1,8 / 2 160 22-06-2027 09-07-2027 —
6.5.1 SRE 1,8 / 2 160 06-10-2027 14-01-2028 3.2.6
6.5.2 SRE 1,8 / 2 160 04-11-2027 14-01-2028 —
6.5.3 SRE 1,8 / 2 160 06-10-2027 25-11-2027 —
6.5.4 SRE 2 / 3 320 01-09-2027 14-01-2028 5.1.4, 2.4.3, 2.4.4; cuatro kits al 30-09-2027 para 4.1.4
6.5.5 SRE 1,8 / 2 160 04-11-2027 14-01-2028 —
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
74


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 11 — continuación
Paquete Rol Personas (prom.
/ máx.)
HH Inicio Fin Predecesoras (cuenta o paquete)
6.5.6 SRE 1,8 / 2 160 06-10-2027 14-01-2028 —
6.6.1 SRE 1,8 / 2 160 10-06-2027 30-06-2027 6.3.1–6.3.3 (D-12)
6.6.2 SRE 1,8 / 2 160 10-06-2027 30-06-2027 6.3.1–6.3.3 (D-12)
6.6.3 SRE 3,6 / 4 160 10-06-2027 18-06-2027 6.3.1–6.3.3 (D-12)
7.1.1 IMP 1,8 / 2 160 02-11-2027 24-12-2027 —
7.1.6 IMP 1,8 / 2 160 02-11-2027 24-12-2027 —
7.2.2 IMP 1,8 / 2 160 02-05-2028 23-06-2028 —
7.2.3 IMP 1,8 / 2 160 01-03-2027 25-05-2027 —
7.3.1 IMP 1,8 / 2 160 01-02-2028 24-03-2028 —
7.3.2 IMP 1,8 / 2 160 03-07-2028 25-07-2028 —
9.1.1 DES 1,8 / 2 80 02-10-2028 11-10-2028 —
9.1.2 JP 1,8 / 2 80 26-10-2028 07-11-2028 4.3.3
9.2.2 SEG 1,8 / 2 80 01-09-2031 09-09-2031 —
2.4.3 SRE 2,5 / 3 320 01-04-2027 30-04-2027 5.1.4, 5.3.4; prototipo Greengrass y TC58e
2.4.4 ARQ 2,5 / 3 240 03-05-2027 28-05-2027 2.4.3; Calidad del CLIENTE
4.1.4 IMP 1,7 / 2 320 09-11-2027 20-12-2027 2.4.3, 2.4.4, 3.4.4, 3.4.5, 3.8.1 y H4, 5.3.4; cuatro actas
parciales 6.5.4
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
75


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 11 — continuación
Paquete Rol Personas (prom.
/ máx.)
HH Inicio Fin Predecesoras (cuenta o paquete)
5.1.4 ARQ 1,8 / 2 240 01-02-2027 31-03-2027 Especificación SD4; ocho semanas de homologación
móvil
5.3.4 SRE 1,8 / 2 80 01-03-2027 12-03-2027 5.1.4 (especificación, CC); servicio de banco antes de
2.4.3
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
76


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 12 Actividades de los paquetes que terminan hasta el H2. Fuente: elaboración a partir de la Tabla 11. Bloque 1 de 2.
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
1.1.1.A01 Elaboración, revisión y
aprobación del entregable
JP 2 80 01-02-2027 09-02-2027 7 —
1.1.2.A01 Elaboración, revisión y
aprobación del entregable
JP 2 80 01-02-2027 09-02-2027 7 —
1.1.3.A01 Elaboración, revisión y
aprobación del entregable
JP 2 80 01-02-2027 09-02-2027 7 —
1.2.1.A01 Elaboración, revisión y
aprobación del entregable
ARQ 2 80 01-02-2027 09-02-2027 7 —
1.2.3.A01 Elaboración, revisión y
aprobación del entregable
ARQ 2 80 01-02-2027 09-02-2027 7 —
1.2.4.A01 Elaboración, revisión y
aprobación del entregable
CAL 2 80 01-03-2027 09-03-2027 7 —
1.3.1.A01 Elaboración, revisión y
aprobación del entregable
JP 2 80 10-02-2027 18-02-2027 7 —
1.3.2.A01 Elaboración, revisión y
aprobación del entregable
JP 2 80 01-03-2027 09-03-2027 7 —
1.3.3.A01 Elaboración, revisión y
aprobación del entregable
JP 2 80 01-03-2027 09-03-2027 7 —
1.3.4.A01 Elaboración, revisión y
aprobación del entregable
JP 2 80 01-03-2027 09-03-2027 7 —
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
77


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 12 — continuación
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
1.4.1.A01 Elaboración, revisión y
aprobación del entregable
JP 2 80 01-02-2027 09-02-2027 7 —
1.4.2.A01 Elaboración, revisión y
aprobación del entregable
JP 2 80 01-02-2027 09-02-2027 7 —
1.5.1.A01 Elaboración, revisión y
aprobación del entregable
CAL 2 80 01-03-2027 09-03-2027 7 —
1.6.1.A01 Elaboración, revisión y
aprobación del entregable
JP 2 80 01-03-2027 09-03-2027 7 —
1.7.1.A01 Elaboración, revisión y
aprobación del entregable
JP 2 80 01-04-2027 09-04-2027 7 —
1.9.1.A01 Elaboración, revisión y
aprobación del entregable
SEG 2 80 01-02-2027 09-02-2027 7 —
1.9.2.A01 Elaboración, revisión y
aprobación del entregable
SEG 2 80 01-02-2027 09-02-2027 7 —
1.9.3.A01 Elaboración, revisión y
aprobación del entregable
SEG 2 80 01-03-2027 09-03-2027 7 —
2.1.1.A01 Levantamiento de insu-
mos y análisis
ARQ 2 80 01-03-2027 09-03-2027 7 1.2.1.A01
2.1.1.A02 Elaboración del entrega-
ble
ARQ 2 80 10-03-2027 18-03-2027 7 2.1.1.A01
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
78


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 12 — continuación
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
2.1.1.A03 Revisión, corrección y
presentación para aproba-
ción
ARQ 2 80 19-03-2027 29-03-2027 7 2.1.1.A02
2.1.2.A01 Levantamiento de insu-
mos y análisis
ARQ 2 80 01-03-2027 09-03-2027 7 —
2.1.2.A02 Elaboración del entrega-
ble
ARQ 2 80 10-03-2027 18-03-2027 7 2.1.2.A01
2.1.2.A03 Revisión, corrección y
presentación para aproba-
ción
ARQ 2 80 19-03-2027 29-03-2027 7 2.1.2.A02
2.1.3.A01 Levantamiento de insu-
mos y análisis
DAT 2 80 01-03-2027 09-03-2027 7 —
2.1.3.A02 Elaboración del entrega-
ble
DAT 2 80 10-03-2027 18-03-2027 7 2.1.3.A01
2.1.3.A03 Revisión, corrección y
presentación para aproba-
ción
DAT 2 80 19-03-2027 29-03-2027 7 2.1.3.A02
2.2.1.A01 Levantamiento de insu-
mos y análisis
SEG 2 80 01-03-2027 09-03-2027 7 —
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
79


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 12 — continuación
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
2.2.1.A02 Elaboración del entrega-
ble
SEG 2 80 10-03-2027 18-03-2027 7 2.2.1.A01
2.2.1.A03 Revisión, corrección y
presentación para aproba-
ción
SEG 2 80 19-03-2027 29-03-2027 7 2.2.1.A02
2.2.3.A01 Levantamiento de insu-
mos y análisis
SEG 4 80 01-04-2027 06-04-2027 4 —
2.2.3.A02 Elaboración del entrega-
ble
SEG 4 80 07-04-2027 12-04-2027 4 2.2.3.A01
2.2.3.A03 Revisión, corrección y
presentación para aproba-
ción
SEG 4 80 13-04-2027 16-04-2027 4 2.2.3.A02
2.2.4.A01 Levantamiento de insu-
mos y análisis
SEG 2 80 01-03-2027 09-03-2027 7 —
2.2.4.A02 Elaboración del entrega-
ble
SEG 2 80 10-03-2027 18-03-2027 7 2.2.4.A01
2.2.4.A03 Revisión, corrección y
presentación para aproba-
ción
SEG 2 80 19-03-2027 29-03-2027 7 2.2.4.A02
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
80


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 12 — continuación
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
2.3.1.A01 Levantamiento de insu-
mos y análisis
SRE 2 80 01-02-2027 09-02-2027 7 —
2.3.1.A02 Elaboración del entrega-
ble
SRE 2 80 10-02-2027 18-02-2027 7 2.3.1.A01
2.3.1.A03 Revisión, corrección y
presentación para aproba-
ción
SRE 2 80 19-02-2027 01-03-2027 7 2.3.1.A02
2.3.2.A01 Levantamiento de insu-
mos y análisis
SRE 2 80 01-02-2027 09-02-2027 7 —
2.3.2.A02 Elaboración del entrega-
ble
SRE 2 80 10-02-2027 18-02-2027 7 2.3.2.A01
2.3.2.A03 Revisión, corrección y
presentación para aproba-
ción
SRE 2 80 19-02-2027 01-03-2027 7 2.3.2.A02
2.3.3.A01 Levantamiento de insu-
mos y análisis
SRE 2 80 01-03-2027 09-03-2027 7 —
2.3.3.A02 Elaboración del entrega-
ble
SRE 2 80 10-03-2027 18-03-2027 7 2.3.3.A01
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
81


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 12 — continuación
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
2.3.3.A03 Revisión, corrección y
presentación para aproba-
ción
SRE 2 80 19-03-2027 29-03-2027 7 2.3.3.A02
2.4.1.A01 Levantamiento de insu-
mos y análisis
ARQ 5 80 19-04-2027 21-04-2027 3 2.1.1.A03, 2.1.2.A03,
2.1.3.A03, 2.2.1.A03,
2.2.3.A03, 2.2.4.A03
2.4.1.A02 Elaboración del entrega-
ble
ARQ 5 80 22-04-2027 26-04-2027 3 2.4.1.A01
2.4.1.A03 Revisión, corrección y
presentación para aproba-
ción
ARQ 5 80 27-04-2027 29-04-2027 3 2.4.1.A02
2.5.1.A01 Levantamiento de insu-
mos y análisis
SRE 2 80 01-04-2027 09-04-2027 7 —
2.5.1.A02 Elaboración del entrega-
ble
SRE 2 80 12-04-2027 20-04-2027 7 2.5.1.A01
2.5.1.A03 Revisión, corrección y
presentación para aproba-
ción
SRE 2 80 21-04-2027 29-04-2027 7 2.5.1.A02
2.5.2.A01 Levantamiento de insu-
mos y análisis
SRE 2 80 01-04-2027 09-04-2027 7 —
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
82


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 12 — continuación
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
2.5.2.A02 Elaboración del entrega-
ble
SRE 2 80 12-04-2027 20-04-2027 7 2.5.2.A01
2.5.2.A03 Revisión, corrección y
presentación para aproba-
ción
SRE 2 80 21-04-2027 29-04-2027 7 2.5.2.A02
Tabla 13 Actividades de los paquetes que terminan hasta el H2. Fuente: elaboración a partir de la Tabla 11. Bloque 2 de 2.
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
2.6.1.A01 Levantamiento de insu-
mos y análisis
IMP 2 80 01-03-2027 09-03-2027 7 —
2.6.1.A02 Elaboración del entrega-
ble
IMP 2 80 10-03-2027 18-03-2027 7 2.6.1.A01
2.6.1.A03 Revisión, corrección y
presentación para aproba-
ción
IMP 2 80 19-03-2027 29-03-2027 7 2.6.1.A02
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
83


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 13 — continuación
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
2.6.2.A01 Levantamiento de insu-
mos y análisis
IMP 2 80 01-04-2027 09-04-2027 7 —
2.6.2.A02 Elaboración del entrega-
ble
IMP 2 80 12-04-2027 20-04-2027 7 2.6.2.A01
2.6.2.A03 Revisión, corrección y
presentación para aproba-
ción
IMP 2 80 21-04-2027 29-04-2027 7 2.6.2.A02
2.6.3.A01 Levantamiento de insu-
mos y análisis
IMP 2 80 03-05-2027 11-05-2027 7 —
2.6.3.A02 Elaboración del entrega-
ble
IMP 2 80 12-05-2027 20-05-2027 7 2.6.3.A01
2.6.3.A03 Revisión, corrección y
presentación para aproba-
ción
IMP 2 80 21-05-2027 31-05-2027 7 2.6.3.A02
3.1.4.A01 Levantamiento de insu-
mos y análisis
SRE 2 80 03-05-2027 11-05-2027 7 —
3.1.4.A02 Elaboración del entrega-
ble
SRE 2 80 12-05-2027 20-05-2027 7 3.1.4.A01
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
84


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 13 — continuación
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
3.1.4.A03 Revisión, corrección y
presentación para aproba-
ción
SRE 2 80 21-05-2027 31-05-2027 7 3.1.4.A02
3.2.1.A01 Levantamiento de insu-
mos y análisis
SRE 2 80 03-05-2027 11-05-2027 7 5.2.1.A01
3.2.1.A02 Elaboración del entrega-
ble
SRE 2 80 12-05-2027 20-05-2027 7 3.2.1.A01
3.2.1.A03 Revisión, corrección y
presentación para aproba-
ción
SRE 2 80 21-05-2027 31-05-2027 7 3.2.1.A02
3.2.2.A01 Levantamiento de insu-
mos y análisis
SRE 2 80 03-05-2027 11-05-2027 7 5.2.1.A01
3.2.2.A02 Elaboración del entrega-
ble
SRE 2 80 12-05-2027 20-05-2027 7 3.2.2.A01
3.2.2.A03 Revisión, corrección y
presentación para aproba-
ción
SRE 2 80 21-05-2027 31-05-2027 7 3.2.2.A02
3.2.3.A01 Levantamiento de insu-
mos y análisis
SRE 2 80 03-05-2027 11-05-2027 7 5.2.1.A01
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
85


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 13 — continuación
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
3.2.3.A02 Elaboración del entrega-
ble
SRE 2 80 12-05-2027 20-05-2027 7 3.2.3.A01
3.2.3.A03 Revisión, corrección y
presentación para aproba-
ción
SRE 2 80 21-05-2027 31-05-2027 7 3.2.3.A02
3.2.4.A01 Levantamiento de insu-
mos y análisis
SRE 2 80 03-05-2027 11-05-2027 7 5.2.1.A01
3.2.4.A02 Elaboración del entrega-
ble
SRE 2 80 12-05-2027 20-05-2027 7 3.2.4.A01
3.2.4.A03 Revisión, corrección y
presentación para aproba-
ción
SRE 2 80 21-05-2027 31-05-2027 7 3.2.4.A02
3.2.5.A01 Levantamiento de insu-
mos y análisis
SEG 2 80 03-05-2027 11-05-2027 7 5.2.1.A01
3.2.5.A02 Elaboración del entrega-
ble
SEG 2 80 12-05-2027 20-05-2027 7 3.2.5.A01
3.2.5.A03 Revisión, corrección y
presentación para aproba-
ción
SEG 2 80 21-05-2027 31-05-2027 7 3.2.5.A02
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
86


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 13 — continuación
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
3.10.2.1.A01 Levantamiento de insu-
mos y análisis
CAL 2 80 01-03-2027 09-03-2027 7 —
3.10.2.1.A02 Elaboración del entrega-
ble
CAL 2 80 22-03-2027 30-03-2027 7 3.10.2.1.A01
3.10.2.1.A03 Revisión, corrección y
presentación para aproba-
ción
CAL 2 80 12-04-2027 20-04-2027 7 3.10.2.1.A02
5.1.1.A01 Elaboración, revisión y
aprobación del entregable
ARQ 2 80 01-03-2027 09-03-2027 7 —
5.1.2.A01 Elaboración, revisión y
aprobación del entregable
ARQ 2 80 02-03-2027 10-03-2027 7 2.3.1.A03, 2.3.2.A03
5.2.1.A01 Elaboración, revisión y
aprobación del entregable
SRE 2 80 01-03-2027 09-03-2027 7 —
5.2.2.A01 Elaboración, revisión y
aprobación del entregable
SRE 2 80 03-05-2027 11-05-2027 7 —
5.2.3.A01 Elaboración, revisión y
aprobación del entregable
ARQ 2 80 03-05-2027 11-05-2027 7 —
5.3.1.A01 Elaboración, revisión y
aprobación del entregable
SRE 2 80 03-05-2027 11-05-2027 7 —
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
87


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 13 — continuación
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
5.3.2.A01 Elaboración, revisión y
aprobación del entregable
SRE 2 80 03-05-2027 11-05-2027 7 —
5.3.3.A01 Elaboración, revisión y
aprobación del entregable
SRE 2 80 03-05-2027 11-05-2027 7 —
6.1.1.A01 Preparación y ejecución
de la instalación o de la
capacitación
SRE 2 80 01-04-2027 09-04-2027 7 5.1.2.A01
6.1.1.A02 Prueba o evaluación,
corrección y acta
SRE 2 80 12-04-2027 20-04-2027 7 6.1.1.A01
6.1.2.A01 Preparación y ejecución
de la instalación o de la
capacitación
SRE 2 80 01-04-2027 09-04-2027 7 5.1.2.A01
6.1.2.A02 Prueba o evaluación,
corrección y acta
SRE 2 80 12-04-2027 20-04-2027 7 6.1.2.A01
6.1.3.A01 Preparación y ejecución
de la instalación o de la
capacitación
SRE 2 80 01-04-2027 09-04-2027 7 5.1.2.A01
6.1.3.A02 Prueba o evaluación,
corrección y acta
SRE 2 80 12-04-2027 20-04-2027 7 6.1.3.A01
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
88


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 13 — continuación
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
6.1.4.A01 Preparación y ejecución
de la instalación o de la
capacitación
SRE 2 80 01-04-2027 09-04-2027 7 5.1.2.A01
6.1.4.A02 Prueba o evaluación,
corrección y acta
SRE 2 80 12-04-2027 20-04-2027 7 6.1.4.A01
6.1.5.A01 Preparación y ejecución
de la instalación o de la
capacitación
SRE 2 80 03-05-2027 11-05-2027 7 5.1.2.A01,
6.1.1.A02–6.1.4.A02
6.1.5.A02 Prueba o evaluación,
corrección y acta
SRE 2 80 12-05-2027 20-05-2027 7 6.1.5.A01
6.2.1.A01 Preparación y ejecución
de la instalación o de la
capacitación
SRE 2 80 03-05-2027 11-05-2027 7 —
6.2.1.A02 Prueba o evaluación,
corrección y acta
SRE 2 80 12-05-2027 20-05-2027 7 6.2.1.A01
6.3.3.A01 Preparación y ejecución
de la instalación o de la
capacitación
SRE 2 80 03-05-2027 11-05-2027 7 —
6.3.3.A02 Prueba o evaluación,
corrección y acta
SRE 2 80 12-05-2027 20-05-2027 7 6.3.3.A01
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
89


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 13 — continuación
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
7.2.3.A01 Preparación y ejecución
de la instalación o de la
capacitación
IMP 2 80 01-03-2027 09-03-2027 7 —
7.2.3.A02 Prueba o evaluación,
corrección y acta
IMP 2 80 17-05-2027 25-05-2027 7 7.2.3.A01
2.4.3.A01 Montaje de prototipo y
lectura Modbus/Green-
grass
SRE 3 80 01-04-2027 07-04-2027 5 5.1.4, 5.3.4
2.4.3.A02 Alarmas, satélite y segun-
da evaluación
SRE 3 80 08-04-2027 14-04-2027 5 2.4.3.A01
2.4.3.A03 Fallas, órdenes, persisten-
cia y recuperación
SRE 3 80 15-04-2027 21-04-2027 5 2.4.3.A02
2.4.3.A04 Regresión, correcciones y
acta de banco
SRE 3 80 22-04-2027 28-04-2027 5 2.4.3.A03
2.4.4.A01 Preparación de mapeo y
carga de ensayo
ARQ 3 80 03-05-2027 07-05-2027 5 2.4.3
2.4.4.A02 Comparación de núcleo,
simuladores y aire
ARQ 3 80 10-05-2027 14-05-2027 5 2.4.4.A01
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
90


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 13 — continuación
Actividad Nombre Rol Per-
sonas
HH Inicio Fin Días
hábiles
Predecesoras
2.4.4.A03 Punto crítico, volumen,
tolerancias y acta con
Calidad
ARQ 3 80 17-05-2027 21-05-2027 5 2.4.4.A02
5.1.4.A01 Especificación, cotización
local y solicitud de ho-
mologación desde el 1 de
febrero
ARQ 2 80 01-02-2027 09-02-2027 7 Especificación SD4
5.1.4.A02 Evaluación de proveedor
y seguimiento de homolo-
gación
ARQ 2 80 10-02-2027 18-02-2027 7 5.1.4.A01
5.1.4.A03 Verificación de certifica-
dos y compra de prototipo
ARQ 2 80 23-03-2027 31-03-2027 7 5.1.4.A02; ocho semanas
desde inicio de gestión
5.3.4.A01 Contratos móviles y SBD
y habilitación del servicio
de banco
SRE 2 80 01-03-2027 09-03-2027 7 5.1.4.A01 (especificación)
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
91


---

LafroX SpA Formulario T-15: Nivelación de recursos
6.2 Paquetes de esfuerzo continuo
Los paquetes recurrentes (R), de acompañamiento (A) y de cobertura (C) son de nivel de
esfuerzo: no producen un entregable único, sino un servicio o una reunión que se repite. No
se dividen en entregables más pequeños, sino por ocurrencia o por quincena:
• Un paquete con frecuencia propia en el diccionario del T-14 (quincenal, mensual, trimestral,
semestral o anual) tiene una actividad por ocurrencia, ejecutada dentro de una quincena.
Si una ocurrencia supera 64 HH, se reparte entre dos o más personas.
• Un paquete continuo tiene una actividad por quincena. Si la quincena exige más de 64 HH,
la actividad se divide en relevos o puestos: por ejemplo, el NOC 24×7 de un mes de 31 días
requiere 744 ÷ 2 = 372 HH por quincena, es decir, seis relevos de 62 HH.
• Las preparaciones de comités con frecuencia contractual quincenal (1.6.2 y 1.8.3) tienen
menos de 8 HH por ocurrencia. Son la única excepción al mínimo de la regla: se mantienen
por ocurrencia porque la cadencia la fija el artículo 71 de las Bases Administrativas (p. 37) y
no conviene fusionarlas con otra actividad.
Estos 59 paquetes no se descomponen en una lista de actividades distintas, porque su trabajo
se repite: se programan por quincena u ocurrencia, en relevos de hasta 64 HH cada uno. La
Tabla 14 presenta la regla de cada paquete, el número de relevos u ocurrencias que programa
durante el contrato y el esfuerzo máximo de cada uno.
LafroX SpA
Formulario T-15
Media firma: Alex Aravena
92


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 14 Actividades de los paquetes de esfuerzo continuo. Fuente: elaboración a partir de las secciones 4.1, 4.2 y 4.4 y el diccionario de (Formulario T-14).
Paquete Clase Rol Meses E HH Regla de programación Relevos u
ocurrencias
programados
HH máximas
por relevo u
ocurrencia
1.2.2 G IMP 1–3 80 Una actividad por quincena, por presencia continua o
periódica
6 13.3
1.3.5 R JP 1–20 480 Una actividad de nivel de esfuerzo por quincena 40 12.0
1.4.3 R JP 1–56 896 Una actividad de nivel de esfuerzo por quincena 112 8.0
1.5.2 G CAL 6–20 80 Una actividad cada 3 quincenas, por presencia continua
o periódica
10 8.0
1.6.2 R JP 1–20 160 Una actividad por ocurrencia (quincenal, en cada
Comité de Proyecto), ejecutada dentro de una quincena;
1 actividad(es) por ocurrencia
40 4.0
1.8.1 R JP 1–20 320 Una actividad de nivel de esfuerzo por quincena 40 8.0
1.8.2 R JP 1–56 448 Una actividad por ocurrencia (mensual), ejecutada
dentro de una quincena; 1 actividad(es) por ocurrencia
56 8.0
1.8.3 R JP 1–20 240 Una actividad por ocurrencia (quincenal), ejecutada
dentro de una quincena; 1 actividad(es) por ocurrencia
40 6.0
1.8.4 R ARQ 1–56 448 Una actividad por ocurrencia (mensual), ejecutada
dentro de una quincena; 1 actividad(es) por ocurrencia
56 8.0
1.8.5 R SRE 13–56 352 Una actividad por ocurrencia (mensual), ejecutada
dentro de una quincena; 1 actividad(es) por ocurrencia
44 8.0
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
93


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 14 — continuación
Paquete Clase Rol Meses E HH Regla de programación Relevos u
ocurrencias
programados
HH máximas
por relevo u
ocurrencia
1.8.6 R JP 1–20 480 Una actividad por ocurrencia (mensual), ejecutada
dentro de una quincena; 1 actividad(es) por ocurrencia
20 24.0
1.8.7 R JP 2–56 440 Una actividad cada 2 quincenas, ejecutada en la última
quincena del grupo
55 8.0
1.8.8 R JP 1–56 448 Una actividad cada 2 quincenas, ejecutada en la última
quincena del grupo
56 8.0
1.9.4 R SEG 1–56 224 Una actividad por ocurrencia (anual), ejecutada dentro
de una quincena; 1 actividad(es) por ocurrencia
5 44.8
1.9.5 R JP 1–56 224 Una actividad cada 4 quincenas, ejecutada en la última
quincena del grupo
28 8.0
2.2.2 E SEG 3–10 240 Una actividad por quincena, por presencia continua o
periódica
16 15.0
3.11.1 G ARQ 15–21 80 Una actividad cada 2 quincenas, por presencia continua
o periódica
7 11.4
3.11.2 G SRE 10–20 80 Una actividad cada 3 quincenas, por presencia continua
o periódica
8 10.0
3.11.3 G DES 4–20 80 Una actividad cada 4 quincenas, por presencia continua
o periódica
9 8.9
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
94


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 14 — continuación
Paquete Clase Rol Meses E HH Regla de programación Relevos u
ocurrencias
programados
HH máximas
por relevo u
ocurrencia
3.11.4 G DES 4–20 80 Una actividad cada 4 quincenas, por presencia continua
o periódica
9 8.9
3.11.5 G DES 6–20 80 Una actividad cada 3 quincenas, por presencia continua
o periódica
10 8.0
4.2.1 A IMP 13–15 7392 Una actividad de nivel de esfuerzo por quincena, dividi-
da en 20 relevos o puestos
120 61.6
4.2.2 A IMP 16–20 5408 Una actividad de nivel de esfuerzo por quincena, dividi-
da en relevos o puestos según la HH de cada mes
92 61.6
4.3.1 A IMP 19–20 4928 Una actividad de nivel de esfuerzo por quincena, dividi-
da en 20 relevos o puestos
80 61.6
4.3.2 A IMP 21–22 2464 Una actividad de nivel de esfuerzo por quincena, dividi-
da en relevos o puestos según la HH de cada mes
40 62.1
7.1.2 R IMP 13–56 2816 Una actividad de nivel de esfuerzo por quincena 88 32.0
7.1.3 T IMP 11–20 240 Una actividad por quincena, por presencia continua o
periódica
20 12.0
7.1.4 T IMP 15–20 160 2 ocurrencias en la ventana, por presencia continua o
periódica
2 80.0
7.1.5 T IMP 10–18 160 2 ocurrencias en la ventana, por presencia continua o
periódica
2 80.0
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
95


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 14 — continuación
Paquete Clase Rol Meses E HH Regla de programación Relevos u
ocurrencias
programados
HH máximas
por relevo u
ocurrencia
7.2.1 T IMP 10–16 160 Una actividad por quincena, por presencia continua o
periódica
14 11.4
7.2.4 T IMP 8–20 240 Una actividad por quincena, por presencia continua o
periódica
26 9.24
7.2.5 T IMP 13–21 160 Una actividad por quincena, por presencia continua o
periódica
18 8.9
8.1.1 C SRE 21–56 26280 Una actividad de nivel de esfuerzo por quincena, dividi-
da en relevos o puestos según la HH de cada mes
432 62.0
8.1.2 C SRE 21–56 54239 Una actividad de nivel de esfuerzo por quincena, dividi-
da en relevos o puestos según la HH de cada mes
679 79.9
8.1.3 V SRE 21–56 560 Siete campañas de conmutación real de 80 HH, con
cinco actividades por campaña
35 16.0
8.1.4 R JP 21–56 288 Una actividad por ocurrencia (anual), ejecutada dentro
de una quincena; 2 actividad(es) por ocurrencia
6 48.0
8.1.5 C SEG 13–56 32112 Una actividad de nivel de esfuerzo por quincena, dividi-
da en relevos o puestos según la HH de cada mes
528 62.0
8.1.6 R SRE 21–56 576 Una actividad por ocurrencia (mensual), ejecutada
dentro de una quincena; 1 actividad(es) por ocurrencia
36 16.0
8.2.1 R DES 21–56 4608 Una actividad de nivel de esfuerzo por quincena 72 64.0
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
96


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 14 — continuación
Paquete Clase Rol Meses E HH Regla de programación Relevos u
ocurrencias
programados
HH máximas
por relevo u
ocurrencia
8.2.2 R SEG 21–56 1152 Una actividad de nivel de esfuerzo por quincena 72 16.0
8.2.3 R SRE 21–56 1152 Una actividad de nivel de esfuerzo por quincena 72 16.0
8.2.4 R DES 21–56 2304 Una actividad de nivel de esfuerzo por quincena 72 32.0
8.2.5 R SRE 21–56 288 Una actividad por ocurrencia (anual), ejecutada dentro
de una quincena; 2 actividad(es) por ocurrencia
6 48.0
8.2.6 R SRE 21–56 288 Una actividad por ocurrencia (semestral), ejecutada
dentro de una quincena; 1 actividad(es) por ocurrencia
6 48.0
8.2.7 R SRE 21–56 864 Una actividad de nivel de esfuerzo por quincena 72 12.0
8.3.1 R CAL 21–56 576 Una actividad de nivel de esfuerzo por quincena 72 8.0
8.3.2 R DAT 21–56 288 Una actividad por ocurrencia (semestral), ejecutada
dentro de una quincena; 1 actividad(es) por ocurrencia
6 48.0
8.3.3 G JP 21–23 80 3 ocurrencias en la ventana, por presencia continua o
periódica
3 26.7
8.3.4 R JP 24–56 528 Una actividad por ocurrencia (mensual), ejecutada
dentro de una quincena; 1 actividad(es) por ocurrencia
33 16.0
8.3.5 G IMP 22–26 80 Una actividad por quincena, por presencia continua o
periódica
10 8.0
continúa en la página siguiente
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
97


---

LafroX
SpA
Formulario
T-15:
Nivelación
de
recursos
Tabla 14 — continuación
Paquete Clase Rol Meses E HH Regla de programación Relevos u
ocurrencias
programados
HH máximas
por relevo u
ocurrencia
8.3.6 G IMP 24–27 80 Una actividad por quincena, por presencia continua o
periódica
8 10.0
8.4.1 R SRE 21–56 576 Una actividad por ocurrencia (trimestral), ejecutada
dentro de una quincena; 1 actividad(es) por ocurrencia
12 48.0
8.4.2 R SRE 21–56 576 Una actividad por ocurrencia (mensual), ejecutada
dentro de una quincena; 1 actividad(es) por ocurrencia
36 16.0
8.4.3 R SRE 21–56 288 Una actividad por ocurrencia (anual), ejecutada dentro
de una quincena; 2 actividad(es) por ocurrencia
6 48.0
8.4.4 R JP 21–56 288 Una actividad por ocurrencia (semestral), ejecutada
dentro de una quincena; 1 actividad(es) por ocurrencia
6 48.0
8.5.1 R IMP 21–56 1152 Una actividad por ocurrencia (dos jornadas por año),
ejecutada dentro de una quincena; 3 actividad(es) por
ocurrencia
18 64.0
8.5.2 G IMP 21–27 80 Una actividad cada 2 quincenas, por presencia continua
o periódica
7 11.4
8.5.3 R SRE 21–56 576 Una actividad de nivel de esfuerzo por quincena 72 8.0
9.2.1 G JP 54–56 80 Una actividad por quincena, por presencia continua o
periódica
6 13.3
LafroX
SpA
Formulario
T-15
Media
firma:
Alex
Aravena
98


---

LafroX SpA Formulario T-15: Nivelación de recursos
Así, los 227 paquetes quedan programados de dos formas: los 168 paquetes con entregable,
con fechas en la Tabla 11 y actividades de 80 HH o menos detalladas hasta el H2 y luego por
planificación gradual, y 59 paquetes de esfuerzo continuo que se programan por quincena u
ocurrencia, en relevos de hasta 64 HH cada uno. En ambos casos nada supera una quincena.
Ningún paquete se informa al 50 % durante semanas: el avance de cada quincena se mide por
las actividades terminadas y por los relevos u ocurrencias cumplidos, que alimentan el valor
ganado del SD6, sección 6.1.5.
## Referencias
Las fuentes citadas en este formulario se listan en formato APA 7.ª edición. Las Bases se
citan en el texto con su documento y el artículo, capítulo, sección o código del requisito.
• Dirección del Trabajo. (s.f.). Código del Trabajo: artículos 35 y 35 ter y compendio de feriados
legales. https://dt.gob.cl/legislacion/1624/articles-95516_recurso_1.pdf
• Distribuidora Puelche S.A. (2026a). Bases Administrativas, Licitación TFEP-01/2026.
• Distribuidora Puelche S.A. (2026b). Bases Técnicas Transversales, Licitación TFEP-01/2026.
• Distribuidora Puelche S.A. (2026c). Bases Técnicas del Caso Logística.
• Malcolm, D. G., Roseboom, J. H., Clark, C. E., & Fazar, W. (1959). Application of a technique
for research and development program evaluation. Operations Research, 7(5), 646–669.
• Project Management Institute. (2017). Guía de los fundamentos para la dirección de proyectos
(Guía del PMBOK) (6.ª ed.). Project Management Institute.
LafroX SpA
Formulario T-15
Media firma: Alex Aravena
99


---
