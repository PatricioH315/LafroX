# Ajustes que deben hacer otros subdocumentos por las correcciones del SD7 (09-11-2026)

Rama del SD7: `LafroX-Subdoc7-LateX-CORRIGIENDO`. La línea base pasa de 220.023 a 219.727,83 HH por la estimación por tamaño de los 15 módulos y los rangos por riesgo (T-15, sección 4.3, Tabla de conciliación).

## Cambios del SD7 que afectan a otros

1. **Pasos a producción y actas H7/H12.** H7 y H12 se cierran con una sola acta por etapa (BA, arts. 17.3 y 18.1): entrega del expediente el 02-05-2028 y el 02-10-2028, diez días hábiles de revisión, acta el 16-05-2028 y el 17-10-2028, y paso a producción el **17-05-2028** y el **18-10-2028** (antes: 05-05-2028 y 05-10-2028). Holguras: H7 10 días hábiles y H12 8.
2. **Holguras de los hitos** (CPM por duraciones, T-15, Tabla 9): H1 5, H2 14, H3 18, H4 18, H5 20, H7 10, H8 16, H9 19, H10 14, H12 8.
3. **Estabilización E2 (4.3.2):** refuerzo del 18-10-2028 al 16-11-2028; 1.129,33 HH en el mes 21 y 1.334,67 HH en el mes 22 (antes 513,33 y 1.950,67). La curva mensual del T-15 mueve 616 HH del mes 22 al 21.
4. **Reserva de gestión (T-15, sección 4.5):** el texto dice ahora que las 1.600 HH quedan fuera del total y de la dotación y se liberan con aprobación del Comité Ejecutivo.
5. **Dependencias nuevas** D-48 a D-51 en el Anexo 7.B (54 en total).
6. **Evidencia para el proveedor de lácteos:** expediente inicial en el mes 1 (1.1.3), simulacro de retiro en QA antes del H5 que identifica clientes en menos de 2 horas (3.6.1; R18-01) y simulacro con operación real en la marcha blanca E1.

## Qué debe revisar cada responsable

| Subdocumento | Ajuste |
|---|---|
| SD9 / T-17 (`origin/LafroX-Subdoc9-LateX-corrigiendo`, `SD9_v_nueva/T17/contenido.tex`, líneas 177 y 179) | Cambiar «paso a producción del 5 de mayo de 2028» por 17 de mayo y «5 de octubre de 2028» por 18 de octubre. |
| SD8 / T-16 | Confirmar que la reserva de gestión de 1.600 HH se libera con aprobación del Comité Ejecutivo, como dice ahora el T-15. Si el SD8 define otra instancia, avisar para alinear el T-15. **Resuelto 12-11:** el SD8 fija la reserva de gestión en 160 HH (4 ciclos de 40) con autorización del Comité Ejecutivo; el T-15 se corrigió de 1.600 a 160 HH. |
| Oferta Económica / flujo de caja | Si usan la curva mensual del T-15: 616 HH pasan del mes 22 al mes 21 (4.3.2). El total no cambia. |
| Oferta Económica / flujo de caja | Recategorizar perfiles de implantación según el T-15, sección 6.3: 5 jefes de frente como Analista / Diseñador Senior (4.006,96 HH) y 18 asistentes de terreno como TIC (14.425,04 HH), en lugar de 22 Analista / Diseñador Junior. Plazas de desarrollo: 36 (antes 17). Nuevo perfil 29, Técnico de Redes e Instalaciones (TIC, origen NOC/Infraestructura, 5 plazas, 2.240 HH) que ejecuta 6.1, 6.2, 6.3, 6.6.2 y 6.6.3; los DevOps senior y junior bajan a 3.282,13 y 1.641,07 HH y suben a 7 y 4 plazas. Total de perfiles: 37 y 136 plazas. Las HH totales no cambian. |
| SD1 (`LafroX-Subdoc1-LateX-CORRIGIENDO`, commit local ab798379, sin push) | Área de Implantación y Gestión del Cambio con 9 personas; dotación 133. Pendiente: agregar la caja de la nueva división al organigrama (Figura 1.1, `figuras/organigrama-corporativo.tex`). |

## Pendiente dentro del SD7 que requiere figuras

Las figuras no se modificaron (decisión del 09-11-2026). Quedan desalineadas con el texto:
- Gantt de 56 meses y láminas de la carta: muestran producción el 05-05 y el 05-10-2028 y las barras 4.2.3 y 4.3.3 con sus fechas anteriores.
- Figura del camino del H12 (T-15) y Figura 7.23 (ruta crítica del S7): revisar si muestran las holguras o fechas anteriores de H7/H12.

## Estimación por tamaño (09-11-2026, tarde)

| Subdocumento | Ajuste |
|---|---|
| SD9 | El costo de la calidad (12.016 HH) pasa a ser el 5,47 % de 219.727,83 HH; redondeado sigue en 5,5 %. Cambiar la base citada de 220.023 a 219.727,83 HH. |
| Oferta Económica | Total de HH 219.727,83 (−295,17). Por rol: DES −111,33; DAT −326,50; ARQ +100,00; SRE +21,33; IMP +21,33. Perfiles de la sección 6.3 del T-15 ya actualizados. |
| SD8 | Si cita las 220.023 HH como base de reservas, cambiar a 219.727,83. **Resuelto 12-11** en el Anexo 8.H (rama `Lafrox_Subdocumento_8_Latex_Revision`). |
