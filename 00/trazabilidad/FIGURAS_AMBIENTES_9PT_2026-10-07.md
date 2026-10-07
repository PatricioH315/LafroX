# Figuras de ambientes de 4.2.4 a 9 pt — 2026-10-06/07

Solicitud del usuario: dejar los cinco diagramas de ambientes de la arquitectura de despliegue a ≥ 9 pt, sin texto innecesario, y explicar en el texto cada paso numerado de cada figura.

Fuente de los diagramas: el usuario los mantiene en su draw.io en la nube; el repositorio solo versiona los PNG exportados (zoom 300 %). Los `.drawio` se retiraron del repositorio a pedido del usuario.

Criterio común de las figuras (lienzo ≤ 590 u, texto 12 u, a `\textwidth` ≈ 9,04 pt impreso, orientación vertical):
- Se retiran «Cadena de entrega», «Equipo de desarrollo», «(suscripción) / controles del pipeline», «(SLSA nivel 3)», el marco «AWS Cloud · organización AWS Control Tower», los prefijos AWS/Amazon y las etiquetas de flecha «drenaje» y «Angular». Lo retirado está en el texto de 4.2.4.
- Se conservan el tipo de ambiente, la cuenta, la región, la VPC con su bloque, los códigos N-xx y los pasos numerados.

Estado por figura:
- Desarrollo (Figura 20): PNG del usuario en `amb_desarrollo.png`; texto a 9,1 pt, pero exportado a 95 dpi; pendiente reexportar a 300 %.
- QA (Figura 21): XML entregado; «misma imagen que en Desarrollo» pasa a la etiqueta de ECR; se retira «ensayo de wms_only». Pendiente PNG.
- Preproducción (Figura 22): XML entregado; el sitio emulado pasa dentro de sa-east-1 y se rotula «sin túnel»; «en 2 zonas» pasa al ALB; ambos despliegues conservan el paso 5 porque ocurren juntos, y la flecha conserva «promoción y reconexión» (ensayo de 4.2.4.3). Pendiente PNG y quitar el giro de página en el `.tex`.
- Producción (Figura 23): XML entregado; lienzo vertical con on-premise bajo la nube; la descarga por endpoints y Ansible (F-02, CD Talca) conservan ambos el paso 7. Pendiente PNG y quitar el giro de página en el `.tex`.
- Recuperación ante Desastres (Figura 24): XML entregado; se retira «≈ 7.700 km de la primaria» porque repite la Tabla 36 (la cifra es correcta); las dos cuentas quedan apiladas y el on-premise abajo. Pendiente PNG.

El término «azul-verde con canario» se define en su primer uso, el paso 5 de Preproducción; Producción remite a ese ensayo.

Texto: en `04/partes/4.2_fisica/11_j_despliegue.tex`, cada ambiente cita su figura, la figura va seguida de `\FloatBarrier` y luego una lista numerada con los mismos números de la figura; los pasos compartidos (5 en Preproducción, 7 en Producción) se explican con una sublista.

## Cierre 2026-10-07

- El usuario subió los cinco PNG (zoom 300 %, borde 0). Medición en `entrega/LAFROX-Subdocumento4.pdf`: Figuras 20 a 24 a `\textwidth`, ≈ 285 dpi, texto ≈ 9,07–9,10 pt.
- Preproducción y Producción dejan de ir giradas: figuras verticales a `\textwidth`. Producción y Recuperación usan `[!htbp]` y `[!ht]` sin `\FloatBarrier` para no dejar páginas a medio llenar.
- Punto y coma: a pedido del usuario se retiraron los 56 de la prosa, listas y tablas de 4.2.4, con puntos, comas o listas sin cambiar el contenido. Se conservan los que separan referencias dentro de una cita entre paréntesis. En el resto del Subdocumento 4 quedan unos 420 fuera de citas.
