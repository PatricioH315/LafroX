"""Contrasta SD10 con el diseño vigente de SD4 y las fuentes publicadas.

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

    record = json.loads(read(sd10 / 'trazabilidad/canonicos_sd4_sd10_20261124.json'))
    provider = record['proveedor_mensajeria_instantanea']
    external_differences = []

    def requirement_row(text, code, name):
        rows = [line for line in text.splitlines() if re.search(
            r'^\s*(?:\\textbf\{)?RT-(?:\\allowbreak\{\})?'
            + re.escape(code) + r'(?:\}|[ \t]*&)', line)]
        assert len(rows) == 1, f'{name}: no se identifica una fila única de RT-{code}'
        return rows[0]

    t12 = published('LafroX-Subdoc3-LateX-CORRIGIENDO', 'LAFROX-Formulario-T-12.tex')
    t13 = published('LafroX-Subdoc9-LateX-corrigiendo', 'SD9_v_nueva/T13/matriz_requisitos.tex')
    for name, text in [('T-12', t12), ('T-13', t13)]:
        # RT-16.24 declara proveedores; RT-16.20 exige cobertura multicanal.
        row = requirement_row(text, '16.24', name)
        assert provider in row, f'{name}: RT-16.24 no coincide con el proveedor de SD4'
        coverage = requirement_row(text, '16.20', name)
        if 'AWS End User Messaging Social' in coverage and provider not in coverage:
            external_differences.append({
                'fuente': name, 'requisito': 'RT-16.20',
                'estado': 'pendiente_en_fuente_externa',
                'detalle': 'La descripción conserva el proveedor anterior; RT-16.24 y SD4 identifican Meta.'})

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
    assert record['gerente_HH_operacion'] == total, 'Trazabilidad: HH distintas de T-15 y E2'
    assert record['promedio_HH_mes'] == formatted_average, 'Trazabilidad: promedio mensual distinto'
    assert record['horas_adicionales_incorporadas'] == 0, 'No se deben agregar horas al consolidado'

    directories = [(sd4 / '04' / name) for name in ('partes', 'anexos', 'formularios')]
    directories += [sd10 / '10_servicios_operacion', sd10 / '10_anexos']
    source_count = 0
    for directory in directories:
        for path in directory.rglob('*.tex'):
            text = read(path)
            assert chr(167) not in text, path
            source_count += 1

    for name in (
        '04/anexos/logica/partes/09_anexo_4_1_h_catalogo_de_interfaces_externas.tex',
        '04/formularios/T11/15_anexo_t11.tex',
    ):
        text = read(sd4 / name)
        assert provider in text and 'Amazon SES' in text and 'Amazon SNS' in text, name
        assert 'AWS End User Messaging Social' not in text, name

    layers = read(sd4 / '04/partes/4.1_logica/04_capas_de_la_arquitectura.tex')
    assert 'WhatsApp mediante la API Cloud de Meta' in layers
    security = read(sd4 / '04/anexos/logica/partes/21_anexo_4_1_r_controles_seguridad.tex')
    direct = security.split(r'\paragraph{WhatsApp Cloud API directa}', 1)
    assert len(direct) == 2, 'Falta la integración directa del Anexo 4-R'
    for term in ('Graph API mediante TLS 1.3', 'El webhook de estados',
                 r'TLSv1.3\_2025', 'acepta exclusivamente TLS 1.3',
                 'Antes de habilitar el canal', 'T-13', 'firma', 'correlación', 'deduplicación'):
        assert term in direct[1], f'Anexo 4-R: falta {term}'

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
        assert '??' not in text, path
        if path.parent == sd10:
            assert formatted_total in text and formatted_average in text, path
        else:
            compact = re.sub(r'\W', '', text.casefold())
            assert 'whatsapp' in compact, f'{path.name}: no refleja el canal de SD4'
            if path.name != 'LAFROX-Subdocumento4.pdf':
                assert re.sub(r'\W', '', provider.casefold()) in compact, path
        counts[path.name] = len(reader.pages)

    return {'proyecto': 'LafroX', 'passed': True, 'alcance': 'Controles internos de SD4 y SD10',
            'fuentes_comprobadas': source_count, 'proveedor_RT_16_24': provider,
            'diferencias_fuera_alcance': external_differences,
            'proveedor_coherente_en_t12_t13': not external_differences,
            'gerente_HH_operacion': total,
            'gerente_promedio_HH_mes': str(average), 'paginas': counts,
            'limite': 'Diseño TLS 1.3 documentado; no acredita negociación real ni ensayos ejecutados. Las diferencias externas se informan sin modificar esas fuentes.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--output', type=Path, help='Guardar el resultado de la verificación')
    args = parser.parse_args()
    result = json.dumps(verify(args.workspace), ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(result + '\n', encoding='utf-8', newline='\n')
    print(result)
