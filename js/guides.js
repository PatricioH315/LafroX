/* Ruta explicativa por perfil: pasos sugeridos para usar el prototipo según el actor.
   Cada paso es [título, qué hacer, ruta]. Se muestra en el inicio de cada perfil. */
(function (L) {
  L.guides = {
    evaluador: [
      ['Recorra el flujo de un pedido', 'Simule los 7 pasos de la preventa a la rendición, con crédito retenido y la excepción «local cerrado».', '/flujo'],
      ['Abra la app de reparto', 'Apague el interruptor de señal para ver el modo sin conexión y la cola de sincronización.', '/terreno'],
      ['Revise el proceso secundario', 'Cree una devolución y siga su flujo de aprobación en 5 etapas.', '/devoluciones'],
      ['Explore el tablero analítico', 'Cambie filtros y profundice desde un indicador hasta la entrega.', '/analitica'],
      ['Cambie de perfil', 'Desde el menú de usuario elija otro actor y compare su inicio, su menú y sus permisos.', '/perfil']
    ],
    'gerente-ops': [
      ['Mire el tablero de hoy', 'Indicadores, alertas y ocupación en un solo lugar. Puede reordenar los componentes.', '/tablero'],
      ['Revise las rutas en curso', 'Compare lo planificado con lo real y abra una ruta para ver sus entregas.', '/rutas'],
      ['Profundice en el OTIF', 'Entre al indicador, elija una ruta y llegue hasta la entrega que lo afectó.', '/analitica/otif'],
      ['Resuelva excepciones', 'Las decisiones pendientes llegan a su bandeja de tareas.', '/bandeja']
    ],
    planificador: [
      ['Revise la ruta propuesta', 'Abra el plan de mañana y compruebe secuencia y restricciones.', '/rutas'],
      ['Mire los pedidos por planificar', 'Filtre los pedidos confirmados que aún no tienen ruta.', '/pedidos'],
      ['Compare con la ruta real', 'En telemetría vea desvíos y datos de recorrido.', '/telemetria'],
      ['Atienda sus tareas', 'Aprobaciones y excepciones de planificación esperan en la bandeja.', '/bandeja']
    ],
    preventista: [
      ['Tome un pedido', 'Funciona sin señal: el pedido queda en cola y se envía al volver la conexión.', '/terreno/preventa'],
      ['Consulte a su cliente', 'Vea su crédito, su deuda y su historial antes de ofrecer.', '/clientes'],
      ['Siga sus pedidos', 'Revise en qué estado quedó cada uno y si ya sincronizó.', '/pedidos'],
      ['Revise su bandeja', 'Aquí llegan los pedidos retenidos por crédito u otra validación.', '/bandeja']
    ],
    conductor: [
      ['Inicie su ruta', 'Verá sus entregas en orden. Puede trabajar sin señal.', '/terreno'],
      ['Entregue y deje constancia', 'Registre la prueba digital; si el local está cerrado, marque el intento fallido.', '/terreno'],
      ['Registre una devolución', 'Indique producto y envases devueltos por el cliente.', '/devoluciones/nueva'],
      ['Rinda su turno', 'Cierre con efectivo y documentos para que Finanzas lo revise.', '/rendicion']
    ],
    'conductor-ext': [
      ['Inicie su ruta', 'Ingresó con su PIN y una asignación aprobada por despacho (máx. 16 h). Verá solo sus entregas.', '/terreno'],
      ['Entregue y deje constancia', 'Registre la prueba digital; si el local está cerrado, marque el intento fallido.', '/terreno'],
      ['Registre una devolución', 'Indique producto y envases devueltos por el cliente.', '/devoluciones/nueva'],
      ['Rinda su turno', 'Cierre con efectivo y documentos al terminar.', '/rendicion']
    ],
    preparador: [
      ['Continúe su misión', 'Siga el orden de picking que prioriza el producto que vence antes (FEFO).', '/preparacion'],
      ['Confirme la carga', 'Al terminar, deje la carga lista para que salga la guía electrónica.', '/preparacion'],
      ['Ayude en la recepción', 'Registre lote y vencimiento de lo que llega al andén.', '/recepcion/nueva']
    ],
    bodega: [
      ['Revise las recepciones del día', 'Controle lo recibido contra la orden de compra y las discrepancias.', '/recepcion'],
      ['Mire el inventario', 'Stock por zona, reservas y productos próximos a vencer.', '/inventario'],
      ['Supervise la preparación', 'Siga las misiones y la carga confirmada.', '/preparacion'],
      ['Evalúe devoluciones', 'Apruebe el destino de cada producto devuelto.', '/devoluciones']
    ],
    calidad: [
      ['Vea los lotes', 'Estado sanitario de cada lote, con su trazabilidad completa.', '/calidad'],
      ['Haga un simulacro de retiro', 'Elija un lote y obtenga los clientes afectados, con la meta de menos de 2 horas.', '/calidad/retiro'],
      ['Revise la cadena de frío', 'Abra las excursiones térmicas y decida la disposición del producto.', '/telemetria'],
      ['Atienda sus tareas', 'Los bloqueos y liberaciones esperan en la bandeja.', '/bandeja']
    ],
    comercial: [
      ['Revise la cartera', 'Rentabilidad y riesgo por cliente.', '/clientes'],
      ['Atienda el canal moderno', 'Pedidos EDI y sus excepciones por cadena.', '/canal-moderno'],
      ['Siga los indicadores', 'OTIF y fill rate, con filtros por canal.', '/analitica'],
      ['Mire los pedidos', 'Estado de los pedidos de sus clientes.', '/pedidos']
    ],
    finanzas: [
      ['Revise las rendiciones', 'Tipifique los descuadres de cada rendición del día.', '/rendicion'],
      ['Mire el costo de servir', 'Costo por cliente y por canal.', '/analitica/costo'],
      ['Controle crédito y cobranza', 'Clientes en mora y crédito disponible.', '/clientes'],
      ['Atienda sus tareas', 'Las aprobaciones de crédito esperan en la bandeja.', '/bandeja']
    ],
    ti: [
      ['Gestione personas usuarias', 'Altas, bajas y asignación de roles.', '/admin/usuarios'],
      ['Revise roles y permisos', 'Qué puede ver y hacer cada actor.', '/admin/roles'],
      ['Apruebe parámetros', 'Cambios de configuración pendientes de aprobación.', '/admin/parametros'],
      ['Consulte la auditoría', 'Busque y exporte quién hizo qué y cuándo.', '/admin/auditoria']
    ],
    cliente: [
      ['Haga un pedido', 'Elija productos; verá su crédito disponible antes de confirmar.', '/portal/pedido'],
      ['Siga su entrega', 'Ventana de 30 minutos y estado en vivo.', '/portal/entregas'],
      ['Descargue documentos', 'Facturas y guías de despacho.', '/portal/cuenta']
    ],
    'cliente-moderno': [
      ['Haga un pedido manual', 'Además del pedido EDI que envía su cadena.', '/portal/pedido'],
      ['Siga las entregas por local', 'Ventana de 30 minutos para cada sucursal.', '/portal/entregas'],
      ['Descargue documentos y acuses', 'Facturas, guías y avisos de despacho.', '/portal/cuenta']
    ],
    transportista: [
      ['Asigne conductor y vehículo', 'Para cada ruta de mañana, antes del plazo de hoy a las 18:00.', '/portal/transportista'],
      ['Atienda sus tareas', 'Aquí figuran las asignaciones pendientes.', '/bandeja']
    ],
    proveedor: [
      ['Revise órdenes y recepciones', 'Consulta de solo lectura de sus órdenes de compra.', '/portal/proveedor'],
      ['Atienda las discrepancias', 'Diferencias de cantidad que Bodega reportó.', '/bandeja']
    ]
  };
})(window.LFX = window.LFX || {});
