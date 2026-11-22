# Conciliación de pendientes del SD12

Registro interno para Planificación, Operación y el equipo de oferta. Las imputaciones y los importes de la oferta se actualizan con la versión conciliada de su documento de origen.

## Dedicación de Jefatura, Desarrollo y SRE

El T-15 del SD7 (`0624f701`) y la hoja «HH POR ROL Y MES» del libro `HH_POR_ROL_Y_MES_roles_minimos_20261114.xlsx`, en E2 (`2b04aaa7`), coinciden en el total de cada perfil a 56 meses. El libro contiene una propuesta de valores mensuales fechada el 14 de noviembre de 2026. La diferencia entre ambas fuentes está en el reparto por fase.

| Perfil | T-15, implementación / Operación (HH) | Libro mensual, implementación / Operación (HH) | Cambio de fase propuesto para contrastar |
|---|---:|---:|---|
| 01 · Jefatura | 2.582,10 / 1.012,87 | 2.560,00 / 1.034,97 | 22,10 HH hacia Operación |
| 04 · Desarrollo | 2.565,82 / 691,20 | 2.560,01 / 697,01 | 5,81 HH hacia Operación |
| 24 · SRE | 835,35 / 4.596,00 | 823,35 / 4.608,00 | 12,00 HH hacia Operación |

El libro programa 128 HH cada mes de dedicación completa, con 128,01 HH de Desarrollo en el mes 6. Planificación debe resolver ese centésimo en el cálculo mensual antes de incorporar el reparto. SD10 (`a97b8deb`) y SD11 (`65a89608`, sección 11.2) respaldan la gerencia dedicada de SRE durante los meses 21–56.

En la tabla de partidas del T-15, cruzan la frontera del mes 21 cinco partidas con 884,59 HH de Jefatura (1.3.3, 1.7.2, 1.7.7, 1.7.8 y 1.8.5) y dos líneas con 1.694,55 HH de SRE (1.7.5 y la línea de gerencia y permanencia). Sus ventanas abarcan ambas fases y requieren distribución por mes. Para Desarrollo, las ventanas de las filas suman 2.557,82 HH hasta el mes 20 y 699,20 HH desde el mes 21. La diferencia de 8 HH frente a la tabla por perfil coincide con las 8 HH de Desarrollo de la entrega 6.8.6, programada en el mes 21. Planificación debe verificar la fase de esa entrega y el centésimo del mes 6. Usar el archivo de revisión de roles mínimos de SD7 para rastrear los traspasos de PMO, los perfiles de diseño y DevOps. Cerrar cuando cada ajuste tenga partida y mes y se conserve el total por perfil.

## Soporte previo al corte de E1

El T-15, sección 4.3, imputa mayo completo a 9.3.1. El T-18 de SD7 fija el comienzo del puente el 17 de mayo de 2028. Aplicando la pauta del T-15, se obtiene el siguiente desglose de horas de cobertura.

| Tramo de mayo | NOC, 24 HH por día | Mesa, 41 HH de lunes a sábado | Total HH |
|---|---:|---:|---:|
| 1–16, previo al corte | 384 (16 días) | 574 (14 días) | 958 |
| 17–31, desde el corte | 360 (15 días) | 533 (13 días) | 893 |
| Mes completo | 744 | 1.107 | 1.851 |

Planificación debe comprobar los turnos y las actividades previas con Operación. Si existe cobertura programada, registrar el paquete que corresponda y sustituir su imputación dentro de 9.3.1. Si todo el tramo carece de cobertura respaldada, el puente se reduciría de 9.336 a 8.378 HH y el esfuerzo programado pasaría de 203.548,62 a 202.590,62 HH, antes de cualquier otra corrección. Si se acredita solo una parte, descontar de la línea base únicamente las horas sin actividad respaldada. En cada caso, recalcular la demanda del mes 16 y confirmar el impacto en las plazas y las curvas antes de trasladar la decisión al SD12.

## Desglose económico de servicios externos

El T-15 asigna 1.324,80 HH al código 00. La revisión de coherencia de E2 (`2b04aaa7`, hallazgo C10) identifica la falta del vínculo entre servicio y costo. La búsqueda de partidas se hizo en las hojas de adquisiciones y proveedores del libro de flujo adjunto a E2.

| EDT | HH externas | Partida candidata o evidencia que falta |
|---|---:|---|
| 8.3.2 | 128,00 | Adquisiciones de implementación, filas 51, 52 y 56. Separar el montaje y la puesta en marcha de la compra de UPS, generador y las obras agrupadas. |
| 8.3.3 | 128,00 | Adquisiciones de implementación, filas 53 y 56. Verificar en la cotización dónde se valorizó la instalación y qué parte corresponde a equipos. |
| 8.3.4 | 128,00 | Adquisiciones de implementación, fila 37. Obtener el desglose del montaje incluido con detección y extinción. |
| 6.5.1 | 320,00 | Identificar el importe de la primera evaluación independiente. |
| 6.5.2 | 160,00 | Identificar el importe de la segunda evaluación independiente. |
| 10.2.2 | 230,40 | Obtener los importes de las tres evaluaciones de Operación en los meses 28, 40 y 52. |
| 10.2.6 | 230,40 | Contrastar la adecuación eléctrica de la fila 33 de adquisiciones de Operación con el alcance de revisión semestral. Obtener el costo de las visitas de inspección. |

El equipo de oferta debe vincular cada costo con un desglose o cotización, descontar cualquier importe ya contado en otra fila y aplicar la misma base tributaria al costo y al precio contractual. La tabla de precio de E2 identifica el precio neto en UF como denominador si los costos se recogen netos en UF. Tras validar el numerador y el denominador, trasladar el mismo porcentaje al SD12 y al T-8.

## Designación y documentos de respaldo

| Pendiente | Responsable y evidencia necesaria |
|---|---|
| Representante de Mesa, meses 13–15 | Operación registra en el acta del comité a la persona, su rol, período y facultades. El calendario del T-15 ubica el turno propio de Mesa desde el mes 16, mientras que el SD10 (`a97b8deb`) documenta cobertura del SOC desde el mes 13. |
| Cartas del equipo | El equipo de oferta reúne el índice del Sobre N.º 1 y los diez originales firmados. Coteja por titular el rol, período y dedicación con el T-8 e incorpora los folios verificados al anexo 12.D. |
| AWS | Arquitectura y Operación cotejan el titular, la categoría y las competencias con el certificado o la carta de AWS. El SD1 (`107fa897`, sección 1.6) indica marzo de 2027. Con el día exacto, calcular la fecha límite de 60 días y registrar por separado la evidencia del inicio de renovación. |
