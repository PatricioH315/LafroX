"""Genera las 4 figuras nuevas del Bloque C en formato draw.io (.drawio).

Figuras (en imagenes/Diagramas que faltaban/productos/, carta vertical W=584):
  1. Fig_Red_Precedencias_Productos.drawio  (fuente: tab_7B1.tex, tab_SD7_4.tex, tab_T15_7.tex)
  2. Fig_Cobertura_Alcance_Productos.drawio (fuente: tab_SD7_2.tex, dic_prod_1..10.tex)
  3. Fig_Planificacion_Gradual.drawio       (fuente: T-15 sec. 6.1, tab_T15_paquetes, 9, 9h5, 10)
  4. Fig_Ruta_H12.drawio                    (fuente: tab_T15_7, cpm_detalle, paquetes, 10, sec. 5.5)

Valida todas las aristas (origen, destino y tipo) contra tab_7B1.tex, todas las
fechas y holguras contra tab_T15_7.tex / tab_T15_cpm_detalle.tex / tab_T15_paquetes.tex /
tab_T15_10.tex y garantiza contraste WCAG 2.1 AA >= 4,5:1 para cabeceras sobre blanco.

Nunca escribe en archivos .tex ni sobrescribe imágenes antiguas.
"""
from __future__ import annotations

import argparse

import re
from html import escape
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "imagenes" / "Diagramas que faltaban" / "productos"

# Paleta por producto con contraste WCAG >= 4,5:1 sobre texto blanco #FFFFFF.
PALETTE: dict[int, tuple[str, str]] = {
    1: ("#1F4E79", "#DCE6F1"),   # 8,66:1
    2: ("#21699B", "#DDEEF8"),   # 5,90:1
    3: ("#1E8449", "#DDF0E3"),   # 4,72:1
    4: ("#A85012", "#FBE7D6"),   # 5,50:1
    5: ("#7D3C98", "#EBDDF1"),   # 7,07:1
    6: ("#8D5524", "#EFE3D8"),   # 6,07:1
    7: ("#0F7460", "#D8F0EB"),   # 5,70:1
    8: ("#4D5656", "#E3E6E6"),   # 7,55:1
    9: ("#8B2635", "#F5DFE2"),   # 8,65:1
    10: ("#4F5D2F", "#E8EDDC"),  # 7,14:1
}

ROOT_COLOR = "#262626"
W_CANVAS = 584.0
NBH = "\u2011"  # guion irrompible para evitar saltos en fechas y códigos D-XX


def nbh(text: str) -> str:
    """Reemplaza '-' por guion irrompible en códigos y fechas."""
    return text.replace("-", NBH)


def _wcag_contrast(fg_hex: str, bg_hex: str = "#FFFFFF") -> float:
    def lum(h: str) -> float:
        hx = h.lstrip("#")
        rgb = [int(hx[i : i + 2], 16) / 255.0 for i in (0, 2, 4)]
        lin = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb]
        return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]

    l1, l2 = lum(fg_hex), lum(bg_hex)
    return (max(l1, l2) + 0.05) / (min(l1, l2) + 0.05)


def check_palette_wcag() -> None:
    for pnum, (strong, _) in PALETTE.items():
        cr = _wcag_contrast(strong, "#FFFFFF")
        assert cr >= 4.5, f"Producto {pnum} ({strong}) bajo contraste WCAG 4,5:1 ({cr:.2f}:1)"


# Aristas agrupadas de Fig_Red_Precedencias_Productos validadas contra tab_7B1.tex:
# (id_arista, nodo_origen, nodo_destino, dep_ids, tokens_pred, tokens_succ, tipo_esperado)
RED_EDGES: list[tuple[str, str, str, list[str], list[str], list[str], str]] = [
    ("e1", "r1_c1", "r1_c2", ["D-01"], ["2.1.1"], ["2.2.1"], "Por etapa"),
    ("e1b", "r1_c2", "r1_c3", ["D-09"], ["2.4.1", "2.4.2"], ["8.1.2"], "FC"),
    ("e2", "r1_c1", "r2_c1", ["D-02", "D-40"], ["2.1.5"], ["5.1.1", "5.2.2"], "FC"),
    ("e3", "r1_c2", "r2_c2", ["D-04", "D-05"], ["2.8.1", "2.6.2"], ["Producto 4"], "FC"),
    (
        "e4",
        "r1_c3",
        "r2_c3",
        ["D-14"],
        ["3.1 Ambientes (H3)"],
        ["QA", "producto 4", "no el inicio"],
        "FC",
    ),
    ("e5", "r2_c1", "r2_c2", ["D-15"], ["3.3.1", "5.1"], ["Producto 4"], "CC"),
    ("e6", "r2_c2", "r2_c3", ["D-20"], ["Módulos de la Etapa 1", "5.2.1"], ["6.1.1"], "FC"),
    ("e7", "r2_c3", "r3_c2", ["D-21", "D-21b"], ["6.1.1"], ["6.2.1", "6.3.1", "6.5.1"], "FC"),
    ("e8", "r2_c3", "r3_c3", ["D-48"], ["6.1.1"], ["9.1.1"], "FC"),
    ("e9", "r2_c1", "r3_c1", ["D-41"], ["5.1.1"], ["5.4.1"], "FC"),
    ("e10", "r3_c1", "r4_l", ["D-25", "D-26", "D-38"], ["5.4.5", "8.6", "2.7.3"], ["9.2.1"], "FC"),
    ("e11", "r3_c2", "r4_l", ["D-25"], ["6.7.1"], ["9.2.1"], "FC"),
    ("e12", "r3_c3", "r4_l", ["D-25", "D-27"], ["9.1.1", "9.7.1"], ["9.2.1"], "FC"),
    ("e13", "r4_l", "r4_r", ["D-28"], ["9.2.1"], ["9.4.1", "16-05", "17-05"], "FC"),
    ("e_r1", "r5_c1", "r5_c2", ["D-29"], ["2.1.2", "2.8.2"], ["4.4.1", "4.5.2"], "FC"),
    ("e_r2", "r5_c2", "r5_c3", ["D-30"], ["4.4.1", "4.5.2"], ["6.1.2"], "FC"),
    ("e_r3", "r5_c3", "r6_c2", ["D-32"], ["6.7.2"], ["9.2.2"], "FC"),
    ("e14", "r6_c1", "r6_c2", ["D-32", "D-33", "D-51"], ["5.3.1", "9.1.3", "9.4.3", "5.3.2"], ["9.2.2", "9.4.2"], "FC"),
    ("e15", "r6_c2", "r6_c3", ["D-34"], ["9.4.2"], ["1.7.9", "18-10-2028"], "FC"),
]


def parse_tab_7b1() -> dict[str, dict[str, str]]:
    """Parsea las 54 dependencias de tab_7B1.tex."""
    tab_7b1 = (ROOT / "subdocumento-07-anexos" / "tablas" / "tab_7B1.tex").read_text(encoding="utf-8")
    deps: dict[str, dict[str, str]] = {}
    for line in tab_7b1.splitlines():
        m = re.match(r"^\s*(D-\d+[a-z]?)\s*&\s*(.+?)\s*&\s*(.+?)\s*&\s*(.+?)\s*&\s*(.+?)\s*\\\\", line)
        if m:
            deps[m.group(1)] = {
                "pred": m.group(2).strip(),
                "succ": m.group(3).strip(),
                "tipo": m.group(4).strip(),
                "fund": m.group(5).strip(),
            }
    assert len(deps) == 54 and "D-01" in deps and "D-51" in deps, f"tab_7B1 deps={len(deps)}"
    return deps


def validate_red_edges(deps: dict[str, dict[str, str]]) -> None:
    """Verifica cada arista de RED_EDGES contra tab_7B1.tex (origen, destino y tipo)."""
    for eid, src, dst, dep_ids, pred_toks, succ_toks, exp_tipo in RED_EDGES:
        assert not (src == "r4_r" and dst == "r6_c2"), f"Puente 9.4.1->9.2.2 prohibido ({eid})"
        joined_pred = " | ".join(deps[d]["pred"] for d in dep_ids)
        joined_succ = " | ".join(deps[d]["succ"] + " " + deps[d]["fund"] for d in dep_ids)
        for d in dep_ids:
            assert d in deps, f"{eid}: dependencia {d} no existe en tab_7B1.tex"
            assert deps[d]["tipo"] == exp_tipo, (
                f"{eid} ({d}): tipo tab_7B1='{deps[d]['tipo']}' != esperado='{exp_tipo}'"
            )
        for tok in pred_toks:
            assert tok in joined_pred, f"{eid}: token origen {tok!r} no encontrado en {joined_pred!r}"
        for tok in succ_toks:
            assert tok in joined_succ, f"{eid}: token destino {tok!r} no encontrado en {joined_succ!r}"


def verify_live_sources() -> dict:
    """Lee y valida cifras, dependencias y fechas directamente desde las tablas vigentes."""
    check_palette_wcag()
    deps = parse_tab_7b1()
    validate_red_edges(deps)

    tab_sd7_2 = (ROOT / "subdocumento-07" / "tablas" / "tab_SD7_2.tex").read_text(encoding="utf-8")
    cats = []
    for line in tab_sd7_2.splitlines():
        s = line.strip()
        if "&" in s and not s.startswith("{") and r"\cab" not in s and not s.startswith("\\"):
            parts = [c.strip() for c in s.rstrip("\\").split("&")]
            cats.append(parts[0])
    expected_cats = [
        "Módulos",
        "Interfaces",
        "Servicios comunes",
        "Innovaciones",
        "Seguridad",
        "Calidad",
        "Migración",
        "Implantación",
    ]
    assert cats == expected_cats, f"tab_SD7_2 cats={cats}"

    paq_txt = (ROOT / "formulario-t15" / "tablas" / "tab_T15_paquetes.tex").read_text(encoding="utf-8")
    paq_codes = re.findall(r"^\s*(\d+\.\d+\.\d+)\s*&", paq_txt, re.M)
    t9_1 = (ROOT / "formulario-t15" / "tablas" / "tab_T15_9_bloque_1.tex").read_text(encoding="utf-8")
    t9_2 = (ROOT / "formulario-t15" / "tablas" / "tab_T15_9_bloque_2.tex").read_text(encoding="utf-8")
    t9_acts = re.findall(r"^\s*(\d+\.\d+\.\d+)\.A\d+\s*&", t9_1 + "\n" + t9_2, re.M)
    t9h5 = (ROOT / "formulario-t15" / "tablas" / "tab_T15_9h5.tex").read_text(encoding="utf-8")
    t9h5_rows = re.findall(r"^\s*(\d+\.\d+\.\d+)\s*&\s*[A-Z]\s*&\s*(\d+)\s*&", t9h5, re.M)
    t10 = (ROOT / "formulario-t15" / "tablas" / "tab_T15_10.tex").read_text(encoding="utf-8")
    t10_rows = {}
    for line in t10.splitlines():
        m10 = re.match(
            r"^\s*(\d+\.\d+\.\d+)\s*&\s*[A-Z]\s*&\s*[A-Z]+\s*&\s*([^&]+?)\s*&\s*([^&]+?)\s*&\s*([^&]+?)\s*&\s*(\d+)\s*&\s*([\d.]+)\s*\\\\",
            line,
        )
        if m10:
            t10_rows[m10.group(1)] = {
                "meses": m10.group(2).strip(),
                "hh": m10.group(3).strip(),
                "regla": m10.group(4).strip(),
                "occ": int(m10.group(5)),
                "max_hh": float(m10.group(6)),
            }

    n_paq = len(paq_codes)
    n_h2_pkgs = len(set(t9_acts))
    n_h2_acts = len(t9_acts)
    n_h5_pkgs = len(t9h5_rows)
    n_h5_acts = sum(int(x[1]) for x in t9h5_rows)
    n_post_h5 = n_paq - n_h2_pkgs - n_h5_pkgs
    n_cont = len(t10_rows)

    assert (n_paq, n_h2_pkgs, n_h2_acts, n_h5_pkgs, n_h5_acts, n_post_h5, n_cont) == (
        171, 60, 119, 76, 385, 35, 59
    ), f"T-15 counts mismatch: {(n_paq, n_h2_pkgs, n_h2_acts, n_h5_pkgs, n_h5_acts, n_post_h5, n_cont)}"

    # Validar topes de tab_T15_10.tex: 64 HH nivel de esfuerzo vs 80 HH en 9.5.4 y 9.5.5
    loe_max = max(v["max_hh"] for v in t10_rows.values() if "nivel de esfuerzo" in v["regla"].lower())
    assert loe_max == 64.0, f"Tope nivel de esfuerzo={loe_max}"
    assert t10_rows["9.5.4"]["max_hh"] == 80.0 and t10_rows["9.5.5"]["max_hh"] == 80.0

    # Parsear hitos de tab_T15_7.tex
    tab_7 = (ROOT / "formulario-t15" / "tablas" / "tab_T15_7.tex").read_text(encoding="utf-8")
    milestones = {}
    for line in tab_7.splitlines():
        m7 = re.match(
            r"^\s*(H\d+)\s*&\s*([^&]+?)\s*&\s*([^&]+?)\s*&\s*([^&]+?)\s*&\s*([^&]+?)\s*&\s*(\d+)\s*&\s*(\d+|—)\s*&\s*([^&]+?)\s*\\\\",
            line,
        )
        if m7:
            milestones[m7.group(1)] = {
                "entrega": m7.group(2).strip(),
                "acta": m7.group(3).strip(),
                "paso": m7.group(4).strip(),
                "limite": m7.group(5).strip(),
                "holgura": int(m7.group(7) if m7.group(7) != "—" else m7.group(6)),
                "control": m7.group(8).strip(),
            }
    assert milestones["H11"]["entrega"] == "01-08-2028"
    assert (milestones["H12"]["entrega"], milestones["H12"]["acta"], milestones["H12"]["paso"], milestones["H12"]["limite"], milestones["H12"]["holgura"]) == (
        "02-10-2028", "17-10-2028", "18-10-2028", "31-10-2028", 8
    )

    # Parsear CPM detalle de tab_T15_cpm_detalle.tex
    cpm_txt = (ROOT / "formulario-t15" / "tablas" / "tab_T15_cpm_detalle.tex").read_text(encoding="utf-8")
    cpm_rows = {}
    for line in cpm_txt.splitlines():
        mc = re.match(
            r"^\s*(\d+\.\d+\.\d+)\s*&\s*(\d+)\s*&\s*(\d{2}-\d{2}-\d{4})\s*&\s*(\d{2}-\d{2}-\d{4})\s*&\s*(\d{2}-\d{2}-\d{4})\s*&\s*(\d{2}-\d{2}-\d{4})\s*&\s*(\d+)\s*&\s*(\d+)\s*\\\\",
            line,
        )
        if mc:
            cpm_rows[mc.group(1)] = {
                "dur": int(mc.group(2)),
                "es": mc.group(3),
                "ef": mc.group(4),
                "ls": mc.group(5),
                "lf": mc.group(6),
                "holgura": int(mc.group(7)),
                "hh": int(mc.group(8)),
            }

    # Parsear fechas programadas de paquetes clave en tab_T15_paquetes.tex
    paq_dates = {}
    for line in paq_txt.splitlines():
        mp = re.match(
            r"^\s*(\d+\.\d+\.\d+)\s*&\s*[A-Z]+\s*&\s*[^&]+&\s*(\d+)\s*&\s*(\d{2}-\d{2}-\d{4})\s*&\s*(\d{2}-\d{2}-\d{4})\s*&",
            line,
        )
        if mp:
            paq_dates[mp.group(1)] = {"hh": int(mp.group(2)), "ini": mp.group(3), "fin": mp.group(4)}

    assert cpm_rows["9.4.2"]["hh"] == cpm_rows["9.4.3"]["hh"] == 80
    assert cpm_rows["9.4.3"]["holgura"] >= 0
    assert (paq_dates["9.4.3"]["ini"], paq_dates["9.4.3"]["fin"]) == ("13-09-2028", "25-09-2028")
    assert paq_dates["1.7.9"]["fin"] == "07-11-2028"
    assert t10_rows["9.2.2"]["hh"] == "4928"
    assert "30-09-2028" in deps["D-33"]["fund"]

    return {
        "deps": deps,
        "milestones": milestones,
        "cpm": cpm_rows,
        "paq_dates": paq_dates,
        "t10": t10_rows,
        "n_deps": len(deps),
        "n_paq": n_paq,
        "n_h2_pkgs": n_h2_pkgs,
        "n_h2_acts": n_h2_acts,
        "n_h5_pkgs": n_h5_pkgs,
        "n_h5_acts": n_h5_acts,
        "n_post_h5": n_post_h5,
        "n_cont": n_cont,
    }


def make_diagram(diagram_id: str, name: str, bg_items: list[ET.Element], edges: list[ET.Element], nodes: list[ET.Element]) -> ET.Element:
    diag = ET.Element("diagram", {"id": diagram_id, "name": name})
    model = ET.SubElement(diag, "mxGraphModel", {"grid": "0", "page": "0", "pageScale": "1", "shadow": "0"})
    root = ET.SubElement(model, "root")
    ET.SubElement(root, "mxCell", {"id": "0"})
    ET.SubElement(root, "mxCell", {"id": "1", "parent": "0"})
    for bg in bg_items:
        root.append(bg)
    for e in edges:
        root.append(e)
    for n in nodes:
        root.append(n)
    return diag


def write_drawio(path: Path, diag: ET.Element) -> Path:
    mxfile = ET.Element("mxfile", {"host": "Electron"})
    mxfile.append(diag)
    tree = ET.ElementTree(mxfile)
    ET.indent(tree, space="  ")
    path.parent.mkdir(parents=True, exist_ok=True)
    tree.write(path, encoding="utf-8", xml_declaration=True)
    return path


def add_box(lst: list[ET.Element], cid: str, val: str, style: str, x: float, y: float, w: float, h: float) -> None:
    cell = ET.Element("mxCell", {"id": cid, "value": val, "style": style, "vertex": "1", "parent": "1"})
    ET.SubElement(cell, "mxGeometry", {"x": f"{x:.2f}", "y": f"{y:.2f}", "width": f"{w:.2f}", "height": f"{h:.2f}", "as": "geometry"})
    lst.append(cell)


def add_poly_edge(
    lst: list[ET.Element],
    eid: str,
    pts: list[tuple[float, float]],
    color: str = "#555555",
    width: float = 1.4,
    arrow: bool = True,
    dashed: bool = False,
) -> None:
    end_style = "endArrow=block;endFill=1;endSize=5;" if arrow else "endArrow=none;"
    dash_str = "dashed=1;dashPattern=5 4;" if dashed else ""
    style = f"html=1;rounded=0;{end_style}strokeColor={color};strokeWidth={width:.2f};{dash_str}"
    cell = ET.Element("mxCell", {"id": eid, "style": style, "edge": "1", "parent": "1"})
    geom = ET.SubElement(cell, "mxGeometry", {"relative": "1", "as": "geometry"})
    ET.SubElement(geom, "mxPoint", {"x": f"{pts[0][0]:.2f}", "y": f"{pts[0][1]:.2f}", "as": "sourcePoint"})
    ET.SubElement(geom, "mxPoint", {"x": f"{pts[-1][0]:.2f}", "y": f"{pts[-1][1]:.2f}", "as": "targetPoint"})
    if len(pts) > 2:
        arr = ET.SubElement(geom, "Array", {"as": "points"})
        for px, py in pts[1:-1]:
            ET.SubElement(arr, "mxPoint", {"x": f"{px:.2f}", "y": f"{py:.2f}"})
    lst.append(cell)


def hdr_style(bg: str = ROOT_COLOR, fs: float = 13.5) -> str:
    return (
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={bg};strokeColor={bg};"
        f"strokeWidth=1.2;spacing=0;fontFamily=Arial;absoluteArcSize=1;arcSize=10;"
        f"fontSize={fs};fontColor=#FFFFFF;align=center;verticalAlign=middle;"
        "spacingLeft=10;spacingRight=10;spacingTop=4;spacingBottom=4;"
    )


def build_red_precedencias(data: dict) -> Path:
    deps = data["deps"]
    m_h7 = data["milestones"]["H7"]
    m_h11 = data["milestones"]["H11"]
    m_h12 = data["milestones"]["H12"]

    bgs: list[ET.Element] = []
    edges: list[ET.Element] = []
    nodes: list[ET.Element] = []

    edge_map = {e[0]: (e[3], deps[e[3][0]]["tipo"]) for e in RED_EDGES}

    # Cabecera
    add_box(
        nodes,
        "hdr",
        "<b>Red de precedencias entre productos, cuentas de control e hitos</b>"
        '<br><span style="font-size:12.2px;">Dependencias D\u201101 a D\u201151 (Anexo 7.B) e hitos H1 a H12 (Formulario E\u201125)</span>',
        hdr_style(ROOT_COLOR, 13.5),
        0.0,
        2.0,
        W_CANVAS,
        48.0,
    )

    # Fondos de banda
    add_box(bgs, "bg_e1", "", "rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F7FA;strokeColor=#CFD8E3;strokeWidth=1.2;arcSize=4;", 0.0, 56.0, W_CANVAS, 422.0)
    add_box(bgs, "bg_e2", "", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FDF6F5;strokeColor=#E8C5BE;strokeWidth=1.2;arcSize=4;", 0.0, 486.0, W_CANVAS, 204.0)
    add_box(bgs, "bg_tr", "", "rounded=1;whiteSpace=wrap;html=1;fillColor=#F6F8F7;strokeColor=#D0D7D4;strokeWidth=1.2;arcSize=6;", 0.0, 698.0, W_CANVAS, 64.0)

    lbl_e1 = "text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;fontFamily=Arial;fontSize=12.4;fontColor=#1F4E79;fontStyle=1;"
    lbl_e2 = "text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;fontFamily=Arial;fontSize=12.4;fontColor=#A93226;fontStyle=1;"
    add_box(nodes, "t_e1", "<b>ETAPA 1 · meses 1 a 16 (H1 a H7)</b>", lbl_e1, 10.0, 60.0, 340.0, 20.0)
    add_box(nodes, "t_e2", "<b>ETAPA 2 · diseño H8 (m13–14) a H12 (m21) y Operación (m21–56)</b>", lbl_e2, 10.0, 490.0, 560.0, 20.0)

    def node_card(
        nid: str,
        x: float,
        y: float,
        w: float,
        h: float,
        prod: int,
        title: str,
        sub: str,
        fill_override: str | None = None,
        border_override: str | None = None,
        border_w: float = 1.4,
    ) -> None:
        strong, _ = PALETTE[prod]
        fill = fill_override or "#FFFFFF"
        border = border_override or strong
        st = (
            f"rounded=1;whiteSpace=wrap;html=1;fillColor={fill};strokeColor={border};"
            f"strokeWidth={border_w};spacing=0;fontFamily=Arial;absoluteArcSize=1;arcSize=8;"
            "fontSize=12.2;fontColor=#111111;align=left;verticalAlign=middle;"
            "spacingLeft=9;spacingRight=5;spacingTop=3;spacingBottom=3;"
        )
        add_box(nodes, nid, f"<b>{escape(title)}</b><br>{escape(sub)}", st, x, y, w, h)
        add_box(nodes, f"{nid}_bar", "", f"rounded=0;fillColor={strong};strokeColor=none;", x + 1.0, y + 4.0, 5.0, h - 8.0)

    def edge_pill(pid: str, text_html: str, x: float, y: float, w: float, h: float, bg: str = "#FFFFFF", color: str = "#1F2937") -> None:
        st = (
            f"rounded=1;whiteSpace=wrap;html=1;fillColor={bg};strokeColor=#CBD5E1;"
            f"strokeWidth=0.9;spacing=0;fontFamily=Arial;arcSize=18;fontSize=12.2;"
            f"fontColor={color};align=center;verticalAlign=middle;spacingLeft=3;spacingRight=3;"
        )
        add_box(nodes, pid, text_html, st, x, y, w, h)

    # Columnas: cw=150, brecha horizontal=63 px entre columnas
    cx = [6.0, 219.0, 432.0]
    cw = 146.0

    # Fila 1 (y=84, h=68)
    y1, h1 = 84.0, 68.0
    node_card("r1_c1", cx[0], y1, cw, h1, 2, "P2 · 2.1 Alcance E1 (H1)", nbh("2.1.1, 2.1.3–2.1.5 · D-03, D-40"))
    node_card("r1_c2", cx[1], y1, cw, h1, 2, "P2 · Diseño E1 (H2)", nbh("2.2–2.4, 2.6 → 2.8.1 · D-06"))
    node_card("r1_c3", cx[2], y1, cw, h1, 8, "P8/P3 · Sala, nube y H3", nbh("8.1–8.4, 8.7; 3.1–3.2 · D-07 a D-13"))

    # Fila 2 (y=190, h=68)
    y2, h2 = 190.0, 68.0
    node_card("r2_c1", cx[0], y2, cw, h2, 3, "P3/P5 · Base e integr.", nbh("3.3.1–3.3.6; 5.1–5.2 · D-39"))
    node_card("r2_c2", cx[1], y2, cw, h2, 4, "P4 · Módulos Etapa 1", nbh("4.1–4.3, 4.5.1 · DEV H2 · D-16–19"))
    node_card("r2_c3", cx[2], y2, cw, h2, 6, "P6 · 6.1.1 Integrac. (H4)", nbh("QA completo E1 · 3.3.4–6 · D-20"))

    # Fila 3 (y=296, h=68)
    y3, h3 = 296.0, 68.0
    node_card("r3_c1", cx[0], y3, cw, h3, 5, "P2/P5/P8 · Previo a MB", nbh("2.7 frío, 5.4 datos, 8.6 campo · D-24, 35–43"))
    node_card("r3_c2", cx[1], y3, cw, h3, 6, "P6 · Pruebas E1 (H5)", nbh("6.2–6.6 → 6.7.1 · D-22, D-23"))
    node_card("r3_c3", cx[2], y3, cw, h3, 9, "P9 · Olas, usuarios y actas", nbh("9.1.1–9.1.2, 9.5, 9.7 · D-49"))

    # Fila 4 (y=408, h=62) — w4=224 deja espacio holgado sin partir "paso 17-05"
    y4, h4 = 408.0, 62.0
    x4_l, x4_r, w4 = 18.0, 342.0, 224.0
    h7_acta = nbh(m_h7["acta"][:5])   # 16‑05
    h7_paso = nbh(m_h7["paso"][:5])   # 17‑05
    node_card(
        "r4_l", x4_l, y4, w4, h4, 9,
        "P9 · 9.2.1 Marcha blanca E1 (H6)",
        nbh("Conciliación diaria · mes 13–15"),
        fill_override="#DCE6F1", border_override="#1F4E79", border_w=1.6,
    )
    node_card(
        "r4_r", x4_r, y4, w4, h4, 9,
        "P9 · 9.4.1 Producción E1 (H7)",
        f"Expediente, acta {h7_acta}, paso\u00a0{h7_paso}",
        fill_override="#DDF0E3", border_override="#1E8449", border_w=1.6,
    )

    # Banda 2 — Fila 5 (y=514, h=66)
    y5, h5 = 514.0, 66.0
    node_card("r5_c1", cx[0], y5, cw, h5, 2, "P2 · Diseño E2 (H8)", nbh("2.1.2, 2.8.2 · mes 14"), border_override="#C0392B", border_w=1.8)
    node_card("r5_c2", cx[1], y5, cw, h5, 4, "P4 · Módulos Etapa 2", nbh("4.4.1–4.4.3, 4.5.2"), border_override="#C0392B", border_w=1.8)
    node_card("r5_c3", cx[2], y5, cw, h5, 6, "P6 · Certif. E2 (H9–H10)", nbh("6.1.2 → 6.2–6.6 → 6.7.2 · D-31–31c"), border_override="#C0392B", border_w=1.8)

    # Banda 2 — Fila 6 (y=614, h=68)
    y6, h6 = 614.0, 68.0
    h11_ini = nbh(m_h11["entrega"][:5])
    h12_acta = nbh(m_h12["acta"][:5])
    node_card("r6_c1", cx[0], y6, cw, h6, 5, "P5/P9 · Cadenas y previas", nbh("5.3, 9.1.3, 9.4.3, 9.5.4/8 · D-50"))
    node_card(
        "r6_c2", cx[1], y6, cw, h6, 9,
        "P9 · MB E2 (H11) y H12",
        f"9.2.2 ({h11_ini}) → 9.4.2 acta {h12_acta}",
        fill_override="#F5DFE2", border_override="#C0392B", border_w=1.8,
    )
    node_card(
        "r6_c3", cx[2], y6, cw, h6, 10,
        "P10/P1 · Operación y cierre",
        nbh("10.1–10.5 (m21–56) y 1.7.9"),
        fill_override="#E8EDDC", border_override="#4F5D2F", border_w=1.6,
    )

    # Banda 3 — Transversal (y=705, h=50)
    y7, h7 = 705.0, 50.0
    node_card("r7_l", 6.0, y7, 280.0, h7, 1, "P1 · Gobierno, riesgos y cumplimiento", nbh("Cuentas 1.1 a 1.8 transversales · D-39 (FC)"))
    node_card("r7_r", 298.0, y7, 280.0, h7, 7, "P7 · Innovaciones INN-01 a INN-05", nbh("Cuentas 7.1 a 7.5 · D-44 a D-47 (entregable parcial / FC)"))

    # Aristas Banda 1 + rótulos generados desde edge_map (tab_7B1.tex)
    add_poly_edge(edges, "e1", [(cx[0] + cw, y1 + h1 / 2), (cx[1], y1 + h1 / 2)], "#4A5568", 1.5)
    edge_pill("le1", f"<b>{nbh('D-01')}</b><br>{escape(edge_map['e1'][1])}", 156.5, y1 + h1 / 2 - 15, 58.0, 30.0)

    add_poly_edge(edges, "e1b", [(cx[1] + cw, y1 + h1 / 2), (cx[2], y1 + h1 / 2)], "#4A5568", 1.5)
    edge_pill("le1b", f"<b>{nbh('D-09')}</b><br>{escape(edge_map['e1b'][1])}", 372.5, y1 + h1 / 2 - 15, 52.0, 30.0)

    add_poly_edge(edges, "e2", [(cx[0] + cw / 2, y1 + h1), (cx[0] + cw / 2, y2)], "#4A5568", 1.5)
    edge_pill("le2", f"<b>{nbh('D-02, 40 · ' + edge_map['e2'][1])}</b>", cx[0] + 18, 159.0, 110.0, 22.0)

    add_poly_edge(edges, "e3", [(cx[1] + cw / 2, y1 + h1), (cx[1] + cw / 2, y2)], "#4A5568", 1.5)
    edge_pill("le3", f"<b>{nbh('D-04, 05 · ' + edge_map['e3'][1])}</b>", cx[1] + 18, 159.0, 110.0, 22.0)

    # D-14: 3.1 Ambientes (H3) condiciona entrega en QA (no inicio DEV) -> directo a r2_c3 QA
    add_poly_edge(edges, "e4", [(cx[2] + cw / 2, y1 + h1), (cx[2] + cw / 2, y2)], "#1F4E79", 1.5)
    edge_pill("le4", f"<b>{nbh('D-14 · ' + edge_map['e4'][1] + ' (solo QA)')}</b>", cx[2] + 4, 159.0, 138.0, 22.0, bg="#EFF6FF", color="#1F4E79")

    # D-15: CC (comienzo a comienzo) entre Base e integraciones y Módulos E1
    add_poly_edge(edges, "e5", [(cx[0] + cw, y2 + h2 / 2), (cx[1], y2 + h2 / 2)], "#1E8449", 1.6)
    edge_pill("le5", f"<b>{nbh('D-15')}</b><br><b>{escape(edge_map['e5'][1])}</b>", 159.5, y2 + h2 / 2 - 15, 52.0, 30.0, bg="#ECFDF5", color="#1E8449")

    add_poly_edge(edges, "e6", [(cx[1] + cw, y2 + h2 / 2), (cx[2], y2 + h2 / 2)], "#4A5568", 1.5)
    edge_pill("le6", f"<b>{nbh('D-20')}</b><br>{escape(edge_map['e6'][1])}", 372.5, y2 + h2 / 2 - 15, 52.0, 30.0)

    add_poly_edge(edges, "e9", [(cx[0] + cw / 2, y2 + h2), (cx[0] + cw / 2, y3)], "#4A5568", 1.4)
    edge_pill("le9", f"<b>{nbh('D-41 · ' + edge_map['e9'][1])}</b>", cx[0] + 28, 261.0, 90.0, 22.0)

    # e7 y e8 separados en corredores propios sin cruzar ninguna etiqueta
    add_poly_edge(edges, "e7", [(cx[2] + 34, y2 + h2), (cx[2] + 34, 288.0), (cx[1] + cw / 2, 288.0), (cx[1] + cw / 2, y3)], "#4A5568", 1.5)
    edge_pill("le7", f"<b>{nbh('D-21, 21b · ' + edge_map['e7'][1])}</b>", cx[1] + 18, 261.0, 110.0, 22.0)

    add_poly_edge(edges, "e8", [(cx[2] + 104, y2 + h2), (cx[2] + 104, y3)], "#4A5568", 1.4)
    edge_pill("le8", f"<b>{nbh('D-48 · ' + edge_map['e8'][1])}</b>", cx[2] + 62, 261.0, 84.0, 22.0)

    # Fila 3 -> Fila 4 (H6): etiquetas arriba (368..390) y codos horizontales despejados (395, 401)
    add_poly_edge(edges, "e10", [(cx[0] + cw / 2, y3 + h3), (cx[0] + cw / 2, y4)], "#4A5568", 1.4)
    edge_pill("le10", f"<b>{nbh('D-25, 26, 38 · ' + edge_map['e10'][1])}</b>", cx[0] + 8, 368.0, 130.0, 22.0)

    add_poly_edge(edges, "e11", [(cx[1] + cw / 2, y3 + h3), (cx[1] + cw / 2, 395.0), (x4_l + w4 / 2 + 26, 395.0), (x4_l + w4 / 2 + 26, y4)], "#4A5568", 1.5)
    edge_pill("le11", f"<b>{nbh('D-25 · ' + edge_map['e11'][1])}</b>", cx[1] + 26, 368.0, 94.0, 22.0)

    add_poly_edge(edges, "e12", [(cx[2] + cw / 2, y3 + h3), (cx[2] + cw / 2, 401.0), (x4_l + w4 - 16, 401.0), (x4_l + w4 - 16, y4)], "#4A5568", 1.4)
    edge_pill("le12", f"<b>{nbh('D-25, 27 · ' + edge_map['e12'][1])}</b>", cx[2] + 18, 368.0, 110.0, 22.0)

    # H6 -> H7
    add_poly_edge(edges, "e13", [(x4_l + w4, y4 + h4 / 2), (x4_r, y4 + h4 / 2)], "#1F4E79", 1.8)
    edge_pill("le13", f"<b>{nbh('D-28')}</b><br>{escape(edge_map['e13'][1])}", 262.0, y4 + h4 / 2 - 15, 60.0, 30.0)

    # Cadena roja E2 (SIN puente punteado 9.4.1 -> 9.2.2)
    add_poly_edge(edges, "e_r1", [(cx[0] + cw, y5 + h5 / 2), (cx[1], y5 + h5 / 2)], "#C0392B", 2.0)
    edge_pill("ler1", f"<b>{nbh('D-29')}</b><br>{escape(edge_map['e_r1'][1])}", 159.5, y5 + h5 / 2 - 15, 52.0, 30.0, color="#991B1B")

    add_poly_edge(edges, "e_r2", [(cx[1] + cw, y5 + h5 / 2), (cx[2], y5 + h5 / 2)], "#C0392B", 2.0)
    edge_pill("ler2", f"<b>{nbh('D-30')}</b><br>{escape(edge_map['e_r2'][1])}", 372.5, y5 + h5 / 2 - 15, 52.0, 30.0, color="#991B1B")

    add_poly_edge(edges, "e_r3", [(cx[2] + cw / 2, y5 + h5), (cx[2] + cw / 2, 597.0), (cx[1] + cw / 2, 597.0), (cx[1] + cw / 2, y6)], "#C0392B", 2.0)
    edge_pill("ler3", f"<b>{nbh('D-32 · ' + edge_map['e_r3'][1])}</b>", cx[2] + 28, 583.0, 90.0, 22.0, color="#991B1B")

    # Previas E2 -> H11/H12 -> Operación y cierre
    add_poly_edge(edges, "e14", [(cx[0] + cw, y6 + h6 / 2), (cx[1], y6 + h6 / 2)], "#4A5568", 1.5)
    edge_pill("le14", f"<b>{nbh('D-32, 33')}</b><br>{nbh('D-51 · ' + edge_map['e14'][1])}", 154.0, y6 + h6 / 2 - 15, 63.0, 30.0)

    add_poly_edge(edges, "e15", [(cx[1] + cw, y6 + h6 / 2), (cx[2], y6 + h6 / 2)], "#1E8449", 1.8)
    edge_pill("le15", f"<b>{nbh('D-34')}</b><br>{escape(edge_map['e15'][1])}", 372.5, y6 + h6 / 2 - 15, 52.0, 30.0, color="#1E8449")

    diag = make_diagram("red", "Red de precedencias", bgs, edges, nodes)
    return write_drawio(OUT_DIR / "Fig_Red_Precedencias_Productos.drawio", diag)


def build_cobertura_alcance() -> Path:
    bgs: list[ET.Element] = []
    edges: list[ET.Element] = []
    nodes: list[ET.Element] = []

    add_box(
        nodes,
        "hdr",
        "<b>Cobertura del alcance por componente y producto de la EDT</b>"
        '<br><span style="font-size:12.2px;">Ocho componentes de verificación (Tabla 7.2) y su ubicación en los diez productos</span>',
        hdr_style(ROOT_COLOR, 13.5),
        0.0,
        2.0,
        W_CANVAS,
        48.0,
    )

    cat_w = 206.0
    gap = 18.0
    right_x = cat_w + gap
    right_w = W_CANVAS - right_x

    rows = [
        ("Módulos", "M1–M12 y portales", [(4, "P4 · Cuentas 4.1 a 4.5")]),
        ("Interfaces", "ERP, WMS, flota y terceros", [(5, "P5 · Cuentas 5.1 a 5.3"), (6, "P6 · Contratos en 6.8.3")]),
        ("Servicios comunes", "Reglas, repositorio y plantillas", [(3, "P3 · 3.3.4–3.3.6"), (6, "P6 · Integración en 6.1.1")]),
        ("Innovaciones", "INN-01 a INN-05", [(7, "P7 · Cuentas 7.1 a 7.5")]),
        ("Seguridad", "Diseño, identidad, pruebas y física", [(2, "P2 · 2.3"), (3, "P3 · 3.3"), (6, "P6 · 6.5"), (8, "P8 · 8.5")]),
        ("Calidad", "Plan, puertas, pruebas y deuda", [(1, "P1 · 1.4"), (6, "P6 · 6.1 a 6.7"), (10, "P10 · 10.2.4")]),
        ("Migración", "Perfilamiento, carga y corte", [(5, "P5 · Cuenta 5.4")]),
        ("Implantación", "Olas, MB, capacitación y cambio", [(9, "P9 · Cuentas 9.1 a 9.6")]),
    ]

    cur_y = 62.0
    for r_idx, (cat_name, cat_sub, chips) in enumerate(rows):
        chip_rows = [chips] if len(chips) <= 2 else [chips[:2], chips[2:]]
        chip_h = 34.0
        chip_vgap = 6.0
        row_h = max(48.0, len(chip_rows) * chip_h + (len(chip_rows) - 1) * chip_vgap + 8.0)

        cat_style = (
            "rounded=1;whiteSpace=wrap;html=1;fillColor=#34495E;strokeColor=#2C3E50;"
            "strokeWidth=1.2;spacing=0;fontFamily=Arial;absoluteArcSize=1;arcSize=10;"
            "fontSize=12.5;fontColor=#FFFFFF;align=center;verticalAlign=middle;"
            "spacingLeft=8;spacingRight=8;spacingTop=3;spacingBottom=3;"
        )
        add_box(nodes, f"cat_{r_idx}", f"<b>{escape(cat_name)}</b><br><span style=\"font-size:12.2px;\">{escape(cat_sub)}</span>", cat_style, 0.0, cur_y, cat_w, row_h)
        add_box(bgs, f"cont_{r_idx}", "", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FAFAFA;strokeColor=#D5D8DC;strokeWidth=1.1;arcSize=8;", right_x, cur_y, right_w, row_h)

        ym = cur_y + row_h / 2.0
        add_poly_edge(edges, f"ec_{r_idx}", [(cat_w, ym), (right_x, ym)], "#555555", 1.5, arrow=True)

        inner_pad_x, inner_gap_x = 8.0, 8.0
        cy_chip = cur_y + (row_h - (len(chip_rows) * chip_h + (len(chip_rows) - 1) * chip_vgap)) / 2.0
        for cr_idx, crow in enumerate(chip_rows):
            cw_chip = (right_w - 2 * inner_pad_x - (len(crow) - 1) * inner_gap_x) / len(crow)
            for c_i, (pnum, ctext) in enumerate(crow):
                strong, light = PALETTE[pnum]
                cx_chip = right_x + inner_pad_x + c_i * (cw_chip + inner_gap_x)
                chip_style = (
                    f"rounded=1;whiteSpace=wrap;html=1;fillColor={light};strokeColor={strong};"
                    "strokeWidth=1.4;spacing=0;fontFamily=Arial;absoluteArcSize=1;arcSize=12;"
                    "fontSize=12.2;fontColor=#111111;align=center;verticalAlign=middle;spacingLeft=5;spacingRight=5;"
                )
                add_box(nodes, f"ch_{r_idx}_{cr_idx}_{c_i}", f"<b>{escape(ctext)}</b>", chip_style, cx_chip, cy_chip, cw_chip, chip_h)
            cy_chip += chip_h + chip_vgap
        cur_y += row_h + 10.0

    add_box(
        nodes,
        "nota",
        "Las pruebas de seguridad ofensiva (6.5.1–6.5.2) respaldan a la vez Seguridad y Calidad.",
        "rounded=1;whiteSpace=wrap;html=1;fillColor=#F4F6F7;strokeColor=#BDC3C7;strokeWidth=1.0;spacing=0;fontFamily=Arial;arcSize=10;fontSize=12.2;fontColor=#222222;align=center;verticalAlign=middle;spacingLeft=8;spacingRight=8;",
        0.0,
        cur_y + 2.0,
        W_CANVAS,
        32.0,
    )

    diag = make_diagram("cobertura", "Cobertura por productos", bgs, edges, nodes)
    return write_drawio(OUT_DIR / "Fig_Cobertura_Alcance_Productos.drawio", diag)


def build_planificacion_gradual(data: dict) -> Path:
    fin_179 = nbh(data["paq_dates"]["1.7.9"]["fin"])
    bgs: list[ET.Element] = []
    edges: list[ET.Element] = []
    nodes: list[ET.Element] = []

    add_box(
        nodes,
        "hdr",
        "<b>Planificación gradual del cronograma (regla 8/80 HH y quincena)</b>"
        f'<br><span style="font-size:12.2px;">230 paquetes EDT: {data["n_paq"]} con entregable y {data["n_cont"]} de esfuerzo continuo</span>',
        hdr_style(ROOT_COLOR, 13.5),
        0.0,
        2.0,
        W_CANVAS,
        48.0,
    )

    def tramo_card(tid: str, y: float, h: float, prod: int, title: str, badge: str, body: str, hitos: str, h_footer: float = 28.0) -> None:
        strong, light = PALETTE[prod]
        add_box(bgs, f"{tid}_bg", "", f"rounded=1;whiteSpace=wrap;html=1;fillColor={light};strokeColor={strong};strokeWidth=1.6;arcSize=8;", 0.0, y, W_CANVAS, h)
        add_box(
            nodes, f"{tid}_t", f"<b>{escape(title)}</b>",
            f"rounded=1;whiteSpace=wrap;html=1;fillColor={strong};strokeColor={strong};strokeWidth=1.0;fontFamily=Arial;fontSize=12.4;fontColor=#FFFFFF;align=left;verticalAlign=middle;spacingLeft=10;",
            10.0, y + 10.0, 344.0, 32.0,
        )
        add_box(
            nodes, f"{tid}_b", f"<b>{escape(badge)}</b>",
            f"rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor={strong};strokeWidth=1.3;fontFamily=Arial;fontSize=12.2;fontColor={strong};align=center;verticalAlign=middle;spacingLeft=6;spacingRight=6;",
            362.0, y + 10.0, 212.0, 32.0,
        )
        add_box(
            nodes, f"{tid}_d", body,
            "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#D5D8DC;strokeWidth=1.0;fontFamily=Arial;fontSize=12.2;fontColor=#111111;align=left;verticalAlign=middle;spacingLeft=10;spacingRight=10;",
            10.0, y + 48.0, 564.0, h - 62.0 - h_footer,
        )
        add_box(
            nodes, f"{tid}_h", f"<b>{escape(hitos)}</b>",
            f"rounded=0;whiteSpace=wrap;html=1;fillColor=none;strokeColor=none;fontFamily=Arial;fontSize=12.2;fontColor={strong};align=left;verticalAlign=middle;spacingLeft=4;",
            10.0, y + h - h_footer - 8.0, 564.0, h_footer,
        )

    y1, h1 = 62.0, 142.0
    tramo_card(
        "t1", y1, h1, 1,
        "Horizonte 1 · Meses 1 a 4 (hasta el H2)",
        f'{data["n_h2_pkgs"]} paquetes · {data["n_h2_acts"]} actividades',
        "<b>Detalle inmediato en actividades (Tablas 18 y 19):</b> paquetes de inicio, alcance, diseño y compras tempranas descompuestos en actividades de 8 a 80 HH dentro de una quincena (máximo 10 días hábiles).",
        "Hitos de control en el tramo: H1 (mes 2 · alcance E1) y H2 (mes 4 · arquitectura y diseño E1).",
    )

    y2, h2 = y1 + h1 + 20.0, 142.0
    tramo_card(
        "t2", y2, h2, 2,
        "Horizonte 2 · Meses 5 a 12 (entre H2 y H5)",
        f'{data["n_h5_pkgs"]} paquetes · {data["n_h5_acts"]} actividades',
        "<b>Detalle por plantilla de clase (Tabla 20):</b> módulos D, integraciones I, diseños E, instalaciones/capacitaciones T y pruebas ampliadas V detallados antes de construir (8 a 80 HH, quincena).",
        "Hitos de control en el tramo: H3 (mes 6 · infraestructura/nube), H4 (mes 10 · QA E1) y H5 (mes 12 · certificación E1).",
    )

    y3, h3 = y2 + h2 + 20.0, 166.0
    tramo_card(
        "t3", y3, h3, 7,
        "Horizonte 3 · Posteriores al H5 (desde el mes 13)",
        f'{data["n_post_h5"]} paquetes · gradual',
        "<b>Paquete de planificación gradual:</b> fechas, holguras y dependencias fijadas en línea base (Tablas 13 y 17). El líder de frente detalla las actividades de 8 a 80 HH antes de ejecutar, con aprobación del Comité de Proyecto y sin mover hitos.",
        f"Hitos: H6 (m13), H8 (m14), H7 (m16), H9 (m17), H10 (m18), H11 (m19), H12 (m21) y cierre 1.7.9 ({fin_179}, m22).",
        h_footer=34.0,
    )

    add_poly_edge(edges, "et12", [(W_CANVAS / 2, y1 + h1), (W_CANVAS / 2, y2)], "#1F4E79", 2.0)
    add_poly_edge(edges, "et23", [(W_CANVAS / 2, y2 + h2), (W_CANVAS / 2, y3)], PALETTE[2][0], 2.0)

    yc = y3 + h3 + 16.0
    strong_c, light_c = PALETTE[8]
    add_box(
        nodes,
        "t_cont",
        f'<b>Paquetes de esfuerzo continuo ({data["n_cont"]} paquetes · meses 1 a 56, Tabla 21)</b>'
        '<br>Gobierno, marchas blancas (9.2.1–9.2.2), estabilización (9.3.1–9.3.2) y 36 meses de Operación (Producto 10): relevos quincenales de hasta 64 HH (nivel de esfuerzo) u ocurrencias de hasta 80 HH (p. ej., 9.5.4 y 9.5.5).',
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={light_c};strokeColor={strong_c};strokeWidth=1.5;fontFamily=Arial;arcSize=8;fontSize=12.2;fontColor=#111111;align=left;verticalAlign=middle;spacingLeft=12;spacingRight=10;",
        0.0,
        yc,
        W_CANVAS,
        82.0,
    )

    diag = make_diagram("gradual", "Planificación gradual", bgs, edges, nodes)
    return write_drawio(OUT_DIR / "Fig_Planificacion_Gradual.drawio", diag)


def build_ruta_h12(data: dict) -> Path:
    m11 = data["milestones"]["H11"]
    m12 = data["milestones"]["H12"]
    cpm = data["cpm"]
    p_dates = data["paq_dates"]
    hh_922 = int(data["t10"]["9.2.2"]["hh"])

    f_h11 = nbh(m11["entrega"])
    f_evid = nbh("30-09-2028")
    f_943_ini = nbh(p_dates["9.4.3"]["ini"][:5])
    f_943_fin = nbh(p_dates["9.4.3"]["fin"])
    f_ent = nbh(m12["entrega"])
    f_acta = nbh(m12["acta"])
    f_paso = nbh(m12["paso"])
    f_lim = nbh(m12["limite"])
    hol_h12 = m12["holgura"]
    hol_943 = cpm["9.4.3"]["holgura"]
    hh_942 = cpm["9.4.2"]["hh"]
    hh_943 = cpm["9.4.3"]["hh"]

    bgs: list[ET.Element] = []
    edges: list[ET.Element] = []
    nodes: list[ET.Element] = []

    add_box(
        nodes,
        "hdr",
        "<b>Ruta de aceptación del hito H12 y holgura contractual</b>"
        '<br><span style="font-size:12.2px;">Secuencia de acta integrada para el cierre de la Etapa 2 (mes 21)</span>',
        hdr_style(ROOT_COLOR, 13.5),
        0.0,
        2.0,
        W_CANVAS,
        48.0,
    )

    main_w = 354.0
    side_x = 376.0
    side_w = W_CANVAS - side_x
    s9, l9 = PALETTE[9]
    s1, l1 = PALETTE[1]
    s10, l10 = PALETTE[10]
    s3, l3 = PALETTE[3]

    def step_box(nid: str, x: float, y: float, w: float, h: float, fill: str, stroke: str, html_val: str, dashed: bool = False) -> None:
        dash_str = "dashed=1;dashPattern=5 4;" if dashed else ""
        st = (
            f"rounded=1;whiteSpace=wrap;html=1;fillColor={fill};strokeColor={stroke};"
            f"strokeWidth=1.6;{dash_str}spacing=0;fontFamily=Arial;absoluteArcSize=1;arcSize=8;"
            "fontSize=12.2;fontColor=#111111;align=left;verticalAlign=middle;"
            "spacingLeft=10;spacingRight=10;spacingTop=4;spacingBottom=4;"
        )
        add_box(nodes, nid, html_val, st, x, y, w, h)

    # Paso 1: H11 01-08-2028 y cierre de evidencia 30-09-2028 (cierre formal en H12)
    y1, h1 = 64.0, 82.0
    step_box(
        "s1", 0.0, y1, main_w, h1, l9, s9,
        f"<b>1. Marcha blanca E2 (9.2.2 · H11): evidencia al {f_evid}</b>"
        f"<br>Inicio contractual H11: <b>{f_h11}</b> (meses 19–20 · {hh_922:,} HH)".replace(",", ".")
        + f"<br>Cierre de 4 semanas finales de evidencia: <b>{f_evid}</b> (cierre formal: acta H12)",
    )

    # Trámite paralelo: 9.4.3 Garantía de correcto funcionamiento
    y2, h2 = y1 + h1 + 24.0, 76.0
    step_box(
        "s_gar", side_x, y1 + 28.0, side_w, 146.0, "#FFFFFF", s9,
        "<b>Trámite paralelo · 9.4.3</b>"
        "<br><b>Garantía de correcto funcionamiento</b>"
        f"<br>{f_943_ini} al {f_943_fin} · {hh_943} HH"
        f"<br>Holgura CPM: {hol_943} días hábiles"
        f"<br>{nbh('Condición previa (D-33)')}",
        dashed=True,
    )

    # Paso 2: 9.4.2 Entrega de expediente H12
    step_box(
        "s2", 0.0, y2, main_w, h2, l9, s9,
        "<b>2. Entrega de expediente H12 (paquete 9.4.2)</b>"
        f"<br><b>{f_ent}</b> (primer día hábil tras cierre de evidencia)"
        f"<br>{hh_942} HH · incluye 9.2.2, 9.4.3, 9.5.4 y 9.5.8 ({nbh('D-33')})",
    )

    # Paso 3: Revisión contractual del CLIENTE (10 d.h.) y acta H12
    y3, h3 = y2 + h2 + 24.0, 86.0
    step_box(
        "s3", 0.0, y3, main_w, h3, l1, s1,
        "<b>3. Revisión contractual del CLIENTE y acta H12</b>"
        f"<br>Revisión contractual (10 d.h., Arts. 17.3 y 18.1): {nbh('03-10')} al {f_acta}"
        f"<br>Acta integrada H12 del <b>{f_acta}</b>: cierra la marcha blanca y autoriza el corte",
    )

    # Nota lateral: diferencia entre revisión interna previa y revisión contractual CLIENTE
    step_box(
        "s_note", side_x, y3 - 4.0, side_w, 94.0, "#F8F9F9", "#BDC3C7",
        "<b>6.8.6 · Verificación antes de la firma</b>"
        "<br>La prueba se completa durante la revisión nominal. Confirmar si debe acompañar el ingreso del expediente.",
    )

    # Paso 4: Paso a producción E2 e inicio de Operación
    y4, h4 = y3 + h3 + 24.0, 72.0
    step_box(
        "s4", 0.0, y4, W_CANVAS, h4, l10, s10,
        "<b>4. Corte de E2, registro e inicio de Operación (Producto 10)</b>"
        f"<br><b>{f_paso}</b> (día hábil siguiente al acta H12; habilita el cierre formal 1.7.9, {nbh('D-34')})",
    )

    # Paso 5: Holgura contractual disponible
    y5, h5 = y4 + h4 + 20.0, 64.0
    step_box(
        "s5", 0.0, y5, W_CANVAS, h5, l3, s3,
        f"<b>Holgura contractual disponible: {hol_h12} días hábiles ({nbh('D-33 · T-15, secs. 5.3 y 5.5')})</b>"
        f"<br>Margen entre el paso a producción (<b>{f_paso}</b>) y el límite contractual del mes 21 (<b>{f_lim}</b>)",
    )

    mx = main_w / 2.0
    add_poly_edge(edges, "er1", [(mx, y1 + h1), (mx, y2)], s9, 2.0)
    add_poly_edge(edges, "er2", [(mx, y2 + h2), (mx, y3)], s1, 2.0)
    add_poly_edge(edges, "er3", [(mx, y3 + h3), (mx, y4)], s10, 2.0)
    add_poly_edge(edges, "egar", [(side_x, y2 + h2 / 2.0), (main_w, y2 + h2 / 2.0)], s9, 1.8, dashed=True)
    add_poly_edge(edges, "ehol", [(W_CANVAS / 2.0, y4 + h4), (W_CANVAS / 2.0, y5)], s3, 2.0)

    diag = make_diagram("ruta_h12", "Ruta de H12", bgs, edges, nodes)
    return write_drawio(OUT_DIR / "Fig_Ruta_H12.drawio", diag)


def main() -> None:
    global OUT_DIR
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=OUT_DIR)
    OUT_DIR = parser.parse_args().output_dir.resolve()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    data = verify_live_sources()
    print(
        f"Fuentes verificadas: deps={data['n_deps']}, "
        f"paq={data['n_paq']} ({data['n_h2_pkgs']}/{data['n_h2_acts']}, "
        f"{data['n_h5_pkgs']}/{data['n_h5_acts']}, post={data['n_post_h5']}), "
        f"cont={data['n_cont']}"
    )
    for fn in [
        build_red_precedencias(data),
        build_cobertura_alcance(),
        build_planificacion_gradual(data),
        build_ruta_h12(data),
    ]:
        print(f"Generado: {fn.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
