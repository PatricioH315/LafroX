# LafroX — Resumen del Formulario T-12: Cumplimiento y trazabilidad

[Índice de resúmenes](README.md) · [Formulario original](../03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md)

## Para qué sirve

Relaciona lo exigido con el compromiso de oferta, el componente que lo realiza, el paquete que lo construye y la prueba prevista. Es la consulta principal cuando se pregunta «¿dónde se atiende este requisito?».

## Cómo leer sus dos partes

[La Parte A](../03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md#parte-a--requerimientos-del-caso-y-de-las-bases) responde requisitos del caso y del catálogo: **181 filas RF** —175 ofertados más seis materias complementarias— y **90 RNF** —86 ofertados más cuatro alias/materias absorbidas—. RF significa funcional; RNF, condición de calidad u operación.

Las columnas relacionan identificador, descripción, compromiso, módulo, EDT, prueba, sección, criterio y origen. Un código RF o RNF puede remitir a una materia absorbida por un requisito transversal; no todos los renglones agregan una función nueva.

[La Parte B](../03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md#parte-b--requisitos-de-las-bases-t%C3%A9cnicas-transversales) responde **374 RT**, requisitos de las Bases Técnicas Transversales. Conserva carácter obligatorio, deseable o según caso; «según caso» no significa opcional. Los valores del caso prevalecen cuando endurecen el requisito.

## Qué significan las respuestas

- **Sí (E1/E2/ambas):** compromiso que deberá demostrarse en la etapa indicada.
- **No aplica:** existe una decisión de diseño que justifica la inaplicabilidad.
- **No ofertado:** capacidad deseable no comprometida.
- **Sí (licitación):** acreditación prevista mediante materiales del proceso de licitación.

La columna «Cumple» no es un registro de pruebas ya ejecutadas. OTIF de **95 % en mes 32** y metas anuales tienen verificación posterior a la aceptación provisional de marcha blanca. Véanse [las convenciones](../03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md#convenciones).

## Decisiones que conviene conservar

RF-03.11/RF-03.12 mantienen el precio acordado al capturar el pedido y bloquean diferencias de integración antes de facturar. **RT-05.30** se oferta por INN-03; **RT-05.10 y RT-05.24** siguen como deseables no ofertados. El bloque RT-26 remite a SD13/T-19 para innovaciones.

Los códigos RF-14.01–05-BTT evitan confundir seguridad de Bases con telemetría del caso. La columna EDT conduce a T-14 y la prueba al comportamiento que debe verificarse, no solo al nombre de una herramienta.

## Lectura relacionada

El [resumen de SD3](LAFROX-Subdocumento3-Resumen.md) explica alcance y reglas; [sus anexos](LAFROX-Subdocumento3-Anexos-Resumen.md) contienen los requisitos completos. T-14/T-15 programan la ejecución. La revisión humana pendiente y las verificaciones futuras conservan su estado.

---

**Fuente y actualización:** documento local vigente al 8 de octubre de 2026. Resumen elaborado con asistencia de Codex; no acredita aprobación del CLIENTE ni revisión humana adicional.
