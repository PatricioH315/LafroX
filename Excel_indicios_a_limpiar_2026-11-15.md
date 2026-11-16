# Excel: textos que parecen de IA o de trabajo sin terminar (versión 15-11 22:51)

Uso interno. Revisé todas las celdas de texto de las 19 hojas. Solo cambian textos: ninguno de estos cambios mueve una cifra, salvo los interruptores de la sección 5, que hay que convertir en valores fijos sin cambiar el valor que tienen hoy.

No se encontró ninguna mención directa a IA: ni «Claude», ni «ChatGPT», ni «IA», ni en las celdas, los gráficos o las propiedades del archivo.

**No hay que tocar** (son normales): H1–H12 (hitos), M1–M12 (módulos), T1–T13, E1–E8 y P1–P10 (factores del método de puntos de caso de uso), los SKU de los equipos, la columna «Ubicación» de los cuadros de supuestos (C11, C22, C11:E14…) y la notación M21–M56.

---

## 1. Vínculo externo (lo más grave)

El vínculo apunta a `D:\Usuario\Documents\Proyecto_Lafrox\outputs\01a1ad40-d826-…\indicadores\Indicadores.xlsx`. Una carpeta `outputs\` con un código largo parece salida de una herramienta. Hay que quitarlo en Excel de escritorio: Datos → Vínculos del libro (o Editar vínculos) → Romper vínculo. Después se sube el archivo como versión nueva en Drive.

## 2. Códigos internos que no existen en ningún subdocumento

| Celda | Hoy | Cambiar por |
|---|---|---|
| `ADQUISICIONES IMPLEMENTACIÓN!O55` | Total C08 | Total bases de datos y réplica de producción |
| `ADQUISICIONES IMPLEMENTACIÓN!A85` | Equipos y repuestos C09 · Previsión de compra | Controlador inalámbrico D-02 y repuestos |
| `PROVEEDORES!B102` | Conciliación C12 · diseño y costo vigente | Servicios de comunicación y pagos: proveedor y costo |
| `PROVEEDORES!E76` | «…figuran en la conciliación C12.» | «…figuran en el cuadro de servicios de comunicación y pagos.» |

## 3. Textos de trabajo sin terminar (pendiente, confirmar, por definir)

**`ADQUISICIONES IMPLEMENTACIÓN`, bloque de repuestos (filas 85 a 93):**

| Celda | Hoy | Cambiar por |
|---|---|---|
| I86 (título de columna) | Estado de cobertura | Fuente del precio |
| I87, I88 | Cotización local pendiente | Precio de catálogo del proveedor |
| I89 | Confirmar disponibilidad | Precio de catálogo del proveedor |
| I90 | Opción HPE para DL20 Gen11 SFF. Confirmar coincidencia… | Repuesto compatible con el HPE DL20 Gen11 |
| I91 | Confirmar configuración y stock | Precio de catálogo del proveedor |
| A92, B92 e I92 | Licencias, soporte y despacho · Por definir · Pendiente de respaldo… | **Vaciar solo esas tres celdas**. No suman nada. No borres la fila entera: en O92:V92 está el mes 15 de la tabla de Aurora. |
| A93 | Total previsión de equipos | Total controlador y repuestos |
| I93 | Cotización local pendiente | (dejar vacía) |
| O88 | Validar capacidad WMS y cobertura de otros cargos antes de aplicar. | (borrar) |

**`PROVEEDORES`, filas 104 a 112, columnas E a I:**

| Celda | Hoy | Cambiar por |
|---|---|---|
| H104, H105 | Factibilidad y cotización pendientes | Tarifa referencial |
| H106 | Distribución pendiente | Total del diseño |
| E107, E108, E109, E110 | Cuota por canal pendiente | Según demanda mensual |
| H108, H109 | Tarifa efectiva pendiente | Tarifa pública |
| I108 | Validar segmento y remitente | Cobro por mensaje o segmento |
| I109 | Validar categoría y cargos aplicables | Cobro por mensaje según plantilla |
| H110 | Consumo por conciliar | Incluido en la plataforma |
| E111 | Ventas con tarjeta por confirmar | Según ventas con tarjeta |
| G111 | Pendiente de confirmar | CLIENTE (o LafroX, lo que corresponda) |
| I112 | USD/mes; reemplazar al conciliar | USD/mes |
| E42 | «…La tarifa vigente es referencial y requiere confirmar factibilidad y cotización.» | «…La tarifa vigente es referencial.» |
| E71 | «…Si no hay factibilidad, validar un operador fijo distinto de Entel.» | «…Si no hay factibilidad, se contrata otro operador fijo distinto de Entel.» |

**Otras hojas:**

| Celda | Hoy | Cambiar por |
|---|---|---|
| `FLUJO DE CAJA COMPLETO!D67` | Depreciación de activos por validar | Depreciación de activos |
| `GASTOS ADMINISTRATIVOS!D94` | «…La comisión es una hipótesis presupuestaria pendiente de respaldo bancario.» | «…Se usa la comisión de referencia de mercado.» |
| `GASTOS ADMINISTRATIVOS!D97` | «…Deben respaldarse la tarifa y la correspondencia del mes inicial con el primer entregable depositable.» | Borrar esa última oración. |
| `GASTOS ADMINISTRATIVOS!D98` | «…explicando cómo se reconocen y financian sus costos dentro del modelo.» | «…Su costo se reconoce dentro del modelo en el mes de pago.» |
| `MODELO PUNTOS CASO DE USO!D172` | «…; este criterio metodológico debe quedar explícito.» | Borrar ese final. |
| `INDICADORES!C44` | «…evitando interpretar como completo un flujo con períodos o cobros pendientes.» | «Los indicadores consideran todos los meses e ingresos hasta M56.» |
| `COSTOS HH - SUELDOS!D102` | «…ni una multiplicación adicional del esfuerzo ya agregado.» | Borrar ese final. |

## 4. Rótulos de borrador («Previsión», «Escenario»)

| Celda | Hoy | Cambiar por |
|---|---|---|
| `ADQUISICIONES IMPLEMENTACIÓN!O64` | AWS productiva M6–M20 · Previsión | Nube productiva, meses 6 a 20 |
| `O77` | Subtotal previsión AWS | Subtotal nube productiva |
| `O114` | Previsión productiva. P109 descuenta cobertura acreditada. | (borrar) |
| `O122` | Previsión AWS M6–M20 · incorporada al presupuesto | Nube productiva por mes, meses 6 a 20 |
| `O128` | LCU-h de previsión | LCU-h estimadas |
| `O80` | Escenario de almacenamiento Aurora · M13–M20 | Almacenamiento Aurora, meses 13 a 20 |
| `T89` | Escenario (UF) | Alternativa (UF) |
| `O100` | Escenarios AWS antes de M21 · Verified Access y Shield | Verified Access y Shield Advanced antes del mes 21 |
| `ADQUISICIONES OPERACION!O8:O43` (36 celdas) | QA Fargate (escenario) | QA Fargate |
| `ADQUISICIONES OPERACION!O154` | Nube no productiva · Escenario 24/7 y 12 h | Nube no productiva: comparación 24/7 y 12 h |
| `INNOVACIONES!A107` | Gastos de nube · insumos del escenario base | Gastos de nube: supuestos |

## 5. Interruptores 0/1 (quedan a la vista como «perillas» de prueba)

| Celda | Rótulo | Valor hoy | Qué hacer |
|---|---|---|---|
| `ADQUISICIONES IMPLEMENTACIÓN!O81` / `P81` | Aplicar (0 = no, 1 = sí) | 0 | Cambiar el rótulo a «Alternativa no incluida en el costo» y dejar el 0. **No borres el bloque O80:V98:** `S77` usa `V98`. |
| `O101` / `P101` | Aplicar acceso (0/1) | 1 | Cambiar el rótulo a «Verified Access incluido» y dejar el 1. |
| `O116:P119` | Alta base 13 / Alta alternativa 6 / Aplicar otra alta (0/1) / Adelanto Shield | 13 / 6 / 1 | En este orden: (1) escribir 6 en `P116` y cambiar `O116` a «Mes de alta»; (2) cambiar `P74` a `=MAX(4,$P$116)`; (3) vaciar `O117:P119`. Solo `P74` y `P119` usan esas celdas, así que Shield sigue desde el mes 6 y el costo no cambia. |

## 6. Títulos con «·» (punto medio)

Este estilo se repite unas 30 veces y llama la atención. Conviene cambiar el «·» por «:» o por «de». Por ejemplo, «Fargate · Producción y datos» → «Fargate de producción y datos».
- `ADQUISICIONES IMPLEMENTACIÓN`: O57, O60, O70, O71, O75, O76 y O115, además de las que ya están en las secciones 2 y 4.
- `ADQUISICIONES OPERACION`: O6, O164, A73 a A85 (12 celdas), A96 a A99 y A104 a A106.
- `PROVEEDORES!B112`: «Mapas, avisos y pagos · base vigente» → «Mapas, avisos y pagos: base vigente».

## 6b. Tablas de control y de antes/después (revisión de la versión del 15-11, 23:43)

Revisé todo el libro con un mapa de dependencias: qué celdas alimentan el resumen, el flujo, los indicadores, la Curva S, la sensibilidad y el financiamiento, y cuáles no alimentan nada.

| Dónde | Qué es | Qué hacer |
|---|---|---|
| `ADQUISICIONES OPERACION!A87:E93` | «Conciliación mensual: Anterior / Revisado / Diferencia», con los montos de antes escritos a mano y «Fila 9», «Fila 10»… como texto. | Vaciar A87:E93. No eliminar filas: la columna O sigue con la tabla de ambientes. |
| `INNOVACIONES!B105:E105` | «Control: suma mensual = resumen (sección F)», con fórmulas que muestran «OK egreso» u «OK ingreso», o «REVISAR…» si algo no cuadra. | Vaciar B105:E105. Ninguna fórmula lo usa. |
| `INNOVACIONES!BI100` | Encabezado «Veriif.», mal escrito, sobre la columna que totaliza cada fila. | Escribir `Total`. |
| `ADQUISICIONES IMPLEMENTACIÓN!O80:V98` | La alternativa de Aurora, con columnas «Diferencia (UF)» y «Ajuste (UF)». | Vaciar O82:V98 (sección 5). |
| `PARAMETROS!B70:C70` | «Meta de reducción de horas de cómputo», 0,6. Ninguna fórmula la usa. | Vaciar B70:C70. |
| `COSTOS!B55:B58` | «HH Total» de capacitación, escrita a mano (604,8; 382,4; 764,8; 3.496). Coincide con la suma de cada fila. | Cambiar por `=SUM(C55:BF55)` y arrastrar hasta B58. Con punto y coma: `=SUM(C55:BF55)` (no lleva separador). |
| `HH POR ROL Y MES!B9` y `B31:B33` | Totales escritos a mano, que nada usa. | Usar la misma fórmula de las filas vecinas o vaciarlos. |

**Se pueden dejar** (son parte del modelo, no restos):
- `INDICADORES` A15:C25 y la fila 33 («Control de ingresos», «Completo»): el VAN, la TIR y la fila 29 dependen de ellos. Si los borras, se rompen.
- `ADQUISICIONES OPERACION!O154:T161` (comparación 24/7 y 12 h): justifica el horario de 12 horas.
- Las tablas informativas de `PROVEEDORES`, `HARDWARE DEL CLIENTE`, `COSTOS HH - SUELDOS` (sueldos y plazas), `GASTOS ADMINISTRATIVOS` (K51:M67) e `INNOVACIONES` (secciones A a G, que usa el E2 2.7).
- `COSTOS` A132:E146 (reservas por familia): ya cuadra, con 1.051,33 UF en E141 y en E146.

## 7. Detalles menores

- `ADQUISICIONES OPERACION!B60`: «…F60 muestra el parque base. El escalón del año 3 se aplica en COSTOS, fila 69, según PARAMETROS.» Es una nota que nombra celdas y filas. Cambiar por: «…Desde el año 3 se gestionan 433 equipos.»
- `PROVEEDORES`, columna C: el «—» aparece en 24 celdas. Es mejor dejarlas vacías o poner «Varios».
- `SENSIBILIDAD` B30, B32, B34 y B36: «Δ % vs VAN base» → «Variación respecto del VAN base».
