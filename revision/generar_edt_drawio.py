"""Reconstruye las láminas de la EDT como fuentes draw.io editables.

Lee la geometría y el estilo de los PDF exportados en el commit BASE, reemplaza
los rótulos de los paquetes por los nombres del diccionario del T-14, agrega los
paquetes que falten y reacomoda cada columna apilada (desplazando lo que cuelga
debajo en la misma columna). Escribe un .drawio junto a cada PDF que cambia; la
exportación a PDF se hace con draw.io (--export --crop).
"""
from pathlib import Path
from html import escape
from statistics import median
from xml.sax.saxutils import quoteattr
import re, subprocess, sys
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
DIR = 'imagenes/Imagenes de la edt'
BASE = '72a64f2a'          # PDF originales exportados desde draw.io web
TOL = 2.5
# Métricas reales de la fuente con que draw.io exporta (Arial); Helvetica base-14 no mide −, ° ni –.
FONTS = {True: pymupdf.Font(fontfile='C:/Windows/Fonts/arialbd.ttf'), False: pymupdf.Font(fontfile='C:/Windows/Fonts/arial.ttf')}
WRAP_MARGIN = 0.97
# Descenso de la primera línea que agrega draw.io a una etiqueta html alineada arriba, en
# unidades del PDF original. Medido por lámina al exportar con draw.io desktop (cajas sin cambios).
FIRST_LINE_DROP = {'EDT-EDT completa': 0.152, 'EDT-Fase 1 (1 de 2)': 3.91, 'EDT-Fase 1 (2 de 2)': 3.64,
                   'EDT-Fase 2 (2 de 2)': 4.43, 'EDT-Fase 3 (2 de 5)': 3.96, 'EDT-Fase 3 (3 de 5)': 5.19,
                   'EDT-Fase 3 (5 de 5)': 4.74, 'EDT-Fase 4': 4.22, 'EDT-Fase 5': 5.02, 'EDT-Fase 6 (1 de 2)': 4.33,
                   'EDT-Fase 6 (2 de 2)': 4.22, 'EDT-Fase 7': 4.91, 'EDT-Fase 8 (1 de 2)': 4.03}

def clean_tex(s):
    s = s.replace(r'\allowbreak{}', '').replace(r'\ensuremath{\times}', '×').replace(r'\%', '%')
    s = s.replace('~', ' ').replace('---', '—').replace('--', '–')
    s = re.sub(r'\\text(?:it|bf)\{([^}]*)\}', r'\1', s)
    assert '\\' not in s and '$' not in s, s
    return re.sub(r'\s+', ' ', s).strip()

def t14_names():
    names = {}
    for f in (ROOT / 'formulario-t14/tablas').glob('tab_T14_*.tex'):
        for line in f.read_text(encoding='utf-8').splitlines():
            m = re.match(r'^\s*(\d+(?:\.\d+){2,3})\s*&\s*(.+?)\s*&', line)
            if m: names[m.group(1)] = clean_tex(m.group(2))
    return names

def leaves():
    text = (ROOT / 'formulario-t15/tablas/tab_T15_2.tex').read_text(encoding='utf-8')
    codes = re.findall(r'^\s*(\d+(?:\.\d+)+)\s*&', text, re.M)
    assert len(codes) == 227
    return codes

def key(code): return [int(v) for v in code.split('.')]
def hexcolor(c): return 'none' if c is None else '#%02X%02X%02X' % tuple(round(v * 255) for v in c)
def width_of(spans, size): return sum(FONTS[b].text_length(t, fontsize=size) for t, b in spans)

def wrap(code, name, width, size, mixed):
    """Corta «código nombre» en líneas; con estilo mixto el código va en negrita y el resto en regular."""
    words = [(code, True)] + [(w, not mixed) for w in name.split(' ')]
    lines, cur = [], []
    def joined(parts):
        out = []
        for t, b in parts:
            if out and out[-1][1] == b: out[-1] = (out[-1][0] + t, b)
            else: out.append((t, b))
        return out
    def with_space(parts, word):
        return parts + ([(' ', word[1])] if parts else []) + [word]
    for word in words:
        trial = with_space(cur, word)
        if width_of(trial, size) <= width or not cur:
            cur = trial; continue
        # Corte tras guion, como en las láminas originales («cross-» / «docking»).
        if '-' in word[0]:
            head, tail = word[0].split('-', 1)
            if width_of(with_space(cur, (head + '-', word[1])), size) <= width:
                lines.append(joined(with_space(cur, (head + '-', word[1])))); cur = [(tail, word[1])]; continue
        lines.append(joined(cur)); cur = [word]
    lines.append(joined(cur))
    return lines

class Box:
    def __init__(self, d):
        self.rect = pymupdf.Rect(d['rect']); self.fill = d.get('fill'); self.stroke = d.get('color')
        self.width = d.get('width') or 0; self.dashed = False; self.lines = []; self.new = False
        first = next((i for i in d['items'] if i[0] == 'l'), None)
        curved = any(i[0] == 'c' for i in d['items'])
        self.radius = max(first[1].x - self.rect.x0, 0.01) if curved and first else 0
    @property
    def text(self):
        out = ''
        for l in self.lines:
            t = ''.join(s for s, _ in l['spans']).strip()
            out += t if not out or out.endswith('-') else ' ' + t
        return out
    @property
    def code(self):
        m = re.match(r'^(\d+(?:\.\d+)*)\.?\s', self.text + ' ')
        return m.group(1) if m else None
    def move(self, dy):
        self.rect = pymupdf.Rect(self.rect.x0, self.rect.y0 + dy, self.rect.x1, self.rect.y1 + dy)
        for l in self.lines: l['bbox'] = pymupdf.Rect(l['bbox'].x0, l['bbox'].y0 + dy, l['bbox'].x1, l['bbox'].y1 + dy)

def load(pdf_bytes):
    page = pymupdf.open(stream=pdf_bytes, filetype='pdf')[0]
    boxes, segs = [], []
    for d in page.get_drawings():
        r = d['rect']
        if d.get('fill') and r.width > page.rect.width - 5 and r.height > page.rect.height - 5: continue
        if d.get('fill'):
            boxes.append((Box(d), d))
        else:
            for it in d['items']:
                if it[0] == 'l':
                    segs.append({'a': pymupdf.Point(it[1]), 'b': pymupdf.Point(it[2]),
                                 'color': d.get('color'), 'width': d.get('width'), 'dashed': bool(d.get('dashes') and d['dashes'] != '[] 0')})
    # Un borde punteado llega como trazo relleno con cientos de tramos: se fusiona con su caja.
    real = []
    for b, d in boxes:
        host = next((o for o, _ in boxes if o is not b and len(d['items']) > 40
                     and abs(o.rect.x0 - b.rect.x0) < 1 and abs(o.rect.y1 - b.rect.y1) < 1), None)
        if host:
            # El grosor del borde es lo que el trazo punteado sobresale de la caja.
            host.dashed = True; host.stroke = b.fill; host.width = max(b.rect.width - host.rect.width, 0.01)
            continue
        real.append(b)
    for blk in page.get_text('dict')['blocks']:
        for l in blk.get('lines', []):
            spans = []
            for s in l['spans']:
                bold = 'Bold' in s['font']
                if spans and spans[-1][1] == bold: spans[-1] = (spans[-1][0] + s['text'], bold)
                else: spans.append((s['text'], bold))
            s0 = l['spans'][0]
            c = pymupdf.Point((l['bbox'][0] + l['bbox'][2]) / 2, (l['bbox'][1] + l['bbox'][3]) / 2)
            inside = [b for b in real if b.rect.contains(c)]
            assert inside, ('texto fuera de caja', spans)
            min(inside, key=lambda b: b.rect.get_area()).lines.append(
                {'spans': spans, 'bbox': pymupdf.Rect(l['bbox']), 'size': s0['size'], 'color': s0['color']})
    for b in real: b.lines.sort(key=lambda l: (l['bbox'].y0, l['bbox'].x0))
    return real, segs

def relabel(b, ref, code, name, x0, width):
    """Rehace las líneas de una caja con el estilo y los márgenes de la caja de referencia."""
    first, last = ref.lines[0], ref.lines[-1]
    size = first['size']; pad_l = first['bbox'].x0 - ref.rect.x0
    pad_t = first['bbox'].y0 - ref.rect.y0; pad_b = ref.rect.y1 - last['bbox'].y1
    lh = (last['bbox'].y0 - first['bbox'].y0) / (len(ref.lines) - 1) if len(ref.lines) > 1 else size * 1.2
    mixed = any(len(l['spans']) > 1 for l in ref.lines)
    text = wrap(code, name, (width - 2 * pad_l) * WRAP_MARGIN, size, mixed)
    lh_box = first['bbox'].height
    b.rect = pymupdf.Rect(x0, 0, x0 + width, pad_t + (len(text) - 1) * lh + lh_box + pad_b)
    b.lines = [dict(first, spans=sp, bbox=pymupdf.Rect(x0 + pad_l, pad_t + i * lh, x0 + pad_l + 1, pad_t + i * lh + lh_box))
               for i, sp in enumerate(text)]
    b.new = True

def reflow(boxes, segs, names, leaf_codes, log):
    by_code = {b.code: b for b in boxes if b.code}
    changed = False
    parents = sorted({c.rsplit('.', 1)[0] for c in leaf_codes if c.rsplit('.', 1)[0] in by_code}, key=key)
    for pc in parents:
        parent = by_code[pc]
        expected = sorted([c for c in leaf_codes if c.rsplit('.', 1)[0] == pc], key=key)
        present = sorted([by_code[c] for c in expected if c in by_code], key=lambda b: b.rect.y0)
        if not present: continue
        x0 = present[0].rect.x0
        if any(abs(b.rect.x0 - x0) > TOL for b in present): continue   # no es una columna apilada
        assert [b.code for b in present] == [c for c in expected if c in by_code], pc
        gaps = [present[i + 1].rect.y0 - present[i].rect.y1 for i in range(len(present) - 1)]
        gap = median(gaps) if gaps else (present[0].rect.y0 - parent.rect.y1)
        model, old_bottom = present[-1], present[-1].rect.y1
        band = (min(parent.rect.x0, x0) - 0.15 * parent.rect.width, max(b.rect.x1 for b in present))
        ticks = {b.code: next((s for s in segs if abs(s['a'].y - s['b'].y) < 0.5 and abs(max(s['a'].x, s['b'].x) - b.rect.x0) < TOL
                               and b.rect.y0 - 0.5 <= s['a'].y <= b.rect.y1 + 0.5), None) for b in present}
        first_tick = ticks[present[0].code]
        spine = None
        if first_tick:
            tx = min(first_tick['a'].x, first_tick['b'].x)
            spine = next((s for s in segs if abs(s['a'].x - s['b'].x) < 0.5 and abs(s['a'].x - tx) < TOL
                          and min(s['a'].y, s['b'].y) < present[0].rect.y0 + 1), None)
        frac = lambda b: (ticks[b.code]['a'].y - b.rect.y0) / b.rect.height if ticks.get(b.code) else 0.5
        y, column, own = present[0].rect.y0, [], []
        for code in expected:
            name = names[code]
            b = by_code.get(code)
            if b is None:
                b = Box({'rect': model.rect, 'fill': model.fill, 'color': model.stroke, 'width': model.width, 'items': []})
                boxes.append(b); by_code[code] = b
                ticks[code] = dict(ticks[model.code]) if ticks.get(model.code) else None
                if ticks[code]: segs.append(ticks[code])
                f = frac(model); relabel(b, model, code, name, x0, model.rect.width)
                log.append(f'  + {code} {name}'); changed = True
            else:
                f = frac(b)
                if b.text != f'{code} {name}':
                    log.append(f'  ~ {code}: «{b.text}» → «{name}»')
                    relabel(b, b, code, name, b.rect.x0, b.rect.width); changed = True
            b.move(y - b.rect.y0)
            t = ticks.get(code)
            if t:
                ty = y + f * b.rect.height
                t['a'] = pymupdf.Point(t['a'].x, ty); t['b'] = pymupdf.Point(t['b'].x, ty); own.append(t)
            column.append(b)
            y = b.rect.y1 + gap
        if spine and ticks.get(expected[-1]):
            top = min(spine['a'].y, spine['b'].y)
            spine['a'] = pymupdf.Point(spine['a'].x, top); spine['b'] = pymupdf.Point(spine['b'].x, ticks[expected[-1]]['a'].y)
            own.append(spine)
        # Lo que cuelga debajo de la columna (grupos anidados) baja lo mismo que creció la columna.
        delta = column[-1].rect.y1 - old_bottom
        if abs(delta) > 1e-6:
            for o in boxes:
                if o not in column and o.rect.y0 >= old_bottom - 0.5 and o.rect.x1 > band[0] and o.rect.x0 < band[1]:
                    o.move(delta)
            for s in segs:
                if any(s is x for x in own): continue
                for end in ('a', 'b'):
                    p = s[end]
                    if p.y >= old_bottom - 0.5 and band[0] <= p.x <= band[1]:
                        s[end] = pymupdf.Point(p.x, p.y + delta)
    for i, a in enumerate(boxes):
        for b in boxes[i + 1:]:
            inter = a.rect & b.rect
            if inter.is_valid and not inter.is_empty and not (a.rect.contains(b.rect) or b.rect.contains(a.rect)):
                raise SystemExit(f'Superposición: {a.code} {a.rect} / {b.code} {b.rect}')
    return changed

def update_counts(boxes, leaf_codes, log):
    """Actualiza los subtítulos «N CC · M PT» de las fases y el total de la raíz."""
    changed = False
    for b in boxes:
        for l in b.lines:
            text = ''.join(t for t, _ in l['spans'])
            m = re.fullmatch(r'(\d+) CC · (\d+) PT', text)
            if m and b.code:
                ph = [c for c in leaf_codes if c.split('.')[0] == b.code]
                new = f'{len({".".join(c.split(".")[:2]) for c in ph})} CC · {len(ph)} PT'
            elif re.fullmatch(r'\d+ cuentas de control · \d+ paquetes de trabajo', text):
                new = f'{len({".".join(c.split(".")[:2]) for c in leaf_codes})} cuentas de control · {len(leaf_codes)} paquetes de trabajo'
            else:
                continue
            if new != text:
                log.append(f'  ~ {b.text.split(" ")[0]} subtítulo: «{text}» → «{new}»')
                l['spans'] = [(new, l['spans'][0][1])]; changed = True
    return changed

def cell_xml(i, b, k, drop):
    r = b.rect; first = b.lines[0] if b.lines else None
    centered = (first is not None and not b.new
                and all(abs((l['bbox'].x0 + l['bbox'].x1) / 2 - (r.x0 + r.x1) / 2) < min(3, 0.02 * r.width) for l in b.lines))
    style = {'rounded': 1 if b.radius else 0, 'whiteSpace': 'nowrap', 'html': 1, 'fillColor': hexcolor(b.fill),
             'strokeColor': hexcolor(b.stroke), 'strokeWidth': round(b.width * k, 3), 'spacing': 0, 'fontFamily': 'Arial'}
    if b.radius: style.update(absoluteArcSize=1, arcSize=round(2 * b.radius * k, 2))
    if b.dashed: style.update(dashed=1)
    value = ''
    if first:
        style.update(fontSize=round(first['size'] * k, 3), fontColor='#%06X' % first['color'], fontStyle=0)
        if centered:
            style.update(align='center', verticalAlign='middle')
        else:
            style.update(align='left', verticalAlign='top', spacingLeft=round((first['bbox'].x0 - r.x0) * k, 2),
                         spacingTop=round((first['bbox'].y0 - r.y0 - drop) * k, 2))
        value = '<br>'.join(''.join(f'<b>{escape(t)}</b>' if bold else escape(t) for t, bold in l['spans']) for l in b.lines)
    st = ';'.join(f'{a}={v}' for a, v in style.items()) + ';'
    return (f'<mxCell id="b{i}" value={quoteattr(value)} style={quoteattr(st)} vertex="1" parent="1">'
            f'<mxGeometry x="{r.x0 * k:.2f}" y="{r.y0 * k:.2f}" width="{r.width * k:.2f}" height="{r.height * k:.2f}" as="geometry"/></mxCell>')

def edge_xml(i, s, k):
    st = (f'endArrow=none;html=1;rounded=0;strokeColor={hexcolor(s["color"])};strokeWidth={round((s["width"] or 1) * k, 3)};'
          + ('dashed=1;' if s['dashed'] else ''))
    return (f'<mxCell id="e{i}" style={quoteattr(st)} edge="1" parent="1"><mxGeometry relative="1" as="geometry">'
            f'<mxPoint x="{s["a"].x * k:.2f}" y="{s["a"].y * k:.2f}" as="sourcePoint"/>'
            f'<mxPoint x="{s["b"].x * k:.2f}" y="{s["b"].y * k:.2f}" as="targetPoint"/></mxGeometry></mxCell>')

def write_drawio(path, boxes, segs, k):
    drop = FIRST_LINE_DROP[path.stem]
    cells = [edge_xml(i, s, k) for i, s in enumerate(segs)] + [cell_xml(i, b, k, drop) for i, b in enumerate(boxes)]
    xml = ('<mxfile host="Electron"><diagram name="EDT" id="edt"><mxGraphModel grid="0" page="0" pageScale="1">'
           '<root><mxCell id="0"/><mxCell id="1" parent="0"/>' + ''.join(cells) + '</root></mxGraphModel></diagram></mxfile>')
    path.write_text(xml, encoding='utf-8')

def main():
    names, leaf_codes = t14_names(), leaves()
    assert set(leaf_codes) <= set(names), sorted(set(leaf_codes) - set(names))
    written = []
    for pdf in sorted((ROOT / DIR).glob('EDT-*.drawio.pdf')):
        rel = f'{DIR}/{pdf.name}'
        data = subprocess.run(['git', 'show', f'{BASE}:{rel}'], cwd=ROOT, capture_output=True, check=True).stdout
        boxes, segs = load(data)
        log = []
        changed = reflow(boxes, segs, names, leaf_codes, log)
        if not (update_counts(boxes, leaf_codes, log) or changed): continue
        k = 10 if 'completa' in pdf.name else 1     # evita fuentes por debajo de 1 px en la vista panorámica
        out = pdf.with_name(pdf.name.removesuffix('.pdf'))
        write_drawio(out, boxes, segs, k)
        written.append(out.name)
        print(pdf.name); print('\n'.join(log))
    print('Escritos:', written)

if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
