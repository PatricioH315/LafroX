# Pendientes fuera del Entregable 2 (Informe 3)

Notas internas. No citar ni entregar.

Excel revisado: `LafroX_ModeloFinanciero_3_20261113.xlsx`, versión de Álvaro de las 08:58 UTC del 13-11-2026. Sus cifras son idénticas a las del informe.

## Excel del equipo

1. **Protección y validación.** El E-21 exige proteger las fórmulas críticas y validar las celdas de entrada. Hoy ninguna de las 19 hojas está protegida, y solo MODELO PUNTOS CASO DE USO, GASTOS ADMINISTRATIVOS y COSTOS tienen validación de datos.
2. **Notas de FINANCIAMIENTO (filas 86 a 88).** Ya se borraron las notas «por validar» y «exigidos por el correo». Quedan dos:
   - F86 dice «Su monto debe justificarse mediante la necesidad de caja del proyecto», lo que suena a pendiente. Se puede reemplazar por «Capital de 18.000 UF, que cubre el déficit máximo del mes 9 con un saldo mínimo de 414,40 UF».
   - La fila 88 tiene «C86» en la columna A y un texto suelto en F88 («distribuir el financiamiento…»).
3. **Intune.** El T-11 indica 382 equipos al inicio y 433 en el año 3, pero el Excel carga 382 durante los 36 meses. Los 51 equipos adicionales costarían 3,88 UF por mes desde el año 3. El informe dice «parque inicial».
4. **B53 de ADQUISICIONES IMPLEMENTACIÓN** dice «sattelital».

Resuelto en la versión de las 08:58: el IVA de la celda J53 ya usa `PARAMETROS!C20`, y las fórmulas con valores incrustados de ADQUISICIONES OPERACION (C12 a C18) quedaron como valores de entrada.

Decisión: no se agregan al Excel los totales derivados que usa el informe (subtotales del cuadro maestro, IVA total, grupos de la sección 2.6).

## Subdocumento 7 (rama LafroX-Subdoc7-LateX-CORRIGIENDO)

5. **T-14, cuenta 8.1** (`formulario-t14/contenido.tex`, línea ~1072). Quitar «con 100 % de dedicación en los meses 21 a 56» del párrafo del gerente de servicio. El Excel le carga 651,85 HH en la Operación (684,44 UF), y la sección 2.6 del Entregable 2 usa esa cifra.

## Propuesta elegida: B+ (13-11-2026)

Avance:
- SD4 (commit `ec742eb1`, con push): Anexo 4-W.7 y decisión D48. PDF de anexos de 138 a 139 páginas; desde la página 117 se corren en 1 y ningún documento las cita.
- SD7 (commit `7ef0c419`, con push): T-14 (párrafo de la cuenta 8.1), T-15 (regla C, tablas 2, 3, 4, 4_personas, 7, 8, 10, perfiles, asignación y conciliación, totales del texto), cuerpo del SD7 (operación 54 %, totales y tab_SD7_13), generador `horas_por_rol_20261109.py` y scripts `aplicar_bplus_*`. T-14 de 167 a 168 páginas (desde la 105); nadie las cita. T-15, SD7, anexos y T-18 sin cambio de páginas.
- Revisión hacia atrás (13-11), todo con push:
  - SD8 `a245da20`: anexo de reservas con 199.219,03 / 196.147,03 HH; mismas 102 páginas, y las páginas del SD7 que cita siguen bien.
  - SD6 `73027e8d`: línea base del T-15 de 219.727,83 a 199.219,03 HH.
  - SD4 `82ef4a20` y SD7 `0304a94a`: el NOC nomina a los seis operadores del perfil NOC del T-15 (antes decía cinco); el T-15 explica las 1,9 horas-posición de la franja de 20 a 22 (1,33 h ÷ 70 %).
  - SD7 `ec054cfb`: deuda técnica de 8.2.4 de 1,7872 % a 2,1253 % de las HH de Operación (108.409,17).
  - Barrido final sin cifras antiguas en ninguna rama (salvo SD12, que no se revisa), aparte del Entregable 2.
- Excel del equipo revisado (Drive `LafroX_ModeloFinanciero_3_20261113.xlsx`, id 18wI3…, versión de las 22:05 UTC del 13-11): **alineado con el SD7**.
  - Horas: mesa y NOC calzan mes a mes con la regla del T-15 (38.246 y 21.748,2 HH de Operación); instructor +16 HH en el mes 21; total de perfiles 197.894,23 HH, igual al T-15; cada perfil suma lo mismo que en el T-15.
  - Tarifas: Mesa N1, NOC y SOC a **0,67 / 0,804** (no 0,667 / 0,80). Están dentro del E-26 y mantienen el factor 1,20. Las siete tarifas mínimas siguen con `MAX(F×1,2; mínimo)`.
  - Q y R de `COSTOS HH - SUELDOS` ahora suman por mes calendario (implementación 86.978,89 y operación 110.915,34 HH). El T-15 separa por fase de valorización (90.048,83 y 107.845,40). Los totales son iguales; el Entregable 2 tiene que decir cuál usa.
  - `FINANCIAMIENTO`: columna «Mes» nueva en la tabla de hitos (F8:F20), sin efecto en las referencias externas; nota F86 corregida; fila 88 limpia.
  - Resultado real: costo 194.487,71 UF (implementación 85.446,06; soporte 109.041,65); precio 228.763,92 (100.963,70; 127.800,22); margen 14,98 %; cuota 3.550,01; VAN sin impuestos 23.942,31 (antes 28.055,82), TIR 7,08 % mensual o 127,13 % anual (antes 7,79 % y 146,12 %); VAN del proyecto puro 7.890,33 y financiado 10.524,61; caja acumulada mínima 940,20 UF; crédito 15.200 e intereses 3.683,89.
  - Siguen pendientes en el Excel: Intune en 382 equipos los 36 meses (ítem 3); sin protección y con validación solo en 3 hojas (ítem 1). La nota F87 de `FINANCIAMIENTO` (línea de 1.250 UF al 3 % mensual) calza con la sección 2.3, que la deja como respaldo no usado.
- Entregable 2 actualizado (commit `4e85d307`, con push, rama `LafroX-OfertaEconomica-2-Latex`): 18 tablas regeneradas desde el Excel de Drive con un generador probado contra la versión de las 08:58 (reprodujo el informe anterior sin diferencias, salvo 1 peso de redondeo en dos subtotales en CLP); 58 cifras del texto; Curva S con la escala nueva; textos de B+ en 2.5 y 2.6 (mesa de 04:00 a 20:00, NOC compartido 100/75/50 %, tarifas de 0,67 / 0,804 UF/HH); 2.3 reescrita en el capital (19.000 UF, mínimo en miles) y en el flujo de la Operación (mes 22 negativo antes del crédito; flujo financiado negativo en 15 de los meses 21 a 39; caja mínima en esos meses 22.666,65 UF). 36 páginas, sin errores ni desbordes; el PDF no conserva ninguna cifra antigua. Ningún otro subdocumento cita estas cifras.
  - Scripts en el scratchpad de la sesión (`e2gen.py`, `golden.py`, `aplicar_e2.py`); no quedaron en el repositorio.
- Capital inicial: 19.000 UF en `PARAMETROS`!C54 (decidido el 13-11; crédito 15.200 y socios 3.800). Con 18.000, el saldo del mes 9 quedaba en −2,20 porque B+ baja 416,60 UF los hitos H1–H3; con 19.000 queda ≈ 940 UF y los intereses suben ≈ 194 UF en total. Actualizar la nota F86 de `FINANCIAMIENTO` y la sección 2.3 del Entregable 2.
- Sin verificar: `validar_local_sd7.py` (falta pypdfium2) y `contrastar_esfuerzo_capacidad_sd7.py` (ya fallaba antes por una etiqueta inexistente).

Componentes, en el orden en que se suman (ahorro marginal de costo / precio en UF):
1. P2, tarifas: Mesa N1, NOC y SOC a 0,667/0,80 UF/HH: −11.611,87 / −13.934,24 en Operación (más −1.439,20 / −1.727,04 en implementación).
2. P1, sin el tercer agente de mesa desde el mes 25: −14.161 HH, −9.440,67 / −11.328,80.
3. Refuerzo de peak: tercer agente solo en septiembre y diciembre, meses 32, 35, 44, 47 y 56: +2.176 HH, +1.450,67 / +1.740,80.
4. P6a, NOC compartido con la división 24×7 (dedicación declarada 100 % en el año 1, 75 % en el año 2 y 50 % en el año 3, solo con acta e indicadores sostenidos): −6.570 HH, −4.380 / −5.256.
5. P7b, el NOC atiende la mesa de 20:00 a 22:00 de lunes a sábado, con 272 HH de capacitación: −1.697,8 HH, −1.131,87 / −1.358,24.

Resultado (corregido el 13-11 al aplicar el SD7: en septiembre y diciembre el tercer agente cubre 15 horas y no 17, porque la franja de 20:00 a 22:00 es del NOC; −256 HH de mesa respecto de la primera cifra):
- HH de Operación 128.286,85 → 107.778,05 (mesa 38.246, NOC 21.748,2 con la formación de los operadores, instructor 16, SOC 26.280).
- Operación: costo 134.041,20 → ≈ 108.756,80; precio 157.799,51 → ≈ 127.458,23; cuota 4.383,32 → ≈ 3.540,51.
- Implementación: costo 86.834,70 → 85.395,50; precio 102.630,07 → 100.903,03.
- Proyecto: costo 220.875,90 → ≈ 194.152,30; precio 260.429,58 → ≈ 228.361,26; margen 15,19 % → ≈ 14,98 %.
- Costo medio de Operación por año: 3.800 / 3.676 / 3.697 → ≈ 3.288 / 2.939 / 2.839 UF/mes. Equivalentes: 22,6 / 22,1 / 22,2 → ≈ 20,7 / 18,3 / 17,3.
- T-15 (SD7) con B+: línea base 219.727,83 → 199.219,03 HH; Operación 128.917,97 → 108.409,17 HH; 8.1.1 = 21.764,2 (perfil 30: 21.748,2, perfil 22: 16); 8.1.2 = 38.246.
- Fuera de B+ (decidir aparte): faltantes por Bases del ítem 14.
- Detalle de cada componente y cambios por documento: ítems 6, 9, 13, 16 y 18.

## Reducción de HH de Operación (por concretar, 13-11-2026)

Estado: analizada, sin aplicar. Orden acordado: primero el subdocumento que dimensiona (SD4), después SD7, el Excel y al final el Entregable 2.

6. **Quitar el tercer agente de mesa desde el mes 25.** Factible.
   - Origen: Anexo 4-W del SD4 (rama `LafroX-Subdoc4-LateX-corrigiendo`, `04/anexos/fisica/16_anexo_4b_memoria_calculo.tex`, dimensión 16 de la tabla, línea ~34, y paso 4 de la sección «Dimensiones 15–16», líneas ~284–287). El mismo anexo calcula que 2 agentes fuera de la hora cargada cubren hasta 2.283 contactos al mes, y la demanda del año 3 es 2.258. El tercer agente es margen, no requisito.
   - Cambio: 2 agentes en las 17 horas fuera de la hora cargada durante toda la Operación (41 horas-posición por día de lunes a sábado en vez de 58), y el agente extra pasa a ser un disparador: se activa si la recalibración trimestral del Erlang C, que el anexo ya declara, muestra que los contactos superan el límite. Dotación: 17 personas en operación normal y 19 en peak desde el mes 25 (antes 19 y 21).
   - Efecto calculado sobre el calendario del modelo (mes 25 = febrero de 2029 a mes 56 = septiembre de 2031, 833 días de lunes a sábado × 17 h): −14.161 HH de Operador de Mesa N1, −11.328,80 UF de costo y −13.594,56 UF de precio.
   - Cifras resultantes: HH de Operación 128.286,85 → 114.125,85; HH del proyecto 218.403,03 → 204.242,03; costo 220.875,90 → 209.547,10 UF; precio 260.429,58 → 246.835,02 UF; margen 15,19 % → 15,11 %; cuota mensual ≈ 4.383,32 → 4.005,69 UF, si la rebaja se reparte igual en las 36 cuotas.
   - Riesgo: si los contactos reales pasan de 2.283 al mes, la mesa baja del 80 % de llamadas contestadas antes de 20 segundos (RT-21.06) y hay descuentos por nivel de servicio. Además, el Erlang C no verifica el abandono ≤ 5 % ni la resolución al primer contacto ≥ 70 %. El costo del agente extra, si se activa, lo pone LafroX (precio fijo).
   - Dónde cambiar después del SD4: SD7, T-15 paquete 8.1.2 (54.239 → 40.078 HH, `formulario-t15/tablas/tab_T15_asignacion_partidas.tex`, línea ~210), fila del Operador de Mesa N1 en `tab_T15_perfiles_internos.tex` y totales de T-15 y del subdocumento 7; en la rama `LafroX-Subdoc7-LateX`, `tab_T15_8.tex` dice «el tercer agente de la mesa se suma desde el mes 25». Excel: valores fijos de la fila Operador de Mesa N1 en `HH POR ROL Y MES` (meses 25–56) y `COSTOS HH - SUELDOS!E40`. Entregable 2: secciones 2.1, 2.2, 2.3, 2.5 y cuadro maestro.

7. **NOC y SOC con un solo puesto entre el sábado a las 14:00 y el domingo a las 22:00.** Posible pero no recomendado.
   - Ahorro: 156 sábados × 10 h + 157 domingos × 22 h = 5.014 HH. Quitando horas del NOC: −4.011,20 UF de costo y −4.813,44 UF de precio. Quitando horas del SOC: −3.509,80 y −4.211,76 UF.
   - En contra: el domingo es la «única ventana amplia de intervención semanal» del caso (Caso 02, calendario operacional), así que es cuando el NOC acompaña los cambios. RT-21.01 y RT-11.17 piden NOC y SOC 24×7 por separado, y SD4, T-14 (8.1.1 y 8.1.5) y T-15 declaran un puesto 24×7 para cada uno.

9. **Mesa N1, NOC y SOC a la tarifa mínima del E-26.** Evaluado, sin decidir. Hoy: Mesa N1 y NOC (TIC) a 0,8/0,96 UF/HH y Analista SOC (Ingeniero Senior) a 0,7/0,84. Mínimos del E-26: TIC 0,6–1,0 de costo y 0,8–1,5 de tarifa, Ingeniero Senior 0,6–0,8 y 0,8–1,2. Las tres tarifas quedan en 0,8 UF/HH. Sobre las 121.967 HH de los tres perfiles (implementación y operación):
   - **Criterio elegido (13-11):** bajar costo y tarifa juntos, con el factor 1,20. Costo 0,8 ÷ 1,2 = 0,667 y tarifa 0,80 para los tres perfiles. −13.051,07 UF de costo y −15.661,28 UF de precio. Costo 207.824,83, precio 244.768,30, margen 15,09 %, costo medio de Operación 3.724 → 3.402 UF/mes y cuota ≈ 3.996 UF.
   - Combinado con el ítem 6: −22.491,73 UF de costo y −26.990,08 UF de precio. Costo 198.384,17, precio 233.439,50, margen 15,02 %, costo medio de Operación 3.140 UF/mes y cuota ≈ 3.682 UF.
   - Descartado: dejar el costo en 0,6 con la tarifa en 0,8. Sube el factor a 1,33 y el margen a 18,42 % sin bajar más el precio.
   - Opción para bajar más, sin decidir: clasificar al Operador de Mesa N1 como Analista / Diseñador Junior (costo 0,3–0,6 y tarifa 0,5–0,8 en el E-26), a 0,5/0,6. Con el NOC y el SOC a 0,667/0,8: −23.034,90 UF de costo y −27.641,88 UF de precio, margen 15,01 %. Con el ítem 6: costo 190.760,50, precio 224.291,10, margen 14,95 %, costo medio de Operación 2.954 UF/mes y cuota ≈ 3.459 UF. Hay que justificar que el N1 (recepción, registro, clasificación, soluciones básicas y derivación) calza con esa categoría.
   - La categoría y el costo de cada perfil se declaran en el T-15 del SD7 (`tab_T15_perfiles_internos.tex`); el cambio parte ahí.

10. **Paquete de propuestas para bajar la Operación (13-11).** Las tarifas siempre con el factor 1,20 sobre el costo y dentro del E-26. Sin aplicar.
   - P1: ítem 6, sin el tercer agente (−14.161 HH).
   - P2: ítem 9, Mesa N1, NOC y SOC a 0,667/0,80.
   - P3: el resto de los perfiles con horas en Operación, al mínimo del E-26 con factor 1,20 (JP 1,25/1,50; líderes que son Jefe de TIC, de Desarrollo o de Análisis 0,833/1,00; Ingeniero Senior 0,667/0,80; Ingeniero Junior 0,50/0,60; Asistente de Terreno 0,667/0,80, etc.). Sin cambio en DevOps, Datos, QA Experto y Senior ni en el Encargado de Seguridad, porque ya están en la tarifa mínima. En la Operación solo ahorra −1.164,33 UF de costo y −1.397,20 UF de precio; en el proyecto, −5.173,19 y −6.207,83, porque baja también la implementación. No recomendado: aporta poco y deja a jefaturas y líderes en el piso.
   - P4: ítem 9, opción de clasificar la Mesa N1 como Analista Junior a 0,5/0,6.
   - Resultados (HH de Operación | costo de Operación por mes | cuota | precio del proyecto | margen):
     - Actual: 128.286,85 | 3.724,34 | 4.383,32 | 260.429,58 | 15,19 %
     - P1: 114.125,85 | 3.409,65 | 4.005,69 | 246.835,02 | 15,11 %
     - P2: 128.286,85 | 3.401,79 | 3.996,26 | 244.768,30 | 15,09 %
     - P1 + P2: 114.125,85 | 3.139,55 | 3.681,57 | 233.439,50 | 15,02 % (recomendado)
     - P1 + P2 + P3: 114.125,85 | 3.107,21 | 3.642,76 | 227.231,67 | 14,97 %
     - P1 + P2 + P4: 114.125,85 | 2.954,00 | 3.458,91 | 224.291,10 | 14,95 %
   - Supuesto: la rebaja de precio de la Operación se reparte igual en las 36 cuotas. No se recalcularon el VAN, la TIR, la Curva S ni el financiamiento.
   - **Decisión del 13-11: P1 + P2. P4 queda como cambio posible.** Separado por fase (base: tabla de márgenes de la sección 2.1):
     - Implementación: costo 86.834,70 → 85.395,50 (−1.439,20) y precio 102.630,07 → 100.903,03 (−1.727,04), por las horas de marcha blanca de los tres perfiles.
     - Operación: costo 134.041,20 → 112.988,66 (−21.052,54) y precio 157.799,51 → 132.536,47 (−25.263,04). HH 128.286,85 → 114.125,85.
     - Tarifas por hora: Mesa N1 y NOC (TIC) 0,80/0,96 → 0,667/0,80; Analista SOC (Ingeniero Senior) 0,70/0,84 → 0,667/0,80. Dentro del E-26 (TIC 0,6–1,0 y 0,8–1,5; Ingeniero Senior 0,6–0,8 y 0,8–1,2).

12. **Estudio de viabilidad de P5 (13-11). Reemplaza las cifras del ítem 11.**
   - ¿Hay subcontratados? En el modelo no. El SD4 (Anexo 4-W) dice que el NOC y el SOC son propios de LafroX y operan desde Valparaíso: el NOC «con la división de NOC 24×7 de LafroX» y el SOC «con analistas contratados antes del mes 13». El T-15 pone a la mesa, el NOC y el SOC en perfiles internos, y el Excel los carga como HH. Terceros solo hay en PROVEEDORES (AWS, internet, CrowdStrike, Intune, custodia, mapas y mensajería) y en dos paquetes puntuales del T-15 (3.8.6 y 5.4.4).
   - Puesto único NOC + SOC «año 3 fuera de L–V 8–20»: **no viable**. Cubre la noche de lunes a sábado (preparación de 22:00 a 06:00) y el despacho de 05:30 a 07:00, que el caso declara con «indisponibilidad cero» (RT-10.05). El sábado hasta las 14:00 también es operativo.
   - Versión viable: puesto único solo en el valle, sábado de 14:00 a domingo a las 22:00 (años 2 y 3), más lunes a viernes de 20:00 a 22:00 en el año 3. Condiciones: lo cubre el Analista SOC con formación cruzada en NOC; un especialista de guardia declarada; en las ventanas de cambio del domingo, el SRE que ejecuta el cambio está de turno. −3.850 HH, −2.566,67 UF de costo y −3.080 UF de precio.
   - Mesa de 7 a 6 agentes en la hora cargada desde el mes 33: viable si la recalibración confirma 2,0 contactos por persona. Bajar a 5 (1,5 contactos) no es creíble con la rotación de 38 % al año del turno de noche (Caso 02, entrevista del jefe de bodega). −626 HH, −417,33 UF de costo y −500,80 UF de precio.
   - Con P1 + P2: 3.296 → 2.941 → 2.933 UF/mes. Baja en el año 2 y después se queda plana.
   - P6, NOC compartido con la división 24×7 de LafroX (dedicación declarada del puesto: 100 % en el año 1, 75 % en el año 2 y 50 % en el año 3; RT-21.03 pide «dedicación declarada», no exclusiva). −6.570 HH, −4.380 UF de costo y −5.256 UF de precio. Con P1 + P2 y la mesa a 6: 3.296 → 2.912 → 2.811 UF/mes, −4.797,33 UF de costo y −5.756,80 UF de precio. Es la que más hace bajar la curva. Riesgo: hay que declarar el centro multicliente y la dotación por turno (RT-21.01).
   - Para una curva que siga el volumen hay que subcontratar con precio variable (mesa con un operador acreditado, RT-21.05; SOC gestionado, RT-11.17). Falta cotizar. Límites: hasta 40 % del valor del contrato, con autorización del CLIENTE (Art. 73.1); sin externalizar el núcleo (73.2); acuerdo de tratamiento de datos (73.4). Mesa, NOC y SOC en la Operación, tras P1 + P2, son 74.110 UF, el 31,7 % del precio.

13. **Viabilidad de P6, NOC compartido (13-11): viable con condiciones, no al 100 %.**
   - A favor: el SD1 (rama `LafroX-Subdoc1-LateX-CORRIGIENDO`, `contenido.tex`, líneas ~55–59 y ~123–138) declara un NOC corporativo multicliente en Valparaíso: 32 profesionales, 6 puestos activos y 2 de relevo, 4 equipos de 7 (responsable de turno, 5 operadores y 1 relevo). El SD4 ya dice que el NOC del proyecto lo cubre esa división. RT-21.03 pide «dedicación declarada», no exclusiva, y en cada turno hay 5 operadores, más cobertura que un puesto dedicado.
   - En contra: el SD4 (Anexo 4-W, dimensión 16) y el T-15 (8.1.1, 26.280 HH) declaran hoy un puesto dedicado. RT-21.01 pide declarar la dotación por turno. Los porcentajes 75 % y 50 % hay que justificarlos (menos alertas tras la estabilización, alertamiento automático de RT-14.04) y amarrarlos a una condición: si no se cumplen los niveles de servicio, se vuelve al 100 % por cuenta de LafroX. La mesa a 6 depende de que los contactos bajen.
   - Incoherencia aparte: el SD1 declara una mesa corporativa de 7 puestos y 1 de reserva, y el proyecto solo pide 7 agentes en la hora cargada y 9 en el peak.

14. **Dotación de la implementación (13-11): faltan horas, sobre todo por los roles mínimos de BTT 19.2.**
   - BTT 19.2 exige 100 % en la implementación al Jefe de Proyecto, al Líder de Desarrollo y al Líder Funcional. El Excel les carga 1.339 HH (0,42 equivalentes), 1.610 HH (cero en los meses 1–4 y 10–12) y 144 HH (cero en 17 de los 20 meses). Art. 70.3 de las Bases Administrativas: Jefe de Proyecto «con dedicación exclusiva». BTT 19.2 también exige que la dotación sea coherente con el T-15 y con la curva de recursos. El T-15 (`contenido.tex`, línea 295) dice que esos roles «conservan sus dedicaciones», pero cuenta sus horas solo en los paquetes.
     - Brecha a 128 HH al mes (el tope de 80 % que usa el modelo): +4.586,80 HH, +5.304,51 UF de costo y +6.365,41 UF de precio. A 160 HH al mes: +7.576,51 UF de costo y +9.091,81 UF de precio.
   - Roles «permanentes» con meses en cero: Líder de Integración (7 meses), Líder de Datos (meses 16–20), Líder de Calidad (15 meses en implementación y 35 en Operación), Encargado de Seguridad (meses 11–20 y 27 en Operación) y Líder de Operación / SRE (desde el mes 6: 11 meses en implementación y 9 en Operación). Con un piso de 16 HH en esos meses: implementación +784 HH (+699,20 UF de costo y +890,88 de precio); Operación +1.136 HH (+962,40 y +1.277,44).
   - Huecos técnicos en los peaks (dimensionamiento indicativo, a fijar en el T-15):
     - Mes 12, certificación de la Etapa 1 (H5): total de 7,2 equivalentes, QA 0,2 y desarrollo 0. Corregir defectos de UAT, carga y resiliencia: 2 Back-end Senior y 1 QA Senior en los meses 11–12.
     - Meses 13–20, marcha blanca, H7, Etapa 2 y H11–H12: DevOps/SRE en 0–0,4. Agregar 1 DevOps Senior.
     - Meses 16–20: Datos en 0 justo antes del corte de la Etapa 2. Agregar 1 Ingeniero de Datos Senior en los meses 19–20.
     - Total: +2.048 HH, +1.510,40 UF de costo y +1.863,68 UF de precio.
   - En los peaks (mes 5: 43,9 equivalentes; meses 16, 19 y 20: alrededor de 40), varios perfiles ya están en el tope de 80 % de sus plazas (Back-end Senior 7,2 de 9). No queda holgura sin agregar plazas.
   - Suma indicativa de la implementación: +7.418,80 HH, +7.514,11 UF de costo y +9.119,97 UF de precio.
   - Ojo con el ítem 5: quitar el «100 % de dedicación» del gerente de servicio choca con BTT 19.2 (Líder de Operación / SRE «permanente en Operación») y con RT-21.02 («gerente de servicio dedicado»). Hoy tiene 651,85 HH en 36 meses. Al 50 %: +1.652,10 HH, +1.734,70 UF de costo y +2.081,65 de precio. Al 100 %: +3.956,10 HH, +4.153,90 y +4.984,69.

15. **Por qué hay unas 20 personas en la Operación (13-11).** Equivalentes a 160 HH al mes, promedio por año de Operación:
   - Hoy: mesa 8,8/9,7/9,7, NOC 4,6, SOC 4,6, resto 4,7/3,2/3,3; total 22,6/22,1/22,2.
   - P1 + P2: 20,7/19,3/19,4. Con P6 y la mesa a 6: 20,7/18,0/17,0.
   - Un puesto 24×7 son 168 h a la semana: con 40 h por persona, unas 5 personas por puesto. NOC y SOC son 2 puestos 24×7, unas 10 personas. La mesa son 41 horas-posición al día de lunes a sábado (2 agentes de 04:00 a 22:00 y 7 en la hora cargada), unas 7 personas.
   - Trabajo real de la mesa: 2.000 contactos × 10 min = 333 h al mes (2,1 equivalentes; 376 h con 2.258 contactos). Con P1 se pagan 1.113 h al mes: ocupación de alrededor de 30 %. Se paga la disponibilidad que exigen las Bases (80 % en 20 s, RT-21.06, y horario con la ventana operacional, RT-21.07), no el trabajo.
   - P7 (idea, sin evaluar a fondo): mesa compartida con la mesa corporativa de LafroX del SD1, cobrando al proyecto su trabajo real con una ocupación objetivo de 70 %. ≈ 476 h al mes (537 en el año 3), unas −22.200 HH, ≈ −14.800 UF de costo y ≈ −17.760 UF de precio. Problemas: la mesa del SD1 tiene solo 7 puestos y 1 de reserva; RT-21.14 pide el Erlang C con el volumen proyectado; hay que reescribir el Anexo 4-W. El SOC no se puede compartir: el SD1 (rama CORRIGIENDO) no declara un SOC corporativo, así que queda dedicado o subcontratado.

16. **Evaluación de P7, mesa compartida (13-11): no viable en su versión completa.**
   - El SD1 (rama CORRIGIENDO, `contenido.tex`, línea ~59) dice que los agentes de la mesa corporativa «se dimensionan para cada servicio contratado»: los puestos se comparten, los agentes no. No hay un grupo de agentes compartido ni volumen de otros clientes declarado. El ahorro de ≈ 14.800 UF solo sería real si otros clientes absorben las horas ociosas; si no, el costo sigue existiendo y la oferta queda subvalorada.
   - RT-21.14 pide dimensionar con Erlang C «a partir del volumen de contactos proyectado del caso». Un grupo compartido exige declarar el volumen de otros clientes que nadie conoce. RT-21.08 y RT-21.06 (resolución al primer contacto ≥ 70 %) piden conocer la operación de Puelche, y la rotación de 38 % del turno de noche lo hace más difícil.
   - Capacidad física: la mesa del SD1 tiene 7 puestos simultáneos y Puelche usa 7 en la hora cargada.
   - El mínimo de 2 agentes no se puede bajar: con 1 agente y 3,98 contactos por hora, solo un 34 % se contesta antes de 20 s y la espera media es de 19,7 min. Con 2 agentes: 84 % y 1,2 min.
   - Parte viable, P7b: el NOC corporativo (32 personas, 6 puestos 24×7) atiende la mesa de 20:00 a 22:00, de lunes a sábado, cobrando el trabajo real con 70 % de ocupación (1,33 h de trabajo al día → 1,9 h cobradas, en vez de 4). −1.974 HH, −1.316,18 UF de costo y −1.579,41 UF de precio. Condición: formación funcional del NOC en los procesos de Puelche.
   - Alternativa real: subcontratar la mesa a un centro de atención acreditado (RT-21.05), que sí trabaja con un grupo de varios clientes. Umbral: con P1 + P2 la mesa cuesta 742 UF al mes (≈ 0,371 UF, unos $14.840 por contacto con 2.000 contactos). Una cotización bajo eso ahorra. Hay que cambiar el SD1 (mesa propia), el SD4 y el T-15, y cumplir el Art. 73 (≤ 40 % del contrato, autorización, acuerdo de datos).

17. **Propuestas ordenadas por viabilidad y conjuntos (13-11).** Las cifras de los conjuntos no cuentan dos veces el mismo ahorro y ya incluyen las capacitaciones estimadas.
   - Orden: 1) P2 tarifas (alta); 2) P1 tercer agente (alta); 3) P6a NOC compartido 100/75/50 % (media-alta); 4) P7b NOC atiende la mesa de 20 a 22 (media); 5) P6b mesa a 6 desde el mes 33 (media-baja, depende de los contactos medidos); 6) P4 mesa como Analista Junior (baja-media); 7) P5 puesto único NOC + SOC en el valle del fin de semana (baja; se solapa con P6a y choca con la ventana de cambios del domingo). P3 fuera de los conjuntos (aporta poco y afecta la implementación). Descartados: P7 completo, NOC + SOC en las noches, mesa a 5 agentes. Por cotizar: mesa subcontratada y SOC gestionado.
   - Capacitación estimada: P7b, 8 operadores NOC × 16 h + instructor al inicio (144 HH) y repaso de 64 HH en los meses 33 y 45 (≈ 181 UF de costo). P5, formación cruzada de 6 analistas SOC × 24 h + instructor (168 HH, ≈ 112 UF).
   - Conjuntos (HH de Operación | costo / precio de Operación | cuota | costo medio por año de Operación | equivalentes por año | precio del proyecto | margen):
     - A seguro, P1 + P2: 114.126 | 112.989 / 132.536 | 3.682 | 3.296 / 3.051 / 3.072 | 20,7 / 19,3 / 19,4 | 233.440 | 15,02 %
     - B recomendado, A + P6a + P7b: 105.858 | 107.477 / 125.922 | 3.498 | 3.268 / 2.896 / 2.796 | 20,5 / 17,9 / 16,8 | 226.825 | 14,97 %
     - C condicionado, B + P6b: 105.232 | 107.059 / 125.421 | 3.484 | 3.268 / 2.879 / 2.778 | 20,5 / 17,7 / 16,6 | 226.324 | 14,97 %
     - D máximo, C + P5 + P4: 103.320 | 99.835 / 116.752 | 3.243 | 3.100 / 2.655 / 2.568 | 20,5 / 17,1 / 16,2 | 216.522 | 14,89 %
   - Implementación: A, B y C 85.396 / 100.903 (por P2); D 84.452 / 99.770 (P4 también baja la marcha blanca).
   - Los conjuntos no incluyen lo que exigen las Bases y falta (ítem 14): gerente de servicio (+1.734,70 UF al 50 %), pisos de los roles permanentes en Operación (+962,40) e implementación (+7.514,11).

18. **Estudio del conjunto B (13-11): viable; se recomienda la variante B+.**
   - Respaldo que ya está en los documentos:
     - T-15 (`contenido.tex`, línea 275): si un indicador de la mesa no se cumple dos meses seguidos, «se aumenta la dotación de la franja afectada». Es el disparador que necesita P1.
     - SD7, riesgo P7-07 (`subdocumento-07-anexos/tablas/tab_7F1.tex`): «Decremento sólo con acta e indicadores sostenidos». Así hay que plantear P6a.
     - SD1: NOC multicliente de 32 personas.
   - Hueco detectado: el Anexo 4-W modela 2.000 contactos fijos y no considera más contactos en septiembre, cuando las entregas suben de 1.400 a 2.600. Con P1 y una holgura de 1,1 %, septiembre es el mes de riesgo. **B+** mantiene el tercer agente solo en septiembre y diciembre desde el mes 25 (meses 32, 35, 44, 47 y 56): +2.176 HH, +1.450,67 UF de costo y +1.740,80 UF de precio. Son solo esos 5 meses, no continuos. Variantes: solo septiembre (meses 32, 44 y 56) +1.292 HH, +861,33 UF de costo y +1.033,60 de precio; solo del 1 al 25 de septiembre +1.088 HH, +725,33 y +870,40. Hay que planificarlo de antemano porque el disparador del T-15 actúa después de dos meses de incumplimiento, y el peak de septiembre dura 25 días. Como referencia, el tercer agente original costaba 9.440,67 UF (meses 25–56, a la tarifa de P2).
   - El anexo no dice cuál es la hora cargada. P7b supone que no cae entre las 20:00 y las 22:00, y hay que declararlo.
   - Multas (Art. 80): no hay multa directa por el 80 % en 20 s de la mesa. Respuesta o resolución fuera de plazo: 5 UF por incidente crítico y 2 UF por alto. Incumplir los niveles de servicio tres meses seguidos es causal de término (Art. 81).
   - Cifras:
     - B: HH de Operación 105.858; Operación 107.477 / 125.922 UF; cuota 3.498; 3.268 / 2.896 / 2.796 UF/mes; proyecto 192.872 / 226.825, margen 14,97 %.
     - B+: HH 108.034; Operación 108.927,67 / 127.662,80; cuota ≈ 3.546; ≈ 3.292 / 2.944 / 2.845 UF/mes; proyecto 194.322,67 / 228.565,80, margen ≈ 14,98 %.
   - HH por paquete (B): 8.1.2 Mesa N1 54.239 → 36.326 (B+: 38.502); 8.1.1 NOC 26.280 → 21.492,2 (19.710 compartido + 1.782,2 de la mesa de 20 a 22); capacitación del NOC +272 HH; 8.1.5 SOC sin cambio en HH (solo tarifa).
   - Cambios por documento, en orden:
     - SD4, Anexo 4-W (rama corrigiendo): dimensiones 15 y 16 de la tabla (líneas 33–34), pasos 3 y 4 y párrafo de dotación (líneas ~281–287). Sacar el tercer agente desde el mes 25 salvo en septiembre y diciembre; la franja de 20 a 22 la atiende el NOC; dedicación declarada del NOC 100/75/50 % con acta e indicadores; declarar la hora cargada; nueva dotación total.
     - SD7: T-14 8.1.1 y 8.1.2 (`contenido.tex`, líneas 595, 597 y 1074; `tab_T14_45.tex`); T-15 8.1.1 y 8.1.2 en `tab_T15_asignacion_partidas.tex` (209–210), `tab_T15_2.tex` (203–204) y `tab_T15_10.tex` (38–39); perfiles 17, 30 y 31O en `tab_T15_perfiles_internos.tex` (HH y 0,667/0,80); `contenido.tex`, líneas 117 y 150, y SD7 `contenido.tex`, línea 403 (totales). `formulario-t18`, línea 234 (soporte puente), solo si cambia la mesa antes del mes 21.
     - Excel: `HH POR ROL Y MES` (Mesa N1 y NOC, meses 21–56), `COSTOS HH - SUELDOS` (F/G de las filas 40, 41 y 44) y capacitación en `COSTOS`, filas 55–58.
     - Entregable 2: secciones 2.1, 2.2, 2.3, 2.5, 2.6 y cuadro maestro.
   - No incluye los faltantes por Bases del ítem 14.

11. **P5, curva de Operación a la baja (sin decidir; cifras corregidas en el ítem 12).** Con P1 + P2 el costo medio queda en 3.296, 3.051 y 3.072 UF/mes en los años 1, 2 y 3: más bajo, pero plano. Para que baje:
   - NOC y SOC con un solo puesto (operador integrado, con escalamiento a los especialistas de guardia): en el año 2 (meses 33–44) solo sábados y domingos; en el año 3 (meses 45–56) todo lo que queda fuera de lunes a viernes de 8:00 a 20:00. −8.124 HH, −5.416 UF de costo y −6.499,20 UF de precio.
   - Mesa: la hora cargada baja de 7 a 6 agentes en el año 2 y a 5 en el año 3, si la recalibración trimestral del Erlang C confirma que los contactos bajan de 2,5 a 2,0 y a 1,5 por persona al mes. −939 HH, −626 UF de costo y −751,20 UF de precio. Las otras 17 horas siguen con 2 agentes: ese mínimo se mantiene aunque bajen los contactos.
   - Resultado con P1 + P2: 3.296 → 2.895 → 2.724 UF/mes (años 1, 2 y 3), promedio de 2.972 UF/mes, −6.042 UF de costo y −7.250,40 UF de precio.
   - Riesgo: en el año 3 el puesto único cubre también la noche, que es la ventana crítica (preparación de 22:00 a 06:00, despacho desde las 05:30), y RT-21.01 y RT-11.17 piden NOC y SOC 24×7. Hay que declarar el centro integrado, la dotación por turno y la guardia de especialistas («turnos de disponibilidad declarados», RT-14.04). Variante más segura: solo fines de semana en los años 2 y 3.
   - Otras palancas sin cuantificar: compromisos de consumo en AWS desde el año 2 (Aurora es 111,14 UF de los 368,92 UF/mes de nube; el paquete 8.4.2 de FinOps ya existe), y SOC fuera de horario subcontratado (RT-11.17 lo permite; falta cotizar).

8. **Descartado:** compartir NOC y SOC todas las noches (≈16.800 HH). La noche es la ventana crítica del caso: preparación de 22:00 a 06:00 y despacho de 05:30 a 07:00 (RT-10.05 del caso).
