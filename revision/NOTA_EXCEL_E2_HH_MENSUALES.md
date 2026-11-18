# Nota para el Excel y el E2: HH mensuales tras la reprogramación del T-15

## Reprogramación de olas y cadenas

El total no cambia (202.108,63 HH). Cambia el reparto de los meses 5 a 19 porque los módulos de la Etapa 1 se construyen en tres olas y el intercambio con las cadenas parte en el mes 9. Fuente: `formulario-t15/tablas/tab_T15_4.tex`.

## HH por mes

| Mes | Antes | Ahora | Diferencia |
|---|---:|---:|---:|
| 5 | 7.252,82 | 6.109,48 | -1.143,34 |
| 6 | 5.746,83 | 5.981,05 | 234,22 |
| 7 | 5.472,06 | 5.840,24 | 368,18 |
| 8 | 3.242,95 | 4.033,55 | 790,60 |
| 9 | 2.929,61 | 2.742,22 | -187,39 |
| 10 | 2.777,78 | 2.843,02 | 65,24 |
| 11 | 2.379,96 | 2.448,17 | 68,21 |
| 12 | 1.527,78 | 1.590,06 | 62,28 |
| 13 | 4.867,13 | 4.843,40 | -23,73 |
| 14 | 5.941,14 | 5.923,35 | -17,79 |
| 15 | 5.995,24 | 5.968,55 | -26,69 |
| 16 | 6.865,73 | 7.054,90 | 189,17 |
| 17 | 5.958,99 | 5.910,62 | -48,37 |
| 18 | 4.417,03 | 4.255,77 | -161,26 |
| 19 | 6.609,72 | 6.440,39 | -169,33 |

## Totales por período

| Período | Antes | Ahora | Diferencia |
|---|---:|---:|---:|
| E1 desarrollo | 42.293,99 | 42.551,99 | 258,00 |
| E1 marcha blanca | 12.490,69 | 12.439,49 | -51,20 |
| E2 desarrollo | 10.579,37 | 10.550,11 | -29,26 |
| E2 marcha blanca | 7.486,16 | 7.388,47 | -97,69 |
| E1 producción y estabilización | 16.776,88 | 16.697,03 | -79,85 |
| Operación | 109.791,32 | 109.791,32 | 0,00 |
| E2 cierre | 2.690,22 | 2.690,22 | 0,00 |
| Total | 202.108,63 | 202.108,63 | 0,00 |

## Qué revisar

- Costos mensuales de RR.HH. y Curva S en los meses 5 a 19.
- Las HH por paquete y por perfil no cambian; cambian los meses en que se ejecutan los módulos 4.1.1 a 4.3.5 y 4.5.1, y las integraciones 5.2.3, 5.2.4, 5.3.1 y 5.3.2 (`tab_T15_2.tex` y `tab_T15_asignacion_partidas.tex`).
- Códigos de paquete: usar la equivalencia `revision/edt_equivalencias_20261117.json` si el Excel cita códigos de la EDT.

## D10: servicios comunes de la Etapa 1

| Mes | Rol | Paquetes | HH por paquete | HH de D10 | HH mensuales del proyecto |
|---:|---|---|---:|---:|---:|
| 8 | DES | 3.3.4, 3.3.5 y 3.3.6 | 480 | +1.440 | 5.473,55 |

La línea base del proyecto suma 203.548,62 HH y la suma de la curva mensual es 203.548,63 HH por redondeo. E1 Desarrollo suma 43.991,98 HH en la línea base y 43.991,99 HH en la curva mensual. Para valorizar D10, imputar al mes 8 las 581,10 HH del perfil 09S, 387,39 HH del 09J, 235,76 HH del 08S y 235,75 HH del 08J.
