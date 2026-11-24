"""Corrige el rótulo vectorial de la Figura 1 sin redibujar sus componentes.

Sincroniza el XML editable y el PDF de la figura. Conserva fuentes, imágenes,
conexiones y dimensiones. Se ejecuta una vez; repetirlo solo verifica el cierre.
"""
from pathlib import Path
import re
from pypdf import PdfReader, PdfWriter
from pypdf.generic import ByteStringObject, ContentStream, FloatObject

ROOT = Path(__file__).resolve().parents[2]
XML = ROOT / '04/figuras/fuentes/Arquitectura-logica-general-y-8-capas.drawio.xml'
PDF = ROOT / '04/figuras/logica/capas/ARQL-01_General_definitivo.pdf'


def font_mapping(font):
    source = font['/ToUnicode'].get_data().decode('ascii')
    mapping = {}
    for block in re.findall(r'beginbfchar(.*?)endbfchar', source, re.S):
        for code, value in re.findall(r'<(\w+)>\s*<(\w+)>', block):
            mapping[int(code, 16)] = chr(int(value, 16))
    for block in re.findall(r'beginbfrange(.*?)endbfrange', source, re.S):
        for first, last, value in re.findall(r'<(\w+)>\s*<(\w+)>\s*<(\w+)>', block):
            for code in range(int(first, 16), int(last, 16) + 1):
                mapping[code] = chr(int(value, 16) + code - int(first, 16))
    descendant = font['/DescendantFonts'][0].get_object()
    array, widths, i = descendant['/W'], {}, 0
    while i < len(array):
        start, following = int(array[i]), array[i + 1]
        if isinstance(following, list):
            widths.update({start + j: float(w) for j, w in enumerate(following)})
            i += 2
        else:
            widths.update({j: float(array[i + 2]) for j in range(start, int(following) + 1)})
            i += 3
    return mapping, widths, float(descendant.get('/DW', 1000))


def correct():
    reader = PdfReader(PDF)
    original_text = reader.pages[0].extract_text()
    if 'Valkey' in original_text and ' Redis' not in original_text:
        assert 'Valkey' in XML.read_text(encoding='utf-8')
        print('Figura 1: fuente editable y PDF ya corregidos.')
        return
    writer = PdfWriter()
    writer.clone_document_from_reader(reader)
    page = writer.pages[0]
    fonts = page['/Resources']['/Font']
    maps = {name: font_mapping(font.get_object()) for name, font in fonts.items()}
    stream = ContentStream(page.get_contents(), writer)
    font_name, matches = None, []
    for i, (args, operator) in enumerate(stream.operations):
        if operator == b'Tf':
            font_name = args[0]
        if operator == b'Tj':
            raw = args[0].original_bytes if hasattr(args[0], 'original_bytes') else args[0]
            mapping = maps[font_name][0]
            decoded = ''.join(mapping[int.from_bytes(raw[j:j + 2], 'big')]
                              for j in range(0, len(raw), 2))
            if decoded in ('Redis', '(ElastiCache', '· solo nube)'):
                matches.append((i, decoded, font_name))
    assert [m[1] for m in matches] == ['Redis', '(ElastiCache', '· solo nube)'], matches
    assert len({m[2] for m in matches}) == 1
    font_name = matches[0][2]
    mapping, widths, default_width = maps[font_name]
    inverse = {value: key for key, value in mapping.items()}
    size = 22
    lines = [('Valkey', 3265), ('(Amazon', 3288), ('ElastiCache', 3311), ('· solo nube)', 3334)]
    replacement = []
    for text, baseline in lines:
        width = size * sum(widths.get(inverse[c], default_width) for c in text) / 1000
        assert width < 160
        raw = b''.join(inverse[c].to_bytes(2, 'big') for c in text)
        replacement.extend([
            ([], b'BT'),
            ([font_name, FloatObject(size)], b'Tf'),
            ([FloatObject(v) for v in (1, 0, 0, -1, 762 - width / 2, baseline)], b'Tm'),
            ([ByteStringObject(raw)], b'Tj'),
            ([], b'ET'),
        ])
    first, last = matches[0][0] - 3, matches[-1][0] + 2
    assert stream.operations[first][1] == b'BT'
    assert stream.operations[last - 1][1] == b'ET'
    stream.operations[first:last] = replacement
    page.replace_contents(stream)
    temporary = PDF.with_suffix('.actualizado.pdf')
    writer.write(temporary)
    result = PdfReader(temporary)
    normalize = lambda text: ''.join(text.split())
    new = normalize(result.pages[0].extract_text())
    old = normalize(original_text)
    assert new.replace('Valkey(AmazonElastiCache·solonube)', 'Redis(ElastiCache·solonube)') == old
    assert result.pages[0].mediabox == reader.pages[0].mediabox
    old_images = [obj.get_object().get_data() for obj in reader.pages[0]['/Resources']['/XObject'].values()]
    new_images = [obj.get_object().get_data() for obj in result.pages[0]['/Resources']['/XObject'].values()]
    assert old_images == new_images
    xml_bytes = XML.read_bytes()
    old_value = b'value="Redis&#xA;(ElastiCache \xc2\xb7 solo nube)"'
    new_value = 'value="Valkey&#xA;(Amazon&#xA;ElastiCache&#xA;· solo nube)"'.encode('utf-8')
    assert xml_bytes.count(old_value) == 1
    # Modifica solo el estilo de la celda que contiene el servicio.
    pattern = rb'(<mxCell\s+id="OEwDW-F6gLmMDvgjbRT0-52"[^>]*fontSize=)26(;[^>]*value="Redis&#xA;\(ElastiCache \xc2\xb7 solo nube\)")'
    updated, count = re.subn(pattern, rb'\g<1>22\2', xml_bytes)
    assert count == 1
    XML.write_bytes(updated.replace(old_value, new_value))
    temporary.replace(PDF)
    print('Figura 1: Valkey (Amazon ElastiCache · solo nube); resto del contenido preservado.')


if __name__ == '__main__':
    correct()
