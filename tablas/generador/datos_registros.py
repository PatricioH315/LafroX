"""Registros desarrollados del Cap. 17.1; fuente: decisiones.md y reglas_de_negocio.md."""

DECISIONES = [
 ['D-01','Reparto entre etapas','Etapa 1 habilita captura, OTIF y continuidad; Etapa 2 incorpora canal moderno y costo de servir.','La segunda etapa depende de hechos operacionales confiables.'],
 ['D-02','Medición de OTIF','M10 calcula OTIF diariamente; el costo de servir se completa en Etapa 2.','Evita definiciones distintas por área.'],
 ['D-03','Promesa de entrega','Se parametriza por cliente, zona y capacidad; no hay una ventana universal.','El caso distingue canales y cobertura rural.'],
 ['D-04','Aceptación','Los criterios del Cap. 18 se prueban en marcha blanca con evidencia y responsable.','Una pantalla no demuestra un resultado de negocio.'],
 ['D-05','Reposición','Usa historia de ventas y excepciones revisables.','Sustituye la planilla sin convertir una estimación en decisión irreversible.'],
 ['D-06','Implantación','Despliegue por proceso y zona, con capacitación, conciliación y marcha blanca.','El despacho no admite un corte general.'],
 ['D-07','Reversión','Responsable operativo autoriza reversión; registros quedan en cola para conciliación.','Preserva evidencia y evita pérdida o duplicación.'],
 ['D-08','Modo desconectado','Terreno opera 14 h y CD 24 h con captura local, UUID y sincronización idempotente.','Obligación del caso y RT-03.10/03.12.'],
 ['D-09','Analítica avanzada','Ruteo determinístico y explicable; no se incorpora IA como sustituto de reglas.','El planificador debe revisar y corregir la ruta.'],
 ['D-10','Mesa de servicio','Atención 04:00--22:00 L--S y 24x7 en septiembre y diciembre.','Horario particular exigido por el caso.'],
]

REGLAS = [
 ['RNG-01','Reserva de stock','Reserva al confirmar; offline muestra antigüedad.','Sistema y bodega.','Evita doble compromiso; RF-02.05, RF-03.03.'],
 ['RNG-02','Stock disponible','Disponible = físico menos comprometido; tránsito no se vende antes de recepción.','Sistema y bodega.','Evita sobreventa; RF-02.05, RF-02.06.'],
 ['RNG-03','Crédito en preventa','Consulta límite y deuda; excepción registrada.','Supervisor de crédito.','Bloqueo o excepción trazable; RF-03.04--03.10.'],
 ['RNG-04','Excursión térmica','Sensor registra, sistema alerta y retiene el lote.','Calidad.','Liberación o disposición trazable; RF-09.03--09.10.'],
 ['RNG-05','Local cerrado','Conductor registra; sistema propone próxima ventana.','Planificador.','Reentrega trazable; RF-06.04, RF-04.07.'],
 ['RNG-06','Devolución','Captura SKU, cantidad y motivo aun sin señal.','Bodega y Finanzas.','Proceso tributario en ERP; RF-06.03, RF-08.01--02.'],
 ['RNG-07','Envases retornables','Entrega descuenta y devolución suma saldo por cliente.','Conductor y preventista.','Controla pérdida; RF-06.09, RF-08.03--06.'],
 ['RNG-08','Precio','Precio de despacho; excepción configurada por cliente o cadena.','Administrador comercial.','Alerta al cliente; RF-03.11--03.13.'],
 ['RNG-09','OTIF','In-Full exige unidades completas y On-Time ventana pactada.','Gerencia comercial.','Parcial queda con causal; RF-11.03--04.'],
 ['RNG-10','FEFO','Picking prioriza vencimiento y deja excepción.','Sistema y preparador.','Reduce merma; RF-02.08, RF-05.05.'],
 ['RNG-11','Maestro de productos','Maestro interno conserva equivalencias GS1 y externas.','Administrador de catálogo.','Excepción para código no resuelto; RF-01.10, RF-12.03.'],
 ['RNG-12','Sincronización','Cola local con UUID, deduplicación y bitácora.','Servicio de sincronización.','Sin pedidos perdidos o duplicados; RF-03.15--16.'],
 ['RNG-13','Secuencia térmica','Picking sigue seco, refrigerado y congelado.','Sistema y preparador.','Evita ruptura de frío; RF-05.04, RF-01.11.'],
 ['RNG-14','Capacidad y carga','Ruta no excede peso, volumen ni condición térmica.','Planificador y cargador.','Evita rechazo; RF-04.03--05, RF-05.07.'],
 ['RNG-15','Corte y promesa','Corte y ventana se parametrizan por cliente y zona.','Comercial y operaciones.','No promete plazo universal; RF-03.13, RF-04.07.'],
 ['RNG-16','Descuentos','Excepción comercial se registra antes de confirmar.','Supervisor comercial.','Evita descuento sin trazabilidad; RF-03.07, RF-03.10.'],
]

def grupos(filas):
    roles={'Gerenta General':'Jefe de Proyecto','Gerente Comercial':'Líder de Implantación','Gerente de Operaciones':'Jefe de Proyecto','Gerente de Finanzas':'Líder de Datos','Jefa de Calidad':'Encargado de Seguridad','Jefa de Bodega':'Líder de Implantación','Jefe de TI':'Arquitecto de Solución','Planificador de Rutas':'Líder de Implantación','Preventistas':'Líder de Implantación','Tripulación propia':'Líder de Implantación','Conductores externos':'Líder de Implantación','Empresas transportistas':'Jefe de Proyecto','Preparadores':'Líder de Implantación','Sindicato de Choferes':'Jefe de Proyecto','Canal Tradicional':'Gerente Comercial','Food Service':'Gerente Comercial','Canal Moderno':'Gerente Comercial','Proveedores':'Jefa de Bodega','Autoridad Sanitaria':'Jefa de Calidad'}
    return [[a,b,'Inicio, piloto y seguimiento',roles.get(a,'Jefe de Proyecto'),'Participación y adopción registradas'] for a,b in filas]
