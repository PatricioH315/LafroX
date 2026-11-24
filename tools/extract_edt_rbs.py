"""Extrae la EDT (SD7 / Formulario T-14 y T-15) y la RBS (SD8 / Formulario T-16) vigentes -> data/edt_rbs.json.

Uso:  python -I tools/extract_edt_rbs.py

Fuentes (todas en los worktrees LafroX-worktrees/):
  EDT    sd7-corrigiendo/formulario-t14/tablas/tab_T14_1.tex      productos, cuentas de control (CC) y paquetes (PT)
         sd7-corrigiendo/formulario-t14/tablas/dic_prod_N.tex     nombre de cada cuenta de control y sus paquetes
         sd7-corrigiendo/formulario-t15/tablas/tab_T15_2.tex      horas esperadas (E HH) de los 230 paquetes
         sd7-corrigiendo/revision/edt_estructura_20261117.json    contraste de nombres de producto y de cuenta
  RBS    sd8-revision/08_plan_riesgos/figuras/LafroX_RBS_36_riesgos_S8_v4.drawio   ramas, riesgos, zona
         sd8-revision/LAFROX-Formulario-T-16.tex                  categoria, probabilidad, impacto y exposicion
         sd8-revision/08_plan_riesgos/contenido.tex               Tabla 8.5 (diez de mayor exposicion)
         sd8-revision/08_plan_riesgos/anexo-h-reservas.tex        exposicion inicial, contingencia y gestion (HH)

Lo unico escrito a mano es el bloque CURADO (nombres cortos para tarjetas y respuestas resumidas del top-10);
cada item declara su fuente. Todo lo demas se lee de los documentos y se valida cruzando las fuentes.
"""
import html
import json
import re
from pathlib import Path

BASE = Path("C:/Users/henri/OneDrive/Documentos/Universidad 2026S2/FEP/Repositorios/Principal/LafroX-worktrees")
SD7 = BASE / "sd7-corrigiendo"
SD8 = BASE / "sd8-revision"
OUT = Path(__file__).resolve().parent.parent / "data" / "edt_rbs.json"

# ---------------------------------------------------------------------------------------------- CURADO
# Nombre corto de cada producto para la tarjeta de la lamina (cabe en 2 lineas de 1,5 in).
# Fuente: nombre completo de tab_T14_1.tex, abreviado editorialmente; el nombre completo se usa en el encabezado.
PRODUCTO_CORTO = {
    1: "Gestión del proyecto", 2: "Requisitos y diseño", 3: "Plataforma base", 4: "Software operativo",
    5: "Integraciones y datos", 6: "Solución certificada", 7: "Innovaciones", 8: "Infraestructura y servicios",
    9: "Implantación y usuarios", 10: "Operación y salida",
}
# Nombre corto de las cuentas de control cuyo nombre en T-14 supera ~44 caracteres (no caben en 2 lineas de la tarjeta).
# Fuente: encabezado "Cuenta N.M" de dic_prod_N.tex, abreviado editorialmente. Las demas usan el nombre completo.
CUENTA_CORTO = {
    "6.2": "Pruebas de aceptación y accesibilidad",
    "7.1": "Innovación 1: seguimiento posentrega",
    "7.2": "Innovación 2: reproducción de incidentes",
    "7.3": "Innovación 3: vida útil por historia térmica",
    "7.4": "Innovación 4: tramo variable",
    "7.5": "Innovación 5: hoja del almacenero",
    "8.2": "Nube, licencias y enlaces",
}
# Nombre corto de cada riesgo para las tarjetas (<= 26 caracteres). Fuente: titulo completo del drawio de la RBS
# (LafroX_RBS_36_riesgos_S8_v4.drawio), abreviado editorialmente.
RIESGO_CORTO = {
    "R-002": "Historia sanitaria de origen", "R-032": "Cambio de soporte", "R-033": "Dependencia del proveedor",
    "R-001": "Certificación EDI", "R-003": "Historial de ventas", "R-007": "Deuda viva adicional",
    "R-008": "SII sin respuesta", "R-030": "Interfaces ERP/WMS", "R-034": "ERP indisponible",
    "R-004": "Inventario sin conciliar", "R-005": "Saldo de envases", "R-006": "Línea base de aceptación",
    "R-009": "Matriz térmica pendiente", "R-010": "Equipos llegan tarde", "R-012": "Termógrafo sin instalar",
    "R-016": "Validación del cliente", "R-017": "Enlace de sitio caído", "R-018": "Corte eléctrico largo",
    "R-020": "Permiso en congelamiento", "R-021": "Falla mecánica de camión", "R-022": "Siniestro de camión",
    "R-023": "Asalto a camión", "R-036": "Perfil de carga distinto",
    "R-011": "Firma del transportista", "R-013": "Proceso anterior persiste", "R-014": "Planificador no disponible",
    "R-015": "Asistencia a capacitación", "R-024": "Reemplazos sin aviso", "R-028": "Acuerdo de telemetría",
    "R-029": "Rotación nocturna", "R-035": "Rechazo de conductores",
    "R-025": "Cambios de alcance", "R-027": "Liquidación variable", "R-031": "Cierre bajo peak",
    "R-019": "Datos en la nube", "R-026": "Cambios normativos",
}
# Dos riesgos de ejemplo por rama (lamina de ramas). Fuente: los de mayor exposicion de cada rama en T-16.
RAMA_EJEMPLOS = {
    1: "R-002 Historia sanitaria · R-032 Soporte",
    2: "R-001 Certificación EDI · R-030 Interfaces",
    3: "R-004 Inventario · R-006 Línea base",
    4: "R-013 Proceso anterior · R-029 Rotación",
    5: "R-031 Cierre bajo peak · R-025 Alcance",
    6: "R-019 Datos en la nube · R-026 Normativa",
}
# Respuesta resumida de los diez de mayor exposicion. Fuente: columna "Mitigacion" de T-16 (primera medida).
TOP10_RESPUESTA = {
    "R-002": "Evidencia de origen y decisión sobre lotes",
    "R-004": "Conciliación de inventario antes del corte",
    "R-006": "Horas y montos históricos validados (V-10)",
    "R-013": "Acompañamiento a D-5 de cada ola",
    "R-029": "Tutor y evaluación antes de trabajar solo",
    "R-001": "Agenda de certificación EDI por cadena",
    "R-005": "Conciliación V-08 de saldos de envases",
    "R-009": "Matriz térmica V-11 aprobada en el mes 2",
    "R-011": "Acuerdo y nómina firmados a D-5",
    "R-016": "Área decisora y suplente designados",
}


def num_es(s):
    """'1.199,52' -> 1199.52 ; '0,50' -> 0.5"""
    return float(s.replace(".", "").replace(",", "."))


def read(p):
    return Path(p).read_text(encoding="utf-8")


# ---------------------------------------------------------------------------------------------- EDT
def edt():
    t1 = read(SD7 / "formulario-t14/tablas/tab_T14_1.tex")
    productos = []
    for m in re.finditer(r"^\s*(\d+) & (.+?) & (\d+) & (\d+) \\\\", t1, re.M):
        productos.append({"n": int(m.group(1)), "nombre": m.group(2).strip(), "cc": int(m.group(3)), "pt": int(m.group(4))})
    assert len(productos) == 10, "se esperaban 10 productos"

    # horas esperadas por paquete (T-15, tabla de los 230 paquetes)
    t15 = read(SD7 / "formulario-t15/tablas/tab_T15_2.tex")
    hh = {}
    for m in re.finditer(r"^\s*(\d+\.\d+\.\d+) & \w+ & \w+ & [^&]+ & [\d.]+ & [\d.]+ & [\d.]+ & ([\d.]+) \\\\", t15, re.M):
        hh[m.group(1)] = float(m.group(2))
    assert len(hh) == 230, f"T-15 trae {len(hh)} paquetes, no 230"

    cuentas_n = 0
    for p in productos:
        tx = read(SD7 / f"formulario-t14/tablas/dic_prod_{p['n']}.tex")
        ccs = []
        for m in re.finditer(r"\\textbf\{Cuenta (\d+)\.(\d+) — (.+?)\.\}", tx):
            assert int(m.group(1)) == p["n"]
            cod = f"{m.group(1)}.{m.group(2)}"
            ccs.append({"codigo": cod, "nombre": m.group(3).strip(), "corto": CUENTA_CORTO.get(cod, m.group(3).strip())})
        pkgs = re.findall(r"^\s*(\d+\.\d+\.\d+) & ", tx, re.M)
        for c in ccs:
            mine = [k for k in pkgs if k.rsplit(".", 1)[0] == c["codigo"]]
            c["pt"] = len(mine)
            c["hh"] = round(sum(hh[k] for k in mine), 2)
        assert len(ccs) == p["cc"], f"producto {p['n']}: {len(ccs)} cuentas, la tabla T14-1 declara {p['cc']}"
        assert sum(c["pt"] for c in ccs) == p["pt"], f"producto {p['n']}: paquetes no cuadran"
        p["cuentas"] = ccs
        p["hh"] = round(sum(c["hh"] for c in ccs), 2)
        p["corto"] = PRODUCTO_CORTO[p["n"]]
        cuentas_n += len(ccs)
    assert cuentas_n == 60

    # contraste con la estructura consolidada del 17-11 (revision/edt_estructura_20261117.json)
    est = json.loads(read(SD7 / "revision/edt_estructura_20261117.json"))
    dif = []
    for e in est:
        pn, name, ccs = int(e[0]), e[1], e[2]
        p = productos[pn - 1]
        if p["nombre"] != name:
            dif.append(f"producto {pn}: T-14 '{p['nombre']}' vs estructura '{name}'")
        for i, c in enumerate(ccs):
            if i < len(p["cuentas"]) and p["cuentas"][i]["nombre"] != c[0]:
                dif.append(f"cuenta {p['cuentas'][i]['codigo']}: T-14 '{p['cuentas'][i]['nombre']}' vs estructura '{c[0]}'")
    return productos, hh, dif


# ---------------------------------------------------------------------------------------------- RBS
def rbs():
    dx = read(SD8 / "08_plan_riesgos/figuras/LafroX_RBS_36_riesgos_S8_v4.drawio")
    vals = [re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html.unescape(v))).strip() for v in re.findall(r'value="([^"]*)"', dx)]
    ramas, cur = [], None
    for v in vals:
        m = re.match(r"^(\d) · (.+?) (\d+) riesgos$", v)
        if m:
            cur = {"n": int(m.group(1)), "nombre": m.group(2), "riesgos_decl": int(m.group(3)), "riesgos": []}
            ramas.append(cur)
            continue
        m = re.match(r"^(\d+)\.(\d+) (.+) (R-\d{3}) · (Crítica|Alta|Media|Baja)$", v)
        if m:
            ramas[int(m.group(1)) - 1]["riesgos"].append({"id": m.group(4), "zona": m.group(5), "nombre_completo": m.group(3), "pos": f"{m.group(1)}.{m.group(2)}"})
    for r in ramas:
        assert len(r["riesgos"]) == r["riesgos_decl"], f"rama {r['n']}: drawio declara {r['riesgos_decl']} y lista {len(r['riesgos'])}"
        r["riesgos"].sort(key=lambda x: int(x["pos"].split(".")[1]))

    # registro T-16 (36 filas): categoria, P, I, exposicion y zona
    t16 = read(SD8 / "LAFROX-Formulario-T-16.tex")
    reg = {}
    for line in t16.split("\n"):
        if not re.match(r"^R-\d{3} & ", line):
            continue
        c = [x.strip() for x in line.rstrip().rstrip("\\").rstrip().split(" & ")]
        if len(c) != 8 or c[0] in reg:
            continue
        mp = re.match(r"(\d) / ([\d,]+)", c[3]); mi = re.match(r"(\d) / ([\d,]+)", c[4]); me = re.match(r"([\d,]+) \((\w+)\)", c[5])
        reg[c[0]] = {"categoria": c[2], "p": num_es(mp.group(2)), "i": num_es(mi.group(2)), "e": num_es(me.group(1)), "zona": me.group(2), "responsable": c[7]}
    assert len(reg) == 36, f"T-16 trae {len(reg)} riesgos"

    errores = []
    for r in ramas:
        for k in r["riesgos"]:
            g = reg[k["id"]]
            if g["categoria"] != r["nombre"]:
                errores.append(f"{k['id']}: rama drawio '{r['nombre']}' vs categoria T-16 '{g['categoria']}'")
            if g["zona"] != k["zona"]:
                errores.append(f"{k['id']}: zona drawio {k['zona']} vs T-16 {g['zona']}")
            k.update({"corto": RIESGO_CORTO[k["id"]], "p": g["p"], "i": g["i"], "e": g["e"]})
        r["ejemplos"] = RAMA_EJEMPLOS[r["n"]]
    assert not errores, "\n".join(errores)

    todos = [k for r in ramas for k in r["riesgos"]]
    zonas = {z: sum(1 for k in todos if k["zona"] == z) for z in ("Crítica", "Alta", "Media", "Baja")}

    # matriz probabilidad x impacto con las escalas del SD8 (Tablas 8.2 y 8.3): filas P 0,90..0,10; columnas I 0,05..0,80
    P = [0.9, 0.7, 0.5, 0.3, 0.1]; I = [0.05, 0.10, 0.20, 0.40, 0.80]
    n = [[0] * 5 for _ in range(5)]; ids = [[[] for _ in range(5)] for _ in range(5)]
    for k in sorted(todos, key=lambda x: x["id"]):
        r, c = P.index(k["p"]), I.index(k["i"])
        n[r][c] += 1; ids[r][c].append(k["id"])

    # Tabla 8.5 (diez de mayor exposicion): se lee del SD8 y se contrasta con T-16
    cont = read(SD8 / "08_plan_riesgos/contenido.tex")
    blk = cont.split("Diez riesgos de mayor exposición cualitativa")[1].split("\\end{tablalafrox}")[0]
    top = []
    for m in re.finditer(r"^(R-\d{3}) & ([\d,]+) & ([\d,]+) & ([\d,]+) & (\w+) \\\\", blk, re.M):
        rid = m.group(1)
        assert abs(num_es(m.group(2)) * num_es(m.group(3)) - num_es(m.group(4))) < 1e-9
        assert reg[rid]["zona"] == m.group(5)
        rama = next(r["n"] for r in ramas if any(k["id"] == rid for k in r["riesgos"]))
        corto = RIESGO_CORTO[rid]
        top.append({"id": rid, "nombre": corto, "rama": rama, "p": num_es(m.group(2)), "i": num_es(m.group(3)), "e": num_es(m.group(4)),
                    "zona": m.group(5), "respuesta": TOP10_RESPUESTA[rid]})
    assert len(top) == 10

    # reservas (SD8 anexo 8.H)
    ah = read(SD8 / "08_plan_riesgos/anexo-h-reservas.tex")
    def hhrow(label):
        m = re.search(re.escape(label) + r" & ([\d.,]+) &", ah)
        return num_es(m.group(1))
    reservas = {
        "exposicion_inicial_hh": hhrow("Exposición inicial vigente"),
        "contingencia_hh": hhrow("Contingencia específica propuesta p1H0"),
        "gestion_hh": hhrow("Gestión aprobada"),
        "preventivo_hh": hhrow("Trabajo preventivo adicional A"),
    }
    return ramas, zonas, {"prob": P, "impacto": I, "prob_nombre": ["Muy alta", "Alta", "Media", "Baja", "Muy baja"],
                          "n": n, "ids": ids, "cortes": {"media": 0.08, "alta": 0.20, "critica": 0.40}}, top, reservas


def main():
    productos, hh, dif = edt()
    ramas, zonas, matriz, top, reservas = rbs()
    total_pt_hh = round(sum(hh.values()), 2)
    d = {
        "fuente": "EDT: SD7 (Formularios T-14 y T-15, 23-11-2026). RBS: SD8 (RBS v4 de 36 riesgos, T-16 y anexo 8.H). Generado por tools/extract_edt_rbs.py.",
        "edt": {
            "productos": productos,
            "total": {"productos": len(productos), "cc": sum(p["cc"] for p in productos), "pt": sum(p["pt"] for p in productos), "hh_paquetes": total_pt_hh},
            "nota_hh": "HH = valor esperado PERT de los 230 paquetes (T-15, Tabla 4.2). La linea base de T-15 suma ademas 128 HH de restauraciones, "
                       "9.336 HH de soporte puente, 3.072 HH de reserva protegida y 2.889,59 HH de roles minimos (203.548,62 HH en total).",
            "linea_base_t15_hh": 203548.62,
            "diferencias_nombres_vs_estructura_1117": dif,
        },
        "rbs": {
            "total": sum(len(r["riesgos"]) for r in ramas),
            "ramas": [{"n": r["n"], "nombre": r["nombre"], "riesgos": len(r["riesgos"]), "ejemplos": r["ejemplos"], "lista": r["riesgos"]} for r in ramas],
            "zonas": {"criticos": zonas["Crítica"], "altos": zonas["Alta"], "medios": zonas["Media"], "bajos": zonas["Baja"]},
            "reservas": reservas,
            "reserva_hh": reservas["contingencia_hh"],
        },
        "matriz": matriz,
        "top_riesgos": top,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    print("OK", OUT)
    print("EDT", d["edt"]["total"])
    for p in productos:
        print(f"  {p['n']:>2} {p['nombre']}: {p['cc']} CC, {p['pt']} PT, {p['hh']:,.2f} HH")
    print("RBS", d["rbs"]["total"], d["rbs"]["zonas"], reservas)
    print("diferencias de nombres vs estructura 17-11:", dif or "ninguna")


if __name__ == "__main__":
    main()
