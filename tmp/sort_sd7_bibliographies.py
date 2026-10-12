from pathlib import Path

for root in ('subdocumento-07', 'subdocumento-07-anexos', 'formulario-t14', 'formulario-t15', 'formulario-t18'):
    path = Path(root) / 'contenido.tex'
    text = path.read_text(encoding='utf-8')
    start = text.rfind(r'\section*{Referencias}')
    begin = text.index(r'\begin{itemize}', start) + len(r'\begin{itemize}')
    end = text.index(r'\end{itemize}', begin)
    entries = [line for line in text[begin:end].splitlines() if line.startswith(r'\item ')]
    if not entries:
        raise RuntimeError(root)
    entries.sort(key=lambda s: (s[6:].split('.', 1)[0].casefold(), s))
    path.write_text(text[:begin] + '\n' + '\n'.join(entries) + '\n\n' + text[end:], encoding='utf-8')
    print(root, len(entries))
