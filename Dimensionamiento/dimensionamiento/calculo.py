"""Memoria reproducible del dimensionamiento del Caso 02.

El programa separa hechos, requisitos, parámetros de diseño y supuestos. La
volumetría se distribuye hora por hora antes de obtener las dieciséis
dimensiones; así no se suman ventanas que no coinciden.
"""

from __future__ import annotations

import math
from pathlib import Path


OUT = Path(__file__).with_name("resultados.md")


def fmt(value: float, digits: int = 2) -> str:
    return f"{value:,.{digits}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def fmt_int(value: float) -> str:
    return f"{int(round(value)):,}".replace(",", ".")


def ceil_int(value: float) -> int:
    return math.ceil(value)


def gb_from_kb(value: float) -> float:
    return value / 1_000_000


def erlang_c(agents: int, traffic: float) -> float:
    if traffic >= agents:
        return 1.0
    base = sum(traffic**k / math.factorial(k) for k in range(agents))
    last = traffic**agents / math.factorial(agents) * agents / (agents - traffic)
    return last / (base + last)


def service_level(agents: int, traffic: float, patience_s: float, aht_s: float) -> float:
    if traffic >= agents:
        return 0.0
    return 1 - erlang_c(agents, traffic) * math.exp(-(agents - traffic) * patience_s / aht_s)


def agents_for_service(contacts_hour: float, aht_s: float) -> int:
    traffic = contacts_hour * aht_s / 3600
    for agents in range(1, 101):
        if service_level(agents, traffic, 20.0, aht_s) >= 0.80:
            return agents
    return 100


# ================================ HECHOS ================================
# Las líneas del caso quedan sólo en comentarios para auditoría.
CLIENTES = 14_200                 # Caso, Tabla 2.2, líneas 108-111
FOOD_SERVICE = 2_100              # Caso, Tabla 2.2
CADENAS = 500                      # Caso, Tabla 2.2
SKU = 8_400                       # Caso, Tabla 2.2
POSICIONES = 11_400               # Caso, Tabla 2.3
PROVEEDORES = 180                 # Caso, Tabla 2.2
PEDIDOS_MES = 31_000              # Caso, Tabla 2.2
LINEAS_MES = 260_000              # Caso, Tabla 2.2
UNIDADES_MES = 2_400_000          # Caso, Tabla 2.2
ENTREGAS_NORMAL_DIA = 1_400       # Caso, Tabla 14.1
ENTREGAS_PEAK_DIA = 2_600         # Caso, Tabla 14.1
VIAJES_MES = 2_100                # Caso, Tabla 14.1
KM_MES = 420_000                  # Caso, Tabla 14.1
RECEPCIONES_MES = 1_150           # Caso, Tabla 14.1
PALLETS_MES = 14_500              # Caso, Tabla 14.1
POSICIONES_CONTADAS_MES = 3_400   # Caso, Tabla 14.1
DTE_MES = 34_000                  # Caso, Tabla 14.1
DEVOLUCIONES_MES = 900            # Caso, Tabla 14.1
VISITAS_PREVENTA_DIA = 2_600      # Caso, Anexo B.1; control 62 x 42, Cap. 8
COBROS_EFECTIVO_MES = 11_800      # Caso, Tabla 14.1
PREVENTISTAS = 62                 # Caso, Tabla 2.4
CAMIONES_PROPIOS = 42             # Caso, Tabla 2.3
CAMIONES_TERCEROS = 54            # Caso, Tabla 2.3
CAMIONES_TOTAL = CAMIONES_PROPIOS + CAMIONES_TERCEROS
CAMIONES_FRIO_PROPIOS = 18        # Caso, Tabla 2.3
CAMIONES_FRIO_TERCEROS = 10       # Caso, Tabla 2.3
TERMOGRAFOS = CAMIONES_FRIO_PROPIOS + CAMIONES_FRIO_TERCEROS
PERSONAL_PROPIO = 640             # Caso, Tabla 2.4
CONDUCTORES_TERCEROS = 160        # Caso, Tabla 2.4
PERSONAL_CD = 310                 # Caso, Tabla 2.4
PREPARADORES_NOCHE_TALCA = 120    # Caso, Cap. 8, entrevista jefa de bodega
TALCA_M2 = 18_000                 # Caso, Tabla 2.3
CONCEPCION_M2 = 9_000             # Caso, Tabla 2.3
CROSS_DOCKS = 3                   # Caso, Tabla 2.3
OFICINA_PERSONAS = 184            # Caso, Tabla 2.4
RUTA_PEOR_CLIENTES = 34           # Caso, Cap. 8, entrevista conductor Cauquenes
RUTA_PROMEDIO_NORMAL = 14.6       # cálculo: 1.400 entregas / 96 camiones
RUTA_PROMEDIO_PEAK = 27.1         # cálculo: 2.600 entregas / 96 camiones
CADENA_VENTA_SHARE = 0.11         # Caso, Cap. 7.3
INSTALACIONES = 6                 # Caso, Tabla 14.1

# Proyección literal de la Tabla 14.1 a tres años.
Y3_PEDIDOS_MES = 36_000
Y3_LINEAS_MES = 305_000
Y3_ENTREGAS_NORMAL_DIA = 1_650
Y3_ENTREGAS_PEAK_DIA = 3_100
Y3_DTE_MES = 40_000
Y3_CD_PERSONAL = 350

# ============================== REQUISITOS ===============================
REQ_CD_SIN_ENLACE_H = 24         # Caso, Cap. 15
REQ_TERRENO_SIN_ENLACE_H = 14     # Caso, Cap. 15
REQ_SYNC_DISPOSITIVO_MIN = 10     # Caso, Cap. 15
REQ_SYNC_CD_H = 2                 # Caso, Cap. 15
REQ_CRECIMIENTO = 3.0             # BTT RT-09.03
REQ_PRUEBA_CARGA = 1.5            # BTT RT-09.06
REQ_RET_TEMP_ANIOS = 5            # Caso, Cap. 15
REQ_RET_GEO_MESES = 12            # Caso, Cap. 15
REQ_RET_EVIDENCIA_ANIOS = 6       # Caso, Cap. 15
REQ_MESA_SL = 0.80                # BTT RT-21.06
REQ_MESA_PATIENCE_S = 20.0        # BTT RT-21.06
REQ_MESA_ABANDONO = 0.05         # BTT RT-21.06

# ========================= PARÁMETROS DE DISEÑO ==========================
PICKING_TX_PER_LINE = 2
TRACE_EVENTS_PER_LINE = 5
RESERVATION_MESSAGES_PER_LINE = 4   # retener y liberar, cada uno con solicitud y resultado (INT-03/04)
DELIVERY_TX_PER_DELIVERY = 5
DISPATCH_TX_PER_DELIVERY = 2
DISPATCH_TX_PER_TRUCK = 2
CROSSDOCK_TX_PER_DELIVERY = 4
PREVENTA_TX_PER_VISIT = 2         # consulta de stock y crédito
PREVENTA_TX_PER_LINE = 1
EDI_MESSAGES_PER_ORDER = 4
PAYMENT_MESSAGES_PER_DELIVERY = 2   # cota: un pago electrónico por entrega, solicitud y respuesta
PORTAL_REQUESTS_PER_SESSION = 60
PORTAL_SESSION_MINUTES = 10
PORTAL_SENSITIVITY_REQUESTS = 120
PORTAL_SENSITIVITY_MINUTES = 15
EVIDENCE_PHOTO_KB = 200.0
EVIDENCE_SIGNATURE_KB = 30.0
OFFLINE_ROUTE_MB = 2.0
RECORD_KB = 1.0
MOVEMENT_KB = 0.5
INDEX_AUDIT_FACTOR = 2.0
LOCAL_DISK_FACTOR = 2.0
LOCAL_HORIZON_MONTHS = 4
LOT_RECORDS_PER_SKU = 3
WORKING_SET_FRACTION = 0.25
CPU_UTILIZATION = 0.70
CPU_MS = {"app": 50.0, "db": 20.0, "broker": 10.0, "acl": 20.0, "identity": 10.0, "obs": 5.0}
OBS_MB_PER_NODE_DAY = 250.0
OBS_NODES = {"Talca": 6, "Concepción": 4, "Cada cross-docking": 1}
# RT-03.14: Concepción y cada cross-docking tienen un equipo en espera. No atiende
# transacciones: sin trazas, con métricas y registros estimados en 20 % de un nodo activo.
OBS_STANDBY_NODES = {"Talca": 0, "Concepción": 4, "Cada cross-docking": 1}
OBS_STANDBY_FACTOR = 0.20
CAMERA_POINTS = 21                 # diseño B-01: 15 en Talca y 6 en Concepción (S-37)
CAMERA_POINTS_SITE = {"Talca": 15, "Concepción": 6}
TEMP_MINUTES = 5
TEMP_RECORD_BYTES = 145          # bytes por lectura de temperatura
POSITION_RECORD_BYTES = 145      # bytes por evento de posición
TEMP_COMPRESSION = 0.25
POSITION_SECONDS = 30
ROUTE_HOURS = 12
THERMOGRAPH_ROUTE_HOURS = 14.5   # Caso, Anexo B.1: despacho desde 05:30 y regreso de la flota hasta 20:00
WAL_FACTOR = 3.0
BROKER_FACTOR_OF_CHANGES = 0.50
OFFICE_MB_PER_USER_H = 5.0
APP_UPDATE_GB_PER_DEVICE = 0.1
OS_UPDATE_GB_PER_DEVICE = 2.0
RECEPTION_LINES_PER_RECEIPT = 20.0
OBS_EVENTS_PER_NODE_DAY = 1_000
IDENTITY_MESSAGES_PER_DEVICE_DAY = 2
BACKUP_FULL_WINDOW_H = 8
JORNADA_SEMANAL_H = 42
FARGATE_CPU_MS = 50.0
FARGATE_RESIDENCY_MS = 150.0
FARGATE_RAM_MB = 64
FARGATE_TASKS_MIN = 2
FARGATE_TASKS_MAX = 8
HYPERVISOR_CPU_OVERHEAD = 0.15
HYPERVISOR_RAM_GB = 2.0
CEPH_OSDS_PER_NODE = 2
CEPH_OSD_VCPU = 1
CEPH_OSD_RAM_GB = 4
CEPH_MON_MGR_VCPU = 1
CEPH_MON_MGR_RAM_GB = 2
ERP_SYNC_PROCESSES = 2
ERP_SYNC_RAM_MB_PER_PROCESS = 64
PRIORITY_MESSAGE_KB = 1.0       # guía, respuesta de SII e identidad; cota por mensaje
T11_TALCA_NODES = 3
T11_TALCA_NODE_VCPU = 32
T11_TALCA_NODE_RAM_GB = 64
T11_TALCA_OSD_GB = 960
CEPH_REPLICAS = 3
CEPH_MAX_FILL = 0.80
T11_CONCEPCION_VCPU = 16
T11_CONCEPCION_RAM_GB = 32
T11_CONCEPCION_SSD_GB = 1_920
T11_CONCEPCION_RAID10_DISKS = 4
T11_SATELLITE_MBPS = 2.0
T11_GENERATOR_KVA = 20
T11_SITE_LOAD_KW = 10.8
T11_SERVER_COOLING_KW = 7.0
T11_UPS_ROOM_COOLING_KW = 3.5
VM_BASE_DISK_GB = {"app": 50, "db": 20, "broker": 50, "acl": 20, "identity": 20, "obs": 50}
VM_BASE_RAM_GB = {"app": 4, "db": 4, "broker": 4, "acl": 2, "identity": 2, "obs": 4}
VM_BASE_VCPU = {"app": 2, "db": 2, "broker": 1, "acl": 1, "identity": 1, "obs": 1}
IOPS_PER_TPS = 8
CROSSDOCK_BASE_VCPU = 2
CROSSDOCK_BASE_RAM_GB = 4

# Hora cargada de cada ventana: sólo esta hora recibe SV-04.
LOADED_HOUR = {"preparación": 5, "cross-docking": 4, "cross-docking despacho": 5, "despacho": 6,
               "reparto": 12, "recepción": 10, "preventa": 12,
               "sincronización": 18, "portal": 12, "guías": 5}

# ================================ SUPUESTOS ===============================
S47_PEDIDO_ENTREGA = 1.0
S48_DICIEMBRE_FACTOR = 1.0
S49_TALCA_SHARE = 2 / 3
S39_CONCEPCION_NIGHT_USERS = 60   # S-39 (registro del Subdocumento 3)
S34_FREEZER_CREW_TALCA = 20       # S-34
S35_CROSS_USERS_PER_DOCK = 2      # S-35
S51_CONCENTRATION_FACTOR = 2.0
S52_SHARE_CHAIN_ORDERS = 0.11
S53_HELP_CONTACTS_PER_PERSON = 2.5
S53_HELP_AHT_MIN = 10.0
S53_HELP_PEAK_SHARE = 0.25
S28_THIRD_PARTY_COLD_ACCESS = 1.0  # S-28
S55_OWN_TELEMETRY_ACCESS = 1.0


def hourly_profile(volume_factor: float, edi_active: bool, *, lines_factor: float | None = None,
                   orders_factor: float | None = None, visits_factor: float | None = None,
                   receipts_factor: float | None = None, dte_factor: float | None = None,
                   portal_factor: float = 1.0,
                   avg_lines_order: float | None = None) -> list[dict[str, float]]:
    """Construye la tasa de cada lugar en cada hora civil del día."""
    dispatch_days = PEDIDOS_MES / ENTREGAS_NORMAL_DIA
    lines_factor = volume_factor if lines_factor is None else lines_factor
    orders_factor = volume_factor if orders_factor is None else orders_factor
    visits_factor = volume_factor if visits_factor is None else visits_factor
    receipts_factor = volume_factor if receipts_factor is None else receipts_factor
    dte_factor = volume_factor if dte_factor is None else dte_factor
    orders = ENTREGAS_NORMAL_DIA * orders_factor
    lines = (LINEAS_MES / dispatch_days) * lines_factor
    receipts = (RECEPCIONES_MES / dispatch_days) * receipts_factor
    dte = (DTE_MES / dispatch_days) * dte_factor
    visits = VISITAS_PREVENTA_DIA * visits_factor
    avg_lines_order = (LINEAS_MES / PEDIDOS_MES) if avg_lines_order is None else avg_lines_order
    preventa_volume = visits * (PREVENTA_TX_PER_VISIT + avg_lines_order * PREVENTA_TX_PER_LINE)
    prep_mean_tps = lines * PICKING_TX_PER_LINE / (8 * 3600)
    cross_arrival_mean_tps = orders * (CROSSDOCK_TX_PER_DELIVERY - 1) / (2 * 3600)
    cross_dispatch_mean_tps = orders / 3600
    delivery_mean_tps = orders * DELIVERY_TX_PER_DELIVERY / (12 * 3600)
    preventa_mean_tps = preventa_volume / (9 * 3600)
    receipt_mean_tps = receipts / (10 * 3600)
    trace_mean_tps = lines * TRACE_EVENTS_PER_LINE / (24 * 3600)
    sync_mean_tps = (orders + orders * DELIVERY_TX_PER_DELIVERY) / (3 * 3600)
    edi_mean_tps = (orders * S52_SHARE_CHAIN_ORDERS * EDI_MESSAGES_PER_ORDER / (9 * 3600)) if edi_active else 0.0
    guide_mean_tps = dte / 27_000
    portal_mean_tps = 2_600 * portal_factor * PORTAL_REQUESTS_PER_SESSION / (9 * 3600)
    dispatch_mean_tps = (orders * DISPATCH_TX_PER_DELIVERY + CAMIONES_TOTAL * DISPATCH_TX_PER_TRUCK) / 5_400

    rows: list[dict[str, float]] = []
    for hour in range(24):
        prep = prep_mean_tps if hour in {22, 23, 0, 1, 2, 3, 4, 5} else 0.0
        if hour == LOADED_HOUR["preparación"]:
            prep *= S51_CONCENTRATION_FACTOR
        cross = cross_arrival_mean_tps if hour in {3, 4} else cross_dispatch_mean_tps if hour == 5 else 0.0
        if hour == LOADED_HOUR["cross-docking"]:
            cross *= S51_CONCENTRATION_FACTOR
        if hour == LOADED_HOUR["cross-docking despacho"]:
            cross *= S51_CONCENTRATION_FACTOR
        dispatch = dispatch_mean_tps if hour in {5, 6} else 0.0
        if hour == LOADED_HOUR["despacho"]:
            dispatch *= S51_CONCENTRATION_FACTOR
        delivery = delivery_mean_tps if 7 <= hour < 19 else 0.0
        if hour == LOADED_HOUR["reparto"]:
            delivery *= S51_CONCENTRATION_FACTOR
        preventa = preventa_mean_tps if 9 <= hour < 18 else 0.0
        if hour == LOADED_HOUR["preventa"]:
            preventa *= S51_CONCENTRATION_FACTOR
        receipt = receipt_mean_tps if 8 <= hour < 18 else 0.0
        if hour == LOADED_HOUR["recepción"]:
            receipt *= S51_CONCENTRATION_FACTOR
        trace = trace_mean_tps
        sync = sync_mean_tps if 17 <= hour < 20 else 0.0
        if hour == LOADED_HOUR["sincronización"]:
            sync *= S51_CONCENTRATION_FACTOR
        edi = edi_mean_tps if 9 <= hour < 18 else 0.0
        if hour == LOADED_HOUR["preventa"]:
            edi *= S51_CONCENTRATION_FACTOR
        guides = guide_mean_tps if hour in {22, 23, 0, 1, 2, 3, 4, 5} else 0.0
        if hour == LOADED_HOUR["guías"]:
            guides *= S51_CONCENTRATION_FACTOR
        portal = portal_mean_tps if 9 <= hour < 18 else 0.0
        if hour == LOADED_HOUR["portal"]:
            portal *= S51_CONCENTRATION_FACTOR
        talca = (prep + dispatch) * S49_TALCA_SHARE
        concepcion = (prep + dispatch) * (1 - S49_TALCA_SHARE)
        cloud = preventa + delivery + receipt + trace + sync + edi + guides
        total = talca + concepcion + cross + cloud + portal
        rows.append({"hora": hour, "Talca": talca, "Concepción": concepcion,
                     "cross-docking": cross, "nube": cloud, "portal": portal,
                     "total": total, "guías": guides, "preventa": preventa,
                     "sincronización": sync})
    return rows


def peak_row(rows: list[dict[str, float]], key: str = "total") -> dict[str, float]:
    return max(rows, key=lambda row: row[key])


def resource_line(res: dict[str, float]) -> str:
    return f"{res['vcpu']} vCPU, {res['ram_gb']} GB RAM, {res['disk_gb']} GB disco lógico, {res['iops']} IOPS"


def main() -> None:
    dispatch_days = PEDIDOS_MES / ENTREGAS_NORMAL_DIA
    crosscheck_days = VIAJES_MES / CAMIONES_TOTAL
    factor_peak = ENTREGAS_PEAK_DIA / ENTREGAS_NORMAL_DIA
    orders_day = PEDIDOS_MES / dispatch_days
    lines_day = LINEAS_MES / dispatch_days
    dte_day = DTE_MES / dispatch_days
    return_rate = DEVOLUCIONES_MES / PEDIDOS_MES

    normal_rows = hourly_profile(1.0, True)   # el EDI opera todos los días desde enero de 2029
    peak_rows = hourly_profile(factor_peak, True)
    y3_lines_factor = Y3_LINEAS_MES / LINEAS_MES
    y3_orders_factor = Y3_ENTREGAS_PEAK_DIA / ENTREGAS_PEAK_DIA
    y3_receipts_factor = Y3_PEDIDOS_MES / PEDIDOS_MES
    y3_dte_factor = Y3_DTE_MES / DTE_MES
    year3_peak_rows = hourly_profile(
        1.0,
        True,
        lines_factor=factor_peak * y3_lines_factor,
        orders_factor=factor_peak * y3_orders_factor,
        visits_factor=factor_peak * y3_orders_factor,
        receipts_factor=factor_peak * y3_receipts_factor,
        dte_factor=factor_peak * y3_dte_factor,
        avg_lines_order=Y3_LINEAS_MES / Y3_PEDIDOS_MES,
    )
    normal_max = peak_row(normal_rows)
    peak_max = peak_row(peak_rows)
    place_keys = ["Talca", "Concepción", "cross-docking", "nube", "portal"]
    normal_place_max = {key: peak_row(normal_rows, key) for key in place_keys}
    peak_place_max = {key: peak_row(peak_rows, key) for key in place_keys}
    normal_tps = normal_max["total"]
    peak_tps = peak_max["total"]

    # Dimensión 2: máximo horario efectivo entre las horas que intersectan
    # 05:30–07:00. El tramo 05:00 se supone uniforme y aporta desde 05:30.
    dte_peak_day = dte_day * factor_peak
    dispatch_window_rows_normal = [normal_rows[5], normal_rows[6]]
    dispatch_window_rows_peak = [peak_rows[5], peak_rows[6]]
    dim2_normal = max(row["total"] for row in dispatch_window_rows_normal)
    dim2_peak = max(row["total"] for row in dispatch_window_rows_peak)
    load_test_tps = peak_tps * REQ_PRUEBA_CARGA

    portal_regime_sessions_h = 2_600 / 9 * S51_CONCENTRATION_FACTOR
    portal_regime_requests_s = portal_regime_sessions_h * PORTAL_REQUESTS_PER_SESSION / 3_600
    portal_regime_concurrent = portal_regime_sessions_h * PORTAL_SESSION_MINUTES / 60
    portal_extreme_requests_s = 2_600 * PORTAL_REQUESTS_PER_SESSION / 3_600
    portal_extreme_concurrent = 2_600 * PORTAL_SESSION_MINUTES / 60
    portal_sensitivity_regime_requests_s = portal_regime_sessions_h * PORTAL_SENSITIVITY_REQUESTS / 3_600
    portal_sensitivity_extreme_requests_s = 2_600 * PORTAL_SENSITIVITY_REQUESTS / 3_600
    portal_sensitivity_concurrent = portal_regime_sessions_h * PORTAL_SENSITIVITY_MINUTES / 60
    portal_sensitivity_extreme_concurrent = 2_600 * PORTAL_SENSITIVITY_MINUTES / 60

    internal_users = PERSONAL_PROPIO + CONDUCTORES_TERCEROS
    registered = internal_users + CLIENTES + PROVEEDORES
    def with_reserve(n: float) -> int:
        n = ceil_int(n)
        return n + ceil_int(n * 0.10)
    warehouse_terminals = {"Talca": with_reserve(S34_FREEZER_CREW_TALCA) + with_reserve(PREPARADORES_NOCHE_TALCA - S34_FREEZER_CREW_TALCA),
                           "Concepción": with_reserve(S39_CONCEPCION_NIGHT_USERS)}
    preventa_devices = ceil_int(PREVENTISTAS * 1.10)
    truck_devices = ceil_int(CAMIONES_TOTAL * 1.10)
    cross_scanners = S35_CROSS_USERS_PER_DOCK * CROSS_DOCKS
    cross_park = cross_scanners + CROSS_DOCKS   # una unidad de reserva en cada plataforma, como en el T-11
    equipment_park = {"terminales de bodega": sum(warehouse_terminals.values()),
                      "terminales de preventa": preventa_devices,
                      "terminales de reparto": truck_devices,
                      "impresoras de cabina": truck_devices,
                      "terminales de pago": truck_devices,
                      "terminales de cross-docking": cross_park,
                      "termógrafos": TERMOGRAFOS,
                      "puntos de cámara": CAMERA_POINTS}
    equipment_total = sum(equipment_park.values())
    operational_concurrency = {"noche": PREPARADORES_NOCHE_TALCA + S39_CONCEPCION_NIGHT_USERS + cross_scanners,
                               "despacho": CAMIONES_TOTAL,
                               "día sin portal": PREVENTISTAS + CAMIONES_TOTAL + OFICINA_PERSONAS,
                               "sincronización": CAMIONES_TOTAL + PREVENTISTAS}
    concurrency_regime = operational_concurrency["día sin portal"] + portal_regime_concurrent
    concurrency_extreme = operational_concurrency["día sin portal"] + portal_extreme_concurrent

    movement_records_month = LINEAS_MES + PALLETS_MES + POSICIONES_CONTADAS_MES + RECEPCIONES_MES
    line_event_records_month = LINEAS_MES * TRACE_EVENTS_PER_LINE
    picking_records_month = LINEAS_MES * PICKING_TX_PER_LINE
    delivery_records_month = PEDIDOS_MES * DELIVERY_TX_PER_DELIVERY
    transactional_kb_month = ((line_event_records_month + picking_records_month + delivery_records_month) * RECORD_KB + movement_records_month * MOVEMENT_KB) * INDEX_AUDIT_FACTOR
    transactional_gb_year = gb_from_kb(transactional_kb_month * 12)
    transactional_gb_peak_month = gb_from_kb(transactional_kb_month * factor_peak)
    evidence_kb = EVIDENCE_SIGNATURE_KB + EVIDENCE_PHOTO_KB * (1 + return_rate)
    evidence_gb_year = PEDIDOS_MES * 12 * S47_PEDIDO_ENTREGA * evidence_kb / 1_000_000
    evidence_gb_peak_month = PEDIDOS_MES * factor_peak * evidence_kb / 1_000_000

    camera_messages_day = CAMERA_POINTS * (24 * 60 / TEMP_MINUTES)
    thermograph_messages_day = TERMOGRAFOS * (THERMOGRAPH_ROUTE_HOURS * 60 / TEMP_MINUTES) * S28_THIRD_PARTY_COLD_ACCESS
    temp_messages_day = camera_messages_day + thermograph_messages_day
    temp_records_year = temp_messages_day * 365
    temp_raw_gb_year = temp_records_year * TEMP_RECORD_BYTES / 1_000_000_000
    temp_stored_gb_year = temp_raw_gb_year * TEMP_COMPRESSION
    position_records_year = CAMIONES_PROPIOS * S55_OWN_TELEMETRY_ACCESS * (3600 / POSITION_SECONDS) * ROUTE_HOURS * 365
    position_raw_gb_year = position_records_year * POSITION_RECORD_BYTES / 1_000_000_000
    position_stored_gb_year = position_raw_gb_year * TEMP_COMPRESSION

    historical_domains = {
        "maestros completos": (SKU + POSICIONES + CLIENTES + PROVEEDORES) * RECORD_KB,
        "ventas y pedidos, 3 años": (PEDIDOS_MES + LINEAS_MES) * 36 * RECORD_KB,
        "inventario y movimientos, 2 años": (LINEAS_MES + PALLETS_MES + RECEPCIONES_MES + POSICIONES_CONTADAS_MES) * 24 * MOVEMENT_KB,
        "recepciones con lote, 5 años": RECEPCIONES_MES * RECEPTION_LINES_PER_RECEIPT * 60 * RECORD_KB,
        "cuentas por cobrar, 2 años": DTE_MES * 24 * RECORD_KB}
    historical_raw_kb = sum(historical_domains.values())
    historical_trace_kb = historical_domains["recepciones con lote, 5 años"]
    historical_gb = gb_from_kb(historical_raw_kb * INDEX_AUDIT_FACTOR)
    historical_low_gb = gb_from_kb((historical_raw_kb - historical_trace_kb + historical_trace_kb * 0.5) * INDEX_AUDIT_FACTOR)
    historical_high_gb = gb_from_kb((historical_raw_kb - historical_trace_kb + historical_trace_kb * 1.5) * INDEX_AUDIT_FACTOR)

    obs_active_nodes = OBS_NODES["Talca"] + OBS_NODES["Concepción"] + CROSS_DOCKS * OBS_NODES["Cada cross-docking"]
    obs_standby_nodes = OBS_STANDBY_NODES["Concepción"] + CROSS_DOCKS * OBS_STANDBY_NODES["Cada cross-docking"]
    obs_events_day = (obs_active_nodes + obs_standby_nodes * OBS_STANDBY_FACTOR) * OBS_EVENTS_PER_NODE_DAY
    integration_rows = [
        ("INT-01", "Pedido preventa y consulta", orders_day, ENTREGAS_PEAK_DIA, "1.400 × 1; 2.600 × 1; SV-01"),
        ("INT-02", "Entrega, POD y cobro", ENTREGAS_NORMAL_DIA * DELIVERY_TX_PER_DELIVERY, ENTREGAS_PEAK_DIA * DELIVERY_TX_PER_DELIVERY, "1.400 × 5; 2.600 × 5"),
        ("INT-03", "Eventos de bodega a nube", lines_day * TRACE_EVENTS_PER_LINE, lines_day * factor_peak * TRACE_EVENTS_PER_LINE, "260.000 ÷ 22,14 × 5; peak × 1,857"),
        ("INT-04", "Detalle cross-docking a la nube", ENTREGAS_NORMAL_DIA * CROSSDOCK_TX_PER_DELIVERY, ENTREGAS_PEAK_DIA * CROSSDOCK_TX_PER_DELIVERY, "1.400 × 4; cota de una plataforma"),
        ("INT-03/04", "Coordinación de reserva", round(lines_day) * RESERVATION_MESSAGES_PER_LINE, round(round(lines_day) * factor_peak) * RESERVATION_MESSAGES_PER_LINE, "260.000 ÷ 22,14 × 4; peak: 21.807 líneas × 4"),
        ("INT-05", "Eventos de temperatura", temp_messages_day, temp_messages_day, "6.048 cámaras + 4.872 termógrafos"),
        ("INT-06", "ERP 2017", orders_day + RECEPCIONES_MES / dispatch_days + DEVOLUCIONES_MES / dispatch_days + COBROS_EFECTIVO_MES / dispatch_days, (orders_day + RECEPCIONES_MES / dispatch_days + DEVOLUCIONES_MES / dispatch_days + COBROS_EFECTIVO_MES / dispatch_days) * factor_peak, "1.400 + 1.150 ÷ 22,14 + 900 ÷ 22,14 + 11.800 ÷ 22,14; peak × 1,857"),
        ("INT-07", "DTE/SII", dte_day * 2, dte_peak_day * 2, "34.000 ÷ 22,14 × 2; peak × 1,857"),
        ("INT-08", "Cadenas modernas EDI", orders_day * S52_SHARE_CHAIN_ORDERS * EDI_MESSAGES_PER_ORDER, orders_day * factor_peak * S52_SHARE_CHAIN_ORDERS * EDI_MESSAGES_PER_ORDER, "Escenario 2029 (hoy 0): 1.400 × 11 % × 4; 2.600 × 11 % × 4"),
        ("INT-09", "Pasarela de pago", ENTREGAS_NORMAL_DIA * PAYMENT_MESSAGES_PER_DELIVERY, ENTREGAS_PEAK_DIA * PAYMENT_MESSAGES_PER_DELIVERY, "Cota: un pago electrónico por entrega × 2 mensajes; 1.400 × 2; 2.600 × 2"),
        ("INT-10", "Mapas y geocodificación", CAMIONES_TOTAL, CAMIONES_TOTAL, "96 camiones × 1"),
        ("INT-11", "Avisos al cliente", ENTREGAS_NORMAL_DIA * 2, ENTREGAS_PEAK_DIA * 2, "1.400 × 2; 2.600 × 2"),
        ("INT-12", "Cambios de datos a réplica", movement_records_month / dispatch_days, movement_records_month / dispatch_days * factor_peak, "279.050 ÷ 22,14; peak × 1,857"),
        ("INT-13", "Identidad a sitio", (sum(warehouse_terminals.values()) + preventa_devices + truck_devices + cross_park) * IDENTITY_MESSAGES_PER_DEVICE_DAY, (sum(warehouse_terminals.values()) + preventa_devices + truck_devices + cross_park) * IDENTITY_MESSAGES_PER_DEVICE_DAY, f"{fmt_int(sum(warehouse_terminals.values()) + preventa_devices + truck_devices + cross_park)} dispositivos × 2"),
        ("INT-14", "Métricas y trazas", obs_events_day, obs_events_day, f"{obs_active_nodes} nodos activos × 1.000 + {obs_standby_nodes} en espera × {fmt_int(OBS_EVENTS_PER_NODE_DAY * OBS_STANDBY_FACTOR)}"),
        ("INT-15", "Telemetría existente", CAMIONES_PROPIOS * S55_OWN_TELEMETRY_ACCESS * (3600 / POSITION_SECONDS) * ROUTE_HOURS, CAMIONES_PROPIOS * S55_OWN_TELEMETRY_ACCESS * (3600 / POSITION_SECONDS) * ROUTE_HOURS, "42 × 12 × 120; SV-07")]
    # El redondeo se aplica por integración y luego se suma, para que la tabla
    # sea auditable y el total sea exactamente la suma de sus filas.
    integration_rows = [(code, name, round(normal), round(peak), source)
                        for code, name, normal, peak, source in integration_rows]
    message_total = sum(row[2] for row in integration_rows)
    message_peak = sum(row[3] for row in integration_rows)

    lines_site = {"Talca": lines_day * S49_TALCA_SHARE, "Concepción": lines_day * (1 - S49_TALCA_SHARE)}
    site_tps_peak = {site: peak_row(peak_rows, site)[site] for site in ["Talca", "Concepción"]}
    site_tps_peak["Cada cross-docking"] = peak_row(peak_rows, "cross-docking")["cross-docking"]

    def local_components(site: str) -> dict[str, float]:
        masters = SKU + POSICIONES + CLIENTES + PROVEEDORES
        stock = SKU
        lots = SKU * LOT_RECORDS_PER_SKU
        if site in lines_site:
            share = S49_TALCA_SHARE if site == "Talca" else 1 - S49_TALCA_SHARE
            monthly_movements = LINEAS_MES * share * (TRACE_EVENTS_PER_LINE + PICKING_TX_PER_LINE) + RECEPCIONES_MES * share + PALLETS_MES * share + POSICIONES_CONTADAS_MES * share
        else:
            monthly_movements = ENTREGAS_NORMAL_DIA * dispatch_days * CROSSDOCK_TX_PER_DELIVERY
        masters_kb = (masters + stock + lots) * RECORD_KB
        movements_kb = monthly_movements * MOVEMENT_KB * LOCAL_HORIZON_MONTHS
        db_kb = (masters_kb + movements_kb) * INDEX_AUDIT_FACTOR
        return {"masters": masters, "monthly_movements": monthly_movements, "db_gb": gb_from_kb(db_kb), "movement_data_gb": gb_from_kb(movements_kb * INDEX_AUDIT_FACTOR)}

    components = {site: local_components(site) for site in site_tps_peak}
    local_db = {site: values["db_gb"] for site, values in components.items()}
    local_db_3x = {site: value * REQ_CRECIMIENTO for site, value in local_db.items()}
    working_set_ram = {site: 4.0 + value * 0.25 for site, value in local_db_3x.items()}

    def vm_resource(role: str, tps: float, scale: float, db_gb: float = 0.0, extra_tps: float = 0.0) -> dict[str, float]:
        cpu_load = (tps * scale + extra_tps) * CPU_MS[role] / 1000 / CPU_UTILIZATION
        vcpu = ceil_int(VM_BASE_VCPU[role] + cpu_load)
        ram = VM_BASE_RAM_GB[role]
        if role == "db":
            ram = ceil_int(4.0 + db_gb * 0.25)
        disk = max(20, VM_BASE_DISK_GB[role])
        if role == "db":
            disk = max(20, math.ceil(db_gb * LOCAL_DISK_FACTOR))
        iops = ceil_int(max(1.0, (tps * scale + extra_tps) * IOPS_PER_TPS))
        return {"vcpu": vcpu, "ram_gb": ram, "disk_gb": disk, "iops": iops}

    def vm_set(site: str, scale: float) -> dict[str, dict[str, float]]:
        peak = site_tps_peak[site]
        db = local_db[site] * scale
        if site == "Talca":
            acl = vm_resource("acl", dte_peak_day / 5_400, scale)
            acl["ram_gb"] = max(acl["ram_gb"], ceil_int(VM_BASE_RAM_GB["acl"] + ERP_SYNC_PROCESSES * ERP_SYNC_RAM_MB_PER_PROCESS / 1024))
            return {"VM-01": vm_resource("app", peak, scale), "VM-02": vm_resource("db", peak, scale, db), "VM-03": vm_resource("broker", peak, scale), "VM-04": acl, "VM-05": vm_resource("identity", peak, scale), "VM-06": vm_resource("obs", peak, scale, extra_tps=peak)}
        return {"VM-C01": vm_resource("app", peak, scale), "VM-C02": vm_resource("db", peak, scale, db), "VM-C03": vm_resource("identity", peak, scale), "VM-C04": vm_resource("broker", peak, scale, extra_tps=peak)}

    vm_sets = {"Talca": vm_set("Talca", 1.0), "Concepción": vm_set("Concepción", 1.0)}
    vm_sets_3x = {"Talca": vm_set("Talca", 3.0), "Concepción": vm_set("Concepción", 3.0)}

    def crossdock_resource(scale: float) -> dict[str, float]:
        tps = site_tps_peak["Cada cross-docking"] * scale
        vcpu = ceil_int(CROSSDOCK_BASE_VCPU + tps * 80 / 1000 / CPU_UTILIZATION)
        ram = ceil_int(CROSSDOCK_BASE_RAM_GB + local_db["Cada cross-docking"] * scale * 0.25)
        disk = max(50, math.ceil(local_db["Cada cross-docking"] * scale * LOCAL_DISK_FACTOR))
        iops = ceil_int(max(1.0, tps * IOPS_PER_TPS * 3))
        return {"vcpu": vcpu, "ram_gb": ram, "disk_gb": disk, "iops": iops}

    cross_vm = crossdock_resource(1.0)
    cross_vm_3x = crossdock_resource(3.0)

    def sum_resources(vm_map: dict[str, dict[str, float]]) -> dict[str, float]:
        return {key: sum(item[key] for item in vm_map.values()) for key in ("vcpu", "ram_gb", "disk_gb", "iops")}

    vm_total = {site: sum_resources(values) for site, values in vm_sets.items()}
    vm_total_3x = {site: sum_resources(values) for site, values in vm_sets_3x.items()}

    def cluster_resources(total: dict[str, float], physical_nodes: int, ceph: bool = False) -> dict[str, float]:
        ceph_vcpu = physical_nodes * (CEPH_OSDS_PER_NODE * CEPH_OSD_VCPU + CEPH_MON_MGR_VCPU) if ceph else 0
        ceph_ram = physical_nodes * (CEPH_OSDS_PER_NODE * CEPH_OSD_RAM_GB + CEPH_MON_MGR_RAM_GB) if ceph else 0
        return {key: math.ceil(value * HYPERVISOR_CPU_OVERHEAD + value) + ceph_vcpu if key == "vcpu" else value + HYPERVISOR_RAM_GB * physical_nodes + ceph_ram if key == "ram_gb" else value for key, value in total.items()}

    talca_cluster_required = cluster_resources(vm_total["Talca"], T11_TALCA_NODES, ceph=True)
    talca_cluster_required_3x = cluster_resources(vm_total_3x["Talca"], T11_TALCA_NODES, ceph=True)
    concepcion_cluster_required = cluster_resources(vm_total["Concepción"], 1)
    concepcion_cluster_required_3x = cluster_resources(vm_total_3x["Concepción"], 1)
    t11_talca_n1 = {"vcpu": (T11_TALCA_NODES - 1) * T11_TALCA_NODE_VCPU, "ram_gb": (T11_TALCA_NODES - 1) * T11_TALCA_NODE_RAM_GB, "disk_gb": T11_TALCA_NODES * CEPH_OSDS_PER_NODE * T11_TALCA_OSD_GB // CEPH_REPLICAS}
    t11_concepcion = {"vcpu": T11_CONCEPCION_VCPU, "ram_gb": T11_CONCEPCION_RAM_GB, "disk_gb": T11_CONCEPCION_RAID10_DISKS * T11_CONCEPCION_SSD_GB // 2}
    talca_util_current = {key: talca_cluster_required[key] / t11_talca_n1[key] for key in ("vcpu", "ram_gb", "disk_gb")}
    talca_util_3x = {key: talca_cluster_required_3x[key] / t11_talca_n1[key] for key in ("vcpu", "ram_gb", "disk_gb")}
    min_node_3x = {"vcpu": ceil_int(talca_cluster_required_3x["vcpu"] / 2), "ram_gb": ceil_int(talca_cluster_required_3x["ram_gb"] / 2), "disk_gb": ceil_int(talca_cluster_required_3x["disk_gb"])}

    temp_gb_day = temp_messages_day * TEMP_RECORD_BYTES / 1_000_000_000
    obs_gb_day = {site: (OBS_NODES[site] + OBS_STANDBY_NODES[site] * OBS_STANDBY_FACTOR) * OBS_MB_PER_NODE_DAY / 1000 for site in OBS_NODES}
    links = {"Talca": (20.0, 5.0, T11_SATELLITE_MBPS, "D-03", "D-04", "D-06"), "Concepción": (10.0, 3.0, T11_SATELLITE_MBPS, "D-03", "D-04", "D-06"), "Cada cross-docking": (T11_SATELLITE_MBPS, 2.0, None, "D-06", "D-04", None)}
    # Los equipos de reparto se actualizan donde estaciona su camión, según SV-03; los de preventa, por MDM sobre la red móvil.
    truck_devices_talca = ceil_int(truck_devices * S49_TALCA_SHARE)
    site_update_devices = {"Talca": warehouse_terminals["Talca"] + truck_devices_talca, "Concepción": warehouse_terminals["Concepción"] + truck_devices - truck_devices_talca, "Cada cross-docking": S35_CROSS_USERS_PER_DOCK}
    fleet_device_mb = RUTA_PEOR_CLIENTES * evidence_kb / 1024 + OFFLINE_ROUTE_MB
    min_sync_mbps = fleet_device_mb * 8 / (REQ_SYNC_DISPOSITIVO_MIN * 60)
    fleet_sync_mbps = CAMIONES_TOTAL * fleet_device_mb * 8 / (3 * 3600)
    fleet_peak_hour_devices = CAMIONES_TOTAL / 3 * S51_CONCENTRATION_FACTOR
    fleet_peak_hour_mbps = fleet_peak_hour_devices * fleet_device_mb * 8 / 3600
    fleet_peak_site_mbps = {"Talca": fleet_peak_hour_mbps * S49_TALCA_SHARE,
                            "Concepción": fleet_peak_hour_mbps * (1 - S49_TALCA_SHARE)}
    site_data_day: dict[str, dict[str, float]] = {}
    link_rows: dict[str, dict[str, float | str | None]] = {}
    for site in site_tps_peak:
        principal, backup, satellite, principal_code, backup_code, satellite_code = links[site]
        change_day = components[site]["movement_data_gb"] / (LOCAL_HORIZON_MONTHS * 30)
        changes_wal = change_day * WAL_FACTOR
        broker = change_day * BROKER_FACTOR_OF_CHANGES
        temp_site = CAMERA_POINTS_SITE.get(site, 0) * (24 * 60 / TEMP_MINUTES) * TEMP_RECORD_BYTES / 1_000_000_000
        observability = obs_gb_day[site]
        incremental = change_day
        daily_replicable = changes_wal + broker + temp_site + observability + incremental
        office_gb_day = OFICINA_PERSONAS * OFFICE_MB_PER_USER_H * 18 / 1000 if site == "Talca" else 0.0
        continuous = daily_replicable * 8_000 / 86_400
        guide_messages = dte_peak_day * (S49_TALCA_SHARE if site == "Talca" else 1 - S49_TALCA_SHARE if site == "Concepción" else 1.0)
        identity_messages = (sum(warehouse_terminals.values()) + preventa_devices + truck_devices + cross_park) * IDENTITY_MESSAGES_PER_DEVICE_DAY
        priority_continuous = (changes_wal + broker + temp_site) * 8_000 / 86_400 + (guide_messages * 2 + identity_messages) * PRIORITY_MESSAGE_KB / 1_000_000 * 8_000 / 86_400
        office_mbps = office_gb_day * 8_000 / (18 * 3600) if site == "Talca" else 0.0
        sync_mbps = fleet_peak_site_mbps.get(site, 0.0)
        hour_loaded_regime = continuous * S51_CONCENTRATION_FACTOR + office_mbps + sync_mbps
        hour_loaded_peak = continuous * S51_CONCENTRATION_FACTOR * factor_peak + office_mbps + sync_mbps
        drain = daily_replicable * 8_000 / (REQ_SYNC_CD_H * 3600)
        worst = hour_loaded_regime + drain
        full_backup_gb = local_db_3x[site]
        app_update_gb = APP_UPDATE_GB_PER_DEVICE * site_update_devices[site]
        sunday_capacity_gb = principal * BACKUP_FULL_WINDOW_H * 3600 / 8_000
        app_hours = (full_backup_gb + app_update_gb) * 8_000 / principal / 3600
        remaining_for_os = max(0.0, sunday_capacity_gb - full_backup_gb - app_update_gb)
        os_batch_devices = math.floor(remaining_for_os / OS_UPDATE_GB_PER_DEVICE) if site_update_devices[site] else 0
        os_batch_devices = max(1, os_batch_devices) if site_update_devices[site] else 0
        os_batch_hours = (full_backup_gb + app_update_gb + os_batch_devices * OS_UPDATE_GB_PER_DEVICE) * 8_000 / principal / 3600 if site_update_devices[site] else 0.0
        os_sundays = math.ceil(site_update_devices[site] / os_batch_devices) if os_batch_devices else 0
        site_data_day[site] = {"change_day": change_day, "changes_wal": changes_wal, "broker": broker, "temperature": temp_site, "observability": observability, "incremental": incremental, "daily_replicable": daily_replicable, "office_gb_day": office_gb_day, "continuous_mbps": continuous, "priority_continuous_mbps": priority_continuous, "office_mbps": office_mbps, "sync_mbps": sync_mbps, "hour_loaded_regime": hour_loaded_regime, "hour_loaded_peak": hour_loaded_peak, "drain_mbps": drain, "worst": worst, "full_backup_gb": full_backup_gb, "app_update_gb": app_update_gb, "app_hours": app_hours, "os_batch_devices": os_batch_devices, "os_batch_hours": os_batch_hours, "os_sundays": os_sundays, "sunday_capacity_gb": sunday_capacity_gb}
        link_rows[site] = {"principal": principal, "backup": backup, "satellite": satellite, "principal_code": principal_code, "backup_code": backup_code, "satellite_code": satellite_code, "principal_util": worst / principal, "backup_util": drain / backup, "satellite_util": drain / satellite if satellite else None}

    year3_link_rows: dict[str, float] = {}
    three_x_link_rows: dict[str, float] = {}
    for site in site_tps_peak:
        row = site_data_day[site]
        changes = (row["changes_wal"] + row["broker"] + row["incremental"]) * y3_lines_factor
        y3_daily = changes + row["temperature"] + row["observability"]
        y3_continuous = y3_daily * 8_000 / 86_400
        y3_drain = y3_daily * 8_000 / (REQ_SYNC_CD_H * 3600)
        year3_link_rows[site] = y3_continuous * S51_CONCENTRATION_FACTOR + row["office_mbps"] + row["sync_mbps"] + y3_drain
        three_x_daily = ((row["changes_wal"] + row["broker"] + row["incremental"]) * REQ_CRECIMIENTO
                         + row["temperature"] + row["observability"])
        three_x_continuous = three_x_daily * 8_000 / 86_400
        three_x_drain = three_x_daily * 8_000 / (REQ_SYNC_CD_H * 3600)
        three_x_link_rows[site] = (three_x_continuous * S51_CONCENTRATION_FACTOR
                                   + row["office_mbps"] + row["sync_mbps"] + three_x_drain)

    operational_concurrency["portal régimen"] = portal_regime_concurrent
    operational_concurrency["portal cota extrema"] = portal_extreme_concurrent
    device_mb_avg_normal = RUTA_PROMEDIO_NORMAL * evidence_kb / 1024 + OFFLINE_ROUTE_MB
    device_mb_avg_peak = RUTA_PROMEDIO_PEAK * evidence_kb / 1024 + OFFLINE_ROUTE_MB
    help_contacts_month = internal_users * S53_HELP_CONTACTS_PER_PERSON
    contacts_day = help_contacts_month / dispatch_days
    loaded_contacts_hour = contacts_day * S53_HELP_PEAK_SHARE
    other_contacts_hour = contacts_day * (1 - S53_HELP_PEAK_SHARE) / 17
    help_loaded_agents = agents_for_service(loaded_contacts_hour, S53_HELP_AHT_MIN * 60)
    help_other_agents = agents_for_service(other_contacts_hour, S53_HELP_AHT_MIN * 60)
    weekly_position_hours = (help_loaded_agents + 17 * help_other_agents) * 6
    help_people_hours = ceil_int(weekly_position_hours / JORNADA_SEMANAL_H)
    help_positions_max = help_loaded_agents
    help_people = max(help_people_hours, help_positions_max)
    peak_extra_position_hours = (6 * 6) + 24  # 22:00–04:00 de lunes a sábado y domingo
    peak_extra_people = ceil_int(peak_extra_position_hours / JORNADA_SEMANAL_H)
    help_peak_people = help_people + peak_extra_people
    persons_per_position_42h = ceil_int(168 / 42)
    persons_per_position_40h = ceil_int(168 / 40)
    noc_soc_persons_42h = 2 * persons_per_position_42h
    noc_soc_persons_40h = 2 * persons_per_position_40h
    total_operation_people_42h = help_people + noc_soc_persons_42h
    total_operation_people_40h = help_people + noc_soc_persons_40h
    total_operation_peak_people_42h = help_peak_people + noc_soc_persons_42h
    total_operation_peak_people_40h = help_peak_people + noc_soc_persons_40h

    year3_peak = peak_row(year3_peak_rows)
    # El plan de capacidad usa una sola base por métrica: la dimensión 3 total
    # se proyecta con el factor de pedidos de la Tabla 14.1.
    year3_cloud_load = peak_tps * (Y3_PEDIDOS_MES / PEDIDOS_MES)
    year3_talca_tps = site_tps_peak["Talca"] * y3_lines_factor
    year3_cross_tps = peak_row(year3_peak_rows, "cross-docking")["cross-docking"]
    three_x_cross_tps = site_tps_peak["Cada cross-docking"] * REQ_CRECIMIENTO
    year3_evidence_gb = evidence_gb_year * (Y3_PEDIDOS_MES / PEDIDOS_MES)
    year3_help_contacts = help_contacts_month * (Y3_CD_PERSONAL / PERSONAL_CD)
    y3_cd = Y3_CD_PERSONAL / PERSONAL_CD
    year3_talca_terminals = with_reserve(S34_FREEZER_CREW_TALCA * y3_cd) + with_reserve((PREPARADORES_NOCHE_TALCA - S34_FREEZER_CREW_TALCA) * y3_cd)

    task_capacity_tps = 0.70 / (FARGATE_CPU_MS / 1000)
    cloud_normal_load = max(row["nube"] + row["portal"] for row in normal_rows)
    cloud_peak_load = max(row["nube"] + row["portal"] for row in peak_rows)
    cloud_test_load = cloud_peak_load * REQ_PRUEBA_CARGA
    peak_noon_cloud = peak_rows[12]["nube"]
    extreme_portal_load = peak_noon_cloud + portal_extreme_requests_s
    sensitivity_regime_load = normal_rows[12]["nube"] + portal_sensitivity_regime_requests_s
    sensitivity_extreme_load = peak_noon_cloud + portal_sensitivity_extreme_requests_s
    fargate_tasks = {
        "régimen": max(FARGATE_TASKS_MIN, ceil_int(cloud_normal_load / task_capacity_tps)),
        "peak": max(FARGATE_TASKS_MIN, ceil_int(cloud_peak_load / task_capacity_tps)),
        "prueba": max(FARGATE_TASKS_MIN, ceil_int(cloud_test_load / task_capacity_tps)),
        "cota": max(FARGATE_TASKS_MIN, ceil_int(extreme_portal_load / task_capacity_tps)),
        "sensibilidad régimen": max(FARGATE_TASKS_MIN, ceil_int(sensitivity_regime_load / task_capacity_tps)),
        "sensibilidad cota": max(FARGATE_TASKS_MIN, ceil_int(sensitivity_extreme_load / task_capacity_tps)),
    }

    base_concentration = {"Talca": max(row["Talca"] for row in peak_rows), "Concepción": max(row["Concepción"] for row in peak_rows), "Cada cross-docking": max(row["cross-docking"] for row in peak_rows), "Nube + portal": cloud_peak_load}
    offered_capacity = {"Talca": t11_talca_n1["vcpu"] * 0.70 / (CPU_MS["app"] / 1000), "Concepción": t11_concepcion["vcpu"] * 0.70 / (CPU_MS["app"] / 1000), "Cada cross-docking": CROSSDOCK_BASE_VCPU * 0.70 / (CPU_MS["app"] / 1000), "Nube + portal": FARGATE_TASKS_MAX * task_capacity_tps}
    concentration_break = {site: offered_capacity[site] / base for site, base in base_concentration.items()}
    dte_scenarios = {"22:00–05:30": 27_000 / dte_peak_day, "últimas 3,5 h": 12_600 / dte_peak_day, "05:30–07:00": 5_400 / dte_peak_day}
    max_contacts_7 = None
    for contacts in range(1, 10001):
        daily = contacts / dispatch_days
        loaded = daily * S53_HELP_PEAK_SHARE
        other = daily * (1 - S53_HELP_PEAK_SHARE) / 17
        if agents_for_service(loaded, S53_HELP_AHT_MIN * 60) > help_loaded_agents or agents_for_service(other, S53_HELP_AHT_MIN * 60) > help_other_agents:
            max_contacts_7 = contacts - 1
            break

    def integration_markdown() -> list[str]:
        rows = ["| Integración | Mensajes/día normal | Mensajes/día peak | Origen del volumen |", "|---|---:|---:|---|"]
        rows += [f"| {code} {name} | {fmt(normal, 0)} | {fmt(peak, 0)} | {source} |" for code, name, normal, peak, source in integration_rows]
        rows.append(f"| **Total** | **{fmt(message_total, 0)}** | **{fmt(message_peak, 0)}** | **15 integraciones; portal y API interna fuera** |")
        return rows

    def hourly_markdown() -> list[str]:
        rows = ["| Hora | Talca normal / peak | Concepción normal / peak | Cross-docking normal / peak | Nube normal / peak | Portal normal / peak | Total normal / peak |", "|---:|---:|---:|---:|---:|---:|---:|"]
        for normal, peak in zip(normal_rows, peak_rows):
            rows.append(f"| {int(normal['hora']):02d}:00 | {fmt(normal['Talca'])} / {fmt(peak['Talca'])} | {fmt(normal['Concepción'])} / {fmt(peak['Concepción'])} | {fmt(normal['cross-docking'])} / {fmt(peak['cross-docking'])} | {fmt(normal['nube'])} / {fmt(peak['nube'])} | {fmt(normal['portal'])} / {fmt(peak['portal'])} | {fmt(normal['total'])} / {fmt(peak['total'])} |")
        return rows

    def vm_markdown() -> list[str]:
        rows = ["| VM/equipo | Requerido actual | Requerido 3× | Sitio |", "|---|---|---|---|"]
        for site, vm_map in vm_sets.items():
            for name, res in vm_map.items():
                rows.append(f"| {name} | {resource_line(res)} | {resource_line(vm_sets_3x[site][name])} | {site} |")
        rows.append(f"| Mini-PC | {resource_line(cross_vm)} | {resource_line(cross_vm_3x)} | Cada cross-docking |")
        return rows

    lines = [
        "# Memoria de cálculo de dimensionamiento", "",
        "Los cálculos siguientes expresan la fórmula, la sustitución y el resultado con unidades. Las tasas se obtienen del perfil de 24 horas y los redondeos de integraciones se aplican antes de sumar.", "",
        "## Entradas y control de calendario", "",
        f"Los días equivalentes son 31.000 pedidos/mes ÷ 1.400 entregas/día = **{fmt(dispatch_days)} días**; el control cruzado es 2.100 viajes ÷ 96 camiones = **{fmt(crosscheck_days)} días**. El factor peak es 2.600 ÷ 1.400 = **{fmt(factor_peak, 3)}**. Los totales anuales se obtienen como 12 × el volumen mensual de la Tabla 14.1.", "",
        "## Dimensiones 1–3: transacciones por segundo", "",
        "Se calcula el máximo horario de cada régimen para evitar sumar ventanas que no coinciden. Cross-docking opera de 03:00 a 06:00: tres operaciones por entrega entre 03:00 y 05:00 y el despacho entre 05:00 y 06:00. SV-04 se aplica sólo en la hora cargada de cada tramo.",
        f"En régimen normal el máximo horario es **{fmt(normal_tps)} TPS a las {int(normal_max['hora']):02d}:00**. Los máximos por lugar son Talca {fmt(normal_place_max['Talca']['Talca'])}, Concepción {fmt(normal_place_max['Concepción']['Concepción'])}, cada cross-docking {fmt(normal_place_max['cross-docking']['cross-docking'])}, nube {fmt(normal_place_max['nube']['nube'])} y portal {fmt(normal_place_max['portal']['portal'])} TPS.",
        f"En septiembre el máximo es **{fmt(peak_tps)} TPS a las {int(peak_max['hora']):02d}:00**. Por lugar: Talca {fmt(peak_place_max['Talca']['Talca'])}, Concepción {fmt(peak_place_max['Concepción']['Concepción'])}, cada cross-docking {fmt(peak_place_max['cross-docking']['cross-docking'])}, nube {fmt(peak_place_max['nube']['nube'])} y portal {fmt(peak_place_max['portal']['portal'])} TPS.",
        f"La dimensión 2 toma el mayor total horario dentro de 05:30–07:00: las horas 05:00 y 06:00, suponiendo uniforme el tramo 05:30–06:00; resulta **{fmt(dim2_peak)} TPS** peak y **{fmt(dim2_normal)} TPS** normal. Los {fmt(dte_peak_day, 0)} DTE/día peak son el total de documentos tributarios electrónicos, no sólo guías; tratarlos todos como guías que deben emitirse antes de la salida constituye una cota conservadora. Para el portal, 2.600 ÷ 9 × 2 por SV-04 × 60 ÷ 3.600 = {fmt(portal_regime_requests_s)} solicitudes/s.",
        f"La prueba BTT RT-09.06 aplica una sola vez 1,5 × {fmt(peak_tps)} = **{fmt(load_test_tps)} TPS**.", "",
        "### Perfil horario de 24 horas", "",
        "La tabla conserva las tasas por hora y por lugar. La fila máxima explica la dimensión 1 y la dimensión 3.", *hourly_markdown(), "",
        f"El máximo normal ocurre a las {int(normal_max['hora']):02d}:00 y el de septiembre a las {int(peak_max['hora']):02d}:00; el portal aporta {fmt(normal_max['portal'])} y {fmt(peak_max['portal'])} TPS en esa hora, mientras la nube aporta {fmt(normal_max['nube'])} y {fmt(peak_max['nube'])}. El promedio diario oculta la coincidencia de preventa, reparto y sesiones del portal.", "",
        "## Dimensiones 4–6: personas, concurrencia y dispositivos", "",
        f"Las personas o entidades registradas son (640 + 160) + 14.200 + 180 = **{fmt_int(registered)}**. La concurrencia máxima por ventana es noche {fmt_int(operational_concurrency['noche'])}, despacho {fmt_int(operational_concurrency['despacho'])}, día sin portal {fmt_int(operational_concurrency['día sin portal'])}, sincronización {fmt_int(operational_concurrency['sincronización'])}, y día con portal en régimen **{fmt(concurrency_regime)}**; la cota extrema del portal es **{fmt(concurrency_extreme)}**.",
        "La dimensión 6 es 62 preventistas + 96 equipos de reparto = **158 dispositivos de terreno**. El parque a proveer se informa aparte.", "",
        "## Dimensiones 7–10: almacenamiento y migración", "",
        f"El almacenamiento transaccional parte de {fmt_int(line_event_records_month)} eventos ({fmt_int(LINEAS_MES)} líneas × 5), {fmt_int(picking_records_month)} operaciones ({fmt_int(LINEAS_MES)} líneas × 2), {fmt_int(delivery_records_month)} operaciones ({fmt_int(PEDIDOS_MES)} pedidos × 5) y {fmt_int(movement_records_month)} movimientos ({fmt_int(LINEAS_MES)} líneas + {fmt_int(PALLETS_MES)} pallets + {fmt_int(POSICIONES_CONTADAS_MES)} conteos + {fmt_int(RECEPCIONES_MES)} recepciones). La fórmula es (({fmt_int(line_event_records_month)} + {fmt_int(picking_records_month)} + {fmt_int(delivery_records_month)}) × 1 KB + {fmt_int(movement_records_month)} × 0,5 KB) × 2 × 12 = **{fmt(transactional_gb_year)} GB/año**; seis años acumulan **{fmt(transactional_gb_year * 6)} GB** como cota de retención.",
        f"La evidencia es 30 KB + 200 KB × (1 + 900 ÷ 31.000) = **{fmt(evidence_kb)} KB por entrega**; genera **{fmt(evidence_gb_year)} GB/año** y **{fmt(evidence_gb_peak_month)} GB en el mes peak**.",
        f"Temperatura: {fmt_int(camera_messages_day)} lecturas/día de las cámaras + {fmt_int(thermograph_messages_day)} de los termógrafos de camión = {fmt_int(temp_messages_day)} mensajes/día; con {TEMP_RECORD_BYTES} bytes por lectura son {fmt(temp_raw_gb_year)} GB/año crudos y {fmt(temp_stored_gb_year)} GB/año almacenados, {fmt(temp_raw_gb_year * REQ_RET_TEMP_ANIOS)} GB crudos en 5 años. Posición: {fmt_int(position_records_year)} eventos/año, {fmt(position_raw_gb_year)} GB crudos y {fmt(position_stored_gb_year)} GB almacenados en 12 meses; cada evento usa {POSITION_RECORD_BYTES} bytes. La copia almacenada usa factor 0,25.",
        f"La migración suma maestros {fmt(historical_domains['maestros completos'], 0)} KB, ventas y pedidos {fmt(historical_domains['ventas y pedidos, 3 años'], 0)} KB, inventario y movimientos {fmt(historical_domains['inventario y movimientos, 2 años'], 0)} KB, recepciones con lote {fmt(historical_domains['recepciones con lote, 5 años'], 0)} KB y cuentas por cobrar {fmt(historical_domains['cuentas por cobrar, 2 años'], 0)} KB. Con factor 2: **{fmt(historical_gb)} GB**, sensibilidad **{fmt(historical_low_gb)}–{fmt(historical_high_gb)} GB**.", "",
        "## Dimensiones 11–12: integraciones y enlaces", "",
        f"El apartado 4.1 contiene 15 integraciones. La dimensión 11 suma **{fmt(message_total, 0)} mensajes/día normal** y **{fmt(message_peak, 0)} peak**; portal y llamadas internas a la API quedan fuera. El EDI actual es cero; desde enero de 2029 opera todos los días y usa la cota de 11 % de pedidos en régimen y en peak. La pasarela de pago se acota con un pago electrónico por entrega y dos mensajes por pago.", *integration_markdown(), "",
        "El drenaje contiene cambios con WAL, vaciado del broker, telemetría, observabilidad e incremental de respaldo acumulados durante 24 horas; no incluye tráfico de oficina. La prioridad continua suma WAL, broker, telemetría crítica, guías, SII e identidad; cada mensaje de guía, respuesta SII e identidad usa la cota de 1 KB. El peor caso suma la hora cargada con oficina y la sincronización de la flota cuando corresponde. D-06 se calcula con 2 Mbps de subida mínima supuesta, un parámetro conservador de diseño que se confirma en la instalación."]
    for site in site_tps_peak:
        row = site_data_day[site]
        link = link_rows[site]
        paths = f"{link['principal_code']} {fmt(link['principal_util'] * 100)} % y {link['backup_code']} para drenaje {fmt(link['backup_util'] * 100)} %"
        if site != "Cada cross-docking":
            paths += f" y {link['satellite_code']} para drenaje {fmt(link['satellite_util'] * 100)} %"
        lines.append(f"- {site}: régimen cargado {fmt(row['hour_loaded_regime'])} Mbps; prioridad continua {fmt(row['priority_continuous_mbps'], 3)} Mbps; drenaje {fmt(row['drain_mbps'])} Mbps; peor caso {fmt(row['worst'])} Mbps; {paths}. Datos acumulables: {fmt(row['daily_replicable'])} GB/día.")
    lines += [
        f"El retorno se reparte según SV-03: {fmt(fleet_peak_hour_devices, 0)} camiones en la hora punta total de 17:00–20:00 requieren {fmt(fleet_peak_site_mbps['Talca'])} Mbps en Talca y {fmt(fleet_peak_site_mbps['Concepción'])} Mbps en Concepción para Wi-Fi y enlace; la flota completa requiere {fmt(fleet_peak_hour_mbps)} Mbps en esa hora y {fmt(fleet_sync_mbps)} Mbps agregados en las tres horas. Cada dispositivo queda sincronizado en diez minutos.", "",
        "## Dimensiones 13–14: terreno y sincronización", "",
        f"La peor ruta genera 34 × {fmt(evidence_kb)} KB ÷ 1.024 + 2 MB = **{fmt(fleet_device_mb)} MB** por dispositivo. Una ruta promedio genera **{fmt(device_mb_avg_normal)} MB** normal y **{fmt(device_mb_avg_peak)} MB** en septiembre.",
        f"Con {fmt(fleet_device_mb)} MB, el umbral de quiebre de sincronización es {fmt(fleet_device_mb)} MB × 8 ÷ 600 s = **{fmt(min_sync_mbps)} Mbps efectivos**; el diseño exige que cada dispositivo disponga de al menos ese caudal.", "",
        "## Dimensiones 15–16: mesa de ayuda y operación", "",
        f"La mesa recibe {fmt_int(help_contacts_month)} contactos/mes en el escenario de 2,5 contactos por persona interna. La hora cargada concentra el 25 %: {fmt(loaded_contacts_hour)} contactos/hora; las otras 17 horas reciben {fmt(other_contacts_hour)} cada una. Erlang C exige {help_loaded_agents} agentes en la hora cargada y {help_other_agents} en las demás; la suma semanal es {fmt(weekly_position_hours, 0)} horas-posición y requiere **{help_people} personas** a 42 horas semanales.",
        f"La operación 24×7 de septiembre y diciembre requiere ocho personas para un NOC y un SOC de una posición cada uno: 168 ÷ 42 = {persons_per_position_42h} personas por posición. Desde el 26-04-2028, 168 ÷ 40 = {persons_per_position_40h}; el total mesa más NOC/SOC es **{total_operation_people_42h}** y luego **{total_operation_people_40h} personas**.", "",
        "## Capacidad on-premise", "",
        "La base local incluye maestros, stock, lotes presentes y movimientos de cuatro meses; el histórico de retención vive en la nube. La RAM de la base es 4 GB más 25 % del tamaño a 3×; cada VM suma base de sistema y carga.", *vm_markdown(),
        f"Las VMs de Talca suman {resource_line(vm_total['Talca'])}; con hipervisor (+15 % vCPU y 2 GB RAM por nodo) y Ceph (3 vCPU y 10 GB RAM por nodo) requieren {resource_line(talca_cluster_required)} actual y {resource_line(talca_cluster_required_3x)} a 3×. VM-04 incluye {ERP_SYNC_PROCESSES} procesos erp-sync de {ERP_SYNC_RAM_MB_PER_PROCESS} MB. Las VMs de Concepción suman {resource_line(vm_total['Concepción'])}; con hipervisor requieren {resource_line(concepcion_cluster_required)} actual y {resource_line(concepcion_cluster_required_3x)} a 3×. Frente al T-11 con un nodo caído, Talca dispone de 64 vCPU, 128 GB RAM y 1.920 GB útiles: utilización {fmt(talca_util_current['vcpu'] * 100)} / {fmt(talca_util_current['ram_gb'] * 100)} / {fmt(talca_util_current['disk_gb'] * 100)} % actual y {fmt(talca_util_3x['vcpu'] * 100)} / {fmt(talca_util_3x['ram_gb'] * 100)} / {fmt(talca_util_3x['disk_gb'] * 100)} % a 3×. Concepción utiliza {fmt(concepcion_cluster_required['vcpu'] / t11_concepcion['vcpu'] * 100)} / {fmt(concepcion_cluster_required['ram_gb'] / t11_concepcion['ram_gb'] * 100)} / {fmt(concepcion_cluster_required['disk_gb'] / t11_concepcion['disk_gb'] * 100)} % actual y {fmt(concepcion_cluster_required_3x['vcpu'] / t11_concepcion['vcpu'] * 100)} / {fmt(concepcion_cluster_required_3x['ram_gb'] / t11_concepcion['ram_gb'] * 100)} / {fmt(concepcion_cluster_required_3x['disk_gb'] / t11_concepcion['disk_gb'] * 100)} % a 3×. La configuración mínima N+1 y 3× por nodo es {min_node_3x['vcpu']} vCPU, {min_node_3x['ram_gb']} GB RAM y {min_node_3x['disk_gb']} GB de OSD por nodo; la redundancia fija el mínimo.", "",
        "## Capacidad en nube", "",
        f"El perfil de API atiende aplicaciones y portales N-01 a N-03. Una tarea Fargate entrega 0,70 ÷ 0,05 = **{fmt(task_capacity_tps)} solicitudes/s**. Régimen: {fmt(cloud_normal_load)} solicitudes/s y {fargate_tasks['régimen']} tareas; peak: {fmt(cloud_peak_load)} y {fargate_tasks['peak']}; RT-09.06: {fmt(cloud_test_load)} y {fargate_tasks['prueba']}; cota extrema: {fmt(extreme_portal_load)} y {fargate_tasks['cota']}; sensibilidad de 120 solicitudes por sesión: {fmt(sensitivity_regime_load)} y {fargate_tasks['sensibilidad régimen']} en régimen, {fmt(sensitivity_extreme_load)} y {fargate_tasks['sensibilidad cota']} en cota. El techo es ocho tareas.", "",
        "## Ventana dominical", ""]
    for site in site_tps_peak:
        row = site_data_day[site]
        lines.append(f"- {site}: respaldo completo a 3× {fmt(row['full_backup_gb'])} GB y aplicación {fmt(row['app_update_gb'])} GB requieren {fmt(row['app_hours'])} h; la tanda de sistema operativo es {row['os_batch_devices']} equipos, {fmt(row['os_batch_hours'])} h por domingo y una ronda completa ocupa {row['os_sundays']} domingos. La aplicación se actualiza en un domingo por sitio; el sistema operativo se distribuye en tandas dominicales, con cadencia semestral.")
    lines += ["", "## Crecimiento, umbrales y cuello de botella", "", f"Año 3 usa {fmt_int(Y3_PEDIDOS_MES)} pedidos/mes ({fmt_int(Y3_PEDIDOS_MES)} ÷ {fmt_int(PEDIDOS_MES)} = {fmt(Y3_PEDIDOS_MES / PEDIDOS_MES)}×), {fmt_int(Y3_LINEAS_MES)} líneas/mes ({fmt(Y3_LINEAS_MES / LINEAS_MES)}×), {fmt_int(Y3_ENTREGAS_NORMAL_DIA)}/{fmt_int(Y3_ENTREGAS_PEAK_DIA)} entregas/día y {fmt_int(Y3_DTE_MES)} DTE/mes. Por separado, 3× es 93.000 pedidos, 780.000 líneas, 4.200/7.800 entregas y 102.000 DTE mensuales.", f"La tabla de capacidad del año 3 se obtiene con una base por métrica: WMS Talca {fmt(site_tps_peak['Talca'])} × ({fmt_int(Y3_LINEAS_MES)} ÷ {fmt_int(LINEAS_MES)}) = {fmt(year3_talca_tps)} TPS; cross-docking {fmt(site_tps_peak['Cada cross-docking'])} TPS actual, {fmt(year3_cross_tps)} en año 3 y {fmt(three_x_cross_tps)} a 3×; nube más portal {fmt(peak_tps)} × ({fmt_int(Y3_PEDIDOS_MES)} ÷ {fmt_int(PEDIDOS_MES)}) = {fmt(year3_cloud_load)} solicitudes/s; evidencia {fmt(evidence_gb_year)} × ({fmt_int(Y3_PEDIDOS_MES)} ÷ {fmt_int(PEDIDOS_MES)}) = {fmt(year3_evidence_gb)} GB/año; Talca usa {fmt(year3_link_rows['Talca'])} Mbps en el peor caso y {fmt(three_x_link_rows['Talca'])} Mbps a 3×; bodega Talca usa {year3_talca_terminals} terminales; mesa conserva {fmt_int(year3_help_contacts)} contactos/mes. La columna 3× cubre carga técnica, no aumenta el parque de personas.", f"El umbral de SV-04, expresado como múltiplo de la tasa peak antes de saturar la capacidad calculada, es Talca {fmt(concentration_break['Talca'])}×, Concepción {fmt(concentration_break['Concepción'])}×, cada cross-docking {fmt(concentration_break['Cada cross-docking'])}× y nube más portal {fmt(concentration_break['Nube + portal'])}×. La cota extrema combinada requiere {fargate_tasks['cota']} tareas; la sensibilidad exige {fargate_tasks['sensibilidad cota']} y se mantiene bajo el techo de ocho.", f"Para los {fmt(dte_peak_day, 0)} DTE peak, el tiempo máximo por documento es 27.000 ÷ {fmt(dte_peak_day, 0)} = {fmt(dte_scenarios['22:00–05:30'])} s si se reparte en toda la preparación; {fmt(dte_scenarios['últimas 3,5 h'])} s si se concentra al final; y {fmt(dte_scenarios['05:30–07:00'])} s si se conserva la práctica actual. El diseño emite el documento cuando confirma la carga, durante la noche. Se detectan documentos pendientes frente a la hora de salida de cada camión; se resuelve priorizando la cola y reconciliando el folio, sin crear otro emisor: el ERP sigue siendo el único emisor y el documento acompaña el traslado.", f"Con la dotación de {help_loaded_agents} agentes en la hora cargada y {help_other_agents} en las demás, la mesa tolera {fmt_int(max_contacts_7)} contactos mensuales antes de requerir una posición adicional. Se observan percentiles 95, colas, errores, IOPS, Wi-Fi, ERP y drenaje en RT-09.06 y en la operación.", "", "## Fuentes de validación", "", "El perfilado confirma tamaños de registros y migración; la prueba de carga confirma CPU, residencia Fargate, concurrencia y tasas; la prueba de corte confirma drenaje y la prueba dominical confirma respaldo y actualizaciones. Ninguna de estas verificaciones reemplaza el valor de diseño declarado."]
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
