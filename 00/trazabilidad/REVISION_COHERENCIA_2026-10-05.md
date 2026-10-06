# Revisión de coherencia — 2026-10-05

Revisión hecha sobre los PDF compilados del 3 de octubre (commit 732a9d6): cuerpo de 164 p., anexos de 94 p. y T-11 de 33 p. Claude leyó los tres archivos completos y cotejó con las Bases. GPT (gpt-6-luna, esfuerzo alto, solo lectura) revisó en paralelo tres frentes: A lógica, B física/números y C transversal. No se modificó ningún archivo del subdocumento.

Los hallazgos marcados (GPT) los propuso Codex y Claude los verificó. Las figuras solo se reportan: el usuario las edita.

## Alta

| # | Hallazgo | Dónde | Corrección mínima |
|---|---|---|---|
| 1 | El mini-PC E-01 tiene un solo NVMe de 512 GB y no declara RAID. RT-03.14 y BA Art. 16.4 exigen que el almacenamiento local tolere la falla de un disco y que se declare el nivel RAID. Talca (Ceph), Concepción (RAID 10) y la NAS (RAID 6) sí lo cumplen. | T-11 p.4 (E-01); cuerpo p.77 y Tabla 20 p.124; ADR-10 | Especificar 2 NVMe en RAID 1 para E-01 y declararlo en T-11, en la Tabla 20 y en ADR-10. |
| 2 | Las declaraciones de IA siguen como indicadores de IA: dicen «Revisión final no realizada», «láminas de Tomás», «archivo de trabajo… no conforme» y «22 anexos» (son 23). A.35 no incluye 4-W y A.36 no cubre 4.2, 4.3 ni T-11. *(Pendiente por decisión del usuario.)* | cuerpo p.164; anexos pp.91–94 | Completar con quien revisó y cubrir todos los apartados. |
| 3 | (GPT) En la Figura 24 la réplica de us-east-1 recibe la imagen «desde el ECR de sa-east-1». Según el texto, usa el ECR replicado y no depende del registro primario. | Fig. 24 p.103 frente a p.107, p.160 y T-11 p.23 | Usuario: cambiar el origen en la figura a ECR us-east-1. |

## Media

| # | Hallazgo | Dónde | Corrección mínima |
|---|---|---|---|
| 4 | El plazo de retiro sanitario de menos de 2 h se cita de tres formas distintas. El requisito está en el cap. 18, criterio 1, del caso; el cap. 9.5 solo dice «en horas». | 4.1 p.40 «(Cap. 18)»; 4.2 p.117 «(PUCV, 2026a, cap. 9, p. 18)»; 4-A p.7 «Cap. 9.5: retiro < 2 h» | Unificar con «PUCV, 2026a, cap. 18» y su página, en formato APA. |
| 5 | (GPT) La Figura 19 no dibuja en us-east-1 el ECR replicado ni las colas SQS/SNS vacías que usa el paso 8 de la conmutación. | Fig. 19 p.93 frente a p.107, p.160 y T-11 p.26 | Usuario: agregarlos o declarar que la vista los omite. |
| 6 | Se remite a otros subdocumentos sin comprobar que existan: «plan de calidad (Subdocumento 9)», «capítulo de servicios» y supuestos S-xx «en el Subdocumento 3». Es el mismo riesgo que tenía el Subdocumento 11. | cuerpo p.104, p.37, p.73; anexos p.64 y p.74; T-11 p.2 | Confirmar que existen o quitar las menciones. |
| 7 | RT-08.04 es obligatorio para «todo el equipamiento», pero 4.2.1.2 cubre las impresoras, balanzas y estaciones con «unidades alternativas» sin declararlo como desviación. | cuerpo p.74 | Declarar la desviación y su justificación (o la doble fuente). |
| 8 | Las posiciones de flota no salen de sa-east-1. Sin embargo, alimentan el costo de servir de la analítica, y esa analítica se copia a us-east-1. No se dice que la copia excluya las posiciones crudas. | 4.2.3.2 p.91; Tabla 37 p.157; 4.3.2.2 p.156 | Agregar una frase: la copia analítica lleva kilómetros agregados, no posiciones. |
| 9 | (GPT) C-03 cita la «ficha del fabricante», que no figura en las Referencias del T-11. | T-11 p.11 y p.33 | Agregar la referencia APA o quitar la atribución. |

## Baja

| # | Hallazgo | Dónde |
|---|---|---|
| 10 | Diez encabezados `\paragraph{… .}` se imprimen con doble punto («Eventos canónicos del dominio..»), porque la plantilla ya agrega el punto. | `04/partes/4.1_logica/04_capas_de_la_arquitectura.tex` l.177, 186, 211, 218, 246… |
| 11 | Erratas: «INT11» (p.25), «RT10.03» (p.54), «SV04» (4-W.6, p.81). | — |
| 12 | La Tabla 35 dice 7.000 W y la Tabla 34, 7.020 W de carga TI de diseño. | p.149–150 |
| 13 | «2 × (168 ÷ 40) = 10» da 8,4; debe decir 2 × ⌈168 ÷ 40⌉ = 10. | 4-W.7 p.81 |
| 14 | (GPT) «260.000 ÷ 22,14 × 5 ≈ 58.710» da 58.717 con 22,14; el valor sale de 22,142857. Basta escribir «31.000 ÷ 1.400» o «≈ 58.717». | 4-G p.16; Tablas 26, A.10 y A.30 |
| 15 | (GPT) En el cuerpo, el terminal Starlink está en la bandeja de R02; en T-11 no aparece en esa bandeja. | p.151 frente a T-11 p.20 |
| 16 | (GPT) Talca tiene 2 gateways IoT, pero las Figuras 15 y 28 dibujan uno (solo reportar). | pp.69 y 147 |
| 17 | (GPT) El 3-2-1-1-0 dice «tres copias» y enumera cuatro elementos; aclarar que las instantáneas y D-05 son la misma copia. | p.116 |
| 18 | La Tabla 7 incluye las UPS de piso, pero no las UPS de borde (Concepción 3 kVA y cross-docking 0,75 kVA), que sí están en T-11. | p.72 |
| 19 | «Integración con legados… M1, M5, M7 y M11» omite M8, que también usa la ACL (p.45; 4-L n.° 12). | p.55 |
| 20 | Referencias sin número: «conforme a la Tabla de 4.2» (es la Tabla 16) y «Tabla de correspondencia de 4.2.2» (es la Tabla 8). | p.55, p.11, anexos p.30–31 y p.57 |
| 21 | El título «Anexo 4-W. Memoria…» usa punto; los demás anexos usan raya «Anexo 4-A — …». | anexos p.3 y p.64 |
| 22 | Paréntesis anidado: «(numeral 4.1 … (PUCV, 2026b, cap. 4, p. 10))». | p.104 |

### Cierre de los bajos (2026-10-05)

- Aplicados y compilados sin advertencias: 10 (25 encabezados), 12, 13, 14, 17, 18, 19, 20 (Tabla 16 y Tabla 8), 21 y 22.
- 11, descartado: falso positivo. El LaTeX dice «INT-11», «RT-10.03» y «SV-04»; el guion se perdió al extraer el texto del PDF en el corte de línea.
- 13: el símbolo ⌈ ⌉ no existe en la fuente Inter, así que el redondeo se explicó en palabras.
- 15: Figura 29 y T-11 coinciden (bandeja de R02 = ONT + router LTE); se corrigió el cuerpo (4.3.1.4).
- 16: queda para el usuario (figuras 15 y 28).
- 18: no se agrega fila de UPS de borde para Talca, porque su UPS es la de la sala (Tabla 34).

### Cierre de altos y medios (2026-10-05)

- **1 E-01:** dos SSD industriales de 512 GB en RAID 1 por software. Se aplicó en T-11, 4.2.2.1, Tabla 20 (con su comentario) y ADR-10, con la justificación frente a RAID 5/10 que exige RT-03.14.
- **4 Retiro y ruta:** se unificó la cita en «PUCV, 2026a, cap. 18, p. 34» (criterios 1 y 7; página impresa verificada en el PDF del caso). Se aplicó en 4.1.4, Tabla 17 y Anexo 4-A.
- **6 Subdocumentos:** por decisión del usuario, no se mencionan subdocumentos superiores (sí los inferiores). Se quitaron el Subdocumento 5 y el capítulo 5 (4 lugares), el Subdocumento 9 y el «capítulo de servicios» (el SOC remite ahora al Anexo 4-W). Se conservan el Subdocumento 3 y el Formulario T-12, que pertenece al Subdocumento 3.
- **7 RT-08.04:** se ignora por decisión del usuario.
- **8 Posiciones de flota:** la copia analítica excluye las posiciones. Se aplicó en 4.2.3.2, 4.3.2.2, Tabla 37 y ADR-19.
- **9 T-11:** se quitó «según ficha del fabricante».

### Revisión del T-11 frente al documento (2026-10-05)

- Los 36 componentes del catálogo de 4.2.2 están en el T-11, y las cantidades, potencias y productos coinciden con la Tabla 7, 4.2.1.2, la Tabla 34, la Tabla A.33, 4-W y las ADR.
- Aplicado en el T-11:
  - Nombres alineados con 4.2.2: A-01 pasa a «Motor WMS» y F-02 a «Gestión de parches»; «núcleo» en lugar de «core»; «rack» R01/R02 en lugar de «gabinete».
  - La columna Cantidad queda solo con cantidades (N-04, N-05, N-09, N-13); el detalle pasó a Producto o Justificación.
  - La columna Ubicación queda sin citas.
  - E-01: se declara el diseño sin ventilador y la operación hasta 60 °C, que justifica 4.2.1.2.
- Propuesto al usuario (pendiente):
  - RT-08.12: caídas e IP por dispositivo.
  - RT-08.13: ciclo de vida, repuestos y reposición.
  - RT-08.06: equipamiento nuevo con garantía.
  - Especificar la climatización y el control de acceso del borde de Concepción y el medio de respaldo rotativo.
  - «El equipamiento físico lo adquiere el CLIENTE»: el caso (cap. 11) lo limita al hardware de terreno, y BA Art. 14.2 incluye en el alcance la provisión de los componentes on-premise.

## Verificado coherente

- Las cantidades coinciden en Tabla 7, 4.2.6.4, 4-W.3 y T-11: 186 terminales en operación y 205 con reserva (22 de congelado y 183 estándar), 233 a tres años (Talca 151), 69/106 en terreno, 72 AP, 7 módulos y 24 sondas, 3+1 gateways, 28+3 termógrafos, 380 equipos en MDM, 209 agentes EDR, 8 planes LTE y 20 túneles.
- Los mensajes 178.661 / 260.155 cuadran por grupo (Tablas 26, A.10 y A.30). También cuadran los drenajes 1,68/1,09/0,27 GB, que equivalen a 1,87/1,21/0,30 Mbps, y la Tabla 27, que coincide con la A.31.
- TPS: 12,30 / 14,66 / 3,76–6,94, coherentes con el perfil A.29. Tareas Fargate 2/2/2/4/7 con techo de 8; Aurora xlarge.
- VMs (A.32 frente a Tabla 28), Ceph 1,92 TB, N+1, energía Talca (5.850 → 7.020 W, UPS 10 kVA, PUE ≈ 1,5, generador 20 kVA) y UPS de borde (Tabla A.33 frente a T-11).
- Ventana dominical: 203/101 equipos, tandas de 18/9 y 12 domingos.
- Etapas según BA Art. 17; Tabla 16 conforme a Art. 78.2; MTTR, cambios fallidos y RTO/RPO al 100 % según Art. 78.3; residencia según Art. 23; regiones sa-east-1/us-east-1; conmutación de 135 min.
- Los 142 RT citados existen en las Bases. RT-03.13, RT-10.05, RT-16.14, RT-16.30 y RT-17.01 se citan con su versión del caso.
- Coherentes entre cuerpo, anexos y T-11: ADR-01 a ADR-22 frente a la Tabla 3; colas ERP (D33); guía sin WAN (D32); Starlink en espera caliente; identidad 8/14/24/26 h; Concepción no es sitio de DR.
- Inventario 4-N: 37 IDs transversales + 12 módulos = 49.
- No hay precios.
