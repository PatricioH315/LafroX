from html import unescape
import re
import xml.etree.ElementTree as ET
from pathlib import Path

source = Path('08_plan_riesgos/figuras/LafroX_RBS_riesgos.drawio')
target = Path('08_plan_riesgos/figuras/rbs.tex')
root = ET.parse(source).getroot()
branches = {}
risks = {i: [] for i in range(1, 7)}

def plain(value):
    value = re.sub(r'<br\s*/?>', '\n', value, flags=re.I)
    value = re.sub(r'<[^>]+>', '', value)
    return unescape(value)

def tex_escape(value):
    return (value.replace('\\', r'\textbackslash{}')
                 .replace('&', r'\&').replace('%', r'\%')
                 .replace('$', r'\$').replace('#', r'\#')
                 .replace('_', r'\_').replace('{', r'\{')
                 .replace('}', r'\}'))

for cell in root.iter('mxCell'):
    cell_id = cell.get('id', '')
    value = plain(cell.get('value', '')).strip()
    if cell_id.startswith('b') and cell_id[1:].isdigit():
        n = int(cell_id[1:])
        first = value.splitlines()[0]
        match = re.match(r'\d+\s*·\s*(.+)', first)
        count = re.search(r'(\d+)\s+riesgos', value)
        if match and count:
            branches[n] = (match.group(1), int(count.group(1)))
        continue
    node = re.match(r'n([1-6])\.', cell_id)
    if not node:
        continue
    rid = re.search(r'R-\d{3}', value)
    zone = re.search(r'R-\d{3}\s*·\s*([^\s]+)', value)
    if not rid or not zone:
        continue
    lines = value.splitlines()
    title = re.sub(r'^\s*\d+(?:\.\d+)?\s+', '', lines[0]).strip()
    risks[int(node.group(1))].append((rid.group(0), title, zone.group(1)))

assert set(branches) == set(range(1, 7)), branches
assert sum(map(len, risks.values())) == 40, {k: len(v) for k, v in risks.items()}
all_ids = [risk[0] for branch_risks in risks.values() for risk in branch_risks]
assert len(set(all_ids)) == 40, 'duplicate risk IDs'
assert set(all_ids) == {f'R-{n:03d}' for n in range(1, 41)}, 'risk ID coverage mismatch'
assert all(len(risks[k]) == branches[k][1] for k in branches)

lines = [r'\clearpage', r'\begingroup',
         r'\newgeometry{layoutwidth=330mm,layoutheight=216mm,layoutoffset={0mm,0mm},margin=10mm,headheight=0pt,headsep=0pt,footskip=28pt}',
         r'\setlength{\paperwidth}{330mm}', r'\setlength{\paperheight}{216mm}',
         r'\pagewidth=\paperwidth', r'\pageheight=\paperheight',
         r'\setlength{\parindent}{0pt}', r'\setlength{\fboxsep}{4pt}',
         r'\newcommand{\RBSrisk}[3]{\noindent\textbf{#1} \hfill {\scriptsize #3}\\[-1pt] #2\par\vspace{3pt}}']

for page, group in enumerate((range(1, 4), range(4, 7)), start=1):
    if page == 2:
        lines.append(r'\clearpage')
    lines += [r'\thispagestyle{empty}', r'\begin{center}',
              r'{\Large\bfseries Estructura de desglose de riesgos (RBS)}\\[3pt]',
              r'{\small LafroX · 40 riesgos · clasificación por fuente predominante · página %d de 2}' % page,
              r'\end{center}']
    if page == 1:
        lines += [r'\captionof{figure}{Estructura de desglose de riesgos (EDR/RBS) del proyecto LafroX: 40 riesgos, organizada en seis ramas y distribuida en dos páginas oficio. Fuente: elaboración propia.}',
                  r'\label{fig:sd8-rbs}', r'\vspace{5pt}']
    else:
        lines += [r'\vspace{8pt}']
    columns = []
    for number in group:
        name, count = branches[number]
        col = [r'\begin{minipage}[t]{0.32\textwidth}', r'\fbox{',
               r'\begin{minipage}[t]{0.90\linewidth}',
               r'{\large\bfseries %d · %s}\\[-1pt]' % (number, tex_escape(name)),
               r'{\small %d riesgos}\\[3pt]\hrule\vspace{5pt}' % count,
               r'\footnotesize']
        for rid, title, zone in sorted(risks[number], key=lambda row: int(row[0][2:])):
            col.append(r'\RBSrisk{%s}{%s}{%s}' % (rid, tex_escape(title), tex_escape(zone)))
        col += [r'\end{minipage}', r'}', r'\end{minipage}']
        columns.append('\n'.join(col))
    lines.append('\hfill\n'.join(columns))
    lines += [r'\vspace{4pt}']

lines += [r'\restoregeometry', r'\pagewidth=\paperwidth', r'\pageheight=\paperheight', r'\endgroup', '']
target.write_text('\n'.join(lines), encoding='utf-8')
print(f'Generated {target}: {sum(map(len, risks.values()))} risks across 2 oficio pages')
