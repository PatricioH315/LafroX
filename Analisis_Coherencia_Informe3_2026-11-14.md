# Análisis de coherencia — Informe 3 (14-11-2026, noche)

Uso interno. No citar ni entregar.

## Qué se revisó

| Fuente | Versión revisada |
|---|---|
| SD1 | `LafroX-Subdoc1-LateX-CORRIGIENDO` 278a4c41 (14-11 19:27) |
| SD2 | `LafroX-Subdoc2-LateX-CORRIGIENDO` a72407bc (08-11) |
| SD3 / T-12 | `LafroX-Subdoc3-LateX-CORRIGIENDO` 00404b4f (14-11 20:38) |
| SD4 / T-11 | `LafroX-Subdoc4-LateX-corrigiendo` 2d508f46 (14-11 19:27) |
| SD5 | `LafroX-Subdoc5-LateX-CORRIGIENDO` e11af658 (14-11 21:38, Bastián) |
| SD6 / T-9 / T-10 | `LafroX-Subdoc6-LateX-corrigiendo` b18698ec (14-11 20:07) |
| SD7 / T-14 / T-15 / T-18 | `LafroX-Subdoc7-LateX-CORRIGIENDO` 68669bef (14-11 20:36) |
| SD8 / T-16 | `Lafrox_Subdocumento_8_Latex_Revision` 629a9566 (14-11 21:28, Max) |
| SD9 / T-13 / T-17 | `LafroX-Subdoc9-LateX-corrigiendo` 24e243d4 (14-11 20:42) |
| SD13 / T-19 | `LafroX-Subdoc13-LateX-corrigiendo` dd509aa1 (09-11) |
| Entregable 2 | `LafroX-OfertaEconomica-2-Latex` 68595089 (14-11 21:18) |
| Anexo A (trazabilidad Art. 46) | `LAFROX-Subdocumentos-Anexos` bf1614de |
| Excel | `LafroX_ModeloFinanciero_3_20261113.xlsx` (Drive 18wI3…), última versión de Álvaro, 15-11 00:50 UTC (21:50 hora local del 14-11), recalculada con Excel |

Contraste: Bases Administrativas (E-21, E-24, E-25, E-26, arts. 35–38), correo de aclaraciones del 01-11 y diapositivas FEP08 del 12-11.

Método: lectura de fórmulas y valores del Excel recalculado, búsqueda de cada cifra del E2 en las celdas del Excel, texto de los 33 PDF compilados de las ramas y cruces dirigidos (HH, plazas, hitos, dotación, equipos, riesgos, innovaciones, nombres).

---

## 1. Críticos: bloquean la entrega

### C1. El E2 ya no coincide con el Excel

Álvaro modificó el Excel después del último commit del E2 (E2 a las 21:18; Excel a las 21:39 y 21:50). Enlazó el bloque de horario de los ambientes de prueba (`ADQUISICIONES IMPLEMENTACIÓN` O8:Z45) a `COSTOS!C63:V63`. El E-21 exige que los valores de los tres documentos sean idénticos, y cualquier discrepancia descalifica.

| Cifra | E2 (commit 68595089) | Excel actual |
|---|---|---|
| Costo total | 200.024,98 | **199.911,43** |
| Costo implementación | 88.884,92 | **88.771,38** |
| Servicios de proveedores, implementación | 4.472,14 | **4.358,60** |
| Implementación servicios (cuadro por ítem) | 8.064,61 | **7.951,07** |
| Margen total | 35.283,66 (14,99 %) | **35.397,21 (15,04 %)** |
| Margen implementación | 16.208,45 | **16.322,00** |
| VAN sin impuestos | 24.691,13 | **24.793,00** |
| TIR mensual / anual | 7,13 % / 128,44 % | **7,16 % / 129,36 %** |
| Caja mínima (mes 9) | 489,87 | **537,47** |
| Saldo final | 35.399,78 | **35.513,32** |
| Precio | 235.308,64 | 235.308,64 (sin cambio, ver C2) |

Afecta las secciones 2.1, 2.2 (flujo anual y mensual, sensibilidad), 2.3 (texto, tabla y figura). Las secciones 2.5 y 2.6 (Operación) no cambian.

### C2. En el Excel, el costo de los ambientes cambió pero su precio no

- `COSTOS!D63:V63` (Sites Cloud, implementación) = `I13 − I9 + SUMIF(bloque de horario)` → 494,96 UF en los meses 2–20.
- `INGRESOS!D80:V80` sigue en `='ADQUISICIONES IMPLEMENTACIÓN'!I13*(1+$B$77)` → 35,23 UF fijos por mes, 669,36 UF.
- Esa línea queda con un recargo de 35 % en vez del 10 % que se declara para adquisiciones y servicios. Por eso el precio no se movió y el margen subió.
- Corrección: que `INGRESOS!D80:V80` tome `COSTOS!D63:V63*(1+$B$77)`, igual que la fila 87 de innovaciones. El precio baja unos 125 UF.

### C3. El bloque de ambientes cuenta la mitad de las horas

- `ADQUISICIONES IMPLEMENTACIÓN!W8` = `NETWORKDAYS(...)*12*(PARAMETROS!C69-PARAMETROS!C68)`. C69 − C68 = 20:00 − 08:00 = 0,5 día, así que la fórmula da 6 horas por día hábil (138 h en marzo de 2027, con 23 días hábiles). Con encendido de 08:00 a 20:00 son 12 horas: el factor debe ser 24, no 12.
- Con 12 h/día, el costo de cómputo de los ambientes sube de 349,70 a 680,76 UF (+331 UF de costo, +364 UF de precio con el 10 %). Queda incluso sobre los 463,25 UF que tenía la versión fija anterior.
- `PARAMETROS!C70` («Meta de reducción de horas de cómputo», 0,6) no lo usa ninguna fórmula. Si la idea era aplicarla, falta; si no, sobra.
- Hay que decidir esto **antes** de regenerar el E2; si no, se regenera dos veces.

### C4. El Excel no tiene protección ni validación

El E-21 exige validar las celdas de entrada y proteger las fórmulas críticas, y el correo del 01-11 dice que estas exigencias rigen desde el Informe 3. Hoy ninguna de las 19 hojas está protegida, y solo tres tienen validación de datos (MODELO PUNTOS CASO DE USO 3, GASTOS ADMINISTRATIVOS 4, COSTOS 1). Si se protege con contraseña, hay que informarla en el informe.

### C5. Valores fijos dentro de fórmulas

Lo prohíben el E-21 («ausencia de valores fijos incrustados») y el correo del 01-11 (puntos 5 y 10):
- `COSTOS HH - SUELDOS!G8:G44`: `=F8*1.2` en 35 celdas, `MAX(F*1.2,1)`, `MAX(F*1.2,0.8)` y `MAX(F*1.2,1.5)`. El 1,20 y los pisos del E-26 deben ir en PARAMETROS (el C46 actual es otro recargo, el de reservas, y vale 0).
- `ADQUISICIONES OPERACION!C19`: tramos de precio de AWS escritos en la fórmula (10000, 0.09, 70000, 0.07…). También C50 (`8*40000*1.5`), C51 (`80000`) y C56 (`198*6990`).
- `ADQUISICIONES IMPLEMENTACIÓN!W8:W45` (el 12 de C3), `INNOVACIONES!D80` (`*52/12`), `INNOVACIONES!G79/G81` (`*12`).
- `FINANCIAMIENTO!B17` (24 cuotas) y `B18` (fecha de inicio) son supuestos fuera de PARAMETROS; `PARAMETROS!C67` toma la fecha de FINANCIAMIENTO.

---

## 2. Altos

### A1. El T-12 y el T-13 citan una Operación de HH obsoleta

- T-12 (SD3, RT-21.21, línea 669) y T-13 (SD9, `matriz_requisitos.tex` línea 719): «2.304 HH DES de 8.2.4, equivalentes al 1,7881 % de las **128.853,67 HH de Operación de T-15**».
- El SD7 (Tabla 7.4, p. 46) da hoy **109.791,32 HH** de Operación (meses 21–56). Con esa base son 2,0985 %.
- Es una contradicción entre subdocumentos (indicador del punto 7.1 de la pauta). Arreglo mínimo: cambiar la cifra y el porcentaje en las dos filas.

### A2. La hoja RESUMEN muestra HH y costos que no son los del proyecto

`RESUMEN!B32:B37` (bloque «Viabilidad y HH», alimentado por MODELO PUNTOS CASO DE USO) muestra:
- «Cantidad HH Proyecto» **47.768,44 HH**, cuando el T-15 tiene 202.108,62 HH;
- «Costo Total (Según Tablas)» **36.575,17 UF** y «Venta Total» 44.168,35 UF, en la misma hoja que el costo de 199.911,43 UF y el precio de 235.308,64 UF.

Ningún documento menciona ese bloque. Como la hoja RESUMEN no puede cambiar sus filas ni rótulos, lo seguro es dejar una nota que explique qué mide ese bloque (solo programación por puntos de caso de uso) y cómo se concilia con el T-15. Otra opción es alimentar B35 con el total del T-15.

### A3. Hay cifras del E2 que no existen como celda en el Excel

El E-21 exige valores idénticos y el correo del 01-11 pide rastrear cada dato. Al buscar cada cifra del E2 en las celdas del Excel (incluidas las de Operación, que no cambiaron), no aparecen:
- los equivalentes en CLP y USD del cuadro maestro, de los márgenes y del IVA (por ejemplo 2.629.411.540, 3.394.110, 11.200.691.415);
- los subtotales de la sección 2.5: Mesa N1 25.624,82, NOC 14.571,29, SOC 17.607,60, «Otros perfiles» 22.886,00 HH / 18.563,75 UF, 109.160,20 HH sin capacitación, promedio de 3.087,22 UF/mes;
- el IVA del proyecto (44.708,64) y el precio con IVA (280.017,29).

En la nota de pendientes se decidió no agregar esos totales al Excel. El riesgo es que un evaluador compare cifra por cifra y no las encuentre. Basta un bloque de conciliación en INDICADORES o RESUMEN que las calcule con fórmulas.

### A4. Intune: 382 equipos durante los 36 meses

El T-11 (N-13), el T-12 (RT-03.18), el T-13 y la hoja HARDWARE DEL CLIENTE dicen 382 equipos al inicio y 433 en el año 3. El Excel cobra 382 los 36 meses, y el E2 (2.4 y 2.5) lo dice como «parque inicial». Faltan unos 3,88 UF/mes desde el año 3. Es poco, pero es un costo que no se rastrea hasta la propuesta técnica (Art. 57.2).

### A5. SD8: el PDF quedó atrás del .tex, y hay PDF sueltos en la rama

- El commit 99418330 de Max (21:23) cambia `contenido.tex`, `anexo-e`, `anexo-f`, el T-16 y los anexos, pero los PDF de la raíz son del commit 97b6dccc (20:37). Los PDF no reflejan sus cambios.
- La rama tiene una carpeta `tmp/` con 12 carpetas de compilación y unos 35 PDF (`tarea2-build`, `odd-firma-sd8`, etc.). Hay riesgo de entregar uno de esos por error.

### A6. El Excel tiene un texto pendiente visible

`FLUJO DE CAJA COMPLETO!D67`: «Depreciación de activos **por validar**». Es un indicador de trabajo inconcluso en un entregable.

---

## 3. Medios

| # | Punto | Dónde | Arreglo mínimo |
|---|---|---|---|
| M1 | Tres cortes distintos para las HH de Operación: E2 109.160,20 (meses 21–56 sin capacitación), SD7 109.791,32 (Tabla 7.4) y Excel 112.297,49 (perfiles, meses 21–56). En la implementación, el E2 y el Excel usan los meses 1–20 (88.486,33 HH), mientras que el SD7 usa los meses 1–21 más la estabilización de los meses 21–22 (92.317,30 HH). | E2 2.1 y 2.5; SD7 p. 46 | Una frase en el E2 2.1 que concilie los cortes con la Tabla 7.4 del SD7. |
| M2 | El E2 nombra las 200.783,82 HH de perfiles, pero nunca concilia con las 202.108,62 HH del T-15. Faltan las 1.324,80 HH de servicios especializados (código 00) y no se dice en qué partida del Excel se costean. | E2 2.1, línea 40 | Una frase: «más 1.324,80 HH de servicios especializados que se contratan como …». |
| M3 | El E2 2.6 pone al NOC entre los recursos «dedicados», pero en la misma sección y en la 2.5 lo describe como compartido con la división 24×7 (100/75/50 %). | E2 2.6, líneas 10 y 17 | Pasar el NOC a compartido, o llamarlo «puesto dedicado con dotación compartida». |
| M4 | La hoja PROVEEDORES sigue mostrando «AWS ambientes de pruebas, 1.083,62 USD/mes», pero ese costo ya no entra a COSTOS (ahora sale del bloque de horario). PROVEEDORES no cuadra con COSTOS. | Excel | Que PROVEEDORES muestre el costo del bloque. |
| M5 | KVM: el Excel compra 2 «KVM IP» (130,02 UF) y el T-11 declara 1 consola KVM (Talca, R01, U24). | Excel / SD4 T-11 | Corregir la cantidad o declarar la segunda en el T-11. |
| M6 | Curva S con dos criterios: el E2 2.3 grafica las tres series de la nota 6 del correo (ingresos = hitos + cuotas, costos + intereses, saldo), mientras que la hoja CURVA S usa el criterio de FEP08 (cobros con capital y pagos con amortización). Los puntos de la figura del E2 no están como serie en el Excel. | E2 2.3 / CURVA S | Agregar a CURVA S las tres series de la nota 6 (el E2 ya usa ese criterio y el correo es parte de las Bases). |
| M7 | La etiqueta «TIR» de `RESUMEN!G27` muestra 1,29 (la TIR anual), y el E2 habla de una TIR mensual. | Excel | Cambiar el rótulo a «TIR anual», o mostrar la mensual. |
| M8 | INN-05: el Excel reparte la inversión en los meses 13–17 y 18–23, mientras que el T-15 la tiene en los meses 13–21 (3.10.4.x) y el resto en 8.3.5–8.3.6 (meses 22–27). El total de HH de innovación cuadra (5.552 HH). | INNOVACIONES filas 62–63 | Ajustar los meses en E62:F63. |

---

## 4. Bajos y de forma

- **Símbolo de sección** (regla del equipo, además de verse poco natural): T-13 tiene 250, SD3-Anexos 249 (columna de origen, del tipo «Caso, [símbolo doble] 4.1 y 9.4»), SD8 3 (citas al PMI y a BTT 20.2) y SD5 2 (referencias a 5.1.7 y 5.1.11). Buscar el carácter U+00A7 en los .tex.
- **Abreviaturas «S7», «S4»** como fuente en el SD8-Anexos (Tabla 8.H.1: «S7 Tabla 7.4»; R-035: «S4, pp. 78, 84 y 183»; «S7, pp. 21–22 y 32») y en el SD5 («Proyección de S4», «S4 Anexos 4-G»). Mejor escribir «Subdocumento 7».
- **Fechas de portada mezcladas:** 12 de octubre en SD1–5, SD7, SD9, SD13 y en sus formularios; 27 de octubre en SD6 y SD8 (en SD8 con «Octubre» en mayúscula); 13 de noviembre en el E2.
- **SD7, Figura 7.24:** las leyendas dicen «continuación 2 de 6 … 6 de 6», pero las láminas dicen «Lámina 1 de 5 … 5 de 5».
- **Excel, ortografía:** «sattelital» (ADQUISICIONES OPERACION B55), «temperatira» (HARDWARE DEL CLIENTE B24), «Convercion» (PARAMETROS D58), «horacios» (PARAMETROS B66), «Justificacion» sin tilde en 18 hojas. En HARDWARE DEL CLIENTE, la «Luz y zumbador de alarma» tiene como modelo el DUPS40 de Mean Well, que es la UPS de la fila siguiente. Varias marcas empiezan con un tabulador (ITA, Mean Well, Victron).
- **Nombres de archivo:** `LAFROX_AnalisisFinanciero_2_…pdf` frente a `LafroX_ModeloFinanciero_3_…xlsx`. El E-21 pide la misma [EMPRESA].
- **FLUJO CAJA NETO!D21** suma `D27:D71` (mezcla ingresos y egresos), mientras que el resto de la fila suma `27:40`. Hoy no cambia nada porque el mes 0 está en cero.

---

## 5. Lo que sí cuadra

- **Línea base de HH:** 202.108,62 HH en el T-15, SD6, SD8 (199.036,62 + 3.072) y SD9 (T-13). Las 200.783,82 HH de perfiles del Excel (`COSTOS HH - SUELDOS!E45`) más 1.324,80 de servicios dan el mismo total. No quedan cifras antiguas (199.219, 219.727, 220.023 solo como «antes»).
- **Plazas:** 137 = 91 de planta + 9 de Implantación + 13 de mesa + 6 del SOC + 18 por obra o faena, igual en T-15, Excel (J45 = 137, J40 = 13, J41 = 8, J43 = 4, J44 = 6), SD1 (133 de planta, con mesa y SOC aparte), SD6 y Anexo A. Picos de 60 (mes 5), 51 (mes 15) y 58 (mes 20) en SD7 y T-15.
- **Roles mínimos BTT 19.2:** JP, Líder Funcional y Líder de Desarrollo con 2.560 HH (20 × 128) en la implementación; Líder de Operación / SRE con 4.608 HH (36 × 128) en la Operación, igual en Excel, T-14 y E2 2.6.
- **Nombres:** Patricio Henríquez solo como Líder de Implantación; Líder Funcional sin nombre; Guillermo Castillo como Líder de Operación / SRE; Tomás Pérez como Líder de Desarrollo; Leandro Chamorro como Líder de Datos; Maximiliano Miño como Líder de Calidad; Álvaro Catalán como Encargado de Seguridad; Bastián Trejo como Arquitecto. Sin cruces entre documentos.
- **Hitos:** los 12 del E-25 con los mismos meses y porcentajes en PARAMETROS, FINANCIAMIENTO y la Carta Gantt del SD7 (H1 23-03-27 = mes 2 … H12 mes 21, con inicio en febrero de 2027). La cuota de Operación es G11/36, de los meses 21 a 56.
- **E-24:** USD 900, EUR 1.000, UF 40.000, 0,9 %, 3 %, tope de la línea de 1.250 UF, 80/20, IVA 19 %, 56 meses. Tasa de 0,998 % mensual = 0,9 % × 0,8 + ((1,18)^(1/12) − 1) × 0,2, menor que 20 % y sin dividir por 12. La TIR anual usa (1 + TIR)^12 − 1. El VAN se calcula sobre el flujo del proyecto, sin intereses (INDICADORES fila 30, filas 65–70 del flujo).
- **E-26:** los 37 perfiles tienen costo y tarifa dentro de su rango, incluidos Mesa y NOC (TIC 0,67/0,80) y SOC (Ingeniero Senior 0,67/0,80).
- **Gastos administrativos:** overhead, las tres garantías con los montos de los arts. 35–37 (USD 500.000 por 150 días, USD 1.000.000 hasta 12 meses después de la Operación, 5 % de la implementación por 24 meses), los cuatro seguros del art. 38 (RC y ciberriesgo de UF 20.000), gastos notariales y custodia de fuentes. Cada uno declara su criterio. Los intereses no están ahí.
- **Rentabilidad:** 15,04 % EBITDA/ingresos, menor que 20 %. Caja siempre positiva: no se usa la línea de crédito.
- **Hardware del cliente:** fuera del flujo, con especificación, marca, modelo, cantidad y costo estimado. Las cantidades cuadran con el T-11 (175 TC58e + 207 MC9400 = 382; 433 en el año 3; 28 + 3 = 31 kits de frío).
- **Equipos de la solución, Excel frente al T-11:** FortiGate 100F 5, Rugged 60F 7, C9300 5, C9200 7, Moxa EDS 7, AP Cisco IW9167I 72, DL345 3, DL20 2, mini-PC 7, UC-8200 4, Starlink 5, LTE 8, estaciones 8, CrowdStrike 217. Solo falla la KVM (M5).
- **Riesgos:** los R-001 a R-035 citados fuera del SD8 existen. Los Anexos 8.A a 8.H existen. El R-027 de SD13/T-19 (P = 3, I = 3, exposición 0,10, zona Media) coincide con las escalas del SD8.
- **Innovaciones:** 5.552 HH en el Excel = paquetes 3.10.x + 8.3.x + 5.4.3 del T-15. SD13 y T-19 citan los mismos paquetes y el Anexo 7.D, que existe.
- **Precios en la oferta técnica (Art. 50.2):** no hay montos de la oferta en los subdocumentos técnicos. Solo aparecen antecedentes financieros de LafroX (SD1) y rangos de contratos pasados (T-6).
- **Reservas de riesgo:** SD8 (180 + 821,13 + 160 HH) frente al Excel (180 + 821,17 + 160 HH; 1.036,79 UF = E2). La diferencia de 0,04 HH viene del redondeo mensual.

---

## 6. Contraste con el correo de aclaraciones del 01-11

| Punto | Exigencia | Estado |
|---|---|---|
| 1a | Proveedores, adquisiciones, Curva S, costos, VAN/TIR, cinco innovaciones, planilla | Cubierto en E2 2.1–2.7 y en el Excel |
| 1a | Valores derivados de dotación, HH, EDT y arquitectura (Art. 57.2) | Cumple en general; fallan A1, A2, A4, M2 y M5 |
| 1b | Trazabilidad observación–respuesta (Art. 46) como anexo | Existe (rama `LAFROX-Subdocumentos-Anexos`) |
| 1b | Avance del prototipo navegable | No se revisó |
| 3 | 56 meses: E1 1–16, E2 13–21, Operación 21–56 | Cumple |
| 4 | 12 hitos del E-25; Operación en 36 pagos, de los meses 21 a 56 | Cumple |
| 5 | No modificar RESUMEN | Filas y rótulos intactos, pero muestra cifras que no son del proyecto (A2) |
| 5 | Hojas mínimas (E-21, Proveedores, Sensibilidad, Innovaciones, Financiamiento) | Cumple (19 hojas) |
| 5 | Curva S graficada, mensual, 56 meses | Hay un gráfico; el criterio difiere del E2 (M6) |
| 5 | Flujo mensual con total del mes y acumulado | Cumple (FLUJO CAJA NETO filas 7–8) |
| 5 / 10 | Todo con fórmulas, sin valores fijos | **No cumple** (C5) |
| 6 | Hoja de gastos administrativos con criterio por ítem | Cumple |
| 7 | Rentabilidad ≤ 20 % (EBITDA/ingresos) | Cumple: 15,04 % |
| 8 | Tasa mensual, ponderada, menor que 20 %, en PARAMETROS | Cumple: 0,998 % |
| 9 | Hardware del cliente fuera del flujo, en hoja informativa | Cumple |
| 10 | Validación, protección, supuestos en cada hoja, sin valores fijos | **No cumple** (C4 y C5). Los supuestos por hoja sí están. |
| Nota 3 | Tasa anual pasada a mensual con potencia | Cumple |
| Nota 5 | VAN con el flujo del proyecto; Curva S con el flujo financiado | Cumple |
| Nota 6 | Curva S: costos + intereses, ingresos y saldo | El E2 cumple; el Excel usa el criterio de FEP08 (M6) |
| Nota 7.6 | Déficit cubierto con la línea, respetando el tope | No hay déficit (mínimo de 537,47 UF) |

---

## 7. Orden sugerido de corrección (mínimo arrastre)

1. **Excel** (lo edita el equipo): corregir C2 (`INGRESOS!D80:V80`) y C3 (×24), y decidir si se usa `PARAMETROS!C70`. Después C5 (llevar el 1,20 y los pisos a PARAMETROS), A6, M4, M5, M7, M8 y la ortografía. Al final, proteger y validar (C4).
2. **E2:** regenerar 2.1, 2.2 y 2.3 desde el Excel corregido. Agregar las frases de M1, M2 y M3, y las series de M6 si se elige ese criterio.
3. **SD3 (T-12) y SD9 (T-13):** cambiar 128.853,67 por 109.791,32 y 1,7881 % por 2,0985 % (A1).
4. **SD8:** recompilar los PDF sobre el commit de Max y sacar `tmp/` de la rama (A5).
5. **Forma:** el símbolo de sección en T-13, SD3-Anexos, SD8 y SD5; «S7»/«S4»; fechas de portada; leyenda de la Figura 7.24.
