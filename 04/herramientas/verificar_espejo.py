"""Read-only acceptance checks for the SD4 Markdown/LaTeX mirror."""
import contextlib
import hashlib
import io
import json
import re
import runpy
import urllib.parse
from pathlib import Path

capture=io.StringIO()
with contextlib.redirect_stdout(capture):
    s=runpy.run_path(str(Path(__file__).with_name('auditar_espejo.py')))
root=s['ROOT']; md=s['MD']; labels=s['labels']; conv=s['conv']
assert all(not r['differences'] for r in s['result']), 'Text differences remain'
files={p.name:p.read_text(encoding='utf-8-sig') for p in md.glob('*.md')}
def slug(t):
    t=t.casefold(); t=re.sub(r'[^\w\s-]','',t);return re.sub(r'\s+','-',t).strip('-')
anchors={name:set(re.findall(r'<a id="([^"]+)"',text))|{slug(t) for t in re.findall(r'^#+ (.+)$',text,re.M)} for name,text in files.items()}
broken=[]; checked=0
for name,text in files.items():
    for link in re.findall(r'\[[^\n]*?\]\(([^)]+)\)',text):
        if link.startswith(('http:','https:')):continue
        target,_,fragment=urllib.parse.unquote(link).partition('#')
        target=target or name
        if target in files:
            checked+=1
            if fragment and fragment not in anchors[target]:broken.append((name,link))
        elif not (md/target).exists():broken.append((name,link))
assert not broken, broken

body=files['LAFROX-Subdocumento4.md']
compiled=dict(conv.lof_entries(root/'entrega/_build','LAFROX-Subdocumento4'))
figures=re.findall(r'^\*\*Figura (\d+) — (.+)\*\*$',body,re.M)
assert len(figures)==len(compiled)==27,(len(figures),len(compiled))
assert dict(figures)==compiled,'Figure titles or numbering differ'
figure_assets=[]
for url in re.findall(r'https://raw.githubusercontent.com/PatricioH315/LafroX/[^/]+/([^\s)]+)',body):
    path=root/urllib.parse.unquote(url)
    assert path.is_file(),str(path)
    figure_assets.append(str(path.relative_to(root)).replace('\\','/'))
assert len(figure_assets)==27,len(figure_assets)
for number,target in re.findall(r'\[(\d+)\]\(LAFROX-Subdocumento4.md#(fig:[^)]+)\)',body):
    assert labels[target]['number']==number,(target,number,labels[target]['number'])

diagram=root/'04/figuras/fuentes/fisica/Red_general_sitios_regiones.drawio'
digest=hashlib.sha256(diagram.read_bytes()).hexdigest()
assert digest=='912bf7b551a9bd005b9e8f00b39d265faa7ff34221b6934f33cf4ee33b841aac','Approved XML changed'
summary={'text_blocks':{r['doc']:r['md_lines'] for r in s['result']},'content_differences':0,'local_links_checked':checked,'broken_local_links':broken,'figures':len(figures),'assets':figure_assets,'approved_diagram_sha256':digest}
print(json.dumps(summary,ensure_ascii=False))
