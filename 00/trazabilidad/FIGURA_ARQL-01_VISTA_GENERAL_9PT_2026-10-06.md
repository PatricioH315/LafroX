# Figura 1 (ARQL-01) — vista general a 9 pt — 2026-10-06

Solicitud del usuario: rehacer la legibilidad de la vista general de la arquitectura lógica a ≥ 9 pt, conservando el esquema por capas, y corregir faltantes y sobrantes.

Decisiones del usuario:
- Una sola página; los módulos M1–M12 quedan solo con su título (las 72 funciones se retiran de la figura).
- Donde la figura contradecía al texto de 4.1, manda el texto.

Archivos:
- Fuente nueva: `04/figuras/fuentes/logica/ARQL-01_Vision_general_9pt.drawio` (590 × 759 u, texto 12 u).
- Exportación vectorial: `04/figuras/logica/ARQL-01_Vision_general_9pt.pdf`.
- `04/partes/4.1_logica/04_capas_de_la_arquitectura.tex`: la Figura 1 usa el PDF nuevo a `\linewidth`.
- El PNG anterior (`figuras/logica/cambios laravel/ARQL-01_Vision_general.png`) y el XML de origen del usuario se conservan sin cambios.

Medición en `entrega/LAFROX-Subdocumento4.pdf` (p. 13): todo el texto de la figura mide 9,05 pt; carta vertical, sin desbordes.

Cambios de contenido respecto del XML «(Arreglado) Arquitectura_Logica_Puelche»:
- Observabilidad alineada a ADR-14: CloudWatch para logs (12 + 24 meses), métricas (13 meses), trazas y tableros. Se retiran AMP, X-Ray y Grafana.
- Integración: se retira EventBridge; SNS difunde eventos y alertas. Se agregan los adaptadores de pago y mapas, y los sistemas externos (ERP 2017 y SII, cadenas del canal moderno, pasarela de pago y GPS/mapas).
- Seguridad: caché del verificador local con TTL de 24 h (antes 8 h); se agregan EDR CrowdStrike Falcon y MDM sin códigos internos.
- Borde y puerta de enlace: se agregan Lambda autorizadora (JWT), Verified Access para consolas y NLB + OpenAS2 para AS2. El flujo queda CloudFront/WAF → API Gateway → ALB → módulos; las apps entran por el borde.
- Se agrega la puerta de API local del sitio (WMS: M1, M2, M5, M8, M9).
- Datos: los 15 dominios lógicos de 4.1.5 en la nube; en sitios, copia local de BD_INVENTARIO, BD_PREPARACION, BD_CALIDAD_TRAZABILIDAD y BD_MAESTROS_CONF (antes duplicados sin aclarar y con BD_RUTAS local).
- Se corrigen «Applicación» y «Gerente de operacions» y se retiran los códigos D1, D13, D15 y N-13.
- Capas nombradas como en 4.1.3 (Capa 1 a Capa 8).

Diferencia menor con el texto: el ALB aparece en la Capa 3 (después de API Gateway) para mostrar el flujo; la lista de 4.1.3 lo menciona dentro de la Capa 2.
