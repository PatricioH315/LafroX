# Incorporación de cambios de `alvaro-md` al LaTeX — 2026-10-05

Origen: commits `e87513b` (CD-05) y `26c345c` (alineación SD3–SD4) de `origin/alvaro-md`. Los pasajes reemplazados coincidían con el LaTeX vigente (`428b9b2`). Decisiones del usuario: trasladar A1–A13, CD-05 con su parte física (C1-a), precio según RNG-08 (C2) y AL-STOCK-01/AL-ACT-01 en la tabla de 4-V y en 4.1.22 (C3).

## Cuerpo
- 4.1.2: dotación de terreno según la tabla del caso, cap. 14: 84 conductores propios y peonetas y unos 160 conductores de transportistas.
- 4.1.3: Greengrass bloquea ante una excursión crítica y sostenida. Nuevo `\paragraph` sobre los actores del sistema (15 actores del SD3 3.4.2.1).
- 4.1.4: precio pactado (RNG-08), promesa 24/48 h (RNG-15), local cerrado (RNG-05) y etapas de M10/M11/M12. Regla térmica graduada (RNG-04). Reserva confirmada tras la retención local. RF-03.16 (RF-03.17 no existe). RF-07.05/09 y RF-07.02 + INT-06. Nuevo `\paragraph` sobre la reserva comercial y la retención física (CD-05).
- 4.1.9: extracto conciliado en Talca y conteo físico en Concepción. Legado en solo lectura. La reversión no reactiva el legado.
- 4.1.17/18: un cambio de carga sin conexión se pospone y una guía anulada no se reutiliza.
- 4.1.19: declaración del conductor externo por despacho en E1 y por el portal en E2.
- 4.1.22: lista de protocolos con AL-STOCK-01 y AL-ACT-01.
- 4.2: cola FIFO de coordinación por sitio en N-09 (`02_a`, `02_b`), shipper y permisos IAM (`11_j`), totales de mensajes en 4.2.12 (tabla, texto y Dimensión 11).

## Anexos y formulario
- 4-D: actores y etapas mixtas. 4-G: contrato de coordinación dentro de INT-03/04. 4-I y 4-W: fila de coordinación de reserva, 46.968/87.228 mensajes/día (260.000 ÷ 22,14 × 4, peak × 1,857). Totales 225.629/347.383. 4-W explica por qué no cambia el drenaje.
- 4-K y 4-L: filas de doble reserva, precio, local cerrado, térmica, conductor externo y decisiones 8/9.
- 4-N: tabla de 15 actores y permisos. 4-V: AL-STOCK-01 y AL-ACT-01 en la tabla y en el desarrollo.
- T-11 N-09: 13 colas por región (se agregan 5 de coordinación).

## No trasladado
- Registros de proceso de `alvaro-md` (coherencia, verificación, complemento CD-05) y frases de no acreditación o dependencias pendientes.
- La regla para pedidos ingresados después de las 14:00 queda fuera del SD4 hasta que la defina el SD3.

## Pendientes fuera del SD4
- T-12 RF-03.11/12 siguen con el precio de despacho como regla por defecto. El redactor del SD3 debe alinearlos con RNG-08.
- Las figuras de las vistas generales no se han cotejado con los 15 actores ni con la regla térmica graduada (solo reportar, no editar imágenes).
