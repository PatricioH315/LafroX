"""Extrae del modelo financiero SD7 los datos de la presentacion final -> data/final.json.

Uso:  python -I tools/extract_final_data.py [ruta_al_xlsx]

Las celdas se ubican POR ETIQUETA (texto de la fila / columna), no por direccion fija, salvo
las series mensuales de CURVA S y FLUJO, que se ubican por la etiqueta de su fila.
Las cifras que no provienen del modelo (innovaciones: tipo y meta, criterios de calidad, problema, continuidad, equipo)
se copian de los subdocumentos y quedan en el bloque "documentos" del JSON. La EDT y la RBS vigentes salen de
tools/extract_edt_rbs.py (data/edt_rbs.json).
"""
import json
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

import openpyxl

DEFAULT_XLSX = (
    "C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Repositorios/Principal/LafroX-worktrees/"
    "sd7-corrigiendo/outputs/sd7-ajuste-20261122/LafroX_ModeloFinanciero_3_SD7.xlsx"
)
OUT = Path(__file__).resolve().parent.parent / "data" / "final.json"


def norm(s):
    s = str(s).replace("–", "-").replace("—", "-")
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return " ".join(s.upper().split())


class Book:
    def __init__(self, path):
        self.wb = openpyxl.load_workbook(path, data_only=True)
        self.path = path

    def ws(self, name):
        for w in self.wb.worksheets:
            if norm(w.title) == norm(name):
                return w
        raise KeyError(name)

    def find(self, sheet, label, col=None, start=1, exact=True):
        """Fila donde aparece la etiqueta (en la columna dada o en cualquiera)."""
        ws = self.ws(sheet)
        key = norm(label)
        for r in range(start, ws.max_row + 1):
            cols = [col] if col else range(1, min(ws.max_column, 20) + 1)
            for c in cols:
                v = ws.cell(r, c).value
                if isinstance(v, str) and (norm(v) == key if exact else key in norm(v)):
                    return r, c
        raise KeyError(f"{sheet}: {label}")

    def after(self, sheet, label, offset=1, **kw):
        r, c = self.find(sheet, label, **kw)
        return self.ws(sheet).cell(r, c + offset).value

    def row_series(self, sheet, row, c0, n=57):
        ws = self.ws(sheet)
        return [ws.cell(row, c0 + i).value or 0 for i in range(n)]


def r2(v, n=4):
    return round(float(v), n)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_XLSX
    bk = Book(path)
    uf = float(bk.after("PARAMETROS", "UF", 1))
    usd = float(bk.after("PARAMETROS", "Dolar", 1))
    d = {"fuente": {"archivo": Path(path).name, "ruta": path}}

    # ---------------------------------------------------------------- parametros
    P = lambda lbl: bk.after("PARAMETROS", lbl)
    d["parametros"] = {
        "uf_clp": uf,
        "usd_clp": usd,
        "horizonte_meses": int(P("Horizonte de evaluacion")),
        "inicio_proyecto": str(bk.ws("PARAMETROS").cell(*[bk.find("PARAMETROS", "Inicio del proyecto")[0], 3]).value)[:10],
        "iva": r2(P("IVA")),
        "impuesto": r2(P("impuestos")),
        "tasa_credito_mensual": r2(P("Tasa de Interes - credito de consumo")),
        "tasa_linea_mensual": r2(P("Tasa de interes - linea de credito")),
        "rentabilidad_maxima": r2(P("Rentabilidad Maxima")),
        "pct_bancario": r2(P("Porcentaje maximo financiamiento bancario")),
        "pct_propio": r2(P("Porcentaje maximo financiamiento propio")),
        "costo_capital_propio_anual": r2(P("Costo anual del capital propio")),
        "tasa_descuento_mensual": r2(P("Tasa de descuento mensual del proyecto"), 6),
        "capital_inicial_uf": float(P("Capital inicial del proyecto (UF)")),
        "mes_amortizacion_credito": int(P("Mes de amortizacion del credito bancario")),
        "factor_tarifa_rrhh": r2(P("Factor de tarifa de RR.HH. sobre el costo")),
        "hh_mes": float(P("HH Mes")),
    }

    # ---------------------------------------------------------------- resumen: tarifa / costo / margen
    S = "RESUMEN"
    r_imp, _ = bk.find(S, "Total de Implementacion", col=1)
    ws = bk.ws(S)
    r_sop = bk.find(S, "Total en Soporte", col=1)[0]
    r_proj = bk.find(S, "Total en Proyecto", col=1)[0]
    def trio(r, c0):
        return {"uf": r2(ws.cell(r, c0).value), "clp": round(ws.cell(r, c0 + 1).value), "usd": round(ws.cell(r, c0 + 2).value)}
    d["tarifa"] = {"implementacion": trio(r_imp, 7), "soporte": trio(r_sop, 7), "total": trio(r_proj, 7)}
    d["costo"] = {"implementacion": trio(r_imp, 2), "soporte": trio(r_sop, 2), "total": trio(r_proj, 2)}
    d["margen"] = {"implementacion": trio(r_imp, 12), "soporte": trio(r_sop, 12), "total": trio(r_proj, 12)}
    d["rentabilidad_nominal"] = r2(ws.cell(bk.find(S, "Rentabilidad nominal", col=11)[0], 12).value)

    cats = []
    for lbl, key in [
        ("Implementacion Recursos Humanos", "RR.HH. implementacion"),
        ("Soporte Recursos Humanos", "RR.HH. soporte"),
        ("Implementacion Adquisiciones", "Adquisiciones implementacion"),
        ("Implementacion Servicios", "Servicios implementacion"),
        ("Soporte Servicios", "Servicios soporte"),
        ("Implementacion Capacitaciones", "Capacitaciones"),
    ]:
        r = bk.find(S, lbl, col=1)[0]
        cats.append({"categoria": key, "costo_uf": r2(ws.cell(r, 2).value), "tarifa_uf": r2(ws.cell(r, 7).value)})
    d["estructura_costo"] = sorted(cats, key=lambda c: -c["costo_uf"])

    # ---------------------------------------------------------------- hitos y operacion (FINANCIAMIENTO)
    F = "FINANCIAMIENTO"
    wf = bk.ws(F)
    r_h1 = bk.find(F, "H1", col=5)[0]
    pct = {}
    rp = bk.find("PARAMETROS", "H1", col=2)[0]
    wp = bk.ws("PARAMETROS")
    for i in range(12):
        pct[f"H{i+1}"] = r2(wp.cell(rp + i, 4).value)
    hitos = []
    for i in range(12):
        r = r_h1 + i
        h = wf.cell(r, 5).value
        hitos.append({
            "hito": h, "mes": int(wf.cell(r, 6).value), "pct": pct[h], "uf": r2(wf.cell(r, 8).value),
            "iva_uf": r2(wf.cell(r, 9).value), "total_con_iva_uf": r2(wf.cell(r, 10).value),
        })
    d["hitos"] = hitos
    r_op = bk.find(F, "Hito de operacion", col=5)[0]
    d["operacion"] = {"cuota_uf_mes": r2(wf.cell(r_op, 8).value), "mes_desde": 21, "mes_hasta": 56,
                      "texto": wf.cell(r_op, 7).value, "iva_uf": r2(wf.cell(r_op, 9).value)}
    # meses de operacion a partir del texto "Desde M21 hasta M56"
    import re
    m = re.search(r"M(\d+).*M(\d+)", str(wf.cell(r_op, 7).value))
    if m:
        d["operacion"]["mes_desde"], d["operacion"]["mes_hasta"] = int(m.group(1)), int(m.group(2))
    d["operacion"]["meses"] = d["operacion"]["mes_hasta"] - d["operacion"]["mes_desde"] + 1

    # financiamiento
    r_cred = bk.find(F, "Monto Credito", col=5)[0]
    d["financiamiento"] = {
        "credito_uf": float(wf.cell(r_cred, 6).value), "aporte_socios_uf": float(wf.cell(r_cred + 1, 6).value),
        "tasa_credito_mensual": d["parametros"]["tasa_credito_mensual"],
        "costo_capital_propio_anual": d["parametros"]["costo_capital_propio_anual"],
        "pct_bancario": d["parametros"]["pct_bancario"], "pct_propio": d["parametros"]["pct_propio"],
        "cuotas": int(bk.after(F, "Cuotas", 1, col=1)),
        "tasa_descuento_mensual": d["parametros"]["tasa_descuento_mensual"],
        "tasa_descuento_anual": r2(bk.after("SENSIBILIDAD", "Tasa de descuento anual", 1, col=2)),
    }

    # ---------------------------------------------------------------- indicadores
    I = "INDICADORES"
    iv = lambda lbl: float(bk.after(I, lbl, 1, col=1))
    d["indicadores"] = {
        "van_sin_impuestos_uf": r2(iv("VAN sin impuestos")),
        "impuestos_uf": r2(iv("Valor de impuestos")),
        "van_sobre_impuestos_uf": r2(iv("VAN sobre impuestos")),
        "tir_sin_imp_mensual": r2(iv("TIR sin impuestos")),
        "tir_sin_imp_anual": r2(iv("TIR sin impuestos anual")),
        "tir_post_imp_mensual": r2(iv("TIR del proyecto sobre de impuesto")),
        "tir_post_imp_anual": r2(iv("TIR anual del proyecto sobre impuesto")),
        "punto_quiebre_indicadores_uf": r2(iv("Punto de quiebre")),  # = costo total; NO usar como "quiebre de ingresos"
    }

    # ---------------------------------------------------------------- sensibilidad
    SN = "SENSIBILIDAD"
    wsn = bk.ws(SN)
    r_var = bk.find(SN, "Variable / Variacion", col=2)[0]
    vars_ = [float(wsn.cell(r_var, c).value) for c in range(3, 8)]
    sens = []
    for lbl, key in [("Ingresos - VAN", "Ingresos"), ("Costo HH (sueldos) - VAN", "Costo HH (sueldos)"),
                     ("Otros egresos - VAN", "Otros egresos"), ("Tasa de descuento - VAN", "Tasa de descuento")]:
        r = bk.find(SN, lbl, col=2)[0]
        sens.append({"variable": key, "van": [r2(wsn.cell(r, c).value) for c in range(3, 8)]})
    d["sensibilidad"] = {
        "variaciones": vars_, "tabla": sens, "van_base_uf": r2(bk.after(SN, "VAN del Proyecto", 1, col=2)),
        "ingreso_minimo_pct": r2(bk.after(SN, "Ingreso minimo", 1, col=2)),
        "aumento_max_costo_hh": r2(bk.after(SN, "Aumento maximo tolerable del costo HH", 1, col=2)),
        "primer_mes_flujo_positivo": int(bk.after(SN, "Primer mes de flujo positivo", 1, col=2)),
    }

    # ---------------------------------------------------------------- curva S y flujos
    CS = "CURVA S"
    wc = bk.ws(CS)
    r_mes = bk.find(CS, "mes", col=5)[0] if False else None
    r_ing = bk.find(CS, "A.2- INGRESO ACUMULADO", col=2)[0]
    r_egr = bk.find(CS, "B.2- EGRESO TOTAL", col=2)[0]
    r_res = bk.find(CS, "RESULTADO ACUMULADO", col=2)[0]
    ing = bk.row_series(CS, r_ing, 5)  # columna E = mes 0
    egr = bk.row_series(CS, r_egr, 5)
    res = [0] + bk.row_series(CS, r_res, 6, 56)
    cap = d["parametros"]["capital_inicial_uf"]
    comercial = [0] + [round(v - cap, 2) for v in ing[1:]]
    r_pe = bk.find(CS, "PUNTO EQUILIBRIO", col=2)[0]
    r_mn = bk.find(CS, "MES MAS BAJO", col=2)[0]
    d["curva_s"] = {
        "meses": list(range(57)),
        "ingreso_acum_incl_capital": [round(v, 2) for v in ing],
        "ingreso_comercial_acum": comercial,
        "egreso_acum": [round(v, 2) for v in egr],
        "resultado_acum_con_financiamiento": [round(v, 2) for v in res],
        "capital_inicial_uf": cap,
        "payback_mes": int(wc.cell(r_pe, 5).value),
        "caja_minima_uf": r2(wc.cell(r_mn, 4).value),
        "caja_minima_mes": int(wc.cell(r_mn, 5).value),
    }
    # flujo del proyecto (sin financiamiento, antes de impuestos): hoja INDICADORES, bloque "Flujo de Base"
    r_fl = bk.find(I, "Flujo del proyecto (UF)", col=1)[0]
    r_fa = bk.find(I, "Flujo acumulado (UF)", col=1)[0]
    r_in = bk.find(I, "Ingresos (UF)", col=1)[0]
    r_eg = bk.find(I, "Egresos (UF)", col=1)[0]
    flujo = bk.row_series(I, r_fl, 2)
    acum = bk.row_series(I, r_fa, 2)
    mn = min(range(57), key=lambda i: acum[i])
    d["flujo_mensual"] = {
        "meses": list(range(57)),
        "ingresos": [round(v, 2) for v in bk.row_series(I, r_in, 2)],
        "egresos": [round(v, 2) for v in bk.row_series(I, r_eg, 2)],
        "flujo_proyecto": [round(v, 2) for v in flujo],
        "flujo_acumulado": [round(v, 2) for v in acum],
        "minimo_acumulado_uf": round(acum[mn], 2), "minimo_acumulado_mes": mn,
    }

    # ---------------------------------------------------------------- RR.HH.
    HS = "COSTOS HH - SUELDOS"
    wh = bk.ws(HS)
    r0 = bk.find(HS, "ROL", col=1)[0] + 1
    c_hh = bk.find(HS, "HH implementacion + operacion", col=None, exact=False)[1] if False else 5
    c_pl = bk.find(HS, "Plazas propuestas", col=None)[1]
    roles = plazas = 0
    hh_total = 0.0
    r = r0
    while wh.cell(r, 1).value and norm(wh.cell(r, 1).value) != "TOTAL" and wh.cell(r, c_pl).value is not None:
        roles += 1
        plazas += wh.cell(r, c_pl).value
        hh_total += wh.cell(r, 5).value or 0
        r += 1
    HM = "HH POR ROL Y MES"
    wm = bk.ws(HM)
    rh = bk.find(HM, "ROL", col=1)[0]
    monthly = defaultdict(float)
    r = rh + 1
    while wm.cell(r, 1).value and not str(wm.cell(r, 1).value).startswith("Ubicaci"):
        for c in range(3, 3 + 56):
            monthly[c - 2] += wm.cell(r, c).value or 0
        r += 1
    peak_m = max(monthly, key=lambda k: monthly[k])
    d["rrhh"] = {"roles": roles, "plazas": int(plazas), "hh_total": round(hh_total, 2),
                 "hh_pico": round(monthly[peak_m]), "hh_pico_mes": peak_m,
                 "hh_por_mes": [round(monthly[m], 1) for m in range(1, 57)]}

    # ---------------------------------------------------------------- innovaciones
    IN = "INNOVACIONES"
    wi = bk.ws(IN)
    r_res = bk.find(IN, "F. RESUMEN POR INNOVACION.", col=1)[0]
    inn = []
    for k in range(5):
        r = r_res + 2 + k
        inn.append({
            "id": wi.cell(r, 1).value, "nombre": wi.cell(r, 2).value, "inversion_uf": r2(wi.cell(r, 5).value),
            "costo_operacion_uf": r2(wi.cell(r, 8).value), "beneficio_cliente_uf": r2(wi.cell(r, 9).value),
            "ingreso_lafrox_uf": r2(wi.cell(r, 10).value),
        })
    rt = r_res + 7
    d["innovaciones"] = {
        "tabla": inn, "inversion_total_uf": r2(wi.cell(rt, 5).value), "costo_operacion_total_uf": r2(wi.cell(rt, 8).value),
        "beneficio_cliente_total_uf": r2(sum(i["beneficio_cliente_uf"] for i in inn)),
        "ingreso_lafrox_total_uf": r2(wi.cell(rt, 10).value),
        "nota_beneficio": "beneficio estimado para Puelche (no forma parte del flujo de LafroX)",
    }

    # ---------------------------------------------------------------- proveedores (implementacion)
    PV = "PROVEEDORES"
    wv = bk.ws(PV)
    r_i = bk.find(PV, "Implementacion", col=2)[0]
    r_o = bk.find(PV, "Operacion", col=2, start=r_i + 2)[0]
    def read_block(r_start, r_end):
        rows = []
        for r in range(r_start, r_end):
            prov, bien, cant, tot = wv.cell(r, 2).value, wv.cell(r, 4).value, wv.cell(r, 6).value, wv.cell(r, 12).value
            if prov and bien and isinstance(tot, (int, float)):
                rows.append((str(prov), str(bien), cant, float(tot)))
        return rows
    impl = read_block(r_i + 2, r_o)
    oper = read_block(r_o + 2, r_o + 2 + 60)
    agg = defaultdict(lambda: {"impl": 0.0, "op": 0.0, "bienes": []})
    for prov, bien, cant, tot in impl:
        agg[prov]["impl"] += tot
        agg[prov]["bienes"].append((tot, bien))
    for prov, bien, cant, tot in oper:
        agg[prov]["op"] += tot
    sup = []
    for prov, v in agg.items():
        if v["impl"] > 0:
            principal = max(v["bienes"])[1]
            names = [n.strip() for n in prov.split(";")]
            short = "; ".join(names[:2]) + (" y otros" if len(names) > 2 else "")
            sup.append({"proveedor": short, "bien": principal, "cantidad_lineas": len(v["bienes"]), "impl_uf": r2(v["impl"], 1)})
    sup.sort(key=lambda s: -s["impl_uf"])
    d["proveedores"] = {
        "top_implementacion": sup[:10],
        "aws_operacion_uf_mes": r2(sum(t for p, b, c, t in oper if p.upper().startswith("AWS")), 1),
        "nota": "Costo total estimado en UF (implementacion); AWS operacion = suma de servicios AWS, costo mensual de referencia M21-M56.",
    }

    # ---------------------------------------------------------------- adquisiciones de implementacion
    AQ = "ADQUISICIONES IMPLEMENTACION"
    wa = bk.ws(AQ)
    items, cat = [], None
    cats_aq = {}
    for r in range(8, 70):
        a = wa.cell(r, 1).value
        if isinstance(a, str) and a.startswith("//"):
            cat = a.strip("/ ").strip()
            continue
        if wa.cell(r, 6).value == "Total" and cat:
            cats_aq[cat] = r2(wa.cell(r, 9).value)
            continue
        if a and cat and isinstance(wa.cell(r, 9).value, (int, float)) and isinstance(wa.cell(r, 6).value, (int, float)):
            items.append({"categoria": cat, "componente": str(a), "cantidad": wa.cell(r, 6).value, "total_uf": r2(wa.cell(r, 9).value, 1)})
    r_tot = bk.find(AQ, "ADQUISICIONES FASE IMPLEMENTACION", col=1)[0]
    items.sort(key=lambda i: -i["total_uf"])
    d["adquisiciones_implementacion"] = {
        "total_uf": r2(wa.cell(r_tot, 2).value, 1), "por_categoria": cats_aq, "top": items[:10],
    }

    # ---------------------------------------------------------------- documentos (SD / Informe 2)
    d["documentos"] = {
        # La EDT vigente (10 productos, 60 cuentas, 230 paquetes), la RBS (36 riesgos), la matriz y el top-10 salen de
        # data/edt_rbs.json (tools/extract_edt_rbs.py, SD7 y SD8).
        # Fases de cada etapa contractual: SD7 (seccion "Carta Gantt y calendario") y SD1 ("cuatro fases en cascada"); sin cifras de paquetes.
        "fases_cascada": [
            {"nombre": "Requisitos y diseño", "detalle": "Concluye en H1 y H2 (Etapa 1) y en H8 (Etapa 2)"},
            {"nombre": "Construcción", "detalle": "Frentes de módulos e integraciones en paralelo; versiones a QA"},
            {"nombre": "Integración y certificación", "detalle": "Integración en H4 o H9; acta de certificación en H5 o H10"},
            {"nombre": "Implantación", "detalle": "Marcha blanca desde H6 o H11; paso a producción en H7 o H12"}],
        "etapas": {"etapa1": [1, 16], "etapa2": [13, 21], "operacion": [21, 56], "h7_mes": 16, "h12_mes": 21},
        "innovaciones_info": [
            {"id": "INN-01", "tipo": "Producto", "nombre": "Seguimiento posentrega", "meta": "−25 % relativo en unidades vencidas en el local", "evaluacion": "Mes 28"},
            {"id": "INN-02", "tipo": "Proceso", "nombre": "Reproducción de incidentes", "meta": "−30 % relativo en horas hasta causa reproducida", "evaluacion": "Mes 15"},
            {"id": "INN-03", "tipo": "Tecnológica", "nombre": "Vida útil por historia térmica", "meta": "≥ 80 % de lotes dentro de ±15 % de la vida nominal", "evaluacion": "Mes 15"},
            {"id": "INN-04", "tipo": "Modelo de negocio", "nombre": "Pago ligado al costo de servir", "meta": "Costo comparable −5 % con OTIF de más de 95 %", "evaluacion": "Mes 36"},
            {"id": "INN-05", "tipo": "Impacto social", "nombre": "Hoja del almacenero", "meta": "Medir cobertura, comprensión y uso", "evaluacion": "Meses 14, 22–26, 27 y 33"}],
        "calidad": {"p95_preparacion_s": 1, "disponibilidad_pct": 99.9, "rto_h": 4, "rpo_min": 15, "casos": 1328, "gates": "G0–G6",
                    "cobertura_negocio_pct": 70, "cobertura_global_pct": 80, "p95_entrega_s": 2, "p95_preventa_s": 1.5,
                    "p95_stock_credito_s": 2, "disponibilidad_infra_pct": 99.95},
        "problema": {"retiro_dias": 9, "otif_actual_pct": 82.4, "otif_meta_pct": 95, "costo_servir_anio": 2016, "kg": 4800,
                     "suspension_meses": 6, "ventas_riesgo_pct": 6},
        "continuidad": {"horas_sin_senal": 14, "horas_sin_enlace": 24, "sync_min": 10, "sync_horas": 2, "identificar_clientes_h": 2},
        # Equipo nominado: nombres y cargos tal como figuran en el Formulario T-8 (sd12-corrigiendo/formulario-t8/tablas/tab_T8_equipo.tex)
        "equipo": [["AA", "Alex Aravena", "Jefe de Proyecto"], ["BT", "Bastián Trejo", "Arquitecto de Solución"],
                   ["ÁC", "Álvaro Catalán", "Encargado de Seguridad de la Información"], ["LC", "Leandro Chamorro", "Líder de Datos"],
                   ["TP", "Tomás Pérez", "Líder de Desarrollo"], ["MM", "Maximiliano Miño", "Líder de Calidad"],
                   ["GC", "Guillermo Castillo", "Líder de Operación / SRE"],
                   ["PH", "Patricio Henríquez", "Líder de Implantación y Gestión del Cambio"],
                   ["CF", "Carolina Fuentes", "Líder Funcional"], ["RV", "Rodrigo Valdés", "Líder de Integración"]],
        "fuente": "Subdocumentos SD1–SD13 e Informe 2 (no provienen del modelo financiero).",
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    print("OK", OUT)
    t = d["tarifa"]["total"]
    print("tarifa", t, "| costo", d["costo"]["total"]["uf"], "| margen", d["margen"]["total"]["uf"], "| rent", d["rentabilidad_nominal"])
    print("VAN", d["indicadores"]["van_sin_impuestos_uf"], d["indicadores"]["van_sobre_impuestos_uf"], "| TIR", d["indicadores"]["tir_sin_imp_mensual"], d["indicadores"]["tir_sin_imp_anual"])
    print("rrhh", {k: v for k, v in d["rrhh"].items() if k != "hh_por_mes"})
    print("payback", d["curva_s"]["payback_mes"], d["curva_s"]["caja_minima_uf"], d["curva_s"]["caja_minima_mes"])


if __name__ == "__main__":
    main()
