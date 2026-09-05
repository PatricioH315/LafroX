---
name: cloud-architecture
description: Justificar y diseñar la arquitectura híbrida nube+on-premise (RT-03) del proyecto TFEP-01/2026, respondiendo la matriz de emplazamiento y el carácter híbrido obligatorio del Art. 16°. Use al justificar cada componente a nube u on-premise según latencia, criticidad, volumen, acoplamiento, elasticidad y regulación. Trigger: "híbrido", "nube", "on-premise", "emplazamiento", "RT-03", "RT-16.1", "matrix de emplazamiento".
---

# cloud-architecture — Arquitectura híbrida nube + on-premise

Diseña y justifica el emplazamiento híbrido obligatorio (Art. 16°, RT-16.1): la
carga principal en nube pública + componentes **on-premise**. No se admiten
propuestas solo-nube ni solo-on-premise.

## Criterios de emplazamiento (RT-03)

Asignar cada componente con justificación documentada según:

- **Latencia** (interfaz de picking, preventa, reparto en terreno).
- **Criticidad** (ventana de despacho 05:30–07:00 con cero indisponibilidad).
- **Volumen de datos** (260.000 líneas/mes, telemetría, DTE).
- **Acoplamiento físico** (cámaras, RS-485, sensores de temperatura).
- **Elasticidad** (septiembre casi duplica la carga por 3 semanas).
- **Regulación** (DTE, trazabilidad sanitaria).

## Anotación clave del caso

La operación es dispersa y de terreno: preventa, reparto, preparación y recepción
son en la calle/local del cliente con **14 h sin señal** (RT-03.10) y almacenes
sin internet. El componente on-premise debe operar de forma autónoma y degradada
ante la pérdida total del enlace con la nube. Emplazamiento con tabla que cubra
100 % de componentes y justificación por cada uno.

## Stack de referencia (lógica adoptada)

- Nube (analítica + DR): Aurora/RDS, S3 (POD/DTE), Kubernetes multi-zona, IaC Terraform.
- On-premise por CD: PostgreSQL+PostGIS, RabbitMQ, cache/colas locales, buffers offline.

## Cómo responder (Formulario T-12 / Subdoc 3 y arquitectura física T-11)

- Tabla de emplazamiento nube/on-premise con justificación por componente
  (ver RT-03 y su valor según caso).
- Evidenciar el carácter híbrido en la arquitectura (no un diagrama genérico).
- Declarar funciones NO disponibles en modo desconectado y el procedimiento manual
  que las suple (RT-03.13).

## Verificación

- No contradecir el cronograma de 56 meses ni las 5 innovaciones obligatorias.
- Cero vendor lock-in y mantenible por equipo TI de 4 personas.