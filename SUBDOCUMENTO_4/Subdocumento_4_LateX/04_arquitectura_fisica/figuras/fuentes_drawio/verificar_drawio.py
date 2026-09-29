"""Verifica las vistas v3 de draw.io: legibilidad impresa y geometría V1–V6.

Uso: python verificar_drawio.py [archivo_v3.drawio ...]
Sin argumentos revisa únicamente los dos archivos *_v3.drawio de esta carpeta.
"""
from __future__ import annotations

import html
import math
import re
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

HERE = Path(__file__).resolve().parent
EPS = 0.01
Box = tuple[float, float, float, float]
Point = tuple[float, float]


def style_of(raw: str) -> dict[str, str]:
    return dict(part.split("=", 1) for part in raw.split(";") if "=" in part)


def number(raw: str | None) -> float:
    return float(raw or 0)


def rect(x: float, y: float, w: float, h: float) -> Box:
    return x, y, x + w, y + h


def unite(a: Box | None, b: Box) -> Box:
    if a is None:
        return b
    return min(a[0], b[0]), min(a[1], b[1]), max(a[2], b[2]), max(a[3], b[3])


def overlap(a: Box, b: Box) -> bool:
    return (min(a[2], b[2]) - max(a[0], b[0]) > EPS
            and min(a[3], b[3]) - max(a[1], b[1]) > EPS)


def hit(p: Point, q: Point, b: Box) -> bool:
    if abs(p[0] - q[0]) < EPS:
        return (b[0] - EPS <= p[0] <= b[2] + EPS
                and min(p[1], q[1]) < b[3] - EPS
                and max(p[1], q[1]) > b[1] + EPS)
    return (b[1] - EPS <= p[1] <= b[3] + EPS
            and min(p[0], q[0]) < b[2] - EPS
            and max(p[0], q[0]) > b[0] + EPS)


def parallel_gap(p: Point, q: Point, r: Point, s: Point) -> float:
    if abs(p[0] - q[0]) < EPS and abs(r[0] - s[0]) < EPS:
        common = min(max(p[1], q[1]), max(r[1], s[1])) - max(min(p[1], q[1]), min(r[1], s[1]))
        if common > EPS:
            return abs(p[0] - r[0])
    if abs(p[1] - q[1]) < EPS and abs(r[1] - s[1]) < EPS:
        common = min(max(p[0], q[0]), max(r[0], s[0])) - max(min(p[0], q[0]), min(r[0], s[0]))
        if common > EPS:
            return abs(p[1] - r[1])
    return math.inf


def crosses_interior(p: Point, q: Point, b: Box) -> bool:
    """True only for positive-length travel inside an open container rectangle."""
    if abs(p[0] - q[0]) < EPS:
        return (b[0] + EPS < p[0] < b[2] - EPS
                and min(max(p[1], q[1]), b[3])
                - max(min(p[1], q[1]), b[1]) > EPS)
    if abs(p[1] - q[1]) < EPS:
        return (b[1] + EPS < p[1] < b[3] - EPS
                and min(max(p[0], q[0]), b[2])
                - max(min(p[0], q[0]), b[0]) > EPS)
    return False


def rows(value: str, width: float, size: float) -> list[str]:
    clean = re.sub(r"(?i)<br\s*/?\s*>", "\n", html.unescape(value))
    clean = re.sub(r"<[^>]*>", "", clean)
    limit = max(1, math.floor(width / (0.68 * size))) if size else 1
    result: list[str] = []
    for line in clean.split("\n"):
        current = ""
        for word in line.split():
            candidate = (current + " " + word).strip()
            if current and len(candidate) > limit:
                result.append(current)
                current = word
            else:
                current = candidate
        result.append(current)
    return result


def text_box(value: str, width: float, size: float, cx: float, cy: float) -> tuple[list[str], float, float, Box]:
    lines = rows(value, width, size)
    tw = max((len(line) * 0.68 * size for line in lines), default=0) + 8
    th = len(lines) * 1.2 * size + 8
    return lines, tw, th, rect(cx - tw / 2, cy - th / 2, tw, th)


def sides(b: Box) -> list[tuple[Point, Point]]:
    x1, y1, x2, y2 = b
    return [((x1, y1), (x2, y1)), ((x1, y2), (x2, y2)),
            ((x1, y1), (x1, y2)), ((x2, y1), (x2, y2))]


def at_path(points: list[Point], relative: float) -> tuple[float, float, Point, Point]:
    lengths = [abs(q[0] - p[0]) + abs(q[1] - p[1]) for p, q in zip(points, points[1:])]
    distance = sum(lengths) * (relative + 1) / 2
    for (p, q), length in zip(zip(points, points[1:]), lengths):
        if distance <= length + EPS:
            ratio = distance / length if length else 0
            return (p[0] + (q[0] - p[0]) * ratio,
                    p[1] + (q[1] - p[1]) * ratio, p, q)
        distance -= length
    return points[-1][0], points[-1][1], points[-2], points[-1]


def inspect(path: Path) -> tuple[float, float, float, list[str]]:
    errors: list[str] = []
    try:
        root = ET.parse(path).getroot()
        model = root.find("./diagram/mxGraphModel")
        if model is None:
            raise ValueError("Falta mxGraphModel sin comprimir")
    except (ET.ParseError, ValueError) as exc:
        return 0, 0, 0, [f"XML: {exc}"]

    cells = {c.get("id"): c for c in model.findall("./root/mxCell")}
    vertices = {key: c for key, c in cells.items() if c.get("vertex") == "1"}
    edges = {key: c for key, c in cells.items() if c.get("edge") == "1"}
    geo: dict[str, Box] = {}

    def absolute(key: str) -> Box:
        if key in geo:
            return geo[key]
        cell = vertices[key]
        g = cell.find("mxGeometry")
        if g is None:
            raise ValueError(f"{key}: sin mxGeometry")
        x, y = number(g.get("x")), number(g.get("y"))
        parent = cell.get("parent")
        if parent in vertices:
            p = absolute(parent)
            x, y = x + p[0], y + p[1]
        geo[key] = rect(x, y, number(g.get("width")), number(g.get("height")))
        return geo[key]

    for key in vertices:
        try:
            absolute(key)
        except (ValueError, RecursionError) as exc:
            errors.append(str(exc))
    if not geo:
        return 0, 0, 0, errors + ["Sin vértices"]

    groups: list[str] = []
    titles: dict[str, Box] = {}
    leaves: dict[str, Box] = {}
    leaf_parts: dict[str, list[Box]] = {}
    bounds: Box | None = None
    minimum = math.inf
    for key, cell in vertices.items():
        if key not in geo:
            continue
        b = geo[key]
        s = style_of(cell.get("style", ""))
        value = cell.get("value", "")
        group = s.get("container") == "1" or s.get("shape") == "mxgraph.aws4.group"
        bounds = unite(bounds, b)
        if group:
            groups.append(key)
        else:
            leaves[key] = b
            leaf_parts[key] = [b]
        if not value.strip():
            shape = s.get("shape", "")
            if shape == "image" or shape.startswith("mxgraph.aws4."):
                label_id = cell.get("data-label")
                if label_id not in vertices:
                    errors.append(f"{key}: icono sin rótulo inferior asociado")
                elif label_id in geo:
                    label_box = geo[label_id]
                    horizontal_centers = abs((b[0] + b[2]) / 2 - (label_box[0] + label_box[2]) / 2)
                    if label_box[1] < b[3] - EPS or horizontal_centers > 5:
                        errors.append(f"{key}: rótulo no está debajo y centrado")
            continue
        size = number(s.get("fontSize"))
        minimum = min(minimum, size)
        if size < 24:
            errors.append(f"{key}: fontSize < 24")
        if s.get("fontStyle") != "1":
            errors.append(f"{key}: texto sin negrita")
        if not group:
            clean = re.sub(r"(?i)<br\s*/?\s*>", "\n", html.unescape(value))
            clean = re.sub(r"<[^>]*>", "", clean)
            words = re.findall(r"\S+", clean)
            logical_lines = clean.splitlines() or [clean]
            exception = path.name == "Arquitectura_Fisica_General_v3.drawio" and key == "mini_label"
            if not exception and (len(words) > 4 or len(logical_lines) > 2):
                errors.append(f"{key}: texto de hoja > 4 palabras o > 2 líneas")
        if group:
            left, top = number(s.get("spacingLeft")), number(s.get("spacingTop"))
            available = b[2] - b[0] - left - 16
            lines, tw, th, _ = text_box(value, available, size, 0, 0)
            if len(lines) > 1:
                errors.append(f"{key}: título de contenedor partido")
            if tw > available + EPS or th > b[3] - b[1] - top + EPS:
                errors.append(f"{key}: título desborda contenedor")
            title = rect(b[0] + left, b[1] + top, tw, th)
            titles[key] = title
            bounds = unite(bounds, title)
        elif s.get("verticalLabelPosition") == "bottom":
            _, tw, th, _ = text_box(value, b[2] - b[0], size, (b[0] + b[2]) / 2, 0)
            label = rect((b[0] + b[2] - tw) / 2, b[3] + 3, tw, th)
            leaves[key] = unite(b, label)
            leaf_parts[key] = [b, label]
            bounds = unite(bounds, label)
        else:
            space = number(s.get("spacing"))
            available = b[2] - b[0] - 2 * space
            _, tw, th, label = text_box(value, available, size, (b[0] + b[2]) / 2, (b[1] + b[3]) / 2)
            if tw > available + EPS or th > b[3] - b[1] - 2 * space + EPS:
                errors.append(f"{key}: texto desborda caja")
            leaves[key] = unite(b, label)
            bounds = unite(bounds, label)

    for key, a in leaves.items():
        for other, b in leaves.items():
            if key < other and overlap(a, b):
                errors.append(f"{key}/{other}: hojas superpuestas")
        for other, b in titles.items():
            if overlap(a, b):
                errors.append(f"{key}: hoja sobre título {other}")
    for key, parts in leaf_parts.items():
        for b in parts:
            for group in groups:
                c = geo[group]
                inside = (b[0] >= c[0] - EPS and b[1] >= c[1] - EPS
                          and b[2] <= c[2] + EPS and b[3] <= c[3] + EPS)
                if not inside and overlap(b, c):
                    errors.append(f"{key}: hoja sobre borde de {group}")
                if inside and any(abs(x - y) < EPS for x, y in zip(b, c)):
                    errors.append(f"{key}: hoja toca borde de {group}")

    paths: dict[str, list[Point]] = {}
    edge_labels: dict[str, Box] = {}
    page_w = number(model.get("pageWidth")) or 1700
    page_h = number(model.get("pageHeight")) or 1100
    canvas_sides = sides(rect(0, 0, page_w, page_h))
    for key, cell in edges.items():
        s = style_of(cell.get("style", ""))
        source, target = cell.get("source"), cell.get("target")
        if source not in geo or target not in geo:
            errors.append(f"{key}: extremo ausente")
            continue
        required = ("exitX", "exitY", "exitDx", "exitDy", "entryX", "entryY", "entryDx", "entryDy")
        if any(item not in s for item in required):
            errors.append(f"{key}: anclajes incompletos")
            continue
        if s.get("edgeStyle") != "none" or s.get("rounded") != "0":
            errors.append(f"{key}: estilo de arista no determinista")
        allowed: set[str] = set()
        for endpoint in (source, target):
            current = endpoint
            while current in vertices:
                allowed.add(current)
                current = vertices[current].get("parent")
        a, b = geo[source], geo[target]
        start = (a[0] + (a[2] - a[0]) * number(s["exitX"]), a[1] + (a[3] - a[1]) * number(s["exitY"]))
        end = (b[0] + (b[2] - b[0]) * number(s["entryX"]), b[1] + (b[3] - b[1]) * number(s["entryY"]))
        g = cell.find("mxGeometry")
        arr = g.find("Array[@as='points']") if g is not None else None
        points = [start]
        if arr is not None:
            points += [(number(p.get("x")), number(p.get("y"))) for p in arr.findall("mxPoint")]
        points.append(end)
        paths[key] = points
        for p in points:
            bounds = unite(bounds, (p[0], p[1], p[0], p[1]))
        for p, q in zip(points, points[1:]):
            if abs(p[0] - q[0]) > EPS and abs(p[1] - q[1]) > EPS:
                errors.append(f"{key}: diagonal")
            for other, obstacle in leaves.items():
                if other not in (source, target) and hit(p, q, obstacle):
                    errors.append(f"{key}: atraviesa hoja {other}")
            for other, obstacle in titles.items():
                if hit(p, q, obstacle):
                    errors.append(f"{key}: atraviesa título {other}")
            for group in groups:
                if group not in allowed and crosses_interior(p, q, geo[group]):
                    errors.append(f"{key}: entra en contenedor ajeno {group}")
                for r, t in sides(geo[group]):
                    if parallel_gap(p, q, r, t) < 15 - EPS:
                        errors.append(f"{key}: paralelo al borde de {group}")
            for r, t in canvas_sides:
                if parallel_gap(p, q, r, t) < EPS:
                    errors.append(f"{key}: recorre borde del lienzo")
        value = cell.get("value", "")
        if value.strip():
            size = number(s.get("fontSize"))
            minimum = min(minimum, size)
            if size < 24:
                errors.append(f"{key}: fontSize rótulo < 24")
            if s.get("fontStyle") != "1":
                errors.append(f"{key}: rótulo sin negrita")
            relative = number(g.get("x")) if g is not None else 0
            x, y, p, q = at_path(points, relative)
            offset = g.find("mxPoint[@as='offset']") if g is not None else None
            normal = number(g.get("y")) if g is not None else 0
            nx = normal if abs(p[0] - q[0]) < EPS else 0
            ny = normal if abs(p[1] - q[1]) < EPS else 0
            x += nx + (number(offset.get("x")) if offset is not None else 0)
            y += ny + (number(offset.get("y")) if offset is not None else 0)
            _, _, _, label = text_box(value, 10000, size, x, y)
            edge_labels[key] = label
            bounds = unite(bounds, label)
            for other, obstacle in leaves.items():
                if overlap(label, obstacle):
                    errors.append(f"{key}: rótulo sobre hoja {other}")
            for other, obstacle in titles.items():
                if overlap(label, obstacle):
                    errors.append(f"{key}: rótulo sobre título {other}")
            for group in groups:
                for r, t in sides(geo[group]):
                    if hit(r, t, label):
                        errors.append(f"{key}: rótulo sobre borde de {group}")

    for key, points in paths.items():
        for other, other_points in paths.items():
            if key >= other:
                continue
            for p, q in zip(points, points[1:]):
                for r, t in zip(other_points, other_points[1:]):
                    if parallel_gap(p, q, r, t) < 15 - EPS:
                        errors.append(f"{key}/{other}: aristas paralelas < 15 px")
                if other in edge_labels and hit(p, q, edge_labels[other]):
                    errors.append(f"{key}: cruza rótulo {other}")
            for r, t in zip(other_points, other_points[1:]):
                if key in edge_labels and hit(r, t, edge_labels[key]):
                    errors.append(f"{other}: cruza rótulo {key}")
            if key in edge_labels and other in edge_labels and overlap(edge_labels[key], edge_labels[other]):
                errors.append(f"{key}/{other}: rótulos superpuestos")

    assert bounds is not None
    width, height = bounds[2] - bounds[0], bounds[3] - bounds[1]
    if width <= 0 or height <= 0:
        errors.append("extensión nula")
    landscape = minimum * min(625 / width, 380 / height) if width and height else 0
    portrait = minimum * min(447 / width, 590 / height) if width and height else 0
    if max(landscape, portrait) < 9.0 - EPS:
        errors.append(f"letra impresa insuficiente: horizontal {landscape:.2f} pt; vertical {portrait:.2f} pt")
    return width, height, minimum if minimum != math.inf else 0, list(dict.fromkeys(errors))


def main() -> int:
    files = [Path(p) for p in sys.argv[1:]] if len(sys.argv) > 1 else sorted(HERE.glob("*_v3.drawio"))
    files = [p for p in files if p.name.endswith("_v3.drawio")]
    if not files:
        print("Sin diagramas", file=sys.stderr)
        return 1
    failed = False
    for path in files:
        try:
            width, height, minimum, errors = inspect(path)
        except (OSError, ValueError) as exc:
            print(f"{path}: {exc}", file=sys.stderr)
            failed = True
            continue
        land = minimum * min(625 / width, 380 / height) if width and height else 0
        port = minimum * min(447 / width, 590 / height) if width and height else 0
        chosen = "horizontal" if land >= port else "vertical"
        print(f"{path.name}: {width:.1f} × {height:.1f} px; fuente mínima {minimum:g} px; "
              f"horizontal {land:.2f} pt; vertical {port:.2f} pt; elegir {chosen}; {len(errors)} falla(s)")
        for error in errors:
            print(f"  ERROR: {error}")
        failed |= bool(errors)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
