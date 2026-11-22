"""Dibuja la vista de frentes del SD7 a partir del Gantt y del T-15."""
import re

from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.colors import HexColor

from gantt_local_vector import ROOT, SRC, W, H, add_month, heading, label, read

OUT = SRC / 'Revision-local'
BLUE = HexColor('#32628c')
SHADE = HexColor('#fbeacb')
GRID = HexColor('#d5dfe6')
INK = HexColor('#253746')
SIZE = 10


def scale(origin, left, months):
    step = (W - 12 - left) / months

    def position(day):
        month = (day.year - origin.year) * 12 + day.month - origin.month
        boundary = add_month(origin, month)
        fraction = (day - boundary).days / (add_month(boundary, 1) - boundary).days
        return left + step * (month + fraction)

    return position


def draw_grid(c, x, origin, months, bottom, top, ticks):
    def boundary(offset):
        return x(add_month(origin, offset))

    for first, last in ((13, 15), (19, 20)):
        c.setFillColor(SHADE)
        c.rect(boundary(first - 1), bottom, boundary(last) - boundary(first - 1),
               top - bottom, fill=1, stroke=0)
    for offset in range(months + 1):
        c.setStrokeColor(GRID)
        c.setLineWidth(0.65 if offset in ticks else 0.25)
        c.line(boundary(offset), bottom, boundary(offset), top)
    c.setFont('ArialLocal', SIZE)
    c.setFillColor(INK)
    for month in ticks:
        c.drawCentredString((boundary(month - 1) + boundary(month)) / 2,
                            bottom - 15, str(month))
    label(c, 9, bottom - 15, 'Mes contractual', size=SIZE)


def bar(c, x0, x1, center, color):
    c.setFillColor(color)
    c.rect(x0, center - 5, x1 - x0, 10, fill=1, stroke=0)


def legend(c, entries, y):
    x = 10
    for text, color in entries:
        bar(c, x, x + 13, y + 3, color)
        label(c, x + 18, y, text, size=SIZE)
        x += 37 + stringWidth(text, 'ArialLocal', SIZE)
    assert x - 19 <= W


def fronts(origin):
    table = ROOT / 'formulario-t15/tablas/tab_T15_1.tex'
    rows = []
    for line in table.read_text(encoding='utf-8').splitlines():
        if re.match(r'^\s*F\d ', line):
            name, owner, _, interval = line.strip().removesuffix(r'\\').split(' & ')
            first, last = map(int, re.match(r'(\d+) a (\d+)', interval).groups())
            rows.append((name, owner, first, last))
    assert [name.split()[0] for name, *_ in rows] == [f'F{i}' for i in range(1, 9)]
    x = scale(origin, 308, 21)
    limit = x(add_month(origin, 21))
    c = canvas.Canvas(str(OUT / 'Frentes-trabajo-resumen.pdf'), pagesize=(W, H), invariant=1)
    c.setTitle('Frentes de trabajo del Subdocumento 7')
    heading(c, 'Frentes de trabajo · meses 1 a 21',
            'Ventana de actividad por frente y rol responsable')
    draw_grid(c, x, origin, 21, 68, 284, list(range(1, 22)))
    for i, (name, owner, first, last) in enumerate(rows):
        y = 272 - 26 * i
        assert max(stringWidth(name, 'ArialLocalBold', SIZE), stringWidth(owner, 'ArialLocal', SIZE)) < 293
        label(c, 9, y + 1, name, bold=True, size=SIZE)
        label(c, 9, y - 10, owner, size=SIZE)
        start = x(add_month(origin, first - 1))
        end = x(add_month(origin, min(last, 21)))
        bar(c, start, end - (6 if last > 21 else 0), y, BLUE)
        if last > 21:
            path = c.beginPath()
            path.moveTo(limit - 6, y + 5)
            path.lineTo(limit, y)
            path.lineTo(limit - 6, y - 5)
            path.close()
            c.drawPath(path, fill=1, stroke=0)
    legend(c, [('Frente activo', BLUE), ('Solapamientos 13–15 y 19–20', SHADE)], 31)
    continuing = [f'{name.split()[0]} hasta el mes {last}' for name, _, _, last in rows if last > 21]
    label(c, 9, 13, 'Flecha a la derecha: ' + ' y '.join(continuing) + '.', size=SIZE)
    c.save()


def generate_fronts_summary():
    tasks, _ = read(SRC / 'Fig_7_Gantt_56_Meses.gan')
    origin = next(t['start'] for t in tasks if t['name'].startswith('Etapa 1 · Desarrollo'))
    fronts(origin)



if __name__ == '__main__':
    generate_fronts_summary()
