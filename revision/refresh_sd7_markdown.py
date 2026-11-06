"""Extrae el texto de los cinco PDF; los diagramas se consultan en el PDF.

Usa pypdf del runtime, evitando la dependencia implícita del pdftotext de MiKTeX.
"""
from pathlib import Path
import subprocess
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
branch = subprocess.check_output(['git', 'branch', '--show-current'], cwd=ROOT, text=True).strip()
if branch != 'LafroX-Subdoc7-LateX-CORRIGIENDO':
    raise RuntimeError('Rama no autorizada para regenerar entregables: ' + branch)

titles = {
    'Subdocumento7': 'Subdocumento 7 — Plan de trabajo, EDT, cronograma e implantación',
    'Subdocumento7-Anexos': 'Anexos del Subdocumento 7',
    'Formulario-T-14': 'Formulario T-14 — Plan de trabajo, EDT y carta Gantt',
    'Formulario-T-15': 'Formulario T-15 — Nivelación de recursos',
    'Formulario-T-18': 'Formulario T-18 — Propuesta de implantación y puesta en marcha controlada',
}

for stem, title in titles.items():
    pdf = ROOT / f'LAFROX-{stem}.pdf'
    md = pdf.with_suffix('.md')
    body = '\n\n---\n\n'.join((p.extract_text() or '').strip() for p in PdfReader(pdf).pages).strip()
    body = '\n'.join(line.rstrip() for line in body.splitlines())
    where = body.rfind('\nReferencias\n')
    if where < 0:
        raise RuntimeError(f'No references in {pdf}')
    body = body[:where] + body[where:].replace('\nReferencias\n', '\n## Referencias\n', 1)
    md.write_text(f'# {title}\n\n> Texto extraído del [PDF final]({pdf.name}). Las figuras y la composición visual se consultan en el PDF.\n\n{body}\n', encoding='utf-8')
    print(md, len(body.splitlines()), 'lines')
