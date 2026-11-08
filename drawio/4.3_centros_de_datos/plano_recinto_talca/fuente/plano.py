"""Genera el plano acotado del recinto técnico del CD Talca en draw.io."""
import sys
from xml.sax.saxutils import escape
from geom import ROOMS, DOORS, EQUIP, FM200, EXTERIOR, DUCTS, T_EXT, T_INT, FACADE_Y

U = 60.0            # unidades draw.io por metro: 1:60 si el ancho impreso es 9,40 m / 60
XMIN, XMAX = -0.95, 8.45
YMAX, YMIN = 8.45, -2.85
FS = 12             # 12 u = 9,45 pt en la página

COL = {
    'muro': '#3C3C3C', 'fachada': '#9A9A9A',
    'piso_S': '#EEF3F8', 'piso': '#FBFAF6', 'grid': '#C5D0DC',
    'rack': ('#DAE8FC', '#6C8EBF'), 'clima': ('#E1D5E7', '#9673A6'),
    'energia': ('#FFF2CC', '#D6B656'), 'incendio': ('#F8CECC', '#B85450'),
    'mueble': ('#F5F5F5', '#8C8C8C'), 'ext': '#F1F4EC',
}

cells = []
nid = [10]


def X(x): return round((x - XMIN) * U, 1)
def Y(y): return round((YMAX - y) * U, 1)


def add(style, x, y, w, h, value='', rot=0):
    nid[0] += 1
    st = style + (f'rotation={rot};' if rot else '')
    v = escape(value, {'"': '&quot;'})
    cells.append(f'<mxCell id="c{nid[0]}" value="{v}" style="{st}" vertex="1" parent="1">'
                 f'<mxGeometry x="{round(x,1)}" y="{round(y,1)}" width="{round(w,1)}" height="{round(h,1)}" as="geometry"/></mxCell>')


def rect_w(x0, y0, x1, y1, style, value=''):
    add(style, X(x0), Y(y1), (x1 - x0) * U, (y1 - y0) * U, value)


def text(x, y, w, h, value, size=FS, align='center', rot=0, color='#1A1A1A'):
    """Texto centrado en (x, y) metros, caja de w × h metros."""
    st = (f'text;html=1;whiteSpace=wrap;align={align};verticalAlign=middle;fontSize={size};fontColor={color};'
          'spacing=0;overflow=visible;')
    W, H = w * U, h * U
    add(st, X(x) - W / 2, Y(y) - H / 2, W, H, value, rot)


DIM = ('shape=dimension;whiteSpace=wrap;html=1;align=center;points=[];verticalAlign=bottom;spacingBottom=1;'
       f'labelBackgroundColor=none;fontSize={FS};strokeWidth=0.8;fontColor=#1A1A1A;')


def dim_h(xa, xb, yline, ext, label):
    """Cota horizontal con la línea en yline y extensiones hacia el norte."""
    h = ext * U
    add(DIM, X(xa), Y(yline) - h, (xb - xa) * U, h, label)


def dim_v(ya, yb, xline, ext, label, toward='W'):
    """Cota vertical en xline; extensiones y rótulo hacia el oeste o el este."""
    L, h = (yb - ya) * U, ext * U
    cy = (Y(ya) + Y(yb)) / 2
    cx, rot = (X(xline) - h / 2, -90) if toward == 'W' else (X(xline) + h / 2, 90)
    add(DIM, cx - L / 2, cy - h / 2, L, h, label, rot)


SHAPE = {('S', 'W'): ('doorLeft', 0), ('S', 'E'): ('doorRight', 0),
         ('N', 'E'): ('doorLeft', 180), ('N', 'W'): ('doorRight', 180),
         ('W', 'N'): ('doorLeft', 90), ('W', 'S'): ('doorRight', 90),
         ('E', 'S'): ('doorLeft', 270), ('E', 'N'): ('doorRight', 270)}


def door(did, wall, c, a, b, swing, hinge):
    t = T_EXT if did == 'entrada' else T_INT
    d = b - a
    w, h = d * U, d * U * 85 / 80
    shp, rot = SHAPE[(swing, hinge)]
    st = f'shape=mxgraph.floorplan.{shp};aspect=fixed;strokeWidth=0.8;fillColor=#FFFFFF;'
    if wall == 'h':
        lo, hi = (c - t, c) if swing == 'N' else (c, c + t)
        rect_w(a, lo, b, hi, 'fillColor=#FFFFFF;strokeColor=none;')
        y_top = Y(c) - h if swing == 'N' else Y(c)
        add(st, X(a), y_top, w, h, '', rot)
    else:
        lo, hi = (c, c + t) if swing == 'W' else (c - t, c)
        rect_w(lo, a, hi, b, 'fillColor=#FFFFFF;strokeColor=none;')
        cy = (Y(a) + Y(b)) / 2
        cx = X(c) - h / 2 if swing == 'W' else X(c) + h / 2
        add(st, cx - w / 2, cy - h / 2, w, h, '', rot)


# Marco invisible: fija el recorte del PDF a XMIN..XMAX × YMIN..YMAX
rect_w(XMIN, YMIN, XMAX, YMAX, 'fillColor=none;strokeColor=none;')
# --- Exterior y bodega -------------------------------------------------------
rect_w(-0.20, FACADE_Y, 7.70, 8.30, f'rounded=0;fillColor={COL["ext"]};strokeColor=#B7C4A8;dashed=1;strokeWidth=0.8;')
rect_w(-0.20, 5.65, 3.70, FACADE_Y, f'fillColor={COL["fachada"]};strokeColor=none;')

# --- Muros del recinto y pisos ------------------------------------------------
for k, (x0, y0, x1, y1, _) in ROOMS.items():
    rect_w(x0 - T_EXT, y0 - T_EXT, x1 + T_EXT, y1 + T_EXT, f'fillColor={COL["muro"]};strokeColor=none;')
for k, (x0, y0, x1, y1, _) in ROOMS.items():
    rect_w(x0, y0, x1, y1, f'fillColor={COL["piso_S"] if k == "S" else COL["piso"]};strokeColor=none;')

# Piso técnico de la sala de servidores: baldosas de 0,6 m
x0, y0, x1, y1, _ = ROOMS['S']
for i in range(1, 6):
    rect_w(x0 + 0.6 * i, y0, x0 + 0.6 * i + 0.001, y1, f'fillColor=none;strokeColor={COL["grid"]};strokeWidth=0.6;')
j = 1
while y0 + 0.6 * j < y1:
    rect_w(x0, y0 + 0.6 * j, x1, y0 + 0.6 * j + 0.001, f'fillColor=none;strokeColor={COL["grid"]};strokeWidth=0.6;')
    j += 1

for dd in DOORS:
    door(*dd)

# --- Equipos -----------------------------------------------------------------
for eid, x0, y0, x1, y1, lab, fam, _h in EQUIP:
    fill, stroke = COL[fam]
    vertical = (x1 - x0) < 0.55 and (y1 - y0) > 0.9
    show = lab if ((x1 - x0) >= 0.3 and (y1 - y0) >= 0.3) or vertical else ''
    st = (f'rounded=0;whiteSpace=wrap;html=1;fillColor={fill};strokeColor={stroke};strokeWidth=1;fontSize={FS};'
          f'spacing=0;{"horizontal=0;" if vertical else ""}')
    rect_w(x0, y0, x1, y1, st, show)
cx, cy, r = FM200
add(f'ellipse;fillColor={COL["incendio"][0]};strokeColor={COL["incendio"][1]};strokeWidth=1;',
    X(cx - r), Y(cy + r), 2 * r * U, 2 * r * U)
text(cx - 0.62, cy, 0.9, 0.3, 'FM-200')
text(4.45, 5.10, 0.7, 0.3, 'ASD', align='left')
text(6.90, 0.75, 0.8, 0.3, 'Tablero')
text(7.10, 1.62, 0.7, 0.3, 'Clima')
add('shape=mxgraph.floorplan.office_chair;strokeWidth=0.8;', X(0.38), Y(1.80), 0.45 * U, 0.48 * U, '', 180)

# --- Rótulos de recintos -----------------------------------------------------
text(5.60, 3.00, 3.2, 0.5, '<b>5 Sala de servidores y<br>comunicaciones</b>')
text(5.70, 0.30, 3.4, 0.3, '<b>4 Sala de UPS y baterías</b>')
text(1.50, 0.98, 1.9, 0.5, '<b>1 Zona de trabajo<br>y respaldo</b>')
text(3.20, 2.05, 2.0, 0.3, '<b>2 Pasillo de control</b>', rot=-90)
text(3.15, 4.20, 1.1, 0.3, '<b>3 Esclusa</b>')

# --- Exterior ----------------------------------------------------------------
for eid, x0, y0, x1, y1, lab, fam, _h in EXTERIOR:
    fill, stroke = COL[fam]
    rect_w(x0, y0, x1, y1, f'rounded=0;whiteSpace=wrap;html=1;fillColor={fill};strokeColor={stroke};fontSize={FS};spacing=1;', lab)
for lab, x, ytop in DUCTS:
    rect_w(x - 0.012, 5.65, x + 0.012, ytop, 'fillColor=#6C8EBF;strokeColor=#6C8EBF;dashed=1;strokeWidth=1.2;')
text(5.12, 7.62, 0.7, 0.3, 'Fibra')
text(7.25, 7.18, 0.6, 0.3, 'LTE')
text(6.40, 7.75, 1.8, 0.3, 'Starlink en techo', color='#444444')
text(6.55, 8.12, 2.2, 0.3, '<b>Exterior del edificio</b>')

# --- Bodega: simbología y rótulos ------------------------------------------------
sim = [('TA', 'Transferencia automática'), ('CO', 'Condensadora'), ('ASD', 'Detección temprana'), ('EN', 'Mesón de enrolamiento')]
rows = ''.join(f'<tr><td style="padding-right:5px"><b>{a}</b></td><td>{b}</td></tr>' for a, b in sim)
text(0.70, 3.55, 3.25, 1.30, f'<b>Simbología</b><table style="font-size:{FS}px;border-collapse:collapse" cellpadding="0">{rows}</table>', align='left')
text(0.70, 4.95, 3.25, 0.3, 'Bodega del CD (fuera del recinto)', color='#555555', align='left')
text(1.70, 5.42, 3.6, 0.3, 'Muro exterior del edificio', color='#555555')

# --- Cotas -------------------------------------------------------------------
dim_h(0.00, 2.40, -0.62, 0.40, '2,40')
dim_h(2.55, 3.75, -0.62, 0.40, '1,20')
dim_h(3.90, 7.50, -0.62, 0.40, '3,60')
dim_h(-0.20, 7.70, -1.02, 0.80, '7,90 exterior')
dim_v(0.00, 2.00, 8.12, 0.40, '2,00', toward='W')
dim_v(2.15, 5.65, 8.12, 0.40, '3,50', toward='W')
dim_v(0.00, 2.50, -0.62, 0.40, '2,50', toward='E')
dim_v(0.00, 3.00, 3.62, 0.08, '3,00', toward='W')
dim_v(3.15, 4.35, 2.22, 0.08, '1,20', toward='W')   # fuera de la esclusa: no cruza el rótulo
dim_h(3.90, 4.90, 2.27, 0.08, '1,00')
dim_h(4.90, 6.70, 2.27, 0.08, '1,80')
dim_h(6.70, 7.50, 2.27, 0.08, '0,80')
dim_v(2.15, 3.35, 7.38, 0.08, '1,20', toward='W')
dim_v(3.35, 4.55, 7.38, 0.08, '1,20', toward='W')
dim_v(4.55, 5.65, 7.38, 0.08, '1,10', toward='W')

# --- Banda inferior: escala y leyenda (las superficies van en la Tabla del texto) ---
for i in range(3):
    rect_w(-0.20 + i, -1.55, 0.80 + i, -1.45, f'fillColor={"#1A1A1A" if i % 2 == 0 else "#FFFFFF"};strokeColor=#1A1A1A;strokeWidth=0.8;')
for i, t in enumerate(['0', '1', '2', '3 m']):
    text(-0.20 + i + (0.12 if t == '3 m' else 0), -1.75, 0.5, 0.3, t)
text(1.10, -2.10, 2.9, 0.3, 'Escala 1:60 en tamaño carta')
text(1.10, -2.45, 2.9, 0.3, 'Cotas en metros', color='#555555')
leg = [('Muro con blindaje', COL['muro'], COL['muro']), ('Cómputo y red', *COL['rack']),
       ('Energía', *COL['energia']), ('Climatización', *COL['clima']), ('Incendio', *COL['incendio'])]
for i, (lab, f, s) in enumerate(leg):
    yy = -1.42 - 0.30 * i
    rect_w(3.35, yy - 0.10, 3.63, yy + 0.10, f'fillColor={f};strokeColor={s};')
    text(3.73 + 0.95, yy, 1.9, 0.28, lab, align='left')
add('shape=singleArrow;direction=north;arrowWidth=0.45;arrowSize=0.45;fillColor=#1A1A1A;strokeColor=none;', X(7.92), Y(8.30), 14, 26)
text(8.04, 7.70, 0.4, 0.3, '<b>N</b>')

xml = ('<mxfile><diagram name="Recinto CD Talca"><mxGraphModel dx="800" dy="800" grid="0" gridSize="10" page="0">'
       '<root><mxCell id="0"/><mxCell id="1" parent="0"/>' + ''.join(cells) + '</root></mxGraphModel></diagram></mxfile>')
open(sys.argv[1], 'w', encoding='utf-8').write(xml)
print('celdas', len(cells), 'lienzo', round((XMAX - XMIN) * U), 'x', round((YMAX - YMIN) * U))
