# Informe 2 — Provisión del sistema de cadena de frío (SD4)

| Observación | Respuesta | Sección modificada |
| --- | --- | --- |
| El T-11 declara que LafroX «provee, instala y mantiene el sistema de cadena de frío B-01, B-02 y B-03 a B-15»; el Cap. 11 del caso dice que el hardware de terreno lo adquiere el CLIENTE. | Se alinea con el Cap. 11: el CLIENTE adquiere B-01 y B-03 a B-14 según la especificación de LafroX; LafroX los instala, integra y mantiene. B-02 queda como infraestructura on-premise de LafroX (art. 14.2) y B-15 como servicio contratado en el paquete 5.3.4. | 4.2.1; 4.2.2 (B-03 a B-15); Anexo 4-O, ADR-24; T-11: introducción, fila B-03 y nota de responsabilidad. |

## Coherencia con otros subdocumentos

- SD6: corregido en la rama `LafroX-Subdoc6-LateX-corrigiendo` (commit `2c82d936` sobre `LafroX-Subdoc6-LateX` `df7eacb1`: 6.1.3, Anexo 6.B y T-9, con sus tres PDF regenerados y el mismo número de páginas).
- SD7: corregido en `LafroX-Subdoc7-LateX-CORRIGIENDO` (commit `648f2fea` sobre `f97e9f71`): entregable del paquete 5.1.4 del T-14, su PDF (166 páginas, sin cambio), el espejo Markdown y la tabla de auditoría K4. El título del paquete se conserva, porque LafroX compra los gateways B-02 y el prototipo; así no cambian las Gantt.
- SD3: corregido en `LafroX-Subdoc3-LateX-CORRIGIENDO` (commit `1b145ecd` sobre `866619f1`): E-09 y su párrafo en el Anexo 3.D, S-28, S-38 y las filas RF-09.03, RF-09.04, RNF-23.01 y RNF-23.02 del T-12, con los PDF de anexos (184 páginas) y del T-12 (261 páginas) regenerados. El cuerpo no cambia. Ningún documento cita páginas del SD3, así que la página adicional no desplaza referencias.
- Informe 3: fuera de alcance de esta corrección.

## Verificación

1. Búsqueda en `04/` de «provee, instala», «LafroX provee», «LafroX compra» y equivalentes: sin afirmaciones de compra de B-01 o B-03 a B-14 por LafroX.
2. `.\compilar.ps1` regenera el cuerpo, los anexos y el T-11.
