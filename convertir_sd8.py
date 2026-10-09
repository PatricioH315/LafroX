"""Conversión reproducible de las tres fuentes Markdown del SD8 a LaTeX."""
from pathlib import Path
import re
import math

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent.parent / 'Git Markdown' / 'LafroX' / '08_plan_riesgos'
DEST = ROOT / '08_plan_riesgos'
DEST.mkdir(exist_ok=True)

def inline(text):
    tokens = []
    def save(value):
        tokens.append(value)
        return f'ZZTOKEN{len(tokens)-1}ZZ'
    text = re.sub(r'`([^`]+)`', lambda m: save(r'\texttt{' + escape(m[1]) + '}'), text)
    text = escape(text)
    text = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', text)
    text = re.sub(r'\*([^*]+)\*', r'\\emph{\1}', text)
    for i, value in enumerate(tokens):
        text = text.replace(f'ZZTOKEN{i}ZZ', value)
    return text

def escape(text):
    mapping = {'\\': r'\textbackslash{}', '&': r'\&', '%': r'\%', '$': r'\$', '#': r'\#', '_': r'\_', '{': r'\{', '}': r'\}', '~': r'\textasciitilde{}', '^': r'\textasciicircum{}', '≤': r'\ensuremath{\leq}', '≥': r'\ensuremath{\geq}', '×': r'\ensuremath{\times}', '−': r'\ensuremath{-}', '→': r'\ensuremath{\rightarrow}', '≈': r'\ensuremath{\approx}', 'Σ': r'\ensuremath{\Sigma}'}
    return ''.join(mapping.get(c, c) for c in text)

def convert(filename, kind):
    lines = (SOURCE / filename).read_text(encoding='utf-8-sig').splitlines()
    out = ['% Fuente: ' + filename, '% Texto y datos conservados; formato adaptado a lafrox.cls.']
    pending = None
    scope = 'Plan de riesgos'
    i = 1
    table = 0
    inlist = False
    while i < len(lines):
        line = lines[i].strip()
        if inlist and not line.startswith('- '):
            out.append(r'\end{itemize}')
            inlist = False
        if line.startswith('```mermaid'):
            while not lines[i+1].startswith('```'):
                i += 1
            i += 2
            out.append(r'\parte{figuras/rbs}')
            continue
        if line.startswith('**Figura 8.1'):
            i += 1
            continue
        match = re.match(r'\*\*Tabla ([\w.]+)\s*[—–-]\s*(.*?)\*\*$', line)
        if match:
            pending = (match[1], match[2])
            i += 1
            continue
        if line.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?', c) for c in cells):
                    rows.append(cells)
                i += 1
            n = len(rows[0]); table += 1
            assert all(len(row) == n for row in rows), (filename, i)
            landscape = False  # La plantilla exige papel en orientación vertical.
            if landscape:
                out.append(r'\begin{landscape}')
            inferred = None
            if kind == 'anexos':
                inferred = {2: ('B.1', 'Prioridad cualitativa y exposición inicial'), 4: ('C.1', 'Escenarios deterministas: reglas, efectos y decisiones')}.get(table)
            number, title = pending or inferred or (None, scope)
            if number:
                out.append(r'\renewcommand{\thetable}{' + number + '}')
            else:
                prefix = {'cuerpo': '8.IA', 'anexos': '8.Aux', 't16': 'T-16'}[kind]
                out.append(r'\renewcommand{\thetable}{' + prefix + '.' + str(table) + '}')
            # Ancho proporcional a la cantidad de texto de cada columna.
            weights = [max(1.0, math.sqrt(sum(len(r[c]) for r in rows)/len(rows))) for c in range(n)]
            if kind == 't16' and n == 8:
                weights = [1.3, 3, 1.8, 0.9, 1.1, 1, 5.8, 1.9]
            weights = [w*n/sum(weights) for w in weights]
            columns = ' '.join(r'>{\hsize=' + f'{w:.5f}' + r'\hsize\linewidth=\hsize\RaggedRight\arraybackslash}X' for w in weights)
            out.append(r'\begin{tablalafrox}{' + inline(title) + '}{tab:sd8-' + kind + '-' + str(table) + '}{' + columns + '}{' + ' & '.join(r'\cab{' + inline(c) + '}' for c in rows[0]) + '}')
            out.extend(' & '.join(inline(c) for c in row) + r' \\' for row in rows[1:])
            out.append(r'\end{tablalafrox}')
            if landscape:
                out.append(r'\end{landscape}')
            pending = None
            continue
        heading = re.match(r'(#+)\s+(.+)', line)
        if heading:
            level, title = len(heading[1]), heading[2]
            scope = title
            if kind == 'cuerpo' and re.match(r'8\.\d', title):
                title = re.sub(r'^8\.\d+(?:\.\d+)*\s+', '', title)
                command = 'section' if level == 2 else 'subsection'
                out.append('\\' + command + '{' + inline(title) + '}')
            else:
                command = 'subsection' if level >= 3 else 'section'
                if title.startswith('Anexo 8.'):
                    out.append(r'\clearpage')
                out.append('\\' + command + '*{' + inline(title) + '}')
                if command == 'section':
                    out.append(r'\addcontentsline{toc}{section}{' + inline(title) + '}')
            i += 1
            continue
        if line.startswith('- '):
            if not inlist:
                out.append(r'\begin{itemize}[leftmargin=*,itemsep=3pt]')
                inlist = True
            out.append(r'\item ' + inline(line[2:]))
        elif line == '---':
            out.append(r'\medskip')
        else:
            out.append(inline(line))
        i += 1
    if inlist:
        out.append(r'\end{itemize}')
    return '\n'.join(out) + '\n'

for name, kind, target in [
    ('LAFROX-Subdocumento8.md', 'cuerpo', 'partes/cuerpo.tex'),
    ('LAFROX-Subdocumento8-Anexos.md', 'anexos', 'anexos/anexos.tex'),
    ('LAFROX-Formulario-T-16.md', 't16', 'formularios/t16.tex'),
]:
    path = DEST / target
    path.parent.mkdir(parents=True, exist_ok=True)
    converted = convert(name, kind)
    # Cada párrafo, viñeta y celda debe aparecer completo en la salida.
    fenced = False
    checked = 0
    for original in (SOURCE / name).read_text(encoding='utf-8-sig').splitlines():
        original = original.strip()
        if original.startswith('```'):
            fenced = not fenced
            continue
        if fenced or not original or original.startswith('#') or original.startswith('**Tabla') or original.startswith('**Figura') or original == '---':
            continue
        if original.startswith('|'):
            cells = [c.strip() for c in original.strip('|').split('|')]
            if all(re.fullmatch(r':?-+:?', c) for c in cells):
                continue
        else:
            cells = [original[2:] if original.startswith('- ') else original]
        for cell in cells:
            assert inline(cell) in converted, (name, cell)
            checked += 1
    path.write_text(converted, encoding='utf-8')
    print(f'{name}: {checked} párrafos y celdas verificados.')

(DEST / 'contenido.tex').write_text(r'''\chapter{Plan de riesgos}
\label{cap:sd8}
\parte{partes/cuerpo}
\clearpage
\section*{Anexos del Subdocumento 8}
\addcontentsline{toc}{section}{Anexos del Subdocumento 8}
\parte{anexos/anexos}
\clearpage
\section*{Formulario T-16: Plan de riesgos}
\addcontentsline{toc}{section}{Formulario T-16: Plan de riesgos}
\parte{formularios/t16}
''', encoding='utf-8')
