"""LafroX: variantes vectoriales de 4.1; conserva los PDF originales.

Ejecutar desde la raíz del checkout con reportlab, pypdf y pdfplumber.
"""
from pathlib import Path
from io import BytesIO
import re
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from pypdf import PdfReader, PdfWriter
import pdfplumber

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / '04/figuras/logica/capas'
pdfmetrics.registerFont(TTFont('LfxArial', 'C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('LfxArialBold', 'C:/Windows/Fonts/arialbd.ttf'))
INK = HexColor('#243640')
ORANGE = HexColor('#e66c25')


def general():
    c = canvas.Canvas(str(OUT / 'ARQL-01_General_41_corregida.pdf'), pagesize=(720, 440))
    c.setTitle('LafroX — Mapa de arquitectura lógica 4.1')
    c.setAuthor('LafroX')

    def box(x, y, w, h, lines, accent=False):
        c.setStrokeColor(ORANGE if accent else HexColor('#bdc9ce'))
        c.setFillColor(HexColor('#fff5ed') if accent else HexColor('#f2f6f7'))
        c.roundRect(x, y, w, h, 6, fill=1, stroke=1)
        c.setFillColor(INK)
        yy = y + h / 2 + (len(lines) - 1) * 7 - 4
        for j, line in enumerate(lines):
            c.setFont('LfxArialBold' if j == 0 else 'LfxArial', 12)
            c.drawCentredString(x + w / 2, yy, line)
            yy -= 14

    def arrow(x1, y1, x2, y2):
        c.setStrokeColor(INK)
        c.setLineWidth(1.1)
        c.line(x1, y1, x2, y2)
        c.line(x2, y2, x2 - 3, y2 + 5)
        c.line(x2, y2, x2 + 3, y2 + 5)

    box(12, 378, 224, 52, ['1. Bodega y Calidad', 'Kotlin: perfil local autorizado'])
    box(248, 378, 224, 52, ['1. Preventa y reparto', 'Kotlin: captura y cola sin señal'])
    box(484, 378, 224, 52, ['1. Canales web', 'Clientes, contrapartes y gestión'])
    box(12, 303, 224, 56, ['2–3. Acceso local privado', 'API WMS + verificador de turno', 'Autonomía; capturas en el terminal'], True)
    box(248, 303, 460, 56, ['2–3. Acceso central', 'Borde protegido → API → autorización por recurso', 'OIDC; consolas por acceso verificado'], True)
    for x in [124, 360, 596]:
        arrow(x, 378, x, 359)
        arrow(x, 303, x, 283)
    c.setFont('LfxArialBold', 12)
    c.setFillColor(INK)
    c.drawString(14, 269, '4. Negocio: monolito modular Laravel/PHP; contratos y dueños separados')
    modules = [
        ['M1', 'Recepción'], ['M2', 'Inventario'], ['M3', 'Preventa'],
        ['M4', 'Rutas'], ['M5', 'Preparación'], ['M6', 'Reparto'],
        ['M7', 'Cobranza y', 'rendición'], ['M8', 'Devoluciones', 'y envases'],
        ['M9', 'Calidad y', 'trazabilidad'], ['M10', 'Analítica'],
        ['M11', 'Canal moderno'], ['M12', 'Telemetría'],
    ]
    for i, lines in enumerate(modules):
        box(12 + (i % 6) * 118, 211 - (i // 6) * 53, 106, 47, lines)
    box(12, 91, 342, 49, ['5. Integración y eventos', 'Outbox / RabbitMQ → SQS/SNS; ACL → ERP'])
    box(366, 91, 342, 49, ['6. Datos por dueño', 'Room/SQLite; PostgreSQL; objetos y analítica'])
    arrow(183, 158, 183, 140)
    arrow(537, 158, 537, 140)
    box(12, 12, 696, 62, ['7. Seguridad y 8. Observabilidad atraviesan todos los recorridos',
                          'Identidad personal, mínimo privilegio, auditoría y correlación',
                          'Sin WAN: bodega local; pedido móvil pendiente hasta confirmación'], True)
    c.showPage()
    c.save()


def cmap(font):
    raw = font['/ToUnicode'].get_object().get_data().decode()
    result = {}
    for block in re.findall(r'beginbfchar(.*?)endbfchar', raw, re.S):
        for a, b in re.findall(r'<([0-9a-fA-F]+)>\s*<([0-9a-fA-F]+)>', block):
            result[chr(int(a, 16))] = bytes.fromhex(b).decode('utf-16-be')
    for block in re.findall(r'beginbfrange(.*?)endbfrange', raw, re.S):
        for a, b, z in re.findall(r'<([0-9a-fA-F]+)>\s*<([0-9a-fA-F]+)>\s*<([0-9a-fA-F]+)>', block):
            for q in range(int(a, 16), int(b, 16) + 1):
                result[chr(q)] = chr(int(z, 16) + q - int(a, 16))
    return result


def canonical_names(name):
    source = OUT / name
    reader = PdfReader(source)
    writer = PdfWriter()
    page = writer.add_page(reader.pages[0])
    maps = {str(k): cmap(v.get_object()) for k, v in page['/Resources']['/Font'].items()}
    stream = page.get_contents()
    text_ops = []
    font = None
    for index, (args, op) in enumerate(stream.operations):
        if op == b'Tf':
            font = str(args[0])
        if op == b'Tj' and font:
            decoded = ''.join(maps[font].get(char, char) for char in str(args[0]))
            text_ops.append((index, decoded))
    start = next(i for i, (_, text) in enumerate(text_ops) if text == 'M10 · BI')
    count = 5 if text_ops[start + 4][1] == 'Canal Moderno' else 6
    selected = text_ops[start:start + count]
    assert [s for _, s in selected[:4]] == ['M10 · BI', 'Gerencia', 'M1', '1 · EDI'], selected
    assert [s for _, s in selected[4:]] in [['Canal Moderno'], ['Canal', 'Moderno']], selected
    remove = {i for i, _ in selected}
    stream.operations = [item for i, item in enumerate(stream.operations) if i not in remove]
    page.replace_contents(stream)
    with pdfplumber.open(source) as doc:
        words = doc.pages[0].extract_words()
        positions = {}
        for module in ['M10', 'M11']:
            anchor = next(w for w in words if w['text'] == module)
            group = [w for w in words if anchor['x0'] - 15 <= w['x0'] <= anchor['x0'] + 100
                     and anchor['top'] - 1 <= w['top'] <= anchor['top'] + 45]
            positions[module] = ((min(w['x0'] for w in group) + max(w['x1'] for w in group)) / 2,
                                 float(page.mediabox.height) - anchor['top'])
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=(float(page.mediabox.width), float(page.mediabox.height)))
    c.setFillColor(INK)
    c.setFont('LfxArialBold', 21)
    for module, lines in [('M10', ['M10', 'Analítica']), ('M11', ['M11', 'Canal', 'moderno'])]:
        x, top = positions[module]
        for j, line in enumerate(lines):
            c.drawCentredString(x, top - 18 - j * 23, line)
    c.save()
    page.merge_page(PdfReader(buffer).pages[0])
    writer.add_metadata({'/Title': 'LafroX — nombres canónicos de módulos 4.1'})
    with (OUT / name.replace('.pdf', '_41_corregida.pdf')).open('wb') as f:
        writer.write(f)


if __name__ == '__main__':
    general()
    for name in ['ARQL-23_Enlace_servicios.pdf', 'ARQL-24_Negocio.pdf', 'ARQL-25_Integracion_eventos.pdf']:
        canonical_names(name)
    print('LafroX: 4 variantes vectoriales generadas; originales conservados.')
