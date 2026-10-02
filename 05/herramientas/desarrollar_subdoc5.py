"""Materializa fuentes de propuesta y anexos. No conecta sistemas del CLIENTE.

La edición posterior se realiza en los .tex y los JSON generados; este constructor
conserva la primera elaboración para reproducir y auditar su origen.
"""
from pathlib import Path
import csv, hashlib, json, re

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / '05'

def write(path, content):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content.strip() + '\n', encoding='utf-8')

def tex(s):
    return ''.join({'&':r'\&','%':r'\%','_':r'\_\allowbreak ','/':r'/\allowbreak ','#':r'\#','$':r'\$','{':r'\{','}':r'\}'}.get(c,c) for c in str(s))

def table(title, label, headers, rows, widths=None):
    widths = widths or [0.22] * (len(headers)-1)
    cols = ' '.join('F{'+str(x)+'}' for x in widths) + ' Y'
    return '\n'+r'\begin{tablalafrox}{'+tex(title)+'}{'+label+'}{'+cols+'}{'+ ' & '.join(r'\cab{'+tex(h)+'}' for h in headers)+'}\n'+ '\n'.join(' & '.join(tex(c) for c in row)+r' \\' for row in rows)+'\n'+r'\end{tablalafrox}'+'\n'

def fig(name, caption, explanation):
    return 'La Figura~\\ref{fig:5-'+name+'} '+explanation+'\n\n'+r'\begin{figure}[htbp]'+'\n'+r'\centering'+'\n'+r'\input{05/figuras/fuentes/datos/'+name+'.tex}'+'\n'+r'\caption{'+caption+'}'+'\n'+r'\label{fig:5-'+name+'}'+'\n'+r'{\fontsize{9pt}{11pt}\selectfont Fuente: elaboración de LafroX a partir del Caso 02 y la arquitectura de referencia.}'+'\n'+r'\end{figure}\FloatBarrier'+'\n'

# Datos documentales: cada atributo tiene tipo, dominio, obligatoriedad y sensibilidad.
entities=[]
def entity(name, domain, module, owner, attrs, rule, common=True):
    fields=[]
    if common:
        fields=[['id','uuid','UUID estable, PK','Sí','Interno'],['creado_en','timestamptz','UTC; instante de persistencia','Sí','Interno'],['version','bigint','Entero mayor o igual a 1','Sí','Interno']]
    for row in attrs.split('\n'):
        if row.strip():
            parts=row.strip().split('|')
            if len(parts)!=5: raise ValueError((name,row))
            fields.append(parts)
    entities.append(dict(nombre=name,dominio=domain,modulo=module,propietario=owner,atributos=[dict(nombre=f[0],tipo=f[1],valores=f[2],obligatorio=f[3],sensibilidad=f[4],propietario=owner) for f in fields],regla=rule))

entity('cliente','BD_MAESTROS_CONF','M3/M7','Comercial', '''rut|varchar(12)|RUT normalizado y DV válido; único|Sí|Personal
codigo_erp|varchar(40)|Identificador único en ERP|Sí|Interno
razon_social|varchar(160)|Texto no vacío|Sí|Personal
canal|varchar(20)|tradicional, food_service, cadena|Sí|Interno
estado|varchar(16)|activo, bloqueado, inactivo|Sí|Interno
preferencia_canal|varchar(16)|app, sms, mensajeria, correo, sin_digital|Sí|Personal''','ERP publica el maestro autorizado mediante ACL; M3 mantiene preferencia de canal bajo su propio contrato. Un RUT puede tener varios puntos de entrega.')
entity('punto_entrega','BD_MAESTROS_CONF','M3/M4','Comercial', '''cliente_id|uuid|Referencia a cliente|Sí|Interno
codigo|varchar(40)|Único por cliente|Sí|Interno
direccion|varchar(240)|Dirección de entrega|Sí|Personal
posicion|geography(Point,4326)|Latitud y longitud válidas; geocodificación revisada|No|Personal
ventana_desde|time|Hora local America/Santiago|Sí|Interno
ventana_hasta|time|Fin posterior al inicio; excepción nocturna parametrizada|Sí|Interno
zona|varchar(40)|Catálogo de zonas logísticas|Sí|Interno''','FK lógica a cliente; UNIQUE(cliente_id,codigo). La ventana se copia en cada entrega prometida para preservar el compromiso histórico.')
entity('producto','BD_MAESTROS_CONF','M1/M2','Abastecimiento', '''codigo_erp|varchar(40)|SKU autorizado único|Sí|Interno
gtin|varchar(14)|GTIN normalizado; dígito verificador|Sí|Interno
descripcion|varchar(160)|Nombre comercial|Sí|Interno
unidad|varchar(16)|Catálogo GS1/unidades autorizadas|Sí|Interno
clase_temperatura|varchar(16)|seco, refrigerado, congelado|Sí|Interno
temperatura_min|numeric(5,2)|Grados Celsius; según ficha aprobada|No|Interno
temperatura_max|numeric(5,2)|Mayor o igual al mínimo|No|Interno
vida_util_dias|integer|Entero positivo|Sí|Interno''','GTIN se versiona por presentación. M9 autoriza rangos térmicos; el maestro ERP conserva la identidad comercial y sus equivalencias.')
entity('proveedor','BD_MAESTROS_CONF','M1','Abastecimiento', '''rut|varchar(12)|RUT y DV válido; único|Sí|Personal
codigo_erp|varchar(40)|Código externo único|Sí|Interno
razon_social|varchar(160)|Texto no vacío|Sí|Personal
plazo_dias|integer|Entero no negativo|Sí|Interno''','Maestro completo migrado del ERP; modificar plazo exige versión y autor.')
entity('sitio','BD_MAESTROS_CONF','M1/M2/M5','Operaciones', '''codigo|varchar(24)|Talca, Concepción, Curicó, Chillán, Los Ángeles; ampliable|Sí|Interno
tipo|varchar(16)|cd, crossdock, oficina|Sí|Interno
zona_horaria|varchar(40)|America/Santiago|Sí|Interno''','Código estable y único; solo los cinco sitios logísticos escriben WMS. Casa matriz opera por nube.')
entity('recepcion','BD_INVENTARIO','M1','Jefatura de bodega', '''sitio_id|uuid|Referencia a sitio logístico|Sí|Interno
proveedor_id|uuid|Referencia al maestro proveedor|Sí|Interno
documento_origen|varchar(80)|Documento ERP/proveedor; clave externa|Sí|Interno
estado|varchar(16)|capturada, validada, observada, cerrada|Sí|Interno
ocurrido_en|timestamptz|Instante físico de recepción|Sí|Interno''','La recepción cerrada tiene al menos una línea; el cierre genera movimientos y outbox en una misma transacción local.')
entity('lote','BD_CALIDAD_TRAZABILIDAD','M1/M9','Calidad', '''producto_id|uuid|Referencia al producto/GTIN|Sí|Interno
proveedor_id|uuid|Proveedor de origen|Sí|Interno
lote_proveedor|varchar(80)|Código de lote no vacío|Sí|Interno
vence_en|date|Fecha de vencimiento|Sí|Interno
estado|varchar(20)|liberado, bloqueado, retiro, descartado|Sí|Interno''','UNIQUE(producto_id,proveedor_id,lote_proveedor). Si un GTIN/lote aparece con varios proveedores se conserva el origen y se agrupa el retiro por GTIN/lote. Un vencimiento discordante se aísla para Calidad.')
entity('unidad_logistica','BD_INVENTARIO','M1/M2','Jefatura de bodega', '''sscc|varchar(18)|SSCC y dígito verificador; único|Sí|Interno
sitio_id|uuid|Sitio custodio actual|Sí|Interno
ubicacion|varchar(40)|Posición autorizada del sitio|Sí|Interno
estado|varchar(16)|recibida, almacenada, preparada, despachada|Sí|Interno''','La unidad puede contener varios lotes mediante contenido_unidad. El movimiento conserva SSCC y custodia; no se usa SSCC para identificar cada envase retornable.')
entity('contenido_unidad','BD_INVENTARIO','M1/M2','Jefatura de bodega', '''unidad_id|uuid|Referencia a unidad logística|Sí|Interno
lote_id|uuid|Referencia a lote|Sí|Interno
cantidad|numeric(14,3)|Cantidad mayor que cero en unidad base|Sí|Interno''','UNIQUE(unidad_id,lote_id); suma de cantidades se concilia con recepción y movimientos.')
entity('linea_recepcion','BD_INVENTARIO','M1','Jefatura de bodega', '''recepcion_id|uuid|FK a recepción|Sí|Interno
lote_id|uuid|Referencia a lote|Sí|Interno
unidad_id|uuid|Referencia a SSCC|Sí|Interno
cantidad|numeric(14,3)|Mayor que cero|Sí|Interno
temperatura|numeric(5,2)|Lectura de control en Celsius|No|Interno''','Cada línea identifica lote y SSCC; una observación térmica bloquea liberación hasta decisión de Calidad.')
entity('movimiento_stock','BD_INVENTARIO','M2','Jefatura de bodega', '''sitio_id|uuid|Autoridad de escritura del sitio|Sí|Interno
lote_id|uuid|Referencia a lote|Sí|Interno
unidad_id|uuid|Unidad logística afectada|Sí|Interno
tipo|varchar(24)|recepcion, traslado, preparacion, despacho, devolucion, ajuste|Sí|Interno
cantidad_delta|numeric(14,3)|Entrada positiva o salida negativa, distinta de cero|Sí|Interno
ubicacion|varchar(40)|Ubicación en sitio|Sí|Interno
secuencia_sitio|bigint|Monótona por sitio y época|Sí|Interno
evento_origen_id|uuid|Identidad de operación; única|Sí|Interno
ocurrido_en|timestamptz|Hora del hecho físico|Sí|Interno''','Libro inmutable; correcciones mediante movimiento compensatorio aprobado. Stock se obtiene de suma de deltas, no de la última cifra recibida.')
entity('reserva','BD_INVENTARIO','M2','Jefatura de bodega', '''linea_pedido_id|uuid|Referencia a línea del pedido|Sí|Interno
sitio_id|uuid|Sitio que confirma|Sí|Interno
lote_id|uuid|Lote asignado por FEFO|Sí|Interno
cantidad|numeric(14,3)|Mayor que cero|Sí|Interno
estado|varchar(16)|pendiente, confirmada, consumida, liberada, rechazada|Sí|Interno
expira_en|timestamptz|Plazo parametrizado por operación|No|Interno''','M2 es autoridad por agregado sitio/lote. Para confirmar bloquea saldo y comprueba disponible; la nube coordina sin confirmar contra una réplica atrasada.')
entity('pedido','BD_PREVENTA','M3','Comercial', '''cliente_id|uuid|Maestro cliente|Sí|Interno
punto_id|uuid|Punto de entrega del mismo cliente|Sí|Interno
actor_id|uuid|Preventista o cuenta de autoservicio|Sí|Personal
estado|varchar(20)|capturado, pendiente, confirmado, preparado, despachado, parcial, entregado, rendido, cancelado|Sí|Interno
capturado_en|timestamptz|Hora en terminal, conservada|Sí|Interno
transaction_id|uuid|Correlación transversal estable|Sí|Interno
tarifa_version|varchar(40)|Versión de tarifa mostrada|Sí|Interno''','Capturado offline no equivale a reserva confirmada. Pedido tiene una o más líneas; reenvío con mismo UUID devuelve resultado anterior.')
entity('linea_pedido','BD_PREVENTA','M3','Comercial', '''pedido_id|uuid|FK a pedido|Sí|Interno
numero|integer|Entero positivo único por pedido|Sí|Interno
producto_id|uuid|Referencia al SKU autorizado|Sí|Interno
cantidad|numeric(14,3)|Mayor que cero|Sí|Interno
precio_informado|numeric(18,2)|Moneda CLP; mayor o igual a cero|Sí|Comercial restringido
unidad|varchar(16)|Unidad de captura y conversión versionada|Sí|Interno''','UNIQUE(pedido_id,numero). Un cambio de tarifa genera revalidación explícita; el importe es dato operativo del CLIENTE, no precio de oferta.')
entity('asignacion_lote','BD_PREPARACION','M5','Jefatura de bodega', '''linea_pedido_id|uuid|Línea servida|Sí|Interno
lote_id|uuid|Lote proveedor|Sí|Interno
unidad_id|uuid|SSCC de procedencia|Sí|Interno
reserva_id|uuid|Reserva aceptada en M2|Sí|Interno
cantidad|numeric(14,3)|Mayor que cero; no superar reserva neta|Sí|Interno''','Una línea puede servirse con varios lotes. Las cantidades asignadas y entregadas permiten traza hacia adelante y hacia atrás.')
entity('mision','BD_PREPARACION','M5','Jefatura de bodega', '''sitio_id|uuid|Sitio ejecutor|Sí|Interno
oleada|varchar(40)|Grupo de preparación|Sí|Interno
actor_id|uuid|Preparador autorizado en turno|Sí|Personal
dispositivo_id|uuid|Terminal HHT|Sí|Interno
estado|varchar(16)|descargada, ejecutada, cerrada|Sí|Interno''','No se reasigna una misión descargada sin revocar o cerrar su versión previa.')
entity('linea_mision','BD_PREPARACION','M5','Jefatura de bodega', '''mision_id|uuid|FK a misión|Sí|Interno
asignacion_id|uuid|Referencia a asignación de lote|Sí|Interno
cantidad_confirmada|numeric(14,3)|Entre cero y cantidad asignada|Sí|Interno
confirmada_en|timestamptz|Hora del escaneo|No|Interno''','Confirmar línea y consumir reserva es operación idempotente; faltante requiere causal y ajuste autorizado.')
entity('despacho','BD_PREPARACION','M5','Operaciones', '''sitio_id|uuid|Sitio de salida|Sí|Interno
viaje_id|uuid|Viaje aprobado|Sí|Interno
carga_version|bigint|Versión positiva de carga|Sí|Interno
estado|varchar(24)|carga_confirmada, guia_solicitada, resultado_incierto, guia_disponible, salida_liberada|Sí|Interno
guia_id|uuid|DTE confirmado por ERP|No|Interno
liberado_en|timestamptz|Instante de salida autorizada|No|Interno''','Solo salida_liberada exige guía vigente de la misma carga y copia disponible localmente. Ningún booleano fusiona guía, SII y acuse de mercadería.')
entity('viaje','BD_RUTAS','M4/M12','Planificación', '''sitio_id|uuid|Sitio de origen|Sí|Interno
vehiculo_id|uuid|Vehículo propio o tercero|Sí|Interno
conductor_id|uuid|Vínculo autorizado vigente|Sí|Personal
fecha_operacion|date|Fecha local de jornada|Sí|Interno
estado|varchar(16)|planificado, aprobado, iniciado, cerrado|Sí|Interno
distancia_km|numeric(12,3)|Distancia no negativa|No|Interno''','Planificador aprueba versión de ruta. El conductor de cada hecho no se reemplaza retrospectivamente cuando cambia la asignación.')
entity('parada','BD_RUTAS','M4','Planificación', '''viaje_id|uuid|FK a viaje|Sí|Interno
punto_id|uuid|Punto autorizado de entrega|Sí|Interno
secuencia|integer|Entero positivo único por viaje|Sí|Interno
ventana_inicio|timestamptz|Compromiso para esta visita|Sí|Interno
ventana_fin|timestamptz|Posterior al inicio|Sí|Interno
restriccion|varchar(160)|Regla de acceso o excepción documentada|No|Interno''','UNIQUE(viaje_id,secuencia). Se conserva la ventana original aun si la ruta real cambia.')
entity('vehiculo','BD_RUTAS','M12','Flota', '''patente|varchar(12)|Identificador normalizado único|Sí|Interno
transportista_id|uuid|Empresa propietaria, si es tercero|No|Interno
capacidad_kg|numeric(12,3)|Mayor que cero|Sí|Interno
capacidad_m3|numeric(10,3)|Mayor que cero|Sí|Interno
frio|boolean|Capacidad de transporte refrigerado|Sí|Interno''','Maestro de capacidades gobernado por Flota; no se deduce capacidad del GPS.')
entity('entrega','BD_REPARTO','M6','Operaciones', '''pedido_id|uuid|Referencia al pedido|Sí|Interno
parada_id|uuid|Visita que origina el intento|Sí|Interno
despacho_id|uuid|Salida con guía válida|Sí|Interno
intento|integer|Número positivo por pedido/parada|Sí|Interno
estado|varchar(20)|completa, parcial, no_entregada, en_conflicto|Sí|Interno
receptor_cifrado|bytea|Identidad mínima cifrada; nombre o causal de ausencia|No|Personal restringido
ocurrido_en|timestamptz|Momento efectivo de recepción|Sí|Interno
actor_id|uuid|Conductor autor del registro|Sí|Personal''','Pedido tiene cero o muchas entregas/intentos. Entrega completa exige cubrir todas las cantidades pendientes; intento fallido conserva causal sin fabricar receptor.')
entity('detalle_entrega','BD_REPARTO','M6','Operaciones', '''entrega_id|uuid|FK a entrega|Sí|Interno
asignacion_id|uuid|Lote y SSCC entregado|Sí|Interno
aceptada|numeric(14,3)|Cantidad no negativa|Sí|Interno
rechazada|numeric(14,3)|Cantidad no negativa|Sí|Interno
causal|varchar(40)|daño, vencimiento, no_solicitado, faltante, otra|No|Interno''','Aceptada más rechazada no supera asignación pendiente. Rechazo mayor que cero exige causal y retorno vinculado.')
entity('evidencia_pod','BD_REPARTO','M6','Operaciones', '''entrega_id|uuid|Entrega documentada|Sí|Interno
objeto_id|uuid|Manifiesto de objeto S3|Sí|Interno
tipo|varchar(16)|firma, foto, qr, constancia|Sí|Personal restringido
hash_sha256|char(64)|Huella del objeto original|Sí|Interno
capturada_en|timestamptz|Hora en dispositivo|Sí|Interno
causal_sin_firma|varchar(80)|Negativa, imposibilidad o receptor ausente|No|Personal''','Una entrega conserva cero o varias evidencias según causal y política; no se cambia el original ni se presume validez tributaria de una foto.')
entity('documento_tributario','BD_COBRANZA_FINANZAS','M5/M7','Tributación', '''emisor_rut|varchar(12)|RUT del emisor ERP|Sí|Personal
tipo|varchar(24)|guia, factura, boleta, nota_credito, otro|Sí|Interno
folio|bigint|Folio positivo; único por emisor y tipo|Sí|Interno
despacho_id|uuid|Salida asociada para guía|No|Interno
objeto_id|uuid|XML/documento original|Sí|Interno
estado_erp|varchar(24)|solicitado, incierto, emitido, rechazado, anulado|Sí|Interno
clave_solicitud|uuid|Clave idempotente estable por carga|Sí|Interno''','ERP único emisor. UNIQUE(emisor_rut,tipo,folio); consulta por clave tras timeout antes de reemitir.')
entity('acuse','BD_COBRANZA_FINANZAS','M7','Tributación', '''documento_id|uuid|Documento relacionado|Sí|Interno
tipo|varchar(24)|tecnico_sii, mercaderia_destinatario, mdn_edi|Sí|Interno
origen|varchar(80)|ERP, SII o destinatario/cadena|Sí|Interno
estado|varchar(20)|recibido, aceptado, rechazado, observado|Sí|Interno
objeto_id|uuid|Comprobante original|Sí|Interno
ocurrido_en|timestamptz|Hora de recepción|Sí|Interno''','Los acuses se registran por tipo; un MDN AS2 no equivale a aceptación comercial ni tributaria.')
entity('cobro','BD_COBRANZA_FINANZAS','M7','Tesorería', '''entrega_id|uuid|Entrega que origina pago|Sí|Interno
conductor_id|uuid|Custodio en turno|Sí|Personal
medio|varchar(16)|efectivo, tarjeta, transferencia, credito|Sí|Interno
monto_cifrado|bytea|Importe CLP no negativo cifrado|Sí|Financiero restringido
referencia_pasarela|varchar(100)|Referencia tokenizada; sin PAN ni CVV|No|Financiero restringido
estado|varchar(16)|capturado, confirmado, incierto, rechazado|Sí|Interno
ocurrido_en|timestamptz|Hora del pago|Sí|Interno''','No se confirma tarjeta por timeout. El efectivo capturado se concilia con rendición; no se suma dos veces por reintento.')
entity('rendicion','BD_COBRANZA_FINANZAS','M7','Tesorería', '''conductor_id|uuid|Autor/custodio|Sí|Personal
viaje_id|uuid|Viaje rendido|Sí|Interno
esperado_cifrado|bytea|Suma de cobros de efectivo confirmados|Sí|Financiero restringido
recibido_cifrado|bytea|Monto contado por Tesorería|Sí|Financiero restringido
causal_diferencia|varchar(160)|Explicación obligatoria si hay diferencia|No|Financiero restringido
estado|varchar(16)|abierta, conciliada, observada, cerrada|Sí|Interno''','Tesorería valida esperado, recibido y diferencia. Corrección por ajuste con autor y motivo; la captura del conductor no es cierre contable ERP.')
entity('saldo_credito','BD_COBRANZA_FINANZAS','M7','Tesorería', '''cliente_id|uuid|Maestro cliente único|Sí|Interno
saldo_cifrado|bytea|Saldo vivo CLP cifrado|Sí|Financiero restringido
limite_cifrado|bytea|Límite autorizado cifrado|Sí|Financiero restringido
bloqueado|boolean|Restricción comunicada por ERP|Sí|Interno
vigente_en|timestamptz|Fecha de fuente ERP|Sí|Interno''','Proyección del ERP; no se sustituye con un saldo offline. M3 presenta antigüedad y no habilita crédito adicional durante incertidumbre.')
entity('devolucion','BD_INVENTARIO','M8','Operaciones', '''entrega_id|uuid|Entrega o intento original|Sí|Interno
lote_id|uuid|Lote de retorno|Sí|Interno
cantidad|numeric(14,3)|Mayor que cero|Sí|Interno
causal|varchar(40)|daño, vencimiento, no_solicitado, otra|Sí|Interno
estado|varchar(20)|capturada, recibida, cuarentena, liberada, descartada|Sí|Interno
documento_posterior_id|uuid|Documento emitido por ERP si corresponde|No|Interno''','Recepción física local no acredita aptitud ni abono. Calidad decide reingreso; ERP emite documento posterior enlazado al original.')
entity('movimiento_envase','BD_INVENTARIO','M8','Operaciones', '''cliente_id|uuid|Cuenta corriente del cliente|Sí|Interno
tipo_envase|varchar(16)|canastillo, pallet|Sí|Interno
cantidad_delta|integer|Cargo positivo, retorno negativo; distinto de cero|Sí|Interno
entrega_id|uuid|Entrega de origen si aplica|No|Interno
sitio_id|uuid|Sitio de recepción física|Sí|Interno
estado|varchar(16)|capturado, aceptado, disputado, compensado|Sí|Interno
evidencia_id|uuid|Constancia vinculada|No|Personal restringido''','Saldo por cliente/tipo = suma de movimientos aceptados. No se crea una identidad por cada canastillo; disputa no elimina evidencia del hecho.')
entity('sensor','BD_TELEMETRIA','M9','Calidad', '''codigo|varchar(40)|Identificador único del sensor físico|Sí|Interno
sitio_id|uuid|Sitio; nulo para vehículo|No|Interno
vehiculo_id|uuid|Vehículo; nulo para cámara|No|Interno
calibrado_en|date|Fecha de última calibración|Sí|Interno
intervalo_seg|integer|Muestreo positivo según perfil técnico|Sí|Interno''','Exactamente una ubicación sitio/vehículo; gateway redundante no crea un segundo sensor físico.')
entity('lectura_termica','BD_TELEMETRIA','M9','Calidad', '''sensor_id|uuid|Sensor de origen|Sí|Interno
secuencia_origen|bigint|Secuencia del dispositivo y sesión|Sí|Interno
sesion_origen|varchar(40)|Identifica reinicio del termógrafo|Sí|Interno
ocurrido_en|timestamptz|Hora de muestreo UTC|Sí|Interno
valor_c|numeric(5,2)|Temperatura Celsius|Sí|Interno
calidad|varchar(16)|valida, sospechosa, sin_calibracion|Sí|Interno
gateway_id|varchar(40)|Gateway que transportó, no clave de lectura|Sí|Interno''','Clave de deduplicación sensor/sesión/secuencia; conservar discrepancias de valor como incidente. Raw en DynamoDB, serie validada en Parquet y Redshift.')
entity('bloqueo_calidad','BD_CALIDAD_TRAZABILIDAD','M9','Calidad', '''lote_id|uuid|Lote afectado|Sí|Interno
sensor_id|uuid|Sensor causante si térmico|No|Interno
motivo|varchar(80)|Excursión, retiro sanitario u observación|Sí|Interno
estado|varchar(16)|activo, liberado, descartado|Sí|Interno
decisor_id|uuid|Responsable de Calidad para liberar|No|Personal
ocurrido_en|timestamptz|Hora de bloqueo|Sí|Interno''','Bloqueo local aplica a M5 en menos de 5 s según arquitectura; liberación exige decisión motivada de Calidad, no tiempo de espera.')
entity('posicion_flota','BD_TELEMETRIA','M12','Flota', '''vehiculo_id|uuid|Vehículo telemático|Sí|Interno
viaje_id|uuid|Viaje asociado si existe|No|Interno
referencia_tercero|varchar(100)|Clave de lectura externa única|Sí|Interno
posicion_cifrada|bytea|Coordenadas cifradas a nivel de campo|Sí|Personal restringido
ocurrido_en|timestamptz|Hora del GPS|Sí|Interno''','Se ingiere por INT-15 desde telemetría existente. Plazo máximo de dato personal 12 meses; métricas agregadas irreversibles se separan del identificador de persona.')
entity('transportista','BD_GOBIERNO_ACCESO','M6/M12','Flota', '''rut|varchar(12)|RUT válido único|Sí|Personal
razon_social|varchar(160)|Empresa autorizada|Sí|Personal
estado|varchar(16)|activo, suspendido, finalizado|Sí|Interno''','Transportista declara conductores; autorización y revocación conservan versión y rastro.')
entity('vinculo_conductor','BD_GOBIERNO_ACCESO','M6','Flota', '''actor_id|uuid|Identidad Keycloak estable|Sí|Personal
transportista_id|uuid|Empresa; nulo si propio|No|Interno
desde|timestamptz|Inicio del vínculo|Sí|Interno
hasta|timestamptz|Fin del vínculo, posterior al inicio|No|Interno
estado|varchar(16)|activo, revocado, expirado|Sí|Interno''','Autor de POD refiere actor y vínculo histórico. Reemplazar conductor requiere un vínculo nuevo, sin sobrescribir el anterior.')
entity('autorizacion_turno','BD_GOBIERNO_ACCESO','M1/M5/M6','Seguridad', '''actor_id|uuid|Identidad del autor|Sí|Personal
dispositivo_id|uuid|Equipo autorizado|Sí|Interno
sitio_id|uuid|Sitio o ámbito del turno|Sí|Interno
valida_hasta|timestamptz|8 h bodega o 14 h terreno según arquitectura|Sí|Interno
manifiesto_hash|char(64)|Manifiesto firmado de autorización|Sí|Interno
estado|varchar(16)|vigente, revocada, expirada|Sí|Interno''','El caché de identidad de 24 h no extiende la credencial del turno. No se almacenan PIN ni tokens en texto claro.')
entity('mensaje_edi','BD_EDI_CANALMODERNO','M11','Comercial', '''cadena_id|varchar(40)|Socio y perfil versionado|Sí|Interno
referencia_externa|varchar(100)|Documento único por cadena/tipo|Sí|Interno
tipo|varchar(24)|pedido, respuesta, aviso_despacho, factura|Sí|Interno
formato|varchar(16)|EANCOM, GS1_XML, EPCIS|Sí|Interno
objeto_id|uuid|Original AS2 y transformación|Sí|Interno
pedido_id|uuid|Pedido canónico resultante|No|Interno
estado|varchar(20)|recibido, validado, traducido, observado, respondido|Sí|Interno''','MDN se separa de respuesta comercial; M11 solicita a M3 el pedido y no escribe reserva M2.')
entity('notificacion','BD_MAILS_NOTIF','M3/M6','Comercial', '''cliente_id|uuid|Destinatario autorizado|Sí|Interno
canal|varchar(16)|sms, mensajeria, correo, app|Sí|Personal
plantilla|varchar(40)|Plantilla versionada sin datos de pago en claro|Sí|Interno
evento_id|uuid|Hecho que genera aviso|Sí|Interno
estado|varchar(16)|pendiente, enviada, entregada, fallida|Sí|Interno
referencia_proveedor|varchar(100)|Acuse técnico del proveedor|No|Interno''','UNIQUE(evento_id,cliente_id,canal,plantilla); enviada no implica leída. Cliente sin canal digital conserva atención por preventista/conductor.')
entity('objeto_documental','S3_DOCS','M6/M7/M9','Operaciones y Tributación', '''clave_objeto|varchar(240)|Ruta opaca; sin RUT ni nombre en URL|Sí|Interno
version_objeto|varchar(160)|Versión inmutable identificable|Sí|Interno
mime|varchar(80)|Tipo autorizado|Sí|Interno
hash_sha256|char(64)|Huella verificable|Sí|Interno
tamano_bytes|bigint|Mayor que cero|Sí|Interno
retener_hasta|timestamptz|Política por categoría y bloqueo legal|Sí|Interno
cifrado_clave_id|varchar(160)|Referencia a KMS, nunca secreto|Sí|Interno''','Conservar manifiesto y hashes; transacción de metadatos solo publica evidencia verificada. Object Lock se aplica por categoría, no indefinidamente a todo objeto.')
entity('evento_outbox','dominio_productor','M1–M12','Propietario del módulo', '''event_id|uuid|Identificador único|Sí|Interno
transaction_id|uuid|Correlación de extremo a extremo|Sí|Interno
agregado_id|uuid|Entidad cuya versión cambia|Sí|Interno
agregado_version|bigint|Versión positiva|Sí|Interno
sitio_id|uuid|Origen del hecho|Sí|Interno
tipo|varchar(80)|Nombre canónico en pasado|Sí|Interno
schema_version|varchar(16)|SemVer del contrato|Sí|Interno
payload|jsonb|Esquema validado; datos personales minimizados/cifrados|Sí|Según carga
estado|varchar(16)|pendiente, enviado, acusado, excepcion|Sí|Interno''','Persiste junto con cambio y auditoría en una transacción; solo se purga después de acuse durable y plazo de deduplicación.')
entity('resultado_inbox','dominio_consumidor','M1–M12','Propietario del módulo', '''event_id|uuid|Clave idempotente única por consumidor|Sí|Interno
hash_payload|char(64)|Huella de carga canónica|Sí|Interno
regla|varchar(80)|Regla aplicada y versión|Sí|Interno
resultado|jsonb|Estado y referencia de efecto durable|Sí|Interno
actor_id|uuid|Autor original o cuenta de sistema|Sí|Personal
resuelto_en|timestamptz|Instante de persistencia|Sí|Interno
expira_en|timestamptz|30 días como mínimo antes de archivo|Sí|Interno''','Duplicado con misma huella devuelve resultado; distinto payload bajo mismo UUID se aísla. Mensaje de más de 30 días requiere revisión antes de nueva escritura.')
entity('auditoria','dominio_productor','M1–M12','Seguridad y dueño de negocio', '''entidad|varchar(80)|Tipo de registro|Sí|Interno
entidad_id|uuid|Registro afectado|Sí|Interno
actor_id|uuid|Autor y vínculo verificables|Sí|Personal
dispositivo_id|uuid|Equipo o cuenta técnica|Sí|Interno
accion|varchar(40)|crear, modificar, compensar, consultar_sensible, eliminar|Sí|Interno
antes_cifrado|bytea|Valores anteriores protegidos; nulo al crear|No|Según carga
despues_cifrado|bytea|Valores posteriores protegidos; nulo al eliminar|No|Según carga
transaction_id|uuid|Correlación|Sí|Interno
ocurrido_en|timestamptz|Hora del hecho|Sí|Interno''','La bitácora de negocio acompaña al registro durante su retención, aunque los logs técnicos tengan otro plazo. Registrar también lectura sensible.')
entity('carga_migracion','BD_MAESTROS_CONF','Migración','Responsable de migración', '''fuente|varchar(160)|Sistema y exportación versionada|Sí|Interno
hash_origen|char(64)|Huella del extracto protegido|Sí|Interno
reglas_version|varchar(40)|Versión de mapeo|Sí|Interno
filas_origen|bigint|Recuento no negativo|Sí|Interno
filas_aceptadas|bigint|Recuento no negativo|Sí|Interno
filas_cuarentena|bigint|Recuento no negativo|Sí|Interno
estado|varchar(20)|perfilada, ensayada, conciliada, revertida|Sí|Interno''','Aceptadas más cuarentena deben explicar el total de origen; conservar mapeo de IDs y reporte de diferencias.')
entity('hecho_entrega','BD_BI_GERENCIA','M10','Control de gestión', '''entrega_id|uuid|Clave natural del evento operativo|Sí|Interno
pedido_id|uuid|Permite evaluar OTIF por pedido|Sí|Interno
fecha_key|integer|Clave a dim_fecha|Sí|Interno
cliente_key|bigint|Clave sustituta SCD2|Sí|Interno
sitio_key|bigint|Clave a dim_sitio|Sí|Interno
cantidad_aceptada|numeric(14,3)|Suma por evento, no acumulado duplicado|Sí|Interno
completa|boolean|Todas las líneas netas cubiertas|Sí|Interno
a_tiempo|boolean|Recepción dentro de ventana prometida|Sí|Interno
fuente_event_id|uuid|Evento canónico único|Sí|Interno
visible_en|timestamptz|Momento disponible en modelo semántico|Sí|Interno''','Hecho a grano de entrega; OTIF se agrega por pedido sin contar intentos como pedidos adicionales. No almacena identidad de receptor ni ubicación personal en claro.')
entity('dim_cliente','BD_BI_GERENCIA','M10','Control de gestión', '''cliente_key|bigint|Clave sustituta única|Sí|Interno
cliente_id|uuid|Identidad seudonimizada para navegación autorizada|Sí|Personal
canal|varchar(20)|Canal en la versión histórica|Sí|Interno
zona|varchar(40)|Zona logística histórica|Sí|Interno
valida_desde|timestamptz|Inicio de vigencia SCD2|Sí|Interno
valida_hasta|timestamptz|Fin exclusivo, nulo si vigente|No|Interno''','Intervalos sin solapamiento por cliente; hechos enlazan la versión válida al ocurrir el evento.')
entity('cache_lectura','REDIS_SESIONES_CACHE','M3/M4','Plataforma', '''clave|varchar(160)|Entidad, versión, sitio y ámbito; sin PII|Sí|Interno
valor|jsonb|Proyección minimizada de lectura|Sí|Según carga
version_fuente|bigint|Versión del registro publicado|Sí|Interno
expira_en|timestamptz|TTL por categoría|Sí|Interno''','Caché prescindible; no confirma stock, crédito ni pagos. Vaciarla no pierde registros de negocio.',common=False)

# Extensiones que concretan los maestros externos y el esquema de explotación.
entity('equivalencia_maestro','BD_MAESTROS_CONF','ACL','Dueño del maestro', '''fuente|varchar(40)|ERP, WMS o cadena autorizada|Sí|Interno
entidad|varchar(40)|Tipo de entidad del catálogo|Sí|Interno
codigo_externo|varchar(100)|Identificador en la fuente|Sí|Interno
canonico_id|uuid|Entidad canónica referida|Sí|Interno
desde|timestamptz|Inicio de vigencia|Sí|Interno
hasta|timestamptz|Fin exclusivo, nulo si vigente|No|Interno''','UNIQUE(fuente,entidad,codigo_externo) vigente; fusión conserva alias, origen y aprobación.')
entity('dispositivo','BD_GOBIERNO_ACCESO','MDM','Plataforma', '''codigo_mdm|varchar(80)|Inventario MDM único|Sí|Interno
tipo|varchar(20)|preventa, reparto, hht, gateway|Sí|Interno
sitio_id|uuid|Sitio de adscripción|No|Interno
estado|varchar(20)|activo, bloqueado, perdido, retirado|Sí|Interno
ultima_sync|timestamptz|Último acuse|No|Interno''','Equipo compartido no determina autor: autorización de turno identifica la persona.')
dimdefs={
'dim_fecha':('fecha_key|integer|AAAAMMDD único|Sí|Interno\nfecha|date|Día America/Santiago|Sí|Interno\nmes|integer|1 a 12|Sí|Interno\nanio|integer|Año calendario|Sí|Interno\ntemporada|varchar(24)|normal, septiembre, diciembre|Sí|Interno','Clave fecha no sustituye hora UTC del hecho.'),
'dim_sitio':('sitio_key|bigint|Clave sustituta única|Sí|Interno\nsitio_id|uuid|Sitio canónico|Sí|Interno\ncodigo|varchar(24)|Código de sitio|Sí|Interno\ntipo|varchar(16)|cd, crossdock, oficina|Sí|Interno','Mapeo de código estable; historia cuando cambia clasificación.'),
'dim_producto':('producto_key|bigint|Clave sustituta única|Sí|Interno\nproducto_id|uuid|Producto canónico|Sí|Interno\ngtin|varchar(14)|Presentación histórica|Sí|Interno\nfamilia|varchar(40)|Familia autorizada|Sí|Interno\ncondicion_termica|varchar(16)|seco, refrigerado, congelado|Sí|Interno\nvalida_desde|timestamptz|Inicio SCD2|Sí|Interno\nvalida_hasta|timestamptz|Fin exclusivo, nulo vigente|No|Interno','Sin solapamiento de vigencia por producto.'),
'dim_ruta':('ruta_key|bigint|Clave sustituta única|Sí|Interno\nviaje_id|uuid|Viaje canónico|Sí|Interno\nversion_ruta|bigint|Versión aprobada|Sí|Interno\nzona|varchar(40)|Zona logística|Sí|Interno','UNIQUE(viaje_id,version_ruta); no expone GPS personal.'),
'dim_causal':('causal_key|bigint|Clave sustituta única|Sí|Interno\ncodigo|varchar(40)|Código gobernado|Sí|Interno\nfamilia|varchar(20)|faltante, daño, rechazo, demora, calidad, otra|Sí|Interno\ndescripcion|varchar(160)|Definición de uso|Sí|Interno','Conservar versión del significado histórico.')}
for name,(attrs,rule) in dimdefs.items(): entity(name,'BD_BI_GERENCIA','M10','Control de gestión',attrs,rule)
factdefs={
'hecho_pedido':('linea_id|uuid|Línea canónica|Sí|Interno\nversion_linea|bigint|Versión de compromiso|Sí|Interno\nfecha_key|integer|dim_fecha|Sí|Interno\ncliente_key|bigint|dim_cliente SCD2|Sí|Interno\nproducto_key|bigint|dim_producto SCD2|Sí|Interno\ncantidad_comprometida|numeric(14,3)|Mayor que cero en unidad base|Sí|Interno','Línea/version; seleccionar versión vigente, no sumar revisiones.'),
'hecho_movimiento':('movimiento_id|uuid|Movimiento canónico único|Sí|Interno\nfecha_key|integer|dim_fecha|Sí|Interno\nsitio_key|bigint|dim_sitio|Sí|Interno\nproducto_key|bigint|dim_producto|Sí|Interno\nlote_id|uuid|Referencia sanitaria|Sí|Interno\ncantidad_delta|numeric(14,3)|Delta firmado|Sí|Interno','No mezclar delta y snapshot de saldo en una misma suma.'),
'hecho_temperatura':('lectura_id|uuid|Lectura deduplicada única|Sí|Interno\nsensor_id|uuid|Sensor físico|Sí|Interno\nfecha_key|integer|dim_fecha|Sí|Interno\nsitio_key|bigint|dim_sitio para cámara|No|Interno\nvalor_c|numeric(5,2)|Valor Celsius validado|Sí|Interno\nfuera_rango|boolean|Regla aprobada de Calidad|Sí|Interno\nregla_version|varchar(40)|Versión de rango|Sí|Interno','Hueco de muestra no acredita duración continua.'),
'hecho_rendicion':('rendicion_id|uuid|Rendición de origen|Sí|Interno\nfecha_key|integer|dim_fecha|Sí|Interno\nruta_key|bigint|dim_ruta|Sí|Interno\nesperado_cifrado|bytea|Importe CLP protegido|Sí|Financiero restringido\nrecibido_cifrado|bytea|Importe CLP protegido|Sí|Financiero restringido\ncausal_key|bigint|dim_causal si diferencia|No|Interno','Detalle solo Tesorería; agregados no identifican personas.')}
for name,(attrs,rule) in factdefs.items(): entity(name,'BD_BI_GERENCIA','M10','Control de gestión',attrs,rule)
for e in entities:
    if e['nombre'].startswith('hecho_'):
        existing={a['nombre'] for a in e['atributos']}
        for n,t,v in [('fuente_event_id','uuid','Evento canónico único'),('dataset_origen','varchar(120)','Dataset gobernado'),('lote_etl','uuid','Ejecución con manifiesto'),('transformation_version','varchar(40)','Regla aplicada'),('ocurrido_en','timestamptz','Momento de origen UTC'),('visible_en','timestamptz','Momento disponible en modelo semántico')]:
            if n not in existing: e['atributos'].append(dict(nombre=n,tipo=t,valores=v,obligatorio='Sí',sensibilidad='Interno',propietario=e['propietario']))
    if e['nombre']=='producto':
        for a in e['atributos']:
            if a['nombre'].startswith('temperatura') or a['nombre']=='vida_util_dias': a['propietario']='Calidad'

domains=[
('BD_INVENTARIO','M1/M2/M8','PostgreSQL local; proyección Aurora','Bodega','Sitio custodio','Saldo, reserva y movimientos por sitio/lote','Consistencia local; sin nueva promesa remota aislada'),
('BD_PREVENTA','M3','Aurora PostgreSQL; Room en terminal','Comercial','M3 nube; captura en terminal','Pedido y tarifa informada','Captura disponible; confirmación espera M2'),
('BD_RUTAS','M4/M12','PostgreSQL/PostGIS y Aurora compatible','Planificación/Flota','M4 versión aprobada','Viaje, restricciones y paradas','Lectura local de ruta; cambios en autoridad'),
('BD_PREPARACION','M5','PostgreSQL por sitio','Bodega','M5 sitio','Misión, asignación y salida','Consistencia local sobre carga vigente'),
('BD_REPARTO','M6','Aurora; Room en dispositivo','Operaciones','M6; hechos capturados en terreno','Entrega, rechazo y POD','Disponible para capturar; validación diferida'),
('BD_COBRANZA_FINANZAS','M7/ACL','Aurora; ERP externo','Tesorería/Tributación','M7 captura; ERP contabiliza y emite','Cobros, rendición, saldo proyectado, DTE','Consistencia para cargo; estado incierto ante falla'),
('BD_MAESTROS_CONF','M1/M3/ACL','Aurora; copias locales versionadas','Comercial/Abastecimiento','ERP identidad comercial; módulo configuración','Clientes, SKU, proveedor, sitios','Lectura local; modificación en fuente autorizada'),
('BD_GOBIERNO_ACCESO','Keycloak/M6','PostgreSQL Keycloak; manifiesto local','Seguridad/Flota','IdP identidad; módulo autoriza vínculo','Actor, empresa, turno y autorización','No emitir nuevas identidades aislado'),
('BD_CALIDAD_TRAZABILIDAD','M9','PostgreSQL local y Aurora','Calidad','M9 por lote y sitio','Lote, bloqueo, retiro y custodia','Bloqueo disponible local; liberación autorizada'),
('BD_TELEMETRIA','M9/M12','DynamoDB raw; S3 Parquet; Redshift','Calidad/Flota','Sensor o tercero; consumidor deduplica','Lecturas térmicas y posición','Ingesta disponible; consolidación eventual'),
('BD_EDI_CANALMODERNO','M11','Aurora + originales S3','Comercial','M11 traducción; M3 pedido','Equivalencias, mensajes y acuses','Respuesta comercial tras validación'),
('BD_BI_GERENCIA','M10','S3 Parquet + Glue + Redshift','Control de gestión','Proyección derivada, sin escritura OLTP','Hechos, dimensiones y modelo semántico','Eventual con SLA de frescura explícito'),
('BD_MAILS_NOTIF','Servicio notificaciones','Aurora + SNS','Comercial','Consumidor de avisos','Preferencias, entregas técnicas y reintentos','Eventual; aviso no modifica venta'),
('REDIS_SESIONES_CACHE','Plataforma','Redis administrado central','Plataforma','Fuente OLTP/IdP, nunca caché','Lecturas y sesiones centrales','Eventual; invalidación y bypass'),
('S3_DOCS','M6/M7/M9','S3 cifrado con manifiesto y Object Lock','Operaciones/Tributación','Módulo dueño del objeto','POD, XML DTE, acuses y archivos','Objeto verificado antes de publicar referencia')]

# Cardinalidades lógicas entre contextos; no representan FK físicas entre bases.
relations=[('cliente','punto_entrega','1','0..N','composición comercial'),('cliente','pedido','1','0..N','cliente del pedido'),('pedido','linea_pedido','1','1..N','detalle obligatorio'),('producto','linea_pedido','1','0..N','SKU solicitado'),('producto','lote','1','0..N','origen sanitario'),('proveedor','lote','1','0..N','proveedor del lote'),('recepcion','linea_recepcion','1','1..N','recepción cerrada'),('lote','linea_recepcion','1','0..N','lote recibido'),('unidad_logistica','contenido_unidad','1','1..N','unidad no vacía'),('lote','contenido_unidad','1','0..N','contenido mixto'),('lote','movimiento_stock','1','0..N','libro de custodia'),('linea_pedido','reserva','1','0..N','reservas por lote/sitio'),('reserva','asignacion_lote','1','0..N','consumo acotado'),('linea_pedido','asignacion_lote','1','0..N','servicio multilot'),('mision','linea_mision','1','1..N','misión descargada'),('asignacion_lote','linea_mision','1','0..N','preparación'),('viaje','parada','1','1..N','ruta aprobada'),('viaje','despacho','1','0..N','cargas/salidas'),('pedido','entrega','1','0..N','intentos o parcialidad'),('parada','entrega','1','0..N','visita'),('entrega','detalle_entrega','1','0..N','cero si local cerrado'),('asignacion_lote','detalle_entrega','1','0..N','traza a lote y SSCC'),('entrega','evidencia_pod','1','0..N','evidencias por causal'),('documento_tributario','acuse','1','0..N','acuses diferenciados'),('entrega','cobro','1','0..N','pagos por medio'),('viaje','rendicion','1','0..N','conciliaciones y ajustes'),('entrega','devolucion','1','0..N','rechazos/retornos'),('cliente','movimiento_envase','1','0..N','saldo por tipo'),('sensor','lectura_termica','1','0..N','serie deduplicada'),('lote','bloqueo_calidad','1','0..N','calidad'),('vehiculo','viaje','1','0..N','asignación'),('transportista','vinculo_conductor','0..1','0..N','propio o tercero'),('cliente','saldo_credito','1','0..1','proyección del ERP'),('pedido','mensaje_edi','0..1','0..N','canal moderno')]
write('05/anexos/datos/fuentes/modelo.json',json.dumps(dict(version='1.0-propuesta',base_commit='2799de341bb425c0323119ca51d0e51e050d506a',dominios=domains,entidades=entities,relaciones=relations),ensure_ascii=False,indent=2))
with (BASE/'anexos/datos/fuentes/diccionario.csv').open('w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f); w.writerow(['entidad','dominio','modulo','atributo','tipo','valores','obligatorio','propietario','sensibilidad','regla_entidad'])
    for e in entities:
        for a in e['atributos']: w.writerow([e['nombre'],e['dominio'],e['modulo'],a['nombre'],a['tipo'],a['valores'],a['obligatorio'],a['propietario'],a['sensibilidad'],e['regla']])

sources=[]
external=['Bases MarkDown/Bases Administrativas.md','Bases MarkDown/Bases_Tecnicas_Transversales.md','Bases MarkDown/Caso_02_Logistica.md','LafroX-alvaro-md/Bases/aclaraciones-licitacion.md','LafroX-alvaro-md/03_esquema_solucion_alcance/LAFROX-Subdocumento3.md','LafroX-alvaro-md/03_esquema_solucion_alcance/LAFROX-Formulario-T-12.md']
for name in external:
    p=ROOT.parent/name
    if p.exists(): sources.append(dict(tipo='base o alcance',ruta=name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),consulta='2026-10-02'))
for folder in ['04/partes','04/anexos','04/formularios','Dimensionamiento/dimensionamiento']:
    for p in sorted((ROOT/folder).rglob('*')):
        if p.suffix in ['.tex','.md','.py']: sources.append(dict(tipo='arquitectura base',ruta=p.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),commit='2799de3'))
write('05/formularios/trazabilidad/FUENTES.json',json.dumps(sources,ensure_ascii=False,indent=2))

def diagram(name,nodes,edges):
    out=[r'\begin{tikzpicture}[x=1cm,y=1cm,>=stealth,box/.style={draw=lafroxGris,rounded corners=1pt,text width=3.55cm,minimum height=1.25cm,align=left,inner sep=5pt,font=\fontsize{9.5pt}{12pt}\selectfont},edge/.style={->,line width=.6pt},lab/.style={fill=white,inner sep=2pt,font=\fontsize{9pt}{11pt}\selectfont}]']
    for ident,x,y,title,detail in nodes:
        out.append(r'\node[box] ('+ident+') at ('+str(x)+','+str(y)+') {\\textbf{'+tex(title)+'}\\\\'+tex(detail)+'};')
    for a,b,label in edges:
        positions={ident:(x,y) for ident,x,y,title,detail in nodes}
        placement='lab,midway,above=0.8cm' if positions[a][1]==positions[b][1] else 'lab,midway,text width=1.8cm,align=center'
        out.append(r'\draw[edge] ('+a+') -- node['+placement+'] {'+tex(label)+'} ('+b+');')
    out.append(r'\end{tikzpicture}')
    write('05/figuras/fuentes/datos/'+name+'.tex','\n'.join(out))

diagram('pedido', [('a',0,0,'Cliente','RUT; código ERP'),('b',5.1,0,'Pedido','UUID; tarifa; estado'),('c',5.1,-2.5,'Línea de pedido','SKU; cantidad; precio'),('d',0,-2.5,'Punto de entrega','Dirección; ventana'),('e',5.1,-5,'Reserva M2','Sitio; lote; cantidad'),('f',0,-5,'Producto','GTIN; unidad; rango térmico')],[('a','b','1 : 0..N'),('a','d','1 : 0..N'),('b','c','1 : 1..N'),('c','e','1 : 0..N'),('f','c','1 : 0..N')])
diagram('custodia',[('a',0,0,'Recepción M1','Sitio; proveedor; documento'),('b',5.1,0,'Línea de recepción','Lote; SSCC; cantidad'),('c',0,-2.5,'Lote M9','GTIN + lote proveedor'),('d',5.1,-2.5,'Unidad logística','SSCC; ubicación; contenido'),('e',0,-5,'Movimiento M2','Delta; sitio; secuencia'),('f',5.1,-5,'Asignación M5','Línea pedido; reserva; lote')],[('a','b','1 : 1..N'),('c','b','1 : 0..N'),('d','b','1 : 0..N'),('c','e','1 : 0..N'),('c','f','1 : 0..N'),('d','f','1 : 0..N')])
diagram('entrega',[('a',0,0,'Viaje / parada M4','Conductor; ventana prometida'),('b',5.1,0,'Despacho M5','Carga vigente; guía ERP'),('c',0,-2.5,'Entrega M6','Intento; parcialidad; receptor'),('d',5.1,-2.5,'Detalle de entrega','Asignación; aceptado/rechazado'),('e',0,-5,'POD / objeto','Firma, foto, QR o causal'),('f',5.1,-5,'DTE / acuses','ERP; SII; destinatario')],[('a','b','1 : 0..N'),('a','c','1 : 0..N'),('c','d','1 : 0..N'),('c','e','1 : 0..N'),('b','f','guía vigente')])
diagram('retornos',[('a',0,0,'Entrega M6','UUID; cantidades; evidencias'),('b',5.1,0,'Cobro M7','Medio; monto protegido'),('c',0,-2.5,'Devolución M8','Lote; causal; cuarentena'),('d',5.1,-2.5,'Rendición M7','Esperado; recibido; diferencia'),('e',0,-5,'Movimiento de envase','Cliente; tipo; delta'),('f',5.1,-5,'ERP vía ACL','Abono/DTE; saldo contable')],[('a','b','1 : 0..N'),('a','c','1 : 0..N'),('b','d','conciliación'),('c','e','hechos separados'),('d','f','resultado confirmado')])
diagram('frio',[('a',0,0,'Sensor físico','ID; sesión; secuencia'),('b',5.1,0,'Raw DynamoDB','TTL 30 días; duplicados'),('c',0,-2.5,'Bloqueo local M9','Lote; regla; decisión Calidad'),('d',5.1,-2.5,'Serie S3 / Redshift','Validada; conservación 5 años'),('e',0,-5,'M5 salida','Verifica bloqueo activo'),('f',5.1,-5,'Posición M12','API tercero; campo cifrado')],[('a','b','INT-05'),('a','c','evaluación local'),('c','e','bloquea'),('b','d','hash y conciliación')])
diagram('gobierno',[('a',0,0,'ERP / Keycloak','Maestro comercial / identidad'),('b',5.1,0,'Copias de lectura','Versionadas; ámbito de sitio'),('c',0,-2.5,'M11 Canal moderno','Original; equivalencia; MDN'),('d',5.1,-2.5,'Avisos / Redis','Preferencia / caché derivada'),('e',0,-5,'Auditoría de negocio','Antes; después; actor; equipo'),('f',5.1,-5,'Objetos S3','Manifiesto; hash; retención')],[('a','b','publicación'),('c','e','correlación'),('d','e','consulta sensible'),('e','f','archivo protegido')])
diagram('analitica',[('a',0,0,'Eventos OLTP','Outbox; event_id; versión'),('b',5.1,0,'Ingesta incremental','Orden; duplicados; marca agua'),('c',0,-2.5,'S3 / Glue','Parquet; catálogo; linaje'),('d',5.1,-2.5,'Redshift','Hechos; dimensiones SCD2'),('e',0,-5,'Modelo semántico','Indicador; fórmula; fuente'),('f',5.1,-5,'Autoservicio CLIENTE','Filtros; detalle; exportación')],[('a','b','acuse durable'),('b','d','microcarga'),('c','d','reproceso'),('d','e','vista gobernada'),('e','f','permisos por fila')])
diagram('migracion',[('a',0,0,'ERP / WMS / archivos','Extracto fechado y con huella'),('b',5.1,0,'Perfilado','Duplicados; nulos; unidades'),('c',0,-2.5,'Transformación','Mapeo ID; reglas versionadas'),('d',5.1,-2.5,'Carga aislada','Aceptados / cuarentena'),('e',0,-5,'Conciliación','Recuentos; sumas; muestra'),('f',5.1,-5,'Corte o reversión','Responsables; límite de tiempo')],[('a','b','exportación'),('b','d','calidad'),('c','d','mapeo'),('d','e','control'),('e','f','decisión')])
diagram('autoridad',[('a',5.1,0,'M3 nube','Captura; solicita reserva'),('b',0,0,'M2 sitio custodio','Confirma sitio/lote; versión'),('c',0,-5.6,'Aurora proyección','Consume eventos; no doble stock'),('d',0,-2.8,'Outbox local','Movimiento y resultado durable'),('e',5.1,-2.8,'DMS INT-12','Talca: esquema solo lectura'),('f',5.1,-5.6,'Room en terreno','UUID; 14 h; acuse de resultado')],[('a','b','Solicitud con enlace'),('b','d','Commit local'),('d','c','INT-03 / 04'),('b','e','CDC lectura'),('f','c','INT-01 / 02')])

intro=r'''\chapter{Introducción al Modelo y gestión de datos}
\label{cap:datos}
LafroX estructura los datos de Distribuidora Puelche S.A. para reconstruir la relación entre pedido, lote, preparación, salida y entrega, incluso cuando el hecho se captura sin cobertura. El modelo desarrolla las entidades de la arquitectura del Subdocumento 4 y conserva el alcance por etapas del Subdocumento 3. La identidad comercial y la emisión tributaria permanecen en el ERP; los módulos logísticos mantienen autoridad explícita sobre sus operaciones.

El apartado 5.1 presenta el modelo por dominio; 5.2 justifica persistencia, consistencia, analítica y gobierno; 5.3 establece migración y conciliación; y 5.4 deriva las decisiones de desempeño de la volumetría del caso. El archivo independiente \emph{LAFROX-Subdocumento5-Anexos.pdf} contiene el diccionario y las matrices 5-A a 5-H. La trazabilidad se aporta para su integración al Formulario T-12 que acompaña al Subdocumento 3, sin sustituirlo.

Las cifras de entrada corresponden a las Bases del Caso 02 y a la memoria de dimensionamiento de arquitectura. Los parámetros de diseño se identifican como supuestos y criterios de aceptación; no se presentan como mediciones de sistemas del CLIENTE. La ejecución de cargas, pruebas y certificación de resultados se realizará en los ambientes de implantación, con evidencias y responsables designados.
'''
write('05/partes/00_introduccion.tex',intro)

model=r'''\section{Modelo}
\label{sec:5-modelo}
El dato se captura donde ocurre el hecho: recepción en andén, preparación por lectura GS1, entrega en el local y rendición en Tesorería. El identificador original enlaza esos registros sin exigir que la persona vuelva a digitarlos. Los dominios separan propietarios y reglas; compartir PostgreSQL o el proceso Laravel no permite escribir tablas privadas de otro módulo.

\subsection{Identidad, relaciones y datos maestros}
El ERP conserva la identidad autorizada de cliente, producto y proveedor. La ACL traduce sus códigos a UUID canónicos y mantiene una correspondencia única \emph{fuente, entidad, identificador externo}. Cambios de presentación del producto crean equivalencias GTIN versionadas; una misma razón social escrita de dos maneras no crea dos clientes. Comercial gobierna preferencias de contacto y puntos de entrega, Abastecimiento los atributos de compra y Calidad los rangos sanitarios. Cada propiedad tiene una autoridad, aunque el maestro reúna aportes de varios responsables.

El esquema operacional se normaliza hasta tercera forma normal dentro de cada contexto: cabecera y detalle se separan, las relaciones muchos a muchos se materializan y los catálogos limitan estados y unidades. Precio informado, ventana prometida y autor del hecho se conservan como instantáneas históricas deliberadas; no se recalculan con el maestro vigente. La FK dentro de un contexto comprueba integridad; entre bases se usa referencia canónica, validación contractual y conciliación de referencias huérfanas.

Todos los registros de negocio incorporan UUID, fecha UTC y versión positiva. Hora del hecho y hora de persistencia son distintas. La presentación usa America/Santiago, conservando el desplazamiento horario de la captura. Los importes operacionales se expresan con decimales exactos y las cantidades con unidad base y conversión versionada; no se redondea un saldo con coma flotante.
'''+fig('pedido','Modelo de cliente, pedido y reserva','relaciona cliente, punto de entrega y líneas del pedido con la reserva de M2.')+r'''
Un pedido confirmado posee al menos una línea. Una línea puede originar varias reservas y asignaciones a lote; la suma aceptada no excede la cantidad solicitada, salvo modificación explícita y autorizada del pedido. La captura offline conserva precio y tarifa, pero no promete una reserva que el sitio custodio aún no confirmó. Esto evita que dos preventistas comprometan la última unidad usando copias atrasadas.

\subsection{Recepción, inventario y preparación}
M1 registra recepción y sus líneas, enlazadas a lote y unidad logística. El lote sanitario se identifica por GTIN y lote del proveedor; se mantiene también el proveedor de origen para desambiguar colisiones. Vencimiento es atributo, no identidad de un nuevo lote. Si el mismo código llega con vencimientos incompatibles, Calidad resuelve la discrepancia antes de liberarlo. Una unidad SSCC puede contener varios lotes mediante una relación de contenido.
'''+fig('custodia','Modelo de lote, SSCC y custodia','expone el camino desde la recepción hasta la asignación del pedido y el libro de movimientos.')+r'''
M2 calcula stock por sitio, lote y ubicación a partir del libro de movimientos. La reserva inmoviliza cantidad; la preparación la consume y el despacho reduce existencia física. M5 conserva misión, línea confirmada y asignación a lote/SSCC. Para responder un retiro se recorre lote, asignación, detalle de entrega y cliente; para investigar una entrega se sigue la ruta inversa. Un ajuste deja contramovimiento, motivo y aprobación, sin borrar el hecho original.

\subsection{Ruta, salida y entrega}
M4 conserva viaje aprobado, capacidades y paradas ordenadas; M12 añade ruta real por la API de telemetría existente. La ventana prometida se registra antes del reparto para que OTIF sea reproducible. M5 mantiene la versión de carga y su guía emitida por ERP. El estado de salida liberada exige documento válido de esa misma carga, disponible localmente.
'''+fig('entrega','Modelo de salida, entrega y evidencias','distingue visita, carga, intento de entrega, evidencia operativa y documentación tributaria.')+r'''
Un pedido puede no tener entrega o tener varios intentos y entregas parciales. Cada detalle refiere una asignación de lote y expresa cantidad aceptada, rechazada y causal. Una entrega sin recepción, por ejemplo local cerrado, no fabrica un receptor ni un POD firmado. Las evidencias son objetos con hash, versión y fecha; la constancia de negativa se distingue de una firma. El acuse técnico del SII, el MDN EDI y el acuse de mercadería del destinatario se registran como tipos separados. El mecanismo de validez del acuse se selecciona con Tributación conforme al Subdocumento 4; una foto o un QR no lo acredita por sí solo.

\subsection{Cobranza, devoluciones y retornables}
M7 captura cobro por medio y lo vincula a entrega, viaje y conductor custodio. Tesorería compara efectivo esperado con recibido; la diferencia conserva causal y decisión. Un timeout de pasarela deja el pago incierto hasta consultar su referencia estable. El saldo de crédito es proyección fechada del ERP y no se incrementa por una lectura del dispositivo.
'''+fig('retornos','Modelo de cobro y logística inversa','separa cobro, rendición, devolución de producto y movimiento de envase.')+r'''
M8 distingue recepción física del retorno, aptitud sanitaria y efecto financiero. El sitio registra el hecho aun sin WAN; Calidad decide liberación o descarte, y el ERP emite el documento posterior cuando corresponde. Los envases se controlan por cuenta corriente de cliente y tipo, con movimientos de cargo y devolución; SSCC pertenece a custodia logística y no individualiza los 68.000 canastillos del caso. Una disputa conserva el saldo aceptado y la evidencia en una bandeja de excepción.

\subsection{Calidad, telemetría e información transversal}
M9 relaciona sensor, lectura, lote y bloqueo. Dos gateways de Talca leyendo el mismo sensor transmiten la misma identidad de muestra; la clave sensor/sesión/secuencia impide duplicar la serie. La diferencia de valor bajo esa clave genera incidente. La geolocalización se recibe por INT-15, se cifra por campo y se usa para ruta y costo, sin incorporar cámaras de cabina ni convertir GPS en control de jornada.
'''+fig('frio','Modelo de temperatura y bloqueo','separa la decisión local de Calidad de la conservación de series y la posición de flota.')+r'''
La temperatura cruda tiene una permanencia propuesta de 30 días en DynamoDB; la serie validada se conserva cinco años en S3 Parquet y Redshift. El plazo corto del raw no reemplaza la retención sanitaria. El consumidor verifica publicación y conciliación de la serie antes de permitir su expiración.
'''+fig('gobierno','Dominios de maestros, acceso, EDI y documentos','ubica maestros, copias versionadas, mensajes de cadenas, notificaciones y registros de auditoría.')+r'''
BD\_GOBIERNO\_ACCESO conserva la referencia a identidad Keycloak, vínculo histórico de conductor y autorización de turno; no almacena contraseñas de aplicación ni sustituye al IdP. BD\_EDI\_CANALMODERNO enlaza original, traducción y pedido M3. BD\_MAILS\_NOTIF registra preferencia, envío y acuse técnico. REDIS\_SESIONES\_CACHE es prescindible y S3\_DOCS conserva los objetos bajo manifiesto. BD\_BI\_GERENCIA representa información derivada; su modelo dimensional se desarrolla en 5.2.

El Anexo 5-A documenta cada atributo con tipo, dominio de valores, obligatoriedad, propietario y sensibilidad. El Anexo 5-B detalla cardinalidades y los quince dominios de almacenamiento. Las tablas auxiliares de outbox, inbox y auditoría pertenecen a cada contexto productor o consumidor; no agregan tres bases físicas a las quince familias de arquitectura.
'''
write('05/partes/5.1_modelo/01_modelo.tex',model)

management=r'''\section{Gestión de datos}
\label{sec:5-gestion}
La gestión conserva el derecho de cada módulo a decidir y el del CLIENTE a consultar, exportar y verificar sus datos. La selección tecnológica de arquitectura se concreta aquí por dominio, transacción y comportamiento durante una partición; no se atribuye una única propiedad CAP a toda la solución.

\subsection{Persistencia y límites transaccionales}
PostgreSQL/PostGIS se mantiene para WMS y geografía, y Aurora PostgreSQL para dominios centrales. La referencia de arquitectura es PostgreSQL 16.x y PostGIS compatible; la versión de Aurora se fija por compatibilidad y soporte al implantar. Las cantidades, relaciones y restricciones justifican persistencia relacional en inventario, pedidos, entregas y finanzas. DynamoDB recibe muestras de telemetría identificables por clave; S3 guarda objetos y series Parquet; Redshift sirve hechos y dimensiones. Redis acelera lecturas, no custodia movimientos ni pagos.

La reserva M2 bloquea el saldo del agregado sitio/lote, valida disponibilidad y escribe reserva, auditoría y outbox en una transacción. Para reglas que abarcan varios saldos se propone aislamiento serializable con reintento completo y orden estable de bloqueo. No se mantiene una transacción abierta mientras se espera al ERP o a otro sitio. Una solicitud de M3 se resuelve como pendiente, confirmada o rechazada; compensar libera una reserva idempotentemente y deja registro. La semántica de aislamiento y sus reintentos se basa en PostgreSQL Global Development Group (s. f.-a).

Entre contextos el flujo utiliza eventos canónicos con \emph{event\_id}, \emph{transaction\_id}, agregado, versión, sitio, fecha del hecho y versión del esquema. La outbox persiste con el cambio; el consumidor confirma solo después de resultado durable en su inbox. El envío puede repetirse; la unicidad de identidad y huella evita repetir el efecto de negocio. La deduplicación conserva resultado durante 30 días según arquitectura; mensajes anteriores se aíslan para revisión. El FIFO y la cola no sustituyen esa regla.

\subsection{Autoridad, particiones y sincronización}
Talca conserva el maestro operativo WMS y publica su CDC INT-12 en un esquema de lectura separado. Concepción ejecuta el perfil wms\_only y cada cross-docking conserva su operación local acotada. La autoridad de un movimiento corresponde al sitio custodio; el pedido central no modifica el saldo remoto desde una proyección de Aurora. El agregado se identifica por sitio/lote/ubicación y época de autoridad. Transferir autoridad requiere cerrar la versión anterior, conciliar y habilitar la nueva; durante un corte no se promueve otra autoridad a ciegas.
'''+fig('autoridad','Autoridad de escritura y recorridos de sincronización','muestra la confirmación en M2, la outbox local y la separación entre proyección de eventos y CDC de lectura.')+r'''
Durante la partición se favorece consistencia para nueva reserva, liberación sanitaria, pago confirmado y emisión tributaria: sin respuesta de su autoridad, esos efectos quedan pendientes o bloqueados. Se favorece disponibilidad de captura para pedido, POD, retorno físico y lectura térmica, manteniendo identidad, evidencia y estado pendiente de reconciliación. El WMS sigue trabajando sobre existencias propias y misiones ya asignadas durante 24 horas; el dispositivo captura su turno de 14 horas. Ese funcionamiento no permite comprometer stock de un sitio inaccesible.

La sincronización ordena por agregado y secuencia, detecta huecos y no aplica un evento futuro antes de su dependencia. El sitio retiene movimientos hasta acuse durable; la nube consolida una sola proyección por evento. Stock se concilia con saldo inicial más movimientos y reservas, no con \emph{last write wins}. Entrega posterior a cancelación queda en conflicto para Operaciones, precio cambiado requiere aceptación comercial y devolución no acredita nota de crédito antes de respuesta ERP. El Anexo 5-C reproduce el protocolo y sus salidas por escenario.

La réplica DMS y los consumidores de INT-03 no escriben la misma tabla de destino. La protección externa durante pérdida simultánea de sitio y WAN sigue condicionada a la prueba AL-DR-01 de arquitectura; una cola local no demuestra RPO de 15 minutos. Se conserva RTO máximo de cuatro horas y RPO máximo de quince minutos para servicios críticos, con ensayo de pérdida de sitio. No se ofrece una excepción implícita por operación desconectada.

\subsection{Contratos y carga masiva}
OpenAPI 3.1 documenta las operaciones y AsyncAPI 2.6 o superior los eventos; la generación desde código y la validación se incorporan a CI/CD al implementar. El contrato fija tipos, obligatoriedad, errores por fila, idempotencia y versión SemVer. Un cambio incompatible tiene preaviso mínimo de seis meses y coexistencia de versiones con prueba de consumidores. OAuth 2.1 con credenciales de cliente o mTLS protege intercambios; se heredan las quince interfaces, ventanas y volúmenes de los anexos 4.1-G/H/I, sin renumerarlas.

La ACL traduce el ERP, conserva código de origen y consulta el resultado de una solicitud tributaria incierta antes de reintentar. GS1 identifica producto, SSCC y ubicaciones; EANCOM, GS1 XML y EPCIS se aplican por perfil de cadena, y el ERP preserva el formato tributario original. La importación CSV UTF-8 o JSON valida primero esquema y referencias, reporta número de fila y causa, y separa aceptadas de cuarentena. Se carga cada agregado completo en su transacción; procesar parcialmente un archivo no deja media cabecera con detalles ausentes.

El portal de desarrolladores existente en el alcance de contratos publicará documentación navegable. Credenciales de prueba autoservidas y sandbox, materia deseable RT-05.24, se proponen con ámbito y expiración sin acceso productivo; la cobertura documental no afirma que el portal esté desplegado.

\subsection{Separación transaccional y explotación analítica}
M10 consume eventos e incrementales en recursos distintos del OLTP. No ejecuta paneles directamente sobre las tablas WMS ni usa INT-12 como único canal de frescura, porque CDC puede retrasarse bajo aislamiento. S3 Parquet conserva capas de recepción y curación con manifiestos; Glue transforma y registra origen; Redshift materializa el modelo dimensional. El flujo incremental operacional usa microcargas propuestas de un minuto y marca de agua por fuente; los procesos históricos y de gestión corren en colas separadas. La prueba determina el tamaño de lote y la concurrencia compatible con los SLA.
'''+fig('analitica','Modelo de explotación y linaje analítico','relaciona eventos de negocio, transformación, hechos/dimensiones y autoservicio del CLIENTE.')+r'''
El hecho de entrega tiene grano de intento/entrega, el de pedido una línea versionada, el de inventario un movimiento, el de frío una lectura validada y el de rendición un cierre por viaje/conductor. Dimensiones conformadas de fecha, sitio, cliente, producto, canal, ruta y causal permiten navegación común; cliente, producto y zona usan historia SCD2 cuando cambia un atributo de análisis. La transacción de origen y la versión de transformación permanecen asociadas al hecho. Reproceso sustituye la misma clave/version, sin sumar de nuevo.

OTIF se calcula por pedido comprometido en el período: numerador de pedidos con todas sus líneas netas aceptadas dentro de ventana sobre denominador de pedidos comprometidos. Un intento parcial no cuenta como completo; reintento se evalúa contra la promesa inicial salvo modificación acordada antes del vencimiento y auditada. Fill rate compara unidades aceptadas con unidades comprometidas en su unidad base; perfect order añade ausencia de daño y documentación correcta. Devoluciones, merma, diferencia de caja y costo de servir tienen fórmulas y granularidad en el Anexo 5-F. Un costo operativo del CLIENTE no incluye precios de la oferta tecnológica.

El modelo semántico expone filtros por período, sitio, canal, zona, producto y causal, y profundiza hasta el registro de origen autorizado. QuickSight del catálogo de arquitectura sirve autoservicio; vistas y permisos por fila excluyen receptor, pago y GPS personal de usuarios sin facultad. Cada informe exporta CSV/JSON y admite calendario de envío con registro de destinatario. Se propone catálogo automatizado de dataset, columna, transformación y ejecución enlazado a event\_id para RT-05.10.

La latencia del caso es cinco minutos para indicadores diarios, dos horas para cierre comercial tras el último camión y cuatro horas para gestión. Se mide desde ocurrido\_en hasta visible\_en, no solo duración del ETL. Bajo ausencia de enlace se muestra antigüedad y cobertura por sitio: no se declara fresco un panel que no recibió el hecho. La recuperación de backlog se prueba junto con la sincronización de dos horas del CD y diez minutos por terminal; la imposibilidad de sostener cinco minutos globales sin enlace se registra como condición de aceptación, sin rebajar el umbral exigido. No se incorpora analítica predictiva, deseable RT-05.30, por coherencia con la arquitectura propuesta.

\subsection{Calidad, auditoría y protección}
La calidad se gestiona con completitud, exactitud y consistencia conforme al marco requerido ISO/IEC 25012. Validación de RUT/GTIN, cantidades, unidad, lote/vencimiento y estados ocurre en captura y se repite en el servidor. Los datos sanitarios y financieros inválidos quedan en cuarentena; nunca se corrigen inventando lote o duplicando un saldo. Cada defecto tiene fuente, regla, responsable, severidad, decisión y reejecución. El tablero expone proporción válida, defectos abiertos y antigüedad por dominio; Anexo 5-G declara metas de diseño y evidencia de verificación.

La auditoría de negocio guarda quién, qué, cuándo, equipo, valores anteriores y posteriores, motivo, correlación y regla aplicada. Se persiste con el cambio y se exporta a archivo inmutable; las lecturas sensibles también dejan huella. El plazo sigue al dato auditado. Los logs técnicos de CloudWatch mantienen doce meses en línea y veinticuatro de archivo conforme a arquitectura; ese plazo técnico no limita los seis años de trazabilidad del DTE o POD.

El CLIENTE conserva rol responsable y LafroX actúa como encargado bajo instrucciones documentadas y acuerdo del Artículo 85. Cada atributo del diccionario declara sensibilidad. Cifrado de campo cubre comportamiento de pago, antecedentes comerciales restringidos y posición de personas, con claves KMS separadas, permisos mínimos y rotación; TLS protege transporte. Para búsqueda de identificadores cifrados se propone token de igualdad bajo clave separada, nunca texto claro en logs. No se conservan PAN ni CVV; pasarela entrega token/referencia. SQL y exportaciones respetan ámbitos de sitio, rol y finalidad.

Subencargados y transferencia internacional requieren autorización escrita del CLIENTE según las bases. La localización primaria sa-east-1 y recuperación us-east-1 de arquitectura se incluye en ese acuerdo; no se presume autorización por elegir región. Preproducción usa datos sintéticos o seudonimizados salvo extracto controlado para ensayo. Solicitudes de titulares se tramitan con el CLIENTE, registrando base de retención y acciones; la brecha se comunica dentro de las 24 horas exigidas, además de la cadena crítica de seguridad.

\subsection{Retención, archivado, eliminación y portabilidad}
Los documentos tributarios y POD se conservan seis años; trazabilidad sanitaria, al menos cinco años o vida útil más seis meses si es mayor; temperatura, cinco años; GPS personal, doce meses. La base local retiene cuatro meses de movimientos según capacidad de arquitectura y los lotes/stock presentes; archivar no elimina un lote todavía necesario ni un evento sin acuse. La consulta histórica usa nube y repositorio protegido. Los tiempos se cuentan desde cierre documental o fecha del hecho según categoría, conservando excepciones y suspensión legal.

El TTL de DynamoDB es asíncrono y no prueba una fecha exacta de borrado (Amazon Web Services, s. f.-a). Una rutina controla vencidos, excluye registros caducos de consulta y verifica eliminación con inventario posterior. Raw térmico solo expira tras consolidación comprobada. S3 Object Lock protege versiones por plazo y retención legal; no permite prometer borrado de una versión todavía retenida (Amazon Web Services, s. f.-b). Se separan buckets/categorías y se evita bloquear GPS durante seis años.

La eliminación genera orden aprobada, listado de claves/versiones, controles de dependencias y certificado con huellas y resultado. El procedimiento comprende OLTP, hechos/dimensiones, Parquet, todas las versiones S3, índices, cachés, móviles y copias temporales. Los respaldos inmutables siguen su calendario definido: la orden de supresión queda fuera del respaldo y se reaplica antes de abrir un entorno restaurado. Si existe bloqueo legal se conserva lo requerido y se comunica la causa y nueva revisión; no se promete borrar criptográficamente una copia cuya clave sea compartida con datos vigentes.

El CLIENTE puede exportar por autoservicio la totalidad de datos en CSV/JSON, Parquet para series y XML/originales para documentos, con diccionario, relaciones, manifiesto de archivos, recuentos y SHA-256. La exportación autorizada se ejecuta sobre instantánea consistente o marca de agua por fuente, queda auditada y no exige intervención de LafroX ni costo adicional. En finalización contractual se realiza devolución verificada y eliminación certificada bajo instrucciones del CLIENTE, incluyendo subencargados y ventanas de expiración de respaldos.
'''
write('05/partes/5.2_gestion_de_datos/01_gestion.tex',management)

migration=r'''\section{Estrategia de migración}
\label{sec:5-migracion}
La migración reemplaza el WMS 2013 por sitio y ola, preserva el ERP 2017 e incorpora los registros de planillas y cuadernos que el caso identifica. No se supone que esos orígenes tienen API, esquema limpio o cinco años completos de temperatura digital. El inventario y perfilado determina su disponibilidad; las ausencias se explican al CLIENTE sin fabricar historia.

\subsection{Alcance, fuentes y estimación de volumen}
Maestros de clientes, productos y proveedores se cargan completos; ventas y pedidos abarcan tres años; inventario y movimientos dos; trazabilidad sanitaria cinco; cuentas por cobrar saldos vivos más dos años. Históricos anteriores y documentos sujetos a retención permanecen consultables en repositorio protegido aunque no formen parte del saldo OLTP. Fotografías/POD, XML y registros térmicos existentes se inventarían y se trasladan como objetos o archivos, preservando su integridad.

La Tabla~\ref{tab:5-migracion-volumen} reproduce el cálculo de arquitectura con KB binarios: GB = KB/1.048.576. El factor dos reserva índices y sobrecarga lógica de destino; no representa una segunda copia de seguridad.
'''+table('Volumen de migración estructurada de referencia','tab:5-migracion-volumen',['Familia','Derivación de KB','KB estimados'],[
('Maestros','14.200 × 2 + 8.400 × 0,5 + 180 × 1','34.180'),('Ventas/pedidos','(31.000 + 260.000) × 36 × 1','10.476.000'),('Inventario','279.050 × 24 × 0,5','3.348.600'),('Trazabilidad','1.150 × 60 × 20','1.380.000'),('Cuentas por cobrar','34.000 × 24 × 1','816.000'),('Total origen','Suma de cinco familias','16.054.780'),('Destino con sobrecarga','Total × 2 / 1.000.000','30,62 GiB (32,11 GB decimales)')],[.24,.43])+r'''
La memoria de arquitectura rotula 32,11 GB: su equivalencia se obtiene con 1.000 KB por MB y 1.000 MB por GB, mientras el cálculo binario da 30,62 GiB. Se conservan ambos valores y se fija la unidad en cada reporte. Las 20 KB por recepción trazable, una KB por registro comercial y saldos vivos incluidos en la cota de dos años son supuestos SV de dimensionamiento, no tamaños medidos. Si saldos vivos fuera de esa cota o archivos documentales elevan el volumen, se amplía el presupuesto antes del ensayo. El Anexo 5-E presenta sensibilidad y evita sumar evidencia nueva como si fuera historia efectivamente disponible.

\subsection{Perfilado, saneamiento y transformación}
Cada extracto se recibe fechado, con hash, origen, permisos y responsable. Se trabaja en staging aislado; las reglas se versionan. Se verifica unicidad de RUT/código, GTIN, unidades, cardinalidades, signos y saldos; se detectan fechas imposibles, referencias huérfanas, cliente duplicado, lote ausente y temperaturas fuera de instrumento. La limpieza conserva original, regla, valor transformado y decisión humana cuando afecta dinero, lote o identidad.
'''+fig('migracion','Flujo de migración y decisión de corte','separa los extractos de origen, la calidad, la carga y el control antes de abrir el destino.')+r'''
La transformación normaliza RUT y GTIN, fechas con zona, códigos y unidad base; asigna UUID por correspondencia durable, no aleatoriamente en cada reejecución. Pedido y detalle se cargan juntos; movimientos preservan referencia de lote/SSCC y fecha. Una trazabilidad sin lote se registra como evidencia incompleta en repositorio histórico y no se convierte en stock libre. Las decisiones de fusión de cliente y ajuste de saldo son responsabilidad de Comercial y Tesorería respectivamente. El Anexo 5-D detalla origen, destino, reglas y tratamiento de excepciones.

\subsection{Dos ensayos y conciliación verificable}
El primer ensayo completo en Preproducción ejecuta extracción, carga, conciliación y reversión con un inventario de todas las familias. Mide duración y defectos por fase. El segundo repite el alcance completo con reglas corregidas y ensaya captura de delta, congelamiento de escritura, aplicación final y arranque. Se requiere que ambos produzcan acta, logs, hashes y reporte de diferencias, no solo muestras. DMS ayuda a validar las tablas replicadas compatibles, pero no sustituye controles de objetos, reglas de negocio ni fuentes no relacionales (Amazon Web Services, s. f.-c).

La conciliación compara filas por familia/período/sitio, sumas exactas de cantidades e importes, saldos vivos, referencias y hashes de objetos. Origen aceptado más cuarentena y exclusiones autorizadas explica el total extraído. Se exige cero diferencias monetarias o de stock sin explicación y cero huérfanos en conjuntos liberados; 100\% de archivos documentales tienen huella. El muestreo dirigido propuesto cubre al menos 30 casos por fuente y cada patrón de excepción, incluyendo los de mayor importe, lotes bloqueados, devolución y entrega parcial; no reemplaza las sumas completas. La aceptación de un defecto no elimina la obligación sanitaria o contractual.

\subsection{Corte por sitio y reversión}
El volumen inicial se precarga antes del corte. Se propone domingo de ocho horas como ventana de diseño: 30 minutos congelar y comprobar respaldo, 60 extraer/aplicar delta, 90 conciliar, 60 probar recorridos, 30 decidir apertura y 120 reservar para reversión; quedan 90 minutos de margen. Son presupuestos que ambos ensayos deben demostrar. A 20 Mbps efectivos, 32,11 GB de destino equivaldrían a 3,57 horas de transferencia ideal; por ello no se transfiere toda la historia durante el corte. La cota propuesta de delta es 1,5 GB, con diez minutos ideales a ese caudal y 60 presupuestados incluyendo transformación; se verifica en sitio.

El cronograma de Subdocumento 7 fijará mes y fecha de cada ola; aquí se establece precedencia: maestros y Talca, Concepción, después cada cross-dock según ensayo y readiness. El corte termina antes de preparación 22:00 y no se programa durante 1–25 de septiembre, diciembre ni primeros tres días hábiles de mes. Se respetan las ventanas protegidas de recepción, preparación y despacho. Una ventana dominical solo se usa tras acordar las actividades reales del sitio.

La decisión go/no-go corresponde a Operaciones, Tesorería, Calidad y responsable de implantación. Antes de apertura, un fallo restaura el punto consistente probado y devuelve escritura a la fuente anterior. Después de apertura no se restaura ciegamente una copia vieja: se congela destino, exportan todos los eventos nuevos y se concilian para reaplicar o compensar en el legado antes de reabrirlo. Nunca escriben ambos WMS sobre el mismo agregado. Si las dos horas de reserva no bastan en ensayo, la ola se rediseña antes de producción. Los históricos no migrados permanecen consultables y con identificador de fuente hasta terminar su retención.
'''
write('05/partes/5.3_estrategia_de_migracion/01_migracion.tex',migration)

performance=r'''\section{Estrategia de desempeño}
\label{sec:5-desempeno}
Las consultas y escrituras se priorizan según la ventana real del caso. Preparación, despacho, preventa y retorno de flota tienen cargas distintas; sumar sus máximos como si fueran simultáneos sobredimensiona y usar promedio diario oculta el cuello de botella. El cálculo de referencia mantiene el perfil horario de arquitectura y distingue transacción de negocio, solicitudes API y mensajes de integración.

\subsection{Carga, capacidad y unidades}
El caso entrega 31.000 pedidos y 260.000 líneas mensuales, con 1.400 entregas diarias normales y 2.600 en septiembre. El factor peak es 2.600/1.400 = 1,857. La memoria vigente obtiene 12,30 solicitudes/s en régimen, 14,66 peak y una prueba a 1,5 × 14,66 = 21,99; el máximo del despacho es 5,50 y no el máximo diario. Esas solicitudes no se convierten directamente en IOPS: la prueba mide SQL, filas, WAL, aciertos de caché y tiempo de bloqueo por recorrido.

La Tabla~\ref{tab:5-capacidad} conserva estimaciones decimales de almacenamiento y distingue contenido de sobrecarga, horizonte y sensibilidad.
'''+table('Capacidad de referencia y horizontes de conservación','tab:5-capacidad',['Familia','Generación anual','Horizonte / volumen'],[
('Transaccional','50,75 GB con factor 2','6 años: 304,49 GB; cota, no retención universal'),('POD','87,72 GB','6 años: 526,34 GB al volumen actual'),('Temperatura','0,5602 GB raw; 0,1400 GB comprimidos','5 años: 0,7002 GB consolidados'),('Posición','3,2009 GB raw; 0,8002 GB comprimidos','12 meses: 0,8002 GB consolidados'),('POD año 3','87,72 × 36.000/31.000','101,87 GB/año'),('Migración estructurada','16,05 GB payload estimado','32,11 GB con factor 2')],[.24,.33])+r'''
Las fórmulas y sensibilidad a crecimiento están en el Anexo 5-E. El factor 0,25 de compresión de series se valida con Parquet; no se aplica a fotografías ya comprimidas ni a bytes cifrados sin ensayo. El almacenamiento retenido, respaldo, réplica y buffer se presupuesta por separado: el payload histórico compartido no se vuelve a sumar por cada dominio lógico. La base local conserva maestros, existencias, lotes presentes y cuatro meses de movimientos; historia de retención se archiva en nube con referencias consultables.

\subsection{Índices, particiones y consultas}
Stock usa índice por sitio/lote/ubicación y reserva activa por sitio/lote/estado. FEFO filtra existencia liberada y ordena por vencimiento, no por nombre de producto. Pedido se busca por cliente/fecha y UUID; línea por pedido/número. Trazabilidad indexa GTIN/lote proveedor, asignación por lote y detalle de entrega por asignación. Geografía usa GiST de PostGIS y consulta parametrizada; el teléfono recibe ruta aprobada, no calcula un join analítico sobre el historial GPS.

Movimientos, auditoría y eventos voluminosos se proponen con partición mensual por ocurrido\_en, particiones futuras y control de poda. La llave única física de una tabla particionada incluye la clave de partición; un registro de identidad no particionado controla unicidad global event\_id. No se declara un índice global inexistente ni se retira una partición con retención o referencias activas. PostgreSQL documenta esas limitaciones y las ventajas de poda de particiones (PostgreSQL Global Development Group, s. f.-b).

El Anexo 5-E presenta un catálogo de consultas y candidatos de índices que se confirman con EXPLAIN ANALYZE y datos representativos en QA; no se ejecuta ANALYZE costoso sobre producción en despacho. Se evitan SELECT *, lecturas N+1 del ORM y páginas profundas con OFFSET; la paginación por clave fecha/id limita filas. Las exportaciones y reportes usan lectura dedicada o capa analítica y colas de baja prioridad. Los planes se comparan después de cada versión y se retiran índices que agregan costo de escritura sin uso observado.

\subsection{Caché y copias de turno}
Se propone TTL central de 30 segundos para vista indicativa de stock/crédito y 15 minutos para catálogo, siempre con versión e invalidación por evento. Esos TTL son parámetros de diseño: confirmar reserva consulta M2 y confirmar crédito la autoridad financiera. Ante caída de Redis se omite caché con límites de concurrencia; no se detiene la escritura durable. SQLite/Room mantiene copia cifrada de datos asignados a turno y cola de operaciones distinta. No borra UUID/POD por terminar turno antes de acuse; un supervisor gestiona cola vencida o de más de 30 días.

La identidad respeta credencial de ocho horas en bodega y catorce en terreno; la copia de solo lectura de 24 horas del sitio no habilita identidades nuevas. El dispositivo solo carga datos de su ámbito, purga tras sincronización y plazo de trabajo autorizado, y MDM bloquea o borra ante pérdida. Fotos conservan hash y tamaño máximo de diseño de la memoria; una compresión posterior no reemplaza el original de una evidencia ya registrada.

\subsection{Drenaje, mantenimiento y verificación}
La ruta rural de 34 clientes produce 9,83 MB por dispositivo conforme a arquitectura. Para diez minutos requiere 9,83 × 8/600 = 0,131 Mbps efectivos. Se ensaya reparto completo, reenvíos y competencia de Wi-Fi al retorno. El CD acumula 1,68 GB/día en Talca y 1,09 en Concepción; su drenaje dimensionado en arquitectura incluye WAL, broker, telemetría, observabilidad y respaldo, no solo eventos. Los dos gateways de Talca no duplican las muestras térmicas en el almacén curado.

Los recorridos críticos se verifican contra el caso: confirmar línea de preparación hasta un segundo, registrar entrega hasta dos, línea de preventa hasta 1,5 y consulta stock/crédito hasta dos. Se registran percentiles y máximos, errores y operaciones no confirmadas; publicar un p95 favorable no exime las violaciones del umbral exigido. El ensayo combina 21,99 solicitudes/s, datos retenidos, 24 horas de backlog, pérdida de caché y restauración, con presupuestos de concurrencia por perfil. El límite de ocho tareas Fargate y las capacidades de sitio son los de arquitectura, no nuevos recursos implícitos.

Se observan bloqueo, lag de réplica, edad de outbox, tasa de excepción, espacio libre, particiones, autovacuum y latencia analítica. Se propone alerta de espacio al 70\%, acción de ampliación al 80\% y reserva de al menos 20\% tras crecimiento proyectado, ajustadas con prueba. Backups y restauración se ensayan hasta los RTO/RPO de arquitectura. DDL, cargas completas y cambios de índices se programan fuera de ventanas protegidas; operaciones de mantenimiento que necesiten bloqueo se prueban antes. El primer riesgo a vigilar sigue siendo el ERP al emitir guía en ventana crítica: acelerar PostgreSQL no elimina el tiempo del emisor ni autoriza salida sin documento.
'''
write('05/partes/5.4_estrategia_de_desempeno/01_desempeno.tex',performance)

references=r'''\section*{Referencias}
\addcontentsline{toc}{section}{Referencias}
Las bases y aclaraciones de Distribuidora Puelche S.A. determinan alcance y umbrales; las fuentes técnicas fundamentan mecanismos concretos de persistencia y archivo. Los nombres de normas expresan los marcos exigidos por las bases, sin atribuir certificación a la propuesta.

Distribuidora Puelche S.A. (2026a). \emph{Bases Administrativas de la licitación TFEP-01/2026}. Formulario T-7, Subdocumento 5; artículos 16, 40 y 85.

Distribuidora Puelche S.A. (2026b). \emph{Bases Técnicas Transversales}. Capítulos 2, 5, 9, 10, 11 y 17.

Distribuidora Puelche S.A. (2026c). \emph{Caso 02: Logística}. Numerales 14, 15, 16.1 y 17.

Distribuidora Puelche S.A. (2026d). \emph{Aclaraciones de la licitación}. Índice obligatorio del capítulo 5, reglas de figuras, anexos y declaración de IA.

LafroX. (2026a). \emph{Subdocumento 4: Arquitectura de la solución}. Rama rama-latex, commit 2799de3, y memoria de cálculo de dimensionamiento.

LafroX. (2026b). \emph{Subdocumento 3: Alcance de la solución y Formulario T-12}. Fuentes Markdown consultadas el 2 de octubre de 2026; versiones y huellas en inventario de fuentes.

PostgreSQL Global Development Group. (s. f.-a). \emph{Transaction isolation}. Documentación oficial. Recuperado el 2 de octubre de 2026, de \url{https://www.postgresql.org/docs/16/transaction-iso.html}

PostgreSQL Global Development Group. (s. f.-b). \emph{Table partitioning}. Documentación oficial. Recuperado el 2 de octubre de 2026, de \url{https://www.postgresql.org/docs/16/ddl-partitioning.html}

Amazon Web Services. (s. f.-a). \emph{Using time to live (TTL) in DynamoDB}. Recuperado el 2 de octubre de 2026, de \url{https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html}

Amazon Web Services. (s. f.-b). \emph{Locking objects with Object Lock}. Recuperado el 2 de octubre de 2026, de \url{https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html}

Amazon Web Services. (s. f.-c). \emph{AWS DMS data validation}. Recuperado el 2 de octubre de 2026, de \url{https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Validating.html}
'''
write('05/partes/90_referencias.tex',references)
ai=r'''\section*{Declaración de uso de IA}
\addcontentsline{toc}{section}{Declaración de uso de IA}
Se utilizó Codex para desarrollar texto, modelo, cálculos reproducibles, código de diagramas y verificaciones documentales. El nivel declarado es alto donde hubo generación sustancial. No existe constancia de revisión humana de esta versión; esa condición se declara expresamente sin atribuir firmas, aprobación ni trabajo de revisión a personas que no lo han realizado. La verificación automática de fuentes y compilación no sustituye revisión profesional ni aceptación del CLIENTE.
'''+table('Uso de IA y estado de revisión','tab:5-ia',['Sección','Herramienta','Finalidad','Nivel texto','Nivel diagramas','Revisión humana'],[(s,'Codex','Modelo, redacción y diagramas' if s in ['5.1','5.2','5.3'] else 'Redacción, cálculo y verificación','Alto','Alto' if s in ['5.1','5.2','5.3'] else 'Ninguno','Sin constancia de revisión humana de esta versión') for s in ['Introducción','5.1','5.2','5.3','5.4','Anexo 5-A','Anexo 5-B','Anexo 5-C','Anexo 5-D','Anexo 5-E','Anexo 5-F','Anexo 5-G','Anexo 5-H','Matriz de apoyo T-12']],[.13,.15,.23,.10,.13])
write('05/partes/91_declaracion_ia.tex',ai)

# Anexos: detalle documental fuera del cuerpo principal.
def annex(code,title,intro,content):
    write('05/anexos/datos/partes/'+code+'_anexo.tex',r'\chapter*{Anexo 5-'+code+' --- '+title+'}'+'\n'+r'\addcontentsline{toc}{chapter}{Anexo 5-'+code+' --- '+title+'}'+'\n'+r'\label{anx:5-'+code+'}'+'\n'+intro+'\n\n'+content)

dictionary=r'''El diccionario es lógico y orientado a diseño; el tamaño físico y las versiones menores se fijan durante implementación y perfilado. Todos los atributos definidos se incluyen en la exportación CSV UTF-8 de apoyo. Las marcas Interno, Personal y Restringido controlan permisos y minimización; no convierten automáticamente todo dato en categoría legal sensible. Cifrado explícito indica almacenamiento por campo protegido; sus restricciones de negocio se comprueban antes del cifrado bajo servicio autorizado.

UUID, creado\_en y version son campos comunes de registros de negocio, repetidos aquí para que cada entidad sea autocontenida. Las entidades de caché tienen identidad por clave. Tipos documentales en series se traducen a esquemas DynamoDB/Parquet equivalentes; la representación PostgreSQL expresa el dominio lógico, no obliga a desplegar telemetría en una tabla SQL.
'''
for e in entities:
    dictionary+='\n\\section*{'+tex(e['nombre'])+'}\n'+tex('Dominio: '+e['dominio']+'. Módulo: '+e['modulo']+'. Propietario: '+e['propietario']+'. '+e['regla'])+'\n'
    dictionary+=table('Atributos de '+e['nombre'],'tab:5-dict-'+e['nombre'],['Atributo y tipo','Valores / validación','Oblig.','Sensibilidad'],[(a['nombre']+'\n'+a['tipo'],a['valores']+('; propietario: '+a['propietario'] if a['propietario']!=e['propietario'] else ''),a['obligatorio'],a['sensibilidad']) for a in e['atributos']],[.29,.34,.10])
annex('A','Diccionario de datos y reglas de integridad','Cada entidad conserva sus restricciones y propietario, y cada atributo su tipo, dominio de valores, obligatoriedad y sensibilidad.',dictionary)

annex('B','Relaciones y propietarios','Las cardinalidades se leen desde la primera entidad hacia la segunda. Las referencias entre contextos son lógicas y se validan por contrato; no se exige una FK física cruzando motores.',table('Dominios de información y propietario','tab:5-dominios',['Dominio / módulo','Motor y emplazamiento','Propietario / autoridad'],[(d[0]+' / '+d[1],d[2],d[3]+'; '+d[4]) for d in domains],[.30,.34])+table('Relaciones del modelo','tab:5-relaciones',['Origen','Destino','Cardinalidad','Regla'],[(a,b,c+' : '+d,rule) for a,b,c,d,rule in relations],[.23,.23,.13]))

scenarios=[
('AC-01 Pedido repetido','M3/inbox','Mismo UUID y hash devuelve resultado; hash distinto aísla','Un pedido y una reserva efectiva'),
('AC-02 Doble reserva','M2 sitio/lote','Bloqueo y comprobación de saldo; segunda solicitud en excepción','Saldo no negativo y razón de rechazo'),
('AC-03 Corte 24 h','M1/M2/M5/M8','Continúa ámbito local; secuencia y outbox durable','Reconciliación CD hasta 2 h tras enlace'),
('AC-04 POD vs cancelación','M6/Operaciones','Conservar ambos hechos; supervisor resuelve antes de cobro/DTE','Ningún hecho sobrescrito'),
('AC-05 Cambio precio','M3/Comercial','Mantener precio mostrado; solicitar aceptación versionada','Sin modificación silenciosa'),
('AC-06 Retorno físico','M8 sitio','Registrar recibido; Calidad y ERP resuelven por separado','Sin doble abono ni stock liberado sin Calidad'),
('AC-07 Excursión térmica','M9/M5','Bloqueo local; liberación motivada por Calidad','Bloqueo antes de 5 s; serie sin duplicados'),
('AC-08 Pago incierto','M7/ACL','Consultar referencia pasarela; conservar estado incierto','Una sola confirmación de cobro'),
('AC-09 DTE timeout','M5/ERP','Consultar misma clave; bloquear salida sin guía de carga vigente','No folio duplicado; AL-DTE-01'),
('AC-10 Gateway redundante','M9/telemetría','Deduplicar sensor/sesión/secuencia; diferencia de valor incidente','Una lectura física en serie consolidada'),
('AC-11 Pérdida sitio y WAN','Infraestructura','Restaurar protección externa ensayada; no promover a ciegas','AL-DR-01; RTO 4 h y RPO 15 min'),
('AC-12 Restore tras supresión','Seguridad','Reaplicar órdenes de borrado antes de exposición','GPS vencido no reaparece en consulta')]
protocol=r'''\section*{Protocolo de aceptación de evento}
El receptor autentica ámbito y versión, comprueba hash e identidad, exige versión anterior o pone el mensaje en espera por hueco, y aplica regla de negocio. Persiste efecto, resultado e historial antes del acuse. El emisor reintenta la misma identidad hasta acuse durable. Las operaciones rechazadas producen un resultado consultable, no desaparecen de la cola sin explicación. Se retiene evidencia del conflicto y su decisión.

\section*{Límites de autoridad}
No se usa replicación multimaestro genérica ni sobrescritura por fecha. Cada agregado de stock tiene sitio custodio y época de autoridad; el traslado físico registra salida y recepción separadas con referencia común. Un consumidor nube consolida movimientos, y DMS conserva una copia Talca de lectura separada. La autoridad se transfiere solo con conciliación y revocación de la anterior.
'''
annex('C','Persistencia y reconciliación','Esta matriz concreta la elección de persistencia y la conducta de cada dominio durante interrupción de comunicación.',table('Persistencia y garantías por dominio','tab:5-cap',['Dominio','Agregado / alcance','Conducta durante partición'],[(d[0],d[5],d[6]) for d in domains],[.29,.34])+protocol+table('Escenarios y resultados de aceptación','tab:5-escenarios',['Escenario','Autoridad','Resolución','Criterio'],scenarios,[.22,.17,.31]))

maps=[('ERP clientes/proveedores','cliente/proveedor','Normalizar RUT; UUID estable; fusionar solo con aprobación','Comercial/Abastecimiento'),('ERP productos','producto','Código SKU, GTIN por presentación, unidad y conversión','Abastecimiento/Calidad'),('ERP ventas/pedidos 3 años','pedido/linea_pedido','Conservar importe exacto, fecha y tarifa conocida; marcar desconocida como dato histórico, no valor inventado','Comercial'),('WMS Talca 2013','recepcion/lote/movimiento','2 años movimientos; 5 años sanitario; mapear ubicación y lote','Bodega/Calidad'),('Planillas Concepción','movimiento_stock','Saldo inicial conciliado; inventario físico y diferencias aprobadas','Bodega'),('Planillas rutas 11 hojas','viaje/parada/restricciones','Extraer reglas, ventanas y decisiones con planificador','Planificación'),('ERP CxC','saldo_credito y archivo de movimientos','Saldos vivos + 2 años; explicar balance de apertura','Tesorería'),('Cuadernos/planillas sanitarios','archivo + lote cuando verificable','Digitalización controlada; doble verificación; reportar ausencia de lote','Calidad'),('ERP XML / POD existente','objeto_documental/acuse/evidencia','Huella, referencia, tipo y retención; inventariar disponibilidad','Tributación/Operaciones'),('Temperatura/GPS históricos','series o archivo de consulta','Zona horaria y calidad; no extrapolar lecturas inexistentes','Calidad/Flota')]
templates=r'''\section*{Protocolo de actas de ensayo}
Cada acta tendrá identificador ENS-1 o ENS-2, fecha, responsables, ambientes, extractos y hashes, versiones de reglas/código, inicio y fin por fase, recuentos, sumas y diferencias por familia, tiempos de corte y reversión, pruebas funcionales y decisión firmada. No se rellenan resultados anticipadamente. ENS-1 recorre toda la migración y retorno al legado; ENS-2 añade delta y arranque de operación.

\section*{Defectos y umbrales}
RUT inválido, duplicado de clave, lote ausente, cantidades incompatibles, saldo financiero discordante y objeto sin huella son defectos bloqueantes para el conjunto afectado. Se permite cargar el resto si sus agregados están completos y el CLIENTE conoce la cobertura. Cada diferencia autorizada conserva razón y evidencia; aprobación no habilita despacho de producto no trazable ni omite una obligación tributaria.

\section*{Secuencia de corte y reversión}
Antes del corte: copia verificada, ensayo de restauración, lista de dispositivos y colas sin sincronizar, inventario de fuentes y delta congelado. Durante el corte: impedir doble escritura, aplicar delta por orden de dependencia, conciliar y probar recepción, FEFO, preparación, guía, POD y rendición. Apertura requiere lista completa y decisión de Operaciones, Calidad y Tesorería. Ante reversión posterior a apertura, exportar eventos nuevos, resolver su correspondencia y reingresarlos o compensarlos en origen antes de reabrir. Conservación del original permite investigar sin alterar evidencia.
'''
annex('D','Migración, saneamiento y conciliación','El mapeo identifica sistema de origen, conjunto de destino, transformación y autoridad para defectos; las fechas finales se incorporan al cronograma de implantación.',table('Mapeo de fuentes','tab:5-mapeo',['Origen','Destino','Reglas','Responsable'],maps,[.21,.23,.34])+templates)

# Memoria cuantitativa reproducible: GB decimal, GiB binario por separado.
monthly_events=260000*5+260000*2+31000*5
monthly_movements=260000+14500+3400+1150
oltp=(monthly_events*1000+monthly_movements*500)*2*12
pod_kb=30+200*(1+900/31000)
pod=31000*12*pod_kb*1000
temp=(6048+4536)*145*365
gps=22075200*145
mig_kb=34180+10476000+3348600+1380000+816000
calculations=dict(unidades={'GB':'10^9 bytes','GiB':'2^30 bytes','KB_fuente':'1000 bytes para mantener GB de arquitectura'},oltp_bytes_anual=oltp,pod_bytes_anual=pod,temperatura_raw_bytes_anual=temp,temperatura_curada_bytes_anual=temp*.25,gps_raw_bytes_anual=gps,gps_curado_bytes_anual=gps*.25,migracion_bytes_destino=mig_kb*1000*2,migracion_gib_destino=mig_kb*1000*2/2**30,migracion_sensibilidad_gb=[(mig_kb-690000)*2/1e6,(mig_kb+690000)*2/1e6],escenarios={'pod_seis_anos_constante_gb':pod*6/1e9,'pod_seis_anos_crecimiento_lineal_gb':pod*(1+1.16+1.32+1.48+1.64+1.8)/1e9,'pod_aumento_duplicado_imagenes_gb_anual':(30+400*(1+900/31000))*31000*12/1e6})
write('05/anexos/datos/fuentes/CALCULOS.json',json.dumps(calculations,ensure_ascii=False,indent=2))
queries=[('Q1 Stock/FEFO','sitio,lote,ubicación; lote(producto,vence)','Reserva serializada; copia indicativa no confirma','<=2 s consulta stock/crédito'),('Q2 Confirmación línea','mision,id; asignacion,reserva','Transacción corta; evento único','<=1 s'),('Q3 Pedido preventa','pedido(cliente,capturado_en,id); línea(pedido,numero)','Paginación por clave; validación precio','<=1,5 s por línea'),('Q4 Entrega/POD','entrega(pedido,ocurrido_en); detalle(asignacion)','Metadatos separados de carga de objeto; hash verificado','<=2 s registro'),('Q5 Retiro sanitario','lote(producto,lote_proveedor); asignacion(lote); detalle(asignacion)','Cruce cliente de destino; no escaneo completo de fotos','Medir contra RF/RNF del retiro del caso'),('Q6 Ruta/geocerca','GiST punto; viaje(fecha,sitio)','SQL parametrizado y versión de ruta','Medir carga espacial en QA'),('Q7 Outbox/inbox','Pendientes por estado/creado_en; identidad global event_id','Partición fecha + registro global identidad','Backlog CD <=2 h; terminal <=10 min'),('Q8 Serie térmica','sensor,fecha; Parquet por fecha/sitio','Deduplicar muestra y separar histórico','Indicador del día <=5 min'),('Q9 Analítica','hecho por fecha/sitio; dimensiones por clave','Redshift; sin consulta de tablero al OLTP','Gestión <=4 h; cierre <=2 h')]
calc_text=r'''\section*{Derivaciones y sensibilidad}
Se usa GB decimal para los resultados de arquitectura. El tamaño de origen comercial es una KB por fila y el de movimiento 0,5 KB; se aplica factor dos por índices y sobrecarga. El tamaño real se medirá mediante perfilado, considerando cifrado, JSON de auditoría y WAL, que pueden exceder esa cota.

Transaccional anual: $[(260.000\times5+260.000\times2+31.000\times5)\times1.000+279.050\times500]\times2\times12 = 50.748.600.000$ bytes. Son 50,75 GB y 304,49 GB a seis años constantes. El factor dos ya está incluido; no se vuelve a aplicar a cada dominio.

POD: $30+200\times(1+900/31.000)=235,806$ KB por entrega; $31.000\times12\times235,806\times1.000=87,72$ GB/año. Seis años constantes dan 526,32 GB aproximadamente. Como sensibilidad de crecimiento lineal de 16\% por año, factores 1; 1,16; 1,32; 1,48; 1,64; 1,80 suman 8,4 años equivalentes y producen 736,85 GB. Esa extrapolación más allá del año 3 es supuesto adicional, no proyección entregada por el CLIENTE. Duplicar tamaño de fotografía eleva la generación a 164,28 GB/año y debe recalcularse antes de comprometer espacio.

Temperatura: $(6.048+4.536)\times145\times365=560.158.200$ bytes/año raw. Compresión 0,25: 0,1400 GB/año y 0,7002 GB a cinco años. Raw 30 días: 0,0460 GB, sin sobrecarga DynamoDB. No se duplica el volumen porque dos gateways leen las cámaras de Talca.

GPS: $22.075.200\times145=3.200.904.000$ bytes/año raw y 0,8002 GB curados con factor 0,25. Se conserva doce meses; cifrado y esquema real se medirán antes de aplicar esa compresión.

Migración: $34.180+10.476.000+3.348.600+1.380.000+816.000=16.054.780$ KB; por dos da 32,10956 GB. La sensibilidad de trazabilidad de 10 a 30 KB por recepción varía 690.000 KB a cada lado, resultando 30,72956--33,48956 GB de destino. Las 1 KB por fila, saldos vivos y fuentes documentales adicionales se verifican mediante inventario. El valor binario correcto para 32,10956 GB decimales es 29,9044 GiB; no 30,62 GiB, que surgiría de tratar las KB de origen como KiB. Esta distinción se aplica a todo el presupuesto.

El total de contenido retenido transaccional, POD, temperatura curada y GPS curado a volumen constante es aproximadamente 832,31 GB. Es una suma de clases sin superponer la copia raw ni migración ya incluida en la historia; no es el tamaño final de infraestructura. Para reserva propuesta de 20\% libre se divide entre 0,8, y se agregan separadamente respaldo, réplica, WAL, staging, metadatos y crecimiento después del perfilado. Arquitectura mantiene su dimensionamiento on-premise; cualquier desviación se eleva con fórmula y evidencia.
'''
annex('E','Desempeño y memoria de capacidad','Las estimaciones se entregan con fórmulas y unidades. CALCULOS.json conserva sus resultados sin redondeo; no son mediciones de producción.',calc_text+table('Consultas representativas y candidato de acceso','tab:5-consultas',['Consulta','Acceso propuesto','Control','Umbral'],queries,[.18,.28,.31]))

indicators=[('OTIF','Pedido comprometido','100 × pedidos completos y a tiempo / pedidos comprometidos','Ventana y cantidades de M3/M6; período, sitio, canal, zona'),('Fill rate','Línea y unidad base','100 × unidades aceptadas / unidades comprometidas','Asignación y detalle M5/M6; SKU, sitio, período'),('Perfect order','Pedido','100 × pedidos OTIF sin daño y con documentos válidos / comprometidos','M3/M5/M6/ERP; causal, cliente, canal'),('Faltantes','Línea','Suma max(comprometido - aceptado,0) en unidad base','M3/M5/M6; producto, lote, sitio'),('Devoluciones','Cantidad por causal','100 × cantidad devuelta / cantidad despachada, misma unidad','M8/M5; período, producto, causal'),('Merma vencimiento','Valor inventario','100 × valor descartado por vencimiento / valor medio inventario','M2/M9/ERP; valor medio diario, sitio, SKU'),('Diferencia rendición','Viaje/conductor','Efectivo recibido - esperado; absolutos y causales por separado','M7; Tesorería accede a detalle cifrado'),('Saldo envases','Cliente/tipo','Suma cargos - retornos aceptados; disputas separadas','M8; cliente, tipo, período'),('Excursión térmica','Sensor/evento','Conteo y duración de intervalos fuera de rango aprobado','M9; sensor, lote, sitio; no inferir continuidad en huecos'),('Costo por entrega','Entrega','Costo operativo asignado / entregas del período; intentos fallidos visibles','ERP + M4/M6/M8; km, tiempo, capacidad; pesos aprobados'),('Costo de servir','Cliente/canal','Ruta + atención + retornos + custodia asignados sin doble reparto','ERP/M4/M7/M8; reconciliar total de costos de origen')]
semantic=r'''\section*{Esquema dimensional y frescura}
dim\_fecha tiene día, semana, mes, temporada y zona horaria; dim\_sitio código y tipo; dim\_producto SKU, GTIN, familia y condición térmica; dim\_cliente canal y zona con intervalos SCD2; dim\_ruta viaje y versión; dim\_causal vocabulario gobernado. Cada dimensión usa clave sustituta, referencia canónica, versión y vigencia; dimensión no conocida usa clave de excepción y se regulariza preservando el hecho.

hecho\_pedido: una línea/version, cantidad comprometida y fecha de promesa; hecho\_entrega: un intento, cantidades y fuente; hecho\_movimiento: un delta de stock; hecho\_temperatura: una muestra válida; hecho\_rendicion: un cierre con importes protegidos. Todos incluyen source\_event\_id, dataset de origen, lote ETL, transformation\_version, occurred\_at y visible\_at. En Parquet el manifiesto vincula rango de claves, filas, hash y esquema.

Las fichas de indicadores excluyen denominador cero, mostrándolo como sin población. Un pedido cancelado antes del compromiso solo se excluye con causal autorizada y publicada; cancelarlo después no mejora artificialmente OTIF. No se suman múltiples intentos como nuevos pedidos. Las metas de negocio se conservan del caso y se acuerda su definición operacional antes de marcha blanca.

El tablero muestra fecha de última transacción por sitio, cobertura, marca de agua y diferencia occurred\_at--visible\_at. Objetivos: diarios <=5 minutos, cierre <=2 horas tras último camión, gestión <=4 horas. La prueba incluye hechos tardíos de 24 h; se mide latencia total y recuperación, diferenciando retraso de conectividad. Catálogo y linaje se actualizan por ejecución y se prueban navegando del indicador al registro y extracto de origen.
'''
annex('F','Modelo analítico, indicadores y linaje','Las fórmulas usan una misma granularidad y sus dimensiones permiten investigar la causa del resultado sin convertir datos personales en acceso general.',semantic+table('Fichas de indicadores','tab:5-kpi',['Indicador','Grano','Fórmula','Origen / dimensiones'],indicators,[.18,.16,.32]))

retention=[('DTE/XML/acuses','6 años desde emisión/cierre','S3 y manifiesto; ERP mantiene su responsabilidad','Tributación; legal hold por expediente'),('POD/firma/foto','6 años desde entrega','S3 versionado; metadatos/linaje','Operaciones; expurgo de todas versiones'),('Lote/custodia sanitaria','Mayor de 5 años o vida útil + 6 meses','Histórico protegido; local stock vigente + 4 meses movimientos','Calidad; bloquear purga si retiro abierto'),('Temperatura consolidada','5 años desde lectura','Parquet/Redshift; raw 30 días tras verificación','Calidad; verificar copia antes de TTL'),('GPS personal','12 meses desde lectura','Campo cifrado; datasets y respaldos controlados','Flota/Seguridad; no Object Lock de 6 años'),('Ventas/pedidos','Migrar 3 años; conservar 6 años como propuesta de negocio','OLTP activo/archivo; respetar documentos vinculados','Comercial valida plazo propuesto'),('Inventario no sanitario','Migrar 2 años; 6 años propuestos para auditoría de negocio','Local 4 meses; archivo nube','Bodega valida plazo; sanitario prevalece'),('CxC y cobros','Saldos vivos + 2 años migrados; 6 años propuestos','ERP/Aurora y archivo cifrado','Tesorería; saldo abierto no se purga'),('Identidad y vínculo','Vigencia + retención de actos vinculados; minimizar atributos','Keycloak/ref. histórica; manif. TTL 24 h','Seguridad; no prolongar autorización de turno'),('Outbox/inbox','Resultado al menos 30 días; evidencia según registro','Contexto/archivo; no purgar sin acuse','Plataforma; antiguos aislados'),('Logs técnicos','12 meses línea + 24 meses archivo','CloudWatch/archivo inmutable','Seguridad; auditoría de negocio plazo propio'),('Caché/móvil','TTL central por categoría; turno y cola hasta acuse','Redis/Room cifrado','Plataforma; borrado remoto y certificado'),('Notificaciones','12 meses propuestos; actos relevantes se archivan con negocio','Estado y acuse; contenido mínimo','Comercial valida plazo por finalidad'),('EDI','6 años para vínculo comercial/tributario propuesto','S3 original/transformación; metadatos','Comercial/Tributación; aplicar categoría mayor'),('Staging migración','90 días tras aceptación, salvo expediente requerido','Extractos cifrados; acceso restringido','Migración/CLIENTE; certificado al expirar')]
quality=[('Completitud','100 × atributos obligatorios informados / obligatorios esperados','100% en conjunto liberado','Dueño del dominio; cuarentena'),('Exactitud identidad','100 × RUT/GTIN válidos / identificadores evaluados','100% de registros liberados','Comercial/Abastecimiento; cotejo fuente'),('Consistencia saldo','Saldo origen - saldo destino, por cuenta/sitio/lote','0 diferencia no explicada','Tesorería/Bodega; conciliación completa'),('Unicidad','Número de claves de negocio repetidas sin equivalencia autorizada','0 en conjunto liberado','Dueño del maestro; fusión documentada'),('Integridad documental','Objetos con hash correcto / objetos liberados','100%','Operaciones/Tributación; aislar corruptos'),('Frescura operacional','visible_en - ocurrido_en','<=5 min con origen accesible; registrar totalidad','Control de gestión/Plataforma'),('Cobertura sanitaria','Movimientos identificados a lote/SSCC / movimientos sanitarios','100% de nuevo flujo; defectos históricos explicados','Calidad; no fabricar lotes')]
governance=r'''\section*{Responsabilidades y controles de ciclo de vida}
Los propietarios del Anexo 5-B aceptan reglas de calidad y permisos. Seguridad administra acceso, claves y respuesta a incidente; Plataforma ejecuta particiones, respaldos y borrado; el CLIENTE decide finalidades, subencargados, transferencias y excepciones legales. El certificado de eliminación registra categorías, orden, hashes, versiones, ejecutor, verificador y excepciones con fecha de próxima revisión.

Política de respaldo propuesta para cerrar el diseño: copias operacionales diarias con ventana de 35 días cuando el servicio lo admite, coherente con PITR de Aurora; archivo documental conserva su plazo propio y no depende de backups diarios. Las políticas efectivas on-premise y recuperación deben cotejarse y probarse contra 4.2 antes de liberación. Un GPS vencido puede persistir hasta expirar un backup de 35 días, sin consulta ni restauración abierta; una supresión se reaplica antes de exposición. La prueba de borrado recorre tablas, archivos Parquet, índices, todas las versiones S3, dispositivos y caché.

Para exportar, el CLIENTE define ámbito y obtiene paquete con datasets, diccionario, relaciones, archivos originales y manifiesto; recuentos y huellas verifican cobertura. En datos particionados se fija snapshot/marca de agua y se informa fecha por fuente. Credenciales de exportación tienen expiración y registro de descargas. No se incluyen secretos ni material privado de claves en la portabilidad de datos.
'''
annex('G','Calidad, clasificación y ciclo de vida','Se distinguen plazos exigidos por el caso y parámetros propuestos por LafroX; los segundos se formalizan con el dueño de negocio antes de producción.',table('Políticas por categoría','tab:5-retencion',['Categoría','Plazo / base','Representaciones','Responsable / control'],retention,[.20,.26,.28])+table('Calidad y metas de diseño','tab:5-calidad',['Dimensión','Medición','Criterio','Responsable'],quality,[.18,.36,.20])+governance)

requirements=[
('01','Obligatorio','Modelo y diccionario','5.1','5-A/B','VD-01; diccionario completo y DER','Diseñado'),('02','Obligatorio','Motor, paradigma y CAP','5.2.1–2','5-C','AC-02/03; autoridad por agregado','Diseñado'),('03','Obligatorio','Auditoría de operación','5.2.5','5-A/G','AC-01/04; antes/después y autor','Diseñado'),('04','Obligatorio','Calidad de datos','5.2.5','5-G','VD-03; tablero y cuarentena','Diseñado'),('05','Obligatorio','Separación OLTP/OLAP','5.2.4; 5.4','5-E/F','VD-04; carga sin degradación OLTP','Diseñado'),('06','Obligatorio','Exportación completa','5.2.6','5-G','VD-05; recuentos y hashes','Diseñado'),('07','Obligatorio','Retención y eliminación','5.2.6','5-G','AC-12; expiración por categoría','Diseñado'),('08','Obligatorio','Datos personales','5.2.5','5-A/G','VD-06; ACL/cifrado campo','Diseñado; acuerdo Art.85 requerido'),('09','Obligatorio','Datos maestros','5.1.1','5-B/D','VD-03; no claves duplicadas','Diseñado'),('10','Deseable','Catálogo y linaje automático','5.2.4','5-F','VD-07; indicador hasta origen','Propuesto'),('11','Obligatorio','Plan de migración','5.3','5-D/E','ENS-1/2; cobertura y reversión','Diseñado'),('12','Obligatorio','Perfilado y saneamiento','5.3.2','5-D','VD-03; reporte de defectos','Procedimiento definido'),('13','Obligatorio','Dos ensayos completos','5.3.3','5-D','ENS-1/2 con actas y tiempos','Programado en implantación; no ejecutado'),('14','Obligatorio','Conciliación verificable','5.3.3','5-D','ENS-1/2; cero diferencia inexplicada','Criterios definidos'),('15','Según caso','Históricos no migrados y alcance del caso','5.3.1/4','5-D/G','VD-05; archivo accesible durante retención','Diseñado; códigos cotejados por materia'),('16','Obligatorio','OpenAPI/AsyncAPI','5.2.3','5-C/H; referencia 4.1-G/H','VD-08; generación/validación CI','Diseño; contratos ejecutables por implementar'),('17','Obligatorio','Versionado y preaviso','5.2.3','5-C','VD-08; coexistencia y 6 meses','Diseñado'),('18','Obligatorio','OAuth 2.1 / mTLS','5.2.3','5-C/G','VD-06; intercambio autenticado','Diseñado'),('19','Obligatorio','Correlación entrada/salida','5.2.1/3','5-A/C','AC-01; transaction_id común','Diseñado'),('20','Obligatorio','ACL frente al legado','5.1.1; 5.2.3','5-C/D','AC-09; mismo folio tras timeout','Diseñado'),('21','Obligatorio','Modo, volumen y falla de interfaces','5.2.3; 5.4.1','5-C/E; referencia 4.1-G/H/I','VD-08; 15 INT y pruebas de terceros','Hereda catálogo de arquitectura'),('22','Obligatorio','Carga masiva y errores por registro','5.2.3; 5.3.2','5-D','VD-03; parcialidad por agregado íntegro','Diseñado'),('23','Según caso','GS1, EDI y formato tributario','5.1.2/3; 5.2.3','5-A/C','VD-08; validación de perfiles','Diseñado; perfiles de cadenas requeridos'),('24','Deseable','Portal de desarrolladores','5.2.3','5-H','VD-08; sandbox y credenciales expirables','Propuesto; no desplegado'),('25','Obligatorio','Tableros del caso','5.2.4','5-F','VD-07; fórmulas y fuentes','Diseñado'),('26','Obligatorio','Filtros y profundización','5.2.4','5-F','VD-07; ámbito por rol y grano','Diseñado'),('27','Obligatorio','Autoservicio del CLIENTE','5.2.4','5-F/G','VD-07; informe creado por rol CLIENTE','Diseñado'),('28','Obligatorio','Exportar/programar informes','5.2.4','5-F/G','VD-05/07; CSV/JSON/calendario','Diseñado'),('29','Según caso','Latencia analítica','5.2.4','5-F/H','VD-04; 5 min / 2 h / 4 h','Exigencia conservada; aislamiento requiere ensayo'),('30','Deseable','Analítica predictiva','5.2.4','5-H','Coherencia de alcance con arquitectura','No incorporada; explotación descriptiva')]
with (BASE/'formularios/trazabilidad/MATRIZ_RT05.csv').open('w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f);w.writerow(['requisito','caracter','materia','seccion','anexo','evidencia_prevista','estado'])
    for no,*row in requirements:w.writerow(['RT-05.'+no]+row)
decisions=[('DD-01 Índice','Adoptar cuatro títulos de aclaraciones; analítica/gobierno dentro de 5.2','Aclaraciones cap.5','Resuelve estructura del plan anterior'),('DD-02 Stock','Autoridad M2 por sitio/lote; nube no confirma con proyección','4.1 reconciliación/INT-12','Conserva autonomía y evita doble reserva'),('DD-03 CDC','DMS Talca a esquema lectura separado de eventos','4.1 catálogo INT-12','Sin replicación bidireccional genérica'),('DD-04 Retorno M8','Recepción local distinta de liberación y abono','Commit 2799de3','Propaga último ajuste al modelo'),('DD-05 Thermal','Clave sensor/sesión/secuencia independiente de gateway','3 gateways de arquitectura','Deduplica dos lectores Talca'),('DD-06 Unidades','KB/GB decimales para memoria; GiB calculado aparte','Memoria de dimensionamiento','Evita ambigüedad de factor 1000/1024'),('DD-07 Historia','Retención del caso y migración por materia, no por código aislado','Caso cap.15/BTT cap.5','RT-05.10/15 desajustados se anotan'),('DD-08 Auditoría','Plazo de negocio sigue dato; log técnico plazo distinto','RT-05.03 y arquitectura','No reducir DTE/POD a 36 meses'),('DD-09 Analítica','Microcarga y marcas de agua; sin IA predictiva','4.1 y Caso RT-05.29','No prometer frescura global sin enlace'),('DD-10 Privacidad','Autorización Art.85 para regiones y subencargados','4.2 región/BA Art.85','Sin aprobación implícita del CLIENTE')]
pending=[('PD-01','Disponibilidad y tamaño real de extractos/históricos','Inventario y perfilado con dueños ERP/WMS/Calidad','Antes ENS-1'),('PD-02','Procedimiento tributario de contingencia AL-DTE-01','Operaciones/Tributación; ensayo 96 salidas','Antes producción de despacho'),('PD-03','Protección externa con sitio/WAN perdidos AL-DR-01','Infraestructura; ensayo RPO/RTO','Antes aceptación continuidad'),('PD-04','Frescura 5 minutos bajo aislamiento','CLIENTE/Operaciones; visibilidad local y global ensayada','Antes marcha blanca M10'),('PD-05','Fecha/mes de olas y corte','Implantación; dependencia del cronograma Subdoc-7','Antes ENS-2'),('PD-06','Políticas comerciales y maestro compartido','Comercial/Tesorería; precio, reservas, crédito y OTIF','Antes liberación funcional'),('PD-07','Acuerdo datos personales y regiones','CLIENTE/Seguridad; Art.85 y subencargados','Antes tratamiento real'),('PD-08','Revisión humana de contenido y aceptación de diseño','Responsables del proyecto; constancia identificable','Antes presentación final'),('PD-09','Tamaños de auditoría/cifrado y retención local efectiva','Plataforma; perfilado frente capacidad 4.2','Antes prueba de carga'),('PD-10','Implementación física de hechos y dimensiones','M10; contrato analítico desde modelo propuesto','Durante implementación; antes autoservicio')]
acceptances=[('VD-01','Modelo/diccionario','Todos los atributos tienen seis propiedades; relaciones referidas existen','Diseño verificado automáticamente'),('VD-02','Reconexión','Escenarios AC-01–12; cero efecto repetido; stock conciliado','Ensayo previsto'),('VD-03','Calidad/migración','Conjunto liberado sin huérfanos; diferencias explicadas','ENS-1/ENS-2 previstos'),('VD-04','Carga/analítica','21,99 solicitudes/s y umbrales caso; lag end-to-end visible','Ensayo previsto'),('VD-05','Exportación/eliminación','Paquete completo/hashes; ninguna versión expuesta después de supresión','Ensayo previsto'),('VD-06','Seguridad','Mínimo privilegio, cifrado, consulta sensible y revocación','Ensayo previsto'),('VD-07','BI','Filtros, fórmula, drill-down, autoservicio y calendario','Ensayo previsto'),('VD-08','Contratos','Compatibilidad esquemas, rechazo de credencial inválida y perfiles GS1/EDI','Implementación/ensayo previstos')]
htext=r'''\section*{Correspondencia y condiciones de cierre}
La matriz es una contribución documental al T-12 vigente del Subdocumento 3. Conserva IDs RT sin declarar cumplimiento implementado. RT-05.10 transversal trata catálogo/linaje; el caso usa ese código para retención. RT-05.15 transversal trata consulta de históricos no migrados; el caso lo usa para alcance de migración. Se satisfacen ambas materias en filas y referencias separadas por fuente.

Las pruebas y decisiones de la siguiente matriz son criterios de implantación. Actas, responsables nominados y fechas se incorporan cuando se ejecuten; este documento no simula su firma. Las condiciones de continuidad tributaria, pérdida de sitio y frescura bajo aislamiento conservan los requisitos exigidos y se resuelven por evidencia y acuerdo identificable, no por compilación del PDF.
'''
annex('H','Trazabilidad, decisiones y aceptación','Las decisiones del diseño, los criterios de prueba y las dependencias se mantienen separados para poder revisar cada conclusión con su fuente.',htext+table('Cobertura RT-05','tab:5-rt',['Requisito / carácter','Materia / sección','Evidencia / estado'],[('RT-05.'+no+' / '+ch,ma+'; '+se+'; '+an,ev+'; '+st) for no,ch,ma,se,an,ev,st in requirements],[.22,.34])+table('Decisiones de datos','tab:5-adr',['Decisión','Regla','Fuente','Efecto'],decisions,[.19,.35,.21])+table('Dependencias y validación','tab:5-pend',['ID','Materia','Responsable / evidencia','Hito'],pending,[.09,.29,.36])+table('Criterios de verificación','tab:5-acept',['ID','Recorrido','Criterio','Estado'],acceptances,[.10,.19,.45]))

for folder,filename in [('5.1_modelo','01_modelo.tex'),('5.2_gestion_de_datos','01_gestion.tex'),('5.3_estrategia_de_migracion','01_migracion.tex'),('5.4_estrategia_de_desempeno','01_desempeno.tex')]:
    write('05/partes/'+folder+'/contenido.tex',r'\input{05/partes/'+folder+'/'+filename+'}')
write('contenido_subdocumento_5.tex','\n'.join(r'\input{'+p+'}' for p in ['05/partes/00_introduccion.tex']+['05/partes/'+folder+'/contenido.tex' for folder in ['5.1_modelo','5.2_gestion_de_datos','5.3_estrategia_de_migracion','5.4_estrategia_de_desempeno']]+['05/partes/90_referencias.tex','05/partes/91_declaracion_ia.tex']))
write('05/anexos/datos/contenido.tex','\n'.join(r'\input{05/anexos/datos/partes/'+c+'_anexo.tex}' for c in 'ABCDEFGH')+'\n'+r'\input{05/partes/90_referencias.tex}'+'\n'+r'\input{05/partes/91_declaracion_ia.tex}')

preamble=r'''% !TeX program = lualatex
\makeatletter
\def\input@path{{00/plantilla/fisica/}}
\makeatother
\documentclass[carta,firma]{lafrox}
\usepackage{etoolbox}
\captionsetup{hypcap=false}
\setcounter{tocdepth}{2}
\setcounter{secnumdepth}{2}
% Índice detallado compacto: conserva tamaño y títulos de la plantilla.
\titlecontents{chapter}[0pt]
  {\addvspace{7pt}\intersemibold\color{lafroxTinta}}
  {\textcolor{lafroxFuerte}{\thecontentslabel}\enspace}{}
  {\normalfont\color{lafroxGris}\hfill\contentspage}
\titlecontents{section}[1.5em]
  {\addvspace{1pt}\fontsize{10pt}{12pt}\selectfont\color{lafroxTinta}}
  {\textcolor{lafroxGris}{\thecontentslabel}\enspace}{}
  {\normalfont\color{lafroxGris}\hfill\contentspage}
\titlecontents{subsection}[3.4em]
  {\fontsize{9.5pt}{11pt}\selectfont\color{lafroxGris}}
  {\thecontentslabel\enspace}{}
  {\hfill\contentspage}
\newcommand{\datosdocumentocinco}[2]{
\datoslafrox{documento={Propuesta Técnica},subtitulo={#1},alcance={Modelo y gestión de datos},formulario={Formulario T-7},fecha={02 de octubre de 2026},version={1.0},nomenclatura={#2}}
\hypersetup{pdftitle={#1}}
\renewcommand{\LFXestadodoc}{Propuesta de diseño}
\patchcmd{\portadalafrox}{\LFXcampoportada{Versión}{\LFXversion}}{\LFXcampoportada{Documento}{5}}{}{}
}
'''
write('05/preambulo.tex',preamble)
write('main_subdocumento_5.tex',r'''\input{05/preambulo.tex}
\datosdocumentocinco{Subdocumento 5 --- Modelo y gestión de datos}{LAFROX-Subdocumento5.pdf}
\begin{document}
\portadalafrox
\indicelafrox
\setcounter{chapter}{4}
\input{contenido_subdocumento_5.tex}
\end{document}''')
write('05/anexos_datos.tex',r'''% Compilar desde la raíz del repositorio.
\input{05/preambulo.tex}
\datosdocumentocinco{Subdocumento 5 --- Anexos}{LAFROX-Subdocumento5-Anexos.pdf}
\begin{document}
\portadalafrox
\indicelafrox
\renewcommand{\thetable}{5A.\arabic{table}}
\input{05/anexos/datos/contenido.tex}
\end{document}''')

# Corregir los redondeos/unidades en el cuerpo usando los resultados calculados.
p=BASE/'partes/5.3_estrategia_de_migracion/01_migracion.tex'
s=p.read_text(encoding='utf-8').replace('con KB binarios: GB = KB/1.048.576','con KB y GB decimales: GB = KB/1.000.000').replace('30,62 GiB (32,11 GB decimales)','32,11 GB (29,90 GiB)')
s=s.replace('mientras el cálculo binario da 30,62 GiB','mientras la conversión binaria de los mismos bytes da 29,90 GiB')
p.write_text(s,encoding='utf-8')
p=BASE/'partes/5.4_estrategia_de_desempeno/01_desempeno.tex'
p.write_text(p.read_text(encoding='utf-8').replace('526,34','526,32'),encoding='utf-8')
print(json.dumps({'entidades':len(entities),'atributos':sum(len(e['atributos']) for e in entities),'relaciones':len(relations),'dominios':len(domains),'requisitos':len(requirements),'fuentes':len(sources)},ensure_ascii=False))
