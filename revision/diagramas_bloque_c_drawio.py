"""Genera las 4 figuras nuevas del Bloque C en formato draw.io (.drawio).

Figuras (en imagenes/Diagramas que faltaban/productos/, carta vertical W=584):
  1. Fig_Red_Precedencias_Productos.drawio  (fuente: tab_7B1.tex, tab_SD7_4.tex, tab_T15_7.tex)
  2. Fig_Cobertura_Alcance_Productos.drawio (fuente: tab_SD7_2.tex, dic_prod_1..10.tex)
  3. Fig_Planificacion_Gradual.drawio       (fuente: T-15 sec. 6.1, tab_T15_paquetes, 9, 9h5, 10)
  4. Fig_Ruta_H12.drawio                    (fuente: tab_T15_7, cpm_detalle, paquetes, 10, sec. 5.5)

Nunca escribe en archivos .tex ni sobrescribe imágenes antiguas.
"""
from __future__ import annotations

import re
from html import escape
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "imagenes" / "Diagramas que faltaban" / "productos"

PALETTE: dict[int, tuple[str, str]] = {
    1: ("#1F4E79", "#DCE6F1"),
    2: ("#2E86C1", "#DDEEF8"),
    3: ("#1E8449", "#DDF0E3"),
    4: ("#C0601A", "#FBE7D6"),
    5: ("#7D3C98", "#EBDDF1"),
    6: ("#8D5524", "#EFE3D8"),
    7: ("#148F77", "#D8F0EB"),
    8: ("#4D5656", "#E3E6E6"),
    9: ("#8B2635", "#F5DFE2"),
    10: ("#4F5D2F", "#E8EDDC"),
}

ROOT_COLOR = "#262626"
W_CANVAS = 584.0


def verify_live_sources() -> dict:
    """Lee y verifica cifras y códigos directamente desde las tablas vigentes."""
    tab_7b1 = (ROOT / "subdocumento-07-anexos" / "tablas" / "tab_7B1.tex").read_text(encoding="utf-8")
    deps = re.findall(r"^\s*(D-\d+[a-z]?)\s*&", tab_7b1, re.M)
    assert "D-01" in deps and "D-51" in deps and len(deps) == 54, f"tab_7B1 deps={len(deps)}"

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
    t10_codes = re.findall(r"^\s*(\d+\.\d+\.\d+)\s*&", t10, re.M)

    n_paq = len(paq_codes)
    n_h2_pkgs = len(set(t9_acts))
    n_h2_acts = len(t9_acts)
    n_h5_pkgs = len(t9h5_rows)
    n_h5_acts = sum(int(x[1]) for x in t9h5_rows)
    n_post_h5 = n_paq - n_h2_pkgs - n_h5_pkgs
    n_cont = len(t10_codes)

    assert (n_paq, n_h2_pkgs, n_h2_acts, n_h5_pkgs, n_h5_acts, n_post_h5, n_cont) == (
        171, 60, 119, 76, 385, 35, 59
    ), f"T-15 counts mismatch: {(n_paq, n_h2_pkgs, n_h2_acts, n_h5_pkgs, n_h5_acts, n_post_h5, n_cont)}"

    tab_7 = (ROOT / "formulario-t15" / "tablas" / "tab_T15_7.tex").read_text(encoding="utf-8")
    assert "02-10-2028" in tab_7 and "17-10-2028" in tab_7 and "18-10-2028" in tab_7 and "31-10-2028" in tab_7
    cpm = (ROOT / "formulario-t15" / "tablas" / "tab_T15_cpm_detalle.tex").read_text(encoding="utf-8")
    assert re.search(r"^\s*9\.4\.2\s*&.*&\s*8\s*&\s*80\s*\\\\", cpm, re.M)
    assert re.search(r"^\s*9\.4\.3\s*&.*&\s*12\s*&\s*80\s*\\\\", cpm, re.M)
    assert re.search(r"^\s*9\.4\.3\s*&.*13-09-2028\s*&\s*25-09-2028", paq_txt, re.M)
    assert re.search(r"^\s*9\.2\.2\s*&.*4928\s*&", t10, re.M)

    return {
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


def build_red_precedencias() -> Path:
    bgs: list[ET.Element] = []
    edges: list[ET.Element] = []
    nodes: list[ET.Element] = []

    # Cabecera
    add_box(
        nodes,
        "hdr",
        "<b>Red de precedencias entre productos, cuentas de control e hitos</b>"
        '<br><span style="font-size:12.2px;">Dependencias D-01 a D-51 (Anexo 7.B) e hitos H1 a H12 (Formulario E-25)</span>',
        hdr_style(ROOT_COLOR, 13.5),
        0.0,
        2.0,
        W_CANVAS,
        48.0,
    )

    # Fondos de banda
    add_box(
        bgs,
        "bg_e1",
        "",
        "rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F7FA;strokeColor=#CFD8E3;strokeWidth=1.2;arcSize=4;",
        0.0,
        58.0,
        W_CANVAS,
        380.0,
    )
    add_box(
        bgs,
        "bg_e2",
        "",
        "rounded=1;whiteSpace=wrap;html=1;fillColor=#FDF6F5;strokeColor=#E8C5BE;strokeWidth=1.2;arcSize=4;",
        0.0,
        446.0,
        W_CANVAS,
        208.0,
    )
    add_box(
        bgs,
        "bg_tr",
        "",
        "rounded=1;whiteSpace=wrap;html=1;fillColor=#F6F8F7;strokeColor=#D0D7D4;strokeWidth=1.2;arcSize=6;",
        0.0,
        662.0,
        W_CANVAS,
        66.0,
    )

    lbl_e1 = "text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;fontFamily=Arial;fontSize=12.5;fontColor=#1F4E79;fontStyle=1;"
    lbl_e2 = "text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;fontFamily=Arial;fontSize=12.5;fontColor=#A93226;fontStyle=1;"
    add_box(nodes, "t_e1", "<b>ETAPA 1 · meses 1 a 16 (H1 a H7)</b>", lbl_e1, 10.0, 62.0, 320.0, 22.0)
    # Comienza a la derecha del canal vertical x=194.5 para no ser cruzada por el puente E1->E2
    add_box(nodes, "t_e2", "<b>ETAPA 2 · H8 a H12 (m13–21) y Operación (m21–56)</b>", lbl_e2, 206.0, 450.0, 372.0, 22.0)

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
        strong, light = PALETTE[prod]
        fill = fill_override or "#FFFFFF"
        border = border_override or strong
        st = (
            f"rounded=1;whiteSpace=wrap;html=1;fillColor={fill};strokeColor={border};"
            f"strokeWidth={border_w};spacing=0;fontFamily=Arial;absoluteArcSize=1;arcSize=8;"
            "fontSize=12.2;fontColor=#111111;align=left;verticalAlign=middle;"
            "spacingLeft=10;spacingRight=6;spacingTop=3;spacingBottom=3;"
        )
        html_val = f"<b>{escape(title)}</b><br>{escape(sub)}"
        add_box(nodes, nid, html_val, st, x, y, w, h)
        # Barra de color de producto al borde izquierdo (estilo Fig_7-20)
        bar_st = f"rounded=0;fillColor={strong};strokeColor=none;"
        add_box(nodes, f"{nid}_bar", "", bar_st, x + 1.0, y + 4.0, 5.5, h - 8.0)

    # Coordenadas de columnas en Banda 1 y 2
    cx = [10.0, 205.0, 400.0]
    cw = 174.0

    # Fila 1 (y=88, h=64)
    y1, h1 = 88.0, 64.0
    node_card("r1_c1", cx[0], y1, cw, h1, 2, "P2 · 2.1 Alcance E1 (H1)", "2.1.1, 2.1.3–2.1.5 · D\u201101–03, D\u201140")
    node_card("r1_c2", cx[1], y1, cw, h1, 2, "P2 · Diseño E1 (H2)", "2.2–2.3, 2.6 → 2.8.1 · D\u201104 a D\u201106")
    node_card("r1_c3", cx[2], y1, cw, h1, 8, "P8/P3 · Sala, nube y H3", "8.1–8.4, 8.7; 3.1–3.2 · D\u201107 a D\u201114")

    # Fila 2 (y=176, h=66)
    y2, h2 = 176.0, 66.0
    node_card("r2_c1", cx[0], y2, cw, h2, 3, "P3/P5 · Base e integraciones", "3.3.1–3.3.6; 5.1–5.2 · D\u201115, D\u201139")
    node_card("r2_c2", cx[1], y2, cw, h2, 4, "P4 · Módulos Etapa 1", "4.1–4.3, 4.5.1 · D\u201116 a D\u201119")
    node_card("r2_c3", cx[2], y2, cw, h2, 6, "P6 · 6.1.1 Integrac. (H4)", "QA completo E1 · D\u201120")

    # Fila 3 (y=266, h=66)
    y3, h3 = 266.0, 66.0
    node_card("r3_c1", cx[0], y3, cw, h3, 5, "P2/P5/P8 · Previo a MB E1", "2.7 frío, 5.4 datos, 8.6 campo · D\u201124–38")
    node_card("r3_c2", cx[1], y3, cw, h3, 6, "P6 · Pruebas E1 (H5)", "6.2–6.6 → 6.7.1 · D\u201121 a D\u201123")
    node_card("r3_c3", cx[2], y3, cw, h3, 9, "P9 · Olas, usuarios y actas", "9.1.1–9.1.2, 9.5, 9.7 · D\u201127, D\u201148–49")

    # Fila 4 (y=356, h=66)
    y4, h4 = 356.0, 66.0
    x4_l, x4_r, w4 = 52.0, 322.0, 210.0
    node_card("r4_l", x4_l, y4, w4, h4, 9, "P9 · 9.2.1 Marcha blanca E1 (H6)", "Conciliación diaria · mes 13 · D\u201125", fill_override="#DCE6F1", border_override="#1F4E79", border_w=1.6)
    node_card("r4_r", x4_r, y4, w4, h4, 9, "P9 · 9.4.1 Producción E1 (H7)", "Expediente, acta 16-05 y paso 17-05 · D\u201128", fill_override="#DDF0E3", border_override="#1E8449", border_w=1.6)

    # Banda 2 — Fila 5 (y=476, h=66): Cadena crítica E2 en rojo
    y5, h5 = 476.0, 66.0
    node_card("r5_c1", cx[0], y5, cw, h5, 2, "P2 · Diseño E2 (H8)", "2.1.2, 2.8.2 · mes 14 · D\u201129", border_override="#C0392B", border_w=1.8)
    node_card("r5_c2", cx[1], y5, cw, h5, 4, "P4 · Módulos Etapa 2", "4.4.1–4.4.3, 4.5.2 · D\u201130", border_override="#C0392B", border_w=1.8)
    node_card("r5_c3", cx[2], y5, cw, h5, 6, "P6 · Certific. E2 (H9–H10)", "6.1.2 → 6.2–6.6 → 6.7.2 · D\u201131–31c", border_override="#C0392B", border_w=1.8)

    # Banda 2 — Fila 6 (y=568, h=70)
    y6, h6 = 568.0, 70.0
    node_card("r6_c1", cx[0], y6, cw, h6, 5, "P5/P9 · Cadenas y previas", "5.3.1–5.3.2, 9.1.3, 9.4.3, 9.5 · D\u201132–51")
    node_card("r6_c2", cx[1], y6, cw, h6, 9, "P9 · MB E2 (H11) y H12", "9.2.2 → 9.4.2 acta 17-10 · D\u201133", fill_override="#F5DFE2", border_override="#C0392B", border_w=1.8)
    node_card("r6_c3", cx[2], y6, cw, h6, 10, "P10/P1 · Operación y cierre", "10.1–10.5 (m21–56) y 1.7.9 · D\u201134", fill_override="#E8EDDC", border_override="#4F5D2F", border_w=1.6)

    # Banda 3 — Transversal (y=670, h=50)
    y7, h7 = 670.0, 50.0
    node_card("r7_l", 10.0, y7, 276.0, h7, 1, "P1 · Gobierno, riesgos y cumplimiento", "Cuentas 1.1 a 1.8 transversales · D\u201139")
    node_card("r7_r", 298.0, y7, 276.0, h7, 7, "P7 · Innovaciones INN-01 a INN-05", "Cuentas 7.1 a 7.5 por entregable parcial · D\u201144 a D\u201147")

    # Conectores Banda 1 (corredores y=164, y=254, y=344; canales x=194.5, x=389.5)
    add_poly_edge(edges, "e1", [(cx[0] + cw, y1 + h1 / 2), (cx[1], y1 + h1 / 2)], "#4A5568", 1.5)
    add_poly_edge(edges, "e2", [(cx[0] + 60, y1 + h1), (cx[0] + 60, y2)], "#4A5568", 1.5)  # D-02, D-40
    add_poly_edge(edges, "e3", [(cx[1] + cw / 2, y1 + h1), (cx[1] + cw / 2, y2)], "#4A5568", 1.5)
    add_poly_edge(edges, "e4", [(cx[2] + cw / 2, y1 + h1), (cx[2] + cw / 2, 162.0), (cx[1] + cw - 20, 162.0), (cx[1] + cw - 20, y2)], "#4A5568", 1.4)  # H3 -> QA E1 (D-14)
    add_poly_edge(edges, "e5", [(cx[0] + cw, y2 + h2 / 2), (cx[1], y2 + h2 / 2)], "#4A5568", 1.5)
    add_poly_edge(edges, "e6", [(cx[1] + cw, y2 + h2 / 2), (cx[2], y2 + h2 / 2)], "#4A5568", 1.5)
    add_poly_edge(edges, "e7", [(cx[2] + cw / 2, y2 + h2), (cx[2] + cw / 2, 254.0), (cx[1] + cw / 2, 254.0), (cx[1] + cw / 2, y3)], "#4A5568", 1.5)
    add_poly_edge(edges, "e8", [(cx[2] + cw / 2, y2 + h2), (cx[2] + cw / 2, y3)], "#4A5568", 1.4)
    add_poly_edge(edges, "e9", [(cx[0] + cw / 2, y2 + h2), (cx[0] + cw / 2, y3)], "#4A5568", 1.4)
    # Fila 3 -> Fila 4 (H6): bajadas rectas desde cada centro de columna sin quiebre innecesario
    add_poly_edge(edges, "e10", [(cx[0] + cw / 2, y3 + h3), (cx[0] + cw / 2, y4)], "#4A5568", 1.4)
    add_poly_edge(edges, "e11", [(cx[1] + cw / 2, y3 + h3), (cx[1] + cw / 2, 344.0), (x4_l + w4 / 2, 344.0), (x4_l + w4 / 2, y4)], "#4A5568", 1.5)
    add_poly_edge(edges, "e12", [(cx[2] + cw / 2, y3 + h3), (cx[2] + cw / 2, 344.0), (x4_l + w4 - 24, 344.0), (x4_l + w4 - 24, y4)], "#4A5568", 1.4)
    # Fila 4: 9.2.1 H6 -> 9.4.1 H7
    add_poly_edge(edges, "e13", [(x4_l + w4, y4 + h4 / 2), (x4_r, y4 + h4 / 2)], "#1F4E79", 1.8)

    # Puente limpio E1 -> E2 (desde H7 9.4.1 hasta MB E2 9.2.2 pasando por canal vacío x=194.5!)
    add_poly_edge(
        edges,
        "e_e1_e2",
        [(x4_r + w4 / 2, y4 + h4), (x4_r + w4 / 2, 434.0), (194.5, 434.0), (194.5, 554.0), (cx[1] + 28, 554.0), (cx[1] + 28, y6)],
        "#6E7781",
        1.4,
        dashed=True,
    )

    # Cadena roja E2 (D-29 a D-31c -> H11/H12)
    add_poly_edge(edges, "e_r1", [(cx[0] + cw, y5 + h5 / 2), (cx[1], y5 + h5 / 2)], "#C0392B", 2.0)
    add_poly_edge(edges, "e_r2", [(cx[1] + cw, y5 + h5 / 2), (cx[2], y5 + h5 / 2)], "#C0392B", 2.0)
    add_poly_edge(edges, "e_r3", [(cx[2] + cw / 2, y5 + h5), (cx[2] + cw / 2, 554.0), (cx[1] + cw / 2, 554.0), (cx[1] + cw / 2, y6)], "#C0392B", 2.0)

    # Previas E2 -> H11/H12 -> Operación y Cierre (D-32, D-33, D-34)
    add_poly_edge(edges, "e14", [(cx[0] + cw, y6 + h6 / 2), (cx[1], y6 + h6 / 2)], "#4A5568", 1.5)
    add_poly_edge(edges, "e15", [(cx[1] + cw, y6 + h6 / 2), (cx[2], y6 + h6 / 2)], "#1E8449", 1.8)

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

    # Columnas: izquierda componente (x=0, w=206), derecha chips de producto (x=224, w=360)
    cat_w = 206.0
    gap = 18.0
    right_x = cat_w + gap  # 224.0
    right_w = W_CANVAS - right_x  # 360.0

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
        n_chips = len(chips)
        if n_chips <= 2:
            chip_rows = [chips]
        else:
            chip_rows = [chips[:2], chips[2:]]

        chip_h = 34.0
        chip_vgap = 6.0
        row_h = max(48.0, len(chip_rows) * chip_h + (len(chip_rows) - 1) * chip_vgap + 8.0)

        cat_style = (
            "rounded=1;whiteSpace=wrap;html=1;fillColor=#34495E;strokeColor=#2C3E50;"
            "strokeWidth=1.2;spacing=0;fontFamily=Arial;absoluteArcSize=1;arcSize=10;"
            "fontSize=12.5;fontColor=#FFFFFF;align=center;verticalAlign=middle;"
            "spacingLeft=8;spacingRight=8;spacingTop=3;spacingBottom=3;"
        )
        cat_val = f"<b>{escape(cat_name)}</b><br><span style=\"font-size:12.2px;\">{escape(cat_sub)}</span>"
        add_box(nodes, f"cat_{r_idx}", cat_val, cat_style, 0.0, cur_y, cat_w, row_h)

        # Contenedor claro de la fila derecha
        cont_style = "rounded=1;whiteSpace=wrap;html=1;fillColor=#FAFAFA;strokeColor=#D5D8DC;strokeWidth=1.1;arcSize=8;"
        add_box(bgs, f"cont_{r_idx}", "", cont_style, right_x, cur_y, right_w, row_h)

        # Conector horizontal limpio entre tarjeta componente y contenedor
        ym = cur_y + row_h / 2.0
        add_poly_edge(edges, f"ec_{r_idx}", [(cat_w, ym), (right_x, ym)], "#555555", 1.5, arrow=True)

        # Chips de producto dentro del contenedor
        inner_pad_x = 8.0
        inner_gap_x = 8.0
        cy_chip = cur_y + (row_h - (len(chip_rows) * chip_h + (len(chip_rows) - 1) * chip_vgap)) / 2.0
        for cr_idx, crow in enumerate(chip_rows):
            cw_chip = (right_w - 2 * inner_pad_x - (len(crow) - 1) * inner_gap_x) / len(crow)
            for c_i, (pnum, ctext) in enumerate(crow):
                strong, light = PALETTE[pnum]
                cx_chip = right_x + inner_pad_x + c_i * (cw_chip + inner_gap_x)
                chip_style = (
                    f"rounded=1;whiteSpace=wrap;html=1;fillColor={light};strokeColor={strong};"
                    "strokeWidth=1.4;spacing=0;fontFamily=Arial;absoluteArcSize=1;arcSize=12;"
                    "fontSize=12.2;fontColor=#111111;align=center;verticalAlign=middle;"
                    "spacingLeft=5;spacingRight=5;"
                )
                add_box(nodes, f"ch_{r_idx}_{cr_idx}_{c_i}", f"<b>{escape(ctext)}</b>", chip_style, cx_chip, cy_chip, cw_chip, chip_h)
            cy_chip += chip_h + chip_vgap

        cur_y += row_h + 10.0

    # Nota de pie
    note_style = (
        "rounded=1;whiteSpace=wrap;html=1;fillColor=#F4F6F7;strokeColor=#BDC3C7;"
        "strokeWidth=1.0;spacing=0;fontFamily=Arial;arcSize=10;"
        "fontSize=12.2;fontColor=#222222;align=center;verticalAlign=middle;spacingLeft=8;spacingRight=8;"
    )
    add_box(
        nodes,
        "nota",
        "Las pruebas de seguridad ofensiva (6.5.1–6.5.2) respaldan a la vez Seguridad y Calidad.",
        note_style,
        0.0,
        cur_y + 2.0,
        W_CANVAS,
        32.0,
    )

    diag = make_diagram("cobertura", "Cobertura por productos", bgs, edges, nodes)
    return write_drawio(OUT_DIR / "Fig_Cobertura_Alcance_Productos.drawio", diag)


def build_planificacion_gradual(counts: dict) -> Path:
    bgs: list[ET.Element] = []
    edges: list[ET.Element] = []
    nodes: list[ET.Element] = []

    add_box(
        nodes,
        "hdr",
        "<b>Planificación gradual del cronograma (regla 8/80 HH y quincena)</b>"
        f'<br><span style="font-size:12.2px;">230 paquetes EDT: {counts["n_paq"]} con entregable y {counts["n_cont"]} de esfuerzo continuo</span>',
        hdr_style(ROOT_COLOR, 13.5),
        0.0,
        2.0,
        W_CANVAS,
        48.0,
    )

    def tramo_card(
        tid: str,
        y: float,
        h: float,
        prod: int,
        title: str,
        badge: str,
        body: str,
        hitos: str,
    ) -> None:
        strong, light = PALETTE[prod]
        # Contenedor
        add_box(
            bgs,
            f"{tid}_bg",
            "",
            f"rounded=1;whiteSpace=wrap;html=1;fillColor={light};strokeColor={strong};strokeWidth=1.6;arcSize=8;",
            0.0,
            y,
            W_CANVAS,
            h,
        )
        # Banda título izquierda-superior
        add_box(
            nodes,
            f"{tid}_t",
            f"<b>{escape(title)}</b>",
            f"rounded=1;whiteSpace=wrap;html=1;fillColor={strong};strokeColor={strong};strokeWidth=1.0;fontFamily=Arial;fontSize=12.6;fontColor=#FFFFFF;align=left;verticalAlign=middle;spacingLeft=10;",
            10.0,
            y + 10.0,
            326.0,
            32.0,
        )
        # Badge derecha con cifras
        add_box(
            nodes,
            f"{tid}_b",
            f"<b>{escape(badge)}</b>",
            f"rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor={strong};strokeWidth=1.3;fontFamily=Arial;fontSize=12.2;fontColor={strong};align=center;verticalAlign=middle;spacingLeft=6;spacingRight=6;",
            344.0,
            y + 10.0,
            230.0,
            32.0,
        )
        # Cuerpo descriptivo
        add_box(
            nodes,
            f"{tid}_d",
            body,
            "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#D5D8DC;strokeWidth=1.0;fontFamily=Arial;fontSize=12.2;fontColor=#111111;align=left;verticalAlign=middle;spacingLeft=10;spacingRight=10;",
            10.0,
            y + 48.0,
            564.0,
            h - 90.0,
        )
        # Hitos en pie de tramo
        add_box(
            nodes,
            f"{tid}_h",
            f"<b>{escape(hitos)}</b>",
            f"rounded=0;whiteSpace=wrap;html=1;fillColor=none;strokeColor=none;fontFamily=Arial;fontSize=12.2;fontColor={strong};align=left;verticalAlign=middle;spacingLeft=4;",
            10.0,
            y + h - 36.0,
            564.0,
            28.0,
        )

    y1, h1 = 64.0, 144.0
    tramo_card(
        "t1",
        y1,
        h1,
        1,
        "Horizonte 1 · Meses 1 a 4 (hasta el H2)",
        f'{counts["n_h2_pkgs"]} paquetes · {counts["n_h2_acts"]} actividades',
        "<b>Detalle inmediato en actividades (Tablas 18 y 19):</b> paquetes de inicio, alcance, diseño y compras tempranas descompuestos en actividades de 8 a 80 HH dentro de una quincena (máximo 10 días hábiles).",
        "Hitos de control en el tramo: H1 (mes 2 · alcance E1) y H2 (mes 4 · arquitectura y diseño E1).",
    )

    y2, h2 = y1 + h1 + 22.0, 144.0
    tramo_card(
        "t2",
        y2,
        h2,
        2,
        "Horizonte 2 · Meses 5 a 12 (entre H2 y H5)",
        f'{counts["n_h5_pkgs"]} paquetes · {counts["n_h5_acts"]} actividades',
        "<b>Detalle por plantilla de clase (Tabla 20):</b> módulos D, integraciones I, diseños E, instalaciones/capacitaciones T y pruebas ampliadas V detallados antes de construir (8 a 80 HH, quincena).",
        "Hitos de control en el tramo: H3 (mes 6 · infraestructura/nube), H4 (mes 10 · QA E1) y H5 (mes 12 · certificación E1).",
    )

    y3, h3 = y2 + h2 + 22.0, 154.0
    tramo_card(
        "t3",
        y3,
        h3,
        7,
        "Horizonte 3 · Meses 13 a 21 (posteriores al H5)",
        f'{counts["n_post_h5"]} paquetes · gradual',
        "<b>Paquete de planificación gradual:</b> fechas, holguras y dependencias fijadas en línea base (Tablas 13 y 17). El líder de frente detalla las actividades de 8 a 80 HH antes de ejecutar, con aprobación del Comité de Proyecto y sin mover hitos.",
        "Hitos de control: H6 (m13), H8 (m14), H7 (m16), H9 (m17), H10 (m18), H11 (m19) y H12 (m21).",
    )

    # Flechas de progresión temporal entre tramos
    add_poly_edge(edges, "et12", [(W_CANVAS / 2, y1 + h1), (W_CANVAS / 2, y2)], "#1F4E79", 2.0)
    add_poly_edge(edges, "et23", [(W_CANVAS / 2, y2 + h2), (W_CANVAS / 2, y3)], "#2E86C1", 2.0)

    # Banda inferior de esfuerzo continuo
    yc = y3 + h3 + 18.0
    strong_c, light_c = PALETTE[8]
    add_box(
        nodes,
        "t_cont",
        f'<b>Paquetes de esfuerzo continuo ({counts["n_cont"]} paquetes · meses 1 a 56, Tabla 21)</b>'
        '<br>Gobierno, marchas blancas (9.2.1–9.2.2), estabilización (9.3.1–9.3.2) y 36 meses de Operación (Producto 10): programados por quincena en relevos de hasta 64 HH máximas por puesto.',
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={light_c};strokeColor={strong_c};strokeWidth=1.5;fontFamily=Arial;arcSize=8;fontSize=12.2;fontColor=#111111;align=left;verticalAlign=middle;spacingLeft=12;spacingRight=10;",
        0.0,
        yc,
        W_CANVAS,
        74.0,
    )

    diag = make_diagram("gradual", "Planificación gradual", bgs, edges, nodes)
    return write_drawio(OUT_DIR / "Fig_Planificacion_Gradual.drawio", diag)


def build_ruta_h12() -> Path:
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
    side_w = W_CANVAS - side_x  # 208.0
    s9, l9 = PALETTE[9]
    s1, l1 = PALETTE[1]
    s10, l10 = PALETTE[10]
    s3, l3 = PALETTE[3]

    def step_box(nid: str, x: float, y: float, w: float, h: float, fill: str, stroke: str, html_val: str, dashed: bool = False) -> None:
        dash_str = "dashed=1;dashPattern=5 4;" if dashed else ""
        st = (
            f"rounded=1;whiteSpace=wrap;html=1;fillColor={fill};strokeColor={stroke};"
            f"strokeWidth=1.6;{dash_str}spacing=0;fontFamily=Arial;absoluteArcSize=1;arcSize=8;"
            "fontSize=12.4;fontColor=#111111;align=left;verticalAlign=middle;"
            "spacingLeft=10;spacingRight=10;spacingTop=4;spacingBottom=4;"
        )
        add_box(nodes, nid, html_val, st, x, y, w, h)

    # Paso 1: 9.2.2 Marcha blanca Etapa 2
    y1, h1 = 68.0, 74.0
    step_box(
        "s1",
        0.0,
        y1,
        main_w,
        h1,
        l9,
        s9,
        "<b>1. Cierre de marcha blanca E2 (paquete 9.2.2 · H11)</b>"
        "<br>Meses 19 y 20 · 4.928 HH (esfuerzo continuo)"
        "<br>Cierre de las 4 semanas finales de evidencia: <b>30-09-2028</b>",
    )

    # Rama paralela derecha: 9.4.3 Garantía de correcto funcionamiento (alineada con y2 + h2/2 = 205)
    step_box(
        "s_gar",
        side_x,
        y1 + 26.0,
        side_w,
        142.0,
        "#FFFFFF",
        s9,
        "<b>Trámite paralelo · 9.4.3</b>"
        "<br><b>Garantía de correcto funcionamiento</b>"
        "<br>13-09 al 25-09-2028 · 80 HH"
        "<br>Holgura CPM: 12 días hábiles"
        "<br>Condición previa (D\u201133)",
        dashed=True,
    )

    # Paso 2: 9.4.2 Entrega expediente H12
    y2, h2 = y1 + h1 + 26.0, 74.0
    step_box(
        "s2",
        0.0,
        y2,
        main_w,
        h2,
        l9,
        s9,
        "<b>2. Entrega de expediente H12 (paquete 9.4.2)</b>"
        "<br><b>02-10-2028</b> (primer día hábil tras el cierre)"
        "<br>80 HH · incluye 9.2.2, 9.4.3, 9.5.4 y 9.5.8 (D-33)",
    )

    # Paso 3: Revisión CLIENTE + Acta H12
    y3, h3 = y2 + h2 + 26.0, 76.0
    step_box(
        "s3",
        0.0,
        y3,
        main_w,
        h3,
        l1,
        s1,
        "<b>3. Revisión de Contraparte y acta H12 (Arts. 17.3 y 18.1)</b>"
        "<br>10 días hábiles de revisión: 03-10 al 17-10-2028"
        "<br>Firma del acta integrada H12: <b>17-10-2028</b>",
    )

    # Nota lateral explicativa de 9.4.2/H12 sin cruzar flechas
    step_box(
        "s_note",
        side_x,
        y3,
        side_w,
        h3,
        "#F8F9F9",
        "#BDC3C7",
        "<b>Control contractual</b>"
        "<br>Expediente revisado antes de entrega; sin usar las 4 semanas de marcha blanca como reserva.",
    )

    # Paso 4: Paso a producción E2 e Operación
    y4, h4 = y3 + h3 + 26.0, 70.0
    step_box(
        "s4",
        0.0,
        y4,
        W_CANVAS,
        h4,
        l10,
        s10,
        "<b>4. Paso a producción de la Etapa 2 e inicio de la Operación (Producto 10)</b>"
        "<br><b>18-10-2028</b> (día hábil siguiente al acta H12; habilita el cierre formal 1.7.9, D-34)",
    )

    # Paso 5: Franja de holgura contractual
    y5, h5 = y4 + h4 + 20.0, 62.0
    step_box(
        "s5",
        0.0,
        y5,
        W_CANVAS,
        h5,
        l3,
        s3,
        "<b>Holgura contractual disponible: 8 días hábiles (D-33 · T-15, secs. 5.3 y 5.5)</b>"
        "<br>Margen entre el paso a producción (<b>18-10-2028</b>) y el límite contractual del mes 21 (<b>31-10-2028</b>)",
    )

    # Flechas ortogonales limpias
    mx = main_w / 2.0
    add_poly_edge(edges, "er1", [(mx, y1 + h1), (mx, y2)], s9, 2.0)
    add_poly_edge(edges, "er2", [(mx, y2 + h2), (mx, y3)], s1, 2.0)
    add_poly_edge(edges, "er3", [(mx, y3 + h3), (mx, y4)], s10, 2.0)
    # Conector lateral limpio de Garantía 9.4.3 hacia costado derecho de 9.4.2
    add_poly_edge(edges, "egar", [(side_x, y2 + h2 / 2.0), (main_w, y2 + h2 / 2.0)], s9, 1.8, dashed=True)
    # Conector de Paso a producción hacia holgura límite contractual
    add_poly_edge(edges, "ehol", [(W_CANVAS / 2.0, y4 + h4), (W_CANVAS / 2.0, y5)], s3, 2.0)

    diag = make_diagram("ruta_h12", "Ruta de H12", bgs, edges, nodes)
    return write_drawio(OUT_DIR / "Fig_Ruta_H12.drawio", diag)


def main() -> None:
    counts = verify_live_sources()
    print(f"Fuentes verificadas: {counts}")
    for fn in [
        build_red_precedencias(),
        build_cobertura_alcance(),
        build_planificacion_gradual(counts),
        build_ruta_h12(),
    ]:
        print(f"Generado: {fn.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
