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

La duración deberá contrastarse con esfuerzo, capacidad efectiva y dependencias. Las ventanas de la sección 4 son supuestos; la red agregada de la sección 5 explicita un cálculo provisional de calendario. Las dependencias entre paquetes están en el Anexo 7.B del Subdocumento 7, y sobre esa red se aplica el método de la ruta crítica (PMI, 2017, pp. 210–211): una pasada hacia adelante da el inicio y el fin tempranos; una pasada hacia atrás, desde los meses fijos del Art. 17°, da el inicio y el fin tardíos; la diferencia LS − ES es la holgura total; la holgura libre se calcula respecto del ES de sus sucesores. Los hitos del Formulario E-25 son restricciones de fecha fija: un camino que no llega a su hito tiene holgura negativa y obliga a replanificar.

La sección 5 incorpora las revisiones del CLIENTE (Art. 18.3) como retardos, calcula el PERT de duración por camino con su desviación y probabilidad de cumplir cada hito, y añade escenarios deterministas de demora. La probabilidad por camino no se presenta como probabilidad de cumplir todo el proyecto. La nivelación ajusta el inicio de los paquetes con holgura para que ningún rol supere su dotación disponible (PMI, 2017, pp. 211–212); los paquetes de la ruta crítica no se mueven.

## 2 Ruta crítica y holguras

La cadena crítica nace en las interfaces del sistema de gestión sin documentación (Caso 02, sección 17.5): 1.2.3 Especificación de las interfaces, 3.3.2 Integración con el ERP, 3.4 Módulos de la Etapa 1, 3.8.1 Pruebas de integración (H4, mes 10), 3.8.2 a 3.8.6 Pruebas de certificación, 3.8.7 Certificación (H5, mes 12), 4.2.1 Marcha blanca (H6, mes 13) y 4.2.3 Paso a producción (H7, mes 16). La Figura «fig:T15-ruta» la presenta junto con los caminos casi críticos.

  
  **Descripción textual de figura.** No sustituye la revisión visual del PDF.
- Caminos casi críticos
- 5.1.2 y 6.1 a 6.6 terminan en el H3
- Marcha / blanca E1
- Marcha / blanca E2
  
**Figura: Ruta crítica identificada y caminos casi críticos de la implementación. Fuente: elaboración propia a partir del Anexo 7.B del Subdocumento 7 y de los períodos del Formulario T-14.**

  <a id="fig:T15-ruta"></a>

La figura identifica cadenas de riesgo, pero no permite concluir holgura cero por coincidencia de meses. La sección 5 calcula holguras en una red agregada provisional y declara sus límites. Los caminos casi críticos son la sala técnica (2.3.1, 5.1.2, 6.1, 6.3 y 6.6.3), que llega al H3 del mes 6; la captura de las reglas de ruteo del planificador (1.2.2 y 3.4.7 M4 Rutas), antes de su jubilación; los acuerdos con los diez transportistas y con el sindicato (5.4.1 y 5.4.2), antes de la ola de reparto; y la certificación del intercambio electrónico con las cadenas (3.6.5 y 3.6.6), antes del mes 21.

La holgura se gestiona en las instancias de gobierno de la EDT: el avance de la ruta crítica y de los caminos casi críticos se revisa en la reunión semanal y en el Comité de Proyecto quincenal (paquetes 1.3.5 y 1.8.3); toda desviación que comprometa un hito se escala al Comité Ejecutivo con su análisis de impacto (paquetes 1.4.3 y 1.8.2); y el informe mensual con valor ganado avisa toda desviación mayor al 10 % con su plan dentro de cinco días hábiles (paquete 1.8.6).

## 3 Frentes de trabajo y solapamientos

Un frente de trabajo es un equipo con un responsable y un conjunto de cuentas de control que avanza en paralelo con los demás. La Tabla «tab:T15-frentes» define los frentes a partir de la EDT del Formulario T-14 y de los responsables de su diccionario.

**Frentes de trabajo. Fuente: elaboración propia a partir del Formulario T-14.**

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

Los frentes se sincronizan en los hitos del Formulario E-25 y en los comités del Art. 71°, cuyas actas registran los acuerdos entre frentes (paquetes 1.8.2 a 1.8.5). La Figura «fig:T15-frentes» presenta su ventana de actividad entre los meses 1 y 21.

  
  **Descripción textual de figura.** No sustituye la revisión visual del PDF.
- Solapamiento / meses 13 a 15
- Solapamiento / meses 19 y 20
- **F8 Operación** / Líder de Operación / SRE
- 8.1–8.3, 8.5: desde el mes 21 hasta el 56 $→$
  
**Figura: Frentes de trabajo de los meses 1 a 21 y solapamientos del Art. 17.2. Fuente: elaboración propia a partir de la Tabla T-15.1 y del Formulario T-14.**

  <a id="fig:T15-frentes"></a>

En los meses 13 a 15 trabajan a la vez F7, en la marcha blanca de la Etapa 1; F3, en las correcciones de esa marcha blanca; F4, en el desarrollo de la Etapa 2; F6, en las pruebas de ambas etapas; y F1 y F2. F3 y F4 dependen del mismo rol, el Líder de Desarrollo, y por eso son equipos distintos: el equipo que atiende la marcha blanca no puede ser el que desarrolla la Etapa 2 (Art. 17.2, punto 1). En los meses 19 y 20 trabajan F7, en la marcha blanca de la Etapa 2; F4, en sus correcciones; F6; y el soporte de la Etapa 1 en producción.

## 4 Modelo cuantitativo provisional de recursos

**Base de cálculo:** estimación de planificación con tamaños supuestos. No acredita productividad medida, contratación, turnos nominales ni aceptación del CLIENTE. Permite preparar SD8 con supuestos trazables.

### 4.1 Supuestos y cálculo

- Capacidad nominal asumida: 160 HH/persona-mes; disponibilidad programable 80 %; capacidad efectiva 128 HH. El 20 % cubre ausencias y coordinación no imputada. No es una jornada contractual ni un cálculo de cumplimiento laboral.
- Esfuerzo inicial por clase y paquete: G gestión/acta 80 HH; E diseño/configuración/innovación 240 HH; D módulo 960 HH; I integración/migración 480 HH; V prueba 320 HH (integración y cierres de certificación: 160 HH); T instalación/capacitación 160 HH. Son tamaños supuestos, a sustituir por estimaciones del equipo con trazabilidad al T-12 y cantidades reales.
- R identifica esfuerzo recurrente mensual, incluidos equivalentes mensuales de actividades anuales/semestrales: la distribución contable no cambia la frecuencia de ejecución del T-14.
- A identifica acompañamiento: 13 puestos simultáneos de terreno/coordinación; 12 × 24 días × 8 horas + 160 HH de coordinación = 2.464 HH por cuatro semanas; soporte E1 meses 16–20 con previsión 2.464/1.312/544/544/544 HH para puestos 13/7/3/3/3, condicionada a los indicadores del T-18. Las cuatro semanas de 4.3.2 se reparten por días: con el H12 firmado el 5 de octubre de 2028, primer día después de los tres primeros días hábiles, 23 de los 24 días de lunes a sábado caen en el mes 21 y uno en el mes 22; por eso 4.3.2 imputa 2.361,33 HH en el mes 21 y 102,67 en el mes 22. Si la fecha efectiva cambia, se recalcula el reparto sin acortar las cuatro semanas.
- C identifica cobertura por horas-posición del calendario real, con el mes 1 en febrero de 2027 (Anexo 7.A). NOC (8.1.1) y SOC (8.1.5) mantienen un puesto 24×7 cada uno: días del mes × 24, es decir 744 HH en un mes de 31 días, 720 en uno de 30 y 672 en febrero. La mesa (8.1.2, primera línea de incidentes del Art. 78°) aplica las posiciones del SD4, Anexo 4-W.7: 7 en la hora cargada y 2 en las otras 17 horas de 04:00 a 22:00, o 41 horas-posición por día de lunes a sábado; en septiembre y diciembre se suman 6 horas-posición de 22:00 a 04:00 de lunes a sábado y 24 los domingos. Así, un mes de 26 días de lunes a sábado exige 26 × 41 = 1.066 HH de mesa, y septiembre de 2028 exige 26 × 47 + 4 × 24 = 1.318 HH. El SOC puede prestarse con personal propio o subcontratado (RT-11.17; SD4, Anexo 4-W.7); en ambos casos sus HH se imputan aquí. Las posiciones de la mesa provienen de un Erlang C con supuestos de demanda: no acreditan abandono ni resolución al primer contacto, que se miden según la sección 5.6. La curva dimensiona relevos con 128 HH efectivas.
- O = 0,75M; P = 1,25M; E = (O + 4M + P)/6 = M. Para A/C, O = M = P: no se reduce cobertura por un escenario optimista. Los riesgos de demanda y ausencias se tratan separadamente.
- E se reparte uniformemente entre los meses inclusivos declarados. Las ventanas relativas son supuestos de asignación; las restricciones originales de aceptación del T-14 prevalecen. Coincidir en un mes no demuestra que una precedencia dentro del mes se haya satisfecho.
- Personas por rol/mes = techo(HH del rol / 128). Se suman techos por familia de trabajo dirigida por el rol; el responsable nominado dirige el equipo, no ejecuta solo todas las HH. JP/ARQ y los otros códigos identifican equipos con liderazgo y apoyo competente: un valor 5 en JP significa cinco personas equivalentes de dirección/documentación, no cinco jefes de proyecto. La sección 5.7 compara la curva con la dotación declarada y con los roles mínimos; antes de aprobar recursos se deben asignar personas distintas con competencias y turnos verificables.
- Reserva protegida E1 en meses 13–20: dos desarrolladores y un QA, 256 HH DES + 128 HH CAL/mes; no se presta a E2 ni se duplica como trabajo base.
- Soporte puente E1 meses 16–20: NOC + mesa con la misma regla de calendario que la operación (1.851, 1.786, 1.810, 1.851 y 2.038 HH; total 9.336 HH), imputado a 4.2.2 y financiado dentro de implementación. El SOC opera desde el mes 13 por 8.1.5, porque la marcha blanca ya trata datos reales. Operación contractual empieza en el mes 21.
- Ventanas ajustadas para respetar el Anexo 7.B: 2.3.1/2.3.2 terminan en el mes 3 y 5.1.2 ocupa el mes 4 (D-09); la sala 6.1.1–6.1.4 empieza en el mes 5, después de la especificación (D-10), y su recepción 6.1.5 ocurre en el mes 6, después de 6.1.2–6.1.4 y antes de los racks (D-11); los prototipos 2.6.2 terminan en el mes 4, antes de la construcción 3.4 (D-05); la identidad 3.3.1 empieza en el mes 5, después del plan de seguridad 2.2.1 aprobado en el H2 (D-06); la integración con el ERP 3.3.2 termina en el mes 9 para dejar la revisión del H4 dentro del mes 10 (sección 5.5). La actualización anual del Plan de Reversibilidad 1.7.2 ocurre en el mes 15, primer aniversario de su entrega del mes 3; las siguientes son 8.1.4. El acompañamiento de salida 9.2.1 ocupa los meses 54 a 56 para cubrir sus 90 días dentro del contrato.

### 4.2 Horas por los 222 paquetes

| EDT | Clase | Rol | Meses | O HH | M HH | P HH | E HH |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1.1 | G | JP | 1–1 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.1.2 | G | JP | 1–1 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.1.3 | G | JP | 1–1 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.2.1 | G | ARQ | 1–2 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.2.2 | G | IMP | 1–3 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.2.3 | G | ARQ | 1–4 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.2.4 | G | CAL | 2–2 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.2.5 | G | ARQ | 13–14 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.3.1 | G | JP | 1–2 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.3.2 | G | JP | 2–2 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.3.3 | G | JP | 2–2 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.3.4 | G | JP | 2–2 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.3.5 | R | JP | 1–20 | 360.00 | 480.00 | 600.00 | 480.00 |
| 1.4.1 | G | JP | 1–1 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.4.2 | G | JP | 1–1 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.4.3 | R | JP | 1–56 | 672.00 | 896.00 | 1120.00 | 896.00 |
| 1.5.1 | G | CAL | 2–4 | 60.00 | 80.00 | 100.00 | 80.00 |
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
| 1.9.1 | G | SEG | 1–4 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.9.2 | G | SEG | 1–3 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.9.3 | G | SEG | 2–4 | 60.00 | 80.00 | 100.00 | 80.00 |
| 1.9.4 | R | SEG | 1–56 | 168.00 | 224.00 | 280.00 | 224.00 |
| 1.9.5 | R | JP | 1–56 | 168.00 | 224.00 | 280.00 | 224.00 |
| 2.1.1 | E | ARQ | 2–4 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.1.2 | E | ARQ | 2–4 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.1.3 | E | DAT | 2–4 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.1.4 | E | ARQ | 13–14 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.2.1 | E | SEG | 2–4 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.2.2 | E | SEG | 3–10 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.2.3 | E | SEG | 3–6 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.2.4 | E | SEG | 2–4 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.3.1 | E | SRE | 2–3 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.3.2 | E | SRE | 2–3 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.3.3 | E | SRE | 2–4 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.4.1 | E | ARQ | 4–4 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.4.2 | E | ARQ | 14–14 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.5.1 | E | SRE | 3–8 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.5.2 | E | SRE | 3–8 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.6.1 | E | IMP | 2–4 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.6.2 | E | IMP | 3–4 | 180.00 | 240.00 | 300.00 | 240.00 |
| 2.6.3 | E | IMP | 4–6 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.1.1 | E | SRE | 6–6 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.1.2 | E | SRE | 6–6 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.1.3 | E | SRE | 6–6 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.1.4 | E | SRE | 4–6 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.1.5 | E | SRE | 6–6 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.2.1 | E | SRE | 4–6 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.2.2 | E | SRE | 4–6 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.2.3 | E | SRE | 4–8 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.2.4 | E | SRE | 4–6 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.2.5 | E | SEG | 4–6 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.2.6 | E | SRE | 5–6 | 180.00 | 240.00 | 300.00 | 240.00 |
| 3.3.1 | I | SEG | 5–8 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.3.2 | I | ARQ | 5–9 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.3.3 | I | ARQ | 5–9 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.3.4 | I | ARQ | 5–9 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.3.5 | I | ARQ | 5–9 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.3.6 | I | ARQ | 5–9 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.4.1 | D | DES | 5–7 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.4.2 | D | DES | 5–7 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.4.3 | D | DES | 8–8 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.4.4 | D | DES | 8–9 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.4.5 | D | DES | 5–9 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.4.6 | D | DES | 6–8 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.4.7 | D | DES | 9–9 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.4.8 | D | DES | 9–9 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.4.9 | D | DES | 9–9 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.4.10 | D | DES | 9–9 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.4.11 | D | DAT | 8–9 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.5.1 | D | DES | 15–16 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.5.2 | D | DES | 15–16 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.5.3 | D | DES | 15–16 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.5.4 | D | DAT | 15–16 | 720.00 | 960.00 | 1200.00 | 960.00 |
| 3.6.1 | I | DAT | 7–11 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.6.2 | I | DES | 7–10 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.6.3 | I | DES | 7–10 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.6.4 | I | DES | 7–10 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.6.5 | I | DES | 13–18 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.6.6 | I | DES | 17–19 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.7.1 | I | DAT | 7–8 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.7.2 | I | DAT | 9–10 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.7.3 | I | DAT | 11–11 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.7.4 | I | DAT | 11–11 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.7.5 | I | DAT | 12–12 | 360.00 | 480.00 | 600.00 | 480.00 |
| 3.8.1 | V | CAL | 10–10 | 120.00 | 160.00 | 200.00 | 160.00 |
| 3.8.2 | V | CAL | 11–12 | 240.00 | 320.00 | 400.00 | 320.00 |
| 3.8.3 | V | CAL | 11–12 | 240.00 | 320.00 | 400.00 | 320.00 |
| 3.8.4 | V | CAL | 11–12 | 240.00 | 320.00 | 400.00 | 320.00 |
| 3.8.5 | V | CAL | 11–12 | 240.00 | 320.00 | 400.00 | 320.00 |
| 3.8.6 | V | SEG | 11–12 | 120.00 | 160.00 | 200.00 | 160.00 |
| 3.8.7 | V | CAL | 12–12 | 120.00 | 160.00 | 200.00 | 160.00 |
| 3.8.8 | V | SRE | 11–12 | 240.00 | 320.00 | 400.00 | 320.00 |
| 3.9.1 | V | CAL | 17–17 | 120.00 | 160.00 | 200.00 | 160.00 |
| 3.9.2 | V | CAL | 18–18 | 240.00 | 320.00 | 400.00 | 320.00 |
| 3.9.3 | V | CAL | 18–18 | 240.00 | 320.00 | 400.00 | 320.00 |
| 3.9.4 | V | CAL | 18–18 | 240.00 | 320.00 | 400.00 | 320.00 |
| 3.9.5 | V | SEG | 18–18 | 240.00 | 320.00 | 400.00 | 320.00 |
| 3.9.6 | V | CAL | 18–18 | 120.00 | 160.00 | 200.00 | 160.00 |
| 3.9.7 | V | SRE | 18–18 | 120.00 | 160.00 | 200.00 | 160.00 |
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
| 4.1.1 | G | IMP | 10–12 | 60.00 | 80.00 | 100.00 | 80.00 |
| 4.1.2 | G | IMP | 11–12 | 60.00 | 80.00 | 100.00 | 80.00 |
| 4.1.3 | G | IMP | 17–18 | 60.00 | 80.00 | 100.00 | 80.00 |
| 4.2.1 | A | IMP | 13–15 | 7392.00 | 7392.00 | 7392.00 | 7392.00 |
| 4.2.2 | A | IMP | 16–20 | 5408.00 | 5408.00 | 5408.00 | 5408.00 |
| 4.2.3 | G | JP | 16–16 | 60.00 | 80.00 | 100.00 | 80.00 |
| 4.3.1 | A | IMP | 19–20 | 4928.00 | 4928.00 | 4928.00 | 4928.00 |
| 4.3.2 | A | IMP | 21–22 | 2464.00 | 2464.00 | 2464.00 | 2464.00 |
| 4.3.3 | G | JP | 21–21 | 60.00 | 80.00 | 100.00 | 80.00 |
| 4.3.4 | G | JP | 21–21 | 60.00 | 80.00 | 100.00 | 80.00 |
| 5.1.1 | G | ARQ | 2–4 | 60.00 | 80.00 | 100.00 | 80.00 |
| 5.1.2 | G | ARQ | 4–4 | 60.00 | 80.00 | 100.00 | 80.00 |
| 5.1.3 | G | SRE | 5–6 | 60.00 | 80.00 | 100.00 | 80.00 |
| 5.2.1 | G | SRE | 2–3 | 60.00 | 80.00 | 100.00 | 80.00 |
| 5.2.2 | G | SRE | 4–6 | 60.00 | 80.00 | 100.00 | 80.00 |
| 5.2.3 | G | ARQ | 4–6 | 60.00 | 80.00 | 100.00 | 80.00 |
| 5.3.1 | G | SRE | 4–6 | 60.00 | 80.00 | 100.00 | 80.00 |
| 5.3.2 | G | SRE | 4–6 | 60.00 | 80.00 | 100.00 | 80.00 |
| 5.3.3 | G | SRE | 4–6 | 60.00 | 80.00 | 100.00 | 80.00 |
| 5.4.1 | G | IMP | 9–12 | 60.00 | 80.00 | 100.00 | 80.00 |
| 5.4.2 | G | IMP | 9–12 | 60.00 | 80.00 | 100.00 | 80.00 |
| 5.4.3 | G | JP | 17–20 | 60.00 | 80.00 | 100.00 | 80.00 |
| 5.4.4 | G | JP | 7–9 | 60.00 | 80.00 | 100.00 | 80.00 |
| 6.1.1 | T | SRE | 5–5 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.1.2 | T | SRE | 5–6 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.1.3 | T | SRE | 5–6 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.1.4 | T | SRE | 5–6 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.1.5 | T | SRE | 6–6 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.2.1 | T | SRE | 4–6 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.2.2 | T | SRE | 6–6 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.2.3 | T | SRE | 7–11 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.3.1 | T | SRE | 6–6 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.3.2 | T | SRE | 6–6 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.3.3 | T | SRE | 6–6 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.3.4 | T | SRE | 9–11 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.4.1 | T | SEG | 5–6 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.4.2 | T | SEG | 5–6 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.4.3 | T | SEG | 5–6 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.5.1 | T | SRE | 9–12 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.5.2 | T | SRE | 10–12 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.5.3 | T | SRE | 9–11 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.5.4 | T | SRE | 10–12 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.5.5 | T | SRE | 10–12 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.5.6 | T | SRE | 9–12 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.6.1 | T | SRE | 5–6 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.6.2 | T | SRE | 5–6 | 120.00 | 160.00 | 200.00 | 160.00 |
| 6.6.3 | T | SRE | 6–6 | 120.00 | 160.00 | 200.00 | 160.00 |
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

| Etapa | HH base y cobertura | HH reserva protegida | HH programadas | Frentes | Meses |
| --- | --- | --- | --- | --- | --- |
| E1 Desarrollo | 37735.09 | 0 | 37735.09 | F1,F2,F3,F5,F6,F7 | 1–12 |
| E1 Marcha blanca | 11263.39 | 1152 | 12415.39 | F1,F2,F3,F5,F6,F7 | 13–15 |
| E2 Desarrollo | 11537.86 | 0 | 11537.86 | F1,F2,F4,F5,F6,F7 | 13–18 |
| E2 Marcha blanca | 7374.45 | 0 | 7374.45 | F1,F2,F4,F6,F7 | 19–20 |
| E1 Soporte puente | 14744.00 | 1920 | 16664.00 | F3,F5,F6,F7 | 16–20 |
| Operación | 114212.67 | 0 | 114212.67 | F1,F8 | 21–56 |
| Cierre y estabilización implementación | 2834.54 | 0 | 2834.54 | F1,F2,F4,F6,F7 | 21–22 |

Total exacto de paquetes y componentes = 202774.00 HH (190.366 base + 9.336 puente + 3.072 reserva); peak mensual conjunto = 66 personas equivalentes en el mes 16, cuando coinciden el desarrollo de la Etapa 2, el soporte puente de la Etapa 1 y el SOC. La versión anterior publicaba 147.328 HH porque imputaba un solo puesto de mesa, 32 HH/mes de SOC y promedios de 730 HH por mes; la mesa y el SOC dimensionados en el SD4 y el calendario real elevan la operación y el soporte puente. La implementación imputada a los meses 21 y 22 se separa de Operación; las actividades generales que continúan como servicio permanecen en Operación. Los peaks de etapas no se suman. Las centésimas de presentación se distribuyen por mayor resto entre meses y se concilian por etapa; la suma publicada conserva 202.774 HH exactas.

### 4.4 Curvas mensuales: horas por etapa y personas por rol

| Mes | E1 desarrollo | E1 MB | E2 desarrollo | E2 MB | Soporte puente | Operación | Cierre y estabilización implementación | Total HH | JP | ARQ | SEG | DAT | DES | CAL | SRE | IMP | Personas totales |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 705.33 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 705.33 | 5 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 8 |
| 2 | 1785.33 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1785.33 | 4 | 2 | 2 | 1 | 0 | 2 | 3 | 2 | 16 |
| 3 | 1835.33 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1835.33 | 2 | 2 | 3 | 2 | 0 | 2 | 4 | 3 | 18 |
| 4 | 2346.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 2346.08 | 1 | 5 | 3 | 2 | 1 | 1 | 6 | 3 | 22 |
| 5 | 3706.08 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3706.08 | 1 | 5 | 5 | 1 | 7 | 1 | 11 | 1 | 32 |
| 6 | 5636.74 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 5636.74 | 1 | 5 | 5 | 1 | 10 | 1 | 25 | 1 | 49 |
| 7 | 2992.74 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 2992.74 | 2 | 4 | 2 | 4 | 12 | 1 | 2 | 0 | 27 |
| 8 | 4272.75 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 4272.75 | 2 | 4 | 2 | 8 | 19 | 1 | 2 | 0 | 38 |
| 9 | 7171.41 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 7171.41 | 2 | 4 | 1 | 11 | 39 | 1 | 2 | 1 | 61 |
| 10 | 2045.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 2045.99 | 1 | 1 | 1 | 6 | 3 | 2 | 4 | 2 | 20 |
| 11 | 2895.99 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 2895.99 | 1 | 1 | 1 | 9 | 1 | 6 | 5 | 3 | 27 |
| 12 | 2341.32 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 2341.32 | 1 | 1 | 1 | 5 | 1 | 7 | 4 | 3 | 23 |
| 13 | 0.00 | 4075.10 | 360.00 | 0.00 | 0.00 | 0.00 | 0.00 | 4435.10 | 1 | 2 | 6 | 1 | 3 | 2 | 1 | 22 | 38 |
| 14 | 0.00 | 4123.10 | 720.00 | 0.00 | 0.00 | 0.00 | 0.00 | 4843.10 | 1 | 4 | 6 | 1 | 3 | 2 | 1 | 23 | 41 |
| 15 | 0.00 | 4217.19 | 2200.00 | 0.00 | 0.00 | 0.00 | 0.00 | 6417.19 | 2 | 1 | 6 | 5 | 14 | 2 | 1 | 23 | 54 |
| 16 | 0.00 | 0.00 | 3329.19 | 0.00 | 4699.00 | 0.00 | 0.00 | 8028.19 | 2 | 1 | 6 | 4 | 14 | 2 | 15 | 22 | 66 |
| 17 | 0.00 | 0.00 | 1662.34 | 0.00 | 3482.00 | 0.00 | 0.00 | 5144.34 | 2 | 1 | 6 | 0 | 4 | 3 | 15 | 13 | 44 |
| 18 | 0.00 | 0.00 | 3266.33 | 0.00 | 2738.00 | 0.00 | 0.00 | 6004.33 | 2 | 1 | 9 | 0 | 4 | 10 | 16 | 8 | 50 |
| 19 | 0.00 | 0.00 | 0.00 | 3779.23 | 2779.00 | 0.00 | 0.00 | 6558.23 | 2 | 1 | 6 | 0 | 4 | 2 | 15 | 26 | 56 |
| 20 | 0.00 | 0.00 | 0.00 | 3595.22 | 2966.00 | 0.00 | 0.00 | 6561.22 | 2 | 1 | 6 | 0 | 3 | 2 | 17 | 26 | 57 |
| 21 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3098.32 | 2834.54 | 5932.86 | 3 | 1 | 7 | 1 | 3 | 1 | 16 | 20 | 52 |
| 22 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3232.99 | 0.00 | 3232.99 | 1 | 1 | 6 | 1 | 2 | 1 | 16 | 2 | 30 |
| 23 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3454.32 | 0.00 | 3454.32 | 1 | 1 | 7 | 1 | 2 | 1 | 18 | 1 | 32 |
| 24 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3228.65 | 0.00 | 3228.65 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 2 | 31 |
| 25 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 2961.65 | 0.00 | 2961.65 | 1 | 1 | 6 | 1 | 2 | 1 | 15 | 2 | 29 |
| 26 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3228.65 | 0.00 | 3228.65 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 2 | 31 |
| 27 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3082.65 | 0.00 | 3082.65 | 1 | 1 | 6 | 1 | 2 | 1 | 15 | 1 | 28 |
| 28 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3181.23 | 0.00 | 3181.23 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 29 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3092.23 | 0.00 | 3092.23 | 1 | 1 | 6 | 1 | 2 | 1 | 16 | 1 | 29 |
| 30 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3140.23 | 0.00 | 3140.23 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 31 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3181.23 | 0.00 | 3181.23 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 32 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3321.23 | 0.00 | 3321.23 | 1 | 1 | 6 | 1 | 2 | 1 | 17 | 1 | 30 |
| 33 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3181.22 | 0.00 | 3181.22 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 34 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3092.22 | 0.00 | 3092.22 | 1 | 1 | 6 | 1 | 2 | 1 | 16 | 1 | 29 |
| 35 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3416.22 | 0.00 | 3416.22 | 1 | 1 | 7 | 1 | 2 | 1 | 18 | 1 | 32 |
| 36 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3181.22 | 0.00 | 3181.22 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 37 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 2914.22 | 0.00 | 2914.22 | 1 | 1 | 6 | 1 | 2 | 1 | 15 | 1 | 28 |
| 38 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3140.22 | 0.00 | 3140.22 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 39 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3092.22 | 0.00 | 3092.22 | 1 | 1 | 6 | 1 | 2 | 1 | 16 | 1 | 29 |
| 40 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3181.22 | 0.00 | 3181.22 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 41 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3051.22 | 0.00 | 3051.22 | 1 | 1 | 6 | 1 | 2 | 1 | 15 | 1 | 28 |
| 42 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3181.22 | 0.00 | 3181.22 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 43 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3181.22 | 0.00 | 3181.22 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 44 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3321.22 | 0.00 | 3321.22 | 1 | 1 | 6 | 1 | 2 | 1 | 17 | 1 | 30 |
| 45 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3181.22 | 0.00 | 3181.22 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 46 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3092.22 | 0.00 | 3092.22 | 1 | 1 | 6 | 1 | 2 | 1 | 16 | 1 | 29 |
| 47 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3416.22 | 0.00 | 3416.22 | 1 | 1 | 7 | 1 | 2 | 1 | 18 | 1 | 32 |
| 48 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3181.22 | 0.00 | 3181.22 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 49 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 2914.22 | 0.00 | 2914.22 | 1 | 1 | 6 | 1 | 2 | 1 | 15 | 1 | 28 |
| 50 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3140.22 | 0.00 | 3140.22 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 51 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3092.22 | 0.00 | 3092.22 | 1 | 1 | 6 | 1 | 2 | 1 | 16 | 1 | 29 |
| 52 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3181.22 | 0.00 | 3181.22 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 53 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3051.22 | 0.00 | 3051.22 | 1 | 1 | 6 | 1 | 2 | 1 | 15 | 1 | 28 |
| 54 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3207.89 | 0.00 | 3207.89 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 55 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3166.89 | 0.00 | 3166.89 | 1 | 1 | 7 | 1 | 2 | 1 | 16 | 1 | 30 |
| 56 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3450.89 | 0.00 | 3450.89 | 1 | 1 | 7 | 1 | 2 | 1 | 18 | 1 | 32 |

Factibilidad por capacidad aritmética: se debe dotar cada rol con la curva indicada. Esto no acredita contratación, disponibilidad real ni suficiencia de la mesa. El registro nominal y los turnos deben comprobarse antes de aprobar la línea base. La reserva E1 es exclusiva; el trabajo de E2 usa capacidad adicional. La revisión de HH modifica conjuntamente dotación, cronograma y exposición de SD8.

## 5 Red agregada, restricciones y escenarios de calendario

### 5.1 Cálculo reproducible

t = 0 abre el mes 1; t = 10 cierra el mes 10 (H4). Cada hito del Formulario E-25 se cumple con el acta de aceptación (Art. 18.1), y el CLIENTE dispone de diez días hábiles para revisar cada entregable (Art. 18.3). Por eso la red incluye, antes de cada hito de aceptación, un retardo R de 0,5 mes, equivalente a esos diez días hábiles: el trabajo técnico termina medio mes antes del cierre del mes del hito. Los diez días hábiles de subsanación no se programan como trabajo normal; si se necesitan, el hito se atrasa, y la segunda presentación con observaciones de la misma naturaleza es atraso imputable (Art. 18.3). t = 12/18 abre la marcha blanca siguiente; t = 15/20 marca la frontera hacia los meses 16/21, cuyo acta se firma en un día permitido del mes.

ES = máximo(liberación, EF de predecesores); EF = ES + d; LF = mínimo(LS sucesores, plazo aplicable); LS = LF − d; HT = LS − ES; HL = mínimo(ES sucesores) − EF. Se calcularon ambas pasadas sobre 24 bloques de trabajo y sus retardos de revisión, no sobre los 222 paquetes.

| ID | Bloque | d meses | Liberación t | Predecesores FC | ES | EF | LS | LF | HT | HL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| N01 | Alcance: 1.2.1, 1.2.4 | 1.50 | 0.00 | — | 0.00 | 1.50 | 0.00 | 1.50 | 0.00 | 0.00 |
| R-H1 | Revisión Art. 18.3 | 0.50 | 0.00 | N01 | 1.50 | 2.00 | 1.50 | 2.00 | 0.00 | 0.00 |
| N02 | Diseño E1: 2.1, 2.2, 2.4.1 | 1.50 | 0.00 | N01 | 1.50 | 3.00 | 2.00 | 3.50 | 0.50 | 0.50 |
| N03 | Interfaces: 1.2.3 | 3.50 | 0.00 | — | 0.00 | 3.50 | 0.00 | 3.50 | 0.00 | 0.00 |
| R-H2 | Revisión Art. 18.3 | 0.50 | 0.00 | N02, N03 | 3.50 | 4.00 | 3.50 | 4.00 | 0.00 | 0.00 |
| H2 | Aprobación H2 | 0.00 | 4.00 | R-H2 | 4.00 | 4.00 | 4.00 | 4.00 | 0.00 | 0.00 |
| N04 | Plataforma/borde H3 | 1.50 | 0.00 | H2 | 4.00 | 5.50 | 4.00 | 5.50 | 0.00 | 0.00 |
| R-H3 | Revisión Art. 18.3 | 0.50 | 0.00 | N04 | 5.50 | 6.00 | 5.50 | 6.00 | 0.00 | 0.00 |
| H3 | Ambientes H3 | 0.00 | 6.00 | R-H3 | 6.00 | 6.00 | 6.00 | 6.00 | 0.00 | 1.00 |
| N05 | Recepción/inventario: 3.4.1/2 | 3.00 | 0.00 | H2 | 4.00 | 7.00 | 4.00 | 7.00 | 0.00 | 0.00 |
| N06 | ERP/base: 3.3; cierre fin m9 | 5.00 | 0.00 | H2 | 4.00 | 9.00 | 4.00 | 9.00 | 0.00 | 0.00 |
| N07 | Resto E1: 3.4.3–11; cierre m9 | 2.00 | 0.00 | N05, H3 | 7.00 | 9.00 | 7.00 | 9.00 | 0.00 | 0.00 |
| N08 | Integración E1: 3.8.1, primera mitad m10 | 0.50 | 0.00 | N06, N07 | 9.00 | 9.50 | 9.00 | 9.50 | 0.00 | 0.00 |
| R-H4 | Revisión Art. 18.3 | 0.50 | 0.00 | N08 | 9.50 | 10.00 | 9.50 | 10.00 | 0.00 | 0.00 |
| H4 | Integración H4 | 0.00 | 10.00 | R-H4 | 10.00 | 10.00 | 10.00 | 10.00 | 0.00 | 0.00 |
| N09 | Certificación E1: 3.8.2–8 | 1.50 | 0.00 | H4 | 10.00 | 11.50 | 10.00 | 11.50 | 0.00 | 0.00 |
| R-H5 | Revisión Art. 18.3 | 0.50 | 0.00 | N09 | 11.50 | 12.00 | 11.50 | 12.00 | 0.00 | 0.00 |
| H5 | Certificación H5 | 0.00 | 12.00 | R-H5 | 12.00 | 12.00 | 12.00 | 12.00 | 0.00 | 0.00 |
| N10 | Marcha blanca E1 | 3.00 | 12.00 | H5 | 12.00 | 15.00 | 12.00 | 15.00 | 0.00 | 0.00 |
| H7 | Frontera producción E1; mes 16 | 0.00 | 15.00 | N10 | 15.00 | 15.00 | 15.00 | 15.00 | 0.00 | 0.00 |
| N11 | Diseño E2: 1.2.5, 2.1.4, 2.4.2 | 1.50 | 12.00 | — | 12.00 | 13.50 | 12.00 | 13.50 | 0.00 | 0.00 |
| R-H8 | Revisión Art. 18.3 | 0.50 | 0.00 | N11 | 13.50 | 14.00 | 13.50 | 14.00 | 0.00 | 0.00 |
| H8 | Diseño H8 | 0.00 | 14.00 | R-H8 | 14.00 | 14.00 | 14.00 | 14.00 | 0.00 | 0.00 |
| N12 | Módulos E2: 3.5; cierre m16 | 2.00 | 0.00 | H8 | 14.00 | 16.00 | 14.00 | 16.00 | 0.00 | 0.00 |
| N13 | Integración E2: 3.9.1; primera mitad m17 | 0.50 | 0.00 | N12 | 16.00 | 16.50 | 16.00 | 16.50 | 0.00 | 0.00 |
| R-H9 | Revisión Art. 18.3 | 0.50 | 0.00 | N13 | 16.50 | 17.00 | 16.50 | 17.00 | 0.00 | 0.00 |
| H9 | Integración H9 | 0.00 | 17.00 | R-H9 | 17.00 | 17.00 | 17.00 | 17.00 | 0.00 | 0.00 |
| N14 | Certificación E2: 3.9.2–7; primera mitad m18 | 0.50 | 0.00 | H9 | 17.00 | 17.50 | 17.00 | 17.50 | 0.00 | 0.00 |
| R-H10 | Revisión Art. 18.3 | 0.50 | 0.00 | N14 | 17.50 | 18.00 | 17.50 | 18.00 | 0.00 | 0.00 |
| H10 | Certificación H10 | 0.00 | 18.00 | R-H10 | 18.00 | 18.00 | 18.00 | 18.00 | 0.00 | 0.00 |
| N15 | Marcha blanca E2 | 2.00 | 18.00 | H10 | 18.00 | 20.00 | 18.00 | 20.00 | 0.00 | 0.00 |
| H12 | Frontera producción E2; mes 21 | 0.00 | 20.00 | N15 | 20.00 | 20.00 | 20.00 | 20.00 | 0.00 | 0.00 |

La red incorpora las precedencias corregidas del Anexo 7.B: D-05 (prototipos 2.6.2 cerrados en el mes 4, antes de N05/N07), D-06 (identidad 3.3.1 desde el mes 5, dentro de N06), D-09–D-11 (planos, especificación, sala y recepción en secuencia mensual) y D-28 (la estabilización 4.2.2 sigue al paso a producción). Las garantías, la certificación externa de las interfaces de las cadenas (3.6.5/3.6.6) y las interfaces de terceros no forman bloques propios: se programan como restricciones de los paquetes que las contienen y se verifican en el calendario diario.

### 5.2 Secuencias que hacen compatible el modelo

La preparación 3.4.3 completa sus 960 HH en mes 8, después de recepción/inventario; preventa 3.4.6 termina mes 8. Rutas 3.4.7 y reparto 3.4.8 se ejecutan en mes 9. Dentro de ese mes, reparto entrega su base aceptada en la primera mitad y cobranza 3.4.10 ejecuta sus 960 HH en la segunda; devoluciones 3.4.9 e indicadores 3.4.11 terminan en mes 9. Esta secuencia preserva D-16/D-18/D-19. Para reparto y cobranza, 960 / (0,5 × 128) = 15 personas equivalentes por subventana, con especialistas distintos o transferencia ordenada; el techo mensual no prueba esa asignación.

ERP/base 3.3 finaliza en t = 9,0 y 3.8.1 usa la primera mitad del mes 10; la segunda mitad queda para la revisión del CLIENTE. 3.6.2–4 y las funcionalidades INN-01/INN-03 que habilitan H4 finalizan también antes de t = 9,5. La certificación E1 concentra 3.8.2–3.8.8 en el mes 11 y la primera mitad del mes 12; la certificación E2 concentra 3.9.2–3.9.7 en la primera mitad del mes 18. Las HH de esas ventanas no cambian: se concentran en la subventana y requieren capacidad por subventana, cuya verificación nominal es condición de aprobación de la programación.

Los cuatro módulos 3.5 se construyen meses 15–16 después de H8; integración ocupa la primera mitad del mes 17 y certificación la del mes 18. La interfaz 3.6.5 se prepara meses 13–18 y debe aprobarse antes de H10; 3.6.6 certifica cada perfil antes de activarlo y todo el alcance antes del tramo final del T-18. La interfaz no se considera terminada por el fin de 3.5.

El bloque N04 resume las cadenas paralelas de compra, sala, racks y configuración: 5.1.2 en el mes 4; 6.1.1–6.1.4 en los meses 5 y 6; 6.1.5 al inicio del mes 6; 6.3.1/6.3.2 después de esa acta, y 6.6.3 antes de t = 5,5. Ningún paquete se entrega en QA antes de H3. Las entregas parciales dentro del mes 6 (acta de sala, montaje y configuración) se programan por día antes de aprobar la línea base.

### 5.3 Márgenes y análisis PERT de duración

| Control | Fin técnico t | Revisión Art. 18.3 | Hito t | Reserva de calendario utilizable |
| --- | --- | --- | --- | --- |
| Integración E1 | 9,5 | 9,5–10 | H4 10 | 0 meses |
| Certificación E1 | 11,5 | 11,5–12 | H5 12 | 0 meses |
| Integración E2 | 16,5 | 16,5–17 | H9 17 | 0 meses |
| Certificación E2 | 17,5 | 17,5–18 | H10 18 | 0 meses |

La duración PERT de cada bloque usa la misma tríada relativa que las HH: O = 0,75 d, M = d, P = 1,25 d, con dotación constante. Por eso T_E = (O + 4M + P)/6 = d y σ = (P − O)/6 = d/12. Los retardos de revisión se toman en su máximo de diez días hábiles y las marchas blancas tienen duración contractual fija; ninguno aporta varianza. La varianza de un camino es la suma de las varianzas de sus bloques, y la probabilidad de cumplir el hito es Φ((t_hito − T_E)/σ_camino).

| Hito | Camino de mayor varianza | σ camino (meses) | T_E = t hito | P(cumplir) | Reserva para 90 % (1,2816 σ) |
| --- | --- | --- | --- | --- | --- |
| H2 | N03 (3,5) | 0,29 | 4 | 50 % | 0,37 mes |
| H3 | N03 (3,5) + N04 (1,5) | 0,32 | 6 | 50 % | 0,41 mes |
| H4 | N03 (3,5) + N06 (5,0) + N08 (0,5) | 0,51 | 10 | 50 % | 0,65 mes |
| H5 | camino H4 + N09 (1,5) | 0,53 | 12 | 50 % | 0,67 mes |
| H9 | N11 (1,5) + N12 (2,0) + N13 (0,5) | 0,21 | 17 | 50 % | 0,27 mes |
| H10 | camino H9 + N14 (0,5) | 0,22 | 18 | 50 % | 0,28 mes |

Por ejemplo, para H4: σ = √(3,5² + 5,0² + 0,5²)/12 = √37,5/12 = 0,51 mes, unos 16 días. Con holgura cero y una tríada simétrica, cada hito tiene 50 % de probabilidad de cumplirse en su fecha, y la probabilidad conjunta es menor porque varios caminos convergen en el mismo hito. La red, por lo tanto, no tiene la reserva que el PERT exige para un 90 %: faltan 0,65 mes antes de H4 y 0,67 mes antes de H5. Esta brecha no se oculta con márgenes nominales. Antes de aprobar la línea base, LafroX debe crear esa reserva adelantando trabajo de la ruta crítica (N03 y N06) con capacidad adicional, o reducir su variabilidad con la estimación de equipo de la sección 4. Hasta entonces el riesgo queda registrado en el SD8 (R8-11 y E8-02).

Escenario determinista: una demora no recuperada de 0,25 mes en N06/N08 lleva la entrega de H4 a t = 9,75 y deja sólo 0,25 mes para la revisión; sin recuperación, el acta del H4 cae fuera del mes 10 y amenaza H5. Una demora de 0,50 mes en N12/N13 lleva H9 a t = 17,50 y amenaza H10. Se trata de sensibilidad, no de autorización para mover hitos. La capacidad protegida E1 es 3.072 HH en meses 13–20 y no puede sanar un retraso previo a H5.

### 5.4 Gobierno

Las ventanas mensuales de acompañamiento son una imputación inicial: cuatro semanas desde un acta en día permitido pueden cruzar al mes siguiente, como ocurre con 4.3.2. Confirmada la fecha, se redistribuyen las mismas HH entre meses y se recalculan relevos; no se acorta el acompañamiento para mantener una celda mensual.

El JP revisa semanalmente fechas pronosticadas, consumo de capacidad y restricciones. Una amenaza a H4/H5/H9/H10 se escala sin esperar consumo de una holgura inexistente. La actualización de tareas, equipos o duración obliga a repetir el cálculo y conservar D-01–D-34; se mantienen los 56 meses y las condiciones del Art. 17.3. Ver SD8, Anexos 8.C/8.D, para escenarios, reservas y condiciones de evidencia.

### 5.5 Presentación de entregables y revisión del CLIENTE

Cada entregable que gatilla un hito se presenta al terminar su bloque técnico, medio mes antes del cierre del mes del hito, para que la revisión de diez días hábiles del Art. 18.3 termine dentro de ese mes. Los entregables que admiten revisión por partes se presentan por incrementos: los informes de QA de M1/M2 al cerrar N05 (t = 7), los del resto de los módulos al cerrar N07 (t = 9) y el informe de integración al cerrar N08 (t = 9,5). Así, la revisión final del H4 cubre sólo el último incremento. Si el CLIENTE formula observaciones, la subsanación de diez días hábiles corre en paralelo con el bloque siguiente, pero el hito no se da por cumplido hasta el acta. Este procedimiento no supone que el CLIENTE renuncie a su plazo ni que firme el acta el mismo día de la entrega.

### 5.6 Medición de los niveles de atención

El Erlang C de la mesa (SD4, Anexo 4-W.7) dimensiona la espera con llegadas de Poisson, atención exponencial y paciencia infinita. Sirve para el 80 % de respuestas antes de 20 segundos, pero no modela el abandono ni la resolución al primer contacto del RT-21.06 de las Bases Técnicas Transversales. Para ambos se aplica medición: desde la marcha blanca de la Etapa 1, la mesa registra por contacto la hora de llegada, de respuesta o de abandono y si se resolvió sin escalar. Con al menos cuatro semanas de registros se calibra un modelo con abandono (Erlang A) usando la paciencia observada, y se recalcula la dotación de 8.1.2 antes del mes 21. La resolución al primer contacto se sostiene con la base de conocimiento de 3.11 y la capacitación de 7.1, y se informa mensualmente. Si un indicador no se cumple durante dos meses seguidos, se aumenta la dotación de la franja afectada sin esperar la revisión anual.

### 5.7 Dotación requerida, roles mínimos y dotación declarada

La curva de la sección 4.4 se compara con la dotación técnica declarada en el SD1, Tabla 1.1. La comparación muestra dónde la curva cabe en las divisiones de LafroX y dónde se requiere asignación, contratación o subcontratación antes de aprobar la línea base. No acredita disponibilidad: las personas de esas divisiones atienden otros contratos.

| Familia T-15 | Peak de la curva | División del SD1 que la provee | Dotación declarada | Condición |
| --- | --- | --- | --- | --- |
| DES | 39 en el mes 9 | Desarrollo de software | 48 | La división declara Python, Django y móvil; la oferta usa Laravel/PHP. Se asignan sólo personas con experiencia en Laravel/PHP o capacitadas antes del mes 5, con verificación del Líder de Desarrollo. |
| SRE | 25 en el mes 6; 15 a 18 en Operación | SRE y Cloud (12) y NOC 24×7 (32) | 44 | El mes 6 concentra la instalación de sala, racks y sitios: energía, climatización e incendio (6.1.2–6.1.4) los ejecutan instaladores especializados supervisados por SRE. NOC y mesa se cubren con personal del NOC con turnos asignados. |
| SEG | 9 en el mes 18; 6 o 7 desde el mes 13 | CISO y especialistas en ciberseguridad | 7 | El puesto SOC 24×7 exige 6 personas equivalentes. Se cubre con contratación o con un servicio SOC subcontratado (RT-11.17), con las mismas horas de la sección 4.2. |
| CAL | 10 en el mes 18 | Aseguramiento y automatización de pruebas | 10 | Cabe sin margen; cualquier ausencia exige refuerzo. |
| ARQ y DAT | 5 y 11; 15 en conjunto en el mes 9 | Arquitectura de solución e integración | 15 | Datos y arquitectura comparten la división y la ocupan completa en el mes 9. |
| IMP | 26 en los meses 19 y 20 | La Tabla 1.1 no tiene una división de implantación | — | Los 13 puestos de acompañamiento se cubren con personal de implantación contratado para las marchas blancas y capacitado en 7.1. |
| JP | 5 en el mes 1 | Dirección de Operaciones, fuera de la Tabla 1.1 | — | Personas de dirección y documentación, no cinco jefes de proyecto. |

Los roles mínimos del numeral 19.2 de las Bases Técnicas Transversales se imputan a las familias así. El Jefe de Proyecto (100 % en implementación) se imputa a JP en los meses 1–21. El Líder de Desarrollo (100 % en implementación) se imputa a ARQ en los meses 1–4, donde participa en el diseño 2.1 y en los prototipos 2.6.2, y a DES desde el mes 4 (3.11.3/3.11.4 y los módulos); por eso la curva muestra DES cero en los meses 1–3 sin que el rol quede sin horas. El Líder Funcional (100 % en implementación) se imputa a IMP en los meses 1–4 (1.2.2 y 2.6) y a CAL e IMP desde el mes 5 (pruebas de aceptación y olas). El Líder de Integración (permanente en implementación) se imputa a ARQ (1.2.3, 3.3 y 3.6). Ninguna de estas imputaciones agrega horas: forman parte de las horas de los paquetes donde trabajan. El SD1, sección 1.5, nomina a las personas que ocupan cada rol.

## Referencias

Las fuentes de método citadas en este formulario son las siguientes.

  
-  Malcolm, D. G., Roseboom, J. H., Clark, C. E., & Fazar, W. (1959). Application of a technique for research and development program evaluation. *Operations Research, 7*(5), 646–669.
  
-  Project Management Institute. (2017). *La guía de los fundamentos para la dirección de proyectos (Guía del PMBOK®)* (6.ª ed.). Project Management Institute.

## Declaración de uso de IA

La tabla declara el uso de IA en este formulario; se consolida en la declaración del SD7 y en el Formulario A-6.

| Sección | Herramienta | Finalidad del uso | Nivel en texto | Nivel en diagramas | Revisión humana (quién y qué verificó) |
| --- | --- | --- | --- | --- | --- |
| 1 a 3 | Claude Code; Codex | Redacción del método, ruta crítica y frentes | Alto | Alto (descripciones de figuras) | No documentada |
| 4 Modelo de recursos | Codex; Claude Code | Cálculo de HH, curvas, calendario real y cobertura de mesa/SOC (7 de octubre de 2026) | Alto | Ninguno | No documentada |
| 5 Red, PERT y dotación | Claude Code | Red con revisiones Art. 18.3, PERT de duración, medición de atención y comparación con la dotación declarada (7 de octubre de 2026) | Alto | Ninguno | No documentada |
