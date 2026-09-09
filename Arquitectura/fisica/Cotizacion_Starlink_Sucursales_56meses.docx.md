  
**COTIZACIÓN CONECTIVIDAD STARLINK**

**Sitios operacionales — período completo del contrato**

*Distribuidora Puelche S.A. — Licitación TFEP-01/2026, Caso Logística*

**Preparado para: Departamento de Estructura Física**

Alcance: 5 sitios — CD Talca, CD/oficina Concepción, cross-dock Curicó, Chillán y Los Ángeles

Vigencia de la cotización: 56 meses (duración total del contrato)

Septiembre de 2026

# **1\. Por qué se cotiza esta conectividad**

Las Bases del caso exigen que la solución sostenga la operación aun cuando falle el enlace de datos, y en dos de los cinco sitios ese enlace hoy no existe de forma confiable:

| Sitio | Problema documentado |
| :---- | :---: |
| CD Talca | Tiene fibra, pero se corta 4 veces al año y no cuenta con enlace de respaldo. El centro debe sostener recepción, preparación y despacho durante 24 horas continuas sin enlace (RT-03.10), y la ventana de despacho de 05:30 a 07:00 exige indisponibilidad cero. |
| CD / oficina Concepción | No tiene enlace de respaldo. Un corte deja sin conectividad a toda la operación administrativa y de coordinación de la plataforma. |
| Cross-dock Curicó | Conectividad exclusivamente por red móvil, sin respaldo. Ventana de operación de solo 3 horas en la madrugada, sin margen para intermitencias. |
| Cross-dock Chillán | Misma condición que Curicó: solo red móvil, sin respaldo, ventana de 3 horas. |
| Cross-dock Los Ángeles | El caso más crítico: la señal móvil es intermitente justo entre las 03:00 y las 05:00, que es exactamente su ventana de operación. El sitio pierde cobertura cuando más la necesita. |

Sin resolver esto, la plataforma no puede cumplir los requisitos no funcionales del proyecto: disponibilidad ≥ 99,9% en servicios críticos, indisponibilidad cero en el despacho de la mañana, y operación de 24 horas sin enlace en el centro de distribución. Esta cotización cubre únicamente los 5 sitios fijos; no incluye conectividad a bordo de los camiones (ver el documento "Propuesta de Conectividad Satelital", planes 1 y 2, para esa alternativa).

# **2\. Solución propuesta**

Un enlace Starlink fijo por sitio, operando como respaldo automático en los dos centros de distribución y como enlace principal en las tres plataformas de cross-docking (que hoy no tienen fibra ni la tendrán en el horizonte de este contrato).

* Hardware: kit Starlink fijo estándar / alto rendimiento por sitio, con conmutación automática al enlace satelital cuando cae el enlace principal (en los CD) o como único enlace disponible (en los cross-dock).

* Plan de datos empresarial con prioridad de red, dimensionado según la intensidad de uso de cada sitio: mayor capacidad en los centros de distribución (más dispositivos, mayor volumen de datos) y capacidad media en los cross-dock (ventana operativa corta, menor volumen).

* Cobertura contractual: la cotización se extiende por los 56 meses de duración del contrato, para que el enlace quede disponible desde la habilitación de ambientes (Hito H3, mes 6\) y se sostenga durante toda la fase de Operación (36 meses, hasta el mes 56).

# **3\. Detalle de la cotización**

## **3.1 Hardware (pago único)**

| Sitio | Rol del enlace | Hardware (CLP) |
| :---- | :---: | :---: |
| CD Talca | Respaldo automático | $350.000 |
| CD / oficina Concepción | Respaldo automático | $350.000 |
| Cross-dock Curicó | Enlace principal | $350.000 |
| Cross-dock Chillán | Enlace principal | $350.000 |
| Cross-dock Los Ángeles | Enlace principal | $350.000 |
| **Subtotal hardware** |  | **$1.750.000** |

Se agrega una reposición de hardware del 15% del valor (repuestos y reemplazo por ciclo de vida durante los 56 meses del contrato, conforme exige RT-08.13): $262.500 CLP.

## **3.2 Plan mensual de datos**

| Sitio | Plan | Mensual (CLP) | 56 meses (CLP) |
| :---- | :---: | :---: | :---: |
| CD Talca | Empresarial 1 TB prioritario | $243.000 | $13.608.000 |
| CD / oficina Concepción | Empresarial 1 TB prioritario | $243.000 | $13.608.000 |
| Cross-dock Curicó | Empresarial 500 GB prioritario | $138.000 | $7.728.000 |
| Cross-dock Chillán | Empresarial 500 GB prioritario | $138.000 | $7.728.000 |
| Cross-dock Los Ángeles | Empresarial 500 GB prioritario | $138.000 | $7.728.000 |
| **Subtotal plan mensual** |  | **$900.000** | **$50.400.000** |

# **4\. Resumen de la cotización**

| Concepto | Monto CLP | Monto USD aprox. |
| :---- | :---: | :---: |
| Hardware — 5 sitios | $1.750.000 | $1.944 |
| Reposición de hardware (15%, durante 56 meses) | $262.500 | $292 |
| **CAPEX total** | **$2.012.500** | **$2.236** |
| Plan mensual — 5 sitios | $900.000 | $1.000 |
| **OPEX total (56 meses)** | **$50.400.000** | **$56.000** |
| **TOTAL COTIZACIÓN (56 meses)** | **$52.412.500** | **$58.236** |

Tipo de cambio referencial: USD $900 CLP (Formulario E-24 de las Bases Administrativas). El monto de reposición de hardware es un supuesto propio y debe incorporarse al Registro de Supuestos del proyecto.

# **5\. Condiciones y supuestos de esta cotización**

* Cotización exclusiva para los 5 sitios fijos; no incluye conectividad para camiones.

* No incluye obra civil, cableado interno del sitio ni el estudio de cobertura Wi-Fi al interior de las cámaras de frío (RT-03.24), que se cotizan por separado.

* Se asume instalación del enlace en el mes de habilitación de ambientes (Hito H3, mes 6); si se requiere antes, para pruebas de sitio, se factura desde el mes de instalación efectiva.

* Los valores de plan mensual son de referencia según tarifas empresariales vigentes en Chile; deben confirmarse en la etapa de compras del proyecto por variación de tipo de cambio y de tarifas del proveedor.

* No incluye la conectividad de respaldo entre el sitio on-premise y la nube que exige RT-03.17 (conmutación automática ≤ 5 minutos) como enlace redundante de arquitectura; Starlink actúa aquí como ese enlace redundante físico.