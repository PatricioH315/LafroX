from pathlib import Path
import json
from pypdf import PdfReader

root = Path('Datos externos/Informe_2_LafroX')
out = Path('tmp/revision_riesgos_fuentes/pages.jsonl')
files = sorted(root.rglob('*.pdf'))
with out.open('w', encoding='utf-8') as f:
    for path in files:
        reader = PdfReader(str(path))
        rel = str(path.relative_to(root))
        for n, page in enumerate(reader.pages, 1):
            text = page.extract_text() or ''
            f.write(json.dumps({'file': rel, 'page': n, 'text': text}, ensure_ascii=False) + '\n')
        print(f'{rel}: {len(reader.pages)} pages', flush=True)
