from pathlib import Path
from copy import deepcopy
from lxml import etree as E
import zipfile, hashlib, json, re

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'Presentaciones/Actualizada/LafroX - Informe 2 - numeracion Gantt y EDT ajustadas.pptx'
OUTPUT = ROOT / 'Presentaciones/Actualizada/LafroX - Informe 2 - transicion Gantt y EDT refinadas.pptx'
N = {'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
     'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
def shapes(r): return r.findall('p:cSld/p:spTree/p:sp', N)
def cn(s): return s.find('p:nvSpPr/p:cNvPr', N)
def tree(r): return r.find('p:cSld/p:spTree', N)
def byid(r, sid): return next(s for s in shapes(r) if cn(s).get('id') == str(sid))
def byname(r, name): return next(s for s in shapes(r) if cn(s).get('name') == name)
def xfrm(s): return s.find('p:spPr/a:xfrm', N)
def text(s): return s.xpath('.//a:t/text()', namespaces=N)
if OUTPUT.exists():
    prior = json.loads((ROOT/'tmp/ppt_edits/refine-report.json').read_text(encoding='utf-8'))
    assert hashlib.sha256(OUTPUT.read_bytes()).hexdigest() == prior['output_sha256'], 'Output changed outside this refinement'
source_hash = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
with zipfile.ZipFile(SOURCE) as z:
    data = {f: z.read(f) for f in z.namelist()}; infos = z.infolist()
original = data.copy()
slides = {i: E.fromstring(data[f'ppt/slides/slide{i}.xml']) for i in range(1, 52)}

# Leave the EDT overview (22) byte-identical. Give every inactive dot the
# exact geometry of its source in that overview, not a shrunken substitute.
overview = {cn(s).get('name'): s for s in shapes(slides[22]) if cn(s).get('name').startswith('!!edt_cc_')}
assert len(overview) == 49
for i in range(23, 32):
    active = i - 22
    for s in shapes(slides[i]):
        name = cn(s).get('name')
        if name.startswith('!!edt_cc_'):
            phase = int(name.split('_')[2])
            if phase != active:
                old = xfrm(s)
                s.find('p:spPr', N).replace(old, deepcopy(xfrm(overview[name])))
            else:
                off = xfrm(s).find('a:off', N)
                off.set('y', str(int(off.get('y')) + 914400))
        elif any(t.startswith('FASE ') and 'CUENTAS DE CONTROL' in t for t in text(s)):
            off = xfrm(s).find('a:off', N)
            off.set('y', str(int(off.get('y')) + 914400))

# Make slide 20 a meaningful Morph bridge rather than a pushed-in frame
# with nearly zero-length bars. Slide 21 keeps revealing waves and milestones.
for name in ['!!gv_0', '!!gv_1', '!!gv_2', '!!gv_3', '!!gv_5', '!!gv_9']:
    s = byname(slides[20], name)
    s.find('p:spPr', N).replace(xfrm(s), deepcopy(xfrm(byname(slides[21], name))))

# These two activity bars previously appeared only on 21. Include them in
# the bridge and keep their exact final dates and placement.
for sid, name in [(1657, '!!gv_4'), (1670, '!!gv_10')]:
    final_bar = byid(slides[21], sid)
    cn(final_bar).set('name', name)
    clone = deepcopy(final_bar)
    cn(clone).set('id', str(3000 + sid))
    label_id = 1656 if sid == 1657 else 1669
    label = byid(slides[20], label_id)
    tree(slides[20]).insert(tree(slides[20]).index(label) + 1, clone)

# Force correspondences only where the meaning is conserved: Architecture,
# Construction E1/E2, Implementation and Operation. Do not conflate quality,
# governance or infrastructure with migration, for example.
for sid, name in {1535:'!!gv_0', 1538:'!!gv_1', 1541:'!!gv_4', 1550:'!!gv_3', 1553:'!!gv_10'}.items():
    cn(byid(slides[19], sid)).set('name', name)
for src, dest, name in [(1533,1647,'!!gantt_label_design'), (1536,1649,'!!gantt_label_e1'),
                         (1539,1656,'!!gantt_label_e2'), (1551,1669,'!!gantt_label_operation')]:
    cn(byid(slides[19], src)).set('name', name)
    cn(byid(slides[20], dest)).set('name', name)
    cn(byid(slides[21], dest)).set('name', name)

# Keep the moving bars as the visual link. A three-line title forced into
# a single-line box stretches badly mid-Morph, so fade between those two
# titles instead; the Gantt title remains stable between 20 and 21.
for i in [20, 21]:
    cn(byname(slides[i], '!!title')).set('name', '!!gantt_title')

# Reuse a known-good native PowerPoint Morph extension. Keep the original
# automatic 100ms advance of this bridge, now after a 1.4s transformation.
transition = slides[20].find('p:transition', N)
assert transition is not None
slides[20].remove(transition)
alt = deepcopy(next(x for x in slides[21] if E.QName(x).localname == 'AlternateContent'))
for t in alt.xpath('.//p:transition', namespaces=N):
    t.set('advTm', '100')
    if t.get('{http://schemas.microsoft.com/office/powerpoint/2010/main}dur'):
        t.set('{http://schemas.microsoft.com/office/powerpoint/2010/main}dur', '1400')
slides[20].append(alt)

modified = [19,20,21,*range(23,32)]
for i in modified:
    data[f'ppt/slides/slide{i}.xml'] = E.tostring(slides[i], xml_declaration=True, encoding='UTF-8', standalone=True)

for i in range(1,52):
    old = E.fromstring(original[f'ppt/slides/slide{i}.xml'])
    new = slides[i]
    old_text = old.xpath('//a:t/text()', namespaces=N)
    new_text = new.xpath('//a:t/text()', namespaces=N)
    assert old_text == new_text, f'Text changed: {i}'
    assert len(new.findall('.//p:cNvPr', N)) == len(set(c.get('id') for c in new.findall('.//p:cNvPr', N))), f'Duplicate ID: {i}'
    if i != 20:
        other = lambda r: [E.tostring(c) for c in r if E.QName(c).localname != 'cSld']
        assert other(old) == other(new), f'Other transition changed: {i}'
    if 23 <= i <= 31:
        dots = [s for s in shapes(new) if cn(s).get('name').startswith('!!edt_cc_') and s.find('p:spPr/a:prstGeom',N).get('prst')=='ellipse']
        cards = [s for s in shapes(new) if cn(s).get('name').startswith('!!edt_cc_') and s not in dots]
        assert len(dots)+len(cards)==49
        for dot in dots:
            assert E.tostring(xfrm(dot)) == E.tostring(xfrm(overview[cn(dot).get('name')]))
        max_dot_y = max(int(xfrm(d).find('a:off',N).get('y')) + int(xfrm(d).find('a:ext',N).get('cy')) for d in dots)
        heading = next(s for s in shapes(new) if any(t.startswith('FASE ') and 'CUENTAS DE CONTROL' in t for t in text(s)))
        assert int(xfrm(heading).find('a:off',N).get('y')) - max_dot_y >= 400000
        for card in cards:
            assert int(xfrm(card).find('a:off',N).get('y'))+int(xfrm(card).find('a:ext',N).get('cy')) < 9000000

assert data['ppt/slides/slide22.xml'] == original['ppt/slides/slide22.xml']
assert set(f for f in data if data[f]!=original[f])=={f'ppt/slides/slide{i}.xml' for i in modified}
with zipfile.ZipFile(OUTPUT, 'w', zipfile.ZIP_DEFLATED) as z:
    for info in infos: z.writestr(info, data[info.filename])
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==source_hash
report = {'source':str(SOURCE),'output':str(OUTPUT),'source_sha256':source_hash,
          'output_sha256':hashlib.sha256(OUTPUT.read_bytes()).hexdigest(), 'slide_count':51,
          'modified_slides':modified,'edt_overview_unchanged':True,'detail_offset_emu':914400,
          'inactive_dots_identical_to_overview':True,'transition20':'native Morph, 1400ms, automatic advance preserved',
          'text_and_other_package_parts_unchanged':True}
(ROOT/'tmp/ppt_edits/refine-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
