from pathlib import Path
import re

for root in ('subdocumento-07', 'subdocumento-07-anexos', 'formulario-t14', 'formulario-t15', 'formulario-t18'):
    path = Path(root) / 'contenido.tex'
    source = path.read_text(encoding='utf-8')
    body = '\n'.join(line for line in source.splitlines() if not line.lstrip().startswith(r'\item LafroX'))
    body += '\n' + '\n'.join(p.read_text(encoding='utf-8') for p in (Path(root) / 'tablas').glob('*.tex'))
    cites = set(re.findall(r'LafroX\s*\(?2026([a-z])', body)) | set(re.findall(r'LafroX,\s*2026([a-z])', body))
    refs = set(re.findall(r'\\item LafroX\. \(2026([a-z])\)', source))
    print(root, 'cites=' + ''.join(sorted(cites)), 'refs=' + ''.join(sorted(refs)), 'missing=' + ''.join(sorted(cites-refs)), 'unused=' + ''.join(sorted(refs-cites)))

for name in ('LafroX-Subdocumento7.md', 'LafroX-Subdocumento7-Anexos.md', 'LafroX-Formulario-T-14.md', 'LafroX-Formulario-T-15.md', 'LafroX-Formulario-T-18.md'):
    text = Path(name).read_text(encoding='utf-8')
    body = text[:text.rfind('\nReferencias\n')]
    cites = set(re.findall(r'LafroX\s*\(?2026([a-z])', body)) | set(re.findall(r'LafroX,\s*2026([a-z])', body))
    refs = set(re.findall(r'[•-]\s+LafroX\. \(2026([a-z])\)', text))
    print(name, 'cites=' + ''.join(sorted(cites)), 'refs=' + ''.join(sorted(refs)), 'missing=' + ''.join(sorted(cites-refs)), 'unused=' + ''.join(sorted(refs-cites)))
