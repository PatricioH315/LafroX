"""Estimación ascendente de los 15 módulos del T-15 (09-11-2026).

Cada módulo se descompone en elementos de alcance del T-12 (requisitos del SD3,
rama CORRIGIENDO, columna «Paquete EDT»). Cada funcionalidad compartida por varios
módulos se cuenta una sola vez, en el módulo que la implementa; en los demás
aparece como punto de integración interna y no suma un flujo.

Tasas (M, HH) — supuestos de planificación por juicio de ingeniería del equipo,
declarados en el T-15; se contrastan con las HH medidas por iteración (sección 4):
  flujo S (consulta o registro sin reglas)                       24
  flujo M (registro con validaciones, estados o notificaciones)   48
  flujo C (cálculo, optimización, conciliación o motor de reglas) 96
  interfaz externa (contrato, adaptador, cola, reintento, idempotencia) 64
  dispositivo (integración con equipo físico y pruebas con el equipo)    64
  operación sin conexión (cola local, sincronización, duplicados)       120
  objetivo de rendimiento medible (prueba y ajuste del flujo)            24
  otra necesidad especial (seguridad, accesibilidad, tiempo real, etc.)   48
Actividades del módulo:
  análisis y diseño específico = 8 HH por flujo + 8 HH por interfaz o dispositivo
  construcción                 = suma de los elementos
  pruebas unitarias y contrato = 25 % de la construcción (cobertura mínima RT-04.11)
  integración y entrega en QA  = 40 HH + 16 HH por interfaz o dispositivo
  revisión de iteraciones      = 12 HH por iteración de dos semanas (Tabla de iteraciones)
"""
import json, math, sys
from pathlib import Path

RATE = {'S': 24, 'M': 48, 'C': 96, 'I': 64, 'D': 64, 'OFF': 120, 'REN': 24, 'ESP': 48}

# (paquete, nombre, iteraciones, elementos, (O_factor, motivo O), (P_factor, motivo P))
MODS = [
 ('3.4.1', 'M1 Recepción', 5, [
   ('M', 'Recepción contra OC con alerta por discrepancia', 'RF-01.01'),
   ('M', 'Captura de lote y vencimiento por GS1', 'RF-01.02, RF-01.03, RF-01.06'),
   ('M', 'No conformidad con fotografía y cuarentena', 'RF-01.04, RF-01.05'),
   ('M', 'Generación de SSCC y etiqueta GS1-128', 'RF-01.07'),
   ('S', 'Ubicación del SSCC con validación térmica', 'RF-01.08'),
   ('M', 'Maestro de productos', 'RF-01.10'),
   ('I', 'Ingreso de inventario al ERP con cola y reintento', 'RF-01.09'),
   ('D', 'Impresora de etiquetas', 'RF-01.07'),
   ('OFF', 'Operación sin conexión en bodega', 'RT-17.01'),
   ('REN', 'Registro de ítem dentro del tiempo exigido', 'RNF-01.01')],
  (0.85, 'reutiliza identidad, auditoría y sincronización de la base compartida (3.3)'),
  (1.25, 'variantes de etiquetas GS1 de proveedores y ajustes con la impresora en el piloto')),
 ('3.4.2', 'M2 Inventario', 5, [
   ('M', 'Instalaciones, zonas y ubicaciones', 'RF-02.01'),
   ('M', 'Stock consolidado y disponible para venta', 'RF-02.02, RF-02.05'),
   ('C', 'Propuesta de slotting por rotación ABC', 'RF-02.03'),
   ('M', 'Conteo cíclico y ajuste', 'RF-02.04'),
   ('M', 'Inventario en tránsito entre sitios', 'RF-02.06'),
   ('S', 'Ocupación por zona', 'RF-02.07'),
   ('M', 'Control FEFO y alertas de vencimiento', 'RF-02.09'),
   ('M', 'Lecturas en cross-docking', 'RF-02.11'),
   ('S', 'Validación térmica en reubicación', 'RF-01.11'),
   ('S', 'Mermas por vencimiento', 'RF-08.05'),
   ('C', 'Reposición sugerida con promociones', 'RF-10.01, RF-10.02'),
   ('I', 'Traspaso de reposición y transferencias al ERP', 'RF-10.03, RF-02.06')],
  (0.85, 'reutiliza el modelo de producto, lote y ubicación de M1 y de la base compartida'),
  (1.30, 'calibración del slotting y de la reposición con datos reales de rotación')),
 ('3.4.3', 'M5 Preparación', 5, [
   ('M', 'Generación de misiones por turno', 'RF-05.01'),
   ('C', 'Picking dirigido con secuencia seco, refrigerado, congelado', 'RF-02.08, RF-05.04'),
   ('M', 'Validación por escaneo y registro de lote', 'RF-05.02, RF-09.08'),
   ('S', 'Faltantes con motivo', 'RF-05.03'),
   ('M', 'Asignación FEFO', 'RF-05.05'),
   ('M', 'Carga en secuencia inversa a la ruta', 'RF-05.07'),
   ('M', 'Tiempo fuera de frío en andén', 'RF-09.11'),
   ('I', 'Cierre de misión al ERP', 'RF-05.06'),
   ('OFF', 'Operación sin cobertura en cámara', 'RNF-09.04, RT-17.01'),
   ('REN', 'Confirmación de línea en 1 segundo', 'RNF-05.01'),
   ('ESP', 'Interfaz operable con guantes a −22 °C', 'RNF-05.02')],
  (0.85, 'reutiliza lectura GS1 y cola local de M1'),
  (1.30, 'repetición de pruebas en cámara con guantes y con preparadores nuevos')),
 ('3.4.4', 'M9 Calidad, trazabilidad y frío en cámaras', 8, [
   ('C', 'Ciclo de vida del lote', 'RF-02.10'),
   ('C', 'Trazabilidad hacia adelante y hacia atrás', 'RF-09.01, RF-09.02'),
   ('M', 'Registro continuo de temperatura en cámaras', 'RF-09.03, RNF-09.05'),
   ('C', 'Motor de excursión térmica parametrizable y alertas', 'RF-09.05, RF-09.10'),
   ('M', 'Bloqueo preventivo del lote', 'RF-09.06'),
   ('S', 'Rechazo por sospecha de ruptura de frío', 'RF-09.07'),
   ('M', 'Evidencia de cumplimiento de cadena de frío', 'RF-09.09'),
   ('C', 'Habilitación de bajada de SSCC por latido y manifiesto', 'RF-09.12'),
   ('C', 'Retención en el terminal sin red', 'RF-09.13, RNF-09.06'),
   ('M', 'Disposición del producto retenido', 'RF-09.14'),
   ('D', 'Sensores y gateways de cámara', 'RF-09.03'),
   ('D', 'Termógrafo certificado y simuladores de producto', 'RNF-09.08'),
   ('I', 'Publicación a la capa analítica', 'RT-05.29'),
   ('ESP', 'Coherencia sin pérdidas ni duplicados en datos de sensores', 'RNF-09.09'),
   ('REN', 'Clientes afectados por lote en menos de 2 horas', 'RNF-09.01')],
  (0.95, 'poca reutilización: reglas térmicas y dispositivos son propios del módulo'),
  (1.45, 'homologación de sensores y repetición de ensayos de excursión y sin red en el banco 2.4.3')),
 ('3.4.5', 'M12 Telemetría y frío en camiones', 6, [
   ('M', 'Registro de temperatura en camiones', 'RF-09.04'),
   ('M', 'Ruta planificada frente a recorrida', 'RF-14.02'),
   ('M', 'Alerta por desvío de ruta', 'RF-14.03'),
   ('S', 'Envío de kilómetros y tiempos a costo de servir', 'RF-14.04'),
   ('M', 'Vínculo conductor, camión y viaje', 'RF-14.05'),
   ('M', 'Geocercas', 'RF-14.06'),
   ('D', 'Gateways de camión y telemetría del tercero', 'RF-09.04'),
   ('D', 'Doble camino móvil e Iridium SBD', 'RNF-09.07'),
   ('I', 'Administración remota de dispositivos', 'RT-03.18'),
   ('ESP', 'Ingesta en tiempo real con coherencia de secuencia', 'RNF-09.09')],
  (0.95, 'poca reutilización: canales de comunicación propios del camión'),
  (1.45, 'cobertura variable en ruta y ajustes de los dos caminos durante el piloto 4.1.4')),
 ('3.4.6', 'M3 Preventa', 5, [
   ('M', 'Stock con y sin conexión', 'RF-03.01, RF-03.02'),
   ('C', 'Reserva de stock por orden de llegada al servidor', 'RF-03.03'),
   ('M', 'Crédito y deuda con y sin conexión', 'RF-03.04, RF-03.05'),
   ('S', 'Historial de compra', 'RF-03.06'),
   ('M', 'Promociones', 'RF-03.07'),
   ('M', 'Alerta, bloqueo de crédito y autorización de supervisor', 'RF-03.08, RF-03.09, RF-03.10, RF-07.05'),
   ('M', 'Precio acordado y alerta de discrepancia', 'RF-03.11, RF-03.12'),
   ('C', 'Fecha y ventana de entrega comprometible', 'RF-03.13'),
   ('M', 'Sugerencia de productos', 'RF-03.14'),
   ('M', 'Identificador único y descarte de duplicados', 'RF-03.15, RF-03.16'),
   ('M', 'Cobranza en efectivo del preventista', 'RF-07.11'),
   ('I', 'Pedido, crédito y deuda con el ERP', 'RF-03.04'),
   ('OFF', 'Preventa sin conexión', 'RT-17.01'),
   ('REN', 'Registro de línea en 1,5 s', 'RNF-03.01'),
   ('REN', 'Consulta de stock y crédito en 2 s', 'RNF-03.02'),
   ('REN', 'Consulta de historial en 2 s', 'RNF-03.03')],
  (0.85, 'reutiliza la cola local y la sincronización de la base compartida'),
  (1.30, 'conflictos de reserva al sincronizar y reglas comerciales por validar con Comercial')),
 ('3.4.7', 'M4 Rutas', 6, [
   ('C', 'Asignación y secuenciación por capacidad y zona', 'RF-04.01'),
   ('M', 'Edición manual de secuencia y reasignación', 'RF-04.02'),
   ('S', 'Bloqueo por peso y volumen', 'RF-04.03'),
   ('C', 'Ventanas horarias del cliente en la secuencia', 'RF-04.04, RF-04.07'),
   ('S', 'Restricción de pedidos de frío a camiones con equipo', 'RF-04.05'),
   ('M', 'Aviso de llegada con ventana de 30 minutos', 'RF-04.06'),
   ('M', 'Planificación de la ventana del canal moderno', 'RF-12.10'),
   ('I', 'Motor de ruteo', 'RF-04.01'),
   ('I', 'Notificación al contacto del cliente', 'RF-04.06'),
   ('REN', 'Rutas del día en menos de 20 minutos', 'RNF-04.01')],
  (0.90, 'el motor de ruteo es un componente existente que se configura'),
  (1.45, 'calibración de restricciones con el planificador y validación sin él (R18-16)')),
 ('3.4.8', 'M6 Reparto', 6, [
   ('M', 'Recepción conforme por línea o guía', 'RF-06.01'),
   ('M', 'Firma o fotografía como evidencia de entrega', 'RF-06.02, RF-06.12, RF-12.12'),
   ('M', 'Rechazo total o parcial', 'RF-06.03'),
   ('S', 'Local cerrado', 'RF-06.04'),
   ('S', 'Hora de llegada y término', 'RF-06.06'),
   ('C', 'Sincronización completa del turno', 'RF-06.07'),
   ('M', 'Inicio de jornada con OTP para conductores externos', 'RF-06.08'),
   ('M', 'Confirmación por QR', 'RF-06.11'),
   ('M', 'Comprobante térmico por Bluetooth', 'RF-06.13'),
   ('M', 'Evidencia y acuse con el ERP', 'RF-06.14'),
   ('M', 'Acuse digital al canal moderno', 'RF-12.13'),
   ('S', 'Cumplimiento de la ventana de 30 minutos', 'RF-12.11'),
   ('C', 'Firma electrónica conforme a la Ley 19.799', 'RF-18.01'),
   ('I', 'Evidencia de entrega y acuse tributario con el ERP', 'RF-06.14'),
   ('D', 'Impresora portátil Bluetooth', 'RF-06.13'),
   ('D', 'Enlace local con el gateway del camión', 'RF-09.13'),
   ('OFF', 'Reparto sin conexión', 'RT-17.01'),
   ('ESP', 'Documentos cifrados con verificación de integridad', 'RT-16.16')],
  (0.85, 'reutiliza la cola local y la identidad de la base compartida'),
  (1.30, 'pruebas de campo con impresoras y firma electrónica en rutas sin señal')),
 ('3.4.9', 'M8 Devoluciones y retornables', 8, [
   ('S', 'Envases devueltos en la entrega', 'RF-06.09'),
   ('M', 'Cuenta corriente de envases y parque retornable', 'RF-06.10, RF-08.03'),
   ('M', 'Devolución en la entrega sin conexión', 'RF-08.01'),
   ('M', 'Destino de la devolución en andén', 'RF-08.02'),
   ('S', 'Alerta por umbral de envases', 'RF-08.04'),
   ('S', 'Reporte de pérdida de envases', 'RF-08.06'),
   ('I', 'Devoluciones al ERP', 'RF-08.02'),
   ('REN', 'Registro en andén en 30 s por ítem', 'RNF-08.01')],
  (0.80, 'reutiliza la aplicación y la sincronización de reparto (M6)'),
  (1.20, 'variedad de envases y destinos por validar con Logística')),
 ('3.4.10', 'M7 Cobranza y rendición', 9, [
   ('S', 'Monto en efectivo recaudado', 'RF-06.05'),
   ('M', 'Monto esperado de rendición por camión', 'RF-07.01'),
   ('C', 'Planilla digital de rendición', 'RF-07.02'),
   ('M', 'Causales de diferencia con bloqueo', 'RF-07.03'),
   ('C', 'Consola de cartera de crédito a 30 días', 'RF-07.04'),
   ('M', 'Cobro con tarjeta en ruta', 'RF-07.06'),
   ('M', 'Bandeja de validación de pagos del portal', 'RF-07.08'),
   ('M', 'Anticipos y pagos parciales', 'RF-07.10'),
   ('C', 'Liquidación y cierre comercial por camión', 'RF-11.07'),
   ('I', 'Recaudación idempotente hacia cuentas por cobrar del ERP', 'RF-07.09'),
   ('D', 'Terminal de pago por Bluetooth', 'RF-07.06'),
   ('REN', 'Sincronización de cobranzas en 10 minutos', 'RNF-07.01'),
   ('ESP', 'Controles de seguridad del medio de pago', 'RF-07.06')],
  (0.85, 'reutiliza la aplicación de reparto y la cola de sincronización'),
  (1.35, 'certificación del terminal de pago y conciliación con Finanzas')),
 ('3.4.11', 'M10 Analítica de la Etapa 1', 2, [
   ('C', 'Indicador OTIF', 'RF-11.03'),
   ('M', 'Fill rate y pedido perfecto', 'RF-11.04'),
   ('M', 'Utilización de capacidad por viaje', 'RF-11.05'),
   ('C', 'Tablero operacional en tiempo real', 'RF-11.06'),
   ('M', 'Reportes ejecutivos programados y exportables', 'RF-11.01, RT-05.28'),
   ('M', 'Filtros y detalle hasta la transacción', 'RT-05.26'),
   ('I', 'Ingesta desde la base transaccional', 'RT-05.25, RT-05.29'),
   ('REN', 'Indicadores del día en 5 minutos', 'RNF-11.01'),
   ('REN', 'Indicadores de gestión dentro de su latencia', 'RNF-11.04'),
   ('ESP', 'Aislamiento entre analítica y transacciones', 'RNF-11.02')],
  (0.85, 'reutiliza el modelo de datos de los módulos de operación'),
  (1.30, 'definiciones de indicadores por validar con Gerencia y datos incompletos al inicio')),
 ('3.5.1', 'M11 Canal moderno: intercambio electrónico', 3, [
   ('M', 'Recepción del pedido electrónico', 'RF-12.01'),
   ('M', 'Validación del pedido', 'RF-12.02'),
   ('M', 'Equivalencias de producto por cadena', 'RF-12.03'),
   ('M', 'Registro automático en el ERP', 'RF-12.04'),
   ('S', 'Pedido disponible para rutas', 'RF-12.05'),
   ('M', 'Bandeja de excepciones', 'RF-12.06'),
   ('M', 'Confirmación o rechazo a la cadena', 'RF-12.07'),
   ('S', 'Historial de estados del pedido', 'RF-12.08'),
   ('M', 'Aviso de despacho (ASN)', 'RF-12.09'),
   ('M', 'Portal de proveedores de solo lectura', 'RF-12.22, RF-12.23, RF-12.24'),
   ('I', 'Mensajería con las cadenas', 'RF-12.01, RF-12.07, RF-12.09'),
   ('I', 'Pedidos al ERP', 'RF-12.04'),
   ('REN', 'Acuse a la cadena dentro de 30 minutos', 'RNF-12.03')],
  (0.85, 'reutiliza la validación de pedidos y la cola de integración de la Etapa 1'),
  (1.40, 'diferencias entre perfiles de mensajes de cada cadena y certificación (3.6.5)')),
 ('3.5.2', 'M11 Canal moderno: portal de clientes', 3, [
   ('M', 'Portal público con catálogo', 'RF-12.14, RF-17.13, RT-16.31'),
   ('C', 'Pedido en autoservicio con crédito y stock', 'RF-12.15'),
   ('S', 'Estado de entregas', 'RF-12.16'),
   ('M', 'Documentos tributarios descargables', 'RF-12.17'),
   ('M', 'Saldo, estado de cuenta y cartola', 'RF-12.18, RF-07.07'),
   ('C', 'Registro, autenticación y recuperación de acceso', 'RF-12.25 a RF-12.29, RT-12.12'),
   ('M', 'Pago en Transbank', 'RF-12.30'),
   ('S', 'Medición de la autoatención', 'RT-16.32, RT-16.33'),
   ('I', 'Saldo y documentos desde el ERP', 'RF-12.17, RF-12.18'),
   ('I', 'Plataforma de pagos', 'RF-12.30'),
   ('ESP', 'Diseño responsivo y para equipos de bajo costo', 'RT-13.02, RT-17.08'),
   ('ESP', 'Seguridad de cuentas de usuarios externos', 'RT-12.12')],
  (0.85, 'reutiliza el validador de crédito y stock de preventa'),
  (1.30, 'certificación con la plataforma de pagos y pruebas de accesibilidad')),
 ('3.5.3', 'M11 Canal moderno: portal de transportistas', 3, [
   ('S', 'Rutas asignadas del día siguiente', 'RF-12.19'),
   ('S', 'Documentación de despacho por ruta', 'RF-12.20'),
   ('M', 'Confirmación de conductor y vehículo', 'RF-12.21'),
   ('ESP', 'Segregación por empresa', 'RF-12.19')],
  (0.80, 'reutiliza la autenticación del portal de clientes'),
  (1.20, 'ajuste de permisos con cada transportista')),
 ('3.5.4', 'M10 Costo de servir y rentabilidad', 3, [
   ('C', 'Costo de cada entrega', 'RF-04.08'),
   ('M', 'Costo de devoluciones y mermas por cliente', 'RF-08.07'),
   ('C', 'Costo de servir real por entrega y cliente', 'RF-11.02, RF-14.04'),
   ('C', 'Segmentación por rentabilidad', 'RF-11.08'),
   ('I', 'Costos directos desde el ERP', 'RF-11.02')],
  (0.85, 'reutiliza la capa analítica de la Etapa 1'),
  (1.35, 'validación del modelo de imputación con Finanzas')),
]

def estimate():
    out = []
    for code, name, it, els, (of, om), (pf, pm) in MODS:
        nf = {k: sum(1 for e in els if e[0] == k) for k in RATE}
        flows = nf['S'] + nf['M'] + nf['C']; ints = nf['I'] + nf['D']
        constr = sum(RATE[e[0]] for e in els)
        diseno = 8 * flows + 8 * ints
        pruebas = math.ceil(0.25 * constr)
        integ = 40 + 16 * ints
        iterac = 12 * it
        M = diseno + constr + pruebas + integ + iterac
        O = round(M * of); P = round(M * pf)
        E = round((O + 4 * M + P) / 6, 2)
        ids = sorted({x.strip() for e in els for x in e[2].replace(' a ', ', ').split(',')})
        out.append(dict(code=code, name=name, it=it, nf=nf, flows=flows, ints=ints, diseno=diseno,
                        constr=constr, pruebas=pruebas, integ=integ, iterac=iterac,
                        O=O, M=M, P=P, E=E, omot=om, pmot=pm, els=els, nreq=len(ids)))
    return out

if __name__ == '__main__':
    res = estimate()
    tot = sum(r['E'] for r in res)
    for r in res:
        n = r['nf']
        print(f"{r['code']:7} S{n['S']} M{n['M']} C{n['C']} I{n['I']} D{n['D']} OFF{n['OFF']} REN{n['REN']} ESP{n['ESP']} | dis {r['diseno']} con {r['constr']} pru {r['pruebas']} int {r['integ']} it {r['iterac']} | O {r['O']} M {r['M']} P {r['P']} E {r['E']}")
    print('total E', round(tot, 2), 'antes 15360', 'dif', round(tot - 15360, 2))
    if len(sys.argv) > 1:
        Path(sys.argv[1]).write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding='utf-8')
