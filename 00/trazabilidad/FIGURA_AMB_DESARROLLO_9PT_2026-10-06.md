# Figura 20 — Ambiente de Desarrollo a 9 pt — 2026-10-06

Solicitud del usuario: arreglar el diagrama de Desarrollo de 4.2.4 y quitarle el texto innecesario. Antes, el texto de la figura se imprimía a unos 3,7 pt (lienzo de 1550 u con texto de 13 u a `\textwidth`).

Archivos:
- Fuente nueva: `04/figuras/fuentes/fisica/A1_Ambiente_Desarrollo_9pt.drawio` (588 × 324 u, texto 12 u).
- Exportación vectorial: `04/figuras/fisica/ambientes/amb_desarrollo_9pt.pdf`.
- `04/partes/4.2_fisica/11_j_despliegue.tex`: la Figura 20 usa el PDF nuevo a `\textwidth`.
- Se conservan sin cambios `A1_Ambiente_Desarrollo.drawio`, `amb_desarrollo.png` y `generar_diagramas_ambientes.py`.

Medición en `entrega/LAFROX-Subdocumento4.pdf` (p. 88): todo el texto de la figura mide 9,04 pt; carta vertical, sin desbordes.

Texto retirado (lo cubre el párrafo de la figura o el resto de 4.2.4):
- Recuadro «Cadena de entrega» e ícono «Equipo de desarrollo»; la secuencia empieza en GitLab CI, como en el texto.
- «(suscripción)» y «controles del pipeline» bajo GitLab CI; «construye la imagen (SLSA nivel 3)» bajo CodeBuild (SLSA nivel 3 se declara en el párrafo del pipeline).
- Rótulo de flecha «con la configuración y los secretos del ambiente» (está en el párrafo) y «Angular» en «portales Angular».
- Marco exterior «AWS Cloud · organización AWS Control Tower» (Control Tower se declara en el párrafo de cuentas); «Desarrollo» en el rótulo de la VPC y «(São Paulo)» en el de la región.
- Prefijos «AWS»/«Amazon» en CodeBuild, ECR, S3 y CloudFront.

Se conservan: tipo de ambiente, pasos 1–5 de izquierda a derecha, cuenta, región, VPC 10.104.0.0/16, N-01 a N-03, N-04, imagen firmada y S3 privado servido por CloudFront.
