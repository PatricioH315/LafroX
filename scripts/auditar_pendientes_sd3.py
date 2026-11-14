"""Inventario reproducible de trazabilidad; no emite dictámenes semánticos."""
from __future__ import annotations

import csv
import json
import re
import subprocess
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SD7 = 'origin/LafroX-Subdoc7-LateX-CORRIGIENDO'
SD9 = 'origin/LafroX-Subdoc9-LateX-corrigiendo'
T13 = 'SD9_v_nueva/T13/matriz_requisitos.tex'
IDENT = re.compile(r'^\s*((?:RF|RNF|RT)-\d{2}\.\d{2}(?:-BTT)?)\s*&')


def git(ref, path):
    return subprocess.check_output(['git', 'show', f'{ref}:{path}'], cwd=ROOT).decode('utf-8')


def rows(text):
    out = {}
    for line in text.splitlines():
        m = IDENT.match(line)
        if not m:
            continue
        cells = [s.strip() for s in line.strip().removesuffix(r'\\').split(' & ')]
        if m[1] in out:
            raise ValueError(f'Identificador repetido: {m[1]}')
        out[m[1]] = cells
    return out


def plain(s):
    return re.sub(r'\s+', ' ', s.replace(r'\allowbreak{}', '').replace(r'\_', '_')).strip()


def comparable(s):
    normalized = unicodedata.normalize('NFKD', plain(s).lower())
    return re.sub(r'[^a-z0-9]', '', normalized)


def main():
    t12 = rows((ROOT / 'LAFROX-Formulario-T-12.tex').read_text(encoding='utf8'))
    assert len(t12) == 653 and all(len(v) == 6 for v in t12.values())
    catalogs = {}
    for name in ['rf_caso.tex', 'rf_btt.tex', 'rf_propios.tex', 'rnf_caso.tex', 'rnf_btt.tex', 'rnf_propios.tex']:
        for ident, fields in rows((ROOT / 'tablas_anexo' / name).read_text(encoding='utf8')).items():
            if ident in catalogs:
                raise ValueError(f'Identificador de catálogo repetido: {ident}')
            catalogs[ident] = (name, fields)
    assert len(catalogs) == 270

    matrix = {}
    aliases = {}
    for line in git(SD9, T13).replace(r'\allowbreak{}', '').splitlines():
        m = re.match(r'\\textbf\{((?:RF|RNF|RT)-\d{2}\.\d{2}(?:-BTT)?)\}', line)
        if m:
            cells = line.split(' & ')
            if len(cells) != 4 or m[1] in matrix:
                raise ValueError(f'Fila T13 ambigua: {m[1]}')
            matrix[m[1]] = cells
        elif (m := re.match(r'((?:RF|RNF)-\d{2}\.\d{2}(?:-BTT)?)\s+&', line)):
            cells = line.split(' & ')
            if len(cells) == 3 and cells[-1].strip().startswith('0'):
                aliases[m[1]] = cells
    assert len(matrix) == 644 and len(aliases) == 9

    paths = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', SD7], cwd=ROOT).decode('utf8').splitlines()
    packages = {}
    for path in paths:
        if not path.startswith('formulario-t14/') or not path.endswith('.tex'):
            continue
        for line in git(SD7, path).splitlines():
            m = re.match(r'\s*(\d+(?:\.\d+){1,3})\s+&\s*(.*?)\s+&', line)
            if m:
                packages.setdefault(m[1], []).append((path, m[2]))
    hierarchy = git(SD7, 'formulario-t14/contenido.tex')
    accounts = {}
    for line in hierarchy.splitlines():
        m = re.match(r'\\item\s+(\d+(?:\.\d+){1,3})\s+(.+)', line)
        if m:
            accounts[m[1]] = m[2]

    old = json.loads((ROOT / 'revision/semantica_t12_2026-10-25/matriz_revision.json').read_text(encoding='utf8'))
    previous = {r['id']: r for r in old['filas']}
    data = []
    for ident, fields in t12.items():
        requirement, state, component, edt, refs = fields[1:]
        cat = catalogs.get(ident)
        expected = cat[1][4 if ident.startswith('RF-') else 2] if cat else ''
        origin = cat[1][-1] if cat else ('BTT '+ident if ident.startswith('RT-') else 'Ver tabla de alias 3.A.3a/3.A.5a')
        if ident.startswith('RT-') and 'Caso, cap. 15' in requirement:
            origin += '; Caso, cap. 15: ' + ident
        target = matrix.get(ident)
        t13state = t13edt = test = criterion = t13origin = t13component = ''
        if target:
            t13origin = plain(target[0].split(r'\newline', 1)[-1])
            t13component = plain(target[1].split(r'\newline \textbf{EDT:}')[0])
            hit = re.search(r'\\textbf\{EDT:\}\s*(.*)', target[1])
            t13edt = plain(hit[1]) if hit else ''
            test = plain(target[2].split(r'\newline')[0])
            hit = re.search(r'\\newline\s*(Parcial|No cumple|Cumple)', target[2])
            t13state = {'Parcial':'Cumple parcialmente','No cumple':'No cumple','Cumple':'Cumple'}.get(hit[1], '') if hit else ''
            criterion = plain(target[3].split(r'\newline \emph{')[0])
        codes = re.findall(r'(?<![\d.])\d+(?:\.\d+){1,3}(?![\d.])', edt)
        names = []
        for code in codes:
            hits=packages.get(code, [])
            names.append(code + ': ' + (' / '.join(sorted({x[1] for x in hits})) if hits else ('[cuenta o grupo: ' + accounts[code] + ']' if code in accounts else '[sin fila de diccionario encontrada]')))
        former = previous.get(ident, {})
        data.append({
            'id': ident, 'exigencia': requirement, 'estado': state, 'componente': component,
            'origen_declarado': origin, 'catalogo': cat[0] if cat else '', 'resultado_catalogo': expected,
            'edt_t12': edt, 'paquetes_t14': ' | '.join(names), 'referencias_t12': refs,
            'tipo_t13': 'ficha' if target else ('alias' if ident in aliases else 'ausente'),
            'estado_t13': t13state, 'componente_t13': t13component, 'edt_t13': t13edt, 'casos_previstos_t13': test,
            'estado_coincide_t13': str(state == t13state) if target else 'No aplica: alias',
            'componente_coincide_t13': str(plain(component) == t13component) if target else 'No aplica: alias',
            'edt_coincide_t13': str(plain(edt) == t13edt) if target else 'No aplica: alias',
            'origen_t13': t13origin, 'origen_coincide_t13': str(comparable(origin) == comparable(t13origin)) if target and cat else 'No comparado',
            'criterio_t13': criterion, 'criterio_coincide_catalogo': str(comparable(expected) == comparable(criterion)) if target and cat else 'No comparado',
            'version_revision_previa': old['revision']['fecha'] if former else '',
            'dictamen_previo': former.get('dictamen',''),
            'exigencia_cambio_desde_revision_previa': str(plain(former.get('exigencia','')) != plain(requirement)) if former else 'sin antecedente',
            'respuesta_cambio_desde_revision_previa': str(plain(former.get('respuesta_final','')) != plain(component)) if former else 'sin antecedente',
            'estado_cambio_desde_revision_previa': str(former.get('estado_final','') != state) if former else 'sin antecedente',
            'revision_semantica_actual': 'Pendiente de cotejo individual',
        })
    output = ROOT / 'trazabilidad' / 'auditoria_pendientes_sd3.csv'
    with output.open('w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(data[0]))
        writer.writeheader(); writer.writerows(data)
    print(json.dumps({'filas':len(data),'catalogos':len(catalogs),'fichas':len(matrix),'alias':len(aliases),
                      'paquetes_sin_fila':Counter(x for row in data for x in row['paquetes_t14'].split(' | ') if '[sin fila' in x),
                      'referencias_a_cuentas':Counter(x for row in data for x in row['paquetes_t14'].split(' | ') if '[cuenta o grupo:' in x),
                      'estado_t13_distinto': [row['id'] for row in data if row['estado_coincide_t13'] == 'False'],
                      'edt_t13_distinto': [row['id'] for row in data if row['edt_coincide_t13'] == 'False'],
                      'origen_t13_distinto': [row['id'] for row in data if row['origen_coincide_t13'] == 'False'],
                      'criterio_t13_distinto': [row['id'] for row in data if row['criterio_coincide_catalogo'] == 'False'],
                      'estados':Counter(row['estado'] for row in data),
                      'cambio_respuesta':Counter(row['respuesta_cambio_desde_revision_previa'] for row in data),
                      'cambio_exigencia':Counter(row['exigencia_cambio_desde_revision_previa'] for row in data),
                      'cambio_estado':Counter(row['estado_cambio_desde_revision_previa'] for row in data)},ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
