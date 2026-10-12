"""Read-only comparison of SD4 Markdown and assembled LaTeX content."""
import difflib
import importlib.util
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
MD = ROOT.parent / 'LafroX-alvaro-md' / '04_arquitectura'
spec = importlib.util.spec_from_file_location('tex2md',ROOT/'00/herramientas/tex2md.py')
conv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(conv)
DOCS = [('cuerpo','main.tex','LAFROX-Subdocumento4'),('anexos','04/anexos_logica.tex','LAFROX-Subdocumento4-Anexos'),('t11','04/formulario_T11.tex','LAFROX-Formulario-T-11')]
build = ROOT/'entrega/_build'
labels = {}; owners = {}
for doc,entry,stem in DOCS:
    found=conv.aux_labels(build,stem)
    labels.update(found); owners.update({k:doc for k in found})

def norm(line):
    line=line.strip()
    if re.fullmatch(r'(?:fisica\.chapter|4\.chapter|4-W\.section|anexo42A\.section|\[block\]|25pt28ptlafroxFuerte|0\.45em|\[1\]8pt|#12pt)',line):return ''
    line=re.sub(r'<a\s[^>]+></a>','',line)
    if re.match(r'^!?\[.*\]\(https://raw.githubusercontent.com/',line):return ''
    if re.match(r'^!?\[.*\]\([A-Za-z]:/[^)]+\.(?:pdf|png)\)$',line):return ''
    if re.match(r'^\*\*Figura .*',line):return ''
    if line.startswith('Fuente:'):return ''
    if re.match(r'^\|(?:\s*:?-+:?\s*\|)+$',line):return ''
    line=re.sub(r'\[([^]]+)\]\([^)]*\)',r'\1',line)
    line=line.replace('<dominio>','dominio')
    line=re.sub(r'<[^>]+>',' ',line)
    line=line.replace('²','2').replace('³','3')
    return ' '.join(re.findall(r'\w+',line.casefold()))

def prepared(s):
    # Navigation is format-specific; body, annexes and specifications are not.
    lines=s.splitlines()
    start=next((i for i,l in enumerate(lines) if re.match(r'^# 4[. ]',l) or l.startswith('# Anexos del Subdocumento 4') or l.startswith('# Formulario T-11')),0)
    return [(i+1,l,norm(l)) for i,l in enumerate(lines[start:]) if norm(l)]

result=[]
for doc,entry,stem in DOCS:
    src=conv.expand(ROOT/entry)
    src=re.sub(r'\\Needspace\{[^}]+\}', '', src)
    src=src.replace(r'\slash ', '/').replace(r'\multicolumn{5}{@{}l}',r'\multicolumn{5}{l}')
    generated,_=conv.convert(src,doc,stem,conv.toc_entries(build,stem),labels,owners,ROOT)
    actual=(MD/(stem+'.md')).read_text(encoding='utf-8-sig')
    a=prepared(actual); b=prepared(generated)
    changes=[]
    for tag,i,j,k,l in difflib.SequenceMatcher(None,[x[2] for x in a],[x[2] for x in b],autojunk=False).get_opcodes():
        if tag!='equal':changes.append({'type':tag,'md':[x[1] for x in a[i:j]],'tex':[x[1] for x in b[k:l]],'before_tex':b[k-1][1] if k else ''})
    result.append({'doc':stem,'md_lines':len(a),'tex_lines':len(b),'differences':changes})
if len(sys.argv)>1:
    target=next(r for r in result if r['doc']==sys.argv[1])
    offset=int(sys.argv[2]) if len(sys.argv)>2 else 0
    count=int(sys.argv[3]) if len(sys.argv)>3 else 12
    target=dict(target,differences=target['differences'][offset:offset+count])
    print(json.dumps(target,ensure_ascii=False))
else:
    print(json.dumps([dict(r,differences=len(r['differences'])) for r in result],ensure_ascii=False))
