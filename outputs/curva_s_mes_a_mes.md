# Curva S mes a mes (LafroX, Excel del 13-11-2026)

Fuente: `LafroX_ModeloFinanciero_3_20261113.xlsx`, hojas **CURVA S** y **FLUJO CAJA NETO**. Montos en UF.

## Cómo se lee

- **Entra** = FLUJO CAJA NETO fila 21. **Sale** = fila 59. **Resultado** = Entra − Sale (fila 7; CURVA S fila 37).
- **Saldo** = saldo del mes anterior + Resultado (CURVA S fila 38). También es igual a Cobros acumulados − Pagos acumulados (CURVA S filas 34 y 35).
- La Curva S dibuja las dos columnas acumuladas. Cuando no entra nada, la curva de cobros queda plana. La distancia entre las dos curvas es el saldo de caja.
- Implementación: meses 1 a 20. Operación: meses 21 a 56. Crédito: interés del mes 2 al 39, cuota (amortización) del mes 16 al 39.

## Resumen

| Dato | Valor |
|---|---|
| Capital inicial (mes 1) | 18.000 (crédito 14.400 al 0,9 % mensual + socios 3.600) |
| Saldo más bajo | 414 en el mes 9 |
| Punto de equilibrio del flujo puro | mes 17 |
| Cobros totales | 278.430 (incluye el capital) |
| Pagos totales | 238.766 (incluye intereses 3.490 y amortización 14.400) |
| Saldo final | 39.664 |

## Tabla

| Mes | Entra | Qué entra | Sale | Sueldos | Otros pagos importantes | Resultado | Saldo | Cobros acum. | Pagos acum. |
|---:|---:|---|---:|---:|---|---:|---:|---:|---:|
| 1 | 18.000 | Capital 18.000 | 2.021 | 1.067 | Gastos adm. 785, Reservas 169 | 15.979 | **15.979** | 18.000 | 2.021 |
| 2 | 8.210 | Hito 1 8.210 | 15.905 | 2.578 | Adquisiciones 12.975, Gastos adm. 152, Intereses 130 | -7.694 | **8.285** | 26.210 | 17.925 |
| 3 | 0 | — | 2.546 | 2.256 | Gastos adm. 108, Intereses 130 | -2.546 | **5.739** | 26.210 | 20.471 |
| 4 | 7.184 | Hito 2 7.184 | 3.241 | 2.724 | Servicios 259, Gastos adm. 108, Intereses 130 | 3.943 | **9.682** | 33.395 | 23.712 |
| 5 | 0 | — | 5.597 | 5.080 | Servicios 259, Gastos adm. 108, Intereses 130 | -5.597 | **4.085** | 33.395 | 29.309 |
| 6 | 10.263 | Hito 3 10.263 | 4.372 | 3.855 | Servicios 259, Gastos adm. 108, Intereses 130 | 5.891 | **9.977** | 43.658 | 33.681 |
| 7 | 0 | — | 4.244 | 3.727 | Servicios 259, Gastos adm. 108, Intereses 130 | -4.244 | **5.732** | 43.658 | 37.925 |
| 8 | 0 | — | 2.767 | 2.250 | Servicios 259, Gastos adm. 108, Intereses 130 | -2.767 | **2.965** | 43.658 | 40.692 |
| 9 | 0 | — | 2.551 | 2.034 | Servicios 259, Gastos adm. 108, Intereses 130 | -2.551 | **414** | 43.658 | 43.243 |
| 10 | 10.263 | Hito 4 10.263 | 2.394 | 1.744 | Servicios 259, Gastos adm. 166, Intereses 130 | 7.869 | **8.283** | 53.921 | 45.637 |
| 11 | 0 | — | 2.172 | 1.546 | Capacitaciones 109, Servicios 259, Gastos adm. 108, Intereses 130 | -2.172 | **6.111** | 53.921 | 47.809 |
| 12 | 10.263 | Hito 5 10.263 | 1.509 | 928 | Servicios 259, Gastos adm. 108, Intereses 130 | 8.754 | **14.865** | 64.184 | 49.319 |
| 13 | 5.132 | Hito 6 5.132 | 4.900 | 3.520 | Capacitaciones 160, Servicios 259, Gastos adm. 733, Intereses 130 | 232 | **15.097** | 69.315 | 54.218 |
| 14 | 5.132 | Hito 8 5.132 | 4.832 | 4.113 | Capacitaciones 167, Servicios 259, Gastos adm. 137, Intereses 130 | 300 | **15.396** | 74.447 | 59.050 |
| 15 | 0 | — | 4.875 | 4.212 | Capacitaciones 140, Servicios 259, Gastos adm. 108, Intereses 130 | -4.875 | **10.521** | 74.447 | 63.926 |
| 16 | 10.263 | Hito 7 10.263 | 6.124 | 4.922 | Capacitaciones 139, Servicios 260, Gastos adm. 108, Intereses 130, Amortización 540 | 4.139 | **14.660** | 84.710 | 70.049 |
| 17 | 10.263 | Hito 9 10.263 | 5.352 | 4.168 | Capacitaciones 122, Servicios 260, Gastos adm. 108, Intereses 125, Amortización 545 | 4.911 | **19.571** | 94.973 | 75.402 |
| 18 | 10.263 | Hito 10 10.263 | 4.396 | 3.123 | Capacitaciones 210, Servicios 260, Gastos adm. 108, Intereses 120, Amortización 550 | 5.867 | **25.438** | 105.236 | 79.798 |
| 19 | 5.132 | Hito 11 5.132 | 6.055 | 4.878 | Servicios 260, Gastos adm. 108, Intereses 115, Amortización 555 | -924 | **24.514** | 110.367 | 85.853 |
| 20 | 0 | — | 6.145 | 4.960 | Capacitaciones 105, Servicios 260, Gastos adm. 108, Intereses 110, Amortización 560 | -6.145 | **18.369** | 110.367 | 91.998 |
| | | **— fin implementación —** | | | | | | | |
| 21 | 14.646 | Hito 12 10.263, Mensualidad op. 4.383 | 5.724 | 3.363 | Adquisiciones 672, Servicios 712, Gastos adm. 159, Intereses 105, Amortización 565 | 8.922 | **27.291** | 125.013 | 97.722 |
| 22 | 4.383 | Mensualidad op. 4.383 | 4.964 | 3.307 | Capacitaciones 125, Servicios 712, Gastos adm. 144, Amortización 570 | -581 | **26.710** | 129.397 | 102.686 |
| 23 | 4.383 | Mensualidad op. 4.383 | 4.164 | 2.610 | Servicios 712, Gastos adm. 108, Amortización 575 | 219 | **26.930** | 133.780 | 106.850 |
| 24 | 4.383 | Mensualidad op. 4.383 | 3.986 | 2.421 | Servicios 712, Gastos adm. 108, Amortización 580 | 397 | **27.327** | 138.163 | 110.836 |
| 25 | 4.383 | Mensualidad op. 4.383 | 4.712 | 2.529 | Servicios 712, Gastos adm. 733, Amortización 586 | -329 | **26.998** | 142.547 | 115.548 |
| 26 | 4.383 | Mensualidad op. 4.383 | 4.321 | 2.761 | Servicios 712, Gastos adm. 108, Amortización 591 | 62 | **27.061** | 146.930 | 119.869 |
| 27 | 4.383 | Mensualidad op. 4.383 | 4.220 | 2.663 | Servicios 712, Gastos adm. 108, Amortización 596 | 163 | **27.224** | 151.313 | 124.090 |
| 28 | 4.383 | Mensualidad op. 4.383 | 4.313 | 2.764 | Servicios 712, Gastos adm. 108, Amortización 602 | 71 | **27.294** | 155.697 | 128.402 |
| 29 | 4.383 | Mensualidad op. 4.383 | 4.238 | 2.688 | Servicios 712, Gastos adm. 108, Amortización 607 | 146 | **27.440** | 160.080 | 132.640 |
| 30 | 4.383 | Mensualidad op. 4.383 | 4.270 | 2.729 | Servicios 712, Gastos adm. 108, Amortización 612 | 113 | **27.554** | 164.463 | 136.910 |
| 31 | 4.383 | Mensualidad op. 4.383 | 4.298 | 2.762 | Servicios 712, Gastos adm. 108, Amortización 618 | 85 | **27.639** | 168.847 | 141.208 |
| 32 | 4.383 | Mensualidad op. 4.383 | 4.399 | 2.853 | Servicios 712, Gastos adm. 108, Amortización 623 | -15 | **27.623** | 173.230 | 145.607 |
| 33 | 4.383 | Mensualidad op. 4.383 | 4.362 | 2.765 | Servicios 712, Gastos adm. 159, Amortización 629 | 21 | **27.644** | 177.613 | 149.969 |
| 34 | 4.383 | Mensualidad op. 4.383 | 4.268 | 2.677 | Servicios 712, Gastos adm. 144, Amortización 635 | 116 | **27.760** | 181.997 | 154.237 |
| 35 | 4.383 | Mensualidad op. 4.383 | 4.483 | 2.945 | Servicios 712, Gastos adm. 108, Amortización 640 | -100 | **27.660** | 186.380 | 158.719 |
| 36 | 4.383 | Mensualidad op. 4.383 | 4.322 | 2.773 | Servicios 712, Gastos adm. 108, Amortización 646 | 61 | **27.721** | 190.763 | 163.042 |
| 37 | 4.383 | Mensualidad op. 4.383 | 4.682 | 2.515 | Servicios 712, Gastos adm. 733, Amortización 652 | -298 | **27.423** | 195.147 | 167.723 |
| 38 | 4.383 | Mensualidad op. 4.383 | 4.254 | 2.697 | Servicios 712, Gastos adm. 108, Amortización 658 | 130 | **27.553** | 199.530 | 171.977 |
| 39 | 4.383 | Mensualidad op. 4.383 | 4.269 | 2.697 | Servicios 712, Gastos adm. 108, Amortización 664 | 115 | **27.667** | 203.913 | 176.246 |
| 40 | 4.383 | Mensualidad op. 4.383 | 3.634 | 2.762 | Servicios 712, Gastos adm. 108 | 749 | **28.417** | 208.296 | 179.880 |
| 41 | 4.383 | Mensualidad op. 4.383 | 3.523 | 2.640 | Servicios 712, Gastos adm. 108 | 860 | **29.277** | 212.680 | 183.403 |
| 42 | 4.383 | Mensualidad op. 4.383 | 3.628 | 2.756 | Servicios 712, Gastos adm. 108 | 755 | **30.032** | 217.063 | 187.031 |
| 43 | 4.383 | Mensualidad op. 4.383 | 3.646 | 2.775 | Servicios 712, Gastos adm. 108 | 737 | **30.770** | 221.446 | 190.677 |
| 44 | 4.383 | Mensualidad op. 4.383 | 3.728 | 2.852 | Servicios 712, Gastos adm. 108 | 655 | **31.425** | 225.830 | 194.405 |
| 45 | 4.383 | Mensualidad op. 4.383 | 3.642 | 2.766 | Servicios 712, Gastos adm. 108 | 742 | **32.166** | 230.213 | 198.047 |
| 46 | 4.383 | Mensualidad op. 4.383 | 3.565 | 2.661 | Servicios 712, Gastos adm. 141 | 818 | **32.984** | 234.596 | 201.612 |
| 47 | 4.383 | Mensualidad op. 4.383 | 3.820 | 2.949 | Servicios 712, Gastos adm. 108 | 563 | **33.547** | 238.980 | 205.433 |
| 48 | 4.383 | Mensualidad op. 4.383 | 3.652 | 2.784 | Servicios 712, Gastos adm. 108 | 732 | **34.279** | 243.363 | 209.084 |
| 49 | 4.383 | Mensualidad op. 4.383 | 4.277 | 2.517 | Servicios 712, Gastos adm. 990 | 106 | **34.385** | 247.746 | 213.361 |
| 50 | 4.383 | Mensualidad op. 4.383 | 3.586 | 2.710 | Servicios 712, Gastos adm. 108 | 797 | **35.182** | 252.130 | 216.947 |
| 51 | 4.383 | Mensualidad op. 4.383 | 3.562 | 2.697 | Servicios 712, Gastos adm. 108 | 821 | **36.004** | 256.513 | 220.509 |
| 52 | 4.383 | Mensualidad op. 4.383 | 3.640 | 2.766 | Servicios 712, Gastos adm. 108 | 743 | **36.746** | 260.896 | 224.150 |
| 53 | 4.383 | Mensualidad op. 4.383 | 3.495 | 2.623 | Servicios 712, Gastos adm. 108 | 889 | **37.635** | 265.280 | 227.645 |
| 54 | 4.383 | Mensualidad op. 4.383 | 3.665 | 2.786 | Servicios 712, Gastos adm. 108 | 718 | **38.353** | 269.663 | 231.310 |
| 55 | 4.383 | Mensualidad op. 4.383 | 3.616 | 2.746 | Servicios 712, Gastos adm. 108 | 767 | **39.120** | 274.046 | 234.926 |
| 56 | 4.383 | Mensualidad op. 4.383 | 3.840 | 2.963 | Servicios 712, Gastos adm. 108 | 544 | **39.664** | 278.430 | 238.766 |

«Otros pagos importantes» muestra los rubros de 100 UF o más. Los menores (servicios, gastos administrativos y reservas chicas) están incluidos en «Sale».

## Notas por mes

- **Mes 1:** Entra el capital. Es el saldo más alto de la implementación.
- **Mes 2:** Se compra el hardware (12.975). Sale casi el doble de lo que entra.
- **Mes 3:** Primer mes sin hito: solo pagos.
- **Mes 5:** Mes sin hito con sueldos altos (5.080).
- **Mes 7:** Empieza la racha de tres meses sin hito (7, 8 y 9).
- **Mes 9:** **Punto más bajo de la caja (414).** Este mes fija el tamaño del capital: con menos de 18.000 la caja quedaría negativa.
- **Mes 10:** Entra el Hito 4 y la caja se recupera.
- **Mes 12:** El mes de pagos más bajo de la implementación (1.509).
- **Mes 13:** Empieza el despliegue: los sueldos suben a 3.500–5.000 al mes.
- **Mes 15:** Mes sin hito en pleno despliegue.
- **Mes 16:** Empieza a pagarse la cuota del crédito (amortización).
- **Mes 17:** El flujo puro del proyecto (sin crédito) se vuelve positivo: «punto de equilibrio» de INDICADORES.
- **Mes 19:** Meses 19 y 20: el gasto más alto (~6.100) con poco cobro.
- **Mes 20:** Último mes de implementación, sin hito.
- **Mes 21:** Entra el Hito 12 y empieza la mensualidad de operación (4.383). Se compran adquisiciones de operación.
- **Mes 22:** Desde aquí solo entra la mensualidad. Los pagos (operación + cuota) casi la igualan, así que la caja queda plana en ~27.000.
- **Mes 39:** Última cuota del crédito.
- **Mes 40:** Sin cuota, los pagos bajan a ~3.600 y la caja vuelve a crecer unas 700 UF al mes.
- **Mes 56:** Cierre: 278.430 cobrados contra 238.766 pagados, con un saldo de 39.664.

## Preguntas probables

- **¿Por qué es negativo el mes 2 si los cobros acumulados (26.210) superan a los pagos (17.925)?** Porque esas cifras arrastran el capital del mes 1. En el mes 2 por sí solo entraron 8.210 y salieron 15.905.
- **¿Por qué el capital es 18.000?** Es el mínimo que mantiene la caja sobre cero en el peor mes (el mes 9) y cubre los intereses que se pagan antes de los hitos (clase FEP08: «financiar lo mínimo», 80 % banco y 20 % socios).
- **¿Por qué la caja queda plana entre los meses 22 y 39?** La mensualidad (4.383) casi iguala los pagos de operación más la cuota del crédito.
- **¿Se usa la línea de crédito?** No: la caja nunca baja de cero.
- **¿La tasa de descuento afecta la Curva S?** No. La curva usa montos nominales; la tasa (0,998 % mensual) solo se usa en el VAN.
