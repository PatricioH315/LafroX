"""Localiza fuentes citadas en 3.A.1; la existencia no certifica suficiencia semántica."""
from __future__ import annotations

import csv
import re
import subprocess
from pathlib import Path

from auditar_pendientes_sd3 import ROOT, bases_rt, rows

SD2 = 'origin/LafroX-Subdoc2-LateX-CORRIGIENDO'
SD4 = 'origin/LafroX-Subdoc4-LateX-corrigiendo'


def git(ref, path):
    return subprocess.check_output(['git', 'show', f'{ref}:{path}'], cwd=ROOT).decode('utf-8')


def main():
    caso = git(SD4, 'Bases/Caso_02_Logistica.md')
    sd2 = git(SD2, 'anexos.tex') + '\n' + git(SD2, 'contenido.tex')
    sd2_version = subprocess.check_output(['git', 'rev-parse', SD2], cwd=ROOT, text=True).strip()
    sd4_version = subprocess.check_output(['git', 'rev-parse', SD4], cwd=ROOT, text=True).strip()
    btt_rt, caso_rt = bases_rt()
    headings = dict(re.findall(r'^#{2,4}\s+(\d+\.\d+)\s+([^\n]+)', caso, re.M))
    chapters = set(re.findall(r'^#{2,4}\s+CAP[IÍ]TULO\s+(\d+)\b', caso, re.M | re.I))
    catalog = rows((ROOT / 'tablas_anexo/rf_caso.tex').read_text(encoding='utf8'))
    assert len(catalog) == 134
    results = []
    for ident, cells in catalog.items():
        origin = cells[-1]
        case_part = origin.split(';', 1)[0] if origin.startswith('Caso,') else ''
        section_ids = list(dict.fromkeys(re.findall(r'(?<![\w-])(\d+\.\d+)(?![\w.])', case_part)))
        chapter_groups = re.findall(r'cap(?:s)?\.\s*([\d,\s]+(?:y\s+\d+)?)', case_part)
        chapter_ids = list(dict.fromkeys(x for group in chapter_groups for x in re.findall(r'\d+', group)))
        # Capítulo 15 comparte numeración RT con BTT, pero tiene exigencias distintas.
        in_parentheses = re.findall(r'cap\.\s*15\s*\(([^)]*)\)', case_part)
        case_codes = list(dict.fromkeys(re.findall(r'RT-\d{2}\.\d{2}', ' '.join(in_parentheses))))
        btt_part = origin.split('BTT,', 1)[1].split(';', 1)[0] if 'BTT,' in origin else ''
        btt_codes = list(dict.fromkeys(re.findall(r'RT-\d{2}\.\d{2}', btt_part)))
        sd2_part = origin.split('SD2,', 1)[1].split(';', 1)[0] if 'SD2,' in origin else ''
        sd2_codes = list(dict.fromkeys(re.findall(r'(?<![\w-])[FS]-\d{2}(?!\d)', sd2_part)))
        missing = ([f'Caso §{x}' for x in section_ids if x not in headings]
                   + [f'Caso cap. {x}' for x in chapter_ids if x not in chapters]
                   + [f'Caso {x}' for x in case_codes if x not in caso_rt]
                   + [f'BTT {x}' for x in btt_codes if x not in btt_rt]
                   + [f'SD2 {x}' for x in sd2_codes if not re.search(r'(?<![\w-])' + re.escape(x) + r'(?!\d)', sd2)])
        results.append({
            'id': ident, 'requisito': cells[2], 'origen_declarado': origin,
            'apartados_caso': ' | '.join(f'{x} {headings.get(x, "[NO LOCALIZADO]")}' for x in section_ids),
            'capitulos_caso': ', '.join(chapter_ids), 'rt_caso': ', '.join(case_codes),
            'rt_btt': ', '.join(btt_codes), 'codigos_sd2': ', '.join(sd2_codes),
            'localizadores_no_encontrados': ' | '.join(missing),
            'alcance_comprobacion': 'Localización automática; suficiencia semántica pendiente de revisión individual',
            'version_sd2': sd2_version, 'version_sd4': sd4_version,
        })
    out = ROOT / 'trazabilidad/localizacion_origenes_3a1.csv'
    with out.open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    print(f'{len(results)} filas. Localizadores no encontrados:')
    for row in results:
        if row['localizadores_no_encontrados']:
            print(row['id'], row['localizadores_no_encontrados'], '|', row['origen_declarado'])


if __name__ == '__main__':
    main()
