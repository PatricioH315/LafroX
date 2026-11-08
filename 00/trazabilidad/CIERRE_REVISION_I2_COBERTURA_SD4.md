# Informe 2 — Estudio de cobertura dentro de las cámaras (SD4)

| Observación | Respuesta | Sección modificada |
| --- | --- | --- |
| «Estudio de cobertura dentro de las cámaras (RT-03.24 del caso). El T-11 ofrece 72 puntos de acceso [...] como "estimación preliminar por superficie" [...]. El estudio no se presenta.» Se espera «el estudio, o su método, alcance y fecha en el cronograma». | Se presenta el estudio en tres fases: diseño predictivo por zona (incluido en la oferta), verificación en sitio en el mes 2, antes del cableado del mes 4, y medición de aceptación antes de cada marcha blanca. Las densidades (500 m² con racks, 300 m² por cámara con mínimo de dos y 900 m² en nave abierta) reproducen los 65 + 7 = 72 AP: no cambia ninguna cantidad. | Anexo 4-W.13 (nuevo); 4.2.1; T-11, fila Red inalámbrica. |
| Puntos de falla de la red inalámbrica (revisión interna, a pedido del usuario). El SD4 no declaraba modelo de AP, controlador ni dónde se autentica la Wi-Fi durante un corte de WAN. | AP Cisco Catalyst IW9167I (−40 a +55 °C, IP67, 25 W con PoE+), par de controladores CW9800L con conmutación de estado en R02 de Talca, AP en FlexConnect con conmutación local y RADIUS local (FreeRADIUS 3.2) junto a la caché de identidad en VM-05, VM-C03 y E-01. Tabla de puntos de falla con su prueba. | Anexo 4-W.13; 4.2.1; 4.3.1 (tabla eléctrica, cálculos, R02, VM-05); T-11 (fila nueva D-02 Controlador inalámbrico, UPS, generador, climatización, gabinetes); Anexo 4-P (FreeRADIUS). |

## Fuentes verificadas

- Cisco (2025), *Cisco Catalyst IW9167 Heavy Duty Series Data Sheet*, tabla 4: IW9167I de −40 a +55 °C, IP67, antenas integradas, 25 W y radios 2x2 con PoE+, EAP-TLS, WPA3 y 802.11r/k/v.
- Cisco (2026), *CW9800L Wireless Controller Data Sheet*, tablas 1 y 5: 1 RU, bandeja doble, 500 AP, 90 W, opción de alimentación redundante CW9800L-RPS, FlexConnect y puerto de redundancia para SSO.
- Cisco (2024), *Catalyst 9800 FlexConnect Branch Deployment Guide*, «Local authentication and backup radius server»: el AP sin controlador sigue con su última configuración y autentica contra un RADIUS del sitio; dos servidores, principal y respaldo.
- Cisco (s. f.), guía de configuración del IW9167I (IOS XE 17.16): FlexConnect entre sus modos.
- FreeRADIUS (2026), versiones en GitHub: 3.2.10 publicada el 3 de junio de 2026.

## Efecto en la sala de Talca

Carga TI base 7.450 → 7.630 W; diseño 8.940 → 9.156 W (≈ 9,2 kW); UPS ≈ 12,0 kVA sobre 15 kVA; PUE 13,8 ÷ 9,2 = 1,5; sitio ≈ 13,9 kW; generador ≈ 17,4 kVA, 70 % de 25 kVA; una unidad de clima de 10 kW sigue cubriendo la carga; R02 pasa de 12U a 13U (31 %) y de 0,65/0,8 kW a 0,83/1,0 kW.

## Páginas

Cuerpo: 194 páginas; solo el inicio del 4.2.2 pasa de la página 96 a la 97, sin mover las secciones siguientes. Anexos: el 4-W.13 ocupa las páginas 113 a 117 y las Referencias pasan de la página 113 a la 117. T-11: de 49 a 51 páginas.

## Coherencia con otros subdocumentos (pendiente, en sus ramas)

Registrado en `PENDIENTES.md`, sección «Estudio de cobertura y red inalámbrica — 6 de noviembre de 2026».
