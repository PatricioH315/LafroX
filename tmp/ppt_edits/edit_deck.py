from pathlib import Path
from copy import deepcopy
import hashlib, json, re, zipfile
from lxml import etree as E

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'Presentaciones/Actualizada/LafroX - Informe 2 - calidad e innovaciones revisadas.pptx'
OUTPUT = ROOT / 'Presentaciones/Actualizada/LafroX - Informe 2 - numeracion Gantt y EDT ajustadas.pptx'
NS = {'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
      'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
COUNTS = [9, 6, 11, 3, 4, 6, 3, 5, 2]

def cn(shape):
    return shape.find('p:nvSpPr/p:cNvPr', NS)

def text(shape):
    return ' '.join(shape.xpath('.//a:t/text()', namespaces=NS))

def set_text(shape, value):
    runs = shape.findall('.//a:t', NS)
    assert runs
    runs[0].text = value
    for run in runs[1:]:
        run.text = ''

def tree(root):
    return root.find('p:cSld/p:spTree', NS)

def shapes(root):
    return root.findall('p:cSld/p:spTree/p:sp', NS)

def name_for(phase, index):
    return f'!!edt_cc_{phase}_{index}'

def xml(root):
    return E.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True)

assert not OUTPUT.exists(), 'Do not overwrite a previous output'
before_hash = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
with zipfile.ZipFile(SOURCE) as z:
    original = {name: z.read(name) for name in z.namelist()}
    infos = z.infolist()
data = dict(original)
slides = {i: E.fromstring(original[f'ppt/slides/slide{i}.xml']) for i in range(1, 52)}
assert len(E.fromstring(original['ppt/presentation.xml']).find('p:sldIdLst', NS)) == 51

# Change the existing footer only; no recreation of slides, media or transitions.
for i, root in slides.items():
    counters = [s for s in shapes(root) if cn(s).get('name') == '!!slidenum']
    assert len(counters) == (0 if i == 1 else 1), (i, len(counters))
    if counters:
        set_text(counters[0], f'{i:02d}')

# Remove both labels and the native shapes which actually encode the removed details.
removed = {}
for i in [20, 21]:
    removed[i] = []
    for s in list(shapes(slides[i])):
        c = cn(s)
        sid, name = int(c.get('id')), c.get('name')
        if sid == 1637:
            set_text(s, 'Meses 1–24 · actividades, hitos y congelamientos')
        # Quality's only bars represent certification and restoration. Remove
        # its now-empty heading too, along with the already-empty software row.
        if sid in {1660, 1664, 1665, 1666, 1671, 1673} or name in {'!!gv_6', '!!gv_7', '!!gv_8'}:
            removed[i].append({'id': sid, 'name': name, 'text': text(s)})
            tree(slides[i]).remove(s)

note_path = 'ppt/notesSlides/notesSlide21.xml'
note = E.fromstring(original[note_path])
body = note.xpath('.//p:sp[p:nvSpPr/p:nvPr/p:ph[@type="body"]]', namespaces=NS)
assert len(body) == 1
set_text(body[0], 'Gantt mes a mes. En gris, los congelamientos de septiembre y diciembre: no se despliega nada. Migración en los meses 7 a 12; la Etapa 1 entra en tres olas y pasa a producción en el H7 (mes 16), y la Etapa 2 en el H12 (mes 21). Los hitos marcan los puntos de control del cronograma. (T-14 y T-15)')
data[note_path] = xml(note)

# The overview contains exactly 49 circles, one per control account.
dots = {}
phase = None
for s in shapes(slides[22]):
    name = cn(s).get('name')
    if re.fullmatch(r'!!ph[1-9]', name):
        phase = int(name[4:])
    geom = s.find('p:spPr/a:prstGeom', NS)
    if geom is not None and geom.get('prst') == 'ellipse':
        assert phase is not None
        dots.setdefault(phase, []).append(s)

for phase, count in enumerate(COUNTS, 1):
    assert len(dots[phase]) == count
    for j, s in enumerate(dots[phase], 1):
        cn(s).set('name', name_for(phase, j))
        cn(s).set('descr', f'Cuenta de control {phase}.{j}')

for phase in range(1, 10):
    root = slides[22 + phase]
    active = []
    for s in shapes(root):
        first = s.find('.//a:t', NS)
        if first is not None and re.fullmatch(fr'{phase}\.\d+', first.text or ''):
            j = int(first.text.split('.')[1])
            cn(s).set('name', name_for(phase, j))
            cn(s).set('descr', f'Cuenta de control {phase}.{j}')
            active.append(j)
    assert sorted(active) == list(range(1, COUNTS[phase-1] + 1))
    # Preserve all inactive account objects so they can retract and expand.
    # Compact circles into the gap above the detail heading (8px, 10px pitch
    # at 1600px render width). The three-row Construction group ends at y458.
    next_id = max(int(c.get('id')) for c in root.findall('.//p:cNvPr', NS)) + 1
    for other in range(1, 10):
        if other == phase:
            continue
        for j, source_dot in enumerate(dots[other]):
            dot = deepcopy(source_dot)
            cn(dot).set('id', str(next_id))
            next_id += 1
            xfrm = dot.find('p:spPr/a:xfrm', NS)
            off, ext = xfrm.find('a:off', NS), xfrm.find('a:ext', NS)
            off.set('x', str(int(off.get('x')) + (int(ext.get('cx')) - 91440) // 2))
            off.set('y', str(4914900 + (j // 5) * 114300))
            ext.set('cx', '91440')
            ext.set('cy', '91440')
            tree(root).append(dot)

for i, root in slides.items():
    raw = xml(root)
    # Keep parts which did not semantically change byte-for-byte.
    if E.tostring(root) != E.tostring(E.fromstring(original[f'ppt/slides/slide{i}.xml'])):
        data[f'ppt/slides/slide{i}.xml'] = raw

# Package-level and content regression assertions.
for i in range(1, 52):
    old, new = E.fromstring(original[f'ppt/slides/slide{i}.xml']), slides[i]
    strip = lambda r: [E.tostring(x) for x in r if E.QName(x).localname not in {'cSld'}]
    assert strip(old) == strip(new), f'Non-content slide metadata changed: {i}'
    ids = [c.get('id') for c in new.findall('.//p:cNvPr', NS)]
    assert len(ids) == len(set(ids)), f'Duplicate IDs: {i}'
    if i >= 2:
        assert [text(s) for s in shapes(new) if cn(s).get('name') == '!!slidenum'] == [f'{i:02d}']
    if i not in {20, 21}:
        texts = lambda r: [text(s) for s in shapes(r) if cn(s).get('name') != '!!slidenum' and text(s)]
        assert texts(old) == texts(new), f'Content text changed: {i}'

expected_names = {name_for(p, j) for p in range(1, 10) for j in range(1, COUNTS[p-1]+1)}
for i in range(22, 32):
    names = [cn(s).get('name') for s in shapes(slides[i]) if cn(s).get('name').startswith('!!edt_cc_')]
    assert len(names) == 49 and set(names) == expected_names
    assert slides[i].xpath('//*[local-name()="morph"][@option="byObject"]')
    if i >= 23:
        p = i - 22
        for s in shapes(slides[i]):
            name = cn(s).get('name')
            if name.startswith('!!edt_cc_'):
                geom = s.find('p:spPr/a:prstGeom', NS).get('prst')
                assert geom == ('roundRect' if name.startswith(f'!!edt_cc_{p}_') else 'ellipse')

for i in [20, 21]:
    joined = ' '.join(text(s) for s in shapes(slides[i])).lower()
    assert not any(word in joined for word in ['certif', 'riesgo', 'restauraci', 'reversi'])
    for s in shapes(slides[i]):
        sid = cn(s).get('id')
        old = [x for x in shapes(E.fromstring(original[f'ppt/slides/slide{i}.xml'])) if cn(x).get('id') == sid][0]
        assert E.tostring(s.find('p:spPr', NS)) == E.tostring(old.find('p:spPr', NS)), (i, sid)

changed = [name for name in data if data[name] != original[name]]
assert all(re.fullmatch(r'ppt/slides/slide\d+\.xml', name) or name == note_path for name in changed)
with zipfile.ZipFile(OUTPUT, 'w', zipfile.ZIP_DEFLATED) as z:
    for info in infos:
        z.writestr(info, data[info.filename])
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == before_hash
report = {'source': str(SOURCE), 'output': str(OUTPUT), 'source_sha256': before_hash,
          'output_sha256': hashlib.sha256(OUTPUT.read_bytes()).hexdigest(), 'slides': 51,
          'changed_parts': changed, 'gantt_removed': removed,
          'morph_accounts_per_slide': 49, 'morph_phase_counts': COUNTS,
          'all_other_package_parts_unchanged': True, 'assertions': 'passed'}
(Path(__file__).parent / 'edit_report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(report, ensure_ascii=False, indent=2))
