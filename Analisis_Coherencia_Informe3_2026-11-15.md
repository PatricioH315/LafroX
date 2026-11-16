# Análisis de coherencia — Informe 3 (15-11-2026, noche)

Uso interno. No citar ni entregar. No se corrigió nada: ni ramas, ni Excel, ni PDF.

## Qué se revisó

Se hizo `git fetch --all` y `git pull` antes de revisar. Se leyeron las ramas remotas, no las carpetas locales.

| Fuente | Versión revisada |
|---|---|
| SD1 | `LafroX-Subdoc1-LateX-CORRIGIENDO` 278a4c41 (14-11 19:27) |
| SD2 | `LafroX-Subdoc2-LateX-CORRIGIENDO` a72407bc (08-11) |
| SD3 / T-12 | `LafroX-Subdoc3-LateX-CORRIGIENDO` 887ab84c (15-11 18:23) |
| SD4 / T-11 | `LafroX-Subdoc4-LateX-corrigiendo` 5485aaf9 (15-11 16:04) |
| SD5 | `LafroX-Subdoc5-LateX-CORRIGIENDO` daec1657 (14-11 23:02) |
| SD6 / T-9 / T-10 | `LafroX-Subdoc6-LateX-corrigiendo` 68a9f14f (15-11 16:04) |
| SD7 / T-14 / T-15 / T-18 | `LafroX-Subdoc7-LateX-CORRIGIENDO` c088f82c (15-11 18:37) |
| SD8 / T-16 | `Lafrox_Subdocumento_8_Latex_Revision` c619c8e7 (15-11 16:04) |
| SD9 / T-13 / T-17 | `LafroX-Subdoc9-LateX-corrigiendo` fd88261e (15-11 18:44) |
| SD13 / T-19 | `LafroX-Subdoc13-LateX-corrigiendo` f6b57fa6 (15-11 18:44) |
| Entregable 2 | `LafroX-OfertaEconomica-2-Latex` ffed857c (15-11 18:50) |
| Anexo A (trazabilidad) | `LAFROX-Subdocumentos-Anexos` e128b52b (15-11 18:44) |
| Excel | `LafroX_ModeloFinanciero_3_20261113.xlsx` (Drive 18wI3…), modificado el 15-11 a las 21:04 hora local. Se leyeron los valores que guardó Google Sheets y se recalculó una copia con Excel 365. |

Método:
- Volcado de las 19 hojas del Excel, con fórmulas y valores.
- Búsqueda automática de cada cifra de las secciones 2.1 a 2.7 del E2 en el Excel (también ×40.000 para CLP, ÷900 para USD y ×100 para porcentajes).
- Cruces dirigidos entre las fuentes .tex de las ramas: HH, plazas, hitos, reservas, riesgos, innovaciones, equipos y nube.
- Comparación del estado de cumplimiento de los 374 RT entre el T-12 y el T-13.
- Fecha de cada PDF frente a los cambios posteriores en sus .tex.

---

## 1. Críticos: bloquean la entrega

### C1. En Excel de escritorio el modelo muestra `#NAME?` en la Operación, el VAN, la TIR y la Curva S

- El archivo lo guardó Google Sheets. Las 38 fórmulas con `LET` quedaron escritas sin el prefijo `_xlfn.` que Excel necesita: 36 en `COSTOS!W63:BF63` (Sites Cloud de la Operación) y 2 en `ADQUISICIONES OPERACION!R161:S161`.
- Al recalcular con Excel 365, Excel las lee como una función desconocida (`_xludf.LET`) y el error se propaga a 705 celdas:
  - `RESUMEN` B11:B13, G11:G13, L11:L13 y la rentabilidad nominal;
  - `INDICADORES` (VAN, TIR, punto de quiebre);
  - `FLUJO CAJA NETO`, `FLUJO DE CAJA COMPLETO`, `FINANCIAMIENTO` y `CURVA S`.
- El archivo no tiene `calcId`, así que Excel lo recalcula completo al abrirlo. El evaluador vería errores en vez de cifras.
- En Google Sheets se ve bien. Todas las cifras de este informe son las que calcula Google Sheets.
- Arreglo: reescribir esas 38 fórmulas sin `LET`, o abrir el libro en Excel de escritorio, volver a ingresarlas y guardarlo desde Excel. Después, abrir el archivo final en Excel y confirmar que no queda ningún `#NAME?`.

### C2. El E2 ya no coincide con el Excel: hay que regenerar las secciones 2.1 a 2.5

El último commit del E2 (ffed857c) solo tocó la sección 2.7. Las secciones 2.1 a 2.5 siguen con las cifras del 14-11. Al buscarlas en el Excel, no aparecen 126 de las 188 cifras de 2.1, 264 de las 290 de 2.2, 72 de las 86 de 2.3 y 83 de las 142 de 2.5. La sección 2.7 sí cuadra.

| Cifra | E2 (ffed857c) | Excel actual |
|---|---|---|
| Costo total | 200.024,98 | **204.882,93** |
| Costo de implementación | 88.884,92 | **93.613,56** |
| Costo de Operación | 111.140,06 | **111.269,37** |
| Infraestructura y equipamiento, implementación (`COSTOS!V73`) | 12.975,08 | **13.614,93** |
| Servicios de proveedores, implementación (`V74`) | 4.472,14 | **8.557,21** |
| Servicios de proveedores, Operación (`BF74`) | 25.623,76 | **25.747,87** |
| Gastos administrativos, implementación / Operación | 3.592,47 / 6.229,43 | **3.596,20 / 6.234,63** |
| Precio neto | 235.308,64 | **240.652,39** |
| Precio de implementación / Operación | 105.093,38 / 130.215,27 | **110.294,88 / 130.357,51** |
| Cuota de Operación | 3.617,09 | **3.621,04** |
| Margen (rentabilidad) | 35.283,66 (14,99 %) | **35.769,46 (14,86 %)** |
| Margen de implementación / Operación | 16.208,45 / 19.075,21 | **16.681,32 (15,12 %) / 19.088,14 (14,64 %)** |
| IVA del proyecto / precio con IVA | 44.708,64 / 280.017,29 | **45.723,95 / 286.376,35** |
| VAN sin impuestos | 24.691,13 | **25.070,29** |
| TIR mensual / anual | 7,13 % / 128,44 % | **7,16 % / 129,36 %** |
| VA de ingresos / VA de otros egresos | 182.088,92 / 45.819,81 | **186.777,84 / 50.129,57** |
| Mínimo del flujo acumulado sin financiamiento (mes 9) | −17.415,73 | **−17.828,48** |
| Ingreso mínimo para VAN = 0 / alza tolerable de sueldos | 86,44 % / 22,13 % | **86,58 % / 22,47 %** |
| H1 | 8.407,47 | **8.823,59** |
| Capital inicial (crédito / socios) | 19.000 (15.200 / 3.800) | **20.000 (16.000 / 4.000)** |
| Interés mensual / cuota del crédito / total de intereses | 136,80 / 707,03 / 3.683,89 | **144,00 / 744,24 / 3.877,77** |
| Caja mínima financiada (mes 9) / saldo final | 489,87 / 35.399,78 | **1.019,52 / 35.891,68** |
| Gastos administrativos totales | 9.821,90 | **9.830,84** |
| Servicios contratados de Operación, por mes | 710,69 | **715,22** |

Qué cambió en el Excel después del E2:
1. **Nube productiva desde el mes 6** (bloque nuevo en `ADQUISICIONES IMPLEMENTACIÓN` O49:V150): Aurora de producción y de recuperación, Fargate, DMS desde el mes 13, ALB, VPN y TGW de São Paulo, NAT, Private CA, Shield Advanced, Verified Access y tráfico. Suma 3.867,55 UF en los meses 6 a 20.
2. **Ambientes de prueba con el factor 24** (antes 12): 680,76 UF. Con los puntos 1 y 2, Sites Cloud de la implementación llega a 4.693,57 UF.
3. **Controladora inalámbrica Cisco CW9800L y repuestos** (filas 85 a 93): +629,65 UF en equipos. Ahora sí está costeado el par CW9800L que declara el T-11 (D-02).
4. **Intune** pasa de 382 a 433 equipos desde el mes 25 (`PARAMETROS!C73:C75`): +124,11 UF en la Operación.
5. **Capital de 20.000 UF** (`PARAMETROS!C54`).
6. Garantía de correcto funcionamiento y seguro de equipos: +8,94 UF, porque dependen del precio de implementación y del valor de los equipos.

Secciones del E2 que hay que regenerar o reescribir:
- **2.1:** las cuatro tablas y el texto.
- **2.2:** flujo anual y mensual, VAN y TIR, sensibilidad y equilibrio.
- **2.3:** capital, tabla de financiamiento, figura y su tabla, y el texto (ver C3).
- **2.4:** total de equipos. «Equipos de red y oficina» sube de 6.411,51 a 7.006,28 UF; «Servidores y equipos de borde», de 1.424,97 a 1.470,03 UF. Falta mencionar el CW9800L. Los servicios de Operación pasan a 715,22 UF/mes.
- **2.5:** servicios (Intune ya no es 29,05 UF fijos en los 36 meses), gastos administrativos, total y promedio mensual (3.090,82 UF).
- **2.6:** solo si cita el precio, la cuota o los gastos administrativos.

Hoy el E2 no explica en ninguna parte que la implementación paga nube productiva desde el mes 6.

### C3. Capital de 20.000 UF frente al criterio escrito en el E2

- La sección 2.3 del E2 dice que el capital es «el menor monto, en miles de UF, que mantiene la caja sobre cero», y que con 18.000 el mes 9 queda negativo.
- Con las cifras actuales, 19.000 UF todavía alcanzan: 19.000 − 17.828,48 − 8 × 136,80 de intereses = **≈ 77 UF** en el mes 9.
- El Excel usa 20.000 y justifica la cifra como «Cobertura de primer hito» (`PARAMETROS!D63`).
- Hay que decidir el criterio:
  - **Volver a 19.000:** el texto actual sirve, pero la holgura es de solo 77 UF.
  - **Mantener 20.000:** hay que cambiar el texto de 2.3 por el criterio de cobertura, y todas las cifras de financiamiento.

### C4. El Excel sigue sin protección ni validación

Ninguna de las 19 hojas está protegida. Solo tres hojas tienen validación de datos (`COSTOS`, `GASTOS ADMINISTRATIVOS` y `MODELO PUNTOS CASO DE USO`). Esta exigencia rige desde el Informe 3.

### C5. Valores fijos dentro de fórmulas (hubo avance parcial)

- **Corregido:** el factor 1,20 ya está en `PARAMETROS!C55` y `COSTOS HH - SUELDOS!G8:G44` lo usa.
- **Pendiente:**
  - `ADQUISICIONES OPERACION!C19` tiene los tramos de soporte de AWS escritos en la fórmula (10000, 0.09, 70000, 0.07…). La fórmula `LET` de `COSTOS!W63` repite los mismos tramos.
  - El bloque nuevo de nube productiva tiene constantes escritas a mano: meses de alta 6 y 13, tarifas en USD (V66:V76), 1.000 GB/mes, `P131 = 1.68+1.29+3*0.32`, tasa de soporte de 9 %, `4*29`.
  - `FINANCIAMIENTO!B17:B18` (24 cuotas y fecha de inicio) siguen fuera de PARAMETROS.

---

## 2. Altos

### A1. El Excel muestra trabajo sin terminar

Son textos y celdas visibles para el evaluador:
- **`ADQUISICIONES IMPLEMENTACIÓN` I87:I93 y B92:** «Cotización local pendiente», «Confirmar disponibilidad», «Confirmar configuración y stock», «Por definir», «Pendiente de respaldo. Excluido del subtotal de equipos».
- **`PROVEEDORES` 104 a 111:** «Factibilidad y cotización pendientes» (fibra de Talca y Concepción), «Cuota por canal pendiente», «Tarifa efectiva pendiente», «Pendiente de confirmar» (Transbank), «Consumo por conciliar».
- **`ADQUISICIONES OPERACION` O44:AA151:** «Pendiente» y «Sin valorizar» en 648 celdas. Los ambientes de Desarrollo Fargate, Preproducción Fargate y Preproducción Aurora de los meses 21 a 56 no tienen costo. Solo «QA Fargate (escenario)» está valorizado, con 17,90 UF. Si esos ambientes siguen encendidos en la Operación (T-14, paquetes 3.1.1 y 3.1.2), falta su costo. Si no siguen encendidos, sobran esas filas.
- **Interruptores de escenario 0/1:** `P81` (almacenamiento Aurora), `P101` (Verified Access) y `P118` («Aplicar otra alta» de Shield). Shield Advanced queda en el mes 6 solo porque `P118 = 1`. El valor base escrito es 13.
- **`FLUJO DE CAJA COMPLETO!D67`:** sigue diciendo «Depreciación de activos por validar».

### A2. La contingencia del SD8 no cuadra con el Excel

| Perfil | SD8 Tabla 8.H.3 (c619c8e7) | Excel `COSTOS` C111:C117 |
|---|---|---|
| ARQ | 127,88 | 118,30 |
| CAL | 338,07 | 331,40 |
| JP, DAT, SRE, IMP, SEG | iguales | iguales |
| **Total** | **837,53** | **821,17** |

- Además, la distribución mensual difiere en los 56 meses.
- Las 180 HH preventivas y las 160 de gestión sí cuadran.
- La diferencia de costo es de unos 14,5 UF. Cambia las reservas de riesgo del E2 (1.036,79 UF) y el total.
- Como el SD8 es la fuente de las reservas, lo natural es llevar al Excel la Tabla 8.H.3.

### A3. PDF atrasados respecto de sus .tex

Verificado por archivo:

| Rama | PDF | Qué cambió después |
|---|---|---|
| SD7 | `LAFROX-Subdocumento7.pdf` (14-11 20:03) | `subdocumento-07/contenido.tex` y `tab_SD7_11` (8216b639, 15-11) |
| SD7 | `LAFROX-Formulario-T-14.pdf` (14-11 20:36) | `formulario-t14/contenido.tex`, `tab_T14_27` y `tab_T14_47` (8216b639) |
| SD7 | `LAFROX-Subdocumento7-Anexos.pdf` (09-11) | `tab_7D1` y otros (18 commits) |
| SD7 | `LAFROX-Formulario-T-18.pdf` (09-11) | `formulario-t18/contenido.tex` (d396b433, 15-11) |
| SD6 | Subdocumento, Anexos y T-9 (15-11 14:14); T-10 (12-11) | `LAFROX-Formulario-T-9.tex`, `LAFROX-Formulario-T-10.tex` y `contenido.tex` (68a9f14f) |
| SD8 | `LAFROX-Subdocumento8-Anexos.pdf` (15-11 02:04) | `LAFROX-Subdocumento8-Anexos.tex` (c619c8e7) |
| SD4 | `entrega/` SD4 y Anexos (14-11 23:49) | `05_modulos_funcionales…` y `15_anexo_4_1_n…` (5485aaf9) |

Para revisar (hubo cambios de .tex después del PDF, pero no se confirmó que ese PDF los incluya): `LAFROX-Subdocumento3-Anexos.pdf` (15-11 01:13), `LAFROX-Subdocumento5-Anexos.pdf` (08-11), `LAFROX-Formulario-T-6.pdf` (07-11), y el T-17 y los Anexos del SD9 (15-11 18:16).

Al día: T-15, T-12, T-13, SD9, SD13 completo y el PDF del E2. Pero el E2 está al día solo respecto de su .tex: el .tex está desfasado del Excel (C2).

### A4. Siguen abiertos de la revisión anterior

- **`RESUMEN!B32:B37`:** muestra el bloque por puntos de caso de uso (47.768,44 HH, 36.575,17 UF y 44.168,35 UF) junto al costo real del proyecto.
- **Cifras del E2 sin celda en el Excel:** los montos en CLP y USD, los subtotales de 2.5 (Mesa N1, NOC, SOC, «Otros perfiles») y el IVA.
- **KVM:** el Excel compra 2 (`ADQUISICIONES IMPLEMENTACIÓN!F21`, 130,02 UF). El T-11 y el SD4 (Tabla del sitio principal, línea 89) declaran 1 consola en R01, U24.

### A5. El Excel apunta a un archivo local de un compañero

`xl/externalLinks/externalLink1.xml` apunta a `D:\Usuario\Documents\Proyecto_Lafrox\outputs\…\indicadores\Indicadores.xlsx`. Ninguna fórmula lo usa, pero Excel muestra el aviso de vínculos externos y la ruta queda a la vista. Conviene quitarlo con «Editar vínculos → Romper vínculo».

---

## 3. Medios

| # | Punto | Dónde | Arreglo mínimo |
|---|---|---|---|
| M1 | Tres cortes de HH de Operación: E2 109.160,20 (meses 21–56 sin capacitación), SD7 Tabla 7.4 109.791,32, Excel por perfiles en los meses 21–56. | E2 2.1 y 2.5; SD7 | Una frase de conciliación en el E2. |
| M2 | El E2 cita 200.783,82 HH de perfiles, pero nunca nombra las 202.108,62 del T-15 ni las 1.324,80 de servicios especializados. | E2 2.1, línea 40 | Una frase. |
| M3 | El E2 2.6 pone al NOC entre los recursos «dedicados», pero en la misma sección lo describe como un puesto compartido. | E2 2.6, líneas 10 y 17 | Pasar el NOC a compartido. |
| M4 | La hoja PROVEEDORES no refleja lo que se costea. Sigue mostrando «AWS ambientes de pruebas 1.083,62 USD/mes», que ya se resta del costo (`COSTOS!D63` usa I13 − I9). No lista el CW9800L ni la nube productiva de los meses 6 a 20. | Excel | Que PROVEEDORES lea los bloques nuevos. |
| M5 | `RESUMEN!F27` dice «TIR» y muestra 1,29, que es la TIR anual. El E2 usa la mensual. | Excel | Rótulo «TIR anual». |
| M6 | Intune: el Excel supone que el «año 3» parte en el mes 25 (`PARAMETROS!C75`, «supuesto»). El T-11 y el SD4 hablan de «433 en el año 3», sin decir desde qué mes. | Excel / SD4 | Declarar el supuesto en el E2 2.5, o precisarlo en el T-11. |
| M7 | `COSTOS!D63:W63` tiene cinco versiones distintas de la fórmula según la columna (D–E, F–G, H–N, O–V, W). Los valores están bien (se verificaron mes a mes), pero es difícil de auditar. | Excel | Una sola fórmula para toda la fila. |
| M8 | La Curva S del E2 y la hoja CURVA S usan criterios distintos. Hoy no se volvió a revisar. | E2 2.3 / Excel | Revisar al regenerar 2.3. |

---

## 4. Bajos y de forma

- **Símbolo de sección:** sigue en el T-13 (`SD9_v_nueva/T13/matriz_requisitos.tex`, 250), en `SD3/tablas_anexo/rf_caso.tex` (245), `rnf_caso.tex` (2), `rf_propios.tex` (2), `SD3/trazabilidad/Trazabilidad-SD3.tex` (6), SD8 (3), `SD5/…/5_2_gestion.tex` (2) y `LAFROX-Subdocumento2.tex` (2).
- **Abreviatura «S7»:** SD8, `anexo-h-reservas.tex` línea 8 («S7, Tabla 7.4, pp. 45--46»). También en la trazabilidad del Anexo A (líneas 409, 451, 461, 497 y 505 de `Trazabilidad-Informe2/partes/tablas.tex`).
- **`FLUJO CAJA NETO!D21`:** suma `D27:D71`, mezclando ingresos y egresos. Hoy no cambia nada.
- **Nombre del archivo:** `LAFROX_AnalisisFinanciero_2_…` frente a `LafroX_ModeloFinanciero_3_…`.

---

## 5. Lo que sí cuadra (verificado hoy)

- **HH:** 202.108,62 en T-15, SD6, SD8 y SD9. Las 200.783,82 de perfiles (`COSTOS HH - SUELDOS!E45`) más 1.324,80 dan ese total. Las 109.791,32 HH de Operación aparecen igual en SD3 (T-12), SD7 y SD9 (T-13). Ya no queda ninguna mención a 128.853,67.
- **Plazas:** 137 (J45). Mesa 13, NOC 8, ciberseguridad 4, SOC 6.
- **Hitos:** las fechas de pago del T-15 (Tabla 7) caen en los mismos meses que `PARAMETROS` C26:C37 y `FINANCIAMIENTO` G9:G20: H1 mes 2, H2 4, H3 6, H4 10, H5 12, H6 13, H8 14, H7 16, H9 17, H10 18, H11 19 y H12 21.
- **Nube productiva desde el mes 6:** cuadra con el T-14 (3.1.2 y 3.1.3, producción y recuperación operativas en el H3) y con el SD6 (servicios AWS antes del mes 4). La compra de equipos en el mes 2 cuadra con el SD6 (orden de compra en el mes 2).
- **Innovaciones:** el Excel tiene 5.552 HH. INN-05 va en los meses 13–21 y 22–27, igual que el T-15 y el E2 2.7, así que se cerró el punto M8 anterior. El E2 2.7 cuadra con el Excel, y el SD13 no trae montos. El cambio de hoy al T-15 (fin de 3.10.x.4 el 28-04-2028) no cambia HH ni meses del modelo.
- **T-12 y T-13:** los 374 RT tienen el mismo estado en los dos, incluido RT-26.04 como «Cumple».
- **R-027:** 25 %, impacto 3, exposición 0,06, zona Baja. Igual en SD8, SD13 y T-19.
- **Reservas del SD8:** las 180 HH preventivas cuadran por perfil y por mes con `COSTOS` A100:A107. La reserva de gestión es de 160 HH en los dos.
- **Correcciones del Excel cerradas desde la revisión anterior:**
  - `INGRESOS!D80` sigue a `COSTOS` fila 63;
  - ambientes de prueba con el factor 24;
  - escalón de Intune en el año 3;
  - tarifa 1,20 llevada a PARAMETROS;
  - CW9800L costeado.
- **Nombres y roles:** no hay cruces entre documentos.

---

## 6. Orden sugerido de corrección (mínimo arrastre)

1. **Excel (lo edita el equipo):**
   - quitar `LET` o regrabar el libro desde Excel (C1);
   - decidir el capital, 19.000 o 20.000 (C3);
   - cerrar los textos pendientes y los interruptores de escenario, y decidir si los ambientes de Desarrollo y Preproducción de la Operación tienen costo (A1);
   - llevar la contingencia del SD8 (A2);
   - corregir la KVM (A4), quitar el vínculo externo (A5) y arreglar PROVEEDORES (M4) y el rótulo de la TIR (M5);
   - al final, proteger y validar (C4) y sacar los valores fijos (C5).
2. **Comprobar** que el libro abre en Excel de escritorio sin errores.
3. **E2:** regenerar 2.1 a 2.5 desde el Excel final (C2). Agregar el texto sobre la nube productiva desde el mes 6, el CW9800L y el escalón de Intune. Ajustar el criterio del capital en 2.3, y agregar las frases de M1, M2 y M3.
4. **Recompilar los PDF** de A3: SD7 ×4, SD6 ×4, SD8-Anexos y SD4 ×2. Revisar los de la lista «para revisar».
5. **Forma:** el símbolo de sección, «S7» y `FLUJO CAJA NETO!D21`.
