"""Actualiza los controles quincenales de construcción en T-15 y GanttProject."""

import argparse
import calendar
from collections import defaultdict
from datetime import date
from pathlib import Path
import re
from xml.etree import ElementTree as ET

from edt_cpm_20261117 import CAL, ROOT, START, build

DETAIL = 'Fig_7_Gantt_Resumen_Dependencias.gan'
REVIEW = 'Seguimiento de construcción'
DELIVERY = 'Entrega a QA'
DEMO = 'Demostración de módulos en QA'
ROOTS = {
    'Inicio contractual (supuesto V-12)': ('1.1.1', '2.4.1'),
    'Especificación de equipos de frío disponible (SD4)': ('8.1.4',),
}


def controls(packages):
    by_stage = {'E1': {}, 'E2': {}}
    for code, row in packages.items():
        if not code.startswith('4.'):
            continue
        stage = 'E2' if code.startswith('4.4.') or code == '4.5.2' else 'E1'
        by_stage[stage][code] = row
    for stage, modules in by_stage.items():
        first = min(row['start'] for row in modules.values())
        last = max(row['finish'] for row in modules.values())
        previous = date(first.year, first.month, 1)
        for day in (d for d in CAL if first <= d <= last):
            end = date(day.year, day.month, 15 if day.day <= 15 else calendar.monthrange(day.year, day.month)[1])
            if day != max(d for d in CAL if d <= end) and day != last:
                continue
            active = [code for code, row in modules.items() if row['start'] <= day and row['finish'] >= previous]
            ready = [code for code, row in modules.items() if previous <= row['finish'] <= day]
            if active:
                yield stage, day, active, ready
            previous = CAL[CAL.index(day) + 1]


def export_detail(origin, output, packages, checkpoints):
    parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
    tree = ET.parse(origin, parser=parser)
    task_list = tree.getroot().find('tasks')
    items = task_list.findall('task')
    previous = {item.get('id') for item in items if item.get('name').startswith(
        (REVIEW, DELIVERY, DEMO, *ROOTS))}
    for item in items:
        if item.get('id') in previous:
            task_list.remove(item)
    items = task_list.findall('task')
    next_id = max(int(item.get('id')) for item in items) + 1
    by_code = {}
    for item in items:
        match = re.match(r'^(\d+\.\d+\.\d+) ', item.get('name'))
        if match and item.get('meeting') == 'false':
            by_code[match[1]] = item

    def milestone(title, day, note):
        nonlocal next_id
        item = ET.SubElement(task_list, 'task', id=str(next_id), name=title, color='#735423',
                             meeting='true', start=day.isoformat(), duration='0', complete='0', expand='true')
        next_id += 1
        ET.SubElement(item, 'notes').text = note
        ET.SubElement(item, 'customproperty', {'taskproperty-id': 'tpc2', 'value': '0'})
        return item

    for name, successors in ROOTS.items():
        item = milestone(name, START, 'Fecha nominal. JP confirma V-12; ARQ verifica el insumo externo antes de 8.1.4.')
        for code in successors:
            ET.SubElement(item, 'depend', id=by_code[code].get('id'), type='1', difference='0', hardness='Rubber')

    for stage, day, active, ready in checkpoints:
        milestone(f'{REVIEW} {stage} · {day:%d/%m/%Y}', day,
                  f'Líder de Desarrollo. Acta: estado, horas, pruebas de código y bloqueos. EDT: {", ".join(active)}.')
        if ready:
            milestone(f'{DEMO} {stage} · {day:%d/%m/%Y}', day,
                      f'Líder Funcional y Calidad. Registro de versión y observaciones. EDT: {", ".join(ready)}.')
    for code in sorted({code for _, _, _, group in checkpoints for code in group}):
        milestone(f'{DELIVERY} · {code}', packages[code]['finish'],
                  'Líder de Desarrollo y Calidad. Evidencia: versión desplegada e integración registrada.')
    ET.indent(tree, space='    ')
    tree.write(output, encoding='utf-8', xml_declaration=True)


def export_table(output, checkpoints):
    lines = [
        r'\begin{tablalafrox}{Controles quincenales de construcción y demostraciones. Fuente: fechas niveladas de la sección 6.1.}{tab:T15-controles-qa}',
        r'{L{1cm} L{2.1cm} Y Y}',
        r'{\cab{Etapa} & \cab{Revisión y demo} & \cab{Paquetes en seguimiento} & \cab{Entregas a QA para demostrar}}',
    ]
    for stage, day, active, ready in checkpoints:
        lines.append(' & '.join((stage, day.strftime('%d-%m-%Y'), ', '.join(active),
                                 ', '.join(ready) or 'Sin entrega en la quincena')) + r' \\')
    lines.append(r'\end{tablalafrox}')
    output.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    _, _, _, packages, _, _, _ = build()
    checkpoints = list(controls(packages))
    assert {code for _, _, _, codes in checkpoints for code in codes} == {
        code for code in packages if code.startswith('4.')
    }
    origin = ROOT / 'imagenes/Diagramas que faltaban' / DETAIL
    directory = args.output_dir
    directory.mkdir(parents=True, exist_ok=True)
    export_detail(origin, directory / DETAIL, packages, checkpoints)
    export_table(directory / 'tab_T15_controles_qa.tex', checkpoints)
    print(f'{len(checkpoints)} revisiones y 15 entregas a QA')


if __name__ == '__main__':
    main()
