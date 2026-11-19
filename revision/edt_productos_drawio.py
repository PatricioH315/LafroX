"""Genera los diagramas editables de la EDT por producto en formato draw.io (.drawio).

Lee las fuentes vigentes del Formulario T-14 (tab_T14_1.tex y dic_prod_1..10.tex)
y construye en imagenes/Imagenes de la edt/productos/:
  - EDT-General.drawio: nivel 0 (proyecto) y nivel 1 (10 productos con conteos)
  - EDT-Producto-01.drawio .. EDT-Producto-10.drawio: cuentas y paquetes completos

Nunca modifica archivos .tex ni sobrescribe imágenes antiguas.
"""
from __future__ import annotations

import argparse
import math
import re
from dataclasses import dataclass
from html import escape
from pathlib import Path
import xml.etree.ElementTree as ET
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
T14_TABLES = ROOT / "formulario-t14" / "tablas"
OUT_DIR = ROOT / "imagenes" / "Imagenes de la edt" / "productos"

ARIAL_R = pymupdf.Font(fontfile="C:/Windows/Fonts/arial.ttf")
ARIAL_B = pymupdf.Font(fontfile="C:/Windows/Fonts/arialbd.ttf")

# Paleta por producto: (color fuerte de cabecera/borde, color claro de cuenta).
# Todos los colores fuertes cumplen contraste WCAG 2.1 AA >= 4,5:1 sobre blanco (#FFFFFF).
PALETTE: dict[int, tuple[str, str]] = {
    1: ("#1F4E79", "#DCE6F1"),
    2: ("#21699B", "#DDEEF8"),
    3: ("#1E8449", "#DDF0E3"),
    4: ("#A85012", "#FBE7D6"),
    5: ("#7D3C98", "#EBDDF1"),
    6: ("#8D5524", "#EFE3D8"),
    7: ("#0F7460", "#D8F0EB"),
    8: ("#4D5656", "#E3E6E6"),
    9: ("#8B2635", "#F5DFE2"),
    10: ("#4F5D2F", "#E8EDDC"),
}

ROOT_COLOR = "#262626"
TRUNK_COLOR = "#555555"

# Geometría para carta vertical (A.3: ancho <= 590, alto <= 768, fuente >= 12).
W_CANVAS = 584.0
H_MAX = 768.0


def bind_nbsp_percent(text: str) -> str:
    """Evita que el símbolo '%' quede huérfano al final de una línea."""
    return re.sub(r"(\d)\s+%", lambda m: f"{m.group(1)}\u00a0%", text)


@dataclass
class Package:
    code: str
    name: str


@dataclass
class Cuenta:
    code: str
    name: str
    packages: list[Package]


@dataclass
class Product:
    num: int
    name: str
    num_cuentas: int
    num_packages: int
    cuentas: list[Cuenta]


def clean_tex(s: str) -> str:
    s = s.replace(r"\allowbreak{}", "")
    s = s.replace(r"\ensuremath{\times}", "×")
    s = s.replace(r"\%", "%")
    s = s.replace("~", " ")
    s = s.replace("---", "—")
    s = s.replace("--", "–")
    s = re.sub(r"\\text(?:it|bf)\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\s+", " ", s).strip()
    assert "\\" not in s and "$" not in s, f"TeX residual no limpiado: {s}"
    return s


def load_edt_data() -> list[Product]:
    t14_1 = (T14_TABLES / "tab_T14_1.tex").read_text(encoding="utf-8")
    products: list[Product] = []

    for line in t14_1.splitlines():
        m = re.match(r"^\s*(\d+)\s*&\s*(.+?)\s*&\s*(\d+)\s*&\s*(\d+)\s*\\\\", line)
        if not m:
            continue
        pnum = int(m.group(1))
        pname = clean_tex(m.group(2))
        nc_exp = int(m.group(3))
        np_exp = int(m.group(4))

        dic_path = T14_TABLES / f"dic_prod_{pnum}.tex"
        cuentas: list[Cuenta] = []
        cur_cuenta: Cuenta | None = None

        for dline in dic_path.read_text(encoding="utf-8").splitlines():
            s = dline.strip()
            mc = re.search(r"\\textbf\{Cuenta\s+(\d+\.\d+)\s*[—–-]\s*([^}]+)\}", s)
            if mc:
                cname = clean_tex(mc.group(2)).rstrip(".")
                cur_cuenta = Cuenta(code=mc.group(1), name=cname, packages=[])
                cuentas.append(cur_cuenta)
                continue
            mp = re.match(r"^(\d+\.\d+\.\d+)\s*&\s*(.+?)\s*&", s)
            if mp:
                assert cur_cuenta is not None, f"Paquete sin cuenta previa: {s}"
                cur_cuenta.packages.append(Package(code=mp.group(1), name=clean_tex(mp.group(2))))

        assert len(cuentas) == nc_exp, f"P{pnum}: {len(cuentas)} CC != {nc_exp}"
        tot_p = sum(len(c.packages) for c in cuentas)
        assert tot_p == np_exp, f"P{pnum}: {tot_p} PT != {np_exp}"
        products.append(Product(pnum, pname, nc_exp, np_exp, cuentas))

    assert len(products) == 10, f"Se esperaban 10 productos, hay {len(products)}"
    assert sum(p.num_cuentas for p in products) == 60
    assert sum(p.num_packages for p in products) == 230
    return products


def estimate_wrapped_lines(
    words_with_bold: list[tuple[str, bool]],
    avail_w: float,
    fontsize: float,
    safety: float = 1.07,
) -> int:
    """Estima líneas al envolver en HTML (Arial) considerando segmentos con guion."""
    tokens: list[tuple[str, bool]] = []
    for word, is_bold in words_with_bold:
        # En HTML los cortes también ocurren tras '-' si es necesario, pero para ser conservador
        # medimos la palabra completa salvo que por sí sola supere avail_w.
        tokens.append((word, is_bold))

    space_w = ARIAL_R.text_length(" ", fontsize=fontsize) * safety
    lines = 1
    cur_w = 0.0
    for word, is_bold in tokens:
        font = ARIAL_B if is_bold else ARIAL_R
        ww = font.text_length(word, fontsize=fontsize) * safety
        if cur_w == 0.0:
            if ww <= avail_w:
                cur_w = ww
            else:
                # Si una palabra larga supera el ancho (ej. con guion), partir por segmentos
                cur_w = ww
        elif cur_w + space_w + ww <= avail_w:
            cur_w += space_w + ww
        else:
            lines += 1
            cur_w = ww
    return lines


def make_mxgraph_diagram(diagram_id: str, name: str, cells_edges: list[ET.Element], cells_nodes: list[ET.Element]) -> ET.Element:
    diag = ET.Element("diagram", {"id": diagram_id, "name": name})
    model = ET.SubElement(
        diag,
        "mxGraphModel",
        {"grid": "0", "page": "0", "pageScale": "1", "shadow": "0"},
    )
    root = ET.SubElement(model, "root")
    ET.SubElement(root, "mxCell", {"id": "0"})
    ET.SubElement(root, "mxCell", {"id": "1", "parent": "0"})
    for e in cells_edges:
        root.append(e)
    for n in cells_nodes:
        root.append(n)
    return diag


def add_edge(
    edges: list[ET.Element],
    eid: str,
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    color: str,
    width: float = 1.333,
) -> None:
    style = f"endArrow=none;html=1;rounded=0;strokeColor={color};strokeWidth={width:.3f};"
    cell = ET.Element("mxCell", {"id": eid, "style": style, "edge": "1", "parent": "1"})
    geom = ET.SubElement(cell, "mxGeometry", {"relative": "1", "as": "geometry"})
    ET.SubElement(geom, "mxPoint", {"x": f"{x1:.2f}", "y": f"{y1:.2f}", "as": "sourcePoint"})
    ET.SubElement(geom, "mxPoint", {"x": f"{x2:.2f}", "y": f"{y2:.2f}", "as": "targetPoint"})
    edges.append(cell)


def add_box(
    nodes: list[ET.Element],
    nid: str,
    value_html: str,
    style: str,
    x: float,
    y: float,
    w: float,
    h: float,
) -> None:
    cell = ET.Element(
        "mxCell",
        {"id": nid, "value": value_html, "style": style, "vertex": "1", "parent": "1"},
    )
    ET.SubElement(
        cell,
        "mxGeometry",
        {"x": f"{x:.2f}", "y": f"{y:.2f}", "width": f"{w:.2f}", "height": f"{h:.2f}", "as": "geometry"},
    )
    nodes.append(cell)


def write_drawio(path: Path, diagrams: list[ET.Element]) -> None:
    mxfile = ET.Element("mxfile", {"host": "Electron"})
    for d in diagrams:
        mxfile.append(d)
    tree = ET.ElementTree(mxfile)
    ET.indent(tree, space="  ")
    path.parent.mkdir(parents=True, exist_ok=True)
    tree.write(path, encoding="utf-8", xml_declaration=True)


def build_edt_general(products: list[Product]) -> Path:
    edges: list[ET.Element] = []
    nodes: list[ET.Element] = []

    root_x, root_y, root_w, root_h = 32.0, 2.0, 520.0, 56.0
    root_style = (
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={ROOT_COLOR};strokeColor={ROOT_COLOR};"
        "strokeWidth=1.2;spacing=0;fontFamily=Arial;absoluteArcSize=1;arcSize=10;"
        "fontSize=13.5;fontColor=#FFFFFF;fontStyle=0;align=center;verticalAlign=middle;"
        "spacingLeft=10;spacingRight=10;spacingTop=5;spacingBottom=5;"
    )
    tot_c = sum(p.num_cuentas for p in products)
    tot_p = sum(p.num_packages for p in products)
    root_val = (
        "<b>Plataforma Digital de Misión Crítica — Distribuidora Puelche</b>"
        f'<br><span style="font-size:12.5px;">{len(products)} productos · {tot_c} cuentas de control · {tot_p} paquetes de trabajo</span>'
    )
    add_box(nodes, "root_box", root_val, root_style, root_x, root_y, root_w, root_h)

    col_gap = 28.0
    col_w = (W_CANVAS - col_gap) / 2.0  # 278.0
    cx = W_CANVAS / 2.0                 # 292.0
    card_h = 70.0
    row_gap = 16.0
    top_y = root_y + root_h + 22.0      # 80.0

    # Tronco vertical central desde raíz hasta eje medio de fila 5
    last_mid_y = top_y + 4 * (card_h + row_gap) + card_h / 2.0
    add_edge(edges, "e_trunk", cx, root_y + root_h, cx, last_mid_y, TRUNK_COLOR, 1.5)

    for idx, prod in enumerate(products):
        row = idx // 2
        col = idx % 2
        x = 0.0 if col == 0 else col_w + col_gap
        y = top_y + row * (card_h + row_gap)
        strong, _ = PALETTE[prod.num]
        style = (
            f"rounded=1;whiteSpace=wrap;html=1;fillColor={strong};strokeColor={strong};"
            "strokeWidth=1.2;spacing=0;fontFamily=Arial;absoluteArcSize=1;arcSize=8;"
            "fontSize=13;fontColor=#FFFFFF;fontStyle=0;align=center;verticalAlign=middle;"
            "spacingLeft=10;spacingRight=10;spacingTop=5;spacingBottom=5;"
        )
        val = (
            f"<b>{prod.num}. {escape(prod.name)}</b>"
            f'<br><span style="font-size:12.5px;">{prod.num_cuentas} cuentas · {prod.num_packages} paquetes</span>'
        )
        add_box(nodes, f"prod_{prod.num}", val, style, x, y, col_w, card_h)

        # Rama horizontal hacia cada tarjeta (emitir por fila una sola vez de col0 a col1)
        if col == 0:
            ymid = y + card_h / 2.0
            add_edge(edges, f"e_row_{row}", col_w, ymid, col_w + col_gap, ymid, TRUNK_COLOR, 1.5)

    diag = make_mxgraph_diagram("general", "EDT General", edges, nodes)
    out = OUT_DIR / "EDT-General.drawio"
    write_drawio(out, [diag])
    return out


def measure_cuenta(
    c: Cuenta,
    col_w: float,
    indent: float,
    fs_cta: float,
    fs_pkg: float,
    pad_cta: float,
    pad_pkg: float,
    pkg_gap: float,
) -> dict:
    inner_c = col_w - 14.0
    pkg_w = col_w - indent
    inner_p = pkg_w - 14.0
    line_c = fs_cta * 1.19
    line_p = fs_pkg * 1.19

    c_words = [(w, True) for w in bind_nbsp_percent(f"{c.code} {c.name}").split(" ")]
    clines = estimate_wrapped_lines(c_words, inner_c, fs_cta, safety=1.07)
    ch = max(32.0, math.ceil(clines * line_c + pad_cta))

    pkgs_layout = []
    for p in c.packages:
        disp_name = bind_nbsp_percent(p.name)
        words = disp_name.split(" ")
        p_words = [(p.code, True)] + [(w, False) for w in words]
        plines = estimate_wrapped_lines(p_words, inner_p, fs_pkg, safety=1.06)
        ph = max(23.0, math.ceil(plines * line_p + pad_pkg))
        pkgs_layout.append((Package(p.code, disp_name), ph))

    pkg_area_h = sum(ph for _, ph in pkgs_layout) + max(0, len(pkgs_layout) - 1) * pkg_gap
    return {
        "cuenta": c,
        "ch": ch,
        "pkgs": pkgs_layout,
        "pkg_area_h": pkg_area_h,
        "total_h": ch + 7.0 + pkg_area_h,
    }


def plan_product_pages(
    measured: list[dict],
    header_h: float,
    top_gap: float,
    row_gap: float,
    h_max: float,
) -> list[list[list[dict]]]:
    """Reparte cuentas en láminas (cada lámina es lista de filas de 1 o 2 cuentas).

    Mantiene el orden secuencial de cuentas y evita dejar una lámina con 1 sola cuenta
    para conservar constante el ancho completo W_CANVAS en todas las láminas.
    """
    top_y = 2.0 + header_h + top_gap
    pages: list[list[list[dict]]] = []
    cur_rows: list[list[dict]] = []
    cur_y = top_y

    # Agrupación inicial por pares [[c0, c1], [c2, c3], ...]
    pairs = [measured[i : i + 2] for i in range(0, len(measured), 2)]
    for pair in pairs:
        row_ch = max(item["ch"] for item in pair)
        row_h = max(row_ch + 7.0 + item["pkg_area_h"] for item in pair)
        needed = row_h if not cur_rows else (row_gap + row_h)
        if cur_rows and (cur_y + needed > h_max):
            pages.append(cur_rows)
            cur_rows = []
            cur_y = top_y
            needed = row_h
        cur_rows.append(pair)
        cur_y += needed
    if cur_rows:
        pages.append(cur_rows)

    def page_height(pg_rows: list[list[dict]]) -> float:
        h = top_y
        for idx_r, r in enumerate(pg_rows):
            if idx_r > 0:
                h += row_gap
            rch = max(item["ch"] for item in r)
            h += max(rch + 7.0 + item["pkg_area_h"] for item in r)
        return h

    # Equilibrar si la última lámina quedó demasiado corta (< 290 px) moviendo la última fila entera previa
    if len(pages) >= 2 and page_height(pages[-1]) < 290.0 and len(pages[-2]) >= 2:
        cand_last = [pages[-2][-1]] + pages[-1]
        if page_height(cand_last) <= h_max:
            pages[-1] = cand_last
            pages[-2].pop()

    for pi, pg in enumerate(pages):
        cnt = sum(len(r) for r in pg)
        if cnt == 1 and pi > 0 and len(pages[pi - 1]) >= 2:
            last_item = pg[0][0]
            prev_last_row = pages[pi - 1][-1]
            if len(prev_last_row) == 2:
                moved = prev_last_row.pop()
                pages[pi] = [[moved, last_item]]

    for pg in pages:
        for ri, row in enumerate(pg):
            if ri < len(pg) - 1:
                assert len(row) == 2, "Fila intermedia con una sola cuenta rompería el tronco central"

    return pages


def build_product_diagram(prod: Product) -> Path:
    strong, light = PALETTE[prod.num]
    col_gap = 22.0
    col_w = (W_CANVAS - col_gap) / 2.0  # 281.0
    indent = 13.0
    pkg_w = col_w - indent              # 268.0
    cx = W_CANVAS / 2.0                 # 292.0

    fs_hdr = 14.0
    fs_cta = 12.5
    fs_pkg = 12.5
    pad_cta = 8.0
    pad_pkg = 6.5
    pkg_gap = 3.5
    row_gap = 16.0
    top_gap = 16.0

    # Medir cabecera de producto (con espacio para sufijo « (1 de 2)»)
    hdr_w = 468.0
    hdr_x = (W_CANVAS - hdr_w) / 2.0
    hdr_words = [(w, True) for w in f"{prod.num}. {prod.name} (2 de 2)".split(" ")]
    hdr_lines = estimate_wrapped_lines(hdr_words, hdr_w - 20.0, fs_hdr, safety=1.07)
    hdr_h = max(44.0, math.ceil(hdr_lines * (fs_hdr * 1.22) + 12.0))

    measured = [
        measure_cuenta(c, col_w, indent, fs_cta, fs_pkg, pad_cta, pad_pkg, pkg_gap)
        for c in prod.cuentas
    ]
    pages = plan_product_pages(measured, hdr_h, top_gap, row_gap, H_MAX)
    n_pages = len(pages)

    diagrams: list[ET.Element] = []
    for p_idx, page_rows in enumerate(pages, start=1):
        edges: list[ET.Element] = []
        nodes: list[ET.Element] = []
        eid = 0
        nid = 0

        def next_e() -> str:
            nonlocal eid
            eid += 1
            return f"e{p_idx}_{eid}"

        def next_n() -> str:
            nonlocal nid
            nid += 1
            return f"n{p_idx}_{nid}"

        suffix = f" ({p_idx} de {n_pages})" if n_pages > 1 else ""
        hdr_title = f"<b>{prod.num}. {escape(prod.name)}{suffix}</b>"
        hdr_style = (
            f"rounded=1;whiteSpace=wrap;html=1;fillColor={strong};strokeColor={strong};"
            f"strokeWidth=1.2;spacing=0;fontFamily=Arial;absoluteArcSize=1;arcSize=10;"
            f"fontSize={fs_hdr};fontColor=#FFFFFF;fontStyle=0;align=center;verticalAlign=middle;"
            "spacingLeft=10;spacingRight=10;spacingTop=4;spacingBottom=4;"
        )
        add_box(nodes, next_n(), hdr_title, hdr_style, hdr_x, 2.0, hdr_w, hdr_h)

        cur_y = 2.0 + hdr_h + top_gap
        row_meta = []
        for row in page_rows:
            row_ch = max(it["ch"] for it in row)
            row_tot_h = max(row_ch + 7.0 + it["pkg_area_h"] for it in row)
            row_meta.append((cur_y, row_ch, row_tot_h, row))
            cur_y += row_tot_h + row_gap

        # Conectores del tronco central (desde cabecera hasta la última fila)
        last_y, _, _, last_row = row_meta[-1]
        if len(last_row) == 2:
            trunk_end_y = last_y - row_gap / 2.0
        else:
            trunk_end_y = last_y
        add_edge(edges, next_e(), cx, 2.0 + hdr_h, cx, trunk_end_y, TRUNK_COLOR, 1.333)

        cta_style = (
            f"rounded=1;whiteSpace=wrap;html=1;fillColor={light};strokeColor={strong};"
            f"strokeWidth=1.6;spacing=0;fontFamily=Arial;absoluteArcSize=1;arcSize=8;"
            f"fontSize={fs_cta};fontColor=#111111;fontStyle=0;align=center;verticalAlign=middle;"
            "spacingLeft=6;spacingRight=6;spacingTop=4;spacingBottom=4;"
        )
        pkg_style = (
            f"rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor={strong};"
            f"strokeWidth=1.1;spacing=0;fontFamily=Arial;"
            f"fontSize={fs_pkg};fontColor=#111111;fontStyle=0;align=left;verticalAlign=middle;"
            "spacingLeft=7;spacingRight=6;spacingTop=3;spacingBottom=3;"
        )

        for ry, row_ch, _, row in row_meta:
            if len(row) == 2:
                xs = [0.0, col_w + col_gap]
                by = ry - row_gap / 2.0
                c_left_mid = xs[0] + col_w / 2.0
                c_right_mid = xs[1] + col_w / 2.0
                add_edge(edges, next_e(), c_left_mid, by, c_right_mid, by, TRUNK_COLOR, 1.333)
                add_edge(edges, next_e(), c_left_mid, by, c_left_mid, ry, TRUNK_COLOR, 1.333)
                add_edge(edges, next_e(), c_right_mid, by, c_right_mid, ry, TRUNK_COLOR, 1.333)
            else:
                xs = [(W_CANVAS - col_w) / 2.0]

            for col_x, item in zip(xs, row):
                c: Cuenta = item["cuenta"]
                c_html = f"<b>{c.code} {escape(bind_nbsp_percent(c.name))}</b>"
                add_box(nodes, next_n(), c_html, cta_style, col_x, ry, col_w, row_ch)

                rail_x = col_x + indent / 2.0
                pkg_x = col_x + indent
                py = ry + row_ch + 7.0
                pkg_mids = []
                for p, ph in item["pkgs"]:
                    p_html = f"<b>{p.code}</b> {escape(p.name)}"
                    add_box(nodes, next_n(), p_html, pkg_style, pkg_x, py, pkg_w, ph)
                    pkg_mids.append(py + ph / 2.0)
                    py += ph + pkg_gap

                if pkg_mids:
                    add_edge(edges, next_e(), rail_x, ry + row_ch, rail_x, pkg_mids[-1], strong, 1.333)
                    for ym in pkg_mids:
                        add_edge(edges, next_e(), rail_x, ym, pkg_x, ym, strong, 1.333)

        diag_name = f"{p_idx} de {n_pages}" if n_pages > 1 else "EDT"
        diagrams.append(make_mxgraph_diagram(f"p{p_idx}", diag_name, edges, nodes))

    out = OUT_DIR / f"EDT-Producto-{prod.num:02d}.drawio"
    write_drawio(out, diagrams)
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--products", default="all", help="Lista separada por comas (ej. general,1) o 'all'")
    args = parser.parse_args()

    products = load_edt_data()
    targets = {t.strip().lower() for t in args.products.split(",")}

    if "all" in targets or "general" in targets:
        out_gen = build_edt_general(products)
        print(f"Generado: {out_gen.relative_to(ROOT)}")

    for prod in products:
        if "all" in targets or str(prod.num) in targets:
            out_p = build_product_diagram(prod)
            print(f"Generado: {out_p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
