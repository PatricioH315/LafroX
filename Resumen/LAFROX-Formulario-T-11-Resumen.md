# LafroX — Resumen del Formulario T-11: Especificaciones técnicas

[Índice de resúmenes](README.md) · [Formulario original](../04_arquitectura/LAFROX-Formulario-T-11.md)

## Para qué sirve y cómo leerlo

Es el inventario detallado de hardware, plataforma, red, nube y software que materializa la arquitectura. La tabla identifica **componente, producto/servicio, lugar, cantidad y justificación**. El código de componente conecta cada fila con el emplazamiento del SD4.

No conviene sumar cantidades sin distinguir unidades instaladas, reserva y crecimiento: una fila puede representar equipos, licencias, servicios, planes o capacidad.

## Qué familias contiene

- Cómputo y almacenamiento: clúster de **tres servidores en Talca**, respaldo local y custodia externa.
- Borde: **dos servidores de Concepción**, activo/en espera, y **seis mini-PC de cross-docking más uno de reserva**.
- Red y seguridad: perímetros, switches, inalámbrica, fibra, LTE, satélite y túneles.
- Terreno: terminales de preventa, reparto y bodega, impresoras, pagos y registro térmico.
- Recinto técnico y gabinetes: energía, climatización, protección, racks y acceso.
- Plataforma de nube y software base: componentes con su función, región y licenciamiento.

Véase [la tabla completa](../04_arquitectura/LAFROX-Formulario-T-11.md#formulario-t-11-especificaciones-t%C3%A9cnicas-ofertadas).

## Cantidades y responsabilidades

Las reservas de dispositivos y componentes críticos siguen el **10 % redondeado hacia arriba**, con excepciones justificadas por componente. El parque inicial de reparto usa **96 instalados + 10 de reserva = 106** por fila correspondiente; el año 3 pasa a **110 + 11 = 121**. Los termógrafos son **28 + 3 = 31**; los repuestos no aumentan la ingesta térmica normal.

El formulario asigna compra de hardware de terreno al CLIENTE y provisión on-premise al adjudicatario; este último instala, integra y mantiene. SD6 asigna al CLIENTE la compra de sala técnica: la responsabilidad difiere entre fuentes y requiere coordinación, sin que el resumen la resuelva.

## Dónde está el fundamento

SD4 §4.2.1 explica selección, §4.2.2 ubicación y Anexo 4-W los cálculos. La cantidad inalámbrica depende del estudio de cobertura; cantidades y características declaradas no acreditan entrega, instalación ni ensayo.

El [resumen del SD4](LAFROX-Subdocumento4-Resumen.md) permite ubicar el conjunto y el [resumen de sus anexos](LAFROX-Subdocumento4-Anexos-Resumen.md) conduce a la memoria.

---

**Fuente y actualización:** documento local vigente al 8 de octubre de 2026. Resumen elaborado con asistencia de Codex; no acredita aprobación del CLIENTE ni revisión humana adicional.
