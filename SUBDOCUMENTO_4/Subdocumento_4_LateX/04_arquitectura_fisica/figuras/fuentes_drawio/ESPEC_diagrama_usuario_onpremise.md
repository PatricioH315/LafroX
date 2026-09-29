# Parte on-premise del diagrama general del usuario (referencia de diseño)

Transcripción fiel del diagrama general del usuario (su XML no está en disco). La parte de nube del
mismo diagrama es idéntica al diagrama de nube embebido en `../Arquitectura_Fisica_Nube.drawio.png`
(chunk tEXt "mxfile"). Íconos: clip art de draw.io, style `image;html=1;image=img/lib/clip_art/<ruta>`.

Estilo común: contenedor de sitio = rectángulo blanco, borde #475569, strokeWidth=2, título arriba-izquierda
negrita. Subgrupos = rectángulo redondeado dashed, borde #94a3b8, título arriba-izquierda negrita #334155.
Aristas: #475569, strokeWidth 1.5, ortogonales. Fila de sitios bajo la nube, de izquierda a derecha:
CD Talca, CD Concepción, Cross-docking × 3. Cada firewall de sitio sube con una línea a la VPC Hub
(Transit Gateway) de la nube.

## CD Talca · sala técnica
- Fibra (`networking/Modem_128x128.png`) → subgrupo "Firewall · par HA" [activo, pasivo: `networking/Firewall_02_128x128.png`, línea dashed "HA" entre ambos].
- LTE (`networking/Wireless_Router_N_128x128.png`) — dashed "respaldo" → subgrupo Firewall.
- Subgrupo Firewall → subgrupo "Switching" [core a, core b, gestión: `networking/Switch_128x128.png`].
- Subgrupo Firewall → (sube) VPC Hub / Transit Gateway.
- Switching → subgrupo "Máquinas virtuales" (dos flechas desde el borde inferior de Switching).
- Switching (gestión) — dashed morado #8C4FFF rótulo "DMS" → VM-02 PostgreSQL.
- Máquinas virtuales: VM-01 WMS Core (`computers/Virtual_Machine_128x128.png`), VM-02 PostgreSQL (`computers/Database_128x128.png`), VM-03 RabbitMQ (`computers/Virtual_Application_128x128.png`), VM-04 ACL del ERP (`computers/Data_Filtering_128x128.png`), VM-05 cache Keycloak (`general/Keys_128x128.png`), VM-06 ADOT + SSM (`computers/Software_128x128.png`).
- VM-01 → VM-02; VM-01 → VM-03; VM-01 → VM-05.
- VM-04 — ERP 2017 (`computers/Server_Rack_128x128.png`, fuera del subgrupo, a la izquierda).
- Máquinas virtuales → subgrupo "Respaldo" [NAS WORM: `computers/Server_Tower_128x128.png`].
- Subgrupo "Bodega" [Wi-Fi 6E: `networking/Wireless_Router_128x128.png`; Terminales: `computers/IBM_Tablet_128x128.png`, arista "Wi-Fi" Terminales→Wi-Fi 6E; Impresoras de andén: `computers/Printer_128x128.png`] — "LAN" → Switching.
- Subgrupo "Cadena de frío" [Sensores: `shape=mxgraph.aws4.sensor` (fill #7AA116) → Gateway IoT: `mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.greengrass`] — "MQTTS y bloqueo de despacho" → Switching.

## CD Concepción · gabinete de borde
- Fibra (Modem) → Firewall (Firewall_02, rótulo a la derecha); LTE (Wireless_Router_N) — dashed "respaldo" → Firewall.
- Firewall → Switch (Switch_128x128); Firewall → (sube) VPC Hub / Transit Gateway.
- Switch → subgrupo "Servidor Proxmox · nodo único": VM-C01 WMS Core (Virtual_Machine), VM-C02 PostgreSQL (Database), VM-C03 cache Keycloak (Keys), VM-C04 RabbitMQ, shipper y ADOT (Virtual_Application).
- VM-C01 → VM-C02; VM-C01 → VM-C03; VM-C01 → VM-C04.
- Subgrupo "Bodega" (igual a Talca) — "LAN" → Switch.
- Subgrupo "Cadena de frío" (Sensores → Gateway IoT) — "MQTTS y bloqueo de despacho" → Switch.

## Cross-docking × 3
- Starlink (principal) (`telecommunication/Signal_tower_on_128x128.png`) → Firewall compacto (Firewall_02).
- LTE doble SIM (Wireless_Router_N) — dashed "respaldo" → Firewall compacto.
- Firewall compacto → Switch compacto (Switch_128x128) → subgrupo "Mini-PC industrial · Docker" [un ícono Virtual_Machine rotulado "WMS, PostgreSQL, RabbitMQ, Caché de identidad, ADOT"].
- Firewall compacto → (sube) VPC Hub / Transit Gateway.
- Subgrupo "Operación" [Escáneres GS1: IBM_Tablet] → Mini-PC.
