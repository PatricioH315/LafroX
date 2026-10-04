# LafroX — Complemento CD-05: reserva comercial y custodia física

Fecha: 3 de octubre de 2026. Cambio de diseño coordinado autorizado al ejecutar el plan del Subdocumento 5. Complementa el SD4 convertido desde 732a9d6; no acredita aprobación del CLIENTE ni modifica retrospectivamente esa procedencia.

## Autoridad y protocolo

M2 nube conserva la reserva comercial; M2 del sitio conserva existencia física, movimiento y retención de disponibilidad. M3 confirma pedidos solo después de que M2 central haya recibido la retención local durable. La proyección consolidada y el esquema DMS son de lectura y no autorizan reservar por sí solos.

1. M2 central persiste pendiente y solicita retención con UUID, correlación, sitio, época, lote, ubicación, cantidad y versión de esquema.
2. El shipper del sitio lee por conexión saliente una cola FIFO de coordinación propia, con IAM por sitio, y entrega la solicitud a RabbitMQ local. Este transporte desarrolla M2/INT-03/04; no crea una llamada de nube hacia una API del sitio.
3. M2 local bloquea el agregado, valida Calidad y disponibilidad, y persiste retención, auditoría y outbox. Una repetición recupera el resultado anterior.
4. INT-03/04 devuelve el resultado a nube. M2 central confirma solo después de persistir el acuse; M3 obtiene el resultado por su UUID.
5. Cancelación o expiración central inicia liberación pendiente; el stock sigue retenido hasta el resultado durable local. Una retención consumida no se libera como si siguiera disponible.

Durante aislamiento cada sitio continúa recepción, movimientos y misiones asignadas dentro de su autoridad. No se confirma una nueva reserva remota sin respuesta del custodio. Una pérdida de acuse conserva la retención y estado incierto, evitando la doble promesa. Las épocas no se promueven durante partición; un cambio de autoridad exige conciliación y revocación de la anterior.

## Emplazamiento, seguridad y capacidad

La coordinación tiene colas separadas de erp-sync, reconciliación de eventos y trabajos de framework; los sobres JSON se validan antes de ejecutar reglas. Las colas por sitio las consume exclusivamente su shipper mediante sesión saliente; nube publica solicitudes y recibe resultados por los canales existentes. La única conexión iniciada desde nube hacia sitio sigue siendo DMS de Talca. erp-sync y ACL continúan en VM-04.

Dos mensajes lógicos por reserva y dos por liberación añaden 2N+2L al presupuesto antes de reintentos. Los 178.661/260.155 mensajes/día de 4-I y 4-W son la línea base publicada; el nuevo intercambio se estima aparte, se prueba y se incorpora al dimensionamiento antes de producción. No se declara validada su latencia dentro de la confirmación de pedido ni su capacidad de enlace por esta descripción.

## Invariantes y aceptación

- Una reserva central confirmada corresponde a retención local durable de misma identidad, época y cantidad.
- Disponible local = existencia libre menos retenciones activas; no puede ser negativo.
- Confirmar y liberar tienen un solo resultado efectivo, incluso con reenvíos o pérdida de acuses.
- Preparación consume retención; reconciliación central registra ese hecho sin emitir otro movimiento físico.
- Pruebas de última unidad multicanal, timeout antes/después del commit, liberación durante corte, época obsoleta y consumo antes de cancelación se ejecutan antes de liberar el contrato.

El SD5 2.0 representa reserva, retencion_stock, épocas y referencias. Los escenarios documentales no acreditan pruebas de sistemas implantados. AL-OFF-01, AL-DTE-01 y AL-DR-01 mantienen sus exigencias. Frescura global de cinco minutos ante pérdida de todos los enlaces continúa como dependencia explícita del CLIENTE y prueba operacional; mostrar atraso no acredita cumplimiento.
