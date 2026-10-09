# Formulario T-15: Nivelación de recursos

Este formulario presenta la información de planificación que pide el Formulario T-15 de las Bases Administrativas para el Subdocumento 7: el método con que se estiman las horas hombre de cada paquete, la programación sobre la red de dependencias, la ruta crítica y sus holguras, y los frentes de trabajo, con el detalle de los solapamientos de los meses 13 a 15 y 19 a 20. Los paquetes de trabajo son los de la EDT del Formulario T-14. Este formulario no contiene precios ni costos (Art. 50.2).

## 1 Método de estimación y de programación

La estimación y la programación siguen el PMBOK y la técnica PERT, de modo que cada duración y cada holgura se puedan reconstruir a partir de valores declarados.

### 1.1 Estimación

El esfuerzo de cada paquete se estima con tres valores en horas hombre (Project Management Institute [PMI], 2017, p. 201): el optimista (O), que corresponde al mejor escenario; el más probable (M), con recursos y productividad realistas; y el pesimista (P), que corresponde al peor escenario. La incertidumbre de cada estimación se representa con una distribución beta, que el PMBOK admite entre las distribuciones para modelar la incertidumbre (PMI, 2017, p. 432). Con ella, la técnica PERT calcula el valor esperado y la desviación (Malcolm et al., 1959):
T_E = (O + 4M + P) / 6; σ = (P − O) / 6.

La p. 201 del PMBOK presenta también la distribución triangular, $(O + M + P)/3$. Se usa la beta porque pondera más el valor más probable, que se funda en los requerimientos y cantidades de cada paquete.

Las bases de cada estimación se declaran por tipo de paquete. Los módulos y las integraciones se estiman con los requerimientos del Formulario T-12 asignados al paquete; la infraestructura, con las cantidades del Formulario T-11; la implantación y la capacitación, con las personas y rutas del caso y la dotación del Formulario T-18, sección 2.6; y la operación, con los horarios de cobertura de los paquetes 8.1.1 y 8.1.2 y la periodicidad de los informes. Los paquetes de la fase 8 son de esfuerzo continuo: su estimación es mensual y se multiplica por los 36 meses de operación.

### 1.2 Programación

La duración se contrasta con esfuerzo, capacidad efectiva y dependencias. La sección 6 descompone cada paquete en actividades de 8 a 80 HH que caben en una quincena; sobre ellas se programa en detalle y se informa el avance. Las ventanas de la sección 4 son supuestos de asignación y la red agregada de la sección 5 explicita el cálculo del calendario. Las dependencias entre paquetes están en el Anexo 7.B del Subdocumento 7, y sobre esa red se aplica el método de la ruta crítica (PMI, 2017, pp. 210–211): una pasada hacia adelante da el inicio y el fin tempranos; una pasada hacia atrás, desde los meses fijos del Art. 17°, da el inicio y el fin tardíos; la diferencia LS − ES es la holgura total; la holgura libre se calcula respecto del ES de sus sucesores. Los hitos del Formulario E-25 son restricciones de fecha fija: un camino que no llega a su hito tiene holgura negativa y obliga a replanificar.

La sección 5 incorpora las revisiones del CLIENTE (Art. 18.3) como retardos, calcula el PERT de duración por camino con su desviación y probabilidad de cumplir cada hito, y añade escenarios deterministas de demora. La probabilidad por camino no se presenta como probabilidad de cumplir todo el proyecto. La nivelación ajusta el inicio de los paquetes con holgura para que ningún rol supere su dotación disponible (PMI, 2017, pp. 211–212); los paquetes de la ruta crítica no se mueven.

## 2 Ruta crítica y holguras

La ruta crítica se identifica sobre el cronograma por actividad de la sección 6.1, con la red de la sección 5. Con fechas de hito fijas, la holgura total de cada camino es su reserva hasta la fecha límite de entrega de la Tabla 5.2. La ruta crítica es la cadena de la Etapa 2: diseño (1.2.5, 2.1.4 y 2.4.2; H8, 13 días hábiles de reserva), módulos (3.5), prueba de integración (3.9.1; H9, 21 días hábiles y 89,9 % de probabilidad de entrega a tiempo en la simulación con riesgos del SD8) y certificación (3.9.2–3.9.7; H10, 28 días hábiles). Son caminos casi críticos la cadena de la Etapa 1 que nace en las interfaces sin documentación del ERP (1.2.3 → 3.3.2 → 3.4 → 3.8.1, H4 con 19 días; → 3.8.2–3.8.8, H5 con 35 días) y la sala técnica y los ambientes del H3 (2.3, 5.1.2, 6.1, 6.3, 6.6.3 y 3.1; 19 días). El H1 tiene la menor reserva absoluta, 6 días hábiles, con una desviación mínima (σ 0,58) y una probabilidad de entrega a tiempo superior al 99,9 %. Las marchas blancas (4.2.1, meses 13 a 15, y 4.3.1, meses 19 y 20) y los pasos a producción (H7 en el mes 16 y H12 en el mes 21) tienen fechas contractuales fijas.

  
- Caminos casi críticos
- 5.1.2 y 6.1 a 6.6 terminan en el H3
- Marcha / blanca E1
- Marcha / blanca E2
  
**Figura T15.1. Ruta crítica identificada y caminos casi críticos de la implementación. Fuente: elaboración propia a partir del Anexo 7.B del Subdocumento 7 y de los períodos del Formulario T-14.**

  <a id="fig:T15-ruta"></a>

La figura presenta la secuencia mensual de la implementación y la convergencia de los caminos casi críticos en los hitos. En el Anexo 7.B, D-29 a D-31 forman la ruta crítica, D-02, D-04 y D-14 a D-25 forman la cadena casi crítica de la Etapa 1 y D-07 a D-13 convergen en el H3. También son caminos casi críticos la captura de las reglas de ruteo del planificador (1.2.2 y 3.4.7 M4 Rutas), antes de su jubilación; los acuerdos con los diez transportistas y con el sindicato (5.4.1 y 5.4.2), antes de la ola de reparto; y la certificación del intercambio electrónico con las cadenas (3.6.5 y 3.6.6), antes del mes 21.

La holgura se gestiona en las instancias de gobierno de la EDT: el avance de la ruta crítica y de los caminos casi críticos se revisa en la reunión semanal y en el Comité de Proyecto quincenal (paquetes 1.3.5 y 1.8.3); toda desviación que comprometa un hito se escala al Comité Ejecutivo con su análisis de impacto (paquetes 1.4.3 y 1.8.2); y el informe mensual con valor ganado avisa toda desviación mayor al 10 % con su plan dentro de cinco días hábiles (paquete 1.8.6).

## 3 Frentes de trabajo y solapamientos

Un frente de trabajo es un equipo con un responsable y un conjunto de cuentas de control que avanza en paralelo con los demás. La Tabla T15.1 define los frentes a partir de la EDT del Formulario T-14 y de los responsables de su diccionario.

**Tabla T15.1. Frentes de trabajo. Fuente: elaboración propia a partir del Formulario T-14.**

<a id="tab:T15-frentes"></a>

| Frente | Responsable | Cuentas de control | Meses activos |
| --- | --- | --- | --- |
| F1 Dirección, gobierno y cumplimiento | Jefe de Proyecto | 1.1 a 1.4, 1.6 a 1.9, 5.4.1 a 5.4.3, 8.4, 9 | 1 a 56 |
| F2 Arquitectura, seguridad y datos | Arquitecto de Solución, con Seguridad y Datos | 2.1 a 2.6, 3.3, 3.7, 3.11 | 1 a 21 |
| F3 Construcción y correcciones E1 | Líder de Desarrollo | 3.4, 3.6.1 a 3.6.4, 3.10.1 a 3.10.3; capacidad protegida 4.2.2 | 1 a 20 |
| F4 Construcción de la Etapa 2 | Líder de Desarrollo | 3.5, 3.6.5, 3.6.6, 3.10.4 | 13 a 20 |
| F5 Plataforma, infraestructura y soporte puente | Líder de Operación / SRE | 3.1, 3.2, 5.1 a 5.3, 6.1 a 6.6; soporte 4.2.2 | 1 a 20 |
| F6 Calidad y pruebas | Líder de Calidad | 1.5, 3.8, 3.9 | 1 a 21 |
| F7 Implantación y gestión del cambio | Líder de Implantación y Gestión del Cambio | 4.1 a 4.3, 7.1 a 7.3 | 9 a 21 |
| F8 Operación y soporte | Líder de Operación / SRE | 8.1 a 8.3, 8.5 | 21 a 56 |

Los frentes se sincronizan en los hitos del Formulario E-25 y en los comités del Art. 71°, cuyas actas registran los acuerdos entre frentes (paquetes 1.8.2 a 1.8.5). La Figura T15.2 presenta su ventana de actividad entre los meses 1 y 21.

  
- Solapamiento / meses 13 a 15
- Solapamiento / meses 19 y 20
- **F8 Operación** / Líder de Operación / SRE
- 8.1–8.3, 8.5: desde el mes 21 hasta el 56
  
**Figura T15.2. Frentes de trabajo de los meses 1 a 21 y solapamientos del Art. 17.2. Fuente: elaboración propia a partir de la Tabla T-15.1 y del Formulario T-14.**

  <a id="fig:T15-frentes"></a>

En los meses 13 a 15 trabajan a la vez F7, en la marcha blanca de la Etapa 1; F3, en las correcciones de esa marcha blanca; F4, en el desarrollo de la Etapa 2; F6, en las pruebas de ambas etapas; y F1 y F2. F3 y F4 dependen del mismo rol, el Líder de Desarrollo, y por eso son equipos distintos: el equipo que atiende la marcha blanca no puede ser el que desarrolla la Etapa 2 (Art. 17.2, punto 1). En los meses 19 y 20 trabajan F7, en la marcha blanca de la Etapa 2; F4, en sus correcciones; F6; y el soporte de la Etapa 1 en producción.

## 4 Modelo cuantitativo de recursos

**Base de cálculo:** estimación por clases de tamaño trazable al T-12 y al T-11, que se recalcula con el equipo al establecer la línea base y que el Capítulo 8 usa para cuantificar los riesgos. La productividad y la dotación se contrastan con el avance real en cada Comité de Proyecto.

### 4.1 Supuestos y cálculo

Los supuestos y el cálculo del modelo de recursos son los siguientes.

- Capacidad nominal asumida: 160 HH/persona-mes; disponibilidad programable 80 %; capacidad efectiva 128 HH. El 20 % cubre ausencias y coordinación no imputada. No es una jornada contractual ni un cálculo de cumplimiento laboral.
- Esfuerzo inicial por clase y paquete: G gestión/acta 80 HH; E diseño/configuración/innovación 240 HH; D módulo 960 HH; I integración/migración 480 HH; V prueba 320 HH (integración y cierres de certificación: 160 HH); T instalación/capacitación 160 HH. Las clases de tamaño se fundan en los requerimientos del T-12 y en las cantidades del T-11, y se recalculan con el equipo al establecer la línea base.
- R identifica esfuerzo recurrente mensual, incluidos equivalentes mensuales de actividades anuales/semestrales: la distribución contable no cambia la frecuencia de ejecución del T-14.
- A identifica acompañamiento: 13 puestos simultáneos de terreno/coordinación; 12 × 24 días × 8 horas + 160 HH de coordinación = 2.464 HH por cuatro semanas; soporte E1 meses 16–20 con previsión 2.464/1.312/544/544/544 HH para puestos 13/7/3/3/3, condicionada a los indicadores del T-18. Las cuatro semanas de 4.3.2 se reparten por días: con el H12 firmado el 5 de octubre de 2028, primer día después de los tres primeros días hábiles, 23 de los 24 días de lunes a sábado caen en el mes 21 y uno en el mes 22; por eso 4.3.2 imputa 2.361,33 HH en el mes 21 y 102,67 en el mes 22. Si la fecha efectiva cambia, se recalcula el reparto sin acortar las cuatro semanas.
- C identifica cobertura por horas-posición del calendario real, con el mes 1 en febrero de 2027 (Anexo 7.A). NOC (8.1.1) y SOC (8.1.5) mantienen un puesto 24×7 cada uno: días del mes × 24, es decir 744 HH en un mes de 31 días, 720 en uno de 30 y 672 en febrero. La mesa (8.1.2, primera línea de incidentes del Art. 78°) aplica las posiciones del SD4, Anexo 4-W.7: 7 en la hora cargada y 2 en las otras 17 horas de 04:00 a 22:00, o 41 horas-posición por día de lunes a sábado; en septiembre y diciembre se suman 6 horas-posición de 22:00 a 04:00 de lunes a sábado y 24 los domingos. Así, un mes de 26 días de lunes a sábado exige 26 × 41 = 1.066 HH de mesa, y septiembre de 2028 exige 26 × 47 + 4 × 24 = 1.318 HH. El SOC puede prestarse con personal propio o subcontratado (RT-11.17; SD4, Anexo 4-W.7); en ambos casos sus HH se imputan aquí. Las posiciones de la mesa provienen de un Erlang C con supuestos de demanda: no acreditan abandono ni resolución al primer contacto, que se miden según la sección 5.6. La curva dimensiona relevos con 128 HH efectivas.
- O = 0,75M; P = 1,25M; E = (O + 4M + P)/6 = M. Para A/C, O = M = P: no se reduce cobertura por un escenario optimista. Los riesgos de demanda y ausencias se tratan separadamente.
- E se reparte uniformemente entre los meses inclusivos declarados. Las ventanas relativas son supuestos de asignación; las restricciones originales de aceptación del T-14 prevalecen. Coincidir en un mes no demuestra que una precedencia dentro del mes se haya satisfecho.
- Personas por rol/mes = techo(HH del rol / 128). Se suman techos por familia de trabajo dirigida por el rol; el responsable nominado dirige el equipo, no ejecuta solo todas las HH. JP/ARQ y los otros códigos identifican equipos con liderazgo y apoyo competente: un valor 5 en JP significa cinco personas equivalentes de dirección/documentación, no cinco jefes de proyecto. La sección 5.7 compara la curva con la dotación declarada y con los roles mínimos; antes de aprobar recursos se deben asignar personas distintas con competencias y turnos verificables.
- Reserva protegida E1 en meses 13–20: dos desarrolladores y un QA, 256 HH DES + 128 HH CAL/mes; no se presta a E2 ni se duplica como trabajo base.
- Soporte puente E1 meses 16–20: NOC + mesa con la misma regla de calendario que la operación (1.851, 1.786, 1.810, 1.851 y 2.038 HH; total 9.336 HH), imputado a 4.2.2 y financiado dentro de implementación. El SOC opera desde el mes 13 por 8.1.5, porque la marcha blanca ya trata datos reales. Operación contractual empieza en el mes 21.
- Ventanas ajustadas con el cronograma por actividad de la sección 6.1: cada paquete con entregable ocupa los meses de sus actividades, y sus HH se reparten según los días de cada actividad, no en forma pareja. Los planos 2.3.1/2.3.2 se hacen en el mes 1, la especificación y compra 5.1.2 en el mes 2, la instalación 6.1.1–6.1.4 en el mes 3 y la recepción 6.1.5 en el mes 4 (D-09 a D-11). Los prototipos 2.6.2 terminan antes de la construcción 3.4 (D-05); la identidad 3.3.1 empieza después del plan de seguridad (D-06); los módulos se programan con dependencias por interfaz (D-16, D-18 y D-19); y las certificaciones empiezan al terminar su prueba de integración (D-21 y D-31). La actualización anual del Plan de Reversibilidad 1.7.2 ocurre en el mes 15, primer aniversario de su entrega del mes 3; las siguientes son 8.1.4. El acompañamiento de salida 9.2.1 ocupa los meses 54 a 56 para cubrir sus 90 días dentro del contrato.

### 4.2 Horas por los 222 paquetes

La tabla siguiente presenta las horas de cada paquete con sus tres estimaciones y su valor esperado.

| EDT | Clase | Rol | Meses | O HH | M HH | P HH | E HH |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1.1 | G | JP | 1–1 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.1.2 | G | JP | 1–1 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.1.3 | G | JP | 1–1 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.2.1 | G | ARQ | 1–1 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.2.2 | G | IMP | 1–3 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.2.3 | G | ARQ | 1–4 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.2.4 | G | CAL | 2–2 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.2.5 | G | ARQ | 13–13 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.3.1 | G | JP | 1–1 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.3.2 | G | JP | 2–2 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.3.3 | G | JP | 2–2 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.3.4 | G | JP | 2–2 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.3.5 | R | JP | 1–20 | 360.00 | 480.00 | 600.00 | 480.00 |
| 1.4.1 | G | JP | 1–1 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.4.2 | G | JP | 1–1 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.4.3 | R | JP | 1–56 | 672.00 | 896.00 | 1120.00 | 896.00 |
| 1.5.1 | G | CAL | 2–2 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.5.2 | G | CAL | 6–20 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.6.1 | G | JP | 2–2 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.6.2 | R | JP | 1–20 | 120.00 | 160.00 | 200.00 | 160.00 |
| 1.7.1 | G | JP | 3–3 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.7.2 | G | JP | 15–15 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.8.1 | R | JP | 1–20 | 240.00 | 320.00 | 400.00 | 320.00 |
| 1.8.2 | R | JP | 1–56 | 336.00 | 448.00 | 560.00 | 448.00 |
| 1.8.3 | R | JP | 1–20 | 180.00 | 240.00 | 300.00 | 240.00 |
| 1.8.4 | R | ARQ | 1–56 | 336.00 | 448.00 | 560.00 | 448.00 |
| 1.8.5 | R | SRE | 13–56 | 264.00 | 352.00 | 440.00 | 352.00 |
| 1.8.6 | R | JP | 1–20 | 360.00 | 480.00 | 600.00 | 480.00 |
| 1.8.7 | R | JP | 2–56 | 330.00 | 440.00 | 550.00 | 440.00 |
| 1.8.8 | R | JP | 1–56 | 336.00 | 448.00 | 560.00 | 448.00 |
| 1.9.1 | G | SEG | 1–1 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.9.2 | G | SEG | 1–1 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.9.3 | G | SEG | 2–2 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.9.4 | R | SEG | 1–56 | 168.00 | 224.00 | 280.00 | 224.00 |
| 1.9.5 | R | JP | 1–56 | 168.00 | 224.00 | 280.00 | 224.00 |
| 2.1.1 | E | ARQ | 2–2 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.1.2 | E | ARQ | 2–2 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.1.3 | E | DAT | 2–2 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.1.4 | E | ARQ | 13–13 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.2.1 | E | SEG | 2–2 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.2.2 | E | SEG | 3–10 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.2.3 | E | SEG | 3–3 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.2.4 | E | SEG | 2–2 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.3.1 | E | SRE | 1–2 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.3.2 | E | SRE | 1–2 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.3.3 | E | SRE | 2–2 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.4.1 | E | ARQ | 4–4 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.4.2 | E | ARQ | 14–14 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.5.1 | E | SRE | 3–3 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.5.2 | E | SRE | 3–3 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.6.1 | E | IMP | 2–2 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.6.2 | E | IMP | 3–3 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.6.3 | E | IMP | 4–4 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.1.1 | E | SRE | 5–5 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.1.2 | E | SRE | 5–5 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.1.3 | E | SRE | 5–5 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.1.4 | E | SRE | 4–4 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.1.5 | E | SRE | 5–5 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.2.1 | E | SRE | 4–4 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.2.2 | E | SRE | 4–4 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.2.3 | E | SRE | 4–4 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.2.4 | E | SRE | 4–4 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.2.5 | E | SEG | 4–4 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.2.6 | E | SRE | 5–5 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.3.1 | I | SEG | 6–7 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.3.2 | I | ARQ | 5–6 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.3.3 | I | ARQ | 5–6 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.3.4 | I | ARQ | 5–6 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.3.5 | I | ARQ | 6–7 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.3.6 | I | ARQ | 6–7 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.4.1 | D | DES | 6–6 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.4.2 | D | DES | 6–6 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.4.3 | D | DES | 6–7 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.4.4 | D | DES | 8–8 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.4.5 | D | DES | 6–7 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.4.6 | D | DES | 6–6 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.4.7 | D | DES | 7–7 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.4.8 | D | DES | 7–7 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.4.9 | D | DES | 8–8 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.4.10 | D | DES | 8–8 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.4.11 | D | DAT | 8–8 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.5.1 | D | DES | 15–15 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.5.2 | D | DES | 15–15 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.5.3 | D | DES | 15–15 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.5.4 | D | DAT | 15–15 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.6.1 | I | DAT | 9–10 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.6.2 | I | DES | 7–8 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.6.3 | I | DES | 7–8 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.6.4 | I | DES | 7–8 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.6.5 | I | DES | 13–18 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.6.6 | I | DES | 17–19 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.7.1 | I | DAT | 7–8 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.7.2 | I | DAT | 9–10 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.7.3 | I | DAT | 11–11 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.7.4 | I | DAT | 11–11 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.7.5 | I | DAT | 12–12 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.8.1 | V | CAL | 9–9 | 120.00 | 160.00 | 200.00 | 160.00 |
| 3.8.2 | V | CAL | 9–10 | 240.00 | 320.00 | 400.00 | 320.00 |
| 3.8.3 | V | CAL | 9–10 | 240.00 | 320.00 | 400.00 | 320.00 |
| 3.8.4 | V | CAL | 9–10 | 240.00 | 320.00 | 400.00 | 320.00 |
| 3.8.5 | V | CAL | 9–10 | 240.00 | 320.00 | 400.00 | 320.00 |
| 3.8.6 | V | SEG | 9–9 | 120.00 | 160.00 | 200.00 | 160.00 |
| 3.8.7 | V | CAL | 10–10 | 120.00 | 160.00 | 200.00 | 160.00 |
| 3.8.8 | V | SRE | 9–10 | 240.00 | 320.00 | 400.00 | 320.00 |
| 3.9.1 | V | CAL | 16–16 | 120.00 | 160.00 | 200.00 | 160.00 |
| 3.9.2 | V | CAL | 16–16 | 240.00 | 320.00 | 400.00 | 320.00 |
| 3.9.3 | V | CAL | 16–16 | 240.00 | 320.00 | 400.00 | 320.00 |
| 3.9.4 | V | CAL | 16–16 | 240.00 | 320.00 | 400.00 | 320.00 |
| 3.9.5 | V | SEG | 16–16 | 240.00 | 320.00 | 400.00 | 320.00 |
| 3.9.6 | V | CAL | 16–17 | 120.00 | 160.00 | 200.00 | 160.00 |
| 3.9.7 | V | SRE | 16–16 | 120.00 | 160.00 | 200.00 | 160.00 |
| 3.10.1.1 | E | DAT | 7–9 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.10.1.2 | E | DAT | 9–10 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.10.1.3 | E | DAT | 9–10 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.10.1.4 | E | DAT | 11–15 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.10.2.1 | E | CAL | 2–3 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.10.2.2 | E | CAL | 3–5 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.10.2.3 | E | CAL | 5–10 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.10.2.4 | E | CAL | 11–15 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.10.3.1 | E | DAT | 3–5 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.10.3.2 | E | DAT | 5–9 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.10.3.3 | E | DAT | 9–10 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.10.3.4 | E | DAT | 11–15 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.10.4.1 | E | IMP | 13–14 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.10.4.2 | E | IMP | 14–15 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.10.4.3 | E | IMP | 15–17 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.10.4.4 | E | IMP | 18–21 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.11.1 | G | ARQ | 15–21 | 60.00 | 80.00 | 100.00 | 80.00 |
| 3.11.2 | G | SRE | 10–20 | 60.00 | 80.00 | 100.00 | 80.00 |
| 3.11.3 | G | DES | 4–20 | 60.00 | 80.00 | 100.00 | 80.00 |
| 3.11.4 | G | DES | 4–20 | 60.00 | 80.00 | 100.00 | 80.00 |
| 3.11.5 | G | DES | 6–20 | 60.00 | 80.00 | 100.00 | 80.00 |
| 4.1.1 | G | IMP | 10–10 | 60.00 | 80.00 | 100.00 | 80.00 |
| 4.1.2 | G | IMP | 11–11 | 60.00 | 80.00 | 100.00 | 80.00 |
| 4.1.3 | G | IMP | 17–17 | 60.00 | 80.00 | 100.00 | 80.00 |
| 4.2.1 | A | IMP | 13–15 | 7392.00 | 7392.00 | 7392.00 | 7392.00 |
| 4.2.2 | A | IMP | 16–20 | 5408.00 | 5408.00 | 5408.00 | 5408.00 |
| 4.2.3 | G | JP | 16–16 | 60.00 | 80.00 | 100.00 | 80.00 |
| 4.3.1 | A | IMP | 19–20 | 4928.00 | 4928.00 | 4928.00 | 4928.00 |
| 4.3.2 | A | IMP | 21–22 | 2464.00 | 2464.00 | 2464.00 | 2464.00 |
| 4.3.3 | G | JP | 21–21 | 60.00 | 80.00 | 100.00 | 80.00 |
| 4.3.4 | G | JP | 21–21 | 60.00 | 80.00 | 100.00 | 80.00 |
| 5.1.1 | G | ARQ | 2–2 | 60.00 | 80.00 | 100.00 | 80.00 |
| 5.1.2 | G | ARQ | 2–2 | 60.00 | 80.00 | 100.00 | 80.00 |
| 5.1.3 | G | SRE | 5–5 | 60.00 | 80.00 | 100.00 | 80.00 |
| 5.2.1 | G | SRE | 2–2 | 60.00 | 80.00 | 100.00 | 80.00 |
| 5.2.2 | G | SRE | 4–4 | 60.00 | 80.00 | 100.00 | 80.00 |
| 5.2.3 | G | ARQ | 4–4 | 60.00 | 80.00 | 100.00 | 80.00 |
| 5.3.1 | G | SRE | 4–4 | 60.00 | 80.00 | 100.00 | 80.00 |
| 5.3.2 | G | SRE | 4–4 | 60.00 | 80.00 | 100.00 | 80.00 |
| 5.3.3 | G | SRE | 4–4 | 60.00 | 80.00 | 100.00 | 80.00 |
| 5.4.1 | G | IMP | 9–12 | 60.00 | 80.00 | 100.00 | 80.00 |
| 5.4.2 | G | IMP | 9–12 | 60.00 | 80.00 | 100.00 | 80.00 |
| 5.4.3 | G | JP | 17–20 | 60.00 | 80.00 | 100.00 | 80.00 |
| 5.4.4 | G | JP | 7–7 | 60.00 | 80.00 | 100.00 | 80.00 |
| 6.1.1 | T | SRE | 3–3 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.1.2 | T | SRE | 3–3 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.1.3 | T | SRE | 3–3 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.1.4 | T | SRE | 3–3 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.1.5 | T | SRE | 4–4 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.2.1 | T | SRE | 4–4 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.2.2 | T | SRE | 6–6 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.2.3 | T | SRE | 7–7 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.3.1 | T | SRE | 4–5 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.3.2 | T | SRE | 4–5 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.3.3 | T | SRE | 4–4 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.3.4 | T | SRE | 9–9 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.4.1 | T | SEG | 5–5 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.4.2 | T | SEG | 5–5 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.4.3 | T | SEG | 5–6 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.5.1 | T | SRE | 9–12 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.5.2 | T | SRE | 10–12 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.5.3 | T | SRE | 9–11 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.5.4 | T | SRE | 10–12 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.5.5 | T | SRE | 10–12 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.5.6 | T | SRE | 9–12 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.6.1 | T | SRE | 5–5 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.6.2 | T | SRE | 5–5 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.6.3 | T | SRE | 5–5 | 120.00 | 160.00 | 200.00 | 160.00 |
| 7.1.1 | T | IMP | 10–12 | 120.00 | 160.00 | 200.00 | 160.00 |
| 7.1.2 | R | IMP | 13–56 | 2112.00 | 2816.00 | 3520.00 | 2816.00 |
| 7.1.3 | T | IMP | 13–20 | 120.00 | 160.00 | 200.00 | 160.00 |
| 7.1.4 | T | IMP | 15–20 | 120.00 | 160.00 | 200.00 | 160.00 |
| 7.1.5 | T | IMP | 10–18 | 120.00 | 160.00 | 200.00 | 160.00 |
| 7.1.6 | T | IMP | 10–12 | 120.00 | 160.00 | 200.00 | 160.00 |
| 7.2.1 | T | IMP | 10–16 | 120.00 | 160.00 | 200.00 | 160.00 |
| 7.2.2 | T | IMP | 16–18 | 120.00 | 160.00 | 200.00 | 160.00 |
| 7.2.3 | T | IMP | 2–6 | 120.00 | 160.00 | 200.00 | 160.00 |
| 7.2.4 | T | IMP | 11–20 | 120.00 | 160.00 | 200.00 | 160.00 |
| 7.2.5 | T | IMP | 13–21 | 120.00 | 160.00 | 200.00 | 160.00 |
| 7.3.1 | T | IMP | 13–15 | 120.00 | 160.00 | 200.00 | 160.00 |
| 7.3.2 | T | IMP | 18–18 | 120.00 | 160.00 | 200.00 | 160.00 |
| 8.1.1 | C | SRE | 21–56 | 26280.00 | 26280.00 | 26280.00 | 26280.00 |
| 8.1.2 | C | SRE | 21–56 | 40078.00 | 40078.00 | 40078.00 | 40078.00 |
| 8.1.3 | G | SRE | 21–56 | 60.00 | 80.00 | 100.00 | 80.00 |
| 8.1.4 | R | JP | 21–56 | 216.00 | 288.00 | 360.00 | 288.00 |
| 8.1.5 | C | SEG | 13–56 | 32112.00 | 32112.00 | 32112.00 | 32112.00 |
| 8.1.6 | R | SRE | 21–56 | 432.00 | 576.00 | 720.00 | 576.00 |
| 8.2.1 | R | DES | 21–56 | 3456.00 | 4608.00 | 5760.00 | 4608.00 |
| 8.2.2 | R | SEG | 21–56 | 864.00 | 1152.00 | 1440.00 | 1152.00 |
| 8.2.3 | R | SRE | 21–56 | 864.00 | 1152.00 | 1440.00 | 1152.00 |
| 8.2.4 | R | DES | 21–56 | 1728.00 | 2304.00 | 2880.00 | 2304.00 |
| 8.2.5 | R | SRE | 21–56 | 216.00 | 288.00 | 360.00 | 288.00 |
| 8.2.6 | R | SRE | 21–56 | 216.00 | 288.00 | 360.00 | 288.00 |
| 8.2.7 | R | SRE | 21–56 | 648.00 | 864.00 | 1080.00 | 864.00 |
| 8.3.1 | R | CAL | 21–56 | 432.00 | 576.00 | 720.00 | 576.00 |
| 8.3.2 | R | DAT | 21–56 | 216.00 | 288.00 | 360.00 | 288.00 |
| 8.3.3 | G | JP | 21–23 | 60.00 | 80.00 | 100.00 | 80.00 |
| 8.3.4 | R | JP | 24–56 | 396.00 | 528.00 | 660.00 | 528.00 |
| 8.3.5 | G | IMP | 22–26 | 60.00 | 80.00 | 100.00 | 80.00 |
| 8.3.6 | G | IMP | 24–27 | 60.00 | 80.00 | 100.00 | 80.00 |
| 8.4.1 | R | SRE | 21–56 | 432.00 | 576.00 | 720.00 | 576.00 |
| 8.4.2 | R | SRE | 21–56 | 432.00 | 576.00 | 720.00 | 576.00 |
| 8.4.3 | R | SRE | 21–56 | 216.00 | 288.00 | 360.00 | 288.00 |
| 8.4.4 | R | JP | 21–56 | 216.00 | 288.00 | 360.00 | 288.00 |
| 8.5.1 | R | IMP | 21–56 | 864.00 | 1152.00 | 1440.00 | 1152.00 |
| 8.5.2 | G | IMP | 21–27 | 60.00 | 80.00 | 100.00 | 80.00 |
| 8.5.3 | R | SRE | 21–56 | 432.00 | 576.00 | 720.00 | 576.00 |
| 9.1.1 | G | DES | 21–21 | 60.00 | 80.00 | 100.00 | 80.00 |
| 9.1.2 | G | JP | 21–21 | 60.00 | 80.00 | 100.00 | 80.00 |
| 9.2.1 | G | JP | 54–56 | 60.00 | 80.00 | 100.00 | 80.00 |
| 9.2.2 | G | SEG | 56–56 | 60.00 | 80.00 | 100.00 | 80.00 |

Se agregan explícitamente soporte puente SRE de 4.2.2 = 9336.00 HH y reserva F3/QA = 8 × (256 + 128) = 3.072 HH. Son componentes separados de las filas base (190.366 HH), incluidos en las curvas siguientes.

### 4.3 Resumen T-15

La tabla siguiente resume las horas programadas por etapa contractual.

| Etapa | HH base y cobertura | HH reserva protegida | HH programadas | Frentes | Meses |
| --- | --- | --- | --- | --- | --- |
| E1 Desarrollo | 37981.17 | 0 | 37981.17 | F1,F2,F3,F5,F6,F7 | 1–12 |
| E1 Marcha blanca | 11147.17 | 1152 | 12299.17 | F1,F2,F3,F5,F6,F7 | 13–15 |
| E2 Desarrollo | 11566.54 | 0 | 11566.54 | F1,F2,F4,F5,F6,F7 | 13–18 |
| E2 Marcha blanca | 7275.91 | 0 | 7275.91 | F1,F2,F4,F6,F7 | 19–20 |
| E1 Soporte puente | 14744.00 | 1920 | 16664.00 | F3,F5,F6,F7 | 16–20 |
| Operación | 114212.67 | 0 | 114212.67 | F1,F8 | 21–56 |
| Cierre y estabilización implementación | 2774.54 | 0 | 2774.54 | F1,F2,F4,F6,F7 | 21–22 |

Total exacto de paquetes y componentes = 202774.00 HH (190.366 base + 9.336 puente + 3.072 reserva); peak mensual conjunto = 69 personas equivalentes en el mes 15, cuando coinciden la construcción de los módulos de la Etapa 2, la marcha blanca de la Etapa 1 y su acompañamiento. La mesa y el SOC dimensionados en el SD4, aplicados sobre el calendario real, determinan las horas de operación y de soporte puente. La implementación imputada a los meses 21 y 22 se separa de Operación; las actividades generales que continúan como servicio permanecen en Operación. Los peaks de etapas no se suman. Las centésimas de presentación se distribuyen por mayor resto entre meses y se concilian por etapa; la suma publicada conserva 202.774 HH exactas.

### 4.4 Curvas mensuales: horas por etapa y personas por rol

La tabla siguiente presenta, mes a mes, las horas por etapa y las personas equivalentes por rol.

| Mes | E1 desarrollo | E1 MB | E2 desarrollo | E2 MB | Soporte puente | Operación | Cierre y estabilización implementación | Total HH | JP | ARQ | SEG | DAT | DES | CAL | SRE | IMP | Personas totales |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1415.81 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1415.81 | 5 | 2 | 2 | 0 | 0 | 0 | 4 | 1 | 14 |
| 2 | 2909.52 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 2909.52 | 4 | 6 | 5 | 2 | 0 | 3 | 3 | 3 | 26 |
| 3 | 2121.67 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 2121.67 | 2 | 1 | 3 | 1 | 0 | 2 | 9 | 3 | 21 |
| 4 | 3382.78 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3382.78 | 1 | 3 | 3 | 1 | 1 | 1 | 17 | 3 | 30 |
| 5 | 4079.21 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 4079.21 | 1 | 10 | 4 | 2 | 1 | 2 | 15 | 0 | 35 |
| 6 | 5925.05 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 5925.05 | 1 | 9 | 4 | 1 | 31 | 1 | 2 | 0 | 49 |
| 7 | 4964.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 4964.01 | 2 | 1 | 1 | 5 | 30 | 1 | 2 | 0 | 42 |
| 8 | 4695.14 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 4695.14 | 1 | 1 | 1 | 9 | 27 | 1 | 0 | 0 | 40 |
| 9 | 3391.92 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3391.92 | 1 | 1 | 2 | 11 | 1 | 8 | 5 | 2 | 31 |
| 10 | 2120.57 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 2120.57 | 1 | 1 | 1 | 4 | 1 | 6 | 4 | 3 | 21 |
| 11 | 2076.35 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 2076.35 | 1 | 1 | 1 | 9 | 1 | 1 | 4 | 3 | 21 |
| 12 | 899.14 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 899.14 | 1 | 1 | 1 | 5 | 0 | 1 | 1 | 1 | 11 |
| 13 | 0.00 | 3936.70 | 548.57 | 0.00 | 0.00 | 0.00 | 0.00 | 4485.27 | 1 | 3 | 6 | 0 | 3 | 2 | 1 | 23 | 39 |
| 14 | 0.00 | 4317.79 | 571.43 | 0.00 | 0.00 | 0.00 | 0.00 | 4889.22 | 1 | 2 | 6 | 2 | 3 | 2 | 1 | 24 | 41 |
| 15 | 0.00 | 4044.68 | 4160.00 | 0.00 | 0.00 | 0.00 | 0.00 | 8204.68 | 2 | 1 | 6 | 8 | 26 | 2 | 1 | 23 | 69 |
| 16 | 0.00 | 0.00 | 3054.06 | 0.00 | 4699.00 | 0.00 | 0.00 | 7753.06 | 2 | 1 | 9 | 0 | 3 | 11 | 16 | 22 | 64 |
| 17 | 0.00 | 0.00 | 1669.57 | 0.00 | 3482.00 | 0.00 | 0.00 | 5151.57 | 2 | 1 | 6 | 0 | 4 | 2 | 15 | 14 | 44 |
| 18 | 0.00 | 0.00 | 1562.91 | 0.00 | 2738.00 | 0.00 | 0.00 | 4300.91 | 1 | 1 | 6 | 0 | 4 | 2 | 15 | 8 | 37 |
| 19 | 0.00 | 0.00 | 0.00 | 3753.86 | 2779.00 | 0.00 | 0.00 | 6532.86 | 1 | 1 | 6 | 0 | 4 | 2 | 15 | 26 | 55 |
| 20 | 0.00 | 0.00 | 0.00 | 3522.05 | 2966.00 | 0.00 | 0.00 | 6488.05 | 1 | 1 | 6 | 0 | 2 | 1 | 16 | 25 | 52 |
| 21 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3120.48 | 2774.54 | 5895.02 | 3 | 1 | 7 | 1 | 3 | 1 | 16 | 20 | 52 |
| 22 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3234.77 | 0.00 | 3234.77 | 1 | 1 | 6 | 1 | 2 | 1 | 16 | 2 | 30 |
| 23 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3442.76 | 0.00 | 3442.76 | 1 | 1 | 7 | 1 | 2 | 1 | 18 | 1 | 32 |
| 24 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3250.14 | 0.00 | 3250.14 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 2 | 31 |
| 25 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 2935.72 | 0.00 | 2935.72 | 1 | 1 | 6 | 1 | 2 | 1 | 15 | 1 | 28 |
| 26 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3231.43 | 0.00 | 3231.43 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 2 | 31 |
| 27 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3083.05 | 0.00 | 3083.05 | 1 | 1 | 6 | 1 | 2 | 1 | 15 | 1 | 28 |
| 28 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3179.00 | 0.00 | 3179.00 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 29 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3090.00 | 0.00 | 3090.00 | 1 | 1 | 6 | 1 | 2 | 1 | 16 | 1 | 29 |
| 30 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3138.00 | 0.00 | 3138.00 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 31 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3179.00 | 0.00 | 3179.00 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 32 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3319.00 | 0.00 | 3319.00 | 1 | 1 | 6 | 1 | 2 | 1 | 17 | 1 | 30 |
| 33 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3192.33 | 0.00 | 3192.33 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 34 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3090.00 | 0.00 | 3090.00 | 1 | 1 | 6 | 1 | 2 | 1 | 16 | 1 | 29 |
| 35 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3414.00 | 0.00 | 3414.00 | 1 | 1 | 7 | 1 | 2 | 1 | 18 | 1 | 32 |
| 36 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3179.00 | 0.00 | 3179.00 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 37 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 2912.00 | 0.00 | 2912.00 | 1 | 1 | 6 | 1 | 2 | 1 | 15 | 1 | 28 |
| 38 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3138.00 | 0.00 | 3138.00 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 39 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3103.33 | 0.00 | 3103.33 | 1 | 1 | 6 | 1 | 2 | 1 | 16 | 1 | 29 |
| 40 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3179.00 | 0.00 | 3179.00 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 41 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3049.00 | 0.00 | 3049.00 | 1 | 1 | 6 | 1 | 2 | 1 | 15 | 1 | 28 |
| 42 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3179.00 | 0.00 | 3179.00 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 43 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3179.00 | 0.00 | 3179.00 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 44 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3319.00 | 0.00 | 3319.00 | 1 | 1 | 6 | 1 | 2 | 1 | 17 | 1 | 30 |
| 45 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3192.33 | 0.00 | 3192.33 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 46 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3090.00 | 0.00 | 3090.00 | 1 | 1 | 6 | 1 | 2 | 1 | 16 | 1 | 29 |
| 47 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3414.00 | 0.00 | 3414.00 | 1 | 1 | 7 | 1 | 2 | 1 | 18 | 1 | 32 |
| 48 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3179.00 | 0.00 | 3179.00 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 49 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 2912.00 | 0.00 | 2912.00 | 1 | 1 | 6 | 1 | 2 | 1 | 15 | 1 | 28 |
| 50 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3138.00 | 0.00 | 3138.00 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 51 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3103.33 | 0.00 | 3103.33 | 1 | 1 | 6 | 1 | 2 | 1 | 16 | 1 | 29 |
| 52 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3179.00 | 0.00 | 3179.00 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 53 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3049.00 | 0.00 | 3049.00 | 1 | 1 | 6 | 1 | 2 | 1 | 15 | 1 | 28 |
| 54 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3210.11 | 0.00 | 3210.11 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 55 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3160.22 | 0.00 | 3160.22 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 56 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3448.67 | 0.00 | 3448.67 | 1 | 1 | 7 | 1 | 2 | 1 | 18 | 1 | 32 |

Factibilidad por capacidad aritmética: se debe dotar cada rol con la curva indicada. El registro nominal de personas y los turnos se aprueban junto con la línea base del H1. La reserva E1 es exclusiva; el trabajo de E2 usa capacidad adicional. La revisión de HH modifica conjuntamente dotación, cronograma y exposición de SD8.

## 5 Red agregada, restricciones y escenarios de calendario

### 5.1 Cálculo reproducible

La red se calcula sobre las 564 actividades de los paquetes con entregable de la sección 6, no sobre bloques mensuales. El calendario usa días hábiles de lunes a viernes, con el mes 1 en febrero de 2027 (supuesto del Anexo 7.A); una persona aporta 6,4 HH efectivas por día (8 horas al 80 %), coherente con las 128 HH por mes de la sección 4.1. Las reglas del cálculo son las siguientes:

- **Duración de una actividad.** Es sus HH divididas por las HH diarias de las personas asignadas, redondeada hacia arriba en días. Ninguna actividad supera diez días hábiles, una quincena.
- **Equipo del paquete.** Cada paquete tiene un equipo constante: el menor que cumple la regla de la quincena y termina dentro de su ventana. Los incrementos de construcción de un módulo avanzan en paralelo, por lo que un módulo de 960 HH ocupa un equipo de 12 personas durante unos 18 días hábiles.
- **Lógica.** Dentro del paquete, las actividades siguen su plantilla (análisis, diseño, construcción, pruebas, integración y entrega). Entre paquetes rigen las dependencias del Anexo 7.B: las de tipo FC exigen que el predecesor termine; las de tipo CC, que haya empezado; y las de tipo «por interfaz» (D-16, D-18 y D-19) hacen que el sucesor construya después de que el predecesor fija sus contratos (actividad A02) e integre después de que el predecesor entrega (A12).
- **Revisión del CLIENTE.** Cada hito se cumple con el acta de aceptación (Art. 18.1), y el CLIENTE dispone de diez días hábiles para revisar (Art. 18.3). Por eso los paquetes que gatillan un hito terminan, a más tardar, diez días hábiles antes del último día hábil del mes del hito, y antes de esa fecha límite se deja la reserva que pide el PERT (sección 5.3). La subsanación no se programa como trabajo normal: si se necesita, consume la reserva.
- **Nivelación de recursos.** Los paquetes se programan en el orden de su holgura y cada uno en la primera fecha en que no supera la dotación declarada en el SD1: 48 personas de desarrollo, 44 de SRE y NOC, 15 de arquitectura y datos en conjunto, 7 de seguridad sin contar el SOC subcontratable y 10 de calidad, que se refuerza con evaluadores subcontratados hasta 16 durante las certificaciones (PMI, 2017, pp. 211–212). La carga diaria suma las actividades y el esfuerzo continuo del mes.

El resultado no tiene dependencias incumplidas, ningún paquete termina fuera de su ventana y ningún día supera la dotación declarada. La Tabla 5.1 resume las fechas de los grupos de paquetes; la sección 6.1 da las fechas de cada actividad.

**Tabla 5.1 — Fechas programadas por grupo de paquetes. Fuente: elaboración propia a partir de la sección 6.1.**

| Grupo | Paquetes | Inicio | Fin |
| --- | --- | --- | --- |
| Alcance (H1) | 1.2.1, 1.2.4 | 01-02-2027 | 09-03-2027 |
| Interfaces sin documentación | 1.2.3 | 01-02-2027 | 09-02-2027 |
| Diseño E1 y seguridad (H2) | 2.1.1–2.1.3, 2.2.1, 2.2.4 | 01-03-2027 | 29-03-2027 |
| Planos, especificación y sala técnica | 2.3.1, 2.3.2, 5.1.2, 6.1 | 01-02-2027 | 20-05-2027 |
| Racks y borde de los CD (H3) | 6.3.1–6.3.3, 6.6 | 03-05-2027 | 29-06-2027 |
| Servicios de nube y ambientes (H3) | 3.2.1, 3.2.2, 3.2.4, 3.2.5, 3.1 | 03-05-2027 | 21-06-2027 |
| Base compartida | 3.3 | 01-06-2027 | 05-08-2027 |
| Módulos E1 | 3.4 | 06-07-2027 | 27-09-2027 |
| Integraciones externas E1 | 3.6.1–3.6.4 | 06-08-2027 | 10-11-2027 |
| Prueba de integración E1 (H4) | 3.8.1 | 01-10-2027 | 20-10-2027 |
| Certificación E1 (H5) | 3.8.2–3.8.8 | 01-10-2027 | 29-11-2027 |
| Diseño E2 (H8) | 1.2.5, 2.1.4, 2.4.2 | 01-02-2028 | 30-03-2028 |
| Módulos E2 | 3.5 | 03-04-2028 | 26-04-2028 |
| Intercambio con las cadenas | 3.6.5, 3.6.6 | 01-02-2028 | 23-08-2028 |
| Prueba de integración E2 (H9) | 3.9.1 | 01-05-2028 | 18-05-2028 |
| Certificación E2 (H10) | 3.9.2–3.9.7 | 01-05-2028 | 07-06-2028 |

### 5.2 Secuencias que hacen compatible el modelo

El cálculo por actividad y la simulación del SD8 corrigieron cuatro supuestos de la programación mensual anterior.

- **Ventanas de módulos.** Un módulo no cabe en medio mes: su secuencia interna toma unos 18 días hábiles con 12 personas. Por eso las ventanas de 3.4.3 (meses 6 a 8), 3.4.7 y 3.4.8 (meses 7 a 9) y 3.4.9 y 3.4.10 (meses 8 y 9) se ampliaron, y las dependencias entre módulos pasaron a ser por interfaz.
- **Sala técnica y ambientes.** La cadena deja reserva ante el H3: planos 2.3.1/2.3.2 en el mes 1, especificación y orden de compra emitida por LafroX en el mes 2 (5.1.2), instalación 6.1.1–6.1.4 en el mes 3 y recepción 6.1.5 en el mes 4. Los racks R01/R02 se montan en los meses 4 y 5, el gabinete de Concepción en el mes 4 y el borde de los CD entra en servicio en el mes 5 (6.6.3), junto con los ambientes en la nube. Los gabinetes de cross-docking se montan en el mes 9. El CLIENTE solo compra el equipamiento de terreno antes de cada ola. Las actas 5.1.3 acreditan la recepción técnica de ambos suministros.
- **Certificación.** Las pruebas de aceptación y de operación sin conexión (3.8.2 y 3.8.3) empiezan al terminar la prueba de integración (D-21); las pruebas de carga, recuperación, seguridad ofensiva y respaldo (3.8.4 a 3.8.6 y 3.8.8) empiezan con la entrega de los módulos en QA (D-21b), porque no dependen del resultado funcional de la integración. En la Etapa 2, la integración (3.9.1) y la certificación (3.9.2 a 3.9.7) se adelantan al mes 16, una vez entregados los módulos. Todas corren en paralelo con la revisión del CLIENTE del H4 y del H9; si esa revisión formula observaciones sobre el software, la certificación repite los casos afectados dentro de su reserva.
- **Refuerzo de calidad.** Durante las certificaciones (meses 9 a 12 y 16 a 18) el equipo de calidad se refuerza con evaluadores subcontratados hasta 16 personas por día (SD6, sección 6.1.3), para dejar ante el H5 y el H10 la reserva que exige la simulación del SD8.

La nivelación concentra la construcción de la Etapa 1 entre julio y septiembre de 2027 con 48 personas de desarrollo, toda la división declarada. Las dependencias D-08 y D-12 del Anexo 7.B se precisaron por paquete, porque a nivel de cuenta bloqueaban sin necesidad: los ambientes no esperan a la plataforma de IoT (3.2.3), que precede a M12, ni la configuración de los CD espera a los gabinetes de cross-docking (6.3.4), que preceden al equipamiento de campo.

### 5.3 Reservas y análisis PERT de duración

La duración PERT de cada paquete usa la tríada de la sección 4.1: O = 0,75 d, M = d y P = 1,25 d, con el equipo programado. Por eso T_E = d y σ = d/12. Para cada hito se recorren todos los caminos que llegan a sus paquetes, desde la fecha de liberación de su primer paquete; la varianza de un camino es la suma de las varianzas de sus paquetes, y la probabilidad de entregar a tiempo es Φ(reserva/σ). Esa probabilidad sólo mide la variación de las horas. El SD8, Anexo 8.C, agrega una simulación de Monte Carlo sobre la misma red que suma la ocurrencia de los riesgos del registro; la Tabla 5.2 muestra ambos resultados.

**Tabla 5.2 — Entrega, reserva y probabilidad por hito. Fuente: elaboración propia a partir de la sección 6.1 y del SD8, Anexo 8.C.**

| Hito | Entrega programada | Fecha límite de entrega (acta − 10 días hábiles) | Reserva (días hábiles) | Camino de menor probabilidad (PERT) | σ del camino (días hábiles) | P(entrega a tiempo), PERT | P(entrega a tiempo), simulación con riesgos | Fecha P80 simulada |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| H1 | 09-03-2027 | 17-03-2027 | 6 | 1.2.1 | 0,58 | > 99,9 % | > 99,9 % | 10-03-2027 |
| H2 | 29-03-2027 | 17-05-2027 | 35 | 2.1.1 | 1,75 | > 99,9 % | > 99,9 % | 09-04-2027 |
| H3 | 21-06-2027 | 16-07-2027 | 19 | 3.1.1 | 1,25 | > 99,9 % | 98,6 % | 09-07-2027 |
| H4 | 20-10-2027 | 16-11-2027 | 19 | 3.8.1 | 1,17 | > 99,9 % | > 99,9 % | 03-11-2027 |
| H5 | 29-11-2027 | 17-01-2028 | 35 | 3.8.2 | 1,67 | > 99,9 % | 97,7 % | 05-01-2028 |
| H8 | 29-02-2028 | 17-03-2028 | 13 | 2.1.4 | 1,75 | > 99,9 % | 99,3 % | 09-03-2028 |
| H9 | 18-05-2028 | 16-06-2028 | 21 | 3.9.1 | 1,17 | > 99,9 % | 89,9 % | 14-06-2028 |
| H10 | 07-06-2028 | 17-07-2028 | 28 | 3.9.2 | 1,67 | > 99,9 % | 97,7 % | 07-07-2028 |

Ni el PERT ni la simulación incluyen un error sistemático en los tamaños supuestos que afecte a todos los paquetes a la vez, la falta de personas con las competencias requeridas ni un suministro de la infraestructura fuera de plazo más allá de lo modelado en R8-19. Esos casos se tratan con los disparadores del SD8, y su control es el seguimiento semanal de la reserva de cada hito.

### 5.4 Gobierno

Las ventanas mensuales de acompañamiento son una imputación inicial: cuatro semanas desde un acta en día permitido pueden cruzar al mes siguiente, como ocurre con 4.3.2. Confirmada la fecha, se redistribuyen las mismas HH entre meses y se recalculan relevos; no se acorta el acompañamiento para mantener una celda mensual.

El JP revisa semanalmente fechas pronosticadas, consumo de capacidad y restricciones. Toda amenaza a un hito se escala cuando la desviación proyectada supera la mitad de su reserva de la Tabla 5.2, sin esperar a consumirla. La actualización de tareas, equipos o duración obliga a repetir el cálculo y conservar D-01–D-34; se mantienen los 56 meses y las condiciones del Art. 17.3. Ver SD8, Anexos 8.C/8.D, para escenarios, reservas y condiciones de evidencia.

### 5.5 Presentación de entregables y revisión del CLIENTE

Cada entregable que gatilla un hito se presenta en la fecha de entrega de la Tabla 5.2, con al menos diez días hábiles antes del último día hábil del mes del hito, para que la revisión del Art. 18.3 termine dentro de ese mes. Los entregables que admiten revisión por partes se presentan por incrementos: el informe de QA de cada módulo de la Etapa 1 se entrega con su actividad A12, entre julio y septiembre de 2027, y el informe de integración al terminar 3.8.1, el 20 de octubre de 2027. Así, la revisión final del H4 cubre sólo el último incremento. Si el CLIENTE formula observaciones, la subsanación de diez días hábiles usa la reserva del hito, y el hito no se da por cumplido hasta el acta. Este procedimiento no supone que el CLIENTE renuncie a su plazo ni que firme el acta el mismo día de la entrega.

### 5.6 Medición de los niveles de atención

El Erlang C de la mesa (SD4, Anexo 4-W.7) dimensiona la espera con llegadas de Poisson, atención exponencial y paciencia infinita. Sirve para el 80 % de respuestas antes de 20 segundos, pero no modela el abandono ni la resolución al primer contacto del RT-21.06 de las Bases Técnicas Transversales. Para ambos se aplica medición: desde la marcha blanca de la Etapa 1, la mesa registra por contacto la hora de llegada, de respuesta o de abandono y si se resolvió sin escalar. Con al menos cuatro semanas de registros se calibra un modelo con abandono (Erlang A) usando la paciencia observada, y se recalcula la dotación de 8.1.2 antes del mes 21. La resolución al primer contacto se sostiene con la base de conocimiento de 3.11 y la capacitación de 7.1, y se informa mensualmente. Si un indicador no se cumple durante dos meses seguidos, se aumenta la dotación de la franja afectada sin esperar la revisión anual.

### 5.7 Dotación requerida, roles mínimos y dotación declarada

La curva de la sección 4.4 y la carga diaria de la sección 6.1 se comparan con la dotación técnica declarada en el SD1, Tabla 1.1. Las personas equivalentes de la curva son HH del mes divididas por 128; las simultáneas son las que trabajan el mismo día según el cronograma por actividad, y son las que la dotación debe cubrir. La comparación muestra dónde la curva cabe en las divisiones de LafroX y dónde se requiere asignación, contratación o subcontratación antes de aprobar la línea base. Como las personas de esas divisiones atienden otros contratos, la asignación nominal se confirma antes del H1.

| Familia T-15 | Peak de la curva | División del SD1 que la provee | Dotación declarada | Condición |
| --- | --- | --- | --- | --- |
| DES | 31 equivalentes en el mes 6; 48 personas simultáneas entre julio y septiembre de 2027 | Desarrollo de software | 48 | La división trabaja en PHP/Laravel y Kotlin, el mismo stack de la oferta; el Líder de Desarrollo verifica la experiencia de cada persona asignada antes del mes 5. |
| SRE | 17 equivalentes en el mes 4; 24 simultáneas en el mes 4; 15 a 18 en Operación | SRE y Cloud (12) y NOC 24×7 (32) | 44 | Los meses 3 a 6 concentran la instalación de sala, racks y sitios: energía, climatización e incendio (6.1.2–6.1.4) los ejecutan instaladores especializados supervisados por SRE. NOC y mesa se cubren con personal del NOC con turnos asignados. |
| SEG | 9 en el mes 16 con el SOC; 6 simultáneas sin el SOC | CISO y especialistas en ciberseguridad | 7 | El puesto SOC 24×7 suma 744 HH en un mes de 31 días, es decir, 6 personas equivalentes con las 128 HH efectivas de la sección 4.1; el SD4, Anexo 4-W.7, lo cubre con 4 personas a 42 horas semanales (5 desde el 26-04-2028) y la diferencia corresponde a ausencias y relevos. Se cubre con contratación o con un servicio SOC subcontratado (RT-11.17), con las mismas horas de la sección 4.2. |
| CAL | 11 equivalentes y 13 simultáneas en el mes 16 | Aseguramiento y automatización de pruebas | 10 | La división declara 10; durante las certificaciones se agregan evaluadores subcontratados hasta 16 por día (SD6, sección 6.1.3). |
| ARQ y DAT | 10 y 11 equivalentes; 15 simultáneas en conjunto en el mes 7 | Arquitectura de solución e integración | 15 | Datos y arquitectura comparten la división; la nivelación la limita a 15 personas por día. |
| IMP | 26 equivalentes en el mes 19; 30 simultáneas en el mes 14 | La Tabla 1.1 no tiene una división de implantación | — | Los 13 puestos de acompañamiento se cubren con personal de implantación contratado para las marchas blancas y capacitado en 7.1. |
| JP | 5 en el mes 1 | Dirección de Operaciones, fuera de la Tabla 1.1 | — | Personas de dirección y documentación, no cinco jefes de proyecto. |

Los roles mínimos del numeral 19.2 de las Bases Técnicas Transversales se imputan a las familias así. El Jefe de Proyecto (100 % en implementación) se imputa a JP en los meses 1–21. El Líder de Desarrollo (100 % en implementación) se imputa a ARQ en los meses 1–4, donde participa en el diseño 2.1 y en los prototipos 2.6.2, y a DES desde el mes 4 (3.11.3/3.11.4 y los módulos); por eso la curva muestra DES cero en los meses 1–3 sin que el rol quede sin horas. El Líder Funcional (100 % en implementación) se imputa a IMP en los meses 1–4 (1.2.2 y 2.6) y a CAL e IMP desde el mes 5 (pruebas de aceptación y olas). El Líder de Integración (permanente en implementación) se imputa a ARQ (1.2.3, 3.3 y 3.6). Ninguna de estas imputaciones agrega horas: forman parte de las horas de los paquetes donde trabajan. El SD1, sección 1.5, nomina a las personas que ocupan cada rol.

## 6 Lista de actividades: regla del 8/80 y del período de reporte

La EDT del Formulario T-14 llega hasta el paquete de trabajo; fuera de ella, cada paquete se descompone en las actividades que permiten programarlo, asignarlo y controlarlo (PMI, 2017, pp. 183–185). Las actividades cumplen dos reglas de tamaño:

- **Regla del 8/80.** Cada actividad requiere entre 8 y 80 horas hombre de esfuerzo.
- **Regla del período de reporte.** Cada actividad cabe en una quincena, el período de reporte del Comité de Proyecto (paquete 1.8.3): dura como máximo diez días hábiles. Con 6,4 HH efectivas por persona y día, una actividad de 80 HH con dos personas dura ⌈80 ÷ 12,8⌉ = 7 días hábiles; si su ventana es más corta, se le asignan más personas. Toda actividad de nivel de esfuerzo se divide en relevos de 64 HH como máximo.

La descomposición no cambia las HH de la sección 4: la suma de las actividades de cada paquete es igual a su esfuerzo esperado E. Las actividades heredan el responsable y la ventana del paquete. Cada actividad tiene fecha de inicio y de fin en la Tabla 6.1. Por planificación gradual (PMI, 2017, p. 185), antes de cada Comité de Proyecto se revisan en detalle las actividades de los tres meses siguientes con las estimaciones del equipo, sin mover los hitos ni consumir más reserva que la registrada. El avance se informa por el código de la actividad, que cuelga del código de su paquete.

### 6.1 Paquetes descompuestos en actividades

Los paquetes de producto se descomponen con una plantilla por clase. Un módulo (D, 960 HH) se divide en 12 actividades de 80 HH; una integración (I, 480 HH), en 6; un diseño o configuración (E, 240 HH), en 3; una instalación o capacitación (T, 160 HH), en 2; una prueba ampliada (V, 320 HH), en 4, y una de integración o cierre (V, 160 HH), en 2. Un paquete de gestión (G, 80 HH) es una actividad única, porque ya cumple ambas reglas. Las plantillas son supuestos de planificación, como los tamaños de la sección 4.1: el equipo de cada paquete las ajusta al refinar su estimación, sin superar 80 HH ni una quincena por actividad.

La Tabla 6.1 es el cronograma de las 564 actividades de los 163 paquetes con entregable: cada actividad tiene responsable (el rol de su paquete), personas asignadas, HH, fechas de inicio y fin en días hábiles, duración y predecesoras. Las predecesoras de la primera actividad de un paquete son las actividades finales de los paquetes de los que depende en el Anexo 7.B; en las dependencias por interfaz, la construcción del sucesor espera la actividad A02 del predecesor, y su integración, la A12. Las fechas suponen el inicio del contrato en febrero de 2027 y se trasladan si cambia la fecha efectiva (V-12).

**Tabla 6.1 — Cronograma de las actividades de los paquetes con entregable. Fuente: elaboración propia a partir de las secciones 4.1, 4.2 y 5.1.**

| Actividad | Nombre | Rol | Personas | HH | Inicio | Fin | Días hábiles | Predecesoras |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1.1.A01 | Elaboración, revisión y aprobación del entregable | JP | 2 | 80 | 01-02-2027 | 09-02-2027 | 7 | — |
| 1.1.2.A01 | Elaboración, revisión y aprobación del entregable | JP | 2 | 80 | 01-02-2027 | 09-02-2027 | 7 | — |
| 1.1.3.A01 | Elaboración, revisión y aprobación del entregable | JP | 2 | 80 | 01-02-2027 | 09-02-2027 | 7 | — |
| 1.2.1.A01 | Elaboración, revisión y aprobación del entregable | ARQ | 2 | 80 | 01-02-2027 | 09-02-2027 | 7 | — |
| 1.2.3.A01 | Elaboración, revisión y aprobación del entregable | ARQ | 2 | 80 | 01-02-2027 | 09-02-2027 | 7 | — |
| 1.2.4.A01 | Elaboración, revisión y aprobación del entregable | CAL | 2 | 80 | 01-03-2027 | 09-03-2027 | 7 | — |
| 1.2.5.A01 | Elaboración, revisión y aprobación del entregable | ARQ | 2 | 80 | 01-02-2028 | 09-02-2028 | 7 | — |
| 1.3.1.A01 | Elaboración, revisión y aprobación del entregable | JP | 2 | 80 | 10-02-2027 | 18-02-2027 | 7 | — |
| 1.3.2.A01 | Elaboración, revisión y aprobación del entregable | JP | 2 | 80 | 01-03-2027 | 09-03-2027 | 7 | — |
| 1.3.3.A01 | Elaboración, revisión y aprobación del entregable | JP | 2 | 80 | 01-03-2027 | 09-03-2027 | 7 | — |
| 1.3.4.A01 | Elaboración, revisión y aprobación del entregable | JP | 2 | 80 | 01-03-2027 | 09-03-2027 | 7 | — |
| 1.4.1.A01 | Elaboración, revisión y aprobación del entregable | JP | 2 | 80 | 01-02-2027 | 09-02-2027 | 7 | — |
| 1.4.2.A01 | Elaboración, revisión y aprobación del entregable | JP | 2 | 80 | 01-02-2027 | 09-02-2027 | 7 | — |
| 1.5.1.A01 | Elaboración, revisión y aprobación del entregable | CAL | 2 | 80 | 01-03-2027 | 09-03-2027 | 7 | — |
| 1.6.1.A01 | Elaboración, revisión y aprobación del entregable | JP | 2 | 80 | 01-03-2027 | 09-03-2027 | 7 | — |
| 1.7.1.A01 | Elaboración, revisión y aprobación del entregable | JP | 2 | 80 | 01-04-2027 | 09-04-2027 | 7 | — |
| 1.7.2.A01 | Elaboración, revisión y aprobación del entregable | JP | 2 | 80 | 03-04-2028 | 11-04-2028 | 7 | — |
| 1.9.1.A01 | Elaboración, revisión y aprobación del entregable | SEG | 2 | 80 | 01-02-2027 | 09-02-2027 | 7 | — |
| 1.9.2.A01 | Elaboración, revisión y aprobación del entregable | SEG | 2 | 80 | 01-02-2027 | 09-02-2027 | 7 | — |
| 1.9.3.A01 | Elaboración, revisión y aprobación del entregable | SEG | 2 | 80 | 01-03-2027 | 09-03-2027 | 7 | — |
| 2.1.1.A01 | Levantamiento de insumos y análisis | ARQ | 2 | 80 | 01-03-2027 | 09-03-2027 | 7 | 1.2.1.A01 |
| 2.1.1.A02 | Elaboración del entregable | ARQ | 2 | 80 | 10-03-2027 | 18-03-2027 | 7 | 2.1.1.A01 |
| 2.1.1.A03 | Revisión, corrección y presentación para aprobación | ARQ | 2 | 80 | 19-03-2027 | 29-03-2027 | 7 | 2.1.1.A02 |
| 2.1.2.A01 | Levantamiento de insumos y análisis | ARQ | 2 | 80 | 01-03-2027 | 09-03-2027 | 7 | — |
| 2.1.2.A02 | Elaboración del entregable | ARQ | 2 | 80 | 10-03-2027 | 18-03-2027 | 7 | 2.1.2.A01 |
| 2.1.2.A03 | Revisión, corrección y presentación para aprobación | ARQ | 2 | 80 | 19-03-2027 | 29-03-2027 | 7 | 2.1.2.A02 |
| 2.1.3.A01 | Levantamiento de insumos y análisis | DAT | 2 | 80 | 01-03-2027 | 09-03-2027 | 7 | — |
| 2.1.3.A02 | Elaboración del entregable | DAT | 2 | 80 | 10-03-2027 | 18-03-2027 | 7 | 2.1.3.A01 |
| 2.1.3.A03 | Revisión, corrección y presentación para aprobación | DAT | 2 | 80 | 19-03-2027 | 29-03-2027 | 7 | 2.1.3.A02 |
| 2.1.4.A01 | Levantamiento de insumos y análisis | ARQ | 2 | 80 | 01-02-2028 | 09-02-2028 | 7 | — |
| 2.1.4.A02 | Elaboración del entregable | ARQ | 2 | 80 | 10-02-2028 | 18-02-2028 | 7 | 2.1.4.A01 |
| 2.1.4.A03 | Revisión, corrección y presentación para aprobación | ARQ | 2 | 80 | 21-02-2028 | 29-02-2028 | 7 | 2.1.4.A02 |
| 2.2.1.A01 | Levantamiento de insumos y análisis | SEG | 2 | 80 | 01-03-2027 | 09-03-2027 | 7 | — |
| 2.2.1.A02 | Elaboración del entregable | SEG | 2 | 80 | 10-03-2027 | 18-03-2027 | 7 | 2.2.1.A01 |
| 2.2.1.A03 | Revisión, corrección y presentación para aprobación | SEG | 2 | 80 | 19-03-2027 | 29-03-2027 | 7 | 2.2.1.A02 |
| 2.2.3.A01 | Levantamiento de insumos y análisis | SEG | 2 | 80 | 01-04-2027 | 09-04-2027 | 7 | — |
| 2.2.3.A02 | Elaboración del entregable | SEG | 2 | 80 | 12-04-2027 | 20-04-2027 | 7 | 2.2.3.A01 |
| 2.2.3.A03 | Revisión, corrección y presentación para aprobación | SEG | 2 | 80 | 21-04-2027 | 29-04-2027 | 7 | 2.2.3.A02 |
| 2.2.4.A01 | Levantamiento de insumos y análisis | SEG | 2 | 80 | 01-03-2027 | 09-03-2027 | 7 | — |
| 2.2.4.A02 | Elaboración del entregable | SEG | 2 | 80 | 10-03-2027 | 18-03-2027 | 7 | 2.2.4.A01 |
| 2.2.4.A03 | Revisión, corrección y presentación para aprobación | SEG | 2 | 80 | 19-03-2027 | 29-03-2027 | 7 | 2.2.4.A02 |
| 2.3.1.A01 | Levantamiento de insumos y análisis | SRE | 2 | 80 | 01-02-2027 | 09-02-2027 | 7 | — |
| 2.3.1.A02 | Elaboración del entregable | SRE | 2 | 80 | 10-02-2027 | 18-02-2027 | 7 | 2.3.1.A01 |
| 2.3.1.A03 | Revisión, corrección y presentación para aprobación | SRE | 2 | 80 | 19-02-2027 | 01-03-2027 | 7 | 2.3.1.A02 |
| 2.3.2.A01 | Levantamiento de insumos y análisis | SRE | 2 | 80 | 01-02-2027 | 09-02-2027 | 7 | — |
| 2.3.2.A02 | Elaboración del entregable | SRE | 2 | 80 | 10-02-2027 | 18-02-2027 | 7 | 2.3.2.A01 |
| 2.3.2.A03 | Revisión, corrección y presentación para aprobación | SRE | 2 | 80 | 19-02-2027 | 01-03-2027 | 7 | 2.3.2.A02 |
| 2.3.3.A01 | Levantamiento de insumos y análisis | SRE | 2 | 80 | 01-03-2027 | 09-03-2027 | 7 | — |
| 2.3.3.A02 | Elaboración del entregable | SRE | 2 | 80 | 10-03-2027 | 18-03-2027 | 7 | 2.3.3.A01 |
| 2.3.3.A03 | Revisión, corrección y presentación para aprobación | SRE | 2 | 80 | 19-03-2027 | 29-03-2027 | 7 | 2.3.3.A02 |
| 2.4.1.A01 | Levantamiento de insumos y análisis | ARQ | 5 | 80 | 18-05-2027 | 20-05-2027 | 3 | — |
| 2.4.1.A02 | Elaboración del entregable | ARQ | 5 | 80 | 21-05-2027 | 25-05-2027 | 3 | 2.4.1.A01 |
| 2.4.1.A03 | Revisión, corrección y presentación para aprobación | ARQ | 5 | 80 | 26-05-2027 | 28-05-2027 | 3 | 2.4.1.A02 |
| 2.4.2.A01 | Levantamiento de insumos y análisis | ARQ | 5 | 80 | 20-03-2028 | 22-03-2028 | 3 | — |
| 2.4.2.A02 | Elaboración del entregable | ARQ | 5 | 80 | 23-03-2028 | 27-03-2028 | 3 | 2.4.2.A01 |
| 2.4.2.A03 | Revisión, corrección y presentación para aprobación | ARQ | 5 | 80 | 28-03-2028 | 30-03-2028 | 3 | 2.4.2.A02 |
| 2.5.1.A01 | Levantamiento de insumos y análisis | SRE | 2 | 80 | 01-04-2027 | 09-04-2027 | 7 | — |
| 2.5.1.A02 | Elaboración del entregable | SRE | 2 | 80 | 12-04-2027 | 20-04-2027 | 7 | 2.5.1.A01 |
| 2.5.1.A03 | Revisión, corrección y presentación para aprobación | SRE | 2 | 80 | 21-04-2027 | 29-04-2027 | 7 | 2.5.1.A02 |
| 2.5.2.A01 | Levantamiento de insumos y análisis | SRE | 2 | 80 | 01-04-2027 | 09-04-2027 | 7 | — |
| 2.5.2.A02 | Elaboración del entregable | SRE | 2 | 80 | 12-04-2027 | 20-04-2027 | 7 | 2.5.2.A01 |
| 2.5.2.A03 | Revisión, corrección y presentación para aprobación | SRE | 2 | 80 | 21-04-2027 | 29-04-2027 | 7 | 2.5.2.A02 |
| 2.6.1.A01 | Levantamiento de insumos y análisis | IMP | 2 | 80 | 01-03-2027 | 09-03-2027 | 7 | — |
| 2.6.1.A02 | Elaboración del entregable | IMP | 2 | 80 | 10-03-2027 | 18-03-2027 | 7 | 2.6.1.A01 |
| 2.6.1.A03 | Revisión, corrección y presentación para aprobación | IMP | 2 | 80 | 19-03-2027 | 29-03-2027 | 7 | 2.6.1.A02 |
| 2.6.2.A01 | Levantamiento de insumos y análisis | IMP | 2 | 80 | 01-04-2027 | 09-04-2027 | 7 | — |
| 2.6.2.A02 | Elaboración del entregable | IMP | 2 | 80 | 12-04-2027 | 20-04-2027 | 7 | 2.6.2.A01 |
| 2.6.2.A03 | Revisión, corrección y presentación para aprobación | IMP | 2 | 80 | 21-04-2027 | 29-04-2027 | 7 | 2.6.2.A02 |
| 2.6.3.A01 | Levantamiento de insumos y análisis | IMP | 2 | 80 | 03-05-2027 | 11-05-2027 | 7 | — |
| 2.6.3.A02 | Elaboración del entregable | IMP | 2 | 80 | 12-05-2027 | 20-05-2027 | 7 | 2.6.3.A01 |
| 2.6.3.A03 | Revisión, corrección y presentación para aprobación | IMP | 2 | 80 | 21-05-2027 | 31-05-2027 | 7 | 2.6.3.A02 |
| 3.1.1.A01 | Levantamiento de insumos y análisis | SRE | 3 | 80 | 01-06-2027 | 07-06-2027 | 5 | 3.2.1.A03, 3.2.2.A03, 3.2.4.A03, 3.2.5.A03 |
| 3.1.1.A02 | Elaboración del entregable | SRE | 3 | 80 | 08-06-2027 | 14-06-2027 | 5 | 3.1.1.A01 |
| 3.1.1.A03 | Revisión, corrección y presentación para aprobación | SRE | 3 | 80 | 15-06-2027 | 21-06-2027 | 5 | 3.1.1.A02 |
| 3.1.2.A01 | Levantamiento de insumos y análisis | SRE | 3 | 80 | 01-06-2027 | 07-06-2027 | 5 | 3.2.1.A03, 3.2.2.A03, 3.2.4.A03, 3.2.5.A03 |
| 3.1.2.A02 | Elaboración del entregable | SRE | 3 | 80 | 08-06-2027 | 14-06-2027 | 5 | 3.1.2.A01 |
| 3.1.2.A03 | Revisión, corrección y presentación para aprobación | SRE | 3 | 80 | 15-06-2027 | 21-06-2027 | 5 | 3.1.2.A02 |
| 3.1.3.A01 | Levantamiento de insumos y análisis | SRE | 3 | 80 | 01-06-2027 | 07-06-2027 | 5 | 3.2.1.A03, 3.2.2.A03, 3.2.4.A03, 3.2.5.A03 |
| 3.1.3.A02 | Elaboración del entregable | SRE | 3 | 80 | 08-06-2027 | 14-06-2027 | 5 | 3.1.3.A01 |
| 3.1.3.A03 | Revisión, corrección y presentación para aprobación | SRE | 3 | 80 | 15-06-2027 | 21-06-2027 | 5 | 3.1.3.A02 |
| 3.1.4.A01 | Levantamiento de insumos y análisis | SRE | 2 | 80 | 03-05-2027 | 11-05-2027 | 7 | — |
| 3.1.4.A02 | Elaboración del entregable | SRE | 2 | 80 | 12-05-2027 | 20-05-2027 | 7 | 3.1.4.A01 |
| 3.1.4.A03 | Revisión, corrección y presentación para aprobación | SRE | 2 | 80 | 21-05-2027 | 31-05-2027 | 7 | 3.1.4.A02 |
| 3.1.5.A01 | Levantamiento de insumos y análisis | SRE | 3 | 80 | 01-06-2027 | 07-06-2027 | 5 | — |
| 3.1.5.A02 | Elaboración del entregable | SRE | 3 | 80 | 08-06-2027 | 14-06-2027 | 5 | 3.1.5.A01 |
| 3.1.5.A03 | Revisión, corrección y presentación para aprobación | SRE | 3 | 80 | 15-06-2027 | 21-06-2027 | 5 | 3.1.5.A02 |
| 3.2.1.A01 | Levantamiento de insumos y análisis | SRE | 2 | 80 | 03-05-2027 | 11-05-2027 | 7 | 5.2.1.A01 |
| 3.2.1.A02 | Elaboración del entregable | SRE | 2 | 80 | 12-05-2027 | 20-05-2027 | 7 | 3.2.1.A01 |
| 3.2.1.A03 | Revisión, corrección y presentación para aprobación | SRE | 2 | 80 | 21-05-2027 | 31-05-2027 | 7 | 3.2.1.A02 |
| 3.2.2.A01 | Levantamiento de insumos y análisis | SRE | 2 | 80 | 03-05-2027 | 11-05-2027 | 7 | 5.2.1.A01 |
| 3.2.2.A02 | Elaboración del entregable | SRE | 2 | 80 | 12-05-2027 | 20-05-2027 | 7 | 3.2.2.A01 |
| 3.2.2.A03 | Revisión, corrección y presentación para aprobación | SRE | 2 | 80 | 21-05-2027 | 31-05-2027 | 7 | 3.2.2.A02 |
| 3.2.3.A01 | Levantamiento de insumos y análisis | SRE | 2 | 80 | 03-05-2027 | 11-05-2027 | 7 | 5.2.1.A01 |
| 3.2.3.A02 | Elaboración del entregable | SRE | 2 | 80 | 12-05-2027 | 20-05-2027 | 7 | 3.2.3.A01 |
| 3.2.3.A03 | Revisión, corrección y presentación para aprobación | SRE | 2 | 80 | 21-05-2027 | 31-05-2027 | 7 | 3.2.3.A02 |
| 3.2.4.A01 | Levantamiento de insumos y análisis | SRE | 2 | 80 | 03-05-2027 | 11-05-2027 | 7 | 5.2.1.A01 |
| 3.2.4.A02 | Elaboración del entregable | SRE | 2 | 80 | 12-05-2027 | 20-05-2027 | 7 | 3.2.4.A01 |
| 3.2.4.A03 | Revisión, corrección y presentación para aprobación | SRE | 2 | 80 | 21-05-2027 | 31-05-2027 | 7 | 3.2.4.A02 |
| 3.2.5.A01 | Levantamiento de insumos y análisis | SEG | 2 | 80 | 03-05-2027 | 11-05-2027 | 7 | 5.2.1.A01 |
| 3.2.5.A02 | Elaboración del entregable | SEG | 2 | 80 | 12-05-2027 | 20-05-2027 | 7 | 3.2.5.A01 |
| 3.2.5.A03 | Revisión, corrección y presentación para aprobación | SEG | 2 | 80 | 21-05-2027 | 31-05-2027 | 7 | 3.2.5.A02 |
| 3.2.6.A01 | Levantamiento de insumos y análisis | SRE | 2 | 80 | 01-06-2027 | 09-06-2027 | 7 | 5.2.1.A01 |
| 3.2.6.A02 | Elaboración del entregable | SRE | 2 | 80 | 10-06-2027 | 18-06-2027 | 7 | 3.2.6.A01 |
| 3.2.6.A03 | Revisión, corrección y presentación para aprobación | SRE | 2 | 80 | 21-06-2027 | 29-06-2027 | 7 | 3.2.6.A02 |
| 3.3.1.A01 | Análisis de la interfaz con muestras reales y horarios | SEG | 4 | 80 | 06-07-2027 | 09-07-2027 | 4 | 2.2.1.A03 |
| 3.3.1.A02 | Diseño del contrato, del manejo de errores y de la idempotencia | SEG | 4 | 80 | 12-07-2027 | 15-07-2027 | 4 | 3.3.1.A01 |
| 3.3.1.A03 | Construcción del adaptador, parte 1 | SEG | 2 | 80 | 16-07-2027 | 26-07-2027 | 7 | 3.3.1.A02 |
| 3.3.1.A04 | Construcción del adaptador, parte 2, con reintentos | SEG | 2 | 80 | 16-07-2027 | 26-07-2027 | 7 | 3.3.1.A02 |
| 3.3.1.A05 | Pruebas de contrato, de falla y de lentitud de la contraparte | SEG | 4 | 80 | 27-07-2027 | 30-07-2027 | 4 | 3.3.1.A03, 3.3.1.A04 |
| 3.3.1.A06 | Corrección, documentación y entrega en QA | SEG | 4 | 80 | 02-08-2027 | 05-08-2027 | 4 | 3.3.1.A05 |
| 3.3.2.A01 | Análisis de la interfaz con muestras reales y horarios | ARQ | 4 | 80 | 01-06-2027 | 04-06-2027 | 4 | 1.2.3.A01 |
| 3.3.2.A02 | Diseño del contrato, del manejo de errores y de la idempotencia | ARQ | 4 | 80 | 07-06-2027 | 10-06-2027 | 4 | 3.3.2.A01 |
| 3.3.2.A03 | Construcción del adaptador, parte 1 | ARQ | 2 | 80 | 11-06-2027 | 21-06-2027 | 7 | 3.3.2.A02 |
| 3.3.2.A04 | Construcción del adaptador, parte 2, con reintentos | ARQ | 2 | 80 | 11-06-2027 | 21-06-2027 | 7 | 3.3.2.A02 |
| 3.3.2.A05 | Pruebas de contrato, de falla y de lentitud de la contraparte | ARQ | 4 | 80 | 22-06-2027 | 25-06-2027 | 4 | 3.3.2.A03, 3.3.2.A04 |
| 3.3.2.A06 | Corrección, documentación y entrega en QA | ARQ | 4 | 80 | 28-06-2027 | 01-07-2027 | 4 | 3.3.2.A05 |
| 3.3.3.A01 | Análisis de la interfaz con muestras reales y horarios | ARQ | 4 | 80 | 01-06-2027 | 04-06-2027 | 4 | — |
| 3.3.3.A02 | Diseño del contrato, del manejo de errores y de la idempotencia | ARQ | 4 | 80 | 07-06-2027 | 10-06-2027 | 4 | 3.3.3.A01 |
| 3.3.3.A03 | Construcción del adaptador, parte 1 | ARQ | 2 | 80 | 11-06-2027 | 21-06-2027 | 7 | 3.3.3.A02 |
| 3.3.3.A04 | Construcción del adaptador, parte 2, con reintentos | ARQ | 2 | 80 | 11-06-2027 | 21-06-2027 | 7 | 3.3.3.A02 |
| 3.3.3.A05 | Pruebas de contrato, de falla y de lentitud de la contraparte | ARQ | 4 | 80 | 22-06-2027 | 25-06-2027 | 4 | 3.3.3.A03, 3.3.3.A04 |
| 3.3.3.A06 | Corrección, documentación y entrega en QA | ARQ | 4 | 80 | 28-06-2027 | 01-07-2027 | 4 | 3.3.3.A05 |
| 3.3.4.A01 | Análisis de la interfaz con muestras reales y horarios | ARQ | 4 | 80 | 10-06-2027 | 15-06-2027 | 4 | — |
| 3.3.4.A02 | Diseño del contrato, del manejo de errores y de la idempotencia | ARQ | 4 | 80 | 16-06-2027 | 21-06-2027 | 4 | 3.3.4.A01 |
| 3.3.4.A03 | Construcción del adaptador, parte 1 | ARQ | 2 | 80 | 22-06-2027 | 30-06-2027 | 7 | 3.3.4.A02 |
| 3.3.4.A04 | Construcción del adaptador, parte 2, con reintentos | ARQ | 2 | 80 | 22-06-2027 | 30-06-2027 | 7 | 3.3.4.A02 |
| 3.3.4.A05 | Pruebas de contrato, de falla y de lentitud de la contraparte | ARQ | 4 | 80 | 01-07-2027 | 06-07-2027 | 4 | 3.3.4.A03, 3.3.4.A04 |
| 3.3.4.A06 | Corrección, documentación y entrega en QA | ARQ | 4 | 80 | 07-07-2027 | 12-07-2027 | 4 | 3.3.4.A05 |
| 3.3.5.A01 | Análisis de la interfaz con muestras reales y horarios | ARQ | 4 | 80 | 02-07-2027 | 07-07-2027 | 4 | — |
| 3.3.5.A02 | Diseño del contrato, del manejo de errores y de la idempotencia | ARQ | 4 | 80 | 08-07-2027 | 13-07-2027 | 4 | 3.3.5.A01 |
| 3.3.5.A03 | Construcción del adaptador, parte 1 | ARQ | 2 | 80 | 14-07-2027 | 22-07-2027 | 7 | 3.3.5.A02 |
| 3.3.5.A04 | Construcción del adaptador, parte 2, con reintentos | ARQ | 2 | 80 | 14-07-2027 | 22-07-2027 | 7 | 3.3.5.A02 |
| 3.3.5.A05 | Pruebas de contrato, de falla y de lentitud de la contraparte | ARQ | 4 | 80 | 23-07-2027 | 28-07-2027 | 4 | 3.3.5.A03, 3.3.5.A04 |
| 3.3.5.A06 | Corrección, documentación y entrega en QA | ARQ | 4 | 80 | 29-07-2027 | 03-08-2027 | 4 | 3.3.5.A05 |
| 3.3.6.A01 | Análisis de la interfaz con muestras reales y horarios | ARQ | 4 | 80 | 02-07-2027 | 07-07-2027 | 4 | — |
| 3.3.6.A02 | Diseño del contrato, del manejo de errores y de la idempotencia | ARQ | 4 | 80 | 08-07-2027 | 13-07-2027 | 4 | 3.3.6.A01 |
| 3.3.6.A03 | Construcción del adaptador, parte 1 | ARQ | 2 | 80 | 14-07-2027 | 22-07-2027 | 7 | 3.3.6.A02 |
| 3.3.6.A04 | Construcción del adaptador, parte 2, con reintentos | ARQ | 2 | 80 | 14-07-2027 | 22-07-2027 | 7 | 3.3.6.A02 |
| 3.3.6.A05 | Pruebas de contrato, de falla y de lentitud de la contraparte | ARQ | 4 | 80 | 23-07-2027 | 28-07-2027 | 4 | 3.3.6.A03, 3.3.6.A04 |
| 3.3.6.A06 | Corrección, documentación y entrega en QA | ARQ | 4 | 80 | 29-07-2027 | 03-08-2027 | 4 | 3.3.6.A05 |
| 3.4.1.A01 | Análisis de los requerimientos del T-12 asignados y de sus criterios de aceptación | DES | 12 | 80 | 06-07-2027 | 07-07-2027 | 2 | 2.4.1.A03, 2.6.2.A03, 3.3.1.A01 (CC), 3.3.2.A01 (CC), 3.3.3.A01 (CC), 3.3.4.A01 (CC), 3.3.5.A01 (CC), 3.3.6.A01 (CC) |
| 3.4.1.A02 | Diseño detallado del módulo y de sus contratos de interfaz | DES | 12 | 80 | 08-07-2027 | 09-07-2027 | 2 | 3.4.1.A01 |
| 3.4.1.A03 | Construcción, incremento 1 | DES | 2 | 80 | 12-07-2027 | 20-07-2027 | 7 | 3.4.1.A02 |
| 3.4.1.A04 | Construcción, incremento 2 | DES | 2 | 80 | 12-07-2027 | 20-07-2027 | 7 | 3.4.1.A02 |
| 3.4.1.A05 | Construcción, incremento 3 | DES | 2 | 80 | 12-07-2027 | 20-07-2027 | 7 | 3.4.1.A02 |
| 3.4.1.A06 | Construcción, incremento 4 | DES | 2 | 80 | 12-07-2027 | 20-07-2027 | 7 | 3.4.1.A02 |
| 3.4.1.A07 | Construcción, incremento 5 | DES | 2 | 80 | 12-07-2027 | 20-07-2027 | 7 | 3.4.1.A02 |
| 3.4.1.A08 | Construcción, incremento 6 | DES | 2 | 80 | 12-07-2027 | 20-07-2027 | 7 | 3.4.1.A02 |
| 3.4.1.A09 | Pruebas unitarias y de contrato | DES | 12 | 80 | 21-07-2027 | 22-07-2027 | 2 | 3.4.1.A03, 3.4.1.A04, 3.4.1.A05, 3.4.1.A06, 3.4.1.A07, 3.4.1.A08 |
| 3.4.1.A10 | Integración con la base compartida y pruebas en QA | DES | 6 | 80 | 23-07-2027 | 27-07-2027 | 3 | 3.4.1.A09 |
| 3.4.1.A11 | Corrección de los defectos de QA | DES | 6 | 80 | 23-07-2027 | 27-07-2027 | 3 | 3.4.1.A09 |
| 3.4.1.A12 | Documentación y entrega en QA | DES | 12 | 80 | 28-07-2027 | 29-07-2027 | 2 | 3.4.1.A10, 3.4.1.A11, 3.1.1.A03, 3.1.2.A03, 3.1.3.A03, 3.1.4.A03, 3.1.5.A03 |
| 3.4.2.A01 | Análisis de los requerimientos del T-12 asignados y de sus criterios de aceptación | DES | 12 | 80 | 06-07-2027 | 07-07-2027 | 2 | 2.4.1.A03, 2.6.2.A03, 3.3.1.A01 (CC), 3.3.2.A01 (CC), 3.3.3.A01 (CC), 3.3.4.A01 (CC), 3.3.5.A01 (CC), 3.3.6.A01 (CC) |
| 3.4.2.A02 | Diseño detallado del módulo y de sus contratos de interfaz | DES | 12 | 80 | 08-07-2027 | 09-07-2027 | 2 | 3.4.2.A01 |
| 3.4.2.A03 | Construcción, incremento 1 | DES | 2 | 80 | 12-07-2027 | 20-07-2027 | 7 | 3.4.2.A02 |
| 3.4.2.A04 | Construcción, incremento 2 | DES | 2 | 80 | 12-07-2027 | 20-07-2027 | 7 | 3.4.2.A02 |
| 3.4.2.A05 | Construcción, incremento 3 | DES | 2 | 80 | 12-07-2027 | 20-07-2027 | 7 | 3.4.2.A02 |
| 3.4.2.A06 | Construcción, incremento 4 | DES | 2 | 80 | 12-07-2027 | 20-07-2027 | 7 | 3.4.2.A02 |
| 3.4.2.A07 | Construcción, incremento 5 | DES | 2 | 80 | 12-07-2027 | 20-07-2027 | 7 | 3.4.2.A02 |
| 3.4.2.A08 | Construcción, incremento 6 | DES | 2 | 80 | 12-07-2027 | 20-07-2027 | 7 | 3.4.2.A02 |
| 3.4.2.A09 | Pruebas unitarias y de contrato | DES | 12 | 80 | 21-07-2027 | 22-07-2027 | 2 | 3.4.2.A03, 3.4.2.A04, 3.4.2.A05, 3.4.2.A06, 3.4.2.A07, 3.4.2.A08 |
| 3.4.2.A10 | Integración con la base compartida y pruebas en QA | DES | 6 | 80 | 23-07-2027 | 27-07-2027 | 3 | 3.4.2.A09 |
| 3.4.2.A11 | Corrección de los defectos de QA | DES | 6 | 80 | 23-07-2027 | 27-07-2027 | 3 | 3.4.2.A09 |
| 3.4.2.A12 | Documentación y entrega en QA | DES | 12 | 80 | 28-07-2027 | 29-07-2027 | 2 | 3.4.2.A10, 3.4.2.A11, 3.1.1.A03, 3.1.2.A03, 3.1.3.A03, 3.1.4.A03, 3.1.5.A03 |
| 3.4.3.A01 | Análisis de los requerimientos del T-12 asignados y de sus criterios de aceptación | DES | 12 | 80 | 06-07-2027 | 07-07-2027 | 2 | 2.4.1.A03, 2.6.2.A03, 3.3.1.A01 (CC), 3.3.2.A01 (CC), 3.3.3.A01 (CC), 3.3.4.A01 (CC), 3.3.5.A01 (CC), 3.3.6.A01 (CC) |
| 3.4.3.A02 | Diseño detallado del módulo y de sus contratos de interfaz | DES | 12 | 80 | 08-07-2027 | 09-07-2027 | 2 | 3.4.3.A01 |
| 3.4.3.A03 | Construcción, incremento 1 | DES | 2 | 80 | 12-07-2027 | 20-07-2027 | 7 | 3.4.3.A02, 3.4.1.A02, 3.4.2.A02 |
| 3.4.3.A04 | Construcción, incremento 2 | DES | 2 | 80 | 12-07-2027 | 20-07-2027 | 7 | 3.4.3.A02, 3.4.1.A02, 3.4.2.A02 |
| 3.4.3.A05 | Construcción, incremento 3 | DES | 2 | 80 | 12-07-2027 | 20-07-2027 | 7 | 3.4.3.A02, 3.4.1.A02, 3.4.2.A02 |
| 3.4.3.A06 | Construcción, incremento 4 | DES | 2 | 80 | 12-07-2027 | 20-07-2027 | 7 | 3.4.3.A02, 3.4.1.A02, 3.4.2.A02 |
| 3.4.3.A07 | Construcción, incremento 5 | DES | 2 | 80 | 12-07-2027 | 20-07-2027 | 7 | 3.4.3.A02, 3.4.1.A02, 3.4.2.A02 |
| 3.4.3.A08 | Construcción, incremento 6 | DES | 2 | 80 | 12-07-2027 | 20-07-2027 | 7 | 3.4.3.A02, 3.4.1.A02, 3.4.2.A02 |
| 3.4.3.A09 | Pruebas unitarias y de contrato | DES | 12 | 80 | 21-07-2027 | 22-07-2027 | 2 | 3.4.3.A03, 3.4.3.A04, 3.4.3.A05, 3.4.3.A06, 3.4.3.A07, 3.4.3.A08 |
| 3.4.3.A10 | Integración con la base compartida y pruebas en QA | DES | 6 | 80 | 30-07-2027 | 03-08-2027 | 3 | 3.4.3.A09, 3.4.1.A12, 3.4.2.A12 |
| 3.4.3.A11 | Corrección de los defectos de QA | DES | 6 | 80 | 30-07-2027 | 03-08-2027 | 3 | 3.4.3.A09, 3.4.1.A12, 3.4.2.A12 |
| 3.4.3.A12 | Documentación y entrega en QA | DES | 12 | 80 | 04-08-2027 | 05-08-2027 | 2 | 3.4.3.A10, 3.4.3.A11, 3.1.1.A03, 3.1.2.A03, 3.1.3.A03, 3.1.4.A03, 3.1.5.A03 |
| 3.4.4.A01 | Análisis de los requerimientos del T-12 asignados y de sus criterios de aceptación | DES | 12 | 80 | 01-09-2027 | 02-09-2027 | 2 | 2.4.1.A03, 2.6.2.A03, 3.3.1.A01 (CC), 3.3.2.A01 (CC), 3.3.3.A01 (CC), 3.3.4.A01 (CC), 3.3.5.A01 (CC), 3.3.6.A01 (CC) |
| 3.4.4.A02 | Diseño detallado del módulo y de sus contratos de interfaz | DES | 12 | 80 | 03-09-2027 | 06-09-2027 | 2 | 3.4.4.A01 |
| 3.4.4.A03 | Construcción, incremento 1 | DES | 2 | 80 | 07-09-2027 | 15-09-2027 | 7 | 3.4.4.A02, 3.4.1.A02, 3.4.2.A02 |
| 3.4.4.A04 | Construcción, incremento 2 | DES | 2 | 80 | 07-09-2027 | 15-09-2027 | 7 | 3.4.4.A02, 3.4.1.A02, 3.4.2.A02 |
| 3.4.4.A05 | Construcción, incremento 3 | DES | 2 | 80 | 07-09-2027 | 15-09-2027 | 7 | 3.4.4.A02, 3.4.1.A02, 3.4.2.A02 |
| 3.4.4.A06 | Construcción, incremento 4 | DES | 2 | 80 | 07-09-2027 | 15-09-2027 | 7 | 3.4.4.A02, 3.4.1.A02, 3.4.2.A02 |
| 3.4.4.A07 | Construcción, incremento 5 | DES | 2 | 80 | 07-09-2027 | 15-09-2027 | 7 | 3.4.4.A02, 3.4.1.A02, 3.4.2.A02 |
| 3.4.4.A08 | Construcción, incremento 6 | DES | 2 | 80 | 07-09-2027 | 15-09-2027 | 7 | 3.4.4.A02, 3.4.1.A02, 3.4.2.A02 |
| 3.4.4.A09 | Pruebas unitarias y de contrato | DES | 12 | 80 | 16-09-2027 | 17-09-2027 | 2 | 3.4.4.A03, 3.4.4.A04, 3.4.4.A05, 3.4.4.A06, 3.4.4.A07, 3.4.4.A08 |
| 3.4.4.A10 | Integración con la base compartida y pruebas en QA | DES | 6 | 80 | 20-09-2027 | 22-09-2027 | 3 | 3.4.4.A09, 3.4.1.A12, 3.4.2.A12 |
| 3.4.4.A11 | Corrección de los defectos de QA | DES | 6 | 80 | 20-09-2027 | 22-09-2027 | 3 | 3.4.4.A09, 3.4.1.A12, 3.4.2.A12 |
| 3.4.4.A12 | Documentación y entrega en QA | DES | 12 | 80 | 23-09-2027 | 24-09-2027 | 2 | 3.4.4.A10, 3.4.4.A11, 3.1.1.A03, 3.1.2.A03, 3.1.3.A03, 3.1.4.A03, 3.1.5.A03 |
| 3.4.5.A01 | Análisis de los requerimientos del T-12 asignados y de sus criterios de aceptación | DES | 12 | 80 | 23-07-2027 | 26-07-2027 | 2 | 2.4.1.A03, 2.6.2.A03, 3.2.3.A03, 3.3.1.A01 (CC), 3.3.2.A01 (CC), 3.3.3.A01 (CC), 3.3.4.A01 (CC), 3.3.5.A01 (CC), 3.3.6.A01 (CC) |
| 3.4.5.A02 | Diseño detallado del módulo y de sus contratos de interfaz | DES | 12 | 80 | 27-07-2027 | 28-07-2027 | 2 | 3.4.5.A01 |
| 3.4.5.A03 | Construcción, incremento 1 | DES | 2 | 80 | 29-07-2027 | 06-08-2027 | 7 | 3.4.5.A02 |
| 3.4.5.A04 | Construcción, incremento 2 | DES | 2 | 80 | 29-07-2027 | 06-08-2027 | 7 | 3.4.5.A02 |
| 3.4.5.A05 | Construcción, incremento 3 | DES | 2 | 80 | 29-07-2027 | 06-08-2027 | 7 | 3.4.5.A02 |
| 3.4.5.A06 | Construcción, incremento 4 | DES | 2 | 80 | 29-07-2027 | 06-08-2027 | 7 | 3.4.5.A02 |
| 3.4.5.A07 | Construcción, incremento 5 | DES | 2 | 80 | 29-07-2027 | 06-08-2027 | 7 | 3.4.5.A02 |
| 3.4.5.A08 | Construcción, incremento 6 | DES | 2 | 80 | 29-07-2027 | 06-08-2027 | 7 | 3.4.5.A02 |
| 3.4.5.A09 | Pruebas unitarias y de contrato | DES | 12 | 80 | 09-08-2027 | 10-08-2027 | 2 | 3.4.5.A03, 3.4.5.A04, 3.4.5.A05, 3.4.5.A06, 3.4.5.A07, 3.4.5.A08 |
| 3.4.5.A10 | Integración con la base compartida y pruebas en QA | DES | 6 | 80 | 11-08-2027 | 13-08-2027 | 3 | 3.4.5.A09 |
| 3.4.5.A11 | Corrección de los defectos de QA | DES | 6 | 80 | 11-08-2027 | 13-08-2027 | 3 | 3.4.5.A09 |
| 3.4.5.A12 | Documentación y entrega en QA | DES | 12 | 80 | 16-08-2027 | 17-08-2027 | 2 | 3.4.5.A10, 3.4.5.A11, 3.1.1.A03, 3.1.2.A03, 3.1.3.A03, 3.1.4.A03, 3.1.5.A03 |
| 3.4.6.A01 | Análisis de los requerimientos del T-12 asignados y de sus criterios de aceptación | DES | 12 | 80 | 06-07-2027 | 07-07-2027 | 2 | 2.4.1.A03, 2.6.2.A03, 3.3.1.A01 (CC), 3.3.2.A01 (CC), 3.3.3.A01 (CC), 3.3.4.A01 (CC), 3.3.5.A01 (CC), 3.3.6.A01 (CC), 3.4.2.A01 (CC) |
| 3.4.6.A02 | Diseño detallado del módulo y de sus contratos de interfaz | DES | 12 | 80 | 08-07-2027 | 09-07-2027 | 2 | 3.4.6.A01 |
| 3.4.6.A03 | Construcción, incremento 1 | DES | 2 | 80 | 12-07-2027 | 20-07-2027 | 7 | 3.4.6.A02 |
| 3.4.6.A04 | Construcción, incremento 2 | DES | 2 | 80 | 12-07-2027 | 20-07-2027 | 7 | 3.4.6.A02 |
| 3.4.6.A05 | Construcción, incremento 3 | DES | 2 | 80 | 12-07-2027 | 20-07-2027 | 7 | 3.4.6.A02 |
| 3.4.6.A06 | Construcción, incremento 4 | DES | 2 | 80 | 12-07-2027 | 20-07-2027 | 7 | 3.4.6.A02 |
| 3.4.6.A07 | Construcción, incremento 5 | DES | 2 | 80 | 12-07-2027 | 20-07-2027 | 7 | 3.4.6.A02 |
| 3.4.6.A08 | Construcción, incremento 6 | DES | 2 | 80 | 12-07-2027 | 20-07-2027 | 7 | 3.4.6.A02 |
| 3.4.6.A09 | Pruebas unitarias y de contrato | DES | 12 | 80 | 21-07-2027 | 22-07-2027 | 2 | 3.4.6.A03, 3.4.6.A04, 3.4.6.A05, 3.4.6.A06, 3.4.6.A07, 3.4.6.A08 |
| 3.4.6.A10 | Integración con la base compartida y pruebas en QA | DES | 6 | 80 | 23-07-2027 | 27-07-2027 | 3 | 3.4.6.A09 |
| 3.4.6.A11 | Corrección de los defectos de QA | DES | 6 | 80 | 23-07-2027 | 27-07-2027 | 3 | 3.4.6.A09 |
| 3.4.6.A12 | Documentación y entrega en QA | DES | 12 | 80 | 28-07-2027 | 29-07-2027 | 2 | 3.4.6.A10, 3.4.6.A11, 3.1.1.A03, 3.1.2.A03, 3.1.3.A03, 3.1.4.A03, 3.1.5.A03 |
| 3.4.7.A01 | Análisis de los requerimientos del T-12 asignados y de sus criterios de aceptación | DES | 12 | 80 | 02-08-2027 | 03-08-2027 | 2 | 1.2.2.A01, 2.4.1.A03, 2.6.2.A03, 3.3.1.A01 (CC), 3.3.2.A01 (CC), 3.3.3.A01 (CC), 3.3.4.A01 (CC), 3.3.5.A01 (CC), 3.3.6.A01 (CC) |
| 3.4.7.A02 | Diseño detallado del módulo y de sus contratos de interfaz | DES | 12 | 80 | 04-08-2027 | 05-08-2027 | 2 | 3.4.7.A01 |
| 3.4.7.A03 | Construcción, incremento 1 | DES | 2 | 80 | 06-08-2027 | 16-08-2027 | 7 | 3.4.7.A02, 3.4.3.A02, 3.4.6.A02 |
| 3.4.7.A04 | Construcción, incremento 2 | DES | 2 | 80 | 06-08-2027 | 16-08-2027 | 7 | 3.4.7.A02, 3.4.3.A02, 3.4.6.A02 |
| 3.4.7.A05 | Construcción, incremento 3 | DES | 2 | 80 | 06-08-2027 | 16-08-2027 | 7 | 3.4.7.A02, 3.4.3.A02, 3.4.6.A02 |
| 3.4.7.A06 | Construcción, incremento 4 | DES | 2 | 80 | 06-08-2027 | 16-08-2027 | 7 | 3.4.7.A02, 3.4.3.A02, 3.4.6.A02 |
| 3.4.7.A07 | Construcción, incremento 5 | DES | 2 | 80 | 06-08-2027 | 16-08-2027 | 7 | 3.4.7.A02, 3.4.3.A02, 3.4.6.A02 |
| 3.4.7.A08 | Construcción, incremento 6 | DES | 2 | 80 | 06-08-2027 | 16-08-2027 | 7 | 3.4.7.A02, 3.4.3.A02, 3.4.6.A02 |
| 3.4.7.A09 | Pruebas unitarias y de contrato | DES | 12 | 80 | 17-08-2027 | 18-08-2027 | 2 | 3.4.7.A03, 3.4.7.A04, 3.4.7.A05, 3.4.7.A06, 3.4.7.A07, 3.4.7.A08 |
| 3.4.7.A10 | Integración con la base compartida y pruebas en QA | DES | 6 | 80 | 19-08-2027 | 23-08-2027 | 3 | 3.4.7.A09, 3.4.3.A12, 3.4.6.A12 |
| 3.4.7.A11 | Corrección de los defectos de QA | DES | 6 | 80 | 19-08-2027 | 23-08-2027 | 3 | 3.4.7.A09, 3.4.3.A12, 3.4.6.A12 |
| 3.4.7.A12 | Documentación y entrega en QA | DES | 12 | 80 | 24-08-2027 | 25-08-2027 | 2 | 3.4.7.A10, 3.4.7.A11, 3.1.1.A03, 3.1.2.A03, 3.1.3.A03, 3.1.4.A03, 3.1.5.A03 |
| 3.4.8.A01 | Análisis de los requerimientos del T-12 asignados y de sus criterios de aceptación | DES | 12 | 80 | 02-08-2027 | 03-08-2027 | 2 | 2.4.1.A03, 2.6.2.A03, 3.3.1.A01 (CC), 3.3.2.A01 (CC), 3.3.3.A01 (CC), 3.3.4.A01 (CC), 3.3.5.A01 (CC), 3.3.6.A01 (CC) |
| 3.4.8.A02 | Diseño detallado del módulo y de sus contratos de interfaz | DES | 12 | 80 | 04-08-2027 | 05-08-2027 | 2 | 3.4.8.A01 |
| 3.4.8.A03 | Construcción, incremento 1 | DES | 2 | 80 | 06-08-2027 | 16-08-2027 | 7 | 3.4.8.A02, 3.4.3.A02, 3.4.6.A02 |
| 3.4.8.A04 | Construcción, incremento 2 | DES | 2 | 80 | 06-08-2027 | 16-08-2027 | 7 | 3.4.8.A02, 3.4.3.A02, 3.4.6.A02 |
| 3.4.8.A05 | Construcción, incremento 3 | DES | 2 | 80 | 06-08-2027 | 16-08-2027 | 7 | 3.4.8.A02, 3.4.3.A02, 3.4.6.A02 |
| 3.4.8.A06 | Construcción, incremento 4 | DES | 2 | 80 | 06-08-2027 | 16-08-2027 | 7 | 3.4.8.A02, 3.4.3.A02, 3.4.6.A02 |
| 3.4.8.A07 | Construcción, incremento 5 | DES | 2 | 80 | 06-08-2027 | 16-08-2027 | 7 | 3.4.8.A02, 3.4.3.A02, 3.4.6.A02 |
| 3.4.8.A08 | Construcción, incremento 6 | DES | 2 | 80 | 06-08-2027 | 16-08-2027 | 7 | 3.4.8.A02, 3.4.3.A02, 3.4.6.A02 |
| 3.4.8.A09 | Pruebas unitarias y de contrato | DES | 12 | 80 | 17-08-2027 | 18-08-2027 | 2 | 3.4.8.A03, 3.4.8.A04, 3.4.8.A05, 3.4.8.A06, 3.4.8.A07, 3.4.8.A08 |
| 3.4.8.A10 | Integración con la base compartida y pruebas en QA | DES | 6 | 80 | 19-08-2027 | 23-08-2027 | 3 | 3.4.8.A09, 3.4.3.A12, 3.4.6.A12 |
| 3.4.8.A11 | Corrección de los defectos de QA | DES | 6 | 80 | 19-08-2027 | 23-08-2027 | 3 | 3.4.8.A09, 3.4.3.A12, 3.4.6.A12 |
| 3.4.8.A12 | Documentación y entrega en QA | DES | 12 | 80 | 24-08-2027 | 25-08-2027 | 2 | 3.4.8.A10, 3.4.8.A11, 3.1.1.A03, 3.1.2.A03, 3.1.3.A03, 3.1.4.A03, 3.1.5.A03 |
| 3.4.9.A01 | Análisis de los requerimientos del T-12 asignados y de sus criterios de aceptación | DES | 12 | 80 | 01-09-2027 | 02-09-2027 | 2 | 2.4.1.A03, 2.6.2.A03, 3.3.1.A01 (CC), 3.3.2.A01 (CC), 3.3.3.A01 (CC), 3.3.4.A01 (CC), 3.3.5.A01 (CC), 3.3.6.A01 (CC) |
| 3.4.9.A02 | Diseño detallado del módulo y de sus contratos de interfaz | DES | 12 | 80 | 03-09-2027 | 06-09-2027 | 2 | 3.4.9.A01 |
| 3.4.9.A03 | Construcción, incremento 1 | DES | 2 | 80 | 07-09-2027 | 15-09-2027 | 7 | 3.4.9.A02 |
| 3.4.9.A04 | Construcción, incremento 2 | DES | 2 | 80 | 07-09-2027 | 15-09-2027 | 7 | 3.4.9.A02 |
| 3.4.9.A05 | Construcción, incremento 3 | DES | 2 | 80 | 07-09-2027 | 15-09-2027 | 7 | 3.4.9.A02 |
| 3.4.9.A06 | Construcción, incremento 4 | DES | 2 | 80 | 07-09-2027 | 15-09-2027 | 7 | 3.4.9.A02 |
| 3.4.9.A07 | Construcción, incremento 5 | DES | 2 | 80 | 07-09-2027 | 15-09-2027 | 7 | 3.4.9.A02 |
| 3.4.9.A08 | Construcción, incremento 6 | DES | 2 | 80 | 07-09-2027 | 15-09-2027 | 7 | 3.4.9.A02 |
| 3.4.9.A09 | Pruebas unitarias y de contrato | DES | 12 | 80 | 16-09-2027 | 17-09-2027 | 2 | 3.4.9.A03, 3.4.9.A04, 3.4.9.A05, 3.4.9.A06, 3.4.9.A07, 3.4.9.A08 |
| 3.4.9.A10 | Integración con la base compartida y pruebas en QA | DES | 6 | 80 | 20-09-2027 | 22-09-2027 | 3 | 3.4.9.A09 |
| 3.4.9.A11 | Corrección de los defectos de QA | DES | 6 | 80 | 20-09-2027 | 22-09-2027 | 3 | 3.4.9.A09 |
| 3.4.9.A12 | Documentación y entrega en QA | DES | 12 | 80 | 23-09-2027 | 24-09-2027 | 2 | 3.4.9.A10, 3.4.9.A11, 3.1.1.A03, 3.1.2.A03, 3.1.3.A03, 3.1.4.A03, 3.1.5.A03 |
| 3.4.10.A01 | Análisis de los requerimientos del T-12 asignados y de sus criterios de aceptación | DES | 12 | 80 | 01-09-2027 | 02-09-2027 | 2 | 2.4.1.A03, 2.6.2.A03, 3.3.1.A01 (CC), 3.3.2.A01 (CC), 3.3.3.A01 (CC), 3.3.4.A01 (CC), 3.3.5.A01 (CC), 3.3.6.A01 (CC) |
| 3.4.10.A02 | Diseño detallado del módulo y de sus contratos de interfaz | DES | 12 | 80 | 03-09-2027 | 06-09-2027 | 2 | 3.4.10.A01 |
| 3.4.10.A03 | Construcción, incremento 1 | DES | 2 | 80 | 07-09-2027 | 15-09-2027 | 7 | 3.4.10.A02, 3.4.8.A02 |
| 3.4.10.A04 | Construcción, incremento 2 | DES | 2 | 80 | 07-09-2027 | 15-09-2027 | 7 | 3.4.10.A02, 3.4.8.A02 |
| 3.4.10.A05 | Construcción, incremento 3 | DES | 2 | 80 | 07-09-2027 | 15-09-2027 | 7 | 3.4.10.A02, 3.4.8.A02 |
| 3.4.10.A06 | Construcción, incremento 4 | DES | 2 | 80 | 07-09-2027 | 15-09-2027 | 7 | 3.4.10.A02, 3.4.8.A02 |
| 3.4.10.A07 | Construcción, incremento 5 | DES | 2 | 80 | 07-09-2027 | 15-09-2027 | 7 | 3.4.10.A02, 3.4.8.A02 |
| 3.4.10.A08 | Construcción, incremento 6 | DES | 2 | 80 | 07-09-2027 | 15-09-2027 | 7 | 3.4.10.A02, 3.4.8.A02 |
| 3.4.10.A09 | Pruebas unitarias y de contrato | DES | 12 | 80 | 16-09-2027 | 17-09-2027 | 2 | 3.4.10.A03, 3.4.10.A04, 3.4.10.A05, 3.4.10.A06, 3.4.10.A07, 3.4.10.A08 |
| 3.4.10.A10 | Integración con la base compartida y pruebas en QA | DES | 6 | 80 | 20-09-2027 | 22-09-2027 | 3 | 3.4.10.A09, 3.4.8.A12 |
| 3.4.10.A11 | Corrección de los defectos de QA | DES | 6 | 80 | 20-09-2027 | 22-09-2027 | 3 | 3.4.10.A09, 3.4.8.A12 |
| 3.4.10.A12 | Documentación y entrega en QA | DES | 12 | 80 | 23-09-2027 | 24-09-2027 | 2 | 3.4.10.A10, 3.4.10.A11, 3.1.1.A03, 3.1.2.A03, 3.1.3.A03, 3.1.4.A03, 3.1.5.A03 |
| 3.4.11.A01 | Análisis de los requerimientos del T-12 asignados y de sus criterios de aceptación | DAT | 12 | 80 | 02-09-2027 | 03-09-2027 | 2 | 2.4.1.A03, 2.6.2.A03, 3.3.1.A01 (CC), 3.3.2.A01 (CC), 3.3.3.A01 (CC), 3.3.4.A01 (CC), 3.3.5.A01 (CC), 3.3.6.A01 (CC) |
| 3.4.11.A02 | Diseño detallado del módulo y de sus contratos de interfaz | DAT | 12 | 80 | 06-09-2027 | 07-09-2027 | 2 | 3.4.11.A01 |
| 3.4.11.A03 | Construcción, incremento 1 | DAT | 2 | 80 | 08-09-2027 | 16-09-2027 | 7 | 3.4.11.A02 |
| 3.4.11.A04 | Construcción, incremento 2 | DAT | 2 | 80 | 08-09-2027 | 16-09-2027 | 7 | 3.4.11.A02 |
| 3.4.11.A05 | Construcción, incremento 3 | DAT | 2 | 80 | 08-09-2027 | 16-09-2027 | 7 | 3.4.11.A02 |
| 3.4.11.A06 | Construcción, incremento 4 | DAT | 2 | 80 | 08-09-2027 | 16-09-2027 | 7 | 3.4.11.A02 |
| 3.4.11.A07 | Construcción, incremento 5 | DAT | 2 | 80 | 08-09-2027 | 16-09-2027 | 7 | 3.4.11.A02 |
| 3.4.11.A08 | Construcción, incremento 6 | DAT | 2 | 80 | 08-09-2027 | 16-09-2027 | 7 | 3.4.11.A02 |
| 3.4.11.A09 | Pruebas unitarias y de contrato | DAT | 12 | 80 | 17-09-2027 | 20-09-2027 | 2 | 3.4.11.A03, 3.4.11.A04, 3.4.11.A05, 3.4.11.A06, 3.4.11.A07, 3.4.11.A08 |
| 3.4.11.A10 | Integración con la base compartida y pruebas en QA | DAT | 6 | 80 | 21-09-2027 | 23-09-2027 | 3 | 3.4.11.A09 |
| 3.4.11.A11 | Corrección de los defectos de QA | DAT | 6 | 80 | 21-09-2027 | 23-09-2027 | 3 | 3.4.11.A09 |
| 3.4.11.A12 | Documentación y entrega en QA | DAT | 12 | 80 | 24-09-2027 | 27-09-2027 | 2 | 3.4.11.A10, 3.4.11.A11, 3.1.1.A03, 3.1.2.A03, 3.1.3.A03, 3.1.4.A03, 3.1.5.A03 |
| 3.5.1.A01 | Análisis de los requerimientos del T-12 asignados y de sus criterios de aceptación | DES | 12 | 80 | 03-04-2028 | 04-04-2028 | 2 | 1.2.5.A01, 2.4.2.A03 |
| 3.5.1.A02 | Diseño detallado del módulo y de sus contratos de interfaz | DES | 12 | 80 | 05-04-2028 | 06-04-2028 | 2 | 3.5.1.A01 |
| 3.5.1.A03 | Construcción, incremento 1 | DES | 2 | 80 | 07-04-2028 | 17-04-2028 | 7 | 3.5.1.A02 |
| 3.5.1.A04 | Construcción, incremento 2 | DES | 2 | 80 | 07-04-2028 | 17-04-2028 | 7 | 3.5.1.A02 |
| 3.5.1.A05 | Construcción, incremento 3 | DES | 2 | 80 | 07-04-2028 | 17-04-2028 | 7 | 3.5.1.A02 |
| 3.5.1.A06 | Construcción, incremento 4 | DES | 2 | 80 | 07-04-2028 | 17-04-2028 | 7 | 3.5.1.A02 |
| 3.5.1.A07 | Construcción, incremento 5 | DES | 2 | 80 | 07-04-2028 | 17-04-2028 | 7 | 3.5.1.A02 |
| 3.5.1.A08 | Construcción, incremento 6 | DES | 2 | 80 | 07-04-2028 | 17-04-2028 | 7 | 3.5.1.A02 |
| 3.5.1.A09 | Pruebas unitarias y de contrato | DES | 12 | 80 | 18-04-2028 | 19-04-2028 | 2 | 3.5.1.A03, 3.5.1.A04, 3.5.1.A05, 3.5.1.A06, 3.5.1.A07, 3.5.1.A08 |
| 3.5.1.A10 | Integración con la base compartida y pruebas en QA | DES | 6 | 80 | 20-04-2028 | 24-04-2028 | 3 | 3.5.1.A09 |
| 3.5.1.A11 | Corrección de los defectos de QA | DES | 6 | 80 | 20-04-2028 | 24-04-2028 | 3 | 3.5.1.A09 |
| 3.5.1.A12 | Documentación y entrega en QA | DES | 12 | 80 | 25-04-2028 | 26-04-2028 | 2 | 3.5.1.A10, 3.5.1.A11 |
| 3.5.2.A01 | Análisis de los requerimientos del T-12 asignados y de sus criterios de aceptación | DES | 12 | 80 | 03-04-2028 | 04-04-2028 | 2 | 1.2.5.A01, 2.4.2.A03 |
| 3.5.2.A02 | Diseño detallado del módulo y de sus contratos de interfaz | DES | 12 | 80 | 05-04-2028 | 06-04-2028 | 2 | 3.5.2.A01 |
| 3.5.2.A03 | Construcción, incremento 1 | DES | 2 | 80 | 07-04-2028 | 17-04-2028 | 7 | 3.5.2.A02 |
| 3.5.2.A04 | Construcción, incremento 2 | DES | 2 | 80 | 07-04-2028 | 17-04-2028 | 7 | 3.5.2.A02 |
| 3.5.2.A05 | Construcción, incremento 3 | DES | 2 | 80 | 07-04-2028 | 17-04-2028 | 7 | 3.5.2.A02 |
| 3.5.2.A06 | Construcción, incremento 4 | DES | 2 | 80 | 07-04-2028 | 17-04-2028 | 7 | 3.5.2.A02 |
| 3.5.2.A07 | Construcción, incremento 5 | DES | 2 | 80 | 07-04-2028 | 17-04-2028 | 7 | 3.5.2.A02 |
| 3.5.2.A08 | Construcción, incremento 6 | DES | 2 | 80 | 07-04-2028 | 17-04-2028 | 7 | 3.5.2.A02 |
| 3.5.2.A09 | Pruebas unitarias y de contrato | DES | 12 | 80 | 18-04-2028 | 19-04-2028 | 2 | 3.5.2.A03, 3.5.2.A04, 3.5.2.A05, 3.5.2.A06, 3.5.2.A07, 3.5.2.A08 |
| 3.5.2.A10 | Integración con la base compartida y pruebas en QA | DES | 6 | 80 | 20-04-2028 | 24-04-2028 | 3 | 3.5.2.A09 |
| 3.5.2.A11 | Corrección de los defectos de QA | DES | 6 | 80 | 20-04-2028 | 24-04-2028 | 3 | 3.5.2.A09 |
| 3.5.2.A12 | Documentación y entrega en QA | DES | 12 | 80 | 25-04-2028 | 26-04-2028 | 2 | 3.5.2.A10, 3.5.2.A11 |
| 3.5.3.A01 | Análisis de los requerimientos del T-12 asignados y de sus criterios de aceptación | DES | 12 | 80 | 03-04-2028 | 04-04-2028 | 2 | 1.2.5.A01, 2.4.2.A03 |
| 3.5.3.A02 | Diseño detallado del módulo y de sus contratos de interfaz | DES | 12 | 80 | 05-04-2028 | 06-04-2028 | 2 | 3.5.3.A01 |
| 3.5.3.A03 | Construcción, incremento 1 | DES | 2 | 80 | 07-04-2028 | 17-04-2028 | 7 | 3.5.3.A02 |
| 3.5.3.A04 | Construcción, incremento 2 | DES | 2 | 80 | 07-04-2028 | 17-04-2028 | 7 | 3.5.3.A02 |
| 3.5.3.A05 | Construcción, incremento 3 | DES | 2 | 80 | 07-04-2028 | 17-04-2028 | 7 | 3.5.3.A02 |
| 3.5.3.A06 | Construcción, incremento 4 | DES | 2 | 80 | 07-04-2028 | 17-04-2028 | 7 | 3.5.3.A02 |
| 3.5.3.A07 | Construcción, incremento 5 | DES | 2 | 80 | 07-04-2028 | 17-04-2028 | 7 | 3.5.3.A02 |
| 3.5.3.A08 | Construcción, incremento 6 | DES | 2 | 80 | 07-04-2028 | 17-04-2028 | 7 | 3.5.3.A02 |
| 3.5.3.A09 | Pruebas unitarias y de contrato | DES | 12 | 80 | 18-04-2028 | 19-04-2028 | 2 | 3.5.3.A03, 3.5.3.A04, 3.5.3.A05, 3.5.3.A06, 3.5.3.A07, 3.5.3.A08 |
| 3.5.3.A10 | Integración con la base compartida y pruebas en QA | DES | 6 | 80 | 20-04-2028 | 24-04-2028 | 3 | 3.5.3.A09 |
| 3.5.3.A11 | Corrección de los defectos de QA | DES | 6 | 80 | 20-04-2028 | 24-04-2028 | 3 | 3.5.3.A09 |
| 3.5.3.A12 | Documentación y entrega en QA | DES | 12 | 80 | 25-04-2028 | 26-04-2028 | 2 | 3.5.3.A10, 3.5.3.A11 |
| 3.5.4.A01 | Análisis de los requerimientos del T-12 asignados y de sus criterios de aceptación | DAT | 12 | 80 | 03-04-2028 | 04-04-2028 | 2 | 1.2.5.A01, 2.4.2.A03 |
| 3.5.4.A02 | Diseño detallado del módulo y de sus contratos de interfaz | DAT | 12 | 80 | 05-04-2028 | 06-04-2028 | 2 | 3.5.4.A01 |
| 3.5.4.A03 | Construcción, incremento 1 | DAT | 2 | 80 | 07-04-2028 | 17-04-2028 | 7 | 3.5.4.A02 |
| 3.5.4.A04 | Construcción, incremento 2 | DAT | 2 | 80 | 07-04-2028 | 17-04-2028 | 7 | 3.5.4.A02 |
| 3.5.4.A05 | Construcción, incremento 3 | DAT | 2 | 80 | 07-04-2028 | 17-04-2028 | 7 | 3.5.4.A02 |
| 3.5.4.A06 | Construcción, incremento 4 | DAT | 2 | 80 | 07-04-2028 | 17-04-2028 | 7 | 3.5.4.A02 |
| 3.5.4.A07 | Construcción, incremento 5 | DAT | 2 | 80 | 07-04-2028 | 17-04-2028 | 7 | 3.5.4.A02 |
| 3.5.4.A08 | Construcción, incremento 6 | DAT | 2 | 80 | 07-04-2028 | 17-04-2028 | 7 | 3.5.4.A02 |
| 3.5.4.A09 | Pruebas unitarias y de contrato | DAT | 12 | 80 | 18-04-2028 | 19-04-2028 | 2 | 3.5.4.A03, 3.5.4.A04, 3.5.4.A05, 3.5.4.A06, 3.5.4.A07, 3.5.4.A08 |
| 3.5.4.A10 | Integración con la base compartida y pruebas en QA | DAT | 6 | 80 | 20-04-2028 | 24-04-2028 | 3 | 3.5.4.A09 |
| 3.5.4.A11 | Corrección de los defectos de QA | DAT | 6 | 80 | 20-04-2028 | 24-04-2028 | 3 | 3.5.4.A09 |
| 3.5.4.A12 | Documentación y entrega en QA | DAT | 12 | 80 | 25-04-2028 | 26-04-2028 | 2 | 3.5.4.A10, 3.5.4.A11 |
| 3.6.1.A01 | Análisis de la interfaz con muestras reales y horarios | DAT | 4 | 80 | 11-10-2027 | 14-10-2027 | 4 | — |
| 3.6.1.A02 | Diseño del contrato, del manejo de errores y de la idempotencia | DAT | 4 | 80 | 15-10-2027 | 20-10-2027 | 4 | 3.6.1.A01 |
| 3.6.1.A03 | Construcción del adaptador, parte 1 | DAT | 2 | 80 | 21-10-2027 | 29-10-2027 | 7 | 3.6.1.A02 |
| 3.6.1.A04 | Construcción del adaptador, parte 2, con reintentos | DAT | 2 | 80 | 21-10-2027 | 29-10-2027 | 7 | 3.6.1.A02 |
| 3.6.1.A05 | Pruebas de contrato, de falla y de lentitud de la contraparte | DAT | 4 | 80 | 01-11-2027 | 04-11-2027 | 4 | 3.6.1.A03, 3.6.1.A04 |
| 3.6.1.A06 | Corrección, documentación y entrega en QA | DAT | 4 | 80 | 05-11-2027 | 10-11-2027 | 4 | 3.6.1.A05 |
| 3.6.2.A01 | Análisis de la interfaz con muestras reales y horarios | DES | 4 | 80 | 06-08-2027 | 11-08-2027 | 4 | — |
| 3.6.2.A02 | Diseño del contrato, del manejo de errores y de la idempotencia | DES | 4 | 80 | 12-08-2027 | 17-08-2027 | 4 | 3.6.2.A01 |
| 3.6.2.A03 | Construcción del adaptador, parte 1 | DES | 2 | 80 | 18-08-2027 | 26-08-2027 | 7 | 3.6.2.A02 |
| 3.6.2.A04 | Construcción del adaptador, parte 2, con reintentos | DES | 2 | 80 | 18-08-2027 | 26-08-2027 | 7 | 3.6.2.A02 |
| 3.6.2.A05 | Pruebas de contrato, de falla y de lentitud de la contraparte | DES | 4 | 80 | 27-08-2027 | 01-09-2027 | 4 | 3.6.2.A03, 3.6.2.A04 |
| 3.6.2.A06 | Corrección, documentación y entrega en QA | DES | 4 | 80 | 02-09-2027 | 07-09-2027 | 4 | 3.6.2.A05 |
| 3.6.3.A01 | Análisis de la interfaz con muestras reales y horarios | DES | 4 | 80 | 06-08-2027 | 11-08-2027 | 4 | — |
| 3.6.3.A02 | Diseño del contrato, del manejo de errores y de la idempotencia | DES | 4 | 80 | 12-08-2027 | 17-08-2027 | 4 | 3.6.3.A01 |
| 3.6.3.A03 | Construcción del adaptador, parte 1 | DES | 2 | 80 | 18-08-2027 | 26-08-2027 | 7 | 3.6.3.A02 |
| 3.6.3.A04 | Construcción del adaptador, parte 2, con reintentos | DES | 2 | 80 | 18-08-2027 | 26-08-2027 | 7 | 3.6.3.A02 |
| 3.6.3.A05 | Pruebas de contrato, de falla y de lentitud de la contraparte | DES | 4 | 80 | 27-08-2027 | 01-09-2027 | 4 | 3.6.3.A03, 3.6.3.A04 |
| 3.6.3.A06 | Corrección, documentación y entrega en QA | DES | 4 | 80 | 02-09-2027 | 07-09-2027 | 4 | 3.6.3.A05 |
| 3.6.4.A01 | Análisis de la interfaz con muestras reales y horarios | DES | 4 | 80 | 18-08-2027 | 23-08-2027 | 4 | — |
| 3.6.4.A02 | Diseño del contrato, del manejo de errores y de la idempotencia | DES | 4 | 80 | 24-08-2027 | 27-08-2027 | 4 | 3.6.4.A01 |
| 3.6.4.A03 | Construcción del adaptador, parte 1 | DES | 2 | 80 | 30-08-2027 | 07-09-2027 | 7 | 3.6.4.A02 |
| 3.6.4.A04 | Construcción del adaptador, parte 2, con reintentos | DES | 2 | 80 | 30-08-2027 | 07-09-2027 | 7 | 3.6.4.A02 |
| 3.6.4.A05 | Pruebas de contrato, de falla y de lentitud de la contraparte | DES | 4 | 80 | 08-09-2027 | 13-09-2027 | 4 | 3.6.4.A03, 3.6.4.A04 |
| 3.6.4.A06 | Corrección, documentación y entrega en QA | DES | 4 | 80 | 14-09-2027 | 17-09-2027 | 4 | 3.6.4.A05 |
| 3.6.5.A01 | Análisis de la interfaz con muestras reales y horarios | DES | 2 | 80 | 01-02-2028 | 09-02-2028 | 7 | — |
| 3.6.5.A02 | Diseño del contrato, del manejo de errores y de la idempotencia | DES | 2 | 80 | 08-03-2028 | 16-03-2028 | 7 | 3.6.5.A01 |
| 3.6.5.A03 | Construcción del adaptador, parte 1 | DES | 2 | 80 | 13-04-2028 | 21-04-2028 | 7 | 3.6.5.A02 |
| 3.6.5.A04 | Construcción del adaptador, parte 2, con reintentos | DES | 2 | 80 | 13-04-2028 | 21-04-2028 | 7 | 3.6.5.A02 |
| 3.6.5.A05 | Pruebas de contrato, de falla y de lentitud de la contraparte | DES | 2 | 80 | 19-05-2028 | 29-05-2028 | 7 | 3.6.5.A03, 3.6.5.A04 |
| 3.6.5.A06 | Corrección, documentación y entrega en QA | DES | 2 | 80 | 26-06-2028 | 04-07-2028 | 7 | 3.6.5.A05 |
| 3.6.6.A01 | Análisis de la interfaz con muestras reales y horarios | DES | 2 | 80 | 01-06-2028 | 09-06-2028 | 7 | — |
| 3.6.6.A02 | Diseño del contrato, del manejo de errores y de la idempotencia | DES | 2 | 80 | 20-06-2028 | 28-06-2028 | 7 | 3.6.6.A01 |
| 3.6.6.A03 | Construcción del adaptador, parte 1 | DES | 2 | 80 | 07-07-2028 | 17-07-2028 | 7 | 3.6.6.A02 |
| 3.6.6.A04 | Construcción del adaptador, parte 2, con reintentos | DES | 2 | 80 | 07-07-2028 | 17-07-2028 | 7 | 3.6.6.A02 |
| 3.6.6.A05 | Pruebas de contrato, de falla y de lentitud de la contraparte | DES | 2 | 80 | 27-07-2028 | 04-08-2028 | 7 | 3.6.6.A03, 3.6.6.A04 |
| 3.6.6.A06 | Corrección, documentación y entrega en QA | DES | 2 | 80 | 15-08-2028 | 23-08-2028 | 7 | 3.6.6.A05 |
| 3.7.1.A01 | Análisis de la interfaz con muestras reales y horarios | DAT | 4 | 80 | 02-08-2027 | 05-08-2027 | 4 | — |
| 3.7.1.A02 | Diseño del contrato, del manejo de errores y de la idempotencia | DAT | 4 | 80 | 06-08-2027 | 11-08-2027 | 4 | 3.7.1.A01 |
| 3.7.1.A03 | Construcción del adaptador, parte 1 | DAT | 2 | 80 | 12-08-2027 | 20-08-2027 | 7 | 3.7.1.A02 |
| 3.7.1.A04 | Construcción del adaptador, parte 2, con reintentos | DAT | 2 | 80 | 12-08-2027 | 20-08-2027 | 7 | 3.7.1.A02 |
| 3.7.1.A05 | Pruebas de contrato, de falla y de lentitud de la contraparte | DAT | 4 | 80 | 23-08-2027 | 26-08-2027 | 4 | 3.7.1.A03, 3.7.1.A04 |
| 3.7.1.A06 | Corrección, documentación y entrega en QA | DAT | 4 | 80 | 27-08-2027 | 01-09-2027 | 4 | 3.7.1.A05 |
| 3.7.2.A01 | Análisis de la interfaz con muestras reales y horarios | DAT | 4 | 80 | 01-10-2027 | 06-10-2027 | 4 | — |
| 3.7.2.A02 | Diseño del contrato, del manejo de errores y de la idempotencia | DAT | 4 | 80 | 07-10-2027 | 12-10-2027 | 4 | 3.7.2.A01 |
| 3.7.2.A03 | Construcción del adaptador, parte 1 | DAT | 2 | 80 | 13-10-2027 | 21-10-2027 | 7 | 3.7.2.A02 |
| 3.7.2.A04 | Construcción del adaptador, parte 2, con reintentos | DAT | 2 | 80 | 13-10-2027 | 21-10-2027 | 7 | 3.7.2.A02 |
| 3.7.2.A05 | Pruebas de contrato, de falla y de lentitud de la contraparte | DAT | 4 | 80 | 22-10-2027 | 27-10-2027 | 4 | 3.7.2.A03, 3.7.2.A04 |
| 3.7.2.A06 | Corrección, documentación y entrega en QA | DAT | 4 | 80 | 28-10-2027 | 02-11-2027 | 4 | 3.7.2.A05 |
| 3.7.3.A01 | Análisis de la interfaz con muestras reales y horarios | DAT | 4 | 80 | 01-12-2027 | 06-12-2027 | 4 | — |
| 3.7.3.A02 | Diseño del contrato, del manejo de errores y de la idempotencia | DAT | 4 | 80 | 07-12-2027 | 10-12-2027 | 4 | 3.7.3.A01 |
| 3.7.3.A03 | Construcción del adaptador, parte 1 | DAT | 2 | 80 | 13-12-2027 | 21-12-2027 | 7 | 3.7.3.A02 |
| 3.7.3.A04 | Construcción del adaptador, parte 2, con reintentos | DAT | 2 | 80 | 13-12-2027 | 21-12-2027 | 7 | 3.7.3.A02 |
| 3.7.3.A05 | Pruebas de contrato, de falla y de lentitud de la contraparte | DAT | 4 | 80 | 22-12-2027 | 27-12-2027 | 4 | 3.7.3.A03, 3.7.3.A04 |
| 3.7.3.A06 | Corrección, documentación y entrega en QA | DAT | 4 | 80 | 28-12-2027 | 31-12-2027 | 4 | 3.7.3.A05 |
| 3.7.4.A01 | Análisis de la interfaz con muestras reales y horarios | DAT | 4 | 80 | 01-12-2027 | 06-12-2027 | 4 | — |
| 3.7.4.A02 | Diseño del contrato, del manejo de errores y de la idempotencia | DAT | 4 | 80 | 07-12-2027 | 10-12-2027 | 4 | 3.7.4.A01 |
| 3.7.4.A03 | Construcción del adaptador, parte 1 | DAT | 2 | 80 | 13-12-2027 | 21-12-2027 | 7 | 3.7.4.A02 |
| 3.7.4.A04 | Construcción del adaptador, parte 2, con reintentos | DAT | 2 | 80 | 13-12-2027 | 21-12-2027 | 7 | 3.7.4.A02 |
| 3.7.4.A05 | Pruebas de contrato, de falla y de lentitud de la contraparte | DAT | 4 | 80 | 22-12-2027 | 27-12-2027 | 4 | 3.7.4.A03, 3.7.4.A04 |
| 3.7.4.A06 | Corrección, documentación y entrega en QA | DAT | 4 | 80 | 28-12-2027 | 31-12-2027 | 4 | 3.7.4.A05 |
| 3.7.5.A01 | Análisis de la interfaz con muestras reales y horarios | DAT | 5 | 80 | 03-01-2028 | 05-01-2028 | 3 | 3.7.1.A06, 3.7.2.A06, 3.7.3.A06, 3.7.4.A06 |
| 3.7.5.A02 | Diseño del contrato, del manejo de errores y de la idempotencia | DAT | 5 | 80 | 06-01-2028 | 10-01-2028 | 3 | 3.7.5.A01 |
| 3.7.5.A03 | Construcción del adaptador, parte 1 | DAT | 2 | 80 | 11-01-2028 | 19-01-2028 | 7 | 3.7.5.A02 |
| 3.7.5.A04 | Construcción del adaptador, parte 2, con reintentos | DAT | 2 | 80 | 11-01-2028 | 19-01-2028 | 7 | 3.7.5.A02 |
| 3.7.5.A05 | Pruebas de contrato, de falla y de lentitud de la contraparte | DAT | 5 | 80 | 20-01-2028 | 24-01-2028 | 3 | 3.7.5.A03, 3.7.5.A04 |
| 3.7.5.A06 | Corrección, documentación y entrega en QA | DAT | 5 | 80 | 25-01-2028 | 27-01-2028 | 3 | 3.7.5.A05 |
| 3.8.1.A01 | Preparación y ejecución de la prueba | CAL | 2 | 80 | 01-10-2027 | 11-10-2027 | 7 | 3.4.1.A12, 3.4.10.A12, 3.4.11.A12, 3.4.2.A12, 3.4.3.A12, 3.4.4.A12, 3.4.5.A12, 3.4.6.A12, 3.4.7.A12, 3.4.8.A12, 3.4.9.A12 |
| 3.8.1.A02 | Registro de defectos, regresión e informe | CAL | 2 | 80 | 12-10-2027 | 20-10-2027 | 7 | 3.8.1.A01 |
| 3.8.2.A01 | Preparación de casos, datos y ambiente de prueba | CAL | 3 | 80 | 21-10-2027 | 27-10-2027 | 5 | 3.8.1.A02 |
| 3.8.2.A02 | Ejecución de la prueba, ciclo 1 | CAL | 3 | 80 | 28-10-2027 | 03-11-2027 | 5 | 3.8.2.A01 |
| 3.8.2.A03 | Ejecución de la prueba, ciclo 2, y registro de defectos | CAL | 3 | 80 | 04-11-2027 | 10-11-2027 | 5 | 3.8.2.A02 |
| 3.8.2.A04 | Regresión e informe de resultados | CAL | 3 | 80 | 11-11-2027 | 17-11-2027 | 5 | 3.8.2.A03 |
| 3.8.3.A01 | Preparación de casos, datos y ambiente de prueba | CAL | 3 | 80 | 21-10-2027 | 27-10-2027 | 5 | 3.8.1.A02 |
| 3.8.3.A02 | Ejecución de la prueba, ciclo 1 | CAL | 3 | 80 | 28-10-2027 | 03-11-2027 | 5 | 3.8.3.A01 |
| 3.8.3.A03 | Ejecución de la prueba, ciclo 2, y registro de defectos | CAL | 3 | 80 | 04-11-2027 | 10-11-2027 | 5 | 3.8.3.A02 |
| 3.8.3.A04 | Regresión e informe de resultados | CAL | 3 | 80 | 11-11-2027 | 17-11-2027 | 5 | 3.8.3.A03 |
| 3.8.4.A01 | Preparación de casos, datos y ambiente de prueba | CAL | 2 | 80 | 01-10-2027 | 11-10-2027 | 7 | 3.4.1.A12, 3.4.10.A12, 3.4.11.A12, 3.4.2.A12, 3.4.3.A12, 3.4.4.A12, 3.4.5.A12, 3.4.6.A12, 3.4.7.A12, 3.4.8.A12, 3.4.9.A12 |
| 3.8.4.A02 | Ejecución de la prueba, ciclo 1 | CAL | 2 | 80 | 12-10-2027 | 20-10-2027 | 7 | 3.8.4.A01 |
| 3.8.4.A03 | Ejecución de la prueba, ciclo 2, y registro de defectos | CAL | 2 | 80 | 21-10-2027 | 29-10-2027 | 7 | 3.8.4.A02 |
| 3.8.4.A04 | Regresión e informe de resultados | CAL | 2 | 80 | 01-11-2027 | 09-11-2027 | 7 | 3.8.4.A03 |
| 3.8.5.A01 | Preparación de casos, datos y ambiente de prueba | CAL | 2 | 80 | 01-10-2027 | 11-10-2027 | 7 | 3.1.3.A03, 3.4.1.A12, 3.4.10.A12, 3.4.11.A12, 3.4.2.A12, 3.4.3.A12, 3.4.4.A12, 3.4.5.A12, 3.4.6.A12, 3.4.7.A12, 3.4.8.A12, 3.4.9.A12 |
| 3.8.5.A02 | Ejecución de la prueba, ciclo 1 | CAL | 2 | 80 | 12-10-2027 | 20-10-2027 | 7 | 3.8.5.A01 |
| 3.8.5.A03 | Ejecución de la prueba, ciclo 2, y registro de defectos | CAL | 2 | 80 | 21-10-2027 | 29-10-2027 | 7 | 3.8.5.A02 |
| 3.8.5.A04 | Regresión e informe de resultados | CAL | 2 | 80 | 01-11-2027 | 09-11-2027 | 7 | 3.8.5.A03 |
| 3.8.6.A01 | Preparación y ejecución de la prueba | SEG | 2 | 80 | 01-10-2027 | 11-10-2027 | 7 | 3.4.1.A12, 3.4.10.A12, 3.4.11.A12, 3.4.2.A12, 3.4.3.A12, 3.4.4.A12, 3.4.5.A12, 3.4.6.A12, 3.4.7.A12, 3.4.8.A12, 3.4.9.A12 |
| 3.8.6.A02 | Registro de defectos, regresión e informe | SEG | 2 | 80 | 12-10-2027 | 20-10-2027 | 7 | 3.8.6.A01 |
| 3.8.7.A01 | Preparación y ejecución de la prueba | CAL | 4 | 80 | 18-11-2027 | 23-11-2027 | 4 | 3.8.2.A04, 3.8.3.A04, 3.8.4.A04, 3.8.5.A04, 3.8.6.A02 |
| 3.8.7.A02 | Registro de defectos, regresión e informe | CAL | 4 | 80 | 24-11-2027 | 29-11-2027 | 4 | 3.8.7.A01 |
| 3.8.8.A01 | Preparación de casos, datos y ambiente de prueba | SRE | 2 | 80 | 01-10-2027 | 11-10-2027 | 7 | 3.4.1.A12, 3.4.10.A12, 3.4.11.A12, 3.4.2.A12, 3.4.3.A12, 3.4.4.A12, 3.4.5.A12, 3.4.6.A12, 3.4.7.A12, 3.4.8.A12, 3.4.9.A12 |
| 3.8.8.A02 | Ejecución de la prueba, ciclo 1 | SRE | 2 | 80 | 12-10-2027 | 20-10-2027 | 7 | 3.8.8.A01 |
| 3.8.8.A03 | Ejecución de la prueba, ciclo 2, y registro de defectos | SRE | 2 | 80 | 21-10-2027 | 29-10-2027 | 7 | 3.8.8.A02 |
| 3.8.8.A04 | Regresión e informe de resultados | SRE | 2 | 80 | 01-11-2027 | 09-11-2027 | 7 | 3.8.8.A03 |
| 3.9.1.A01 | Preparación y ejecución de la prueba | CAL | 2 | 80 | 01-05-2028 | 09-05-2028 | 7 | 3.5.1.A12, 3.5.2.A12, 3.5.3.A12, 3.5.4.A12 |
| 3.9.1.A02 | Registro de defectos, regresión e informe | CAL | 2 | 80 | 10-05-2028 | 18-05-2028 | 7 | 3.9.1.A01 |
| 3.9.2.A01 | Preparación de casos, datos y ambiente de prueba | CAL | 3 | 80 | 01-05-2028 | 05-05-2028 | 5 | — |
| 3.9.2.A02 | Ejecución de la prueba, ciclo 1 | CAL | 3 | 80 | 08-05-2028 | 12-05-2028 | 5 | 3.9.2.A01 |
| 3.9.2.A03 | Ejecución de la prueba, ciclo 2, y registro de defectos | CAL | 3 | 80 | 15-05-2028 | 19-05-2028 | 5 | 3.9.2.A02 |
| 3.9.2.A04 | Regresión e informe de resultados | CAL | 3 | 80 | 22-05-2028 | 26-05-2028 | 5 | 3.9.2.A03 |
| 3.9.3.A01 | Preparación de casos, datos y ambiente de prueba | CAL | 3 | 80 | 01-05-2028 | 05-05-2028 | 5 | — |
| 3.9.3.A02 | Ejecución de la prueba, ciclo 1 | CAL | 3 | 80 | 08-05-2028 | 12-05-2028 | 5 | 3.9.3.A01 |
| 3.9.3.A03 | Ejecución de la prueba, ciclo 2, y registro de defectos | CAL | 3 | 80 | 15-05-2028 | 19-05-2028 | 5 | 3.9.3.A02 |
| 3.9.3.A04 | Regresión e informe de resultados | CAL | 3 | 80 | 22-05-2028 | 26-05-2028 | 5 | 3.9.3.A03 |
| 3.9.4.A01 | Preparación de casos, datos y ambiente de prueba | CAL | 3 | 80 | 01-05-2028 | 05-05-2028 | 5 | — |
| 3.9.4.A02 | Ejecución de la prueba, ciclo 1 | CAL | 3 | 80 | 08-05-2028 | 12-05-2028 | 5 | 3.9.4.A01 |
| 3.9.4.A03 | Ejecución de la prueba, ciclo 2, y registro de defectos | CAL | 3 | 80 | 15-05-2028 | 19-05-2028 | 5 | 3.9.4.A02 |
| 3.9.4.A04 | Regresión e informe de resultados | CAL | 3 | 80 | 22-05-2028 | 26-05-2028 | 5 | 3.9.4.A03 |
| 3.9.5.A01 | Preparación de casos, datos y ambiente de prueba | SEG | 3 | 80 | 01-05-2028 | 05-05-2028 | 5 | — |
| 3.9.5.A02 | Ejecución de la prueba, ciclo 1 | SEG | 3 | 80 | 08-05-2028 | 12-05-2028 | 5 | 3.9.5.A01 |
| 3.9.5.A03 | Ejecución de la prueba, ciclo 2, y registro de defectos | SEG | 3 | 80 | 15-05-2028 | 19-05-2028 | 5 | 3.9.5.A02 |
| 3.9.5.A04 | Regresión e informe de resultados | SEG | 3 | 80 | 22-05-2028 | 26-05-2028 | 5 | 3.9.5.A03 |
| 3.9.6.A01 | Preparación y ejecución de la prueba | CAL | 4 | 80 | 29-05-2028 | 01-06-2028 | 4 | 3.9.1.A02, 3.9.2.A04, 3.9.3.A04, 3.9.4.A04, 3.9.5.A04 |
| 3.9.6.A02 | Registro de defectos, regresión e informe | CAL | 4 | 80 | 02-06-2028 | 07-06-2028 | 4 | 3.9.6.A01 |
| 3.9.7.A01 | Preparación y ejecución de la prueba | SRE | 2 | 80 | 01-05-2028 | 09-05-2028 | 7 | — |
| 3.9.7.A02 | Registro de defectos, regresión e informe | SRE | 2 | 80 | 10-05-2028 | 18-05-2028 | 7 | 3.9.7.A01 |
| 3.10.1.1.A01 | Levantamiento de insumos y análisis | DAT | 2 | 80 | 02-08-2027 | 10-08-2027 | 7 | — |
| 3.10.1.1.A02 | Elaboración del entregable | DAT | 2 | 80 | 01-09-2027 | 09-09-2027 | 7 | 3.10.1.1.A01 |
| 3.10.1.1.A03 | Revisión, corrección y presentación para aprobación | DAT | 2 | 80 | 30-09-2027 | 08-10-2027 | 7 | 3.10.1.1.A02 |
| 3.10.1.2.A01 | Levantamiento de insumos y análisis | DAT | 2 | 80 | 01-10-2027 | 11-10-2027 | 7 | — |
| 3.10.1.2.A02 | Elaboración del entregable | DAT | 2 | 80 | 21-10-2027 | 29-10-2027 | 7 | 3.10.1.2.A01 |
| 3.10.1.2.A03 | Revisión, corrección y presentación para aprobación | DAT | 2 | 80 | 11-11-2027 | 19-11-2027 | 7 | 3.10.1.2.A02 |
| 3.10.1.3.A01 | Levantamiento de insumos y análisis | DAT | 2 | 80 | 01-10-2027 | 11-10-2027 | 7 | — |
| 3.10.1.3.A02 | Elaboración del entregable | DAT | 2 | 80 | 21-10-2027 | 29-10-2027 | 7 | 3.10.1.3.A01 |
| 3.10.1.3.A03 | Revisión, corrección y presentación para aprobación | DAT | 2 | 80 | 11-11-2027 | 19-11-2027 | 7 | 3.10.1.3.A02 |
| 3.10.1.4.A01 | Levantamiento de insumos y análisis | DAT | 2 | 80 | 01-12-2027 | 09-12-2027 | 7 | — |
| 3.10.1.4.A02 | Elaboración del entregable | DAT | 2 | 80 | 20-01-2028 | 28-01-2028 | 7 | 3.10.1.4.A01 |
| 3.10.1.4.A03 | Revisión, corrección y presentación para aprobación | DAT | 2 | 80 | 10-03-2028 | 20-03-2028 | 7 | 3.10.1.4.A02 |
| 3.10.2.1.A01 | Levantamiento de insumos y análisis | CAL | 2 | 80 | 01-03-2027 | 09-03-2027 | 7 | — |
| 3.10.2.1.A02 | Elaboración del entregable | CAL | 2 | 80 | 22-03-2027 | 30-03-2027 | 7 | 3.10.2.1.A01 |
| 3.10.2.1.A03 | Revisión, corrección y presentación para aprobación | CAL | 2 | 80 | 12-04-2027 | 20-04-2027 | 7 | 3.10.2.1.A02 |
| 3.10.2.2.A01 | Levantamiento de insumos y análisis | CAL | 2 | 80 | 01-04-2027 | 09-04-2027 | 7 | — |
| 3.10.2.2.A02 | Elaboración del entregable | CAL | 2 | 80 | 03-05-2027 | 11-05-2027 | 7 | 3.10.2.2.A01 |
| 3.10.2.2.A03 | Revisión, corrección y presentación para aprobación | CAL | 2 | 80 | 01-06-2027 | 09-06-2027 | 7 | 3.10.2.2.A02 |
| 3.10.2.3.A01 | Levantamiento de insumos y análisis | CAL | 2 | 80 | 01-06-2027 | 09-06-2027 | 7 | — |
| 3.10.2.3.A02 | Elaboración del entregable | CAL | 2 | 80 | 02-08-2027 | 10-08-2027 | 7 | 3.10.2.3.A01 |
| 3.10.2.3.A03 | Revisión, corrección y presentación para aprobación | CAL | 2 | 80 | 30-09-2027 | 08-10-2027 | 7 | 3.10.2.3.A02 |
| 3.10.2.4.A01 | Levantamiento de insumos y análisis | CAL | 2 | 80 | 01-12-2027 | 09-12-2027 | 7 | — |
| 3.10.2.4.A02 | Elaboración del entregable | CAL | 2 | 80 | 20-01-2028 | 28-01-2028 | 7 | 3.10.2.4.A01 |
| 3.10.2.4.A03 | Revisión, corrección y presentación para aprobación | CAL | 2 | 80 | 10-03-2028 | 20-03-2028 | 7 | 3.10.2.4.A02 |
| 3.10.3.1.A01 | Levantamiento de insumos y análisis | DAT | 2 | 80 | 01-04-2027 | 09-04-2027 | 7 | — |
| 3.10.3.1.A02 | Elaboración del entregable | DAT | 2 | 80 | 03-05-2027 | 11-05-2027 | 7 | 3.10.3.1.A01 |
| 3.10.3.1.A03 | Revisión, corrección y presentación para aprobación | DAT | 2 | 80 | 01-06-2027 | 09-06-2027 | 7 | 3.10.3.1.A02 |
| 3.10.3.2.A01 | Levantamiento de insumos y análisis | DAT | 2 | 80 | 01-06-2027 | 09-06-2027 | 7 | — |
| 3.10.3.2.A02 | Elaboración del entregable | DAT | 2 | 80 | 21-07-2027 | 29-07-2027 | 7 | 3.10.3.2.A01 |
| 3.10.3.2.A03 | Revisión, corrección y presentación para aprobación | DAT | 2 | 80 | 10-09-2027 | 20-09-2027 | 7 | 3.10.3.2.A02 |
| 3.10.3.3.A01 | Levantamiento de insumos y análisis | DAT | 2 | 80 | 01-10-2027 | 11-10-2027 | 7 | — |
| 3.10.3.3.A02 | Elaboración del entregable | DAT | 2 | 80 | 21-10-2027 | 29-10-2027 | 7 | 3.10.3.3.A01 |
| 3.10.3.3.A03 | Revisión, corrección y presentación para aprobación | DAT | 2 | 80 | 11-11-2027 | 19-11-2027 | 7 | 3.10.3.3.A02 |
| 3.10.3.4.A01 | Levantamiento de insumos y análisis | DAT | 2 | 80 | 01-12-2027 | 09-12-2027 | 7 | — |
| 3.10.3.4.A02 | Elaboración del entregable | DAT | 2 | 80 | 20-01-2028 | 28-01-2028 | 7 | 3.10.3.4.A01 |
| 3.10.3.4.A03 | Revisión, corrección y presentación para aprobación | DAT | 2 | 80 | 10-03-2028 | 20-03-2028 | 7 | 3.10.3.4.A02 |
| 3.10.4.1.A01 | Levantamiento de insumos y análisis | IMP | 2 | 80 | 01-02-2028 | 09-02-2028 | 7 | — |
| 3.10.4.1.A02 | Elaboración del entregable | IMP | 2 | 80 | 22-02-2028 | 01-03-2028 | 7 | 3.10.4.1.A01 |
| 3.10.4.1.A03 | Revisión, corrección y presentación para aprobación | IMP | 2 | 80 | 13-03-2028 | 21-03-2028 | 7 | 3.10.4.1.A02 |
| 3.10.4.2.A01 | Levantamiento de insumos y análisis | IMP | 2 | 80 | 01-03-2028 | 09-03-2028 | 7 | — |
| 3.10.4.2.A02 | Elaboración del entregable | IMP | 2 | 80 | 21-03-2028 | 29-03-2028 | 7 | 3.10.4.2.A01 |
| 3.10.4.2.A03 | Revisión, corrección y presentación para aprobación | IMP | 2 | 80 | 11-04-2028 | 19-04-2028 | 7 | 3.10.4.2.A02 |
| 3.10.4.3.A01 | Levantamiento de insumos y análisis | IMP | 2 | 80 | 03-04-2028 | 11-04-2028 | 7 | — |
| 3.10.4.3.A02 | Elaboración del entregable | IMP | 2 | 80 | 03-05-2028 | 11-05-2028 | 7 | 3.10.4.3.A01 |
| 3.10.4.3.A03 | Revisión, corrección y presentación para aprobación | IMP | 2 | 80 | 01-06-2028 | 09-06-2028 | 7 | 3.10.4.3.A02 |
| 3.10.4.4.A01 | Levantamiento de insumos y análisis | IMP | 2 | 80 | 03-07-2028 | 11-07-2028 | 7 | — |
| 3.10.4.4.A02 | Elaboración del entregable | IMP | 2 | 80 | 11-08-2028 | 21-08-2028 | 7 | 3.10.4.4.A01 |
| 3.10.4.4.A03 | Revisión, corrección y presentación para aprobación | IMP | 2 | 80 | 21-09-2028 | 29-09-2028 | 7 | 3.10.4.4.A02 |
| 4.1.1.A01 | Elaboración, revisión y aprobación del entregable | IMP | 2 | 80 | 01-11-2027 | 09-11-2027 | 7 | — |
| 4.1.2.A01 | Elaboración, revisión y aprobación del entregable | IMP | 2 | 80 | 01-12-2027 | 09-12-2027 | 7 | — |
| 4.1.3.A01 | Elaboración, revisión y aprobación del entregable | IMP | 2 | 80 | 01-06-2028 | 09-06-2028 | 7 | — |
| 4.2.3.A01 | Elaboración, revisión y aprobación del entregable | JP | 2 | 80 | 04-05-2028 | 12-05-2028 | 7 | 7.3.1.A02 |
| 4.3.3.A01 | Elaboración, revisión y aprobación del entregable | JP | 2 | 80 | 11-10-2028 | 19-10-2028 | 7 | 4.3.4.A01, 7.1.4.A02, 7.3.2.A02 |
| 4.3.4.A01 | Elaboración, revisión y aprobación del entregable | JP | 2 | 80 | 02-10-2028 | 10-10-2028 | 7 | — |
| 5.1.1.A01 | Elaboración, revisión y aprobación del entregable | ARQ | 2 | 80 | 01-03-2027 | 09-03-2027 | 7 | — |
| 5.1.2.A01 | Elaboración, revisión y aprobación del entregable | ARQ | 2 | 80 | 02-03-2027 | 10-03-2027 | 7 | 2.3.1.A03, 2.3.2.A03 |
| 5.1.3.A01 | Elaboración, revisión y aprobación del entregable | SRE | 2 | 80 | 01-06-2027 | 09-06-2027 | 7 | — |
| 5.2.1.A01 | Elaboración, revisión y aprobación del entregable | SRE | 2 | 80 | 01-03-2027 | 09-03-2027 | 7 | — |
| 5.2.2.A01 | Elaboración, revisión y aprobación del entregable | SRE | 2 | 80 | 03-05-2027 | 11-05-2027 | 7 | — |
| 5.2.3.A01 | Elaboración, revisión y aprobación del entregable | ARQ | 2 | 80 | 03-05-2027 | 11-05-2027 | 7 | — |
| 5.3.1.A01 | Elaboración, revisión y aprobación del entregable | SRE | 2 | 80 | 03-05-2027 | 11-05-2027 | 7 | — |
| 5.3.2.A01 | Elaboración, revisión y aprobación del entregable | SRE | 2 | 80 | 03-05-2027 | 11-05-2027 | 7 | — |
| 5.3.3.A01 | Elaboración, revisión y aprobación del entregable | SRE | 2 | 80 | 03-05-2027 | 11-05-2027 | 7 | — |
| 5.4.1.A01 | Elaboración, revisión y aprobación del entregable | IMP | 2 | 80 | 01-10-2027 | 11-10-2027 | 7 | — |
| 5.4.2.A01 | Elaboración, revisión y aprobación del entregable | IMP | 2 | 80 | 01-10-2027 | 11-10-2027 | 7 | — |
| 5.4.3.A01 | Elaboración, revisión y aprobación del entregable | JP | 2 | 80 | 01-06-2028 | 09-06-2028 | 7 | — |
| 5.4.4.A01 | Elaboración, revisión y aprobación del entregable | JP | 2 | 80 | 02-08-2027 | 10-08-2027 | 7 | — |
| 6.1.1.A01 | Preparación y ejecución de la instalación o de la capacitación | SRE | 2 | 80 | 01-04-2027 | 09-04-2027 | 7 | 5.1.2.A01 |
| 6.1.1.A02 | Prueba o evaluación, corrección y acta | SRE | 2 | 80 | 12-04-2027 | 20-04-2027 | 7 | 6.1.1.A01 |
| 6.1.2.A01 | Preparación y ejecución de la instalación o de la capacitación | SRE | 2 | 80 | 01-04-2027 | 09-04-2027 | 7 | 5.1.2.A01 |
| 6.1.2.A02 | Prueba o evaluación, corrección y acta | SRE | 2 | 80 | 12-04-2027 | 20-04-2027 | 7 | 6.1.2.A01 |
| 6.1.3.A01 | Preparación y ejecución de la instalación o de la capacitación | SRE | 2 | 80 | 01-04-2027 | 09-04-2027 | 7 | 5.1.2.A01 |
| 6.1.3.A02 | Prueba o evaluación, corrección y acta | SRE | 2 | 80 | 12-04-2027 | 20-04-2027 | 7 | 6.1.3.A01 |
| 6.1.4.A01 | Preparación y ejecución de la instalación o de la capacitación | SRE | 2 | 80 | 01-04-2027 | 09-04-2027 | 7 | 5.1.2.A01 |
| 6.1.4.A02 | Prueba o evaluación, corrección y acta | SRE | 2 | 80 | 12-04-2027 | 20-04-2027 | 7 | 6.1.4.A01 |
| 6.1.5.A01 | Preparación y ejecución de la instalación o de la capacitación | SRE | 2 | 80 | 03-05-2027 | 11-05-2027 | 7 | 5.1.2.A01 |
| 6.1.5.A02 | Prueba o evaluación, corrección y acta | SRE | 2 | 80 | 12-05-2027 | 20-05-2027 | 7 | 6.1.5.A01 |
| 6.2.1.A01 | Preparación y ejecución de la instalación o de la capacitación | SRE | 2 | 80 | 03-05-2027 | 11-05-2027 | 7 | — |
| 6.2.1.A02 | Prueba o evaluación, corrección y acta | SRE | 2 | 80 | 12-05-2027 | 20-05-2027 | 7 | 6.2.1.A01 |
| 6.2.2.A01 | Preparación y ejecución de la instalación o de la capacitación | SRE | 2 | 80 | 01-07-2027 | 09-07-2027 | 7 | — |
| 6.2.2.A02 | Prueba o evaluación, corrección y acta | SRE | 2 | 80 | 12-07-2027 | 20-07-2027 | 7 | 6.2.2.A01 |
| 6.2.3.A01 | Preparación y ejecución de la instalación o de la capacitación | SRE | 2 | 80 | 02-08-2027 | 10-08-2027 | 7 | — |
| 6.2.3.A02 | Prueba o evaluación, corrección y acta | SRE | 2 | 80 | 11-08-2027 | 19-08-2027 | 7 | 6.2.3.A01 |
| 6.3.1.A01 | Preparación y ejecución de la instalación o de la capacitación | SRE | 2 | 80 | 21-05-2027 | 31-05-2027 | 7 | 6.1.5.A02 |
| 6.3.1.A02 | Prueba o evaluación, corrección y acta | SRE | 2 | 80 | 01-06-2027 | 09-06-2027 | 7 | 6.3.1.A01 |
| 6.3.2.A01 | Preparación y ejecución de la instalación o de la capacitación | SRE | 2 | 80 | 21-05-2027 | 31-05-2027 | 7 | 6.1.5.A02 |
| 6.3.2.A02 | Prueba o evaluación, corrección y acta | SRE | 2 | 80 | 01-06-2027 | 09-06-2027 | 7 | 6.3.2.A01 |
| 6.3.3.A01 | Preparación y ejecución de la instalación o de la capacitación | SRE | 2 | 80 | 03-05-2027 | 11-05-2027 | 7 | — |
| 6.3.3.A02 | Prueba o evaluación, corrección y acta | SRE | 2 | 80 | 12-05-2027 | 20-05-2027 | 7 | 6.3.3.A01 |
| 6.3.4.A01 | Preparación y ejecución de la instalación o de la capacitación | SRE | 2 | 80 | 01-10-2027 | 11-10-2027 | 7 | — |
| 6.3.4.A02 | Prueba o evaluación, corrección y acta | SRE | 2 | 80 | 12-10-2027 | 20-10-2027 | 7 | 6.3.4.A01 |
| 6.4.1.A01 | Preparación y ejecución de la instalación o de la capacitación | SEG | 2 | 80 | 01-06-2027 | 09-06-2027 | 7 | — |
| 6.4.1.A02 | Prueba o evaluación, corrección y acta | SEG | 2 | 80 | 10-06-2027 | 18-06-2027 | 7 | 6.4.1.A01 |
| 6.4.2.A01 | Preparación y ejecución de la instalación o de la capacitación | SEG | 2 | 80 | 01-06-2027 | 09-06-2027 | 7 | — |
| 6.4.2.A02 | Prueba o evaluación, corrección y acta | SEG | 2 | 80 | 10-06-2027 | 18-06-2027 | 7 | 6.4.2.A01 |
| 6.4.3.A01 | Preparación y ejecución de la instalación o de la capacitación | SEG | 2 | 80 | 21-06-2027 | 29-06-2027 | 7 | — |
| 6.4.3.A02 | Prueba o evaluación, corrección y acta | SEG | 2 | 80 | 30-06-2027 | 08-07-2027 | 7 | 6.4.3.A01 |
| 6.5.1.A01 | Preparación y ejecución de la instalación o de la capacitación | SRE | 2 | 80 | 01-10-2027 | 11-10-2027 | 7 | 3.2.6.A03 |
| 6.5.1.A02 | Prueba o evaluación, corrección y acta | SRE | 2 | 80 | 02-12-2027 | 10-12-2027 | 7 | 6.5.1.A01 |
| 6.5.2.A01 | Preparación y ejecución de la instalación o de la capacitación | SRE | 2 | 80 | 01-11-2027 | 09-11-2027 | 7 | — |
| 6.5.2.A02 | Prueba o evaluación, corrección y acta | SRE | 2 | 80 | 16-12-2027 | 24-12-2027 | 7 | 6.5.2.A01 |
| 6.5.3.A01 | Preparación y ejecución de la instalación o de la capacitación | SRE | 2 | 80 | 01-10-2027 | 11-10-2027 | 7 | — |
| 6.5.3.A02 | Prueba o evaluación, corrección y acta | SRE | 2 | 80 | 17-11-2027 | 25-11-2027 | 7 | 6.5.3.A01 |
| 6.5.4.A01 | Preparación y ejecución de la instalación o de la capacitación | SRE | 2 | 80 | 01-11-2027 | 09-11-2027 | 7 | — |
| 6.5.4.A02 | Prueba o evaluación, corrección y acta | SRE | 2 | 80 | 16-12-2027 | 24-12-2027 | 7 | 6.5.4.A01 |
| 6.5.5.A01 | Preparación y ejecución de la instalación o de la capacitación | SRE | 2 | 80 | 01-11-2027 | 09-11-2027 | 7 | — |
| 6.5.5.A02 | Prueba o evaluación, corrección y acta | SRE | 2 | 80 | 16-12-2027 | 24-12-2027 | 7 | 6.5.5.A01 |
| 6.5.6.A01 | Preparación y ejecución de la instalación o de la capacitación | SRE | 2 | 80 | 01-10-2027 | 11-10-2027 | 7 | — |
| 6.5.6.A02 | Prueba o evaluación, corrección y acta | SRE | 2 | 80 | 02-12-2027 | 10-12-2027 | 7 | 6.5.6.A01 |
| 6.6.1.A01 | Preparación y ejecución de la instalación o de la capacitación | SRE | 2 | 80 | 10-06-2027 | 18-06-2027 | 7 | 6.3.1.A02, 6.3.2.A02, 6.3.3.A02 |
| 6.6.1.A02 | Prueba o evaluación, corrección y acta | SRE | 2 | 80 | 21-06-2027 | 29-06-2027 | 7 | 6.6.1.A01 |
| 6.6.2.A01 | Preparación y ejecución de la instalación o de la capacitación | SRE | 2 | 80 | 10-06-2027 | 18-06-2027 | 7 | 6.3.1.A02, 6.3.2.A02, 6.3.3.A02 |
| 6.6.2.A02 | Prueba o evaluación, corrección y acta | SRE | 2 | 80 | 21-06-2027 | 29-06-2027 | 7 | 6.6.2.A01 |
| 6.6.3.A01 | Preparación y ejecución de la instalación o de la capacitación | SRE | 4 | 80 | 10-06-2027 | 15-06-2027 | 4 | 6.3.1.A02, 6.3.2.A02, 6.3.3.A02 |
| 6.6.3.A02 | Prueba o evaluación, corrección y acta | SRE | 4 | 80 | 16-06-2027 | 21-06-2027 | 4 | 6.6.3.A01 |
| 7.1.1.A01 | Preparación y ejecución de la instalación o de la capacitación | IMP | 2 | 80 | 01-11-2027 | 09-11-2027 | 7 | — |
| 7.1.1.A02 | Prueba o evaluación, corrección y acta | IMP | 2 | 80 | 16-12-2027 | 24-12-2027 | 7 | 7.1.1.A01 |
| 7.1.6.A01 | Preparación y ejecución de la instalación o de la capacitación | IMP | 2 | 80 | 01-11-2027 | 09-11-2027 | 7 | — |
| 7.1.6.A02 | Prueba o evaluación, corrección y acta | IMP | 2 | 80 | 16-12-2027 | 24-12-2027 | 7 | 7.1.6.A01 |
| 7.2.2.A01 | Preparación y ejecución de la instalación o de la capacitación | IMP | 2 | 80 | 01-05-2028 | 09-05-2028 | 7 | — |
| 7.2.2.A02 | Prueba o evaluación, corrección y acta | IMP | 2 | 80 | 15-06-2028 | 23-06-2028 | 7 | 7.2.2.A01 |
| 7.2.3.A01 | Preparación y ejecución de la instalación o de la capacitación | IMP | 2 | 80 | 01-03-2027 | 09-03-2027 | 7 | — |
| 7.2.3.A02 | Prueba o evaluación, corrección y acta | IMP | 2 | 80 | 17-05-2027 | 25-05-2027 | 7 | 7.2.3.A01 |
| 7.3.1.A01 | Preparación y ejecución de la instalación o de la capacitación | IMP | 2 | 80 | 01-02-2028 | 09-02-2028 | 7 | — |
| 7.3.1.A02 | Prueba o evaluación, corrección y acta | IMP | 2 | 80 | 16-03-2028 | 24-03-2028 | 7 | 7.3.1.A01 |
| 7.3.2.A01 | Preparación y ejecución de la instalación o de la capacitación | IMP | 2 | 80 | 03-07-2028 | 11-07-2028 | 7 | — |
| 7.3.2.A02 | Prueba o evaluación, corrección y acta | IMP | 2 | 80 | 17-07-2028 | 25-07-2028 | 7 | 7.3.2.A01 |
| 9.1.1.A01 | Elaboración, revisión y aprobación del entregable | DES | 2 | 80 | 02-10-2028 | 10-10-2028 | 7 | — |
| 9.1.2.A01 | Elaboración, revisión y aprobación del entregable | JP | 2 | 80 | 02-10-2028 | 10-10-2028 | 7 | — |
| 9.2.2.A01 | Elaboración, revisión y aprobación del entregable | SEG | 2 | 80 | 01-09-2031 | 09-09-2031 | 7 | — |

### 6.2 Paquetes de esfuerzo continuo

Los paquetes recurrentes (R), de acompañamiento (A) y de cobertura (C) son de nivel de esfuerzo: no producen un entregable único, sino un servicio o una reunión que se repite. No se dividen en entregables más pequeños, sino por ocurrencia o por quincena:

- Un paquete con frecuencia propia en el diccionario del T-14 (quincenal, mensual, trimestral, semestral o anual) tiene una actividad por ocurrencia, ejecutada dentro de una quincena. Si una ocurrencia supera 64 HH, se reparte entre dos o más personas.
- Un paquete continuo tiene una actividad por quincena. Si la quincena exige más de 64 HH, la actividad se divide en relevos o puestos: por ejemplo, el NOC 24×7 de un mes de 31 días requiere 744 ÷ 2 = 372 HH por quincena, es decir, seis relevos de 62 HH.
- Las preparaciones de comités con frecuencia contractual quincenal (1.6.2 y 1.8.3) tienen menos de 8 HH por ocurrencia. Son la única excepción al mínimo de la regla: se mantienen por ocurrencia porque la cadencia la fija el Art. 71° y no conviene fusionarlas con otra actividad.

Estos 59 paquetes no se descomponen en una lista de actividades distintas, porque su trabajo se repite: se programan por quincena u ocurrencia, en relevos de hasta 64 HH cada uno. La Tabla 6.2 presenta la regla de cada paquete, el número de relevos u ocurrencias que programa durante el contrato y el esfuerzo máximo de cada uno.

**Tabla 6.2 — Actividades de los paquetes de esfuerzo continuo. Fuente: elaboración propia a partir de las secciones 4.1, 4.2 y 4.4 y del diccionario del Formulario T-14.**

| Paquete | Clase | Rol | Meses | E HH | Regla de programación | Relevos u ocurrencias programados | HH máximas por relevo u ocurrencia |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.2.2 | G | IMP | 1–3 | 80 | Una actividad por quincena, por presencia continua o periódica | 6 | 13.3 |
| 1.3.5 | R | JP | 1–20 | 480 | Una actividad de nivel de esfuerzo por quincena | 40 | 12.0 |
| 1.4.3 | R | JP | 1–56 | 896 | Una actividad de nivel de esfuerzo por quincena | 112 | 8.0 |
| 1.5.2 | G | CAL | 6–20 | 80 | Una actividad cada 3 quincenas, por presencia continua o periódica | 10 | 8.0 |
| 1.6.2 | R | JP | 1–20 | 160 | Una actividad por ocurrencia (quincenal, en cada Comité de Proyecto), ejecutada dentro de una quincena; 1 actividad(es) por ocurrencia | 40 | 4.0 |
| 1.8.1 | R | JP | 1–20 | 320 | Una actividad de nivel de esfuerzo por quincena | 40 | 8.0 |
| 1.8.2 | R | JP | 1–56 | 448 | Una actividad por ocurrencia (mensual), ejecutada dentro de una quincena; 1 actividad(es) por ocurrencia | 56 | 8.0 |
| 1.8.3 | R | JP | 1–20 | 240 | Una actividad por ocurrencia (quincenal), ejecutada dentro de una quincena; 1 actividad(es) por ocurrencia | 40 | 6.0 |
| 1.8.4 | R | ARQ | 1–56 | 448 | Una actividad por ocurrencia (mensual), ejecutada dentro de una quincena; 1 actividad(es) por ocurrencia | 56 | 8.0 |
| 1.8.5 | R | SRE | 13–56 | 352 | Una actividad por ocurrencia (mensual), ejecutada dentro de una quincena; 1 actividad(es) por ocurrencia | 44 | 8.0 |
| 1.8.6 | R | JP | 1–20 | 480 | Una actividad por ocurrencia (mensual), ejecutada dentro de una quincena; 1 actividad(es) por ocurrencia | 20 | 24.0 |
| 1.8.7 | R | JP | 2–56 | 440 | Una actividad cada 2 quincenas, ejecutada en la última quincena del grupo | 55 | 8.0 |
| 1.8.8 | R | JP | 1–56 | 448 | Una actividad cada 2 quincenas, ejecutada en la última quincena del grupo | 56 | 8.0 |
| 1.9.4 | R | SEG | 1–56 | 224 | Una actividad por ocurrencia (anual), ejecutada dentro de una quincena; 1 actividad(es) por ocurrencia | 5 | 44.8 |
| 1.9.5 | R | JP | 1–56 | 224 | Una actividad cada 4 quincenas, ejecutada en la última quincena del grupo | 28 | 8.0 |
| 2.2.2 | E | SEG | 3–10 | 240 | Una actividad por quincena, por presencia continua o periódica | 16 | 15.0 |
| 3.11.1 | G | ARQ | 15–21 | 80 | Una actividad cada 2 quincenas, por presencia continua o periódica | 7 | 11.4 |
| 3.11.2 | G | SRE | 10–20 | 80 | Una actividad cada 3 quincenas, por presencia continua o periódica | 8 | 10.0 |
| 3.11.3 | G | DES | 4–20 | 80 | Una actividad cada 4 quincenas, por presencia continua o periódica | 9 | 8.9 |
| 3.11.4 | G | DES | 4–20 | 80 | Una actividad cada 4 quincenas, por presencia continua o periódica | 9 | 8.9 |
| 3.11.5 | G | DES | 6–20 | 80 | Una actividad cada 3 quincenas, por presencia continua o periódica | 10 | 8.0 |
| 4.2.1 | A | IMP | 13–15 | 7392 | Una actividad de nivel de esfuerzo por quincena, dividida en 20 relevos o puestos | 120 | 61.6 |
| 4.2.2 | A | IMP | 16–20 | 5408 | Una actividad de nivel de esfuerzo por quincena, dividida en relevos o puestos según la HH de cada mes | 92 | 61.6 |
| 4.3.1 | A | IMP | 19–20 | 4928 | Una actividad de nivel de esfuerzo por quincena, dividida en 20 relevos o puestos | 80 | 61.6 |
| 4.3.2 | A | IMP | 21–22 | 2464 | Una actividad de nivel de esfuerzo por quincena, dividida en relevos o puestos según la HH de cada mes | 40 | 62.1 |
| 7.1.2 | R | IMP | 13–56 | 2816 | Una actividad de nivel de esfuerzo por quincena | 88 | 32.0 |
| 7.1.3 | T | IMP | 13–20 | 160 | Una actividad por quincena, por presencia continua o periódica | 16 | 10.0 |
| 7.1.4 | T | IMP | 15–20 | 160 | 2 ocurrencias en la ventana, por presencia continua o periódica | 2 | 80.0 |
| 7.1.5 | T | IMP | 10–18 | 160 | 2 ocurrencias en la ventana, por presencia continua o periódica | 2 | 80.0 |
| 7.2.1 | T | IMP | 10–16 | 160 | Una actividad por quincena, por presencia continua o periódica | 14 | 11.4 |
| 7.2.4 | T | IMP | 11–20 | 160 | Una actividad por quincena, por presencia continua o periódica | 20 | 8.0 |
| 7.2.5 | T | IMP | 13–21 | 160 | Una actividad por quincena, por presencia continua o periódica | 18 | 8.9 |
| 8.1.1 | C | SRE | 21–56 | 26280 | Una actividad de nivel de esfuerzo por quincena, dividida en relevos o puestos según la HH de cada mes | 432 | 62.0 |
| 8.1.2 | C | SRE | 21–56 | 40078 | Una actividad de nivel de esfuerzo por quincena, dividida en relevos o puestos según la HH de cada mes | 666 | 61.5 |
| 8.1.3 | G | SRE | 21–56 | 80 | 6 ocurrencias en la ventana, por presencia continua o periódica | 6 | 13.3 |
| 8.1.4 | R | JP | 21–56 | 288 | Una actividad por ocurrencia (anual), ejecutada dentro de una quincena; 2 actividad(es) por ocurrencia | 6 | 48.0 |
| 8.1.5 | C | SEG | 13–56 | 32112 | Una actividad de nivel de esfuerzo por quincena, dividida en relevos o puestos según la HH de cada mes | 528 | 62.0 |
| 8.1.6 | R | SRE | 21–56 | 576 | Una actividad por ocurrencia (mensual), ejecutada dentro de una quincena; 1 actividad(es) por ocurrencia | 36 | 16.0 |
| 8.2.1 | R | DES | 21–56 | 4608 | Una actividad de nivel de esfuerzo por quincena | 72 | 64.0 |
| 8.2.2 | R | SEG | 21–56 | 1152 | Una actividad de nivel de esfuerzo por quincena | 72 | 16.0 |
| 8.2.3 | R | SRE | 21–56 | 1152 | Una actividad de nivel de esfuerzo por quincena | 72 | 16.0 |
| 8.2.4 | R | DES | 21–56 | 2304 | Una actividad de nivel de esfuerzo por quincena | 72 | 32.0 |
| 8.2.5 | R | SRE | 21–56 | 288 | Una actividad por ocurrencia (anual), ejecutada dentro de una quincena; 2 actividad(es) por ocurrencia | 6 | 48.0 |
| 8.2.6 | R | SRE | 21–56 | 288 | Una actividad por ocurrencia (semestral), ejecutada dentro de una quincena; 1 actividad(es) por ocurrencia | 6 | 48.0 |
| 8.2.7 | R | SRE | 21–56 | 864 | Una actividad de nivel de esfuerzo por quincena | 72 | 12.0 |
| 8.3.1 | R | CAL | 21–56 | 576 | Una actividad de nivel de esfuerzo por quincena | 72 | 8.0 |
| 8.3.2 | R | DAT | 21–56 | 288 | Una actividad por ocurrencia (semestral), ejecutada dentro de una quincena; 1 actividad(es) por ocurrencia | 6 | 48.0 |
| 8.3.3 | G | JP | 21–23 | 80 | 3 ocurrencias en la ventana, por presencia continua o periódica | 3 | 26.7 |
| 8.3.4 | R | JP | 24–56 | 528 | Una actividad por ocurrencia (mensual), ejecutada dentro de una quincena; 1 actividad(es) por ocurrencia | 33 | 16.0 |
| 8.3.5 | G | IMP | 22–26 | 80 | Una actividad por quincena, por presencia continua o periódica | 10 | 8.0 |
| 8.3.6 | G | IMP | 24–27 | 80 | Una actividad por quincena, por presencia continua o periódica | 8 | 10.0 |
| 8.4.1 | R | SRE | 21–56 | 576 | Una actividad por ocurrencia (trimestral), ejecutada dentro de una quincena; 1 actividad(es) por ocurrencia | 12 | 48.0 |
| 8.4.2 | R | SRE | 21–56 | 576 | Una actividad por ocurrencia (mensual), ejecutada dentro de una quincena; 1 actividad(es) por ocurrencia | 36 | 16.0 |
| 8.4.3 | R | SRE | 21–56 | 288 | Una actividad por ocurrencia (anual), ejecutada dentro de una quincena; 2 actividad(es) por ocurrencia | 6 | 48.0 |
| 8.4.4 | R | JP | 21–56 | 288 | Una actividad por ocurrencia (semestral), ejecutada dentro de una quincena; 1 actividad(es) por ocurrencia | 6 | 48.0 |
| 8.5.1 | R | IMP | 21–56 | 1152 | Una actividad por ocurrencia (dos jornadas por año), ejecutada dentro de una quincena; 3 actividad(es) por ocurrencia | 18 | 64.0 |
| 8.5.2 | G | IMP | 21–27 | 80 | Una actividad cada 2 quincenas, por presencia continua o periódica | 7 | 11.4 |
| 8.5.3 | R | SRE | 21–56 | 576 | Una actividad de nivel de esfuerzo por quincena | 72 | 8.0 |
| 9.2.1 | G | JP | 54–56 | 80 | Una actividad por quincena, por presencia continua o periódica | 6 | 13.3 |

Así, los 222 paquetes quedan programados de dos formas: 564 actividades definidas para los 163 paquetes con entregable, cada una de 80 HH o menos, y 59 paquetes de esfuerzo continuo que se programan por quincena u ocurrencia, en relevos de hasta 64 HH cada uno. En ambos casos nada supera una quincena. Ningún paquete se informa al 50 % durante semanas: el avance de cada quincena se mide por las actividades terminadas y por los relevos u ocurrencias cumplidos, que alimentan el valor ganado del SD6, sección 6.1.5.

## Referencias

Las fuentes de método citadas en este formulario son las siguientes.

  
-  Malcolm, D. G., Roseboom, J. H., Clark, C. E., & Fazar, W. (1959). Application of a technique for research and development program evaluation. *Operations Research, 7*(5), 646–669.
  
-  Project Management Institute. (2017). *La guía de los fundamentos para la dirección de proyectos (Guía del PMBOK®)* (6.ª ed.). Project Management Institute.

## Declaración de uso de IA

En cumplimiento de la sección 7.2 de las Aclaraciones de la licitación, la tabla siguiente declara el uso de herramientas de inteligencia artificial en este formulario, con la revisión humana de cada parte. La declaración se consolida en el Formulario A-6.

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
| --- | --- | --- | --- | --- | --- |
| 1 a 3 | Claude Code; Codex | Redacción del método, ruta crítica y frentes | Alto | Alto (descripciones de figuras) | [[REVISIÓN HUMANA]] |
| 4 Modelo de recursos | Codex; Claude Code | Cálculo de HH, curvas, calendario real y cobertura de mesa/SOC | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 6 Lista de actividades | Claude Code | Descomposición de los 222 paquetes en actividades con la regla del 8/80 y del período de reporte | Alto | Ninguno | [[REVISIÓN HUMANA]] |
| 5 Red, PERT y dotación | Claude Code | Red con revisiones Art. 18.3, PERT de duración, medición de atención y comparación con la dotación declarada | Alto | Ninguno | [[REVISIÓN HUMANA]] |
