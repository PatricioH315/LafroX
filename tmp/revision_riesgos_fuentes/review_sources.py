from pathlib import Path
import json, re
from collections import defaultdict

rows = [json.loads(line) for line in Path('tmp/revision_riesgos_fuentes/pages.jsonl').read_text(encoding='utf-8').splitlines()]
terms = {
    'SII tributario': r'\bSII\b|tributari|DTE',
    'avisos': r'aviso|notificaci[oó]n|mensajer[ií]a',
    'GIS': r'\bGIS\b|cuota|mapas|geocodific',
    'transportistas': r'transportista|acuerdo operacional|acuerdo de operaci[oó]n',
    'termografo': r'term[oó]graf|cadena de fr[ií]o',
    'certificacion': r'certificaci[oó]n de usuarios|evaluaci[oó]n de usuarios|formaci[oó]n',
    'energia': r'corte de energ[ií]a|corte el[eé]ctrico|autonom[ií]a|\bUPS\b',
    'residencia': r'residencia|transferencia de datos|ADR-19',
    'credenciales': r'credencial|token ajeno|suplantaci[oó]n|M3\b',
    'EDI': r'\bEDI\b|OpenAS2|cadena autorizada',
    'telemetria': r'telemetr[ií]a|\bGPS\b|posici[oó]n|INT-15',
}
out = []
for topic, pattern in terms.items():
    rx = re.compile(pattern, re.I)
    hits = defaultdict(list)
    for row in rows:
        if rx.search(row['text']):
            hits[row['file']].append(row['page'])
    out.append(f'## {topic}')
    for file, pages in hits.items():
        out.append(f'- {file}: {", ".join(map(str,pages[:40]))}' + (' ...' if len(pages)>40 else ''))
    out.append('')
Path('tmp/revision_riesgos_fuentes/review_hits.md').write_text('\n'.join(out),encoding='utf-8')
print(len(rows), 'pages', len({r['file'] for r in rows}), 'files')
