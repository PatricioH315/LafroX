"""Contrasta proveedor, referencias y esfuerzo con las fuentes canónicas de origin.

Solo lee fuentes y PDF. No modifica otros subdocumentos ni declara pruebas TLS.
"""
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
import argparse
import json
import re
import subprocess

from pypdf import PdfReader


def verify(workspace):
    sd4 = workspace / 'tmp/sd4-corrigiendo-integracion'
    sd10 = Path(__file__).resolve().parents[1]

    def published(branch, path):
        return subprocess.check_output(
            ['git', '-C', str(sd4), 'show', f'origin/{branch}:{path}']
        ).decode('utf-8-sig')

    def read(path):
        return path.read_text(encoding='utf-8-sig')

    provider = 'AWS End User Messaging Social'
    t12 = published('LafroX-Subdoc3-LateX-CORRIGIENDO', 'LAFROX-Formulario-T-12.tex')
    t13 = published('LafroX-Subdoc9-LateX-corrigiendo', 'SD9_v_nueva/T13/matriz_requisitos.tex')
    for name, text in [('T-12', t12), ('T-13', t13)]:
        rows = [line for line in text.splitlines() if re.search(
            r'^\s*(?:\\textbf\{)?RT-(?:\\allowbreak\{\})?16\.20(?:\}|[ \t]*&)', line)]
        assert len(rows) == 1, f'{name}: no se identifica una fila única de RT-16.20'
        assert provider in rows[0], f'{name}: cambió el proveedor canónico de RT-16.20'

    profiles = published('LafroX-Subdoc7-LateX-CORRIGIENDO',
                         'formulario-t15/tablas/tab_T15_perfiles_internos.tex')
    row = next(line for line in profiles.splitlines() if line.startswith('24 & SRE &'))
    total = int(row.split('&')[7].strip().replace('.', ''))
    economic = published('LafroX-OfertaEconomica-2-Latex',
                         '02_analisis_economico_financiero/secciones/2-6_mantencion_soporte.tex')
    match = re.search(r'con ([\d.]+) HH en la Operación', economic)
    assert match and int(match[1].replace('.', '')) == total, 'T-15 y E2 no coinciden'
    average = (Decimal(total) / 36).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
    formatted_total = f'{total:,}'.replace(',', '.')
    formatted_average = str(average).replace('.', ',')

    directories = [(sd4 / '04' / name) for name in ('partes', 'anexos', 'formularios')]
    directories += [sd10 / '10_servicios_operacion', sd10 / '10_anexos']
    source_count = 0
    for directory in directories:
        for path in directory.rglob('*.tex'):
            text = read(path)
            assert not re.search(r'whatsapp|developers\.facebook\.com|Graph API', text, re.I), path
            assert chr(167) not in text, path
            source_count += 1

    for name in (
        '04/partes/4.1_logica/04_capas_de_la_arquitectura.tex',
        '04/anexos/logica/partes/09_anexo_4_1_h_catalogo_de_interfaces_externas.tex',
        '04/formularios/T11/15_anexo_t11.tex',
    ):
        assert provider in read(sd4 / name), name

    service = read(sd10 / '10_servicios_operacion/partes/10_1_servicios.tex')
    annex = read(sd10 / '10_anexos/contenido.tex')
    for text in (service, annex):
        assert f'{formatted_total} HH' in text
        assert formatted_average in text
    assert 'La programación mensual del T-15 prevé 128 HH' not in service
    assert 'Para Redes/NOC, SD4 (Anexo 4-W.7)' in annex
    assert 'Las guías de este Anexo 10.C' in annex
    assert 'apartado 4.2.4.1.4' in annex
    assert not re.search(r'Anexo\s+4-B\b', annex)

    pdfs = [sd4 / 'entrega' / name for name in (
        'LAFROX-Subdocumento4.pdf', 'LAFROX-Subdocumento4-Anexos.pdf',
        'LAFROX-Formulario-T-11.pdf')]
    pdfs += [sd10 / name for name in (
        'LAFROX-Subdocumento10.pdf', 'LAFROX-Subdocumento10-Anexos.pdf')]
    counts = {}
    for path in pdfs:
        reader = PdfReader(path)
        text = '\n'.join(page.extract_text() or '' for page in reader.pages)
        text = re.sub(r'-\s*\n\s*', '', text).replace('\u00ad', '')
        assert not re.search(r'what\s*sapp|developers\.facebook\.com|Graph API', text, re.I), path
        assert '??' not in text, path
        if path.parent == sd10:
            assert formatted_total in text and formatted_average in text, path
        counts[path.name] = len(reader.pages)

    return {'proyecto': 'LafroX', 'passed': True, 'fuentes_comprobadas': source_count,
            'proveedor_RT_16_20': provider, 'gerente_HH_operacion': total,
            'gerente_promedio_HH_mes': str(average), 'paginas': counts,
            'limite': 'Coherencia documental; no acredita TLS 1.3 del recorrido administrado ni ensayos ejecutados.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    print(json.dumps(verify(args.workspace), ensure_ascii=False, indent=2))
