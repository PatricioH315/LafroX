"""Dibuja las dos láminas de síntesis del SD7 a partir del Gantt y del T-15."""
from datetime import timedelta
import re

from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.colors import HexColor

from gantt_local_vector import ROOT, SRC, W, H, add_month, heading, label, read

OUT = SRC / 'Revision-local'
BLUE = HexColor('#32628c')
TEAL = HexColor('#18776d')
GOLD = HexColor('#b36a27')
PURPLE = HexColor('#605184')
SHADE = HexColor('#fbeacb')
GRID = HexColor('#d5dfe6')
INK = HexColor('#253746')
WHITE = HexColor('#ffffff')
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


def diamond(c, x, y):
    path = c.beginPath()
    path.moveTo(x, y + 4)
    path.lineTo(x + 4, y)
    path.lineTo(x, y - 4)
    path.lineTo(x - 4, y)
    path.close()
    c.setFillColor(INK)
    c.drawPath(path, fill=1, stroke=0)


def legend(c, entries, y):
    x = 10
    for text, color in entries:
        bar(c, x, x + 13, y + 3, color)
        label(c, x + 18, y, text, size=SIZE)
        x += 37 + stringWidth(text, 'ArialLocal', SIZE)
    assert x - 19 <= W


def overview(tasks, origin):
    rows = {t['name'].split(' · ')[0]: t for t in tasks if not t['milestone']}
    month_table = ROOT / 'subdocumento-07/tablas/tab_SD7_4.tex'
    months = {h: int(m) for h, m in re.findall(r'^\s*(H\d+) & (\d+) &', month_table.read_text(encoding='utf-8'), re.M)}
    milestones = {}
    for h, month in months.items():
        event = ('Paso a producción' if h in {'H7', 'H12'} else
                 'Inicio contractual de marcha blanca' if h in {'H6', 'H11'} else
                 'Firma del acta')
        day = next(t['start'] for t in tasks if t['name'] == f'{h} · {event}')
        assert add_month(origin, month - 1) <= day < add_month(origin, month), (h, day, month)
        milestones[h] = day
    assert set(milestones) == {f'H{i}' for i in range(1, 13)}
    x = scale(origin, 115, 56)
    c = canvas.Canvas(str(OUT / 'Gantt-SD7-general.pdf'), pagesize=(W, H), invariant=1)
    c.setTitle('Carta Gantt general del Subdocumento 7')
    heading(c, 'Carta Gantt general · 56 meses',
            'Escenario nominal · inicio en febrero de 2027')
    draw_grid(c, x, origin, 56, 128, 277, [1, *range(4, 53, 4), 56])
    # La programación vigente define una barra de desarrollo por etapa.
    # Los hitos explican el avance dentro de esa barra sin imputar fechas nuevas.
    lanes = [
        ('Etapa 1', 212, [('Etapa 1', BLUE), ('9.2.1 Marcha blanca de la Etapa 1', GOLD),
                           ('9.3.1 Estabilización y soporte puente E1', PURPLE)]),
        ('Etapa 2', 184, [('Etapa 2', BLUE), ('9.2.2 Marcha blanca de la Etapa 2', GOLD),
                           ('9.3.2 Estabilización de la Etapa 2', PURPLE)]),
        ('Operación', 156, [('Producto 10', TEAL)]),
    ]
    for title, y, intervals in lanes:
        label(c, 9, y - 3, title, bold=True, size=SIZE)
        for name, color in intervals:
            row = rows[name]
            bar(c, x(row['start']), x(row['end'] + timedelta(days=1)), y, color)
    label(c, 9, 259, 'Hitos E-25', bold=True, size=SIZE)
    lane_right = [0, 0, 0]
    for h, day in sorted(milestones.items(), key=lambda pair: pair[1]):
        pos = x(day)
        width = stringWidth(h, 'ArialLocalBold', SIZE)
        lane = next(i for i, right in enumerate(lane_right) if pos - width / 2 > right + 4)
        lane_right[lane] = pos + width / 2
        y = 240 + 15 * lane
        c.setStrokeColor(INK)
        c.setLineWidth(0.45)
        c.line(pos, 227, pos, y - 8)
        diamond(c, pos, y - 8)
        c.setFillColor(WHITE)
        c.rect(pos - width / 2 - 1, y - 1, width + 2, 11, fill=1, stroke=0)
        c.setFillColor(INK)
        c.setFont('ArialLocalBold', SIZE)
        c.drawCentredString(pos, y, h)
    legend(c, [('Desarrollo', BLUE), ('Marcha blanca', GOLD),
               ('Estabilización y soporte', PURPLE), ('Operación', TEAL),
               ('Solapamientos 13–15 y 19–20', SHADE)], 89)
    label(c, 9, 67, 'Requisitos y diseño: H1, H2 y H8. Entrega de construcción a QA: H4 y H9.', size=SIZE)
    label(c, 9, 53, 'Integración y certificación: H5 y H10. Implantación: marchas blancas y cortes.', size=SIZE)
    cuts = ' · '.join(f'{h}: {milestones[h]:%d/%m/%Y}' for h in ('H7', 'H12'))
    label(c, 9, 33, f'Pasos a producción · {cuts}. La operación comienza con H12.', size=SIZE)
    c.save()


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
    c = canvas.Canvas(str(OUT / 'Gantt-SD7-frentes.pdf'), pagesize=(W, H), invariant=1)
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


def generate_summary():
    tasks, _ = read(SRC / 'Fig_7_Gantt_56_Meses.gan')
    origin = next(t['start'] for t in tasks if t['name'].startswith('Etapa 1 · Desarrollo'))
    overview(tasks, origin)
    fronts(origin)



if __name__ == '__main__':
    generate_summary()
