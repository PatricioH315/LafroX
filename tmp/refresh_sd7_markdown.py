from pathlib import Path
import subprocess

titles = {
    'Subdocumento7': 'Subdocumento 7 — Plan de trabajo',
    'Subdocumento7-Anexos': 'Subdocumento 7 — Anexos',
    'Formulario-T-14': 'Formulario T-14 — Estructura de desglose del trabajo',
    'Formulario-T-15': 'Formulario T-15 — Cronograma y asignación de recursos',
    'Formulario-T-18': 'Formulario T-18 — Implantación de la solución',
}

for stem, title in titles.items():
    pdf = Path(f'LafroX-{stem}.pdf')
    md = pdf.with_suffix('.md')
    extraction = subprocess.check_output(['pdftotext', '-raw', '-enc', 'UTF-8', str(pdf), '-'])
    body = extraction.decode('utf-8-sig').replace('\r\n', '\n').replace('\f', '\n\n---\n\n').strip()
    where = body.rfind('\nReferencias\n')
    if where < 0:
        raise RuntimeError(f'No references in {pdf}')
    body = body[:where] + body[where:].replace('\nReferencias\n', '\n## Referencias\n', 1)
    md.write_text(f'# {title}\n\n> Texto extraído del [PDF final]({pdf.name}). Las figuras y la composición visual se consultan en el PDF.\n\n{body}\n', encoding='utf-8')
    print(md, len(body.splitlines()), 'lines')
