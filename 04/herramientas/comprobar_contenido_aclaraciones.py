"""Check local figures, internal links, IA coverage and full SD3 section mapping."""
from pathlib import Path
import json, re, unicodedata, urllib.parse
ROOT=Path(__file__).resolve().parents[2]
MDROOT=ROOT.parent/'LafroX-alvaro-md'
MD=MDROOT/'04_arquitectura'
QA=ROOT/'04/revision/aclaraciones_20261011'
docs={p.name:p.read_text(encoding='utf-8-sig') for p in MD.glob('*.md')}
def slug(s):
    return re.sub(r'\s+','-',re.sub(r'[^\w\s-]','',s.lower())).strip('-')
anchors={name:set(re.findall(r'<a id="([^"]+)"',s))|{slug(m) for m in re.findall(r'^#{1,6}\s+(.+)$',s,re.M)} for name,s in docs.items()}
errors=[]; links=0
for name,s in docs.items():
    for dest in re.findall(r'\]\(([^)]+)\)',s):
        if '#' not in dest or dest.startswith(('https:','D:')):continue
        filename,anchor=dest.split('#',1);filename=filename or name
        anchor=urllib.parse.unquote(anchor)
        if filename in docs:
            links+=1
            if anchor not in anchors[filename]:errors.append(name+' -> '+dest)
    ids=re.findall(r'<a id="([^"]+)"',s)
    assert len(ids)==len(set(ids)), ('duplicate anchors',name)
    assert not re.search(r'caso\s*0?2\b',s,re.I),name
    assert '[[REVISIÓN HUMANA]]' not in s,name
assert not errors,errors
body=docs['LAFROX-Subdocumento4.md']
sections=re.findall(r'^#{1,6}\s+(4(?:\.\d+)+)\s',body,re.M)
rows=[line for line in body.splitlines() if line.startswith('| ') and 'OpenAI Codex' in line]
codes=[line.split('|')[1].strip() for line in rows]
assert len(rows)==len(sections)+24==132
assert set(sections).issubset(codes)
assert all('Álvaro Catalán:' in line and 'Alex Aravena' not in line for line in rows)
figures=[]
for match in re.finditer(r'^\*\*Figura (\d+) — (.+)\*\*\n\n(?:!\[[^]]*\]|\[[^]]*\])\(([^)]+)\)',body,re.M):
    number,title,url=match.groups()
    if url.startswith('https://raw.githubusercontent.com/'):
        suffix=url.split('/04/',1)[1]
        path=ROOT/'04'/urllib.parse.unquote(suffix)
    else:path=Path(url)
    assert path.is_file(),path
    figures.append({'number':int(number),'title':title,'path':str(path)})
assert [f['number'] for f in figures]==list(range(1,30))
annex=docs['LAFROX-Subdocumento4-Anexos.md']
assert 'Anexo Anexo' not in annex
for letter in 'jklmn':assert '- Amazon Web Services. (s. f.-'+letter+').' in annex
assert 'La selección siguiente organiza' in annex
mapping=annex[annex.index('**Tabla A.14'):annex.index('**Tabla A.15')]
modules={int(m) for m in re.findall(r'\bM(\d+)\b',mapping)}
assert set(range(1,13)).issubset(modules)
sd3=(MDROOT/'03_esquema_solucion_alcance/LAFROX-Subdocumento3.md').read_text(encoding='utf-8-sig')
expected=re.findall(r'^### (3\.[34]\.\d+) ',sd3,re.M)
assert len(expected)==9
assert all(code in mapping for code in expected)
actor_table=annex[annex.index('**Tabla A.17'):annex.index('## Anexo 4-O')]
actors=[line.split('|')[1].strip() for line in actor_table.splitlines() if line.startswith('| ')][2:]
assert len(actors)==15
for actor in actors:assert actor in sd3,actor
assert len(re.findall(r'^\| [^|]+ \|',mapping,re.M))-2==22

citations=[]
for folder in ['04/partes','04/anexos','04/formularios/T11']:
    for path in (ROOT/folder).rglob('*.tex'):
        for n,line in enumerate(path.read_text(encoding='utf-8-sig').splitlines(),1):
            for m in re.finditer(r'(Bases Técnicas Transversales|Bases Técnicas del caso|Bases Administrativas),\s*(?:cap\.|caps\.|art\.)[^;)\n]{1,100}',line):
                if not re.search(r'\bp{1,2}\.',m.group()):citations.append((path.relative_to(ROOT).as_posix(),n,m.group()))
# This is a targeted inventory, not fabricated original pagination.
report='# LafroX — Citas a Bases sin folio original verificado\n\nLas Bases disponibles localmente son Markdown sin paginación original. Se añadió la sección 16.5 a las citas de RT-16.23/24; no se inventaron folios. Completar esta lista contra el PDF original, conservando el contenido de la oferta.\n\n| Fuente LaTeX | Línea | Cita que requiere cotejo de página |\n| --- | --- | --- |\n'
report+='\n'.join(f'| {p} | {n} | {s} |' for p,n,s in citations)+'\n'
(QA/'citas_Bases_paginas_pendientes.md').write_text(report,encoding='utf-8')
(MDROOT/'Revision/citas_Bases_SD4_paginas_pendientes.md').write_text(report,encoding='utf-8')
results={'valid_internal_links':links,'figures':len(figures),'sections':len(sections),'ia_rows':len(rows),'reviewer':'Álvaro Catalán','mapped_SD3_subsections':expected,'mapped_modules':sorted(modules),'actors':actors,'citation_occurrences_without_page':len(citations)}
(QA/'contenido_verificacion.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(results,ensure_ascii=False))
